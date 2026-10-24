"""Figures and small helpers for the Level 5 holiday lessons 9 (Pattern Generalisers) and 10 (Challenge Day).

Plain inline SVG built with the shared helpers in practice/holiday/hlib.py (viewBox only, so a figure scales to a 390 px phone; the builder lifts the text to at
least 12 px).  The pattern figures are drawn from the stated rules (tables in a row with a chair on every free side, matchstick houses, dot squares, diamonds)
and the number of chairs, sticks and dots is COUNTED from the drawn shapes by the lesson checkers (never read off a formula).  No question figure prints an answer;
every solution figure is built from the CHECKED values passed in.
"""
import math, os, re, sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from hlib import svg, T, Ln, Ci, Re, NAVY, YEL, TEAL, WARM, PALE      # noqa: E402,F401

SKY = '#CDE8F7'
GREY = '#44506F'
GREEN = '#E3F4EE'
SOFT = '#FFF0C2'
RED = '#C0392B'
BLUE = '#2F6DB5'


# ================================================================= lesson 9: tables and chairs
TB, CR = 28, 6.5          # table side, chair radius


def tables_cells(n):
    """The n square tables of a long row, as grid cells (column, row)."""
    return [(i, 0) for i in range(n)]


def chairs_by_free_sides(cells):
    """One chair on every free side of a table: count the sides of each table cell that touch no other table."""
    s = set(cells)
    free = 0
    for (c, r) in cells:
        for dc, dr in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            if (c + dc, r + dr) not in s:
                free += 1
    return free


def tables_group(n, gx, ty):
    """Drawing of n tables pushed together in a row starting at x = gx; returns (svg body, width)."""
    tx = gx + 2 * CR + 3
    b = ''
    for i in range(n):
        x = tx + i * TB + TB / 2
        b += Ci(x, ty - CR - 3, CR, YEL, NAVY, 2.2) + Ci(x, ty + TB + CR + 3, CR, YEL, NAVY, 2.2)
    b += Ci(tx - CR - 3, ty + TB / 2, CR, YEL, NAVY, 2.2) + Ci(tx + n * TB + CR + 3, ty + TB / 2, CR, YEL, NAVY, 2.2)
    for i in range(n):
        b += Re(tx + i * TB, ty, TB, TB, SKY, NAVY, 2.6)
    return b, n * TB + 4 * CR + 6


def tables_fig(counts=(1, 2, 3), note=None):
    """Q1: square tables pushed together in a row, 1 table, 2 tables and 3 tables, a chair on each free side (no chair numbers are printed)."""
    body, x = '', 4
    for n in counts:
        g, w = tables_group(n, x, 20)
        body += g + T(x + w / 2, 82, f'{n} table{"s" if n > 1 else ""}', 15)
        x += w + 12
    if note:
        body += T(150, 108, note, 14, 'middle', 700, GREY)
    return svg(x - 8, 92 + (22 if note else 0), body, 'Square tables pushed together in a row, with one chair on each free side: ' + ', '.join(f'{n} table{"s" if n > 1 else ""}' for n in counts) + '.')


def drawn_chairs(counts_fig):
    """Count the chairs in a drawn figure: the circles of tables_fig (tables are rects)."""
    return len(re.findall(r'<circle', counts_fig))


def rows_fig(rows, per_row, show=3):
    """A2 solution picture: separate rows of `per_row` tables (a chair on every free side); the first `show` rows are drawn, the rest are written as a note."""
    body, y = '', 6
    for r in range(min(rows, show)):
        g, w = tables_group(per_row, 8, y + CR + 3)
        body += g
        y += TB + 2 * CR + 12
    note = f'{rows} rows of {per_row} tables' + (f' (3 drawn)' if rows > show else '')
    body += T(150, y + 12, note, 17, 'middle', 700, GREY)
    return svg(300, y + 26, body, f'{rows} separate rows of {per_row} square tables, each row with a chair on every free side.')


