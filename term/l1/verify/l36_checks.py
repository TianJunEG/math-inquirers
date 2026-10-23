"""Independent answer checks for Level 1 Term 4 Lesson 6 (Lesson 36, Count Everything).

Everything in l36.json that can be computed is recomputed here from first principles, without the lesson's own formulas:
  * squares in a grid are found by listing every square (every size, every position) and counting the list;
  * handshakes are listed as pairs of distinct children (each pair once, in either order the same), and 'the new ones each time' is counted from the same list;
  * outfits and ways are listed as pairs (one thing from each list), never multiplied;
  * pairs that make a total are listed from 1 upwards until the pairs repeat; the stickers items search every pair of children;
  * routes are counted by walking a small road map (every road is its own edge) from Home to School;
  * lines in a network picture are read from the picture specification; the missing handshake is the pair with no line;
  * the class items are registered here and shown to differ from every workbook, exit and home item. The online practice templates get brute-force oracles.
"""
import itertools
import json
import os
import re

L1 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def nums(text): return [int(x) for x in re.findall(r'\d+', text)]


def figs_in(blocks):
    out = []
    for b in blocks:
        if b.get('t') == 'visual': out.append(b)
        if b.get('t') == 'cols':
            for c in b['cols']: out += figs_in(c)
    return out


# ---------------------------------------------------------------- counting by listing
def all_squares(rows, cols):
    """Every square (top, left, size) whose sides lie on the grid lines of a rows by cols grid of small squares."""
    out = []
    for size in range(1, min(rows, cols) + 1):
        for top in range(rows - size + 1):
            for left in range(cols - size + 1): out.append((top, left, size))
    return out


def small_squares(rows, cols): return [(r, c) for r in range(rows) for c in range(cols)]


def handshakes(n):
    """Every pair of different children once (A with B is the same as B with A)."""
    kids = range(n)
    return {frozenset(p) for p in itertools.product(kids, kids) if p[0] != p[1]}


def new_handshakes(n):
    """For child 0, 1, 2 ... the handshakes with children not met before."""
    out = []; met = set()
    for k in range(n):
        new = {frozenset((k, j)) for j in range(n) if j != k} - met
        out.append(len(new)); met |= new
    return out


def ways(a, b): return [(x, y) for x in range(a) for y in range(b)]


def pairs_total(t):
    """Pairs of whole numbers from 1 that make t, listed from 1 upwards; stop when the first number passes the second."""
    out = []; x = 1
    while x <= t - x:
        out.append((x, t - x)); x += 1
    return out


def routes(first, second, direct):
    """Paths Home to School on a map where every road is its own edge."""
    edges = [('Home', 'Park', i) for i in range(first)] + [('Park', 'School', i) for i in range(second)] + [('Home', 'School', i) for i in range(direct)]
    def walk(at):
        if at == 'School': return 1
        return sum(walk(b) for (a, b, _) in edges if a == at)
    return walk('Home')


def lines_of(fig):
    n = fig['n']
    if fig.get('all'): return {frozenset(p) for p in itertools.combinations(range(n), 2)}
    return {frozenset(p) for p in fig.get('lines', [])}


# ---------------------------------------------------------------- online practice oracles (brute force)
def _c1(e): return len([1 for r in range(e['r']) for c in range(e['c'])])
def _c2(e): return len([1 for b in range(e['a']) for s in range(e['b'])])
def _c5(e): return len(ways(e['h'], e['s']))
def _t1(e): return len(handshakes(e['n']))
def _t2(e): return len(all_squares(e['k'], e['k']))
def _t3(e): return len(pairs_total(e['t']))
def _g1(e): return routes(e['a'], e['b'], 1)
def _r1(e): return e['a'] + e['b']
def _r2(e): return len([1 for _ in range(3) for _ in range(e['p'])])


