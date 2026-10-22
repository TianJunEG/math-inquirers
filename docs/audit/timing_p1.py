#!/usr/bin/env python3
"""Lesson timing audit helper, Math Inquirers Level N=1 (P1, ages 6-8).

READ-ONLY on the repo. It reads:
  hp/lessons.js, hp/scripts.js, deck/data.js, hp/gaps.json, hp/qbank.json  (via node)
  split/l1..l10/project/slides/*.html + deck.json                           (slide text, MIN badges, notes)
  hp/Math_Inquirers_P1_Student_Workbook_Designed.pdf                        (via pdftotext, question counts)
  levels/reccues.js                                                         (REC cue lines, via node)
and prints the model tables as markdown on stdout.

  python3 -I docs/audit/timing_p1.py > /tmp/tables.md

Every number below is an ESTIMATE from the stated model, not a stopwatch timing.
The judged inputs (activity minutes, minutes per workbook question) are the dictionaries
EXPLORE_ACT, ITEMS and the break/exit constants, so a reader can change them and re-run.
"""
import json, re, html, subprocess, os, sys, math

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

# ------------------------------------------------------------------ model constants (same for every level)
SPEAK_WPM = 120      # tutor speech incl. natural pauses
READ_WPM = 110       # questions read aloud
WAIT_Q = 30          # s: 10 s think + 20 s to take one or two answers (per question put to the group)
HOLDUP = 30          # s: "hold up papers/boards to the camera" moment
SLIDE = 25           # s per slide change online (20-30)
BREAKOUT = 90        # s to move to OR from breakout rooms / fetch materials (60-120)
WS_START = 120       # s to get started on the worksheet
GREET = 4            # s per child greeting (8 children)
N_CHILD = 8
REC_S = None         # None = use the real word count of each REC cue at SPEAK_WPM (the guide says "under ten seconds")
ACT_MULT = 1.0       # scenario multiplier on child work time (explore, worksheet)
LOW_X, HIGH_X = 1.7, 0.65   # LOW child takes 1.7x MID time per item, HIGH 0.65x

# ------------------------------------------------------------------ judged inputs
# Explore activity, minutes of actual child work for a MIDDLE child (low, mid, high) and the reason.
EXPLORE_ACT = {
 1: (9, 6.5, 4.5, 'make 0-50 strip (cut 2 rows, tape) ~2.5; 12+10 landings marked ~3; list shared numbers ~1'),
 2: (8, 5.5, 4,   'fill ten-frame and record 11 pairs, ~25 s each, plus setting up counters'),
 3: (8, 5.5, 4,   'draw 5 rows, place ~27 counters, write key, read graph aloud (most/fewest/same/how many more)'),
 4: (7, 5, 3.5,   'build 1, 2, 3 triangles with straws (3+2+2 sticks), count, predict and build the 4th, record'),
 5: (7, 5, 3.5,   'two rounds of hide / add / work back / lift cup, swap roles; online the cup trick is done on camera'),
 6: (8, 5.5, 4,   'find the 4 ways to make 20c with 20/10/5 coins, record each, argue "have I got them all"'),
 7: (9, 6, 4.5,   'fold a square corner to corner, cut (scissors), rearrange two triangles into new shapes and name each'),
 8: (8, 5.5, 4,   'lay two string loops, sort buttons by two rules, find the middle; online: find objects at home first'),
 9: (11, 8, 6,    'cut/tape cube strip, estimate and measure pencil, book, shoe, then hand spans and compare with partner'),
 10: (None, None, None, 'see CARDS below'),
}
# L10 puzzle cards: minutes of work for a MIDDLE child per card, LOW, HIGH
CARD_MID = {'Coins': 4.0, 'Patterns': 3.0, 'Logic': 3.5, 'Measuring': 2.5}   # mean 3.25 -> round 1 ~4 for MID; LOW up to 8

