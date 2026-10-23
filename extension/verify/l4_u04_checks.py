"""Independent checks for Level 4 Unit 4 (fractions): exact Fraction arithmetic; unknown wholes are found by search."""
from fractions import Fraction as Fr
CHECKS = {}


def check(id_):
    def deco(f):
        CHECKS[id_] = f
        return f
    return deco


def s(xs):
    return [str(x) for x in xs]


def mixed(n, d):
    w, r = divmod(n, d)
    return w, r, d


def unit_search(parts, shown_value):
    """The whole for 'parts' units equal to shown_value: smallest unit u with parts * u == shown_value."""
    return next(u for u in range(1, 10000) if parts * u == shown_value)


def tf(b):
    return ['>' if b else '<']


@check('L4U04-L01')
def _():
    n, d = 3 * 5 + 4, 5
    return s([n, d])


@check('L4U04-S01')
def _():
    shaded = 6 + 6 + 5
    w, r, d = mixed(shaded, 6)
    return {'a': s([shaded]), 'b': s([w, r, d])}


@check('L4U04-S02')
def _():
    return {'a': s(mixed(19, 4)), 'b': s(mixed(23, 6)), 'c': s(mixed(31, 8)), 'd': s([Fr(40, 5)])}


@check('L4U04-S03')
def _():
    def imp(w, n, d):
        t = Fr(w) + Fr(n, d)
        return [t.numerator, t.denominator] if d == t.denominator else [w * d + n, d]
    return {'a': s(imp(3, 2, 5)), 'b': s(imp(5, 1, 3)), 'c': s(imp(2, 7, 8))}


@check('L4U04-S04')
def _():
    u = unit_search(9, 36)
    return {'a': s([5 * u]), 'b': s([36 - 5 * u])}


@check('L4U04-S05')
def _():
    third = Fr(1, 3)
    pts = {'A': 2 * third, 'B': 4 * third, 'C': 8 * third}
    b = pts['B']
    return {'a': s([pts['A'].numerator, pts['A'].denominator]), 'b': s([b.numerator // b.denominator, (b - 1).numerator, (b - 1).denominator]),
            'c': s([pts['C'].numerator, pts['C'].denominator])}


@check('L4U04-S06')
def _():
    u = unit_search(3, 36)
    return {'a': s([7 * u]), 'b': s([7 * u - 36])}


@check('L4U04-S07')
def _():
    return {'a': tf(Fr(3, 4) > Fr(5, 8)), 'b': tf(Fr(4, 6) > Fr(7, 12)), 'c': tf(Fr(3, 8) > Fr(5, 9)), 'd': tf(Fr(5, 6) > Fr(5, 8))}


@check('L4U04-S08')
def _():
    fs = [(3, 4), (2, 3), (5, 12), (1, 2)]
    return [f'{a}/{b}' for a, b in sorted(fs, key=lambda t: Fr(*t))]


@check('L4U04-S09')
def _():
    a = next(n for n in range(1, 100) if Fr(n, 12) == Fr(2, 3))
    b = next(n for n in range(1, 100) if Fr(15, 20) == Fr(3, n))
    c = next(n for n in range(1, 100) if Fr(9, 12) == Fr(n, 4))
    d = next(n for n in range(1, 100) if Fr(4, 5) == Fr(12, n))
    return {'a': s([a]), 'b': s([b]), 'c': s([c]), 'd': s([d])}


@check('L4U04-S10')
def _():
    w, r, d = mixed(27, 8)
    return {'a': s([w, r, d]), 'b': s([5 * 8]), 'c': s([4 * 8 - 27])}


@check('L4U04-S11')
def _():
    pieces = int((Fr(2) + Fr(2, 3)) / Fr(1, 3))
    left = (pieces - 5) * Fr(1, 3)
    assert left.denominator == 1
    return {'a': s([pieces]), 'b': s([left.numerator])}


@check('L4U04-S12')
def _():
    n = 48
    n -= n // 4
    n -= n // 3
    return s([n])


@check('L4U04-S13')
def _():
    return {'a': s([5 * 4]), 'b': s([3 * 6]), 'c': s([int(Fr(5, 2) / Fr(1, 2))])}


@check('L4U04-T01')
def _():
    c = [n for n in range(1, 60) if Fr(3) < Fr(n, 7) < Fr(4) and n % 2 == 0 and abs(Fr(n, 7) - 4) < abs(Fr(n, 7) - 3)]
    assert len(c) == 1
    return s([c[0], 7])


@check('L4U04-T02')
def _():
    c = [m for m in range(1, 1000) if m - m * Fr(2, 5) - m * Fr(1, 3) == 24]
    assert len(c) == 1
    return s(c)


@check('L4U04-T03')
def _():
    c = [m for m in range(1, 2000) if (m - m * Fr(1, 3)) * (1 - Fr(3, 4)) == 20]
    assert len(c) == 1
    return s(c)


@check('L4U04-G01')
def _():
    c = [n for n in range(1, 40) if Fr(1, 4) < Fr(n, 20) < Fr(3, 5)]
    half = [n for n in range(1, 40) if Fr(n, 20) == Fr(1, 2)]
    return {'a': s([len(c)]), 'b': s(half)}


@check('L4U04-G02')
def _():
    out = {}
    for lab, target in (('a', Fr(5, 6)), ('b', Fr(3, 4)), ('c', Fr(7, 10))):
        sols = [(x, y) for x in range(2, 40) for y in range(x + 1, 80) if Fr(1, x) + Fr(1, y) == target]
        assert len(sols) == 1
        out[lab] = s(sols[0])
    return out


@check('L4U04-G03')
def _():
    c = [m for m in range(1, 1000) if m * Fr(2, 5) * Fr(1, 3) == 6]
    assert len(c) == 1
    return s(c)


@check('L4U04-G04')
def _():
    return {'a': tf(Fr(7, 9) > Fr(8, 10)), 'b': tf(Fr(11, 12) > Fr(9, 10)), 'c': tf(Fr(14, 15) > Fr(19, 20))}


@check('L4U04-C01')
def _():
    return s(mixed(29, 6))


@check('L4U04-C02')
def _():
    t = 5 + Fr(3, 8)
    return s([t.numerator, t.denominator])


@check('L4U04-C03')
def _():
    return ['5/8' if Fr(5, 8) > Fr(7, 12) else '7/12']


@check('L4U04-C04')
def _():
    return s([9 * unit_search(4, 28)])
