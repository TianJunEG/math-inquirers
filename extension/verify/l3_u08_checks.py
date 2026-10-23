"""Independent checks for Level 3 Unit 8 (Angle and line detectives): angles are measured from the coordinates of the drawing with vector
cross and dot products (right angle: dot product 0), parallel lines have cross product 0, and counts are made by listing pairs."""
import itertools
import math
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


def cross(u, v):
    return u[0] * v[1] - u[1] * v[0]


def dot(u, v):
    return u[0] * v[0] + u[1] * v[1]


def vec(a, b):
    return (b[0] - a[0], b[1] - a[1])


def angles_of(poly):
    """interior angle in degrees at each vertex of a simple polygon (list of points)"""
    n = len(poly)
    area2 = sum(cross(poly[i], poly[(i + 1) % n]) for i in range(n))
    sign = 1 if area2 > 0 else -1
    out = []
    for i in range(n):
        d_in = vec(poly[i - 1], poly[i])
        d_out = vec(poly[i], poly[(i + 1) % n])
        turn = math.degrees(math.atan2(cross(d_in, d_out) * sign, dot(d_in, d_out)))     # positive: convex corner
        out.append(round(180 - turn, 6))
    return out


def right_angles(poly):
    return sum(1 for a in angles_of(poly) if abs(a - 90) < 1e-6)


def greater_angles(poly):
    return sum(1 for a in angles_of(poly) if a > 90 + 1e-6 and a > 180 - 1e-6 + 0)     # dents: reflex corners


def reflex(poly):
    return sum(1 for a in angles_of(poly) if a > 180 + 1e-6)


def cmp90(deg):
    return 'smaller than' if deg < 90 else ('equal to' if deg == 90 else 'greater than')


def seg_dir(sg):
    return (sg[2] - sg[0], sg[3] - sg[1])


def has_pair(segments, kind):
    for a, b in itertools.combinations(segments, 2):
        da, db = seg_dir(a), seg_dir(b)
        if kind == 'parallel' and cross(da, db) == 0:
            return True
        if kind == 'perpendicular' and dot(da, db) == 0:
            return True
    return False


LET = {'F': [(0, 0, 0, 4), (0, 4, 3, 4), (0, 2, 2, 2)], 'V': [(0, 4, 1.5, 0), (1.5, 0, 3, 4)],
       'N': [(0, 0, 0, 4), (0, 4, 3, 0), (3, 0, 3, 4)], 'L': [(0, 4, 0, 0), (0, 0, 3, 0)],
       'E': [(0, 0, 0, 4), (0, 4, 3, 4), (0, 2, 2.5, 2), (0, 0, 3, 0)], 'H': [(0, 0, 0, 4), (3, 0, 3, 4), (0, 2, 3, 2)],
       'T': [(0, 4, 3, 4), (1.5, 4, 1.5, 0)], 'Y': [(0, 4, 1.5, 2), (3, 4, 1.5, 2), (1.5, 2, 1.5, 0)], 'Z': [(0, 4, 3, 4), (3, 4, 0, 0), (0, 0, 3, 0)]}


@check('L3U08-L01')
def _():
    return [cmp90(70)]


@check('L3U08-S01')
def _():
    deg = {'A': 90, 'B': 55, 'C': 125, 'D': 150, 'E': 40, 'F': 90}
    return {'a': [k for k, v in deg.items() if v < 90], 'b': [k for k, v in deg.items() if v == 90], 'c': [k for k, v in deg.items() if v > 90]}


SHAPE_A = [(0, 0), (4, 0), (4, 2), (2, 2), (2, 4), (0, 4)]
SHAPE_B = [(0, 4), (4, 4), (4, 3), (3, 3), (3, 0), (1, 0), (1, 3), (0, 3)]
SHAPE_C = [(0, 0), (4, 0), (3, 4), (0, 4)]


