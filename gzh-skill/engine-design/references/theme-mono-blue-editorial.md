# 公众号排版组件库 —— 墨蓝刊读

> **使用说明**：本组件库为「墨蓝刊读」主题，所有组件使用**内联样式**，可直接复制粘贴到微信公众号编辑器。
>
> **设计风格**：黑白杂志气质——纯白纸底 + 强对比黑白灰阶为唯一基调，克莱因蓝 `#1B3A8C` 作为全文唯一点睛强调色，衬线字体（标题/数字）与无衬线小标签（Arial）分工，直角无阴影、层次全靠边框与留白建立。整体克制、理性、国际编辑部气质，信息密度中等，适合深度观点、专题报道、教程与盘点等多种文章类型。
>
> **公众号平台限制须知**：
> - ❌ 不支持 `<style>`/`<script>`、CSS class/id、`position:fixed/absolute`、`float`、`@media`/`@keyframes`、`display:grid`
> - ✅ 支持内联 `style`、`display:flex`（含 `gap`）、`border-radius`、`<section>/<p>/<span>/<strong>/<img>/<figure>/<figcaption>/<hr>/<table>/<tr>/<td>` 等基础标签
>
> **WeChat 兼容铁律**（本主题组件全部已按此写好，改动时必须遵守）：
> - 原始区块库中的 `id="block-*"` 与预览标签均已清除；新增组件同样不能带 `id`/`class`/`<div>`
> - 所有文字节点一律 `<span leaf="">` 包裹，装饰性空元素内放 `<span leaf=""><br></span>`
> - 行内代码一律用 `<span>` 模拟（不用 `<code>` 标签）；按钮一律用 `<span>` 模拟（不用 `<a>`/`<button>`）
> - 图片一律只保留 `src`/`alt`/`style`，用 `max-width:100%;height:auto;display:block;margin:0 auto;`
> - 全部直角（0px 圆角）、无阴影、无渐变，层级只靠黑边框/灰边框/深色底/留白表达

---

## 设计变量速查表

```
克莱因蓝（唯一点睛强调/编号/标签/下划线）： #1B3A8C
浅克莱因蓝（装饰线/代码命令文字）：          #5B7FD6 / #7B93D6
正文色：                                   #1A1A1A
次要文字：                                 #333333 / #3A3A3A / #4A4A4A
辅助文字：                                 #6B6B6B
弱化文字：                                 #8A8A8A / #9A9A9A / #B0B0B0
深黑底（刊头/引文页/页脚）：                 #111111
背景色：                                   #FFFFFF
浅灰背景（信息卡/流程/图注底）：              #F5F5F5 / #F0F0F0
浅蓝高亮底（文字强调 b）：                   #E8EDF8
边框/分隔线：                               #D9D9D9（灰）/ #1A1A1A（强）
正文字号：                                 15px
正文行高：                                 1.95
标签/图注字号：                             11px / 12px（Arial）
最大宽度：                                 677px
区块左右内边距：                             22px（正文组件统一）
圆角：                                     0px（全部直角，仅个别标签不容圆角）
阴影：                                     无阴影，层次全部靠边框与留白建立
```

字体栈：
- 正文/标题（衬线）：`Georgia,'Songti SC','STSong','SimSun',serif`
- 标签/数字/说明（无衬线）：`Arial,'PingFang SC','Microsoft YaHei',sans-serif`
- 代码：`'Courier New',monospace`

**正文关键词下划线**（对应 theme-index"正文下划线 CSS"列）：`border-bottom:2px solid #1B3A8C;font-weight:600;`——克莱因蓝是全文唯一点睛色，下划线即"点睛"本体，每段 1~3 处、全文克制使用。

---

## 组件 1 全局容器

```html
<section style="max-width:677px;margin:0 auto;background-color:#FFFFFF;color:#1A1A1A;font-family:Georgia,'Songti SC','STSong','SimSun',serif;line-height:1.8;">

  <!-- 所有组件放在这里，第一个子元素是组件 2 封面刊头；正文组件自带 margin-bottom 与 padding:0 22px -->

</section>
```

---

## 组件 2 封面刊头 cover-masthead

**用途**：文章开篇封面区，黑底反白刊头，杂志第一版面。全文唯一一处、放在最前面。

**可替换字段**：`{{刊号标签}}` `{{主标题}}` `{{副标题说明}}`

```html
<section style="margin:0 0 28px 0;padding:36px 22px 30px 22px;background-color:#111111;">
  <p style="margin:0 0 12px 0;"><span leaf=""><span style="display:inline-block;padding:2px 10px;border:1px solid #FFFFFF;color:#FFFFFF;font-size:11px;letter-spacing:2px;font-family:Arial,'PingFang SC',sans-serif;">{{刊号标签}}</span></span></p>
  <p style="margin:0 0 14px 0;font-size:24px;font-weight:700;line-height:1.4;color:#FFFFFF;"><span leaf="">{{主标题}}</span></p>
  <p style="margin:0 0 14px 0;width:44px;height:3px;background-color:#5B7FD6;font-size:0;line-height:0;"><span leaf=""><br></span></p>
  <p style="margin:0;font-family:Arial,'PingFang SC',sans-serif;font-size:13px;line-height:1.7;color:#BFBFBF;"><span leaf="">{{副标题说明}}</span></p>
</section>
```

---

## 组件 3 头版摘要卡 lead-summary

**用途**：封面之后的一句话导读，头版摘要位。

**可替换字段**：`{{一句话导读}}`

```html
<section style="margin:0 0 28px 0;padding:0 22px;">
  <p style="margin:0 0 8px 0;font-family:Arial,'PingFang SC',sans-serif;font-size:12px;font-weight:700;color:#1B3A8C;letter-spacing:2px;"><span leaf="">摘要 · SUMMARY</span></p>
  <p style="margin:0;font-size:16px;line-height:1.75;color:#1A1A1A;font-weight:600;"><span leaf="">{{一句话导读}}</span></p>
</section>
```

---

## 组件 4 编者按 editors-note

**用途**：交代选题缘由或阅读方式的克制引言，上下强黑边框。仅原文有独立引言/背景说明时使用。

**可替换字段**：`{{编者按内容}}`

