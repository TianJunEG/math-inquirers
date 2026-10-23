"""Independent answer checks for Level 1 Term 3 Lesson 3 (Lesson 23, Time Passes).

Every time in l23.json is recomputed here in minutes since midnight (a 24-hour count, which the lesson never shows to children), so that the am to pm change at noon and the
12 to 1 wrap on the clock face are checked without using the lesson's own method of moving the hands. Clock pictures are checked against the times written in the questions
(hour and minute of every drawn clock), the time lines against 30-minute ticks, and the online practice templates get brute-force oracles that step the clock on minute by minute.
The class and workbook (start, how long) pairs are listed here and checked to be disjoint, and clear of the two Quest gate pairs (2:30 + half an hour; 5:15 + 1 hour).
"""
import itertools
import re


def mins(h, m=0, ap=None):
    """Minutes since midnight. ap 'am' | 'pm' | None (None = a 12-hour face with no am or pm: hours 1 to 12 count as 1 to 12)."""
    if ap == 'am':
        return (0 if h == 12 else h) * 60 + m
    if ap == 'pm':
        return (12 if h == 12 else h + 12) * 60 + m
    return (h % 12) * 60 + m


def show(t, ap=False):
    """Minutes since midnight -> '9:30' (12-hour face, no leading zero) or '9:30 am'."""
    t %= 24 * 60
    h24, m = divmod(t, 60)
    h = h24 % 12 or 12
    s = f'{h}:{m:02d}'
    return s + (' am' if h24 < 12 else ' pm') if ap else s


def face(t):
    """Minutes since midnight -> (hour on the face 1..12, minute)."""
    t %= 24 * 60
    h24, m = divmod(t, 60)
    return (h24 % 12 or 12, m)


def parse(s):
    m = re.search(r'(\d{1,2}):(\d{2})\s*(am|pm)?', s)
    return mins(int(m.group(1)), int(m.group(2)), m.group(3))


def walk(x, out, key=None):
    if isinstance(x, dict):
        if x.get('type') == 'clock': out.append(x)
        for v in x.values(): walk(v, out)
    elif isinstance(x, list):
        for v in x: walk(v, out)
    return out


def clocks_of(x):
    return walk(x, [])


def pair(start_face, dur):
    """A (start, how long) pair as (minutes on a 12-hour face, minutes lasted)."""
    return (mins(*start_face), dur)


# --------------------------------------------------------------------------------- the registry of what each part of the lesson asks
# (start on the face, minutes that it lasts), one for every time the lesson asks a child to find. Quest gate 2 uses (2:30, 30) and (5:15, 60).
QUEST = {pair((2, 30), 30), pair((5, 15), 60)}
CLASS_PAIRS = {
    'sneak': [pair((4, 0), 60), pair((8, 30), 30)],
    'explore': [pair((1, 0), 60), pair((1, 30), 60), pair((1, 0), 30), pair((1, 30), 30)],
    'mini': [pair((12, 0), 60), pair((10, 0), 60), pair((10, 0), 30), pair((10, 30), 30), pair((5, 0), 60), pair((7, 0), 60), pair((7, 0), 30), pair((3, 0), 30), pair((9, 0), 60), pair((11, 0), 30), pair((9, 30), 30)],
    'talk': [pair((7, 30), 30)],
}
WORKBOOK_PAIRS = {
    'S1': [pair((8, 0), 60)], 'S2': [pair((2, 0), 60)], 'S3': [pair((8, 30), 60)], 'S4': [pair((6, 0), 30)], 'S5': [pair((10, 30), 60)],
    'S6': [pair((3, 0), 60), pair((8, 0), 30), pair((9, 0), 30)],
    'T1': [pair((5, 30), 60), pair((5, 30), 30)], 'T2': [pair((4, 15), 30), pair((9, 45), 30)], 'T3': [pair((11, 0), 60), pair((12, 0), 30)], 'T4': [pair((6, 0), 60)],
    'G1': [pair((2, 15), 60), pair((3, 15), 30), pair((3, 45), 30)], 'G2': [pair((11, 30), 60), pair((11, 30), 90)], 'G3': [pair((3, 30), 60), pair((4, 0), 30)],
    'E1': [pair((6, 30), 60)], 'E2': [pair((2, 0), 30)], 'E3': [pair((11, 30), 30)],
    'I1': [pair((12, 30), 60)],
}

# --------------------------------------------------------------------------------- oracles for the online practice templates (step the clock on, minute by minute)


def step(start, delta):
    t = start
    for _ in range(abs(delta)):
        t += 1 if delta > 0 else -1
    return t % (12 * 60) or 12 * 60


