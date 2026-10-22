#!/usr/bin/env python3
"""P3 lesson-timing audit helper.  Run:  python3 docs/audit/timing_p3.py [--md]
READ-ONLY: reads p3/data.js, p3/gifted.json (via node) and split/p3l*/project/slides/*.html;
writes nothing except stdout.  It rebuilds the numbers quoted in docs/audit/timing_p3.md.

MODEL (identical constants should be used for every level so results compare)
  speech            130 words/min (tutor SAY lines, slide narration, closing words)
  read aloud        120 words/min (questions read to the group)
  group question    10 s wait + 20 s to take one or two answers = 30 s
  hold-up moment    30 s (boards / papers to camera)
  slide change      20 / 25 / 30 s  (low / central / high)
  breakout move     60 / 90 / 120 s per move (to OR from rooms); materials find 60 / 75 / 120 s
  worksheet start   2 min
  REC cue           10 s at the start of each of the 8 parts
  group             8 children (the guide's maximum)
  activity speed    low / central / high = x0.85 / x1.0 / x1.2 on MID-child minutes
The hand-judged inputs (minutes per workbook item, pair-task minutes, exit-ticket minutes)
are the tables ITEMS, EXPLORE_X and EXIT_WORK below; change them and re-run.
"""
import json, re, os, subprocess, sys, html

R = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
W_SAY, W_READ = 130.0, 120.0
GROUP = 8
PARAMS = {  # slide change s, breakout move s, materials s, activity factor, talk-move round trip s
    'low':     dict(slide=20, move=60,  mat=60,  act=0.85, tmove=40),
    'central': dict(slide=25, move=90,  mat=75,  act=1.00, tmove=60),
    'high':    dict(slide=30, move=120, mat=120, act=1.20, tmove=90),
}
SCRIPTED = [('Opening', 2), ('Sneak-peek + warm-up game + quick questions', 8), ('Explore', 15),
            ('Mini-lesson', 10), ('Brain break', 5), ('Worksheet', 30), ('Talk time', 10),
            ('Exit ticket + look-back + close', 10)]

# ---- fixed guide text (copied from p3/guide.js) ----------------------------------------------
SNEAK_SAY = ('Here are two sneak-peek puzzles. These are ideas we have not learnt yet, so guessing is welcome and so is '
             '"I do not know". Nobody is marked. Write your answer on your own paper. When I say "show me", hold it up to the camera for me.')
WORK_SAY = 'Talk to your partner while you work. I will come round and ask you questions.'
PAIRS_SAY = 'Pairs first. Read each question aloud and talk about it before you write. I am not looking for speed. I am looking for good thinking.'
START_SAY = 'Pairs first. Talk before you write.'
CHOICE_SAY = 'When you have finished Start here you can choose Think harder, Go further or the Investigation.'
BRK_TAIL = 'Water. Toilet break for anyone who needs it. Keep it to five minutes.'
EXIT_SAY = 'Take a slip of paper. Write your answer. No talking, no helping. Show it to me when you have finished.'
LB_SAY1 = ('Turn to the last page of today\'s lesson and find Look back. Tick or write one thing for each line: something you did well, '
           'the hardest part, and what helped you. There are no right answers, and you may pass on any line.')
LB_SAY2 = ('Would anyone like to share something they did well, or what helped? Thank you. When you got stuck and tried something else, '
           'that is exactly what mathematicians do.')
CERT_SAY = 'You are real inquirers now: you notice, test, and explain why. Here is your certificate.'

