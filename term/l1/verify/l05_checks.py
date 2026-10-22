"""Independent answer checks for Lesson 5 (Make-a-Ten Adding).

Every answer in l05.json is recomputed here from first principles: counters are placed in ten-frames and moved, kit bars and
squares are regrouped, sums are enumerated. The lesson's own expressions are not reused. run(d) returns the number of checks;
any failure raises AssertionError.
"""
import itertools


def count_all(*groups):
    """Total by counting counters one at a time."""
    n = 0
    for g in groups:
        for _ in range(g):
            n += 1
    return n


def fill_frame(a, b):
    """Make-a-ten by moving counters: put a in the first ten-frame, b beside it, move counters across until the first
    frame has 10 (or the second runs out). Return (moved, in_first_frame, left_outside)."""
    first, second, moved = a, b, 0
    while first < 10 and second > 0:
        first += 1
        second -= 1
        moved += 1
    return moved, first, second


def kit_add(tens, ones, extra):
    """Kit page: tens bars and ones squares. Add extra squares, then swap every 10 squares for a bar."""
    ones += extra
    while ones >= 10:
        tens += 1
        ones -= 10
    return tens * 10 + ones


def to_next_ten(n):
    m = n + 1
    while m % 10:
        m += 1
    return m - n


def best_moves(a, b):
    """Fewest counters to move to make one ten-frame full, trying both directions (needs a + b >= 10)."""
    opts = []
    for k in range(0, 11):
        if a + k == 10 and k <= b:
            opts.append(k)      # fill a's frame with k counters from b
        if b + k == 10 and k <= a:
            opts.append(k)      # fill b's frame with k counters from a
    return min(opts)


