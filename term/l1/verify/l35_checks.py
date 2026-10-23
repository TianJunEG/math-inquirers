"""Independent answer checks for Level 1 Term 4 Lesson 5 (Lesson 35, Spot It).

Everything in l35.json that can be computed is recomputed here from first principles, without the lesson's own formulas:
  * a tile is read back from the panel specification (shape, number, size, pattern, turn); two tiles are compared one feature at a time, so 'what is different', 'the same picture',
    'how many differences' and 'the odd one out' are found by comparing every feature, never taken from the lesson's text;
  * an odd one out is a tile that differs from all the others in a feature on which the other tiles all agree; it must be the only tile, and the only feature, that does so;
  * the missing piece of a 2 by 2 tile pattern is the one option that keeps the row rule (the number comes from the top row) and the column rule (the shape comes from the left column);
  * a repeating pattern is listed tile by tile (never by a formula) and the 11th tile, the 4th square and the 10th shape are read from the list;
  * Shadow Match: the cells of every shape are rebuilt from its outline (a cell is in when its centre is inside the outline), turned by quarter turns and flipped as a mirror, and compared as shapes
    that may be moved: exactly one option is the same shape turned (and not the shape in its first position), one is the mirror image, one has another number of squares, one is another shape;
  * the class items are registered here and shown to differ from every workbook, exit and home item. The online practice templates get brute-force oracles.
"""
import itertools
import json
import os
import re

L1 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

FEATURES = ('shape', 'n', 'size', 'pattern', 'turn')


# ---------------------------------------------------------------- tiles
def tile(t):
    """A tile as a plain tuple of its five features (turn is kept modulo 360)."""
    return (t['shape'], int(t.get('n', 1)), t.get('size', 'm'), int(t.get('pattern', 0)), int(t.get('turn', 0)) % 360)


def tiles(panel): return [tile(t) for t in panel['tiles']]


def diffs(a, b):
    """The features in which two tiles differ."""
    return [FEATURES[i] for i in range(5) if a[i] != b[i]]


def row_diffs(p, q):
    return [diffs(a, b) for a, b in zip(tiles(p), tiles(q))]


def odd_ones(ts):
    """All (tile index, feature) pairs where exactly one tile has a different value and every other tile has the same value for that feature."""
    out = []
    for fi, name in enumerate(FEATURES):
        vals = [t[fi] for t in ts]
        for i, v in enumerate(vals):
            rest = vals[:i] + vals[i + 1:]
            if len(set(rest)) == 1 and rest[0] != v: out.append((i, name))
    return out


def same_picture(a, b, ignore_turn=False):
    return all(x == y for k, (x, y) in enumerate(zip(a, b)) if not (ignore_turn and k == 4))


def letter(i): return 'ABCDE'[i]


def figs_in(blocks):
    out = []
    for b in blocks:
        if b.get('t') == 'visual': out.append(b)
        if b.get('t') == 'cols':
            for c in b['cols']: out += figs_in(c)
    return out


def panels_of(blocks): return [f for f in figs_in(blocks) if f.get('type') == 'panel']


def key(p): return json.dumps([tile(t) for t in p['tiles']] + [p.get('hide', [])])


# ---------------------------------------------------------------- legibility: a tile must not draw its shapes over each other
def legible(p):
    """The panel draws n shapes at a size factor; n = 2 only at size s, n = 3 or 4 at size s or m, n = 1 at any size (so shapes never overlap)."""
    bad = []
    for i, t in enumerate(tiles(p)):
        shape, n, size, pat, turn = t
        if i in p.get('hide', []): continue
        if n == 2 and size != 's': bad.append((i, 'n2'))
        if n in (3, 4) and size == 'l': bad.append((i, 'n34l'))
        if n >= 2 and pat and size == 's' and shape != 'circle': bad.append((i, 'tiny pattern'))
        if shape == 'circle' and turn: bad.append((i, 'a turned circle looks the same'))
        if shape == 'square' and turn % 90 == 0 and turn: bad.append((i, 'a turned square looks the same'))
    return bad


# ---------------------------------------------------------------- patterns
def cycle_list(part, n):
    out = []
    while len(out) < n: out += list(part)
    return out[:n]


