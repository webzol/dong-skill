# 每日 AI 热点写作流程（DAILY NEWS WORKFLOW）

> 这是**跨模型、跨电脑**的固定作业流程。任何读到本目录的 AI（Claude Code / Codex / Cursor / OpenCode / Gemini CLI …）
> 都按此文件执行「每天 3 篇 AI 大模型热点文章」的活。
> 触发词：`早报` / `今天的热点` / `每日 3 篇` / `按每日流程跑` / 用户直接贴 X「Today's News」截图。

---

## 0. 一次交付的定义

**产出 3 篇**，同一套模板与主题，全部落到 `E:\WX\<YYYY-MM-DD>\`：

| 项 | 规格 |
|---|---|
| 篇幅 | 每篇 900–1600 汉字（成稿后数一遍，别估） |
| 模板 | `minimal-tech`（默认） |
| 主题 | `dongpro` |
| 配图 | 每篇 2–5 张（证据特别多可到 6，再多就拆篇），**内嵌在对应正文位置**，不堆文末 |
| 图注 | 图下 12px、`#8a8a8a`、居中，`margin:-8px 0 16px` |
| 资源 | 单文件 HTML，图片一律 `data:image/png;base64,...` |
| 外壳 | `wrap_preview.py` 包一层，右上角「复制到公众号」按钮 |
| 归档 | 同时存一份 `E:\dong-skill\generated\<date>\`（gitignored） |

### 0.1 什么时候才会真的跑

| 情况 | 会跑吗 |
|---|---|
| 用户说 `早报` / `今天的热点` / `每日 3 篇` / `按每日流程跑` | 会 |
| 用户贴 X「Today's News」截图 | 会 |
| 用户只说「排版这篇」 | 不跑整套，只走排版 |
| 没人说话 / 只是打开了仓库 | **不会**。AI 没有定时器，需要一句触发词或系统任务计划 |

在本仓库里被唤醒但用户没给任务时，**主动问一句**「跑今天的早报，还是排版某篇稿子？」，不要沉默。

### 0.2 换电脑要改的三处

这份流程默认跑在 TD 的 Windows 机上，路径写死的地方只有三个，换机器照改。
**`install.ps1` / `install.sh` 跑完会自动打印这份清单并体检**（目录在不在、浏览器找没找到），照着改即可。

| 项 | 默认值 | 改哪里 |
|---|---|---|
| 成品根目录 | `E:\WX` | 本文件 §7、`AGENTS.md` |
| 仓库路径 | `E:\dong-skill` | 本文件 §6（`wrap_preview.py` 走相对路径 `..\engine-design`，别把目录拆散）、§7 |
| 浏览器 | 自动探测 Chrome / Edge | 一般不用改，`xshot.ps1` 会依次找 Program Files 与 x86 |

其余脚本（`crop.py` / `bands.py` / `inject_images.py`）都用相对路径，跟着仓库走。

---

## 1. 选题（每天 3 条）

### 1.1 信源清单（每天就抓这些站）

| 层级 | 站点 / URL 形态 | 页面里抓哪块 | 拿什么 |
|---|---|---|---|
| 选题 | X「Today's News」（用户截图） | 整屏 | 当天 3 条头条 |
| 选题（备） | `x.com/explore/tabs/news`、`x.com/i/trending` | — | **需登录，脚本抓不到**，只作人工参考 |
| 选题复现 | websearch | — | 原始推文链接、HF 卡、官方公告 |
| 官方 ★ | `huggingface.co/<org>/<model>` | 模型卡 README：简介 → benchmark 柱状图 → 完整基准表 → 许可证段 | 参数量、上下文、许可证、benchmark 全表 |
| 官方 ★ | `help.openai.com/en/articles/<id>-<slug>` | 正文中段：套餐表 / 额度变更条款 / FAQ | 价格、倍数、生效日期、grandfathering 窗口 |
| 官方 ★ | `openai.com/index/<slug>`、`anthropic.com/news`、`blog.google/technology/ai`、`ai.meta.com/blog`、`deepmind.google/discover/blog` | 文章正文 | 发布公告原文 |
| 官方 X | `x.com/<官方账号>`、`x.com/<user>/status/<id>` | 主页置顶 / 单条推文 | 官宣措辞、负责人解释 |
| 媒体 ○ | `marktechpost.com`、`thenextweb.com`、`techcrunch.com`、`theverge.com`、`venturebeat.com` | 文章正文 | 二手解读、补充数字 |
| 第三方榜 ○ | `lmarena.ai`、`artificialanalysis.ai`、`swebench.com`、`terminalbench.com` | 榜单表格 | 独立复现分数（有则加分） |
| 社区 △ | `reddit.com/r/LocalLLaMA`、`news.ycombinator.com`、X 普通用户推文 | 高赞评论 | 争议点、质疑（必须标「社区」） |

★ 官方＝可直接写进正文；○ 媒体＝标「据 XX 报道」；△ 社区＝标「未官宣 / 传言」。

检索句式（explore 登录墙绕不过，用这个复现头条）：

```
websearch: "<头条英文标题>"
websearch: "<模型名> benchmark model card"
websearch: "site:help.openai.com <产品名> <变更>"
websearch: "<产品名> pricing change <月份> <年份>"
```

搜索结果里通常直接带 `x.com/i/trending/<id>`、原始推文、HF 模型卡、官方 help 文章。

### 1.2 选题规则

- 只取 **AI 大模型 / Agent / 编程工具 / 算力定价** 相关；
- 3 篇不重复角度：**1 篇发布/泄露类 + 1 篇开源模型类 + 1 篇价格/额度类** 是常见最优组合；
- 有官方页面（blog / help center / Hugging Face 模型卡）的优先，纯社区传言最多 1 篇，且必须写清置信度。

---

## 2. 事实收集铁律

1. **不编数字**。没查到的就不写；写"未公开"。
2. 区分三类口径并显式标注：
   - 官方公告 / help center（最高）
   - 媒体转述（中）
   - 社区泄露、截图、传言（低，必须写"未官宣"）
3. 自报 benchmark 一律注明"官方自报，无第三方复现"。
4. 每篇结尾给 1–3 个可点击来源链接（官方优先）。
5. 日期、价格、倍数、上下文长度这类硬数字，写前进原文核对一遍。

---

## 3. 配图获取（三条路，按优先级）

### 3.1 公开 X 推文 → 截图（主力）

**关键**：X 会 403 掉 `HeadlessChrome` UA；必须传普通 Chrome UA。
**另一个坑**：预览面板里的 `browser.*` 工具**连不上 x.com**（`ERR_CONNECTION_CLOSED`），别在那上面浪费时间。

> 本节命令默认在 `gzh-skill\engine-wx\` 目录下执行（脚本用相对路径 `.\scripts\`）；
> 用 `powershell -ExecutionPolicy Bypass -File` 而不是 `pwsh -File`，免得目标机只有 PowerShell 5.1。

```powershell
# 单条推文：窄窗 640 宽 → 侧栏消失，只剩单列推文
powershell -ExecutionPolicy Bypass -File .\scripts\xshot.ps1 -Url "https://x.com/<user>/status/<id>" -Name "tweet1" -W 640 -H 1500

