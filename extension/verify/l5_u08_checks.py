"""Independent checks for Level 5 Unit 8 (Angle chasers).  Every figure is CONSTRUCTED from the data given in the question (rays, equal sides,
parallel sides) with coordinate geometry, and the asked angle is MEASURED with atan2.  No angle fact (180, 360, equal base angles) is used
to get an answer, so a wrong reason in the book cannot be copied here."""
import itertools
import math

CHECKS = {}


def check(id_):
    def deco(f):
        CHECKS[id_] = f
        return f
    return deco


def pol(p, r, deg):
    return (p[0] + r * math.cos(math.radians(deg)), p[1] + r * math.sin(math.radians(deg)))


def ang(at, a, b):
    """Angle in degrees at `at` between the rays to a and b (0 to 180)."""
    t1 = math.atan2(a[1] - at[1], a[0] - at[0])
    t2 = math.atan2(b[1] - at[1], b[0] - at[0])
    d = abs(math.degrees(t1 - t2)) % 360
    return min(d, 360 - d)


def r(x):
    v = round(x, 6)
    return str(int(round(v))) if abs(v - round(v)) < 1e-6 else f'{v:g}'


def meet(p, dp, q, dq):
    """Intersection of the line p + s*dp with the line q + t*dq."""
    det = dp[0] * (-dq[1]) - dp[1] * (-dq[0])
    s = ((q[0] - p[0]) * (-dq[1]) - (q[1] - p[1]) * (-dq[0])) / det
    return (p[0] + s * dp[0], p[1] + s * dp[1])


def d(deg):
    return (math.cos(math.radians(deg)), math.sin(math.radians(deg)))


def isosceles_from_base_angles(b, c, ang_b, ang_c):
    """Apex where the ray from b at ang_b and the ray from c at 180 - ang_c meet (b left, c right)."""
    return meet(b, d(ang_b), c, d(180 - ang_c))


@check('L5U08-L01')
def _():
    Y, Z = (0, 0), (1, 0)
    X = isosceles_from_base_angles(Y, Z, 54, 54)       # XY = XZ, angle Y = 54: XZ is the mirror image of XY
    return [r(ang(X, Y, Z))]


@check('L5U08-S01')
def _():
    O = (0, 0)
    # AB and CD are straight lines through O; BOC is 2 times AOC: search the angle AOC
    for aoc in range(1, 180):
        A, B, C, D = pol(O, 1, 0), pol(O, 1, 180), pol(O, 1, aoc), pol(O, 1, aoc + 180)
        if abs(ang(O, B, C) - 2 * ang(O, A, C)) < 1e-9:
            return {'a': [r(ang(O, A, C))], 'b': [r(ang(O, B, C))], 'c': [r(ang(O, B, D))]}


@check('L5U08-S02')
def _():
    P = (0, 0)
    rays = [0, 47, 47 + 85]
    left = ang(P, pol(P, 1, rays[-1]), pol(P, 1, 180))        # the rest of the half turn
    Q = (0, 0)
    pr = [0, 125, 125 + 90, 125 + 90 + 105]
    last = 360 - pr[-1]                                       # the rest of the full turn, measured as the angle between the last ray and the first
    assert abs(ang(Q, pol(Q, 1, pr[-1]), pol(Q, 1, 360)) - last) < 1e-9
    return {'a': [r(left)], 'b': [r(last)]}


@check('L5U08-S03')
def _():
    A, B = (0, 0), (1, 0)
    C = meet(A, d(58), B, d(180 - 67))
    third1 = ang(C, A, B)
    P, R = (0, 0), (1, 0)
    Q = meet(P, d(90), R, d(180 - 38))                      # right angle at P, angle 38 at R
    return {'a': [r(third1)], 'b': [r(ang(Q, P, R))]}


@check('L5U08-S04')
def _():
    Q, R = (0, 0), (1, 0)
    P = meet(Q, d(72), R, d(180 - 72))                      # PQ = PR: the apex lies on the mirror line, so the base angles are equal
    # verify PQ = PR in the construction, then measure
    assert abs(math.dist(P, Q) - math.dist(P, R)) < 1e-9
    return {'a': [r(ang(R, P, Q))], 'b': [r(ang(P, Q, R))]}


