"""Independent checks for Level 4 Unit 6 (angles and turns): turns are simulated step by step on the 8-point compass; clock angles are computed
from the positions of the hands; angles in drawings are read from the figure data in the unit file (and the printed labels are cross-checked)."""
import json
from common import load_unit
CHECKS = {}
DIRS = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
U = load_unit(4, 6)
ITEM = {i['id']: i for i in [U['learn']['try']] + U['items']}


def check(id_):
    def deco(f):
        CHECKS[id_] = f
        return f
    return deco


def s(xs):
    return [str(x) for x in xs]


def turn(direction, degrees, clockwise=True):
    k = DIRS.index(direction)
    for _ in range(abs(degrees) // 45):
        k = (k + (1 if clockwise else -1)) % 8
    return DIRS[k]


def clock_angle(h, m):
    hour = (h % 12) * 30 + m * 0.5
    minute = m * 6
    d = abs(hour - minute) % 360
    d = min(d, 360 - d)
    return int(d) if d == int(d) else d


@check('L4U06-L01')
def _():
    return [turn('NE', 135, True)]


@check('L4U06-S01')
def _():
    angs = ITEM['L4U06-S01']['figure']['angles']
    got = [abs(a['d2'] - a['d1']) for a in angs]
    assert [a['label'] for a in angs] == ['a', 'b', 'c']
    return dict(zip('abc', [[str(g)] for g in got]))


@check('L4U06-S02')
def _():
    f = ITEM['L4U06-S02']['figure']
    ang = f['angle']
    return {'a': s([ang]), 'b': ['smaller' if ang < 90 else 'greater']}


@check('L4U06-S03')
def _():
    f = ITEM['L4U06-S03']['figure']
    d = {r['label']: r['d'] for r in f['rays']}
    # cross-check the printed arc labels against the ray directions
    for a in f['arcs']:
        r1, r2 = f['rays'][a['i']]['d'], f['rays'][a['j']]['d']
        assert a['text'] == f'{r2 - r1}°', (a, r1, r2)
    n_rays = len(f['rays'])
    pairs = sum(1 for i in range(n_rays) for j in range(i + 1, n_rays))
    return {'a': s([d['C'] - d['A']]), 'b': s([d['D'] - d['B']]), 'c': s([d['D'] - d['A']]), 'd': s([pairs])}


@check('L4U06-S04')
def _():
    return {'a': [turn('W', 90, True)], 'b': [turn('SE', 180, True)], 'c': [turn('NE', 270, True)],
            'd': [next(d for d in DIRS if turn(d, 135, False) == 'S')]}


@check('L4U06-S05')
def _():
    f = ITEM['L4U06-S05']['figure']['clocks']
    assert [c['h'] for c in f] == [5, 8, 11] and all(c['m'] == 0 for c in f)
    return {'a': s([clock_angle(5, 0)]), 'b': s([clock_angle(8, 0)]), 'c': s([clock_angle(11, 0)])}


@check('L4U06-S06')
def _():
    steps_cw = next(n for n in range(1, 9) if turn('W', 45 * n, True) == 'NE')
    steps_acw = next(n for n in range(1, 9) if turn('W', 45 * n, False) == 'NE')
    return {'a': s([45 * min(steps_cw, steps_acw)]), 'b': ['clockwise' if steps_cw < steps_acw else 'anticlockwise']}


@check('L4U06-S07')
def _():
    figs = ITEM['L4U06-S07']['figure']['figs']
    a = [p['deg'] for p in figs[0]['parts'] if p['text'] == 'a'][0]
    b = [p['deg'] for p in figs[1]['parts'] if p['text'] == 'b'][0]
    # labels in the drawings: 37 and 19 + 28
    assert 37 + a == 90 and 19 + 28 + b == 90
    return {'a': s([90 - 37]), 'b': s([90 - 19 - 28])}


@check('L4U06-S08')
def _():
    d, total = 'E', 0
    for deg, cw in ((135, False), (90, True), (45, True)):
        d = turn(d, deg, cw)
        total += deg
    return {'a': [d], 'b': s([total])}


@check('L4U06-S09')
def _():
    sol = [(x, 5 * x) for x in range(1, 90) if x + 5 * x == 90]
    assert len(sol) == 1
    return {'a': s([sol[0][0]]), 'b': s([sol[0][1]])}


@check('L4U06-S10')
def _():
    return {k: s([next(m for m in range(1, 120) if m * 6 == deg)]) for k, deg in zip('abcd', (90, 180, 270, 60))}


@check('L4U06-T01')
def _():
    a = next(x for x in range(1, 180) if 47 + 85 + x == 180)
    b = next(x for x in range(1, 360) if 95 + 120 + 78 + x == 360)
    return {'a': s([a]), 'b': s([b])}


@check('L4U06-T02')
def _():
    return {'a': s([clock_angle(7, 30)]), 'b': s([clock_angle(1, 30)])}


@check('L4U06-T03')
def _():
    d, total = 'N', 0
    for deg, cw in ((90, True), (135, False), (225, True), (45, False)):
        d = turn(d, deg, cw)
        total += deg
    return {'a': [d], 'b': s([total])}


@check('L4U06-G01')
def _():
    sol = [a for a in range(1, 100) if a + (a + 10) + (a + 20) + (a + 30) == 180]
    assert len(sol) == 1
    return {'a': s(sol), 'b': s([sol[0] + 30])}


@check('L4U06-G02')
def _():
    d, n = 'N', 0
    while True:
        d = turn(turn(d, 90, True), 45, False)
        n += 1
        if d == 'N':
            break
    d21 = 'N'
    for _ in range(21):
        d21 = turn(turn(d21, 90, True), 45, False)
    return {'a': s([n]), 'b': [d21]}


@check('L4U06-G03')
def _():
    sol = [(x, 2 * x, 3 * x, 3 * x) for x in range(1, 361) if x + 2 * x + 3 * x + 3 * x == 360]
    assert len(sol) == 1
    return {'a': s([sol[0][0]]), 'b': s([sol[0][3]])}


@check('L4U06-G04')
def _():
    ts = [h for h in range(1, 13) if 100 < clock_angle(h, 0) < 160]
    return {'a': s([len(ts)]), 'b': s(ts)}


@check('L4U06-C01')
def _():
    return s([clock_angle(7, 0)])


@check('L4U06-C02')
def _():
    return [turn('S', 135, True)]


@check('L4U06-C03')
def _():
    return s([next(x for x in range(1, 90) if x + 41 == 90)])


@check('L4U06-C04')
def _():
    return s([(35 - 10) * 6])
