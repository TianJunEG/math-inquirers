"""Lesson timing model for Math Inquirers P2 (ages 7-9). ANALYSIS ONLY: reads content, writes nothing but stdout.

Run:  python3 -I docs/audit/timing_p2.py [--tables | --summary | --json]
      (default: --summary).  --tables prints the per-lesson markdown tables used in docs/audit/timing_p2.md.

Sources read: p2/data.js (via node: lessons, scripts = SAY lines, deck, qbank, gaps), split/p2lN/project/deck.json and
slides/*.html (slide order, on-slide text, speaker notes), workbook text from the PDF (counted by hand, see WS below).

MODEL (identical for every level):
  speaking   tutor speech 125 wpm (pauses included); questions read aloud 115 wpm
  waiting    10 s after each group question + 20 s to take one or two answers = 30 s; hold-up boards 30 s
  transition 25 s per slide change online; 90 s each way for breakout rooms; 60-150 s to find/hand out materials;
             120 s to get started on the worksheet
  REC cue    10 s said at the start of each of the 11 guide segments
  activity   scripted time for explore pair work / worksheet / break, but replaced by a content-based estimate of what
             the task really needs where the task is bigger or smaller than the window (see per-lesson tables)
  tiers      per-question minutes below are for a MIDDLE child working alone; pairs x1.15 (talk before write);
             LOW = x1.7, HIGH = x0.65
  flags      diff = needed - scripted; OVER >= +2.0; TIGHT +0.5..+2.0; OK -3.0..+0.5; LOOSE <= -3.0
"""
import json, re, html, subprocess, sys, os, math

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
WPM_SAY, WPM_Q = 125, 115

SCEN = {  # central is the base model; low/high bracket it
    'low':     dict(slide=20, breakout=60,  wait=20, hold=20, rec=8,  say=140, q=130, act=0.92, matx=0.7),
    'central': dict(slide=25, breakout=90,  wait=30, hold=30, rec=10, say=125, q=115, act=1.00, matx=1.0),
    'high':    dict(slide=30, breakout=120, wait=40, hold=40, rec=10, say=110, q=100, act=1.10, matx=1.3),
}

def wc(s):
    return len(re.findall(r"\S+", s or ''))

def load():
    js = ("const L=require('./data.js');process.stdout.write(JSON.stringify({lessons:L.lessons,scripts:L.scripts,"
          "deck:L.deck,qbank:L.qbank,gaps:L.gaps}));")
    out = subprocess.run(['node', '-e', js], cwd=os.path.join(ROOT, 'p2'), capture_output=True, text=True, check=True).stdout
    return json.loads(out)

def slides(n):
    dk = json.load(open(os.path.join(ROOT, 'split', f'p2l{n}', 'project', 'deck.json')))
    res = []
    for sid in dk['order']:
        h = open(os.path.join(ROOT, 'split', f'p2l{n}', 'project', 'slides', sid + '.html')).read()
        note = re.search(r'<aside>(.*?)</aside>', h, re.S)
        body = re.sub(r'<aside>.*?</aside>', '', h, flags=re.S)
        body = re.sub(r'<svg.*?</svg>', ' ', body, flags=re.S)
        txt = re.sub(r'<[^>]+>', ' ', body)
        txt = re.sub(r'\s+', ' ', html.unescape(txt))
        txt = txt.replace('Math Inquirers P2 Holiday Program • Notice it. Test it. Explain why.', '')
        txt = re.sub(r'^\s*\d+\s*[–-]\s*\d+ MIN', '', txt.strip())
        res.append((sid.split('-', 1)[1], wc(txt), wc(html.unescape(note.group(1)) if note else '')))
    return res

