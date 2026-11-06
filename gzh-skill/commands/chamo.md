---
description: 茶模型 —— 茶知识 / 茶文化 / 茶器内容一键排版，自动选茶模板 + 茶志主题
argument-hint: "[茶稿路径或一句主题；也可只写『茶知识』『茶器』『茶文化』]"
---

# 茶模型

凡涉及茶的内容，一律走这条线：主题固定 `tea-atelier`，模板从下面六套里选。

## 选模板

| 内容 | 首选 | 备选 |
|---|---|---|
| 茶知识 · 风味 / 参数 / 冲泡 / 存茶 | `tea-notes` | `tea-almanac` |
| 茶知识 · 时间 / 节气 / 一天四泡 | `tea-almanac` | `tea-notes` |
| 茶文化 · 茶史 / 点茶 / 茶礼 / 茶书茶画 | `tea-culture` | `tea-scroll` |
| 茶文化 · 公案 / 茶人 / 茶席随笔 | `tea-scroll` | `tea-culture` |
| 茶器 · 多器对比 / 怎么选 | `tea-ware` | `tea-catalog` |
| 茶器 · 单件拆解 / 部位 / 手感 | `tea-catalog` | `tea-ware` |

- 用户没说方向：先问一句「茶知识、茶文化，还是茶器？」，别自己猜。
- 用户只给了「茶」+ 一篇稿：按稿子内容判断；判断不出按 `tea-notes` 走。

## 硬规则

1. 正文**不放 h1**（公众号标题栏已有）、**不放灰字导语**、文末**不加页脚、不加来源列表**；
2. 图**内嵌在对应正文位置**，`display:block;width:100%;margin:14px 0 20px;`，**无边框、无圆角、图下不写字**；
3. 图片一律 base64，交付单文件 HTML（带右上角「复制到公众号」按钮）；
4. 不用底色卡片、圆角、阴影；表头只允许 `#f7f3ea`；
5. 宋体标题 + 苹方正文，15px / 1.95 行高 / 两端对齐；
6. 不写保健功效，不做「越陈越香」的绝对判断；参数只给区间。

## 执行

1. 读模板骨架：`gzh-skill/engine-wx/templates/<模板>.md`；主题：`themes/tea-atelier.json`；
2. 写 `generated/<date>/<slug>/body.html`（内联样式，占位 `{{IMG_A}}`）；
3. 配图放 `generated/<date>/<slug>/img/`，写 `images.json`；
4. 串行跑：`validate_gzh_html.py`（需 `<span leaf="">`）→ `inject_images.py --allow-missing-captions` → `wrap_preview.py`；
5. 落盘 `E:\WX\<YYYY-MM-DD>\`，备份 `generated\<date>\<slug>\`；
6. 台账 `docs/sources/<date>-<slug>.md`（事实出处 + 配图来源）；
7. `git add` → `commit` → `push`，回复报 commit 短号；
8. 交付三句用法 + 「本版 = 模板 X + 主题 tea-atelier」。

用户这次给的内容：
$ARGUMENTS
