# Copilot 项目说明

本仓库 = 公众号排版 skill（`gzh-skill/`）+ 成品归档。

- 常驻规则：`AGENTS.md`
- 每日热点流程：`gzh-skill/engine-wx/DAILY_NEWS_WORKFLOW.md`

开工前先读这两个文件。本文件只做转发，不要在代码里另写一套规则。

## 默认组合

模板 `minimal-tech` × 主题 `dongpro`。

## 每日 AI 热点（触发词：早报 / 今天的热点 / 每日 3 篇 / 按每日流程跑）

1. 按 `DAILY_NEWS_WORKFLOW.md` 的 9 个环节执行；
   （信源清单 §1.1 · 抓图参数与坐标 §3.5 · 信源台账 §7.1）
2. 产出 3 篇（发布/泄露、开源模型、价格额度 各一条最稳）；
3. 排版：h1 16px、h2 17px、小节标题不带「一、二、三、」；配图内嵌对应正文位置，
   图下 12px `#8a8a8a` 居中图注；图片一律 base64 单文件；
4. 成品落盘 `E:\WX\<YYYY-MM-DD>\`，备份 `generated/<date>/`（gitignored）；
5. 交付三句用法 + 「本版 = 模板 X + 主题 Y」。

## 硬约束

- 截图用 `gzh-skill/engine-wx/scripts/xshot.ps1` + `crop.py`；不要用浏览器工具开 `x.com`（连不上）。
- `inject_images.py` → `engine-design/scripts/wrap_preview.py` 必须串行，防残留 `{{IMG_*}}`。
- 不编数字；官方 / 媒体 / 社区三类口径写清。
- 卡片只用 `1px #ececec` 细边框，不加 `#f7f7f7` 灰填充。
