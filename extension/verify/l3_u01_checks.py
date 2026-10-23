"""Independent checks for Level 3 Unit 1 (Number sleuths): every answer is recomputed by brute force over digits, never copied."""
import itertools
from common import s

CHECKS = {}


def check(id_):
    def deco(f):
        CHECKS[id_] = f
        return f
    return deco


def perms(cards):
    """All different 4-digit numbers (no leading 0) made with every card once, as ints, sorted."""
    return sorted({int(''.join(map(str, p))) for p in itertools.permutations(cards) if p[0] != 0})


@check('L3U01-L01')
def _():
    return s([max(n for n in perms([3, 8, 1, 4]) if n % 2 == 0)])


@check('L3U01-S01')
def _():
    d = [4, 0, 7, 2]
    return {'a': s([int(''.join(map(str, d)))]), 'b': s([d[2] * 10])}


@check('L3U01-S02')
def _():
    return {'a': s([6 * 1000 + 5 * 100 + 9]), 'b': s([2 * 1000 + 15 * 10]), 'c': s([5 * 1000 + 12 * 100 + 3])}


@check('L3U01-S03')
def _():
    return {'a': s([6457 + 1000]), 'b': s([3050 - 100]), 'c': s([8995 + 10]), 'd': s([7000 - 1])}


@check('L3U01-S04')
def _():
    return s(sorted([5830, 5083, 5380, 5038]))


@check('L3U01-S05')
def _():
    return s([3 * 1000 + 14 * 100 + 6])


@check('L3U01-S06')
def _():
    ns = perms([2, 7, 5, 8])
    odd = [n for n in ns if n % 2]
    return {'a': s([ns[-1]]), 'b': s([ns[0]]), 'c': s([odd[-1]]), 'd': s([odd[0]])}


@check('L3U01-S07')
def _():
    return s(perms([3, 0, 0, 5]))


@check('L3U01-S08')
def _():
    def nxt_arith(seq, k=2):
        d = seq[-1] - seq[-2]
        return [seq[-1] + d * (i + 1) for i in range(k)]
    a = nxt_arith([2300, 2600, 2900])
    b = nxt_arith([9000, 8750, 8500])
    seq, j = [3, 4, 6, 9, 13], 5
    c = []
    cur = seq[-1]
    for _ in range(2):
        cur += j; j += 1; c.append(cur)
    return {'a': s(a), 'b': s(b), 'c': s(c)}


@check('L3U01-S09')
def _():
    seq = [4000 + 500 * i for i in range(0, 12)]
    return {'a': ['Yes' if 6800 in seq else 'No'], 'b': s([min(x for x in seq if x > 6800)])}


@check('L3U01-S10')
def _():
    # read from the drawing (viewed): A is halfway between the 6100 and 6200 labels, B halfway between 6400 and 6500, C halfway between 6300 and 6400
    mid = lambda lo, hi: (lo + hi) // 2
    return {'a': s([mid(6100, 6200)]), 'b': s([mid(6400, 6500)]), 'c': s([mid(6300, 6400)])}


@check('L3U01-S11')
def _():
    out = []
    for h in range(10):
        for t in range(10):
            for o in range(10):
                if 6 - h == 3 and t == 0 and o == max(d for d in range(10) if d % 2):
                    out.append(6000 + h * 100 + t * 10 + o)
    assert len(out) == 1
    return s(out)


@check('L3U01-S12')
def _():
    ns = perms([9, 4, 6, 2])
    return {'a': ['No' if 9642 not in [n for n in ns if n % 2] else 'Yes'], 'b': s([max(n for n in ns if n % 2)])}


@check('L3U01-S13')
def _():
    digits = [int(c) for c in '5737']
    first7 = digits.index(7)
    last7 = len(digits) - 1 - digits[::-1].index(7)
    v1 = 7 * 10 ** (len(digits) - 1 - first7)
    v2 = 7 * 10 ** (len(digits) - 1 - last7)
    return {'a': s([v1]), 'b': s([v2]), 'c': s([v1 - v2])}


@check('L3U01-T01')
def _():
    ok = [n for n in range(1000, 10000) if len(set(str(n))) == 4 and sum(map(int, str(n))) == 8 and n % 2 == 0]
    return {'a': s([max(ok)]), 'b': s([min(ok)])}


@check('L3U01-T02')
def _():
    return s([sum(str(n).count('7') for n in range(1, 201))])


@check('L3U01-T03')
def _():
    ns = sorted(int(''.join(p)) for p in itertools.product('12', repeat=4))
    return s([ns[9]])


@check('L3U01-G01')
def _():
    def count(total):
        return sum(1 for n in range(100, 1000) if sum(map(int, str(n))) == total)
    return {'a': s([count(4)]), 'b': s([count(5)])}


@check('L3U01-G02')
def _():
    seq = [5, 8, 14, 23, 35]
    jumps = [b - a for a, b in zip(seq, seq[1:])]
    assert all(j2 - j1 == 3 for j1, j2 in zip(jumps, jumps[1:]))
    out = []
    j = jumps[-1]
    cur = seq[-1]
    for _ in range(2):
        j += 3; cur += j; out.append(cur)
    return s(out)


@check('L3U01-G03')
def _():
    # the example puzzle must have exactly one solution
    sols = [n for n in range(7000, 8000) if (n // 100) % 10 == 2 * ((n // 10) % 10) and n % 10 == (n // 10) % 10 + 1 and sum(map(int, str(n))) == 16]
    assert sols == [7423], sols
    return s(sols)


@check('L3U01-G04')
def _():
    sols = [n for n in range(3000, 4000) if len(set(str(n))) == 4 and (n // 10) % 10 == 0 and (n // 100) % 10 == 2 * (n % 10) and sum(map(int, str(n))) == 15]
    assert len(sols) == 1
    return s(sols)


@check('L3U01-C01')
def _():
    return s([int('7258'[1]) * 100])


@check('L3U01-C02')
def _():
    seq = [6500, 6000, 5500]
    d = seq[1] - seq[0]
    return s([seq[-1] + d, seq[-1] + 2 * d])


@check('L3U01-C03')
def _():
    return s([perms([6, 1, 0, 5])[0]])


@check('L3U01-C04')
def _():
    return s([5 * 1000 + 12 * 100 + 8])