# ---------------------------------------------------------------------------------------------------------------
# Hand-judged inputs (from reading each lesson's workbook pages, slides and script).
# ws: core workbook minutes per numbered question for a MIDDLE child working alone (page 1 then page 2)
# parts: lettered sub-answers on the page (for the check-together slide), expl: items needing a spoken "how do you know"
# ---------------------------------------------------------------------------------------------------------------
HP = {
 1: dict(game=135, ex_work=4.5, ex_mat=60, ex_extra=60,
         try_=dict(try1=(3, 35), try2=(3, 40)), ws=([2.5, 4, 3], [4, 3, 6]), parts=(10, 8), expl=(2, 1),
         wsteach=dict(teachchart=40, teachcount=45, teachriddle=30), exit_s=75),
 2: dict(game=105, ex_work=5, ex_mat=20, ex_extra=0,
         try_=dict(try1=(3, 60), try2=(3, 60), try3=(3, 45)), ws=([4, 4, 6], [5.5, 6, 4]), parts=(10, 6), expl=(2, 1),
         wsteach=dict(teachsq=20, teachtri=20, teachtwo=20), exit_s=60),
 3: dict(game=210, ex_work=6, ex_mat=60, ex_extra=0,
         try_=dict(try1=(3, 30), try2=(3, 60)), ws=([2.5, 3, 4], [3.5, 2.5, 5]), parts=(6, 6), expl=(1, 1),
         wsteach=dict(teachshare=0, teachround=0, teachall=20, try3=180), exit_s=150),
 4: dict(game=120, ex_work=5, ex_mat=90, ex_extra=0,
         try_=dict(try1=(3, 30)), ws=([4.5, 4.5, 3.5], [4, 5, 4]), parts=(8, 11), expl=(2, 2),
         wsteach=dict(teachtimes=0, teachgrow=0, teachboth=20, try2=150), exit_s=90),
 5: dict(game=180, ex_work=7, ex_mat=60, ex_extra=0,
         try_=dict(try1=(3, 50), try2=(3, 50)), ws=([5.5, 3.5], [3.5, 4, 4]), parts=(6, 6), expl=(0, 1),
         wsteach=dict(teachparts=0, teachorder=30), exit_s=90, pre_teach=True),
 6: dict(game=300, ex_work=6.5, ex_mat=90, ex_extra=0,
         try_=dict(try1=(3, 50), try2=(3, 50)), ws=([5, 5], [3.5, 4.5, 2, 5]), parts=(7, 6), expl=(1, 1),
         wsteach=dict(teachchange=0, teachenough=30, teachlist2=0), exit_s=120, pre_teach=True),
 7: dict(game=120, ex_work=8, ex_mat=120, ex_extra=0,
         try_=dict(try1=(3, 35), try2=(3, 40)), ws=([3, 2, 5.5], [6, 3.5, 4]), parts=(8, 9), expl=(2, 1),
         wsteach=dict(teachadd=0, tryadd=120, teachstory=0, teachsame=0), exit_s=75),
 8: dict(game=150, ex_work=7, ex_mat=120, ex_extra=0,
         try_=dict(try1=(3, 35), try2=(3, 50)), ws=([5, 7.5], [6, 9]), parts=(5, 4), expl=(1, 1),
         wsteach=dict(teachcube=0, trycube=150, teachnet=0, trynet=180), exit_s=90),
 9: dict(game=180, ex_work=8, ex_mat=150, ex_extra=0,
         try_=dict(try1=(3, 50), try2=(3, 70)), ws=([5, 6], [4, 4, 5]), parts=(6, 6), expl=(1, 1),
         wsteach=dict(teachlen=40, teachclock=30, teachdur=0, trytime=180), exit_s=90),
 10: dict(game=300, ex_work=6, ex_mat=30, ex_extra=60,
          try_=dict(try1=(3, 55), try2=(3, 50)), ws=([4.5, 3.5, 4], [4, 3.5, 4]), parts=(7, 6), expl=(1, 1),
          wsteach=dict(teachlogic=0, teachgrow=60), exit_s=150, pre_teach=True),
}
TIER = dict(LOW=1.7, MIDDLE=1.0, HIGH=0.65)
PAIR = 1.15

def say_words(s):
    return wc(' '.join(s))

COMMON_FIX = dict(sneak_say_words=28, sneak_work=(45, 90), warm_q=2, ex_breakout_scale=0.667, deb_disc=15, ex_slides_cut=1,
                  brk_act=120, chk_part=5, chk_q=10, talk_act=90 + 70 + 20, exit_check=80, exit_reveal=20, open_greet=0)

