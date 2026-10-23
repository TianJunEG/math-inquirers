"""Primary 5 figures (pure black and white SVG). Every figure prints its numbers as <text> elements carrying data-* attributes, so the independent
solver of each page reads the PRINTED drawing (labels, marks, face counts), not the generator's variables.
Lengths are millimetres of the page. Strokes at least 0.5 mm."""
import math
from .common import svg

SW = 0.5
def T(x, y, s, anchor="middle", size=3.9, weight=600, attrs=""):
    return f'<text x="{x:.2f}" y="{y:.2f}" text-anchor="{anchor}" dominant-baseline="central" font-family="Fredoka" font-weight="{weight}" font-size="{size}" fill="#000" {attrs}>{s}</text>'

def TB(x, y, s, anchor="middle", size=3.9, weight=600, attrs=""):
    """a label with a white backing so that a line passing under it does not run through the digits"""
    n = len(s.replace("&#176;", "x"))
    wd = n * size * 0.58 + 1.0
    x0 = x - wd / 2 if anchor == "middle" else x - 0.5 if anchor == "start" else x - wd + 0.5
    return f'<rect x="{x0:.2f}" y="{y - size * 0.62:.2f}" width="{wd:.2f}" height="{size * 1.24:.2f}" fill="#fff"/>' + T(x, y, s, anchor, size, weight, attrs)

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
    (outside [0,1] the base is extended with a dotted line). The height label sits above the apex, the base label under the base, so no label touches a side.
    `side` is a distractor length printed beside the right-hand slanted side."""
    left_ext = max(0.0, -foot * b); right_ext = max(0.0, (foot - 1) * b)
    sc = min((w - 16) / (b + left_ext + right_ext), (hh - 15) / h, 4.4)
    bw, hgt = b * sc, h * sc
    x0, y0 = 8 + left_ext * sc, hh - 8
    A = (x0 + foot * bw, y0 - hgt); B = (x0, y0); C = (x0 + bw, y0)
    o = [PG([A, B, C], attrs='class="tri"')]
    fx = A[0]
    if foot < 0: o.append(LN(fx, y0, x0, y0, dash="1.2 1.2"))
    if foot > 1: o.append(LN(C[0], y0, fx, y0, dash="1.2 1.2"))
    o.append(LN(fx, A[1], fx, y0, dash="1.8 1.2", attrs='data-r="hline"'))
    o.append(RA(fx, y0, -1 if foot > 0.5 else 1, 0, 0, -1))
    o.append(T((B[0] + C[0]) / 2, y0 + 4.4, f"{b} cm", size=4.1, attrs='data-r="base"'))
    o.append(T(fx, A[1] - 3.6, f"{h} cm", size=4.1, attrs='data-r="height"'))
    if side is not None and 0.2 < foot < 0.8 and b >= 9:
        o.append(T((A[0] + C[0]) / 2 + 1.8, (A[1] + C[1]) / 2 - 0.5, f"{side} cm", anchor="start", size=4.1, attrs='data-r="side"'))
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
    side: rectangle wd x ln with a right-angled triangle (one side ln, width th) joined on the right. Labels never touch a side."""
    tot_w = wd + (th if kind == "side" else 0)
    tot_h = ln + (th if kind == "house" else 0)
    sc = min((w - 20) / tot_w, (hh - 17) / tot_h, 5.0)
    x0, y0 = 14, hh - 8
    W, L_, Th = wd * sc, ln * sc, th * sc
    o = []
    if kind == "house":
        o.append(PG([(x0, y0), (x0 + W, y0), (x0 + W, y0 - L_), (x0 + W / 2, y0 - L_ - Th), (x0, y0 - L_)]))
        o.append(LN(x0, y0 - L_, x0 + W, y0 - L_, dash="1.4 1.2"))
        o.append(LN(x0 + W / 2, y0 - L_ - Th, x0 + W / 2, y0 - L_, dash="1.8 1.2"))
        o.append(T(x0 + W / 2, y0 - L_ - Th - 3.6, f"{th} cm", size=4.1, attrs='data-r="th"'))
    elif kind == "notch":
        o.append(PG([(x0, y0), (x0 + W, y0), (x0 + W, y0 - L_), (x0 + W / 2, y0 - L_ + Th), (x0, y0 - L_)]))
        o.append(LN(x0, y0 - L_, x0 + W, y0 - L_, dash="1.4 1.2"))
        o.append(LN(x0 + W / 2, y0 - L_ + Th, x0 + W / 2, y0 - L_, dash="1.8 1.2"))
        o.append(T(x0 + W / 2, y0 - L_ - 3.6, f"{th} cm", size=4.1, attrs='data-r="th"'))
    else:
        o.append(PG([(x0, y0), (x0 + W, y0), (x0 + W + Th, y0), (x0 + W, y0 - L_), (x0, y0 - L_)]))
        o.append(LN(x0 + W, y0, x0 + W, y0 - L_, dash="1.4 1.2"))
        o.append(T(x0 + W + Th / 2 + 0.5, y0 + 4.4, f"{th} cm", size=4.1, attrs='data-r="th"'))
    o.append(T(x0 + W / 2, y0 + 4.4, f"{wd} cm", size=4.1, attrs='data-r="wd"'))
    o.append(T(x0 - 1.5, y0 - L_ / 2, f"{ln} cm", anchor="end", size=4.1, attrs='data-r="ln"'))
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
    sc = min((w - 26) / ((A + B) * C30), (hh - 16) / ((A + B) * S30 + C), 6.0)
    ox, oy = 8 + B * C30 * sc, 6 + C * sc
    P = lambda i, j, k: iso_pt(i, j, k, sc, ox, oy)
    o = [PG([P(0, 0, C), P(A, 0, C), P(A, B, C), P(0, B, C)]),
         PG([P(0, B, 0), P(A, B, 0), P(A, B, C), P(0, B, C)]),
         PG([P(A, 0, 0), P(A, B, 0), P(A, B, C), P(A, 0, C)])]
    # labels: i-edge along the bottom of the left face, j-edge along the bottom of the right face, k-edge up the near vertical edge
    (x1, y1), (x2, y2) = P(0, B, 0), P(A, B, 0)
    o.append(T((x1 + x2) / 2 - 3.5, (y1 + y2) / 2 + 3.6, labels[0], size=4.1, attrs='data-r="d1"'))
    (x1, y1), (x2, y2) = P(A, B, 0), P(A, 0, 0)
    o.append(T((x1 + x2) / 2 + 3.5, (y1 + y2) / 2 + 3.6, labels[1], size=4.1, attrs='data-r="d2"'))
    (x1, y1), (x2, y2) = P(A, 0, 0), P(A, 0, C)
    o.append(T(x1 + 2.2, (y1 + y2) / 2, labels[2], anchor="start", size=4.1, attrs='data-r="d3"'))
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
        o.append(_label(cx, cy, (a + a1) / 2, r_arc + (5.2 if v > 40 else 6.5), parts[k], size=4.0))
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
            o.append(_label(cx, cy, (a0 + a1) / 2, r_arc + (5.5 if (a1 - a0) > 50 else 7.5), labs[k], rel="given" if k == 0 else ("opposite" if k == 2 else "adjacent"), size=4.0))
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
    else: A_, B_ = (90, g[0]) if g[0] < 45 else (90, 90 - g[0])      # the given acute angle is always the wider of the two, so its label has room
    pts, C_ = build(A_, B_)
    sc = min((w - 12) / max(p[0] for p in pts), (hh - 12) / max(p[1] for p in pts), 1.4)
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
    given = None
    if kind == "sum": given = [g[0], g[1], "?"]
    if kind == "equi": given = ["?", None, None]
    if kind == "apex": given = ["?", None, g[0]]
    if kind == "base": given = [g[0], None, "?"]
    if kind == "right": given = [None, g[0], "?"] if g[0] < 45 else [None, "?", g[0]]
    pos = ["base1", "base2", "apex"]
    for k in range(3):
        v = given[k]
        if v is None: continue
        if kind == "right" and v == 90: continue
        px, py = P[k]
        u1 = (P[(k + 1) % 3][0] - px, P[(k + 1) % 3][1] - py); u2 = (P[(k + 2) % 3][0] - px, P[(k + 2) % 3][1] - py)
        l1, l2 = math.hypot(*u1), math.hypot(*u2)
        bx, by = u1[0] / l1 + u2[0] / l2, u1[1] / l1 + u2[1] / l2; bl = math.hypot(bx, by)
        th = math.acos(max(-1, min(1, (u1[0] * u2[0] + u1[1] * u2[1]) / (l1 * l2))))
        d = min(6.4 / max(math.sin(th / 2), 0.22), 0.42 * min(l1, l2), 14.0)
        lx, ly = px + bx / bl * d, py + by / bl * d
        o.append(T(lx, ly, "?" if v == "?" else f"{v}\u00b0", size=4.2, attrs=f'data-v="{v}" data-pos="{pos[k]}"'))
    return svg(w, hh, "".join(o), cls="fsvg", extra=f'data-fig="tri-{kind}"')

