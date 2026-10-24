"""Figures and small helpers for the Level 5 holiday lessons 5 (Volume Vault) and 6 (Rate Racers).

Plain inline SVG built with the shared helpers in practice/holiday/hlib.py (viewBox only, so a figure scales to a 390 px phone; the builder lifts the text to at least
12 px).  The solids are drawn in the same oblique way as the printed workbook (length to the right, height up, breadth going back at 30 degrees, half size), but at a size
that is readable on a phone.  No question figure prints an answer; every solution figure is built from the CHECKED values passed in.
"""
import math, os, sys
from fractions import Fraction

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from hlib import svg, T, Ln, Ci, Re, NAVY, YEL, TEAL, WARM, PALE      # noqa: E402,F401

SKY = '#CDE8F7'
WSIDE, WTOP = '#BCD6EE', '#EEF5FC'
GREY = '#44506F'
F_FRONT, F_TOP, F_SIDE = '#FFD966', '#FFE9A8', '#E8B923'          # painted (yellow) cubes
M_FRONT, M_TOP, M_SIDE = '#C9CED8', '#E3E6EC', '#AEB4C2'          # metal cubes and blocks


# ---------------------------------------------------------------- oblique solids
def OB(x0, y0, s):
    return lambda x, y, z: (round(x0 + x * s + z * s * 0.433, 1), round(y0 - y * s - z * s * 0.25, 1))


def _pts(P, lst):
    return ' '.join('%s,%s' % P(*q) for q in lst)


def _ln(P, a, b, sw=1.5, dash=None, c=NAVY):
    (x1, y1), (x2, y2) = P(*a), P(*b)
    return Ln(x1, y1, x2, y2, sw, c, dash)


def box(P, L, B, H, grid=False, fill=None, water=None, labels=None, lsize=15, wlabel=None):
    """A box L x B x H (length, breadth, height).  grid: unit-cube lines.  fill: (front, top, right) colours.  water: depth of water (an open glass tank).
    labels: (length, height, breadth) texts.  wlabel: text for the water-depth arrow."""
    s = ''
    if water is not None:
        s += _ln(P, (0, 0, B), (L, 0, B), 1.5, '5 4') + _ln(P, (0, 0, B), (0, H, B), 1.5, '5 4') + _ln(P, (0, 0, 0), (0, 0, B), 1.5, '5 4')
        if water > 0:
            w = water
            s += f'<polygon points="{_pts(P, [(0, w, 0), (L, w, 0), (L, w, B), (0, w, B)])}" fill="{WTOP}" stroke="{NAVY}" stroke-width="1"/>'
            s += f'<polygon points="{_pts(P, [(0, 0, 0), (L, 0, 0), (L, w, 0), (0, w, 0)])}" fill="{SKY}"/>'
            s += f'<polygon points="{_pts(P, [(L, 0, 0), (L, 0, B), (L, w, B), (L, w, 0)])}" fill="{WSIDE}"/>'
    elif fill:
        s += f'<polygon points="{_pts(P, [(0, 0, 0), (L, 0, 0), (L, H, 0), (0, H, 0)])}" fill="{fill[0]}"/>'
        s += f'<polygon points="{_pts(P, [(0, H, 0), (L, H, 0), (L, H, B), (0, H, B)])}" fill="{fill[1]}"/>'
        s += f'<polygon points="{_pts(P, [(L, 0, 0), (L, 0, B), (L, H, B), (L, H, 0)])}" fill="{fill[2]}"/>'
    if grid:
        for i in range(1, L):
            s += _ln(P, (i, 0, 0), (i, H, 0)) + _ln(P, (i, H, 0), (i, H, B))
        for j in range(1, H):
            s += _ln(P, (0, j, 0), (L, j, 0)) + _ln(P, (L, j, 0), (L, j, B))
        for k in range(1, B):
            s += _ln(P, (0, H, k), (L, H, k)) + _ln(P, (L, 0, k), (L, H, k))
    e = f'fill="none" stroke="{NAVY}" stroke-width="2.5" stroke-linejoin="round"'
    s += f'<polygon points="{_pts(P, [(0, 0, 0), (L, 0, 0), (L, H, 0), (0, H, 0)])}" {e}/>'
    s += f'<polygon points="{_pts(P, [(0, H, 0), (L, H, 0), (L, H, B), (0, H, B)])}" {e}/>'
    s += f'<polygon points="{_pts(P, [(L, 0, 0), (L, 0, B), (L, H, B), (L, H, 0)])}" {e}/>'
    if labels:
        a, b, c = labels
        if a:
            x, y = P(L / 2, 0, 0); s += T(x, y + lsize + 6, a, lsize)
        if b:
            x, y = P(0, H / 2, 0); s += T(x - 8, y + 6, b, lsize, 'end')
        if c:
            x, y = P(L, 0, B / 2); s += T(x + 10, y + lsize + 2, c, lsize, 'start')
    if water is not None and water > 0 and wlabel:
        x1, y1 = P(L * 0.12, 0, 0)
        _, y2 = P(L * 0.12, water, 0)
        s += f'<line x1="{x1}" y1="{y1 - 3}" x2="{x1}" y2="{y2 + 3}" stroke="{TEAL}" stroke-width="2.5"/>'
        s += f'<polygon points="{x1 - 6},{y2 + 12} {x1 + 6},{y2 + 12} {x1},{y2 + 2}" fill="{TEAL}"/><polygon points="{x1 - 6},{y1 - 12} {x1 + 6},{y1 - 12} {x1},{y1 - 2}" fill="{TEAL}"/>'
        s += T(x1 + 10, (y1 + y2) / 2 + 6, wlabel, lsize, 'start', 700, TEAL)
    return s