# 主页（含置顶/首条）：同参数即可
powershell -ExecutionPolicy Bypass -File .\scripts\xshot.ps1 -Url "https://x.com/nanbeige" -Name "nb_profile" -W 640 -H 1600

# 需要更清晰的字（价目表、提示框等小字截图）：加 -Scale 2，出 2 倍像素
powershell -ExecutionPolicy Bypass -File .\scripts\xshot.ps1 -Url "https://docs.devin.ai/desktop/models" -Name "devin_2x" -W 1300 -H 2600 -Scale 2
```

截图里会带「发帖 / 登录 注册」顶栏和底部「继续前往 X」按钮 → 用 `scripts/crop.py` 裁掉：

```powershell
python .\scripts\crop.py in.png out.png 52 50 640 1180
# 参数：左 上 右 下（像素），窗口 640 宽时正文从 x≈52 开始
```

窄窗 640 下，单条推文通常落在 `y = 55 … 1180`；具体坐标照 §3.5 的表，别凭感觉。

### 3.2 官方页面 → 截图

Hugging Face 模型卡、OpenAI help center、官方 blog 都可以直接整页截，再裁关键表格：

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\xshot.ps1 -Url "https://huggingface.co/<org>/<model>" -Name "hf_model" -W 1500 -H 3400
python .\scripts\bands.py "$env:TEMP\opencode\hf_model.png" 80 770   # 先看内容块落在哪几行
python .\scripts\crop.py hf_model.png hf_table.png 86 1448 770 2524  # 再按 §3.5 的坐标裁
```

