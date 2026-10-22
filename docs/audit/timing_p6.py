#!/usr/bin/env python3
"""Timing model for the P6 lessons (ANALYSIS ONLY: reads the repo, writes nothing but stdout).

Usage:  python3 docs/audit/timing_p6.py [--json] [--lesson N]

What it does
  * Loads the real content with node (p6/data.js + hp/common_html.js) and the real decks in split/p6lN.
  * Counts words of SAY lines, questions read aloud, slide narration, answers, per lesson part.
  * Adds waiting time, transitions, child activity time and the REC cue lines, in seconds.
  * Prints one table per lesson (part, scripted, speaking, waiting, activity, transition, needed, diff, flag).

Model (identical for every level so results compare)
  speaking : tutor speech 140 wpm (SAY lines, think-aloud, slide narration); questions read aloud 130 wpm
  waiting  : 10 s after each question put to the group + 20 s to take one or two answers; 'hold up boards' 30 s
  transit. : 25 s per slide change (20 / 30 in the fast / slow runs); 90 s (60 / 120) per move to or from breakout
             rooms and per hand-out / find-materials moment; 120 s to start a worksheet
  activity : child time on explore, worksheet, brain break and thinking puzzles, judged from the actual task
  REC cues : 10 s at the start of each part (9 parts + looking back + closing = 11 cues)
  Slides shown while children work independently (Think harder / Go further / see-it / walk-through) cost no
  group time, because the tutor is idle then; they are listed as tutor workload only.
The numbers are estimates, not stopwatch timings. Group size 8 (the maximum the guide allows).
"""
import json, re, html, subprocess, sys, os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
SAY_WPM, READ_WPM = 140.0, 130.0
GROUP = 8
GREET = 30            # greet the children by name
REC_NOTICE = 15       # say that the lesson is recorded (levels/reccues.js RULES.privacy)
FACT = 0.8            # share of a worked-example slide's printed words that is actually spoken
CHECK_Q = 60          # check-together: per numbered question (volunteer, answer shown, children mark in a different colour)
FOOTER = 'Math Inquirers P6 • Notice it. Test it. Explain why.'

SCEN = {  # slide change, breakout/materials move, activity multiplier
    'fast': dict(slide=20, bo=60, act=0.85),
    'central': dict(slide=25, bo=90, act=1.00),
    'slow': dict(slide=30, bo=120, act=1.15),
}

# ---- fixed SAY lines copied from p6/guide.js (same in every lesson) -------------------------------
SNEAK_SAY = ('Two sneak-peek puzzles. They are ideas we have not learnt yet, so guessing is welcome and “I do not know” is welcome. '
             'Nobody is marked. Write your answers on your own paper. When I say “show”, everyone holds their paper to the camera at the same moment.')
SNEAK_CLOSE = 'Both of these are what we learn today.'
PARTNER_SAY = 'Talk to your partner while you work. I will come round and ask you questions.'
PAIRS_SAY = ('Pairs first. Read each question aloud and talk about it before you write. '
             'I am not looking for speed. I am looking for good thinking.')
WS_OPEN = 'Minute 40: give out the workbook. Read the title of the lesson aloud. Say Pairs first. Talk before you write.'
LB_SAY_SHORT = ('Two minutes, just for you, in the Looking back box: something I did well, the hardest part, and what helped. '
                'You can write pass. Nobody marks this. If you are still stuck, tick that box and I will check in with you in the open session.')
LB_SAY = ('Two minutes, just for you, in the Looking back box on the Finish page. Finish: something I did well, the hardest part was, '
          'and tick what helped you. You can write pass. If you are still stuck, tick that box and I will check in with you in the open '
          'session, in the shared room, with your parent nearby. Nobody marks this and nobody has to show it.')


def wc(s):
    return len(re.findall(r'\S+', s or ''))


def sec(words, wpm):
    return words / wpm * 60.0


