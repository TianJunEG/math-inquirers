"""Primary 4 pictures, part 2: dot-grid corners, mirror figures, symmetry grids, solids and nets. Pure black and white.
Every picture has a reader that recovers its facts from the DRAWING only (used by the independent solvers)."""
import math, re, itertools
from shapely.geometry import Polygon, LineString, Point
from shapely import affinity
from .common import svg

ST = 'fill="#fff" stroke="#000" stroke-width="0.6" stroke-linejoin="round" stroke-linecap="round"'
DASH = 'fill="none" stroke="#000" stroke-width="0.45" stroke-dasharray="1.2 0.9"'

# ---------------------------------------------------------------- dot-grid corners (rectangles and squares)
G = 5.2           # mm between dots

def corner_svg(n, c0, c1, c2, cands):
    """an n by n grid of dots; the arms c1-c0 and c0-c2 drawn; the three corners marked; candidate points ringed with their letters. cands: [(gx, gy, letter)]"""
    W = (n - 1) * G + 8; H = (n - 1) * G + 8; o = 4.0
    P = lambda g: (o + g[0] * G, o + g[1] * G)
    p = []
    for i in range(n):
        for j in range(n):
            x, y = P((i, j)); p.append(f'<circle class="gpt" cx="{x:.2f}" cy="{y:.2f}" r="0.55" fill="#000"/>')
    a, b, c = P(c1), P(c0), P(c2)
    p.append(f'<polyline class="arms" points="{a[0]:.2f},{a[1]:.2f} {b[0]:.2f},{b[1]:.2f} {c[0]:.2f},{c[1]:.2f}" fill="none" stroke="#000" stroke-width="0.9" stroke-linejoin="miter" stroke-linecap="round"/>')
    for q in (a, b, c): p.append(f'<circle class="corner" cx="{q[0]:.2f}" cy="{q[1]:.2f}" r="1.25" fill="#000"/>')
    for gx, gy, L in cands:
        x, y = P((gx, gy))
        p.append(f'<circle class="cand" cx="{x:.2f}" cy="{y:.2f}" r="2.5" fill="#fff" stroke="#000" stroke-width="0.5"/>'
                 f'<text class="cl2" x="{x:.2f}" y="{y:.2f}" text-anchor="middle" dominant-baseline="central" font-family="Nunito Sans" font-weight="800" font-size="3.4" fill="#000">{L}</text>')
    return svg(round(W, 1), round(H, 1), "".join(p))

def read_corner(s):
    """independent reader: (corner points of the two arms in mm: p1, p0, p2, candidates [(x, y, letter)])"""
    m = re.search(r'class="arms" points="([\d.]+),([\d.]+) ([\d.]+),([\d.]+) ([\d.]+),([\d.]+)"', s)
    pts = [(float(m[1]), float(m[2])), (float(m[3]), float(m[4])), (float(m[5]), float(m[6]))]
    cands = [(float(x), float(y), t) for x, y, t in re.findall(r'class="cand" cx="([\d.]+)" cy="([\d.]+)"[^>]*/><text class="cl2"[^>]*>(\w)</text>', s)]
    return pts, cands

# ---------------------------------------------------------------- mirror figures
def mirror_svg(poly, axis=None, size=(46, 34)):
    """a figure (polygon points in mm inside size) and optionally a dashed line (two points, drawn a little beyond its ends)"""
    W, H = size
    p = [f'<polygon class="fig" points="{" ".join(f"{x:.2f},{y:.2f}" for x, y in poly)}" fill="#fff" stroke="#000" stroke-width="0.7" stroke-linejoin="round"/>']
    if axis:
        (x1, y1), (x2, y2) = axis; dx, dy = x2 - x1, y2 - y1; L = math.hypot(dx, dy); ux, uy = dx / L, dy / L
        e = 3.0
        p.append(f'<line class="axis" x1="{x1 - ux * e:.2f}" y1="{y1 - uy * e:.2f}" x2="{x2 + ux * e:.2f}" y2="{y2 + uy * e:.2f}" stroke="#000" stroke-width="0.6" stroke-dasharray="2.2 1.4"/>')
    return svg(W, H, "".join(p))

