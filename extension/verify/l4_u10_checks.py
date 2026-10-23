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
    a = 8 + 1 + 4
    b = next(n for n in range(1, 100) if n - 6 == 4)      # 6th in line with 4 behind: n - place people are behind
    return {'a': s([a]), 'b': s([b])}



@check('L4U10-S09')
def _():
    sol = [k for k in range(1, 45) if k + 4 * k == 45]
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
    sol = [(five, 12 - five) for five in range(13) if 5 * five + 2 * (12 - five) == 45]
    assert len(sol) == 1
    return {'a': s([sol[0][0]]), 'b': s([sol[0][1]])}



@check('L4U10-T02')
def _():
    names = ['Ali', 'Ben', 'Kumar', 'Mei', 'Siti']
    sols = []
    for perm in itertools.permutations(range(1, 6)):
        p = dict(zip(names, perm))
        if p['Ali'] < p['Mei'] < p['Ben'] and p['Kumar'] == p['Siti'] + 1 and p['Ben'] != 5:
            sols.append(p)
    assert len(sols) == 1
    return {'a': [n for _, n in sorted((place, n) for n, place in sols[0].items())]}



@check('L4U10-T03')
def _():
    total, day = 0, 0
    while total <= 100:
        day += 1
        total += 2 * day
    return {'a': s([day]), 'b': s([total])}



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
    return s([9 + 1 + 6])



@check('L4U10-C04')
def _():
    sol = [n for n in range(1, 1000) if n * (n + 1) == 272]
    assert len(sol) == 1
    return s([sol[0], sol[0] + 1])