def lesson_model(n, D, sc, fix=None):
    """Return rows for one lesson. fix=None gives the plan as scripted; fix=dict gives the re-budgeted plan."""
    S = SCEN[sc]
    fx = fix or {}
    g = lambda k, d: fx.get(k, d)
    hp = HP[n]
    les = D['lessons'][n - 1]; scr = D['scripts'][str(n)]; dk = D['deck'][str(n)]; gp = D['gaps'][str(n)]; gc = D['gaps']['common']
    sl = slides(n)
    byid = {s[0]: s for s in sl}
    ids = [s[0] for s in sl]
    sec = lambda words, wpm: words / wpm * 60.0
    saysec = lambda w: sec(w, S['say'])
    qsec = lambda w: sec(w, S['q'])
    B = g('budget', {})
    rows = []
    def add(key, part, scripted, speak=0, wait=0, act=0, trans=0, rec=None, note=''):
        r = S['rec'] if rec is None else rec
        rows.append(dict(key=key, part=part, sched=B.get(key, scripted), speak=speak / 60, wait=wait / 60, act=act / 60,
                         trans=trans / 60, rec=r / 60, note=note))
    n10 = n == 10
    # 1 Opening
    add('open', 'Opening 0-1', 1, speak=saysec(say_words(scr['hook'])) + qsec(wc('Today we will ' + dk['today'])),
        trans=S['slide'] + g('open_greet', 16))
    # 2 Sneak peek
    pre = gp['pre']
    w1, w2 = g('sneak_work', (60, 120))
    add('sneak', 'Sneak-peek 1-4', 3, speak=saysec(g('sneak_say_words', wc(gc['preSay']))) + qsec(sum(wc(x['q']) for x in pre)) + saysec(sum(wc(x['a']) for x in pre) + 12),
        act=(w1 + w2) * S['act'] + 20, trans=S['slide'] + 15)
    # 3 Warm-up
    wq = dk['warmQs']; askq = [wq[0], wq[2], wq[4]][:g('warm_q', 3)]
    add('warm', 'Warm-up 4-8', 4, speak=saysec(say_words(scr['warmIntro']) * g('warm_intro_scale', 1)) + qsec(sum(wc(x[0]) for x in askq)),
        wait=len(askq) * S['wait'], act=g('warm_game', hp['game']) * S['act'], trans=2 * S['slide'])
    # 4 Explore
    n_ex_sl = sum(1 for s in sl if s[0] in ('explore1', 'goexp', 'explore2') or s[0].startswith('card')) - g('ex_slides_cut', 0)
    deb_q = g('deb_q', len(dk['expAsk']))
    ex_speak = saysec(say_words(scr['predict']) + 15 + 4 + 20) + qsec(sum(wc(x) for x in dk['expSetup']) + sum(wc(x[0]) for x in dk['expAsk'][:deb_q]))
    ex_wait = S['wait'] * 0.7 + deb_q * (S['wait'] + g('deb_disc', 30) * S['wait'] / 30)
    ex_act = g('ex_work', hp['ex_work']) * 60 * S['act'] + g('ex_extra', hp['ex_extra'])
    ex_trans = n_ex_sl * S['slide'] + 2 * S['breakout'] * g('ex_breakout_scale', 1.0) + g('ex_mat', hp['ex_mat']) * S['matx']
    add('explore', 'Explore 8-20', 12, speak=ex_speak, wait=ex_wait, act=ex_act, trans=ex_trans)
    # 5 Mini-lesson: slides from teach1 to key, with optional drops/merges/additions
    i0 = ids.index('teach1'); i1 = ids.index('key')
    mini = [s for s in sl[i0:i1 + 1] if s[0] not in g('mini_drop', [])] + [byid[k] for k in g('mini_add', [])]
    merged = set(g('mini_merge', []))
    teach_w = sum(s[1] for s in mini if s[0].startswith(('teach', 'we')))
    try_w = sum(s[1] for s in mini if s[0].startswith('try'))
    n_teach = sum(1 for s in mini if s[0].startswith(('teach', 'we')) and s[0] not in merged)
    key_say = wc(dk['keyHead'] + ' ' + dk['keyBig']) + 12
    mini_speak = saysec(say_words(scr['think']) + key_say) + saysec(0.5 * teach_w) + qsec(try_w)
    mini_act = 0; n_try = 0
    for k, (items, sps) in g('mini_try', hp['try_']).items():
        if k in [s[0] for s in mini]:
            mini_act += items * sps * S['act']; n_try += 1
    mini_wait = n_teach * S['wait'] + 15 + n_try * (S['hold'] + 20)
    add('mini', 'Mini-lesson 20-32', 12, speak=mini_speak, wait=mini_wait, act=mini_act,
        trans=(len(mini) - len(merged)) * S['slide'])
    # 6 Brain break
    add('brk', 'Brain break 32-36', 4, speak=saysec(wc(dk['brk'])), act=g('brk_act', 150 + 45) * S['act'] if False else g('brk_act', 195) * S['act'], trans=S['slide'])
    # 7 Worksheet block
    ws_say = saysec(wc('Pairs first. Read each question aloud and talk about it before you write. I am not looking for speed. I am looking for good thinking.') + wc(gc['neutral']) + 8)
    pre_teach = hp.get('pre_teach', False)
    if pre_teach:
        pt = sl[ids.index('break') + 1: ids.index('ws1')]
        add('wst', 'WS teach slide 36-38', 2, speak=saysec(sum(s[1] for s in pt)), wait=S['wait'], act=40 * S['act'], trans=len(pt) * S['slide'])
        p1_sched, p1_rec = 12, 0
        p1name = 'WS page 1 pairs 38-50'
    else:
        p1_sched, p1_rec = 14, None
        p1name = 'WS page 1 pairs 36-50'
    p1, p2 = g('ws_p1', hp['ws'][0]), g('ws_p2', hp['ws'][1])
    add('p1', p1name, p1_sched, speak=ws_say, act=sum(p1) * PAIR * 60 * S['act'], trans=120 + S['slide'], rec=p1_rec,
        note='start 2 min + Core demand, MIDDLE, pairs')
    parts = g('parts', hp['parts']); expl = g('expl', hp['expl'])
    chk = lambda page: (parts[page] * g('chk_part', 8) + len(hp['ws'][page] if False else (p1, p2)[page]) * g('chk_q', 15) + expl[page] * 30 + 10)
    add('c1', 'WS check page 1 50-52', 2, speak=chk(0), trans=S['slide'], rec=0)
    wt = g('wsteach', hp['wsteach'])
    wt_w = sum(byid[k][1] for k in wt)
    wt_wait = sum(S['wait'] if not k.startswith('try') else (S['hold'] + 20) for k in wt)
    add('wt', 'WS teaching 52-57', 5, speak=saysec(wt_w), wait=wt_wait, act=sum(wt.values()) * S['act'], trans=len(wt) * S['slide'], rec=0)
    add('p2', 'WS page 2 alone 57-69', 12, act=sum(p2) * 60 * S['act'], rec=0, note='Core demand, MIDDLE')
    add('c2', 'WS check page 2 69-72', 3, speak=chk(1), trans=S['slide'], rec=0)
    # 8 Talk
    add('talk', 'Talk time 72-80', 8, speak=saysec(say_words(scr['talk']) + 20) + qsec(wc(les['share'])), wait=S['wait'],
        act=g('talk_act', 120 + 135 + 45) * S['act'], trans=S['slide'])
    # 9 Exit ticket
    add('exit', 'Exit ticket %s' % ('80-85' if n10 else '80-87'), 5 if n10 else 7, speak=qsec(wc(les['exit']['q'])) + saysec(25),
        act=g('exit_s', hp['exit_s']) * S['act'] + g('exit_check', 120) + g('exit_reveal', 30), trans=S['slide'] + 30)
    # 10 Looking back
    add('lb', 'Looking back %s' % ('85-87' if n10 else '87-89'), 2, speak=saysec(wc(gc['refSay'])), act=75 * S['act'], trans=S['slide'])
    # 11 Close
    if n10:
        add('close', 'Certificates + close 87-90', 3, speak=saysec(say_words(scr['close'])), act=8 * 12 * S['act'], trans=S['slide'] + 20)
    else:
        add('close', 'Closing + stamps 89-90', 1, speak=saysec(say_words(scr['close'])), act=20, trans=S['slide'] + 15)
    for r in rows:
        r['need'] = r['speak'] + r['wait'] + r['act'] + r['trans'] + r['rec']
        r['diff'] = r['need'] - r['sched']
    if fix is not None and 'buffer' in fx:
        rows.append(dict(key='buffer', part='Standing buffer', sched=fx['buffer'], speak=0, wait=0, act=0, trans=0, rec=0, note='', need=0.0, diff=-fx['buffer']))
    return rows

