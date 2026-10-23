"""Independent answer checks for Level 1 Term 4 Lesson 7 (Lesson 37, Make Your Own Graph).

Everything in l37.json that can be computed is recomputed here from first principles, without the lesson's own sums:
  * a tray is a table of icon cells; the count of each kind is found by walking the cells and counting the icons (never by the lesson's numbers);
  * a picture graph is read from its rows (label, n, hidden boxes): a row with hidden boxes is an EMPTY row to be drawn, so its number is never read from the picture;
  * a tally is rebuilt stroke by stroke (groups of five are four strokes and a gate), and the number a tally shows is read back by counting the groups and the loose strokes;
  * 'how many more', 'in all', 'fewest' and the missing row are computed by matching pictures one to one (pairing) and by enumerating every possible size of the missing row;
  * a key where each picture stands for 2 is read by counting in 2s, a half picture is 1 thing;
  * the clues of G2 are solved by trying every number of stickers for Ben, Lily, Jamie and Ravi from 0 to 21 and keeping the sets that satisfy all four clues and the total (exactly one set);
  * the class items are registered here and shown to differ from every workbook, exit and home item. The online practice templates get brute-force oracles.
"""
import itertools
import json
import os
import re
from collections import Counter

L1 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# ---------------------------------------------------------------- readers
def nums(text):
    return [int(x) for x in re.findall(r'\d+', text)]


def tray_counts(fig):
    """Walk the cells of a table figure and count the icons of each kind (a cell may hold n copies)."""
    c = Counter()
    for row in fig['rows']:
        for cell in row:
            c[cell['icon']] += cell.get('n', 1)
    return dict(c)


def graph_rows(fig):
    """[(label, n, hidden)] of a picture graph: n is the number of pictures drawn, or the number of EMPTY boxes when the row is hidden."""
    out = []
    for r in fig['rows']:
        hid = len(r.get('hide', []))
        out.append((r['label'], r['n'], hid > 0))
    return out


def drawn(fig):
    """Pictures drawn in each row (0 for a row whose boxes are all empty)."""
    return {l: (0 if h else n) for l, n, h in graph_rows(fig)}


def things(fig):
    """Things each row stands for: pictures times the key (each=2 means each picture is 2 things); half a picture counts as half the key."""
    k = fig.get('each', 1)
    return {l: v * k for l, v in drawn(fig).items()}


def tally_marks(n):
    """Draw a tally for n things: a list of groups, each group is 4 strokes and a gate, then the loose strokes."""
    groups = []
    left = n
    while left >= 5:
        groups.append(['|', '|', '|', '|', '/']); left -= 5
    if left: groups.append(['|'] * left)
    return groups


def tally_reads(groups):
    """Read a tally back: a full group (four strokes and a gate) is 5, a loose stroke is 1."""
    t = 0
    for g in groups:
        t += 5 if g[-1] == '/' else len(g)
    return t


def more(a, b):
    """How many more a than b: pair the pictures one to one and count the pictures of a that are left without a partner."""
    left = 0
    for i in range(a):
        if i >= b: left += 1
    return left


def figs_in(blocks):
    out = []
    for b in blocks:
        if b.get('t') == 'visual': out.append(b)
        if b.get('t') == 'cols':
            for c in b['cols']: out += figs_in(c)
    return out


# ---------------------------------------------------------------- registries: what the class pictures show, and what the workbook pictures show
CLASS_TRAYS = {'s-rem3': {'sock': 5, 'shoe': 3}, 's-sneak': {'cup': 4, 'button': 3, 'sock': 2}, 's-m1': {'ball': 5, 'car': 3, 'bike': 4}}
CLASS_GRAPHS = {'s-rem1': (6, 4, 5), 's-explore2': (4, 2, 3), 's-m1-ans': (5, 3, 4), 's-m2-ans': (5, 3, 4), 's-m3': (5, 3, 4), 's-m4': (5, 3, 4), 's-m5-ans': (6, 5, 3), 's-opt': (5,)}
WB_TRAYS = {'S1': {'book': 6, 'cup': 4, 'ruler': 2}, 'E1': {'pencil': 4, 'rubber': 3}}
WB_GRAPHS = {'S2': (6, 8), 'S3': (7, 4, 6), 'S5': (3, 5, 8), 'T1': (9, 5, 6), 'T2': (6, 2, 4), 'T3': (4, 7, 5), 'G1': (4, 3, 7), 'G3': (5, 3, 9), 'E2': (7, 2)}


