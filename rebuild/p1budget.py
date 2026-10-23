"""P1 re-budget pass (docs/audit/timing_p1.md, sections 5 to 7): every lesson fits 90 minutes when a tutor runs it live online.

This module is the single source of the new Level 1 timing plan.
  * BOUNDS / SLIDES / OPTIONAL / DROP describe the plan per lesson.
  * apply(D, n) is the LAST step of each rebuild/gen_lK.py (after p1neutral.apply): it removes dropped slides, sets every
    clock pill and the 'Minutes a to b' line of the speaker notes, labels optional slides, rewrites the title-slide time plan
    and patches the text that quotes minutes.  Idempotent.
  * `python3 rebuild/p1budget.py` writes hp/budget.json (read by hp/guide.js and by the tutor console) and
    hp/budget_slides.json (slide clock ranges, read by hp/guide.js for the worksheet lines).
"""
import os, re, json, glob
import p1fix
from slidekit import *

H = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(H, '..')
OPT = 'Optional, if you finish early'
OPT_REMIND = 'Optional, if you need a reminder'

PART_TITLES = ['Opening', 'Warm-up', 'Sneak-peek', 'Explore', 'Mini-lesson', 'Brain break', 'Worksheet', 'Talk time', 'Exit ticket', 'Look-back', 'Flex time']
STD = dict(op=2, wu=8, sn=12, ex=26, mi=36, br=40, ws=72, ta=79, xt=85, lb=88, fl=90)
BOUNDS = {
    1: dict(STD, op=4, wu=10, sn=14, ex=28, mi=38, br=42),
    2: dict(STD),
    3: dict(STD, mi=37, br=41),
    4: dict(STD, mi=37, br=41),
    5: dict(STD),
    6: dict(STD),
    7: dict(STD, ex=28, mi=36),
    8: dict(STD),
    9: dict(STD, ex=27, mi=37, br=41),
    10: dict(op=2, wu=6, sn=10, ex=28, mi=37, br=41, ws=71, ta=79, xt=87, lb=90, fl=None),
}


def parts(n):
    b = BOUNDS[n]; keys = ['op', 'wu', 'sn', 'ex', 'mi', 'br', 'ws', 'ta', 'xt', 'lb', 'fl']
    out = []; prev = 0
    for k, title in zip(keys, PART_TITLES):
        if b[k] is None: continue
        out.append((title, prev, b[k])); prev = b[k]
    assert prev == 90, (n, prev)
    return out


