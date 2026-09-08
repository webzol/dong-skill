# 模板：wechat-pai-essay（微信派·文艺长文）

> **定位**：杂志文艺感长文版式。两端对齐、明显字距、PingFang SC 字体、微信绿强调。
> **风格**：克制、舒展、阅读优先。最适合品牌叙事、产品故事、深度长文。
> **搭配**：`wechat-pai` 主题色（白底 + 中灰字 + #07c160 微信绿）。

## 骨架（占位符替换为主题色）

> 通用外框与「字号/字距/对齐/字体族」由主题 typography 字段描述，
> 模板负责**节奏与装饰件**。所有 `<p>` 默认 `text-align:justify`（两端对齐）+ `letter-spacing:1px` + `line-height:1.6`。

### 页眉：单行小标签 + 大标题 + 副标题

```html
<section style="max-width:677px;margin:0 auto;background:{{bg}};color:{{text}};padding:32px 22px;box-sizing:border-box;font-family:'PingFang SC','PingFang SC NEW',-apple-system,'Helvetica Neue','Microsoft YaHei',sans-serif;">
  <p style="margin:0 0 18px;font-size:12px;letter-spacing:3px;color:{{accent}};text-transform:uppercase;">{{分类标签 · 如 BRAND / STORY}}</p>
  <h1 style="margin:0 0 14px;font-size:24px;line-height:1.4;font-weight:700;letter-spacing:1px;color:{{text}};">{{标题}}</h1>
  <p style="margin:0 0 24px;font-size:14px;letter-spacing:1px;color:{{muted}};">{{副标题 · 一句话引子}}</p>
  <section style="height:1px;background:{{divider}};margin:0 0 28px;"></section>
```

### 小节标题：编号 + 中文 + 微信绿装饰

```html
<section style="margin:36px 0 18px;">
  <p style="margin:0 0 8px;font-size:11px;letter-spacing:2px;color:{{accent}};font-weight:600;">N° {{01}}</p>
  <h2 style="margin:0;font-size:18px;line-height:1.5;font-weight:700;letter-spacing:1px;color:{{text}};">{{小节名}}</h2>
</section>
```

### 正文段落（两端对齐 + 大行距）

```html
<p style="margin:0 0 14px;font-size:15px;line-height:1.6;letter-spacing:1px;color:{{text}};text-align:justify;">{{段落正文……}}</p>
```

### 强调（行内）

```html
<p style="margin:0 0 14px;font-size:15px;line-height:1.6;letter-spacing:1px;color:{{text}};text-align:justify;">关键概念用 <strong style="color:{{accent}};font-weight:600;">{{微信绿强调}}</strong>，链接用 <a href="{{url}}" style="color:{{accent2}};text-decoration:none;border-bottom:1px solid {{accent2}};">{{蓝色超链}}</a>。</p>
```

### 引言 / 金句（点线左边 + 微信绿）

```html
<section style="margin:28px 0;padding:14px 0 14px 18px;border-left:2px dotted {{quoteBorder}};">
  <p style="margin:0;font-size:15px;line-height:1.7;letter-spacing:1px;color:{{text}};font-style:italic;">「{{引言 / 金句}}」</p>
  <p style="margin:10px 0 0;font-size:12px;letter-spacing:1.5px;color:{{muted}};">— {{署名}}</p>
</section>
```

### 分隔线（居中小圆点）

```html
<section style="margin:32px auto;text-align:center;color:{{divider}};letter-spacing:6px;">· · ·</section>
```

### 标签云（多 chip）

```html
<table cellpadding="0" cellspacing="0" style="margin:18px 0;">
  <tr>
    <td style="padding:0 6px 6px 0;"><section style="background:{{cardBg}};border:1px solid {{cardBorder}};border-radius:14px;padding:4px 12px;font-size:12px;letter-spacing:1px;color:{{muted}};">#{{标签1}}</section></td>
    <td style="padding:0 6px 6px 0;"><section style="background:{{cardBg}};border:1px solid {{cardBorder}};border-radius:14px;padding:4px 12px;font-size:12px;letter-spacing:1px;color:{{muted}};">#{{标签2}}</section></td>
    <td style="padding:0 6px 6px 0;"><section style="background:{{cardBg}};border:1px solid {{cardBorder}};border-radius:14px;padding:4px 12px;font-size:12px;letter-spacing:1px;color:{{muted}};">#{{标签3}}</section></td>
  </tr>
</table>
```

### 图片 + 图说（左右留白 + 居中图说）

```html
<img src="{{图片URL}}" style="display:block;width:100%;border-radius:6px;margin:24px 0;" alt="{{描述}}"/>
<p style="margin:-12px 0 24px;font-size:12px;letter-spacing:1px;color:{{muted}};text-align:center;">{{图说}}</p>
```

### 卡片（轻底 + 左侧细线）

```html
<section style="background:{{cardBg}};border-left:2px solid {{accent}};border-radius:6px;padding:16px 18px;margin:20px 0;">
  <p style="margin:0 0 6px;font-size:13px;letter-spacing:1.5px;color:{{accent}};font-weight:600;">{{卡片角标 · 如 CASE}}</p>
  <p style="margin:0;font-size:15px;line-height:1.7;letter-spacing:1px;color:{{text}};text-align:justify;">{{卡片内容}}</p>
</section>
```

### 行动号召按钮（微信绿填充）

```html
<table style="margin:30px auto;"><tr><td>
  <a href="{{链接}}" style="display:inline-block;background:{{accent}};color:#ffffff;font-size:14px;font-weight:600;letter-spacing:2px;padding:10px 26px;border-radius:24px;text-decoration:none;">{{按钮文字}}</a>
</td></tr></table>
```

### 页脚（订阅 / 品牌）

```html
<section style="margin-top:42px;padding-top:20px;border-top:1px solid {{divider}};text-align:center;">
  <p style="margin:0 0 4px;font-size:13px;letter-spacing:2px;color:{{accent}};font-weight:600;">{{品牌 / 栏目名}}</p>
  <p style="margin:0;font-size:12px;letter-spacing:1px;color:{{muted}};">{{一句脚注 · 扫码 / 留言 / 下期预告}}</p>
</section>
```

## 节奏要求

- **段间 14px**，**小节前 36px** —— 段落呼吸要够，靠空隙不靠装饰。
- **每段 ≤ 1 处强调**，强调用 `<strong>` 颜色就行，不堆边框/底色。
- **每 2-3 段一个分隔**（居中小圆点 · · ·）做节奏切换。
- **图片永远 100% 宽 + 6px 圆角**，图说与图之间 -12px 拉近。
- **全文最外层 padding 用 32px×22px**（比默认的 24×18 稍宽，匹配两端对齐的呼吸感）。
