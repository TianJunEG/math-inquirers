#!/usr/bin/env python3
"""Lesson timing audit helper, Math Inquirers Level N=4 (P4, ages 9-11).

Analysis only. Reads (never writes) p4/data.js + p4/content/l1..l10.js (through node),
levels/reccues.js (REC cue lines), split/p4l*/project (deck order, slide text, speaker notes)
and the workbook HTML produced by each lesson's workbook(). Prints markdown tables to stdout.

    python3 docs/audit/timing_p4.py            # tables for the report
    python3 docs/audit/timing_p4.py --json     # raw numbers

MODEL (identical for every level; see docs/audit/timing_p4.md section 2)
  speech   : tutor SAY lines / narration 135 wpm; questions read aloud 125 wpm
  waits    : 10 s after each question put to the group + 20 s to take one or two answers (30 s);
             'hold up' moments 30 s
  moves    : slide change 20/25/30 s; breakout in and out 60/90/120 s each; worksheet start 120 s
  activity : scripted time for the game / brain break; judged time for explore, exit ticket and
             each workbook question (MIDDLE child; LOW child x1.7, HIGH child x0.65)
  fixed    : sneak-peek puzzles (2 x 90 s + 2 hold-ups + walkthrough), look-back (2 min child time),
             REC cue lines (real text from levels/reccues.js, spoken at 135 wpm), recording notice
Three tutor scenarios: BEST (lean), TYPICAL, SLOW.  Camera/tech glitches ignored.
"""
import json, re, html, subprocess, sys, os, math

ROOT = os.environ.get('MI_ROOT', '/home/user/math-inquirers')
P4 = ROOT + '/p4'
WPM_SAY, WPM_READ = 135.0, 125.0
GROUP = 8                       # children per tutor (design maximum)

SCEN = {
    #            slide, move(each way), optional 'your turn' slides, speaker-note ASKs, greeting s/child,
    #            second talk question, 'any other way?' ask in sneak, pair-talk move total (s)
    'BEST':    dict(slide=20, move=60,  opt=False, asks=False, greet=1.5, talk2=False, other=False, pairmove=0),
    'TYPICAL': dict(slide=25, move=90,  opt=True,  asks=True,  greet=2.5, talk2=True,  other=True,  pairmove=60),
    'LEAN':    dict(slide=25, move=90,  opt=False, asks=False, greet=2.5, talk2=True,  other=True,  pairmove=60),   # TYPICAL but skipping optional slides + note ASKs
    'SLOW':    dict(slide=30, move=120, opt=True,  asks=True,  greet=4.0, talk2=True,  other=True,  pairmove=120),
}
START_WS = 120                  # get started on the worksheet
HOLD = 30                       # hold-up moment
ASK = 30                        # 10 s wait + 20 s answers
LOWF, HIGHF = 1.7, 0.65         # LOW / HIGH child pace relative to MIDDLE

