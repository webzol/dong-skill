# 版式组件库（拼版零件）

这里是一整套**原子块**，全都已做微信兼容（内联样式、无 flex/grid）。按需取用拼装文章。
占位符 `{{...}}` 在生成时替换为所选主题的色值；数字尺寸可按模板节奏微调。

> 组件里的 `{{bg}} {{text}} {{muted}} {{accent}} {{accent2}} {{cardBg}} {{cardBorder}} {{divider}} {{codeBg}} {{codeText}} {{titleBar}} {{quoteBorder}}` 全部来自 `themes/<theme>.json`。

---

## 1. 文章最外层（全文必有一个）

```html
<section style="max-width:677px;margin:0 auto;background:{{bg}};color:{{text}};padding:24px 18px;box-sizing:border-box;">
  <!-- 标题 / 正文 / 脚注都放这里 -->
</section>
```

## 2. 标题栏（页眉）

```html
<section style="border-top:2px solid {{titleBar}};padding-top:14px;">
  <section style="width:18px;height:18px;background:{{titleBar}};border-radius:3px;"></section>
</section>
<h1 style="margin:14px 0 6px;font-size:28px;line-height:1.3;font-weight:700;letter-spacing:1px;color:{{text}};">{{标题}}</h1>
<p style="margin:0 0 22px;font-size:14px;color:{{muted}};letter-spacing:.5px;">{{副标题}}</p>
<section style="height:1px;background:{{divider}};margin:0 0 26px;"></section>
```

## 3. 小节标题（左竖线式）

```html
<section style="border-left:4px solid {{accent}};padding-left:10px;font-size:20px;font-weight:700;color:{{text}};margin:34px 0 16px;line-height:1.4;">{{小节名}}</section>
```
（变体：左下角短横线 == 简约，不用竖线，改成 `border-bottom:2px solid {{accent}};padding-bottom:10px;`）

## 4. 正文段落

```html
<p style="margin:0 0 18px;font-size:16px;line-height:1.8;color:{{text}};letter-spacing:.3px;">{{段落文字}}</p>
<!-- 强调 -->
<p style="margin:0 0 18px;font-size:16px;line-height:1.8;color:{{text}};">重点用 <strong style="color:{{accent2}};">{{强调}}</strong> 提升</p>
```

## 5. 引言 / 金句（引用块）

```html
<section style="margin:24px 0;padding:16px 18px;background:{{cardBg}};border-left:4px solid {{quoteBorder}};border-radius:8px;">
  <p style="margin:0;font-size:15px;line-height:1.7;color:{{text}};">「{{引言内容}}」</p>
  <p style="margin:10px 0 0;font-size:13px;color:{{muted}};">—— {{署名}}</p>
</section>
```

## 6. 卡片（单块）

```html
<section style="background:{{cardBg}};border:1px solid {{cardBorder}};border-radius:10px;padding:18px 16px;margin:16px 0;">
  <p style="margin:0 0 8px;font-size:17px;font-weight:700;color:{{text}};">{{卡片标题}}</p>
  <p style="margin:0;font-size:15px;line-height:1.7;color:{{text}};">{{卡片内容}}</p>
</section>
```

## 7. 双列并排（table，代替 flex）

```html
<table width="100%" cellpadding="0" cellspacing="0" style="margin:16px 0;">
  <tr>
    <td width="50%" valign="top" style="padding-right:8px;">{{左块}}</td>
    <td width="50%" valign="top" style="padding-left:8px;">{{右块}}</td>
  </tr>
</table>
```

## 8. 分隔线

```html
<section style="height:1px;background:{{divider}};margin:30px 0;"></section>
```

## 9. 代码块

```html
<section style="background:{{codeBg}};border-left:3px solid {{accent}};border-radius:6px;padding:14px 16px;margin:16px 0;">
  <p style="margin:0;color:{{codeText}};font-size:14px;line-height:1.7;font-family:'Menlo','Consolas','Courier New',monospace;white-space:pre-wrap;">{{代码}}</p>
</section>
```

## 10. 行内代码

```html
<code style="background:{{codeBg}};color:{{codeText}};font-family:'Menlo','Consolas',monospace;padding:2px 5px;border-radius:4px;">{{code}}</code>
```

## 11. 按钮 / 行动号召

```html
<!-- 用 table 做居中按钮（避免用 flex/定位） -->
<table style="margin:24px auto;"><tr><td>
  <a href="{{链接}}" style="display:inline-block;background:{{accent}};color:{{bg}};font-size:15px;font-weight:600;padding:10px 24px;border-radius:6px;text-decoration:none;">{{按钮文字}}</a>
</td></tr></table>
```

## 12. 列表

```html
<!-- 左竖线列表 -->
<section style="margin:14px 0;">
  <p style="margin:0 0 8px;border-left:3px solid {{accent}};padding-left:10px;font-size:15px;line-height:1.6;color:{{text}};">{{项 1}}</p>
  <p style="margin:0 0 8px;border-left:3px solid {{divider}};padding-left:10px;font-size:15px;line-height:1.6;color:{{text}};">{{项 2}}</p>
</section>
```
（如需标准 `<ul>`：`<ul style="padding-left:18px;color:{{text}};font-size:15px;line-height:1.8;"><li>{{项}}</li></ul>`）

## 13. 图片 + 说明

```html
<img src="{{图片URL}}" style="max-width:100%;width:100%;border-radius:8px;margin:16px 0;" alt="{{描述}}"/>
<p style="margin:-8px 0 16px;font-size:12px;color:{{muted}};text-align:center;">{{图片说明}}</p>
```
> 图片 `src` 必须是**公网可访问**的 URL（微信不会本地存图）；`.gif` 也支持。

## 14. 数据指标（单条）

```html
<section style="background:{{cardBg}};border:1px solid {{cardBorder}};border-radius:12px;padding:20px 18px;margin:16px 0;">
  <p style="margin:0;font-size:40px;font-weight:800;line-height:1;color:{{accent}};">{{数值}}</p>
  <p style="margin:10px 0 0;font-size:14px;color:{{muted}};">{{指标名}}</p>
</section>
```

## 15. 脚注 / 关注引导

```html
<section style="margin-top:34px;padding-top:18px;border-top:1px solid {{divider}};">
  <p style="margin:0;font-size:13px;color:{{muted}};letter-spacing:.5px;text-align:center;">{{脚注文字}}</p>
</section>
```

## 组装口诀

- **先外框，后内容**：全文只有一个 677px 外框。
- **标题→小节→段落→特殊块** 依次排列；特殊块（引言/卡片/代码/数据）复用组件。
- 节奏：段间 18px、小节前 34px、卡片间 16px，别乱塞间距。
- 生成时把所有 `{{x}}` 换成主题色；**不要新增主题之外的色值**。
