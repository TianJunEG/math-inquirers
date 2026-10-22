#!/usr/bin/env python3
"""Lesson timing audit helper, Math Inquirers Level N=5 (P5).  ANALYSIS ONLY: reads the repo, writes nothing.

Usage:  python3 docs/audit/timing_p5.py            (prints the per-lesson tables as markdown)
        python3 docs/audit/timing_p5.py --plan     (recommended new budgets per lesson, summing to 90)
        python3 docs/audit/timing_p5.py --plan-md  (the same as one markdown table)
        python3 docs/audit/timing_p5.py --json     (prints raw numbers)

What it does: loads p5/data.js (script, deck, lesson, qbank) through node, reads the slide decks in
split/p5l*/project, counts the words that are SAID or READ ALOUD in each part, adds waiting, activity and
transition time with ONE set of constants for all lessons (below), and compares with the minutes in the
tutor guide generator p5/guide.js (the seg('a-b min') calls: 0-3 sneak, 3-9 warm-up, 9-21 explore,
21-33 mini-lesson, 33-37 brain break, 37-76 workbook (guide.js labels it 37-72, see audit), 76-82 talk,
82-90 exit/reflection/closing).  Judgement inputs (how long a child needs for a puzzle, a try-it slide,
a worksheet item) are the dictionaries LES / below; they were entered by reading the real text of each
slide and worksheet question.  These are estimates, not stopwatch times.
"""
import json, re, html, subprocess, sys, os

ROOT = '/home/user/math-inquirers'

# ---------------- constants, identical for every lesson / level ----------------
SAY_WPM, READ_WPM = 140, 130     # tutor speech incl. natural pauses; read-aloud of questions
REC = 10                         # REC cue line, seconds, at the start of each guide part (9 parts incl. opening)
WAIT_Q, TAKE = 10, 20            # wait after a group question + taking 1-2 answers (seconds)
HOLD = 30                        # 'hold up boards / paper to camera' moment (seconds)
SLIDE = 25                       # one slide change online (20-30 s)
BO_OUT, BO_BACK = 90, 60         # move to / back from breakout rooms (60-120 s range)
MAIN_OUT, MAIN_BACK = 30, 30     # same cost when pairs stay in the main room (mute/unmute, switch to whiteboard)
START_WB = 120                   # getting started on a worksheet
GREET = 30                       # greet 6-8 children by name
REC_NOTICE = 15                  # tell the group the lesson is recorded (reccues.js RULES.privacy)
FACT = 0.8                       # share of a worked-example slide's printed words that is actually spoken
LOW_X, HIGH_X = 1.6, 0.65        # LOW / HIGH child time multipliers vs MIDDLE child
SCRIPT = dict(open=0, sneak=3, warm=6, explore=12, mini=12, brk=4, wb=39, talk=6, exit=8)
WB_SCRIPT = dict(p1=12, chk1=4, teach=5, p2=14, chk2=4)   # 37-49, 49-53, 53-58, 58-72, 72-76

