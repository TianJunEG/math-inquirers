"""Independent checks for Level 2 Unit 7 (fractions): exact arithmetic with fractions.Fraction; equal parts are tested from the drawn geometry."""
import itertools
from fractions import Fraction as Fr
from common import s

CHECKS = {}


def check(i):
    def d(f):
        CHECKS['L2U07-' + i] = f
        return f
    return d


def fs(n, d):
    return f'{n}/{d}'


def area(poly):
    return abs(sum(poly[i][0] * poly[(i + 1) % len(poly)][1] - poly[(i + 1) % len(poly)][0] * poly[i][1] for i in range(len(poly)))) / 2


@check('L01')
def _():
    n = 10 - 3
    return [fs(n, 10)]


@check('S01')
def _():
    def equal(sizes):
        return len(set(round(x, 6) for x in sizes)) == 1
    bar_a = [1, 1, 1, 1]
    bar_b = [1, 1, 1, 3]
    circ_c = [90, 90, 90, 90]
    circ_d = [120, 90, 90, 60]
    s_ = 100.0
    c = (s_ / 2, s_ / 2)
    corners = [(0, 0), (s_, 0), (s_, s_), (0, s_)]
    diag = [area([corners[i], corners[(i + 1) % 4], c]) for i in range(4)]
    strips = [1, 1, 1, 3]
    Y = lambda b: 'Yes' if b else 'No'
    return {'a': [Y(equal(bar_a))], 'b': [Y(equal(bar_b))], 'c': [Y(equal(circ_c))], 'd': [Y(equal(circ_d))], 'e': [Y(equal(diag))], 'f': [Y(equal(strips))]}


@check('S02')
def _():
    def nm(parts, shaded):
        return [fs(shaded, parts), fs(parts - shaded, parts)]
    return {'a': nm(5, 2), 'b': nm(8, 6), 'c': nm(12, 5), 'd': s([8 - 5])}


@check('S03')
def _():
    return {'a': s([int(Fr(6, 6))]), 'b': s([9]), 'c': s([x for x in range(0, 9) if Fr(4, 8) + Fr(x, 8) == 1])}


@check('S04')
def _():
    unit = lambda n: Fr(1, n)
    g1 = '1/3' if unit(3) > unit(4) else '1/4'
    g2 = '1/6' if unit(6) < unit(8) else '1/8'
    order = sorted([2, 6, 4, 8], reverse=True)       # greater bottom number = smaller fraction
    assert [unit(n) for n in order] == sorted([unit(n) for n in order])
    return {'a': [g1], 'b': [g2], 'c': [fs(1, n) for n in order]}


@check('S05')
def _():
    big = lambda a, b: a if a > b else b
    return {'a': [fs(big(3, 6), 10)], 'b': [fs(big(7, 5), 12)], 'c': [fs(n, 7) for n in sorted([6, 2, 4])]}


@check('S06')
def _():
    r = lambda f, d: fs(f.numerator * (d // f.denominator), d)
    return {'a': [r(Fr(3, 12) + Fr(6, 12), 12)], 'b': [r(Fr(7, 8) - Fr(2, 8), 8)], 'c': [r(1 - Fr(3, 5), 5)], 'd': [fs(x, 9) for x in range(0, 10) if Fr(4, 9) + Fr(x, 9) == 1]}


@check('S07')
def _():
    siti, ravi = 3, 4
    return {'a': [fs(siti + ravi, 10)], 'b': [fs(10 - siti - ravi, 10)], 'c': ['Siti' if siti > ravi else 'Ravi'], 'd': [fs(abs(ravi - siti), 10)]}


@check('S08')
def _():
    each = Fr(1, 5)
    two = each * 2
    return {'a': [fs(each.numerator, each.denominator)], 'b': [fs(two.numerator, 5)], 'c': [fs((1 - two) * 5, 5)]}


@check('S09')
def _():
    steps = 8
    return {'a': [fs(3, steps)], 'b': [fs(7, steps)]}


@check('T01')
def _():
    ravi, siti = Fr(3, 4), Fr(5, 8)
    diff = abs(ravi - siti)
    return {'a': ['Ravi' if ravi > siti else 'Siti'], 'b': [fs(diff.numerator, diff.denominator)]}


@check('T02')
def _():
    left = 1 - Fr(1, 4)
    ali = left / 2
    left2 = left - ali
    return {'a': [fs(left.numerator, left.denominator)], 'b': [fs(ali.numerator, ali.denominator)], 'c': [fs(left2.numerator, left2.denominator)]}


@check('T03')
def _():
    sol = [(a, b) for a in range(0, 13) for b in range(0, 13) if a + b == 12 and b - a == 6]
    assert len(sol) == 1
    return {'a': [fs(sol[0][0], 12)], 'b': [fs(sol[0][1], 12)]}


@check('G01')
def _():
    f = lambda q, d: [x for x in range(0, d + 1) if Fr(x, d) == q][0]
    return {'a': s([f(Fr(1, 2), 6)]), 'b': s([f(Fr(2, 3), 6)]), 'c': s([f(Fr(3, 4), 8)])}


@check('G02')
def _():
    ways = [(a, b, c) for a in range(1, 10) for b in range(a + 1, 10) for c in range(b + 1, 10) if a + b + c == 9]
    six = [w for w in ways if w[2] == 6]
    assert len(six) == 1
    return {'a': s([len(ways)]), 'b': s(six[0][:2])}


@check('G03')
def _():
    ex = [3, 2, 1, 2]     # the book's example: shares 3, 2, 1 eighths and 2 eighths left
    assert sum(ex) == 8
    return ['open']


@check('G04')
def _():
    ds = [d for d in range(2, 30) if Fr(1, 9) < Fr(1, d) < Fr(1, 3)]
    return {'a': [fs(1, d) for d in ds], 'b': s([len(ds)])}


@check('C01')
def _():
    return [fs(5, 8)]


@check('C02')
def _():
    return ['1/5' if Fr(1, 5) > Fr(1, 9) else '1/9']


@check('C03')
def _():
    return [fs(2 + 4, 7)]


@check('C04')
def _():
    left = Fr(12, 12) - Fr(5, 12) - Fr(3, 12)
    return [fs(int(left * 12), 12)]
