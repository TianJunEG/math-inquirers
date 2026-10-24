"""K2 Starter Pack: printable A4 PDF for parents of children aged 5-6 about to start Primary 1.
Run:  cd k2 && python3 k2_starter_pack.py      -> Math_Inquirers_K2_Starter_Pack.pdf
Every puzzle answer is computed in the VERIFY section below (brute force or direct count) and the answer page is
built from those computed values, so the printed answers cannot drift from the puzzles.
Style: parent edition (hp/parent_style.css), Fredoka and Nunito Sans (fonts/fonts.css), project palette."""
import os, sys, itertools, math
HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)
sys.path.insert(0, os.path.join(HERE, '..', 'diag'))
from lib import *   # NAVY TEAL YEL RED ... T R C L PG PL ARC SVG

# ---------------------------------------------------------------- VERIFY: compute every answer
ANS = {}
# 1. count on across a ten: 37 38 _ _ 41 _
track = [37, 38, None, None, 41, None]
full = list(range(37, 43))
assert all(t is None or t == f for t, f in zip(track, full))
ANS[1] = [f for t, f in zip(track, full) if t is None]                 # 39, 40, 42
# 2. order numbers to 50
cards = [41, 29, 35, 24]
ANS[2] = sorted(cards); biggest = max(cards)                           # 24 29 35 41
# 3. tens and ones: 3 full ten-frames + one frame with 4
frames = [10, 10, 10, 4]
ANS[3] = sum(frames); assert ANS[3] == 34 and 20 < ANS[3] < 50
# 4. bonds: 10 = 6 + _ , 5 = 2 + _
ANS[4] = (10 - 6, 5 - 2)
assert 6 + ANS[4][0] == 10 and 2 + ANS[4][1] == 5
# 5. hops that grow by one: 1 2 4 7 _ _
seq = [1]
for step in range(1, 6): seq.append(seq[-1] + step)                    # steps 1,2,3,4,5
assert seq[:4] == [1, 2, 4, 7]
ANS[5] = seq[4:6]                                                      # 11, 16
# 6. beads: R R B Y repeating; colour of 11th and 12th
unit = ['red', 'red', 'blue', 'yellow']
beads = [unit[i % 4] for i in range(12)]
ANS[6] = (beads[10], beads[11])                                        # blue, yellow
assert beads[:10] == ['red', 'red', 'blue', 'yellow', 'red', 'red', 'blue', 'yellow', 'red', 'red']
# 7. two-line picture sums: star + star + moon = 10 ; star + moon = 7  (whole numbers 1..10, must be unique)
sols = [(s, m) for s in range(1, 11) for m in range(1, 11) if 2 * s + m == 10 and s + m == 7]
assert len(sols) == 1
ANS[7] = sols[0]                                                       # star 3, moon 4
# 8. tower plan: heights on a 2 by 2 plan; total cubes, cubes to make every tower 3 tall
plan = [[3, 1], [2, 2]]
total = sum(map(sum, plan)); ANS[8] = (total, 4 * 3 - total)           # 8 cubes, 4 more
assert ANS[8] == (8, 4)
# 9. pizza: n straight cuts all through the middle at different angles make 2n pieces
def pieces_through_centre(angles):
    rays = {round(a % 360, 6) for a in angles} | {round((a + 180) % 360, 6) for a in angles}
    return len(rays)
cuts3 = [0, 60, 120]; cuts4 = cuts3 + [30]
ANS[9] = (pieces_through_centre(cuts3), pieces_through_centre(cuts4))  # 6, 8
assert ANS[9] == (6, 8) and len(set(cuts4)) == 4
# 10. ribbons measured in blocks
rib = {'A': 7, 'B': 5, 'C': 9}
longest = max(rib, key=rib.get); shortest = min(rib, key=rib.get)
ANS[10] = (longest, shortest, rib[longest] - rib[shortest])            # C, B, 4
assert len(set(rib.values())) == 3 and ANS[10] == ('C', 'B', 4)
print('all answers verified:', ANS)