# ---------------- judgement inputs per lesson (entered from the real text) ----------------
# sneak: seconds a child needs for puzzle 1 (access) and puzzle 2 (thinking)
# game: seconds of the warm-up game (children playing, incl. its reveals); expl: seconds pairs need in the explore
# mat: seconds to hand out / find materials; bo: pairs use breakout rooms for (explore, page 1)
# try_m / try_t: solve seconds for each 'Your turn' slide in the mini-lesson / in the page-2 teaching
# p1 / p2: per question, list of minutes for a MIDDLE child per answer part; start2: (question, n_parts or None=all) named on the page-2 plan
# exit: seconds a child needs for the exit ticket;  brk: seconds of the movement part of the brain break
LES = {
 1: dict(sneak=(75, 90), game=190, expl=420, mat=60, bo=(1, 1), open_extra=0,
         try_m=dict(try1=75, try2=150), try_t=dict(trybrackets=160), brk=120, exit=150, nasks=dict(),
         p1=[(1, [1, 1, 1]), (2, [1, 2, 4.5]), (3, [7])],
         p2=[(4, [1.25, 1.5, 1, 1.25]), (5, [1.5, 1.5, 2.5, 5]), (6, [2, 5])],
         start2=[(4, None), (5, 2)]),
 2: dict(sneak=(60, 90), game=150, expl=480, mat=90, bo=(1, 1), open_extra=0,
         try_m=dict(try1=75, try2=160), try_t={}, brk=120, exit=150,
         p1=[(1, [1, 1, 2.5]), (2, [1.5, 1.5, 3, 4.5]), (3, [3, 1, 1.5])],
         p2=[(4, [1.5, 4, 3]), (5, [4, 1]), (6, [3, 3.5, 5])],
         start2=[(5, None), (4, 2)]),
 3: dict(sneak=(45, 75), game=180, expl=480, mat=60, bo=(0, 0), open_extra=0,
         try_m=dict(try1=200, try2=175), try_t=dict(trydiff=150), brk=120, exit=240,
         p1=[(1, [1.5, 3.5, 1.5, 1.5]), (2, [0.5, 4])],
         p2=[(3, [2, 4]), (4, [1.5, 1.5, 3.5]), (5, [0.5, 4, 2, 1])],
         start2=[(3, 1), (4, 2), (5, 2)]),
 4: dict(sneak=(90, 75), game=120, expl=480, mat=120, bo=(0, 0), open_extra=0,
         try_m=dict(try1=85, try2=115), try_t={}, brk=120, exit=90,
         p1=[(1, [1, 1.5, 1.5, 1]), (2, [1, 1, 2])],
         p2=[(3, [0.5, 1, 1, 0.5]), (4, [0.5, 1.5, 1.5, 1.5, 1]), (5, [1, 2, 1.5])],
         start2=[(5, None), (3, None)]),
 5: dict(sneak=(60, 75), game=180, expl=480, mat=90, bo=(0, 0), open_extra=90,
         try_m=dict(try1=160, try2=110), try_t={}, brk=120, exit=180, mini_extra=90,
         p1=[(1, [1, 3]), (2, [4.5, 1.5]), (3, [1.5, 2, 1.5, 3])],
         p2=[(4, [1, 2.5, 1, 2]), (5, [6]), (6, [2, 3, 4.5])],
         start2=[(4, 3), (5, None)]),
 6: dict(sneak=(60, 60), game=120, expl=540, mat=60, bo=(1, 0), open_extra=0,
         try_m=dict(try1=110, try2=100), try_t={}, brk=150, exit=180,
         p1=[(1, [3, 2]), (2, [1, 3, 0.5, 4.5]), (3, [1, 1.5, 2, 2.5])],
         p2=[(4, [2, 3.5, 4]), (5, [1.5, 3, 2.5]), (6, [2, 1.5, 2])],
         start2=[(4, 1), (6, 1), (5, None)]),
 7: dict(sneak=(60, 75), game=120, expl=360, mat=60, bo=(0, 0), open_extra=0,
         try_m=dict(try1=105, try2=135), try_t={}, brk=120, exit=210,
         p1=[(1, [3, 1, 1.5]), (2, [1, 1.5, 2, 1, 3.5]), (3, [1, 1, 2.5])],
         p2=[(4, [1, 1, 1.5, 1, 3]), (5, [6])],
         start2=[(4, 4), (5, None)]),
 8: dict(sneak=(45, 60), game=120, expl=360, mat=90, bo=(0, 0), open_extra=0,
         try_m=dict(try1=75, try2=140), try_t={}, brk=120, exit=180,
         p1=[(1, [0.75, 0.75, 0.75, 1.5]), (2, [2.5, 3, 2.5])],
         p2=[(3, [1.5, 2, 1, 2.5]), (4, [1, 2, 1.5, 3]), (5, [3, 2.5])],
         start2=[(3, 2), (4, 2)]),
 9: dict(sneak=(60, 90), game=180, expl=540, mat=90, bo=(1, 1), open_extra=0,
         try_m=dict(try1=115, try2=130, try3=105), try_t={}, brk=120, exit=210,
         p1=[(1, [3, 1.5, 2.5, 2]), (2, [2, 2.5, 2.5])],
         p2=[(3, [4.5]), (4, [3, 4]), (5, [4, 3.5])],
         start2=[(3, None), (4, 2)]),
 10: dict(sneak=(75, 75), game=200, expl=540, mat=60, bo=(1, 0), open_extra=0,
         try_m=dict(try1=150, try2=120), try_t={}, brk=150, exit=180, cert=True,
         p1=[(1, [5]), (2, [4.5]), (3, [4.5])],
         p2=[(4, [1.5, 2.5, 2.5]), (5, [4.5]), (6, [4, 1])],
         start2=[(4, None), (5, None), (6, 1)]),
}

