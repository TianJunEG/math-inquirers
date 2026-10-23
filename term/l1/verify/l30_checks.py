"""Independent answer checks for Level 1 Term 3 Lesson 10 (Lesson 30, Calendar Detective, and Mi's Challenge Quest).

Every day, date and count in l30.json is recomputed here by stepping ONE DAY AT A TIME round the week (not by a modulo formula in the lesson): 'n days later', 'the day before', the weekday
of each date on the made-up month page (the 1st is a Wednesday, 31 days), a week and a fortnight later, the 10th day from Monday, 100 days later (stepped, then compared with 14 weeks and
2 days), every Wednesday of the month, and how many times each weekday occurs in the month (Wednesday, Thursday and Friday five times). The Quest gates are recomputed too: the clock hands
for 4:35, the coins (95 cents), the change, the two prices, the 3 by 3 grid (every row and column holds one of each shape), the stick counts for triangles (counted from the drawing's
points), the wrong sum and the cave ways for $14. Class items (warm-up, sneak-peek, Explore, Mini-lesson, Talk) are listed and checked to differ from the workbook, exit ticket, home
items and the Quest gates. Online practice templates get brute-force oracles; kit contract and hand-offs are checked against the neighbouring lessons.
"""
import itertools
import json
import os
import re

L1 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WEEK = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


def later(day, n):
    """The day n days later, stepping one day at a time."""
    i = WEEK.index(day)
    for _ in range(n):
        i += 1
        if i == 7:
            i = 0
    return WEEK[i]


def before(day, n=1):
    i = WEEK.index(day)
    for _ in range(n):
        i -= 1
        if i < 0:
            i = 6
    return WEEK[i]


def weekday_of_date(date, first='Wednesday'):
    """Weekday of a date in a month whose 1st is `first`, stepping from the 1st."""
    d = first
    for _ in range(date - 1):
        d = later(d, 1)
    return d


def dates_on(day, first='Wednesday', length=31):
    return [n for n in range(1, length + 1) if weekday_of_date(n, first) == day]


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


def ways(target, prices):
    out = []
    for combo in itertools.product(range(target + 1), repeat=len(prices)):
        if sum(c * p for c, p in zip(combo, prices)) == target:
            out.append(combo)
    return out


def triangle_sticks(n):
    """Sticks in n triangles in a row, counted from the zigzag points: the points alternate bottom, top; each triangle j uses edges (j,j+1), (j+1,j+2), (j,j+2)."""
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


QUEST = {'C1': ('clock', 4, 35), 'C2': ('later', 2, 30, 30), 'C3': ('coins', 95), 'C4': ('prices', 6, 9), 'C5': ('grid',), 'C6': ('sticks',), 'C7': ('sum', 49, 38, 77), 'C8': ('days', 'Friday', 3), 'cave': ('ways', 14)}
CLASS = {
    'remember': [('seq7', 3), ('seq7', 5), ('ordinal', 3), ('order',)],
    'sneak': [('days', 'Monday', 1), ('days', 'Thursday', 5)],
    'explore': [('days', 'Tuesday', 5), ('days', 'Sunday', 3), ('week', 5), ('after', 'Sunday')],
    'mini': [('days', 'Thursday', 4), ('before', 'Monday'), ('week', 9), ('fortnight', 4), ('week', 2), ('after', 'Friday'), ('before', 'Thursday')],
    'break': [('seq7', 7)],
    'talk': [('days', 'Monday', 10)],
    'opt': [('date', 15)],
}
WORKBOOK = {
    'S1': [('missing', 'Wednesday', 'Saturday')], 'S2': [('before', 'Wednesday'), ('after', 'Saturday')], 'S3': [('days', 'Tuesday', 3)], 'S4': [('days', 'Saturday', 2)], 'S5': [('week', 6)],
    'S6': [('tfday', 1), ('tfday', 2), ('tfday', 3), ('tfday', 4)],
    'T1': [('yesterday2', 'Thursday')], 'T2': [('dayn', 'Monday', 7), ('dayn', 'Monday', 10)], 'T3': [('weeks', 3), ('weeks', 2)], 'T4': [('date', 18), ('week', 18)],
    'G1': [('days', 'Monday', 100)], 'G2': [('wednesdays',), ('date', 31)], 'G3': [('weeks', 3, 6)], 'I1': [('five',)],
    'E1': [('days', 'Sunday', 2)], 'E2': [('week', 11)], 'E3': [('week', 4)],
    'H1': [('days', 'Wednesday', 4)], 'H2': [('date', 10)], 'H3': [('week', 14), ('fortnight', 14)], 'H4': [('days', 'Saturday', 9)], 'H5': [('steps', 36, 10, 4)],
}