# ---------------------------------------------------------------- online practice oracles (brute force)
def _c1(e):
    cats, dogs = e['a'], e['b']
    return more(cats, dogs)


def _c2(e):
    n = 0
    for row in (e['a'], e['b'], e['c']):
        for _ in range(row): n += 1
    return n


def _c4(e):
    return tally_reads(tally_marks(5 + e['k']))


def _c5(e):
    return len([x for x in range(e['t']) if x >= e['a']])


def _t1(e):
    t = e['a'] + e['b'] + e['c']
    for c in range(0, 30):
        if e['a'] + e['b'] + c == t: return c


def _t3(e):
    n = 0
    for _ in range(e['n']):
        for _ in range(2): n += 1
    return n


def _r1(e):
    return 7 * e['w']                                                             # days in w weeks (Term 3 Lesson 7 c2, copied)


def _r2(e):
    return e['s'] + 21                                                            # next number counting in 7s (Term 3 Lesson 7 c5, copied)


ORACLES = {'c1': _c1, 'c2': _c2, 'c4': _c4, 'c5': _c5, 't1': _t1, 't3': _t3, 'r1': _r1, 'r2': _r2}
BASE_ENV = {'c1': dict(a=7, b=4), 'c2': dict(a=3, b=2, c=4), 'c4': dict(k=3), 'c5': dict(t=10, a=4), 't1': dict(a=6, b=5, c=4), 't3': dict(n=3), 'r1': dict(n=3), 'r2': dict(n=3)}


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

    # ---------------------------------------------------------------- tally reading is sound for every number used
    for m in range(0, 21):
        eq(tally_reads(tally_marks(m)), m, f'tally for {m} reads back as {m}')
    eq(len(tally_marks(8)), 2, 'a tally of 8 is one group of 5 and one group of 3'); eq(tally_marks(8)[0][-1], '/', 'the first group of 8 is a full group')

    # ---------------------------------------------------------------- class registries match the slides, and differ from the workbook
    for sid, want in CLASS_TRAYS.items():
        eq(tray_counts(F(sid)), want, f'{sid} tray counts')
    eq(tray_counts(F('s-m1')), CLASS_TRAYS['s-m1'], 's-m1 tray')
    eq(tuple(drawn(F('s-rem1')).values()), CLASS_GRAPHS['s-rem1'], 's-rem1 graph')
    eq(tuple(v for v in things(F('s-explore2', 0)).values()), CLASS_GRAPHS['s-explore2'], 's-explore2 example graph'); eq(F('s-explore2', 0)['orient'], 'rows', 's-explore2 example is a rows graph like the mat')
    eq(tuple(drawn(F('s-m1-ans')).values()), CLASS_GRAPHS['s-m1-ans'], 's-m1-ans tally rows'); eq(F('s-m1-ans').get('tally'), True, 's-m1-ans is a tally')
    eq(tuple(drawn(F('s-m2-ans')).values()), CLASS_GRAPHS['s-m2-ans'], 's-m2-ans graph'); eq(all(h for _, _, h in graph_rows(F('s-m2'))), True, 's-m2 asks the child to draw: every row is empty')
    eq(tuple(drawn(F('s-m3')).values()), CLASS_GRAPHS['s-m3'], 's-m3 graph'); eq(tuple(drawn(F('s-m4')).values()), CLASS_GRAPHS['s-m4'], 's-m4 graph')
    eq(tuple(drawn(F('s-m5-ans')).values()), CLASS_GRAPHS['s-m5-ans'], 's-m5-ans graph'); eq(F('s-opt').get('each'), 2, 's-opt key is 2'); eq(tuple(drawn(F('s-opt')).values()), CLASS_GRAPHS['s-opt'], 's-opt graph')
    cls_tuples = {tuple(sorted(v)) for v in CLASS_GRAPHS.values()}
    wb_tuples = [tuple(sorted(v)) for v in WB_GRAPHS.values()]
    eq([t for t in wb_tuples if t in cls_tuples], [], 'no workbook, exit or home graph repeats the numbers of a class graph')
    eq(len(set(wb_tuples)) - len(wb_tuples), 0, 'the workbook graphs are all different from each other, except where one question shares the picture of another')
    cls_trays = [tuple(sorted(v.items())) for v in CLASS_TRAYS.values()]
    eq(set(tuple(sorted(v.items())) for v in WB_TRAYS.values()) & set(cls_trays), set(), 'no workbook tray repeats a class tray')

    # ---------------------------------------------------------------- warm-up
    g = drawn(F('s-rem1')); eq(max(g, key=g.get), 'Mei', 's-rem1 who read the most'); eq(more(g['Mei'], g['Ben']), 2, 's-rem1 Mei has 2 more than Ben'); eq(g['Ben'] + g['Siti'], 9, 's-rem1 your turn: Ben and Siti in all')
    f = F('s-rem2'); eq((f['start'], f['end'], f['step']), (0, 20, 2), 's-rem2 line'); shown = [x for x in range(0, 21, 2) if x not in f['hide']]; eq(f['hide'], [6, 12, 16], 's-rem2 missing numbers'); eq(len(shown), 8, 's-rem2 numbers shown')
    eq([x for x in range(10, 21, 2)], [10, 12, 14, 16, 18, 20], 's-rem2 your turn counts in 2s from 10 to 20')
    tc = tray_counts(F('s-rem3')); eq((tc['sock'], tc['shoe'], sum(tc.values())), (5, 3, 8), 's-rem3 tray')
    # ---------------------------------------------------------------- sneak-peek
    sp = d['sneak_peek']; tc = tray_counts(F('s-sneak')); eq(tc['cup'], 4, 'sneak 1 cups'); eq(sp['a1'], '4 cups.', 'sneak a1'); eq(sum(tc.values()), 9, 'sneak tray has 9 things'); eq(sorted(tc.values()), [2, 3, 4], 'sneak kinds 4, 3 and 2')
    eq('4 cups' in sp['a2'] and '3 buttons' in sp['a2'] and '2 socks' in sp['a2'], True, 'sneak a2 matches the tray')
    # ---------------------------------------------------------------- Explore: no counts on the slides (each child has their own things)
    for sid in ('s-explore1', 's-explore3'):
        eq(len(figs_in(sl[sid]['blocks'])), 0, f'{sid} has no picture that shows a count')
    # ---------------------------------------------------------------- Mini-lesson
    tc = tray_counts(F('s-m1')); eq(sum(tc.values()), 12, 'm1 tray has 12 toys'); eq((tc['ball'], tc['car'], tc['bike']), (5, 3, 4), 'm1 counts'); eq(5 + 3 + 4, 12, 'm1 sum')
    f = F('s-m1-ans'); eq(tuple(v for _, v, _ in graph_rows(f)), (5, 3, 4), 'm1-ans tally rows'); eq(tally_reads(tally_marks(5)), 5, 'm1 one group of 5')
    f = F('s-m2'); eq([len(r['hide']) for r in f['rows']], [6, 6, 6], 'm2 empty boxes: 6 in each row, more than any row needs'); eq(max(5, 3, 4) < 6, True, 'm2 boxes are more than needed')
    f = F('s-m3'); g = drawn(f); eq(more(g['Balls'], g['Cars']), 2, 'm3 balls over cars'); eq(sum(g.values()), 12, 'm3 total'); eq(min(g, key=g.get), 'Cars', 'm3 fewest'); eq(sum(g.values()), sum(tc.values()), 'm3 total equals the tray')
    g4 = drawn(F('s-m4')); eq(g4['Bikes'], 4, 'm4 question 1: bikes'); eq(more(g4['Balls'], g4['Cars']), 2, 'm4 question 3: more balls than cars')
    eq('Questions 1 and 3' in sl['s-m4-ans']['blocks'][0]['text'], True, 'm4 answer slide names questions 1 and 3')
    f = F('s-m5'); rr = graph_rows(f); eq([(l, n, h) for l, n, h in rr], [('Plums', 6, False), ('Figs', 5, False), ('Pears', 7, True)], 'm5 rows'); total = 14; seen = 6 + 5
    sols = [c for c in range(0, 8) if 6 + 5 + c == total]; eq(sols, [3], 'm5 only 3 pears fit the total'); eq(sols[0] < 7, True, 'm5 the 7 boxes are more than needed'); eq(drawn(F('s-m5-ans'))['Pears'], 3, 'm5-ans pears')
    eq(nums(sl['s-m5']['blocks'][-1]['text']), [14], 'm5 text total')
    # ---------------------------------------------------------------- Talk
    eq(d['talk']['answer'].startswith('No. The graph shows the pets in the shop'), True, 'talk answer')
    f = F('s-opt'); eq(sum(2 for _ in range(int(f['rows'][0]['n']))), 10, 's-opt 5 pictures of 2 are 10 shells')
    # ---------------------------------------------------------------- Start here
    q = T['S1']; tc = tray_counts(vis(q)); eq((tc['cup'], tc['book'], tc['ruler']), (4, 6, 2), 'S1 counts'); eq(q['val'], [4, 6, 2], 'S1 val'); eq(sum(tc.values()), 12, 'S1 total'); eq([nums(p['text']) for p in q['parts']], [[], [], []], 'S1 parts hold no numbers other than the boxes')
    eq(WB_TRAYS['S1'], tc, 'S1 registry'); eq(len(vis(q)['rows']) * len(vis(q)['rows'][0]), 12, 'S1 cells')
    q = T['S2']; f = vis(q); eq(f.get('tally'), True, 'S2 is a tally'); g = drawn(f); eq((tally_reads(tally_marks(g['Pens'])), tally_reads(tally_marks(g['Rubbers']))), (6, 8), 'S2 pens and rubbers'); eq(q['val'], [6, 8], 'S2 val'); eq(tuple(g.values()), WB_GRAPHS['S2'], 'S2 registry')
    eq(len(tally_marks(6)), 2, 'S2 pens are one group of 5 and 1 stroke'); eq(len(tally_marks(8)), 2, 'S2 rubbers are one group of 5 and 3 strokes')
    q = T['S3']; g = drawn(vis(q)); eq(tuple(g.values()), WB_GRAPHS['S3'], 'S3 registry'); eq(more(g['Cats'], g['Fish']), 3, 'S3 more cats than fish'); eq(sum(g.values()), 17, 'S3 total'); eq(q['val'], [3, 17], 'S3 val'); eq(nums(q['text']), [1], 'S3 key is 1')
    q = T['S4']; f = vis(q); eq([len(r['hide']) for r in f['rows']], [6, 6, 6], 'S4 boxes'); eq(nums(q['text']), [2, 5, 3, 1], 'S4 text numbers: 2, 5, 3 fruits and 1 picture each'); eq(q['val'], [2, 5, 3], 'S4 val'); eq(max(q['val']) < 6, True, 'S4 boxes are more than needed'); eq(sum(q['val']), 10, 'S4 pictures')
    eq([r['label'] for r in f['rows']], ['Apples', 'Pears', 'Plums'], 'S4 labels'); eq(f['each'] if 'each' in f else 1, 1, 'S4 key is 1')
    q = T['S5']; g = drawn(vis(q)); eq(tuple(g.values()), WB_GRAPHS['S5'], 'S5 registry'); eq(min(g, key=g.get), 'Chess', 'S5 fewest'); eq(g['Ludo'] + g['Cards'], 13, 'S5 ludo and cards'); eq(q['val'], ['Chess', 13], 'S5 val'); eq(q['parts'][0]['choices'], ['Chess', 'Ludo', 'Cards'], 'S5 choices')
    q = T['S6']; g = drawn(vis(T['S5'])); st = [min(g, key=g.get) == 'Cards', more(g['Ludo'], g['Chess']) == 2, g['Chess'] + g['Ludo'] == g['Cards'], sum(g.values()) == 15]
    eq(['True' if x else 'False' for x in st], q['val'], 'S6 true or false'); eq([s['s'] for s in q['tf']][1], 'Ludo has 2 more children than chess.', 'S6 statement 2'); eq(len(q['tf']), 4, 'S6 four statements'); eq(sum(g.values()), 16, 'S6 total is 16, so 15 is false')
    eq(len([x for x in st if x]) == 2 and len([x for x in st if not x]) == 2, True, 'S6 has two true and two false statements'); eq(q.get('visual'), None, 'S6 uses the graph in question 5'); eq('in S5' in q['text'], True, 'S6 text points to S5')
    eq(sum(x['mins'] for x in d['tiers']['start']) <= 20, True, 'Start here fits in 20 minutes'); eq([x['page'] for x in d['tiers']['start']], [1, 1, 1, 2, 2, 2], 'Start here pages')
    # ---------------------------------------------------------------- Think harder
    q = T['T1']; f = vis(q, 0); g = drawn(f); eq(f.get('tally'), True, 'T1 tally'); got = [tally_reads(tally_marks(g[k])) for k in ('Hats', 'Bags', 'Shoes')]; eq(got, [9, 5, 6], 'T1 numbers'); eq(sum(got), 20, 'T1 total'); eq(q['val'], [9, 5, 6, 20], 'T1 val')
    tb = vis(q, 1); eq(sum(1 for r in tb['rows'] if r[1] == '[]'), 3, 'T1 table has 3 boxes'); eq([r[0] for r in tb['rows']], ['Hats', 'Bags', 'Shoes'], 'T1 table rows match the tally'); eq(tuple(g.values()), WB_GRAPHS['T1'], 'T1 registry')
    q = T['T2']; f = vis(q); g = drawn(f); eq(tuple(g.values()), WB_GRAPHS['T2'], 'T2 registry'); opts = q['mcq']['options']; eq(len(opts), 4, 'T2 four options')
    can = [False, True, False, False]; eq(q['val'], [2], 'T2 val'); eq(can.index(True) + 1, 2, 'T2 only option 2 can be read from the graph'); eq(more(g['Shells'], g['Stones']), 4, 'T2 option 2 has an answer on the graph'); eq('more shells than stones' in opts[1], True, 'T2 option 2 text')
    q = T['T3']; f = vis(q); rr = graph_rows(f); eq([(l, h) for l, _, h in rr], [('Maths', False), ('Story', False), ('Art', True)], 'T3 rows'); a, b = rr[0][1], rr[1][1]; total = 16
    sols = [c for c in range(0, 9) if a + b + c == total]; eq(sols, [5], 'T3 exactly 5 art books'); eq(a + b, 11, 'T3 maths and story'); eq(q['val'], [11, 5], 'T3 val'); eq(nums(q['text']), [1, 16], 'T3 text: key 1, total 16'); eq(rr[2][1], 8, 'T3 8 empty boxes, more than needed'); eq((a, b, sols[0]), WB_GRAPHS['T3'][:2] + (5,), 'T3 registry')
    eq(len(d['tiers']['think']), 3, 'three Think harder items')
    # ---------------------------------------------------------------- Go further
    q = T['G1']; f = vis(q); eq(f['each'], 2, 'G1 key is 2'); rr = f['rows']; eq(rr[0]['n'], 4, 'G1 mints drawn'); mints = rr[0]['n'] * f['each']; eq(mints, 8, 'G1 mints are 8 sweets')
    toff = 0
    for _ in range(3): toff += 2
    eq(toff, 6, 'G1 3 pictures are 6 toffees'); eq(q['parts'][0]['val'], 3, 'G1 pictures'); gums = 3 * 2 + 1; eq(gums, 7, 'G1 gums'); eq(rr[2]['n'], 3.5, 'G1 gums row shows 3 and a half pictures'); eq(rr[2]['n'] * f['each'], 7, 'G1 half picture is half of 2')
    eq(len(rr[1]['hide']), 5, 'G1 toffees: 5 boxes, more than 3'); eq(rr[1]['label'], 'Toffees', 'G1 toffees row'); eq(q['val'], [3, 7], 'G1 val'); eq(nums(q['parts'][0]['text']), [6], 'G1 part text'); eq(d['beyond']['where'], ['G1'], 'G1 is the beyond item')
    eq(WB_GRAPHS['G1'], (4, 3, 7), 'G1 registry (pictures drawn or needed: 4, 3 and 7 gums)'); eq([r['label'] for r in rr], ['Mints', 'Toffees', 'Gums'], 'G1 labels')
    q = T['G2']; sols = []
    for ben in range(0, 22):
        for lily in range(0, 22):
            for jamie in range(0, 22):
                for ravi in range(0, 22):
                    if ben == 4 and lily == ben + 3 and jamie == lily - 2 and ben + lily + jamie + ravi == 21: sols.append((ben, lily, jamie, ravi))
    eq(sols, [(4, 7, 5, 5)], 'G2 exactly one set of numbers fits every clue'); eq(q['val'], [sols[0][1], sols[0][3]], 'G2 val: Lily and Ravi'); eq(nums(q['text']), [21, 4, 3, 2], 'G2 text')
    q = T['G3']; g = drawn(vis(q)); eq(tuple(g.values()), WB_GRAPHS['G3'], 'G3 registry'); eq(more(g['Tulips'], g['Daisies']), 6, 'G3 example answer: 6 more tulips than daisies'); eq(sum(g.values()), 17, 'G3 example answer: 17 flowers'); eq(min(g, key=g.get), 'Daisies', 'G3 fewest is daisies')
    eq(('6 more' in q['solution'] and '17' in q['solution'] and 'Daisies' in q['solution']), True, 'G3 solution examples match the graph'); eq(q['val'], ['open'], 'G3 open')
    # ---------------------------------------------------------------- Investigation
    eq(inv['val'], ['open'], 'I1 open'); eq(inv.get('draw'), 0, 'I1 draws on paper at home'); eq(nums(inv['first'] + ' ' + inv['text']), [6, 2, 12, 3], 'I1 numbers')
    # ---------------------------------------------------------------- Exit ticket
    q = X['E1']; tc = tray_counts(vis(q)); eq(tc['rubber'], 3, 'E1 rubbers'); eq(q['val'], 3, 'E1 val'); eq(WB_TRAYS['E1'], tc, 'E1 registry'); eq(sum(tc.values()), 7, 'E1 total')
    q = X['E2']; g = drawn(vis(q)); eq(tuple(g.values()), WB_GRAPHS['E2'], 'E2 registry'); eq(more(g['Ali'], g['Mei']), 5, 'E2 more biscuits'); eq(q['val'], 5, 'E2 val')
    q = X['E3']; eq(q['val'], [1], 'E3 val'); eq(len(q['mcq']['options']), 2, 'E3 two options'); eq(q['mcq']['options'][0], 'How many cars are in the box?', 'E3 option 1 can be read from a graph of toys'); eq('best' in q['mcq']['options'][1], True, 'E3 option 2 is about liking')
    # ---------------------------------------------------------------- home practice
    q = H['H1']; eq(nums(q['text'])[:3], [10, 4, 3], 'H1 text'); eq(10 - (4 + 3), 3, 'H1'); eq(q['val'], 3, 'H1 val')
    q = H['H2']; eq(nums(q['text'])[:3], [8, 5, 1], 'H2 text'); eq(more(8, 5), 3, 'H2'); eq(q['val'], 3, 'H2 val')
    q = H['H3']; eq(nums(q['text'])[:3], [8, 1, 5], 'H3 text'); eq(len(tally_marks(8)[1]), 3, 'H3 strokes after the group of 5'); eq(q['val'], 3, 'H3 val')
    q = H['H4']; eq(nums(q['text'])[:3], [15, 6, 5], 'H4 text'); sols = [c for c in range(0, 16) if 6 + 5 + c == 15]; eq(sols, [4], 'H4'); eq(q['val'], 4, 'H4 val')
    q = H['H5']; l17 = json.load(open(os.path.join(L1, 'lessons', 'l17.json')))['home_practice']; src = [h for h in l17 if h['id'] == 'H1'][0]; eq((q['text'], q['answer'], q['val']), (src['text'], src['answer'], src['val']), 'H5 is the Term 2 Lesson 7 item H1, copied')
    eq(q['rewind_of'], 'Term 2 Lesson 7', 'H5 tag'); eq(len([x for x in range(10) if x % 2 == 0]), 5, 'H5 dealing 10 stickers to 2 friends gives 5 each'); eq(q['val'], [5], 'H5 val'); eq([h['tier'] for h in d['home_practice']], ['start', 'start', 'start', 'think', 'start'], 'home tiers')
    # ---------------------------------------------------------------- online practice, authored numbers
    items = {i['id']: i for i in d['online_practice']['items']}
    eq(items['c1']['answer'], _c1(dict(a=7, b=4)), 'c1'); eq(items['c2']['answer'], _c2(dict(a=3, b=2, c=4)), 'c2')
    f = items['c3']['fig']; g = drawn(f); eq(min(g, key=g.get), 'Socks', 'c3 fewest'); eq(items['c3']['answer'], 'socks', 'c3'); eq(items['c3']['options'], ['spoons', 'socks', 'shoes'], 'c3 options'); eq(tuple(g.values()), (5, 2, 4), 'c3 graph')
    eq(items['c4']['answer'], _c4(dict(k=3)), 'c4'); eq(items['c5']['answer'], _c5(dict(t=10, a=4)), 'c5'); eq(items['t1']['answer'], _t1(dict(a=6, b=5, c=4)), 't1'); eq(6 + 5 + items['t1']['answer'], 15, 't1 sums to 15')
    eq(items['t2']['answer'], 'How many more cups than spoons are in the bag?', 't2'); eq(items['t2']['options'][1], items['t2']['answer'], 't2 option')
    eq(items['t3']['answer'], _t3(dict(n=3)), 't3'); eq(items['g1']['answer'], 3 * 2 + 1, 'g1'); eq(items['g1']['fig']['rows'][0]['n'] * items['g1']['fig']['each'], 7, 'g1 fig')
    ben = 5; kumar = ben + 3; aisha = kumar - 2; eq(items['g2']['answer'], aisha, 'g2'); eq(items['g2']['answer'], 6, 'g2 value')
    l27 = {i['id']: i for i in json.load(open(os.path.join(L1, 'lessons', 'l27.json')))['online_practice']['items']}
    eq((items['r1']['q'], items['r1']['answer']), (l27['c2']['q'], l27['c2']['answer']), 'r1 is Term 3 Lesson 7 c2'); eq((items['r2']['q'], items['r2']['answer']), (l27['c5']['q'], l27['c5']['answer']), 'r2 is Term 3 Lesson 7 c5')
    eq((items['r1']['rewind_of'], items['r2']['rewind_of']), ('Term 3 Lesson 7', 'Term 3 Lesson 7'), 'rewind tags'); eq(_r1(dict(w=2)), 14, 'r1 2 weeks'); eq(_r2(dict(s=3)), 24, 'r2 3, 10, 17, 24')
    # ---------------------------------------------------------------- kit contract and hand-offs
    k = d['workbook']['kits'][0]; eq((k['type'], k['cols'], k['rows']), ('graph_mat', 8, 5), 'kit page: the graph mat is 5 rows of 8 squares (one row for each kind)')
    kc = {r['piece'].split(' (')[0]: r for r in d['materials']['kit_contract']}; eq(kc['graph mat page']['supplied'], 1, 'one mat'); eq(kc['graph mat page']['max_used'], 1, 'Explore uses the mat once')
    eq(kc['small things from home']['supplied'] >= kc['small things from home']['max_used'], True, 'enough things'); eq(kc['small things from home']['max_used'], 12, 'Explore sorts 12 things'); eq(8 <= 8 and 3 <= 5, True, 'at most 8 of a kind and 3 or 4 kinds fit a mat of 5 rows of 8 squares')
    eq(d['materials']['ruler'], False, 'no ruler needed')
    pn = ' '.join(d['parent']['next_materials']).lower(); eq('nothing to cut' in pn, True, 'hand-off to the next lesson: nothing to cut'); eq('graph detectives' in json.dumps(sl['s-end']['blocks']).lower(), True, 's-end names the next lesson')
    eq(set(d['beyond']['where']) <= set(T) and not (set(d['beyond']['where']) & {q['id'] for q in d['tiers']['start']}), True, 'beyond items sit at Think harder or Go further')
    # no class number appears in Start here, Think harder or the exit ticket as a tray or graph registry entry
    return n
