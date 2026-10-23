"""Independent answer checks for Level 1 Term 3 Lesson 6 (Lesson 26, The School Shop).

Every total, change, cost of equal items and 'exactly' claim in l26.json is recomputed here by counting one dollar at a time, by listing every pair, triple or number of notes (brute force, so the
stated number of ways is exact: 2 pairs for $12 from six tags, 2 ways for $10 and for $12 with $2 and $5 notes, 2 ways for $20 with pens and books, 2 ways for $18 with rubbers and pencils,
6 ways for $20 with three kinds of note, one way for 7 things, and the amounts $1 and $3 that $2 and $5 notes cannot make). The items used in class (warm-up, sneak-peek, Explore, Mini-lesson,
Talk) are listed and checked to differ from the items in the workbook, the exit ticket and home sheet, and from the Quest gate for this lesson (pen $6 and ruler $9; two items that cost exactly
$10: $4 and $6) and from the Quest cave idea ($14 with $2 and $5 notes). The online practice templates get brute-force oracles. The kit contract and the hand-offs are checked against the
neighbouring lessons.
"""
import itertools
import json
import os
import re

L1 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def count_up(a, b):
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


def nums(text):
    return [int(m) for m in re.findall(r'\$(\d+)', text)]


def tags_of(x, out=None):
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


