"""Math Inquirers P6, Lesson 8: Secret Codes. Writes split/p6l8/project (deck.json + slides/*.html).
Text that the tutor guide also reads (today, warm-up, explore, key idea, talk, exit, question bank) comes from p6/content/l8.js.
Code strips and clocks are computed (letter number + shift, mod 26), so every picture is exact."""
import json, os, sys, math, re, subprocess, datetime
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, H)
import slidekit
from slidekit import *
slidekit.FOOT = 'Math Inquirers P6  •  Notice it. Test it. Explain why.'
ROOT = os.path.join(H, '..')
D = os.path.join(ROOT, 'split', 'p6l8', 'project'); os.makedirs(os.path.join(D, 'slides'), exist_ok=True)
C = json.loads(subprocess.check_output(['node', '-e', "const c=require(process.argv[1]);console.log(JSON.stringify({lesson:c.lesson,script:c.script,deck:c.deck,qbank:c.qbank}))", os.path.join(ROOT, 'p6', 'content', 'l8.js')]))
L, SC, DK, QB = C['lesson'], C['script'], C['deck'], C['qbank']
S = {}
def put(i, h): S[i] = h
RED = '#D64545'
ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# ---------- SVG helpers ----------
def SV(w, h, body, label, extra=''): return f'<svg aria-label="{E(label)}" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="width:{w}px;height:{h}px;{extra}">{body}</svg>'
def T(x, y, s, size=32, fill=NAVY, weight=700, anchor='middle'): return f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" fill="{fill}" font-family="Fredoka, Arial">{E(str(s))}</text>'

# code blocks: our own simple coloured shapes. prog items: (kind, text) or (kind, text, [children]); {..} = white slot
BC = {'event': (YEL, NAVY), 'ctrl': (WHITE, NAVY), 'motion': (SKY, NAVY), 'pen': (TEAL, WHITE), 'var': (RED, WHITE), 'looks': (YEL, NAVY)}
def cwid(s, fs): return sum(fs * (0.36 if c in "iltfjr .,:()'|" else 0.78 if (c.isupper() or c in 'mw%×') else 0.62) for c in s)
def segs(t): return [(x[1:-1], True) if x.startswith('{') else (x.strip(), False) for x in re.split(r'(\{[^}]*\})', t) if x.strip()]
def blocks(prog, fs=28, h=52):
    pad, arm, gap, sp = 14, 28, 9, 12
    def lw(t): return sum(cwid(g, fs) + (2 * sp if sl else 0) + gap for g, sl in segs(t)) - gap + 2 * pad
    def txt(x, y, t, fg):
        s = ''; cx = x + pad; ty = y + h / 2 + fs * 0.36
        for g, sl in segs(t):
            w = cwid(g, fs)
            if sl:
                s += f'<rect x="{cx:.1f}" y="{y+7}" width="{w+2*sp:.1f}" height="{h-14}" rx="{(h-14)/2}" fill="{WHITE}" stroke="{NAVY}" stroke-width="2.5"/>'
                s += f'<text x="{cx+sp+w/2:.1f}" y="{ty:.1f}" font-size="{fs}" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="Arial">{E(g)}</text>'; cx += w + 2 * sp + gap
            else:
                s += f'<text x="{cx:.1f}" y="{ty:.1f}" font-size="{fs}" font-weight="700" fill="{fg}" font-family="Arial">{E(g)}</text>'; cx += w + gap
        return s
    mx = [0]
    def draw(items, x, y):
        s = ''
        for it in items:
            kind, t = it[0], it[1]; bg, fg = BC[kind]
            if len(it) > 2:
                w = max(lw(t), 180); inner, y2 = draw(it[2], x + arm, y + h + 3)
                yb = max(y2, y + h + 24); wb = max(w * 0.45, 120)
                s += f'<path d="M{x} {y} H{x+w:.1f} V{y+h} H{x+arm} V{yb} H{x+wb:.1f} V{yb+22} H{x} Z" fill="{bg}" stroke="{NAVY}" stroke-width="3" stroke-linejoin="round"/>' + txt(x, y, t, fg) + inner
                mx[0] = max(mx[0], x + w); y = yb + 25
            else:
                w = lw(t)
                s += f'<rect x="{x}" y="{y}" width="{w:.1f}" height="{h}" rx="{22 if kind=="event" else 10}" fill="{bg}" stroke="{NAVY}" stroke-width="3"/>' + txt(x, y, t, fg)
                mx[0] = max(mx[0], x + w); y += h + 3
        return s, y
    body, y = draw(prog, 3, 3)
    return body, math.ceil(mx[0] + 6), math.ceil(y + 3)
def blocks_svg(prog, label, fs=28, h=52):
    b, w, hh = blocks(prog, fs, h); return SV(w, hh, b, label)

def ostep(left, top, n, text, ov=None, ovw=0, ovh=0, dx=0, dy=0, tw=1000, size=34, build='fade'):
    """One click = overlay marks (same left/top as the base picture) + the step text box beside it."""
    lab = f'<span style="color:{TEAL};font-weight:800">Step {n}.</span>  ' if n else ''
    box = f'<div style="margin-top:{dy}px;width:{tw}px;box-sizing:border-box;background:{WHITE};border-radius:20px;padding:16px 28px;flex:none"><p style="font-size:{size}px;font-weight:600;line-height:1.3">{lab}{E(text)}</p></div>'
    if ov is None: return pin(left + dx, top, tw, box, build)
    o = f'<div style="width:{ovw}px;height:{ovh}px;flex:none">{ov}</div>'
    return pin(left, top, dx + tw, f'<div style="display:flex;align-items:flex-start;gap:{dx-ovw}px">{o}{box}</div>', build)
