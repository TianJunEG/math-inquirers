"""Independent checks for Level 3 Unit 6 (Fraction walls): every answer is recomputed with exact fractions (fractions.Fraction) or by
listing all candidates; equal fractions are found by scaling, never read from the book."""
import itertools
from fractions import Fraction as Fr
from common import s

CHECKS = {}


def check(id_):
    def deco(f):
        CHECKS[id_] = f
        return f
    return deco


def only(xs):
    xs = list(xs)
    assert len(xs) == 1, xs
    return xs[0]


def sym(a, b):
    return '<' if a < b else ('>' if a > b else '=')


def top_over(den, value):
    """the numerator of `value` written with bottom number den (must be exact)"""
    x = value * den
    assert x.denominator == 1, (den, value)
    return int(x)


def fmt(f, den=None):
    if den:
        return f'{top_over(den, f)}/{den}'
    return f'{f.numerator}/{f.denominator}'


@check('L3U06-L01')
def _():
    return [sym(Fr(7, 12), Fr(2, 3))]


@check('L3U06-S01')
def _():
    one3, two3, five6 = Fr(1, 3), Fr(2, 3), Fr(5, 6)
    return {'a': s([top_over(6, one3), top_over(12, one3)]), 'b': s([top_over(6, two3), top_over(12, two3)]), 'c': s([top_over(12, five6)])}


@check('L3U06-S02')
def _():
    # shapes in the figure: (shaded parts, parts in the whole)
    shapes = {'a': (3, 8), 'b': (4, 6), 'c': (7, 10), 'd': (2, 5)}
    return {k: s([v[0], v[1]]) for k, v in shapes.items()}


@check('L3U06-S03')
def _():
    # equal parts: bar A cut at 1/4, 1/2, 3/4; bar B cut at 0.15, 0.55, 0.8; circle C 6 sectors of 60; circle D sectors 150, 60, 90, 60
    parts = {'A': [0.25] * 4, 'B': [0.15, 0.4, 0.25, 0.2], 'C': [60] * 6, 'D': [150, 60, 90, 60]}
    return [k for k, v in parts.items() if len(set(v)) == 1]


@check('L3U06-S04')
def _():
    return {'a': [sym(Fr(5, 8), Fr(3, 8))], 'b': [sym(Fr(1, 3), Fr(1, 4))], 'c': [sym(Fr(2, 4), Fr(4, 8))], 'd': [sym(Fr(3, 4), Fr(5, 6))]}


@check('L3U06-S05')
def _():
    return [fmt(f) for f in sorted([Fr(5, 6), Fr(1, 3), Fr(1, 2), Fr(2, 3)])]


@check('L3U06-S06')
def _():
    return {'a': s([top_over(10, Fr(3, 10) + Fr(4, 10))]), 'b': s([top_over(8, Fr(5, 8) - Fr(2, 8))]),
            'c': s([top_over(12, Fr(9, 12) - Fr(4, 12))]), 'd': s([top_over(10, 1 - Fr(3, 10))])}


@check('L3U06-S07')
def _():
    return {'a': s([top_over(4, Fr(1, 2) + Fr(1, 4))]), 'b': s([top_over(6, Fr(1, 3) + Fr(1, 6))]),
            'c': s([top_over(8, Fr(3, 4) - Fr(1, 8))]), 'd': s([top_over(6, Fr(5, 6) - Fr(1, 2))])}


@check('L3U06-S08')
def _():
    ali, ben = Fr(3, 12), Fr(4, 12)
    return {'a': s([top_over(12, ali + ben)]), 'b': s([top_over(12, 1 - ali - ben)]), 'c': s([top_over(12, ben - ali)])}


@check('L3U06-S09')
def _():
    # 8 equal steps; the arrows are read from the drawing at steps 3, 5, 7 and 4
    steps = {'A': 3, 'B': 5, 'C': 7, 'D': 4}
    half = [k for k, v in steps.items() if Fr(v, 8) == Fr(1, 2)]
    return {'a': s([steps['A']]), 'b': s([steps['B']]), 'c': s([steps['C']]), 'd': [only(half)]}


@check('L3U06-S10')
def _():
    return {'a': s([top_over(12, Fr(3, 4))]), 'b': s([top_over(10, Fr(2, 5))]),
            'c': s([only(d for d in range(1, 40) if Fr(5, d) == Fr(1, 2))]), 'd': s([only(d for d in range(1, 40) if Fr(3, d) == Fr(6, 8))])}


@check('L3U06-S11')
def _():
    right = Fr(3, 8) + Fr(2, 8)
    return {'a': ['Yes' if right == Fr(5, 16) else 'No'], 'b': s([top_over(8, right)])}


@check('L3U06-T01')
def _():
    return [fmt(Fr(k, 12), 12) for k in range(1, 12) if Fr(1, 3) < Fr(k, 12) < Fr(2, 3)]


@check('L3U06-T02')
def _():
    sols = [(t, b) for b in range(1, 100) for t in range(1, b) if Fr(t, b) == Fr(2, 5) and b - t == 9]
    return s(only(sols))


@check('L3U06-T03')
def _():
    mei, ali = Fr(1, 4), Fr(1, 3)
    return {'a': s([top_over(12, mei + ali)]), 'b': s([top_over(12, 1 - mei - ali)])}


@check('L3U06-G01')
def _():
    def second(total, first):
        left = total - first
        assert left.numerator == 1
        return left.denominator
    return {'a': s([second(Fr(3, 4), Fr(1, 2))]), 'b': s([second(Fr(5, 6), Fr(1, 2))]), 'c': s([second(Fr(7, 12), Fr(1, 3))])}


@check('L3U06-G02')
def _():
    sols = [(h, q, e) for h in range(7) for q in range(7) for e in range(7)
            if h + q + e == 6 and h * Fr(1, 2) + q * Fr(1, 4) + e * Fr(1, 8) == 1]
    return {'a': s(only(sols))}


@check('L3U06-G03')
def _():
    lines, dots = Fr(1, 2) * 12, Fr(1, 3) * 12
    white = 12 - lines - dots
    return {'a': s([int(white)]), 'b': s([only(d for d in range(1, 40) if Fr(1, d) == white / 12)])}


@check('L3U06-G04')
def _():
    assert Fr(3, 8) + Fr(2, 8) == Fr(5, 8)     # the example story
    return ['5/8']


@check('L3U06-C01')
def _():
    shaded, parts = 5, 8
    return s([shaded])


@check('L3U06-C02')
def _():
    return [sym(Fr(5, 8), Fr(3, 4))]


@check('L3U06-C03')
def _():
    return s([top_over(8, Fr(5, 8) - Fr(1, 4))])


@check('L3U06-C04')
def _():
    return s([top_over(12, Fr(2, 3))])
