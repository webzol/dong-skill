# AGENTS.md — dong-skill（公众号排版 + 每日 AI 热点）

本仓库是公众号排版 skill（`gzh-skill/`，两套引擎）及其产出目录。
任何 AI 工具（OpenCode / Claude Code / Codex / Cursor / Gemini CLI）读到这里，都按以下约定工作。

## 〇、怎么生效（先读这一节）

| 你的情况 | 结果 |
|---|---|
| 在**本仓库目录**里开 AI 会话 | `AGENTS.md` / `CLAUDE.md` / `GEMINI.md` / `.cursorrules` 等会被自动读入，默认规则直接生效 |
| clone 到别处、在**别的项目目录**里问 | 不生效。要么在本仓库里开，要么跑 `gzh-skill\install.ps1`（或 `install.sh`）装成 skill，要么把 `DAILY_NEWS_WORKFLOW.md` 的路径明确告诉它 |
| 想让它**开始收集今天的 3 篇** | **必须给触发词**：`早报` / `今天的热点` / `每日 3 篇` / `按每日流程跑`，或斜杠命令 `/zaobao`，或贴 X「Today's News」截图。AI 没有定时器，不会自己起床 |

- 在本仓库里被唤醒、用户又没给具体任务时：**先问一句「跑今天的早报，还是排版某篇稿子？」**，不要沉默等着。
- 一旦触发，一律以 `gzh-skill/engine-wx/DAILY_NEWS_WORKFLOW.md` 为准，不要凭记忆简化。
- 换电脑时只需改三处：成品根目录（默认 `E:\WX`）、仓库路径、Chrome 路径（`xshot.ps1` 已自动探测）。

## 一、常驻约定

- 排版默认组合：**模板 `minimal-tech` × 主题 `dongpro`**。
- 配图规范：图片**内嵌在对应正文位置**，不堆文末；**图下不写任何文字**（2026-10-30 定版，取消 12px 灰图注），
  间距固定为 `display:block;margin:14px 0 20px`——图要说明什么，写进它上面或下面的正文，不要挂在图底下；
  图片一律 base64 内嵌，交付单文件 HTML（含右上角「复制到公众号」按钮）；**图片不加边框和圆角**，铺满栏宽即可。
- 能拿到原图就用原图：推文配图走 `https://pbs.twimg.com/media/<id>?format=jpg&name=large`
  （`<id>` 从推文页 HTML 里 `pbs.twimg.com/media/` 抓，`Invoke-WebRequest` 可用，`curl` 走 schannel 会握手失败）。
  只有「帖子本身」才截图；截正文里的图会带白边和页面边框。
- 长截图**不整张放进去**：按 `-Scale 3` 截图，切成 2–4 段高清裁图（900px 宽），按原帖顺序嵌进正文对应位置。
- 开头**不从日期或时刻起笔**：第一段直接进事件（截图里写了什么、谁说了什么），时间信息挪到后文再交代。
- 正文**不点名平台**：不写「X 上」「推文」，用「网上」「一位用户 / 博主」替代；也不挂 `@handle`，直接写「发图的人」「一位英文博主」。
- 不要多余底色：卡片只用 `1px #ececec` 细边框，不加 `#f7f7f7` 灰填充（表格表头 / 行内代码除外）。
- 成品落盘：`E:\WX\<YYYY-MM-DD>\`；同时备份 `generated/<date>/`（gitignored，不入库）。
  文件名禁用全角「：」「／」与 `/\:*?"<>|`，冒号用「 · 」或「 - 」，否则预览面板打不开。
- 文末**不加页脚**（2026-10-30 定版）：不写「品牌 · 产品 · 状态 · 日期」那一行，正文最后一句就结束；也不放来源列表。
- 交付话术固定三句：打开成品 → 点「复制到公众号」 → 公众号编辑器粘贴；结尾写「本版 = 模板 X + 主题 Y」。
- **铁律：改完必须提交并推送**（2026-10-30 用户定版）：任何一次改稿或改规则，必须在同一轮里改源头 → 重新生成 → 更新台账 → 回写规则 → `commit` + `push`，并在回复里报 commit 短号。不许只答复不落盘，也不许把改动留在工作区不推。细则见下一节。

## 二、改动同步（铁律）

改一篇稿、改一条规则，都按这个顺序走完：

