"""P4 fix pass, shared by rebuild/gen_p4l1.py ... gen_p4l10.py (own file for P4; slidekit.py is not edited).

finish(S, n, G, pic=None) is called by each generator just before the slides are written. It
  * rebuilds the warm-up check as "Sneak-peek puzzles" (access question + thinking question, answers shown privately),
  * rebuilds the reflection slide ("Looking back", 2 minutes, pass allowed),
  * adds the 'Go further' what-if strip to the explore slide,
  * renames Core / Think Harder / Challenge / Open investigation neutrally (Start here / Think harder / Go further / Investigation),
  * removes fast-track wording and writes the neutral 'choose' rule,
  * adds a minute label to every slide, adds the pass / volunteers-first rule to talk time.
G is the lesson's `gaps` export (p4/content/lN.js) as a dict.
"""
import re, html, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import slidekit
from slidekit import *

E = html.escape
FOOTSTART = '\n<p style="position:absolute;left:128px;bottom:64px'

TIME_PLAN = ('Time plan: opening 0 to 1, sneak-peek puzzles 1 to 4 (two ideas we have not learnt yet; answers shown privately, nobody marked), '
             'warm-up game 4 to 6 (one short round), quick questions 6 to 8, explore 8 to 18 (a Go further what-if is on the slide from minute 8), '
             'teaching 18 to 30 (click to reveal each step and answer; the "your turn" slides are optional, skip them if short of time), brain break 30 to 34, '
             'worksheet page 1 (Start here, in pairs) {P1}, short teaching before page 2 53 to 58, worksheet page 2 (on your own) 58 to 76 and check together 76 to 80, '
             'talk time 80 to 85, exit ticket {EX}, looking back (reflection) {RF}.{L10} '
             'After question 3 every child may choose: carry on, or try the Think harder page. Think harder, Go further and the Investigation have no fixed time slot: any child may choose them at any time, or take them home. '
             'The tutor never announces who is on which page, and pairs are not split unless both children agree. '
             'Online: page 1 is pair work, so allow about 2 minutes to move into and out of breakout rooms (or run page 1 as a whole-group screen-share if there are only 8 children).')

def _time_plan(n):
    P1 = '34 to 50 and check together 50 to 53' if n != 6 else '36 to 50 (after the 2-minute protractor demo at 34 to 36) and check together 50 to 53'
    if n == 10:
        return TIME_PLAN.format(P1=P1, EX='85 to 87', RF='87 to 89', L10=' Certificates and stamps 89 to 90.')
    return TIME_PLAN.format(P1=P1, EX='85 to 88', RF='88 to 90 (2 minutes)', L10='')

def _short(a):
    return a.split('. ')[0].rstrip('.') + '.'

def check_slide(n, G, pic=None):
    ID = f'p4l{n}'
    ck = G['check']
    body = h2('Sneak-peek puzzles')
    body += p('Ideas we have not learnt yet. Guesses and "I do not know" are welcome. Nobody is marked.', 30, 600, MUTED)
    body += p('Show your answer only to your tutor: hold your own paper to the camera, or use private chat.', 30, 600, MUTED)
    tops = [372, 660]
    labels = [('1', 'Try it'), ('2', 'Think')]
    for i, c in enumerate(ck):
        top = tops[i]
        pw = 440
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
        'Minutes 1 to 4 (3 minutes). SNEAK-PEEK PUZZLES. Say: "These are ideas we have not learnt yet. Guessing is welcome, drawing is welcome and so is saying I do not know. Nobody is marked, and nobody\'s answer is shown to the group." '
        'Puzzle 1 is a TRY IT puzzle: any child can start it with objects, a drawing or counting, so everyone has a first win. Puzzle 2 needs a little thinking. About 90 seconds each. '
        'Children show their answers PRIVATELY: on their own paper held up to your camera, or in private chat. Never ask for boards up in front of the group, never read out whose answer is whose, and never say who got it right. '
        'Then click to show each answer and talk it through for everyone ("some of you tried ..."), naming no child. Ask for volunteers first if you want a reason said aloud; nobody is called on by name, and passing is always fine. '
        'ANSWERS: 1) ' + ck[0]['a'] + ' 2) ' + ck[1]['a'] + ' '
        'A GOOD REASON: ' + G['why'] + ' '
        'Use what you see only to plan your help. It does not decide who is on which page and it is not recorded as a mark. '
        'After question 3 on page 1 every child may choose: carry on, or try the Think harder page. You may quietly invite a child with a PRIVATE chat message ("try the Think harder page when you are ready"), never by name in front of the group, and you never announce who is on which page. '
        'Everyone stays in the same room and every child turns to the page they choose. If a pair would be split, ask both children first; never leave a child alone on page 1 (join them to another pair or to yourself).')
    return sec(f'{ID}-check', '1–4 MIN', body, notes)

def _box(txt='', w=26):
    return f'<span style="display:inline-block;width:{w}px;height:{w}px;border:4px solid {NAVY};border-radius:6px;margin:0 12px -4px 24px;background:{WHITE}"></span>'

