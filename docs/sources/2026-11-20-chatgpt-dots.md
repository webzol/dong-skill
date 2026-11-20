# 2026-11-20 第二篇 · ChatGPT 手机版重做（dot 占底栏正中）

稿名：`ChatGPT 手机版重做 · dot 占住底栏正中，Plus 开始小范围解锁`
模板 / 主题：`minimal-tech` × `dongpro`（Mio 官宣稿腔：关键词浅底 `#EEF0F7` + 深蓝 `#1F2F8F`，判断句加粗，无橙色、无灰底章节条）

选题来源：用户给的 X 趋势页 `https://x.com/i/trending/2123571242196410744`（趋势摘要：OpenAI 扩展 Dots 助手功能并推出重新设计的移动聊天 GPT 应用，最后更新 2026-11-20）。

## 一、事实来源

| 稿中说法 | 来源 | 说明 |
|---|---|---|
| dot 开始让一小部分 ChatGPT Plus 用户测试；同时向所有 ChatGPT Business Standard 用户开放，当天开始推送 | `https://x.com/thsottiaux/status/2123556256392847657`（Tibo，7:17 · 11/20） | 官方原贴，纯文字 → 双语卡片 |
| 新移动端体验：dot 有独立标签页，Codex、Projects、Images 等可钉到底栏，部分人默认开启，可在 Settings > New ChatGPT Design 随时开关 | `https://x.com/thsottiaux/status/2123557171321561133`（Tibo，7:20 · 11/20） | 官方原贴 + 20 秒演示视频（`amplify_video_thumb/2123557071723565056`） |
| 界面细节：底栏三个入口（首页 / dot / 宫格）；首页「Good morning 👋 What are we tackling today?」+ DHL 待办卡；dot 页「Message dot」+ 早期预览提示；宫格「Tap and hold an item to pin it to the tab bar」，九项为 Space / Projects / Images / Scheduled / Codex / Plugins / Finance / Health / Sites | 同条演示视频逐帧（1s / 13s / 16s 三帧） | 逐帧截图，裁掉播放器控件条 |
| 范围：已有 dot 或有资格创建 dot 的 Pro 用户，部分默认开启；不含欧洲经济区（含欧盟）、英国、瑞士、韩国；手机网页版不支持，需 iOS/Android App | `https://www.digitaltrends.com/computing/chatgpt-new-mobile-design/`；`https://www.theverge.com/ai-artificial-intelligence/1038334/...`；`https://www.payforchat.com/articles/gpt-chatgpt-new-mobile-design-dots-eligibility-2026` | 媒体 / 支持页口径，正文标「官方给的范围」「边界写得比通常更细」 |
| Business Standard：美国符合条件的成员可在工作区建 1 个个人 dot，有用量限制；Enterprise / Edu / Healthcare 从 11/18 起默认开启、管理员可关 | `https://www.payforchat.com/articles/gpt-chatgpt-new-mobile-design-dots-eligibility-2026`（转述支持页） | 正文明确写「这两条出自支持页，不是推文」 |
| 「我们正在努力把 dots 带给全球 Plus 用户，有反馈可以继续冲我喊」 | `https://x.com/_samirism/status/2123562008977330564`（samir，7:40 · 11/20） | 内部口径，无时间表 → 双语卡片 |
| 「Le ChatGPT 2.0」（两小时后转自己那条 demo）+ 17 万浏览 / 1600 多赞 | `https://x.com/thsottiaux/status/2123612433923051976`（11:00 · 11/20） | 正文一句话，未作图；稿中写明「官方文档里没有 2.0 这个说法」 |
| dots 是 9 月 29 日 DevDay 发布，常驻智能体，自有云电脑与浏览器，接 4000 多应用，GPT-6 Astra 驱动；11 月 3 日加入 GPT-6.1 Terra 可选 | `https://openai.com/zh-Hans-CN/index/introducing-dots/`；`https://help.openai.com/zh-hans-cn/articles/20001530-getting-started-with-your-dot` | 官方产品页 + 帮助中心 |
| 计费：首个 dot 含在 Pro / Business Premium 内不额外收费；与 dot 对话不计入 ChatGPT 用量，让它去 Codex / ChatGPT 工作起任务照常算额度；以后加 dot、提速按月付费 | 同上（官方产品页「开始使用 dot」段） | 官方口径 |
| 英国区 Pro 每月 89 英镑起、三档用量、清单含「Dot, your always-on agent」 | Tibo 扩围推文配图 `HXhlQC2XEAA_0FH`（`?format=png&name=orig`） | 官方定价卡原图 |

## 二、图片

| 占位 | 文件 | 来源 |
|---|---|---|
| `{{IMG_HOME}}` | `home.jpg`（1000×1107） | 官方演示视频 1s 帧，裁掉播放器控件 |
| `{{IMG_GRID}}` | `grid.jpg`（1000×1107） | 同视频 16s 帧（宫格 + 钉选提示） |
| `{{IMG_DOT}}` | `dot.jpg`（1000×1107） | 同视频 13s 帧（dot 标签页对话 + 早期预览提示） |
| `{{IMG_TIBO}}` | `tibo_plus.jpg`（900×866） | 纯文字推 → 双语卡片（unavatar 头像，上英下中，重点同步加粗，无水印，底部 60px） |
| `{{IMG_SAMIR}}` | `samir_plus.jpg`（900×530） | 同上 |
| `{{IMG_PRICE}}` | `plus_orig.png`（772×1852） | Tibo 推文配图原图（Pro 定价卡） |

显示宽度 641px；最高为定价卡 ≈ 1535px，未到 2000px、高宽比 2.4，均未触发 §13c 滑动框。视频帧一律裁掉底部的播放/进度/静音/全屏控件条。

## 三、口径分层

- **官方**：dot 扩围范围（Plus 小范围、Business Standard 全量）、新界面开关与首批对象、dots 的产品定位与计费、英国区定价卡。
- **媒体 / 支持页**：区域排除名单（EEA 含欧盟、英国、瑞士、韩国）、Business Standard 的「美国符合条件成员 + 1 个 dot + 用量限制」、Enterprise/Edu/Healthcare 11/18 默认开启。
- **内部**：samir 的「全球 Plus 在推进」，无时间表；Tibo 自己喊的「Le ChatGPT 2.0」不是官方版本号。
- **未采用**：趋势页里另外两条（「只有 2% 美国家庭付费订阅 AI 服务」「DevDay 2026 发布 Dots」），前者与本稿主题无关，后者只作背景一句带过。

## 四、修订记录

- 2026-11-20 初稿：界面改版 + dots 扩围同日双线，6 图（3 官方视频帧 + 2 双语卡片 + 1 官方定价卡）；`validate → inject --allow-missing-captions → wrap` 全过（23 处 leaf，img 6 / data:image 6 / `{{` 0 / 无 h1）。
- 2026-11-20 二修：小标题「这个 dot 到底是什么，官方写得很清楚」改为结论句「dot 是自己带云电脑的常驻智能体」；「只写了四个词」改为「只写了一行」；「Tibo 那条推文」明确为「扩围那条推文」；首页问候补回原图 emoji 👋；删掉对评论区的未核实推断，改为「官方文档里没有 2.0 这个说法」。
