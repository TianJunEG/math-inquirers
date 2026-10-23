"""Math Inquirers P6, Lesson 7: Turtle Geometry. Writes split/p6l7/project (deck.json + slides/*.html).
Text that the tutor guide also reads (today, warm-up, explore, key idea, talk, exit, question bank) comes from p6/content/l7.js.
Turtle pictures are computed by stepping a turtle (move, turn right) so every polygon and star is geometrically exact."""
import json, os, sys, math, re, subprocess, datetime
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, H)
import slidekit
from slidekit import *
slidekit.FOOT = 'Math Inquirers P6  •  Notice it. Test it. Explain why.'
ROOT = os.path.join(H, '..')
D = os.path.join(ROOT, 'split', 'p6l7', 'project'); os.makedirs(os.path.join(D, 'slides'), exist_ok=True)
C = json.loads(subprocess.check_output(['node', '-e', "const c=require(process.argv[1]);console.log(JSON.stringify({lesson:c.lesson,script:c.script,deck:c.deck,qbank:c.qbank}))", os.path.join(ROOT, 'p6', 'content', 'l7.js')]))
L, SC, DK, QB = C['lesson'], C['script'], C['deck'], C['qbank']
S = {}
def put(i, h): S[i] = h
RED = '#D64545'

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

# turtle: start at (0,0) heading h0 (degrees, clockwise from east on screen); 'right' turns clockwise on screen
def turtle_pts(n, turn, L=100, h0=0):
    x = y = 0.0; hd = h0; pts = [(0.0, 0.0)]
    for _ in range(n):
        x += L * math.cos(math.radians(hd)); y += L * math.sin(math.radians(hd)); pts.append((x, y)); hd += turn
    return pts
def fit(pts, x0, y0, w, h):
    xs = [p[0] for p in pts]; ys = [p[1] for p in pts]; bw = max(xs) - min(xs) or 1; bh = max(ys) - min(ys) or 1
    s = min(w / bw, h / bh); ox = x0 + (w - bw * s) / 2 - min(xs) * s; oy = y0 + (h - bh * s) / 2 - min(ys) * s
    return [(ox + a * s, oy + b * s) for a, b in pts], s
def arrow(x, y, hd, size=26, col=TEAL):
    a = math.radians(hd); f = (x + size * math.cos(a), y + size * math.sin(a))
    l = (x + size * 0.6 * math.cos(a + 2.5), y + size * 0.6 * math.sin(a + 2.5)); r = (x + size * 0.6 * math.cos(a - 2.5), y + size * 0.6 * math.sin(a - 2.5))
    return f'<polygon points="{f[0]:.1f},{f[1]:.1f} {l[0]:.1f},{l[1]:.1f} {r[0]:.1f},{r[1]:.1f}" fill="{col}" stroke="{NAVY}" stroke-width="2"/>'
def turtle_svg(n, turn, w, h, label, fill=SKY, closed=True, m=24, sw=5, h0=0, extra=''):
    pts, _ = fit(turtle_pts(n, turn, 100, h0), m, m, w - 2 * m, h - 2 * m)
    ps = ' '.join(f'{a:.1f},{b:.1f}' for a, b in pts)
    shape = f'<polygon points="{ps}" fill="{fill}" stroke="{NAVY}" stroke-width="{sw}" stroke-linejoin="round"/>' if closed else f'<polyline points="{ps}" fill="none" stroke="{NAVY}" stroke-width="{sw}" stroke-linejoin="round" stroke-linecap="round"/>'
    return SV(w, h, shape + arrow(pts[0][0], pts[0][1], h0) + extra, label)

def corner_svg(t=70, part='all'):
    B = (420, 120); A = (40, 120); r = math.radians
    Cc = (B[0] + 300 * math.cos(r(t)), B[1] + 300 * math.sin(r(t)))
    def pt(rad, a): return (B[0] + rad * math.cos(r(a)), B[1] + rad * math.sin(r(a)))
    def arc(rad, a1, a2, col): p1, p2 = pt(rad, a1), pt(rad, a2); return f'<path d="M{p1[0]:.1f} {p1[1]:.1f} A{rad} {rad} 0 0 1 {p2[0]:.1f} {p2[1]:.1f}" fill="none" stroke="{col}" stroke-width="7"/>'
    s = ''
    if part in ('base', 'all'):
        s += f'<line x1="{B[0]}" y1="{B[1]}" x2="{B[0]+250}" y2="{B[1]}" stroke="{NAVY}" stroke-width="4" stroke-dasharray="14 10"/>' + T(B[0] + 175, B[1] - 22, 'straight on', 28, MUTED, 600)
        s += f'<polyline points="{A[0]},{A[1]} {B[0]},{B[1]} {Cc[0]:.1f},{Cc[1]:.1f}" fill="none" stroke="{NAVY}" stroke-width="8" stroke-linejoin="round"/>' + arrow(170, 120, 0, 34)
    if part in ('turn', 'all'):
        q = pt(150, t / 2); s += arc(95, 0, t, RED) + T(q[0] + 10, q[1] + 14, f'turn {t}°', 34, RED, 800, 'start')
    if part in ('inside', 'all'):
        q = pt(118, 150); s += arc(62, t, 180, TEAL) + T(q[0] - 6, q[1] + 30, f'inside {180-t}°', 34, TEAL, 800, 'end')
    return s

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
        body += pin(128 + lw, y, 1664 - lw - 52, f'<p style="font-size:{size}px;font-weight:800;line-height:1.25">{E(b)}</p>', None, YEL, 20, '18px 26px')
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

