# 公众号排版组件库 —— 科技橙（Tech Orange）

> **使用说明**：本组件库为「科技橙」主题，所有组件使用**内联样式**，可直接复制粘贴到微信公众号编辑器。
>
> **设计风格**：明亮现代科技感 + 橙色高亮强调 + 渐变背景卡片 + 干净利落数据展示。橙色系点缀配合浅灰/白底，适合科技、AI、产品发布类文章。
>
> **公众号平台限制须知**：
> - ❌ 不支持 `<style>` 标签、`<script>` 标签、CSS class
> - ❌ 不支持 `position: fixed/absolute`、`float`
> - ❌ 不支持 `@media` 媒体查询、`@keyframes` 动画
> - ❌ 不支持 `display: grid`
> - ✅ 支持内联 `style` 属性
> - ✅ 支持 `display: flex`（有限支持）
> - ✅ 支持 `linear-gradient`
> - ✅ 支持 `border-radius`、`box-shadow`
> - ✅ 支持 `<section>`、`<p>`、`<span>`、`<strong>`、`<img>` 等基础标签

---

## 设计变量速查表

```
主色调（科技橙）：    #FF6B35（点缀/强调/按钮专用）
辅助橙色：            #FF8C42（渐变过渡/次要强调）
标题色：              #1A1A2E（深蓝黑，现代感）
正文色：              #333333（深灰）
辅助文字色：          #999999（小字/说明/来源）
背景色：              #FFFFFF（纯白）
卡片背景：            #F8F9FA（浅灰卡片底）
渐变起点：            #FFF5F0（极浅橙）
渐变终点：            #FFFFFF（白）
标签底色：            #FFF0E8（浅橙底）
标签文字色：          #CC5522（深橙）
下划线标记色：        #FF6B35（橙色关键词下划线）
数据高亮色：          #FF6B35（大数字/关键指标）

正文字号：            15px
行高：                1.8
字间距：              0.3px
段落间距：            18px
章节上下留白：        32-40px
内容区边距：          0 16px

标题字体：            -apple-system, BlinkMacSystemFont, 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', sans-serif
正文字体：            -apple-system, BlinkMacSystemFont, 'PingFang SC', 'Hiragino Sans GB', 'Microsoft YaHei', sans-serif
```

---

## 组件 1 全局容器

```html
<section style="max-width:677px;margin:0 auto;background:#ffffff;font-family:-apple-system,BlinkMacSystemFont,'PingFang SC','Hiragino Sans GB','Microsoft YaHei',sans-serif;color:#333333;line-height:1.8;letter-spacing:0.3px;overflow-x:hidden;">
  <!-- 所有内容放在此 section 内 -->
</section>
```

---

## 组件 2 头部标题区 —— 渐变背景+橙色强调

```html
<section style="padding:32px 16px 24px;background:linear-gradient(180deg,#FFF5F0 0%,#FFFFFF 100%);text-align:center;">
  <p style="font-size:11px;color:#FF6B35;letter-spacing:4px;margin:0 0 12px;font-weight:600;text-transform:uppercase;"><span leaf="">AI · DEEP DIVE</span></p>
  <h1 style="font-size:20px;font-weight:800;color:#1A1A2E;margin:0 0 12px;line-height:1.5;letter-spacing:-0.3px;"><span leaf="">文章大标题放在这里</span></h1>
  <p style="font-size:13px;color:#999999;margin:0;line-height:1.6;"><span leaf="">副标题或一句话摘要放在这里</span></p>
</section>
```

---

## 组件 3 头部标题区 —— 纯白简洁版

```html
<section style="padding:28px 16px 20px;text-align:center;">
  <p style="font-size:11px;color:#FF6B35;letter-spacing:3px;margin:0 0 8px;font-weight:600;"><span leaf="">SECTION TAG</span></p>
  <h1 style="font-size:19px;font-weight:800;color:#1A1A2E;margin:0 0 10px;line-height:1.5;"><span leaf="">文章大标题放在这里</span></h1>
  <p style="font-size:13px;color:#999999;margin:0;"><span leaf="">作者名 · 日期</span></p>
</section>
```

---

## 组件 4 正文段落