def _c1(e): return plus(e['a'], 7)
def _c2(e): return 7 * e['w']
def _c5(e): return plus(e['s'], 21)
def _t1(e): return plus(e['a'], 14)
def _t3(e): return 14 * e['w']
def _g1(e):
    # the Mondays of a 31-day month when the a-th is a Monday: list them
    return len([n for n in range(e['a'], 32, 7)])


ORACLES = {'c1': _c1, 'c2': _c2, 'c5': _c5, 't1': _t1, 't3': _t3, 'g1': _g1}
BASE_ENV = {'c1': dict(a=5), 'c2': dict(w=2), 'c5': dict(s=3), 't1': dict(a=4), 't3': dict(w=2), 'g1': dict(a=2)}


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
    qset = set(QUEST.values())
    eq(sorted((set(allcls) | set(allwb)) & qset, key=str), [], 'no class or workbook item is a Quest gate')
    # class items that are plain 'week of date' also must not equal the gate (3 -> 10)
    eq(any(p == ('week', 3) for p in allcls + allwb), False, 'no class or workbook item uses the gate date (the 3rd)')

    # ---------------------------------------------------------------- the calendar itself
    eq([later(WEEK[0], k) for k in range(8)], WEEK + ['Monday'], 'after Sunday comes Monday')
    eq(before('Monday'), 'Sunday', 'before Monday')
    for dn in WEEK: eq(later(dn, 7), dn, f'a week later than {dn} is {dn}')
    eq(weekday_of_date(1), 'Wednesday', 'the 1st is a Wednesday')
    month = {k: weekday_of_date(k) for k in range(1, 32)}
    eq([month[k + 7] == month[k] for k in range(1, 25)], [True] * 24, 'a week later is the same weekday for every date')
    eq(sl['s-explore3']['blocks'][0]['highlight'], [5], 's-explore3 highlights the 5th'); eq(sl['s-explore3']['blocks'][0]['start'], 'Wed', 's-explore3 month starts on a Wednesday')
    # ---------------------------------------------------------------- warm-up
    s = sl['s-rem1']['blocks'][0]; eq(s['items'], [3, 10, 17, None], 's-rem1 items'); eq((plus(3, 7), plus(10, 7), plus(17, 7)), (10, 17, 24), 's-rem1 count in 7s'); eq(s['gaps'], ['+7'] * 3, 's-rem1 gaps')
    eq(plus(plus(5, 7), 7), 19, 's-rem1 your turn: 5, 12, 19')
    eq(len(sl['s-rem2']['blocks'][0].get('highlight', [])), 1, 's-rem2 one highlighted child'); eq(sl['s-rem2']['blocks'][0]['highlight'], [2], 's-rem2 third place (index 2)')
    tb = sl['s-rem3']['blocks'][0]['rows']; eq([c for r in tb for c in r][:7], WEEK, 's-rem3 days in order'); eq(tb[1][3], '?', 's-rem3 the blank after Sunday')
    # ---------------------------------------------------------------- sneak-peek
    sp = d['sneak_peek']; eq(later('Monday', 1), 'Tuesday', 'sneak 1'); eq(later('Thursday', 5), 'Tuesday', 'sneak 2'); eq((sp['a1'], sp['a2'].split('.')[0]), ('Tuesday.', 'Tuesday'), 'sneak answers')
    eq([later('Thursday', k) for k in range(1, 6)], ['Friday', 'Saturday', 'Sunday', 'Monday', 'Tuesday'], 'sneak 2 count on')
    eq(later('Thursday', 0 + 1 - 1 + 4), 'Monday', 'a child who counts Thursday as day 1 gets Monday')
    # ---------------------------------------------------------------- Explore
    eq(later('Tuesday', 5), 'Sunday', 'explore 2a'); eq(later('Sunday', 3), 'Wednesday', 'explore 2b'); eq(sl['s-explore2-ans']['blocks'][0]['rows'][1:], [['Tuesday', '5', 'Sunday'], ['Sunday', '3', 'Wednesday']], 's-explore2-ans')
    eq((plus(5, 7), month[12], month[5]), (12, 'Sunday', 'Sunday'), 'explore 3: the 12th is a week after the 5th, both Sundays'); eq(sl['s-explore3-ans']['blocks'][0]['highlight'], [5, 12], 's-explore3-ans')
    eq([k for k in range(1, 32) if month[k] == 'Sunday'], [5, 12, 19, 26], 'explore 4: the Sundays')
    row = sl['s-explore1-ans']['blocks'][0]['rows']; eq(row[0], ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun', 'Mon'], 's-explore1-ans row')
    # ---------------------------------------------------------------- Mini-lesson
    eq(later('Thursday', 4), 'Monday', 's-m1'); eq(later('Wednesday', 6), 'Tuesday', 'not used in class any more but still true')
    eq(before('Monday'), 'Sunday', 's-m2'); eq((later('Friday', 1), before('Thursday')), ('Saturday', 'Wednesday'), 's-m2 your turn'); eq((month[15], plus(1, 14)), ('Wednesday', 15), 's-opt: the 15th is a Wednesday')
    eq((sl['s-m3']['blocks'][0]['highlight'], plus(9, 7), month[9], month[16]), ([9], 16, 'Thursday', 'Thursday'), 's-m3')
    eq(plus(2, 7), 9, 's-m3 your turn: a week after the 2nd')
    eq((sl['s-m4']['blocks'][0]['highlight'], plus(4, 14), month[4], month[18]), ([4], 18, 'Saturday', 'Saturday'), 's-m4'); eq((7 * 2, plus(4, 7), plus(plus(4, 7), 7)), (14, 11, 18), 's-m4 steps')
    eq((7, 14), (7 * 1, 7 * 2), 's-m4 your turn: a week is 7 days and a fortnight 14')
    # ---------------------------------------------------------------- Start here
    q = T['S1']; eq(q['visual']['rows'][0], ['Monday', 'Tuesday', '[]', 'Thursday', 'Friday', '[]', 'Sunday'], 'S1 table'); eq([WEEK[i] for i in (2, 5)], q['val'], 'S1 missing days')
    eq([d_ for d_ in WEEK if d_ not in ('Monday', 'Tuesday', 'Thursday', 'Friday', 'Sunday')], ['Wednesday', 'Saturday'], 'S1 recomputed')
    q = T['S2']; eq((before('Wednesday'), later('Saturday', 1)), ('Tuesday', 'Sunday'), 'S2'); eq(q['val'], ['Tuesday', 'Sunday'], 'S2 val')
    q = T['S3']; eq(later('Tuesday', 3), 'Friday', 'S3'); eq(later('Tuesday', 5), 'Sunday', 'S3b'); eq(q['val'], ['Friday', 'Sunday'], 'S3 val'); eq(q['visual']['rows'][0][1], 'today', 'S3 marks today')
    q = T['S4']; eq(later('Saturday', 2), 'Monday', 'S4'); eq(q['val'], ['Monday'], 'S4 val')
    q = T['S5']; eq(q['visual']['highlight'], [6], 'S5 highlight'); eq((7, plus(6, 7), month[6], month[13]), (7, 13, 'Monday', 'Monday'), 'S5'); eq(q['val'], [7, 13], 'S5 val')
    q = T['S6']; st = [x['s'] for x in q['tf']]
    truth = [later('Sunday', 1) == 'Monday', before('Thursday') == 'Friday', WEEK.index('Wednesday') == WEEK.index('Tuesday') + 1 == WEEK.index('Thursday') - 1, before('Sunday') == 'Saturday']
    eq(truth, [True, False, True, True], 'S6 truth values'); eq(q['val'], ['True', 'False', 'True', 'True'], 'S6 val'); eq(len(st), 4, 'S6 four statements')
    eq(sum(x['mins'] for x in d['tiers']['start']) <= 20, True, 'Start here within 20 minutes')
    # ---------------------------------------------------------------- Think harder
    q = T['T1']; yd = before('Thursday'); dby = before(yd); eq((yd, dby, later(dby, 2)), ('Wednesday', 'Tuesday', 'Thursday'), 'T1a is today'); tm = later('Thursday', 1); eq((tm, before(tm, 2)), ('Friday', 'Wednesday'), 'T1b'); eq(q['val'], ['Thursday', 'Wednesday'], 'T1 val')
    q = T['T2']; eq(later('Monday', 6), 'Sunday', 'T2 day 7 (6 steps after day 1)'); eq(later('Monday', 9), 'Wednesday', 'T2 day 10 (9 steps after day 1)'); eq(later('Monday', 7), 'Monday', 'T2 day 8 is Monday'); eq(q['val'], ['Sunday', 'Wednesday'], 'T2 val')
    q = T['T3']; eq((plus(plus(7, 7), 7), plus(7, 7)), (21, 14), 'T3'); eq(q['val'], [21, 14], 'T3 val')
    q = T['T4']; eq((month[18], plus(18, 7), month[25]), ('Saturday', 25, 'Saturday'), 'T4'); eq(q['val'], ['Saturday', 25], 'T4 val'); eq(q['visual']['highlight'], [18], 'T4 highlight')
    eq(dates_on('Wednesday'), [1, 8, 15, 22, 29], 'T4 hint: the Wednesdays')
    # ---------------------------------------------------------------- Go further
    q = T['G1']; eq(later('Monday', 100), 'Wednesday', 'G1 stepped 100 days'); eq((7 * 14, 100 - 7 * 14), (98, 2), 'G1 14 weeks and 2 days'); eq(later('Monday', 98), 'Monday', 'G1 98 days is whole weeks'); eq(q['val'], [14, 2, 'Wednesday'], 'G1 val')
    eq(sum(1 for k in range(1, 101) if k % 7 == 0), 14, 'G1 whole weeks in 100 days (counted)')
    q = T['G2']; w = dates_on('Wednesday'); eq(w, [1, 8, 15, 22, 29], 'G2 Wednesdays'); eq([plus(x, 7) for x in w[:-1]], w[1:], 'G2 each is 7 more'); eq(month[31], 'Friday', 'G2 the 31st'); eq(q['val'], [8, 15, 22, 29, 'Friday'], 'G2 val')
    q = T['G3']; eq((plus(plus(7, 7), 7), plus(6, 21), month[6], month[27]), (21, 27, 'Monday', 'Monday'), 'G3'); eq(q['val'], [21, 27, 'Monday'], 'G3 val')
    # ---------------------------------------------------------------- Investigation: weekdays that come 5 times
    cnt = {dn: len(dates_on(dn)) for dn in WEEK}; eq(cnt, {'Monday': 4, 'Tuesday': 4, 'Wednesday': 5, 'Thursday': 5, 'Friday': 5, 'Saturday': 4, 'Sunday': 4}, 'I1 counts'); eq(sum(cnt.values()), 31, 'I1 every date counted once')
    eq((7 * 4, 31 - 28), (28, 3), 'I1 4 weeks and 3 days over'); eq(inv['val'], ['5', 'Thursday', 'Friday'], 'I1 val')
    eq(dates_on('Thursday'), [2, 9, 16, 23, 30], 'I1 Thursdays'); eq(dates_on('Friday'), [3, 10, 17, 24, 31], 'I1 Fridays')
    # ---------------------------------------------------------------- talk, exit
    eq((later('Monday', 10), later('Monday', 8)), ('Thursday', 'Tuesday'), 'talk: 10 days later is Thursday; 8 days later is Tuesday'); eq(later(later('Monday', 7), 3), 'Thursday', 'talk: a week then 3 days')
    q = X['E1']; eq(later('Sunday', 2), 'Tuesday', 'E1'); eq(q['val'], ['Tuesday'], 'E1 val')
    q = X['E2']; opts = [nums(o)[0] for o in q['mcq']['options']]; eq([o for o in opts if o == plus(11, 7) and month[o] == month[11]], [18], 'E2 one correct option'); eq(q['val'], [2], 'E2 val'); eq(opts, [17, 18, 19, 25], 'E2 options'); eq(plus(plus(11, 7), 7), 25, 'E2 distractor is a fortnight')
    q = X['E3']; eq(plus(4, 7), 11, 'E3'); eq(q['val'], [11], 'E3 val')
    # ---------------------------------------------------------------- home
    eq(later('Wednesday', 4), 'Sunday', 'H1'); eq(H['H1']['val'], 'Sunday', 'H1 val'); eq(month[10], 'Friday', 'H2'); eq(H['H2']['val'], 'Friday', 'H2 val')
    eq((plus(14, 7), plus(14, 14)), (21, 28), 'H3'); eq(H['H3']['val'], [21, 28], 'H3 val'); eq(later('Saturday', 9), 'Monday', 'H4'); eq(H['H4']['val'], 'Monday', 'H4 val')
    eq(minus(plus(36, 10), 4), 42, 'H5'); eq(H['H5']['val'], 42, 'H5 val'); eq(H['H5'].get('rewind_of'), 'Term 1 Lesson 10', 'H5 is the rewind item'); eq(len([h for h in d['home_practice'] if h['tier'] == 'start']) >= 3, True, 'home has 3 Start here items')
    # ---------------------------------------------------------------- Quest gates
    q = G['C1']; eq((q['visual']['h'], q['visual']['m']), (4, 35), 'C1 clock'); hour_at = 4 + 35 / 60; eq(abs(hour_at - 4.5833) < 0.001, True, 'C1 hour hand a little before the 5'); eq(35 // 5, 7, 'C1 long hand on the 7'); eq(q['val'], ['4:35', 'am'], 'C1 val')
    q = G['C2']; eq(nums(q['text']), [2, 30], 'C2 text'); eq((2 * 60 + 30 + 30, 5 * 60 + 30 + 60), (3 * 60, 6 * 60 + 30), 'C2 minutes'); eq(q['val'], ['3:00', '6:30'], 'C2 val')
    q = G['C3']; eq(coin_total(['50c', '20c', '20c', '5c']), 95, 'C3 coins'); eq(q['visual']['items'], [{'v': '50c'}, {'v': '20c', 'n': 2}, {'v': '5c'}], 'C3 picture'); eq(minus(10, 7), 3, 'C3 change'); eq(q['val'], [95, 3], 'C3 val')
    q = G['C4']; eq((minus(9, 6), [p for p in (6, 9) if p == max(6, 9)]), (3, [9]), 'C4 more'); eq([c for c in itertools.combinations((4, 5, 6), 2) if sum(c) == 10], [(4, 6)], 'C4 exactly one pair for $10'); eq(q['val'], ['ruler', 3, 4, 6], 'C4 val')
    q = G['C5']; tiles = [t['shape'] for t in q['visual']['tiles']]; grid = [tiles[0:3], tiles[3:6], tiles[6:9]]; hid = q['visual']['hide'][0]; r_, c_ = divmod(hid, 3)
    need = {'circle', 'square', 'triangle'} - ({grid[r_][k] for k in range(3) if k != c_}); need2 = {'circle', 'square', 'triangle'} - ({grid[k][c_] for k in range(3) if k != r_}); eq((need, need2), ({'triangle'}, {'triangle'}), 'C5 row and column agree')
    full = [list(row) for row in grid]; full[r_][c_] = 'triangle'; eq(all(len(set(row)) == 3 for row in full) and all(len({full[i][j] for i in range(3)}) == 3 for j in range(3)), True, 'C5 completed grid is a Latin square'); eq(q['val'], ['triangle'], 'C5 val')
    q = G['C6']; eq([triangle_sticks(k) for k in (1, 2, 3, 4, 5)], [3, 5, 7, 9, 11], 'C6 sticks counted from the drawing'); eq(q['val'], [9, 11], 'C6 val')
    q = G['C7']; eq(plus(49, 38), 87, 'C7'); eq(plus(49, 38) == 77, False, 'C7 77 is wrong'); eq(minus(77, 38), 39, 'C7 check'); eq(q['val'], ['No', 87], 'C7 val')
    q = G['C8']; eq(later('Friday', 3), 'Monday', 'C8a'); eq((plus(3, 7), month[3], month[10]), (10, 'Friday', 'Friday'), 'C8b: the 3rd is a Friday on the month page'); eq(q['val'], ['Monday', 10], 'C8 val'); eq(q['visual']['highlight'], [3], 'C8 highlight')
    c = cq['optional']; w = ways(14, (2, 5)); eq(sorted(w), [(2, 2), (7, 0)], 'cave exactly two ways'); eq(c['val'], [7, 0], 'cave val')
    eq([g['page'] for g in cq['questions']], [1, 1, 2, 2, 3, 3, 3, 4], 'gates per page'); eq(cq['sheet_pages'], 4, 'quest log pages')
    covered = sorted({n_ for g in cq['questions'] for n_ in (g['lesson'] if isinstance(g['lesson'], list) else [g['lesson']])}); eq(covered, list(range(21, 31)), 'every lesson of the term is visited by a gate')
    eq(sorted(q_ for s_ in cq['strands'] for q_ in s_['questions']), sorted(g['id'] for g in cq['questions']), 'every gate is in a strand')
    # ---------------------------------------------------------------- online practice
    items = {i['id']: i for i in d['online_practice']['items']}
    for cid, env in BASE_ENV.items(): eq(items[cid]['answer'], ORACLES[cid](env), cid + ' authored answer')
    eq((items['c3']['answer'], later('Tuesday', 3)), ('Friday', 'Friday'), 'c3'); eq((items['c4']['answer'], later('Sunday', 1)), ('Monday', 'Monday'), 'c4')
    eq((items['t2']['answer'], later(before(before('Thursday')), 2)), ('Thursday', 'Thursday'), 't2'); eq((items['g2']['answer'], later('Monday', 100)), ('Wednesday', 'Wednesday'), 'g2')
    for it in items.values():
        for s_ in it.get('slips', []):
            if it['type'] == 'number': eq(it['answer'] in s_['a'], False, it['id'] + ' slip is wrong')
        if it['type'] == 'choice': eq(it['answer'] in it['options'], True, it['id'] + ' answer is an option')
    for a in items['c1']['tpl']['vars']['a']: eq(plus(a, 7) <= 31, True, f'c1 {a} stays in the month')
    for s_ in items['c5']['tpl']['vars']['s']: eq(plus(s_, 21) - s_, 21, f'c5 {s_}')
    for a in items['t1']['tpl']['vars']['a']: eq(plus(a, 14) <= 31, True, f't1 {a} stays in the month')
    for a in items['g1']['tpl']['vars']['a']: eq(_g1(dict(a=a)), 5 if a <= 3 else 4, f'g1 {a} Mondays')
    # ---------------------------------------------------------------- kit contract, hand-offs
    kc = {r['piece']: r for r in d['materials']['kit_contract']}
    for r in kc.values(): eq(r['supplied'] >= r['max_used'], True, 'kit contract ' + r['piece'])
    eq(kc['day cards (Monday to Sunday)']['supplied'], 7, 'seven day cards'); eq(len(WEEK), 7, 'seven days')
    nm = ' '.join(d['parent']['next_materials']).lower(); eq(('term 4' in nm and 'cut' in nm), True, 'hand-off to Term 4 names the book and the cut-out')
    p29 = json.load(open(os.path.join(L1, 'lessons', 'l29.json'), encoding='utf-8')); pm = ' '.join(p29['parent']['next_materials']).lower()
    mk = ' '.join(d['materials']['child']).lower()
    eq(all(w_ in pm for w_ in ('quest log', 'quest partner', 'calendar', '7 day cards')) and all(w_ in mk for w_ in ('quest log', 'quest partner', 'day cards', 'calendar')), True, 'Lesson 29 hand-off matches this lesson\'s materials')
    eq(d['workbook']['kits'][0]['type'], 'calendar_cards', 'the kit is the calendar page')
    return n
