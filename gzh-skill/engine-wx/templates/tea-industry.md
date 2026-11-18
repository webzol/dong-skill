# 模板：tea-industry（茶志 · 行业观察）

> **定位**：茶行业信息稿——新茶上市与产区行情、价格与市场、政策与标准、展会动态、财报与渠道。
> **风格**：数据简报 + 克制解读。数字先出、口径后标（官方 / 媒体 / 行情），每条事件带时间与出处。
> **搭配**：`tea-atelier` 主题。
> **写作前读**：`../references/tea-knowledge.md`；行情与价格是时点数据，**保持原值、带采集时间**，不换算不折现；政策与标准以发布文本为准。

## 骨架

### 外框

```html
<section style="max-width:677px;margin:0 auto;background:{{bg}};padding:30px 22px 50px;box-sizing:border-box;font-family:'PingFang SC',-apple-system,'Helvetica Neue','Microsoft YaHei',sans-serif;color:{{text}};">
```

> 正文不放 h1、不放灰字导语、文末不加页脚、不放来源列表。

### 栏目签

```html
<p style="margin:0 0 20px;font-size:10px;line-height:1.6;letter-spacing:4px;color:{{accent}};text-transform:uppercase;">行业观察 · TEA INDUSTRY</p>
```

### 首段（一句总纲）

```html
<p style="margin:0 0 22px;font-size:15px;line-height:1.95;letter-spacing:.5px;color:{{text}};text-align:justify;">{{第一段：本期行业信息的一句话判断，直接给结论。}}
```

### 关键数字条（三格，本期最硬的三个数）

```html
<table cellpadding="0" cellspacing="0" style="width:100%;border-collapse:collapse;margin:14px 0 20px;font-size:13px;line-height:1.7;">
  <tr>
    <td style="width:33.3%;padding:14px 8px;text-align:center;border-top:2px solid {{accent}};border-bottom:1px solid {{divider}};border-right:1px solid {{divider}};">
      <p style="margin:0 0 4px;font-size:22px;line-height:1.2;font-weight:700;color:{{accent}};font-family:'Songti SC','STSong','SimSun',serif;">{{12.5%}}</p>
      <p style="margin:0;font-size:12px;line-height:1.6;color:{{muted}};">{{同比 · 口径与时间}}</p>
    </td>
    <td style="width:33.3%;padding:14px 8px;text-align:center;border-top:2px solid {{accent}};border-bottom:1px solid {{divider}};border-right:1px solid {{divider}};">
      <p style="margin:0 0 4px;font-size:22px;line-height:1.2;font-weight:700;color:{{accent}};font-family:'Songti SC','STSong','SimSun',serif;">{{数值}}</p>
      <p style="margin:0;font-size:12px;line-height:1.6;color:{{muted}};">{{指标 · 口径与时间}}</p>
    </td>
    <td style="width:33.3%;padding:14px 8px;text-align:center;border-top:2px solid {{accent}};border-bottom:1px solid {{divider}};">
      <p style="margin:0 0 4px;font-size:22px;line-height:1.2;font-weight:700;color:{{accent}};font-family:'Songti SC','STSong','SimSun',serif;">{{数值}}</p>
      <p style="margin:0;font-size:12px;line-height:1.6;color:{{muted}};">{{指标 · 口径与时间}}</p>
    </td>
  </tr>
</table>
```

> 数字必须带口径与时间（谁统计的、截至何时）；没有出处的数字不进条。

### 事件条目（时间 + 标题 + 解读 + 口径行）

