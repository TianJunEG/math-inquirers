"""Independent answer checks for Level 1 Term 2 Lesson 20 (Find One First, with the end-of-term check).

Prices are found by trying every whole-dollar price (0 to 40) until the groups add back to the total; costs of many are built by adding the price
again and again; money left over is counted down one dollar at a time. Nothing uses the take-the-total-and-divide shortcut the lesson teaches.
The end-of-term check answers are recomputed the same way (a line of children is a list, sums are counted, shapes are solved by trial).
"""


def price_of_one(total, n, lim=40):
    """The whole-dollar price p such that n groups of p add back to the total (tried one price at a time). None if there is none."""
    for p in range(lim + 1):
        s = 0
        for _ in range(n):
            s += p
        if s == total:
            return p
    return None


def cost_of_many(p, n):
    s = 0
    for _ in range(n):
        s += p
    return s


def how_many_fit(p, money):
    n, spent = 0, 0
    while spent + p <= money:
        spent += p
        n += 1
    return n


def left_over(money, spent):
    left = money
    for _ in range(spent):
        left -= 1
    return left


def line_places(n):
    return list(range(1, n + 1))                 # 1st ... nth from the front


ORACLES = {
    'c1': lambda e: price_of_one(cost_of_many(e['u'], e['n']), e['n']),
    'c2': lambda e: cost_of_many(e['u'], e['n']),
    'c3': lambda e: (lambda t: {'u': price_of_one(t, e['n']), 'v': cost_of_many(price_of_one(t, e['n']), 2)})(cost_of_many(e['u'], e['n'])),
    'c4': lambda e: 'yes' if cost_of_many(e['k'], 4) == 12 else 'no',
    'c6': lambda e: cost_of_many(e['u'], e['n']),
    't1': lambda e: (lambda u: {'u': u, 'w': cost_of_many(u, e['m'])})(price_of_one(cost_of_many(e['u'], e['n']), e['n'])),
    't2': lambda e: cost_of_many(price_of_one(cost_of_many(e['u'], 12), 12), e['k']),
    't3': lambda e: how_many_fit(price_of_one(cost_of_many(e['u'], e['n']), e['n']), cost_of_many(e['u'], e['j'])),
    'g1': lambda e: price_of_one(cost_of_many(e['a'], 2), 2) + cost_of_many(price_of_one(cost_of_many(e['b'], 3), 3), 2),
    'g2': lambda e: left_over(e['m'], cost_of_many(price_of_one(cost_of_many(e['u'], e['n']), e['n']), e['k'])),
}
BASE_ENV = {'c1': {'n': 4, 'u': 5}, 'c2': {'n': 4, 'u': 3}, 'c6': {'n': 5, 'u': 3}, 't2': {'u': 2, 'k': 3}, 't3': {'n': 3, 'u': 3, 'j': 4}, 'g1': {'a': 5, 'b': 6}, 'g2': {'u': 3, 'n': 6, 'k': 4, 'm': 20}}


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
    items = {i['id']: i for i in d['online_practice']['items']}
    # ---- Start here
    eq(price_of_one(20, 4), 5, 'S1'); eq(T['S1']['val'], [5], 'S1 val'); eq(T['S1']['visual']['n'], 4, 'S1 picture has 4 pens')
    eq(cost_of_many(3, 4), 12, 'S2'); eq(T['S2']['val'], [12, 12], 'S2 val'); eq(T['S2']['parts'][0]['text'], '4 × 3 = [2]', 'S2 frame'); eq(T['S2']['visual']['n'], 4, 'S2 picture has 4 pens')
    s3 = T['S3']['visual']; eq((s3['units']['n'], s3['brace']['text']), (6, '$12'), 'S3 strip'); eq(price_of_one(12, 6), 2, 'S3'); eq(T['S3']['val'], [2], 'S3 val')
    s4 = T['S4']['visual']; eq((s4['units']['n'], s4['brace']['text']), (3, '$15'), 'S4 strip'); one = price_of_one(15, 3); eq((one, cost_of_many(one, 2)), (5, 10), 'S4'); eq(T['S4']['val'], [5, 10], 'S4 val')
    eq((cost_of_many(4, 4), price_of_one(12, 4), cost_of_many(3, 4) == 12), (16, 3, True), 'S5 Lily 4 groups of 4 is 16, not 12; the price is 3'); eq(T['S5']['val'], ['No', 3], 'S5 val'); eq(T['S5']['visual']['n'], 4, 'S5 picture has 4 pens')
    eq(cost_of_many(3, 5), 15, 'S6'); eq(T['S6']['val'], [15], 'S6 val'); eq(T['S6']['visual']['n'], 5, 'S6 picture has 5 books')
    eq(sum(q['mins'] for q in d['tiers']['start']) <= 20, True, 'Start here within 20 minutes')
    eq(all(cost_of_many(p, k) <= 40 for p, k in ((5, 4), (3, 4), (2, 6), (5, 3), (3, 5))), True, 'Start here products within 40')
    # ---- Think harder
    t1 = price_of_one(12, 3); eq((t1, cost_of_many(t1, 7)), (4, 28), 'T1'); eq(T['T1']['val'], [4, 28], 'T1 val'); eq(T['T1']['visual']['units']['n'], 3, 'T1 strip')
    dozen = 12; t2 = price_of_one(24, dozen); eq((t2, cost_of_many(t2, 3)), (2, 6), 'T2'); eq(T['T2']['val'], [2, 6], 'T2 val')
    t3 = price_of_one(18, 6); eq((t3, cost_of_many(t3, 4)), (3, 12), 'T3'); eq(T['T3']['val'], [3, 12], 'T3 val')
    t4 = price_of_one(15, 5); eq((t4, how_many_fit(t4, 12)), (3, 4), 'T4'); eq(T['T4']['val'], [3, 4], 'T4 val')
    # ---- Go further
    hat, scarf = price_of_one(10, 2), price_of_one(18, 3); eq((hat, scarf, hat + cost_of_many(scarf, 2)), (5, 6, 17), 'G1'); eq(T['G1']['val'], [5, 6, 17], 'G1 val')
    pen = price_of_one(18, 6); spent = cost_of_many(pen, 4); eq((pen, spent, left_over(20, spent)), (3, 12, 8), 'G2'); eq(T['G2']['val'], [3, 12, 8], 'G2 val')
    a, b = price_of_one(12, 4), price_of_one(20, 5); eq((a, b, 'Shop A' if a < b else 'Shop B'), (3, 4, 'Shop A'), 'G3'); eq(T['G3']['val'], [3, 4, 'Shop A'], 'G3 val')
    # ---- Investigation: the two packs have the same price for one pen
    eq((price_of_one(6, 2), price_of_one(15, 5)), (3, 3), 'I1 both packs cost $3 a pen'); eq(d['tiers']['investigation']['val'], ['3', '3'], 'I1 val')
    # ---- Exit ticket and home practice
    eq(price_of_one(9, 3), 3, 'E1'); eq(X['E1']['val'], [3], 'E1 val')
    opts = [int(o.lstrip('$')) for o in X['E2']['mcq']['options']]; eq([i for i, o in enumerate(opts, 1) if o == cost_of_many(2, 5)], [2], 'E2 exactly one option'); eq(X['E2']['val'], [2], 'E2 val')
    e3 = price_of_one(12, 4); eq((e3, cost_of_many(e3, 3)), (3, 9), 'E3'); eq(X['E3']['val'], [3, 9], 'E3 val')
    eq(price_of_one(10, 5), 2, 'H1'); eq(H['H1']['val'], 2, 'H1 val'); eq(cost_of_many(3, 6), 18, 'H2'); eq(H['H2']['val'], [18, 18], 'H2 val')
    eq(cost_of_many(price_of_one(12, 4), 2), 6, 'H3'); eq(H['H3']['val'], 6, 'H3 val'); eq(cost_of_many(price_of_one(24, 12), 4), 8, 'H4'); eq(H['H4']['val'], 8, 'H4 val')
    eq(price_of_one(12, 3) + price_of_one(10, 2), 9, 'H5'); eq(H['H5']['val'], 9, 'H5 val')
    # ---- Sneak-peek, warm-up, explore, mini, talk, optional slide
    eq((price_of_one(8, 4), cost_of_many(price_of_one(6, 3), 5)), (2, 10), 'sneak'); eq(d['sneak_peek']['val1'], 2, 'sneak 1 val')
    eq((price_of_one(12, 3), price_of_one(6, 2), price_of_one(15, 3)), (4, 3, 5), 'warm-up 1'); eq((cost_of_many(4, 3), cost_of_many(2, 5), cost_of_many(5, 4)), (12, 10, 20), 'warm-up 2')
    eq((price_of_one(20, 4), cost_of_many(5, 3), price_of_one(6, 2)), (5, 15, 3), 'warm-up 3')
    g = sl['s-rem2']['blocks'][0]; eq((g['n'], g['each'], cost_of_many(g['each'], g['n'])), (3, 4, 12), 'warm-up bags picture'); eq(sl['s-rem3']['blocks'][0]['units']['n'], 4, 'warm-up strip parts')
    eq((price_of_one(20, 4), cost_of_many(3, 4), price_of_one(20, 4), cost_of_many(5, 3)), (5, 12, 5, 15), 'explore')
    eq(sl['s-explore1']['blocks'][0]['rows'][0][0]['n'], 4, 'explore 1 table'); eq(sl['s-explore2']['blocks'][0]['rows'][1][0]['n'], 4, 'explore 2 table')
    eq(sl['s-explore3']['blocks'][0]['units']['n'], 4, 'explore 3 strip'); eq(sl['s-explore3']['blocks'][0]['brace']['text'], '$20', 'explore 3 total')
    m1 = price_of_one(15, 5); eq((m1, cost_of_many(m1, 2), cost_of_many(m1, 5)), (3, 6, 15), 'mini example and check'); eq(sl['s-m1']['blocks'][0]['units']['n'], 5, 's-m1 strip')
    eq((price_of_one(18, 6), cost_of_many(price_of_one(18, 6), 4)), (3, 12), 'mini your turn'); eq([r[2] for r in sl['s-m4a']['blocks'][0]['rows'][1:]], ['$3', '$12'], 's-m4a')
    eq(sl['s-m3b']['blocks'][0]['n'], 12, 'a dozen picture has 12 items')
    eq((price_of_one(12, 3), cost_of_many(price_of_one(12, 3), 6), 2 * 12), (4, 24, 24), 'talk: 6 books are 2 lots of 3 books')
    eq((price_of_one(6, 2), cost_of_many(price_of_one(6, 2), 4), 2 * 6), (3, 12, 12), 's-opt: 4 pens are 2 lots of 2 pens')
    eq([cost_of_many(3, k) for k in (1, 2, 3)], [3, 6, 9], 'M1'); eq((price_of_one(12, 3), cost_of_many(5, 4), price_of_one(20, 4)), (4, 20, 5), 'M2 and M3')
    # ---- online practice: authored answers, and the variants stay whole-dollar and within 40
    eq(price_of_one(20, 4), items['c1']['answer'], 'c1 authored'); eq(cost_of_many(3, 4), items['c2']['answer'], 'c2 authored')
    c3 = price_of_one(15, 3); eq([c3, cost_of_many(c3, 2)], [f['answer'] for f in items['c3']['fields']], 'c3 authored')
    eq(items['c4']['answer'], 'yes' if cost_of_many(4, 4) == 12 else 'no', 'c4 authored (Lily says 4)'); eq(items['c5']['answer'], 12, 'c5 a dozen')
    eq(cost_of_many(3, 5), items['c6']['answer'], 'c6 authored'); t1i = price_of_one(12, 3); eq([t1i, cost_of_many(t1i, 7)], [f['answer'] for f in items['t1']['fields']], 't1 authored')
    eq(cost_of_many(price_of_one(24, 12), 3), items['t2']['answer'], 't2 authored'); eq(how_many_fit(price_of_one(9, 3), 12), items['t3']['answer'], 't3 authored')
    eq(price_of_one(10, 2) + cost_of_many(price_of_one(18, 3), 2), items['g1']['answer'], 'g1 authored'); eq(left_over(20, cost_of_many(price_of_one(18, 6), 4)), items['g2']['answer'], 'g2 authored')
    for iid, keys in (('c1', ('n', 'u')), ('c2', ('n', 'u')), ('c6', ('n', 'u')), ('c3', ('n', 'u'))):
        vs = items[iid]['tpl']['vars']
        eq(all(cost_of_many(u, k) <= 40 for k in vs[keys[0]] for u in vs[keys[1]]), True, iid + ' variants within 40')
    vs = items['t1']['tpl']['vars']; eq(all(cost_of_many(u, m) <= 40 for u in vs['u'] for m in vs['m']), True, 't1 variants within 40')
    vs = items['t3']['tpl']['vars']; eq(all(cost_of_many(u, k) <= 40 for u in vs['u'] for k in vs['n'] + vs['j']), True, 't3 variants within 40')
    vs = items['g2']['tpl']['vars']; eq(all(cost_of_many(u, k) <= m and cost_of_many(u, nn) <= 40 for u in vs['u'] for k in vs['k'] for nn in vs['n'] for m in vs['m']), True, 'g2 variants: Mei can afford what she buys')
    vs = items['g1']['tpl']['vars']; eq(all(price_of_one(cost_of_many(a_, 2), 2) == a_ and price_of_one(cost_of_many(b_, 3), 3) == b_ for a_ in vs['a'] for b_ in vs['b']), True, 'g1 variants are whole-dollar prices')
    # ---- end-of-term check
    c = d['end_of_term_check']; C = {q['id']: q for q in c['questions']}
    eq(len(c['questions']), 8, 'check has 8 questions'); eq(c['minutes'], 20, 'check is 20 minutes'); eq(all(q['tier'] == 'start' for q in c['questions']), True, 'check is Start here level')
    line = line_places(10); siti = line.index(4) + 1; ben = line[line.index(4) + 1]
    eq((ben, len(line[:line.index(4)])), (5, 3), 'C1'); eq(C['C1']['val'], [5, 3], 'C1 val')
    ravi = 26; lily = ravi;
    for _ in range(9): lily += 1
    eq((lily, ravi + lily), (35, 61), 'C2'); eq(C['C2']['val'], [35, 61], 'C2 val')
    v = C['C3']['visual']; eq((v['a'], v['b'], v['a'] + v['b']), (9, 9, 18), 'C3 ten-frames'); eq(C['C3']['val'][0], 18, 'C3 val a')
    left = 15; pairs = 0
    while left >= 2: left -= 2; pairs += 1
    eq(('odd' if left == 1 else 'even', left), ('odd', 1), 'C3 odd: 15 leaves one over'); eq(C['C3']['val'][1], 'odd', 'C3 val b')
    eq((cost_of_many(5, 3), [x for x in range(2, 11, 2)][3]), (15, 8), 'C4'); eq(C['C4']['val'], [15, 8], 'C4 val')
    eq((price_of_one(16, 4), how_many_fit(2, 10)), (4, 5), 'C5'); eq(C['C5']['val'], [4, 5], 'C5 val')
    bags = cost_of_many(5, 4); eq((bags, left_over(bags, 3)), (20, 17), 'C6'); eq(C['C6']['val'], [20, 17], 'C6 val')
    heart = None
    for h in range(0, 30):
        if h + h == 18: heart = h
    eq((heart, 8 + 8 == 18), (9, False), 'C7 Ben is not correct'); eq(C['C7']['val'], ['No', 9], 'C7 val')
    bun = price_of_one(18, 6); eq((bun, cost_of_many(bun, 4)), (3, 12), 'C8'); eq(C['C8']['val'], [3, 12], 'C8 val')
    o = c['optional']; before = list(range(1, 8)); behind = list(range(1, 8)); total = len(before) + 1 + len(behind)       # 8th from the front: 7 before; 8th from the back: 7 behind
    eq((total, 8 + 8 == total), (15, False), 'CT 15 children and Mei is not correct'); eq(o['val'], ['No', 15], 'CT val')
    q_by_strand = {s['id']: s['questions'] for s in c['strands']}; eq(sorted(sum(q_by_strand.values(), [])), sorted(C), 'every check question is in exactly one area'); eq([len(v) for v in q_by_strand.values()], [4, 4], 'two areas of four questions')
    covered = sorted({l for s in c['strands'] for l in s['lessons']}); eq(covered, list(range(11, 21)), 'every lesson of the term is covered by the check')
    pages = sorted({q['page'] for q in c['questions']}); eq(pages, list(range(1, c['sheet_pages'] + 1)), 'questions use every sheet page')
    eq(all(sl[s]['part'] == 'exit' for s in ('s-check1', 's-check2')), True, 'check slides sit in the check part')
    tp = {p['id']: p for p in d['timing']['parts']}; eq(tp['exit']['end'] - tp['exit']['start'], 20, 'the check part is 20 minutes')
    return n
