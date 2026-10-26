---
description: 跑今天的每日 AI 热点（3 篇）——选题、抓图、写稿、排版、落盘
argument-hint: "[可选：3 条头条线索，或要排版的稿件路径]"
---

读 `gzh-skill/engine-wx/DAILY_NEWS_WORKFLOW.md`（不在仓库里时用安装目录下的同名文件），
严格按 9 个环节执行「每日 AI 热点」：

1. 选 3 条 AI 大模型热点（发布/泄露 + 开源模型 + 价格额度 各一条最稳）；信源清单见 §1.1；
2. 用 websearch 复现可核验事实，不编数字，标注官方 / 媒体 / 社区三类口径；
3. 配图：`scripts/xshot.ps1`（本机 Chrome headless + 普通 UA）→ `bands.py` 探边界 → `crop.py` 裁；
   参数与坐标见 §3.5，**不要**用浏览器工具开 x.com；
4. 写稿：每篇 900–1600 汉字，图 2–5 张，图下 12px `#8a8a8a` 居中图注；
5. 排版：模板 `minimal-tech` × 主题 `dongpro`；h1 16px / h2 17px / 小节标题不带中文序号；
6. 组装：`inject_images.py` → `wrap_preview.py`，串行；一图一注校验不过就补图注；
7. 落盘 `E:\WX\<YYYY-MM-DD>\`，备份 `generated\<date>\`，台账写 `docs\sources\<date>.md`；
8. 文件名禁用全角「：」「／」；
9. 交付三句用法 + 「本版 = 模板 minimal-tech + 主题 dongpro」，并附交付清单（文件 / 大小 / 图数 / 字数）。

用户这次给的线索：
$ARGUMENTS