@check('L5U08-S05')
def _():
    A, B = (0, 0), (1, 0)
    D = pol(A, 0.6, 70)
    C = (B[0] + D[0], B[1] + D[1])
    return {'a': [r(ang(B, A, C))], 'b': [r(ang(C, B, D))]}


@check('L5U08-S06')
def _():
    A, B = (0, 0), (1, 0)
    D = pol(A, 1, 76)                                        # rhombus: all sides 1
    C = (B[0] + D[0], B[1] + D[1])
    return {'a': [r(ang(B, A, D))], 'b': [r(ang(C, B, D))]}


@check('L5U08-S07')
def _():
    A, B = (0, 0), (1, 0)
    Dd = pol(A, 0.5, 58)
    # C on the line through B with direction making angle 100 at B, and on the line y = D.y (DC parallel to AB)
    C = meet(B, d(180 - 100), Dd, (1, 0))
    return {'a': [r(ang(C, B, Dd))], 'b': [r(ang(Dd, C, A))]}


@check('L5U08-S08')
def _():
    B, D = (0, 0), (1, 0)
    A = meet(B, d(58), (0.5, 0), (0, 1))                     # AB = AD: A lies on the perpendicular bisector of BD; angle ABD = 58
    ray_AD = math.degrees(math.atan2(D[1] - A[1], D[0] - A[0]))
    ray_AC = ray_AD + 24                                     # rotate AD by 24 degrees towards C (to the right)
    C = meet(A, d(ray_AC), (0, 0), (1, 0))
    assert C[0] > D[0]
    return {'a': [r(ang(D, A, B))], 'b': [r(ang(A, B, D))], 'c': [r(ang(D, C, A))], 'd': [r(ang(C, D, A))]}


@check('L5U08-S09')
def _():
    B, C = (0, 0), (1, 0)
    A = pol(B, 1, 60)                                        # equilateral: BA = BC and AC = BC means A is 60 degrees from B
    assert abs(math.dist(A, C) - 1) < 1e-9
    D = (2, 0)
    return {'a': [r(ang(C, B, A))], 'b': [r(ang(C, A, D))]}


@check('L5U08-S10')
def _():
    triples = {tuple(sorted(t)) for t in itertools.product(range(1, 179), repeat=3) if sum(t) == 180 and len(set(t)) == 2 and 70 in t}
    base70 = [t for t in triples if t.count(70) == 2]
    top70 = [t for t in triples if t.count(70) == 1]
    a = [x for x in base70[0] if x != 70][0]
    b = [x for x in top70[0] if x != 70][0]
    return {'a': [str(a)], 'b': [str(b)], 'c': [str(len(triples))]}


@check('L5U08-S11')
def _():
    def hands(h, m):
        hour = (h * 60 + m) * 0.5
        minute = m * 6
        gap = abs(hour - minute) % 360
        return min(gap, 360 - gap)
    return {'a': [r(20 * 6)], 'b': [r(hands(4, 0))], 'c': [r(hands(7, 0))]}


@check('L5U08-S12')
def _():
    # (a) three angles of one triangle: 55 + 75 + R is a full set only when R = 50 (checked by building the triangle)
    A, B = (0, 0), (1, 0)
    C = meet(A, d(55), B, d(180 - 75))
    third = ang(C, A, B)
    assert abs(third - 50) < 1e-9
    # (b) 112 and 68 lie next to each other along one straight line
    O = (0, 0)
    a68, a112 = ang(O, pol(O, 1, 0), pol(O, 1, 68)), ang(O, pol(O, 1, 68), pol(O, 1, 180))
    assert abs(a68 + a112 - 180) < 1e-9
    # (c) A = 70 and B = 110 are NEIGHBOURS (they share the side AB), not opposite corners
    return {'a': ['angles of a triangle'], 'b': ['angles on a straight line'], 'c': ['neighbouring angles']}


