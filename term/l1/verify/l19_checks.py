"""Independent answer checks for Level 1 Term 2 Lesson 19 (Find One First; the Quest moved to Lesson 20).

Prices are found by trying every whole-dollar price (0 to 40) until the groups add back to the total; costs of many are built by adding the price
again and again; money left over is counted down one dollar at a time. Nothing uses the take-the-total-and-divide shortcut the lesson teaches.
The end-of-term check answers are recomputed the same way (a line of children is a list, sums are counted, shapes are solved by trial).
"""


import json, re


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
    'c4': lambda e: 'yes' if price_of_one(cost_of_many(e['u'], 4), 4) == e['u'] + e['k'] else 'no',
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
    eq(price_of_one(16, 4), 4, 'S1'); eq(T['S1']['val'], [4], 'S1 val'); eq(T['S1']['visual']['n'], 4, 'S1 picture has 4 pens')
    eq(cost_of_many(2, 7), 14, 'S2'); eq(T['S2']['val'], [14, 14], 'S2 val'); eq(T['S2']['parts'][0]['text'], '7 × 2 = [2]', 'S2 frame'); eq(T['S2']['visual']['n'], 7, 'S2 picture has 7 pens')
    s3 = T['S3']['visual']; eq((s3['units']['n'], s3['brace']['text']), (6, '$12'), 'S3 strip'); eq(price_of_one(12, 6), 2, 'S3'); eq(T['S3']['val'], [2], 'S3 val')
    s4 = T['S4']['visual']; eq((s4['units']['n'], s4['brace']['text']), (3, '$15'), 'S4 strip'); one = price_of_one(15, 3); eq((one, cost_of_many(one, 2)), (5, 10), 'S4'); eq(T['S4']['val'], [5, 10], 'S4 val')
    eq((cost_of_many(4, 5), price_of_one(15, 5), cost_of_many(3, 5) == 15), (20, 3, True), 'S5 Lily 5 groups of 4 is 20, not 15; the price is 3'); eq(T['S5']['val'], ['No', 3], 'S5 val'); eq(T['S5']['visual']['n'], 5, 'S5 picture has 5 pens')
    eq(cost_of_many(4, 3), 12, 'S6'); eq(T['S6']['val'], [12], 'S6 val'); eq(T['S6']['visual']['n'], 3, 'S6 picture has 3 books')
    eq(sum(q['mins'] for q in d['tiers']['start']) <= 20, True, 'Start here within 20 minutes')
    eq(all(cost_of_many(p, k) <= 40 for p, k in ((4, 4), (2, 7), (2, 6), (5, 3), (4, 3))), True, 'Start here products within 40')
    # ---- Think harder
    t1 = price_of_one(12, 4); eq((t1, cost_of_many(t1, 7)), (3, 21), 'T1'); eq(T['T1']['val'], [3, 21], 'T1 val'); eq(T['T1']['visual']['units']['n'], 4, 'T1 strip')
    dozen = 12; t2 = price_of_one(24, dozen); eq((t2, cost_of_many(t2, 3)), (2, 6), 'T2'); eq(T['T2']['val'], [2, 6], 'T2 val')
    t3 = price_of_one(24, 6); eq((t3, cost_of_many(t3, 4)), (4, 16), 'T3'); eq(T['T3']['val'], [4, 16], 'T3 val')
    t4 = price_of_one(8, 4); eq((t4, how_many_fit(t4, 10)), (2, 5), 'T4'); eq(T['T4']['val'], [2, 5], 'T4 val')
    # ---- Go further
    hat, scarf = price_of_one(10, 2), price_of_one(18, 3); eq((hat, scarf, hat + cost_of_many(scarf, 2)), (5, 6, 17), 'G1'); eq(T['G1']['val'], [5, 6, 17], 'G1 val')
    pen = price_of_one(24, 8); spent = cost_of_many(pen, 5); eq((pen, spent, left_over(30, spent)), (3, 15, 15), 'G2'); eq(T['G2']['val'], [3, 15, 15], 'G2 val')
    a, b = price_of_one(12, 4), price_of_one(20, 5); eq((a, b, 'Shop A' if a < b else 'Shop B'), (3, 4, 'Shop A'), 'G3'); eq(T['G3']['val'], [3, 4, 'Shop A'], 'G3 val')
    # ---- Investigation: the two packs have the same price for one pen
    eq((price_of_one(8, 2), price_of_one(20, 5)), (4, 4), 'I1 both packs cost $4 a pen'); eq(d['tiers']['investigation']['val'], ['4', '4'], 'I1 val')
    # ---- Exit ticket and home practice
    eq(price_of_one(9, 3), 3, 'E1'); eq(X['E1']['val'], [3], 'E1 val')
    opts = [int(o.lstrip('$')) for o in X['E2']['mcq']['options']]; eq([i for i, o in enumerate(opts, 1) if o == cost_of_many(5, 3)], [2], 'E2 exactly one option'); eq(X['E2']['val'], [2], 'E2 val')
    e3 = price_of_one(10, 5); eq((e3, cost_of_many(e3, 4)), (2, 8), 'E3'); eq(X['E3']['val'], [2, 8], 'E3 val')
    eq(price_of_one(10, 5), 2, 'H1'); eq(H['H1']['val'], 2, 'H1 val'); eq(cost_of_many(3, 6), 18, 'H2'); eq(H['H2']['val'], [18, 18], 'H2 val')
    eq(cost_of_many(price_of_one(12, 4), 2), 6, 'H3'); eq(H['H3']['val'], 6, 'H3 val'); eq(cost_of_many(price_of_one(36, 12), 4), 12, 'H4'); eq(H['H4']['val'], 12, 'H4 val')
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
    eq([price_of_one(6, 2), price_of_one(12, 4), cost_of_many(3, 4)], [3, 3, 12], 'M1 the price of 1 does not change'); eq((price_of_one(12, 3), cost_of_many(5, 4), price_of_one(20, 4)), (4, 20, 5), 'M2 and M3')
    # ---- online practice: authored answers, and the variants stay whole-dollar and within 40
    eq(price_of_one(20, 4), items['c1']['answer'], 'c1 authored'); eq(cost_of_many(3, 4), items['c2']['answer'], 'c2 authored')
    c3 = price_of_one(15, 3); eq([c3, cost_of_many(c3, 2)], [f['answer'] for f in items['c3']['fields']], 'c3 authored')
    eq(items['c4']['answer'], 'yes' if price_of_one(12, 4) == 4 else 'no', 'c4 authored (Lily says 4)')
    c4v = items['c4']['tpl']['vars']; eq(sum(1 for k in c4v['k'] if k == 0) * 2, len(c4v['k']), 'c4 about half of the variants are yes'); eq(items['c5']['answer'], 12, 'c5 a dozen')
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
    # ---- no Quest in this lesson any more (it moved to Lesson 20); the lesson is an ordinary one with a live exit ticket
    assert 'challenge_quest' not in d and 'end_of_term_check' not in d, 'the Quest lives in Lesson 20 now'
    tp = {p['id']: p for p in d['timing']['parts']}; eq([(tp[k]['end'] - tp[k]['start']) for k in ('explore', 'mini', 'work', 'talk', 'exit', 'look', 'flex')], [12, 12, 30, 6, 6, 3, 5], 'ordinary 90-minute skeleton')
    eq(all(sl[s]['part'] == 'exit' and not sl[s].get('optional') for s in ('s-exit', 's-exitans')), True, 'the exit ticket is live')
    # tokens: at least as many printed as any question can use (the dollar amounts in the lesson go up to $28)
    kit = d['workbook']['kits'][0]; most = max(int(x) for x in re.findall(r'\$(\d+)', json.dumps({k_: v for k_, v in d.items() if k_ in ('tiers', 'exit', 'home_practice', 'talk', 'script', 'slides')})) if int(x) <= 30)
    eq(len(kit['labels']) >= most, True, f'{len(kit["labels"])} tokens printed, the most any item needs is ${most}'); eq(len(kit['labels']), 30, '30 tokens on the kit page')
    return n
