"""Independent checks for Level 1 Term 2 Lesson 18 (Times Stories).
Totals are found by laying out the boxes one by one (loops) and by acting out each story step by step; no multiplication formula is used for the answers.
Every strip picture is checked: the cells of a strip must add up to its length, and the strip must match the story it illustrates."""


def lay_out(groups, each):
    """n boxes with `each` in every box: the list of items, one at a time."""
    items = []
    for g in range(groups):
        for _ in range(each):
            items.append(g)
    return items


def total(groups, each): return len(lay_out(groups, each))


def twice(n): return n + n                    # twice as many = two equal strips
def times_as_many(k, n):                      # k times as many = k equal strips
    s = 0
    for _ in range(k): s += n
    return s


def cells(bar):
    """The cell sizes a strip draws, in order."""
    return [s['v'] for s in bar['segments']] if bar.get('segments') else [bar['len']]


def equal(c): return all(x == c[0] for x in c)


def transfer_to_equal(a, b):
    """Give one card at a time from the bigger pile to the smaller until the piles are equal. Returns how many cards moved."""
    moved = 0
    while a > b:
        a -= 1; b += 1; moved += 1
    assert a == b, 'the piles never become equal'
    return moved


def unit_value(total_amount, boxes):
    """The number in each of `boxes` equal boxes that make `total_amount`, found by trying 1, 2, 3 ..."""
    for v in range(1, total_amount + 1):
        if total(boxes, v) == total_amount: return v
    return None