# Lesson-specific parts of the re-budgeted plan (applied on top of COMMON_FIX). Every Core item moved out of class
# becomes a "home star" (take-home) item; no answers, tiers or pass rules change.
FIX = {
 1: dict(warm_game=100, ex_mat=30, mini_try={'try1': (2, 35), 'try2': (3, 40)}, ws_p2=[3.5, 6], parts=(7, 4),
         wsteach={'teachchart': 0, 'teachriddle': 20}),
 2: dict(warm_game=100, ex_mat=20, mini_drop=['try3'], mini_merge=['we2'], mini_try={'try1': (2, 60), 'try2': (1, 60)},
         ws_p1=[3.3, 4, 2.5], parts=(8, 4), expl=(1, 1), ws_p2=[5.5, 4], wsteach={'teachsq': 20, 'teachtwo': 20}),
 3: dict(warm_game=105, ex_work=5, ex_mat=30, exit_s=120, mini_drop=['try1'], mini_try={'try2': (2, 60)},
         wsteach={'teachshare': 0, 'teachround': 0, 'teachall': 20}),
 4: dict(warm_game=90, ex_mat=30, mini_add=['teachtimes', 'teachgrow'], mini_try={'try1': (3, 30)},
         ws_p1=[4.5, 2.5, 2.8], ws_p2=[3.2, 4, 4], parts=(6, 9), expl=(1, 1), wsteach={'teachboth': 20}),
 5: dict(warm_game=120, ex_work=5.5, ex_mat=30, deb_q=2, mini_try={'try1': (1, 50), 'try2': (2, 50)},
         ws_p1=[4.1, 3.5], parts=(5, 6)),
 6: dict(warm_game=120, ex_work=5.5, ex_mat=45, mini_try={'try1': (1, 50), 'try2': (2, 50)},
         ws_p1=[3.75, 4], ws_p2=[2, 2, 2, 5], parts=(6, 5), wsteach={'teachchange': 0, 'teachenough': 0, 'teachlist2': 0}),
 7: dict(warm_game=100, ex_work=5.5, ex_mat=60, deb_q=2, mini_merge=['we3'], mini_try={'try1': (2, 35), 'try2': (2, 40)},
         ws_p1=[2.3, 2, 5.5], ws_p2=[3.6, 3.5, 4], parts=(7, 7), wsteach={'teachadd': 0, 'teachstory': 0, 'teachsame': 0}),
 8: dict(warm_game=100, ex_work=5.5, ex_mat=30, mini_drop=['we3'], mini_try={'try1': (2, 35), 'try2': (2, 50)},
         ws_p1=[3.8, 5], ws_p2=[6, 4], parts=(4, 3), wsteach={'teachcube': 0, 'teachnet': 0}),
 9: dict(warm_game=105, ex_work=5.5, ex_mat=45, mini_drop=['try2'], mini_try={'try1': (2, 50)},
         ws_p1=[5, 3], ws_p2=[4, 1.5, 3.8], parts=(5, 4), wsteach={'teachclock': 30, 'teachdur': 0}),
 10: dict(warm_game=120, ex_work=4.5, ex_mat=30, ex_slides_cut=4, exit_s=120, mini_drop=['teach1', 'try1'], mini_try={'try2': (2, 50)},
          ws_p1=[4.5, 3.5], parts=(5, 6), wsteach={'teachlogic': 0, 'teachgrow': 0}),
}

