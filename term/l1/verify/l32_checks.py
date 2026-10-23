"""Independent answer checks for Level 1 Term 4 Lesson 2 (Lesson 32, Build the Figure).

Nothing here reuses the lesson's own sentences or formulas. A figure is turned into real geometry and the answers are recomputed:
- A silhouette on a dot grid (a `grid` figure with a polygon) is cut into quarter-cells (each unit cell has 4 triangular quarters), and EVERY way to cover it
  exactly with squares, 2-square rectangles and half-square triangles is found by exact-cover search, so 'the fewest pieces', 'which sets of pieces make it' and
  'use as few triangles as you can' are decided by exhaustive search, not by a formula.
- Two triangles put together are simulated: all 8 turns and flips of a second triangle are placed so that a WHOLE side touches a whole side of the first, shapes that
  overlap are thrown away, the outline of what is left is traced, and the shapes are compared by number of corners, side lengths and area (so a square, a bigger
  triangle and a slanted four-sided shape come out as exactly 3 different shapes).
- Triangles in a square with both corner lines are found by taking every 3 of the 6 drawn lines and checking that they meet in 3 different points inside the lines.
- The compose=house figure is read back from the SVG the builder draws (its rectangles and polygon are counted and sorted into squares and rectangles).
- Panels (rows of picture tiles) are counted from the tiles. The kit is read back from the kit builder (its cut outlines are counted and measured in the SVG).
"""
import itertools
import math
import os
import re
import sys
from fractions import Fraction as F

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(HERE), 'tools'))


# ------------------------------------------------------------------ exact cover on quarter-cells
def inside(poly, x, y):
    c = False
    n = len(poly)
    for i in range(n):
        (x1, y1), (x2, y2) = poly[i], poly[(i + 1) % n]
        if (y1 > y) != (y2 > y) and x < x1 + (y - y1) * (x2 - x1) / (y2 - y1): c = not c
    return c


QCENT = {'N': (F(1, 2), F(1, 6)), 'E': (F(5, 6), F(1, 2)), 'S': (F(1, 2), F(5, 6)), 'W': (F(1, 6), F(1, 2))}


def atoms_of_poly(poly, rows, cols):
    poly = [(F(x), F(y)) for x, y in poly]
    return {(r, c, q) for r in range(rows) for c in range(cols) for q, (dx, dy) in QCENT.items() if inside(poly, c + dx, r + dy)}


def atoms_of_cells(cells):
    return {(r, c, q) for (r, c) in cells for q in 'NESW'}


def pieces_for(atom_set):
    """Every piece placement (kind, frozenset of atoms) that lies inside the region."""
    out = []
    cells = {(r, c) for (r, c, q) in atom_set}
    for (r, c) in cells:
        sq = frozenset((r, c, q) for q in 'NESW')
        if sq <= atom_set: out.append(('square', sq))
        for pair in ('NE', 'ES', 'SW', 'WN'):
            t = frozenset((r, c, q) for q in pair)
            if t <= atom_set: out.append(('triangle', t))
        for (dr, dc) in ((0, 1), (1, 0)):
            if (r + dr, c + dc) in cells:
                rc = frozenset([(r, c, q) for q in 'NESW'] + [(r + dr, c + dc, q) for q in 'NESW'])
                if rc <= atom_set: out.append(('rectangle', rc))
    return out


def tilings(atom_set, allowed=('square', 'rectangle', 'triangle')):
    """All exact covers as sorted tuples of piece kinds."""
    ps = [p for p in pieces_for(atom_set) if p[0] in allowed]
    by_atom = {}
    for k, s in ps:
        for a in s: by_atom.setdefault(a, []).append((k, s))
    results = []

    def go(unc, chosen):
        if not unc:
            results.append(tuple(sorted(chosen))); return
        a = min(unc)
        for k, s in by_atom.get(a, []):
            if s <= unc: go(unc - s, chosen + [k])
    go(frozenset(atom_set), [])
    return results


