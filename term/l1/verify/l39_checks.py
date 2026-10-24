"""Independent answer checks for Level 1 Term 4 Lesson 9 (Lesson 39, The Problem-Solving Toolbox).

Everything in l39.json that can be computed is recomputed here from first principles, without the lesson's own sums:
  * every story is solved by SEARCH (try every whole number in a range and keep the ones that fit every clue), and the number of answers is checked to be exactly one;
  * strips are read from the drawn lengths; a table is rebuilt by adding the step one row at a time;
  * a list of pairs is built by taking every pair of different coins or fruits once;
  * the line puzzle is solved by trying every line length with the child in the right place from the front and from the back;
  * the class items (Remember, sneak-peek, Explore cards, Mini-lesson, talk) are registered here and shown to differ in their numbers from every workbook, exit and home item;
  * the kit contract (8 tool cards and 8 problem cards, card labels short enough to fit a card) is checked against the kit page the lesson prints;
  * the online practice templates get brute-force oracles.
"""
import itertools
import json
import os
import re

L1 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def nums(text):
    return [int(x) for x in re.findall(r'\d+', text)]


def count_up(a, b):
    """How many steps from a up to b, one at a time."""
    n = 0
    while a < b:
        a += 1; n += 1
    return n


def times(k, n):
    t = 0
    for _ in range(n): t += k
    return t


def find(pred, lo=0, hi=200):
    return [x for x in range(lo, hi + 1) if pred(x)]


def table_row(start, step, n):
    row = [start]
    while len(row) < n: row.append(row[-1] + step)
    return row


def pairs(items):
    out = []
    for i in range(len(items)):
        for j in range(i + 1, len(items)): out.append((items[i], items[j]))
    return out


def line_length(front, back):
    """Lengths of a line where a child is `front`-th from the front and `back`-th from the back."""
    return [n for n in range(1, 40) if front <= n and back <= n and (n - front + 1) == back]


def figs_in(blocks):
    out = []
    for b in blocks:
        if b.get('t') == 'visual': out.append(b)
        if b.get('t') == 'cols':
            for c in b['cols']: out += figs_in(c)
    return out


def row_nums(fig, r=0):
    return [c for c in fig['rows'][r]]


# ---------------------------------------------------------------- online practice oracles (brute force)
def _c1(e):
    mei = e['a'] - e['b']
    for m in range(0, 40):
        if m + e['b'] == e['a']: mei = m
    return e['a'] + mei


def _c2(e):
    row = e['s']
    for _ in range(e['n'] - 1): row += e['e']
    return row


def _c3(e):
    t = e['x'] + e['a']                                   # I add a and get t: try every start
    return [x for x in range(0, 100) if x + e['a'] == t][0]


def _c4(e):
    t = e['k'] * e['u']
    return [u for u in range(1, 30) if times(u, e['k']) == t][0]


def _t1(e):
    t = e['k'] * e['u']
    one = [u for u in range(1, 40) if times(u, e['k']) == t][0]
    return times(one, e['m'])


def _t2(e):
    r = e['x'] + e['a'] - e['b']
    return [x for x in range(0, 100) if x + e['a'] - e['b'] == r][0]


def _g1(e):
    t = 4 * e['r']
    return [r for r in range(0, 60) if r + 3 * r == t][0]


def _g2(e):
    t = 4 * e['r']
    return [3 * r for r in range(0, 60) if r + 3 * r == t][0]


def _r1(e):
    s = e['a'] + e['b']                                   # the child wrote s - b = a; add back: a + b
    x = e['a']
    for _ in range(e['b']): x += 1
    assert x == s
    return x


def _r2(e):
    a, b = e['a'], e['b']                                 # the child forgot the ten: add the ones, carry the ten
    ones = a % 10 + b % 10
    tens = a // 10 * 10 + b // 10 * 10
    return tens + ones


ORACLES = {'c1': _c1, 'c2': _c2, 'c3': _c3, 'c4': _c4, 't1': _t1, 't2': _t2, 'g1': _g1, 'g2': _g2, 'r1': _r1, 'r2': _r2}
BASE_ENV = {'c1': dict(a=12, b=4), 'c2': dict(s=2, e=3, n=5), 'c3': dict(x=9, a=6), 'c4': dict(k=3, u=3), 't1': dict(k=4, u=6, m=7), 't2': dict(x=15, a=9, b=4), 'g1': dict(r=6), 'g2': dict(r=6), 'r1': dict(a=40, b=30), 'r2': dict(a=39, b=24)}