def read_tri_angles(h):
    import re
    kind = re.search(r'data-fig="tri-(\w+)"', h).group(1)
    labs = re.findall(r'data-v="([\d?]+)" data-pos="(\w+)"', h)
    ticks = len(re.findall(r'class="tick"', h)); ra = 'class="ra"' in h
    return kind, labs, ticks, ra

# =============================================================================== two-step angle figures
def _fit(P, w, hh, pad=8.0, cap=2.2):
    xs = [p[0] for p in P.values()]; ys = [p[1] for p in P.values()]
    sc = min((w - 2 * pad) / (max(xs) - min(xs)), (hh - 2 * pad) / (max(ys) - min(ys)), cap)
    return {k: (pad + (x - min(xs)) * sc, pad + (y - min(ys)) * sc) for k, (x, y) in P.items()}

def _lab(P, k, centre, v, pos, d=8.0, size=4.1):
    px, py = P[k]; dx, dy = centre[0] - px, centre[1] - py; l = math.hypot(dx, dy) or 1
    s = "?" if v == "?" else f"{v}°"
    return T(px + dx / l * d, py + dy / l * d, s, size=size, attrs=f'data-v="{v}" data-pos="{pos}"')

def _inlab(P, k, n1, n2, v, pos, size=4.1):
    """an interior angle label on the bisector at vertex k (neighbours n1 and n2), far enough in for the label to clear both sides"""
    px, py = P[k]; u1 = (P[n1][0] - px, P[n1][1] - py); u2 = (P[n2][0] - px, P[n2][1] - py)
    l1, l2 = math.hypot(*u1), math.hypot(*u2)
    bx, by = u1[0] / l1 + u2[0] / l2, u1[1] / l1 + u2[1] / l2; bl = math.hypot(bx, by)
    th = math.acos(max(-1, min(1, (u1[0] * u2[0] + u1[1] * u2[1]) / (l1 * l2))))
    d = min(6.4 / max(math.sin(th / 2), 0.22), 0.42 * min(l1, l2), 14.0)
    s_ = "?" if v == "?" else f"{v}\u00b0"
    return T(px + bx / bl * d, py + by / bl * d, s_, size=size, attrs=f'data-v="{v}" data-pos="{pos}"')

