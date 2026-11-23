# 模板：tea-festival（茶志 · 节令茶单）

> **定位**：传统节假日 × 茶——春节守岁茶、清明新茶、端午、中秋、重阳、冬至、除夕的茶俗与家宴茶。
> **风格**：节令笔记。节日起行、俗语引路、家宴场景落地，参数收在最后。
> **搭配**：`tea-atelier` 主题。
> **写作前读**：`../references/tea-knowledge.md`；节俗是文化内容，茶俗细节有出处才写，不编故事；不写功效、不写吉凶。

## 骨架

### 外框

```html
<section style="max-width:677px;margin:0 auto;background:{{bg}};padding:30px 22px 50px;box-sizing:border-box;font-family:'PingFang SC',-apple-system,'Helvetica Neue','Microsoft YaHei',sans-serif;color:{{text}};">
```

> 正文不放 h1、不放灰字导语、文末不加页脚。

### 栏目签

```html
<p style="margin:0 0 20px;font-size:10px;line-height:1.6;letter-spacing:4px;color:{{accent}};text-transform:uppercase;">节令茶单 · FESTIVAL TEA</p>
```

### 首段（一句总纲）

```html
<p style="margin:0 0 22px;font-size:15px;line-height:1.95;letter-spacing:.5px;color:{{text}};text-align:justify;">{{第一段：从一个节日场景进入，说明这份节令茶单写给谁。}}
```

### 当令茶提示条（可选，全篇一个）

```html
<section style="margin:14px 0 18px;padding:10px 14px;border-top:1px solid {{cardBorder}};border-bottom:1px solid {{cardBorder}};">
  <p style="margin:0;font-size:13px;line-height:1.75;letter-spacing:.3px;color:{{text}};"><span style="color:{{accent}};font-weight:600;">{{当令}}</span>　{{冬至}} → <strong style="color:{{text}};">{{红茶、煮老白茶、熟普}}</strong></p>
</section>
```

> 细节见 `components.md` §16e；中性时间提示，禁止写成「宜 / 忌」。

### 节令条目（节日 + 日期 + 茶）

> 条目顶部可换 **节日题签**（`components.md` §16b：节日名 + 农历日期），替代「月.日」小签；农历与干支写法全篇统一。

```html
<section style="margin:32px 0 0;padding-top:12px;border-top:1px solid {{cardBorder}};">
  <p style="margin:0 0 4px;font-size:11px;line-height:1.6;letter-spacing:3px;color:{{accent2}};">{{腊月三十}}</p>
  <h2 style="margin:0 0 12px;font-size:17px;line-height:1.6;font-weight:700;letter-spacing:.6px;color:{{text}};font-family:'Songti SC','STSong','SimSun',serif;">{{除夕 · 守岁煮一壶老白茶}}</h2>
  <p style="margin:0 0 14px;font-size:15px;line-height:1.95;letter-spacing:.5px;color:{{text}};text-align:justify;">{{这个节令的家宴场景与茶位置，两句说完。}}</p>
  <p style="margin:0 0 18px;font-size:13px;line-height:1.7;letter-spacing:.3px;color:{{muted}};">{{茶样与泡法；水温区间、茶量 g / 水量 mL、时间区间及计时口径}}</p>
</section>
```

> 日期用农历或「节日名 + 公历日期」二选一，全篇统一；标题写「节日 + 一个动作」，不写茶名堆叠。
> 参数用一行小字收尾，不另开表。

### 俗谚/引文（每个节令最多一条）

```html
<section style="margin:16px 0 20px;padding:2px 0 2px 16px;border-left:3px solid {{quoteBorder}};">
  <p style="margin:0;font-size:14px;line-height:1.85;letter-spacing:.3px;color:{{muted}};font-family:'Songti SC','STSong','SimSun',serif;">{{俗谚或古籍引文一句}}</p>
  <p style="margin:6px 0 0;font-size:12px;line-height:1.6;letter-spacing:.4px;color:{{muted}};">{{— 出处《书名·篇目》}}</p>
</section>
```

> 引文必须给出处；没有出处的「老话」改写成自述，不装古籍。

### 节令分隔（换一个月用一次）

```html
<section style="height:1px;background:{{divider}};margin:26px 0 3px;"></section>
<section style="height:1px;background:{{divider}};margin:0 0 26px;"></section>
```

### 图片（每个节令最多一张）

```html
<img src="{{IMG_A}}" style="max-width:100%;width:100%;display:block;height:auto;margin:14px 0 20px;border:0;border-radius:0;box-sizing:border-box;" alt="{{描述}}"/>
```

> 可按组件库 §13a 加简短图注；整图超过约 2000px 或高宽比 > 4 套 `components.md` §13c 滑动框，交付前自测。

### 使用提醒（短，三条以内）

```html
<p style="margin:0 0 12px;font-size:15px;line-height:1.95;color:{{text}};text-align:justify;"><span style="color:{{accent}};font-weight:600;">·</span>　{{按实际茶样与家宴条件调整，不必凑齐全部节令。}}</p>
```

### 收尾

```html
<p style="margin:0;font-size:15px;line-height:1.95;letter-spacing:.5px;color:{{text}};text-align:justify;">{{最后一句：给读者一个最近的节日可以试的动作。}}</p>
```

## 节奏

- 节令条目 **3–4 个**，每个「日期 + 标题 + 2 段 + 参数行」为一组，俗谚可省。
- 条目之间 **32px**；跨月用节令分隔线隔开一次。
- 全篇图 **1–2 张**；使用提醒放在最后，不单独成节。
- 篇幅 **900–1300 汉字**；不写功效承诺，不写「排毒」「养胃」，不写年节吉凶。

## 适配

- 与 `tea-atelier` 主题配套。
- 适合：春节/清明/端午/中秋/重阳/冬至/除夕等节日茶俗、家宴茶单、送礼茶。
- 不适合：二十四节气茶单（改 `tea-almanac`）、茶史（改 `tea-culture`）、冲泡参数教学（改 `tea-notes`）。
