# 模板：tea-almanac（茶志 · 茶历）

> **定位**：按时间、节气、场景组织的喝茶建议。一天四泡、二十四节气、四季茶单。
> **风格**：历书。时间点起行、短句为主、双线分栏，参数收在最后。
> **搭配**：`tea-atelier` 主题。
> **写作前读**：`../references/tea-knowledge.md`；时间与节气是组织内容的线索，不构成健康建议。

## 骨架

### 外框

```html
<section style="max-width:677px;margin:0 auto;background:{{bg}};padding:30px 22px 50px;box-sizing:border-box;font-family:'PingFang SC',-apple-system,'Helvetica Neue','Microsoft YaHei',sans-serif;color:{{text}};">
```

> 正文不放 h1、不放灰字导语、文末不加页脚。

### 栏目签

```html
<p style="margin:0 0 20px;font-size:10px;line-height:1.6;letter-spacing:4px;color:{{accent}};text-transform:uppercase;">茶历 · TEA ALMANAC</p>
```

### 首段（一句总纲）

```html
<p style="margin:0 0 22px;font-size:15px;line-height:1.95;letter-spacing:.5px;color:{{text}};text-align:justify;">{{第一段：从一个真实生活场景进入，说明这份茶单适合谁。}}</p>
```

### 时间条目（时刻 + 茶类 + 一句）

```html
<section style="margin:32px 0 0;padding-top:12px;border-top:1px solid {{cardBorder}};">
  <p style="margin:0 0 4px;font-size:11px;line-height:1.6;letter-spacing:3px;color:{{accent2}};">07:00</p>
  <h2 style="margin:0 0 12px;font-size:17px;line-height:1.6;font-weight:700;letter-spacing:.6px;color:{{text}};font-family:'Songti SC','STSong','SimSun',serif;">{{早茶 · 留一点从容}}</h2>
  <p style="margin:0 0 14px;font-size:15px;line-height:1.95;letter-spacing:.5px;color:{{text}};text-align:justify;">{{这个场景的口味、器具与时间条件，两句说完。}}</p>
  <p style="margin:0 0 18px;font-size:13px;line-height:1.7;letter-spacing:.3px;color:{{muted}};">{{适用茶样与泡法；水温区间、茶量 g / 水量 mL、时间区间及计时口径}}</p>
</section>
```

> 时间用 24 小时制、两位数字；标题写「时段 + 一个动作」，不写茶名堆叠。
> 参数用一行小字收尾，不另开表。

### 双线分隔（换半天用一次）

```html
<section style="height:1px;background:{{divider}};margin:26px 0 3px;"></section>
<section style="height:1px;background:{{divider}};margin:0 0 26px;"></section>
```

### 图片（每个半天最多一张）

```html
<img src="{{IMG_A}}" style="max-width:100%;width:100%;display:block;margin:14px 0 20px;box-sizing:border-box;" alt="{{描述}}"/>
```

### 使用提醒（短，三条以内）

```html
<p style="margin:0 0 12px;font-size:15px;line-height:1.95;color:{{text}};text-align:justify;"><span style="color:{{accent}};font-weight:600;">·</span>　{{按实际器具与个人口味调整，不必凑齐全部时段。}}</p>
```

### 收尾

```html
<p style="margin:0;font-size:15px;line-height:1.95;letter-spacing:.5px;color:{{text}};text-align:justify;">{{最后一句：给读者一个适合当前场景的尝试动作。}}</p>
```

## 节奏

- 条目 **3–5 个**，每个「时刻 + 标题 + 2 段 + 参数行」为一组。
- 条目之间 **32px**；上半日与下半日之间用双线隔开一次。
- 全篇图 **1–2 张**；使用提醒放在最后，不单独成节。
- 篇幅 **900–1300 汉字**；不写功效承诺，不写「排毒」「养胃」这类词。

## 适配

- 与 `tea-atelier` 主题配套。
- 适合：一天四泡、二十四节气茶单、四季饮茶、办公室茶。
- 不适合：器物拆解（改 `tea-catalog`）、茶史（改 `tea-scroll`）。
