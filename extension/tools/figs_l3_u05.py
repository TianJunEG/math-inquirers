"""Level 3 Unit 5 (Remainder riddles) figure types.

  l3_groups  n objects put into groups of k: full groups are solid boxes of k dots, the leftover is one dashed box.
             spec: n, k, cols (boxes per row), hide_left (bool: draw the leftover as dots without a box so that it must be counted)
"""
import figs as F
from figs_l3_common import T, wrap, NAVY, SOFT

FIGS = {}


def groups(spec, w=None):
    n, k, cols = spec['n'], spec['k'], spec.get('cols', 3)
    pitch = 42
    bw = k * pitch + 22
    bh = 66
    full, left = divmod(n, k)
    boxes = [k] * full + ([left] if left else [])
    P = []
    for i, c in enumerate(boxes):
        r, cc = divmod(i, cols)
        x, y = 8 + cc * (bw + 16), 8 + r * (bh + 14)
        dash = ' stroke-dasharray="9 6"' if c < k else ''
        P.append(f'<rect x="{x}" y="{y}" width="{bw}" height="{bh}" rx="12" fill="#fff" stroke="{NAVY}" stroke-width="3.4"{dash}/>')
        for j in range(c):
            P.append(f'<circle cx="{x + 22 + pitch * j + pitch / 2 - 11:.1f}" cy="{y + bh / 2}" r="14" fill="{NAVY}"/>')
    rows = (len(boxes) + cols - 1) // cols
    W = 16 + min(cols, len(boxes)) * (bw + 16)
    H = 16 + rows * (bh + 14)
    return wrap(P, W, H, f'{n} dots in groups of {k}', w)


FIGS['l3_groups'] = groups
