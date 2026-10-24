"""Level 6 helpers for the online holiday practice lessons (shared by practice/holiday/p6/NN/lesson.py).

* figures: the workbook's own drawing code (p6/content/l1.js blocks() and sticksSvg(), l2.js treesSvg()) is called through blocks_bridge.js, so the code blocks
  on the screen are the code blocks printed in the workbook.  `compose` stacks several of them into ONE svg (the shared runner takes a single <svg> per figure).
* `run`: a small INDEPENDENT interpreter for the block programs (set / change / repeat / if ... mod ... / say); the checkers of every code question run the
  program as drawn, they never copy the printed answer.
* number helpers (factors, primes, prime factorisation, sequences) written as plain loops, and a factor-tree drawing built from the checked factorisation.
"""
import json, os, re, subprocess
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
NAVY, YEL, TEAL, WARM, PALE = '#1B2A49', '#FFC93C', '#1F7A6F', '#B5481F', '#FFF9E8'


# ---------------------------------------------------------------- figures from the workbook's own generators
_cache = {}


def bridge(reqs):
    key = json.dumps(reqs, sort_keys=True)
    if key not in _cache:
        r = subprocess.run(['node', os.path.join(HERE, 'blocks_bridge.js')], input=key, capture_output=True, text=True, check=True)
        _cache[key] = json.loads(r.stdout)
    return _cache[key]


def blocks(prog, label='Code', fs=14):
    svg = bridge([dict(kind='blocks', prog=prog, label=label, fs=fs)])[0]
    svg = svg.replace('#D64545', '#C03B3B')               # the workbook's red block is 4.38:1 with its white text; this red is 5.3:1 (the printed colour is unchanged)
    return re.sub(r'<text[^>]*>\s*</text>', '', svg)       # an empty value slot is drawn with a blank text node: not needed


def sticks_fig():
    """Matchstick squares, patterns 1 to 3 (same drawing as the workbook, redrawn at a width that is readable on a phone)."""
    s, gap, x, g = 34, 30, 22, ''

    def stick(x1, y1, x2, y2):
        import math
        dx, dy = x2 - x1, y2 - y1
        L = math.hypot(dx, dy); ux, uy = dx / L, dy / L
        a, b = (x1 + ux * 4, y1 + uy * 4), (x2 - ux * 4, y2 - uy * 4)
        return (f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" stroke="{NAVY}" stroke-width="4.5" stroke-linecap="round"/>'
                f'<circle cx="{b[0]:.1f}" cy="{b[1]:.1f}" r="3.8" fill="#D64545"/>')
    for k in (1, 2, 3):
        top, bot = 12, 12 + s
        for j in range(k):
            x0 = x + j * s
            g += stick(x0, top, x0 + s, top) + stick(x0, bot, x0 + s, bot)
        for j in range(k + 1):
            x0 = x + j * s
            g += stick(x0, bot, x0, top)
        g += T(x + k * s / 2, bot + 26, f'Pattern {k}', 15, 'middle', 700, TEAL)
        x += k * s + gap
    W = x - gap + 22
    return (f'<svg viewBox="0 0 {W} 92" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Matchstick squares in a row: patterns 1, 2 and 3" '
            f'style="width:100%;max-width:{W}px;height:auto;display:block;margin:0 auto">{g}</svg>')


def trees_fig():
    """Factor tree tops for 72 and 150, each splitting into two empty boxes (as printed)."""
    g = ''
    for cx, v in ((85, 72), (255, 150)):
        g += (f'<line x1="{cx}" y1="42" x2="{cx - 42}" y2="86" stroke="{NAVY}" stroke-width="2.5"/><line x1="{cx}" y1="42" x2="{cx + 42}" y2="86" stroke="{NAVY}" stroke-width="2.5"/>'
              f'<circle cx="{cx}" cy="24" r="21" fill="{YEL}" stroke="{NAVY}" stroke-width="2.5"/>' + T(cx, 31, v, 18, 'middle', 800) +
              f'<rect x="{cx - 76}" y="86" width="68" height="36" rx="8" fill="#fff" stroke="{NAVY}" stroke-width="2.5"/>'
              f'<rect x="{cx + 8}" y="86" width="68" height="36" rx="8" fill="#fff" stroke="{NAVY}" stroke-width="2.5"/>')
    return (f'<svg viewBox="0 0 340 130" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Factor tree tops for 72 and 150, each splitting into two empty boxes" '
            f'style="width:100%;max-width:340px;height:auto;display:block;margin:0 auto">{g}</svg>')


