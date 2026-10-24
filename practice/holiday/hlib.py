"""Shared helpers for the online holiday practice lessons (any level): SVG figure helpers, the accepted wordings of a counting rule,
and small brute-force helpers that lesson files use for their INDEPENDENT checkers.

A lesson file (practice/holiday/<level key>/<NN>/lesson.py) imports this as `from hlib import *`.
Figures are drawn here as inline SVG (viewBox only, width 100%), sized so that the text is at least about 12 px on a 390 px phone.
No coin or note pictures.
"""
import itertools, re

NAVY, YEL, TEAL, WARM, PALE = '#1B2A49', '#FFE08A', '#1F7A6F', '#B5481F', '#FFF9E8'


# ---------------------------------------------------------------- svg basics
def svg(w, h, body, label):
    return (f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{esc(label)}" '
            f'style="width:100%;max-width:{w}px;height:auto;display:block;margin:0 auto" font-family="Nunito Sans, Arial, sans-serif">{body}</svg>')


def esc(s):
    return str(s).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')


def T(x, y, s, size=15, anchor='middle', w=700, fill=NAVY, italic=False):
    return (f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{w}" text-anchor="{anchor}" fill="{fill}"'
            f'{" font-style=\"italic\"" if italic else ""}>{esc(s)}</text>')


def Ln(x1, y1, x2, y2, sw=2.5, c=NAVY, dash=None):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{c}" stroke-width="{sw}" stroke-linecap="round"' + (f' stroke-dasharray="{dash}"' if dash else '') + '/>'


def Ci(x, y, r, fill='none', stroke=NAVY, sw=2.4):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'


def Re(x, y, w, h, fill='none', stroke=NAVY, sw=2.4, rx=0, dash=None):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"' + (f' stroke-dasharray="{dash}"' if dash else '') + '/>'


# ---------------------------------------------------------------- number line with hops (frog)
def number_line(lo=0, hi=20, hops=None, circled=(), crosses=(), caption='', first_hop_only=False):
    """A number line lo..hi, one label per number. hops: list of (from, to). circled: numbers ringed. crosses: numbers marked with an X above the line."""
    sp, x0 = 20, 20
    W = (hi - lo) * sp + 2 * x0 + 6
    y = 62
    px = lambda n: x0 + (n - lo) * sp
    b = ''
    if caption:
        b += T(x0 - 8, 16, caption, 14, 'start', 800)
    b += Ln(px(lo) - 10, y, px(hi) + 12, y, 3)
    for n in range(lo, hi + 1):
        b += Ln(px(n), y - 6, px(n), y + 6, 2.2) + T(px(n), y + 26, n, 15)
    for a, c in (hops or []):
        mx = (px(a) + px(c)) / 2
        b += f'<path d="M{px(a)} {y - 9} Q{mx} {y - 46} {px(c)} {y - 9}" fill="none" stroke="{TEAL}" stroke-width="2.4"/>'
        b += f'<polygon points="{px(c)},{y - 8} {px(c) - 5},{y - 17} {px(c) + 4},{y - 16}" fill="{TEAL}"/>'
        b += T(mx, y - 38, c - a, 14, 'middle', 800, TEAL)
    for n in circled:
        b += Ci(px(n), y, 11, YEL, NAVY, 2.2) + T(px(n), y + 5, n, 14)
    for n in crosses:
        b += T(px(n), y - 14, '×', 24, 'middle', 800, WARM)
    return svg(W, 96, b, caption or f'Number line from {lo} to {hi}')


def stack(*figs):
    """Several figures one above the other (each is its own svg)."""
    return ''.join(f'<div style="margin:0 0 6px">{f}</div>' for f in figs)


