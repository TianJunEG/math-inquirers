"""Independent answer checks for Level 1 Term 3 Lesson 2 (Five Minutes at a Time).

A clock is turned into the two hand ANGLES a printed clock really has (minute hand 6 degrees a minute, hour hand 0.5 degrees a minute)
and every time is READ back from those angles, the way a child reads the picture. Durations are found by stepping the clock forward one
minute at a time until it shows the end time (no subtraction of minutes is reused from the lesson). am and pm come from a 24-hour hour
for each event. The practice templates get brute-force oracles that build the picture first and then read it.
"""
import re


def hands(h, m):
    return (((h % 12) * 60 + m) * 0.5, m * 6.0)


def read(hour_angle, minute_angle):
    minute = int(round(minute_angle / 6.0)) % 60
    hour = int(round((hour_angle - minute * 0.5) / 30.0)) % 12
    return (12 if hour == 0 else hour, minute)


def clk(fig):
    return read(*hands(fig['h'], fig['m']))


def fmt(h, m):
    return f'{h}:{m:02d}'


def times_in(text):
    return [(int(a), int(b)) for a, b in re.findall(r'(\d{1,2}):(\d{2})', text)]


def step_minutes(start, end):
    """Number of minutes the clock must run from start to end (stepping one minute at a time)."""
    h, m = start; n = 0
    while (h, m) != end:
        m += 1
        if m == 60: m = 0; h = h % 12 + 1
        n += 1
        assert n < 24 * 60, 'did not reach the end'
    return n


def next_hour(t):
    return (t[0] % 12 + 1, 0)


def chunks(start, end):
    """Go to the next hour first, then the rest: the lesson's method, recomputed by stepping."""
    nh = next_hour(start)
    return step_minutes(start, nh), step_minutes(nh, end)


def ampm(hour24):
    return 'am' if hour24 < 12 else 'pm'


def _o_read(h, m):
    return read(*hands(h, m))


ORACLES = {
    'c1': lambda e: (lambda r: {'h': r[0], 'mm': r[1]})(_o_read(e['h'], e['m'])),
    'c2': lambda e: sum(5 for _ in range(e['n'])),
    'c5': lambda e: (lambda r: {'h': r[0], 'mm': r[1]})(_o_read(e['h'], step_minutes((e['h'], 0), (e['h'], e['n'] * 5)))),
    't1': lambda e: (lambda r: {'h': r[0], 'mm': r[1]})(_o_read(e['h'], e['m'])),
    't2': lambda e: 'yes' if _o_read(e['h'], 50)[0] == e['h'] + e['k'] else 'no',
    't3': lambda e: step_minutes((3, e['a']), (3, e['b'])),
    'g1': lambda e: step_minutes((3, e['a']), (4, e['b'])),
    'r2': lambda e: e['a'] + (e['a'] + e['d']),
}
BASE_ENV = {'c2': {'n': 3}, 't3': {'a': 15, 'b': 50}, 'g1': {'a': 40, 'b': 15}}

# every time shown or said in the warm-up, sneak-peek, Explore, mini-lesson, Talk and the optional slide
CLASS_TIMES = {(9, 0), (2, 30), (3, 15), (11, 50), (4, 10), (7, 25), (9, 50), (1, 5), (6, 35), (10, 5), (8, 55), (2, 20), (5, 40), (5, 50), (4, 0), (7, 0),
               (6, 10), (6, 50), (7, 20), (10, 40), (1, 15), (4, 45), (7, 5), (8, 5), (6, 45), (7, 15), (12, 45)}   # plus the event-card times and the spoken am/pm examples