# ---- per-lesson judgement inputs (seconds unless stated) -------------------------------------------
# sneak: (access puzzle, thinking puzzle) child thinking seconds
# warm_game: seconds of the game itself (items x 35 s where item-by-item), excluding the spoken intro
# exp_act: minutes of child task time in Explore (incl. opening and building in Scratch)
# demo: seconds the tutor spends building / running code live in the mini-lesson while children copy
# brk: seconds of the movement game itself
# exit_write: minutes children need for the exit slip
# items: worksheet 'Start here' items for a MIDDLE child: (label, page, minutes)
INP = {
    1: dict(sneak=(45, 60), warm_game=240, exp_act=8.5, demo=180, brk=90, exit_write=3.0,
            items=[('Q1 squares table, rule, 100th, which pattern', 1, 5.0), ('Q2 two sequences, 6 cells', 1, 3.5), ('Q3 backwards / is 150 in it', 1, 3.0),
                   ('Q4 predict + trace table + repeat 100', 2, 4.0), ('Q5 plan code (blocks + last number)', 2, 4.0), ('Q6 spot the bug + fix', 2, 3.0)]),
    2: dict(sneak=(60, 75), warm_game=210, exp_act=6.5, demo=240, brk=120, exit_write=3.0,
            items=[('Q1 factor table (5 nos) + circle primes + Ali 87', 1, 6.0), ('Q2 factor trees 72, 150 + product', 1, 3.5),
                   ('Q3 trace factor counter (6 rows) + change to 13', 2, 5.5), ('Q4 Goldbach 24 + why 27 fails', 2, 3.5),
                   ('Q5 numbers 1-30 with exactly 3 factors + notice', 2, 4.5), ('Q6 order the blocks + count', 2, 4.0)]),
    3: dict(sneak=(40, 50), warm_game=180, exp_act=6.5, demo=0, brk=90, exit_write=1.5,
            items=[('Q1 number line a,b,c', 1, 2.5), ('Q2 Harbin temperatures a-e', 1, 3.5), ('Q3 sea level a-c', 1, 2.5), ('Q4 six negative-number sums', 1, 4.5),
                   ('Q5 trace x, 4 repeats + (b)', 2, 3.0), ('Q6 lift bug a-c', 2, 2.5), ('Q7 diver plan 3 blanks + (b)', 2, 3.0)]),
    4: dict(sneak=(40, 75), warm_game=240, exp_act=11.0, demo=0, brk=120, exit_write=2.0,
            items=[('Q1 guess my rule x4 tables', 1, 4.5), ('Q2 two machines a-c', 1, 4.0), ('Q3 four backwards equations + checks', 1, 5.0),
                   ('Q4 predict the code a-c', 2, 2.5), ('Q5 trace table + rule + repeat 10', 2, 2.5), ('Q6 plan a search 8n-5=91', 2, 4.0), ('Q7 number trick a-c', 2, 4.5)]),
    5: dict(sneak=(60, 75), warm_game=240, exp_act=8.5, demo=180, brk=90, exit_write=2.0,
            items=[('Q1 outfits (two counts)', 1, 1.5), ('Q2 digit cards: list 9 two-digit numbers, count 3-digit', 1, 5.0), ('Q3 trace nested loop, 6 rows + b,c,d', 1, 6.0),
                   ('Q4 handshakes 7 friends + Ali error', 2, 4.0), ('Q5 grid routes + puddle', 2, 6.0), ('Q6 plan code 3 gaps + (a)(b)', 2, 5.5)]),
    6: dict(sneak=(45, 90), warm_game=210, exp_act=6.5, demo=60, brk=90, exit_write=2.5,
            items=[('Q1 spinner four parts', 1, 3.5), ('Q2 predict coin code a-c', 1, 3.5), ('Q3 bag of counters', 1, 2.0),
                   ('Q4 difference game table ~24 cells + P + fair?', 2, 7.0), ('Q5 plan doubles code a-b', 2, 4.0)]),
    7: dict(sneak=(60, 75), warm_game=150, exp_act=11.0, demo=135, brk=120, exit_write=2.0,
            items=[('Q1 regular polygon table (~10 cells) + a, b', 1, 6.5), ('Q2 predict 9-gon program a-c', 1, 3.5),
                   ('Q3 trace running total a-d', 2, 5.0), ('Q4 star table 9-point', 2, 4.0), ('Q5 inside-angle table + rule', 2, 6.0)]),
    8: dict(sneak=(40, 90), warm_game=180, exp_act=8.5, demo=150, brk=90, exit_write=2.0,
            items=[('Q1 five clock / calendar puzzles', 1, 4.0), ('Q2 Caesar: code PIZZA, decode 9 letters, forward shift', 1, 7.0),
                   ('Q3 trace W A Y table', 2, 5.0), ('Q4 crack the code a-c', 2, 3.5), ('Q5 two shifts a-d', 2, 5.0)]),
    9: dict(sneak=(60, 75), warm_game=150, exp_act=9.0, demo=240, brk=120, exit_write=2.5,
            items=[('Q1 mean + balance check', 1, 3.0), ('Q2 missing value a-c', 1, 3.0), ('Q3 four predict-then-compute', 1, 4.5),
                   ('Q4 mean, median, mode + typical?', 1, 4.5), ('Q5 trace list sum + any-length fix', 2, 6.0), ('Q6 temperatures plan code', 2, 4.5)]),
}
# questions on each worksheet page (for the check-together slides)
PAGE_Q = {1: (3, 3), 2: (2, 4), 3: (4, 3), 4: (3, 4), 5: (3, 3), 6: (3, 2), 7: (2, 3), 8: (2, 3), 9: (4, 2)}
# scripted ws1 / ws2 independent windows read off the slide labels (minutes)
WIN = {1: (10, 13), 2: (14, 11), 3: (12, 15), 4: (12, 15), 5: (13, 11), 6: (12, 13), 7: (10, 17), 8: (10, 16), 9: (11, 14)}
SCRIPTED = [('Opening', 2), ('Sneak-peek puzzles', 3), ('Warm-up', 5), ('Explore', 15), ('Mini-lesson', 10), ('Brain break', 5),
            ('Worksheet', 35), ('Talk time', 7), ('Exit slip, looking back, close', 8)]