# Start-here workbook items: (id, MID minutes, optional?, page). One line of reasoning per lesson in the md.
ITEMS = {
 1: [('Q1', 2.0, 0, 1), ('Q2', 2.5, 0, 1), ('Q3', 2.0, 0, 1), ('Q4', 3.0, 0, 2), ('Q5', 4.0, 0, 2)],
 2: [('Q1', 1.0, 0, 1), ('Q2', 3.0, 0, 1), ('Q3', 2.2, 0, 1), ('Q4', 3.0, 0, 2), ('Q5a', 5.0, 0, 2), ('Q6a', 2.5, 0, 2), ('Q5b+Q6b', 3.0, 1, 2)],
 3: [('Q1', .5, 0, 1), ('Q2', .5, 0, 1), ('Q3', 1.0, 0, 1), ('Q4', .8, 0, 1), ('Q5', 1.5, 0, 1), ('Q6', 1.5, 0, 2), ('Q7', 1.5, 0, 2), ('PartB vote+tally', 3.5, 0, 2), ('Q8', 1.0, 0, 2), ('Q9', 1.5, 0, 2)],
 4: [('Q1', 1.0, 0, 1), ('Q2', 5.0, 0, 1), ('Q3', 5.0, 0, 2), ('Q4 (if time)', 4.0, 1, 2)],
 5: [('Q1', 2.6, 0, 1), ('Q2', 2.5, 0, 1), ('Q3', 4.0, 0, 2), ('Q4', 4.0, 0, 2), ('Q5', 2.5, 0, 2)],
 6: [('Q1', 5.0, 0, 1), ('Q2', 4.0, 0, 1), ('Q3a', 3.0, 0, 2), ('Q4', 2.5, 0, 2), ('Q3b (if time)', 2.0, 1, 2)],
 7: [('Q1', 2.0, 0, 1), ('Q2', 3.5, 0, 1), ('Q3', 1.5, 0, 2), ('Q4', 2.5, 0, 2), ('Q5', 2.0, 0, 2), ('Q6', 1.5, 0, 2)],
 8: [('Q1', 4.0, 0, 1), ('Q2', 4.0, 0, 1), ('Q3', 3.0, 0, 2), ('Q4', 2.5, 0, 2), ('Q5 (if time)', 2.0, 1, 2), ('Q6 (if time)', 2.0, 1, 2)],
 9: [('Q1', 3.0, 0, 1), ('Q2', 7.0, 0, 1), ('Q3', 2.5, 0, 2), ('Q5', 3.0, 0, 2), ('Q6', 3.5, 0, 2), ('Q4 (if time)', 3.0, 1, 2)],
 10: [('Q1', 1.0, 0, 1), ('Q2', 2.0, 0, 1), ('Q3', 2.5, 0, 1), ('Q4', 3.0, 0, 1), ('Q5', 2.5, 0, 2), ('Q6', .8, 0, 2), ('Q7', 1.5, 0, 2), ('Q8', 1.5, 0, 2)],
}
T_ITEM_MID = 5.0     # Think Harder item, middle child (4-6 min); HIGH ~3.5

# Quick-question game (warm-up 2-5): minutes of play incl. instructions given by SAY (judged from the game text)
GAME_MIN = {1: 2.0, 2: 2.0, 3: 2.0, 4: 1.5, 5: 1.5, 6: 2.5, 7: 2.5, 8: 2.5, 9: 2.0, 10: 0.0}   # 10: the game is the 5-question whiteboard round, timed under 'waiting'
# Brain break: movement minutes + water/toilet/regroup online
BREAK_MOVE = {1: 1.0, 2: 1.0, 3: 1.5, 4: 1.5, 5: 1.5, 6: 1.5, 7: 1.5, 8: 1.0, 9: 2.0, 10: 1.0}
BREAK_WATER = 1.5    # min: fetch water / toilet / settle back on camera
# Exit ticket: minutes the children need to write the answer (ticket question judged), per lesson
EXIT_WRITE = {1: 1.5, 2: 2.0, 3: 2.0, 4: 2.0, 5: 2.0, 6: 2.0, 7: 2.0, 8: 2.0, 9: 2.0, 10: 1.5}


def words(s):
    return len(re.findall(r"[A-Za-z0-9¢$'’\-]+", s))


def secs_speak(w):
    return w / SPEAK_WPM * 60


def secs_read(w):
    return w / READ_WPM * 60


# ------------------------------------------------------------------ load data
def load_js():
    js = r"""
const L=require('./hp/lessons.js'),SC=require('./hp/scripts.js'),DD=require('./deck/data.js'),G=require('./hp/gaps.json'),Q=require('./hp/qbank.json');
const R=require('./levels/reccues.js');
const segs=[['0–2 min','Opening'],['2–7 min','Warm-up game and quick questions'],['7–10 min','Sneak-peek puzzles (3 minutes)'],['10–25 min','Explore (in pairs, with objects)'],['25–35 min','Mini-lesson (you teach, they join in)'],['35–40 min','Brain break'],['40–72 min','Worksheet (pairs, then alone, then check together)'],['72–80 min','Talk time'],['80–88 min','Exit ticket and closing'],['88–90 min','Look-back (2 minutes)']];
const rec=segs.map(s=>R.cue(s[1],s[0],null).say);
process.stdout.write(JSON.stringify({L:L.lessons,SC,DD,G,Q,rec,RULES:R.RULES}));
"""
    out = subprocess.run(['node', '-e', js], cwd=ROOT, capture_output=True, text=True, check=True).stdout
    return json.loads(out)


def vis_text(h):
    h = re.sub(r'<aside>.*?</aside>', '', h, flags=re.S)
    h = re.sub(r'<(script|style)[^>]*>.*?</\1>', '', h, flags=re.S)
    h = re.sub(r'<br\s*/?>|</p>|</div>|</h\d>|</li>', '\n', h)
    h = re.sub(r'<[^>]+>', '', h)
    t = ' '.join(html.unescape(h).split())
    return t.replace('Math Inquirers Holiday Program • Notice it. Test it. Explain why.', '').strip()


def load_slides(n):
    base = f'{ROOT}/split/l{n}/project/'
    deck = json.load(open(base + 'deck.json'))
    out = []
    for sid in deck['order']:
        h = open(base + f'slides/{sid}.html').read()
        m = re.search(r'letter-spacing:2px[^>]*>(\d+)\s*[–-]\s*(\d+)\s*MIN<', h)
        a = re.search(r'<aside>(.*?)</aside>', h, flags=re.S)
        out.append(dict(id=sid, s=int(m.group(1)) if m else None, e=int(m.group(2)) if m else None,
                        vis=vis_text(h), notes=html.unescape(a.group(1)) if a else ''))
    return out


