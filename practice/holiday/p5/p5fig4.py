"""Figures and small helpers for the Level 5 holiday lessons 7 (Percentage Puzzles) and 8 (Angle Chasers).

Plain inline SVG built with the shared helpers in practice/holiday/hlib.py (viewBox only, so a figure scales to a 390 px phone; the builder lifts the text to at
least 12 px).  The percentage figures are the workbook figures redrawn narrower; the angle figures are built from coordinates (every printed angle is checked with
`chk`, which stops the build if the drawing disagrees) like the workbook ones, one figure per shape so that each reads on a phone.  No question figure prints an
answer; every solution figure is built from the CHECKED values passed in.
"""
import math, os, sys
from fractions import Fraction

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from hlib import svg, T, Ln, Ci, Re, NAVY, YEL, TEAL, WARM, PALE      # noqa: E402,F401

SKY = '#CDE8F7'
GREY = '#44506F'
GREEN = '#E3F4EE'
SOFT = '#FFF0C2'


# ================================================================= lesson 7: percentages
def shops():
    """The two rice-cooker price tags, one under the other."""
    def tag(y, fill, title, lines):
        b = f'<polygon points="4,{y + 52} 36,{y + 4} 296,{y + 4} 296,{y + 104} 36,{y + 104}" fill="{fill}" stroke="{NAVY}" stroke-width="3" stroke-linejoin="round"/>'
        b += Ci(30, y + 52, 6.5, '#FFFFFF', NAVY, 2.5) + T(168, y + 28, title, 18, 'middle', 800)
        for i, (s, c) in enumerate(lines):
            b += T(168, y + 54 + i * 20, s, 15, 'middle', 800 if i == 0 else 700, c)
        return b
    body = tag(2, YEL, 'Shop A', [('$160 before GST', TEAL), ('20% OFF today!', NAVY), ('9% GST added at the till', NAVY)])
    body += tag(116, SKY, 'Shop B', [('$140', TEAL), ('GST already included', NAVY), ('No sale today', NAVY)])
    return svg(300, 228, body, 'Two price tags for the same rice cooker. Shop A: 160 dollars before GST, 20 percent off today, 9 percent GST added at the till. '
               'Shop B: 140 dollars, GST already included, no sale today.')


def _cap(x1, x2, y, text, size=15, fill=NAVY, up=True):
    d = -8 if up else 8
    b = f'<path d="M{x1} {y} V{y + d} H{x2} V{y}" fill="none" stroke="{NAVY}" stroke-width="2.4"/>'
    return b + T((x1 + x2) / 2, y + (2 * d if up else 4 * abs(d)) - (4 if up else -4), text, size, 'middle', 800, fill)


def rise_cut_bars(sol=None):
    """Q3: the $80 T-shirt.  Question: a bar for $80 (100%), a longer bar with a shaded extra part for the 25% rise, and a dashed empty bar for the cut.
    sol = (start, after_rise, after_cut) writes the checked dollars on the bars."""
    u, x0 = 44, 10
    b = T(x0, 16, 'At first', 15, 'start', 800)
    b += Re(x0, 22, 4 * u, 34, SKY, NAVY, 2.4) + T(x0 + 2 * u, 45, ('$%d = 100%%' % sol[0]) if sol else '$80 = 100%', 15, 'middle', 800)
    b += T(x0, 84, 'After the 25% rise', 15, 'start', 800)
    b += Re(x0, 90, 4 * u, 34, SKY, NAVY, 2.4) + Re(x0 + 4 * u, 90, u, 34, YEL, NAVY, 2.4) + T(x0 + 4.5 * u, 113, '+25%', 14, 'middle', 800)
    if sol:
        b += T(x0 + 2 * u, 113, '$%d' % sol[0], 15, 'middle', 800) + T(x0 + 5 * u + 6, 113, '= $%d' % sol[1], 15, 'start', 800, TEAL)
    b += T(x0, 152, 'The 20% cut', 15, 'start', 800)
    if sol:
        b += Re(x0, 158, 4 * u, 34, SKY, NAVY, 2.4) + T(x0 + 2 * u, 181, '$%d' % sol[2], 15, 'middle', 800, TEAL)
        b += Re(x0 + 4 * u, 158, u, 34, '#FFFFFF', NAVY, 2.4, 0, '5 4') + T(x0 + 4.5 * u, 181, 'cut', 14, 'middle', 800, WARM)
        b += T(x0, 212, 'The 20%% cut is of the $%d bar,' % sol[1], 14, 'start', 700, GREY) + T(x0, 230, 'not of the $%d bar.' % sol[0], 14, 'start', 700, GREY)
        return svg(300, 238, b, 'The bars with the checked prices: $%d at first, $%d after the 25%% rise, $%d after the 20%% cut of the new price.' % sol)
    b += Re(x0, 158, 5 * u, 34, '#FFFFFF', NAVY, 2.4, 0, '6 4') + T(x0 + 2.5 * u, 181, 'cut 20% of THIS price', 14, 'middle', 800)
    return svg(300, 202, b, 'A bar for the 80 dollar price. Under it a longer bar with a shaded extra part for the 25 percent rise. '
               'Under that a dashed empty bar as long as the new price, for the 20 percent cut.')


