"""Level 2 (P2) helpers for holiday week 4 (lesson 7 Fair Shares, lesson 8 Shape Builders): fraction figures drawn for a phone, the six shapes of Q1 (re-laid out
2 by 3), the robot, a labelled net-extension grid, and the INDEPENDENT checkers (areas by sampling, geometry of lines, rolling a cube over a net, counting cubes).
Imported by p2/07/lesson.py and p2/08/lesson.py (after `from hlib import *`)."""
import itertools, math, re
from fractions import Fraction as Fr
from hlib import svg as _svg, T, Ln, Ci, Re, NAVY, YEL, TEAL, WARM, PALE

SKY = '#DDEBF7'


# ---------------------------------------------------------------- typed lists
def list_forms(parts, ordered=True, sym=' < '):
    """A typed list 'a, b, c' written with ', ' / ',' / ';' / space / 'and' (and ' < ' when ordered); all orders when not ordered.  The first form is 'a, b, c'."""
    orders = [list(parts)] if ordered else [list(p) for p in itertools.permutations(parts)]
    out = []
    for o in orders:
        for sp in [', ', ',', ';', ' '] + ([sym] if ordered and sym else []):
            out.append(sp.join(o))
        if len(o) > 1:
            out.append(', '.join(o[:-1]) + ' and ' + o[-1])
        if len(o) > 2:
            out.append(', '.join(o[:-1]) + ', and ' + o[-1])
    first = ', '.join(parts)
    return [first] + sorted(set(out) - {first})


# ---------------------------------------------------------------- fraction figures (equal parts, nothing written for the answer)
def _part(x, y, w, h, on):
    return f'<rect class="part" x="{x:g}" y="{y:g}" width="{w:g}" height="{h:g}" fill="{YEL if on else "#FFFFFF"}" stroke="{NAVY}" stroke-width="2.4"/>'


def frac_bars(rows, caption='', label_w=70, W=340):
    """rows = [(label, n parts, [shaded part indexes])]: bars of the SAME length, each cut into n EQUAL parts."""
    bw = W - label_w - 12
    b, y = '', 6
    for lab, n, sh in rows:
        if lab:
            b += T(4, y + 25, lab, 16, 'start', 800)
        for i in range(n):
            b += _part(label_w + i * bw / n, y, bw / n, 34, i in sh)
        y += 48
    cap = caption or ('Bars of the same length: ' + '; '.join(f'{lab or "a bar"} cut into {n} equal parts with {len(sh)} shaded' for lab, n, sh in rows))
    return _svg(W, y, b, cap)


def frac_bar(n, shade=(), label='', caption=''):
    return frac_bars([(label, n, list(shade))], caption or f'A bar cut into {n} equal parts, {len(shade)} shaded', label_w=70 if label else 4)


def frac_pie(n, shade=(), caption=''):
    cx, cy, r = 170, 74, 62
    b = ''
    for i in range(n):
        a0, a1 = 360 * i / n, 360 * (i + 1) / n
        p0 = (cx + r * math.cos(math.radians(a0 - 90)), cy + r * math.sin(math.radians(a0 - 90)))
        p1 = (cx + r * math.cos(math.radians(a1 - 90)), cy + r * math.sin(math.radians(a1 - 90)))
        b += (f'<path class="part" d="M{cx} {cy} L{p0[0]:.1f} {p0[1]:.1f} A{r} {r} 0 {1 if a1 - a0 > 180 else 0} 1 {p1[0]:.1f} {p1[1]:.1f} Z" '
              f'fill="{YEL if i in shade else "#FFFFFF"}" stroke="{NAVY}" stroke-width="2.4" stroke-linejoin="round"/>')
    return _svg(340, 148, b, caption or f'A circle cut into {n} equal parts, {len(shade)} shaded')


def frac_grid(cols, rows, shade, caption=''):
    c = 40
    x0 = (340 - cols * c) / 2
    b = ''
    for r in range(rows):
        for k in range(cols):
            b += _part(x0 + k * c, 6 + r * c, c, c, (r, k) in shade)
    return _svg(340, rows * c + 12, b, caption or f'A grid of {cols * rows} equal squares, {len(shade)} shaded')


def count_parts(svg):
    """(shaded parts, all parts) READ FROM THE DRAWING: every element with class part, and how many are yellow."""
    parts = re.findall(r'<(?:rect|path) class="part"[^>]*?fill="([^"]+)"', svg)
    return sum(1 for f in parts if f == YEL), len(parts)


