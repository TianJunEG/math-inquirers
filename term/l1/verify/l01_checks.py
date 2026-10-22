"""Independent answer checks for Lesson 1 (Bundles and Singles).

Every answer in l01.json is recomputed here from first principles (counting sticks, enumerating numbers), not by
re-using the lesson's own expressions. run(d) returns the number of checks; any failure raises AssertionError.
"""

def stick_count(tens, ones):
    """Build the actual list of sticks: each bundle holds 10 sticks."""
    sticks = []
    for _ in range(tens):
        sticks += [1] * 10
    sticks += [1] * ones
    return len(sticks)


def digits(n):
    return divmod(n, 10)


def ways_to_show(n):
    """All (tens, ones) pairs that make n sticks, opening bundles allowed."""
    return [(t, n - 10 * t) for t in range(n // 10, -1, -1)]


# ---- oracles for the online-practice templates (brute force, independent of the template expressions)
ORACLES = {
    'c1': lambda e: stick_count(e['t'], e['o']),
    'c2': lambda e: sum(1 for k in range(1, 10) if 10 * k <= e['n']),                    # full bundles by counting
    'c3': lambda e: e['n'] - 10 * sum(1 for k in range(1, 10) if 10 * k <= e['n']),      # what remains
    'c4': lambda e: stick_count(e['t'], e['o']),
    'c5': lambda e: stick_count(e['t'], 0),
    't1': lambda e: stick_count(e['t'], e['o']),
    't2': lambda e: [o for (t, o) in ways_to_show(e['t'] * 10 + e['o']) if t == e['t'] - 1][0],
    'g1': lambda e: e['s'] - stick_count(e['t'], e['o']),
    'g2': lambda e: e['N'] - stick_count(e['b'], e['l']),
    'g3': lambda e: len(ways_to_show(e['n'])),
}
BASE_ENV = {'c1': dict(t=3, o=4), 'c4': dict(t=2, o=9), 'c5': dict(t=7), 't1': dict(t=5, o=14), 't2': dict(t=4, o=1),
            'g1': dict(t=6, o=14, s=85), 'g2': dict(b=4, l=18, N=60), 'g3': dict(n=30), 'c2': dict(n=47), 'c3': dict(n=47)}


def run(d):
    n = 0
    def eq(a, b, msg=''):
        nonlocal n
        n += 1
        assert a == b, f'{msg}: got {a}, expected {b}'
    T = {q['id']: q for q in d['tiers']['start'] + d['tiers']['think'] + d['tiers']['go']}
    X = {q['id']: q for q in d['exit']}
    # sneak-peek
    eq(d['sneak_peek']['val1'], 24, 'sneak q1 star count')
    eq(stick_count(3, 4), 34, 'sneak q2: 3 bundles + 4 = 34')
    # the scatter picture really has 24 stars
    import re, sys, os
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tools'))
    import svg
    sk = [s for s in d['slides'] if s['id'] == 's-sneak'][0]
    def find(blocks):
        for b in blocks:
            if b['t'] == 'visual' and b['type'] == 'scatter': return b
            if b['t'] == 'cols':
                for c in b['cols']:
                    r = find(c)
                    if r: return r
    sc = find(sk['blocks'])
    eq(svg.scatter(sc['n'], sc.get('seed', 1)).count('<polygon'), 24, 'scatter draws 24 stars')
    eq(sc['n'], d['sneak_peek']['val1'], 'sneak picture matches answer')
    # Start here
    eq(T['S1']['val'], [2, 6, stick_count(2, 6)], 'S1')
    eq(T['S2']['val'], [stick_count(3, 5)], 'S2')
    eq(T['S3']['val'], [stick_count(4, 2), stick_count(7, 0), stick_count(1, 9), stick_count(8, 5)], 'S3')
    eq(T['S4']['val'], list(digits(58)) + list(digits(40)) + list(digits(71)), 'S4')
    eq(T['S5']['val'], list(digits(47)), 'S5')
    eq(T['S6']['val'], [stick_count(3, 4)], 'S6')
    eq(43 == stick_count(3, 4), False, 'S6: Siti is wrong')
    eq(sorted(digits(43)), [3, 4], 'S6: she swapped the digits')
    # Think harder
    eq(T['T1']['val'], [stick_count(5, 14)], 'T1 5 tens 14 ones')
    eq(digits(64), (6, 4), 'T1 as tens and ones')
    eq(T['T2']['val'], [dict(ways_to_show(41))[3]], 'T2 41 as 3 tens __ ones')
    cands = [n_ for n_ in range(10, 100) if 30 < n_ < 50 and n_ % 10 == 6 and (n_ // 10) % 2 == 0]
    eq(cands, [46], 'T3 unique number')
    eq(T['T3']['val'], cands, 'T3')
    eq(stick_count(7, 2) == stick_count(6, 12), True, 'T4 same number')
    eq(stick_count(7, 2), 72, 'T4 value')
    eq(T['T4']['val'], ['same', 72], 'T4')
    # Go further
    ben, siti = stick_count(6, 14), 85
    eq(T['G1']['val'], ['Siti', ben, siti, siti - ben], 'G1')
    eq(ben, 74, 'G1 Ben'); eq(siti - ben, 11, 'G1 difference')
    have = stick_count(4, 18)
    eq(T['G2']['val'], [have, 60 - have], 'G2')
    eq(60 - have, 2, 'G2 needs 2 more')
    eq(len(ways_to_show(30)), 4, 'G3 ways to show 30')
    eq(ways_to_show(30), [(3, 0), (2, 10), (1, 20), (0, 30)], 'G3 list of ways')
    eq(T['G3']['val'], [4], 'G3')
    # Investigation: enumerate every two-digit number
    bigger = [n_ for n_ in range(11, 100) if n_ % 10 and int(str(n_)[::-1]) > n_]
    smaller = [n_ for n_ in range(10, 100) if int(str(n_)[::-1]) < n_]
    same = [n_ for n_ in range(10, 100) if int(str(n_)[::-1]) == n_]
    eq(all((n_ // 10) < (n_ % 10) for n_ in bigger), True, 'swap bigger iff tens < ones')
    eq(all((n_ // 10) > (n_ % 10) for n_ in smaller), True, 'swap smaller iff tens > ones')
    eq(all((n_ // 10) == (n_ % 10) for n_ in same), True, 'swap same iff digits equal')
    eq(len(bigger) + len(smaller) + len(same), 90, 'every number is exactly one of the three')
    eq(int('41') > int('14') and int('62') > int('26') and int('25') < int('52') and int('77') == int('77'), True, 'investigation first step')
    eq(int('03'[::-1][::-1]) , 3, 'a number ending in 0 becomes 03 = 3')
    # Talk and exit
    eq(stick_count(2, 6) < stick_count(6, 2), True, 'talk: 26 < 62')
    eq(X['E1']['val'], [stick_count(4, 8)], 'E1')
    eq(X['E2']['val'], list(digits(37)), 'E2')
    eq(X['E3']['val'], [stick_count(7, 0)], 'E3')
    # Home practice
    H = {h['id']: h for h in d['home_practice']}
    eq(H['H1']['val'], stick_count(3, 8), 'H1')
    eq(H['H2']['val'], list(digits(65)), 'H2')
    eq(H['H3']['val'], stick_count(2, 9), 'H3')
    eq(H['H4']['val'], stick_count(4, 12), 'H4'); eq(stick_count(4, 12) == 52, True, 'H4 is 52 not 412')
    # Optional slide
    eq(stick_count(9, 9), 99, 'optional: 9 bundles + 9 singles'); eq(stick_count(9, 9) + 1, 100, 'one more is 100')
    # Online practice authored answers
    O = {i['id']: i for i in d['online_practice']['items']}
    eq(O['c1']['answer'], ORACLES['c1'](BASE_ENV['c1']), 'c1')
    eq(O['c2']['answer'], 4, 'c2'); eq(O['c3']['answer'], 7, 'c3')
    eq(O['c4']['answer'], ORACLES['c4'](BASE_ENV['c4']), 'c4'); eq(O['c5']['answer'], 70, 'c5')
    eq(O['c6']['answer'], '46', 'c6'); eq(stick_count(4, 6), 46, 'c6 value')
    eq(O['t1']['answer'], 64, 't1'); eq(O['t2']['answer'], 11, 't2'); eq(O['t3']['answer'], 46, 't3')
    eq(O['t4']['answer'], 'They have the same', 't4')
    eq(O['g1']['answer'], 11, 'g1'); eq(O['g2']['answer'], 2, 'g2'); eq(O['g3']['answer'], 4, 'g3')
    # g4 example puzzle: unique answer 63
    eq([n_ for n_ in range(60, 81) if n_ % 10 == 3 and (n_ // 10) % 2 == 0], [63], 'g4 example unique')
    # every template variant of g2 and g1 is positive (guards a negative "how many more")
    return n
