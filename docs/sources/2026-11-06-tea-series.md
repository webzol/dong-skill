# 2026-11-06 · 茶系列（tea-atelier）

## 产出

| 文件 | 作用 |
|---|---|
| `gzh-skill/engine-wx/themes/tea-atelier.json` | 茶志主题：白底 + 墨黑 + 古铜 / 青灰，宋体标题 1.95 行高 |
| `gzh-skill/engine-wx/themes/themes.json` | 注册 `tea-atelier` |
| `gzh-skill/engine-wx/templates/tea-culture.md` | 茶文化：图录式编号 + 步骤条 + 引文 + 时代对照 |
| `gzh-skill/engine-wx/templates/tea-ware.md` | 茶器：一器一节 + 器物图 + 材质对照 |
| `gzh-skill/engine-wx/templates/tea-notes.md` | 茶知识：味道小节 + 变量表 + 参数卡 |
| `gzh-skill/engine-wx/templates/_index.md` | 登记三套模板 |
| `E:\WX\2026-11-06\茶文化模板 · 宋人点茶，点的不是茶.html` | 示例成稿 872 字 + 2 图 |
| `E:\WX\2026-11-06\茶器模板 · 盖碗、紫砂、玻璃，怎么选.html` | 示例成稿 814 字 + 3 图 |
| `E:\WX\2026-11-06\茶知识模板 · 一杯茶里的四种味道.html` | 示例成稿 903 字 + 2 图 |

## 设计口径

- 白底、墨黑 `#1c1a17`、古铜 `#8a6a3f`、青灰 `#5f7358`、宣纸边 `#e3ddd1`、分隔线 `#ebe5da`。
- 标题宋体（`Songti SC / STSong / SimSun`），正文苹方；15px / 1.95 行高 / 两端对齐 / 0.5px 字距。
- 图录式编号：`01 · PROCESS` 小字 + 宋体钩子标题；不带「一、二、三、」中文序号。
- 不用底色卡片、圆角、阴影；只有表头允许 `#f7f3ea` 浅茶色。
- 正文不放 h1、不放灰字导语、文末不加页脚、不放来源列表。
- 图片 `display:block;width:100%;margin:14–16px 0 20–22px;`，无边框、无圆角、图下不写字。

## 配图（5 张，均 CC0 1.0，已 base64 内嵌）

| 文件 | 内容 | 来源 |
|---|---|---|
| `tea-template/img/a_leaves.jpg` | 茶树新梢与嫩叶（3:2 横裁） | Diganta Sarkar / WordPress Photos `https://wordpress.org/photos/photo/70669bba3d/` |
| `tea-template/img/c_pour.jpg` | 白瓷壶向杯中出汤（4:5 竖裁） | Burst / StockSnap `https://stocksnap.io/photo/hands-pouring-H1SR2TNSL9` |
| `tea-template/img/d_history.jpg` | 清代茶事绘画，挑茶、筛茶 | rawpixel `https://www.rawpixel.com/image/13969605/image-plant-person-grass` |
| `tea-series/img/w_porcelain.jpg` | 白瓷侧把手急须，蒸汽 | Burst / StockSnap `https://stocksnap.io/photo/hot-teapot-RVFDXZEEFB` |
| `tea-series/img/w_yixing.jpg` | 清代宜兴紫砂壶（克利夫兰美术馆藏） | clevelandart / rawpixel `https://www.rawpixel.com/image/9711749/yixing-teapot` |
| `tea-series/img/w_glass.jpg` | 玻璃杯中的红茶 | rawpixel `https://www.rawpixel.com/image/5911919/image-public-domain-black-glass` |

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

> 三篇均不写保健功效，不做「越陈越香」的绝对判断；参数只给区间。