def load_content():
    js = ("const C=require(%r);const L=require(%r);const H=Object.assign({},C,{fig:s=>'<div class=\"FIG\"></div>'});"
          "console.log(JSON.stringify(L.content.map(c=>({lesson:c.lesson,script:c.script,deck:c.deck,qbank:c.qbank,gaps:c.gaps,th:c.lesson.th,wb:c.workbook(H).map(String)}))));"
          % (os.path.join(ROOT, 'hp/common_html.js'), os.path.join(ROOT, 'p6/data.js')))
    out = subprocess.run(['node', '-e', js], capture_output=True, text=True, check=True).stdout
    return json.loads(out)


def load_slides(n):
    d = os.path.join(ROOT, 'split/p6l%d/project' % n)
    deck = json.load(open(d + '/deck.json'))
    res = []
    for sid in deck['order']:
        s = open('%s/slides/%s.html' % (d, sid), encoding='utf-8').read()
        m = re.search(r'<aside>(.*?)</aside>', s, re.S)
        notes = html.unescape(m.group(1)) if m else ''
        body = s[:m.start()] if m else s
        body = re.sub(r'<svg.*?</svg>', ' ', body, flags=re.S)
        body = re.sub(r'<[^>]+>', ' ', body)
        vis = re.sub(r'\s+', ' ', html.unescape(body)).strip().replace(FOOTER, '').strip()
        vis = re.sub(r'^(?:[\d.]+–[\d.]+ MIN|Optional, if you finish early)\s*', '', vis)
        builds = len(re.findall(r'data-build|data-fragment|class="build', s))
        res.append(dict(id=sid.split('-', 1)[1], vis=vis, notes=notes, words=wc(vis), builds=builds))
    return res


class Part:
    def __init__(self, name, scripted):
        self.name, self.scripted = name, scripted
        self.speak = self.wait = self.act = self.trans = 0.0
        self.notes = []

    @property
    def need(self):
        return (self.speak + self.wait + self.act + self.trans) / 60.0

    def flag(self):
        d = self.need - self.scripted
        if d >= 2: return 'OVER'
        if d >= 1: return 'TIGHT'
        if d <= -3: return 'LOOSE'
        return 'OK' if d < -0.5 else 'OK (no slack)'


