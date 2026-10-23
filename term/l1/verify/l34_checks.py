"""Independent answer checks for Level 1 Term 4 Lesson 4 (Lesson 34, Cubes and Views).

Everything in l34.json that can be computed is recomputed here from first principles, without the lesson's own formulas:
  * a stack is a set of cubes (row, column, level); totals are counted by listing the cubes, never by the lesson's sums;
  * 'how many cubes can you not see' is computed by PROJECTION: every cube is drawn as the same hexagon the picture uses, the cubes in front are laid over the cubes behind,
    and a cube is hidden when every point sampled on its three faces is covered by a cube in front of it;
  * a top view is read back from the cube set (the number of cubes in each stack), with the back row on top;
  * a folded paper is opened by reflection: one hole through 2 layers gives 2 holes mirrored about the fold, a second fold gives 4 holes mirrored about both folds; each
    'opened paper' option in the workbook is compared with the holes the fold really makes, so exactly one option is right;
  * the other hole on the dot grid is the mirror image across the dashed line, and its steps from the line are counted one at a time.
The class items are registered here and shown to differ from every workbook, exit and home item. The online practice templates get brute-force oracles.
"""
import itertools
import json
import os
import re

L1 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
W3, H3, SS = 0.8660254, 0.5, 1.0


# ---------------------------------------------------------------- stacks
def cubes(heights):
    """The set of cubes (row, column, level) of a stack: row 0 is the back row, column 0 the left column."""
    return {(r, c, z) for r, row in enumerate(heights) for c, h in enumerate(row) for z in range(h)}


def total(heights):
    n = 0
    for _ in cubes(heights): n += 1
    return n


def hexagon(r, c, z):
    x = (c - r) * W3; y = (c + r) * H3 - z * SS
    return [(x, y - SS), (x + W3, y - SS / 2), (x + W3, y + SS / 2), (x, y + SS), (x - W3, y + SS / 2), (x - W3, y - SS / 2)]


def faces(r, c, z):
    x = (c - r) * W3; y = (c + r) * H3 - z * SS
    return [[(x, y - SS), (x + W3, y - SS / 2), (x, y), (x - W3, y - SS / 2)],                 # top
            [(x - W3, y - SS / 2), (x, y), (x, y + SS), (x - W3, y + SS / 2)],                 # left
            [(x + W3, y - SS / 2), (x, y), (x, y + SS), (x + W3, y + SS / 2)]]                 # right


def inside(poly, p):
    """Point in a convex polygon (any vertex order of a convex shape)."""
    sign = 0
    for a, b in zip(poly, poly[1:] + poly[:1]):
        cr = (b[0] - a[0]) * (p[1] - a[1]) - (b[1] - a[1]) * (p[0] - a[0])
        if abs(cr) < 1e-9: continue
        s = 1 if cr > 0 else -1
        if sign and s != sign: return False
        sign = s
    return True


def samples(poly):
    (a, b, c, d) = poly
    pts = []
    for i in range(1, 6):
        for j in range(1, 6):
            u, v = i / 6.0, j / 6.0
            pts.append((a[0] + u * (b[0] - a[0]) + v * (d[0] - a[0]), a[1] + u * (b[1] - a[1]) + v * (d[1] - a[1])))
    return pts


def hidden_cubes(heights):
    """Cubes of which no part can be seen. A cube is in front of another when its row plus column is bigger (or it is higher in the same stack)."""
    cs = cubes(heights); hid = set()
    for cube in cs:
        r, c, z = cube
        front = [o for o in cs if o != cube and ((o[0] + o[1]) > (r + c) or ((o[0], o[1]) == (r, c) and o[2] > z))]
        seen = False
        for f in faces(*cube):
            for p in samples(f):
                if not any(inside(hexagon(*o), p) for o in front): seen = True
        if not seen: hid.add(cube)
    return hid


