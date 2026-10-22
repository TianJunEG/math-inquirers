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
import json, re, html, subprocess, sys, os

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

def lesson_model(n, D, sc):
    S = SCEN[sc]
    hp = HP[n]
    les = D['lessons'][n - 1]; scr = D['scripts'][str(n)]; dk = D['deck'][str(n)]; gp = D['gaps'][str(n)]; gc = D['gaps']['common']
    sl = slides(n)
    byid = {s[0]: s for s in sl}
    sec = lambda words, wpm: words / wpm * 60.0
    saysec = lambda w: sec(w, S['say'])
    qsec = lambda w: sec(w, S['q'])
    rows = []  # (part, scripted, speak, wait, act, trans, rec)
    def add(part, scripted, speak=0, wait=0, act=0, trans=0, rec=None, note=''):
        r = S['rec'] if rec is None else rec
        rows.append(dict(part=part, sched=scripted, speak=speak / 60, wait=wait / 60, act=act / 60, trans=trans / 60,
                         rec=r / 60, note=note))
    nQ = lambda ask: len(ask)
    # 1 Opening
    add('Opening 0-1', 1, speak=saysec(say_words(scr['hook'])) + qsec(wc('Today we will ' + dk['today'])), wait=0,
        act=0, trans=S['slide'] + 8 * 2)  # title slide + greeting each child by name (~2 s x 8)
    # 2 Sneak peek
    pre = gp['pre']
    add('Sneak-peek 1-4', 3, speak=saysec(wc(gc['preSay'])) + qsec(sum(wc(x['q']) for x in pre)) + saysec(sum(wc(x['a']) for x in pre) + 12),
        wait=0, act=(60 + 120) * S['act'] + 20, trans=S['slide'] + 15)
    # 3 Warm-up
    wq = dk['warmQs']; ask3 = [wq[0], wq[2], wq[4]]
    add('Warm-up 4-8', 4, speak=saysec(say_words(scr['warmIntro'])) + qsec(sum(wc(x[0]) for x in ask3)),
        wait=3 * S['wait'], act=hp['game'] * S['act'], trans=2 * S['slide'])
    # 4 Explore
    n_ex_sl = sum(1 for s in sl if s[0] in ('explore1', 'goexp', 'explore2') or s[0].startswith('card'))
    ex_speak = saysec(say_words(scr['predict']) + 15 + 4 + 20) + qsec(sum(wc(x) for x in dk['expSetup']) + sum(wc(x[0]) for x in dk['expAsk']))
    ex_wait = S['wait'] * 0.7 + nQ(dk['expAsk']) * (S['wait'] + 30)  # predict (write a guess) + 3 debrief Qs with 'how do you know?'
    ex_act = hp['ex_work'] * 60 * S['act'] + hp['ex_extra']
    ex_trans = n_ex_sl * S['slide'] + 2 * S['breakout'] + hp['ex_mat'] * S['matx']
    add('Explore 8-20', 12, speak=ex_speak, wait=ex_wait, act=ex_act, trans=ex_trans)
    # 5 Mini-lesson: slides from teach1 to key
    ids = [s[0] for s in sl]
    i0 = ids.index('teach1'); i1 = ids.index('key')
    mini = sl[i0:i1 + 1]
    teach_w = sum(s[1] for s in mini if s[0].startswith(('teach', 'we')))
    try_w = sum(s[1] for s in mini if s[0].startswith('try'))
    n_teach = sum(1 for s in mini if s[0].startswith(('teach', 'we')))
    key_say = wc(dk['keyHead'] + ' ' + dk['keyBig']) + 12
    mini_speak = saysec(say_words(scr['think']) + key_say) + saysec(0.5 * teach_w) + qsec(try_w)
    mini_wait = n_teach * S['wait'] + 15
    mini_act = 0; n_try = 0
    for k, (items, sps) in hp['try_'].items():
        mini_act += items * sps * S['act']; n_try += 1
    mini_wait += n_try * (S['hold'] + 20)
    add('Mini-lesson 20-32', 12, speak=mini_speak, wait=mini_wait, act=mini_act, trans=len(mini) * S['slide'])
    # 6 Brain break
    add('Brain break 32-36', 4, speak=saysec(wc(dk['brk'])), wait=0, act=150 * S['act'] + 45, trans=S['slide'])
    # 7 Worksheet block (page 1 row includes the 2-minute start; L5, L6, L10 begin with a 2-minute teach slide)
    ws_say = saysec(wc('Pairs first. Read each question aloud and talk about it before you write. I am not looking for speed. I am looking for good thinking.') + wc(gc['neutral']) + 8)
    pre_teach = hp.get('pre_teach', False)
    if pre_teach:
        pt = [s for s in sl[ids.index('break') + 1: ids.index('ws1')]]
        w = sum(s[1] for s in pt)
        add('WS teach slide 36-38', 2, speak=saysec(w), wait=S['wait'], act=40 * S['act'], trans=len(pt) * S['slide'])
        p1_sched = 12; p1_rec = 0
    else:
        p1_sched = 14; p1_rec = None
    p1, p2 = hp['ws']
    p1_need = sum(p1) * PAIR * 60 * S['act']
    p2_need = sum(p2) * 60 * S['act']
    add('WS page 1 pairs 36-50' if not pre_teach else 'WS page 1 pairs 38-50', p1_sched, speak=ws_say, act=p1_need, trans=120 + S['slide'], rec=p1_rec, note='start 2 min + content demand of Core Q1-Q%d, MIDDLE, pairs' % len(p1))
    def check(page, extra_slides=1):
        parts = hp['parts'][page]; ex = hp['expl'][page]; q = len(hp['ws'][page])
        ans_words = 0
        return dict(speak=parts * 8 + q * 15 + ex * 30 + 10, trans=S['slide'])
    c1 = check(0)
    add('WS check page 1 50-52', 2, speak=c1['speak'] - 0, trans=c1['trans'], rec=0)
    wt = hp['wsteach']
    wt_w = sum(byid[k][1] for k in wt)
    wt_speak = saysec(wt_w)
    wt_wait = sum(S['wait'] if not k.startswith('try') else (S['hold'] + 20) for k in wt)
    wt_act = sum(v for v in wt.values()) * S['act']
    add('WS teaching 52-57', 5, speak=wt_speak, wait=wt_wait, act=wt_act, trans=len(wt) * S['slide'], rec=0)
    add('WS page 2 alone 57-69', 12, act=p2_need, rec=0, note='content demand of Core Q%d-Q%d, MIDDLE' % (len(p1) + 1, len(p1) + len(p2)))
    c2 = check(1)
    add('WS check page 2 69-72', 3, speak=c2['speak'], trans=c2['trans'], rec=0)
    # REC cue for worksheet counted on 'WS start'
    # 8 Talk
    talk_words = say_words(scr['talk']) + 20
    add('Talk time 72-80', 8, speak=saysec(talk_words) + qsec(wc(les['share'])), wait=S['wait'] * 1, act=120 * S['act'] + 3 * 45 + 45, trans=S['slide'])
    # 9 Exit ticket
    n10 = n == 10
    add('Exit ticket %s' % ('80-85' if n10 else '80-87'), 5 if n10 else 7, speak=qsec(wc(les['exit']['q'])) + saysec(25), wait=0,
        act=hp['exit_s'] * S['act'] + 8 * 15 + 30, trans=S['slide'] + 30)
    # 10 Looking back
    add('Looking back %s' % ('85-87' if n10 else '87-89'), 2, speak=saysec(wc(gc['refSay'])), act=75 * S['act'], trans=S['slide'])
    # 11 Close
    if n10:
        add('Certificates + close 87-90', 3, speak=saysec(say_words(scr['close'])), act=8 * 12 * S['act'], trans=S['slide'] + 20)
    else:
        add('Closing + stamps 89-90', 1, speak=saysec(say_words(scr['close'])), act=20, trans=S['slide'] + 15)
    # REC cue rows: the 'rec' value was assigned per row; rows for sub-parts of the worksheet carry rec=0 except start
    for r in rows:
        r['need'] = r['speak'] + r['wait'] + r['act'] + r['trans'] + r['rec']
        r['diff'] = r['need'] - r['sched']
    # the 'WS start' row holds the REC for the whole worksheet block, others 0
    return rows