@check('L3U08-S02')
def _():
    return {'a': s([right_angles(SHAPE_A)]), 'b': s([right_angles(SHAPE_B)]), 'c': s([right_angles(SHAPE_C)])}


@check('L3U08-S03')
def _():
    names = ['F', 'V', 'N', 'L']
    return {'a': [n for n in names if has_pair(LET[n], 'parallel')], 'b': [n for n in names if has_pair(LET[n], 'perpendicular')]}


@check('L3U08-S04')
def _():
    n = 4
    rays = range(n)
    by_size = {k: sum(1 for i, j in itertools.combinations(rays, 2) if j - i == k) for k in range(1, n)}
    return {'a': s([by_size[1]]), 'b': s([by_size[2]]), 'c': s([by_size[3]]), 'd': s([sum(by_size.values())])}


@check('L3U08-S05')
def _():
    lines = {'AB': (1, 1, 5, 3), 'P': (2, 5, 4, 1), 'Q': (0, 4, 4, 2), 'R': (2, 0, 6, 2), 'S': (4, 4, 6, 6)}
    ab = seg_dir(lines['AB'])
    par = [k for k, v in lines.items() if k != 'AB' and cross(ab, seg_dir(v)) == 0]
    per = [k for k, v in lines.items() if k != 'AB' and dot(ab, seg_dir(v)) == 0]
    return {'a': [only(par)], 'b': [only(per)]}


@check('L3U08-S06')
def _():
    rails = [(0, 0, 0, 4), (3, 0, 3, 4)]
    rungs = [(0, 1, 3, 1), (0, 2, 3, 2), (0, 3, 3, 3)]
    def at_junction(rung, rail):
        # the rung ends on the rail: its end point lies on the rail line; a rung end inside the rail makes 2 right angles
        end = [(rung[0], rung[1]), (rung[2], rung[3])]
        for e in end:
            if rail[0] == rail[2] == e[0] and min(rail[1], rail[3]) < e[1] < max(rail[1], rail[3]) and dot(seg_dir(rung), seg_dir(rail)) == 0:
                return 2
        return 0
    per_rung = sum(at_junction(rungs[0], r) for r in rails)
    total = sum(at_junction(g, r) for g in rungs for r in rails)
    return {'a': s([per_rung]), 'b': s([total])}


@check('L3U08-S07')
def _():
    names = ['N', 'E', 'S', 'W']
    face = lambda start, turns_right: names[(names.index(start) + turns_right) % 4]
    return {'a': [face('N', 1)], 'b': [face('N', 3)], 'c': [face('N', -2)]}


@check('L3U08-S08')
def _():
    rect = [(0, 0), (5, 0), (5, 3), (0, 3)]
    edges = [(rect[i], rect[(i + 1) % 4]) for i in range(4)]
    pairs = sum(1 for a, b in itertools.combinations(edges, 2) if cross(vec(*a), vec(*b)) == 0)
    # most right angles a triangle with corners on a 0..6 grid can have
    best = 0
    pts = [(x, y) for x in range(7) for y in range(7)]
    for tri in itertools.combinations(pts, 3):
        if cross(vec(tri[0], tri[1]), vec(tri[0], tri[2])) == 0:
            continue
        best = max(best, sum(1 for i in range(3) if dot(vec(tri[i], tri[(i + 1) % 3]), vec(tri[i], tri[(i + 2) % 3])) == 0))
    meet = [e for e in [(edges[0], edges[1])] if dot(vec(*e[0]), vec(*e[1])) == 0]
    return {'a': s([right_angles(rect)]), 'b': s([pairs]), 'c': s([best]), 'd': ['perpendicular' if meet else 'parallel']}


