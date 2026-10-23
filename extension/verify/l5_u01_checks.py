"""Independent checks for Level 5 Unit 1 (Million puzzles). Each answer is recomputed by simulation or brute force from the question text."""
import itertools
from common import s

CHECKS = {}


def check(id_):
    def deco(f):
        CHECKS[id_] = f
        return f
    return deco


def digs(n):
    return [int(c) for c in str(n)]


def perms_numbers(cards):
    """Every 7-digit number (no leading zero) made from all the cards once."""
    out = set()
    for p in itertools.permutations(cards):
        if p[0] != 0:
            out.add(int(''.join(map(str, p))))
    return out


def closest(cards, target):
    best = min(perms_numbers(cards), key=lambda v: (abs(v - target), v))
    return best


def rnd(n, place):
    """Round half up to a multiple of `place`."""
    return (n + place // 2) // place * place


def evaluate(tokens):
    """tokens: list of ints/strings; use Python eval on a rewritten string (× ÷ to * //; all our divisions are exact)."""
    e = ''.join(str(t) for t in tokens).replace('×', '*').replace('÷', '/').replace(' ', '')
    return eval(e)


def one_bracket(nums, ops, target):
    """Every way to put one pair of brackets round consecutive numbers; return the lines whose value is the target (as text)."""
    out = []
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if i == 0 and j == n - 1:
                continue
            toks = []
            for k in range(n):
                if k == i:
                    toks.append('(')
                toks.append(str(nums[k]))
                if k == j:
                    toks.append(')')
                if k < n - 1:
                    toks.append(ops[k])
            e = ' '.join(toks).replace('( ', '(').replace(' )', ')')
            if abs(eval(e.replace('×', '*').replace('÷', '/')) - target) < 1e-9:
                out.append(e)
    return out


@check('L5U01-L01')
def _():
    return s([closest([0, 1, 3, 4, 6, 7, 9], 8000000)])


@check('L5U01-S01')
def _():
    words = 6 * 1000000 + 205 * 1000 + 30
    return {'a': s([words]), 'b': s([7 * 10000]), 'c': s([8604000 // 1000])}


@check('L5U01-S02')
def _():
    return s(sorted([4096213, 940621, 4906213, 4096231]))


@check('L5U01-S03')
def _():
    x = 7849520
    return {'a': s([rnd(x, 1000)]), 'b': s([rnd(x, 100000)]), 'c': s([rnd(x, 1000000)])}


@check('L5U01-S04')
def _():
    nums = perms_numbers([0, 1, 4, 5, 7, 8, 9])
    return {'a': s([max(v for v in nums if v % 5 == 0)]), 'b': s([min(nums)])}


@check('L5U01-S05')
def _():
    n = 6482315 + 2 * 100000 - 5 * 10000
    return s([n])


@check('L5U01-S06')
def _():
    def est(f, a, b, op):
        """round each number to one significant figure, then apply the operation"""
        def r1(x):
            d = len(str(x)) - 1
            return rnd(x, 10 ** d) if d else x
        return {'×': r1(a) * r1(b), '+': r1(a) + r1(b), '÷': r1(a) / r1(b)}[op]

    def verdict(shown, e):
        return 'could be right' if 0.5 * e <= shown <= 2 * e else 'must be wrong'
    return {'a': [verdict(20722, est(0, 3985, 52, '×'))], 'b': [verdict(6912005, est(0, 4012018, 2899987, '+'))],
            'c': [verdict(2395400, est(0, 8120, 295, '×'))], 'd': [verdict(4050, est(0, 6480, 16, '÷'))]}


@check('L5U01-S07')
def _():
    a = one_bracket([9, 2, 3, 1], ['-', '×', '+'], 22)
    b = one_bracket([9, 2, 3, 1], ['-', '×', '+'], 1)
    c = one_bracket([2400000, 300, 100, 2], ['÷', '+', '×'], 12000)
    assert len(a) == 1 and len(b) == 1 and len(c) == 1
    return {'a': [a[0]], 'b': [b[0]], 'c': [c[0]]}


@check('L5U01-S08')
def _():
    boxes = 1250000 // 500
    cartons = boxes // 24
    return s([cartons])


@check('L5U01-S09')
def _():
    fits = [v for v in range(8000, 9400) if rnd(v, 100) == 8700]
    return {'a': s([min(fits)]), 'b': s([max(fits)])}


@check('L5U01-S10')
def _():
    a = 5400000 == 54 * 100000
    b = 1000000 - 1 == 99999
    c = max(range(100000, 1000000)) == min(range(1000000, 10000000)) - 1
    t = lambda x: 'True' if x else 'False'
    return {'a': [t(a)], 'b': [t(b)], 'c': [t(c)]}


@check('L5U01-S11')
def _():
    towns = {'Alder': 1204500, 'Birch': 1240500, 'Cedar': 1024500, 'Dune': 1420050}
    return {'a': [max(towns, key=towns.get)], 'b': s([max(towns.values()) - min(towns.values())])}


@check('L5U01-S12')
def _():
    sol = []
    for v in range(100000, 1000000):
        d = digs(v)
        if len(set(d)) != 6 or rnd(v, 10000) != 470000 or d[2] != 2 or d[3] != 2 * d[4] or d[5] != 0:
            continue
        sol.append(v)
    assert len(sol) == 1
    return s(sol)


@check('L5U01-S13')
def _():
    mon = 3100
    tue = mon * 2
    wed = tue - 1250
    return s([mon + tue + wed])


@check('L5U01-S14')
def _():
    c = [v for v in (4499999, 4500000, 5499999, 5500000) if rnd(v, 1000000) == 5000000]
    return s(c)


@check('L5U01-T01')
def _():
    sol = []
    for v in range(6350000, 6450000):
        d = digs(v)
        if len(set(d)) == 7 and rnd(v, 100000) == 6400000 and d[2] == d[1] - 1 and d[4] == d[3] + 2 and d[5] == 0 and sum(d) == 33:
            sol.append(v)
    assert len(sol) == 1
    return s(sol)


@check('L5U01-T02')
def _():
    near = [v for v in range(100000, 300000) if rnd(v, 10000) == 200000]
    assert min(near) == 195000 and max(near) == 204999
    return {'a': s([len([v for v in near if sum(digs(v)) == 4])])}


@check('L5U01-T03')
def _():
    best = 0
    for p in itertools.permutations([2, 3, 5, 7, 9]):
        a = int(''.join(map(str, p[:3])))
        b = int(''.join(map(str, p[3:])))
        best = max(best, a * b)
    return s([best])


@check('L5U01-G01')
def _():
    count = 0
    for p in itertools.permutations(range(10), 7):
        if p[0] != 0:
            count += 1
    return s([count])


@check('L5U01-G02')
def _():
    return s([sum(sum(digs(v)) for v in range(1, 1000))])


@check('L5U01-G03')
def _():
    from fractions import Fraction

    def reach(items):
        if len(items) == 1:
            return {items[0]}
        res = set()
        for i in range(len(items)):
            for j in range(i + 1, len(items)):
                rest = [items[k] for k in range(len(items)) if k not in (i, j)]
                a, b = items[i], items[j]
                cands = {a + b, a * b, a - b, b - a}
                if b:
                    cands.add(a / b)
                if a:
                    cands.add(b / a)
                for c in cands:
                    res |= reach(rest + [c])
        return res
    vals = reach([Fraction(x) for x in (3, 4, 7, 9)])
    best = min(vals, key=lambda v: (abs(v - 100), v))
    return s([int(best)])


@check('L5U01-G04')
def _():
    per_day = 2400 * 8
    days, total = 0, 0
    while total < 1000000:
        days += 1
        total += per_day
    return s([days])


@check('L5U01-C01')
def _():
    n = 5280436
    d = digs(n)
    return {'a': s([d[1] * 100000]), 'b': s([rnd(n, 100000)])}


@check('L5U01-C02')
def _():
    return s([closest([0, 2, 3, 5, 6, 7, 9], 4000000)])


@check('L5U01-C03')
def _():
    r = one_bracket([8, 12, 4, 2], ['+', '÷', '×'], 10)
    assert len(r) == 1
    return [r[0]]


@check('L5U01-C04')
def _():
    return s([18 * 1250 * 12])