PY = open(os.path.join(ROOT, 'p6', 'content', 'l7.js')).read().split('const PY = `')[1].split('`;')[0]
PYNOTE = 'Optional Python version (Python turtle module; it opens a drawing window), for children who already know Python:\n' + PY + '\nRun as it is, it draws the 5-point star and prints 144.0 720.0 (the turn, then the total turning). Change n and k: n, k = 8, 1 draws the octagon and prints 45.0 360.0.'

# ================= 1. title =================
inner = (f'<p style="font-size:32px;font-weight:700;letter-spacing:4px;color:{YEL}">LESSON 7  •  WEEK 4  •  MATHS + CODE</p>'
         f'<h1 style="font-family:{HF};font-size:128px;font-weight:600;line-height:1.05">Turtle Geometry</h1>'
         f'<p style="font-size:44px;color:#C9D4EC">Angles in polygons</p>'
         f'<div style="background:#26385F;border-radius:24px;padding:40px;display:flex;flex-direction:column;gap:12px"><p style="font-size:28px;font-weight:700;letter-spacing:3px;color:{YEL}">TODAY WE WILL</p><p style="font-size:44px;font-weight:600">{E(DK["today"])}</p></div>')
put('p6l7-title', dark('p6l7-title', NAVY, inner,
    f'Objective: {L["objective"]} Materials: {L["materials"]} Online: {L["online"]} Scratch set-up: before the lesson, check every child can open scratch.mit.edu and add the Pen extension (the button at the bottom left of the block menu). The turtle is any sprite with its pen down; in Scratch the turn block is "turn ↻ … degrees" (clockwise), shown on our slides as "turn right". '
    'Time plan: warm-up 0 to 10, explore at the computer 10 to 25, teaching 25 to 35 (click to reveal each step and answer), brain break 35 to 40, worksheet 40 to 75 with short teaching before each page and a check-together slide after it, talk time 75 to 82, exit ticket 82 to 90.'))

# ================= 2. warm-up 1: turtle says =================
cx, cy = 210, 210
comp = (f'<circle cx="{cx}" cy="{cy}" r="160" fill="{WHITE}" stroke="{NAVY}" stroke-width="5"/>'
        + ''.join(f'<line x1="{cx+150*math.cos(math.radians(a))}" y1="{cy+150*math.sin(math.radians(a))}" x2="{cx+130*math.cos(math.radians(a))}" y2="{cy+130*math.sin(math.radians(a))}" stroke="{NAVY}" stroke-width="4"/>' for a in range(0, 360, 45))
        + T(cx, cy - 175, 'N', 40) + T(cx + 190, cy + 14, 'E', 40) + T(cx, cy + 205, 'S', 40) + T(cx - 190, cy + 14, 'W', 40)
        + f'<polygon points="{cx},{cy-105} {cx-30},{cy+30} {cx},{cy+12} {cx+30},{cy+30}" fill="{TEAL}" stroke="{NAVY}" stroke-width="4"/>')
body = h2('Warm-up: Turtle says') + stitle('Stand up (or sit and use your arm as the turtle’s nose) and face the screen: that is north. Turn, then say which way you face.')
body += pin(128, 310, 420, SV(420, 440, comp, 'A compass with N, E, S and W. A turtle arrow points north.'))
cmds = [('1.', 'Turn right 90°', 'East'), ('2.', 'Turn right 180°', 'West'), ('3.', 'Turn left 270°', 'North'), ('4.', 'Turn right 45°', 'North-east'), ('5.', 'Turn right 360°', 'Still north-east')]
for i, (a, b, c) in enumerate(cmds):
    body += qrow(620, 290 + i * 104, 700, a, b, 36) + answer(1360, 290 + i * 104, 432, c)
body += qrow(620, 815, 700, '6.', 'A full turn in 3 equal turns?', 34) + answer(1360, 815, 432, '120° each')
put('p6l7-warm1', sec('p6l7-warm1', '0–5 MIN', body,
    'Turtle says (the game stays about 150 seconds; if you run late stop after call 4). Everyone stands (online: stand back from the camera) or sits and uses an arm as the turtle’s nose; nobody has to stand. The turns follow on from each other: each one starts where the last one ended. Call each turn, children turn their bodies, then ask "Which way are you facing?" and click to show it. '
    '1) right 90 from north: east. 2) right 180 from east: west. 3) left 270 from west: north (left 270 is the same as right 90). 4) right 45: north-east. 5) right 360: a full turn, still north-east. 6) "Make one full turn in 3 equal turns. How big is each?" 360 ÷ 3 = 120°. Ask: "Which other turn would have done the same as left 270?" (right 90). Keep this picture in mind: a full turn is 360°.'))

