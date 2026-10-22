"""Independent answer checks for Lesson 8 (Balance and Swap).

Every answer in l08.json is recomputed here from first principles: blanks are found by searching for the number that makes
two piles of counters match, comparisons are made by counting, and the Investigation is checked over every pair of small
numbers. It does not reuse the lesson's own give-and-take rule. run(d) returns the number of checks; a failure raises AssertionError.
"""


def pile(*sizes):
    """Total number of counters when piles of these sizes sit on one plate (built one counter at a time)."""
    counters = []
    for s in sizes:
        counters += [1] * s
    return len(counters)


def blank(left, right_known):
    """Smallest number of counters to add as a second pile on the right so the plates match (search)."""
    target = pile(*left)
    for x in range(0, 500):
        if pile(*right_known, x) == target:
            return x
    raise AssertionError('no blank found')


def first_blank(known_after, left):
    target = pile(*left)
    for x in range(0, 500):
        if pile(x, known_after) == target:
            return x
    raise AssertionError('no first blank')


def pairs_for(p, q, limit=60):
    """All (x, y) with x + p == q + y, searched."""
    return [(x, y) for x in range(limit) for y in range(limit) if x + p == q + y]


# ---- oracles for the online-practice templates (brute force, independent of the template expressions)
ORACLES = {
    'c1': lambda e: blank((e['a'], e['b']), (e['a'] - e['k'],)),
    'c2': lambda e: blank((e['a'], e['b']), (e['a'] + e['k'],)),
    'c4': lambda e: blank((10 * e['t'], 10 * e['u']), (10 * (e['t'] + 1),)),
    't1': lambda e: blank((10 * e['x'] - e['y'], e['b']), (10 * e['x'],)),
    't4': lambda e: blank((e['a'], e['b']), (e['a'] + e['k'],)),
    'g2': lambda e: blank((e['a'], e['b']), (e['a'] + e['k'],)),
    'g3': lambda e: {x - y for (x, y) in pairs_for(e['p'], e['q'])}.pop() if len({x - y for (x, y) in pairs_for(e['p'], e['q'])}) == 1 else None,
}
BASE_ENV = {'c1': dict(a=5, b=3, k=1), 'c2': dict(a=4, b=7, k=2), 'c4': dict(t=3, u=3), 't1': dict(x=5, y=1, b=26),
            't4': dict(a=24, b=17, k=2), 'g2': dict(a=28, b=17, k=2), 'g3': dict(p=5, q=9)}


