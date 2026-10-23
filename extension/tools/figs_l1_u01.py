"""Extra figure for Level 1 unit 1: sticker_boxes.
  sticker_boxes   a row of numbered boxes; `counts` gives the stickers (small outlined stars) in each box, None = empty dashed box for the child
Palette NAVY / TEAL only, white fills: the print edition needs no recolouring.  Nothing depends on colour.
"""
import math
import figs as F

NAVY, TEAL = F.NAVY, F.TEAL


def _star(cx, cy, r):
    pts = []
    for k in range(10):
        a = -math.pi / 2 + k * math.pi / 5
        rr = r if k % 2 == 0 else r * 0.45
        pts.append(f'{cx + rr * math.cos(a):.1f},{cy + rr * math.sin(a):.1f}')
    return f'<polygon points="{" ".join(pts)}" fill="#fff" stroke="{NAVY}" stroke-width="3" stroke-linejoin="round"/>'


def sticker_boxes(spec, w=None):
    counts = spec['counts']
    bw, gap, cols, pitch = 112, 14, 3, 34
    rows = max(3, spec.get('rows', 3))
    bh = 36 + rows * pitch + 6
    P = []
    for i, n in enumerate(counts):
        x0 = 4 + i * (bw + gap)
        dash = ' stroke-dasharray="9 6"' if n is None else ''
        P.append(f'<rect x="{x0}" y="30" width="{bw}" height="{bh}" rx="10" fill="#fff" stroke="{NAVY}" stroke-width="3"{dash}/>')
        P.append(F._t(x0 + bw / 2, 22, f'Box {i + 1}', 24, NAVY, 'middle', 800))
        for k in range(n or 0):
            r, c = divmod(k, cols)
            P.append(_star(x0 + 22 + c * 34 + (bw - 22 * 2 - 2 * 34) / 2, 30 + 30 + r * pitch, 14))
    W = len(counts) * (bw + gap) + 4
    return F._wrap(''.join(P), W, bh + 38, 'boxes of stickers', w or 160)


FIGS = {'sticker_boxes': sticker_boxes}
