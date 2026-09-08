# DEV_NOTES — dong-skill

> 接手的 Codex/AI 先看这里。本文件记录项目演进过程中的关键决策、踩坑和遗留事项。

---

## 1. 项目定位

dong-skill（GitHub: webzol/dong-skill）是 skill 集合仓库，托管 TD 自有或精选的 Codex skill。

- 本地路径：E:\dong-skill
- 当前内容：
  - gzh-skill/（公众号排版合并版 skill，v1.0.0，2026-09-08 由原 gzh-design-skill 与 wxskill 合并而成）
    - engine-design/（原 gzh-design-skill，从 isjiamu/gzh-design-skill v1.0.0 import）
    - engine-wx/（原 wxskill，自有 skill v0.2.1，源自 webzol/WXSKill，2026-09-08 加入）

---

## 2. 目录约定

每个 skill 独立顶级子目录，命名小写、连字符；skill 内部可再按引擎分子目录。

`
E:\dong-skill\
├── .git\
├── DEV_NOTES.md
├── README.md
└── gzh-skill\                 公众号排版统一 skill（双引擎）
    ├── SKILL.md               统一入口：定位 + 引擎路由规则（薄入口，AI 先读这份）
    ├── README.md
    ├── install.sh / install.ps1   一键安装（整体复制 gzh-skill 到各 AI 工具 skill 目录）
    ├── engine-design\         design 引擎 = 原 gzh-design-skill，内容原样保留
    │   ├── SKILL.md           引擎执行手册（保留原文件名，便于 upstream 同步）
    │   ├── references\ scripts\ assets\ docs\ archive\ .github\
    │   └── LICENSE            AGPL-3.0（上游作者：甲木 × 摸鱼小李）
    └── engine-wx\             wx 引擎 = 原 wxskill，内容原样保留
        ├── SKILL.md           引擎执行手册
        ├── templates\ themes\ references\ examples\ preview\
        └── LICENSE            MIT
`

---

## 3. 关键决策

### 3.1 子目录 vs 根目录 merge
- dong-skill 名字暗示集合，根目录被单个 skill 占满不利扩展
- 子目录命名跟远端同名，方便 git log --follow 追溯单个文件历史
- 不污染 dong-skill 自身的根级文件

### 3.2 git archive vs merge --allow-unrelated-histories
- 后者把 gzh-design-skill 的全部历史 commit 铺到 dong-skill main
- 前者只 import 工作树内容，dong-skill main 上只有 1 个 import commit
- 完整原历史保留在 .git/objects/ 里，可通过 git log --follow 追溯

### 3.3 保留 gzh-design-skill remote
- 后续升级不需要重填 URL
- 升级命令固化（见第 5 节）

### 3.4 wxskill 的引入方式（2026-09-08）
- wxskill 是自有仓库（webzol/WXSKill），与 gzh-design-skill 的「upstream import」性质不同
- 处理：直接 cp -r 快照进 dong-skill/wxskill/，删除其内嵌 .git（避免嵌套仓库/子模块歧义）
- 原仓库 E:\wxskill 仍是开发主目录，继续独立维护
- 后续同步：wxskill 有更新时，重复 cp -r + rm .git + commit 即可（可写个小脚本固化）

### 3.5 两 skill 合并为 gzh-skill（2026-09-08）
- 背景：两个 skill 都是公众号排版，定位有重叠，使用者没必要装/触发两个
- **决策：双引擎统一入口，不做深度架构统一**
  - 新建 `gzh-skill/`，根 SKILL.md 只写定位 + 路由规则（薄入口）；两套引擎目录原样移入 `engine-design/`、`engine-wx/`，内部文件不改
  - 为什么不深合并：gzh-design 是「每主题 = 完整组件库」，wxskill 是「模板骨架 × 色板 JSON」正交组合，两种架构互转都要重写大量组件且丢功能（校验闭环 / 模板自由组合二选一），收益低风险高
  - 路由默认 design 引擎（校验更严）；点名 wx 模板/主题、docx/PDF、生成新主题等信号分流，规则固化在 gzh-skill/SKILL.md