# ---------------- loading ----------------
def load_data():
    js = ("const L=require('%s/p5/data.js');const o={};L.content.forEach(c=>{o[c.lesson.n]={lesson:c.lesson,script:c.script,deck:c.deck,qbank:c.qbank}});"
          "process.stdout.write(JSON.stringify(o))") % ROOT
    return json.loads(subprocess.check_output(['node', '-e', js]))

def clean(s):
    s = re.sub(r'<style.*?</style>|<script.*?</script>|<svg.*?</svg>', '', s, flags=re.S)
    s = re.sub(r'<br\s*/?>|</p>|</div>|</li>|</h\d>|</tr>', '\n', s)
    s = re.sub(r'<[^>]+>', ' ', s); s = html.unescape(s)
    return re.sub(r'[ \t]+', ' ', re.sub(r'\n\s*\n+', '\n', s)).strip()

FOOT = 'Math Inquirers P5 Holiday Program • Notice it. Test it. Explain why.'
def load_slides(n):
    d = '%s/split/p5l%d/project/' % (ROOT, n)
    order = json.load(open(d + 'deck.json'))['order']; out = []
    for o in order:
        h = open(d + 'slides/' + o + '.html').read()
        m = re.search(r'<aside>(.*?)</aside>', h, re.S)
        notes = clean(m.group(1)) if m else ''
        txt = clean(re.sub(r'<aside>.*?</aside>', '', h, flags=re.S)).replace(FOOT, '')
        txt = re.sub(r'^\s*\d+–\d+ MIN.*$', '', txt, flags=re.M)
        out.append(dict(id=o.replace('p5l%d-' % n, ''), text=txt.strip(), notes=notes, opt='OPTION' in clean(h)))
    return out

W = lambda s: len(re.findall(r"\S+", s if isinstance(s, str) else ' '.join(s)))
say_s = lambda w: w / SAY_WPM * 60
read_s = lambda w: w / READ_WPM * 60

def part(**k):
    base = dict(speak=0, wait=0, act=0, trans=0); base.update(k); return base
def tot(p): return p['speak'] + p['wait'] + p['act'] + p['trans']

def qa_words(slides_by_id, ids):
    return sum(W(slides_by_id[i]['text']) for i in ids if i in slides_by_id)

