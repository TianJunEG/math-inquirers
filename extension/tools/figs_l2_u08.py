"""Figure types for Level 2 unit 8 (2D and 3D shapes).

  l2_cubes      stacks of cubes in an isometric picture.  stacks: [{label?, heights: [[row of heights, ...], ...]}]  (first row is the BACK row, first column is on the left;
                every column is drawn from the table up, so nothing floats).  Top faces are white, left faces white, right faces hatched (print) so each cube can be counted.
  l2_solids     pictures of solids: items [{kind: cube|cuboid|cylinder|cone|sphere, label?}]
  l2_pieces     flat pieces in a row: items of semicircle | quarter | square | triangle, in the given order (to be counted by kind)
  l2_nets       squares joined edge to edge: nets [{label, cells: [[row, col], ...]}]
  l2_trilines   a triangle with `apex` lines from the top corner to the base and `across` lines parallel to the base (for counting triangles)
Palette NAVY / SOFT / SKY / YEL only.
"""
import math
import figs as F
from figs_l2_core import T, box, line, wrap, NAVY, SKY, SOFT, YEL

A = 36           # half width of a cube
L = 41.6         # edge length (A / cos 30)


def _cube(P, px, py, top='#fff', left='#fff', right=YEL):
    """a cube whose top vertex is (px, py)"""
    a, l = A, L
    P.append(f'<polygon points="{px},{py} {px + a},{py + l / 2} {px},{py + l} {px - a},{py + l / 2}" fill="{top}" stroke="{NAVY}" stroke-width="3" stroke-linejoin="round"/>')
    P.append(f'<polygon points="{px - a},{py + l / 2} {px},{py + l} {px},{py + 2 * l} {px - a},{py + 1.5 * l}" fill="{left}" stroke="{NAVY}" stroke-width="3" stroke-linejoin="round"/>')
    P.append(f'<polygon points="{px},{py + l} {px + a},{py + l / 2} {px + a},{py + 1.5 * l} {px},{py + 2 * l}" fill="{right}" stroke="{NAVY}" stroke-width="3" stroke-linejoin="round"/>')


def _box(px, py, nx, ny, nz, sc=1.0):
    """one solid box (cuboid) whose top vertex is (px, py): nx along the right-down edge, ny along the left-down edge, nz high; edge unit = sc"""
    a, l = A * sc, L * sc
    ux, uy = a, l / 2
    vx, vy = -a, l / 2
    T0 = (px, py)
    p1 = (px + nx * ux, py + nx * uy)
    p2 = (p1[0] + ny * vx, p1[1] + ny * vy)
    p3 = (px + ny * vx, py + ny * vy)
    h = nz * l
    pts = lambda *q: ' '.join(f'{x:.1f},{y:.1f}' for x, y in q)
    return [f'<polygon points="{pts(T0, p1, p2, p3)}" fill="#fff" stroke="{NAVY}" stroke-width="3" stroke-linejoin="round"/>',
            f'<polygon points="{pts(p3, p2, (p2[0], p2[1] + h), (p3[0], p3[1] + h))}" fill="#fff" stroke="{NAVY}" stroke-width="3" stroke-linejoin="round"/>',
            f'<polygon points="{pts(p2, p1, (p1[0], p1[1] + h), (p2[0], p2[1] + h))}" fill="{YEL}" stroke="{NAVY}" stroke-width="3" stroke-linejoin="round"/>']


def _stack(heights, ox, oy):
    """draw a stack; returns (svg parts, width, height).  oy is the top of the drawing area"""
    R = len(heights)
    C = max(len(r) for r in heights)
    H = max(max(r) for r in heights)
    # screen position of the top vertex of the cube at (i, j, k): i = column (right-down), j = row index from the back (left-down)
    # use i = column, j = (R - 1 - row) so that the first row is the back row
    cells = []
    for r, row in enumerate(heights):
        for c, h in enumerate(row):
            for k in range(h):
                i, j = c, R - 1 - r          # +i goes right-down, +j goes left-down (front)
                # the back row must be drawn first: smaller i + j first
                cells.append((i + j, k, i, j))
    cells.sort()
    xs = [(i - j) * A for _, _, i, j in cells]
    minx = min(xs) - A
    P = []
    base_x = ox - minx
    ymin = min((i + j) * L / 2 - (k + 1) * L for _, k, i, j in cells)
    for _, k, i, j in cells:
        px = base_x + (i - j) * A
        py = oy - ymin + (i + j) * L / 2 - k * L - L
        _cube(P, px, py)
    width = (max(xs) + A) - (min(xs) - A)
    height = max((i + j) * L / 2 - k * L for _, k, i, j in cells) + 2 * L - ymin - L
    return P, width, height


def cubes(spec, w=None):
    P = []
    x = 8
    built = []
    for st in spec['stacks']:
        pcs, sw, sh = _stack(st['heights'], x, 8)
        built.append((pcs, sw, sh, x, st.get('label')))
        x += sw + 70
    H = max(b[2] for b in built)
    for pcs, sw, sh, xx, lab in built:
        P += pcs
        if lab:
            P.append(T(xx + sw / 2, H + 40, lab, 32))
    return wrap(P, x - 50, H + (60 if any(b[4] for b in built) else 14), 'stacks of cubes', w, 0.2)


