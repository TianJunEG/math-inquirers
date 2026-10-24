"""Shared helpers for the Level 3 (P3) holiday online practice, WEEK 4 (lessons 7 and 8): figures drawn larger than the printed ones (one angle, one shape, one letter per
card) from the SAME data as the workbook's own figures (the build checks that the data equals the printed figures, via figs_p3_w4.js), and small exact-arithmetic helpers
for the INDEPENDENT checkers (area and perimeter of squares-figures and polygons, right angles inside a polygon, right angles where lines meet, parallel and perpendicular
pairs of lines, the clock hands).  Imported by p3/07/lesson.py and p3/08/lesson.py (after `from hlib import *`)."""
import itertools, json, os, re, subprocess
from fractions import Fraction as Fr
from math import cos, sin, radians

HERE = os.path.dirname(os.path.abspath(__file__))
_f4 = None


def figs4():
    """{'printed': {name: svg}, 'data': {...}} from the workbook's own generator functions (node, figs_p3_w4.js)."""
    global _f4
    if _f4 is None:
        _f4 = json.loads(subprocess.check_output(['node', os.path.join(HERE, 'figs_p3_w4.js')], text=True))
    return _f4


def _h():
    import sys
    sys.path.insert(0, os.path.join(HERE, '..'))
    import hlib
    return hlib


SKY, GRIDC, PURPLE, BLUE2 = '#DDEBF7', '#B9C6DE', '#7A4FB5', '#1F6FB5'


def letter_forms(letters):
    """Typed letters 'A, C, D': any order, comma / space / semicolon / 'and' before the last."""
    out = set()
    for p in itertools.permutations(letters):
        out.update([', '.join(p), ','.join(p), ' '.join(p), '; '.join(p), ', '.join(p[:-1]) + ' and ' + p[-1]])
    first = ', '.join(letters)
    return [first] + sorted(out - {first})


# ================================================================= squares-figures (cells): exact area and perimeter
def cell_area(cells):
    return len(set(map(tuple, cells)))


def cell_perimeter(cells):
    """The perimeter of a figure made of unit squares: every square edge that is not shared with another square of the figure."""
    s = set(map(tuple, cells))
    n = 0
    for a, b in s:
        for da, db in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            if (a + da, b + db) not in s:
                n += 1
    return n


def poly_area(pts):
    s = 0
    for (x1, y1), (x2, y2) in zip(pts, pts[1:] + pts[:1]):
        s += x1 * y2 - x2 * y1
    return Fr(abs(s), 2)


def poly_perimeter(pts):
    t = 0
    for (x1, y1), (x2, y2) in zip(pts, pts[1:] + pts[:1]):
        t += abs(x2 - x1) + abs(y2 - y1)         # sides of the figures in this lesson are all along the grid
    return t


def polyominoes(n):
    """Every fixed polyomino of n unit squares (squares joined along whole sides), as frozensets of cells, built by adding one square at a time."""
    cur = {frozenset([(0, 0)])}
    for _ in range(n - 1):
        nxt = set()
        for p in cur:
            for a, b in p:
                for da, db in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    c = (a + da, b + db)
                    if c not in p:
                        q = frozenset(p | {c})
                        mx, my = min(x for x, _ in q), min(y for _, y in q)
                        nxt.add(frozenset((x - mx, y - my) for x, y in q))
        cur = nxt
    return cur


def stair_cells(n, decreasing=True):
    """Columns of n, n-1, ... 1 squares side by side (tallest first); x to the right, y up from the floor."""
    hs = list(range(n, 0, -1)) if decreasing else list(range(1, n + 1))
    return [(i, j) for i, h in enumerate(hs) for j in range(h)]


# ================================================================= polygons: right angles inside, dents
def corner_kinds(pts):
    """For a polygon (list of vertices in order, sides along the grid or slanted): (convex 90 degree corners, corners with an inside angle of 270 degrees, others)."""
    n = len(pts)
    a2 = sum(x1 * y2 - x2 * y1 for (x1, y1), (x2, y2) in zip(pts, pts[1:] + pts[:1]))
    orient = 1 if a2 > 0 else -1
    r90 = r270 = other = 0
    for i in range(n):
        p0, p1, p2 = pts[i - 1], pts[i], pts[(i + 1) % n]
        v1 = (p1[0] - p0[0], p1[1] - p0[1])
        v2 = (p2[0] - p1[0], p2[1] - p1[1])
        cross = v1[0] * v2[1] - v1[1] * v2[0]
        dot = v1[0] * v2[0] + v1[1] * v2[1]
        if dot == 0:
            if cross * orient > 0:
                r90 += 1
            else:
                r270 += 1
        else:
            other += 1
    return r90, r270, other