def soft(left, top, width, text, size=34, build='fade'): return pin(left, top, width - 56, p(text, size, 700), build, SOFT, 20, '18px 28px')
def stitle(t, size=34): return p(t, size, 600, MUTED)
def num(a, b): return f'<span style="color:{TEAL}">{E(a)}</span>  {E(b)}'
def check2(sid, time, title, rows, notes, lw=230, size=34, gap=24, top=250):
    """check-together slide: label + answer box (click), heights from the number of lines"""
    body = h2(title); y = top
    for a, b, nl in rows:
        hgt = int(nl * size * 1.25 + 36)
        body += pin(128, y, lw - 20, f'<p style="font-size:34px;font-weight:800;color:{TEAL}">{E(a)}</p>', None, WHITE, 20, '18px 24px')
        body += pin(128 + lw, y, 1664 - lw - 52, f'<p style="font-size:{size}px;font-weight:800;line-height:1.25">{E(b)}</p>', 'pop', YEL, 20, '18px 26px')
        y += hgt + gap
    assert y <= 940, (sid, y)
    return sec(sid, time, body, notes)
def qa_slide(sid, time, title, sub, rows, notes, size=36, step=150, top=330, qw=1250):
    body = h2(title) + (stitle(sub) if sub else '')
    for i, (a, b, c) in enumerate(rows):
        body += qrow(128, top + i * step, qw, a, b, size) + answer(128 + qw + 42, top + i * step, 1664 - qw - 42, c)
    return sec(sid, time, body, notes)
def dark(sid, bg, inner, notes, foot='#B7C3DD'):
    return (f'<section id="{sid}" data-transition="fade" style="background:{bg};color:{CREAM};font-family:{BF};padding:128px 128px 160px;display:flex;flex-direction:column;justify-content:center;gap:36px">\n'
            f'{inner}\n<p style="position:absolute;left:128px;bottom:64px;width:1400px;font-size:24px;color:{foot}">{E(slidekit.FOOT)}</p>\n<aside>{E(notes)}</aside>\n</section>\n')


PY = open(os.path.join(ROOT, 'p6', 'content', 'l8.js')).read().split('const PY = `')[1].split('`;')[0]
PYNOTE = 'Optional Python version (for children who already know Python):\n' + PY + '\nRun as it is, it prints PHHW DW WKH PUW (MEET AT THE MRT with shift 3). Set shift = -3 and message = "PHHW DW WKH PUW" to decode (Python % gives a answer between 0 and 25 even for negative numbers).'

# ---------- clocks, day rings and code strips ----------
def clock(hr, cx=200, cy=200, r=170, hand=TEAL, ghost=None, label='', mark=None):
    s = f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{WHITE}" stroke="{NAVY}" stroke-width="6"/>'
    for k in range(1, 13):
        a = math.radians(-90 + 30 * k); s += T(cx + (r - 38) * math.cos(a), cy + (r - 38) * math.sin(a) + 12, k, 34)
    def hnd(h, col, w=10, ln=0.55):
        a = math.radians(-90 + 30 * (h % 12)); return f'<line x1="{cx}" y1="{cy}" x2="{cx + r * ln * math.cos(a):.1f}" y2="{cy + r * ln * math.sin(a):.1f}" stroke="{col}" stroke-width="{w}" stroke-linecap="round"/>'
    if ghost is not None: s += hnd(ghost, '#9AA6C0', 8, 0.5)
    s += hnd(hr, hand) + f'<circle cx="{cx}" cy="{cy}" r="12" fill="{NAVY}"/>'
    return s
def clock_arc(h1, h2, cx=200, cy=200, r=125, col=RED):
    a1 = math.radians(-90 + 30 * (h1 % 12)); a2 = math.radians(-90 + 30 * (h2 % 12))
    large = 1 if ((h2 - h1) % 12) > 6 else 0
    return f'<path d="M{cx + r * math.cos(a1):.1f} {cy + r * math.sin(a1):.1f} A{r} {r} 0 {large} 1 {cx + r * math.cos(a2):.1f} {cy + r * math.sin(a2):.1f}" fill="none" stroke="{col}" stroke-width="9" stroke-linecap="round" stroke-dasharray="3 14"/>'
DAYS = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
def dayring(start=None, end=None, cx=230, cy=230, r=170, label=''):
    s = ''
    for k, d in enumerate(DAYS):
        a = math.radians(-90 + 360 * k / 7); x, y = cx + r * math.cos(a), cy + r * math.sin(a)
        fill = YEL if k == start else (SKY if k == end else WHITE)
        s += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="52" fill="{fill}" stroke="{NAVY}" stroke-width="5"/>' + T(x, y + 11, d, 32)
    return s
def codestrip(shift, w=1664, hl=(), label=None, top=0):
    cw = w / 26; s = ''
    for row, off, y in ((0, 0, 4), (1, shift, 78)):
        for i in range(26):
            c = ABC[(i + off) % 26]; x = i * cw
            fill = YEL if (row == 0 and i in hl) else (SKY if row == 1 and i in hl else (WHITE if row == 0 else '#EAF4EF'))
            s += f'<rect x="{x:.1f}" y="{y}" width="{cw:.1f}" height="68" fill="{fill}" stroke="{NAVY}" stroke-width="3"/>' + T(x + cw / 2, y + 46, c, 36)
    for i in range(26): s += T(i * cw + cw / 2, 168, i, 24, MUTED, 600)
    return s