# ---------------------------------------------------------------- drawing helpers
def box(x, y, w, h, fill=WHITE, dash=False): return R(x, y, w, h, fill, NAVY, 3, 12, dash)
def numrow(vals, w=560, bw=70, gap=None, y=6):
    n = len(vals); gap = (w - n * bw) / (n - 1) if gap is None and n > 1 else (gap or 0); b = ''
    for i, v in enumerate(vals):
        x = 4 + i * (bw + gap); blank = v is None
        b += R(x, y, bw, bw, WHITE if blank else YEL, NAVY, 3, 12, blank) + ('' if blank else T(x + bw / 2, y + 47, str(v), 32))
    return b
def numrow_svg(vals, w=560, bw=70, h=82, arcs=False):
    n = len(vals); gap = (w - n * bw) / (n - 1)
    b = numrow(vals, w, bw, gap)
    if arcs:
        b = ''
        b += numrow(vals, w, bw, gap, y=40)
        for i in range(n - 1):
            x1 = 4 + i * (bw + gap) + bw / 2; x2 = 4 + (i + 1) * (bw + gap) + bw / 2
            b += f'<path d="M{x1},38 Q{(x1+x2)/2},4 {x2},38" fill="none" stroke="{TEAL}" stroke-width="3.5"/>'
        h = 116
    return SVG(w + 8, h, b, f'max-width:{w+8}px')
def tenframe(a, cols=5, rows=2, cell=34, fill=RED):
    b = ''
    for r in range(rows):
        for c in range(cols):
            x = 3 + c * cell; y = 3 + r * cell; b += R(x, y, cell, cell, WHITE, NAVY, 2.5, 0)
            if r * cols + c < a: b += C(x + cell / 2, y + cell / 2, cell * 0.34, fill, NAVY, 2)
    return b, cols * cell + 6, rows * cell + 6
def frames_svg(counts, cell=34, gap=18):
    b = ''; x = 0
    for a in counts:
        g, w, h = tenframe(a, cell=cell)
        b += f'<g transform="translate({x},0)">{g}</g>'; x += w + gap
    return SVG(x, 2 * cell + 8, b, f'width:{x}px;max-width:100%')
def single_frame(a, cell=36, cols=5, rows=2):
    g, w, h = tenframe(a, cols, rows, cell); return SVG(w, h, g, f'width:{w}px')
def star(cx, cy, r=26, fill=YEL):
    pts = []
    for i in range(10):
        rr = r if i % 2 == 0 else r * 0.45; a = math.radians(-90 + i * 36)
        pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    return PG(pts, fill, NAVY, 3)
def moon(cx, cy, r=24):
    return C(cx, cy, r, '#DDEBF7', NAVY, 3) + C(cx + r * 0.45, cy - r * 0.2, r * 0.82, WHITE, WHITE, 0)
def starmoon():
    b = ''
    # line 1: star star moon = 10
    b += star(40, 40) + T(80, 50, '+', 30) + star(120, 40) + T(160, 50, '+', 30) + moon(200, 40) + T(250, 50, '=', 30) + T(300, 50, '10', 34, RED)
    # line 2: star moon = 7
    b += star(40, 110) + T(80, 120, '+', 30) + moon(120, 110) + T(170, 120, '=', 30) + T(220, 120, '7', 34, RED)
    return SVG(330, 150, b, 'width:240px')
def tower_plan(plan, cell=64):
    b = ''
    for r, row in enumerate(plan):
        for c, v in enumerate(row):
            b += R(4 + c * cell, 4 + r * cell, cell, cell, '#FFF4D1', NAVY, 3, 4) + T(4 + c * cell + cell / 2, 4 + r * cell + cell / 2 + 12, str(v), 34)
    n = len(plan[0]) * cell + 8
    return SVG(n, len(plan) * cell + 8, b, f'width:{n}px')
def cube_stack(heights, w=60, h=26):
    # side view of towers: simple stacked squares
    b = ''
    for i, k in enumerate(heights):
        for j in range(k): b += R(4 + i * (w + 8), 4 + (max(heights) - 1 - j) * h, w, h, '#DDEBF7' if (i + j) % 2 else YEL, NAVY, 2.5, 3)
    return b