```html
<section style="padding:0 16px 18px;">
  <p style="margin:0;font-size:15px;color:#333333;line-height:1.8;text-align:justify;"><span leaf="">正文内容放在这里，保持简洁清晰。科技橙风格适合用橙色下划线标记关键词。</span></p>
</section>
```

---

## 组件 5 橙色高亮文字（关键词标记）

```html
<span style="color:#FF6B35;font-weight:700;"><span leaf="">橙色高亮关键词</span></span>
```

---

## 组件 6 橙色下划线标记

```html
<span style="text-decoration:underline;text-decoration-color:#FF6B35;text-underline-offset:3px;"><span leaf="">带橙色下划线的关键词</span></span>
```

---

## 组件 7 章节标题 —— 橙色竖线+大字

```html
<section style="padding:0 16px 16px;">
  <section style="display:flex;align-items:center;gap:12px;margin-bottom:16px;">
    <span style="width:4px;height:28px;background:linear-gradient(180deg,#FF6B35,#FF8C42);border-radius:2px;flex-shrink:0;"></span>
    <h2 style="font-size:17px;font-weight:700;color:#1A1A2E;margin:0;line-height:1.5;"><span leaf="">章节标题放在这里</span></h2>
  </section>
</section>
```

---

## 组件 8 章节标题 —— 橙色背景标签版

```html
<section style="padding:0 16px 16px;">
  <p style="margin:0 0 12px;"><span style="display:inline-block;background:#FF6B35;color:#ffffff;font-size:12px;font-weight:700;padding:4px 14px;border-radius:3px;letter-spacing:1px;"><span leaf="">01</span></span></p>
  <h2 style="font-size:17px;font-weight:700;color:#1A1A2E;margin:0;line-height:1.5;"><span leaf="">章节标题放在这里</span></h2>
</section>
```

---

## 组件 9 章节标题 —— 渐变背景卡片版

```html
<section style="padding:0 16px 16px;">
  <section style="background:linear-gradient(135deg,#FFF5F0 0%,#FFFFFF 100%);border-radius:8px;padding:16px 18px;border-left:4px solid #FF6B35;">
    <h2 style="font-size:17px;font-weight:700;color:#1A1A2E;margin:0 0 6px;line-height:1.5;"><span leaf="">章节标题放在这里</span></h2>
    <p style="font-size:12px;color:#999999;margin:0;"><span leaf="">可选的章节副标题或描述</span></p>
  </section>
</section>
```

---

## 组件 10 数据卡片 —— 橙色强调版

```html
<section style="padding:0 16px 16px;">
  <section style="background:#F8F9FA;border-radius:10px;padding:20px 18px;text-align:center;">
    <p style="font-size:36px;font-weight:900;color:#FF6B35;margin:0 0 6px;line-height:1;"><span leaf="">71.0</span></p>
    <p style="font-size:13px;color:#666666;margin:0;"><span leaf="">关键数据指标说明</span></p>
  </section>
</section>
```

---

## 组件 11 数据卡片组 —— 两列并排

```html
<section style="padding:0 16px 16px;">
  <section style="display:flex;gap:12px;">
    <section style="flex:1;background:#F8F9FA;border-radius:10px;padding:18px 14px;text-align:center;">
      <p style="font-size:28px;font-weight:900;color:#FF6B35;margin:0 0 4px;line-height:1;"><span leaf="">$0.20</span></p>
      <p style="font-size:12px;color:#999999;margin:0;"><span leaf="">每小时成本</span></p>
    </section>
    <section style="flex:1;background:#F8F9FA;border-radius:10px;padding:18px 14px;text-align:center;">
      <p style="font-size:28px;font-weight:900;color:#FF6B35;margin:0 0 4px;line-height:1;"><span leaf="">$0.84</span></p>
      <p style="font-size:12px;color:#999999;margin:0;"><span leaf="">对比竞品</span></p>
    </section>
  </section>
</section>
```

---

## 组件 12 引言卡 —— 橙色左边框

```html
<section style="padding:0 16px 18px;">
  <section style="border-left:3px solid #FF6B35;padding:14px 16px;background:#FFF8F5;border-radius:0 6px 6px 0;">
    <p style="margin:0;font-size:14px;color:#555555;line-height:1.8;font-style:italic;"><span leaf="">引用内容放在这里，可以是名人名言、官方声明或重要提示。</span></p>
  </section>
</section>
```

