"""Shared helpers for the online holiday practice lessons (any level): SVG figure helpers, the accepted wordings of a counting rule,
and small brute-force helpers that lesson files use for their INDEPENDENT checkers.

A lesson file (practice/holiday/<level key>/<NN>/lesson.py) imports this as `from hlib import *`.
Figures are drawn here as inline SVG (viewBox only, width 100%), sized so that the text is at least about 12 px on a 390 px phone.
No coin or note pictures.
"""
import itertools, re
from fractions import Fraction

NAVY, YEL, TEAL, WARM, PALE = '#1B2A49', '#FFE08A', '#1F7A6F', '#B5481F', '#FFF9E8'


# ---------------------------------------------------------------- svg basics
MIN_PX, PHONE_PX = 12.5, 290     # figure text is at least MIN_PX (12.5: the 4 px viewBox padding takes about 3%) on a 360 px phone, where a figure is about PHONE_PX wide (card padding and page margins taken off)
SOL_PX = 250                     # a SOLUTION figure sits inside the grey/green answer box (more padding): about SOL_PX wide on a 360 px phone
PAD = 4                          # viewBox padding on every side, so strokes and rounded text at the edge are not cut off (the svg also has overflow visible)


def lift_text(w, body, phone=PHONE_PX):
    """Raise any font-size so the text is at least MIN_PX on screen when the figure is shown `phone` px wide (the figure is scaled by phone / w)."""
    scale = min(1.0, phone / w)
    need = round(MIN_PX / scale, 1)
    def fix(m):
        v = float(m.group(1))
        return f'font-size="{max(v, need):g}"'
    return re.sub(r'font-size="([\d.]+)"', fix, body)


def lift_svg(svg_text, solution=False):
    """The final pass over a finished <svg ...> string (the builder runs it once on every question and solution figure, after the lesson has composed it):
    the viewBox gets PAD of padding on every side (strokes and text at the edge are not cut off), the font sizes are lifted so the text is at least MIN_PX on a 360 px phone
    (solution=True: for the narrower solution box, SOL_PX), and the root svg gets overflow="visible". The lesson's own viewBox still reads "0 0 w h" while it composes figures."""
    out = svg_text
    m = re.search(r'viewBox="([-\d.]+) ([-\d.]+) ([\d.]+) ([\d.]+)"', out)
    if m:
        x, y, w, h = (float(v) for v in m.groups())
        W, H = w + 2 * PAD, h + 2 * PAD
        out = out.replace(m.group(0), f'viewBox="{x - PAD:g} {y - PAD:g} {W:g} {H:g}"', 1)
        out = re.sub(r'max-width:' + re.escape(f'{w:g}') + 'px', f'max-width:{W:g}px', out, count=1)
        out = lift_text(W, out, SOL_PX if solution else PHONE_PX)
    if re.match(r'\s*<svg\b', out) and 'overflow=' not in out[:out.index('>')]:
        out = re.sub(r'<svg\b', '<svg overflow="visible"', out, count=1)
    return out