# ================================================================= lesson 9: matchstick houses
HU = 32                # side of the square
HR = HU * math.sqrt(3) / 2


def house_sticks(n):
    """The sticks of n matchstick houses joined in a row (square + equilateral roof), as drawn lines ((x1,y1),(x2,y2)) with y up; shared walls are one stick."""
    out = []
    for i in range(n):
        x = i * HU
        out += [((x, 0), (x + HU, 0)), ((x, HU), (x + HU, HU)), ((x, HU), (x + HU / 2, HU + HR)), ((x + HU / 2, HU + HR), (x + HU, HU))]
    for i in range(n + 1):
        out.append(((i * HU, 0), (i * HU, HU)))
    return out


def stick_svg(a, b, ox, oy, col=NAVY, dash=None, sw=4.6):
    (x1, y1), (x2, y2) = a, b
    L = math.hypot(x2 - x1, y2 - y1)
    dx, dy = (x2 - x1) / L * 2.2, (y2 - y1) / L * 2.2
    return (f'<line x1="{ox + x1 + dx:.1f}" y1="{oy - y1 - dy:.1f}" x2="{ox + x2 - dx:.1f}" y2="{oy - y2 + dy:.1f}" stroke="{col}" stroke-width="{sw}" stroke-linecap="round"'
            + (f' stroke-dasharray="{dash}"' if dash else '') + '/>')


def houses_fig(counts=(1, 2, 3), hl=None):
    """Q2: matchstick houses joined in a row.  hl = k: the sticks that the k-th house ADDS are teal and the shared wall is dashed (a solution picture)."""
    body, x = '', 8
    oy = 8 + HR + HU + 4
    for n in counts:
        sticks = house_sticks(n)
        for s in sticks:
            col, dash = NAVY, None
            if hl and n == hl:
                (x1, y1), (x2, y2) = s
                if x1 == x2 == (n - 1) * HU:          # the wall shared with the house before
                    col, dash = WARM, '3 4'
                elif min(x1, x2) >= (n - 1) * HU - 0.01:
                    col = TEAL
            body += stick_svg(s[0], s[1], x, oy, col, dash)
        body += T(x + n * HU / 2, oy + 26, f'{n} house{"s" if n > 1 else ""}', 17)
        x += n * HU + 26
    w = x - 12
    if hl:
        body += T(w / 2, oy + 50, 'teal = the sticks the new house adds', 16, 'middle', 700, GREY) + T(w / 2, oy + 72, 'dashed = the wall it shares', 16, 'middle', 700, GREY)
    return svg(w, oy + (80 if hl else 34), body, 'Matchstick houses joined in a row: ' + ', '.join(f'{n} house{"s" if n > 1 else ""}' for n in counts) + '. Each house is a square with a triangle roof.')


def drawn_sticks(fig):
    return len(re.findall(r'<line', fig))


# ================================================================= lesson 9: dot squares (odd numbers), diamonds, beads
def dot_squares_fig(upto=4, hl=True):
    """Solution picture: the squares of dots 1 by 1 to upto by upto; each new L-shaped border is teal."""
    d, body, x = 15, '', 8
    for k in range(1, upto + 1):
        for r in range(k):
            for c in range(k):
                new = hl and (r == k - 1 or c == k - 1)
                body += Ci(x + c * d + 6, 14 + r * d, 5.2, TEAL if new else YEL, NAVY, 1.6)
        body += T(x + (k - 1) * d / 2 + 6, 14 + upto * d + 6, f'{k} × {k}', 14)
        x += k * d + 22
    return svg(x - 10, 14 + upto * d + 14, body, 'Squares of dots, 1 by 1, 2 by 2, 3 by 3 and 4 by 4. Each new square adds an L-shaped border of dots (shown in teal).')


