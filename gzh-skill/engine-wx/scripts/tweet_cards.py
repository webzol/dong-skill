# -*- coding: utf-8 -*-
"""双语推文卡片 / 中文还原截图 生成库（2026-11-22 定版样式，入库随 skill 走）

定版口径（AGENTS.md「英文博主发言两种样式」「中文长推截断兜底」，规格唯一出处见各规则文件）：
- 双语卡片：白底大圆角卡浮于横向渐变底上（`linear-gradient(to right,#8f94fb,#4e54c8)`，
  四边 ≈18px@1x 渐变框），真实头像+昵称+认证徽章+@handle 原样不动，上英文黑字、下中文灰字，
  重点词两边同步加粗，emoji 用 Segoe UI Emoji 彩色渲染、换行按单词边界断、底部留白 60px@1x，
  卡上不加任何水印。
- 中文还原截图：长推在 X 界面被「Show more」截断、无头工具又不能点击展开时的兜底——按真实
  头像/昵称/徽章/@handle 还原说话部分（全文不截断、无底栏无时间行），成品 1500px 2.2x 画布。
- 认证徽章绘制：individual = 蓝色锯齿圆 + 白勾；组织 = 蓝色圆 + 白色四角星。
- 引用推文块：小头像 + 昵称 + 双徽章 + @handle + 引文，1px #ececec 圆角框。

用法（import 后调 render_card，一次一张；参考 2026-11-22 Gemini 5 稿实例）：

    import sys; sys.path.insert(0, r"E:\\dong-skill\\gzh-skill\\engine-wx\\scripts")
    from tweet_cards import render_card

    render_card({
        "mode": "card",              # card=双语卡片（渐变底衬）；shot=中文还原截图（白底）
        "handle": "vedantmisra",
        "nickname": "Vedant Misra",
        "avatar": "av_vedant.jpg",   # 相对 assets_dir；pbs.twimg.com profile_images 400x400 直下
        "paragraphs": [              # ('en'|'cn', 文本, [加粗词])；en=黑字 cn=灰字（shot 模式全黑字）
            ("en", "Gemini 5", ["Gemini 5"]),
            ("cn", "引用 Logan Kilpatrick 的帖子：你这周末打算用 Gemini 4 Neon 做点什么？",
             ["Gemini 4 Neon"]),
        ],
        "quote": {                   # 可选；渲染在第一个 en 段之后
            "name": "Logan Kilpatrick", "handle": "OfficialLoganK",
            "avatar": "av_logan.jpg", "badges": ["individual", "org"],
            "text": "What are you building with Gemini 4 Neon this weekend?",
            "bolds": ["Gemini 4 Neon"],
        },
        "out": r"D:\\out\\card_vedant.png",
    }, assets_dir=r"C:\\path\\to\\assets")

头像直下：`https://pbs.twimg.com/profile_images/<id>/<file>_400x400.jpg`（普通 Chrome UA）。
"""
import math
import os
import re

from PIL import Image, ImageDraw, ImageFont

# ── 画布与字号（2.2x of 677px 栏宽）────────────────────────────
W = 1500
PAD_X = 84
TEXT_W = W - PAD_X * 2
BOTTOM_PAD = 120                       # 60px @1x

EN_SIZE, EN_LH = 33, 54
CN_SIZE, CN_LH = 31, 52
PARA_GAP = 28
EN_CN_GAP = 44

# 引用推文块
Q_IN = 40
Q_TEXT_SIZE, Q_TEXT_LH = 29, 46
Q_AV = 56
Q_NAME = 31
Q_HANDLE = 26

# ── 颜色 ──────────────────────────────────────────────────────
INK = (20, 20, 20, 255)                # 卡片英文黑字
XINK = (15, 20, 25, 255)               # X 界面正文近黑（还原截图用）
GRAY = (138, 138, 138, 255)            # 卡片中文灰字
XGRAY = (83, 100, 113, 255)            # @handle 灰
GRAYB = (95, 95, 95, 255)              # 中文加粗
BORDER = (236, 236, 236, 255)          # 1px #ececec 卡片边框
DIVID = (240, 240, 240, 255)
BLUE = (29, 155, 240, 255)             # 认证徽章蓝

# 双语卡片渐变底衬（2026-11-22 用户定版）：#8f94fb → #4e54c8 横向
GRAD_L = (143, 148, 251)
GRAD_R = (78, 84, 200)
CARD_MARGIN = 40                       # 渐变底外框宽度 @2.2x（≈18px @1x）