# ================= 3. warm-up 2 =================
qs = [(f'{i+1}.', q, a) for i, (q, a) in enumerate(DK['warmQs'])]
body = h2('Quick questions')
for i, (a, b, c) in enumerate(qs): body += qrow(128, 250 + i * 128, 1250, a, b, 34) + answer(1420, 250 + i * 128, 372, c)
put('p6l7-warm2', sec('p6l7-warm2', '5–10 MIN', body,
    'Three questions only. Read each aloud, give thinking time, take answers on whiteboards, then click. Ask "How do you know?" each time. 1) 360°. 2) 180 − 50 − 75 = 55°. 3) 45. These facts (straight line 180°, full turn 360°) are the two tools for today.'))

# ================= 3b. set-up blocks (keep drawings on the stage) =================
setup_prog = [('pen', 'erase all'), ('motion', 'go to x: {-50} y: {100}'), ('motion', 'point in direction {90}'), ('pen', 'pen down')]
body = h2('Set-up: 2 steps')
body += pin(128, 260, 700, blocks_svg(setup_prog, 'The 4 set-up blocks: erase all, go to x: -50 y: 100, point in direction 90, pen down', 34, 62), None)
body += step(1, 'Click the blue Add Extension button (bottom left) and pick Pen.', left=900, top=300, width=836, size=34)
body += step(2, 'Build these 4 blocks and keep them at the top of EVERY drawing.', left=900, top=480, width=836, size=34)
body += soft(128, 700, 1664, 'Or open the Turtle start file your tutor shares: the 4 blocks are already there. Turn ↻ is the clockwise turn (turn right).', 30)
# ================= 4. explore 1 =================
sq_prog = [('event', 'when green flag clicked'), ('pen', 'pen down'), ('ctrl', 'repeat {4}', [('motion', 'move {100} steps'), ('motion', 'turn ↻ {90} degrees')])]
bb, bw, bh = blocks(sq_prog, 24, 42)
sqp, _ = fit(turtle_pts(4, 90), 0, 0, 170, 170)
sq = f'<g transform="translate({bw+40},{bh/2-85:.0f})"><polygon points="{" ".join(f"{a:.1f},{b:.1f}" for a, b in sqp)}" fill="{SKY}" stroke="{NAVY}" stroke-width="5"/>{arrow(sqp[0][0], sqp[0][1], 0, 28)}</g>'
pic = SV(bw + 230, max(bh, 180), bb + sq, 'The square program as blocks: when green flag clicked, pen down, repeat 4: move 100 steps, turn ↻ 90 degrees. Beside it, the square it draws, with a turtle arrow at the start.')
lst = ''.join(f'<li>{E(x)}</li>' for x in DK['expSetup'])
body = h2('Explore: at the computer')
body += card(chip('EXPLORE, IN PAIRS') + f'<ol style="font-size:32px;font-weight:600;padding-left:48px;display:flex;flex-direction:column;gap:6px;line-height:1.25">{lst}</ol>', extra='padding:24px 40px')
body += card(f'<div style="display:flex;align-items:center;gap:40px">{pic}<p style="font-size:30px;font-weight:600;color:{MUTED};line-height:1.3">Record in a table: sides, turn, did it close? Begin with the 4 set-up blocks.</p></div>', extra='padding:12px 40px')
put('p6l7-explore1', sec('p6l7-explore1', '11–15 MIN', body,
    'The Set-up slide is merged into this one. The Turtle start file (L7_Turtle_Start.sb3, sent to families with the workbook; the tutor also keeps a copy) already has the 4 set-up blocks (erase all, go to x: -50 y: 100, point in direction 90, pen down), so children open it in about 60 seconds instead of building them; a child without the file adds the Pen extension (blue button, bottom left) and builds the 4 blocks. Say the stage size aloud: 480 wide, 360 tall, shapes grow right and DOWN; start at x: -50, y: 100 so every shape stays on the stage (up to 10 sides move 80, 12 to 15 sides move 50, 24 sides move 30, 36 sides move 10). Turn ↻ is clockwise, our turn right. One child drives Scratch, the other predicts the turn BEFORE each run; swap for each shape. Build the square program together first and run it. Then the challenge: change one number to get an equilateral triangle. Expect many pairs to type 60 (the inside angle): let them run it. It draws only half a hexagon. Ask: "How far did the turtle turn altogether? Did it come home?" '
    'Then the hexagon only (6 sides); the pentagon (5 sides, turn 72) is the Go further what-if. Finished early: the pentagon, then a regular shape with 10 sides. Online: breakout rooms, the driver shares their screen. Every run starts with the same 4 set-up blocks (erase all, go to x: -50 y: 100, point in direction 90, pen down) so each run starts clean and stays on the stage. Pairs add the other blocks below them. Use the clockwise arrow turn block.'))

# ================= 5. explore 2 =================
body = h2('Explore: talk about it') + ''.join(card(p(num(f'{i+1}.', q), 40, 600, raw=True)) for i, (q, a) in enumerate(DK['expAsk']))
put('p6l7-explore2', sec('p6l7-explore2', '15–25 MIN', body,
    'Two questions (1 and 3). Let pairs finish, then gather. Answers: ' + '  '.join(f'{i+1}) {a}' for i, (q, a) in enumerate(DK['expAsk'])) +
    ' Collect the table on the board: 3 sides 120°, 4 sides 90°, 5 sides 72°, 6 sides 60°, and multiply each pair. Do not name the rule yet: the teaching slides do that.'))

