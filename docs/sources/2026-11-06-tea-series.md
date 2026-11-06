# 2026-11-06 · 茶系列（tea-atelier）

## 产出

| 文件 | 作用 |
|---|---|
| `gzh-skill/engine-wx/themes/tea-atelier.json` | 茶志主题：白底 + 墨黑 + 古铜 / 青灰，宋体标题 1.95 行高 |
| `gzh-skill/engine-wx/themes/themes.json` | 注册 `tea-atelier` |
| `gzh-skill/engine-wx/templates/tea-culture.md` | 茶文化：图录式编号 + 步骤条 + 引文 + 时代对照 |
| `gzh-skill/engine-wx/templates/tea-ware.md` | 茶器：一器一节 + 器物图 + 材质对照 |
| `gzh-skill/engine-wx/templates/tea-notes.md` | 茶知识：味道小节 + 变量表 + 参数卡 |
| `gzh-skill/engine-wx/templates/tea-scroll.md` | 茶文化·手卷：题记 + 点线分隔 + 居中引文，无表格无编号 |
| `gzh-skill/engine-wx/templates/tea-catalog.md` | 茶器·图录：大编号 + 部位条目 + 规格行 |
| `gzh-skill/engine-wx/templates/tea-almanac.md` | 茶知识·茶历：时刻条目 + 双线分隔 + 参数小字 |
| `gzh-skill/engine-wx/templates/_index.md` | 登记三套模板 |
| `E:\WX\2026-11-06\茶文化模板 · 宋人点茶，点的不是茶.html` | 示例成稿 872 字 + 2 图 |
| `E:\WX\2026-11-06\茶器模板 · 盖碗、紫砂、玻璃，怎么选.html` | 示例成稿 814 字 + 3 图 |
| `E:\WX\2026-11-06\茶知识模板 · 一杯茶里的四种味道.html` | 示例成稿 903 字 + 2 图 |
| `E:\WX\2026-11-06\茶文化模板 · 吃茶去，三个字.html` | 示例成稿（手卷）+ 1 图 |
| `E:\WX\2026-11-06\茶器模板 · 一把壶，五个地方要摸.html` | 示例成稿（图录）+ 1 图 |
| `E:\WX\2026-11-06\茶知识模板 · 一天里的四泡茶.html` | 示例成稿（茶历）+ 2 图 |

## 设计口径

- 白底、墨黑 `#1c1a17`、古铜 `#8a6a3f`、青灰 `#5f7358`、宣纸边 `#e3ddd1`、分隔线 `#ebe5da`。
- 标题宋体（`Songti SC / STSong / SimSun`），正文苹方；15px / 1.95 行高 / 两端对齐 / 0.5px 字距。
- 图录式编号：`01 · PROCESS` 小字 + 宋体钩子标题；不带「一、二、三、」中文序号。
- 不用底色卡片、圆角、阴影；只有表头允许 `#f7f3ea` 浅茶色。
- 正文不放 h1、不放灰字导语、文末不加页脚、不放来源列表。
- 图片 `display:block;width:100%;margin:14–16px 0 20–22px;`，无边框、无圆角、图下不写字。
- 三套新风格的区分：`tea-scroll` 手卷（居中题记 + `· · ·` 点线 + 居中引文，**无表格无编号**）；`tea-catalog` 图录（24px 大编号 + 部位条目 + 细线分隔 + 规格行）；`tea-almanac` 茶历（24 小时制时刻 + 双线分半日 + 参数收成一行小字）。

## 配图（6 张，均 CC0 1.0，已 base64 内嵌）

| 文件 | 内容 | 来源 |
|---|---|---|
| `tea-template/img/a_leaves.jpg` | 茶树新梢与嫩叶（3:2 横裁） | Diganta Sarkar / WordPress Photos `https://wordpress.org/photos/photo/70669bba3d/` |
| `tea-template/img/c_pour.jpg` | 白瓷壶向杯中出汤（4:5 竖裁） | Burst / StockSnap `https://stocksnap.io/photo/hands-pouring-H1SR2TNSL9` |
| `tea-template/img/d_history.jpg` | 清代茶事绘画，挑茶、筛茶 | rawpixel `https://www.rawpixel.com/image/13969605/image-plant-person-grass` |
| `tea-series/img/w_porcelain.jpg` | 白瓷侧把手急须，蒸汽 | Burst / StockSnap `https://stocksnap.io/photo/hot-teapot-RVFDXZEEFB` |
| `tea-series/img/w_yixing.jpg` | 清代宜兴紫砂壶（克利夫兰美术馆藏） | clevelandart / rawpixel `https://www.rawpixel.com/image/9711749/yixing-teapot` |
| `tea-series/img/w_glass.jpg` | 玻璃杯中的红茶 | rawpixel `https://www.rawpixel.com/image/5911919/image-public-domain-black-glass` |
| `tea-series/img/s_ceremony.jpg` | 茶席上把干茶拨入壶中（黑白） | rawpixel CC0 `https://images.rawpixel.com/editor_1024/cHJpdmF0ZS9zdGF0aWMvaW1hZ2Uvd2Vic2l0ZS8yMDIyLTA0L2xyL2ZydGVhX2NoYV82MTMzNzEtaW1hZ2Uta3liY2xuc2kuanBn.jpg` |