# ---- hand-judged inputs ----------------------------------------------------------------------
# ITEMS[n] = list of (label, MID-child minutes, if_time, answer boxes); first three = page 1 (pairs), rest = page 2 (alone)
ITEMS = {
 1: [('Q1 greatest/smallest/odd/closest', 2.5, 0, 5), ('Q2 list 2,0,5,5 (9 numbers)', 3.5, 0, 3), ('Q3 four patterns', 2.5, 0, 8),
     ('Q4 renaming', 2.5, 0, 3), ('Q5 clue number (a)', 3.0, 0, 2), ('Q6 digit sum 3 list', 4.0, 1, 4)],
 2: [('Q1 missing digits', 3.0, 0, 3), ('Q2 digit cards 1-6', 4.0, 0, 3), ('Q3 magic square', 3.0, 0, 2),
     ('Q4 pyramids', 3.0, 0, 2), ('Q5 9999 pairs', 2.5, 0, 3), ('Q6 letter puzzle', 4.5, 1, 2)],
 3: [('Q1 9s pattern', 2.5, 0, 4), ('Q2 7s last digits', 3.0, 0, 4), ('Q3 split 7x8, 9x6', 2.0, 0, 3),
     ('Q4 grid puzzle', 4.5, 1, 1), ('Q5 36 chairs all ways', 4.0, 0, 3), ('Q6 number riddle', 4.5, 1, 2)],
 4: [('Q1 bakery model', 2.5, 0, 2), ('Q2 three comparisons', 3.0, 0, 3), ('Q3 3 times as many', 3.0, 0, 4),
     ('Q4 sum+difference', 3.5, 0, 2), ('Q5 give to make equal', 3.5, 0, 2), ('Q6 same difference', 3.0, 0, 3)],
 5: [('Q1 47 / 6 + error', 2.5, 0, 4), ('Q2 four remainder stories', 3.0, 0, 4), ('Q3 12 bags of 8 (a)', 2.0, 0, 1),
     ('Q4 two-clue number (a)', 3.5, 0, 1), ('Q5 remainders of 8', 3.0, 0, 2), ('Q6 party tables', 5.0, 1, 3)],
 6: [('Q1 fraction wall fills', 3.5, 0, 12), ('Q2 compare 6 + order 4', 4.0, 0, 7), ('Q3 shaded shapes', 2.0, 0, 2),
     ('Q4 add/subtract six', 3.5, 0, 6), ('Q5 fence bar', 2.5, 0, 3), ('Q6 five pairs of one whole', 2.0, 0, 5)],
 7: [('Q1 area+perimeter of 4 figures', 4.0, 0, 10), ('Q2 18 m fence list', 4.0, 0, 9), ('Q3 square from rectangle', 2.0, 0, 1),
     ('Q4 missing sides, area, perimeter', 4.0, 0, 4), ('Q5 staircase', 3.5, 0, 4), ('Q6 add one square', 3.5, 1, 3)],
 8: [('Q1 fold checker + sort 6 angles', 3.5, 0, 3), ('Q2 right angles in 4 shapes', 3.0, 0, 3), ('Q3 count angles 6 lines + 8 lines', 4.5, 0, 7),
     ('Q4 parallel/perp 6 letters', 3.5, 0, 14), ('Q5 draw parallel/perp lines', 3.5, 0, 2), ('Q6 right angles in window', 3.0, 0, 1)],
 9: [('Q1 unit conversions a-f', 4.0, 0, 6), ('Q2 order 4 masses + error', 2.5, 0, 2), ('Q3 buy 3 things, $20 (a)', 2.0, 0, 1),
     ('Q4 24-hour clock', 3.5, 1, 7), ('Q5 time lines a-c', 4.5, 0, 3), ('Q6 bus timetable', 4.5, 1, 3)],
 10: [('Q1 bar graph (draw a bar)', 4.0, 0, 4), ('Q2 logic grid 4 x 4', 4.5, 0, 4), ('Q3 queues', 2.5, 0, 2),
      ('Q4 list 3-digit numbers', 3.0, 0, 3), ('Q5 stick table', 3.0, 0, 2), ('Q6 odd number riddle', 4.5, 1, 1)],
}
# pair-task minutes for the Explore block (hands-on, MID pair, includes setting up the cards/paper)
EXPLORE_X = {1: 6, 2: 8, 3: 9, 4: 7, 5: 7, 6: 10, 7: 7, 8: 7, 9: 9, 10: 15}  # L10 = two 7-minute stations + 1 switch
EXPLORE_X_FIX = {1: 6, 2: 7, 3: 6.5, 4: 7, 5: 7, 6: 7.5, 7: 7, 8: 7, 9: 7, 10: 9}  # after the explore fixes in the report
# FIX: lesson-specific extras (indices are 0-based positions in ITEMS: 0 = Q1 ... 5 = Q6)
FIX_EXTRA = {
    2: dict(item_scale={1: 2.5}, explore_x=6.5, mini_drop=['try2']),                                   # Q2(c) to take-home
    4: dict(demote=[5], item_scale={4: 3.0}, drop_mid=['teachsame'], talk_add=90, explore_x=6.5),     # Q6 + teachsame move to talk time
    6: dict(item_scale={0: 2.5}, demote=[5], drop_mid=['teachbetween', 'teachpairs'], explore_x=6.5), # Q1(c), Q6 to take-home
    7: dict(explore_x=6),
    8: dict(demote=[5], item_scale={3: 2.5, 2: 3.5}, explore_x=6),                                     # Q4 four letters, Q3(b) to take-home
    10: dict(drop_mid=['teachtable', 'teachbetween'], exit_work=2.0),                                  # review lesson: one combined recap slide
}
# FIX: teaching slides cut (they only serve an 'if time' item, or are a second try-it that the worksheet itself repeats)
DROP_SLIDES = {1: ['teachsum', 'tryclues'], 2: ['teachshape'], 3: [], 4: ['tryunits'], 5: ['teachtable'],
               6: ['tryadd'], 7: ['teachadd'], 8: ['try1'], 9: ['teach24'], 10: []}