F_DIR = r'C:\Windows\Fonts'


def F(name, size, idx=0):
    return ImageFont.truetype(os.path.join(F_DIR, name), size, index=idx)


SEGOE = lambda s: F('segoeui.ttf', s)
SEGOEB = lambda s: F('segoeuib.ttf', s)
YAHEI = lambda s: F('msyh.ttc', s)
YAHEIB = lambda s: F('msyhbd.ttc', s)
EMOJI = lambda s: F('seguiemj.ttf', s)

EMOJI_RE = re.compile('[\U0001F000-\U0001FAFF\u2600-\u27BF\u2B00-\u2BFF\uFE0F\u200D]')
CJK_RE = re.compile('[\u4e00-\u9fff\u3000-\u303f\uff01-\uff5e\u2018\u2019\u201c\u201d\u3001\u3002\uff08\uff09]')


def is_emoji_ch(c):
    return bool(EMOJI_RE.match(c))


# ── 文本分词 / 断行 / 渲染（词边界断行，加粗词不区分大小写最长匹配）──
def tokenize(text, bold_words):
    segs = []
    low = text.lower()
    bw = sorted([w.lower() for w in bold_words], key=len, reverse=True)
    i = 0
    while i < len(text):
        hit = None
        for w in bw:
            if low.startswith(w, i):
                hit = w
                break
        if hit:
            segs.append((text[i:i + len(hit)], True))
            i += len(hit)
        else:
            j = i
            while j < len(text):
                h2 = None
                for w in bw:
                    if low.startswith(w, j):
                        h2 = w
                        break
                if h2:
                    break
                j += 1
            segs.append((text[i:j], False))
            i = j
    tokens = []
    for seg_text, seg_bold in segs:
        buf = ''

        def flush():
            nonlocal buf
            if buf:
                tokens.append((buf, seg_bold, False))
                buf = ''
        for c in seg_text:
            if is_emoji_ch(c):
                flush()
                tokens.append((c, False, True))
            elif c == '\n':
                flush()
                tokens.append(('\n', seg_bold, False))
            elif re.match(r'[A-Za-z0-9@#\'\-\.…,;:!?/()\[\]&+]+$', c):
                buf += c
            else:
                flush()
                tokens.append((c, seg_bold, False))
        flush()
    return tokens


def wrap(tokens, max_w, size, draw):
    fonts = {}

    def tok_font(t, bold, emoji):
        key = (bold, emoji, bool(CJK_RE.search(t) and not emoji))
        if key not in fonts:
            if emoji:
                fonts[key] = EMOJI(size)
            elif key[2]:
                fonts[key] = (YAHEIB if bold else YAHEI)(size)
            else:
                fonts[key] = (SEGOEB if bold else SEGOE)(size)
        return fonts[key]
    lines, cur, cur_w = [], [], 0
    for tok in tokens:
        text, bold, emoji = tok
        if text == '\n':
            lines.append(cur)
            cur, cur_w = [], 0
            continue
        w = draw.textlength(text, font=tok_font(text, bold, emoji))
        if text == ' ':
            if cur:
                cur.append(tok)
                cur_w += w
            continue
        if cur_w + w > max_w and cur:
            while cur and cur[-1][0] == ' ':
                cur_w -= draw.textlength(' ', font=tok_font(*cur[-1]))
                cur.pop()
            lines.append(cur)
            cur, cur_w = [], 0
        cur.append(tok)
        cur_w += w
    if cur:
        lines.append(cur)
    return lines


def render_tokens(d, tokens, size, lh, color, bold_color, x0, y, max_w):
    lines = wrap(tokens, max_w, size, d)
    for line in lines:
        x = x0
        for text, bold, emoji in line:
            if emoji:
                f = EMOJI(size)
                d.text((x, y), text, font=f, fill=color, embedded_color=True)
            elif CJK_RE.search(text):
                f = (YAHEIB if bold else YAHEI)(size)
                d.text((x, y), text, font=f, fill=bold_color if bold else color)
            else:
                f = (SEGOEB if bold else SEGOE)(size)
                d.text((x, y), text, font=f, fill=bold_color if bold else color)
            x += d.textlength(text, font=f)
        y += lh
    return y


def block_h(d, tokens, size, lh, max_w):
    return len(wrap(tokens, max_w, size, d)) * lh


