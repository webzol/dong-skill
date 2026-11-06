# 模板：tea-catalog（茶志 · 图录）

> **定位**：单件器物的拆解。一把壶、一只盖碗、一个茶则，按部位逐条看。
> **风格**：博物馆图录。大编号、部位名、规格行，条目之间一条细线。
> **搭配**：`tea-atelier` 主题。

## 骨架

### 外框

```html
<section style="max-width:677px;margin:0 auto;background:{{bg}};padding:30px 20px 50px;box-sizing:border-box;font-family:'PingFang SC',-apple-system,'Helvetica Neue','Microsoft YaHei',sans-serif;color:{{text}};">
```

> 正文不放 h1、不放灰字导语、文末不加页脚。

### 栏目签

```html
<p style="margin:0 0 20px;font-size:10px;line-height:1.6;letter-spacing:4px;color:{{accent}};text-transform:uppercase;">图录 · TEA CATALOG</p>
```

### 首段

```html
<p style="margin:0 0 20px;font-size:15px;line-height:1.95;letter-spacing:.5px;color:{{text}};text-align:justify;">{{第一段：这件器物只有几个关键部位，其余都是装饰。}}</p>
```

### 器物全图（开篇一张，满栏）

```html
<img src="{{IMG_A}}" style="max-width:100%;width:100%;display:block;margin:6px 0 24px;box-sizing:border-box;" alt="{{器物全图}}"/>
```

### 条目头（大编号 + 部位名）

```html
<section style="margin:36px 0 14px;border-top:1px solid {{cardBorder}};padding-top:14px;">
  <p style="margin:0 0 2px;font-size:24px;line-height:1.2;letter-spacing:1px;color:{{accent}};font-family:'Songti SC','STSong','SimSun',serif;">01</p>
  <p style="margin:0;font-size:11px;line-height:1.6;letter-spacing:2.4px;color:{{accent2}};text-transform:uppercase;">{{SPOUT}} · 壶嘴</p>
</section>
```

> 编号用两位数字，古铜色，宋体；下面一行是英文 + 中文部位名。
> 每条目上方一条 `1px` 细线，不用底色。

### 条目正文（两段以内）

```html
<p style="margin:0 0 16px;font-size:15px;line-height:1.95;letter-spacing:.5px;color:{{text}};text-align:justify;">{{这一部位决定什么，怎么看，什么算好。}}</p>
```

### 规格行（三条以内，无表头）

```html
<table cellpadding="0" cellspacing="0" style="width:100%;border-collapse:collapse;margin:4px 0 8px;font-size:13px;line-height:1.7;">
  <tr>
    <td style="padding:10px 14px;width:26%;color:{{muted}};border-bottom:1px solid {{divider}};">{{看什么}}</td>
    <td style="padding:10px 14px;color:{{text}};border-bottom:1px solid {{divider}};">{{出水是否成线}}</td>
  </tr>
</table>
```

> 规格行同样四向留白（纵向 10px、横向 14px），文字不贴边；标签列维持 `{{muted}}`。
### 局部图（可选，紧贴对应条目）

```html
<img src="{{IMG_B}}" style="max-width:100%;width:100%;display:block;margin:14px 0 22px;box-sizing:border-box;" alt="{{局部}}"/>
```

### 引文（末尾一条）

```html
<section style="margin:32px 0 30px;padding:2px 0 2px 18px;border-left:2px solid {{quoteBorder}};">
  <p style="margin:0 0 10px;font-size:16px;line-height:1.95;letter-spacing:.6px;color:{{text}};font-family:'Songti SC','STSong','SimSun',serif;">「{{引文}}」</p>
  <p style="margin:0;font-size:12px;line-height:1.6;letter-spacing:.4px;color:{{muted}};">{{— 出处}}</p>
</section>
```

### 收尾

```html
<p style="margin:0;font-size:15px;line-height:1.95;letter-spacing:.5px;color:{{text}};text-align:justify;">{{最后一句：买之前摸一遍，摸完就知道。}}</p>
```

## 节奏

- 条目 **4–6 个**，每个「细线 + 大编号 + 2 段 + 规格行」为一组。
- 条目之间 **36px**；全篇图 **2 张**（全图 + 一张局部），不逐条配图。
- 规格行最多 3 条，只写可验证的观察点，不写「透气性好」这类空话。
- 篇幅 **900–1400 汉字**；不写价格、不写品牌。

## 适配

- 与 `tea-atelier` 主题配套。
- 适合：壶的五个部位、盖碗的六个部位、茶则 / 茶针 / 公道杯拆解。
- 不适合：多器对比（改 `tea-ware`）、茶史（改 `tea-culture`）。