MAT_EXTRA = {6: 45}  # L6: extra seconds to find/mark the 7 strips on top of the standard materials time
EXIT_WORK = {1: 3.0, 2: 3.0, 3: 3.0, 4: 3.5, 5: 3.0, 6: 3.0, 7: 3.0, 8: 3.0, 9: 3.5, 10: 3.5}
LOW_F, HIGH_F = 1.7, 0.6  # LOW child takes 1.7 x MID time (plus help), HIGH child 0.6 x

# ---- load content ----------------------------------------------------------------------------
def load():
    js = ("const L=require('./data.js');const GF=require('./gifted.json');const o={};"
          "L.content.forEach(c=>{const n=c.lesson.n;o[n]={lesson:{title:c.lesson.title,share:c.lesson.share,exit:c.lesson.exit},"
          "script:c.script,deck:c.deck,gf:{check:GF[n].check}}});console.log(JSON.stringify(o))")
    out = subprocess.check_output(['node', '-e', js], cwd=os.path.join(R, 'p3'))
    return {int(k): v for k, v in json.loads(out).items()}

def slides(n):
    d = json.load(open(f'{R}/split/p3l{n}/project/deck.json'))
    rows = []
    for sid in d['order']:
        h = open(f'{R}/split/p3l{n}/project/slides/{sid}.html').read()
        m = re.search(r'letter-spacing:2px[^>]*>(\d+)[–-](\d+) MIN<', h)
        a = re.search(r'<aside>(.*?)</aside>', h, re.S)
        notes = html.unescape(re.sub('<[^>]+>', ' ', a.group(1))) if a else ''
        body = re.sub(r'<aside>.*?</aside>', '', h, flags=re.S)
        body = re.sub(r'<svg.*?</svg>', ' ', body, flags=re.S)
        vis = re.sub(r'\s+', ' ', html.unescape(re.sub('<[^>]+>', ' ', body))).replace(
            'Math Inquirers P3 Holiday Program • Notice it. Test it. Explain why.', '').strip()
        rows.append(dict(id=sid.split('-', 1)[-1], a=int(m.group(1)) if m else None, b=int(m.group(2)) if m else None,
                         vis=len(vis.split()), notes=len(notes.split()), asks=len(re.findall(r'\bAsk\b', notes)),
                         yourturn='Your turn' in vis, q=notes.count('?'), steps=len(re.findall(r'Step \d', vis))))
    return rows

def nw(x):
    if isinstance(x, (list, tuple)):
        return sum(nw(i) for i in x)
    return len(re.findall(r'\S+', str(x)))

def say(words): return words / W_SAY * 60
def read(words): return words / W_READ * 60

# ---- one lesson ------------------------------------------------------------------------------
def teach_slide(s, P):
    """cost (speak, wait, act, trans, words) in seconds for one teaching / try-it slide."""
    sl = P['slide']; dur = (s['b'] - s['a']) * 60 if s['a'] is not None else 60
    if s['id'].startswith('try'):
        w = round(s['vis'] * 0.55)          # the problem text; the answers are hidden until the click
        return dict(speak=read(w), wait=30 + 15, act=max(60, 0.6 * dur), trans=sl, words=w)
    w = round(s['vis'] * 0.8)               # tutor explains / thinks aloud around the slide text
    asks = max(s['asks'], 1 if s['q'] >= 1 else 0)
    d = dict(speak=say(w), wait=asks * 30 + s['steps'] * 10, act=0, trans=sl, words=w)
    if s['yourturn']:
        d['act'] += 60; d['wait'] += 30
    return d