def model_lesson(n, C, sc, fx=None):
    """fx = None gives the lesson as written. fx = dict of proposed fixes (see FX below) gives the lesson after the fixes."""
    fx = fx or {}
    c = C[n - 1]; sl = load_slides(n); S = {s['id']: s for s in sl}
    slide, bo, am = sc['slide'], sc['bo'], sc['act']
    L, SC, DK, GP = c['lesson'], c['script'], c['deck'], c['gaps']
    I = INP.get(n)
    if n == 10:
        return model_l10(C, sc, sl, fx)
    P = []
    REC = 10

    # Opening
    p = Part('Opening', 2); P.append(p)
    p.speak = sec(sum(wc(x) for x in SC['hook']), SAY_WPM) + sec(wc(DK['today']), READ_WPM) + REC + REC_NOTICE
    p.wait = GREET + 10
    p.trans = slide
    # Sneak
    p = Part('Sneak-peek puzzles', 3); P.append(p)
    cap = 15 if fx.get('sneak_lean') else 25
    ans = sum(min(cap, wc(x[1])) for x in GP['sneak'])
    p.speak = REC + sec(wc(SNEAK_SAY), SAY_WPM) + sec(sum(wc(x[0]) for x in GP['sneak']), READ_WPM) + sec(ans + wc(SNEAK_CLOSE), SAY_WPM)
    # as written: a hold-up-your-paper moment for each puzzle + 30 s of reaction when the answers are revealed
    p.wait = 30 if fx.get('sneak_lean') else 2 * 30 + 10 + 20
    p.act = (I['sneak'][0] + I['sneak'][1]) * am
    p.trans = slide
    # Warm-up
    p = Part('Warm-up', 5); P.append(p)
    nq = fx.get('warm_q', len(DK['warmQs']))
    qs = DK['warmQs'][:nq]
    p.speak = REC + sec(wc(DK['warmGame']) + sum(wc(x) for x in SC['warmIntro']), SAY_WPM) + sec(sum(wc(q[0]) for q in qs), READ_WPM)
    p.wait = nq * 30 + 20
    p.act = (I['warm_game'] - fx.get('warm_cut_s', 0)) * am
    p.trans = 2 * slide
    # Explore
    p = Part('Explore', 15); P.append(p)
    nask = fx.get('exp_q', 3)
    asks = DK['expAsk'][:nask]
    exp_sp = sec(sum(wc(x) for x in SC['predict']) + wc(PARTNER_SAY), SAY_WPM) + sec(sum(wc(x) for x in DK['expSetup']), READ_WPM)
    go_read = 0 if fx.get('go_drop') else sec(min(40, wc(GP['go'][0])), READ_WPM)
    ask = sec(sum(wc(q[0]) for q in asks), READ_WPM) + sec(sum(min(25, wc(q[1])) for q in asks), SAY_WPM)
    p.speak = REC + exp_sp + go_read + ask
    p.wait = nask * 30 + 30  # the discussion questions + the written prediction
    p.act = fx.get('exp_act', I['exp_act']) * 60 * am
    nsl = 3 + (1 if 'setup' in S else 0) - (1 if fx.get('go_drop') else 0) - fx.get('exp_slide_merge', 0)
    p.trans = nsl * slide + bo + bo + int(bo * 2 / 3)   # find materials / Scratch window, out to rooms, back from rooms
    # Mini-lesson
    p = Part('Mini-lesson', 10); P.append(p)
    ids = [s['id'] for s in sl]
    a = ids.index('teach1'); b = ids.index('key')
    mini_all = sl[a:b + 1]
    drop = set(fx.get('mini_drop', [])); merge = set(fx.get('mini_merge', []))
    mini = [s for s in mini_all if s['id'] not in drop]
    narr = sum(max(0, s['words'] - 3) for s in mini if not s['id'].startswith('try') and s['id'] != 'key')
    say_total = sum(wc(x) for x in SC['think'])
    key_say = wc(DK['keyHead']) + wc(DK['keyBig']) + 6
    tryread = sum(max(0, s['words'] - 3) for s in mini if s['id'].startswith('try'))
    p.speak = REC + sec(max(FACT * narr, say_total), SAY_WPM) + sec(key_say, SAY_WPM) + sec(0.6 * tryread, READ_WPM)
    ntry = sum(1 for s in mini if s['id'].startswith('try'))
    npred = sum(1 for s in mini if s['id'].startswith('we') or s['id'] in ('code1', 'change'))
    p.wait = npred * 30 + ntry * (75 + 30) + 15
    demo = fx.get('demo', I['demo'])
    p.act = demo * am
    p.trans = (len(mini) - len(merge & {x['id'] for x in mini})) * slide
    p.notes.append('%d slides (%d your-turn, %d live-code seconds)' % (len(mini), ntry, demo))
    # Brain break
    p = Part('Brain break', 5); P.append(p)
    p.speak = REC + sec(wc(DK['brk']), SAY_WPM)
    p.act = (I['brk'] * am) + fx.get('water', 120) + 30   # the game + water/toilet + settle back
    p.trans = slide
    # Worksheet
    p = Part('Worksheet', 35); P.append(p)
    ib = ids.index('break')
    ws = []
    for s_ in sl[ib + 1:]:
        if s_['id'] in ('stretch', 'challenge', 'chdiag', 'chwalk', 'talk', 'exit', 'reflect'): break
        ws.append(s_)
    wmerge = set(fx.get('ws_merge', []))
    teach = [s_ for s_ in ws if (s_['id'].startswith('teach') or s_['id'].startswith('try'))]
    tasks = [s_ for s_ in ws if s_['id'] in ('ws1', 'ws2')]
    checks = [s_ for s_ in ws if s_['id'] in ('ws1ans', 'ws2ans')]
    sp = REC + sec(wc(PAIRS_SAY) + wc(WS_OPEN), SAY_WPM)
    wt = 0.0
    for s_ in teach:
        if s_['id'].startswith('try'):
            sp += sec(0.6 * max(0, s_['words'] - 3), READ_WPM); wt += 75 + 30
        else:
            sp += sec(FACT * max(0, s_['words'] - 3), SAY_WPM); wt += 30
    if not fx.get('ws_noread'):
        for s_ in tasks:
            sp += sec(max(0, s_['words'] - 3), READ_WPM)
    q1, q2 = PAGE_Q[n]
    moved = fx.get('ws_move', [])            # item indexes moved to take-home
    items_all = I['items']
    items = [it for k, it in enumerate(items_all) if k not in moved]
    qn_moved = [0, 0]
    for k in moved:
        if items_all[k][0].startswith('Q'): qn_moved[items_all[k][1] - 1] += 1
    chq = fx.get('check_q', CHECK_Q)
    for s_, qn, mv in zip(checks, (q1, q2), qn_moved):
        w_ = max(0, s_['words'] - 3)
        sp += sec(w_ * (1 - mv / max(1, qn)), READ_WPM) * (0.5 if fx.get('check_q') else 1.0)
        wt += (qn - mv) * chq
    p.speak = sp
    p.wait = wt
    mid = sum(i[2] for i in items)
    p.act = mid * 60 * am + 120      # independent work (middle child) + 2 min to get started
    p.trans = (len(ws) - len(wmerge)) * slide + 60   # every group slide change + pairs stay in the main room (30 s to pair up, 30 s back)
    p.notes.append('worksheet mid-child work %.1f min on %d Qs' % (mid * am, len(items)))
    # Talk time
    p = Part('Talk time', 7); P.append(p)
    tq = SC['talk'][:1] if fx.get('talk_lean') else SC['talk']
    p.speak = REC + sec(sum(wc(x) for x in tq), READ_WPM) + sec(min(60, wc(SC['talkAns'])), SAY_WPM)
    p.wait = (10 if fx.get('talk_lean') else 20) + 30
    p.act = ((90 if fx.get('talk_lean') else 120) + 3 * 35) * am
    p.trans = slide
    # Exit
    p = Part('Exit slip, looking back, close', 8); P.append(p)
    lb = LB_SAY if not fx.get('exit_lean') else LB_SAY_SHORT
    p.speak = 3 * REC + sec(wc(L['exit']['q']), READ_WPM) + sec(sum(wc(x) for x in SC['close']) + wc(lb), SAY_WPM) + sec(10, SAY_WPM)
    p.wait = (30 + 30) if fx.get('exit_lean') else (GROUP * 10 + 30)   # lean: everyone holds the slip up at once, then goodbye
    p.act = I['exit_write'] * 60 * am + 120   # exit slip + looking back (2 min)
    p.trans = 2 * slide
    return P, dict(slides=len(sl), mini=mini, ws=ws, items=items, window=WIN[n])


