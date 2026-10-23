"""P4 fix pass, shared by rebuild/gen_p4l1.py ... gen_p4l10.py (own file for P4; slidekit.py is not edited).

finish(S, n, G, pic=None) is called by each generator just before the slides are written. It
  * rebuilds the warm-up check as "Sneak-peek puzzles" (access question + thinking question, answers ticked or said together on three; nothing held up to the camera),
  * rebuilds the reflection slide ("Looking back", 2 minutes, pass allowed),
  * adds the 'Go further' what-if strip to the explore slide,
  * renames Core / Think Harder / Challenge / Open investigation neutrally (Start here / Think harder / Go further / Investigation),
  * removes fast-track wording and writes the neutral 'choose' rule,
  * adds a minute label to every slide, adds the pass / volunteers-first rule to talk time.
  * re-budget pass (docs/audit/rebudget_p4.md): every clock time comes from rebuild/p4_budget.py (title-slide Time plan,
    sneak-peek and Looking back slides); check_times() stops the build if any slide pill disagrees with that plan.
G is the lesson's `gaps` export (p4/content/lN.js) as a dict.
"""
import re, html, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import slidekit
from slidekit import *
import p4_budget as B

E = html.escape
FOOTSTART = '\n<p style="position:absolute;left:128px;bottom:64px'

def _r(a, b):
    return f'{B.fmt(a)} to {B.fmt(b)}'

def _win(n, suffix):
    a, b = B.window(n, suffix)
    return _r(a, b)

def _time_plan(n, G):
    P = {t: (a, b) for t, a, b in B.parts(n)}
    W = {i: (a, b) for i, (t, a, b) in enumerate(B.ws_blocks(n))}
    buf = B.fmt(B.BUFFER[n])
    keep = B.KEPT_TRY[n]
    tries = ('the one "your turn" slide is optional: skip it if you are behind' if keep else 'there is no "your turn" slide today')
    p1 = G['p1']
    ws = P['Worksheet']
    pre = ''
    if n == 6:
        pre = ' (the first 2 minutes are the protractor demo)'
    s = (f'Time plan (90 minutes in all; every part has a budget and there is a {buf}-minute standing buffer inside the page-2 block). '
         f'Opening {_r(*P["Opening"])}. Sneak-peek puzzles {_r(*P["Sneak-peek puzzles"])} (puzzle 1 about 60 seconds, puzzle 2 about 90 seconds, then ONE check moment for both puzzles; answers ticked or said together on three; nothing held up to the camera, nobody marked). '
         f'Warm-up game {_win(n, "warm1")} (one short round, about 90 seconds), quick questions {_win(n, "warm2")} (three questions). '
         f'Explore {_r(*P["Explore (in pairs)"])} (the only breakout of the first half: about 60 seconds each way, closed by a 60-second timer; a Go further what-if is on the slide from the start; two debrief questions). '
         f'Teaching {_r(*P["Mini-lesson"])} (click to reveal each step and answer; {tries}). '
         f'Brain break {_r(*P["Brain break"])} (water and toilet first, then the game; clock check at the end of the break: if you are more than 1.5 minutes behind, skip the next optional item, never a check, the exit ticket or Looking back). '
         f'Worksheet {_r(*ws)}: page 1 (Start here, in pairs){pre} {_r(*W[0])}, check together {_r(*W[1])}, short teaching before page 2 {_r(*W[2])}, '
         f'page 2 on your own {_r(*W[3])} (the last {buf} minutes are the standing buffer: if earlier parts ran long, spend the buffer first, then the choice questions, and never the checks, the exit ticket or Looking back), check together {_r(*W[4])}. '
         f'Talk time {_r(*P["Talk time"])} (one minute of pair talk, no breakout; one minute is the tool question: where did you use today\'s tool?). Exit ticket {_r(*P["Exit ticket"])}. Looking back {_r(*P["Looking back"])} (common look-back: 90-second timer, then about 60 seconds to stamp journals). ')
    if n == 10:
        s += f'Certificates and goodbye {_r(*P["Certificates and goodbye"])} (whole group, no per-child comments). '
    s += (p1 + ' Think harder, Go further and the Investigation have no fixed time slot: any child may choose them at any time, or take them home. '
          'The tutor never announces who is on which page, and pairs are not split unless both children agree. '
          'Online: page 1 is pair work, so allow about 2 minutes to move into and out of breakout rooms (or run page 1 as a whole-group screen-share if there are only 8 children).')
    return s