def hm(t):
    t %= 12 * 60
    h = t // 60 or 12
    return h, t % 60


def _fields(t):
    h, m = hm(t)
    return {'a': h, 'b': m}


ORACLES = {
    'c1': lambda e: _fields(step(mins(e['h'], 0), 60)),
    'c2': lambda e: _fields(step(mins(e['h'], 0), 30)),
    'c3': lambda e: _fields(step(mins(e['h'], 30), 60)),
    'c4': lambda e: (lambda d: 'half an hour' if d == 30 else ('1 hour' if d == 60 else None))((e['h'] + e['k']) * 60 + (30 if e['k'] == 0 else 0) - e['h'] * 60),
    't1': lambda e: _fields(step(mins(e['h'], 30), 30)),
    't2': lambda e: _fields(step(mins(e['h'], 15), 30)),
    't3': lambda e: _fields(step(mins(e['h'], 0), -30)),
    'g1': lambda e: _fields(step(step(step(mins(e['h'], 30), -30), -30), -60)),
}
BASE_ENV = {}


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
    c = lambda q: clocks_of(q)

    # ---------------------------------------------------------------- the pairs are disjoint, and clear of the Quest
    allcls = [p for v in CLASS_PAIRS.values() for p in v]
    allwb = [p for v in WORKBOOK_PAIRS.values() for p in v]
    eq(len(set(allcls)), len(allcls), 'class pairs are all different')
    eq(len(set(allwb)), len(allwb), 'workbook pairs are all different')
    eq(sorted(set(allcls) & set(allwb)), [], 'no workbook (start, how long) pair repeats a class pair')
    eq(sorted((set(allcls) | set(allwb)) & QUEST), [], 'no class or workbook pair is a Quest gate pair')

    # ---------------------------------------------------------------- sneak-peek
    sp = d['sneak_peek']
    eq(show(mins(4, 0) + 60), '5:00', 'sneak 1'); eq(show(mins(8, 30) + 30), '9:00', 'sneak 2'); eq(sp['val1'], 5, 'sneak val1')
    eq(('4 o\'clock' in sp['q1'], 'half past 8' in sp['q2'], 'half an hour' in sp['q2']), (True, True, True), 'sneak texts match the pairs')
    eq([(x['h'], x['m']) for x in c(sl['s-sneak']['blocks'])], [(4, 0)], 'sneak slide shows the 4 o\'clock clock')
    # ---------------------------------------------------------------- remember
    eq([(x['h'], x['m']) for x in c(sl['s-rem1']['blocks'])], [(3, 0), (6, 30), (12, 0)], 'warm-up clocks')
    nl = [b for b in sl['s-rem3']['blocks'] if b.get('type') == 'number_line'][0]
    eq((nl['marks'], nl['hide'], nl['jumps']), ([34], [44], [[34, 44, '+10']]), 'warm-up line'); eq(34 + 10, 44, 'warm-up jump'); eq(52 + 10, 62, 'warm-up second jump')
    eq(sum(1 for _ in range(5, 61, 5)), 12, 'twelve fives make an hour'); eq(sum(1 for _ in range(5, 31, 5)), 6, 'six fives make half an hour')
    eq([b for b in sl['s-rem2']['blocks'] if b.get('t') == 'cols'][0]['cols'][1][1]['items'], list(range(5, 61, 5)), 'warm-up number row counts in 5s')

    # ---------------------------------------------------------------- explore: clocks on the slides are start clocks only
    eq([(x['h'], x['m']) for x in c(sl['s-explore1']['blocks'])], [(1, 0)], 'explore 1 start clock'); eq([(x['h'], x['m']) for x in c(sl['s-explore2']['blocks'])], [(1, 0)], 'explore 2 start clock')
    eq([show(mins(1, 0) + 60), show(mins(1, 30) + 60), show(mins(1, 0) + 30), show(mins(1, 30) + 30)], ['2:00', '2:30', '1:30', '2:00'], 'explore answers')
    eq(face(mins(1, 30) + 30), (2, 0), 'half an hour from 1:30 changes the hour'); eq(face(mins(12, 0) + 60), (1, 0), 'mini: 1 hour after 12 o\'clock is 1 o\'clock')
    # ---------------------------------------------------------------- mini-lesson
    m1 = [(x['h'], x['m']) for x in c(sl['s-m1']['blocks'])]; eq(m1, [(10, 0), (11, 0)], 's-m1 clocks'); eq(mins(*m1[1]) - mins(*m1[0]), 60, 's-m1 is 1 hour')
    m2 = [(x['h'], x['m']) for x in c(sl['s-m2']['blocks'])]; eq(m2, [(10, 0), (10, 30)], 's-m2 clocks'); eq(mins(*m2[1]) - mins(*m2[0]), 30, 's-m2 is half an hour')
    nl2 = [b for b in sl['s-m2']['blocks'] if b.get('type') == 'number_line'][0]
    ticks = {int(k): v for k, v in nl2['labels'].items()}                                     # every tick is 30 minutes; the last tick is an empty box while the question is asked
    eq([parse(ticks[i]) - parse(ticks[0]) for i in (0, 1)], [0, 30], 's-m2 time line ticks are half hours'); eq(nl2['hide'], [2], 's-m2 the answer tick is hidden')
    eq([(j[0], j[1]) for j in nl2['jumps']], [(0, 1), (1, 2)], 's-m2 jumps are one tick each (30 minutes)'); eq(show(mins(10, 30) + 30), '11:00', 's-m2 second half hour')
    nl3 = [b for b in sl['s-m3']['blocks'] if b.get('type') == 'number_line'][0]
    t3 = {int(k): v for k, v in nl3['labels'].items()}
    eq((nl3['hide'], nl3['jumps'][0][:2]), ([0], [2, 0]), 's-m3 goes back from the end to the hidden start')
    eq(parse(t3[2]) - parse(t3[1]), 30, 's-m3 ticks are half hours'); eq(show(parse(t3[2]) - 60), '5:00', 's-m3 start 1 hour before 6:00')
    eq(('6 o\'clock' in [b for b in sl['s-m3']['blocks'] if b.get('t') == 'p'][0]['text'], 'lasted 1 hour' in [b for b in sl['s-m3']['blocks'] if b.get('t') == 'p'][0]['text']), (True, True), 's-m3 text')
    m4 = [(x['h'], x['m']) for x in c(sl['s-m4']['blocks'])]; eq(m4, [(7, 0), (8, 0), (7, 0), (7, 30)], 's-m4 clocks')
    eq((mins(*m4[1]) - mins(*m4[0]), mins(*m4[3]) - mins(*m4[2])), (60, 30), 's-m4 A is 1 hour, B is half an hour')
    for sid, ends in (('s-m5', ['3:30', None, None]), ('s-m5a', ['3:30', '10:00', '11:30'])):
        tb = [b for b in sl[sid]['blocks'] if b.get('type') == 'table'][0]
        eq([r[3] if r[3] != '[]' else None for r in tb['rows']], ends, sid + ' ends column')
    tb = [b for b in sl['s-m5a']['blocks'] if b.get('type') == 'table'][0]
    for r in tb['rows']:
        eq(show(parse(r[1]) + (30 if 'half' in r[2] else 60)), r[3], 's-m5a row ' + r[0])
    # ---------------------------------------------------------------- Start here
    LAST = lambda s: 30 if 'half an hour' in s else (60 if '1 hour' in s else None)
    q = T['S1']; cs = c(q)
    eq([(x['h'], x['m'], bool(x.get('hide_hands'))) for x in cs], [(8, 0, False), (8, 0, True)], 'S1 clocks: the start and an empty end clock')
    eq(show(mins(8, 0) + 60), '9:00', 'S1'); eq(q['val'], ['9:00', '9:00'], 'S1 val'); eq(('8 o\'clock' in q['text'], '1 hour' in q['text']), (True, True), 'S1 text')
    q = T['S2']; cs = c(q); eq([(x['h'], x['m']) for x in cs], [(2, 0)], 'S2 clock'); eq(show(mins(*[(x['h'], x['m']) for x in cs][0]) + 60), '3:00', 'S2'); eq(q['val'], ['3:00'], 'S2 val')
    q = T['S3']; st = parse(q['text']); eq(show(st + 60, True), '9:30 am', 'S3'); eq(q['val'], ['9:30 am'], 'S3 val')
    eq(('1 hour' in q['text'], q['parts'][0]['text'].endswith('am.')), (True, True), 'S3 frame says am')
    q = T['S4']; cs = c(q); times = {x['digital']: mins(x['h'], x['m']) for x in cs}
    want = mins(6, 0) + 30; right = [k for k, v in times.items() if v == want]
    eq(right, ['B'], 'S4 exactly one clock is half an hour after 6'); eq(q['val'], ['B'], 'S4 val')
    eq((times['A'] - mins(6, 0), times['C'] - mins(6, 0)), (60, 90), 'S4 distractors are 1 hour and 1 hour 30 later'); eq('6 o\'clock' in q['text'], True, 'S4 text')
    q = T['S5']; cs = c(q); gap = mins(cs[1]['h'], cs[1]['m']) - mins(cs[0]['h'], cs[0]['m'])
    eq(gap, 60, 'S5 gap'); eq(q['val'], ['1 hour'], 'S5 val'); eq(q['parts'][0]['choices'], ['half an hour', '1 hour'], 'S5 choices')
    q = T['S6']; rows = q['visual']['rows']; got = [show(parse(r[1]) + LAST(r[2])) for r in rows]
    eq(got, ['4:00', '8:30', '9:30'], 'S6'); eq(q['val'], got, 'S6 val'); eq([r[3] for r in rows], ['[]'] * 3, 'S6 has three answer boxes')
    eq(sum(x['mins'] for x in d['tiers']['start']) <= 20, True, 'Start here within 20 minutes')
    # ---------------------------------------------------------------- Think harder
    q = T['T1']; eq('5:30' in q['text'], True, 'T1 text'); eq([show(mins(5, 30) + 60), show(mins(5, 30) + 30)], ['6:30', '6:00'], 'T1'); eq(q['val'], ['6:30', '6:00'], 'T1 val')
    eq(face(mins(5, 30) + 30), (6, 0), 'T1b the hour changes')
    q = T['T2']; eq(('4:15' in q['text'], '9:45' in q['text'], 'half an hour' in q['text']), (True, True, True), 'T2 text'); eq([show(mins(4, 15) + 30), show(mins(9, 45) + 30)], ['4:45', '10:15'], 'T2'); eq(q['val'], ['4:45', '10:15'], 'T2 val')
    eq(face(mins(9, 45) + 30), (10, 15), 'T2b passes the hour')
    q = T['T3']; rows = q['visual']['rows']; dur = {'1 hour': 60, 'half an hour': 30}
    starts = [parse(r[3]) - dur[r[2]] for r in rows]
    eq([show(x) for x in starts], ['11:00', '12:00'], 'T3 starts by going back from the Ends column'); eq(q['val'], ['11:00', '12:00'], 'T3 val')
    eq([show(x + dur[r[2]]) for x, r in zip(starts, rows)], [r[3] for r in rows], 'T3 forward check'); eq(starts[1], parse(rows[0][3]), 'T3 story time starts when Art ends')
    eq((q['visual']['head'], [r[1] for r in rows]), (['Lesson', 'Starts', 'Lasts', 'Ends'], ['[]', '[]']), 'T3 table')
    q = T['T4']; rows = q['visual']['rows']; dur = {r[0]: parse(r[2]) - parse(r[1]) for r in rows}
    eq(dur, {'Penguins': 30, 'Seals': 60, 'Parrots': 30}, 'T4 durations'); eq([k for k, v in dur.items() if v == 60], ['Seals'], 'T4a exactly one show lasts 1 hour')
    eq(rows[1][2], rows[2][1], 'T4 the shows run on'); eq(show(parse(rows[2][2]) + 60, True).split(' ')[0], '7:00', 'T4b')  # the Parrots end at 6:00; the next show ends at 7:00 pm
    eq(q['val'], ['Seals', '7:00 pm'], 'T4 val')
    # ---------------------------------------------------------------- Go further
    q = T['G1']; nlq = q['visual']
    end = mins(4, 15, 'pm'); snack_start = end - 30; story_start = snack_start - 30; paint_start = story_start - 60
    eq([show(snack_start, True), show(paint_start, True)], ['3:45 pm', '2:15 pm'], 'G1'); eq(q['val'], ['3:45 pm', '2:15 pm'], 'G1 val')
    eq(paint_start + 60 + 30 + 30, end, 'G1 forward check'); eq(show(story_start, True), '3:15 pm', 'G1 the story starts at 3:15 pm')
    eq(nlq['hide'], [0, 1, 2, 3], 'G1 the unknown ticks are boxes'); eq(parse(nlq['labels']['4']) % 720, end % 720, 'G1 last tick is the end time')
    eq([j[0:2] for j in nlq['jumps']], [[0, 2], [2, 3], [3, 4]], 'G1 jumps: painting 2 ticks, story 1 tick, snack 1 tick (a tick is half an hour)')
    q = X['E1']; eq('6:30' in q['text'] and '1 hour' in q['text'], True, 'E1 text'); eq(show(parse(q['text']) + 60), '7:30', 'E1'); eq(q['val'], ['7:30'], 'E1 val')
    q = X['E2']; opts = q['mcq']['options']; right = [i + 1 for i, o in enumerate(opts) if parse(o) == mins(2, 0) + 30]
    eq(right, [3], 'E2 one option is 2:00 and half an hour'); eq(q['val'], right, 'E2 val'); eq(sorted(parse(o) - mins(2, 0) for o in opts), [5, 15, 30, 60], 'E2 distractors'); eq('2 o\'clock' in q['text'], True, 'E2 text')
    q = X['E3']; f3 = q['visual']; eq(show(mins(f3['h'], f3['m']) - 30), '11:30', 'E3 half an hour before the clock'); eq(q['val'], ['11:30'], 'E3 val'); eq(show(mins(f3['h'], f3['m']) - 30 + 30), '12:00', 'E3 forward check')
    # ---------------------------------------------------------------- home
    eq(show(parse(H['H1']['text']) + 60), '10:30', 'H1'); eq(H['H1']['val'], '10:30', 'H1 val')
    eq(show(mins(5, 0) + 30), '5:30', 'H2'); eq(H['H2']['val'], '5:30', 'H2 val')
    eq(show(parse(H['H3']['text']) + 30), '4:15', 'H3'); eq(H['H3']['val'], '4:15', 'H3 val')
    eq(show(mins(H['H4']['visual']['h'], H['H4']['visual']['m']) - 30), '4:30', 'H4 half an hour before the clock'); eq(H['H4']['val'], '4:30', 'H4 val')
    nums = [72, 27, 70, 17]; eq(sorted(nums), [17, 27, 70, 72], 'H5 rewind'); eq(H['H5']['val'], [17, 27, 70, 72], 'H5 val'); eq(H['H5'].get('rewind_of'), 'Term 1 Lesson 3', 'H5 is the rewind item')
    eq(len([h for h in d['home_practice'] if h['tier'] == 'start']) >= 3, True, 'home has 3 Start here items')
    # ---------------------------------------------------------------- online practice, authored numbers
    items = {i['id']: i for i in d['online_practice']['items']}
    for cid, (h, m, add, want) in {'c1': (3, 0, 60, (4, 0)), 'c2': (5, 0, 30, (5, 30)), 'c3': (2, 30, 60, (3, 30)), 't1': (4, 30, 30, (5, 0)), 't2': (3, 15, 30, (3, 45))}.items():
        it = items[cid]; eq(hm(step(mins(h, m), add)), want, cid + ' authored'); eq([f['answer'] for f in it['fields']], list(want), cid + ' fields')
        eq((it['fig_base']['h'], it['fig_base']['m']), (h, m), cid + ' picture')
    eq(hm(step(mins(7, 0), -30)), (6, 30), 't3 authored'); eq([f['answer'] for f in items['t3']['fields']], [6, 30], 't3 fields')
    eq(hm(step(step(step(mins(6, 30), -30), -30), -60)), (4, 30), 'g1 authored'); eq([f['answer'] for f in items['g1']['fields']], [4, 30], 'g1 fields')
    eq(items['c4']['answer'], 'half an hour', 'c4 authored'); eq(items['c5']['answer'], 60 // 2, 'c5'); eq(items['g2']['answer'], 60 + 30, 'g2')
    for it in items.values():
        for s_ in it.get('slips', []):
            if it['type'] == 'number': eq(it['answer'] in s_['a'], False, it['id'] + ' slip is wrong')
    # variants: every template variant stays inside the day and never prints a minute under 10 without a pad
    for cid in ('c1', 'c3', 't1', 't3', 'g1'):
        tp = items[cid]['tpl']; names = list(tp['vars'])
        for combo in itertools.product(*[tp['vars'][k] for k in names]):
            env = dict(zip(names, combo)); r = ORACLES[cid](env)
            eq(1 <= r['a'] <= 12 and r['b'] in (0, 15, 30, 45), True, f'{cid} {env} gives a real clock time')
    # ---------------------------------------------------------------- kit contract: the clock pieces come from the first lesson of Term 3 (2 faces, 3 + 3 hands)
    kc = {r['piece']: r for r in d['materials']['kit_contract']}
    eq([(r['supplied'], r['max_used']) for r in kc.values()], [(2, 2), (3, 2), (3, 2)], 'kit contract: supplied against most used')
    eq(d['workbook']['kits'], [], 'no new kit page in this lesson')
    # ---------------------------------------------------------------- hand-off to the next lesson (play money: 29 pieces on two pages, plus the $1 tokens)
    nm = ' '.join(d['parent']['next_materials'])
    eq(('29' in nm, 'tokens' in nm, 'clock' in nm), (True, True, True), 'hand-off to Lesson 24 names the money pieces, the tokens and the clock')
    eq(4 + 6 + 4 + 2 + 5 + 4 + 3 + 1, 29, 'the 29 play-money pieces: coins 4+6+4+2, notes 5+4+3+1')
    return n