def stair_polygon(n):
    """The outline of the staircase of n steps (columns of 1, 2, ... n squares side by side, tallest on the right), going round once."""
    pts = [(0, 0), (n, 0)]
    for c in range(n, 0, -1):
        pts += [(c, c), (c - 1, c)]
    return pts


# ================================================================= lines: parallel, perpendicular, right angles where lines meet
def _P(p):
    return (Fr(p[0]), Fr(p[1]))


def _seg(s):
    return (_P(s[0]), _P(s[1]))


def _dir(s):
    (a, b), (c, d) = s
    return (c - a, d - b)


def _cross(u, v):
    return u[0] * v[1] - u[1] * v[0]


def _dot(u, v):
    return u[0] * v[0] + u[1] * v[1]


def _on(P, s):
    A, B = s
    if _cross((B[0] - A[0], B[1] - A[1]), (P[0] - A[0], P[1] - A[1])) != 0:
        return False
    return min(A[0], B[0]) <= P[0] <= max(A[0], B[0]) and min(A[1], B[1]) <= P[1] <= max(A[1], B[1])


def _meet(s, t):
    """The point where two (non-parallel) segments meet, or None."""
    d1, d2 = _dir(s), _dir(t)
    den = _cross(d1, d2)
    if den == 0:
        return None
    A, C = s[0], t[0]
    u = _cross((C[0] - A[0], C[1] - A[1]), d2) / den
    P = (A[0] + u * d1[0], A[1] + u * d1[1])
    return P if _on(P, s) and _on(P, t) else None


def segs_from(raw):
    return [_seg(s) for s in raw]


def pairs_parallel(raw):
    """Pairs of the given segments that are parallel (same direction, not on the same line)."""
    S = segs_from(raw)
    out = []
    for (i, s), (j, t) in itertools.combinations(list(enumerate(S)), 2):
        if _cross(_dir(s), _dir(t)) == 0 and _cross(_dir(s), (t[0][0] - s[0][0], t[0][1] - s[0][1])) != 0:
            out.append((i, j))
    return out


def pairs_perpendicular(raw):
    """Pairs of the given segments that meet at a right angle (perpendicular and touching)."""
    S = segs_from(raw)
    out = []
    for (i, s), (j, t) in itertools.combinations(list(enumerate(S)), 2):
        if _dot(_dir(s), _dir(t)) == 0 and _meet(s, t) is not None:
            out.append((i, j))
    return out


def right_angles_at_points(raw):
    """Right angles in a drawing of straight lines: visit every point where lines meet (ends of lines and crossing points); at each point take every line leaving it in a
    different direction; every two of them that are perpendicular make one right angle.  Returns (total, {point: right angles there})."""
    S = segs_from(raw)
    pts = {p for s in S for p in s}
    for s, t in itertools.combinations(S, 2):
        m = _meet(s, t)
        if m is not None:
            pts.add(m)
    per = {}
    for P in pts:
        dirs = set()
        for s in S:
            if _on(P, s):
                for E in s:
                    if E != P:
                        v = (E[0] - P[0], E[1] - P[1])
                        m = abs(v[0]) + abs(v[1])
                        dirs.add((v[0] / m, v[1] / m))
        k = sum(1 for u, v in itertools.combinations(sorted(dirs), 2) if _dot(u, v) == 0)
        if k:
            per[P] = k
    return sum(per.values()), per


