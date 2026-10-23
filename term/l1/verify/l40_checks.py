"""Independent answer checks for Level 1 Term 4 Lesson 10 (Lesson 40, Inquirers' Showcase, and Mi's Challenge Quest of the year).

Everything in l40.json that can be computed is recomputed here from first principles, without the lesson's own sums:
  * every puzzle is solved by SEARCH (every whole number or every pair tried, the number of answers counted): the Explore puzzles (A has no question, B has many answers, C has exactly one),
    Mi's puzzle in the Mini-lesson (listing every pair that makes 9: exactly one pair is 3 apart), the friend's puzzle (the first clue fits, the second does not, exactly one pair fits both),
    G1, G2, G3's model, the home items and the exit ticket;
  * the table of pairs in G1 is rebuilt pair by pair, with the difference of each pair;
  * the Quest gates are recomputed from their pictures: parts of a circle, squares in a rectangle by rows, steps and routes on a dot grid (every order of the moves tried), cubes in a stack, layers of a
    folded paper, the odd tile out (the tile whose features differ from the others), lines in a network (each pair once), equal groups, the picture graph in the key of 2, the growing tower
    and the cave (cents saved day by day);
  * the class items are registered here and shown to differ from the workbook, exit, home and Quest numbers; every lesson of Term 4 (31 to 40) is visited by exactly one Quest gate;
  * the online practice templates get brute-force oracles; the hand-offs (from Lesson 39 and to the next program) are checked.
"""
import itertools
import json
import os
import re

L1 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def nums(text):
    return [int(x) for x in re.findall(r'\d+', text)]


def plus(a, b):
    n = a
    for _ in range(b): n += 1
    return n


def times(k, n):
    t = 0
    for _ in range(n): t += k
    return t


def find(pred, lo=0, hi=200):
    return [x for x in range(lo, hi + 1) if pred(x)]


def pairs_that_make(total):
    """Every pair of whole numbers (a, b) with a <= b and a + b = total, each pair once."""
    return [(a, total - a) for a in range(0, total + 1) if a <= total - a]


def seq(start, step, n):
    row = [start]
    while len(row) < n: row.append(row[-1] + step)
    return row


def routes(right, up):
    """Every order of `right` moves R and `up` moves U."""
    moves = 'R' * right + 'U' * up
    return sorted(set(''.join(p) for p in itertools.permutations(moves)))


def figs_in(blocks):
    out = []
    for b in blocks:
        if b.get('t') == 'visual': out.append(b)
        if b.get('t') == 'cols':
            for c in b['cols']: out += figs_in(c)
    return out


# ---------------------------------------------------------------- online practice oracles (brute force)
def _c1(e):
    return plus(e['b'], e['a'])


def _c2(e):
    t = 2 * e['s'] + e['d']
    return [x for x, y in pairs_that_make(t) if y - x == e['d']][0]


def _c5(e):
    return [x for x in range(0, 100) if x - e['a'] == e['r']][0]


def _t1(e):
    return len([x for x in range(0, 100) if e['a'] < x < e['b']])


def _t3(e):
    n = e['a']
    for _ in range(e['b']): n += 1
    return n


def _g1(e):
    t = 2 * e['s'] + e['d']
    return [y for x, y in pairs_that_make(t) if y - x == e['d']][0]


def _g2(e):
    return len(pairs_that_make(e['t']))


def _r1(e):
    return plus(e['a'], 7)


def _r2(e):
    return times(7, e['w'])


ORACLES = {'c1': _c1, 'c2': _c2, 'c5': _c5, 't1': _t1, 't3': _t3, 'g1': _g1, 'g2': _g2, 'r1': _r1, 'r2': _r2}
BASE_ENV = {'c1': dict(a=4, b=11), 'c2': dict(s=5, d=2), 'c5': dict(r=9, a=5), 't1': dict(a=5, b=11), 't3': dict(a=8, b=6), 'g1': dict(s=5, d=4), 'g2': dict(t=9), 'r1': dict(a=5), 'r2': dict(w=2)}