def ways(target, prices, cap=None):
    """Every way (a count of each kind of item, zero allowed) to pay exactly target with the given prices: brute force over all counts."""
    cap = cap or (target // min(prices) + 1)
    out = []
    for combo in itertools.product(range(cap + 1), repeat=len(prices)):
        if sum(c * p for c, p in zip(combo, prices)) == target:
            out.append(combo)
    return out


# (kind, ...) items. The Quest items for this lesson and the cave idea:
QUEST = {('gap', 6, 9), ('exact', 10, (4, 6)), ('ways', 14, (2, 5))}
CLASS = {
    'remember': [('ten', 7), ('times', 4, 3), ('times', 2, 3), ('pairs', 6)],
    'sneak': [('total', 3, 2), ('exact', 9, (2, 4, 5, 7))],
    'explore': [('exact', 12, (2, 3, 4, 5, 7, 8)), ('ways', 10, (2, 5))],
    'mini': [('enough', 15, 11, 6), ('enough', 12, 4, 9), ('times', 5, 3), ('times', 2, 5), ('ways', 12, (2, 5)), ('totalchange', 8, 3, 20)],
    'talk': [('order', 'pen and book')],
    'opt': [('ways', 10, (4, 2))],
}
WORKBOOK = {
    'S1': [('exact', 10, (3, 5, 7, 8))], 'S2': [('total', 7, 8)], 'S3': [('left', 20, 14)], 'S4': [('enough', 10, 7, 5)], 'S5': [('times', 7, 3)], 'S6': [('left', 20, 12), ('left', 15, 9), ('left', 17, 8)],
    'T1': [('ways', 20, (2, 7))], 'T2': [('ways', 16, (2, 5))], 'T3': [('change3', 9, 4, 2, 50)], 'T4': [('ways', 18, (3, 4))],
    'G1': [('ways', 20, (2, 5, 10))], 'G2': [('seven', 20)], 'G3': [('open',)], 'I1': [('cannot', (2, 5))],
    'E1': [('exact', 11, (3, 4, 5, 8))], 'E2': [('enough', 12, 6, 8)], 'E3': [('times', 3, 4)],
    'H1': [('enough', 10, 3, 4)], 'H2': [('times', 3, 5)], 'H3': [('left2', 20, 8, 5)], 'H4': [('ways', 18, (2, 5))],
}


def _ways_count(t):
    return len(ways(t, (2, 5)))


def _change4(p):
    return count_up(4 * p, 50) if False else count_up(total(p, p, p, p), 50)


ORACLES = {
    'c1': lambda e: total(e['a'], e['b']),
    'c2': lambda e: count_up(e['p'], 20),
    'c3': lambda e: total(e['p'], e['p'], e['p']),
    'c4': lambda e: 'Yes' if total(e['x'], e['y']) <= 10 else 'No',
    'c5': lambda e: count_up(e['a'], e['b']),
    't1': lambda e: count_up(total(e['a'], e['b'], e['c']), 50),
    't2': lambda e: _ways_count(e['t']),
    't3': lambda e: [k for k in range(0, 20) if 5 * e['b'] + 2 * k == 5 * e['b'] + 2 * e['k']][0],
    'g1': lambda e: [b for b in range(0, 8) for a in range(0, 8) if a + b == e['a'] + e['b'] and 2 * a + 5 * b == 2 * e['a'] + 5 * e['b']][0],
    'g2': lambda e: count_up(_cost4(e['p']), 50),
}


def _cost4(p):
    return total(p, p, p, p)


BASE_ENV = {'c1': dict(a=6, b=5), 'c2': dict(p=14), 'c3': dict(p=7), 'c5': dict(a=10, b=13), 't1': dict(a=12, b=8, c=3), 't2': dict(t=16), 't3': dict(b=2, k=4), 'g1': dict(a=5, b=2), 'g2': dict(p=8)}


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

    # ---------------------------------------------------------------- the registries
    allcls = [p for v in CLASS.values() for p in v]
    allwb = [p for v in WORKBOOK.values() for p in v if p != ('open',)]
    eq(len(set(allcls)), len(allcls), 'class items are all different')
    eq(len(set(allwb)), len(allwb), 'workbook items are all different')
    eq(sorted(set(allcls) & set(allwb)), [], 'no workbook, exit or home item repeats a class item')
    eq(sorted((set(allcls) | set(allwb)) & QUEST), [], 'no class or workbook item is a Quest gate or cave item')
    for it in allcls + allwb:
        if it[0] == 'exact' and it[1] == 10: eq(4 in it[2] and 6 in it[2], False, 'no exact-$10 puzzle holds both $4 and $6')
    # ---------------------------------------------------------------- warm-up
    eq((total(7, 3), sl['s-rem1']['blocks'][0]['filled']), (10, 7), 's-rem1 ten-frame has 7 counters and 3 more make 10')
    t = tags_of(sl['s-rem2']['blocks']); eq(t, [('pen', 4)] * 3, 's-rem2 tags'); eq(total(4, 4, 4), 12, 's-rem2')
    tb = [b for b in sl['s-rem3']['blocks'] if b.get('type') == 'table'][0]['rows']
    eq([r for r in tb], [['1', '5'], ['2', '[]'], ['3', '[]']], 's-rem3 rows')
    pairs = [(a, b) for a in range(1, 7) for b in range(1, 7) if a + b == 6 and a <= b]; eq(pairs, [(1, 5), (2, 4), (3, 3)], 's-rem3 pairs that make 6, in order')
    # ---------------------------------------------------------------- sneak
    sp = d['sneak_peek']; eq(nums(sp['q1']), [3, 2], 'sneak 1 numbers'); eq(total(3, 2), 5, 'sneak 1'); eq(sp['val1'], 5, 'sneak val1')
    tg = nums(sp['q2']); eq(tg, [9, 2, 4, 5, 7], 'sneak 2 numbers'); eq([c for c in itertools.combinations((2, 4, 5, 7), 2) if total(*c) == 9], [(2, 7), (4, 5)], 'sneak 2 has two answers')
    # ---------------------------------------------------------------- Explore: the six tags come from the Lesson 25 kit page
    p25 = json.load(open(os.path.join(L1, 'lessons', 'l25.json'), encoding='utf-8'))
    kit = {i: int(pr.lstrip('$')) for i, pr in zip(p25['workbook']['kits'][0]['items'], p25['workbook']['kits'][0]['prices'])}
    six = ('rubber', 'pencil', 'pen', 'glue', 'ruler', 'cup'); sixp = [kit[i] for i in six]; eq(sixp, [2, 3, 4, 5, 7, 8], 'the six tags are on the Lesson 25 kit page')
    w = [c for c in itertools.combinations(sixp, 2) if total(*c) == 12]; eq(w, [(4, 8), (5, 7)], 'explore 1 exactly two pairs')
    eq([(need, need in sixp) for need in [12 - x for x in sixp]], [(10, False), (9, False), (8, True), (7, True), (5, True), (4, True)], 'explore 1 partners (the way to be sure)')
    eq(sorted(tags_of(sl['s-explore1-ans']['blocks'])), sorted([('pen', 4), ('cup', 8), ('glue', 5), ('ruler', 7)]), 's-explore1-ans'); eq(all(kit[i] == p for i, p in tags_of(sl['s-explore1-ans']['blocks'])), True, 's-explore1-ans prices match the kit')
    eq(tags_of(sl['s-explore1']['blocks']), [], 's-explore1 shows no price while the question is asked')
    w = ways(10, (2, 5)); eq(sorted(w), [(0, 2), (5, 0)], 'explore 2 exactly two ways for $10 with $2 and $5 notes'); eq((5 <= 5, 2 <= 4), (True, True), 'explore 2 fits the notes of the money pages (5 two-dollar, 4 five-dollar)')
    mo = [b['items'] for b in sl['s-explore2-ans']['blocks'] if b.get('type') == 'money']; eq(mo, [[dict(v='$2', n=5)], [dict(v='$5', n=2)]], 's-explore2-ans notes')
    # ---------------------------------------------------------------- Mini-lesson
    t = tags_of(sl['s-m1']['blocks']); eq(t, [('car', 11), ('shoe', 6)], 's-m1 tags'); eq(total(11, 6), 17, 's-m1 total'); eq(17 > 15, True, 's-m1 not enough'); eq(count_up(15, 17), 2, 's-m1 needs 2 more')
    eq(total(4, 9) > 12 and count_up(12, 13) == 1, True, 's-m1 your turn: $12 is not enough for 4 and 9, 1 more')
    t = tags_of(sl['s-m2']['blocks']); eq(t, [('glue', 5)] * 3, 's-m2 tags'); eq(total(5, 5, 5), 15, 's-m2'); eq(total(2, 2, 2, 2, 2), 10, 's-m2 your turn')
    rows = [b for b in sl['s-m3']['blocks'] if b.get('type') == 'table'][0]['rows']; eq([r[:2] for r in rows], [['0', '12'], ['1', '7'], ['2', '2']], 's-m3 money left after 0, 1, 2 five-dollar notes')
    eq([12 - 5 * int(r[0]) for r in rows], [int(r[1]) for r in rows], 's-m3 money left is recomputed')
    filled = [b for b in sl['s-m3a']['blocks'] if b.get('type') == 'table'][0]['rows']
    eq([r[2] for r in filled], ['6', 'X', '1'], 's-m3a filled column')
    eq([(left // 2 if left % 2 == 0 else 'X') for left in (12, 7, 2)], [6, 'X', 1], 's-m3a recomputed'); eq(sorted(ways(12, (2, 5))), [(1, 2), (6, 0)], 's-m3 exactly two ways for $12')
    eq(5 * 3 > 12, True, 's-m3 a third five-dollar note is too much'); eq(6 > 5, True, 's-m3 six two-dollar notes is more than the 5 in the kit: written, not laid out')
    eq([b for b in sl['s-m3']['blocks'] if b.get('type') == 'table'][0]['rows'][0][2], '[]', 's-m3 hides the answers')
    t = tags_of(sl['s-m4']['blocks']); eq(t, [('cup', 8), ('pencil', 3)], 's-m4 tags'); eq((total(8, 3), count_up(total(8, 3), total(10, 10))), (11, 9), 's-m4 total then change')
    # ---------------------------------------------------------------- Start here
    q = T['S1']; tg = tags_of(q); eq([p for _, p in tg], [3, 5, 7, 8], 'S1 tags'); w = [c for c in itertools.combinations([p for _, p in tg], 2) if total(*c) == 10]; eq(w, [(3, 7)], 'S1 exactly one pair of different tags')
    eq(all(kit[i] == p for i, p in tg), True, 'S1 tags are kit tags with the kit prices'); eq('different' in q['text'], True, 'S1 says two different things'); eq(q['val'], [3, 7], 'S1 val'); eq(nums(q['text']), [10], 'S1 budget')
    q = T['S2']; eq(nums(q['text']), [7, 8], 'S2 text'); eq(total(7, 8), 15, 'S2'); eq(q['val'], [15], 'S2 val'); eq(tags_of(q), [('ruler', 7), ('cup', 8)], 'S2 tags')
    q = T['S3']; eq(nums(q['text']), [20, 14], 'S3 text'); eq(count_up(14, 20), 6, 'S3'); eq(q['val'], [6], 'S3 val'); eq(tags_of(q), [('jar', 14)], 'S3 tag')
    q = T['S4']; a = nums(q['text']); eq(a, [10, 7, 5], 'S4 text'); eq((total(7, 5) <= 10, count_up(10, total(7, 5))), (False, 2), 'S4'); eq(q['val'], ['No', 2], 'S4 val'); eq(tags_of(q), [('ruler', 7), ('glue', 5)], 'S4 tags')
    q = T['S5']; eq(nums(q['text']), [7], 'S5 text'); eq(total(7, 7, 7), 21, 'S5'); eq(q['val'], [7, 7, 7, 21, 21], 'S5 val')
    q = T['S6']; rows = q['visual']['rows']; had = {r[0]: r[1:] for r in rows}
    eq(count_up(12, 20), 8, 'S6 Ravi left'); eq(count_up(6, 15), 9, 'S6 Aisha spent'); eq(total(8, 9), 17, 'S6 Kumar had'); eq(q['val'], [8, 9, 17], 'S6 val')
    eq([r[1:] for r in rows], [['20', '12', '[]'], ['15', '[]', '6'], ['[]', '8', '9']], 'S6 table')
    eq(sum(x['mins'] for x in d['tiers']['start']) <= 20, True, 'Start here within 20 minutes'); eq(max(max(nums(x['text']) or [0]) for x in d['tiers']['start']) <= 20, True, 'Start here money within $20')
    # ---------------------------------------------------------------- Think harder
    q = T['T1']; eq(nums(q['text']), [20, 2, 7, 20], 'T1 text'); w = ways(20, (2, 7)); eq(sorted(w), [(3, 2), (10, 0)], 'T1 exactly two ways (pens, books)'); eq(q['val'][:3], [10, 'X', 3], 'T1 val')
    tbl = [(books, (20 - 7 * books) // 2 if (20 - 7 * books) % 2 == 0 else 'X') for books in (0, 1, 2)]; eq(tbl, [(0, 10), (1, 'X'), (2, 3)], 'T1 table rows'); eq(7 * 3 > 20, True, 'T1 three books are too much (X)')
    eq([r[0] for r in q['visual']['rows']], ['0', '1', '2', '3'], 'T1 table is by number of books, to the stopping point'); eq(q['val'], [10, 'X', 3, 'X', 2], 'T1 val with the last row')
    q = T['T2']; eq(nums(q['text']), [16, 2, 5, 2], 'T2 text'); w = ways(16, (2, 5)); eq(sorted(w), [(3, 2), (8, 0)], 'T2 exactly two ways'); eq(q['val'], ['No', 2, 3], 'T2 val')
    eq(len(w) == 1, False, 'T2 the child list (eight 2s only) is not complete'); eq((8 * 2, 2 * 5 + 3 * 2), (16, 16), 'T2 both ways make 16')
    q = T['T3']; eq(nums(q['text']), [9, 4, 2], 'T3 text'); eq((total(9, 4, 2), count_up(total(9, 4, 2), 50)), (15, 35), 'T3'); eq(q['val'], [15, 35], 'T3 val')
    q = T['T4']; eq(nums(q['text']), [3, 4, 18], 'T4 text'); w = ways(18, (3, 4)); eq(sorted(w), [(2, 3), (6, 0)], 'T4 exactly two ways (rubbers, pencils)')
    st = [s['s'] for s in q['tf']]; eq(len(st), 4, 'T4 four statements')
    claims = [(6, 0) in w, (2, 3) in w, False, (4, 2) in w]      # statement 3 is about the same way in another order: not a new way
    eq(claims, [True, True, False, False], 'T4 truth values'); eq(q['val'], ['True', 'True', 'False', 'False'], 'T4 val'); eq((total(12, 8)), 20, 'T4 statement 4 costs 20, not 18')
    # ---------------------------------------------------------------- Go further
    q = T['G1']; w = ways(20, (10, 5, 2)); eq(sorted(w), [(0, 0, 10), (0, 2, 5), (0, 4, 0), (1, 0, 5), (1, 2, 0), (2, 0, 0)], 'G1 exactly six ways'); eq(len(w), 6, 'G1 count')
    eq([r[1:] for r in q['visual']['rows']][0], ['2', '0', '0'], 'G1 way 1 is shown'); eq(sum(1 for r in q['visual']['rows'] if r[1] == '[]'), 6, 'G1 six empty rows: one more than there are ways to find'); eq(q['val'], [6], 'G1 val')
    q = T['G2']; sols = [(s, p) for s in range(0, 8) for p in range(0, 8) if s + p == 7 and 2 * s + 5 * p == 20]; eq(sols, [(5, 2)], 'G2 exactly one answer'); eq(q['val'], [5, 2], 'G2 val'); eq(nums(q['text']), [2, 5, 20], 'G2 text')
    q = T['G3']; eq([p for _, p in tags_of(q)], [2, 3, 5, 7, 8], 'G3 tags are kit tags'); eq(all(kit[i] == p for i, p in tags_of(q)), True, 'G3 prices match the kit page'); eq(q['val'], ['open'], 'G3 is open')
    # ---------------------------------------------------------------- Investigation: amounts from $1 to $12 that $2 and $5 notes cannot make
    cannot = [x for x in range(1, 13) if not ways(x, (2, 5))]; eq(cannot, [1, 3], 'I1 cannot pay $1 or $3'); eq(inv['val'], ['1', '3'], 'I1 val'); eq(bool(ways(7, (2, 5))), True, 'I1 first step: $7 can be paid')
    eq(nums(inv['first']), [7, 2, 5], 'I1 first step text')
    # ---------------------------------------------------------------- talk, exit
    eq(d['talk']['answer'].startswith('The second child is right'), True, 'talk names the second child')
    q = X['E1']; opts = [nums(o) for o in q['mcq']['options']]; right = [i + 1 for i, o in enumerate(opts) if total(*o) == 11]; eq(right, [2], 'E1 one correct option'); eq(q['val'], right, 'E1 val'); eq(nums(q['text']), [11, 3, 4, 5, 8], 'E1 text')
    eq([total(*o) for o in opts], [7, 11, 9, 13], 'E1 option totals')
    q = X['E2']; eq(nums(q['text']), [12, 6, 8], 'E2 text'); eq(total(6, 8) > 12, True, 'E2 is No'); eq(q['val'], ['No'], 'E2 val')
    q = X['E3']; eq(nums(q['text']), [3], 'E3 text'); eq(total(3, 3, 3, 3), 12, 'E3'); eq(q['val'], [12], 'E3 val')
    # ---------------------------------------------------------------- home
    eq(nums(H['H1']['text']), [10, 3, 4], 'H1 numbers'); eq(total(3, 4) <= 10, True, 'H1 is Yes'); eq(H['H1']['val'], 'Yes', 'H1 val')
    eq(nums(H['H2']['text']), [3], 'H2 numbers'); eq(total(3, 3, 3, 3, 3), 15, 'H2'); eq(H['H2']['val'], 15, 'H2 val')
    eq(nums(H['H3']['text']), [20, 8, 5], 'H3 numbers'); eq(count_up(total(8, 5), 20), 7, 'H3'); eq(H['H3']['val'], 7, 'H3 val')
    eq(nums(H['H4']['text']), [18, 2, 5], 'H4 numbers'); w = ways(18, (2, 5)); eq(sorted(w), [(4, 2), (9, 0)], 'H4 exactly two ways'); eq(H['H4']['val'], [0, 9, 2, 4], 'H4 val')
    eq((86 - 40, 86 - 4), (46, 82), 'H5 rewind'); eq(H['H5']['val'], [46, 82], 'H5 val'); eq(H['H5'].get('rewind_of'), 'Term 1 Lesson 6', 'H5 is the rewind item')
    eq(len([h for h in d['home_practice'] if h['tier'] == 'start']) >= 3, True, 'home has 3 Start here items')
    # ---------------------------------------------------------------- online practice
    items = {i['id']: i for i in d['online_practice']['items']}
    for cid, env in BASE_ENV.items():
        eq(items[cid]['answer'], ORACLES[cid](env), cid + ' authored answer')
    eq(items['c4']['answer'], 'No', 'c4 authored'); eq(total(7, 5) > 10, True, 'c4 authored total')
    for it in items.values():
        for s_ in it.get('slips', []):
            if it['type'] == 'number': eq(it['answer'] in s_['a'], False, it['id'] + ' slip is wrong')
    for env in [dict(zip(('a', 'b'), c)) for c in itertools.product(items['g1']['tpl']['vars']['a'], items['g1']['tpl']['vars']['b'])]:
        sols = [(s, p) for s in range(0, 12) for p in range(0, 12) if s + p == env['a'] + env['b'] and 2 * s + 5 * p == 2 * env['a'] + 5 * env['b']]
        eq(len(sols), 1, f'g1 {env} has exactly one answer')
    for t in items['t2']['tpl']['vars']['t']:
        eq(t % 2, 0, f't2 {t} is even so the count formula t//10+1 holds'); eq(_ways_count(t), t // 10 + 1, f't2 {t} ways')
    for p in items['g2']['tpl']['vars']['p']: eq(_cost4(p) < 50, True, f'g2 {p} stays under $50')
    for a, b, c in itertools.product(items['t1']['tpl']['vars']['a'], items['t1']['tpl']['vars']['b'], items['t1']['tpl']['vars']['c']): eq(a + b + c < 50, True, 't1 total under 50')
    for b, k in itertools.product(items['t3']['tpl']['vars']['b'], items['t3']['tpl']['vars']['k']): eq(5 * b + 2 * k <= 40, True, 't3 amount')
    # ---------------------------------------------------------------- kit contract and hand-offs (this lesson has no kit page; the tags and notes come from Lessons 24 and 25)
    kc = {r['piece']: r for r in d['materials']['kit_contract']}
    for r in kc.values(): eq(r['supplied'] >= r['max_used'], True, 'kit contract ' + r['piece'])
    eq(d['workbook']['kits'], [], 'no kit page in this lesson'); eq(len(six), 6, 'six tags at once is the most'); eq(kc['price tags with a price (from the lesson before)']['max_used'], 6, 'tag contract max_used')
    for where, ob in (('slides', d['slides']), ('tiers', d['tiers']), ('exit', d['exit']), ('home', d['home_practice'])):
        for it, pr in tags_of(ob):
            if it in kit: eq(kit[it], pr, f'{where}: the {it} tag shows the Lesson 25 kit price')
    nm = ' '.join(d['parent']['next_materials']).lower(); eq(('16' in nm, 'tiles' in nm), (True, True), 'hand-off to Lesson 27 names the 16 grid tiles')
    pm = ' '.join(p25['parent']['next_materials']).lower(); eq(('price tags' in pm and 'play money' in pm and 'nothing new' in pm), True, 'Lesson 25 hands off the tags and the money with nothing new to cut')
    return n