def _short(a):
    return a.split('. ')[0].rstrip('.') + '.'

def check_slide(n, G, pic=None):
    ID = f'p4l{n}'
    ck = G['check']
    body = h2('Sneak-peek puzzles')
    body += p('Ideas we have not learnt yet. Guesses and "I do not know" are welcome. Nobody is marked.', 30, 600, MUTED)
    body += p('Write your answer on your own paper. When your tutor says, say your answer together on three. Only your tutor looks.', 30, 600, MUTED)
    tops = [372, 660]
    labels = [('1', 'Try it'), ('2', 'Think')]
    for i, c in enumerate(ck):
        top = tops[i]
        pw = (260 if (pic and pic.get(i) and 'viewBox="0 0 220' in pic[i]) else 440)
        qw = 1664 - 190 - 20 - (pw + 20 if (pic and pic.get(i)) else 0)
        lab = f'<div style="width:170px;flex:none;background:{WHITE};border-radius:20px;padding:14px 10px;display:flex;flex-direction:column;align-items:center;justify-content:center"><p style="font-size:44px;font-weight:800;color:{TEAL};line-height:1">{labels[i][0]}</p><p style="font-size:26px;font-weight:700;color:{MUTED}">{labels[i][1]}</p></div>'
        qd = f'<div style="flex:1;min-width:0;background:{WHITE};border-radius:20px;padding:16px 28px;display:flex;align-items:center"><p style="font-size:32px;font-weight:700;line-height:1.28">{E(c["q"])}</p></div>'
        extra = ''
        if pic and pic.get(i):
            extra = f'<div style="width:{pw}px;flex:none;background:{WHITE};border-radius:20px;padding:10px;display:flex;align-items:center;justify-content:center">{pic[i]}</div>'
        row = f'<div style="display:flex;gap:20px;align-items:stretch">{lab}{qd}{extra}</div>'
        body += pin(128, top, 1664, row, None)
        body += pin(128 + 190, top + (150 if len(c['q']) < 150 else 168) + (22 if (pic and pic.get(i)) else 0), 1664 - 190 - 0, f'<p style="font-size:32px;font-weight:800;line-height:1.2">{E(c.get("s") or _short(c["a"]))}</p>', 'pop', YEL, 20, '14px 26px')
    notes = (
        f'Minutes {B.fmt(B.window(n, "check")[0])} to {B.fmt(B.window(n, "check")[1])} ({B.fmt(B.DUR[n]["sneak"])} minutes). SNEAK-PEEK PUZZLES. Say: "These are ideas we have not learnt yet. Guessing is welcome, drawing is welcome and so is saying I do not know. Nobody is marked, and nobody\'s answer is shown to the group." '
        'Puzzle 1 is a TRY IT puzzle: any child can start it with objects, a drawing or counting, so everyone has a first win. Puzzle 2 needs a little thinking. Give about 60 seconds for puzzle 1 and about 90 seconds for puzzle 2. '
        'Children show their answers PRIVATELY: written on their own paper and said together on three (nothing is held up to the camera). Make ONE check for both puzzles, after puzzle 2: children say the answers together on three. Never use private chat or DMs. Never ask for boards or paper held up in front of the group or to the camera, never read out whose answer is whose, and never say who got it right. '
        'Then click to show each answer and talk it through for everyone ("some of you tried ..."), naming no child. Nobody is called on by name, and passing is always fine. '
        'ANSWERS: 1) ' + ck[0]['a'] + ' 2) ' + ck[1]['a'] + ' '
        'A GOOD REASON: ' + G['why'] + ' '
        'Use what you see only to plan your help. It does not decide who is on which page and it is not recorded as a mark. '
        + ' ON PAGE 1 (printed): "' + G['p1'] + '" Make the invitation to the WHOLE group ("when you have finished Start here you can choose Think harder, Go further or the Investigation"), so nobody is singled out. Never message a child privately, never name a child, and never announce who is on which page. '
        'Everyone stays in the same room and every child turns to the page they choose. If a pair would be split, ask both children first; never leave a child alone on page 1 (join them to another pair or to yourself).')
    return sec(f'{ID}-check', B.pill(n, 'check'), body, notes)