---

## 组件 13 引言卡 —— 渐变背景大字版

```html
<section style="padding:24px 16px;">
  <section style="background:linear-gradient(135deg,#FFF5F0 0%,#FFFFFF 100%);border-radius:10px;padding:24px 20px;text-align:center;">
    <p style="font-size:18px;font-weight:700;color:#1A1A2E;margin:0;line-height:1.6;"><span leaf="">「一句话金句或核心观点放在这里」</span></p>
  </section>
</section>
```

---

## 组件 14 引用块 —— 社交媒体风格

```html
<section style="padding:0 16px 18px;">
  <section style="background:#F8F9FA;border-radius:10px;padding:16px 18px;">
    <section style="display:flex;align-items:center;gap:10px;margin-bottom:10px;">
      <span style="width:36px;height:36px;background:#FF6B35;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#ffffff;font-size:14px;font-weight:700;flex-shrink:0;"><span leaf="">@</span></span>
      <section>
        <p style="font-size:14px;font-weight:700;color:#1A1A2E;margin:0;"><span leaf="">用户名</span></p>
        <p style="font-size:11px;color:#999999;margin:0;"><span leaf="">@handle · 来源平台</span></p>
      </section>
    </section>
    <p style="margin:0;font-size:14px;color:#333333;line-height:1.7;"><span leaf="">引用的社交媒体内容放在这里。</span></p>
  </section>
</section>
```

---

## 组件 15 列表 —— 橙色圆点

```html
<section style="padding:0 16px 18px;">
  <section style="margin:0;padding-left:0;">
    <section style="display:flex;align-items:flex-start;gap:10px;margin-bottom:10px;">
      <span style="width:6px;height:6px;background:#FF6B35;border-radius:50%;flex-shrink:0;margin-top:8px;"></span>
      <p style="margin:0;font-size:15px;color:#333333;line-height:1.8;"><span leaf="">列表项内容放在这里。</span></p>
    </section>
    <section style="display:flex;align-items:flex-start;gap:10px;margin-bottom:10px;">
      <span style="width:6px;height:6px;background:#FF6B35;border-radius:50%;flex-shrink:0;margin-top:8px;"></span>
      <p style="margin:0;font-size:15px;color:#333333;line-height:1.8;"><span leaf="">第二个列表项内容。</span></p>
    </section>
  </section>
</section>
```

---

## 组件 16 列表 —— 编号版

```html
<section style="padding:0 16px 18px;">
  <section style="margin:0;padding-left:0;">
    <section style="display:flex;align-items:flex-start;gap:10px;margin-bottom:10px;">
      <span style="min-width:22px;height:22px;background:#FF6B35;color:#ffffff;font-size:11px;font-weight:700;border-radius:4px;display:flex;align-items:center;justify-content:center;flex-shrink:0;margin-top:2px;"><span leaf="">1</span></span>
      <p style="margin:0;font-size:15px;color:#333333;line-height:1.8;"><span leaf="">第一个要点内容。</span></p>
    </section>
    <section style="display:flex;align-items:flex-start;gap:10px;margin-bottom:10px;">
      <span style="min-width:22px;height:22px;background:#FF6B35;color:#ffffff;font-size:11px;font-weight:700;border-radius:4px;display:flex;align-items:center;justify-content:center;flex-shrink:0;margin-top:2px;"><span leaf="">2</span></span>
      <p style="margin:0;font-size:15px;color:#333333;line-height:1.8;"><span leaf="">第二个要点内容。</span></p>
    </section>
  </section>
</section>
```

---

## 组件 17 要点卡片组 —— 橙色标题版

```html
<section style="padding:0 16px 18px;">
  <section style="background:#F8F9FA;border-radius:8px;padding:16px 18px;margin-bottom:12px;">
    <p style="font-size:14px;font-weight:700;color:#FF6B35;margin:0 0 6px;"><span leaf="">要点标题一</span></p>
    <p style="font-size:14px;color:#555555;margin:0;line-height:1.7;"><span leaf="">要点内容解释，简明扼要。</span></p>
  </section>
  <section style="background:#F8F9FA;border-radius:8px;padding:16px 18px;">
    <p style="font-size:14px;font-weight:700;color:#FF6B35;margin:0 0 6px;"><span leaf="">要点标题二</span></p>
    <p style="font-size:14px;color:#555555;margin:0;line-height:1.7;"><span leaf="">要点内容解释。</span></p>
  </section>
</section>
```

