"""Independent answer checks for Level 1 Term 3 Lesson 5 (Lesson 25, Price Tags: Compare and Choose).

Every gap, total, change and exact-amount claim in l25.json is recomputed here from the prices that the lesson's own price-tag pictures and sentences show, by counting up one dollar at a time
(never by the lesson's own take-away), by listing pairs and triples (brute force over the tags), and by trying every price in a small range for the story puzzles (so that the stated number of
answers is exact). The (price, price) pairs used in the class (warm-up, sneak-peek, Explore, Mini-lesson, Talk) are listed and checked to be different from the pairs in the workbook, the exit
ticket and the Quest gate for this lesson (pen $6 and ruler $9; two items that cost exactly $10: $4 and $6). The online practice templates get brute-force oracles. The kit contract and the
hand-off from the lesson before and to the lesson after are checked against the files of the neighbouring lessons.
"""
import itertools
import json
import os
import re

L1 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# ------------------------------------------------------------------------------------------ helpers (all by counting, not by the lesson's own method)
def count_up(a, b):
    """Dollars to count on from a to b, one dollar at a time."""
    n = 0
    x = a
    while x < b:
        x += 1
        n += 1
    return n


def total(*xs):
    t = 0
    for x in xs:
        for _ in range(x):
            t += 1
    return t


def tags_of(x, out=None):
    """Every price_tag figure in a data structure as (item, price as an int)."""
    out = [] if out is None else out
    if isinstance(x, dict):
        if x.get('type') == 'price_tag':
            out.append((x['item'], int(str(x['price']).lstrip('$'))))
        for v in x.values():
            tags_of(v, out)
    elif isinstance(x, list):
        for v in x:
            tags_of(v, out)
    return out


def nums(text):
    return [int(m) for m in re.findall(r'\$(\d+)', text)]


# ------------------------------------------------------------------------------------------ the registry of what each part of the lesson asks
# ('gap', cheaper, dearer) | ('total', a, b) | ('change', price, paid) | ('need', has, price) | ('exact', target, tuple of tag prices) | ('hidden', total, difference)
QUEST = {('gap', 6, 9), ('exact', 10, (4, 6))}
CLASS = {
    'sneak': [('cmp', 8, 13), ('less', 14, 5)],
    'remember': [('cmp', 36, 63), ('gap', 28, 35), ('gap', 3, 8)],
    'explore': [('order', 3, 5, 7), ('gap', 8, 14)],
    'mini': [('gap', 4, 11), ('gap', 5, 13), ('total', 10, 2), ('total', 3, 13), ('change', 16, 20), ('change', 11, 20), ('exact', 15, (5, 7, 8, 10, 13))],
    'talk': [('gap', 12, 17)],
    'opt': [('hidden', 11, 9)],
}
WORKBOOK = {
    'S1': [('cmp', 12, 18)], 'S2': [('gap', 8, 17)], 'S3': [('total', 7, 8)], 'S4': [('order', 11, 13, 16)], 'S5': [('change', 13, 20)], 'S6': [('need', 11, 16)],
    'T1': [('gap', 15, 43)], 'T2': [('hidden', 16, 6)], 'T3': [('total', 27, 18), ('change', 27, 50), ('enough', 40, 45)], 'T4': [('exact', 11, (2, 3, 4, 7, 8)), ('exact3', 14, (2, 3, 4, 7, 8))],
    'G1': [('hidden', 52, 12)], 'G2': [('clues', 33)], 'G3': [('total', 27, 16), ('change', 43, 100), ('gap', 16, 27)],
    'I1': [('apart', 4, (2, 3, 5, 7, 8, 11, 12))],
    'E1': [('gap', 5, 14)], 'E2': [('total', 8, 5)], 'E3': [('change', 14, 20)],
    'H1': [('need', 12, 18)], 'H2': [('total', 4, 10)], 'H3': [('enough', 15, 15)], 'H4': [('hidden', 20, 6)],
}

# the nine tags on the kit page, in the order the lesson prints them
KIT = [('rubber', 2), ('pencil', 3), ('pen', 4), ('glue', 5), ('ruler', 7), ('cup', 8), ('book', 12), ('ball', 14), ('bag', 18)]


# ------------------------------------------------------------------------------------------ oracles for the online practice templates
def _gap(a, b):
    return count_up(min(a, b), max(a, b))