# ================= 6. teach 1: the turn is the outside angle =================
W0, H0 = 760, 440
base = SV(W0, H0, corner_svg(70, 'base'), 'A turtle walks along one side, reaches a corner and turns. A dashed line shows straight on.')
ov2 = SV(W0, H0, corner_svg(70, 'turn'), 'The turn from straight on, 70 degrees, marked in red')
ov3 = SV(W0, H0, corner_svg(70, 'inside'), 'The inside angle, 110 degrees, marked in teal')
body = h2('The turtle turns the OUTSIDE angle')
body += pin(128, 260, W0, base)
body += ostep(128, 260, 1, 'The turtle walks along a side. At the corner it turns away from “straight on”.', None, dx=W0 + 40, dy=0, tw=1664 - W0 - 40, size=32)
body += ostep(128, 260, 2, 'The turn is the angle between straight on and the new side: 70°.', ov2, W0, H0, dx=W0 + 40, dy=150, tw=1664 - W0 - 40, size=32)
body += ostep(128, 260, 3, 'The inside angle and the turn sit on one straight line: 110° + 70° = 180°.', ov3, W0, H0, dx=W0 + 40, dy=300, tw=1664 - W0 - 40, size=32)
body += soft(128, 740, 1664, 'Go once round a closed shape and come home facing the same way: the turns add up to one full turn, 360°.', 34)
put('p6l7-teach1', sec('p6l7-teach1', '25–26 MIN', body,
    'Teach. Act it out: walk along a line on the floor, stop at the "corner" and point straight on, then turn to face the new side. "How far did I turn? Not the angle inside the corner: the angle from straight on." Click 1: the walk. Click 2: the turn (red). Click 3: the inside angle (teal): angles on a straight line make 180°. Click 4: the big idea. '
    'Think-aloud: "In Explore the square needed 90 and the triangle needed 120, not 60. That is because the turtle turns the outside angle. Every time it comes home facing the way it started, it has turned exactly once round: 360°. Sides times turn was 360 every time."'))

# ================= 7. worked example 1: octagon =================
oct_prog = [('pen', 'pen down'), ('ctrl', 'repeat {8}', [('motion', 'move {80} steps'), ('motion', 'turn ↻ {45} degrees')])]
body = h2('Worked example: a regular octagon') + stitle('What turn draws a regular octagon? What is each inside angle?')
body += step(1, 'Going once round, the turtle turns 360° altogether.', top=320, width=1000, size=34)
body += step(2, '8 equal turns:  360° ÷ 8 = 45°  at each corner.', top=430, width=1000, size=34)
body += step(3, 'Inside angle = 180° − 45° = 135°.', top=540, width=1000, size=34)
body += pin(128, 660, 1040, f'<div style="display:flex;align-items:center;gap:28px"><p style="font-size:32px;font-weight:800;color:{TEAL}">Step 4. Code it (after set-up):</p>{blocks_svg(oct_prog, "Blocks: pen down, repeat 8: move 80 steps, turn ↻ 45 degrees", 26, 46)}</div>', 'fade', WHITE, 20, '14px 28px', 'width:1004px;box-sizing:border-box')
body += pin(1252, 300, 480, f'<p style="font-size:30px;font-weight:800;color:{TEAL}">Test it: it closes!</p>' + turtle_svg(8, 45, 480, 480, 'A regular octagon drawn by the turtle, with an arrow at the start', fill=SKY), 'fade', WHITE, 24, '18px 30px')
put('p6l7-we1', sec('p6l7-we1', '26–28 MIN', body,
    'Click through the steps; ask the group to predict each before you reveal it. Think-aloud: "' + SC['think'][0].strip('“”') + '" Step 4: build it live in Scratch and run it. Ask: "What would 8 turns of 135 draw?" (try it: it does not close after 8, because 8 × 135 = 1080, 3 times round, and it draws an 8-point star: a preview of the star slide). '
    + PYNOTE))

# ================= 8. your turn 1 =================
put('p6l7-try1', qa_slide('p6l7-try1', '28–29 MIN', 'Your turn: regular polygons', 'Whiteboards. Turn first, then the inside angle.',
    [('a', 'A regular 20-sided polygon. What is the turn?', '18°'), ('b', 'What is its inside angle?', '162°'), ('c', '360 sides: the turn and the inside angle? What does it look like?', '1° and 179°')],
    'Write it, say the answer together on three, then click. a) 360 ÷ 20 = 18°. b) 180 − 18 = 162°. c) 360 ÷ 360 = 1°, inside 179°: with tiny steps (move 1) it looks just like a circle. That is how Scratch artists draw circles: repeat 360 [move 1, turn right 1]. Let a fast pair test it.'))

