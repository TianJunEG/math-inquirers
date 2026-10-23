"""Independent checks for Level 2 Unit 6 (money): all amounts are whole cents; ways to pay come from brute-force enumeration of multisets."""
import itertools
from common import s

CHECKS = {}


def check(i):
    def d(f):
        CHECKS['L2U06-' + i] = f
        return f
    return d


def d2(c):
    """cents -> dollars with 2 decimals"""
    return f'{c // 100}.{c % 100:02d}'


def dw(c):
    """cents -> whole dollars (must be whole)"""
    assert c % 100 == 0
    return str(c // 100)


NOTES = (10000, 5000, 1000, 500, 200)
COINS = (100, 50, 20, 10, 5)
ALL = NOTES + COINS


def multisets(values, total):
    """every multiset of pieces (as sorted tuples) from values that sums to total (cents)"""
    out = []

    def rec(i, left, cur):
        if left == 0:
            out.append(tuple(cur))
            return
        if i == len(values):
            return
        v = values[i]
        for k in range(left // v + 1):
            rec(i + 1, left - k * v, cur + [v] * k)
    rec(0, total, [])
    return out


def fewest(total, values):
    """fewest pieces by dynamic programming over every amount up to total (cents)."""
    INF = 10 ** 9
    best = [0] + [INF] * total
    for c in range(1, total + 1):
        for v in values:
            if v <= c and best[c - v] + 1 < best[c]:
                best[c] = best[c - v] + 1
    return best[total], None


@check('L01')
def _():
    return s([fewest(685, ALL)[0]])


@check('S01')
def _():
    return {'a': s([3 * 100 + 45]), 'b': [d2(275)], 'c': [d2(6 * 100 + 5)], 'd': s([1 * 100 + 30])}


@check('S02')
def _():
    pcs = [500, 200, 200, 100, 50, 20, 10]
    return {'a': [d2(sum(pcs))]}


@check('S03')
def _():
    return {'a': s([fewest(285, ALL)[0]]), 'b': s([fewest(740, ALL)[0]]), 'c': s([fewest(2365, ALL)[0]])}


@check('S04')
def _():
    ways = [(a, b, c) for a in range(0, 2) for b in range(0, 4) for c in range(0, 8) if 5 * a + 2 * b + c == 7]
    four = [w for w in ways if sum(w) == 4]
    assert len(four) == 1
    return {'a': s([len(ways)]), 'b': s([four[0][1], four[0][2]])}


@check('S05')
def _():
    return {'a': s([100 - 70]), 'b': [d2(1000 - 430)], 'c': [dw(5000 - 3700)], 'd': s([fewest(1300, NOTES + COINS)[0]])}


@check('S06')
def _():
    p = {'Shoes': 1750, 'T-shirt': 990, 'Hat': 460}
    two = p['Shoes'] + p['T-shirt']
    allc = sum(p.values())
    return {'a': [d2(two)], 'b': ['Yes' if allc <= 3000 else 'No'], 'c': [d2(max(0, allc - 3000))]}


@check('S07')
def _():
    start = [c for c in range(0, 5000) if c - 350 - 125 == 475][0]
    return [d2(start)]


@check('S08')
def _():
    per4 = 100          # 4 pencils cost $1
    per5 = 200          # 5 stickers cost $2
    return {'a': [dw(12 // 4 * per4)], 'b': [dw(20 // 5 * per5)], 'c': s([600 // per5 * 5])}


@check('S09')
def _():
    p = {'Car': 450, 'Ball': 625, 'Top': 800, 'Kite': 375}
    pairs = [c for c in itertools.combinations(p, 2) if sum(p[x] for x in c) == 1250]
    assert len(pairs) == 1
    return list(pairs[0])


@check('S10')
def _():
    sets = [c for c in itertools.combinations_with_replacement((5, 10, 20, 50), 4) if sum(c) == 95]
    assert len(sets) == 1
    return s(sorted(sets[0], reverse=True))


@check('T01')
def _():
    ways = multisets((20, 10, 5), 35)
    five = [w for w in ways if len(w) == 5]
    assert len(five) == 1
    return {'a': s([len(ways)]), 'b': s([five[0].count(10), five[0].count(5)])}


@check('T02')
def _():
    sol = [(l, c) for l in range(0, 8) for c in range(0, 8) if l + c == 7 and 20 * l + 50 * c == 260]
    assert len(sol) == 1
    return {'a': s([sol[0][0]]), 'b': s([sol[0][1]])}


@check('T03')
def _():
    sol = [(p, p + 400) for p in range(0, 1300, 5) if p + p + 400 == 1300]
    assert len(sol) == 1
    return {'a': [d2(sol[0][0])], 'b': [d2(sol[0][1])]}


@check('G01')
def _():
    half = lambda c: c // 2
    assert 960 % 2 == 0 and 1450 % 2 == 0
    return {'a': [d2(half(960))], 'b': [d2(half(1450))], 'c': [d2(580 * 2)]}


@check('G02')
def _():
    totals = sorted({20 * a + 50 * (5 - a) for a in range(6)})
    three50 = [20 * a + 50 * 3 for a in [2]]
    return {'a': s([len(totals)]), 'b': [d2(20 * 2 + 50 * 3)], 'c': ['Yes' if 140 in totals else 'No']}


@check('G03')
def _():
    sets = [c for c in itertools.combinations_with_replacement((5, 10, 20, 50), 3) if sum(c) == 80]
    assert len(sets) == 1 and sorted(sets[0]) == [10, 20, 50]
    return ['open']


@check('G04')
def _():
    a = 12 // 3 * 2
    b = 12 // 4 * 3
    return {'a': [str(a)], 'b': [str(b)], 'c': ['A' if a < b else 'B']}


@check('C01')
def _():
    return s([4 * 100 + 5])


@check('C02')
def _():
    return s([fewest(635, ALL)[0]])


@check('C03')
def _():
    return [d2(1000 - 740)]


@check('C04')
def _():
    start = [c for c in range(0, 5000) if c - 240 - 310 == 450][0]
    return [d2(start)]
