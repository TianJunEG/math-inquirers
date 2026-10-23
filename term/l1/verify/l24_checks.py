"""Independent answer checks for Level 1 Term 3 Lesson 4 (Lesson 24, Dollars and Change).

All money is held in whole cents here ($1 = 100 cents), so nothing depends on how the lesson writes an amount. Every count of coins and notes is recomputed from the pieces drawn in the figures,
every 'ways' and 'fewest' answer is found by brute force or by dynamic programming (not by the greedy method that the lesson teaches), and the printed kit pages are read back from the kit builder
(the pieces on each page are counted in its SVG) and compared with the kit contract and with the most any task uses. The Term 2 Lesson 9 token page (30 tokens) is read from l19.json.
The class and workbook coin sets and (price, paid) pairs are listed here and checked to be disjoint, and clear of the Quest gate (50, 20, 20, 5 cents; $7 paid with $10).
"""
import itertools
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(HERE), 'tools'))

COINS = [5, 10, 20, 50]
PIECES = [100, 200, 500, 1000, 5000]          # $1 coin, $2, $5, $10, $50 notes: there is no $20 note


def cents(v):
    v = str(v).replace('¢', 'c')
    if v.endswith('c'): return int(v[:-1])
    if v.startswith('$'): return int(v[1:]) * 100
    raise AssertionError('piece ' + v)


def pieces(fig):
    out = []
    for it in fig['items']:
        it = {'v': it} if isinstance(it, str) else it
        out += [cents(it['v'])] * int(it.get('n', 1))
    return out


def total(fig):
    return sum(pieces(fig))


def figs_in(x, kind, out=None):
    out = [] if out is None else out
    if isinstance(x, dict):
        if x.get('type') == kind: out.append(x)
        for v in x.values(): figs_in(v, kind, out)
    elif isinstance(x, list):
        for v in x: figs_in(v, kind, out)
    return out


def fewest(n, den):
    """Fewest pieces that make n (dynamic programming over every amount, not the greedy rule)."""
    best = [0] + [10 ** 9] * n
    for a in range(1, n + 1):
        for p in den:
            if p <= a and best[a - p] + 1 < best[a]: best[a] = best[a - p] + 1
    return best[n]


def multisets(n_coins, amount, den=COINS):
    return sorted(c for c in itertools.combinations_with_replacement(den, n_coins) if sum(c) == amount)


# --------------------------------------------------------------------------------- the registry of what each part of the lesson asks
QUEST_SET = (5, 20, 20, 50)                  # Quest gate: count 50c, 20c, 20c, 5c
QUEST_CHANGE = (700, 1000)                   # Quest gate: a $7 toy paid with $10
CLASS_SETS = {'sneak': (5, 5, 10, 10, 10), 'explore A': (10, 10, 50), 'explore B': (5, 20, 20, 20), 'mini worked': (5, 10, 10, 50), 'mini try': (5, 20, 20)}
WORKBOOK_SETS = {'S1': (5, 5, 20, 50), 'S4 row': (5, 5, 10, 10, 20, 50), 'T4 A': (10, 20, 50), 'T4 B': (10, 20, 20, 20), 'T4 C': (5, 5, 50), 'E1': (10, 10, 20, 50)}
CLASS_CHANGE = {'explore sweet': (40, 50), 'explore ruler': (600, 1000), 'mini ball': (800, 1000), 'mini pencil': (35, 50), 'mini try': (500, 1000)}
WORKBOOK_CHANGE = {'S6': (300, 500), 'T1': (900, 1000), 'T3': (60, 100), 'G1b': (3700, 5000), 'G3': (90, 100), 'E2': (400, 1000)}

