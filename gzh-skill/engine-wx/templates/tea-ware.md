# 模板：tea-ware（茶志 · 茶器）

> **定位**：器物选择与使用。盖碗、紫砂、玻璃、白瓷、银壶、煮水器。
> **风格**：器物图录。一张图配一段判断，表格做材质对照，不做参数轰炸。
> **搭配**：`tea-atelier` 主题（白底 + 墨黑 `#1c1a17` + 古铜 `#8a6a3f` + 青灰 `#5f7358`）。

## 骨架

### 外框

```html
<section style="max-width:677px;margin:0 auto;background:{{bg}};padding:28px 20px 48px;box-sizing:border-box;font-family:'PingFang SC',-apple-system,'Helvetica Neue','Microsoft YaHei',sans-serif;color:{{text}};">
```

> 正文不放 h1、不放灰字导语、文末不加页脚。

### 栏目签

```html
<p style="margin:0 0 18px;font-size:10px;line-height:1.6;letter-spacing:4px;color:{{accent}};text-transform:uppercase;">器物 · TEA WARE</p>
```

### 首段（先给结论）

```html
<p style="margin:0 0 18px;font-size:15px;line-height:1.95;letter-spacing:.5px;color:{{text}};text-align:justify;">{{第一段：一句直接的选择建议，再补一句为什么。}}</p>
```

### 器物小节（编号 + 材质名 + 一句判词）

```html
<p style="margin:38px 0 0;font-size:10px;line-height:1.6;letter-spacing:2.6px;color:{{accent2}};text-transform:uppercase;">01 · {{PORCELAIN}}</p>
<h2 style="margin:4px 0 16px;font-size:17px;line-height:1.6;font-weight:700;letter-spacing:.6px;color:{{text}};font-family:'Songti SC','STSong','SimSun',serif;">{{白瓷不争味，所以最稳}}</h2>
```

> 每个器物一节：材质特性 → 适合什么茶 → 不适合什么茶。三段以内说完。

### 器物图（紧跟小节标题）

```html
<img src="{{IMG_A}}" style="max-width:100%;width:100%;display:block;margin:4px 0 22px;box-sizing:border-box;" alt="{{器物描述}}"/>
```

> 图放小节标题后、正文前；无边框、无圆角、图下不写字。

### 材质对照表（三列以内）

```html
<p style="margin:26px 0 0;font-size:11px;line-height:1.6;letter-spacing:4px;color:{{accent}};font-family:'Songti SC','STSong','SimSun',serif;text-align:center;">· 材质对照 ·</p>
<table cellpadding="0" cellspacing="0" style="width:100%;border-collapse:collapse;margin:10px 0 12px;font-size:13px;line-height:1.75;border-top:2px solid {{accent}};">
  <tr>
    <th style="padding:10px 14px;text-align:left;font-weight:600;font-family:'Songti SC','STSong','SimSun',serif;letter-spacing:2px;color:{{accent}};background:{{codeBg}};border-bottom:1px solid {{cardBorder}};">材质</th>
    <th style="padding:10px 14px;text-align:left;font-weight:600;font-family:'Songti SC','STSong','SimSun',serif;letter-spacing:2px;color:{{accent}};background:{{codeBg}};border-bottom:1px solid {{cardBorder}};">香气</th>
    <th style="padding:10px 14px;text-align:left;font-weight:600;font-family:'Songti SC','STSong','SimSun',serif;letter-spacing:2px;color:{{accent}};background:{{codeBg}};border-bottom:1px solid {{cardBorder}};">温度</th>
  </tr>
  <tr>
    <td style="padding:12px 14px;font-family:'Songti SC','STSong','SimSun',serif;font-weight:600;color:{{text}};border-bottom:1px solid {{divider}};">白瓷</td>
    <td style="padding:12px 14px;color:{{text}};border-bottom:1px solid {{divider}};">不吸香</td>
    <td style="padding:12px 14px;color:{{text}};border-bottom:1px solid {{divider}};">散热中等</td>
  </tr>
</table>
```

> 带表头色块的对照表：表上方加**题签**——居中一行宋体 `{{accent}}` 小字（11px、字距 4px、格式「· 四字名 ·」），表顶部一条 `2px solid {{accent}}` **书衣线**（只压顶，其余三边无框、无圆角）；表头宋体 + `{{accent}}` + 字距 2px，**所有单元格四向 padding（横向 ≥14px），文字不许贴边**；首列正文宋体加重做行头；表头允许 `{{codeBg}}` 浅茶色，正文单元格一律白底；列数不超过 3，手机端 4 列会挤。

### 选器三问（编号列表，不用卡片）

```html
<p style="margin:26px 0 8px;font-size:15px;line-height:1.95;color:{{text}};text-align:justify;"><span style="color:{{accent}};font-weight:600;">一</span>　{{你常喝什么茶？}}</p>
<p style="margin:0 0 8px;font-size:15px;line-height:1.95;color:{{text}};text-align:justify;"><span style="color:{{accent}};font-weight:600;">二</span>　{{几个人喝？}}</p>
<p style="margin:0 0 18px;font-size:15px;line-height:1.95;color:{{text}};text-align:justify;"><span style="color:{{accent}};font-weight:600;">三</span>　{{愿不愿意养？}}</p>
```

### 引文

```html
<section style="margin:28px 0 30px;padding:2px 0 2px 18px;border-left:2px solid {{quoteBorder}};">
  <p style="margin:0 0 10px;font-size:16px;line-height:1.95;letter-spacing:.6px;color:{{text}};font-family:'Songti SC','STSong','SimSun',serif;">「{{引文}}」</p>
  <p style="margin:0;font-size:12px;line-height:1.6;letter-spacing:.4px;color:{{muted}};">{{— 作者《书名·篇目》}}</p>
</section>
```

### 收尾

```html
<p style="margin:0;font-size:15px;line-height:1.95;letter-spacing:.5px;color:{{text}};text-align:justify;">{{最后一句：一句可执行的建议，写完就结束。}}</p>
```

## 节奏

- 器物小节之间 **38px**；每节「图 + 2–3 段」为基本单元。
- 全篇图 **2–3 张**，每张都跟着对应器物，不堆在文末。
- 对照表只做一次，放在所有器物小节之后，做总结。
- 篇幅 **900–1400 汉字**；不写价格、不写品牌，不做带货。

## 适配

- 与 `tea-atelier` 主题配套。
- 适合：盖碗 / 紫砂 / 玻璃 / 白瓷 / 银壶 / 煮水器 / 茶则茶针。
- 不适合：茶史文化（改 `tea-culture`）、冲泡参数（改 `tea-notes`）。
