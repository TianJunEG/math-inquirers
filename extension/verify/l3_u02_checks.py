"""Independent checks for Level 3 Unit 2 (Cryptarithm crackers): missing digits, magic squares, pyramids and letter puzzles are
solved by brute force over the unknowns; every answer is recomputed here, never copied from the book."""
import itertools
from common import s

CHECKS = {}


def check(id_):
    def deco(f):
        CHECKS[id_] = f
        return f
    return deco


def digit_solutions(fn):
    """All digits d in 0..9 for which fn(d) is true."""
    return [d for d in range(10) if fn(d)]


def only(xs):
    assert len(xs) == 1, xs
    return xs[0]


def num(*ds):
    return int(''.join(str(d) for d in ds))


@check('L3U02-L01')
def _():
    return s([only(digit_solutions(lambda d: num(3, d, 4, 8) + 2517 == 5965))])


@check('L3U02-S01')
def _():
    return {'a': s([only(digit_solutions(lambda d: num(3, d, 4, 6) + 1251 == 4597))]),
            'b': s([only(digit_solutions(lambda d: num(2, 6, d, 9) + 1435 == 4104))])}


@check('L3U02-S02')
def _():
    return {'a': s([only(digit_solutions(lambda d: 6405 - num(2, d, 1, 8) == 3687))]),
            'b': s([only(digit_solutions(lambda d: num(9, d, 3, 0) - 4617 == 4513))])}


@check('L3U02-S03')
def _():
    sat, sun = 3875, 2968
    return {'a': s([sat + sun]), 'b': s([sat - sun])}


@check('L3U02-S04')
def _():
    left = 8000
    for used in (2475, 3150):
        left -= used
    return s([left])


@check('L3U02-S05')
def _():
    claim = 5000 - 1768   # the correct value, computed here
    siti = 3342
    return {'a': s([siti + 1768]), 'b': ['Yes' if siti == claim else 'No'], 'c': s([claim])}


def magic_ok(g):
    tot = sum(g[0])
    lines = [r for r in g] + [[g[r][c] for r in range(3)] for c in range(3)] + [[g[i][i] for i in range(3)], [g[i][2 - i] for i in range(3)]]
    return all(sum(l) == tot for l in lines)


@check('L3U02-S07')
def _():
    sols = []
    for A in range(0, 1200, 10):
        for B in range(0, 1200, 10):
            for C in range(0, 1200, 10):
                g = [[200, 450, A], [550, 350, 150], [300, B, C]]
                if magic_ok(g):
                    sols.append((A, B, C, sum(g[1])))
    A, B, C, tot = only(sols)
    return {'a': s([tot]), 'b': s([A, B, C])}


def pyramid_ok(bottom_to_top):
    for lower, upper in zip(bottom_to_top, bottom_to_top[1:]):
        if any(upper[i] != lower[i] + lower[i + 1] for i in range(len(upper))):
            return False
    return True


@check('L3U02-S08')
def _():
    sols = []
    for P_ in range(0, 1600):
        for Q in range(0, 1600):
            rows = [[350, Q, 270], [830, P_], [1580]]
            if pyramid_ok(rows):
                sols.append((P_, Q))
    P_, Q = only(sols)
    return {'a': s([P_]), 'b': s([Q])}


@check('L3U02-S09')
def _():
    sols = [(a, b) for a in range(10) for b in range(10) if num(3, a, 5, 2) + num(2, 4, b, 6) == 6148]
    a, b = only(sols)
    return {'a': s([a]), 'b': s([b])}


@check('L3U02-S11')
def _():
    sols = [(a, b) for a in range(10) for b in range(10) if num(6, a, 0, 2) - num(2, 8, b, 5) == 3657]
    a, b = only(sols)
    return {'a': s([a]), 'b': s([b])}


@check('L3U02-S10')
def _():
    a = only([d for d in range(1, 10) if (10 * d + 3) + (20 + d) == 56])
    c = only([d for d in range(1, 10) if (10 * d + 5) * 2 == 90])
    return {'a': s([a]), 'b': s([c])}


