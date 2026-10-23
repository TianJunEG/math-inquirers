"""Level 1 'Go further: see it' picture slides (final_fixes_levels_1_4.md).

The gifted-audit pass rebuilt the Go further slides from hp/qbank.json (rebuild/p1gifted.py) and dropped the old picture slide, which drew
the retired items.  This module draws NEW pictures for the CURRENT printed Go further items (challenge[-3:]) of every lesson.
Each picture shows the problem, never the answer (every panel is generated from numbers stated in the question).

apply(D, n) writes slide lN-chdiag and puts it in the deck order right after lN-challenge.  Called at the end of p1gifted.apply().  Idempotent.
"""
import os, json
from slidekit import *

RED = '#D64545'
SILVER = '#D5D8DC'
GOLD = '#E9D58A'
W, H = 800, 500


def svg(body, w=W, h=H, label=''):
    return (f'<svg aria-label="{E(label)}" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto">{body}</svg>')


def T(x, y, s, size=28, anchor='middle', weight=700, fill=NAVY, family="Nunito Sans, Arial"):
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" fill="{fill}" font-family="{family}">{E(str(s))}</text>'


def R(x, y, w, h, fill='none', stroke=NAVY, sw=3, rx=0, dash=False):
    d = ' stroke-dasharray="8 6"' if dash else ''
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>'


def C(x, y, r, fill='none', stroke=NAVY, sw=3, dash=False):
    d = ' stroke-dasharray="6 5"' if dash else ''
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>'


def L(x1, y1, x2, y2, stroke=NAVY, sw=3, dash=False, cap='round'):
    d = ' stroke-dasharray="8 6"' if dash else ''
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{sw}" stroke-linecap="{cap}"{d}/>'


def PATH(d, stroke=NAVY, sw=3, fill='none', dash=False):
    ds = ' stroke-dasharray="8 6"' if dash else ''
    return f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linecap="round"{ds}/>'


# ---------------------------------------------------------------- Lesson 1: patterns
def p1_gaps():
    x0, u, y = 40, 24, 330
    b = L(x0, y, x0 + 30 * u + 20, y, sw=4)
    for k in range(0, 31):
        x = x0 + k * u
        b += L(x, y - (14 if k % 5 == 0 else 7), x, y + (14 if k % 5 == 0 else 7), sw=2)
        if k % 5 == 0: b += T(x, y + 46, k, 24, weight=600)
    pts = [1, 2, 4, 7, 11, 16]
    for i, v in enumerate(pts):
        x = x0 + v * u
        if i:
            xa = x0 + pts[i - 1] * u
            hgt = 22 + (v - pts[i - 1]) * 14
            b += PATH(f'M{xa} {y - 14} Q{(xa + x) / 2} {y - 14 - 2 * hgt} {x} {y - 14}', stroke=TEAL, sw=4)
            b += T((xa + x) / 2, y - 22 - hgt * 1.25, f'+{v - pts[i - 1]}', 26, fill=TEAL, weight=800)
        b += C(x, y, 11, YEL, NAVY, 3)
    xl = x0 + 16 * u
    b += PATH(f'M{xl + 14} {y - 14} L{xl + 150} {y - 14}', stroke=TEAL, sw=4, dash=True)
    b += T(xl + 82, y - 34, '+ ?  …', 28, fill=TEAL, weight=800)
    return svg(b, label='Number line with dots at 1, 2, 4, 7, 11 and 16 and hops of +1, +2, +3, +4, +5')


def p1_chart():
    b = ''
    cw, ch, x0, y0 = 70, 62, 50, 20
    ali = set(range(2, 51, 3))
    for r in range(5):
        for c in range(10):
            n = r * 10 + c + 1
            x, y = x0 + c * cw, y0 + r * ch
            fill = '#BFE3DC' if n in ali else WHITE
            b += R(x, y, cw - 4, ch - 4, fill, NAVY, 2, 6)
            b += T(x + (cw - 4) / 2, y + 40, n, 26, weight=700)
    b += C(x0 + 33, y0 + 29, 30, 'none', RED, 5)
    b += T(400, 372, "Teal squares: Ali (from 2, in 3s).", 26, weight=700, fill=TEAL)
    b += T(400, 408, "Red ring: Mei starts at 1 and counts in 4s.", 26, weight=700, fill=RED)
    b += T(400, 444, "Mark Mei's numbers. Which squares are marked twice?", 26, weight=700)
    return svg(b, label='Number chart 1 to 50 with Ali\'s numbers shaded and Mei\'s start ringed')


