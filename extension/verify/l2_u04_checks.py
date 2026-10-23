"""Independent checks for Level 2 Unit 4 (patterns): patterns are generated place by place and counted; tables are built step by step."""
import itertools
from common import s

CHECKS = {}


def check(i):
    def d(f):
        CHECKS['L2U04-' + i] = f
        return f
    return d


def place(group, n):
    """The shape in place n (1-based) of a repeating pattern: built place by place, no formula."""
    seq = []
    while len(seq) < n:
        seq.extend(group)
    return seq[n - 1]


def count_in(group, k, what):
    return sum(1 for i in range(1, k + 1) if place(group, i) == what)


def steps(start, add, n):
    out, v = [], start
    for _ in range(n):
        out.append(v)
        v += add
    return out


@check('L01')
def _():
    return [place(['star', 'square', 'square'], 14)]


@check('S01')
def _():
    return s(steps(4, 4, 6)[3:])


@check('S02')
def _():
    g = ['star', 'square', 'square', 'circle']
    return {'a': [place(g, 16)], 'b': [place(g, 22)], 'c': [place(g, 33)]}


@check('S03')
def _():
    g = list('CHESS')
    sixth_e = [i for i in range(1, 100) if place(g, i) == 'E'][5]
    return {'a': [place(g, 17)], 'b': s([sixth_e]), 'c': s([count_in(g, 30, 'S')])}


@check('S04')
def _():
    g = ['sq', 'c', 'c', 'c', 'c']
    # 8 squares: find the length of the string that has exactly 8 squares at the end of a group
    n = 0
    while count_in(g, n, 'sq') < 8 or n % 5:
        n += 1
    return {'a': s([count_in(g, n, 'c')]), 'b': s([n])}


@check('S05')
def _():
    sl = steps(4, 4, 10)
    return {'a': s(sl[1:6]), 'b': s([sl[9]]), 'c': s([x for x in range(1, 20) if 4 * x == 28]), 'd': s([14 // 4, 14 % 4])}


@check('S06')
def _():
    def sticks(n):                      # a chain of squares drawn stick by stick: 4 for the first, then 3 for each more
        return 4 + 3 * (n - 1)
    assert [sticks(1), sticks(2), sticks(3)] == [4, 7, 10]
    return {'a': s([sticks(4)]), 'b': s([sticks(6)]), 'c': s([sticks(8)])}


@check('S07')
def _():
    a = steps(7, 5, 6)
    b = steps(50, -6, 5)
    rule_a = {a[1] - a[0]}
    rule_b = {b[0] - b[1]}
    assert rule_a == {5} and rule_b == {6}
    return {'a': s(a[4:]) + ['add 5'], 'b': s(b[3:]) + ['subtract 6']}


@check('S08')
def _():
    siti = set(steps(3, 3, 14)) & set(range(1, 41))
    ravi = set(steps(5, 5, 8))
    both = sorted(x for x in siti & ravi if x <= 40)
    nxt = min(x for x in set(steps(3, 3, 30)) & set(steps(5, 5, 30)) if x > 40)
    return {'a': s(both), 'b': s([nxt])}


@check('S09')
def _():
    g = ['t', 'c', 'c']
    k = 24
    return {'a': s([k // len(g)]), 'b': s([count_in(g, k, 'c')]), 'c': s([count_in(g, k, 't')])}


@check('S10')
def _():
    t = steps(4, 2, 10)
    return {'a': s(t[3:6]), 'b': s([t[9]]), 'c': s([t.index(18) + 1])}


@check('T01')
def _():
    seq, v, add = [], 3, 2
    while v < 100:
        seq.append(v)
        v += add
        add = 4 if add == 2 else 2
    return {'a': ['Yes' if 41 in seq else 'No'], 'b': ['Yes' if 40 in seq else 'No']}


@check('T02')
def _():
    g = ['square', 'star', 'circle', 'circle', 'triangle']
    Y = lambda n: 'Yes' if place(g, n) == 'star' else 'No'
    return {'a': [Y(17)], 'b': [Y(22)], 'c': [Y(35)], 'd': [Y(47)]}


@check('T03')
def _():
    def sticks(n):                      # triangles in a chain: 3 sticks, then 2 more for each extra triangle
        return 3 + 2 * (n - 1)
    assert [sticks(1), sticks(2), sticks(3)] == [3, 5, 7]
    best = max(n for n in range(1, 60) if sticks(n) <= 40)
    return {'a': s([sticks(10)]), 'b': s([best]), 'c': s([40 - sticks(best)])}


@check('G01')
def _():
    sq = [n * n for n in range(1, 20)]
    return {'a': s([sq[5]]), 'b': s([x for x in sq if x > 25][:2]), 'c': s([sq[9]])}


@check('G02')
def _():
    A = set(steps(4, 4, 30))
    B = set(steps(1, 3, 40))
    both = sorted(x for x in A & B if x <= 30)
    nxt = min(x for x in A & B if x > 28)
    C = set(steps(2, 4, 60))
    ever = bool(A & C)
    return {'a': s(both), 'b': s([nxt]), 'c': ['Yes' if ever else 'No']}


@check('G03')
def _():
    g = ['star', 'circle', 'circle', 'square', 'square']
    ravi, siti = place(g, 40) == 'star', place(g, 40) == 'square'
    assert siti and not ravi
    return {'a': ['Siti'], 'b': [place(g, 43)]}


@check('G04')
def _():
    g = ['triangle', 'square', 'circle', 'circle']
    assert place(g, 30) == 'square' and place(g, 28) == 'circle'
    return ['open']


@check('C01')
def _():
    return [place(['star', 'circle', 'square'], 20)]


@check('C02')
def _():
    return s([sum([5] * 9)])


@check('C03')
def _():
    return s([len(set(steps(4, 4, 10)) & set(steps(5, 5, 8)))])


@check('C04')
def _():
    return s([steps(3, 4, 6)[5]])
