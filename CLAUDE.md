# CLAUDE.md

@AGENTS.md

## 每日 AI 热点（Claude Code 入口）

用户说 **`早报` / `今天的热点` / `每日 3 篇` / `按每日流程跑`**，或直接贴 X「Today's News」截图时：

1. 读 `gzh-skill/engine-wx/DAILY_NEWS_WORKFLOW.md`，按里面 9 个环节执行；
   （信源清单 §1.1 · 抓图参数与坐标 §3.5 · 信源台账 §7.1）
2. 产出 3 篇，模板 `minimal-tech` × 主题 `dongpro`；
3. 配图内嵌对应位置、**图下不加文字**；长图切段不放整张；开头不写时间；标题 16px / 小节标题 17px / 不带中文序号；
4. 成品落盘 `E:\WX\<YYYY-MM-DD>\`，备份 `generated/<date>/`；
5. 交付三句用法 + 「本版 = 模板 X + 主题 Y」；
6. **铁律**：每次改稿或改规则，改完立刻 `git add -A` → `commit` → `push`，回复里报 commit 短号，工作区不许留未提交改动。

## 茶模型（Claude Code 入口）

内容涉及茶（茶知识 / 茶文化 / 茶器 / 茶史 / 茶席 / 冲泡 / 存茶），或用户说 **`茶模型`** / `/chamo` 时：
主题固定 `tea-atelier`，模板六选一（`tea-notes` / `tea-almanac` / `tea-culture` / `tea-scroll` / `tea-ware` / `tea-catalog`），
流程与硬规则见 `gzh-skill/commands/chamo.md`。不要用默认科技风。

> 本文件只做入口转发，规则以 `AGENTS.md` 与 `DAILY_NEWS_WORKFLOW.md` 为准，不要在这里另写一套。
