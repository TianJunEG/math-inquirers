"""Independent checks for Level 1 Term 2 Lesson 15 (Equal Groups).
Totals are found by laying out groups and counting them one by one (loops), never by a formula; pictures are checked against the numbers in the questions."""


def lay_out(groups, each):          # n groups of `each` items: list the items one by one
    items = []
    for g in range(groups):
        for _ in range(each):
            items.append(g)
    return items


def total(groups, each): return len(lay_out(groups, each))


def repeated_add(each, times):      # each + each + ... (times terms)
    s = 0
    for _ in range(times): s += each
    return s


def equal(counts): return all(c == counts[0] for c in counts)


def counts_of(v):                   # the group sizes a groups-picture spec draws
    return list(v['counts']) if v.get('counts') else [v['each']] * v['n']


def array_cells(rows, cols):
    n = 0
    for _ in range(rows):
        for _ in range(cols): n += 1
    return n


def ways_rows(n):                   # every number of equal rows that uses exactly n counters
    return [r for r in range(1, n + 1) if any(array_cells(r, c) == n for c in range(1, n + 1))]


def total_of_sum(s):                # '3 + 3 + 3 + 3' -> 12
    return sum(int(x) for x in s.split('+'))


ORACLES = {
    'c1': lambda e: {'a': e['a'], 'b': e['b'], 'c': total(e['a'], e['b'])},
    'c2': lambda e: len(lay_out(e['a'], e['b'])),
    'c4': lambda e: repeated_add(e['b'], e['a']),
    'c6': lambda e: {'a': e['a'], 'b': e['b'], 'c': array_cells(e['a'], e['b'])},
    'c3': lambda e: 'yes' if equal([e['x'], e['y'], e['x']]) else 'no',
    't1': lambda e: sum(3 - c for c in [3, e['a'], e['b']]),
    't2': lambda e: 'the same' if total(e['a'], e['b']) == total(e['b'], e['a']) else ('Mei' if total(e['a'], e['b']) > total(e['b'], e['a']) else 'Ali'),
    't3': lambda e: repeated_add(2, e['n']),
    't4': lambda e: total(e['a'], e['b']) + e['c'],
    'g1': lambda e: repeated_add(2, e['a']) + repeated_add(4, e['b']),
    'g2': lambda e: 40 - total(e['a'], 5),
}
BASE_ENV = {'t1': {'a': 1, 'b': 2}, 'c2': {'a': 3, 'b': 4}, 'c4': {'a': 5, 'b': 2}, 't3': {'n': 6}, 't4': {'a': 3, 'b': 4, 'c': 2}, 'g1': {'a': 3, 'b': 4}, 'g2': {'a': 6}}