- 原始下载图在 `%TEMP%\opencode\tea_img\`；裁好的图在 `generated\2026-11-06\tea-template\img\` 与 `generated\2026-11-06\tea-series\img\`。
- 每篇图片位置：文化篇（茶史段后 / 收尾前）、器物篇（每种材质标题下）、知识篇（鲜味段后 / 变量表后）。

## 事实与出处

| 用于 | 内容 | 出处 |
|---|---|---|
| 点茶五步 | 炙、碾、罗、调、击 | 蔡襄《茶录·点茶》；宋徽宗《大观茶论》 |
| 斗茶标准 | 汤色鲜白、沫饽咬盏、著盏无水痕 | 蔡襄《茶录·点茶》：「视其面色鲜白，著盏无水痕为绝佳」 |
| 建盏 | 胎厚保温、釉色深衬白沫；兔毫、油滴为窑变 | 宋代建窑器物通识 |
| 明代断点 | 洪武二十四年罢造龙团，惟采芽茶以进；散茶瀹饮兴起 | 《明太祖实录》洪武二十四年九月条；茶史通用叙述 |
| 茶器引文 | 「茶滋于水，水藉乎器，汤成于火，四者相须，缺一则废。」 | 许次纾《茶疏》 |
| 紫砂 | 双气孔结构、吸香、保温；一壶一茶、不用洗涤剂 | 宜兴紫砂陶瓷学通识 |
| 白瓷 / 玻璃 | 白瓷不吸香、散热中等；玻璃不吸味、散热快 | 材质通识 |
| 四种味道 | 鲜=氨基酸（茶氨酸为主）；苦=咖啡碱；涩=茶多酚（酯型儿茶素）；甜=糖类与回甘对比 | 茶学通用 |
| 玉露遮阴 | 采摘前覆盖遮阴，提高茶氨酸、压低苦涩 | 日本宇治茶工艺通识 |
| 冲泡参数 | 85℃ / 1:50 / 60–90 秒，以 150ml 为基准 | 通用建议，因茶因器而异 |
| 吃茶去公案 | 曾到、不曾到、院主三问，皆答「吃茶去」 | 《五灯会元》卷四 · 赵州从谂 |
| 寺院茶 | 唐代寺院设茶堂、茶鼓，茶入日常仪轨 | 禅门清规通识；《敕修百丈清规》 |
| 径山茶宴 | 宋代径山寺茶宴；荣西入宋带回茶种与点茶法，著《吃茶养生记》 | 中日茶史通用叙述 |
| 壶的引文 | 「茶壶以砂者为上，盖既不夺香，又无熟汤气。」 | 文震亨《长物志》卷十二 |
| 壶的五处 | 嘴、盖、把、身、底；出水成线、断水利落、重心稳 | 器物使用通识 |
| 咖啡碱代谢 | 半衰期个体差异大，睡前六小时避免浓茶 | 通用建议，非医学结论 |

> 六篇均不写保健功效，不做「越陈越香」的绝对判断；参数只给区间。

## 修订记录

### 2026-11-06 · 对照表样式重做（不贴边 + 宋体古铜表头）

- **改了什么**：带表头色块的对照表全部重排。涉及成品：`茶器模板 · 盖碗、紫砂、玻璃，怎么选`（材质表）、`茶知识模板 · 一杯茶里的四种味道`（变量表）、`茶知识模板 · 一片叶子六种茶`（茶类 ×2 表）。
- **为什么**：旧表单元格左 padding 为 0，文字贴死表格左缘，浅茶色表头横铺到边，观感拥挤、像办公表格，不符合茶模板留白口径（用户 2026-11-06 反馈「太贴边」）。
- **改前 → 改后**：
  - 表头：`padding:8px 8px 8px 0`（末列 `8px 0`）、灰字 `{{muted}}` → `padding:10px 14px`、宋体 + 主题强调色（tea-atelier `#8a6a3f` / tea-garden `#9a6b3f`）+ 字距 2px；
  - 单元格：`padding:10px 8px 10px 0` / `9px 6px` → 四向 `12px 14px`，文字不贴边；
  - 首列行头：与正文同 weigh → 宋体加重。
