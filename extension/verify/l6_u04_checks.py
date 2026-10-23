"""Independent checks for Level 6 Unit 4 (Algebra machines).  Machines are run forwards on every IN by brute force (no inverse formulas), rules are found by
trying every pair of numbers, tables are read from the unit file, and the printed code is run by the l6_lib interpreter."""
from common import load_unit
from l6_lib import run, s, fit_rule

CHECKS = {}
U = load_unit(6, 4)
ITEM = {i['id']: i for i in U['items']}
LEARN = U['learn']


def check(id_):
    def deco(f):
        CHECKS[id_] = f
        return f
    return deco


def prog_of(id_):
    return ITEM[id_]['figure']['prog']


def table(id_):
    rows = ITEM[id_]['figure']['rows']
    return [(int(a), int(b)) for a, b in zip(rows[0][1:], rows[1][1:])]


def inverse(f, out, lim=500):
    """the IN that gives this OUT, found by trying every whole number"""
    hits = [n for n in range(0, lim) if f(n) == out]
    assert len(hits) == 1, hits
    return hits[0]


@check('L6U04-L01')
def _():
    f = lambda n: n * 4 + 9
    return s([inverse(f, 41)])


@check('L6U04-S01')
def _():
    a, b = fit_rule(table('L6U04-S01'))
    f = lambda n: a * n + b
    return {'a': [a, b], 'b': [f(10)], 'c': [inverse(f, 50)]}


@check('L6U04-S02')
def _():
    a, b = fit_rule(table('L6U04-S02'))
    f = lambda n: a * n + b
    assert b < 0
    return {'a': [a, -b], 'b': [f(20)], 'c': [inverse(f, 100)]}


@check('L6U04-S03')
def _():
    P_ = lambda x: x * 2 + 6
    Q_ = lambda x: (x + 6) * 2
    same = all(P_(x) == Q_(x) for x in range(0, 50))
    return {'a': [P_(7), Q_(7)], 'b': [P_(10), Q_(10)], 'c': ['Yes' if same else 'No']}


@check('L6U04-S04')
def _():
    ch = ITEM['L6U04-S04']['figure']['chain']
    inn, out = int(ch[0]), int(ch[4])
    mid = inn * 3
    k = out - mid
    assert ch[3] == '+ ?'
    return {'a': [mid], 'b': [k], 'c': [9 * 3 + k]}