@check('L3U08-S09')
def _():
    a = dot((1, 0), (0, 1)) == 0                      # perpendicular lines meet at a right angle (definition, tested on x and y axes)
    b = cross((2, 1), (4, 2)) == 0 and cross(vec((0, 0), (0, 3)), (2, 1)) != 0   # parallel lines 2 apart: they never meet
    rails = [(0, 0, 0, 4), (3, 0, 3, 4)]
    c = all(dot(seg_dir((0, 1, 3, 1)), seg_dir(r)) == 0 for r in rails)
    d = dot((1, 0), (1, 1)) != 0                      # two crossing lines that are not perpendicular
    return {'a': ['True' if a else 'False'], 'b': ['False' if b else 'True'], 'c': ['True' if c else 'False'], 'd': ['False' if d else 'True']}


@check('L3U08-S10')
def _():
    ang = angles_of(SHAPE_A)[3]      # corner (2, 2): the dent
    return {'a': ['Yes' if ang == 90 else 'No'], 'b': [cmp90(ang if ang <= 180 else ang)]}


@check('L3U08-T01')
def _():
    pairs = lambda n: sum(1 for i, j in itertools.combinations(range(n), 2))
    assert (pairs(2), pairs(3), pairs(4)) == (1, 3, 6)
    return {'a': s([pairs(5)]), 'b': s([pairs(7)])}


@check('L3U08-T02')
def _():
    A, B, C = (0, 2), (4, 4), (2, 6)
    dots = {'P': (2, 0), 'Q': (4, 0), 'R': (5, 0), 'S': (6, 0)}      # the dots on the bottom row
    ab = vec(A, B)
    return {'a': [only(k for k, d in dots.items() if dot(ab, vec(C, d)) == 0)]}


STEPS_POLY = [(0, 0), (4, 0), (4, 1), (3, 1), (3, 2), (2, 2), (2, 3), (1, 3), (1, 4), (0, 4)]


@check('L3U08-T03')
def _():
    p = STEPS_POLY
    # (c): an orthogonal shape has (right angles) - (dents) = 4, and right + dents = corners
    corners, dents = 14, 5
    right = [r for r in range(corners + 1) if r + dents == corners and r - dents == 4]
    return {'a': s([reflex(p)]), 'b': s([right_angles(p)]), 'c': s([only(right)])}


@check('L3U08-G01')
def _():
    right = 90
    return {'a': s([right + right]), 'b': s([4 * right]), 'c': s([right // 2]), 'd': s([3 * right])}


@check('L3U08-G02')
def _():
    ups = [(1.5, -1.2, 1.5, 1.8), (4.5, -1.2, 4.5, 1.8)]
    flat = (0, 0, 6, 0)
    both_perp = all(dot(seg_dir(u), seg_dir(flat)) == 0 for u in ups)
    parallel = cross(seg_dir(ups[0]), seg_dir(ups[1])) == 0
    d0 = seg_dir(ups[0])
    L = (-d0[1], d0[0])                                   # the direction perpendicular to the first upright
    other_perp = dot(L, seg_dir(ups[1])) == 0
    return {'a': ['parallel' if both_perp and parallel else 'perpendicular'], 'b': ['Yes' if other_perp and parallel else 'No']}


@check('L3U08-G03')
def _():
    def board(h, v):
        crossings = h * v
        return h * (h - 1) // 2 + v * (v - 1) // 2, 4 * crossings
    return {'a': s([board(2, 2)[0]]), 'b': s([board(2, 2)[1]]), 'c': s([board(3, 3)[1]])}


@check('L3U08-C01')
def _():
    return [cmp90(120)]


@check('L3U08-C02')
def _():
    return [n for n in ['E', 'H', 'V', 'Y'] if has_pair(LET[n], 'parallel')]


@check('L3U08-C03')
def _():
    rect = [(0, 0), (5, 0), (5, 3), (0, 3)]
    edges = [(rect[i], rect[(i + 1) % 4]) for i in range(4)]
    return s([sum(1 for a, b in itertools.combinations(edges, 2) if cross(vec(*a), vec(*b)) == 0)])


@check('L3U08-C04')
def _():
    names = ['N', 'E', 'S', 'W']
    return [names[(names.index('E') - 1) % 4]]
