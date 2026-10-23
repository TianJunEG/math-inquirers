"""Independent checks for Level 5 Unit 2 (Fraction feats): exact Fraction arithmetic, simulation and brute force."""
import itertools
from fractions import Fraction as Fr

CHECKS = {}


def check(id_):
    def deco(f):
        CHECKS[id_] = f
        return f
    return deco


def fmt(x):
    """Fraction -> text: whole number, proper fraction, or mixed number 'w n/d'."""
    x = Fr(x)
    if x.denominator == 1:
        return str(x.numerator)
    w, r = divmod(x.numerator, x.denominator)
    return (f'{w} ' if w else '') + f'{r}/{x.denominator}'


def share(total, people):
    return Fr(total, people)


@check('L5U02-L01')
def _():
    beads = 120
    beads -= beads * Fr(1, 4)           # bracelet
    beads -= beads * Fr(2, 3)           # necklace takes 2/3 of the rest
    return [fmt(beads)]


@check('L5U02-S01')
def _():
    return {'a': [fmt(share(7, 10))], 'b': [fmt(share(3, 8))], 'c': [fmt(share(9, 4))]}


@check('L5U02-S02')
def _():
    def bigger(a, b):
        return a if Fr(a) > Fr(b) else b
    return {'a': [bigger('4/5', '5/6')], 'b': [bigger('5/9', '4/7')],
            'c': ['3/4 of 20' if Fr(3, 4) * 20 > Fr(2, 3) * 24 else '2/3 of 24']}


@check('L5U02-S03')
def _():
    part = Fr(64, 8)
    return {'a': [fmt(3 * part)], 'b': [fmt(5 * part)], 'c': [fmt(Fr(1, 4) * 64)]}


@check('L5U02-S04')
def _():
    return {'a': [fmt(Fr(2, 3) + Fr(1, 4))], 'b': [fmt(Fr(5, 6) - Fr(3, 8))], 'c': [fmt(Fr(3, 4) - Fr(1, 6))]}


@check('L5U02-S05')
def _():
    total = Fr(0)
    for _day in range(6):
        total += Fr(3, 4)
    return [fmt(total)]


@check('L5U02-S06')
def _():
    cards = 72
    cards -= cards // 3
    cards -= cards * 3 // 4
    return [str(cards)]


@check('L5U02-S07')
def _():
    left = fmt(Fr(7, 12) - Fr(1, 3))
    return [left, left]


@check('L5U02-S08')
def _():
    seq = lambda k: Fr(k, 2 * k + 1)
    pos = next(k for k in range(1, 100) if seq(k) == Fr(13, 27))
    return {'a': [fmt(seq(5)), fmt(seq(6))], 'b': [fmt(seq(10))], 'c': [str(pos)]}


@check('L5U02-S09')
def _():
    return [fmt(1 - (Fr(2, 5) + Fr(1, 4)))]


@check('L5U02-S10')
def _():
    # quarter marks: the point at 5 quarters and the point at 7 quarters
    return {'a': [fmt(Fr(5, 4))], 'b': [fmt(Fr(7, 4))]}


@check('L5U02-S11')
def _():
    return {'a': [fmt(Fr(2, 3) * Fr(3, 8))], 'b': [fmt(Fr(3, 5) * Fr(2, 3))], 'c': [fmt(Fr(4, 9) * 3)]}


@check('L5U02-S12')
def _():
    # Solve forwards for every possible start money: book 1/3, lunch 1/2 of rest, $18 left
    start = next(m for m in range(1, 1000) if m - m // 3 - (m - m // 3) // 2 == 18 and m % 3 == 0)
    lunch = (start - start // 3) // 2
    return {'a': [str(lunch)], 'b': [str(start)]}


@check('L5U02-S13')
def _():
    n = 40
    cyc = n - Fr(3, 8) * n - Fr(1, 4) * n
    return [fmt(cyc)]


@check('L5U02-S14')
def _():
    t = lambda b: 'True' if b else 'False'
    return {'a': [t(Fr(3, 5) == Fr(5, 3))], 'b': [t(Fr(7, 8) > Fr(5, 6))], 'c': [t(Fr(1, 4) * Fr(1, 2) == Fr(1, 8))]}


@check('L5U02-T01')
def _():
    sols = [(a, b) for a in range(2, 200) for b in range(a + 1, 2000) if Fr(1, a) + Fr(1, b) == Fr(2, 5)]
    assert len(sols) == 1
    a, b = sols[0]
    return {'': [f'1/{a}', f'1/{b}']}


@check('L5U02-T02')
def _():
    for start in range(1, 1000):
        e = Fr(start)
        e -= e * Fr(1, 3)
        e -= e * Fr(1, 4)
        e -= e * Fr(2, 5)
        if e == 36:
            return [str(start)]


@check('L5U02-T03')
def _():
    sums = [Fr(a, b) + Fr(c, d) for a, b, c, d in itertools.permutations([2, 3, 5, 7])]
    return {'a': [fmt(max(sums))], 'b': [fmt(min(sums))]}


@check('L5U02-G01')
def _():
    return [fmt(Fr(5, 6) / 10)]


@check('L5U02-G02')
def _():
    ways = {(a, b) for a in range(2, 500) for b in range(a + 1, 5000) if Fr(1, a) + Fr(1, b) == Fr(1, 6)}
    return [str(len(ways))]


@check('L5U02-G03')
def _():
    for start in range(1, 1000):
        h = Fr(start)
        heights = [h]
        for _b in range(3):
            h = h * Fr(3, 4)
            heights.append(h)
        if h == 27:
            first_under = next(i for i, x in enumerate(heights) if x < Fr(start, 2))
            return {'a': [str(start)], 'b': [str(first_under)]}


@check('L5U02-G04')
def _():
    return [fmt(sum(Fr(1, (2 * k - 1) * (2 * k + 1)) for k in range(1, 5)))]


@check('L5U02-C01')
def _():
    return {'a': [fmt(share(5, 6))], 'b': [fmt(share(7, 3))]}


@check('L5U02-C02')
def _():
    return {'a': [fmt(Fr(7, 8) - Fr(1, 3))], 'b': [fmt(Fr(2, 5) + Fr(3, 10))]}


@check('L5U02-C03')
def _():
    m = 120
    m -= m // 5
    m -= m * 3 // 8
    return [str(m)]


@check('L5U02-C04')
def _():
    return [fmt(1 - Fr(3, 4) - Fr(1, 6))]
