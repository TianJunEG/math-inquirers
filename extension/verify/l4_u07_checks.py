"""Independent checks for Level 4 Unit 7 (area and perimeter): areas and perimeters of drawn shapes are computed from the corner points of the figure
data (shoelace formula and edge lengths), and every printed length label is cross-checked against the drawing; puzzles are solved by brute force."""
from common import load_unit
CHECKS = {}
U = load_unit(4, 7)
ITEM = {i['id']: i for i in [U['learn']['try']] + U['items']}


def check(id_):
    def deco(f):
        CHECKS[id_] = f
        return f
    return deco


def s(xs):
    return [str(x) for x in xs]


def area(pts):
    a = 0
    for i in range(len(pts)):
        x1, y1 = pts[i]
        x2, y2 = pts[(i + 1) % len(pts)]
        a += x1 * y2 - x2 * y1
    return abs(a) // 2


def perim(pts):
    return sum(abs(pts[i][0] - pts[(i + 1) % len(pts)][0]) + abs(pts[i][1] - pts[(i + 1) % len(pts)][1]) for i in range(len(pts)))


def seg(pts, i):
    (x1, y1), (x2, y2) = pts[i], pts[(i + 1) % len(pts)]
    return abs(x2 - x1) + abs(y2 - y1)


def shape(id_, k=0):
    return ITEM[id_]['figure']['shapes'][k]


def labels_ok(sh):
    """Every numeric label 'N cm' must equal the drawn length of its edge."""
    for lab in sh.get('labels', []):
        t = lab['text']
        if t.endswith(' cm'):
            assert int(t[:-3]) == seg(sh['pts'], lab['seg']), (t, lab)


def tiles_area_perim(cells):
    cs = {tuple(c) for c in cells}
    p = 0
    for (x, y) in cs:
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            if (x + dx, y + dy) not in cs:
                p += 1
    return len(cs), p


def factor_pairs(n):
    return [(n // d, d) for d in range(1, n + 1) if n % d == 0 and n // d >= d]


@check('L4U07-L01')
def _():
    return s([12 * 5 - 3 * 2])


@check('L4U07-S01')
def _():
    sh = shape('L4U07-S01')
    labels_ok(sh)
    pts = sh['pts']
    a, b = seg(pts, 2), seg(pts, 3)
    return {'a': s([a, b]), 'b': s([area(pts)]), 'c': s([perim(pts)])}


@check('L4U07-S02')
def _():
    sh = shape('L4U07-S02')
    labels_ok(sh)
    pts = sh['pts']
    whole = 12 * 9
    corner = seg(pts, 2) * seg(pts, 1)
    assert area(pts) == whole - corner
    return {'a': s([whole]), 'b': s([corner]), 'c': s([area(pts)])}


@check('L4U07-S03')
def _():
    rows = ITEM['L4U07-S03']['figure']['rows']
    out = []
    for length, _w, _p in rows:
        L = int(length)
        w = next(w for w in range(1, 100) if L * w == 28)
        out += [w, 2 * (L + w)]
    perims = [out[1], out[3], out[5]]
    assert min(perims) == min(2 * (a + b) for a, b in factor_pairs(28))
    return {'a': s(out), 'b': s([min(perims)])}


@check('L4U07-S04')
def _():
    sh = ITEM['L4U07-S04']['figure']['shapes']
    res = [tiles_area_perim(x['cells']) for x in sh]
    assert [x['name'] for x in sh] == ['A', 'B', 'C']
    best = min(range(3), key=lambda i: res[i][1])
    return {'a': s([res[0][0]]), 'b': s([r[1] for r in res]), 'c': ['ABC'[best]]}


@check('L4U07-S05')
def _():
    sh = shape('L4U07-S05')
    labels_ok(sh)
    pts = sh['pts']
    # 4 equal steps of 3 across and 2 up
    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]
    assert max(xs) - min(xs) == 4 * 3 and max(ys) - min(ys) == 4 * 2
    return {'a': s([perim(pts)]), 'b': s([area(pts)])}


@check('L4U07-S06')
def _():
    sh = shape('L4U07-S06')
    outer, hole = sh['pts'], sh['hole']
    ow, oh = max(p[0] for p in outer), max(p[1] for p in outer)
    hw, hh = max(p[0] for p in hole) - min(p[0] for p in hole), max(p[1] for p in hole) - min(p[1] for p in hole)
    assert (ow, oh, hw, hh) == (16, 10, 4, 4)
    return {'a': s([area(outer) - area(hole)]), 'b': s([perim(outer) + perim(hole)])}


@check('L4U07-S07')
def _():
    f = ITEM['L4U07-S07']['figure']['shapes']
    a, b = f[0]['pts'], f[1]['pts']
    assert area(a) == area(b)
    return {'a': s([area(a), area(b)]), 'b': s([perim(a), perim(b)])}


@check('L4U07-S08')
def _():
    w = next(w for w in range(1, 100) if 9 * w == 72)
    return {'a': s([w]), 'b': s([2 * (9 + w)])}


@check('L4U07-S09')
def _():
    tiles_l, tiles_w = 12 // 2, 8 // 2
    total = tiles_l * tiles_w
    border = sum(1 for x in range(tiles_l) for y in range(tiles_w) if x in (0, tiles_l - 1) or y in (0, tiles_w - 1))
    return {'a': s([total]), 'b': s([border])}


@check('L4U07-T01')
def _():
    sol = [(l, w) for w in range(1, 40) for l in range(1, 40) if 2 * (l + w) == 42 and l == w + 5]
    assert len(sol) == 1
    return s([sol[0][0] * sol[0][1]])


@check('L4U07-T02')
def _():
    rects = [(l, w) for l in range(1, 37) for w in range(1, l + 1) if l * w == 36]
    return {'a': s([len(rects)]), 'b': s([max(2 * (l + w) for l, w in rects)])}


@check('L4U07-T03')
def _():
    L, W, k = 15, 9, 3
    cells = {(x, y) for x in range(L) for y in range(W)}
    corners = {(x, y) for x in range(L) for y in range(W) if (x < k or x >= L - k) and (y < k or y >= W - k)}
    left = cells - corners
    # perimeter by counting the edges of cells that border a cell outside the shape
    edges = sum(1 for (x, y) in left for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)) if (x + dx, y + dy) not in left)
    return {'a': s([len(left)]), 'b': s([edges])}