def strip_svg(shift, hl=(), w=1664, label=None):
    return SV(w, 180, codestrip(shift, w, hl), label or f'A code strip: the alphabet A to Z on the top row and, underneath, the alphabet shifted by {shift}, so A sits above {ABC[shift % 26]}. Letter numbers 0 to 25 are shown below.')

# ================= 1. title =================
inner = (f'<p style="font-size:32px;font-weight:700;letter-spacing:4px;color:{YEL}">LESSON 8  •  WEEK 4  •  MATHS + CODE</p>'
         f'<h1 style="font-family:{HF};font-size:128px;font-weight:600;line-height:1.05">Secret Codes</h1>'
         f'<p style="font-size:44px;color:#C9D4EC">Clock (modular) arithmetic</p>'
         f'<div style="background:#26385F;border-radius:24px;padding:40px;display:flex;flex-direction:column;gap:12px"><p style="font-size:28px;font-weight:700;letter-spacing:3px;color:{YEL}">TODAY WE WILL</p><p style="font-size:44px;font-weight:600">{E(DK["today"])}</p></div>')
put('p6l8-title', dark('p6l8-title', NAVY, inner,
    f'Objective: {L["objective"]} Materials: {L["materials"]} Online: {L["online"]} Scratch set-up: share a starter project with a list called alphabet holding the letters A to Z (add each letter with the add to list block, or use the list monitor import). Scratch lists count from item 1, so letter number n (A = 0) is item n + 1. The mod block is in the Operators menu. Dark-blue Scratch blocks for lists are drawn on our slides as simple coloured shapes. '
    'Time plan: warm-up 0 to 10, explore 10 to 25, teaching 25 to 35 (click to reveal each step and answer), brain break 35 to 40, worksheet 40 to 70 with short teaching before each page and a check-together slide after it, talk time 70 to 80, exit ticket 80 to 90.'))

# ================= 2. warm1: clock jumps =================
body = h2('Warm-up: clock jumps') + stitle('Answer on your whiteboard. Which time will it be?')
jumps = [('6 o’clock', 3, 9, '9 o’clock'), ('9 o’clock', 5, 14, '2 o’clock'), ('11 o’clock', 4, 15, '3 o’clock')]
body += pin(128, 270, 420, SV(420, 420, clock(9), 'A clock showing 9 o’clock'))
rows = [('1.', 'It is 7 o’clock. 3 hours later?', '10 o’clock'), ('2.', 'It is 10 o’clock. 4 hours later?', '2 o’clock'), ('3.', 'It is 3 o’clock. 5 hours ago?', '10 o’clock'), ('4.', 'It is 8 o’clock. 12 hours later?', '8 o’clock'), ('5.', 'It is Monday. 3 days later? 10 days later?', 'Thu, Thu')]
for i, (a, b, c) in enumerate(rows): body += qrow(620, 290 + i * 118, 760, a, b, 34) + answer(1420, 290 + i * 118, 372, c)
put('p6l8-warm1', sec('p6l8-warm1', '0–5 MIN', body,
    'Minutes 0 to 5. Show each question, give thinking time, whiteboards up together, then click. 1) 10 o’clock. 2) 10 + 4 = 14, past 12, so 2 o’clock. 3) 3 − 5 = −2: go back 3 to 12, then 2 more to 10. 4) 12 hours is a full turn: back to 8. 5) Monday + 3 = Thursday. 10 days: one full week (7) and 3 more: Thursday again. Ask: "What do you do when you go past 12?" (start again at 1). This wrapping round is today\'s big idea.'))

# ================= 3. warm2 =================
qs = [(f'{i+1}.', q, a) for i, (q, a) in enumerate(DK['warmQs'])]
body = h2('Quick questions: remainders')
for i, (a, b, c) in enumerate(qs): body += qrow(128, 250 + i * 128, 1250, a, b, 34) + answer(1420, 250 + i * 128, 372, c)
put('p6l8-warm2', sec('p6l8-warm2', '5–10 MIN', body,
    'Minutes 5 to 10. Whiteboards, then click. 1) 17 = 3 × 5 + 2. 2) 30 = 4 × 7 + 2. 3) 26 ÷ 26 = 1 remainder 0. 4) 40 = 3 × 12 + 4. 5) 7 = 2 × 3 + 1 and 10 = 3 × 3 + 1. Today we call the remainder "mod": 17 mod 5 = 2. Ask: "What are the only possible remainders when you divide by 5?" (0, 1, 2, 3, 4).'))

# ================= 4. explore1 =================
lst = ''.join(f'<li>{E(x)}</li>' for x in DK['expSetup'])
body = h2('Explore: make a code strip')
body += card(chip('EXPLORE, IN PAIRS') + f'<ol style="font-size:32px;font-weight:600;padding-left:48px;display:flex;flex-direction:column;gap:6px;line-height:1.25">{lst}</ol>', extra='padding:24px 40px')
body += card(strip_svg(3, (23, 24, 25), 1560, 'Shift-3 code strip: the top row is A to Z, the bottom row starts at D. X, Y and Z are highlighted and sit above A, B and C.'), extra='padding:14px 28px')
put('p6l8-explore1', sec('p6l8-explore1', '10–15 MIN', body,
    'Minutes 10 to 15 (pairs keep going until 25). Children write A to Z on paper, then the alphabet again underneath, starting with D under A. They code their first names, swap, decode, then decode PDWK LV IXQ (MATH IS FUN). The highlighted X, Y, Z show the key moment: the bottom row runs out, so it wraps round to A, B, C. Do not explain this yet: ask "What happened at the end?" Online: send coded names privately in the chat. Finished early: invent your own shift and send a coded word with one clue.'))

