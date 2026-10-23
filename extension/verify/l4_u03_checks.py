"""Independent checks for Level 4 Unit 3 (four operations): word problems are solved by searching for the unknown, expressions are evaluated by Python."""
import itertools
from fractions import Fraction
CHECKS = {}


def check(id_):
    def deco(f):
        CHECKS[id_] = f
        return f
    return deco


def s(xs):
    return [str(x) for x in xs]


def rnd(n, p):
    lo = (n // p) * p
    return lo + p if n - lo >= p / 2 else lo


def ev(expr):
    """Evaluate a printed expression with exact fractions (x and ÷ before + and -, left to right)."""
    import re
    e = expr.replace('×', '*').replace('÷', '/').replace('−', '-')
    e = re.sub(r'(\d+)', r'Fraction(\1)', e)
    return eval(e)


def unit_total(times, total):
    """Smallest unit u with (1 + times) * u == total, found by search."""
    return next(u for u in range(1, total + 1) if u + times * u == total)


@check('L4U03-L01')
def _():
    return s([unit_total(5, 114)])


@check('L4U03-S01')
def _():
    return {'a': s([3706 * 4]), 'b': s([85 * 47]), 'c': s([next(q for q in range(1, 9999) if 6 * q == 7524)]), 'd': s([next(q for q in range(1, 9999) if 5 * q == 8150)])}


@check('L4U03-S02')
def _():
    return {'a': s([rnd(4986, 1000) * 4]), 'b': s([rnd(9120, 1000) // 3]), 'c': s([rnd(7020, 1000) - rnd(2980, 1000)])}


@check('L4U03-S03')
def _():
    chairs = 0
    for _ in range(28):
        chairs += 36
    return s([chairs - 45])


@check('L4U03-S04')
def _():
    boxes, left = 0, 5468
    while left >= 8:
        left -= 8
        boxes += 1
    return {'a': s([boxes]), 'b': s([left])}


@check('L4U03-S05')
def _():
    return s([unit_total(4, 385)])


@check('L4U03-S06')
def _():
    r = next(r for r in range(1, 47) if r + (r + 9) == 47)
    return {'a': s([r]), 'b': s([r + 9])}


@check('L4U03-S07')
def _():
    c = [n for n in range(1, 1000) if (n * 6 - 9) / 3 == 31]
    assert len(c) == 1
    return s(c)


@check('L4U03-S08')
def _():
    def trick(n):
        return (n * 3 + 12) / 3 - n
    outs = {trick(n) for n in range(1, 200)}
    assert len(outs) == 1
    return {'a': s([int(trick(6))]), 'b': s([int(trick(15))]), 'c': s([int(trick(1))])}


@check('L4U03-S09')
def _():
    return {'a': s([next(x for x in range(1, 9999) if 7 * x == 4249)]), 'b': s([next(x for x in range(1, 9999) if x // 9 == 124 and x % 9 == 0)]),
            'c': s([next(x for x in range(0, 5000) if 5000 - x == 2738)]), 'd': s([next(x for x in range(0, 9999) if x + 1905 == 6400)])}


@check('L4U03-S10')
def _():
    cost = 6 * 3 + 4 * 2
    return s([50 - cost])


@check('L4U03-S11')
def _():
    def chain(a, b, n=5):
        out = [a, b]
        while len(out) < n:
            out.append(out[-1] + out[-2])
        return out
    a = next(b for b in range(1, 60) if chain(4, 9)[3] == 22 or True)
    ca = chain(4, 9)
    assert ca[3] == 22
    first = [x for x in range(1, 30) if chain(x, 6)[2] == 11]
    assert len(first) == 1
    cb = chain(first[0], 6)
    assert cb[4] == 28
    return {'a': s([ca[2], ca[4]]), 'b': s([cb[0], cb[3]])}


@check('L4U03-S12')
def _():
    u = unit_total(3, 480)
    return s([3 * u - u])


@check('L4U03-T01')
def _():
    return {'a': s([ev('60 − 4 × 9 + 12 ÷ 3')]), 'b': s([ev('5 × (13 + 7) − 6')])}


@check('L4U03-T02')
def _():
    import json, os
    ud = json.load(open(os.path.join(os.path.dirname(__file__), '..', 'data', 'l4_u03.json')))
    f = next(i for i in ud['items'] if i['id'] == 'L4U03-T02')['figure']['rows']
    assert f[0]['segs'][0]['t'] == '52' and [x.get('t') for x in f[2]['segs']] == ['5', None, '11']
    found = []
    for m in range(1, 200):
        mid = (5 + m, m + 11)
        if mid[0] + mid[1] == 52:
            found.append(m)
    assert len(found) == 1
    return s(found)


@check('L4U03-T03')
def _():
    c = [(b, b + 30) for b in range(1, 84) if b + (b + 30) == 84]
    assert len(c) == 1
    mv = [m for m in range(0, 60) if c[0][1] - m == c[0][0] + m]
    assert len(mv) == 1
    return {'a': s([c[0][0]]), 'b': s(mv)}


@check('L4U03-G01')
def _():
    sol = []
    for ops in itertools.product('+−×÷', repeat=2):
        if ev(f'9 {ops[0]} 4 {ops[1]} 6') == 30:
            sol.append(ops)
    assert len(sol) == 1
    nums = [7, 3, 8, 4]
    signs = ['+', '×', '−']
    bra = []
    for i in range(3):
        for j in range(i + 1, 4):
            if j - i < 1:
                continue
            parts = []
            for k in range(4):
                if k == i:
                    parts.append('(')
                parts.append(str(nums[k]))
                if k == j:
                    parts.append(')')
                if k < 3:
                    parts.append(signs[k])
            e = ' '.join(parts).replace('( ', '(').replace(' )', ')')
            if ev(e) == 76 and e != ' '.join(map(str, [7, '+', 3, '×', 8, '−', 4])):
                bra.append((i, j))
    assert bra == [(0, 1)], bra
    return {'a': [sol[0][0].replace('−', '−'), sol[0][1]], 'b': s([nums[0], nums[1]])}


@check('L4U03-G02')
def _():
    a, b, wk = 15, 0, 0
    while a != b:
        a += 8
        b += 13
        wk += 1
        assert wk < 100
    return {'a': s([wk]), 'b': s([a])}


@check('L4U03-G03')
def _():
    c = [(a, b) for a in range(10) for b in range(10) if (300 + 10 * a + 4) * 7 == 2000 + 100 * b + 38]
    assert len(c) == 1
    return {'a': s([c[0][0]]), 'b': s([c[0][1]])}


@check('L4U03-C01')
def _():
    return s([4728 * 5, next(q for q in range(1, 9999) if 7 * q == 9135)])


@check('L4U03-C02')
def _():
    return s([15 * 12 - 64])


@check('L4U03-C03')
def _():
    return s([4 * unit_total(4, 275)])


@check('L4U03-C04')
def _():
    c = [n for n in range(1, 500) if (n + 17) * 3 - 20 == 94]
    assert len(c) == 1
    return s(c)
