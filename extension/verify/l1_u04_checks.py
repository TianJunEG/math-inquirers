"""Independent checks for Level 1 Unit 4 (repeating and growing patterns): every pattern is generated place by place (no formula
for the nth term), and stick counts come from the drawn edges (figs_l1_u03_u04.count_sticks)."""
import os, sys
from common import s, EXT

sys.path.insert(0, os.path.join(EXT, 'tools'))
CHECKS = {}


def check(id_):
    def deco(f):
        CHECKS[id_] = f
        return f
    return deco


def rep(core, n):
    """First n places of a repeating pattern, written out one by one."""
    out = []
    while len(out) < n:
        out.extend(core)
    return out[:n]


def grow(first, step, n):
    out, v = [], first
    for _ in range(n):
        out.append(v); v += step
    return out


def sticks(n):
    import figs_l1_u03_u04 as f
    return f.count_sticks('tri', n)


@check('L1U04-L01')
def _():
    return [rep(['circle', 'square', 'triangle', 'star'], 10)[9]]


@check('L1U04-S01')
def _():
    return [rep(['triangle', 'circle'], 7)[6]]


@check('L1U04-S02')
def _():
    return [rep(['star', 'heart', 'heart'], 9)[8]]


@check('L1U04-S03')
def _():
    return [rep(['dark', 'dark', 'white'], 12)[11]]


@check('L1U04-S04')
def _():
    seq = rep(['M', 'N', 'O'], 9)
    assert seq[:7] == ['M', 'N', 'O', 'M', 'N', 'O', 'M']
    return seq[7:9]


@check('L1U04-S05')
def _():
    return [rep(['clap', 'clap', 'stomp'], 10)[9]]


@check('L1U04-S06')
def _():
    return [rep(['square', 'star', 'star', 'circle'], 16)[15]]


@check('L1U04-S07')
def _():
    seq = rep(['triangle', 'circle', 'square'], 13)
    return {'a': [seq[8]], 'b': [seq[11]], 'c': [seq[12]]}


@check('L1U04-S08')
def _():
    seq = rep(['triangle', 'circle', 'square'], 20)
    places = [i + 1 for i, v in enumerate(seq) if v == 'circle']
    assert places[:3] == [2, 5, 8]
    return s(places[3:6])


@check('L1U04-S09')
def _():
    seq = rep(list('abcd'), 13)
    tf = lambda b: ['True' if b else 'False']
    return {'a': tf(seq[7] == seq[3]), 'b': tf(seq[9] == seq[3]), 'c': tf(seq[12] == seq[0])}


@check('L1U04-S10')
def _():
    return s([sum(1 for v in rep(['star', 'circle', 'circle'], 12) if v == 'circle')])


@check('L1U04-S11')
def _():
    t = grow(3, 2, 12)
    return {'a': s([t[4]]), 'b': s([t.index(15) + 1])}


@check('L1U04-S12')
def _():
    t = grow(2, 3, 12)
    assert t[:3] == [2, 5, 8]
    return {'a': s([t[3]]), 'b': s([t[5]]), 'c': s([t.index(23) + 1])}


@check('L1U04-S13')
def _():
    return {'a': s([sticks(2)]), 'b': s([sticks(3)]), 'c': s([sticks(4)])}


@check('L1U04-T01')
def _():
    seq = rep(['heart', 'star', 'star'], 30)
    stars = [i + 1 for i, v in enumerate(seq) if v == 'star']
    return {'a': [seq[14]], 'b': s([sum(1 for v in seq[:18] if v == 'star')]), 'c': s([stars[4]])}


@check('L1U04-T02')
def _():
    n = 0
    while sticks(n + 1) <= 24:
        n += 1
    return {'a': s([n]), 'b': s([24 - sticks(n)])}


@check('L1U04-T03')
def _():
    t = grow(5, 3, 20)
    return {'a': s([t[5]]), 'b': s([t.index(32) + 1])}


@check('L1U04-G01')
def _():
    t, v, j = [1], 1, 1
    while len(t) < 10:
        v += j; t.append(v); j += 1
    assert t[:5] == [1, 2, 4, 7, 11]
    return {'a': s(t[5:7]), 'b': s([t[7]])}


@check('L1U04-G02')
def _():
    import figs_l1_u03_u04 as f
    ravi, mei = f.count_sticks('tri_sep', 7), sticks(7)
    return {'a': s([ravi]), 'b': s([mei]), 'c': s([ravi - mei])}


@check('L1U04-G03')
def _():
    top, bottom = rep(['circle', 'star'], 24), rep(['A', 'B', 'C'], 24)
    places = [i + 1 for i in range(24) if top[i] == 'star' and bottom[i] == 'C']
    return {'a': s([places[0]]), 'b': s([places[1]])}


@check('L1U04-C01')
def _():
    return [rep(['sun', 'moon', 'moon'], 9)[8]]


@check('L1U04-C02')
def _():
    return [rep(list('PQRS'), 18)[17]]


@check('L1U04-C03')
def _():
    return s([grow(3, 4, 5)[4]])


@check('L1U04-C04')
def _():
    return s([sticks(6)])
