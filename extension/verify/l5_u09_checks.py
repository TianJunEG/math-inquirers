"""Independent checks for Level 5 Unit 9 (Pattern generalisers).  Growing patterns are BUILT figure by figure from the picture rules in the question and
COUNTED (sticks, tiles, chairs); far figures and 'which figure' questions are answered by building or searching, never with the rule printed in the book.
'Two kinds' puzzles are solved by checking every possible split."""
import itertools
import math
from fractions import Fraction as Fr

CHECKS = {}


def check(id_):
    def deco(f):
        CHECKS[id_] = f
        return f
    return deco


def hexagon_sticks(n):
    """Matchstick hexagons in a row; neighbours share a side. Count distinct unit segments."""
    edges = set()
    for k in range(n):
        cx = k * math.sqrt(3)
        v = [(round(cx + math.cos(math.radians(30 + 60 * j)), 6), round(math.sin(math.radians(30 + 60 * j)), 6)) for j in range(6)]
        for j in range(6):
            a, b = v[j], v[(j + 1) % 6]
            edges.add(frozenset([a, b]))
    return len(edges)


def plus_tiles(n):
    """Middle tile plus 4 arms of n tiles."""
    cells = {(0, 0)}
    for k in range(1, n + 1):
        cells |= {(k, 0), (-k, 0), (0, k), (0, -k)}
    return len(cells)


def chairs_for_tables(n):
    """n tables, each 2 wide; 2 chairs on each long side of each table, one chair at each end of the row."""
    chairs = set()
    for k in range(n):
        for dx in (0.5, 1.5):
            chairs.add((2 * k + dx, 1))
            chairs.add((2 * k + dx, -1))
    chairs.add((-1, 0))
    chairs.add((2 * n + 1, 0))
    return len(chairs)


def frame_tiles(n):
    m = n + 2
    return sum(1 for c in range(m) for r in range(m) if c in (0, m - 1) or r in (0, m - 1))


def stair_tiles(n):
    return sum(1 for r in range(n) for c in range(n - r))


def first_figure(f, target, limit=2000):
    return next((n for n in range(1, limit) if f(n) == target), None)


@check('L5U09-L01')
def _():
    return [str(hexagon_sticks(12))]


@check('L5U09-S01')
def _():
    return {'a': [str(hexagon_sticks(4))], 'b': [str(hexagon_sticks(5))], 'c': [str(hexagon_sticks(6) - hexagon_sticks(5))]}


@check('L5U09-S02')
def _():
    # find (m, c) with sticks = m * n + c for all n from 1 to 30, by testing every pair
    sol = [(m, c) for m in range(0, 10) for c in range(0, 10) if all(hexagon_sticks(n) == m * n + c for n in range(1, 31))]
    assert len(sol) == 1
    return {'a': [str(sol[0][0]), str(sol[0][1])], 'b': [str(hexagon_sticks(20))]}


@check('L5U09-S03')
def _():
    best = max(n for n in range(1, 200) if hexagon_sticks(n) <= 100)
    return {'a': [str(first_figure(hexagon_sticks, 96))], 'b': [str(best), str(100 - hexagon_sticks(best))]}


@check('L5U09-S04')
def _():
    sol = [(m, c) for m in range(0, 10) for c in range(0, 10) if all(plus_tiles(n) == m * n + c for n in range(1, 30))]
    assert len(sol) == 1
    return {'a': [str(plus_tiles(4))], 'b': [str(plus_tiles(15))], 'c': [str(sol[0][0]), str(sol[0][1])], 'd': [str(first_figure(plus_tiles, 81))]}


@check('L5U09-S05')
def _():
    seq = [7]
    while len(seq) < 60:
        seq.append(seq[-1] + 5)
    return {'a': [str(seq[4]), str(seq[5])], 'b': [str(seq[9])], 'c': ['Yes' if 100 in seq else 'No']}