1. **改源头**：改 `generated/<date>/<slug>/body.html`（或规则文档本身），不要直接手改成品 HTML；
2. **重新生成**：`inject_images.py --allow-missing-captions` → `wrap_preview.py`，**串行**，成品同时写 `E:\WX\<date>\` 和 `generated/<date>/` 两份；
3. **更新台账**：`docs/sources/<date>.md` 追加「修订记录」——改了什么、为什么改、改前改后（配图换了原图、删了页脚、换了标题都算）；
4. **规则回写**：这次改动如果确立了新口径，同步改 `AGENTS.md` / `DAILY_NEWS_WORKFLOW.md` / `SKILL.md` / `components.md` 等，把旧口径就地改掉，不要留两套；
5. **推送**：`git add -A` → `git commit -m "..."` → `git push`，并在回复里报 commit 短号。

自查：`git status --short` 必须为空，成品 `data:image` 数 = 图张数、`{{` 残留为 0。

## 三、每日 AI 热点（3 篇）

触发词：`早报` / `今天的热点` / `每日 3 篇` / `按每日流程跑`，或用户直接贴 X「Today's News」截图。

**完整流程见 `gzh-skill/engine-wx/DAILY_NEWS_WORKFLOW.md`，执行前必读。** 摘要：

1. 选 3 条 AI 大模型相关热点（发布/泄露、开源模型、价格额度 各一条最稳）；
2. 用 websearch 复现可核验事实（x.com/explore 需登录，抓不到，别硬试）；
   信源清单固定在 `DAILY_NEWS_WORKFLOW.md` §1.1（HF 模型卡 / OpenAI help center / 官方 blog / 官方 X / 媒体 / 第三方榜 / 社区）；
3. 配图：`gzh-skill/engine-wx/scripts/xshot.ps1` 截公开推文/官方页面 → `bands.py` 探边界 → `crop.py` 裁切；
   各站截图参数与裁剪坐标写在 `DAILY_NEWS_WORKFLOW.md` §3.5，高清原图走推文页 `og:image`；
4. 写稿：先硬事实、再解读，标注官方 / 媒体 / 社区三类口径，不编数字；**禁止单独灰字导语块**，**正文不要放 h1 大标题**（公众号标题栏已有），直接正文（可点题 / 幽默 / 对比写进第一段）；文内 `h2`/`h3` **不要直接写内容**（短钩子、不剧透要点；详见 `DAILY_NEWS_WORKFLOW.md` §4）；
5. 组装：`scripts/inject_images.py` → `engine-design/scripts/wrap_preview.py`，**串行**；
6. 质检：无 `{{` 残留、`data:image` 数 = 图张数、目录只留成品；
7. 写信源台账 `docs/sources/<date>.md`（哪个数字/哪张图 ← 哪个 URL 的哪一块；**入库**）；
8. 预览 + 交付清单。

## 四、茶类内容（自动调用）

**只要涉及茶，就不用问、直接走茶模板**：茶知识、茶文化、茶器、茶史、茶席、冲泡、存茶、茶叶、茶单，
都算。显式指令是 **`茶模型`**（或 `/chamo`），效果相同。

- 主题固定 **`tea-atelier`**（白底 + 墨黑 + 古铜 `#8a6a3f` + 青灰 `#5f7358`，宋体标题 1.95 行高）。
- 模板六选一：

| 内容 | 首选 | 备选 |
|---|---|---|
| 茶知识 · 风味 / 参数 / 冲泡 / 存茶 | `tea-notes` | `tea-almanac` |
| 茶知识 · 时间 / 节气 / 一天四泡 | `tea-almanac` | `tea-notes` |
| 茶文化 · 茶史 / 点茶 / 茶礼 / 茶书茶画 | `tea-culture` | `tea-scroll` |
| 茶文化 · 公案 / 茶人 / 茶席随笔 | `tea-scroll` | `tea-culture` |
| 茶器 · 多器对比 / 怎么选 | `tea-ware` | `tea-catalog` |
| 茶器 · 单件拆解 / 部位 / 手感 | `tea-catalog` | `tea-ware` |

- 用户没说方向时，先问一句「茶知识、茶文化，还是茶器？」，不要自己猜。
- 完整流程与硬规则见 `gzh-skill/commands/chamo.md`；模板骨架在 `gzh-skill/engine-wx/templates/`。
- 茶稿同样守常驻约定：不放 h1、不放灰字导语、图下不写字、无边框圆角、文末无页脚、base64 单文件、改完必须 push。

## 五、已知坑

- `browser.*` 工具连不上 `x.com`（`ERR_CONNECTION_CLOSED`），截图必须走本机 Chrome 脚本；
- X 会 403 掉 `HeadlessChrome` UA，`xshot.ps1` 已内置普通 Chrome UA；
- 注入 + 包装 + 删除中间文件必须同一条命令串行，否则成品可能残留 `{{IMG_*}}`；
- GBK 控制台跑 Python 先设 `$env:PYTHONIOENCODING='utf-8'`；
- 文件名含全角「／」时预览面板打不开，复制 ASCII 副本到 `.tmp-preview/` 再预览。
- §13c 可上滑长图交付前必须滑动自测（2026-11-01）。
