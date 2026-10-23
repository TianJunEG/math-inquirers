"""Independent checks for Level 5 Unit 4 (Triangle areas).  Areas are computed from vertex coordinates with the shoelace formula and by counting
grid squares; heights are computed as point-to-line distances.  No answer is copied from the book."""
import itertools
import math
from fractions import Fraction as Fr

CHECKS = {}


def check(id_):
    def deco(f):
        CHECKS[id_] = f
        return f
    return deco


def area(pts):
    """Shoelace formula (exact)."""
    s = Fr(0)
    for (x1, y1), (x2, y2) in zip(pts, pts[1:] + pts[:1]):
        s += Fr(x1) * Fr(y2) - Fr(x2) * Fr(y1)
    return abs(s) / 2


def fmt(x):
    x = Fr(x).limit_denominator(1000)
    if x.denominator == 1:
        return str(x.numerator)
    v = float(x)
    return f'{v:g}'


def dist_point_line(p, a, b):
    (x0, y0), (x1, y1), (x2, y2) = p, a, b
    return abs((x2 - x1) * (y1 - y0) - (x1 - x0) * (y2 - y1)) / math.hypot(x2 - x1, y2 - y1)


def length(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])


def grid_count(poly, step_div=4):
    """Area by counting small squares whose centres are inside the polygon (points on a 1/step_div grid)."""
    n = 0
    xs = [p[0] for p in poly]; ys = [p[1] for p in poly]
    k = step_div
    for i in range(int(min(xs) * k), int(max(xs) * k)):
        for j in range(int(min(ys) * k), int(max(ys) * k)):
            cx, cy = (i + .5) / k, (j + .5) / k
            inside = False
            for (x1, y1), (x2, y2) in zip(poly, poly[1:] + poly[:1]):
                if (y1 > cy) != (y2 > cy) and cx < (x2 - x1) * (cy - y1) / (y2 - y1) + x1:
                    inside = not inside
            n += inside
    return Fr(n, k * k)


@check('L5U04-L01')
def _():
    P, Q, R = (0, 9), (0, 0), (12, 0)
    return [fmt(area([P, Q, R]))]


@check('L5U04-S01')
def _():
    import math
    A, B, C = (0, 0), (8, 0), (4, 3)
    P, Q, R = (11, 0), (25, 0), (16, 12)
    assert [math.dist(A, C), math.dist(B, C), math.dist(P, R), math.dist(Q, R)] == [5, 5, 13, 15]   # the labelled slanting sides
    return {'a': [fmt(area([A, B, C]))], 'b': [fmt(area([P, Q, R]))]}


@check('L5U04-S02')
def _():
    P, Q, R = (0, 6), (0, 0), (8, 0)
    perp = lambda a, b, c: (b[0] - a[0]) * (c[0] - a[0]) + (b[1] - a[1]) * (c[1] - a[1]) == 0   # angle at a is a right angle
    side_when_PQ_base = 'QR' if perp(Q, P, R) else 'PR'
    return {'a': [fmt(area([P, Q, R]))], 'b': [fmt(dist_point_line(P, Q, R))], 'c': [side_when_PQ_base]}


@check('L5U04-S03')
def _():
    def h_of(area_, base):
        return next(h for h in range(1, 200) if Fr(base * h, 2) == area_)
    def b_of(area_, h):
        return next(b for b in range(1, 200) if Fr(b * h, 2) == area_)
    return {'a': [str(h_of(36, 9))], 'b': [str(b_of(45, 9))]}


@check('L5U04-S04')
def _():
    areas = {area([(0, 0), (12, 0), (px, 7)]) for px in range(0, 13)}
    verdict = 'is the same' if len(areas) == 1 else 'changes'
    return {'a': [fmt(area([(0, 0), (12, 0), (4, 7)]))], 'b': [verdict]}


@check('L5U04-S05')
def _():
    square = area([(0, 0), (8, 0), (8, 8), (0, 8)])
    top = area([(0, 8), (8, 8), (3, 13)])
    whole = area([(0, 0), (8, 0), (8, 8), (3, 13), (0, 8)])
    assert whole == square + top
    return [fmt(whole)]


@check('L5U04-S06')
def _():
    rect = area([(0, 0), (14, 0), (14, 9), (0, 9)])
    tri = area([(0, 0), (14, 0), (5, 9)])
    return {'a': [fmt(tri)], 'b': [fmt(rect - tri)]}


