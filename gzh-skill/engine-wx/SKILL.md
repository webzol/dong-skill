---
name: wechat-typesetting
description: >-
  将文章草稿（Markdown / 纯文本）排版成微信公众平台「可直接粘贴」的科技感 / 简约风富文本 HTML。
  当用户需要：1) 给公众号文章排版、配色调、挑模板；2) 生成微信编辑器能正常显示的图文；3) 做标题栏、
  引言卡片、代码块、数据面板等版式块时使用。产出的是一段内联样式、无 flex/grid、宽度约 677px 的
  HTML，粘贴进公众号编辑器即得：「简约 + 科技感」风格、模板可换、色调（微信可显示的配色）可选。
  WeChat-official-account typesetting: minimal + tech-style inline-styled HTML with selectable
  templates and multiple color themes.
version: 0.2.1
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

**参数（均可缺省，缺省用默认「简约科技 × 极简白」）：**

- `--template` 模板名：`minimal-tech`（简约科技·默认）/ `cyber-card`（卡片）/ `terminal-code`（终端风）/ `hud`（数据面板）/ `wechat-pai-essay`（微信派·文艺长文）
- `--theme` 主题名：`minimal-light`（极简白·默认）/ `minimal-dark`（极简黑）/ `tech-blue`（科技蓝）/ `cyber-green`（赛博绿）/ `neon-purple`（霓虹紫）/ `taobao-flash`（淘宝闪购）/ `wechat-pai`（微信派）/ `qianwen`（千问）
- `[草稿]` 文章内容：文件路径，或直接内联

不指定时自动用一个合理默认，并**明确告知所选模板/主题**，方便用户反悔重选。

---

## 二、工作流（每次都按这个走）

### 第 1 步　读懂草稿
- 若是文件，用 Read 读取；若是粘贴文本，直接读正文。
- 识别文章结构：标题 / 小节 / 正文段落 / 引用强调 / 代码 / 列表 / 要点卡片 / 数据指标 / 结尾关注。

### 第 2 步　锁定模板 + 主题
- 读 `templates/_index.md` 与 `themes/themes.json`，看清单与各自风格一句话说明。
- 模板决定**版式骨架**（怎么摆块），主题决定**颜色**（色板）。两者自由组合。
- 默认 `minimal-tech` + `minimal-light`。除非用户点名，否则别自作主张换更强效果的组合。

### 第 3 步　生成微信兼容 HTML（核心）
1. 通读 `references/wechat-compat.md`——**铁律**，逐条遵守。
2. 通读 `references/components.md`——整套**可复用版式块**（标题栏 / 引言 / 卡片网格 / 分隔线 / 代码块 / 按钮 / 数据面板 / 脚注）。
3. 读对应模板文件，拿到它的**块骨架与占位符**。
4. 读对应主题文件，取出它的**色彩字典**（`bg / text / muted / accent / accent2 / cardBg / cardBorder / divider / codeBg / codeText / titleBar / quoteBorder`）。
5. 用主题色填模板骨架里的占位符（如 `{{accent}}`），把草稿内容塞进合适块里。

**产出：一段 `<section style="max-width:677px;margin:0 auto;">…</section>` 包裹的 HTML**，
全部内联样式，**禁止** flex / grid / `var()` / `:hover` / `@media` / 伪元素 / class 选择器依赖 / 外部样式表。
正文宽度统一 677px（微信桌面容器）；深色主题里文字用浅色，对比度 ≥ 4.5:1。

### 第 4 步　交付
- 产出写入**当天日期目录** `generated/<YYYY-MM-DD>/`（见第 4.5 步），只交付一个带「复制」按钮的 HTML 成品；**不再默认用 ```` ```html ```` 代码块整段输出**（用户明确要看源码时才贴）。
- 给一句话操作说明：浏览器打开成品 → 点右上角「复制到公众号」→ 公众号编辑器「新建图文」→「粘贴」。
- 若用户想看整体效果再定稿：生成或更新 `preview/preview.html`（见下），浏览器打开对比所见≈微信所见。
- 结尾给一行「本版 = 模板 X + 主题 Y」，并提示可换组合。

### 第 4.5 步　输出归档（每次必做）

在当前工作目录下新建（或复用）**当天日期目录**，把产出放进去：

```
generated/
└── YYYY-MM-DD/                                  ← 生成当天的本地日期（ISO 格式）
    └── <theme>-<template>-<slug>.html            ← 带复制按钮的成品（唯一交付文件）
