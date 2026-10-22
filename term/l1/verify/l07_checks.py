"""Independent answer checks for Lesson 7 (Take Away, Count Up).

Every answer in l07.json is recomputed here from first principles: taking away is done by removing tokens from a pile,
and a gap is found by counting up one step at a time (never by using the lesson's own subtraction). run(d) returns the
number of checks; any failure raises AssertionError.
"""

def pile(n):
    return list(range(n))


def take_away(n, k):
    """Remove k tokens from a pile of n tokens and count what is left."""
    p = pile(n)
    for _ in range(k):
        p.pop()
    return len(p)


def take_away_tens_then_ones(n, k):
    """Take away the tens of k first, then its ones, one token at a time."""
    p = pile(n)
    for _ in range((k // 10) * 10):
        p.pop()
    mid = len(p)
    for _ in range(k % 10):
        p.pop()
    return mid, len(p)


def count_up(a, b):
    """Steps of 1 from a up to b."""
    x, steps = a, 0
    while x < b:
        x += 1
        steps += 1
    return steps


def hops(a, b):
    """(hop to next ten, tens jumps as a number, last hop) counting up from a to b; the sum is the gap."""
    x = a
    h1 = 0
    while x % 10 != 0 and x < b:
        x += 1; h1 += 1
    j = 0
    while x + 10 <= b:
        x += 10; j += 10
    h2 = 0
    while x < b:
        x += 1; h2 += 1
    return h1, j, h2


def next_ten_gap(n):
    return count_up(n, ((n // 10) + 1) * 10)


# ---- oracles for the online-practice templates (brute force, independent of the template expressions)
ORACLES = {
    'c1': lambda e: take_away(e['a'], e['t'] * 10),
    'c2': lambda e: take_away(e['a'], e['o']),
    'c3': lambda e: take_away_tens_then_ones(e['ta'] * 10 + e['oa'], e['tb'] * 10 + e['ob'])[1],
    'c4': lambda e: take_away(e['a'], e['b']),
    't1': lambda e: sum(hops(e['x'], e['x'] + e['g'])),
    't2': lambda e: count_up(e['b'], e['b'] + e['g']),
    't3': lambda e: count_up(e['a'] + e['c'], e['a'] + e['g'] + e['c']),
    'g1': lambda e: count_up(e['n'], 100),
    # the blank is the number whose gap up to the new top number equals the old gap (b up to a)
    'g2': lambda e: [x for x in range(0, 200) if x < e['a'] + e['c'] and count_up(x, e['a'] + e['c']) == count_up(e['b'], e['a'])][0],
    'g3': lambda e: [x for x in range(0, e['m'] + 1) if count_up(x, e['m']) == e['g']][0],
}
BASE_ENV = {'c1': dict(a=58, t=2), 'c2': dict(a=76, o=3), 'c3': dict(ta=6, oa=8, tb=2, ob=5), 'c4': dict(a=86, b=32),
            't1': dict(x=38, g=24), 't2': dict(b=58, g=4), 't3': dict(a=24, g=7, c=10),
            'g1': dict(n=64), 'g2': dict(a=83, b=47, c=3), 'g3': dict(m=71, g=24)}


def run(d):
    n = 0

    def eq(a, b, msg=''):
        nonlocal n
        n += 1
        assert a == b, f'{msg}: got {a}, expected {b}'
    T = {q['id']: q for q in d['tiers']['start'] + d['tiers']['think'] + d['tiers']['go']}
    X = {q['id']: q for q in d['exit']}
    # sneak-peek
    eq(d['sneak_peek']['val1'], take_away(15, 4), 'sneak q1: 15 stars, cross out 4')
    eq(d['sneak_peek']['val1'], 11, 'sneak q1 value')
    eq(count_up(58, 62), 4, 'sneak q2 gap')
    eq(sum(hops(58, 62)), 4, 'sneak q2 hops 2 + 2')
    eq(hops(58, 62), (2, 0, 2), 'sneak q2 hops')
    eq(d['sneak_peek']['a2'].startswith('4 more'), True, 'sneak a2 says 4 more')
    import sys, os
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
    eq(svg.scatter(sc['n'], sc.get('seed', 1)).count('<polygon'), 15, 'scatter draws 15 stars')
    # Start here
    eq(take_away_tens_then_ones(68, 20), (48, 48), 'S1 68 - 2 tens')
    eq(T['S1']['val'], [6 - 2, 8, take_away(68, 20)], 'S1')
    eq(take_away(68, 20) // 10, 4, 'S1 tens left'); eq(take_away(68, 20) % 10, 8, 'S1 ones left')
    eq(T['S2']['val'], [take_away(57, 20), take_away(57, 4), take_away(86, 30), take_away(86, 5)], 'S2')
    eq(take_away_tens_then_ones(68, 25), (48, 43), 'S3 tens then ones')
    eq(T['S3']['val'], list(take_away_tens_then_ones(68, 25)), 'S3')
    eq(T['S4']['val'], [take_away(46, 12), take_away(46, 12) + 12], 'S4')
    eq(take_away(46, 12) + 12, 46, 'S4 check by adding gives the start')
    eq(T['S5']['val'], [take_away(45, 13)], 'S5')
    eq(take_away_tens_then_ones(45, 13), (35, 32), 'S5 tens then ones')
    eq(T['S6']['val'], [take_away(59, 20)], 'S6')
    eq(take_away(59, 2), 57, 'S6 Kumar took away 2 ones')
    eq(take_away(59, 20) == 57, False, 'S6 Kumar is wrong')
    eq(T['S7']['val'], [take_away(64, 21)], 'S7')
    eq(take_away(64, 21) + 21, 64, 'S7 check by adding')
    # Think harder
    eq(hops(38, 62), (2, 20, 2), 'T1 hops')
    eq(T['T1']['val'], [count_up(38, 62)], 'T1')
    eq(count_up(38, 62), 24, 'T1 gap')
    eq(38 + 24, 62, 'T1 check by adding')
    eq(hops(77, 83), (3, 0, 3), 'T2 hops')
    eq(T['T2']['val'], [count_up(77, 83)], 'T2')
    eq(take_away(83, 77), 6, 'T2 value by take away')
    eq(take_away(83, 14) == 69, True, 'T2 column-swap slip 14 is wrong')
    ali, ben = 24, 31
    eq(count_up(ali, ben), 7, 'T3 gap before')
    eq(count_up(ali + 10, ben + 10), 7, 'T3 gap after both get 10 more')
    eq(T['T3']['val'], [count_up(ali + 10, ben + 10)], 'T3')
    eq(hops(46, 71), (4, 20, 1), 'T4 hops')
    eq(T['T4']['val'], [count_up(46, 71)], 'T4')
    eq(take_away(71, 46), 25, 'T4 same by take away')
    # Go further
    eq(T['G1']['val'], [count_up(68, 71), take_away(71, 20)], 'G1')
    eq(hops(68, 71), (2, 0, 1), 'G1 hops 2 then 1')
    eq(take_away_tens_then_ones(71, 20)[1], 51, 'G1 take away 2 tens')
    eq(T['G2']['val'], [count_up(64, 100)], 'G2 count up')
    eq(take_away_tens_then_ones(100, 64), (40, 36), 'G2 take away 6 tens then 4 ones')
    eq(hops(64, 100), (6, 30, 0), 'G2 hops')
    eq(take_away(100, 64) + 64, 100, 'G2 check by adding')
    g3a, g3b = count_up(47, 83), take_away(86, 50)
    eq(T['G3']['val'], [g3a, g3b], 'G3')
    eq(g3a == g3b, True, 'G3 same answer')
    eq(hops(47, 83), (3, 30, 3), 'G3 hops')
    eq((86 - 83, 50 - 47), (3, 3), 'G3 both numbers go up by 3')
    # Investigation: count-up is shorter when the numbers are close; take-away is short when the small number is whole tens or small
    eq(count_up(49, 52), 3, 'I1 52 - 49'); eq(take_away(52, 10), 42, 'I1 52 - 10')
    # the gap does not change when both numbers move by the same amount, for every pair
    ok_all = all(count_up(a, b) == count_up(a + k, b + k) for a in range(0, 30) for b in range(a, a + 20) for k in (1, 5, 10, 20))
    eq(ok_all, True, 'gap stays the same when both numbers move by the same amount')
    # Talk and exit
    eq(sum(hops(49, 52)), 3, 'talk: 49 to 52 is 3'); eq(hops(49, 52), (1, 0, 2), 'talk: hops 1 then 2')
    eq(take_away(52, 40), 12, 'talk: Ravi 52 - 40'); eq(take_away(12, 9), 3, 'talk: Ravi then 12 - 9')
    eq(X['E1']['val'], [take_away(58, 24)], 'E1'); eq(take_away_tens_then_ones(58, 24), (38, 34), 'E1 tens then ones')
    eq(X['E2']['val'], [count_up(57, 62), count_up(57, 62)], 'E2'); eq(hops(57, 62), (3, 0, 2), 'E2 hops')
    eq(X['E3']['val'], [count_up(87, 90)], 'E3'); eq(take_away(90, 87), 3, 'E3 by take away')
    # Home practice
    H = {h['id']: h for h in d['home_practice']}
    eq(H['H1']['val'], take_away(78, 20), 'H1')
    eq(H['H2']['val'], [take_away(76, 43), take_away(76, 43) + 43], 'H2'); eq(take_away(76, 43), 33, 'H2 value')
    eq(H['H3']['val'], take_away(89, 36), 'H3'); eq(take_away_tens_then_ones(89, 36), (59, 53), 'H3 tens then ones')
    eq(H['H4']['val'], count_up(47, 71), 'H4'); eq(hops(47, 71), (3, 20, 1), 'H4 hops'); eq(count_up(38, 71), 33, 'H5 example gap 33')
    eq(hops(38, 71), (2, 30, 1), 'H5 example hops')
    # Optional slide and spare-time menu
    eq(count_up(59, 63), 4, 'optional 59 to 63'); eq(count_up(68, 72), 4, 'optional 68 to 72'); eq(count_up(58, 62), 4, 'optional 58 to 62')
    eq([count_up(a, a + 8) for a in (12, 22, 32)], [8, 8, 8], 'M1 gap 8 each time')
    eq(count_up(12, 20), 8, 'M1 12 to 20'); eq(count_up(22, 30), 8, 'M1 22 to 30'); eq(count_up(32, 40), 8, 'M1 32 to 40')
    eq(count_up(58, 62), 4, 'M3 58 to 62'); eq(hops(58, 62), (2, 0, 2), 'M3 hops')
    # Mini-lesson worked examples
    eq(take_away_tens_then_ones(57, 24), (37, 33), 'm1 57 - 24')
    eq(33 + 24, 57, 'm2 check by adding'); eq(take_away(57, 33), 24, 'm2 57 - 33')
    eq(hops(47, 52), (3, 0, 2), 'm3 hops 3 then 2'); eq(count_up(47, 52), 5, 'm3 gap')
    eq(hops(38, 62), (2, 20, 2), 'm4 hops')
    eq(count_up(78, 81), 3, 'm5 81 - 78'); eq(take_away_tens_then_ones(65, 23), (45, 42), 'm5 65 - 23')
    eq(count_up(59, 62), 3, 'm6 62 - 59 by counting up'); eq(take_away(62, 20), 42, 'm6 62 - 20')
    # Explore
    eq(take_away_tens_then_ones(57, 24), (37, 33), 'explore 57 - 24')
    eq(take_away_tens_then_ones(76, 25), (56, 51), 'explore 76 take away 2 bars and 5 squares leaves 51')
    eq(hops(38, 62), (2, 20, 2), 'explore 38 to 62'); eq(hops(47, 52), (3, 0, 2), 'explore 47 to 52')
    # warm-up
    eq([next_ten_gap(7), next_ten_gap(4), next_ten_gap(9), next_ten_gap(2)], [3, 6, 1, 8], 'remember fingers to ten')
    eq([next_ten_gap(38), next_ten_gap(47), next_ten_gap(56)], [2, 3, 4], 'remember next ten')
    # break pairs
    eq([sum(hops(a, b)) for a, b in ((8, 30), (25, 40), (47, 52), (36, 71))], [22, 15, 5, 35], 'break gaps')
    # Online practice authored answers
    O = {i['id']: i for i in d['online_practice']['items']}
    for k in ('c1', 'c2', 'c3', 'c4', 't1', 't2', 't3', 'g1', 'g2', 'g3'):
        eq(O[k]['answer'], ORACLES[k](BASE_ENV[k]), 'authored ' + k)
    eq(O['c5']['answer'], '33 + 24 = 57', 'c5'); eq(33 + 24, 57, 'c5 value')
    eq(O['t4']['answer'], 'Count up from 79 to 82', 't4'); eq(count_up(79, 82), 3, 't4 gap'); eq(hops(79, 82), (1, 0, 2), 't4 hops 1 then 2')
    eq(count_up(47, 71), 24, 'g4 example gap'); eq(47 + 24, 71, 'g4 example check')
    return n