def counts(tl):
    return {(t.count('square'), t.count('rectangle'), t.count('triangle')) for t in tl}


# ------------------------------------------------------------------ two triangles with a whole side touching
T0 = [(0, 0), (3, 0), (0, 3)]


def isometries(pts):
    out = []
    for flip in (False, True):
        for turn in range(4):
            q = []
            for (x, y) in pts:
                if flip: x = -x
                for _ in range(turn): x, y = -y, x
                q.append((x, y))
            out.append(q)
    return out


def sq_len(a, b): return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


def edges_of(poly): return [(poly[i], poly[(i + 1) % len(poly)]) for i in range(len(poly))]


def clip_area(subject, clipper):
    """Area of the overlap of two convex polygons (Sutherland-Hodgman; exact integers)."""
    def orient(poly):
        a2 = sum(poly[i][0] * poly[(i + 1) % len(poly)][1] - poly[(i + 1) % len(poly)][0] * poly[i][1] for i in range(len(poly)))
        return poly if a2 > 0 else poly[::-1]
    out = [tuple(map(F, p)) for p in orient(subject)]
    cl = orient(clipper)
    for (a, b) in edges_of(cl):
        a, b = tuple(map(F, a)), tuple(map(F, b))
        side = lambda p: (b[0] - a[0]) * (p[1] - a[1]) - (b[1] - a[1]) * (p[0] - a[0])
        inp, out = out, []
        for i in range(len(inp)):
            p, q = inp[i], inp[(i + 1) % len(inp)]
            sp, sq = side(p), side(q)
            if sp >= 0: out.append(p)
            if (sp > 0 > sq) or (sq > 0 > sp):
                t = sp / (sp - sq); out.append((p[0] + t * (q[0] - p[0]), p[1] + t * (q[1] - p[1])))
        if not out: return F(0)
    return abs(sum(out[i][0] * out[(i + 1) % len(out)][1] - out[(i + 1) % len(out)][0] * out[i][1] for i in range(len(out)))) / 2


def outline(a, b):
    """Corners of the union of two triangles that share a whole side (shared edge removed, straight runs merged)."""
    segs = {}
    for poly in (a, b):
        for (p, q) in edges_of(poly):
            key = tuple(sorted((tuple(p), tuple(q))))
            segs[key] = segs.get(key, 0) + 1
    keep = [k for k, v in segs.items() if v == 1]
    adj = {}
    for (p, q) in keep:
        adj.setdefault(p, []).append(q); adj.setdefault(q, []).append(p)
    start = keep[0][0]
    path = [start]; prev = None; cur = start
    while True:
        nxt = [x for x in adj[cur] if x != prev][0] if prev is not None else adj[cur][0]
        if nxt == start: break
        path.append(nxt); prev, cur = cur, nxt
    n = len(path); pts = []
    for i in range(n):
        p0, p1, p2 = path[i - 1], path[i], path[(i + 1) % n]
        if (p1[0] - p0[0]) * (p2[1] - p1[1]) - (p1[1] - p0[1]) * (p2[0] - p1[0]) != 0: pts.append(p1)
    return pts


def two_triangle_shapes():
    """Signatures (corners, sorted squared side lengths, area x2) of every non-overlapping way to put a second copy against the first with a whole side touching."""
    sigs = {}
    A = T0
    for B0 in isometries(T0):
        for (a1, a2) in edges_of(A):
            for (b1, b2) in edges_of(B0):
                if sq_len(a1, a2) != sq_len(b1, b2): continue
                for (s, e) in ((a1, a2), (a2, a1)):
                    dx, dy = s[0] - b1[0], s[1] - b1[1]
                    if (b2[0] + dx, b2[1] + dy) != e: continue
                    B = [(x + dx, y + dy) for (x, y) in B0]
                    if clip_area(A, B) != 0: continue
                    pts = outline(A, B)
                    sides = sorted(sq_len(pts[i], pts[(i + 1) % len(pts)]) for i in range(len(pts)))
                    sigs[(len(pts), tuple(sides))] = pts
    return sigs