def _box(txt='', w=26):
    return f'<span style="display:inline-block;width:{w}px;height:{w}px;border:4px solid {NAVY};border-radius:6px;margin:0 12px -4px 24px;background:{WHITE}"></span>'

def reflect_slide(n, G):
    ID = f'p4l{n}'
    t0 = B.pill(n, 'reflect'); w = B.window(n, 'reflect'); t1 = f'{B.fmt(w[0])} to {B.fmt(w[1])} (2 minutes of writing, {B.fmt(B.DUR[n]["look"])} minutes with the routine)'
    body = h2('Looking back')
    body += p('2 minutes. Write, tick or pass: you choose. Nobody marks it and it is not shown to the group. Nothing is held up to the camera.', 30, 600, MUTED)
    body += pin(128, 340, 820, p('Something I did well …', 40, 700), None, WHITE, 20, '22px 34px', 'box-sizing:border-box;')
    body += pin(972, 340, 820, p('The hardest part was …', 40, 700), None, WHITE, 20, '22px 34px', 'box-sizing:border-box;')
    opts = ['drawing it', 'a list or table', 'a smaller number', 'my partner', 'reading it again', 'I asked for help', 'other: ______']
    inner = p('What helped me:', 36, 700) + '<p style="font-size:28px;font-weight:600;line-height:1.6">' + ''.join(f'<span style="white-space:nowrap">{_box(w=22)}{E(o)}</span>' for o in opts) + '</p>'
    body += pin(128, 480, 820, inner, None, WHITE, 20, '20px 28px', 'box-sizing:border-box;')
    opts2 = ['drawing it', 'a list or table', 'a smaller number', 'a partner', 'another question like this', 'other: ______']
    inner = p('One thing I could try next:', 36, 700) + '<p style="font-size:28px;font-weight:600;line-height:1.6">' + ''.join(f'<span style="white-space:nowrap">{_box(w=22)}{E(o)}</span>' for o in opts2) + '</p>'
    body += pin(972, 480, 820, inner, None, WHITE, 20, '20px 28px', 'box-sizing:border-box;')
    inner = f'<p style="font-size:28px;font-weight:600;line-height:1.5"><span style="white-space:nowrap">{_box(w=22)}<b>I am still stuck</b> (my tutor will check in with me)</span><span style="white-space:nowrap">{_box(w=22)}<b style="color:{TEAL}">I pass on this one, or today.</b> That is always fine.</span></p>'
    body += pin(128, 760, 1664, inner, None, WHITE, 20, '16px 28px', 'box-sizing:border-box;')
    notes = (f'Minutes {t1}. LOOKING BACK. Children fill in the box on the Investigation page, the page every child has (something I did well; the hardest part was; what helped me; one thing I could try next). '
             'Say one sentence: "Turn to page 3, the Looking back box. Write, tick or pass. Two minutes, no talking." The printed box says the rest. Model one yourself first: "' + G['reflect'] + '" Say: "Ticking I am still stuck is a good thing to do: it tells me where to help." '
             'Do not ask anyone to read theirs out. If a child wants to share, take one volunteer and thank them for the strategy. '
             'Never grade it, never correct it, never collect it for marks and never show it to the group. Never ask a child to hold a page to the camera. Never ask for photos or private messages. '
             'If I am still stuck is ticked, check in during the open session: a quick visit to the shared breakout room or a hand signal, with a parent nearby. Never send a DM. Praise strategies ("you drew it", "you asked for help"), not speed or scores.')
    return sec(f'{ID}-reflect', t0, body, notes)

def go_strip(txt):
    return (f'<div style="background:{SOFT};border-radius:20px;padding:14px 30px;border:3px solid {YEL}">'
            f'<p style="font-size:29px;font-weight:700;line-height:1.3"><span style="color:{TEAL};font-weight:800">Go further (any time):</span>  {E(txt)}</p></div>')

def add_go_further(h, txt):
    # tighten the two cards a little so the strip fits above y 920, then append the strip after the last card
    h = h.replace('padding:32px 40px;display:flex', 'padding:18px 40px;display:flex', 2)
    h = h.replace('font-size:34px;font-weight:600;padding-left:52px', 'font-size:31px;font-weight:600;padding-left:52px')
    h = h.replace('font-size:32px;font-weight:600;padding-left:52px', 'font-size:31px;font-weight:600;padding-left:52px')
    h = h.replace('padding:20px 32px', 'padding:8px 32px')
    h = h.replace('padding:128px 128px 160px;display:flex;flex-direction:column;gap:28px', 'padding:112px 128px 160px;display:flex;flex-direction:column;gap:12px', 1)
    i = h.index(FOOTSTART)
    return h[:i] + '\n' + go_strip(txt) + h[i:]

