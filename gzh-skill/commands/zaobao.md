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
4. 写稿：**先读 `gzh-skill/engine-wx/references/writing-style.md` 定腔调**（新智元/卡兹克/量子位/ASI），开篇样例见 `writing-style-samples.md`；
   每篇 900–1600 汉字，图 2–5 张，**图下不加文字**；开头不写时间、不放灰字导语块；小标题用结论短句不用问句；
5. 排版默认用 `minimal-tech × dongpro`，另排 1–2 个备选。正文直接开篇，小节标题 17px；
6. 各版注入并检查同一批图片，按 §6 一次打包同稿备选；
7. 落盘 `E:\WX\<YYYY-MM-DD>\`，备份 `generated\<date>\`，台账写 `docs\sources\<date>.md`；
8. 文件名禁用全角「：」「／」；
9. 交付三句用法。打开成品按需切换版式 → 点「复制到公众号」→ 公众号编辑器粘贴。结尾写实际默认组合，并附文件、大小、图数、字数。

用户这次给的线索：
$ARGUMENTS