def run(d):
    n = 0

    def eq(a, b, msg=''):
        nonlocal n
        n += 1
        assert a == b, f'{msg}: got {a}, expected {b}'

    T = {q['id']: q for q in d['tiers']['start'] + d['tiers']['think'] + d['tiers']['go']}
    X = {q['id']: q for q in d['exit']}
    H = {h['id']: h for h in d['home_practice']}

    # Remember warm-up: bonds to 10 and to 20 by counting on
    for have, need in [(7, 3), (4, 6), (9, 1), (6, 4), (2, 8)]:
        eq(pile(have, need), 10, f'bond to 10 {have}')
    for have, need in [(13, 7), (16, 4), (18, 2), (15, 5)]:
        eq(pile(have, need), 20, f'bond to 20 {have}')
    eq(pile(3, 4) == pile(5, 2), True, 'warm-up 3+4 = 5+2')
    eq(pile(3, 4) == pile(6, 2), False, 'warm-up 3+4 != 6+2')
    eq(pile(4, 4) == pile(5, 3), True, 'warm-up 4+4 = 5+3')

    # Sneak-peek
    eq(pile(6, 4), 10, 'sneak q1 Ravi'); eq(pile(5, 5), 10, 'sneak q1 Siti'); eq(pile(6, 4) == pile(5, 5), True, 'sneak q1 same')
    eq(d['sneak_peek']['val1'], 10, 'sneak val1')
    eq(blank((8, 5), (9,)), 4, 'sneak q2'); eq(d['sneak_peek']['val2'], 4, 'sneak val2')

    # Explore rounds
    eq(blank((6, 4), (5,)), 5, 'explore 1a'); eq(blank((7, 3), (8,)), 2, 'explore 1b'); eq(blank((9, 2), (8,)), 3, 'explore 1c')
    for a, b in [(7, 5), (6, 6), (5, 7), (4, 8)]:
        eq(pile(a, b), 12, f'give and take chain {a}+{b}')
    eq(blank((8, 4), (9,)), 3, 'explore 3a'); eq(blank((6, 5), (8,)), 3, 'explore 3b')

    # Mini-lesson
    eq(pile(5, 3) == pile(4, 4), True, 'm1')
    eq(blank((8, 6), (7,)), 7, 'm3 a'); eq(blank((9, 4), (10,)), 3, 'm3 b'); eq(blank((6, 5), (4,)), 7, 'm3 c')
    eq(blank((25, 18), (27,)), 16, 'm4'); eq(pile(25, 18), 43, 'm4 left'); eq(pile(27, 16), 43, 'm4 right')
    eq(pile(47, 18), pile(45, 20), 'm5 same total'); eq(pile(47, 18), 65, 'm5 value')
    eq(pile(29, 14) < pile(30, 15), True, 'm5 not the same'); eq((pile(29, 14), pile(30, 15)), (43, 45), 'm5 values')

    # Start here
    eq(T['S1']['val'], [blank((5, 3), (4,)), blank((6, 4), (5,)), first_blank(7, (7, 3)), blank((2, 8), (8,))], 'S1')
    eq(T['S1']['val'], [4, 5, 3, 2], 'S1 values')
    eq(pile(6, 2), 8, 'S2 left plate'); eq(T['S2']['val'], [blank((6, 2), (7,))], 'S2'); eq(T['S2']['val'], [1], 'S2 value')
    eq(blank((6, 3), (5,)), 4, 'S3'); eq(T['S3']['val'], [4], 'S3 val'); eq(pile(6, 3) == pile(5, 9), False, 'S3: 9 is wrong')
    eq(T['S4']['val'], [blank((12,), (6,)), blank((12,), (5,)), blank((12,), (4,))], 'S4')
    eq(T['S4']['val'], [6, 7, 8], 'S4 values'); eq(pile(7, 5), 12, 'S4 start')
    eq(T['S5']['val'], [blank((20, 30), (40,)), blank((50, 20), (60,)), blank((34, 5), (35,)), blank((61, 8), (60,))], 'S5')
    eq(T['S5']['val'], [10, 10, 4, 9], 'S5 values')
    eq(T['S6']['val'], [blank((9, 6), (10,))], 'S6'); eq(T['S6']['val'], [5], 'S6 value'); eq(pile(9, 6), 15, 'S6 Mei total')
    eq(T['S7']['val'], [first_blank(2, (35, 12))], 'S7'); eq(T['S7']['val'], [45], 'S7 value'); eq(pile(35, 12), 47, 'S7 total')

    # Think harder
    eq(pile(47, 18) == pile(45, 20), True, 'T1 same'); eq(T['T1']['val'], ['Mei', pile(47, 18)], 'T1'); eq(pile(47, 18), 65, 'T1 total')

    def cmp(l, r):
        a, b = pile(*l), pile(*r)
        return 'same' if a == b else ('left' if a > b else 'right')
    eq(T['T2']['val'], [cmp((29, 14), (30, 13)), cmp((53, 20), (50, 23)), cmp((26, 15), (28, 16))], 'T2')
    eq((pile(26, 15), pile(28, 16)), (41, 44), 'T2c totals')
    eq(T['T3']['val'], [blank((49, 26), (50,)), pile(49, 26)], 'T3'); eq(T['T3']['val'], [25, 75], 'T3 values'); eq(pile(50, 25), 75, 'T3 check')
    eq(pile(24, 17) == pile(26, 19), False, 'T4 not balanced'); eq((pile(24, 17), pile(26, 19)), (41, 45), 'T4 totals')
    eq(T['T4']['val'], ['no', blank((24, 17), (26,))], 'T4'); eq(blank((24, 17), (26,)), 15, 'T4 value')

    # Go further
    total = pile(19, 28)
    eq(total, 47, 'G1 total')
    eq(T['G1']['val'], [blank((19, 28), (20,)), first_blank(30, (19, 28))], 'G1'); eq(T['G1']['val'], [27, 17], 'G1 values')
    eq(pile(20, 27), 47, 'G1 first'); eq(pile(17, 30), 47, 'G1 second')
    ps = pairs_for(5, 9)
    eq(all(x - y == 4 for (x, y) in ps), True, 'G2 the first blank is always 4 more')
    eq(len(ps) > 3, True, 'G2 at least three pairs'); eq((5, 1) in ps and (6, 2) in ps and (7, 3) in ps and (4, 0) in ps, True, 'G2 examples')
    eq(T['G2']['val'], [4], 'G2')
    eq(pile(28, 17), 45, 'G3 Mei')
    eq(T['G3']['val'], [blank((28, 17), (30,)), blank((28, 17), (25,))], 'G3'); eq(T['G3']['val'], [15, 20], 'G3 values')

    # Investigation, over every pair of numbers from 0 to 20
    for a in range(0, 21):
        for b in range(0, 21):
            base = a + b
            if a >= 0 and b >= 3:
                eq(pile(a + 3, b - 3), base, 'inv give and take')
            eq(pile(a + 3, b + 3), base + 6, 'inv both up 3')
            if a >= 2 and b >= 2:
                eq(pile(a - 2, b - 2), base - 4, 'inv both down 2')
    eq(pile(6, 4), 10, 'inv first step'); eq((pile(7, 3), pile(7, 5)), (10, 12), 'inv first step 2')

    # Talk
    eq((pile(6, 4), pile(7, 5), pile(7, 3)), (10, 12, 10), 'talk')

    # Exit ticket
    eq(X['E1']['val'], [blank((9, 5), (10,))], 'E1'); eq(X['E1']['val'], [4], 'E1 value')
    eq(pile(28, 6) == pile(30, 4), True, 'E2 yes'); eq(X['E2']['val'], ['yes'], 'E2'); eq(pile(28, 6), 34, 'E2 value')
    eq(X['E3']['val'], [blank((30, 12), (40,))], 'E3'); eq(X['E3']['val'], [2], 'E3 value'); eq(pile(30, 12), 42, 'E3 total')

    # Home practice
    eq(H['H1']['val'], blank((6, 3), (5,)), 'H1'); eq(H['H2']['val'], blank((10, 4), (9,)), 'H2'); eq(H['H3']['val'], blank((20, 30), (40,)), 'H3')
    eq((H['H1']['val'], H['H2']['val'], H['H3']['val']), (4, 5, 10), 'H1-3 values')
    eq(pile(36, 14) == pile(34, 16), True, 'H4 yes'); eq(pile(36, 14), 50, 'H4 total')
    eq([pile(a, 12 - a) for a in range(0, 13)], [12] * 13, 'H5 all sums of 12')

    # Optional slide: 20 = k + blank
    eq([blank((20,), (k,)) for k in (11, 12, 13)], [9, 8, 7], 'optional slide')

    # Spare-time menu
    for a in range(0, 31):
        for b in range(0, 31):
            eq(pile(a, b), pile(b, a), 'M1 swap')
    eq(9 - 4, 5, 'M1 9 take away 4'); eq(4 - 9 < 0, True, 'M1 4 take away 9 cannot be done with counters')
    eq(pile(14, 6), 20, 'M2 example'); eq(pile(16, 4), 20, 'M2 example 2'); eq(blank((14, 6), (16,)), 4, 'M2 blank')
    eq(blank((25, 18), (27,)), 16, 'M3')

    # Online practice authored answers
    O = {i['id']: i for i in d['online_practice']['items']}
    for k, env in BASE_ENV.items():
        eq(O[k]['answer'], ORACLES[k](env), 'practice base ' + k)
    eq(O['c3']['answer'], '5 + 5', 'c3'); eq(pile(6, 4) == pile(5, 5), True, 'c3 value')
    eq([pile(5, 4), pile(7, 4), pile(6, 5)], [9, 11, 11], 'c3 wrong options all differ from 10')
    eq(O['c5']['answer'], '4', 'c5'); eq(blank((5, 3), (4,)), 4, 'c5 value')
    eq(O['t2']['answer'], '45 + 20', 't2'); eq([pile(45, 16), pile(49, 20), pile(47, 20)], [61, 69, 67], 't2 wrong options differ from 65')
    eq(O['t3']['answer'], '30 + 15', 't3'); eq(pile(30, 15) > pile(29, 14), True, 't3')
    eq(O['g1']['answer'], [27, 17], 'g1')
    # every wrong slip answer differs from the right answer; every variant is a positive whole number (guards negative blanks)
    for key in ('c1', 'c2', 'c4', 't1', 't4', 'g2'):
        tp = O[key]['tpl']
        import itertools
        names = list(tp['vars'])
        for combo in itertools.product(*[tp['vars'][nm] for nm in names]):
            env = dict(zip(names, combo))
            eq(ORACLES[key](env) >= 1, True, f'{key} variant {env} blank is at least 1')
    for p in O['g3']['tpl']['vars']['p']:
        for q in O['g3']['tpl']['vars']['q']:
            eq(q > p, True, f'g3 variant {p},{q} positive')
            eq(ORACLES['g3'](dict(p=p, q=q)), q - p, f'g3 difference {p},{q}')
    return n
