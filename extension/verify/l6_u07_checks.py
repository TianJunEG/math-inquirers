"""Independent checks for Level 6 Unit 7 (Turtle geometry).  A small turtle simulator (position, heading, total turned) runs the printed programs; polygon
angles are found by trying whole numbers of sides and turns (no angle-sum formulas); the printed tables are read from the unit file."""
import math, re
from common import load_unit
from l6_lib import run, ev, s

CHECKS = {}
U = load_unit(6, 7)
ITEM = {i['id']: i for i in U['items']}


def check(id_):
    def deco(f):
        CHECKS[id_] = f
        return f
    return deco


def prog_of(id_):
    return ITEM[id_]['figure']['prog']


def turtle(prog, env=None, heading=90.0):
    """run a program of 'move (n) steps' and 'turn (a) degrees' blocks; returns the state"""
    st = {'x': 0.0, 'y': 0.0, 'h': heading, 'turned': 0.0, 'dist': 0.0, 'log': []}

    def mv(t, e, kids):
        n = ev(re.match(r'move \((.*)\) steps', t).group(1), e)
        st['x'] += n * math.sin(math.radians(st['h']))
        st['y'] += n * math.cos(math.radians(st['h']))
        st['dist'] += n

    def tn(t, e, kids):
        a = ev(re.match(r'turn \S+ \((.*)\) degrees', t).group(1), e)
        st['h'] += a
        st['turned'] += a
        st['log'].append(st['turned'])

    def pd(t, e, kids):
        st['h'] = ev(re.match(r'point in direction \((.*)\)', t).group(1), e)

    run(prog, env=env, hooks={r'move \(': mv, r'turn': tn, r'point in direction': pd})
    return st


def sides_for_turn(t):
    """number of equal turns of t degrees that bring the turtle back to its start direction after exactly one full turn"""
    n = 1
    while n * t < 360:
        n += 1
    return n if n * t == 360 else None


def turn_for_sides(n):
    cands = [t for t in range(1, 361) if n * t == 360]
    return cands[0] if cands else None


@check('L6U07-L01')
def _():
    t = turn_for_sides(18)
    return s([t, 180 - t])


@check('L6U07-S01')
def _():
    out = []
    t = turn_for_sides(5); out += [t, 180 - t]
    t = turn_for_sides(12); out += [t, 180 - t]
    n = sides_for_turn(18); out += [n, 180 - 18]
    t = 180 - 172; out += [sides_for_turn(t), t]
    rows = ITEM['L6U07-S01']['figure']['rows']
    assert rows[0][0] == '5' and rows[1][0] == '12' and rows[2][1] == '18°' and rows[3][2] == '172°'
    return s(out)


@check('L6U07-S02')
def _():
    progs = {'A': (10, 36), 'B': (12, 30), 'C': (6, 30)}
    good = [k for k, (n, a) in progs.items() if 180 - a == 150 and n * a == 360]
    assert good == ['B']
    n, a = progs['C']
    return {'a': good, 'b': [n * a, 'closes' if (n * a) % 360 == 0 else 'does not close']}


@check('L6U07-S03')
def _():
    st = turtle(prog_of('L6U07-S03'))
    return {'a': [round(st['turned']) % 360], 'b': ['Yes' if round(st['turned']) % 360 == 0 else 'No']}


@check('L6U07-S04')
def _():
    turns = [60, 85, 110, 50]
    last = 360 - sum(turns)
    inside = [180 - t for t in turns + [last]]
    return {'a': [last], 'b': [180 - last], 'c': [sum(inside)]}


@check('L6U07-S05')
def _():
    t = turn_for_sides(18)
    return {'a': [t], 'b': [180 - t], 'c': [18 * (180 - t)]}


@check('L6U07-S06')
def _():
    n = 30
    t = turn_for_sides(n)
    st = turtle([['ctl', f'repeat ({n})', [['move', 'move (30) steps'], ['turn', f'turn ↻ ({t}) degrees']]]])
    assert abs(st['x']) < 1e-6 and abs(st['y']) < 1e-6 and round(st['turned']) == 360        # the shape closes after one full turn
    return {'a': [n], 'b': [t], 'c': [180 - t]}