def pizza(angles, r=88):
    cx = cy = r + 10; b = C(cx, cy, r, '#FFE3A8', NAVY, 4)
    for a in angles:
        t = math.radians(a); b += L(cx - r * math.cos(t), cy + r * math.sin(t), cx + r * math.cos(t), cy - r * math.sin(t), NAVY, 4)
    return SVG(2 * r + 20, 2 * r + 20, b, f'width:{2*r+20}px')
def ribbons(rib, unit=36):
    b = ''; y = 6
    cols = {'A': '#FFD1D1', 'B': '#D3F1E4', 'C': '#DDEBF7'}
    for k, n in rib.items():
        b += T(14, y + 25, k, 26, NAVY, 'middle', 800)
        for i in range(n): b += R(38 + i * unit, y, unit, 34, cols[k], NAVY, 2.5, 0)
        y += 46
    return SVG(38 + max(rib.values()) * unit + 8, y, b, 'width:%dpx' % (38 + max(rib.values()) * unit + 8))
BEADFILL = {'red': RED, 'blue': '#3B6FC9', 'yellow': YEL}
def bead_row():
    b = ''
    for i, c in enumerate(beads[:10]):
        b += C(30 + i * 56, 30, 22, BEADFILL[c], NAVY, 3) + T(30 + i * 56, 38, c[0].upper(), 20, WHITE if c != 'yellow' else NAVY, 'middle', 800)
    for i in range(2): b += R(8 + (10 + i) * 56 + 0, 8, 44, 44, WHITE, NAVY, 3, 22, True)
    return SVG(30 + 12 * 56, 62, b, 'width:100%;max-width:700px')
def cover_art():
    b = ''; heights = [1, 2, 3, 4]; cw = 92
    cols = [YEL, '#DDEBF7']
    for i, k in enumerate(heights):
        for j in range(k):
            b += R(60 + i * (cw + 14), 400 - (j + 1) * cw, cw, cw, cols[(i + j) % 2], NAVY, 5, 10)
    b += R(60 + 4 * (cw + 14), 400 - cw * 5, cw, cw * 5, WHITE, NAVY, 5, 10, True) + T(60 + 4 * (cw + 14) + cw / 2, 400 - cw * 2.3, '?', 86, RED)
    b += C(700, 90, 48, '#FFE3A8', NAVY, 5) + L(652, 90, 748, 90, NAVY, 4) + L(700, 42, 700, 138, NAVY, 4)
    b += PG([(640, 300), (700, 190), (760, 300)], '#D3F1E4', NAVY, 5)
    return SVG(800, 420, b, 'width:100%')

