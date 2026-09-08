# 模板：cyber-card（卡片风）

> **定位**：圆角卡片分隔块，块与块之间用卡片承载，最有「产品感」。
> **风格**：卡片 + 圆角 + 细边框 + 主题强调色点缀。

## 骨架（占位符替换为主题色）

### 页眉（卡片标题卡）
```html
<section style="max-width:677px;margin:0 auto;background:{{bg}};color:{{text}};padding:24px 18px;box-sizing:border-box;">
  <section style="background:{{cardBg}};border:1px solid {{cardBorder}};border-radius:12px;padding:22px 20px;">
    <p style="margin:0 0 6px;font-size:12px;letter-spacing:2px;color:{{accent}};">{{栏目小标 · 可选}}</p>
    <h1 style="margin:0;font-size:26px;line-height:1.3;font-weight:700;color:{{text}};">{{标题}}</h1>
    <p style="margin:10px 0 0;font-size:14px;color:{{muted}};">{{副标题}}</p>
  </section>
</section>
```

### 单卡片块
```html
<section style="background:{{cardBg}};border:1px solid {{cardBorder}};border-radius:10px;padding:18px 16px;margin:16px 0;">
  <p style="margin:0 0 8px;font-size:17px;font-weight:700;color:{{text}};">{{卡片标题}}</p>
  <p style="margin:0;font-size:15px;line-height:1.7;color:{{text}};">{{卡片内容}}</p>
</section>
```

### 双列卡片（用 table 实现，不用 flex）
```html
<table width="100%" cellpadding="0" cellspacing="0" style="margin:16px 0;">
  <tr>
    <td width="50%" valign="top" style="padding-right:8px;">
      <section style="background:{{cardBg}};border:1px solid {{cardBorder}};border-radius:10px;padding:16px 12px;">
        <p style="margin:0;font-weight:700;color:{{text}};">左卡标题</p>
        <p style="margin:6px 0 0;font-size:13px;color:{{muted}};">左卡内容</p>
      </section>
    </td>
    <td width="50%" valign="top" style="padding-left:8px;">
      <section style="background:{{cardBg}};border:1px solid {{cardBorder}};border-radius:10px;padding:16px 12px;">
        <p style="margin:0;font-weight:700;color:{{text}};">右卡标题</p>
        <p style="margin:6px 0 0;font-size:13px;color:{{muted}};">右卡内容</p>
      </section>
    </td>
  </tr>
</table>
```

### 强调卡（顶部色条）
```html
<section style="background:{{cardBg}};border:1px solid {{cardBorder}};border-top:3px solid {{accent}};border-radius:10px 10px 10px 10px;padding:16px;margin:16px 0;">
  <p style="margin:0;font-size:15px;line-height:1.7;color:{{text}};">{{强调内容}}</p>
</section>
```

### 页脚
```html
<section style="margin-top:32px;padding-top:16px;border-top:1px solid {{cardBorder}};">
  <p style="margin:0;font-size:13px;color:{{muted}};text-align:center;letter-spacing:1px;">点击卡片 · 关注我们</p>
</section>
```

## 节奏要求
- 卡片间距 16px，圆角统一 10–12px，边框统一 `1px solid {{cardBorder}}`。
- 卡片内标题 + 正文两档字号（17/15px or 16/13px），别塞太多层级。
- 需要「网格」一律用 table 双列/三列，别用 flex。