def lesson(n, C, P, fix=False):
    c = C[n]; S = slides(n); sc, dk, gf = c['script'], c['deck'], c['gf']
    sl, mv, mat, act, tmove = P['slide'], P['move'], P['mat'], P['act'], P['tmove']
    if fix: mv = mv / 2; tmove = tmove / 2        # FIX: pre-assigned rooms, auto-move and auto-close
    REC = 10
    X = FIX_EXTRA.get(n, {}) if fix else {}
    parts = {}
    def add(name, speak, wait, actv, trans, words, **extra):
        parts[name] = dict(speak=speak, wait=wait, act=actv, trans=trans, rec=REC, words=words, **extra)
    # 1 Opening: hook, "Today we will", greet each child by name (3 s each); title slide is already up
    add('Opening', say(nw(sc['hook'])) + read(nw(dk['today'])), GROUP * 3, 0, 0, nw(sc['hook']) + nw(dk['today']))
    # 2 Sneak-peek + game + quick questions
    q1, q2 = nw(gf['check'][0]['q']), nw(gf['check'][1]['q'])
    wq = dk['warmQs'][:3] if fix else dk['warmQs']          # FIX: three quick questions, the rest go to take-home
    nq = len(wq); qw = sum(nw(x[0]) for x in wq)
    asks_game = sum(1 for l in sc['warmIntro'][1:] if '?' in l)
    add('Sneak-peek + warm-up game + quick questions',
        say(nw(SNEAK_SAY)) + read(q1 + q2) + say(nw(sc['warmIntro'])) + read(qw),
        (1 if fix else 2) * 30 + asks_game * 30 + nq * 30 + 5,   # hold-ups (FIX: one for both puzzles), game questions, 30 s per quick question
        2 * 60 + (120 if fix else 180),              # 1 min per puzzle, game play (FIX: 2 min)
        3 * sl, nw(SNEAK_SAY) + q1 + q2 + nw(sc['warmIntro']) + qw)
    # 3 Explore
    ea = sum(nw(x[0]) for x in dk['expAsk'])
    add('Explore', say(nw(sc['predict'])) + read(nw(dk['expSetup'])) + say(nw(WORK_SAY)) + read(ea),
        30 + 30 + len(dk['expAsk']) * 30,            # prediction hold-up, tutor check-in, three group questions
        (X.get('explore_x', EXPLORE_X_FIX[n]) if fix else EXPLORE_X[n]) * 60 * act,
        mat + (0 if fix else MAT_EXTRA.get(n, 0)) + 2 * mv + 2 * sl, nw(sc['predict']) + nw(dk['expSetup']) + ea)
    # 4 Mini-lesson = slides starting at minutes 25..34
    mini = [s for s in S if s['a'] is not None and 25 <= s['a'] < 35]
    mini = [x for x in mini if x['id'] not in X.get('mini_drop', [])]
    if fix and len(mini) >= 7:                      # FIX: merge the shortest 'we' into the next try-it slide
        drop = min((x for x in mini if x['id'].startswith('we')), key=lambda x: x['vis'], default=None)
        mini = [x for x in mini if x is not drop]
    t = dict(speak=0, wait=0, act=0, trans=0, words=0)
    for s in mini:
        if s['id'] == 'key':
            w = nw(dk['keyHead']) + nw(dk['keyBig']) + 8
            d = dict(speak=say(w) + 10, wait=0, act=0, trans=sl, words=w)
        else:
            d = teach_slide(s, P)
        for k in t: t[k] += d[k]
    add('Mini-lesson', t['speak'], t['wait'], t['act'], t['trans'], t['words'], slides=len(mini))
    # 5 Brain break: 2 min movement + 2.5 min water / toilet / settle back (the guide caps it at five)
    add('Brain break', say(nw(dk['brk'])) + say(nw(BRK_TAIL)), 0, 120 + 150, sl, nw(dk['brk']) + nw(BRK_TAIL))
    # 6 Worksheet (40-70)
    byid = {s['id']: s for s in S}
    ws1, ws2 = byid['ws1'], byid['ws2']
    pre = [s for s in S if s['a'] is not None and 40 <= s['a'] < ws1['a'] and not s['id'].startswith(('ws', 'stretch'))]
    mid = [s for s in S if s['a'] is not None and 54 <= s['a'] < ws2['a'] and not s['id'].startswith(('ws', 'stretch'))]
    sp = wt = ac = tr = words = 0; detail = {}
    def acc(label, d):
        nonlocal sp, wt, ac, tr, words
        sp += d['speak']; wt += d['wait']; ac += d['act']; tr += d['trans']; words += d.get('words', 0)
        detail[label] = (d['speak'] + d['wait'] + d['act'] + d['trans']) / 60
    def sumslides(lst):
        z = dict(speak=0, wait=0, act=0, trans=0, words=0)
        for s in lst:
            d = teach_slide(s, P)
            for k in z: z[k] += d[k]
        return z
    it = [list(i) for i in ITEMS[n]]
    for i, v in X.get('item_scale', {}).items(): it[i][1] = v
    for i in X.get('demote', []): it[i][2] = 1
    p1, p2 = it[:3], it[3:]
    if fix:
        pre = [x for x in pre if x['id'] not in DROP_SLIDES[n]]; mid = [x for x in mid if x['id'] not in DROP_SLIDES[n] + X.get('drop_mid', [])]
    p1_min = sum(i[1] for i in p1) * act
    p2_min = sum(i[1] for i in p2 if not i[2]) * act
    sw = nw(START_SAY) + nw(PAIRS_SAY)
    acc('teaching slides before page 1', sumslides(pre))
    acc('hand out + get started (2 min)', dict(speak=say(sw), wait=0, act=120, trans=0, words=sw))
    acc('breakout in + out', dict(speak=0, wait=0, act=0, trans=2 * mv))
    acc('page 1 pairs work (Q1-Q3)', dict(speak=0, wait=0, act=p1_min * 60, trans=sl))
    CHK = 60 if fix else 3 * 40                   # FIX: self-check slide, tutor probes one or two answers only
    a1 = round(byid['ws1ans']['vis'] * 0.5)
    acc('check page 1 (3 questions)', dict(speak=say(a1), wait=CHK, act=0, trans=sl, words=a1))
    acc('teaching slides before page 2', sumslides(mid))
    acc('page 2 alone (compulsory Q4-Q6)', dict(speak=0, wait=0, act=p2_min * 60 + 30, trans=sl))
    a2 = round(byid['ws2ans']['vis'] * 0.5)
    acc('check page 2 (3 questions)', dict(speak=say(a2), wait=CHK, act=0, trans=sl, words=a2))
    cw = nw(CHOICE_SAY)
    acc('choose Think harder / Go further (3 min)', dict(speak=say(cw), wait=0, act=180 - 2 * sl - say(cw), trans=2 * sl, words=cw))
    add('Worksheet', sp, wt, ac, tr, words, slides=len(pre) + len(mid) + 6, p1_min=p1_min, p2_min=p2_min, detail=detail)
    # 7 Talk time
    sh = nw(c['lesson']['share']); tw = nw(sc['talk']); ans = nw(sc['talkAns'])
    add('Talk time', say(tw) + read(sh) + say(ans) + read(q2),
        3 * 30 + 30 + 30,                            # three volunteer questions, puzzle-2 revisit, follow-up
        120 + X.get('talk_add', 0),                  # partner talk, 2 min (+ FIX: slides moved here) (notes: "Pairs talk for 2 minutes, then share")
        sl + tmove, tw + sh + ans + q2)
    # 8 Exit ticket + look-back + close
    ex = nw(c['lesson']['exit']['q'])
    ac = X.get('exit_work', EXIT_WORK[n]) * 60 * act + 120               # exit work + a full 2 minutes of look-back
    if n == 10:
        ac += GROUP * (20 if fix else 30) + (30 if fix else 60)   # 8 certificates with one specific praise each (FIX: 20 s), volunteers
    add('Exit ticket + look-back + close',
        say(nw(EXIT_SAY)) + read(ex) + say(nw(LB_SAY1) + nw(LB_SAY2)) + say(nw(sc['close'])),
        30 + GROUP * 6 + 30 + 20,                    # tickets to camera, tutor scans 8 papers, volunteer share, stuck check
        ac, 3 * sl + mat * 0.8,                      # exit, look-back, end slide; find a slip of paper
        nw(EXIT_SAY) + ex + nw(LB_SAY1) + nw(LB_SAY2) + nw(sc['close']))
    for k in parts:
        p = parts[k]; p['total'] = (p['speak'] + p['wait'] + p['act'] + p['trans'] + p['rec']) / 60
    return parts, S

