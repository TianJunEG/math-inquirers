"""Independent checks for Level 3 Unit 3 (Times table treasure): products are built by repeated addition of the number, tables are
listed term by term, riddles and grids are solved by search; nothing is copied from the book."""
import itertools
from common import s

CHECKS = {}


def check(id_):
    def deco(f):
        CHECKS[id_] = f
        return f
    return deco


def times(a, b):
    """a groups of b by repeated addition."""
    t = 0
    for _ in range(a):
        t += b
    return t


def table(n, upto=10):
    return [times(k, n) for k in range(1, upto + 1)]


def only(xs):
    assert len(xs) == 1, xs
    return xs[0]


@check('L3U03-L01')
def _():
    return s([times(3, 8) + times(3, 8)])


@check('L3U03-S01')
def _():
    t = table(8)
    return s([t[3], t[5], t[8]])    # 8 x 4, 8 x 6, 8 x 9 (the empty cells in the figure)


@check('L3U03-S02')
def _():
    return {'a': s([times(6, 8)]), 'b': s([times(7, 9)]), 'c': s([times(9, 6)]), 'd': s([times(8, 7)])}


@check('L3U03-S03')
def _():
    base = times(5, 8)
    assert base == 40
    return {'a': s([base + 8]), 'b': s([base - 8]), 'c': s([base + base]), 'd': s([times(10, 8) - 8])}


@check('L3U03-S04')
def _():
    eggs = times(9, 7)
    boxes = len([k for k in range(1, 60) if times(k, 7) <= 56 and times(k, 7) % 7 == 0])
    return {'a': s([eggs]), 'b': s([boxes])}


@check('L3U03-S06')
def _():
    top = times(5, 9)
    bottom = times(2, 9)
    return {'a': s([top]), 'b': s([bottom]), 'c': s([top + bottom])}


@check('L3U03-S09')
def _():
    last = lambda a, b: times(a, b) % 10
    return {'a': s([last(6, 13)]), 'b': s([last(8, 27)]), 'c': s([last(9, 45)]), 'd': s([last(7, 68)])}


@check('L3U03-S07')
def _():
    return {'': s([times(6, 8), times(7, 6), times(7, 9), times(8, 7)])}


@check('L3U03-S08')
def _():
    sols = []
    for r1, r2, c1, c2 in itertools.product(range(1, 13), repeat=4):
        if (r1 * c1, r1 * c2, r2 * c1, r2 * c2) == (54, 63, 48, 56):
            sols.append((c1, c2, r1, r2))
    return s(only(sols))


@check('L3U03-S10')
def _():
    ways = [(r, 30 // r) for r in range(2, 16) if 30 % r == 0 and 30 // r >= 2]
    return {'': s([len(ways)])}


@check('L3U03-S05')
def _():
    c = [n for n in range(51, 80) if n % 7 == 0 and sum(map(int, str(n))) == 9]
    return s([only(c)])


@check('L3U03-S11')
def _():
    six = set(table(6, 20))
    return s([n for n in (24, 38, 42, 56, 60) if n in six])


@check('L3U03-S12')
def _():
    mei, ben = times(6, 8), times(7, 7)
    return {'a': ['Mei' if mei > ben else 'Ben'], 'b': s([abs(mei - ben)])}


@check('L3U03-T01')
def _():
    return s([sum(1 for k in range(1, 31) if times(k, 7) % 10 == 4)])


@check('L3U03-T02')
def _():
    sols = []
    for R in itertools.product(range(6, 10), repeat=3):
        for C in itertools.product(range(6, 10), repeat=3):
            g = [[R[i] * C[j] for j in range(3)] for i in range(3)]
            if g[0][0] == 42 and g[0][1] == 48 and g[1][0] == 49 and g[1][2] == 63 and g[2][2] == 72:
                sols.append((g[0][2], g[1][1], g[2][0], g[2][1]))
    return dict(zip('abcd', s(only(sols))))


@check('L3U03-T03')
def _():
    pairs = [(a, b) for a in range(1, 64) for b in range(a, 64) if times(a, b) == 63 and a + b == 16]
    return s(only(pairs))


@check('L3U03-G01')
def _():
    def root(n):
        while n > 9:
            n = sum(map(int, str(n)))
        return n
    return s([n for n in (738, 825, 963, 1089) if n % 9 == 0 and root(n) == 9])


@check('L3U03-G02')
def _():
    seats = [7 + 2 * k for k in range(8)]
    return {'a': s([seats[-1]]), 'b': s([sum(seats)])}


@check('L3U03-G03')
def _():
    rows, cols = (6, 7), (7, 8)
    shown = {(0, 0): 42, (0, 1): 48, (1, 0): 49}
    sols = []
    for r1, r2, c1, c2 in itertools.product(range(6, 10), repeat=4):
        g = {(0, 0): r1 * c1, (0, 1): r1 * c2, (1, 0): r2 * c1, (1, 1): r2 * c2}
        if all(g[k] == v for k, v in shown.items()):
            sols.append(g[(1, 1)])
    return s([only(sols)])


@check('L3U03-G04')
def _():
    ends6 = [d for d in range(10) if times(8, d) % 10 == 6]
    ends5 = [d for d in range(10) if times(8, d) % 10 == 5]
    return {'a': s(ends6), 'b': ['none' if not ends5 else str(ends5)]}


@check('L3U03-C01')
def _():
    return s([times(7, 8)])


@check('L3U03-C02')
def _():
    return s([times(5, 7) + 7])


@check('L3U03-C03')
def _():
    return s([times(7, 6) % 10])


@check('L3U03-C04')
def _():
    return s([only([k for k in range(1, 60) if times(k, 6) == 54])])