# ================= 5. explore2 =================
body = h2('Explore: talk about it') + ''.join(card(p(num(f'{i+1}.', q), 40, 600, raw=True)) for i, (q, a) in enumerate(DK['expAsk']))
put('p6l8-explore2', sec('p6l8-explore2', '15–25 MIN', body, 'Minutes 15 to 25. Gather the pairs. Answers: ' + '  '.join(f'{i+1}) {a}' for i, (q, a) in enumerate(DK['expAsk'])) + ' Link back to the clock: letters are a 26-hour clock.'))

# ================= 6. teach1: clock arithmetic and mod =================
W0 = 420
base = SV(W0, W0, clock(9), 'A clock showing 9 o’clock')
ov = SV(W0, W0, clock(2, ghost=9) + clock_arc(9, 2), 'The hour hand moves 5 hours from 9 round to 2, past 12')
body = h2('Clock arithmetic: wrap round') + stitle('9 o’clock + 5 hours. Count on, then use mod.')
body += pin(128, 270, W0, base)
body += ostep(128, 270, 1, 'Count on 5 hours: 10, 11, 12, 1, 2.  The hand wraps round past 12.', ov, W0, W0, dx=W0 + 40, dy=0, tw=1664 - W0 - 40, size=32)
body += ostep(128, 270, 2, 'With adding: 9 + 5 = 14. A clock has only 12 numbers, so take away 12: 14 − 12 = 2.', None, dx=W0 + 40, dy=130, tw=1664 - W0 - 40, size=32)
body += ostep(128, 270, 3, 'In maths: 14 mod 12 = 2. “mod” means the remainder when you divide: 14 = 1 × 12 + 2.', None, dx=W0 + 40, dy=260, tw=1664 - W0 - 40, size=32)
body += soft(128, 740, 1664, 'On a clock with m numbers, n mod m is where you land after n steps. Landing on 0 is the same as landing on 12.', 32)
put('p6l8-teach1', sec('p6l8-teach1', '25–27 MIN', body,
    'Teach. Use a real clock or the picture. Click 1: the hand sweeps from 9 to 2. Click 2: the addition and subtracting a full turn. Click 3: the word "mod". Think-aloud: "' + SC['think'][0].strip('“”') + '" Say: mod is just the remainder: 14 ÷ 12 = 1 remainder 2. Note: on a real clock we write 12 where maths writes 0; both mean the top of the clock.'))

# ================= 7. we1: day ring =================
ring_base = SV(460, 460, dayring(3), 'A week as a ring of 7 days: Mon, Tue, Wed, Thu, Fri, Sat, Sun. Thursday is highlighted.')
ring_ov = SV(460, 460, dayring(3, 6), 'The ring with Thursday and then Sunday, 3 days later, highlighted')
body = h2('A week is a 7-day clock') + stitle('Today is Thursday. What day is it in 45 days?')
body += pin(128, 280, 460, ring_base)
body += ostep(128, 280, 1, 'A week wraps round after 7 days, like a clock after 12. So use mod 7.', None, dx=520, dy=0, tw=1144, size=32)
body += ostep(128, 280, 2, '45 ÷ 7 = 6 remainder 3, so 45 mod 7 = 3. Six whole weeks bring us back to Thursday.', None, dx=520, dy=115, tw=1144, size=32)
body += ostep(128, 280, 3, 'Then 3 more days: Friday, Saturday, Sunday.', ring_ov, 460, 460, dx=520, dy=230, tw=1144, size=32)
body += answer(648, 560, 1144, 'In 45 days it is Sunday')
body += soft(648, 680, 1144, 'Check: 6 × 7 = 42, and 42 + 3 = 45 ✓. Do not count today as day 1.', 32)
put('p6l8-we1', sec('p6l8-we1', '27–29 MIN', body,
    'Click through; ask the group to predict before each reveal. Think-aloud: "45 days is 6 whole weeks and 3 days. The whole weeks do nothing, because after 7 days it is the same day again. So only the remainder matters: 3 days after Thursday is Sunday." Watch for: counting today as day 1 (that gives Saturday). Ask: "What day was it 45 days ago?" (Thursday − 3 = Monday).'))

# ================= 8. try1 =================
put('p6l8-try1', qa_slide('p6l8-try1', '29–30 MIN', 'Your turn: clocks and days', 'Whiteboards. Use mod.',
    [('a', '10 o’clock + 27 hours. What time? (27 mod 12 = ?)', '1 o’clock'), ('b', 'Today is Wednesday. What day is it in 20 days?', 'Tuesday'), ('c', 'It is 2 o’clock. What time was it 5 hours ago?', '9 o’clock')],
    'Whiteboards, then click. a) 27 mod 12 = 3, 10 + 3 = 13, 13 − 12 = 1 o’clock. b) 20 mod 7 = 6, Wednesday + 6 = Tuesday (Thu, Fri, Sat, Sun, Mon, Tue). c) 2 − 5 = −3, below 0 so add 12: 9. Going backwards: if you go below the start, add a full turn.'))