# ── 头像 / 徽章 / 头部 ────────────────────────────────────────
def circle_avatar(path, size):
    im = Image.open(path).convert('RGB')
    side = min(im.size)
    im = im.crop(((im.width - side) // 2, (im.height - side) // 2,
                  (im.width + side) // 2, (im.height + side) // 2))
    im = im.resize((size, size), Image.LANCZOS)
    mask = Image.new('L', (size * 4, size * 4), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, size * 4 - 1, size * 4 - 1), fill=255)
    mask = mask.resize((size, size), Image.LANCZOS)
    out = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    out.paste(im, (0, 0), mask)
    return out


def badge_individual(d, cx, cy, s):
    """X 个人认证徽章：蓝色锯齿圆 + 白色对勾"""
    r = s * 0.40
    for ang in range(0, 360, 45):
        a = math.radians(ang)
        bx = cx + r * 0.72 * math.cos(a)
        by = cy + r * 0.72 * math.sin(a)
        d.ellipse((bx - r * 0.42, by - r * 0.42, bx + r * 0.42, by + r * 0.42), fill=BLUE)
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=BLUE)
    lw = max(2, int(s * 0.11))
    d.line([(cx - s * 0.17, cy + s * 0.01), (cx - s * 0.045, cy + s * 0.145)],
           fill=(255, 255, 255, 255), width=lw)
    d.line([(cx - s * 0.045, cy + s * 0.145), (cx + s * 0.185, cy - s * 0.115)],
           fill=(255, 255, 255, 255), width=lw)


def badge_org(d, cx, cy, s):
    """组织徽章：蓝色圆 + 白色四角星（AI Studio 风格）"""
    r = s * 0.42
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=BLUE)
    R, rr = s * 0.26, s * 0.065
    pts = []
    for ang in (270, 315, 0, 45, 90, 135, 180, 225):
        a = math.radians(ang)
        rad = R if ang % 90 == 0 else rr
        pts.append((cx + rad * math.cos(a), cy + rad * math.sin(a)))
    d.polygon(pts, fill=(255, 255, 255, 255))


def draw_header(d, img, avatar_path, nickname, handle, y_top=64, av_size=112,
                name_size=38, handle_size=29, x0=PAD_X, name_color=INK):
    av = circle_avatar(avatar_path, av_size)
    img.paste(av, (x0, y_top), av)
    hx = x0 + av_size + 30
    nf = YAHEIB(name_size)
    d.text((hx, y_top + 8), nickname, font=nf, fill=name_color)
    nw = d.textlength(nickname, font=nf)
    bsz = int(name_size * 0.92)
    badge_individual(d, hx + nw + 8 + bsz / 2, y_top + 8 + name_size * 0.62, bsz)
    d.text((hx, y_top + 8 + name_size + 14), '@' + handle, font=SEGOE(handle_size), fill=XGRAY)
    return y_top + max(av_size, 8 + name_size + 14 + handle_size + 10)


# ── 渐变底衬（双语卡片定版）──────────────────────────────────
def gradient_canvas(w, h):
    bg = Image.new('RGB', (w, h))
    d = ImageDraw.Draw(bg)
    for x in range(w):
        t = x / max(1, w - 1)
        c = tuple(int(GRAD_L[i] + (GRAD_R[i] - GRAD_L[i]) * t) for i in range(3))
        d.line([(x, 0), (x, h)], fill=c)
    return bg


def save_bilingual_card(img, out_path, radius=40):
    """白卡圆角浮于 #8f94fb→#4e54c8 横向渐变底上"""
    m = CARD_MARGIN
    bg = gradient_canvas(img.width + m * 2, img.height + m * 2)
    card = img.convert('RGBA')
    mask = Image.new('L', (img.width * 4, img.height * 4), 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, img.width * 4 - 1, img.height * 4 - 1),
                                           radius=radius * 4, fill=255)
    mask = mask.resize((img.width, img.height), Image.LANCZOS)
    card.putalpha(mask)
    bg.paste(card, (m, m), card)
    bg.save(out_path)
    print('saved', out_path, bg.size)


