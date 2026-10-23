"""Independent checks for Level 1 Term 2 Lesson 17 (Sharing and Grouping).
Every answer is found by simulation: dealing counters one at a time onto plates (share) and taking away groups of a given size again and again (group).
No division sign and no formula for the answers. Pictures are checked against the numbers in the questions."""


def deal(total, plates):
    """Deal `total` counters one at a time round `plates` plates. Returns the list of plate counts."""
    plate = [0] * plates
    for k in range(total):
        plate[k % plates] += 1
    return plate


def share_each(total, plates):
    return min(deal(total, plates))    # what every plate has at least


def share_left(total, plates):
    p = deal(total, plates)
    return sum(p) - min(p) * plates    # counters that made the plates unequal


def group_up(total, size):
    """Make groups of `size` until there are not enough. Returns (groups, left over)."""
    left, n = total, 0
    while left >= size:
        left -= size
        n += 1
    return n, left


def groups_count(total, size): return group_up(total, size)[0]
def left_over(total, size): return group_up(total, size)[1]
def repeated_add(each, times):
    s = 0
    for _ in range(times): s += each
    return s
def times(a, b): return repeated_add(b, a)
def wei_total(e): return times(e['a'], e['b']) + e['k']      # Wei's stickers: the shared ones plus the ones he keeps
def divisors(n): return [k for k in range(1, n + 1) if group_up(n, k)[1] == 0]
def equal(c): return all(x == c[0] for x in c)
def counts_of(v): return list(v['counts']) if v.get('counts') else [v['each']] * v['n']