# ================= 9. we2: Caesar =================
body = h2('Caesar code: letters are numbers') + stitle('Letters on a 26-hour clock: A = 0, B = 1 … Z = 25. Code ZOO with shift 5.')
body += pin(128, 300, 1664, strip_svg(5, (25, 14), 1560, 'Code strip shift 5: Z and O are highlighted on top, with their code letters E and T underneath'), None, WHITE, 20, '16px 52px')
body += step(1, 'Z = 25.  25 + 5 = 30.  There is no letter 30, so wrap round: 30 mod 26 = 4, and 4 is E.', top=560, size=32)
body += step(2, 'O = 14.  14 + 5 = 19, and 19 is T.   Second O: also T.', top=665, size=32)
body += answer(128, 790, 1664, 'ZOO becomes ETT      code number = (letter number + shift) mod 26')
put('p6l8-we2', sec('p6l8-we2', '29–31 MIN', body,
    'Click through. Think-aloud: "' + SC['think'][1].strip('“”') + '" Point out the highlighted letters on the strip: Z is above E, O above T. Ask: "Which letters wrap round with shift 5?" (V, W, X, Y, Z become A to E). Say: this is called a Caesar cipher after Julius Caesar, who used a shift of 3 to send orders. ' + PYNOTE))

# ================= 10. try2 =================
put('p6l8-try2', qa_slide('p6l8-try2', '31–32 MIN', 'Your turn: code and decode', 'Letter numbers: A = 0 … Z = 25.',
    [('a', 'Code CAT with shift 3.', 'FDW'), ('b', 'Code YES with shift 4. (Y = 24)', 'CIW'), ('c', 'Decode FRGH. It was made with shift 3.', 'CODE')],
    'Whiteboards, then click. a) C 2 + 3 = 5 = F, A 0 + 3 = 3 = D, T 19 + 3 = 22 = W: FDW. b) Y 24 + 4 = 28, 28 mod 26 = 2 = C; E 4 + 4 = 8 = I; S 18 + 4 = 22 = W: CIW (the wrap-round case). c) Decoding subtracts: F 5 − 3 = 2 = C, R 17 − 3 = 14 = O, G 6 − 3 = 3 = D, H 7 − 3 = 4 = E: CODE. Ask: Which letters go below 0 when decoding with shift 3? (A, B and C: add 26.)'))

# ================= 11. we3: decode and the Scratch machine =================
loop = [('var', 'set {n} to {(item # of (letter) in alphabet) − 1}'), ('var', 'set {m} to {(n + shift) mod 26}'), ('var', 'set {code} to {join (code) (item (m + 1) of alphabet)}')]
body = h2('Decoding: add 26 if you go below 0') + stitle('Decode AEB. It was made with shift 4.')
body += step(1, 'A = 0.  0 − 4 = −4: below 0. Add 26: −4 + 26 = 22, and 22 is W.', top=300, width=1664, size=32)
body += step(2, 'E = 4.  4 − 4 = 0, and 0 is A.      B = 1.  1 − 4 = −3, + 26 = 23, and 23 is X.', top=405, width=1664, size=32)
body += answer(128, 510, 1664, 'AEB is WAX')
body += pin(128, 610, 1100, blocks_svg(loop, 'Blocks: set n to (item number of the letter in alphabet) minus 1; set m to (n plus shift) mod 26; set code to join code and item (m plus 1) of alphabet', 24, 42), 'fade', WHITE, 24, '14px 24px')
body += pin(1280, 640, 512, p('The Scratch code machine runs these 3 blocks for each letter. Lists start at item 1, so letter n is item n + 1.', 28, 700), 'fade', SOFT, 20, '18px 24px')
put('p6l8-we3', sec('p6l8-we3', '32–34 MIN', body,
    'Click through the decoding steps, then the Scratch blocks. Think-aloud: "' + SC['think'][2].strip('“”') + '" Decoding with shift 4 is the same as coding with shift 22, because 26 − 4 = 22. The blocks run once for each letter of the message: "for each letter" is a repeat loop. Build it live from the starter project and code HELLO. ' + PYNOTE))

# ================= 12. key =================
body = h2(DK['keyHead']) + card(p(DK['keyBig'], 44, 700)) + card(p(DK['keySmall'], 38, 600, MUTED))
put('p6l8-key', sec('p6l8-key', '34–35 MIN', body, 'Say the key idea together. Common mistakes to watch for during the worksheet: (1) ' + L['mistakes'][0] + ' (2) ' + L['mistakes'][1] + ' (3) ' + L['mistakes'][2]))

# ================= 13. break =================
put('p6l8-break', dark('p6l8-break', TEAL,
    f'<p style="font-size:32px;font-weight:700;letter-spacing:4px;color:{YEL}">35–40 MIN</p><h2 style="font-family:{HF};font-size:110px;font-weight:600;line-height:1.05">Brain break</h2>'
    f'<p style="font-size:48px;font-weight:600">{E(DK["brk"])}</p><p style="font-size:36px;color:#D7EFEA">Then: a drink of water and back to the computer.</p>',
    'Five minutes. Online: children stay in view of the camera. The 12-hour sweep returns the arm to the same place: that is 12 mod 12 = 0.', '#D7EFEA'))

# ================= 14–15. ws1 =================
put('p6l8-ws1', ws_preview('p6l8-ws1', '40–50 MIN', 'Worksheet page 1: with your partner',
    [('Q1', 'Clock and calendar puzzles: hours, days, and mod.'), ('Q2', 'Caesar codes: code PIZZA, decode MYNO SC PEX. Test in Scratch.')],
    'Use the letter strip at the top of the page. A = 0.',
    'Minutes 40 to 50, in pairs. Walk around. Ask "How do you know?" before giving any help. For Q2 check pairs write the letter numbers first and wrap round with 26.'))
