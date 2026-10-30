# GEMINI.md

本仓库的常驻规则全部写在 `AGENTS.md`，每日热点流程细节写在
`gzh-skill/engine-wx/DAILY_NEWS_WORKFLOW.md`。开工前先读这两个文件。

本文件不重复规则，只做入口转发——规则改动请改 `AGENTS.md`，避免多处不一致。

## 每日 AI 热点（3 篇）

触发词：`早报` / `今天的热点` / `每日 3 篇` / `按每日流程跑`，或用户直接贴 X「Today's News」截图。

1. 读 `gzh-skill/engine-wx/DAILY_NEWS_WORKFLOW.md`，按里面 9 个环节执行；
   （信源清单 §1.1 · 抓图参数与坐标 §3.5 · 信源台账 §7.1）
2. 产出 3 篇，模板 `minimal-tech` × 主题 `dongpro`；
3. 排版：h1 16px、h2 17px、小节标题不带「一、二、三、」；配图内嵌在对应正文位置，
   **图下不加文字**；长截图切段，不放整张；开头不写时间；图片 base64 单文件；
4. 成品落盘 `E:\WX\<YYYY-MM-DD>\`，备份 `generated/<date>/`（gitignored）；
5. 交付三句用法 + 结尾「本版 = 模板 X + 主题 Y」。

## 硬约束速记

- 截图用 `gzh-skill/engine-wx/scripts/xshot.ps1`（本机 Chrome headless + 普通 UA），
  **不要**用浏览器工具去开 `x.com`（连不上）。
- 组装 `inject_images.py` → `wrap_preview.py` 必须串行，防残留 `{{IMG_*}}`。
- 不编数字；官方 / 媒体 / 社区三类口径要写清。