# the six capital letters of Lesson 8 Q4, as in the workbook: segments (x1, y1, x2, y2) in a box 50 wide and 80 tall, y down
LETTER_SEGS = {
    'E': [(0, 0, 0, 80), (0, 0, 50, 0), (0, 40, 40, 40), (0, 80, 50, 80)],
    'H': [(0, 0, 0, 80), (50, 0, 50, 80), (0, 40, 50, 40)],
    'T': [(0, 0, 50, 0), (25, 0, 25, 80)],
    'L': [(0, 0, 0, 80), (0, 80, 50, 80)],
    'Z': [(0, 0, 50, 0), (50, 0, 0, 80), (0, 80, 50, 80)],
    'N': [(0, 80, 0, 0), (0, 0, 50, 80), (50, 80, 50, 0)],
}


def letter_raw(ch):
    return [((a, b), (c, d)) for a, b, c, d in LETTER_SEGS[ch]]


# ================================================================= clocks
def hands_angle(hour):
    """The angle between the hands at `hour` o'clock (minute hand on 12, hour hand on the hour), the short way round, in degrees: the hour hand turns 30 degrees an hour."""
    a = 0
    for _ in range(hour):
        a += 30
    return a if a <= 180 else 360 - a


# ================================================================= six-sided shapes with the most right angles (brute force on a small lattice)
def _simple(pts):
    n = len(pts)
    S = [(_P(pts[i]), _P(pts[(i + 1) % n])) for i in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if j == i + 1 or (i == 0 and j == n - 1):
                # neighbouring sides may only share their common corner (no folding back along each other)
                a, b = S[i], S[j]
                if _cross(_dir(a), _dir(b)) == 0:
                    return False
                continue
            s, t = S[i], S[j]
            if _cross(_dir(s), _dir(t)) == 0:
                # parallel sides: they must not touch
                if _on(t[0], s) or _on(t[1], s) or _on(s[0], t) or _on(s[1], t):
                    return False
            elif _meet(s, t) is not None:
                return False
    return True


def hexagon_right_angles(size=4):
    """All six-sided shapes (simple polygons, six real corners, no straight angle) whose corners are points of a size x size lattice: the set of the numbers of right angles inside them."""
    pts = [(x, y) for x in range(size) for y in range(size)]
    found = set()
    for comb in itertools.combinations(pts, 6):
        first, rest = comb[0], comb[1:]
        for perm in itertools.permutations(rest):
            if perm[0] > perm[-1]:
                continue
            poly = [first] + list(perm)
            if any(_cross((poly[i][0] - poly[i - 1][0], poly[i][1] - poly[i - 1][1]), (poly[(i + 1) % 6][0] - poly[i][0], poly[(i + 1) % 6][1] - poly[i][1])) == 0 for i in range(6)):
                continue
            if not _simple(poly):
                continue
            found.add(corner_kinds(poly)[0])
    return found


# ================================================================= figures
def grid_path(x, y, cols, rows, c):
    d = ''.join(f'M{x + i * c} {y}V{y + rows * c}' for i in range(cols + 1)) + ''.join(f'M{x} {y + j * c}H{x + cols * c}' for j in range(rows + 1))
    return f'<path d="{d}" stroke="{GRIDC}" stroke-width="1.2" fill="none"/>'


def cells_draw(cells, x0, y0, c, fill=SKY, dashed=False, outline=True):
    """Squares of a figure on a grid (x right, y DOWN): thin lines between squares, a thick outline round the whole figure."""
    h = _h()
    s = set(map(tuple, cells))
    r, d = '', ''
    for a, b in sorted(s):
        x, y = x0 + a * c, y0 + b * c
        if dashed:
            r += f'<rect x="{x}" y="{y}" width="{c}" height="{c}" fill="#fff" stroke="{h.NAVY}" stroke-width="2" stroke-dasharray="5 4"/>'
            continue
        r += f'<rect x="{x}" y="{y}" width="{c}" height="{c}" fill="{fill}" stroke="{h.NAVY}" stroke-width="1"/>'
        if (a, b - 1) not in s:
            d += f'M{x} {y}H{x + c}'
        if (a, b + 1) not in s:
            d += f'M{x} {y + c}H{x + c}'
        if (a - 1, b) not in s:
            d += f'M{x} {y}V{y + c}'
        if (a + 1, b) not in s:
            d += f'M{x + c} {y}V{y + c}'
    if d and outline:
        r += f'<path d="{d}" stroke="{h.NAVY}" stroke-width="3.5" stroke-linecap="square" fill="none"/>'
    return r


def squares_fig(cells, title, caption, cols=7, rows=5, c=40, dx=1, dy=1):
    """One figure of unit squares (each 1 cm by 1 cm) on a grid, with a title above."""
    h = _h()
    x0, y0 = 4, 30
    body = h.T(x0 + cols * c / 2, 20, title, 20, 'middle', 800)
    body += grid_path(x0, y0, cols, rows, c) + cells_draw([(a + dx, b + dy) for a, b in cells], x0, y0, c)
    return h.svg(cols * c + 2 * x0, y0 + rows * c + 6, body, caption)


def lshape_fig(W, H, top, right, caption='An L-shaped figure with some lengths marked'):
    """The workbook's L-shape: bottom W, left side H, top top, right side `right`; the two sides of the step have no lengths marked."""
    h = _h()
    k = min(26, 260 // W)
    x0, y0 = 70, 36
    P = [(0, 0), (top, 0), (top, H - right), (W, H - right), (W, H), (0, H)]
    pts = ' '.join(f'{x0 + a * k},{y0 + b * k}' for a, b in P)
    b = f'<polygon points="{pts}" fill="{SKY}" stroke="{h.NAVY}" stroke-width="3.5" stroke-linejoin="miter"/>'
    b += h.T(x0 + top * k / 2, y0 - 10, f'{top} cm', 20) + h.T(x0 - 10, y0 + H * k / 2 + 6, f'{H} cm', 20, 'end') + h.T(x0 + W * k / 2, y0 + H * k + 26, f'{W} cm', 20)
    b += h.T(x0 + W * k + 10, y0 + (H - right / 2) * k + 6, f'{right} cm', 20, 'start')
    return h.svg(x0 + W * k + 70, y0 + H * k + 40, b, caption)


def stairs_fig(n, caption, gaps=False, decreasing=True):
    """A staircase of n steps drawn on a grid; gaps=True shows the squares that would fill it up to an n by n square as dashed boxes."""
    h = _h()
    c = min(40, 270 // (n + 2))
    cols = rows = n + 2
    x0, y0 = 4, 4
    cells = [(1 + i, 1 + (n - 1) - j) for i, j in stair_cells(n, decreasing)]
    body = grid_path(x0, y0, cols, rows, c)
    if gaps:
        full = {(1 + i, 1 + j) for i in range(n) for j in range(n)}
        body += cells_draw(sorted(full - set(cells)), x0, y0, c, dashed=True)
    body += cells_draw(cells, x0, y0, c)
    return h.svg(cols * c + 2 * x0, rows * c + 2 * x0, body, caption)


L6 = [(2, 1), (2, 2), (2, 3), (3, 3)]
CANDS = {'A': (2, 0), 'B': (1, 1), 'C': (3, 1), 'D': (1, 2), 'E': (3, 2), 'F': (1, 3), 'G': (4, 3), 'H': (2, 4), 'I': (3, 4)}


def perimeter_with(letter):
    return cell_perimeter(L6 + [CANDS[letter]])


def cand_fig(caption='An L shape of 4 squares on a grid, with nine places marked A to I where a new square could go'):
    h = _h()
    c, cols, rows, x0, y0 = 44, 6, 5, 4, 4
    body = grid_path(x0, y0, cols, rows, c) + cells_draw(L6, x0, y0, c)
    for k, (a, b) in CANDS.items():
        x, y = x0 + a * c, y0 + b * c
        body += f'<rect x="{x + 3}" y="{y + 3}" width="{c - 6}" height="{c - 6}" rx="4" fill="#fff" stroke="{h.NAVY}" stroke-width="2" stroke-dasharray="5 4"/>' + h.T(x + c / 2, y + c / 2 + 7, k, 20)
    return h.svg(cols * c + 2 * x0, rows * c + 2 * x0, body, caption)


def l6_plain_fig(caption='An L shape of 4 squares on a grid'):
    h = _h()
    c, cols, rows, x0, y0 = 44, 6, 5, 4, 4
    return h.svg(cols * c + 2 * x0, rows * c + 2 * x0, grid_path(x0, y0, cols, rows, c) + cells_draw(L6, x0, y0, c), caption)


def move_row_fig(caption):
    """4 by 4 square -> 5 by 3 rectangle: the bottom row of 4 squares is moved to the right as a new column of 3 squares and 1 square is left over."""
    h = _h()
    c, x0, y0 = 30, 6, 6
    body = ''
    for a in range(5):
        for b in range(3):
            body += f'<rect x="{x0 + a * c}" y="{y0 + b * c}" width="{c}" height="{c}" fill="{SKY if a < 4 else "#D3F1E4"}" stroke="{h.NAVY}" stroke-width="1.4"/>'
    body += f'<rect x="{x0}" y="{y0 + 3 * c + 6}" width="{c}" height="{c}" fill="{h.YEL}" stroke="{h.NAVY}" stroke-width="1.4"/>'
    body += h.T(x0 + 5 * c + 8, y0 + 1.5 * c + 6, '3 squares', 15, 'start', 800, h.TEAL) + h.T(x0 + c + 8, y0 + 3 * c + 6 + c / 2 + 5, 'this 1 square is left over', 15, 'start', 800)
    return h.svg(x0 * 2 + 5 * c + 100, y0 + 4 * c + 12, body, caption)


def shape_fig(pts, title, caption, u=34):
    """One shape (vertices with y UP inside the shape) drawn at unit u, with its title (such as 'Shape B') below."""
    h = _h()
    W = max(x for x, _ in pts)
    H = max(y for _, y in pts)
    x0, y0 = 20, 12
    P = ' '.join(f'{x0 + a * u},{y0 + (H - b) * u}' for a, b in pts)
    body = f'<polygon points="{P}" fill="{SKY}" stroke="{h.NAVY}" stroke-width="3.5" stroke-linejoin="miter"/>' + h.T(x0 + W * u / 2, y0 + H * u + 32, title, 22, 'middle', 800)
    return h.svg(W * u + 2 * x0, y0 + H * u + 44, body, caption)


SHAPES = {
    'A': [(1, 0), (2, 0), (2, 1), (3, 1), (3, 2), (2, 2), (2, 3), (1, 3), (1, 2), (0, 2), (0, 1), (1, 1)],
    'B': [(0, 0), (3, 0), (3, 1), (2, 1), (2, 2), (1, 2), (1, 3), (0, 3)],
    'C': [(0, 0), (4, 0), (4, 3), (2, 5), (0, 3)],
    'D': [(0, 0), (5, 0), (3, 3), (0, 3)],
}
U_SHAPE = [(0, 0), (3, 0), (3, 2), (2, 2), (2, 1), (1, 1), (1, 2), (0, 2)]


def angle_fig(data, letter):
    h = _h()
    l, d1, sz, L1, L2 = [a for a in data if a[0] == letter][0]
    d2 = d1 + sz
    pt = lambda d, L: (L * cos(radians(d)), -L * sin(radians(d)))
    K = 1.75
    p1, p2 = pt(d1, L1 * K), pt(d2, L2 * K)
    xs, ys = [0, p1[0], p2[0]], [0, p1[1], p2[1]]
    s = min(1, 250 / (max(xs) - min(xs)), 150 / (max(ys) - min(ys)))
    cx, cy = 150, 84
    vx = cx - s * (min(xs) + max(xs)) / 2
    vy = cy - s * (min(ys) + max(ys)) / 2
    r = 26
    a1 = (vx + r * cos(radians(d1)), vy - r * sin(radians(d1)))
    a2 = (vx + r * cos(radians(d2)), vy - r * sin(radians(d2)))
    body = f'<path d="M{a1[0]:.1f} {a1[1]:.1f} A{r} {r} 0 0 0 {a2[0]:.1f} {a2[1]:.1f}" fill="none" stroke="{h.TEAL}" stroke-width="3.2"/>'
    for p in (p1, p2):
        body += f'<line x1="{vx:.1f}" y1="{vy:.1f}" x2="{vx + s * p[0]:.1f}" y2="{vy + s * p[1]:.1f}" stroke="{h.NAVY}" stroke-width="4.5" stroke-linecap="round"/>'
    body += f'<circle cx="{vx:.1f}" cy="{vy:.1f}" r="4.5" fill="{h.NAVY}"/>' + h.T(150, 184, 'angle ' + letter, 22, 'middle', 800)
    return h.svg(300, 194, body, f'Angle {letter}: two straight arms meet at a point and a small arc marks the angle between them')


def fan_fig(n, caption=None):
    h = _h()
    ox, oy, L = 150, 150, 135
    body = ''
    for i in range(n):
        d = 15 + (150 * i) / (n - 1)
        body += f'<line x1="{ox}" y1="{oy}" x2="{ox + L * cos(radians(d)):.1f}" y2="{oy - L * sin(radians(d)):.1f}" stroke="{h.NAVY}" stroke-width="4" stroke-linecap="round"/>'
    body += f'<circle cx="{ox}" cy="{oy}" r="6" fill="{h.NAVY}"/>' + h.T(ox, oy + 28, 'O', 22, 'middle', 800)
    return h.svg(300, 184, body, caption or f'{n} straight lines going out from one point O, spread out like a fan')


def letter_fig(ch):
    h = _h()
    k = 2.2
    x0, y0 = 70, 14
    body = ''
    for a, b, c, d in LETTER_SEGS[ch]:
        body += f'<line x1="{x0 + a * k:.1f}" y1="{y0 + b * k:.1f}" x2="{x0 + c * k:.1f}" y2="{y0 + d * k:.1f}" stroke="{h.NAVY}" stroke-width="10" stroke-linecap="round"/>'
    return h.svg(250, 200, body + h.T(125, 196, 'Letter ' + ch, 22, 'middle', 800), f'The capital letter {ch} drawn with straight lines')


def hash_fig():
    h = _h()
    body = ''
    for x in (90, 160):
        body += f'<line x1="{x}" y1="14" x2="{x}" y2="150" stroke="{h.NAVY}" stroke-width="8" stroke-linecap="round"/>'
    for y in (54, 108):
        body += f'<line x1="40" y1="{y}" x2="210" y2="{y}" stroke="{h.NAVY}" stroke-width="8" stroke-linecap="round"/>'
    return h.svg(250, 164, body, 'The # sign: two upright lines crossed by two lines going across')


def window_raw():
    return [((0, 0), (4, 0)), ((4, 0), (4, 2)), ((4, 2), (0, 2)), ((0, 2), (0, 0)), ((2, 0), (2, 2)), ((0, 1), (4, 1))]


def window_fig():
    h = _h()
    body = f'<rect x="20" y="15" width="200" height="130" fill="{SKY}" stroke="{h.NAVY}" stroke-width="4"/>'
    body += f'<line x1="120" y1="15" x2="120" y2="145" stroke="{h.NAVY}" stroke-width="4"/><line x1="20" y1="80" x2="220" y2="80" stroke="{h.NAVY}" stroke-width="4"/>'
    return h.svg(240, 160, body, 'A window: a rectangle with one line from the middle of the top to the middle of the bottom and one line from the middle of the left side to the middle of the right side')


def row_raw(k):
    segs = [((0, 0), (k, 0)), ((k, 0), (k, 1)), ((k, 1), (0, 1)), ((0, 1), (0, 0))]
    return segs + [((i, 0), (i, 1)) for i in range(1, k)]


def row_fig(k):
    h = _h()
    w = min(40, 270 // k)
    x0, y0 = 10, 12
    body = f'<rect x="{x0}" y="{y0}" width="{k * w}" height="{w}" fill="{SKY}" stroke="{h.NAVY}" stroke-width="4"/>'
    for i in range(1, k):
        body += f'<line x1="{x0 + i * w}" y1="{y0}" x2="{x0 + i * w}" y2="{y0 + w}" stroke="{h.NAVY}" stroke-width="4"/>'
    return h.svg(k * w + 2 * x0, w + 2 * y0, body, f'A long rectangle cut into {k} squares in a row by {k - 1} lines')


def clocks_fig():
    h = _h()
    body = ''
    for k in range(1, 12):
        col, row = (k - 1) % 3, (k - 1) // 3
        cx, cy = 52 + col * 100, 50 + row * 108
        body += h.Ci(cx, cy, 40, '#fff', h.NAVY, 2.6)
        for q in range(12):
            a = radians(30 * q)
            body += h.Ln(round(cx + 34 * sin(a), 1), round(cy - 34 * cos(a), 1), round(cx + 39 * sin(a), 1), round(cy - 39 * cos(a), 1), 2, h.NAVY)
        a = radians(30 * k)
        body += h.Ln(cx, cy, cx, cy - 31, 3.4, h.NAVY) + h.Ln(cx, cy, round(cx + 20 * sin(a), 1), round(cy - 20 * cos(a), 1), 5, h.WARM)
        body += h.Ci(cx, cy, 3.5, h.NAVY, h.NAVY, 1) + h.T(cx, cy + 62, f'{k}:00', 18, 'middle', 800)
    return h.svg(304, 4 * 108 + 8, body, 'Eleven clock faces showing 1 o’clock to 11 o’clock: the long minute hand points at 12 and the short red hour hand points at the hour')


# ---- grid lines (Q5): points, a base line, candidate lines
def _clip(P, d, xmin, xmax, ymin, ymax):
    """The line through P with direction d, cut to the rectangle; returns two end points (floats)."""
    lo, hi = -1e9, 1e9
    for p, dd, a, b in ((P[0], d[0], xmin, xmax), (P[1], d[1], ymin, ymax)):
        if dd == 0:
            continue
        t1, t2 = (a - p) / dd, (b - p) / dd
        lo, hi = max(lo, min(t1, t2)), min(hi, max(t1, t2))
    return (P[0] + lo * d[0], P[1] + lo * d[1]), (P[0] + hi * d[0], P[1] + hi * d[1])


LINE_COL = [None, '#B5481F', '#1F7A6F', '#7A4FB5', '#1F6FB5']


def lines_fig(box, c, points, base, cands=None, answer=None, caption=''):
    """A square grid (box = xmin, xmax, ymin, ymax in grid points, c px per square) with labelled points, the base line (given by two of its points),
    and either numbered candidate lines through a point [(label number, point, direction)] or the answer line drawn in teal."""
    h = _h()
    xmin, xmax, ymin, ymax = box
    cols, rows = xmax - xmin, ymax - ymin
    x0, y0 = 14, 14
    px = lambda p: (x0 + (p[0] - xmin) * c, y0 + (p[1] - ymin) * c)
    body = grid_path(x0, y0, cols, rows, c)

    def line(P, d, col, sw, dash=None):
        a, b = _clip(P, d, xmin, xmax, ymin, ymax)
        (X1, Y1), (X2, Y2) = px(a), px(b)
        return f'<line x1="{X1:.1f}" y1="{Y1:.1f}" x2="{X2:.1f}" y2="{Y2:.1f}" stroke="{col}" stroke-width="{sw}" stroke-linecap="round"' + (f' stroke-dasharray="{dash}"' if dash else '') + '/>'
    A, B = points[base[0]], points[base[1]]
    body += line(A, (B[0] - A[0], B[1] - A[1]), h.NAVY, 4.5)
    if cands:
        for num, P, d in cands:
            body += line(P, d, LINE_COL[num], 3.2)
            a, b = _clip(P, d, xmin, xmax, ymin, ymax)
            # the number sits at the end of the line that is the most to the right (or the top)
            e = b if (b[0], -b[1]) > (a[0], -a[1]) else a
            ex, ey = px(e)
            body += h.Ci(round(ex, 1), round(ey, 1), 11, '#fff', LINE_COL[num], 2.4) + h.T(round(ex, 1), round(ey + 6, 1), num, 16, 'middle', 800, LINE_COL[num])
    if answer:
        P, d = answer
        body += line(P, d, h.TEAL, 4.5)
    for name, p in points.items():
        X, Y = px(p)
        body += h.Ci(round(X, 1), round(Y, 1), 5.5, h.NAVY, h.NAVY, 1)
        dx, dy = 0, 0
        body += h.T(round(X + 12, 1), round(Y - 7, 1), name, 20, 'middle', 800)
    return h.svg(cols * c + 2 * x0, rows * c + 2 * x0, body, caption)


# ---- the staircase corner counts of the Investigation (L8), from the outline
def stair_counts(n):
    r90, r270, other = corner_kinds(stair_polygon(n))
    return r90, r270, r90 + r270 + other