def model_l10(C, sc, sl, fx=None):
    """Lesson 10 follows its own plan (p6/guide.js 'Lesson 10 timing' line, same as the deck):
    0-2 opening, 2-5 sneak, 5-8 warm, 8-23 challenge round, 23-30 starters, 30-32 break, 32-62 plan and build,
    62-85 showcase, 85-86 talk, 86-88 exit slip, 88-90 looking back + certificates."""
    fx = fx or {}
    c = C[9]; SC, DK, GP, L = c['script'], c['deck'], c['gaps'], c['lesson']
    slide, bo, am = sc['slide'], sc['bo'], sc['act']
    REC = 10
    S = {s['id']: s for s in sl}
    nar = lambda k: max(0, S[k]['words'] - 3)
    P = []
    p = Part('Opening', 2); P.append(p)
    p.speak = REC + REC_NOTICE + sec(sum(wc(x) for x in SC['hook']), SAY_WPM) + sec(wc(DK['today']), READ_WPM)
    p.wait = GREET + 10; p.trans = slide
    p = Part('Sneak-peek puzzles', 3); P.append(p)
    cap = 15 if fx.get('sneak_lean') else 25
    ans = sum(min(cap, wc(x[1])) for x in GP['sneak'])
    p.speak = REC + sec(wc(SNEAK_SAY), SAY_WPM) + sec(sum(wc(x[0]) for x in GP['sneak']), READ_WPM) + sec(ans + wc(SNEAK_CLOSE), SAY_WPM)
    p.wait = 30 if fx.get('sneak_lean') else 2 * 30 + 10 + 20
    p.act = (40 + 90) * am; p.trans = slide
    p = Part('Warm-up (lightning relay)', 3); P.append(p)
    p.speak = REC + sec(wc(DK['warmGame']) + sum(wc(x) for x in SC['warmIntro']), SAY_WPM)
    if fx.get('no_relay'):
        p.speak = p.act = p.wait = p.trans = 0
    else:
        p.act = (fx.get('relay_n', GROUP) * 20) * am; p.wait = 30; p.trans = slide
    p = Part('Challenge round (teams of 2) + check', 15); P.append(p)
    items = [('Q1 hexagon chain a-d (rule, 101 sticks, code)', 1, 4.5), ('Q2 prime hunters a-c (49, 84, all pairs for 40)', 1, 6.0), ('Q3 quick-fire a-d', 1, 4.0)]
    keep = [it for k, it in enumerate(items) if k not in fx.get('ch_move', [])]
    nkeep = len(keep)
    ex2 = 0 if fx.get('drop_explore2') else nar('explore2')
    p.speak = REC + sec(nar('explore1') + nar('ws1') * (0 if fx.get('ws_noread') else 1) + nar('ws1ans') * nkeep / 3.0 + ex2, READ_WPM) + sec(wc(SC['predict'][0]), SAY_WPM)
    p.wait = 30 + nkeep * fx.get('check_q', CHECK_Q) + (0 if fx.get('drop_explore2') else 60)
    p.act = sum(i[2] for i in keep) * 0.8 * 60 * am   # teams of 2 share the work (x0.8)
    p.trans = (4 - (1 if fx.get('drop_explore2') else 0)) * slide + bo + int(bo * 2 / 3)
    p = Part('Starter projects (A-D)', 7); P.append(p)
    drop = set(fx.get('mini_drop', []))
    mini = [S[k] for k in ('teach1', 'we1', 'try1', 'we2', 'we3', 'key') if k in S and k not in drop]
    narr = sum(max(0, s_['words'] - 3) for s_ in mini if not s_['id'].startswith('try'))
    ntry = sum(1 for s_ in mini if s_['id'].startswith('try'))
    p.speak = REC + sec(FACT * narr, SAY_WPM) + sec(0.6 * sum(max(0, s_['words'] - 3) for s_ in mini if s_['id'].startswith('try')), READ_WPM)
    nlive = fx.get('starters_live', 4)
    p.wait = nlive * 30 + ntry * 105 + 15 + 3 * 15
    p.act = nlive * 45 * am      # run a starter on screen and show its result
    p.trans = len(mini) * slide
    p = Part('Brain break', 2); P.append(p)
    p.speak = REC + sec(wc(DK['brk']), SAY_WPM); p.act = 90 * am + fx.get('water', 120) + 30; p.trans = slide
    p = Part('Plan and build', 30); P.append(p)
    p.speak = REC + sec(FACT * (nar('teachplan') + nar('teachtest')), SAY_WPM) + sec(nar('ws2') * (0 if fx.get('ws_noread') else 1), READ_WPM)
    p.wait = 60 + 30
    plan = [('Q4 maths first (3 parts)', 5.0), ('Q5 planning table (4 cells)', 4.0), ('Q6 blocks + 3 tests written before running', 4.0),
            ('load a starter (.sb3 from the shared file) and open Scratch', 1.5), ('build the one change', 8.0), ('run the tests, compare, fix one bug', 6.0)]
    if fx.get('plan_lean'):
        plan = [('Q4 maths first, for the chosen starter only (a or b or c)', 2.0), ('Q5 planning table: idea, answer, twist (3 cells)', 3.0),
                ('Q6 three test rows written before running', 2.5), plan[3], ('build the one change', 8.0), ('run the tests, compare, fix one bug', 5.0)]
    p.act = sum(x[1] for x in plan) * 60 * am + 120   # + 2 min to get started
    p.trans = 3 * slide + 30
    p.notes.append('plan+build mid-child %.1f min' % (sum(x[1] for x in plan) * am))
    p = Part('Showcase (8 children)', 23); P.append(p)
    # deck/guide: 2 min 30 s each + 20 s switch, the audience question is answered during the switch; quick spoken stars add 15 s
    p.speak = REC + sec(nar('showcase'), READ_WPM)
    p.act = GROUP * fx.get('show_s', 150) * am
    p.wait = GROUP * (20 + (0 if fx.get('stars_chat') else 15))
    p.trans = slide
    p.notes.append('with 6 children: %.1f min' % ((6 * (150 * am + 35) + 60) / 60.0))
    p = Part('Talk time', 1); P.append(p)
    if not fx.get('no_talk'):
        p.speak = REC + sec(nar('talk'), READ_WPM)
        p.wait = 20 + 2 * 30; p.trans = slide
    p = Part('Exit slip', 2); P.append(p)
    p.speak = REC + sec(wc(L['exit']['q']), READ_WPM)
    p.act = 2.0 * 60 * am; p.wait = 30 if fx.get('exit_lean') else GROUP * 10; p.trans = slide
    p = Part('Looking back + certificates', 2); P.append(p)
    lb = LB_SAY_SHORT if fx.get('exit_lean') else LB_SAY
    if fx.get('cert_pdf'):
        p.speak = 2 * REC + sec(wc(lb) + sum(wc(x) for x in SC['close']) + 25, SAY_WPM)
        p.wait = 0
    else:
        p.speak = 2 * REC + sec(wc(lb) + sum(wc(x) for x in SC['close']) + wc(S['end']['notes']) * 0.35, SAY_WPM)
        p.wait = GROUP * 25            # hand over each certificate with one specific thing they did well
    p.act = 2.0 * 60 * am
    p.trans = 2 * slide
    return P, dict(slides=len(sl), mini=mini, ws=[], items=items + [(x[0], 2, x[1]) for x in plan], window=(10, 25))