REPL = [
    ('Early finishers / take-home', B.OPT_PILL),
    ('>Stretch</h2>', '>Think harder</h2>'),
    ('>Challenge</h2>', '>Go further</h2>'),
    ('>Challenge: see it</h2>', '>Go further: see it</h2>'),
    ('>Challenge: walk-through</h2>', '>Go further: walk-through</h2>'),
    ('Early finishers: ', 'Go further (on the slide), for any child who wants it: '),
    ('Early finishers', 'Children who choose to go further'),
    ('early finishers', 'children who choose to go further'),
    ('Stretch and Challenge come next', 'Think harder and Go further come next'),
    ('Stretch and challenge', 'Think harder and Go further'),
    ('Warm-up check', 'Sneak-peek puzzles'),
    ('Think Harder', 'Think harder'),
    ('Open investigation', 'Investigation'),
    ('the Challenge slides', 'the Go further slides'),
    ('Challenge slide notes', 'Go further slide notes'),
    ('the Challenge', 'Go further'),
    ('after pairs have tried the Challenge', 'after pairs have tried Go further'),
]

def _renames(h, n):
    for a, b in REPL:
        h = h.replace(a, b)
    if n == 10:
        pass
    # remaining capitalised section word "Challenge" (but not "Challenge Day")
    h = re.sub(r'\bChallenge(?! Day)\b', 'Go further', h)
    return h

def _label(h, text):
    """add a minute label to a slide with none: put it top right like sec() does"""
    if 'MIN' in h[:900] and re.search(r'right:128px;top:(64|52)px', h):
        return h
    tag = f'<p style="position:absolute;right:128px;top:64px;font-size:28px;font-weight:700;letter-spacing:2px;color:{YEL}">{E(text)}</p>'
    i = h.index('>') + 1
    # insert after the opening <section ...> tag
    m = re.match(r'<section[^>]*>', h)
    return h[:m.end()] + '\n' + tag + h[m.end():]

def _buffer_note(n):
    a, b = B.buffer_window(n)
    return (f'BUFFER: the last {B.fmt(B.BUFFER[n])} minutes of this block (minute {B.fmt(a)} to {B.fmt(b)}) are the standing buffer. If earlier parts ran long, page 2 starts late and the buffer is spent first, then the choice questions at the end of the page. '
            'Never shorten the checks, the exit ticket or Looking back. Say nothing about the buffer to the children.')

PILL_RE = re.compile(r'(?:\d+(?:\.\d)?–\d+(?:\.\d)? MIN(?: • OPTIONAL)?|Optional, if you finish early)')

def check_times(S, n):
    """stop the build if a slide pill disagrees with rebuild/p4_budget.py (or a slide has no entry in the plan)"""
    ID = f'p4l{n}'
    known = {s for s, a, b in B.SLIDES[n]} | set(B.EARLY[n])
    for sid, h in S.items():
        suf = sid[len(ID) + 1:]
        if suf not in known:
            raise AssertionError(f'{sid}: not in the P4 budget plan (rebuild/p4_budget.py)')
        want = B.pill(n, suf)
        head = h[:1500]
        if want not in head:
            raise AssertionError(f'{sid}: time pill should read {want!r}')
        for m in PILL_RE.findall(head):
            if m != want:
                raise AssertionError(f'{sid}: second time label {m!r} (plan: {want!r})')
    for suf in known:
        if f'{ID}-{suf}' not in S:
            raise AssertionError(f'{ID}-{suf}: in the budget plan but not built')