def bag_bar(sol=None):
    """Q4: a bar for $120 cut into 10 equal parts (each part 10%).  sol = (bag, book, left) shades the parts and writes the checked dollars."""
    x0, w, y, h = 5, 290, 34, 36
    cw = w / 10
    b = _cap(x0, x0 + w, y - 4, '$120', 16)
    colours = ['#FFFFFF'] * 10
    if sol:
        colours = [YEL] * 2 + [SKY] * 2 + [GREEN] * 6
    for k in range(10):
        b += Re(round(x0 + k * cw, 1), y, round(cw, 1), h, colours[k], NAVY, 2.4)
    b += T(x0 + w / 2, y + h + 22, 'Each part is 10% of $120.', 15, 'middle', 700, GREY)
    if sol:
        b += T(x0 + cw, y + h + 46, 'bag $%d' % sol[0], 14, 'middle', 800) + T(x0 + 4.2 * cw, y + h + 46, 'book $%d' % sol[1], 14, 'middle', 800) \
            + T(x0 + 8.0 * cw, y + h + 46, 'left $%d' % sol[2], 14, 'middle', 800, TEAL)
        return svg(300, 108, b, 'The bar of 120 dollars with the checked parts: the bag is 2 parts, $%d; the book is 25 percent of the 8 parts left, 2 parts, $%d; 6 parts are left, $%d.' % sol)
    return svg(300, 100, b, 'A bar for 120 dollars cut into 10 equal parts. Each part is 10 percent of 120 dollars.')


def class_table(sol=None):
    """Q5: the class of 40 pupils.  sol = (girls, boys, girls_glasses, boys_glasses) fills the table."""
    cw = [66, 70, 70, 94]
    xs = [4]
    for c in cw:
        xs.append(xs[-1] + c)
    rows = [['', 'Girls', 'Boys', 'Whole class'], ['Pupils', '?', '?', '40'], ['Glasses', '?', '?', '?']]
    if sol:
        g, bo, gg, bg = sol
        rows[1][1:] = [str(g), str(bo), '40']
        rows[2][1:] = [str(gg), str(bg), str(gg + bg)]
    body = ''
    for r, row in enumerate(rows):
        y = 4 + r * 40
        for c, s in enumerate(row):
            head = r == 0 or c == 0
            q = s == '?'
            new = bool(sol) and r > 0 and 0 < c < 3 or (bool(sol) and r == 2 and c == 3)
            body += Re(xs[c], y, cw[c], 40, '#E4E8F0' if head else (PALE if q else (GREEN if new else '#FFFFFF')), NAVY, 2.2, 0, '5 4' if q else None)
            if s:
                body += T(xs[c] + cw[c] / 2, y + 26, s, 15 if head else 18, 'middle', 800, TEAL if new else NAVY)
    lab = ('The class table. Girls, Boys and Whole class; rows Pupils and Glasses. The whole class has 40 pupils. The other cells are empty.' if not sol else
           'The completed table: girls %d, boys %d, whole class 40 pupils; glasses: girls %d, boys %d, whole class %d.' % (sol[0], sol[1], sol[2], sol[3], sol[2] + sol[3]))
    return svg(xs[-1] + 4, 128, body, lab)