put('p6l8-ws1ans', check2('p6l8-ws1ans', '50–52 MIN', 'Page 1: check together', [
    ('Q1', 'a) 3 o’clock   b) 5 o’clock   c) 7 o’clock   d) Monday   e) Thursday   f) 5, 1, 22', 2),
    ('Q2a, b', 'PIZZA with shift 7 is WPGGH.   MYNO SC PEX is CODE IS FUN.', 1),
    ('Q2c', 'Shift 16: decoding by 10 is the same as coding by 26 − 10 = 16.', 1)],
    'Click each answer after a pair explains. Q1: a) 8 + 7 = 15, 15 − 12 = 3. b) 30 mod 12 = 6, 11 + 6 = 17, 17 − 12 = 5. c) 4 − 9 = −5, + 12 = 7. d) 100 mod 7 = 2 (98 = 14 weeks), Saturday + 2 = Monday. e) 30 mod 7 = 2, Saturday back 2 = Thursday. f) 29 mod 12 = 5, 50 mod 7 = 1 (49 = 7 × 7), 100 mod 26 = 22 (78 = 3 × 26). Q2a: P 15 → 22 = W, I 8 → 15 = P, Z 25 → 32 mod 26 = 6 = G, A 0 → 7 = H. Q2b: M 12 − 10 = 2 = C, Y 24 − 10 = 14 = O, N 13 − 10 = 3 = D, O 14 − 10 = 4 = E.'))

# ================= 16. teach trace =================
trace_blocks = [('var', 'set {n} to {(item # of (letter) in alphabet) − 1}'), ('var', 'set {m} to {(n + shift) mod 26}'), ('var', 'set {code} to {join (code) (item (m + 1) of alphabet)}')]
body = h2('Trace the code: SKY with shift 10') + stitle('A trace table follows the program one letter at a time.')
body += pin(128, 290, 1100, blocks_svg(trace_blocks, 'Three blocks: set n to letter number, set m to (n plus shift) mod 26, set code to join code and the letter at m plus 1', 24, 42), None, WHITE, 20, '12px 24px')
Wt = [180, 150, 200, 300, 220]
body += trow(128, 520, ['letter', 'n', 'n + 10', 'm = mod 26', 'code'], Wt, None, True, 34)
for i, (l, n_) in enumerate(zip('SKY', [18, 10, 24])):
    m = (n_ + 10) % 26
    body += trow(128, 600 + i * 78, [l, str(n_), str(n_ + 10), str(m), ABC[m]], Wt, 'rise', False, 34)
body += answer(128, 850, 1664, 'The program says CUI (SKY: Y gives 34, 34 mod 26 = 8, which is I)')
put('p6l8-teachtrace', sec('p6l8-teachtrace', '52–54 MIN', body,
    'Teach before worksheet page 2 (Q3 traces WAY with shift 5; this is a different word). Click to add each row: S = 18 → 28 → 2 = C; K = 10 → 20 = U; Y = 24 → 34 → 8 = I. Ask: "Which letter needed the mod?" (S and Y, because the number went past 25). A trace table is how programmers check code by hand.'))

# ================= 17. teach crack =================
body = h2('Crack the code') + card(p('YMNX NX KZS.   No shift given. How do we crack it?', 40, 700), extra='padding:24px 40px')
body += step(1, 'Look for short words. NX looks like IS (the same letters appear in YMNX).', top=400, size=32)
body += step(2, 'N → I: N = 13 and I = 8. Shift back 5 (13 − 5 = 8). Try S: X = 23 − 5 = 18 = S ✓', top=495, size=32)
body += step(3, 'Decode every letter with shift 5: YMNX is THIS, NX is IS, KZS is FUN.', top=590, size=32)
body += answer(128, 700, 1664, 'THIS IS FUN')
body += soft(128, 800, 1664, 'Only 25 shifts are possible. A computer can try them all in a blink.', 30)
put('p6l8-teachcrack', sec('p6l8-teachcrack', '54–55 MIN', body,
    'Teach before worksheet page 2 (Q4 cracks a different message by finding a repeated 3-letter word). Think-aloud: "A short word is the best clue. A two-letter word that makes sense is IS, IT, IN, AT, OF. If NX is IS, N went to I, so the shift is 5 backwards. Then I test it on the other words." Show the crack program (Python): for shift in range(1, 26) prints every shift: the one that reads as English wins. In Scratch: repeat 25, change shift by 1, decode and say. This is called brute force.'))

# ================= 18. teach combine =================
body = h2('Two shifts in a row') + card(p('Code with shift 15, then code the result with shift 15. What is the same as one shift?', 38, 700), extra='padding:24px 40px')
body += step(1, 'Take A (0): shift 15 gives 15 (P). Shift 15 again: 30, and 30 mod 26 = 4 (E).', top=410, size=32)
body += step(2, 'So A became E: that is one shift of 4.  Shifts add up: 15 + 15 = 30, and 30 mod 26 = 4.', top=515, size=32)
body += step(3, 'Shifts add up like jumps on a 26-hour clock. Shift 26 is a full turn: it changes nothing.', top=620, size=32)
body += answer(128, 740, 1664, 'Shift 15 then shift 15 is shift 4')
put('p6l8-teachcomb', sec('p6l8-teachcomb', '55–56 MIN', body,
    'Teach before worksheet page 2 (Q5 combines other shifts). Use a letter to show it: A → P → E, and A shift 4 → E ✓. Say: a shift is a jump on the clock, and two jumps add. Ask: "What shift undoes shift 15?" (11, since 15 + 11 = 26).'))