def svg(w, h, body, label):
    body = lift_text(w, body)
    return (f'<svg viewBox="0 0 {w} {h}" overflow="visible" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{esc(label)}" '
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
    """A number line lo..hi, one label per number; a long line is drawn as two rows (the second starts where the first ends, so the number
    in the middle appears in both). hops: list of (from, to), a hop over the break is drawn as two arcs. circled: numbers ringed. crosses: X above."""
    span = hi - lo
    rows = [(lo, hi)] if span <= 12 else [(lo, lo + span // 2), (lo + span // 2, hi)]
    sp, x0 = (30 if len(rows) > 1 else 28), 22
    W = max(r[1] - r[0] for r in rows) * sp + 2 * x0 + 4
    rh = 92
    top = 24 if caption else 4
    body = T(6, 17, caption, 15, 'start', 800) if caption else ''
    for k, (a, c) in enumerate(rows):
        y = top + k * rh + 62
        px = lambda n: x0 + (n - a) * sp
        body += Ln(px(a) - 12, y, px(c) + 12, y, 3)
        for n in range(a, c + 1):
            body += Ln(px(n), y - 6, px(n), y + 6, 2.2) + T(px(n), y + 26, n, 16)
        for h0, h1 in (hops or []):
            s0, s1 = max(h0, a), min(h1, c)
            if s0 >= s1:
                continue
            mx = (px(s0) + px(s1)) / 2
            body += f'<path d="M{px(s0)} {y - 9} Q{mx} {y - 50} {px(s1)} {y - 9}" fill="none" stroke="{TEAL}" stroke-width="2.4"/>'
            if s1 == h1:
                body += f'<polygon points="{px(s1)},{y - 8} {px(s1) - 5},{y - 17} {px(s1) + 4},{y - 16}" fill="{TEAL}"/>'
            if (s1 - s0) * 2 >= (h1 - h0):
                body += T(mx, y - 36, h1 - h0, 15, 'middle', 800, TEAL)
        for n in circled:
            if a <= n <= c:
                body += Ci(px(n), y, 12, YEL, NAVY, 2.2) + T(px(n), y + 5, n, 15)
        for n in crosses:
            if a <= n <= c:
                body += T(px(n), y - 12, '×', 26, 'middle', 800, WARM)
    return svg(W, top + (len(rows) - 1) * rh + 96, body, caption or f'Number line from {lo} to {hi}')


def stack(*figs):
    """Several figures one above the other (each is its own svg)."""
    return ''.join(f'<div style="margin:0 0 6px">{f}</div>' for f in figs)


# ---------------------------------------------------------------- boxes of dots (stickers)
def dot_boxes(counts, blank_from=None, caption=''):
    """Boxes 1..n, each shows `counts[i]` dots; boxes with None are empty dashed 'draw here' boxes."""
    bw, bh, gp, x0, y0 = 66, 58, 28, 6, 26
    W = x0 * 2 + len(counts) * bw + (len(counts) - 1) * gp
    b = ''
    for i, n in enumerate(counts):
        x = x0 + i * (bw + gp)
        b += T(x + bw / 2, y0 - 8, f'Box {i + 1}', 15) + Re(x, y0, bw, bh, '#fff' if n is None else PALE, NAVY, 2.4, 8, '5 4' if n is None else None)
        if n is None:
            b += T(x + bw / 2, y0 + bh / 2 - 2, 'draw', 14, 'middle', 600, '#44506F', True) + T(x + bw / 2, y0 + bh / 2 + 14, 'here', 14, 'middle', 600, '#44506F', True)
        else:
            for k in range(n):
                cx, cy = x + 11 + (k % 4) * 15, y0 + 12 + (k // 4) * 15
                b += Ci(cx, cy, 6, YEL, NAVY, 1.5)
        if i < len(counts) - 1:
            b += T(x + bw + gp / 2, y0 + bh / 2 + 5, '+3', 14, 'middle', 800, TEAL)
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


# ---------------------------------------------------------------- algebra rules and equal fractions: the BUILD-TIME twins of the checks in practice/submit/mark.js (same grammar, exact arithmetic)
# poly_parse(s, var): a tiny recursive-descent parser for digits, one letter, + - x * / ( ) ^ and writing side by side (4n, 4(n+3)); division only by a number; NOTHING is evaluated as code.
# It returns the polynomial as a tuple of Fractions (constant term first) or None. rule_equal / poly_ok say whether a typed rule equals the key as a polynomial ('=' chains allowed).
_MINUS = re.compile('[\u2212\u2013\u2014\u2010\u2011]')


def poly_parse(s, var='n'):
    import unicodedata
    s = _MINUS.sub('-', unicodedata.normalize('NFKC', str(s).replace('\u00b2', '^2').replace('\u00b3', '^3'))).lower()
    for ch in '\u00d7\u00b7\u22c5*':
        s = s.replace(ch, '*')
    s = s.replace('\u00f7', '/')
    if var != 'x':
        s = s.replace('x', '*')
    if re.search(r'\d\s+\d', s):
        return None
    t = re.findall(r'\d+\.?\d*|\.\d+|[-+*/()^]|.', re.sub(r'\s+', '', s))
    st = {'p': 0, 'bad': False}
    isnum = lambda x: x is not None and re.fullmatch(r'\d+\.?\d*|\.\d+', x) is not None
    at = lambda i: t[i] if 0 <= i < len(t) else None

    def mul(a, b):
        if len(a) + len(b) > 10:
            st['bad'] = True
            return [Fraction(0)]
        r = [Fraction(0)] * (len(a) + len(b) - 1)
        for i, x in enumerate(a):
            for j, y in enumerate(b):
                r[i + j] += x * y
        return r

    def nxt():
        x = at(st['p']); st['p'] += 1
        return x

    def atom():
        x = nxt()
        if x == '(':
            v = total()
            if nxt() != ')':
                st['bad'] = True
            return v
        if x == var:
            return [Fraction(0), Fraction(1)]
        if isnum(x):
            return [Fraction(x.rstrip('.') or '0')]
        st['bad'] = True
        return [Fraction(0)]

    def power():
        b = atom()
        if at(st['p']) == '^':
            st['p'] += 1
            e = nxt()
            if e is None or not re.fullmatch(r'[0-4]', e):
                st['bad'] = True
                return b
            r = [Fraction(1)]
            for _ in range(int(e)):
                r = mul(r, b)
            return r
        return b

    def unary():
        if at(st['p']) == '-':
            st['p'] += 1
            return mul([Fraction(-1)], unary())
        if at(st['p']) == '+':
            st['p'] += 1
            return unary()
        return power()

    def prod():
        v = unary()
        while True:
            o = at(st['p'])
            if o == '*':
                st['p'] += 1; v = mul(v, unary())
            elif o == '/':
                st['p'] += 1
                d = unary()
                if len(d) != 1 or d[0] == 0:
                    st['bad'] = True
                    return v
                v = [c / d[0] for c in v]
            elif o == '(' or o == var or (isnum(o) and not isnum(at(st['p'] - 1))):
                v = mul(v, power())
            else:
                return v

    def total():
        v = prod()
        while at(st['p']) in ('+', '-'):
            o = nxt(); r = prod()
            n = max(len(v), len(r))
            v = [(v[i] if i < len(v) else 0) + (1 if o == '+' else -1) * (r[i] if i < len(r) else 0) for i in range(n)]
        return v

    out = total()
    if st['bad'] or st['p'] < len(t):
        return None
    out = list(out)
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return tuple(out)


def rule_sides(s):
    """The sides of a typed chain 'a = b = c' that are not the word OUT (a final full stop is ignored)."""
    return [x.strip() for x in _MINUS.sub('-', str(s)).strip().rstrip('.!').split('=') if not re.fullmatch(r'(?i)out', x.strip())]


def poly_ok(keys, v, var='n'):
    """True if every side of the typed rule equals (as a polynomial in `var`) one of the sides of the keys."""
    kp = [q for k in keys for sd in rule_sides(k) for q in [poly_parse(sd, var)] if q is not None]
    sides = rule_sides(v)
    return bool(sides) and bool(kp) and all((q := poly_parse(sd, var)) is not None and q in kp for sd in sides)


def auto_poly(accept, var='n'):
    """The letter if EVERY accepted writing of a text item is an expression in that letter and they are all the same polynomial (and it really uses the letter), else None.
    The builder turns such an item into 'compare as a polynomial' without the lesson file saying so."""
    polys = set()
    for a in accept:
        sides = rule_sides(a)
        if not sides:
            return None
        for sd in sides:
            q = poly_parse(sd, var)
            if q is None:
                return None
            polys.add(q)
    return var if len(polys) == 1 and len(next(iter(polys))) > 1 else None


def frac_tokens(s):
    """('7/12, 8/12 10/12') -> ([(7,12), (8,12), (10,12)], '') : the fractions in a typed list, and any other symbols left (such as '<'), spaces, commas and semicolons removed."""
    import unicodedata
    toks = []
    txt = re.sub(r'\s*/\s*', '/', _MINUS.sub('-', unicodedata.normalize('NFKC', str(s))))

    def one(m):
        if m.group(2) is not None:
            toks.append(((int(m.group(2)) * int(m.group(4)) + int(m.group(3))) * (-1 if m.group(1) else 1), int(m.group(4))))
        elif m.group(5) is not None:
            toks.append((int(m.group(5)), int(m.group(6))))
        else:
            toks.append((int(m.group(0)), 1))
        return ' '
    rest = re.sub(r'(-?)(\d+)\s+(\d+)/(\d+)|(-?\d+)/(\d+)|-?\d+', one, txt)
    return toks, re.sub(r'[\s,;]+', '', rest).rstrip('.!')


def frac_list_ok(keys, v):
    V, vr = frac_tokens(v)
    if not V or any(d <= 0 for _, d in V):
        return False
    for k in keys:
        K, kr = frac_tokens(k)
        if len(K) == len(V) and kr == vr and all(d > 0 and n * V[i][1] == V[i][0] * d for i, (n, d) in enumerate(K)):
            return True
    return False