# ---------------------------------------------------------------- Lesson 2: number bonds
def p2_shapes():
    b = ''
    def sq(x, y): return R(x, y, 64, 64, YEL, NAVY, 4, 8)
    def ci(x, y): return C(x + 32, y + 32, 34, '#BFE3DC', NAVY, 4)
    row1 = [ci, ci, sq]; row2 = [ci, sq, sq]
    for i, f in enumerate(row1): b += f(60 + i * 96, 70)
    b += T(430, 118, '= 12', 64, anchor='start', family="Fredoka, Arial", weight=700)
    for i, f in enumerate(row2): b += f(60 + i * 96, 230)
    b += T(430, 278, '= 9', 64, anchor='start', family="Fredoka, Arial", weight=700)
    b += T(400, 400, 'The same circle and the same square in every row.', 26, weight=700, fill=TEAL)
    b += T(400, 440, 'What number is each shape?', 28, weight=800)
    return svg(b, label='Two circles and a square make 12. A circle and two squares make 9.')


# ---------------------------------------------------------------- Lesson 3: picture graphs
def p3_bar():
    b = R(40, 130, 720, 80, WHITE, NAVY, 3, 8)
    u = 30
    b += R(40, 130, 6 * u, 80, '#F4B6B6', NAVY, 3, 8) + T(40 + 3 * u, 182, 'Apple 6', 30, weight=800)
    b += R(40 + 6 * u, 130, 18 * u, 80, WHITE, NAVY, 3, 0, dash=True) + T(40 + 6 * u + 9 * u, 182, 'Banana and orange ?', 30, weight=800, fill=TEAL)
    b += PATH('M40 108 L760 108', stroke=NAVY, sw=3) + L(40, 98, 40, 118) + L(760, 98, 760, 118)
    b += T(400, 90, '24 children voted', 30, weight=800)
    b += T(400, 280, 'Orange got 6 MORE votes than banana.', 28, weight=700, fill=TEAL)
    # two bars with the extra
    b += R(40, 320, 240, 60, '#FFE08A', NAVY, 3, 6) + T(160, 360, 'banana', 26, weight=700)
    b += R(40, 400, 240, 60, '#FFE08A', NAVY, 3, 6) + R(280, 400, 180, 60, '#FFB38A', NAVY, 3, 6, dash=True) + T(160, 440, 'orange', 26, weight=700) + T(370, 440, '6 more', 26, weight=800, fill=RED)
    return svg(b, label='A bar of 24 children split into apple 6 and the rest, with the banana and orange bars')


def p3_pict():
    b = T(400, 40, 'Key: 1 picture = 2 children', 28, weight=800, fill=TEAL)
    rows = [('A', 3, 0), ('B', 3, 2), ('C', 0, 0)]
    for i, (nm, solid, dashed) in enumerate(rows):
        y = 110 + i * 110
        b += T(60, y + 14, nm, 40, weight=800, family="Fredoka, Arial")
        for k in range(solid): b += C(140 + k * 80, y, 30, '#BFE3DC', NAVY, 3)
        for k in range(dashed): b += C(140 + (solid + k) * 80, y, 30, WHITE, RED, 4, dash=True)
        if nm == 'B': b += T(140 + 5 * 80 + 30, y + 10, '2 more than A', 24, anchor='start', weight=700, fill=RED)
        if nm == 'C': b += T(140, y + 10, '?', 44, anchor='start', weight=800, fill=TEAL) + T(210, y + 10, 'pictures', 26, anchor='start', weight=700)
    b += T(400, 450, '20 children voted for three fruits.', 28, weight=800)
    return svg(b, label='A picture graph with rows A (3 pictures), B (2 more than A) and C (unknown)')