# ================= 9. worked example 2: backwards =================
body = h2('Worked example: work backwards') + card(p('Each inside angle of a regular polygon is 174°. How many sides does it have?', 38, 700), extra='padding:24px 40px')
body += step(1, 'Turn = 180° − 174° = 6°.', top=420, size=34)
body += step(2, 'The turns make 360°, so the number of sides is 360 ÷ 6 = 60.', top=525, size=34)
body += step(3, 'Check: 60 × 6° = 360° ✓  A 60-gon.', top=630, size=34)
body += soft(128, 750, 1664, 'Inside angle 115°? Turn 65°, and 360 ÷ 65 = 5.53…  Not a whole number of sides: impossible!', 34)
put('p6l7-we2', sec('p6l7-we2', '29–31 MIN', body,
    'Click through. Think-aloud: "' + SC['think'][1].strip('“”') + '" The last box is the important twist: a turn angle must share 360 exactly. Ask: "Could a regular polygon have a turn of 7°?" (no: 360 ÷ 7 is not whole). "Which whole-number turns work?" (the factors of 360 that are less than 180: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 18, 20, 24, 30, 36, 40, 45, 60, 72, 90, 120).'))

# ================= 10. your turn 2 =================
put('p6l7-try2', qa_slide('p6l7-try2', '31–32 MIN', 'Your turn: work backwards', 'Turn first. Then share 360.',
    [('a', 'The turn is 4°. How many sides?', '90'), ('b', 'Each inside angle is 168°. How many sides?', '30'), ('c', 'Can a regular polygon have inside angles of 125°?', 'No: turn 55°')],
    'Whiteboards, then click. a) 360 ÷ 4 = 90. b) turn 180 − 168 = 12°, 360 ÷ 12 = 30. c) The turn would be 55°, and 360 ÷ 55 = 6.54…, not a whole number of sides. Ask a child to explain c in words.'))

# ================= 11. worked example 3: the star =================
star_prog = [('pen', 'pen down'), ('ctrl', 'repeat {5}', [('motion', 'move {150} steps'), ('motion', 'turn ↻ {144} degrees')])]
body = h2('Worked example: a 5-point star') + stitle('Change ONE number in the pentagon program.')
body += pin(128, 300, 1080, blocks_svg(star_prog, 'Blocks: pen down, repeat 5: move 150 steps, turn ↻ 144 degrees', 26, 46), None)
body += step(1, 'Add the turns: 5 × 144° = 720° = 2 full turns. It goes round twice.', top=525, width=1020, size=32)
body += step(2, 'Star rule: turn = 360° × times round ÷ points = 720° ÷ 5 = 144°.', top=645, width=1020, size=32)
body += step(3, 'Angle at each point = 180° − 144° = 36°.', top=765, width=1020, size=32)
body += pin(1260, 300, 472, turtle_svg(5, 144, 440, 440, 'A 5-point star drawn by the turtle with turn 144 degrees', fill=SKY), 'fade', WHITE, 24, '24px 30px')
put('p6l7-we3', sec('p6l7-we3', '32–34 MIN', body,
    'Ask first: "The pentagon was repeat 5, turn 72. What happens if I double the turn to 144?" Take predictions, then click through. Think-aloud: "' + SC['think'][2].strip('“”') + '" Last click: run it in Scratch (after the 4 set-up blocks) and show the star. '
    'Point out: the turtle still turns at 5 corners, but it goes round twice, so the turns add up to 720°, not 360°. The angle at each point is still on a straight line with the turn: 180 − 144 = 36°. Ask: "How many times round would a turn of 216 go?" (5 × 216 = 1080: 3 times; it is the same star drawn the other way round).'))

# ================= 12. key idea =================
body = h2(DK['keyHead']) + card(p(DK['keyBig'], 44, 700)) + card(p(DK['keySmall'], 38, 600, MUTED))
put('p6l7-key', sec('p6l7-key', '34–35 MIN', body,
    'Say the key idea together. Common mistakes to watch for during the worksheet: (1) ' + L['mistakes'][0] + ' (2) ' + L['mistakes'][1] + ' (3) ' + L['mistakes'][2]))

# ================= 13. break =================
put('p6l7-break', dark('p6l7-break', TEAL,
    f'<p style="font-size:32px;font-weight:700;letter-spacing:4px;color:{YEL}">35–40 MIN</p><h2 style="font-family:{HF};font-size:110px;font-weight:600;line-height:1.05">Brain break</h2>'
    f'<p style="font-size:48px;font-weight:600">{E(DK["brk"])}</p><p style="font-size:36px;color:#D7EFEA">Then: a drink of water and back to the computer.</p>',
    'Five minutes. Online: children stay in view of the camera and turn on the spot. Ask during the hexagon: "How big is each turn?" (60°, a sixth of a turn).', '#D7EFEA'))

# ================= 14–15. worksheet page 1 =================
put('p6l7-ws1', ws_preview('p6l7-ws1', '40–50 MIN', 'Worksheet page 1: with your partner',
    [('Q1', 'The polygon table: some rows forwards, some backwards. Test two rows. New words are in the box at the top.'), ('Q2', 'Ben’s nonagon program. Predict what it draws first, then run it.')],
    'Predict on paper first, then run it. If the screen surprises you, ask why.',
    'At the computer in pairs. Walk around. Ask "How do you know?" before giving any help. For Q2 insist on a written prediction before anyone runs the program.'))