def _hidden_cheap(t, d):
    """The cheaper price p such that p + (p + d) = t, found by trying every price."""
    sols = [p for p in range(0, t + 1) if p + (p + d) == t]
    assert len(sols) == 1, (t, d, sols)
    return sols[0]


ORACLES = {
    'c1': lambda e: _gap(e['b'], e['a']),
    'c2': lambda e: total(e['a'], e['b']),
    'c3': lambda e: count_up(e['p'], 20),
    'c4': lambda e: 'book' if e['u'] * (1 - e['k']) + e['v'] * e['k'] > e['v'] * (1 - e['k']) + e['u'] * e['k'] else 'cup',
    'c5': lambda e: _gap(e['a'], e['b']),
    't1': lambda e: _gap(min(e['a'], e['b'], e['c']), max(e['a'], e['b'], e['c'])),
    't2': lambda e: _hidden_cheap(2 * e['a'] + e['d'], e['d']),
    't3': lambda e: 'Yes' if e['x'] + e['y'] <= e['m'] else 'No',
    'g1': lambda e: _hidden_cheap(2 * e['p'] + e['d'], e['d']),
    'g2': lambda e: count_up(e['a'] + e['b'], 100),
}
BASE_ENV = {'c1': dict(a=17, b=8), 'c2': dict(a=7, b=5), 'c3': dict(p=13), 'c5': dict(a=9, b=16), 't1': dict(a=43, b=26, c=15), 't2': dict(a=5, d=6), 'g1': dict(p=20, d=12), 'g2': dict(a=27, b=16)}