def diamond_fig(figs=(1, 2, 3), sol=None):
    """B1: diamond dot patterns.  Figure f has rows of 1, 3, ..., 2f - 1, ..., 3, 1 dots."""
    d, body, x = 12.5, '', 6
    maxf = max(figs)
    wmax = (2 * maxf - 1) * d
    for f in figs:
        rows = list(range(1, 2 * f, 2)) + list(range(2 * f - 3, 0, -2))
        cx = x + wmax / 2
        top = 12 + (maxf - f) * d
        for r, n in enumerate(rows):
            for i in range(n):
                body += Ci(round(cx + (i - (n - 1) / 2) * d, 1), top + r * d, 4.2, YEL, NAVY, 1.6)
        body += T(cx, 12 + (2 * maxf - 1) * d + 18, f'Figure {f}', 14)
        x += wmax + 22
    return svg(x - 14, 12 + (2 * maxf - 1) * d + 28, body, 'Diamond dot patterns: ' + ', '.join(f'figure {f}' for f in figs) + '. Each figure is a diamond of dots with rows that grow and then shrink.')


def drawn_dots(fig):
    return len(re.findall(r'<circle', fig))


BEADS = [('R', RED, '#FFFFFF'), ('R', RED, '#FFFFFF'), ('B', BLUE, '#FFFFFF'), ('Y', YEL, NAVY), ('Y', YEL, NAVY), ('Y', YEL, NAVY)]


def beads_fig(groups=2):
    """A1: the first two groups of beads: red, red, blue, yellow, yellow, yellow, then the pattern goes on (the letters are R, B, Y so colour is not the only clue)."""
    r, sp, x0, body = 10.5, 24, 14, ''
    for k in range(6 * groups):
        c = BEADS[k % 6]
        x = x0 + k * sp
        body += Ci(x, 22, r, c[1], NAVY, 2) + T(x, 27.5, c[0], 14, 'middle', 800, c[2])
    body += T(x0 + 6 * groups * sp - 6, 28, '…', 20, 'start', 800)
    return svg(x0 + 6 * groups * sp + 22, 46, body, 'A string of beads: red, red, blue, yellow, yellow, yellow, then the same again, and so on. R is red, B is blue and Y is yellow.')


def bead_at(k):
    """The colour of the k-th bead (1, 2, 3 ...), found by walking along the string."""
    return {'R': 'red', 'B': 'blue', 'Y': 'yellow'}[BEADS[(k - 1) % 6][0]]


# ================================================================= lesson 10: bar models
def seg_row(x0, y, u, h, segs, off=0.0):
    """One bar: segs = [(units, text, fill, dashed)], starting `off` units from x0.  Returns the svg body."""
    b, x = '', x0 + off * u
    for units, text, fill, dashed in segs:
        b += Re(round(x, 1), y, round(units * u, 1), h, fill, NAVY, 2.4, 0, '5 4' if dashed else None)
        if text:
            b += T(round(x + units * u / 2, 1), y + h / 2 + 5, text, 13.5, 'middle', 800)
        x += units * u
    return b


def brace_top(x1, x2, y, text, size=15):
    return f'<path d="M{x1} {y} V{y - 8} H{x2} V{y}" fill="none" stroke="{NAVY}" stroke-width="2.4"/>' + T((x1 + x2) / 2, y - 14, text, size, 'middle', 800)