ORACLES = {
    'c1': lambda e: {'c': times(e['a'], e['b']), 'a': e['a'], 'b': e['b']},
    'c2': lambda e: share_each(times(e['a'], e['b']), e['a']),
    'c3': lambda e: groups_count(times(e['a'], e['b']), e['b']),
    'c6': lambda e: len([1 for _ in range(e['a']) for _ in range(e['b'])]),
    't1': lambda e: groups_count(times(e['a'], e['b']) + e['c'], e['b']),
    't2': lambda e: left_over(times(e['a'], e['b']) + e['c'], e['b']),
    't3': lambda e: share_each(times(e['c'] + 1, e['k']), e['c'] + 1),
    't4': lambda e: e['b'] - left_over(times(e['a'], e['b']) + e['c'], e['b']),
    'g1': lambda e: divisors(e['t']),
    'g2': lambda e: share_each(times(e['a'], e['b']), e['a']) + e['m'],
    'g3': lambda e: share_each(wei_total(e) - e['k'], e['a']),
}
BASE_ENV = {'c2': {'a': 3, 'b': 4}, 'c3': {'a': 4, 'b': 3}, 'c6': {'a': 4, 'b': 3}, 't1': {'a': 3, 'b': 4, 'c': 2}, 't2': {'a': 3, 'b': 5, 'c': 2}, 't3': {'c': 3, 'k': 5},
            't4': {'a': 3, 'b': 5, 'c': 2}, 'g2': {'a': 4, 'b': 5, 'm': 3}, 'g3': {'a': 3, 'b': 6, 'k': 2}}


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
    v = T['S1']['visual']; eq((len(counts_of(v)), v.get('empty')), (4, True), 'S1 four empty plates'); eq(share_each(8, 4), 2, 'S1'); eq(deal(8, 4), [2, 2, 2, 2], 'S1 equal'); eq(T['S1']['val'], [2], 'S1 val'); eq(T['S1']['text'].split(' dots')[0], 'Share 8', 'S1 text says 8 dots')
    v = T['S2']['visual']; eq((v['icon'], v['n']), ('cookie', 12), 'S2 picture'); eq(group_up(12, 3), (4, 0), 'S2'); eq(T['S2']['val'], [4], 'S2 val')
    v = T['S3']['visual']; eq(v['n'], 14, 'S3 picture'); eq(deal(14, 2), [7, 7], 'S3'); eq(T['S3']['val'], [7], 'S3 val'); eq(T['S3']['text'].startswith('Ali has 14 sweets'), True, 'S3 text says 14 sweets')
    rows = T['S4']['visual']['rows']; got = [share_each(int(r[0]), int(r[1])) for r in rows]; eq(got, [4, 3, 4], 'S4'); eq([share_left(int(r[0]), int(r[1])) for r in rows], [0, 0, 0], 'S4 no left over')
    eq(T['S4']['val'], got, 'S4 val'); eq([r[2] for r in rows], ['[]', '[]', '[]'], 'S4 single-digit boxes'); eq(all(times(int(r[1]), g) == int(r[0]) for r, g in zip(rows, got)), True, 'S4 check by multiplying')
    nl = T['S5']['visual']; eq((nl['start'], nl['end'], nl['step']), (0, 20, 5), 'S5 line'); eq(group_up(20, 5), (4, 0), 'S5'); eq(T['S5']['val'], [4], 'S5 val')
    eq(times(4, 3), 12, 'S6'); eq(share_each(12, 4), 3, 'S6 each'); eq(times(4, 3) == 12, True, 'S6 matches'); eq(T['S6']['val'], [4, 3, 12, 'Yes'], 'S6 val')
    eq((deal(12, 3), group_up(12, 6)), ([4, 4, 4], (2, 0)), 'S7 Lily deals 12 to 3 friends (share), Jamie packs boxes of 6 (group)'); eq(T['S7']['val'], ['Share', 'Group'], 'S7 val')
    # ---- Think harder
    eq(d['tiers']['think'][0]['visual']['n'], 19, 'T1 picture'); eq(group_up(19, 4), (4, 3), 'T1'); eq(T['T1']['val'], [4, 3], 'T1 val'); eq(T['T1']['text'].startswith('Ali has 19 counters'), True, 'T1 text says 19'); eq(19 in (12, 14, 15, 16, 18), False, 'T1 is not a class number (class left-over example is 14 and 15 in groups of 4)')
    eq(group_up(15, 4), (3, 3), 'm4 question: 15 in groups of 4')
    people = 1 + 3; eq(people, 4, 'T2 people'); eq(deal(20, people), [5, 5, 5, 5], 'T2'); eq(deal(20, 3), [7, 7, 6], 'T2 sharing among 3 would not be equal'); eq(people == 3, False, 'T2 Aisha is wrong'); eq(T['T2']['val'], ['No', 5], 'T2 val')
    eq(group_up(18, 6), (3, 0), 'T3 A bags'); eq(deal(18, 6), [3] * 6, 'T3 B each'); eq(T['T3']['val'], ['Group', 3, 'Share', 3], 'T3 val'); eq(T['T3']['text'].startswith('Mei has 18 sweets'), True, 'T3 text says 18'); eq('bags of 6' in T['T3']['parts'][0]['text'] and 'among 6 bags' in T['T3']['parts'][2]['text'], True, 'T3 stories use 6')
    eq(group_up(17, 5), (3, 2), 'T4 bags and left over'); eq(5 - 2, 3, 'T4 more needed'); eq(group_up(17 + 3, 5), (4, 0), 'T4 with 3 more it is 4 full bags'); eq(T['T4']['val'], [3, 2, 3], 'T4 val')
    # ---- Go further
    rowfr = T['G1']['visual']['head'][1:]; each = [share_each(12, int(f)) for f in rowfr]
    eq(each, [12, 6, 4, 3, 2, 1], 'G1 table'); eq([share_left(12, int(f)) for f in rowfr], [0] * 6, 'G1 none left over')
    eq(rowfr, [str(k) for k in divisors(12)], 'G1 columns are exactly the numbers of friends that work'); eq(share_left(12, 5), 2, 'G1 five friends leave 2'); eq(T['G1']['val'][:-1], each + ['No', 2], 'G1 val')
    eq(T['G1']['visual']['rows'][0][1], '[2]', 'G1 first box has two digits')
    # G1 part (c): every number of friends that shares 18 with none left over (tested by dealing, 1 to 18)
    ways18 = [f for f in range(1, 19) if share_left(18, f) == 0]
    eq(ways18, [1, 2, 3, 6, 9, 18], 'G1c ways to share 18'); eq(ways18, divisors(18), 'G1c matches divisors'); eq(T['G1']['parts'][2]['val'], ways18, 'G1c val'); eq(T['G1']['val'][-1], ways18, 'G1 val last')
    eq((share_each(20, 4), share_each(20, 4) + 3), (5, 8), 'G2'); eq(sum(deal(20, 4)) + 4 * 3, 32, 'G2 all pencils now'); eq(times(4, 8), 32, 'G2 4 pots of 8'); eq(T['G2']['val'], [5, 8, 32], 'G2 val')
    eq((20 - 2, share_each(20 - 2, 3), share_left(20 - 2, 3)), (18, 6, 0), 'G3'); eq(share_each(20, 3), 6, 'G3 sharing all 20 leaves a left over'); eq(share_left(20, 3), 2, 'G3 left over if no stickers kept')
    eq(T['G3']['val'], [18, 6], 'G3 val')
    # ---- Investigation: 13 to 20 shared among 4 plates
    heads = [13, 14, 15, 16, 17, 18, 19, 20]; eq(d['tiers']['investigation']['text'].split(' counters')[0], 'Share 13, 14, 15, 16, 17, 18, 19 and 20', 'I1 text lists 13 to 20'); row = heads
    left = [share_left(k, 4) for k in heads]; eq(left, [1, 2, 3, 0, 1, 2, 3, 0], 'I1 left over'); eq(d['tiers']['investigation']['val'], left, 'I1 val')
    eq((deal(8, 4), share_left(9, 4)), ([2, 2, 2, 2], 1), 'I1 first step'); eq(max(share_left(k, 4) for k in range(1, 41)), 3, 'I1 never more than 3 left over')
    eq(all(share_left(k, 4) == share_left(k + 4, 4) for k in range(1, 40)), True, 'I1 the pattern repeats every 4')
    # ---- Exit ticket and home practice
    eq(deal(20, 4), [5] * 4, 'E1'); eq(X['E1']['val'], [5], 'E1 val')
    stories = X['E2']['mcq']['options']
    eq(stories[1], 'Mei puts 12 sweets into bags of 4.', 'E2 option 2'); eq(group_up(12, 4), (3, 0), 'E2 groups of 4 make 3 bags'); eq(deal(12, 4), [3] * 4, 'E2 option 1 is a share: 3 each, not groups of 4')
    eq(12 - 4, 8, 'E2 option 3 is taking away'); eq(12 + 4, 16, 'E2 option 4 is adding'); eq(X['E2']['val'], [2], 'E2 val')
    eq((group_up(18, 3), times(6, 3)), ((6, 0), 18), 'E3'); eq(X['E3']['val'], [6, 6], 'E3 val')
    eq(deal(10, 2), [5, 5], 'H1'); eq(group_up(12, 3), (4, 0), 'H2'); eq(group_up(15, 5), (3, 0), 'H3 groups of 5 is a group story'); eq(H['H3']['text'].startswith('Amelia puts 15 apples into boxes of 5'), True, 'H3 text'); eq(group_up(13, 4), (3, 1), 'H4')
    eq(share_each(18 - 6, 4), 3, 'H5'); eq(share_left(18 - 6, 4), 0, 'H5 none left over')
    eq([H['H1']['val'], H['H2']['val'], H['H3']['val'], H['H4']['val'], H['H5']['val']], [[5], [4, 4], ['Group'], [3, 1], [3]], 'home vals')
    # ---- sneak-peek, warm-up, slides, talk, spare time
    eq(deal(6, 2), [3, 3], 'sneak 1'); eq(d['sneak_peek']['val1'], 3, 'sneak 1 val')
    eq((group_up(12, 3)[0], deal(12, 3)[0]), (4, 4), 'sneak 2 numbers'); eq((3, 4), (3, 4), 'sneak 2 Ali has 3 in each bag, Mei 4'); eq(deal(12, 3)[0] > 3, True, 'sneak 2 Mei has more in each bag')
    eq(deal(6, 3), [2, 2, 2], 'warm-up 6 on 3 plates'); eq(deal(10, 2), [5, 5], 'warm-up 10 on 2 plates'); eq(deal(8, 2), [4, 4], 'warm-up 8 on 2 plates')
    eq([sl['s-rem1']['blocks'][1]['n'], sl['s-rem1']['blocks'][1]['each']], [2, 4], 's-rem1 picture')
    eq(12 + 3, 15, 'warm-up after 12 in threes'); eq(12 + 4, 16, 'warm-up after 12 in fours')
    nls = [x for col in sl['s-rem2']['blocks'][0]['cols'] for x in col if x.get('type') == 'number_line']; eq([(b['step'], b['end']) for b in nls], [(3, 12), (4, 12)], 's-rem2 lines')
    eq([[j[1] - j[0] for j in b['jumps']] for b in nls], [[3, 3, 3], [4, 4]], 's-rem2 jump sizes'); eq(times(3, 4), 12, 'warm-up 3 groups of 4')
    eq((sl['s-rem3']['blocks'][0]['n'], sl['s-rem3']['blocks'][0]['each']), (3, 4), 's-rem3 picture')
    eq([deal(12, 3), deal(10, 2), deal(12, 4)], [[4] * 3, [5] * 2, [3] * 4], 'explore round 1'); eq([group_up(12, 4), group_up(12, 3)], [(3, 0), (4, 0)], 'explore round 2')
    eq([group_up(12, 6), deal(12, 4), deal(15, 3)], [(2, 0), [3] * 4, [5] * 3], 'explore round 3 stories A B C (A share 3 each, B group 2 boxes, C share 5 each)')
    rows = sl['s-explore3']['blocks'][1]['rows'][1:]; eq([r[0] for r in rows], ['A', 'B', 'C'], 's-explore3 rows')
    eq(sl['s-explore1']['blocks'][1]['empty'], True, 's-explore1 plates are empty (answer not shown)')
    eq([(x['blocks'][0]['n'], len(x['blocks'])) for x in (sl['s-m1'], sl['s-m2'])], [(12, 2), (12, 2)], 's-m1 and s-m2 ask with 12 loose sweets; the answer table is left off the question slide'); eq([x['blocks'][2]['rows'][1][1] for x in (sl['s-m1-ans'], sl['s-m2-ans'])], ['4 in each bag', '3 bags'], 's-m1 and s-m2 answers (4 in each bag, 3 bags)'); eq((deal(12, 3)[0], group_up(12, 4)[0]), (4, 3), 's-m1 s-m2 numbers')
    eq((times(3, 4), times(4, 5)), (12, 20), 's-m3'); c = sl['s-m4']['blocks'][0]
    g4, l4 = group_up(14, 4); eq((c['counts'], sum(c['counts'])), ([4] * g4 + [l4], 14), 's-m4 picture: full plates, then the left over'); eq(group_up(14, 4), (3, 2), 's-m4')
    eq((sl['s-m5-ans']['blocks'][1]['cols'][0][0]['seats'], len(sl['s-m5']['blocks'])), (4, 1), 's-m5 four at the table, shown only on the answer slide'); eq(deal(8, 1 + 3), [2] * 4, 's-m5')
    eq([deal(12, 4)[0], group_up(15, 5)[0], deal(16, 2)[0], group_up(18, 3)[0]], [3, 3, 8, 6], 's-m6 answers')
    eq([r[1] for r in sl['s-m6a']['blocks'][0]['rows'][1:]], ['3 each', '3 groups', '8 each', '6 groups'], 's-m6a table')
    eq([deal(8, 2)[0], deal(6, 3)[0], deal(12, 4)[0], deal(10, 5)[0]], [4, 2, 3, 2], 'break totals')
    eq((deal(12, 3)[0], group_up(12, 3)[0], deal(12, 4)[0], group_up(12, 4)[0], deal(10, 5)[0], group_up(10, 5)[0], deal(16, 2)[0], group_up(16, 2)[0]), (4, 4, 3, 3, 2, 2, 8, 8), 'talk pairs: the number is the same')
    c1, c2 = sl['s-sneakans']['blocks'][0]['cols']; eq(((c1[0]['n'], c1[0]['each']), (c2[0]['n'], c2[0]['each'])), ((4, 3), (3, 4)), 's-sneakans pictures')
    eq((group_up(16, 8)[0], deal(16, 8)[0]), (2, 2), 'optional slide'); eq(sl['s-opt']['blocks'][0]['text'], 'Ravi has 16 sweets.', 'optional slide text'); eq((deal(8, 4)[0]), 2, 'spare M3'); eq(sum(1 for _ in range(4) for _ in range(2)), 8, 'spare M3 check')
    eq((deal(12, 4)[0], deal(10, 2)[0], deal(15, 3)[0], group_up(12, 4)[0], group_up(10, 2)[0], group_up(15, 3)[0]), (3, 5, 5, 3, 5, 5), 'spare M1')
    # ---- online practice items without templates
    items = {i['id']: i for i in d['online_practice']['items']}
    eq(items['c2']['answer'], 4, 'c2 authored'); eq(items['c3']['answer'], 4, 'c3 authored'); eq(items['c6']['answer'], 12, 'c6 authored')
    eq((items['c4']['answer'], items['c5']['answer']), ('group', 'share'), 'c4 c5'); eq(group_up(15, 5), (3, 0), 'c4 15 in bags of 5'); eq(deal(16, 4), [4] * 4, 'c5 16 to 4 friends')
    eq((items['t1']['answer'], items['t2']['answer'], items['t4']['answer']), (3, 2, 3), 't1 t2 t4 authored'); eq(group_up(14, 4), (3, 2), 't1 t2'); eq(group_up(17, 5), (3, 2), 't4')
    eq(items['t3']['answer'], 5, 't3 authored'); eq(deal(20, 4)[0], 5, 't3')
    eq(items['g1']['answer'], divisors(12), 'g1 authored'); eq(items['g2']['answer'], 8, 'g2 authored'); eq(items['g3']['answer'], 6, 'g3 authored'); eq(share_each(18, 3), 6, 'g3')
    return n