def esc(s):
    return str(s).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')


def T(x, y, s, size=15, anchor='middle', w=700, fill=NAVY):
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{w}" text-anchor="{anchor}" fill="{fill}" font-family="Nunito Sans, Arial, sans-serif">{esc(s)}</text>'


def _size(svg):
    m = re.search(r'viewBox="0 0 ([\d.]+) ([\d.]+)"', svg)
    return float(m.group(1)), float(m.group(2))


def _place(svg, x, y, scale=1.0):
    w, h = _size(svg)
    head_end = svg.index('>')
    head = svg[:head_end]
    head = re.sub(r'\s(width|height|style)="[^"]*"', '', head)
    return f'{head} x="{x:.1f}" y="{y:.1f}" width="{w * scale:.1f}" height="{h * scale:.1f}" style="width:{w * scale:.1f}px;height:{h * scale:.1f}px;max-width:none"' + svg[head_end:], w * scale, h * scale


def compose(rows, label, width=None, gap=10, pad=4, align='center'):
    """rows: list of svg strings or ('text', str) or (label_str, svg) stacked one above the other in one svg."""
    placed, ys, y, maxw = [], [], pad, 0
    for r in rows:
        if isinstance(r, tuple) and r[0] == '__text__':
            placed.append(('t', r[1], y)); y += 22; maxw = max(maxw, 10 * len(r[1]) * 0.6)
            continue
        lab = None
        if isinstance(r, tuple):
            lab, r = r
        w, h = _size(r)
        placed.append(('s', r, y, lab, w, h)); y += h + gap; maxw = max(maxw, w + (30 if lab else 0))
    W = width or maxw + 2 * pad
    body = ''
    for p in placed:
        if p[0] == 't':
            body += T(pad, p[2] + 15, p[1], 15, 'start', 800)
            continue
        _, s, yy, lab, w, h = p
        off = 30 if lab else 0
        x = pad + off + ((W - 2 * pad - off - w) / 2 if align == 'center' else 0)
        if lab:
            body += T(pad + 8, yy + h / 2 + 6, lab, 18, 'middle', 800)
        sv, _, _ = _place(s, x, yy)
        body += sv
    return (f'<svg viewBox="0 0 {W:.0f} {y:.0f}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{esc(label)}" '
            f'style="width:100%;max-width:{W:.0f}px;height:auto;display:block;margin:0 auto">{body}</svg>')


def text_row(s):
    return ('__text__', s)


# ---------------------------------------------------------------- the block-program interpreter (independent checker for every code question)
HAT = ['hat', 'when green flag clicked']


def _val(e, v):
    e = e.strip()
    if re.fullmatch(r'-?\d+', e):
        return int(e)
    return v[e]


def run(prog, v=None):
    """Runs a block program (the same nested lists the figure is drawn from). Returns (said values in order, final variables)."""
    v = dict(v or {}); said = []

    def go(items):
        for it in items:
            kind, text = it[0], it[1]
            if kind == 'hat':
                continue
            m = re.fullmatch(r'set (\w+) to \((.+)\)', text)
            if m:
                v[m.group(1)] = _val(m.group(2), v); continue
            m = re.fullmatch(r'change (\w+) by \((.+)\)', text)
            if m:
                v[m.group(1)] += _val(m.group(2), v); continue
            m = re.fullmatch(r'say \((.+?)\)( for \(\d+\) seconds)?', text)
            if m:
                said.append(_val(m.group(1), v)); continue
            m = re.fullmatch(r'repeat \((.+)\)', text)
            if m:
                for _ in range(_val(m.group(1), v)):
                    go(it[2])
                continue
            m = re.fullmatch(r'if \((\w+) mod (\w+) = (\w+)\) then', text)
            if m:
                if _val(m.group(1), v) % _val(m.group(2), v) == _val(m.group(3), v):
                    go(it[2])
                continue
            raise ValueError('cannot run block: ' + text)
    go(prog)
    return said, v


# ---------------------------------------------------------------- number helpers (plain loops)
def factors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def is_prime(n):
    return len(factors(n)) == 2


def primes_upto(n):
    return [k for k in range(2, n + 1) if is_prime(k)]


def prime_factors(n):
    out, d = [], 2
    while n > 1:
        while n % d == 0:
            out.append(d); n //= d
        d += 1
    return out


def ap(first, diff, count):
    out, v = [], first
    for _ in range(count):
        out.append(v); v += diff
    return out