def top_view(heights):
    """The top view read back from the cubes: rows from back to front, the number of cubes in each stack."""
    cs = cubes(heights)
    rows = max(r for r, _, _ in cs) + 1 if cs else 0
    cols = max(c for _, c, _ in cs) + 1 if cs else 0
    return [[sum(1 for (r, c2, z) in cs if r == r0 and c2 == c0) for c0 in range(cols)] for r0 in range(rows)]


# ---------------------------------------------------------------- folds (a paper square is 0..1 across and down)
def open_v(u, v):
    """Fold in half with the fold on the left edge of the folded paper: a hole at (u, v) of the folded paper is 2 holes when opened."""
    return {(round(0.5 + 0.5 * u, 6), v), (round(0.5 - 0.5 * u, 6), v)}


def open_h(u, v):
    """Fold in half with the fold on the top edge of the folded paper: a hole at (u, v) of the folded paper is 2 holes when opened (one above the fold line, one below)."""
    return {(u, round(0.5 + 0.5 * v, 6)), (u, round(0.5 - 0.5 * v, 6))}


def open_quarter(u, v):
    """Fold twice (a vertical and a horizontal fold in the middle): the folded paper is a quarter, and a hole at (u, v) of it is 4 holes when opened."""
    xs = (round(0.5 + 0.5 * u, 6), round(0.5 - 0.5 * u, 6)); ys = (round(0.5 + 0.5 * v, 6), round(0.5 - 0.5 * v, 6))
    return {(x, y) for x in xs for y in ys}


def shown(spec):
    """The holes a workbook 'opened paper' picture draws, as the picture is specified."""
    f = spec['fold']; hs = [tuple(h) for h in spec['holes']]
    if f == 'v': return set().union(*[open_v(u, v) for u, v in hs])
    if f == 'h': return set().union(*[open_h(u, v) for u, v in hs])
    if f == 'quarter': return set().union(*[open_quarter(u, v) for u, v in hs])
    return {(round(u, 6), round(v, 6)) for u, v in hs}


def nums(text):
    return [int(x) for x in re.findall(r'\d+', text)]


def figs_in(blocks):
    out = []
    for b in blocks:
        if b.get('t') == 'visual': out.append(b)
        if b.get('t') == 'cols':
            for c in b['cols']: out += figs_in(c)
    return out


# ---------------------------------------------------------------- class items: nothing here may appear in the workbook, exit or home sheet
CLASS_STACKS = {'rem3': [[2, 1]], 'sneak1': [[2, 2]], 'sneak2': [[1, 1], [1, 2]], 'explore': [[1, 1], [2, 2]], 'm1': [[2, 2], [1, 2]], 'm2': [[1, 1], [3, 1]], 'm3': [[3, 1], [1, 1]]}
CLASS_FOLDS = {'explore': ('v', (0.55, 0.3)), 'm4': ('v', (0.7, 0.7)), 'opt': ('quarter', (0.4, 0.6))}
CLASS_MIRRORS = {'m5': (2, (0, 1))}
WB_STACKS = {'S1': [[1, 2], [1, 1]], 'S2': [[1, 0], [1, 2]], 'S3': [[1, 1], [2, 1]], 'S4': [[3, 0], [2, 1]], 'S6': [[2, 3], [1, 1]], 'T1': [[2, 3], [1, 3]], 'G2': [[3, 1], [2, 2]], 'E1': [[1, 1], [2, 0]], 'E2': [[2, 1], [2, 1]]}
WB_FOLDS = {'T2': ('h', (0.3, 0.6)), 'G1': ('quarter', (0.7, 0.6))}
WB_MIRRORS = {'T3': (2, (1, 3))}


def _tuple(h): return tuple(tuple(r) for r in h)


# ---------------------------------------------------------------- online practice oracles (brute force)
def _c1(e):
    return total([[e['a'], e['b'], e['c']]])


def _c2(e):
    return len([z for z in range(e['n']) if z < e['n'] - 1])


def _c3(e):
    a, b = e['a'], e['a'] + e['k'] - 1
    return 'the back stack' if a > b else ('the front stack' if b > a else 'the same')


