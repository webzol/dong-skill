# 模板：ai-model（AI 实验室 · 大模型速写）

> **定位**：科技 / AI / 大模型类长文。模型速写、发布解读、选型指南、价格与基准对照。
> **风格**：产品说明书式克制排版。无衬线标题、靛蓝强调、关键数字条，官方截图与表格各就各位。
> **搭配**：`ai-lab` 主题（白底 + 墨黑 + 靛蓝 `#2a55c7` + 松石 `#0f8a7e`）。
> **图片是主角**：模型发布、定价页、榜单、模型卡截图都要落在对应论点后面。

## 骨架

### 外框

```html
<section style="max-width:677px;margin:0 auto;background:{{bg}};padding:26px 20px 46px;box-sizing:border-box;font-family:'PingFang SC',-apple-system,'Helvetica Neue','Microsoft YaHei',sans-serif;color:{{text}};">
```

> 正文**不放 h1**（公众号标题栏已有），**不放灰字导语**，文末**不加页脚、不加来源列表**。

### 栏目签

```html
<p style="margin:0 0 16px;font-size:10px;line-height:1.6;letter-spacing:4px;color:{{accent}};text-transform:uppercase;">AI · MODEL NOTES</p>
```

### 元信息条（一行，型号 · 厂商 · 状态）

```html
<p style="margin:0 0 20px;font-size:13px;line-height:1.7;letter-spacing:.3px;color:{{muted}};">
  <span style="color:{{text}};font-weight:600;">{{型号}}</span> · {{厂商}} · {{状态 · 如 灰度中 / 已发布}} · {{一句话定位}}
</p>
<section style="height:1px;background:{{divider}};margin:0 0 22px;"></section>
```

> 一行说完对象是谁，不做副标题段落。

### 首段（直接进结论）

```html
<p style="margin:0 0 20px;font-size:15px;line-height:1.95;letter-spacing:.3px;color:{{text}};text-align:justify;">{{第一段：一个反常识判断或一个具体结论，不写日期、不写“今天”。}}</p>
```

### 关键数字条（三格，细线分隔，无底色）

```html
<table cellpadding="0" cellspacing="0" style="width:100%;border-collapse:collapse;margin:20px 0 24px;">
  <tr>
    <td style="padding:0 16px 0 0;vertical-align:top;border-right:1px solid {{divider}};">
      <p style="margin:0 0 3px;font-size:21px;line-height:1.3;font-weight:700;letter-spacing:-.2px;color:{{text}};">{{60}}</p>
      <p style="margin:0;font-size:11px;line-height:1.6;letter-spacing:.4px;color:{{muted}};">{{指标名 · 如 Intelligence Index}}</p>
    </td>
    <td style="padding:0 16px;vertical-align:top;border-right:1px solid {{divider}};">
      <p style="margin:0 0 3px;font-size:21px;line-height:1.3;font-weight:700;letter-spacing:-.2px;color:{{text}};">{{$1.27}}</p>
      <p style="margin:0;font-size:11px;line-height:1.6;letter-spacing:.4px;color:{{muted}};">{{每任务成本}}</p>
    </td>
    <td style="padding:0 0 0 16px;vertical-align:top;">
      <p style="margin:0 0 3px;font-size:21px;line-height:1.3;font-weight:700;letter-spacing:-.2px;color:{{text}};">{{1.05M}}</p>
      <p style="margin:0;font-size:11px;line-height:1.6;letter-spacing:.4px;color:{{muted}};">{{上下文窗口}}</p>
    </td>
  </tr>
</table>
```

> 三格；数字用无衬线 21px，说明 11px 灰蓝。**不放卡片、不加底色**，只用一条竖线分格。
> 数字必须是可核验的；抓不到就少放一格，别凑。

### 图位（三类图，各有各的位置）

```html
<img src="{{IMG_A}}" style="max-width:100%;width:100%;display:block;margin:16px 0 22px;box-sizing:border-box;" alt="{{官方定价页截图}}"/>
```

| 图 | 放哪 | 证明什么 |
|---|---|---|
| A 官方定价 / 文档页 | 首段或第一个价格小节后 | 价格、档位、限额这类官方口径 |
| B 第三方榜单 / 实测 | 讲性价比、排名、速度时 | 别人的数据，必须标第三方口径 |
| C 模型卡 / 参数页 | 讲上下文、模态、截止日期时 | 参数原文 |

> 图片一律满栏、无边框、无圆角、**图下不写字**；图证明什么，写进它上面或下面的正文。
> 长图（榜单、文档）先裁成 2–4 段，按原顺序嵌进正文，不要整张长图塞进去。