put('p6l7-ws1ans', check2('p6l7-ws1ans', '50–52 MIN', 'Page 1: check together', [
    ('Q1', '9: 40°, 140°    10: 36°, 144°    36: 10°, 170°    turn 24°: 15 sides, 156°    inside 165°: turn 15°, 24 sides', 2),
    ('Q1a, b', 'Sides × turn is always 360°: one full turn.    b) No: turn 50°, 360 ÷ 50 = 7.2', 2),
    ('Q2', 'A triangle drawn 3 times over.  9 × 120° = 1080° (3 full turns).  Fix: change 120 to 40.', 2)],
    'All the answers are shown at once. Children mark in a different colour; ask ONE volunteer to explain only Q1 (the backwards rows), about 35 seconds a question. Q1: the backwards rows: 360 ÷ 24 = 15 sides, 180 − 24 = 156°; 180 − 165 = 15°, 360 ÷ 15 = 24 sides. Q2: 120 is the turn of a triangle, so after 3 moves the turtle is home, and the other 6 moves go round the same triangle twice more. Run it slowly in Scratch (add "wait 0.5 seconds" inside the loop) so children see it.'))

# ================= 16. teach before page 2: trace a running total =================
trace_prog = [('var', 'set {total} to {0}'), ('ctrl', 'repeat {5}', [('motion', 'move {150} steps'), ('motion', 'turn ↻ {144} degrees'), ('var', 'change {total} by {144}')]), ('looks', 'say {total}')]
body = h2('Trace the code: a running total') + stitle('Before you run it, follow the code one repeat at a time.')
body += pin(128, 310, 700, blocks_svg(trace_prog, 'Blocks: set total to 0, repeat 5: move 150 steps, turn ↻ 144 degrees, change total by 144; then say total', 26, 46), None)
Wt = [190, 170, 190]
body += trow(900, 300, ['repeat', 'turn', 'total'], Wt, None, True)
for i in range(5): body += trow(900, 380 + i * 78, [str(i + 1), '144', str(144 * (i + 1))], Wt, 'rise')
body += pin(128, 640, 640, p('Each row: add the turn to the total.', 30, 700), None, SOFT, 20, '18px 22px')
body += answer(128, 790, 1664, 'It says 720.   720 ÷ 360 = 2: the turtle goes round 2 times.')
put('p6l7-teachtrace', sec('p6l7-teachtrace', '52–53 MIN', body,
    'Teach before worksheet page 2 (Q3 traces a different star). Click to add each row while children say the next total. A trace table is how programmers check code by hand: one row for each time round the loop. Ask: "How do we know how many times the turtle went round?" (divide the total by 360).'))

# ================= 17. teach: plan a star =================
body = h2('Plan a star: 8 points, 3 times round')
body += step(1, 'Total turning: 3 × 360° = 1080°.', top=270, width=1020, size=34)
body += step(2, 'Turn: 1080° ÷ 8 = 135°.', top=375, width=1020, size=34)
body += step(3, 'Angle at each point: 180° − 135° = 45°.', top=480, width=1020, size=34)
body += pin(128, 600, 1080, f'<div style="display:flex;align-items:center;gap:28px"><p style="font-size:32px;font-weight:800;color:{TEAL}">Step 4. Code (after set-up):</p>{blocks_svg([("ctrl", "repeat {8}", [("motion", "move {200} steps"), ("motion", "turn ↻ {135} degrees")])], "Blocks: repeat 8: move 200 steps, turn ↻ 135 degrees", 26, 46)}</div>', 'fade', WHITE, 20, '14px 28px', 'width:1080px;box-sizing:border-box')
body += pin(1260, 270, 472, turtle_svg(8, 135, 440, 440, 'An 8-point star drawn by the turtle with turn 135 degrees', fill=SKY), 'fade', WHITE, 24, '24px 30px')
put('p6l7-teachstar', sec('p6l7-teachstar', '53–54 MIN', body,
    'Teach before worksheet page 2 (Q4 plans two different stars). Click through the steps, then the picture. Say the order out loud: times round → total turning → turn → point angle. Ask: "Which star has sharper points, this one or the 5-point star?" (the 5-point star: 36° is smaller than 45°).'))

# ================= 18. teach: add the inside angles =================
op, _ = fit(turtle_pts(8, 45), 40, 40, 420, 420)
cxo = sum(a for a, b in op[:8]) / 8; cyo = sum(b for a, b in op[:8]) / 8
labs = ''.join(T(a + (cxo - a) * 0.24, b + (cyo - b) * 0.24 + 10, '135°', 28, TEAL, 800) for a, b in op[:8])
octo = SV(500, 500, f'<polygon points="{" ".join(f"{a:.1f},{b:.1f}" for a, b in op)}" fill="{SKY}" stroke="{NAVY}" stroke-width="5" stroke-linejoin="round"/>' + labs, 'A regular octagon with 135 degrees marked inside each corner')
# ================= 19–20. worksheet page 2 =================
put('p6l7-ws2', ws_preview('p6l7-ws2', '55–72 MIN', 'Worksheet page 2: on your own',
    [('Q3', 'Trace the star program: fill in total after each repeat.'), ('Q4', 'Plan a star: total, turn, point angle. Test it.'), ('Q5', '★ Take-home: add up the inside angles. Find a rule for n sides.')],
    'Finished early? Stretch and Challenge come next.',
    'Children work alone on Q3 and Q4 (they may test in Scratch); Q5 (inside-angle sums) is the take-home question, marked with a star in the workbook. Show this preview, do not read it aloud. Note who needs a short catch-up next lesson.'))
