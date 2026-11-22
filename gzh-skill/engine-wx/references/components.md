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
<h1 style="margin:0 0 6px;font-size:16px;line-height:1.3;font-weight:700;letter-spacing:1px;color:{{text}};">{{标题}}</h1>
<p style="margin:0 0 22px;font-size:14px;color:{{muted}};letter-spacing:.5px;">{{副标题}}</p>
```

> 顶部只放文字，**不加**装饰块（黑色粗线 / 色块 / 分隔线）——用户明确要求「只要文字」时用这版。
> 需要装饰感时可在标题前加 `<section style="border-top:2px solid {{titleBar}};padding-top:14px;"></section>`，或标题下加
> `<section style="height:1px;background:{{divider}};margin:0 0 26px;"></section>` 分隔线。

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


## 正文对齐（2026-10-31 定版）

正文段落、列表项、卡片内说明文字一律 **两端对齐**：内联加 `text-align:justify;`（小标题 h1/h2、导语灰字、表头、§13c 底部上滑提示仍可居中或左对齐）。

```html
<p style="margin:0 0 16px;padding:0;font-size:15px;line-height:1.95;color:#141414;text-align:justify;">{{正文}}</p>
```

## 13. 图片 + 说明（配图默认规范，每次都照此办）

```html
<img src="{{base64或图片URL}}" style="max-width:100%;width:100%;display:block;margin:14px 0 20px;box-sizing:border-box;" alt="{{描述}}"/>
```

> **固定用法（TD 定稿，以后一律如此）：**
> 1. **内嵌位置**：图片放在正文里**与它对应的内容之后**——原帖链接后、基准数据后、宣传图对应段落后。
>    **禁止把配图统一堆到文末**。
> 2. **图下不写文字**（2026-10-30 定版，取消 12px 灰图注）：图要说明什么，写进紧邻的正文段落；
>    图与下文的间距由 `margin:14px 0 20px` 提供。
> 3. **长截图两种处理**（2026-10-31 增补）：优先切成 2–4 段高清裁图按序嵌入；若必须保留整张长图（如 Help Center / changelog 全文），改用 **§13c 可上滑长图**，不要整页撑开。
> 4. **src 一律 base64 内嵌**：`data:image/png;base64,…` 直接写进 `src`，保证成品单文件、开箱即复制。
>    本地文件路径（`file://`）无效；原稿只给了公网 URL 时也先下载转 base64 内嵌。`.gif` 同样支持。
> 5. 图片还没准备好时改用 §13b 占位框，不要留空。

## 13b. 图片占位（预留上传位置，默认排版必须留）

```html
<section style="margin:16px 0;padding:32px 16px;background:{{cardBg}};border:1px dashed #d8d8d8;border-radius:14px;text-align:center;">
  <p style="margin:0 0 6px;font-size:15px;font-weight:700;color:{{text}};letter-spacing:.5px;">图片占位</p>
  <p style="margin:0;font-size:13px;color:{{muted}};letter-spacing:.3px;">上传 {{图片来源说明}}</p>
</section>
```

> 用途：正文需要配图但图还没准备好时，先占住位置。粘进公众号后删掉占位框、插入真实图片即可。
> 虚线框用 `#d8d8d8`（中性灰，不随主题变，避免彩色虚线在浅色主题上刺眼）；文字色仍取主题 `{{text}}` / `{{muted}}`。
> **默认规则**：凡需要截图/配图的位置（如博主原帖、榜单、实测画面、主页等），**用户没给图**时一律先放此占位框，不要留空。
> **用户已给图**时直接按 §13 内嵌，不放占位框。


## 13c. 可滑动长图（2026-11-05 定版 · 对齐范文）

> 范文：https://mp.weixin.qq.com/s/pTY1Wm0eFdbWX4XbfomHBA（mdnice 长图滑动）
> 适用：整张 Help / changelog / 官帖全文 / 榜单等**过高**的图；矮图仍用 §13 直展，不要套滑动框。
> 交付前必须自测：框内能滑、底部渐隐可见、能滑到图底看完。

