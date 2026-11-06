# 模板：tea-notes（茶志 · 茶知识）

> **定位**：分类、工艺、风味、冲泡与存茶知识。围绕一个具体问题选用解释、对照表、操作步骤和参数卡。
> **写作前读**：`../references/tea-knowledge.md`；下列块按题材取舍，不强制写四种味道。
> **风格**：工具文，但保持纸感。少量表格，一个参数卡，其余交给句子。
> **搭配**：`tea-atelier` 主题（白底 + 墨黑 `#1c1a17` + 古铜 `#8a6a3f` + 青灰 `#5f7358`）。

## 骨架

### 外框

```html
<section style="max-width:677px;margin:0 auto;background:{{bg}};padding:28px 20px 48px;box-sizing:border-box;font-family:'PingFang SC',-apple-system,'Helvetica Neue','Microsoft YaHei',sans-serif;color:{{text}};">
```

> 正文不放 h1、不放灰字导语、文末不加页脚、不放来源列表。

### 栏目签

```html
<p style="margin:0 0 18px;font-size:10px;line-height:1.6;letter-spacing:4px;color:{{accent}};text-transform:uppercase;">风味 · TEA NOTES</p>
```

### 首段（直接进入问题）

```html
<p style="margin:0 0 18px;font-size:15px;line-height:1.95;letter-spacing:.5px;color:{{text}};text-align:justify;">{{第一段：一个具体困惑或可观察现象；有证据时再纠正误解。}}</p>
```

### 知识小节（编号 + 关键词 + 钩子标题）

```html
<p style="margin:38px 0 0;font-size:10px;line-height:1.6;letter-spacing:2.6px;color:{{accent2}};text-transform:uppercase;">01 · {{UMAMI}}</p>
<h2 style="margin:4px 0 16px;font-size:17px;line-height:1.6;font-weight:700;letter-spacing:.6px;color:{{text}};font-family:'Songti SC','STSong','SimSun',serif;">{{这一口，差在哪}}</h2>
```

> 每节回答一个问题：现象 → 经核验的解释 → 可尝试的动作及边界；物质机制需有来源，不把示例当结论。

### 变量表（三列：变量 / 调高会怎样 / 调低会怎样）

```html
<p style="margin:26px 0 0;font-size:11px;line-height:1.6;letter-spacing:4px;color:{{accent}};font-family:'Songti SC','STSong','SimSun',serif;text-align:center;">· 变量与滋味 ·</p>
<table cellpadding="0" cellspacing="0" style="width:100%;border-collapse:collapse;margin:10px 0 12px;font-size:13px;line-height:1.75;border-top:2px solid {{accent}};">
  <tr>
    <th style="padding:10px 14px;text-align:left;font-weight:600;font-family:'Songti SC','STSong','SimSun',serif;letter-spacing:2px;color:{{accent}};background:{{codeBg}};border-bottom:1px solid {{cardBorder}};">变量</th>
    <th style="padding:10px 14px;text-align:left;font-weight:600;font-family:'Songti SC','STSong','SimSun',serif;letter-spacing:2px;color:{{accent}};background:{{codeBg}};border-bottom:1px solid {{cardBorder}};">调高</th>
    <th style="padding:10px 14px;text-align:left;font-weight:600;font-family:'Songti SC','STSong','SimSun',serif;letter-spacing:2px;color:{{accent}};background:{{codeBg}};border-bottom:1px solid {{cardBorder}};">调低</th>
  </tr>
  <tr>
    <td style="padding:12px 14px;font-family:'Songti SC','STSong','SimSun',serif;font-weight:600;color:{{text}};border-bottom:1px solid {{divider}};">水温</td>
    <td style="padding:12px 14px;color:{{text}};border-bottom:1px solid {{divider}};">{{调高后的变化及适用条件}}</td>
    <td style="padding:12px 14px;color:{{text}};border-bottom:1px solid {{divider}};">{{调低后的变化及适用条件}}</td>
  </tr>
</table>
```

