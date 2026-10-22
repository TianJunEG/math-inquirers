"""Independent answer checks for Level 1 Term 2 Lesson 19 (Picture Equations).

Every picture equation in l19.json is solved here by trying EVERY assignment of whole numbers (0 to 40) to the unknown shapes and keeping
the assignments that make every line true; nothing is solved by the take-one-line-away method the lesson teaches. A puzzle passes only if
exactly one assignment fits and all different shapes get different numbers (rule 3 of the lesson). The practice templates get brute-force
oracles that build the picture from the hidden numbers, then solve it from the totals alone.
"""
import itertools

LIM = 40


def line_value(items, op, env):
    vals = []
    for sym, n in items:
        vals += [env[sym]] * n
    if op == '+':
        return sum(vals)
    if op == '×':
        p = 1
        for v in vals:
            p *= v
        return p
    if op in ('−', '-'):
        assert len(vals) == 2
        return vals[0] - vals[1]
    raise AssertionError('operator ' + op)


def rows_of(fig):
    """picture_equation spec -> [(items, op, total)], and the legend {sym: value or None for an answer box}."""
    rows = [([(it['sym'], it.get('n', 1)) for it in r['items']], r.get('op', '+'), int(r['total'])) for r in fig['rows']]
    given = {}
    for k, v in (fig.get('values') or {}).items():
        if str(v) not in ('[]', ''):
            given[k] = int(v)
    return rows, given


def solve(rows, given=None, lim=LIM, extra=None):
    """All assignments (0..lim) to the shapes that are not given such that every line is true."""
    given = given or {}
    shapes = sorted({s for items, _, _ in rows for s, _ in items} | set(given))
    free = [s for s in shapes if s not in given]
    out = []
    for combo in itertools.product(range(lim + 1), repeat=len(free)):
        env = dict(zip(free, combo)); env.update(given)
        if all(line_value(it, op, env) == t for it, op, t in rows) and (extra is None or extra(env)):
            out.append(env)
    return out


def unique(rows, given=None, extra=None):
    sols = solve(rows, given, extra=extra)
    assert len(sols) == 1, f'{len(sols)} solutions for {rows} {given}: {sols[:3]}'
    env = sols[0]
    assert len(set(env.values())) == len(env), f'different shapes must be different numbers: {env}'
    return env


def solve_fig(fig, extra=None):
    rows, given = rows_of(fig)
    return unique(rows, given, extra)


def build_rows(spec, env):
    """spec [(op, [(sym, n)])] -> rows with totals computed from the hidden numbers env (as if counters were counted)."""
    return [(items, op, line_value(items, op, env)) for op, items in spec]


# ---------------------------------------------------------------------------------------------------------- practice oracles
def _hidden(spec, env, given_syms):
    rows = build_rows(spec, env)
    return unique(rows, {s: env[s] for s in given_syms})


