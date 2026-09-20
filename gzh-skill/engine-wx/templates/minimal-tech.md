# 模板：minimal-tech（简约科技）

> **定位**：细标题线 + 大留白 + 干净信息流。最「简约科技」，默认模板。
> **风格**：克制、留白为骨、字距为魂。装饰只用一个细线和一个强调色。

## 骨架（占位符替换为主题色）

### 页眉
```html
<section class="gzh-article" style="max-width:677px;margin:0 auto;background:{{bg}};color:{{text}};padding:24px 18px;box-sizing:border-box;">
  <h1 class="gzh-title" style="margin:14px 0 6px;font-size:18px;line-height:1.3;font-weight:700;letter-spacing:1px;color:{{text}};">{{标题}}</h1>
  <section class="gzh-divider" style="height:1px;background:{{divider}};margin:0 0 26px;"></section>
```

### 小节标题
```html
<h2 class="gzh-section" style="margin:34px 0 16px;font-size:20px;font-weight:700;color:{{text}};">
  {{小节名}}
</h2>
```
> 注意：本节标题不含左侧竖条（微信兼容性更稳定）。如需竖条可加 `<span style="display:inline-block;width:4px;height:20px;background:{{accent}};margin-right:10px;border-radius:2px;"></span>`

### 正文段落
```html
<p class="gzh-body" style="margin:0 0 18px;font-size:16px;line-height:1.8;color:{{text}};letter-spacing:.3px;">
  正文。重点可用 <strong class="gzh-accent" style="color:{{accent2}};">强调文字</strong> 或 <em style="color:{{muted}};">辅助</em>。
</p>
```

### 卡片块
```html
<section class="gzh-card" style="background:{{cardBg}};border:1px solid {{cardBorder}};border-radius:14px;padding:18px 16px;margin:16px 0;">
  <p style="margin:0 0 8px;font-size:17px;font-weight:700;color:{{text}};">{{卡片标题}}</p>
  <p style="margin:0;font-size:15px;line-height:1.7;color:{{text}};">{{卡片内容}}</p>
</section>
```

### 分隔线
```html
<section class="gzh-divider" style="height:1px;background:{{divider}};margin:30px 0;"></section>
```

### 页脚
```html
<section style="margin-top:34px;padding-top:18px;border-top:1px solid {{divider}};">
  <p style="margin:0;font-size:13px;color:{{muted}};letter-spacing:.5px;text-align:center;">
    关注我们 · 获取更多
  </p>
</section>
```

## 动态换肤 JS 约定

- 所有可换肤元素使用 CSS 类：`.gzh-title` `.gzh-subtitle` `.gzh-body` `.gzh-section` `.gzh-card` `.gzh-divider` `.gzh-accent`
- 根容器 `class="gzh-article"` + `data-theme-*` 属性
- 换肤函数：
  ```js
  function applyTheme(theme){
    var el=document.querySelector('.gzh-article');
    var c=theme.colors;
    el.style.background=c.bg; el.style.color=c.text;
    document.querySelectorAll('.gzh-title,.gzh-section').forEach(function(e){e.style.color=c.text;});
    document.querySelectorAll('.gzh-subtitle,.gzh-body').forEach(function(e){e.style.color=c.text;});
    document.querySelectorAll('.gzh-subtitle').forEach(function(e){e.style.color=c.muted;});
    document.querySelectorAll('.gzh-accent').forEach(function(e){e.style.color=c.accent2;});
    document.querySelectorAll('.gzh-card').forEach(function(e){e.style.background=c.cardBg;e.style.border='1px solid '+c.cardBorder;});
    document.querySelectorAll('.gzh-divider').forEach(function(e){e.style.background=c.divider;});
  }
  ```
- 预览页自动加载主题选择弹窗（见 `references/components.md` 的 theme-picker 组件）