# ---------------------------------------------------------------- Q1: six shapes, each cut into 4 parts, 1 shaded
def _inside_circle(x, y, cx, cy, r):
    return (x - cx) ** 2 + (y - cy) ** 2 <= r * r


def _shape_region(k, x, y):
    """Which of the 4 parts of shape k the point (x, y) is in (local 100 by 100 cell), or None outside the shape."""
    if k == 'A':
        return int((x - 10) // 20) if 10 <= x < 90 and 10 <= y <= 90 else None
    if k == 'B':
        return (x > 35, y < 65) if _inside_circle(x, y, 50, 50, 42) else None
    if k == 'C':
        return (x > 50, y > 50) if 5 <= x <= 95 and 20 <= y <= 80 else None
    if k == 'D':
        if not (5 <= x <= 95 and 20 <= y <= 80):
            return None
        return sum(1 for cut in (17, 37, 63) if x > cut)
    if k == 'E':
        if not (10 <= x <= 90 and 10 <= y <= 90):
            return None
        u, v = x - 50, y - 50
        return ('L' if u < 0 else 'R') if abs(u) > abs(v) else ('T' if v < 0 else 'B')
    if k == 'F':
        ap, bl, br = (50, 90 - 40 * math.sqrt(3)), (10, 90), (90, 90)
        d = (bl[1] - br[1]) * (ap[0] - br[0]) + (br[0] - bl[0]) * (ap[1] - br[1])
        l1 = ((bl[1] - br[1]) * (x - br[0]) + (br[0] - bl[0]) * (y - br[1])) / d
        l2 = ((br[1] - ap[1]) * (x - br[0]) + (ap[0] - br[0]) * (y - br[1])) / d
        l3 = 1 - l1 - l2
        if min(l1, l2, l3) < 0:
            return None
        if max(l1, l2, l3) <= 0.5:
            return 'mid'
        return (l1, l2, l3).index(max(l1, l2, l3))
    raise ValueError(k)


def region_areas(k, step=0.4):
    """Area of each part of shape k, found by counting sample points (no formula, no printed answer)."""
    cnt = {}
    n = int(100 / step)
    for i in range(n):
        for j in range(n):
            r = _shape_region(k, (i + 0.5) * step + 0.0137, (j + 0.5) * step + 0.0071)
            if r is not None:
                cnt[r] = cnt.get(r, 0) + 1
    return cnt


def is_quarters(k):
    """True when the shape is cut into exactly 4 parts of the same size (areas within 3 per cent)."""
    a = list(region_areas(k).values())
    return len(a) == 4 and (max(a) - min(a)) / max(a) < 0.03


def six_shapes_fig():
    def cell(k, ox, oy):
        g = f'<g transform="translate({ox} {oy})">'
        if k == 'A':
            g += Re(10, 10, 80, 80, '#fff') + Re(30, 10, 20, 80, YEL) + Ln(70, 10, 70, 90)
        elif k == 'B':
            cx = cy = 50
            a, r = 15, 42
            h = math.sqrt(r * r - a * a)
            g += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#fff" stroke="{NAVY}" stroke-width="2.5"/>'
            g += (f'<path d="M{cx - a} {cy + a} L{cx - a} {cy - h:.1f} A{r} {r} 0 0 1 {cx + h:.1f} {cy + a} Z" fill="{YEL}" stroke="{NAVY}" stroke-width="2.5"/>')
            g += Ln(cx - a, cy - h, cx - a, cy + h) + Ln(cx - h, cy + a, cx + h, cy + a)
        elif k == 'C':
            g += Re(5, 20, 90, 60, '#fff') + Re(5, 20, 45, 30, YEL) + Ln(50, 20, 50, 80) + Ln(5, 50, 95, 50)
        elif k == 'D':
            g += Re(5, 20, 90, 60, '#fff') + Re(63, 20, 32, 60, YEL) + Ln(17, 20, 17, 80) + Ln(37, 20, 37, 80)
        elif k == 'E':
            g += Re(10, 10, 80, 80, '#fff') + f'<polygon points="10,10 10,90 50,50" fill="{YEL}" stroke="{NAVY}" stroke-width="2.5" stroke-linejoin="round"/>' + Ln(10, 10, 90, 90) + Ln(90, 10, 10, 90)
        else:
            ap = (50, 90 - 40 * math.sqrt(3))
            g += f'<polygon points="{ap[0]},{ap[1]:.1f} 10,90 90,90" fill="#fff" stroke="{NAVY}" stroke-width="2.5" stroke-linejoin="round"/>'
            g += f'<polygon points="30,{(ap[1] + 90) / 2:.1f} 70,{(ap[1] + 90) / 2:.1f} 50,90" fill="{YEL}" stroke="{NAVY}" stroke-width="2.5" stroke-linejoin="round"/>'
        return g + T(50, 118, k, 20, 'middle', 800) + '</g>'
    b = ''
    for i, k in enumerate('ABCDEF'):
        b += cell(k, 5 + (i % 3) * 110, (i // 3) * 126)
    return _svg(340, 252, b, 'Six shapes A to F, each cut into 4 parts with 1 part shaded')


def strips_fig():
    """Fraction strips of the same length: one whole, halves, thirds, quarters, sixths, eighths (lesson 7 Investigation)."""
    rows = [('whole', 1), ('halves', 2), ('thirds', 3), ('quarters', 4), ('sixths', 6), ('eighths', 8)]
    bw, x0, y = 250, 84, 6
    b = ''
    for name, n in rows:
        b += T(4, y + 25, name, 15, 'start', 800)
        for i in range(n):
            b += Re(x0 + i * bw / n, y, bw / n, 34, '#fff', NAVY, 2.4) + T(x0 + (i + .5) * bw / n, y + 24, '1' if n == 1 else f'1/{n}', 13 if n > 4 else 15, 'middle', 700)
        y += 46
    return _svg(340, y, b, 'Fraction strips of the same length: a whole, then strips cut into halves, thirds, quarters, sixths and eighths, each part labelled')


def covers(kind, whole_part):
    """How many pieces of 1/kind exactly cover a strip of 1/whole_part (0 if no whole number of them does), found by adding pieces one at a time."""
    total, n = Fr(0), 0
    while total < Fr(1, whole_part) and n < 40:
        total += Fr(1, kind)
        n += 1
    return n if total == Fr(1, whole_part) else 0


# ---------------------------------------------------------------- lesson 8 figures and checkers
def robot_fig():
    """The robot of Q1 (hat triangle, head square, ear half circles, body square, shoulder quarter circles, hand triangles, foot half circles), no table."""
    x = -150
    P = lambda d: f'<path d="{d}" fill="{SKY}" stroke="{NAVY}" stroke-width="2.5" stroke-linejoin="round"/>'
    Po = lambda pts: f'<polygon points="{" ".join(f"{a:g},{b:g}" for a, b in pts)}" fill="{SKY}" stroke="{NAVY}" stroke-width="2.5" stroke-linejoin="round"/>'
    s = Po([(300 + x, 8), (262 + x, 58), (338 + x, 58)])
    s += Re(262 + x, 58, 76, 76, SKY, NAVY, 2.5)
    s += P(f'M{262 + x} 72 A24 24 0 0 0 {262 + x} 120 Z') + P(f'M{338 + x} 72 A24 24 0 0 1 {338 + x} 120 Z')
    s += Re(244 + x, 134, 112, 112, SKY, NAVY, 2.5)
    s += P(f'M{244 + x} 134 L{196 + x} 134 A48 48 0 0 0 {244 + x} 182 Z') + P(f'M{356 + x} 134 L{404 + x} 134 A48 48 0 0 1 {356 + x} 182 Z')
    s += Po([(200 + x, 190), (234 + x, 190), (217 + x, 226)]) + Po([(366 + x, 190), (400 + x, 190), (383 + x, 226)])
    s += P(f'M{244 + x} 282 A28 28 0 0 1 {300 + x} 282 Z') + P(f'M{300 + x} 282 A28 28 0 0 1 {356 + x} 282 Z')
    return _svg(220, 290, f'<g transform="translate(-40 0)">{s}</g>', 'A robot made of shapes: a triangle hat, a square head, two half-circle ears, a square body, two quarter-circle shoulders, two triangle hands and two half-circle feet')


def robot_kinds(fig):
    """Count the pieces of the drawn robot by kind from the picture: 3 points = triangle, rect = square, an arc path is a half circle when its chord is twice the radius, a quarter circle when the chord is radius * sqrt 2."""
    k = dict(square=0, triangle=0, half=0, quarter=0)
    k['square'] = len(re.findall(r'<rect ', fig))
    k['triangle'] = sum(1 for p in re.findall(r'<polygon points="([^"]+)"', fig) if len(p.split()) == 3)
    for d in re.findall(r'<path d="([^"]+)"', fig):
        m = re.match(r'M([\d.-]+) ([\d.-]+)(?: L([\d.-]+) ([\d.-]+))? A([\d.]+) [\d.]+ 0 \d \d ([\d.-]+) ([\d.-]+) Z', d)
        x0, y0 = (float(m.group(3)), float(m.group(4))) if m.group(3) else (float(m.group(1)), float(m.group(2)))
        r, x1, y1 = float(m.group(5)), float(m.group(6)), float(m.group(7))
        chord = math.hypot(x1 - x0, y1 - y0)
        k['half' if abs(chord - 2 * r) < 0.5 else 'quarter'] += 1
    return k


def squares_in_grid(cols, rows):
    """Squares of every size in a cols by rows grid, counted by trying every size and every top-left corner."""
    by = {}
    for s in range(1, min(cols, rows) + 1):
        by[s] = sum(1 for x in range(cols) for y in range(rows) if x + s <= cols and y + s <= rows)
    return by


def rectangles_in_grid(cols, rows):
    """Rectangles (squares included) in a grid, by trying every pair of left/right and top/bottom lines."""
    return sum(1 for x0 in range(cols + 1) for x1 in range(x0 + 1, cols + 1) for y0 in range(rows + 1) for y1 in range(y0 + 1, rows + 1))


TRI_PTS = dict(P=(440, 12), B=(320, 170), D=(400, 170), E=(480, 170), C=(560, 170), L=(380, 91), M=(420, 91), N=(460, 91), R=(500, 91))
TRI_LINES = ['PLB', 'PMD', 'PNE', 'PRC', 'BDEC', 'LMNR']


def triangles_in_fig():
    """(triangles on the bottom line, triangles on the line across, all): every triple of marked points that are not on one line and whose three pairs each lie on a drawn line."""
    def on_line(a, b):
        return any(a in ln and b in ln for ln in TRI_LINES)
    bottom = across = 0
    for a, b, c in itertools.combinations(TRI_PTS, 3):
        if any(a in ln and b in ln and c in ln for ln in TRI_LINES):
            continue
        if on_line(a, b) and on_line(b, c) and on_line(a, c):
            if sum(1 for p in (a, b, c) if p in 'BDEC') == 2:
                bottom += 1
            else:
                across += 1
    return bottom, across, bottom + across


STACKS = dict(A=[[2, 2, 1]], B=[[2, 2], [2, 2]], C=[[1, 1, 1], [2, 2, 1], [3, 2, 1]])


def cubes_in(hm):
    """Cubes in a stack given as heights of its columns: counted one cube at a time (no sums by layer)."""
    n = 0
    for row in hm:
        for h in row:
            for _ in range(h):
                n += 1
    return n


def painted_counts(n):
    """For an n by n by n cube painted outside: {faces painted: small cubes}, by looking at every small cube."""
    out = {}
    for x, y, z in itertools.product(range(n), repeat=3):
        f = (x == 0) + (x == n - 1) + (y == 0) + (y == n - 1) + (z == 0) + (z == n - 1)
        out[f] = out.get(f, 0) + 1
    return out


NETS = {'A': ['.#..', '####', '.#..'], 'B': ['###', '###'], 'C': ['#...', '####', '...#'], 'D': ['.##.', '####'], 'E': ['##..', '.##.', '..##'], 'F': ['#....', '#####']}


def cells_of(rows):
    return {(r, c) for r, row in enumerate(rows) for c, ch in enumerate(row) if ch == '#'}


def folds_into_cube(cells):
    """Roll a cube over the squares: put it on one square, roll it to each neighbour in turn, and note which face of the cube lands on every square.  It is a net of a cube when 6 squares get 6 different faces."""
    cells = set(cells)
    if len(cells) != 6:
        return False
    start = min(cells)
    # faces: bottom, top, north, south, east, west
    state = {start: dict(b=0, t=1, n=2, s=3, e=4, w=5)}
    todo = [start]
    while todo:
        cur = todo.pop()
        f = state[cur]
        for dr, dc, name in ((0, 1, 'e'), (0, -1, 'w'), (-1, 0, 'n'), (1, 0, 's')):
            nb = (cur[0] + dr, cur[1] + dc)
            if nb in cells and nb not in state:
                g = dict(f)
                if name == 'e':
                    g['b'], g['e'], g['t'], g['w'] = f['e'], f['t'], f['w'], f['b']
                elif name == 'w':
                    g['b'], g['w'], g['t'], g['e'] = f['w'], f['t'], f['e'], f['b']
                elif name == 'n':
                    g['b'], g['n'], g['t'], g['s'] = f['n'], f['t'], f['s'], f['b']
                else:
                    g['b'], g['s'], g['t'], g['n'] = f['s'], f['t'], f['n'], f['b']
                state[nb] = g
                todo.append(nb)
    return len(state) == 6 and len({s['b'] for s in state.values()}) == 6


def _canon(cells):
    best = None
    pts = list(cells)
    for flip in (False, True):
        for rot in range(4):
            q = pts
            if flip:
                q = [(r, -c) for r, c in q]
            for _ in range(rot):
                q = [(c, -r) for r, c in q]
            r0, c0 = min(r for r, _ in q), min(c for _, c in q)
            key = tuple(sorted((r - r0, c - c0) for r, c in q))
            if best is None or key < best:
                best = key
    return best


def polyominoes(n):
    """All different shapes of n squares joined edge to edge (turning and flipping give the same shape), found by growing shapes one square at a time."""
    shapes = {_canon({(0, 0)})}
    for _ in range(n - 1):
        new = set()
        for s in shapes:
            for r, c in s:
                for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    p = (r + dr, c + dc)
                    if p not in s:
                        new.add(_canon(set(s) | {p}))
        shapes = new
    return sorted(shapes)


def polyominoes_fig(n):
    shapes = polyominoes(n)
    c, gap = 26, 24
    x, b, H = 8, '', 0
    for s in shapes:
        w = (max(cc for _, cc in s) + 1) * c
        h = (max(r for r, _ in s) + 1) * c
        for r, cc in s:
            b += Re(x + cc * c, 8 + r * c, c, c, YEL, NAVY, 2.2)
        x += w + gap
        H = max(H, h)
    return _svg(max(340, x), H + 16, b, f'All {len(shapes)} different shapes made of {n} squares joined edge to edge')


NET_BASE = {(1, 2), (2, 1), (2, 2), (2, 3), (2, 4)}      # the printed shape: a row of 4 squares with 1 square above the second


def net_places():
    """Every empty square touching the printed shape, in reading order, and which of them make a net of a cube."""
    cand = sorted({(r + dr, c + dc) for r, c in NET_BASE for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0))} - NET_BASE)
    return cand, [folds_into_cube(NET_BASE | {p}) for p in cand]


def net_places_fig(show_good=False):
    cand, good = net_places()
    c = 38
    b = ''
    for r in range(0, 4):
        for k in range(0, 6):
            b += Re(6 + k * c, 6 + r * c, c, c, 'none', '#8A94AD', 1, 0, '3 3')
    for r, k in NET_BASE:
        b += Re(6 + k * c, 6 + r * c, c, c, SKY, NAVY, 2.4)
    for i, ((r, k), g) in enumerate(zip(cand, good)):
        fill = '#BFE8C8' if (show_good and g) else '#FFFFFF'
        b += Re(6 + k * c + 3, 6 + r * c + 3, c - 6, c - 6, fill, NAVY, 2, 5, '4 3') + T(6 + k * c + c / 2, 6 + r * c + c / 2 + 6, i + 1, 18, 'middle', 800)
    return _svg(6 + 6 * c + 6, 6 + 4 * c + 6, b, 'A shape of 5 squares (a row of 4 and 1 square above the second) on a dotted grid, with the empty squares next to it numbered ' + f'1 to {len(cand)}')


def grid_plain(cols, rows, c=None):
    c = c or min(40, 300 // max(cols, rows))
    b = ''
    for r in range(rows):
        for k in range(cols):
            b += Re(20 + k * c, 6 + r * c, c, c, '#fff', NAVY, 2.4)
    return _svg(40 + cols * c, rows * c + 12, b, f'A grid {cols} squares long and {rows} squares high')