def assign_parts(slides):
    """Assign each slide in deck order to a lesson part. Untimed slides inside the worksheet run
    (before the page-2 check slide) belong to the worksheet; untimed slides after it are 'choice' slides."""
    ws2ans = max(i for i, s in enumerate(slides) if s['id'].endswith('ws2ans'))
    part = None
    for i, s in enumerate(slides):
        sid, a, b = s['id'], s['s'], s['e']
        if sid in ('cover', 'routine', 'rules') or sid.endswith('title'):
            p = 'open'
        elif sid.endswith('warmcheck'):
            p = 'sneak'
        elif re.search(r'warm[12]$', sid):
            p = 'warm'
        elif sid.endswith('break'):
            p = 'break'
        elif sid.endswith('talk'):
            p = 'talk'
        elif sid.endswith('exit'):
            p = 'exit'
        elif sid.endswith('reflect'):
            p = 'look'
        elif sid == 'end':
            p = 'end'
        elif a is not None and a >= 10 and b <= 25:
            p = 'explore'
        elif a is not None and a >= 25 and b <= 35:
            p = 'mini'
        elif a is not None and a >= 40 and b <= 72:
            p = 'work'
        else:  # untimed
            if part == 'mini' and i < ws2ans:   # none observed, kept for safety
                p = 'mini'
            elif part == 'work' and i < ws2ans:
                p = 'work'
            else:
                p = 'choice'
        s['part'] = p
        if p not in ('choice',):
            part = p if p != 'end' else part
        if sid.endswith('ws2ans'):
            part = 'after'
    return slides


def kind(sid):
    m = re.search(r'-(\w+)$', sid)
    k = m.group(1) if m else sid
    return k


def group_qs(vis):
    return vis.count('?')


# ------------------------------------------------------------------ model
FIX = False   # when True, apply the universal fixes (REC cues <= 10 s, 3 quick questions, one camera moment in sneak-peek)