# slide id -> (start, end) clock minutes. Slides not listed keep no clock (end, cover) or are optional.
SLIDES = {
    1: {'routine': (0, 1), 'rules': (1, 2), 'l1-title': (2, 4), 'l1-warm1': (4, 8), 'l1-warm2': (8, 10), 'l1-warmcheck': (10, 14),
        'l1-explore1': (14, 19), 'l1-explore2': (19, 28),
        'l1-teach1': (28, 30), 'l1-we1': (30, 32), 'l1-try1': (32, 33), 'l1-we2': (33, 35), 'l1-try2': (35, 36), 'l1-key': (36, 38),
        'l1-break': (38, 42),
        'l1-ws1': (42, 52), 'l1-ws1ans': (52, 54), 'l1-teachboth': (54, 56), 'l1-teachtable': (56, 58), 'l1-ws2': (58, 68), 'l1-ws2ans': (68, 72),
        'l1-talk': (72, 79), 'l1-exit': (79, 85), 'l1-reflect': (85, 88)},
    2: {'l2-title': (0, 2), 'l2-warm1': (2, 6), 'l2-warm2': (6, 8), 'l2-warmcheck': (8, 12), 'l2-explore1': (12, 17), 'l2-explore2': (17, 26),
        'l2-teach1': (26, 28), 'l2-try1': (28, 29), 'l2-teach2': (29, 31), 'l2-try2': (31, 32), 'l2-teach3': (32, 35), 'l2-key': (35, 36),
        'l2-break': (36, 40),
        'l2-ws1': (40, 50), 'l2-ws1ans': (50, 52), 'l2-teachpage2': (52, 54), 'l2-ws2': (54, 66), 'l2-ws2ans': (66, 72),
        'l2-talk': (72, 79), 'l2-exit': (79, 85), 'l2-reflect': (85, 88)},
    3: {'l3-title': (0, 2), 'l3-warm1': (2, 6), 'l3-warm2': (6, 8), 'l3-warmcheck': (8, 12), 'l3-explore1': (12, 17), 'l3-explore2': (17, 26),
        'l3-teach1': (26, 28), 'l3-try1': (28, 29), 'l3-teach2': (29, 31), 'l3-try2': (31, 32), 'l3-teach3': (32, 35), 'l3-key': (35, 37),
        'l3-break': (37, 41),
        'l3-ws1': (41, 50), 'l3-ws1ans': (50, 52), 'l3-teachwho': (52, 54), 'l3-teachtally': (54, 55), 'l3-ws2': (55, 67), 'l3-ws2ans': (67, 72),
        'l3-talk': (72, 79), 'l3-exit': (79, 85), 'l3-reflect': (85, 88)},
    4: {'l4-title': (0, 2), 'l4-warm1': (2, 6), 'l4-warm2': (6, 8), 'l4-warmcheck': (8, 12), 'l4-explore1': (12, 17), 'l4-explore2': (17, 26),
        'l4-teach1': (26, 28), 'l4-we1': (28, 30), 'l4-try1': (30, 31), 'l4-teach2': (31, 33), 'l4-we2': (33, 35), 'l4-try2': (35, 36), 'l4-key': (36, 37),
        'l4-break': (37, 41),
        'l4-ws1': (41, 53), 'l4-ws1ans': (53, 55), 'l4-ws2': (55, 67), 'l4-ws2ans': (67, 72),
        'l4-talk': (72, 79), 'l4-exit': (79, 85), 'l4-reflect': (85, 88)},
    5: {'l5-title': (0, 2), 'l5-warm1': (2, 6), 'l5-warm2': (6, 8), 'l5-warmcheck': (8, 12), 'l5-explore1': (12, 17), 'l5-explore2': (17, 26),
        'l5-teach1': (26, 29), 'l5-we1': (29, 31), 'l5-try1': (31, 32), 'l5-we2': (32, 34), 'l5-try2': (34, 35), 'l5-key': (35, 36),
        'l5-break': (36, 40),
        'l5-teachm': (40, 42), 'l5-teachbar': (42, 44), 'l5-ws1': (44, 52), 'l5-ws1ans': (52, 54), 'l5-teachq1': (54, 56), 'l5-teachq2': (56, 58),
        'l5-ws2': (58, 68), 'l5-ws2ans': (68, 72),
        'l5-talk': (72, 79), 'l5-exit': (79, 85), 'l5-reflect': (85, 88)},
    6: {'l6-title': (0, 2), 'l6-warm1': (2, 6), 'l6-warm2': (6, 8), 'l6-warmcheck': (8, 12), 'l6-explore1': (12, 17), 'l6-explore2': (17, 26),
        'l6-teach1': (26, 28), 'l6-we1': (28, 30), 'l6-try1': (30, 32), 'l6-try2': (32, 34), 'l6-try3': (34, 35), 'l6-key': (35, 36),
        'l6-break': (36, 40),
        'l6-ws1': (40, 52), 'l6-ws1ans': (52, 54), 'l6-teachfew': (54, 58), 'l6-ws2': (58, 68), 'l6-ws2ans': (68, 72),
        'l6-talk': (72, 79), 'l6-exit': (79, 85), 'l6-reflect': (85, 88)},
    7: {'l7-title': (0, 2), 'l7-warm1': (2, 6), 'l7-warm2': (6, 8), 'l7-warmcheck': (8, 12), 'l7-explore1': (12, 18), 'l7-explore2': (18, 28),
        'l7-teach1': (28, 30), 'l7-we1': (30, 32), 'l7-try1': (32, 35), 'l7-key': (35, 36),
        'l7-break': (36, 40),
        'l7-teachpic': (40, 41), 'l7-teachsides': (41, 42), 'l7-ws1': (42, 52), 'l7-ws1ans': (52, 54), 'l7-teachwho': (54, 55), 'l7-teachtri': (55, 58),
        'l7-ws2': (58, 68), 'l7-ws2ans': (68, 72),
        'l7-talk': (72, 79), 'l7-exit': (79, 85), 'l7-reflect': (85, 88)},
    8: {'l8-title': (0, 2), 'l8-warm1': (2, 6), 'l8-warm2': (6, 8), 'l8-warmcheck': (8, 12), 'l8-explore1': (12, 17), 'l8-explore2': (17, 26),
        'l8-teach1': (26, 28), 'l8-we1': (28, 30), 'l8-try1': (30, 31), 'l8-we2': (31, 33), 'l8-try2': (33, 35), 'l8-key': (35, 36),
        'l8-break': (36, 40),
        'l8-teachorder': (40, 42), 'l8-ws1': (42, 52), 'l8-ws1ans': (52, 54), 'l8-teachline': (54, 56), 'l8-teachriddle': (56, 57), 'l8-teachodd': (57, 58),
        'l8-ws2': (58, 68), 'l8-ws2ans': (68, 72),
        'l8-talk': (72, 79), 'l8-exit': (79, 85), 'l8-reflect': (85, 88)},
    9: {'l9-title': (0, 2), 'l9-warm1': (2, 6), 'l9-warm2': (6, 8), 'l9-warmcheck': (8, 12), 'l9-explore1': (12, 17), 'l9-explore2': (17, 27),
        'l9-teach1': (27, 29), 'l9-we1': (29, 31), 'l9-try1': (31, 32), 'l9-teachcm': (32, 33), 'l9-we2': (33, 35), 'l9-try2': (35, 36), 'l9-key': (36, 37),
        'l9-break': (37, 41),
        'l9-ws1': (41, 50), 'l9-ws1ans': (50, 52), 'l9-teachunit': (52, 54), 'l9-teachconv': (54, 56), 'l9-teachmore': (56, 58), 'l9-ws2': (58, 68), 'l9-ws2ans': (68, 72),
        'l9-talk': (72, 79), 'l9-exit': (79, 85), 'l9-reflect': (85, 88)},
    10: {'l10-title': (0, 2), 'l10-warm1': (2, 6), 'l10-warmcheck': (6, 10), 'l10-explore1': (10, 11), 'l10-cards': (11, 17), 'l10-explore2': (17, 28),
         'l10-teach1': (28, 29), 'l10-we1': (29, 31), 'l10-we2': (31, 33), 'l10-we3': (33, 35), 'l10-key': (35, 37),
         'l10-break': (37, 41),
         'l10-ws1': (41, 53), 'l10-ws1ans': (53, 55), 'l10-ws2': (55, 67), 'l10-ws2ans': (67, 71),
         'l10-talk': (71, 79), 'l10-exit': (79, 84), 'end': (84, 87), 'l10-reflect': (87, 90)},
}