- 引擎子目录里的 SKILL.md **保留原名不改**：一是内部大量文件互相引用「SKILL.md 第 X 步」；二是 skill 加载器只识别 `skills/<名>/SKILL.md` 一层，嵌套 SKILL.md 不会被当成独立 skill，无冲突
- install.sh / install.ps1 从 engine-wx 提升到 gzh-skill 根，安装名改为 `gzh-skill`（原 `/wechat-typesetting` 斜杠命令由 `/gzh-skill` 取代，description 里保留了旧触发词）
- **许可注意**：engine-design 是 AGPL-3.0、engine-wx 是 MIT，各自 LICENSE 随引擎目录保留；合并属于聚合分发，不要把两目录内容互相拷贝后改成单一许可
- 旧目录已删（git 历史可找回：合并前的 commit 里有完整 gzh-design-skill/ 与 wxskill/）

### 3.6 输出归档约定：generated/<日期>/ 单文件交付（2026-09-08，TD 提出）
- 规则：每次排版新建 `generated/<YYYY-MM-DD>/`，最终只留**一个**带「复制」按钮的 HTML 成品；design 的干净正文仅作校验中间产物（包按钮后删除），wx 的 source/README 三件套不再默认生成
- 落点：约定写在 gzh-skill/SKILL.md「输出归档约定」一节，并声明优先级高于两引擎文档的输出步骤——引擎文件保持原样不动，upstream 同步不会被覆盖
- 复制按钮方案：复用 engine-design 的 wrap_preview.py（按钮和脚本只在预览外壳里，粘出去的仍是干净正文），对 wx 引擎产出的 section 同样适用
- 仓库根新增 .gitignore 忽略 generated/
- 2026-09-08 再补充（TD）：该规则**已直接写进两引擎 SKILL.md 的输出章节**（engine-design 第 6 步 / engine-wx 第 4、4.5 步），不再只靠统一入口覆盖——任意入口读到都生效
- ⚠️ 同步注意：engine-design 走 upstream 整目录替换（见 5.1）会覆盖此改动，同步后需重打「输出目录约定」一节；engine-wx 从 E:\wxskill 快照同步同理（或把该节改动先合入主仓库 E:\wxskill 的 SKILL.md，一劳永逸）

### 3.7 主题选择约定：不指定就问，不默认（2026-09-08，TD 提出）
- 用户没指定主题时必须列出全部可选主题让用户选，不得自行默认（可标「推荐」但不能替用户定）
- 2026-09-08 补充（TD）：主题清单必须**两引擎合并列出**（design 6 套 + wx 8 色板全量），不得只列单引擎；选 wx 色板即路由 wx 引擎，且模板也要问、不默认
- 唯一例外：用户明确说「直接排 / 不用问」放弃选择时才自动选，交付时说明理由
- 写在 gzh-skill/SKILL.md「主题选择约定」，优先级高于两引擎文档的默认主题规则（design「默认第一行」、wx「缺省简约科技 × 极简白」）；引擎文件保持原样
- 2026-09-08 再补充（TD）：**必须自动弹出交互式选择框**（AskUserQuestion 类组件）让用户点选，UX 优先——不打字回复、不来回追问；选项超上限先按引擎分组或「推荐 4 + 看全部」两步走；选题与其他确认合并一轮；选 wx 色板后紧接弹模板选择框

### 3.8 安装完成输出使用提示（2026-09-08，TD 提出）
- install.sh / install.ps1 末尾固定打印使用提示：触发方式（「公众号排版」//gzh-skill）、点名主题示例（「排版文章使用千问 qianwen 主题」）、wx 模板示例、不指定主题会列 14 套让用户选、产物归档到 generated/<日期>/ 单文件带复制按钮
- 目的：装完即知道怎么用，不需要再去翻 README

---

## 4. 踩过的坑（避免重蹈）