```html
<section style="margin:0 0 28px 0;padding:20px 22px;border-top:1px solid #1A1A1A;border-bottom:1px solid #1A1A1A;">
  <p style="margin:0 0 10px 0;font-family:Arial,'PingFang SC',sans-serif;font-size:12px;font-weight:700;color:#1A1A1A;letter-spacing:2px;"><span leaf="">编者按</span></p>
  <p style="margin:0;font-size:14px;line-height:1.85;color:#3A3A3A;font-style:italic;"><span leaf="">{{编者按内容}}</span></p>
</section>
```

---

## 组件 5 期号标签条 issue-tag

**用途**：专栏名 + 期号 + 阅读时长的横向信息条，轻量分节过渡。

**可替换字段**：`{{专栏名}}` `{{期号}}` `{{阅读时长}}`

```html
<section style="margin:0 0 28px 0;padding:0 22px;">
  <p style="margin:0;display:flex;align-items:center;">
    <span style="font-family:Arial,'PingFang SC',sans-serif;font-size:11px;color:#1A1A1A;letter-spacing:1.5px;font-weight:700;"><span leaf="">{{专栏名}} · {{期号}}</span></span>
    <span style="flex:1;height:1px;background-color:#D9D9D9;margin:0 10px;font-size:0;line-height:0;"><span leaf=""><br></span></span>
    <span style="font-family:Arial,'PingFang SC',sans-serif;font-size:11px;color:#8A8A8A;letter-spacing:1px;"><span leaf="">{{阅读时长}}</span></span>
  </p>
</section>
```

---

## 组件 6 分栏索引卡 section-index

**用途**：目录/章节索引，蓝色衬线大编号 + 章节名，长文专用（3000 字以上建议使用）。行数按实际章节增删。

**可替换字段**：`{{章节标题一}}` `{{章节标题二}}` `{{章节标题三}}`

```html
<section style="margin:0 0 28px 0;padding:0 22px;">
  <p style="margin:0;padding:14px 0;border-top:1px solid #1A1A1A;border-bottom:1px solid #D9D9D9;display:flex;align-items:baseline;">
    <span style="font-family:Georgia,serif;font-size:20px;font-weight:700;color:#1B3A8C;margin-right:12px;"><span leaf="">01</span></span>
    <span style="font-size:14px;color:#1A1A1A;"><span leaf="">{{章节标题一}}</span></span>
  </p>
  <p style="margin:0;padding:14px 0;border-bottom:1px solid #D9D9D9;display:flex;align-items:baseline;">
    <span style="font-family:Georgia,serif;font-size:20px;font-weight:700;color:#1B3A8C;margin-right:12px;"><span leaf="">02</span></span>
    <span style="font-size:14px;color:#1A1A1A;"><span leaf="">{{章节标题二}}</span></span>
  </p>
  <p style="margin:0;padding:14px 0;border-bottom:1px solid #D9D9D9;display:flex;align-items:baseline;">
    <span style="font-family:Georgia,serif;font-size:20px;font-weight:700;color:#1B3A8C;margin-right:12px;"><span leaf="">03</span></span>
    <span style="font-size:14px;color:#1A1A1A;"><span leaf="">{{章节标题三}}</span></span>
  </p>
</section>
```

---

## 组件 7 章节编号标题 numbered-chapter

**用途**：大章节标题，默认主力分节样式，蓝色衬线编号 01/02/03…（末章编号可用 ///）。

**可替换字段**：`{{编号}}` `{{章节标题}}`

```html
<section style="margin:28px 0 24px 0;padding:0 22px;">
  <p style="margin:0;display:flex;align-items:baseline;border-bottom:2px solid #1A1A1A;padding-bottom:10px;">
    <span style="font-family:Georgia,serif;font-size:22px;font-weight:700;color:#1B3A8C;margin-right:10px;"><span leaf="">{{编号}}</span></span>
    <span style="font-size:18px;font-weight:700;color:#1A1A1A;"><span leaf="">{{章节标题}}</span></span>
  </p>
</section>
```

---

## 组件 8 栏目条大标题 column-title

**用途**：黑底反白栏目条，重量级分节强调（全文 ≤2 处），用于开启一个大板块。

**可替换字段**：`{{栏目标题}}`

```html
<section style="margin:28px 0 24px 0;padding:0 22px;">
  <p style="margin:0;padding:10px 14px;background-color:#111111;font-size:17px;font-weight:700;color:#FFFFFF;"><span leaf="">{{栏目标题}}</span></p>
</section>
```

---

## 组件 9 引题式标题 kicker-title

**用途**：小节引题（KICKER）+ 主标题的两行结构，用于专题式分节。

**可替换字段**：`{{引题}}` `{{主标题}}`

```html
<section style="margin:28px 0 24px 0;padding:0 22px;">
  <p style="margin:0 0 6px 0;font-family:Arial,'PingFang SC',sans-serif;font-size:12px;color:#1B3A8C;letter-spacing:2px;font-weight:700;"><span leaf="">{{引题}}</span></p>
  <p style="margin:0;font-size:19px;font-weight:700;line-height:1.4;color:#1A1A1A;"><span leaf="">{{主标题}}</span></p>
</section>
```

---

## 组件 10 小节标签标题 label-subtitle

**用途**：章节内的二级小标题，克莱因蓝小标签 + 加粗标题。

**可替换字段**：`{{小节标签}}` `{{小节标题}}`

```html
<section style="margin:24px 0 20px 0;padding:0 22px;">
  <p style="margin:0;"><span leaf=""><span style="font-family:Arial,'PingFang SC',sans-serif;font-size:11px;color:#FFFFFF;background-color:#1B3A8C;padding:2px 8px;margin-right:8px;">{{小节标签}}</span><span style="font-size:15px;font-weight:700;color:#1A1A1A;">{{小节标题}}</span></span></p>
</section>
```

---

## 组件 11 标准正文段落 body-paragraph（含文字强调 a–d）

**用途**：正文主力段落组件。每段主动标记 1~3 处关键词强调。

```html
<section style="margin:0 0 22px 0;padding:0 22px;">
  <p style="margin:0 0 16px 0;font-size:15px;line-height:1.95;color:#1A1A1A;"><span leaf="">正文段落占位，用于承接上一段的论点，补充说明或给出反例。段落长度控制在四到六行为宜，避免一整块无停顿的长文字。</span></p>
</section>
```