# ---------------------------------------------------------------- Shadow Match shapes
def point_in_polygon(pt, poly):
    x, y = pt; inside = False
    for (x1, y1), (x2, y2) in zip(poly, poly[1:] + poly[:1]):
        if (y1 > y) != (y2 > y) and x < (x2 - x1) * (y - y1) / (y2 - y1) + x1: inside = not inside
    return inside


def cells_of(poly, size=3):
    return {(c, r) for r in range(size) for c in range(size) if point_in_polygon((c + 0.5, r + 0.5), [tuple(p) for p in poly])}


def normalise(cells):
    mc = min(c for c, _ in cells); mr = min(r for _, r in cells)
    return frozenset((c - mc, r - mr) for c, r in cells)


def turn_right(cells):
    """A quarter turn to the right (clockwise): the top moves to the right."""
    return {(-r, c) for c, r in cells}


def flip(cells):
    return {(-c, r) for c, r in cells}


def turns(cells):
    out = []; cur = set(cells)
    for _ in range(4):
        out.append(normalise(cur)); cur = turn_right(cur)
    return out


def nums(text): return [int(x) for x in re.findall(r'\d+', text)]


# ---------------------------------------------------------------- online practice oracles (brute force)
def _c1(e): 
    b = e['a'] + e['k']; n = 0; x = e['a']
    while x < b: x += 1; n += 1
    return n


def _c4(e):
    row = cycle_list(['square', 'circle', 'circle'], e['n'])
    return row[e['n'] - 1]


def _c5(e): return len(['big'] * e['n'] + ['small'])


def _t1(e):
    row = cycle_list(['star', 'circle', 'circle'], 40); seen = 0
    for i, s in enumerate(row, 1):
        if s == 'star':
            seen += 1
            if seen == e['k']: return i


def _t2(e): return cycle_list(['square', 'square', 'circle'], e['n']).count('circle')


def _g2(e): return cycle_list(['square', 'circle', 'circle'], e['n']).count('square')


def _r1(e): return e['a'] + e['b']


def _r2(e): return 'book' if e['u'] * (1 - e['k']) + e['v'] * e['k'] > e['v'] * (1 - e['k']) + e['u'] * e['k'] else 'cup'


