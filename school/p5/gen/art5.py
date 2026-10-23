"""Primary 5 figures (pure black and white SVG). Every figure prints its numbers as <text> elements carrying data-* attributes, so the independent
solver of each page reads the PRINTED drawing (labels, marks, face counts), not the generator's variables.
Lengths are millimetres of the page. Strokes at least 0.5 mm."""
import math
from .common import svg

SW = 0.5
def T(x, y, s, anchor="middle", size=3.9, weight=600, attrs=""):
    return f'<text x="{x:.2f}" y="{y:.2f}" text-anchor="{anchor}" dominant-baseline="central" font-family="Fredoka" font-weight="{weight}" font-size="{size}" fill="#000" {attrs}>{s}</text>'

def LN(x1, y1, x2, y2, sw=SW, dash=None, attrs=""):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" stroke="#000" stroke-width="{sw}" stroke-linecap="round"{d} {attrs}/>'

def PG(pts, fill="#fff", sw=SW, attrs=""):
    return f'<polygon points="{" ".join(f"{x:.2f},{y:.2f}" for x, y in pts)}" fill="{fill}" stroke="#000" stroke-width="{sw}" stroke-linejoin="round" {attrs}/>'

def ARC(cx, cy, r, a0, a1, sw=SW):
    """arc from angle a0 to a1 (degrees, counter-clockwise on the page: y up), drawn in svg coordinates (y down)"""
    x0, y0 = cx + r * math.cos(math.radians(a0)), cy - r * math.sin(math.radians(a0))
    x1, y1 = cx + r * math.cos(math.radians(a1)), cy - r * math.sin(math.radians(a1))
    large = 1 if (a1 - a0) % 360 > 180 else 0
    return f'<path d="M{x0:.2f},{y0:.2f} A{r:.2f},{r:.2f} 0 {large} 0 {x1:.2f},{y1:.2f}" fill="none" stroke="#000" stroke-width="{sw}"/>'

def RA(x, y, ux, uy, vx, vy, s=2.6):
    """right-angle mark at (x, y) between unit vectors u and v"""
    p = [(x + ux * s, y + uy * s), (x + (ux + vx) * s, y + (uy + vy) * s), (x + vx * s, y + vy * s)]
    return f'<polyline points="{" ".join(f"{a:.2f},{b:.2f}" for a, b in p)}" fill="none" stroke="#000" stroke-width="{SW}" class="ra"/>'

# =============================================================================== triangles with a base and a height
def tri_base_height(b, h, foot=0.5, side=None, w=62, hh=40, name=None, pts_named=False):
    """triangle with base b cm and height h cm (labelled), the height drawn dashed with a right-angle mark; foot in [0,1] is where the height meets the base
    (outside [0,1] the base is extended with a dotted line). `side` is a distractor length printed on one slanted side."""
    sc = min((w - 14) / max(b + max(0, -foot * b) + max(0, (foot - 1) * b), 1e-6) * 1.0, (hh - 12) / h)
    sc = min(sc, 4.2)
    bw, hgt = b * sc, h * sc
    left = 7 + max(0, -foot * bw)
    x0, y0 = left, hh - 8
    A = (x0 + foot * bw, y0 - hgt); B = (x0, y0); C = (x0 + bw, y0)
    o = [PG([A, B, C], attrs='class="tri"')]
    fx = A[0]
    if foot < 0: o.append(LN(fx, y0, x0, y0, dash="1.2 1.2"))
    if foot > 1: o.append(LN(C[0], y0, fx, y0, dash="1.2 1.2"))
    o.append(LN(fx, A[1], fx, y0, dash="1.8 1.2", attrs='data-r="hline"'))
    o.append(RA(fx, y0, -1 if foot > 0.5 else 1, 0, 0, -1))
    o.append(T((B[0] + C[0]) / 2, y0 + 3.6, f"{b} cm", attrs='data-r="base"'))
    o.append(T(fx + (2.0 if foot <= 0.5 else -2.0), (A[1] + y0) / 2, f"{h} cm", anchor="start" if foot <= 0.5 else "end", attrs='data-r="height"'))
    if side is not None:
        if foot > 0.15: o.append(T((A[0] + B[0]) / 2 - 1.5, (A[1] + B[1]) / 2 - 1, f"{side} cm", anchor="end", attrs='data-r="side"'))
        else: o.append(T((A[0] + C[0]) / 2 + 1.5, (A[1] + C[1]) / 2 - 1, f"{side} cm", anchor="start", attrs='data-r="side"'))
    return svg(w, hh, "".join(o), cls="fsvg", extra='data-fig="tri"')