def _size(L, B, H, s, left=0, right=0, below=0, top=0, ox=14):
    """(width, height, origin x, origin y) of a viewBox that holds a box drawn with scale s."""
    w = ox + left + L * s + B * s * 0.433 + right + 10
    h = top + H * s + B * s * 0.25 + below + 14
    return round(w), round(h), ox + left, round(top + H * s + B * s * 0.25 + 6)


# ---------------------------------------------------------------- lesson 5 figures
def cuboid_grid(L, B, H, s=34, label=None):
    """A solid cuboid made of 1-cm cubes (grid lines), no sizes written on it."""
    w, h, x0, y0 = _size(L, B, H, s)
    lab = label or f'A solid cuboid built from 1-centimetre cubes: {L} cubes long, {B} cubes deep and {H} cubes high'
    return svg(w, h, box(OB(x0, y0, s), L, B, H, grid=True, fill=(F_FRONT, F_TOP, F_SIDE)), lab)


def plain_box(L, B, H, s, labels, label):
    w, h, x0, y0 = _size(L, B, H, s, left=48, right=48, below=24)
    return svg(w, h, box(OB(x0, y0, s), L, B, H, fill=('#F4F8FC', '#FFFFFF', '#DCE6F2'), labels=labels), label)


def tank_q3():
    s = 4.2
    w, h, x0, y0 = _size(50, 30, 40, s, left=52, right=52, below=24)
    return svg(w, h, box(OB(x0, y0, s), 50, 30, 40, water=18, labels=('50 cm', '40 cm', '30 cm'), wlabel='18 cm'),
               'A glass tank 50 cm long, 30 cm wide and 40 cm high. The water in it is 18 cm deep.')


def tank_q4():
    """Tank 40 x 25 x 30 with water 15 cm deep, and below it the 5 metal cubes with 10 cm edges, all at the same scale."""
    s = 3.6
    w0, h0, x0, y0 = _size(40, 25, 30, s, left=52, right=52, below=24)
    body = box(OB(x0, y0, s), 40, 25, 30, water=15, labels=('40 cm', '30 cm', '25 cm'), wlabel='15 cm')
    cy = h0 + 58                               # baseline of the cubes
    cs = 10 * s
    step = cs + 10 * s * 0.433 + 10
    for k in range(5):
        body += box(OB(10 + k * step, cy, s), 10, 10, 10, fill=(M_FRONT, M_TOP, M_SIDE))
    body += T(10 + 2 * step + cs / 2, cy + 22, '5 metal cubes, each edge 10 cm', 15)
    W = max(w0, round(10 + 5 * step + 8))
    return svg(W, cy + 30, body, 'A tank with a base 40 cm by 25 cm and water 15 cm deep, and below it 5 metal cubes with edges of 10 cm, drawn to the same scale as the tank.')


def painted_cube_4():
    return cuboid_grid(4, 4, 4, 30, 'A cube made of 64 small cubes, 4 along each edge. The outside is painted yellow.')