# ---------------- model of one lesson ----------------
def model(n, D, S, fx=None):
    fx = fx or {}
    L = dict(LES[n]);
    for k_ in ('p1', 'p2', 'start2'):
        if k_ in fx: L[k_] = fx[k_]
    d = D[str(n)] if str(n) in D else D[n]
    sc, dk = d['script'], d['deck']
    ids = [s['id'] for s in S]; by = {s['id']: s for s in S}
    # slide groups by position in the deck
    i_exp2 = ids.index('explore2'); i_key = ids.index('key'); i_brk = ids.index('break')
    i_ws1 = ids.index('ws1'); i_ws1a = ids.index('ws1ans'); i_ws2 = ids.index('ws2'); i_ws2a = ids.index('ws2ans')
    drop = set(fx.get('drop', []))
    mini_ids = [i for i in ids[i_exp2 + 1:i_key + 1] if i not in drop]
    teach_ids = [i for i in ids[i_ws1a + 1:i_ws2] if not by[i]['opt'] and i not in drop]
    res = {}
    bo_e, bo_p = L['bo']
    # --- opening (before the clock) ---
    today = by['title']['text'].split('TODAY WE WILL')[-1]
    res['open'] = part(speak=REC + say_s(W(sc['hook']) + W(today)) + REC_NOTICE, wait=(15 if fx else GREET) + L['open_extra'], trans=SLIDE)
    # --- sneak-peek ---
    qs = dk['check']
    pw = sum(W(q[0]) for q in qs); aw = sum(min(W(q[1]), 20) + 12 for q in qs)
    if fx:
        aw = sum(min(W(q[1]), 12) for q in qs)     # say the answer and one short reason only
        res['sneak'] = part(speak=REC + say_s(12 + 30 + aw) + read_s(pw), wait=HOLD,   # one hold-up for both puzzles, no volunteer round
                            act=min(L['sneak'][0], 60) + min(L['sneak'][1], 75), trans=SLIDE)
    else:
        res['sneak'] = part(speak=REC + say_s(21 + 30 + aw) + read_s(pw), wait=2 * HOLD + WAIT_Q + TAKE,
                            act=sum(L['sneak']), trans=SLIDE)
    # --- warm-up ---
    wq = [q[0] for q in dk['warmQs']]
    if fx: wq = wq[:4]
    res['warm'] = part(speak=REC + say_s(W(sc['warmIntro'])) + read_s(sum(W(q) for q in wq)),
                       wait=len(wq) * (WAIT_Q + TAKE), act=(min(L['game'], fx.get('game_cap', 150)) if fx else L['game']), trans=2 * SLIDE)
    # --- explore ---
    think30 = 30 if 'Think for 30 seconds' in ' '.join(sc.get('predict', [])) else 0   # protected think time before touching objects
    think30_talk = 30 if any('Protected think time' in x for x in sc.get('talkRules', [])) else 0
    ea = dk['expAsk']
    out_, back_ = (BO_OUT, BO_BACK) if bo_e else (MAIN_OUT, MAIN_BACK)
    if fx: ea = ea[:2]; L['mat'] = min(L['mat'], 30); L['expl'] = min(L['expl'], fx.get('expl_cap', 390))
    res['explore'] = part(
        speak=REC + say_s(W(sc['predict']) + 15 + 10 + 0.5 * sum(W(a[1]) for a in ea)) + read_s(W(dk['expSetup']) + sum(W(a[0]) for a in ea)),
        wait=20 + 30 + len(ea) * (WAIT_Q + TAKE), act=L['expl'] + think30, trans=2 * SLIDE + L['mat'] + out_ + back_ + 20)
    # --- mini-lesson ---
    sp = wt = ac = 0
    for i in mini_ids:
        s = by[i]
        if i.startswith('try'):
            f = fx.get('try_f', 1.0)
            sp += read_s(W(s['text']) * 0.6 * f); wt += HOLD + 20; ac += L['try_m'].get(i, 90) * f
        elif i == 'key':
            sp += say_s(W(s['text'])) + 10
        else:
            sp += say_s(W(s['text']) * FACT); wt += WAIT_Q + TAKE
    sp = max(sp, say_s(W(sc['think'])))
    res['mini'] = part(speak=REC + sp, wait=wt, act=ac + (L.get('mini_extra', 0) if 'teachlist' not in drop else 0), trans=len(mini_ids) * SLIDE)
    # --- brain break ---
    res['brk'] = part(speak=REC + read_s(W(dk['brk'])) + 20, wait=60 + 20, act=(90 if fx else L['brk']), trans=SLIDE)
    # --- workbook ---
    wb = {}
    def mid_total(blocks): return sum(sum(x) for _, x in blocks)
    p1m, p2m = mid_total(L['p1']), mid_total(L['p2'])
    s2 = 0
    for q, k in L['start2']:
        parts = dict(L['p2'])[q]; s2 += sum(parts if k is None else parts[:k])
    out1, back1 = (BO_OUT, BO_BACK) if bo_p else (MAIN_OUT, MAIN_BACK)
    wb['p1'] = part(speak=REC + say_s(38 + 15 + 30), act=p1m * 60, trans=START_WB + out1 + SLIDE)
    nq1 = len(L['p1']); nq2 = len(L['p2'])
    ans1 = by['ws1ans']['text']
    heavy = lambda blocks: sum(1 for _, x in blocks if sum(x) >= 6)
    wb['chk1'] = part(speak=read_s(W(ans1)), wait=nq1 * (45 if fx else 60) + (0 if fx else 30) * heavy(L['p1']), trans=SLIDE + back1 + 20)
    tsp = twt = tac = ttr = 0
    for i in teach_ids:
        s = by[i]
        if i.startswith('try'):
            f = fx.get('try_f', 1.0); tsp += read_s(W(s['text']) * 0.6 * f); twt += HOLD + 20; tac += L['try_t'].get(i, 90) * f
        else:
            tsp += say_s(W(s['text']) * FACT); twt += WAIT_Q + TAKE
        ttr += SLIDE
    wb['teach'] = part(speak=tsp, wait=twt, act=tac, trans=ttr)
    wb['p2'] = part(speak=say_s(25), act=s2 * 60, trans=SLIDE + 30)
    ans2 = by['ws2ans']['text']
    wb['chk2'] = part(speak=read_s(W(ans2)), wait=nq2 * (45 if fx else 60) + (0 if fx else 30) * heavy(L['p2']), trans=SLIDE + 20)
    res['wb'] = {k: v for k, v in wb.items()}
    res['wbmeta'] = dict(p2_all=p2m, p1_mid=p1m, p2_mid=p2m, start2_mid=s2, nslides_teach=len(teach_ids),
                         p1_items=sum(len(x) for _, x in L['p1']), p2_items=sum(len(x) for _, x in L['p2']))
    # --- talk ---
    tq = W(by['talk']['text'].split('Sentence starters')[0])
    # pairs talk 120 s + Investigation first step 120 s are activity; volunteers share 120 s is waiting/answers
    if fx:   # Investigation first step moves to take-home / next lesson opener; volunteers 90 s
        res['talk'] = part(speak=REC + say_s(W(sc['talk']) + 20) + read_s(tq) + 10, wait=90, act=120, trans=SLIDE + 30)
    else:   # + protected 30 s silent think before the pairs talk (and before the Investigation first step)
        res['talk'] = part(speak=REC + say_s(W(sc['talk']) + 20 + 15) + read_s(tq) + 10, wait=120, act=240 + think30_talk,
                           trans=SLIDE + 30 + 30)
    # --- exit, reflection, closing ---
    ex = S[ids.index('exit')]['text']
    exq = ex.split('Write your')[0].split('Draw a model')[0]
    e = part(speak=REC + say_s(W(sc['close']) + 20) + read_s(W(exq)), wait=30 + 8 * 5, act=L['exit'], trans=SLIDE)
    r = part(speak=say_s(30 + 20), act=(75 if fx else 90), trans=SLIDE + 20)
    if L.get('cert'):
        c = part(speak=say_s(45), act=(8 * 12 if fx else 8 * 20 + 8 * 8), trans=SLIDE)
    else:
        c = part(speak=say_s(35), act=(15 if fx else 8 * 8), trans=0)
    res['exit'] = {k: e[k] + r[k] + c[k] for k in e}
    res['exit_sub'] = dict(exit=e, refl=r, close=c)
    res['counts'] = dict(slides=len(S), say_words=sum(W(sc[k]) for k in ('hook', 'warmIntro', 'predict', 'think', 'talk', 'close')),
                         whole_group_slides=len([i for i in ids if not by[i]['opt'] and i not in ('stretch', 'challenge', 'chdiag', 'chwalk')]),
                         opt_slides=len([i for i in ids if i in ('stretch', 'challenge', 'chdiag', 'chwalk') or by[i]['opt']]))
    return res