def backwards_fig(sol=None, lunch=12, left=15):
    """Q2: Ali spent 1/3 on a book, $x on lunch, half of the rest on a gift, $y left.  Not to scale.
    sol = (start, book, rest, lunch, before_gift, gift) writes the checked dollars on the bars."""
    u, x0, h = 40, 14, 30
    body = brace_top(x0, x0 + 6 * u, 24, '? at the start' if not sol else f'${sol[0]} at the start')
    body += T(x0, 52, 'Start', 14, 'start', 700, GREY)
    body += seg_row(x0, 58, u, h, [(2, 'book 1/3' if not sol else f'book ${sol[1]}', YEL, False), (4, 'the rest' if not sol else f'the rest ${sol[2]}', SKY, False)])
    body += T(x0 + 2 * u, 106, 'After the book', 14, 'start', 700, GREY)
    body += seg_row(x0, 112, u, h, [(1.2, f'${lunch}', SOFT, False), (2.8, 'what was left' if not sol else f'left ${sol[4]}', SKY, False)], off=2)
    body += T(x0 + 3.2 * u, 160, 'After lunch', 14, 'start', 700, GREY)
    body += seg_row(x0, 166, u, h, [(1.4, 'gift' if not sol else f'gift ${sol[5]}', YEL, False), (1.4, f'${left} left', GREEN, False)], off=3.2)
    return svg(x0 + 6 * u + 14, 206, body, 'Not to scale. A bar for all of Ali\'s money, cut into a book part (one third) and the rest. The rest is cut into the lunch money and what was left. '
               'What was left is cut into two halves: the gift and the money left at the end.')


def two_bars_fig(total, extra, sol=None):
    """Q3: Mei is 4 equal units; Ravi is 3 of the same units and a shaded extra part; a brace on the right marks the total.  sol = unit value."""
    u, x0, h = 44, 50, 32
    body = T(x0 - 6, 38, 'Mei', 15, 'end', 800) + T(x0 - 6, 82, 'Ravi', 15, 'end', 800)
    unit_t = '' if not sol else f'${sol}'
    body += seg_row(x0, 20, u, h, [(1, unit_t, SKY, False)] * 4)
    body += seg_row(x0, 64, u, h, [(1, unit_t, SKY, False)] * 3 + [(1, f'${extra}', YEL, False)])
    xb = x0 + 4 * u + 10
    body += f'<path d="M{xb} 20 H{xb + 8} V{64 + h} H{xb}" fill="none" stroke="{NAVY}" stroke-width="2.4"/>' + T(xb + 14, 62, f'${total}', 15, 'start', 800)
    return svg(x0 + 4 * u + 64, 108, body, 'Not to scale. Two bars. Mei has 4 equal units. Ravi has 3 of the same units plus a shaded extra part of $%d. A brace on the right marks $%d altogether.' % (extra, total))


def siti_fig(left, sol=None):
    """A1 (Think harder): Siti spent 2/5 of her money, then 1/3 of what was left, and had `left` dollars at the end.  sol = value of one fifth."""
    u, x0, h = 52, 14, 30
    body = brace_top(x0, x0 + 5 * u, 24, '? at the start' if not sol else f'${5 * sol} at the start')
    body += seg_row(x0, 34, u, h, [(2, 'spent 2/5' if not sol else f'spent ${2 * sol}', YEL, False), (3, 'the rest' if not sol else f'the rest ${3 * sol}', SKY, False)])
    body += T(x0 + 2 * u, 86, 'The rest is cut in three', 14, 'start', 700, GREY)
    body += seg_row(x0, 92, u, h, [(1, '1/3' if not sol else f'${sol}', SOFT, False), (2, f'${left} left', GREEN, False)], off=2)
    return svg(x0 + 5 * u + 14, 134, body, 'Not to scale. Siti\'s money bar: two fifths are spent. The rest is cut in three equal parts: one third of it is spent next and the other two thirds, $%d, are left.' % left)


