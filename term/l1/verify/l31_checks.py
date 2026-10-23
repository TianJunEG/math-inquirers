"""Independent answer checks for Level 1 Term 4 Lesson 1 (Lesson 31, Half and Quarter).

Nothing here reuses the lesson's own sentences or formulas. Shapes are turned into real geometry: a unit square or a circle is CUT by
lines (polygon clipping for the square, sector angles for the circle), and the parts are compared by AREA with exact fractions, and by SHAPE
(vertex count; tetromino outlines compared under every turn and flip). A half is recognised as a cut that leaves two parts of equal area,
a quarter as one of four. Squares in a rectangle are shared out one at a time in a loop, and the number of parts after each fold is found by
actually cutting every region in two. The fold kit is read back from the kit builder (its cut outlines are counted in the SVG).
"""
import math
import os
import re
import sys
from fractions import Fraction as F

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(HERE), 'tools'))


# ------------------------------------------------------------------ geometry
def clip(poly, a, b, c):
    """Part of a convex polygon on the side a*x + b*y <= c (Sutherland-Hodgman, exact fractions)."""
    out = []
    n = len(poly)
    for i in range(n):
        p, q = poly[i], poly[(i + 1) % n]
        fp, fq = a * p[0] + b * p[1] - c, a * q[0] + b * q[1] - c
        if fp <= 0: out.append(p)
        if (fp < 0 < fq) or (fq < 0 < fp):
            t = fp / (fp - fq)
            out.append((p[0] + t * (q[0] - p[0]), p[1] + t * (q[1] - p[1])))
    return out


def area(poly):
    return abs(sum(poly[i][0] * poly[(i + 1) % len(poly)][1] - poly[(i + 1) % len(poly)][0] * poly[i][1] for i in range(len(poly)))) / 2


def corners(poly):
    """Number of real corners (collinear points removed)."""
    pts = []
    for p in poly:
        if not pts or p != pts[-1]: pts.append(p)
    if len(pts) > 1 and pts[0] == pts[-1]: pts.pop()
    k = 0
    n = len(pts)
    for i in range(n):
        a, b, c = pts[i - 1], pts[i], pts[(i + 1) % n]
        if (b[0] - a[0]) * (c[1] - b[1]) - (b[1] - a[1]) * (c[0] - b[0]) != 0: k += 1
    return k


SQ = [(F(0), F(0)), (F(1), F(0)), (F(1), F(1)), (F(0), F(1))]


def cut_square(a, b, c):
    """Cut the unit square by the line a*x + b*y = c: returns the two parts."""
    return clip(SQ, a, b, c), clip(SQ, -a, -b, -c)


def is_half_cut(a, b, c):
    p, q = cut_square(a, b, c)
    return area(p) == area(q) == F(1, 2)


CUTS = {                                   # every cut a child may draw, as a line a*x + b*y = c
    'down the middle': (F(1), F(0), F(1, 2)), 'across the middle': (F(0), F(1), F(1, 2)),
    'corner to corner': (F(1), F(-1), F(0)), 'the other corner to corner': (F(1), F(1), F(1)),
    'a third of the way across': (F(1), F(0), F(1, 3)),
}


# tetrominoes on a square grid: canonical shape under every turn and flip
def canon(cells):
    best = None
    pts = [tuple(c) for c in cells]
    for flip in (False, True):
        for turn in range(4):
            q = []
            for (r, c) in pts:
                if flip: c = -c
                for _ in range(turn): r, c = c, -r
                q.append((r, c))
            mr = min(r for r, c in q); mc = min(c for r, c in q)
            key = tuple(sorted((r - mr, c - mc) for r, c in q))
            if best is None or key < best: best = key
    return best


def figs_in(x, kind, out=None):
    out = [] if out is None else out
    if isinstance(x, dict):
        if x.get('type') == kind: out.append(x)
        for v in x.values(): figs_in(v, kind, out)
    elif isinstance(x, list):
        for v in x: figs_in(v, kind, out)
    return out


def circle_part_angles(parts):
    return [F(360, parts)] * parts


def name_of_part(whole_parts):
    """What one of N equal parts of a whole is called, found from the part's share of the whole."""
    share = F(1, whole_parts)
    return {F(1, 2): 'half', F(1, 4): 'quarter'}.get(share)


def fold_parts(k):
    """Cut a paper in two with each fold: every existing region is split by the new fold."""
    regions = 1
    for _ in range(k): regions = sum(2 for _ in range(regions))
    return regions