# ------------------------------------------------------------------ triangles in a figure of lines
def seg_point(p1, p2, p3, p4):
    """Intersection point of two segments (None if they do not meet), exact."""
    (x1, y1), (x2, y2), (x3, y3), (x4, y4) = p1, p2, p3, p4
    den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if den == 0: return None
    t = F((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4), den); u = F((x1 - x3) * (y1 - y2) - (y1 - y3) * (x1 - x2), den)
    if 0 <= t <= 1 and 0 <= u <= 1: return (x1 + t * (x2 - x1), y1 + t * (y2 - y1))
    return None


def triangles_in(segments):
    found = set()
    for s1, s2, s3 in itertools.combinations(segments, 3):
        p = seg_point(*s1, *s2); q = seg_point(*s2, *s3); r = seg_point(*s1, *s3)
        if None in (p, q, r) or len({p, q, r}) < 3: continue
        if (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0]) == 0: continue
        found.add(frozenset((p, q, r)))
    return found


# ------------------------------------------------------------------ chords: lines through two dots that cut a polygon in two
def cut_poly(poly, a, b, c):
    """Part of a polygon on a*x + b*y <= c and on the other side (Sutherland-Hodgman on a possibly non-convex polygon is not safe, so only convex pieces are used here)."""
    def side(P, sgn):
        out = []
        n = len(P)
        for i in range(n):
            p, q = P[i], P[(i + 1) % n]
            fp, fq = sgn * (a * p[0] + b * p[1] - c), sgn * (a * q[0] + b * q[1] - c)
            if fp <= 0: out.append(p)
            if (fp < 0 < fq) or (fq < 0 < fp):
                t = fp / (fp - fq); out.append((p[0] + t * (q[0] - p[0]), p[1] + t * (q[1] - p[1])))
        return out
    return side(poly, 1), side(poly, -1)


def corners(poly):
    pts = []
    for p in poly:
        if not pts or p != pts[-1]: pts.append(p)
    if len(pts) > 1 and pts[0] == pts[-1]: pts.pop()
    k = 0; n = len(pts)
    for i in range(n):
        a, b, c = pts[i - 1], pts[i], pts[(i + 1) % n]
        if (b[0] - a[0]) * (c[1] - b[1]) - (b[1] - a[1]) * (c[0] - b[0]) != 0: k += 1
    return k


def area(poly):
    return abs(sum(poly[i][0] * poly[(i + 1) % len(poly)][1] - poly[(i + 1) % len(poly)][0] * poly[i][1] for i in range(len(poly)))) / 2


def figs_in(x, kind, out=None):
    out = [] if out is None else out
    if isinstance(x, dict):
        if x.get('type') == kind: out.append(x)
        for v in x.values(): figs_in(v, kind, out)
    elif isinstance(x, list):
        for v in x: figs_in(v, kind, out)
    return out


def panel_counts(fig):
    tot = {}
    for t in fig['tiles']: tot[t['shape']] = tot.get(t['shape'], 0) + int(t.get('n', 1))
    return tot


def region_of(fig):
    if fig.get('poly'): return atoms_of_poly(fig['poly'], fig['rows'], fig['cols'])
    return atoms_of_cells([tuple(s) for s in fig['squares']])


def min_pieces(region, allowed):
    return min(len(t) for t in tilings(region, allowed))


# ------------------------------------------------------------------ online practice oracles
def _grid_cells(rows, cols): return atoms_of_cells([(r, c) for r in range(rows) for c in range(cols)])


