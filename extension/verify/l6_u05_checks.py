"""Independent checks for Level 6 Unit 5 (Every possible way).  Every count is made by listing every case with itertools or a small search (no counting formulas),
and the printed code is run by the l6_lib interpreter."""
import itertools
from common import load_unit
from l6_lib import run, s

CHECKS = {}
U = load_unit(6, 5)
ITEM = {i['id']: i for i in U['items']}


def check(id_):
    def deco(f):
        CHECKS[id_] = f
        return f
    return deco


def prog_of(id_):
    return ITEM[id_]['figure']['prog']


def routes(c0, r0, c1, r1, via=None):
    """list every route of right / up moves from (c0, r0) to (c1, r1) by depth first search; via = a node it must pass"""
    out = []

    def go(c, r, path):
        if (c, r) == (c1, r1):
            out.append(path)
            return
        if c < c1:
            go(c + 1, r, path + [(c + 1, r)])
        if r < r1:
            go(c, r + 1, path + [(c, r + 1)])
    go(c0, r0, [(c0, r0)])
    if via:
        out = [p for p in out if via in p]
    return out


@check('L6U05-L01')
def _():
    return s([len(list(itertools.product(range(4), range(6))))])


@check('L6U05-S01')
def _():
    frames, seats, bells = ['red', 'blue', 'green', 'grey', 'black'], range(3), range(2)
    n = len(list(itertools.product(frames, seats, bells)))
    n6 = len(list(itertools.product(frames + ['white'], seats, bells)))
    nj = len([x for x in itertools.product(frames, seats, bells) if x[0] == 'red'])
    return {'a': [n], 'b': [n6], 'c': [nj]}


@check('L6U05-S02')
def _():
    res = list(itertools.product('HT', range(1, 7)))
    return {'a': [len(res)], 'b': [len([r for r in res if r[0] == 'T' and r[1] > 4])], 'c': [len([r for r in res if r[0] == 'H' and r[1] % 2 == 0])]}


@check('L6U05-S03')
def _():
    games = lambda n: len(list(itertools.combinations(range(n), 2)))
    n66 = [n for n in range(2, 40) if games(n) == 66][0]
    assert games(4) == 6                    # the picture
    return {'a': [games(8)], 'b': [games(11)], 'c': [n66]}


@check('L6U05-S04')
def _():
    env, said = run(prog_of('L6U05-S04'))
    return {'a': [said.count('A')], 'b': [said.count('B')], 'c': [len(said)]}


@check('L6U05-S05')
def _():
    fig = ITEM['L6U05-S05']['figure']
    return {'a': [len(routes(0, 0, fig['cols'], fig['rows']))]}


@check('L6U05-S06')
def _():
    return {'a': [len(list(itertools.product('ABCD', repeat=3)))], 'b': [len(list(itertools.permutations('ABCD', 3)))],
            'c': [len([p for p in itertools.product('ABCD', repeat=3) if p[0] == 'A'])]}


@check('L6U05-S07')
def _():
    podium = list(itertools.permutations(range(5), 3))
    return {'a': [len(podium)], 'b': [len([p for p in podium if p[0] == 0])]}


@check('L6U05-S08')
def _():
    prog = prog_of('L6U05-S08')
    env, said = run(prog)
    inner4 = [prog[0], ['ctl', 'repeat (3)', [prog[1][2][0], ['ctl', 'repeat (4)', prog[1][2][1][2]], prog[1][2][2]]]]
    env4, said4 = run(inner4)
    return {'a': [said[2]], 'b': [len(said)], 'c': [len(said4)]}


@check('L6U05-S09')
def _():
    nums = [p for p in itertools.permutations([0, 1, 2, 3], 3) if p[0] != 0]
    return {'a': [len(nums)], 'b': [len([p for p in nums if p[2] % 2 == 1])]}


@check('L6U05-S10')
def _():
    def diagonals(n):
        pairs = list(itertools.combinations(range(n), 2))
        sides = [p for p in pairs if (p[1] - p[0]) % n in (1, n - 1)]
        return len(pairs), len(pairs) - len(sides)
    return {'a': [diagonals(8)[0]], 'b': [diagonals(8)[1]], 'c': [diagonals(10)[1]]}


@check('L6U05-S11')
def _():
    def rects(k):
        return len([(i, j) for i in range(k) for j in range(i + 1, k + 1)])       # a rectangle runs from cut i to cut j
    assert len(ITEM['L6U05-S11']['figure']['rows'][0]) == 5
    return {'a': [rects(5)], 'b': [rects(7)]}


@check('L6U05-T01')
def _():
    fig = ITEM['L6U05-T01']['figure']
    c, r = [int(x) for x in fig['mark'][0].split(',')]
    to_x = len(routes(0, 0, c, r))
    from_x = len(routes(c, r, fig['cols'], fig['rows']))
    through = len(routes(0, 0, fig['cols'], fig['rows'], via=(c, r)))
    return {'a': [to_x, from_x], 'b': [through]}


@check('L6U05-T02')
def _():
    nums = [int(''.join(map(str, p))) for p in itertools.permutations([1, 2, 3, 4])]
    return {'a': [len(nums)], 'b': [len([n for n in nums if n % 2 == 0])], 'c': [len([n for n in nums if n % 4 == 0])]}


@check('L6U05-T03')
def _():
    tri = lambda k: len(list(itertools.combinations(range(k), 2)))        # P with 2 of the k points
    assert len([p for p in ITEM['L6U05-T03']['figure']['groups'][0]['pts'] if p[2] != 'P']) == 5
    return {'a': [tri(4)], 'b': [tri(5)], 'c': [tri(8)]}


@check('L6U05-G01')
def _():
    codes = list(itertools.product(range(1, 6), repeat=3))
    return {'a': [len(codes)], 'b': [len([c for c in codes if 5 not in c])], 'c': [len([c for c in codes if 5 in c])]}


@check('L6U05-G02')
def _():
    prog = prog_of('L6U05-G02')
    env, said = run(prog)
    # count the pairs checked: add a counter to the inner repeat (the figure is: set count, set a, outer repeat, say count)
    assert prog[2][0] == 'ctl' and prog[3][0] == 'look'
    outer = prog[2]
    inner = outer[2][1]
    prog_pairs = [prog[0], prog[1], ['var', 'set pairs to (0)'], ['ctl', outer[1], [outer[2][0], ['ctl', inner[1], inner[2] + [['var', 'change pairs by (1)']]], outer[2][2]]], prog[3]]
    env_p, _ = run(prog_pairs)
    six = [prog[0], prog[1], ['ctl', 'repeat (6)', [outer[2][0], ['ctl', 'repeat (6)', inner[2]], outer[2][2]]], prog[3]]
    env6, said6 = run(six)
    return {'a': [env_p['pairs']], 'b': [said[0]], 'c': [said6[0]]}


@check('L6U05-G03')
def _():
    def ways(n):
        if n == 0:
            return 1
        return sum(ways(n - k) for k in (1, 2) if n - k >= 0)       # list every sequence of 1s and 2s that makes n
    return {'a': [ways(3)], 'b': [ways(4)], 'c': [ways(6)], 'd': [ways(8)]}


@check('L6U05-C01')
def _():
    return s([len(list(itertools.product(range(5), range(3))))])


@check('L6U05-C02')
def _():
    return s([len(list(itertools.permutations(range(5), 2)))])


@check('L6U05-C03')
def _():
    return s([len(list(itertools.permutations([2, 5, 8])))])


@check('L6U05-C04')
def _():
    return s([len(list(itertools.product('ABCDE', 'ABCDE', range(1, 5))))])
