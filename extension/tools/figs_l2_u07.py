"""Figure types for Level 2 unit 7 (fractions).

  l2_frac   a row (wrapping) of fraction pictures.  items: list of dicts {kind, label?, ...}
     bar     n equal parts in a rectangle (or `widths` = relative widths for unequal parts); `shaded` is a count (first parts) or a list of 0-based indexes;
             `marks` {index: letter} prints a letter in a part; `w` drawn width (default 360)
     circle  n equal sectors (or `angles` list in degrees for unequal sectors); `shaded` as above
     sq      a square cut by `style`: strips (n equal strips), cross (2 x 2), diag (4 triangles from the corners), unequal (strips with relative `widths`),
             halves (2 strips), thirds; `shaded` list of part indexes
     line    a number line from 0 to 1 cut into n equal steps; `arrows` [{k, label}] point at k/n
     wall    fraction wall: `rows` list of n values (each row is a bar cut into n parts, all the same length); `shaded` {n: index}; every row is labelled 1/n at the left
Shaded parts use the YEL fill (hatching in the print edition); nothing depends on colour.
"""
import math
import figs as F
from figs_l2_core import T, box, line, wrap, NAVY, SKY, SOFT, YEL


def _is_sh(shaded, i):
    if isinstance(shaded, int):
        return i < shaded
    return i in (shaded or [])


def _bar(it, x, y):
    w = it.get('w', 360)
    h = it.get('h', 70)
    n = it.get('n')
    widths = it.get('widths')
    if widths:
        tot = sum(widths)
        ws = [a / tot * w for a in widths]
    else:
        ws = [w / n] * n
    P = []
    xx = x
    for i, pw in enumerate(ws):
        sh = _is_sh(it.get('shaded'), i)
        P.append(f'<rect x="{xx:.1f}" y="{y}" width="{pw:.1f}" height="{h}" fill="{YEL if sh else "#fff"}" stroke="{NAVY}" stroke-width="3.2"/>')
        marks = {int(k): v for k, v in (it.get('marks') or {}).items()}
        if i in marks:
            P.append(T(xx + pw / 2, y + h / 2 + 12, marks[i], 34))
        xx += pw
    return P, w, h


def _circle(it, x, y):
    r = it.get('r', 74)
    cx, cy = x + r, y + r
    n = it.get('n')
    angles = it.get('angles') or [360 / n] * n
    P = []
    a0 = -90.0
    for i, a in enumerate(angles):
        a1 = a0 + a
        sh = _is_sh(it.get('shaded'), i)
        x0, y0 = cx + r * math.cos(math.radians(a0)), cy + r * math.sin(math.radians(a0))
        x1, y1 = cx + r * math.cos(math.radians(a1)), cy + r * math.sin(math.radians(a1))
        large = 1 if a > 180 else 0
        if len(angles) == 1:
            P.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{YEL if sh else "#fff"}" stroke="{NAVY}" stroke-width="3.2"/>')
        else:
            P.append(f'<path d="M{cx} {cy} L{x0:.1f} {y0:.1f} A{r} {r} 0 {large} 1 {x1:.1f} {y1:.1f}Z" fill="{YEL if sh else "#fff"}" stroke="{NAVY}" stroke-width="3.2" stroke-linejoin="round"/>')
        a0 = a1
    return P, 2 * r, 2 * r


def _sq(it, x, y):
    s = it.get('s', 140)
    st = it['style']
    sh = it.get('shaded')
    fill = lambda i: YEL if _is_sh(sh, i) else '#fff'
    P = []
    if st in ('strips', 'unequal', 'halves'):
        n = it.get('n', 2 if st == 'halves' else 4)
        widths = it.get('widths') or [1] * n
        tot = sum(widths)
        xx = x
        for i, wv in enumerate(widths):
            pw = wv / tot * s
            P.append(f'<rect x="{xx:.1f}" y="{y}" width="{pw:.1f}" height="{s}" fill="{fill(i)}" stroke="{NAVY}" stroke-width="3.2"/>')
            xx += pw
    elif st == 'cross':
        for i in range(4):
            r, c = divmod(i, 2)
            P.append(f'<rect x="{x + c * s / 2}" y="{y + r * s / 2}" width="{s / 2}" height="{s / 2}" fill="{fill(i)}" stroke="{NAVY}" stroke-width="3.2"/>')
    elif st == 'diag':
        c = (x + s / 2, y + s / 2)
        corners = [(x, y), (x + s, y), (x + s, y + s), (x, y + s)]
        # parts: top, right, bottom, left
        for i in range(4):
            a, b = corners[i], corners[(i + 1) % 4]
            P.append(f'<path d="M{a[0]} {a[1]} L{b[0]} {b[1]} L{c[0]} {c[1]}Z" fill="{fill(i)}" stroke="{NAVY}" stroke-width="3.2" stroke-linejoin="round"/>')
    return P, s, s


def _line(it, x, y):
    n = it['n']
    w = it.get('w', 600)
    x += 24
    P = [line(x, y + 50, x + w, y + 50, 3.4)]
    for k in range(n + 1):
        xx = x + k * w / n
        big = k in (0, n)
        P.append(line(xx, y + 50 - (22 if big else 14), xx, y + 50 + (22 if big else 14), 3.4 if big else 2.6))
    P.append(T(x, y + 110, '0', 34))
    P.append(T(x + w, y + 110, '1', 34))
    for a in it.get('arrows', []):
        xx = x + a['k'] / n * w
        P.append(f'<path d="M{xx} {y + 44} L{xx - 14} {y + 8} L{xx + 14} {y + 8} Z" fill="{NAVY}"/>')
        P.append(T(xx, y - 6, a['label'], 34))
    return P, w + 48, 120


def _wall(it, x, y):
    w = it.get('w', 540)
    rh = it.get('rh', 56)
    LW = 84
    P = []
    for ri, n in enumerate(it['rows']):
        yy = y + ri * (rh + 8)
        P.append(T(x + LW - 12, yy + rh / 2 + 11, '1' if n == 1 else f'1/{n}', 28, anchor='end'))
        for i in range(n):
            shd = {int(k): v for k, v in (it.get('shaded') or {}).items()}
            sh = shd.get(n) == i
            P.append(f'<rect x="{x + LW + i * w / n:.1f}" y="{yy}" width="{w / n:.1f}" height="{rh}" fill="{YEL if sh else "#fff"}" stroke="{NAVY}" stroke-width="3"/>')
    return P, LW + w, len(it['rows']) * (rh + 8)


KIND = {'bar': _bar, 'circle': _circle, 'sq': _sq, 'line': _line, 'wall': _wall}


def frac(spec, w=None):
    maxw = spec.get('max_w', 720)
    gap = 44
    P = []
    x = y = 6
    rowh = 0
    totw = 0
    for it in spec['items']:
        # measure first by drawing at the origin
        pcs, iw, ih = KIND[it['kind']](it, 0, 0)
        if x > 6 and x + iw > maxw:
            x = 6
            y += rowh + gap
            rowh = 0
        pcs, iw, ih = KIND[it['kind']](it, x, y + (34 if it.get('arrows') else 0))
        P += pcs
        lab_h = 0
        if it.get('label'):
            P.append(T(x + iw / 2, y + ih + 46 + (34 if it.get('arrows') else 0), it['label'], 32))
            lab_h = 56
        x += iw + gap
        rowh = max(rowh, ih + lab_h + (34 if it.get('arrows') else 0))
        totw = max(totw, x - gap + 6)
    H = y + rowh + 10
    return wrap(P, totw, H, 'fraction pictures', w, 0.2)


FIGS = {'l2_frac': frac}