def read_tri(h):
    """independent reader: (base, height, side or None) from the printed labels"""
    import re
    g = lambda r: (lambda m: int(m.group(1)) if m else None)(re.search(rf'data-r="{r}"[^>]*>(\d+) cm<', h))
    return g("base"), g("height"), g("side")

# triangle ABC with a named base and named feet (for "which line is the height?")
def tri_named(P, base, apex, D, E, w=66, hh=46):
    """P: dict of point names -> (x, y) in mm already placed; draws triangle A B C, the points D, E on the base line (E slanted), and the dashed height from `apex` to D"""
    raise NotImplementedError

# =============================================================================== composite figures
def composite(kind, wd, ln, th, w=70, hh=48):
    """house: rectangle wd x ln with a triangle (base wd, height th) on top; notch: rectangle wd x ln with a triangular notch (base wd, depth th) cut from the top;
    side: rectangle wd x ln with a right-angled triangle (one side ln, width th) joined on the right."""
    tot_w = wd + (th if kind == "side" else 0)
    tot_h = ln + (th if kind == "house" else 0)
    sc = min((w - 16) / tot_w, (hh - 12) / tot_h, 4.0)
    x0, y0 = 8, hh - 6
    W, L_, Th = wd * sc, ln * sc, th * sc
    o = []
    if kind == "house":
        o.append(PG([(x0, y0), (x0 + W, y0), (x0 + W, y0 - L_), (x0 + W / 2, y0 - L_ - Th), (x0, y0 - L_)]))
        o.append(LN(x0, y0 - L_, x0 + W, y0 - L_, dash="1.4 1.2"))
        o.append(LN(x0 + W / 2, y0 - L_ - Th, x0 + W / 2, y0 - L_, dash="1.8 1.2"))
        o.append(T(x0 + W / 2 + 1.5, y0 - L_ - Th / 2, f"{th} cm", anchor="start", attrs='data-r="th"'))
    elif kind == "notch":
        o.append(PG([(x0, y0), (x0 + W, y0), (x0 + W, y0 - L_), (x0 + W / 2, y0 - L_ + Th), (x0, y0 - L_)]))
        o.append(LN(x0, y0 - L_, x0 + W, y0 - L_, dash="1.4 1.2"))
        o.append(LN(x0 + W / 2, y0 - L_ + Th, x0 + W / 2, y0 - L_, dash="1.8 1.2"))
        o.append(T(x0 + W / 2 + 1.5, y0 - L_ + Th / 2 - 1.0, f"{th} cm", anchor="start", attrs='data-r="th"'))
    else:
        o.append(PG([(x0, y0), (x0 + W, y0), (x0 + W + Th, y0), (x0 + W, y0 - L_), (x0, y0 - L_)]))
        o.append(LN(x0 + W, y0, x0 + W, y0 - L_, dash="1.4 1.2"))
        o.append(T(x0 + W + Th / 2 + 0.5, y0 + 3.6, f"{th} cm", attrs='data-r="th"'))
    o.append(T(x0 + W / 2 - (0 if kind != "side" else 0), y0 + 3.6, f"{wd} cm", attrs='data-r="wd"'))
    o.append(T(x0 - 1.5, y0 - L_ / 2, f"{ln} cm", anchor="end", attrs='data-r="ln"'))
    return svg(w, hh, "".join(o), cls="fsvg", extra=f'data-fig="{kind}"')

def read_composite(h):
    import re
    kind = re.search(r'data-fig="(\w+)"', h).group(1)
    g = lambda r: int(re.search(rf'data-r="{r}"[^>]*>(\d+) cm<', h).group(1))
    return kind, g("wd"), g("ln"), g("th")

# =============================================================================== isometric cuboids
C30, S30 = math.cos(math.radians(30)), math.sin(math.radians(30))
def iso_pt(i, j, k, u, ox, oy):
    return (ox + (i - j) * C30 * u, oy + (i + j) * S30 * u - k * u)