```

**规则（gzh-skill 合并版约定，覆盖旧三件套行为）**：
- 目录：`YYYY-MM-DD`（本地日期，4 位年-2 位月-2 位日）；同一天多次排版共用同一天目录
- **只交付一个文件**：用统一入口包的复制按钮脚本给正文包一层预览外壳
  （`engine-design/scripts/wrap_preview.py <正文.html> <成品.html>`，按钮和脚本只在外壳里，粘贴出去的仍是干净正文）
- `source.md` / `README.md` 归档三件套**不再默认生成**（用户明确要求时才附）
- `generated/` 不入 git（.gitignore 已忽略）；与 `examples/` 的边界：examples 是长期示例，generated 是当日产出

---

## 三、必须遵守的兼容性铁律（完整版见 references/wechat-compat.md）

- ✅ **只允许**：内联 `style`；`section / p / span / strong / em / a / img / table / td / tr / ul / ol / li / br`
- ❌ **禁止**：`Flexbox`、`Grid`、`position`、`z-index`、`var(--x)`、`:hover/:before/:after`、
  `@media`、`@font-face`、依赖 class 选择器的 `<style>`、外部 `<link>`、`backdrop-filter`、`filter`、`transform`
- ⚠️ **谨慎**：`box-shadow`、`border-radius`、`letter-spacing`（多数版本可用，个别机型失效；**布局切勿依赖**）
- `img` 必须有 `src`（微信外链图），宽度用 `width:100%` 或固定值；不要用背景图承载关键内容
- 字距、行高、留白是「简约科技感」的灵魂——优先用 `letter-spacing`、`line-height`、`margin/padding` 的节奏，而不是复杂装饰

---

## 四、主题（多个色调，可加）

读取 `themes/themes.json` 获全列表。内置 8 个：

| 主题 | 风格 | 关键色 |
|---|---|---|
| `minimal-light` | 极简白·默认 | 白底、灰字、单一黑/蓝 accent |
| `minimal-dark` | 极简黑 | 深底、浅字、细线、克制的 accent |
| `tech-blue` | 科技蓝 | 深蓝底 + 亮蓝/青，数据感 |
| `cyber-green` | 赛博绿 | 暗底 + 荧光绿，终端/矩阵感 |
| `neon-purple` | 霓虹紫 | 暗底 + 紫/品红，夜店科技感 |
| `taobao-flash` | 淘宝闪购 | 白底 + 蓝橙双强调，紧凑电商风 |
| `wechat-pai` | 微信派 | 白底 + 微信绿 #07c160，文艺杂志感 |
| `qianwen` | 千问 | 白底 + 近黑字 + 苹果系统字体栈，1.95 行高 + 14px 圆角卡片，轻盈通透 |

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

## 六、预览（可选，推荐用来定稿）

写一个 `preview/preview.html`：把「当前选中的模板 × 主题」渲染成浏览器可打开的整页，用**真实将进微信
的那段内联 HTML** 嵌入（同色、同布局，支持 flex 的部分也如实反映）。**浏览器里看到的 ≈ 微信里看到的**。
用户换模板/主题时对应刷新预览。`preview/preview.html` 默认展示全部 5×4 = 20 种组合画廊，可先看全集再挑一个组合深耕。

---

## 七、扩展与质量要求

- 人名/机构名、专有名词不虚构；只排版，不增删用户原意与事实。
- 颜色遵循主题字典，禁止随手硬编码主题之外的色值。
- 输出 HTML 前自查一遍兼容性铁律；如为效果必须破例，用 `<!-- wx-note: 此处降级说明 -->` 写明。
- 长文如需分段交付，每段都是独立可粘贴的 section，全段首尾粘连即完整文章。

## 相关文件

- `templates/_index.md` 模板清单 —— 选骨架
- `themes/themes.json` 主题注册表 —— 选色板
- `references/wechat-compat.md` 兼容性铁律 —— **生成前必读**
- `references/components.md` 版式块库 —— 拼版零件
- `examples/sample-article.md` 示例草稿 —— 试跑一遍
- `preview/preview.html` 预览画廊 —— 对比 20 种组合
- `generated/<YYYY-MM-DD>/` 当日产出归档 —— 一个带「复制」按钮的 HTML 成品