**文字强调**（写进段落 `<span leaf="">` 内部）：
- a 强调加粗：`<strong><span leaf="">{{关键词}}</span></strong>`
- b 浅蓝高亮：`<span style="background-color:#E8EDF8;padding:0 2px;"><span leaf="">{{关键词}}</span></span>`
- c 克莱因蓝下划线（**默认标记**，每段 1~3 处）：`<span style="border-bottom:2px solid #1B3A8C;font-weight:600;"><span leaf="">{{关键词}}</span></span>`
- d 行内代码：`<span style="font-family:'Courier New',monospace;font-size:13px;background-color:#F0F0F0;color:#1B3A8C;padding:1px 6px;"><span leaf="">{{代码}}</span></span>`

---

## 组件 12 首字下沉段落 dropcap-paragraph

**用途**：章节开篇导语段，首字放大下沉（衬线蓝色），全文 ≤2 处。

**可替换字段**：`{{首字}}` `{{导语段落内容}}`

```html
<section style="margin:0 0 22px 0;padding:0 22px;">
  <p style="margin:0;font-size:15px;line-height:1.95;color:#1A1A1A;"><span leaf=""><span style="font-size:24px;font-weight:700;line-height:1;color:#1B3A8C;">{{首字}}</span>{{导语段落内容，用于章节开篇，交代背景与问题意识，篇幅控制在三到五句为宜，避免与正文段落混淆。}}</span></p>
</section>
```

---

## 组件 13 大字强调段落 emphasis-paragraph

**用途**：核心判断/金句的独立强调段（20px 加粗），全文 ≤2 处。

**可替换字段**：`{{强调段落}}`

```html
<section style="margin:0 0 22px 0;padding:0 22px;">
  <p style="margin:0;font-size:20px;font-weight:700;line-height:1.6;color:#1A1A1A;"><span leaf="">{{强调段落：真正重要的判断，放在这里单独成段。}}</span></p>
</section>
```

---

## 组件 14 行内代码段落 inline-code-paragraph

**用途**：整句需要嵌入行内代码/字段名时的段落写法（`<span>` 模拟，不用 `<code>`）。

**可替换字段**：`{{段落文字一}}` `{{占位变量名}}` `{{段落文字二}}`

```html
<section style="margin:0 0 22px 0;padding:0 22px;">
  <p style="margin:0;font-size:15px;line-height:1.9;color:#1A1A1A;"><span leaf="">{{段落文字一}}</span><span style="font-family:'Courier New',monospace;font-size:13px;background-color:#F0F0F0;color:#1B3A8C;padding:1px 6px;"><span leaf="">{{占位变量名}}</span></span><span leaf="">{{段落文字二}}</span></p>
</section>
```

---

## 组件 15 大引文页 full-quote-page

**用途**：黑底反白金句页，全文最强的收束/转场锚点，全文 ≤1 处。

**可替换字段**：`{{引用金句}}` `{{引用来源}}`

```html
<section style="margin:0 0 28px 0;padding:36px 22px;background-color:#111111;">
  <p style="margin:0 0 16px 0;font-family:Georgia,'Songti SC','STSong','SimSun',serif;font-size:22px;font-weight:700;line-height:1.6;color:#FFFFFF;"><span leaf="">“{{引用金句}}”</span></p>
  <p style="margin:0;font-family:Arial,'PingFang SC',sans-serif;font-size:12px;color:#8A8A8A;letter-spacing:1px;"><span leaf="">—— {{引用来源}}</span></p>
</section>
```

---

## 组件 16 短引用条 quote-strip

**用途**：轻量引用，克莱因蓝左竖条，用于承上启下的短句。

**可替换字段**：`{{引用内容}}`

```html
<section style="margin:0 0 24px 0;padding:14px 18px;border-left:3px solid #1B3A8C;">
  <p style="margin:0;font-size:14px;line-height:1.85;color:#333333;font-style:italic;"><span leaf="">{{引用内容，一到两行}}</span></p>
</section>
```

---

## 组件 17 提示卡组（提示 / 警示 / 结论 / 背景）

**用途**：四类语义提示卡，按内容语义四选一。

**提示卡 NOTE**：

```html
<section style="margin:0 0 22px 0;padding:16px 18px;border:1px solid #D9D9D9;">
  <p style="margin:0 0 6px 0;font-family:Arial,'PingFang SC',sans-serif;font-size:12px;font-weight:700;color:#1B3A8C;letter-spacing:1px;"><span leaf="">提示 · NOTE</span></p>
  <p style="margin:0;font-size:14px;line-height:1.8;color:#333333;"><span leaf="">{{提示说明}}</span></p>
</section>
```

**警示卡 CAUTION**：

```html
<section style="margin:0 0 22px 0;padding:16px 18px;border:1px solid #1A1A1A;border-left:4px solid #1A1A1A;">
  <p style="margin:0 0 6px 0;font-family:Arial,'PingFang SC',sans-serif;font-size:12px;font-weight:700;color:#1A1A1A;letter-spacing:1px;"><span leaf="">警示 · CAUTION</span></p>
  <p style="margin:0;font-size:14px;line-height:1.8;color:#333333;"><span leaf="">{{警示说明}}</span></p>
</section>
```

**结论卡 RESULT**：

```html
<section style="margin:0 0 22px 0;padding:16px 18px;border:1px solid #D9D9D9;border-left:4px solid #1B3A8C;">
  <p style="margin:0 0 6px 0;font-family:Arial,'PingFang SC',sans-serif;font-size:12px;font-weight:700;color:#1B3A8C;letter-spacing:1px;"><span leaf="">结论 · RESULT</span></p>
  <p style="margin:0;font-size:14px;line-height:1.8;color:#333333;"><span leaf="">{{结论说明}}</span></p>
</section>
```

**背景信息卡 INFO**：

```html
<section style="margin:0 0 22px 0;padding:16px 18px;background-color:#F5F5F5;">
  <p style="margin:0 0 6px 0;font-family:Arial,'PingFang SC',sans-serif;font-size:12px;font-weight:700;color:#1A1A1A;letter-spacing:1px;"><span leaf="">背景 · INFO</span></p>
  <p style="margin:0;font-size:14px;line-height:1.8;color:#333333;"><span leaf="">{{背景信息}}</span></p>
</section>
```

---

## 组件 18 编辑旁注 editor-remark

**用途**：正文旁的小字补充说明，"注·"蓝色前缀。

**可替换字段**：`{{旁注内容}}`

