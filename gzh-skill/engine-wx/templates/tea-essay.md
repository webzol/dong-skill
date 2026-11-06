# 模板：tea-essay（茶席 · 茶知识长文）

> **定位**：茶知识 / 茶文化 / 茶器 / 产区风物类长文。用宋体标题 + 苹方正文、茶汤琥珀与茶青双强调，靠留白和细线撑住版面。
> **风格**：安静、克制、有纸感；不堆卡片、不加底色、不用彩色虚线。
> **搭配**：`tea-garden` 主题（白底 + 墨褐字 + `#9a6b3f` 茶汤琥珀 + `#5f7a52` 茶青）。

## 骨架（占位符替换为主题色）

### 外框

```html
<section style="max-width:677px;margin:0 auto;background:{{bg}};padding:26px 20px 44px;box-sizing:border-box;font-family:'PingFang SC',-apple-system,'Helvetica Neue','Microsoft YaHei',sans-serif;color:{{text}};">
```

> 正文**不放 h1 大标题**（公众号标题栏已有）。标题写进公众号标题栏，正文第一段直接点题。
> 全文**不放灰字导语块**，第一段就是正文，字号与后文一致。

### 栏目签（可选，一行小字）

```html
<p style="margin:0 0 14px;font-size:11px;line-height:1.6;letter-spacing:3px;color:{{accent}};text-transform:uppercase;">茶事 · TEA NOTES</p>
```

### 首段（直接点题，不用灰字）

```html
<p style="margin:0 0 18px;font-size:15px;line-height:1.9;letter-spacing:.4px;color:{{text}};text-align:justify;">{{第一段：一句判断或一个反差，直接进主题，不写日期、不写“今天”。}}</p>
```

### 细双线（开篇分隔）

```html
<section style="height:1px;background:{{divider}};margin:0 0 4px;"></section>
<section style="height:1px;background:{{divider}};margin:0 0 24px;"></section>
```

### 小节标题（宋体 + 英文微标）

```html
<p style="margin:34px 0 6px;font-size:10px;line-height:1.6;letter-spacing:2.4px;color:{{accent2}};text-transform:uppercase;">{{PROCESS}}</p>
<h2 style="margin:0 0 14px;font-size:17px;line-height:1.6;font-weight:700;letter-spacing:.5px;color:{{text}};font-family:'Songti SC','STSong','SimSun',serif;">{{短钩子 · 不剧透结论}}</h2>
```

> 小节标题只写钩子，不把答案写进标题；答案留在正文第一句。**不带「一、二、三、」中文序号**。

### 正文段落

```html
<p style="margin:0 0 18px;font-size:15px;line-height:1.9;letter-spacing:.4px;color:{{text}};text-align:justify;">{{段落正文。关键概念用 <strong style="color:{{accent}};font-weight:600;">强调</strong>，数字或产地用 <span style="color:{{accent2}};">次强调</span>。}}</p>
```

### 茶类对照表（表头浅茶色，仅表头允许底色）

```html
<table cellpadding="0" cellspacing="0" style="width:100%;border-collapse:collapse;margin:20px 0 22px;font-size:13px;line-height:1.7;letter-spacing:.2px;">
  <tr>
    <th style="padding:10px 14px;text-align:left;font-weight:600;font-family:'Songti SC','STSong','SimSun',serif;letter-spacing:2px;color:{{accent}};background:{{codeBg}};border-bottom:1px solid {{cardBorder}};">茶类</th>
    <th style="padding:10px 14px;text-align:left;font-weight:600;font-family:'Songti SC','STSong','SimSun',serif;letter-spacing:2px;color:{{accent}};background:{{codeBg}};border-bottom:1px solid {{cardBorder}};">关键一步</th>
    <th style="padding:10px 14px;text-align:left;font-weight:600;font-family:'Songti SC','STSong','SimSun',serif;letter-spacing:2px;color:{{accent}};background:{{codeBg}};border-bottom:1px solid {{cardBorder}};">氧化程度</th>
  </tr>
  <tr>
    <td style="padding:12px 14px;font-family:'Songti SC','STSong','SimSun',serif;font-weight:600;color:{{text}};border-bottom:1px solid {{divider}};">{{绿茶}}</td>
    <td style="padding:12px 14px;color:{{text}};border-bottom:1px solid {{divider}};">{{杀青}}</td>
    <td style="padding:12px 14px;color:{{muted}};border-bottom:1px solid {{divider}};">{{尽量不氧化}}</td>
  </tr>
</table>
```