def ext_fig(a, b, w=64, hh=36):
    """triangle ABC (angle b at B, angle a at A, the rest at C) with BC extended beyond C to D; the angle between CA and CD is asked"""
    Cc = 180 - a - b
    Bp, Cp = (0.0, 0.0), (40.0, 0.0)
    ab = math.sin(math.radians(Cc)) / math.sin(math.radians(a)) * 40.0           # |BA|
    Ap = (ab * math.cos(math.radians(b)), -ab * math.sin(math.radians(b)))
    Dp = (40.0 + 11.0, 0.0)
    P = _fit({"B": Bp, "C": Cp, "A": Ap, "D": Dp}, w, hh, pad=6.0, cap=3.0)
    o = [PG([P["A"], P["B"], P["C"]]), LN(*P["C"], *P["D"])]
    o.append(_inlab(P, "A", "B", "C", a, "apex")); o.append(_inlab(P, "B", "A", "C", b, "base1"))
    cx, cy = P["C"]; ang = math.degrees(math.atan2(-(P["A"][1] - cy), P["A"][0] - cx))
    if ang > 0: o.append(ARC(cx, cy, 5.0, 0, ang, sw=0.45))
    mid = ang / 2
    o.append(T(cx + 10.5 * math.cos(math.radians(mid)), cy - 10.5 * math.sin(math.radians(mid)), "?", size=4.3, attrs='data-v="?" data-pos="ext"'))
    return svg(w, hh, "".join(o), cls="fsvg", extra='data-fig="ext"')

def isoext_fig(g, w=64, hh=36):
    """isosceles triangle with apex angle g (printed), equal sides ticked, base extended beyond the right base vertex; the exterior angle there is asked"""
    base = (180 - g) / 2
    Bp, Cp = (0.0, 0.0), (40.0, 0.0)
    h = 20.0 * math.tan(math.radians(base))
    Ap = (20.0, -h)
    P = _fit({"B": Bp, "C": Cp, "A": Ap, "D": (58.0, 0.0)}, w, hh)
    o = [PG([P["A"], P["B"], P["C"]]), LN(*P["C"], *P["D"])]
    def tick(p, q):
        mx, my = (p[0] + q[0]) / 2, (p[1] + q[1]) / 2; dx, dy = q[0] - p[0], q[1] - p[1]; l = math.hypot(dx, dy); nx, ny = -dy / l, dx / l
        return LN(mx - nx * 1.4, my - ny * 1.4, mx + nx * 1.4, my + ny * 1.4, attrs='class="tick"')
    o += [tick(P["A"], P["B"]), tick(P["A"], P["C"])]
    o.append(T(P["A"][0], P["A"][1] - 4.2, f"{g}\u00b0", size=4.1, attrs=f'data-v="{g}" data-pos="apex"'))
    cx, cy = P["C"]; ang = math.degrees(math.atan2(-(P["A"][1] - cy), P["A"][0] - cx))
    o.append(ARC(cx, cy, 5.0, 0, ang, sw=0.45))
    o.append(T(cx + 10.5 * math.cos(math.radians(ang / 2)), cy - 10.5 * math.sin(math.radians(ang / 2)), "?", size=4.3, attrs='data-v="?" data-pos="ext"'))
    return svg(w, hh, "".join(o), cls="fsvg", extra='data-fig="isoext"')

