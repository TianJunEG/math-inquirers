"""Primary 4 pictures: fraction bars, fraction number lines, sets in rings, angle figures, protractors, number rings.
Pure black and white. Every picture has a reader function that recovers its value from the DRAWING only (used by the independent solvers)."""
import math, re
from fractions import Fraction
from .common import svg, obj_g, OBJ_ST
from . import art as _art
from .art import osz, opitch

BLK = 'fill="#000" stroke="#000" stroke-width="0.4"'
OUT = 'fill="#fff" stroke="#000" stroke-width="0.55" stroke-linejoin="round"'

# ---------------------------------------------------------------- fraction bars (shaded parts are inset black rectangles so that touching shaded parts stay apart on a photocopy)
def bar_g(x, y, w, h, d, shaded):
    p = []
    cw = w / d
    for i in range(d):
        p.append(f'<rect class="cell" x="{x + i * cw:.2f}" y="{y:.2f}" width="{cw:.2f}" height="{h:.2f}" {OUT}/>')
        if i < shaded:
            p.append(f'<rect class="on" x="{x + i * cw + 0.9:.2f}" y="{y + 0.9:.2f}" width="{cw - 1.8:.2f}" height="{h - 1.8:.2f}" {BLK}/>')
    return "".join(p)

def bars_svg(d, total_shaded, per_row=3, w=36, h=8.5, gap=3.5):
    """whole bars each cut into d equal parts; total_shaded parts are shaded from the left, bar after bar"""
    nb = -(-total_shaded // d)
    rows = -(-nb // per_row)
    W = min(nb, per_row) * (w + gap) - gap + 1; H = rows * (h + gap) - gap + 1
    p = []; left = total_shaded
    for b in range(nb):
        r, c = divmod(b, per_row)
        k = min(d, left); left -= k
        p.append(bar_g(0.5 + c * (w + gap), 0.5 + r * (h + gap), w, h, d, k))
    return svg(round(W, 1), round(H, 1), "".join(p))

def read_bars(s):
    """independent reader: (parts in one whole bar, parts shaded in all, number of bars)"""
    cells = re.findall(r'<rect class="cell" x="([\d.]+)" y="([\d.]+)" width="([\d.]+)"', s)
    ys = sorted({y for _, y, _ in cells}); xs = sorted({x for x, _, _ in cells}, key=float)
    # parts in one bar: cells that share one y and are joined edge to edge
    rows = {}
    for x, y, w in cells: rows.setdefault(y, []).append((float(x), float(w)))
    bars = []
    for y, lst in rows.items():
        lst.sort(); cur = [lst[0]]
        for a in lst[1:]:
            if abs(a[0] - (cur[-1][0] + cur[-1][1])) < 0.05: cur.append(a)
            else: bars.append(cur); cur = [a]
        bars.append(cur)
    d = len(bars[0])
    return d, len(re.findall(r'<rect class="on"', s)), len(bars)

# ---------------------------------------------------------------- fraction number line
NL_W = 26.0           # mm for one unit

def numline_svg(a, d, value, units=3):
    """a number line from whole number a to a+units (labelled at the whole numbers), ticks every 1/d, an arrow above the position `value` (Fraction)"""
    x0 = 6.0; y = 11.0
    W = x0 * 2 + units * NL_W
    p = [f'<line x1="{x0}" y1="{y}" x2="{x0 + units * NL_W}" y2="{y}" stroke="#000" stroke-width="0.6"/>']
    for k in range(units * d + 1):
        x = x0 + k * NL_W / d; whole = k % d == 0
        p.append(f'<line class="tick" x1="{x:.2f}" y1="{y - (3.2 if whole else 1.8):.2f}" x2="{x:.2f}" y2="{y + (3.2 if whole else 1.8):.2f}" stroke="#000" stroke-width="{0.6 if whole else 0.45}"/>')
        if whole: p.append(f'<text class="lab" x="{x:.2f}" y="{y + 8.2:.2f}" text-anchor="middle" font-family="Fredoka" font-weight="600" font-size="4.4" fill="#000">{a + k // d}</text>')
    px = x0 + float(value - a) * NL_W
    p.append(f'<polygon class="ptr" points="{px - 2:.2f},1.5 {px + 2:.2f},1.5 {px:.2f},{y - 3.6:.2f}" fill="#000" stroke="#000" stroke-width="0.3"/>')
    return svg(round(W, 1), 20, "".join(p))

def read_numline(s):
    """independent reader: the value (Fraction) the arrow points at, from the drawing"""
    ticks = sorted(float(x) for x in re.findall(r'class="tick" x1="([\d.]+)"', s))
    labs = [(float(x), int(v)) for x, v in re.findall(r'class="lab" x="([\d.]+)"[^>]*>(\d+)<', s)]
    pts = re.search(r'class="ptr" points="([\d.]+),[\d.]+ ([\d.]+),[\d.]+ ([\d.]+),', s)
    px = float(pts.group(3))
    unit = labs[1][0] - labs[0][0]
    d = round(unit / (ticks[1] - ticks[0]))
    k = round((px - labs[0][0]) / (unit / d))
    return Fraction(labs[0][1]) + Fraction(k, d)

# ---------------------------------------------------------------- sets of objects in rings
def groups_svg(kind, per_group, ngroups, per_row=None):
    """ngroups rings, each holding per_group objects (a ring is a rounded rectangle); returns svg"""
    size = osz(kind); pitch = opitch(kind)
    cols = per_row or per_group
    gw = cols * pitch + 2.4; rows_g = -(-per_group // cols); gh = rows_g * pitch + 2.4
    W = ngroups * (gw + 3) - 3 + 1; H = gh + 1
    p = []
    for g in range(ngroups):
        gx = 0.5 + g * (gw + 3)
        p.append(f'<rect class="ring" x="{gx:.2f}" y="0.5" width="{gw:.2f}" height="{gh:.2f}" rx="3.5" fill="#fff" stroke="#000" stroke-width="0.55"/>')
        for i in range(per_group):
            r, c = divmod(i, cols)
            p.append(obj_g(kind, gx + 1.2 + c * pitch, 1.7 + r * pitch, size))
    return svg(round(W, 1), round(H, 1), "".join(p))

def read_groups(s):
    return len(re.findall(r'class="ring"', s)), len(re.findall(r'class="obj"', s))

# ---------------------------------------------------------------- angles
def pol(cx, cy, r, deg):
    a = math.radians(deg); return cx + r * math.cos(a), cy - r * math.sin(a)

def angle_fig_svg(vertex, rays, marks, size=(60, 40), R=24):
    """rays: {label: degrees (anticlockwise from the right)}; marks: [(label_of_arc, ray1, ray2, radius)] each drawn as an arc with the small letter inside.
    The vertex letter is printed beside the vertex."""
    W, H = size; cx, cy = W / 2, H - 6
    p = []
    for lab, deg in rays.items():
        x, y = pol(cx, cy, R, deg); tx, ty = pol(cx, cy, R + 4.2, deg)
        p.append(f'<line class="ray" data-l="{lab}" x1="{cx}" y1="{cy}" x2="{x:.2f}" y2="{y:.2f}" stroke="#000" stroke-width="0.6"/>')
        p.append(f'<text class="pt" data-l="{lab}" x="{tx:.2f}" y="{ty:.2f}" text-anchor="middle" dominant-baseline="central" font-family="Fredoka" font-weight="600" font-size="4.6" fill="#000">{lab}</text>')
    for small, r1, r2, rad in marks:
        a1, a2 = sorted((rays[r1], rays[r2]))
        xa, ya = pol(cx, cy, rad, a1); xb, yb = pol(cx, cy, rad, a2)
        p.append(f'<path class="arc" data-a="{small}" data-from="{r1}" data-to="{r2}" d="M{xa:.2f},{ya:.2f} A{rad},{rad} 0 0 0 {xb:.2f},{yb:.2f}" fill="none" stroke="#000" stroke-width="0.6"/>')
        if small:
            cands = [(a1 + a2) / 2, a1 + 0.22 * (a2 - a1), a1 + 0.78 * (a2 - a1)]
            best = max(cands, key=lambda c: min(abs(c - d) for d in rays.values()))        # keep the small letter clear of any ray inside the arc
            tx, ty = pol(cx, cy, rad + 3.4, best)
            p.append(f'<text class="small" data-a="{small}" x="{tx:.2f}" y="{ty:.2f}" text-anchor="middle" dominant-baseline="central" font-family="Fredoka" font-weight="600" font-size="4.4" fill="#000">{small}</text>')
    p.append(f'<text class="vtx" x="{cx - 3.3:.2f}" y="{cy + 3.2:.2f}" text-anchor="middle" dominant-baseline="central" font-family="Fredoka" font-weight="600" font-size="4.6" fill="#000">{vertex}</text>')
    return svg(W, H, "".join(p))

def read_angle_fig(s):
    """independent reader, from the coordinates only: (vertex letter, {ray label: degrees}, [(small letter or '', label of the ray at one end of the arc, label at the other end)]).
    A ray's label is the printed letter nearest to the end of the ray."""
    rays = {}; ends = {}
    lines = re.findall(r'class="ray" data-l="\w" x1="([\d.]+)" y1="([\d.]+)" x2="([\d.]+)" y2="([\d.]+)"', s)
    cx, cy = float(lines[0][0]), float(lines[0][1])
    texts = [(c, float(x), float(y)) for x, y, c in re.findall(r'class="pt" data-l="\w" x="([\d.]+)" y="([\d.]+)"[^>]*>(\w)<', s)]
    for x1, y1, x2, y2 in lines:
        x2, y2 = float(x2), float(y2)
        lab = min(texts, key=lambda t: (t[1] - x2) ** 2 + (t[2] - y2) ** 2)[0]
        rays[lab] = math.degrees(math.atan2(cy - y2, x2 - cx))
    arcs = []
    def near(deg): return min(rays, key=lambda l: abs(rays[l] - deg))
    for m in re.finditer(r'class="arc" data-a="(\w*)" data-from="\w" data-to="\w" d="M([\d.]+),([\d.]+) A([\d.]+),[\d.]+ 0 0 0 ([\d.]+),([\d.]+)"', s):
        xa, ya, xb, yb = float(m[2]), float(m[3]), float(m[5]), float(m[6])
        arcs.append((m[1], near(math.degrees(math.atan2(cy - ya, xa - cx))), near(math.degrees(math.atan2(cy - yb, xb - cx)))))
    v = re.search(r'class="vtx"[^>]*>(\w)<', s)[1]
    return v, rays, arcs

# ---------------------------------------------------------------- protractor
def protractor_svg(angle, base="right", R=28.0, size=72):
    """a protractor (outer scale 0 to 180 from the right, inner scale 0 to 180 from the left, a tick every 5 degrees, numbers every 20 degrees on both scales, all printed along the radius) with an angle drawn from its centre.
    base='right': the arm along the base points to the right and the other arm is `angle` degrees above it; base='left': the base arm points to the left."""
    W = size; H = R + 4.5 + 15.0; cx = W / 2; cy = R + 4.5
    Ri = R - 12.5
    p = [f'<path d="M{cx - R:.2f},{cy:.2f} A{R},{R} 0 0 1 {cx + R:.2f},{cy:.2f} Z" fill="#fff" stroke="#000" stroke-width="0.55"/>']
    p.append(f'<path d="M{cx - Ri:.2f},{cy:.2f} A{Ri},{Ri} 0 0 1 {cx + Ri:.2f},{cy:.2f}" fill="none" stroke="#000" stroke-width="0.35"/>')
    def label(k, r, txt):
        lx, ly = pol(cx, cy, r, k)
        rot = -k if k <= 90 else 180 - k
        return (f'<text x="{lx:.2f}" y="{ly:.2f}" transform="rotate({rot} {lx:.2f} {ly:.2f})" text-anchor="middle" dominant-baseline="central" '
                f'font-family="Nunito Sans" font-weight="700" font-size="3.3" fill="#000">{txt}</text>')
    for k in range(0, 181, 5):
        major = k % 10 == 0
        x1, y1 = pol(cx, cy, R, k); x2, y2 = pol(cx, cy, R - (3.0 if major else 1.7), k)
        p.append(f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" stroke="#000" stroke-width="{0.5 if major else 0.35}"/>')
        x3, y3 = pol(cx, cy, Ri, k); x4, y4 = pol(cx, cy, Ri + (3.0 if major else 1.7), k)
        p.append(f'<line x1="{x3:.2f}" y1="{y3:.2f}" x2="{x4:.2f}" y2="{y4:.2f}" stroke="#000" stroke-width="{0.5 if major else 0.35}"/>')
        if k % 20 == 0 and k not in (0, 180): p.append(label(k, R - 5.9, k))
        if k % 20 == 0 and 40 <= k <= 140: p.append(label(k, Ri - 5.0, 180 - k))
    def flat(x, y, txt):
        return (f'<text x="{x:.2f}" y="{y:.2f}" text-anchor="middle" dominant-baseline="central" font-family="Nunito Sans" font-weight="700" font-size="3.0" fill="#000">{txt}</text>')
    p.append(flat(cx + R - 4.2, cy - 2.6, 0)); p.append(flat(cx - R + 4.6, cy - 2.6, 180))          # outer scale: 0 at the right end, 180 at the left end
    p.append(flat(cx - Ri + 4.2, cy - 2.6, 0)); p.append(flat(cx + Ri - 4.6, cy - 2.6, 180))        # inner scale: 0 at the left end, 180 at the right end
    p.append(f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r="0.9" fill="#000"/>')
    if base == "right": a_base, a_other = 0, angle
    else: a_base, a_other = 180, 180 - angle
    bx, by = pol(cx, cy, R + 4.0, a_base); ox, oy = pol(cx, cy, R + 4.0, a_other)
    p.append(f'<line class="base" x1="{cx:.2f}" y1="{cy:.2f}" x2="{bx:.2f}" y2="{by:.2f}" stroke="#000" stroke-width="1.0"/>')
    p.append(f'<line class="arm" x1="{cx:.2f}" y1="{cy:.2f}" x2="{ox:.2f}" y2="{oy:.2f}" stroke="#000" stroke-width="1.0"/>')
    return svg(W, round(H, 1), "".join(p))

def read_protractor(s):
    """independent reader: the angle between the two arms, from their end points"""
    b = re.search(r'class="base" x1="([\d.]+)" y1="([\d.]+)" x2="([\d.]+)" y2="([\d.]+)"', s)
    o = re.search(r'class="arm" x1="([\d.]+)" y1="([\d.]+)" x2="([\d.]+)" y2="([\d.]+)"', s)
    def ang(m): return math.degrees(math.atan2(float(m[2]) - float(m[4]), float(m[3]) - float(m[1])))
    d = abs(ang(b) - ang(o)) % 360
    return round(d if d <= 180 else 360 - d)

# ---------------------------------------------------------------- number ring (loop)
RING_W, RING_H = 170.0, 118.0

def ring_svg(vals, ops):
    """six nodes round an oval, the first a circle holding the start number and five empty boxes (the pupil writes v1..v5); an arrow with an operation between each
    pair of nodes, the last arrow back to the start. vals: list of 6 ints (only vals[0] is printed); ops: list of 6 strings like '×6' or '÷3'."""
    cx, cy, rx, ry = RING_W / 2, RING_H / 2, 62.0, 39.0
    n = 6; R = 11.2; HW, HH = 12.5, 6.4
    pos = [(cx + rx * math.sin(2 * math.pi * k / n), cy - ry * math.cos(2 * math.pi * k / n)) for k in range(n)]
    def edge(k, ux, uy):
        """distance from the centre of node k to its edge along the unit vector (ux, uy)"""
        if k == 0: return R
        tx = HW / abs(ux) if abs(ux) > 1e-9 else 1e9; ty = HH / abs(uy) if abs(uy) > 1e-9 else 1e9
        return min(tx, ty)
    p = []
    for k in range(n):
        j = (k + 1) % n
        x1, y1 = pos[k]; x2, y2 = pos[j]
        dx, dy = x2 - x1, y2 - y1; L = math.hypot(dx, dy); ux, uy = dx / L, dy / L
        s0 = edge(k, ux, uy) + 1.4; e0 = L - edge(j, ux, uy) - 1.6
        sx, sy = x1 + ux * s0, y1 + uy * s0; ex, ey = x1 + ux * e0, y1 + uy * e0
        p.append(f'<line x1="{sx:.2f}" y1="{sy:.2f}" x2="{ex - ux * 2.4:.2f}" y2="{ey - uy * 2.4:.2f}" stroke="#000" stroke-width="0.7"/>')
        nx, ny = -uy, ux
        p.append(f'<polygon points="{ex:.2f},{ey:.2f} {ex - ux * 3.8 + nx * 2.0:.2f},{ey - uy * 3.8 + ny * 2.0:.2f} {ex - ux * 3.8 - nx * 2.0:.2f},{ey - uy * 3.8 - ny * 2.0:.2f}" fill="#000"/>')
        mx, my = (sx + ex) / 2, (sy + ey) / 2
        ox, oy = mx - cx, my - cy; ol = math.hypot(ox, oy); lx, ly = mx + ox / ol * 7.0, my + oy / ol * 5.6
        p.append(f'<rect x="{lx - 7:.2f}" y="{ly - 3.6:.2f}" width="14" height="7.2" rx="1.6" fill="#fff" stroke="#000" stroke-width="0.45"/>'
                 f'<text class="rop" data-k="{k}" x="{lx:.2f}" y="{ly:.2f}" text-anchor="middle" dominant-baseline="central" font-family="Fredoka" font-weight="600" font-size="5.2" fill="#000">{ops[k]}</text>')
    for k in range(n):
        x, y = pos[k]
        if k == 0:
            p.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{R}" fill="#fff" stroke="#000" stroke-width="1.0"/>')
            p.append(f'<text class="given" x="{x:.2f}" y="{y:.2f}" text-anchor="middle" dominant-baseline="central" font-family="Fredoka" font-weight="700" font-size="{6.2 if vals[0] < 1000 else 5.0}" fill="#000">{vals[0]}</text>')
        else:
            p.append(f'<rect class="blank" data-k="{k}" x="{x - HW:.2f}" y="{y - HH:.2f}" width="{2 * HW}" height="{2 * HH}" rx="2" fill="#fff" stroke="#000" stroke-width="0.6"/>')
    p.append(f'<text x="{cx:.2f}" y="{cy:.2f}" text-anchor="middle" dominant-baseline="central" font-family="Nunito Sans" font-weight="700" font-size="4.6" fill="#000">start here</text>')
    return svg(RING_W, RING_H, "".join(p))

def read_ring(s):
    """independent reader: (start number, the six operations as (sign, number)) from the drawing"""
    g = int(re.search(r'class="given"[^>]*>(\d+)<', s)[1])
    ops = [re.search(r'class="rop" data-k="%d"[^>]*>(.*?)<' % k, s)[1] for k in range(6)]
    return g, [(o[0], int(o[1:])) for o in ops]
