"""Independent checks for Level 1 Unit 6 (Money): amounts are in cents; every answer comes from brute-force enumeration of coin multisets."""
import itertools
from common import s

CHECKS = {}


def check(id_):
    def deco(f):
        CHECKS[id_] = f
        return f
    return deco


COINS = (5, 10, 20, 50)


def multisets(values, k):
    return [c for c in itertools.combinations_with_replacement(values, k)]


def ways(target, values, k=None, max_k=30):
    """Every multiset of coins (sorted tuples) from `values` that sums to target (with exactly k coins if k is given)."""
    out = []
    for n in ([k] if k else range(1, max_k + 1)):
        out += [c for c in multisets(values, n) if sum(c) == target]
    return out


def fewest(target, values):
    for n in range(1, 40):
        w = [c for c in multisets(values, n) if sum(c) == target]
        if w:
            return n, w
    return None


def key(c):
    return ','.join(str(x) for x in sorted(c, reverse=True))


@check('L1U06-L01')
def _():
    w = ways(80, COINS, 3)
    assert len(w) == 1
    return s(sorted(w[0], reverse=True))


@check('L1U06-S01')
def _():
    return s([sum([50, 10, 10])])


@check('L1U06-S02')
def _():
    return s([sum([10, 5, 2, 2])])


@check('L1U06-S03')
def _():
    n = lambda total, coin: [k for k in range(1, 100) if k * coin == total][0]
    return {'a': s([n(50, 10)]), 'b': s([n(20, 5)]), 'c': s([n(100, 20)]), 'd': s([n(100, 50)])}


@check('L1U06-S04')
def _():
    def two(t):
        w = ways(t, COINS, 2)
        assert len(w) == 1, (t, w)
        return s(sorted(w[0], reverse=True))
    return {'a': two(25), 'b': two(60), 'c': two(30)}


@check('L1U06-S05')
def _():
    ok = [f'{c}¢' for c in (5, 10, 20, 50) if c + c == 40]
    assert len(ok) == 1
    return ok


@check('L1U06-S06')
def _():
    p = {'rubber': 15, 'pencil': 25, 'ruler': 45, 'glue': 30}
    return {'a': s([p['rubber'] + p['pencil']]), 'b': ['ruler' if p['ruler'] > p['glue'] else 'glue'], 'c': s([p['ruler'] - p['rubber']])}


@check('L1U06-S07')
def _():
    return s([c for c in range(0, 51) if 30 + c == 50])


@check('L1U06-S08')
def _():
    toys = {'Kite': 4, 'Top': 7, 'Puzzle': 8, 'Bat': 11}
    pairs = [p for p in itertools.combinations(toys, 2) if sum(toys[x] for x in p) == 12]
    assert len(pairs) == 1
    return list(pairs[0])


@check('L1U06-S09')
def _():
    return s([m for m in range(0, 20) if 8 + m == 13])


@check('L1U06-S10')
def _():
    A, B = sum([20, 20, 5, 5]), sum([50, 5])
    return {'a': ['A' if A > B else 'B'], 'b': s([abs(A - B)])}


@check('L1U06-S11')
def _():
    w = [(a, b) for a in range(0, 5) for b in range(0, 5) if 20 * a + 10 * b == 40]
    return {'a': [f'{a},{b}' for a, b in w], 'b': s([len(w)])}


@check('L1U06-S12')
def _():
    tf = lambda b: 'True' if b else 'False'
    return {'a': [tf(20 + 20 + 10 == 50)], 'b': [tf(3 * 10 == 40)], 'c': [tf(10 * 10 == 100)], 'd': [tf(4 * 5 == 25)]}


@check('L1U06-S13')
def _():
    return {'a': s([fewest(40, COINS)[0]]), 'b': s([fewest(90, COINS)[0]])}


@check('L1U06-S14')
def _():
    row = [50, 20, 20, 10, 5, 5]
    sel = set()
    for r in range(1, len(row) + 1):
        for idx in itertools.combinations(range(len(row)), r):
            if sum(row[i] for i in idx) == 65:
                sel.add(tuple(sorted((row[i] for i in idx), reverse=True)))
    assert len(sel) == 1
    return [f'{c}¢' for c in list(sel)[0]]


@check('L1U06-T01')
def _():
    w = ways(65, COINS, 4)
    return [key(c) for c in w]


@check('L1U06-T02')
def _():
    sols = [(a, 7 - a) for a in range(0, 8) if 5 * a + 10 * (7 - a) == 50]
    assert len(sols) == 1
    return {'a': s([sols[0][0]]), 'b': s([sols[0][1]])}


@check('L1U06-T03')
def _():
    toys = {'Car': 6, 'Top': 7, 'Ball': 8, 'Kite': 9, 'Drum': 12}
    pairs = [p for p in itertools.combinations(toys, 2) if sum(toys[x] for x in p) == 15]
    assert len(pairs) == 2
    partner = lambda name: [b if a == name else a for a, b in pairs if name in (a, b)]
    return {'a': partner('Car'), 'b': partner('Top')}


@check('L1U06-G01')
def _():
    share = lambda total, n: [x for x in range(0, total + 1) if x * n == total][0]
    # can 2 children get equal amounts if the coins are 20c and 10c only: try every multiset of those coins totalling 50 and every split
    possible = False
    for n in range(1, 10):
        for c in multisets((10, 20), n):
            if sum(c) != 50:
                continue
            for r in range(0, n + 1):
                for sub in itertools.combinations(range(n), r):
                    if sum(c[i] for i in sub) * 2 == 50:
                        possible = True
    return {'a': s([share(80, 2)]), 'b': s([share(80, 4)]), 'c': ['Yes' if possible else 'No']}


@check('L1U06-G02')
def _():
    sols = [(spent, bag) for spent in range(0, 51) for bag in range(0, 51) if 50 - spent == 12 and bag + 18 == spent]
    assert len(sols) == 1
    return {'a': s([sols[0][0]]), 'b': s([sols[0][1]])}


@check('L1U06-G03')
def _():
    n, w = fewest(38, (1, 2, 5, 10))
    assert len(w) == 1
    return {'a': s([n]), 'b': s(sorted(w[0], reverse=True))}


@check('L1U06-C01')
def _():
    return s([sum([20, 20, 10, 5, 5])])


@check('L1U06-C02')
def _():
    w = ways(70, COINS, 3)
    assert len(w) == 1
    return s(sorted(w[0], reverse=True))


@check('L1U06-C03')
def _():
    return s([m for m in range(0, 91) if 65 + m == 90])


@check('L1U06-C04')
def _():
    dollar_coin_in_cents = 100   # a $1 coin
    return ['$1' if dollar_coin_in_cents > 85 else '85¢']