def read_mirror(s):
    poly = [tuple(map(float, q.split(","))) for q in re.search(r'class="fig" points="([^"]+)"', s)[1].split()]
    m = re.search(r'class="axis" x1="([\d.\-]+)" y1="([\d.\-]+)" x2="([\d.\-]+)" y2="([\d.\-]+)"', s)
    axis = ((float(m[1]), float(m[2])), (float(m[3]), float(m[4]))) if m else None
    return poly, axis

def reflect(poly, a, b):
    """the polygon reflected in the line through a and b"""
    (x1, y1), (x2, y2) = a, b; dx, dy = x2 - x1, y2 - y1; L2 = dx * dx + dy * dy
    out = []
    for x, y in poly:
        t = ((x - x1) * dx + (y - y1) * dy) / L2; fx, fy = x1 + t * dx, y1 + t * dy
        out.append((2 * fx - x, 2 * fy - y))
    return out

def is_symmetric_about(poly, a, b, tol=0.012):
    P0 = Polygon(poly); P1 = Polygon(reflect(poly, a, b))
    return P0.symmetric_difference(P1).area < tol * P0.area

def has_line_of_symmetry(poly):
    P0 = Polygon(poly); c = P0.centroid
    for deg in range(0, 180):
        t = math.radians(deg); a = (c.x, c.y); b = (c.x + math.cos(t), c.y + math.sin(t))
        if is_symmetric_about(poly, a, b): return True
    return False

# ---------------------------------------------------------------- symmetry grids
def symm_svg(ncols, nrows, on, axis, cell=5.2):
    """a grid of squares with the shaded squares of one side of a dashed line; axis = ('v', k) the line is between column k-1 and k (k columns on its left), or ('h', k)"""
    o = 7.0
    W = o + ncols * cell + 2; H = nrows * cell + 5.5
    p = []
    for r in range(nrows):
        p.append(f'<text class="rn" x="{o - 2.0:.2f}" y="{3 + r * cell + cell / 2 + 0.2:.2f}" text-anchor="end" dominant-baseline="central" font-family="Nunito Sans" font-weight="800" font-size="3.3" fill="#000">{r + 1}</text>')
    for c in range(ncols):
        p.append(f'<text class="cn" x="{o + c * cell + cell / 2:.2f}" y="{3 + nrows * cell + 2.4:.2f}" text-anchor="middle" dominant-baseline="central" font-family="Nunito Sans" font-weight="800" font-size="3.3" fill="#000">{c + 1}</text>')
    for r in range(nrows):
        for c in range(ncols):
            x, y = o + c * cell, 3 + r * cell
            p.append(f'<rect class="c" x="{x:.2f}" y="{y:.2f}" width="{cell}" height="{cell}" fill="#fff" stroke="#000" stroke-width="0.35"/>')
            if (r, c) in on: p.append(f'<rect class="on" x="{x + 0.55:.2f}" y="{y + 0.55:.2f}" width="{cell - 1.1}" height="{cell - 1.1}" fill="#000"/>')
    kind, k = axis
    if kind == "v": x = o + k * cell; p.append(f'<line class="axis" x1="{x:.2f}" y1="1" x2="{x:.2f}" y2="{3 + nrows * cell + 0.5:.2f}" stroke="#000" stroke-width="0.9" stroke-dasharray="2.4 1.4"/>')
    else: y = 3 + k * cell; p.append(f'<line class="axis" x1="{o - 1:.2f}" y1="{y:.2f}" x2="{o + ncols * cell + 1:.2f}" y2="{y:.2f}" stroke="#000" stroke-width="0.9" stroke-dasharray="2.4 1.4"/>')
    return svg(round(W, 1), round(H, 1), "".join(p))

