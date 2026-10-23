"""Independent checks for Level 6 Unit 9 (Data detectives).  Means are found by adding up and dividing (written out, no statistics library), medians by sorting,
missing values by trying every number, T01 by listing every possible set of 5 numbers; the printed bar charts, tables and code are read from the unit file."""
import itertools
from fractions import Fraction
from common import load_unit
from l6_lib import run, s

CHECKS = {}
U = load_unit(6, 9)
ITEM = {i['id']: i for i in U['items']}


def check(id_):
    def deco(f):
        CHECKS[id_] = f
        return f
    return deco


def prog_of(id_):
    return ITEM[id_]['figure']['prog']


def fr(x):
    return Fraction(str(x))


def mean(xs):
    t = Fraction(0)
    for x in xs:
        t += fr(x)
    return t / len(xs)


def num(f):
    """a Fraction as a plain number text: 7, 2.75, 1.3"""
    f = Fraction(f)
    return int(f) if f.denominator == 1 else float(f)


def median(xs):
    ys = sorted(xs)
    n = len(ys)
    return Fraction(ys[n // 2]) if n % 2 else (Fraction(ys[n // 2 - 1]) + Fraction(ys[n // 2])) / 2


def modes(xs):
    counts = {}
    for x in xs:
        counts[x] = counts.get(x, 0) + 1
    top = max(counts.values())
    return sorted(k for k, v in counts.items() if v == top)


@check('L6U09-L01')
def _():
    x = [x for x in range(0, 200) if mean([8, 14, 12, 7, x]) == 10][0]
    return s([x])


@check('L6U09-S01')
def _():
    return {'a': [num(mean([14, 9, 11, 6]))], 'b': [num(mean([9, 0, 6, 0, 10]))], 'c': [num(mean([1.5, 2.5, 4, 3]))]}


@check('L6U09-S02')
def _():
    vals = ITEM['L6U09-S02']['figure']['values']
    m = mean(vals)
    moved = sum(v - m for v in vals if v > m)
    return {'a': [num(m)], 'b': [num(moved)]}


@check('L6U09-S03')
def _():
    total = [t for t in range(0, 200) if t / 5 == 6][0]            # 5 parcels with a mean of 6 kg
    others = [x for x in range(0, 100) if 4 + 9 + 7 + x == total]
    return {'a': [total], 'b': others}


@check('L6U09-S04')
def _():
    x = [x for x in range(0, 101) if mean([78, 90, 85, x]) == 82][0]
    y = [y for y in range(0, 101) if mean([78, 90, 85, x, y]) == 82][0]
    return {'a': [x], 'b': [y]}


@check('L6U09-S05')
def _():
    base = [10, 12, 14]
    m0 = mean(base)
    same = mean(base + [12]) == m0
    return {'a': ['stays the same' if same else ('goes up' if mean(base + [12]) > m0 else 'goes down')],
            'b': [num(mean(base + [20]))], 'c': [num(mean([10, 12]))]}


@check('L6U09-S06')
def _():
    d1, d2 = [12, 7, 9, 7, 5], [2, 8, 4, 6]
    m = modes(d1)
    assert len(m) == 1
    return {'a': [num(median(d1))], 'b': m, 'c': [num(mean(d1))], 'd': [num(median(d2))]}


@check('L6U09-S07')
def _():
    pay = [1500, 1600, 1600, 1700, 1800, 1900, 9500]
    mn, md = mean(pay), median(pay)
    near = lambda c: len([p for p in pay if abs(p - c) <= 500])      # how many staff earn within 500 of the average
    return {'a': [num(mn)], 'b': [num(md)], 'c': ['median' if near(md) > near(mn) else 'mean']}


@check('L6U09-S08')
def _():
    vals = ITEM['L6U09-S08']['figure']['values']
    m = mean(vals)
    return {'a': [sum(vals)], 'b': [num(m)], 'c': [len([v for v in vals if v > m])]}


@check('L6U09-S09')
def _():
    prog = prog_of('L6U09-S09')
    env, said = run(prog, env={'scores': [7, 9, 3, 5]})
    p3 = prog[:3] + [['look', 'say (total ÷ 3)']]
    env3, said3 = run(p3, env={'scores': [7, 9, 3, 5]})
    return {'a': [env['total']], 'b': [said[0]], 'c': [said3[0]]}


@check('L6U09-S10')
def _():
    base = [4, 8, 12]
    return {'a': [num(mean([x + 5 for x in base]))], 'b': [num(mean([2 * x for x in base]))]}


@check('L6U09-S11')
def _():
    five = 5 * 40
    six = five + 52
    return {'a': [five], 'b': [six], 'c': [num(Fraction(six, 6))]}


@check('L6U09-T01')
def _():
    sols = []
    for t in itertools.combinations_with_replacement(range(1, 31), 5):
        if mean(list(t)) == 8 and median(list(t)) == 7 and t[-1] == 12 and modes(list(t)) == [5]:
            sols.append(t)
    assert len(sols) == 1
    t = sols[0]
    return {'a': [sum(t)], 'b': [t[0]], 'c': [t[3]]}


@check('L6U09-T02')
def _():
    girls, boys = 12 * 40, 18 * 45
    allm = Fraction(girls + boys, 30)
    return {'a': [girls], 'b': [boys], 'c': [num(allm)], 'd': ['boys' if allm > Fraction(40 + 45, 2) else 'girls']}


@check('L6U09-T03')
def _():
    total = 3 * fr(4.6)
    third = total - fr(3.9) - fr(5.4)
    return {'a': [num(total)], 'b': [num(third)]}


@check('L6U09-G01')
def _():
    seq = [7 + 5 * k for k in range(20)]
    assert seq[-1] == 102
    pairs = [(seq[k], seq[-1 - k]) for k in range(10)]
    assert all(a + b == seq[0] + seq[-1] for a, b in pairs)
    return {'a': [seq[0] + seq[-1]], 'b': [len(pairs)], 'c': [num(mean(seq))]}


@check('L6U09-G02')
def _():
    prog = prog_of('L6U09-G02')
    env, said = run(prog, env={'marks': [4, 8, 6, 10, 7]})
    p4 = [prog[0], prog[1], ['ctl', 'repeat (4)', prog[2][2]], prog[3]]
    env4, said4 = run(p4, env={'marks': [4, 8, 6, 10, 7]})
    env6, said6 = run(prog, env={'marks': [4, 8, 6, 10, 7, 13]})
    return {'a': [said[0]], 'b': [round(said4[0], 1)], 'c': [said6[0]]}


@check('L6U09-G03')
def _():
    fig = ITEM['L6U09-G03']['figure']['rows']
    goals = [int(g) for g in fig[0][1:]]
    matches = [int(m) for m in fig[1][1:]]
    data = []
    for g, m in zip(goals, matches):
        data += [g] * m
    assert len(data) == 10
    return {'a': [sum(data)], 'b': [num(mean(data))], 'c': [num(median(data))]}


@check('L6U09-C01')
def _():
    return s([num(mean([6, 10, 2, 14]))])


@check('L6U09-C02')
def _():
    d = [4, 9, 4, 6, 11]
    return s([num(median(d)), modes(d)[0]])


@check('L6U09-C03')
def _():
    return s([[x for x in range(0, 100) if mean([3, 7, 4, 9, x]) == 6][0]])


@check('L6U09-C04')
def _():
    tests = [70, 70, 70, 70]
    return s([num(mean(tests + [80]))])
