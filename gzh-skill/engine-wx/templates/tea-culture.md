# 模板：tea-culture（茶志 · 茶文化）

> **定位**：茶史、茶事、器物背后的文化脉络。宋代点茶、明清瀹饮、茶书茶画、寺院茶礼。
> **风格**：博物馆图录感。宋体标题、古铜编号、大量留白，靠文字本身撑住版面。
> **搭配**：`tea-atelier` 主题（白底 + 墨黑 `#1c1a17` + 古铜 `#8a6a3f` + 青灰 `#5f7358`）。

## 骨架

### 外框

```html
<section style="max-width:677px;margin:0 auto;background:{{bg}};padding:28px 20px 48px;box-sizing:border-box;font-family:'PingFang SC',-apple-system,'Helvetica Neue','Microsoft YaHei',sans-serif;color:{{text}};">
```

> 正文**不放 h1**（公众号标题栏已有）；**不放灰字导语**；第一段直接进事件或判断。
> 文末**不加页脚、不加来源列表**。

### 栏目签

```html
<p style="margin:0 0 18px;font-size:10px;line-height:1.6;letter-spacing:4px;color:{{accent}};text-transform:uppercase;">茶事 · TEA CULTURE</p>
```

### 首段（直接切入）

```html
<p style="margin:0 0 18px;font-size:15px;line-height:1.95;letter-spacing:.5px;color:{{text}};text-align:justify;">{{第一段：一个具体场景或一个反常识判断，不写日期，不写“今天”。}}</p>
```

### 图录式小节（编号 + 英文微标 + 宋体标题）

```html
<p style="margin:38px 0 0;font-size:10px;line-height:1.6;letter-spacing:2.6px;color:{{accent2}};text-transform:uppercase;">{{01}} · {{PROCESS}}</p>
<h2 style="margin:4px 0 16px;font-size:17px;line-height:1.6;font-weight:700;letter-spacing:.6px;color:{{text}};font-family:'Songti SC','STSong','SimSun',serif;">{{短钩子 · 不剧透答案}}</h2>
```

> 编号用 `01 / 02 / 03`，古铜或青灰小字；标题不带「一、二、三、」中文序号。
> 小节标题只写钩子，结论留给正文第一句。

### 步骤条（五步之内，横向编号）

```html
<table cellpadding="0" cellspacing="0" style="width:100%;border-collapse:collapse;margin:22px 0 10px;font-size:13px;line-height:1.75;">
  <tr>
    <td style="padding:9px 10px 9px 0;width:14%;vertical-align:top;color:{{accent}};font-family:'Songti SC','STSong',serif;border-bottom:1px solid {{divider}};">壹</td>
    <td style="padding:9px 10px 9px 0;width:22%;vertical-align:top;color:{{text}};border-bottom:1px solid {{divider}};">{{炙}}</td>
    <td style="padding:9px 0;vertical-align:top;color:{{muted}};border-bottom:1px solid {{divider}};">{{微火烘乾茶饼，去水气与青气}}</td>
  </tr>
</table>
```

> 三列：序号 / 动作 / 一句解释。最多五步，超过五步改用正文叙述。

### 引文（宋体 + 古铜竖线）

```html
<section style="margin:28px 0 30px;padding:2px 0 2px 18px;border-left:2px solid {{quoteBorder}};">
  <p style="margin:0 0 10px;font-size:16px;line-height:1.95;letter-spacing:.6px;color:{{text}};font-family:'Songti SC','STSong','SimSun',serif;">「{{引文}}」</p>
  <p style="margin:0;font-size:12px;line-height:1.6;letter-spacing:.4px;color:{{muted}};">{{— 作者《书名·篇目》}}</p>
</section>
```

> 引文只用可核对的真句，标书名与篇目；记不清出处就不引。

### 对照表（两种做法 / 两个时代）

```html
<table cellpadding="0" cellspacing="0" style="width:100%;border-collapse:collapse;margin:22px 0 12px;font-size:13px;line-height:1.75;">
  <tr>
    <th style="padding:8px 8px 8px 0;text-align:left;font-weight:600;color:{{muted}};background:{{codeBg}};border-bottom:1px solid {{cardBorder}};">{{宋}}</th>
    <th style="padding:8px 0;text-align:left;font-weight:600;color:{{muted}};background:{{codeBg}};border-bottom:1px solid {{cardBorder}};">{{明}}</th>
  </tr>
  <tr>
    <td style="padding:10px 10px 10px 0;vertical-align:top;color:{{text}};border-bottom:1px solid {{divider}};">{{团茶 · 碾末 · 点汤击拂}}</td>
    <td style="padding:10px 0;vertical-align:top;color:{{text}};border-bottom:1px solid {{divider}};">{{散茶 · 全叶 · 壶泡杯瀹}}</td>
  </tr>
</table>
```

### 图片位（真图无边框无圆角，图下不写字）

```html
<img src="{{IMG_A}}" style="max-width:100%;width:100%;display:block;margin:16px 0 22px;box-sizing:border-box;" alt="{{描述}}"/>
```

> 图要说明什么，写进它上面或下面的正文，不挂在图底下。

### 收尾

```html
<p style="margin:0;font-size:15px;line-height:1.95;letter-spacing:.5px;color:{{text}};text-align:justify;">{{最后一句：给判断，或给一个今天能做的动作，写完就结束。}}</p>
```

## 节奏

- 小节间距 **38px**，段间 **18px**；靠留白分段，不用卡片、不用底色。
- 每篇 **3–5 个小节**，视觉换气件在「引文 / 表格 / 图片」之间轮换，不连排两个表。
- 强调色全篇不超过 **6 次**；青灰只给英文微标和年代数字。
- 篇幅 **900–1500 汉字**；宁可少一个知识点，不要堆。

## 适配

- 与 `tea-atelier` 主题配套。
- 适合：宋代点茶、明清瀹饮、茶马古道、寺院茶礼、茶书茶画、节气茶事。
- 不适合：参数型工具文（改 `tea-notes`）、器物选购（改 `tea-ware`）。
