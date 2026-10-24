"""Independent checks for Level 1 Unit 7 (2D shapes).  Counts come from the figure specs in the unit file (geometry is recomputed:
triangles by finding every triangle whose three sides lie on drawn lines; squares and rectangles by listing every position; fold
lines by reflecting the corner points), names come from a side-count table, and arithmetic is done with the numbers in the text."""
import itertools, math
from common import s, load_unit

CHECKS = {}
U = load_unit(1, 7)
ITEM = {it['id']: it for it in U['items']}
ITEM[U['learn']['try']['id']] = U['learn']['try']
ITEM['EXAMPLE'] = U['learn']['example']


def check(id_):
    def deco(f):
        CHECKS[id_] = f
        return f
    return deco


CORNERS = {'circle': 0, 'triangle': 3, 'square': 4, 'rectangle': 4, 'tall_rectangle': 4, 'pentagon': 5, 'hexagon': 6, 'heptagon': 7, 'octagon': 8}
NAME_OF_SIDES = {3: 'triangle', 5: 'pentagon', 6: 'hexagon', 7: 'heptagon', 8: 'octagon'}


def kinds(fig):
    return [(i['name'] if isinstance(i, dict) else i) for i in fig['items']]


# ---------------- geometry helpers ----------------
def segments(fig):
    segs = []
    for e in fig['elements']:
        if 'poly' in e and not e.get('dash'):
            p = e['poly']
            segs += [(tuple(p[i]), tuple(p[(i + 1) % len(p)])) for i in range(len(p))]
        elif 'line' in e and not e.get('dash'):
            x1, y1, x2, y2 = e['line']
            segs.append(((x1, y1), (x2, y2)))
    return segs


def inter(a, b):
    (x1, y1), (x2, y2) = a
    (x3, y3), (x4, y4) = b
    d = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if abs(d) < 1e-9:
        return None
    t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / d
    u = ((x1 - x3) * (y1 - y2) - (y1 - y3) * (x1 - x2)) / d
    if -1e-9 <= t <= 1 + 1e-9 and -1e-9 <= u <= 1 + 1e-9:
        return (x1 + t * (x2 - x1), y1 + t * (y2 - y1))
    return None


def on_seg(pt, seg, eps=1e-6):
    (x1, y1), (x2, y2) = seg
    cx = (x2 - x1) * (pt[1] - y1) - (y2 - y1) * (pt[0] - x1)
    if abs(cx) > eps * max(1, math.hypot(x2 - x1, y2 - y1)):
        return False
    return min(x1, x2) - eps <= pt[0] <= max(x1, x2) + eps and min(y1, y2) - eps <= pt[1] <= max(y1, y2) + eps