put('p6l7-ws2ans', check2('p6l7-ws2ans', '72–75 MIN', 'Page 2: check together', [
    ('Q3', '80, 160, 240 … 720.  Says 720.  Round 2 times.  A 9-point star, 100° points.', 2),
    ('Q4', '9 points, 4 round: 1440°, 160°, 20°.', 2),
    ('Q5 ★', 'Take-home. 180°, 360°, 540°, 720°, 1440°.  +180° each time.  Rule: (n − 2) × 180°', 2)],
    'All the answers are shown at once. Children mark in a different colour; ask ONE volunteer to explain only Q3 (the running total). Q5 is the take-home question: its answer is here so children can mark it at home, and you take it up at the start of the next lesson (the octagon idea: every corner gives a straight line of 180°, the turns make 360°, so the inside angles add up to n × 180° − 360°). Q4: the 9-point star has the sharper points (20°). Q5: each inside angle 60, 90, 108, 120, 144; the rule can also be written n × 180 − 360 (the turtle way). Ask: "Why does one more side add 180°?" (one more corner adds one more straight line of 180°, and the turns still make 360°).'))

# ================= 21. stretch (3 new) =================
st = QB['stretch'][4:7]
body = h2('Stretch') + ''.join(card(p(num(f'{i+1}.', x['q']), 34, 600, raw=True), extra='padding:26px 40px') for i, x in enumerate(st))
put('p6l7-stretch', sec('p6l7-stretch', 'For early finishers', body, 'For children who finish early (not on the worksheet). Answers: ' + '  '.join(f'{i+1}) {x["a"]}' for i, x in enumerate(st))))

# ================= 22. challenge =================
ch = [QB['challenge'][0], QB['challenge'][3]]
body = h2('Challenge') + ''.join(card(p(num(f'{i+1}.', x['q']), 36, 600, raw=True)) for i, x in enumerate(ch))
put('p6l7-challenge', sec('p6l7-challenge', 'Challenge', body, 'Pairs try first (they may test ideas in Scratch), then use the "see it" slide if stuck, then the walk-through. Answers: ' + '  '.join(f'{i+1}) {x["a"]}' for i, x in enumerate(ch))))

# ================= 23. challenge: see it =================
ap = turtle_pts(5, 108); apf, _ = fit(ap, 40, 40, 640, 380)
ali = (f'<polyline points="{" ".join(f"{a:.1f},{b:.1f}" for a, b in apf)}" fill="none" stroke="{NAVY}" stroke-width="6" stroke-linejoin="round" stroke-linecap="round"/>' + arrow(apf[0][0], apf[0][1], 0, 30)
       + f'<circle cx="{apf[-1][0]:.1f}" cy="{apf[-1][1]:.1f}" r="12" fill="{RED}" stroke="{NAVY}" stroke-width="3"/>' + T(360, 452, 'repeat 5 [move 100, turn ↻ 108]', 30, NAVY, 700))
dots = ''
for i in range(12):
    a = math.radians(-90 + 30 * i); x, y = 330 + 170 * math.cos(a), 235 + 170 * math.sin(a)
    dots += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="16" fill="{YEL}" stroke="{NAVY}" stroke-width="3"/>' + T(330 + 212 * math.cos(a), 235 + 212 * math.sin(a) + 10, i, 28, NAVY, 700)
dots += T(330, 512, 'Jump the same number of dots each time', 28, TEAL, 800)
body = h2('Challenge: see it', 60) + '<div style="display:flex;gap:32px;align-items:flex-start">'
body += card(f'<p style="font-size:30px;font-weight:700;color:{TEAL}">Q1: Ali’s pentagon (where does it stop?)</p>' + SV(720, 470, ali, 'Ali’s drawing: 5 moves with turns of 108 degrees. It does not get back to the start, which is marked with an arrow; the end is a red dot.', 'width:100%;height:auto'), extra='flex:1;min-width:0;padding:20px 24px')
body += card(f'<p style="font-size:30px;font-weight:700;color:{TEAL}">Q2: 12 points round a circle</p>' + SV(660, 530, dots, '12 dots round a circle numbered 0 to 11', 'width:100%;height:500px'), extra='flex:1;min-width:0;padding:20px 24px')
body += '</div>'
put('p6l7-chdiag', sec('p6l7-chdiag', 'Challenge', body,
    'Show after pairs have tried, or if they are stuck. The pictures show the problem, not the answer. Q1: "Where would the turtle have to be to close the shape? How many more turns of 108 until the total is a whole number of full turns?" Q2: a star with 12 points joins every k-th dot, and the turn is 30° × k. "Join every 2nd dot. Every 3rd. Which jumps visit all 12 dots?"'))

