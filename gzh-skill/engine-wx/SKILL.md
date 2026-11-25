---
name: wechat-typesetting
description: >-
  将文章草稿（Markdown / 纯文本）排版成微信公众平台「可直接粘贴」的科技感 / 简约风富文本 HTML。
  当用户需要：1) 给公众号文章排版、配色调、挑模板；2) 生成微信编辑器能正常显示的图文；3) 做标题栏、
  引言卡片、代码块、数据面板等版式块时使用。产出的是一段内联样式、无 flex/grid、宽度约 677px 的
  HTML，粘贴进公众号编辑器即得：「简约 + 科技感」风格、模板可换、色调（微信可显示的配色）可选。
  WeChat-official-account typesetting: minimal + tech-style inline-styled HTML with selectable
  templates and multiple color themes.
  茶类内容（茶知识 / 茶文化 / 茶器 / 茶史 / 茶席 / 冲泡）自动启用茶模板 + tea-atelier 主题；
  显式指令「茶模型」或 /chamo。
metadata:
  version: "0.2.1"
---

# 微信公众号排版 Skill

把草稿变成「公众号里能真正显示」的科技感排版。核心原则一句话：

> **用内联样式的 `<section>` + `<table>` 拼版，颜色全部来自所选主题，版式来自所选模板。**

微信富文本编辑器会剥掉 flex / grid / CSS 变量 / 伪元素 / 媒体查询 / 自定义字体 / class 选择器；
能稳用的是**内联 style 的 section · p · span · table · img · strong · em · a**。所以本 Skill 产出的
每一段都是内联样式，跟着模板与主题走，避免任何现代 CSS 黑魔法。

---

## 一、怎么用（三种入口）

| 入口 | 示例 |
|---|---|
| 斜杠命令 | `/wechat-typesetting 我的文章.md --template cyber-card --theme tech-blue` |
| 自然语言 | "把这篇排版成科技蓝风格，用卡片模板" |
| 草图 + 指令 | 直接贴 Markdown 草稿，说"用 terminal-code 模板，赛博绿" |

**参数（均可缺省，缺省用默认「简约科技 × DONGPro极简科技（排版推荐）」）：**

- `--template` 模板名：`minimal-tech`（简约科技·默认）/ `cyber-card`（卡片）/ `terminal-code`（终端风）/ `hud`（数据面板）/ `wechat-pai-essay`（微信派·文艺长文）
  / 茶系列：`tea-culture`（茶文化）/ `tea-scroll`（手卷）/ `tea-ware`（茶器）/ `tea-catalog`（图录）/ `tea-notes`（茶知识）/ `tea-almanac`（茶历）
  / `tea-festival`（节令茶单）/ `tea-industry`（行业观察）
  / AI 科技：`ai-model`（大模型速写：元信息条 + 关键数字条 + 官方截图/榜单图各就位）
- `--theme` 主题名：`dongpro`（DONGPro极简科技 · **排版推荐**·默认）/ `minimal-light`（极简白）/ `minimal-dark`（极简黑）/ `tech-blue`（科技蓝）/ `cyber-green`（赛博绿）/ `neon-purple`（霓虹紫）/ `taobao-flash`（淘宝闪购）/ `wechat-pai`（微信派）/ `qianwen`（千问）
  / 茶系列：`tea-garden`（茶席）/ `tea-atelier`（茶志 · 茶模板默认）
  / AI 科技：`ai-lab`（AI 实验室 · 白底 + 靛蓝/松石 · ai-model 默认）
- `[草稿]` 文章内容：文件路径，或直接内联

不指定时自动用一个合理默认，并**明确告知所选模板/主题**，方便用户反悔重选。

---

## 二、工作流（每次都按这个走）