```html
<section style="margin:14px 0 8px;padding:18px;background:#4e54c8;background:-webkit-linear-gradient(to right,#8f94fb,#4e54c8);background:linear-gradient(to right,#8f94fb,#4e54c8);">
  <section style="height:320px;overflow-y:scroll;scrollbar-width:none;-ms-overflow-style:none;mask-image:linear-gradient(rgb(0,0,0) 88%, rgba(0,0,0,0.55) 100%);-webkit-mask-image:linear-gradient(rgb(0,0,0) 88%, rgba(0,0,0,0.55) 100%);border:1px solid #e5e5e5;border-radius:0;box-sizing:border-box;text-align:center;background:#ffffff;">
    <img src="{{base64或图片URL}}" style="max-width:100%;width:100%;display:block;margin:0 auto;border:none;border-radius:0;box-shadow:none;box-sizing:border-box;" alt="{{描述}}"/>
  </section>
  <p style="margin:8px 0 0;padding:0;font-size:12px;line-height:1.6;letter-spacing:.5px;color:#ffffff;text-align:center;">{{短说明}} · {{往下划引导}}</p>
</section>
```

> **固定用法（以后一律如此）：**
> 1. **高度用 `height:320px`**（固定高，不是 `max-height:280px`）。
> 2. **`overflow-y:scroll` + `scrollbar-width:none`**（隐藏滚动条）；可加 `-ms-overflow-style:none`。
> 3. **底部渐隐**：`mask-image` / `-webkit-mask-image: linear-gradient(rgb(0,0,0) 88%, rgba(0,0,0,0.55) 100%)`，提示下面还有内容。
> 4. **边框** `1px solid #e5e5e5`，`border-radius:0`；图本身不要再加圆角/阴影。
> 5. **说明在渐变底衬内、图框下方**：12px、白字 `#ffffff`、居中；文案用「{{短说明}} · {{往下划引导}}」（例：`Cat Wu 官宣加入 OpenAI · 官宣帖全文，往下划看她怎么夸 OpenAI`）。
> 6. **禁止**再用旧版「↑ 上滑查看完整说明 · …」灰字；禁止把引导字叠在图上。
> 7. 图 `src` 仍一律 base64 内嵌（同 §13）。
> 8. **渐变底衬（2026-11-22 用户定版）**：滑动框外包一层渐变 wrapper——`padding:18px` + `background:#4e54c8` + `background:-webkit-linear-gradient(to right,#8f94fb,#4e54c8)` + `background:linear-gradient(to right,#8f94fb,#4e54c8)`（三行按此顺序写死，前者兜底），白色滑动框与引导行都放 wrapper 内；与双语卡片渐变底衬同款。旧「无底衬 + 灰字引导」形态作废。

## 14. 数据指标（单条）

```html
<section style="background:{{cardBg}};border:1px solid {{cardBorder}};border-radius:12px;padding:20px 18px;margin:16px 0;">
  <p style="margin:0;font-size:40px;font-weight:800;line-height:1;color:{{accent}};">{{数值}}</p>
  <p style="margin:10px 0 0;font-size:14px;color:{{muted}};">{{指标名}}</p>
</section>
```

## 15. 脚注 / 关注引导

```html
<section style="margin-top:34px;padding-top:18px;">
  <p style="margin:0;font-size:13px;color:{{muted}};letter-spacing:.5px;text-align:center;">{{脚注文字}}</p>
</section>
```

## 16. 茶 · 节气与节令元素（2026-11-18 定版 · 配 `tea-almanac` / `tea-festival`）

> 颜色全部用主题占位符（颜色唯一来源 `themes/*.json`）；日期统一「月.日」两位数；农历写「腊月三十」式；
> **不写宜忌、不写吉凶**，节气是时间线索不是养生指令；候名/节俗没把握就删，不硬凑。

### 16a 节气签（节气名 + 日期 + 英文微标）

```html
<p style="margin:0 0 6px;font-size:11px;line-height:1.6;letter-spacing:3px;color:{{accent2}};">{{11.22 · LIGHT SNOW}}</p>
<h2 style="margin:0 0 10px;font-size:26px;line-height:1.3;font-weight:700;letter-spacing:2px;color:{{text}};font-family:'Songti SC','STSong','SimSun',serif;">{{小雪}}</h2>
```