- **重新生成**：`inject_images.py --allow-missing-captions` → `wrap_preview.py` 串行；质检 data:image = 3/2/4（对应该篇图数）、`{{` 残留 0；`E:\WX\2026-11-06\` 三份成品同步覆盖。
- **规则回写**：`gzh-skill/engine-wx/templates/` 下 `tea-ware.md`、`tea-notes.md`、`tea-culture.md`、`tea-essay.md` 四个模板的对照表骨架同步为新口径（无表头色块的 label-value 参数表维持原样）。

### 2026-11-06（二）· 宋人点茶篇对照表补排

- **改了什么**：`茶文化模板 · 宋人点茶，点的不是茶` 的「宋 · 点茶 / 明 · 瀹饮」对照表按新口径重排（表头宋体 + `#8a6a3f` + 字距 2px，单元格四向 `12px 14px`）。该篇表格写法与前三篇不同，第一轮重排时漏网，本轮全树扫 `<th` 确认无其他遗漏。
- **口径修正**：宋/明两列是并列对照，正文格一律同 weigh，不加重首列；「首列宋体加重」只适用于行头式对照表（材质表、变量表、茶类表）。`templates/tea-culture.md` 骨架与说明已同步改掉上一轮的误写。
- **重新生成**：串行 inject → wrap；data:image = 2、`{{` 残留 0，`E:\WX\2026-11-06\` 副本一致。

### 2026-11-06（三）· 口径铺满：无表头参数表也四向留白

- **改了什么**：所有茶模板的全部表格统一口径。带表头色块对照表（th `10px 14px` 宋体 accent / td `12px 14px`）之外，**无表头的 label-value 参数表**（tea-notes 参数卡、tea-essay 参数面板与说法对照、tea-culture 步骤条、tea-catalog 规格行）由左贴边（`padding:7–11px … 0`）改为四向 `10px 14px`；标签列维持 muted 不加重。
- **涉及成品**：`一杯茶里的四种味道`（参数卡 6 格）、`宋人点茶`（五步条 15 格）、`一把壶，五个地方要摸`（规格行 4 格）、`一片叶子六种茶`（说法对照 6 格）；tea-almanac / tea-scroll / tea-ware 篇无此类表，未动。
- **规则回写**：`templates/tea-notes.md`、`tea-essay.md`、`tea-culture.md`、`tea-catalog.md` 骨架与口径注同步。
- **质检**：四篇串行重新生成，data:image = 2/2/1/4 对应、`{{` 残留 0、六个 body 无任何旧 padding 残留；`E:\WX\2026-11-06\` 四份副本一致。

### 2026-11-06（四）· 茶文化元素升级：题签 + 书衣线 + 宋体标签列

- **改了什么**：全部茶表格加线装书语汇（用户要求「整体再高级一些、加茶文化元素」）：
  - **题签**：带表头色块的对照表上方居中一行宋体强调色小字（11px、字距 4px、「· 四字名 ·」格式）——`· 材质对照 ·`（ware）、`· 变量与滋味 ·`（notes）、`· 宋明对照 ·`（culture）、`· 六大茶类 ·` / `· 冲泡对照 ·`（template×2）；
  - **书衣线**：表顶部一条 `2px solid` 主题强调色粗线（古籍文武线外粗），其余三边仍无框无圆角；
  - **宋体标签列**：无表头参数表标签列（参数卡 / 说法对照 / 规格行）改宋体，灰调不加粗；点茶五步条「动作列」宋体加重。
- **补漏**：宋明对照表右列 3 格仍为 `padding:10px 0`（第二轮只改了左列，右列模式未进对账清单），本轮全树扫 `padding:Npx 0` 清零；五步条动作列补 `font-weight:600` 与模板口径对齐。
- **涉及成品**：盖碗紫砂玻璃 / 四种味道 / 宋人点茶 / 一把壶 / 六种茶，共 5 篇全部重新生成；质检 data:image = 3/2/2/1/4 对应、`{{` 残留 0、题签书衣线各就位、`E:\WX\2026-11-06\` 副本一致。
- **规则回写**：`templates/tea-ware.md`、`tea-notes.md`、`tea-culture.md`、`tea-essay.md`、`tea-catalog.md` 骨架与口径注同步（tea-almanac / tea-scroll 无表格，不改）。

## 泡茶用水（茶知识模板 · 同一款茶，两种汤）— 2026-11-06 新增

> 新版表格语汇（题签 / 书衣线 / 宋体标签列）定稿后的第一篇成稿，用户点名「根据新版排版一个看看」。

| 用于 | 内容 | 出处 |
|---|---|---|
| 硬水影响 | 钙镁离子与茶多酚结合，涩感变钝、香气发闷、汤色发暗 | 茶学通识（本日台账「四种味道」篇已核） |
| 纯净水偏薄 / 过滤水最稳 | 纯净水泡出的汤偏薄层次少；过滤水留少量矿物、两头不极端 | 茶学通识（同上） |
| 矿物过多压香发咸 | 钠偏高的矿泉水会压香、带咸味 | 茶学通识，定性不引数字 |
| 余氯 | 自来水余氯与管道味进汤，泡清香型茶明显；烧开开盖多滚一两分钟可让氯挥发 | 生活通识 |
| 《茶经》引文 | 「其水，用山水上，江水中，井水下」 | 陆羽《茶经·五之煮》 |
| 参数卡 | 85℃ / 1:50（3g·150ml）/ 首泡 60–90 秒 | 通用建议区间（本日台账已核），试水时固定为对照条件 |

- 配图 2 张，复用本日已入库 CC0 图：`a_leaves.jpg`（茶树嫩叶）、`c_pour.jpg`（白瓷壶出汤），来源见 `2026-11-06-tea-template.md` 配图表；图下无文字、无边框圆角。
- 新版元素就位：题签「· 水质对照 ·」、`2px #8a6a3f` 书衣线、参数卡宋体标签列 ×3、水质表首列宋体加重 ×3。