def wbsum(res):
    ks = ('speak', 'wait', 'act', 'trans')
    return {k: sum(v[k] for v in res['wb'].values()) for k in ks}

def flag(diff):
    if diff >= 2.0: return 'OVER'
    if diff >= 0.75: return 'TIGHT'
    if diff <= -3.0: return 'LOOSE'
    return 'OK'

def child_items(blocks, avail_min, mult):
    """items (answer parts) and whole questions a child finishes in avail_min, working in order."""
    t = 0; items = 0; qs = 0
    for q, parts in blocks:
        done = True
        for m in parts:
            if t + m * mult <= avail_min + 1e-9: t += m * mult; items += 1
            else: done = False; break
        if done: qs += 1
        else: break
    return items, qs

def report(n, D, out):
    S = load_slides(n); R = model(n, D, S); L = LES[n]
    bo_p = L['bo'][1]
    wb = R['wb']
    # budgets from guide.js / data.js timeline
    rows = []   # name, scripted, speak, wait, act, trans, need_content, need_box, flag(content)
    def add(name, sc, p, box=None, flagit=True):
        t = tot(p) / 60
        rows.append(dict(name=name, sc=sc, sp=p['speak'] / 60, wt=p['wait'] / 60, ac=p['act'] / 60, tr=p['trans'] / 60, need=t,
                         box=(sc if box == 'sc' else t), diff=t - sc, flag=(flag(t - sc) if flagit else 'PRE-CLOCK')))
    add('Opening (before clock)', 0, R['open'], flagit=False)
    add('Sneak-peek 0-3', 3, R['sneak']); add('Warm-up 3-9', 6, R['warm']); add('Explore 9-21', 12, R['explore'])
    add('Mini-lesson 21-33', 12, R['mini']); add('Brain break 33-37', 4, R['brk'])
    add('WB page 1 pairs 37-49', 12, wb['p1'], box='sc'); add('WB check p1 49-53', 4, wb['chk1'])
    add('WB teaching 53-58', 5, wb['teach']); add('WB page 2 alone 58-72', 14, wb['p2'], box='sc')
    add('WB check p2 72-76', 4, wb['chk2']); add('Talk time 76-82', 6, R['talk']); add('Exit/reflect/close 82-90', 8, R['exit'])
    # page 1 needs the START-HERE page complete (all of it); page 2 needs only the named start set
    t_box = sum(r['box'] for r in rows)
    t_full = sum((max(r['need'], r['sc']) if r['name'].startswith('WB page') else r['box']) for r in rows)
    # children: working time inside the blocks
    avail1 = WB_SCRIPT['p1'] - (REC + say_s(83) + START_WB + (BO_OUT if bo_p else MAIN_OUT) + SLIDE) / 60
    avail2 = WB_SCRIPT['p2'] - (say_s(25) + SLIDE + 30) / 60
    seq1 = [(q, parts) for q, parts in L['p1']]
    order2 = []; seen = set()
    for q, k in L['start2']:
        parts = dict(L['p2'])[q]; sel = parts if k is None else parts[:k]
        order2.append((q, sel)); seen.add(q)
    rest2 = []
    for q, parts in L['p2']:
        done = next((len(sel) for qq, sel in order2 if qq == q), 0)
        if done < len(parts): rest2.append((q, parts[done:]))
    kids = {}
    for nm, mult in (('LOW', LOW_X), ('MID', 1.0), ('HIGH', HIGH_X)):
        i1, q1 = child_items(seq1, avail1, mult)
        flat2 = [m for _, ps in order2 + rest2 for m in ps]
        t = 0; i2 = 0
        for m in flat2:
            if t + m * mult <= avail2 + 1e-9: t += m * mult; i2 += 1
            else: break
        kids[nm] = (i1, i2)
    meta = R['wbmeta']
    grp = [R[k] for k in ('open', 'sneak', 'warm', 'explore', 'mini', 'brk', 'talk', 'exit')] + [wb['chk1'], wb['teach'], wb['chk2']]
    fixed = [tot(p) for p in grp]
    lo = sum(tot(p) - 0.1 * p['speak'] - 0.15 * (p['wait'] + p['act'] + p['trans']) for p in grp) / 60 + 26
    hi = sum(tot(p) + 0.1 * p['speak'] + 0.15 * (p['wait'] + p['act'] + p['trans']) for p in grp) / 60 + 26
    out[n] = dict(rows=rows, t_box=t_box, t_full=t_full, lo=lo, hi=hi, kids=kids, meta=meta, avail=(avail1, avail2),
                  counts=R['counts'], exit_sub={k: tot(v) / 60 for k, v in R['exit_sub'].items()},
                  p1_items=meta['p1_items'], p2_items=meta['p2_items'])