def discount_bars(first, second, price=100, sol=False):
    """Investigation: the price as a bar, after the first discount and after the second (checked dollars written on the bars; used only as a solution picture)."""
    x0, w = 14, 270
    f1 = Fraction(price) * (100 - first) / 100
    f2 = f1 * (100 - second) / 100
    body = ''
    for i, (name, v) in enumerate((('At first', Fraction(price)), (f'After {first}% off', f1), (f'Then {second}% off the new price', f2))):
        y = 6 + i * 62
        body += T(x0, y + 14, name, 14, 'start', 800)
        body += Re(x0, y + 20, round(w * float(v) / price, 1), 28, YEL if i == 0 else (SKY if i == 1 else GREEN), NAVY, 2.4) + T(x0 + w * float(v) / price / 2, y + 40, '$%g' % float(v), 15, 'middle', 800)
    return svg(300, 194, body, f'Three bars: ${price} at first, ${float(f1):g} after {first} percent off, ${float(f2):g} after a further {second} percent off.')


# ================================================================= lesson 8: angles
def rad(d):
    return math.radians(d)


def P(v, r, deg):
    """A point at distance r from v in the maths direction deg (anticlockwise, y up) as a screen point."""
    return (v[0] + r * math.cos(rad(deg)), v[1] - r * math.sin(rad(deg)))


def ang(v, a, b):
    d = abs(math.atan2(a[1] - v[1], a[0] - v[0]) - math.atan2(b[1] - v[1], b[0] - v[0])) * 180 / math.pi
    return 360 - d if d > 180 else d


def dist(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])


def chk(v, a, b, exp, name):
    if abs(ang(v, a, b) - exp) > 0.05:
        raise AssertionError(f'angle {name} is {ang(v, a, b):.2f}, not {exp}')


def chk_eq(a, b, c, d, name):
    if abs(dist(a, b) - dist(c, d)) > 0.05:
        raise AssertionError(f'sides {name} are not equal')


def chk_par(a, b, c, d, name):
    if abs((b[0] - a[0]) * (d[1] - c[1]) - (b[1] - a[1]) * (d[0] - c[0])) > 0.5:
        raise AssertionError(f'{name} not parallel')


def f1(x):
    return '%.1f' % x


def seg(a, b, col=NAVY, sw=3, dash=None):
    return Ln(f1(a[0]), f1(a[1]), f1(b[0]), f1(b[1]), sw, col, dash)


def polygon(pts, fill=SKY, sw=3):
    return f'<polygon points="{" ".join(f1(p[0]) + "," + f1(p[1]) for p in pts)}" fill="{fill}" stroke="{NAVY}" stroke-width="{sw}" stroke-linejoin="round"/>'


def arc(v, a, b, r, label='', col=WARM, lr=0, fs=17):
    """An angle arc at v between the rays to a and b (the smaller angle); `label` sits inside the wedge at distance lr."""
    a1, a2 = math.atan2(a[1] - v[1], a[0] - v[0]), math.atan2(b[1] - v[1], b[0] - v[0])
    d = a2 - a1
    while d > math.pi:
        d -= 2 * math.pi
    while d < -math.pi:
        d += 2 * math.pi
    p1 = (v[0] + r * math.cos(a1), v[1] + r * math.sin(a1))
    p2 = (v[0] + r * math.cos(a2), v[1] + r * math.sin(a2))
    s = f'<path d="M{f1(p1[0])} {f1(p1[1])} A{r} {r} 0 0 {1 if d > 0 else 0} {f1(p2[0])} {f1(p2[1])}" fill="none" stroke="{col}" stroke-width="3"/>'
    if label:
        am, rr = a1 + d / 2, lr or r + 22
        s += T(f1(v[0] + rr * math.cos(am)), f1(v[1] + rr * math.sin(am) + fs * 0.35), label, fs, 'middle', 800, col)
    return s


def rmark(v, a, b, s=13):
    """The little square of a right angle at v between the rays to a and b."""
    u, w = (a[0] - v[0], a[1] - v[1]), (b[0] - v[0], b[1] - v[1])
    lu, lw = math.hypot(*u), math.hypot(*w)
    p1 = (v[0] + u[0] / lu * s, v[1] + u[1] / lu * s)
    p2 = (p1[0] + w[0] / lw * s, p1[1] + w[1] / lw * s)
    p3 = (v[0] + w[0] / lw * s, v[1] + w[1] / lw * s)
    return f'<path d="M{f1(p1[0])} {f1(p1[1])} L{f1(p2[0])} {f1(p2[1])} L{f1(p3[0])} {f1(p3[1])}" fill="none" stroke="{WARM}" stroke-width="2.5"/>'


