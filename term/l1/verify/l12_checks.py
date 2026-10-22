"""Independent answer checks for Level 1 Term 2 Lesson 12 (Bar Strips: More and Fewer).

A strip is modelled as a list of cells. The gap between two strips is the number of cells of the longer strip that the
shorter one does not cover; "more than" adds cells; altogether joins the two lists; sum-and-difference and transfer
problems are solved by trying every possible split (brute force), not by the lesson's own halving rule.
run(d) returns the number of checks; any failure raises AssertionError.
"""
import itertools


def strip(n):
    return [1] * n


def gap(long_n, short_n):
    return sum(1 for i in range(long_n) if i >= short_n)


def add_cells(n, extra):
    s = strip(n)
    for _ in range(extra): s.append(1)
    return len(s)


def altogether(*ns):
    joined = []
    for n in ns: joined += strip(n)
    return len(joined)


def split_by_total_and_gap(total, g):
    """All (small, big) whole-number pairs with small + big = total and big - small = g."""
    return [(a, total - a) for a in range(0, total + 1) if (total - a) - a == g]


def transfer_to_equal(a, b):
    """Cells to move from the bigger strip to the smaller one so the two are equal."""
    return [m for m in range(0, a + 1) if a - m == b + m]


def three_with_steps(total, d):
    """Ali, Ben = Ali + d, Mei = Ben + d with the given total: all Ali values."""
    return [x for x in range(0, total + 1) if x + (x + d) + (x + 2 * d) == total]


def fewer_than(r, d):
    return [w for w in range(0, r + 1) if r - w == d]


def top_shelf_first(total, moved):
    return [t for t in range(0, total + 1) if (t - moved) == (total - t) + moved]


ORACLES = {
    'c1': lambda e: gap(e['a'], e['b']),
    'c2': lambda e: add_cells(e['a'], e['d']),
    'c4': lambda e: altogether(e['a'], add_cells(e['a'], e['d'])),
    't1': lambda e: split_by_total_and_gap(e['T'], e['d'])[0][0],
    't2': lambda e: transfer_to_equal(e['a'], e['b'])[0],
    't3': lambda e: fewer_than(e['r'], e['d'])[0],
    'g1': lambda e: top_shelf_first(e['T'], e['m'])[0],
    'g2': lambda e: three_with_steps(e['T'], e['d'])[0],
}
BASE_ENV = {'c1': dict(a=12, b=8), 'c2': dict(a=15, d=7), 'c4': dict(a=10, d=4), 't1': dict(T=40, d=8), 't2': dict(a=30, b=18),
            't3': dict(d=18, r=52), 'g1': dict(T=52, m=7), 'g2': dict(T=90, d=10)}


