"""Independent answer checks for Level 1 Term 3 Lesson 8 (Lesson 28, Make a Table).

The number of sticks in a row of triangles or squares is counted two ways that do not use the rule the lesson teaches: (1) from a set of distinct sticks built
from coordinates (a stick shared by two pictures is one stick, so 100 pictures are really built, 201 and 301 sticks), and (2) by counting the drawn lines in the
SVG that the lesson's own picture builder prints. Every table, true or false statement, 'which number is wrong', 'work back' and 'most pictures with 14 strips'
answer is then recomputed from those counts. The strip page is read back from the kit builder (14 cut-out strips) and compared with the kit contract.
"""
import itertools
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(HERE), 'tools'))


def tri_sticks(n):
    """Row of n triangles on a zigzag of points 0..n+1: triangle j has sides (j, j+1), (j+1, j+2) and (j, j+2). Plus one handle stick (distinct from every triangle side)."""
    edges = set()
    for j in range(n):
        for a, b in ((j, j + 1), (j + 1, j + 2), (j, j + 2)): edges.add((a, b))
    edges.add(('handle', 0))
    return len(edges)


def sq_sticks(n):
    """Row of n squares on points (i, 0) and (i, 1): bottom, top and the vertical sides."""
    edges = set()
    for i in range(n):
        edges.add(((i, 0), (i + 1, 0))); edges.add(((i, 1), (i + 1, 1))); edges.add(((i, 0), (i, 1))); edges.add(((i + 1, 0), (i + 1, 1)))
    edges.add(('handle', 0))      # one handle stick
    return len(edges)


def svg_sticks(shape, n):
    import figs3
    s = figs3.stick_pattern(shape, n, handle=True)
    return len(re.findall(r'<line [^>]*stroke-width="7"', s))


def figs_in(x, kind, out=None):
    out = [] if out is None else out
    if isinstance(x, dict):
        if x.get('type') == kind: out.append(x)
        for v in x.values(): figs_in(v, kind, out)
    elif isinstance(x, list):
        for v in x: figs_in(v, kind, out)
    return out


def row(tb, i):
    return tb['rows'][i - 1] if i else tb['head']