def tick(a, b, n=1):
    """Equal-side tick marks across the middle of a side."""
    m = ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2)
    l = dist(a, b)
    u = ((b[0] - a[0]) / l, (b[1] - a[1]) / l)
    nn = (-u[1], u[0])
    s = ''
    for i in range(n):
        o = (i - (n - 1) / 2) * 7
        c = (m[0] + u[0] * o, m[1] + u[1] * o)
        s += Ln(f1(c[0] - nn[0] * 8), f1(c[1] - nn[1] * 8), f1(c[0] + nn[0] * 8), f1(c[1] + nn[1] * 8), 3, WARM)
    return s


def parr(a, b):
    """A parallel-lines arrow on a side."""
    m = ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2)
    l = dist(a, b)
    u = ((b[0] - a[0]) / l, (b[1] - a[1]) / l)
    nn = (-u[1], u[0])
    t = (m[0] + u[0] * 8, m[1] + u[1] * 8)
    p = (m[0] - u[0] * 6 + nn[0] * 7, m[1] - u[1] * 6 + nn[1] * 7)
    q = (m[0] - u[0] * 6 - nn[0] * 7, m[1] - u[1] * 6 - nn[1] * 7)
    return f'<polyline points="{f1(p[0])},{f1(p[1])} {f1(t[0])},{f1(t[1])} {f1(q[0])},{f1(q[1])}" fill="none" stroke="{TEAL}" stroke-width="3"/>'


def pl(p, name, dx, dy, size=19):
    return T(f1(p[0] + dx), f1(p[1] + dy), name, size, 'middle', 800, NAVY)


def shift(pts, dx, dy):
    return [(p[0] + dx, p[1] + dy) for p in pts]


def lab_angle(text, known):
    return text if known else '?'


# ---------- Q1 ----------
def cross_pts(x=68):
    """Two straight lines AB and CD crossing at O, with angle AOC = x degrees (screen points)."""
    O = (140, 96)
    return O, P(O, 95, 200), P(O, 95, 20), P(O, 95, 200 - x), P(O, 95, 380 - x)


def cross_fig(x=68, sol=False):
    O, A, B, C, D = cross_pts(x)
    chk(O, A, C, x, 'AOC'); chk(O, B, C, 180 - x, 'BOC'); chk(O, B, D, x, 'BOD'); chk(O, A, D, 180 - x, 'AOD')
    s = seg(A, B) + seg(C, D)
    if sol:
        s += arc(O, A, C, 26, f'{x}°', WARM, 50, 16) + arc(O, B, C, 40, f'{180 - x}°', TEAL, 66, 16) + arc(O, B, D, 26, f'{x}°', WARM, 50, 16) + arc(O, A, D, 40, f'{180 - x}°', TEAL, 66, 16)
    else:
        s += arc(O, A, C, 30, f'{x}°', WARM, 58)
    s += pl(A, 'A', -14, 6) + pl(B, 'B', 14, 6) + pl(C, 'C', -4, -10) + pl(D, 'D', 6, 22) + pl(O, 'O', 22, 8)
    lab = f'Two straight lines AB and CD cross at O. Angle AOC is {x} degrees.'
    if sol:
        lab = f'Two straight lines AB and CD cross at O. Angle AOC is {x} degrees, BOC is {180 - x}, BOD is {x} and AOD is {180 - x} degrees.'
    return svg(280, 190, s, lab)


def point_fig(a=95, b=130, c=70, sol=False):
    """Four angles round a point: a, b, c and the missing one."""
    Q = (140, 96)
    ds = [P(Q, 80, 0), P(Q, 80, a), P(Q, 80, a + b), P(Q, 80, a + b + c)]
    miss = 360 - a - b - c
    chk(Q, ds[0], ds[1], a, 'q1'); chk(Q, ds[1], ds[2], b, 'q2'); chk(Q, ds[2], ds[3], c, 'q3'); chk(Q, ds[3], ds[0], miss, 'q4')
    s = ''.join(seg(Q, d) for d in ds)
    s += arc(Q, ds[0], ds[1], 26, f'{a}°', WARM, 50) + arc(Q, ds[1], ds[2], 26, f'{b}°', WARM, 52) + arc(Q, ds[2], ds[3], 26, f'{c}°', WARM, 50)
    s += arc(Q, ds[3], ds[0], 26, f'{miss}°' if sol else '?', TEAL if sol else WARM, 50)
    lab = f'Four angles meet at a point and measure {a}, {b}, {c} and a question mark degrees.' if not sol else f'Four angles meet at a point and measure {a}, {b}, {c} and {miss} degrees.'
    return svg(280, 190, s, lab)