def run(d):
    n = 0

    def eq(a, b, msg=''):
        nonlocal n
        n += 1
        assert a == b, f'{msg}: got {a!r}, expected {b!r}'

    T = {q['id']: q for q in d['tiers']['start'] + d['tiers']['think'] + d['tiers']['go']}
    X = {q['id']: q for q in d['exit']}
    # warm-up
    eq([x for x in range(0, 20) if x + 4 == 10], [6], 'warm-up: add 4 to get 10'); eq([x for x in range(0, 30) if x - 3 == 8], [11], 'warm-up: take away 3 to get 8')
    eq(gap(14, 9), 5, 'warm-up gap 14 and 9'); eq(gap(13, 6), 7, 'warm-up gap 13 and 6')
    eq(altogether(10, 10, 10, 6), 36, 'warm-up strip of 36')
    # sneak-peek
    eq(add_cells(5, 3), 8, 'sneak 1'); eq(d['sneak_peek']['val1'], 8, 'sneak val1')
    eq(transfer_to_equal(14, 10), [2], 'sneak 2'); eq(d['sneak_peek']['val2'], 2, 'sneak val2')
    # explore and mini-lesson
    eq(gap(12, 8), 4, 'explore gap'); eq(add_cells(5, 3), 8, 'explore Ali 8'); eq(add_cells(9, 4), 13, 'explore Ali 13'); eq(altogether(9, 13), 22, 'explore all'); eq(gap(13, 9), 4, 'explore gap 2')
    eq(gap(12, 7), 5, 'mini gap'); eq(add_cells(14, 6), 20, 'mini more than'); eq(altogether(14, 7), 21, 'mini altogether'); eq(gap(15, 8), 7, 'mini your turn')
    eq(split_by_total_and_gap(40, 8), [(16, 24)], 'mini total and difference'); eq(transfer_to_equal(30, 18), [6], 'mini transfer')
    # Start here
    eq(gap(12, 8), 4, 'S1'); eq(T['S1']['val'], [4], 'S1 val')
    eq(add_cells(15, 7), 22, 'S2'); eq(T['S2']['val'], [22], 'S2 val')
    dev = add_cells(34, 17); eq(dev, 51, 'S3a'); eq(altogether(34, dev), 85, 'S3b'); eq(T['S3']['val'], [51, 85], 'S3 val')
    eq(gap(9, 5), 4, 'S4'); eq(T['S4']['val'], [4], 'S4 val')
    ali = add_cells(28, 6); eq(ali, 34, 'S5a'); eq(altogether(28, ali), 62, 'S5b'); eq(T['S5']['val'], [34, 62], 'S5 val')
    eq(gap(45, 30), 15, 'S6'); eq(T['S6']['val'], [15], 'S6 val')
    opts = {1: 24 + 40, 2: 40 - 24, 3: 40 + 40, 4: 24 + 24}
    eq([k for k, v in opts.items() if v == gap(40, 24)], [2], 'S7 only sentence (2) gives the gap'); eq(T['S7']['val'], [2], 'S7 val')
    eq([o for o in T['S7']['mcq']['options']], ['24 + 40', '40 - 24', '40 + 40', '24 + 24'], 'S7 options match the model')
    # Think harder
    eq(split_by_total_and_gap(40, 8), [(16, 24)], 'T1'); eq(T['T1']['val'], [16, 24], 'T1 val')
    eq(transfer_to_equal(30, 18), [6], 'T2'); eq(T['T2']['val'], [6], 'T2 val')
    w = fewer_than(52, 18); eq(w, [34], 'T3a'); eq(altogether(52, w[0]), 86, 'T3b'); eq(T['T3']['val'], [34, 86], 'T3 val')
    # Go further
    eq(top_shelf_first(52, 7), [33], 'G1 top'); eq(52 - 33, 19, 'G1 bottom'); eq(33 - 7, 19 + 7, 'G1 equal after the move'); eq(T['G1']['val'], [33, 19], 'G1 val')
    x = three_with_steps(90, 10); eq(x, [20], 'G2 Ali'); eq(x[0] + 2 * 10, 40, 'G2 Mei'); eq(T['G2']['val'], [20, 40], 'G2 val')
    sit = [(sv, sv + 12) for sv in range(5, 40)]
    eq({(kv + 4) - (sv - 4) for sv, kv in sit}, {20}, 'G3: for every start, Kumar then has 20 more'); eq(T['G3']['val'], [20], 'G3 val')
    # Investigation: same total 10, gaps 2, 4, 6
    eq([split_by_total_and_gap(10, g)[0] for g in (2, 4, 6)], [(4, 6), (3, 7), (2, 8)], 'investigation pairs'); eq(split_by_total_and_gap(10, 3), [], 'investigation: total 10 with an odd gap is impossible')
    eq(d['tiers']['investigation']['val'], ['6 and 4', '7 and 3', '8 and 2'], 'investigation val')
    # Exit and home
    eq(gap(13, 9), 4, 'E1'); eq(add_cells(27, 15), 42, 'E2'); eq(altogether(25, add_cells(25, 8)), 58, 'E3'); eq([X['E1']['val'], X['E2']['val'], X['E3']['val']], [[4], [42], [58]], 'exit vals')
    eq(gap(14, 9), 5, 'H1'); eq(add_cells(38, 20), 58, 'H2'); eq(altogether(25, add_cells(25, 15)), 65, 'H3')
    eq(split_by_total_and_gap(30, 6)[0][0], 12, 'H4'); eq(transfer_to_equal(24, 10), [7], 'H5')
    return n
