# 模板：hud（数据面板）

> **定位**：指标大字 + 迷你进度条 + 面板框。适合 KPI / 评测 / 榜单 / 数据总结。
> **风格**：仪表盘感，数字是主角，面板有框、进度条用色带，科技感强。

## 骨架（占位符替换为主题色）

### 页眉
```html
<section style="max-width:677px;margin:0 auto;background:{{bg}};color:{{text}};padding:24px 18px;box-sizing:border-box;">
  <section style="display:inline-block;background:{{accent}};color:{{bg}};font-size:12px;letter-spacing:2px;padding:3px 10px;border-radius:12px;">{{LIVE · 可选状态标签}}</section>
  <h1 style="margin:12px 0 6px;font-size:26px;line-height:1.3;font-weight:800;color:{{text}};letter-spacing:1px;">{{标题}}</h1>
  <p style="margin:0 0 22px;font-size:14px;color:{{muted}};">{{副标题 / 数据口径}}</p>
  <section style="height:1px;background:{{divider}};margin-bottom:22px;"></section>
```
> 若浏览器/微信不支持 `display:inline-block`，状态标签改为普通 `<span style="...">` 即可。

### 指标面板（单个大字）
```html
<section style="background:{{cardBg}};border:1px solid {{cardBorder}};border-radius:12px;padding:20px 18px;margin:16px 0;">
  <p style="margin:0;font-size:40px;font-weight:800;line-height:1;color:{{accent}};">{{数值，如 98.6%}}</p>
  <p style="margin:10px 0 0;font-size:14px;color:{{muted}};">{{指标名，如 通过率}}</p>
  <section style="height:4px;background:{{divider}};border-radius:2px;margin:16px 0 0;">
    <section style="height:4px;width:{{百分比}}%;background:{{accent2}};border-radius:2px;"></section>
  </section>
</section>
```

### KPI 三列（table 实现）
```html
<table width="100%" cellpadding="0" cellspacing="0" style="margin:16px 0;">
  <tr>
    <td width="33%" valign="top" style="padding-right:6px;">
      <section style="background:{{cardBg}};border:1px solid {{cardBorder}};border-radius:10px;padding:14px 10px;">
        <p style="margin:0;font-size:22px;font-weight:800;color:{{accent}};">{{A}}</p>
        <p style="margin:6px 0 0;font-size:12px;color:{{muted}};">{{A名}}</p>
      </section>
    </td>
    <td width="33%" valign="top" style="padding:0 3px;"> <!-- 中间列 -->
      <section style="background:{{cardBg}};border:1px solid {{cardBorder}};border-radius:10px;padding:14px 10px;">
        <p style="margin:0;font-size:22px;font-weight:800;color:{{accent}};">{{B}}</p>
        <p style="margin:6px 0 0;font-size:12px;color:{{muted}};">{{B名}}</p>
      </section>
    </td>
    <td width="33%" valign="top" style="padding-left:6px;">
      <section style="background:{{cardBg}};border:1px solid {{cardBorder}};border-radius:10px;padding:14px 10px;">
        <p style="margin:0;font-size:22px;font-weight:800;color:{{accent}};">{{C}}</p>
        <p style="margin:6px 0 0;font-size:12px;color:{{muted}};">{{C名}}</p>
      </section>
    </td>
  </tr>
</table>
```

### 对比条 / 榜单
```html
<section style="margin:14px 0;">
  <p style="margin:0 0 6px;font-size:13px;color:{{muted}};">{{榜单名}} —— <strong style="color:{{text}};">{{得分}}</strong></p>
  <section style="height:10px;background:{{divider}};border-radius:5px;">
    <section style="height:10px;width:{{得分}}%;background:{{accent}};border-radius:5px;"></section>
  </section>
</section>
```

### 页脚
```html
<section style="margin-top:32px;padding-top:16px;border-top:1px solid {{divider}};text-align:center;">
  <p style="margin:0 0 6px;font-size:20px;font-weight:800;color:{{accent}};">{{号召语，如 ↑ 点个关注}}</p>
  <p style="margin:0;font-size:13px;color:{{muted}};">{{附加说明}}</p>
</section>
```

## 节奏要求
- 数字 40px 或 22px 是主角；指标名 12–14px 灰字做配角。
- 进度条统一用「背景灰槽 + accent 色带」，高度 4–10px，圆角同槽高一半。
- 面板圆角 10–12px、边框 `1px solid {{cardBorder}}`；不要用 box-shadow 撑布局。
