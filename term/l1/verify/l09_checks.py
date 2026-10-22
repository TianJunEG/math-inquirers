"""Independent answer checks for Lesson 9 (Draw and Measure).

Every answer in l09.json is recomputed here from first principles: a line is modelled as a start position and an end position
on a ruler (in millimetres); its length in whole centimetres is found by counting the 1 cm gaps it covers, and the nearest
centimetre is found by choosing the closest mark. Paths, ribbons and snails are simulated step by step.
run(d) returns the number of checks; any failure raises AssertionError.
"""
import itertools


def gaps(start_mark, end_mark):
    """Number of 1 cm gaps a line covers when it starts at start_mark and ends at end_mark (both whole-cm marks)."""
    return sum(1 for k in range(start_mark, end_mark))


def nearest_mark(position_mm):
    """The ruler mark (whole cm) closest to a position given in mm."""
    return min(range(0, 400), key=lambda m: (abs(m * 10 - position_mm), m))


def end_mark(start_mark, length_cm):
    pos = start_mark
    for _ in range(length_cm):
        pos += 1
    return pos


def path_length(pieces):
    total = 0
    for p in pieces:
        total += gaps(0, p)
    return total


def snail(start, forward_to, back_cm):
    pos, crawled = start, 0
    while pos < forward_to:
        pos += 1; crawled += 1
    for _ in range(back_cm):
        pos -= 1; crawled += 1
    return pos, crawled


def cut_places(strip_cm):
    """Marks strictly inside the strip (cuts at the two ends make no new piece)."""
    return [m for m in range(0, strip_cm + 1) if 0 < m < strip_cm]


# ---- oracles for the online-practice templates (brute force, independent of the template expressions)
ORACLES = {
    'c1': lambda e: gaps(0, e['n']),
    'c2': lambda e: gaps(e['b'], e['a']),
    'c4': lambda e: gaps(0, e['a']) + e['d'] * 1,
    'c5': lambda e: nearest_mark(e['m'] * 10 + 8),
    't1': lambda e: gaps(e['s'], e['e']),
    't2': lambda e: path_length([e['a'], e['b'], e['c']]),
    't3': lambda e: end_mark(e['s'], e['l']),
    'g1': lambda e: e['T'] - path_length([e['a'], e['a'] + e['d']]),
    'g2': lambda e: snail(e['s'], e['e'], e['b'])[1],
    'g3': lambda e: len(cut_places(e['n'])),
}
BASE_ENV = {'c1': dict(n=12), 'c2': dict(a=12, b=5), 'c4': dict(a=5, d=3), 'c5': dict(m=14), 't1': dict(s=2, e=9),
            't2': dict(a=5, b=3, c=4), 't3': dict(s=3, l=6), 'g1': dict(T=30, a=8, d=3), 'g2': dict(s=4, e=13, b=5), 'g3': dict(n=10)}


