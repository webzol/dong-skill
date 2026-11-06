# 2026-11-06 · 茶知识模板（tea-essay × tea-garden）

## 产出

| 文件 | 作用 |
|---|---|
| `gzh-skill/engine-wx/templates/tea-essay.md` | 茶知识 / 茶文化长文版式骨架 |
| `gzh-skill/engine-wx/themes/tea-garden.json` | 茶席主题色板与字体节奏 |
| `gzh-skill/engine-wx/themes/themes.json` | 注册 `tea-garden` |
| `gzh-skill/engine-wx/templates/_index.md` | 登记 `tea-essay` |
| `E:\WX\2026-11-06\茶知识模板 · 一片叶子六种茶.html` | 示例成稿（单文件、可复制到公众号） |

## 设计口径

- 白底、墨褐字 `#26231e`、茶汤琥珀 `#9a6b3f`、茶青 `#5f7a52`、宣纸边 `#e7e0d4`。
- 标题用宋体（`Songti SC / STSong / SimSun`），正文用苹方；15px / 1.9 行高 / 两端对齐 / 0.4px 字距。
- 不加底色卡片、不用圆角阴影；表头允许 `#f7f3ea` 浅茶色，正文单元格白底。
- 正文不放 h1（公众号标题栏已有），不放灰字导语块，文末不加页脚与来源列表。
- 图片位按 §13 / §13b：真图无边框无圆角、图下不写字；没图时用中性灰虚线占位。

## 事实与出处

| 用于 | 内容 | 出处 |
|---|---|---|
| 六大茶类 | 按加工工艺与茶多酚氧化程度分为绿、白、黄、青、红、黑；黑茶为后发酵 | 茶学通用分类（陈椽六大茶类分类体系），本稿只写共识 |
| 工艺 | 杀青钝化酶、发酵主动氧化、渥堆微生物与湿热后发酵 | 同上 |
| 引文 | 「其水，用山水上，江水中，井水下。」 | 陆羽《茶经·五之煮》 |
| 茶史 | 唐代煎茶加盐；宋代点茶、斗茶比沫饽与咬盏；明代废团茶兴散茶 | 中国茶史通用叙述；明代罢造龙团见洪武二十四年诏 |
| 冲泡 | 水温、投茶比、出汤时间为通用建议，按 150ml 水折算 | 行业通用冲泡参数，因茶、因器而异 |
| 存茶 | 避光、密封、干燥、无异味；绿茶与清香乌龙冷藏，其余常温 | 通用存茶建议 |

> 本稿不写保健功效，不做「越陈越香」的绝对判断；白茶、黑茶只写「越存越不同」。

## 配图（4 张，均为 CC0 1.0，已 base64 内嵌）

| 位置 | 文件 | 内容 | 来源 |
|---|---|---|---|
| 开篇后 | `a_leaves.jpg` | 茶树新梢与嫩叶，3:2 横裁 | Diganta Sarkar / WordPress Photos，`https://wordpress.org/photos/photo/70669bba3d/` |
| 六大茶类表后 | `b_dry.jpg` | 干燥后的条索状茶叶 | rawpixel，`https://www.rawpixel.com/image/3296169/free-photo-image-animal-beverage-cc0` |
| 水温表后 | `c_pour.jpg` | 白瓷壶向杯中出汤，4:5 竖裁 | Burst / StockSnap，`https://stocksnap.io/photo/hands-pouring-H1SR2TNSL9` |
| 茶史段后 | `d_history.jpg` | 清代茶事绘画，挑茶、筛茶 | rawpixel，`https://www.rawpixel.com/image/13969605/image-plant-person-grass` |

- 图片样式：`display:block;width:100%;margin:14px 0 20px;`，无边框、无圆角、图下无文字。
- 原始下载图在 `%TEMP%\opencode\tea_img\`，裁好的图在 `generated\2026-11-06\tea-template\img\`。