> 带表头色块的对照表：表上方加**题签**（宋体 `{{accent}}` 居中，11px、字距 4px、「· 四字名 ·」），表顶部一条 `2px solid {{accent}}` 书衣线；表头宋体 + `{{accent}}` + 字距 2px，单元格四向 padding（横向 ≥14px），文字不贴边，首列宋体加重；表头 `{{codeBg}}`，正文白底；三列刚好，不要加第四列。

### 调整清单（单变量试泡，用编号不用卡片）

```html
<p style="margin:24px 0 10px;font-size:15px;line-height:1.95;color:{{text}};text-align:justify;"><span style="color:{{accent}};font-weight:600;">01</span>　{{记录茶样、器具和当前冲泡参数}}</p>
<p style="margin:0 0 10px;font-size:15px;line-height:1.95;color:{{text}};text-align:justify;"><span style="color:{{accent}};font-weight:600;">02</span>　{{针对问题选择一个变量调整，其余保持一致}}</p>
<p style="margin:0 0 18px;font-size:15px;line-height:1.95;color:{{text}};text-align:justify;"><span style="color:{{accent}};font-weight:600;">03</span>　{{比较口感并记录，再决定下一轮调整}}</p>
```

> 不设通用的降温、减茶、缩时顺序；每轮只改变一个变量，调整幅度按具体茶样与依据填写。

### 参数卡（三行，无填充）

```html
<table cellpadding="0" cellspacing="0" style="width:100%;border-collapse:collapse;margin:22px 0 8px;font-size:13px;line-height:1.75;">
  <tr>
    <td style="padding:10px 14px;width:30%;font-family:'Songti SC','STSong','SimSun',serif;color:{{muted}};border-bottom:1px solid {{divider}};">水温</td>
    <td style="padding:10px 14px;color:{{text}};border-bottom:1px solid {{divider}};">{{建议水温区间与测量口径}}</td>
  </tr>
  <tr>
    <td style="padding:10px 14px;width:30%;font-family:'Songti SC','STSong','SimSun',serif;color:{{muted}};border-bottom:1px solid {{divider}};">投茶比</td>
    <td style="padding:10px 14px;color:{{text}};border-bottom:1px solid {{divider}};">{{投茶量 g / 实际注水量 mL，注明质量与体积比例}}</td>
  </tr>
  <tr>
    <td style="padding:10px 14px;width:30%;font-family:'Songti SC','STSong','SimSun',serif;color:{{muted}};">出汤</td>
    <td style="padding:10px 14px;color:{{text}};">{{建议时间区间，注明泡次及计时起止}}</td>
  </tr>
</table>
<p style="margin:0 0 22px;font-size:12px;line-height:1.7;letter-spacing:.4px;color:{{muted}};">{{适用茶样、泡法与器具；数据依据和调整条件。}}</p>
```

> 无表头参数表同样四向留白：纵向 10px、横向 14px，文字不贴边；标签列宋体、维持 `{{muted}}`，不加重。
### 图片位

```html
<img src="{{IMG_A}}" style="max-width:100%;width:100%;display:block;margin:14px 0 20px;box-sizing:border-box;" alt="{{描述}}"/>
```

### 收尾

```html
<p style="margin:0;font-size:15px;line-height:1.95;letter-spacing:.5px;color:{{text}};text-align:justify;">{{最后一句：一个可以立刻试的动作，写完就结束。}}</p>
```

## 节奏

- 知识小节之间 **38px**；按文章需要选用对照表、调整清单和参数卡，分类或存茶稿不必硬塞冲泡参数。
- 全篇表格 **不超过 2 个**，中间必须有段落和图片隔开。
- 冲泡建议给有依据的起始区间和适用条件；引用值与实测值保持原值，单位及比例需校对。
- 篇幅 **900–1400 汉字**；不写保健功效，不写「越陈越香」这类绝对判断。

## 适配

- 与 `tea-atelier` 主题配套。
- 适合：四种味道、苦涩来源、水温与时间、投茶比、降苦顺序、冷泡参数。
- 不适合：茶史（改 `tea-culture`）、器物选购（改 `tea-ware`）。
