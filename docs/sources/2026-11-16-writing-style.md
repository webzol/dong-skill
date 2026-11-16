# 2026-11-16 · 写作风格接入全部入口（writing-style）

## 背景

本机 `gzh-skill` 已新增写稿风格库 `engine-wx/references/writing-style.md`（四腔：新智元 / 卡兹克 / 量子位 / ASI）+ `writing-style-samples.md` + `writing-style-corpus/`。入库提交见 `49ca3de`。

入库后发现的口径漏洞：该文件当时只被 4 处引用（根 `AGENTS.md`、`gzh-skill/SKILL.md`、`engine-wx/DAILY_NEWS_WORKFLOW.md`、它自己），而 agent 做排版时被要求必读的 **`engine-wx/SKILL.md` 里零引用**——「排版」拿得到，「写稿口吻」拿不到。

## 本次改动：把风格挂进所有读得到的入口

| 入口文件 | 改动 |
|---|---|
| `gzh-skill/engine-wx/SKILL.md` | ① 模式段新增「写稿口吻」说明；② 新增 **第 0 步 写稿口吻（需要写正文时必做）**，位于「第 1 步 读懂草稿」之前；③「相关文件」补齐 writing-style / samples / corpus / tea-knowledge；④「七、扩展与质量要求」加口吻条 |
| `gzh-skill/engine-wx/AGENTS.md` | 新增「写作风格（写正文前必读）」整节；`references/` 清单补齐 |
| `gzh-skill/commands/zaobao.md` | 第 4 步写稿前置「先读 writing-style.md 定腔调」 |
| `gzh-skill/commands/chamo.md` | 选模板段加「写正文前读 writing-style.md」（茶稿取腔：知识=量子位式，文化/器=卡兹克式）；执行第 1 步加口吻文件 |
| `gzh-skill/SKILL.md` | 「写稿口吻」节由「写 AI/模型稿时」放宽为「凡涉及写正文，不论题材」，并列出各入口分工 |
| 根 `AGENTS.md` | 「常驻约定」新增写正文先读风格库一条（含「冲突以它为准 / 小标题不用问句」） |
| `CLAUDE.md` / `GEMINI.md` / `.cursorrules` | 各自新增「写稿口吻」转发段（这三份是转发型入口，此前完全没提） |
| `install.ps1` / `install.sh` | 斜杠命令复制由只装 `zaobao.md` 扩为 `zaobao.md` + `chamo.md`（茶模型此前没装进命令目录） |

## 口径冲突处理

`writing-style.md` 定为**写稿口径唯一出处**，冲突时以它为准，最典型一条：旧文档写「小标题可用问句」，风格库要求「小标题结论式短句、不用问句」。已在 `engine-wx/SKILL.md`、`engine-wx/AGENTS.md`、根 `AGENTS.md`、三份转发入口写明。

## 同时订正的事实错误

`writing-style.md` §5 原写「每条含 `*-content.html`、`*-cover.jpg`、部分 `*-full.html`」——语料里实际只有 `*-body.txt` + `*-style.json`，属虚报。已改为实际构成，并注明：

- `ref-马斯克首次实现-筷子夹飞船-SpaceX改写人类航天史` 仅有 `style.json`（原始正文缺失，可读其 `paragraph_preview` 25 段 + `short_lines` 18 条）；
- `anthropic-crazy-chart-*` 与 `main-style-ref-*` 为同一篇两种命名，内容一致。

## 未做（需用户确认）

- **未跑 `install.ps1`**：本机 `~/.agents/skills/gzh-skill` 仍是 2026-10-27 的旧副本（`references/` 里只有 `components.md` + `wechat-compat.md`，无 writing-style、无茶模板、无 ai-model）。该脚本是**整包替换**（先 `Remove-Item -Recurse` 再复制），会覆盖仓库外的目录，待确认后执行。

## 验证

- 各入口 `grep -c writing-style`：`engine-wx/SKILL.md` 8、`engine-wx/AGENTS.md` 6、根 `AGENTS.md` 2、`chamo.md` 2、`SKILL.md`/`zaobao.md`/`DAILY_NEWS_WORKFLOW.md`/`CLAUDE.md`/`GEMINI.md`/`.cursorrules` 各 1。
- 本次只改规则文档，未改任何文章源稿，按 `chamo.md` 约定**不重生成历史文章**。

## 补记：已执行安装同步（2026-11-16）

用户确认后执行 `powershell -ExecutionPolicy Bypass -File gzh-skill/install.ps1`（整包替换），结果：

- 覆盖前核对：已装副本无「仓库里没有」的文件，覆盖**不丢任何东西**；两份已装副本（`.claude` / `.agents`）当时逐字节一致。
- 写入：`~/.claude/skills/gzh-skill`、`~/.agents/skills/gzh-skill`（各 131 → 164 个文件）。
- 命令：`~/.claude/commands/` 与 `~/.config/opencode/command/` 各装 `zaobao.md` + `chamo.md`（此前只有 zaobao.md）。
- 核对：`references/writing-style.md`、`writing-style-samples.md`、`writing-style-corpus/`、7 套茶模板、`ai-model` 模板、`ai-lab` 主题、`tea-knowledge.md` 均已到位；副本与仓库逐字节一致（`diff -rq` 无输出）。
- 已装副本内引用数：`SKILL.md` 1 / `engine-wx/SKILL.md` 8 / `engine-wx/AGENTS.md` 6 / `commands/chamo.md` 2 / `commands/zaobao.md` 1。

## 已知未覆盖（不属本次范围）

- `~/.config/opencode/skill/` 下仍是旧的 `gzh-design`（9-09）与 `draw`，**没有** `gzh-skill` 整包；`install.ps1` 不写这个目录。若要用 opencode 直接认到本技能，需另行安装或告知路径。
- 全局入口 `~/.claude/CLAUDE.md` 等用户级指令文件不受 install 影响；仓库根的 `CLAUDE.md`/`GEMINI.md`/`.cursorrules` 只在本仓库工作时生效。