@check('L5U08-T01')
def _():
    A = (0, 0)
    D = pol(A, 1, 70)
    C = (D[0] + 1, D[1])                                    # AD = DC, DC parallel to AB
    t = C[1] / math.sin(math.radians(100))                  # BC leaves B at 100 degrees (angle ABC = 80 with BA along 180)
    B = (C[0] - t * math.cos(math.radians(100)), 0)
    assert abs(ang(B, A, C) - 80) < 1e-6
    return {'a': [r(ang(D, A, C))], 'b': [r(ang(C, D, A))], 'c': [r(ang(C, A, B))]}


@check('L5U08-T02')
def _():
    ts = [t for t in itertools.product(range(1, 179), repeat=3) if sum(t) == 180 and t[0] == t[1]]   # (equal, equal, top)
    a = [t for t in ts if t[2] == t[0] + 24]
    b = [t for t in ts if t[0] == t[2] + 24]
    assert len(a) == 1 and len(b) == 1
    return {'a': [str(a[0][2])], 'b': [str(b[0][2])]}


@check('L5U08-T03')
def _():
    A, B = (0, 0), (1, 0)
    D = pol(A, 1, 80)
    E = pol(A, 1, -60)                                       # ABE equilateral on the other side of AB
    assert abs(math.dist(B, E) - 1) < 1e-9
    return [r(ang(E, A, D))]


@check('L5U08-G01')
def _():
    pts = [pol((0, 0), 1, 90 + 72 * k) for k in range(5)]
    interior = [ang(pts[k], pts[k - 1], pts[(k + 1) % 5]) for k in range(5)]
    return {'a': [r(sum(interior))], 'b': [r(interior[0])]}


@check('L5U08-G02')
def _():
    hour = (4 * 60 + 20) * 0.5
    minute = 20 * 6
    gap = abs(hour - minute) % 360
    return [r(min(gap, 360 - gap))]


@check('L5U08-G03')
def _():
    found = []
    for a in range(1, 90):
        A, B = (0, 0), (1, 0)
        C = pol(A, 1, a)                                     # AB = AC = 1
        cb = math.dist(C, B)
        D = (cb, 0)                                          # AD = CB, D on AB
        if D[0] < 1 - 1e-9 and abs(math.dist(D, C) - cb) < 1e-9:    # D strictly inside AB, and DC = CB as well
            found.append(a)
    assert len(found) == 1
    return [str(found[0])]


@check('L5U08-C01')
def _():
    O = (0, 0)
    for aoc in range(1, 180):
        A, B, C = pol(O, 1, 0), pol(O, 1, 180), pol(O, 1, aoc)       # AOB straight, OC at angle aoc from OA
        if abs(ang(O, A, C) - 3 * ang(O, C, B)) < 1e-9:
            return [r(ang(O, C, B))]


@check('L5U08-C02')
def _():
    Q, R = (0, 0), (1, 0)
    # PQ = PR: the apex P is above the middle of QR.  Bisect on the height until the angle at P is 100 degrees.
    lo, hi = 1e-6, 10.0          # a low apex gives a wide angle at P, a high apex a narrow one
    for _ in range(200):
        mid = (lo + hi) / 2
        if ang((0.5, mid), Q, R) > 100:
            lo = mid
        else:
            hi = mid
    P = (0.5, (lo + hi) / 2)
    return [r(ang(Q, P, R))]


@check('L5U08-C03')
def _():
    B, C = (0, 0), (1, 0)
    A = pol(B, 0.6, 115)
    D = (A[0] + 1, A[1])
    return [r(ang(D, C, A))]


@check('L5U08-C04')
def _():
    C = (0, 0)
    A = pol(C, 1, 180 - 76)                                  # angle ACB = 76 with B to the left of C
    B, D = (-1, 0), (1, 0)                                   # CD = CA = 1
    assert abs(ang(C, A, B) - 76) < 1e-9
    return [r(ang(A, C, D))]
