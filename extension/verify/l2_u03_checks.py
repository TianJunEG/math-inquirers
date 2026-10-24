"""Independent checks for Level 2 Unit 3 (arrays, equal groups, legs and wheels): counting, enumeration and brute force."""
import itertools
from common import s

CHECKS = {}


def check(i):
    def d(f):
        CHECKS['L2U03-' + i] = f
        return f
    return d


def mix(total_items, legs_total, a_legs, b_legs):
    """All (a, b) counts with a + b = total_items and a*a_legs + b*b_legs = legs_total."""
    return [(a, total_items - a) for a in range(total_items + 1) if a * a_legs + (total_items - a) * b_legs == legs_total]


def groups_ways(n, lo_rows=2, lo_cols=2):
    return [(r, n // r) for r in range(lo_rows, n + 1) if n % r == 0 and n // r >= lo_cols]


@check('L01')
def _():
    sol = mix(3, 10, 2, 4)
    assert len(sol) == 1
    return s([sol[0][1]])


@check('S01')
def _():
    r, c = 3, 7
    n = r * c
    cells = [(i, j) for i in range(r) for j in range(c)]
    assert len(cells) == n
    return {'a': s([r, c, n, c, r, n]), 'b': s([n, r, n // r, n, c, n // c])}


@check('S02')
def _():
    R, C = 4, 8
    covered = {(i, j) for i in range(2, 4) for j in range(4, 8)}
    visible = R * C - len(covered)
    row_len = sum(1 for j in range(C) if (0, j) not in covered)       # the top row is not covered
    return {'a': s([row_len]), 'b': s([R * row_len]), 'c': s([R * row_len - visible])}


@check('S03')
def _():
    plates, per = 4, 5
    T = lambda b: 'True' if b else 'False'
    return {'a': [T(plates == 4 and per == 5)], 'b': [T(5 + 5 + 5 == plates * per)], 'c': [T(4 * 5 == plates * per and plates == 4)], 'd': [T(plates == 5 and per == 4)]}


@check('S04')
def _():
    dog, duck = 3, 2
    return {'a': s([dog * 4]), 'b': s([duck * 2]), 'c': s([dog * 4 + duck * 2])}


@check('S05')
def _():
    legs = [d * 2 + (8 - d) * 4 for d in (8, 7, 6, 5, 4, 3)]
    assert legs[:2] == [16, 18]
    sol = mix(8, 26, 2, 4)
    assert len(sol) == 1
    return {'a': s(legs[2:]), 'b': s(sol[0])}


@check('S06')
def _():
    return {'a': s([6 * 4]), 'b': s([x for x in range(1, 31) if x * 5 == 30]), 'c': s([x for x in range(1, 46) if x * 5 == 45]), 'd': s([sum([4] * 6)])}


@check('S07')
def _():
    full = max(k for k in range(0, 38) if 5 * k <= 37)
    left = 37 - 5 * full
    return {'a': s([full]), 'b': s([left]), 'c': s([5 - left])}


@check('S08')
def _():
    buses = min(k for k in range(1, 20) if 10 * k >= 47)
    return {'a': s([buses]), 'b': s([10 * buses - 47])}


@check('S09')
def _():
    row = []
    for r in range(2, 10):
        row.append(str(18 // r) if 18 % r == 0 and 18 // r >= 2 else 'no')
    return {'a': row, 'b': s([len(groups_ways(18))])}


@check('S10')
def _():
    out = {}
    for lab, n, k in (('a', 3, 3), ('b', 4, 4), ('c', 10, 10)):
        pass
    left = lambda n, k: (24 // k, 24 - (24 // k) * k)
    return {'a': s([left(24, 3)[0]]), 'b': s([left(24, 4)[0]]), 'c': s(list(left(24, 10))), 'd': s([24 // (1 + 3)])}


@check('T01')
def _():
    ways = [(b, t) for t in range(1, 8) for b in range(1, 11) if 2 * b + 3 * t == 21]
    return {'a': s([len(ways)]), 'b': s([min(b + t for b, t in ways)])}


@check('T02')
def _():
    possible = {h * 2 + (6 - h) * 4 for h in range(0, 7)}
    Y = lambda n: 'Yes' if n in possible else 'No'
    return {'a': [Y(18)], 'b': [Y(25)], 'c': [Y(26)], 'd': [Y(12)]}


@check('T03')
def _():
    ok = [n for n in range(31, 50) if n % 3 == 0 and n % 4 == 1 and n % 5 == 3]
    assert len(ok) == 1
    return s(ok)


@check('G01')
def _():
    return {'a': s([6 * 6]), 'b': s([6 * 8]), 'c': s([x for x in range(1, 20) if 6 * x == 54]), 'd': s([6 * 7])}


@check('G02')
def _():
    sol = [(a, 9 - a) for a in range(10) if 3 * a + 5 * (9 - a) == 35]
    assert len(sol) == 1
    possible40 = any(3 * a + 5 * (9 - a) == 40 for a in range(10))
    return {'a': s(sol[0]), 'b': ['Yes' if possible40 else 'No']}


@check('G03')
def _():
    sol = mix(6, 21, 3, 4)
    assert sol == [(3, 3)]
    return ['open']


@check('G04')
def _():
    return s([len(groups_ways(24))])


@check('C01')
def _():
    return s([3 * 8])


@check('C02')
def _():
    return s([5 * 4 + 4 * 2])


@check('C03')
def _():
    return s([47 // 10, 47 % 10])


@check('C04')
def _():
    sol = mix(9, 24, 2, 4)
    assert len(sol) == 1
    return s([sol[0][1]])
