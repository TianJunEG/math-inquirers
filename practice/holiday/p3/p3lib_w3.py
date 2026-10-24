"""Shared helpers for the Level 3 (P3) holiday online practice, WEEK 3 (lessons 5 and 6): the workbook's own figures (drawn by the workbook generators, via
figs_p3_w3.js), phone-sized redrawings of the fraction wall, the five shapes and the partner cards, fraction helpers for the typed answers, and small brute-force
helpers used by the INDEPENDENT checkers.  Imported by p3/05/lesson.py and p3/06/lesson.py (after `from hlib import *`)."""
import itertools, json, os, re, subprocess
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
_figs3 = None


def figs3():
    """{name: svg} of the Level 3 week 3 figures drawn by the workbook's own functions (node, figs_p3_w3.js: l5.js counters, l6.js wall/shapes/cards, figs_l3.js empty bars)."""
    global _figs3
    if _figs3 is None:
        _figs3 = json.loads(subprocess.check_output(['node', os.path.join(HERE, 'figs_p3_w3.js')], text=True))
    return _figs3


def _h():
    import sys
    sys.path.insert(0, os.path.join(HERE, '..'))
    import hlib
    return hlib


# ---------------------------------------------------------------- division by trying (no // or % in the checkers)
def groups_of(n, d):
    """(full groups, left over) of n shared into groups of d, found by counting up in d."""
    q = 0
    while (q + 1) * d <= n:
        q += 1
    return q, n - q * d


def groups_needed(n, d):
    """The smallest number of groups of d that hold n things (counting up in d until the total reaches n)."""
    k = 0
    while k * d < n:
        k += 1
    return k


DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


def day_after(start, n):
    """The day n days after `start` (n may be negative), found by stepping one day at a time."""
    i = DAYS.index(start)
    for _ in range(abs(n)):
        i = i + 1 if n > 0 else i - 1
        i = 0 if i == 7 else (6 if i == -1 else i)
    return DAYS[i]


# ---------------------------------------------------------------- fractions: typed answers
def ftxt(f):
    f = Fr(f)
    return str(f.numerator) if f.denominator == 1 else f'{f.numerator}/{f.denominator}'


def eq_forms(f, maxk=12):
    """Every way to write the fraction f as n/d with the same value (k times the top and bottom of the simplest form), simplest first."""
    f = Fr(f)
    return [f'{f.numerator * k}/{f.denominator * k}' for k in range(1, maxk + 1)]


def list_forms(parts, ordered=True):
    """A typed list of fractions 'a, b, c' (comma, semicolon, space, 'and' before the last; with ' < ' too when ordered); the first form is the plain 'a, b, c'.
    parts: list of strings.  All orders when not ordered."""
    orders = [list(parts)] if ordered else [list(p) for p in itertools.permutations(parts)]
    out = []
    for o in orders:
        seps = [', ', ';', ' '] + ([' < '] if ordered else [])
        for sp in seps:
            out.append(sp.join(o))
        if len(o) > 1:
            out.append(', '.join(o[:-1]) + ' and ' + o[-1])
    first = ', '.join(parts)
    return [first] + sorted(set(out) - {first})


def fracs_between(lo, hi, maxd=48):
    """Every n/d (d up to maxd, not only the simplest form) strictly between lo and hi, as typed text; found by cross-multiplying."""
    lo, hi = Fr(lo), Fr(hi)
    out = []
    for d in range(1, maxd + 1):
        for n in range(1, d):
            if lo < Fr(n, d) < hi:
                out.append(f'{n}/{d}')
    return out


