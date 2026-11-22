---
name: gzh-skill
description: 微信公众号文章排版统一 Skill（由 gzh-design 与 wxskill 两套引擎合并而成）。将 Markdown / Word(.docx) / PDF / 纯文本草稿转换为可直接粘贴进公众号编辑器、粘贴后样式不丢失的内联样式 HTML。内含两套引擎：design 引擎（主题组件库：9 套主题 + 主题生成器 + Python 校验脚本 + 一键复制预览页）与 wx 引擎（5 模板 × 8 主题自由组合 + 产出按日期归档）。触发场景：(1) 用户提到"公众号排版""公众号文章""微信排版""gzh""自动排版""一键排版""wechat-typesetting"，(2) 想把文章（md/docx/pdf/纯文本）转成公众号 HTML，(3) 想换模板/换配色/模板×主题组合，(4) 想生成自定义主题/按参考图做组件库。不用于生成普通网页/落地页/PPT。
---

# 公众号排版 Skill（统一入口）

把文章草稿变成「粘贴进微信公众号编辑器就能正常显示」的内联样式 HTML。

本 Skill 由两套同方向的引擎合并而成，**本文件只做定位与路由（薄入口）**：选定引擎后必须 Read 该引擎的 SKILL.md，并严格按其流程执行；所有 HTML 一律取自引擎自带资产，不要凭记忆手写。

## 引擎一览

| 引擎 | 位置 | 架构 | 强项 |
|---|---|---|---|
| design 引擎（原 gzh-design-skill，2026-09 同步至 9 套主题版） | `engine-design/` | 主题组件库：每套主题 = 一份完整组件库（9 套主题 + 主题生成器） | docx/PDF 输入归一化、章节自动编号、正文关键词下划线、`validate_gzh_html.py` 校验到 0 ERROR、带「复制」按钮的预览页 |
| wx 引擎（原 wxskill v0.2.1） | `engine-wx/` | 模板 × 主题正交组合：5 版式骨架 × 8 色板，自由搭配 | 模板/配色随时可换、677px 宽度约束明确、`generated/<日期>/` 单文件归档（带「复制」按钮成品） |

## 路由规则（按顺序判定，命中即停）

0. **茶类稿件或「茶模型」/ `/chamo`** → **wx 引擎**，先读 `commands/chamo.md`。默认版和备选均用茶模板 × `tea-atelier`。茶知识补写或审稿还须读 `engine-wx/references/tea-knowledge.md`。若输入是 Word/PDF，先提取内容再回到茶模板。维护茶类规则时只做所请求的维护。

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

## 成品风格选择

- 各风格共用用户指定或项目约定的模板与主题。普通 wx 稿默认 `minimal-tech × dongpro`，茶稿按 `commands/chamo.md` 选茶模板并固定 `tea-atelier`。缺少已有偏好时，按正文题材确定适合的组合。
- 按题材从写作风格库选 1–2 种口吻，总数含默认项。用户指定的风格优先，否则以最贴题的一种为默认。若有备选，用同一事实和图片另写一版正文，保持信源口径、图序和版式一致。纯排已定稿时保留原稿一个风格。每版先完成内联样式和兼容性检查，再打包。
- 用户明确要先看样式时，可打开 [design 主题画廊](engine-design/docs/gallery/index.html) 或 [wx 版式选择页](engine-wx/preview/selection.html)。用户明确只要一版时，按单版流程交付。

## 输出归档约定（两引擎文档已同步此约定，此处为总纲）

每次排版产出统一按本节执行：

1. **先建当天文件夹**：在当前工作目录下新建 `generated/<YYYY-MM-DD>/`（本地日期），当次产物只放这一个文件夹；同一天多次排版共用同一天的文件夹。
2. **每篇交付一个 HTML 成品**。design 各版干净正文以 `validate_gzh_html.py` 校验到 0 ERROR 0 WARNING，wx 各版按 `engine-wx/references/wechat-compat.md` 逐项检查。校验通过后用统一预览脚本打包。

   ```text
   python engine-design/scripts/wrap_preview.py default.html final.html --default-label "新智元" --variant "量子位" alternate.html
   ```

   有备选时传一次 `--variant`。同序图片在打包时共享。单版使用 `--default-label "风格名"`，省略 `--variant`。茶稿与本仓库稿件的各版正文源文件、图片映射和源图保留在稿件子目录，供后续修订。
3. `generated/` 不入库：仓库根 `.gitignore` 已忽略该目录。
4. 交付说明固定三句：浏览器打开成品并按需切换写作风格 → 点「复制到公众号」复制当前版 → 到公众号编辑器粘贴。正文含 `{{作者名}}` 等占位时提醒替换。

## 平台共性红线（两引擎一致，完整规则以各自引擎文件为准）

- 微信编辑器会剥掉：`<style>`/`<script>`、class/id 选择器依赖、CSS 变量、伪元素、`@media`、外部字体/CSS；wx 引擎还禁用 flex/grid 与 `position`，design 引擎仅允许有限 flex。
- 样式全部内联 `style`；元素只用 `section / p / span / strong / em / a / img / table / ul / ol / li / br / h3` 这类安全集合。
- `box-shadow` / `border-radius` / `letter-spacing` 谨慎使用，**布局不要依赖**。

## 安装与维护

- 安装：整个 skill 目录复制到 AI 工具的 skill 目录，或直接运行本目录下的 `install.sh`（macOS/Linux）/ `install.ps1`（Windows）。
- 升级与维护约定（含 engine-design 的 upstream 同步流程、engine-wx 的主仓库快照同步）见仓库根 `DEV_NOTES.md`。
- 许可：`engine-design/` 为 AGPL-3.0（见其 LICENSE），`engine-wx/` 为 MIT（见其 LICENSE），许可文件随各自引擎目录保留。

## 写稿口吻（2026-11-16）

**凡涉及「写正文」（不只是照排已定稿草稿），不论题材，先读 `engine-wx/references/writing-style.md`**：按 §2 定腔调，套 §1 共用配方 + §3 该腔细则；开篇样例 `writing-style-samples.md`，语料 `writing-style-corpus/`。该文件是写稿口径的唯一出处，与其它文档冲突时以它为准。排版流程不变。

入口分工：`engine-wx/SKILL.md` 第 0 步为写稿口吻步（AI 稿）；`commands/zaobao.md`（每日热点）、`commands/chamo.md`（茶稿）各自在第 4 步 / 选模板段挂同一份风格文件。
