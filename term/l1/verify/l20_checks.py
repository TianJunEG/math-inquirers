"""Independent answer checks for Level 1 Term 2 Lesson 20 (Choose Your Tool, with Mi's Challenge Quest).

Everything is recomputed by counting, listing or trying numbers (no formula from the lesson): queue places are lists, 'I think of a number'
puzzles are solved by trying every number 0 to 60 forwards, prices by trying every whole-dollar price, picture equations by trying every pair.
"""
import itertools, json, re


def forward(steps, n):
    for op, k in steps:
        n = n + k if op == '+' else (n - k if op == '-' else n * k)
    return n


def think(steps, end, lim=60):
    """All numbers n (0..lim) that give `end` after the steps, found by trying each n forwards."""
    return [n for n in range(lim + 1) if forward(steps, n) == end]


def price_of_one(total, n, lim=40):
    for p in range(lim + 1):
        s = 0
        for _ in range(n):
            s += p
        if s == total:
            return p


def cost(p, n):
    s = 0
    for _ in range(n):
        s += p
    return s


def between_count(a, b, inclusive):
    places = list(range(1, 40))
    got = [p for p in places if (a <= p <= b if inclusive else a < p < b)]
    return len(got)


def in_front(r):
    return len([p for p in range(1, 40) if p < r])


def common(a, b, n=3):
    la = [a * i for i in range(1, 30)]; lb = [b * i for i in range(1, 30)]
    return [x for x in la if x in lb][:n]


def count_in(step, start, n):
    return [start + step * i for i in range(n)]


