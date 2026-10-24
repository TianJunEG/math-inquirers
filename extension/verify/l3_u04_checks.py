"""Independent checks for Level 3 Unit 4 (Model makers): each story is solved by searching the unknown amounts (integer or cents)
and testing every condition of the story, never by re-using the book's method or answer."""
from fractions import Fraction
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


@check('L3U04-L01')
def _():
    return s([only(x for x in range(0, 481) if x + 215 == 480)])


@check('L3U04-S01')
def _():
    return s([only(w for w in range(0, 2401) if 875 + w == 2400)])


@check('L3U04-S02')
def _():
    aisha = only(a for a in range(0, 1451) if a + 380 == 1450)
    return {'a': s([aisha]), 'b': s([1450 + aisha])}


@check('L3U04-S03')
def _():
    fri, sat, sun = 468, 539, 392
    return {'a': s([fri + sat + sun]), 'b': s([only(d for d in range(0, 600) if sun + d == sat)])}


@check('L3U04-S05')
def _():
    sols = [(si, me) for si in range(0, 141) for me in range(0, 141) if si + me == 140 and me == 3 * si]
    si, me = only(sols)
    return {'a': s([si]), 'b': s([me])}


@check('L3U04-S06')
def _():
    sols = [(w, k) for w in range(0, 91) for k in range(0, 91) if w + k == 90 and k == w + 18]
    w, k = only(sols)
    return {'a': s([w]), 'b': s([k])}


@check('L3U04-S07')
def _():
    return s([only(p for p in range(0, 79) if 78 - p == 52 + p)])


@check('L3U04-S04')
def _():
    siti, wei, add = 64, 29, 12
    return {'a': s([siti - wei]), 'b': s([(siti + add) - (wei + add)])}


@check('L3U04-S08')
def _():
    mon = 85
    tue = only(t for t in range(0, 300) if t == mon + 28)
    wed = only(w for w in range(0, 300) if w + 17 == tue)
    return {'a': s([tue]), 'b': s([wed]), 'c': s([mon + tue + wed])}


@check('L3U04-S09')
def _():
    cents = only(c for c in range(0, 5001) if c + 1840 + 675 == 5000)
    return s([f'{cents // 100}.{cents % 100:02d}'])


@check('L3U04-S10')
def _():
    sols = [(a, w) for a in range(0, 100) for w in range(0, 100) if w == 3 * a and w == 48]
    a, w = only(sols)
    return {'a': s([a]), 'b': s([a + w])}


@check('L3U04-S11')
def _():
    ravi_claim = 54 + 18
    ben = only(b for b in range(0, 100) if b + 18 == 54)
    return {'a': ['Yes' if ravi_claim == ben else 'No'], 'b': s([ben])}


@check('L3U04-S12')
def _():
    saved = 0
    for _ in range(7):
        saved += 12
    return s([saved - 35])


@check('L3U04-T01')
def _():
    sols = []
    for wei in range(1, 85):
        kumar = 84 - wei
        if kumar != 3 * wei:
            continue
        for give in range(0, kumar + 1):
            if kumar - give == wei + give:
                sols.append(give)
    return s([only(sols)])


@check('L3U04-T02')
def _():
    sols = [(pen, box) for pen in range(1, 30) for box in range(1, 30) if box + 2 * pen == 14 and box + 5 * pen == 23]
    pen, box = only(sols)
    return {'a': s([pen]), 'b': s([box])}


@check('L3U04-T03')
def _():
    return s([only(y for y in range(0, 100) if 35 + y == 2 * (7 + y))])


@check('L3U04-G01')
def _():
    sols = [(l, k, a) for l in range(0, 141) for k in (l + 12,) for a in (2 * k,) if l + k + a == 140]
    l, k, a = only(sols)
    return {'a': s([l]), 'b': s([k]), 'c': s([a])}


@check('L3U04-G02')
def _():
    sols = [4 * b + b for b in range(1, 100) if 4 * b - 18 == b]
    return s([only(sols)])


@check('L3U04-G03')
def _():
    sols = [(a, b) for a in range(0, 61) for b in range(0, 61) if a + b == 60 and b == a + 12]
    a, b = only(sols)
    return s([a])


@check('L3U04-C01')
def _():
    return s([only(x for x in range(0, 2001) if x + 735 + 640 == 2000)])


@check('L3U04-C02')
def _():
    siti = 560 + 135
    return s([560 + siti])


@check('L3U04-C03')
def _():
    sols = [(k, si) for k in range(0, 73) for si in range(0, 73) if si == 5 * k and k + si == 72]
    return s([only(sols)[1]])


@check('L3U04-C04')
def _():
    sols = [(a, b) for a in range(0, 51) for b in range(0, 51) if a + b == 50 and a == b + 8]
    return s([only(sols)[0]])
