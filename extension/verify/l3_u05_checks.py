"""Independent checks for Level 3 Unit 5 (Remainder riddles): division with remainder is done by repeated subtraction of the
divisor; riddles and puzzles are solved by listing every candidate number and testing every clue."""
from common import s

CHECKS = {}


def check(id_):
    def deco(f):
        CHECKS[id_] = f
        return f
    return deco


def divmod_sub(n, d):
    """quotient and remainder by repeated subtraction"""
    q = 0
    while n >= d:
        n -= d
        q += 1
    return q, n


def only(xs):
    xs = list(xs)
    assert len(xs) == 1, xs
    return xs[0]


@check('L3U05-L01')
def _():
    return s(divmod_sub(43, 6))


@check('L3U05-S01')
def _():
    q, r = divmod_sub(19, 4)
    return {'a': s([q]), 'b': s([r])}


@check('L3U05-S02')
def _():
    return {k: s(divmod_sub(a, b)) for k, (a, b) in zip('abcd', [(38, 7), (50, 8), (61, 9), (75, 6)])}


@check('L3U05-S03')
def _():
    q1, r1 = divmod_sub(26, 5)
    q2, r2 = divmod_sub(37, 6)
    q3, r3 = divmod_sub(30, 4)
    cars = q1 + (1 if r1 else 0)     # leftover people still need a car
    return {'a': s([cars]), 'b': s([q2]), 'c': s([q3]), 'd': s([r3])}


@check('L3U05-S04')
def _():
    # Kumar's answer breaks the rule remainder < divisor
    claimed_r, divisor = 10, 7
    assert claimed_r >= divisor
    return {'a': s([divisor]), 'b': s(divmod_sub(59, 7))}


@check('L3U05-S05')
def _():
    lst = [3 + 5 * k for k in range(40)]
    return {'a': s([only({divmod_sub(n, 5)[1] for n in lst})]), 'b': s(['Yes' if 83 in lst else 'No']), 'c': s([lst[9]])}


@check('L3U05-S06')
def _():
    rems = sorted({divmod_sub(n, 5)[1] for n in range(5, 200)} | {0})
    ok = [n for n in range(20, 41) if divmod_sub(n, 6)[1] == 0 and divmod_sub(n, 5)[1] == 1]
    return {'a': s(rems), 'b': s([only(ok)])}


@check('L3U05-S07')
def _():
    rems = [divmod_sub(n, 4)[1] for n in range(12, 20)]
    return {'a': s(rems), 'b': s([divmod_sub(30, 4)[1]]), 'c': s([divmod_sub(100, 4)[1]])}


@check('L3U05-S08')
def _():
    first = [n for n in range(31, 40) if divmod_sub(n, 6)[1] == 1]
    both = [n for n in first if divmod_sub(n, 4)[1] == 3]
    return {'a': s(first), 'b': s([only(both)])}


@check('L3U05-S09')
def _():
    q, r = divmod_sub(52, 9)
    buses = q + (1 if r else 0)
    return {'a': s([buses]), 'b': s([r]), 'c': s([9 - r])}


@check('L3U05-S10')
def _():
    letters = 'ABCD'
    nth = lambda n: letters[(n - 1) % 4]
    return {'a': [nth(30)], 'b': [nth(32)]}


@check('L3U05-S11')
def _():
    beads = 8 * 9 + 5
    return {'a': s([beads]), 'b': s(divmod_sub(beads, 9))}


@check('L3U05-S12')
def _():
    return s([n for n in (18, 23, 33, 41, 48) if divmod_sub(n, 5)[1] == 3])


@check('L3U05-S13')
def _():
    rems = {d: divmod_sub(47, d)[1] for d in (4, 5, 6, 7, 8)}
    return s([only(d for d, r in rems.items() if r == max(rems.values()))])


DAYS = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']


@check('L3U05-T01')
def _():
    today = DAYS.index('Tue')
    ahead = today
    for _ in range(45):
        ahead = (ahead + 1) % 7      # step one day at a time
    back = today
    for _ in range(20):
        back = (back - 1) % 7
    return {'a': [DAYS[ahead]], 'b': [DAYS[back]]}


@check('L3U05-T02')
def _():
    c = [n for n in range(10, 100) if divmod_sub(n, 5)[1] == 2 and divmod_sub(n, 3)[1] == 1 and divmod_sub(n, 4)[1] == 3]
    return s([only(c)])


@check('L3U05-T03')
def _():
    def seat(start, moves):
        pos = start
        for _ in range(moves):
            pos = pos % 8 + 1
        return pos
    return {'a': s([seat(3, 29)]), 'b': s([seat(5, 50)])}


@check('L3U05-G01')
def _():
    def rems(n, d, f):
        return divmod_sub(f(n), d)[1]
    a = {rems(n, 7, lambda x: x + 5) for n in range(3, 500, 7)}
    b = {rems(n, 7, lambda x: 2 * x) for n in range(3, 500, 7)}
    c = {rems(n, 8, lambda x: 2 * x) for n in range(5, 500, 8)}
    return {'a': s([only(a)]), 'b': s([only(b)]), 'c': s([only(c)])}


@check('L3U05-G02')
def _():
    c = [n for n in range(21, 100) if divmod_sub(n, 3)[1] == 1 and divmod_sub(n, 4)[1] == 2 and divmod_sub(n, 5)[1] == 3]
    return s([only(c)])


@check('L3U05-G03')
def _():
    c = [n for n in range(11, 25) if divmod_sub(n, 4)[1] == 1 and divmod_sub(n, 3)[1] == 2]
    return s([only(c)])


@check('L3U05-G04')
def _():
    can = lambda n: any((n - 5 * five) >= 0 and (n - 5 * five) % 3 == 0 for five in range(0, n // 5 + 1))
    return {'a': ['Yes' if can(11) else 'No'], 'b': s([n for n in range(1, 16) if not can(n)])}


@check('L3U05-C01')
def _():
    return s(divmod_sub(52, 8))


@check('L3U05-C02')
def _():
    q, r = divmod_sub(40, 9)
    return s([q + (1 if r else 0)])


@check('L3U05-C03')
def _():
    return s([divmod_sub(25, 6)[1]])


@check('L3U05-C04')
def _():
    c = [n for n in range(21, 30) if divmod_sub(n, 3)[1] == 2 and divmod_sub(n, 5)[1] == 4]
    return s([only(c)])
