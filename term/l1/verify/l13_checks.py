"""Independent checks for Level 1 Term 2 Lesson 13 (Doubles and Near Doubles).
Every answer is recomputed from first principles: doubles by laying two equal piles of counters and counting them, near doubles by
adding or removing one counter, tens by counting bars. ORACLES drive the practice-template checks."""
import re


def pile(n):                       # n counters
    return ['o'] * n


def total(*piles):                 # count counters in several piles laid together
    return len([c for p in piles for c in p])


def double(n):                     # two equal piles, counted
    return total(pile(n), pile(n))


def near_up(n):                    # double n then one more counter
    return total(pile(n), pile(n), pile(1))


def near_down(n):                  # double n then one counter taken off
    p = pile(n) + pile(n)
    p.pop()
    return len(p)


def bars(k):                       # k tens bars, each a stack of ten squares
    return [[1] * 10 for _ in range(k)]


def tens_total(*stacks):           # count the squares in several piles of bars
    return sum(len(r) for s in stacks for r in s)


def sum_by_counting(nums):         # lay out every pile and count
    return len([c for n in nums for c in pile(n)])


ORACLES = {
    'c1': lambda e: total(pile(e['n']), pile(e['n'])),
    'c2': lambda e: double(e['n']),
    'c3': lambda e: tens_total(bars(e['n']), bars(e['n'])),
    'c5': lambda e: total(pile(e['n']), pile(e['n'])),
    'c6': lambda e: {'a': e['a'], 'b': e['a'], 'c': total(pile(e['a']), pile(e['a']))},
    't1': lambda e: near_up(e['a']),                      # a + (a+1): double a, one more counter
    't2': lambda e: near_down(e['a']),                    # a + (a-1): double a, one counter off
    't4': lambda e: sum_by_counting([e['a'], e['a'] + 1]),
    'g1': lambda e: sum_by_counting([e['m'], e['m'] + 1, e['m'], e['m'] - 1, e['m']]),
    'g2': lambda e: sum_by_counting([e['m'] - 1, e['m'], e['m'] + 1]),
    'g3': lambda e: sum_by_counting([e['n'], e['n']]),
}
BASE_ENV = {'c1': {'n': 6}, 'c2': {'n': 7}, 'c3': {'n': 2}, 'c5': {'n': 8}, 't1': {'a': 7}, 't2': {'a': 9}, 't4': {'a': 6}, 'g1': {'m': 8}, 'g2': {'m': 20}, 'g3': {'n': 35}}


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
    s1 = [p for p in T['S1']['visuals']]
    eq([v['left'] for v in s1], [v['right'] for v in s1], 'S1 every domino is a double (both halves equal)')
    eq([double(v['left']) for v in s1], [6, 8, 10], 'S1 totals'); eq(T['S1']['val'], [6, 8, 10], 'S1 val')
    eq([p['val'] for p in T['S1']['parts']], [3 + 3, 4 + 4, 5 + 5], 'S1 parts')
    v = T['S2']['visual']; eq(v['filled'][0], 6, 'S2 red'); eq(v['extra'][1], 6, 'S2 yellow')
    eq(total(pile(v['filled'][0]), pile(v['extra'][1])), 12, 'S2 total'); eq(T['S2']['val'], [12, 12], 'S2 val')
    eq([double(k) for k in (2, 5, 7, 9)], [4, 10, 14, 18], 'S3'); eq(T['S3']['val'], [4, 10, 14, 18], 'S3 val')
    vs = T['S4']['visuals']; eq([x['tens'] for x in vs], [3, 3], 'S4 bars')
    eq(tens_total(bars(3), bars(3)) // 10, 6, 'S4 tens'); eq(tens_total(bars(3), bars(3)), 60, 'S4 number'); eq(tens_total(bars(4), bars(4)), 80, 'S4 double 40')
    eq(T['S4']['val'], [6, 60, 80], 'S4 val')
    items = T['S5']['visual']['items']; eq([i['n'] for i in items], [8, 8], 'S5 picture 8 and 8'); eq(sum_by_counting([i['n'] for i in items]), 16, 'S5 total'); eq(T['S5']['val'], [8, 8, 16, 16], 'S5 val')
    # S6: evaluate every statement from its text
    truth = []
    for r in T['S6']['tf']:
        s = r['s']
        m = re.fullmatch(r'Double (\d+) is (\d+)\.', s)
        if m:
            k = int(m.group(1))
            truth.append((double(k) if k < 10 else tens_total(bars(k // 10), bars(k // 10))) == int(m.group(2)))
            continue
        m = re.fullmatch(r'(\d+) \+ (\d+) is a double\.', s)
        if m: truth.append(int(m.group(1)) == int(m.group(2))); continue
        raise AssertionError('S6 unparsed ' + s)
    eq(truth, [True, False, True, True], 'S6 truth'); eq(['T' if t else 'F' for t in truth], T['S6']['val'], 'S6 val')
    eq(len(T['S6']['tf']), 4, 'S6 rows')
    # ---- Think harder
    v = T['T1']['visual']; eq((v['filled'][0], v['extra'][1]), (7, 8), 'T1 picture')
    eq(double(7), 14, 'T1a'); eq(near_up(7), 15, 'T1b by one more counter'); eq(sum_by_counting([7, 8]), 15, 'T1b by counting'); eq(T['T1']['val'], [14, 15], 'T1 val')
    eq([near_up(6), near_up(8), near_up(4), near_up(9)], [13, 17, 9, 19], 'T2'); eq(T['T2']['val'], [13, 17, 9, 19], 'T2 val')
    eq([sum_by_counting([a, b]) for a, b in ((6, 7), (8, 9), (4, 5), (9, 10))], [13, 17, 9, 19], 'T2 by counting')
    opts = T['T3']['mcq']['options']
    pairs = [[int(x) for x in o.split('+')] for o in opts]
    near = [i for i, (a, b) in enumerate(pairs, 1) if abs(a - b) == 1]
    notnear = [i for i in range(1, 5) if i not in near]
    eq(notnear, [3], 'T3 only 5 + 8 is not a near double'); eq(T['T3']['val'], [3], 'T3 val')
    eq(16 - 1 == sum_by_counting([8, 9]), False, 'T4 Kumar is wrong'); eq(sum_by_counting([8, 9]), 17, 'T4 right answer'); eq(near_up(8), 17, 'T4 by double + 1'); eq(T['T4']['val'], ['No', 17], 'T4 val')
    # ---- Go further
    eq(sum_by_counting([8, 9, 8, 7, 8]), 40, 'G1'); eq(sum_by_counting([8] * 5), 40, 'G1 five eights'); eq(8 + 8 + 9 + 7 + 8, 40, 'G1 pairs'); eq(T['G1']['val'], [40], 'G1 val')
    eq(sum_by_counting([9, 10, 11]) == sum_by_counting([10, 10, 10]), True, 'G2a'); eq(sum_by_counting([19, 20, 21]), 60, 'G2b'); eq(T['G2']['val'], ['Yes', 60], 'G2 val')
    eq([sum_by_counting([30, 30]), sum_by_counting([5, 5]), sum_by_counting([35, 35])], [60, 10, 70], 'G3'); eq(60 + 10, 70, 'G3 parts add'); eq(T['G3']['val'], [60, 10, 70], 'G3 val')

    # Investigation: can two piles be made equal by moving counters? only when the total can be split into two equal piles
    def can_match(a, b):
        for move in range(0, a + b + 1):
            if a - move == b + move or a + move == b - move: return True
        return False
    eq([can_match(6, 8), can_match(5, 9), can_match(7, 8)], [True, True, False], 'Investigation')
    eq([a + b for a, b in ((6, 8), (5, 9), (7, 8))], [14, 14, 15], 'Investigation totals')
    # ---- Exit ticket and home practice
    eq([X['E1']['val'][0], X['E2']['val'][0], X['E3']['val'][0]], [double(9), tens_total(bars(3), bars(3)), sum_by_counting([9, 8])], 'exit')
    eq([X['E1']['val'][0], X['E2']['val'][0], X['E3']['val'][0]], [18, 60, 17], 'exit literal')
    eq(H['H1']['val'], [double(4), double(6), double(8)], 'H1'); eq(H['H2']['val'], double(7), 'H2')
    eq(H['H3']['val'], [tens_total(bars(2), bars(2)), tens_total(bars(4), bars(4))], 'H3'); eq(H['H4']['val'], [near_up(6), near_up(9)], 'H4')
    eq(sum_by_counting([7, 8, 7, 6, 7]), 35, 'H5'); eq(H['H5']['val'], 35, 'H5 val')
    # ---- sneak-peek, talk, warm-up and slides
    eq(total(pile(4), pile(4)), 8, 'sneak 1'); eq(d['sneak_peek']['val1'], 8, 'sneak 1 val'); eq(near_up(6), 13, 'sneak 2 is 6 + 6 and one more'); eq(double(6), 12, 'sneak 2 base')
    eq((double(7) + 1, near_down(8)), (15, 15), 'talk: Mei double 7 and 1, Ali double 8 less 1'); eq(sum_by_counting([7, 8]), 15, 'talk total')
    eq([10 - k for k in (7, 4, 9, 6, 8)], [3, 6, 1, 4, 2], 'warm-up 1')
    eq([tens_total(bars(k), bars(k)) for k in (3, 2, 4)], [60, 40, 80], 'warm-up 2')
    eq([5 + 3, 4 + 4], [8, 8], 'warm-up 3 plates'); eq([6 + 2 - 5, 7 + 1 - 6, 5 + 3 - 4], [3, 2, 4], 'warm-up 3 missing numbers')
    eq([double(k) for k in range(1, 11)], [2, 4, 6, 8, 10, 12, 14, 16, 18, 20], 'doubles table')
    eq([double(k) - 10 for k in (6, 7, 8, 9)], [2, 4, 6, 8], 'double as ten and ...')
    eq([double(k) for k in (2, 3, 4, 5, 6)], [4, 6, 8, 10, 12], 'break stomps')
    eq(double(9), 10 + 8, 'optional slide double 9 is 10 and 8')
    eq([near_up(k) for k in (4, 9, 12)], [9, 19, 25], 'spare M1 near doubles')
    # the ten-frame pictures on the slides show what they say
    sl = {s['id']: s for s in d['slides']}
    for sid, want in (('s-m3', (7, 8)), ('s-explore1', (3, 3))):
        for b in sl[sid]['blocks']:
            if b.get('type') == 'ten_frame':
                eq((b['filled'][0], b['extra'][1]), want, sid + ' picture')
    cols = [b for b in sl['s-m3b']['blocks'] if b['t'] == 'cols'][0]['cols']
    eq([(c[0]['filled'][0], c[0]['extra'][1]) for c in cols], [(7, 7), (8, 8)], 's-m3b pictures are doubles')
    eq(8 + 8, 16, 's-m3b double 8'); eq(near_down(8), 15, 's-m3b 7 + 8 as double 8 less 1')
    return n
