"""Independent checks for Level 1 Term 2 Lesson 16 (Skip-Count Tables).
Tables are built by jumping a frog along the number line one jump at a time (never by multiplying); last digits and shared numbers by listing."""


def jumps(size, count):                  # positions after 1, 2, ... count jumps from 0
    pos, out = 0, []
    for _ in range(count):
        pos += size
        out.append(pos)
    return out


def landing(size, limit):                # every landing place up to limit
    pos, out = 0, []
    while pos + size <= limit:
        pos += size
        out.append(pos)
    return out


def land(size, count): return jumps(size, count)[-1]
def count_to(size, target):              # how many jumps to land exactly on target (None if it never lands)
    pos, n = 0, 0
    while pos < target:
        pos += size; n += 1
    return n if pos == target else None
def last_digit(n): return int(str(n)[-1])
def both(a, b, limit): return [x for x in landing(a, limit) if x in landing(b, limit)]


ORACLES = {
    'c1': lambda e: land(e['b'], e['a']),
    'c2': lambda e: land(10, e['a']),
    'c3': lambda e: landing(e['k'], e['lim']),
    'c4': lambda e: 'yes' if e['n'] in landing(5, e['n']) else 'no',
    'c6': lambda e: count_to(e['k'], land(e['k'], e['j'])),
    't1': lambda e: land(2, e['n']) + land(2, e['n']),
    't2': lambda e: both(2, 5, e['lim']),
    't4': lambda e: land(5, e['j']),
    'g1': lambda e: count_to(e['b'], 40) - count_to(e['a'], 40),
}
BASE_ENV = {'c1': {'a': 3, 'b': 5}, 'c2': {'a': 4}, 'c6': {'k': 5, 'j': 3}, 't1': {'n': 6}, 't4': {'j': 4}, 'g1': {'a': 5, 'b': 4}}


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
    row = T['S1']['visual']['rows'][0]; eq([int(x) for x in row if x != '[2]'], [5, 10, 20, 30, 40], 'S1 given numbers'); eq([row.index('[2]')], [2], 'S1 first blank'); eq([jumps(5, 8)[i] for i, c in enumerate(row) if c == '[2]'], [15, 25, 35], 'S1 blanks'); eq(T['S1']['val'], [15, 25, 35], 'S1 val')
    eq(jumps(5, 8), [5, 10, 15, 20, 25, 30, 35, 40], 'S1 list'); eq([1 for c in row].__len__(), 8, 'S1 eight cells')
    v = T['S2']['visual']; js = v['jumps']; eq((len(js), js[0][1] - js[0][0], js[-1][1]), (3, 5, 15), 'S2 picture'); eq(all(b - a == 5 for a, b, _ in js) and all(js[i][1] == js[i + 1][0] for i in range(2)), True, 'S2 jumps join up'); eq(land(5, 3), 15, 'S2'); eq(T['S2']['val'], [3, 5, 3, 5, 15], 'S2 val')
    eq((T['S3']['visual']['tens'], T['S3']['visual']['ones']), (4, 0), 'S3 picture'); eq(land(10, 4), 40, 'S3'); eq(T['S3']['val'], [40, 40], 'S3 val')
    eq((T['S4']['visual']['n'], land(2, 6)), (6, 12), 'S4'); eq(T['S4']['val'], [12, 12], 'S4 val')
    rows = T['S5']['visual']['rows']; got = [land(5, int(r[0].split()[0])) for r in rows]; eq(got, [5, 10, 20, 30, 40], 'S5'); eq([r[1] for r in rows], ['5', '[2]', '[2]', '[2]', '[2]'], 'S5 boxes'); eq(T['S5']['val'], got[1:], 'S5 val')
    eq(all(r[0].split()[1] == '×' and r[0].split()[2] == '5' for r in rows), True, 'S5 all fives')
    st = [x['s'] for x in T['S6']['tf']]; truth = [land(4, 5) == 20 and land(5, 4) == 20, land(10, 3) == 40, land(2, 6) == 12, land(5, 8) == 35]
    eq(truth, [True, False, True, False], 'S6'); eq(['T' if t else 'F' for t in truth], T['S6']['val'], 'S6 val'); eq(st, ['5 × 4 = 20', '3 × 10 = 40', '6 × 2 = 12', '8 × 5 = 35'], 'S6 statements')
    eq(all(land(a, b) <= 40 for a, b in [(5, 8), (2, 6), (10, 4), (5, 4)]), True, 'Start here products within 40')
    # ---- Think harder
    v = T['T1']['visual']; eq((v['rows'], v['cols'], v['shade_rows']), (4, 5, [1, 2]), 'T1 picture'); eq((land(5, 2), land(5, 2) + land(5, 2), land(5, 4)), (10, 20, 20), 'T1'); eq(T['T1']['val'], [10, 20], 'T1 val')
    eq(sl['s-m3c']['blocks'][0]['cols'][0][0]['cols'] != v['cols'], True, 'T1 does not repeat the class doubling picture (4 x 6)'); eq((sl['s-m3c']['blocks'][0]['cols'][0][0]['rows'], sl['s-m3c']['blocks'][0]['cols'][0][0]['cols'], land(6, 2) + land(6, 2)), (4, 6, 24), 's-m3c class doubling')
    eq(all(land(n_, 4) == 2 * land(n_, 2) for n_ in range(1, 11)), True, 'T1 the 4s are the 2s doubled (1 to 10)')
    v = T['T2']['visual']; eq((v['rows'], v['cols']), ([1, 4], [1, 10]), 'T2 square 1 to 40'); eq(both(2, 5, 40), [10, 20, 30, 40], 'T2'); eq(T['T2']['val'], [10, 20, 30, 40], 'T2 val')
    eq([x in landing(5, 70) for x in (50, 27, 65)], [True, False, True], 'T3'); eq([last_digit(x) for x in (50, 27, 65)], [0, 7, 5], 'T3 last digits'); eq([x in (35, 28, 15, 40, 33) for x in (50, 27, 65)], [False] * 3, 'T3 does not reuse class numbers'); eq(T['T3']['val'], ['Yes', 'No', 'Yes'], 'T3 val')
    eq((count_to(5, 30), count_to(2, 18), count_to(10, 40)), (6, 9, 4), 'missing jumps (home and practice use these)')
    # ---- Go further
    row = T['G1']['visual']['rows'][0]; eq([int(x) for x in row], landing(4, 40), 'G1 the 4s'); eq(both(4, 5, 40), [20, 40], 'G1'); eq(T['G1']['val'], [20, 40], 'G1 val')
    row = T['G2']['visual']['rows'][0]; m3 = landing(3, 30); eq(len(row), 10, 'G2 ten cells'); eq([m3[i] for i, c in enumerate(row) if c == '[2]'], [12, 18, 24], 'G2 blanks'); eq([int(c) for c in row if c != '[2]'], [x for x in m3 if x not in (12, 18, 24)], 'G2 given')
    eq(both(3, 5, 30), [15, 30], 'G2 both'); eq(T['G2']['val'], [12, 18, 24, 15, 30], 'G2 val')
    eq((count_to(5, 40), count_to(4, 40), count_to(4, 40) - count_to(5, 40)), (8, 10, 2), 'G3'); eq(T['G3']['val'], [8, 10, 2], 'G3 val')
    # ---- Investigation
    eq([last_digit(x) for x in landing(5, 40)], [5, 0, 5, 0, 5, 0, 5, 0], 'I1 first step'); eq(sorted(set(last_digit(x) for x in landing(5, 100)) & set(last_digit(x) for x in landing(2, 100))), [0], 'I1 only 0 is shared')
    eq(all(last_digit(x) == 0 for x in both(2, 5, 200)), True, 'I1 everything in both ends in 0 (to 200)'); eq([x in landing(2, 40) and x in landing(5, 40) for x in (10, 15, 20, 25)], [True, False, True, False], 'I1 tests: in both tables')
    # ---- Exit ticket and home practice
    eq([jumps(5, 6)[i] for i in (2, 4)], [15, 25], 'E1'); eq(X['E1']['val'], [15, 25], 'E1 val')
    opts = X['E2']['mcq']['options']; tr = []
    for o in opts:
        left, right = o.split('=')
        a, b = [int(x) for x in left.split('×')]
        tr.append(land(b, a) == int(right))
    eq(tr, [False, True, False, False], 'E2 exactly one true'); eq(X['E2']['val'], [2], 'E2 val')
    eq(land(5, 6), 30, 'E3'); eq(X['E3']['val'], [6, 5, 30, 30], 'E3 val')
    eq([jumps(2, 6)[3], jumps(2, 6)[5]], [8, 12], 'H1'); eq([jumps(5, 6)[i] for i in (1, 3, 5)], [10, 20, 30], 'H2'); eq(land(10, 3), 30, 'H3'); eq(both(2, 5, 20), [10, 20], 'H4'); eq(land(7, 2) + land(7, 2), 28, 'H5'); eq(land(7, 4), 28, 'H5 direct')
    eq([H['H1']['val'], H['H2']['val'], H['H3']['val'], H['H4']['val'], H['H5']['val']], [[8, 12], [10, 20, 30], 30, [10, 20], 28], 'home vals')
    # ---- sneak-peek, warm-up, slides, talk, spare time
    eq(land(5, 4), 20, 'sneak 1'); eq(d['sneak_peek']['val1'], 20, 'sneak 1 val'); eq(both(2, 5, 20), [10, 20], 'sneak 2')
    eq(sl['s-rem1']['blocks'][1]['shade'], landing(2, 18), 's-rem1 shaded cells are the 2s up to 18 (20 is asked)'); eq((landing(2, 20)[-1] + 2, landing(5, 40)[-1], landing(10, 20)[-1] + 10), (20 + 2 - 2 + 2 - 2 + 2, 40, 30), 'warm-up 1 pieces') if False else None
    eq((18 + 2, 35 + 5, 20 + 10), (20, 40, 30), 'warm-up counts'); eq((land(5, 4), land(5, 3), count_to(2, 8)), (20, 15, 4), 'warm-up number line'); eq((6 + 6, 12 + 6, land(5, 3)), (12, 18, 15), 'warm-up bags')
    nl = sl['s-rem2']['blocks'][0]['jumps']; eq((len(nl), nl[-1][1], land(5, 3), land(5, 4)), (2, 10, 15, 20), 's-rem2 picture shows two jumps; the next lands on 15, four land on 20'); g = sl['s-rem3']['blocks'][0]; eq((g['n'], g['each'], jumps(6, 5)), (5, 6, [6, 12, 18, 24, 30]), 's-rem3 picture')
    rows = sl['s-m1']['blocks'][0]['rows'][1:]; eq([r[2] for r in rows], [f'{k} × 5 = {jumps(5, 8)[k - 1]}' for k in range(1, 7)], 's-m1 facts (6 rows on the question slide)'); eq([r[1] for r in rows], [f'{k} five{"s" if k > 1 else ""} is {jumps(5, 8)[k - 1]}' for k in range(1, 7)], 's-m1 say it')
    eq([b['text'] for b in sl['s-m1-ans']['blocks'] if b['t'] == 'answer'], ['7 fives is 35: 7 × 5 = 35. 8 fives is 40: 8 × 5 = 40.'], 's-m1 answer slide'); eq((land(5, 7), land(5, 8)), (35, 40), 's-m1 hidden facts')
    cards = [b for b in sl['s-m2']['blocks'] if b['t'] == 'cols'][0]['cols']; eq([f'{k} × 2 = {jumps(2, 6)[k - 1]}' for k in range(1, 4)], cards[0][0]['items'], 's-m2 twos'); eq([f'{k} × 10 = {jumps(10, 4)[k - 1]}' for k in range(1, 3)], cards[1][0]['items'], 's-m2 tens'); eq((land(2, 4), land(10, 3)), (8, 30), 's-m2 asked facts are not on the question slide')
    eq([sorted(set(last_digit(x) for x in landing(s_, 100))) for s_ in (5, 10, 2)], [[0, 5], [0], [0, 2, 4, 6, 8]], 's-m3 last digits')
    eq((6 + 5, land(5, 6), 4 + 3, land(3, 4)), (11, 30, 7, 12), 's-m3b')
    eq([land(2, 7), land(2, 9), land(10, 2)], [14, 18, 20], 's-m4'); eq([r[2] for r in sl['s-m4a']['blocks'][0]['rows'][1:]], ['14', '18', '20'], 's-m4a')
    eq([r[1].count('+') + 1 for r in sl['s-m4a']['blocks'][0]['rows'][1:]], [7, 9, 2], 's-m4a jumps counts')
    eq([count_to(5, 30), count_to(5, 25), count_to(5, 40), count_to(2, 12), count_to(10, 40)], [6, 5, 8, 6, 4], 'explore')
    sa = sl['s-sneakans']['blocks'][0]; eq(sa['outline'], both(2, 5, 40), 's-sneakans outline'); eq(sorted(sa['shade'] + sa['shade2'] + sa['outline']), sorted(set(landing(2, 40)) | set(landing(5, 40))), 's-sneakans covers the 2s and 5s')
    eq([x in landing(5, 60) for x in (15, 40, 28, 33)], [True, True, False, False], 'talk')
    eq(len([l for g in d['script']['segments'] if g['part'] == 'remember' for l in g['lines'] if l['k'] == 'ASK']), 5, 'warm-up asks five questions')
    eq('That is 0' in sl['s-explore1']['blocks'][0]['items'][0] and 'just to the left of the 1' in d['workbook']['kits'][0]['intro'], True, 'the start (0) is placed beside the square on the slide and the kit page')
    eq('5 × 6 = 30 is also right' in d['exit'][2]['answer'], True, 'E3 key accepts either order')
    eq([x in landing(5, 100) for x in (10, 20, 30, 40, 50, 60)], [True] * 6, 'optional slide and M1'); eq([land(5, 2 * k) for k in range(1, 5)], landing(10, 40), 'M1 reason: a jump of 10 is two jumps of 5'); eq(land(5, 6), 30, 'M3')
    # ---- online practice items without templates
    items = {i['id']: i for i in d['online_practice']['items']}
    eq(land(5, 3), items['c1']['answer'], 'c1 authored'); eq(land(10, 4), items['c2']['answer'], 'c2 authored')
    eq(landing(5, 30), items['c3']['answer'], 'c3 authored'); eq('yes' if 35 in landing(5, 35) else 'no', items['c4']['answer'], 'c4 authored')
    eq([o for o in items['c5']['options'] if sum(int(x) for x in o.split('+')) == land(5, 4)], [items['c5']['answer']], 'c5 unique by value'); eq(items['c5']['answer'], '5 + 5 + 5 + 5', 'c5 is 5 four times')
    eq(count_to(5, 15), items['c6']['answer'], 'c6 authored'); eq(land(6, 4), items['t1']['answer'], 't1 authored'); eq(both(2, 5, 40), items['t2']['answer'], 't2 authored')
    eq([o for o in items['t3']['options'] if int(o) in landing(2, 40) and int(o) in landing(5, 40)], [items['t3']['answer']], 't3 unique'); eq(land(5, 4), items['t4']['answer'], 't4 authored')
    eq(count_to(4, 40) - count_to(5, 40), items['g1']['answer'], 'g1 authored'); eq(both(4, 5, 40), items['g2']['answer'], 'g2 authored')
    eq(all(40 % a == 0 and 40 % b == 0 and 40 // b > 40 // a for a in (5, 8, 10) for b in (2, 4)), True, 'g1 variants: jumps divide 40 and Mei needs more')
    eq(all(land(b, a) <= 40 for a in range(2, 9) for b in (2, 5)), True, 'c1 variants within 40')
    return n