# ---------------------------------------------------------------- Lesson 4: patterns
def p4_beads():
    cols = [RED, RED, '#3B6EC9', '#3B6EC9', '#2E9E57']
    b = ''
    for i in range(15):
        x = 50 + i * 47
        b += C(x, 150, 20, cols[i % 5], NAVY, 3) + T(x, 215, i + 1, 22, weight=600)
    b += T(745, 160, '…', 40, weight=800)
    b += T(400, 280, 'Red, red, blue, blue, green: the pattern repeats every 5 beads.', 26, weight=700, fill=TEAL)
    b += T(400, 330, 'How many green beads are in the first 47 beads?', 28, weight=800)
    b += T(400, 390, 'Can you spot where the first green beads sit? Count in 5s.', 26, weight=600)
    return svg(b, label='Fifteen beads in the repeating pattern red, red, blue, blue, green')


def p4_dots():
    b = ''
    x = 20
    for k in range(1, 6):
        # triangle of dots: row r has r+1 dots, centred on x+cx
        cx = x + 60
        for r in range(k):
            for c in range(r + 1):
                b += C(cx - r * 15 + c * 30, 80 + r * 30, 11, YEL, NAVY, 2)
        b += T(cx, 270, f'{[1, 3, 6, 10, 15][k - 1]}', 34, weight=800, fill=TEAL, family="Fredoka, Arial")
        x += 150
    b += T(400, 345, 'Dots: 1, 3, 6, 10, 15 …', 30, weight=800)
    b += T(400, 395, 'Each new triangle has one more row.', 26, weight=600, fill=TEAL)
    b += T(400, 440, 'What are the next two numbers? What is the 10th?', 28, weight=800)
    return svg(b, label='Triangles of dots with 1, 3, 6, 10 and 15 dots')


# ---------------------------------------------------------------- Lesson 5: working backwards
def machine_row(y, left_label, out_label, q_in):
    b = ''
    b += R(30, y - 40, 110, 80, WHITE if not q_in else '#FFF0C2', NAVY, 3, 14) + T(85, y + 14, left_label, 38, weight=800, family="Fredoka, Arial")
    b += T(85, y - 52, 'IN', 22, weight=800, fill=TEAL)
    b += L(140, y, 200, y, sw=4)
    b += R(200, y - 40, 150, 80, SKY, NAVY, 3, 14) + T(275, y + 12, 'add 3', 32, weight=800)
    b += L(350, y, 410, y, sw=4)
    b += R(410, y - 40, 150, 80, SKY, NAVY, 3, 14) + T(485, y + 12, 'add 4', 32, weight=800)
    b += L(560, y, 620, y, sw=4)
    b += R(620, y - 40, 120, 80, '#FFF0C2', NAVY, 3, 14) + T(680, y + 14, out_label, 38, weight=800, family="Fredoka, Arial")
    b += T(680, y - 52, 'OUT', 22, weight=800, fill=TEAL)
    return b


def p5_machine():
    b = machine_row(130, '5', '12', False) + machine_row(300, '?', '20', True)
    b += T(400, 420, 'Same machine, two jobs.', 26, weight=700, fill=TEAL)
    b += T(400, 462, 'What IN gives OUT 20? Can ONE box do the same job?', 28, weight=800)
    return svg(b, label='A machine that adds 3 then adds 4: IN 5 gives OUT 12, and IN ? gives OUT 20')


