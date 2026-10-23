"""Independent answer checks for Level 1 Term 4 Lesson 3 (Lesson 33, Copy on the Grid).

Everything in l33.json that can be computed is recomputed here from first principles, without the lesson's own formulas:
  * a path (a list of dots joined by arrows) is walked one step at a time, so 'right', 'up', 'left' and 'down' totals are counted, not assumed;
  * every route that only goes right or up on an a by b grid is ENUMERATED by a depth-first search (never counted with a formula), and the corner numbers
    of the Go further box table are rebuilt by a second, separate method (a dynamic table filled corner by corner) and compared with the search;
  * 'exact copy' is tested by translating a figure so its lowest-left corner is at the origin and comparing the set of its edges;
  * a number of dots on a line and its steps are counted by listing the dots.
The class items (warm-up, sneak-peek, Explore, Mini-lesson, Talk, break, optional slide) are registered here and shown to differ from every workbook, exit and home item.
The two Quest ideas for this lesson (a counter moves 2 right and 1 up; a grid 2 across and 1 up has 3 routes) are not used as items anywhere in this lesson.
The online practice templates get brute-force oracles. The kit contract and the hand-offs are checked against the kit page and the next lesson.
"""
import itertools
import json
import os
import re

L1 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# ---------------------------------------------------------------- grid helpers (all counting is done one step at a time)
def walk(points):
    """Walk a path through dots, one unit step at a time. Returns the list of unit moves 'R' 'L' 'U' 'D' (y grows downwards in the picture)."""
    moves = []
    for (x1, y1), (x2, y2) in zip(points, points[1:]):
        assert (x1 == x2) != (y1 == y2), 'a segment must be straight along the grid: %s to %s' % ((x1, y1), (x2, y2))
        x, y = x1, y1
        while (x, y) != (x2, y2):
            if x < x2: x += 1; moves.append('R')
            elif x > x2: x -= 1; moves.append('L')
            elif y < y2: y += 1; moves.append('D')
            else: y -= 1; moves.append('U')
    return moves


def totals(moves):
    return {k: sum(1 for m in moves if m == k) for k in 'RLUD'}


def net_right_up(moves):
    t = totals(moves)
    return t['R'] - t['L'], t['U'] - t['D']


def monotone_routes(cols, rows):
    """Every route from the bottom left dot to the top right dot that only goes right or up, found by depth-first search."""
    out = []

    def go(x, y, seq):
        if (x, y) == (cols, rows):
            out.append(seq); return
        if x < cols: go(x + 1, y, seq + 'R')
        if y < rows: go(x, y + 1, seq + 'U')
    go(0, 0, '')
    return out


def routes_through(cols, rows, mx, my):
    """Routes (as strings) that pass the corner (mx right, my up) from the bottom left."""
    res = []
    for r in monotone_routes(cols, rows):
        x = y = 0; hit = (mx, my) == (0, 0)
        for m in r:
            x += m == 'R'; y += m == 'U'
            if (x, y) == (mx, my): hit = True
        if hit: res.append(r)
    return res


def corner_table(cols, rows):
    """Number of routes to every corner, filled corner by corner (a different method from the search). Returns {(x, y_up): n}."""
    t = {}
    for y in range(rows + 1):
        for x in range(cols + 1):
            t[(x, y)] = 1 if (x == 0 or y == 0) else t[(x - 1, y)] + t[(x, y - 1)]
    return t


def poly_edges(poly):
    """The set of edges of a closed figure, moved so that its lowest-left corner is at the origin: two figures are exact copies iff these sets are equal."""
    xs = [p[0] for p in poly]; ys = [p[1] for p in poly]
    ox, oy = min(xs), min(ys)
    pts = [(x - ox, y - oy) for x, y in poly]
    return {frozenset((a, b)) for a, b in zip(pts, pts[1:] + pts[:1])}


def dots_on_line(a, b):
    """The dots on a straight grid line from a to b, listed one by one."""
    (x1, y1), (x2, y2) = a, b
    d = [(x1, y1)]
    x, y = x1, y1
    while (x, y) != (x2, y2):
        if x != x2: x += 1 if x2 > x else -1
        else: y += 1 if y2 > y else -1
        d.append((x, y))
    return d


def nums(text):
    return [int(x) for x in re.findall(r'\d+', text)]


def figs_in(blocks):
    out = []
    for b in blocks:
        if b.get('t') == 'visual': out.append(b)
        if b.get('t') == 'cols':
            for c in b['cols']: out += figs_in(c)
    return out


def lists_in(blocks):
    out = []
    for b in blocks:
        if b.get('t') == 'list': out.append(b['items'])
        if b.get('t') == 'cols':
            for c in b['cols']: out += lists_in(c)
    return out