# ---- judged activity times (MIDDLE child / pair), minutes ---------------------------------
EXPLORE_HANDS = {1: 5.0, 2: 6.0, 3: 5.0, 4: 6.0, 5: 6.5, 6: 5.0, 7: 5.0, 8: 7.0, 9: 7.5, 10: 9.0}
EXIT_WRITE = {1: 2.0, 2: 1.5, 3: 1.0, 4: 1.7, 5: 2.0, 6: 1.7, 7: 2.5, 8: 1.0, 9: 1.5, 10: 3.0}
BREAK_ACTIVITY = 3.0            # play ~1.75 min + water/toilet/return ~1.25 min of the 4 scripted
GAME_ACTIVITY = 2.0             # warm-up round, as scripted ("about 2 minutes")
# workbook items: (label, minutes for a MIDDLE child, page, priority)  priority = on the printed "Aim for" note
P, C = True, False
ITEMS = {
 1: [('Q1', 3.5, 1, P), ('Q2', 3.0, 1, P), ('Q3', 3.5, 1, P), ('Q4', 4.5, 2, P), ('Q5', 7.0, 2, P), ('Q6', 6.0, 2, C)],
 2: [('Q1', 4.0, 1, P), ('Q2', 6.0, 1, P), ('Q3', 4.5, 1, P), ('Q4a', 4.0, 2, P), ('Q5', 4.5, 2, P), ('Q6a', 1.5, 2, P), ('Q4b', 3.0, 2, C), ('Q6bc', 4.0, 2, C)],
 3: [('Q1', 4.0, 1, P), ('Q2', 5.0, 1, P), ('Q3', 4.8, 1, P), ('Q4', 2.5, 2, P), ('Q5', 5.0, 2, P), ('Q6', 5.0, 2, P), ('Q7', 4.0, 2, C)],
 4: [('Q1', 5.0, 1, P), ('Q2', 2.5, 1, P), ('Q3', 2.5, 1, P), ('Q4', 6.5, 2, P), ('Q5', 3.2, 2, P), ('Q6', 4.0, 2, C)],
 5: [('Q1', 4.7, 1, P), ('Q2', 3.5, 1, P), ('Q3', 2.5, 1, P), ('Q4', 5.5, 2, P), ('Q5', 4.0, 2, P), ('Q6', 4.5, 2, C)],
 6: [('Q1', 8.0, 1, P), ('Q2', 5.0, 1, P), ('Q3', 2.9, 2, P), ('Q4', 4.0, 2, P), ('Q5', 3.0, 2, C), ('Q6', 1.5, 2, C)],
 7: [('Q1', 6.0, 1, P), ('Q2', 4.0, 1, P), ('Q3', 3.5, 1, P), ('Q4', 5.0, 2, P), ('Q5', 6.5, 2, P), ('Q6', 5.5, 2, C)],
 8: [('Q1', 5.0, 1, P), ('Q2', 3.0, 1, P), ('Q3', 3.5, 1, P), ('Q4', 4.0, 2, P), ('Q5', 5.0, 2, P), ('Q6', 5.0, 2, C)],
 9: [('Q1', 5.5, 1, P), ('Q2', 5.0, 1, P), ('Q3', 5.5, 2, P), ('Q4', 4.5, 2, P), ('Q5', 4.0, 2, C)],
 10: [('Q1', 6.5, 1, P), ('Q2', 6.0, 1, P), ('Q3', 4.5, 1, P), ('Q4', 4.5, 2, P), ('Q5', 3.5, 2, P), ('Q6', 5.0, 2, C)],
}
# fixed SAY texts copied from p4/guide.js
SNEAK_SAY = 'Two sneak-peek puzzles about {idea}. These are ideas we have not learnt yet, so guessing and "I do not know" are welcome. Nobody is marked. Write your answer on your own paper and hold it up to the camera when I say.'
EXPLORE_TALK = 'Talk to your partner while you work. I will come round and ask you questions.'
WS_SAY = 'Pairs first. Read each question aloud and talk about it before you write. I am not looking for speed. I am looking for good thinking.'
INVITE = 'After question 3 you may choose: carry on, or try Think harder.'
LOOK_SAY = ['Turn to page 3, to the small box called Looking back. You can write, tick or pass: you choose. Finish what you like: Something I did well, The hardest part was, What helped me. Two minutes, no talking.',
            'Model one yourself first: "{reflect}" Ticking "I am still stuck" is a good thing to do: it tells me where to help.']
REC_NOTICE = 'This lesson is being recorded. Only the tutor and the screen are recorded, and you can keep your camera off.'

# --------------------------------------------------------------------------------------------
NODE = r"""
const path = require('path'); process.chdir(process.argv[1] + '/p4');
const C = require(process.argv[1] + '/hp/common_html.js');
const L = require(process.argv[1] + '/p4/data.js');
const R = require(process.argv[1] + '/levels/reccues.js');
const H = Object.assign({}, C, { fig: s => '<div class="p img" style="text-align:center">' + s + '</div>' });
const segs = n => [['0–1 min','Opening'],['1–4 min','Sneak-peek puzzles (3 minutes)'],['4–8 min','Warm-up game and quick questions'],['8–18 min','Explore (in pairs, with objects)'],['18–30 min','Mini-lesson (you teach, they join in)'],['30–34 min','Brain break'],['34–80 min','Worksheet (pairs, then alone)'],['80–85 min','Talk time'],[n===10?'85–87 min':'85–88 min','Exit ticket and closing'],[n===10?'87–89 min':'88–90 min','Looking back (2 minutes)']];
console.log(JSON.stringify(L.content.map(c => ({ lesson: c.lesson, script: c.script, deck: c.deck, qbank: c.qbank, gaps: c.gaps,
  wb: c.workbook(H).map(String), rec: segs(c.lesson.n).map(s => R.cue(s[1], s[0]).say) }))));
"""

def load():
    out = subprocess.run(['node', '-e', NODE, ROOT], capture_output=True, text=True, cwd=P4, check=True).stdout
    return json.loads(out)