### 小节（编号 + 英文微标 + 无衬线标题）

```html
<p style="margin:36px 0 0;font-size:10px;line-height:1.6;letter-spacing:2.6px;color:{{accent2}};text-transform:uppercase;">01 · {{PRICE}}</p>
<h2 style="margin:4px 0 14px;font-size:17px;line-height:1.6;font-weight:700;letter-spacing:.3px;color:{{text}};">{{钩子 · 不剧透结论}}</h2>
```

> 编号用 `01 / 02 / 03`；小节标题不带「一、二、三、」中文序号。
> 标题只写钩子，答案留在正文第一句。

### 正文段落

```html
<p style="margin:0 0 18px;font-size:15px;line-height:1.95;letter-spacing:.3px;color:{{text}};text-align:justify;">{{段落正文。官方口径写明出处，第三方口径写明是谁测的；数字不编。}}</p>
```

### 对照表（题签 + 书衣线 + 四向留白）

```html
<p style="margin:26px 0 0;font-size:11px;line-height:1.6;letter-spacing:4px;color:{{accent}};font-family:'Songti SC','STSong','SimSun',serif;text-align:center;">· {{对照名}} ·</p>
<table cellpadding="0" cellspacing="0" style="width:100%;border-collapse:collapse;margin:10px 0 12px;font-size:13px;line-height:1.75;border-top:2px solid {{accent}};">
  <tr>
    <th style="padding:10px 14px;text-align:left;font-weight:600;font-family:'Songti SC','STSong','SimSun',serif;letter-spacing:2px;color:{{accent}};background:{{codeBg}};border-bottom:1px solid {{cardBorder}};">{{列一}}</th>
    <th style="padding:10px 14px;text-align:left;font-weight:600;font-family:'Songti SC','STSong','SimSun',serif;letter-spacing:2px;color:{{accent}};background:{{codeBg}};border-bottom:1px solid {{cardBorder}};">{{列二}}</th>
  </tr>
  <tr>
    <td style="padding:12px 14px;color:{{text}};border-bottom:1px solid {{divider}};">{{行一}}</td>
    <td style="padding:12px 14px;color:{{text}};border-bottom:1px solid {{divider}};">{{行二}}</td>
  </tr>
</table>
```

> 题签居中宋体小字；顶线 2px 主色；表头宋体主色字；单元格四向留白 12px 14px，不贴边。
> 三列以内；列名写清楚口径（官方 / 第三方）。

### 定义行（无表头的参数表）

```html
<table cellpadding="0" cellspacing="0" style="width:100%;border-collapse:collapse;margin:22px 0 8px;font-size:13px;line-height:1.75;">
  <tr>
    <td style="padding:10px 14px;width:30%;color:{{muted}};border-bottom:1px solid {{divider}};">{{模型 ID}}</td>
    <td style="padding:10px 14px;color:{{text}};border-bottom:1px solid {{divider}};">{{gpt-6.1-sol}}</td>
  </tr>
</table>
```

### 引文（官方原话）

```html
<section style="margin:28px 0 30px;padding:2px 0 2px 18px;border-left:2px solid {{quoteBorder}};">
  <p style="margin:0 0 10px;font-size:16px;line-height:1.95;letter-spacing:.4px;color:{{text}};">「{{官方原话}}」</p>
  <p style="margin:0;font-size:12px;line-height:1.6;letter-spacing:.4px;color:{{muted}};">{{— 官方页面 / 文档章节}}</p>
</section>
```

### 收尾

```html
<p style="margin:0;font-size:15px;line-height:1.95;letter-spacing:.3px;color:{{text}};text-align:justify;">{{最后一句：给一个可执行的选择，写完就结束。}}</p>
```

## 节奏

- 段间 **18px**，小节前 **36px**；靠留白分段，不靠卡片。
- 图 **2–4 张**，一张图只服务一个论点；图与图之间至少隔一个段落或小节。
- 强调色全篇不超过 **6 次**；松石只给第三方口径与英文微标。
- 表头允许 `{{codeBg}}`，正文单元格一律白底；不用圆角、阴影、彩色虚线。
- 篇幅 **900–1600 汉字**；官方 / 媒体 / 第三方三类口径分开写。

## 适配

- 与 `ai-lab` 主题配套。
- 适合：模型发布速写、价格与额度对照、选型指南、基准解读、API 参数速查。
- 不适合：茶类内容（走 `tea-*` 模板）、纯促销电商（走 `taobao-flash`）、KPI 榜单（走 `hud`）。
