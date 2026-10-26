#!/usr/bin/env python3
"""探测截图里的内容块边界，用来确定 crop.py 的 T / B（上下）坐标。

用法：
    python bands.py shot.png                 # 默认扫 x 60..760
    python bands.py shot.png 80 770          # 指定扫描列范围
    python bands.py shot.png 80 770 --min-h 20 --thresh 245

输出形如：
    935  1205   270   内容块
    1448 2524   1076  内容块
分别是：起始行、结束行、高度、标记。
直接拿第一列当 crop.py 的 top，第二列当 bottom。

原理：把图转灰度，逐行统计扫描范围内有多少像素"比阈值暗"；
连续若干行都暗 → 一个内容块；连续纯白 → 块间空隙。
页面改版、拉长、换宽度后先跑它，比反复试坐标快。
"""
import sys

try:
    from PIL import Image
except ImportError:
    print('需要 Pillow: pip install pillow')
    sys.exit(1)


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    path = sys.argv[1]
    rest = [a for a in sys.argv[2:] if not a.startswith('--')]
    x0 = int(rest[0]) if len(rest) > 0 else 60
    x1 = int(rest[1]) if len(rest) > 1 else 760
    min_h = 6
    thresh = 250
    if '--min-h' in sys.argv:
        min_h = int(sys.argv[sys.argv.index('--min-h') + 1])
    if '--thresh' in sys.argv:
        thresh = int(sys.argv[sys.argv.index('--thresh') + 1])

    im = Image.open(path).convert('L')
    w, h = im.size
    px = im.load()
    x1 = min(x1, w)

    blocks = []
    start = None
    for y in range(h):
        dark = 0
        for x in range(max(0, x0), x1, 4):
            if px[x, y] < thresh:
                dark += 1
        if dark and start is None:
            start = y
        elif not dark and start is not None:
            if y - start >= min_h:
                blocks.append((start, y))
            start = None
    if start is not None and h - start >= min_h:
        blocks.append((start, h))

    print(f'{path}  {w}x{h}   scan x={x0}..{x1}  thresh={thresh}')
    for s, e in blocks:
        print(f'  top={s:5d}  bottom={e:5d}  h={e - s:5d}')


if __name__ == '__main__':
    main()
