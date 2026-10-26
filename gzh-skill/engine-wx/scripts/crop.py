#!/usr/bin/env python3
"""裁图 / 缩放，用于把浏览器截图裁成公众号配图。

用法：
    python crop.py in.png out.png 60 55 640 1120
    python crop.py in.png out.png 60 55 640 1120 --resize 640
    python crop.py in.png out.png 60 55 640 1120 --jpeg

参数是像素坐标：left top right bottom（不含 right/bottom）。
"""
import sys
from PIL import Image


def main():
    if len(sys.argv) < 7:
        print(__doc__)
        sys.exit(1)
    src, dst = sys.argv[1], sys.argv[2]
    l, t, r, b = (int(x) for x in sys.argv[3:7])
    resize = None
    as_jpeg = '--jpeg' in sys.argv
    if '--resize' in sys.argv:
        resize = int(sys.argv[sys.argv.index('--resize') + 1])

    im = Image.open(src).convert('RGB')
    w, h = im.size
    box = (max(0, l), max(0, t), min(w, r), min(h, b))
    if box[2] - box[0] < 10 or box[3] - box[1] < 10:
        print(f'bad crop box {box} for image {w}x{h}')
        sys.exit(2)

    out = im.crop(box)
    if resize and out.width > resize:
        out = out.resize((resize, round(out.height * resize / out.width)), Image.LANCZOS)
    if as_jpeg:
        out.save(dst, quality=92, optimize=True)
    else:
        out.save(dst, optimize=True)
    print(f'OK {dst} {out.width}x{out.height}')


if __name__ == '__main__':
    main()