建议宽度：官方文档 1200；HF 表格 1500（否则第 4 列会被裁）。

### 3.3 原图直取（最高清）

推文页 HTML 的 `og:image` 就是原图（`pbs.twimg.com`，比截图清晰）：

```powershell
$r = Invoke-WebRequest "https://x.com/<user>/status/<id>" -UseBasicParsing `
      -Headers @{ 'User-Agent'='Mozilla/5.0 ... Chrome/124 Safari/537.36' }
[regex]::Match($r.Content,'property="og:image"\s+content="([^"]+)"').Groups[1].Value
```

拿到 URL 后 `Invoke-WebRequest -OutFile` 下载（`?format=jpg&name=orig` 取原尺寸）。

### 3.4 图片取舍

- 优先要**能证伪的图**：官方定价表、官方 benchmark 表、help center 条款、当事人推文；
- 不要同一条推文的截图 + 原图重复放；
- 一张图只服务一个论点，图注写"这张图证明什么"，不要写"图片来源"。

### 3.5 抓取位置（实测坐标，2026-10-26 验证）

截图参数 → 页面里取哪块 → 裁剪框，一一对应，照抄即可。页面改版后先跑 `scripts/bands.py` 重探边界，不要硬猜。

| 目标 | 截图参数 | 页面里取哪块 | `crop.py L T R B` |
|---|---|---|---|
| X 单条推文（长） | `-W 640 -H 1500` | 顶栏 0–55 裁掉，正文 x≈52 起，底部「继续前往 X」按钮 y>1180 裁掉 | `52 50 640 1180` |
| X 单条推文（短） | `-W 640 -H 1500` | 同上，正文 55–1060 | `52 55 640 1060` |
| X 主页首条 | `-W 640 -H 1600` | 头像/昵称 0–560，首条正文 560–1005 | `52 560 640 1005` |
| HF benchmark 柱状图 | `-W 1500 -H 3400` | 模型卡上部、简介下方，y≈935–1205，x 78–760 | `78 935 760 1205` |
| HF 完整基准表 | `-W 1500 -H 3400` | y≈1448–2524，**4 列必须 x 到 770**，否则末列被切 | `86 1448 770 2524` |
| OpenAI help 套餐表 | `-W 1200 -H 4200` | 正文中段，y≈715–950 | `28 715 790 950` |
| OpenAI help 变更条款 | `-W 1200 -H 4200` | y≈1340–1600 | `28 1340 760 1600` |
| 推文原图（最高清） | 不截图 | HTML `<meta property="og:image">` | 直接下载，`?format=jpg&name=orig` |

各站版心参考：X 窄窗 640 时左留白 ≈52–60px，右侧贴边；HF 1500 宽时左右各留 ≈78px；help center 1200 宽时左留白 ≈28px。

**探边界脚本**（页面高度/版式变了先跑它）：

```powershell
python .\scripts\bands.py "$env:TEMP\opencode\nb_hf_tall.png" 80 770
# 输出每段「有内容的行」起止，直接当 crop.py 的 T / B
```

### 3.6 落点约定（哪些是交付物）

| 阶段 | 路径 | 是否交付 |
|---|---|---|
| 原始整页截图 | `%TEMP%\opencode\<name>.png` | 否，可随时清 |
| 裁好的配图 | `%TEMP%\opencode\<name>.png` | 否，注入后即删 |
| 正文 + `{{IMG_*}}` 占位符 | `E:\dong-skill\generated\<date>\<slug>-body.html` | 否，组装后删 |
| 图片映射 | `generated\<date>\<slug>-images.json` | 否，组装后删 |
| 信源台账 | `E:\dong-skill\docs\sources\<date>.md` | **是**（入库，供下次复用） |
| 成品 | `E:\WX\<date>\<标题>.html` | **是** |
| 成品备份 | `generated\<date>\<标题>.html` | 否（gitignored） |

---

## 4. 写稿骨架（沿用 Terra / WorkBuddy 那几篇）

```html
<h1>标题（≤ 30 字，含主体 + 冲突/结论）</h1>
<p>导语（1–3 句，说清"硬事实"；灰色 13px）</p>
<hr 1px divider>