def iso_size(A, B, C, u):
    return ((A + B) * C30 * u, (A + B) * S30 * u + C * u)

def iso_units(A, B, C, u=8.0, pad=3.0):
    """a cuboid of A x B x C unit cubes in isometric view: every visible unit face is its own polygon (class uf, data-face top/left/right)"""
    w, h = iso_size(A, B, C, u)
    ox, oy = pad + B * C30 * u, pad + C * u
    o = []
    for i in range(A):                      # top
        for j in range(B):
            o.append(PG([iso_pt(i, j, C, u, ox, oy), iso_pt(i + 1, j, C, u, ox, oy), iso_pt(i + 1, j + 1, C, u, ox, oy), iso_pt(i, j + 1, C, u, ox, oy)], attrs='class="uf" data-face="top"'))
    for i in range(A):                      # face j = B (left-hand face)
        for k in range(C):
            o.append(PG([iso_pt(i, B, k, u, ox, oy), iso_pt(i + 1, B, k, u, ox, oy), iso_pt(i + 1, B, k + 1, u, ox, oy), iso_pt(i, B, k + 1, u, ox, oy)], attrs='class="uf" data-face="left"'))
    for j in range(B):                      # face i = A (right-hand face)
        for k in range(C):
            o.append(PG([iso_pt(A, j, k, u, ox, oy), iso_pt(A, j + 1, k, u, ox, oy), iso_pt(A, j + 1, k + 1, u, ox, oy), iso_pt(A, j, k + 1, u, ox, oy)], attrs='class="uf" data-face="right"'))
    return svg(round(w + 2 * pad, 2), round(h + 2 * pad, 2), "".join(o), cls="fsvg", extra='data-fig="isounits"')

def read_units(h):
    """independent reader: volume = sqrt(top faces x left faces x right faces) of the printed unit faces"""
    import re
    f = {k: len(re.findall(rf'data-face="{k}"', h)) for k in ("top", "left", "right")}
    v = math.isqrt(f["top"] * f["left"] * f["right"])
    assert v * v == f["top"] * f["left"] * f["right"], f
    return v, f

def iso_dims(A, B, C, labels, w=64, hh=48, cube=False):
    """cuboid drawn in isometric view (proportional, capped), with length labels on three edges. labels = (texts for the i-edge, j-edge, k-edge) e.g. '12 cm'"""
    sc = min((w - 18) / ((A + B) * C30), (hh - 16) / ((A + B) * S30 + C), 6.0)
    ox, oy = 8 + B * C30 * sc, 6 + C * sc
    P = lambda i, j, k: iso_pt(i, j, k, sc, ox, oy)
    o = [PG([P(0, 0, C), P(A, 0, C), P(A, B, C), P(0, B, C)]),
         PG([P(0, B, 0), P(A, B, 0), P(A, B, C), P(0, B, C)]),
         PG([P(A, 0, 0), P(A, B, 0), P(A, B, C), P(A, 0, C)])]
    # labels: i-edge along the bottom of the left face, j-edge along the bottom of the right face, k-edge up the near vertical edge
    (x1, y1), (x2, y2) = P(0, B, 0), P(A, B, 0)
    o.append(T((x1 + x2) / 2 - 3.5, (y1 + y2) / 2 + 3.2, labels[0], attrs='data-r="d1"'))
    (x1, y1), (x2, y2) = P(A, B, 0), P(A, 0, 0)
    o.append(T((x1 + x2) / 2 + 3.5, (y1 + y2) / 2 + 3.2, labels[1], attrs='data-r="d2"'))
    (x1, y1), (x2, y2) = P(A, 0, 0), P(A, 0, C)
    o.append(T(x1 + 2.2, (y1 + y2) / 2, labels[2], anchor="start", attrs='data-r="d3"'))
    return svg(w, hh, "".join(o), cls="fsvg", extra='data-fig="isodims"')

def read_dims(h):
    import re
    out = []
    for r in ("d1", "d2", "d3"):
        m = re.search(rf'data-r="{r}"[^>]*>([\d.]+) (cm|m)<', h); out.append((m.group(1), m.group(2)))
    return out