def two_containers():
    """Container A (30 x 20 x 24, full of water) above tank B (40 x 30 x 25, empty), same scale."""
    s = 3.4
    wa, ha, xa, ya = _size(30, 20, 24, s, left=40, right=48, below=24)
    wb, hb, xb, yb = _size(40, 30, 25, s, left=40, right=48, below=24)
    gap = 26
    body = T(xa, 18, 'Container A (full of water)', 15, 'start', 800)
    body += box(OB(xa, 28 + ya, s), 30, 20, 24, water=24, labels=('30 cm', '24 cm', '20 cm'))
    oy = 28 + ha + gap
    body += T(xb, oy + 14, 'Tank B (empty)', 15, 'start', 800)
    body += box(OB(xb, oy + 24 + yb, s), 40, 30, 25, water=0, labels=('40 cm', '25 cm', '30 cm'))
    return svg(max(wa, wb), oy + 24 + hb, body, 'Container A, 30 cm by 20 cm by 24 cm, full of water, above tank B, 40 cm by 30 cm by 25 cm, which is empty. Both are drawn to the same scale.')


def tank_block():
    """Tank 30 x 20 with water 10 cm deep; a block 10 x 10 x 15 stands upright on the bottom."""
    s = 5
    w, h, x0, y0 = _size(30, 20, 25, s, left=6, right=50, below=24, top=26)
    P = OB(x0, y0, s)
    body = T(x0, 20, 'Block: 10 cm by 10 cm, 15 cm high', 15, 'start', 800)
    body += box(P, 30, 20, 25, water=10, labels=('30 cm', '', '20 cm'), wlabel='10 cm')
    body += box(lambda x, y, z: P(x + 17, y, z + 4), 10, 10, 15, fill=(M_FRONT, M_TOP, M_SIDE))
    return svg(w, h, body, 'A tank with a base 30 cm by 20 cm and water 10 cm deep. A block 10 cm by 10 cm by 15 cm stands upright on the bottom of the tank.')


def kinds_bar(parts):
    """Solution picture for the painted cube: a bar of the 64 small cubes cut by the number of painted faces. parts = [(label, count)]"""
    tot = sum(c for _, c in parts)
    x0, w = 10, 340
    body = T(x0 + w / 2, 18, f'all {tot} small cubes', 15, 'middle', 800)
    cols = ['#F2B7A0', '#FFD966', '#BFE3C8', SKY]
    x = x0
    for k, (lab, c) in enumerate(parts):
        ww = w * c / tot
        body += Re(round(x, 1), 28, round(ww, 1), 36, cols[k % 4], NAVY, 2.4) + T(round(x + ww / 2, 1), 52, str(c), 17, 'middle', 800)
        body += T(round(x + ww / 2, 1), 84 + (k % 2) * 18, lab, 13, 'middle', 700, GREY)
        x += ww
    return svg(360, 124, body, 'A bar of the small cubes cut into four parts by the number of painted faces: ' + ', '.join(f'{lab}: {c}' for lab, c in parts) + '.')


# ---------------------------------------------------------------- lesson 6 figures
def shops():
    """Three shop price boards, one under the other."""
    def board(y, name, l1, l2, l3, fill, h):
        b = Re(4, y, 352, h, fill, NAVY, 2.5, 10) + Re(4, y, 92, h, NAVY, NAVY, 2.5, 10) + Re(70, y, 26, h, NAVY, NAVY, 0)
        b += T(50, y + h / 2 + 6, name, 17, 'middle', 800, '#FFFFFF')
        b += T(108, y + (22 if l3 else h / 2 + 6), l1, 16, 'start', 700) + T(348, y + (22 if l3 else h / 2 + 7), l2, 22, 'end', 800)
        if l3:
            b += T(108, y + h - 12, l3, 15, 'start', 800, WARM)
        return b
    body = board(4, 'SHOP A', 'Pack of 6 cans', '$4.20', '', '#FFFFFF', 48) + board(60, 'SHOP B', 'Pack of 4 cans', '$2.92', '', '#FFFFFF', 48) \
        + board(116, 'SHOP C', 'Pack of 10 cans', '$7.80', '+ 2 cans FREE!', '#FFF0C2', 62)
    return svg(360, 186, body, 'Shop A: a pack of 6 cans for $4.20. Shop B: a pack of 4 cans for $2.92. Shop C: a pack of 10 cans for $7.80, and 2 more cans free.')