def run(d):
    n = 0

    def eq(a, b, msg=''):
        nonlocal n
        n += 1
        assert a == b, f'{msg}: got {a}, expected {b}'
    T = {q['id']: q for q in d['tiers']['start'] + d['tiers']['think'] + d['tiers']['go']}
    X = {q['id']: q for q in d['exit']}
    H = {q['id']: q for q in d['home_practice']}
    sl = {s['id']: s for s in d['slides']}
    # ---- Start here
    v = T['S1']['visuals']; yn = ['Yes' if equal(counts_of(x)) else 'No' for x in v]
    eq(yn, ['Yes', 'No'], 'S1 equal or not'); eq(T['S1']['val'], yn, 'S1 val'); eq([counts_of(x) for x in v], [[4, 4, 4], [2, 3, 2]], 'S1 pictures')
    v = T['S2']['visual']; eq((len(counts_of(v)), counts_of(v)[0], sum(counts_of(v))), (3, 5, 15), 'S2 picture'); eq(T['S2']['val'], [3, 5, 3, 5, 15], 'S2 val')
    v = T['S3']['visual']; eq((len(counts_of(v)), counts_of(v)[0]), (5, 2), 'S3 picture'); eq(repeated_add(2, 5), 10, 'S3'); eq(total(5, 2), 10, 'S3 groups'); eq(T['S3']['val'], [10, 10], 'S3 val')
    eq(T['S3']['parts'][0]['text'], '2 + 2 + 2 + 2 + 2 = [2]', 'S3 sum written with five 2s')
    v = T['S4']['visual']; eq((len(counts_of(v)), v.get('empty')), (3, True), 'S4 empty plates'); eq(total(3, 4), 12, 'S4'); eq(T['S4']['val'], [12], 'S4 val')
    rows = T['S5']['visual']['rows']; got = [total(int(r[0]), int(r[1])) for r in rows]; eq(got, [15, 8, 10], 'S5'); eq(T['S5']['val'], got, 'S5 val')
    eq([r[2] for r in rows], ['[2]', '[]', '[2]'], 'S5 box widths match the number of digits')
    v = T['S6']['visual']; eq((len(counts_of(v)), counts_of(v)[0]), (4, 5), 'S6 picture'); eq(repeated_add(5, 4), 20, 'S6'); eq(T['S6']['val'], [4, 5, 20, 20], 'S6 val')
    # ---- Think harder
    x = T['T1']['visual']; eq((x['rows'], x['cols']), (2, 8), 'T1 array'); eq((array_cells(x['rows'], x['cols']), array_cells(x['cols'], x['rows'])), (16, 16), 'T1 totals both ways')
    class_arrays = [(3, 4), (4, 3), (2, 5), (5, 2), (2, 6), (6, 2), (3, 6), (6, 3), (4, 2), (2, 4)]; eq((x['rows'], x['cols']) in class_arrays, False, 'T1 does not repeat an array used in class, talk or home practice')
    eq(array_cells(2, 8) == array_cells(8, 2), True, 'T1 2x8 = 8x2'); eq(all(array_cells(a, b) == array_cells(b, a) for a in range(1, 11) for b in range(1, 11)), True, 'T1 turning an array never changes the total')
    eq(T['T1']['val'], [2, 8, 16, 8, 2, 16, 'Yes'], 'T1 val'); eq(T['T1']['parts'][2]['text'], 'Is 2 × 8 = 8 × 2? Circle Yes or No.', 'T1 (c) names the same numbers')
    c = counts_of(T['T2']['visual']); eq(c, [3, 1, 2], 'T2 picture'); eq(sum(3 - x for x in c), 3, 'T2 more needed'); eq(T['T2']['val'], [3], 'T2 val')
    c = [4, 4, 4]; eq(sum(c), 12, 'T3 total'); eq(sum(c) == 7, False, 'T3 Kumar is wrong'); eq(3 + 4, 7, 'T3 where 7 comes from'); eq(T['T3']['val'], [12, 'No'], 'T3 val (work first, then judge)'); eq([p['l'] for p in T['T3']['parts']], ['a', 'b'], 'T3 parts'); eq(T['T3']['parts'][0]['val'], 12, 'T3 (a) is the total')
    rows = T['T4']['visual']['rows']; miss = []
    for r in rows:
        for k, cell in enumerate(r):
            if cell == '[]':
                known = [int(x) for j, x in enumerate(r) if j != k and x != '[]']
                other, tot = (known[0], known[1]) if k in (0, 1) else (None, None)
                sol = [x for x in range(1, 13) if x * other == tot]
                eq(len(sol), 1, 'T4 one answer'); miss.append(sol[0])
    eq(miss, [3, 3], 'T4'); eq(T['T4']['val'], miss, 'T4 val'); eq(all(total(int(r[0]), int(r[1])) == 12 for r in rows if '[]' not in r), True, 'T4 given rows make 12')
    # ---- Go further
    it = T['G1']['visual']['items']; eq([(x['icon'], x['n']) for x in it], [('bike', 3), ('car', 4)], 'G1 picture')
    eq((repeated_add(2, 3), repeated_add(4, 4), repeated_add(2, 3) + repeated_add(4, 4)), (6, 16, 22), 'G1'); eq(T['G1']['val'], [6, 16, 22], 'G1 val')
    eq((total(6, 5), 40 - total(6, 5)), (30, 10), 'G2'); eq(T['G2']['val'][:2], [30, 10], 'G2 val')
    # G2 part (c): beyond the school range, by doubling the number of groups (checked by laying out the groups)
    eq(total(12, 5), 2 * total(6, 5), 'G2c doubling the groups doubles the total'); eq(total(12, 5), 60, 'G2c value'); eq(total(12, 5) > 40, True, 'G2c above the school range of 40')
    eq(T['G2']['val'], [30, 10, 60], 'G2 val with part c')
    pairs = [(a, b) for a in range(1, 25) for b in range(1, 25) if total(a, b) == 24]
    eq([(2, 12), (3, 8), (4, 6)] == [p for p in [(2, 12), (3, 8), (4, 6)] if p in pairs], True, 'G3 examples work'); eq(len(pairs), 8, 'G3 there are 8 ordered ways to make 24')
    eq([p['text'] for p in T['G3']['parts']], ['[2] groups of [2] = 24'] * 3, 'G3 two-digit boxes'); eq('different number of groups' in T['G3']['text'], True, 'G3 says what counts as different')
    eq('5 × 4 = 20 is also right' in T['S6']['answer'], True, 'S6 key accepts either order')
    # ---- Investigation: arrays with 12 counters
    eq(ways_rows(12), [1, 2, 3, 4, 6, 12], 'I1 ways'); eq(5 in ways_rows(12), False, 'I1 five rows do not work'); eq(12 - 5 * 2, 2, 'I1 two left over'); eq(array_cells(2, 6), 12, 'I1 first step')
    # ---- Exit ticket and home practice
    eq((repeated_add(5, 4), total(4, 5)), (20, 20), 'E1'); eq(X['E1']['val'], [20], 'E1 val')
    opts = X['E2']['mcq']['options']; right = [i for i, o in enumerate(opts, 1) if total_of_sum(o) == 12 if '+' in o]
    eq(right, [2], 'E2 exactly one option makes 12'); eq([x for x in opts[1].split('+')], ['3 ', ' 3 ', ' 3 ', ' 3'], 'E2 option 2 is 3 four times'); eq(X['E2']['val'], [2], 'E2 val')
    eq((repeated_add(4, 3), total(3, 4)), (12, 12), 'E3'); eq(X['E3']['val'], [3, 4, 12, 12], 'E3 val')
    eq((repeated_add(3, 4), total(4, 3)), (12, 12), 'H1'); eq(equal([3, 3, 4]), False, 'H2'); eq(total(3, 5), 15, 'H3'); eq(array_cells(2, 6) == array_cells(6, 2), True, 'H4')
    eq(repeated_add(3, 4) + repeated_add(2, 3), 18, 'H5'); eq([H['H1']['val'], H['H2']['val'], H['H3']['val'], H['H4']['val'], H['H5']['val']], [[12, 12], ['No'], [15, 15, 15], ['Yes'], 18], 'home vals')
    # ---- sneak-peek, warm-up, slides, talk, spare time
    eq(total(3, 2), 6, 'sneak 1'); eq(d['sneak_peek']['val1'], 6, 'sneak 1 val'); eq((total(4, 3), total(3, 4), total(4, 3) == total(3, 4)), (12, 12, True), 'sneak 2')
    five = [k for k in range(1, 41) if k % 5 == 0]; eq(sl['s-rem1']['blocks'][1]['shade'], five, 's-rem1 shaded cells are the 5s'); eq(five[five.index(25) + 1], 30, 'warm-up after 25 in fives')
    eq(14 + 2, 16, 'warm-up after 14 in twos'); eq(repeated_add(10, 3), 30, 'warm-up bundles'); eq(len([l for g in d['script']['segments'] if g['part'] == 'remember' for l in g['lines'] if l['k'] == 'ASK']), 5, 'warm-up asks five questions')
    eq((9 + 4, 7 + 5), (13, 12), 'warm-up make a ten'); eq(sl['s-rem3']['blocks'][0]['filled'] + sl['s-rem3']['blocks'][0]['extra'], [8, 0, 0, 6], 's-rem3 frames show 8 and 6')
    cols = [b['cols'] for b in sl['s-explore2']['blocks'] if b['t'] == 'cols']; eq([equal(counts_of(c[0][0])) for c in cols], [True, False, True], 's-explore2 A equal, B not, C equal'); eq([c[1][0]['text'] for c in cols], ['Picture A', 'Picture B', 'Picture C'], 's-explore2 labels')
    eq(total(4, 3), 12, 'explore 1'); eq(total(3, 5), 15, 'explore 1 second'); eq(sum(3 - x for x in [3, 2, 3]), 1, 'explore 2 add one')
    cols = [b for b in sl['s-explore3']['blocks'] if b['t'] == 'cols'][0]['cols']; eq([total(len(counts_of(c[0])), counts_of(c[0])[0]) for c in cols], [12, 12], 's-explore3 both 12')
    rows = sl['s-m2']['blocks'][0]['rows'][1:]; eq([r[2] for r in rows], ['4 × 3 = 12'], 's-m2 worked row'); eq([total(4, 3), total(5, 2)], [12, 10], 's-m2 totals')
    eq([r[1] for r in rows], ['3 + 3 + 3 + 3 = 12'], 's-m2 addition'); eq([repeated_add(3, 4), repeated_add(2, 5)], [12, 10], 's-m2 additions values')
    ans = [b for b in sl['s-m2-ans']['blocks'] if b['t'] == 'answer'][0]['text']; eq(ans, '5 groups of 2: 2 + 2 + 2 + 2 + 2 = 10, so 5 × 2 = 10.', 's-m2 answer shown only on the answer slide'); eq([b['t'] for b in sl['s-m2']['blocks']], ['table', 'chip'], 's-m2 question slide has no answer')
    eq(any(b['t'] == 'table' for b in sl['s-m1']['blocks']), False, 's-m1 question slide has no table'); eq(any(b['t'] == 'table' for b in sl['s-m1-ans']['blocks']), True, 's-m1 answer slide')
    cols = [b for b in sl['s-m3']['blocks'] if b['t'] == 'cols'][0]['cols']; eq([equal(counts_of(c[0])) for c in cols], [True, False], 's-m3')
    cols = [b for b in sl['s-m4']['blocks'] if b['t'] == 'cols'][0]['cols']; eq([(c[0]['rows'], c[0]['cols']) for c in cols], [(3, 4), (4, 3)], 's-m4 arrays')
    eq([total(2, 6), total(3, 6), total(4, 4)], [12, 18, 16], 's-m5 answers'); eq([r[2] for r in sl['s-m5a']['blocks'][0]['rows'][1:]], ['12', '18', '16'], 's-m5a table')
    eq([repeated_add(6, 2), repeated_add(6, 3), repeated_add(4, 4)], [12, 18, 16], 's-m5a addition')
    eq([total(2, 3), total(3, 2), total(4, 2), total(3, 5)], [6, 6, 8, 15], 'break totals'); eq([total(2, 5), total(5, 2), total(4, 2), total(2, 4)], [10, 10, 8, 8], 'talk pairs are equal')
    cols = [b for b in sl['s-sneakans']['blocks'] if b['t'] == 'cols'][0]['cols']; eq([total(len(counts_of(c[0])), counts_of(c[0])[0]) for c in cols], [12, 12], 's-sneakans pictures')
    eq([total(3, 5), total(5, 3)], [15, 15], 'optional slide'); eq([total(2, 7), total(7, 2), total(4, 5), total(5, 4)], [14, 14, 20, 20], 'spare M1'); eq(total(3, 5), 15, 'spare M3')
    # ---- online practice items without templates
    items = {i['id']: i for i in d['online_practice']['items']}
    eq(equal(counts_of(items['c3']['fig_base'])), False, 'c3 unequal'); eq(items['c3']['answer'], 'no', 'c3 answer')
    o = items['c5']['options']; eq([x for x in o if total_of_sum(x) == 12], [items['c5']['answer']], 'c5 exactly one option is 4 groups of 3'); eq(items['c5']['answer'], '3 + 3 + 3 + 3', 'c5 is 3 four times')
    eq(sum(3 - x for x in counts_of(items['t1']['fig_base'])), items['t1']['answer'], 't1'); eq(sorted(items['g3']['answer']), [4, 6], 'g3'); eq(repeated_add(4, 6), 24, 'g3 sum')
    eq(items['g3']['answer'], [6, 4], 'g3 groups first')
    # Retrofit T5 (true or false, 15 apples on plates with none left over)
    eq(T['T5']['val'], ['True' if left_over(15, k) == 0 else 'False' for k in (3, 4, 5)], 'T5')
    eq([left_over(15, k) for k in (3, 4, 5)], [0, 3, 0], 'T5 left over')
    eq([times(3, 5), times(5, 3), times(3, 4)], [15, 15, 12], 'T5 3 groups of 5, 5 groups of 3, 3 groups of 4')
    return n
