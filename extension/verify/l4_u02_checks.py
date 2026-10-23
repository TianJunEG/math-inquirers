"""Independent checks for Level 4 Unit 2 (numbers to 100 000): rounding is done by a half-up function; bounds are found by scanning every whole number."""
from itertools import permutations
CHECKS = {}


def check(id_):
    def deco(f):
        CHECKS[id_] = f
        return f
    return deco


def s(xs):
    return [str(x) for x in xs]


def rnd(n, p):
    """Round n to the nearest p, halves up."""
    lo = (n // p) * p
    return lo + p if n - lo >= p / 2 else lo


def having(p, target, lo=0, hi=100000):
    return [n for n in range(lo, hi) if rnd(n, p) == target]


def perms(cards, first_nonzero=True):
    out = set()
    for q in permutations(cards):
        if first_nonzero and q[0] == 0:
            continue
        out.add(int(''.join(map(str, q))))
    return sorted(out)


@check('L4U02-L01')
def _():
    return s([rnd(52718, 100)])


@check('L4U02-S01')
def _():
    out = []
    for n in (38746, 70049, 9996):
        out += [rnd(n, 10), rnd(n, 100), rnd(n, 1000)]
    return s(out)


@check('L4U02-S02')
def _():
    def val(n, d):
        digits = str(n)
        i = digits.index(str(d))
        return int(d) * 10 ** (len(digits) - 1 - i)
    return {'a': s([val(46281, 6)]), 'b': s([val(60912, 6)]), 'c': s([val(83062, 6)])}


@check('L4U02-S03')
def _():
    return {'a': s([42 * 1000 + 7]), 'b': s([9 * 10000 + 4 * 100 + 3])}


@check('L4U02-S04')
def _():
    return s(sorted([58304, 58340, 58034, 58430], reverse=True))


@check('L4U02-S05')
def _():
    step = 100
    a = 24000 + 3 * step
    b = 24500 + 3 * step
    return {'a': s([a]), 'b': s([b]), 'c': s([rnd(b, 1000)])}


@check('L4U02-S06')
def _():
    return {'a': s([rnd(36482, 1000)]), 'b': s([rnd(36482, 100)])}


@check('L4U02-S07')
def _():
    r = having(1000, 12000)
    return {'a': s([min(r)]), 'b': s([max(r)])}


@check('L4U02-S08')
def _():
    r = having(100, 4700)
    return {'a': s([min(r)]), 'b': s([max(r)]), 'c': s([len(r)])}


@check('L4U02-S09')
def _():
    est = 5 * rnd(4018, 1000)
    ex = sum(4018 for _ in range(5))
    return {'a': s([est]), 'b': s([ex]), 'c': ['more' if ex > est else 'less']}


@check('L4U02-S10')
def _():
    c = [n for n in having(1000, 52000, 10000) if (n // 100) % 10 == 7 and (n // 10) % 10 == 5 and n % 10 == 2]
    assert len(c) == 1
    return s(c)


@check('L4U02-S11')
def _():
    p = perms([2, 4, 0, 7, 9])
    return {'a': s([max(p)]), 'b': s([min(p)]), 'c': s([max(n for n in p if n % 2 == 1)])}


@check('L4U02-S12')
def _():
    def ap(a, d, k, n):
        return [a + d * i for i in range(k, k + n)]
    return {'a': s(ap(31600, 1000, 3, 2)), 'b': s(ap(70400, -1500, 3, 2)), 'c': s(ap(4997, 3, 4, 2))}


@check('L4U02-S13')
def _():
    sg = lambda x, y: ['>' if x > y else '<']
    return {'a': sg(45009, 45090), 'b': sg(8999, 10000), 'c': sg(62100, 62010), 'd': sg(3 * 10000 + 7 * 100, 30070)}


@check('L4U02-T01')
def _():
    p = perms([1, 3, 4, 6, 8])
    best = min(p, key=lambda n: abs(n - 40000))
    assert sorted(abs(n - 40000) for n in p)[0] != sorted(abs(n - 40000) for n in p)[1]
    return s([best])


@check('L4U02-T02')
def _():
    a, b = having(1000, 41000), having(1000, 28000)
    return {'a': s([min(a) + min(b)]), 'b': s([max(a) + max(b)])}


@check('L4U02-T03')
def _():
    c = [n for n in range(10000, 100000) if rnd(n, 10000) == 70000 and len(set(str(n))) == 5]
    return {'a': s([max(c)]), 'b': s([min(c)])}


def steps(n):
    return rnd(rnd(rnd(n, 10), 100), 1000)


@check('L4U02-G01')
def _():
    first = next(n for n in range(1000, 10000) if steps(n) != rnd(n, 1000))
    return {'a': s([steps(36449)]), 'b': s([rnd(36449, 1000)]), 'c': s([first])}


@check('L4U02-G02')
def _():
    return s([sum(1 for n in range(1, 1001) if '7' in str(n))])


@check('L4U02-G03')
def _():
    seq = []
    for k in range(5):
        seq += [12000 - 1000 * k, 3 * (k + 1)]
    return {'a': s([seq[8]]), 'b': s([seq[9]])}


@check('L4U02-G04')
def _():
    a = set(having(1000, 7000))
    b = set(having(100, 7000))
    wrong = [n for n in a if n not in b]
    return {'a': ['No' if wrong else 'Yes'], 'b': s([len(a & b)])}


@check('L4U02-C01')
def _():
    return {'a': s([rnd(25962, 10)]), 'b': s([rnd(25962, 100)]), 'c': s([rnd(25962, 1000)])}


@check('L4U02-C02')
def _():
    r = having(100, 8300)
    return {'a': s([min(r)]), 'b': s([max(r)])}


@check('L4U02-C03')
def _():
    return s([min(n for n in perms([4, 0, 7, 1, 8]) if n % 2 == 1)])


@check('L4U02-C04')
def _():
    seq = [53200 - 1500 * i for i in range(5)]
    return s(seq[3:5])