# ---------- Q2 ----------
def parallelogram_fig(A_ang=72, sol=False):
    A = (30, 150)
    B = (A[0] + 150, A[1])
    Dd = P(A, 100, A_ang)
    C = (Dd[0] + 150, Dd[1])
    chk(A, B, Dd, A_ang, 'A'); chk(B, A, C, 180 - A_ang, 'B'); chk_par(A, B, Dd, C, 'AB DC'); chk_eq(A, Dd, B, C, 'AD BC')
    s = polygon([A, B, C, Dd]) + tick(A, B) + tick(Dd, C) + tick(A, Dd, 2) + tick(B, C, 2)
    s += arc(A, B, Dd, 22, f'{A_ang}°', WARM, 42, 15)
    if sol:
        s += arc(B, A, C, 22, f'{180 - A_ang}°', TEAL, 42, 15) + arc(C, B, Dd, 22, f'{A_ang}°', TEAL, 42, 15) + arc(Dd, A, C, 22, f'{180 - A_ang}°', TEAL, 42, 15)
    s += pl(A, 'A', -12, 16) + pl(B, 'B', 12, 16) + pl(C, 'C', 14, 4) + pl(Dd, 'D', -14, 4)
    lab = f'Parallelogram ABCD with angle A {A_ang} degrees. Opposite sides are equal and parallel.'
    if sol:
        lab = f'Parallelogram ABCD: A {A_ang}, B {180 - A_ang}, C {A_ang} and D {180 - A_ang} degrees.'
    return svg(270, 176, s, lab)


def rhombus_fig(Pang=64, sol=False):
    p = (34, 150)
    q = (p[0] + 110, p[1])
    sp = P(p, 110, Pang)
    r = (sp[0] + 110, sp[1])
    chk(p, q, sp, Pang, 'QPS'); chk(q, p, r, 180 - Pang, 'PQR'); chk(p, q, r, (180 - (180 - Pang)) / 2, 'QPR')
    chk_eq(p, q, q, r, 'PQ QR'); chk_eq(p, q, p, sp, 'PQ PS')
    s = polygon([p, q, r, sp]) + seg(p, r, TEAL, 3, '7 5')
    s += tick(p, q) + tick(q, r) + tick(r, sp) + tick(sp, p)
    qpr = ang(p, q, r)
    s += arc(p, q, sp, 24)
    s += T(f1(p[0] + 3), f1(p[1] - 58), f'{Pang}°', 15, 'middle', 800, WARM)             # outside the shape, left of PS, next to the little arc
    s += arc(p, q, r, 62, f'{qpr:.0f}°' if sol else '?', TEAL if sol else WARM, 86, 15)
    s += arc(q, p, r, 24)
    s += T(f1(q[0] + 38), f1(q[1] - 12), f'{180 - Pang}°' if sol else '?', 15, 'middle', 800, TEAL if sol else WARM)      # outside the shape, right of QR
    s += pl(p, 'P', -12, 16) + pl(q, 'Q', 12, 16) + pl(r, 'R', 12, 4) + pl(sp, 'S', -14, 4)
    lab = f'Rhombus PQRS with all four sides equal and angle P {Pang} degrees. The diagonal PR is drawn dashed.'
    if sol:
        lab = f'Rhombus PQRS: angle P {Pang}, angle PQR {180 - Pang}, angle QPR {qpr:.0f} degrees.'
    return svg(270, 176, s, lab)


def trapezium_pts(Aang=110, Bang=80):
    tA = (50, 30)
    tB = (tA[0] + 130, tA[1])
    tD = P(tA, 100, 360 - Aang)
    L = (tD[1] - tB[1]) / math.sin(rad(Bang))
    BC = P(tB, L, 180 + Bang)
    C2 = (BC[0], tD[1])
    return tA, tB, C2, tD


