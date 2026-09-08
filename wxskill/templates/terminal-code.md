# 模板：terminal-code（终端风）

> **定位**：等宽标题 + 命令符 `>` 引导 + 代码高亮块。最强「技术感 / 极客风」。
> **风格**：等宽字体、命令提示符、区块底色深、强调色做代码高亮。

## 骨架（占位符替换为主题色）

### 字族
正文与标题用等宽近似字族（微信不加载外链字体，用系统等宽逼近）：
```html
<!-- 统一 style 前缀 -->
font-family:'Menlo','Consolas','Courier New',monospace;
```

### 页眉（命令符标题）
```html
<section style="max-width:677px;margin:0 auto;background:{{bg}};color:{{text}};padding:24px 18px;box-sizing:border-box;">
  <section style="margin-bottom:6px;font-size:13px;color:{{accent}};letter-spacing:1px;font-family:'Menlo','Consolas',monospace;">
    &gt; {{路径，如 ~/projects/pub}}
  </section>
  <h1 style="margin:0 0 6px;font-size:24px;line-height:1.3;font-weight:700;color:{{text}};letter-spacing:1px;font-family:'Menlo','Consolas',monospace;">{{标题}}</h1>
  <section style="height:2px;background:{{accent}};margin:14px 0 24px;"></section>
```

### 命令 / 输出（逐条）
```html
<p style="margin:0 0 6px;font-size:14px;color:{{text}};font-family:'Menlo','Consolas',monospace;line-height:1.7;">
  <span style="color:{{accent}};">&gt;</span> <strong style="color:{{text}};">{{命令，如 npm run build}}</strong>
</p>
<p style="margin:0 0 16px 18px;font-size:13px;color:{{muted}};font-family:'Menlo','Consolas',monospace;line-height:1.7;">
  {{输出 / 说明}}
</p>
```

### 小节标题（等宽 + 前缀）
```html
<section style="border-left:3px solid {{accent}};padding-left:10px;font-size:19px;font-weight:700;color:{{text}};margin:30px 0 14px;line-height:1.4;font-family:'Menlo','Consolas',monospace;">
  <span style="color:{{accent2}};">##</span> {{小节名}}
</section>
```

### 代码块
```html
<section style="background:{{codeBg}};border-left:3px solid {{accent}};border-radius:6px;padding:14px 16px;margin:16px 0;font-size:14px;line-height:1.7;">
  <p style="margin:0;color:{{codeText}};font-family:'Menlo','Consolas',monospace;white-space:pre-wrap;">{{代码内容}}</p>
</section>
```

### 分隔线（等宽的 ---）
```html
<section style="margin:28px 0;font-family:'Menlo','Consolas',monospace;color:{{divider}};font-size:12px;letter-spacing:2px;text-align:center;">- - -</section>
```

### 页脚
```html
<section style="margin-top:30px;padding-top:16px;border-top:1px solid {{divider}};font-family:'Menlo','Consolas',monospace;">
  <p style="margin:0;font-size:13px;color:{{muted}};letter-spacing:1px;">&gt; exit</p>
  <p style="margin:6px 0 0;font-size:12px;color:{{muted}};">关注我们 · 下期见</p>
</section>
```

## 节奏要求
- 命令用 `>` 前缀、说明缩进 18px；重点命令加粗。
- 代码块底部边框仅作装饰，布局不依赖它（个别机型圆角/阴影弱化无妨）。
- 等宽字族是风格核心，但要保证可读性：正文代码 ≥ 13px。