def ways(units, sizes=(4, 2, 1), pieces=None):
    """All ways to fill `units` eighths with pieces of the given sizes in eighths (halves 4, quarters 2, eighths 1), order not mattering.
    Each way is (halves, quarters, eighths); listed with the most halves first, then the most quarters.  pieces: only the ways that use exactly that many pieces."""
    out = []
    for h in range(units // sizes[0], -1, -1):
        for q in range((units - h * sizes[0]) // sizes[1], -1, -1):
            e = units - h * sizes[0] - q * sizes[1]
            if e >= 0 and (pieces is None or h + q + e == pieces):
                out.append((h, q, e))
    return out


# ---------------------------------------------------------------- figures
SKY = '#DDEBF7'
BLU = '#BFE3F7'
GRN = '#CDEBD7'


def sfr(x, y, n, d, size=20, col=None):
    """A stacked fraction centred at x, the fraction line at y."""
    h = _h()
    col = col or h.NAVY
    w = max(len(str(n)), len(str(d))) * size * 0.62 + 6
    return (h.T(x, y - 4, n, size, 'middle', 800, col) + h.Ln(x - w / 2, y, x + w / 2, y, 2, col) + h.T(x, y + size - 1, d, size, 'middle', 800, col))


def wall_fig(caption='Fraction wall: one whole, halves, thirds, quarters, sixths, eighths and twelfths'):
    """The fraction wall of Lesson 6 Q1: one whole and rows of halves, thirds, quarters, sixths, eighths and twelfths (each row is the same whole cut into equal parts)."""
    h = _h()
    dens = [1, 2, 3, 4, 6, 8, 12]
    x0, W, rh = 4, 480, 54
    body = ''
    for r, d in enumerate(dens):
        y = 4 + r * rh
        w = W / d
        fill = h.YEL if d == 1 else (SKY if r % 2 else '#fff')
        for i in range(d):
            body += h.Re(round(x0 + i * w, 2), y, round(w, 2), rh, fill, h.NAVY, 2.2)
            if d == 1:
                body += h.T(x0 + W / 2, y + 34, '1 whole', 24, 'middle', 800)
            else:
                body += sfr(round(x0 + i * w + w / 2, 2), y + 26, 1, d, 20 if d < 12 else 19)
    return h.svg(W + 2 * x0, 4 + len(dens) * rh + 4, body, caption)


_SHAPES = dict(A=(4, 1), B=(8, 2), C=(6, 2), D=(12, 3), E=(8, 3))     # shape: (equal parts, shaded parts) as printed


def shapes_fig(caption='Five shapes A to E, each cut into equal parts with some parts shaded'):
    """The five shapes of Lesson 6 Q3, bigger than the printed row so that the parts can be counted on a phone: A square with both diagonals, B strips, C a circle in sixths,
    D a 4 by 3 grid, E a 4 by 2 grid.  The shaded parts are the printed ones."""
    h = _h()
    import math
    NV, Y = h.NAVY, '#FFC93C'
    body = ''
    lab = lambda x, y, t: h.T(x, y, t, 26, 'middle', 800)
    # A: square 108, both diagonals, top triangle shaded
    x, y, a = 6, 8, 108
    body += f'<polygon points="{x},{y} {x + a},{y} {x + a / 2},{y + a / 2}" fill="{Y}"/>'
    body += h.Re(x, y, a, a, 'none', NV, 2.8) + h.Ln(x, y, x + a, y + a, 2.2) + h.Ln(x + a, y, x, y + a, 2.2) + lab(x + a / 2, 142, 'A')
    # B: 8 strips, strips 2 and 6 shaded
    x, y, w, hh = 132, 22, 112, 80
    for i in range(8):
        body += h.Re(round(x + i * w / 8, 2), y, round(w / 8, 2), hh, Y if i in (1, 5) else '#fff', NV, 2.2)
    body += lab(x + w / 2, 142, 'B')
    # C: circle in 6 equal sectors, first two shaded
    cx, cy, R = 300, 62, 54
    for i in range(6):
        a0, a1 = math.radians(i * 60 - 90), math.radians((i + 1) * 60 - 90)
        body += (f'<path d="M{cx},{cy} L{round(cx + R * math.cos(a0), 2)},{round(cy + R * math.sin(a0), 2)} A{R},{R} 0 0 1 {round(cx + R * math.cos(a1), 2)},{round(cy + R * math.sin(a1), 2)} Z" '
                 f'fill="{Y if i < 2 else "#fff"}" stroke="{NV}" stroke-width="2.2"/>')
    body += lab(cx, 142, 'C')
    # D: 4 by 3 grid of squares, three shaded (not next to each other); E: 4 by 2 grid, three shaded
    c = 30
    xd, yd = 40, 176
    for r in range(3):
        for k in range(4):
            body += h.Re(xd + k * c, yd + r * c, c, c, Y if f'{k},{r}' in ('0,0', '2,1', '1,2') else '#fff', NV, 2.2)
    body += lab(xd + 2 * c, 290, 'D')
    xe, ye = 210, 190
    for r in range(2):
        for k in range(4):
            body += h.Re(xe + k * c, ye + r * c, c, c, Y if f'{k},{r}' in ('0,0', '1,0', '3,1') else '#fff', NV, 2.2)
    body += lab(xe + 2 * c, 290, 'E')
    return h.svg(360, 300, body, caption)


def cards_fig(yellow, blue, caption='Ten fraction cards: five yellow and five blue'):
    """The ten partner cards of Lesson 6 Q6 (take-home): a row of five yellow cards and a row of five blue cards.  yellow, blue: lists of (top, bottom)."""
    h = _h()
    cw, ch, gap, x0 = 58, 78, 8, 4
    body = ''
    for r, (name, cards, fill) in enumerate((('Yellow cards', yellow, '#FFE08A'), ('Blue cards', blue, BLU))):
        y = 6 + r * (ch + 40)
        body += h.T(x0, y + 16, name, 17, 'start', 800, h.TEAL)
        for i, (n, d) in enumerate(cards):
            x = x0 + i * (cw + gap)
            body += h.Re(x, y + 26, cw, ch, fill, h.NAVY, 2.4, 9) + sfr(x + cw / 2, y + 26 + ch / 2 - 1, n, d, 22)
    return h.svg(x0 * 2 + 5 * cw + 4 * gap, 2 * (ch + 40) + 2, body, caption)


def pieces_fig(caption='The pieces you may use: 1/2, 1/4 and 1/8 of a whole bar'):
    """The three kinds of piece in the 'ways' puzzles (Lesson 6 Go further 6 and Investigation): a half, a quarter and an eighth, drawn to the same scale."""
    h = _h()
    u = 34
    body = h.T(4, 18, 'Pieces you may use:', 16, 'start', 800)
    x = 4
    for name, k, col in (('1/2', 4, '#FFE08A'), ('1/4', 2, BLU), ('1/8', 1, GRN)):
        body += h.Re(x, 28, k * u, 34, col, h.NAVY, 2.4) + h.T(x + k * u / 2, 51, name, 17, 'middle', 800)
        x += k * u + 14
    return h.svg(x, 70, body, caption)


def ways_fig(ways_list, units, caption, whole_label='1 whole'):
    """Each way of filling the bar drawn as a row of pieces (halves yellow, quarters blue, eighths green), most halves first.
    ways_list: [(halves, quarters, eighths)], units: the length of the bar in eighths (8 = 1 whole, 6 = 3/4)."""
    h = _h()
    u, rh, x0 = 34, 42, 62
    body = ''
    for r, (hh, q, e) in enumerate(ways_list):
        y = 6 + r * rh
        body += h.T(4, y + 25, f'Way {r + 1}', 15, 'start', 800)
        x = x0
        for k, name, col, cnt in ((4, '1/2', '#FFE08A', hh), (2, '1/4', BLU, q), (1, '1/8', GRN, e)):
            for _ in range(cnt):
                body += h.Re(x, y, k * u, 34, col, h.NAVY, 2.2) + h.T(x + k * u / 2, y + 23, name, 15 if k > 1 else 13, 'middle', 800)
                x += k * u
    return h.svg(x0 + units * u + 8, 6 + len(ways_list) * rh, body, caption)


from p3lib import grp      # noqa: E402,F401  (frame helper shared with weeks 1 and 2)