def trapezium_fig(Aang=110, Bang=80, sol=False):
    tA, tB, C2, tD = trapezium_pts(Aang, Bang)
    chk(tA, tB, tD, Aang, 'A'); chk(tB, tA, C2, Bang, 'B'); chk_par(tA, tB, tD, C2, 'AB DC'); chk(tD, tA, C2, 180 - Aang, 'D'); chk(C2, tB, tD, 180 - Bang, 'C')
    s = polygon([tA, tB, C2, tD]) + parr(tA, tB) + parr(tD, C2)
    s += arc(tA, tB, tD, 24, f'{Aang}°', WARM, 42, 15) + arc(tB, tA, C2, 24, f'{Bang}°', WARM, 40, 15)
    s += arc(tD, tA, C2, 24, f'{180 - Aang}°' if sol else '?', TEAL if sol else WARM, 44, 15) + arc(C2, tB, tD, 24, f'{180 - Bang}°' if sol else '?', TEAL if sol else WARM, 42, 15)
    s += pl(tA, 'A', -12, 2) + pl(tB, 'B', 14, 2) + pl(C2, 'C', 14, 20) + pl(tD, 'D', -14, 20)
    lab = f'Trapezium ABCD with AB parallel to DC, angle A {Aang} degrees and angle B {Bang} degrees.'
    if sol:
        lab += f' Angle D is {180 - Aang} and angle C is {180 - Bang} degrees.'
    return svg(270, 164, s, lab)


# ---------- Q3 ----------
def tri_pts(Bang=62, DAC=38):
    L = 118
    B = (24, 160)
    A = P(B, L, Bang)
    D = (B[0] + 2 * L * math.cos(rad(Bang)), B[1])
    # C is where the ray from A, turned DAC degrees past AD, meets the line BD (found by intersection, not from the answer)
    ad = math.atan2(D[1] - A[1], D[0] - A[0])
    th = ad - rad(DAC)                                # screen y is down: turning towards C means a smaller screen angle
    dx, dy = math.cos(th), math.sin(th)
    t = (B[1] - A[1]) / dy
    C = (A[0] + t * dx, B[1])
    return A, B, C, D


def tri_fig(sol=False, Bang=62, DAC=38):
    """sol: False (question), True (the three angles BAD, ADC and ACD) or a tuple of 'ADB', 'BAD', 'ADC', 'ACD' (only those angles are written on the solution picture)."""
    A, B, C, D = tri_pts(Bang, DAC)
    adb = Bang
    bad = 180 - 2 * Bang
    adc = 180 - Bang
    acd = 180 - adc - DAC
    chk_eq(B, A, A, D, 'AB AD'); chk(B, A, C, Bang, 'B'); chk(A, D, C, DAC, 'DAC'); chk(D, A, B, adb, 'ADB'); chk(D, A, C, adc, 'ADC'); chk(C, A, B, acd, 'C'); chk(A, B, D, bad, 'BAD')
    show = ('BAD', 'ADC', 'ACD') if sol is True else (tuple(sol) if sol else ())
    s = polygon([A, B, C]) + seg(A, D) + tick(B, A) + tick(A, D)
    s += arc(B, C, A, 30, f'{Bang}°', WARM, 54, 15) + arc(A, D, C, 34, f'{DAC}°', WARM, 66, 15)
    if 'ADB' in show:
        s += arc(D, A, B, 24, f'{adb}°', TEAL, 42, 14)
    if 'BAD' in show:
        s += arc(A, B, D, 30, f'{bad}°', TEAL, 52, 14)
    if 'ADC' in show:
        s += arc(D, A, C, 36, f'{adc}°', TEAL, 58, 14)
    if 'ACD' in show:
        s += arc(C, A, B, 40, f'{acd}°', TEAL, 72, 14)
    s += pl(A, 'A', 0, -8) + pl(B, 'B', -12, 16) + pl(D, 'D', 2, 22) + pl(C, 'C', 14, 16)
    lab = f'Triangle ABC. D is a point on BC with AB equal to AD. Angle ABC is {Bang} degrees and angle DAC is {DAC} degrees. The line AD is drawn.'
    if show:
        lab += ' Checked angles: ' + ', '.join({'ADB': f'ADB {adb}', 'BAD': f'BAD {bad}', 'ADC': f'ADC {adc}', 'ACD': f'ACD {acd}'}[k] + ' degrees' for k in show) + '.'
    return svg(340, 184, s, lab)


# ---------- Q4 / A3 ----------
def para_e_pts(Babc=56):
    D = (30, 150)
    a, c = 130, 190
    A = P(D, a, Babc)
    B = (A[0] + c, A[1])
    C = (D[0] + c, D[1])
    E = (D[0] + a, D[1])
    return A, B, C, D, E