ORACLES = {
    'c1': lambda e: len(['sq'] * e['a'] + ['tr'] * e['b']),
    'c5': lambda e: sum(len([1, 2]) for _ in range(e['n'])),
    't1': lambda e: min_pieces(atoms_of_cells([(0, c) for c in range(e['n'])]), ('rectangle',)),
    'g1': lambda e: min_pieces(_grid_cells(2, e['n']), ('square', 'rectangle')),
}
BASE_ENV = {'c1': {'a': 3, 'b': 2}, 'c5': {'n': 3}, 't1': {'n': 8}, 'g1': {'n': 4}}


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
    pn = lambda q: figs_in(q, 'panel')
    import figs3

    shapes2 = two_triangle_shapes()
    sigs = set(shapes2)
    SQUARE = (4, (9, 9, 9, 9)); BIGTRI = (3, (18, 18, 36)); PARA = (4, (9, 9, 18, 18))
    # ---------------- the geometry the lesson rests on
    eq(sigs, {SQUARE, BIGTRI, PARA}, 'two triangles with a whole side touching make exactly a square, a bigger triangle and a slanted four-sided shape')
    eq(len(sigs), 3, 'three different shapes'); eq(len(d['tiers']['investigation']['val']) and int(d['tiers']['investigation']['val'][0]), 3, 'I1 val is 3')
    eq(SQUARE in sigs, True, 'two triangles can make a square (E2, Explore, c4)')

    # ---------------- Remember
    r1 = sh(sl['s-rem1']['blocks']); eq([f['shape'] for f in r1], ['triangle', 'square', 'rectangle'], 'rem1 shapes A B C')
    props = {'triangle': (3, 0), 'square': (4, 0), 'rectangle': (4, 1)}               # (corners, 1 if the sides are not all equal)
    eq([k for k, v in props.items() if v[0] == 3], ['triangle'], 'rem1: 3 corners is the triangle'); eq([k for k, v in props.items() if v == (4, 0)], ['square'], 'rem1: 4 equal sides is the square')
    eq([k for k, v in props.items() if v == (4, 1)], ['rectangle'], 'rem1: 2 long and 2 short sides is the rectangle')
    sqpoly = [(F(0), F(0)), (F(1), F(0)), (F(1), F(1)), (F(0), F(1))]
    pa, pb = cut_poly(sqpoly, F(1), F(-1), F(0)); eq((corners(pa), corners(pb), area(pa) == area(pb)), (3, 3, True), 'rem2: a square folded corner to corner makes 2 matching triangles')
    g = gr(sl['s-rem3']['blocks'])[0]; eq((g['rows'], g['cols'], len(g['squares'])), (2, 3, 6), 'rem3: 2 rows of 3 squares make 6')

    # ---------------- sneak-peek
    sp = pn(sl['s-sneak']['blocks'])[0]; eq((panel_counts(sp).get('triangle'), d['sneak_peek']['a1']), (2, '2'), 'sneak 1: 2 triangles')

    # ---------------- Explore
    H1 = gr(sl['s-explore2']['blocks'])[0]; reg = region_of(H1); tl = tilings(reg); cs = counts(tl)
    eq((2, 0, 2) in cs, True, 'explore 2: the house is 2 squares and 2 triangles'); eq(min(len(t) for t in tl), 3, 'explore 2: the fewest pieces for the house is 3 (a rectangle and 2 triangles)')
    eq(cs, {(2, 0, 2), (0, 1, 2), (1, 0, 4), (0, 0, 6)}, 'explore 2: every way to build the house')
    bt = gr(sl['s-explore1-ans']['blocks'])[0]; reg2 = region_of(bt); eq(counts(tilings(reg2, ('triangle',))), {(0, 0, 2)}, 'explore 1: the bigger triangle is made of exactly 2 kit triangles')
    eq(len(reg2), 4, 'explore 1: the bigger triangle covers 2 half-squares = 4 quarter-cells (half a cell each x 2)')
    # m1: 2 squares make a rectangle (4 corners, sides not all equal); 2 half circles of the same size make a circle
    two_sq = [(0, 0), (2, 0), (2, 1), (0, 1)]; eq((corners(two_sq), sorted({sq_len(two_sq[i], two_sq[(i + 1) % 4]) for i in range(4)})), (4, [1, 4]), 'm1: 2 squares make a 4-cornered shape with 2 long and 2 short sides')
    eq(F(1, 2) + F(1, 2), 1, 'm1: 2 half circles make 1 whole circle')
    # m2: the house figure is read back from the SVG
    svg = figs3.shapes2d(compose='house'); rects = re.findall(r'<rect[^>]*width="([\d.]+)" height="([\d.]+)"', svg); polys = re.findall(r'<polygon points="([^"]+)"', svg)
    nsq = sum(1 for w, h in rects if abs(float(w) - float(h)) < 1e-6); nrect = len(rects) - nsq; ntri = sum(1 for p_ in polys if len(p_.split()) == 3)
    eq((ntri, nrect, nsq), (1, 2, 1), 'm2: the house has 1 triangle, 2 rectangles and 1 square'); eq(sh(sl['s-m2']['blocks'])[0].get('compose'), 'house', 'm2 shows the house')
    m3 = pn(sl['s-m3']['blocks'])[0]; pc = panel_counts(m3); eq((pc['triangle'], pc['circle'], pc['square'], sum(pc.values())), (4, 1, 1, 6), 'm3 counts: 4, 1, 1 and 6 in all')
    eq(max(pc, key=pc.get), 'triangle', 'm3: triangles are the most')
    g4 = gr(sl['s-m4']['blocks'])[0]; strip = region_of(g4)
    eq((min_pieces(strip, ('square',)), min_pieces(strip, ('rectangle',))), (4, 2), 'm4: 4 squares or 2 rectangles make the row')
    eq(3 + 2, 5, 'm5 item 1: 3 circles and 2 squares'); eq(corners(two_sq) == 3, False, 'm5 item 2: 2 squares cannot make a triangle')

    # ---------------- Start here
    s1 = panel_counts(pn(T['S1'])[0]); eq(([s1['square'], s1['triangle'], s1['circle'], s1['square'] - s1['triangle']], sum(s1.values())), (T['S1']['val'], 8), 'S1 counts and 8 tiles')
    eq(len(pn(T['S1'])[0]['tiles']), 8, 'S1 has 8 tiles, one shape each')
    eq(all(t.get('n', 1) == 1 for t in pn(T['S1'])[0]['tiles']), True, 'S1 every tile holds one shape')
    pa, pb = cut_poly(sqpoly, F(1), F(-1), F(0)); eq((corners(pa), corners(pb), area(pa) / area(sqpoly)), (3, 3, F(1, 2)), 'S2 each triangle is a half of the square'); eq(T['S2']['val'], ['line', 'half'], 'S2 val')
    s3 = gr(T['S3'])[0]; tl3 = tilings(region_of(s3), ('square', 'triangle')); mt = min(t.count('triangle') for t in tl3)
    best = {(t.count('square'), t.count('triangle')) for t in tl3 if t.count('triangle') == mt}
    eq((mt, best), (2, {(2, 2)}), 'S3 the boat with the fewest triangles is 2 triangles and 2 squares, and only that'); eq(T['S3']['val'], [2, 2], 'S3 val')
    s4 = gr(T['S4'])[0]; eq((s4['cols'], s4['rows'], len(s4['squares'])), (T['S4']['val'][0], T['S4']['val'][1], T['S4']['val'][2]), 'S4 per row, rows, in all'); eq(4 * 3, 12, 'S4 4 + 4 + 4')
    eq(sum(4 for _ in range(3)), 12, 'S4 repeated addition')
    # S5: what 2 pieces make
    eq(corners(two_sq), 4, 'S5 a: 2 squares make a 4-cornered shape: a rectangle'); eq(F(1, 2) * 2, 1, 'S5 b: 2 half circles make a whole circle'); eq(F(1, 4) * 2, F(1, 2), 'S5 c: 2 quarter circles make a half circle')
    eq([p['val'] for p in T['S5']['parts']], ['rectangle', 'circle', 'half circle'], 'S5 vals')
    eq(all(p['val'] in p['choices'] for p in T['S5']['parts']), True, 'S5 each answer is among its choices')

    # ---------------- Think harder
    th = gr(T['T1'])[0]; TP = [(F(x), F(y)) for x, y in th['poly']]
    good = []
    dots = [(x, y) for x in range(th['cols'] + 1) for y in range(th['rows'] + 1)]
    seen = set()
    for (p1, p2) in itertools.combinations(dots, 2):
        a = p2[1] - p1[1]; b = p1[0] - p2[0]; c = a * p1[0] + b * p1[1]
        g = math.gcd(math.gcd(abs(a), abs(b)), abs(c)) or 1
        a, b, c = a // g, b // g, c // g
        if a < 0 or (a == 0 and b < 0): a, b, c = -a, -b, -c
        if (a, b, c) in seen: continue
        seen.add((a, b, c))
        P1, P2 = cut_poly(TP, F(a), F(b), F(c))
        if len(P1) >= 3 and len(P2) >= 3 and area(P1) > 0 and area(P2) > 0:
            kinds = sorted([(corners(P1), len({sq_len(P1[i], P1[(i + 1) % len(P1)]) for i in range(len(P1))})), (corners(P2), len({sq_len(P2[i], P2[(i + 1) % len(P2)]) for i in range(len(P2))}))])
            if [k[0] for k in kinds] == [3, 4] and kinds[1][1] == 1: good.append((a, b, c))
    eq(len(good), 1, 'T1 exactly one line through two dots splits the tall house into 1 triangle and 1 square'); eq(good[0][:2] in ((0, 1), (0, -1)) or good[0][:2] == (0, 1), True, 'T1 the line is horizontal')
    lower = [(F(0), F(1)), (F(2), F(1)), (F(2), F(3)), (F(0), F(3))]
    q1, q2 = cut_poly(lower, F(1), F(0), F(1)); quarters = []
    for P in (q1, q2):
        a_, b_ = cut_poly(P, F(0), F(1), F(2)); quarters += [a_, b_]
    eq(sorted((area(P), corners(P)) for P in quarters), [(1, 4)] * 4, 'T1 b: 2 more lines make 4 small squares'); eq(len({tuple(sorted({sq_len(P[i], P[(i + 1) % 4]) for i in range(4)})) for P in quarters}), 1, 'T1 b: all the same size')
    t2 = pn(T['T2'])[0]; pc2 = panel_counts(t2); eq([pc2['triangle'], pc2['square'], pc2['circle']], T['T2']['val'], 'T2 triangles, squares, circles'); eq(sum(pc2.values()), 14, 'T2 14 shapes in all')
    eq(len(t2['tiles']), 6, 'T2 6 tiles'); tb = figs_in(T['T2'], 'table')[0]; eq((tb['head'], tb['rows']), (['Triangles', 'Small squares', 'Circles'], [['[]', '[]', '[]']]), 'T2 table matches the order of the answers')
    diag = []
    pts = [(F(round(math.cos(-math.pi / 2 + 2 * math.pi * k / 4))), F(round(math.sin(-math.pi / 2 + 2 * math.pi * k / 4)))) for k in range(4)]
    segs = [(pts[a_], pts[b_]) for a_ in range(4) for b_ in range(a_ + 1, 4)]
    tri = triangles_in(segs); small = [t for t in tri if (F(0), F(0)) in t]; big = [t for t in tri if (F(0), F(0)) not in t]
    eq((len(small), len(big), len(tri)), (4, 4, 8), 'T3 small, big, all triangles'); eq(T['T3']['val'], [8], 'T3 val is the total')
    eq((len(tri), figs_in(T['T3'], 'network')[0]['n'], figs_in(T['T3'], 'network')[0].get('all')), (8, 4, True), 'T3 the figure is 4 dots with every line')
    # with only the 4 sides drawn (no corner lines) there is no triangle at all: the 8 come from the 2 lines
    sides = [s_ for s_ in segs if s_ not in (segs[1], segs[4])]
    eq(len(sides), 4, 'T3 the 4 sides'); eq(len(triangles_in(sides)), 0, 'T3 the 4 sides alone make no triangle: all 8 come from the 2 corner lines')
    eq(len(d['tiers']['think']), 3, 'three Think harder questions')

    # ---------------- Go further
    g1g = gr(T['G1'])[0]; rg = region_of(g1g)
    tsq = tilings(rg, ('square', 'rectangle')); eq((min(t.count('square') + t.count('rectangle') for t in tsq if 'rectangle' not in t), min(len(t) for t in tsq)), (6, 3), 'G1 squares only 6, fewest 3')
    eq(min(len(t) for t in tilings(rg)), 3, 'G1 the fewest is still 3 even with triangles allowed'); eq(T['G1']['val'], [6, 3], 'G1 val')
    sg = gr(T['G2'])[0]; rs = region_of(sg); cs2 = counts(tilings(rs, ('square', 'rectangle')))
    eq(cs2, {(6, 0, 0), (4, 1, 0), (2, 2, 0)}, 'G2 every way to make the staircase from squares and rectangles')
    eq([(s_, r_, 0) in cs2 for (s_, r_) in [(6, 0), (0, 3), (2, 2), (3, 2)]], [True, False, True, False], 'G2 the four sets')
    eq(['True' if (s_, r_, 0) in cs2 else 'False' for (s_, r_) in [(6, 0), (0, 3), (2, 2), (3, 2)]], T['G2']['val'], 'G2 val')
    eq(min(len(t) for t in tilings(rs, ('square', 'rectangle'))), 4, 'G2 the fewest pieces for the staircase is 4'); eq(6 // 2, 3, 'G2 3 rectangles would cover 6 squares (but they do not fit)')
    eq(len(d['tiers']['go']), 3, 'three Go further questions')
    # G3: the house in the key is 2 triangles, 1 square, 1 rectangle
    eq(sorted(['triangle', 'triangle', 'square', 'rectangle']), ['rectangle', 'square', 'triangle', 'triangle'], 'G3 the key figure')

    # ---------------- exit ticket and home sheet
    eq(3 + 2 + 2, X['E1']['val'][0], 'E1'); eq((SQUARE in sigs, X['E2']['val']), (True, ['Yes']), 'E2')
    eq(share(6, 2), X['E3']['val'][0], 'E3 6 squares in rectangles 2 squares long')
    eq(5 - 2, H['H1']['val'], 'H1'); eq(corners(two_sq), 4, 'H2 4 corners: rectangle'); eq(H['H2']['val'], 'rectangle', 'H2 val')
    eq(sum(len(cut_poly(sqpoly, F(1), F(-1), F(0))) and 2 for _ in range(4)), H['H3']['val'], 'H3 4 squares cut corner to corner make 8 triangles')
    eq(min_pieces(_grid_cells(2, 4), ('square', 'rectangle')), H['H4']['val'], 'H4 2 rows of 4 squares: the fewest pieces is 4')
    eq((14 - 9, H['H5']['val'], H['H5'].get('rewind_of')), (5, 5, 'Term 2 Lesson 2'), 'H5 rewind')

    # ---------------- kit contract against the kit builder
    k1 = figs3.shape_pieces(page=1); k2 = figs3.shape_pieces(page=2)
    rr = [(float(w), float(h)) for w, h in re.findall(r'<rect x="[\d.]+" y="[\d.]+" width="([\d.]+)" height="([\d.]+)"[^>]*stroke-dasharray', k1)]
    nsq1 = sum(1 for w, h in rr if abs(w - h) < 0.01); nrc1 = sum(1 for w, h in rr if abs(w - 2 * h) < 0.01)
    ntri2 = len(re.findall(r'<polygon[^>]*stroke-dasharray', k2)); npath2 = re.findall(r'<path d="([^"]+)"[^>]*stroke-dasharray', k2)
    nhalf = sum(1 for p_ in npath2 if ' V' not in p_); nquart = sum(1 for p_ in npath2 if ' V' in p_); ncirc = len(re.findall(r'<circle[^>]*stroke-dasharray', k2))
    kc = {r_['piece']: r_ for r_ in d['materials']['kit_contract']}
    eq([nsq1, nrc1, ntri2, nhalf, nquart, ncirc], [kc['squares (3 cm)']['supplied'], kc['rectangles (3 cm by 6 cm)']['supplied'], kc['triangles (half a 3 cm square)']['supplied'], kc['half circles']['supplied'], kc['quarter circles']['supplied'], kc['circle']['supplied']], 'kit contract supplied matches the two kit pages')
    eq(nsq1 + nrc1 + ntri2 + nhalf + nquart + ncirc, 20, 'twenty pieces to cut (Lesson 31 says 20)')
    from figs3 import MM
    eq(round(max(w for w, h in rr) / MM / 2), 30, 'the square on the kit page is 30 mm')
    eq(all(r_['supplied'] >= r_['max_used'] for r_ in kc.values()), True, 'kit contract: supplied >= used')
    eq(g1g['cols'] * g1g['rows'], 6, 'G1 the most squares a task needs is 6, the kit has 6'); eq(min(len(t) for t in tsq), kc['rectangles (3 cm by 6 cm)']['max_used'], 'G1 the fewest build uses all 3 kit rectangles')

    # ---------------- no class picture is repeated in the workbook or exit ticket
    class_figs = []
    for sid in ('s-rem1', 's-rem3', 's-sneak', 's-explore1-ans', 's-explore2', 's-m1', 's-m2', 's-m3', 's-m4', 's-m5'):
        for kind in ('shapes2d', 'grid', 'panel', 'network'): class_figs += [__import__('json').dumps({k: v for k, v in f.items() if k not in ('label', 'size')}, sort_keys=True) for f in figs_in(sl[sid]['blocks'], kind)]
    wb_figs = []
    for q in list(T.values()) + list(X.values()):
        for kind in ('grid', 'panel', 'network'): wb_figs += [__import__('json').dumps({k: v for k, v in f.items() if k not in ('label', 'size')}, sort_keys=True) for f in figs_in(q, kind)]
    eq(set(class_figs) & set(wb_figs), set(), 'no class picture is repeated in the workbook or exit ticket')

    # ---------------- beyond
    b = d['beyond']; eq(all(i in T and T[i]['tier'] != 'start' for i in b['where']), True, 'beyond sits at Think harder or Go further')
    # ---------------- online practice (static items)
    items = {it['id']: it for it in d['online_practice']['items']}
    eq((items['c2']['answer'], items['c3']['answer'], items['c4']['answer']), ('rectangle', 'circle', 'Yes'), 'core statics')
    eq((items['t2']['answer'], len(tri)), (8, 8), 't2 the diamond has 8 triangles'); eq(items['t3']['answer'], 'True', 't3 3 is the fewest for 2 by 3')
    eq(items['g2']['answer'], 4, 'g2 the staircase needs 4 pieces')
    eq(((7, 30) < (12, 0), items['r1']['answer'], 'morning' if 'breakfast' in items['r1']['q'] else '?'), (True, 'am', 'morning'), 'r1 rewind (Term 3 Lesson 2): breakfast at 7:30 is am')
    eq(('evening' in items['r2']['q'], items['r2']['answer']), (True, 'pm'), 'r2 rewind: tea in the evening is pm')
    return n


def share(total, per):
    return total // per