> 用在节气条目顶部，替代普通条目的「月.日」小签；英文微标 = 节气名意译大写（`LIGHT SNOW` / `WINTER SOLSTICE`）。
> 用签时下面那行标题降级为「动作句」（如「围炉煮一壶老白茶」），不重复节气名。

### 16b 节日题签（节日名 + 农历日期）

```html
<h2 style="margin:0 0 4px;font-size:24px;line-height:1.3;font-weight:700;letter-spacing:2px;color:{{text}};font-family:'Songti SC','STSong','SimSun',serif;">{{除夕}}</h2>
<p style="margin:0 0 10px;font-size:12px;line-height:1.6;letter-spacing:2px;color:{{muted}};">{{农历腊月三十 · 丁未年}}</p>
```

> 用在节日条目顶部，替代「月.日」小签；农历与年份干支可只写其一，全篇统一。

### 16c 三候条（七十二候 · 三格）

```html
<table cellpadding="0" cellspacing="0" style="width:100%;border-collapse:collapse;margin:8px 0 16px;font-size:13px;line-height:1.7;border-top:2px solid {{accent}};border-bottom:1px solid {{divider}};">
  <tr>
    <td style="width:33.3%;padding:10px 8px;text-align:center;border-right:1px solid {{divider}};">
      <p style="margin:0 0 3px;font-size:11px;line-height:1.6;color:{{muted}};">初候</p>
      <p style="margin:0;font-size:14px;line-height:1.6;color:{{text}};font-family:'Songti SC','STSong','SimSun',serif;">{{蚯蚓结}}</p>
    </td>
    <td style="width:33.3%;padding:10px 8px;text-align:center;border-right:1px solid {{divider}};">
      <p style="margin:0 0 3px;font-size:11px;line-height:1.6;color:{{muted}};">二候</p>
      <p style="margin:0;font-size:14px;line-height:1.6;color:{{text}};font-family:'Songti SC','STSong','SimSun',serif;">{{麋角解}}</p>
    </td>
    <td style="width:33.3%;padding:10px 8px;text-align:center;">
      <p style="margin:0 0 3px;font-size:11px;line-height:1.6;color:{{muted}};">三候</p>
      <p style="margin:0;font-size:14px;line-height:1.6;color:{{text}};font-family:'Songti SC','STSong','SimSun',serif;">{{水泉动}}</p>
    </td>
  </tr>
</table>
```

> 加在节气条目（`tea-almanac` §16a 签）之下、场景段之上；候名以《月令七十二候集解》为准，**没把握的格子整行删掉**，不编候名。

### 16d 季签（季节一枚 + 当令一句）

```html
<p style="margin:0 0 8px;font-size:10px;line-height:1.6;letter-spacing:4px;color:{{accent}};text-transform:uppercase;">{{WINTER · 冬}}</p>
<p style="margin:0 0 16px;font-size:14px;line-height:1.75;letter-spacing:.3px;color:{{muted}};"><span style="color:{{accent}};font-weight:600;">{{冬}}</span>　{{当令说明一句，如：茶台从绿茶换到老白茶与熟普。}}</p>
```

> 四季茶单的段首用（`tea-almanac`），一季一枚；季名后那句写茶台怎么换，不写身体怎么养。

### 16e 当令茶提示条（节气/节日 + 茶，一行总览）

```html
<section style="margin:14px 0 18px;padding:10px 14px;border-top:1px solid {{cardBorder}};border-bottom:1px solid {{cardBorder}};">
  <p style="margin:0;font-size:13px;line-height:1.75;letter-spacing:.3px;color:{{text}};"><span style="color:{{accent}};font-weight:600;">{{当令}}</span>　{{小雪}} → <strong style="color:{{text}};">{{煮老白茶、饮熟普}}</strong></p>
</section>
```

> 放首段之后、第一个条目之前，给全篇一个总览；「当令」是中性时间提示，**禁止改写成「宜 / 忌」**。

## 组装口诀

- **先外框，后内容**：全文只有一个 677px 外框。
- **标题→小节→段落→特殊块** 依次排列；特殊块（引言/卡片/代码/数据）复用组件。
- 节奏：段间 18px、小节前 34px、卡片间 16px，别乱塞间距。
- 生成时把所有 `{{x}}` 换成主题色；**不要新增主题之外的色值**。