```html
<section style="margin:0 0 24px 0;padding:0 22px;">
  <p style="margin:0;font-size:13px;line-height:1.8;color:#6B6B6B;"><span leaf=""><span style="color:#1B3A8C;font-weight:700;">注·</span>{{旁注内容}}</span></p>
</section>
```

---

## 组件 19 步骤条 step-strip

**用途**：操作步骤，蓝色衬线 STEP 编号 + 灰分隔线，教程类主力组件。

**可替换字段**：`{{步骤编号}}` `{{步骤说明}}`

```html
<section style="margin:0 0 24px 0;padding:0 22px;">
  <p style="margin:0 0 12px 0;padding-bottom:12px;border-bottom:1px solid #D9D9D9;display:flex;align-items:baseline;">
    <span style="font-family:Georgia,serif;font-size:18px;font-weight:700;color:#1B3A8C;margin-right:10px;"><span leaf="">STEP {{步骤编号一}}</span></span>
    <span style="font-size:14px;color:#1A1A1A;"><span leaf="">{{步骤说明一}}</span></span>
  </p>
  <p style="margin:0 0 12px 0;padding-bottom:12px;border-bottom:1px solid #D9D9D9;display:flex;align-items:baseline;">
    <span style="font-family:Georgia,serif;font-size:18px;font-weight:700;color:#1B3A8C;margin-right:10px;"><span leaf="">STEP {{步骤编号二}}</span></span>
    <span style="font-size:14px;color:#1A1A1A;"><span leaf="">{{步骤说明二}}</span></span>
  </p>
  <p style="margin:0;display:flex;align-items:baseline;">
    <span style="font-family:Georgia,serif;font-size:18px;font-weight:700;color:#1B3A8C;margin-right:10px;"><span leaf="">STEP {{步骤编号三}}</span></span>
    <span style="font-size:14px;color:#1A1A1A;"><span leaf="">{{步骤说明三}}</span></span>
  </p>
</section>
```

---

## 组件 20 流程总览 process-overview

**用途**：节点流程条，末节点用蓝底反白标记当前/关键阶段。

**可替换字段**：`{{节点一}}` `{{节点二}}` `{{节点三}}`

```html
<section style="margin:0 0 24px 0;padding:16px 18px;background-color:#F5F5F5;">
  <p style="margin:0;display:flex;align-items:center;flex-wrap:wrap;">
    <span style="font-family:Arial,'PingFang SC',sans-serif;font-size:11px;color:#1A1A1A;border:1px solid #1A1A1A;padding:4px 8px;"><span leaf="">{{节点一}}</span></span>
    <span style="margin:0 6px;color:#8A8A8A;font-size:12px;"><span leaf="">→</span></span>
    <span style="font-family:Arial,'PingFang SC',sans-serif;font-size:11px;color:#1A1A1A;border:1px solid #1A1A1A;padding:4px 8px;"><span leaf="">{{节点二}}</span></span>
    <span style="margin:0 6px;color:#8A8A8A;font-size:12px;"><span leaf="">→</span></span>
    <span style="font-family:Arial,'PingFang SC',sans-serif;font-size:11px;color:#FFFFFF;background-color:#1B3A8C;padding:4px 8px;"><span leaf="">{{节点三}}</span></span>
  </p>
</section>
```

---

## 组件 21 时间线 timeline

**用途**：阶段/事件时间线，左竖线 + 蓝色节点标记。

**可替换字段**：`{{节点时间一}}` `{{节点说明一}}` `{{节点时间二}}` `{{节点说明二}}`

```html
<section style="margin:0 0 24px 0;padding:0 22px;">
  <p style="margin:0 0 14px 0;padding-left:14px;border-left:2px solid #1A1A1A;">
    <span style="display:block;font-family:Arial,'PingFang SC',sans-serif;font-size:11px;color:#1B3A8C;font-weight:700;margin-bottom:4px;"><span leaf="">{{节点时间一}}</span></span>
    <span style="font-size:13px;color:#333333;"><span leaf="">{{节点说明一}}</span></span>
  </p>
  <p style="margin:0;padding-left:14px;border-left:2px solid #D9D9D9;">
    <span style="display:block;font-family:Arial,'PingFang SC',sans-serif;font-size:11px;color:#8A8A8A;font-weight:700;margin-bottom:4px;"><span leaf="">{{节点时间二}}</span></span>
    <span style="font-size:13px;color:#333333;"><span leaf="">{{节点说明二}}</span></span>
  </p>
</section>
```

---

## 组件 22 图片卡 media-image

**用途**：配图 + 可选图注。无图注时删除 `<figcaption>` 整行。

**可替换字段**：`{{图片地址}}` `{{图片说明}}` `{{图注}}`

```html
<section style="margin:0 0 24px 0;padding:0 22px;">
  <figure style="margin:0;padding:0;">
    <img src="{{图片地址}}" alt="{{图片说明}}" style="max-width:100%;height:auto;display:block;margin:0 auto;">
    <figcaption style="margin:8px 0 0 0;font-family:Arial,'PingFang SC',sans-serif;font-size:11px;color:#8A8A8A;"><span leaf="">{{图注}}</span></figcaption>
  </figure>
</section>
```

---

## 组件 23 双图对比 dual-image-compare

**用途**：A/B 对照两组图片，蓝色小标签分组。

**可替换字段**：`{{对照标签A}}` `{{图片地址A}}` `{{对照标签B}}` `{{图片地址B}}`

```html
<section style="margin:0 0 24px 0;padding:0 22px;">
  <p style="margin:0 0 6px 0;font-family:Arial,'PingFang SC',sans-serif;font-size:11px;color:#1B3A8C;font-weight:700;letter-spacing:1px;"><span leaf="">{{对照标签A}}</span></p>
  <figure style="margin:0 0 14px 0;padding:0;">
    <img src="{{图片地址A}}" alt="{{对照图片A}}" style="max-width:100%;height:auto;display:block;margin:0 auto;">
  </figure>
  <p style="margin:0 0 6px 0;font-family:Arial,'PingFang SC',sans-serif;font-size:11px;color:#1B3A8C;font-weight:700;letter-spacing:1px;"><span leaf="">{{对照标签B}}</span></p>
  <figure style="margin:0;padding:0;">
    <img src="{{图片地址B}}" alt="{{对照图片B}}" style="max-width:100%;height:auto;display:block;margin:0 auto;">
  </figure>
</section>
```

---

## 组件 24 图注说明卡 caption-card