# ── 组装入口 ──────────────────────────────────────────────────
def render_card(spec, assets_dir, out_path=None):
    """按 spec 渲染一张卡片 / 还原截图。

    spec 字段见模块 docstring；mode='card' 走渐变底衬双语卡片，
    mode='shot' 走白底中文还原截图（无渐隐无底栏无时间行）。
    """
    out_path = out_path or spec['out']
    mode = spec.get('mode', 'card')
    probe = Image.new('RGB', (10, 10))
    pd = ImageDraw.Draw(probe)

    av = lambda f: os.path.join(assets_dir, f)
    header_h = max(112, 8 + 38 + 14 + 29 + 10)

    quote = spec.get('quote')
    paragraphs = spec['paragraphs']

    # 高度预算
    y = 64 + header_h + 26
    toks_list = []
    for kind, text, bolds in paragraphs:
        size, lh = (EN_SIZE, EN_LH) if kind == 'en' else (CN_SIZE, CN_LH)
        toks = tokenize(text, bolds)
        toks_list.append((kind, toks, size, lh))
        y += block_h(pd, toks, size, lh, TEXT_W) + PARA_GAP
    q_toks = q_h = None
    if quote:
        q_toks = tokenize(quote['text'], quote.get('bolds', []))
        q_name_w = pd.textlength(quote['name'], font=YAHEIB(Q_NAME))
        row_w = Q_AV + 24 + q_name_w + 8 + 34 + 8 + 34 + 12 + \
            pd.textlength('@' + quote['handle'], font=SEGOE(Q_HANDLE))
        q_text_h = block_h(pd, q_toks, Q_TEXT_SIZE, Q_TEXT_LH, TEXT_W - Q_IN * 2)
        q_h = 36 + max(Q_AV, 34 + 12) + 18 + q_text_h + 36
        first_en = next((i for i, (k, _, _, _) in enumerate(toks_list) if k == 'en'), 0)
        toks_list.insert(first_en + 1, ('quote', None, None, None))
        y += q_h + 26
    H = int(y + BOTTOM_PAD)

    img = Image.new('RGB', (W, H), (255, 255, 255))
    d = ImageDraw.Draw(img)
    if mode == 'card':
        d.rounded_rectangle((1, 1, W - 2, H - 2), radius=40, outline=BORDER, width=2)

    yy = draw_header(d, img, av(spec['avatar']), spec['nickname'], spec['handle'],
                     name_color=INK if mode == 'card' else XINK)
    if mode == 'shot':
        d.line((PAD_X, yy + 8, W - PAD_X, yy + 8), fill=DIVID, width=2)
    yy += 26

    prev_kind = None
    for kind, toks, size, lh in toks_list:
        if kind == 'quote':
            qy = yy
            d.rounded_rectangle((PAD_X, qy, W - PAD_X, qy + q_h), radius=24,
                                outline=BORDER, width=2)
            qav = circle_avatar(av(quote['avatar']), Q_AV)
            img.paste(qav, (PAD_X + Q_IN, qy + 36), qav)
            nx = PAD_X + Q_IN + Q_AV + 24
            ny = qy + 36 + (Q_AV - Q_NAME) // 2 - 6
            d.text((nx, ny), quote['name'], font=YAHEIB(Q_NAME), fill=INK)
            q_name_w = d.textlength(quote['name'], font=YAHEIB(Q_NAME))
            b1 = 34
            badges = quote.get('badges', ['individual', 'org'])
            bx = nx + q_name_w + 8
            for b in badges:
                (badge_individual if b == 'individual' else badge_org)(
                    d, bx + b1 / 2, ny + Q_NAME * 0.62, b1)
                bx += b1 + 8
            d.text((bx + 4, ny + 3), '@' + quote['handle'], font=SEGOE(Q_HANDLE), fill=XGRAY)
            ty = qy + 36 + max(Q_AV, 34 + 12) + 18
            render_tokens(d, q_toks, Q_TEXT_SIZE, Q_TEXT_LH, INK, INK,
                          PAD_X + Q_IN, ty, TEXT_W - Q_IN * 2)
            yy = qy + q_h + 26
            prev_kind = 'en'
            continue
        if mode == 'shot':
            color, bold_color = XINK, XINK
        elif kind == 'en':
            color, bold_color = INK, INK
        else:
            color, bold_color = GRAY, GRAYB
            if prev_kind == 'en':
                yy += EN_CN_GAP - PARA_GAP
        yy = render_tokens(d, toks, size, lh, color, bold_color, PAD_X, yy, TEXT_W)
        yy += PARA_GAP
        prev_kind = kind

    if mode == 'card':
        save_bilingual_card(img, out_path)
    else:
        img.save(out_path)
        print('saved', out_path, img.size)
    return out_path
