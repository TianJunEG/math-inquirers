"""Independent checks for Level 6 Unit 3 (Below zero).  Numbers are moved one step at a time along a line (no sign rules), the printed code is run by the
l6_lib interpreter, and marks on the printed number lines are read from the unit file."""
from common import load_unit
from l6_lib import run, s

CHECKS = {}
U = load_unit(6, 3)
ITEM = {i['id']: i for i in U['items']}


def check(id_):
    def deco(f):
        CHECKS[id_] = f
        return f
    return deco


def move(start, delta):
    """walk |delta| single steps right (delta > 0) or left (delta < 0)"""
    x = start
    for _ in range(abs(delta)):
        x += 1 if delta > 0 else -1
    return x


def steps(a, b):
    """number of single steps from a to b (either direction)"""
    n, x = 0, a
    while x != b:
        x += 1 if b > a else -1
        n += 1
    return n


def prog_of(id_):
    return ITEM[id_]['figure']['prog']


def mark(id_, label):
    return [m['at'] for m in ITEM[id_]['figure']['marks'] if m['lab'] == label][0]


@check('L6U03-L01')
def _():
    return s([move(-3, -8)])


@check('L6U03-S01')
def _():
    nums = [2, -6, -11, 0, -3, 8]
    pairs = [(-4, -10), (0, -2), (-15, 1)]
    return {'a': s(sorted(nums)), 'b': ['>' if a > b else '<' for a, b in pairs]}


@check('L6U03-S02')
def _():
    f = 'L6U03-S02'
    A_, B_, C_ = mark(f, 'A'), mark(f, 'B'), mark(f, 'C')
    return {'a': s([A_, B_, C_]), 'b': s([steps(A_, B_), steps(B_, C_)])}


@check('L6U03-S03')
def _():
    f = 'L6U03-S03'
    am, noon, pm = mark(f, '6 a.m.'), mark(f, 'noon'), mark(f, '9 p.m.')
    return {'a': [am], 'b': [noon], 'c': [pm], 'd': [steps(am, noon)], 'e': [steps(noon, pm)]}


@check('L6U03-S04')
def _():
    return {'a': [move(-6, 10)], 'b': [move(3, -9)], 'c': [move(-7, -5)], 'd': [move(-4, 15)]}


@check('L6U03-S05')
def _():
    r = range(-60, 61)
    return {'a': [[x for x in r if move(-5, x) == 6][0]], 'b': [[x for x in r if move(4, -x) == -3][0]],
            'c': [[x for x in r if move(x, 8) == 2][0]], 'd': [[x for x in r if move(x, -5) == -9][0]]}


@check('L6U03-S06')
def _():
    return {'a': [steps(-9, 4)], 'b': [steps(-6, -1)], 'c': [steps(-14, 31)]}


@check('L6U03-S07')
def _():
    env, said = run(prog_of('L6U03-S07'))
    return {'a': [said[2]], 'b': [said[-1]], 'c': [sum(1 for v in said if v < 0)]}


@check('L6U03-S08')
def _():
    d = [d for d in range(-60, 60) if run([['var', 'set x to (100)'], ['ctl', 'repeat (4)', [['var', f'change x by ({d})']]]])[0]['x'] == 0][0]
    env, _ = run([['var', 'set x to (100)'], ['ctl', 'repeat (8)', [['var', 'change x by (-20)']]]])
    return {'a': [d], 'b': [env['x']]}


@check('L6U03-S09')
def _():
    bal = move(25, -40)
    bal2 = move(bal, 30)
    return {'a': [bal], 'b': [bal2], 'c': [steps(-15, 20)]}


@check('L6U03-S10')
def _():
    order = [c for c in ITEM['L6U03-S10']['figure']['rows'][0]]      # L3 L2 L1 B1 B2 B3 from the top floor down
    def floors(a, b):
        i, n = order.index(a), 0
        while order[i] != b:
            i += 1 if order.index(b) > i else -1
            n += 1
        return n
    return {'a': [floors('L3', 'B2')], 'b': [floors('B3', 'L1')], 'c': [floors('L2', 'B1')]}


@check('L6U03-S11')
def _():
    nums = [-9, 5, -3, 7, -4]
    return {'a': [min(nums, key=lambda v: steps(0, v))], 'b': [max((-8, 6), key=lambda v: steps(0, v))]}


@check('L6U03-T01')
def _():
    def minus(a, b):
        # a - b is the number of steps to go from b up to a (a > b here); found by walking
        return steps(b, a) if a > b else -steps(a, b)
    r1, r2 = minus(6, -4), minus(-2, -5)
    plus4 = [k for k in range(-20, 21) if 6 + k == r1][0]
    assert -2 + 5 == r2 and 6 + 4 == r1
    return {'a': [r1], 'b': [r2], 'c': [plus4]}


@check('L6U03-T02')
def _():
    trace = []
    env, said = run(prog_of('L6U03-T02'), trace=trace)
    return {'a': [len(trace)], 'b': [said[0]]}


@check('L6U03-T03')
def _():
    mon = 3
    tue = move(mon, -11)
    wed = move(tue, 6)
    thu = -4
    return {'a': [tue], 'b': [wed], 'c': [steps(mon, thu)]}


@check('L6U03-G01')
def _():
    a, b, rows = -12, -40, []
    for minute in range(0, 12):
        rows.append((minute, a, b))
        a = move(a, -4)
        b = move(b, 6)
    first = [m for m, x, y in rows if y > x][0]
    r3 = rows[3]
    r5 = rows[5]
    return {'a': [r3[1], r3[2]], 'b': [first], 'c': [steps(r5[1], r5[2])]}


@check('L6U03-G02')
def _():
    prog = prog_of('L6U03-G02')
    out = {}
    for lab, (a, b) in (('a', (-8, 5)), ('b', (-3, -9)), ('c', (-6, -6))):
        env, said = run(prog, env={'a': a, 'b': b})
        assert said[0] == steps(a, b)          # it says the gap between a and b
        out[lab] = [said[0]]
    return out


@check('L6U03-G03')
def _():
    years = [f'{y} BC' for y in range(12, 0, -1)] + [f'AD {y}' for y in range(1, 15)]     # no year 0
    def gap(a, b):
        return years.index(b) - years.index(a)
    return {'a': [gap('5 BC', '1 BC')], 'b': [gap('3 BC', 'AD 4')], 'c': [gap('10 BC', 'AD 12')]}


@check('L6U03-C01')
def _():
    return s([move(-9, 14), move(6, -13)])


@check('L6U03-C02')
def _():
    return s(sorted([4, -7, -2, 0]))


@check('L6U03-C03')
def _():
    return s([move(move(-6, 11), -8)])


@check('L6U03-C04')
def _():
    env, _ = run([['var', 'set x to (20)'], ['ctl', 'repeat (3)', [['var', 'change x by (-15)']]]])
    return s([env['x']])