# =============================================================================== angles
def _label(cx, cy, ang, r, v, rel=None, size=3.9):
    x, y = cx + r * math.cos(math.radians(ang)), cy - r * math.sin(math.radians(ang))
    s = "?" if v == "?" else f"{v}°"
    ex = f' data-rel="{rel}"' if rel else ""
    return T(x, y, s, size=size, attrs=f'data-v="{v}"{ex}')

def line_fig(parts, w=64, hh=34, kind="line"):
    """angles on a straight line: `parts` = list of values or '?' that add up to 180 (the figure draws them to scale)"""
    vals = [0 if p == "?" else p for p in parts]
    tot = 180
    known = sum(v for v in vals)
    unk = [i for i, p in enumerate(parts) if p == "?"]
    if unk: vals[unk[0]] = tot - known
    cx, cy, R = w / 2, hh - 5, min(w / 2 - 4, hh - 8)
    o = [LN(cx - R - 2, cy, cx + R + 2, cy)]
    a = 0
    for k, v in enumerate(vals):
        a1 = a + v
        if 0 < a1 < 180: o.append(LN(cx, cy, cx + R * math.cos(math.radians(a1)), cy - R * math.sin(math.radians(a1))))
        r_arc = 5.5 + (k % 2) * 2.0
        o.append(ARC(cx, cy, r_arc, a, a1, sw=0.45))
        o.append(_label(cx, cy, (a + a1) / 2, r_arc + 4.6, parts[k]))
        a = a1
    return svg(w, hh, "".join(o), cls="fsvg", extra='data-fig="line"')

def point_fig(parts, w=60, hh=46):
    vals = [0 if p == "?" else p for p in parts]
    unk = [i for i, p in enumerate(parts) if p == "?"]
    if unk: vals[unk[0]] = 360 - sum(vals)
    cx, cy, R = w / 2, hh / 2, min(w / 2 - 5, hh / 2 - 3)
    o = []
    a = 20
    for k, v in enumerate(vals):
        o.append(LN(cx, cy, cx + R * math.cos(math.radians(a)), cy - R * math.sin(math.radians(a))))
        a1 = a + v
        r_arc = 4.5 + (k % 2) * 1.8
        o.append(ARC(cx, cy, r_arc, a, a1, sw=0.45))
        o.append(_label(cx, cy, (a + a1) / 2, r_arc + (5.2 if v > 40 else 6.5), parts[k], size=3.6))
        a = a1
    return svg(w, hh, "".join(o), cls="fsvg", extra='data-fig="point"')

def opp_fig(alpha, given, ask, w=60, hh=46):
    """two straight lines cross. The line through angle alpha (degrees from the page's right) and the horizontal-ish line cross; `given` is the value printed in the sector
    between ray 0 and ray alpha (left part is its vertically opposite); `ask` is 'opposite' (vertically opposite) or 'adjacent'. Rays: 0, alpha, 180, 180 + alpha."""
    cx, cy, R = w / 2, hh / 2, min(w / 2 - 4, hh / 2 - 3)
    o = [LN(cx - R, cy, cx + R, cy), LN(cx - R * math.cos(math.radians(alpha)), cy + R * math.sin(math.radians(alpha)), cx + R * math.cos(math.radians(alpha)), cy - R * math.sin(math.radians(alpha)))]
    secs = [(0, alpha), (alpha, 180), (180, 180 + alpha), (180 + alpha, 360)]
    labs = [None] * 4
    labs[0] = given
    labs[2 if ask == "opposite" else 1] = "?"
    for k, (a0, a1) in enumerate(secs):
        r_arc = 5.0 + (k % 2) * 1.6
        o.append(ARC(cx, cy, r_arc, a0, a1, sw=0.45))
        if labs[k] is not None:
            rel = {0: "given", 1: "adjacent", 2: "opposite"}[k] if labs[k] == "?" or k == 0 else None
            o.append(_label(cx, cy, (a0 + a1) / 2, r_arc + (5.5 if (a1 - a0) > 50 else 7.5), labs[k], rel="given" if k == 0 else ("opposite" if k == 2 else "adjacent"), size=3.6))
    return svg(w, hh, "".join(o), cls="fsvg", extra='data-fig="opp"')

