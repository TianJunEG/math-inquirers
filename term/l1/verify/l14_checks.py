"""Independent checks for Level 1 Term 2 Lesson 14 (Odd + Odd: Always, Sometimes, Never).
Parity is decided by pairing counters off one by one (never by %), sums by laying out counters; claims are tested by enumeration."""


def left_over(n):                  # pair counters off two at a time, count what remains
    rest = ['o'] * n
    while len(rest) >= 2:
        rest.pop(); rest.pop()
    return len(rest)


def kind(n): return 'odd' if left_over(n) == 1 else 'even'
def pairs(n):
    c = 0; rest = n
    while rest >= 2: rest -= 2; c += 1
    return c
def total(*nums): return len([c for n in nums for c in ['o'] * n])
def last_digit(n): return int(str(n)[-1])


def two_odds(n):                   # can n be made by adding two odd numbers (each at least 1)?
    return any(kind(a) == 'odd' and kind(n - a) == 'odd' for a in range(1, n))


ORACLES = {
    'c1': lambda e: kind(e['n']),
    'c2': lambda e: left_over(e['n']),
    'c4': lambda e: kind(e['n']),
    'c5': lambda e: left_over(e['n']),
    'c6': lambda e: [k for k in range(1, e['lim'] + 1) if left_over(k) == 0],
    't1': lambda e: kind(total(e['a'], e['b'])),
    't3': lambda e: 'yes' if two_odds(e['n']) else 'no',
    't4': lambda e: left_over(total(e['a'], e['b'])),
    'g1': lambda e: kind(total(e['a'], e['b'], e['c'])),
    'g2': lambda e: len([k for k in range(1, e['lim'] + 1) if left_over(k) == 1]),
}
BASE_ENV = {'c2': {'n': 7}, 'c5': {'n': 11}, 't4': {'a': 9, 'b': 5}, 'g2': {'lim': 10}}