def strip(s):
    return html.unescape(re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', s))).strip()

def nw(s):
    return len(re.findall(r'\S+', s)) if s else 0

def spk(words):  return words / WPM_SAY * 60.0
def rd(words):   return words / WPM_READ * 60.0

def parse_slides(n):
    base = '%s/split/p4l%d/project/' % (ROOT, n)
    deck = json.load(open(base + 'deck.json'))
    out = []
    for sid in deck['order']:
        s = open(base + 'slides/%s.html' % sid).read()
        notes = re.findall(r'<aside>(.*?)</aside>', s, re.S)
        body = re.sub(r'<aside>.*?</aside>', '', s, flags=re.S)
        body = re.sub(r'<p[^>]*bottom:64px[^>]*>.*?</p>', '', body, flags=re.S)
        t = strip(body)
        m = re.search(r'(\d+)\s*[–-]\s*(\d+)\s*MIN', t)
        nt = strip(notes[0]) if notes else ''
        asks = re.findall(r'\bAsk\b[^"“”]{0,60}?["“]([^"”]+)["”]', nt)
        out.append(dict(id=sid.replace('p4l%d-' % n, ''), t=t, words=nw(re.sub(r'\d+\s*[–-]\s*\d+\s*MIN', '', t)), notes=nt,
                        asks=asks, start=int(m.group(1)) if m else None, end=int(m.group(2)) if m else None))
    return out

def bucket(sl):
    b = {k: [] for k in ['open', 'sneak', 'warm', 'explore', 'mini', 'break', 'ws1', 'chk1', 'teach', 'ws2', 'chk2', 'ext', 'talk', 'exit', 'look', 'end']}
    stage = 'open'
    for s in sl:
        i = s['id']
        if i == 'title': stage = 'open'
        elif i == 'check': stage = 'sneak'
        elif i.startswith('warm'): stage = 'warm'
        elif i.startswith('explore'): stage = 'explore'
        elif stage == 'explore': stage = 'mini'
        if i == 'break': stage = 'break'
        elif stage == 'break': stage = 'ws1'
        if i == 'ws1ans': stage = 'chk1'
        elif stage == 'chk1': stage = 'teach'
        if i == 'ws2': stage = 'ws2'
        if i == 'ws2ans': stage = 'chk2'
        if i in ('stretch', 'challenge', 'chdiag', 'chwalk'): stage = 'ext'
        if i == 'talk': stage = 'talk'
        if i == 'exit': stage = 'exit'
        if i == 'reflect': stage = 'look'
        if i == 'end': stage = 'end'
        b[stage].append(s)
    return b

def wb_questions(wb):
    """core questions from the workbook HTML: page, stem words, sub-part words, sub-part count"""
    page, qs, cur = 1, [], None
    for e in wb:
        if 'class="brk"' in e: page = 2
        m = re.search(r'<span class="qn">(\w+)</span><span class="qt">(.*)$', e, re.S)
        if 'class="p q' in e and m:
            cur = dict(num=m.group(1), page=page, stem=nw(strip(m.group(2))), sub=0, subw=0, cells=0)
            qs.append(cur)
        elif cur is not None and 'class="p sub' in e:
            m2 = re.search(r'<span class="sl">[^<]*</span>(.*)$', e, re.S)
            cur['sub'] += 1; cur['subw'] += nw(strip(m2.group(1) if m2 else e))
        elif cur is not None and 'class="tb"' in e:
            cur['cells'] += e.count('<td')
    return qs

# --------------------------------------------------------------------------------------------
def row(part, scripted, c, flag_extra=''):
    """c: dict of seconds: speak, wait, act, trans, rec"""
    need = sum(c.values()) / 60.0
    return dict(part=part, scripted=scripted, need=need, diff=need - scripted, c={k: v / 60.0 for k, v in c.items()}, flag=flag(need - scripted), note=flag_extra)

def flag(d):
    if d >= 2: return 'OVER'
    if d > -1: return 'TIGHT'
    if d > -3: return 'OK'
    return 'LOOSE'

FIXPAR = dict(sneak_act=150, sneak_hold=1, sneak_other=False, warm_nq=3, warm_game=90, warm_asks=False, explore_debrief=2,
              mini_tries=1, mini_asks=3, break_act=150, teach_tries=False, teach_asks=3, pair_talk=60, pairmove=0, talk2=False,
              look_first='Turn to page 3, to the box called Looking back. Write, tick or pass. Two minutes, no talking.')

def lesson_model(x, sl, sc, fix=False, over=None):
    S = dict(SCEN[sc])
    F = None
    if fix:
        F = dict(FIXPAR); F.update(over or {})
        S['pairmove'] = F['pairmove']; S['talk2'] = F['talk2']; S['other'] = F['sneak_other']
    n = x['lesson']['n']
    dk, sp, gp, rec = x['deck'], x['script'], x['gaps'], x['rec']
    B = bucket(sl)
    if F and F.get('drop'):
        for k in B: B[k] = [z for z in B[k] if z['id'] not in F['drop']]
    slide = S['slide']
    rows = []
    cue = lambda i: spk(nw(rec[i]))
    def asks_sec(slides, cap=None):
        if not S['asks']: return 0
        a = [q for s in slides for q in s['asks']]
        if cap is not None: a = a[:cap]
        return sum(rd(nw(q)) + ASK for q in a)
    G = lambda k, d: (F.get(k, d) if F else d)

    # 0 Opening
    c = dict(speak=spk(nw(' '.join(sp['hook']))) + spk(nw(dk['today'])) + spk(nw(REC_NOTICE)), wait=0, act=0, trans=GROUP * S['greet'], rec=cue(0))
    rows.append(row('Opening', 1, c))

    # 1 Sneak-peek
    chk = gp['check']
    qs_words = sum(nw(k['q']) for k in chk)
    ans_words = sum(nw(k['a']) for k in chk) + nw(gp['why'])
    holds = G('sneak_hold', 2)
    c = dict(speak=spk(nw(SNEAK_SAY.format(idea=gp['idea']))) + rd(qs_words) + spk(ans_words),
             wait=holds * HOLD + (ASK if S['other'] else 0), act=G('sneak_act', 180), trans=slide * max(1, len(B['sneak'])), rec=cue(1))
    rows.append(row('Sneak-peek puzzles', 3, c))

    # 2 Warm-up
    wq = dk['warmQs'][:G('warm_nq', 99)]
    wasks = asks_sec(B['warm']) if not (F and not F['warm_asks']) else 0
    c = dict(speak=spk(nw(' '.join(sp['warmIntro']))) + sum(rd(nw(q[0])) + spk(nw(q[1])) for q in wq),
             wait=HOLD + len(wq) * ASK + wasks, act=G('warm_game', GAME_ACTIVITY * 60), trans=slide * len(B['warm']), rec=cue(2))
    rows.append(row('Warm-up game + quick questions', 4, c))

    # 3 Explore
    setup_words = sum(nw(s) for s in dk['expSetup'])
    eaq = dk['expAsk'][:G('explore_debrief', 99)]
    hands = (F.get('explore_hands') if F and F.get('explore_hands') else EXPLORE_HANDS[n])
    c = dict(speak=spk(nw(' '.join(sp['predict']))) + rd(setup_words) + spk(nw(EXPLORE_TALK)) + 10 + sum(rd(nw(a[0])) + spk(nw(a[1])) for a in eaq),
             wait=HOLD + len(eaq) * ASK, act=hands * 60, trans=slide * len(B['explore']) + 2 * S['move'], rec=cue(3))
    rows.append(row('Explore (pairs, objects)', 10, c))

    # 4 Mini-lesson
    think_words = nw(' '.join(sp['think'])) - G('think_cut', 0)
    key_words = nw(dk['keyHead']) + nw(dk['keyBig']) + 4
    we = [s for s in B['mini'] if s['id'].startswith('we')]
    tries = [s for s in B['mini'] if s['id'].startswith('try')]
    teachs = [s for s in B['mini'] if not s['id'].startswith(('we', 'try', 'key'))]
    extra_we = max(0, len(we) - len(sp['think'])) / max(1, len(we))
    narr = sum(0.6 * s['words'] for s in teachs) + sum(0.6 * s['words'] for s in we) * extra_we
    keep_tries = tries if not F else tries[-F['mini_tries']:] if F['mini_tries'] else []
    keep_tries = keep_tries if S['opt'] else []
    shown = [s for s in B['mini'] if not s['id'].startswith('try')] + keep_tries
    trysec = sum(rd(0.55 * s['words']) + 60 + HOLD + 15 for s in keep_tries)
    c = dict(speak=spk(think_words + key_words + narr), wait=15 + asks_sec(shown, G('mini_asks', None)) + trysec, act=0,
             trans=slide * len(shown), rec=cue(4))
    rows.append(row('Mini-lesson (%d slides)' % len(shown), 12, c))

    # 5 Brain break
    c = dict(speak=spk(nw(dk['brk'])), wait=0 if F else asks_sec(B['break']), act=G('break_act', BREAK_ACTIVITY * 60), trans=slide + 20, rec=cue(5))
    rows.append(row('Brain break', 4, c))

    # 6 Worksheet (sub-blocks)
    q = wb_questions(x['wb'])
    items = (F.get('items') if F and F.get('items') else ITEMS[n])
    p1 = [i for i in items if i[2] == 1]; p2 = [i for i in items if i[2] == 2]
    p1_min = sum(i[1] for i in p1); p2_prio = sum(i[1] for i in p2 if i[3]); p2_all = sum(i[1] for i in p2)
    qwords, stems = {}, {}
    for qq in q:
        qwords[qq['page']] = qwords.get(qq['page'], 0) + qq['stem'] + qq['subw']
        stems[qq['page']] = stems.get(qq['page'], 0) + qq['stem']
    frac1 = 1.0 if not (F and F.get('items')) else len(p1) / max(1, len([i for i in ITEMS[n] if i[2] == 1]))
    read1 = (rd(qwords.get(1, 0)) if sc != 'BEST' else rd(stems.get(1, 0))) * frac1
    read2 = (rd(qwords.get(2, 0) * (p2_prio / max(1e-9, sum(i[1] for i in ITEMS[n] if i[2] == 2)))) if sc != 'BEST' else rd(stems.get(2, 0) * (p2_prio / max(1e-9, sum(i[1] for i in ITEMS[n] if i[2] == 2)))))
    pre = [s for s in B['ws1'] if s['id'] != 'ws1']        # e.g. L6 teachfan before page 1
    moves = 2 * S['move']
    a = dict(speak=spk(nw(WS_SAY)) + 2 * spk(nw(INVITE)) + read1 + sum(spk(0.6 * s['words']) for s in pre), wait=asks_sec(B['ws1']) + asks_sec(pre),
             act=p1_min * 60, trans=START_WS + moves + slide * (1 + len(pre)), rec=cue(6))
    rows.append(row('WS-a  Start + page 1 (pairs)', 16, a))
    chk1 = B['chk1'][0]
    nq1 = len(re.findall(r'\bQ\d', chk1['t'])) if not (F and F.get('items')) else len(p1)
    b = dict(speak=spk(0.9 * chk1['words'] * (nq1 / max(1, len(re.findall(r'\bQ\d', chk1['t']))))), wait=nq1 * ASK + asks_sec(B['chk1'], 0 if F else None), act=0, trans=slide, rec=0)
    rows.append(row('WS-b  Check page 1', 3, b))
    t_speak = t_wait = t_trans = 0
    tasks = 0
    for s in B['teach']:
        if s['id'].startswith('try'):
            if S['opt'] and not (F and not F['teach_tries']):
                t_speak += rd(0.55 * s['words']); t_wait += 60 + HOLD + 15; t_trans += slide
        else:
            t_speak += spk(0.6 * s['words']); t_trans += slide
    t_wait += asks_sec(B['teach'], G('teach_asks', None))
    rows.append(row('WS-c  Teaching before page 2', 5, dict(speak=t_speak, wait=t_wait, act=0, trans=t_trans, rec=0)))
    cap = 'Page 2 is on your own. Aim for the first questions. The rest is a choice for the last few minutes.'
    d_ = dict(speak=spk(nw(cap)) + read2, wait=0, act=p2_prio * 60, trans=slide + 30, rec=0)
    rows.append(row('WS-d  Page 2 solo (priority items)', 18, d_))
    chk2 = B['chk2'][0]
    nq2 = len(re.findall(r'\bQ\d', chk2['t']))
    n1_orig = len([i for i in ITEMS[n] if i[2] == 1]); moved = max(0, n1_orig - len(p1))     # page-1 items checked late
    e_ = dict(speak=spk(0.9 * (chk2['words'] + moved * chk1['words'] / max(1, len(re.findall(r'\bQ\d', chk1['t']))))),
              wait=(nq2 + moved) * ASK + asks_sec(B['chk2'], 0 if F else None), act=0, trans=slide * (1 + (1 if moved else 0)), rec=0)
    rows.append(row('WS-e  Check page 2', 4, e_))

    # 7 Talk
    tk = sp['talk']
    c = dict(speak=spk(nw(tk[0])) + (spk(nw(tk[1])) if S['talk2'] else 0) + spk(nw(sp['talkAns'])),
             wait=10 + 2 * 40 + (ASK if S['talk2'] else 0), act=G('pair_talk', 120), trans=slide + S['pairmove'], rec=cue(7))
    rows.append(row('Talk time', 5, c))

    # 8 Exit
    c = dict(speak=rd(nw(x['lesson']['exit']['q'])) + spk(nw(' '.join(sp['close']))), wait=HOLD, act=EXIT_WRITE[n] * 60, trans=slide, rec=cue(8))
    rows.append(row('Exit ticket + closing', 2 if n == 10 else 3, c))

    # 9 Looking back
    lk = nw(G('look_first', LOOK_SAY[0])) + nw(LOOK_SAY[1].format(reflect=gp['reflect']))
    c = dict(speak=spk(lk), wait=0, act=120, trans=slide + 15, rec=cue(9))
    rows.append(row('Looking back', 2, c))

    # 10 Lesson 10 only: certificates 89-90 (slide 'end', not a guide segment)
    if n == 10:
        kids = GROUP if not F else F.get('cert_kids', GROUP)
        if F and F.get('cert_whole_group'):
            c = dict(speak=spk(40), wait=3 * 20 + 20, act=0, trans=slide, rec=spk(nw(R_CLOSE)))
        else:
            c = dict(speak=kids * (rd(nw('Name one puzzle you enjoyed and one way in you will use again.')) / 2 + 8), wait=kids * 15, act=0,
                     trans=slide + kids * 5, rec=spk(nw(R_CLOSE)))
        rows.append(row('Certificates + last stamp (slide "end")', 1, c))

    info = dict(p1_min=p1_min, p2_prio=p2_prio, p2_all=p2_all, items=items, nslides=len(sl), think_words=think_words,
                say_words=think_words + nw(' '.join(sp['hook'])) + nw(' '.join(sp['warmIntro'])) + nw(' '.join(sp['predict'])) + nw(' '.join(sp['talk'])) + nw(' '.join(sp['close'])),
                n_core=len(q), n_sub=sum(z['sub'] for z in q), wb_words=sum(z['stem'] + z['subw'] for z in q))
    return rows, info


P_, C_ = True, False
def _mv(n, labels, new=None):
    """items for lesson n with the given page-1 labels moved to the solo block (schedule change only)"""
    out = []
    for lab, m, pg, pr in ITEMS[n]:
        if lab in labels: pg, pr = 2, True
        if new and lab in new: m = new[lab]
        out.append((lab, m, pg, pr))
    return out
FIX_OVER = {   # per-lesson overrides of FIXPAR (what each fix assumes; see the report, section 6)
 1: dict(mini_asks=2, teach_asks=2),
 2: dict(items=_mv(2, ['Q3']), mini_tries=0, mini_asks=2),
 3: dict(items=_mv(3, ['Q3']), drop=['teachchain'], mini_tries=0, mini_asks=2, teach_asks=2),
 6: dict(items=_mv(6, [], {'Q1': 4.5})),
 7: dict(items=_mv(7, ['Q3'], {'Q1': 4.0}), mini_tries=0, drop=['we3'], think_cut=50),
 10: dict(items=[i for i in _mv(10, ['Q3']) if i[0] != 'Q1'] + [('Q1a', 3.0, 1, True)], explore_hands=6.0, cert_whole_group=True),
}

def ceil_half(v):
    return math.ceil(v * 2 - 0.3) / 2.0       # next half minute (a 0.15 min overshoot is tolerated)

def fix_budget(x, sl, n):
    rows, info = lesson_model(x, sl, 'TYPICAL', fix=True, over=FIX_OVER.get(n))
    rows_b, _ = lesson_model(x, sl, 'BEST', fix=True, over=FIX_OVER.get(n))
    rows_s, _ = lesson_model(x, sl, 'SLOW', fix=True, over=FIX_OVER.get(n))
    out = []
    non = [r for r in rows if not r['part'].startswith('WS-')]
    wsr = [r for r in rows if r['part'].startswith('WS-')]
    nb = {r['part']: ceil_half(r['need']) for r in non}
    spent = sum(nb.values())
    ws_left = 90 - spent
    wb = {r['part']: ceil_half(r['need']) for r in wsr}
    d_key = [k for k in wb if k.startswith('WS-d')][0]
    others = sum(v for k, v in wb.items() if k != d_key)
    wb[d_key] = ws_left - others
    need_d = [r for r in wsr if r['part'].startswith('WS-d')][0]['need']
    return rows, rows_b, rows_s, nb, wb, ws_left, wb[d_key] - need_d, info

R_CLOSE = 'Recording: well done for finishing the lesson! Show your journal and workbook to a grown-up and tell them one thing you found out.'

def totals(rows):
    ws = [r for r in rows if r['part'].startswith('WS-')]
    non = [r for r in rows if not r['part'].startswith('WS-')]
    ws_need = sum(r['need'] for r in ws); ws_scr = sum(r['scripted'] for r in ws)
    non_need = sum(r['need'] for r in non)
    return dict(ws_need=ws_need, ws_scr=ws_scr, non_need=non_need, A=non_need + ws_need, B=non_need + ws_scr,
                left=90 - non_need, spare=90 - non_need - ws_need)

def child_items(items, w1, w2):
    """whole items completed in order for LOW / MID / HIGH within page windows (minutes)"""
    res = {}
    for name, f in (('LOW', LOWF), ('MID', 1.0), ('HIGH', HIGHF)):
        done1 = done2p = done2c = 0; t = 0
        for it in [i for i in items if i[2] == 1]:
            t += it[1] * f
            if t <= w1 + 1e-9: done1 += 1
            else: break
        t = 0
        for it in [i for i in items if i[2] == 2 and i[3]]:
            t += it[1] * f
            if t <= w2 + 1e-9: done2p += 1
            else: break
        else:
            for it in [i for i in items if i[2] == 2 and not i[3]]:
                t += it[1] * f
                if t <= w2 + 1e-9: done2c += 1
                else: break
        res[name] = (done1, done2p, done2c)
    return res

def main():
    data = load()
    allres = {}
    for x in data:
        n = x['lesson']['n']
        sl = parse_slides(n)
        allres[n] = dict(title=x['lesson']['title'], slides=len(sl), sc={}, info=None)
        for sc in SCEN:
            rows, info = lesson_model(x, sl, sc)
            allres[n]['sc'][sc] = dict(rows=rows, tot=totals(rows))
            allres[n]['info'] = info
    if '--json' in sys.argv:
        print(json.dumps(allres, default=str, indent=1)); return
    f1 = lambda v: '%.1f' % v
    for n in sorted(allres):
        r = allres[n]; info = r['info']
        print('\n### Lesson %d: %s  (%d slides, %d SAY words, %d core workbook questions / %d sub-parts, %d words)\n' % (n, r['title'], r['slides'], info['say_words'], info['n_core'], info['n_sub'], info['wb_words']))
        rows = r['sc']['TYPICAL']['rows']
        print('| Part | Scripted | Speak | Wait | Activity | Transition | REC | **Need** | Diff | Flag | Need range (best-slow) |')
        print('|---|--:|--:|--:|--:|--:|--:|--:|--:|:-:|:-:|')
        for i, rw in enumerate(rows):
            lo = r['sc']['BEST']['rows'][i]['need']; hi = r['sc']['SLOW']['rows'][i]['need']
            c = rw['c']
            print('| %s | %s | %s | %s | %s | %s | %s | **%s** | %+.1f | %s | %s-%s |' % (rw['part'], f1(rw['scripted']), f1(c['speak']), f1(c['wait']), f1(c['act']), f1(c['trans']), f1(c['rec']), f1(rw['need']), rw['diff'], rw['flag'], f1(lo), f1(hi)))
        t = r['sc']['TYPICAL']['tot']
        wsr = [z for z in rows if z['part'].startswith('WS-')]
        wsn = sum(z['need'] for z in wsr)
        print('| **Worksheet total (a-e)** | 46.0 | | | | | | **%s** | %+.1f | %s | |' % (f1(wsn), wsn - 46, flag(wsn - 46)))
        print()
        print('Total needed (worksheet at priority items only): best %s / typical %s / slow %s min. As scripted (worksheet runs its full 46): best %s / typical %s / slow %s. Worksheet time left after the other parts take what they need (typical): %s of 46 scripted; spare after priority items: %s.' % (
            f1(r['sc']['BEST']['tot']['A']), f1(t['A']), f1(r['sc']['SLOW']['tot']['A']),
            f1(r['sc']['BEST']['tot']['B']), f1(t['B']), f1(r['sc']['SLOW']['tot']['B']), f1(t['left']), f1(t['spare'])))
    print('\n### Summary\n')
    print('| L | Title | Slides | Best A | Typ A | Slow A | Typ B (ws held) | Slow B | ws left (typ) | Verdict |')
    print('|--:|---|--:|--:|--:|--:|--:|--:|--:|---|')
    for n in sorted(allres):
        r = allres[n]; t = r['sc']['TYPICAL']['tot']
        print('| %d | %s | %d | %s | %s | %s | %s | %s | %s | %s |' % (n, r['title'], r['slides'], f1(r['sc']['BEST']['tot']['A']), f1(t['A']), f1(r['sc']['SLOW']['tot']['A']),
              f1(t['B']), f1(r['sc']['SLOW']['tot']['B']), f1(t['left']), 'does not fit' if t['spare'] < 0 else ('fits only by cutting worksheet to %s min' % f1(t['left']) if t['left'] < 40 else 'fits')))
    print('\n### Workbook items finished (LOW/MID/HIGH child) with windows as scripted, and squeezed by what the other parts really need (tutor skips the optional slides)\n')
    print('| L | Page-1 items | Page-1 window | LOW p1 | MID p1 | HIGH p1 | Page-2 window (scripted / squeezed) | LOW p2 prio+choice | MID | HIGH |')
    print('|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|')
    for n in sorted(allres):
        r = allres[n]; info = r['info']; t = r['sc']['LEAN']['tot']
        w1 = 16 - 2 - 3 - (0 if n != 6 else 2)
        w2s = 18 - 1.5
        w2q = max(0, w2s - max(0, 46 - t['left']))
        a = child_items(info['items'], w1, w2s); b = child_items(info['items'], w1, w2q)
        n1 = sum(1 for i in info['items'] if i[2] == 1); np2 = sum(1 for i in info['items'] if i[2] == 2 and i[3]); nc = sum(1 for i in info['items'] if i[2] == 2 and not i[3])
        fmt = lambda k, d: '%d/%d' % (d[k][0], n1)
        fm2 = lambda k, d: '%d/%d+%d/%d' % (d[k][1], np2, d[k][2], nc)
        print('| %d | %d (%.1f min) | %.1f | %s | %s | %s | %.1f / %.1f | %s -> %s | %s -> %s | %s -> %s |' % (
            n, n1, info['p1_min'], w1, fmt('LOW', a), fmt('MID', a), fmt('HIGH', a), w2s, w2q,
            fm2('LOW', a), fm2('LOW', b), fm2('MID', a), fm2('MID', b), fm2('HIGH', a), fm2('HIGH', b)))

    print('\n### Where the time goes (TYPICAL tutor, whole lesson, minutes) and effect of skipping optional items\n')
    print('| L | Speak | Wait | Activity | Transition | REC | Total (worksheet at priority) | Lean script (skip optional + note ASKs) | Slide changes (n x 25 s) | Breakout moves (4 x 90 s + 60 s pair talk) |')
    print('|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|')
    tot = {k: 0 for k in ('speak', 'wait', 'act', 'trans', 'rec')}
    for n in sorted(allres):
        rows = allres[n]['sc']['TYPICAL']['rows']
        c = {k: sum(r['c'][k] for r in rows) for k in tot}
        for k in tot: tot[k] += c[k]
        t = allres[n]['sc']['TYPICAL']['tot']; lean = allres[n]['sc']['LEAN']['tot']
        print('| %d | %s | %s | %s | %s | %s | %s | %s | %d (%.1f min) | 7.0 |' % (n, f1(c['speak']), f1(c['wait']), f1(c['act']), f1(c['trans']), f1(c['rec']), f1(t['A']), f1(lean['A']), allres[n]['slides'] - 4, (allres[n]['slides'] - 4) * 25 / 60.0))
    print('| mean | %s | %s | %s | %s | %s | | | | |' % tuple(f1(tot[k] / 10) for k in ('speak', 'wait', 'act', 'trans', 'rec')))

    print('\n### Proposed budgets after the fixes (TYPICAL tutor)\n')
    for n in sorted(allres):
        x = [z for z in data if z['lesson']['n'] == n][0]
        sl = parse_slides(n)
        rows, rb, rs, nb, wb, ws_left, spare_d, info = fix_budget(x, sl, n)
        old = {r['part']: r['scripted'] for r in rows}
        print('\n**Lesson %d** worksheet window %.1f min (was 46), page-2 spare after priority items %.1f min' % (n, ws_left, spare_d))
        print('| Part | Old | New budget | New clock (min) | Need after fixes (best / typical / slow) |')
        print('|---|--:|--:|--:|--:|')
        clk = 0.0
        for i, r in enumerate(rows):
            bud = nb.get(r['part'], wb.get(r['part']))
            print('| %s | %.1f | %.1f | %.1f-%.1f | %.1f / %.1f / %.1f |' % (r['part'], r['scripted'], bud, clk, clk + bud, rb[i]['need'], r['need'], rs[i]['need']))
            clk += bud
        print('| Sum | 90.0 | %.1f | | typical need %.1f; cushion %.1f |' % (sum(nb.values()) + sum(wb.values()), sum(r['need'] for r in rows), 90 - sum(r['need'] for r in rows)))

if __name__ == '__main__':
    main()