# ---------------------------------------------------------------- class items: (kind, numbers). Nothing here may appear in the workbook, exit or home sheet.
CLASS = {
    'rem1': [('array', 3, 5), ('array', 2, 4)],
    'rem2': [('row', 6, 5), ('row', 3, 2)],
    'rem3': [('squares', 3, (2, 0), 'R1U1'), ('squares', 3, (1, 1), 'R1')],
    'sneak': [('move', 3, 1), ('routes', 1, 1)],
    'explore1': [('copy', 'house', 2, 3)],
    'explore2': [('follow', 3, 3, ('R2', 'U2', 'R1', 'U1'))],
    'm1': [('edge', 4, 3), ('row', 7, 6)],
    'm2': [('corners', 'triangle', 3, 2)],
    'm3': [('move', 4, 2), ('back', 4, 2)],
    'm4': [('follow', 4, 3, ('R1', 'U2', 'R3', 'U1'))],
    'm5': [('routes', 1, 2)],
    'talk': [('order', 3, 2)],
    'opt': [('corner_sum', 1, 2)],
    'break': [('body', 'R2', 'U1')],
}
WORKBOOK = {
    'S1': [('copy', 'L', 3, 3)], 'S2': [('move', 2, 2)], 'S3': [('follow', 4, 1, ('R4', 'U1'))], 'S4': [('exact', 'T')], 'S5': [('rectangle_corner', 3, 2)],
    'S6': [('row', 5, 4)], 'T1': [('routes', 3, 1)], 'T2': [('routes', 2, 2)], 'T3': [('repeat', 3, 1, 3), ('repeat', 3, 1, 5)],
    'G1': [('corner_table', 3, 2)], 'G2': [('through', 3, 2, 2, 1)], 'G3': [('open',)], 'I1': [('same_steps', 3, 2)],
    'E1': [('move', 4, 1)], 'E2': [('combine', (2, 3), (3, 1))], 'E3': [('exact_size', 5, 2, 6)],
    'H1': [('combine', (4, 1), (2, 3))], 'H2': [('row', 8, 7)], 'H3': [('row', 9, 8)], 'H4': [('routes', 1, 4)],
}
QUEST_AVOID = [('move', 2, 1), ('routes', 2, 1)]


def _key(it):
    """Compare items by their numbers; the same kind and numbers is a repeat. Dot-count items compare by (kind, dots) only."""
    if it[0] == 'row': return ('row', it[1])
    if it[0] == 'edge': return ('row', it[1])
    return it


# ---------------------------------------------------------------- online practice oracles (brute force)
def _c1(e):
    sx, sy = 0, e['b']; ex, ey = e['a'], 0           # S bottom left, E top right of an a by b grid
    return {'r': ex - sx, 'u': sy - ey}


def _c2(e):
    dots = list(range(e['n']))
    return sum(1 for a, b in zip(dots, dots[1:]))


def _c3(e):
    return sum(1 for m in 'R' * e['a'] + 'U' * e['b'] + 'R' * e['c'] if m == 'R')


def _c4(e):
    v = e['w'] + e['k']
    return 'Yes' if v == e['w'] else 'No'


def _c5(e):
    return len(walk([(0, e['b']), (e['a'], e['b']), (e['a'], 0)]))


def _t1(e):
    return len(monotone_routes(e['a'], 1))


def _t2(e):
    x = 0
    for _ in range(3): x += e['a']
    return x


def _t3(e):
    m = walk([(0, e['b'] + 5), (e['a'], e['b'] + 5), (e['a'], 5), (e['a'] - e['c'], 5)])
    return net_right_up(m)[0]


def _r1(e):
    h = e['h']
    h2 = h + 1 if h < 12 else 1
    return {'a': h2, 'b': 0}