# --------------------------------------------------------------------------------- oracles for the online practice templates
ORACLES = {
    'c1': lambda e: sum([20] * e['a'] + [10] * e['b'] + [5] * e['c']),
    'c2': lambda e: sum([10] * e['a'] + [5] * e['b'] + [2] * e['c']),
    'c3': lambda e: next(ch for ch in range(0, 6) if e['p'] + ch == 5),
    'c4': lambda e: next(ch for ch in range(0, 11) if e['p'] + ch == 10),
    't1': lambda e: next(ch for ch in range(0, 101) if e['p'] + ch == 100),
    't2': lambda e: next(ch for ch in range(0, 11) if e['a'] + e['b'] + ch == 10),
    'g1': lambda e: fewest(e['n'], [1, 2, 5, 10, 50]),
}
BASE_ENV = {'c1': {'a': 1, 'b': 1, 'c': 1}, 'c2': {'a': 1, 'b': 1, 'c': 1}, 'c3': {'p': 3}, 'c4': {'p': 6}, 't1': {'p': 60}, 't2': {'a': 4, 'b': 5}, 'g1': {'n': 73}}


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
    M = lambda x: figs_in(x, 'money')
    tags = lambda x: figs_in(x, 'price_tag')
    cat = lambda x: tuple(sorted(pieces(x)))

    # ---------------------------------------------------------------- the pieces are disjoint, and clear of the Quest
    eq(len(set(CLASS_SETS.values())), len(CLASS_SETS), 'class coin sets differ')
    eq(len(set(WORKBOOK_SETS.values())), len(WORKBOOK_SETS), 'workbook coin sets differ')
    eq(sorted(set(CLASS_SETS.values()) & set(WORKBOOK_SETS.values())), [], 'no workbook coin set repeats a class coin set')
    eq(QUEST_SET in set(CLASS_SETS.values()) | set(WORKBOOK_SETS.values()), False, 'no set is the Quest coin set')
    eq(sorted(set(CLASS_CHANGE.values()) & set(WORKBOOK_CHANGE.values())), [], 'no workbook (price, paid) pair repeats a class pair')
    eq(QUEST_CHANGE in set(CLASS_CHANGE.values()) | set(WORKBOOK_CHANGE.values()), False, 'no pair is the Quest pair')
    eq(len(set(CLASS_CHANGE.values())) + len(set(WORKBOOK_CHANGE.values())), len(CLASS_CHANGE) + len(WORKBOOK_CHANGE), 'change pairs are all different')
    eq(any(p not in (5, 10, 20, 50, 100, 200, 500, 1000, 5000) for s_ in list(CLASS_SETS.values()) + list(WORKBOOK_SETS.values()) for p in s_), False, 'only real denominations, no $20 note')

    # ---------------------------------------------------------------- sneak-peek and warm-up
    sp = d['sneak_peek']
    eq(sum([10] * 3 + [5] * 2), 40, 'sneak 1'); eq(sp['val1'], 40, 'sneak val1'); eq(cat(M(sl['s-sneak']['blocks'])[0]), CLASS_SETS['sneak'], 'sneak slide picture is 3 tens and 2 fives')
    eq(10 * 10, cents('$1'), 'sneak 2: ten 10c coins make $1'); eq(('10 ten-cent coins' in sp['q2'], 'one-dollar coin' in sp['q2']), (True, True), 'sneak 2 text')
    eq(cat(M(sl['s-rem2']['blocks'])[0]), (5, 10, 20, 50), 'warm-up coins are 5, 10, 20, 50'); eq(sorted(pieces(M(sl['s-rem2']['blocks'])[0])), [5, 10, 20, 50], 'warm-up order')
    eq([b for b in sl['s-rem1']['blocks'] if b.get('t') == 'numrow'][0]['items'], list(range(5, 101, 5)), 'warm-up number row counts in 5s to 100')
    nl = [b for b in sl['s-rem3']['blocks'] if b.get('type') == 'number_line'][0]
    eq((nl['marks'], 35 - 28, 50 - 46), ([28, 35], 7, 4), 'warm-up count up')
    # ---------------------------------------------------------------- explore
    ways60 = [(a, b, c, e) for a in range(0, 5) for b in range(0, 7) for c in range(0, 5) for e in range(0, 3) if 5 * a + 10 * b + 20 * c + 50 * e == 60]
    eq(len(ways60) >= 5, True, 'there are many ways to make 60c from the kit coins')
    eq(((0, 6, 0, 0) in ways60, (0, 0, 3, 0) in ways60, (0, 0, 0, 1) in ways60 or (0, 1, 0, 1) in ways60), (True, True, True), 'explore 60c: six 10s, three 20s and 50 + 10 are all inside the kit supply')
    eq(max(w[1] for w in ways60), 6, 'most ten-cent coins a way to make 60c needs is 6 (kit supplies 6)'); eq(max(w[2] for w in ways60), 3, 'most twenty-cent coins is 3 (kit supplies 4)')
    A, B = M(sl['s-explore2']['blocks'])
    eq((cat(A), cat(B), total(A), total(B)), (CLASS_SETS['explore A'], CLASS_SETS['explore B'], 70, 65), 'explore 2 pictures'); eq(A['label'] + B['label'], 'Picture APicture B', 'explore 2 labels')
    tg = tags(sl['s-explore3']['blocks']); eq([t['price'] for t in tg], ['40¢', '$6'], 'explore 3 tags')
    eq((50 - 40, 1000 - 600), (10, 400), 'explore 3 changes'); eq(CLASS_CHANGE['explore sweet'], (40, 50), 'registry'); eq(1000 - 600, 4 * 100, 'ruler change is $4 = four $1 tokens (or two $2 notes)')
    # ---------------------------------------------------------------- mini-lesson
    m1 = M(sl['s-m1']['blocks']); eq([sorted(set(pieces(f))) for f in m1], [[5, 10, 20, 50, 100], [200, 500, 1000, 5000]], 's-m1 coins and notes')
    m2 = M(sl['s-m2']['blocks'])[0]; eq((cat(m2), total(m2)), (CLASS_SETS['mini worked'], 75), 's-m2 worked example'); run_ = list(itertools.accumulate(sorted(pieces(m2), reverse=True)))
    eq([f'{x}¢' for x in run_], [b for b in sl['s-m2']['blocks'] if b.get('t') == 'numrow'][0]['items'], 's-m2 counts biggest first: 50, 60, 70, 75')
    m3 = M((sl.get('s-m3-ans') or sl['s-m3'])['blocks']); eq([total(f) for f in m3], [100, 100, 100], 's-m3: $1, two 50c and ten 10c are all 100c'); eq([len(pieces(f)) for f in m3], [1, 2, 10], 's-m3 pieces')
    tg = tags(sl['s-m4']['blocks']); eq(tg[0]['price'], '$8', 's-m4 price'); eq(total(M(sl['s-m4']['blocks'])[0]), 1000, 's-m4 pays $10'); eq((1000 - 800) // 100, 2, 's-m4 change $2')
    nl4 = [b for b in sl['s-m4']['blocks'] if b.get('type') == 'number_line'][0]; eq((nl4['start'], nl4['end'], nl4['prefix']), (8, 10, '$'), 's-m4 line from $8 to $10'); eq('jumps' in nl4, False, 's-m4 line carries no answer jump')
    eq(50 - 35, 15, 'mini cents change'); eq(CLASS_CHANGE['mini pencil'], (35, 50), 'registry')
    m5 = M(sl['s-m5']['blocks']); eq((cat(m5[0]), total(m5[0])), (CLASS_SETS['mini try'], 45), 's-m5 count'); eq(1000 - 500, 500, 's-m5 change $5'); eq(tags(sl['s-m5']['blocks'])[0]['price'], '$5', 's-m5 tag')
    eq([b for b in sl['s-m5a']['blocks'] if b.get('t') == 'answer'][0]['text'], 'Count: 45¢. Change: $5.', 's-m5a answers')
    # ---------------------------------------------------------------- Start here
    q = T['S1']; f = q['visual']; eq((cat(f), total(f), q['val']), (WORKBOOK_SETS['S1'], 80, [80]), 'S1')
    q = T['S2']; f = q['visual']; eq((total(f) // 100, q['val'], all(p >= 200 for p in pieces(f))), (19, [19], True), 'S2 notes only'); eq(sorted(pieces(f)), [200, 200, 500, 1000], 'S2 notes')
    q = T['S3']; eq((50 // 10, 50 // 5, q['val']), (5, 10, [5, 10]), 'S3'); eq(pieces(q['visual']), [50], 'S3 picture is one 50c coin')
    q = T['S4']; row = pieces(q['visual']); eq(tuple(sorted(row)), WORKBOOK_SETS['S4 row'], 'S4 row')
    subs = sorted({tuple(sorted(row[i] for i in idx)) for r in range(1, len(row) + 1) for idx in itertools.combinations(range(len(row)), r) if sum(row[i] for i in idx) == 55})
    eq(subs, [(5, 50)], 'S4 only one set of coin values makes 55c'); eq(q['val'], [50, 5], 'S4 val (the two coins circled)'); eq(sum(row), 100, 'S4 row is larger than needed (it holds 100c)')
    q = T['S5']; fs = M(q); eq([total(x) for x in fs], [200, 100], 'S5 pictures'); eq(('$2 note' if total(fs[0]) > total(fs[1]) else '$1 coin', q['val']), ('$2 note', ['$2 note']), 'S5'); eq(q['parts'][0]['choices'], ['$2 note', '$1 coin'], 'S5 choices')
    q = T['S6']; eq((tags(q)[0]['price'], total(M(q)[0]), (total(M(q)[0]) - 300) // 100, q['val']), ('$3', 500, 2, [2]), 'S6'); eq(WORKBOOK_CHANGE['S6'], (300, 500), 'registry')
    eq(sum(x['mins'] for x in d['tiers']['start']) <= 20, True, 'Start here within 20 minutes')
    # ---------------------------------------------------------------- Think harder
    q = T['T1']; tt = re.findall(r'\$\d+', q['text'])[:2]; paid = 1000 if 'ten-dollar note' in q['text'] else 0; cost = sum(int(p[1:]) for p in tt)
    eq((tt, cost, paid // 100 - cost, q['val']), (['$4', '$5'], 9, 1, [9, 1]), 'T1')
    q = T['T2']; ways = [(a, b) for a in range(0, 6) for b in range(0, 3) if 10 * a + 20 * b == 50]
    eq(ways, [(1, 2), (3, 1), (5, 0)], 'T2 brute force: exactly 3 ways to make 50c from 10c and 20c coins'); rows = q['visual']['rows']
    eq((int(rows[0][0]), int(rows[0][1]), rows[1], rows[2]), (5, 0, ['[]', '[]'], ['[]', '[]']), 'T2 one row given, two to find'); eq(sorted(q['val']), [[1, 2], [3, 1]], 'T2 val = the other two ways')
    q = T['T3']; eq((cents('$1'), cents('$1') - 40, q['val']), (100, 60, [100, 60]), 'T3 works backwards: $1 paid, 40c change, the price is 60c'); eq('40¢' in q['text'], True, 'T3 text'); eq(WORKBOOK_CHANGE['T3'], (60, 100), 'registry')
    q = T['T4']; sets_ = {f['label']: f for f in M(q)}; tot = {k: total(v) for k, v in sets_.items()}
    eq(tot, {'Set A': 80, 'Set B': 70, 'Set C': 60}, 'T4 totals'); eq(max(tot, key=tot.get), 'Set A', 'T4 most money'); eq(max(sets_, key=lambda k: len(pieces(sets_[k]))), 'Set B', 'T4 Set B has the most coins but not the most money')
    eq((tot['Set A'] - tot['Set C'], q['val']), (20, ['A', 20]), 'T4 difference'); eq([cat(sets_['Set A']), cat(sets_['Set B']), cat(sets_['Set C'])], [WORKBOOK_SETS['T4 A'], WORKBOOK_SETS['T4 B'], WORKBOOK_SETS['T4 C']], 'T4 registry')
    # ---------------------------------------------------------------- Go further
    q = T['G1']; den = sorted(pieces(q['visual'])); eq(den, [100, 200, 500, 1000, 5000], 'G1 has no $20 note')
    eq((fewest(73, [1, 2, 5, 10, 50]), fewest(50 - 37, [1, 2, 5, 10, 50]), q['val']), (5, 3, [5, 3]), 'G1 by dynamic programming')
    best73 = sorted(c for c in itertools.combinations_with_replacement([1, 2, 5, 10, 50], 5) if sum(c) == 73); eq(best73, [(1, 2, 10, 10, 50)], 'G1: exactly one way to make $73 in 5 pieces')
    best13 = sorted(c for c in itertools.combinations_with_replacement([1, 2, 5, 10, 50], 3) if sum(c) == 13); eq(best13, [(1, 2, 10)], 'G1: exactly one way to make the $13 change in 3 pieces')
    eq(all(fewest(k, [1, 2, 5, 10, 50]) == k // 50 + (k % 50) // 10 + (k % 10) // 5 + ((k % 10) % 5) // 2 + ((k % 10) % 5) % 2 for k in range(1, 100)), True, 'the greedy count used by the online template is the fewest for every amount to $99')
    eq(WORKBOOK_CHANGE['G1b'], (3700, 5000), 'registry')
    q = T['G2']; ps = [p // 100 for p in pieces(q['visual'])]; sums = sorted({sum(c) for r in range(1, 4) for c in itertools.combinations(ps, r)})
    eq((sorted(ps), sums, len(sums), q['val']), ([1, 2, 5], [1, 2, 3, 5, 6, 7, 8], 7, [7, [1, 2, 3, 5, 6, 7, 8]]), 'G2'); eq(4 in sums, False, 'G2 $4 cannot be made')
    q = T['G3']; eq((tags(q)[0]['price'], 100 // 30, 100 - 3 * 30, 4 * 30 > 100, q['val']), ('30¢', 3, 10, True, [3, 10]), 'G3'); eq(WORKBOOK_CHANGE['G3'], (90, 100), 'registry')
    # ---------------------------------------------------------------- Investigation: every multiset of 3 or 4 kit coins that makes 35c
    kit = {5: 4, 10: 6, 20: 4, 50: 2}
    ok = lambda ms: all(ms.count(c) <= kit[c] for c in set(ms))
    w2, w3, w4 = multisets(2, 35), multisets(3, 35), multisets(4, 35)
    eq((w2, w3, w4), ([], [(5, 10, 20)], [(5, 5, 5, 20), (5, 10, 10, 10)]), 'I1 ways with 2, 3 and 4 coins'); eq(all(ok(list(w)) for w in w3 + w4), True, 'I1 every way is inside the kit')
    eq(d['tiers']['investigation']['val'], [str(len(w3)), str(len(w4))], 'I1 val'); eq(max(w.count(5) for w in w3 + w4), 3, 'I1 uses at most three 5c coins (kit supplies 4)')
    # ---------------------------------------------------------------- talk
    eq((50 < 100, 2 * 50 == 100), (True, True), 'talk: 50c is half of $1; two 50c coins make $1'); eq(d['talk']['answer'].startswith('No.'), True, 'talk answer')
    # ---------------------------------------------------------------- exit
    q = X['E1']; eq((cat(q['visual']), total(q['visual']), q['val']), (WORKBOOK_SETS['E1'], 90, [90]), 'E1')
    q = X['E2']; opts = [int(o[1:]) for o in q['mcq']['options']]; right = [i + 1 for i, o in enumerate(opts) if o == 10 - 4]
    eq((right, q['val'], opts), ([3], [3], [4, 5, 6, 14]), 'E2'); eq(WORKBOOK_CHANGE['E2'], (400, 1000), 'registry')
    q = X['E3']; eq((10 + 2 + 2 + 1, q['val']), (15, [15]), 'E3'); eq('two $2 notes' in q['text'] and '$10 note' in q['text'] and '$1 coin' in q['text'], True, 'E3 text')
    # ---------------------------------------------------------------- home
    eq((20 + 20 + 10 + 5, H['H1']['val']), (55, 55), 'H1'); eq((5 - 2, H['H2']['val']), (3, 3), 'H2'); eq((10 - (3 + 2), H['H3']['val']), (5, 5), 'H3')
    eq((fewest(46, [1, 2, 5, 10, 50]), H['H4']['val']), (6, 6), 'H4 by dynamic programming'); eq(sorted(c for c in itertools.combinations_with_replacement([1, 2, 5, 10, 50], 6) if sum(c) == 46), [(1, 5, 10, 10, 10, 10)], 'H4 one way in 6 pieces')
    eq((list(range(40, 70, 5))[3:], H['H5']['val'], H['H5'].get('rewind_of')), ([55, 60, 65], [55, 60, 65], 'Term 1 Lesson 4'), 'H5 rewind')
    eq(len([h for h in d['home_practice'] if h['tier'] == 'start']) >= 3, True, 'home has 3 Start here items')
    # ---------------------------------------------------------------- online practice
    items = {i['id']: i for i in d['online_practice']['items']}
    for cid, want in (('c1', 35), ('c2', 17), ('c3', 2), ('c4', 4), ('t1', 40), ('t2', 1), ('g1', 5), ('g2', 7)):
        eq(items[cid]['answer'] if 'answer' in items[cid] else None, want, cid + ' authored answer')
    eq(items['t3']['answer'], 3, 't3'); eq(items['t3']['type'], 'number', 't3 is one number'); eq(10 * 3 + 20 * 1, 50, 't3 coins make 50c'); eq(items['c5']['answer'], 'the $2 note', 'c5')
    for cid, env in BASE_ENV.items():
        eq(ORACLES[cid](env), items[cid]['answer'], cid + ' oracle at the authored numbers')
    eq(total(items['c1']['fig_base']), 35, 'c1 picture')
    eq(sum(cents(i['v']) * i['n'] for i in items['c2']['fig_base']['items']) // 100, 17, 'c2 picture')
    for it in items.values():
        for s_ in it.get('slips', []):
            if it['type'] == 'number': eq(it['answer'] in s_['a'], False, it['id'] + ' slip is wrong')
    # a variant never reads '1 dollars': every templated change is at least 2 dollars, and totals stay whole
    for cid in ('c3', 'c4', 't2'):
        tp = items[cid]['tpl']; names = list(tp['vars'])
        for combo in itertools.product(*[tp['vars'][k] for k in names]):
            env = dict(zip(names, combo)); eq(ORACLES[cid](env) >= 2, True, f'{cid} {env} change is 2 or more dollars')
    for combo in itertools.product(*[items['c1']['tpl']['vars'][k] for k in 'abc']):
        e = dict(zip('abc', combo)); eq(ORACLES['c1'](e) <= 105, True, 'c1 total stays near a dollar')
    # ---------------------------------------------------------------- the kit pages: read back from the kit builder
    import figs3
    printed = {}
    for pg in (1, 2):
        svg = figs3.render_kit({'type': 'play_money', 'page': pg})
        for lab in ('5¢', '10¢', '20¢', '50¢', '$2', '$5', '$10', '$50'):
            c = len(re.findall('>' + re.escape(lab) + '<', svg))
            if c: printed[lab] = c
    eq(printed, {'5¢': 4, '10¢': 6, '20¢': 4, '50¢': 2, '$2': 5, '$5': 4, '$10': 3, '$50': 1}, 'printed pieces: 16 coins and 13 notes')
    eq(sum(printed.values()), 29, '29 pieces')
    names = {'five-cent coins': '5¢', 'ten-cent coins': '10¢', 'twenty-cent coins': '20¢', 'fifty-cent coins': '50¢', 'two-dollar notes': '$2', 'five-dollar notes': '$5', 'ten-dollar notes': '$10', 'fifty-dollar notes': '$50'}
    for r in d['materials']['kit_contract']:
        if r['piece'] in names: eq(r['supplied'], printed[names[r['piece']]], r['piece'] + ' supplied matches the printed page')
        eq(r['supplied'] >= r['max_used'], True, r['piece'] + ' supplied covers the most used')
    l20 = json.load(open(os.path.join(os.path.dirname(HERE), 'lessons', 'l19.json')))
    eq(len([x for x in l20['workbook']['kits'][0]['labels'] if x == '$1']), 30, 'Term 2 Lesson 9 prints 30 $1 tokens')
    tok = [r for r in d['materials']['kit_contract'] if 'one-dollar' in r['piece']][0]; eq((tok['supplied'], tok['max_used'] <= tok['supplied']), (30, True), 'tokens supplied')
    eq((1000 - 600) // 100 <= 5, True, 'explore ruler change uses at most four $1 tokens (the contract maximum is 5)')
    # ---------------------------------------------------------------- hand-off to the next lesson (price tags: 12 tags)
    nm = ' '.join(d['parent']['next_materials'])
    eq(('12' in nm, 'price-tag' in nm, 'play money' in nm, 'tokens' in nm), (True, True, True, True), 'hand-off to Lesson 25 names the 12 tags, the money and the tokens')
    eq(d['workbook']['kits'][0]['page'], 1, 'kit page 1 is the coins'); eq(d['workbook']['kits'][1]['page'], 2, 'kit page 2 is the notes')
    return n