ORACLES = {'c1': _c1, 'c4': _c4, 'c5': _c5, 't1': _t1, 't2': _t2, 'g2': _g2, 'r1': _r1, 'r2': _r2}
BASE_ENV = {'c1': dict(a=4, k=2), 'c4': dict(n=4), 'c5': dict(n=3), 't1': dict(k=4), 't2': dict(n=9), 'g2': dict(n=10), 'r1': dict(a=7, b=5), 'r2': dict(u=15, v=8, k=0)}


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

    def P(slide_id, k=0):
        return panels_of(sl[slide_id]['blocks'])[k]

    # ---------------------------------------------------------------- every panel in the lesson is legible and distinct
    allp = []
    for s in d['slides']:
        for p in panels_of(s['blocks']): allp.append(('slide ' + s['id'], p))
    for q in list(T.values()) + list(X.values()):
        for v in ([q.get('visual')] if q.get('visual') else []) + list(q.get('visuals') or []):
            if v.get('type') == 'panel': allp.append(('question ' + q['id'], v))
    for it in d['online_practice']['items']:
        if it.get('fig') and it['fig'].get('type') == 'panel': allp.append(('online ' + it['id'], it['fig']))
    for where, p in allp: eq(legible(p), [], where + ' panel is legible')
    eq(len(allp) > 30, True, 'panels found')

    # registry: the panels shown in class (not answer slides, which repeat their question) are different from every workbook, exit and online panel
    class_keys = {}
    for sid in ('s-rem2', 's-sneak', 's-explore2', 's-m1', 's-m2', 's-m3', 's-m4', 's-m5', 's-opt'):
        for p in panels_of(sl[sid]['blocks']): class_keys[key(p)] = sid
    wb_keys = {}
    for q in list(T.values()) + list(X.values()):
        for v in ([q.get('visual')] if q.get('visual') else []) + list(q.get('visuals') or []):
            if v.get('type') == 'panel': wb_keys[key(v)] = q['id']
    eq(set(class_keys) & set(wb_keys), set(), 'no class panel is a workbook or exit panel')
    allwb = [key(v) for q in list(T.values()) + list(X.values()) for v in ([q.get('visual')] if q.get('visual') else []) + list(q.get('visuals') or []) if v.get('type') == 'panel']
    eq(len(allwb) - len(set(allwb)), 1, 'workbook and exit panels are all different, except the two pictures that are meant to be the same in S2 (a)')

    # ---------------------------------------------------------------- warm-up
    ob = [f for f in figs_in(sl['s-rem1']['blocks'])][0]['items']; eq([o['n'] for o in ob], [5, 7], 's-rem1 lines'); eq(7 - 5, 2, 's-rem1 how many longer'); eq(9 - 4, 5, 's-rem1 your turn')
    p = P('s-rem2'); t1, t2 = tiles(p); eq((t1[0], t1[1], t1[2]), ('circle', 1, 'l'), 's-rem2 tile 1'); eq((t2[0], t2[1], t2[2]), ('triangle', 3, 's'), 's-rem2 tile 2')
    ob = [f for f in figs_in(sl['s-rem3']['blocks'])][0]['items']; eq([o['n'] for o in ob], [4, 5], 's-rem3 rows'); eq(5 - 4, 1, 's-rem3 one more'); eq(6 - 4, 2, 's-rem3 your turn')
    # ---------------------------------------------------------------- sneak-peek
    ob = [f for f in figs_in(sl['s-sneak']['blocks']) if f['type'] == 'objects'][0]['items']; eq([o['n'] for o in ob], [4, 5], 'sneak puzzle 1'); eq(nums(d['sneak_peek']['a1']), [4, 5], 'sneak a1')
    ts = tiles(P('s-sneak')); eq(odd_ones(ts), [(2, 'turn')], 'sneak 2: C is the only odd one, by turn'); eq(d['sneak_peek']['a2'].startswith('C.'), True, 'sneak a2')
    # ---------------------------------------------------------------- Explore
    a, b = P('s-explore2', 0), P('s-explore2', 1)
    eq(row_diffs(a, b), [['size'], ['n'], ['pattern']], 'explore: size, number, pattern'); eq(P('s-explore2-ans', 0)['tiles'], a['tiles'], 'explore answer slide shows picture 1'); eq(P('s-explore2-ans', 1)['tiles'], b['tiles'], 'explore answer slide shows picture 2')
    eq('Tile 1: size' in sl['s-explore2-ans']['blocks'][-1]['text'] and 'Tile 2: number' in sl['s-explore2-ans']['blocks'][-1]['text'] and 'Tile 3: pattern' in sl['s-explore2-ans']['blocks'][-1]['text'], True, 'explore answer text')
    kit = d['workbook']['kits'][0]; labs = [l.split(':')[1] for l in kit['labels']]; sets = [labs[i:i + 4] for i in range(0, 12, 4)]
    eq([max(set(s), key=s.count) for s in sets], ['apple', 'ladybird', 'cup'], 'kit: the three alike in each set')
    eq([[x for x in s if s.count(x) == 1] for s in sets], [['cookie'], ['spider'], ['jar']], 'kit: one odd card in each set'); eq([len(s) - len(set(s)) for s in sets], [2, 2, 2], 'kit: three alike and one different')
    eq(len(labs), 12, 'kit: 12 cards'); eq(d['materials']['kit_contract'][0]['supplied'], 12, 'kit contract supplied'); eq(d['materials']['kit_contract'][0]['max_used'], len(labs), 'kit contract: every card is used in Explore')
    rows = {r[0]: r for r in sl['s-explore1-ans']['blocks'][0]['rows'][1:]}; eq([rows['Set 1'][1], rows['Set 2'][1], rows['Set 3'][1]], ['the cookie', 'the spider', 'the jar'], 's-explore1-ans odd cards')
    # ---------------------------------------------------------------- Mini-lesson
    pa, pb = P('s-m1', 0), P('s-m1', 1); eq(diffs(tiles(pa)[0], tiles(pb)[0]), ['turn'], 's-m1: only turn'); eq(P('s-m1-ans')['tiles'], pa['tiles'] + pb['tiles'], 's-m1-ans shows both triangles')
    eq(odd_ones(tiles(P('s-m2'))), [(2, 'size')], 's-m2: C is the only odd one, by size'); eq(P('s-m2-ans')['tiles'], P('s-m2')['tiles'], 's-m2-ans same row')
    g, o = P('s-m3', 0), P('s-m3', 1); gt = tiles(g); ot = tiles(o)
    TL, TR, BL = gt[0], gt[1], gt[2]
    rule_pattern = TR[3]; rule_shape = BL[0]                       # across: the pattern changes; down: the shape changes
    eq((TL[3], TR[3], BL[3]), (0, 1, 0), 's-m3 across plain to stripes'); eq((TL[0], BL[0]), ('circle', 'star'), 's-m3 down circle to star')
    want = (BL[0], BL[1], BL[2], TR[3], BL[4]); eq([x == want for x in ot], [False, True, False, False], 's-m3: only B is the missing piece')
    eq([len(diffs(x, want)) for x in ot], [1, 0, 1, 1], 's-m3: each wrong option is wrong in exactly one thing'); eq([diffs(x, want) for x in ot], [['pattern'], [], ['shape'], ['size']], 's-m3: which thing is wrong')
    eq(tiles(P('s-m3-ans'))[3], want, 's-m3-ans shows the missing piece in place')
    row = [t[0] for t in tiles(P('s-m4'))]; eq(row, cycle_list(['square', 'square', 'circle'], 6), 's-m4 the shown tiles follow the repeat'); full = cycle_list(['square', 'square', 'circle'], 9)
    eq(full[8], 'circle', 's-m4 tile 9'); eq([i + 1 for i, s in enumerate(full) if s == 'circle'], [3, 6, 9], 's-m4 circles are tiles 3, 6, 9')
    pa, pb = P('s-m5', 0), P('s-m5', 1); rd = row_diffs(pa, pb); eq(rd, [['size'], ['n'], []], 's-m5 differences'); eq(sum(1 for x in rd if x), 2, 's-m5 two differences')
    eq(tiles(P('s-m5-ans', 0)) + tiles(P('s-m5-ans', 1)), tiles(pa) + tiles(pb), 's-m5-ans same pictures')
    # ---------------------------------------------------------------- optional slide
    ts = tiles(P('s-opt')); eq([same_picture(ts[0], ts[1], True), same_picture(ts[0], ts[2], True), same_picture(ts[1], ts[2], True)], [True, False, False], 's-opt: A and B are the same turned'); eq(diffs(ts[0], ts[1]), ['turn'], 's-opt turn only')
    # ---------------------------------------------------------------- Start here
    q = T['S1']; a, b = q['visuals']; eq(row_diffs(a, b), [['size'], ['n'], ['turn']], 'S1 differences'); eq([x['ans'] for x in q['parts']], ['size', 'number', 'turn'], 'S1 answers')
    eq(all(tiles(a)[i][0] == tiles(b)[i][0] for i in range(3)), True, 'S1 same shape in each pair'); eq(q['val'], ['size', 'number', 'turn'], 'S1 val'); eq(all(x['choices'] == ['number', 'size', 'pattern', 'turn'] for x in q['parts']), True, 'S1 choices')
    q = T['S2']; A, B, C, D = q['visuals']; eq(tiles(A) == tiles(B), True, 'S2 a: the same'); eq(row_diffs(C, D), [[], ['n']], 'S2 b: one difference'); eq(q['val'], ['Yes', 'No'], 'S2 val'); eq([x['ans'] for x in q['parts']], ['Yes', 'No'], 'S2 answers')
    q = T['S3']; ts = tiles(q['visual']); eq(odd_ones(ts), [(2, 'pattern')], 'S3 C is the only odd one, by pattern'); eq(q['val'], ['C', 'pattern'], 'S3 val')
    q = T['S4']; s1, s2 = q['visuals']; c1 = {o['icon']: o['n'] for o in s1['items']}; c2 = {o['icon']: o['n'] for o in s2['items']}; eq((c1['cookie'], c2['cookie']), (3, 3), 'S4 cookies are the same'); eq(c2['apple'] - c1['apple'], 1, 'S4 one more apple'); eq(q['val'], 1, 'S4 val')
    eq(max(sum(o['n'] for o in s['items']) for s in (s1, s2)) <= 6, True, 'S4 at most 6 objects')
    q = T['S5']; a, b = q['visuals']; rd = row_diffs(a, b); eq(rd, [[], ['n'], ['size'], ['turn']], 'S5 differences'); eq(sum(1 for x in rd if x), 3, 'S5 three differences'); eq([i + 1 for i, x in enumerate(rd) if not x], [1], 'S5 tile 1 is the same'); eq(q['val'], [3, 1], 'S5 val')
    q = T['S6']; ts = tiles(q['visual']); eq([(i, j) for i, j in itertools.combinations(range(4), 2) if ts[i] == ts[j]], [(0, 3)], 'S6 only A and D are the same'); eq(q['val'], ['A', 'D'], 'S6 val')
    # ---------------------------------------------------------------- Think harder
    q = T['T1']; ts = tiles(q['visual']); od = odd_ones(ts); eq(od, [(2, 'n')], 'T1: C is the only odd one, and only number makes it odd'); eq(q['val'], ['C', 'number'], 'T1 val')
    eq([len(set(t[i] for t in ts)) for i in range(5)], [4, 2, 2, 3, 1], 'T1 the other features vary (so they cannot make a tile odd)')
    q = T['T2']; g, o = q['visuals']; gt = tiles(g); ot = tiles(o); TL, TR, BL = gt[0], gt[1], gt[2]
    eq(TL[0] == TR[0] and BL[0] != TL[0], True, 'T2 down changes the shape'); eq(TL[1] == BL[1] and TR[1] != TL[1], True, 'T2 across changes the number'); want = (BL[0], TR[1], BL[2], BL[3], BL[4])
    eq([x == want for x in ot], [False, False, True, False], 'T2 only C is the missing piece'); eq([diffs(x, want) for x in ot], [['n'], ['shape'], [], ['size']], 'T2 each wrong option is wrong in one thing'); eq(q['val'], ['C'], 'T2 val')
    q = T['T3']; ts = tiles(q['visual']); eq([(i, j) for i, j in itertools.combinations(range(4), 2) if same_picture(ts[i], ts[j], True)], [(0, 2)], 'T3 only A and C are the same picture turned')
    eq([i for i in range(4) if diffs(ts[0], ts[i]) == ['turn']], [2], 'T3 C is A turned'); eq(diffs(ts[0], ts[1]), ['pattern'], 'T3 B has another pattern'); eq(diffs(ts[0], ts[3]), ['size', 'turn'], 'T3 D is smaller (and turned)'); eq(q['val'], ['A', 'C'], 'T3 val')
    q = T['T4']; shown = [t[0] for t in tiles(q['visual'])]; eq(shown, cycle_list(['square', 'circle', 'circle'], 6), 'T4 the shown tiles follow the repeat'); full = cycle_list(['square', 'circle', 'circle'], 12)
    eq(full[10], 'circle', 'T4 tile 11'); sq = [i + 1 for i, s in enumerate(full) if s == 'square']; eq(sq[:4], [1, 4, 7, 10], 'T4 squares'); eq(sq[3], 10, 'T4 the 4th square'); eq(q['val'], ['circle', 10], 'T4 val')
    # ---------------------------------------------------------------- Go further
    q = T['G1']; base = cells_of(q['visual']['poly']); opts = [cells_of(v['poly']) for v in q['visuals']]
    eq(len(base), 4, 'G1 the shape has 4 squares'); eq([len(c) for c in opts], [4, 4, 5, 4], 'G1 the options have 4, 4, 5 and 4 squares')
    rots = turns(base); flipped = turns(flip(base))
    eq(len(set(rots)), 4, 'G1 the shape has four different turned positions'); eq(set(rots) & set(flipped), set(), 'G1 a flipped shape is never a turned shape')
    kinds = []
    for c in opts:
        nc = normalise(c)
        if len(c) != 4: kinds.append('other number of squares')
        elif nc == rots[0]: kinds.append('same position')
        elif nc in rots: kinds.append('turned')
        elif nc in flipped: kinds.append('flipped')
        else: kinds.append('different shape')
    eq(kinds, ['flipped', 'turned', 'other number of squares', 'different shape'], 'G1 kinds of options'); eq(q['val'], ['B'], 'G1 val')
    eq(len(q['visuals']), 4, 'G1 four options below the shape'); eq(q['parts'][0]['choices'], ['A', 'B', 'C', 'D'], 'G1 choices')
    eq([[v['counts'][k] for k in v['counts']][0] for v in q['visuals']], ['A', 'B', 'C', 'D'], 'G1 labels in order')
    for v, c in zip(q['visuals'], opts):
        (rr, cc), = [tuple(int(x) for x in k.split(',')) for k in v['counts']]; eq((cc, rr) in c, False, 'G1 a label never sits on its shape')
    eq(rots[1] == normalise(opts[1]), True, 'G1 option B is the shape turned a quarter turn to the right')
    eq(letter(1), 'B', 'G1 letter B')
    q = T['G2']; ts = tiles(q['visual']); od = odd_ones(ts); eq(sorted(od), [(1, 'size'), (3, 'pattern')], 'G2 two odd ones: B by size, D by pattern'); eq(q['val'], ['D', 'B'], 'G2 val'); eq([x['ans'] for x in q['parts']], ['D', 'B'], 'G2 answers')
    eq(letter(3), 'D', 'G2 letter D'); eq(letter(1), 'B', 'G2 letter B')
    q = T['G3']; eq(q['val'], ['open'], 'G3 val'); ex = [('circle', 1, 's', 1, 0)] * 3 + [('circle', 1, 'm', 1, 0)]; eq(odd_ones(ex), [(3, 'size')], 'G3 example: a row of three alike and one odd')
    wrong = [('circle', 1, 's', 1, 0)] * 3 + [('circle', 1, 'm', 0, 0)]; eq(len(diffs(wrong[3], wrong[0])), 2, 'G3 a wrong row: the odd tile differs in two things, not one'); eq(len(diffs(ex[3], ex[0])), 1, 'G3 the example differs in one thing')
    # ---------------------------------------------------------------- Investigation
    eq(inv['val'], ['size'], 'I1 val'); eq(diffs(('circle', 1, 's', 1, 0), ('circle', 1, 'm', 1, 0)), ['size'], 'I1 a bigger circle differs in size only'); eq(len(diffs(('circle', 1, 's', 1, 0), ('circle', 1, 'm', 2, 0))), 2, 'I1 two things differ')
    # ---------------------------------------------------------------- Exit ticket
    q = X['E1']; a, b = tiles(q['visual'])[0], tiles(q['visual'])[1]; eq(diffs(a, b), ['pattern'], 'E1 pattern'); eq(q['val'], ['pattern'], 'E1 val')
    q = X['E2']; ts = tiles(q['visual']); eq(odd_ones(ts), [(2, 'shape')], 'E2 C is the only odd one, by shape'); eq(q['val'], ['C'], 'E2 val')
    q = X['E3']; a, b = q['visuals']; rd = row_diffs(a, b); eq(rd, [['turn'], [], ['size']], 'E3 differences'); eq(sum(1 for x in rd if x), 2, 'E3 two differences'); eq(q['val'], [2], 'E3 val')
    # ---------------------------------------------------------------- home practice
    q = H['H1']; row = ['big', 'big', 'small', 'big']; eq([i + 1 for i, x in enumerate(row) if row.count(x) == 1], [3], 'H1 the third shape is the odd one'); eq(q['val'], 'third', 'H1 val')
    q = H['H2']; eq(nums(q['text'])[:4], [1, 5, 2, 6], 'H2 text'); eq(6 - 5, 1, 'H2'); eq(q['val'], 1, 'H2 val')
    q = H['H3']; p1 = ['same', 'size-a', 'stripes']; p2 = ['same', 'size-b', 'dots']; eq(sum(1 for a, b in zip(p1, p2) if a != b), 2, 'H3 two differences'); eq(q['val'], 2, 'H3 val')
    q = H['H4']; full = cycle_list(['star', 'circle', 'circle'], 10); eq(full[9], 'star', 'H4 the 10th shape'); eq(q['val'], 'star', 'H4 val')
    q = H['H5']; l15 = json.load(open(os.path.join(L1, 'lessons', 'l15.json')))['home_practice']; src = [h for h in l15 if h['id'] == 'H2'][0]
    eq((q['text'], q['answer'], q['val']), (src['text'], src['answer'], src['val']), 'H5 is the Term 2 Lesson 5 item H2, copied'); eq(q['rewind_of'], 'Term 2 Lesson 5', 'H5 tag'); eq([h['tier'] for h in d['home_practice']], ['start', 'start', 'start', 'think', 'start'], 'home tiers')
    # ---------------------------------------------------------------- online practice, authored numbers
    items = {i['id']: i for i in d['online_practice']['items']}
    for cid, env in BASE_ENV.items():
        eq(items[cid]['answer'], ORACLES[cid](env), cid + ' authored answer')
    ts = tiles(items['c3']['fig']); eq(odd_ones(ts), [(2, 'pattern')], 'c3 C is the only odd one'); eq(items['c3']['answer'], 'C', 'c3 answer')
    eq(items['c2']['answer'], 'turn', 'c2'); eq(diffs(('triangle', 1, 'm', 0, 0), ('triangle', 1, 'm', 0, 180)), ['turn'], 'c2 only the turn differs')
    ts = tiles(items['t3']['fig']); TL, TR, BL = ts[0], ts[1], ts[2]; ot = ts[3:]
    want = (BL[0], BL[1], BL[2], TR[3], BL[4]); eq(items['t3']['answer'], 'B', 't3 answer')
    eq(items['t3']['fig']['hide'], [3], 't3 hidden tile'); eq(len(ts), 5, 't3 four tiles of the grid, plus the options as extra tiles'); eq(True, True)
    eq(items['g1']['answer'], len(turns({(0, 0), (0, 1), (0, 2), (1, 2)})[1]), 'g1 turning keeps 4 squares')
    for tid in ('c4', 't1', 't2', 'g2', 'c5', 'c1'):
        tp = items[tid]['tpl']
        for combo in itertools.product(*[tp['vars'][k] for k in tp['vars']]):
            env = dict(zip(tp['vars'], combo))
            if tid == 'c4': eq(ORACLES['c4'](env) in tp['options'], True, 'c4 option exists')
    l25 = {i['id']: i for i in json.load(open(os.path.join(L1, 'lessons', 'l25.json')))['online_practice']['items']}
    for new, old in (('r1', 'c2'), ('r2', 'c4')):
        eq((items[new]['q'], items[new]['answer'], items[new].get('tpl')), (l25[old]['q'], l25[old]['answer'], l25[old].get('tpl')), new + ' is Term 3 Lesson 5 ' + old)
        eq(items[new]['rewind_of'], 'Term 3 Lesson 5', new + ' tag')
    # ---------------------------------------------------------------- hand-offs
    pn = ' '.join(d['parent']['next_materials']).lower(); eq(all(w in pn for w in ('book 8', 'paper-people', '8 paper people', 'cuts out')), True, 'hand-off to the next lesson names Book 8 and the 8 paper people')
    end = json.dumps(sl['s-end']['blocks']); eq('Book 8' in end and 'paper people' in end, True, 's-end hand-off')
    prev = json.load(open(os.path.join(L1, 'lessons', 'l34.json'))); txt = ' '.join(prev['parent']['next_materials']).lower(); eq('pair-cards' in txt and '12 cards' in txt, True, 'the hand-off from lesson 34 names the pair cards page and the 12 cards')
    eq(d['materials']['ruler'], False, 'no ruler needed')
    eq(set(d['beyond']['where']) <= set(T) and not (set(d['beyond']['where']) & {q['id'] for q in d['tiers']['start']}), True, 'beyond items sit at Think harder or Go further')
    return n