def finishers(n, info, p_ws, am=1.0, block=35):
    """How many Start-here questions a LOW / MIDDLE / HIGH child completes in the independent window."""
    items = info['items']
    tut = p_ws.need * 60 - sum(i[2] for i in items) * 60 * am - 120   # tutor-led seconds in the worksheet block
    window = max(0.0, block * 60 - tut - 120) / 60.0                      # minutes left for independent work
    out = {}
    for name, mult in (('LOW', 1.6), ('MIDDLE', 1.0), ('HIGH', 0.65)):
        t = 0.0; done = 0.0
        for lab, pg, m in items:
            m = m * mult * am
            if t + m <= window: t += m; done += 1
            else:
                done += max(0.0, (window - t) / m); t = window; break
        out[name] = round(done, 1)
    hi_spare = max(0.0, window - sum(i[2] for i in items) * 0.65 * am)
    out['TH_items_HIGH'] = round(hi_spare / (5.0 * 0.8), 1)   # Think Harder 4-6 min, high child ~0.8
    out['window_min'] = round(window, 1)
    out['n_items'] = len(items)
    return out


# ---- proposed fixes (applied by model_lesson(..., fx=FX[n])) -----------------------------------------------
# sneak_lean   one hold-up moment for both puzzles, no reaction round, answers said in 15 words each
# warm_cut_s / warm_q   seconds cut from the game / number of quick questions kept (the first N in the deck order)
# go_drop      the Go further what-if leaves the group flow (it stays in the chat and on the workbook); exp_q = discussion questions kept
# exp_act      minutes of child task time in Explore after the cut; exp_slide_merge = explore slides merged away
# mini_drop / mini_merge   mini-lesson slides removed / folded into the previous slide;  demo = seconds of live code
# ws_merge     worksheet teaching slides folded into the previous teaching slide; ws_noread = preview slides ws1 / ws2 are shown, not read
# check_q      seconds per question in check-together (children self-mark from the slide; tutor explains the key question only)
# ws_move      worksheet items (index into INP[n]['items']) moved to take-home / the Finish page
# talk_lean    one talk question, pairs talk 90 s;  exit_lean = everyone holds the exit slip up at once + shorter looking-back line
FX = {
    1: dict(sneak_lean=1, warm_cut_s=70, warm_q=3, go_drop=1, exp_q=2, exp_act=5.0, demo=240, ws_merge=['teachplan', 'teachbug'], ws_noread=1, check_q=35, ws_move=[4], exit_lean=1, talk_lean=1),
    2: dict(sneak_lean=1, warm_cut_s=70, warm_q=3, go_drop=1, exp_q=2, demo=150, mini_drop=['try1'], ws_merge=['teachsq', 'teachplan'], ws_noread=1, check_q=35, ws_move=[4], exit_lean=1, talk_lean=1),
    3: dict(sneak_lean=1, warm_cut_s=30, warm_q=3, go_drop=1, ws_merge=['teachbug'], ws_noread=1, check_q=35, exit_lean=1),
    4: dict(sneak_lean=1, warm_cut_s=60, warm_q=3, go_drop=1, exp_q=2, exp_act=6.5, mini_drop=['try1'], ws_merge=['teachsearch', 'teachtrick'], ws_noread=1, check_q=35, ws_move=[6], exit_lean=1, talk_lean=1),
    5: dict(sneak_lean=1, warm_cut_s=70, warm_q=3, go_drop=1, exp_q=2, exp_act=5.0, mini_drop=['try2'], ws_merge=['teachhandcode', 'teachroute'], ws_noread=1, check_q=35, ws_move=[4], exit_lean=1, talk_lean=1),
    6: dict(sneak_lean=1, warm_cut_s=70, warm_q=3, go_drop=1, exp_q=2, mini_merge=['teachwhy'], ws_merge=['teachplan'], ws_noread=1, check_q=35, exit_lean=1),
    7: dict(sneak_lean=1, warm_q=3, go_drop=1, exp_q=2, exp_act=7.0, exp_slide_merge=1, ws_merge=['teachsum'], ws_noread=1, check_q=35, ws_move=[4], exit_lean=1, talk_lean=1),
    8: dict(sneak_lean=1, warm_cut_s=60, warm_q=3, go_drop=1, exp_q=2, exp_act=7.0, mini_drop=['try1'], mini_merge=['teachloop'], demo=120, ws_merge=['teachcomb'], ws_noread=1, check_q=35, ws_move=[4], exit_lean=1),
    9: dict(sneak_lean=1, warm_cut_s=50, warm_q=3, go_drop=1, exp_q=2, exp_act=6.0, demo=150, mini_merge=['change'], ws_merge=['teachif'], ws_noread=1, check_q=35, ws_move=[5], exit_lean=1, talk_lean=1),
    10: dict(sneak_lean=1, no_relay=1, show_s=135, ch_move=[1], drop_explore2=1, ws_noread=1, check_q=35, mini_drop=['try1'], starters_live=2, water=30, plan_lean=1,
             stars_chat=1, no_talk=1, exit_lean=1, cert_pdf=1),
}
# new budgets per part (minutes) in the order the model prints them; the last number is the flex (buffer) row.
BUD = {}