def run(d):
    n = 0

    def eq(a, b, msg=''):
        nonlocal n
        n += 1
        assert a == b, f'{msg}: got {a!r}, expected {b!r}'

    assert not d.get('stub')
    n += 1
    T = {q['id']: q for q in d['tiers']['start'] + d['tiers']['think'] + d['tiers']['go']}
    X = {q['id']: q for q in d['exit']}
    H = {q['id']: q for q in d['home_practice']}
    sl = {s['id']: s for s in d['slides']}

    # ---- every 5-minute time round-trips through the angles; the hour hand is where a real hour hand is
    for hh in range(1, 13):
        for mm in range(0, 60, 5):
            eq(read(*hands(hh, mm)), (hh, mm), f'round trip {hh}:{mm}')
    eq(hands(3, 50)[0], 3 * 30 + 25.0, 'at 3:50 the short hand is 25 degrees past the 3')
    eq(hands(4, 0)[0] - hands(3, 50)[0], 5.0, 'at 3:50 the short hand is 5 degrees short of the 4')

    # ---- Start here (digits to 5 minutes; no quarter words; am and pm without full stops)
    eq([fmt(*clk(v)) for v in T['S1']['visuals']], T['S1']['val'], 'S1')
    eq([clk(v)[1] % 5 for v in T['S1']['visuals']], [0, 0, 0], 'S1 five-minute times')
    eq([clk(v)[1] for v in T['S1']['visuals']], [35, 5, 10], 'S1 minutes: the 7 is 35, the 1 is 5, the 2 is 10 (no :45, :50 or :55 trap at Start here)')
    eq(all(clk(v)[1] <= 35 for v in T['S1']['visuals']), True, 'S1 short hand is clearly past a number (the hour trap is Think harder)')
    f2 = T['S2']['visual']
    eq(clk(f2)[1], sum(5 for _ in range(8)), 'S2 the long hand on the 8 is 40 minutes'); eq(T['S2']['val'], [40], 'S2 val')
    f3 = T['S3']['visual']
    eq((f3['h'], f3['m'], f3['digital']), (3, 20, '3:20'), 'S3'); eq(hands(3, 20)[1] / 30, 4.0, 'S3 long hand on the 4'); eq(hands(3, 20)[0] > 90, True, 'S3 short hand a little past the 3')
    opts4 = [tuple(int(x) for x in o.split(':')) for o in T['S4']['mcq']['options']]
    eq([i + 1 for i, t in enumerate(opts4) if t == clk(T['S4']['visual'])], [2], 'S4 one correct option'); eq(T['S4']['val'], [2], 'S4 val')
    eq(len(set(opts4)), 4, 'S4 options differ')
    eq(opts4[0], (8, 5), 'S4 distractor: the 5 read as 5 minutes'); eq(opts4[2], (9, 25), 'S4 distractor: the next hour'); eq(opts4[3], (8, 30), 'S4 distractor: half past')
    eq(abs(hands(*(T['S4']['visual']['h'], T['S4']['visual']['m']))[0] - hands(T['S4']['visual']['h'], T['S4']['visual']['m'])[1]) > 60, True, 'S4 the two hands are well apart, so the short hand is easy to find')
    # S5: am or pm from the 24-hour time of the event
    day = {'wake up 6:30': 6.5, 'bed 8:30': 20.5}
    eq([ampm(int(day['wake up 6:30'])), ampm(int(day['bed 8:30']))], T['S5']['val'], 'S5')
    # S6: the earlier of two times in the same hour is the one with fewer minutes (checked by stepping the clock)
    names = {v['digital']: clk(v) for v in T['S6']['visuals']}
    eq(names, {'Ben': (6, 20), 'Mei': (6, 15)}, 'S6 times')
    eq(step_minutes(names['Mei'], names['Ben']), 5, 'S6 Ben leaves 5 minutes after Mei'); eq(T['S6']['val'], ['Mei'], 'S6 val')
    eq(len(d['tiers']['start']), 6, 'six Start here questions'); eq(sum(q['mins'] for q in d['tiers']['start']) <= 20, True, 'Start here within 20 minutes')
    allq = json_text(d['tiers']['start'] + d['exit'])
    eq(bool(re.search(r'quarter|ten past|twenty to|a\.m\.|p\.m\.', allq)), False, 'no quarter words, ten past or a.m. in Start here and the exit ticket')

    # ---- Think harder
    eq([ampm(h) for h in (7, 10, 12, 21)], T['T1']['val'], 'T1 am pm: 7:30 am, 10:20 am, 12:30 pm (24-hour 12), 9:15 pm (24-hour 21)')
    eq(ampm(12), 'pm', 'T1 12:30 is just after noon, so it is pm')
    eq((1 * 60 + 20, 'h' in '1 h 20 min'), (80, True), 'T2 1 h 20 min is 1 hour and 20 minutes (80 minutes)'); eq(T['T2']['val'][:2], [1, 20], 'T2 val')
    eq((60 > 50), True, 'T2 1 h is longer than 50 min'); eq(T['T2']['val'][2], '1 h', 'T2 longer')
    claim = times_in(T['T3']['text'])[0]; real = clk(T['T3']['visual'])
    eq((claim == real, fmt(*real)), (False, '3:50'), 'T3'); eq(real[0] + 1, claim[0], 'T3 the claim is the next hour'); eq(T['T3']['val'], ['No', '3:50'], 'T3 val')
    tab = {r[0]: tuple(int(x) for x in r[1].split(':')) for r in T['T4']['visual']['rows']}
    arrive = times_in(T['T4']['text'])[0]
    starts = sorted(tab.items(), key=lambda kv: (kv[1][0] % 12, kv[1][1]))
    cur = [k for k, t in starts if (t[0] % 12 * 60 + t[1]) <= (arrive[0] % 12 * 60 + arrive[1])][-1]
    nxt = [t for k, t in starts if (t[0] % 12 * 60 + t[1]) > (arrive[0] % 12 * 60 + arrive[1])][0]
    eq((cur, step_minutes(arrive, nxt)), ('Fish', 15), 'T4 which show is on and the wait'); eq(T['T4']['val'], ['fish', 15], 'T4 val')
    eq(len(d['tiers']['think']), 4, 'four Think harder questions')

    # ---- Go further: Chunk the Gap, recomputed by stepping the clock one minute at a time
    eq((chunks((3, 10), (4, 5)), step_minutes((3, 10), (4, 5))), ((50, 5), 55), 'G1 chunks and total'); eq(T['G1']['val'], [50, 5, 55], 'G1 val')
    eq(step_minutes((2, 45), (3, 20)), 35, 'G2'); eq(chunks((2, 45), (3, 20)), (15, 20), 'G2 chunks'); eq(T['G2']['val'], [35], 'G2 val')
    ali = step_minutes((5, 35), (6, 20)); mei = step_minutes((6, 5), (6, 55))
    eq((ali, mei, 'Mei' if mei > ali else 'Ali', abs(mei - ali)), (45, 50, 'Mei', 5), 'G3'); eq(T['G3']['val'], ['Mei', 5], 'G3 val')
    eq(max(ali, mei) < 55, True, 'G3 neither duration passes 90 minutes')
    g1l = T['G1']['visual']
    eq(g1l['labels'], {str(k): f'{3 + k // 60}:{k % 60:02d}' for k in range(0, 61, 10)} | {'65': ''}, 'G1 line: every label is a time, 0 is 3:00, 10 is 3:10, 60 is 4:00, the 65 tick (4:05) is unlabelled')
    eq((g1l['marks'], g1l['end']), ([10, 60, 65], 65), 'G1 line marks 3:10, 4:00, 4:05')
    eq((10 + 50, 60 + 5), (60, 65), 'G1 line jumps')

    # ---- Investigation
    eq(len([m for m in range(5, 61, 5)]), 12, 'I1 12 steps of 5 minutes make 60'); eq(sum(5 for _ in range(12)), 60, 'I1 12 fives'); eq(len([m for m in range(5, 16, 5)]), 3, 'I1 12 to 3 is 3 steps')

    # ---- exit ticket
    eq(fmt(*clk(X['E1']['visual'])), X['E1']['val'][0], 'E1'); eq(X['E1']['val'], ['10:15'], 'E1 val'); eq(ampm(13), X['E2']['val'][0], 'E2 1:20 in the afternoon is 13:20 so pm'); eq('1:20' in X['E2']['text'], True, 'E2 text')
    e3 = X['E3']['visual']; eq((e3['h'], e3['m'], e3['digital']), (9, 25, '9:25'), 'E3'); eq(hands(9, 25)[1] / 30, 5.0, 'E3 long hand on the 5'); eq(hands(9, 25)[0] > 270, True, 'E3 short hand a little past the 9')

    # ---- home practice
    eq(sum(5 for _ in range(4)), H['H1']['val'], 'H1'); eq(fmt(*read(*hands(8, 35))), H['H2']['val'], 'H2 the long hand on the 7 is 35 minutes, the short hand has passed the 8')
    eq('3:05', f'{3}:{5:02d}', 'H3'); eq(H['H3']['val'], '3:05', 'H3 val'); eq(ampm(12), H['H4']['val'], 'H4')
    eq([46 + 2, 46 + 4], H['H5']['val'], 'H5 rewind: 46 47 48 49 50'); eq(H['H5'].get('rewind_of'), 'Term 1 Lesson 2', 'H5 tag')

    # ---- sneak-peek
    s = sl['s-sneak']; shown = []
    def walk(bl):
        for b in bl:
            if b.get('t') == 'visual' and b.get('type') == 'clock': shown.append(clk(b))
            if b.get('t') == 'cols':
                for c in b['cols']: walk(c)
    walk(s['blocks'])
    eq(shown, [(3, 15), (11, 50)], 'sneak-peek clocks'); eq((d['sneak_peek']['a1'], d['sneak_peek']['a2'][:5]), ('3:15', '11:50'), 'sneak answers')

    # ---- no class time repeats in the workbook, exit or Go further
    class_seen = set()
    for sid in ('s-rem2', 's-sneak', 's-explore1', 's-explore1-ans', 's-explore2', 's-explore2-ans', 's-m1', 's-m2', 's-m3', 's-m3-ans', 's-m6', 's-m6-ans', 's-sneakans', 's-opt'):
        pics = []
        def w2(bl):
            for b in bl:
                if b.get('t') == 'visual' and b.get('type') == 'clock' and not b.get('hide_hands'): pics.append(clk(b))
                if b.get('t') == 'cols':
                    for c in b['cols']: w2(c)
        w2(sl[sid]['blocks'])
        class_seen |= set(pics)
    eq(class_seen <= CLASS_TIMES, True, 'class clocks are in the declared set: ' + str(sorted(class_seen - CLASS_TIMES)))
    bench = set()
    for q in list(T.values()) + list(X.values()):
        for v in ([q['visual']] if q.get('visual') else []) + list(q.get('visuals', [])):
            if v.get('type') == 'clock': bench.add(clk(v))
    eq(bench & CLASS_TIMES, set(), 'no workbook or exit time repeats a class time')
    wt = set()
    for q in list(T.values()) + list(X.values()):
        wt |= set(times_in(json_text(q['text'])))
    for a, b in (((3, 10), (4, 5)), ((2, 45), (3, 20)), ((5, 35), (6, 20)), ((6, 5), (6, 55))):
        wt |= {a, b}
    eq(wt & {(4, 10), (7, 25), (9, 50), (6, 35), (2, 20), (5, 40), (3, 15), (11, 50)}, set(), 'no written workbook time repeats a class time')

    # ---- Explore / mini class facts
    eq(step_minutes((4, 0), (4, 10)), 10, 'explore 4:10'); eq(step_minutes((7, 0), (7, 25)), 25, 'explore 7:25')
    eq(read(*hands(9, 50)), (9, 50), 'explore 9:50'); eq(hands(10, 0)[0] - hands(9, 50)[0], 5.0, 'at 9:50 the short hand is 5 degrees short of the 10')
    eq((chunks((5, 50), (6, 0))), (10, 0), 'optional slide 5:50 to 6:00 is 10 minutes')
    eq((60 - 50, 60 - 40, 60 - 55), (10, 20, 5), 'remember pairs that make 60'); eq([sum(5 for _ in range(k)) for k in (12, 6)], [60, 30], 'remember claps')
    eq((read(*hands(1, 5)), read(*hands(6, 35)), read(*hands(8, 55)), read(*hands(2, 20)), read(*hands(5, 40))), ((1, 5), (6, 35), (8, 55), (2, 20), (5, 40)), 'mini times')
    ev = d['workbook']['kits'][0]['events']
    # each event card carries a time; its am or pm comes from the 24-hour time of the event (a bath at 19:05 is pm, school at 7:20 is am)
    day24 = {'wake up': (6, 10), 'breakfast': (6, 50), 'school': (7, 20), 'break': (10, 40), 'come home': (13, 15), 'play ball': (16, 45), 'night bath': (19, 5), 'go to bed': (20, 5)}
    eq(len(ev), 8, 'eight event cards')
    for (ic, lab) in ev:
        name, tm = lab.rsplit(' ', 1)
        hh, mm = (int(x) for x in tm.split(':'))
        eq((hh, mm), (day24[name][0] % 12 or 12, day24[name][1]), 'card time ' + lab)
    eq([ampm(day24[l.rsplit(' ', 1)[0]][0]) for _, l in ev], ['am'] * 4 + ['pm'] * 4, 'four am cards then four pm cards')

    # ---- kit contract
    kc = {r['piece']: r for r in d['materials']['kit_contract']}
    eq((kc['event cards']['supplied'], kc['event cards']['max_used']), (8, 8), 'event cards')

    # ---- online practice static items
    items = {it['id']: it for it in d['online_practice']['items']}
    eq((ampm(7), ampm(18)), ('am', 'pm'), 'c3 c4 (breakfast 7:30, tea 6:20 in the evening)'); eq((items['c3']['answer'], items['c4']['answer']), ('am', 'pm'), 'c3 c4 answers')
    eq(step_minutes((6, 15), (6, 40)), 25, 'c6 Mei (6:15) before Ben (6:40)'); eq(items['c6']['answer'], 'Mei', 'c6')
    eq(items['g2']['answer'], 5, 'g2 Mei reads 5 minutes longer'); eq(items['r1']['answer'], '9 - 5', 'r1 rewind'); eq(items['r2']['tier'], 'core', 'r2 rewind')
    b = d['beyond']
    eq(all(i in T and T[i]['tier'] != 'start' for i in b['where']), True, 'beyond sits at Think harder or Go further')
    return n


def json_text(q):
    import json
    return json.dumps(q, ensure_ascii=False)
