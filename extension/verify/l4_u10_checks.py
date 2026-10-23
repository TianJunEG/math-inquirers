"""Independent checks for Level 4 Unit 10 (puzzle day): every puzzle is solved by exhaustive search over the unknown (no supposition or algebra), and
logic puzzles by trying every arrangement."""
import itertools
from common import load_unit
CHECKS = {}
U = load_unit(4, 10)
ITEM = {i['id']: i for i in [U['learn']['try']] + U['items']}


def check(id_):
    def deco(f):
        CHECKS[id_] = f
        return f
    return deco


def s(xs):
    return [str(x) for x in xs]


def two_kinds(total, legs, a_legs, b_legs):
    """All (a, b) counts with a + b = total animals and a*a_legs + b*b_legs = legs."""
    return [(a, total - a) for a in range(total + 1) if a * a_legs + (total - a) * b_legs == legs]


@check('L4U10-L01')
def _():
    sol = two_kinds(10, 66, 8, 6)
    assert len(sol) == 1
    return s([sol[0][0]])


@check('L4U10-S01')
def _():
    sol = [n for n in range(1, 1000) if n * (n + 1) == 506]
    assert len(sol) == 1
    return s([sol[0], sol[0] + 1])


@check('L4U10-S02')
def _():
    ways = [(p, n) for p in range(1, 20) for n in range(1, 10) if 3 * p + 5 * n == 41]
    fewest = min(ways)
    return {'a': s([len(ways)]), 'b': s(fewest)}


@check('L4U10-S03')
def _():
    sol = two_kinds(17, 50, 4, 2)          # (cows, hens)
    assert len(sol) == 1
    return {'a': s([17 * 2]), 'b': s([50 - 17 * 2]), 'c': s([sol[0][0]])}


@check('L4U10-S04')
def _():
    sol = two_kinds(13, 33, 3, 2)          # (tricycles, bicycles)
    assert len(sol) == 1
    return {'a': s([sol[0][0]]), 'b': s([sol[0][1]])}


@check('L4U10-S05')
def _():
    ops = ITEM['L4U10-S05']['figure']['ops']
    assert ops == ['÷ 2', '+ 12', '− 7']
    sol = [x for x in range(2, 1000, 2) if x // 2 + 12 - 7 == 25]
    assert len(sol) == 1
    return s(sol)


@check('L4U10-S06')
def _():
    sol = [x for x in range(1, 500) if (x * 2 + 14) / 4 == 10]
    assert len(sol) == 1
    return s(sol)


@check('L4U10-S07')
def _():
    pets = ['cat', 'dog', 'fish', 'rabbit']
    sols = []
    for perm in itertools.permutations(pets):
        ali, ben, mei, siti = perm
        if ali == 'dog' and ben == 'fish' and mei != 'rabbit':
            sols.append(perm)
    assert len(sols) == 1
    return dict(zip('abcd', [[x] for x in sols[0]]))


@check('L4U10-S08')
def _():
    total = next(n for n in range(1, 200) if 9 <= n and n - 5 + 1 == 9)       # 9th from the front and 5th from the back
    back = 25 - 8 + 1
    return {'a': s([total]), 'b': s([back])}


@check('L4U10-S09')
def _():
    sol = [sit for sit in range(1, 44) if (44 - sit) + 6 == 3 * (sit + 6)]
    assert len(sol) == 1
    return s(sol)


@check('L4U10-S10')
def _():
    sol = [k for k in range(10) if 50 * k + 20 * (9 - k) == 300]
    assert len(sol) == 1
    return s(sol)


@check('L4U10-S11')
def _():
    sol = [n for n in range(1, 100) if n + n + 1 + n + 2 == 87]
    assert len(sol) == 1
    return s([sol[0], sol[0] + 1, sol[0] + 2])


@check('L4U10-S12')
def _():
    sol = [10 * a + b for a in range(1, 10) for b in range(10) if a + b == 12 and 10 * b + a == 10 * a + b + 18]
    assert len(sol) == 1
    return s(sol)


@check('L4U10-T01')
def _():
    sol = [(t6, 14 - t6) for t6 in range(15) if 6 * t6 + 4 * (14 - t6) == 68]
    assert len(sol) == 1
    totals = [6 * k + 4 * (14 - k) for k in range(15)]
    return {'a': s([sol[0][0]]), 'b': s([min(totals), max(totals)])}


@check('L4U10-T02')
def _():
    names = ['Aisha', 'Ben', 'Kumar', 'Mei', 'Ravi']
    sols = []
    for perm in itertools.permutations(range(1, 6)):
        p = dict(zip(names, perm))
        if (p['Aisha'] == 3 and p['Kumar'] in (1, 5) and abs(p['Kumar'] - p['Ravi']) != 1 and p['Mei'] > p['Ravi'] and abs(p['Ben'] - p['Aisha']) != 1):
            sols.append(p)
    assert len(sols) == 1
    p = sols[0]
    return {'a': [n for _, n in sorted((seat, n) for n, seat in p.items())]}


@check('L4U10-T03')
def _():
    sol = [g for g in range(1, 100) if 7 * g + 12 == 3 * (g + 12)]
    assert len(sol) == 1
    return s(sol)


@check('L4U10-G01')
def _():
    return s([sum(1 for n in range(1, 201) if sum(int(d) for d in str(n)) == 5)])


@check('L4U10-G02')
def _():
    sol = [n for n in range(1, 100) if 50 * n + 20 * (3 * n) == 440]
    assert len(sol) == 1
    return s([4 * sol[0]])


@check('L4U10-G03')
def _():
    sols = []
    for n in range(11, 200):
        mei = n - 8 + 1                 # place of Mei counted from the left
        if mei != 11 and abs(mei - 11) - 1 == 5:
            sols.append(n)
    return s(sols)


@check('L4U10-G04')
def _():
    return {'a': s([3 ** 5 % 10]), 'b': s([3 ** 20 % 10])}


@check('L4U10-C01')
def _():
    sol = two_kinds(10, 28, 4, 2)
    assert len(sol) == 1
    return s([sol[0][0]])


@check('L4U10-C02')
def _():
    sol = [x for x in range(1, 500) if (x + 8) * 2 - 6 == 30]
    assert len(sol) == 1
    return s(sol)


@check('L4U10-C03')
def _():
    return s([6 - 1 + 1 + 9 - 1])


@check('L4U10-C04')
def _():
    sol = [n for n in range(1, 1000) if n * (n + 1) == 272]
    assert len(sol) == 1
    return s([sol[0], sol[0] + 1])