---

## 组件 18 高亮文本框 —— 渐变背景

```html
<section style="padding:0 16px 18px;">
  <section style="background:linear-gradient(135deg,#FFF5F0 0%,#FFFFFF 100%);border-radius:8px;padding:16px 18px;">
    <p style="margin:0;font-size:14px;color:#333333;line-height:1.8;"><span leaf="">重点内容或特别提示放在这里，用渐变背景突出显示。</span></p>
  </section>
</section>
```

---

## 组件 19 关键数字 —— 大号橙色

```html
<section style="padding:0 16px 18px;text-align:center;">
  <p style="font-size:48px;font-weight:900;color:#FF6B35;margin:0 0 4px;line-height:1;"><span leaf="">26%</span></p>
  <p style="font-size:13px;color:#999999;margin:0;"><span leaf="">数字说明文字</span></p>
</section>
```

---

## 组件 20 对比卡片 —— 双栏

```html
<section style="padding:0 16px 18px;">
  <section style="display:flex;gap:12px;">
    <section style="flex:1;background:#F8F9FA;border-radius:8px;padding:16px;text-align:center;">
      <p style="font-size:11px;color:#999999;margin:0 0 6px;text-transform:uppercase;letter-spacing:1px;"><span leaf="">BEFORE</span></p>
      <p style="font-size:22px;font-weight:800;color:#1A1A2E;margin:0;"><span leaf="">旧数据</span></p>
    </section>
    <section style="flex:1;background:#FFF5F0;border-radius:8px;padding:16px;text-align:center;">
      <p style="font-size:11px;color:#FF6B35;margin:0 0 6px;text-transform:uppercase;letter-spacing:1px;"><span leaf="">AFTER</span></p>
      <p style="font-size:22px;font-weight:800;color:#FF6B35;margin:0;"><span leaf="">新数据</span></p>
    </section>
  </section>
</section>
```

---

## 组件 21 图片+图注

```html
<section style="padding:0 16px 18px;">
  <img src="图片URL" style="width:100%;border-radius:8px;display:block;" />
  <p style="font-size:12px;color:#999999;margin:8px 0 0;text-align:center;"><span leaf="">图片说明文字</span></p>
</section>
```

---

## 组件 22 分割线

```html
<section style="padding:0 16px;"><section style="height:1px;background:#F0F0F0;margin:0;"></section></section>
```

---

## 组件 23 标签组

```html
<section style="padding:0 16px 18px;">
  <section style="display:flex;flex-wrap:wrap;gap:8px;">
    <span style="display:inline-block;background:#FFF0E8;color:#CC5522;font-size:12px;padding:4px 12px;border-radius:20px;font-weight:600;"><span leaf="">标签一</span></span>
    <span style="display:inline-block;background:#F8F9FA;color:#666666;font-size:12px;padding:4px 12px;border-radius:20px;"><span leaf="">标签二</span></span>
    <span style="display:inline-block;background:#F8F9FA;color:#666666;font-size:12px;padding:4px 12px;border-radius:20px;"><span leaf="">标签三</span></span>
  </section>
</section>
```

---

## 组件 24 进度/流程条

```html
<section style="padding:0 16px 18px;">
  <section style="display:flex;align-items:center;gap:8px;">
    <section style="flex:1;height:4px;background:#FF6B35;border-radius:2px;"></section>
    <section style="flex:1;height:4px;background:#FF6B35;border-radius:2px;"></section>
    <section style="flex:1;height:4px;background:#FF6B35;border-radius:2px;"></section>
    <section style="flex:1;height:4px;background:#F0F0F0;border-radius:2px;"></section>
  </section>
</section>
```

---

## 组件 25 强调框 —— 橙色边框