def read_symm(s):
    """independent reader: (columns, rows, shaded cells {(row, col)}, axis ('v' or 'h', number of columns or rows before the line))"""
    cells = re.findall(r'class="c" x="([\d.]+)" y="([\d.]+)" width="([\d.]+)"', s)
    cell = float(cells[0][2]); xs = sorted({round(float(x), 2) for x, y, w in cells}); ys = sorted({round(float(y), 2) for x, y, w in cells})
    on = set()
    for x, y in re.findall(r'class="on" x="([\d.]+)" y="([\d.]+)"', s):
        on.add((ys.index(min(ys, key=lambda v: abs(v - (float(y) - 0.55)))), xs.index(min(xs, key=lambda v: abs(v - (float(x) - 0.55))))))
    m = re.search(r'class="axis" x1="([\d.]+)" y1="([\d.]+)" x2="([\d.]+)" y2="([\d.]+)"', s)
    if abs(float(m[1]) - float(m[3])) < 0.01: axis = ("v", round((float(m[1]) - xs[0]) / cell))
    else: axis = ("h", round((float(m[2]) - ys[0]) / cell))
    return len(xs), len(ys), on, axis

def mirror_cells(on, ncols, nrows, axis):
    kind, k = axis; out = set(on)
    for r, c in on:
        if kind == "v": out.add((r, 2 * k - 1 - c))
        else: out.add((2 * k - 1 - r, c))
    return out

# ---------------------------------------------------------------- solids (oblique drawings)
def solid_svg(kind, w=16.0, h=16.0, d=16.0):
    """cube, cuboid, cylinder, cone, triangular prism (lying on a rectangular face) and square pyramid, drawn in oblique view"""
    pts = lambda *p: " ".join(f"{a:.2f},{b:.2f}" for a, b in p)
    if kind in ("cube", "cuboid"):
        if kind == "cube": h = d = w
        ox, oy = 0.45 * d, -0.45 * d; x, y = 2.0, 2.0 - oy
        inner = (f'<polygon class="face" points="{pts((x, y), (x + w, y), (x + w, y + h), (x, y + h))}" {ST}/>'
                 f'<polygon class="face" points="{pts((x, y), (x + w, y), (x + w + ox, y + oy), (x + ox, y + oy))}" {ST}/>'
                 f'<polygon class="face" points="{pts((x + w, y), (x + w, y + h), (x + w + ox, y + h + oy), (x + w + ox, y + oy))}" {ST}/>')
        return svg(round(w + ox + 4, 1), round(h - oy + 4, 1), inner)
    if kind == "cylinder":
        rx, ry = w / 2, w / 5.0; cx = 2.0 + rx; top = 2.0 + ry; bot = top + h
        body = f'<path d="M{cx - rx:.2f},{top:.2f} L{cx - rx:.2f},{bot:.2f} A{rx:.2f},{ry:.2f} 0 0 0 {cx + rx:.2f},{bot:.2f} L{cx + rx:.2f},{top:.2f}" {ST}/>'
        return svg(round(w + 4, 1), round(h + 2 * ry + 4, 1), body + f'<ellipse class="rim" cx="{cx:.2f}" cy="{top:.2f}" rx="{rx:.2f}" ry="{ry:.2f}" {ST}/>')
    if kind == "cone":
        rx, ry = w / 2, w / 5.0; cx = 2.0 + rx; apex = 2.0; base = apex + h
        inner = (f'<path d="M{cx - rx:.2f},{base:.2f} A{rx:.2f},{ry:.2f} 0 0 0 {cx + rx:.2f},{base:.2f}" {DASH}/>'
                 f'<polygon class="cone" points="{pts((cx, apex), (cx - rx, base), (cx + rx, base))}" {ST}/><ellipse class="rim" cx="{cx:.2f}" cy="{base:.2f}" rx="{rx:.2f}" ry="{ry:.2f}" {ST}/>')
        return svg(round(w + 4, 1), round(h + ry + 4, 1), inner)
    if kind == "prism":
        # a triangular prism lying on a rectangular face: the front triangle and the two sloping rectangles (shallow roof so that both slopes are seen)
        ox, oy = 0.45 * d, -0.45 * d; x, y = 2.0, 2.0 + h - oy
        A, B, C = (x, y), (x + w, y), (x + w / 2, y - h)
        A2, B2, C2 = (A[0] + ox, A[1] + oy), (B[0] + ox, B[1] + oy), (C[0] + ox, C[1] + oy)
        inner = (f'<polygon class="face" points="{pts(A, C, C2, A2)}" {ST}/><polygon class="face" points="{pts(C, B, B2, C2)}" {ST}/><polygon class="face" points="{pts(A, B, C)}" {ST}/>')
        return svg(round(w + ox + 4, 1), round(h - oy + 4, 1), inner)
    if kind == "pyramid":
        ox, oy = 0.5 * d, -0.5 * d * 0.55; x, y = 2.0, 2.0 + h - oy
        P1, P2, P3, P4 = (x, y), (x + w, y), (x + w + ox, y + oy), (x + ox, y + oy)
        apex = (x + w / 2 + ox / 2, y - h + oy / 2)
        inner = (f'<path d="M{P1[0]:.2f},{P1[1]:.2f} L{P4[0]:.2f},{P4[1]:.2f} L{P3[0]:.2f},{P3[1]:.2f} M{P4[0]:.2f},{P4[1]:.2f} L{apex[0]:.2f},{apex[1]:.2f}" {DASH}/>'
                 f'<polygon class="face" points="{pts(P1, P2, apex)}" {ST}/><polygon class="face" points="{pts(P2, P3, apex)}" {ST}/>')
        return svg(round(w + ox + 4, 1), round(h - oy + 4, 1), inner)
    raise ValueError(kind)

