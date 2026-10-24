"""Independent checks for Level 2 Unit 5 (number machines, working backwards): every IN is found by trying numbers forwards through the machine."""
import itertools
from common import s

CHECKS = {}


def check(i):
    def d(f):
        CHECKS['L2U05-' + i] = f
        return f
    return d


def run(x, ops):
    for op, n in ops:
        x = {'+': x + n, '-': x - n, '*': x * n, '/': x / n}[op]
    return x


def find_in(ops, out, hi=500):
    sol = [x for x in range(0, hi + 1) if run(x, ops) == out]
    assert len(sol) == 1, (ops, out, sol)
    return sol[0]


@check('L01')
def _():
    return s([find_in([('*', 5), ('-', 8)], 32)])


@check('S01')
def _():
    return {'a': s([find_in([('+', 27)], 61)]), 'b': s([find_in([('*', 5)], 35)]), 'c': s([find_in([('/', 4)], 9)]), 'd': s([find_in([('-', 18)], 25)])}


@check('S02')
def _():
    # the step that undoes an operation: it must return every test number to where it started
    undo = {'+': '-', '-': '+', '*': '/', '/': '*'}
    def undoes(op1, n, op2):
        return all(run(run(x, [(op1, n)]), [(op2, n)]) == x for x in (12, 24, 60))
    pick = lambda op1, n, options: [o for o in options if undoes(op1, n, o)]
    a = pick('+', 7, ['+', '-', '*'])
    b = pick('*', 5, ['*', '/', '-'])
    c = pick('-', 12, ['-', '+', '/'])
    d = pick('/', 3, ['/', '+', '*'])
    for r in (a, b, c, d):
        assert len(r) == 1
    names = {'+': '+ ', '-': '- ', '*': '× ', '/': '÷ '}
    return {'a': [names[a[0]] + '7'], 'b': [names[b[0]] + '5'], 'c': [names[c[0]] + '12'], 'd': [names[d[0]] + '3']}


@check('S03')
def _():
    return {'a': s([find_in([('*', 2), ('+', 9)], 25)]), 'b': s([find_in([('-', 6), ('*', 4)], 28)]), 'c': s([find_in([('/', 5), ('+', 7)], 11)])}


@check('S04')
def _():
    f = lambda t: find_in(t, 0) if False else None
    sol = lambda expr: [x for x in range(0, 200) if expr(x)]
    a = sol(lambda x: x / 2 + 7 == 15)
    b = sol(lambda x: 4 * x - 5 == 19)
    c = sol(lambda x: x * 10 + 8 == 78)
    assert len(a) == len(b) == len(c) == 1
    return {'a': s(a), 'b': s(b), 'c': s(c)}


@check('S05')
def _():
    ops = [('*', 4), ('-', 1)]
    return {'a': s([run(3, ops), run(6, ops), find_in(ops, 31), find_in(ops, 39)])}


@check('S06')
def _():
    fits = [(m, a) for m in (2, 3, 4) for a in range(0, 20) if 3 * m + a == 11 and 6 * m + a == 17]
    assert len(fits) == 1
    m, a = fits[0]
    return {'a': s([m]), 'b': s([a]), 'c': s([10 * m + a])}


@check('S07')
def _():
    ops = [('-', 18), ('+', 25)]
    start = find_in(ops, 60)
    return {'a': s([60 - 25]), 'b': s([start]), 'c': s([run(start, ops[:1]), run(start, ops)])}


@check('S08')
def _():
    box = [x for x in range(1, 100) if x - 3 == 7][0]     # box 4 held 7 after 3 came out, so it held 10 before
    assert box == 10
    return {'a': s([box]), 'b': s([4 * box])}


@check('S09')
def _():
    ops = [('+', 12), ('/', 4)]
    start = find_in(ops, 5)
    return {'a': s([4 * 5]), 'b': s([start])}


@check('S10')
def _():
    spent = 3 + 8
    start = [x for x in range(0, 200) if x - 3 - 8 == 12][0]
    return {'a': s([spent]), 'b': s([start])}


@check('T01')
def _():
    sol = [(m, m + 6, m + 9) for m in range(0, 52) if m + m + 6 + m + 9 == 51]
    assert len(sol) == 1
    return {'a': s([sol[0][0]]), 'b': s([sol[0][1]]), 'c': s([sol[0][2]])}


@check('T02')
def _():
    sol = [(first, after) for first in range(0, 100) for after in [first - 8] if after + after == 30]
    assert len(sol) == 1
    return {'a': s([sol[0][1]]), 'b': s([sol[0][0]])}


@check('T03')
def _():
    outs = {4 * x + 1 for x in range(0, 100)}
    Y = lambda n: 'Yes' if n in outs else 'No'
    return {'a': [Y(29)], 'b': [Y(30)], 'c': [Y(33)], 'd': [Y(42)]}


@check('G01')
def _():
    f = lambda e: [n for n in range(0, 200) if e(n)]
    a, b, c = f(lambda n: 3 * n + 4 == 25), f(lambda n: 5 * n - 3 == 27), f(lambda n: n / 2 + 8 == 13)
    assert len(a) == len(b) == len(c) == 1
    return {'a': s(a), 'b': s(b), 'c': s(c)}


@check('G02')
def _():
    sol = []
    for a, b, c in itertools.product(range(0, 37), repeat=3):
        if a + b + c != 36:
            continue
        a2, b2 = a - 4, b + 4        # 4 beans from A to B
        b3, c3 = b2 - 6, c + 6       # then 6 from B to C
        if a2 == b3 == c3:
            sol.append((a, b, c))
    assert len(sol) == 1
    a, b, c = sol[0]
    return {'a': s([36 // 3]), 'b': s([a, b, c])}


@check('G03')
def _():
    ops = [('+', 7), ('*', 2)]
    assert run(12, ops) == 38 and find_in(ops, 38) == 12
    return ['open']


@check('G04')
def _():
    A = [('*', 2), ('+', 3)]
    B = [('-', 5), ('*', 3)]
    sol = [x for x in range(0, 300) if run(run(x, A), B) == 36]
    assert len(sol) == 1
    return {'a': s([run(sol[0], A)]), 'b': s(sol)}


@check('C01')
def _():
    return s([find_in([('*', 4), ('+', 6)], 38)])


@check('C02')
def _():
    return s([find_in([('-', 14), ('+', 9)], 31)])


@check('C03')
def _():
    return s([find_in([('*', 2), ('+', 9)], 25)])


@check('C04')
def _():
    each = [x for x in range(1, 100) if x - 6 == 4][0]
    return s([5 * each])
