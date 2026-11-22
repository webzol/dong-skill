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
| 节日茶俗 · 春节/清明/端午/中秋/冬至等 | `tea-festival` | `tea-scroll` |
| 行业信息 · 新茶上市/价格行情/政策标准/展会财报 | `tea-industry` | `tea-notes` |

- 用户没说方向：先问一句「茶知识、茶文化，还是茶器？」，别自己猜。
- 用户只给了「茶」+ 一篇稿：按稿子内容判断；判断不出按 `tea-notes` 走。
- 已明确“茶知识”但没有选题或草稿：只问具体要解决的问题，不再追问三大方向。维护模板或技能的请求直接做维护，不自动写一篇文章。
- 茶知识写作或审稿先读 `gzh-skill/engine-wx/references/tea-knowledge.md`，按其中的选题、事实核验、参数与台账口径执行。
- **写正文前读 `gzh-skill/engine-wx/references/writing-style.md`**：茶稿同样守 §1 共用配方（开篇不写日期、不放灰字导语块、小标题结论式短句不用问句、收尾一句判断后停）；腔调按题材取——知识类偏量子位式信息密度，文化 / 器类偏卡兹克式从容。只做排版、草稿已定稿时可跳过。

## 硬规则

1. 正文**不放 h1**（公众号标题栏已有）、**不放灰字导语**、文末**不加页脚、不加来源列表**；
2. 图**内嵌在对应正文位置**，`display:block;width:100%;margin:14px 0 20px;`，**无边框、无圆角、图下不写字**；
3. 图片一律 base64，交付单文件 HTML（带右上角「复制到公众号」按钮）；
4. 不用底色卡片、圆角、阴影；表头只允许 `#f7f3ea`；
5. 宋体标题 + 苹方正文，15px / 1.95 行高 / 两端对齐；
6. 不写保健功效，不做「越陈越香」的绝对判断；冲泡建议给有依据的起始区间及适用条件，实测值和引用数据保持原值。

## 执行

1. 读模板骨架：`gzh-skill/engine-wx/templates/<模板>.md`；主题：`themes/tea-atelier.json`；口吻：`gzh-skill/engine-wx/references/writing-style.md`；
2. 写 `generated/<date>/<slug>/body.html`，用同一正文和图序另排适合的备选。各版用茶模板和 `tea-atelier`，图片共用 `{{IMG_A}}` 等占位符；
3. 配图放 `generated/<date>/<slug>/img/`，写 `images.json`；
4. 各版文本按校验器要求包 `<span leaf="">`，逐版先校验、再注入图片、再校验注入后的正文。全部通过后按 [统一打包流程](../SKILL.md) 用 `wrap_preview.py` 打包默认版和备选；
5. 落盘 `E:\WX\<YYYY-MM-DD>\`，备份 `generated\<date>\<slug>\`；
6. 台账 `docs/sources/<date>-<slug>.md`（事实出处、适用条件、配图来源与修订记录），在 `docs/sources/<date>.md` 链接；保留 `body.html`、`images.json` 和源图用于后续改稿，交付目录只放成品；
7. `git add` → `commit` → `push`，回复报 commit 短号；
8. 交付三句用法。打开成品并按需切换模板 → 点「复制到公众号」→ 到公众号编辑器粘贴。结尾写「默认版 = 模板 X + 主题 tea-atelier」。

仅维护规则、未修改文章源稿时，不重生成历史文章；在台账与 `DEV_NOTES.md` 说明变更范围、验证结果及旧稿待核验项。提交推送遵守仓库授权边界；主分支推送未获确认时使用 `codex/` 分支。

用户这次给的内容：
$ARGUMENTS
