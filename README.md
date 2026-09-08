# dong-skill

TD 的 AI 工具 skill 集合仓库。每个 skill 独立顶级子目录，克隆后按需安装。

## 包含的 Skill

| Skill | 说明 | 版本 |
|---|---|---|
| [gzh-skill/](gzh-skill/) | 微信公众号文章排版（合并版）：Markdown/Word/PDF/纯文本 → 可直接粘贴公众号编辑器的内联样式 HTML。统一入口内含两套引擎——**design 引擎**（原 gzh-design-skill：主题组件库 + 主题生成器 + 校验脚本）与 **wx 引擎**（原 wxskill：5 模板 × 8 主题 + 产出归档），按请求自动路由 | v1.0.0 |

> 2026-09-08 起，原 `gzh-design-skill/` 与 `wxskill/` 两个顶级目录已合并为 `gzh-skill/`（两套引擎分别移入其 `engine-design/` 与 `engine-wx/`，内容原样保留）。合并决策与升级方式见 `DEV_NOTES.md`。

## 安装方式

```bash
git clone https://github.com/webzol/dong-skill.git

# 方式一：一键脚本（复制到 Claude Code / Codex 等 skill 目录）
bash dong-skill/gzh-skill/install.sh                    # macOS / Linux
powershell -File dong-skill\gzh-skill\install.ps1       # Windows

# 方式二：手动
mkdir -p ~/.claude/skills
cp -R dong-skill/gzh-skill ~/.claude/skills/gzh-skill
```

安装后重启 AI 会话生效。触发方式：斜杠命令 `/gzh-skill`，或自然语言「公众号排版」「gzh」「自动排版」「wechat-typesetting」等（详见 [gzh-skill/SKILL.md](gzh-skill/SKILL.md)）。

## 维护约定

- 根目录 `DEV_NOTES.md` 记录架构决策、升级流程、踩坑，**接手前必读**
- 每个 skill 独立顶级子目录，命名小写、连字符
- gzh-skill 内：engine-design 走 upstream import 流程升级（remote 已配好），engine-wx 从 `E:\wxskill`（webzol/WXSKill）快照同步进来，原仓库是开发主目录