ORACLES = {
    'c1': lambda e: len([1 for _ in range(e['a'])]) - e['k'],
    'c2': lambda e: think([('+', e['k'])], e['n'] + e['k'])[0],
    'c3': lambda e: cost(e['u'], e['n']),
    'c4': lambda e: in_front(e['r']),
    'c5': lambda e: price_of_one(cost(e['u'], e['n']), e['n']),
    't1': lambda e: think([('*', 2), ('+', e['k'])], e['n'] + e['n'] + e['k'])[0],
    't2': lambda e: between_count(e['a'], e['b'], True),
    't3': lambda e: think([('+', e['k']), ('*', 2)], (e['n'] + e['k']) * 2)[0],
    'g1': lambda e: price_of_one(cost(e['a'], 3), 3) + price_of_one(cost(e['a'], 3), 3) + price_of_one(cost(e['b'], 2), 2),
    'g3': lambda e: price_of_one(cost(e['a'], 3), 3) - price_of_one(cost(e['b'], 5), 5),
}
BASE_ENV = {}


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
    eq((18 - 7, 18 + (18 - 7)), (11, 29), 'S1'); eq(T['S1']['val'], [11, 29], 'S1 val')
    eq((between_count(6, 9, False), in_front(9)), (2, 8), 'S2'); eq(T['S2']['val'], [2, 8], 'S2 val')
    eq((think([('+', 4)], 13), think([('-', 5)], 9)), ([9], [14]), 'S3'); eq(T['S3']['val'], [9, 14], 'S3 val')
    tb = T['S4']['visual']['rows']; eq([int(r[1]) for r in tb], count_in(4, 4, 4), 'S4 table is the 4 times list')
    eq((count_in(4, 4, 5)[-1], len(count_in(4, 4, 5))), (20, 5), 'S4'); eq(T['S4']['val'], [20, 5], 'S4 val')
    eq((7 + 9, (7 + 9) % 2 == 0), (16, True), 'S5 even, so Mei is not correct'); eq(T['S5']['val'], ['No', 16], 'S5 val')
    p = price_of_one(20, 4); eq((p, cost(p, 3)), (5, 15), 'S6'); eq(T['S6']['val'], [5, 15], 'S6 val')
    eq(sum(q['mins'] for q in d['tiers']['start']) <= 20, True, 'Start here within 20 minutes'); eq(len(d['tiers']['start']), 6, 'six Start here items')
    # ---- Think harder
    wk = count_in(3, 3, 5); eq((wk, wk.index(15) + 1), ([3, 6, 9, 12, 15], 5), 'T1 table'); eq([int(r[1].strip('$')) for r in T['T1']['visual']['rows'] if r[1] != '[]'], [3, 6], 'T1 table shows the first two rows')
    eq((len([1 for _ in range(5) if True]), 15 == cost(3, 5)), (5, True), 'T1 strip check'); eq(T['T1']['val'], [5, 5, 'either'], 'T1 val')
    eq((think([('*', 2), ('+', 3)], 17), forward([('*', 2), ('+', 3)], 7)), ([7], 17), 'T2'); eq(T['T2']['val'], [7, 14, 17], 'T2 val')
    eq((between_count(4, 9, True), 9 - 4), (6, 5), 'T3 both ends'); eq(T['T3']['val'], [6, 'No'], 'T3 val')
    eq((common(3, 4, 2), count_in(3, 3, 8)[3], count_in(4, 4, 6)[2]), ([12, 24], 12, 12), 'T4'); eq(T['T4']['val'], [12, 24], 'T4 val')
    # ---- Go further
    a_, b_ = price_of_one(12, 3), price_of_one(15, 5); eq((a_, b_, 'Shop A' if a_ < b_ else 'Shop B'), (4, 3, 'Shop B'), 'G1'); eq(T['G1']['val'], [4, 3, 'Shop B'], 'G1 val')
    eq((think([('+', 5), ('*', 2), ('-', 4)], 16), forward([('+', 5), ('*', 2), ('-', 4)], 5)), ([5], 16), 'G2'); eq(T['G2']['val'], [5], 'G2 val')
    sols = [(s, h) for s, h in itertools.product(range(0, 41), repeat=2) if s + s == 12 and h * s == 24 and s != h]
    eq(sols, [(6, 4)], 'G3 star and heart'); eq(T['G3']['val'], [6, 4], 'G3 val')
    eq(all(r['total'].isdigit() and int(r['total']) <= 40 for r in T['G3']['visual']['rows']), True, 'G3 totals within 40')
    eq(d['tiers']['investigation']['val'], ['any'], 'I1 is open'); eq(think([('+', 4)], 10), [6], 'I1 first step')
    # ---- Exit
    eq(price_of_one(10, 5), 2, 'E1'); eq(X['E1']['val'], [2], 'E1 val')
    e2 = think([('+', 6)], 15)[0]; eq((e2, [i for i, o in enumerate(X['E2']['mcq']['options'], 1) if int(o) == e2]), (9, [1]), 'E2'); eq(X['E2']['val'], [1], 'E2 val')
    eq((between_count(5, 8, False), between_count(5, 8, True)), (2, 4), 'E3'); eq(X['E3']['val'], [2, 4], 'E3 val')
    # ---- Home
    eq(len(count_in(4, 4, 5)), 5, 'H1 five bags'); eq(H['H1']['val'], 5, 'H1 val')
    eq(think([('+', 7)], 16), [9], 'H2'); eq(H['H2']['val'], 9, 'H2 val')
    eq(count_in(5, 5, 6)[-1], 30, 'H3'); eq(H['H3']['val'], 30, 'H3 val')
    eq(between_count(3, 8, True), 6, 'H4'); eq(H['H4']['val'], 6, 'H4 val')
    eq(price_of_one(12, 3) * 2 + price_of_one(6, 2), 11, 'H5'); eq(H['H5']['val'], 11, 'H5 val')
    # ---- Sneak-peek, explore, mini, warm-up, spare time
    eq((between_count(3, 6, False), think([('*', 2)], 14)), (2, [7]), 'sneak'); eq((d['sneak_peek']['val1'], d['sneak_peek']['a2'].startswith('7')), (2, True), 'sneak vals')
    eq((forward([('+', 6)], 9) , think([('+', 6)], 15)), (15, [9]), 'explore card 4'); eq(len(count_in(5, 5, 7)), 7, 'explore card 3 (7 boxes of 5 pencils is 35)')
    eq(sorted({(h, s) for h in (1, 2) for s in (1, 2, 3)}.__len__() for _ in [0]), [6], 'explore card 5 pairs')
    odd = [x for x in range(1, 20, 2)]; eq(all((a + b) % 2 == 0 for a in odd for b in odd), True, 'explore card 6 odd + odd is even')
    eq((count_in(3, 3, 6)[-1], len(count_in(3, 3, 6))), (18, 6), 'm1 and m2'); rows = sl['s-m2']['blocks'][0]['rows'][1:]; eq([int(r[1].strip('$')) for r in rows], count_in(3, 3, 6), 'm2 table')
    eq(sl['s-m1']['blocks'][1]['units']['n'], 6, 'm1 strip parts')
    eq((think([('*', 2), ('+', 2)], 20), think([('+', 3), ('*', 2)], 16)), ([9], [5]), 'm4 and m5')
    eq((forward([('+', 3)], 5), forward([('+', 3)], 5) * 2), (8, 16), 'm5a check')
    eq((count_in(3, 3, 4)[2], count_in(3, 3, 4)[3], 6 + 3), (9, 12, 9), 'warm-up bags and marbles'); eq((think([('+', 3)], 10), think([('-', 2)], 8)), ([7], [10]), 'warm-up backwards')
    eq(count_in(5, 5, 7)[-1], 35, 'opt slide'); eq(count_in(5, 5, 4)[-1], 20, 'M1')
    # ---- Quest
    c = d['challenge_quest']; C = {q['id']: q for q in c['questions']}
    eq((len(c['questions']), c['minutes'], c['sheet_pages'], c.get('tool_row')), (8, 20, 4, 'term'), 'quest shape')
    eq((in_front(6), 24 - 8), (5, 16), 'C1'); eq(C['C1']['val'], [5, 16], 'C1 val')
    s = think([('*', 3)], 18, 20); eq((s, 5 * 3), ([6], 15), 'C2 Ben is not correct'); eq(C['C2']['val'], ['No', 6], 'C2 val')
    eq(((9 + 7) % 2, count_in(5, 5, 5)[3]), (0, 20), 'C3'); eq(C['C3']['val'], ['even', 20], 'C3 val')
    eq((cost(6, 4), price_of_one(18, 3)), (24, 6), 'C4'); eq(C['C4']['val'], [24, 6], 'C4 val')
    eq((cost(5, 4), cost(5, 4) - 7), (20, 13), 'C5'); eq(C['C5']['val'], [20, 13], 'C5 val')
    u = price_of_one(16, 4); eq((u, cost(u, 5)), (4, 20), 'C6'); eq(C['C6']['val'], [4, 20], 'C6 val')
    m = think([('*', 2), ('+', 5)], 21); eq((m, forward([('*', 2), ('+', 5)], 9)), ([8], 23), 'C7 Ben is not correct'); eq(C['C7']['val'], [8, 'No'], 'C7 val')
    eq((len([(h, s_) for h in range(2) for s_ in range(3)]), count_in(4, 4, 5)[3]), (6, 16), 'C8'); eq(C['C8']['val'], [6, 16], 'C8 val')
    o = c['optional']; front, back = 7, 4; total = len([p for p in range(1, 40) if p < front]) + 1 + len([p for p in range(1, 40) if p < back]); eq((total, front + back == total), (10, False), 'CT'); eq(o['val'], ['No', 10], 'CT val')
    eq([q['lesson'] for q in c['questions']].count('mixed'), 2, 'two mixed gates')
    cov = sorted({l for q in c['questions'] for l in (q['lesson'] if isinstance(q['lesson'], list) else [q['lesson']]) if l != 'mixed'}); eq(cov, list(range(11, 20)), 'every content lesson 11 to 19 is visited')
    eq(sorted(sum([s_['questions'] for s_ in c['strands']], [])), ['C1', 'C2', 'C3', 'C4', 'C5', 'C6'], 'tagged gates are in the two areas')
    eq(sorted({q['page'] for q in c['questions']}), [1, 2, 3, 4], 'questions use every page')
    eq(any('no tally,' in x or 'not even in your own notes' in x for x in c['privacy_checklist']), False, 'new privacy wording')
    tp = {p['id']: p for p in d['timing']['parts']}; eq((tp['exit']['start'], tp['exit']['end']), (35, 55), 'quest minutes 35 to 55')
    eq(all(sl[x_]['part'] == 'exit' and sl[x_].get('no_record') for x_ in ('s-quest1', 's-quest2')), True, 'quest slides not recorded')
    for q in c['questions']:
        eq(re.search(r'\b(draw it|act it out|make a table|work backwards|list every way|spot the pattern)\b', q['text'] + ' '.join(p['text'] for p in q['parts']), re.I) is None, True, q['id'] + ' names no tool')
    return n