# ---------------------------------------------------------------- page furniture
CSS = open('../hp/parent_style.css').read() + """
@page{size:A4;margin:0}
.page{width:794px;height:1123px;position:relative;overflow:hidden;break-after:page;background:#fff;padding:52px 56px}
.page .cover{height:100%}
.foot{position:absolute;left:56px;right:56px;bottom:22px;font-size:11px;color:#5B6785;display:flex;justify-content:space-between;border-top:1px solid #D5DDEA;padding-top:6px}
.intro{font-size:16.5px;color:#3B4A6B;margin:-6px 0 10px}
.facts{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin:0 0 10px}
.facts div{background:#F3F6FA;border-top:5px solid #FFC93C;padding:10px 10px 8px;text-align:center;font-size:13px;line-height:1.3}
.facts b{display:block;font-family:'Fredoka',Arial,sans-serif;font-weight:600;font-size:21px;color:#1F7A6F;line-height:1.15;margin-bottom:2px}
.two{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.card{background:#F3F6FA;border-top:5px solid #1F7A6F;padding:11px 14px 10px;break-inside:avoid;font-size:14.6px;line-height:1.42}
.card h3{font-size:18px;color:#1F7A6F;margin-bottom:3px}
.card .t{font-weight:800;color:#D64545;font-size:11.5px;letter-spacing:.08em;text-transform:uppercase}
.card p{margin:0 0 5px}
.card ul{margin:0;padding-left:18px}.card li{margin-bottom:2px}
.sec{font-family:'Fredoka',Arial,sans-serif;font-weight:600;font-size:19px;margin:11px 0 6px;display:flex;align-items:center;gap:8px;color:#1B2A49}
.sec:after{content:"";flex:1;border-top:1.5px dashed #8A94AD}
ul.pl{margin:0 0 4px;padding-left:20px;font-size:14.5px;line-height:1.45}ul.pl li{margin-bottom:3px}
.sayt{width:100%;border-collapse:collapse;font-size:14px}
.sayt td{padding:6px 10px;border-bottom:1px dashed #C9D4EC;vertical-align:top;width:50%}
.sayt th{font-family:'Fredoka',Arial,sans-serif;font-weight:600;font-size:15px;text-align:left;padding:6px 10px;color:#fff}
.say th:first-child,.sayt th:first-child{background:#1F7A6F}.sayt th:last-child{background:#8A94AD}
.q{grid-template-columns:34px 1fr;margin-bottom:9px;border-bottom:1px solid #E6EBF3;padding-bottom:6px}
.q .txt{font-size:15.5px;font-weight:600;margin-bottom:5px}
.ans{display:inline-block;border-bottom:2px solid #1B2A49;min-width:70px;height:20px;vertical-align:bottom;margin:0 4px}
.row{display:flex;gap:18px;align-items:center;flex-wrap:wrap}
.ablk{break-inside:avoid;margin-bottom:10px}
.ar{display:grid;grid-template-columns:26px 1fr;gap:6px;font-size:14px;padding:4px 0;border-bottom:1px dashed #D5DDEA}
.note{font-size:12px;color:#5B6785;line-height:1.45}
.sm{font-size:12.5px;color:#3B4A6B}
"""
def foot(n): return f'<div class="foot"><span>K2 Starter Pack  •  Math Inquirers  •  Parent edition</span><span>{n}</span></div>'
def head(num, topic, title, kick='K2 Starter Pack  •  For parents of children aged 5 to 6'):
    return f'<div class="kick">{kick}</div><div class="hd"><div class="big">{num}</div><div><div class="tp">{topic}</div><h1>{title}</h1></div></div>'
def Q(n, text, svg='', extra=''):
    return f'<div class="q"><span class="n">{n}</span><div><div class="txt">{text}</div>{svg}{extra}</div></div>'
def A(w=70): return f'<span class="ans" style="min-width:{w}px"></span>'
def card(tag, title, body): return f'<div class="card"><div class="t">{tag}</div><h3>{title}</h3>{body}</div>'

pages = []
# ---- 1 cover
pages.append(f'''<div class="page"><div class="cover"><div class="kick">For parents of children aged 5 to 6, about to start Primary 1</div>
<div class="ctitle">K2 Starter<br><span>Pack</span></div>
<div class="lede">Short games to play at home, ten puzzles to try together, and what to expect from our friendly 15-minute readiness check. Buttons, spoons and blocks are all you need.</div>
<div class="rule"></div><div>{cover_art()}</div>
<div class="bottom"><div class="slogan">Notice it. Test it. Explain why.</div><div class="by">From the Math Inquirers Holiday Program<br>Preciouslyours Pte Ltd</div></div></div></div>''')