def items_done(window_min, items, factor):
    t, done = 0.0, 0.0
    for label, m, iff, nb in items:
        need = m * factor
        if t + need <= window_min + 1e-9:
            t += need; done += 1
        else:
            done += max(0.0, (window_min - t) / need); break
    return done

def flag(diff):
    if diff >= 2.0: return 'OVER'
    if diff >= 0.75: return 'TIGHT'
    if diff <= -3.0: return 'LOOSE'
    return 'OK'

def main():
    C = load(); out = {}
    for n in range(1, 11):
        res = {}
        for pn, P in PARAMS.items():
            res[pn], S = lesson(n, C, P)
        out[n] = (res, S)
    print('lesson | est total low/central/high | slides | SAY+read words')
    for n in range(1, 11):
        res, S = out[n]
        tot = {pn: sum(p['total'] for p in res[pn].values()) for pn in res}
        words = sum(p['words'] for p in res['central'].values())
        print(f"L{n:2d} {C[n]['lesson']['title'][:28]:28s} {tot['low']:6.1f} {tot['central']:6.1f} {tot['high']:6.1f}   slides {len(S)}  words {words}")
    if '--md' in sys.argv:
        for n in range(1, 11):
            res, S = out[n]; r = res['central']
            print(f"\n### Lesson {n}: {C[n]['lesson']['title']}\n")
            print('| Part | Scripted | Speak | Wait | Activity | Trans | REC | Need (central) | Diff | Flag | Range low-high |')
            print('|---|---|---|---|---|---|---|---|---|---|---|')
            for (k, sm) in SCRIPTED:
                p = r[k]; d = p['total'] - sm
                print(f"| {k} | {sm} | {p['speak']/60:.1f} | {p['wait']/60:.1f} | {p['act']/60:.1f} | {p['trans']/60:.1f} | {p['rec']/60:.2f} | {p['total']:.1f} | {d:+.1f} | {flag(d)} | {res['low'][k]['total']:.1f}-{res['high'][k]['total']:.1f} |")
            tot = {pn: sum(p['total'] for p in res[pn].values()) for pn in res}
            print(f"| TOTAL | 90 | | | | | | {tot['central']:.1f} | {tot['central']-90:+.1f} | | {tot['low']:.1f}-{tot['high']:.1f} |")
            print('\nWorksheet block detail (central, minutes): ' + '; '.join(f"{k} {v:.1f}" for k, v in r['Worksheet']['detail'].items()))
            byid = {s['id']: s for s in S}
            P = PARAMS['central']
            w1 = (byid['ws1']['b'] - byid['ws1']['a']) - 2 - 2 * P['move'] / 60
            w2 = (byid['ws2']['b'] - byid['ws2']['a']) - 0.5
            it = ITEMS[n]
            row = []
            for nm, f in (('LOW', LOW_F), ('MID', 1.0), ('HIGH', HIGH_F)):
                row.append(f"{nm} {items_done(w1, it[:3], f):.1f}/3 + {items_done(w2, it[3:], f):.1f}/3")
            print(f"Items finished in the scripted windows (page 1 work time {w1:.1f} min; page 2 work time {w2:.1f} min): " + '; '.join(row))
            print(f"MID minutes needed: page 1 {sum(i[1] for i in it[:3]):.1f}, page 2 compulsory {sum(i[1] for i in it[3:] if not i[2]):.1f}, page 2 incl. if-time {sum(i[1] for i in it[3:]):.1f}")
            print(f"Slides {len(S)}; spoken+read-aloud words (central model) {sum(p['words'] for p in r.values())}")

def fixed_table():
    C = load()
    print('FIXED scenario (central): part needs per lesson')
    names = [k for k, _ in SCRIPTED]
    print('lesson | ' + ' | '.join(n[:10] for n in names) + ' | total (low-high)')
    for n in range(1, 11):
        r = {pn: lesson(n, C, PARAMS[pn], fix=True)[0] for pn in PARAMS}
        c = r['central']
        tot = {pn: sum(p['total'] for p in r[pn].values()) for pn in r}
        print(f"L{n:2d} | " + ' | '.join(f"{c[k]['total']:.1f}" for k in names) + f" | {tot['central']:.1f} ({tot['low']:.1f}-{tot['high']:.1f})")

if __name__ == '__main__':
    main()
    if '--fix' in sys.argv: fixed_table()