def bow_fig(a, b, c, w=60, hh=46):
    """two straight lines cross at O; the triangle POQ above has angles a at P and b at Q, the triangle SOR below has angle c at S and ? at R"""
    O_ = (0.0, 0.0)
    ang_o = 180 - a - b
    PQ = 30.0
    OP = PQ * math.sin(math.radians(b)) / math.sin(math.radians(ang_o))
    tP = math.radians(a)
    Hh = OP * math.sin(tP)
    Px = -OP * math.cos(tP); Qx = Px + PQ
    P_ = (Px, -Hh); Q_ = (Qx, -Hh)
    R_ang = a + b - c
    Sd = 14.0
    dirP = (-P_[0], -P_[1]); lp = math.hypot(*dirP); S_ = (dirP[0] / lp * Sd, dirP[1] / lp * Sd)
    OR = Sd * math.sin(math.radians(c)) / math.sin(math.radians(R_ang))
    dirQ = (-Q_[0], -Q_[1]); lq = math.hypot(*dirQ); R_ = (dirQ[0] / lq * OR, dirQ[1] / lq * OR)
    P = _fit({"P": P_, "Q": Q_, "O": O_, "S": S_, "R": R_}, w, hh, pad=7.0)
    o = [LN(*P["P"], *P["S"]), LN(*P["Q"], *P["R"]), LN(*P["P"], *P["Q"]), LN(*P["S"], *P["R"])]
    ct = ((P["P"][0] + P["Q"][0] + P["O"][0]) / 3, (P["P"][1] + P["Q"][1] + P["O"][1]) / 3)
    cb = ((P["S"][0] + P["R"][0] + P["O"][0]) / 3, (P["S"][1] + P["R"][1] + P["O"][1]) / 3)
    o.append(_lab(P, "P", ct, a, "P", 7.5)); o.append(_lab(P, "Q", ct, b, "Q", 7.5))
    o.append(_lab(P, "S", cb, c, "S", 7.5)); o.append(_lab(P, "R", cb, "?", "R", 7.5))
    return svg(w, hh, "".join(o), cls="fsvg", extra='data-fig="bow"')

def read_labels(h):
    import re
    kind = re.search(r'data-fig="(\w+)"', h).group(1)
    return kind, {pos: v for v, pos in re.findall(r'data-v="([\d?]+)" data-pos="(\w+)"', h)}


def ext2_fig(e, f, w=64, hh=34):
    """triangle ABC on a straight line (extended both sides); the two exterior angles e (at B) and f (at C) are printed, the angle at A is asked"""
    be, ga = 180 - e, 180 - f
    al = 180 - be - ga
    Bp, Cp = (0.0, 0.0), (40.0, 0.0)
    ba = 40.0 * math.sin(math.radians(ga)) / math.sin(math.radians(al))
    Ap = (ba * math.cos(math.radians(be)), -ba * math.sin(math.radians(be)))
    P = _fit({"B": Bp, "C": Cp, "A": Ap, "L": (-12.0, 0.0), "R": (52.0, 0.0)}, w, hh, pad=5.0)
    o = [PG([P["A"], P["B"], P["C"]]), LN(*P["L"], *P["R"])]
    bx, by = P["B"]; cx, cy = P["C"]
    o.append(ARC(bx, by, 5.0, be, 180, sw=0.45)); o.append(ARC(cx, cy, 5.0, 0, f, sw=0.45))
    mb, mc = (be + 180) / 2, f / 2
    o.append(T(bx + 10.5 * math.cos(math.radians(mb)), by - 10.5 * math.sin(math.radians(mb)), f"{e}\u00b0", size=4.1, attrs=f'data-v="{e}" data-pos="extB"'))
    o.append(T(cx + 10.5 * math.cos(math.radians(mc)), cy - 10.5 * math.sin(math.radians(mc)), f"{f}\u00b0", size=4.1, attrs=f'data-v="{f}" data-pos="extC"'))
    ax, ay = P["A"]
    d1 = math.degrees(math.atan2(-(by - ay), bx - ax)); d2 = math.degrees(math.atan2(-(cy - ay), cx - ax))
    o.append(ARC(ax, ay, 5.0, min(d1, d2), max(d1, d2), sw=0.45))
    o.append(T(ax, ay + 9.0, "?", size=4.3, attrs='data-v="?" data-pos="apex"'))
    return svg(w, hh, "".join(o), cls="fsvg", extra='data-fig="ext2"')
