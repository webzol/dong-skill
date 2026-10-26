#!/usr/bin/env python3
"""把正文 HTML 里的 {{IMG_*}} 占位符替换成 base64 data URI，并做结构检查。

用法：
    python inject_images.py body.html images.json out.html
    python inject_images.py body.html images.json out.html --allow-missing-captions

images.json：
    {
      "{{IMG_A}}": "C:/shots/a.png",
      "{{IMG_B}}": "C:/shots/b.jpg"
    }

规则：
- 全部占位符必须命中，任一缺失直接失败（不产出半成品）；
- 替换完仍有 {{ 残留 → 失败；
- 每张图下方必须有 12px #8a8a8a 居中图注，数量对不上 → 失败（exit 5）；
  确实不要图注时加 --allow-missing-captions；
- 输出 UTF-8 单文件，图片按原格式内联（png/jpg/webp）。
"""
import base64
import json
import mimetypes
import os
import re
import sys


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    allow_missing = '--allow-missing-captions' in sys.argv
    if len(args) < 3:
        print(__doc__)
        sys.exit(1)
    body_path, map_path, out_path = args[:3]

    html = open(body_path, encoding='utf-8-sig').read()
    mapping = json.load(open(map_path, encoding='utf-8-sig'))

    total = 0
    for token, img in mapping.items():
        if token not in html:
            print(f'✗ 占位符未出现在正文里: {token}')
            sys.exit(2)
        if not os.path.isfile(img):
            print(f'✗ 图片不存在: {img}')
            sys.exit(3)
        mime = mimetypes.guess_type(img)[0] or 'image/png'
        b64 = base64.b64encode(open(img, 'rb').read()).decode()
        html = html.replace(token, f'data:{mime};base64,{b64}')
        total += len(b64)
        print(f'✓ {token} ← {os.path.basename(img)} ({len(b64)} b64 chars)')

    if '{{' in html:
        left = html[html.index('{{'):html.index('{{') + 40]
        print(f'✗ 仍有未替换占位符: {left}')
        sys.exit(4)

    # 结构检查：每张图后面（下一张图之前）必须紧跟一条 12px #8a8a8a 图注
    imgs = [m.end() for m in re.finditer(r'<img\b[^>]*>', html)]
    missing = []
    for i, pos in enumerate(imgs):
        nxt = imgs[i + 1] if i + 1 < len(imgs) else len(html)
        window = html[pos:min(nxt, pos + 1500)]
        if not re.search(r'<p[^>]*font-size:\s*12px[^>]*color:\s*#8a8a8a'
                         r'|<p[^>]*color:\s*#8a8a8a[^>]*font-size:\s*12px', window):
            missing.append(i + 1)

    if missing:
        msg = (f'✗ 第 {", ".join(map(str, missing))} 张图后面没有 12px 灰色居中图注'
               f'（共 {len(imgs)} 张图）。\n'
               f'  每张图下方都要有一条「这张图证明什么」的图注（§5 排版规范）。')
        if allow_missing:
            print('⚠ ' + msg.split('\n')[0] + '（已用 --allow-missing-captions 放行）')
        else:
            print(msg)
            sys.exit(5)
    else:
        print(f'✓ 一图一注：{len(imgs)} 张图全部带图注')

    open(out_path, 'w', encoding='utf-8').write(html)
    print(f'✓ {out_path}  {os.path.getsize(out_path)} bytes  (b64 {total})')


if __name__ == '__main__':
    main()