def md(n, o):
    t = ['', '#### Lesson %d' % n, '', '| Part | Scripted | Speak | Wait | Activity | Transition | Need | Diff | Flag |', '|---|---|---|---|---|---|---|---|---|']
    for r in o['rows']:
        t.append('| %s | %s | %.1f | %.1f | %.1f | %.1f | %.1f | %+.1f | %s |' % (r['name'], r['sc'], r['sp'], r['wt'], r['ac'], r['tr'], r['need'], r['diff'], r['flag']))
    t.append('| **Total, worksheet blocks held to their scripted minutes** | **90** | | | | | **%.1f** (range %.0f-%.0f) | **%+.1f** | |' % (o['t_box'], o['lo'], o['hi'], o['t_box'] - 90))
    t.append('| **Total if middle pairs finish page 1** | 90 | | | | | **%.1f** | %+.1f | |' % (o['t_full'], o['t_full'] - 90))
    return '\n'.join(t)


# ---------------- recommended plan (the fix scenario) ----------------
# For every lesson: what stays in class (page 1, page 2, page-2 teaching slides), what moves to take-home, and the
# mini-lesson slides that move out.  Minutes per answer part are the same MIDDLE-child estimates as above.
FIX = {
 1: dict(drop_mini=[], keep_teach=['teachest', 'teachbrackets'], p1=[(2, [1, 2]), (3, [7])], p2=[(4, [1.25, 1.5, 1, 1.25]), (5, [1.5])], game_cap=120),
 2: dict(drop_mini=[], keep_teach=['teachback'], p1=[(1, [1, 1, 2.5]), (2, [1.5, 1.5]), (3, [3])], p2=[(5, [4, 1]), (4, [1.5])]),
 3: dict(drop_mini=[], keep_teach=['teachdiff'], p1=[(1, [1.5, 3.5, 1.5]), (2, [0.5, 4])], p2=[(4, [1.5, 1.5, 3.5])]),
 4: dict(drop_mini=[], keep_teach=['teachtake', 'teachsame'], p1=[(1, [1, 1.5, 1.5, 1]), (2, [1, 1, 2])], p2=[(5, [1, 2, 1.5]), (4, [0.5, 1.5, 1.5, 1.5, 1])]),
 5: dict(drop_mini=['teachlist'], keep_teach=[], p1=[(2, [4.5, 1.5]), (3, [1.5, 2, 1.5])], p2=[(4, [1, 2.5, 1, 2])]),
 6: dict(drop_mini=[], keep_teach=['teachplans'], p1=[(1, [3, 2]), (2, [1, 3, 0.5]), (3, [1])], p2=[(4, [2, 3.5]), (6, [2])]),
 7: dict(drop_mini=[], keep_teach=['teachrem'], p1=[(1, [3, 1, 1.5]), (3, [1, 1, 2.5])], p2=[(2, [1, 1.5, 2, 1]), (4, [1, 1, 1.5, 1])]),
 8: dict(drop_mini=[], keep_teach=['teachchain', 'teachcombo'], p1=[(1, [0.75, 0.75, 0.75, 1.5]), (2, [2.5, 3])], p2=[(3, [1.5, 2]), (4, [1, 2])]),
 9: dict(drop_mini=['try3'], keep_teach=['teachgs', 'teachsup'], p1=[(1, [3, 1.5]), (2, [2, 2.5])], p2=[(3, [4.5]), (4, [3])], game_cap=120, expl_cap=330),
 10: dict(drop_mini=['try2'], keep_teach=['teachsq'], p1=[(1, [5]), (2, [4.5])], p2=[(3, [4.5]), (4, [1.5])]),
}
BUFFER = 2.0