def finish(S, n, G, pic=None, go2=None, tp=None):
    ID = f'p4l{n}'
    S[f'{ID}-check'] = check_slide(n, G, pic)
    S[f'{ID}-reflect'] = reflect_slide(n, G)
    # title slide: label, time plan
    t = S[f'{ID}-title']
    t = re.sub(r'(LESSON \d+  •  WEEK \d+)', lambda m: m.group(1) + '  •  ' + B.pill(n, 'title'), t, count=1)
    t = re.sub(r'Time plan:.*?(</aside>)', lambda m: E(tp or _time_plan(n, G)) + m.group(1), t, count=1, flags=re.S)
    S[f'{ID}-title'] = t
    # go further strip on the explore slide
    S[f'{ID}-explore1'] = add_go_further(S[f'{ID}-explore1'], G['go2']['q'])
    # notes of explore1: add the go-further answer
    S[f'{ID}-explore1'] = S[f'{ID}-explore1'].replace('</aside>', E(' GO FURTHER (on the slide from the start of the explore, so nobody waits): ' + G['go2']['q'] + ' Answer: ' + G['go2']['a']) + '</aside>')
    # ws slides
    w1, w2 = f'{ID}-ws1', f'{ID}-ws2'
    S[w1] = S[w1].replace('Worksheet page 1: with your partner', 'Page 1 (Start here): with your partner')
    S[w2] = S[w2].replace('Worksheet page 2: on your own', 'Page 2: on your own')
    tipre = re.compile(r'(<p style="font-size:34px;font-weight:600;color:#3B4A6B;line-height:1\.3">)(.*?)(</p>)', re.S)
    S[w1] = tipre.sub(lambda m: m.group(1) + m.group(2) + E(' ' + G['p1']) + m.group(3), S[w1], count=1)
    S[w2] = tipre.sub(lambda m: m.group(1) + E(G['cap'] + ' When you finish, choose: Think harder, Go further or the Investigation.') + m.group(3), S[w2], count=1)
    S[w1] = S[w1].replace('</aside>', E(' CHOOSING (printed on page 1: "' + G['p1'] + '"): invite the WHOLE group ("when you have finished Start here you can choose Think harder, Go further or the Investigation"); never message a child privately, never name a child, never announce who is on which page. If one child of a pair wants to move on, do not split the pair unless both agree; if a pair does lose a member, join the other child to another pair or to yourself straight away. Children on Think harder keep working through the page check; reading along is optional.') + '</aside>')
    S[w2] = S[w2].replace('</aside>', E(' SOLO PAGE CAP: ' + G['cap'] + ' Children who finish choose Think harder, Go further or the Investigation; nobody is told which. ' + _buffer_note(n)) + '</aside>')
    # talk slide
    tk = S[f'{ID}-talk']
    tk = tk.replace(FOOTSTART, '\n' + card(p('Pass is always fine. Volunteers share first. We do not keep scores.', 30, 600, MUTED)) + FOOTSTART, 1)
    tk = tk.replace('</aside>', E(' TALK TIME RULES: ask for volunteers first; a child may always pass; never call on a child by name to answer; no public tallies, scores or rankings; praise the reason, not the child. If a question uses a mistaken idea (a character who gets it wrong), present it as the character\'s idea and ask "What would you say to them?" so no child owns the mistake.') + '</aside>')
    S[f'{ID}-talk'] = tk
    # clock: talk and exit windows come from the budget (Talk time got 1 minute from Looking back, spine routine, 23 Oct)
    for suf in ('talk', 'exit'):
        a, b = B.window(n, suf); h = S[f'{ID}-{suf}']
        h = PILL_RE.sub(B.pill(n, suf), h, count=1)
        h = re.sub(r'Minutes [\d.]+ to [\d.]+\.', f'Minutes {B.fmt(a)} to {B.fmt(b)}.', h, count=1)
        S[f'{ID}-{suf}'] = h
    S[f'{ID}-talk'] = S[f'{ID}-talk'].replace('</aside>', E(' TOOL MINUTE: Talk time is one minute longer than before (the common look-back is shorter). Spend it on the question on the slide: where did you use today\'s tool, and what did it help you see? Listen for the tool named, not for the answer; a child may pass.') + '</aside>', 1)
    # all slides: neutral names
    for k in list(S):
        S[k] = _renames(S[k], n)
    # minute labels on every slide that lacks one
    return S

def order(order_list, n):
    ID = f'p4l{n}'
    o = [x for x in order_list if x not in (f'{ID}-check', f'{ID}-reflect')]
    o.insert(o.index(f'{ID}-warm1'), f'{ID}-check')
    # reflection is the last slide (L10: before the end slide)
    if f'{ID}-end' in o:
        o.insert(o.index(f'{ID}-end'), f'{ID}-reflect')
    else:
        o.append(f'{ID}-reflect')
    return o