def model(n, D):
    L = D['L'][n - 1]; SC = D['SC'][str(n)]; DDn = D['DD'][str(n)]; G = D['G'][str(n)]
    slides = assign_parts(load_slides(n))
    byp = {}
    for s in slides:
        byp.setdefault(s['part'], []).append(s)
    rec = [words(x) for x in D['rec']]
    recs = [secs_speak(w) if REC_S is None else REC_S for w in rec]   # seconds, 10 cues
    if FIX: recs = [min(r, 10) for r in recs]
    say = lambda lines: sum(words(re.sub(r'^[“"]|[”"]$', '', x)) for x in lines)
    parts = []   # (name, scripted, comps dict minutes)

    # 1 OPENING --------------------------------------------------------------
    c = {}
    c['REC cue'] = recs[0] / 60
    sw = say(SC['hook']) + words(D['RULES']['privacy'][4]) + 0   # hook + recording notice
    rw = words(DDn['today']) + 5
    extra_slides = len(byp['open'])
    c['speaking'] = (secs_speak(sw) + secs_read(rw)) / 60
    c['waiting'] = (N_CHILD * GREET) / 60
    if n == 1:
        rr = [s for s in byp['open'] if s['id'] in ('routine', 'rules')]
        c['speaking'] += secs_read(sum(words(s['vis']) for s in rr) * 0.8) / 60 + secs_speak(60) / 60  # read routine+rules, explain
    c['transitions'] = extra_slides * SLIDE / 60
    c['activity'] = 0
    parts.append(('Opening', 2, c, extra_slides))

    # 2 WARM-UP ---------------------------------------------------------------
    c = {}
    c['REC cue'] = recs[1] / 60
    wq = DDn['warmQs'][:3] if FIX else DDn['warmQs']
    game_words = say(SC['warmIntro']) + words(DDn['warmGame'])
    qread = sum(words(q[0]) for q in wq)
    c['speaking'] = (secs_speak(game_words) + secs_read(qread) + len(wq) * 3) / 60   # +3 s per answer reveal read
    if n == 10:   # whiteboard round (slide warm1): 5 questions, everyone writes at once (no 20 s answer-taking)
        c['speaking'] += (5 * 9) / 60
        c['waiting'] = (5 * 13 + len(wq) * WAIT_Q) / 60
    else:
        c['waiting'] = len(wq) * WAIT_Q / 60
    c['activity'] = GAME_MIN[n]
    c['transitions'] = len(byp['warm']) * SLIDE / 60
    parts.append(('Warm-up game + quick questions', 5, c, len(byp['warm'])))

    # 3 SNEAK-PEEK ------------------------------------------------------------
    c = {}
    c['REC cue'] = recs[2] / 60
    fixed_say = ['These two are sneak-peek puzzles. They are ideas we have not learnt yet, so a guess is a great start. I do not know is welcome too. Nobody is marked.',
                 'The first one you can try with counters or a drawing. Write or draw on your own paper. When I say, show it to me only (online: hold your paper up to the camera for me).']
    qs = G['check']
    qread = sum(words(x['q']) for x in qs)
    ans_w = sum(words(x['short']) + 2 for x in qs) + 12   # read answer + "lots of us had a different idea"
    if FIX: fixed_say = ['Two sneak-peek puzzles: ideas we have not learnt yet. A guess is a great start, and I do not know is welcome. Nobody is marked.']
    c['speaking'] = (secs_speak(say(fixed_say) + ans_w) + secs_read(qread)) / 60
    c['waiting'] = ((1 if FIX else 2) * HOLDUP) / 60
    c['activity'] = 2.0       # scripted: "about a minute for each question"; Q2 (think) judged fair for MID if only a guess is expected
    c['transitions'] = len(byp['sneak']) * SLIDE / 60
    parts.append(('Sneak-peek puzzles', 3, c, len(byp['sneak'])))

    # 4 EXPLORE ----------------------------------------------------------------
    c = {}
    c['REC cue'] = recs[3] / 60
    setup_w = sum(words(x) for x in DDn['expSetup'])
    ask = DDn['expAsk']
    ask_read = sum(words(x[0]) for x in ask)
    eslides = byp['explore']
    if n != 10:
        spw = say(SC['predict']) + setup_w + 15 + 20      # + "talk to your partner" + 20 words Go-further what-if
        c['speaking'] = (secs_speak(spw) + secs_read(ask_read) + 10) / 60   # + "pencils down" 10 s
        c['waiting'] = (HOLDUP + 30 + len(ask) * (WAIT_Q + 20)) / 60       # predict vote + write prediction 30 s, debrief 50 s each
        c['transitions'] = (len(eslides) * SLIDE + 2 * BREAKOUT) / 60
        c['activity'] = EXPLORE_ACT[n][1] * ACT_MULT
    else:
        cards = L['cards']
        cardw = sum(words(x['text']) for x in cards)
        spw = say(SC['predict']) + setup_w + 20
        c['speaking'] = (secs_speak(spw) + secs_read(cardw) + secs_read(ask_read) + 10) / 60
        # online: one card per breakout room, then swap, then four pair reports of 30 s
        c['waiting'] = (HOLDUP + len(ask) * (WAIT_Q + 20) + 4 * 30) / 60
        c['transitions'] = (len(eslides) * SLIDE + 2 * BREAKOUT + 60) / 60   # +60 s to swap cards between rooms
        c['activity'] = (4.5 + 3.5) * ACT_MULT    # round 1 (hardest card 4 min, MID) + round 2 (3.5); scripted 10 + 4
    parts.append(('Explore (pairs, objects)', 15, c, len(eslides)))

    # 5 MINI-LESSON ---------------------------------------------------------------
    c = {}
    c['REC cue'] = recs[4] / 60
    ms = byp['mini']
    vis_w = 0; gq = 0; tries = 0; nsl = len(ms)
    for s in ms:
        k = kind(s['id'])
        if k == 'key':
            continue
        vis_w += words(s['vis'])
        if k.startswith('try'):
            tries += 1
        else:
            gq += group_qs(s['vis'])
    key_say = ['The key idea today is: ' + DDn['keyHead'] + '. ' + DDn['keyBig'] + ' Say it with me.']
    think_w = say(SC['think']) + say(key_say)
    c['speaking'] = (secs_speak(think_w) + secs_read(0.7 * vis_w)) / 60 + 20 / 60
    c['waiting'] = (gq * WAIT_Q + tries * (45 + 20)) / 60
    c['transitions'] = nsl * SLIDE / 60
    c['activity'] = 0
    parts.append(('Mini-lesson', 10, c, nsl))

    # 6 BRAIN BREAK ---------------------------------------------------------------
    c = {}
    c['REC cue'] = recs[5] / 60
    c['speaking'] = secs_speak(words(DDn['brk']) + 25) / 60
    c['waiting'] = BREAK_WATER
    c['activity'] = BREAK_MOVE[n]
    c['transitions'] = SLIDE / 60 + 0.5   # slide + settle back
    parts.append(('Brain break', 5, c, len(byp['break'])))

    # 7 WORKSHEET -------------------------------------------------------------------
    c = {}
    c['REC cue'] = recs[6] / 60
    ws = byp['work']
    if FIX and n == 10:
        ws = [x for x in ws if kind(x['id']) not in ('teachgraph', 'teachtri', 'teachlen')]
    items = ITEMS[n]
    qtxt = WBQ[str(n)]['S']
    q12 = sum(words(q[1]) for q in qtxt[:2])
    teach = [s for s in ws if kind(s['id']) not in ('ws1', 'ws2', 'ws1ans', 'ws2ans')]
    check = [s for s in ws if kind(s['id']) in ('ws1ans', 'ws2ans')]
    tw = 0; tq = 0
    for s in teach:
        tw += secs_read(0.7 * words(s['vis'])) + secs_speak(0.4 * words(s['notes']))
        tq += group_qs(s['vis'])
    ncheck = sum(len(re.findall(r'\bQ\d+[a-z]?\b', s['vis'])) for s in check)
    pairs_say = 35 + 25 + 20   # pairs-first SAY, "after question 3" line, title + instructions
    c['speaking'] = (secs_speak(pairs_say) + secs_read(q12 + sum(words(s['vis']) for s in ws if kind(s['id']) in ('ws1', 'ws2')) * 0.5) + tw) / 60 + 15 / 60
    c['waiting'] = (WS_START + tq * WAIT_Q + ncheck * 20) / 60 + 1.0   # +1 min stand-up stretch
    work_mid = sum(m for _, m, o, _p in items if not o)
    c['activity'] = work_mid * ACT_MULT
    c['transitions'] = (len(ws) * SLIDE + BREAKOUT) / 60       # slides + one return from breakout rooms
    parts.append(('Worksheet (Start here)', 32, c, len(ws)))

    # 8 TALK TIME -------------------------------------------------------------------
    c = {}
    c['REC cue'] = recs[7] / 60
    if n != 10:
        c['speaking'] = (secs_speak(say(SC['talk']) + 12) + secs_read(words(L['share']))) / 60
        c['waiting'] = (3 * 45) / 60     # three volunteers, ~45 s each incl. "how do you know?"
        c['activity'] = 2.0              # pairs talk, scripted 2 min
        c['transitions'] = (SLIDE + 2 * 60) / 60   # slide + breakout in/out (60 s each)
    else:
        c['speaking'] = (secs_speak(say(SC['talk']) + 25) + secs_read(words(L['share']))) / 60
        c['waiting'] = (3 * 45) / 60
        c['activity'] = 6.0  # pairs write a puzzle + answer (3.5) and swap and solve (2.5); the scripted 2-min pair talk is this swap
        c['transitions'] = (SLIDE + 2 * 60) / 60
    parts.append(('Talk time', 8, c, len(byp['talk'])))

    # 9 EXIT -------------------------------------------------------------------------
    c = {}
    c['REC cue'] = recs[8] / 60
    qw = words(L['exit']['q'])
    c['speaking'] = (secs_read(qw) + secs_speak(say(SC['close']) + 25 + 10)) / 60    # + "no talking, no helping" + show answer
    c['waiting'] = (N_CHILD * 8) / 60 + HOLDUP / 60    # each child shows slip to camera ~8 s; answer reveal
    c['activity'] = EXIT_WRITE[n] + 0.5               # write + stamp/journal (online stamp is done later)
    c['transitions'] = SLIDE / 60 * (len(byp['exit']) + len(byp.get('end', []))) + 0.3
    if n == 10:
        cert = secs_speak(words('You are real inquirers now. Here is your certificate and your completed inquiry journal.') + 30) + N_CHILD * (15 + 12)
        c['speaking'] += cert / 60 - N_CHILD * 12 / 60 * 0
        c['waiting'] += 0
        c['activity'] += 0
        parts.append(('Exit ticket + closing (+ certificates)', 8, c, len(byp['exit']) + len(byp.get('end', []))))
    else:
        parts.append(('Exit ticket + closing', 8, c, len(byp['exit'])))

    # 10 LOOK-BACK ------------------------------------------------------------------------
    c = {}
    c['REC cue'] = recs[9] / 60
    lb = ['Turn to the Choose and look-back page and look at the box called Look-back. Tick what was hard for you and what helped you. Write or draw one thing you did well. You can pass. If you are still stuck, tick the box and I will come and help you. I will not say your name to the group. This is not shown to the group.',
          'Thank you. Drawing it, using counters, asking a friend or asking for help: those are all good ways to get unstuck.']
    c['speaking'] = (secs_speak(say(lb)) + 20) / 60     # + goodbye
    c['waiting'] = 0
    c['activity'] = 1.0                                  # children tick / draw
    c['transitions'] = SLIDE / 60
    parts.append(('Look-back', 2, c, len(byp['look'])))
    return parts, dict(slides=slides, byp=byp, rec_words=rec)


