#!/usr/bin/env python3
"""把正文 HTML 里的 {{IMG_*}} 占位符替换成 base64 data URI。

用法：
    python inject_images.py body.html images.json out.html

images.json：
    {
      "{{IMG_A}}": "C:/shots/a.png",
      "{{IMG_B}}": "C:/shots/b.jpg"
    }

规则：
- 全部占位符必须命中，任一缺失直接失败（不产出半成品）；
- 替换完仍有 {{ 残留 → 失败；
- 输出 UTF-8 单文件，图片按原格式内联（png/jpg/webp）。
"""
import base64
import json
import mimetypes
import os
import sys


def main():
    if len(sys.argv) < 4:
        print(__doc__)
        sys.exit(1)
    body_path, map_path, out_path = sys.argv[1:4]

    html = open(body_path, encoding='utf-8').read()
    mapping = json.load(open(map_path, encoding='utf-8'))

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

    open(out_path, 'w', encoding='utf-8').write(html)
    print(f'✓ {out_path}  {os.path.getsize(out_path)} bytes  (b64 {total})')


if __name__ == '__main__':
    main()
