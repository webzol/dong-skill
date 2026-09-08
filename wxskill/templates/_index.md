# 模板清单（选版式骨架）

| 模板 | 定位 | 版式重点 |
|---|---|---|
| `minimal-tech` | 简约科技 · **默认** | 细标题线 + 大留白 + 干净信息流 |
| `cyber-card` | 卡片风 | 圆角卡片分隔块，最有产品感 |
| `terminal-code` | 终端风 | 等宽标题 + 命令符 `>` + 代码高亮块 |
| `hud` | 数据面板 | 指标大字 + 迷你条 + 面板框，适合 KPI/评测/榜单 |
| `wechat-pai-essay` | 微信派·文艺长文 | PingFang + 1px 字距 + 两端对齐 + 1.6 行高 + 微信绿强调，适合品牌叙事/长文 |

**通用约定：**

- 所有模板只用**内联样式**的 `section / p / span / table / td / img / strong / em / a`，**禁 flex / grid**。
- 骨架里的 `{{accent}}`、`{{text}}`、`{{bg}}`、`{{cardBg}}`、`{{divider}}` 等是**占位符**，生成时全部替换成主题色（读对应 `themes/<theme>.json`）。
- 原子版式块（标题栏 / 引言 / 卡片 / 分隔 / 代码 / 按钮 / 脚注）在 `references/components.md`，模板负责**节奏与骨架**，组件负责**细节块**。
- 全文最外层：`<section style="max-width:677px;margin:0 auto;background:{{bg}};color:{{text}};padding:24px 18px;box-sizing:border-box;">`。

**新增模板**：复制本目录下一个 `.md`，改骨架与占位符，并在上方表格登记。