def run(d):
    n = 0

    def eq(a, b, msg=''):
        nonlocal n
        n += 1
        assert a == b, f'{msg}: got {a}, expected {b}'

    T = {q['id']: q for q in d['tiers']['start'] + d['tiers']['think'] + d['tiers']['go']}
    X = {q['id']: q for q in d['exit']}
    # the ruler model itself
    eq(gaps(0, 5), 5, 'five gaps from 0 to 5'); eq(len(range(0, 6)), 6, 'six marks 0..5 but five gaps')
    eq(nearest_mark(88), 9, 'between 8 and 9, closer to 9'); eq(nearest_mark(124), 12, 'between 12 and 13, closer to 12')
    # remember warm-up and mini-lesson examples
    eq(gaps(0, 8), 8, 'warm-up 0 to 8'); eq(gaps(0, 10), 10, 'warm-up 0 to 10'); eq(gaps(0, 6), 6, 'mini 0 to 6')
    eq(gaps(3, 8), 5, 'mini: 3 to 8 is 5 cm'); eq(gaps(2, 9), 7, 'mini your turn: 2 to 9 is 7 cm')
    eq(gaps(0, 5), 5, 'mini draw 5 cm ends at 5')
    # sneak-peek
    eq(d['sneak_peek']['val1'], gaps(0, 3), 'sneak q1: 3 cm line')
    eq(gaps(1, 9), 8, 'sneak q2: pencil from 1 to 9 is 8 cm'); eq(gaps(1, 9) == 9, False, 'sneak q2: Ali is wrong')
    # explore: Ravi starts before the 0 mark (ruler edge about 2 mm before 0): his line is longer than 8 cm
    eq((8 * 10 - (-2)) > 80, True, 'Ravi line longer than 8 cm')
    # Start here
    eq(T['S1']['val'], [0, end_mark(0, 7)], 'S1'); eq(gaps(0, end_mark(0, 7)), 7, 'S1 length')
    eq(T['S2']['val'], [gaps(0, 9), gaps(0, 9) - gaps(0, 4)], 'S2'); eq(gaps(4, 9), 5, 'S2 count on')
    eq(T['S3']['val'], 'open', 'S3 open')
    eq(T['S4']['val'], [gaps(0, 13), gaps(0, 9), gaps(9, 13)], 'S4'); eq(gaps(0, 13) - gaps(0, 9), 4, 'S4 difference')
    eq(T['S5']['val'], [gaps(0, 5) + 3], 'S5'); eq(end_mark(0, 5) + 3, 8, 'S5 end mark')
    eq(T['S6']['val'], ['no', gaps(0, 7)], 'S6'); eq(gaps(0, 7) == 8, False, 'S6 Mei is wrong'); eq(end_mark(0, 8), 8, 'S6 should end at 8')
    # S7: tip 14.x, closer to 15 (say 14.7 cm = 147 mm)
    eq(T['S7']['val'], [nearest_mark(147)], 'S7'); eq(nearest_mark(147), 15, 'S7 closer to 15')
    # Think harder
    eq(T['T1']['val'], [path_length([5, 3, 4])], 'T1'); eq(5 + 3 + 4, 12, 'T1 sum')
    eq(T['T2']['val'], [gaps(2, 9), end_mark(3, 6)], 'T2'); eq(gaps(2, 9) == 9, False, 'T2 not 9')
    eq(T['T3']['val'], [gaps(0, 13) - gaps(0, 5)], 'T3'); eq(gaps(5, 13), 8, 'T3 measured from the dot')
    eq(T['T4']['val'], [nearest_mark(164), nearest_mark(188), nearest_mark(188) - nearest_mark(164)], 'T4')
    eq(nearest_mark(164), 16, 'T4 Ali 16.4'); eq(nearest_mark(188), 19, 'T4 Mei 18.8')
    # Go further
    A_, B_ = 8, 8 + 3
    eq(T['G1']['val'], [30 - A_ - B_], 'G1'); eq(A_ + B_ + (30 - A_ - B_), 30, 'G1 pieces add to the ribbon')
    pos, crawled = snail(4, 13, 5)
    eq(T['G2']['val'], [pos, crawled], 'G2'); eq((pos, crawled), (8, 14), 'G2 simulated')
    eq(abs(pos - 4), 4, 'G2 only 4 cm from where it began')
    ex = (5, 7, 8)
    eq(sum(ex), 20, 'G3 example sums to 20'); eq(len(set(ex)), 3, 'G3 example distinct')
    triples = [t for t in itertools.combinations(range(1, 20), 3) if sum(t) == 20]
    eq((3, 8, 9) in triples and (4, 7, 9) in triples and ex in triples, True, 'G3 other examples')
    eq(len(triples) > 10, True, 'G3 has many answers (so it is open)'); eq(T['G3']['val'], 'open', 'G3 open')
    # Investigation: any start mark, same length (end = start + 6)
    for s_ in range(0, 10):
        eq(gaps(s_, end_mark(s_, 6)), 6, f'investigation start {s_}')
    eq([end_mark(s_, 6) for s_ in (2, 3, 5)], [8, 9, 11], 'investigation end marks')
    # Talk: 15 vs 16 of the same pencil: a tip at 15.5 cm is the halfway case that can round either way
    eq(nearest_mark(150) , 15, 'talk: 15.0 -> 15'); eq(nearest_mark(158), 16, 'talk: 15.8 -> 16')
    # Exit
    eq(X['E1']['val'], [0, end_mark(0, 6)], 'E1')
    eq(X['E2']['val'], [gaps(6, 15)], 'E2'); eq(gaps(0, 15) - gaps(0, 6), 9, 'E2 difference')
    eq(X['E3']['val'], [gaps(3, 10)], 'E3'); eq(gaps(3, 10) == 10, False, 'E3 not 10')
    # Home practice
    H = {h['id']: h for h in d['home_practice']}
    eq(H['H1']['val'], [0, end_mark(0, 8)], 'H1')
    eq(H['H2']['val'], gaps(11, 17), 'H2'); eq(gaps(0, 17) - 11, 6, 'H2 difference')
    eq(H['H3']['val'], 'open', 'H3')
    eq(H['H4']['val'], gaps(4, 15), 'H4'); eq(gaps(4, 15) == 15, False, 'H4 not 15')
    eq(H['H5']['val'], 'open', 'H5'); eq(sum((6, 8, 11)), 25, 'H5 example'); eq(len({6, 8, 11}), 3, 'H5 distinct')
    # Optional slide and spare-time menu
    eq(len(cut_places(10)), 9, 'optional: 10 cm strip has 9 cutting places'); eq(len(cut_places(20)), 19, 'optional: 20 cm strip has 19')
    eq([gaps(s_, 9) for s_ in (0, 2, 4)], [9, 7, 5], 'M1 lines ending at 9')
    eq(5 + 7 + 8 == 20, True, 'g4 example')
    # Break: big jump 10 cm, small hop 1 cm
    for num_, (j, h_) in {14: (1, 4), 23: (2, 3), 30: (3, 0), 8: (0, 8)}.items():
        eq(j * 10 + h_, num_, f'break {num_}')
    # Online practice authored answers
    O = {i['id']: i for i in d['online_practice']['items']}
    for k in ('c1', 'c2', 'c4', 'c5', 't1', 't2', 't3', 'g1', 'g2', 'g3'):
        eq(O[k]['answer'], ORACLES[k](BASE_ENV[k]), 'authored ' + k)
    eq(O['c3']['answer'], 'On the dot where the line starts', 'c3')
    eq(O['t4']['answer'], 'No, it is 7 cm long', 't4'); eq(gaps(2, 9), 7, 't4 value')
    eq([r for r in range(10, 100)] != [], True, 'sanity')
    # g1 and g2 variants: every piece positive and the rest of the ribbon is positive
    for a_, d_ in itertools.product([6, 7, 8, 9], [2, 3, 4, 5]):
        eq(30 - (a_ + a_ + d_) > 0, True, f'g1 positive {a_},{d_}')
    # c2 variants: the first line is always the longer one
    for a_, b_ in itertools.product([9, 11, 12, 13, 14, 15], [3, 4, 5, 6, 7, 8]):
        eq(a_ > b_, True, f'c2 order {a_},{b_}')
    # g2 variants: the snail never goes below 0
    for s_, e_, b_ in itertools.product([3, 4, 5], [12, 13, 14], [4, 5, 6]):
        eq(e_ - b_ >= 0, True, f'g2 stays on ruler {s_},{e_},{b_}')
    return n
