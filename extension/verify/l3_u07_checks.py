"""Independent checks for Level 3 Unit 7 (Area architects): shapes made of squares are measured by listing the cells and counting boundary
edges; polygons by the shoelace formula and the sum of side lengths; rectangle riddles by searching whole-number sides."""
import itertools
from common import s

CHECKS = {}


def check(id_):
    def deco(f):
        CHECKS[id_] = f
        return f
    return deco


def only(xs):
    xs = list(xs)
    assert len(xs) == 1, xs
    return xs[0]


def cells_of(rows):
    return {(r, c) for r, row in enumerate(rows) for c, ch in enumerate(row) if ch == 'X'}


def area(cells):
    return len(cells)


def perimeter(cells):
    """count the unit edges that have a square on one side only"""
    n = 0
    for (r, c) in cells:
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            if (r + dr, c + dc) not in cells:
                n += 1
    return n


def poly_area(pts):
    a = 0
    for i in range(len(pts)):
        x1, y1 = pts[i]
        x2, y2 = pts[(i + 1) % len(pts)]
        a += x1 * y2 - x2 * y1
    return abs(a) // 2


def poly_perimeter(pts):
    return sum(abs(pts[i][0] - pts[(i + 1) % len(pts)][0]) + abs(pts[i][1] - pts[(i + 1) % len(pts)][1]) for i in range(len(pts)))


def rect(l, w):
    return l * w, 2 * (l + w)


@check('L3U07-L01')
def _():
    a, p = rect(9, 4)
    return s([a, p])


@check('L3U07-S01')
def _():
    A = cells_of(['XXXX', 'XXXX']); B = cells_of(['XXXX', 'X..X']); C = cells_of(['XXX', 'XXX'])
    same_area = [k for k, v in {'A,B': (A, B), 'A,C': (A, C), 'B,C': (B, C)}.items() if area(v[0]) == area(v[1]) and perimeter(v[0]) != perimeter(v[1])]
    return {'a': s([area(A), perimeter(A)]), 'b': s([area(B), perimeter(B)]), 'c': s([area(C), perimeter(C)]), 'd': [only(same_area)]}


@check('L3U07-S02')
def _():
    return {'a': s(rect(8, 6)), 'b': s(rect(11, 4))}


@check('L3U07-S03')
def _():
    side36 = only(x for x in range(1, 40) if 4 * x == 36)
    return {'a': s([4 * 7]), 'b': s([7 * 7]), 'c': s([side36])}


@check('L3U07-S04')
def _():
    sols = [(w, 9 * w) for w in range(1, 30) if 2 * (9 + w) == 30]
    return {'a': s([only(sols)[0]]), 'b': s([only(sols)[1]])}


@check('L3U07-S05')
def _():
    along = only(n for n in range(1, 30) if n * 3 == 15)
    across = only(n for n in range(1, 30) if n * 3 == 9)
    return {'a': s([along]), 'b': s([across]), 'c': s([along * across])}


@check('L3U07-S06')
def _():
    rects = [(l, w) for l in range(1, 14) for w in range(1, l + 1) if 2 * (l + w) == 14]
    return {'a': s([len(rects)]), 'b': s([max(l * w for l, w in rects)])}


@check('L3U07-S07')
def _():
    pts = [(0, 0), (8, 0), (8, 3), (4, 3), (4, 6), (0, 6)]
    side = lambda i: abs(pts[i][0] - pts[(i + 1) % 6][0]) + abs(pts[i][1] - pts[(i + 1) % 6][1])
    return {'a': s([side(2)]), 'b': s([side(3)]), 'c': s([poly_area(pts)]), 'd': s([poly_perimeter(pts)])}


@check('L3U07-S08')
def _():
    st = cells_of(['XXXXXX', 'XXXX..', 'XX....'])
    full = cells_of(['XXXXXX'] * 3)
    return {'a': s([area(st)]), 'b': s([perimeter(st)]), 'c': s([len(full - st)]), 'd': s([perimeter(full)])}


@check('L3U07-S09')
def _():
    mei_p = rect(10, 2)[1]
    side = only(x for x in range(1, 40) if 4 * x == mei_p)
    mei_a, ben_a = rect(10, 2)[0], side * side
    return {'a': s([side]), 'b': ['Ben’s' if ben_a > mei_a else 'Mei’s'], 'c': s([abs(ben_a - mei_a)])}


@check('L3U07-S10')
def _():
    base = cells_of(['.XXX.', '..X..'])     # the 4-square figure without the candidate squares
    assert perimeter(base) == 10
    cand = {'A': (0, 4), 'B': (2, 2), 'C': (1, 1)}
    res = {k: perimeter(base | {v}) for k, v in cand.items()}
    return {'a': [k for k, v in res.items() if v == 12], 'b': [only(k for k, v in res.items() if v == 10)]}


@check('L3U07-S11')
def _():
    side = only(x for x in range(1, 40) if x * x == 64)
    return {'a': s([side]), 'b': s([4 * side])}


@check('L3U07-T01')
def _():
    one = rect(8, 4)[1]
    return {'a': s([one]), 'b': s([2 * one]), 'c': s([2 * one - 4 * 8])}


@check('L3U07-T02')
def _():
    sols = [(l, w) for l in range(1, 40) for w in range(1, l + 1) if l * w == 36 and 2 * (l + w) == 26]
    l, w = only(sols)
    return {'a': s([l]), 'b': s([w])}


@check('L3U07-T03')
def _():
    side = [(0, 0), (7, 0), (7, 3), (4, 3), (4, 4), (0, 4)]
    stack = [(0, 0), (4, 0), (4, 4), (3, 4), (3, 7), (0, 7)]     # the 3 cm square on top of the 4 cm square, left edges level
    return {'a': s([poly_area(side)]), 'b': s([poly_perimeter(side)]), 'c': s([poly_perimeter(stack)])}


@check('L3U07-G01')
def _():
    per = lambda n: perimeter(cells_of(['X' * n]))
    return {'a': s([per(10)]), 'b': s([only(n for n in range(1, 60) if per(n) == 30)])}


@check('L3U07-G02')
def _():
    outer = (6 + 2 * 1, 4 + 2 * 1)
    path = outer[0] * outer[1] - 6 * 4
    return {'a': s(list(outer)), 'b': s([path])}


@check('L3U07-G03')
def _():
    best = max(t for t in range(1, 13) if 12 % t == 0 and 10 % t == 0)
    return {'a': s([best]), 'b': s([(12 // best) * (10 // best)])}


@check('L3U07-C01')
def _():
    return s([rect(9, 5)[0]])


@check('L3U07-C02')
def _():
    return s([only(x for x in range(1, 50) if 4 * x == 20)])


@check('L3U07-C03')
def _():
    sh = cells_of(['XXX', 'XX.', 'XX.'])
    return s([area(sh), perimeter(sh)])


@check('L3U07-C04')
def _():
    return s([only(l for l in range(1, 30) if 2 * (l + 4) == 22)])
