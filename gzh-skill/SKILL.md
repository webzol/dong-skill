---
name: gzh-skill
description: 微信公众号文章排版统一 Skill（由 gzh-design 与 wxskill 两套引擎合并而成）。将 Markdown / Word(.docx) / PDF / 纯文本草稿转换为可直接粘贴进公众号编辑器、粘贴后样式不丢失的内联样式 HTML。内含两套引擎：design 引擎（主题组件库：6 套主题 + 主题生成器 + Python 校验脚本 + 一键复制预览页）与 wx 引擎（5 模板 × 8 主题自由组合 + 产出按日期归档）。触发场景：(1) 用户提到"公众号排版""公众号文章""微信排版""gzh""自动排版""一键排版""wechat-typesetting"，(2) 想把文章（md/docx/pdf/纯文本）转成公众号 HTML，(3) 想换模板/换配色/模板×主题组合，(4) 想生成自定义主题/按参考图做组件库。不用于生成普通网页/落地页/PPT。
---

# 公众号排版 Skill（统一入口）

把文章草稿变成「粘贴进微信公众号编辑器就能正常显示」的内联样式 HTML。

本 Skill 由两套同方向的引擎合并而成，**本文件只做定位与路由（薄入口）**：选定引擎后必须 Read 该引擎的 SKILL.md，并严格按其流程执行；所有 HTML 一律取自引擎自带资产，不要凭记忆手写。

## 引擎一览

| 引擎 | 位置 | 架构 | 强项 |
|---|---|---|---|
| design 引擎（原 gzh-design-skill v1.0.0） | `engine-design/` | 主题组件库：每套主题 = 一份完整组件库（6 套主题 + 主题生成器） | docx/PDF 输入归一化、章节自动编号、正文关键词下划线、`validate_gzh_html.py` 校验到 0 ERROR、带「复制」按钮的预览页 |
| wx 引擎（原 wxskill v0.2.1） | `engine-wx/` | 模板 × 主题正交组合：5 版式骨架 × 8 色板，自由搭配 | 模板/配色随时可换、677px 宽度约束明确、`generated/<日期>/` 单文件归档（带「复制」按钮成品） |

## 路由规则（按顺序判定，命中即停）

1. 用户**点名 wx 引擎的模板或主题名**——模板：`minimal-tech` / `cyber-card` / `terminal-code` / `hud` / `wechat-pai-essay`；主题：`minimal-light` / `minimal-dark` / `tech-blue` / `cyber-green` / `neon-purple` / `taobao-flash` / `wechat-pai` / `qianwen`；或要求「模板 × 配色自由组合 / 换模板 / 换配色」→ **wx 引擎**
2. 输入是 **.docx 或 .pdf** → **design 引擎**（走其 format-normalize + extract_docx 流程）
3. 要求**生成新主题 / 自定义风格 / 按参考图做一套组件库** → **design 引擎**（theme-generator 工作流）
4. 要求**产出归档**（generated/日期/ 目录）→ **wx 引擎**
5. 其余情况（含「公众号排版」「自动排版」等无附加要求）→ **design 引擎**（校验闭环更严、文章化处理更全）

**冲突处理**：同时命中多条时，用户显式点名的优先；无法判定时用第 5 条默认。用户对路由选择有疑问时，说明「当前用的是 X 引擎（原因），可以换 Y 引擎重排」。

## 路由后怎么做

- Read `engine-design/SKILL.md` 或 `engine-wx/SKILL.md`。**此后该引擎文件里提到的相对路径，一律相对其引擎目录解析**（design 引擎 → `engine-design/…`，wx 引擎 → `engine-wx/…`），包括 references / templates / themes / scripts / examples。
- **两引擎资产互不混用**：不要拿 wx 的主题 JSON 去填 design 的组件库，也不要把 design 的组件 HTML 塞进 wx 的模板骨架。
- 校验脚本用绝对路径调用：`<本 skill 安装根目录>/engine-design/scripts/validate_gzh_html.py`。

## 主题选择约定（覆盖两引擎的默认主题行为，用户体验第一）

