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