def rate_table(fill=None):
    """The machine's rate table: Minutes 1, 3, 5, ?, 12 and Bottles ?, 48, ?, 160, ?.  fill = the five (minutes, bottles) pairs to show instead of the question marks."""
    orig = [('1', '?'), ('3', '48'), ('5', '?'), ('?', '160'), ('12', '?')]
    cols = [(str(m), str(b)) for m, b in fill] if fill else orig
    x0, lw, cw, rh = 4, 76, 56, 38
    body = ''
    for r, name in enumerate(('Minutes', 'Bottles')):
        y = 4 + r * rh
        body += Re(x0, y, lw, rh, '#E4E8F0', NAVY, 2.2) + T(x0 + lw / 2, y + 25, name, 15, 'middle', 800)
        for k, c in enumerate(cols):
            v = c[r]
            q = v == '?'
            new = bool(fill) and orig[k][r] == '?'
            body += Re(x0 + lw + k * cw, y, cw, rh, PALE if q else ('#E3F4EE' if new else '#FFFFFF'), NAVY, 2.2, 0, '5 4' if q else None)
            body += T(x0 + lw + k * cw + cw / 2, y + 26, v, 18, 'middle', 800, TEAL if new else NAVY)
    lab = ('A rate table with two rows. Minutes: 1, 3, 5, a missing number, 12. Bottles: a missing number, 48, a missing number, 160, a missing number.' if not fill
           else 'The completed rate table. Minutes: ' + ', '.join(c[0] for c in cols) + '. Bottles: ' + ', '.join(c[1] for c in cols) + '.')
    return svg(x0 * 2 + lw + 5 * cw, 2 * rh + 8, body, lab)


def tank_taps():
    """The 240 litre tank with tap A (12 litres a minute), tap B (18 litres a minute) and a crack (6 litres a minute out)."""
    body = T(10, 20, 'Tap A: 12 ℓ a min', 15, 'start', 800) + T(350, 20, 'Tap B: 18 ℓ a min', 15, 'end', 800)
    body += f'<path d="M10 36 H112 V84" fill="none" stroke="{NAVY}" stroke-width="9" stroke-linecap="round"/><path d="M350 36 H248 V84" fill="none" stroke="{NAVY}" stroke-width="9" stroke-linecap="round"/>'
    body += Re(90, 96, 180, 112, '#FFFFFF', NAVY, 3) + Re(92, 140, 176, 66, SKY, SKY, 0)
    body += Ln(112, 92, 112, 132, 5, '#7FB2DE', '8 5') + Ln(248, 92, 248, 132, 5, '#7FB2DE', '8 5')
    body += T(180, 176, 'holds 240 ℓ', 18, 'middle', 800)
    body += Ci(262, 212, 4, '#7FB2DE', '#7FB2DE', 1) + Ci(268, 226, 4, '#7FB2DE', '#7FB2DE', 1) + T(350, 252, 'crack: 6 ℓ a min out', 15, 'end', 800, WARM)
    return svg(360, 262, body, 'A tank that holds 240 litres, filled by tap A at 12 litres a minute and tap B at 18 litres a minute. A crack lets out 6 litres a minute.')


def printer_bar(solution=None):
    """The 900-page job as one bar of 6 equal parts: the first part is P alone (5 minutes) and the other five parts are P and Q together.
    solution = (alone_minutes, alone_pages, together_minutes, together_pages, total_minutes, pages) adds the checked numbers."""
    x0, w = 14, 332
    u = w / 6
    body = f'<path d="M{x0} 52 V44 H{x0 + w} V52" fill="none" stroke="{NAVY}" stroke-width="2.4"/>' + T(x0 + w / 2, 36, (f'{solution[5]} pages' if solution else '900 pages'), 15, 'middle', 800)
    body += Re(x0, 56, u, 44, YEL, NAVY, 2.4) + T(x0 + u / 2, 75, 'P', 14, 'middle', 800) + T(x0 + u / 2, 92, 'alone', 13, 'middle', 800)
    body += Re(round(x0 + u, 1), 56, round(5 * u, 1), 44, SKY, NAVY, 2.4) + T(x0 + 3.5 * u, 83, 'P and Q together', 14, 'middle', 800)
    body += f'<path d="M{x0} 108 V116 H{x0 + w} V108" fill="none" stroke="{NAVY}" stroke-width="2.4"/>' + T(x0 + w / 2, 138, ('whole job: %d minutes' % solution[4]) if solution else '? minutes in all, from the start', 15, 'middle', 800, TEAL)
    if solution:
        body += T(x0, 158, f'{solution[0]} min', 13, 'start', 700, GREY) + T(x0, 174, f'{solution[1]} pages', 13, 'start', 700, GREY)
        body += T(x0 + 3.5 * u, 158, f'{solution[2]} min', 13, 'middle', 700, GREY) + T(x0 + 3.5 * u, 174, f'{solution[3]} pages', 13, 'middle', 700, GREY)
        return svg(360, 184, body, 'The bar with the checked numbers: P alone for %d minutes printed %d pages; P and Q together for %d minutes printed %d pages; %d minutes in all.' % (solution[0], solution[1], solution[2], solution[3], solution[4]))
    return svg(360, 148, body, 'A bar for the whole 900-page job in 6 equal parts. The first part is P printing alone for 5 minutes. The other five parts are P and Q printing together. A brace under the bar asks for the minutes in all.')


