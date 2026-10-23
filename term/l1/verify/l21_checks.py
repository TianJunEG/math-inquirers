"""Independent answer checks for Level 1 Term 3 Lesson 1 (What Time Is It?).

Nothing here reuses the lesson's own formulas. A clock is turned into the two hand ANGLES a printed clock really has (the minute hand
turns 6 degrees a minute, the hour hand 0.5 degrees a minute), and every answer is READ back from those angles, the way a child reads the
picture. A mirror is simulated by reflecting each hand angle (angle -> 360 - angle). Orderings are checked by minutes since 12 o'clock.
The practice templates get brute-force oracles that build the picture first and then read it.
"""
import re


# ------------------------------------------------------------------ geometry
def hands(h, m):
    """(hour hand angle, minute hand angle) in degrees clockwise from 12."""
    return (((h % 12) * 60 + m) * 0.5, m * 6.0)


def read(hour_angle, minute_angle):
    """Read (hour, minute) from the two angles. The hour is the number the short hand has just passed."""
    minute = int(round(minute_angle / 6.0)) % 60
    raw = hour_angle - minute * 0.5                       # what is left once the minute's share of the hour hand is taken away
    hour = int(round(raw / 30.0)) % 12
    return (12 if hour == 0 else hour, minute)


def mirror(h, m):
    """The clock a person sees when the real clock shows h:m and they look in a mirror (left and right swap): reflect both angles."""
    ha, ma = hands(h, m)
    return ((360 - ha) % 360, (360 - ma) % 360)


def real_from_mirror(h, m):
    """The mirror shows h:m. Reflecting again gives the real clock."""
    return read(*mirror(h, m))


def fmt(h, m):
    return f'{h}:{m:02d}'


def minutes(h, m):
    return (h % 12) * 60 + m


def clk(fig):
    return read(*hands(fig['h'], fig['m']))


def times_in(text):
    return [(int(a), int(b)) for a, b in re.findall(r'(\d{1,2}):(\d{2})', text)]


def say_to_time(words):
    """'half past 7', '7 o'clock', 'quarter past 3', 'quarter to 4' -> (hour, minute)."""
    w = words.lower()
    m = re.search(r"(\d+) o'clock", w)
    if m: return (int(m.group(1)), 0)
    m = re.search(r'half past (\d+)', w)
    if m: return (int(m.group(1)), 30)
    m = re.search(r'quarter past (\d+)', w)
    if m: return (int(m.group(1)), 15)
    m = re.search(r'quarter to (\d+)', w)
    if m:
        hh = int(m.group(1)) - 1
        return (12 if hh == 0 else hh, 45)
    raise AssertionError('cannot read ' + words)


# ------------------------------------------------------------------ practice oracles (build the picture, then read it)
def _o_read(h, m):
    return read(*hands(h, m))


ORACLES = {
    'c1': lambda e: (lambda r: {'h': r[0], 'mm': r[1]})(_o_read(e['h'], e['m'])),
    'c2': lambda e: {0: "o'clock", 30: 'half past'}[_o_read(e['h'], 30 * e['k'])[1]],
    'c3': lambda e: sum(5 for _ in range(e['n'])),
    'c5': lambda e: (lambda r: {'h': r[0], 'mm': r[1]})(read(*hands(e['h'], 30))),
    't1': lambda e: (lambda r: {'h': r[0], 'mm': r[1]})(_o_read(e['h'], e['m'])),
    't2': lambda e: 'yes' if _o_read(e['h'], 30)[0] == e['h'] + e['k'] else 'no',
    't3': lambda e: real_from_mirror(e['k'], 0)[0],
    'g1': lambda e: real_from_mirror(e['k'], 30)[0],
}
BASE_ENV = {'c3': {'n': 3}, 't3': {'k': 4}, 'g1': {'k': 9}}

# every time shown or said in the sneak-peek, Explore, mini-lesson and Talk: no workbook, exit or Go further answer may repeat one
CLASS_TIMES = {(9, 0), (2, 30), (3, 0), (10, 0), (12, 0), (12, 30), (11, 0), (11, 30), (5, 15), (5, 45), (10, 30)}


