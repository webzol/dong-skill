# AGENTS.md — WXSkill 微信公众号排版 Skill

本仓库是**一个可安装的 Agent Skill**（开放 Agent Skills 标准），仓库根即 skill 包。
作用：把文章草稿排版成微信公众平台「可直接粘贴」的科技感 / 简约风 HTML。

## 这是什么

- `SKILL.md` —— skill 主指令（`name: wechat-typesetting` / `description` 触发词）。任何读到本目录的
  AI 工具（Codex、Cursor、Claude Code、Gemini CLI、Copilot、Windsurf…）都可以把本项目当成技能用。
- `templates/` —— 版式骨架：`minimal-tech` / `cyber-card` / `terminal-code` / `hud`。
- `themes/` —— 色调色板：`themes.json` 注册表 + `minimal-light` / `minimal-dark` / `tech-blue` / `cyber-green` / `neon-purple`。
- `references/` —— `wechat-compat.md`（微信编辑器兼容性铁律）+ `components.md`（可复用版式块）。
- `examples/` —— 一段示例草稿，拿来跑一遍。
- `preview/` —— 5 主题 × 4 模板共 20 种组合的预览画廊（浏览器打开对比）。

## 作为 Agent 的用法

若你是一个正在编辑公众号文章的 AI 工具：

1. 读 `SKILL.md`，按其工作流执行（读懂草稿 → 选模板+主题 → 生成内联样式、约 677px 宽、无 flex/grid 的 HTML）。
2. 每个模板/主题的具体骨架与色值读取对应文件，**不要臆造**。
3. 生成前务必看 `references/wechat-compat.md`，输出内联样式 HTML，禁 flex/grid/var()/伪元素/外部样式表。

若你是用户来安装这个 skill，请直接看 `README.md` 即最简安装路径。

## 每日热点写作（固定流程，跨模型通用）

当用户说 **`早报` / `今天的热点` / `每日 3 篇` / `按每日流程跑`**，或直接贴 X「Today's News」截图时：

1. 读 `DAILY_NEWS_WORKFLOW.md`，严格按里面 9 个环节执行；
2. 产出 **3 篇** AI 大模型热点文章，模板 `minimal-tech` + 主题 `dongpro`；
3. 配图必须**内嵌在对应正文位置**（`components.md` §13 样式），**图下不加任何文字**；
   长截图不整张放，按 `-Scale 3` 截取后切段嵌入；
4. 图片获取用 `scripts/xshot.ps1`（Chrome headless + 普通 UA）→ `scripts/bands.py` 探内容块边界 → `scripts/crop.py` 裁；
   各站截图参数、裁剪坐标、落点约定见 `DAILY_NEWS_WORKFLOW.md` §3.5 / §3.6，**不要**用 `browser.*` 去开 x.com（连不上）；
5. 组装用 `scripts/inject_images.py` → `engine-design/scripts/wrap_preview.py`，串行执行；
6. 落盘 `E:\WX\<YYYY-MM-DD>\`，并在 `generated/<date>/` 留一份备份；
7. 写信源台账 `generated/<date>/sources.md`（结论/配图 ← URL + 页面位置），格式见 §7.1；
8. 交付三句用法 + 「本版 = 模板 X + 主题 Y」。

细节、坑位与命令示例都在 `DAILY_NEWS_WORKFLOW.md`，不要凭记忆简化。

**生效条件**：本目录不在工作区时规则不会自动读入（需 `install.ps1` 装成 skill，或把路径告诉 AI）；
在本仓库里被唤醒但用户没给具体任务时，先问一句「跑今天的早报，还是排版某篇稿子？」。