### 4.1 sandbox 不允许 git read-tree 写 .git/index
执行 git read-tree -u --prefix=... 会失败：Permission denied: .git/index.lock。
fetch 能成功是因为只写 objects/ 和 packed-refs，不写 index。
绕开方式：git archive 从本地 objects 导出 tar 流再 tar -x，或者直接 clone 到临时目录拷文件。

### 4.2 sandbox 不允许写 E 盘
E:\ 不在 Codex 默认 writable_roots，所有写 E 盘的操作（git add/commit/push、文件 mv/cp/rm）都必须 require_escalated。

### 4.3 git clone 有内容时偶发 TLS 凭证失败
症状：fatal: schannel: AcquireCredentialsHandle failed SEC_E_NO_CREDENTIALS。
空仓库能 clone（无 objects 下载），非空有时失败。
当前可用策略：先用 git fetch 把 objects 拉到本地 .git/objects/，再用 git archive 离线导出。

### 4.4 当前 shell 是 PowerShell 不是 Git Bash
AGENTS.md 写的是 Git Bash，但 Codex 当前实际是 PowerShell。管道符 | 走 PowerShell 解析，跟 bash 行为有差异。写命令时优先用 Get-ChildItem、Select-Object 等 PowerShell 原生语法，少用 unix 工具链。

---

## 5. 升级 gzh-skill 引擎的标准流程

### 5.1 engine-design（upstream）

`powershell
cd E:\dong-skill
git fetch gzh-design-skill
# 预览变更（不实际改文件）：git archive --format=tar gzh-design-skill/main | tar -df - -C gzh-skill\engine-design
Remove-Item -Recurse -Force gzh-skill\engine-design
git archive --format=tar --prefix=gzh-skill/engine-design/ gzh-design-skill/main | tar -x -f - -C .
git add -A
git commit -m 'update: gzh-skill/engine-design from upstream'
git push origin main
`

- upstream 同步是整目录替换，合并时对 engine-design 没有做过内容改动，所以可无损重复执行
- 唯一注意：upstream 的 README 若提到安装方式，按 gzh-skill/README.md 为准（引擎 README 有同步注释）

### 5.2 engine-wx（自有主仓库快照）

wxskill 在 E:\wxskill（webzol/WXSKill）继续开发，有更新时：

`powershell
cd E:\dong-skill
Remove-Item -Recurse -Force gzh-skill\engine-wx
Copy-Item -Recurse E:\wxskill gzh-skill\engine-wx
Remove-Item -Recurse -Force gzh-skill\engine-wx\.git   # 避免嵌套仓库
git add -A
git commit -m 'update: gzh-skill/engine-wx snapshot from WXSKill'
git push origin main
`

注意：engine-wx 的 install.sh/install.ps1 已提升到 gzh-skill 根目录，同步后若 E:\wxskill 里又出现安装脚本，删掉引擎目录里的那份，保持只有根上一份。engine-wx/README.md 顶部的「已并入 gzh-skill」注释是本地改动，同步后需检查是否被覆盖。

---

## 6. 远端 / 分支

| remote | URL | 用途 |
|---|---|---|
| origin | https://github.com/webzol/dong-skill.git | 本仓库主地址，push 目标 |
| gzh-design-skill | https://github.com/isjiamu/gzh-design-skill.git | upstream，升级用，不要 push |

分支：main（唯一活跃分支，承载所有 import 内容）

---

## 7. 待办 / 待 TD 决策

- [ ] dong-skill 根目录是否加 README.md 索引所有 skill（目前访问者只能看到单个 commit message）→ ✅ 已加（2026-09-08，e8fe973）：索引两个 skill + 各自安装方式 + 维护约定
- [ ] 是否加 CI（gzh-design-skill 自带 .github/，但没动它）
- [ ] 是否把 webzol/dong-skill 改成 organization 名（目前是 user 仓库）
- [ ] v1.0.0 之前的 tag（assets-v1）没同步到 dong-skill，需要的话 git push origin assets-v1