**用途**：示意图 + 浅灰底长图注（图 01 式编号），适合交代图表来源或含义。

**可替换字段**：`{{图片地址}}` `{{示意图说明}}` `{{编号}}` `{{较长图注说明}}`

```html
<section style="margin:0 0 24px 0;padding:0 22px;">
  <figure style="margin:0;padding:0;">
    <img src="{{图片地址}}" alt="{{示意图说明}}" style="max-width:100%;height:auto;display:block;margin:0 auto;">
    <figcaption style="margin:8px 0 0 0;padding:8px 10px;background-color:#F5F5F5;font-family:Arial,'PingFang SC',sans-serif;font-size:11px;line-height:1.6;color:#4A4A4A;"><span leaf="">图 {{编号}} · {{较长图注说明}}</span></figcaption>
  </figure>
</section>
```

---

## 组件 25 深色代码块 code-dark

**用途**：终端/命令行风格代码块（默认）。每行一个 `<p style="margin:0">`，命令行用浅克莱因蓝，输出行浅灰，行首缩进用全角空格。

**可替换字段**：`{{代码行}}` `{{输出行}}`

```html
<section style="margin:0 0 24px 0;padding:16px 18px;background-color:#111111;">
  <p style="margin:0 0 4px 0;font-family:'Courier New',monospace;font-size:13px;line-height:1.6;color:#7B93D6;"><span leaf="">{{代码行一}}</span></p>
  <p style="margin:0;font-family:'Courier New',monospace;font-size:13px;line-height:1.6;color:#DDDDDD;"><span leaf="　{{输出行}}"></span></p>
</section>
```

---

## 组件 26 浅色代码块 code-light

**用途**：配置/字段展示风格代码块。

**可替换字段**：`{{代码行}}` `{{注释行}}`

```html
<section style="margin:0 0 24px 0;padding:16px 18px;background-color:#F0F0F0;border:1px solid #D9D9D9;">
  <p style="margin:0 0 4px 0;font-family:'Courier New',monospace;font-size:13px;line-height:1.6;color:#1B3A8C;"><span leaf="">{{代码行}}</span></p>
  <p style="margin:0;font-family:'Courier New',monospace;font-size:13px;line-height:1.6;color:#333333;"><span leaf="　{{注释行}}"></span></p>
</section>
```

---

## 组件 27 数据表格 data-table

**用途**：真实数据表格（仅表格语义使用 `table`），黑粗表头线 + 灰行线，数值列克莱因蓝加粗。

**可替换字段**：`{{字段}}` `{{条目}}` `{{数值}}` `{{备注}}`

```html
<section style="margin:0 0 24px 0;padding:0 22px;">
  <table style="width:100%;border-collapse:collapse;font-size:13px;">
    <tr style="border-bottom:2px solid #1A1A1A;">
      <td style="padding:8px 6px;font-family:Arial,'PingFang SC',sans-serif;font-weight:700;color:#1A1A1A;"><span leaf="">{{字段一}}</span></td>
      <td style="padding:8px 6px;font-family:Arial,'PingFang SC',sans-serif;font-weight:700;color:#1A1A1A;"><span leaf="">{{字段二}}</span></td>
      <td style="padding:8px 6px;font-family:Arial,'PingFang SC',sans-serif;font-weight:700;color:#1A1A1A;"><span leaf="">{{字段三}}</span></td>
    </tr>
    <tr style="border-bottom:1px solid #D9D9D9;">
      <td style="padding:8px 6px;color:#333333;"><span leaf="">{{条目一}}</span></td>
      <td style="padding:8px 6px;color:#1B3A8C;font-weight:700;"><span leaf="">{{数值一}}</span></td>
      <td style="padding:8px 6px;color:#6B6B6B;"><span leaf="">{{备注一}}</span></td>
    </tr>
    <tr>
      <td style="padding:8px 6px;color:#333333;"><span leaf="">{{条目二}}</span></td>
      <td style="padding:8px 6px;color:#1B3A8C;font-weight:700;"><span leaf="">{{数值二}}</span></td>
      <td style="padding:8px 6px;color:#6B6B6B;"><span leaf="">{{备注二}}</span></td>
    </tr>
  </table>
</section>
```

---

## 组件 28 参数对照表 param-table

**用途**：两列参数/字段对照表。

**可替换字段**：`{{参数名}}` `{{取值说明}}`

```html
<section style="margin:0 0 24px 0;padding:0 22px;">
  <table style="width:100%;border-collapse:collapse;font-size:13px;">
    <tr style="border-bottom:1px solid #D9D9D9;">
      <td style="padding:8px 6px;color:#6B6B6B;width:36%;"><span leaf="">{{参数名一}}</span></td>
      <td style="padding:8px 6px;color:#1A1A1A;"><span leaf="">{{取值说明一}}</span></td>
    </tr>
    <tr style="border-bottom:1px solid #D9D9D9;">
      <td style="padding:8px 6px;color:#6B6B6B;"><span leaf="">{{参数名二}}</span></td>
      <td style="padding:8px 6px;color:#1A1A1A;"><span leaf="">{{取值说明二}}</span></td>
    </tr>
    <tr>
      <td style="padding:8px 6px;color:#6B6B6B;"><span leaf="">{{参数名三}}</span></td>
      <td style="padding:8px 6px;color:#1A1A1A;"><span leaf="">{{取值说明三}}</span></td>
    </tr>
  </table>
</section>
```

---

## 组件 29 指标卡 metric-card

**用途**：单个关键指标，黑边框卡 + 蓝色衬线大数字。

**可替换字段**：`{{指标数值}}` `{{指标说明}}`

```html
<section style="margin:0 0 24px 0;padding:18px 20px;border:1px solid #1A1A1A;">
  <p style="margin:0 0 4px 0;font-family:Georgia,serif;font-size:24px;font-weight:700;color:#1B3A8C;"><span leaf="">{{指标数值}}</span></p>
  <p style="margin:0;font-family:Arial,'PingFang SC',sans-serif;font-size:12px;color:#6B6B6B;letter-spacing:0.5px;"><span leaf="">{{指标说明}}</span></p>
</section>
```

---

## 组件 30 进度条 progress-bar

**用途**：单一进度指标，蓝色进度 + 灰底轨。

**可替换字段**：`{{进度说明}}` `{{百分比}}`（如 `72%`，两处需一致）

