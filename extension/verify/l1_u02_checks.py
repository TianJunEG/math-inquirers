"""Independent checks for Level 1 Unit 2 (Number bonds): brute force over small numbers."""
import itertools
from common import s

CHECKS = {}


def check(id_):
    def deco(f):
        CHECKS[id_] = f
        return f
    return deco


def solve(lhs, rhs):
    """The one x in 0..60 with lhs(x) == rhs(x)."""
    sols = [x for x in range(61) if lhs(x) == rhs(x)]
    assert len(sols) == 1, sols
    return sols[0]


@check('L1U02-L01')
def _():
    return s([solve(lambda x: 20, lambda x: 17 + x)])


@check('L1U02-S01')
def _():
    return {'a': s([solve(lambda x: 10, lambda x: 4 + x)]), 'b': s([solve(lambda x: 10, lambda x: 4 + x)])}


@check('L1U02-S02')
def _():
    return {'a': s([solve(lambda x: 10, lambda x: 8 + x)]), 'b': s([solve(lambda x: 10, lambda x: x + 3)]),
            'c': s([solve(lambda x: 10, lambda x: 5 + x)]), 'd': s([solve(lambda x: 10, lambda x: 1 + x)])}


@check('L1U02-S03')
def _():
    return s([solve(lambda x: 10, lambda x: 6 + x)])


@check('L1U02-S04')
def _():
    return s([solve(lambda x: 10, lambda x, k=k: k + x) for k in (1, 3, 6, 8)])


@check('L1U02-S05')
def _():
    return s([solve(lambda x: 12, lambda x: 7 + x), 6 + 8])


@check('L1U02-S06')
def _():
    return {'a': s([solve(lambda x: 20, lambda x: 15 + x)]), 'b': s([solve(lambda x: 20, lambda x: x + 14)]),
            'c': s([solve(lambda x: 20, lambda x: 18 + x)]), 'd': s([solve(lambda x: 20, lambda x: 11 + x)])}


@check('L1U02-S07')
def _():
    assert 7 + 3 == 10
    return s([solve(lambda x: 20, lambda x: 17 + x), solve(lambda x: 30, lambda x: 27 + x), solve(lambda x: 50, lambda x: 47 + x)])


@check('L1U02-S08')
def _():
    return s([solve(lambda x: 20, lambda x: 16 + x)])


@check('L1U02-S09')
def _():
    return {'a': s([solve(lambda x: 6 + 5, lambda x: 7 + x)]), 'b': s([solve(lambda x: 8 + 2, lambda x: 5 + x)]),
            'c': s([solve(lambda x: 9 + 4, lambda x: x + 5)])}


@check('L1U02-S10')
def _():
    seconds = [solve(lambda x: 9, lambda x, k=k: k + x) for k in (2, 3, 4)]
    firsts_up = True
    seconds_down = all(seconds[i + 1] < seconds[i] for i in range(2)) and seconds[0] < 8
    return {'a': s(seconds), 'b': ['down' if seconds_down and firsts_up else 'up']}


@check('L1U02-S11')
def _():
    tf = lambda b: 'True' if b else 'False'
    return {'a': [tf(4 + 6 == 10)], 'b': [tf(8 + 3 == 10)], 'c': [tf(13 + 7 == 20)], 'd': [tf(15 + 6 == 20)]}


@check('L1U02-S12')
def _():
    return s([solve(lambda x: 20, lambda x: 7 + x)])


@check('L1U02-S13')
def _():
    return {'a': s([solve(lambda x: 10, lambda x: 8 + x)]), 'b': s([solve(lambda x: 20, lambda x: 8 + x)])}


@check('L1U02-T01')
def _():
    ways = [(a, 14 - a) for a in range(1, 14) if a < 14 - a]
    return {'': s([len(ways)])}


@check('L1U02-T02')
def _():
    return {'a': s([solve(lambda x: 17, lambda x: x + x + 5)]), 'b': s([solve(lambda x: 21, lambda x: x + x + x)])}


@check('L1U02-T03')
def _():
    sets = [c for c in itertools.combinations(range(1, 7), 3) if sum(c) == 9]
    return [','.join(str(x) for x in c) for c in sets]


@check('L1U02-G01')
def _():
    ali, mei = 16, 8
    gives = [g for g in range(0, 17) if ali - g == mei + g]
    assert len(gives) == 1
    g = gives[0]
    return {'a': s([g]), 'b': s([ali - g])}


@check('L1U02-G02')
def _():
    sols = [(a, b) for a in range(0, 18) for b in range(0, 18) if a + b == 17 and a == b + 5]
    assert len(sols) == 1
    return {'a': s([sols[0][0]]), 'b': s([sols[0][1]])}


@check('L1U02-G03')
def _():
    return s([n for n in range(0, 100) if (n + 7) % 10 == 0 and 15 < n + 7 < 45])


@check('L1U02-G04')
def _():
    count = {}
    for a, b in itertools.combinations(range(1, 6), 2):
        count[a + b] = count.get(a + b, 0) + 1
    return {'a': s(sorted(count)), 'b': s(sorted(t for t, c in count.items() if c == 1))}


@check('L1U02-C01')
def _():
    return s([solve(lambda x: 10, lambda x: 2 + x)])


@check('L1U02-C02')
def _():
    return s([solve(lambda x: 20, lambda x: 6 + x)])


@check('L1U02-C03')
def _():
    return s([solve(lambda x: 7 + 5, lambda x: 9 + x)])


@check('L1U02-C04')
def _():
    return s([solve(lambda x: 20, lambda x: 11 + x)])
