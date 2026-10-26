# AGENTS.md — dong-skill（公众号排版 + 每日 AI 热点）

本仓库是公众号排版 skill（`gzh-skill/`，两套引擎）及其产出目录。
任何 AI 工具（OpenCode / Claude Code / Codex / Cursor / Gemini CLI）读到这里，都按以下约定工作。

## 〇、怎么生效（先读这一节）

| 你的情况 | 结果 |
|---|---|
| 在**本仓库目录**里开 AI 会话 | `AGENTS.md` / `CLAUDE.md` / `GEMINI.md` / `.cursorrules` 等会被自动读入，默认规则直接生效 |
| clone 到别处、在**别的项目目录**里问 | 不生效。要么在本仓库里开，要么跑 `gzh-skill\install.ps1`（或 `install.sh`）装成 skill，要么把 `DAILY_NEWS_WORKFLOW.md` 的路径明确告诉它 |
| 想让它**开始收集今天的 3 篇** | **必须给触发词**：`早报` / `今天的热点` / `每日 3 篇` / `按每日流程跑`，或贴 X「Today's News」截图。AI 没有定时器，不会自己起床 |

- 在本仓库里被唤醒、用户又没给具体任务时：**先问一句「跑今天的早报，还是排版某篇稿子？」**，不要沉默等着。
- 一旦触发，一律以 `gzh-skill/engine-wx/DAILY_NEWS_WORKFLOW.md` 为准，不要凭记忆简化。
- 换电脑时只需改三处：成品根目录（默认 `E:\WX`）、仓库路径、Chrome 路径（`xshot.ps1` 已自动探测）。

## 一、常驻约定

- 排版默认组合：**模板 `minimal-tech` × 主题 `dongpro`**。
- 配图规范：图片**内嵌在对应正文位置**，不堆文末；每图下方 12px `#8a8a8a` 居中图注；
  图片一律 base64 内嵌，交付单文件 HTML（含右上角「复制到公众号」按钮）。
- 不要多余底色：卡片只用 `1px #ececec` 细边框，不加 `#f7f7f7` 灰填充（表格表头 / 行内代码除外）。
- 成品落盘：`E:\WX\<YYYY-MM-DD>\`；同时备份 `generated/<date>/`（gitignored，不入库）。
- 交付话术固定三句：打开成品 → 点「复制到公众号」 → 公众号编辑器粘贴；结尾写「本版 = 模板 X + 主题 Y」。

## 二、每日 AI 热点（3 篇）

触发词：`早报` / `今天的热点` / `每日 3 篇` / `按每日流程跑`，或用户直接贴 X「Today's News」截图。

**完整流程见 `gzh-skill/engine-wx/DAILY_NEWS_WORKFLOW.md`，执行前必读。** 摘要：

1. 选 3 条 AI 大模型相关热点（发布/泄露、开源模型、价格额度 各一条最稳）；
2. 用 websearch 复现可核验事实（x.com/explore 需登录，抓不到，别硬试）；
   信源清单固定在 `DAILY_NEWS_WORKFLOW.md` §1.1（HF 模型卡 / OpenAI help center / 官方 blog / 官方 X / 媒体 / 第三方榜 / 社区）；
3. 配图：`gzh-skill/engine-wx/scripts/xshot.ps1` 截公开推文/官方页面 → `bands.py` 探边界 → `crop.py` 裁切；
   各站截图参数与裁剪坐标写在 `DAILY_NEWS_WORKFLOW.md` §3.5，高清原图走推文页 `og:image`；
4. 写稿：先硬事实、再解读，标注官方 / 媒体 / 社区三类口径，不编数字；
5. 组装：`scripts/inject_images.py` → `engine-design/scripts/wrap_preview.py`，**串行**；
6. 质检：无 `{{` 残留、`data:image` 数 = 图张数、目录只留成品；
7. 写信源台账 `generated/<date>/sources.md`（哪个数字/哪张图 ← 哪个 URL 的哪一块）；
8. 预览 + 交付清单。

## 三、已知坑

- `browser.*` 工具连不上 `x.com`（`ERR_CONNECTION_CLOSED`），截图必须走本机 Chrome 脚本；
- X 会 403 掉 `HeadlessChrome` UA，`xshot.ps1` 已内置普通 Chrome UA；
- 注入 + 包装 + 删除中间文件必须同一条命令串行，否则成品可能残留 `{{IMG_*}}`；
- GBK 控制台跑 Python 先设 `$env:PYTHONIOENCODING='utf-8'`；
- 文件名含全角「／」时预览面板打不开，复制 ASCII 副本到 `.tmp-preview/` 再预览。