def reflect_slide(n, G):
    ID = f'p4l{n}'
    t0, t1 = ('88–90 MIN', '88 to 90 (2 minutes)') if n != 10 else ('87–89 MIN', '87 to 89 (2 minutes)')
    body = h2('Looking back')
    body += p('2 minutes. Write, tick or pass: you choose. Nobody marks it and it is not shown to the group. Your tutor may read it privately.', 30, 600, MUTED)
    body += pin(128, 340, 1664, p('Something I did well …', 40, 700), None, WHITE, 20, '22px 34px')
    body += pin(128, 460, 1664, p('The hardest part was …', 40, 700), None, WHITE, 20, '22px 34px')
    opts = ['drawing it', 'a list or table', 'a smaller number', 'my partner', 'reading it again', 'I asked for help']
    inner = p('What helped me:', 40, 700) + '<p style="font-size:32px;font-weight:600;line-height:1.9">' + ''.join(f'{_box()}{E(o)}' for o in opts) + '</p>'
    inner += f'<p style="font-size:32px;font-weight:600;line-height:1.9">{_box()}<b>I am still stuck</b> (my tutor will check in privately){_box()}other: ______</p>'
    body += pin(128, 580, 1664, inner, None, WHITE, 20, '22px 34px')
    body += pin(128, 840, 1664, f'<p style="font-size:32px;font-weight:700;color:{TEAL}">{_box()}<b>I pass today.</b> That is always fine.</p>', None)
    notes = (f'Minutes {t1}. LOOKING BACK. Children fill in the box on the Investigation page, the page every child has (something I did well; the hardest part was; what helped me). '
             'Say: "You can write, tick or pass. Ticking I am still stuck is a good thing to do: it tells me where to help." Model one yourself first: "' + G['reflect'] + '" '
             'Do not ask anyone to read theirs out. If a child wants to share, take one volunteer and thank them for the strategy. '
             'Never grade it, never correct it, never collect it for marks and never show it to the group. You may read a child\'s page privately (the child holds it to your camera when you ask, or sends a photo by the approved private channel). '
             'If I am still stuck is ticked, send a private message after the lesson or check in privately at the start of the next one. Praise strategies ("you drew it", "you asked for help"), not speed or scores.')
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
    ('Early finishers / take-home', 'Any time • take-home'),
    ('>Stretch</h2>', '>Think harder</h2>'),
    ('>Challenge</h2>', '>Go further</h2>'),
    ('>Challenge: see it</h2>', '>Go further: see it</h2>'),
    ('>Challenge: walk-through</h2>', '>Go further: walk-through</h2>'),
    ('Early finishers: ', 'Go further (on the slide), for any child who wants it: '),
    ('Early finishers', 'Children who choose to go further'),
    ('early finishers', 'children who choose to go further'),
    ('Stretch and Challenge come next', 'Think harder and Go further come next'),
    ('Stretch and challenge', 'Think harder and Go further'),
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

def finish(S, n, G, pic=None, go2=None, tp=None):
    ID = f'p4l{n}'
    S[f'{ID}-check'] = check_slide(n, G, pic)
    S[f'{ID}-reflect'] = reflect_slide(n, G)
    # title slide: label, time plan
    t = S[f'{ID}-title']
    t = re.sub(r'(LESSON \d+  •  WEEK \d+)', r'\1  •  0–1 MIN', t, count=1)
    t = re.sub(r'Time plan:.*?(</aside>)', lambda m: E(tp or _time_plan(n)) + m.group(1), t, count=1, flags=re.S)
    S[f'{ID}-title'] = t
    # go further strip on the explore slide
    S[f'{ID}-explore1'] = add_go_further(S[f'{ID}-explore1'], G['go2']['q'])
    # notes of explore1: add the go-further answer
    S[f'{ID}-explore1'] = S[f'{ID}-explore1'].replace('</aside>', E(' GO FURTHER (on the slide from minute 8, so nobody waits): ' + G['go2']['q'] + ' Answer: ' + G['go2']['a']) + '</aside>')
    # ws slides
    w1, w2 = f'{ID}-ws1', f'{ID}-ws2'
    S[w1] = S[w1].replace('Worksheet page 1: with your partner', 'Page 1 (Start here): with your partner')
    S[w2] = S[w2].replace('Worksheet page 2: on your own', 'Page 2: on your own')
    tipre = re.compile(r'(<p style="font-size:34px;font-weight:600;color:#3B4A6B;line-height:1\.3">)(.*?)(</p>)', re.S)
    S[w1] = tipre.sub(lambda m: m.group(1) + m.group(2) + E(' After question 3 you may choose: carry on, or try Think harder.') + m.group(3), S[w1], count=1)
    S[w2] = tipre.sub(lambda m: m.group(1) + E(G['cap'] + ' When you finish, choose: Think harder, Go further or the Investigation.') + m.group(3), S[w2], count=1)
    S[w1] = S[w1].replace('</aside>', E(' CHOOSING: after question 3 every child may carry on or try the Think harder page. Invite a child quietly by PRIVATE chat only; never by name in front of the group; never announce who is on which page. If one child of a pair wants to move on, do not split the pair unless both agree; if a pair does lose a member, join the other child to another pair or to yourself straight away. Children on Think harder keep working through the page check; reading along is optional.') + '</aside>')
    S[w2] = S[w2].replace('</aside>', E(' SOLO PAGE CAP: ' + G['cap'] + ' Children who finish choose Think harder, Go further or the Investigation; nobody is told which.') + '</aside>')
    # talk slide
    tk = S[f'{ID}-talk']
    tk = tk.replace(FOOTSTART, '\n' + card(p('Pass is always fine. Volunteers share first. We do not keep scores.', 30, 600, MUTED)) + FOOTSTART, 1)
    tk = tk.replace('</aside>', E(' TALK TIME RULES: ask for volunteers first; a child may always pass; never call on a child by name to answer; no public tallies, scores or rankings; praise the reason, not the child. If a question uses a mistaken idea (a character who gets it wrong), present it as the character\'s idea and ask "What would you say to them?" so no child owns the mistake.') + '</aside>')
    S[f'{ID}-talk'] = tk
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