```html
<section style="margin:0 0 24px 0;padding:0 22px;">
  <p style="margin:0 0 6px 0;display:flex;justify-content:space-between;">
    <span style="font-family:Arial,'PingFang SC',sans-serif;font-size:12px;color:#1A1A1A;"><span leaf="">{{进度说明}}</span></span>
    <span style="font-family:Arial,'PingFang SC',sans-serif;font-size:12px;color:#1B3A8C;font-weight:700;"><span leaf="">{{百分比}}</span></span>
  </p>
  <p style="margin:0;height:4px;background-color:#EAEAEA;font-size:0;line-height:0;"><span leaf=""><span style="display:block;width:{{百分比}};height:4px;background-color:#1B3A8C;"><br></span></span></p>
</section>
```

---

## 组件 31 优劣对照卡 pros-cons-card

**用途**：优势/局限两段式对照，蓝框优势 + 灰框局限。

**可替换字段**：`{{优势标签}}` `{{优势说明}}` `{{局限标签}}` `{{局限说明}}`

```html
<section style="margin:0 0 24px 0;padding:0 22px;">
  <p style="margin:0 0 8px 0;padding:12px 14px;border:1px solid #1B3A8C;">
    <span style="display:block;font-family:Arial,'PingFang SC',sans-serif;font-size:11px;color:#1B3A8C;font-weight:700;margin-bottom:4px;"><span leaf="">{{优势标签}}</span></span>
    <span style="font-size:13px;color:#333333;"><span leaf="">{{优势说明}}</span></span>
  </p>
  <p style="margin:0;padding:12px 14px;border:1px solid #D9D9D9;">
    <span style="display:block;font-family:Arial,'PingFang SC',sans-serif;font-size:11px;color:#8A8A8A;font-weight:700;margin-bottom:4px;"><span leaf="">{{局限标签}}</span></span>
    <span style="font-size:13px;color:#333333;"><span leaf="">{{局限说明}}</span></span>
  </p>
</section>
```

---

## 组件 32 列表组（无序 / 有序 / 任务清单）

**无序列表**（灰左竖条）：

```html
<section style="margin:0 0 22px 0;padding:0 22px;">
  <p style="margin:0 0 8px 0;padding-left:14px;border-left:2px solid #D9D9D9;font-size:14px;color:#1A1A1A;"><span leaf="">{{条目一}}</span></p>
  <p style="margin:0 0 8px 0;padding-left:14px;border-left:2px solid #D9D9D9;font-size:14px;color:#1A1A1A;"><span leaf="">{{条目二}}</span></p>
  <p style="margin:0;padding-left:14px;border-left:2px solid #D9D9D9;font-size:14px;color:#1A1A1A;"><span leaf="">{{条目三}}</span></p>
</section>
```

**有序列表**（蓝色衬线序号）：

```html
<section style="margin:0 0 22px 0;padding:0 22px;">
  <p style="margin:0 0 8px 0;display:flex;"><span style="font-family:Georgia,serif;font-size:13px;font-weight:700;color:#1B3A8C;margin-right:8px;"><span leaf="">1.</span></span><span style="font-size:14px;color:#1A1A1A;"><span leaf="">{{条目一}}</span></span></p>
  <p style="margin:0 0 8px 0;display:flex;"><span style="font-family:Georgia,serif;font-size:13px;font-weight:700;color:#1B3A8C;margin-right:8px;"><span leaf="">2.</span></span><span style="font-size:14px;color:#1A1A1A;"><span leaf="">{{条目二}}</span></span></p>
  <p style="margin:0;display:flex;"><span style="font-family:Georgia,serif;font-size:13px;font-weight:700;color:#1B3A8C;margin-right:8px;"><span leaf="">3.</span></span><span style="font-size:14px;color:#1A1A1A;"><span leaf="">{{条目三}}</span></span></p>
</section>
```

**任务清单**（方框 + 蓝底已完成划线）：

```html
<section style="margin:0 0 22px 0;padding:0 22px;">
  <p style="margin:0 0 8px 0;display:flex;align-items:center;"><span style="display:inline-block;width:14px;height:14px;border:1px solid #1A1A1A;margin-right:8px;"><span leaf=""><br></span></span><span style="font-size:14px;color:#1A1A1A;"><span leaf="">{{待办条目}}</span></span></p>
  <p style="margin:0;display:flex;align-items:center;"><span style="display:inline-block;width:14px;height:14px;background-color:#1B3A8C;margin-right:8px;"><span leaf=""><br></span></span><span style="font-size:14px;color:#1A1A1A;text-decoration:line-through;"><span leaf="">{{已完成条目}}</span></span></p>
</section>
```

---

## 组件 33 FAQ 问答卡 faq

**用途**：常见问题，蓝色 Q· 前缀 + 灰色 A· 回答。

**可替换字段**：`{{问题}}` `{{回答}}`

```html
<section style="margin:0 0 22px 0;padding:0 22px;">
  <p style="margin:0 0 8px 0;font-size:14px;font-weight:700;color:#1A1A1A;"><span leaf=""><span style="color:#1B3A8C;">Q·</span>{{问题}}</span></p>
  <p style="margin:0;padding-left:16px;font-size:13px;line-height:1.8;color:#4A4A4A;"><span leaf=""><span style="color:#8A8A8A;">A·</span>{{回答}}</span></p>
</section>
```

---

## 组件 34 作者信息卡 author-card

**用途**：作者署名 + 一句话简介，上下黑边框，常与固定签名段落配合。

**可替换字段**：`{{作者署名}}` `{{作者简介}}`

```html
<section style="margin:0 0 22px 0;padding:16px 18px;border-top:1px solid #1A1A1A;border-bottom:1px solid #1A1A1A;">
  <p style="margin:0 0 4px 0;font-size:14px;font-weight:700;color:#1A1A1A;"><span leaf="">{{作者署名}}</span></p>
  <p style="margin:0;font-family:Arial,'PingFang SC',sans-serif;font-size:12px;color:#6B6B6B;line-height:1.7;"><span leaf="">{{作者简介}}</span></p>
</section>
```

---

## 组件 35 延伸阅读卡 further-reading

**用途**：文末相关内容索引，灰分隔线列表。

**可替换字段**：`{{延伸阅读一}}` `{{延伸阅读二}}`

