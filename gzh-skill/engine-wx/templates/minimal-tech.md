# 模板：minimal-tech（简约科技）

> **定位**：细标题线 + 大留白 + 干净信息流。最「简约科技」，默认模板。
> **风格**：克制、留白为骨、字距为魂。装饰只用一个细线和一个强调色。

## 骨架（占位符替换为主题色）

### 页眉
```html
<!--- 标题栏：左上 4px 竖线 + 上方细横线 --->
<section style="max-width:677px;margin:0 auto;background:{{bg}};color:{{text}};padding:24px 18px;box-sizing:border-box;">
  <section style="border-top:2px solid {{titleBar}};padding-top:14px;">
    <section style="width:18px;height:18px;background:{{titleBar}};border-radius:3px;"></section>
  </section>
  <h1 style="margin:14px 0 6px;font-size:28px;line-height:1.3;font-weight:700;letter-spacing:1px;color:{{text}};">{{标题}}</h1>
  <p style="margin:0 0 22px;font-size:14px;color:{{muted}};letter-spacing:.5px;">{{副标题 · 可选}}</p>
  <section style="height:1px;background:{{divider}};margin:0 0 26px;"></section>
```

### 小节标题
```html
<h2 style="margin:34px 0 16px;font-size:20px;font-weight:700;color:{{text}};display:flex;align-items:center;">
  <span style="display:inline-block;width:4px;height:20px;background:{{accent}};margin-right:10px;"></span>
  {{小节名}}
</h2>
```
> 注意：`display:flex` 在微信里可能失效 — 请改为：
> `<section style="border-left:4px solid {{accent}};padding-left:10px;font-size:20px;font-weight:700;color:{{text}};margin:34px 0 16px;line-height:1.4;">{{小节名}}</section>`

### 正文段落
```html
<p style="margin:0 0 18px;font-size:16px;line-height:1.8;color:{{text}};letter-spacing:.3px;">
  正文。重点可用 <strong style="color:{{accent2}};">强调文字</strong> 或 <em style="color:{{muted}};">辅助</em>。
</p>
```

### 分隔线
```html
<section style="height:1px;background:{{divider}};margin:30px 0;"></section>
```

### 页脚
```html
<section style="margin-top:34px;padding-top:18px;border-top:1px solid {{divider}};">
  <p style="margin:0;font-size:13px;color:{{muted}};letter-spacing:.5px;text-align:center;">
    关注我们 · 获取更多
  </p>
</section>
```

## 节奏要求
- 段间留白 18px、小节前 34px —— 用留白说话，别用边框堆砌。
- 每段 ≤ 2 处强调，突出即克制。
- 引用、卡片、代码等特殊块一律复用 `references/components.md`（本模板语境下列表用朴素 `<ul>` + 左竖线）。