<p>背景段：为什么今天讨论这件事</p>
<h2>一、硬事实 / 核心数据</h2>
  表格或卡片：官方数字，标注来源
<h2>二、争议 / 差异</h2>
  对比表或左竖线列表
<h2>三、能用到什么程度</h2>
  适用 / 不适用 两张卡片
<h2>四、怎么读这条消息</h2>
  判断 + 置信度边界
<p>来源链接（14px 灰）</p>
<p>页脚一行：品牌 · 产品 · 状态</p>
```

写作口吻：克制的科技媒体，**先给可核验事实，再给解读**；不吹、不踩，不用"炸裂/王炸/彻底改变"。

---

## 5. 排版规范（不可省）

1. 读 `references/wechat-compat.md`（内联样式、禁 flex/grid/position/var）。
2. 读 `references/components.md` §13 配图块（**唯一允许的图片样式**）：

```html
<img src="{{IMG_X}}" style="max-width:100%;width:100%;border:1px solid #ececec;border-radius:8px;margin:16px 0;box-sizing:border-box;" alt="..."/>
<p style="margin:-8px 0 16px;font-size:12px;color:#8a8a8a;text-align:center;">图注</p>
```

3. 正文容器：`max-width:677px;margin:0 auto;background:#ffffff;padding:24px 18px 56px;`。
4. **不要多余底色**：卡片只用 `1px #ececec` 细边框，不加 `#f7f7f7` 灰填充；表格表头/行内代码的浅灰除外（有信息作用）。预览页外围（`preview-template.html` 的 `body`）一律纯白，2026-10-27 已把模板里的 `#eef0f2` 灰底永久改为 `#ffffff`，以后任何产出都不要灰底。
5. 强调色 `#615ced`，正文 `#141414`，次要 `#8a8a8a`，分隔线 `#efefef`。
6. **字号定版（2026-10-26 用户确认）**：
   - 文章大标题 `h1`：**16px**，字重 700，行高 1.35
   - 小节标题 `h2`：**17px**，字重 700（不要做成 20px 的大标题）
   - 小节标题**不带「一、二、三、」中文序号**，直接写内容标题
   - 正文 15–16px / 行高 1.9–1.95；导语 13px 灰；图注 12px 灰；来源链接 14px 灰

---

## 6. 组装（串行，别并行）

```powershell
$env:PYTHONIOENCODING='utf-8'
# 仍在 gzh-skill\engine-wx 目录下执行

# 1) 正文 HTML 写占位符 {{IMG_A}} {{IMG_B}} ...
# 2) 注入 base64 并包预览壳（必须串行，曾因并行竞态留下未替换占位符）
python .\scripts\inject_images.py body.html images.json out.html
if ($LASTEXITCODE -eq 0) {
  python ..\engine-design\scripts\wrap_preview.py out.html final.html
  if ($LASTEXITCODE -eq 0) { Remove-Item body.html, out.html -Force }
}
```

`images.json` 形如 `{"{{IMG_A}}": "C:\\path\\a.png", "{{IMG_B}}": "C:\\path\\b.png"}`。
PowerShell 5.1 用 `Set-Content -Encoding UTF8` 写出来会带 BOM，脚本已用 `utf-8-sig` 读，不用手改。

`inject_images.py` 自带两条硬校验，失败会直接退出、不产出半成品：

| 退出码 | 含义 | 处理 |
|---|---|---|
| 2 / 3 | 占位符没出现在正文 / 图片文件不存在 | 补占位符或改路径 |
| 4 | 残留 `{{` | 说明有图没配进 images.json |
| 5 | **一图一注对不上** | 每张图下方补 12px 灰色居中图注；确实不要图注才加 `--allow-missing-captions` |

