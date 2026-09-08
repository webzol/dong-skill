# gzh-skill — 微信公众号排版（合并版）

把公众号文章草稿一键排版成**微信编辑器里真正能显示**的内联样式 HTML。本 skill 由原 dong-skill 仓库的两套公众号排版 skill 合并而成，一份统一入口 + 两套引擎：

| 引擎 | 目录 | 来源 / 许可 | 架构与强项 |
|---|---|---|---|
| **design 引擎** | `engine-design/` | 原 `gzh-design-skill`（import 自 [isjiamu/gzh-design-skill](https://github.com/isjiamu/gzh-design-skill) v1.0.0）· AGPL-3.0 | 主题组件库（6 套主题 + 主题生成器）、docx/PDF 归一化、章节编号/关键词下划线、Python 校验到 0 ERROR、一键复制预览页 |
| **wx 引擎** | `engine-wx/` | 原 `wxskill`（自有，开发主仓库 [webzol/WXSKill](https://github.com/webzol/WXSKill) v0.2.1）· MIT | 5 模板 × 8 主题正交组合、677px 宽度约束、`generated/<日期>/` 单文件归档（带「复制」按钮成品） |

**引擎怎么选**：由 AI 按请求自动路由（规则见 [`SKILL.md`](SKILL.md) 的「路由规则」）。速记版——

- 点名模板（cyber-card / hud / terminal-code…）或主题（tech-blue / qianwen…）、要自由换配色 → **wx 引擎**
- 给的是 Word/PDF、要严格校验、要生成新主题 → **design 引擎**
- 都没提 → 默认 **design 引擎**

## 安装

```bash
git clone https://github.com/webzol/dong-skill.git

# 方式一：一键脚本（复制到 Claude Code / Codex 等 skill 目录）
bash dong-skill/gzh-skill/install.sh                    # macOS / Linux
powershell -File dong-skill\gzh-skill\install.ps1       # Windows

# 方式二：手动
mkdir -p ~/.claude/skills
cp -R dong-skill/gzh-skill ~/.claude/skills/gzh-skill
```

装完**重启 AI 会话**生效。触发方式：斜杠命令 `/gzh-skill`，或自然语言「公众号排版」「gzh」「自动排版」「wechat-typesetting」等。

## 目录结构

```
gzh-skill/
├── SKILL.md                # 统一入口：定位 + 引擎路由规则（AI 先读这份）
├── README.md
├── install.sh / install.ps1
├── engine-design/          # design 引擎（原 gzh-design-skill，内容原样保留）
│   ├── SKILL.md            # design 引擎执行手册
│   ├── references/         # 主题组件库（6 套）+ 主题生成器
│   ├── scripts/            # validate_gzh_html.py 等校验脚本
│   ├── assets/ docs/ archive/ .github/
│   └── LICENSE             # AGPL-3.0
└── engine-wx/              # wx 引擎（原 wxskill，内容原样保留）
    ├── SKILL.md            # wx 引擎执行手册
    ├── templates/          # 5 模板
    ├── themes/             # 8 主题色板
    ├── references/         # 微信兼容铁律 + 版式块库
    ├── examples/ preview/
    └── LICENSE             # MIT
```

## 许可说明

两引擎来源与许可不同，**各自保留原许可**：`engine-design/` 为 AGPL-3.0（版权归原上游作者甲木 × 摸鱼小李），`engine-wx/` 为 MIT。合并仅做目录聚合与入口整合，未修改两引擎的实质内容与许可。

## 维护

- **产出归档**：每次排版统一落 `generated/<YYYY-MM-DD>/`，每篇只交付一个带「复制」按钮的 HTML 成品（约定详见 [`SKILL.md`](SKILL.md)「输出归档约定」）。
- 升级流程、目录约定、踩坑记录见仓库根 [`DEV_NOTES.md`](../DEV_NOTES.md)。
- engine-wx 的持续开发在主仓库 `webzol/WXSKill`（`E:\wxskill`），本目录为其快照；engine-design 走 upstream 同步。