WBQ = None


def wb_questions():
    """Parse the designed workbook PDF text into per-lesson question lists (cached json)."""
    txt = subprocess.run(['pdftotext', '-layout', f'{ROOT}/hp/Math_Inquirers_P1_Student_Workbook_Designed.pdf', '-'],
                         capture_output=True, text=True, check=True).stdout
    lesson = None; sec = None; out = {}; cur = None
    for ln in txt.split('\n'):
        m = re.match(r'\s*Lesson (\d+)\s{2,}(\S.*?)\s{2,}Start here', ln)
        if m:
            lesson = int(m.group(1)); sec = 'S'; out[lesson] = {'S': [], 'T': [], 'C': []}; cur = None; continue
        if re.match(r'\s*Lesson \d+ • .*Choose, then look back', ln): sec = 'I'; cur = None; continue
        if re.match(r'\s*Lesson \d+\s{2,}[A-Z0-9 ]+$', ln) and sec in ('I', 'S'): sec = 'T'; cur = None; continue
        if re.match(r'\s*Lesson \d+ • [A-Z0-9 ]+$', ln) and sec == 'T': sec = 'C'; cur = None; continue
        if lesson is None or sec not in ('S', 'T', 'C'): continue
        if 'Cut-outs' in ln: lesson = None; continue
        m = re.match(r'\s*No\.(\w+)', ln)
        if m:
            cur = [m.group(1), []]; out[lesson][sec].append(cur); continue
        if 'Math Inquirers Holiday' in ln or not ln.strip(): continue
        if cur: cur[1].append(ln.strip())
    res = {str(n): {k: [(q[0], ' '.join(q[1])) for q in v[k]] for k in v} for n, v in out.items()}
    return res


def flag(scripted, need):
    d = scripted - need
    if d <= -2: return 'OVER'
    if d < 1: return 'TIGHT'
    if d < 3: return 'OK'
    return 'LOOSE'


def fmt(x): return f'{x:.1f}'