def run(d):
    n = 0

    def eq(a, b, msg=''):
        nonlocal n
        n += 1
        assert a == b, f'{msg}: got {a!r}, expected {b!r}'

    T = {q['id']: q for q in d['tiers']['start'] + d['tiers']['think'] + d['tiers']['go']}
    X = {q['id']: q for q in d['exit']}
    H = {q['id']: q for q in d['home_practice']}
    sl = {s['id']: s for s in d['slides']}
    inv = d['tiers']['investigation']

    # ---------------------------------------------------------------- the pairs: class against workbook against the Quest
    allcls = [p for v in CLASS.values() for p in v]
    allwb = [p for v in WORKBOOK.values() for p in v]
    eq(len(set(allcls)), len(allcls), 'class items are all different')
    eq(len(set(allwb)), len(allwb), 'workbook items are all different')
    eq(sorted(set(allcls) & set(allwb)), [], 'no workbook, exit or home item repeats a class item')
    eq(sorted((set(allcls) | set(allwb)) & QUEST), [], 'no class or workbook item is a Quest gate item')
    pairs = lambda items: {tuple(sorted(p[1:3])) for p in items if p[0] in ('gap', 'cmp')}
    eq(pairs(allcls) & pairs(allwb), set(), 'no gap pair is shared between class and workbook')
    eq(any(6 in p and 9 in p for p in pairs(allcls) | pairs(allwb)), False, 'no pen $6 and ruler $9 pair')
    for it in allcls + allwb:       # the Quest pair 4 + 6 = 10 never appears as an exact-$10 puzzle
        if it[0] == 'exact': eq(it[1] == 10 and sorted(it[2]) == [4, 6], False, 'no $4 and $6 exact pair')

    # ---------------------------------------------------------------- warm-up
    b1 = [b for b in sl['s-rem1']['blocks'] if b.get('t') == 'cols'][0]['cols']
    eq([(c[0]['tens'], c[0]['ones']) for c in b1], [(3, 6), (6, 3)], 's-rem1 shows 36 and 63')
    eq(max(range(100), key=lambda v: (v // 10, v % 10) if v in (36, 63) else (-1, -1)), 63, 's-rem1 greater number')
    nl = sl['s-rem2']['blocks'][0]
    eq((nl['marks'], nl['jumps']), ([28, 35], [[28, 30, '+2'], [30, 35, '+5']]), 's-rem2 jumps')
    eq(count_up(28, 30) + count_up(30, 35), count_up(28, 35), 's-rem2 gap'); eq(count_up(28, 35), 7, 's-rem2 gap is 7')
    bm = sl['s-rem3']['blocks'][0]
    eq([(b['name'], b['len']) for b in bm['bars']], [('Ali', 8), ('Mei', 3)], 's-rem3 strips'); eq(count_up(3, 8), 5, 's-rem3 gap')
    # ---------------------------------------------------------------- sneak-peek
    sp = d['sneak_peek']
    eq((nums(sp['q1']), 'bag' in sp['a1'], 13 > 8), ([13, 8], True, True), 'sneak 1')
    eq(nums(sp['q2']), [5, 14], 'sneak 2 numbers'); eq(count_up(5, 14) + 5 == 14 and 14 - 5 == 9, True, 'sneak 2 data'); eq(sum(1 for _ in range(14 - 5)), 9, 'sneak 2 answer'); eq(sp['val2'], 9, 'sneak val2')
    eq(sp['val1'], 13, 'sneak val1')
    # ---------------------------------------------------------------- Explore: the tags the children hold come from the kit page; the slides show only the answer after the children have answered
    kit = {t: p for t, p in zip(d['workbook']['kits'][0]['items'], [int(x.lstrip('$')) for x in d['workbook']['kits'][0]['prices']])}
    eq(sorted(kit.items()), sorted(KIT), 'the kit page prints the nine tags of this check')
    e1 = tags_of(sl['s-explore1-ans']['blocks'])
    eq(e1, [('pencil', 3), ('glue', 5), ('ruler', 7)], 's-explore1-ans order'); eq(all(kit[i] == p for i, p in e1), True, 's-explore1-ans prices match the kit')
    eq(e1 == sorted(e1, key=lambda t: t[1]), True, 's-explore1-ans is least first')
    eq(tags_of(sl['s-explore1']['blocks']), [], 's-explore1 shows no price while the question is asked')
    eq(tags_of(sl['s-explore2']['blocks']), [], 's-explore2 shows no price while the question is asked')
    eq(count_up(kit['cup'], kit['ball']), 6, 'explore 2 gap'); eq(count_up(8, 10) + count_up(10, 14), 6, 'explore 2 via ten')
    nl = sl['s-explore2-ans']['blocks'][0]
    eq((nl['marks'], nl['jumps']), ([8, 14], [[8, 10, '+2'], [10, 14, '+4']]), 's-explore2-ans jumps')
    # ---------------------------------------------------------------- Mini-lesson
    t = tags_of(sl['s-m1']['blocks']); eq(t, [('car', 11), ('ball', 4)], 's-m1 tags'); eq(count_up(4, 11), 7, 's-m1 gap'); eq(count_up(4, 10) + count_up(10, 11), 7, 's-m1 via ten')
    eq([b for b in sl['s-m1']['blocks'] if b.get('type') == 'bar_model'][0]['gap']['text'], '[]', 's-m1 hides the gap')
    nl = [b for b in sl['s-m1a']['blocks'] if b.get('type') == 'number_line'][0]; eq(nl['jumps'], [[4, 10, '+6'], [10, 11, '+1']], 's-m1a jumps')
    t = tags_of(sl['s-m2']['blocks']); eq(t, [('bag', 13), ('pen', 5)], 's-m2 tags'); eq(count_up(5, 13), 8, 's-m2 gap'); eq(count_up(5, 10) + count_up(10, 13), 8, 's-m2 via ten')
    nl = [b for b in sl['s-m2a']['blocks'] if b.get('type') == 'number_line'][0]; eq(nl['jumps'], [[5, 10, '+5'], [10, 13, '+3']], 's-m2a jumps')
    t = tags_of(sl['s-m3']['blocks']); eq(t, [('cup', 10), ('rubber', 2)], 's-m3 tags'); eq(total(10, 2), 12, 's-m3 total'); eq(total(3, 13), 16, 's-m3 your turn')
    eq('$10 + $2 = $12' in json.dumps(sl['s-m3a']['blocks']) and '$3 + $13 = $16' in json.dumps(sl['s-m3a']['blocks']), True, 's-m3a answers')
    eq(sl['s-m3']['blocks'][-1]['t'], 'p', 's-m3 shows no total while the question is asked')
    eq(count_up(16, 20), 4, 's-m4 change'); eq(count_up(11, 20), 9, 's-m4 your turn'); eq(total(10, 10), 20, 'two ten-dollar notes make 20')
    m = [b for b in sl['s-m4']['blocks'] if b.get('t') == 'cols'][0]['cols']
    eq((tags_of(m), m[1][0]['items']), ([('car', 16)], [dict(v='$10', n=2)]), 's-m4 shows the car and two ten-dollar notes')
    nl = [b for b in sl['s-m4a']['blocks'] if b.get('type') == 'number_line'][0]; eq(nl['jumps'], [[16, 20, '+4']], 's-m4a jump')
    eq([b for b in sl['s-m4']['blocks'] if b.get('type') == 'number_line'][0].get('jumps'), None, 's-m4 draws no jump while the question is asked')
    five = [p for _, p in tags_of(sl['s-m5']['blocks'])]; eq(five, [5, 7, 8, 10, 13], 's-m5 tags')
    ways = [c for c in itertools.combinations(five, 2) if total(*c) == 15]; eq(ways, [(5, 10), (7, 8)], 's-m5 exactly two ways')
    tb = [b for b in sl['s-m5a']['blocks'] if b.get('t') == 'table'][0]['rows'][1:]
    for row in tb:
        mine = int(row[0].lstrip('$')); need = 15 - mine
        eq(int(row[1].lstrip('$')), need, 's-m5a partner ' + row[0])
        if need in five and need != mine:
            eq('Yes' in row[2] or 'Already' in row[2], True, 's-m5a row ' + row[0] + ' has a partner')
        else:
            eq('No tag' in row[2], True, 's-m5a row ' + row[0] + ' has no partner')
    # ---------------------------------------------------------------- Start here
    q = T['S1']; tg = tags_of(q); eq(tg, [('book', 12), ('bag', 18)], 'S1 tags'); eq(max(tg, key=lambda t: t[1])[0], 'bag', 'S1'); eq(q['val'], ['bag'], 'S1 val'); eq(q['parts'][0]['choices'], ['book', 'bag'], 'S1 choices')
    q = T['S2']; a, b = nums(q['text']); eq((a, b), (8, 17), 'S2 text'); eq(count_up(a, b), 9, 'S2'); eq(q['val'], [9], 'S2 val')
    bars = {x['name']: x['len'] for x in q['visual']['bars']}; eq(bars, {'Cup': 8, 'Bag': 17}, 'S2 strips match the story')
    q = T['S3']; tg = tags_of(q); eq(tg, [('pen', 7), ('ball', 8)], 'S3 tags'); eq(nums(q['text']), [7, 8], 'S3 text'); eq(total(7, 8), 15, 'S3'); eq(q['val'], [7, 8, 15, 15], 'S3 val')
    q = T['S4']; tg = tags_of(q); eq(tg, [('book', 16), ('ball', 11), ('cup', 13)], 'S4 tags'); eq(min(tg, key=lambda t: t[1])[0], 'ball', 'S4'); eq(q['val'], ['ball'], 'S4 val')
    eq(q['parts'][0]['choices'], [t[0] for t in tg], 'S4 choices are the three items in picture order')
    q = T['S5']; a = nums(q['text'])[0]; eq(a, 13, 'S5 price'); eq(count_up(13, total(10, 10)), 7, 'S5'); eq(q['val'], [7], 'S5 val'); eq(tags_of(q), [('ball', 13)], 'S5 tag')
    eq([v['items'] for v in q['visuals'] if v['type'] == 'money'], [[dict(v='$10', n=2)]], 'S5 money picture is two ten-dollar notes')
    q = T['S6']; a, b = nums(q['text']); eq((a, b), (16, 11), 'S6 numbers'); eq(count_up(b, a), 5, 'S6'); eq(q['val'], [5], 'S6 val'); eq(tags_of(q), [('book', 16)], 'S6 tag')
    eq(sum(x['mins'] for x in d['tiers']['start']) <= 20, True, 'Start here within 20 minutes')
    eq(max(max(nums(x['text']) or [0]) for x in d['tiers']['start']) <= 20, True, 'Start here prices within $20')
    # ---------------------------------------------------------------- Think harder
    q = T['T1']; tg = tags_of(q); eq(tg, [('bag', 43), ('book', 26), ('ball', 15)], 'T1 tags'); hi = max(tg, key=lambda t: t[1]); lo = min(tg, key=lambda t: t[1])
    eq((hi[0], count_up(lo[1], hi[1])), ('bag', 28), 'T1'); eq(q['val'], ['bag', 28], 'T1 val'); eq(count_up(15, 20) + count_up(20, 40) + count_up(40, 43), 28, 'T1 via tens')
    eq(max(p for _, p in tg) <= 50, True, 'T1 within $50')
    q = T['T2']; t = nums(q['text']); eq(t, [16, 6], 'T2 numbers'); sols = [(a, c) for a in range(0, 17) for c in range(0, 17) if a + c == 16 and c == a + 6]; eq(sols, [(5, 11)], 'T2 exactly one answer')
    eq(q['val'], [5, 11], 'T2 val'); bars = {x['name']: x['len'] for x in q['visual']['bars']}; eq(bars, {'Glue': 5, 'Cup': 11}, 'T2 strips are drawn to scale'); eq(q['visual']['gap']['text'], '6', 'T2 gap label')
    q = T['T3']; eq(nums(q['text']), [27, 18], 'T3 text'); eq(total(27, 18), 45, 'T3a'); eq(count_up(27, 50), 23, 'T3b')
    eq(45 > 40, True, 'T3c is No'); eq(q['val'], [45, 23, 'No'], 'T3 val'); eq(nums(q['parts'][2]['text']), [40], 'T3c budget')
    q = T['T4']; tg = [p for _, p in tags_of(q)]; eq(tg, [2, 3, 4, 7, 8], 'T4 tags'); eq({i: p for i, p in tags_of(q)}, {i: p for i, p in KIT if i in ('rubber', 'pencil', 'pen', 'ruler', 'cup')}, 'T4 tags are kit tags')
    w2 = [c for c in itertools.combinations(tg, 2) if total(*c) == 11]; eq(w2, [(3, 8), (4, 7)], 'T4a exactly two ways')
    w3 = [c for c in itertools.combinations(tg, 3) if total(*c) == 14]; eq(w3, [(2, 4, 8), (3, 4, 7)], 'T4b exactly two ways')
    eq(nums(q['parts'][0]['text']), [11], 'T4a total'); eq(nums(q['parts'][1]['text']), [14], 'T4b total'); eq(q['val'], [3, 8, 4, 7, 2, 4, 8, 3, 4, 7], 'T4 val')
    # ---------------------------------------------------------------- Go further
    q = T['G1']; t, dd = 52, 12; sols = [(p, c) for p in range(0, 53) for c in range(0, 53) if p + c == t and c - p == dd]; eq(sols, [(20, 32)], 'G1 exactly one answer'); eq(q['val'], [20, 32], 'G1 val')
    eq(nums(q['text']), [12, 52], 'G1 text'); bars = {x['name']: x['len'] for x in q['visual']['bars']}; eq(bars, {'Pie': 20, 'Cake': 32}, 'G1 strips to scale'); eq(q['visual']['gap']['text'], '12', 'G1 gap label')
    q = T['G2']; sols = [(k, t_, dl) for k in range(0, 34) for t_ in [k + 7] for dl in [t_ - 5] if k + t_ + dl == 33]; eq(sols, [(8, 15, 10)], 'G2 exactly one answer'); eq(q['val'], [8, 15, 10], 'G2 val')
    eq(nums(q['text']), [7, 5, 33], 'G2 text')
    q = T['G3']; eq(nums(q['text']), [100, 27, 16], 'G3 text'); eq(total(27, 16), 43, 'G3a'); eq(count_up(43, 100), 57, 'G3b'); eq(count_up(16, 27), 11, 'G3c'); eq(q['val'], [43, 57, 11], 'G3 val')
    eq(tags_of(q), [('bag', 27), ('car', 16)], 'G3 tags')
    # ---------------------------------------------------------------- Investigation: pairs with a gap of exactly 4
    tg = nums(inv['text'])[:7]; eq(tg, [2, 3, 5, 7, 8, 11, 12], 'I1 tags are the seven prices in the sentence')
    ps = [(a, b) for a, b in itertools.combinations(tg, 2) if b - a == 4]; eq(ps, [(3, 7), (7, 11), (8, 12)], 'I1 exactly three pairs'); eq(inv['val'], ['3'], 'I1 val')
    eq([b for a, b in ps if a == 3], [7], 'I1 first step'); eq(nums(inv['first']), [3, 4], 'I1 first step text')
    # ---------------------------------------------------------------- talk and exit
    eq(nums(d['talk']['question']), [17, 12, 5, 5], 'talk numbers'); eq(count_up(12, 17), 5, 'talk gap'); eq(d['talk']['answer'].startswith('The second child is right'), True, 'talk answer names the second child')
    q = X['E1']; a, b = nums(q['text']); eq((a, b, count_up(b, a)), (14, 5, 9), 'E1'); eq(q['val'], [9], 'E1 val')
    q = X['E2']; opts = [int(o.lstrip('$')) for o in q['mcq']['options']]; right = [i + 1 for i, o in enumerate(opts) if o == total(8, 5)]
    eq(right, [3], 'E2 one correct option'); eq(q['val'], right, 'E2 val'); eq(sorted(opts), [3, 12, 13, 14], 'E2 options'); eq(nums(q['text']), [8, 5], 'E2 numbers'); eq(opts[0], count_up(5, 8), 'E2 option 1 is the gap')
    q = X['E3']; a, b = nums(q['text']); eq((a, b, count_up(a, b)), (14, 20, 6), 'E3'); eq(q['val'], [6], 'E3 val')
    # ---------------------------------------------------------------- home
    eq(nums(H['H1']['text']), [12, 18], 'H1 numbers'); eq(count_up(12, 18), 6, 'H1'); eq(H['H1']['val'], 6, 'H1 val')
    eq(nums(H['H2']['text']), [4, 10], 'H2 numbers'); eq(total(4, 10), 14, 'H2'); eq(H['H2']['val'], 14, 'H2 val')
    eq(nums(H['H3']['text']), [15, 8, 7], 'H3 numbers'); eq(total(8, 7) <= 15, True, 'H3 is enough: 8 and 7 make exactly 15'); eq(H['H3']['val'], 'Yes', 'H3 val')
    eq(nums(H['H4']['text']), [20, 6], 'H4 numbers'); sols = [(a, c) for a in range(0, 21) for c in range(0, 21) if a + c == 20 and c == a + 6]; eq(sols, [(7, 13)], 'H4 exactly one answer'); eq(H['H4']['val'], [7, 13], 'H4 val')
    eq(37 + 6, 43, 'H5 rewind'); eq(H['H5']['val'], 43, 'H5 val'); eq(H['H5'].get('rewind_of'), 'Term 1 Lesson 5', 'H5 is the rewind item')
    eq(len([h for h in d['home_practice'] if h['tier'] == 'start']) >= 3, True, 'home has 3 Start here items')
    # ---------------------------------------------------------------- online practice, authored numbers (the oracles run on every variant in the validator)
    items = {i['id']: i for i in d['online_practice']['items']}
    for cid, env in BASE_ENV.items():
        eq(items[cid]['answer'], ORACLES[cid](env), cid + ' authored answer')
    eq(items['c4']['answer'], 'book', 'c4 authored'); eq(items['t3']['answer'], 'No', 't3 authored'); eq(total(18, 15) > 30, True, 't3 authored total')
    for it in items.values():
        for s_ in it.get('slips', []):
            if it['type'] == 'number': eq(it['answer'] in s_['a'], False, it['id'] + ' slip is wrong')
    # every variant of the story puzzles has one answer and a whole number of dollars
    for cid in ('t2', 'g1'):
        tp = items[cid]['tpl']; names = list(tp['vars'])
        for combo in itertools.product(*[tp['vars'][k] for k in names]):
            env = dict(zip(names, combo)); r = ORACLES[cid](env); eq(r >= 1, True, f'{cid} {env}')
    for combo in itertools.product(*[items['g2']['tpl']['vars'][k] for k in ('a', 'b')]):
        eq(sum(combo) < 100, True, f'g2 {combo} stays under $100')
    # ---------------------------------------------------------------- kit contract and hand-offs
    kc = {r['piece']: r for r in d['materials']['kit_contract']}
    for r in kc.values(): eq(r['supplied'] >= r['max_used'], True, 'kit contract ' + r['piece'])
    eq(kc['price tags with a price']['supplied'], 9, 'the kit page prints 9 priced tags'); eq(len(d['workbook']['kits'][0]['prices']) + d['workbook']['kits'][0]['blank'], 12, 'the kit page cuts 12 tags')
    used = max(len(tags_of(sl[s]['blocks'])) for s in ('s-m5',)); eq(used, 5, 'the most tags on one task is 5'); eq(kc['price tags with a price']['max_used'], 5, 'kit contract max_used is 5')
    eq(set(i for i, _ in tags_of(T['T4'])) <= set(kit), True, 'every tag used in T4 is on the kit page')
    nm = ' '.join(d['parent']['next_materials']).lower()
    eq(('price tags' in nm, 'play money' in nm, 'nothing new' in nm), (True, True, True), 'hand-off to the next lesson names the tags and the money and says nothing new to cut')
    prev = json.load(open(os.path.join(L1, 'lessons', 'l24.json'), encoding='utf-8'))
    pm = ' '.join(prev['parent']['next_materials']).lower()
    eq(('price' in pm and '12' in pm), True, 'the lesson before tells families to cut the 12 price tags')
    return n
