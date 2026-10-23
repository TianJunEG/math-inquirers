"""Independent answer checks for Level 1 Term 4 Lesson 8 (Lesson 38, Graph Detectives).

Everything in l38.json that can be computed is recomputed here from first principles, without the lesson's own sums:
  * a picture graph is read from its rows (label, pictures n, hidden boxes): a row with hidden boxes is an EMPTY row to be drawn, so its number is never read from the picture;
  * a row is turned into THINGS by counting in the key (each picture is 1, 2 or 3 things; a half picture is half the key), never by multiplying;
  * 'how many more' and 'how many fewer' are found by pairing pictures one to one and counting the pictures left without a partner, and then counted in the key;
  * 'the same number', 'fewest', 'most', 'in all' are found by comparing and adding the rows;
  * a missing bar is found by trying every size of the missing row from 0 to the number of empty boxes (exactly one size fits the total), and the empty boxes are checked to be more than needed;
  * the clues of G2 are solved by trying every number of ducks, geese and hens from 0 to 18 and keeping the sets that fit all the clues and the total (exactly one set);
  * the class items are registered here and shown to differ from every workbook, exit and home item. The online practice templates get brute-force oracles.
"""
import json
import os
import re

L1 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# ---------------------------------------------------------------- readers
def nums(text):
    return [int(x) for x in re.findall(r'\d+', text)]


def graph_rows(fig):
    """[(label, pictures n, hidden)]: n is the pictures drawn, or the number of EMPTY boxes when the row is hidden."""
    return [(r['label'], r['n'], len(r.get('hide', [])) > 0) for r in fig['rows']]


def drawn(fig):
    """Pictures drawn in each row (0 for a row whose boxes are all empty)."""
    return {l: (0 if h else n) for l, n, h in graph_rows(fig)}


def things(fig):
    """Things each row stands for: count in the key once for each picture; a half picture is half of the key."""
    k = fig.get('each', 1)
    out = {}
    for l, n in drawn(fig).items():
        t = 0
        whole = int(n)
        for _ in range(whole): t += k
        if n - whole: t += k / 2
        out[l] = int(t) if t == int(t) else t
    return out


def more(a, b):
    """How many more a than b: pair the pictures one to one and count the pictures of a that have no partner."""
    left = 0
    for i in range(a):
        if i >= b: left += 1
    return left


def count_in(k, n):
    """Count in k's n times: k, 2k, ... and return the last number said."""
    t = 0
    for _ in range(n): t += k
    return t


def figs_in(blocks):
    out = []
    for b in blocks:
        if b.get('t') == 'visual': out.append(b)
        if b.get('t') == 'cols':
            for c in b['cols']: out += figs_in(c)
    return out


# ---------------------------------------------------------------- registries
CLASS_GRAPHS = {'s-rem1': ((7, 4, 5), 1), 's-rem3': ((4,), 2), 's-sneak': ((3, 5), 2), 's-explore2-A': ((4,), 1), 's-explore2-B': ((4,), 2), 's-m1': ((2, 6, 4), 2), 's-m2-ans': ((2, 6, 4, 4), 2),
                's-m3-ans': ((7, 4, 5), 1), 's-m4': ((6, 4, 5), 1), 's-opt': ((4,), 3)}
WB_GRAPHS = {'S1': ((6, 9, 4, 6), 1), 'S4': ((8, 5, 3, 5), 1), 'T1': ((7, 5, 6), 1), 'T2': ((3, 4, 5), 2), 'G1': ((3, 2, 3), 3), 'G3': ((9, 6, 4, 5), 1), 'E1': ((5, 8, 3), 1)}


# ---------------------------------------------------------------- online practice oracles (brute force)
def _c1(e):
    return more(e['a'], e['b'])


def _c2(e):
    n = 0
    for row in (e['a'], e['b'], e['c']):
        for _ in range(row): n += 1
    return n


def _c5(e):
    return len([x for x in range(e['t']) if x >= e['a']])


def _t1(e):
    b = e['a'] - e['d']
    t = e['a'] + b + e['c']
    for c in range(0, 40):
        if e['a'] + b + c == t: return c


def _t2(e):
    n = 0
    for i in range(e['n']):
        if i >= e['m']:
            for _ in range(2): n += 1
    return n


def _g1(e):
    return count_in(3, e['n'])


def _r1(e):
    t = 0
    for _ in range(e['k']): t += e['p']
    return t