@check('L6U04-S05')
def _():
    f = lambda pred: [n for n in range(0, 300) if pred(n)][0]
    return {'a': [f(lambda n: 5 * n + 8 == 63)], 'b': [f(lambda n: 9 * n - 7 == 74)], 'c': [f(lambda n: (n + 4) * 6 == 66)],
            'd': [f(lambda n: n % 5 == 0 and n // 5 + 3 == 11)]}


def ask_run(prog, value):
    env, said = run(prog, hooks={r'ask \(': lambda t, env, kids: env.__setitem__('answer', value)})
    return said[0]


@check('L6U04-S06')
def _():
    prog = prog_of('L6U04-S06')
    ins = [n for n in range(0, 300) if ask_run(prog, n) == 61]
    assert len(ins) == 1
    return {'a': [ask_run(prog, 9)], 'b': [ask_run(prog, 25)], 'c': ins}


@check('L6U04-S07')
def _():
    prog = prog_of('L6U04-S07')
    # the blanks: set n to start, repeat until (7n - 4) = target, change n by step
    start, target, step = 0, 73, 1
    filled = [['var', f'set n to ({start})'], ['ctl', prog[1][1].replace('( )', f'({target})'), [['var', f'change n by ({step})']]], prog[2]]
    env, said = run(filled)
    n = said[0]
    assert 7 * n - 4 == target
    return {'a': [start], 'b': [target], 'c': [step], 'd': [n]}


@check('L6U04-S08')
def _():
    n = 8
    mei, wei = n + 5, 3 * n
    total = lambda k: k + (k + 5) + 3 * k
    a, b = fit_rule([(1, total(1)), (2, total(2)), (3, total(3))])
    return {'a': [mei, wei], 'b': [total(8)], 'c': [a, b]}


@check('L6U04-S09')
def _():
    cost = lambda n: 12 + 3 * n
    a, b = fit_rule([(n, cost(n)) for n in range(1, 5)])
    best = max(n for n in range(0, 100) if cost(n) <= 60)
    assert cost(best) == 60
    return {'a': [cost(5)], 'b': [a, b], 'c': [best]}


@check('L6U04-S10')
def _():
    def trick(x):
        v = x + 4
        v = v * 3
        v = v - 9
        v = v // 3 if v % 3 == 0 else None
        return v - x
    results = {trick(x) for x in range(0, 200)}
    assert results == {1}
    return {'a': [trick(7)], 'b': [trick(12)], 'c': [1]}


@check('L6U04-S11')
def _():
    prog = prog_of('L6U04-S11')
    f = lambda n: ask_run(prog, n)
    eights = [n for n in range(0, 100) if f(n) == 8]
    assert len(eights) == 2
    return {'a': [f(6)], 'b': [f(15)], 'c': s(eights)}


@check('L6U04-T01')
def _():
    X_ = lambda x: x * 2 + 3
    Y_ = lambda y: y * 3 - 4
    f = lambda n: Y_(X_(n))
    a, b = fit_rule([(n, f(n)) for n in range(0, 5)])
    return {'a': [f(5)], 'b': [inverse(f, 77)], 'c': [a, b]}


@check('L6U04-T02')
def _():
    total = lambda n: n + (n + 4) + 3 * n
    n = [k for k in range(1, 80) if total(k) == 64][0]
    a, b = fit_rule([(k, total(k)) for k in range(0, 4)])
    return {'a': [a, b], 'b': [n], 'c': [3 * n]}


@check('L6U04-T03')
def _():
    pts = [(3, 13), (8, 38)]
    a, b = fit_rule(pts)
    assert b < 0
    return {'a': [pts[1][1] - pts[0][1]], 'b': [a, -b], 'c': [inverse(lambda n: a * n + b, 98)]}


@check('L6U04-G01')
def _():
    A_ = lambda n: n * 4 + 1
    B_ = lambda n: n * 2 + 13
    n = [k for k in range(0, 100) if A_(k) == B_(k)]
    assert len(n) == 1
    return {'a': [A_(2), B_(2)], 'b': [n[0], A_(n[0])]}


@check('L6U04-G02')
def _():
    def starts(count, step, total):
        return [n for n in range(0, 200) if sum(n + step * i for i in range(count)) == total]
    a = starts(4, 1, 130)
    b = [n for n in starts(5, 2, 125) if n % 2 == 1]
    c = starts(4, 1, 100)
    return {'a': s(a), 'b': s(b), 'c': ['Yes' if c else 'No']}


@check('L6U04-G03')
def _():
    prog = prog_of('L6U04-G03')
    env, said = run(prog)
    p2 = [prog[0], [prog[1][0], prog[1][1].replace('(120)', '(123)'), prog[1][2]], prog[2]]
    assert p2[1][1] != prog[1][1]
    env2, said2 = run(p2)
    return {'a': [said[0]], 'b': [env['n'] * 7 - 3], 'c': [said2[0]]}


@check('L6U04-C01')
def _():
    a, b = fit_rule([(1, 6), (2, 11), (3, 16), (4, 21)])
    return s([a, b])


@check('L6U04-C02')
def _():
    return s([inverse(lambda n: n * 9 - 5, 49)])


@check('L6U04-C03')
def _():
    return s([inverse(lambda n: 4 * n + 9, 57)])


@check('L6U04-C04')
def _():
    return s([[n for n in range(0, 100) if n + (n + 4) == 30][0]])
