"""Independent checks for Level 6 Unit 1 (Code the pattern).  Every answer is recomputed: sequences are generated term by term, matchstick patterns are counted
edge by edge, and the printed code blocks are run by the small interpreter in l6_lib (the program is read from the unit file, the answer is not)."""
from common import load_unit
from l6_lib import run, s, rule_str, fit_rule

CHECKS = {}
U = load_unit(6, 1)
ITEM = {i['id']: i for i in U['items']}


def check(id_):
    def deco(f):
        CHECKS[id_] = f
        return f
    return deco


def seq(first, diff, n):
    out, v = [], first
    for _ in range(n):
        out.append(v)
        v += diff
    return out


def term(first, diff, k):
    """the k-th term, found by stepping k-1 times"""
    return seq(first, diff, k)[-1]


def sticks_squares(cols, rows):
    """count distinct unit edges of a cols x rows block of unit squares"""
    edges = set()
    for c in range(cols):
        for r in range(rows):
            edges |= {('h', c, r), ('h', c, r + 1), ('v', c, r), ('v', c + 1, r)}
    return len(edges)


def sticks_stairs(k):
    edges = set()
    for c in range(k):
        for r in range(c + 1):
            edges |= {('h', c, r), ('h', c, r + 1), ('v', c, r), ('v', c + 1, r)}
    return len(edges)


def prog_of(id_):
    return ITEM[id_]['figure']['prog']


@check('L6U01-L01')
def _():
    a, b = fit_rule([(1, 3), (2, 10), (3, 17), (4, 24)])
    return [a, -b, term(3, 7, 100)]          # the rule is printed as a x n - b


@check('L6U01-S01')
def _():
    counts = [sticks_squares(k, 2) for k in range(1, 60)]     # pattern k = k columns of 2 squares
    a, b = fit_rule([(k, counts[k - 1]) for k in range(1, 8)])
    n92 = [k for k in range(1, 60) if counts[k - 1] == 92][0]
    return {'a': [counts[2], counts[3] - counts[2]], 'b': [a, b], 'c': [counts[39]], 'd': [n92]}


@check('L6U01-S02')
def _():
    out = []
    for first, diff in ((8, 6), (3, 5)):
        a, b = fit_rule([(k + 1, t) for k, t in enumerate(seq(first, diff, 6))])
        out += [diff, rule_str(a, b), term(first, diff, 100)]
    return s(out)


@check('L6U01-S03')
def _():
    terms = set(seq(7, 5, 200))
    k157 = seq(7, 5, 200).index(157) + 1
    return {'a': ['Yes' if 157 in terms else 'No', k157], 'b': ['Yes' if 205 in terms else 'No'], 'c': [term(7, 5, 60)]}


@check('L6U01-S04')
def _():
    env, said = run(prog_of('L6U01-S04'))      # 4 loops
    p50 = list(prog_of('L6U01-S04'))
    p50[2] = ['ctl', 'repeat (50)', p50[2][2]]
    env50, said50 = run(p50)
    return {'a': [said[-1]], 'b': [said50[-1]]}


@check('L6U01-S05')
def _():
    # the child fills set n to a, repeat r, change by d; the program must say the first 15 terms of 11, 18, 25, ...
    target = seq(11, 7, 15)
    prog = [['hat', 'when green flag clicked'], ['var', 'set n to (11)'], ['ctl', 'repeat (15)', [['look', 'say (n) for (1) seconds'], ['var', 'change n by (7)']]]]
    env, said = run(prog)
    assert said == target
    return {'a': [11], 'b': [15], 'c': [7], 'd': [said[-1]]}


@check('L6U01-S06')
def _():
    env, said = run(prog_of('L6U01-S06'))
    first_ok = seq(4, 5, 31)
    reps = [r for r in range(0, 60) if run([['var', 'set n to (4)'], ['ctl', f'repeat ({r})', [['var', 'change n by (5)']]], ['look', 'say (n)']])[1][0] == first_ok[29]][0]
    return {'a': [said[0]], 'b': [first_ok[29]], 'c': [reps]}


@check('L6U01-S07')
def _():
    money = seq(15, 7, 40)
    a, b = fit_rule([(d + 1, money[d]) for d in range(6)])
    day200 = [d + 1 for d, v in enumerate(money) if v > 200][0]
    return {'a': [money[3]], 'b': [a, b], 'c': [money[29]], 'd': [day200]}