```html
<section style="padding:0 16px 18px;">
  <section style="border:1px solid #FF6B35;border-radius:8px;padding:16px 18px;background:#FFFAF7;">
    <p style="margin:0;font-size:14px;color:#333333;line-height:1.8;"><span leaf="">特别强调的内容放在这里，橙色边框+浅橙底色突出。</span></p>
  </section>
</section>
```

---

## 组件 26 时间轴 —— 左侧橙色线

```html
<section style="padding:0 16px 18px;">
  <section style="border-left:2px solid #FF6B35;padding-left:20px;margin-left:8px;">
    <section style="margin-bottom:18px;">
      <p style="font-size:12px;color:#FF6B35;font-weight:700;margin:0 0 4px;"><span leaf="">时间点</span></p>
      <p style="font-size:14px;color:#333333;margin:0;line-height:1.7;"><span leaf="">事件描述。</span></p>
    </section>
    <section style="margin-bottom:18px;">
      <p style="font-size:12px;color:#FF6B35;font-weight:700;margin:0 0 4px;"><span leaf="">时间点</span></p>
      <p style="font-size:14px;color:#333333;margin:0;line-height:1.7;"><span leaf="">事件描述。</span></p>
    </section>
  </section>
</section>
```

---

## 组件 27 底部互动区

```html
<section style="padding:24px 16px;text-align:center;">
  <section style="height:1px;background:#F0F0F0;margin:0 0 24px;"></section>
  <p style="font-size:14px;color:#999999;margin:0 0 8px;"><span leaf="">觉得有用？点个「在看」分享给更多人</span></p>
  <p style="font-size:12px;color:#cccccc;margin:0;"><span leaf="">转发是最好的支持 🙏</span></p>
</section>
```

---

## 组件 28 作者签名区

```html
<section style="padding:20px 16px;">
  <section style="height:1px;background:#F0F0F0;margin:0 0 20px;"></section>
  <section style="display:flex;align-items:center;gap:12px;">
    <span style="width:40px;height:40px;background:#FF6B35;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#ffffff;font-size:16px;font-weight:700;flex-shrink:0;"><span leaf="">A</span></span>
    <section>
      <p style="font-size:14px;font-weight:700;color:#1A1A2E;margin:0;"><span leaf="">作者名</span></p>
      <p style="font-size:12px;color:#999999;margin:2px 0 0;"><span leaf="">公众号名称 · 写于 2026年X月X日</span></p>
    </section>
  </section>
</section>
```

---

## 组件 29 大段引用 —— 居中金句

```html
<section style="padding:24px 16px;text-align:center;">
  <p style="font-size:20px;font-weight:700;color:#1A1A2E;margin:0 0 8px;line-height:1.6;"><span leaf="">「金句内容放在这里」</span></p>
  <p style="font-size:13px;color:#999999;margin:0;"><span leaf="">—— 出处</span></p>
</section>
```

---

## 组件 30 结尾分割+总结

```html
<section style="padding:0 16px 18px;">
  <section style="height:1px;background:linear-gradient(90deg,transparent,#FF6B35,transparent);margin:0 0 18px;"></section>
  <p style="margin:0;font-size:15px;color:#333333;line-height:1.8;text-align:center;"><span leaf="">总结内容放在这里。</span></p>
</section>
```

---

## 留白控制规则（全局强制）

> **必须遵守，否则文章整体松散、阅读体验差。**

- 段落间 `margin-bottom` 控制在 **14-20px**，不超过 22px
- 章节标题上方 `margin-top` 第一章 **16px**，后续章节 **32-48px**，不超过 48px
- 章节标题下方 `margin-bottom` 控制在 **16-24px**
- 组件与组件之间**不要重复叠加 margin**：如果相邻两个组件都有 `margin-bottom`，外层不要额外加 `padding-top`/`margin-top`
- 引言卡/金句卡上下留白控制在 **24-40px**，不超过 48px
- 结尾签名区/互动区上方留白控制在 **20-32px**
- 图片容器下方 `margin-bottom` **8-16px**，图注再加 `margin-top: 4-8px`
- 列表项之间 `margin-bottom` **6-10px**
- 数据卡片/要点卡片组上下 `margin-bottom` **16-24px**
- 分割线两侧留白 **24-32px**，不超过 40px
- **一句话原则**：宁可紧凑，不可松散