def child_completion(n):
    """Required Start-here items finished by a LOW / MID / HIGH child in the scripted independent-work time."""
    L = {}
    slides = assign_parts(load_slides(n))
    ws = {kind(s['id']): s for s in slides if s['part'] == 'work'}
    w1 = ws['ws1']; w2 = ws['ws2']
    teach_before = w1['s'] - 40
    # page-1 independent work minutes: slide length minus 3 (start-up + reading Q1/Q2) when the slide starts at 40
    W1 = (w1['e'] - w1['s']) - (3 if w1['s'] == 40 else 1)
    W2 = (w2['e'] - w2['s']) - 1     # 1 min to settle and re-read instructions
    out = {}
    for lab, x in (('LOW', LOW_X), ('MID', 1.0), ('HIGH', HIGH_X)):
        done = 0; tot = 0; spare = 0; t1 = 0; t2 = 0
        for pg, W in ((1, W1), (2, W2)):
            t = 0
            for iid, m, opt, p in ITEMS[n]:
                if p != pg or opt: continue
                tot += 1
                if t + m * x <= W + 0.01:
                    t += m * x; done += 1
                else:
                    break      # a child works in order and stops where the page time runs out
            if pg == 1: t1 = t
            else: t2 = t
            spare += W - t
        # optional / Think-harder items a child could add with the spare time
        opts = [m for _, m, o, _p in ITEMS[n] if o]
        extra = 0; sp = spare
        for m in opts:
            if sp >= m * x: sp -= m * x; extra += 1
        t_item = T_ITEM_MID * (x if x != LOW_X else 1.2)   # LOW child rarely chooses T; shown for scale only
        tcount = int(sp // t_item) if lab == 'HIGH' else int(sp // (T_ITEM_MID * x)) if lab == 'MID' else 0
        out[lab] = dict(done=done, tot=tot, spare=spare, opt=extra, T=tcount, W1=W1, W2=W2, t1=t1, t2=t2)
    return out



# ------------------------------------------------------------------ proposed fixes (lesson-specific deltas on top of FIX=True)
PART_NAMES = ['Opening', 'Warm-up', 'Sneak-peek', 'Explore', 'Mini-lesson', 'Brain break', 'Worksheet', 'Talk time', 'Exit ticket', 'Look-back']
# (part index, component, delta minutes, what the fix is)
LESSON_DELTAS = {
 1: [(0, 'speaking', -0.9, 'show the routine slide for 30 s and name the four phases instead of reading the table'),
     (0, 'transitions', -0.4, 'skip the cover slide (title slide says the same)'),
     (3, 'activity', -2.5, 'parents cut and tape the 0-50 number strip BEFORE the lesson (add to the materials mail)')],
 2: [(4, 'transitions', -0.4, 'drop slide l2-try3 (its three items repeat workbook Q4)'),
     (4, 'waiting', -1.1, 'drop slide l2-try3: no whiteboard round'),
     (4, 'speaking', -0.3, 'drop slide l2-try3: no reading')],
 3: [(4, 'transitions', -0.4, 'merge l3-try3 into l3-teach3 as one "your turn" item'),
     (4, 'waiting', -0.7, 'l3-try3 (b), (c) become Think harder / take-home; keep (a)'),
     (4, 'speaking', -0.3, 'trim the third think-aloud quote')],
 4: [(6, 'activity', +6.0, 'add four Core items from the Question Bank (core 1, 3, 4, 5: repeating-pattern positions) to Start here: 1.5 + 1.0 + 2.0 + 1.5 min')],
 5: [(6, 'activity', -2.5, 'Q5 (make your own story) marked "if you have time" like Q3d')],
 6: [(4, 'transitions', +0.8, 'add two "your turn" slides (Question Bank core 4 + 1/2; core 5/6)'),
     (4, 'waiting', +2.2, 'two added try slides'),
     (4, 'speaking', +0.4, 'two added try slides'),
     (6, 'activity', +2.0, 'add Question Bank core 5 and 6 (count the money: 35c, 45c) to Start here page 2')],
 8: [(6, 'speaking', -1.0, 'show l8-teachriddle and l8-teachodd with all steps revealed, 30 s each (they only serve optional Q5, Q6)'),
     (6, 'transitions', -0.4, 'two fewer slide clicks')],
 9: [(6, 'activity', -4.0, 'Q2: copy the pencil / book / shoe numbers from Explore into the table instead of measuring again'),
     (3, 'activity', -2.0, 'parents cut the cube strip BEFORE the lesson'),
     (5, 'activity', -0.5, 'giant steps in place, not across the room'),
     (6, 'speaking', -0.3, 'drop slide l9-tryconv (serves only optional Q4)'),
     (6, 'transitions', -0.4, 'drop slide l9-tryconv'),
     (6, 'waiting', -1.1, 'drop slide l9-tryconv')],
 10: [(3, 'speaking', -0.7, 'pairs read their own card; tutor does not read all four aloud'),
      (3, 'waiting', -2.4, 'debrief with ONE question (Q3); pair reports 20 s each'),
      (4, 'transitions', -0.4, 'drop slide l10-try2'),
      (4, 'waiting', -1.1, 'drop slide l10-try2'),
      (4, 'speaking', -0.3, 'drop slide l10-try2'),
      (8, 'speaking', -1.2, 'certificates: 10 s per child, one specific praise line each'),
      (1, 'waiting', -1.5, 'drop slide l10-warm2: the 5-question whiteboard round already revisits the nine lessons'),
      (1, 'speaking', -0.4, 'drop slide l10-warm2'),
      (1, 'transitions', -0.4, 'drop slide l10-warm2'),
      (4, 'transitions', -0.4, 'also drop l10-try1 (draw it): Explore cards are the practice'),
      (4, 'waiting', -1.1, 'also drop l10-try1'),
      (4, 'speaking', -0.3, 'also drop l10-try1'),
      (6, 'activity', +3.5, 'Q9 (make a puzzle for a friend) back on worksheet page 2, using the time freed by dropping 3 re-teach slides'),
      (7, 'activity', -3.5, 'talk time = swap, solve, share only')],
}
# proposed budgets: 10 parts + standing buffer (sum 90)
NEW_BUDGET = {
 1: ([4, 6, 4, 14, 10, 4, 30, 7, 6, 3], 2),
 2: ([2, 6, 4, 14, 10, 4, 32, 7, 6, 3], 2),
 3: ([2, 6, 4, 14, 11, 4, 31, 7, 6, 3], 2),
 4: ([2, 6, 4, 14, 11, 4, 31, 7, 6, 3], 2),
 5: ([2, 6, 4, 14, 10, 4, 32, 7, 6, 3], 2),
 6: ([2, 6, 4, 14, 10, 4, 32, 7, 6, 3], 2),
 7: ([2, 6, 4, 16, 8, 4, 32, 7, 6, 3], 2),
 8: ([2, 6, 4, 14, 10, 4, 32, 7, 6, 3], 2),
 9: ([2, 6, 4, 15, 10, 4, 31, 7, 6, 3], 2),
 10: ([2, 4, 4, 18, 9, 4, 30, 8, 8, 3], 0),
}


def fixed_parts(n, D):
    global FIX
    FIX = True
    try:
        parts, info = model(n, D)
    finally:
        FIX = False
    parts = [(a, b, dict(c), d) for a, b, c, d in parts]
    for idx, comp, delta, _txt in LESSON_DELTAS.get(n, []):
        parts[idx][2][comp] += delta
    return parts


SCENARIOS = {
    # name: (SPEAK_WPM, READ_WPM, WAIT_Q, HOLDUP, SLIDE, BREAKOUT, WS_START, ACT_MULT)
    'fast':  (135, 125, 24, 20, 20, 60, 90, 0.85),
    'base':  (120, 110, 30, 30, 25, 90, 120, 1.0),
    'slow':  (105, 95, 36, 40, 30, 120, 150, 1.15),
}


def set_scenario(name):
    global SPEAK_WPM, READ_WPM, WAIT_Q, HOLDUP, SLIDE, BREAKOUT, WS_START, ACT_MULT
    SPEAK_WPM, READ_WPM, WAIT_Q, HOLDUP, SLIDE, BREAKOUT, WS_START, ACT_MULT = SCENARIOS[name]


def lesson_total(n, D, fixed=False):
    parts = fixed_parts(n, D) if fixed else model(n, D)[0]
    return sum(sum(c.values()) for _, _, c, _ in parts)


def main():
    global WBQ
    WBQ = wb_questions()
    D = load_js()
    allout = []
    print('<!-- generated by docs/audit/timing_p1.py: base scenario tables -->')
    set_scenario('base')
    for n in range(1, 11):
        parts, info = model(n, D)
        tot_s = sum(p[1] for p in parts)
        tot_need = 0
        print(f'\n#### Lesson {n}: {D["L"][n-1]["title"]}\n')
        print('| Part (slides) | Scripted | REC | Speak | Wait | Activity | Transit | **Need** | Scripted - need | Flag | Clock end: scripted / est. |')
        print('|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|')
        rows = []; clock_s = 0
        for name, sc, c, ns in parts:
            need = sum(c.values())
            tot_need += need; clock_s += sc
            fl = flag(sc, need)
            print(f'| {name} ({ns}) | {sc} | {fmt(c["REC cue"])} | {fmt(c["speaking"])} | {fmt(c["waiting"])} | {fmt(c["activity"])} | {fmt(c["transitions"])} | **{fmt(need)}** | {fmt(sc-need)} | {fl} | {clock_s} / {fmt(tot_need)} |')
            rows.append((name, sc, need, fl, c))
        dd = tot_s - tot_need
        print(f'| **Whole lesson** | **{tot_s}** | {fmt(sum(r[4]["REC cue"] for r in rows))} | {fmt(sum(r[4]["speaking"] for r in rows))} | {fmt(sum(r[4]["waiting"] for r in rows))} | {fmt(sum(r[4]["activity"] for r in rows))} | {fmt(sum(r[4]["transitions"] for r in rows))} | **{fmt(tot_need)}** | **{fmt(dd)}** | {"OVER" if dd<=-2 else "TIGHT" if dd<1 else "OK" if dd<3 else "LOOSE"} | |')
        cc = child_completion(n)
        SC = D['SC'][str(n)]
        say_words = sum(words(re.sub(r'^[“"]|[”"]$', '', x)) for k in ('hook', 'warmIntro', 'predict', 'think', 'talk', 'close') for x in SC[k])
        all_words = sum(words(x) for k, v in SC.items() for x in (v if isinstance(v, list) else [v]))
        nslides = len(info['slides']); ntimed = sum(1 for s in info['slides'] if s['part'] != 'choice')
        mid = cc['MID']
        p1 = sum(m for _, m, o, pg in ITEMS[n] if pg == 1 and not o); p2 = sum(m for _, m, o, pg in ITEMS[n] if pg == 2 and not o)
        print(f'\nWorkbook (Start here, required items, MID child): page 1 needs {fmt(p1)} min of {mid["W1"]} available; page 2 needs {fmt(p2)} min of {mid["W2"]} available. '
              f'Finished in the scripted time: LOW {cc["LOW"]["done"]}/{cc["LOW"]["tot"]}, MIDDLE {cc["MID"]["done"]}/{cc["MID"]["tot"]}, HIGH {cc["HIGH"]["done"]}/{cc["HIGH"]["tot"]}. '
              f'Spare work minutes: MID {fmt(mid["spare"])}, HIGH {fmt(cc["HIGH"]["spare"])} (about {cc["HIGH"]["T"]} Think harder item(s) for a HIGH child).')
        print(f'\nSAY words (hook, warm-up intro, predict, think-aloud, talk, close): {say_words}; all lines in scripts.js: {all_words}; slides: {nslides} ({ntimed} on the timed path, {nslides-ntimed} untimed choice/Think harder/Go further slides).')
        allout.append(dict(n=n, need=tot_need, rows=rows, say=say_words, slides=nslides, timed=ntimed))
    print('\n#### Children and the Start-here worksheet\n')
    print('| Lesson | Required items (Start here) | Page 1 need / have | Page 2 need / have | LOW finishes | MIDDLE finishes | HIGH finishes | HIGH spare min (about Think harder items) |')
    print('|---|---:|---|---|---|---|---|---|')
    for n in range(1, 11):
        cc = child_completion(n); m = cc['MID']
        p1 = sum(x for _, x, o, pg in ITEMS[n] if pg == 1 and not o); p2 = sum(x for _, x, o, pg in ITEMS[n] if pg == 2 and not o)
        print(f'| {n} | {m["tot"]} | {fmt(p1)} / {m["W1"]} | {fmt(p2)} / {m["W2"]} | {cc["LOW"]["done"]} of {m["tot"]} | {m["done"]} of {m["tot"]} | {cc["HIGH"]["done"]} of {m["tot"]} | {fmt(cc["HIGH"]["spare"])} ({cc["HIGH"]["T"]}) |')
    print('\n#### Running clock (as scripted today): estimated minute at which each scripted mark is actually reached\n')
    print('| Lesson | min 10 | min 25 | min 40 | min 72 | min 80 | min 88 | end |')
    print('|---|---:|---:|---:|---:|---:|---:|---:|')
    for o in allout:
        cum = []; t = 0
        for r in o['rows']:
            t += r[2]; cum.append(t)
        print(f'| {o["n"]} | ' + ' | '.join(fmt(cum[i]) for i in (2, 3, 5, 6, 7, 8)) + f' | {fmt(cum[9])} |')
    print('\n#### After fixes\n')
    fixsum = []
    for n in range(1, 11):
        before, _ = model(n, D)
        after = fixed_parts(n, D)
        bud, buf = NEW_BUDGET[n]
        assert sum(bud) + buf == 90, (n, sum(bud) + buf)
        print(f'\n##### Lesson {n} after fixes\n')
        print('| Part | Old budget | Old need | New need | New budget | New scripted - need | Flag | New clock (start-end) |')
        print('|---|---:|---:|---:|---:|---:|---|---|')
        t0 = 0; tot_new = 0; tot_old = 0
        for i, ((nm, sc, c0, _), (_n2, _s2, c1, _x), nb) in enumerate(zip(before, after, bud)):
            o = sum(c0.values()); nw = sum(c1.values()); tot_new += nw; tot_old += o
            print(f'| {PART_NAMES[i]} | {sc} | {fmt(o)} | {fmt(nw)} | {nb} | {fmt(nb-nw)} | {flag(nb, nw)} | {t0}-{t0+nb} |')
            t0 += nb
        print(f'| Standing buffer | 0 | | | {buf} | | | {t0}-{t0+buf} |')
        print(f'| **Total** | 90 | **{fmt(tot_old)}** | **{fmt(tot_new)}** | **{sum(bud)+buf}** | **{fmt(sum(bud)-tot_new)}** (buffer {buf} not counted) | | |')
        fixsum.append((n, tot_old, tot_new))
    print('\n#### Summary (base)\n')
    print('| Lesson | Slides (timed) | SAY words | Need (min) | vs 90 | Range fast-slow | Parts OVER | Parts LOOSE | Need after fixes (base; fast-slow) |')
    print('|---|---:|---:|---:|---:|---|---|---|---|')
    for o in allout:
        n = o['n']
        set_scenario('fast'); f = lesson_total(n, D)
        set_scenario('slow'); sl = lesson_total(n, D)
        set_scenario('base')
        ov = ', '.join(r[0].split(' (')[0].split(' +')[0] for r in o['rows'] if r[3] == 'OVER')
        lo = ', '.join(r[0].split(' (')[0].split(' +')[0] for r in o['rows'] if r[3] == 'LOOSE')
        set_scenario('fast'); ff = lesson_total(n, D, True)
        set_scenario('slow'); fs = lesson_total(n, D, True)
        set_scenario('base'); fb = lesson_total(n, D, True)
        print(f'| {n} | {o["slides"]} ({o["timed"]}) | {o["say"]} | {fmt(o["need"])} | {o["need"]-90:+.1f} | {fmt(f)} - {fmt(sl)} | {ov or "-"} | {lo or "-"} | {fmt(fb)} ({fmt(ff)} - {fmt(fs)}) |')


if __name__ == '__main__':
    main()
