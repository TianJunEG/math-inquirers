"""Independent answer checks for Level 1 Term 3 Lesson 10 (Lesson 30, Tool Detectives, and Mi's Challenge Quest).

This lesson replaces the old Lesson 30 (Calendar Detective, now Lesson 27). Every number is recomputed here by stepping, listing or simulating (not by the lesson's own formula): clock times by counting minutes, money left
by counting back, which two tags make an exact amount by trying every pair, linear patterns by adding step by step, the 5-cent and 10-cent coin puzzles by trying every split, the pet puzzle by trying all six
assignments against the clues, the cycle of 3 days on a week of 7 by stepping day by day, the wrong sum by recomputing it, and the Quest gates one by one (clock hands, coins, prices, calendar, sticks counted from the
drawing, the wrong sum, the two mixed gates and the cave ways for $14). Class items (warm-up, sneak-peek, Explore, Mini-lesson, Talk) are listed and checked to differ from the workbook, exit ticket, home items and the
Quest gates. Online practice templates get brute-force oracles. The kit contract and hand-offs are checked against the neighbouring lessons.
"""
import itertools
import json
import os
import re

L1 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WEEK = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


def later(day, n):
    i = WEEK.index(day)
    for _ in range(n):
        i += 1
        if i == 7:
            i = 0
    return WEEK[i]


def plus(a, b):
    n = a
    for _ in range(b):
        n += 1
    return n


def minus(a, b):
    n = a
    for _ in range(b):
        n -= 1
    return n


def nums(text):
    return [int(x) for x in re.findall(r'\d+', text)]


def add_minutes(h, m, mins):
    """Clock time after mins minutes, stepping one minute at a time (12-hour clock)."""
    for _ in range(mins):
        m += 1
        if m == 60:
            m = 0
            h += 1
            if h == 13:
                h = 1
    return h, m


def fmt(t):
    return f'{t[0]}:{t[1]:02d}'


def ways(target, prices):
    return [c for c in itertools.product(range(target + 1), repeat=len(prices)) if sum(x * p for x, p in zip(c, prices)) == target]


def pairs_with_total(tags, total):
    return [c for c in itertools.combinations(tags, 2) if sum(c) == total]


def linear(first, step, n):
    """The n-th term of a pattern that adds `step` each time, built by adding one step at a time."""
    v = first
    for _ in range(n - 1):
        v = plus(v, step)
    return v


def coin_splits(count, total, a=5, b=10):
    return [(x, count - x) for x in range(count + 1) if x * a + (count - x) * b == total]


def pets():
    sols = []
    for perm in itertools.permutations(['cat', 'fish', 'bird']):
        mei, ali, ben = perm
        if ali == 'fish' and mei != 'cat':
            sols.append(perm)
    return sols


def triangle_sticks(n):
    edges = set()
    for j in range(n):
        for a, b in ((j, j + 1), (j + 1, j + 2), (j, j + 2)):
            edges.add((a, b))
    return len(edges)


def coin_total(vs):
    t = 0
    for v in vs:
        t = plus(t, int(v.rstrip('c')))
    return t


def _c1(e): return minus(e['m'], e['b'])
def _c2(e): return e['h'] + 1
def _c4(e): return linear(e['a'], e['d'], 4)
def _c5(e): return sum(e['p'] for _ in range(e['n']))
def _t1(e): return plus(e['l'], e['e'])
def _t3(e): return linear(e['a'], 3, e['n'])


ORACLES = {'c1': _c1, 'c2': _c2, 'c4': _c4, 'c5': _c5, 't1': _t1, 't3': _t3}
BASE_ENV = {'c1': dict(m=15, b=6), 'c2': dict(h=3), 'c4': dict(a=2, d=3), 'c5': dict(n=3, p=4), 't1': dict(e=5, l=8), 't3': dict(a=4, n=5)}