# ---- 2 the readiness check
pages.append(f'''<div class="page">{head('1', 'Before we meet', 'The 15-minute readiness check')}
<p class="intro">A short chat with a tutor over a few number games. Your child should feel they played, not that they sat a test.</p>
<div class="facts"><div><b>15 minutes</b>one child at a time</div><div><b>Free</b>we arrange it after you register</div><div><b>On video</b>with counters at home</div><div><b>You stay</b>a grown-up sits beside your child</div></div>
<div class="sec">What the tutor will notice</div>
<div class="two">
{card('Counting', 'Counting and numbers', '<ul><li>Counting out a number of counters, touching each one once</li><li>Reading numbers to 20 and writing a few</li><li>Counting on from a number, and back from 10</li></ul>')}
{card('Number sense', 'More, less and parts', '<ul><li>Which number is more, and how your child knows</li><li>One more and one less</li><li>Splitting 7 counters into two groups in more than one way</li><li>Small adding and taking-away stories</li></ul>')}
{card('Thinking', 'Patterns, shapes, reasons', '<ul><li>What comes next in a colour pattern or a counting pattern</li><li>Naming a circle, triangle, square and rectangle</li><li>Telling us how an answer was worked out, in words or with counters</li></ul>')}
{card('Working', 'How your child works', '<ul><li>Staying with a game for about 15 minutes with small reminders</li><li>Following a two-step request</li><li>Having another go when something is tricky</li></ul>')}
</div>
<div class="sec">What it is, and what it is not</div>
<ul class="pl"><li><b>It is not an entrance test.</b> There is no pass mark and no ranking, and your child is never compared with other children.</li>
<li><b>It helps us plan.</b> We use it to decide how to set up your child's place: which questions to start with, whether a little warm-up at home (like this pack) would be useful, and who might sit beside them.</li>
<li><b>It is about fit, not a grade.</b> If we think a later start would suit your child better, we will say so kindly and explain why. Many children simply enjoy it more after a term of Primary 1.</li>
<li><b>Wrong answers are welcome.</b> We say "Let's try another one". We stop early if your child is tired or upset.</li></ul>
<div class="sec">After the check</div>
<p class="sm" style="margin:0">Within a day we send <b>you</b> a short message: one thing your child did well and what we suggest next. We never message your child privately; the tutor speaks with you and your child together.</p>
{foot(2)}</div>''')

# ---- 3 home activities 1
pages.append(f'''<div class="page">{head('2', 'Play at home, part 1', 'Counting and number games')}
<p class="intro">Five minutes is plenty. Little and often works better than one long session. Stop while it is still fun.</p>
<div class="two">
{card('Counting to 20, then 50', 'Count everything', '<p>Count steps, stairs, spoons, stones, lift buttons. Count to 20 first, then stretch to 30, 40 and 50.</p><p><b>The tricky bit:</b> the jump to a new ten. Pause at 19, 29, 39 and ask "What comes next?" Count on from any number, not only from 1. Count back from 10, then from 20.</p>')}
{card('One-to-one counting', 'Touch it, move it, say it', '<p>Put 15 grapes or buttons in a heap. Ask: "Count out 12 for me." Your child touches each one once and moves it to a new pile, so none is counted twice or missed.</p><p>Then ask: "How many are left in the heap?"</p>')}
{card('Number bonds to 5', 'Fingers and cups', '<p>Show 5 fingers. Fold some down: "How many are hiding?" Put 5 counters under a cup, show 2 and ask how many are under the cup.</p><p>Try 3 and 2, 4 and 1, 5 and 0. Notice that 3 and 2 is the same as 2 and 3.</p>')}
{card('Number bonds to 10', 'The ten-frame', '<p>Draw two rows of 5 boxes (or use an egg box with 2 cups cut off). Put 7 counters in. "How many more to fill it?" Try every number from 1 to 9.</p><p>Say it as a story: "7 and 3 make 10."</p>')}
{card('Numbers 20 to 50', 'Tens and ones', '<p>Make bundles of 10 spoons or pasta tubes with rubber bands. 3 bundles and 4 loose ones is 34. Ask: "Which is more, 34 or 43? How do you know?"</p><p>Look for numbers on doors, buses and lifts, and read them aloud.</p>')}
{card('Writing numbers', 'Big and slow', '<p>Write numbers in sand, flour or on the window with a finger first, then with a pencil. Take care with 6, 9, 12, 17 and 19. Starting at the top and checking "does it face the right way?" matters more than speed.</p>')}
</div>
<div class="quote" style="margin-top:16px">Ask "How do you know?" even when the answer is right. That is where the thinking is.</div>
{foot(3)}</div>''')