def share_round_robin(n, groups):
    sizes = [0] * groups
    for i in range(n): sizes[i % groups] += 1
    assert len(set(sizes)) == 1, f'{n} cannot be shared equally into {groups}'
    return sizes[0]


# ------------------------------------------------------------------ online practice oracles
ORACLES = {
    'c1': lambda e: name_of_part(len(circle_part_angles(e['p']))) and ('a ' + name_of_part(e['p'])),
    't1': lambda e: share_round_robin(e['n'], 2),
    't2': lambda e: share_round_robin(e['n'], 4),
    't4': lambda e: fold_parts(e['k']),
    'g1': lambda e: e['n'] - share_round_robin(e['n'], 4),
    'g2': lambda e: sum(e['q'] for _ in range(4)),
}
BASE_ENV = {'t1': {'n': 8}, 't2': {'n': 12}, 't4': {'k': 3}, 'g1': {'n': 16}, 'g2': {'q': 3}}


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
    sh = lambda q: figs_in(q, 'shapes2d')
    gr = lambda q: figs_in(q, 'grid')

    # ---------------- the geometry facts the lesson rests on
    eq(is_half_cut(*CUTS['down the middle']), True, 'down the middle makes halves')
    eq(is_half_cut(*CUTS['across the middle']), True, 'across the middle makes halves')
    eq(is_half_cut(*CUTS['corner to corner']), True, 'corner to corner makes halves')
    eq(is_half_cut(*CUTS['the other corner to corner']), True, 'the other corner to corner makes halves')
    eq(is_half_cut(*CUTS['a third of the way across']), False, 'a cut a third of the way across does not make halves (crooked fold)')
    pa, pb = cut_square(*CUTS['corner to corner'])
    eq((corners(pa), corners(pb)), (3, 3), 'corner to corner: each half of a square is a triangle')
    pa, pb = cut_square(*CUTS['down the middle'])
    eq((corners(pa), corners(pb)), (4, 4), 'down the middle: each half is a rectangle')
    # two lines through the middle that cross make 4 equal parts; so do both corner lines; so do 3 parallel lines
    cross = clip(clip(SQ, 1, 0, F(1, 2)), 0, 1, F(1, 2))
    eq(area(cross), F(1, 4), 'a cross of two middle lines: one part is a quarter of the square')
    diag = clip(clip(SQ, 1, -1, 0), 1, 1, 1)
    eq(area(diag), F(1, 4), 'both corner lines: one part is a quarter of the square'); eq(corners(diag), 3, 'both corner lines: each part is a triangle')
    strip = clip(SQ, 1, 0, F(1, 4)); eq(area(strip), F(1, 4), '3 parallel lines: one strip is a quarter of the square')
    # unequal parts are not halves
    pa, pb = cut_square(*CUTS['a third of the way across']); eq((area(pa), area(pb)), (F(1, 3), F(2, 3)), 'unequal parts have unequal areas')
    # a half circle is half the area of a circle, a quarter circle a quarter
    A_c = F(1); eq((A_c / 2, A_c / 4, A_c / 2 > A_c / 4), (F(1, 2), F(1, 4), True), 'half circle is bigger than a quarter circle')
    eq(F(1, 4) + F(1, 4), F(1, 2), 'two quarters make a half'); eq(sum(F(1, 4) for _ in range(4)), 1, 'four quarters make a whole'); eq(sum(F(1, 2) for _ in range(2)), 1, 'two halves make a whole')

    # ---------------- Remember
    eq(share_round_robin(8, 2), 4, 'warm-up: 8 dots, 2 plates, 4 each')
    try:
        share_round_robin(7, 2); ok7 = True
    except AssertionError:
        ok7 = False
    eq(ok7, False, 'warm-up: 7 dots cannot be shared into 2 equal plates'); eq(7 - 2 * (7 // 2), 1, 'warm-up: 1 dot is left over')
    eq([f['shape'] for f in sh(sl['s-rem2']['blocks'])], ['circle', 'square', 'rectangle', 'triangle'], 'warm-up shapes in order A to D')
    eq([3, 4, 4], [3, 4, 4], 'sides (triangle, square, rectangle)')

    # ---------------- sneak-peek: fold twice gives 4 equal parts
    eq(fold_parts(1), 2, 'sneak-peek 1'); eq(fold_parts(2), 4, 'sneak-peek 2'); eq((d['sneak_peek']['a1'], d['sneak_peek']['a2'][:2]), ('2', '4.'), 'sneak answers')

    # ---------------- Explore and mini-lesson facts
    e1 = sh(sl['s-explore1-ans']['blocks'])[0]; eq((e1['shape'], e1['parts'], name_of_part(e1['parts'])), ('circle', 2, 'half'), 'explore 1 answer picture')
    e2 = sh(sl['s-explore2-ans']['blocks'])[0]; eq((e2['shape'], e2['parts'], name_of_part(e2['parts'])), ('circle', 4, 'quarter'), 'explore 2 answer picture')
    for sid in ('s-explore1', 's-explore2', 's-explore3', 's-m3', 's-m5'):          # the picture or answer is off the slide while the question is asked
        q, a = sl[sid], sl[sid + '-ans']
        eq((len(q['blocks']) < len(a['blocks']), any(b.get('t') == 'answer' for b in q['blocks'])), (True, False), sid + ' keeps the answer off the question slide')
    m1 = sh(sl['s-m1']['blocks'])[0]; eq((m1['parts'], name_of_part(m1['parts'])), (2, 'half'), 'mini 1')
    m2 = sh(sl['s-m2']['blocks'])[0]; eq((m2['parts'], name_of_part(m2['parts'])), (4, 'quarter'), 'mini 2')
    g1_, g2_ = gr(sl['s-m3']['blocks'])
    tot = lambda g: g['rows'] * g['cols']
    col = lambda g: len(g['squares'])
    eq(((tot(g1_), col(g1_), tot(g1_) - col(g1_)), (tot(g2_), col(g2_), tot(g2_) - col(g2_))), ((6, 3, 3), (6, 4, 2)), 'mini 3: counting coloured and white squares')
    eq([col(g) * 2 == tot(g) for g in (g1_, g2_)], [True, False], 'mini 3: half is coloured only in picture 1')
    m5 = sh(sl['s-m5']['blocks'])[0]; eq((m5['shape'], m5['parts'], name_of_part(m5['parts'])), ('rectangle', 4, 'quarter'), 'mini 5 item 1')
    eq(F(1, 2) > F(1, 4), True, 'mini 5 item 2: a half of the same circle is bigger than a quarter')
    eq([f['shape'] for f in sh(sl['s-m4']['blocks'])], ['circle', 'half_circle', 'quarter_circle'], 'mini 4 shapes')

    # ---------------- Start here
    S1 = [f for f in sh(T['S1'])]
    eq([F(len(f.get('shade', []) or []), f['parts']) == F(1, 2) for f in S1], [True, False, True], 'S1 half coloured? (by share of the whole)')
    eq(T['S1']['val'], ['Yes', 'No', 'Yes'], 'S1 val'); eq([p['val'] for p in T['S1']['parts']], T['S1']['val'], 'S1 part vals')
    s2 = S1[1]; eq((s2['shape'], s2['parts'], name_of_part(s2['parts'])), ('circle', 4, 'quarter'), 'S2 refers to shape B of S1, a circle in 4 equal parts'); eq(T['S2']['val'], [4, 'quarter'], 'S2 val')
    eq('shape B' in T['S2']['text'] and T['S1']['visuals'][1]['label'] == 'B', True, 'S2 names shape B and S1 labels it B')
    s3 = sh(T['S3']); eq([(f['parts'], name_of_part(f['parts'])) for f in s3], [(2, 'half'), (4, 'quarter')], 'S3 colour a half of the square and a quarter of the circle')
    eq([f['shape'] for f in s3], ['square', 'circle'], 'S3 shapes')
    eq([int(1 / F(1, 2)), int(1 / F(1, 4))], T['S4']['val'], 'S4 the number of halves and of quarters that make 1 whole'); eq([name_of_part(2), name_of_part(4)], ['half', 'quarter'], 'S4 names')
    eq(sh(T['S4']), [], 'S4 has no picture (the page is full)')
    s5 = {f['label']: f['shape'] for f in sh(T['S5'])}; eq((s5[str(T['S5']['val'][0])], s5[str(T['S5']['val'][1])]), ('half_circle', 'quarter_circle'), 'S5 shape numbers')
    eq(sorted(s5.values()), sorted(['circle', 'half_circle', 'quarter_circle', 'square']), 'S5 four different shapes')
    eq([f['shape'] for f in sh(T['S6'])], ['square', 'square'], 'S6 two blank squares'); eq([f['parts'] for f in sh(T['S6'])], [1, 1], 'S6 blank')
    eq([len(T['S6']['val'])], [2], 'S6 val')
    eq((len(T['S6']['parts']), 'ruler' in T['S6']['text']), (2, True), 'S6 asks for a ruler')

    # ---------------- Think harder
    t1 = sh(T['T1']); eq([(f['shape'], f['parts']) for f in t1], [('square', 1)] * 3, 'T1 three blank squares')
    eq(len([k for k in ('down the middle', 'across the middle', 'corner to corner') if is_half_cut(*CUTS[k])]), 3, 'T1 at least three different halving cuts exist')
    g = gr(T['T2'])[0]; total = g['rows'] * g['cols']
    eq((total, share_round_robin(total, 2), share_round_robin(total, 4)), (8, 4, 2), 'T2 8 squares: half 4, quarter 2'); eq(T['T2']['val'], [4, 2], 'T2 val')
    st = [True, False, True, False]
    eq(corners(cut_square(*CUTS['corner to corner'])[0]) == 3, st[0], 'T3 a half of a square can be a triangle')
    eq(any(not is_half_cut(*CUTS[k]) for k in CUTS), True, 'T3 some pair of parts are not halves'); eq(st[1], False, 'T3 any 2 parts are halves is false')
    eq(F(1, 4) + F(1, 4) == F(1, 2), st[2], 'T3 two quarters make a half')
    eq(F(1, 2) == F(1, 4), st[3], 'T3 a half circle is the same size as a quarter circle')
    eq(['True' if x else 'False' for x in st], T['T3']['val'], 'T3 val'); eq(len(T['T3']['tf']), 4, 'T3 four statements')
    eq(len(d['tiers']['think']), 3, 'three Think harder questions')

    # ---------------- Go further: Same Half, Different Shape
    cells = []
    for gg in gr(T['G1']):
        cs = [tuple(x) for x in gg['squares']]; cells.append(cs)
        eq((gg['rows'] * gg['cols'], len(cs), len(cs) * 2 == gg['rows'] * gg['cols']), (8, 4, True), 'G1 each rectangle: 8 squares, 4 coloured, half')
        eq((1, 3) in cs, False, 'G1 the label square is white')
    eq(T['G1']['val'][:3], [len(c) for c in cells], 'G1 counts')
    eq(len({canon(c) for c in cells}), 3, 'G1 the three coloured halves have three different shapes')
    eq(T['G1']['val'][3:], ['No'], 'G1 val: same shape no'); eq('A half of each is coloured' in T['G1']['text'], True, 'G1 says half of each is coloured (true: 4 of 8)')
    for c in cells:                                                    # each coloured half is joined up (edge to edge), so it is one piece
        seen = {c[0]}; todo = [c[0]]
        while todo:
            r, k = todo.pop()
            for (dr, dc) in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nb = (r + dr, k + dc)
                if nb in c and nb not in seen: seen.add(nb); todo.append(nb)
        eq(len(seen), len(c), 'G1 each coloured half is one connected piece')
    # properties of shapes for the riddles: (straight sides, curved sides, copies that make the whole circle or square)
    props = {'circle': (0, 1, 1), 'half circle': (1, 1, 2), 'quarter circle': (2, 1, 4), 'rectangle': (4, 0, None), 'triangle': (3, 0, 2)}
    ga = T['G2']['parts'][0]; gb = T['G2']['parts'][1]
    ra = [nm for nm in ga['choices'] if props[nm][0] == 1 and props[nm][1] == 1 and props[nm][2] == 2]
    eq((ra, ga['val']), (['half circle'], 'half circle'), 'G2 riddle a has exactly one answer among the choices')
    # riddle b: cut from a square, 3 corners (3 straight sides), 2 of me make the square
    rb = [nm for nm in gb['choices'] if props[nm][0] == 3 and props[nm][2] == 2]
    eq((rb, gb['val']), (['triangle'], 'triangle'), 'G2 riddle b has exactly one answer among the choices'); eq(corners(cut_square(*CUTS['corner to corner'])[0]), 3, 'G2 b: two triangles make the square')
    gq = gr(T['G3'])[0]; strip_n = len(gq['squares']); eq((gq['rows'], gq['cols'], strip_n), (1, 3, 3), 'G3 strip of 3 squares')
    whole = sum(strip_n for _ in range(4)); eq((whole, whole // 2), (12, 6), 'G3 whole 12, half 6'); eq(T['G3']['val'], [12, 6], 'G3 val')
    eq(len(d['tiers']['go']), 3, 'three Go further questions')

    # ---------------- Investigation: several ways to make 4 equal parts exist
    inv = d['tiers']['investigation']
    eq(fold_parts(1), 2, 'I1 first step: one fold makes 2 parts'); eq(inv['val'], ['2'], 'I1 val')
    eq(len({F(1, 4)}), 1, 'I1 all three ways give quarters of the same area')
    eq([c for c in (area(cross), area(diag), area(strip))], [F(1, 4)] * 3, 'I1 cross, corners, strips')
    eq([corners(cross), corners(diag), corners(strip)], [4, 3, 4], 'I1 the parts of the cross are 4-cornered, of the corner lines 3-cornered')
    eq(len(sh(inv)), 2, 'I1 two squares to draw on')

    # ---------------- exit ticket and home sheet
    eq((name_of_part(4), X['E1']['val'], '4 equal parts' in X['E1']['text']), ('quarter', ['quarter'], True), 'E1')
    eq((len([1 for _ in range(2)]), X['E2']['val']), (2, [2]), 'E2'); eq(X['E3']['val'], ['No'], 'E3 val'); pa, pb = cut_square(*CUTS['a third of the way across']); eq(area(pa) == area(pb), False, 'E3 unequal parts')
    eq((H['H1']['val'], name_of_part(4)), ('quarter', 'quarter'), 'H1'); eq((H['H2']['val'], 4), (4, 4), 'H2')
    eq(share_round_robin(12, 2), H['H3']['val'], 'H3'); eq([share_round_robin(16, 4), share_round_robin(16, 2)], H['H4']['val'], 'H4')
    eq(sum(1 for place in range(1, 7)), H['H5']['val'], 'H5 rewind: 6 children in front of the 7th'); eq(H['H5'].get('rewind_of'), 'Term 2 Lesson 1', 'H5 rewind tag')

    # ---------------- no class picture appears again in the workbook or the exit ticket
    def key(f): return (f['shape'], f['parts'], tuple(f.get('shade', []) or []))
    class_pics = set()
    for sid in ('s-explore1-ans', 's-explore2-ans', 's-m1', 's-m2', 's-m5'):
        class_pics |= {key(f) for f in sh(sl[sid]['blocks'])}
    wb_pics = set()
    for q in list(T.values()) + list(X.values()) + [inv]:
        wb_pics |= {key(f) for f in sh(q) if f['shape'] in ('square', 'circle', 'rectangle') and (f.get('shade'))}
    eq(wb_pics & class_pics, set(), 'no shaded class picture is repeated in the workbook or exit ticket: ' + str(sorted(wb_pics & class_pics)))

    # ---------------- kit contract against the kit builder
    import figs3
    svg = figs3.fold_shapes(4, 4, 2)
    n_circ = len(re.findall(r'<circle[^>]*stroke-dasharray', svg)); n_rect = len(re.findall(r'<rect[^>]*stroke-dasharray', svg)); n_lines = len(re.findall(r'<line ', svg))
    eq((n_circ, n_rect, n_lines), (4, 6, 6), 'kit page: 4 circles, 4 squares plus 2 rectangles (6 cut boxes), 3 faint lines on each rectangle')
    kc = {r['piece']: r for r in d['materials']['kit_contract']}
    eq([kc[k]['supplied'] for k in kc], [n_circ, 4, 2], 'kit contract supplied matches the page (circles, squares, rectangles)')
    eq(all(r['supplied'] >= r['max_used'] for r in kc.values()), True, 'kit contract: supplied >= used')
    eq(n_circ + (n_rect - 2) + 2, 10, 'ten pieces to cut (the hand-off in Lesson 30 says 10)')

    # ---------------- beyond
    b = d['beyond']; eq(all(i in T and T[i]['tier'] != 'start' for i in b['where']), True, 'beyond sits at Think harder or Go further')
    # ---------------- online practice (static items)
    items = {it['id']: it for it in d['online_practice']['items']}
    eq((items['c2']['answer'], items['c3']['answer'], items['c4']['answer'], items['c5']['answer']), (4, 'a half', 'a half circle', 'a quarter circle'), 'core statics')
    eq(items['t3']['answer'], 'False', 't3'); eq(items['g3']['answer'], 'No', 'g3 the 2 halves need not have the same shape')
    eq((items['r1']['answer'], items['r2']['answer']), ('the short hand', 'Ben'), 'rewinds from Term 3 Lesson 1 (the clock)')
    return n
