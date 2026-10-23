"""Independent checks for Level 2 Unit 1 (numbers to 1000): everything is recomputed by enumeration."""
import itertools
from common import s

CHECKS = {}


def check(i):
    def d(f):
        CHECKS['L2U01-' + i] = f
        return f
    return d


def perms(cards):
    return sorted({int(''.join(map(str, p))) for p in itertools.permutations(cards, 3) if p[0] != 0})


def digsum(n):
    return sum(int(c) for c in str(n))


@check('L01')
def _():
    return s([len(perms([9, 0, 3]))])


@check('S01')
def _():
    return {'a': s([3 * 100 + 5 * 10 + 6]), 'b': s([8 * 100 + 0 + 4]), 'c': s([(590 - 500) // 10]), 'd': s([int(str(837)[1]) * 10])}


@check('S02')
def _():
    return s([3 * 100 + 12 * 10 + 4])


@check('S03')
def _():
    return s(perms([8, 1, 5]))


@check('S04')
def _():
    L = perms([8, 1, 5])
    return {'a': s([max(L), min(L)]), 'b': s([min(L, key=lambda n: abs(n - 600))]), 'c': s([sum(1 for n in L if n % 2)])}


@check('S05')
def _():
    L = perms([6, 0, 4])
    return {'a': s(L), 'b': s([len(L)])}


@check('S06')
def _():
    f = lambda a, b: '<' if a < b else ('>' if a > b else '=')
    return {'a': [f(745, 754)], 'b': [f(306, 296)], 'c': [f(5 * 100 + 2 * 10, 502)], 'd': [f(88 * 10, 880)]}


@check('S07')
def _():
    return s(sorted([508, 85, 580, 805]))


@check('S08')
def _():
    A, B = 300 + 4 * 10, 300 + 7 * 10      # arrows sit on the 4th and 7th tick after 300 (ticks every 10)
    return {'a': s([A]), 'b': s([B]), 'c': s([B - A])}


@check('S09')
def _():
    val = lambda r, c: 571 + c + 10 * r      # one step right +1, one step down +10
    given = {(0, 0): 571, (0, 1): 572, (1, 1): 582, (1, 2): 583, (2, 0): 591}
    assert all(val(*k) == v for k, v in given.items())
    return {'a': s([val(0, 2), val(1, 0), val(2, 1), val(2, 2)]), 'b': s([645 - 10, 645 - 1, 645 + 1, 645 + 10]), 'c': s([612 + 3 * 10])}


@check('S10')
def _():
    a = [n for n in range(100, 1000) if n // 100 == 6 and n % 10 == n // 10 % 10 - 2 and digsum(n) == 14]
    b = [n for n in range(301, 310) if n % 2 and digsum(n) == 8]
    assert len(a) == 1 and len(b) == 1
    return {'a': s(a), 'b': s(b)}


@check('S11')
def _():
    T = lambda b: 'True' if b else 'False'
    return {'a': [T(5 * 10 + 12 == 62)], 'b': [T(7 * 100 == 700 * 10)], 'c': [T(900 == 9)], 'd': [T(10 * 100 == 1000)]}


@check('T01')
def _():
    L = sorted({int(''.join(map(str, p))) for p in itertools.permutations([1, 4, 6, 9], 3)})
    L = [n for n in L if n % 2 == 0]
    return {'a': s([len(L)]), 'b': s([sum(1 for n in L if n > 600)])}


@check('T02')
def _():
    L = [n for n in range(100, 1000) if n % 2 and n // 10 % 10 == 0 and digsum(n) == 11]
    return {'a': s(L), 'b': s([min(L, key=lambda n: abs(n - 500))])}


@check('T03')
def _():
    cnt = lambda hi: sum(str(n).count('7') for n in range(1, hi + 1))
    return {'a': s([cnt(100)]), 'b': s([cnt(200)])}


@check('G01')
def _():
    return {'a': s([4 * 1000 + 2 * 100 + 0 * 10 + 7]), 'b': s([2650 + 1000]), 'c': s([25 * 100])}


@check('G02')
def _():
    return s([sum(1 for n in range(100, 1000) if str(n) == str(n)[::-1])])


@check('G03')
def _():
    ok = [n for n in range(100, 1000) if n // 10 % 10 == 5 and digsum(n) == 12 and int(str(n)[::-1]) - n == 297]
    assert len(ok) == 1
    return s(ok)


@check('G04')
def _():
    ok = [n for n in range(300, 400) if digsum(n) == 12 and n % 10 == 2]   # the book's example clues must leave only 372
    assert ok == [372]
    return ['open']


@check('C01')
def _():
    return s([7 * 100 + 13 * 10])


@check('C02')
def _():
    return s([max(n for n in perms([5, 0, 8]) if n % 2 == 0)])


@check('C03')
def _():
    v, out = 312, []
    for _ in range(4):
        v -= 10
        out.append(v)
    return s(out[2:])


@check('C04')
def _():
    return s([sum(1 for n in range(531, 542) if n % 2)])