# ---- 4 home activities 2
pages.append(f'''<div class="page">{head('3', 'Play at home, part 2', 'Patterns, shapes, lengths and blocks')}
<p class="intro">These games need no workbook. Use things you already have: socks, spoons, leaves, boxes, building blocks or LEGO bricks.</p>
<div class="two">
{card('Patterns', 'What comes next?', '<p>Make a row with socks or spoons: big, small, small, big, small, small, ... "What comes next? What will the 10th one be?" Clap and stamp patterns count too.</p><p>Then try a growing pattern with blocks: 1, 2, 3 blocks in towers. "How many in the next one?"</p>')}
{card('Shapes', 'Shape hunt', '<p>Find a circle, triangle, square and rectangle around the home. Count the sides and corners together. Make shapes with straws or playdough.</p><p>Fold a sheet of paper in half and in half again. How many boxes when you open it?</p>')}
{card('Comparing lengths', 'Longer, shorter, same', '<p>Line up a spoon, a shoe and a pencil, starting at the same line on the table. "Which is longest? Shortest? How can we be sure?"</p><p>Then measure with blocks or paper clips laid end to end. "The shoe is 6 blocks long."</p>')}
{card('Spatial play', 'Build it, then draw it', '<p>Build a tower of 5 blocks, and a wall of 3 rows. "How many blocks? How many can you see from the front? How many are hiding?"</p><p>Make a plan with numbers on squares: 3, 1, 2 means towers 3, 1 and 2 blocks tall. Can your child build it from the plan?</p>')}
{card('Paper play', 'Fold and cut', '<p>Fold a paper in half, cut a triangle from the folded edge, and guess before you open it: what will the hole look like? Draw a round pizza on paper and cut it with 1, 2 and then 3 straight lines. Count the pieces each time.</p>')}
{card('Left and right', 'Turn and tell', '<p>"Put the cup on the left of the plate." Turn around and ask again: "Where is the cup now?" Act it out with a teddy.</p>')}
</div>
<p class="note" style="margin-top:14px"><b>Safety:</b> keep small blocks, buttons, coins and dried beans away from younger brothers and sisters, and stay close while your child plays.</p>
{foot(4)}</div>''')

# ---- 5 talking about maths + what to bring
pages.append(f'''<div class="page">{head('4', 'Talk and prepare', 'Talking about maths, and what to bring')}
<div class="sec" style="margin-top:0">How to talk about maths at home</div>
<table class="sayt"><tr><th>Try saying</th><th>Rather than</th></tr>
<tr><td>"What do you notice?"</td><td>"Look, it is 5."</td></tr>
<tr><td>"How do you know?" or "Show me with the blocks."</td><td>"Yes, well done" or "No, try again."</td></tr>
<tr><td>"Mistakes help us. What could we try now?"</td><td>"That is easy" or "That is wrong."</td></tr>
<tr><td>"I like how you checked that."</td><td>"You are so clever."</td></tr>
<tr><td>"I wonder what happens if we add one more."</td><td>Telling the whole method straight away.</td></tr></table>
<ul class="pl" style="margin-top:10px"><li><b>Wait.</b> Count slowly to ten in your head before you help.</li><li><b>Use real things.</b> Counters and blocks make numbers visible.</li><li><b>Keep it short.</b> Five to ten minutes, then stop.</li><li><b>Use everyday moments.</b> "How many plates do we need?" "Which cup holds more?"</li><li><b>Notice it. Test it. Explain why.</b> Notice something, try it, then say how you know.</li></ul>
<div class="sec">What to bring to the readiness check</div>
<div class="two">
{card('Set out before we start', 'Things to have ready', '<ul><li>About 25 counters: buttons, coins, dried beans or LEGO bricks (keep them in a bowl until we ask)</li><li>A pencil and a sheet of paper</li><li>A laptop or tablet with the camera and sound on, steady on a table, so we can see the table and your child’s hands</li><li>A quiet table and a glass of water</li></ul>')}
{card('On the day', 'What helps', '<ul><li>A grown-up beside your child for the whole check, in view of the camera</li><li>A rested, fed child. A morning or after a nap is often best</li><li>A calm, light mood: "We are going to play some number games."</li><li>Please do not coach or prompt answers. If your child is unsure, that is useful for us to see</li></ul>')}
</div>
<p class="note" style="margin-top:10px">You do not need to practise before the check, and nothing in this pack is a "must do". If your child plays a few of the games, they will meet the same kinds of ideas.</p>
{foot(5)}</div>''')

