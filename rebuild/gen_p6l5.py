"""Math Inquirers P6, Lesson 5: Every Possible Way. Writes split/p6l5/project (deck.json + slides/*.html).
Content strings (warm-up questions, explore, key idea, question bank, exit) are read from p6/content/l5.js so the deck matches the workbook."""
import json, os, sys, re, subprocess, math, datetime
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, H)
import slidekit
slidekit.FOOT = 'Math Inquirers P6  •  Notice it. Test it. Explain why.'
from slidekit import *
N = 5; PRE = f'p6l{N}'
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
         "Time plan: warm-up 0 to 10, explore 10 to 25 (paper first, then at the computer), teaching 25 to 35 (click to reveal each step and answer), brain break 35 to 40, "
         "worksheet 40 to 75 with short teaching before each page and a check-together slide after it, talk time 75 to 82, exit ticket 82 to 90. "
         "Before the lesson: share the starter project “Every Order” as an .sb3 file (a sprite with: set tea to 1, repeat 3: say tea for 1 second, change tea by 1). The sprite says the numbers 1, 2, 3, not the tea names: tell children that teas are numbered 1 = milk, 2 = green, 3 = taro and toppings 1 = pearls, 2 = jelly, so \"join tea topping\" saying 21 means green with pearls.")
body = (f'<p style="font-size:32px;font-weight:700;letter-spacing:4px;color:{YEL}">LESSON {N}  •  WEEK 3</p>'
        f'<h1 style="font-family:{HF};font-size:128px;font-weight:600;line-height:1.05">{E(L["title"])}</h1>'
        f'<p style="font-size:44px;color:#C9D4EC">Counting  •  nested loops</p>'
        f'<div style="background:#26385F;border-radius:24px;padding:40px;display:flex;flex-direction:column;gap:12px"><p style="font-size:28px;font-weight:700;letter-spacing:3px;color:{YEL}">TODAY WE WILL</p><p style="font-size:44px;font-weight:600">{E(DK["today"])}</p></div>')
put(f'{PRE}-title', f'<section id="{PRE}-title" data-transition="fade" style="background:{NAVY};color:{CREAM};font-family:{BF};padding:128px 128px 160px;display:flex;flex-direction:column;justify-content:center;gap:36px">\n{body}\n<p style="position:absolute;left:128px;bottom:64px;width:1400px;font-size:24px;color:#B7C3DD">{E(slidekit.FOOT)}</p>\n<aside>{E(notes)}</aside>\n</section>\n')

# ---------- 2 warm-up game ----------
wc = [('Pages 15 to 40 of a book. How many pages?', '26  (40 − 15 + 1)'), ('How many 2-digit numbers are there?', '90  (10 to 99)'), ('Multiples of 5 from 5 to 100?', '20  (100 ÷ 5)'),
      ('Lamp posts every 10 m on a 100 m road, one at each end?', '11  (10 gaps, 11 posts)'), ('Numbers from 1 to 100 with a 7 in them?', '19  (77 counted once)'), ('Even numbers from 2 to 50?', '25  (50 ÷ 2)')]