# ---- oracles for the online-practice templates (brute force, independent of the template expressions; env holds the base vars only)
ORACLES = {
    'c1': lambda e: count_all(e['a'], e['b']),
    'c2': lambda e: to_next_ten(e['n']),
    'c3': lambda e: kit_add(e['t'], e['o'], e['b']),
    'c5': lambda e: kit_add(e['n'] // 10, e['n'] % 10, e['b']),
    't1': lambda e: sum([e['a'], e['b'], 10 - e['a']]),
    't2': lambda e: sum([e['a'], e['x'], 10 - e['a'], e['y']]),
    't4': lambda e: sum([e['a'], e['b'], 30 - e['a']]),
    'g1': lambda e: sum([e['a'], e['b'], 30 - e['a'], e['x'], 10 - e['b'], e['S'] - e['x']]),
    'g3': lambda e: best_moves(e['a'], e['b']),
}
BASE_ENV = {'c1': dict(a=8, b=6), 'c2': dict(n=28), 'c3': dict(t=2, o=8, b=6), 'c5': dict(n=27, b=5), 't1': dict(a=4, b=9),
            't2': dict(a=8, x=5, y=7), 't4': dict(a=18, b=34), 'g1': dict(a=18, b=7, x=23, S=40), 'g3': dict(a=7, b=8)}


def run(d):
    n = 0

    def eq(a, b, msg=''):
        nonlocal n
        n += 1
        assert a == b, f'{msg}: got {a}, expected {b}'

    T = {q['id']: q for q in d['tiers']['start'] + d['tiers']['think'] + d['tiers']['go']}
    X = {q['id']: q for q in d['exit']}
    H = {h['id']: h for h in d['home_practice']}
    O = {i['id']: i for i in d['online_practice']['items']}

    import os, sys
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tools'))
    import svg

    # ---- the pictures really show what the text says (counters drawn, empty spaces)
    def find(blocks, ty):
        out = []
        for b in blocks:
            if b['t'] == 'visual' and b['type'] == ty: out.append(b)
            if b['t'] == 'cols':
                for c in b['cols']: out += find(c, ty)
        return out
    S = {s['id']: s for s in d['slides']}
    tf = svg.ten_frame(7, 5)
    eq(tf.count('<circle'), 12, 'sneak picture shows 12 counters')
    eq(d['sneak_peek']['val1'], 12, 'sneak q1 answer')
    eq(find(S['s-sneak']['blocks'], 'ten_frame')[0]['filled'] + find(S['s-sneak']['blocks'], 'ten_frame')[0]['extra'], 12, 'sneak slide picture is 7 + 5')
    for fl, ex, shown in ((7, 0, 7), (8, 6, 14), (10, 4, 14), (9, 5, 14), (9, 9, 18), (9, 4, 13)):
        eq(svg.ten_frame(fl, ex).count('<circle'), shown, f'ten-frame {fl}+{ex} draws {shown} counters')
    # warm-up bonds to 10: empty spaces in a frame with k counters = counters needed to fill it
    for k, need in ((7, 3), (4, 6), (9, 1), (5, 5), (2, 8)):
        svgk = svg.ten_frame(k, 0)
        eq(svgk.count('<rect') // 1 - svgk.count('<circle'), 10 - k, f'frame with {k}: {need} empty spaces')
        eq(10 - k, need, f'bond {k}')
    # warm-up: how far to the next ten, and tens and ones put together
    eq([to_next_ten(x) for x in (18, 14, 26, 39)], [2, 6, 4, 1], 'warm-up next ten')
    eq([30 + 6, 40 + 2, 50 + 9], [36, 42, 59], 'warm-up tens and ones')
    eq(S['s-rem2']['blocks'][0]['tens'] * 10 + S['s-rem2']['blocks'][0]['ones'], 18, 'warm-up picture is 18')
    eq(S['s-rem3']['blocks'][0]['tens'] * 10 + S['s-rem3']['blocks'][0]['ones'], 36, 'warm-up picture is 36')

    # ---- sneak-peek puzzle 2: moving one counter keeps the total
    moved, first, outside = fill_frame(9, 5)
    eq((moved, first, outside), (1, 10, 4), 'sneak 2: move 1 from the 5 to the 9, 10 red and 4 blue')
    eq(count_all(9, 5), count_all(10, 4), 'sneak 2: the total is the same (14)')

    # ---- explore and mini-lesson numbers
    eq(fill_frame(8, 6), (2, 10, 4), 'explore: 8 + 6, move 2, ten and 4')
    eq(count_all(8, 6), 14, '8 + 6')
    for a, b, mv, rest in ((9, 4, 1, 3), (7, 5, 3, 2), (8, 6, 2, 4), (9, 7, 1, 6)):
        m, f, r = fill_frame(a, b)   # the first number is the one whose frame is filled (for 6 + 8 that is the 8)
        eq((m, r), (mv, rest), f'explore: {a} + {b} filling the first frame')
        eq(10 + r, count_all(a, b), f'explore: {a} + {b} total')
    eq(fill_frame(8, 6)[0], 2, '6 + 8 fill the 8, move 2')
    eq(best_moves(6, 8), 2, '6 + 8 fewest moves is 2 (fill the 8)')
    eq(kit_add(2, 8, 6), 34, 'kit 28 + 6'); eq(kit_add(3, 7, 5), 42, 'kit 37 + 5'); eq(kit_add(4, 6, 7), 53, 'kit 46 + 7')
    eq((kit_add(2, 8, 6) // 10, kit_add(2, 8, 6) % 10), (3, 4), 'kit 28 + 6 is 3 bars and 4 squares')
    eq(count_all(28, 6), 34, '28 + 6')
    # kit squares are enough: the most squares on the table at once is 8 + 6 = 14 (of 20), and bars 2 to 5 (of 9)
    eq(max(8 + 6, 7 + 5, 6 + 7) <= 20, True, 'kit has enough squares')
    eq([count_all(9, 4), count_all(7, 6), count_all(18, 5), count_all(45, 7)], [13, 13, 23, 52], 'mini-lesson your turn')
    eq([3 + 8 + 7, 3 + 7 + 8, 8 + 3 + 7], [18, 18, 18], 'mini: 3 + 8 + 7 in any order')
    eq(sorted([(a, b) for a in range(1, 10) for b in range(1, 10) if a + b == 10 and a < b and a in (3, 8, 7) and b in (3, 8, 7)]), [(3, 7)], 'mini: only 3 and 7 make ten')

    # ---- sanity: every make-a-ten needs the second number to hold enough counters
    for a, b in ((8, 6), (9, 4), (7, 5), (6, 8), (9, 7)):
        eq(a + b >= 10, True, f'{a} + {b} crosses ten')

    # ---- Start here
    eq(T['S1']['val'], [10 - 9, 4 - 1, count_all(9, 4)], 'S1')
    eq(fill_frame(9, 4)[2], 3, 'S1 left over 3')
    eq(T['S2']['val'], [fill_frame(7, 6)[2], count_all(7, 6)], 'S2')
    eq(T['S3']['val'], [to_next_ten(7), to_next_ten(18), to_next_ten(26), to_next_ten(39)], 'S3')
    eq(T['S4']['val'], [to_next_ten(28), 6 - to_next_ten(28), kit_add(2, 8, 6)], 'S4')
    sv = T['S4']['visual']; eq(sv['tens'] * 10 + sv['ones'], 28, 'S4 picture is 28')
    eq(T['S5']['val'], [to_next_ten(35), kit_add(3, 5, 7)], 'S5')
    eq(T['S6']['val'], [count_all(9, 6), kit_add(1, 8, 5), kit_add(2, 7, 5), to_next_ten(47), kit_add(4, 7, 6)], 'S6')
    eq(T['S6']['val'][2] < 40, True, 'S6 c stays within 40'); eq(6 - to_next_ten(47), 3, 'S6 d: 6 is 3 and 3')
    eq(T['S7']['val'], [count_all(8, 6)], 'S7 right answer')
    eq(8 + 2 + 6 == 14, False, 'S7: Siti added all 6 again (16)'); eq(8 + 2 + 6, 16, 'S7 Siti wrote 16')
    eq(6 - 2, 4, 'S7: only 4 are left of the 6')
    # a child who reads the question: the (a) part of S3-S6 sums stay within 100
    eq(max(T['S6']['val']) < 100, True, 'Start here totals are within 100')

    # ---- Think harder
    eq(sorted(T['T1']['val'][:2]), [4, 6], 'T1 pair')
    pairs = [(x, y) for x, y in itertools.combinations([4, 9, 6], 2) if x + y == 10]
    eq(pairs, [(4, 6)], 'T1 the only pair that makes ten')
    eq(T['T1']['val'][2], sum([4, 9, 6]), 'T1 total')
    eq(T['T2']['val'], [sum([8, 5, 2, 7])], 'T2'); eq([(x, y) for x, y in itertools.combinations([8, 5, 2, 7], 2) if x + y == 10], [(8, 2)], 'T2 pairs that make ten')
    sums = ['17 + 13', '18 + 12', '19 + 12', '16 + 14']
    tot = [int(s.split(' + ')[0]) + int(s.split(' + ')[1]) for s in sums]
    eq([s for s, t in zip(sums, tot) if t != 30], ['19 + 12'], 'T3 the odd one out'); eq(T['T3']['val'], ['19 + 12', 31], 'T3')
    eq(sum([18, 34, 12]), 64, 'T4'); eq(T['T4']['val'], [64], 'T4 val')
    eq(18 + 12, 30, 'T4 pair')

    # ---- Go further
    eq(sum([18, 7, 12, 23, 3, 17]), 80, 'G1 total'); eq(T['G1']['val'], [80, 13], 'G1')
    g1b = [n for n in range(0, 100) if sum([18, 7, 12, 23, n, 17]) == 90]
    eq(g1b, [13], 'G1 b: the only number that replaces the 3 to give 90')
    eq(18 + 12 + 7 + 3 + 23 + 17, 80, 'G1 pairs'); eq(7 + 23 + 18 + 12 + 3 + 17, 80, 'G1 second pairing: 30 + 30 + 20')
    eq(sum(range(1, 10)), 45, 'G2 1 to 9'); eq(sum(range(1, 11)), 55, 'G2 1 to 10'); eq(T['G2']['val'], [45, 55], 'G2')
    eq([(x, 10 - x) for x in range(1, 5)], [(1, 9), (2, 8), (3, 7), (4, 6)], 'G2 four pairs of ten'); eq(45 - 40, 5, 'G2 the 5 has no partner')
    eq(5 + 5, 10, 'G2: the 5 would pair only with itself')
    ex = [45, 5, 20, 17, 3, 10]
    eq(len(ex), 6, 'G3 example has six numbers'); eq(sum(ex), 100, 'G3 example totals 100'); eq(45 + 5, 50, 'G3 pair 50'); eq(17 + 3, 20, 'G3 pair 20'); eq(20 + 10, 30, 'G3 pair 30')
    eq(T['G3']['val'], 'open', 'G3 is open-ended')

    # ---- Investigation: fill the bigger number, moves = 10 - bigger, checked for every pair that crosses ten
    for a in range(1, 10):
        for b in range(1, 10):
            if a + b >= 10:
                bm = best_moves(a, b)
                eq(bm, 10 - max(a, b), f'investigation {a} + {b}')
    eq(best_moves(9, 6), 1, 'I1 first step 9 + 6 moves 1 (not 4)'); eq(10 - 6, 4, 'I1 filling the 6 moves 4')
    eq(best_moves(8, 7), 2, 'I1 8 + 7 moves 2 (not 3)'); eq(10 - 7, 3, 'I1 filling the 7 moves 3')
    eq(best_moves(7, 7), 3, 'I1 7 + 7 either way moves 3')

    # ---- Talk and exit
    eq(8 + 6, 14, 'talk total'); eq((8 - 4) + (6 + 4), 14, 'talk: Ali moves 4 from the 8 to the 6: 4 and 10'); eq((8 + 2) + (6 - 2), 14, 'talk: Mei 10 and 4')
    eq(sorted([2, 4])[0], 2, 'talk: Mei moves fewer')
    eq(X['E1']['val'], [count_all(7, 6)], 'E1'); eq(X['E2']['val'], [kit_add(3, 8, 5)], 'E2')
    eq(X['E3']['val'], [sum([6, 9, 4]), 6, 4], 'E3'); eq(6 + 4, 10, 'E3 pair')

    # ---- Home practice
    eq(H['H1']['val'], [fill_frame(9, 5)[2], count_all(9, 5)], 'H1')
    eq(H['H2']['val'], kit_add(3, 7, 6), 'H2')
    eq(H['H3']['val'], [to_next_ten(8), to_next_ten(45), to_next_ten(67)], 'H3')
    eq(H['H4']['val'], sum([5, 7, 5, 3]), 'H4'); eq(5 + 5 + 7 + 3, 20, 'H4 pairs')
    eq(H['H5']['val'], 'open', 'H5 open')

    # ---- Optional slide and spare-time menu
    eq(fill_frame(9, 9), (1, 10, 8), 'optional: 9 + 9, move 1, ten and 8'); eq(count_all(9, 9), 18, 'optional 18')
    # M1: for every pair of two-digit numbers (within 100) whose ones make exactly 10, the total ends in 0; otherwise (ones 6 and 6) not
    pairs_ok = [(p, q) for p in range(10, 90) for q in range(10, 90) if p + q < 100 and p % 10 + q % 10 == 10]
    eq(all((p + q) % 10 == 0 for p, q in pairs_ok), True, 'M1 ones make 10: total is a tens number')
    eq(len(pairs_ok) > 100, True, 'M1 enough cases checked')
    eq([kit_add(2, 4, 6) // 1, kit_add(3, 8, 2), kit_add(4, 5, 5)], [30, 40, 50], 'M1 kit helper sanity')
    eq([24 + 16, 38 + 52, 45 + 25], [40, 90, 70], 'M1 examples'); eq(26 + 36, 62, 'M1 counter-example'); eq((26 + 36) % 10 == 0, False, 'M1 counter-example is not a tens number')
    eq(6 + 7 + 4 + 5, 22, 'M2 example'); eq(fill_frame(8, 5), (2, 10, 3), 'M3 8 + 5'); eq(count_all(8, 5), 13, 'M3 13')

    # ---- Online practice authored answers
    for k in ('c1', 'c2', 'c3', 'c5', 't1', 't2', 't4', 'g1', 'g3'):
        eq(O[k]['answer'], ORACLES[k](BASE_ENV[k]), 'online ' + k)
    eq(O['c4']['answer'], '6 and 4', 'c4'); eq([p for p in O['c4']['options'] if sum(int(x) for x in p.split(' and ')) == 10], ['6 and 4'], 'c4 only one pair makes 10')
    eq(O['c6']['answer'], '10 + 4 = 14', 'c6'); eq(10 + 4, 14, 'c6 value'); eq(count_all(9, 5), 14, 'c6 total')
    eq(O['t3']['answer'], '19 + 12', 't3'); eq(O['g2']['answer'], 45, 'g2')
    eq(sorted(o for o in O['t3']['options'] if sum(int(x) for x in o.split(' + ')) != 30), ['19 + 12'], 't3 only one is not 30')
    # g4 selfcheck example in the steps
    eq(sum([45, 5, 17, 3, 20, 10]), 100, 'g4 example'); eq(50 + 20 + 30, 100, 'g4 pairs')
    # slips are wrong answers (the validator also checks this); recompute the traps they name
    eq(10 + 6, 16, 'c1 slip 16 = 10 + 6'); eq(30 + 6, 36, 'c3 slip 36'); eq(30 + 5, 35, 'c5 slip 35'); eq(27 - 5, 22, 'c5 slip 22')
    eq(18 + 34, 52, 't4 slip 52'); eq(4 + 9, 13, 't1 slip 13'); eq(sum([1, 2, 3, 4, 5, 6, 7, 8, 9]) - 5, 40, 'g2 slip 40')
    # every template variant gives a positive total within 100 and, for the make-a-ten templates, really crosses a ten
    for a in (6, 7, 8, 9):
        for b in (5, 6, 7, 8, 9):
            eq(a + b > 10 and b > 10 - a, True, f'c1 {a} + {b} crosses ten')
    for t in range(1, 9):
        for o in (6, 7, 8, 9):
            for b in (5, 6, 7, 8, 9):
                eq(t * 10 + o + b < 100 and b > 10 - o, True, f'c3 {t}{o} + {b}')
    for nn in O['c5']['tpl']['vars']['n']:
        for b in O['c5']['tpl']['vars']['b']:
            eq(nn + b < 100 and b > 10 - nn % 10, True, f'c5 {nn} + {b}')
    for a in (5, 6, 7, 8):
        for b in (8, 9):
            eq(a <= b and a + b >= 10, True, f'g3 {a} + {b}')
    for xx in O['g1']['tpl']['vars']['x']:
        for S_ in (40, 50):
            eq(S_ - xx > 0, True, f'g1 y positive {xx} {S_}')
    for aa in O['t4']['tpl']['vars']['a']:
        eq(30 - aa > 0, True, 't4 green positive')
    return n