def budgets(P):
    import math
    b = [round(p.need * 2) / 2.0 for p in P]
    return b, 90 - sum(b)


def stats(n, C):
    c = C[n - 1]; SC = c['script']; sl = load_slides(n)
    say = sum(wc(x) for k in ('hook', 'warmIntro', 'predict', 'think', 'talk', 'close') for x in SC[k])
    say += wc(SNEAK_SAY) + wc(PARTNER_SAY) + wc(PAIRS_SAY) + wc(LB_SAY)
    optional = ('stretch', 'challenge', 'chdiag', 'chwalk')
    grp = [x for x in sl if x['id'] not in optional]
    nq = sum(1 for x in c['wb'] if 'class="p q' in x)
    nsub = sum(1 for x in c['wb'] if 'class="p sub' in x)
    return dict(slides=len(sl), group_slides=len(grp), vis_words=sum(x['words'] for x in grp), notes_words=sum(wc(x['notes']) for x in sl),
                say_words=say, wb_q=nq, wb_sub=nsub, builds=sum(x['builds'] for x in grp))


def table(n, P, sc_name='central'):
    rows = ['| Part | Scripted | Speaking | Waiting | Activity | Transit. | Needed | Diff | Flag |', '|---|---:|---:|---:|---:|---:|---:|---:|---|']
    ts = tn = 0.0
    for p in P:
        d = p.need - p.scripted
        rows.append('| %s | %d | %.1f | %.1f | %.1f | %.1f | %.1f | %+.1f | %s |' % (p.name, p.scripted, p.speak / 60, p.wait / 60, p.act / 60, p.trans / 60, p.need, d, p.flag()))
        ts += p.scripted; tn += p.need
    sp = sum(p.speak for p in P) / 60; wt = sum(p.wait for p in P) / 60; ac = sum(p.act for p in P) / 60; tr = sum(p.trans for p in P) / 60
    rows.append('| **Whole lesson** | **%d** | **%.1f** | **%.1f** | **%.1f** | **%.1f** | **%.1f** | **%+.1f** | |' % (ts, sp, wt, ac, tr, tn, tn - ts))
    return '\n'.join(rows)