> 对照表单元格四向 padding（横向 ≥14px），文字不贴边；表头宋体 + `{{accent}}` + 字距 2px，首列宋体加重。列数控制在 3–4 列；手机端 5 列会挤。代表茶名放在第二行小字，不另开一列。

### 冲泡参数面板（三列，无填充）

```html
<table cellpadding="0" cellspacing="0" style="width:100%;border-collapse:collapse;margin:20px 0 8px;font-size:13px;line-height:1.7;">
  <tr>
    <td style="padding:7px 0;color:{{muted}};border-bottom:1px solid {{divider}};width:30%;">{{水温}}</td>
    <td style="padding:7px 0;color:{{text}};border-bottom:1px solid {{divider}};">{{80–85℃}}</td>
  </tr>
  <tr>
    <td style="padding:7px 0;color:{{muted}};border-bottom:1px solid {{divider}};">{{投茶比}}</td>
    <td style="padding:7px 0;color:{{text}};border-bottom:1px solid {{divider}};">{{1:50}}</td>
  </tr>
  <tr>
    <td style="padding:7px 0;color:{{muted}};">{{出汤}}</td>
    <td style="padding:7px 0;color:{{text}};">{{1–2 分钟}}</td>
  </tr>
</table>
<p style="margin:0 0 22px;font-size:12px;line-height:1.7;letter-spacing:.3px;color:{{muted}};">{{注：比例以 150ml 水为基准，器具容量不同按同比例换算。}}</p>
```

### 引文（宋体 + 茶色竖线）

```html
<section style="margin:26px 0 28px;padding:2px 0 2px 16px;border-left:2px solid {{quoteBorder}};">
  <p style="margin:0 0 8px;font-size:16px;line-height:1.9;letter-spacing:.5px;color:{{text}};font-family:'Songti SC','STSong','SimSun',serif;">「{{引文}}」</p>
  <p style="margin:0;font-size:12px;line-height:1.6;letter-spacing:.3px;color:{{muted}};">{{— 出处}}</p>
</section>
```

> 引文只用真句子，标明书名与篇目；不确定出处的宁可不引。

### 说法对照（左竖线两列）

```html
<table cellpadding="0" cellspacing="0" style="width:100%;border-collapse:collapse;margin:18px 0 22px;font-size:14px;line-height:1.8;">
  <tr>
    <td style="padding:10px 10px 10px 0;width:34%;vertical-align:top;color:{{muted}};border-bottom:1px solid {{divider}};">{{常见说法}}</td>
    <td style="padding:10px 0;vertical-align:top;color:{{text}};border-bottom:1px solid {{divider}};">{{实际怎么回事}}</td>
  </tr>
</table>
```

### 图片位（用户没给图时占位；给了图按 §13，不加边框圆角）

```html
<section style="margin:16px 0 20px;padding:30px 16px;background:{{bg}};border:1px dashed #d8d8d8;text-align:center;">
  <p style="margin:0 0 6px;font-size:14px;font-weight:700;color:{{text}};letter-spacing:.5px;">图片占位</p>
  <p style="margin:0;font-size:12px;color:{{muted}};letter-spacing:.3px;">{{建议画面 · 如干茶特写 / 茶汤对比}}</p>
</section>
```

> 真图样式：`display:block;width:100%;margin:14px 0 20px;`，**不加 border、不加圆角、图下不写文字**。

### 收尾（不加页脚、不加来源列表）

```html
<p style="margin:0;font-size:15px;line-height:1.9;letter-spacing:.4px;color:{{text}};text-align:justify;">{{最后一句：给判断或给一个可执行的动作，写完就结束。}}</p>
```

## 节奏要求

- 段间 **18px**，小节前 **34px**；靠留白分段，不靠卡片和底色。
- 每 **2–3 段** 出现一次视觉换气：细线、引文、表格，三者轮换，不要连着排两个表。
- 全篇强调色出现不超过 **6 次**；茶青只给数字、产地、对照项。
- 表头底色只允许 `{{codeBg}}`（`#f7f3ea`），正文单元格一律白底。
- 不用圆角、不用阴影、不用彩色虚线；图片无边框。
- 篇幅 900–1600 汉字；标题写进公众号标题栏，正文不重复 h1。

## 适配

- 与 `tea-garden` 主题配套；换主题只需替换占位符色值，骨架不动。
- 适合：六大茶类科普、产区风物、冲泡参数、茶器选择、茶史人物、节气饮茶。
- 不适合：需要强促销的电商页（改用 `taobao-flash`）、数据榜单（改用 `hud`）。