# class items and the items of the workbook, exit ticket, home and Quest, as (kind, ...) tuples; none may repeat
CLASS = {
    'remember': [('diff', 9, 5), ('back', 4, 11), ('next', 3, 3)],
    'sneak': [('days', 'Monday', 3), ('back', 6, 15)],
    'explore': [('film', 3, 30, 60), ('pair', 12), ('stars', 2, 8), ('back', 7, 12), ('coins', 4, 30), ('days', 'Wednesday', 10)],
    'mini': [('left', 15, 10), ('squares', 4, 8)],
    'talk': [('pattern20',)],
    'opt': [('notes', 3, 2, 10)],
}
WORKBOOK = {
    'S1': [('film', 7, 30, 60), ('film', 3, 0, 30)], 'S2': [('left', 20, 13)], 'S3': [('pair', 15)], 'S4': [('next', 5, 3, 4)], 'S5': [('days', 'Thursday', 6)], 'S6': [('sumcheck', 63, 28)],
    'T1': [('back', 7, 9)], 'T2': [('steps', 3, 4, 8)], 'T3': [('pets',)], 'T4': [('coins', 5, 35)],
    'G1': [('buy', 30)], 'G2': [('mix', 3, 5, 4, 16)], 'G3': [('swims', 'Monday', 3)],
    'E1': [('film', 4, 0, 30)], 'E2': [('left', 20, 12)], 'E3': [('back', 3, 8)],
    'H1': [('left', 20, 9)], 'H2': [('pair', 13)], 'H3': [('film', 9, 0, 30)], 'H4': [('next', 4, 2, 6)], 'H5': [('story', 52, 20, 7)],
}
QUEST = {'C1': ('clock', 4, 35), 'C2': ('coins', 95), 'C3': ('prices', 6, 9), 'C4': ('days', 'Friday', 3), 'C5': ('sticks',), 'C6': ('sum', 49, 38, 77), 'C7': ('first', 9, 6), 'C8': ('coins', 4, 25), 'cave': ('ways', 14)}


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
    cq = d['challenge_quest']
    G = {q['id']: q for q in cq['questions']}

    # ---------------------------------------------------------------- registries
    allcls = [p for v in CLASS.values() for p in v]
    allwb = [p for v in WORKBOOK.values() for p in v]
    eq(len(set(allcls)), len(allcls), 'class items are all different')
    eq(len(set(allwb)), len(allwb), 'workbook items are all different')
    eq(sorted(set(allcls) & set(allwb), key=str), [], 'no workbook, exit or home item repeats a class item')
    eq(sorted((set(allcls) | set(allwb)) & set(QUEST.values()), key=str), [], 'no class or workbook item is a Quest gate')
    eq([p for p in allcls + allwb if p[0] == 'coins' and p[1:] in ((4, 25), (5, 35))], [('coins', 5, 35)], 'only T4 uses the 5-coin puzzle')

    # ---------------------------------------------------------------- warm-up
    eq((minus(9, 5), plus(4, 4) == 8 and minus(11, 4) == 7), (4, True), 'remember 1 and 2'); eq(plus(7, 4), 11, 'remember 2 forwards check')
    s = sl['s-rem2']['blocks'][0]; eq([b['len'] for b in s['bars']], [9, 5], 's-rem2 bars')
    s = sl['s-rem3']['blocks'][0]; eq((s['hide'], s['jumps']), ([7], [[7, 11, '+4']]), 's-rem3 number line')
    s = sl['s-rem4']['blocks'][0]; eq((s['items'], [linear(3, 3, k) for k in (1, 2, 3, 4)]), ([3, 6, 9, None], [3, 6, 9, 12]), 's-rem4 pattern')
    eq([r[0] for r in sl['s-rem1']['blocks'][0]['rows']], ['Draw it', 'Act it out', 'Spot the pattern', 'List every way', 'Make a table', 'Work backwards', 'Guess and check'], 's-rem1 lists the seven card names')
    # ---------------------------------------------------------------- sneak-peek
    sp = d['sneak_peek']; eq(later('Monday', 3), 'Thursday', 'sneak 1'); eq(minus(15, 6), 9, 'sneak 2'); eq(plus(9, 6), 15, 'sneak 2 check'); eq((sp['val1'], sp['a2'][:1]), ('Thursday', '9'), 'sneak answers')
    # ---------------------------------------------------------------- Explore (nobody solves: the answers are for the tutor)
    eq(fmt(add_minutes(3, 30, 60)), '4:30', 'explore film'); eq(pairs_with_total((3, 5, 8, 9), 12), [(3, 9)], 'explore card 2 has exactly one pair')
    eq(linear(2, 2, 8), 16, 'explore stars row 8'); eq(minus(12, 0) + 7, 19, 'explore card 4: 19 take away 7 is 12'); eq(minus(19, 7), 12, 'explore card 4 check')
    eq(coin_splits(4, 30), [(2, 2)], 'explore card 5: one split'); eq(later('Wednesday', 10), 'Saturday', 'explore card 6')
    # ---------------------------------------------------------------- Mini-lesson
    eq(minus(minus(15, 6), 4), 5, 'm2 backwards'); eq(plus(plus(6, 4), 5), 15, 'm2 third check'); b = sl['s-m1']['blocks'][0]['bars'][0]['segments']; eq([x['v'] for x in b], [6, 4, 5], 's-m1 strip parts'); eq(sum(x['v'] for x in b), 15, 's-m1 strip total')
    eq([triangle_sticks(1) + 0], [3], 'triangle row check (gate 5 uses it)')
    sq = [linear(4, 3, k) for k in range(1, 9)]; eq(sq, [4, 7, 10, 13, 16, 19, 22, 25], 's-m3 table'); eq(sl['s-m3-ans']['blocks'][0]['rows'][0][1:], [str(x) for x in sq], 's-m3-ans row'); eq(plus(4, 21), 25, 's-m3 check another way')
    eq((sl['s-m3']['blocks'][0]['shape'], sl['s-m3']['blocks'][0]['n']), ('square', 3), 's-m3 picture')
    # ---------------------------------------------------------------- Start here
    q = T['S1']; eq((fmt(add_minutes(7, 30, 60)), fmt(add_minutes(3, 0, 30))), ('8:30', '3:30'), 'S1'); eq((q['visual']['h'], q['visual']['m']), (7, 30), 'S1 clock'); eq(q['val'], ['8:30', '3:30'], 'S1 val')
    q = T['S2']; eq((minus(20, 13), plus(7, 13)), (7, 20), 'S2 and its check'); eq(q['val'], [7], 'S2 val')
    q = T['S3']; eq(pairs_with_total((5, 7, 8, 12), 15), [(7, 8)], 'S3 exactly one pair'); eq(q['val'], [7, 8], 'S3 val'); eq([v['price'] for v in q['visuals']], ['$5', '$7', '$8', '$12'], 'S3 tags')
    q = T['S4']; eq([linear(5, 3, k) for k in (1, 2, 3, 4)], [5, 8, 11, 14], 'S4'); eq(q['visual']['rows'][0], ['Tiles', '5', '8', '11', '[]'], 'S4 table'); eq(q['val'], [14], 'S4 val')
    q = T['S5']; eq([later('Thursday', k) for k in range(1, 7)], ['Friday', 'Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday'], 'S5 stepped'); eq(q['val'], ['Wednesday'], 'S5 val')
    q = T['S6']; eq((plus(45, 28), minus(63, 28), 45 == minus(63, 28), plus(35, 28)), (73, 35, False, 63), 'S6'); eq(q['val'], [73, 'No', 35], 'S6 val')
    eq(sum(x['mins'] for x in d['tiers']['start']) <= 20, True, 'Start here within 20 minutes')
    eq(all(any(p['text'].startswith('Tool I used') for p in x['parts']) for x in d['tiers']['start']), True, 'every Start here question has the tool and I checked line')
    # ---------------------------------------------------------------- Think harder
    q = T['T1']; eq((plus(9, 7), minus(16, 7), plus(16, 0)), (16, 9, 16), 'T1 both tools and check'); eq(q['val'], [16, 16], 'T1 val')
    q = T['T2']; row = [linear(3, 4, k) for k in range(1, 9)]; eq(row, [3, 7, 11, 15, 19, 23, 27, 31], 'T2 steps'); eq(q['visual']['rows'][0], ['Blocks', '3', '7', '11', '[]', '[]', '23'], 'T2 table'); eq((row[3], row[4], row[5], row[7]), (15, 19, 23, 31), 'T2 values'); eq(q['val'], [15, 19, 31], 'T2 val')
    q = T['T3']; eq(pets(), [('bird', 'fish', 'cat')], 'T3 exactly one assignment (Mei, Ali, Ben)'); eq(q['val'], ['bird', 'cat'], 'T3 val'); eq([r[0] for r in q['visual']['rows']], ['Mei', 'Ali', 'Ben'], 'T3 table rows'); eq(q['visual']['head'], ['', 'cat', 'fish', 'bird'], 'T3 columns')
    q = T['T4']; eq(2 * 5 + 3 * 10, 40, 'T4a'); eq(coin_splits(5, 35), [(3, 2)], 'T4 exactly one split'); eq(q['val'], [40, 'Too high', 3, 2], 'T4 val')
    # ---------------------------------------------------------------- Go further
    q = T['G1']; eq((plus(6, 6), minus(minus(30, 12), 9)), (12, 9), 'G1'); eq(plus(plus(12, 9), 9), 30, 'G1 check'); eq(q['val'], [12, 9], 'G1 val')
    q = T['G2']; eq([c for c in itertools.product(range(5), repeat=2) if c[0] + c[1] == 4 and 3 * c[0] + 5 * c[1] == 16], [(2, 2)], 'G2 exactly one answer'); eq(q['val'], [2, 2], 'G2 val')
    q = T['G3']; sw = ['Monday']
    for _ in range(4): sw.append(later(sw[-1], 3))
    eq(sw, ['Monday', 'Thursday', 'Sunday', 'Wednesday', 'Saturday'], 'G3 swims'); eq(later('Monday', 12), 'Saturday', 'G3 twelve days'); eq(q['val'], ['Thursday', 'Saturday'], 'G3 val')
    eq(inv['tier'], 'investigation', 'I1'); eq(plus(7, 4), 11, 'I1 example answer')
    # ---------------------------------------------------------------- talk, exit, home
    eq(linear(4, 3, 20), 61, 'talk: the 20th picture by adding'); eq(4 + 19 * 3, 61, 'talk: 4 and 19 lots of 3')
    eq(fmt(add_minutes(4, 0, 30)), '4:30', 'E1'); eq(X['E1']['val'], ['4:30'], 'E1 val')
    eq(minus(20, 12), 8, 'E2'); eq([nums(o)[0] for o in X['E2']['mcq']['options']], [6, 8, 10, 32], 'E2 options'); eq(X['E2']['val'], [2], 'E2 val'); eq(plus(8, 12), 20, 'E2 check')
    eq(plus(8, 3), 11, 'E3'); eq(X['E3']['val'], [11], 'E3 val')
    eq(minus(20, 9), 11, 'H1'); eq(H['H1']['val'], 11, 'H1 val'); eq(pairs_with_total((4, 5, 7, 9), 13), [(4, 9)], 'H2'); eq(H['H2']['val'], [4, 9], 'H2 val')
    eq(fmt(add_minutes(9, 0, 30)), '9:30', 'H3'); eq(H['H3']['val'], '9:30', 'H3 val'); eq(linear(4, 2, 6), 14, 'H4'); eq(H['H4']['val'], 14, 'H4 val')
    eq(plus(minus(52, 20), 7), 39, 'H5'); eq(H['H5']['val'], 39, 'H5 val'); eq(H['H5'].get('rewind_of'), 'Term 1 Lesson 10', 'H5 is the rewind item')
    eq(plus(minus(3 * 5 + 2 * 2, 10), 0), 9, 'optional slide: 19 take away 10')
    # ---------------------------------------------------------------- Quest gates
    q = G['C1']; eq((q['visual']['h'], q['visual']['m']), (4, 35), 'C1 clock'); eq(abs((4 + 35 / 60) - 4.5833) < 0.001, True, 'C1 hour hand'); eq(35 // 5, 7, 'C1 long hand on the 7'); eq(fmt(add_minutes(2, 30, 30)), '3:00', 'C1c'); eq(q['val'], ['4:35', 'am', '3:00'], 'C1 val')
    q = G['C2']; eq(coin_total(['50c', '20c', '20c', '5c']), 95, 'C2 coins'); eq(q['visual']['items'], [{'v': '50c'}, {'v': '20c', 'n': 2}, {'v': '5c'}], 'C2 picture'); eq(minus(10, 7), 3, 'C2 change'); eq(q['val'], [95, 3], 'C2 val')
    q = G['C3']; eq((minus(9, 6), max(6, 9)), (3, 9), 'C3 more'); eq([c for c in itertools.combinations((4, 5, 6), 2) if sum(c) == 10], [(4, 6)], 'C3 exactly one pair'); eq(q['val'], ['ruler', 3, 4, 6], 'C3 val')
    q = G['C4']; month = {1: 'Wednesday'}
    for k in range(2, 32): month[k] = later(month[k - 1], 1)
    eq(later('Friday', 3), 'Monday', 'C4a'); eq((plus(3, 7), month[3], month[10]), (10, 'Friday', 'Friday'), 'C4b'); eq(q['val'], ['Monday', 10], 'C4 val'); eq(q['visual']['highlight'], [3], 'C4 highlight')
    q = G['C5']; eq([triangle_sticks(k) for k in (1, 2, 3, 4, 5)], [3, 5, 7, 9, 11], 'C5 sticks counted from the drawing'); eq(q['val'], [9, 11], 'C5 val')
    q = G['C6']; eq(plus(49, 38), 87, 'C6'); eq(plus(49, 38) == 77, False, 'C6 77 is wrong'); eq(minus(77, 38), 39, 'C6 check'); eq(q['val'], ['No', 87], 'C6 val')
    q = G['C7']; eq((plus(9, 6), minus(9, 4)), (15, 5), 'C7'); eq(q['val'], [15, 5], 'C7 val')
    q = G['C8']; eq(coin_splits(4, 25), [(3, 1)], 'C8 exactly one split'); eq(q['val'], [3, 1], 'C8 val')
    c = cq['optional']; eq(sorted(ways(14, (2, 5))), [(2, 2), (7, 0)], 'cave exactly two ways'); eq(c['val'], [7, 0], 'cave val')
    eq([g['page'] for g in cq['questions']], [1, 1, 2, 2, 3, 3, 4, 4], 'gates per page'); eq(cq['sheet_pages'], 4, 'quest log pages'); eq(cq['tool_row'], 'term', 'Quest v2 tool row')
    eq([g['lesson'] for g in cq['questions'] if g['lesson'] == 'mixed'], ['mixed', 'mixed'], 'two mixed gates')
    covered = sorted({n_ for g in cq['questions'] for n_ in (g['lesson'] if isinstance(g['lesson'], list) else [g['lesson']]) if n_ != 'mixed'})
    eq(covered, [21, 22, 23, 24, 25, 26, 27, 28, 29], 'every content lesson of the term is visited by a gate')
    eq(sorted(q_ for s_ in cq['strands'] for q_ in s_['questions']), sorted(g['id'] for g in cq['questions']), 'every gate is in a strand')
    eq(any('tally' in x and 'not even in your own notes' in x for x in cq['privacy_checklist']), False, 'old privacy line is gone')
    eq(any('no tally or count of any kind' in x for x in cq['privacy_checklist']), True, 'new privacy line')
    toolwords = ('draw it', 'act it out', 'spot the pattern', 'list every way', 'make a table', 'work backwards', 'guess and check')
    eq([w for g in cq['questions'] for w in toolwords if w in json.dumps([g['text'], g['parts'], g['say']]).lower()], [], 'no Quest gate names a tool')
    # ---------------------------------------------------------------- online practice
    items = {i['id']: i for i in d['online_practice']['items']}
    for cid, env in BASE_ENV.items(): eq(items[cid]['answer'], ORACLES[cid](env), cid + ' authored answer')
    eq((items['g1']['answer'], [c_[1] for c_ in itertools.product(range(5), repeat=2) if c_[0] + c_[1] == 4 and 3 * c_[0] + 5 * c_[1] == 16]), (2, [2]), 'g1')
    eq((items['g2']['answer'], later(later('Monday', 3), 3)), ('Sunday', 'Sunday'), 'g2')
    eq(items['c3']['answer'], 'Work backwards', 'c3'); eq(items['t2']['answer'], 'Make a table', 't2')
    for it in items.values():
        for s_ in it.get('slips', []):
            if it['type'] == 'number': eq(it['answer'] in s_['a'], False, it['id'] + ' slip is wrong')
        if it['type'] == 'choice': eq(it['answer'] in it['options'], True, it['id'] + ' answer is an option')
    for m_, b_ in itertools.product(items['c1']['tpl']['vars']['m'], items['c1']['tpl']['vars']['b']): eq(m_ > b_, True, f'c1 {m_} {b_}')
    for e_, l_ in itertools.product(items['t1']['tpl']['vars']['e'], items['t1']['tpl']['vars']['l']): eq(e_ + l_ <= 20, True, f't1 {e_} {l_}')
    for h_ in items['c2']['tpl']['vars']['h']: eq(h_ + 1 <= 11, True, f'c2 {h_}')
    for it in items.values():
        tp = it.get('tpl')
        if tp: eq(re.search(r'\{\w+\}th', json.dumps(tp)), None, it['id'] + ' template never writes {a}th')
    # ---------------------------------------------------------------- kit contract, hand-offs
    kc = {r['piece']: r for r in d['materials']['kit_contract']}
    for r in kc.values(): eq(r['supplied'] >= r['max_used'], True, 'kit contract ' + r['piece'])
    eq((kc['tool cards']['supplied'], len(d['workbook']['kits'][0]['labels'])), (7, 7), 'seven tool cards'); eq(d['workbook']['kits'][0]['labels'], [r[0] for r in sl['s-rem1']['blocks'][0]['rows']], 'cards match the toolbox page')
    nm = ' '.join(d['parent']['next_materials']).lower(); eq(('term 4' in nm and 'cut' in nm), True, 'hand-off to Term 4 names the book and the cut-out')
    p29 = json.load(open(os.path.join(L1, 'lessons', 'l29.json'), encoding='utf-8')); pm = ' '.join(p29['parent']['next_materials']).lower()
    mk = ' '.join(d['materials']['child']).lower()
    eq(all(w_ in pm for w_ in ('quest log', 'quest partner', 'tool-card page', '7 tool cards')) and all(w_ in mk for w_ in ('quest log', 'quest partner', 'tool cards')), True, 'Lesson 29 hand-off matches this lesson\'s materials')
    return n
