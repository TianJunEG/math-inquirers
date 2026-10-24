"""Figure types for Level 2 unit 4 (patterns).

  l2_pattern  a row (or rows) of shapes or letters in numbered boxes.  items: shape names (star, circle, square, triangle, diamond, heart),
              single capital letters, or None (an empty dashed box).  Options: numbers (default true: the place number under each box),
              per_row (default 10), sep (draw a heavier line after every `sep` boxes to show groups).
  l2_sticks   sticks (matches) forming a chain of squares (kind sq) or triangles (kind tri); counts: [1, 2, 3] draws one chain per count with a label.
Shapes differ by outline, never by colour (print edition is black and white).
"""
import figs as F
from figs_l2_core import T, box, line, wrap, NAVY, SKY, SOFT, YEL


def _shape(kind, cx, cy, r):
    if kind == 'circle':
        return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{YEL}" stroke="{NAVY}" stroke-width="3.2"/>'
    if kind == 'square':
        return f'<rect x="{cx - r * 0.9}" y="{cy - r * 0.9}" width="{r * 1.8}" height="{r * 1.8}" fill="#fff" stroke="{NAVY}" stroke-width="3.4"/>'
    if kind == 'triangle':
        return f'<path d="M{cx} {cy - r * 1.05} L{cx + r * 1.1} {cy + r * 0.85} L{cx - r * 1.1} {cy + r * 0.85}Z" fill="{SKY}" stroke="{NAVY}" stroke-width="3.4" stroke-linejoin="round"/>'
    if kind == 'diamond':
        return f'<path d="M{cx} {cy - r * 1.15} L{cx + r * 0.85} {cy} L{cx} {cy + r * 1.15} L{cx - r * 0.85} {cy}Z" fill="{SKY}" stroke="{NAVY}" stroke-width="3.2" stroke-linejoin="round"/>'
    if kind == 'star':
        import math
        pts = []
        for k in range(10):
            ang = -math.pi / 2 + k * math.pi / 5
            rr = r * 1.2 if k % 2 == 0 else r * 0.5
            pts.append(f'{cx + rr * math.cos(ang):.1f},{cy + rr * math.sin(ang):.1f}')
        return f'<polygon points="{" ".join(pts)}" fill="{SOFT}" stroke="{NAVY}" stroke-width="3.2" stroke-linejoin="round"/>'
    if kind == 'heart':
        return (f'<path d="M{cx} {cy + r * 1.0} C{cx - r * 1.7} {cy - r * 0.2} {cx - r * 0.7} {cy - r * 1.3} {cx} {cy - r * 0.4} '
                f'C{cx + r * 0.7} {cy - r * 1.3} {cx + r * 1.7} {cy - r * 0.2} {cx} {cy + r * 1.0}Z" fill="{SKY}" stroke="{NAVY}" stroke-width="3.2" stroke-linejoin="round"/>')
    raise ValueError(kind)


def pattern(spec, w=None):
    items = spec['items']
    per = spec.get('per_row', 10)
    cs = 74
    numbers = spec.get('numbers', True)
    sep = spec.get('sep')
    rows = [items[i:i + per] for i in range(0, len(items), per)]
    rh = cs + (34 if numbers else 0) + 10
    P = []
    for ri, row in enumerate(rows):
        for ci, it in enumerate(row):
            idx = ri * per + ci
            x, y = 6 + ci * cs, 6 + ri * rh
            if it is None:
                P.append(box(x, y, cs, cs, '#fff', dash=True, sw=3, rx=6))
            else:
                P.append(box(x, y, cs, cs, '#fff', sw=3, rx=6))
                if len(it) == 1 and it.isupper():
                    P.append(T(x + cs / 2, y + cs / 2 + 15, it, 48))
                else:
                    P.append(_shape(it, x + cs / 2, y + cs / 2, 20))
            if numbers:
                P.append(T(x + cs / 2, y + cs + 26, idx + 1, 26, weight=600))
            if sep and (idx + 1) % sep == 0 and idx + 1 < len(items) and ci < len(row) - 1:
                P.append(line(x + cs, y - 2, x + cs, y + cs + 2, 6, col=NAVY))
    W = 12 + max(len(r) for r in rows) * cs
    H = 12 + len(rows) * rh
    return wrap(P, W, H, 'pattern of shapes', w, 0.2)


def sticks(spec, w=None):
    kind = spec['kind']
    L = 80
    P = []
    x0 = 56
    H = L + 56
    for n in spec['counts']:
        if kind == 'sq':
            segs = []
            for i in range(n + 1):
                segs.append((i * L, 0, i * L, L))
            for i in range(n):
                segs.append((i * L, 0, (i + 1) * L, 0))
                segs.append((i * L, L, (i + 1) * L, L))
            width = n * L
        else:
            h = L * 0.87
            pts = [((i * L / 2), (h if i % 2 == 0 else 0)) for i in range(n + 2)]
            segs = [(pts[i][0], pts[i][1], pts[i + 1][0], pts[i + 1][1]) for i in range(n + 1)] + [(pts[i][0], pts[i][1], pts[i + 2][0], pts[i + 2][1]) for i in range(n)]
            width = (n + 1) * L / 2
        top = 16
        for (a, b, c, d) in segs:
            P.append(f'<line x1="{x0 + a}" y1="{top + b}" x2="{x0 + c}" y2="{top + d}" stroke="{NAVY}" stroke-width="9" stroke-linecap="round"/>')
            P.append(f'<line x1="{x0 + a}" y1="{top + b}" x2="{x0 + c}" y2="{top + d}" stroke="{SOFT}" stroke-width="4" stroke-linecap="round"/>')
        word = ('square' if kind == 'sq' else 'triangle') + ('' if n == 1 else 's')
        P.append(T(x0 + width / 2, top + L + 40, f'{n} {word}', 28, weight=700))
        x0 += width + 100
    return wrap(P, x0 - 44, H + 30, 'sticks in a chain', w, 0.2)


FIGS = {'l2_pattern': pattern, 'l2_sticks': sticks}