# ---------------------------------------------------------------- boxes of dots (stickers)
def dot_boxes(counts, blank_from=None, caption=''):
    """Boxes 1..n, each shows `counts[i]` dots; boxes with None are empty dashed 'draw here' boxes."""
    bw, bh, gp, x0, y0 = 84, 64, 22, 8, 26
    W = x0 * 2 + len(counts) * bw + (len(counts) - 1) * gp
    b = ''
    for i, n in enumerate(counts):
        x = x0 + i * (bw + gp)
        b += T(x + bw / 2, y0 - 8, f'Box {i + 1}', 15) + Re(x, y0, bw, bh, '#fff' if n is None else PALE, NAVY, 2.4, 8, '5 4' if n is None else None)
        if n is None:
            b += T(x + bw / 2, y0 + bh / 2 + 5, 'draw here', 13, 'middle', 600, '#44506F', True)
        else:
            for k in range(n):
                cx, cy = x + 14 + (k % 4) * 19, y0 + 14 + (k // 4) * 19
                b += Ci(cx, cy, 7, YEL, NAVY, 1.6)
        if i < len(counts) - 1:
            b += T(x + bw + gp / 2, y0 + bh / 2 + 5, '+3', 13, 'middle', 800, TEAL)
    return svg(W, y0 + bh + 8, b, caption or 'Boxes of sticker dots')


# ---------------------------------------------------------------- two bars (smaller / bigger, difference)
def two_bars(total, diff, small=None, big=None):
    b = T(8, 22, 'smaller', 14, 'start') + T(8, 62, 'bigger', 14, 'start')
    unit = 22
    sw = (small if small is not None else 4) * unit
    bgw = sw + diff * unit
    b += Re(80, 6, sw, 24, YEL, NAVY, 2.4) + T(80 + sw / 2, 24, '?' if small is None else small, 16)
    b += Re(80, 46, sw, 24, YEL, NAVY, 2.4) + Re(80 + sw, 46, diff * unit, 24, '#fff', NAVY, 2.4, 0, '4 3')
    b += T(80 + sw / 2, 64, '?' if big is None else big, 16) + T(80 + sw + diff * unit / 2, 64, diff, 14, 'middle', 800, TEAL)
    b += Ln(80, 84, 80 + bgw, 84, 2.4) + T(80 + bgw / 2, 100, f'{total} altogether', 14, 'middle', 800)
    return svg(80 + bgw + 14, 108, b, f'Two bars. The bigger number is {diff} more than the smaller. Together they make {total}.')


# ---------------------------------------------------------------- magic triangle
def magic_triangle(corners=(None, None, None), sides=(None, None, None), caption=''):
    """corners: top, bottom-left, bottom-right.  sides: left side (top to bottom-left), bottom (left to right), right side (top to bottom-right)."""
    top, bl, br = (150, 34), (40, 224), (260, 224)
    mid = lambda p, q: ((p[0] + q[0]) / 2, (p[1] + q[1]) / 2)
    pts = [top, bl, br, mid(top, bl), mid(bl, br), mid(top, br)]
    vals = list(corners) + list(sides)
    b = Ln(*top, *bl, 3) + Ln(*bl, *br, 3) + Ln(*br, *top, 3)
    for p, v in zip(pts, vals):
        b += Ci(p[0], p[1], 22, YEL if v is not None else '#fff', NAVY, 2.6)
        if v is not None:
            b += T(p[0], p[1] + 7, v, 21)
    return svg(300, 256, b, caption or 'A triangle with a circle at each corner and one in the middle of each side')


# ---------------------------------------------------------------- shapes with totals (circles and squares)
def shape_sums(rows):
    """rows: list of (n_circles, n_squares, total).  Draws  ● ● ■ = 12"""
    b = ''
    for k, (c, s, tot) in enumerate(rows):
        y = 28 + k * 56
        x = 12
        for _ in range(c):
            b += Ci(x + 18, y, 18, YEL, NAVY, 2.4); x += 46
        for _ in range(s):
            b += Re(x, y - 17, 34, 34, '#CDE8F7', NAVY, 2.4); x += 46
        b += T(x + 8, y + 7, '=', 22, 'start') + T(x + 34, y + 7, tot, 22, 'start')
    return svg(250, 28 + 56 * len(rows) - 12, b, 'Shape sums: ' + '; '.join(f'{c} circle{"s" if c != 1 else ""} and {s} square{"s" if s != 1 else ""} make {t}' for c, s, t in rows))


# ---------------------------------------------------------------- the accepted wordings of a counting rule
UP = ['add', 'adds', 'plus', '+', 'up', 'up by', 'go up', 'go up by', 'goes up', 'goes up by', 'jump', 'jumps', 'hop', 'hops', 'jump on', 'hop on',
      'count on', 'count up', 'counting on', 'add on', 'adding', 'increase', 'increases', 'increase by', 'increases by', 'count on by', 'plus on']
DOWN = ['take away', 'takes away', 'take', 'takes', 'minus', '-', '−', 'down', 'down by', 'go down', 'go down by', 'goes down', 'goes down by',
        'subtract', 'subtracts', 'subtracting', 'take off', 'count back', 'count down', 'counting back', 'decrease', 'decreases', 'decrease by', 'jump back', 'hop back']
TAIL = ['', ' each time', ' every time', ' each step', ' every step', ' each hop', ' every hop', ' each jump', ' each go', ' each number']


def rule_accepts(direction, n):
    """Accepted typed wordings of 'add n' / 'take away n' (the same list is used by the browser and by the server key; matching ignores case and spacing).
    A bare number is accepted too: the direction is clear from the numbers in the question."""
    verbs = UP if direction == 'add' else DOWN
    out = {str(n)}
    for v in verbs:
        for t in TAIL:
            out.add(f'{v} {n}{t}')
            out.add(f'{v} by {n}{t}' if v in ('add', 'take away', 'take', 'minus', 'subtract', 'plus') else f'{v} {n}{t}')
    more = 'more' if direction == 'add' else 'less'
    for t in TAIL:
        out.add(f'{n} {more}{t}')
        out.add(f'{n} {"up" if direction == "add" else "down"}{t}')
    if direction == 'add':
        out.update([f'+{n}', f'+ {n}', f'plus {n}', f'{n} added', f'add {n} on'])
    else:
        out.update([f'-{n}', f'− {n}', f'−{n}', f'- {n}', f'{n} fewer', f'{n} taken away', f'{n} take away', f'take {n} away', f'take away {n} each time'])
    return sorted(out)


def rule_of(seq):
    """Independent: the rule of an arithmetic sequence, ('add', d) or ('take away', d); raises if it is not arithmetic."""
    ds = {b - a for a, b in zip(seq, seq[1:])}
    if len(ds) != 1:
        raise ValueError('not an arithmetic sequence')
    d = ds.pop()
    return ('add', d) if d > 0 else ('take away', -d)


# ---------------------------------------------------------------- brute-force helpers for checkers
def ap(start, step, count):
    """Arithmetic list built by repeated adding (no formula)."""
    out, v = [], start
    for _ in range(count):
        out.append(v); v += step
    return out


def count_up_to(step, limit, start=None):
    """Counting in `step`s from `start` (default step) while the number is <= limit."""
    v = step if start is None else start
    out = []
    while v <= limit:
        out.append(v); v += step
    return out


def pairs_sum(total, lo=0, hi=None, ordered=False):
    hi = total if hi is None else hi
    out = []
    for a in range(lo, hi + 1):
        for b in range(lo, hi + 1):
            if a + b == total and (ordered or a <= b):
                out.append((a, b))
    return out


def magic_solutions(numbers, side_total):
    """All ways to place `numbers` (six of them) in the magic triangle so that every side adds to side_total.
    Returns a set of (corner triple as sorted tuple, tuple of the three side numbers by side: top-left corner pair etc.) as full arrangements
    (top, bottom-left, bottom-right, left-mid, bottom-mid, right-mid)."""
    sols = []
    for t, bl, br, lm, bm, rm in itertools.permutations(numbers, 6):
        if t + lm + bl == side_total and bl + bm + br == side_total and t + rm + br == side_total:
            sols.append((t, bl, br, lm, bm, rm))
    return sols


def unique_text(s):
    return re.sub(r'\s+', ' ', s).strip()