```html
<section style="margin:0 0 22px 0;padding:0 22px;">
  <p style="margin:0 0 8px 0;padding:10px 0;border-bottom:1px solid #D9D9D9;font-size:13px;color:#1A1A1A;"><span leaf="">{{延伸阅读一}}</span></p>
  <p style="margin:0;padding:10px 0;font-size:13px;color:#1A1A1A;"><span leaf="">{{延伸阅读二}}</span></p>
</section>
```

---

## 组件 36 资源引导条 download-strip

**用途**：附带资料/工具获取方式，浅灰底 + 蓝色引导标签。

**可替换字段**：`{{资源说明}}` `{{引导文案}}`

```html
<section style="margin:0 0 22px 0;padding:14px 18px;background-color:#F5F5F5;">
  <p style="margin:0;display:flex;align-items:center;justify-content:space-between;">
    <span style="font-size:13px;color:#1A1A1A;"><span leaf="">{{资源说明}}</span></span>
    <span style="font-family:Arial,'PingFang SC',sans-serif;font-size:11px;color:#1B3A8C;border:1px solid #1B3A8C;padding:4px 10px;"><span leaf="">{{引导文案}}</span></span>
  </p>
</section>
```

---

## 组件 37 结尾总结区 ending-summary

**用途**：文末总结，顶部 2px 黑线开段，蓝色 SUMMARY 标签。

**可替换字段**：`{{结尾总结}}`

```html
<section style="margin:0 0 22px 0;padding:20px 22px;border-top:2px solid #1A1A1A;">
  <p style="margin:0 0 6px 0;font-family:Arial,'PingFang SC',sans-serif;font-size:12px;font-weight:700;color:#1B3A8C;letter-spacing:2px;"><span leaf="">总结 · SUMMARY</span></p>
  <p style="margin:0;font-size:14px;line-height:1.85;color:#333333;"><span leaf="">{{结尾总结：回顾全篇的核心判断，并给出一个简短的收束句。}}</span></p>
</section>
```

---

## 组件 38 末尾互动区 engagement-strip

**用途**：文末互动引导（{{文末互动引导}} 用 SKILL.md 固定文案第二段）。

**可替换字段**：`{{文末互动引导}}`

```html
<section style="margin:0 0 22px 0;padding:0 22px;">
  <p style="margin:0;font-size:14px;line-height:1.8;color:#1A1A1A;"><span leaf="">{{文末互动引导}}</span></p>
</section>
```

---

## 组件 39 装饰分隔符 divider-mark

**用途**：轻量过渡分隔，三枚蓝色圆点。

```html
<section style="margin:0 0 22px 0;padding:0 22px;text-align:center;">
  <p style="margin:0;font-family:Georgia,serif;font-size:14px;color:#1B3A8C;letter-spacing:6px;"><span leaf="">· · ·</span></p>
</section>
```

---

## 组件 40 页脚版权条 footer-bar

**用途**：全文最末的黑底版权条，全文唯一、放在全局容器闭合之前最后一个组件。

**可替换字段**：`{{版权说明}}`

```html
<section style="margin:28px 0 0 0;padding:16px 22px;background-color:#111111;text-align:center;">
  <p style="margin:0;font-family:Arial,'PingFang SC',sans-serif;font-size:11px;color:#8A8A8A;letter-spacing:1px;"><span leaf="">{{版权说明}} · 保留全部权利</span></p>
</section>
```

---

## 完整文章模板骨架

```html
<section style="max-width:677px;margin:0 auto;background-color:#FFFFFF;color:#1A1A1A;font-family:Georgia,'Songti SC','STSong','SimSun',serif;line-height:1.8;">

  <!-- 1. 封面刊头（组件2 cover-masthead，全文唯一，放最前） -->

  <!-- 2. 期号标签条（组件5 issue-tag，可选，专栏连载时用） -->

  <!-- 3. 头版摘要卡（组件3 lead-summary）或 编者按（组件4 editors-note，二选一） -->

  <!-- 4. 目录（组件6 section-index，可选，3000字以上长文建议使用） -->

  <!-- 5. 第一章（组件7 numbered-chapter，编号01） -->
  <!--    章内按需组合：组件11 正文段落(+文字强调a-d) / 组件12 首字下沉 / 组件13 大字强调 -->
  <!--    / 组件14 行内代码段落 / 组件17 提示卡组 / 组件18 编辑旁注 / 组件19-21 步骤·流程·时间线 -->
  <!--    / 组件22-24 图片 / 组件25-26 代码块 / 组件27-31 数据·指标·对照 / 组件32 列表组 / 组件10 小节标题 -->

  <!-- 6. 第二章…第N章（同上结构，编号递增，末章编号可用 ///；章节间过渡可插组件5/39， -->
  <!--    分节样式不宜超过2种交替使用） -->

  <!-- 7. 全文收束（按文章类型定，见配方表）：组件37 结尾总结区 / 组件15 大引文页（金句收束，≤1处） -->

  <!-- 8. 延伸阅读（组件35，可选） / 资源引导条（组件36，可选） / FAQ（组件33，可选） -->

  <!-- 9. 固定签名段落（组件11 正文段落，SKILL.md 固定文案第一段） + 作者信息卡（组件34，可选） -->

  <!-- 10. 末尾互动区（组件38，{{文末互动引导}} 用 SKILL.md 固定文案第二段） -->

  <!-- 11. 页脚版权条（组件40，全文唯一，最后一个组件） -->

</section>

<!-- 12. 隐藏标记（外层容器之外，全文最后一个元素） -->
<p style="display:none;">
  <mp-style-type data-value="3"></mp-style-type>
</p>
```

**骨架铁律**：
- 封面刊头（组件 2）全文唯一、必须在最前；页脚版权条（组件 40）全文唯一、必须在最后；隐藏标记必须在全局容器闭合**之后**。
- 克莱因蓝是全文唯一点睛色：编号、标签、下划线、进度条都是它的变体，**不要再引入第二种彩色**；高亮/强调每段 ≤2 处。
- 大引文页（组件 15）与结尾引导类的深色块是全文最强的视觉锚点，全文深色块（刊头+引文页+栏目条+页脚）合计 ≤4 处。
- 分节样式在 组件 7/8/9 三种里选 1~2 种保持节奏统一；组件 8 全文 ≤2 处。

---

## 视觉层级（3 层递进）