# ================================================================= lesson 10: logic clue card, grid of squares, staircase
def clue_card():
    """Q1: the four clues once, as a card (shown above each of the four questions)."""
    lines = [('Dishes:', ['chicken rice, laksa, satay, roti prata.']),
             ('Clue 1.', ['Ali did not order laksa or satay.']),
             ('Clue 2.', ['The roti prata was ordered by a girl.', 'Mei and Siti are girls.', 'Ali and Ben are boys.']),
             ('Clue 3.', ['Ben did not order satay.']),
             ('Clue 4.', ['Mei did not order roti prata.'])]
    y, body = 28, ''
    for h, ls in lines:
        body += T(14, y, h, 14, 'start', 800, TEAL)
        for l in ls:
            body += T(76, y, l, 14, 'start', 700)
            y += 21
        y += 6
    return svg(340, y, Re(3, 3, 334, y - 10, PALE, NAVY, 2.2, 10) + body, 'The hawker centre puzzle. Ali, Ben, Mei and Siti each ordered a different dish: chicken rice, laksa, satay or roti prata. '
               'Clue 1: Ali did not order laksa or satay. Clue 2: the roti prata was ordered by a girl; Mei and Siti are girls, Ali and Ben are boys. '
               'Clue 3: Ben did not order satay. Clue 4: Mei did not order roti prata.')


def grid_fig(rows=3, cols=4, caption=True):
    """Q4: a rectangle made of rows x cols small squares, drawn to scale."""
    s = min(44, 250 // cols)
    x0 = 20
    body = ''
    for r in range(rows):
        for c in range(cols):
            body += Re(x0 + c * s, 6 + r * s, s, s, SKY, NAVY, 2.6)
    if caption:
        body += T(x0 + cols * s / 2, 6 + rows * s + 24, f'{rows} rows of {cols} small squares', 15)
    return svg(x0 * 2 + cols * s, 6 + rows * s + (34 if caption else 10), body, f'A rectangle made of {rows} rows of {cols} small squares.')


def squares_in_grid_fig(rows=3, cols=4, size=2, at=(0, 0)):
    """Solution picture: the grid with one square of the given size marked (so the child sees what a '2 by 2 square' is)."""
    s = min(44, 250 // cols)
    x0 = 20
    body = ''
    for r in range(rows):
        for c in range(cols):
            body += Re(x0 + c * s, 6 + r * s, s, s, SKY, NAVY, 2.0)
    body += Re(x0 + at[0] * s, 6 + at[1] * s, size * s, size * s, 'none', WARM, 4.2)
    body += T(x0 + cols * s / 2, 6 + rows * s + 24, f'one {size} by {size} square is outlined', 14, 'middle', 700, WARM)
    return svg(x0 * 2 + cols * s, 6 + rows * s + 34, body, f'The grid of {rows} rows of {cols} small squares with one {size} by {size} square outlined.')


def stairs_fig(n=4):
    """Inv: a staircase with n steps (the figure Ali climbs)."""
    w, h, x0 = 56, 24, 14
    body = ''
    for k in range(n):
        body += Re(x0 + k * w, 8 + (n - 1 - k) * h, w, h * (k + 1), SKY, NAVY, 2.4)
    body += Ci(x0 - 4, 8 + n * h - 14, 9, YEL, NAVY, 2.2) + T(x0 - 4, 8 + n * h - 9, 'A', 13, 'middle', 800)
    body += T(x0 + n * w / 2, 8 + n * h + 22, f'a staircase with {n} steps', 15)
    return svg(x0 * 2 + n * w, 8 + n * h + 34, body, f'A staircase with {n} steps. Ali stands at the bottom.')


def steps_solution_fig(n=4):
    """Inv (a) solution: the five ways to climb 4 steps, as rows of hops (1 or 2 steps)."""
    def ways(k):
        if k == 0:
            return [[]]
        out = []
        for s in (1, 2):
            if k - s >= 0:
                out += [[s] + w for w in ways(k - s)]
        return out
    ws = ways(n)
    body, y = '', 6
    for w in ws:
        x = 14
        for s in w:
            body += Re(x, y, s * 34 - 4, 24, YEL if s == 1 else SKY, NAVY, 2.2) + T(x + s * 17 - 2, y + 18, str(s), 15, 'middle', 800)
            x += s * 34
        y += 32
    return svg(n * 34 + 28, y + 2, body, f'The {len(ws)} ways to climb {n} steps, taking 1 or 2 steps at a time: ' + '; '.join('+'.join(map(str, w)) for w in ws) + '.')