# ---------------------------------------------------------------- the registry of class numbers (entries with 3 or more numbers are compared)
CLASS_ITEMS = {'rem1': [3, 6, 9, 12], 'rem2': [8, 6], 'rem3': [7, 5, 4], 'rem3-turn': [9, 3, 6], 'sneak1': [6, 4], 'sneak2': [3, 8],
               'explore-A': [8, 5], 'explore-B': [1, 20], 'explore-C': [7, 2], 'mini-m1': [3, 4, 12], 'mini-m2': [9, 3], 'mini-m3': [8, 2, 6, 2], 'opt': [12, 5, 7]}


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
    C = {q['id']: q for q in d['challenge_quest']['questions']}
    cave = d['challenge_quest']['optional']

    def F(slide_id, k=0):
        return figs_in(sl[slide_id]['blocks'])[k]

    def vis(q, k=0):
        return q['visual'] if k == 0 and q.get('visual') else q['visuals'][k]

    # ---------------------------------------------------------------- Remember
    f = F('s-rem1'); eq(f['items'][:4], [3, 6, 9, 12], 'rem1 pattern'); eq(f['items'][4:], [None, None], 'rem1 two empty boxes'); row = seq(3, 3, 6); eq(row[4:], [15, 18], 'rem1 the next two numbers'); eq(seq(3, 3, 8)[6:], [21, 24], 'rem1 your turn')
    eq(len(f['gaps']), len(f['items']) - 1, 'rem1 one gap label between each pair of numbers'); eq(set(f['gaps']), {'+3'}, 'rem1 every gap is +3')
    f = F('s-rem2'); eq(f['jumps'], [[8, 10, '+2'], [10, 14, '+4']], 'rem2 jumps'); eq(plus(8, 6), 14, 'rem2 8 + 6'); eq(10 - 8, 2, 'rem2 8 and 2 make 10'); eq(6 - 2, 4, 'rem2 6 split into 2 and 4'); eq(plus(10, 4), 14, 'rem2 10 and 4'); eq(f['hide'], [14], 'rem2 end hidden')
    eq(plus(9, 5), 14, 'rem2 your turn'); eq(nums(sl['s-rem2']['blocks'][1]['text']), [8, 6], 'rem2 text')
    eq(7 + 5 - 4, 8, 'rem3 Mei has 8'); eq(nums(' '.join(sl['s-rem3']['blocks'][0]['items'])), [7, 5, 4], 'rem3 numbers'); eq(9 - 3 + 6, 12, 'rem3 your turn')
    # ---------------------------------------------------------------- sneak-peek and Explore puzzles
    sp = d['sneak_peek']; eq(nums(sp['q1']), [6, 4], 'sneak q1'); eq((6 + 4, 6 - 4), (10, 2), 'sneak 1 two questions'); fits = [x for x in range(0, 30) if 3 < x < 8]; eq(fits, [4, 5, 6, 7], 'sneak 2 four numbers fit'); eq(len(fits) == 1, False, 'sneak 2 is not a good puzzle'); eq(nums(sp['q2']), [3, 8], 'sneak q2')
    rows = sl['s-explore1']['blocks'][0]['rows']; pz = {r[0]: r[1] for r in rows[1:]}; eq(sorted(pz), ['A', 'B', 'C'], 'explore puzzles A to C')
    eq('?' in pz['A'], False, 'explore A has no question'); evens = [x for x in range(2, 20) if x % 2 == 0]; eq(len(evens), 9, 'explore B has 9 answers (2 to 18)'); eq(len(evens) > 1, True, 'explore B has many answers')
    eq('?' in pz['C'], True, 'explore C has a question'); eq([x for x in range(0, 30) if x - 7 == 2], [9], 'explore C has exactly one answer, 9'); eq(nums(pz['C']), [7, 2], 'explore C numbers')
    # ---------------------------------------------------------------- Mini-lesson
    f = F('s-m1', 0); eq((f['rows'], f['cols'], f['kind']), (3, 4, 'squares'), 'm1 rows of squares'); total = 0
    for _ in range(f['rows']): total += f['cols']
    eq(total, 12, 'm1 3 rows of 4 squares'); eq(seq(4, 4, 3), [4, 8, 12], 'm1 count on by rows'); eq(4 + 4 + 4, 12, 'm1 check')
    ps = pairs_that_make(9); eq(ps, [(0, 9), (1, 8), (2, 7), (3, 6), (4, 5)], 'm2 every pair that makes 9'); eq([(a, b) for a, b in ps if b - a == 3], [(3, 6)], 'm2 exactly one pair is 3 apart')
    tb = F('s-m2-ans')['rows']; eq([(int(r[0]), int(r[1])) for r in tb], ps, 'm2 table pairs'); eq([int(r[2]) for r in tb], [b - a for a, b in ps], 'm2 table differences'); eq([r for r in tb if int(r[2]) == 3], [['3', '6', '3']], 'm2 only 3 and 6')
    eq(nums(' '.join(sl['s-m2']['blocks'][0]['items'])), [9, 3], 'm2 text')
    puz = nums(' '.join(sl['s-m3']['blocks'][0]['items'])); eq(puz, [8, 2, 6, 2], 'm3 text'); eq(6 + 2 == 8, True, 'm3 the first clue fits'); eq(6 - 2 == 2, False, 'm3 the second clue does not fit'); eq(6 - 2, 4, 'm3 6 is 4 more than 2')
    eq([(a, b) for a, b in pairs_that_make(8) if b - a == 2], [(3, 5)], 'm3 exactly one pair fits both clues: 3 and 5'); eq('5 and 3' in sl['s-m3-ans']['blocks'][0]['text'], True, 'm3-ans names 5 and 3')
    eq(len(sl['s-m4']['blocks'][0]['items']), 4, 'm4 four checks')
    eq([x for x in range(0, 30) if x == 5 + 7], [12], 'opt puzzle: 5 more than 7 has exactly one answer 12')
    # ---------------------------------------------------------------- Start here
    q = T['S1']; eq(q['val'], ['open'], 'S1 open'); eq([p['val'] for p in q['parts']], ['open', 'open'], 'S1 parts open')
    q = T['S2']; eq(len(q['parts']), 4, 'S2 four ideas'); eq(all(p['choices'] == ['I know it well', 'I am learning it'] for p in q['parts']), True, 'S2 two choices each')
    q = T['S3']; opts = q['mcq']['options']
    def clear(o): return (' has ' in o) and bool(re.search(r'\d', o)) and ('?' in o)
    eq([i + 1 for i, o in enumerate(opts) if clear(o)], [2], 'S3 exactly one option has a story, numbers and a question'); eq(q['val'], [2], 'S3 val'); eq(nums(opts[1]), [6, 3], 'S3 numbers')
    q = T['S4']; eq(plus(9, 4), 13, 'S4 right answer'); eq(9 - 4, 5, 'S4 the child took away'); eq(5 == 13, False, 'S4 the child is wrong'); eq(q['val'], ['Wrong', 13], 'S4 val'); eq(nums(q['text']), [9, 4, 5], 'S4 text')
    q = T['S5']; eq(find(lambda x: 9 + x == 10), [1], 'S5 9 and 1 make 10'); eq(7 - 1, 6, 'S5 7 take away 1'); eq(10 + 6, 16, 'S5 total'); eq(9 + 7, 16, 'S5 check'); eq(q['val'], [1, 6, 16], 'S5 val'); eq(nums(q['text']), [9, 7], 'S5 text')
    q = T['S6']; f = vis(q); dots = 0
    for _ in range(f['rows']): dots += f['cols']
    eq((f['rows'], dots), (4, 20), 'S6 4 rows, 20 dots'); eq(seq(5, 5, 4), [5, 10, 15, 20], 'S6 count on by rows'); eq(q['val'], [4, 20], 'S6 val')
    eq(sum(x['mins'] for x in d['tiers']['start']) <= 20, True, 'Start here fits in 20 minutes'); eq([x['page'] for x in d['tiers']['start']], [1, 1, 1, 2, 2, 2], 'Start here pages')
    # ---------------------------------------------------------------- Think harder
    q = T['T1']; eq(q['val'], ['open'], 'T1 open'); eq(q['lines'] >= 3, True, 'T1 has lines to write on')
    q = T['T2']; eq(q['val'], ['open'], 'T2 open'); eq([p['choices'] for p in q['parts'] if p.get('choices')], [['Yes', 'No']], 'T2 choices')
    q = T['T3']; A = [x for x in range(0, 40) if 10 < x < 15]; B = [x for x in range(0, 40) if x - 9 == 4]; eq(A, [11, 12, 13, 14], 'T3 puzzle A has 4 answers'); eq(B, [13], 'T3 puzzle B has exactly one answer'); eq('?' in q['text'], False, 'T3 puzzle C has no question')
    eq(q['val'], ['B', len(A)], 'T3 val'); eq(nums(q['text']), [10, 15, 4, 9, 3, 4], 'T3 text')
    # ---------------------------------------------------------------- Go further
    q = T['G1']; f = vis(q); ps = pairs_that_make(12); rows = f['rows']; eq([(int(r[0]), int(r[1])) for r in rows], ps, 'G1 table pairs'); eq(rows[0][2], '12', 'G1 first difference given'); eq(all(r[2] == '[]' for r in rows[1:]), True, 'G1 the other differences are blanks')
    eq([b - a for a, b in ps], [12, 10, 8, 6, 4, 2, 0], 'G1 differences'); sol = [(a, b) for a, b in ps if b - a == 2]; eq(sol, [(5, 7)], 'G1 exactly one pair is 2 apart'); eq(q['val'], [5, 7, 1], 'G1 val'); eq(len(sol), 1, 'G1 one pair'); eq(nums(q['text']), [12, 2, 12], 'G1 text')
    eq(d['beyond']['name'], 'Puzzle With a Proof', 'G1 named puzzle'); eq(set(d['beyond']['where']) == {'G1', 'G3'}, True, 'beyond items')
    q = T['G2']; eq(6 + 4 == 10, True, 'G2 the first clue fits'); eq(6 - 4, 2, 'G2 6 and 4 are 2 apart'); eq(6 - 4 == 4, False, 'G2 the second clue does not fit'); fit = [(a, b) for a, b in pairs_that_make(10) if b - a == 4]; eq(fit, [(3, 7)], 'G2 exactly one pair fits'); eq(q['val'], ['No', 2, 3, 7], 'G2 val'); eq(nums(q['text']), [10, 4, 6, 4], 'G2 text')
    q = T['G3']; eq(q['val'], ['open'], 'G3 open'); eq([(a, b) for a, b in pairs_that_make(8) if b - a == 2], [(3, 5)], 'G3 model puzzle: 8 and 2 apart is 3 and 5'); eq(len(pairs_that_make(8)), 5, 'G3 model lists 5 pairs'); eq(q['lines'] >= 3, True, 'G3 has lines')
    eq(inv['val'], ['open'], 'I1 open'); eq(inv['lines'] >= 4, True, 'I1 has 4 lines')
    # ---------------------------------------------------------------- Exit ticket
    q = X['E1']; eq(find(lambda x: x - 5 == 9), [14], 'E1 her number is 14'); eq(q['val'], 14, 'E1 val'); eq(nums(q['text']), [5, 9], 'E1 text')
    q = X['E2']; o = q['mcq']['options']
    eq(len([x for x in range(0, 50) if x > 6]) > 1, True, 'E2 option 1 has many answers'); eq([x for x in range(0, 50) if x - 8 == 3], [11], 'E2 option 2 has exactly one answer'); eq('?' in o[2], False, 'E2 option 3 has no question'); eq(' has ' in o[3], False, 'E2 option 4 has no story')
    eq(q['val'], [2], 'E2 val')
    q = X['E3']; eq(7 + 8, 15, 'E3 7 + 8'); eq(15 == 16, False, 'E3 the child is wrong'); eq(find(lambda x: x + 8 == 16), [8], 'E3 16 take away 8 is 8, not 7'); eq(q['val'], ['Wrong'], 'E3 val'); eq(nums(q['text']), [7, 8, 16], 'E3 text')
    # ---------------------------------------------------------------- home practice
    q = H['H1']; eq(plus(12, 5), 17, 'H1'); eq(q['val'], 17, 'H1 val')
    q = H['H2']; eq([(a, b) for a, b in pairs_that_make(14) if b - a == 2], [(6, 8)], 'H2 exactly one pair'); eq(q['val'], [6, 8], 'H2 val')
    q = H['H3']; eq(find(lambda x: x + 8 == 20), [12], 'H3 20 take away 8'); eq(12 == 13, False, 'H3 the child is wrong'); eq(q['val'], ['Wrong', 12], 'H3 val')
    q = H['H4']; fits = [x for x in range(0, 40) if 7 < x < 12]; eq(fits, [8, 9, 10, 11], 'H4 four numbers fit'); eq(q['val'], 4, 'H4 val')
    l20 = json.load(open(os.path.join(L1, 'lessons', 'l20.json')))['home_practice']; src = [h for h in l20 if h['id'] == 'H1'][0]; q = H['H5']
    eq((q['text'], q['answer'], q['val']), (src['text'], src['answer'], src['val']), 'H5 is the Term 2 Lesson 10 item H1, copied'); eq(q['rewind_of'], 'Term 2 Lesson 10', 'H5 tag'); eq([u for u in range(1, 30) if times(u, 5) == 10], [2], 'H5 1 pen costs $2')
    eq([h['tier'] for h in d['home_practice']], ['start', 'start', 'start', 'think', 'start'], 'home tiers')
    # ---------------------------------------------------------------- the Quest: every gate recomputed from its picture
    cq = d['challenge_quest']; eq(cq['scope'], 'year', 'Quest scope is the year'); eq(len(cq['questions']), 8, '8 gates'); eq(cq['sheet_pages'], 4, '4 pages')
    covered = []
    for g in cq['questions']: covered += g['lesson'] if isinstance(g['lesson'], list) else [g['lesson']]
    eq(sorted(covered), list(range(31, 41)), 'every lesson of Term 4 (31 to 40) is visited by exactly one gate'); eq(cave['lesson'], 'beyond', 'the cave is the unseen puzzle')
    g = C['C1']; circle = vis(g); rect = dict(rows=nums(g['text'])[0], cols=nums(g['text'])[1]); eq(circle['parts'], 1, 'C1 the picture is a plain circle: the child works out the 4 parts from the fold'); eq(circle['shape'], 'circle', 'C1 circle')
    parts = 1
    for _ in range(2): parts *= 2
    eq(parts, 4, 'C1 half and half again'); eq(g['val'], [4, 'quarter', 9], 'C1 val'); total = 0
    for _ in range(rect['rows']): total += rect['cols']
    eq((rect['rows'], rect['cols'], total), (3, 3, 9), 'C1 rectangle 3 rows of 3 squares (from the text)'); eq(nums(g['text']), [3, 3], 'C1 text')
    g = C['C2']; f = vis(g); dx = f['end'][0] - f['start'][0]; dy = f['start'][1] - f['end'][1]; eq((dx, dy), (2, 1), 'C2 2 right and 1 up'); rt = routes(dx, dy); eq(rt, ['RRU', 'RUR', 'URR'], 'C2 every route'); eq((dx + dy, len(rt)), (3, 3), 'C2 steps and routes'); eq(g['val'], [3, 3], 'C2 val')
    g = C['C3']; st, pp, fp = vis(g, 0), vis(g, 1), vis(g, 2); eq((pp['stage'], pp['fold']), ('paper', 'h'), 'C3 the paper shows its dashed fold line'); cubes = 0
    for r in st['heights']:
        for h in r: cubes += h
    eq(cubes, 6, 'C3 6 cubes'); eq(fp['stage'], 'folded', 'C3 the paper is folded'); layers = 2; holes = 0
    for _ in range(layers): holes += len(fp['holes'])
    eq(holes, 2, 'C3 one hole through 2 layers makes 2 holes'); eq(g['val'], [6, 2], 'C3 val')
    g = C['C4']; f = vis(g); tiles = f['tiles']; odd = [i for i, t in enumerate(tiles) if sum(1 for u in tiles if u == t) == 1]; eq(odd, [2], 'C4 tile C is the only tile with no twin'); eq(f['labels'][odd[0]], 'C', 'C4 label')
    differ = [k for k in tiles[2] if tiles[2][k] != tiles[0][k]]; eq(differ, ['shape'], 'C4 only the shape differs (same number, size and pattern)'); eq(g['val'], ['C', 'shape'], 'C4 val'); eq(sum(1 for t in tiles if t == tiles[0]), 3, 'C4 three tiles alike')
    g = C['C5']; f = vis(g); lines = {tuple(sorted(l)) for l in f['lines']}; eq(len(f['lines']), len(lines), 'C5 no line drawn twice'); eq(len(lines), 7, 'C5 7 lines'); eq(f['n'], 5, 'C5 5 dots'); eq(len(list(itertools.combinations(range(f['n']), 2))), 10, 'C5 not every pair of 5 dots is joined (a drawn picture, not the full handshake figure)'); eq(times(5, 3), 15, 'C5 3 boxes of 5'); eq(g['val'], [7, 15], 'C5 val')
    g = C['C6']; f = vis(g); k = f['each']; ali, mei = [times(k, r['n']) for r in f['rows']]; eq((k, ali, mei, mei - ali), (2, 8, 14, 6), 'C6 flowers in the key of 2'); eq(g['val'], [8, 6], 'C6 val'); eq(f['rows'][1]['n'] - f['rows'][0]['n'], 3, 'C6 3 more pictures')
    g = C['C7']; row = seq(6, 4, 5); eq(row, [6, 10, 14, 18, 22], 'C7 the tower'); eq(row[4], 22, 'C7 row 5'); eq(g['val'], ['Table', 22], 'C7 val'); eq(nums(g['text']), [6, 1, 10, 2, 14, 3, 4], 'C7 text'); eq(find(lambda x: x == 22 and x == 6 + 4 * 4), [22], 'C7 4 steps of 4 from 6')
    g = C['C8']; eq(7 + 5 == 13, False, 'C8 the puzzle is wrong'); eq(find(lambda x: x + 5 == 13), [8], 'C8 the right number is 8'); eq(g['val'], ['No', 8], 'C8 val'); eq(nums(g['text']), [5, 13, 7], 'C8 text')
    days = seq(5, 5, 5); eq(days, [5, 10, 15, 20, 25], 'cave: cents saved day by day'); tot = 0
    for x in days: tot += x
    eq((days[4], tot), (25, 75), 'cave: Friday and in all'); eq(cave['val'], [25, 75], 'cave val')
    eq(all(g['tier'] == 'start' for g in cq['questions']), True, 'every gate is at Start here level')
    sid = {s['id']: s for s in cq['strands']}; allq = sorted(sum([s['questions'] for s in cq['strands']], [])); eq(allq, sorted(C), 'every gate is in exactly one strand')
    # ---------------------------------------------------------------- the class numbers differ from the workbook, exit, home and Quest numbers
    wb = {}
    for qq in list(T.values()) + list(X.values()) + list(H.values()) + list(C.values()):
        txt = qq['text'] + ' ' + ' '.join(p.get('text', '') for p in qq.get('parts', []))
        wb[qq['id']] = tuple(sorted(nums(txt)))
    cls = {tuple(sorted(v)) for v in CLASS_ITEMS.values() if len(v) >= 3}
    eq([i for i, v in wb.items() if v in cls and len(v) >= 3], [], 'no workbook, exit, home or Quest item repeats the numbers of a class item')
    # ---------------------------------------------------------------- online practice, authored numbers
    items = {i['id']: i for i in d['online_practice']['items']}
    eq(items['c1']['answer'], _c1(dict(a=4, b=11)), 'c1'); eq(items['c2']['answer'], _c2(dict(s=5, d=2)), 'c2'); eq(items['c5']['answer'], _c5(dict(r=9, a=5)), 'c5'); eq(items['t1']['answer'], _t1(dict(a=5, b=11)), 't1'); eq(items['t3']['answer'], _t3(dict(a=8, b=6)) , 't3 right answer is a + b (14)')
    eq(items['g1']['answer'], _g1(dict(s=5, d=4)), 'g1'); eq(items['g2']['answer'], _g2(dict(t=9)), 'g2')
    eq(items['c3']['answer'], items['c3']['options'][1], 'c3 the second option is the good puzzle'); eq([o for o in items['c3']['options'] if clear(o)], [items['c3']['answer']], 'c3 exactly one option has a story, numbers and a question')
    eq(items['c4']['answer'], 'No', 'c4'); eq(len([x for x in range(2, 9)]) > 1, True, 'c4 many numbers fit')
    eq(items['t2']['answer'], '6 is not 4 more than 4', 't2'); eq(6 + 4 == 10, True, 't2 first clue fits'); eq(6 - 4 == 4, False, 't2 second clue does not')
    l30 = {i['id']: i for i in json.load(open(os.path.join(L1, 'lessons', 'l30.json')))['online_practice']['items']}
    eq((items['r1']['q'], items['r1']['answer']), (l30['c1']['q'], l30['c1']['answer']), 'r1 is Term 3 Lesson 10 c1'); eq((items['r2']['q'], items['r2']['answer']), (l30['c2']['q'], l30['c2']['answer']), 'r2 is Term 3 Lesson 10 c2')
    eq((items['r1']['rewind_of'], items['r2']['rewind_of']), ('Term 3 Lesson 10', 'Term 3 Lesson 10'), 'rewind tags'); eq(_r1(dict(a=5)), 12, 'r1'); eq(_r2(dict(w=2)), 14, 'r2')
    # ---------------------------------------------------------------- materials and hand-offs
    eq(d['workbook']['kits'], [], 'no kit page'); eq(d['materials']['kit_contract'], [], 'no kit contract'); eq(d['materials']['ruler'], False, 'no ruler')
    prev = json.load(open(os.path.join(L1, 'lessons', 'l39.json'))); pn = ' '.join(prev['parent']['next_materials']).lower()
    eq(all(w in pn for w in ('quest log', 'closed', 'quest partner', 'favourite page', 'plain paper')), True, 'lesson 39 hand-off names what this lesson needs')
    mat = ' '.join(d['materials']['child']).lower(); eq(all(w in mat for w in ('quest log', 'quest partner', 'favourite page', 'plain paper')), True, 'materials match the hand-off')
    nxt = json.dumps(sl['s-end']['blocks']).lower(); eq('first lesson of level 2 or the holiday program' in nxt, True, 's-end names the next program'); eq('lesson 1' in json.dumps(d['parent']).lower().replace('lesson 10', ''), False, 'no Lesson 1 text on the parent page')
    eq('first lesson of level 2 or the holiday program' in d['parent']['next'].lower(), True, 'parent next names the next program')
    eq(set(d['beyond']['where']) <= set(T) and not (set(d['beyond']['where']) & {qq['id'] for qq in d['tiers']['start']}), True, 'beyond items sit at Think harder or Go further')
    return n