# optional slides: no clock time, label OPT (early finishers / choice) or OPT_REMIND
OPTIONAL = {
    1: ['l1-stretch', 'l1-challenge', 'l1-chdiag', 'l1-chwalk'],
    2: ['l2-stretch', 'l2-challenge', 'l2-chdiag', 'l2-chwalk'],
    3: ['l3-stretch', 'l3-challenge', 'l3-chdiag', 'l3-chwalk'],
    4: ['l4-stretch', 'l4-challenge', 'l4-chdiag', 'l4-chwalk'],
    5: ['l5-stretch', 'l5-challenge', 'l5-chdiag', 'l5-chwalk'],
    6: ['l6-teachnotes', 'l6-trynotes', 'l6-stretch', 'l6-teachexact', 'l6-teachswap', 'l6-challenge', 'l6-chdiag', 'l6-chwalk'],
    7: ['l7-stretch', 'l7-we2', 'l7-try2', 'l7-we3', 'l7-challenge', 'l7-chdiag', 'l7-chwalk'],
    8: ['l8-stretch', 'l8-challenge', 'l8-chdiag', 'l8-chwalk'],
    9: ['l9-stretch', 'l9-challenge', 'l9-chdiag', 'l9-chwalk'],
    10: ['l10-teachgraph', 'l10-teachtri', 'l10-teachlen', 'l10-stretch', 'l10-challenge', 'l10-chdiag', 'l10-chwalk'],
}
REMIND = {'l10-teachgraph', 'l10-teachtri', 'l10-teachlen'}

# slides removed from the deck (audit section 5): duplicates of the worksheet or of another slide
DROP = {
    1: ['cover'],                       # the title slide repeats it
    2: ['l2-try3'],                     # repeats worksheet Q4; l2-teach3 already works an example
    3: ['l3-try3'],                     # merged into l3-teach3 as one "your turn"
    9: ['l9-tryconv'],                  # serves only the optional Q4 and Think harder T3/T4
    10: ['l10-warm2', 'l10-try1', 'l10-try2'],
}


def ws_start(n):
    return BOUNDS[n]['br']


# ------------------------------------------------------------------------------------------------ helpers
def _path(D, sid): return os.path.join(D, 'slides', sid + '.html')


def _read(D, sid):
    f = _path(D, sid)
    return open(f).read() if os.path.exists(f) else None


PILL = re.compile(r'(<p style="[^"]*letter-spacing:\d+px[^"]*">)(\d+–\d+ MIN|\d+ MIN|Your choice|For early finishers|Challenge|Optional[^<]*)(</p>)')