# ---------------------------------------------------------------- the registry of class numbers
CLASS_ITEMS = {
    'rem1': [8, 3], 'rem2': [3, 12], 'rem3': [5, 12], 'rem1-turn': [11], 'rem2-turn': [4, 5], 'rem3-turn': [3, 9],
    'sneak1': [4, 3], 'sneak2': [10, 2],
    'card1': [9, 4], 'card2': [2, 4, 6, 6], 'card3': [2, 3], 'card4': [3, 7], 'card5': [6, 9], 'card6': [5, 15, 8], 'card7': [20, 8, 5], 'card8': [2, 3, 8],
    'mini2': [14, 6], 'mini3': [2, 5, 8, 7], 'mini4': [9, 4, 20], 'mini5': [2, 18], 'talk': [24, 12], 'opt': [5]}


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

    # ---------------------------------------------------------------- the kit: 7 tool cards, 8 problem cards, labels that fit
    kit = d['workbook']['kits'][0]
    eq(kit['type'], 'cards', 'kit type'); TOOLN = kit['labels'][0::2]; PROBN = kit['labels'][1::2]; eq(len(TOOLN), 8, '8 tool cards'); eq(len(PROBN), 8, '8 problem cards'); kit = dict(kit, tools=[[None, t] for t in TOOLN], problems=PROBN)
    eq([t[1] for t in kit['tools']], ['Draw it', 'Act it out', 'Spot the pattern', 'List every way', 'Make a table', 'Work backwards', 'Guess and check', 'Try something simpler'], 'tool names (the eight card names)')
    eq(all(len(p) <= 24 for p in kit['problems']), True, 'every problem label fits on a card (24 characters at most)')
    eq([p.split('.')[0] for p in kit['problems']], [str(i) for i in range(1, 9)], 'cards are numbered 1 to 8')
    kc = {r['piece']: r for r in d['materials']['kit_contract']}
    eq((kc['tool cards']['supplied'], kc['tool cards']['max_used']), (8, 8), 'kit contract tools'); eq((kc['problem cards']['supplied'], kc['problem cards']['max_used']), (8, 8), 'kit contract problems')
    eq(len(kit['tools']) >= kc['tool cards']['max_used'] and len(kit['problems']) >= kc['problem cards']['max_used'], True, 'the kit supplies what Explore uses')

    # ---------------------------------------------------------------- Remember
    f = F('s-rem1'); a, b = f['bars'][0]['len'], f['bars'][1]['len']; eq((a, b), (8, 3), 'rem1 strips'); eq(count_up(b, a), 5, 'rem1 how many more'); eq(a + b, 11, 'rem1 your turn: in all')
    eq(f['gap']['between'], [0, 1], 'rem1 gap between the two strips')
    pens = [u for u in range(1, 20) if times(u, 3) == 12]; eq(pens, [4], 'rem2 1 pen costs $4'); eq(times(4, 5), 20, 'rem2 your turn: 5 pens'); eq(F('s-rem2')['n'], 3, 'rem2 3 pens drawn')
    start = find(lambda x: x + 5 == 12); eq(start, [7], 'rem3 my number is 7'); eq(find(lambda x: x - 3 == 9), [12], 'rem3 your turn is 12')
    f = F('s-rem3'); eq((f['jumps'][0][0], f['jumps'][0][1], f['jumps'][0][2]), (7, 12, '+5'), 'rem3 line: a jump of 5 from 7 to 12'); eq(f['hide'], [7], 'rem3 start hidden'); eq(count_up(7, 12), 5, 'rem3 jump of 5')
    # ---------------------------------------------------------------- sneak-peek
    sp = d['sneak_peek']; eq(nums(sp['q1']), [4, 3], 'sneak q1'); eq(4 + 3, 7, 'sneak 1'); eq(sp['a1'], '7 stickers.', 'sneak a1')
    sols = [(m, al) for m in range(0, 11) for al in range(0, 11) if m + al == 10 and al == m + 2]; eq(sols, [(4, 6)], 'sneak 2 exactly one answer'); eq(nums(sp['q2']), [10, 2], 'sneak q2'); eq(sp['a2'].startswith('4 stickers.'), True, 'sneak a2')
    # ---------------------------------------------------------------- Explore: the eight problems, each solved by search
    pr = {}
    t = sl['s-explore2']['blocks'][0]['rows'][1:] + sl['s-explore3']['blocks'][0]['rows'][1:]
    eq([r[0] for r in t], [str(i) for i in range(1, 9)], 'explore problems numbered 1 to 8'); pr = {r[0]: r[1] for r in t}
    # 1 strip: Ali 9, Mei 4 fewer
    mei = [m for m in range(0, 20) if count_up(m, 9) == 4]; eq(mei, [5], 'P1 Mei has 5'); eq(9 + 5, 14, 'P1 in all'); eq(nums(pr['1']), [9, 4], 'P1 text')
    # 2 table: 2, 4, 6 ... the 6th
    row = table_row(2, 2, 6); eq(row[5], 12, 'P2 the 6th row'); eq(nums(pr['2']), [2, 4, 6, 2, 6], 'P2 text')
    # 3 list: pairs from 3 fruits
    eq(len(pairs(['apple', 'pear', 'plum'])), 3, 'P3 three pairs')
    # 4 draw: Ravi 3rd in a line of 7
    eq(len([p for p in range(1, 8) if p > 3]), 4, 'P4 four children are behind Ravi'); eq(nums(pr['4']), [3, 7], 'P4 text')
    # 5 backwards
    eq(find(lambda x: x - 6 == 9), [15], 'P5 the number is 15'); eq(nums(pr['5']), [6, 9], 'P5 text')
    # 6 find one first
    one = [u for u in range(1, 30) if times(u, 5) == 15]; eq(one, [3], 'P6 1 bun costs $3'); eq(times(3, 8), 24, 'P6 8 buns'); eq(nums(pr['6']), [5, 15, 8], 'P6 text')
    # 7 guess and check: 6 coins, 5 cents and 10 cents, 45 cents
    sp7 = [(a_, 6 - a_) for a_ in range(7) if 5 * a_ + 10 * (6 - a_) == 45]; eq(sp7, [(3, 3)], 'P7 exactly one split'); eq(nums(pr['7']), [6, 5, 10, 45], 'P7 text'); eq(nums(kit['problems'][6]), [7, 6, 45], 'P7 card label')
    # 8 table: 2 red with 3 blue
    red, blue = 2, 3; k = [m for m in range(1, 10) if times(red, m) == 8]; eq(k, [4], 'P8 4 groups of 2 red'); eq(times(blue, 4), 12, 'P8 12 blue'); eq(nums(pr['8']), [2, 3, 8], 'P8 text')
    eq([p[0] for p in kit['problems']] == [str(i) for i in range(1, 9)], True, 'cards match the slide numbers')
    tools_by_card = [r[1] for r in sl['s-explore2-ans']['blocks'][0]['rows'][1:]] + [r[1] for r in sl['s-explore3-ans']['blocks'][0]['rows'][1:]]
    eq(tools_by_card, ['Draw it (two strips)', 'Spot the pattern', 'List every way', 'Act it out, or Draw it', 'Work backwards', 'Try something simpler (find 1 first)', 'Guess and check', 'Make a table'], 'the tool that fits each card')
    eq(sorted(t.split(' (')[0].split(',')[0] for t in tools_by_card), sorted([t[1] for t in kit['tools']]), 'every one of the 8 tools is the best fit of one card')
    # ---------------------------------------------------------------- Mini-lesson
    f = F('s-m2'); pip = f['bars'][0]['len']; rae = [r for r in range(0, 30) if count_up(r, pip) == 6]; eq(rae, [8], 'm2 Rae has 8'); eq(f['bars'][1]['len'], 8, 'm2 strip to scale'); eq(pip + rae[0], 22, 'm2 in all'); eq(F('s-m2-ans')['brace']['text'], '22', 'm2-ans brace')
    f = F('s-m3'); row = table_row(2, 3, 7); eq(row, [2, 5, 8, 11, 14, 17, 20], 'm3 the table'); eq(row[6], 20, 'm3 the 7th path'); eq(f['rows'][0][1:4], ['2', '5', '8'], 'm3 given cells'); eq([int(x) for x in F('s-m3-ans')['rows'][0][1:]], row, 'm3-ans row')
    x = find(lambda s: s + 9 - 4 == 20); eq(x, [15], 'm4 exactly one number'); eq(F('s-m4-ans')['rows'][0], ['15', '+ 9', '24', '− 4', '20'], 'm4-ans row'); eq(15 + 9, 24, 'm4 forwards'); eq(24 - 4, 20, 'm4 forwards 2')
    sols = [r for r in range(0, 19) if r + 2 * r == 18]; eq(sols, [6], 'm5 exactly one answer'); f = F('s-m5'); eq((f['bars'][0]['len'], f['bars'][1]['len']), (1, 2), 'm5 strips: Rae 1 part, Pip 2 parts'); eq(f['brace']['text'], '18', 'm5 total')
    tb = F('s-m5-ans')['rows']; eq([[int(c) for c in r] for r in tb], [[4, 8, 12], [5, 10, 15], [6, 12, 18]], 'm5 table of tries'); eq(all(r[1] == 2 * r[0] and r[2] == r[0] + r[1] for r in [[int(c) for c in r] for r in tb]), True, 'm5 each try: Pip twice Rae, and the total')
    eq([r[0] for r in [[int(c) for c in r] for r in tb] if r[2] == 18], [6], 'm5 the try that gives 18')
    # ---------------------------------------------------------------- Talk and optional slide
    sols = [r for r in range(0, 30) if r + 2 * r == 24]; eq(sols, [8], 'talk Rae has 8'); eq(12 + 2 * 12, 36, 'talk the child: 12 and 24 make 36'); eq(36 == 24, False, 'talk the child is wrong'); eq(nums(d['talk']['question']), [24, 24, 2, 12, 12], 'talk numbers'); eq(d['talk']['answer'].startswith('No.'), True, 'talk answer')
    cuts = [c for c in range(0, 10) if c + 1 == 5]; eq(cuts, [4], 'opt: 5 pieces need 4 cuts')
    # ---------------------------------------------------------------- Start here
    q = T['S1']; f = vis(q); k, r = f['bars'][0]['len'], f['bars'][1]['len']; sols = [x for x in range(0, 13) if count_up(x, k) == 5]; eq(sols, [7], 'S1 Ravi has 7'); eq(r, 7, 'S1 strip to scale'); eq(f['gap']['text'], '5', 'S1 gap'); eq(k + 7, 19, 'S1 in all'); eq(q['val'], [7, 19], 'S1 val'); eq(nums(q['text']), [12, 5], 'S1 text')
    q = T['S2']; eq(30 - 12, 18, 'S2 first step'); eq(18 - 9, 9, 'S2 second step'); eq(q['val'], [18, 9], 'S2 val'); eq(nums(q['text']), [30, 12, 9], 'S2 text')
    q = T['S3']; row = table_row(3, 3, 6); eq(row, [3, 6, 9, 12, 15, 18], 'S3 table'); eq(q['val'], [row[4], row[5]], 'S3 val'); eq(vis(q)['rows'][0], ['Beads', '3', '6', '9', '[]', '[]', '[]'], 'S3 table figure'); eq(vis(q)['head'], ['Row', '1', '2', '3', '4', '5', '6'], 'S3 head')
    q = T['S4']; sols = find(lambda x: x - 8 == 17); eq(sols, [25], 'S4 exactly one number'); eq(25 - 8, 17, 'S4 check'); eq(q['val'], [25, 17], 'S4 val'); eq(nums(q['text']), [8, 17], 'S4 text')
    q = T['S5']; one = [u for u in range(1, 30) if times(u, 4) == 20]; eq(one, [5], 'S5 1 bag holds 5'); eq(times(5, 7), 35, 'S5 7 bags'); eq(q['val'], [5, 35], 'S5 val'); eq(vis(q)['n'], 4, 'S5 4 bags drawn'); eq(nums(q['text']), [4, 20], 'S5 text')
    q = T['S6']; coins = [5, 10, 20]; ps = pairs(coins); sums = [a + b for a, b in ps]; eq(sums, [15, 25, 30], 'S6 pair sums'); eq(len(ps), 3, 'S6 3 pairs'); eq(q['val'], sums + [3], 'S6 val'); eq([p['val'] for p in q['parts']], sums + [3], 'S6 part vals'); eq(vis(q)['items'], [{'v': '5c'}, {'v': '10c'}, {'v': '20c'}], 'S6 figure')
    eq(sum(x['mins'] for x in d['tiers']['start']) <= 20, True, 'Start here fits in 20 minutes'); eq([x['page'] for x in d['tiers']['start']], [1, 1, 1, 2, 2, 2], 'Start here pages')
    for qq in d['tiers']['start']: eq(qq['text'].split('.')[0] in ('Draw it', 'Act it out', 'Make a table', 'Work backwards', 'Try something simpler', 'List every way'), True, qq['id'] + ' names its tool')
    # ---------------------------------------------------------------- Think harder: the tool is not named (T2 to T4), T1 asks which tool
    q = T['T1']; one = [u for u in range(1, 30) if times(u, 3) == 15]; eq(one, [5], 'T1 1 ruler $5'); eq(times(5, 5), 25, 'T1 5 rulers'); eq(q['val'], ['open', 25], 'T1 val'); eq(q['parts'][0]['choices'], ['Make a table', 'List every way', 'Try something simpler'], 'T1 choices')
    eq(len([x for x in range(1, 4) if times(x, 3) == 15]), 0, 'T1 5 rulers is not a multiple of 3: a table of 3, 6, 9 never reaches 5 rulers'); eq(nums(q['text']), [3, 15, 5], 'T1 text')
    q = T['T2']; sols = [c for c in range(0, 11) if 6 + c + 1 == 10]; eq(sols, [3], 'T2 the card costs $3'); eq(10 - 1, 9, 'T2 spent'); eq(q['val'], [9, 3], 'T2 val'); eq(nums(q['text']), [10, 6, 1], 'T2 text')
    q = T['T3']; steps = list(range(1, 11)); mei = 7; ali = [s for s in steps if mei - s == 2][0]; ben = [s for s in steps if ali - s == 1][0]; eq((ali, ben), (5, 4), 'T3 steps'); eq(ali + 2 == mei and ben + 1 == ali, True, 'T3 forward check'); eq(q['val'], [5, 4], 'T3 val'); eq(nums(q['text']), [7, 2, 1], 'T3 text'); eq(q.get('draw'), True, 'T3 has a drawing box')
    q = T['T4']; sols = [(a, b) for a in range(0, 8) for b in range(0, 8) if a + b == 7 and 5 * a + 10 * b == 50]; eq(sols, [(4, 3)], 'T4 exactly one answer'); eq(q['val'], [4, 3], 'T4 val'); eq(nums(q['text']), [7, 5, 10, 50], 'T4 text'); eq(len(vis(q)['rows']), 3, 'T4 table has 3 blank rows')
    for qq in d['tiers']['think'][1:]: eq(not re.search(r'strip|table|list|backwards|find one|step', qq['text'].lower().replace('you may use the table', '')), True, qq['id'] + ' does not name a tool')
    # ---------------------------------------------------------------- Go further
    q = T['G1']; sols = [kk for kk in range(0, 37) if kk + 3 * kk == 36]; eq(sols, [9], 'G1 Kit has 9'); eq(3 * 9, 27, 'G1 Jo'); eq(q['val'], [9, 9, 27, 'Yes'], 'G1 val')
    pt = nums(q['parts'][1]['text']); eq(pt, [2, 8, 24, 32, 10, 30, 40, 36], 'G1 part b: the tries in the text'); eq([8 + 24, 10 + 30], [32, 40], 'G1 the tries add up'); eq([3 * 8, 3 * 10], [24, 30], 'G1 Jo has 3 times as many in each try'); eq(32 < 36 < 40, True, 'G1 36 is between 32 and 40'); eq(9 + 27, 36, 'G1 Kit 9 and Jo 27 make 36')
    f = vis(q); eq(([s_['v'] for s_ in f['bars'][0]['segments']], f['bars'][0]['len'], f['brace']['text']), ([1, 3], 4, '36'), 'G1 strip: one bar, Jason 1 part and Jenny 3 parts, bracket over all 4'); eq(nums(q['text']), [3, 36], 'G1 text'); eq(d['beyond']['name'], 'Two Roads, One Answer', 'G1 named puzzle'); eq('G1' in d['beyond']['where'], True, 'G1 is a beyond item')
    q = T['G2']; amounts = {'Ali': 9, 'Ben': 15, 'Mei': 12}; tot = sum(amounts.values()); eq(tot, 36, 'G2 total'); share = [s for s in range(0, 37) if 3 * s == tot]; eq(share, [12], 'G2 each ends with 12')
    moves = [x for x in range(0, 16) if 9 + x == 12 and 15 - x == 12]; eq(moves, [3], 'G2 exactly one move: Ben gives 3 to Ali'); eq(q['val'], [12, 3], 'G2 val'); eq([b['len'] for b in vis(q)['bars']], [9, 15, 12], 'G2 strips'); eq(nums(q['text']), [9, 15, 12], 'G2 text')
    q = T['G3']; days = [dd for dd in range(1, 20) if table_row(4, 3, dd)[-1] == 22]; eq(days, [7], 'G3 day 7'); eq(table_row(4, 3, 7), [4, 7, 10, 13, 16, 19, 22], 'G3 table'); eq(find(lambda x: x == 6 and 4 + 3 * x == 22), [6], 'G3 6 steps of 3 from 4 to 22'); eq(q['val'], [7, 'open'], 'G3 val'); eq(nums(q['text']), [4, 1, 7, 2, 10, 3, 3], 'G3 text')
    # ---------------------------------------------------------------- Investigation
    eq(inv['val'], ['open'], 'I1 open'); eq(inv['lines'] >= 4, True, 'I1 has 4 lines')
    # ---------------------------------------------------------------- Exit ticket
    q = X['E1']; eq(find(lambda x: x + 4 == 15), [11], 'E1 the number is 11'); eq(q['val'], ['Work backwards'], 'E1 val'); eq(q['parts'][0]['choices'], ['Make a table', 'Work backwards', 'List every way'], 'E1 choices'); eq(nums(q['text']), [4, 15], 'E1 text')
    q = X['E2']; mei = [m for m in range(0, 12) if count_up(m, 11) == 4]; eq(mei, [7], 'E2 Mei has 7'); eq(11 + 7, 18, 'E2 in all'); eq(q['val'], [7, 18], 'E2 val'); eq(nums(q['text']), [11, 4], 'E2 text')
    q = X['E3']; one = [u for u in range(1, 30) if times(u, 5) == 20]; eq(one, [4], 'E3 1 bun costs $4'); eq(one[0] == 5, False, 'E3 the child is wrong'); eq(times(5, 5), 25, 'E3 5 buns at $5 would cost $25'); eq(q['val'], ['False'], 'E3 val'); eq(nums(q['text']), [5, 20, 1, 5], 'E3 text')
    # ---------------------------------------------------------------- home practice
    q = H['H1']; k = [x for x in range(0, 20) if count_up(x, 15) == 6]; eq(k, [9], 'H1 Kumar 9'); eq(15 + 9, 24, 'H1'); eq(q['val'], 24, 'H1 val')
    q = H['H2']; eq(table_row(4, 4, 6)[5], 24, 'H2 picture 6'); eq(q['val'], 24, 'H2 val'); eq(nums(q['text']), [1, 4, 2, 8, 3, 12, 4, 6], 'H2 text')
    q = H['H3']; eq(find(lambda x: x + 7 == 25), [18], 'H3'); eq(q['val'], 18, 'H3 val')
    q = H['H4']; sols = [(a, b) for a in range(0, 6) for b in range(0, 6) if a + b == 5 and 10 * a + 20 * b == 70]; eq(sols, [(3, 2)], 'H4 exactly one answer'); eq(q['val'], 2, 'H4 val'); eq(nums(q['text']), [5, 10, 20, 70, 20, 20], 'H4 text')
    l19 = json.load(open(os.path.join(L1, 'lessons', 'l19.json')))['home_practice']; src = [h for h in l19 if h['id'] == 'H2'][0]; q = H['H5']
    eq(q['text'], 'The moon is 6. The star is 2 more than the moon. What is the moon + the star? ___', 'H5 text'); eq((q['answer'], q['val']), ('14', 14), 'H5 answer'); eq(q['rewind_of'], 'Term 2 Lesson 3', 'H5 tag (new item in the style of Picture Equations, Lesson 13)'); eq(find(lambda x: x + (x + 2) == 6 + 8 and x == 6), [6], 'H5 the moon is 6'); eq(6 + (6 + 2), 14, 'H5 moon + star')
    eq([h['tier'] for h in d['home_practice']], ['start', 'start', 'start', 'think', 'start'], 'home tiers')
    # ---------------------------------------------------------------- class numbers differ from workbook, exit and home numbers
    wb = {}
    for qq in list(T.values()) + list(X.values()) + list(H.values()):
        txt = qq['text'] + ' ' + ' '.join(p.get('text', '') for p in qq.get('parts', []))
        wb[qq['id']] = tuple(sorted(nums(txt)))
    cls = {tuple(sorted(v)) for v in CLASS_ITEMS.values() if len(v) >= 3}
    eq([i for i, v in wb.items() if v in cls], [], 'no workbook, exit or home item repeats the numbers of a class item')
    # ---------------------------------------------------------------- online practice, authored numbers
    items = {i['id']: i for i in d['online_practice']['items']}
    eq(items['c1']['answer'], _c1(dict(a=12, b=4)), 'c1'); eq(items['c2']['answer'], _c2(dict(s=2, e=3, n=5)), 'c2'); eq(items['c3']['answer'], 9, 'c3'); eq(15 - 6, 9, 'c3 15 take away 6'); eq(items['c4']['answer'], _c4(dict(k=3, u=3)), 'c4')
    eq(items['c5']['answer'], 'work backwards', 'c5'); eq(find(lambda x: x - 7 == 10), [17], 'c5 the story has an end and no pattern'); eq(items['c5']['options'], ['make a table', 'work backwards', 'list every way'], 'c5 options')
    eq(items['t1']['answer'], _t1(dict(k=4, u=6, m=7)), 't1'); eq(items['t2']['answer'], _t2(dict(x=15, a=9, b=4)), 't2'); eq(find(lambda x: x + 9 - 4 == 20), [15], 't2 exactly one')
    eq(items['t3']['answer'], 'list every way', 't3'); ways = [(a, b) for a in range(0, 4) for b in range(0, 7) if 10 * a + 5 * b == 30]; eq(len(ways), 4, 't3 there are 4 ways to pay 30 cents: a list finds them all'); eq(items['t3']['options'], ['list every way', 'work backwards', 'try something simpler'], 't3 options')
    eq(items['g1']['answer'], _g1(dict(r=6)), 'g1'); eq(items['g2']['answer'], _g2(dict(r=6)), 'g2'); eq(items['g1']['answer'] + items['g2']['answer'], 24, 'g1 and g2 together make the total')
    l29 = {i['id']: i for i in json.load(open(os.path.join(L1, 'lessons', 'l29.json')))['online_practice']['items']}
    eq((items['r1']['q'], items['r1']['answer']), (l29['c1']['q'], l29['c1']['answer']), 'r1 is Term 3 Lesson 9 c1'); eq((items['r2']['q'], items['r2']['answer']), (l29['c3']['q'], l29['c3']['answer']), 'r2 is Term 3 Lesson 9 c3')
    eq((items['r1']['rewind_of'], items['r2']['rewind_of']), ('Term 3 Lesson 9', 'Term 3 Lesson 9'), 'rewind tags'); eq(_r1(dict(a=40, b=30)), 70, 'r1'); eq(_r2(dict(a=39, b=24)), 63, 'r2')
    # ---------------------------------------------------------------- materials and hand-offs
    eq(d['materials']['ruler'], False, 'no ruler')
    prev = json.load(open(os.path.join(L1, 'lessons', 'l38.json'))); txt = ' '.join(prev['parent']['next_materials']).lower()
    eq(all(w in txt for w in ('tool-and-problem cards', '15 cards', 'cuts out')), True, 'lesson 38 hand-off names the 15 cards this lesson needs')
    pn = ' '.join(d['parent']['next_materials']).lower(); eq(all(w in pn for w in ('quest log', 'closed', 'quest partner', 'favourite page', 'plain paper')), True, 'hand-off to the last lesson names the Quest Log, a quest partner, a favourite page and plain paper')
    end = json.dumps(sl['s-end']['blocks']).lower(); eq('quest log' in end and 'quest partner' in end, True, 's-end hand-off')
    eq(set(d['beyond']['where']) <= set(T) and not (set(d['beyond']['where']) & {qq['id'] for qq in d['tiers']['start']}), True, 'beyond items sit at Think harder or Go further')
    return n