# ---- 6 puzzles 1-5
p1 = Q(1, 'Count on. Write the missing numbers.', numrow_svg(track, 500, 66), f'<div class="sm">Say the numbers aloud as you go.</div>')

p2 = Q(2, 'Put these number cards in order, <b>smallest first</b>. Which is the biggest?',
       SVG(560, 70, ''.join(box(8 + i * 140, 4, 120, 62, YEL) + T(68 + i * 140, 50, str(v), 36) for i, v in enumerate(cards)), 'max-width:560px'),
       f'<div class="row sm" style="margin-top:4px">Smallest first: {A(40)}{A(40)}{A(40)}{A(40)} &nbsp; Biggest: {A(40)}</div>')
p3 = Q(3, 'The red counters are in tens frames. <b>How many counters in all?</b> (Count the full frames in tens.)',
       frames_svg(frames, 30, 16), f'<div class="row sm" style="margin-top:4px">In all: {A(60)}</div>')
bf = lambda a, cols, rows, cell=30: single_frame(a, cell, cols, rows)
p4 = Q(4, 'How many more counters make a full frame? Fill in the boxes.',
       f'<div class="row"><div>{bf(6,5,2)}<div class="sm"><b>10 = 6 + {A(36)}</b></div></div><div>{bf(2,5,1)}<div class="sm"><b>5 = 2 + {A(36)}</b></div></div></div>')
p5 = Q(5, 'The hops get <b>one bigger</b> each time. What are the next two numbers?',
       numrow_svg([1, 2, 4, 7, None, None], 500, 62, arcs=True), f'<div class="sm">How do you know?</div>')
pages.append(f'''<div class="page">{head('5', 'Practice puzzles, 1 to 5', 'Try these together')}
<p class="intro">Read each puzzle aloud. Let your child use buttons, blocks or fingers. You do not need to do all of them in one go. Answers are on page 8: look after you have tried.</p>
{p1}{p2}{p3}{p4}{p5}
{foot(6)}</div>''')

# ---- 7 puzzles 6-10
p6 = Q(6, 'Here is a bead pattern. <b>What colour is bead 11? And bead 12?</b>', bead_row(),
       f'<div class="row sm" style="margin-top:2px">R = red, B = blue, Y = yellow. &nbsp; Bead 11: {A(80)} &nbsp; Bead 12: {A(80)}</div>')
p7 = Q(7, 'Each shape is a secret number. <b>What is the star? What is the moon?</b> (Use the second line to help with the first.)', starmoon(),
       f'<div class="row sm">Star = {A(40)} &nbsp; Moon = {A(40)}</div>')
p8 = Q(8, 'Towers of blocks, seen from above. Each number is how many blocks tall. <b>How many blocks in all? How many more blocks make every tower 3 tall?</b>',
       f'<div class="row">{tower_plan(plan, 46)}<div class="sm">Build it with blocks to check.<br>Blocks in all: {A(40)}<br>More blocks needed: {A(40)}</div></div>')
p9 = Q(9, 'A round pizza has 3 straight cuts, all through the middle. <b>How many pieces?</b> One more cut through the middle: <b>how many pieces now?</b>',
       f'<div class="row">{pizza(cuts3, 52)}<div class="sm">3 cuts: {A(40)} pieces<br>4 cuts: {A(40)} pieces</div></div>')
p10 = Q(10, 'Three ribbons are measured in blocks. <b>Which is longest? Which is shortest? How many blocks longer is the longest than the shortest?</b>', ribbons(rib, 28),
        f'<div class="row sm" style="margin-top:4px">Longest: {A(36)} &nbsp; Shortest: {A(36)} &nbsp; Longer by: {A(36)} blocks</div>')
pages.append(f'''<div class="page">{head('6', 'Practice puzzles, 6 to 10', 'More to try together')}
{p6}{p7}{p8}{p9}{p10}
{foot(7)}</div>''')