def read_solid(s):
    """independent reader: the solid from its drawn primitives (faces by number of corners, ellipses, apex)"""
    polys = re.findall(r'<polygon class="(face|cone)" points="([^"]+)"', s)
    if any(c == "cone" for c, _ in polys): return "cone"
    if 'class="rim"' in s: return "cylinder"
    P_ = [[tuple(map(float, q.split(","))) for q in pts.split()] for _, pts in polys]
    tri = [p for p in P_ if len(p) == 3]; quad = [p for p in P_ if len(p) == 4]
    if len(tri) == 2 and not quad: return "square pyramid"
    if len(tri) == 1 and len(quad) == 2: return "triangular prism"
    if len(quad) == 3 and not tri:
        front = quad[0]; w = front[1][0] - front[0][0]; h = front[2][1] - front[1][1]
        return "cube" if abs(w - h) < 0.2 else "cuboid"
    raise ValueError(s[:80])

# ---------------------------------------------------------------- nets
CELL = 7.2

def cube_net_ok(cells):
    """does this set of six squares fold into a cube? A cube rolled over the net must touch the six cells with its six different faces"""
    cells = set(cells); start = sorted(cells)[0]
    # faces: 0 top, 1 bottom, 2 north, 3 south, 4 east, 5 west
    state = (0, 1, 2, 3, 4, 5); seen = {start: state}; touched = {state[1]}
    queue = [start]
    def roll(st, d):
        T, B, N, S, E, W = st
        if d == (1, 0): return (W, E, N, S, T, B)       # east
        if d == (-1, 0): return (E, W, N, S, B, T)      # west
        if d == (0, -1): return (S, N, T, B, E, W)      # north (row decreases)
        return (N, S, B, T, E, W)                       # south
    while queue:
        cur = queue.pop(0)
        for d in ((1, 0), (-1, 0), (0, -1), (0, 1)):
            nb = (cur[0] + d[0], cur[1] + d[1])
            if nb in cells and nb not in seen:
                ns = roll(seen[cur], d); seen[nb] = ns
                if ns[1] in touched: return False
                touched.add(ns[1]); queue.append(nb)
    return len(touched) == 6