@check('L5U04-S07')
def _():
    poly = [(1, 1), (7, 1), (3, 6)]
    assert grid_count(poly, 8) - area(poly) < Fr(1, 4)
    return [fmt(area(poly))]


@check('L5U04-S08')
def _():
    return [fmt(area([(0, 0), (11, 0), (16, 12)]))]


@check('L5U04-S09')
def _():
    sq = 12 * 12
    h = next(h for h in range(1, 500) if Fr(18 * h, 2) == sq)
    return {'a': [str(sq)], 'b': [str(h)]}


@check('L5U04-S10')
def _():
    shape = [(0, 0), (12, 0), (12, 4), (8, 9), (0, 9)]
    return [fmt(area(shape))]


@check('L5U04-S11')
def _():
    pairs = [(b, h) for b in range(1, 100) for h in range(1, 100) if Fr(b * h, 2) == 9]
    return {'a': [str(len(pairs))], 'b': [str(next(h for b, h in pairs if b == 3))]}


@check('L5U04-S12')
def _():
    t = lambda v: 'True' if v else 'False'
    # (a) the height of a triangle is the distance from a vertex to the line of the opposite side (perpendicular by definition)
    a = True
    # (b) a slanting side of the 6-8-10 right triangle at the 10 cm side is not perpendicular to the base 8 (dot product != 0)
    P, Q, R = (0, 6), (0, 0), (8, 0)
    b = (P[0] - R[0]) * (Q[0] - R[0]) + (P[1] - R[1]) * (Q[1] - R[1]) == 0
    c = Fr(10 * 6, 2) == Fr(6 * 10, 2)
    return {'a': [t(a)], 'b': [t(b)], 'c': [t(c)]}


@check('L5U04-T01')
def _():
    P, Q, R = (0, 6), (0, 0), (8, 0)
    return [fmt(dist_point_line(Q, P, R))]


@check('L5U04-T02')
def _():
    A, B, C, D = (0, 0), (14, 0), (14, 10), (0, 10)
    M = ((B[0] + C[0]) / 2, (B[1] + C[1]) / 2)
    N = ((C[0] + D[0]) / 2, (C[1] + D[1]) / 2)
    return [fmt(area([A, M, N]))]


@check('L5U04-T03')
def _():
    B, C, A = (0, 0), (9, 0), (5, 7)
    whole = area([A, B, C])
    D = (Fr(1, 3) * C[0], 0)
    E = ((A[0] + D[0]) / 2, (A[1] + D[1]) / 2)
    scale = Fr(72) / whole
    return {'a': [fmt(area([A, B, D]) * scale)], 'b': [fmt(area([B, D, E]) * scale)]}


@check('L5U04-G01')
def _():
    D, E, F = (0, 16), (4, 0), (16, 8)
    return [fmt(area([D, E, F]))]


@check('L5U04-G02')
def _():
    poly = [(1, 1), (7, 3), (3, 6)]
    assert abs(grid_count(poly, 8) - area(poly)) < Fr(1, 4)
    return [fmt(area(poly))]


@check('L5U04-G03')
def _():
    A, B, C = (0, 0), (12, 0), (0, 16)
    whole = area([A, B, C])
    D = (A[0] + (B[0] - A[0]) / 4, A[1] + (B[1] - A[1]) / 4)
    E = (A[0] + (C[0] - A[0]) / 3, A[1] + (C[1] - A[1]) / 3)
    return [fmt(area([A, D, E]) * Fr(96) / whole)]


@check('L5U04-C01')
def _():
    import math
    assert math.dist((0, 0), (8, 6)) == 10 and math.dist((16, 0), (8, 6)) == 10
    return [fmt(area([(0, 0), (16, 0), (8, 6)]))]


@check('L5U04-C02')
def _():
    return [str(next(h for h in range(1, 200) if Fr(14 * h, 2) == 70))]


@check('L5U04-C03')
def _():
    return [fmt(area([(0, 0), (10, 0), (14, 3), (10, 6), (0, 6)]))]


@check('L5U04-C04')
def _():
    garden = area([(0, 0), (18, 0), (0, 10)])
    return [fmt(garden / 6)]
