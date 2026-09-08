# WXSkill — 微信公众号排版 Skill

把公众号文章草稿，一键排版成**微信编辑器里真正能显示**的科技感 / 简约风 / 文艺风图文。

- 🎨 **8 个色调主题**：极简白 / 极简黑 / 科技蓝 / 赛博绿 / 霓虹紫 / 淘宝闪购 / 微信派 / 千问（可自行加，任意改色值）
- 🧱 **5 个排版模板**：简约科技 / 卡片 / 终端风 / 数据面板 / 微信派·文艺长文（可自行加）
- 📁 **按日期归档产出**：每次排版自动落到 `generated/YYYY-MM-DD/`，三件套（原稿 + HTML + 说明）便于二次挑选
- 📱 **微信原生兼容**：内联样式 + `<section>/<table>`，无 flex/grid，粘贴即用不塌版
- 🧰 **跨 AI 工具安装**：Claude Code / OpenAI Codex / Cursor / Gemini CLI / Copilot / Windsurf 通吃

---

## 一、一键安装（推荐）

任选其一，自动复制到所有主流 AI 工具的技能目录：

```bash
# Windows (PowerShell)
.\\install.ps1

# macOS / Linux
bash install.sh
```

脚本会把本包复制到：
- `~/.claude/skills/wechat-typesetting/`（Claude Code）
- `~/.agents/skills/wechat-typesetting/`（Codex 及开放 Agent Skills 标准的工具）

装完**重启你的 AI 会话**即可生效。

## 二、手动安装

**Claude Code**（二选一）

```bash
# 全局（所有项目可用）
mkdir -p ~/.claude/skills
cp -r . ~/.claude/skills/wechat-typesetting

# 或仅当前项目
mkdir -p .claude/skills
cp -r . .claude/skills/wechat-typesetting
```

**OpenAI Codex**（开放标准路径）

```bash
mkdir -p ~/.agents/skills
cp -r . ~/.agents/skills/wechat-typesetting
```

**其他支持 Agent Skills 标准的 AI 工具**（Cursor、Gemini CLI、Copilot…）
读 `.agents/skills/` 或 `AGENTS.md`，同样复制即可。

## 三、使用

```text
/wechat-typesetting 我的文章.md --template cyber-card --theme tech-blue
```

或直接对它说：「把这篇排版成科技蓝、卡片模板」。参数可缺省（默认简约科技 + 极简白）。

## 四、新增主题 / 模板

- **加色调**：复制 `themes/` 下一个 `.json`，改 `colors`，再在 `themes/themes.json` 登记 `file`。
- **加模板**：复制 `templates/` 下一个 `.md`，改骨架与占位符，在 `templates/_index.md` 登记。

## 五、目录

```
wechat-typesetting/
├── SKILL.md              # skill 主指令
├── AGENTS.md             # 跨工具说明（Codex/Cursor/Copilot 读它）
├── templates/            # 版式骨架（5 模板）
├── themes/               # 色调色板（8 主题）
├── references/           # 微信兼容铁律 + 版式组件库
├── examples/             # 长期示例（写进 git）
├── generated/            # 当日产出归档（不入库，按 YYYY-MM-DD/ 组织）
│   └── YYYY-MM-DD/
│       ├── source.md
│       ├── <theme>-<template>-<slug>.html
│       └── README.md
└── preview/              # 40 组合预览画廊（8 主题 × 5 模板）
```

每次排版会自动落档到 `generated/<YYYY-MM-DD>/`，三件套齐全便于二次挑选与复盘。

## 许可

MIT —— 任何人可安装、可修改、可再分发。

> 提示：微信会严格剥离部分 CSS，个别机型的 `box-shadow` / `border-radius` 可能弱化；
> 这是微信平台限制，Skill 已用「简约节奏感」规避对布局的依赖。详见 `references/wechat-compat.md`。