| 层级 | 样式 | 用途 | 频率 |
|------|------|------|------|
| **锚点层** | 封面刊头 2、大引文页 15、栏目条 8、页脚 40（黑底反白） | 全文最强开篇/收束/转场 | 全文 ≤4 处深色块 |
| **标记层** | 克莱因蓝下划线（强调 c）、浅蓝高亮（强调 b） | 正文关键词强调 | 每段 1~3 处 |
| **容器层** | 指标卡 29、优劣对照卡 31、提示卡组 17、步骤条 19、分栏索引卡 6 | 数据、清单、提示、目录 | 按需 |

---

## 文章类型 → 组件组合配方

按 SKILL.md 第 3 步判定的文章类型选配方；核心组件构成本篇的排版主旋律，点缀组件按内容出现处使用，一篇文章点缀组件种类 ≤3。

| 文章类型 | 核心组件组合 | 点缀组件 |
|---|---|---|
| 深度观点/专题报道 | 封面刊头2 + 头版摘要卡3 + 章节编号标题7 + 正文段落11 + 大字强调段落13 + 大引文页15 + 结尾总结区37 | 编者按4、编辑旁注18、首字下沉12 |
| 教程/操作指南 | 封面刊头2 + 期号标签条5 + 章节编号标题7 + 步骤条19 + 行内代码段落14 + 深色代码块25 + 结尾总结区37 | 提示卡17（NOTE/CAUTION）、任务清单32、图注说明卡24 |
| 盘点/工具评测 | 封面刊头2 + 章节编号标题7 + 数据表格27 + 指标卡29 + 优劣对照卡31 + 图片卡22 + 结尾总结区37 | 参数对照表28、进度条30、资源引导条36 |
| 数据复盘/报告 | 封面刊头2 + 引题式标题9 + 指标卡29 + 数据表格27 + 进度条30 + 结尾总结区37 | 时间线21、大引文页15（金句收束） |
| 访谈/人物特稿 | 封面刊头2 + 编者按4 + 章节编号标题7 + 时间线21 + 大引文页15 + 作者信息卡34 | 短引用条16、首字下沉12 |
| 知识整理/方法论 | 封面刊头2 + 分栏索引卡6 + 章节编号标题7 + 列表组32 + FAQ 33 + 结尾总结区37 | 信息卡17（INFO）、编辑旁注18 |

所有类型共用固定结构：封面刊头2 + 固定签名段落(组件11) + 末尾互动区38 + 页脚版权条40 + 隐藏标记。

---

## Markdown → 墨蓝刊读 映射规则

| Markdown 元素 | 对应组件 | 说明 |
|---|---|---|
| `# 标题` | 封面刊头2 主标题 | 平台标题另设，刊头标题从中提炼；副标题取导语首句 |
| 文章开头 `> 引言` | 组件4 编者按 或 组件3 头版摘要卡 | 视引言长度与语气而定 |
| `## 章节标题` | 组件7 章节编号标题（默认） | 编号 01/02/03…，末章可用 ///；特殊板块可用组件8 栏目条（≤2处） |
| `### 子标题` | 组件10 小节标签标题（默认）/ 组件9 引题式标题（专题式） | 按语境二选一 |
| 普通段落 | 组件11 正文段落 | 每段主动标 1~3 处克莱因蓝下划线（强调 c） |
| `**加粗文字**` | 文字强调 a 强调加粗 | |
| `==高亮文字==` | 文字强调 b 浅蓝高亮 | |
| `<u>下划线</u>` / `++文字++` | 文字强调 c 克莱因蓝下划线 | 次要强调（默认标记） |
| 行内 `` `code` `` / 字段名 | 文字强调 d 行内代码标签 | 整句嵌入用组件14 |
| ` ``` 多行代码块 ``` ` | 组件25 深色代码块（默认）/ 组件26 浅色代码块 | 每行一个 `<p style="margin:0">`，缩进用全角空格 |
| `> 引用`（非开头） | 组件15 大引文页（金句，≤1处）/ 组件16 短引用条（普通引用） | 视分量选择 |
| 无序列表 | 组件32 无序列表 | |
| 有序列表 | 组件32 有序列表 | |
| 任务清单 `- [ ]` / `- [x]` | 组件32 任务清单 | |
| 表格 | 组件27 数据表格（数据对照）/ 组件28 参数对照表（字段说明） | 仅真实表格语义用 `table` |
| `![说明](图片)` | 组件22 图片卡 | 有说明才加 `<figcaption>` |
| 图片 + 长说明 | 组件24 图注说明卡 | 图注 ≥1 句时升级使用 |
| A/B 对比图 | 组件23 双图对比 | |
| `---` 分割线 | 组件39 装饰分隔符 | |
| 步骤/流程说明 | 组件19 步骤条 / 组件20 流程总览 | 教程用步骤条，架构用流程总览 |
| 时间线/阶段 | 组件21 时间线 | |
| 常见问题 | 组件33 FAQ 问答卡 | |
| 关键指标 | 组件29 指标卡 / 组件30 进度条 | |
| 优势/局限对比 | 组件31 优劣对照卡 | |
| 文末总结/结语 | 组件37 结尾总结区（默认）/ 组件15 大引文页（金句收束） | 按语气选择 |
| 资源/工具获取 | 组件36 资源引导条 | |
| 相关阅读 | 组件35 延伸阅读卡 | |
| 文末 | 组件38 末尾互动区（+ 固定签名段落）+ 组件40 页脚版权条 | 固定签名段落放互动区前 |

---

## 留白控制规则（全局强制）

> **必须遵守，否则文章整体松散、阅读体验差。**

- 段落间 margin-bottom 控制在 **14-20px**，不超过 22px（禅意风 24px 例外）
- 章节标题上方 margin-top 第一章 **16px**，后续章节 **32-48px**，不超过 48px
- 章节标题下方 margin-bottom 控制在 **16-24px**
- 组件与组件之间**不要重复叠加 margin**：如果相邻两个组件都有 margin-bottom，外层不要额外加 padding-top/margin-top
- 引言卡/金句卡上下留白控制在 **24-40px**，不超过 48px
- 结尾签名区/互动区上方留白控制在 **20-32px**
- 图片容器下方 margin-bottom **8-16px**，图注再加 margin-top: 4-8px
- 列表项之间 margin-bottom **6-10px**
- 数据卡片/要点卡片组上下 margin-bottom **16-24px**
- 分割线两侧留白 **24-32px**，不超过 40px
- **一句话原则**：宁可紧凑，不可松散。读者的眼睛需要连续的视觉流，大面积空白会打断阅读节奏