@check('L3U02-S06')
def _():
    x = 2641
    partner = int(''.join(str(9 - int(ch)) for ch in str(x)))
    assert x + partner == 9999
    return {'a': s([partner]), 'b': s([10000 - x])}


@check('L3U02-S12')
def _():
    return s([9000 - 3475])


@check('L3U02-S13')
def _():
    cards = [2, 3, 4, 5, 7, 8]
    sums = set()
    for p in itertools.permutations(cards):
        sums.add(num(*p[:3]) + num(*p[3:]))
    return {'a': s([max(sums)]), 'b': s([min(sums)])}


def letter_solutions(words_fn, letters):
    out = []
    for d in itertools.permutations(range(10), len(letters)):
        m = dict(zip(letters, d))
        r = words_fn(m)
        if r:
            out.append(m)
    return out


@check('L3U02-T01')
def _():
    f = lambda m: m['A'] and m['B'] and (10 * m['A'] + m['B']) + (10 * m['A'] + m['C']) == 100 * m['B'] + 10 * m['B'] + m['D']
    m = only(letter_solutions(f, 'ABCD'))
    return {'a': s([m['A']]), 'b': s([m['B']]), 'c': s([m['C']]), 'd': s([m['D']])}


@check('L3U02-T02')
def _():
    best = min(num(*p[:3]) + num(*p[3:]) for p in itertools.permutations([1, 3, 5, 6, 8]))
    return s([best])


@check('L3U02-T03')
def _():
    sols = []
    for A in range(0, 700, 30):
        for B in range(0, 700, 30):
            for C in range(0, 700, 30):
                for D in range(0, 700, 30):
                    for E in range(0, 700, 30):
                        g = [[120, 270, A], [B, 210, C], [180, D, E]]
                        if magic_ok(g):
                            sols.append((A, E, sum(g[0])))
    A, E, tot = only(sols)
    return {'a': s([tot]), 'b': s([A]), 'c': s([E])}


@check('L3U02-G01')
def _():
    f = lambda m: m['A'] and m['B'] and m['C'] and 100 * m['A'] + 10 * m['B'] + m['C'] + 10 * m['B'] + m['C'] == 100 * m['C'] + 10 * m['A'] + m['B']
    m = only(letter_solutions(f, 'ABC'))
    return {'a': s([m['A']]), 'b': s([m['B']]), 'c': s([m['C']])}


@check('L3U02-G02')
def _():
    sols = []
    for X in range(0, 1000):
        b = [200, X, X, 440]
        r3 = [b[i] + b[i + 1] for i in range(3)]
        r2 = [r3[i] + r3[i + 1] for i in range(2)]
        if r2[0] + r2[1] == 3280:
            sols.append(X)
    return s([only(sols)])


@check('L3U02-G03')
def _():
    rev = lambda n: int(str(n)[::-1])
    sums = [n + rev(n) for n in (36, 58, 47)]
    common = [k for k in range(2, 20) if all(x % k == 0 for x in sums) and k > 10]
    return {'a': s([sums[0]]), 'b': s([sums[1]]), 'c': s([sums[2]]), 'd': s([only(common)])}


@check('L3U02-G04')
def _():
    # example: shown bricks top 800, middle-left 370, bottom-right 180; the hidden bricks must be unique
    sols = []
    for a in range(0, 801):
        for b in range(0, 801):
            c = 180
            if a + b == 370 and b + c + a + b == 800:
                sols.append((a, b))
    a, b = only(sols)
    assert (a, b, b + 180) == (120, 250, 430)
    return s([800])


@check('L3U02-C01')
def _():
    return s([only(digit_solutions(lambda d: num(4, d, 7, 2) + 2519 == 7091))])


@check('L3U02-C02')
def _():
    return s([only(digit_solutions(lambda d: num(8, d, 0, 4) - 3569 == 4635))])


@check('L3U02-C03')
def _():
    sols = [M for M in range(0, 1200) if pyramid_ok([[240, 280, 360], [M, 640], [1160]])]
    return s([only(sols)])


@check('L3U02-C04')
def _():
    return s([9000 - 2845 - 3260])


@check('L3U02-S14')
def _():
    wk = [1875, 2430, 1790]
    return {'a': s([sum(wk)]), 'b': s([wk[1] - wk[2]])}