def run(d):
    n = 0

    def eq(a, b, msg=''):
        nonlocal n
        n += 1
        assert a == b, f'{msg}: got {a}, expected {b}'
    T = {q['id']: q for q in d['tiers']['start'] + d['tiers']['think'] + d['tiers']['go']}
    X = {q['id']: q for q in d['exit']}
    H = {q['id']: q for q in d['home_practice']}
    # ---- Start here
    eq([left_over(6), left_over(7)], [0, 1], 'S1'); eq(T['S1']['val'], [0, 1], 'S1 val')
    eq([v['cols'] for v in T['S1']['visuals']], [6, 7], 'S1 pictures show 6 and 7 counters')
    eq([kind(k).capitalize() for k in (4, 9, 10, 13)], ['Even', 'Odd', 'Even', 'Odd'], 'S2'); eq(T['S2']['val'], ['Even', 'Odd', 'Even', 'Odd'], 'S2 val')
    eq([last_digit(k) for k in range(2, 21, 2)], [2, 4, 6, 8, 0, 2, 4, 6, 8, 0], 'S3 last digits of the 2s'); eq(sorted(set(last_digit(k) for k in range(2, 21, 2))), [0, 2, 4, 6, 8], 'S3 set')
    eq(T['S3']['val'], [0], 'S3 val')
    opts = [int(o) for o in T['S4']['mcq']['options']]
    eq([i for i, o in enumerate(opts, 1) if kind(o) == 'even'], [3], 'S4 one even option'); eq(T['S4']['val'], [3], 'S4 val')
    eq((left_over(11), pairs(11), kind(11)), (1, 5, 'odd'), 'S5'); eq(T['S5']['visual']['cols'], 11, 'S5 picture'); eq(T['S5']['val'], [1, 'Odd'], 'S5 val')
    truth = [kind(6) == 'even', kind(9) == 'even', kind(15) == 'odd', kind(20) == 'odd']
    eq(truth, [True, False, True, False], 'S6'); eq(['T' if t else 'F' for t in truth], T['S6']['val'], 'S6 val')
    eq([r['s'] for r in T['S6']['tf']], ['6 is even.', '9 is even.', '15 is odd.', '20 is odd.'], 'S6 statements match the truth list')
    # ---- Think harder: test the claims by enumeration
    t1 = [tuple(int(x) for x in p['text'].split('=')[0].split('+')) for p in T['T1']['parts'][:3]]; eq(t1, [(6, 5), (10, 3), (8, 1)], 'T1 sums as printed')
    eq([total(*x) for x in t1], [11, 13, 9], 'T1 totals'); eq([kind(total(*x)) for x in t1], ['odd'] * 3, 'T1 kinds'); eq([kind(a) == 'odd' for a, b in t1].count(True) + [kind(b) == 'odd' for a, b in t1].count(True), 3, 'T1 each sum is one odd and one even')
    eq(set(t1) & {(3, 4), (5, 8), (7, 2)}, set(), 'T1 shares no sum with the class table')
    claim_odd_even = all(kind(a + b) == 'odd' for a in range(1, 40) for b in range(1, 40) if kind(a) == 'odd' and kind(b) == 'even'); eq(claim_odd_even, True, 'T1 claim holds for all pairs up to 39')
    eq(T['T1']['val'], [11, 'Odd', 13, 'Odd', 9, 'Odd', 'Yes'], 'T1 val')
    eq([kind(k).capitalize() for k in (57, 80, 34, 91)], ['Odd', 'Even', 'Even', 'Odd'], 'T2'); eq(T['T2']['val'], ['Odd', 'Even', 'Even', 'Odd'], 'T2 val')
    eq(total(9, 3), 12, 'T3 total'); eq(kind(12), 'even', 'T3 total is even so the claim fails'); eq(T['T3']['parts'][0]['text'], '9 + 3 = [2]', 'T3 sum as printed'); odd_odd_odd = [a + b for a in range(1, 30) for b in range(1, 30) if kind(a) == 'odd' and kind(b) == 'odd' and kind(a + b) == 'odd']
    eq(odd_odd_odd, [], 'T3(c) odd + odd is never odd'); eq(T['T3']['val'], [12, 'No', 'Never'], 'T3 val')
    eq([two_odds(12), two_odds(15), two_odds(20)], [True, False, True], 'T4'); eq(T['T4']['val'], ['Yes', 'No', 'Yes'], 'T4 val')
    eq((5 + 7, 9 + 11), (12, 20), 'T4 example pairs')
    # ---- Go further
    eq((left_over(3), left_over(5), pairs(3), pairs(5), left_over(total(3, 5))), (1, 1, 1, 2, 0), 'G1'); eq(T['G1']['val'], [1, 1, 1], 'G1 val')
    eq([total(3, 5, 7), total(1, 1, 1), total(9, 3, 5)], [15, 3, 17], 'G2 totals'); eq([kind(15), kind(3), kind(17)], ['odd'] * 3, 'G2 kinds')
    all3 = all(kind(a + b + c) == 'odd' for a in range(1, 20) for b in range(1, 20) for c in range(1, 20) if kind(a) == kind(b) == kind(c) == 'odd'); eq(all3, True, 'G2 odd+odd+odd always odd up to 19')
    eq(T['G2']['val'], [15, 'Odd', 3, 'Odd', 17, 'Odd', 'Odd'], 'G2 val')
    eq((left_over(4), left_over(8), total(4, 8), kind(12)), (0, 0, 12, 'even'), 'G3'); eq(T['G3']['val'][0], 0, 'G3 val')
    ee = all(kind(a + b) == 'even' for a in range(2, 40, 2) for b in range(2, 40, 2)); eq(ee, True, 'G3 even + even always even')
    # Investigation: a number plus the next number
    eq([kind(total(a, a + 1)) for a in (3, 5, 8, 10)], ['odd'] * 4, 'Investigation'); eq([total(a, a + 1) for a in (3, 5, 8, 10)], [7, 11, 17, 21], 'Investigation totals')
    eq(all(kind(a + a + 1) == 'odd' for a in range(1, 60)), True, 'Investigation always odd up to 59')
    # ---- Exit ticket, home practice
    eq(kind(17), 'odd', 'E1'); eo = [int(o) for o in X['E2']['mcq']['options']]; eq([i for i, o in enumerate(eo, 1) if kind(o) == 'even'], [3], 'E2'); eq(two_odds(14), True, 'E3'); eq(7 + 7, 14, 'E3 example')
    eq([X['E1']['val'], X['E2']['val'], X['E3']['val']], [['Odd'], [3], ['Yes']], 'exit vals')
    eq([kind(8), kind(15), kind(20)], ['even', 'odd', 'even'], 'H1'); eq(left_over(13), 1, 'H2'); eq(H['H3']['val'], [6, 8], 'H3')
    eq(sorted(set(last_digit(k) for k in range(0, 100, 2))), [0, 2, 4, 6, 8], 'H3 even last digits')
    eq([total(5, 6), kind(11), total(7, 9), kind(16)], [11, 'odd', 16, 'even'], 'H4'); eq(9 + 11, 20, 'H5 example'); eq(15 + 15, 30, 'H5 example 2'); eq(all(kind(k) == 'odd' for k in (9, 11, 15)), True, 'H5 odd numbers')
    # ---- sneak-peek, warm-up, slides
    eq(left_over(7), 1, 'sneak 1'); eq(d['sneak_peek']['val1'], 1, 'sneak 1 val'); eq((total(5, 7), left_over(total(5, 7)), pairs(total(5, 7))), (12, 0, 6), 'sneak 2')
    eq([left_over(k) for k in (8, 5, 10, 7)], [0, 1, 0, 1], 'warm-up 1'); eq([k + 2 for k in (10, 16)] + [8 - 2], [12, 18, 6], 'warm-up 2'); eq([last_digit(k) for k in (38, 63, 90)], [8, 3, 0], 'warm-up 3')
    eq([kind(k) for k in (6, 7, 8, 9, 10)], ['even', 'odd', 'even', 'odd', 'even'], 'explore'); eq([kind(total(3, 5)), kind(total(3, 4)), kind(total(4, 6))], ['even', 'odd', 'even'], 'explore sums')
    eq([kind(total(4, 9)), kind(total(6, 8)), kind(total(7, 5)), kind(total(12, 3))], ['odd', 'even', 'even', 'odd'], 'mini your turn'); eq([total(4, 9), total(6, 8), total(7, 5), total(12, 3)], [13, 14, 12, 15], 'mini totals')
    eq([kind(k) for k in (4, 7, 10, 13, 16, 19)], ['even', 'odd', 'even', 'odd', 'even', 'odd'], 'break')
    eq(kind(57), 'odd', 'mini 57'); eq(two_odds(15), False, 'optional slide'); eq([total(7, 7), total(5, 9), total(7, 9)], [14, 14, 16], 'optional table')
    eq(total(4, 6) == 10 and kind(total(12, 8)) == 'even' and kind(total(10, 10)) == 'even', True, 'spare M1')
    sl = {s['id']: s for s in d['slides']}
    cols = [b for b in sl['s-m4']['blocks'] if b['t'] == 'cols'][0]['cols']; eq([c[0]['cols'] for c in cols], [3, 5], 's-m4 pictures')
    cols = [b for b in sl['s-sneakans']['blocks'] if b['t'] == 'cols'][0]['cols']; eq([c[0]['cols'] for c in cols], [5, 7], 's-sneakans pictures')
    eq(sl['s-rem2']['blocks'][0]['shade'], [k for k in range(1, 21) if left_over(k) == 0], 's-rem2 shaded cells are the 2s')
    return n