def set_pill(D, sid, label, dark=False):
    s = _read(D, sid)
    if s is None:
        print('p1budget: missing slide', sid); return
    if PILL.search(s):
        s = PILL.sub(lambda m: m.group(1) + label + m.group(3), s, count=1)
    else:
        # no pill yet: add one just after the leading decoration
        tag = (f'<p style="position:absolute;right:128px;top:64px;font-size:28px;font-weight:700;letter-spacing:2px;color:#FFC93C">{label}</p>\n' if dark else
               f'<p style="position:absolute;right:128px;top:52px;font-size:26px;font-weight:800;letter-spacing:2px;color:#1F7A6F;background:#FFFFFF;border:2px solid #1F7A6F;border-radius:999px;padding:6px 22px">{label}</p>\n')
        i = s.index('>', s.index('<section')) + 1
        j = i
        while True:
            k = s.find('<', j)
            if s.startswith('<div data-deco', k):
                depth = 0
                for mm in re.finditer(r'<div\b|</div>', s[k:]):
                    depth += 1 if mm.group(0).startswith('<div') else -1
                    if depth == 0: j = k + mm.end(); break
                continue
            break
        s = s[:j] + '\n' + tag + s[j:]
    open(_path(D, sid), 'w').write(s)


def set_minutes_note(D, sid, a, b):
    s = _read(D, sid)
    if s is None or '<aside>' not in s: return
    head, tail = s.split('<aside>', 1)
    tail = re.sub(r'Minutes \d+ to \d+', 'Minutes %d to %d' % (a, b), tail, count=1)
    open(_path(D, sid), 'w').write(head + '<aside>' + tail)


def drop_minutes_note(D, sid):
    s = _read(D, sid)
    if s is None: return
    s2 = re.sub(r'<aside>Minutes \d+ to \d+(?: \([^)]*\))?\.\s*', '<aside>', s)
    if s2 != s: open(_path(D, sid), 'w').write(s2)


def sub_slide(D, sid, pairs, must=False):
    """Idempotent text replacement in one slide (regex pairs are tuples (pattern, repl, True))."""
    s = _read(D, sid)
    if s is None:
        if must: print('p1budget: missing slide', sid)
        return
    t = s
    for pr in pairs:
        if len(pr) == 3:
            t = re.sub(pr[0], pr[1], t, flags=re.S)
        else:
            old, new = pr
            if old in t: t = t.replace(old, new)
            elif must and new not in t: print('p1budget: text not found in', sid, ':', old[:70])
    if t != s: open(_path(D, sid), 'w').write(t)


def sub_deck(D, pairs):
    p1fix.sub_all(D, pairs)


def order_edit(D, fn):
    dj = os.path.join(D, 'deck.json'); deck = json.load(open(dj)); o = deck['order']
    fn(o)
    # sections must start on a slide that exists
    for k, sec in deck.get('sections', {}).items():
        if sec['start'] not in o:
            sec['start'] = o[0]
    json.dump(deck, open(dj, 'w'), indent=1, ensure_ascii=False)


def mini_note(n):
    return {10: ' (how to start a puzzle: draw it, list it, make a table; click to reveal each step and answer)'}.get(n, ' (click to reveal each step and answer)' if n in (1, 2, 3, 4, 5, 6, 7, 8, 9) else '')


def time_plan(n, old=''):
    """The 'Time plan:' sentence of the title-slide notes, built from the budget."""
    b = BOUNDS[n]
    mini = 'mini-lesson' if re.search(r'mini-lesson \d+ to \d+', old) else 'teaching'
    mnote = re.search(r'(?:teaching|mini-lesson) \d+ to \d+( \([^)]*\))?', old)
    mnote = (mnote.group(1) or '') if mnote else ''
    wnote = re.search(r'worksheet \d+ to \d+( with [^(]*?)? \(', old)
    wnote = (wnote.group(1) or '') if wnote else ' with short teaching before each page and a check-together slide after it'
    chk = {2: 6, 3: 5, 4: 5}.get(n, 4)
    s = 'Time plan: opening 0 to %d, warm-up %d to %d (game %d to %d, quick questions %d to %d; ask questions 1 to 3, and 4 and 5 only if you are on time), sneak-peek puzzles %d to %d, ' % (
        b['op'], b['op'], b['wu'], b['op'], b['op'] + 4, b['op'] + 4, b['wu'], b['wu'], b['sn']) if n != 10 else \
        'Time plan: opening 0 to 2, warm-up game and whiteboard round 2 to 6 (five questions), sneak-peek puzzles 6 to 10, '
    s += 'explore %d to %d, %s %d to %d%s, brain break %d to %d, ' % (b['sn'], b['ex'], mini, b['ex'], b['mi'], mnote, b['mi'], b['br'])
    s += 'worksheet %d to %d%s (a 30-second stand-and-stretch reset after the page-1 check, taken from that slot; the last %d minutes check page 2, after a 1-minute stand-up stretch), ' % (b['br'], b['ws'], wnote, chk)
    s += 'talk time %d to %d, exit ticket %d to %d, look-back %d to %d' % (b['ws'], b['ta'], b['ta'], b['xt'], b['xt'], b['lb'])
    s += (', then flex time and goodbye %d to 90 (this is the buffer: if you are behind, use it; do not start anything new).' % b['lb']) if b['fl'] else \
        ' (this lesson has no spare minutes: follow the shortened plan, see the guide).'
    return s