@check('L6U07-S07')
def _():
    cells = [int(c.replace('°', '')) for c in ITEM['L6U07-S07']['figure']['rows'][0]]
    return s([a for a in cells if sides_for_turn(a) and sides_for_turn(a) >= 3])


@check('L6U07-S08')
def _():
    n, rounds = 10, 3
    t = [t for t in range(1, 361) if n * t == rounds * 360][0]
    st = turtle([['ctl', f'repeat ({n})', [['move', 'move (80) steps'], ['turn', f'turn ↻ ({t}) degrees']]]])
    assert abs(st['x']) < 1e-6 and abs(st['y']) < 1e-6        # the star closes
    return {'a': [round(st['turned'])], 'b': [t], 'c': [180 - t]}


@check('L6U07-S09')
def _():
    prog = prog_of('L6U07-S09')
    st = turtle(prog)
    assert abs(st['x']) < 1e-6 and abs(st['y']) < 1e-6       # it is a closed rectangle
    inner = prog[0][2]
    prog80 = [['ctl', prog[0][1], [inner[0], inner[1], ['move', 'move (80) steps'], inner[3]]]]
    st80 = turtle(prog80)
    return {'a': [round(st['turned'])], 'b': [round(st['dist'])], 'c': [round(st80['dist'])]}


@check('L6U07-S10')
def _():
    inside = lambda sides: 180 - turn_for_sides(sides)
    tri, sq, hexa = inside(3), inside(4), inside(6)
    gap = 6 * tri == 360, 3 * sq < 360
    return {'a': [6 * tri], 'b': [3 * sq, 'Yes' if 3 * sq != 360 else 'No'], 'c': [2 * hexa + 2 * tri]}


@check('L6U07-S11')
def _():
    def sides(k):
        for n in range(3, 400):
            if 360 % n == 0:
                turn = 360 // n
                if 180 - turn == k * turn:
                    return n
    return {'a': [sides(2)], 'b': [sides(5)], 'c': [sides(8)]}


@check('L6U07-T01')
def _():
    k = 1
    while (100 * k) % 360 != 0:
        k += 1
    return {'a': [100 * k], 'b': [100 * k // 360], 'c': [k]}


@check('L6U07-T02')
def _():
    n = [n for n in range(3, 100) if (n - 2) * 180 == 2340][0]
    inside = 2340 // n
    return {'a': [n], 'b': [inside], 'c': [180 - inside]}


@check('L6U07-T03')
def _():
    left = 360 - 60 - 90 - 90
    sides = [n for n in range(3, 400) if 360 % n == 0 and 180 - 360 // n == left]
    assert len(sides) == 1
    return {'a': [left], 'b': sides}


@check('L6U07-G01')
def _():
    prog = prog_of('L6U07-G01')
    out = {}
    for lab, reps in (('a', 4), ('b', 12)):
        p = [prog[0], ['ctl', f'repeat ({reps})', prog[1][2]]]
        st = turtle(p)
        out[lab] = [round(st['x']), round(st['y'])]
    return out


@check('L6U07-G02')
def _():
    def point(n, rounds):
        turn = rounds * 360 // n
        assert n * turn == rounds * 360
        return 180 - turn
    return {'a': [5 * point(5, 2)], 'b': [8 * point(8, 3)], 'c': [point(10, 3), 10 * point(10, 3)]}


@check('L6U07-G03')
def _():
    st = turtle([['ctl', 'repeat (360)', [['move', 'move (1) steps'], ['turn', 'turn ↻ (1) degrees']]]])
    assert abs(st['x']) < 1e-6 and abs(st['y']) < 1e-6        # it closes: one full turn
    return {'a': [round(st['dist'])], 'b': [round(st['dist'] / 3.14)]}


@check('L6U07-C01')
def _():
    t = turn_for_sides(40)
    return s([t, 180 - t])


@check('L6U07-C02')
def _():
    return s([sides_for_turn(45)])


@check('L6U07-C03')
def _():
    t = 180 - 156
    return s([sides_for_turn(t)])


@check('L6U07-C04')
def _():
    return s([360 - (95 + 80 + 105)])