ORACLES = {
    'c1': lambda e: {'a': e['a'], 'b': e['b'], 'c': total(e['a'], e['b'])},
    'c2': lambda e: total(e['a'], e['b']),
    'c3': lambda e: total(e['a'], e['b']) + e['c'],
    'c4': lambda e: total(e['a'], e['b']) - e['c'],
    't1': lambda e: twice(e['m']),
    't2': lambda e: e['m'] + twice(e['m']),
    't4': lambda e: transfer_to_equal(twice(e['m']), e['m']),
    'g1': lambda e: total(e['a'], 3) + total(e['c'], 2) + e['r'],
    'g2': lambda e: e['m'] + times_as_many(3, e['m']),
    'g3': lambda e: unit_value(4 * e['k'], 1 + 3),
}
BASE_ENV = {'c2': {'a': 3, 'b': 5}, 'c3': {'a': 3, 'b': 5, 'c': 2}, 'c4': {'a': 4, 'b': 3, 'c': 2}, 't1': {'m': 6}, 't2': {'m': 6}, 't4': {'m': 12}, 'g1': {'a': 4, 'c': 5, 'r': 4}, 'g2': {'m': 7}, 'g3': {'k': 6}}


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

    def strip_ok(b, msg):                                   # the cells of every strip add up to its drawn length
        eq(sum(cells(b)), b['len'], msg + ': cells add up to the strip length')

    # ---- Start here
    v = T['S1']['visual']; b = v['bars'][0]; eq((v['units']['n'], b['len'] // v['units']['n']), (3, 5), 'S1 strip is 3 boxes of 5'); eq(total(3, 5), 15, 'S1'); eq(T['S1']['val'], [5, 5, 5, 15], 'S1 val')
    eq(b['len'], total(3, 5), 'S1 strip length is the total'); eq(T['S1']['parts'][0]['text'], 'Mei has [2] sweets in all.', 'S1 two-digit box')
    eq(total(4, 3), 12, 'S2'); eq(T['S2']['text'].startswith('Ben has 4 boxes. Each box has 3 pencils.'), True, 'S2 story'); eq(T['S2']['val'], [4, 3, 12, 12], 'S2 val')
    bars = T['S3']['visual']['bars']; [strip_ok(x, 'S3 ' + x['name']) for x in bars]
    right = [i for i, x in enumerate(bars, 1) if equal(cells(x)) and len(cells(x)) == 5 and cells(x)[0] == 2]
    eq(right, [2], 'S3 exactly one strip is 5 boxes of 2 (Siti has 5 bags of 2 sweets)'); eq([equal(cells(x)) for x in bars], [True, True, False], 'S3 strip 3 has unequal boxes'); eq(cells(bars[0]), [5, 5], 'S3 strip 1 is 2 boxes of 5'); eq(total(5, 2), 10, 'S3 total'); eq(T['S3']['val'], [2], 'S3 val'); eq(T['S3']['text'].startswith('Siti has 5 bags. Each bag has 2 sweets.'), True, 'S3 story')
    eq(len(T['S3']['mcq']['options']), 3, 'S3 three strips')
    c = cells(T['S4']['visual']['bars'][0]); strip_ok(T['S4']['visual']['bars'][0], 'S4'); eq((c, total(3, 5) + 2), ([5, 5, 5, 2], 17), 'S4 strip and total'); eq(total(3, 5), 15, 'S4 step 1'); eq(T['S4']['val'], [15, 17], 'S4 val')
    eq((total(2, 6), T['S5']['draw']), (12, True), 'S5'); eq(T['S5']['val'], [12], 'S5 val')
    eq((total(4, 3), total(4, 3) - 2), (12, 10), 'S6'); b6 = T['S6']['visual']['bars'][0]; strip_ok(b6, 'S6'); eq((cells(b6), sum(cells(b6))), ([3, 3, 3, 3], total(4, 3)), 'S6 strip is the 4 bags of 3'); eq(T['S6']['val'], [12, 10], 'S6 val')
    # ---- Think harder
    eq((total(3, 6), total(3, 6) + 5, total(3, 6) + 5 - 8), (18, 23, 15), 'T1'); eq(T['T1']['val'], [18, 23, 15], 'T1 val'); eq(T['T1']['text'].startswith('Jenny has 3 boxes with 6 pens in each box and 5 loose pens. She gives 8 pens away.'), True, 'T1 story (not the class numbers 4 boxes of 5 and 6 loose)')
    bars = T['T2']['visual']['bars']; [strip_ok(x, 'T2 ' + x['name']) for x in bars]; eq((cells(bars[0]), cells(bars[1])), ([7], [7, 7]), 'T2 strips'); eq((twice(7), 7 + twice(7)), (14, 21), 'T2'); eq(T['T2']['val'], [14, 21], 'T2 val'); eq(T['T2']['text'].startswith('Mei has 7 marbles.'), True, 'T2 story (not the class numbers 8 and 16)')
    eq((twice(4), 4 + 2), (8, 6), 'T3 twice as many is 8 and Jenny added 2'); eq(twice(4) == 6, False, 'T3 Jenny is wrong'); eq(T['T3']['val'], ['No', 8], 'T3 val'); eq(T['T3']['text'].startswith('Mei has 4 stickers. Ravi has twice as many stickers as Mei. Jenny says Ravi has 6'), True, 'T3 story')
    mei = [m for m in range(1, 25) if twice(m) == 24][0]
    eq((mei, 24 - mei), (12, 12), 'T4 Mei and the gap'); gave = transfer_to_equal(24, mei); eq(gave, 6, 'T4 Ali gives 6'); eq((24 - gave, mei + gave), (18, 18), 'T4 equal after the transfer'); eq(T['T4']['val'], [12, 6], 'T4 val'); bars = T['T4']['visual']['bars']; [strip_ok(x, 'T4 ' + x['name']) for x in bars]; eq((cells(bars[0]), cells(bars[1])), ([12], [12, 12]), 'T4 strips (Ali is two strips of Mei)'); eq(bars[1]['len'], 24, 'T4 Ali has 24')
    # ---- Go further
    eq((total(4, 3), total(5, 2), total(4, 3) + total(5, 2) + 4), (12, 10, 26), 'G1'); eq(T['G1']['val'], [12, 10, 26], 'G1 val')
    bars = T['G2']['visual']['bars']; [strip_ok(x, 'G2 ' + x['name']) for x in bars]; eq((cells(bars[0]), cells(bars[1])), ([5], [5, 5, 5]), 'G2 strips'); eq((times_as_many(3, 5), 5 + times_as_many(3, 5)), (15, 20), 'G2'); eq(T['G2']['val'], [15, 20], 'G2 val'); eq(T['G2']['text'].startswith('Siti has 5 marbles.'), True, 'G2 story')
    lily = unit_value(24, 1 + 3); eq((lily, times_as_many(3, lily), lily + times_as_many(3, lily)), (6, 18, 24), 'G3'); eq(T['G3']['val'], [6, 18], 'G3 val')
    # ---- Investigation: doubling
    seq = [3]
    for _ in range(3): seq.append(twice(seq[-1]))
    eq(seq, [3, 6, 12, 24], 'I1 doubling'); eq(d['tiers']['investigation']['val'], seq, 'I1 val'); eq([3 + 3 * k for k in range(4)] == seq, False, 'I1 adding 3 each time is a different sequence'); eq(twice(3), 6, 'I1 first step')
    # ---- Exit ticket and home practice
    opts = X['E1']['mcq']['options']; eq(opts[1], '4 × 5', 'E1 option 2'); eq(total(4, 5), 20, 'E1 4 bags of 5'); eq(4 + 5, 9, 'E1 option 1 joins'); eq(5 - 4, 1, 'E1 option 3 is a gap'); eq(4 + 4 + 4, 12, 'E1 option 4 is 3 fours not 4 fives'); eq(X['E1']['val'], [2], 'E1 val')
    eq((total(2, 5), total(2, 5) + 3), (10, 13), 'E2'); eq(X['E2']['val'], [13], 'E2 val'); eq((total(3, 4), total(3, 4) - 2), (12, 10), 'E3'); eq(X['E3']['val'], [10], 'E3 val')
    eq((total(4, 2), total(3, 4) + 5, total(4, 4) - 3, 9 + twice(9), times_as_many(3, 4) + 5), (8, 17, 13, 27, 17), 'home answers')
    eq([H['H1']['val'], H['H2']['val'], H['H3']['val'], H['H4']['val'], H['H5']['val']], [[4, 2, 8, 8], [17], [13], [27], [17]], 'home vals')
    # ---- sneak-peek, warm-up, slides, talk, spare time
    eq(total(3, 4), 12, 'sneak 1'); eq(d['sneak_peek']['val1'], 12, 'sneak 1 val'); eq((twice(5), 5 + twice(5)), (10, 15), 'sneak 2')
    rb = sl['s-rem1']['blocks'][0]['bars']; eq(([b['len'] for b in rb], 9 - 5), ([9, 5], 4), 's-rem1 strips and gap')
    g = sl['s-rem2']['blocks'][0]; eq((g['n'], g['each'], total(g['n'], g['each'])), (4, 5, 20), 's-rem2'); eq((6 + 4, 6 + 4 - 3), (10, 7), 's-rem3 steps')
    g = sl['s-sneak']['blocks'][1]['cols'][0][1]; eq((g['n'], g['each'], g['empty']), (3, 4, True), 's-sneak puzzle 1 picture')
    eq(total(3, 5), 15, 'explore 1'); v = sl['s-explore1-ans']['blocks'][1]; eq((v['units']['n'], v['bars'][0]['len'], v['units']['text']), (3, 15, '5'), 's-explore1 strip')
    bars = sl['s-explore2']['blocks'][1]['bars']; [strip_ok(x, 's-explore2 ' + x['name']) for x in bars]; eq([cells(x) for x in bars], [[3] * 4, [4] * 3, [3, 3, 3, 2]], 's-explore2 strips'); eq((total(4, 3), total(3, 4)), (12, 12), 's-explore2 totals')
    bars = sl['s-explore3']['blocks'][1]['bars']; strip_ok(bars[0], 's-explore3'); eq((cells(bars[0]), total(3, 5) + 2), ([5, 5, 5, 2], 17), 's-explore3')
    bars = sl['s-explore4-ans']['blocks'][1]['bars']; [strip_ok(x, 's-explore4 ' + x['name']) for x in bars]; eq((cells(bars[0]), cells(bars[1])), ([6], [6, 6]), 's-explore4 strips'); eq((twice(6), 6 + twice(6), 6 + 2), (12, 18, 8), 's-explore4 twice is not 2 more')
    v = sl['s-m1-ans']['blocks'][1]; eq((v['units']['n'], v['bars'][0]['len']), (3, total(3, 5)), 's-m1 strip')
    bars = sl['s-m2']['blocks'][0]['bars']; strip_ok(bars[0], 's-m2'); eq((cells(bars[0]), total(4, 5), total(4, 5) + 6), ([5, 5, 5, 5, 6], 20, 26), 's-m2'); rows = sl['s-m2']['blocks'][1]['rows'][1:]; eq([r[1] for r in rows], ['4 × 5 = ?', '? + 6 = ?'], 's-m2 table asks, does not tell'); eq((total(4, 5), total(4, 5) + 6), (20, 26), 's-m2 steps')
    bars = sl['s-m3-ans']['blocks'][1]['bars']; [strip_ok(x, 's-m3 ' + x['name']) for x in bars]; eq((cells(bars[0]), cells(bars[1])), ([8], [8, 8]), 's-m3 strips'); rows = sl['s-m3-ans']['blocks'][2]['rows'][1:]; eq([r[1] for r in rows], ['Ali: 8 + 8 = ?', 'Together: 8 + ? = ?'], 's-m3 table asks, does not tell'); eq((8 + 8, 8 + 16), (16, 24), 's-m3 sums')
    eq((total(3, 4), total(5, 2) + 3, twice(5), 5 + twice(5)), (12, 13, 10, 15), 's-m4 answers'); rows = sl['s-m4a']['blocks'][0]['rows'][1:]; eq([r[1] for r in rows], ['12 sweets', '13 pens', 'Ali 10, together 15'], 's-m4a table')
    eq([total(3, 2), total(4, 3), total(2, 5), total(3, 4), twice(4)], [6, 12, 10, 12, 8], 'break totals')
    bars = sl['s-sneakans']['blocks'][0]['bars']; [strip_ok(x, 's-sneakans ' + x['name']) for x in bars]; eq((cells(bars[0]), cells(bars[1]), 5 + twice(5)), ([5], [5, 5], 15), 's-sneakans')
    eq((twice(8), twice(8) - 8, 8 + 2), (16, 8, 10), 'talk: twice 8 is 8 more, not 2 more')
    bars = sl['s-opt']['blocks'][0]['bars']; [strip_ok(x, 's-opt ' + x['name']) for x in bars]; eq((cells(bars[1]), times_as_many(3, 6), times_as_many(3, 6) - 6), ([6, 6, 6], 18, 12), 's-opt')
    eq([twice(n) == n + 2 for n in (2, 3, 8)], [True, False, False], 'spare M1: twice as many is 2 more only for 2'); eq(total(3, 4), 12, 'spare M3 check')
    # ---- online practice items without templates
    items = {i['id']: i for i in d['online_practice']['items']}
    eq(items['c2']['answer'], 15, 'c2 authored'); eq(items['c3']['answer'], 17, 'c3 authored'); eq(items['c4']['answer'], 10, 'c4 authored')
    eq((items['c5']['answer'], total(4, 5)), ('4 × 5', 20), 'c5'); eq(sum(1 for o in items['c5']['options'] if o == '4 × 5'), 1, 'c5 one right option')
    eq((items['t1']['answer'], items['t2']['answer'], items['t4']['answer']), (12, 18, 6), 't1 t2 t4 authored'); eq(([len(sl[i]['blocks']) for i in ('s-explore1', 's-explore4', 's-m1')], len(sl['s-m3']['blocks'])), ([1, 1, 2], 1), 'question slides leave the strips off'); eq(items['t3']['answer'], 'no', 't3'); eq(twice(8) == 10, False, 't3 Jenny is wrong')
    eq(items['g1']['answer'], 26, 'g1 authored'); eq(items['g2']['answer'], 28, 'g2 authored'); eq(items['g3']['answer'], 6, 'g3 authored')
    return n