def read_angle_fig(h):
    """independent reader of an angle figure: (kind, [printed values]) with '?' for the unknown; for 'opp' also the relation of the unknown"""
    import re
    kind = re.search(r'data-fig="(\w+)"', h).group(1)
    vals = re.findall(r'data-v="([\d?]+)"(?: data-rel="(\w+)")?', h)
    return kind, [v for v, _ in vals], [r for _, r in vals]

# triangles with marked angles --------------------------------------------------------------------
def tri_angles(kind, g, w=62, hh=42):
    """kind: 'sum' (two angles given), 'apex' (isosceles, apex angle given, a base angle asked), 'base' (isosceles, a base angle given, the apex asked), 'equi', 'right' (one acute angle given).
    The triangle is drawn to scale. Equal sides carry tick marks; a right angle carries a square. Labels carry data-v and data-pos."""
    def build(A, B):
        C = 180 - A - B
        L = 44.0
        Bx, By = 0.0, 0.0
        Ax, Ay = L * 1.0, 0.0
        # vertex P (apex) from angle at left vertex = A and angle at right vertex = B
        ta, tb = math.tan(math.radians(A)), math.tan(math.radians(B))
        x = L * tb / (ta + tb); y = x * ta
        return [(0, 0), (L, 0), (x, y)], C
    if kind == "sum": A_, B_ = g
    elif kind == "apex": A_ = B_ = (180 - g[0]) / 2
    elif kind == "base": A_ = B_ = g[0]
    elif kind == "equi": A_ = B_ = 60
    else: A_, B_ = 90, g[0]
    pts, C_ = build(A_, B_)
    sc = min((w - 12) / max(p[0] for p in pts), (hh - 12) / max(p[1] for p in pts), 1.0)
    ox, oy = 6, hh - 6
    P = [(ox + x * sc, oy - y * sc) for x, y in pts]
    o = [PG(P)]
    if kind == "right": o.append(RA(P[0][0], P[0][1], 1, 0, 0, -1))
    def tick(p, q, n=1):
        mx, my = (p[0] + q[0]) / 2, (p[1] + q[1]) / 2
        dx, dy = q[0] - p[0], q[1] - p[1]; l = math.hypot(dx, dy); nx, ny = -dy / l, dx / l
        return LN(mx - nx * 1.4, my - ny * 1.4, mx + nx * 1.4, my + ny * 1.4, attrs='class="tick"')
    if kind in ("apex", "base"): o += [tick(P[0], P[2]), tick(P[1], P[2])]
    if kind == "equi": o += [tick(P[0], P[1]), tick(P[1], P[2]), tick(P[0], P[2])]
    # labels (inside near each vertex)
    given = {"sum": [g[0], g[1], "?"], "apex": ["?", "?", g[0]], "base": [g[0], g[0], "?"], "equi": ["?", None, None], "right": [90, g[0], "?"]}[kind]
    if kind == "apex": given = ["?", None, g[0]]
    if kind == "base": given = [g[0], None, "?"]
    if kind == "right": given = [None, g[0], "?"]
    pos = ["base1", "base2", "apex"]
    cxm = sum(p[0] for p in P) / 3; cym = sum(p[1] for p in P) / 3
    for k in range(3):
        v = given[k]
        if v is None: continue
        if kind == "right" and v == 90: continue
        px, py = P[k]
        dx, dy = cxm - px, cym - py; l = math.hypot(dx, dy)
        d = 9.0 if k == 2 else 8.0
        lx, ly = px + dx / l * d, py + dy / l * d
        o.append(T(lx, ly, "?" if v == "?" else f"{v}°", size=3.5, attrs=f'data-v="{v}" data-pos="{pos[k]}"'))
    return svg(w, hh, "".join(o), cls="fsvg", extra=f'data-fig="tri-{kind}"')

def read_tri_angles(h):
    import re
    kind = re.search(r'data-fig="tri-(\w+)"', h).group(1)
    labs = re.findall(r'data-v="([\d?]+)" data-pos="(\w+)"', h)
    ticks = len(re.findall(r'class="tick"', h)); ra = 'class="ra"' in h
    return kind, labs, ticks, ra