> **每日热点模式**：当用户说 `早报` / `今天的热点` / `每日 3 篇`，或贴 X「Today's News」截图时，
> 走 `DAILY_NEWS_WORKFLOW.md`（选题 → 抓推文截图 → 写 3 篇 → 排版 → 落盘 `E:\WX\<date>\`）。
> 该文件是本工作流的固定扩展，含图片获取脚本与已知坑清单。
>
> **快讯模式**：用户说「快讯」「X 分钟内写完」「先出快讯」等限时要求时，走 `DAILY_NEWS_WORKFLOW.md` §0.3——
> 只写给定素材、600–1000 汉字、跳过 websearch；**高清图片 + 高清截图与双语铁律不豁免**，
> 其余工序（组装 / 质检 / 台账 / push）不减。
>
> **茶模式**：只要内容涉及茶（茶知识 / 茶文化 / 茶器 / 茶史 / 茶席 / 冲泡 / 存茶 / 茶单），
> 直接切茶模板 + `tea-atelier`，不要用默认科技风；显式指令为「茶模型」或 `/chamo`。
>
> **AI 模式**：内容是 AI / 大模型（发布、选型、价格、榜单、参数）时，默认 `ai-model` + `ai-lab`；
> 图片位分三类：官方定价或文档页、第三方榜单、模型卡参数页，各贴在对应论点后面，图下不写字。
>
> **写稿口吻（凡是「写」而不只是「排」，都先读）**：动笔前必读 `references/writing-style.md`
> （§1 共用配方 + §2 题材选腔 + §3 所选腔细则），开篇样例见 `references/writing-style-samples.md`。
> 该文件是写稿口径的唯一出处；与本文档旧口径冲突时**以它为准**（尤其：小标题用结论短句，不用问句）。
> 只做纯排版、草稿已定稿且无需改口吻时，可跳过。
> 选模板：茶知识→`tea-notes`／时间节气→`tea-almanac`／节日茶俗→`tea-festival`／行业信息→`tea-industry`／茶史茶礼→`tea-culture`／公案随笔→`tea-scroll`／
> 多器对比→`tea-ware`／单件拆解→`tea-catalog`；方向不明先问「茶知识、茶文化，还是茶器？」。
> 茶模式完整流程见 `../commands/chamo.md`；茶知识写作或审稿必读 `references/tea-knowledge.md`。生成或改写茶稿按茶模式固定交付「茶席随笔」和「茶事笔记」，默认版和备选均使用同一茶模板与 `tea-atelier`；纯排定稿保留原稿一版。茶稿图下可按 `references/components.md` §13a 加一句简短图注。维护规则不启动文章生成。

### 第 0 步　写稿口吻（需要写正文时必做）
- 读 `references/writing-style.md`：先按 §2 定一条主腔，再套 §1 共用配方 + 该腔 §3 细则。
- 需要感性认识时从 `references/writing-style-samples.md` 或 `references/writing-style-corpus/*-body.txt` 取 1～2 段开篇样例，**不要整篇模仿**，只学节奏。
- 硬约束：标题爆点前置；开篇不写日期、不放灰字导语块；小标题结论式短句、**不用问句**；官方 / 媒体 / 社区口径分开标；收尾一句判断后停。
- 草稿已定稿、本次只做排版时跳过本步。

### 第 1 步　读懂草稿
- 若是文件，用 Read 读取；若是粘贴文本，直接读正文。
- 识别文章结构：标题 / 小节 / 正文段落 / 引用强调 / 代码 / 列表 / 要点卡片 / 数据指标 / 结尾关注。

### 第 2 步　确定排版与写作风格
- 读 `templates/_index.md` 与 `themes/themes.json`，看清单与各自风格一句话说明。
- **先按用户指定或项目约定排默认版**。茶模式按题材选茶模板并固定 `tea-atelier`，普通稿默认 `minimal-tech × dongpro`，AI 模型稿按上方约定选型。
- 模板决定**版式骨架**，主题决定**颜色**。按题材从写作风格库选 1–2 种口吻，总数含默认项。用户指定的风格优先，否则以最贴题的一种为默认。若有备选，用同一事实和图片另写一版正文，保持信源口径、图序和版式一致。纯排已定稿时保留原稿一个风格。
- 用户明确要先看样式时，打开 [模板 × 主题选择页](preview/selection.html) 看样稿。用户明确只要一版时，完成所选版即可。

### 第 3 步　生成微信兼容 HTML（核心）
1. 通读 `references/wechat-compat.md`——**铁律**，逐条遵守。
2. 通读 `references/components.md`——整套**可复用版式块**（标题栏 / 引言 / 卡片网格 / 分隔线 / 代码块 / 按钮 / 数据面板 / 脚注）。
3. 读对应模板文件，拿到它的**块骨架与占位符**。
4. 读对应主题文件，取出它的**色彩字典**（`bg / text / muted / accent / accent2 / cardBg / cardBorder / divider / codeBg / codeText / titleBar / quoteBorder`）。
5. 用主题色填模板骨架里的占位符（如 `{{accent}}`），把草稿内容塞进合适块里。
6. **配图**（草稿带图时，规范见 `references/components.md` §13）：
   - 图片**内嵌到与它对应的正文内容之后**（原帖链接后、基准数据后、宣传图段落后），**禁止统一堆到文末**
   - 每张图**下方不写文字**（2026-10-30 定版），说明写进紧邻的正文段落
   - 图片样式固定：`max-width:100%;width:100%;display:block;margin:14px 0 20px;box-sizing:border-box;`
   - `src` 一律 **base64 data URI 内嵌**（成品保持单文件）；用户没给图的位置用 §13b 占位框
   - 英文推文双语卡片、长图滑动框（含渐变底衬）见文末「双语卡片底衬与可滑动长图」一节

**每版产出一段 `<section style="max-width:677px;margin:0 auto;">…</section>` 包裹的 HTML**，
全部内联样式，**禁止** flex / grid / `var()` / `:hover` / `@media` / 伪元素 / class 选择器依赖 / 外部样式表。
正文宽度统一 677px（微信桌面容器）；深色主题里文字用浅色，对比度 ≥ 4.5:1。各版分别检查正文、图片及长图滑动容器，校验通过后统一打包。

### 第 4 步　交付
- 产出写入**当天日期目录** `generated/<YYYY-MM-DD>/`（见第 4.5 步），每篇交付一个含 1–2 种写作风格的 HTML 成品，生成或改写茶稿固定为两种。用户明确要看源码时可提供正文代码。
- 浏览器打开成品，按需切换写作风格 → 点「复制到公众号」复制当前版 → 到公众号编辑器新建图文并粘贴。
- 结尾写「默认风格 = 实际口吻名」。

### 第 4.5 步　输出归档（每次必做）

在当前工作目录下新建（或复用）**当天日期目录**，把产出放进去：

```
generated/
└── YYYY-MM-DD/                                  ← 生成当天的本地日期（ISO 格式）
    └── <theme>-<template>-<slug>.html            ← 带复制按钮的成品（唯一交付文件）
```

**规则（gzh-skill 合并版约定，覆盖旧三件套行为）**：
- 目录：`YYYY-MM-DD`（本地日期，4 位年-2 位月-2 位日）；同一天多次排版共用同一天目录
- **只交付一个文件**。在本引擎目录用统一预览脚本打包。按钮和脚本位于预览外壳，复制时仅取当前版正文。

  ```text
  python ../engine-design/scripts/wrap_preview.py default.html final.html --default-label "新智元" --variant "量子位" alternate.html
  ```

  有备选时传一次 `--variant`，同序图片在打包时共享。单风格用 `--default-label "风格名"` 标出默认项。
- `source.md` / `README.md` 归档三件套**不再默认生成**（用户明确要求时才附）
- `generated/` 不入 git（.gitignore 已忽略）；与 `examples/` 的边界：examples 是长期示例，generated 是当日产出

---

## 三、必须遵守的兼容性铁律（完整版见 references/wechat-compat.md）

- ✅ **只允许**：内联 `style`；`section / p / span / strong / em / a / img / table / td / tr / ul / ol / li / br`
- ❌ **禁止**：`Flexbox`、`Grid`、`position`、`z-index`、`var(--x)`、`:hover/:before/:after`、
  `@media`、`@font-face`、依赖 class 选择器的 `<style>`、外部 `<link>`、`backdrop-filter`、`filter`、`transform`
- ⚠️ **谨慎**：`box-shadow`、`border-radius`、`letter-spacing`（多数版本可用，个别机型失效；**布局切勿依赖**）
- `img` 必须有 `src`：交付成品一律 **base64 data URI 内嵌**（本地 `file://` 路径无效）；宽度 `width:100%`，样式与「内嵌对应位置」及普通图样式见 `references/components.md` §13；不要用背景图承载关键内容
- 字距、行高、留白是「简约科技感」的灵魂——优先用 `letter-spacing`、`line-height`、`margin/padding` 的节奏，而不是复杂装饰

---

## 四、主题（多个色调，可加）

读取 `themes/themes.json` 获全列表。内置 8 个：

| 主题 | 风格 | 关键色 |
|---|---|---|
| `dongpro`·**排版推荐** | DONGPro极简科技 | 白底 + #141414 近黑 + 苹果字体栈 + 1.95 行高 + 紫蓝 accent `#615ced` |
| `minimal-light` | 极简白 | 白底、灰字、单一黑/蓝 accent |
| `minimal-dark` | 极简黑 | 深底、浅字、细线、克制的 accent |
| `tech-blue` | 科技蓝 | 深蓝底 + 亮蓝/青，数据感 |
| `cyber-green` | 赛博绿 | 暗底 + 荧光绿，终端/矩阵感 |
| `neon-purple` | 霓虹紫 | 暗底 + 紫/品红，夜店科技感 |
| `taobao-flash` | 淘宝闪购 | 白底 + 蓝橙双强调，紧凑电商风 |
| `wechat-pai` | 微信派 | 白底 + 微信绿 #07c160，文艺杂志感 |

**新增主题**：复制 `themes/` 下一个 JSON，改 `colors` 字典（可选加 `typography` / `paletteNotes` 字段补充说明），在 `themes.json` 的 `themes` 数组登记 `file` 即可，SKILL 自动发现。

## 五、模板（可加）

读取 `templates/_index.md` 获清单。内置 5 个：

| 模板 | 版式重点 |
|---|---|
| `minimal-tech`·默认 | 细标题线 + 大留白 + 干净信息流，最「简约科技」 |
| `cyber-card` | 卡片网格，块间用圆角卡片分隔，最有「产品感」 |
| `terminal-code` | 等宽标题、命令符 `>` 引导、代码高亮块，最强「技术感」 |
| `hud` | 数据面板：指标大字 + 迷你条 + 面板框，适合 KPI / 评测 / 榜单 |
| `wechat-pai-essay` | PingFang + 1px 字距 + 两端对齐 + 1.6 行高 + 微信绿强调，最「文艺杂志」 |

**新增模板**：复制 `templates/` 下一个 .md，改骨架与占位符，在 `_index.md` 登记。

---

## 六、样式画廊

用户明确想先看样式时，可打开 [模板与主题画廊](preview/preview.html) 查看通用样稿。本文实际的默认版和备选均在交付的成品 HTML 里预览。

---

## 七、扩展与质量要求

- 人名/机构名、专有名词不虚构；只排版，不增删用户原意与事实。
- **口吻**：写正文（而非纯排版）时，先按 `references/writing-style.md` 选定腔调；开篇不放日期、不放灰字导语块，小标题结论式短句不用问句，收尾不写「所以问题来了」式反问。
- 颜色遵循主题字典，禁止随手硬编码主题之外的色值。
- 输出 HTML 前自查一遍兼容性铁律；如为效果必须破例，用 `<!-- wx-note: 此处降级说明 -->` 写明。
- 长文如需分段交付，每段都是独立可粘贴的 section，全段首尾粘连即完整文章。

## 相关文件

- `templates/_index.md` 模板清单 —— 选骨架
- `themes/themes.json` 主题注册表 —— 选色板
- `references/writing-style.md` 写稿口吻（题材选腔 + 共用配方）—— **写正文前必读**（第 0 步）
- `references/writing-style-samples.md` 开篇样例 —— 学节奏，不整篇模仿
- `references/writing-style-corpus/` 范文语料（`*-body.txt` 正文 / `*-style.json` 结构摘要）
- `references/tea-knowledge.md` 茶知识写作与核验 —— 茶稿必读
- `references/wechat-compat.md` 兼容性铁律 —— **生成前必读**
- `references/components.md` 版式块库 —— 拼版零件
- `examples/sample-article.md` 示例草稿 —— 试跑一遍
- `preview/preview.html` 预览画廊 —— 对比 20 种组合
- `generated/<YYYY-MM-DD>/` 当日产出归档 —— 一个带「复制」按钮的 HTML 成品

## 双语卡片底衬与可滑动长图（2026-11-22 定版）

**双语卡片**（英文推文翻译卡）：白底大圆角卡浮于**横向渐变底衬**上——渐变直接烘进图片（`linear-gradient(to right,#8f94fb,#4e54c8)`，四边 ≈18px@1x 渐变框），公众号内零兼容风险；卡上真实头像 + 昵称 + 认证徽章 + @handle **原样不动**，上英文黑字、下中文灰字，重点词两边同步加粗，emoji 彩色渲染、词边界断行。生成脚本：`scripts/tweet_cards.py`（仓库内，支持双语卡片 / 认证徽章 / 引用推文块 / 中文还原截图四种形态）。

**可滑动长图**：Help Center / changelog / 官帖全文等必须整张保留的长截图，以及**竖排多行文字类长图（还原截图 / 长推文全文 / 榜单列表）一律套滑动框，不看 2.5 屏阈值**。规格以 `references/components.md` §13c 为准：`height:320px` + `overflow-y:scroll` + 引导行，外包**同款渐变底衬 wrapper**（`padding:18px` + 三行兜底写法：纯色 → `-webkit-linear-gradient` → `linear-gradient`），引导行放 wrapper 内白字 `#ffffff`；**禁用渐隐 mask**（框内文字一律实色）。能切段的长截图仍优先切段；交付前必须滑动自测（框内能滑、能滑到图底看完）。

普通配图仍图下无字；正文重点词芯片（浅底 `#EEF0F7` + 深蓝 `#1F2F8F`）口径见 `references/writing-style.md` §1。