# ---- 8 answers (computed above)
a1 = ', '.join(map(str, ANS[1])) + f' (after 39 comes 40, a new ten)'
ans = [
 a1,
 ', '.join(map(str, ANS[2])) + f'. The biggest is {biggest}. Compare the tens first, then the ones.',
 f'{ANS[3]} counters: 3 full frames make 30, and 4 more.',
 f'{ANS[4][0]} (10 = 6 + {ANS[4][0]}) and {ANS[4][1]} (5 = 2 + {ANS[4][1]}).',
 f'{ANS[5][0]} and {ANS[5][1]}. The hops grow: +1, +2, +3, +4, +5.',
 f'Bead 11 is {ANS[6][0]} and bead 12 is {ANS[6][1]}. The pattern repeats every 4 beads: red, red, blue, yellow.',
 f'Star = {ANS[7][0]}, moon = {ANS[7][1]}. Line 2 says star + moon = 7, so line 1 has one extra star: 10 - 7 = 3. Check: 3 + 3 + {ANS[7][1]} = 10.',
 f'{ANS[8][0]} blocks (3 + 1 + 2 + 2). Three-tall towers need 4 x 3 = 12, so {ANS[8][1]} more.',
 f'{ANS[9][0]} pieces, then {ANS[9][1]} pieces. Every cut through the middle adds 2 pieces.',
 f'Longest: {ANS[10][0]} (9 blocks). Shortest: {ANS[10][1]} (5 blocks). The longest is {ANS[10][2]} blocks longer.',
]
rows = ''.join(f'<div class="ar"><b style="font-family:Fredoka;color:#D64545">{i+1}</b><span>{t}</span></div>' for i, t in enumerate(ans))
pages.append(f'''<div class="page">{head('&#10003;', 'Look after you have tried', 'Answers')}
<p class="intro">A different way of thinking is fine, as long as your child can show or say how they know. Ask "How did you work it out?"</p>
<div class="ablk">{rows}</div>
<div class="sec">If a puzzle was hard</div>
<ul class="pl"><li>Use real things: counters for puzzles 1 to 5 and 7, blocks for 8, a drawing for 9, paper strips for 10.</li><li>Try a smaller example first, then come back.</li><li>Put it aside and try again next week. Being stuck is part of thinking.</li></ul>
<div class="sec">What next?</div>
<p class="sm" style="margin:0 0 10px">We arrange the free readiness check after you register for the Math Inquirers Holiday Program. Ten 90-minute lessons in small live online groups, hands-on puzzles, and a printed workbook posted to your home.</p>
<p class="note">Math Inquirers is enrichment for thinking skills. It does not promise exam results and is not affiliated with the Ministry of Education or the Gifted Education Programme. We will only email you if you sign up, and you can unsubscribe at any time. We speak to you and your child together, never to your child privately. Preciouslyours Pte Ltd, Singapore.</p>
{foot(8)}</div>''')

html = '<!doctype html><html><head><meta charset="utf-8"><title>Math Inquirers K2 Starter Pack</title><style>' + open('../fonts/fonts.css').read() + CSS + '</style></head><body>' + ''.join(pages) + '</body></html>'
open('_starter.html', 'w').write(html)
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': 794, 'height': 1123})
    pg.goto('file://' + os.path.abspath('_starter.html'), wait_until='networkidle'); pg.wait_for_timeout(800)
    # overflow check: content must end above the footer on every page
    bad = pg.evaluate('''()=>[...document.querySelectorAll('.page')].map((p,i)=>{const fe=p.querySelector('.foot');const f=fe?fe.getBoundingClientRect().top:1123;
      let m=0;for(const e of p.querySelectorAll('*')){if(e.closest('.foot'))continue;const r=e.getBoundingClientRect();if(r.height&&r.bottom>m)m=r.bottom}
      return [i+1,Math.round(m-p.getBoundingClientRect().top),Math.round(f-p.getBoundingClientRect().top)]})''')
    print('page, content bottom, footer top:', bad)
    pg.pdf(path='Math_Inquirers_K2_Starter_Pack.pdf', width='794px', height='1123px', print_background=True)
    b.close()
os.remove('_starter.html')