def _sign_body():
    body = Re(4, 4, 352, 118, '#FFFFFF', NAVY, 3, 14) + Ci(48, 63, 30, TEAL, TEAL, 1) + T(48, 77, 'P', 38, 'middle', 800, '#FFFFFF')
    body += T(94, 36, 'CITY CAR PARK', 18, 'start', 800, TEAL) + T(94, 66, 'First hour:  $1.20', 18, 'start', 800)
    body += T(94, 92, 'After that:  60¢ for every half hour', 15, 'start', 700) + T(94, 112, 'or part of a half hour', 15, 'start', 700)
    return body


def _timeline_body(count=False):
    marks = ['9.40', '10.40', '11.10', '11.40', '12.10', '12.40', '1.10', '1.40']
    ys = [28, 88, 118, 148, 178, 208, 238, 268]
    x0, w = 84, 130
    body = T(x0, 16, 'Ali parks at 9.40 a.m.', 15, 'start', 800, TEAL)
    body += Re(x0, ys[0], w, ys[1] - ys[0], YEL, NAVY, 2.5) + T(x0 + w / 2, (ys[0] + ys[1]) / 2 + 5, 'first hour', 15, 'middle', 800)
    for i in range(1, 7):
        body += Re(x0, ys[i], w, ys[i + 1] - ys[i], '#E3F4EE' if count else '#FFFFFF', NAVY, 2.5)
        body += T(x0 + w / 2 + (8 if count else 0), ys[i] + 20, 'half hour', 14, 'middle', 700, GREY)
        if count:
            body += T(x0 + 18, ys[i] + 21, str(i), 15, 'middle', 800, TEAL)
    for m, y in zip(marks, ys):
        body += Ln(x0 - 8, y, x0, y, 2.5) + T(x0 - 14, y + 5, m, 15, 'end', 700)
    ye = ys[6] + (5 / 30) * (ys[7] - ys[6])                 # 1.15 is 5 minutes after 1.10
    body += Ln(x0 + w, ye, x0 + w + 36, ye, 3, TEAL) + T(x0 + w + 42, ye + 5, 'Ali leaves', 15, 'start', 800, TEAL) + T(x0 + w + 42, ye + 22, '1.15 p.m.', 15, 'start', 800, TEAL)
    return body


def car_park(count=False):
    """One figure: the car park sign, and under it Ali's stay as a time line going down: the first hour (9.40 to 10.40) and then six half hours up to 1.40,
    with 1.15 p.m. marked as the time he leaves.  count=True numbers the six half hours (solution picture)."""
    body = _sign_body() + f'<g transform="translate(10,138)">{_timeline_body(count)}</g>'
    return svg(360, 138 + 290, body, 'Car park sign: first hour $1.20, then 60 cents for every half hour or part of a half hour. Below it a time line going down from 9.40 a.m.: the first hour, '
               'then six half hours up to 1.40 p.m.' + (' The six half hours are numbered 1 to 6.' if count else '') + ' Ali leaves at 1.15 p.m.')


# ---------------------------------------------------------------- typed answers with decimals
def dec_text(v):
    """Exact decimal text of a Fraction with a terminating decimal: 72/5 -> '14.4'."""
    v = Fraction(v)
    n, d = v.numerator, v.denominator
    k = 0
    while d != 1:
        n *= 10; k += 1
        g = math.gcd(n, d)
        n //= g; d //= g
        assert k <= 6, v
    s = str(n)
    if k:
        s = s.rjust(k + 1, '0')
        s = s[:-k] + '.' + s[-k:]
    return s


def dec_accepts(v, units=(), money=False, places=(), also=()):
    """Accepted ways to type a decimal answer: the exact decimal and padded forms ('9.6', '9.60'), each also with a unit word after it (and '$' in front for money)."""
    v = Fraction(v)
    forms = {dec_text(v)}
    for p in places:
        forms.add(('%.' + str(p) + 'f') % float(v))
    out = set(forms)
    if money:
        out |= {'$' + f for f in forms} | {f'{f} dollars' for f in forms} | {f'${f} dollars' for f in forms}
    for u in units:
        for f in forms:
            out.add(f'{f} {u}'); out.add(f'{f}{u}')
    out.update(also)
    return sorted(out)