def _r2(e):
    seq = [e['s']]
    for _ in range(3): seq.append(seq[-1] + e['e'])
    return seq[-1]


ORACLES = {'c1': _c1, 'c2': _c2, 'c5': _c5, 't1': _t1, 't2': _t2, 'g1': _g1, 'r1': _r1, 'r2': _r2}
BASE_ENV = {'c1': dict(a=8, b=3), 'c2': dict(a=2, b=4, c=3), 'c5': dict(t=12, a=5), 't1': dict(a=8, d=3, c=7), 't2': dict(n=7, m=3), 'g1': dict(n=4), 'r1': dict(p=5, k=4), 'r2': dict(s=2, e=3)}


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

    def vis(q, k=0):
        return q['visual'] if k == 0 and q.get('visual') else q['visuals'][k]

    def reg(fig):
        return (tuple(drawn(fig).values()), fig.get('each', 1))

    # ---------------------------------------------------------------- class registry matches the slides and differs from the workbook
    eq(reg(F('s-rem1')), CLASS_GRAPHS['s-rem1'], 's-rem1'); eq(reg(F('s-rem3')), CLASS_GRAPHS['s-rem3'], 's-rem3'); eq(reg(F('s-sneak')), CLASS_GRAPHS['s-sneak'], 's-sneak')
    eq(reg(F('s-explore2', 0)), CLASS_GRAPHS['s-explore2-A'], 's-explore2 graph A'); eq(reg(F('s-explore2', 1)), CLASS_GRAPHS['s-explore2-B'], 's-explore2 graph B'); eq(reg(F('s-explore2-ans', 0)), CLASS_GRAPHS['s-explore2-A'], 's-explore2-ans A'); eq(reg(F('s-explore2-ans', 1)), CLASS_GRAPHS['s-explore2-B'], 's-explore2-ans B')
    eq(reg(F('s-m1')), CLASS_GRAPHS['s-m1'], 's-m1'); eq(reg(F('s-m1-ans')), CLASS_GRAPHS['s-m1'], 's-m1-ans'); eq(reg(F('s-m2-ans')), CLASS_GRAPHS['s-m2-ans'], 's-m2-ans'); eq(reg(F('s-m3-ans')), CLASS_GRAPHS['s-m3-ans'], 's-m3-ans'); eq(reg(F('s-m4')), CLASS_GRAPHS['s-m4'], 's-m4'); eq(reg(F('s-opt')), CLASS_GRAPHS['s-opt'], 's-opt')
    cls = {(tuple(sorted(a)), k) for a, k in CLASS_GRAPHS.values()}
    wb = [(tuple(sorted(a)), k) for a, k in WB_GRAPHS.values()]
    eq([w for w in wb if w in cls], [], 'no workbook or exit graph repeats the numbers and key of a class graph'); eq(len(set(wb)), len(wb), 'the workbook graphs are all different')
    # ---------------------------------------------------------------- warm-up
    g = drawn(F('s-rem1')); eq(max(g, key=g.get), 'Ali', 's-rem1 most'); eq(more(g['Ali'], g['Ben']), 2, 's-rem1 Ali over Ben'); eq(sum(g.values()), 16, 's-rem1 your turn: all the cards')
    f = F('s-rem2', 0); eq((f['start'], f['end'], f['step'], f['hide']), (0, 12, 2, [4, 10]), 's-rem2 line 1'); eq([x for x in range(0, 13, 2) if x in f['hide']], [4, 10], 's-rem2 the missing numbers when counting in 2s')
    f = F('s-rem2', 1); eq((f['start'], f['end'], f['step'], f['hide']), (0, 18, 3, [6, 12]), 's-rem2 line 2'); eq([x for x in range(0, 19, 3) if x in f['hide']], [6, 12], 's-rem2 the missing numbers when counting in 3s'); eq([x for x in range(12, 19, 3)], [12, 15, 18], 's-rem2 your turn counts in 3s from 12 to 18')
    f = F('s-rem3'); eq(f['each'], 2, 's-rem3 key'); eq(things(f)['Shells'], 8, 's-rem3 shells'); eq(count_in(2, 3), 6, 's-rem3 your turn')
    # ---------------------------------------------------------------- sneak-peek
    sp = d['sneak_peek']; f = F('s-sneak'); g = drawn(f); eq(g['Ravi'], 3, 'sneak 1 pictures'); eq(things(f)['Ravi'], 6, 'sneak 2 stickers'); eq(sp['a1'], '3 pictures.', 'sneak a1'); eq(sp['a2'].startswith('6 stickers'), True, 'sneak a2'); eq(nums(sp['q2']), [2], 'sneak q2 key')
    # ---------------------------------------------------------------- Explore
    dots = 8; loops = len([i for i in range(0, dots, 2)]); eq(loops, 4, 'explore 8 dots in pairs'); dots = 12; eq(len([i for i in range(0, dots, 2)]), 6, 'explore 12 dots in pairs')
    eq('8 dots make 4 pictures. 12 dots make 6 pictures.' in sl['s-explore1-ans']['blocks'][0]['text'], True, 's-explore1-ans text')
    a, b = F('s-explore2', 0), F('s-explore2', 1); ta, tb = things(a)['Pens'], things(b)['Rulers']; eq((ta, tb), (4, 8), 'explore 2: graph A shows 4 and graph B shows 8'); eq(tb > ta, True, 'explore 2: graph B shows more'); eq(drawn(a)['Pens'], drawn(b)['Rulers'], 'explore 2: both rows have the same number of pictures')
    # ---------------------------------------------------------------- Mini-lesson
    f = F('s-m1'); t = things(f); eq(f['each'], 2, 'm1 key'); eq(t['Ali'], 12, 'm1 Ali'); eq(t['Ali'] - t['Mei'], 8, 'm1 how many more apples'); eq(more(drawn(f)['Ali'], drawn(f)['Mei']), 4, 'm1 pictures more'); eq(count_in(2, more(drawn(f)['Ali'], drawn(f)['Mei'])), 8, 'm1 4 more pictures of 2')
    f = F('s-m2'); rr = graph_rows(f); eq([(l, h) for l, _, h in rr], [('Mei', False), ('Ali', False), ('Siti', False), ('Ben', True)], 'm2 rows'); pics = [p for p in range(0, 7) if count_in(2, p) == 8]; eq(pics, [4], 'm2 Ben needs 4 pictures'); eq(rr[3][1] > pics[0], True, 'm2 boxes are more than needed')
    eq(drawn(F('s-m2-ans'))['Ben'], 4, 'm2-ans Ben')
    f = F('s-m3'); rr = graph_rows(f); eq([(l, h) for l, _, h in rr], [('Cups', False), ('Plates', True), ('Bowls', True)], 'm3 rows'); cups = rr[0][1]; sols = []
    for plates in range(0, 10):
        for bowls in range(0, 10):
            if plates == cups - 3 and cups + plates + bowls == 16: sols.append((plates, bowls))
    eq(sols, [(4, 5)], 'm3 exactly 4 plates and 5 bowls'); eq(rr[1][1] > 4 and rr[2][1] > 5, True, 'm3 boxes are more than needed'); eq(nums(sl['s-m3']['blocks'][-1]['text']), [1, 16, 3], 'm3 text'); g = drawn(F('s-m3-ans')); eq((g['Cups'], g['Plates'], g['Bowls']), (7, 4, 5), 'm3-ans')
    f = F('s-m4'); g = drawn(f); eq(g['Gold'], 5, 'm4 question 1'); eq(more(g['Red'], g['Blue']), 2, 'm4 question 3'); eq('Question 2' in sl['s-m4-ans']['blocks'][0]['text'], True, 'm4 answer is question 2'); eq(len(sl['s-m4']['blocks'][1]['items']), 3, 'm4 three questions')
    # ---------------------------------------------------------------- Talk and optional slide
    eq(nums(d['talk']['question']), [21, 6, 9, 8], 'talk numbers'); eq(21 - (6 + 9), 6, 'talk the third bar is 6'); eq(6 + 9 + 8, 23, 'talk the child is wrong'); eq(23 == 21, False, 'talk 23 is not 21'); eq(d['talk']['answer'].startswith('No.'), True, 'talk answer')
    f = F('s-opt'); eq((f['each'], things(f)['Stamps']), (3, 12), 's-opt 4 pictures of 3')
    # ---------------------------------------------------------------- Start here
    q = T['S1']; f = vis(q); g = drawn(f); eq(reg(f), WB_GRAPHS['S1'], 'S1 registry'); eq(max(g, key=g.get), 'Mei', 'S1 most'); same = [k for k in g if k != 'Ali' and g[k] == g['Ali']]; eq(same, ['Siti'], 'S1 the same number as Ali'); eq(q['val'], ['Mei', 'Siti'], 'S1 val'); eq(len(f['rows']), 4, 'S1 four rows'); eq(nums(q['text']), [1, 1, 2, 3], 'S1 key is 1 (S1, S2 and S3 named)')
    q = T['S2']; eq(q['val'], [more(g['Mei'], g['Ben']), sum(g.values())], 'S2 val'); eq((more(g['Mei'], g['Ben']), sum(g.values())), (5, 25), 'S2 values'); eq(q.get('visual'), None, 'S2 uses the graph of S1'); eq('in S1' in q['text'], True, 'S2 points to S1')
    q = T['S3']; st = [min(g, key=g.get) == 'Ben', more(g['Mei'], g['Ali']) == 3, g['Ali'] > g['Siti'], sum(g.values()) == 24]; eq(['True' if x else 'False' for x in st], q['val'], 'S3 true or false'); eq(q['val'], ['True', 'True', 'False', 'False'], 'S3 val'); eq(len(q['tf']), 4, 'S3 four statements'); eq(q['tf'][3]['s'], 'The children read 24 books in all.', 'S3 statement 4')
    q = T['S4']; f = vis(q); g4 = drawn(f); eq(reg(f), WB_GRAPHS['S4'], 'S4 registry'); eq(len(f['rows']), 4, 'S4 kinds'); eq([k for k in g4 if k != 'Pears' and g4[k] == g4['Pears']], ['Oranges'], 'S4 the same as pears'); eq(q['val'], [4, 'Oranges'], 'S4 val'); eq(q['parts'][1]['choices'], ['Apples', 'Plums', 'Oranges'], 'S4 choices')
    q = T['S5']; eq(more(g4['Pears'], g4['Plums']), 2, 'S5 fewer plums than pears'); eq(g4['Apples'] + g4['Plums'], 11, 'S5 apples and plums'); eq(q['val'], [2, 11], 'S5 val')
    q = T['S6']; eq(sum(g4.values()), 21, 'S6 total'); eq(max(g4, key=g4.get), 'Apples', 'S6 most'); eq(q['val'], [21, 'Apples'], 'S6 val'); eq(q['parts'][1]['choices'], ['Apples', 'Pears', 'Plums', 'Oranges'], 'S6 choices')
    eq(sum(x['mins'] for x in d['tiers']['start']) <= 20, True, 'Start here fits in 20 minutes'); eq([x['page'] for x in d['tiers']['start']], [1, 1, 1, 2, 2, 2], 'Start here pages'); eq(all(fig.get('each', 1) == 1 for fig in (vis(T['S1']), vis(T['S4']))), True, 'Start here graphs have a key of 1')
    # ---------------------------------------------------------------- Think harder
    q = T['T1']; f = vis(q); rr = graph_rows(f); eq([(l, h) for l, _, h in rr], [('Red', False), ('Blue', True), ('Gold', True)], 'T1 rows'); red = rr[0][1]; sols = []
    for blue in range(0, 9):
        for gold in range(0, 9):
            if blue == red - 2 and red + blue + gold == 18: sols.append((blue, gold))
    eq(sols, [(5, 6)], 'T1 exactly 5 blue and 6 gold'); eq(rr[1][1] > 5 and rr[2][1] > 6, True, 'T1 boxes are more than needed'); eq(q['val'], [5, 6], 'T1 val'); eq(nums(q['text']), [18, 2], 'T1 text')
    q = T['T2']; f = vis(q); eq(f['each'], 2, 'T2 key'); g = drawn(f); eq(reg(f), WB_GRAPHS['T2'], 'T2 registry'); t = things(f); eq(t['Pearl'], 6, 'T2 Pearl'); eq(t['Reef'] - t['Pearl'], 4, 'T2 how many more'); eq(count_in(2, more(g['Reef'], g['Pearl'])), 4, 'T2 2 more pictures of 2'); eq(q['val'], [6, 4], 'T2 val')
    q = T['T3']; eq(t['Coral'], 8, 'T3 Coral has 8 shells'); eq(g['Coral'], 4, 'T3 the child counted 4 pictures'); eq(t['Coral'] != g['Coral'], True, 'T3 the child is wrong'); eq(q['val'], ['No', 8], 'T3 val'); eq(nums(q['text']), [2, 4], 'T3 text: question T2 and the 4 shells she says'); eq('question T2' in q['text'], True, 'T3 points to T2'); eq(nums(q['parts'][1]['text']), [], 'T3 part b')
    # ---------------------------------------------------------------- Go further
    q = T['G1']; f = vis(q); rr = graph_rows(f); k = f['each']; eq(k, 3, 'G1 key is 3'); mei = count_in(k, rr[0][1]); ravi = count_in(k, rr[1][1]); eq((mei, ravi, mei + ravi), (9, 6, 15), 'G1 Mei and Ravi'); lily = [p for p in range(0, 7) if mei + ravi + count_in(k, p) == 24]; eq(lily, [3], 'G1 exactly 3 pictures for Lily'); eq(rr[2][1] > lily[0], True, 'G1 boxes are more than needed'); eq(rr[2][2], True, 'G1 Lily is empty')
    eq(q['val'], [15, 3], 'G1 val'); eq(nums(q['text']), [3, 24], 'G1 text'); eq(WB_GRAPHS['G1'], ((3, 2, 3), 3), 'G1 registry: Mei 3 pictures, Ravi 2, Lily 3'); eq(24 // 3, 8, 'G1 8 pictures in all'); eq(d['beyond']['name'], 'Missing Bar', 'G1 named puzzle'); eq('G1' in d['beyond']['where'], True, 'G1 is a beyond item')
    q = T['G2']; sols = []
    for duck in range(0, 19):
        for goose in range(0, 19):
            for hen in range(0, 19):
                if duck == goose and hen == duck + 3 and duck + goose + hen == 18: sols.append((duck, goose, hen))
    eq(sols, [(5, 5, 8)], 'G2 exactly one set fits every clue'); eq(q['val'], [5, 8], 'G2 val'); eq(nums(q['text']), [18, 3], 'G2 text')
    q = T['G3']; f = vis(q); g = drawn(f); eq(reg(f), WB_GRAPHS['G3'], 'G3 registry'); eq(sum(g.values()), 24, 'G3 total'); eq(g['Story'], 9, 'G3 option 1'); eq(more(g['Story'], g['Art']), 5, 'G3 option 3'); can = [True, False, True, True]; eq(q['val'], [can.index(False) + 1], 'G3 only option 2 cannot be answered')
    eq(len(q['mcq']['options']), 4, 'G3 four options'); eq('best' in q['mcq']['options'][1], True, 'G3 option 2 is about which is best'); eq(all(w in q['solution'] for w in ('9 story', '5 more', '24 books')), True, 'G3 solution matches the graph')
    # ---------------------------------------------------------------- Investigation
    eq(inv['val'], ['open'], 'I1 open'); eq(inv.get('draw'), 0, 'I1 draws on paper'); eq(nums(inv['first']), [3], 'I1 numbers')
    # ---------------------------------------------------------------- Exit ticket
    q = X['E1']; f = vis(q); g = drawn(f); eq(reg(f), WB_GRAPHS['E1'], 'E1 registry'); eq(min(g, key=g.get), 'Siti', 'E1 fewest'); eq(q['val'], ['Siti'], 'E1 val'); eq(q['parts'][0]['choices'], ['Ali', 'Mei', 'Siti'], 'E1 choices')
    q = X['E2']; eq(sum(g.values()), 16, 'E2 total'); eq(q['val'], 16, 'E2 val'); eq(q.get('visual'), None, 'E2 uses the graph of E1')
    q = X['E3']; eq(more(g['Mei'], g['Ali']), 3, 'E3 Mei has 3 more than Ali, true'); eq(q['val'], ['True'], 'E3 val'); eq(nums(q['text']), [1, 3], 'E3 text')
    eq(all(x.get('each', 1) == 1 for x in (f,)), True, 'exit graph has a key of 1 (nothing beyond Primary 1 in the exit ticket)')
    # ---------------------------------------------------------------- home practice
    q = H['H1']; eq(nums(q['text'])[:3], [1, 8, 5], 'H1 text'); eq(8 + 5, 13, 'H1'); eq(q['val'], 13, 'H1 val')
    q = H['H2']; eq(nums(q['text'])[:3], [1, 9, 4], 'H2 text'); eq(9 - 4, 5, 'H2'); eq(more(9, 5), 4, 'H2 check: 4 more'); eq(q['val'], 5, 'H2 val')
    q = H['H3']; eq(nums(q['text'])[:3], [12, 7, 3], 'H3 text'); sols = [c for c in range(0, 13) if 7 + 3 + c == 12]; eq(sols, [2], 'H3'); eq(q['val'], 2, 'H3 val')
    q = H['H4']; eq(nums(q['text'])[:3], [20, 8, 3], 'H4 text'); sols = [(dog, fish) for dog in range(0, 21) for fish in range(0, 21) if dog == 8 - 3 and 8 + dog + fish == 20]; eq(sols, [(5, 7)], 'H4'); eq(q['val'], 7, 'H4 val')
    q = H['H5']; l18 = json.load(open(os.path.join(L1, 'lessons', 'l18.json')))['home_practice']; src = [h for h in l18 if h['id'] == 'H2'][0]; eq((q['text'], q['answer'], q['val']), (src['text'], src['answer'], src['val']), 'H5 is the Term 2 Lesson 8 item H2, copied')
    eq(q['rewind_of'], 'Term 2 Lesson 8', 'H5 tag'); eq(3 * 4 + 5, 17, 'H5 3 boxes of 4 pens and 5 loose pens'); eq(q['val'], [17], 'H5 val'); eq([h['tier'] for h in d['home_practice']], ['start', 'start', 'start', 'think', 'start'], 'home tiers')
    # ---------------------------------------------------------------- online practice, authored numbers
    items = {i['id']: i for i in d['online_practice']['items']}
    eq(items['c1']['answer'], _c1(dict(a=8, b=3)), 'c1'); eq(items['c2']['answer'], _c2(dict(a=2, b=4, c=3)), 'c2')
    g = drawn(items['c3']['fig']); eq(max(g, key=g.get), 'Plates', 'c3 most'); eq(items['c3']['answer'], 'plates', 'c3'); eq(items['c3']['options'], ['cups', 'plates', 'bowls'], 'c3 options')
    eq(items['c4']['answer'], 'Mei', 'c4'); eq(items['c5']['answer'], _c5(dict(t=12, a=5)), 'c5'); eq(items['t1']['answer'], _t1(dict(a=8, d=3, c=7)), 't1'); eq(8 + (8 - 3) + items['t1']['answer'], 20, 't1 sums to 20')
    eq(items['t2']['answer'], _t2(dict(n=7, m=3)), 't2'); eq(items['t3']['answer'], 'Graph B', 't3'); eq((count_in(1, 6), count_in(2, 4)), (6, 8), 't3 graph A shows 6 things and graph B shows 8'); eq(items['g1']['answer'], _g1(dict(n=4)), 'g1'); eq(things(items['g1']['fig_base'])['Stamps'], 12, 'g1 fig')
    eq(items['g2']['answer'], 2, 'g2'); pics_all = [p for p in range(0, 12) if count_in(3, p) == 21]; eq(pics_all, [7], 'g2 7 pictures in all'); eq(pics_all[0] - (3 + 2), 2, 'g2 third row')
    l28 = {i['id']: i for i in json.load(open(os.path.join(L1, 'lessons', 'l28.json')))['online_practice']['items']}
    eq((items['r1']['q'], items['r1']['answer']), (l28['c3']['q'], l28['c3']['answer']), 'r1 is Term 3 Lesson 8 c3'); eq((items['r2']['q'], items['r2']['answer']), (l28['c5']['q'], l28['c5']['answer']), 'r2 is Term 3 Lesson 8 c5')
    eq((items['r1']['rewind_of'], items['r2']['rewind_of']), ('Term 3 Lesson 8', 'Term 3 Lesson 8'), 'rewind tags'); eq(_r1(dict(p=5, k=4)), 20, 'r1'); eq(_r2(dict(s=2, e=3)), 11, 'r2')
    # ---------------------------------------------------------------- materials and hand-offs
    eq(d['workbook']['kits'], [], 'no kit page'); eq(d['materials']['kit_contract'], [], 'no kit contract'); eq(d['materials']['ruler'], False, 'no ruler')
    pn = ' '.join(d['parent']['next_materials']).lower(); eq(all(w in pn for w in ('tool-and-problem cards', '15 cards', 'cuts out')), True, 'hand-off to the next lesson names the 15 cards'); end = json.dumps(sl['s-end']['blocks']).lower(); eq('15 cards' in end and 'tool-and-problem' in end, True, 's-end hand-off')
    prev = os.path.join(L1, 'lessons', 'l37.json'); p = json.load(open(prev)); txt = ' '.join(p['parent']['next_materials']).lower(); eq('nothing to cut' in txt, True, 'lesson 37 hand-off: nothing to cut out for this lesson')
    eq(set(d['beyond']['where']) <= set(T) and not (set(d['beyond']['where']) & {q['id'] for q in d['tiers']['start']}), True, 'beyond items sit at Think harder or Go further')
    return n