# ================= 24. challenge walk-through =================
body = h2('Challenge: walk-through') + pin(128, 250, 800, p('Q1: when is the total a full number of turns?', 34, 800, TEAL))
for i, t in enumerate(['108 × 5 = 540°: 1½ turns. Not home.', '108, 216, 324, 432 … 1080 = 3 × 360', '10 repeats: a 10-point star, round 3 times', 'Each point: 180° − 108° = 72°']): body += pin(128, 330 + i * 110, 800, p(t, 32), 'rise', WHITE)
body += pin(992, 250, 800, p('Q2: turn = 30° × jump', 34, 800, TEAL))
for i, t in enumerate(['Jump 1: 12-gon.  Jump 2: hexagon, twice', 'Jump 3: square, 3 times.  Jump 4: triangle, 4 times', 'Jump 5: a star! Turn 150°, round 5 times ✓', 'Jump 6: a line. So only ONE 12-point star.']): body += pin(992, 330 + i * 110, 800, p(t, 32), 'rise', WHITE)
put('p6l7-chwalk', sec('p6l7-chwalk', 'Challenge', body,
    'Use after pairs have tried. Q1: list the multiples of 108 until one is a multiple of 360 (1080 = 3 × 360). Test it in Scratch: repeat 10 [move 150, turn right 108] draws a 10-point star. Q2: a jump that shares a factor with 12 (2, 3, 4, 6) gets back to 0 early and redraws a smaller shape; only jumps 1 and 5 (and 7 and 11, which are the same shapes the other way round) visit all 12 dots, and jump 1 is the 12-gon. Link to Q4 on the worksheet.'))

# ================= 25. talk =================
body = h2('Talk time') + card(chip('TALK TIME', YEL, NAVY) + p(SC['talk'][0].strip('“”'), 40, 600)) + card(p('Sentence starters:', 34, 400, MUTED) + p('“I noticed that …”   “I tested it by …”   “I know because …”', 38, 600))
put('p6l7-talk', sec('p6l7-talk', '75–82 MIN', body, 'One question only. Pairs talk for 90 seconds, then volunteers share. Second question (only if flex is left; otherwise the opener of the next lesson): ' + SC['talkNext'].strip('“”') + ' Answer: ' + SC['talkAns'] + ' Praise the reasons, not only the answers.'))

# ================= 26. exit =================
body = h2('Exit ticket') + card(chip('EXIT TICKET') + p(L['exit']['q'], 46, 600)) + card(p('Write your answer on a slip of paper. When your tutor says, say your answer together on three. Then collect your stamp in your inquiry journal.', 34, 400))
put('p6l7-exit', sec('p6l7-exit', '82–90 MIN', body, f'Minutes 82 to 90. Answer: {L["exit"]["a"]}. Children who write 175 sides and 5° have swapped the two steps: ask "Which angle does the turtle turn?" Extension: {L["extension"]}'))

# ---------- write ----------
order = ['p6l7-title', 'p6l7-warm1', 'p6l7-warm2', 'p6l7-explore1', 'p6l7-explore2', 'p6l7-teach1', 'p6l7-we1', 'p6l7-try1', 'p6l7-we2', 'p6l7-try2', 'p6l7-we3', 'p6l7-key', 'p6l7-break',
         'p6l7-ws1', 'p6l7-ws1ans', 'p6l7-teachtrace', 'p6l7-teachstar', 'p6l7-ws2', 'p6l7-ws2ans', 'p6l7-stretch', 'p6l7-challenge', 'p6l7-chdiag', 'p6l7-chwalk', 'p6l7-talk', 'p6l7-exit']
assert set(order) == set(S), set(order) ^ set(S)
for f in os.listdir(os.path.join(D, 'slides')):
    if f.endswith('.html') and f[:-5] not in S: os.remove(os.path.join(D, 'slides', f))
for i, h in S.items(): open(os.path.join(D, 'slides', i + '.html'), 'w').write(h)
deck = {'v': 4, 'createdOnFiles': {'v': 1, 'at': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}, 'lists': 'css',
        'title': 'Math Inquirers P6: Lesson 7 – Turtle Geometry', 'order': order, 'cover': 'p6l7-title',
        'sections': {'s1': {'description': 'Warm-up and explore at the computer', 'start': 'p6l7-title'}, 's2': {'description': 'Teach: the 360° turn, polygons and stars', 'start': 'p6l7-teach1'},
                     's3': {'description': 'Worksheet with teaching before each page', 'start': 'p6l7-break'}, 's4': {'description': 'Stretch, challenge, talk and exit', 'start': 'p6l7-stretch'}},
        'faces': {'fredoka': {'family': 'Fredoka', 'href': 'https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&display=swap'},
                  'nunito-sans': {'family': 'Nunito Sans', 'href': 'https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@400;600;700&display=swap'}},
        'designSystems': []}
json.dump(deck, open(os.path.join(D, 'deck.json'), 'w'), indent=1, ensure_ascii=False)
print(len(order), 'slides written to', os.path.normpath(D))

import p6_gaps; p6_gaps.apply(7)