TP = re.compile(r'Time plan: .*?(?= Think harder, Go further and the Investigation are for every child)', re.S)


def title_notes(D, n):
    sid = 'l%d-title' % n
    s = _read(D, sid)
    if s is None: return
    m = TP.search(s)
    if not m:
        print('p1budget: time plan not found in', sid); return
    s = s[:m.start()] + time_plan(n, m.group(0)) + s[m.end():]
    open(_path(D, sid), 'w').write(s)


# ------------------------------------------------------------------------------------------------ main entry
RESET_MARK = 'Reset: stand, stretch, sit'


def micro_reset(D, n):
    """A 30-second stand-stretch-sit reset after the page-1 check (final_fixes_levels_1_4.md).
    Level 1 has one 4-minute break at about minute 38 to 42 and one 1-minute stretch before the page-2 check; children aged 6 to 8
    were otherwise seated for about 26 minutes in the worksheet block. The reset is taken from the 2-minute page-1 check slot, so no
    clock boundary moves and the lesson still sums to 90. It is optional: skip it if the clock is more than a minute behind."""
    sid = 'l%d-ws1ans' % n
    s = _read(D, sid)
    if s is None or RESET_MARK in s:
        return
    chip = ('<p style="position:absolute;right:128px;bottom:52px;font-size:26px;font-weight:800;color:#1B2A49;background:#FFC93C;'
            'border-radius:999px;padding:8px 24px">' + RESET_MARK + ' (30 s)</p>\n')
    mark = '<p style="position:absolute;left:128px;bottom:64px'
    if mark in s:
        s = s.replace(mark, chip + mark, 1)
    note = (' Reset (about 30 seconds, taken from this slot): when the answers are checked, everyone stands, reaches up high, shakes out their hands, takes one slow breath and sits down again, then page 2. '
            'Skip it if you are more than a minute behind.')
    s = s.replace('</aside>', note + '</aside>', 1)
    open(_path(D, sid), 'w').write(s)


def apply(D, n):
    p_ = 'l%d-' % n
    # 1. dropped slides (generators write them; they are removed here, from the order and from disk)
    for sid in DROP.get(n, []):
        f = _path(D, sid)
        if os.path.exists(f): os.remove(f)
    order_edit(D, lambda o: [o.remove(x) for x in DROP.get(n, []) if x in o])
    # 2. clocks: pill + 'Minutes a to b'
    for sid, (a, b) in SLIDES[n].items():
        if _read(D, sid) is None: continue
        set_pill(D, sid, '%d–%d MIN' % (a, b), dark=(sid in ('l%d-break' % n, 'end')))
        set_minutes_note(D, sid, a, b)
    for sid in OPTIONAL[n]:
        if _read(D, sid) is None: continue
        set_pill(D, sid, OPT_REMIND if sid in REMIND else OPT)
        drop_minutes_note(D, sid)
    # 3. title slide time plan
    title_notes(D, n)
    # 4. general wording that quotes minutes
    ws = ws_start(n)
    sub_deck(D, [('At minute 40 invite the WHOLE group', 'When the worksheet starts (minute %d) invite the WHOLE group' % ws),
                 ('At minute 40 read questions 1 and 2 aloud', 'At minute %d read questions 1 and 2 aloud' % ws)] if ws != 40 else [])
    sub_slide(D, p_ + 'break', [('Five minutes. Online', 'Four minutes. Online')])
    warm_end = BOUNDS[n]['wu']
    sub_slide(D, p_ + 'warm2', [('If time is short, take questions 1 to 3 only: the 3-minute sneak-peek puzzles follow on the next slide.',
                                 'Ask questions 1 to 3. Ask 4 and 5 only if the clock at minute %d is on time. The 4-minute sneak-peek puzzles follow on the next slide.' % (warm_end - 2)),
                                (r'(Ask questions 1 to 3\. Ask 4 and 5 only if the clock at minute )\d+', r'\g<1>%d' % (warm_end - 2), True)])
    marks_if_on_time(D, n)
    micro_reset(D, n)
    sub_slide(D, p_ + 'exit', [('after the exit ticket)', 'after the exit ticket)')])
    # 5. lesson-specific cuts and wording
    fn = globals().get('lesson_%d' % n)
    if fn: fn(D)
    if BOUNDS[n]['fl']:
        sub_slide(D, p_ + 'reflect', [('</aside>', ' After the look-back, minutes %d to 90 are flex time: the buffer. If the lesson ran late, finish whatever is still open (stamps, the look-back). If you are on time, say goodbye and thank the parents. Do not start anything new.</aside>' % BOUNDS[n]['lb']),
                                      (r'( After the look-back, minutes \d+ to 90 are flex time: the buffer\.[^<]*?)( After the look-back, minutes \d+ to 90 are flex time: the buffer\.)', r'\1', True)])


