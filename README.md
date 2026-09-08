# dong-skill

TD 的 AI 工具 skill 集合仓库。每个 skill 独立顶级子目录，克隆后按需安装。

## 包含的 Skill

| Skill | 说明 | 版本 | 来源 |
|---|---|---|---|
| [gzh-design-skill/](gzh-design-skill/) | 公众号文章排版：Markdown/Word/PDF → 可直接粘贴公众号编辑器的 HTML，6 套主题 + 主题生成器 + 双关卡质量校验 | v1.0.0 | import 自 [isjiamu/gzh-design-skill](https://github.com/isjiamu/gzh-design-skill) |
| [wxskill/](wxskill/) | 微信公众号排版（自有）：草稿 → 科技感/简约风富文本 HTML，5 模板 × 8 主题，内联样式兼容微信编辑器，按日期归档产出 | v0.2.1 | 自有，开发主仓库 [webzol/WXSKill](https://github.com/webzol/WXSKill) |

两个 skill 都是公众号排版方向，定位略有差异：gzh-design 偏「主题组件库 + 质量校验」，wxskill 偏「模板 × 主题组合 + 产出归档」，可按需选用。

## 安装方式

### gzh-design-skill

克隆本仓库后，把子目录复制到 AI 工具的 skill 目录：

```bash
git clone https://github.com/webzol/dong-skill.git
# Claude Code 全局
mkdir -p ~/.claude/skills
cp -R dong-skill/gzh-design-skill ~/.claude/skills/gzh-design
# Codex / 开放 Agent Skills 标准
mkdir -p ~/.agents/skills
cp -R dong-skill/gzh-design-skill ~/.agents/skills/gzh-design
```

安装后重启 AI 会话生效，触发词：「公众号排版」「gzh」「自动排版」等（详见其 SKILL.md）。

### wxskill

自带一键安装脚本，复制到所有主流 AI 工具的 skill 目录：

```bash
git clone https://github.com/webzol/dong-skill.git
cd dong-skill/wxskill
bash install.sh        # macOS / Linux
# 或 Windows PowerShell:
powershell -File install.ps1
```

安装后重启 AI 会话生效，斜杠命令：`/wechat-typesetting 文章.md --template cyber-card --theme tech-blue`（详见其 SKILL.md）。

## 维护约定

- 根目录 `DEV_NOTES.md` 记录架构决策、升级流程、踩坑，**接手前必读**
- 每个 skill 独立子目录，命名与来源仓库同名（小写、连字符）
- gzh-design-skill 走 upstream import 流程升级（remote 已配好）
- wxskill 从 `E:\wxskill`（webzol/WXSKill）快照同步进来，原仓库是开发主目录