def _solid(kind, cx, cy):
    P = []
    if kind == 'cube':
        P += _box(cx, cy - 48, 1, 1, 1, 1.05)
    elif kind == 'cuboid':
        P += _box(cx - 30, cy - 52, 2, 1, 1, 0.95)
    elif kind == 'cylinder':
        P.append(f'<path d="M{cx - 38} {cy - 40} V{cy + 40} A38 14 0 0 0 {cx + 38} {cy + 40} V{cy - 40}" fill="{SOFT}" stroke="{NAVY}" stroke-width="3.2"/>')
        P.append(f'<ellipse cx="{cx}" cy="{cy - 40}" rx="38" ry="14" fill="#fff" stroke="{NAVY}" stroke-width="3.2"/>')
    elif kind == 'cone':
        P.append(f'<path d="M{cx} {cy - 52} L{cx + 42} {cy + 40} A42 15 0 0 1 {cx - 42} {cy + 40} Z" fill="{SOFT}" stroke="{NAVY}" stroke-width="3.2" stroke-linejoin="round"/>')
    elif kind == 'sphere':
        P.append(f'<circle cx="{cx}" cy="{cy}" r="46" fill="{SOFT}" stroke="{NAVY}" stroke-width="3.2"/>')
        P.append(f'<path d="M{cx - 46} {cy} A46 15 0 0 0 {cx + 46} {cy}" fill="none" stroke="{NAVY}" stroke-width="1.8" stroke-dasharray="6 5"/>')
    return P


def solids(spec, w=None):
    P = []
    x = 70
    for it in spec['items']:
        P += _solid(it['kind'], x, 70)
        if it.get('label'):
            P.append(T(x, 150, it['label'], 30))
        x += 150
    return wrap(P, x - 70 + 10, 170, 'solids', w, 0.2)


def _piece(kind, cx, cy, r=34):
    if kind == 'semicircle':
        return f'<path d="M{cx - r} {cy + r / 2} A{r} {r} 0 0 1 {cx + r} {cy + r / 2} Z" fill="{SKY}" stroke="{NAVY}" stroke-width="3.2" stroke-linejoin="round"/>'
    if kind == 'quarter':
        return f'<path d="M{cx - r / 2 - 4} {cy + r / 2 + 4} L{cx - r / 2 - 4} {cy - r / 2 - 4 - 6} A{r + 10} {r + 10} 0 0 1 {cx + r / 2 + 6} {cy + r / 2 + 4} Z" fill="{YEL}" stroke="{NAVY}" stroke-width="3.2" stroke-linejoin="round"/>'
    if kind == 'square':
        return f'<rect x="{cx - r * 0.85}" y="{cy - r * 0.85}" width="{r * 1.7}" height="{r * 1.7}" fill="#fff" stroke="{NAVY}" stroke-width="3.4"/>'
    if kind == 'triangle':
        return f'<path d="M{cx} {cy - r} L{cx + r * 1.05} {cy + r * 0.8} L{cx - r * 1.05} {cy + r * 0.8} Z" fill="{SOFT}" stroke="{NAVY}" stroke-width="3.4" stroke-linejoin="round"/>'
    raise ValueError(kind)


def pieces(spec, w=None):
    items = spec['items']
    per = spec.get('per_row', 6)
    cs = 100
    P = []
    for i, k in enumerate(items):
        r, c = divmod(i, per)
        P.append(_piece(k, 6 + c * cs + cs / 2, 6 + r * cs + cs / 2))
    rows = (len(items) + per - 1) // per
    return wrap(P, min(per, len(items)) * cs + 12, rows * cs + 12, 'pieces', w, 0.2)


def nets(spec, w=None):
    cs = 60
    P = []
    x0 = 8
    maxh = 0
    for n in spec['nets']:
        cells = n['cells']
        mr = max(r for r, c in cells)
        mc = max(c for r, c in cells)
        for r, c in cells:
            P.append(f'<rect x="{x0 + c * cs}" y="{8 + r * cs}" width="{cs}" height="{cs}" fill="{SOFT}" stroke="{NAVY}" stroke-width="3.2"/>')
        P.append(T(x0 + (mc + 1) * cs / 2, 8 + (mr + 1) * cs + 44, n['label'], 34))
        maxh = max(maxh, (mr + 1) * cs)
        x0 += (mc + 1) * cs + 60
    return wrap(P, x0 - 52, maxh + 70, 'nets', w, 0.2)


def trilines(spec, w=None):
    m = spec.get('apex', 2)
    k = spec.get('across', 0)
    W, H = 400, 330
    ax, ay = W / 2, 14
    bl, br = (10, 14 + H), (W - 10, 14 + H)
    P = [f'<polygon points="{ax},{ay} {br[0]},{br[1]} {bl[0]},{bl[1]}" fill="#fff" stroke="{NAVY}" stroke-width="3.6" stroke-linejoin="round"/>']
    for i in range(1, m + 1):
        bx = bl[0] + i * (br[0] - bl[0]) / (m + 1)
        P.append(line(ax, ay, bx, bl[1], 3.4))
    for j in range(1, k + 1):
        t = j / (k + 1)
        y = ay + t * H
        xl = ax + (bl[0] - ax) * t
        xr = ax + (br[0] - ax) * t
        P.append(line(xl, y, xr, y, 3.4))
    return wrap(P, W + 6, H + 40, 'triangle cut by lines', w, 0.2)


FIGS = {'l2_cubes': cubes, 'l2_solids': solids, 'l2_pieces': pieces, 'l2_nets': nets, 'l2_trilines': trilines}