def p5_snail():
    b = ''
    x, y0, u = 160, 460, 46
    b += R(x - 14, y0 - 9 * u, 28, 9 * u, '#E8DCC8', NAVY, 3)
    for k in range(10):
        b += L(x + 14, y0 - k * u, x + 40, y0 - k * u, sw=2)
        b += T(x + 66, y0 - k * u + 9, k, 24, weight=700)
    b += T(x + 100, y0 - 9 * u + 9, 'cm  top', 22, anchor='start', weight=700, fill=TEAL)
    b += C(x - 14 - 34, y0 - 10, 26, '#BFE3DC', NAVY, 3) + T(x - 14 - 34, y0 - 2, 'S', 24, weight=800)
    ax, bx = x + 250, x + 320
    b += PATH(f'M{ax} {y0 - 6} L{ax} {y0 - 3 * u + 14}', stroke=TEAL, sw=6) + f'<polygon points="{ax},{y0 - 3 * u - 8} {ax - 14},{y0 - 3 * u + 16} {ax + 14},{y0 - 3 * u + 16}" fill="{TEAL}"/>'
    b += T(ax - 26, y0 - 1.5 * u, 'day: up 3 cm', 24, anchor='end', weight=800, fill=TEAL)
    b += PATH(f'M{bx} {y0 - 3 * u} L{bx} {y0 - 2 * u - 14}', stroke=RED, sw=6, dash=True) + f'<polygon points="{bx},{y0 - 2 * u + 8} {bx - 14},{y0 - 2 * u - 16} {bx + 14},{y0 - 2 * u - 16}" fill="{RED}"/>'
    b += T(bx + 26, y0 - 2 * u - 40, 'night: down 1 cm', 24, anchor='start', weight=800, fill=RED)
    b += T(520, 40, 'A 9 cm wall', 28, weight=800)
    return svg(b, label='A snail at the bottom of a 9 cm wall: up 3 cm each day, down 1 cm each night')


# ---------------------------------------------------------------- Lesson 6: money
def coin(x, y, r, label, fill=SILVER, dash=False):
    return C(x, y, r, fill, NAVY, 4, dash=dash) + C(x, y, r - 8, 'none', NAVY, 1.5) + T(x, y + 10, label, 28 if r < 50 else 32, weight=800)


def p6_coins():
    b = coin(95, 150, 40, '5¢') + coin(240, 150, 46, '10¢') + coin(400, 150, 52, '20¢', GOLD) + coin(580, 150, 58, '50¢', GOLD)
    b += coin(400, 330, 64, '$1', WHITE, dash=True)
    b += T(400, 250, 'Four coins. How many different amounts can you make?', 26, weight=800)
    b += T(400, 425, 'What if you also had a $1 coin (100¢)?', 26, weight=800, fill=TEAL)
    return svg(b, label='Coins of 5 cents, 10 cents, 20 cents and 50 cents, and a dashed $1 coin')


def p6_table():
    b = T(400, 40, 'Sweet 15¢       Biscuit 20¢       Ben spends exactly 90¢', 26, weight=800, fill=TEAL)
    cw = 90; x0 = 150
    b += R(30, 80, 120, 60, SOFT, NAVY, 2) + T(90, 118, 'sweets', 24, weight=800)
    b += R(30, 140, 120, 60, SOFT, NAVY, 2) + T(90, 168, 'cost of', 20, weight=700) + T(90, 192, 'sweets', 20, weight=700)
    b += R(30, 200, 120, 60, SOFT, NAVY, 2) + T(90, 228, 'left for', 20, weight=700) + T(90, 252, 'biscuits', 20, weight=700)
    for k in range(7):
        x = x0 + k * cw
        b += R(x, 80, cw, 60, WHITE, NAVY, 2) + T(x + cw / 2, 120, k, 30, weight=800)
        b += R(x, 140, cw, 60, WHITE, NAVY, 2) + T(x + cw / 2, 180, 15 * k, 28, weight=600)
        b += R(x, 200, cw, 60, '#FFFDF4', NAVY, 2, 0, dash=True)
    b += T(400, 340, 'Fill in the last row. Can the biscuits fit exactly (20¢ each)?', 26, weight=800)
    b += T(400, 385, 'Find the one column that works.', 26, weight=600, fill=TEAL)
    return svg(b, label='A table of 0 to 6 sweets at 15 cents with an empty row for the money left for biscuits')


# ---------------------------------------------------------------- Lesson 7: shapes
def tri_lines(cx, k, w=220, h=190, top=40):
    x1, x2 = cx - w / 2, cx + w / 2
    b = f'<polygon points="{cx},{top} {x1},{top + h} {x2},{top + h}" fill="#FFF0C2" stroke="{NAVY}" stroke-width="4" stroke-linejoin="round"/>'
    for i in range(1, k + 1):
        xb = x1 + w * i / (k + 1)
        b += L(cx, top, xb, top + h, sw=3)
    return b