ORACLES = {
    'c1': lambda e: _hidden([('+', [('circle', 1), ('square', 1)])], {'circle': e['y'], 'square': e['x']}, ['square'])['circle'],
    'c2': lambda e: _hidden([('+', [('heart', 2)])], {'heart': e['a']}, [])['heart'],
    'c3': lambda e: _hidden([('+', [('star', 3)])], {'star': e['a']}, [])['star'],
    'c4': lambda e: 'yes' if e['a'] + e['k'] == _hidden([('+', [('square', 2)])], {'square': e['a']}, [])['square'] else 'no',
    'c5': lambda e: (lambda s: {'s': 2 * s['circle'], 'b': s['circle']})(_hidden([('+', [('circle', 2), ('square', 1)])], {'circle': e['b'], 'square': e['x']}, ['square'])),
    'c6': lambda e: [b for b in range(0, 41) if b + b + e['y'] == e['b'] + e['b'] + e['y']][0],
    't1': lambda e: (lambda s: {'a': s['circle'], 'b': s['triangle']})(_hidden([('+', [('circle', 2), ('triangle', 1)]), ('+', [('circle', 1), ('triangle', 1)])], {'circle': e['a'], 'triangle': e['b']}, [])),
    't2': lambda e: _hidden([('×', [('heart', 1), ('circle', 1)])], {'heart': e['h'], 'circle': e['c']}, ['circle'])['heart'],
    't3': lambda e: (lambda rows: 'yes' if all(line_value(it, op, {'circle': e['a'] + e['k'], 'triangle': e['b'] - e['k']}) == t for it, op, t in rows) else 'no')(build_rows([('+', [('circle', 1), ('triangle', 1)]), ('+', [('circle', 2), ('triangle', 1)])], {'circle': e['a'], 'triangle': e['b']})),
    'g1': lambda e: (lambda s: {'a': s['circle'], 'b': s['heart'], 'c': s['star']})(_hidden([('×', [('circle', 2)]), ('+', [('heart', 1), ('circle', 1)]), ('-', [('star', 1), ('heart', 1)])], {'circle': e['a'], 'heart': e['b'], 'star': e['b'] + e['d']}, [])),
    'g2': lambda e: _hidden([('+', [('star', 2), ('heart', 1)]), ('+', [('star', 1), ('heart', 2)])], {'star': e['a'], 'heart': e['b']}, [])['star'],
}
BASE_ENV = {'c1': {'x': 4, 'y': 6}, 'c2': {'a': 7}, 'c3': {'a': 5}, 'g2': {'a': 8, 'b': 6}}


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
    T2text = lambda T: T['T2']['text']

    def fig_of(slide_id, k=0):
        figs = []
        def walk(bl):
            for b in bl:
                if b.get('t') == 'visual' and b.get('type') == 'picture_equation': figs.append(b)
                if b.get('t') == 'cols':
                    for c in b['cols']: walk(c)
        walk(sl[slide_id]['blocks'])
        return figs[k]

    # ---- Start here
    v1 = T['S1']['visual']; loose = [i['n'] for i in v1['items'] if i['icon'] == 'counter_yellow'][0]
    eq([c for c in range(0, 12) if c + loose == 11], [8], 'S1 cup'); eq(T['S1']['val'], [8], 'S1 val'); eq(('3 counters are outside the cup.' in T['S1']['text'], loose), (True, 3), 'S1 text and picture agree on the loose counters')
    eq(solve_fig(T['S2']['visual']), {'circle': 6, 'square': 4}, 'S2'); eq(T['S2']['val'], [6], 'S2 val')
    eq(solve_fig(T['S3']['visual']), {'heart': 8}, 'S3'); eq(T['S3']['val'], [8], 'S3 val')
    eq(solve_fig(T['S4']['visual']), {'star': 5}, 'S4'); eq(T['S4']['val'], [5], 'S4 val')
    s5 = solve(rows_of(T['S5']['visual'])[0], {'square': 4}); eq(len(s5), 1, 'S5 unique'); s5 = s5[0]
    eq(s5, {'triangle': 5, 'square': 4}, 'S5'); eq([2 * s5['triangle'], s5['triangle']], T['S5']['val'], 'S5 val'); eq('The square is 4.' in T['S5']['text'], True, 'S5 square is given as 4')
    s6 = solve_fig(T['S6']['visual']); eq(s6, {'circle': 6}, 'S6'); eq((7 != s6['circle'], 2 * 7), (True, 14), 'S6 Ben is not correct (7 + 7 = 14, not 12)'); eq(T['S6']['val'], ['No', 6], 'S6 val')
    v7 = T['S7']['visual']; bags = [i['n'] for i in v7['items'] if i['icon'] == 'bag'][0]; loose = [i['n'] for i in v7['items'] if i['icon'] == 'sweet'][0]
    per_bag = [b for b in range(0, 14) if bags * b + loose == 13]
    eq(per_bag, [5], 'S7 sweets in one bag'); eq([bags * per_bag[0], per_bag[0]], T['S7']['val'], 'S7 val'); eq(('3 sweets are outside the bags.' in T['S7']['text'], loose, bags), (True, 3, 2), 'S7 text and picture agree')
    eq(sum(q['mins'] for q in d['tiers']['start']) <= 20, True, 'Start here within 20 minutes')
    # ---- Think harder
    t1 = solve_fig(T['T1']['visual']); eq(t1, {'square': 6, 'heart': 7}, 'T1'); eq(T['T1']['val'], [6, 7], 'T1 val')
    rows, _ = rows_of(T['T2']['visual']); kum = {'heart': 8, 'star': 7}
    got = ['T' if line_value(it, op, kum) == t else 'F' for it, op, t in rows]
    eq(got, ['T', 'F'], 'T2 Kumar numbers work in line 1 only'); eq(T['T2']['val'], got, 'T2 val'); eq(solve_fig(T['T2']['visual']), {'heart': 6, 'star': 9}, 'T2 right numbers'); eq('heart is 8 and the star is 7' in T2text(T), True, 'T2 text gives Kumar numbers')
    t3 = solve_fig(T['T3']['visual']); eq(t3, {'heart': 3, 'circle': 5}, 'T3'); eq(T['T3']['val'], [3, 5], 'T3 val')
    # ---- Go further
    g1 = solve_fig(T['G1']['visual']); eq(g1, {'circle': 5, 'heart': 7, 'star': 11}, 'G1'); eq(T['G1']['val'], [5, 7, 11], 'G1 val')
    g2 = solve_fig(T['G2']['visual']); eq(g2, {'star': 8, 'heart': 6}, 'G2'); eq((g2['star'] + g2['heart'], g2['star'], g2['heart']), tuple(T['G2']['val']), 'G2 val')
    eq(2 * 8 + 6 + 8 + 2 * 6, 3 * 14, 'G2 both lines together are 3 stars and 3 hearts')
    rows, _ = rows_of(T['G3']['visual'])
    free = solve(rows)                                                  # without the clue there are two answers (3 and 4, either way round)
    eq(sorted((e['heart'], e['triangle']) for e in free), [(4, 5), (5, 4)], 'G3 before the clue')
    g3 = solve_fig(T['G3']['visual'], extra=lambda e: e['heart'] > e['triangle']); eq(g3, {'heart': 5, 'triangle': 4}, 'G3'); eq(T['G3']['val'], [5, 4], 'G3 val')
    eq('The heart is greater than the triangle' in T['G3']['text'], True, 'G3 clue is in the question')
    for q in (T['G1'], T['G3']):                                          # the times sign must not sit next to the square (its cross looks like the sign)
        eq(any(('square', n) in [(i['sym'], i.get('n', 1)) for i in r['items']] for r in q['visual']['rows'] if r['op'] == '×'), False, q['id'] + ' no square in a times line')
    # ---- Investigation: one line has many answers, two lines have one
    one = [(c, t) for c in range(0, 11) for t in range(0, 11) if c + t == 10]          # 5 and 5 fits line 1 (the key accepts it)
    two = [(c, t) for (c, t) in one if c + c + t == 14]
    eq((len(one), two), (11, [(4, 6)]), 'I1'); eq(d['tiers']['investigation']['val'], ['4', '6'], 'I1 val')
    eq((5 + 5 + 5, 5 + 5 == 10), (15, True), 'I1 5 and 5 fits line 1 but not line 2')
    if d['tiers']['investigation'].get('visual'): eq(solve(rows_of(d['tiers']['investigation']['visual'])[0], extra=None) == [{'circle': 4, 'triangle': 6}], True, 'I1 picture rows have one solution')
    # ---- Exit ticket
    eq(unique([([('triangle', 2)], '+', 18)]), {'triangle': 9}, 'E1'); eq('triangle + the triangle = 18' in X['E1']['text'], True, 'E1 text gives the line'); eq(X['E1']['val'], [9], 'E1 val')
    e2 = unique([([('heart', 1), ('square', 1)], '+', 13)], {'square': 5}); eq(e2, {'heart': 8, 'square': 5}, 'E2'); opts = [int(o) for o in X['E2']['mcq']['options']]
    eq(('The square is 5.' in X['E2']['text'], 'heart + the square = 13' in X['E2']['text']), (True, True), 'E2 text gives both facts')
    eq([i for i, o in enumerate(opts, 1) if o == e2['heart']], [4], 'E2 exactly one option fits'); eq(X['E2']['val'], [4], 'E2 val')
    e3 = solve(rows_of(X['E3']['visual'])[0], {'star': 5}); eq(len(e3), 1, 'E3 unique'); e3 = e3[0]; eq(e3, {'circle': 7, 'star': 5}, 'E3'); eq(X['E3']['val'], [e3['circle']], 'E3 val')
    eq('The star is 5.' in X['E3']['text'], True, 'E3 star is given in the text')
    # ---- Home practice (words in place of pictures)
    eq(solve([([('star', 2)], '+', 8)]), [{'star': 4}], 'H1'); eq(H['H1']['val'], 4, 'H1 val')
    eq([c for c in range(0, 30) if c + 5 == 14], [9], 'H2'); eq(H['H2']['val'], 9, 'H2 val')
    eq(line_value([('heart', 3)], '+', {'heart': 4}), 12, 'H3'); eq(H['H3']['val'], 12, 'H3 val')
    h4 = unique([([('circle', 2), ('triangle', 1)], '+', 15), ([('circle', 1), ('triangle', 1)], '+', 9)]); eq(h4, {'circle': 6, 'triangle': 3}, 'H4'); eq(H['H4']['val'], 3, 'H4 val')
    h5 = unique([([('circle', 2)], '×', 16), ([('heart', 1), ('circle', 1)], '+', 9)]); eq(h5, {'circle': 4, 'heart': 5}, 'H5'); eq(H['H5']['val'], 5, 'H5 val')
    # ---- Sneak-peek, talk, spare time and the optional slide
    eq([c for c in range(0, 20) if c + 4 == 9], [5], 'sneak 1'); eq(d['sneak_peek']['val1'], 5, 'sneak 1 val')
    sn = unique([([('star', 2)], '+', 14), ([('heart', 1), ('star', 1)], '+', 10)]); eq(sn, {'star': 7, 'heart': 3}, 'sneak 2')
    eq(solve_fig(fig_of('s-sneak')), sn, 'sneak slide picture'); eq(solve_fig(fig_of('s-sneakans')), {'star': 7, 'heart': 3}, 's-sneakans picture')
    cup = unique([([('circle', 2)], '+', 12)]); eq(3 * cup['circle'], 18, 'talk: three circles'); eq(solve_fig(fig_of('s-talk')), cup, 's-talk picture')
    eq([(c, s) for c in range(0, 9) for s in range(0, 9) if c + s == 8 and c in (2, 3)], [(2, 6), (3, 5)], 's-opt line 1 alone')
    eq(solve([([('circle', 1), ('square', 1)], '+', 8), ([('circle', 2), ('square', 1)], '+', 11)]), [{'circle': 3, 'square': 5}], 's-opt both lines')
    eq((6 + 4 == 4 + 6, 10), (True, 10), 'M1 order does not matter'); eq(unique([([('circle', 1), ('star', 1)], '+', 10), ([('circle', 2), ('star', 1)], '+', 14)]), {'circle': 4, 'star': 6}, 'M2 example')
    eq([c for c in range(0, 20) if c + 4 == 9], [5], 'M3 cup')
    # ---- Explore and Mini slides
    eq(solve_fig(fig_of('s-explore1')), {'circle': 6, 'square': 4}, 'explore 1'); eq(solve_fig(fig_of('s-explore2')), {'heart': 6}, 'explore 2')
    ex3 = solve_fig(fig_of('s-explore3')); eq(ex3, {'circle': 3, 'triangle': 6}, 'explore 3'); eq(ex3 != {'circle': 7, 'triangle': 3} and ex3['circle'] not in (7,) and ex3['triangle'] not in (3,), True, 'explore 3 does not repeat the sneak-peek puzzle answers (star 7, heart 3)')
    eq(solve_fig(fig_of('s-m2')), {'circle': 6, 'square': 4}, 'm2'); m3 = solve_fig(fig_of('s-m3')); eq(m3, {'star': 5, 'triangle': 7}, 'm3')
    eq([line_value([('star', 2), ('triangle', 1)], '+', m3), line_value([('star', 1), ('triangle', 1)], '+', m3)], [17, 12], 'm3b check')
    tb = sl['s-m3b']['blocks'][0]['rows'][1:]; eq([r[1] for r in tb], ['5 + 5 + 7 = 17', '5 + 7 = 12'], 's-m3b rows')
    m4 = solve_fig(fig_of('s-m4')); eq(m4, {'heart': 4, 'circle': 3}, 'm4'); eq(4 * 3, 12, 'm4 check')
    m5 = solve_fig(fig_of('s-m5')); eq(m5, {'star': 5, 'heart': 6}, 'm5'); tb = sl['s-m5a']['blocks'][0]['rows'][1:]
    eq([(r[0], int(r[1])) for r in tb], [('Star', 5), ('Heart', 6)], 's-m5a'); eq((5 + 6, 5 + 5 + 6), (11, 16), 's-m5a checks')
    # ---- warm-up
    eq(([c for c in range(0, 11) if 6 + c == 10], [c for c in range(0, 9) if c + 3 == 8], [c for c in range(0, 10) if 5 + c == 9]), ([4], [5], [4]), 'warm-up 1')
    eq(([c for c in range(0, 10) if c + c == 8], 5 + 5, 7 + 7, 2 * 6), ([4], 10, 14, 12), 'warm-up 2')
    g = sl['s-rem3']['blocks'][0]; eq((g['n'], g['each'], g['n'] * g['each'], 3 * 4, 2 * 10), (4, 5, 20, 12, 20), 'warm-up 3')
    eq(sl['s-rem1']['blocks'][1]['filled'], 6, 'warm-up ten-frame')
    p2 = sl['s-rem2']['blocks'][0]; eq((p2['n'], p2['each'], p2['n'] * p2['each']), (2, 6, 12), 'warm-up plates total')
    # ---- online practice
    items = {i['id']: i for i in d['online_practice']['items']}
    c1 = solve_fig(items['c1']['fig_base']); eq(c1['circle'], items['c1']['answer'], 'c1 authored')
    eq(all(a != b for a in items['c1']['tpl']['vars']['x'] for b in items['c1']['tpl']['vars']['y']), True, 'c1 variants: different shapes, different numbers')
    eq(solve_fig(items['c2']['fig_base'])['heart'], items['c2']['answer'], 'c2 authored'); eq(solve_fig(items['c3']['fig_base'])['star'], items['c3']['answer'], 'c3 authored')
    eq(items['c4']['answer'], 'no' if 6 != solve_fig(items['c4']['fig_base'])['square'] else 'yes', 'c4 authored'); eq(solve_fig(items['c4']['fig_base']), {'square': 7}, 'c4 picture')
    c5 = solve_fig(items['c5']['fig_base']); eq([2 * c5['circle'], c5['circle']], [f['answer'] for f in items['c5']['fields']], 'c5 authored')
    eq(all(a != b for a in items['c5']['tpl']['vars']['b'] for b in items['c5']['tpl']['vars']['x']), True, 'c5 variants: different numbers')
    v = items['c6']['fig_base']['items']; eq([b for b in range(0, 14) if 2 * b + v[1]['n'] == 13], [items['c6']['answer']], 'c6 authored')
    t1i = solve_fig(items['t1']['fig_base']); eq([t1i['circle'], t1i['triangle']], [f['answer'] for f in items['t1']['fields']], 't1 authored')
    eq(all(a != b for a in items['t1']['tpl']['vars']['a'] for b in items['t1']['tpl']['vars']['b']), True, 't1 variants: different numbers')
    eq(solve_fig(items['t2']['fig_base'])['heart'], items['t2']['answer'], 't2 authored'); eq(all(h * c <= 40 for h in items['t2']['tpl']['vars']['h'] for c in items['t2']['tpl']['vars']['c']), True, 't2 products within 40')
    eq(all(h != c for h in items['t2']['tpl']['vars']['h'] for c in items['t2']['tpl']['vars']['c']), True, 't2 variants: different numbers')
    # t3: the authored claim (5 and 6) fits both lines; in every variant line 1 is true and line 2 is true only when the claim is the real pair
    rows, _ = rows_of(items['t3']['fig_base'])
    eq(solve_fig(items['t3']['fig_base']), {'circle': 5, 'triangle': 6}, 't3 picture'); eq(items['t3']['answer'], 'yes', 't3 authored (5 and 6)')
    tv = items['t3']['tpl']['vars']
    eq(all(a + k != b - k and a != b for a in tv['a'] for b in tv['b'] for k in tv['k']), True, 't3 variants: different numbers, claim and truth')
    eq(sum(1 for k in tv['k'] if k == 0) * 2, len(tv['k']), 't3 about half of the variants are yes')
    g1i = solve_fig(items['g1']['fig_base']); eq([g1i['circle'], g1i['heart'], g1i['star']], [f['answer'] for f in items['g1']['fields']], 'g1 authored')
    eq(solve_fig(items['g2']['fig_base'])['star'], items['g2']['answer'], 'g2 authored'); eq(all(a != b for a in items['g2']['tpl']['vars']['a'] for b in items['g2']['tpl']['vars']['b']), True, 'g2 variants: different numbers')
    eq(all(a <= LIM for a in items['g2']['tpl']['vars']['a']), True, 'g2 within 40')
    # picture totals used by the exit and workbook are within 40 (Term 2 plan: totals within 40)
    for q in list(T.values()) + list(X.values()):
        if q.get('visual', {}).get('type') == 'picture_equation':
            eq(all(r['total'].lstrip('-').isdigit() and int(r['total']) <= 40 for r in q['visual']['rows']), True, q['id'] + ' totals within 40')
    return n