def net_svg(faces):
    """faces: list of polygons in mm; draws each as a closed outline (class nf)"""
    xs = [x for f in faces for x, y in f]; ys = [y for f in faces for x, y in f]
    ox, oy = 2.0 - min(xs), 2.0 - min(ys)
    p = [f'<polygon class="nf" points="{" ".join(f"{x + ox:.2f},{y + oy:.2f}" for x, y in f)}" fill="#fff" stroke="#000" stroke-width="0.7" stroke-linejoin="round"/>' for f in faces]
    return svg(round(max(xs) - min(xs) + 4, 1), round(max(ys) - min(ys) + 4, 1), "".join(p))

def squares_net(cells, cell=CELL):
    return [[(c * cell, r * cell), ((c + 1) * cell, r * cell), ((c + 1) * cell, (r + 1) * cell), (c * cell, (r + 1) * cell)] for (c, r) in sorted(cells)]

def cuboid_net(w=4, h=2, d=3, u=4.2):
    """a cross-shaped net of a cuboid w by h by d (units of u mm)"""
    R = lambda x0, y0, x1, y1: [(x0 * u, y0 * u), (x1 * u, y0 * u), (x1 * u, y1 * u), (x0 * u, y1 * u)]
    return [R(0, d, d, d + h), R(d, d, d + w, d + h), R(d + w, d, 2 * d + w, d + h), R(2 * d + w, d, 2 * d + 2 * w, d + h), R(d, 0, d + w, d), R(d, d + h, d + w, 2 * d + h)]

def prism_net(b=3, L=4, u=5.0):
    """three rectangles b by L side by side and a triangle (base b, height 0.87 b) above and below the middle one"""
    R = lambda x0, y0, x1, y1: [(x0 * u, y0 * u), (x1 * u, y0 * u), (x1 * u, y1 * u), (x0 * u, y1 * u)]
    ht = 0.866 * b
    return [R(0, ht, b, ht + L), R(b, ht, 2 * b, ht + L), R(2 * b, ht, 3 * b, ht + L),
            [(b * u, ht * u), (2 * b * u, ht * u), (1.5 * b * u, 0)], [(b * u, (ht + L) * u), (2 * b * u, (ht + L) * u), (1.5 * b * u, (2 * ht + L) * u)]]

def pyramid_net(s=3, u=5.0):
    """a square s by s with an isosceles triangle (base s, height s) on each side"""
    sq = [(s * u, s * u), (2 * s * u, s * u), (2 * s * u, 2 * s * u), (s * u, 2 * s * u)]
    return [sq, [(s * u, s * u), (2 * s * u, s * u), (1.5 * s * u, 0)], [(2 * s * u, s * u), (2 * s * u, 2 * s * u), (3 * s * u, 1.5 * s * u)],
            [(s * u, 2 * s * u), (2 * s * u, 2 * s * u), (1.5 * s * u, 3 * s * u)], [(s * u, s * u), (s * u, 2 * s * u), (0, 1.5 * s * u)]]

def read_net(s):
    """independent reader: the faces of a net by kind, and the solid it makes. Six squares are folded over a cube to see whether they make one."""
    faces = [[tuple(map(float, q.split(","))) for q in m.split()] for m in re.findall(r'class="nf" points="([^"]+)"', s)]
    def is_square(f):
        if len(f) != 4: return False
        d = [math.dist(f[i], f[(i + 1) % 4]) for i in range(4)]
        return max(d) - min(d) < 0.05
    sq = [f for f in faces if is_square(f)]; tri = [f for f in faces if len(f) == 3]; rect = [f for f in faces if len(f) == 4 and not is_square(f)]
    if len(sq) == 6:
        cell = min(math.dist(f[0], f[1]) for f in sq)
        cells = {(round(f[0][0] / cell), round(f[0][1] / cell)) for f in sq}
        return "cube" if cube_net_ok(cells) else "no solid"
    if len(rect) == 6 and not tri: return "cuboid"
    if len(tri) == 2 and len(rect) == 3: return "triangular prism"
    if len(tri) == 4 and len(sq) == 1: return "square pyramid"
    return "no solid"