def p7_tri():
    b = ''
    for i, k in enumerate((1, 2, 3)):
        cx = 140 + i * 260
        b += tri_lines(cx, k)
        b += T(cx, 285, f'{k} line' + ('s' if k > 1 else ''), 28, weight=800, fill=TEAL)
        b += T(cx, 322, f'{[3, 6, 10][i]} triangles', 26, weight=700)
    b += T(400, 395, 'How many triangles with 4 lines? With 5 lines?', 28, weight=800)
    b += T(400, 440, 'Count the small ones first, then the bigger ones.', 26, weight=600, fill=TEAL)
    return svg(b, label='Big triangles with 1, 2 and 3 lines from the top corner to the bottom')


def p7_sq():
    b = R(250, 40, 300, 300, WHITE, NAVY, 4)
    b += L(400, 40, 400, 340, sw=4) + L(250, 190, 550, 190, sw=4)
    b += L(325, 40, 325, 190, sw=2.5) + L(250, 115, 400, 115, sw=2.5)
    b += T(400, 395, 'A square cut into 4 equal squares.', 26, weight=700)
    b += T(400, 435, 'Then ONE small square is cut into 4 smaller squares.', 26, weight=700, fill=TEAL)
    b += T(400, 478, 'How many squares can you find?', 28, weight=800)
    return svg(b, label='A square cut into four squares with one of them cut into four smaller squares')


# ---------------------------------------------------------------- Lesson 8: logic
def p8_loops():
    b = C(300, 190, 150, 'rgba(31,122,111,0.12)', TEAL, 4) + C(500, 190, 150, 'rgba(255,201,60,0.25)', '#B8860B', 4)
    b += T(250, 40, 'I say it counting in 2s', 24, weight=800, fill=TEAL) + T(560, 40, 'counting in 3s', 24, weight=800, fill='#8A6508')
    b += T(400, 195, 'both', 26, weight=700)
    for i in range(20):
        r, c = divmod(i, 10)
        x = 45 + c * 72
        y = 390 + r * 62
        b += R(x, y, 62, 52, WHITE, NAVY, 2, 8) + T(x + 31, y + 36, i + 1, 28, weight=700)
    b += T(400, 355, 'Move the numbers 1 to 20 into the loops.', 24, weight=700)
    return svg(b, h=520, label='Two overlapping loops labelled counting in 2s and counting in 3s with number tiles 1 to 20')


def p8_grid():
    b = ''
    cols = ['cat', 'dog', 'fish']
    for j, c in enumerate(cols): b += R(250 + j * 160, 60, 150, 70, SOFT, NAVY, 3) + T(325 + j * 160, 105, c, 30, weight=800)
    for i in range(3):
        b += R(60, 140 + i * 90, 180, 80, SOFT, NAVY, 3) + T(150, 190 + i * 90, ['friend 1', 'friend 2', 'friend 3'][i], 26, weight=800)
        for j in range(3): b += R(250 + j * 160, 140 + i * 90, 150, 80, WHITE, NAVY, 3)
    b += T(400, 440, 'Tick where a clue fits, cross where it cannot.', 26, weight=700, fill=TEAL)
    b += T(400, 478, 'Write clues so only ONE grid is left.', 26, weight=800)
    return svg(b, label='An empty grid of three friends by three pets')


# ---------------------------------------------------------------- Lesson 9: length
def p9_train():
    b = ''
    u = 36
    x = 40
    for car in range(3):
        for k in range(6):
            b += R(x + k * u, 110, u - 4, u - 4, '#BFE3DC' if car % 2 == 0 else '#FFE08A', NAVY, 3, 5)
        b += T(x + 3 * u - 2, 100, '6 cubes', 24, weight=800, fill=TEAL)
        x += 6 * u
        if car < 2:
            b += R(x, 110, u - 4, u - 4, WHITE, RED, 3, 5, dash=True)
            if car == 0: b += T(x + 18, 190, '1 cube gap', 22, anchor='start', weight=800, fill=RED)
            x += u
    b += T(400, 275, 'A train of 3 carriages, with a gap between carriages.', 26, weight=700)
    b += T(400, 322, 'How long is the whole train in cubes?', 28, weight=800)
    b += T(400, 372, 'What if there are 5 carriages?', 26, weight=800, fill=TEAL)
    return svg(b, label='A train of three carriages of 6 cubes with a one cube gap between them')


