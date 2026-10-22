"""Math Inquirers Level 6, Lesson 6: Fair or Unfair?. Writes split/p6l6/project (deck.json + slides/*.html).
Content strings (warm-up questions, explore, key idea, question bank, exit) are read from p6/content/l6.js so the deck matches the workbook."""
import json, os, sys, re, subprocess, math, datetime
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, H)
import slidekit
slidekit.FOOT = 'Math Inquirers Level 6  •  Notice it. Test it. Explain why.'
from slidekit import *
N = 6; PRE = f'p6l{N}'
D = os.path.join(H, '..', 'split', PRE, 'project'); os.makedirs(os.path.join(D, 'slides'), exist_ok=True)
C = json.loads(subprocess.run(['node', '-e', f"const c=require({json.dumps(os.path.join(H, '..', 'p6', 'content', f'l{N}.js'))});console.log(JSON.stringify({{lesson:c.lesson,script:c.script,deck:c.deck,qbank:c.qbank}}))"], capture_output=True, text=True, check=True).stdout)
L, SC, DK, QB = C['lesson'], C['script'], C['deck'], C['qbank']
RED = '#D64545'
S = {}
def put(sid, html): S[sid] = html

# ---------- code blocks in our own style (same shapes as the workbook) ----------
BK = {'hat': (RED, WHITE), 'ctrl': (YEL, NAVY), 'var': (TEAL, WHITE), 'look': (SKY, NAVY)}
def blocks_svg(nodes, label, fs=28):
    h = round(fs * 1.9); stp = round(fs * 1.2); cw = fs * 0.6; F = 'Arial, sans-serif'
    segs = lambda t: [s for s in re.split(r'(\[[^\]]*\])', t) if s.strip()]
    pillW = lambda c: fs * 5 if c == '?' else len(c) * cw + fs
    textW = lambda t: sum((pillW(s[1:-1]) if s[0] == '[' else len(s.strip()) * cw) + fs * 0.35 for s in segs(t))
    out = []; mx = [0]
    def txt(x, y, t, fg):
        cx = x; s = ''
        for g in segs(t):
            if g[0] == '[':
                c = g[1:-1]; w = pillW(c); ph = h - 14
                s += f'<rect x="{cx:.1f}" y="{y - ph / 2:.1f}" width="{w:.1f}" height="{ph}" rx="{ph / 2}" fill="{WHITE}" stroke="{NAVY}" stroke-width="2.5"{" stroke-dasharray=\"8 6\"" if c == "?" else ""}/>'
                if c != '?': s += f'<text x="{cx + w / 2:.1f}" y="{y + fs * 0.36:.1f}" font-size="{fs}" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="{F}">{E(c)}</text>'
                cx += w + fs * 0.35
            else:
                t2 = g.strip(); s += f'<text x="{cx:.1f}" y="{y + fs * 0.36:.1f}" font-size="{fs}" font-weight="700" fill="{fg}" font-family="{F}">{E(t2)}</text>'; cx += len(t2) * cw + fs * 0.35
        mx[0] = max(mx[0], cx); return s
    def lay(lst, x, y):
        for n in lst:
            kind, text = n[0], n[1]; kids = n[2] if len(n) > 2 else None; els = n[3] if len(n) > 3 else None
            bg, fg = BK[kind]; w = max(textW(text) + fs * 1.2, fs * 5)
            if kids is None:
                out.append(f'<rect x="{x}" y="{y}" width="{w:.1f}" height="{h}" rx="{fs * 0.9 if kind == "hat" else 8}" fill="{bg}" stroke="{NAVY}" stroke-width="3"/>' + txt(x + fs * 0.6, y + h / 2, text, fg)); mx[0] = max(mx[0], x + w); y += h
            else:
                y0 = y; idx = len(out); out.append('')
                labels = txt(x + fs * 0.6, y0 + h / 2, text, fg); y += h; y = lay(kids, x + stp, y); yE = None
                if els is not None: yE = y; labels += txt(x + fs * 0.6, y + h / 2, 'else', fg); y += h; y = lay(els, x + stp, y)
                hb = round(h * 0.55); wb = fs * 5
                pts = [(x, y0), (x + w, y0), (x + w, y0 + h), (x + stp, y0 + h)]
                if els is not None: pts += [(x + stp, yE), (x + wb, yE), (x + wb, yE + h), (x + stp, yE + h)]
                pts += [(x + stp, y), (x + wb, y), (x + wb, y + hb), (x, y + hb)]
                out[idx] = f'<polygon points="{" ".join(f"{a:.1f},{b:.1f}" for a, b in pts)}" fill="{bg}" stroke="{NAVY}" stroke-width="3" stroke-linejoin="round"/>' + labels
                y += hb; mx[0] = max(mx[0], x + w)
        return y
    Hh = math.ceil(lay(nodes, 3, 3) + 3); W = math.ceil(mx[0] + 6)
    return f'<svg aria-label="{E(label)}" viewBox="0 0 {W} {Hh}" xmlns="http://www.w3.org/2000/svg" style="width:{W}px;height:{Hh}px;flex:none">{"".join(out)}</svg>'

def ptext(t, size=36, weight=700, color=None): return p(t, size, weight, color)
def box(left, top, width, text, build='rise', bg=WHITE, size=34):
    return pin(left, top, width, p(text, size, 700), build, bg, 20, '18px 26px')
def checkrows(sid, time, title, rows, notes, size=32, lw=170):
    body = h2(title); top = 245
    for a, b in rows:
        lines = max(1, math.ceil(len(b) * size * 0.52 / (1664 - lw - 52)))
        hgt = lines * size * 1.25 + 36
        body += pin(128, top, lw - 20, f'<p style="font-size:34px;font-weight:800;color:{TEAL}">{E(a)}</p>', None, WHITE, 20, '16px 22px')
        body += pin(128 + lw, top, 1664 - lw, f'<p style="font-size:{size}px;font-weight:800;line-height:1.25">{E(b)}</p>', 'pop', YEL, 20, '18px 26px')
        top += hgt + 22
    return sec(sid, time, body, notes)
def numcards(sid, time, title, items, notes, size=38):
    return sec(sid, time, h2(title) + ''.join(card(p(f'<span style="color:{TEAL}">{a}</span>  {E(b)}', size, 600, raw=True)) for a, b in items), notes)

# ---------- 1 title ----------
notes = (f"Objective: {L['objective']} Materials: {L['materials']} Online: {L['online']} "
         "Time plan: warm-up 0 to 10, explore 10 to 25 (play the Dice Race, then pool the results), teaching 25 to 35 (click to reveal each step and answer), brain break 35 to 40, "
         "worksheet 40 to 75 with short teaching before each page and a check-together slide after it, talk time 75 to 82, exit ticket 82 to 90. "
         "Before the lesson: have the Explore game program ready to share (Scratch, below on the teach-code slide) and a dice program for children without dice.")