STD = dict(open=1.5, sneak=4.5, warm=4.5, explore=13, mini=12, brk=3, wst=2.5, p1=14, c1=2.5, wt=4.5, p2=11.5, c2=2.5,
           talk=5, exit=5, lb=2, close=1.5)
STD_L10 = dict(STD, close=3)
DEV = {4: dict(wt=2.5), 9: dict(mini=10.5), 10: dict(mini=10, p1=12, wt=3.5)}

def final_budget(n):
    b = dict(STD_L10 if n == 10 else STD)
    if HP[n].get('pre_teach'): b['p1'] = 11.5
    else: b.pop('wst')
    b.update(DEV.get(n, {}))
    return b

def auto_budget(n, D):
    """Standard budget, raised (to the next half minute) only where the re-planned lesson needs more than the standard."""
    base = dict(STD_L10 if n == 10 else STD)
    rows = fixed_rows(n, D)
    b = {}
    for r in rows:
        k = r['key']
        if k not in base: continue
        std = base[k]
        if k == 'p1' and HP[n].get('pre_teach'): std = 11.5
        b[k] = std if r['need'] <= std + 0.25 else math.ceil(r['need'] * 2 - 1e-9) / 2
    return b

def fixed_rows(n, D, sc='central', with_budget=False):
    fx = dict(COMMON_FIX); fx.update(FIX[n])
    if with_budget:
        b = final_budget(n); fx['budget'] = b; fx['buffer'] = round(90 - sum(b.values()), 2)
    return lesson_model(n, D, sc, fx)