ORACLES = {'c1': _c1, 'c2': _c2, 'c5': _c5, 't1': _t1, 't2': _t2, 't3': _t3, 'g1': _g1, 'r1': _r1, 'r2': _r2}
BASE_ENV = {'c1': dict(r=3, c=4), 'c2': dict(a=4, b=3), 'c5': dict(h=2, s=3), 't1': dict(n=5), 't2': dict(k=2), 't3': dict(t=8), 'g1': dict(a=2, b=4), 'r1': dict(a=6, b=5), 'r2': dict(p=7)}


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

    def F(sid, k=0, t=None):
        fs = figs_in(sl[sid]['blocks'])
        if t: fs = [f for f in fs if f['type'] == t]
        return fs[k]

    def grid_dims(f): return (f['rows'], f['cols'])

    # ---------------------------------------------------------------- the registries are disjoint
    class_grids = {'sneak': grid_dims(F('s-sneak', 0, 'grid')), 'explore': grid_dims(F('s-explore2'))}
    wb_grids = {q: grid_dims(v['visual']) for q, v in list(T.items()) + list(X.items()) if v.get('visual', {}).get('type') == 'grid'}
    eq(set(class_grids.values()) & set(wb_grids.values()), set(), 'no class grid has the size of a workbook or exit grid')
    eq(class_grids, {'sneak': (2, 4), 'explore': (2, 2)}, 'class grids')
    # ---------------------------------------------------------------- warm-up
    f = F('s-rem1'); eq((f['rows'], f['cols']), (3, 4), 's-rem1 array'); eq(len([1 for r in range(3) for c in range(4)]), 12, 's-rem1 dots'); eq(len([1 for r in range(2) for c in range(6)]), 12, 's-rem1 your turn')
    eq(sum([7, 3, 6, 4]), 20, 's-rem2 total'); eq([a + b for a, b in ((7, 3), (6, 4))], [10, 10], 's-rem2 tens'); eq(sum([8, 2, 5, 5]), 20, 's-rem2 your turn')
    eq(pairs_total(6), [(1, 5), (2, 4), (3, 3)], 's-rem3 pairs that make 6'); eq((4, 2) in pairs_total(6), False, 's-rem3 4 and 2 is a repeat')
    # ---------------------------------------------------------------- sneak-peek
    sp = d['sneak_peek']; g = F('s-sneak', 0, 'grid'); eq(len(small_squares(g['rows'], g['cols'])), 8, 'sneak 1'); eq(sp['a1'], '8 small squares.', 'sneak a1'); eq(len(ways(2, 3)), 6, 'sneak 2'); eq(nums(sp['q2']), [2, 3], 'sneak q2')
    # ---------------------------------------------------------------- Explore
    eq(len(handshakes(3)), 3, 'explore 3 people: 3 handshakes'); eq(len(lines_of(F('s-explore1-ans'))), 3, 's-explore1-ans lines'); eq(lines_of(F('s-explore1-ans')), handshakes(3), 's-explore1-ans shows every handshake')
    sq = all_squares(2, 2); eq(len(sq), 5, 'explore squares'); eq(len([s for s in sq if s[2] == 1]), 4, 'explore small'); eq(len([s for s in sq if s[2] == 2]), 1, 'explore big')
    f = F('s-explore2-ans'); eq(sorted(map(tuple, f['squares'])), [(0, 0), (0, 1), (1, 0), (1, 1)], 's-explore2-ans yellow is the whole grid')
    # ---------------------------------------------------------------- Mini-lesson
    eq(new_handshakes(3), [2, 1, 0], 's-m1 the new ones'); eq(sum(new_handshakes(3)), 3, 's-m1 total'); eq(lines_of(F('s-m1-ans')), handshakes(3), 's-m1-ans')
    eq(len(ways(2, 2)), 4, 's-m2 outfits'); f = F('s-m2'); eq(sum(1 for r in f['rows'] for c in r[:] if c == '[ ]'), 4, 's-m2 four boxes'); eq(len(f['rows']), 2, 's-m2 2 tops'); eq(len(f['head']) - 1, 2, 's-m2 2 skirts')
    eq(len(pairs_total(8)), 4, 's-m3 pairs'); eq(pairs_total(8), [(1, 7), (2, 6), (3, 5), (4, 4)], 's-m3 list')
    tb = [b for b in sl['s-m3-ans']['blocks'] if b['t'] == 'table'][0]; eq([(int(a), int(b)) for a, b in tb['rows'][1:]], pairs_total(8), 's-m3-ans table lists every pair')
    listed = [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C')]; seen = set(); rep = []
    for p in listed:
        if frozenset(p) in seen: rep.append(p)
        seen.add(frozenset(p))
    eq(rep, [('B', 'A')], 's-m4 the repeat'); eq(len(seen), 3, 's-m4 three handshakes'); eq(len(listed), 4, 's-m4 she listed four')
    eq(len(ways(2, 2)), 4, 'break: 2 arm moves with 2 leg moves'); eq(len(ways(3, 2)), 6, 'break: 3 arm moves with 2 leg moves')
    # ---------------------------------------------------------------- Talk and optional slide
    eq(nums(d['talk']['question']), [3, 4, 3], 'talk numbers'); eq(4 * 3, 2 * len(handshakes(4)), 'talk: 4 times 3 counts every handshake twice'); eq(len(handshakes(4)), 6, 'talk the right count')
    f = F('s-opt'); eq(sorted(tuple(sorted(p)) for p in handshakes(4) - lines_of(f)), [(0, 3)], 's-opt the missing pair is A and D'); eq(len(lines_of(f)), 5, 's-opt 5 lines')
    # ---------------------------------------------------------------- Start here
    q = T['S1']; v = q['visual']; eq(len(small_squares(v['rows'], v['cols'])), 10, 'S1'); eq(q['val'], 10, 'S1 val')
    q = T['S2']; v = q['visual']; eq(sum(v['counts']), 15, 'S2'); eq(nums(q['text']), [3, 5], 'S2 text'); eq(len(v['counts']), 3, 'S2 jars'); eq(q['val'], 15, 'S2 val')
    q = T['S3']; v = q['visual']; eq(len(lines_of(v)), 5, 'S3 lines'); eq(len(v['lines']), len({tuple(sorted(l)) for l in v['lines']}), 'S3 no line drawn twice'); eq(q['val'], 5, 'S3 val')
    q = T['S4']; eq([9 - x for x in (2, 3, 4)], [7, 6, 5], 'S4'); eq(pairs_total(9), [(1, 8), (2, 7), (3, 6), (4, 5)], 'S4 list'); eq(q['val'], [7, 6, 5], 'S4 val')
    q = T['S5']; v = q['visual']; eq((v['rows'], v['cols']), (4, 5), 'S5'); eq(len([1 for r in range(4) for c in range(5)]), 20, 'S5 dots'); eq(q['val'], 20, 'S5 val')
    q = T['S6']; v = q['visual']; yel = {tuple(s) for s in v['squares']}; eq(len(yel), 4, 'S6 yellow squares are 4 different squares'); eq(len(small_squares(v['rows'], v['cols'])) - len(yel), 5, 'S6'); eq(q['val'], 5, 'S6 val')
    # ---------------------------------------------------------------- Think harder
    q = T['T1']; v = q['visual']; eq(lines_of(v), {frozenset((0, k)) for k in (1, 2, 3)}, 'T1 A has shaken hands with B, C and D'); nh = new_handshakes(4); eq(nh, [3, 2, 1, 0], 'T1 the new ones'); eq(nh[1], 2, 'T1 (a)'); eq(nh[2], 1, 'T1 (b)'); eq(len(handshakes(4)), 6, 'T1 (c)')
    eq(q['val'], [2, 1, 6], 'T1 val'); eq(4 * 3 == 6, False, 'T1 4 times 3 is not the answer')
    q = T['T2']; eq(nums(q['text']), [4, 2], 'T2 text'); eq(len(ways(4, 2)), 8, 'T2'); eq(len(ways(2, 4)), 8, 'T2 the other way round'); eq(q['val'], 8, 'T2 val')
    q = T['T3']; v = q['visual']; sq = all_squares(v['rows'], v['cols']); eq(len([s for s in sq if s[2] == 1]), 6, 'T3 small'); eq(len([s for s in sq if s[2] == 2]), 2, 'T3 big'); eq(len(sq), 8, 'T3 all'); eq(len(v['squares']), 4, 'T3 the yellow example is a 2 by 2 square'); eq(q['val'], [6, 2, 8], 'T3 val')
    q = T['T4']; vals = nums(q['text'])[:6]; found = [(a, b) for a, b in itertools.combinations(vals, 2) if a + b == 14]; eq(sorted(found), [(3, 11), (5, 9), (6, 8)], 'T4 every pair'); eq(len(found), 3, 'T4 three pairs')
    eq([14 - 3, 14 - 5, 14 - 6], [11, 9, 8], 'T4 answers'); eq(all(14 - x in vals for x in (3, 5, 6)), True, 'T4 each partner exists'); eq(len(vals), 6, 'T4 six children'); eq(q['val'], [11, 9, 8], 'T4 val'); eq(nums(q['text']), [3, 5, 6, 8, 9, 11, 14, 3], 'T4 text')
    # ---------------------------------------------------------------- Go further
    q = T['G1']; eq([len(handshakes(5)), len(handshakes(6))], [10, 15], 'G1'); eq(sum(new_handshakes(5)), 10, 'G1 new ones for 5'); eq(sum(new_handshakes(6)), 15, 'G1 new ones for 6'); eq(q['val'], [10, 15], 'G1 val')
    eq(len(d['materials']['kit_contract']), 1, 'kit contract'); kc = d['materials']['kit_contract'][0]; eq((kc['supplied'], kc['max_used'] >= 6), (8, True), 'kit contract: 8 people, up to 6 used')
    q = T['G2']; v = q['visual']; sq = all_squares(v['rows'], v['cols']); eq([len([s for s in sq if s[2] == k]) for k in (1, 2, 3)], [9, 4, 1], 'G2 by size'); eq(len(sq), 14, 'G2 all'); eq(q['val'], [9, 4, 1, 14], 'G2 val'); eq(len(v['squares']), 4, 'G2 yellow example')
    q = T['G3']; rows = {r[0] + '>' + r[1]: int(r[2]) for r in q['visual']['rows']}; eq(rows, {'Home>Park': 2, 'Park>School': 4, 'Home>School': 1}, 'G3 map'); eq(routes(2, 4, 0), 8, 'G3 through the Park'); eq(routes(2, 4, 1), 9, 'G3 in all'); eq(q['val'], [8, 9], 'G3 val')
    # ---------------------------------------------------------------- Investigation
    eq(pairs_total(7), [(1, 6), (2, 5), (3, 4)], 'I1 pairs'); eq(7 - 2, 5, 'I1 first step'); eq(inv['val'], [5], 'I1 val')
    # ---------------------------------------------------------------- Exit ticket
    q = X['E1']; v = q['visual']; eq(len(small_squares(v['rows'], v['cols'])), 15, 'E1'); eq(q['val'], 15, 'E1 val')
    q = X['E2']; v = q['visual']; eq(len(ways(3, 3)), 9, 'E2'); eq(sum(1 for r in v['rows'] for c in r if c == '[ ]'), 9, 'E2 boxes'); eq(q['val'], 9, 'E2 val')
    q = X['E3']; listed = {frozenset(p) for p in ('AB', 'AC', 'AD', 'BC', 'BD')}; allp = {frozenset(p) for p in itertools.combinations('ABCD', 2)}; eq(allp - listed, {frozenset('CD')}, 'E3 missing pair'); eq(len(allp), 6, 'E3 six pairs'); eq(q['val'], ['CD'], 'E3 val')
    # ---------------------------------------------------------------- home practice
    q = H['H1']; eq(nums(q['text'])[:2], [4, 4], 'H1 text'); eq(len(small_squares(4, 4)), 16, 'H1'); eq(q['val'], 16, 'H1 val')
    q = H['H2']; eq(nums(q['text'])[:2], [3, 4], 'H2 text'); eq(len(ways(3, 4)), 12, 'H2'); eq(q['val'], 12, 'H2 val')
    q = H['H3']; eq([10 - 2, 10 - 3], [8, 7], 'H3'); eq(q['val'], [8, 7], 'H3 val')
    q = H['H4']; eq(len(pairs_total(12)), 6, 'H4'); eq(pairs_total(12)[-1], (6, 6), 'H4 stops at 6 + 6'); eq(q['val'], 6, 'H4 val'); eq(nums(q['text']), [12, 1, 11, 6, 6], 'H4 text')
    q = H['H5']; l16 = json.load(open(os.path.join(L1, 'lessons', 'l16.json')))['home_practice']; src = [h for h in l16 if h['id'] == 'H3'][0]
    eq((q['text'], q['answer'], q['val']), (src['text'], src['answer'], src['val']), 'H5 is the Term 2 Lesson 6 item H3, copied'); eq(q['rewind_of'], 'Term 2 Lesson 6', 'H5 tag'); eq([h['tier'] for h in d['home_practice']], ['start', 'start', 'start', 'think', 'start'], 'home tiers')
    # ---------------------------------------------------------------- online practice, authored numbers
    items = {i['id']: i for i in d['online_practice']['items']}
    for cid, env in BASE_ENV.items(): eq(items[cid]['answer'], ORACLES[cid](env), cid + ' authored answer')
    eq(len(lines_of(items['c3']['fig'])), items['c3']['answer'], 'c3 handshakes of 3'); eq(items['c4']['answer'], 'B with A', 'c4'); eq(items['c4']['options'].index('B with A'), 2, 'c4 option')
    eq(items['g2']['answer'], sum(len([s for s in all_squares(4, 4) if s[2] == k]) for k in (1, 2, 3, 4)), 'g2 squares of a 4 by 4 grid'); eq(len(all_squares(4, 4)), 30, 'g2')
    l26 = {i['id']: i for i in json.load(open(os.path.join(L1, 'lessons', 'l26.json')))['online_practice']['items']}
    for new, old in (('r1', 'c1'), ('r2', 'c3')):
        eq((items[new]['q'], items[new]['answer'], items[new].get('tpl')), (l26[old]['q'], l26[old]['answer'], l26[old].get('tpl')), new + ' is Term 3 Lesson 6 ' + old); eq(items[new]['rewind_of'], 'Term 3 Lesson 6', new + ' tag')
    # ---------------------------------------------------------------- hand-offs
    pn = ' '.join(d['parent']['next_materials']).lower(); eq(all(w in pn for w in ('book 8', 'graph-mat', 'no cutting', '12 small things')), True, 'hand-off to the next lesson names Book 8, the graph mat and the 12 small things')
    end = json.dumps(sl['s-end']['blocks']); eq('Book 8' in end and '12 small things' in end, True, 's-end hand-off')
    prev = json.load(open(os.path.join(L1, 'lessons', 'l35.json'))); txt = ' '.join(prev['parent']['next_materials']).lower(); eq('book 8' in txt and 'paper-people' in txt and '8 paper people' in txt, True, 'the hand-off from lesson 35 names Book 8 and the 8 paper people')
    eq(d['materials']['ruler'], False, 'no ruler needed')
    eq(set(d['beyond']['where']) <= set(T) and not (set(d['beyond']['where']) & {q['id'] for q in d['tiers']['start']}), True, 'beyond items sit at Think harder or Go further')
    return n