# ================= 19–20. ws2 =================
put('p6l8-ws2', ws_preview('p6l8-ws2', '56–66 MIN', 'Worksheet page 2: on your own',
    [('Q3', 'Trace the code machine in a table: WAY with shift 5.'), ('Q4', 'Crack Mei’s secret message.'), ('Q5', 'Two shifts in a row.')],
    'Finished early? Stretch and Challenge come next.',
    'Children work alone (they may test in Scratch). Note who needs a short catch-up next lesson.'))
put('p6l8-ws2ans', check2('p6l8-ws2ans', '66–70 MIN', 'Page 2: check together', [
    ('Q3', 'W 22, 27, 1, B   A 0, 5, 5, F   Y 24, 29, 3, D   It says BFD.', 1),
    ('Q4', 'BPM is THE.  T to B is shift 8.  THE KEY IS UNDER THE MAT', 2),
    ('Q5', 'a) 15   b) 5   c) The original message: 9 + 17 = 26   d) 13', 1)],
    'Click each answer after a child explains. Q4: the repeated word BPM; "the" is the most common 3-letter word; T = 19, B = 1: 19 + 8 = 27, 27 mod 26 = 1. Decode every letter by 8 back (or forward 18): BPM SMG QA CVLMZ BPM UIB is THE KEY IS UNDER THE MAT. Q5: a) 6 + 9 = 15. b) 19 + 12 = 31, 31 mod 26 = 5. c) 9 + 17 = 26, a full turn. d) Shift 13 used twice is 26: ROT13 is a real code, and coding twice decodes it.'))

# ================= 21. stretch (3 new) =================
st = QB['stretch'][4:7]
body = h2('Stretch') + ''.join(card(p(num(f'{i+1}.', x['q']), 34, 600, raw=True), extra='padding:26px 40px') for i, x in enumerate(st))
put('p6l8-stretch', sec('p6l8-stretch', 'For early finishers', body, 'For children who finish early (not on the worksheet). Answers: ' + '  '.join(f'{i+1}) {x["a"]}' for i, x in enumerate(st))))

# ================= 22. challenge =================
ch = [QB['challenge'][0], QB['challenge'][1]]
body = h2('Challenge') + ''.join(card(p(num(f'{i+1}.', x['q']), 36, 600, raw=True)) for i, x in enumerate(ch))
put('p6l8-challenge', sec('p6l8-challenge', 'Challenge', body, 'Pairs try first, then use the "see it" slide if stuck, then the walk-through. Answers: ' + '  '.join(f'{i+1}) {x["a"]}' for i, x in enumerate(ch))))

# ================= 23. challenge: see it =================
def mulstrip(picks, w=720, y0=44):
    cw = w / 13; s = ''
    for r in range(2):
        for i in range(13):
            idx = i + 13 * r; x = i * cw; y = y0 + r * 70
            s += f'<rect x="{x:.1f}" y="{y}" width="{cw:.1f}" height="56" fill="{YEL if idx in picks else WHITE}" stroke="{NAVY}" stroke-width="3"/>' + T(x + cw / 2, y + 28, ABC[idx], 26) + T(x + cw / 2, y + 51, idx, 24, MUTED, 600)
    return s
ex = ''
for i, (lbl, n_) in enumerate([('A', 0), ('N', 13), ('B', 1), ('O', 14)]):
    x = 100 + i * 170
    ex += f'<rect x="{x-70}" y="210" width="150" height="90" rx="14" fill="{SKY}" stroke="{NAVY}" stroke-width="4"/>' + T(x + 5, 245, f'{lbl} = {n_}', 28) + T(x + 5, 282, f'× 2 = {n_*2}', 28, TEAL, 800)
dg = T(360, 30, 'Mei’s code: × 2, then mod 26', 30, TEAL, 800) + mulstrip((0, 13, 1, 14)) + ex + T(360, 350, 'What comes out for N? And for A?', 30, NAVY, 700)
dg2 = T(360, 30, 'Ben’s code: × 3, then mod 26', 30, TEAL, 800) + mulstrip((2, 0, 1))
for i, (lbl, n_) in enumerate([('C', 2), ('A', 0), ('B', 1)]):
    x = 150 + i * 190
    dg2 += f'<rect x="{x-70}" y="210" width="160" height="90" rx="14" fill="{SKY}" stroke="{NAVY}" stroke-width="4"/>' + T(x + 10, 245, f'{lbl} = {n_}', 28) + T(x + 10, 282, f'× 3 = {n_*3}', 28, TEAL, 800)
dg2 += T(360, 350, 'Does any code letter appear twice?', 30, NAVY, 700)
body = h2('Challenge: see it', 60) + '<div style="display:flex;gap:32px;align-items:flex-start">'
body += card(f'<p style="font-size:30px;font-weight:700;color:{TEAL}">Q1: the × 2 code</p>' + SV(720, 380, dg, 'The alphabet as numbers 0 to 25 in two rows. Mei’s code multiplies by 2 then takes mod 26. Boxes show A = 0, N = 13, B = 1, O = 14 each times 2.', 'width:100%;height:auto'), extra='flex:1;min-width:0;padding:20px 24px')
body += card(f'<p style="font-size:30px;font-weight:700;color:{TEAL}">Q2: the × 3 code</p>' + SV(720, 380, dg2, 'The alphabet as numbers 0 to 25 in two rows. Ben’s code multiplies by 3 then takes mod 26. Boxes show C = 2, A = 0 and B = 1 each times 3.', 'width:100%;height:auto'), extra='flex:1;min-width:0;padding:20px 24px')
body += '</div>'
put('p6l8-chdiag', sec('p6l8-chdiag', 'Challenge', body, 'Show after pairs have tried, or if they are stuck. The pictures show the problem, not the answer. Q1: "What is 13 × 2? What letter is number 26 mod 26?" Q2: "Fill in the three code letters. Could two different letters ever give the same number?"'))