def plan(n, D):
    S = load_slides(n); L = LES[n]; F = FIX[n]
    up = lambda x: -(-x * 2 // 1) / 2
    ids = [s['id'] for s in S]; i_ws1a = ids.index('ws1ans'); i_ws2 = ids.index('ws2')
    all_teach = [i for i in ids[i_ws1a + 1:i_ws2] if not [s for s in S if s['id'] == i][0]['opt']]
    drop = list(F['drop_mini']) + [i for i in all_teach if i not in F['keep_teach']]
    fx = dict(try_f=0.7, drop=drop, p1=F['p1'], p2=F['p2'], start2=[(q, None) for q, _ in F['p2']])
    fx['game_cap'] = F.get('game_cap', 150)
    if n in (1, 2, 6, 9, 10): fx['expl_cap'] = F.get('expl_cap', 360)
    R = model(n, D, S, fx); wb = R['wb']
    g = lambda k: up(tot(R[k]) / 60)
    b = dict(open=max(2.0, g('open')), sneak=g('sneak'), warm=g('warm'), explore=g('explore'), mini=g('mini'), brk=g('brk'),
             chk1=up(tot(wb['chk1']) / 60), teach=up(tot(wb['teach']) / 60), chk2=up(tot(wb['chk2']) / 60), talk=g('talk'), exit=g('exit'))
    b['p1'] = up(tot(wb['p1']) / 60); b['p2'] = up(tot(wb['p2']) / 60)
    used = sum(b.values())
    b['buffer'] = round(90 - used, 1)      # whatever is left is the standing buffer (target 2 min)
    return dict(budgets=b, p1_work=sum(sum(x) for _, x in F['p1']), p2_work=sum(sum(x) for _, x in F['p2']), drop=drop, fx=fx,
                p1_q=[q for q, _ in F['p1']], p2_q=[q for q, _ in F['p2']])

PLAN_NAMES = [('open', 'Opening (inside the 90)'), ('sneak', 'Sneak-peek'), ('warm', 'Warm-up'), ('explore', 'Explore'), ('mini', 'Mini-lesson'),
              ('brk', 'Brain break'), ('p1', 'WB page 1 pairs'), ('chk1', 'WB check p1'), ('teach', 'WB teaching'), ('p2', 'WB page 2 alone'),
              ('chk2', 'WB check p2'), ('talk', 'Talk time'), ('exit', 'Exit/reflect/close'), ('buffer', 'Buffer')]

if __name__ == '__main__':
    D = load_data(); out = {}
    for n in range(1, 11): report(n, D, out)
    if '--plan-md' in sys.argv:
        P = {n: plan(n, D) for n in range(1, 11)}
        print('| Part | Old | ' + ' | '.join('L%d' % n for n in range(1, 11)) + ' |'); print('|---|---|' + '---|' * 10)
        old = dict(open=0, sneak=3, warm=6, explore=12, mini=12, brk=4, p1=12, chk1=4, teach=5, p2=14, chk2=4, talk=6, exit=8, buffer=0)
        for k, lab in PLAN_NAMES:
            print('| %s | %s | ' % (lab, old[k]) + ' | '.join('%.1f' % P[n]['budgets'][k] for n in range(1, 11)) + ' |')
        print('| **Total** | **90** | ' + ' | '.join('**%.0f**' % sum(P[n]['budgets'].values()) for n in range(1, 11)) + ' |')
        sys.exit()
    if '--plan' in sys.argv:
        for n in range(1, 11):
            pl = plan(n, D); b = pl['budgets']
            print('L%d' % n, ' | '.join('%s %.1f' % (lab, b[k]) for k, lab in PLAN_NAMES), '| SUM %.1f' % sum(b.values()))
            print('    p1 Qs', pl['p1_q'], 'MID work %.1f' % pl['p1_work'], '| p2 Qs', pl['p2_q'], 'MID work %.1f' % pl['p2_work'], '| dropped slides', pl['drop'])
        sys.exit()
    if '--json' in sys.argv:
        print(json.dumps(out, indent=1, default=str))
    else:
        for n in range(1, 11):
            print(md(n, out[n]))
        print()
        print('lesson | T_box | range | T_full | page-1 MID work (min) / available | page-2 start-set MID (min) / avail | LOW,MID,HIGH items p1,p2 | slides | SAY words')
        for n in range(1, 11):
            o = out[n]; m = o['meta']
            print(n, '%.1f' % o['t_box'], '%.0f-%.0f' % (o['lo'], o['hi']), '%.1f' % o['t_full'], '%.1f/%.1f' % (m['p1_mid'], o['avail'][0]),
                  '%.1f/%.1f' % (m['start2_mid'], o['avail'][1]), o['kids'], (o['p1_items'], o['p2_items']), o['counts'])
