"""Draws the small pictures used by the look-back box and the pictograph rows (no unicode shape glyphs):
gap_box.png (empty tick box), gap_face_1..3.png (happy, so-so, hard), and dots_<n>_<hex>.png rows of circles.
Usage: python3 gapkit.py            -> icons
       python3 gapkit.py dots N HEX [SIZE] -> hp/dots_N_HEX.png (used by common.js for the Word workbook)"""
import sys, os
from PIL import Image, ImageDraw
H = os.path.dirname(os.path.abspath(__file__)); NAVY = (27, 42, 73)
def box(path=None, s=72):
    im = Image.new('RGBA', (s, s), (255, 255, 255, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle((6, 6, s - 6, s - 6), 12, outline=NAVY, width=6, fill=(255, 255, 255, 255)); im.save(path or os.path.join(H, 'gap_box.png'))
def face(k, s=72):
    im = Image.new('RGBA', (s, s), (255, 255, 255, 0)); d = ImageDraw.Draw(im)
    fill = {1: (255, 201, 60), 2: (186, 220, 245), 3: (245, 170, 150)}[k]
    d.ellipse((4, 4, s - 4, s - 4), fill=fill, outline=NAVY, width=5)
    d.ellipse((22, 24, 29, 33), fill=NAVY); d.ellipse((43, 24, 50, 33), fill=NAVY)
    if k == 1: d.arc((20, 28, 52, 56), 20, 160, fill=NAVY, width=5)
    elif k == 2: d.line((24, 50, 48, 50), fill=NAVY, width=5)
    else: d.arc((20, 44, 52, 70), 200, 340, fill=NAVY, width=5)
    im.save(os.path.join(H, f'gap_face_{k}.png'))
def dots(n, hexc, size=40):
    r = size // 2; gapx = 6; grp = 14
    W = n * (size + gapx) + (n // 5) * grp + 4; im = Image.new('RGBA', (W * 2, size * 2 + 4), (255, 255, 255, 0)); d = ImageDraw.Draw(im)
    col = tuple(int(hexc[i:i + 2], 16) for i in (0, 2, 4)); x = 2
    for i in range(n):
        d.ellipse((x * 2, 2, (x + size) * 2, size * 2 + 2), fill=col); x += size + gapx
        if (i + 1) % 5 == 0: x += grp
    p = os.path.join(H, f'dots_{n}_{hexc}.png'); im.save(p); return p
def ruler(path=None):
    # Lesson 9 Q6: a ruler 0 to 12 cm with a pencil (0 to 12) and a crayon (3 to 8) drawn above it
    from PIL import ImageFont
    W, Hh = 1200, 260; im = Image.new('RGBA', (W, Hh), (255, 255, 255, 0)); d = ImageDraw.Draw(im)
    x0, step = 50, 91
    try: f = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 26); fs = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 22)
    except Exception: f = fs = ImageFont.load_default()
    # pencil bar
    d.rectangle((x0, 20, x0 + 12 * step, 60), fill=(255, 201, 60), outline=NAVY, width=4); d.polygon([(x0 + 12 * step, 20), (x0 + 12 * step + 0, 60), (x0 + 12 * step, 40)], fill=NAVY)
    d.text((x0 + 14, 26), 'pencil', fill=NAVY, font=fs)
    d.rectangle((x0 + 3 * step, 80, x0 + 8 * step, 120), fill=(245, 170, 150), outline=NAVY, width=4); d.text((x0 + 3 * step + 14, 86), 'crayon', fill=NAVY, font=fs)
    # ruler
    d.rectangle((x0 - 20, 150, x0 + 12 * step + 20, 250), fill=(255, 244, 209), outline=NAVY, width=4)
    for i in range(13):
        x = x0 + i * step; d.line((x, 150, x, 185), fill=NAVY, width=4); t = str(i); w = d.textlength(t, font=f); d.text((x - w / 2, 195), t, fill=NAVY, font=f)
    d.line((x0 + 3 * step, 120, x0 + 3 * step, 150), fill=NAVY, width=2); d.line((x0 + 8 * step, 120, x0 + 8 * step, 150), fill=NAVY, width=2)
    im.save(path or os.path.join(H, 'ruler_q6.png'))
if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'ruler': ruler(); sys.exit()
    if len(sys.argv) > 1 and sys.argv[1] == 'dots': print(dots(int(sys.argv[2]), sys.argv[3], int(sys.argv[4]) if len(sys.argv) > 4 else 40))
    else:
        box(); [face(k) for k in (1, 2, 3)]