def para_e_fig(Babc=56, known=(), sol=False):
    """Parallelogram ABCD with E on DC and DA = DE; angle ABC given.  known = names of extra angles shown with their values (solution pictures)."""
    A, B, C, D, E = para_e_pts(Babc)
    adc = Babc
    dea = (180 - Babc) / 2
    aec = 180 - dea
    eab = (180 - Babc) - dea
    chk_par(A, B, D, C, 'AB DC'); chk_eq(A, D, B, C, 'AD BC'); chk_eq(D, A, D, E, 'DA DE')
    chk(B, A, C, Babc, 'ABC'); chk(D, A, C, adc, 'ADC'); chk(E, D, A, dea, 'DEA'); chk(E, A, C, aec, 'AEC'); chk(A, E, B, eab, 'EAB')
    s = polygon([A, B, C, D]) + seg(A, E) + tick(D, A) + tick(D, E)
    s += arc(B, A, C, 28, f'{Babc}°', WARM, 54, 15)
    spec = {'ADC': (D, A, C, adc, 26, 42), 'DEA': (E, D, A, dea, 24, 46), 'AEC': (E, A, C, aec, 34, 66), 'EAB': (A, E, B, eab, 30, 58)}
    for nme in known:
        v, p1, p2, val, r, lr = spec[nme]
        s += arc(v, p1, p2, r, f'{val:g}°', TEAL, lr, 14)
    s += pl(A, 'A', -2, -10) + pl(B, 'B', 4, -10) + pl(C, 'C', 14, 18) + pl(D, 'D', -14, 18) + pl(E, 'E', 2, 22)
    lab = f'Parallelogram ABCD with E a point on the side DC and DA equal to DE. Angle ABC is {Babc} degrees. The line AE is drawn.'
    if known:
        lab += ' Checked angles: ' + ', '.join(f'{k} {spec[k][3]:g} degrees' for k in known) + '.'
    return svg(330, 184, s, lab)


# ---------- Think harder / Go further ----------
def a1_fig(label='3 × B', sol=None):
    """Parallelogram ABCD in which angle A is some times angle B (label text '3 × B' or a template '{k} × B')."""
    A = (80, 130)
    B = (236, 130)
    D = P(A, 84, 135)
    C = (D[0] + 156, D[1])
    s = polygon([A, B, C, D]) + arc(A, B, D, 24, label if sol is None else f'{sol[0]}°', WARM if sol is None else TEAL, 52, 15)
    s += arc(B, A, C, 24, 'B' if sol is None else f'{sol[1]}°', WARM if sol is None else TEAL, 46, 15)
    s += pl(A, 'A', -4, 22) + pl(B, 'B', 14, 18) + pl(C, 'C', 14, 6) + pl(D, 'D', -14, 6)
    lab = 'A parallelogram ABCD in which angle A is a number of times angle B.' if sol is None else f'Parallelogram ABCD with angle A {sol[0]} degrees and angle B {sol[1]} degrees.'
    return svg(300, 156, s, lab)


def a4_fig(sol=None):
    """Square ABCD with the equilateral triangle CDE standing outside it on DC; the line AE is drawn."""
    s_ = 110
    A = (70, 200)
    B = (A[0] + s_, A[1])
    C = (B[0], A[1] - s_)
    D = (A[0], C[1])
    E = (A[0] + s_ / 2, D[1] - s_ * math.sin(rad(60)))
    chk(D, A, E, 150, 'ADE'); chk(A, D, E, 15, 'DAE'); chk_eq(D, C, D, E, 'DC DE')
    s = polygon([A, B, C, D]) + polygon([D, C, E], YEL) + seg(A, E, TEAL, 3, '7 5')
    s += arc(D, A, E, 26, '', WARM)
    s += T(f1(D[0] + 54), f1(D[1] + 22), '150°' if sol else '?', 15, 'middle', 800, TEAL if sol else WARM)
    s += arc(A, D, E, 50, '', WARM)
    s += T(f1(A[0] + 36), f1(A[1] - 52), '15°' if sol else '?', 15, 'middle', 800, TEAL if sol else WARM)
    s += pl(A, 'A', -14, 16) + pl(B, 'B', 14, 16) + pl(C, 'C', 14, 6) + pl(D, 'D', -14, 6) + pl(E, 'E', 0, -10)
    return svg(250, 240, s, 'A square ABCD with an equilateral triangle CDE standing outside it on the side DC. The line AE is drawn.' + (' Angle ADE is 150 degrees and angle DAE is 15 degrees.' if sol else ''))