```html
<section style="margin:32px 0 0;padding-top:12px;border-top:1px solid {{cardBorder}};">
  <p style="margin:0 0 4px;font-size:11px;line-height:1.6;letter-spacing:3px;color:{{accent2}};">{{11.18}}</p>
  <h2 style="margin:0 0 12px;font-size:17px;line-height:1.6;font-weight:700;letter-spacing:.6px;color:{{text}};font-family:'Songti SC','STSong','SimSun',serif;">{{事件一句话标题}}</h2>
  <p style="margin:0 0 14px;font-size:15px;line-height:1.95;letter-spacing:.5px;color:{{text}};text-align:justify;">{{事实段：谁、做了什么、多少数字。}}</p>
  <p style="margin:0 0 18px;font-size:15px;line-height:1.95;letter-spacing:.5px;color:{{text}};text-align:justify;">{{解读段：影响在哪、边界在哪，两句。}}</p>
  <p style="margin:0 0 18px;font-size:13px;line-height:1.7;letter-spacing:.3px;color:{{muted}};">口径：{{官方 / 媒体 / 行情}} · {{来源与采集时间}}</p>
</section>
```

> 日期用「月.日」两位数；标题写结论短句，不用问句。
> **口径行每条必带**：官方口径给发布文本，媒体口径给媒体名，行情口径给市场/采集时间。

### 行情小表（价格/指数类，可选，全篇最多一个）

```html
<table cellpadding="0" cellspacing="0" style="width:100%;border-collapse:collapse;margin:10px 0 12px;font-size:13px;line-height:1.75;border-top:2px solid {{accent}};">
  <tr>
    <td style="padding:12px 14px;font-family:'Songti SC','STSong','SimSun',serif;font-weight:600;color:{{text}};border-bottom:1px solid {{divider}};">{{品类/产区}}</td>
    <td style="padding:12px 14px;font-family:'Songti SC','STSong','SimSun',serif;font-weight:600;color:{{text}};border-bottom:1px solid {{divider}};">{{价格/指数}}</td>
    <td style="padding:12px 14px;font-family:'Songti SC','STSong','SimSun',serif;font-weight:600;color:{{text}};border-bottom:1px solid {{divider}};">{{环比/同比}}</td>
  </tr>
  <tr>
    <td style="padding:12px 14px;color:{{text}};border-bottom:1px solid {{divider}};">{{行 1}}</td>
    <td style="padding:12px 14px;color:{{text}};border-bottom:1px solid {{divider}};">{{数值 + 单位}}</td>
    <td style="padding:12px 14px;color:{{muted}};border-bottom:1px solid {{divider}};">{{方向 + 时间}}</td>
  </tr>
</table>
<p style="margin:0 0 22px;font-size:12px;line-height:1.7;letter-spacing:.4px;color:{{muted}};">{{数据口径：采集市场、采集时间、是否含税。}}</p>
```

> 价格保持原值原单位，不折算；表后必带口径小字。

### 图片（政策原文/展会现场/产区实拍，最多两张）

```html
<img src="{{IMG_A}}" style="max-width:100%;width:100%;display:block;margin:14px 0 20px;box-sizing:border-box;" alt="{{描述}}"/>
```

> 图下不写字；截图必须高清（DPR ≥ 2、无时间行/互动栏）；长图套 `components.md` §13c 滑动框并自测。

### 收尾

```html
<p style="margin:0;font-size:15px;line-height:1.95;letter-spacing:.5px;color:{{text}};text-align:justify;">{{最后一句：本期信息合起来看，下一步盯什么。}}</p>
```

## 节奏

- 关键数字条 **1 个**；事件条目 **3–4 个**；行情表可省，省时数字进数字条。
- 条目之间 **32px**；解读段与事实段分开写，不揉成一段。
- 全篇图 **1–2 张**；口径行不可省。
- 篇幅 **900–1400 汉字**；不做投资建议、不写「必涨/必跌」、不写保健功效。

## 适配

- 与 `tea-atelier` 主题配套。
- 适合：新茶上市与产区行情、价格与市场动态、政策与标准解读、展会与财报。
- 不适合：冲泡参数与风味教学（改 `tea-notes`）、节气/节日茶单（改 `tea-almanac` / `tea-festival`）、茶史随笔（改 `tea-scroll`）。
