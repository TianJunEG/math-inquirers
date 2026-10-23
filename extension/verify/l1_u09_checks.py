"""Independent checks for Level 1 Unit 9 (Length): lengths are modelled as positions on a line; every answer is recomputed by
counting steps or brute force, never copied from the book."""
import itertools
from common import s

CHECKS = {}


def check(id_):
    def deco(f):
        CHECKS[id_] = f
        return f
    return deco


def count_spaces(start, end):
    """Hop from mark `start` to mark `end` one space at a time."""
    hops, m = 0, start
    while m < end:
        m += 1
        hops += 1
    return hops


def end_mark(start, length):
    m = start
    for _ in range(length):
        m += 1
    return m


def longer_by(a, b):
    """How many units must be added to the shorter to reach the longer."""
    short, long_ = min(a, b), max(a, b)
    n = 0
    while short + n < long_:
        n += 1
    return n


@check('L1U09-L01')
def _():
    return s([longer_by(11, 7)])


@check('L1U09-S01')
def _():
    strips = {'A': 5, 'B': 8, 'C': 3}
    return {'a': [max(strips, key=strips.get)], 'b': [min(strips, key=strips.get)], 'c': s([longer_by(strips['B'], strips['A'])])}


@check('L1U09-S02')
def _():
    return s([longer_by(13, 8)])


@check('L1U09-S03')
def _():
    return s(sorted([14, 9, 12, 6]))


@check('L1U09-S04')
def _():
    return s([15 - 6])


@check('L1U09-S05')
def _():
    # Mei: 4 cubes then a gap of 1 then 3 cubes; Ben: 7 touching cubes.
    mei_gaps = 1
    ben_gaps = 0
    fair = 'Ben' if ben_gaps == 0 and mei_gaps > 0 else 'Mei'
    return {'a': [fair], 'b': ['a gap' if mei_gaps else 'cubes overlap']}


@check('L1U09-S06')
def _():
    return s([8 + 5])


@check('L1U09-S07')
def _():
    return s([count_spaces(0, 7)])


@check('L1U09-S08')
def _():
    return s([count_spaces(4, 9)])


@check('L1U09-S09')
def _():
    return s([count_spaces(3, 12)])


@check('L1U09-S11')
def _():
    red, blue = count_spaces(1, 8), count_spaces(3, 9)
    return {'a': s([red]), 'b': s([blue]), 'c': ['red' if red > blue else 'blue']}


@check('L1U09-S10')
def _():
    return s([count_spaces(9, 15)])


@check('L1U09-S12')
def _():
    return s([end_mark(4, 6)])


@check('L1U09-S13')
def _():
    stick = 5
    cubes_for = lambda n: sum(stick for _ in range(n))
    sticks_for = lambda c: [n for n in range(0, 20) if cubes_for(n) == c][0]
    return {'a': s([cubes_for(3)]), 'b': s([sticks_for(20)]), 'c': s([cubes_for(2) + 3])}


@check('L1U09-S14')
def _():
    table = 24                     # any common length that both children measured (used only for the ratio)
    pencil_len, rubber_len = table / 6, table / 9
    return ['a pencil' if pencil_len > rubber_len else 'a rubber']


@check('L1U09-T01')
def _():
    ribbon, pieces = 24, 4
    each = [x for x in range(1, ribbon) if x * pieces == ribbon][0]
    cuts = pieces - 1
    # verify by listing the cut positions
    positions = [each * k for k in range(1, pieces)]
    assert len(positions) == cuts and all(0 < p < ribbon for p in positions)
    return {'a': s([each]), 'b': s([cuts])}


@check('L1U09-T02')
def _():
    clip = 2
    pen = 5 * clip
    bag = 2 * pen
    return {'a': s([pen]), 'b': s([bag])}


@check('L1U09-T03')
def _():
    ali = 10
    mei = ali - 4
    ben = mei + 3
    lens = {"Ali's": ali, "Mei's": mei, "Ben's": ben}
    return {'a': s([mei]), 'b': s([ben]), 'c': [max(lens, key=lens.get)]}


@check('L1U09-G01')
def _():
    posts = 6
    # draw the posts as a string and count the gaps between neighbours
    row = ['P'] * posts
    gaps = sum(1 for a, b in zip(row, row[1:]))
    fence_len = gaps * 3
    ten = ['P'] * 10
    gaps10 = sum(1 for a, b in zip(ten, ten[1:]))
    return {'a': s([gaps]), 'b': s([fence_len]), 'c': s([gaps10])}


@check('L1U09-G02')
def _():
    ali = 3 * 4 + 2
    mei = 14
    return {'a': s([ali]), 'b': ['They are the same' if ali == mei else ("Ali's" if ali > mei else "Mei's")]}


@check('L1U09-G03')
def _():
    sols = [(f, t) for f in range(0, 5) for t in range(0, 6) if 4 * f + 3 * t == 14]
    assert len(sols) == 1, sols
    f, t = sols[0]
    return s([f, t])


@check('L1U09-C01')
def _():
    return s([count_spaces(5, 13)])


@check('L1U09-C02')
def _():
    return s([longer_by(14, 9)])


@check('L1U09-C03')
def _():
    return s([sum(3 for _ in range(5))])


@check('L1U09-C04')
def _():
    t = {'A': 8}
    t['B'] = t['A'] + 3
    t['C'] = t['A'] - 2
    return {'a': [max(t, key=t.get)]}