def _t1(e):
    return total([[e['a'], e['b']], [e['c'], e['d']]])


def _t2(e):
    mirror = 4; hole = 4 - e['n']; other = 2 * mirror - hole
    steps = 0
    x = mirror
    while x < other: x += 1; steps += 1
    return steps


def _t3(e):
    t = e['a'] + e['b'] + e['c'] + e['d']
    for d in range(0, 10):
        if e['a'] + e['b'] + e['c'] + d == t: return d


def _r1(e):
    n = 0
    for p in range(e['p'], 5): n += 1
    return n


ORACLES = {'c1': _c1, 'c2': _c2, 'c3': _c3, 't1': _t1, 't2': _t2, 't3': _t3, 'r1': _r1}
BASE_ENV = {'c1': dict(a=2, b=1, c=3), 'c2': dict(n=4), 't1': dict(a=2, b=1, c=3, d=1), 't2': dict(n=2), 't3': dict(a=2, b=3, c=1, d=1), 'r1': dict(p=3)}


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

    def F(slide_id, k=0, t=None):
        fs = figs_in(sl[slide_id]['blocks'])
        if t: fs = [f for f in fs if f.get('mode') == t or f.get('type') == t]
        return fs[k]

    # ---------------------------------------------------------------- the registries are disjoint
    eq(set(_tuple(v) for v in CLASS_STACKS.values()) & set(_tuple(v) for v in WB_STACKS.values()), set(), 'no class stack is a workbook, exit or home stack')
    eq(len(set(_tuple(v) for v in CLASS_STACKS.values())), len(CLASS_STACKS), 'class stacks are all different'); eq(len(set(_tuple(v) for v in WB_STACKS.values())), len(WB_STACKS), 'workbook stacks are all different')
    eq(set(CLASS_FOLDS.values()) & set(WB_FOLDS.values()), set(), 'no class fold is a workbook fold'); eq(set(CLASS_MIRRORS.values()) & set(WB_MIRRORS.values()), set(), 'no class mirror grid is a workbook one')
    # each registered class stack is the stack on its slide
    eq(F('s-rem3')['heights'], CLASS_STACKS['rem3'], 's-rem3 stack'); eq(F('s-sneak', 0)['heights'], CLASS_STACKS['sneak1'], 's-sneak puzzle 1 stack'); eq(F('s-sneak', 1)['heights'], CLASS_STACKS['sneak2'], 's-sneak puzzle 2 stack')
    eq(F('s-explore1', 0)['heights'], CLASS_STACKS['explore'], 's-explore1 stack'); eq(F('s-explore1', 1)['heights'], CLASS_STACKS['explore'], 's-explore1 top view is the same stack')
    eq(F('s-m1', 0)['heights'], CLASS_STACKS['m1'], 's-m1 stack'); eq(F('s-m2')['heights'], CLASS_STACKS['m2'], 's-m2 stack'); eq(F('s-m3')['heights'], CLASS_STACKS['m3'], 's-m3 top view')
    # ---------------------------------------------------------------- warm-up
    f = F('s-rem1'); eq((f['rows'], f['cols']), (2, 3), 's-rem1 2 rows of 3'); eq(sum(1 for r in range(f['rows']) for c in range(f['cols'])), 6, 's-rem1 counters'); eq(sum(1 for r in range(3) for c in range(2)), 6, 's-rem1 your turn 3 rows of 2')
    f = F('s-rem2'); eq(f['n'], 3, 's-rem2 3 counters'); eq(3 + 3, 6, 'double 3'); eq(5 + 5, 10, 'double 5'); eq(4 + 4, 8, 'double 4')
    eq(total(CLASS_STACKS['rem3']), 3, 's-rem3 cubes'); eq(total([[2, 2]]), 4, 's-rem3 your turn: one more cube on the small tower')
    # ---------------------------------------------------------------- sneak-peek
    sp = d['sneak_peek']; eq(total(CLASS_STACKS['sneak1']), 4, 'sneak 1'); eq(hidden_cubes(CLASS_STACKS['sneak1']), set(), 'sneak 1 has no hidden cube'); eq(sp['a1'], '4 cubes.', 'sneak a1')
    st = CLASS_STACKS['sneak2']; eq(total(st), 5, 'sneak 2 has 5 cubes'); eq(len(hidden_cubes(st)), 1, 'sneak 2: 1 cube hidden'); eq(total(st) - len(hidden_cubes(st)), 4, 'sneak 2: the picture shows 4'); eq(hidden_cubes(st), {(0, 0, 0)}, 'sneak 2: it is the back left bottom cube')
    eq(nums(sp['q2']), [5, 4, 5], 'sneak q2 numbers')
    # ---------------------------------------------------------------- Explore
    st = CLASS_STACKS['explore']; eq(total(st), 6, 'explore: 6 blocks'); eq(len(hidden_cubes(st)), 1, 'explore: 1 hidden'); eq(total(st) - len(hidden_cubes(st)), 5, 'explore: 5 can be seen'); eq(top_view(st), [[1, 1], [2, 2]], 'explore top view')
    eq(open_v(*CLASS_FOLDS['explore'][1]), {(0.775, 0.3), (0.225, 0.3)}, 'explore: one dot makes 2 dots'); eq(len(open_v(*CLASS_FOLDS['explore'][1])), 2, 'explore two dots')
    f = F('s-explore2-ans'); eq(shown(f), open_v(*CLASS_FOLDS['explore'][1]), 's-explore2-ans shows the two dots'); eq([h[1] for h in f['holes']], [0.3], 's-explore2-ans')
    ds = sorted(shown(f)); eq(round(abs(ds[0][0] - 0.5), 6), round(abs(ds[1][0] - 0.5), 6), 'the two dots are the same distance from the fold')
    # ---------------------------------------------------------------- Mini-lesson
    st = CLASS_STACKS['m1']; eq(total(st), 7, 'm1: 7 cubes'); eq(len(hidden_cubes(st)), 1, 'm1: 1 hidden'); eq(total(st) - 1, 6, 'm1: 6 can be seen'); eq(top_view(st), [[2, 2], [1, 2]], 'm1 top view'); eq(2 + 2 + 1 + 2, 7, 'm1 sum')
    st = CLASS_STACKS['m2']; eq(hidden_cubes(st), set(), 'm2: nothing hidden'); eq(top_view(st), [[1, 1], [3, 1]], 'm2 top view'); eq(total(st), 6, 'm2 total'); eq(F('s-m2-ans', 1)['heights'], st, 's-m2-ans top view is the stack')
    eq(sl['s-m2-ans']['blocks'][-1]['text'], 'Top row: 1 and 1. Bottom row: 3 and 1. There are 6 cubes in all.', 's-m2-ans text')
    tv = CLASS_STACKS['m3']; eq(total(tv), 6, 'm3 total'); eq(3 + 1 + 1 + 1, 6, 'm3 sum'); eq(top_view(tv), tv, 'm3 top view round trip'); eq(hidden_cubes(tv), {(0, 0, 0)}, 'm3 the tall stack has its bottom cube hidden in the picture')
    f = F('s-m4'); eq(f['stage'], 'folded', 's-m4 folded'); eq(shown({'fold': 'v', 'holes': f['holes']}), open_v(*CLASS_FOLDS['m4'][1]), 's-m4 opened'); eq(len(open_v(*CLASS_FOLDS['m4'][1])), 2, 's-m4 two holes'); eq(F('s-m4-ans')['holes'], f['holes'], 's-m4-ans same hole')
    f = F('s-m5'); sx = f['mirror']; (mx, my), = [tuple(p) for p in f['mark']]; other = 2 * sx - mx; eq((sx, mx, my), (2, 0, 1), 's-m5 grid'); eq(other, 4, 's-m5 the other hole'); steps = 0; x = mx
    while x < sx: x += 1; steps += 1
    eq(steps, 2, 's-m5 steps from the dashed line'); eq(other - sx, 2, 's-m5 steps on the other side'); eq([tuple(p) for p in F('s-m5-ans')['mark']], [(0, 1), (4, 1)], 's-m5-ans marks both holes'); eq(f['cols'] >= other, True, 's-m5 on the grid')
    # ---------------------------------------------------------------- Talk and optional slide
    eq(d['talk']['answer'].startswith('No. A picture can hide a cube'), True, 'talk answer'); eq(nums(d['talk']['question']), [6, 6], 'talk numbers')
    f = F('s-opt'); eq(f['stage'], 'folded', 's-opt'); eq(len(open_quarter(*f['holes'][0])), 4, 's-opt: 4 holes'); eq(1 * 2 * 2, 4, 's-opt each fold doubles the layers'); eq(F('s-opt')['holes'], [list(CLASS_FOLDS['opt'][1])], 's-opt hole')
    # ---------------------------------------------------------------- Start here
    q = T['S1']; st = WB_STACKS['S1']; eq(q['visual']['heights'], st, 'S1 stack'); eq(total(st), 5, 'S1 total'); eq(hidden_cubes(st), set(), 'S1 no cube hidden, so counting the picture is right'); eq(q['val'], 5, 'S1 val')
    q = T['S2']; st = WB_STACKS['S2']; eq(q['visual']['heights'], st, 'S2 stack'); eq(nums(q['text']), [4], 'S2 text'); eq(total(st), 4, 'S2 total'); seen = total(st) - len(hidden_cubes(st)); eq((seen, len(hidden_cubes(st))), (3, 1), 'S2 3 seen, 1 hidden'); eq(q['val'], [3, 1], 'S2 val')
    q = T['S3']; st = WB_STACKS['S3']; vs = q['visuals']; eq(vs[0]['heights'], st, 'S3 stack'); eq(hidden_cubes(st), set(), 'S3 no hidden cube'); tvw = top_view(st)
    opts = [v['heights'] for v in vs[1:]]; eq([o == tvw for o in opts], [False, True, False], 'S3 only B is the top view'); eq(tvw, [[1, 1], [2, 1]], 'S3 top view: the tall stack is the front left'); eq(q['parts'][0]['ans'], 'B', 'S3 answer'); eq(q['parts'][0]['choices'], ['A', 'B', 'C'], 'S3 labels')
    eq(sorted(map(str, opts)), sorted(map(str, [[[2, 1], [1, 1]], [[1, 1], [2, 1]], [[1, 2], [1, 1]]])), 'S3 options are three different top views'); eq(len({str(o) for o in opts}), 3, 'S3 options differ')
    q = T['S4']; st = WB_STACKS['S4']; eq(q['visuals'][0]['heights'], st, 'S4 stack'); eq(hidden_cubes(st), set(), 'S4 no hidden cube'); eq(top_view(st), [[3, 0], [2, 1]], 'S4 top view'); eq(q['val'], [3, 0, 2, 1], 'S4 val'); eq(sum(1 for v in q['visuals'][1]['counts'].values() if v == '[]'), 4, 'S4 four boxes')
    q = T['S5']; eq(q['visual']['shape'], 'square', 'S5 square'); eq('across the middle' in q['answer'], True, 'S5 answer'); eq('top edge meets the bottom edge' in q['text'], True, 'S5 text')
    q = T['S6']; tv = q['visual']['heights']; eq(tv, WB_STACKS['S6'], 'S6 top view'); eq(total(tv), 7, 'S6 total'); eq(q['val'], 7, 'S6 val'); eq(sum(sum(r) for r in tv), 7, 'S6 sum')
    # ---------------------------------------------------------------- Think harder
    q = T['T1']; st = WB_STACKS['T1']; eq(q['visuals'][0]['heights'], st, 'T1 stack'); eq(total(st), 9, 'T1 total'); eq(nums(q['text']), [9], 'T1 text'); box = q['visuals'][1]['counts']
    given = [int(v) for v in box.values() if v != '[]']; eq(given, [2, 3, 1], 'T1 numbers on the top view'); missing = total(st) - sum(given); eq(missing, 3, 'T1 missing number'); eq(top_view(st)[1][1], 3, 'T1 missing number from the stack'); eq(box['1,1'], '[]', 'T1 front right is empty')
    eq((total(st) - len(hidden_cubes(st)), len(hidden_cubes(st))), (7, 2), 'T1 7 seen, 2 hidden'); eq(q['val'], [3, 2], 'T1 val'); eq(nums(q['parts'][1]['text']), [7], 'T1 part b text')
    q = T['T2']; vs = q['visuals']; f0 = vs[0]; eq((f0['stage'], f0['fold']), ('folded', 'h'), 'T2 folded picture, fold at the top'); right = open_h(*f0['holes'][0]); eq(len(right), 2, 'T2 2 holes'); res = [shown(v) == right for v in vs[1:]]
    eq(res, [True, False, False], 'T2 exactly the first opened paper (A) is right'); eq(q['val'], [2, 'A'], 'T2 val'); eq(q['parts'][1]['choices'], ['A', 'B', 'C'], 'T2 labels'); eq([v.get('tag') for v in vs[1:]], ['A', 'B', 'C'], 'T2 options are labelled'); eq(sorted(right), sorted([(0.3, 0.8), (0.3, 0.2)]), 'T2 holes'); eq(len(shown(vs[2])), 2, 'T2 option B has 2 holes on one side'); eq(len(shown(vs[3])), 1, 'T2 option C has one hole')
    eq(all(y > 0.5 for _, y in shown(vs[2])), True, 'T2 option B has both holes on one side of the fold line'); eq(f0['fold'] != CLASS_FOLDS['m4'][0], True, 'T2 fold differs from the class fold (left edge)')
    q = T['T3']; f = q['visual']; sx = f['mirror']; (mx, my), = [tuple(p) for p in f['mark']]; other = 2 * sx - mx; steps = 0; x = mx
    while x < sx: x += 1; steps += 1
    eq((sx, mx, my, other, steps), (2, 1, 3, 3, 1), 'T3 other hole and steps'); eq(q['val'], ['drawn', 1], 'T3 val'); eq(f['cols'] >= other and f['rows'] >= my, True, 'T3 on the grid')
    # ---------------------------------------------------------------- Go further
    q = T['G1']; vs = q['visuals']; f0 = vs[0]; eq((f0['stage'], f0['fold']), ('folded', 'quarter'), 'G1 folded twice'); right = open_quarter(*f0['holes'][0]); eq(len(right), 4, 'G1 4 holes'); res = [shown(v) == right for v in vs[1:]]
    eq(res, [False, False, True], 'G1 exactly the third opened paper is right'); eq(q['val'], [4, 'C'], 'G1 val'); eq([v.get('tag') for v in vs[1:]], ['A', 'B', 'C'], 'G1 options are labelled'); eq(len(shown(vs[1])), 2, 'G1 option 1 has 2 holes'); eq(len(shown(vs[2])), 4, 'G1 option 2 has 4 holes in a row'); eq(len({y for _, y in shown(vs[2])}), 1, 'G1 option 2 holes are all in one row, which two folds cannot make')
    layers = 1
    for _ in range(2): layers *= 2
    eq(layers, 4, 'G1 two folds make 4 layers'); eq(f0['holes'] != [list(CLASS_FOLDS['opt'][1])], True, 'G1 hole differs from the optional slide')
    q = T['G2']; st = WB_STACKS['G2']; eq(q['visual']['heights'], st, 'G2 stack'); eq(total(st), 8, 'G2 total'); eq(nums(q['text']), [2, 2, 3, 1, 2, 8], 'G2 text'); eq(8 - (3 + 1 + 2), 2, 'G2 front right'); eq(st[1][1], 2, 'G2 front right from the stack')
    eq((total(st) - len(hidden_cubes(st)), len(hidden_cubes(st))), (7, 1), 'G2 7 seen, 1 hidden'); eq(q['val'], [2, 1], 'G2 val')
    q = T['G3']; eq(q['val'], ['open', 7], 'G3 val'); eq(sum(1 for v in q['visual']['counts'].values() if v == '[]'), 4, 'G3 four boxes'); ex = [3, 2, 1, 1]; eq(sum(ex), 7, 'G3 example'); eq(all(1 <= v <= 3 for v in ex), True, 'G3 example heights')
    ways = [c for c in itertools.product(range(1, 4), repeat=4) if sum(c) == 7]; eq(len(ways) > 0 and (3, 2, 1, 1) in ways and (2, 2, 2, 1) in ways, True, 'G3 many answers are right'); eq(len(ways), 16, 'G3 has 16 top views with 7 cubes')
    # ---------------------------------------------------------------- Investigation
    eq(inv['val'], [2], 'I1 val'); eq(len(open_v(0.6, 0.4)), 2, 'I1 one dot makes two'); eq(round(abs(0.5 + 0.5 * 0.6 - 0.5), 6), round(abs(0.5 - 0.5 * 0.6 - 0.5), 6), 'I1 same distance from the fold')
    # ---------------------------------------------------------------- Exit ticket
    q = X['E1']; st = WB_STACKS['E1']; eq(q['visual']['heights'], st, 'E1 stack'); eq(total(st), 4, 'E1 total'); eq(hidden_cubes(st), set(), 'E1 nothing hidden'); eq(q['val'], 4, 'E1 val')
    q = X['E2']; tv = q['visual']['heights']; eq(tv, WB_STACKS['E2'], 'E2 top view'); eq(total(tv), 6, 'E2 total'); eq(q['val'], 6, 'E2 val')
    q = X['E3']; eq('left edge meets the right edge' in q['text'], True, 'E3 text'); eq('down the middle' in q['answer'], True, 'E3 answer')
    # ---------------------------------------------------------------- home practice
    q = H['H1']; eq(nums(q['text'])[:4], [2, 1, 3, 2], 'H1 text'); eq(total([[2, 1], [3, 2]]), 8, 'H1'); eq(q['val'], 8, 'H1 val')
    q = H['H2']; eq(nums(q['text'])[0], 3, 'H2 text'); eq(len([z for z in range(3) if z < 2]), 2, 'H2'); eq(q['val'], 2, 'H2 val')
    q = H['H3']; eq(nums(q['text'])[:2], [12, 7], 'H3 text'); k = 0; x = 7
    while x < 12: x += 1; k += 1
    eq(k, 5, 'H3 counting up'); eq(q['val'], 5, 'H3 val')
    q = H['H4']; eq(nums(q['text']), [2, 3], 'H4 text'); eq(q['val'], 3, 'H4 val'); eq(2 * 4 - (4 - 3), 7, 'H4 holes mirror about the fold at 4: one is 3 left, the other 3 right')
    q = H['H5']; l14 = json.load(open(os.path.join(L1, 'lessons', 'l14.json')))['home_practice']; src = [h for h in l14 if h['id'] == 'H2'][0]; eq((q['text'], q['answer'], q['val']), (src['text'], src['answer'], src['val']), 'H5 is the Term 2 Lesson 4 item H2, copied')
    eq(q['rewind_of'], 'Term 2 Lesson 4', 'H5 tag'); eq(13 - 12, 1, 'H5 13 counters in pairs leave 1'); eq([h['tier'] for h in d['home_practice']], ['start', 'start', 'start', 'think', 'start'], 'home tiers')
    # ---------------------------------------------------------------- online practice, authored numbers
    items = {i['id']: i for i in d['online_practice']['items']}
    eq(items['c1']['answer'], _c1(dict(a=2, b=1, c=3)), 'c1'); eq(items['c2']['answer'], _c2(dict(n=4)), 'c2'); eq(items['c3']['answer'], _c3(dict(a=2, k=2)), 'c3'); eq(nums(items['c3']['q']), [2, 2, 3], 'c3 text')
    eq(items['c4']['answer'], 'down the middle', 'c4'); st = items['c5']['fig']['heights']; eq((total(st), len(hidden_cubes(st)), total(st) - len(hidden_cubes(st))), (5, 1, 4), 'c5 stack has 5 cubes, 4 seen, 1 hidden'); eq(items['c5']['answer'], 1, 'c5')
    eq(items['t1']['answer'], _t1(dict(a=2, b=1, c=3, d=1)), 't1'); eq(items['t2']['answer'], _t2(dict(n=2)), 't2'); eq(items['t3']['answer'], 1, 't3'); eq(2 + 3 + 1 + _t3(dict(a=2, b=3, c=1, d=1)), 7, 't3 sums to 7')
    eq(items['g1']['answer'], len(open_quarter(0.7, 0.6)), 'g1'); st = items['g2']['fig']['heights']; eq(items['g2']['answer'], total(st), 'g2'); eq((total(st), len(hidden_cubes(st))), (8, 1), 'g2 stack')
    eq(items['c3']['options'], ['the back stack', 'the same', 'the front stack'], 'c3 options order matches answer_index k: back, same, front')
    l24 = {i['id']: i for i in json.load(open(os.path.join(L1, 'lessons', 'l24.json')))['online_practice']['items']}
    eq((items['r1']['q'], items['r1']['answer']), (l24['c3']['q'], l24['c3']['answer']), 'r1 is Term 3 Lesson 4 c3'); eq((items['r2']['q'], items['r2']['answer']), (l24['c5']['q'], l24['c5']['answer']), 'r2 is Term 3 Lesson 4 c5'); eq(_r1(dict(p=3)), 2, 'r1 change by counting up')
    # ---------------------------------------------------------------- kit contract and hand-offs
    k = d['workbook']['kits'][0]; eq((k['type'], len(k['labels']), k['w'], k['h']), ('cards', 4, 330, 330), 'kit page: 4 big squares'); kc = {r['piece'].split(' (')[0]: r for r in d['materials']['kit_contract']}
    eq(kc['paper squares']['supplied'], len(k['labels']), 'kit contract: squares supplied'); uses = [1, 1, 1]; eq(sum(uses), kc['paper squares']['max_used'], 'kit contract: Explore 1, Investigation 1, the optional fold twice 1'); eq(kc['small blocks']['max_used'] >= max(total(v) for v in (CLASS_STACKS['explore'], CLASS_STACKS['m3'])), True, 'kit contract: blocks')
    eq(kc['small blocks']['supplied'], 12, 'kit contract: 12 blocks; the biggest class stack is 6 and no task builds more than 8'); eq(max(total(v) for v in CLASS_STACKS.values()) <= 12, True, 'every class stack fits in 12 blocks')
    pn = ' '.join(d['parent']['next_materials']).lower(); eq(all(w in pn for w in ('pair-cards', '12 cards', 'cuts out')), True, 'hand-off to the next lesson names the 12 pair cards'); end = json.dumps(sl['s-end']['blocks']); eq('12 pair cards' in end, True, 's-end hand-off')
    eq(d['materials']['ruler'], False, 'no ruler needed')
    prev = os.path.join(L1, 'lessons', 'l33.json'); p = json.load(open(prev)); txt = ' '.join(p['parent']['next_materials']).lower(); eq('4 paper squares' in txt and '12 small blocks' in txt, True, 'the hand-off from lesson 33 names the 4 squares and the 12 blocks')
    eq(set(d['beyond']['where']) <= set(T) and not (set(d['beyond']['where']) & {q['id'] for q in d['tiers']['start']}), True, 'beyond items sit at Think harder or Go further')
    return n