def flag(diff):
    if diff >= 2.0: return 'OVER'
    if diff >= 0.5: return 'TIGHT'
    if diff <= -3.0: return 'LOOSE'
    return 'OK'

def totals(rows):
    sched = sum(r['sched'] for r in rows)
    full = sum(r['need'] for r in rows)  # waits for the MIDDLE child to finish the Core pages
    boxed = 0
    for r in rows:
        if r['part'].startswith('WS page'):  # time-boxed: tutor stops the work window on the clock
            boxed += min(r['need'], r['sched'])
        else:
            boxed += r['need']
    return sched, boxed, full

def tier_items(n):
    hp = HP[n]; out = {}
    p1, p2 = hp['ws']
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

def spare_for_extension(n):
    hp = HP[n]; p1, p2 = hp['ws']; p1_win = 10 if hp.get('pre_teach') else 12
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

if __name__ == '__main__':
    D = load()
    mode = sys.argv[1] if len(sys.argv) > 1 else '--summary'
    if mode == '--tables':
        for n in range(1, 11):
            print('\n### Lesson %d: %s\n' % (n, D['lessons'][n - 1]['title']))
            print(md_table(n, D))
    elif mode == '--json':
        out = {}
        for n in range(1, 11):
            out[n] = {sc: [dict(r, flag=flag(r['diff'])) for r in lesson_model(n, D, sc)] for sc in SCEN}
        print(json.dumps(out, indent=1))
    else:
        print('lesson  sched  low  central(boxed/full)  high   | slides  SAYwords')
        for n in range(1, 11):
            res = {sc: totals(lesson_model(n, D, sc)) for sc in SCEN}
            st = lesson_stats(n, D)
            print('%2d  %4.0f  %5.1f  %5.1f/%5.1f  %5.1f   | %2d(%2d)  %4d  tiers=%s' % (
                n, res['central'][0], res['low'][2], res['central'][1], res['central'][2], res['high'][2],
                st['slides'], st['shown'], st['say_words'], tier_items(n)))