def p9_ribbon():
    u = 14
    b = T(400, 36, 'A ribbon of 30 cubes is cut into 3 pieces', 26, weight=800)
    mid = 10 * u * 2  # drawn mid width (unknown length, shown schematically)
    base = 220
    b += R(60, 70, base + 4 * u, 58, '#FFE08A', NAVY, 3, 6) + R(60 + base, 70, 4 * u, 58, '#FFB38A', NAVY, 3, 6) + T(60 + base / 2, 108, 'first piece', 26, weight=800) + T(60 + base + 2 * u, 108, '+4', 24, weight=800, fill=RED)
    b += R(60, 160, base, 58, '#FFE08A', NAVY, 3, 6) + T(60 + base / 2, 198, 'second piece  ?', 26, weight=800)
    b += R(60, 250, base - 4 * u, 58, '#FFE08A', NAVY, 3, 6) + R(60 + base - 4 * u, 250, 4 * u, 58, WHITE, RED, 3, 6, dash=True) + T(60 + (base - 4 * u) / 2, 288, 'third', 26, weight=800) + T(60 + base - 2 * u, 288, '−4', 24, weight=800, fill=RED)
    b += T(400, 375, 'The first piece is 4 cubes longer than the second.', 26, weight=700)
    b += T(400, 415, 'The third piece is 4 cubes shorter than the second.', 26, weight=700)
    b += T(400, 462, 'How long is each piece?', 28, weight=800, fill=TEAL)
    return svg(b, label='Three ribbon pieces: the first 4 cubes longer than the second, the third 4 cubes shorter')


# ---------------------------------------------------------------- Lesson 10: mixed puzzles
def tri_row(x, y, k, s=84, h=72):
    b = ''
    v = []
    for j in range(k + 2):
        v.append((x + j * s / 2, y + h if j % 2 == 0 else y))
    for j in range(k + 1): b += L(*v[j], *v[j + 1], stroke=NAVY, sw=5)
    for j in range(k): b += L(*v[j], *v[j + 2], stroke=NAVY, sw=5)
    return b


def sq_row(x, y, k, s=64):
    b = ''
    for j in range(k + 1): b += L(x + j * s, y, x + j * s, y + s, sw=5)
    b += L(x, y, x + k * s, y, sw=5) + L(x, y + s, x + k * s, y + s, sw=5)
    return b


def p10_sticks():
    b = T(400, 40, 'Rows of triangles', 28, weight=800, fill=TEAL)
    for i, k in enumerate((1, 2, 3)):
        b += tri_row(40 + [0, 150, 350][i], 62, k)
        b += T(40 + [0, 150, 350][i] + (k + 1) * 21, 162, f'{2 * k + 1} sticks', 22, weight=700)
    b += T(400, 250, 'Rows of squares', 28, weight=800, fill=TEAL)
    for i, k in enumerate((1, 2, 3)):
        b += sq_row(40 + [0, 150, 350][i], 280, k)
        b += T(40 + [0, 150, 350][i] + k * 32, 372, f'{3 * k + 1} sticks', 22, weight=700)
    b += T(400, 440, 'Which numbers of sticks work for BOTH rows, up to 31?', 26, weight=800)
    b += T(400, 478, 'Same number of sticks, none left over.', 26, weight=600)
    return svg(b, label='Rows of 1, 2 and 3 triangles using 3, 5 and 7 sticks and rows of 1, 2 and 3 squares using 4, 7 and 10 sticks')