def flag(diff):
    if diff >= 2.0: return 'OVER'
    if diff >= 0.5: return 'TIGHT'
    if diff <= -3.0: return 'LOOSE'
    return 'OK'

def totals(rows):
    """(scripted, time-boxed need, content-complete need). Time-boxed: the tutor stops the two pair/alone work windows on the clock."""
    sched = sum(r['sched'] for r in rows)
    full = sum(r['need'] for r in rows)
    boxed = sum(min(r['need'], r['sched']) if r['key'] in ('p1', 'p2') else r['need'] for r in rows)
    return sched, boxed, full

def tier_items(n, fixed=False):
    hp = HP[n]; out = {}
    p1, p2 = hp['ws']
    if fixed:
        p1 = FIX[n].get('ws_p1', p1); p2 = FIX[n].get('ws_p2', p2)
    p1_win = 10 if hp.get('pre_teach') else 12
    for t, m in TIER.items():
        def count(qs, win, f):
            tot = 0; c = 0
            for q in qs:
                tot += q * m * f
                if tot <= win + 0.5: c += 1
                else: break
            return c
        out[t] = (count(p1, p1_win, PAIR), count(p2, 12, 1.0))
    return out

def spare_for_extension(n, fixed=False):
    hp = HP[n]; p1, p2 = hp['ws']
    if fixed:
        p1 = FIX[n].get('ws_p1', p1); p2 = FIX[n].get('ws_p2', p2)
    p1_win = 10 if hp.get('pre_teach') else 12
    res = {}
    for t, m in TIER.items():
        res[t] = (max(0, p1_win - sum(p1) * m * PAIR), max(0, 12 - sum(p2) * m))
    return res

def md_table(n, D, sc='central'):
    rows = lesson_model(n, D, sc)
    L = ['| Part | Scripted | Speak | Wait | Activity | Transition | REC | Needed | Diff | Flag |', '|---|--:|--:|--:|--:|--:|--:|--:|--:|---|']
    for r in rows:
        L.append('| %s | %.0f | %.1f | %.1f | %.1f | %.1f | %.2f | **%.1f** | %+.1f | %s |' % (
            r['part'], r['sched'], r['speak'], r['wait'], r['act'], r['trans'], r['rec'], r['need'], r['diff'], flag(r['diff'])))
    sched, boxed, full = totals(rows)
    L.append('| **Total** | **%.0f** | %.1f | %.1f | %.1f | %.1f | %.1f | **%.1f** (time-boxed %.1f) | %+.1f | |' % (
        sched, sum(r['speak'] for r in rows), sum(r['wait'] for r in rows), sum(r['act'] for r in rows),
        sum(r['trans'] for r in rows), sum(r['rec'] for r in rows), full, boxed, full - sched))
    return '\n'.join(L)

def lesson_stats(n, D):
    scr = D['scripts'][str(n)]; dk = D['deck'][str(n)]; gc = D['gaps']['common']; gp = D['gaps'][str(n)]
    sl = slides(n)
    say = (say_words(scr['hook']) + say_words(scr['warmIntro']) + say_words(scr['predict']) + say_words(scr['think'])
           + say_words(scr['talk']) + say_words(scr['close']) + wc(gc['preSay']) + wc(gc['refSay']) + 15 + 30
           + wc(dk['keyHead'] + dk['keyBig']))
    shown = [s for s in sl if s[0] not in ('stretch', 'challenge', 'chdiag', 'chwalk')]
    return dict(slides=len(sl), shown=len(shown), say_words=say, slide_words=sum(s[1] for s in shown), note_words=sum(s[2] for s in sl))