@check('L6U01-S08')
def _():
    out = {}
    for lab, first, opts in (('a', (4, 9), ['4n + 1', '5n - 1', '5n + 4']), ('b', (10, 13), ['3n + 10', '10n + 3', '3n + 7']), ('c', (3, 11), ['8n + 3', '8n - 5', '3n + 8'])):
        good = []
        for o in opts:
            c, d = o.split('n')
            c = int(c); d = int(d.replace(' ', '') or 0)
            if (c * 1 + d, c * 2 + d) == first:
                good.append(o)
        assert len(good) == 1
        out[lab] = good
    return out


@check('L6U01-S09')
def _():
    # a loop starts on term 1; each repeat moves one term on
    def repeats(start, end):
        k, t = 0, start
        while t < end:
            t += 1
            k += 1
        return k
    return {'a': [repeats(1, 60)], 'b': [1 + 40], 'c': [repeats(8, 25)]}


@check('L6U01-S10')
def _():
    env, said = run(prog_of('L6U01-S10'))
    # c: find a, b with a n + b giving 5, 9, 13 for n = 1, 2, 3
    a, b = fit_rule([(1, 5), (2, 9), (3, 13)])
    return {'a': s(said[:3]), 'b': [said[-1]], 'c': [a, b]}


@check('L6U01-S11')
def _():
    t = seq(2, 6, 4)
    a, b = fit_rule([(k + 1, v) for k, v in enumerate(t)])
    return {'a': ['No' if (6 * 1 != t[0]) else 'Yes'], 'b': [6 * 1, t[0]], 'c': [a, -b]}


@check('L6U01-T01')
def _():
    t = seq(58, -5, 30)
    a, b = fit_rule([(k + 1, v) for k, v in enumerate(t[:5])])
    last_pos = max(k + 1 for k, v in enumerate(t) if v > 0)
    return {'a': [b], 'b': [t[9]], 'c': [last_pos]}


@check('L6U01-T02')
def _():
    seq6 = seq(6, 4, 60)
    fifth = seq6[4]
    env, said = run([['var', f'set n to ({fifth})'], ['ctl', 'repeat (16)', [['var', 'change n by (4)']]], ['look', 'say (n)']])
    end = said[0]
    pos = seq6.index(end) + 1
    reps = [r for r in range(0, 60) if 6 + 4 * r == end][0]
    assert ITEM['L6U01-T02']['figure']['prog'][1][1] == f'set n to ({fifth})'
    return {'a': [pos], 'b': [reps], 'c': [end]}


@check('L6U01-T03')
def _():
    # 4th term 23, 9th term 53: the rise is shared over the jumps in between
    jumps = 9 - 4
    diff = (53 - 23) // jumps
    assert diff * jumps == 53 - 23
    first = 23 - 3 * diff
    a, b = fit_rule([(4, 23), (9, 53)])
    return {'a': [jumps], 'b': [diff], 'c': [first], 'd': [a, -b]}


@check('L6U01-G01')
def _():
    c = [sticks_stairs(k) for k in range(1, 12)]
    return {'a': [c[1], c[2]], 'b': [c[3], c[4]], 'c': [c[9]]}


@check('L6U01-G02')
def _():
    said, odd, even = [], 3, 20
    for place in range(1, 41):
        if place % 2:
            said.append(odd); odd += 4
        else:
            said.append(even); even += 5
    assert said[:8] == [3, 20, 7, 25, 11, 30, 15, 35]
    return {'a': [said[2] - said[0], said[3] - said[1]], 'b': [said[14]], 'c': [said[19]]}


@check('L6U01-G03')
def _():
    env, said = run(prog_of('L6U01-G03'))
    return {'a': [said[0]], 'b': [env['t']]}


@check('L6U01-C01')
def _():
    t = seq(9, 6, 6)
    a, b = fit_rule([(k + 1, v) for k, v in enumerate(t)])
    return s([a, b, term(9, 6, 100)])


@check('L6U01-C02')
def _():
    return ['Yes' if 125 in seq(7, 5, 100) else 'No']


@check('L6U01-C03')
def _():
    env, said = run([['var', 'set n to (8)'], ['ctl', 'repeat (20)', [['var', 'change n by (6)']]]])
    n = env['n']
    return s([n, seq(8, 6, 60).index(n) + 1])


@check('L6U01-C04')
def _():
    env, said = run([['var', 'set n to (5)'], ['ctl', 'repeat (4)', [['var', 'change n by (3)'], ['look', 'say (n)']]]])
    return s([said[0]])