def marks_if_on_time(D, n):
    """Quick questions 4 and 5 are marked '(if on time)' on the warm-up slide (audit U2)."""
    sid = 'l%d-warm2' % n
    s = _read(D, sid)
    if s is None or '(if on time)' in s: return
    tag = ' <span style="font-size:0.62em;font-weight:700;color:#5B6785">(if on time)</span>'
    def rep(m):
        return m.group(1) + m.group(2) + tag + m.group(3)
    t = re.sub(r'(<span style="color:#1F7A6F;font-weight:800">[45]\.</span>  )([^<]*)(</p>)', rep, s)
    if t != s: open(_path(D, sid), 'w').write(t)


# ------------------------------------------------------------------------------------------------ lesson-specific
def lesson_1(D):
    # opening: the cover slide is gone; routine is shown for 30 seconds naming the four phases
    sub_slide(D, 'routine', [('Show this slide in Lesson 1 and refer back to it in Lesson 2. After that children know the routine. Online: ask children to keep materials and the workbook beside them from the first minute.',
                              'Show this slide for 30 seconds in Lesson 1 and name only the four phases: warm-up, explore, teach, worksheet. Do not read the table. Refer back to it in Lesson 2; after that children know the routine. Online: ask children to keep materials and the workbook beside them from the first minute. The times on the slide are the usual lesson; in Lesson 1 everything before the worksheet starts 2 minutes later because the opening takes 4 minutes. Clock checks (say them to yourself): minute 14 (end of sneak-peek puzzles), minute 42 (start of worksheet) and minute 72. If you are more than 2 minutes behind at the worksheet, use the skip list in the tutor guide; never shorten the worksheet below 28 minutes. Never drop the camera and privacy moment, the look-back or the “you can pass” lines.')])
    sub_slide(D, 'routine', [(r'<tr style="background:#FFFFFF"><td>0–10</td>.*?</tr>\n<tr><td>10–25</td>.*?</tr>\n<tr style="background:#FFFFFF"><td>25–35</td>.*?</tr>\n<tr><td>35–40</td>.*?</tr>',
                              '<tr style="background:#FFFFFF"><td>2–12</td><td><b>Warm-up</b></td><td>A quick game, quick questions and 4 minutes of sneak-peek puzzles</td></tr>\n<tr><td>12–26</td><td><b>Explore</b></td><td>Hands-on with objects, in pairs</td></tr>\n<tr style="background:#FFFFFF"><td>26–36</td><td><b>Teach</b></td><td>Worked examples and the key idea</td></tr>\n<tr><td>36–40</td><td><b>Brain break</b></td><td>Move and drink water</td></tr>', True),
                             ('<td>72–80</td>', '<td>72–79</td>'),
                             ('<tr style="background:#FFFFFF"><td>80–90</td>', '<tr style="background:#FFFFFF"><td>79–90</td>'),
                             ('then a two-minute look-back (you can pass)', 'then a three-minute look-back (you can pass), then a goodbye')])
    sub_slide(D, 'l1-title', [('each child uses a paper strip and a pencil.', 'each child uses a paper strip and a pencil. Parents cut out and tape the number strip before the lesson.')])
    # Explore: parents cut and tape the strip before the lesson
    sub_slide(D, 'l1-explore1', [('Take your number strip (0 to 50). It is in your Inquirer Kit.', 'Take your number strip (0 to 50), already cut out and taped end to end.')])
    sub_slide(D, 'l1-explore1', [(' Go further (what-if) is on this slide', ' The number strip is cut out and taped before the lesson (parents are asked in the materials message), so no cutting is needed in class. Go further (what-if) is on this slide')])


def lesson_2(D):
    sub_slide(D, 'l2-ws2', [('Magic triangle.', 'Magic triangle.')])
    sub_slide(D, 'l2-teachpage2', [(' Do not remove', ' Do not remove')])


STAR = ('<svg aria-label="star" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" style="width:34px;height:34px;vertical-align:-6px;margin-right:8px">'
        '<polygon points="12,1.5 15,8.6 22.5,9.2 16.8,14.1 18.6,21.5 12,17.6 5.4,21.5 7.2,14.1 1.5,9.2 9,8.6" fill="#FFC93C" stroke="#1B2A49" stroke-width="1.6" stroke-linejoin="round"/></svg>')