@check('L5U09-S08')
def _():
    sol = [(m, c) for m in range(0, 10) for c in range(0, 10) if all(chairs_for_tables(n) == m * n + c for n in range(1, 30))]
    assert len(sol) == 1
    return {'a': [str(chairs_for_tables(5))], 'b': [str(sol[0][0]), str(sol[0][1])], 'c': [str(first_figure(chairs_for_tables, 50))]}


@check('L5U09-S09')
def _():
    sols = [(a, 15 - a) for a in range(0, 16) if 9 * a + 5 * (15 - a) == 107]
    assert len(sols) == 1
    return {'a': [str(sols[0][0])], 'b': [str(sols[0][1])]}


@check('L5U09-S06')
def _():
    sols = [(c, 17 - c) for c in range(0, 18) if 4 * c + 3 * (17 - c) == 61]
    assert len(sols) == 1
    return {'a': [str(sols[0][0])], 'b': [str(sols[0][1])]}


@check('L5U09-S07')
def _():
    sols = [(right, 12 - right) for right in range(0, 13) if 5 * right - 2 * (12 - right) == 39]
    assert len(sols) == 1
    return {'a': [str(sols[0][1])], 'b': [str(sols[0][0])]}


@check('L5U09-S10')
def _():
    table = {1: 7, 2: 10, 3: 13, 4: 16}
    sol = [(m, c) for m in range(0, 20) for c in range(0, 20) if all(m * k + c == v for k, v in table.items())]
    assert len(sol) == 1
    m, c = sol[0]
    return {'a': [str(m), str(c)], 'b': [str(m * 12 + c)], 'c': [str(next(n for n in range(1, 1000) if m * n + c == 100))]}


@check('L5U09-S11')
def _():
    t = lambda v: 'True' if v else 'False'
    seq = [5 + 4 * k for k in range(100)]
    a = 101 in seq
    b = hexagon_sticks(20) == 102
    ends = {hexagon_sticks(n) % 10 for n in range(1, 200)}
    seq2 = {6 + 5 * k for k in range(200)}
    c = all(x % 10 != 3 for x in seq2)
    return {'a': [t(a)], 'b': [t(b)], 'c': [t(c)]}


@check('L5U09-T01')
def _():
    sols = [k for k in range(0, 25) if 50 * k + 20 * (24 - k) == 960]
    assert len(sols) == 1
    return [str(sols[0])]


@check('L5U09-T02')
def _():
    return {'a': [str(stair_tiles(10))], 'b': [str(first_figure(stair_tiles, 105))]}


@check('L5U09-T03')
def _():
    odds = [k for k in range(1, 50, 2)]
    total, layers = 0, []
    for k in odds:
        total += k
    # the same total from the L-shaped layers: the n-th square has n*n tiles
    n = len(odds)
    assert total == sum(1 for c in range(n) for r in range(n))
    return [str(total)]


@check('L5U09-G01')
def _():
    terms = list(range(4, 101, 3))
    assert terms[-1] == 100
    return [str(sum(terms))]


@check('L5U09-G02')
def _():
    def shakes(n):
        return sum(1 for a, b in itertools.combinations(range(n), 2))
    return {'a': [str(shakes(5))], 'b': [str(shakes(12))]}


@check('L5U09-G03')
def _():
    answered = 30 - 3
    sols = [right for right in range(0, answered + 1) if 4 * right - (answered - right) == 73]
    assert len(sols) == 1
    return [str(sols[0])]


@check('L5U09-C01')
def _():
    seq = [6]
    while len(seq) < 15:
        seq.append(seq[-1] + 5)
    return [str(seq[14])]


@check('L5U09-C02')
def _():
    return [str(next(n for n in range(1, 500) if 3 * n + 2 == 41))]


@check('L5U09-C03')
def _():
    sols = [c for c in range(0, 21) if 4 * c + 3 * (20 - c) == 70]
    assert len(sols) == 1
    return [str(sols[0])]


@check('L5U09-C04')
def _():
    return [str(max(n for n in range(1, 500) if hexagon_sticks(n) <= 130))]
