#!/usr/bin/env python3
"""把同题材的 1–2 种写作风格打包成单文件预览，首个风格默认显示。"""

import argparse
import re
from html import escape
from html.parser import HTMLParser
from pathlib import Path


class ArticleImages(HTMLParser):
    """收集图片标签的属性和源码位置，确保其余正文逐字保留。"""

    def __init__(self, source):
        super().__init__(convert_charrefs=False)
        self.tags = []
        self.line_starts = [0, *(match.end() for match in re.finditer("\n", source))]
        self.feed(source)
        self.close()

    def handle_starttag(self, tag, attrs):
        if tag == "img":
            line, column = self.getpos()
            start = self.line_starts[line - 1] + column
            end = start + len(self.get_starttag_text())
            self.tags.append((start, end, attrs))

    @property
    def sources(self):
        return [dict(attrs).get("src") for _, _, attrs in self.tags]


def share_images(content, original_sources, path):
    images = ArticleImages(content)
    if images.sources != original_sources or None in images.sources:
        raise ValueError(f"{path} 的图片及顺序须与默认版一致，每张图都须有 src。")

    parts = []
    cursor = 0
    for index, (start, end, attrs) in enumerate(images.tags):
        parts.append(content[cursor:start])
        properties = [
            name if value is None else f'{name}="{escape(value, quote=True)}"'
            for name, value in attrs
            if name != "src"
        ]
        properties.append(f'data-gzh-src="{index}"')
        parts.append(f'<img {" ".join(properties)}>')
        cursor = end
    parts.append(content[cursor:])
    return "".join(parts)


def render_picker(default_label, variants, content):
    picker = '<div class="gzh-picker" role="group" aria-label="风格选择"><span class="gzh-picker-label">风格选择</span>\n'
    if not variants:
        return picker + f'<span class="gzh-current">{escape(default_label)} · 默认</span></div>', ""

    if len(variants) > 1:
        raise ValueError("每篇最多两种风格：一个默认风格和一个备选风格。")
    if variants[0][0].strip() == default_label.strip():
        raise ValueError("默认与备选须使用不同的风格名称。")

    original_sources = ArticleImages(content).sources
    labels = [default_label]
    templates = []
    for index, (label, filename) in enumerate(variants, start=1):
        path = Path(filename)
        variant = path.read_text(encoding="utf-8-sig").strip()
        if not variant:
            raise ValueError(f"{path} 没有正文。")
        if re.search(r"</?template\b", variant, re.IGNORECASE):
            raise ValueError(f"{path} 请传入公众号正文片段。")
        labels.append(label)
        shared = share_images(variant, original_sources, path)
        templates.append(f'<template data-gzh-content="{index}">\n{shared}\n</template>')

    buttons = []
    for index, label in enumerate(labels):
        active = "true" if index == 0 else "false"
        badge = "默认" if index == 0 else "备选"
        buttons.append(
            f'<button type="button" class="gzh-option" data-gzh-variant="{index}" '
            f'aria-pressed="{active}"><span class="gzh-option-name">{escape(label)}</span>'
            f"<small>{badge}</small></button>"
        )
    return picker + "\n".join(buttons) + "\n</div>", "\n".join(templates)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path, help="已排版的默认正文 HTML")
    parser.add_argument("output", type=Path, nargs="?", help="单文件成品路径")
    parser.add_argument("--title", help="浏览器标题，缺省使用默认正文的文件名")
    parser.add_argument("--default-label", default="原稿", help="默认写作风格名，纯排版默认为原稿")
    parser.add_argument(
        "--variant", action="append", nargs=2, metavar=("风格名称", "正文HTML"),
        help="添加一个按另一种写作风格撰写的正文",
    )
    args = parser.parse_args()

    try:
        content = args.source.read_text(encoding="utf-8-sig").strip()
        template = Path(__file__).resolve().parent.parent / "assets" / "preview-template.html"
        shell = template.read_text(encoding="utf-8")
        picker, variants = render_picker(args.default_label, args.variant, content)
        out_html = (
            shell.replace("{{TITLE}}", escape(args.title or args.source.stem))
            .replace("<!--GZH_PICKER-->", picker)
            .replace("<!--GZH_VARIANTS-->", variants)
            .replace("<!--GZH_CONTENT-->", content)
        )
        out = args.output or args.source.with_name(f"{args.source.stem}_预览.html")
        out.write_text(out_html, encoding="utf-8")
    except (OSError, ValueError) as error:
        parser.exit(1, f"生成预览失败：{error}\n")

    print(f"✓ 已生成带「复制」按钮的预览页: {out}")
    if args.variant:
        print("  切换写作风格后，复制当前显示的正文。")
    print("  用浏览器打开它，点右上角「复制到公众号」，再去公众号编辑器 Ctrl/⌘+V 粘贴。")


if __name__ == "__main__":
    main()