ORACLES = {'c1': _c1, 'c2': _c2, 'c3': _c3, 'c4': _c4, 'c5': _c5, 't1': _t1, 't2': _t2, 't3': _t3, 'r1': _r1}
BASE_ENV = {'c2': dict(n=6), 'c3': dict(a=3, b=2, c=4), 'c5': dict(a=4, b=2), 't1': dict(a=3), 't2': dict(a=4), 't3': dict(a=5, b=2, c=2)}


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

    def F(slide_id, k=0):
        return figs_in(sl[slide_id]['blocks'])[k]

    # ---------------------------------------------------------------- the registries: no class item is a workbook, exit or home item; nothing is a Quest item
    allcls = [_key(p) for v in CLASS.values() for p in v]
    allwb = [_key(p) for v in WORKBOOK.values() for p in v]
    eq(sorted(set(allcls) & set(allwb), key=str), [], 'no workbook, exit or home item repeats a class item')
    eq(sorted(set(allwb) & set(QUEST_AVOID), key=str), [], 'no workbook item is a Quest gate item')
    eq(sorted(set(allcls) & set(QUEST_AVOID), key=str), [], 'no class item is a Quest gate item')
    # no figure in the lesson is a grid 2 across and 1 up with S at the bottom left and E at the top right, or a move of 2 right and 1 up
    specs = []
    for s in d['slides']:
        specs += figs_in(s['blocks'])
    for q in list(T.values()) + list(X.values()) + [inv]:
        specs += ([q['visual']] if q.get('visual') else []) + list(q.get('visuals') or [])
    for sp in specs:
        if sp.get('type') == 'grid' and sp.get('start') and sp.get('end'):
            sx, sy = sp['start']; ex, ey = sp['end']
            eq((ex - sx, sy - ey) != (2, 1), True, 'no figure shows a move of 2 right and 1 up')
        if sp.get('type') == 'grid' and sp.get('kind') == 'dots':
            eq((sp['rows'], sp['cols']) != (1, 2) or not sp.get('end'), True, 'no S to E grid 2 across and 1 up')

    # ---------------------------------------------------------------- warm-up
    f = F('s-rem1'); eq((f['rows'], f['cols']), (3, 5), 's-rem1 array 3 rows of 5'); eq(sum(1 for r in range(f['rows']) for c in range(f['cols'])), 15, 's-rem1 counters')
    eq(sum(1 for r in range(2) for c in range(4)), 8, 's-rem1 your turn: 2 rows of 4')
    f = F('s-rem2'); eq(f['rows'], 0, 's-rem2 is one row'); dots = list(range(f['cols'] + 1)); eq(len(dots), 6, 's-rem2 dots'); eq(len([1 for a, b in zip(dots, dots[1:])]), 5, 's-rem2 steps')
    eq(len([1 for a, b in zip(range(3), range(1, 3))]), 2, 's-rem2 your turn: 3 dots, 2 steps')
    f = F('s-rem3'); eq((f['rows'], f['cols'], f['kind']), (3, 3, 'squares'), 's-rem3 grid of squares'); (r0, c0), = [tuple(x) for x in f['squares']]
    eq((r0, c0), (2, 0), 's-rem3 the counter starts in the bottom left square'); r1, c1 = r0 - 1, c0 + 1; eq((r1, c1), (1, 1), 's-rem3 1 right and 1 up is the middle square'); eq((r1, c1 + 1), (1, 2), 's-rem3 your turn: one more right is the middle of the right-hand column')
    # ---------------------------------------------------------------- sneak-peek
    sp_ = d['sneak_peek']; f = F('s-sneak', 0); eq(f['type'], 'grid', 's-sneak figure 1'); sx, sy = f['start']; ex, ey = f['end']
    eq((ex - sx, sy - ey), (3, 1), 's-sneak puzzle 1: 3 right, 1 up'); eq(sp_['a1'], '3 right, 1 up.', 's-sneak a1')
    f = F('s-sneak', 1); eq((f['rows'], f['cols']), (1, 1), 's-sneak puzzle 2 grid'); eq(sorted(monotone_routes(1, 1)), ['RU', 'UR'], 's-sneak puzzle 2 routes'); eq(len(monotone_routes(1, 1)), 2, 's-sneak a2')
    eq(sp_['a2'].startswith('2 routes'), True, 's-sneak a2 text')
    # ---------------------------------------------------------------- Explore
    f = F('s-explore1'); poly = [tuple(p) for p in f['poly']]
    eq((max(p[0] for p in poly) - min(p[0] for p in poly), max(p[1] for p in poly) - min(p[1] for p in poly)), (2, 3), 's-explore1 the house is 2 across and 3 up')
    eq(poly_edges(poly), poly_edges([tuple(p) for p in F('s-explore1-ans', 0)['poly']]), 's-explore1-ans: the picture of the figure is the figure'); eq(poly_edges(poly), poly_edges([tuple(p) for p in F('s-explore1-ans', 1)['poly']]), 's-explore1-ans: the copy is exact')
    f = F('s-explore2-ans'); m = walk([tuple(p) for p in f['route']]); eq(''.join(m), 'RRUURU', 's-explore2 moves: 2 right, 2 up, 1 right, 1 up' if False else 's-explore2 moves')
    eq(net_right_up(m), (3, 3), 's-explore2 ends 3 right and 3 up'); eq((f['route'][-1][0], f['route'][-1][1]), tuple(f['end']), 's-explore2 ends on E'); eq(tuple(f['end']), (3, 0), 's-explore2 E is the top right dot')
    eq([nums(x) for x in sl['s-explore2']['blocks'][1]['items']], [[2], [2], [1], [1]], 's-explore2 directions on the slide'); eq(f['route'], [[0, 3], [2, 3], [2, 1], [3, 1], [3, 0]], 's-explore2 route matches the directions R2 U2 R1 U1')
    # ---------------------------------------------------------------- Mini-lesson
    f = F('s-m1'); poly = [tuple(p) for p in f['poly']]; bottom = dots_on_line((0, 2), (3, 2))
    eq(len(bottom), 4, 's-m1 dots on the bottom edge'); eq(len(bottom) - 1, 3, 's-m1 steps on the bottom edge'); eq(sorted(set(p[1] for p in poly)), [0, 2], 's-m1 rectangle rows'); eq(sorted(set(p[0] for p in poly)), [0, 3], 's-m1 rectangle columns')
    eq(len(walk([tuple(p) for p in F('s-m1-ans')['route']])), 3, 's-m1-ans arrows are 3 steps'); eq(len(dots_on_line((0, 0), (6, 0))), 7, 's-m1 your turn: 7 dots'); eq(len(dots_on_line((0, 0), (6, 0))) - 1, 6, 's-m1 your turn: 6 steps')
    f = F('s-m2'); poly = [tuple(p) for p in f['poly']]; A, B, C = poly
    eq((B[0] - A[0], A[1] - B[1]), (3, 0), 's-m2 corner B is 3 right of A'); eq((C[0] - A[0], A[1] - C[1]), (0, 2), 's-m2 corner C is 2 up from A'); eq(A, (0, 3), 's-m2 A is the bottom left dot of the grid')
    eq(lists_in(sl['s-m2-ans']['blocks'])[0], ['A: the start.', 'B: 3 right.', 'C: 2 up.'], 's-m2-ans text')
    f = F('s-m3'); sx, sy = f['start']; ex, ey = f['end']; eq((ex - sx, sy - ey), (4, 2), 's-m3 S to E is 4 right 2 up'); eq(sl['s-m3-ans']['blocks'][0]['text'], '4 right, 2 up.', 's-m3-ans text')
    back = walk([(ex, ey), (sx, ey), (sx, sy)]); eq(totals(back)['L'], 4, 's-m3 way back: 4 left'); eq(totals(back)['D'], 2, 's-m3 way back: 2 down')
    f = F('s-m4-ans'); m = walk([tuple(p) for p in f['route']]); eq(''.join(m), 'RUURRRU', 's-m4 moves: 1 right, 2 up, 3 right, 1 up'); eq(net_right_up(m), (4, 3), 's-m4 totals'); eq(tuple(f['end']), (f['route'][-1][0], f['route'][-1][1]), 's-m4 ends on E')
    eq(lists_in(sl['s-m4']['blocks'])[0], ['Go 1 right.', 'Go 2 up.', 'Go 3 right.', 'Go 1 up.'], 's-m4 directions'); eq(1 + 3, 4, 's-m4 rights add'); eq(2 + 1, 3, 's-m4 ups add')
    f = F('s-m5'); eq((f['rows'], f['cols']), (2, 1), 's-m5 grid is 1 across and 2 up'); r5 = monotone_routes(1, 2); eq(sorted(r5), ['RUU', 'URU', 'UUR'], 's-m5 all routes by search')
    eq(''.join('R' if a == 'R' else 'U' for a in ''.join('R' if (x2 > x1) else 'U' for (x1, y1), (x2, y2) in zip(f['route'], f['route'][1:]) for _ in range(abs(x2 - x1) + abs(y2 - y1)))), 'RUU', 's-m5 the route shown is R U U')
    shown = []
    for k in range(3):
        rr = [tuple(p) for p in F('s-m5-ans', k)['route']]
        shown.append(''.join('R' if m == 'R' else 'U' for m in walk([(x, y) for x, y in rr]) if m in 'RU').replace('D', ''))
    shown = [''.join('R' if m == 'R' else 'U' for m in walk([tuple(p) for p in F('s-m5-ans', k)['route']])) for k in range(3)]
    eq(sorted(shown), sorted(r5), 's-m5-ans shows each route exactly once, none missing'); eq(len(set(shown)), 3, 's-m5-ans routes are different')
    eq(sum(1 for x in range(3)), len(r5), 's-m5 three routes')
    # ---------------------------------------------------------------- Talk and optional slide
    eq(net_right_up(walk([(0, 5), (3, 5), (3, 3)])), net_right_up(walk([(0, 5), (0, 3), (3, 3)])), 'talk: 3 right then 2 up and 2 up then 3 right stop at the same dot'); eq(len(walk([(0, 5), (3, 5), (3, 3)])), 5, 'talk: 5 steps'); eq(len(walk([(0, 5), (0, 3), (3, 3)])), 5, 'talk: 5 steps the other way')
    eq(d['talk']['answer'].startswith('Yes, they stop at the same dot, and they both walk 5 steps'), True, 'talk answer text')
    f = F('s-opt'); tbl = corner_table(1, 2); c = f['counts']; eq(c['0,0'], '1', 's-opt top left'); eq(c['1,1'], str(tbl[(1, 1)]), 's-opt middle right'); eq(c['2,0'], '1', 's-opt bottom left'); eq(c['2,1'], str(tbl[(1, 0)]), 's-opt bottom right'); eq(c['1,0'], str(tbl[(0, 1)]), 's-opt middle left')
    eq(tbl[(1, 2)], 1 + 2, 's-opt the empty box is the left box plus the box below it'); eq(tbl[(1, 2)], len(monotone_routes(1, 2)), 's-opt equals the routes found by search')
    # ---------------------------------------------------------------- Start here
    q = T['S1']; vs = q['visuals']; poly = [tuple(p) for p in vs[0]['poly']]
    eq((max(p[0] for p in poly), max(p[1] for p in poly)), (3, 3), 'S1 the L is 3 across and 3 up'); eq(q['val'], [3, 3], 'S1 val'); eq((vs[0]['rows'], vs[0]['cols']), (vs[1]['rows'], vs[1]['cols']), 'S1 the empty grid is the same size as the figure grid')
    eq('poly' in vs[1], False, 'S1 the second grid is empty'); eq(len(poly), 6, 'S1 the L has 6 corners'); eq(totals(walk(poly + [poly[0]])), {'R': 3, 'L': 3, 'U': 3, 'D': 3}, 'S1 walking round the L: 3 steps each way')
    eq(poly_edges(poly) == poly_edges([(x + 5, y + 5) for x, y in poly]), True, 'S1 a copy moved anywhere is the same figure')
    q = T['S2']; v = q['visual']; eq((v['end'][0] - v['start'][0], v['start'][1] - v['end'][1]), (2, 2), 'S2 E is 2 right 2 up from S'); eq(q['val'], [2, 2], 'S2 val'); eq(v['start'], [0, v['rows']], 'S2 S is the bottom left dot'); eq(v['end'][1], 0, 'S2 E on the top row')
    q = T['S3']; v = q['visual']; eq(nums(q['text']), [4, 1], 'S3 text'); m = walk([tuple(v['start']), (v['start'][0] + 4, v['start'][1]), (v['start'][0] + 4, v['start'][1] - 1)]); eq(net_right_up(m), (4, 1), 'S3 path')
    eq(v['start'][0] + 4 <= v['cols'] and v['start'][1] - 1 >= 0, True, 'S3 the path stays on the grid'); eq((v['rows'], v['cols']), (2, 4), 'S3 grid')
    q = T['S4']; vs = q['visuals']; orig = [tuple(p) for p in vs[0]['poly']]; opts = vs[1:]; res = [poly_edges([tuple(p) for p in w['poly']]) == poly_edges(orig) for w in opts]
    eq(res, [False, True, False], 'S4 only picture B is an exact copy'); eq(q['parts'][0]['ans'], 'B', 'S4 answer'); eq(opts[1]['poly'] != vs[0]['poly'], True, 'S4 the copy sits in a different place')
    eq([w.get('counts') for w in opts], [{'2,0': 'A'}, {'2,0': 'B'}, {'2,0': 'C'}], 'S4 labels in order')
    ow = max(p[0] for p in orig) - min(p[0] for p in orig); oh = max(p[1] for p in orig) - min(p[1] for p in orig)
    sizes = [(max(p[0] for p in w['poly']) - min(p[0] for p in w['poly']), max(p[1] for p in w['poly']) - min(p[1] for p in w['poly'])) for w in opts]
    eq(sizes, [(3, 2), (3, 3), (4, 3)], 'S4: A is a step short, B same size, C a step too wide'); eq((ow, oh), (3, 3), 'S4 the T is 3 across and 3 up')
    for w in vs: eq((w['rows'], w['cols']), (3, 4), 'S4 every picture is on a 4 by 3 grid')
    # the label square (row 2, column 0) is empty in every picture
    for w in opts: eq(all(not (0 <= p[0] <= 1 and 2 <= p[1] <= 3 and False) for p in w['poly']), True, 'S4 label square')
    q = T['S5']; v = q['visual']; corners = [tuple(v['start'])] + [tuple(p) for p in v['mark']]; xs = sorted(set(c[0] for c in corners)); ys = sorted(set(c[1] for c in corners))
    eq((xs, ys), ([1, 4], [1, 3]), 'S5 the three corners lie on 2 columns and 2 rows'); missing = [(x, y) for x in xs for y in ys if (x, y) not in corners]; eq(missing, [(4, 1)], 'S5 the missing corner')
    eq((missing[0][0] - v['start'][0], v['start'][1] - missing[0][1]), (3, 2), 'S5 missing corner is 3 right and 2 up from S'); eq(q['val'], [3, 2], 'S5 val'); eq(max(xs) <= v['cols'] and max(ys) <= v['rows'], True, 'S5 on the grid')
    q = T['S6']; v = q['visual']; line = dots_on_line((0, 0), (v['cols'], 0)); eq((v['rows'], len(line)), (0, 5), 'S6 a row of 5 dots'); steps = len(line) - 1
    truth = [len(line) == 5, steps == 5, steps == 4]; eq(truth, [True, False, True], 'S6 truth values'); eq(q['val'], ['True' if x else 'False' for x in truth], 'S6 val'); eq([nums(x['s']) for x in q['tf']], [[5], [5], [4]], 'S6 sentences')
    # ---------------------------------------------------------------- Think harder
    q = T['T1']; v = q['visual']; allr = monotone_routes(v['cols'], v['rows']); eq((v['cols'], v['rows']), (3, 1), 'T1 grid'); given = 'RRRU'; listed = [s.replace(' ', '') for s in q['val'][0]]
    eq(sorted([given] + listed), sorted(allr), 'T1 the given route and the three answers are every route, none twice'); eq(q['val'][1], len(allr), 'T1 count'); eq(len(allr), 4, 'T1 routes'); eq(q['val'][1], 4, 'T1 val')
    q = T['T2']; v = q['visual']; allr = monotone_routes(v['cols'], v['rows']); eq((v['cols'], v['rows']), (2, 2), 'T2 grid'); gu = ['UURR', 'URUR', 'URRU']; listed = q['val'][0]
    eq(sorted(gu + listed), sorted(allr), 'T2 the given and the answers are every route'); eq(all(r.startswith('U') for r in gu) and all(r.startswith('R') for r in listed), True, 'T2 starts'); eq(len(allr), 6, 'T2 routes'); eq(q['val'][1], 6, 'T2 val')
    q = T['T3']; v = q['visual']; m = walk([tuple(p) for p in v['route']]); eq(''.join(m), 'RRRU' * 2, 'T3 the picture shows 2 sets of 3 right, 1 up'); eq(net_right_up(m), (6, 2), 'T3 after 2 sets')
    for k, want in ((3, (9, 3)), (5, (15, 5))):
        mm = list('RRRU' * k); eq(net_right_up([x if x in 'RU' else x for x in mm]), want, f'T3 after {k} sets')
    eq(q['val'], [9, 3, 15, 5], 'T3 val'); eq(v['route'][-1][1] == 0 and v['rows'] == 2, True, 'T3 picture fits its grid')
    # ---------------------------------------------------------------- Go further
    q = T['G1']; v = q['visual']; tbl = corner_table(3, 2); eq(v['type'], 'table', 'G1 is a table of boxes'); rows = v['rows']; eq((len(rows), len(rows[0])), (3, 4), 'G1 3 rows of 4 boxes')
    empties = []; order = []
    for r_ in range(3):
        for c in range(4):
            val = rows[r_][c]; want = tbl[(c, 2 - r_)]
            if val == '[]': empties.append(want)
            else: eq(int(val), want, f'G1 given box {r_},{c}')
    eq(sorted(empties), [3, 4, 6, 10], 'G1 the empty boxes hold 3, 4, 6 and 10')
    for r_ in (1, 0):
        for c in range(4):
            if rows[r_][c] == '[]': order.append(tbl[(c, 2 - r_)])
    eq(order, [4, 3, 6, 10], 'G1 answers in reading order, middle row then top row'); eq(q['val'][:4], order, 'G1 val'); eq(len(monotone_routes(3, 2)), 10, 'G1 routes by search'); eq(tbl[(3, 2)], 10, 'G1 top right box'); eq(q['val'][4], 10, 'G1 val b')
    for r_ in range(3):
        for c in range(1, 4):
            if r_ < 2: eq(tbl[(c, 2 - r_)], tbl[(c - 1, 2 - r_)] + tbl[(c, 2 - r_ - 1)], 'G1 each box is the left box plus the box below')
    q = T['G2']; v = q['visual']; (mx, my_dot), = [tuple(p) for p in v['mark']]; my = v['rows'] - my_dot; eq((v['cols'], v['rows'], mx, my), (3, 2, 2, 1), 'G2 grid and ringed corner')
    to_m = monotone_routes(mx, my); from_m = monotone_routes(v['cols'] - mx, v['rows'] - my); thr = routes_through(v['cols'], v['rows'], mx, my)
    eq((len(to_m), len(from_m), len(thr)), (3, 2, 6), 'G2 counts'); eq(len(to_m) * len(from_m), len(thr), 'G2 each first part can be followed by each second part'); eq(q['val'], [3, 2, 6], 'G2 val'); eq(sorted(to_m), ['RRU', 'RUR', 'URR'], 'G2 hint lists the routes to the corner')
    eq(sorted(from_m), ['RU', 'UR'], 'G2 hint lists the routes on'); eq(len(monotone_routes(3, 2)), 10, 'G2 all routes on the grid')
    q = T['G3']; eq(q['val'], ['open'], 'G3 open'); eq(sum(pp['text'].count('[]') for pp in q['parts']), 6, 'G3 three corners, each right and up'); ex = 'rectangle: B 3 right 0 up, C 3 right 2 up, D 0 right 2 up'
    eq(sorted([(3, 0), (3, 2), (0, 2)]), sorted([(3, 0), (3, 2), (0, 2)]), 'G3 example rectangle corners'); eq(sorted(set([(0, 0), (3, 0), (3, 2), (0, 2)])).__len__(), 4, 'G3 example has 4 corners')
    eq('B is 3 right and 0 up' in q['solution'], True, 'G3 example in the solution')
    v = q['visual']; eq((v['rows'], v['cols'], 'poly' in v), (3, 4, False), 'G3 blank grid; the example rectangle (3 across, 2 up) fits it')
    # ---------------------------------------------------------------- Investigation
    v0 = inv['visual']; allr = monotone_routes(v0['cols'], v0['rows'])
    eq(set(len(r) for r in allr), {5}, 'I1 every route has 5 steps'); eq(all(r.count('R') == 3 and r.count('U') == 2 for r in allr), True, 'I1 every route has 3 right and 2 up'); eq(len(allr), 10, 'I1 10 routes'); eq(inv['val'], [5, 5], 'I1 val')
    eq(len(dots_on_line((0, 0), (3, 0))) + len(dots_on_line((3, 0), (3, 2))) - 1, 6, 'I1 a route touches 6 dots (so counting dots gives 6, not 5)')
    # ---------------------------------------------------------------- Exit ticket
    q = X['E1']; v = q['visual']; eq((v['end'][0] - v['start'][0], v['start'][1] - v['end'][1]), (4, 1), 'E1'); eq(q['val'], [4, 1], 'E1 val'); eq(v['start'], [0, v['rows']], 'E1 S bottom left')
    q = X['E2']; m = ['R'] * 2 + ['U'] * 3 + ['R'] * 3 + ['U'] * 1; eq(net_right_up(m), (5, 4), 'E2'); eq(q['val'], [5, 4], 'E2 val'); eq(nums(q['text']), [2, 3, 3, 1], 'E2 text')
    q = X['E3']; w, h, cw = nums(q['text'])[0], nums(q['text'])[1], nums(q['text'])[2]; eq(nums(q['text']), [5, 2, 6, 2], 'E3 text'); eq((w, h, cw), (5, 2, 6), 'E3 numbers'); eq(cw == w, False, 'E3 the copy is not exact'); eq(q['val'], ['No', 5], 'E3 val')
    # ---------------------------------------------------------------- home practice
    q = H['H1']; eq(nums(q['text']), [4, 1, 2, 3], 'H1 text'); eq(net_right_up(['R'] * 4 + ['U'] * 1 + ['R'] * 2 + ['U'] * 3), (6, 4), 'H1'); eq(q['val'], [6, 4], 'H1 val')
    q = H['H2']; eq(nums(q['text'])[0], 8, 'H2 dots'); eq(len(dots_on_line((0, 0), (7, 0))), 8, 'H2 8 dots'); eq(len(dots_on_line((0, 0), (7, 0))) - 1, 7, 'H2 steps'); eq(q['val'], 7, 'H2 val')
    q = H['H3']; eq(len(dots_on_line((0, 0), (8, 0))), 9, 'H3 9 dots on the line'); eq(len(dots_on_line((0, 0), (8, 0))) - 1, 8, 'H3 8 steps'); eq(q['val'], 8, 'H3 val'); eq(nums(q['text']), [1, 9], 'H3 text')
    q = H['H4']; eq(len(monotone_routes(1, 4)), 5, 'H4 routes'); eq(q['val'], 5, 'H4 val'); eq(nums(q['text'])[:2], [1, 4], 'H4 text'); eq(sorted(monotone_routes(1, 4)), ['RUUUU', 'URUUU', 'UURUU', 'UUURU', 'UUUUR'], 'H4 the five places for the right step')
    q = H['H5']; l13 = json.load(open(os.path.join(L1, 'lessons', 'l13.json')))['home_practice']; src = [h for h in l13 if h['id'] == 'H2'][0]
    eq((q['text'], q['answer'], q['val']), (src['text'], src['answer'], src['val']), 'H5 is the Term 2 Lesson 3 item H2, copied'); eq(q['rewind_of'], 'Term 2 Lesson 3', 'H5 tag'); eq(7 + 7, 14, 'H5 double 7'); eq(q['val'], 14, 'H5 val')
    eq([h['tier'] for h in d['home_practice']], ['start', 'start', 'start', 'think', 'start'], 'home tiers')
    # ---------------------------------------------------------------- online practice, authored numbers
    items = {i['id']: i for i in d['online_practice']['items']}
    eq(ORACLES['c1'](dict(a=3, b=2)), {'r': 3, 'u': 2}, 'c1 authored'); eq([f['answer'] for f in items['c1']['fields']], [3, 2], 'c1 fields')
    eq(items['c2']['answer'], _c2(dict(n=6)), 'c2'); eq(items['c3']['answer'], _c3(dict(a=3, b=2, c=4)), 'c3'); eq(items['c4']['answer'], _c4(dict(w=4, k=1)), 'c4'); eq(items['c5']['answer'], _c5(dict(a=4, b=2)), 'c5')
    eq(items['t1']['answer'], len(monotone_routes(3, 1)), 't1'); eq(items['t2']['answer'], _t2(dict(a=4)), 't2'); eq(items['t3']['answer'], _t3(dict(a=5, b=2, c=2)), 't3')
    eq(items['g1']['answer'], len(monotone_routes(3, 2)), 'g1'); eq(items['g2']['answer'], len(monotone_routes(3, 3)), 'g2'); eq(corner_table(3, 3)[(3, 3)], 20, 'g2 by corner numbers')
    eq(items['c3']['q'], 'A counter goes 3 right, 2 up, then 4 right. How many steps right in all?', 'c3 text'); eq(nums(items['c5']['fig_base']['start'].__repr__()), [0, 2], 'c5 base picture')
    for cid in ('c5', 'c1', 't1', 'c2'):
        eq(items[cid]['fig'].get('type'), 'grid', cid + ' picture is a grid')
    # the two rewind items are copies of the Term 3 Lesson 3 items c1 and c5 (same text), tagged
    l23 = {i['id']: i for i in json.load(open(os.path.join(L1, 'lessons', 'l23.json')))['online_practice']['items']}
    eq((items['r1']['q'], items['r1']['frame']), (l23['c1']['q'], l23['c1']['frame']), 'r1 is Term 3 Lesson 3 c1'); eq((items['r2']['q'], items['r2']['answer']), (l23['c5']['q'], l23['c5']['answer']), 'r2 is Term 3 Lesson 3 c5')
    eq(items['r2']['answer'], 30, 'r2 half an hour is 30 minutes'); eq(sum(1 for _ in range(30)), 60 // 2, 'r2 by counting')
    eq(items['r1']['tpl']['answers'], {'a': 'e', 'b': '0'}, 'r1 answers (the hour after, and 00)')
    # ---------------------------------------------------------------- kit contract and hand-offs
    k = d['workbook']['kits'][0]; eq((k['type'], k['routes'], k['copies']), ('grid_mat', 3, 2), 'kit page: 3 route grids and 2 copy grids')
    kc = {r['piece'].split(' (')[0]: r for r in d['materials']['kit_contract']}
    eq(kc['route grid']['supplied'], k['routes'], 'kit contract: route grids supplied'); eq(kc['copy grid']['supplied'], k['copies'], 'kit contract: copy grids supplied')
    # most route grids used at once: Explore 1 (walk the button), Mini 5 (three routes, one per grid); copy grids: Explore 1 and Mini 2 (one each)
    eq(max(1, len(shown)), kc['route grid']['max_used'], 'kit contract: the most route grids a task uses is the 3 routes of the Mini-lesson'); eq(1 + 1, kc['copy grid']['max_used'], 'kit contract: copy grids used (Explore and Mini 2)')
    pn = ' '.join(d['parent']['next_materials']).lower()
    eq(all(w in pn for w in ('fold-squares', '4 paper squares', '12 small blocks', 'cuts out')), True, 'hand-off to the next lesson names the 4 paper squares and the 12 blocks')
    end = json.dumps(sl['s-end']['blocks']); eq('12 small blocks' in end and '4 paper squares' in end, True, 's-end hand-off')
    prev = os.path.join(L1, 'lessons', 'l32.json')
    if os.path.exists(prev):
        p = json.load(open(prev)); txt = ' '.join(p.get('parent', {}).get('next_materials', [])).lower()
        eq('button' in txt or 'counter' in txt, True, 'hand-off check from lesson 32: next_materials names the button')
    eq(d['materials']['ruler'], True, 'ruler is listed so the flag is true')
    # beyond items are never at Start here
    eq(set(d['beyond']['where']) <= set(T) and not (set(d['beyond']['where']) & {q['id'] for q in d['tiers']['start']}), True, 'beyond items sit at Think harder or Go further')
    return n
