# DEV_NOTES — WXSkill v0.2.1

创作于 2026-09-02,v0.2.0 更新于 2026-09-08,v0.2.1 更新于 2026-09-08。给后续接手的大模型：这里记录**决策与坑**，比 README 更贴近实现意图。

## 一句话定位
把公众号文章草稿排版成「微信编辑器可直接粘贴」的科技感/简约风/文艺风 HTML，做成**可跨 AI 工具安装的 Agent Skills 包**。

## 关键决策（为什么这么做）

1. **仓库根 = skill 包本身**。`git clone` 后整个仓库就是一个 skill，复制到任意工具的技能目录即装。理由：「任何人可安装」→ 简化到克隆即装。
2. **只产内联样式 HTML，禁 flex/grid/var()/伪元素/外链样式**。这是微信编辑器清洗规则的必然结果（见 `references/wechat-compat.md`）。我们倒逼自己用「字号/字距/留白/细线/纯色」做出高级感，反而不塌版。
3. **宽度统一 677px**（微信桌面容器），`max-width:677px;margin:0 auto`。
4. **并排/网格一律用 `<table>`**，不用 flex —— 这是最容易踩的坑。
5. **模板管版式骨架，主题管颜色**，两者自由组合（v0.2.0 起为 8×5=40）。占位符 `{{accent}}` 等用法见各模板/组件。
6. **颜色唯一来源是 themes/*.json**，生成时禁止硬编码主题之外的色值。
7. **theme JSON 可选 `typography` 字段**：当一个风格的视觉签名包含强 typography 习惯（行高/字号/字距/对齐/字体族）时，写进 theme.json 的 `typography` 子字段。生成时可读取覆盖默认节奏。

## 踩过的坑 / 注意点

- **`display:flex` 在微信多数版本失效**。`minimal-tech.md` 里我故意写了个 flex 版并紧跟「改为 border-left」的修正，生成时**用修正版**。
- **预览页是 themes/*.json 的浏览器侧镜像**（JS 里内联了一份色板）。改色值要**同步**改 `preview/preview.html` 里的 `THEMES` 对象，否则预览与真实脱节。
- **图片必须公网 URL**，微信不本地存图；别用背景图承载关键内容。
- **空 `<section></section>` 会被编辑器吃掉**，别留。
- 个别机型 `box-shadow`/`border-radius`/`letter-spacing` 会弱化，**布局不能依赖它们**（去掉仍成立）。
- `install.ps1` / `install.sh` 会复制到 `~/.claude/skills/` 和 `~/.agents/skills/`；Codex 读 `.agents/skills/`，Claude Code 读 `~/.claude/skills/`。
- **抓取微信文章做参考**：`mp.weixin.qq.com` 对 WebFetch 域名拦截，但 `curl -A Mozilla/...` 在 PowerShell/Git Bash 下仍能拉到完整 HTML（3MB+）。分析时用 `re.findall(r'style\s*=\s*"([^"]*)"', content)` 抠出所有内联样式即可，不要试图跑 headless 浏览器。
- **stdout 中文乱码**：在 Windows Git Bash 里 `print('中文')` 到 stdout 会乱码，但写文件 + Read 出来正常；分析脚本统一写 `.ref/analysis.txt`。

---

## 版本

- **v0.2.1**（2026-09-08）：新增「按日期归档产出」规范
  - 每次排版必须落到 `./generated/<YYYY-MM-DD>/` 目录
  - 三件套：`source.md`（原稿）+ `<theme>-<template>-<slug>.html`（可粘贴 HTML）+ `README.md`（排版参数与注意事项）
  - 命名规则、目录结构、README 必含字段全部写进 SKILL.md 第 4.5 步
  - `generated/` 加入 `.gitignore`（保留 `.gitkeep` 占位说明），但实际归档当日内容不入库
  - 同步更新 README.md 的目录树与特性清单
  - **设计动机**：TD 长期反馈——多次排版内容混在聊天记录里回头找不到；按日期归档能直接 `cd generated/2026-09-08/` 翻今天的所有产出
  - **跨平台路径**：用相对路径 `./generated/`，不绑绝对路径；Claude Code / Codex / Cursor 等所有 Agent Skills 标准的工具都能找到

- **v0.2.0**（2026-09-08）：新增 3 个真实文章复刻的主题
  - `taobao-flash`（淘宝闪购）：白底 + 蓝橙双强调 + 紧凑电商风（参考 #408BFB + #ff6827 双色 + 深黑字 + 紧凑段距）
  - `wechat-pai`（微信派）：白底 + 微信绿 #07c160 + 杂志文艺（参考 PingFang SC + 1px 字距 + 1.6 行高 + justify）
  - `qianwen`（千问）：白底 + #141414 近黑 + 苹果字体栈 + 1.95 行高 + 14px 圆角卡片（参考 AI 产品长文）
  - 新增模板 `wechat-pai-essay`：承载 PingFang/字距/对齐/字体族等微信派专属 typography
  - 主题 JSON 新增可选 `typography` / `paletteNotes` / `usageTip` 字段（向后兼容）
  - 同步更新 `SKILL.md` / `README.md` / `themes.json` / `templates/_index.md` / `preview/preview.html`
  - 新增 3 个示例 HTML 到 `examples/`（taobao-flash-ecommerce / wechat-pai-essay / qianwen-product）
  - `.gitignore` 加 `.ref/` 排除抓取公众号的临时目录

- **v0.1.0**（2026-09-02）：完整骨架（SKILL.md + 5 主题 + 4 模板 + 参考 + 预览 + 全工具安装）。已推 webzol/WXSKill `main`。

---

## v0.2.0 新增风格决策记录

### 为什么不都用 theme + 现有 4 模板?
v0.1.0 现有 4 个模板（minimal-tech / cyber-card / terminal-code / hud）都基于**通用科技感**轴。
- 淘宝闪购：typography 偏普通 + 强调色特殊 → **只做 theme** 即可，最小工作
- 千问：typography 强烈（1.95 行高 + 14px 圆角 + 苹果字体栈）但模板结构与 minimal-tech / cyber-card 重叠 → **只做 theme**，让现有模板消化
- 微信派：typography **极强且独特**（PingFang + 1px 字距 + 两端对齐 + 1.6 行高 + 0px 段间距）→ **必须新加 template** 否则丢一半风格

### theme JSON 的 `typography` 字段语义
仅作**生成提示**，模板读取时**应当用模板内置节奏**作为基础，仅在 theme 显式指定时覆盖。
避免每个 theme 都强制锁死 layout——灵活性是 5×4=20 组合的卖点。

### examples/ 的命名
`<theme-slug>-<template-or-use-case>.html`。当前 3 个文件命名：
- `taobao-flash-ecommerce.html`（电商活动通知场景）
- `wechat-pai-essay.html`（品牌故事场景）
- `qianwen-product.html`（AI 产品介绍场景）

---

## 待办 / 可扩展

- 真实文章实测一篇，确认粘贴进公众号编辑器不塌版。
- 可考虑加「导入公众号 markdown → 自动选模板/主题」的一次性命令示例。
- 预览页可加「复制整段 HTML」按钮（当前只做展示对比）。
- `wechat-pai-essay` 模板未来若扩展，可加「封面图」「作者卡片」专用块。
- `qianwen` 若用户呼声高，可拆出独立 template（保留 14px 圆角 + 1.95 行高）以适配更多场景。
- `.ref/` 临时目录建议每次抓完分析就 `rm -rf`，避免被误 commit（已加 .gitignore）。
- 归档目录 `generated/<YYYY-MM-DD>/` 可考虑加一个 `.schema.json` 自动校验三件套是否齐全（CI 友好）。
- 归档 README.md 的「风格切换指南」可做成自动生成（读 themes.json 的色值表）而不是手写。