质检（三查）：

```powershell
Select-String final.html -Pattern '\{\{'          # 必须 0 命中
Select-String final.html -Pattern 'data:image'   # 必须等于图片张数
Get-ChildItem <dir>                              # 只留最终成品
```

---

## 7. 归档与交付

- 成品：`E:\WX\<YYYY-MM-DD>\<标题>.html`（用户主目录，按日期分文件夹）
- 备份：`E:\dong-skill\generated\<YYYY-MM-DD>\<slug>.html`（gitignored，不入库）
- **文件名规范**：标题里**禁用全角「：」「／」和半角 `/ \ : * ? " < > |`**；
  冒号改「 · 」或「 - 」，斜杠改「／→ · 」。原因：全角冒号会让预览面板打不开文件。
  例：`OpenAI 把 Pro 200 的 Codex 额度砍半 - 10 月 30 日起 20 倍变 10 倍.html`
- 预览：`browser.preview` 打开成品；万一文件名仍带全角字符打不开，复制 ASCII 副本到 `.tmp-preview\`：
  `Copy-Item "<成品>" "E:\dong-skill\.tmp-preview\<slug>.html"`（交付的仍是原文件）
- 交付话术固定三句：① 浏览器打开成品 → ② 点右上角「复制到公众号」 → ③ 公众号编辑器新建图文后粘贴
- 结尾必须写：**本版 = 模板 `minimal-tech` + 主题 `dongpro`**

### 7.1 信源台账（每天必写一份）

写到 `E:\dong-skill\docs\sources\<date>.md`（**入库**，不跟 `generated/` 一起被清），
一条一行：**哪个结论 / 哪张图 → 来自哪个 URL 的哪一块**。
作用有三个：复核数字；页面改版后按"位置"快速找回；换机器的人能接着用同一批信源。
不写台账 = 这一步没做完。

| 用于 | 结论 / 数字 | 来源 URL | 页面位置 |
|---|---|---|---|
| 例：图 2 | Terminal-Bench 2.1 = 80.9 | `https://huggingface.co/<org>/<model>` | 模型卡上部 benchmark 表 |
| 例：正文 | Pro 200 10/30 起 10× | `https://help.openai.com/en/articles/...` | 「About ChatGPT Pro tiers」额度段 |

写台账时顺手记下**抓不到的东西**（登录墙、403、已删除），免得第二天重复踩。
首份实例：`docs/sources/2026-10-26.md`。

---

## 8. 已知坑清单

| 坑 | 现象 | 处理 |
|---|---|---|
| X 屏蔽 headless | `ERR_HTTP_RESPONSE_CODE_FAILURE` | 传 `--user-agent` 普通 Chrome UA |
| `browser.*` 连不上 X | `ERR_CONNECTION_CLOSED` / `ERR_TIMED_OUT` | 改用本机 Chrome 脚本截图 |
| explore/news 要登录 | 跳到「看看正在发生什么」登录页 | 用 websearch 复现头条，再抓具体推文 |
| 并行注入 | 成品残留 `{{IMG_*}}` | 注入 + 包装 + 删除必须一条命令串行 |
| GBK 控制台 | `UnicodeEncodeError: '✗'` | 先 `$env:PYTHONIOENCODING='utf-8'` |
| 全角文件名 | 预览面板打不开 | ASCII 副本预览，交付仍是原文件 |
| 大图体积 | 单文件 1–3MB | 正常；公众号粘贴后会转存，别压到糊 |

---

## 9. "每天早上自动开始"

Agent 无法自行定时唤醒，但可以做到"一句话启动"：

- 用户在 OpenCode / Claude Code 里发一句 **`早报`** 或 **`按每日流程跑`**；
- Agent 立刻：选题 → 抓图 → 写 3 篇 → 排版 → 落盘 `E:\WX\<今天>\` → 预览 → 报交付清单。

可选（用户机器上做一次）：Windows 任务计划程序每天 08:30 打开编辑器并预建当天目录，
脚本见 `scripts/daily_prep.ps1`（只建目录、不生成内容）。