- **用户没指定主题时，必须立即自动弹出交互式风格选择框让用户点选，不得自行默认，也不得只列纯文本清单等用户打字回复**。清单范围 = 两引擎全部主题：design 引擎 6 套（摸鱼绿 / 橄榄手记 / 摸鱼票据风 / 红白色系 / 石墨极简风 / 留白禅意风）+ wx 引擎 8 套色板（minimal-light 极简白 / minimal-dark 极简黑 / tech-blue 科技蓝 / cyber-green 赛博绿 / neon-purple 霓虹紫 / taobao-flash 淘宝闪购 / wechat-pai 微信派 / qianwen 千问）。
- **弹框体验要求（UX 优先）**：
  - 用 AI 工具的交互选择组件（如 Claude Code 的 AskUserQuestion / ZCode 的 AskUserQuestion）弹出，用户点选即回，**不打字、不来回追问**。
  - 选项数超过弹框上限（通常 4 个）时两步走：第一层弹「design 主题 / wx 色板 / 看画廊再选」，第二层弹该组内全部主题；或第一层直接放 4 个最契合题材的（标注「推荐」）+「看全部 14 套」兜底项。
  - 每个选项带一句话风格描述；题材契合的标「推荐」放第一位，但不替用户定。
  - 选题与问其他问题（如确认结构）**合并成一轮**，能一次问完的不拆两次。
  - 用户选 wx 色板后，模板选择框**紧接着弹出**（minimal-tech / cyber-card / terminal-code / hud / wechat-pai-essay），除非已一并点名。
  - 可在弹框中附画廊路径供先看效果：design 画廊 `engine-design/docs/gallery/index.html`、wx 画廊 `engine-wx/preview/preview.html`。
- **唯一例外**：用户明确说「直接排 / 一键 / 不用问」放弃选择时，才自动选最契合的主题（wx 引擎用其默认组合）并在交付时说明理由。
- 两引擎文档中与此冲突的默认规则（design 引擎「默认首选第一行」、wx 引擎「缺省用默认组合」），以本节为准。

## 输出归档约定（两引擎文档已同步此约定，此处为总纲）

每次排版产出统一按本节执行：

1. **先建当天文件夹**：在当前工作目录下新建 `generated/<YYYY-MM-DD>/`（本地日期），当次产物只放这一个文件夹；同一天多次排版共用同一天的文件夹。
2. **只交付一个成品文件**：文件夹里最终只留**一个**带「复制」按钮、可直接粘贴公众号编辑器的 HTML（文件名用简短主题概括，如 `两个AI排版skill合并复盘.html`）。
   - design 引擎：干净 `<section>` 正文只作为校验中间产物——`validate_gzh_html.py` 跑到 0 ERROR 0 WARNING 后，用 `engine-design/scripts/wrap_preview.py <干净正文> <成品文件名>` 包出带「复制」按钮的成品，**随后删除中间的干净正文**，不留两份。
   - wx 引擎：生成内联 HTML 后，同样用 `engine-design/scripts/wrap_preview.py` 包一层带「复制」按钮的预览外壳再交付；`source.md` / `README.md` 归档三件套不再默认生成（用户明确要求时才附）。
3. `generated/` 不入库：仓库根 `.gitignore` 已忽略该目录。
4. 交付说明固定三句：浏览器打开成品 HTML → 点右上角「复制到公众号」→ 到公众号编辑器粘贴；正文含 `{{作者名}}` 等占位时提醒替换。

## 平台共性红线（两引擎一致，完整规则以各自引擎文件为准）

- 微信编辑器会剥掉：`<style>`/`<script>`、class/id 选择器依赖、CSS 变量、伪元素、`@media`、外部字体/CSS；wx 引擎还禁用 flex/grid 与 `position`，design 引擎仅允许有限 flex。
- 样式全部内联 `style`；元素只用 `section / p / span / strong / em / a / img / table / ul / ol / li / br / h3` 这类安全集合。
- `box-shadow` / `border-radius` / `letter-spacing` 谨慎使用，**布局不要依赖**。

## 安装与维护

- 安装：整个 skill 目录复制到 AI 工具的 skill 目录，或直接运行本目录下的 `install.sh`（macOS/Linux）/ `install.ps1`（Windows）。
- 升级与维护约定（含 engine-design 的 upstream 同步流程、engine-wx 的主仓库快照同步）见仓库根 `DEV_NOTES.md`。
- 许可：`engine-design/` 为 AGPL-3.0（见其 LICENSE），`engine-wx/` 为 MIT（见其 LICENSE），许可文件随各自引擎目录保留。