def linear_rule(seq):
    """(difference, constant) so that term n = difference * n + constant, from the first terms (checks the difference is constant)."""
    d = seq[1] - seq[0]
    assert all(b - a == d for a, b in zip(seq, seq[1:])), 'not a constant difference'
    return d, seq[0] - d


def sticks_of_squares(k):
    """Matchsticks in a row of k squares, counted from the picture: top and bottom rows of k sticks each, and k+1 upright sticks."""
    return k + k + (k + 1)


def sticks_of_polygons(sides, n):
    """n regular shapes with `sides` sides in a row, each new one sharing one side with the one before."""
    total = sides
    for _ in range(n - 1):
        total += sides - 1
    return total


def goldbach_pairs(n):
    """Pairs of primes (p, q), p <= q, with p + q = n."""
    return [(p, n - p) for p in primes_upto(n // 2) if is_prime(n - p)]


def terms_below(first, diff, limit):
    return [t for t in ap(first, diff, limit) if t < limit]


# ---------------------------------------------------------------- factor trees (solution drawings, built from the checked factorisation)
def split_pair(n):
    """The factor pair of n closest together (a <= b, a > 1), or None when n is prime."""
    best = None
    for a in range(2, n):
        if a * a > n:
            break
        if n % a == 0:
            best = (a, n // a)
    return best


def _layout(n, x0, depth, leafw, levh):
    """(nodes, edges, width) for the factor tree of n placed from x0; nodes[0] is the root (cx, cy, value, is_prime)."""
    sp = split_pair(n)
    if sp is None:
        return [(x0 + leafw / 2, depth * levh, n, True)], [], leafw
    na, ea, wa = _layout(sp[0], x0, depth + 1, leafw, levh)
    nb, eb, wb = _layout(sp[1], x0 + wa, depth + 1, leafw, levh)
    cx = (na[0][0] + nb[0][0]) / 2
    cy = depth * levh
    edges = [(cx, cy, na[0][0], na[0][1]), (cx, cy, nb[0][0], nb[0][1])] + ea + eb
    return [(cx, cy, n, False)] + na + nb, edges, wa + wb


def factor_tree_svg(n, label):
    nodes, edges, w = _layout(n, 0, 0, 54, 54)
    maxy = max(nd[1] for nd in nodes)
    pad, r = 24, 19
    b = ''
    for x1, y1, x2, y2 in edges:
        b += f'<line x1="{x1 + pad:.1f}" y1="{y1 + pad:.1f}" x2="{x2 + pad:.1f}" y2="{y2 + pad:.1f}" stroke="{NAVY}" stroke-width="2.5"/>'
    for cx, cy, val, pr in nodes:
        b += (f'<circle cx="{cx + pad:.1f}" cy="{cy + pad:.1f}" r="{r}" fill="{YEL if pr else "#fff"}" stroke="{NAVY}" stroke-width="2.5"/>'
              + T(f'{cx + pad:.1f}', f'{cy + pad + 6:.1f}', val, 17, 'middle', 800))
    W, H = w + 2 * pad, maxy + 2 * pad
    return (f'<svg viewBox="0 0 {W:.0f} {H:.0f}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{esc(label)}" '
            f'style="width:100%;max-width:{W:.0f}px;height:auto;display:block;margin:0 auto">{b}</svg>')


# ---------------------------------------------------------------- end-of-lesson housekeeping (lesson-owned items only)
def finish(items, sol_px=250, minus=True):
    """Every self-check item gets an explicit marking_mode ('open' only for a truly open prompt, 'self' for explanations and paper-only items),
    and solution figures get their text sized for the narrower solution box (a 360 px phone shows them about sol_px wide)."""
    import re as _re
    for it in items:
        if minus and it.get('steps'):          # one real minus sign (U+2212) in every worked step: ' - ' and a sign in front of a digit
            it['steps'] = [_re.sub(r'(?<![\w\u2212])-(?=\d)', '\u2212', _re.sub(r'(?<=\s)-(?=\s)', '\u2212', t)) for t in it['steps']]
        if it.get('type') == 'selfcheck' and not it.get('marking_mode'):
            it['marking_mode'] = 'self'
        g = it.get('sol_fig')
        if g:
            def wrap(x, g=g):
                s = g(x)
                m = _re.search(r'viewBox="[-\d.]+ [-\d.]+ ([\d.]+) [\d.]+"', s)
                if not m:
                    return s
                need = round(12.0 / min(1.0, sol_px / float(m.group(1))), 1)
                return _re.sub(r'font-size="([\d.]+)"', lambda k: 'font-size="%g"' % max(float(k.group(1)), need), s)
            it['sol_fig'] = wrap
    return items
