"""Independent checks for Level 4 Unit 5 (decimals): exact Decimal arithmetic; rounding limits are found by scanning every number at the next place."""
from decimal import Decimal as D, ROUND_HALF_UP
from itertools import permutations
CHECKS = {}


def check(id_):
    def deco(f):
        CHECKS[id_] = f
        return f
    return deco


def s(xs):
    return [str(x) for x in xs]


def q(x, dp):
    """Format x with exactly dp decimal places (dp = 0 gives a whole number)."""
    return str(D(x).quantize(D(1).scaleb(-dp), rounding=ROUND_HALF_UP))


def rnd(x, dp):
    return D(x).quantize(D(1).scaleb(-dp), rounding=ROUND_HALF_UP)


def scan(dp_fine, dp_round, target, lo, hi):
    """All numbers with dp_fine decimals in [lo, hi] that round to target at dp_round places."""
    step = D(1).scaleb(-dp_fine)
    out, x = [], D(lo)
    while x <= D(hi):
        if rnd(x, dp_round) == D(target):
            out.append(x)
        x += step
    return out


def tf(a, b):
    a, b = D(a), D(b)
    return ['>' if a > b else '<' if a < b else '=']


@check('L4U05-L01')
def _():
    return [q(rnd('8.46', 1), 1)]


def at(start, step, n):
    return D(start) + D(step) * n


@check('L4U05-S01')
def _():
    return {'a': [q(at(5, '0.1', 3), 1)], 'b': [q(at(5, '0.1', 8), 1)]}


@check('L4U05-S02')
def _():
    c, d = at('0.4', '0.01', 3), at('0.4', '0.01', 8)
    return {'a': [q(c, 2)], 'b': [q(d, 2)], 'c': ['D' if rnd(d, 1) == D('0.5') else 'C']}


@check('L4U05-S03')
def _():
    return {'a': [q(at('3.42', '0.001', 7), 3)]}


@check('L4U05-S04')
def _():
    return {'a': tf('4.06', '4.6'), 'b': tf('0.38', '0.308'), 'c': tf('12.5', '12.50'), 'd': tf('7.09', '7.1')}


@check('L4U05-S05')
def _():
    xs = ['5.205', '5.25', '5.052', '5.5', '5.025']
    return sorted(xs, key=D)


@check('L4U05-S06')
def _():
    def val(num, digit):
        ip, _, fp = num.partition('.')
        if digit in ip:
            return q(D(digit) * D(10) ** (len(ip) - 1 - ip.index(digit)), 0)
        pos = fp.index(digit) + 1
        return str(D(digit) * D(1).scaleb(-pos))
    return {'a': [val('4.562', '6')], 'b': [val('6.043', '6')], 'c': [val('0.936', '6')]}


@check('L4U05-S07')
def _():
    x = '6.847'
    return {'a': [q(rnd(x, 0), 0)], 'b': [q(rnd(x, 1), 1)], 'c': [q(rnd(x, 2), 2)]}


@check('L4U05-S08')
def _():
    cost = D('1.85') + D('2.40')
    return [q(5 - cost, 2)]


@check('L4U05-S09')
def _():
    total = D('8.8')
    k = next(D(c) / 10 for c in range(0, 89) if D(c) / 10 + 3 * (D(c) / 10) == total)
    return {'a': [q(k, 1)], 'b': [q(3 * k, 1)]}


@check('L4U05-S10')
def _():
    book = next(D(c) / 100 for c in range(0, 281) if 4 * D(c) / 100 == D('2.8'))
    case = D('0.35')
    return {'a': [q(book, 1)], 'b': [q(book + case, 2)], 'c': [q(3 * book + case, 2)]}


@check('L4U05-S11')
def _():
    return {'a': [q(D('4.7') + D('2.35'), 2)], 'b': [q(D('9.2') - D('3.64'), 2)], 'c': [q(D('2.5') * 4, 0)], 'd': [q(D('7.2') / 6, 1)]}


@check('L4U05-S12')
def _():
    from fractions import Fraction as Fr

    def dec(fr):
        return str(float(fr))
    return {'a': [dec(Fr(7, 10))], 'b': [dec(Fr(19, 100))], 'c': [dec(Fr(7, 2))], 'd': [dec(Fr(11, 4))]}


@check('L4U05-T01')
def _():
    c = scan(3, 2, '4.27', '4.200', '4.300')
    return {'a': [q(min(c), 3)], 'b': [q(max(c), 3)]}


@check('L4U05-T02')
def _():
    nums = set()
    for p in permutations('1469'):
        for k in range(1, 4):
            nums.add(D(''.join(p[:k]) + '.' + ''.join(p[k:])))
    nums = sorted(nums, key=lambda x: abs(x - 20))
    assert abs(nums[0] - 20) < abs(nums[1] - 20)
    return [str(nums[0])]


@check('L4U05-T03')
def _():
    sol = [(D(c) / 100, D(c) / 100 + D('2.40')) for c in range(0, 1721) if 3 * (D(c) / 100 + D('2.40')) + 2 * (D(c) / 100) == D('17.20')]
    assert len(sol) == 1
    return {'a': [q(sol[0][0], 2)], 'b': [q(sol[0][1], 2)]}


@check('L4U05-G01')
def _():
    sol = [(c, d, r) for c in range(1, 94) for d in range(1, 94) for r in range(1, 94)
           if D(c + d) == D('9.3') * 10 and D(d + r) == D('8.2') * 10 and D(c + r) == D('5.9') * 10]
    assert len(sol) == 1
    return [q(D(sol[0][2]) / 10, 1)]


@check('L4U05-G02')
def _():
    sol = [k for k in range(0, 13) if k * 50 + (12 - k) * 10 == 360]
    assert len(sol) == 1
    return s(sol)


@check('L4U05-G03')
def _():
    sol = [D(c) / 100 for c in range(0, 2041) if sum(D(c) / 100 + D('0.60') * i for i in range(4)) == D('20.40')]
    assert len(sol) == 1
    return {'a': [q(sol[0], 2)], 'b': [q(sol[0] + D('0.60') * 3, 2)]}


@check('L4U05-G04')
def _():
    seq = [D('0.35') + D('0.05') * i for i in range(60)]
    return {'a': [str(seq[19].normalize())], 'b': [str(seq.index(D('2.05')) + 1)]}


@check('L4U05-C01')
def _():
    return sorted(['6.07', '6.7', '6.007', '6.17'], key=D)


@check('L4U05-C02')
def _():
    return [q(rnd('7.846', 0), 0), q(rnd('7.846', 1), 1), q(rnd('7.846', 2), 2)]


@check('L4U05-C03')
def _():
    return [q(10 - 4 * D('1.35'), 2)]


@check('L4U05-C04')
def _():
    c = scan(2, 1, '3.6', '3.00', '4.00')
    return [q(min(c), 2), q(max(c), 2)]
