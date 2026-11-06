# 模板：tea-scroll（茶志 · 手卷）

> **定位**：茶事散文、公案、茶礼、寺院茶。以叙述为主，不做参数，不做对照。
> **风格**：窄栏、居中题记、点线分隔、宋体引文。像一截展开的手卷，字少、留白多。
> **搭配**：`tea-atelier` 主题。

## 骨架

### 外框（比常规窄 40px）

```html
<section style="max-width:677px;margin:0 auto;background:{{bg}};padding:34px 26px 52px;box-sizing:border-box;font-family:'PingFang SC',-apple-system,'Helvetica Neue','Microsoft YaHei',sans-serif;color:{{text}};">
```

> 正文不放 h1、不放灰字导语、文末不加页脚、不放来源列表。
> 全篇**不用表格**，靠句子和留白推进。

### 栏目签（居中）

```html
<p style="margin:0 0 26px;font-size:10px;line-height:1.6;letter-spacing:5px;color:{{accent}};text-transform:uppercase;text-align:center;">茶事 · TEA SCROLL</p>
```

### 题记（宋体居中，全篇唯一的大字）

```html
<p style="margin:0 0 30px;font-size:19px;line-height:1.9;letter-spacing:1px;color:{{text}};font-family:'Songti SC','STSong','SimSun',serif;text-align:center;">{{一句题记 · 不超过 18 字}}</p>
<section style="height:1px;background:{{divider}};margin:0 0 30px;"></section>
```

### 首段（直接进故事）

```html
<p style="margin:0 0 20px;font-size:15px;line-height:2;letter-spacing:.5px;color:{{text}};text-align:justify;">{{第一段：一个人、一句话、一个动作，直接开始，不解释背景。}}</p>
```

### 点线分隔（代替小节标题）

```html
<p style="margin:34px 0 24px;font-size:12px;line-height:1.6;letter-spacing:8px;color:{{accent}};text-align:center;">· · ·</p>
```

> 手卷不用编号，也不用 h2；分段只靠 `· · ·`。全篇 4–5 处即可，多了会碎。

### 短句独立段（节奏换气）

```html
<p style="margin:0 0 26px;font-size:17px;line-height:1.9;letter-spacing:.8px;color:{{text}};font-family:'Songti SC','STSong','SimSun',serif;text-align:center;">{{一句短判断 · 独立成段}}</p>
```

### 引文（居中，无竖线）

```html
<section style="margin:30px 0 32px;padding:0 6px;text-align:center;">
  <p style="margin:0 0 10px;font-size:16px;line-height:1.95;letter-spacing:.6px;color:{{text}};font-family:'Songti SC','STSong','SimSun',serif;">「{{引文}}」</p>
  <p style="margin:0;font-size:12px;line-height:1.6;letter-spacing:.4px;color:{{muted}};">{{— 出处}}</p>
</section>
```

### 图片（满栏，居中留白）

```html
<img src="{{IMG_A}}" style="max-width:100%;width:100%;display:block;margin:20px 0 26px;box-sizing:border-box;" alt="{{描述}}"/>
```

> 无边框、无圆角、图下不写字。黑白照片与手卷最合。

### 收尾

```html
<p style="margin:0;font-size:15px;line-height:2;letter-spacing:.5px;color:{{text}};text-align:justify;">{{最后一句：落回一个动作，写完就结束。}}</p>
```

## 节奏

- 段间 **20px**，分隔点上下 **24–34px**；全篇留白多于文字。
- **不用** h2、编号、表格、卡片；只用题记、短句、引文、点线四种件。
- 强调色出现不超过 **3 次**，只在栏目签与点线。
- 篇幅 **800–1300 汉字**；一段不超过 4 行。

## 适配

- 与 `tea-atelier` 主题配套。
- 适合：赵州吃茶去、径山茶宴、寺院茶礼、茶人小传、茶席随笔。
- 不适合：参数文（改 `tea-notes`）、器物对比（改 `tea-catalog`）。
