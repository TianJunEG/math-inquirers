"""Level 3 Unit 7 (Area architects) figure types.  One drawing unit square = 1 cm; the default cell is 52 drawing units (about 10 mm).

  l3_cells  figures made of unit squares.  spec: rows (list of strings: X = square, . = empty, A B C ... = dashed candidate square with that
            letter), cell (size, default 52), label (text under the figure), thick (bool, default true: heavy outline round the X squares)
  l3_poly   a polygon with straight sides on a grid of `k` drawing units per cm.  spec: pts [[x, y] ...] in cm with y up, labels [{side, text}]
            (side i joins point i and i+1; the text is written outside the side), k (default 40), label, fill (bool, default true)
"""
import figs as F
from figs_l3_common import T, wrap, esc, NAVY, SOFT, SKY, SW

FIGS = {}


def cells(spec, w=None):
    if spec.get('shapes'):          # several figures side by side, each with its own label under it
        s = spec.get('cell', 52)
        gap = spec.get('gap', 70)
        P, x0, H = [], 0, 0
        for sh in spec['shapes']:
            inner = cells(dict(spec, shapes=None, rows=sh['rows'], label=sh.get('label'), _inner=True), 1)
            body = inner.split('>', 1)[1].rsplit('</svg>', 1)[0]
            wv = float(inner.split('viewBox="0 0 ')[1].split(' ')[0]); hv = float(inner.split('viewBox="0 0 ')[1].split(' ')[1].split('"')[0])
            P.append(f'<g transform="translate({x0:.1f},0)">{body}</g>')
            x0 += wv + gap - 20
            H = max(H, hv)
        return wrap(P, x0 - gap + 20, H, 'figures made of squares', w)
    rows = spec['rows']
    s = spec.get('cell', 52)
    nr, nc = len(rows), max(len(r) for r in rows)
    P = []
    filled = {(r, c) for r, row in enumerate(rows) for c, ch in enumerate(row) if ch == 'X'}
    for r, row in enumerate(rows):
        for c, ch in enumerate(row):
            x, y = 10 + c * s, 10 + r * s
            if ch == 'X':
                P.append(f'<rect x="{x}" y="{y}" width="{s}" height="{s}" fill="{SOFT}" stroke="{NAVY}" stroke-width="2"/>')
            elif ch.isalpha() and ch != 'X':
                P.append(f'<rect x="{x}" y="{y}" width="{s}" height="{s}" fill="#fff" stroke="{NAVY}" stroke-width="3" stroke-dasharray="8 6"/>')
                P.append(T(x + s / 2, y + s / 2 + 11, ch, 32))
    if spec.get('thick', True):
        for (r, c) in filled:
            x, y = 10 + c * s, 10 + r * s
            for (dr, dc, x1, y1, x2, y2) in ((-1, 0, x, y, x + s, y), (1, 0, x, y + s, x + s, y + s), (0, -1, x, y, x, y + s), (0, 1, x + s, y, x + s, y + s)):
                if (r + dr, c + dc) not in filled:
                    P.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{NAVY}" stroke-width="6" stroke-linecap="square"/>')
    H = 20 + nr * s
    if spec.get('label'):
        P.append(T(10 + nc * s / 2, H + 32, esc(spec['label']), 30))
        H += 44
    return wrap(P, 20 + nc * s, H, 'figure made of squares', w)


def poly(spec, w=None):
    k = spec.get('k', 40)
    pts = spec['pts']
    xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
    mx, my = 120, 60
    X = lambda x: mx + (x - min(xs)) * k
    Y = lambda y: my + (max(ys) - y) * k
    path = 'M' + ' L'.join(f'{X(x):.1f},{Y(y):.1f}' for x, y in pts) + 'Z'
    P = [f'<path d="{path}" fill="{SOFT if spec.get("fill", True) else "#fff"}" stroke="{NAVY}" stroke-width="5" stroke-linejoin="miter"/>']
    for ex in spec.get('extra', []):
        ep = 'M' + ' L'.join(f'{X(x):.1f},{Y(y):.1f}' for x, y in ex['pts']) + 'Z'
        P.append(f'<path d="{ep}" fill="#fff" stroke="{NAVY}" stroke-width="4" stroke-dasharray="10 7"/>')
    for ar in spec.get('arcs', []):       # arc at a vertex: centre (x, y) in cm, radius r (cm), from angle a0 to a1 degrees anticlockwise (y up)
        import math as _m
        cx_, cy_, r_ = X(ar['x']), Y(ar['y']), ar['r'] * k
        p0 = (cx_ + r_ * _m.cos(_m.radians(ar['a0'])), cy_ - r_ * _m.sin(_m.radians(ar['a0'])))
        p1 = (cx_ + r_ * _m.cos(_m.radians(ar['a1'])), cy_ - r_ * _m.sin(_m.radians(ar['a1'])))
        large = 1 if (ar['a1'] - ar['a0']) % 360 > 180 else 0
        P.append(f'<path d="M{p0[0]:.1f},{p0[1]:.1f} A{r_:.1f},{r_:.1f} 0 {large} 0 {p1[0]:.1f},{p1[1]:.1f}" fill="none" stroke="{NAVY}" stroke-width="4"/>')
    for tx_ in spec.get('texts', []):
        P.append(T(X(tx_['x']), Y(tx_['y']) + 10, esc(tx_['text']), tx_.get('size', 28)))
    n = len(pts)
    area2 = sum(pts[i][0] * pts[(i + 1) % n][1] - pts[(i + 1) % n][0] * pts[i][1] for i in range(n))
    sgn = 1 if area2 > 0 else -1          # counter-clockwise (y up) = 1
    for lab in spec.get('labels', []):
        i = lab['side']
        (x1, y1), (x2, y2) = pts[i], pts[(i + 1) % n]
        dx, dy = x2 - x1, y2 - y1
        ln = (dx * dx + dy * dy) ** 0.5
        nx, ny = sgn * dy / ln, -sgn * dx / ln      # outward normal in y-up coordinates
        sh = lab.get('shift', 0)
        cx, cy = (x1 + x2) / 2 + sh * dx, (y1 + y2) / 2 + sh * dy
        if abs(ny) > 0.5:
            P.append(T(X(cx), Y(cy) - ny * 36 + 10, esc(lab['text']), lab.get('size', 34)))
        else:
            P.append(T(X(cx) + nx * 18, Y(cy) + 10, esc(lab['text']), lab.get('size', 34), anchor='end' if nx < 0 else 'start'))
    H = my + (max(ys) - min(ys)) * k + 60
    if spec.get('label'):
        P.append(T(mx + (max(xs) - min(xs)) * k / 2, H + 18, esc(spec['label']), 30)); H += 40
    return wrap(P, mx * 2 + (max(xs) - min(xs)) * k, H, 'figure with straight sides', w)


FIGS.update({'l3_cells': cells, 'l3_poly': poly})