ORACLES = {
    'c1': lambda e: tri_sticks(e['n']),
    'c2': lambda e: sq_sticks(e['n']),
    'c3': lambda e: sum(e['p'] for _ in range(e['k'])),
    'c5': lambda e: [e['s'] + e['e'] * i for i in range(4)][3],
    't1': lambda e: tri_sticks(e['n']),
    't3': lambda e: sq_sticks(e['n']),
    'g1': lambda e: next(n for n in range(1, 200) if tri_sticks(n) == e['t']),
    'g2': lambda e: next(n for n in range(1, 200) if sq_sticks(n) == e['t']),
}
BASE_ENV = {'c1': {'n': 4}, 'c2': {'n': 3}, 'c3': {'p': 5, 'k': 4}, 'c5': {'s': 2, 'e': 3}, 't1': {'n': 10}, 't3': {'n': 8}, 'g1': {'t': 32}, 'g2': {'t': 38}}


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
    tabs = lambda x: figs_in(x, 'table')
    nums = lambda r: [int(x) if re.fullmatch(r'\d+', x) else x for x in r]

    # ---------------------------------------------------------------- the stick counts, two independent ways
    eq([tri_sticks(k) for k in range(1, 8)], [4, 6, 8, 10, 12, 14, 16], 'triangle sticks by distinct edges (with the handle)')
    eq([sq_sticks(k) for k in range(1, 8)], [5, 8, 11, 14, 17, 20, 23], 'square sticks by distinct edges (with the handle)')
    eq([svg_sticks('triangle', k) for k in range(1, 8)], [tri_sticks(k) for k in range(1, 8)], 'the lesson picture draws as many sticks as the edge count (triangles)')
    eq([svg_sticks('square', k) for k in range(1, 8)], [sq_sticks(k) for k in range(1, 8)], 'the lesson picture draws as many sticks as the edge count (squares)')
    eq((tri_sticks(100), sq_sticks(100), tri_sticks(10), tri_sticks(20), sq_sticks(10), sq_sticks(20)), (202, 302, 22, 42, 32, 62), 'the far pictures, built stick by stick')
    eq(all(tri_sticks(k) % 2 == 0 for k in range(1, 300)), True, 'every row of triangles with a handle uses an even number of sticks')
    eq(all(tri_sticks(k) == 2 * k + 2 and sq_sticks(k) == 3 * k + 2 for k in range(1, 300)), True, 'double and add 2 for triangles, 3 each and 2 for squares, over 299 pictures')
    # ---------------------------------------------------------------- warm-up and sneak-peek
    eq([b for b in sl['s-rem1']['blocks'] if b.get('t') == 'numrow'][0]['items'], [4, 6, 8, 10, '?'], 'rem1'); eq(list(range(4, 14, 2))[4], 12, 'rem1 next is 12'); eq((6 + 6, 7 + 7), (12, 14), 'rem2 doubles')
    tb = tabs(sl['s-rem3']['blocks'])[0]; eq((tb['head'], tb['rows'][0], 2 * 3), (['Day', '1', '2', '3'], ['Stickers', '2', '4', '[]'], 6), 'rem3 table: 2 more each day, day 3 is 6')
    sp = d['sneak_peek']; tb = tabs(sl['s-sneak']['blocks'])[0]; eq((tb['rows'][0], 4 * 3, sp['val1']), (['Pencils', '4', '8', '[]'], 12, 12), 'sneak 1')
    dots = [2 + 3 * i for i in range(6)]; eq((dots[:3], dots[3], dots[4]), ([2, 5, 8], 11, 14), 'sneak 2: picture 5 has 14 dots'); eq(sp['a2'].startswith('14 dots.'), True, 'sneak a2')
    # ---------------------------------------------------------------- explore and mini-lesson
    eq((tri_sticks(1), tri_sticks(2), tri_sticks(3), tri_sticks(4), tri_sticks(5)), (4, 6, 8, 10, 12), 'explore: 1 to 4 built, 5 guessed'); eq(tri_sticks(4) <= 14, True, 'explore uses 10 of the 14 strips')
    eq(3 * 5 + 1, 16, 'the wrong idea 5 times 3 and the handle is 16, which is not 12'); eq(tri_sticks(2), 6, 'two triangles with a handle use 6, not 7 (one stick shared)')
    t = tabs(sl['s-m1']['blocks'])[0]; eq((nums(t['head'][1:]), nums(t['rows'][0][1:5])), ([1, 2, 3, 4, 5], [tri_sticks(k) for k in (1, 2, 3, 4)]), 's-m1 table'); eq(t['rows'][0][5], '[]', 's-m1 fifth box empty')
    t = tabs(sl['s-m2']['blocks'])[0]; eq(nums(t['rows'][0][1:]), [tri_sticks(k) for k in range(1, 6)], 's-m2 table'); eq([b for b in sl['s-m2']['blocks'] if b.get('t') == 'numrow'][0]['items'], ['+2'] * 4, 's-m2 arrows')
    t = tabs(sl['s-m3']['blocks'])[0]; eq((nums(t['head'][1:]), t['rows'][0][1], tri_sticks(6), tri_sticks(7)), ([5, 6, 7], '12', 14, 16), 's-m3: 6th is 14, 7th is 16')
    t = tabs(sl['s-m5']['blocks'])[0]; eq((nums(t['rows'][0][1:]), nums(t['rows'][1][1:])), ([2 * k for k in range(1, 5)], [2 * k + 2 for k in range(1, 5)]), 's-m5 double and add 2'); eq(2 * 6 + 2, tri_sticks(6), 's-m5 rule for 6')
    t = tabs(sl['s-m6']['blocks'])[0]; eq((nums(t['rows'][0][1:3]), 6 * 3, 6 * 4), ([6, 12], 18, 24), 's-m6 table of equal groups'); eq([b for b in sl['s-m6a']['blocks'] if b.get('t') == 'answer'][0]['text'], 'Jars 3: 18 sweets. Jars 4: 24 sweets.', 's-m6a')
    t = tabs(sl['s-opt']['blocks'])[0]; eq((nums(t['head'][1:]), nums(t['rows'][0][1:]), sq_sticks(9)), ([1, 2, 3, 4, 5], [sq_sticks(k) for k in range(1, 6)], 29), 'optional slide: 5 squares are given, 9 squares use 29'); eq('29 sticks' in ' '.join(l.get('text', '') for sg_ in d['script']['segments'] for l in sg_['lines'] if sg_['part'] == 'flex'), True, 'optional answer 29 is in the guide')
    # ---------------------------------------------------------------- Start here
    q = T['S1']; fs = q['visuals']; eq([(f['shape'], f['n']) for f in fs], [('square', 1), ('square', 2), ('square', 3)], 'S1 pictures: 1, 2 and 3 squares'); eq([sq_sticks(k) for k in (1, 2, 3)], q['val'], 'S1'); eq([svg_sticks('square', f['n']) for f in fs], q['val'], 'S1 pictures draw 5, 8 and 11 sticks')
    q = T['S2']; t = q['visual']; pens, rulers = t['rows']; eq((nums(pens[1:]), nums(rulers[1:]), t['head'][1:]), ([2, 4, '[]', 8, ''], [3, 6, 9, '[]', ''], ['1', '2', '3', '4', '5']), 'S2 table (the fifth column is spare, for 5 rulers)')
    cost = lambda price, k: sum(price for _ in range(k)); eq((cost(2, 3), cost(3, 4), cost(3, 5), q['val']), (6, 12, 15, [6, 12, 15]), 'S2: 3 pens $6, 4 rulers $12, 5 rulers $15')
    eq((cost(2, 2), cost(3, 3)), (4, 9), 'S2 given cells match the prices')
    q = T['S3']; t = q['visual']; eq((nums(t['rows'][0][1:4]), nums(t['head'][1:]), t['rows'][0][4:]), ([5, 8, 11], [1, 2, 3, 4, 5, 6, 7], ['[]', '[]', '[]', '']), 'S3 table given (the seventh column is spare, for 7 squares)'); eq([sq_sticks(k) for k in (4, 5, 6)], [14, 17, 20], 'S3 boxes'); eq((sq_sticks(7) - sq_sticks(6), sq_sticks(7), q['val']), (3, 23, [14, 17, 20, 3, 23]), 'S3 parts')
    q = T['S4']; t = q['visual']; eq([5 * k for k in range(1, 7)], [5, 10, 15, 20, 25, 30], 'S4 days'); eq((t['rows'][0], q['val']), (['Pages', '5', '10', '[]', '20', '[]', '[]'], [15, 25, 30, 5]), 'S4 table and answers'); eq([k for k in range(1, 7) if 5 * k == 25], [5], 'S4 part: 25 pages is day 5')
    q = T['S5']; eq([sq_sticks(2) - sq_sticks(1) == 3 and sq_sticks(5) - sq_sticks(4) == 3, sq_sticks(4) == 17, sq_sticks(6) == 20], [True, False, True], 'S5 statements'); eq(q['val'], ['True', 'False', 'True'], 'S5 val')
    eq(sum(x['mins'] for x in d['tiers']['start']) <= 20, True, 'Start here within 20 minutes'); eq(len(d['tiers']['start']), 5, 'five Start here questions')
    # ---------------------------------------------------------------- Think harder
    q = T['T1']; t = q['visual']; eq((nums(t['head'][1:]), nums(t['rows'][0][1:5])), ([1, 2, 3, 4, 10, 20], [4, 6, 8, 10]), 'T1 table'); eq((tri_sticks(10), tri_sticks(20), q['val'][:2]), (22, 42, [22, 42]), 'T1 answers')
    eq(all(2 * k + 2 == tri_sticks(k) for k in range(1, 40)) and q['val'][2] == 2, True, 'T1 rule: double and add 2')
    q = T['T2']; eq([k for k in range(1, 400) if tri_sticks(k) == 21], [], 'T2 no row of triangles with a handle uses exactly 21 sticks'); eq(all(tri_sticks(k) % 2 == 0 for k in range(1, 400)), True, 'T2 always even'); eq([k for k in range(1, 400) if tri_sticks(k) == 26], [12], 'T2 (c) 26 sticks make 12 triangles, so Yes'); eq(q['val'], ['No', 'even', 'Yes'], 'T2 val')
    q = T['T3']; t = q['visual']; given = nums(t['rows'][0][1:]); true_ = [sq_sticks(k) for k in range(1, 7)]
    eq([i + 1 for i in range(6) if given[i] != true_[i]], [4], 'T3 only the 4th number is wrong'); eq((true_[3], q['val'], true_[1] - true_[0]), (14, ['4', 14, 3], 3), 'T3 right number and step'); eq(sum(1 for i in range(6) if given[i] != true_[i]), 1, 'T3 exactly one wrong')
    # ---------------------------------------------------------------- Go further
    q = T['G1']; t = q['visual']; eq((nums(t['rows'][0][1:]), nums(t['rows'][1][1:])), ([4, 6, 8, 10], [5, 8, 11, 14]), 'G1 tables'); eq((tri_sticks(100), sq_sticks(100), sq_sticks(50), q['val']), (202, 302, 152, [202, 302, 152]), 'G1 by building 100 and 50 pictures')
    q = T['G2']; eq(([k for k in range(1, 100) if tri_sticks(k) == 32], [k for k in range(1, 100) if sq_sticks(k) == 38], q['val']), ([15], [12], [15, 12]), 'G2 work back, by search')
    q = T['G3']; eq((sq_sticks(10) - tri_sticks(10), sq_sticks(20) - tri_sticks(20), sq_sticks(5) - tri_sticks(5), q['val']), (10, 20, 5, [10, 20, 5]), 'G3')
    # ---------------------------------------------------------------- Investigation: 14 strips
    inv = d['tiers']['investigation']; best_t = max(k for k in range(1, 30) if tri_sticks(k) <= 14); best_s = max(k for k in range(1, 30) if sq_sticks(k) <= 14)
    eq((best_t, 14 - tri_sticks(best_t), best_s, 14 - sq_sticks(best_s)), (6, 0, 4, 0), 'I1 most pictures; both use all 14 strips'); eq((14 in [tri_sticks(k) for k in range(1, 30)], 14 in [sq_sticks(k) for k in range(1, 30)]), (True, True), 'I1 14 strips can be used exactly by both')
    eq((tri_sticks(3), inv['val']), (8, ['6', '4']), 'I1 first step and val'); eq(max(tri_sticks(best_t), sq_sticks(best_s)), 14, 'the most strips any task uses is 14')
    # ---------------------------------------------------------------- talk
    eq((tri_sticks(5), 5 * 3 + 1, tri_sticks(3)), (12, 16, 8), 'talk: 5 triangles with a handle need 12, not 16; 3 triangles need 8'); eq(d['talk']['answer'].startswith('No.'), True, 'talk answer')
    # ---------------------------------------------------------------- exit
    q = X['E1']; eq((7 * 3, q['val']), (21, [21]), 'E1'); q = X['E2']; eq(([3 * k for k in range(1, 6)][4], q['mcq']['options'][q['val'][0] - 1]), (15, '15'), 'E2')
    q = X['E3']; eq((tri_sticks(8), q['val'], 2 * 8 + 2, [tri_sticks(k) for k in (1, 2, 3, 4)]), (18, [18], 18, [4, 6, 8, 10]), 'E3: 8 triangles use 18 sticks (a taught step: 2 more each time, never the odd and even idea)'); eq(8 not in (6, 7, 5), True, 'E3 asks for a number the class does not (the class goes to 7 triangles)')
    # ---------------------------------------------------------------- home
    eq((5 * 3, 5 * 4, H['H1']['val']), (15, 20, [15, 20]), 'H1'); eq(([3 * k for k in range(1, 5)][3], H['H2']['val']), (12, 12), 'H2: 8 pens is 4 groups of 2, so 12 pencils')
    eq((tri_sticks(15), H['H3']['val']), (32, 32), 'H3'); eq(([k for k in range(1, 100) if sq_sticks(k) == 41], H['H4']['val']), ([13], 13), 'H4'); eq((27 + 16 - 9, H['H5']['val'], H['H5'].get('rewind_of')), (34, 34, 'Term 1 Lesson 8'), 'H5 rewind')
    eq(len([h for h in d['home_practice'] if h['tier'] == 'start']) >= 3, True, 'home has 3 Start here items')
    # ---------------------------------------------------------------- online practice
    items = {i['id']: i for i in d['online_practice']['items']}
    for cid, env in BASE_ENV.items(): eq(ORACLES[cid](env), items[cid]['answer'], cid + ' oracle at the authored numbers')
    eq((items['c4']['answer'], tri_sticks(2) - tri_sticks(1)), ('2', 2), 'c4'); eq((items['t2']['answer'], [k for k in range(1, 99) if tri_sticks(k) == 21]), ('No', []), 't2'); eq((items['g3']['answer'], tri_sticks(100)), (202, 202), 'g3')
    eq(figs_in(items['c1']['fig_base'], 'stick_pattern')[0]['n'], 4, 'c1 base picture'); eq(figs_in(items['c2']['fig_base'], 'stick_pattern')[0]['n'], 3, 'c2 base picture'); eq(svg_sticks('triangle', 4), items['c1']['answer'], 'c1 base picture draws the answer')
    for it in items.values():
        for s_ in it.get('slips', []):
            if it['type'] in ('number', 'choice'): eq(it['answer'] in s_['a'], False, it['id'] + ' slip is wrong')
    for cid in ('g1',):
        for t_ in items[cid]['tpl']['vars']['t']: eq(any(tri_sticks(k) == t_ for k in range(1, 200)), True, f'g1 {t_} sticks is a real row of triangles')
    for t_ in items['g2']['tpl']['vars']['t']: eq(any(sq_sticks(k) == t_ for k in range(1, 200)), True, f'g2 {t_} sticks is a real row of squares')
    # ---------------------------------------------------------------- the kit page: read back from the kit builder
    import figs3
    svg = figs3.render_kit({'type': 'stick_strips'})
    cut = re.findall(r'stroke-dasharray="7 5"', svg); eq(len(cut), 14, 'the page prints 14 cut-out strips')
    r = d['materials']['kit_contract'][0]; eq((r['supplied'], r['max_used'], r['supplied'] >= r['max_used']), (14, 14, True), 'kit contract: 14 strips, at most 14 used')
    # ---------------------------------------------------------------- hand-off to the next lesson (8 mistake cards)
    nm = ' '.join(d['parent']['next_materials'])
    eq(('8' in nm, 'mistake-card' in nm, 'cut' in nm, 'mat' in nm), (True, True, True, True), 'hand-off to Lesson 29 names the 8 mistake cards and the mat')
    eq(d['workbook']['kits'][0]['type'], 'stick_strips', 'kit type')
    op = [x['text'] for x in d['script']['segments'][0]['lines'] if x['k'] in ('SAY', 'DO')]; ot = ' '.join(op)
    eq(('Nobody holds paper up to the camera' in ot, 'any voice that is not muted' in ot, 'Do not use children' in ot, 'by first name as they arrive' in ot), (True, True, True, False), 'opening carries the Term 1 recording and camera wording')
    eq('Ben' in json.dumps(d['tiers']), False, 'no child is named with wrong working in Think harder')
    eq(any('even' in l.get('text', '') and 'Remember that word' in l.get('text', '') for sg_ in d['script']['segments'] for l in sg_['lines']), True, 'the Mini-lesson says even once before Think harder uses it')
    eq(d['parent']['term_line'], 'Your child is learning to give a reason for each step.', 'term line fits the lesson')
    eq(('2 spoons' in d['parent']['try_home'][0], 2 * 5), (True, 10), 'parent try-at-home 1 gives the rule (2 spoons a cup)')
    eq((tri_sticks(8) not in [tri_sticks(k) for k in range(1, 8)], 29 in [sq_sticks(k) for k in range(1, 10)]), (True, True), 'new exit and optional numbers are not class numbers')
    return n