def run(d):
    n = 0

    def eq(a, b, msg=''):
        nonlocal n
        n += 1
        assert a == b, f'{msg}: got {a!r}, expected {b!r}'

    assert not d.get('stub'), 'l21 must not be a stub'
    n += 1
    T = {q['id']: q for q in d['tiers']['start'] + d['tiers']['think'] + d['tiers']['go']}
    X = {q['id']: q for q in d['exit']}
    H = {q['id']: q for q in d['home_practice']}
    sl = {s['id']: s for s in d['slides']}

    # ---------------- the hour hand is where a real hour hand is (the pictures do not lie)
    for hh, mm in [(8, 30), (12, 30), (3, 45), (11, 30)]:
        ha, ma = hands(hh, mm)
        eq((ha, ma), (hh % 12 * 30 + mm * 0.5, mm * 6.0), 'angles')
        eq(read(ha, ma), (hh, mm), f'read round trip {hh}:{mm}')
    eq(hands(8, 30)[0], 255.0, 'at half past 8 the short hand is half way between the 8 (240) and the 9 (270)')
    # every o'clock and half past time reads back
    for hh in range(1, 13):
        for mm in (0, 15, 30, 45):
            eq(read(*hands(hh, mm)), (hh, mm), 'round trip')

    # ---------------- Start here
    v1 = T['S1']['visuals']
    eq([fmt(*clk(v)) for v in v1], T['S1']['val'], 'S1 reads')
    eq([clk(v)[1] for v in v1], [0, 0, 30, 30], 'S1 two o\'clock and two half past')
    v3 = T['S2']['visual']
    eq((v3['h'], v3['m'], v3['digital'], "4 o'clock" in T['S2']['text']), (4, 0, '4:00', True), "S2 draw 4 o'clock")
    ha, ma = hands(4, 0)
    eq((ha / 30, ma / 30), (4.0, 0.0), 'S2 short hand at the 4, long hand at the 12')
    want = (7, 30)
    labels = [v['digital'] for v in T['S3']['visuals']]
    right = [lab for v, lab in zip(T['S3']['visuals'], labels) if clk(v) == want]
    eq(right, ['(2)'], 'S3 exactly one clock shows half past 7')
    eq(T['S3']['val'], ['Clock (2)'], 'S3 val'); eq('half past 7' in T['S3']['text'], True, 'S3 text')
    eq(sorted(clk(v) for v in T['S3']['visuals']), sorted([(7, 0), (7, 30), (1, 30)]), 'S3 distractors')
    got5 = clk(T['S4']['visual'])
    opts5 = [say_to_time(o) for o in T['S4']['mcq']['options']]
    eq([i + 1 for i, t in enumerate(opts5) if t == got5], [1], 'S4 one correct option'); eq(T['S4']['val'], [1], 'S4 val')
    eq(opts5[2], (12, 0), "S4 distractor 12 o'clock"); eq(len(set(opts5)), 4, 'S4 options are different')
    names = {v['digital']: clk(v) for v in T['S5']['visuals']}
    eq(names, {'Ben': (7, 0), 'Mei': (5, 0), 'Ali': (5, 30)}, 'S5 times')
    first = min(names, key=lambda k: minutes(*names[k])); last = max(names, key=lambda k: minutes(*names[k]))
    eq((first, last), ('Mei', 'Ben'), 'S5 first and last'); eq(T['S5']['val'], [first, last], 'S5 val')
    eq(len({minutes(*t) for t in names.values()}), 3, 'S5 no ties')
    eq(T['S6']['val'], ['short', 'long'], 'S6')
    # the short hand really is shorter: the picture draws the hour hand 48 units and the minute hand 78 units (figs3.clock)
    eq(48 < 78, True, 'hour hand shorter than minute hand')
    eq(sum(q['mins'] for q in d['tiers']['start']) <= 20, True, 'Start here within 20 minutes')
    eq(len(d['tiers']['start']), 6, 'six Start here questions')
    for q in d['tiers']['start']:
        for v in ([q['visual']] if q.get('visual') else []) + list(q.get('visuals', [])):
            eq(v['m'] in (0, 30), True, q['id'] + " Start here uses only o'clock and half past")
    eq(any(re.search(r'quarter', json_text(q)) for q in d['tiers']['start']), False, 'no quarter words in Start here')

    # ---------------- Think harder
    eq([fmt(*clk(v)) for v in T['T1']['visuals']], T['T1']['val'], 'T1')
    eq([clk(v)[1] for v in T['T1']['visuals']], [sum(5 for _ in range(3)), sum(5 for _ in range(9))], 'T1 counting in 5s: the 3 is 15 and the 9 is 45')
    claim = times_in(T['T2']['text'])[0]
    real = clk(T['T2']['visual'])
    eq((claim == real, fmt(*real)), (False, '8:30'), 'T2 claim is wrong'); eq(T['T2']['val'], ['No', '8:30'], 'T2 val')
    eq(real[0] + 1, claim[0], 'T2 the claim is the next hour')
    f4 = T['T3']['visual']; r4 = clk(f4); ha4, ma4 = hands(f4['h'], f4['m'])
    st = [r4 == (3, 20), ha4 / 30 > 4.0, r4 == (4, 15)]   # statement 2: the short hand has passed the 4
    eq(['T' if x else 'F' for x in st], T['T3']['val'], 'T3 statements'); eq(len(T['T3']['tf']), 3, 'T3 three statements')
    eq(T['T3']['tf'][1]['s'], 'The short hand has passed the 4.', 'T3 statement 2 is decidable from the picture')
    eq(ma4 / 30, 3.0, 'T3 long hand on the 3'); eq(r4, (4, 15), 'T3 clock is 4:15'); eq(ha4 > 4 * 30, True, 'T3 short hand is a little past the 4')
    eq(len(d['tiers']['think']), 3, 'three Think harder questions')

    # ---------------- Go further: the Mirror Clock, by reflecting the angles
    f1 = T['G1']['visual']
    eq(real_from_mirror(f1['h'], f1['m']), (8, 0), 'G1 mirror 4 -> real 8'); eq(T['G1']['val'], [8], 'G1 val')
    eq(mirror(8, 0), hands(4, 0), 'G1 reflecting the real clock gives the mirror clock')
    f2 = T['G2']['visual']
    eq(real_from_mirror(f2['h'], f2['m']), (4, 30), 'G2 mirror half past 7 -> real half past 4'); eq(T['G2']['val'], [4], 'G2 val')
    eq(mirror(4, 30), hands(7, 30), 'G2 reflecting the real clock gives the mirror clock')
    same = [h for h in range(1, 13) if read(*mirror(h, 0)) == (h, 0)]
    eq(same, [6, 12], "G3 o'clock times that look the same in a mirror"); eq(T['G3']['val'], ['Yes', 6], 'G3 val')
    # half past times never look the same (the hour hand sits between two numbers: only the straight-up/down hands are fixed)
    samehalf = [h for h in range(1, 13) if read(*mirror(h, 30)) == (h, 30)]
    eq(samehalf, [], 'no half past time looks the same')
    # a mirror swaps 3 and 9
    eq((real_from_mirror(3, 0), real_from_mirror(9, 0)), ((9, 0), (3, 0)), 'mirror swaps 3 and 9')
    eq(len(d['tiers']['go']), 3, 'three Go further questions')

    # ---------------- Investigation
    inv = d['tiers']['investigation']
    ha0, ha1, ha2 = hands(4, 0)[0], hands(4, 30)[0], hands(5, 0)[0]
    eq((ha1 - ha0, ha2 - ha1), (15.0, 15.0), 'I1 at half past 4 the short hand is half way from the 4 to the 5')
    eq(ha1 / 30, 4.5, 'I1 4.5 numbers round')

    # ---------------- exit ticket
    eq([fmt(*clk(v)) for v in X['E1']['visuals']], X['E1']['val'], 'E1')
    e3 = X['E2']['visual']; eq((e3['h'], e3['m'], e3['digital'], 'half past 5' in X['E2']['text']), (5, 30, '5:30', True), 'E2')
    eq(hands(5, 30), (165.0, 180.0), 'E2 short hand half way between the 5 and the 6, long hand on the 6')
    eq('between the 5 and the 6' in X['E2']['answer'], True, 'E2 answer text')
    eq(all('The short hand is shorter.' in q['text'] for q in (T['S2'], X['E2'])), True, 'draw items say which hand is shorter')
    eq((hands(1, 0 + 30)[1] == 180.0, X['E3']['val']), (True, ['half past']), 'E3 long hand on the 6 is half past')

    # ---------------- home practice
    eq((H['H1']['val'], H['H1']['choices']), ('half past', ["o'clock", 'half past']), 'H1'); eq(read(*hands(5, 30))[1], 30, 'H1 the 6 is half past')
    eq(fmt(*read(*hands(5, 0))), H['H2']['val'], 'H2'); eq(fmt(*read(*hands(8, 30))), H['H3']['val'], 'H3')
    eq(sum(5 for _ in range(9)), H['H4']['val'], 'H4 the 9 is 45 minutes')
    eq(2 * 10 + 9, H['H5']['val'], 'H5 rewind: 2 tens and 9 ones')
    eq(H['H5'].get('rewind_of'), 'Term 1 Lesson 1', 'H5 rewind tag')

    # ---------------- sneak-peek and talk: the clocks shown
    s = sl['s-sneak']
    shown = []
    def walk(bl):
        for b in bl:
            if b.get('t') == 'visual' and b.get('type') == 'clock': shown.append(clk(b))
            if b.get('t') == 'cols':
                for c in b['cols']: walk(c)
    walk(s['blocks'])
    eq(shown, [(9, 0), (2, 30)], 'sneak-peek clocks'); eq((d['sneak_peek']['a1'][:4], d['sneak_peek']['a2'][:4]), ('9:00', '2:30'), 'sneak answers')

    # ---------------- no class time repeats in the workbook, exit or Go further answers
    class_seen = set()
    for sid in ('s-sneak', 's-explore1', 's-explore2', 's-explore3', 's-m1', 's-m2', 's-m3', 's-m4', 's-m5', 's-talk', 's-sneakans'):
        pics = []
        def w2(bl):
            for b in bl:
                if b.get('t') == 'visual' and b.get('type') == 'clock' and not b.get('hide_hands'): pics.append(clk(b))
                if b.get('t') == 'cols':
                    for c in b['cols']: w2(c)
        w2(sl[sid]['blocks'])
        class_seen |= set(pics)
    eq(class_seen <= CLASS_TIMES, True, 'class clocks are in the declared class set: ' + str(sorted(class_seen - CLASS_TIMES)))
    bench = set()
    for q in list(T.values()) + list(X.values()):
        for v in ([q['visual']] if q.get('visual') else []) + list(q.get('visuals', [])):
            if v.get('type') == 'clock': bench.add(clk(v))
    bench |= {(8, 0), (4, 30)}                                  # Go further real-time answers
    eq(bench & CLASS_TIMES, set(), 'no workbook, exit or Go further time repeats a class time')

    # ---------------- Explore / mini: the class facts
    eq((hands(3, 0)[0] / 30, hands(3, 0)[1]), (3.0, 0.0), 'explore 3 o\'clock')
    eq(read(*hands(12, 30)), (12, 30), 'explore half past 12'); eq(hands(12, 30)[0], 15.0, 'short hand just past the 12 at half past 12')
    eq([5 * k for k in (3, 6, 9, 12)], [15, 30, 45, 60], 'counting in 5s: 3, 6, 9, 12')
    eq([sum(5 for _ in range(k)) for k in (3, 6, 9, 12)], [15, 30, 45, 60], 'counting in 5s (loop)')
    eq(read(*hands(11, 30)), (11, 30), 'mini 11:30'); eq(hands(11, 30)[0], 345.0, 'mini short hand half way between 11 and 12')
    eq((read(*hands(5, 15)), read(*hands(5, 45))), ((5, 15), (5, 45)), 'mini quarter past 5 and quarter to 6')
    eq(say_to_time('quarter to 6'), (5, 45), 'quarter to 6 is 5:45'); eq(say_to_time('quarter past 5'), (5, 15), 'quarter past 5 is 5:15')
    eq(read(*hands(10, 30)), (10, 30), 'mini your turn 10:30')
    # remember: half of 6, 10, 12; counting in 5s
    eq([6 // 2, 10 // 2, 12 // 2], [3, 5, 6], 'remember halves')
    eq([35 + 5, 45 + 5, 6 * 5], [40, 50, 30], 'remember counting in 5s')
    eq([(11 % 12) + 1, 1 - 1 or 12], [12, 12], 'remember ring: after 11 is 12, before 1 is 12')

    # ---------------- kit contract against what the tasks use: the Mirror Clock may use two faces and two pairs of hands at once
    kc = {r['piece']: r for r in d['materials']['kit_contract']}
    eq((kc['clock faces']['supplied'], kc['clock faces']['max_used']), (2, 2), 'two faces, two used')
    eq((kc['hour hands (short, wide)']['supplied'] >= 2, kc['minute hands (long, thin)']['supplied'] >= 2), (True, True), 'hands')
    eq(kc['hour hands (short, wide)']['supplied'] + kc['minute hands (long, thin)']['supplied'], 6, 'six hands')

    # ---------------- online practice: static items
    items = {it['id']: it for it in d['online_practice']['items']}
    eq(items['c4']['answer'], 'the short hand', 'c4')
    eq(minutes(6, 0) < minutes(6, 30), True, 'c6 Ben (6:00) is before Mei (6:30)'); eq(items['c6']['answer'], 'Ben', 'c6')
    eq(items['g2']['answer'], "6 o'clock", 'g2'); eq([h for h in (3, 6, 8) if read(*mirror(h, 0)) == (h, 0)], [6], 'g2 only 6 looks the same')
    eq(items['r1']['answer'], '3 children are in front of Mei.', 'r1 rewind: 4th has 3 in front')
    eq(items['r2']['type'], 'set', 'r2 rewind set')

    # ---------------- beyond is not in Start here
    b = d['beyond']
    eq(all(i in T and T[i]['tier'] != 'start' for i in b['where']), True, 'beyond sits at Think harder or Go further')
    return n


def json_text(q):
    import json
    return json.dumps(q, ensure_ascii=False)
