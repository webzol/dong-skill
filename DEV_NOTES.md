# DEV_NOTES — dong-skill

> 接手的 Codex/AI 先看这里。本文件记录项目演进过程中的关键决策、踩坑和遗留事项。

---

## 1. 项目定位

dong-skill（GitHub: webzol/dong-skill）是 skill 集合仓库，托管 TD 自有或精选的 Codex skill。

- 本地路径：E:\dong-skill
- 当前内容：
  - gzh-design-skill/（从 isjiamu/gzh-design-skill v1.0.0 import）
  - wxskill/（自有 skill，v0.2.1，源自 webzol/WXSKill，2026-09-08 加入）

---

## 2. 目录约定

每个 skill 独立顶级子目录，命名与远端同名（小写、连字符）。

`
E:\dong-skill\
├── .git\
├── DEV_NOTES.md
├── gzh-design-skill\      import 自 isjiamu/gzh-design-skill
└── wxskill\               自有 skill（webzol/WXSKill 镜像快照）
    ├── SKILL.md
    ├── README.md / README.en.md
    ├── LICENSE
    ├── references/        主题参考、组件库
    ├── scripts/           校验/抽取脚本（Python）
    ├── docs/              文档 + 画廊
    ├── archive/           旧版本主题存档
    └── assets/            资源/预览
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

## 5. 升级 gzh-design-skill 的标准流程

`powershell
cd E:\dong-skill
git fetch gzh-design-skill
# 预览变更（不实际改文件）：git archive --format=tar gzh-design-skill/main | tar -df - -C .
Remove-Item -Recurse -Force gzh-design-skill
git archive --format=tar --prefix=gzh-design-skill/ gzh-design-skill/main | tar -x -f - -C .
git add -A
git commit -m 'update: gzh-design-skill from upstream'
git push origin main
`

Remove-Item -Recurse -Force 是不可逆操作，执行前确认当前工作区已 commit。

---

## 6. 远端 / 分支

| remote | URL | 用途 |
|---|---|---|
| origin | https://github.com/webzol/dong-skill.git | 本仓库主地址，push 目标 |
| gzh-design-skill | https://github.com/isjiamu/gzh-design-skill.git | upstream，升级用，不要 push |

分支：main（唯一活跃分支，承载所有 import 内容）

---

## 7. 待办 / 待 TD 决策

- [ ] dong-skill 根目录是否加 README.md 索引所有 skill（目前访问者只能看到单个 commit message）
- [ ] 是否加 CI（gzh-design-skill 自带 .github/，但没动它）
- [ ] 是否把 webzol/dong-skill 改成 organization 名（目前是 user 仓库）
- [ ] v1.0.0 之前的 tag（assets-v1）没同步到 dong-skill，需要的话 git push origin assets-v1
