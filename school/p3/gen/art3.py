"""Primary 3 pictures (original art, black and white). Every picture has a reader that recovers its values from the DRAWING only."""
import math, re
from .common import svg
from .art2 import DISC_R

# ---------------------------------------------------------------------------------------------------- place-value discs with thousands
def disc4(kind, cx, cy):
    lab = {"th": "1000", "h": "100", "t": "10", "o": "1"}[kind]
    fs = {"th": 3.0, "h": 3.7, "t": 4.3, "o": 5.2}[kind]
    sw = {"th": 1.3, "h": 0.9, "t": 0.6, "o": 0.6}[kind]
    return (f'<g class="disc {kind}"><circle cx="{cx:.2f}" cy="{cy:.2f}" r="{DISC_R}" fill="#fff" stroke="#000" stroke-width="{sw}"/>'
            f'<text x="{cx:.2f}" y="{cy+0.1:.2f}" text-anchor="middle" dominant-baseline="central" font-family="Nunito Sans" font-weight="800" font-size="{fs}" fill="#000">{lab}</text></g>')

def pv4_chart(th, h, t, o, per_row=2):
    """four columns (Thousands, Hundreds, Tens, Ones) of discs, `per_row` discs in a row"""
    colw = per_row * 10.4 + 2.5; gap = 2.0; head = 6.5
    rows = max(math.ceil(n / per_row) for n in (th, h, t, o)) or 1
    H = head + rows * 10.4 + 1.5; W = 4 * colw + 3 * gap
    p = []
    for ci, (name, kind, n) in enumerate((("Thousands", "th", th), ("Hundreds", "h", h), ("Tens", "t", t), ("Ones", "o", o))):
        x0 = ci * (colw + gap)
        p.append(f'<rect x="{x0:.2f}" y="0.3" width="{colw:.2f}" height="{H-0.6:.2f}" rx="1.2" fill="#fff" stroke="#000" stroke-width="0.5"/>'
                 f'<text x="{x0+colw/2:.2f}" y="3.6" text-anchor="middle" dominant-baseline="central" font-family="Nunito Sans" font-weight="800" font-size="3.4" fill="#000">{name}</text>'
                 f'<line x1="{x0:.2f}" y1="{head-0.8}" x2="{x0+colw:.2f}" y2="{head-0.8}" stroke="#000" stroke-width="0.4"/>')
        for i in range(n):
            p.append(disc4(kind, x0 + 1.2 + DISC_R + 0.4 + (i % per_row) * 10.4, head + 0.6 + DISC_R + (i // per_row) * 10.4))
    return svg(round(W, 1), round(H, 1), "".join(p))

def read_pv4(s):
    return tuple(len(re.findall(r'class="disc %s"' % k, s)) for k in ("th", "h", "t", "o"))

# ---------------------------------------------------------------------------------------------------- fraction figures (copied from the P2 pages)
from .common import svg
def frac_fig(kind, n, shaded, rng):
    """a figure cut into n EQUAL parts with the parts in `shaded` black (white separators inside black areas); kind: bar, circle, grid (rows x cols)"""
    def part(tag, geom, i):
        sh = i in shaded
        return f'<{tag} class="part{" sh" if sh else ""}" {geom} fill="{"#000" if sh else "#fff"}" stroke="{"none" if sh else "#000"}" stroke-width="0.6" stroke-linejoin="round"/>'
    def gap(tag, geom, i):
        return f'<{tag} class="ol" {geom} fill="none" stroke="#fff" stroke-width="1.1" stroke-linejoin="round"/>' if i in shaded else ""
    items = []; outline = ""
    if kind == "bar":
        w = 48.0; h = 13.0; u = w / n
        for i in range(n): items.append((i, part("rect", f'x="{1+i*u:.2f}" y="1" width="{u:.2f}" height="{h}"', i), gap("rect", f'x="{1+i*u:.2f}" y="1" width="{u:.2f}" height="{h}"', i)))
        outline = f'<rect x="1" y="1" width="{w}" height="{h}" fill="none" stroke="#000" stroke-width="0.8"/>'; W, H = w + 2, h + 2
    elif kind == "circle":
        r = 12.5; cx = cy = r + 1
        for i in range(n):
            a0 = -math.pi / 2 + 2 * math.pi * i / n; a1 = -math.pi / 2 + 2 * math.pi * (i + 1) / n
            x0, y0 = cx + r * math.cos(a0), cy + r * math.sin(a0); x1, y1 = cx + r * math.cos(a1), cy + r * math.sin(a1)
            items.append((i, part("path", f'd="M{cx},{cy} L{x0:.2f},{y0:.2f} A{r},{r} 0 0 1 {x1:.2f},{y1:.2f} Z"', i), gap("path", f'd="M{cx},{cy} L{x0:.2f},{y0:.2f} A{r},{r} 0 0 1 {x1:.2f},{y1:.2f} Z"', i)))
        outline = f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="#000" stroke-width="0.8"/>'; W = H = 2 * r + 2
    else:
        rows, cols = {4: (2, 2), 6: (2, 3), 8: (2, 4), 9: (3, 3), 10: (2, 5), 12: (3, 4)}[n]
        u = 9.5
        for i in range(n):
            rr, cc = divmod(i, cols)
            items.append((i, part("rect", f'x="{1+cc*u:.2f}" y="{1+rr*u:.2f}" width="{u}" height="{u}"', i), gap("rect", f'x="{1+cc*u:.2f}" y="{1+rr*u:.2f}" width="{u}" height="{u}"', i)))
        outline = f'<rect x="1" y="1" width="{cols*u}" height="{rows*u}" fill="none" stroke="#000" stroke-width="0.8"/>'; W, H = cols * u + 2, rows * u + 2
    # black fills first, then a white line (1.1 mm wide, centred on each shaded part's edge), then the white parts with black outlines, then the outer outline
    ordered = [x[1] for x in items if x[0] in shaded] + [x[2] for x in items] + [x[1] for x in items if x[0] not in shaded]
    return svg(round(W, 1), round(H, 1), "".join(ordered) + outline)

def read_frac(s):
    parts = re.findall(r'class="part( sh)?"', s)
    return len(re.findall(r'class="part sh"', s)), len(parts)


