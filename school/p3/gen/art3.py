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



# ---------------------------------------------------------------------------------------------------- weighing dials (copied from P2)
def dial_svg(value, vmax, major, minor, unit):
    """a weighing dial: 270 degree sweep, numerals outside the ring, a needle; value read back by read_dial"""
    cx = cy = 24.0; R = 16.5
    ang = lambda v: math.radians(-135 + 270 * v / vmax)
    p = [f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="#fff" stroke="#000" stroke-width="0.8"/>']
    v = 0
    while v <= vmax + 1e-9:
        a = ang(v); L = 3.0 if v % major == 0 else 1.6
        p.append(f'<line class="dt" x1="{cx+R*math.sin(a):.2f}" y1="{cy-R*math.cos(a):.2f}" x2="{cx+(R-L)*math.sin(a):.2f}" y2="{cy-(R-L)*math.cos(a):.2f}" stroke="#000" stroke-width="{0.7 if v % major == 0 else 0.5}"/>')
        if v % major == 0:
            n_ = len(str(int(v))); rr = R + 1.4 + 1.2 * n_ * abs(math.sin(a)) + 1.4 * abs(math.cos(a))   # numeral box clears the ring (audit M3)
            p.append(f'<text x="{cx+rr*math.sin(a):.2f}" y="{cy-rr*math.cos(a)+0.2:.2f}" text-anchor="middle" dominant-baseline="central" font-family="Nunito Sans" font-weight="800" font-size="3.9" fill="#000">{int(v)}</text>')
        v += minor
    a = ang(value)
    p.append(f'<line class="needle" x1="24" y1="24" x2="{cx+14.2*math.sin(a):.3f}" y2="{cy-14.2*math.cos(a):.3f}" stroke="#000" stroke-width="1.0" stroke-linecap="round"/>')
    p.append(f'<circle cx="{cx}" cy="{cy}" r="1.6" fill="#000"/>')
    p.append(f'<text class="dunit" x="{cx}" y="{cy+9.5}" text-anchor="middle" dominant-baseline="central" font-family="Nunito Sans" font-weight="800" font-size="4.4" fill="#000">{unit}</text>')
    return svg(56, 48, '<g transform="translate(4,0)">' + "".join(p) + '</g>', extra=f'data-max="{vmax}"')

def read_dial(s):
    vmax = int(re.search(r'data-max="(\d+)"', s).group(1))
    m = re.search(r'class="needle" x1="24" y1="24" x2="([-\d.]+)" y2="([-\d.]+)"', s)
    a = math.degrees(math.atan2(float(m.group(1)) - 24, 24 - float(m.group(2))))
    return round((a + 135) / 270 * vmax), re.search(r'class="dunit"[^>]*>([^<]+)<', s).group(1)


# ---------------------------------------------------------------------------------------------------- beakers with a scale in millilitres
def beaker_svg(level, vmax, step, label_step, unit="m\u2113"):
    """a beaker with ticks every `step` and numbers every `label_step` (m\u2113) and a liquid level; read back by read_beaker"""
    top, bot = 4.0, 48.0; x0, x1 = 15.0, 33.0
    y = lambda v: bot - (bot - top) * v / vmax
    p = [f'<rect class="tankbody" x="{x0}" y="{top}" width="{x1-x0}" height="{bot-top}" fill="#fff" stroke="#000" stroke-width="0.7"/>']
    yy = bot - 0.7
    while yy > y(level):
        p.append(f'<line x1="{x0+0.4}" y1="{yy:.2f}" x2="{x1-0.4}" y2="{yy:.2f}" stroke="#000" stroke-width="0.5"/>'); yy -= 2.4
    p.append(f'<line class="level" x1="{x0}" y1="{y(level):.2f}" x2="{x1}" y2="{y(level):.2f}" stroke="#000" stroke-width="0.9"/>')
    v = 0
    while v <= vmax:
        major = v % label_step == 0
        p.append(f'<line class="lt" x1="{x0-(3.2 if major else 1.8):.1f}" y1="{y(v):.2f}" x2="{x0}" y2="{y(v):.2f}" stroke="#000" stroke-width="{0.6 if major else 0.5}"/>')
        if major:
            p.append(f'<text x="{x0-3.8}" y="{y(v)+0.1:.2f}" text-anchor="end" dominant-baseline="central" font-family="Nunito Sans" font-weight="800" font-size="3.4" fill="#000">{v}</text>')
        v += step
    p.append(f'<text class="bunit" x="{(x0+x1)/2}" y="{bot+2.6}" text-anchor="middle" dominant-baseline="central" font-family="Nunito Sans" font-weight="800" font-size="4.6" fill="#000">{unit}</text>')
    return svg(38, 54, "".join(p), extra=f'data-max="{vmax}"')

def read_beaker(s):
    vmax = int(re.search(r'data-max="(\d+)"', s).group(1))
    ys = [float(v) for v in re.findall(r'class="lt" x1="[\d.]+" y1="([\d.]+)"', s)]       # tick y positions, bottom (0) first
    ly = float(re.search(r'class="level" x1="[\d.]+" y1="([\d.]+)"', s).group(1))
    return round((ys[0] - ly) / (ys[0] - ys[-1]) * vmax)

# ---------------------------------------------------------------------------------------------------- stopwatch (a seconds hand on a 0 to 60 face)
def stopwatch_svg(sec):
    cx = cy = 24.0; R = 16.5
    p = [f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="#fff" stroke="#000" stroke-width="0.7"/>']
    for k in range(60):
        a = math.radians(k * 6); L = 3.0 if k % 5 == 0 else 1.5
        p.append(f'<line x1="{cx+R*math.sin(a):.2f}" y1="{cy-R*math.cos(a):.2f}" x2="{cx+(R-L)*math.sin(a):.2f}" y2="{cy-(R-L)*math.cos(a):.2f}" stroke="#000" stroke-width="{0.7 if k % 5 == 0 else 0.5}"/>')
    for k in range(5, 61, 5):
        a = math.radians(k * 6)
        p.append(f'<text x="{cx+20.6*math.sin(a):.2f}" y="{cy-20.6*math.cos(a)+0.2:.2f}" text-anchor="middle" dominant-baseline="central" font-family="Nunito Sans" font-weight="800" font-size="3.9" fill="#000">{k}</text>')
    a = math.radians(sec * 6)
    p.append(f'<line class="needle" x1="24" y1="24" x2="{cx+14.2*math.sin(a):.3f}" y2="{cy-14.2*math.cos(a):.3f}" stroke="#000" stroke-width="1.0" stroke-linecap="round"/>')
    p.append(f'<circle cx="{cx}" cy="{cy}" r="1.6" fill="#000"/>')
    p.append(f'<text x="{cx}" y="{cy + (9.5 if math.cos(a) > -0.2 else -9.5)}" text-anchor="middle" dominant-baseline="central" font-family="Nunito Sans" font-weight="800" font-size="3.6" fill="#000">seconds</text>')   # the word goes on the side away from the hand
    return svg(48, 48, "".join(p))

def read_stopwatch(s):
    m = re.search(r'class="needle" x1="24" y1="24" x2="([-\d.]+)" y2="([-\d.]+)"', s)
    a = math.degrees(math.atan2(float(m.group(1)) - 24, 24 - float(m.group(2)))) % 360
    return round(a / 6) % 60

# ---------------------------------------------------------------------------------------------------- unit-square figures and labelled rectilinear figures
CELL = 8.0      # mm: a counted unit square is 8 mm

def grid_fig(cells, cell=CELL, name=None):
    """a figure made of unit squares; `cells` is a set of (col, row). Each square is drawn (class cell) with a thin line, the outline thick."""
    cols = max(c for c, r in cells) + 1; rows = max(r for c, r in cells) + 1
    p = []
    for c, r in sorted(cells, key=lambda t: (t[1], t[0])):
        p.append(f'<rect class="cell" x="{c * cell + 1:.1f}" y="{r * cell + 1:.1f}" width="{cell}" height="{cell}" fill="#fff" stroke="#000" stroke-width="0.5"/>')
    edges = []
    for c, r in cells:
        if (c, r - 1) not in cells: edges.append((c, r, c + 1, r))
        if (c, r + 1) not in cells: edges.append((c, r + 1, c + 1, r + 1))
        if (c - 1, r) not in cells: edges.append((c, r, c, r + 1))
        if (c + 1, r) not in cells: edges.append((c + 1, r, c + 1, r + 1))
    for x1, y1, x2, y2 in edges:
        p.append(f'<line x1="{x1 * cell + 1:.1f}" y1="{y1 * cell + 1:.1f}" x2="{x2 * cell + 1:.1f}" y2="{y2 * cell + 1:.1f}" stroke="#000" stroke-width="0.9" stroke-linecap="square"/>')
    if name:
        p.append(f'<text x="{cols * cell / 2 + 1:.1f}" y="{rows * cell + 6:.1f}" text-anchor="middle" font-family="Fredoka" font-weight="600" font-size="4.6" fill="#000">{name}</text>')
    H = rows * cell + 2 + (7 if name else 0)
    return svg(round(cols * cell + 2, 1), round(H, 1), "".join(p))

def read_grid_fig(s):
    """independent reader: the set of unit squares (from the drawn rectangles) -> (area, perimeter)"""
    cs = set()
    for m in re.finditer(r'class="cell" x="([\d.]+)" y="([\d.]+)" width="([\d.]+)"', s):
        w = float(m.group(3)); cs.add((round((float(m.group(1)) - 1) / w), round((float(m.group(2)) - 1) / w)))
    per = sum(1 for (c, r) in cs for d in ((1, 0), (-1, 0), (0, 1), (0, -1)) if (c + d[0], r + d[1]) not in cs)
    return len(cs), per, cs

def random_polyomino(rng, n, w, h):
    """a connected figure of n unit squares inside w x h with no hole, at least 2 columns and 2 rows used"""
    for _ in range(2000):
        cells = {(rng.randrange(w), rng.randrange(h))}
        while len(cells) < n:
            c, r = rng.choice(sorted(cells)); d = rng.choice(((1, 0), (-1, 0), (0, 1), (0, -1)))
            q = (c + d[0], r + d[1])
            if 0 <= q[0] < w and 0 <= q[1] < h: cells.add(q)
        if len({c for c, r in cells}) < 2 or len({r for c, r in cells}) < 2: continue
        # normalise to the corner
        mc = min(c for c, r in cells); mr = min(r for c, r in cells); cells = {(c - mc, r - mr) for c, r in cells}
        W = max(c for c, r in cells) + 1; Hh = max(r for c, r in cells) + 1
        # no hole: flood the empty cells from outside the bounding box
        seen = set(); stack = [(-1, -1)]
        while stack:
            q = stack.pop()
            if q in seen or not (-1 <= q[0] <= W and -1 <= q[1] <= Hh) or q in cells: continue
            seen.add(q); stack += [(q[0] + 1, q[1]), (q[0] - 1, q[1]), (q[0], q[1] + 1), (q[0], q[1] - 1)]
        empties = {(c, r) for c in range(W) for r in range(Hh)} - cells
        if empties - seen: continue
        return cells
    raise RuntimeError("polyomino")

def poly_svg(verts, unit, kind, mm_unit, labels_on=None, name=None):
    """a rectilinear polygon (integer vertices, y down) drawn to scale; every side in `labels_on` (default all) gets its length and unit.
    kind: 'rect' (two labels: top and left), 'square' (one: top), 'poly' (all sides). Reader: read_poly."""
    n = len(verts); xs = [v[0] for v in verts]; ys = [v[1] for v in verts]
    mm_unit = min(mm_unit, 28.0 / (max(ys) - min(ys)), 31.0 / (max(xs) - min(xs)))
    W = (max(xs) - min(xs)) * mm_unit; H = (max(ys) - min(ys)) * mm_unit
    ox, oy = 14.0, 5.0
    pts = [(ox + (x - min(xs)) * mm_unit, oy + (y - min(ys)) * mm_unit) for x, y in verts]
    p = [f'<polygon points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in pts)}" fill="#fff" stroke="#000" stroke-width="0.8" stroke-linejoin="miter"/>']
    cx = sum(x for x, y in pts) / n; cy = sum(y for x, y in pts) / n
    area = sum(pts[k][0] * pts[(k + 1) % n][1] - pts[(k + 1) % n][0] * pts[k][1] for k in range(n))
    labs = []
    for i in range(n):
        (x1, y1), (x2, y2) = pts[i], pts[(i + 1) % n]; (a1, b1), (a2, b2) = verts[i], verts[(i + 1) % n]
        ln = abs(a2 - a1) + abs(b2 - b1)
        def refl(k):
            (px_, py_), (qx_, qy_), (rx_, ry_) = pts[(k - 1) % n], pts[k], pts[(k + 1) % n]
            cr = (qx_ - px_) * (ry_ - qy_) - (qy_ - py_) * (rx_ - qx_)
            return cr * area < 0
        tt = 0.5 + (0.2 if refl(i) else 0.0) - (0.2 if refl((i + 1) % n) else 0.0)
        mx, my = x1 + (x2 - x1) * tt, y1 + (y2 - y1) * tt
        horiz = abs(y2 - y1) < 1e-6
        def inside(px, py):
            c = False
            for j in range(n):
                (ax, ay), (bx, by) = pts[j], pts[(j + 1) % n]
                if (ay > py) != (by > py) and px < (bx - ax) * (py - ay) / (by - ay) + ax: c = not c
            return c
        if horiz:
            out_up = not inside(mx, my - 1.2)                    # the outside of the edge is above it
            lx, ly, anc = mx, (my - 1.8 if out_up else my + 4.6), "middle"
        else:
            out_left = not inside(mx - 1.2, my)
            lx, ly, anc = (mx - 1.8 if out_left else mx + 1.8), my + 1.3, ("end" if out_left else "start")
        labs.append((i, ln, lx, ly, anc, horiz, mx, my))
    show = []
    if kind == "rect": show = [i for i, ln, lx, ly, anc, horiz, mx, my in labs if (horiz and my == min(y for x, y in pts)) or ((not horiz) and mx == min(x for x, y in pts))]
    elif kind == "square": show = [i for i, ln, lx, ly, anc, horiz, mx, my in labs if horiz and my == min(y for x, y in pts)]
    else: show = [l[0] for l in labs]
    for i, ln, lx, ly, anc, horiz, mx, my in labs:
        if i in show:
            p.append(f'<text class="lab" data-v="{ln}" x="{lx:.1f}" y="{ly:.1f}" text-anchor="{anc}" font-family="Nunito Sans" font-weight="800" font-size="4.0" fill="#000">{ln} {unit}</text>')
    w_ = ox + W + 12; h_ = oy + H + 7 + (6 if name else 0)
    if name: p.append(f'<text x="{ox + W / 2:.1f}" y="{oy + H + 11:.1f}" text-anchor="middle" font-family="Fredoka" font-weight="600" font-size="4.6" fill="#000">{name}</text>')
    return svg(round(w_, 1), round(h_, 1), "".join(p), extra=f'data-kind="{kind}"')

def read_poly(s):
    """independent reader: kind and the printed side lengths -> (kind, labels, unit)"""
    kind = re.search(r'data-kind="(\w+)"', s).group(1)
    labs = [(int(a), u) for a, u in re.findall(r'class="lab" data-v="(\d+)"[^>]*>\d+ (cm|m)<', s)]
    return kind, [a for a, u in labs], (labs[0][1] if labs else None)

# ---------------------------------------------------------------------------------------------------- angles
def angle_svg(deg, rot, arm=18.5):
    """an angle of `deg` degrees with its vertex near the left; the first arm points `rot` degrees anticlockwise from east.
    Arms are lines (class arm) from the vertex; a small arc marks the angle. Read back by read_angle."""
    vx, vy = 23.0, 23.0
    a1 = math.radians(rot); a2 = math.radians(rot + deg)
    p1 = (vx + arm * math.cos(a1), vy - arm * math.sin(a1)); p2 = (vx + arm * math.cos(a2), vy - arm * math.sin(a2))
    r = 5.0
    q1 = (vx + r * math.cos(a1), vy - r * math.sin(a1)); q2 = (vx + r * math.cos(a2), vy - r * math.sin(a2))
    large = 1 if deg > 180 else 0
    inner = (f'<line class="arm" x1="{vx}" y1="{vy}" x2="{p1[0]:.2f}" y2="{p1[1]:.2f}" stroke="#000" stroke-width="0.8" stroke-linecap="round"/>'
             f'<line class="arm" x1="{vx}" y1="{vy}" x2="{p2[0]:.2f}" y2="{p2[1]:.2f}" stroke="#000" stroke-width="0.8" stroke-linecap="round"/>'
             f'<path d="M{q1[0]:.2f},{q1[1]:.2f} A{r},{r} 0 {large} 0 {q2[0]:.2f},{q2[1]:.2f}" fill="none" stroke="#000" stroke-width="0.5"/>'
             f'<circle cx="{vx}" cy="{vy}" r="0.9" fill="#000"/>')
    return svg(46, 46, inner, extra=f'data-vx="{vx}" data-vy="{vy}"')

def read_angle(s):
    vx = float(re.search(r'data-vx="([\d.]+)"', s).group(1)); vy = float(re.search(r'data-vy="([\d.]+)"', s).group(1))
    arms = [(float(x2) - vx, vy - float(y2)) for x2, y2 in re.findall(r'class="arm" x1="[\d.]+" y1="[\d.]+" x2="([-\d.]+)" y2="([-\d.]+)"', s)]
    a1 = math.degrees(math.atan2(arms[0][1], arms[0][0])); a2 = math.degrees(math.atan2(arms[1][1], arms[1][0]))
    return round(((a2 - a1) % 360), 1)

# ---------------------------------------------------------------------------------------------------- parallel and perpendicular lines
def lines_svg(ref, cands, W=60.0, H=34.0):
    """ref = ((x1,y1),(x2,y2)) drawn thick with the label AB; cands = [(letter, (x1,y1), (x2,y2))] thin lines with their letters. Coordinates in mm."""
    p = [f'<line class="ref" x1="{ref[0][0]:.2f}" y1="{ref[0][1]:.2f}" x2="{ref[1][0]:.2f}" y2="{ref[1][1]:.2f}" stroke="#000" stroke-width="1.4" stroke-linecap="round"/>']
    for lab, (x1, y1), (x2, y2) in cands:
        p.append(f'<line class="cand" data-l="{lab}" x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" stroke="#000" stroke-width="0.7" stroke-linecap="round"/>')
    return p

def seg_cross(p1, p2, p3, p4):
    def o(a, b, c): return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
    d1, d2, d3, d4 = o(p3, p4, p1), o(p3, p4, p2), o(p1, p2, p3), o(p1, p2, p4)
    return (d1 * d2 < 0) and (d3 * d4 < 0)

def pt_seg_dist(p, s):
    (x1, y1), (x2, y2) = s; dx, dy = x2 - x1, y2 - y1
    t = max(0.0, min(1.0, ((p[0] - x1) * dx + (p[1] - y1) * dy) / (dx * dx + dy * dy)))
    return math.hypot(p[0] - (x1 + t * dx), p[1] - (y1 + t * dy))

def seg_dist(s1, s2):
    """shortest distance between two segments that do not cross"""
    return min(pt_seg_dist(s1[0], s2), pt_seg_dist(s1[1], s2), pt_seg_dist(s2[0], s1), pt_seg_dist(s2[1], s1))

def read_lines(s):
    ref = re.search(r'class="ref" x1="([-\d.]+)" y1="([-\d.]+)" x2="([-\d.]+)" y2="([-\d.]+)"', s)
    ref = tuple(float(v) for v in ref.groups())
    cands = {l: tuple(float(v) for v in (x1, y1, x2, y2)) for l, x1, y1, x2, y2 in re.findall(r'class="cand" data-l="(\w)" x1="([-\d.]+)" y1="([-\d.]+)" x2="([-\d.]+)" y2="([-\d.]+)"', s)}
    return ref, cands

def relation(ref, c, tol=0.02):
    """'parallel', 'perpendicular' or 'neither' for two segments given as (x1,y1,x2,y2)"""
    ux, uy = ref[2] - ref[0], ref[3] - ref[1]; vx, vy = c[2] - c[0], c[3] - c[1]
    nu = math.hypot(ux, uy); nv = math.hypot(vx, vy)
    cross = (ux * vy - uy * vx) / (nu * nv); dot = (ux * vx + uy * vy) / (nu * nv)
    if abs(cross) < tol: return "parallel"
    if abs(dot) < tol: return "perpendicular"
    return "neither"

# ---------------------------------------------------------------------------------------------------- bar graphs
def bar_svg(names, values, vmax, step, label_step, w=86.0, h=52.0, title=None, unit=None):
    """a vertical bar graph: scale on the left (a gridline every `step`, a number every `label_step`), black bars. Read back by read_bars."""
    left, right, top, bot = 13.0, w - 2.0, 7.0 if title else 3.0, h - 8.0
    y = lambda v: bot - (bot - top) * v / vmax
    p = []
    if title: p.append(f'<text x="{(left + right) / 2:.1f}" y="3.6" text-anchor="middle" dominant-baseline="central" font-family="Fredoka" font-weight="600" font-size="4.2" fill="#000">{title}</text>')
    v = 0
    while v <= vmax:
        maj = v % label_step == 0
        p.append(f'<line class="axt" data-v="{v}" x1="{left}" y1="{y(v):.2f}" x2="{right}" y2="{y(v):.2f}" stroke="#000" stroke-width="{0.8 if v == 0 else (0.6 if maj else 0.5)}"/>')
        if maj: p.append(f'<text class="axl" data-v="{v}" x="{left - 1.6}" y="{y(v):.2f}" text-anchor="end" dominant-baseline="central" font-family="Nunito Sans" font-weight="800" font-size="3.4" fill="#000">{v}</text>')
        v += step
    p.append(f'<line x1="{left}" y1="{top}" x2="{left}" y2="{bot}" stroke="#000" stroke-width="0.6"/>')
    n = len(names); slot = (right - left) / n; bw = slot * 0.56
    for i, (nm, val) in enumerate(zip(names, values)):
        x = left + slot * i + (slot - bw) / 2
        p.append(f'<rect class="bar" data-n="{nm}" x="{x:.2f}" y="{y(val):.2f}" width="{bw:.2f}" height="{bot - y(val):.2f}" fill="#000"/>')
        p.append(f'<text x="{x + bw / 2:.2f}" y="{bot + 4.2}" text-anchor="middle" dominant-baseline="central" font-family="Nunito Sans" font-weight="800" font-size="3.6" fill="#000">{nm}</text>')
    if unit: p.append(f'<text x="{(left + right) / 2:.1f}" y="{h - 1.6}" text-anchor="middle" dominant-baseline="central" font-family="Nunito Sans" font-weight="700" font-size="3.2" fill="#000">{unit}</text>')
    return svg(w, h, "".join(p))

def read_bars(s):
    """independent reader: {name: value} from the bar heights and the printed axis numbers"""
    labs = {int(v): float(y) for v, y in re.findall(r'class="axl" data-v="(\d+)" x="[-\d.]+" y="([-\d.]+)"', s)}
    v0 = min(labs); v1 = max(labs)
    y0, y1 = labs[v0], labs[v1]
    out = {}
    for nm, y, h in re.findall(r'class="bar" data-n="([^"]+)" x="[-\d.]+" y="([-\d.]+)" width="[-\d.]+" height="([-\d.]+)"', s):
        out[nm] = round(v0 + (float(h)) / (y0 - y1) * (v1 - v0), 1)
    return out