def add_before_footer(D, sid, html, note_add=''):
    s = _read(D, sid)
    if s is None: return False
    mark = '<p style="position:absolute;left:128px;bottom:64px'
    if mark not in s: return False
    s = s.replace(mark, html + '\n' + mark, 1)
    if note_add: s = s.replace('</aside>', note_add + '</aside>', 1)
    open(_path(D, sid), 'w').write(s)
    return True


def lesson_3(D):
    # the old "your turn" (b) and (c) of the Mini-lesson are take-home: they sit on the Think harder slide
    s = _read(D, 'l3-stretch')
    if s is not None and 'Take-home' not in s:
        c = card(p(STAR + '<b>Take-home:</b> The key is lost! Cats have 3 pictures and 6 children chose cats. What is 1 picture worth? Then dogs have 5 pictures: how many children chose dogs?', 28, 600, raw=True), SOFT)
        s2 = _read(D, 'l3-stretch').replace('font-size:36px', 'font-size:32px'); open(_path(D, 'l3-stretch'), 'w').write(s2)
        add_before_footer(D, 'l3-stretch', c, ' Take-home (from the Mini-lesson, not for class time): the key is lost, cats have 3 pictures and 6 children chose cats. Answer: 1 picture = 2 children (try a key of 1: 3 children is too few; try 2: 2, 4, 6). Dogs have 5 pictures: 10 children.')


def lesson_4(D):
    pass


def lesson_5(D):
    pass


def lesson_6(D):
    pass


def lesson_7(D):
    pass


def lesson_8(D):
    sub_slide(D, 'l8-warm1', [(r'(as few questions as they can) (?:together ?)+', r'\1 together', True)])


def lesson_9(D):
    # brain break: giant steps in place (not across the room)
    sub_slide(D, 'l9-break', [('Giant steps. Take your biggest step and your smallest step across the room. Count each: which needs more steps?',
                               'Giant steps, in place. Take 5 giant steps on the spot, then 5 tiny steps. Which would take you further across a room? Why?')])
    # explore: the cube strip is cut out before the lesson
    sub_slide(D, 'l9-explore1', [('</aside>', ' The cube strip (Strip A) is cut out before the lesson (parents are asked in the materials message), so no cutting is needed in class.</aside>'),
                                 (r'( The cube strip \(Strip A\) is cut out before the lesson[^<]*?)( The cube strip \(Strip A\) is cut out before the lesson)', r'\1', True)])


