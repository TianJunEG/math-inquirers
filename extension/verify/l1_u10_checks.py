"""Independent checks for Level 1 Unit 10 (Puzzle day, mixed): each answer is found by simulation or brute force over the puzzle's own rules."""
import itertools
from common import s

CHECKS = {}


def check(id_):
    def deco(f):
        CHECKS[id_] = f
        return f
    return deco


def run_rule(start, step, n):
    out, v = [], start
    for _ in range(n):
        out.append(v)
        v += step
    return out


def undo(result, steps):
    """steps: list of (op, k) applied in order to the secret number; find the secret number by trying 0..100 (forward simulation)."""
    sols = []
    for x in range(101):
        v = x
        for op, k in steps:
            v = v + k if op == '+' else v - k
        if v == result:
            sols.append(x)
    assert len(sols) == 1
    return sols[0]


def coin_sets(total, k, coins=(5, 10, 20, 50)):
    return sorted(set(tuple(sorted(c, reverse=True)) for c in itertools.combinations_with_replacement(coins, k) if sum(c) == total))


@check('L1U10-L01')
def _():
    return s(run_rule(5, 2, 5)[1:])   # a plant 5 cm tall, +2 each week: the 4 tiles after the start

@check('L1U10-S01')
def _():
    seq = run_rule(7, 5, 5)
    assert seq[0] == 7 and seq[1] == 12 and seq[2] == 17 and seq[4] == 27
    return s([seq[3]])


@check('L1U10-S02')
def _():
    seq = run_rule(3, 4, 5)
    assert seq[1] == 7 and seq[3] == 15
    return s([seq[2], seq[4]])


@check('L1U10-S03')
def _():
    return s([x for x in range(21) if 13 + x == 20] + [x for x in range(11) if x + 6 == 10])


@check('L1U10-S04')
def _():
    return {'a': s([x for x in range(30) if 7 + 6 == 8 + x]), 'b': s([x for x in range(30) if 9 + 5 == 7 + x])}


@check('L1U10-S10')
def _():
    w = coin_sets(40, 3)
    assert len(w) == 1
    return s(w[0])


@check('L1U10-S05')
def _():
    return s([x for x in range(71) if 45 + x == 70])


@check('L1U10-S06')
def _():
    g = {'Monday': 6, 'Tuesday': 9, 'Wednesday': 4, 'Thursday': 7}
    return {'a': s([[x for x in range(20) if g['Wednesday'] + x == g['Tuesday']][0]]), 'b': s([g['Monday'] + g['Thursday']])}


@check('L1U10-S07')
def _():
    sides = {'triangle': 3, 'square': 4}
    return s([sum(sides[x] for x in ['triangle', 'square', 'triangle'])])


@check('L1U10-S08')
def _():
    names = ['Lily', 'Ray', 'Jamie', 'Amelia']
    older = [('Lily', 'Ray'), ('Ray', 'Jamie'), ('Amelia', 'Lily')]    # (older, younger)
    sols = [p for p in itertools.permutations(names) if all(p.index(a) < p.index(b) for a, b in older)]
    assert len(sols) == 1
    return list(sols[0])


@check('L1U10-S09')
def _():
    return s([n for n in (13, 16, 18, 21, 24) if n % 2 == 0])


@check('L1U10-S11')
def _():
    return s([undo(15, [('+', 7)])])


@check('L1U10-S12')
def _():
    return s([undo(14, [('-', 3), ('+', 8)])])


@check('L1U10-S13')
def _():
    return s([x for x in range(40) if x + 5 == 13])


@check('L1U10-S14')
def _():
    start, end = 2, 11
    return s([len(range(start, end))])


@check('L1U10-T01')
def _():
    saves, total, tot = [], 0, []
    for d in range(1, 5):
        saves.append(5 * d)
        total += 5 * d
        tot.append(total)
    return {'a': s([saves[3]]), 'b': s([tot[3]])}


@check('L1U10-T02')
def _():
    sides = {'square': 4, 'triangle': 3}
    n = sides['square'] + 2 * sides['triangle']
    cost = 0
    for _ in range(n):      # one 5c sticker for each side
        cost += 5
    return {'a': s([n]), 'b': s([cost])}

@check('L1U10-T03')
def _():
    return s([undo(11, [('-', 4), ('-', 3), ('+', 2)])])


@check('L1U10-G01')
def _():
    parts, seq = 1, {}
    for f in range(1, 7):
        parts *= 2
        seq[f] = parts
    return {'a': s([seq[3]]), 'b': s([seq[5]]), 'c': s([[f for f in seq if seq[f] == 16][0]])}


@check('L1U10-G02')
def _():
    sols = [(a, a + 4, a + 4 - 2) for a in range(1, 24) if a + (a + 4) + (a + 4 - 2) == 24]
    assert len(sols) == 1
    a, b, m = sols[0]
    return {'a': s([a]), 'b': s([b]), 'c': s([m])}


@check('L1U10-G03')
def _():
    sols = [(3 * 3, 17 - 9, q) for q in range(0, 10) if 3 * 3 + 4 * q == 17]
    assert len(sols) == 1
    tri, rest, q = sols[0]
    return {'a': s([tri]), 'b': s([rest]), 'c': s([q])}


@check('L1U10-C01')
def _():
    return s(run_rule(8, 5, 6)[4:])


@check('L1U10-C02')
def _():
    return s([x for x in range(21) if 8 + x == 20])


@check('L1U10-C03')
def _():
    return s([x for x in range(51) if 35 + x == 50])


@check('L1U10-C04')
def _():
    names = ['Wei', 'Siti', 'Ben']
    taller = [('Wei', 'Siti'), ('Siti', 'Ben')]
    sols = [p for p in itertools.permutations(names) if all(p.index(a) < p.index(b) for a, b in taller)]
    return [sols[0][0]]