# ================= 24. chwalk =================
body = h2('Challenge: walk-through') + pin(128, 250, 800, p('Q1: the × 2 code', 34, 800, TEAL))
for i, t in enumerate(['A = 0, and 0 × 2 = 0, so A becomes A.', 'N = 13, and 13 × 2 = 26, and 26 mod 26 = 0: A again!', 'Two letters give A, so a code A could be A or N.', 'Every code number is even: only 13 code letters used.']): body += pin(128, 330 + i * 110, 800, p(t, 30), 'rise', WHITE)
body += pin(992, 250, 800, p('Q2: the × 3 code', 34, 800, TEAL))
for i, t in enumerate(['C = 2: 2 × 3 = 6 = G.   A = 0: 0 = A.', 'B = 1: 1 × 3 = 3 = D.   So CAB is GAD.', 'Could two letters match? That needs 3 × (difference) to be a multiple of 26.', 'It never works: 3 and 26 share no factor. All 26 differ ✓']): body += pin(992, 330 + i * 110, 800, p(t, 30), 'rise', WHITE)
put('p6l8-chwalk', sec('p6l8-chwalk', 'Challenge', body,
    'Use after pairs have tried. Q1: doubling loses information: every code number is even, so only 13 different code letters can appear and each stands for two letters (n and n + 13). That is why a code must be able to be undone: the shift code always can. Q2: ×3 works because 3 and 26 share no common factor; ×13 or ×2 do not. Link: the clock with jumps of 5 (visits all 12 numbers) and jumps of 4 (does not) from the question bank.'))

# ================= 25. talk =================
body = h2('Talk time') + card(chip('TALK TIME', YEL, NAVY) + p(SC['talk'][0].strip('“”'), 40, 600)) + card(p('Sentence starters:', 34, 400, MUTED) + p('“I noticed that …”   “I tested it by …”   “I know because …”', 38, 600))
put('p6l8-talk', sec('p6l8-talk', '70–80 MIN', body, 'Minutes 70 to 80. Pairs talk for 2 minutes, then share. Second question if time: ' + SC['talk'][1].strip('“”') + ' Answer: ' + SC['talkAns'] + ' Praise the reasons, not only the answers.'))

# ================= 26. exit =================
body = h2('Exit ticket') + card(chip('EXIT TICKET') + p(L['exit']['q'], 46, 600)) + card(p('Write your answer on a slip of paper. Show it to your tutor. Then collect your stamp in your inquiry journal.', 34, 400))
put('p6l8-exit', sec('p6l8-exit', '80–90 MIN', body, f'Minutes 80 to 90. Answer: {L["exit"]["a"]} Extension: {L["extension"]}'))

order = ['p6l8-title', 'p6l8-warm1', 'p6l8-warm2', 'p6l8-explore1', 'p6l8-explore2', 'p6l8-teach1', 'p6l8-we1', 'p6l8-try1', 'p6l8-we2', 'p6l8-try2', 'p6l8-we3', 'p6l8-key', 'p6l8-break',
         'p6l8-ws1', 'p6l8-ws1ans', 'p6l8-teachtrace', 'p6l8-teachcrack', 'p6l8-teachcomb', 'p6l8-ws2', 'p6l8-ws2ans', 'p6l8-stretch', 'p6l8-challenge', 'p6l8-chdiag', 'p6l8-chwalk', 'p6l8-talk', 'p6l8-exit']
assert set(order) == set(S), set(order) ^ set(S)
for f in os.listdir(os.path.join(D, 'slides')):
    if f.endswith('.html') and f[:-5] not in S: os.remove(os.path.join(D, 'slides', f))
for i, h in S.items(): open(os.path.join(D, 'slides', i + '.html'), 'w').write(h)
deck = {'v': 4, 'createdOnFiles': {'v': 1, 'at': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}, 'lists': 'css',
        'title': 'Math Inquirers P6: Lesson 8 – Secret Codes', 'order': order, 'cover': 'p6l8-title',
        'sections': {'s1': {'description': 'Warm-up and explore', 'start': 'p6l8-title'}, 's2': {'description': 'Teach: clock arithmetic and Caesar codes', 'start': 'p6l8-teach1'},
                     's3': {'description': 'Worksheet with teaching before each page', 'start': 'p6l8-break'}, 's4': {'description': 'Stretch, challenge, talk and exit', 'start': 'p6l8-stretch'}},
        'faces': {'fredoka': {'family': 'Fredoka', 'href': 'https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&display=swap'},
                  'nunito-sans': {'family': 'Nunito Sans', 'href': 'https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@400;600;700&display=swap'}},
        'designSystems': []}
json.dump(deck, open(os.path.join(D, 'deck.json'), 'w'), indent=1, ensure_ascii=False)
print(len(order), 'slides written to', os.path.normpath(D))
