# 微信编辑器兼容性铁律（生成前必读）

公众号「富文本编辑器」会对粘贴进来 / 合成的 HTML 做**清洗**，很多现代 CSS 会被剥掉或失效。
**这张表是本 Skill 唯一的技术准绳**——违反任何一条「禁止」，成品就可能塌版。

## 一、能稳用的（✅ 放心用）

| 能力 | 说明 |
|---|---|
| HTML 标签 | `section` `p` `span` `strong` `em` `a` `img` `table` `tr` `td` `ul` `ol` `li` `br` `h1~h6`（部分保留） |
| 内联 `style` | 标签上的 `style="..."` 基本保留，这是**唯一可靠的样式来源** |
| 基础样式 | `color` `background` / `background-color` `font-size` `font-weight` `line-height` `text-align` `text-decoration` `letter-spacing`（多数版本） `padding` `margin` `width` `height` `max-width` |
| `border` | 含 `border-left` `border-top` 等，`border-radius`（多数版本生效） |
| 表格布局 | `table` + `td` 的 `width`/`padding` 用于**并排 / 网格 / 按钮**|
| `img` | `src`（需为公网可访问 URL）、`width`、`style="width:100%"` |
| 宽度 | 内容区宽约 `677px`（桌面）；实际排版常设 `max-width:677px;margin:0 auto` |
| box-shadow | **部分**版本/机型生效，可作装饰，**切勿用来撑布局** |

## 二、会被剥掉 / 失效的（❌ 禁止依赖）

| 能力 | 后果 |
|---|---|
| `Flexbox`（`display:flex` 等） | 多数版本失效 → **改用 `table` 或 `section`+内联块** |
| `Grid`（`display:grid`） | 一律失效 → 用 table |
| `position` / `absolute` / `fixed` / `relative` | 失效 → 不要定位 |
| `z-index` | 失效 → 不要叠放 |
| `var(--x)`（CSS 变量） | `:root` 变量多数被清 → **直接把色值写进内联样式** |
| `:hover` / `:before` / `:after` / 其他伪类伪元素 | 基本失效 → 不依赖 |
| `@media` / 媒体查询 | 仅单屏，无响应式 → 按 677px 一张版 |
| `@font-face` / 外链字体 / 自定义字体 | 失效 → 用系统字体族 |
| `<style>` 里的类选择器 | `<style>` 可能保留但**类的匹配不可靠**，避免用 class 控制样式 |
| 外部 `<link>` 样式表 | 失效 → 全部内联 |
| `backdrop-filter` / `filter` / `transform` | 失效 → 避免 |
| `clip` / `mask` / 复杂渐变 | 多数失效 → 用纯色 + 边框 |

## 三、降级 / 风险提示（⚠️ 注意）

- `box-shadow`、`border-radius`、`letter-spacing`：**多版本可用**，但个别机型（尤其 iOS 部分版本）会弱化。
  可作为「锦上添花」，但**布局与可读性不要依赖它们**——即去掉它们页面照样成立。
- `white-space:pre-wrap`（代码保留换行）：多数可用，配合 `<br>` 更稳。
- 背景图：`background-image` 上传到微信编辑器的图不太稳；**关键内容用 `<img>`**，别放背景图。

## 四、会「看不见」的坑

1. **空标签**：不要留无内容也无效的空 `<section></section>`，会被编辑器吃掉。
2. **表格撑破**：`<table width="100%">` 内 `td` 的 `width` 总和 ≤ 100%，否则溢出。
3. **样式写在 `<style>` 内联不到标签**：所有样式都写进每个元素的 `style` 属性。
4. **复制时丢样式**：从编辑器复制到别的编辑器会二次清洗；让用户**直接在公众号编辑器粘贴**。

## 五、可读性硬指标

- 深色主题：`bg` 深 → 文字用浅色，正文与背景对比度 ≥ **4.5:1**；副文字/`muted` 别低于 3:1。
- 正文字号 16px、行高 1.8；深色大段文字用 15–16px 更稳。
- 强调用 `accent` 或 `accent2`，一屏别超过 2 处。

## 六、为什么这样设计

> 简约 + 科技感的本质是**节奏与对比**，不是炫技。微信的限制反而逼我们用干净的
> 字号/字距/留白/边框/纯色做出高级感——这正是本 Skill 选「细线 + 大留白 + 纯色强调」路线的原因，
> 也保证了它在任何设备上都不塌版。