def b1_pts(Aang=40):
    A = (150, 14)
    L = 190
    B = P(A, L, 270 - Aang / 2)
    C = P(A, L, 270 + Aang / 2)
    # D on AC with BD = BC: the point of line AC (other than C) at distance BC from B
    u = ((A[0] - C[0]) / L, (A[1] - C[1]) / L)
    w = (C[0] - B[0], C[1] - B[1])
    t = -2 * (u[0] * w[0] + u[1] * w[1])             # |w + t u|^2 = |w|^2 gives t = 0 or t = -2 u.w
    D = (C[0] + u[0] * t, C[1] + u[1] * t)
    return A, B, C, D


def tick_at(a, b, f, n=1):
    """Equal-side tick marks at the fraction f of the way from a to b."""
    return _tick_pt(a, b, (a[0] + (b[0] - a[0]) * f, a[1] + (b[1] - a[1]) * f), n)


def _tick_pt(a, b, m, n):
    l = dist(a, b)
    u = ((b[0] - a[0]) / l, (b[1] - a[1]) / l)
    nn = (-u[1], u[0])
    s = ''
    for i in range(n):
        o = (i - (n - 1) / 2) * 7
        c = (m[0] + u[0] * o, m[1] + u[1] * o)
        s += Ln(f1(c[0] - nn[0] * 8), f1(c[1] - nn[1] * 8), f1(c[0] + nn[0] * 8), f1(c[1] + nn[1] * 8), 3, WARM)
    return s


def b1_fig(Aang=40, sol=False):
    A, B, C, D = b1_pts(Aang)
    base = (180 - Aang) / 2
    abd = base - Aang
    chk_eq(B, C, B, D, 'BC BD'); chk(A, B, C, Aang, 'A'); chk(B, A, C, base, 'B'); chk(B, C, D, Aang, 'DBC'); chk(B, A, D, abd, 'ABD')
    s = polygon([A, B, C]) + seg(B, D) + tick_at(A, B, 0.3) + tick_at(A, C, 0.3) + tick(B, C, 2) + tick(B, D, 2)
    s += arc(A, B, C, 40, f'{Aang}°', WARM, 74, 15)
    if sol:
        s += arc(B, A, D, 56, f'{abd:g}°', TEAL, 92, 14)
    s += pl(A, 'A', 0, -8) + pl(B, 'B', -14, 14) + pl(C, 'C', 14, 14) + pl(D, 'D', 16, 0)
    return svg(300, 212, s, f'Isosceles triangle ABC with AB equal to AC and angle A {Aang} degrees. D is on AC and BD equals BC.' + (f' Angle ABD is {abd:g} degrees.' if sol else ''))


def b2_fig(sol=False):
    s_ = 110
    A = (40, 150)
    B = (A[0] + s_, A[1])
    C = (B[0], A[1] - s_)
    D = (A[0], C[1])
    E = (A[0] + s_ / 2, A[1] - s_ * math.sin(rad(60)))
    chk(A, B, E, 60, 'A'); chk_eq(A, B, A, E, 'AB AE')
    s = polygon([A, B, C, D]) + polygon([A, B, E], YEL) + seg(D, E, TEAL, 3, '7 5') + seg(C, E, TEAL, 3, '7 5')
    if sol:
        s += arc(E, D, C, 24, '150°', TEAL, 46, 14)
    s += pl(A, 'A', -14, 16) + pl(B, 'B', 14, 16) + pl(C, 'C', 14, 6) + pl(D, 'D', -14, 6) + pl(E, 'E', 0, 28)
    return svg(200, 178, s, 'A square ABCD with a point E inside it so that triangle ABE is equilateral. The lines ED and EC are drawn.' + (' Angle DEC is 150 degrees.' if sol else ''))


def iso_tens_fig(rows):
    """Solution picture for the Investigation: each isosceles triangle as three numbers (top, base, base)."""
    body = ''
    for i, (t, b) in enumerate(rows):
        y = 6 + i * 30
        body += T(16, y + 20, f'{i + 1}', 14, 'start', 800, GREY) + T(54, y + 20, f'top {t}°', 15, 'start', 800) + T(150, y + 20, f'base {b}° and {b}°', 15, 'start', 700, TEAL)
    return svg(300, 12 + 30 * len(rows), body, 'The triangles written as top angle and two base angles: ' + '; '.join(f'{t}, {b}, {b}' for t, b in rows) + '.')