body = h2('Warm-up: count it, don’t list it') + p('Work in pairs. Say HOW you counted. No race.', 34, 600, MUTED)
CWD = 533
for i, (q, a) in enumerate(wc):
    Lx = 128 + (i % 3) * (CWD + 32); T = 290 + (i // 3) * 300
    body += pin(Lx, T, CWD, f'<p style="font-family:{HF};font-size:36px;font-weight:600;line-height:1.2">{E(q)}</p>', None, WHITE, 24, '22px 26px', f'box-sizing:border-box;height:276px;border:4px solid {NAVY};box-shadow:8px 8px 0 {NAVY}')
    body += pin(Lx + 20, T + 176, CWD - 40, f'<p style="font-size:34px;font-weight:800;line-height:1.2">{E(a)}</p>', 'pop', SOFT, 16, '12px 18px', f'box-sizing:border-box;border:3px solid {NAVY}')
put(f'{PRE}-warm1', sec(f'{PRE}-warm1', '0–5 MIN', body,
    'Minutes 5 to 8. ' + DK['warmGame'] + ' Click once per card to show its answer (cards go left to right, top row first). '
    'Answers: 26 pages (40 − 15 = 25 counts the gaps, so add 1); 90 two-digit numbers (99 − 10 + 1); 20 multiples of 5; 11 lamp posts (100 ÷ 10 = 10 gaps, plus 1); '
    '19 numbers with a 7 (7, 17, …, 97 is 10; 70 to 79 is 10; 77 is in both lists, so 10 + 10 − 1); 25 even numbers. '
    'Ask after each: "How did you count without listing?" Praise the "+ 1" fix (fence posts) and the "counted twice" fix (77): both come back today.'))

# ---------- 3 quick questions ----------
qs = DK['warmQs']
body = h2('Quick questions') + ''.join(qrow(128, 240 + i * 128, 1250, f'{i + 1}.', q, 38) for i, (q, a) in enumerate(qs)) + ''.join(answer(1420, 240 + i * 128, 372, a) for i, (q, a) in enumerate(qs))
put(f'{PRE}-warm2', sec(f'{PRE}-warm2', '5–10 MIN', body, 'Minutes 5 to 10. Whiteboards, then click to show each answer. ' + '  '.join(f'{i + 1}) {a}' for i, (q, a) in enumerate(qs)) +
    '. For 2 ask for a quick way (1 + 10, 2 + 9 … five pairs of 11 = 55). For 5: the inner loop says "hi" twice for each of the 5 turns of the outer loop, 5 × 2 = 10. We use this idea a lot today.'))

# ---------- 4 explore 1 ----------
def menu_svg():
    s = f'<svg aria-label="Bubble tea menu: 3 teas, 2 toppings, sizes M and L, and the starter code" viewBox="0 0 760 560" xmlns="http://www.w3.org/2000/svg" style="width:760px;height:560px;flex:none">'
    s += f'<rect x="4" y="4" width="752" height="300" rx="20" fill="{SOFT}" stroke="{NAVY}" stroke-width="4"/><text x="380" y="52" font-size="36" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="Fredoka, Arial">BUBBLE TEA MENU</text>'
    for i, (nm, col) in enumerate([('milk', '#F3D9B1'), ('green', '#BFE3DC'), ('taro', '#C9B6E4')]):
        x = 60 + i * 150
        s += f'<path d="M{x} 90 L{x + 100} 90 L{x + 88} 210 L{x + 12} 210 Z" fill="{col}" stroke="{NAVY}" stroke-width="4"/><line x1="{x + 62}" y1="70" x2="{x + 56}" y2="150" stroke="{RED}" stroke-width="7" stroke-linecap="round"/>'
        s += f'<text x="{x + 50}" y="250" font-size="28" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="Nunito Sans, Arial">{i + 1} {nm}</text>'
    s += f'<text x="530" y="120" font-size="28" font-weight="700" fill="{TEAL}" font-family="Nunito Sans, Arial">toppings</text>'
    s += f'<circle cx="545" cy="160" r="16" fill="{NAVY}"/><text x="575" y="170" font-size="28" font-weight="700" fill="{NAVY}" font-family="Nunito Sans, Arial">1 pearls</text>'
    s += f'<rect x="530" y="190" width="30" height="30" rx="6" fill="{YEL}" stroke="{NAVY}" stroke-width="3"/><text x="575" y="216" font-size="28" font-weight="700" fill="{NAVY}" font-family="Nunito Sans, Arial">2 jelly</text>'
    s += f'<text x="530" y="270" font-size="28" font-weight="700" fill="{TEAL}" font-family="Nunito Sans, Arial">later: M or L</text></svg>'
    return s
start_code = blocks_svg([('hat', 'when green flag clicked'), ('var', 'set tea to [1]'), ('ctrl', 'repeat [3]', [('look', 'say tea for 1 seconds'), ('var', 'change tea by [1]')])], 'Starter code: set tea to 1, repeat 3: say tea, change tea by 1', 26)
steps = ''.join(f'<li>{E(x)}</li>' for x in DK['expSetup'])
body = h2('Explore: the bubble tea shop') + (f'<div style="display:flex;gap:32px;align-items:flex-start">'
        f'<div style="background:{WHITE};border-radius:24px;padding:26px 34px;display:flex;flex-direction:column;gap:12px;flex:1;min-width:0">{chip("EXPLORE")}<ol style="font-size:32px;font-weight:600;padding-left:44px;display:flex;flex-direction:column;gap:10px;line-height:1.3;margin:0">{steps}</ol></div>'
        f'<div style="display:flex;flex-direction:column;gap:18px;flex:none">{menu_svg().replace("height:560px", "height:310px").replace("viewBox=\"0 0 760 560\"", "viewBox=\"0 0 760 310\"")}<div style="background:{WHITE};border-radius:20px;padding:14px 20px">{start_code}</div></div></div>')
put(f'{PRE}-explore1', sec(f'{PRE}-explore1', '10–15 MIN', body,
    'Minutes 10 to 25 (this slide 10 to 15). ' + L['explore'] + ' Predict first: ' + SC['predict'][0] + ' Paper list first (about 5 minutes), then the computer. '
    'The starter project says tea 1, 2, 3 (the menu board shows the numbers: 1 milk, 2 green, 3 taro; 1 pearls, 2 jelly; so "join tea topping" saying 21 means green with pearls). Children drag a second "repeat 2" block inside the first one (with set topping to 1 before it and change topping by 1 inside it) and use "say join tea topping". Hints: ' + ' '.join(SC['exploreHints']) +
    ' Online: ' + L['online'] + '\nPython version (for children who know Python):\n' + 'teas = ["milk", "green", "taro"]\ntoppings = ["pearls", "jelly"]\ncount = 0\nfor tea in teas:\n    for top in toppings:\n        print(tea, "tea with", top)\n        count = count + 1\nprint(count, "orders")'))

# ---------- 5 explore 2 ----------
body = h2('Explore: talk about it') + ''.join(card(p(f'<span style="color:{TEAL}">{i + 1}.</span>  {E(q)}', 40, 600, raw=True), extra='padding:30px 40px') for i, (q, a) in enumerate(DK['expAsk']))
put(f'{PRE}-explore2', sec(f'{PRE}-explore2', '15–25 MIN', body, 'Minutes 15 to 25. Gather pairs (or bring them back from breakout rooms). Ask each, take two or three answers, then share one child’s screen to run their code. Answers: ' + ' '.join(f'{i + 1}) {a}' for i, (q, a) in enumerate(DK['expAsk'])) + ' Watch for children who add (3 + 2 = 5): ask them to point to all 6 orders on their list.'))

# ---------- 6 teach 1: tree ----------
def tree_svg(caps=False):
    sh = [('red', RED), ('blue', SKY), ('white', WHITE)]; s = f'<svg aria-label="Tree: 3 shirts, each with 2 pairs of shorts, makes 6 outfits" viewBox="0 0 900 600" xmlns="http://www.w3.org/2000/svg" style="width:900px;height:600px;flex:none">'
    for i, (nm, col) in enumerate(sh):
        y = 100 + i * 200
        for j, sn in enumerate(['black', 'grey']):
            y2 = y - 50 + j * 100
            s += f'<line x1="250" y1="{y}" x2="420" y2="{y2}" stroke="{NAVY}" stroke-width="4"/>'
            s += f'<rect x="420" y="{y2 - 32}" width="160" height="64" rx="14" fill="{"#5B6785" if sn == "black" else "#EDEDED"}" stroke="{NAVY}" stroke-width="3"/><text x="500" y="{y2 + 11}" font-size="30" font-weight="700" text-anchor="middle" fill="{WHITE if sn == "black" else NAVY}" font-family="Nunito Sans, Arial">{sn}</text>'
            s += f'<text x="610" y="{y2 + 11}" font-size="30" font-weight="700" fill="{TEAL}" font-family="Nunito Sans, Arial">{nm} + {sn}</text>'
        s += f'<path d="M70 {y - 40} L120 {y - 55} L150 {y - 40} L180 {y - 55} L230 {y - 40} L250 {y - 5} L215 {y + 8} L210 {y + 55} L90 {y + 55} L85 {y + 8} L50 {y - 5} Z" fill="{col}" stroke="{NAVY}" stroke-width="4" stroke-linejoin="round"/>'
        s += f'<text x="150" y="{y + 32}" font-size="28" font-weight="700" text-anchor="middle" fill="{WHITE if nm == "red" else NAVY}" font-family="Nunito Sans, Arial">{nm}</text>'
    return s + '</svg>'
body = h2('Every outfit: fix one choice, then the next')
body += pin(128, 250, 900, tree_svg(), 'fade')
body += box(1080, 250, 712, '3 shirts. 2 pairs of shorts. List every outfit.', None, SOFT)
body += box(1080, 400, 712, 'Fix the red shirt: 2 outfits. Every shirt gets the same 2.')
body += box(1080, 550, 712, '3 groups of 2:  3 × 2 = 6 outfits.')
body += box(1080, 700, 712, 'Add 2 caps: each outfit splits in 2.  6 × 2 = 12.', 'pop', YEL)
put(f'{PRE}-teach1', sec(f'{PRE}-teach1', '25–27 MIN', body, 'Teach. Click 1: the tree appears. Then the three steps, then the caps. Think-aloud: ' + SC['think'][0] + ' Name it: "When choices are made one after another, we MULTIPLY. This is called the multiplication rule." Ask: "Why not 3 + 2?" (that counts shirts and shorts, not outfits).'))

# ---------- 7 worked example: lock ----------
body = h2('Worked example: a bike lock') + card(p('A lock has 3 dials. Each dial shows 1, 2, 3, 4 or 5. How many codes?', 40, 700))
body += step(1, 'Dial 1: 5 choices. For each one, dial 2 has 5 choices:  5 × 5 = 25.', top=430, size=36)
body += step(2, 'For each of those 25, dial 3 has 5 choices:  25 × 5 = 125 codes.', top=545, size=36)
body += step(3, 'No digit used twice?  5 × 4 × 3 = 60: each dial has one fewer choice.', top=660, size=36)
body += pin(128, 790, 1664, p('Check: 125 codes go from 111 to 555 using only the digits 1 to 5.', 32, 700), 'fade', SOFT, 20, '16px 28px')
put(f'{PRE}-we1', sec(f'{PRE}-we1', '27–29 MIN', body, 'Click through the steps. Ask before each: "How many choices does the next dial have?" For step 3: "Dial 1 can be any of 5. Dial 2 cannot repeat it: 4. Dial 3 cannot repeat either: 3." This prepares the digit-card question on page 1. Enumerated check: 125 codes with repeats, 60 without.'))

# ---------- 8 try 1 ----------
put(f'{PRE}-try1', try_slide(f'{PRE}-try1', '29–30 MIN', 'Your turn: whiteboards', 'Multiply the choices. Watch out for repeats.',
    [('a', '5 sandwiches, 4 drinks. Meal sets of 1 + 1?', '20'), ('b', 'Codes of 2 letters from A, B, C (repeats allowed)?', '9'), ('c', '4 runners. Ways to give gold AND silver?', '12')],
    'Whiteboards up together, then click. a) 5 × 4 = 20. b) 3 × 3 = 9: AA, AB, AC, BA, BB, BC, CA, CB, CC. c) 4 × 3 = 12: gold can go to any of 4, then silver to one of the other 3. Ask: "Why is c not 4 × 4?" (one runner cannot win both).', size=36))

# ---------- 9 teach code: nested loops ----------
outfit_code = [('hat', 'when green flag clicked'), ('var', 'set shirt to [1]'), ('ctrl', 'repeat [3]', [('var', 'set shorts to [1]'), ('ctrl', 'repeat [2]', [('look', 'say [join shirt shorts] for 1 seconds'), ('var', 'change shorts by [1]')]), ('var', 'change shirt by [1]')])]
body = h2('Let the computer list them: nested loops')
body += pin(128, 240, 960, blocks_svg(outfit_code, 'Code: set shirt to 1, repeat 3: set shorts to 1, repeat 2: say join shirt shorts, change shorts by 1; change shirt by 1', 26), None, WHITE, 20, '18px 22px')
body += box(1150, 240, 642, 'The OUTER loop picks the shirt. The INNER loop picks the shorts.', None, SOFT, 32)
body += box(1150, 420, 642, 'The inner loop runs all the way round for EACH shirt.', 'rise', WHITE, 32)
body += box(1150, 570, 642, 'It says:  11, 12, 21, 22, 31, 32', 'rise', WHITE, 32)
body += pin(1150, 700, 642, p('3 × 2 = 6 things said ✓', 38, 800), 'pop', YEL, 20, '18px 26px')
put(f'{PRE}-teachcode', sec(f'{PRE}-teachcode', '30–32 MIN', body,
    'Teach the code. Share your screen and build it live in Scratch if you can. Think-aloud: ' + SC['think'][1] + ' Point at "set shorts to 1": "Why must this go INSIDE the outer loop?" (so the shorts start again from 1 for every shirt; if it were outside, shirt 2 would start at shorts 3 and say 23 and 24, which are not real outfits). '
    '"join shirt shorts" sticks the two numbers together: shirt 2 and shorts 1 says 21. Ask: "What would it say with repeat 4 inside?" (3 × 4 = 12 things). '
    '\nPython version:\ncount = 0\nfor shirt in range(1, 4):\n    for shorts in range(1, 3):\n        print(shirt, shorts)\n        count = count + 1\nprint(count, "outfits")'))

# ---------- 10 try 2 ----------
put(f'{PRE}-try2', try_slide(f'{PRE}-try2', '32–34 MIN', 'Predict: how many times?', 'Count the says before you run it.',
    [('a', 'repeat 4 { repeat 5 { say hi } }', '20'), ('b', 'repeat 3 { say hi, repeat 2 { say ho } }', '9 (3 + 6)'), ('c', 'repeat 2 { repeat 3 { repeat 4 { say hi } } }', '24')],
    'Whiteboards. a) 4 × 5 = 20. b) "hi" 3 times and "ho" 3 × 2 = 6 times: 9 says. c) 2 × 3 × 4 = 24: three loops, three choices. If time, run a) in Scratch to test.', size=34))

# ---------- 11 key ----------
body = h2(DK['keyHead']) + card(p(DK['keyBig'], 44, 700)) + card(p(DK['keySmall'], 36, 600, MUTED))
put(f'{PRE}-key', sec(f'{PRE}-key', '34–35 MIN', body, 'Say the key idea together. Common mistakes to watch for during the worksheet: (1) ' + L['mistakes'][0] + ' (2) ' + L['mistakes'][1] + ' (3) ' + L['mistakes'][2]))

# ---------- 12 break ----------
put(f'{PRE}-break', f'<section id="{PRE}-break" data-transition="fade" style="background:{TEAL};color:{CREAM};font-family:{BF};padding:128px 128px 160px;display:flex;flex-direction:column;justify-content:center;gap:36px">\n'
    f'<p style="font-size:32px;font-weight:700;letter-spacing:4px;color:{YEL}">35–40 MIN</p><h2 style="font-family:{HF};font-size:110px;font-weight:600;line-height:1.05">Brain break</h2>'
    f'<p style="font-size:48px;font-weight:600">{E(DK["brk"])}</p><p style="font-size:36px;color:#D7EFEA">Then: a drink of water and back to the screen.</p>\n'
    f'<p style="position:absolute;left:128px;bottom:64px;width:1400px;font-size:24px;color:#D7EFEA">{E(slidekit.FOOT)}</p>\n<aside>Five minutes. Poses: 1 arms up + standing, 2 arms up + squat, 3 arms up + one leg, 4 arms out + standing, 5 arms out + squat, 6 arms out + one leg. Online: children stay in view of the camera.</aside>\n</section>\n')

# ---------- 13 teach cards ----------
def cards_svg(ds, w=560):
    s = f'<svg aria-label="Digit cards {", ".join(map(str, ds))}" viewBox="0 0 {w} 120" xmlns="http://www.w3.org/2000/svg" style="width:{w}px;height:120px;flex:none">'
    for i, d in enumerate(ds): x = 10 + i * 130; s += f'<rect x="{x}" y="8" width="104" height="104" rx="14" fill="{YEL if i % 2 == 0 else SKY}" stroke="{NAVY}" stroke-width="4"/><text x="{x + 52}" y="84" font-size="60" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="Fredoka, Arial">{d}</text>'
    return s + '</svg>'
body = h2('Digit cards: order matters, and watch the 0')
body += pin(128, 240, 420, cards_svg([2, 4, 7], 400), None)
body += box(600, 240, 1192, '3-digit numbers from 2, 4, 7:  3 × 2 × 1 = 6', 'rise', WHITE, 34)
body += box(600, 360, 1192, '247, 274, 427, 472, 724, 742', 'rise', SOFT, 34)
body += pin(128, 500, 420, cards_svg([0, 1, 2], 400), 'fade')
body += box(600, 500, 1192, '2-digit numbers from 0, 1, 2: the tens digit cannot be 0.', 'rise', WHITE, 34)
body += box(600, 620, 1192, 'Tens: 2 choices (1 or 2). Ones: 2 left (0 is allowed here).  2 × 2 = 4', 'rise', WHITE, 34)
body += pin(600, 760, 1192, p('10, 12, 20, 21  ✓', 40, 800), 'pop', YEL, 20, '16px 26px')
put(f'{PRE}-teachcards', sec(f'{PRE}-teachcards', '40–42 MIN', body, 'Teach before worksheet page 1 (Q2, digit cards). Click through. Think-aloud: "Hundreds: any of 3 cards. Tens: one card is used, so 2 left. Ones: 1 left. 3 × 2 × 1 = 6. I list them in order to check: 247, 274, 427, 472, 724, 742." Then the 0 trap: "02 is not a 2-digit number, so the tens has only 2 choices, but the ones can be 0." Ask: "How many 3-digit numbers from 0, 1, 2?" (2 × 2 × 1 = 4: 102, 120, 201, 210).'))

# ---------- 14-15 worksheet page 1 ----------
put(f'{PRE}-ws1', ws_preview(f'{PRE}-ws1', '42–55 MIN', 'Worksheet page 1: with your partner', [('Q1', 'Outfits: multiply the choices.'), ('Q2', 'Digit cards 0, 3, 5, 8. List in order. No 0 at the front.'), ('Q3', 'Trace the code on paper first. Then build it in Scratch to check.')],
    'Stuck? Draw a tree or fix the first choice.', 'Minutes 42 to 55. Walk around (or visit breakout rooms). Ask "How do you know you have them all?" before helping. Q3: insist the trace table is filled BEFORE they run the code.'))
k = dict(L['key'])
put(f'{PRE}-ws1ans', checkrows(f'{PRE}-ws1ans', '55–57 MIN', 'Page 1: check together', [('Q1', 'a) 12   b) 24'), ('Q2', 'a) 9: 30, 35, 38, 50, 53, 58, 80, 83, 85   b) 18 (3 × 3 × 2)'), ('Q3', 'a) 11, 12, 13, 14, 21, 22   b) 12   c) 34   d) 20')],
    'Click each answer after a pair explains. Q2a: tens 3 choices (not 0), ones 3 choices (the other three cards). Q2b: 3 × 3 × 2 = 18. Q3: a counts the turns of the outer loop, b the inner loop; b goes back to 1 every time a changes. Full key: ' + k['Q1'] + ' | ' + k['Q2'] + ' | ' + k['Q3']))

# ---------- 16 teach handshakes ----------
def penta_svg():
    pts = [(300 + 220 * math.cos(math.radians(-90 + 72 * i)), 270 + 220 * math.sin(math.radians(-90 + 72 * i))) for i in range(5)]
    s = f'<svg aria-label="5 friends A to E with a line for every handshake" viewBox="0 0 600 540" xmlns="http://www.w3.org/2000/svg" style="width:600px;height:540px;flex:none">'
    cols = [RED, TEAL, YEL, SKY, '#C9B6E4']
    for i in range(5):
        for j in range(i + 1, 5): s += f'<line x1="{pts[i][0]:.0f}" y1="{pts[i][1]:.0f}" x2="{pts[j][0]:.0f}" y2="{pts[j][1]:.0f}" stroke="{NAVY}" stroke-width="4"/>'
    for i, (x, y) in enumerate(pts): s += f'<circle cx="{x:.0f}" cy="{y:.0f}" r="40" fill="{cols[i]}" stroke="{NAVY}" stroke-width="4"/><text x="{x:.0f}" y="{y + 15:.0f}" font-size="42" font-weight="700" text-anchor="middle" fill="{WHITE if i in (0, 1) else NAVY}" font-family="Fredoka, Arial">{"ABCDE"[i]}</text>'
    return s + '</svg>'
body = h2('Handshakes: count each pair once') + pin(128, 230, 600, penta_svg(), None)
body += box(780, 240, 1012, '5 friends. Every pair shakes hands once.', None, SOFT, 34)
body += box(780, 370, 1012, 'A shakes 4 new hands, B 3 new, C 2, D 1, E 0.', 'rise', WHITE, 34)
body += box(780, 500, 1012, '4 + 3 + 2 + 1 = 10 handshakes', 'rise', WHITE, 34)
body += box(780, 630, 1012, 'Or: 5 × 4 = 20 counts every handshake twice (A–B and B–A).  20 ÷ 2 = 10', 'rise', WHITE, 34)
body += pin(780, 800, 1012, p('Count the lines in the picture: 10 ✓', 36, 800), 'pop', YEL, 20, '14px 26px')
put(f'{PRE}-teachhand', sec(f'{PRE}-teachhand', '57–59 MIN', body, 'Teach before worksheet page 2 (Q4). Think-aloud: ' + SC['think'][2] + ' Ask: "With 6 friends?" (5 + 4 + 3 + 2 + 1 = 15, or 6 × 5 ÷ 2). Do not do 7 friends: that is the worksheet.'))

# ---------- 17 handshake code ----------
hand_code = [('hat', 'when green flag clicked'), ('var', 'set count to [0]'), ('var', 'set a to [1]'), ('ctrl', 'repeat [5]', [('var', 'set b to [1]'), ('ctrl', 'repeat [5]', [('ctrl', 'if [a < b] then', [('var', 'change count by [1]')]), ('var', 'change b by [1]')]), ('var', 'change a by [1]')]), ('look', 'say count')]
body = h2('Test it in code: keep only a < b', 64)
body += pin(128, 225, 720, blocks_svg(hand_code, 'Code: set count to 0, set a to 1, repeat 5: set b to 1, repeat 5: if a < b then change count by 1; change b by 1; change a by 1; say count', 24), None, WHITE, 20, '14px 18px')
body += box(900, 240, 892, 'The loops check every pair (a, b): 5 × 5 = 25 pairs.', None, SOFT, 32)
body += box(900, 380, 892, 'a = b is one person with themselves: not a handshake.', 'rise', WHITE, 32)
body += box(900, 520, 892, 'a < b keeps 1–2 but not 2–1: each handshake once.', 'rise', WHITE, 32)
body += pin(900, 660, 892, p('It says 10 ✓  (25 − 5 = 20, then 20 ÷ 2)', 36, 800), 'pop', YEL, 20, '16px 26px')
put(f'{PRE}-teachhandcode', sec(f'{PRE}-teachhandcode', '59–60 MIN', body,
    'Teach before worksheet page 2 (Q6 asks children to plan this program for 7 friends, so do not change the numbers to 7 here). Run it live if you can: it says 10, matching our maths. Ask: "What would it say with a = b?" (5) "With a > b?" (10 again: each pair once, the other way round). '
    'This is our main program today. Python version:\ncount = 0\nfor a in range(1, 6):\n    for b in range(1, 6):\n        if a < b:\n            print(a, "shakes hands with", b)\n            count = count + 1\nprint(count, "handshakes")'))

# ---------- 18 routes ----------
def route_svg(stage):
    c = 150; x0 = 70; y0 = 50; w = 3; hh = 2
    s = f'<svg aria-label="Grid 3 squares wide and 2 tall, from A at the bottom left to B at the top right" viewBox="0 0 640 420" xmlns="http://www.w3.org/2000/svg" style="width:640px;height:420px;flex:none">'
    if stage == 0:
        for i in range(hh + 1): s += f'<line x1="{x0}" y1="{y0 + i * c}" x2="{x0 + w * c}" y2="{y0 + i * c}" stroke="{NAVY}" stroke-width="6"/>'
        for i in range(w + 1): s += f'<line x1="{x0 + i * c}" y1="{y0}" x2="{x0 + i * c}" y2="{y0 + hh * c}" stroke="{NAVY}" stroke-width="6"/>'
        s += f'<text x="{x0 - 64}" y="{y0 + hh * c + 14}" font-size="40" font-weight="700" fill="{TEAL}" font-family="Fredoka, Arial">A</text><text x="{x0 + w * c + 42}" y="{y0 + 14}" font-size="40" font-weight="700" fill="{TEAL}" font-family="Fredoka, Arial">B</text>'
    R = {}
    for x in range(w + 1):
        for y in range(hh + 1): R[x, y] = 1 if x == 0 or y == 0 else R[x - 1, y] + R[x, y - 1]
    for (x, y), v in R.items():
        show = stage == 0 and False or (stage == 1 and (x == 0 or y == 0)) or (stage == 2 and not (x == 0 or y == 0))
        if show: s += f'<circle cx="{x0 + x * c}" cy="{y0 + (hh - y) * c}" r="34" fill="{YEL if (x, y) == (w, hh) else WHITE}" stroke="{NAVY}" stroke-width="4"/><text x="{x0 + x * c}" y="{y0 + (hh - y) * c + 14}" font-size="38" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="Fredoka, Arial">{v}</text>'
    return s + '</svg>'
body = h2('Routes on a grid: add as you go') + p('Walk from A to B along the lines, going only right or up.', 34, 600, MUTED)
body += pin(128, 330, 640, route_svg(0), None) + pin(128, 330, 640, route_svg(1), 'fade') + pin(128, 330, 640, route_svg(2), 'fade')
body += box(830, 330, 962, 'Along the bottom and up the left side there is only 1 way to each point.', 'rise', WHITE, 32)
body += box(830, 480, 962, 'Any other point is reached from the LEFT or from BELOW: add those two numbers.', 'rise', WHITE, 32)
body += box(830, 650, 962, '1 + 2 = 3,  3 + 3 = 6,  4 + 6 = 10 routes to B', 'pop', YEL, 34)
put(f'{PRE}-teachroute', sec(f'{PRE}-teachroute', '60–61 MIN', body, 'Teach before worksheet page 2 (Q5 uses a 3 by 3 grid with a puddle: do not solve it here). Clicks: the 1s on the edges, the first note, the other numbers, the second note, the answer. Check by listing: a route is 3 rights and 2 ups in some order, e.g. RRRUU, RRURU …; there are 10 of them. Ask: "If a point were blocked by a puddle, what number would you write there?" (0: no routes go through it) but let them use this on the worksheet themselves.'))

# ---------- 19-20 worksheet page 2 ----------
put(f'{PRE}-ws2', ws_preview(f'{PRE}-ws2', '61–72 MIN', 'Worksheet page 2: on your own', [('Q4', 'Seven friends shake hands. Then find Ali’s mistake.'), ('Q5', 'Routes: add as you go. Then put 0 at the puddle.'), ('Q6', 'Plan the handshake program for 7 friends, then build it to test Q4.')],
    'Finished early? Stretch and Challenge come next.', 'Children work alone. Note who needs a short catch-up next lesson. Children who finish Q6 build it in Scratch (or Python) and check that it agrees with Q4.'))
put(f'{PRE}-ws2ans', checkrows(f'{PRE}-ws2ans', '72–75 MIN', 'Page 2: check together', [('Q4', 'a) 21   b) every handshake is counted twice: 42 ÷ 2 = 21'), ('Q5', 'a) 20 routes   b) 8 routes avoid P (12 go through it)'), ('Q6', 'repeat 7, repeat 7, if a < b.  It says 21 ✓   With a = b it says 7: each person with themselves')],
    'Click after a child explains. Q5 corner numbers (bottom row first): 1 1 1 1 / 1 2 3 4 / 1 3 6 10 / 1 4 10 20. With 0 at P: 1 1 1 1 / 1 0 1 2 / 1 1 2 4 / 1 2 4 8. Q6: the "if" is checked 7 × 7 = 49 times. Full key: ' + k['Q4'] + ' | ' + k['Q5'] + ' | ' + k['Q6']))

# ---------- 21 stretch (not printed in the workbook) ----------
import p6_th
st = p6_th.get(5)
put(f'{PRE}-stretch', numcards(f'{PRE}-stretch', 'For early finishers', 'Stretch', [(f'{i + 1}.', x['q']) for i, x in enumerate(st)], 'The same four questions as the printed Think harder page, for anyone who wants them. Answers: ' + ' '.join(f'{i + 1}) {x["a"]}' for i, x in enumerate(st)), 27))

# ---------- 22 challenge ----------
ch = QB['challenge'][-2:]
put(f'{PRE}-challenge', numcards(f'{PRE}-challenge', 'Challenge', 'Challenge', [(f'{i + 1}.', x['q']) for i, x in enumerate(ch)], 'Pairs try first, then use the "see it" slide if stuck, then the walk-through. These are also on the Go further page. Answers: ' + ' '.join(f'{i + 1}) {x["a"]}' for i, x in enumerate(ch)), 36))

# ---------- 23 challenge: see it ----------
def domino(x, y, a, b, s=44):
    def pips(cx, cy, n):
        P = {0: [], 1: [(0, 0)], 2: [(-1, -1), (1, 1)], 3: [(-1, -1), (0, 0), (1, 1)], 4: [(-1, -1), (1, -1), (-1, 1), (1, 1)], 5: [(-1, -1), (1, -1), (0, 0), (-1, 1), (1, 1)], 6: [(-1, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (1, 1)]}[n]
        return ''.join(f'<circle cx="{cx + dx * s * 0.3:.0f}" cy="{cy + dy * s * 0.3:.0f}" r="{s * 0.09:.0f}" fill="{NAVY}"/>' for dx, dy in P)
    return (f'<rect x="{x}" y="{y}" width="{2 * s}" height="{s}" rx="8" fill="{WHITE}" stroke="{NAVY}" stroke-width="3"/><line x1="{x + s}" y1="{y + 4}" x2="{x + s}" y2="{y + s - 4}" stroke="{NAVY}" stroke-width="3"/>' + pips(x + s / 2, y + s / 2, a) + pips(x + 1.5 * s, y + s / 2, b))
dsv = f'<svg aria-label="Some dominoes: 0 and 0, 0 and 1, 1 and 1, 2 and 5, 3 and 3, 6 and 6, and a question mark" viewBox="0 0 760 470" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;display:block">'
for i, (a, b) in enumerate([(0, 0), (0, 1), (1, 1), (2, 5), (3, 3), (6, 6)]): dsv += domino(40 + (i % 3) * 240, 40 + (i // 3) * 120, a, b, 80)
dsv += f'<text x="380" y="340" font-size="30" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="Nunito Sans, Arial">Spots 0 to 6 on each half.</text><text x="380" y="390" font-size="30" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="Nunito Sans, Arial">2 | 5 and 5 | 2 are the same domino.</text><text x="380" y="445" font-size="32" font-weight="700" text-anchor="middle" fill="{TEAL}" font-family="Nunito Sans, Arial">How many dominoes in the set?</text></svg>'
gsv = f'<svg aria-label="Three digit boxes adding to 5 and a table by first digit" viewBox="0 0 760 470" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;display:block">'
for i, d in enumerate(['2', '0', '3']): gsv += f'<rect x="{200 + i * 130}" y="30" width="100" height="100" rx="14" fill="{YEL if i == 0 else SKY}" stroke="{NAVY}" stroke-width="4"/><text x="{250 + i * 130}" y="100" font-size="56" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="Fredoka, Arial">{d}</text>'
gsv += f'<text x="380" y="180" font-size="30" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="Nunito Sans, Arial">2 + 0 + 3 = 5. The first digit cannot be 0.</text>'
for i, lab in enumerate(['first digit', '1', '2', '3', '4', '5']):
    x = 30 + i * 118 if i else 30; wdt = 190 if i == 0 else 100; x = 30 if i == 0 else 230 + (i - 1) * 104
    gsv += f'<rect x="{x}" y="220" width="{wdt}" height="70" fill="{YEL if i == 0 else WHITE}" stroke="{NAVY}" stroke-width="3"/><text x="{x + wdt / 2}" y="266" font-size="28" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="Nunito Sans, Arial">{lab}</text>'
    gsv += f'<rect x="{x}" y="290" width="{wdt}" height="70" fill="{YEL if i == 0 else WHITE}" stroke="{NAVY}" stroke-width="3"/><text x="{x + wdt / 2}" y="336" font-size="28" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="Nunito Sans, Arial">{"how many?" if i == 0 else "?"}</text>'
gsv += f'<text x="380" y="430" font-size="32" font-weight="700" text-anchor="middle" fill="{TEAL}" font-family="Nunito Sans, Arial">Fill the table in order.</text></svg>'
body = h2('Challenge: see it', 60) + '<div style="display:flex;gap:32px;align-items:flex-start">' + card(f'<p style="font-size:28px;font-weight:700;color:{TEAL}">Q1: The domino set</p>' + dsv, extra='flex:1;min-width:0;padding:20px 24px') + card(f'<p style="font-size:28px;font-weight:700;color:{TEAL}">Q2: Digits that add up to 5</p>' + gsv, extra='flex:1;min-width:0;padding:20px 24px') + '</div>'
put(f'{PRE}-chdiag', sec(f'{PRE}-chdiag', 'Challenge', body, 'Show after pairs have tried, or if they are stuck. The pictures show the problem, not the answer. Ask: What do you notice? Which earlier idea does the domino set remind you of? (handshakes) How can a table keep the digit list in order?'))

# ---------- 24 challenge walk-through ----------
body = h2('Challenge: walk-through') + pin(128, 240, 800, p('Q1: doubles + handshakes', 38, 800, TEAL))
for i, t in enumerate(['Doubles: 0|0, 1|1, … 6|6 → 7', 'Two different numbers: like 7 friends shaking hands', '6 + 5 + 4 + 3 + 2 + 1 = 21', '7 + 21 = 28 dominoes ✓']): body += pin(128, 320 + i * 120, 800, p(t, 32), 'rise', WHITE)
body += pin(992, 240, 800, p('Q2: sort by the first digit', 38, 800, TEAL))
for i, t in enumerate(['1 _ _: the others add to 4 → 104, 113, 122, 131, 140 (5)', '2: 4 numbers.  3: 3.  4: 2.  5: 1 (500)', '5 + 4 + 3 + 2 + 1 = 15 numbers ✓', 'Test it: 3 nested loops, or check all 900 numbers']): body += pin(992, 320 + i * 120, 800, p(t, 32), 'rise', WHITE)
put(f'{PRE}-chwalk', sec(f'{PRE}-chwalk', 'Challenge', body, 'Use after pairs have tried. Q1: a domino with two different numbers is a pair of numbers from 0 to 6 where order does not matter: exactly the handshake idea with 7 "friends" (21), plus the 7 doubles. Q2: listing by first digit keeps the list in order; the counts 5, 4, 3, 2, 1 are another hidden handshake pattern. A program can test it: for every number from 100 to 999, add up the digits and count the ones that make 5 (it says 15).'))

# ---------- 25 talk ----------
body = h2('Talk time') + card(chip('TALK TIME', YEL, NAVY) + p(SC['talk'][0].strip('“”"'), 42, 600)) + card(p('Sentence starters:', 34, 400, MUTED) + p('“I noticed that …”   “I tested it by …”   “I know because …”', 38, 600))
put(f'{PRE}-talk', sec(f'{PRE}-talk', '75–82 MIN', body, 'Minutes 75 to 82. Pairs talk for 2 minutes, then share. Follow-up: ' + SC['talk'][1] + ' Answer: ' + SC['talkAns'] + ' Close: ' + SC['close'][0]))

# ---------- 26 exit ----------
body = h2('Exit ticket') + card(chip('EXIT TICKET') + p(L['exit']['q'], 46, 600)) + card(p('Write your answer on a slip of paper (or type it in the chat). Show it to your tutor. Then collect your stamp in your inquiry journal.', 34, 400))
put(f'{PRE}-exit', sec(f'{PRE}-exit', '82–90 MIN', body, 'Minutes 82 to 90. Answer: ' + L['exit']['a'] + ' Extension: ' + L['extension']))

# ---------- write ----------
order = [f'{PRE}-{x}' for x in ['title', 'warm1', 'warm2', 'explore1', 'explore2', 'teach1', 'we1', 'try1', 'teachcode', 'try2', 'key', 'break', 'teachcards', 'ws1', 'ws1ans', 'teachhand', 'teachhandcode', 'teachroute', 'ws2', 'ws2ans', 'stretch', 'challenge', 'chdiag', 'chwalk', 'talk', 'exit']]
assert set(order) == set(S), set(order) ^ set(S)
for f in os.listdir(os.path.join(D, 'slides')):
    if f.endswith('.html') and f[:-5] not in S: os.remove(os.path.join(D, 'slides', f))
for sid, h in S.items(): open(os.path.join(D, 'slides', sid + '.html'), 'w').write(h)
deck = {'v': 4, 'createdOnFiles': {'v': 1, 'at': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}, 'lists': 'css',
        'title': f'Math Inquirers P6: Lesson {N} – {L["title"]}', 'order': order, 'cover': order[0],
        'sections': {'s1': {'description': 'Warm-up and explore', 'start': f'{PRE}-title'}, 's2': {'description': 'Teach: the multiplication rule and nested loops', 'start': f'{PRE}-teach1'},
                     's3': {'description': 'Worksheet with teaching before each page', 'start': f'{PRE}-break'}, 's4': {'description': 'Stretch, challenge, talk and exit', 'start': f'{PRE}-stretch'}},
        'faces': {'fredoka': {'family': 'Fredoka', 'href': 'https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&display=swap'}, 'nunito-sans': {'family': 'Nunito Sans', 'href': 'https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@400;600;700&display=swap'}},
        'designSystems': []}
json.dump(deck, open(os.path.join(D, 'deck.json'), 'w'), indent=1, ensure_ascii=False)
print(len(order), 'slides')

import p6_gaps; p6_gaps.apply(5)