def main():
    C = load_content()
    only = None
    if '--lesson' in sys.argv: only = int(sys.argv[sys.argv.index('--lesson') + 1])
    res = {}
    for n in range(1, 11):
        if only and n != only: continue
        r = {}
        for name, sc in SCEN.items():
            P, info = model_lesson(n, C, sc)
            r[name] = (P, info)
        res[n] = r
    if '--stats' in sys.argv:
        for n in range(1, 11):
            print(n, stats(n, C))
        return
    if '--fixed' in sys.argv:
        for n in range(1, 11):
            if only and n != only: continue
            P0, _ = model_lesson(n, C, SCEN['central'])
            P, info = model_lesson(n, C, SCEN['central'], FX[n])
            lo = sum(p.need for p in model_lesson(n, C, SCEN['fast'], FX[n])[0]); hi = sum(p.need for p in model_lesson(n, C, SCEN['slow'], FX[n])[0])
            b, flex = budgets(P)
            print('\n### Lesson %d after fixes (central)\n' % n)
            print('| Part | Was scripted | Need before | Need after | New budget |'); print('|---|---:|---:|---:|---:|')
            for p0, p, bb in zip(P0, P, b):
                print('| %s | %d | %.1f | %.1f | %.1f |' % (p.name, p.scripted, p0.need, p.need, bb))
            print('| Flex buffer | 0 | | | %.1f |' % flex)
            print('| **Total** | 90 | **%.1f** | **%.1f** (fast %.1f / slow %.1f) | **%.1f** |' % (sum(p.need for p in P0), sum(p.need for p in P), lo, hi, sum(b) + flex))
            if n < 10:
                wsp = [p for p in P if p.name == 'Worksheet'][0]
                wb_bud = b[[p.name for p in P].index('Worksheet')]
                print('Worksheet finishers after fixes (block %.1f min):' % wb_bud, finishers(n, info, wsp, block=wb_bud))
        return
    if '--json' in sys.argv:
        out = {}
        for n, r in res.items():
            out[n] = {k: dict(total=round(sum(p.need for p in v[0]), 1), parts={p.name: round(p.need, 1) for p in v[0]}) for k, v in r.items()}
        print(json.dumps(out, indent=1)); return
    for n, r in res.items():
        P, info = r['central']
        print('\n### Lesson %d (central run)\n' % n)
        print(table(n, P))
        lo = sum(p.need for p in r['fast'][0]); hi = sum(p.need for p in r['slow'][0]); mid = sum(p.need for p in P)
        print('\nRange: fast %.1f / central %.1f / slow %.1f min.  Slides %d.' % (lo, mid, hi, info['slides']))
        if n < 10:
            wsp = [p for p in P if p.name == 'Worksheet'][0]
            print('Worksheet finishers:', finishers(n, info, wsp))
        for p in P:
            for t in p.notes: print('  note [%s]: %s' % (p.name, t))


if __name__ == '__main__':
    main()