@check('L4U07-G01')
def _():
    f = ITEM['L4U07-G01']['figure']['shapes'][0]
    n, p = tiles_area_perim(f['cells'])
    assert n == 3
    side = next(sd for sd in range(1, 100) if sd * p == 40)
    return s([n * side * side])


@check('L4U07-G02')
def _():
    sols = [(l, w) for w in range(1, 60) for l in range(w, 60) if l * w == 2 * (l + w)]
    assert (4, 4) in sols and len(sols) == 2
    other = [x for x in sols if x != (4, 4)][0]
    return s(other)


@check('L4U07-G03')
def _():
    f = ITEM['L4U07-G03']['figure']['shapes'][0]
    sq = lambda x0, y0: {(x, y) for x in range(x0, x0 + 6) for y in range(y0, y0 + 6)}
    cells = sq(0, 0) | sq(4, 4)            # two 6 by 6 squares overlapping in a 2 by 2 corner
    assert len(sq(0, 0) & sq(4, 4)) == 4
    assert area(f['pts']) == len(cells)
    edges = sum(1 for (x, y) in cells for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)) if (x + dx, y + dy) not in cells)
    assert perim(f['pts']) == edges
    return {'a': s([len(cells)]), 'b': s([edges])}


@check('L4U07-G04')
def _():
    def dark(n):
        return n * n - (n - 2) * (n - 2)
    return {'a': s([dark(8)]), 'b': s([next(n for n in range(2, 100) if dark(n) == 60)])}


@check('L4U07-C01')
def _():
    sh = shape('L4U07-C01')
    labels_ok(sh)
    return s([area(sh['pts'])])


@check('L4U07-C02')
def _():
    w = next(w for w in range(1, 100) if 12 * w == 60)
    return s([2 * (12 + w)])


@check('L4U07-C03')
def _():
    return s([(10 + 2) * (7 + 2) - 10 * 7])


@check('L4U07-C04')
def _():
    return s([min(2 * (a + b) for a, b in factor_pairs(24))])