def p10_bars():
    u = 26
    b = ''
    a = 6  # drawn schematically
    b += R(130, 60, a * u, 56, '#BFE3DC', NAVY, 3, 6) + T(60, 98, 'Ali', 28, weight=800) + T(130 + a * u / 2, 98, '?', 30, weight=800)
    b += R(130, 150, a * u, 56, '#FFE08A', NAVY, 3, 6) + R(130 + a * u, 150, 4 * u, 56, '#FFB38A', NAVY, 3, 6) + T(60, 188, 'Ben', 28, weight=800) + T(130 + a * u + 2 * u, 188, '+4', 24, weight=800, fill=RED)
    b += R(130, 240, a * u + 1 * u, 56, '#FFE08A', NAVY, 3, 6) + R(130 + a * u + u, 240, 3 * u, 56, WHITE, RED, 3, 6, dash=True) + T(60, 278, 'Mei', 28, weight=800) + T(130 + a * u + 2.5 * u, 278, '−3', 24, weight=800, fill=RED)
    b += T(400, 370, 'Ben has 4 more than Ali. Mei has 3 fewer than Ben.', 26, weight=700)
    b += T(400, 412, 'Together they have 29.', 28, weight=800)
    b += T(400, 458, 'How many does each child have?', 28, weight=800, fill=TEAL)
    return svg(b, label='Three bars: Ali, Ben with 4 more than Ali, Mei with 3 fewer than Ben')


PANELS = {
    1: [(p1_gaps(), 'C1: what is added each time?'), (p1_chart(), 'C2: two counting patterns')],
    2: [(p2_shapes(), 'C1: two shapes, two totals'), (None, 'C3: change the magic triangle')],
    3: [(p3_bar(), 'C1: 24 children voted'), (p3_pict(), 'C2: a picture graph')],
    4: [(p4_beads(), 'C1: beads in a pattern of 5'), (p4_dots(), 'C2: dots that grow')],
    5: [(p5_machine(), 'C1: a machine with two boxes'), (p5_snail(), 'C2: the snail')],
    6: [(p6_coins(), 'C1: how many amounts?'), (p6_table(), 'C2: sweets and biscuits')],
    7: [(p7_tri(), 'C1: triangles in a triangle'), (p7_sq(), 'C2: squares in a square')],
    8: [(p8_loops(), 'C2: two loops'), (p8_grid(), 'C3: a clue grid')],
    9: [(p9_train(), 'C1: a train of cubes'), (p9_ribbon(), 'C2: a ribbon in three pieces')],
    10: [(p10_sticks(), 'C1: sticks in two rows'), (p10_bars(), 'C2: three children')],
}


def _tri_panel():
    from slidekit import triangle_svg
    return '<div style="display:flex;justify-content:center">' + triangle_svg(None, 330, 285, 'with numbers 2 to 7') + '</div>' + p('Use the numbers 2, 3, 4, 5, 6 and 7 once each. Can every side add to the same total? Which totals can you make?', 26, 700, TEAL)


def apply(D, n):
    panels = list(PANELS[n])
    if n == 2:
        panels[1] = (_tri_panel(), 'C3: change the magic triangle')
    sid = 'l%d-chdiag' % n
    body = h2('Go further: see it', 60)
    cards = ''
    for svgs, cap in panels:
        cards += (f'<div style="background:{WHITE};border-radius:24px;padding:18px 24px;display:flex;flex-direction:column;gap:6px;flex:1;min-width:0">'
                  f'<p style="font-size:26px;font-weight:800;color:{TEAL}">{E(cap)}</p>{svgs}</div>')
    body += f'<div style="display:flex;gap:28px;align-items:flex-start">{cards}</div>'
    notes = ('Show this picture slide only if a pair asks for it, or is stuck on Go further. The pictures show each problem, not its answer. '
             'Ask: What do you notice? What do we know? What do we not know yet? Can you draw or build it? Do not point out the answer; wait for a child to find a pattern.')
    s = sec(sid, 'Optional, if you finish early', body, notes)
    open(os.path.join(D, 'slides', sid + '.html'), 'w').write(s)
    dj = os.path.join(D, 'deck.json'); deck = json.load(open(dj)); o = deck['order']
    if sid in o: o.remove(sid)
    anchor = 'l%d-challenge' % n
    o.insert(o.index(anchor) + 1 if anchor in o else len(o), sid)
    json.dump(deck, open(dj, 'w'), indent=1, ensure_ascii=False)
