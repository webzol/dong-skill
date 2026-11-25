#!/usr/bin/env python3
"""清理内联 style 里的单引号，避免公众号草稿箱 API / Muse 整段清空 style。

背景：公众号草稿接口（Muse 等 AI 排版工具走的路径）对内联样式做二次清洗，
style 值里一旦出现 ASCII 单引号 `'`（常见于 font-family:'Songti SC'），
整条 style 会被静默丢弃，正文变成默认字体、字号和行距，排版整体塌掉。
公众号后台手动粘贴对此更宽松，所以本地预览看不出问题。

用法：
    python wx_sanitize.py body.html              # 就地清理
    python wx_sanitize.py body.html out.html     # 写新文件
    python wx_sanitize.py body.html --check      # 只检查，残留则 exit 2

规则：
- 只处理 `style="..."` 属性，不动正文文字（英文撇号原样保留）；
- 字体名去掉引号：font-family:'Songti SC','STSong',serif → font-family:Songti SC,STSong,serif
- 其他样式值里的 `'` 一并删除；
- 输出报告：清理条数 / 残留条数。
"""
import re
import sys

STYLE_RE = re.compile(r'style="([^"]*)"')


def sanitize_styles(html):
    """返回 (清理后的 html, 被清理的 style 条数)。"""
    fixed = 0

    def repl(match):
        nonlocal fixed
        value = match.group(1)
        if "'" not in value:
            return match.group(0)
        fixed += 1
        return 'style="' + value.replace("'", "") + '"'

    return STYLE_RE.sub(repl, html), fixed


def count_bad_styles(html):
    return sum(1 for m in STYLE_RE.finditer(html) if "'" in m.group(1))


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    check = '--check' in sys.argv
    if not args:
        print(__doc__)
        sys.exit(1)

    src = args[0]
    html = open(src, encoding='utf-8-sig').read()

    if check:
        bad = count_bad_styles(html)
        if bad:
            print(f'✗ {src}: {bad} 条 style 含单引号，Muse / 草稿箱 API 会清空这些样式')
            sys.exit(2)
        print(f'✓ {src}: style 无单引号')
        return

    cleaned, fixed = sanitize_styles(html)
    left = count_bad_styles(cleaned)
    dst = args[1] if len(args) > 1 else src
    open(dst, 'w', encoding='utf-8').write(cleaned)
    print(f'✓ 清理 {fixed} 条 style 的单引号 → {dst}')
    if left:
        print(f'✗ 仍有 {left} 条 style 含单引号')
        sys.exit(2)


if __name__ == '__main__':
    main()
