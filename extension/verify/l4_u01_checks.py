"""Independent checks for Level 4 Unit 1 (factors and multiples): everything is recomputed by brute force from the question numbers."""
from math import gcd
CHECKS = {}


def check(id_):
    def deco(f):
        CHECKS[id_] = f
        return f
    return deco


def factors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def mult(n, k):
    return [n * i for i in range(1, k + 1)]


def s(xs):
    return [str(x) for x in xs]


def tf(b):
    return ['True' if b else 'False']


@check('L4U01-L01')
def _():
    return s(factors(45))


@check('L4U01-S01')
def _():
    f = factors(56)
    pairs = [(d, 56 // d) for d in f if d <= 56 // d]
    assert pairs[:4] == [(1, 56), (2, 28), (4, 14), (7, 8)]
    return {'a': s([p[1] for p in pairs[1:]]), 'b': s([len(f)])}


@check('L4U01-S02')
def _():
    return s(factors(66))


@check('L4U01-S03')
def _():
    return s([d for d in factors(32) if 1 < d < 32])


@check('L4U01-S04')
def _():
    return {'a': tf(91 % 7 == 0), 'b': tf(54 in mult(8, 20)), 'c': tf(108 % 9 == 0), 'd': tf(65 in mult(13, 10))}


@check('L4U01-S05')
def _():
    a, b = mult(9, 6), mult(12, 6)
    n = next(x for x in range(1, 1000) if x % 9 == 0 and x % 12 == 0)
    return {'a': s(a), 'b': s(b), 'c': s([n])}


@check('L4U01-S06')
def _():
    a, b = factors(28), factors(42)
    c = [x for x in a if x in b]
    return {'a': s(a), 'b': s(b), 'c': s(c), 'd': s([max(c)])}


@check('L4U01-S07')
def _():
    bags = max(k for k in range(1, 31) if 30 % k == 0 and 45 % k == 0)
    return {'a': s([bags]), 'b': s([30 // bags, 45 // bags])}


@check('L4U01-S08')
def _():
    t = next(d for d in range(1, 200) if d % 10 == 0 and d % 15 == 0)
    return {'a': s([t]), 'b': s([sum(1 for d in range(1, 101) if d % t == 0)])}



@check('L4U01-S09')
def _():
    c = [n for n in range(51, 100) if n % 6 == 0 and n % 7 == 0]
    assert len(c) == 1
    return s(c)


@check('L4U01-S10')
def _():
    nums = [8, 14, 18, 27, 32, 49]
    counts = [len(factors(n)) for n in nums]
    three = [n for n in nums if len(factors(n)) == 3]
    assert len(three) == 1
    return {'a': s(counts), 'b': s(three)}


@check('L4U01-S11')
def _():
    n = next(x for x in range(1, 500) if x % 6 == 0 and x % 8 == 0)
    return {'a': s([n]), 'b': s([n // 6]), 'c': s([n // 8])}


@check('L4U01-S12')
def _():
    return s([n for n in range(11, 30) if 60 % n == 0 and n % 5 == 0])


@check('L4U01-S13')
def _():
    return {'a': s([len(factors(64))]), 'b': s([len(factors(81))]), 'c': s([n for n in (72, 49) if len(factors(n)) % 2 == 1])}


@check('L4U01-T01')
def _():
    c = [n for n in range(10, 100) if n % 3 == 0 and n % 8 == 0 and n // 10 > n % 10 and n // 10 + n % 10 == 9]
    assert len(c) == 1
    return s(c)


@check('L4U01-T02')
def _():
    c = [n for n in range(51, 100) if n % 4 == 3 and n % 5 == 3 and n % 6 == 3]
    assert len(c) == 1
    return s(c)


@check('L4U01-T03')
def _():
    t = next(n for n in range(1, 1000) if n % 12 == 0 and n % 18 == 0)
    return {'a': s([t]), 'b': s([t // 12, t // 18])}


@check('L4U01-G01')
def _():
    n = next(n for n in range(1, 1000) if len(factors(n)) == 10)
    return s([n])


@check('L4U01-G02')
def _():
    t = next(n for n in range(1, 10000) if n % 6 == 0 and n % 8 == 0 and n % 9 == 0)
    times = [m for m in range(1, 601) if m % t == 0]
    return {'a': s([t]), 'b': s([len(times)])}


@check('L4U01-G03')
def _():
    can = {4 * a + 7 * b for a in range(0, 60) for b in range(0, 60)}
    cannot = [n for n in range(1, 200) if n not in can]
    return s([max(cannot)])


@check('L4U01-G04')
def _():
    c = [(l, w) for w in range(1, 85) for l in range(w, 85) if l * w == 84 and 2 * (l + w) == 38]
    assert len(c) == 1
    return s(c[0])


@check('L4U01-C01')
def _():
    return s(factors(52))


@check('L4U01-C02')
def _():
    return s([next(n for n in range(1, 200) if n % 6 == 0 and n % 9 == 0)])


@check('L4U01-C03')
def _():
    return s([max(k for k in range(1, 41) if 40 % k == 0 and 64 % k == 0)])


@check('L4U01-C04')
def _():
    c = [n for n in range(1, 85) if n % 7 == 0 and 84 % n == 0 and sum(int(d) for d in str(n)) == 5]
    assert len(c) == 1
    return s(c)