def lesson_10(D):
    # Explore: card for 6 minutes, swap, round 2 for 4 minutes, ONE debrief question, 20-second pair reports
    sub_deck(D, [('ONE card for 10 minutes. Then you may swap with another pair for 4 minutes.', 'ONE card for 6 minutes. Then you may swap with another pair for 4 minutes.'),
                 ('ONE card for 10 minutes. Then swap cards with another pair for 4 minutes.', 'ONE card for 6 minutes. Then swap cards with another pair for 4 minutes.')])
    sub_slide(D, 'l10-explore1', [(r'<aside>.*?</aside>', '<aside>Minutes 10 to 11. Explain the plan, then move to the next slide with the four puzzle cards. Each pair works on ONE card for 6 minutes (11 to 17), you give 1 minute to swap (17 to 18), then a 4-minute second round (18 to 22), then ONE debrief question and 20-second pair reports (22 to 28). Pairs read their own card: do not read all four aloud. A pair that is still stuck keeps its card for round 2. Materials: the four puzzle cards (workbook Puzzle cards page), play coins, cubes, mini whiteboards. Online: each pair chooses a card from the workbook page. Reporting back is optional: say one thing you tried, not the answer.</aside>', True)])
    sub_slide(D, 'l10-cards', [(r'<aside>.*?Answers: ', '<aside>Minutes 11 to 17. Each pair works on ONE puzzle card for 6 minutes (the printed cards are on the Puzzle cards page of the workbook; online, each pair chooses a card). Pairs read their own card; do not read all four aloud. A middle child solves any card in 2.5 to 4 minutes; the Coins card can take longer, so a pair still stuck keeps its card for round 2. At minute 17 pairs swap with another pair for a 4-minute second round (see the next slide). Reporting back is optional: one thing you tried, not the answer. Answers: ', True)])
    sub_slide(D, 'l10-explore2', [(r'<aside>.*?Answers: ', '<aside>Minutes 17 to 28. 17 to 18: pairs swap cards. 18 to 22: second round (4 minutes). Then ask ONE debrief question: "What helped you when you were stuck?" Take 20-second pair reports from volunteers, one thing they tried, not the answer. Questions 1 and 2 are not asked. Answers: ', True),
                                  (r'<p style="font-size:40px;font-weight:600"><span style="color:#1F7A6F">3\.</span>  ', '<p style="font-size:40px;font-weight:600">', True),
                                  (r'<div style="background:#FFFFFF;[^"]*"><p style="font-size:40px;font-weight:600"><span style="color:#1F7A6F">[12]\.</span>[^<]*</p></div>\n', '', True)])
    sub_slide(D, 'l10-explore2', [('Explore: talk about it', 'Explore: one question')])
    # Mini-lesson: the Explore cards are the practice (the two "your turn" slides are gone)
    sub_slide(D, 'l10-we3', [('Count the places aloud with the children', 'Count the places aloud with the children')])
    # Worksheet page 2 carries Q9 again (about 3.6 minutes); the three re-teach slides are optional reminders
    s = _read(D, 'l10-ws2')
    if s is not None and 'Q9</span>' not in s:
        row = '<p style="font-size:38px;font-weight:600;line-height:1.3"><span style="color:#1F7A6F;font-weight:800">Q9</span>  Make a puzzle for a friend. Write the puzzle and its answer. We swap puzzles in talk time.</p>'
        m = re.search(r'(<p style="[^"]*"><span style="color:#1F7A6F;font-weight:800">Q8</span>[^<]*</p>)', s)
        if m: s = s.replace(m.group(1), m.group(1) + row.replace('font-size:38px', 'font-size:%s' % re.search(r'font-size:(\d+px)', m.group(1)).group(1)), 1)
        open(_path(D, 'l10-ws2'), 'w').write(s)
    sub_slide(D, 'l10-ws2', [('Q9: check that the puzzle has exactly one answer and that the child can say how to start it.', 'Q9 (make a puzzle for a friend) is written on this page, about 3 to 4 minutes at the end: check that the puzzle has exactly one answer and that the child can say how to start it. The three re-teach slides (picture graph, triangles, length) are optional reminders: show one only if a child asks.')])
    sub_slide(D, 'l10-talk', [('Make a puzzle for a friend (workbook Q9) with its answer. Swap it with a partner and solve it. Then pick one puzzle and teach it to the group in two sentences.',
                               'Swap the puzzle you wrote (workbook Q9) with a partner and solve it. Then pick one puzzle and teach it to the group in two sentences.'),
                              ('Q9 (make a puzzle for a friend) is done here, not on worksheet page 2: pairs write a puzzle with its answer, swap, and solve each other\'s.',
                               'Plan: swap puzzles and solve (about 2.5 minutes), 2-minute pair talk, then volunteers. Q9 was written on worksheet page 2.')])
    # Exit + certificates (79 to 87): say the certificate line once, then 10 seconds per child
    sub_slide(D, 'l10-exit', [('Minutes 79 to 84. Answer: Open.', 'Minutes 79 to 84. Answer: Open.')])
    sub_slide(D, 'end', [('Hand out certificates. Ask each child to name one puzzle they enjoyed. Give parents the one-page summary from the tutor guide.',
                          'Minutes 84 to 87. Hand out certificates. Say the certificate line ONCE to the whole group, then spend about 10 seconds on each child with one specific thing they did well. Ask “which puzzle did you enjoy?” as a thumbs-up question, or only of volunteers: do not go round every child. Give parents the one-page summary from the tutor guide. The look-back follows at minute 87 and is never shortened.')])
    # the certificates belong to the exit block: the end slide comes before the look-back
    def fx(o):
        if 'end' in o: o.remove('end')
        o.insert(o.index('l10-reflect'), 'end')
    order_edit(D, fx)


# ------------------------------------------------------------------------------------------------ budget files
def write_json():
    lessons = {}
    slides = {}
    for n in range(1, 11):
        D = os.path.join(ROOT, 'split', 'l%d' % n, 'project')
        order = json.load(open(os.path.join(D, 'deck.json')))['order']
        lessons[str(n)] = {'parts': [{'title': t, 'start': a, 'end': b} for t, a, b in parts(n)],
                           'optional_slides': [s for s in order if s in OPTIONAL[n]]}
        slides[str(n)] = {s: [a, b] for s, (a, b) in SLIDES[n].items() if s in order}
    json.dump({'lessons': lessons}, open(os.path.join(ROOT, 'hp', 'budget.json'), 'w'), indent=1, ensure_ascii=False)
    json.dump(slides, open(os.path.join(ROOT, 'hp', 'budget_slides.json'), 'w'), indent=1, ensure_ascii=False)
    print('wrote hp/budget.json and hp/budget_slides.json')


if __name__ == '__main__':
    write_json()