def count_triangles(fig):
    segs = segments(fig)
    pts = set()
    for sg in segs:
        pts.add(tuple(round(c, 6) for c in sg[0])); pts.add(tuple(round(c, 6) for c in sg[1]))
    for a, b in itertools.combinations(segs, 2):
        p = inter(a, b)
        if p:
            pts.add((round(p[0], 6), round(p[1], 6)))
    pts = sorted(pts)

    def covered(p, q):
        for k in range(1, 40):
            m = (p[0] + (q[0] - p[0]) * k / 40, p[1] + (q[1] - p[1]) * k / 40)
            if not any(on_seg(m, sg) for sg in segs):
                return False
        return True
    areas = []
    for a, b, c in itertools.combinations(pts, 3):
        area2 = (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
        if abs(area2) < 1e-6:
            continue
        if covered(a, b) and covered(b, c) and covered(a, c):
            areas.append(round(abs(area2) / 2, 3))
    return areas


def count_squares(c, r):
    return sum((c - k + 1) * (r - k + 1) for k in range(1, min(c, r) + 1))


def count_rects(c, r):
    return sum((c - w + 1) * (r - h + 1) for w in range(1, c + 1) for h in range(1, r + 1))


def fold_lines(poly):
    n = len(poly)
    cx = sum(p[0] for p in poly) / n
    cy = sum(p[1] for p in poly) / n
    cands = set()
    for p in poly:
        cands.add(round(math.atan2(p[1] - cy, p[0] - cx) % math.pi, 3))
    for i in range(n):
        m = ((poly[i][0] + poly[(i + 1) % n][0]) / 2, (poly[i][1] + poly[(i + 1) % n][1]) / 2)
        cands.add(round(math.atan2(m[1] - cy, m[0] - cx) % math.pi, 3))
    good = set()
    for ang in cands:
        dx, dy = math.cos(ang), math.sin(ang)
        refl = []
        for (x, y) in poly:
            vx, vy = x - cx, y - cy
            dot = vx * dx + vy * dy
            refl.append((cx + 2 * dot * dx - vx, cy + 2 * dot * dy - vy))
        if all(any(math.hypot(r[0] - p[0], r[1] - p[1]) < 1.0 for p in poly) for r in refl):
            good.add(round(ang % math.pi, 2) % round(math.pi, 2))
    # merge angles equal within 0.02 rad
    out = []
    for g in sorted(good):
        if not out or abs(g - out[-1]) > 0.02:
            out.append(g)
    if len(out) > 1 and abs(out[0] + math.pi - out[-1]) < 0.02:
        out.pop()
    return len(out)


# ---------------- items ----------------
assert sum(1 for k in kinds(ITEM['EXAMPLE']['figure']) if CORNERS[k] == 4) == 3   # worked example: 3 shapes have 4 corners


@check('L1U07-L01')
def _():
    return s([sum(1 for k in kinds(ITEM['L1U07-L01']['figure']) if CORNERS[k] == 5)])


@check('L1U07-S01')
def _():
    names = [NAME_OF_SIDES[CORNERS[k]] for k in kinds(ITEM['L1U07-S01']['figure'])]
    return {'a': [names[0]], 'b': [names[1]], 'c': [names[2]], 'd': [names[3]]}


@check('L1U07-S02')
def _():
    return {'a': s([5]), 'b': s([7]), 'c': s([CORNERS['circle']]), 'd': s([8])}


@check('L1U07-S03')
def _():
    ks = kinds(ITEM['L1U07-S03']['figure'])
    return {'a': s([ks.count('circle')]), 'b': s([ks.count('triangle')]), 'c': s([len(ks)])}


@check('L1U07-S04')
def _():
    def find(corners, equal=False):
        c = [k for k, v in CORNERS.items() if v == corners and (not equal or k == 'square') and k not in ('tall_rectangle',)]
        return c
    return {'a': find(5), 'b': find(4, True), 'c': [NAME_OF_SIDES[8]]}


@check('L1U07-S05')
def _():
    ks = kinds(ITEM['L1U07-S05']['figure'])
    return {'': [str(i + 1) for i, k in enumerate(ks) if CORNERS[k] == 4]}


@check('L1U07-S06')
def _():
    g = ITEM['L1U07-S06']['figure']['grids']
    a, b = g[0]['cols'] * g[0]['rows'], g[1]['cols'] * g[1]['rows']
    return {'a': s([a]), 'b': s([b]), 'c': ['A' if a > b else 'B']}


@check('L1U07-S07')
def _():
    fig = ITEM['L1U07-S07']['figure']
    sq = [e for e in fig['elements'] if 'poly' in e][0]['poly']
    cut = [e for e in fig['elements'] if e.get('dash')][0]['line']
    x0, x1 = sq[0][0], sq[1][0]
    y0, y1 = sq[0][1], sq[2][1]
    assert abs(cut[0] - (x0 + x1) / 2) < 1e-6 and cut[0] == cut[2]    # a straight cut down the middle
    w, h = (cut[0] - x0), (y1 - y0)
    name = 'square' if abs(w - h) < 1e-6 else 'rectangle'
    return {'a': [name], 'b': s([4])}


@check('L1U07-S08')
def _():
    sq = [e['poly'] for e in ITEM['L1U07-S08']['figure']['elements'] if 'poly' in e]
    left = [p for p in sq if p[0][0] < 150]
    right = [p for p in sq if p[0][0] > 150]

    def box(ps):
        xs = [pt[0] for p in ps for pt in p]; ys = [pt[1] for p in ps for pt in p]
        return max(xs) - min(xs), max(ys) - min(ys), (max(xs) - min(xs)) * (max(ys) - min(ys)) == sum((p[1][0] - p[0][0]) * (p[2][1] - p[1][1]) for p in ps)
    wl, hl, fl = box(left); wr, hr, fr = box(right)
    assert fl and fr
    return {'a': ['square' if wl == hl else 'rectangle'], 'b': ['square' if wr == hr else 'rectangle']}


@check('L1U07-S09')
def _():
    el = [e for e in ITEM['L1U07-S09']['figure']['elements'] if 'text' not in e]
    x0 = lambda e: e['poly'][0][0] if 'poly' in e else e['line'][0]
    left = {'elements': [e for e in el if x0(e) < 150]}
    right = {'elements': [e for e in el if x0(e) >= 150]}
    return {'a': s([len(count_triangles(left))]), 'b': s([len(count_triangles(right))])}








@check('L1U07-T01')
def _():
    g = ITEM['L1U07-T01']['figure']['grids'][0]
    c, r = g['cols'], g['rows']
    one = sum(1 for w in range(1, c + 1) for h in range(1, r + 1) if (w, h) == (1, 1)) * c * r
    two = (c - 1) * r
    return {'a': s([one]), 'b': s([two]), 'c': s([count_rects(c, r)])}


@check('L1U07-T02')
def _():
    areas = count_triangles(ITEM['L1U07-T02']['figure'])
    small = [a for a in areas if abs(a - min(areas)) < 1e-6]
    return {'a': s([len(small)]), 'b': s([len(areas)])}


@check('L1U07-T03')
def _():
    a_other = [k for k in ('square', 'hexagon', 'octagon') if CORNERS[k] == 11 - CORNERS['pentagon']]
    return {'a': a_other, 'b': s([15 - CORNERS['triangle'] - CORNERS['square']])}


@check('L1U07-G01')
def _():
    polys = [e['poly'] for e in ITEM['L1U07-G01']['figure']['elements'] if 'poly' in e]
    return {'a': s([fold_lines(polys[0])]), 'b': s([fold_lines(polys[1])]), 'c': s([fold_lines(polys[2])])}


@check('L1U07-G02')
def _():
    def rects(n):
        return [(a, b) for b in range(1, n + 1) for a in range(b, n + 1) if a * b == n]
    return {'a': s([len(rects(12))]), 'b': s([len(rects(9))])}


@check('L1U07-G03')
def _():
    g = ITEM['L1U07-G03']['figure']['grids'][0]
    c, r = g['cols'], g['rows']
    big = sum((c - 1) * (r - 1) for _ in range(1))
    return {'a': s([big]), 'b': s([count_squares(c, r)])}


@check('L1U07-C01')
def _():
    return [NAME_OF_SIDES[5]]


@check('L1U07-C02')
def _():
    return s([3 * CORNERS['square']])


@check('L1U07-C03')
def _():
    return s([len(count_triangles(ITEM['L1U07-C03']['figure']))])


@check('L1U07-C04')
def _():
    return s([CORNERS['triangle'] + 3])