body = (f'<p style="font-size:32px;font-weight:700;letter-spacing:4px;color:{YEL}">LESSON {N}  •  WEEK 3</p>'
        f'<h1 style="font-family:{HF};font-size:128px;font-weight:600;line-height:1.05">{E(L["title"])}</h1>'
        f'<p style="font-size:44px;color:#C9D4EC">Probability  •  random numbers</p>'
        f'<div style="background:#26385F;border-radius:24px;padding:40px;display:flex;flex-direction:column;gap:12px"><p style="font-size:28px;font-weight:700;letter-spacing:3px;color:{YEL}">TODAY WE WILL</p><p style="font-size:44px;font-weight:600">{E(DK["today"])}</p></div>')
put(f'{PRE}-title', f'<section id="{PRE}-title" data-transition="fade" style="background:{NAVY};color:{CREAM};font-family:{BF};padding:128px 128px 160px;display:flex;flex-direction:column;justify-content:center;gap:36px">\n{body}\n<p style="position:absolute;left:128px;bottom:64px;width:1400px;font-size:24px;color:#B7C3DD">{E(slidekit.FOOT)}</p>\n<aside>{E(notes)}</aside>\n</section>\n')

# ---------- 2 warm-up: where on the line ----------
ev = [('A', 'Roll a 7 on a normal dice', 0, '0'), ('B', 'Flip a coin: heads', 1 / 2, '1/2'), ('C', 'Roll a number less than 5', 2 / 3, '4/6 = 2/3'),
      ('D', 'Pick a vowel from the letters S I N G A P O R E', 4 / 9, '4/9'), ('E', 'Roll a number from 1 to 6', 1, '1'), ('F', 'Pick the 1 red card from 10 cards', 1 / 10, '1/10')]