def sinks(D):
    """Mean over lessons of (needed - scripted) per part, time-boxed, plus the level-wide split of the extra time."""
    import collections
    ex = collections.defaultdict(float); cat = collections.defaultdict(float)
    for n in range(1, 11):
        rows = lesson_model(n, D, 'central')
        for r in rows:
            need = min(r['need'], r['sched']) if r['key'] in ('p1', 'p2') else r['need']
            ex[r['key']] += (need - r['sched']) / 10
            for c in ('speak', 'wait', 'act', 'trans', 'rec'):
                cat[c] += r[c] / 10
    return dict(ex), dict(cat)

if __name__ == '__main__':
    D = load()
    mode = sys.argv[1] if len(sys.argv) > 1 else '--summary'
    if mode == '--tables':
        for n in range(1, 11):
            print('\n### Lesson %d: %s\n' % (n, D['lessons'][n - 1]['title']))
            print(md_table(n, D))
    elif mode == '--fixed':
        for n in range(1, 11):
            rows = fixed_rows(n, D, 'central', True)
            buf = [r for r in rows if r['key'] == 'buffer'][0]
            order = [r for r in rows if r['key'] != 'buffer']
            i = [r['key'] for r in order].index('c2') + 1
            order.insert(i, buf)  # the flex block sits after the second check, before Talk time
            print('\n#### Lesson %d: %s (re-budgeted)\n' % (n, D['lessons'][n - 1]['title']))
            print('| New minutes | Part | Old budget | New budget | Needed (central) | Slack | Needed (fast / slow tutor) |')
            print('|---|---|--:|--:|--:|--:|--:|')
            lo = {r['key']: r for r in fixed_rows(n, D, 'low', True)}; hi = {r['key']: r for r in fixed_rows(n, D, 'high', True)}
            old = {r['key']: r['sched'] for r in lesson_model(n, D, 'central')}
            t = 0.0
            for r in order:
                k = r['key']
                print('| %g-%g | %s | %s | %.1f | %.1f | %+.1f | %.1f / %.1f |' % (t, t + r['sched'], r['part'],
                      ('%.0f' % old[k]) if k in old else '-', r['sched'], r['need'], r['sched'] - r['need'], lo[k]['need'], hi[k]['need']))
                t += r['sched']
            print('| 0-90 | **Total** | 90 | %.1f | %.1f | %+.1f | %.1f / %.1f |' % (sum(r['sched'] for r in rows), sum(r['need'] for r in rows), sum(r['sched'] - r['need'] for r in rows),
                                                                        sum(r['need'] for r in lo.values()), sum(r['need'] for r in hi.values())))
    elif mode == '--json':
        out = {}
        for n in range(1, 11):
            out[n] = {sc: [dict(r, flag=flag(r['diff'])) for r in lesson_model(n, D, sc)] for sc in SCEN}
        print(json.dumps(out, indent=1))
    else:
        print('lesson | scripted | as-scripted total: fast / central / slow (time-boxed) | content-complete central | slides(shown) | SAY words | items done in class LOW/MIDDLE/HIGH (page1,page2) of Core')
        for n in range(1, 11):
            res = {sc: totals(lesson_model(n, D, sc)) for sc in SCEN}
            st = lesson_stats(n, D)
            ti = tier_items(n)
            ncore = len(HP[n]['ws'][0]) + len(HP[n]['ws'][1])
            print('%2d | %.0f | %5.1f / %5.1f / %5.1f | %5.1f | %2d(%2d) | %4d | %s of %d' % (
                n, res['central'][0], res['low'][1], res['central'][1], res['high'][1], res['central'][2], st['slides'], st['shown'],
                st['say_words'], '/'.join('%d+%d=%d' % (ti[t][0], ti[t][1], sum(ti[t])) for t in ('LOW', 'MIDDLE', 'HIGH')), ncore))
        ex, cat = sinks(D)
        print('mean excess over scripted by part (min, time-boxed):', {k: round(v, 1) for k, v in sorted(ex.items(), key=lambda kv: -kv[1])})
        print('mean minutes by category:', {k: round(v, 1) for k, v in cat.items()})