body = h2('Warm-up: where on the line?') + p('Pairs place each card on the line and give its fraction. Take your time.', 32, 600, MUTED)
CWD = 533
for i, (l, t, v, f) in enumerate(ev):
    Lx = 128 + (i % 3) * (CWD + 32); T = 280 + (i // 3) * 150
    body += pin(Lx, T, CWD, f'<p style="font-size:32px;font-weight:700;line-height:1.2"><span style="color:{TEAL};font-family:{HF};font-size:40px">{l}</span>  {E(t)}</p>', None, WHITE, 20, '16px 22px', f'box-sizing:border-box;height:130px;border:3px solid {NAVY}')
X0, X1 = 230, 1690
line = (f'<svg aria-label="Probability line from 0 (impossible) to 1 (certain)" viewBox="0 0 1664 130" xmlns="http://www.w3.org/2000/svg" style="width:1664px;height:130px;flex:none">'
        f'<line x1="{X0 - 128}" y1="80" x2="{X1 - 128}" y2="80" stroke="{NAVY}" stroke-width="6"/>')
for v, lab in [(0, '0  impossible'), (0.5, '1/2  even chance'), (1, '1  certain')]:
    x = X0 - 128 + v * (X1 - X0); line += f'<line x1="{x}" y1="60" x2="{x}" y2="100" stroke="{NAVY}" stroke-width="6"/><text x="{x}" y="40" font-size="30" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="Nunito Sans, Arial">{lab}</text>'
body += pin(128, 590, 1664, line + '</svg>', None)
for i, (l, t, v, f) in enumerate(ev):
    x = X0 + v * (X1 - X0); below = i in (1, 5)  # alternate label rows for markers that sit close together
    mk = (f'<svg aria-label="Marker {l} at {f}" viewBox="0 0 160 170" xmlns="http://www.w3.org/2000/svg" style="width:160px;height:170px;flex:none"><circle cx="80" cy="36" r="32" fill="{YEL}" stroke="{NAVY}" stroke-width="4"/>'
          f'<text x="80" y="49" font-size="36" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="Fredoka, Arial">{l}</text><text x="80" y="{150 if below else 106}" font-size="30" font-weight="800" text-anchor="middle" fill="{TEAL}" font-family="Nunito Sans, Arial">{E(f)}</text></svg>')
    body += f'<div data-build-in="pop" style="position:absolute;left:{x - 80:.0f}px;top:{670 - 36 + 0:.0f}px;width:160px">{mk}</div>'
put(f'{PRE}-warm1', sec(f'{PRE}-warm1', '0–5 MIN', body,
    'Minutes 0 to 5. ' + DK['warmGame'] + ' Pairs agree on a spot and a fraction for each card (no timer), then click to drop the marker (markers appear A to F). '
    'Answers: A 0 (impossible). B 1/2. C 4/6 = 2/3 (1, 2, 3, 4 out of 6). D 4/9 (I, A, O, E are 4 of the 9 letters). E 1 (certain). F 1/10. '
    'Ask: "Is D more or less than an even chance?" (4/9 is a little less than 1/2, because 4.5/9 would be 1/2.) "Can a probability be 6/5?" (No: never more than 1, never less than 0.) '
    'Key words for today: equally likely outcomes, fair, expect.'))

# ---------- 3 quick questions ----------
qs = DK['warmQs']
body = h2('Quick questions') + ''.join(qrow(128, 240 + i * 128, 1250, f'{i + 1}.', q, 38) for i, (q, a) in enumerate(qs)) + ''.join(answer(1420, 240 + i * 128, 372, a.split(' (')[0]) for i, (q, a) in enumerate(qs))
put(f'{PRE}-warm2', sec(f'{PRE}-warm2', '5–10 MIN', body, 'Minutes 5 to 10. Fraction warm-up: we use all of these today. Whiteboards, then click. Answers: ' + '  '.join(f'{i + 1}) {a}' for i, (q, a) in enumerate(qs)) + '. For 4, compare using a common denominator of 36.'))

# ---------- 4 explore 1 ----------
def die(x, y, n, s=110, col=WHITE):
    P = {1: [(0, 0)], 2: [(-1, -1), (1, 1)], 3: [(-1, -1), (0, 0), (1, 1)], 4: [(-1, -1), (1, -1), (-1, 1), (1, 1)], 5: [(-1, -1), (1, -1), (0, 0), (-1, 1), (1, 1)], 6: [(-1, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (1, 1)]}[n]
    return f'<rect x="{x}" y="{y}" width="{s}" height="{s}" rx="{s * 0.18:.0f}" fill="{col}" stroke="{NAVY}" stroke-width="4"/>' + ''.join(f'<circle cx="{x + s / 2 + dx * s * 0.27:.0f}" cy="{y + s / 2 + dy * s * 0.27:.0f}" r="{s * 0.08:.0f}" fill="{NAVY}"/>' for dx, dy in P)
esv = f'<svg aria-label="Two dice showing 3 and 5, player A totals 2, 3, 4, 10, 11, 12 and player B totals 5 to 9, and a tally chart" viewBox="0 0 700 560" xmlns="http://www.w3.org/2000/svg" style="width:700px;height:560px;flex:none">'
esv += die(160, 10, 3, 120, '#F2A7A7') + die(330, 10, 5, 120, SKY) + f'<text x="520" y="90" font-size="40" font-weight="700" fill="{NAVY}" font-family="Fredoka, Arial">= 8</text>'
esv += f'<rect x="10" y="170" width="330" height="170" rx="18" fill="{SOFT}" stroke="{NAVY}" stroke-width="4"/><text x="175" y="220" font-size="34" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="Fredoka, Arial">Player A</text><text x="175" y="280" font-size="32" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="Nunito Sans, Arial">2  3  4</text><text x="175" y="322" font-size="32" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="Nunito Sans, Arial">10  11  12</text>'
esv += f'<rect x="360" y="170" width="330" height="170" rx="18" fill="{SKY}" stroke="{NAVY}" stroke-width="4"/><text x="525" y="220" font-size="34" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="Fredoka, Arial">Player B</text><text x="525" y="292" font-size="32" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="Nunito Sans, Arial">5  6  7  8  9</text>'
esv += f'<rect x="10" y="370" width="680" height="180" rx="18" fill="{WHITE}" stroke="{NAVY}" stroke-width="4"/><line x1="350" y1="370" x2="350" y2="550" stroke="{NAVY}" stroke-width="3"/><text x="180" y="420" font-size="32" font-weight="700" text-anchor="middle" fill="{TEAL}" font-family="Nunito Sans, Arial">A wins</text><text x="520" y="420" font-size="32" font-weight="700" text-anchor="middle" fill="{TEAL}" font-family="Nunito Sans, Arial">B wins</text>'
for k in range(2): esv += ''.join(f'<line x1="{60 + k * 340 + j * 22}" y1="450" x2="{60 + k * 340 + j * 22}" y2="510" stroke="{NAVY}" stroke-width="5"/>' for j in range(4)) + f'<line x1="{50 + k * 340}" y1="500" x2="{140 + k * 340}" y2="458" stroke="{NAVY}" stroke-width="5"/>'
esv += '</svg>'
steps = ''.join(f'<li>{E(x)}</li>' for x in DK['expSetup'])
body = h2('Explore: the Dice Race') + (f'<div style="display:flex;gap:32px;align-items:flex-start">'
        f'<div style="background:{WHITE};border-radius:24px;padding:26px 34px;display:flex;flex-direction:column;gap:12px;flex:1;min-width:0">{chip("EXPLORE")}<ol style="font-size:32px;font-weight:600;padding-left:44px;display:flex;flex-direction:column;gap:12px;line-height:1.3;margin:0">{steps}</ol></div>'
        f'<div style="background:{WHITE};border-radius:24px;padding:20px;flex:none">{esv.replace("width:700px;height:560px", "width:620px;height:496px")}</div></div>')
put(f'{PRE}-explore1', sec(f'{PRE}-explore1', '10–15 MIN', body,
    'Minutes 10 to 25 (this slide 10 to 15). ' + L['explore'] + ' Predict first: ' + SC['predict'][0] + ' Hints: ' + ' '.join(SC['exploreHints']) + ' Online: ' + L['online'] +
    ' While pairs play, add up the class tallies on a shared slide or in the chat. Expect B to win about 2 rounds in every 3, but a single pair\'s 20 rounds can easily come out level or even favour A: that is why we pool the results.'))

# ---------- 5 explore 2 ----------
body = h2('Explore: talk about it') + ''.join(card(p(f'<span style="color:{TEAL}">{i + 1}.</span>  {E(q)}', 40, 600, raw=True), extra='padding:30px 40px') for i, (q, a) in enumerate(DK['expAsk']))
put(f'{PRE}-explore2', sec(f'{PRE}-explore2', '15–25 MIN', body, 'Minutes 15 to 25. Show the pooled tallies. Answers: ' + ' '.join(f'{i + 1}) {a}' for i, (q, a) in enumerate(DK['expAsk'])) + ' Do not reveal the 36-outcome table yet: it comes in the teaching. Ask: "If a pair got A 11, B 9, does that prove A is luckier?" (No: 20 games is a small sample.)'))

# ---------- 6 teach 1: probability as a fraction ----------
dsv = f'<svg aria-label="The six faces of a dice, with 5 and 6 highlighted" viewBox="0 0 1100 150" xmlns="http://www.w3.org/2000/svg" style="width:1100px;height:150px;flex:none">' + ''.join(die(10 + i * 180, 15, i + 1, 120, YEL if i >= 4 else WHITE) for i in range(6)) + '</svg>'
body = h2('Probability is a fraction') + card(p('P(event)  =  number of ways it can happen  ÷  number of equally likely outcomes', 40, 800))
body += pin(128, 420, 1100, dsv, None)
body += box(128, 600, 1664, 'Roll a dice. P(more than 4)?  5 or 6: 2 ways out of 6.  P = 2/6 = 1/3', 'rise', WHITE, 36)
body += box(128, 720, 1664, '0 means impossible. 1 means certain. Every probability is between 0 and 1.', 'rise', SOFT, 34)
put(f'{PRE}-teach1', sec(f'{PRE}-teach1', '25–27 MIN', body, 'Teach. Think-aloud: ' + SC['think'][0] + ' Stress EQUALLY LIKELY: "Each face of a fair dice has the same chance. That is why we can just count." Ask: "Is P(win the lottery) = 1/2 because you either win or you don\'t?" (No: the two outcomes are not equally likely.)'))

# ---------- 7 worked example: spinner ----------
def spinner6():
    cols = [SKY, YEL, SKY, RED, SKY, YEL]; labs = ['B', 'Y', 'B', 'R', 'B', 'Y']; cx = cy = 190; r = 170
    s = f'<svg aria-label="Spinner with 6 equal parts: 3 blue, 2 yellow, 1 red" viewBox="0 0 380 380" xmlns="http://www.w3.org/2000/svg" style="width:380px;height:380px;flex:none">'
    for i in range(6):
        a0 = math.radians(i * 60 - 90); a1 = math.radians((i + 1) * 60 - 90); am = (a0 + a1) / 2
        s += f'<path d="M{cx},{cy} L{cx + r * math.cos(a0):.1f},{cy + r * math.sin(a0):.1f} A{r},{r} 0 0 1 {cx + r * math.cos(a1):.1f},{cy + r * math.sin(a1):.1f} Z" fill="{cols[i]}" stroke="{NAVY}" stroke-width="4"/>'
        s += f'<text x="{cx + 115 * math.cos(am):.1f}" y="{cy + 115 * math.sin(am) + 14:.1f}" font-size="40" font-weight="700" text-anchor="middle" fill="{WHITE if cols[i] == RED else NAVY}" font-family="Fredoka, Arial">{labs[i]}</text>'
    return s + f'<line x1="{cx}" y1="{cy}" x2="{cx + 30}" y2="{cy - 48}" stroke="{NAVY}" stroke-width="10" stroke-linecap="round"/><circle cx="{cx}" cy="{cy}" r="14" fill="{NAVY}"/></svg>'
body = h2('Worked example: a spinner') + pin(128, 240, 380, spinner6(), None)
body += step(1, '6 equal parts, so 6 equally likely outcomes.', left=560, top=250, width=1232, size=36)
body += step(2, 'Yellow is 2 parts:  P(yellow) = 2/6 = 1/3.', left=560, top=370, width=1232, size=36)
body += step(3, 'Spin 600 times: expect 1/3 × 600 = 200 yellows.', left=560, top=490, width=1232, size=36)
body += step(4, 'ABOUT 200, not exactly: each spin is random.', left=560, top=610, width=1232, size=36)
body += pin(560, 750, 1232, p('Expected number = probability × number of tries', 36, 800), 'pop', YEL, 20, '16px 26px')
put(f'{PRE}-we1', sec(f'{PRE}-we1', '27–28 MIN', body, 'Click through. Ask before step 2: "What fraction is yellow?" Before step 3: "If we spin 600 times, how many yellows should we expect?" Then: "Will it be exactly 200?" Collect a few guesses; we test this with code in a moment. P(blue) = 3/6 = 1/2, P(red) = 1/6: the three add up to 1.'))

# ---------- 8 try 1 ----------
put(f'{PRE}-try1', try_slide(f'{PRE}-try1', '28–29 MIN', 'Your turn: whiteboards', 'A bag has 2 red, 3 green and 5 blue counters. Simplest form.',
    [('a', 'P(green)?', '3/10'), ('b', 'P(not blue)?', '5/10 = 1/2'), ('c', 'Roll a dice. P(prime number)?', '3/6 = 1/2')],
    'Whiteboards. a) 3 out of 10. b) not blue = red or green = 5 out of 10 = 1/2 (or 1 − 5/10). c) 2, 3 and 5 are prime (1 is not prime): 3/6 = 1/2.', size=38))

# ---------- 9 teach two dice ----------
def sum_table(hi=None, layer=False):
    c = 66; x0 = 80; y0 = 66
    s = f'<svg aria-label="Table of totals for a red die and a blue die{" with the 7s highlighted" if hi else ""}" viewBox="0 0 560 540" xmlns="http://www.w3.org/2000/svg" style="width:560px;height:540px;flex:none">'
    if not layer:
        s += f'<text x="{x0 + 3 * c}" y="26" font-size="26" font-weight="700" text-anchor="middle" fill="{TEAL}" font-family="Nunito Sans, Arial">blue die</text><text x="22" y="{y0 + 3 * c}" font-size="26" font-weight="700" text-anchor="middle" fill="{RED}" font-family="Nunito Sans, Arial" transform="rotate(-90 22 {y0 + 3 * c})">red die</text>'
        for i in range(6):
            s += f'<rect x="{x0 + i * c}" y="{y0 - 34}" width="{c}" height="34" fill="{SKY}" stroke="{NAVY}" stroke-width="2"/><text x="{x0 + i * c + c / 2}" y="{y0 - 8}" font-size="26" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="Nunito Sans, Arial">{i + 1}</text>'
            s += f'<rect x="{x0 - 40}" y="{y0 + i * c}" width="40" height="{c}" fill="#F2A7A7" stroke="{NAVY}" stroke-width="2"/><text x="{x0 - 20}" y="{y0 + i * c + 43}" font-size="26" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="Nunito Sans, Arial">{i + 1}</text>'
    for r in range(6):
        for k in range(6):
            t = r + k + 2
            if layer and t != hi: continue
            s += f'<rect x="{x0 + k * c}" y="{y0 + r * c}" width="{c}" height="{c}" fill="{YEL if layer else WHITE}" stroke="{NAVY}" stroke-width="2"/><text x="{x0 + k * c + c / 2}" y="{y0 + r * c + 43}" font-size="30" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="Nunito Sans, Arial">{t}</text>'
    return s + '</svg>'
body = h2('Two dice: 36 equally likely outcomes', 64) + pin(128, 220, 560, sum_table(), None) + pin(128, 220, 560, sum_table(7, True), 'fade')
body += box(740, 240, 1052, '6 outcomes for the red die × 6 for the blue = 36 (a nested loop!).', None, SOFT, 32)
body += box(740, 380, 1052, 'A total of 7 happens 6 ways:  P(7) = 6/36 = 1/6', 'rise', WHITE, 34)
body += box(740, 490, 1052, 'A total of 2 happens 1 way:  P(2) = 1/36', 'rise', WHITE, 34)
body += box(740, 600, 1052, 'Dice Race: A’s totals happen 1 + 2 + 3 + 3 + 2 + 1 = 12 ways. B’s happen 24 ways.', 'rise', WHITE, 32)
body += pin(740, 760, 1052, p('P(A) = 12/36 = 1/3,  P(B) = 24/36 = 2/3: not fair', 36, 800), 'pop', YEL, 20, '16px 26px')
put(f'{PRE}-teachtwo', sec(f'{PRE}-teachtwo', '29–31 MIN', body, 'Teach. Use a red die and a blue die so that 1 + 6 and 6 + 1 are clearly different outcomes. Think-aloud: ' + SC['think'][1] + ' Then link to the Explore: "A has more TOTALS, but B has more OUTCOMES." Common wrong idea: "there are 11 totals, so each is 1/11". Totals are not equally likely; the 36 outcomes are.'))

# ---------- 10 try 2 ----------
put(f'{PRE}-try2', try_slide(f'{PRE}-try2', '31–32 MIN', 'Your turn: use the table', 'Two dice, add. Simplest form.',
    [('a', 'P(total 11)?', '2/36 = 1/18'), ('b', 'P(total 4)?', '3/36 = 1/12'), ('c', 'P(total more than 9)?', '6/36 = 1/6')],
    'Children look at the table. a) 5 + 6 and 6 + 5. b) 1 + 3, 2 + 2, 3 + 1. c) 10, 11 or 12: 3 + 2 + 1 = 6 ways. Ask: "Which total is most likely? Least likely?" (7; 2 and 12).', size=38))

# ---------- 11 teach code: run the game 1000 times ----------
game_code = [('hat', 'when green flag clicked'), ('var', 'set A to [0]'), ('var', 'set B to [0]'), ('ctrl', 'repeat [1000]', [('var', 'set total to [pick random 1 to 6] + [pick random 1 to 6]'), ('ctrl', 'if [total > 4] and [total < 10] then', [('var', 'change B by [1]')], [('var', 'change A by [1]')])]), ('look', 'say A for 2 seconds'), ('look', 'say B')]
body = h2('Test it: let the computer play 1000 games', 64)
body += pin(128, 222, 1060, blocks_svg(game_code, 'Code: set A and B to 0, repeat 1000: set total to two random numbers 1 to 6 added, if total is more than 4 and less than 10 change B by 1, else change A by 1; then say A and B', 24), None, WHITE, 20, '14px 18px')
body += box(1240, 240, 552, 'Expect A: 1/3 × 1000 = 333 1/3', None, SOFT, 32)
body += box(1240, 360, 552, 'Expect B: 2/3 × 1000 = 666 2/3', None, SOFT, 32)
body += box(1240, 480, 552, 'Three real runs:  A 330, B 670;  A 322, B 678;  A 351, B 649', 'rise', WHITE, 32)
body += pin(1240, 680, 552, p('Close to 1/3 and 2/3 every time, never exactly.', 34, 800), 'pop', YEL, 20, '16px 26px')
put(f'{PRE}-teachcode', sec(f'{PRE}-teachcode', '32–33 MIN', body,
    'Teach the code: share your screen and run it 2 or 3 times. Point out "pick random 1 to 6" is one dice roll; adding two of them is two dice (NOT "pick random 2 to 12", which would make every total equally likely: a good question to ask!). '
    'Think-aloud: ' + SC['think'][2] + ' The three runs on the slide are real results from 1000-game runs; yours will differ. '
    'This is our main program today. Python version:\nimport random\na_wins = 0\nb_wins = 0\nfor game in range(1000):\n    d1 = random.randint(1, 6)\n    d2 = random.randint(1, 6)\n    if 5 <= d1 + d2 <= 9:\n        b_wins = b_wins + 1\n    else:\n        a_wins = a_wins + 1\nprint(a_wins, b_wins)'))

# ---------- 12 why not exactly ----------
runs = [102, 101, 85, 103, 97]
bsv = f'<svg aria-label="Bar chart: five runs of 600 rolls gave 102, 101, 85, 103 and 97 sixes; a dashed line marks 100" viewBox="0 -40 900 560" xmlns="http://www.w3.org/2000/svg" style="width:900px;height:560px;flex:none">'
base = 440; sc = 3.4
for v in (0, 50, 100):
    y = base - v * sc; bsv += f'<line x1="110" y1="{y}" x2="880" y2="{y}" stroke="#C9D4EC" stroke-width="2"/><text x="96" y="{y + 10}" font-size="28" font-weight="700" text-anchor="end" fill="{NAVY}" font-family="Nunito Sans, Arial">{v}</text>'
for i, v in enumerate(runs):
    x = 150 + i * 145; bsv += f'<rect x="{x}" y="{base - v * sc:.0f}" width="90" height="{v * sc:.0f}" fill="{TEAL}" stroke="{NAVY}" stroke-width="3"/><text x="{x + 45}" y="{base - v * sc - 12:.0f}" font-size="30" font-weight="800" text-anchor="middle" fill="{NAVY}" font-family="Nunito Sans, Arial">{v}</text><text x="{x + 45}" y="{base + 40}" font-size="28" font-weight="700" text-anchor="middle" fill="{MUTED}" font-family="Nunito Sans, Arial">run {i + 1}</text>'
bsv += f'<line x1="110" y1="{base - 100 * sc}" x2="880" y2="{base - 100 * sc}" stroke="{RED}" stroke-width="5" stroke-dasharray="14 10"/><text x="880" y="{base - 100 * sc - 95}" font-size="28" font-weight="800" text-anchor="end" fill="{RED}" font-family="Nunito Sans, Arial">expected: 1/6 × 600 = 100</text></svg>'
body = h2('Close, but not exact') + p('A program rolls a dice 600 times and counts the 6s. We ran it 5 times.', 34, 600, MUTED)
body += pin(128, 320, 900, bsv, None)
body += box(1080, 330, 712, 'Each roll is random, so each run wobbles around 100.', 'rise', WHITE, 32)
body += box(1080, 470, 712, 'About 9 runs in 10 land between 85 and 115.', 'rise', WHITE, 32)
body += box(1080, 590, 712, 'More rolls: the FRACTION of 6s gets closer to 1/6.', 'rise', WHITE, 32)
body += pin(1080, 730, 712, p('A result near what we expect does not mean the program is broken.', 32, 800), 'pop', YEL, 20, '16px 26px')
put(f'{PRE}-teachwhy', sec(f'{PRE}-teachwhy', '33–34 MIN', body,
    'The five bars are real results of a 600-roll program (counting 6s). Ask: "Run 3 gave 85. Is the dice unfair?" (No: 85 is unusual but possible; about 1 run in 20 is 85 or less.) '
    'Exact facts for the tutor: for 600 rolls, about 91% of runs give between 85 and 115 sixes; exactly 100 happens only about 4 times in 100 runs. For 1000 coin flips, about 95% of runs land between 470 and 530 heads, and exactly 500 happens about 1 run in 40. '
    'Misconception check (whiteboards, true or false): "A coin landed tails 4 times in a row, so heads is more likely next." (False: still 1/2; the coin has no memory.) "If I roll a dice 60 times I will get exactly ten 6s." (False: about 10.)'))

# ---------- 13 key ----------
body = h2(DK['keyHead'], 62) + card(p(DK['keyBig'], 44, 700)) + card(p(DK['keySmall'], 38, 600, MUTED))
put(f'{PRE}-key', sec(f'{PRE}-key', '34–35 MIN', body, 'Say the key idea together. Common mistakes to watch for during the worksheet: (1) ' + L['mistakes'][0] + ' (2) ' + L['mistakes'][1] + ' (3) ' + L['mistakes'][2]))

# ---------- 14 break ----------
put(f'{PRE}-break', f'<section id="{PRE}-break" data-transition="fade" style="background:{TEAL};color:{CREAM};font-family:{BF};padding:128px 128px 160px;display:flex;flex-direction:column;justify-content:center;gap:36px">\n'
    f'<p style="font-size:32px;font-weight:700;letter-spacing:4px;color:{YEL}">35–40 MIN</p><h2 style="font-family:{HF};font-size:110px;font-weight:600;line-height:1.05">Brain break</h2>'
    f'<p style="font-size:46px;font-weight:600">{E(DK["brk"])}</p><p style="font-size:36px;color:#D7EFEA">Then: a drink of water and back to the screen.</p>\n'
    f'<p style="position:absolute;left:128px;bottom:64px;width:1400px;font-size:24px;color:#D7EFEA">{E(slidekit.FOOT)}</p>\n<aside>Five minutes. Roll about 6 times. Afterwards ask: "Did we do each move twice? Should we have?" (Not necessarily: 6 rolls is a tiny sample.) Online: children stay in view of the camera.</aside>\n</section>\n')

# ---------- 15 teach bag ----------
def bag(red, blue, extra_red=0, extra_blue=0):
    tot = red + blue + extra_red + extra_blue
    s = f'<svg aria-label="Bag with {red + extra_red} red and {blue + extra_blue} blue counters" viewBox="0 0 520 170" xmlns="http://www.w3.org/2000/svg" style="width:520px;height:170px;flex:none"><path d="M20 30 Q20 160 70 160 L450 160 Q500 160 500 30" fill="{SOFT}" stroke="{NAVY}" stroke-width="4"/>'
    cols = [RED] * red + [SKY] * blue + [RED] * extra_red + [SKY] * extra_blue
    for i, c in enumerate(cols):
        x = 70 + (i % 8) * 54; y = 70 + (i // 8) * 52; new = i >= red + blue
        s += f'<circle cx="{x}" cy="{y}" r="22" fill="{c}" stroke="{NAVY}" stroke-width="{6 if new else 3}"/>'
    return s + '</svg>'
body = h2('Change the bag, change the chance') + pin(128, 240, 520, bag(2, 4), None)
body += box(700, 250, 1092, '2 red, 4 blue:  P(red) = 2/6 = 1/3', None, WHITE, 36)
body += pin(128, 440, 520, bag(2, 4, 2, 0), 'fade')
body += box(700, 440, 1092, 'Add red until P(red) = 1/2: red must equal blue. Add 2 red: 4/8 = 1/2', 'rise', WHITE, 34)
body += pin(128, 640, 520, bag(2, 4, 0, 2), 'fade')
body += box(700, 640, 1092, 'Start again. Add blue until P(red) = 1/4: 2 must be 1/4 of the total, so the total is 8. Add 2 blue: 2/8 = 1/4', 'rise', WHITE, 32)
put(f'{PRE}-teachbag', sec(f'{PRE}-teachbag', '40–42 MIN', body, 'Teach before worksheet page 1 (Q3 changes a bag of 4 red and 6 blue: do not do those numbers here). Use real counters in a bag if you can. Think-aloud: "For P(red) = 1/4, the red counters are 1 part out of 4 parts. 2 red is one part, so 4 parts is 8 counters. I have 6, so I add 2 blue." Check by writing the new fraction and simplifying. Counters with a thick outline are the new ones.'))

# ---------- 16-17 worksheet page 1 ----------
put(f'{PRE}-ws1', ws_preview(f'{PRE}-ws1', '42–54 MIN', 'Worksheet page 1: with your partner', [('Q1', 'Ben’s spinner: fractions, expected reds, and is his program wrong?'), ('Q2', 'Predict the coin program. Then run it 3 times in Scratch.'), ('Q3', 'Change the bag to change the chance (red to make 1/2).')],
    'Stuck? Count the equally likely outcomes first.', 'Minutes 42 to 54. Walk around. Ask "What are the equally likely outcomes? How many?" Children who finish Q2 build the coin program and compare their 3 runs with their partner\'s.'))
k = dict(L['key'])
put(f'{PRE}-ws1ans', checkrows(f'{PRE}-ws1ans', '54–56 MIN', 'Page 1: check together', [('Q1', 'a) 3/8   b) 6/8 = 3/4   c) about 375   d) No: random results wobble; 362 is close to 375'), ('Q2', 'a) about 500   b) No: each run is random, so it lands near 500, rarely on it   c) about 200'), ('Q3', 'a) 4/10 = 2/5   b) add 2 red (6/12)')],
    'Click after a pair explains. Q1d: with a fair 3/8 spinner, about 19 runs in 20 land between 345 and 405 reds, and about 1 run in 5 gives 362 or fewer. Q2b: exactly 500 heads happens only about 1 run in 40. Q3c: 4 red must be 1/5 of the total, so the total is 20: add 10 blue. Full key: ' + k['Q1'] + ' | ' + k['Q2'] + ' | ' + k['Q3']))

# ---------- 18 teach fair: two coins ----------
def coins_svg():
    s = f'<svg aria-label="Two coins: the four outcomes HH, HT, TH, TT" viewBox="0 0 640 470" xmlns="http://www.w3.org/2000/svg" style="width:640px;height:470px;flex:none">'
    s += f'<text x="215" y="34" font-size="28" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="Nunito Sans, Arial">coin 1</text><text x="355" y="34" font-size="28" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="Nunito Sans, Arial">coin 2</text>'
    for i, (a, b) in enumerate(['HH', 'HT', 'TH', 'TT']):
        y = 100 + i * 105; same = a == b
        s += f'<rect x="120" y="{y - 50}" width="500" height="94" rx="16" fill="{SOFT if same else SKY}" stroke="{NAVY}" stroke-width="3"/>'
        for j, c in enumerate((a, b)): s += f'<circle cx="{215 + j * 140}" cy="{y - 3}" r="38" fill="{YEL}" stroke="{NAVY}" stroke-width="4"/><text x="{215 + j * 140}" y="{y + 11}" font-size="38" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="Fredoka, Arial">{c}</text>'
        s += f'<text x="470" y="{y + 9}" font-size="30" font-weight="800" fill="{TEAL}" font-family="Nunito Sans, Arial">{"Ali" if same else "Ben"}</text><text x="60" y="{y + 9}" font-size="30" font-weight="700" text-anchor="middle" fill="{MUTED}" font-family="Nunito Sans, Arial">{i + 1}</text>'
    return s + '</svg>'
body = h2('Is the game fair?') + card(p('Flip two coins. Ali wins if they are the same. Ben wins if they are different.', 38, 700))
body += pin(128, 380, 640, coins_svg(), 'fade')
body += box(820, 390, 972, 'Not 3 outcomes (two heads, two tails, one of each)! HT and TH are different.', 'rise', WHITE, 32)
body += box(820, 540, 972, '4 equally likely outcomes:  P(Ali) = 2/4,  P(Ben) = 2/4', 'rise', WHITE, 34)
body += pin(820, 680, 972, p('Same probability of winning: the game is fair ✓', 36, 800), 'pop', YEL, 20, '16px 26px')
put(f'{PRE}-teachfair', sec(f'{PRE}-teachfair', '56–58 MIN', body, 'Teach before worksheet page 2 (Q4, the Difference Game: do not do it here). Ask first: "Fair or not? Thumbs up or down." Many say Ali wins only 1/3 (two heads, two tails versus one of each). Use two different coins (a 10¢ and a 20¢) so HT and TH are clearly different. Then: "How could we change an unfair game to make it fair?" (change which outcomes win, or give different points).'))

# ---------- 19 teach plan ----------
coin_plan = [('hat', 'when green flag clicked'), ('var', 'set same to [0]'), ('ctrl', 'repeat [1000]', [('var', 'set a to pick random 1 to [2]'), ('var', 'set b to pick random 1 to [2]'), ('ctrl', 'if [a = b] then', [('var', 'change same by [1]')])]), ('look', 'say same')]
body = h2('Plan your code: the two-coin game', 64)
body += pin(128, 225, 820, blocks_svg(coin_plan, 'Code: set same to 0, repeat 1000: set a to pick random 1 to 2, set b to pick random 1 to 2, if a = b then change same by 1; say same', 26), None, WHITE, 20, '16px 20px')
body += box(1000, 240, 792, 'a and b are the two coins: 1 = heads, 2 = tails.', None, SOFT, 32)
body += box(1000, 380, 792, '“if a = b” counts the games Ali wins.', 'rise', WHITE, 32)
body += box(1000, 500, 792, 'Expect 2/4 × 1000 = about 500.', 'rise', WHITE, 32)
body += pin(1000, 640, 792, p('Plan on paper first: what goes in each box, and what do you expect it to say?', 32, 800), 'pop', YEL, 20, '16px 26px')
put(f'{PRE}-teachplan', sec(f'{PRE}-teachplan', '58–59 MIN', body, 'Teach before worksheet page 2 (Q5 plans a program for two DICE: let them work out the numbers themselves). Point out each coin needs its own random number: one "pick random" for both coins would make them always the same. If time, run it: answers near 500 (e.g. 489, 512) confirm the game is fair.'))

# ---------- 20-21 worksheet page 2 ----------
put(f'{PRE}-ws2', ws_preview(f'{PRE}-ws2', '59–72 MIN', 'Worksheet page 2: on your own', [('Q4', 'The Difference Game: fill the table (two rows are done for you), find each player’s chance, is it fair?'), ('Q5', 'Plan the doubles program. What should it say, and why not exactly?')],
    'Finished early? Run the Python corner, or try Stretch and Challenge.', 'Children work alone. Note who needs a short catch-up next lesson. Children who finish change the Explore program (or the Python corner) to play the Difference Game 1000 times and check their answer to Q4.'))
put(f'{PRE}-ws2ans', checkrows(f'{PRE}-ws2ans', '72–75 MIN', 'Page 2: check together', [('Q4', 'Difference 0: 6 ways, 1: 10, 2: 8, 3: 6, 4: 4, 5: 2.  Ali 24/36 = 2/3, Ben 12/36 = 1/3: not fair.'), ('Q5', 'Gaps 6, 6, a = b.  About 167: P(double) = 6/36 = 1/6 and 1/6 × 1000 = 166 2/3. A count is a whole number, and each run is random.')],
    'Click after a child explains. Q4: other fair rules: Ali on 1 and 2 (10 + 8 = 18); or Ali on 0, 1 and 5 (6 + 10 + 2 = 18). Ask: "Each player had 3 differences. Why was it still unfair?" Q5: about 19 runs in 20 land between 145 and 190 doubles. Full key: ' + k['Q4'] + ' | ' + k['Q5'], 32))

# ---------- 22 stretch ----------
import p6_th
st = p6_th.get(6)
put(f'{PRE}-stretch', numcards(f'{PRE}-stretch', 'For early finishers', 'Stretch', [(f'{i + 1}.', x['q']) for i, x in enumerate(st)], 'The same four questions as the printed Think harder page, for anyone who wants them. Answers: ' + ' '.join(f'{i + 1}) {x["a"]}' for i, x in enumerate(st)), 27))

# ---------- 23 challenge ----------
ch = QB['challenge'][-2:]
put(f'{PRE}-challenge', numcards(f'{PRE}-challenge', 'Challenge', 'Challenge', [(f'{i + 1}.', x['q']) for i, x in enumerate(ch)], 'Pairs try first, then use the "see it" slide if stuck, then the walk-through. These are also on the Go further page. Answers: ' + ' '.join(f'{i + 1}) {x["a"]}' for i, x in enumerate(ch)), 34))

# ---------- 24 challenge: see it ----------
def grid66():
    c = 62; x0 = 140; y0 = 80
    s = f'<svg aria-label="Empty 6 by 6 grid: Mei’s number across, Ali’s number down" viewBox="0 0 760 520" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;display:block">'
    s += f'<text x="{x0 + 3 * c}" y="34" font-size="28" font-weight="700" text-anchor="middle" fill="{TEAL}" font-family="Nunito Sans, Arial">Mei’s number</text><text x="60" y="{y0 + 3 * c}" font-size="28" font-weight="700" text-anchor="middle" fill="{RED}" font-family="Nunito Sans, Arial" transform="rotate(-90 60 {y0 + 3 * c})">Ali’s number</text>'
    for i in range(6):
        s += f'<text x="{x0 + i * c + c / 2}" y="{y0 - 10}" font-size="28" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="Nunito Sans, Arial">{i + 1}</text><text x="{x0 - 20}" y="{y0 + i * c + 41}" font-size="28" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="Nunito Sans, Arial">{i + 1}</text>'
        for j in range(6): s += f'<rect x="{x0 + j * c}" y="{y0 + i * c}" width="{c}" height="{c}" fill="{SOFT if i == j else WHITE}" stroke="{NAVY}" stroke-width="2"/>'
    s += f'<text x="{x0 + 3 * c}" y="{y0 + 6 * c + 50}" font-size="28" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="Nunito Sans, Arial">Mark each square: who wins?</text></svg>'
    return s
def spin(cx, cy, r, nums, col):
    n = len(nums); s = ''
    for i, v in enumerate(nums):
        a0 = math.radians(i * 360 / n - 90); a1 = math.radians((i + 1) * 360 / n - 90); am = (a0 + a1) / 2
        s += f'<path d="M{cx},{cy} L{cx + r * math.cos(a0):.1f},{cy + r * math.sin(a0):.1f} A{r},{r} 0 0 1 {cx + r * math.cos(a1):.1f},{cy + r * math.sin(a1):.1f} Z" fill="{col if i % 2 == 0 else WHITE}" stroke="{NAVY}" stroke-width="3"/><text x="{cx + r * 0.6 * math.cos(am):.1f}" y="{cy + r * 0.6 * math.sin(am) + 11:.1f}" font-size="32" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="Fredoka, Arial">{v}</text>'
    return s
ssv = f'<svg aria-label="Spinner A with 1, 2, 3 and spinner B with 1, 2, 3, 4, and an empty 3 by 4 table of products" viewBox="0 0 760 520" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;display:block">'
ssv += spin(150, 120, 95, [1, 2, 3], YEL) + spin(400, 120, 95, [1, 2, 3, 4], SKY) + f'<text x="150" y="250" font-size="28" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="Nunito Sans, Arial">A</text><text x="400" y="250" font-size="28" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="Nunito Sans, Arial">B</text><text x="610" y="130" font-size="34" font-weight="700" text-anchor="middle" fill="{TEAL}" font-family="Nunito Sans, Arial">A × B</text>'
c = 70; x0 = 230; y0 = 300
ssv += f'<rect x="{x0 - 70}" y="{y0 - 40}" width="70" height="40" fill="{SOFT}" stroke="{NAVY}" stroke-width="2"/><text x="{x0 - 35}" y="{y0 - 10}" font-size="26" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="Nunito Sans, Arial">×</text>'
for j in range(4): ssv += f'<rect x="{x0 + j * c}" y="{y0 - 40}" width="{c}" height="40" fill="{SKY}" stroke="{NAVY}" stroke-width="2"/><text x="{x0 + j * c + c / 2}" y="{y0 - 10}" font-size="26" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="Nunito Sans, Arial">{j + 1}</text>'
for i in range(3):
    ssv += f'<rect x="{x0 - 70}" y="{y0 + i * 56}" width="70" height="56" fill="{YEL}" stroke="{NAVY}" stroke-width="2"/><text x="{x0 - 35}" y="{y0 + i * 56 + 38}" font-size="26" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="Nunito Sans, Arial">{i + 1}</text>'
    for j in range(4): ssv += f'<rect x="{x0 + j * c}" y="{y0 + i * 56}" width="{c}" height="56" fill="{WHITE}" stroke="{NAVY}" stroke-width="2"/>'
ssv += f'<text x="380" y="505" font-size="28" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="Nunito Sans, Arial">Fill in the products: odd or even?</text></svg>'
body = h2('Challenge: see it', 60) + '<div style="display:flex;gap:32px;align-items:flex-start">' + card(f'<p style="font-size:28px;font-weight:700;color:{TEAL}">Q1: Mei and Ali</p>' + grid66(), extra='flex:1;min-width:0;padding:20px 24px') + card(f'<p style="font-size:28px;font-weight:700;color:{TEAL}">Q2: Two spinners</p>' + ssv, extra='flex:1;min-width:0;padding:20px 24px') + '</div>'
put(f'{PRE}-chdiag', sec(f'{PRE}-chdiag', 'Challenge', body, 'Show after pairs have tried, or if they are stuck. The pictures show the problem, not the answer. Ask: How many equally likely outcomes are there? Which squares does Mei win? What has to be true for a product to be odd?'))

# ---------- 25 challenge walk-through ----------
body = h2('Challenge: walk-through') + pin(128, 240, 800, p('Q1: 36 squares', 38, 800, TEAL))
for i, t in enumerate(['Same number: 6 squares (Ali wins these)', 'Mei bigger: 0 + 1 + 2 + 3 + 4 + 5 = 15', 'Ali: 15 + 6 = 21.  P(Mei) = 15/36 = 5/12', 'Not fair. Fix: same number means roll again']): body += pin(128, 320 + i * 120, 800, p(t, 32), 'rise', WHITE)
body += pin(992, 240, 800, p('Q2: 3 × 4 = 12 outcomes', 38, 800, TEAL))
for i, t in enumerate(['Odd × odd is odd. Any even number makes it even.', 'Odd: A is 1 or 3, B is 1 or 3: 2 × 2 = 4', 'P(Odd) = 4/12 = 1/3,  P(Even) = 8/12 = 2/3', 'Not fair: Even is twice as likely']): body += pin(992, 320 + i * 120, 800, p(t, 32), 'rise', WHITE)
put(f'{PRE}-chwalk', sec(f'{PRE}-chwalk', 'Challenge', body, 'Use after pairs have tried. Q1: with "roll again on the same number", each player wins 15 of the 30 remaining outcomes: fair. Q2: test it in code: set a to pick random 1 to 3, set b to pick random 1 to 4, check whether a × b is odd (a × b mod 2 = 1); 1000 games give about 333 odd. Ask: "How could you change the spinners to make the game fair?"'))

# ---------- 26 talk ----------
body = h2('Talk time') + card(chip('TALK TIME', YEL, NAVY) + p(SC['talk'][0].strip('“”"'), 42, 600)) + card(p('Sentence starters:', 34, 400, MUTED) + p('“I noticed that …”   “I tested it by …”   “I know because …”', 38, 600))
put(f'{PRE}-talk', sec(f'{PRE}-talk', '75–82 MIN', body, 'Minutes 75 to 82. Pairs talk for 2 minutes, then share. Follow-up: ' + SC['talk'][1] + ' Answer: ' + SC['talkAns'] + ' Close: ' + SC['close'][0]))

# ---------- 27 exit ----------
body = h2('Exit ticket') + card(chip('EXIT TICKET') + p(L['exit']['q'], 44, 600)) + card(p('Write your answer on a slip of paper (or type it in the chat). Show it to your tutor. Then collect your stamp in your inquiry journal.', 34, 400))
put(f'{PRE}-exit', sec(f'{PRE}-exit', '82–90 MIN', body, 'Minutes 82 to 90. Answer: ' + L['exit']['a'] + ' Extension: ' + L['extension']))

# ---------- write ----------
order = [f'{PRE}-{x}' for x in ['title', 'warm1', 'warm2', 'explore1', 'explore2', 'teach1', 'we1', 'try1', 'teachtwo', 'try2', 'teachcode', 'teachwhy', 'key', 'break', 'teachbag', 'ws1', 'ws1ans', 'teachfair', 'teachplan', 'ws2', 'ws2ans', 'stretch', 'challenge', 'chdiag', 'chwalk', 'talk', 'exit']]
assert set(order) == set(S), set(order) ^ set(S)
for f in os.listdir(os.path.join(D, 'slides')):
    if f.endswith('.html') and f[:-5] not in S: os.remove(os.path.join(D, 'slides', f))
for sid, h in S.items(): open(os.path.join(D, 'slides', sid + '.html'), 'w').write(h)
deck = {'v': 4, 'createdOnFiles': {'v': 1, 'at': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}, 'lists': 'css',
        'title': f'Math Inquirers Level 6: Lesson {N} – {L["title"]}', 'order': order, 'cover': order[0],
        'sections': {'s1': {'description': 'Warm-up and explore', 'start': f'{PRE}-title'}, 's2': {'description': 'Teach: probability as a fraction, two dice, 1000 games in code', 'start': f'{PRE}-teach1'},
                     's3': {'description': 'Worksheet with teaching before each page', 'start': f'{PRE}-break'}, 's4': {'description': 'Stretch, challenge, talk and exit', 'start': f'{PRE}-stretch'}},
        'faces': {'fredoka': {'family': 'Fredoka', 'href': 'https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&display=swap'}, 'nunito-sans': {'family': 'Nunito Sans', 'href': 'https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@400;600;700&display=swap'}},
        'designSystems': []}
json.dump(deck, open(os.path.join(D, 'deck.json'), 'w'), indent=1, ensure_ascii=False)
print(len(order), 'slides')

import p6_gaps; p6_gaps.apply(6)

import p6_stories; p6_stories.apply(6)
