"""Level 3 figure types shared by all units (every type is prefixed l3_ so that it cannot clash with another level's plugin).

Loaded automatically by figs.render() (FIGS table).  All text is >= 26 drawing units at 0.2 mm per unit (about 15 pt) unless a
spec says otherwise; objects (cells, bricks, cards) are >= 44 units (about 9 mm).  Palette: NAVY / TEAL / RED / SKY / SOFT / YEL only,
so figs.recolour() makes the black-and-white print version (SKY and SOFT become white, YEL becomes hatching: never put text on YEL).

  l3_grid     rows of cells (number/text, None = empty box to fill, dict {t, fill, mark, bold}); heads, thick outline
  l3_cards    a row of digit cards
  l3_nline    number line with ticks, labels and marks (arrow / dot / cross)
  l3_bars     bar model: rows of segments (relative widths), braces with text, "?" segments
  l3_array    rows x columns of dots or squares, optional dashed split line
  l3_vsum     a column sum written upright (Th H T O), boxes or letters in any place
  l3_pyramid  number pyramid (bricks), None = empty brick
"""
import figs as F

NAVY, TEAL, RED, SKY, SOFT, YEL = F.NAVY, F.TEAL, F.RED, F.SKY, F.SOFT, F.YEL
SW = 3.0
K = 0.2   # mm per drawing unit


def T(x, y, txt, size=30, fill=NAVY, anchor='middle', weight=800):
    return F._t(x, y, txt, size, fill, anchor, weight)


def wrap(P, W, H, label, w=None):
    return F._wrap(''.join(P), W, H, label, w or round(W * K, 1))


def esc(s):
    return str(s).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


FILL = {'soft': SOFT, 'sky': SKY, 'none': '#fff', 'hatch': YEL}


# ------------------------------------------------------------------------------------------------ grid
def tick_path(x, y, s):
    return f'<path d="M{x + s * .22},{y + s * .55} L{x + s * .42},{y + s * .78} L{x + s * .8},{y + s * .24}" fill="none" stroke="{NAVY}" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>'


def cross_path(x, y, s):
    return f'<path d="M{x + s * .26},{y + s * .26} L{x + s * .74},{y + s * .74} M{x + s * .74},{y + s * .26} L{x + s * .26},{y + s * .74}" fill="none" stroke="{NAVY}" stroke-width="5.5" stroke-linecap="round"/>'


def grid(spec, w=None):
    """rows: list of lists.  A cell is None (empty box), a number/string, or {t, fill: soft|sky|none, mark: y|n, bold, size, dash}.
    cw, ch: cell size; head_row / head_col: first row / column drawn in the heading style (SOFT fill, bold);
    col_w: list of widths; thick: list of [r0, c0, r1, c1] boxes drawn with a thick outline; corner: top-left cell has no frame."""
    rows = spec['rows']
    nr, nc = len(rows), max(len(r) for r in rows)
    cw0, ch = spec.get('cw', 64), spec.get('ch', 56)
    cws = spec.get('col_w') or [cw0] * nc
    fs = spec.get('fs', 30)
    xs = [6]
    for c in cws:
        xs.append(xs[-1] + c)
    P = []
    for r, row in enumerate(rows):
        for c in range(nc):
            v = row[c] if c < len(row) else ''
            x, y = xs[c], 6 + r * ch
            d = v if isinstance(v, dict) else {'t': v}
            head = (spec.get('head_row') and r == 0) or (spec.get('head_col') and c == 0)
            fill = FILL[d.get('fill', 'soft' if head else 'none')]
            if spec.get('corner') and r == 0 and c == 0:
                continue
            dash = ' stroke-dasharray="8 6"' if d.get('dash') else ''
            P.append(f'<rect x="{x}" y="{y}" width="{cws[c]}" height="{ch}" fill="{fill}" stroke="{NAVY}" stroke-width="{SW}"{dash}/>')
            t = d.get('t')
            if t is not None and t != '':
                P.append(T(x + cws[c] / 2, y + ch / 2 + d.get('size', fs) * .36, esc(t), d.get('size', fs), weight=800 if (head or d.get('bold')) else 700))
            if d.get('mark') == 'y':
                P.append(tick_path(x + (cws[c] - ch) / 2, y, ch))
            elif d.get('mark') == 'n':
                P.append(cross_path(x + (cws[c] - ch) / 2, y, ch))
    for r0, c0, r1, c1 in spec.get('thick', []):
        P.append(f'<rect x="{xs[c0]}" y="{6 + r0 * ch}" width="{xs[c1 + 1] - xs[c0]}" height="{(r1 - r0 + 1) * ch}" fill="none" stroke="{NAVY}" stroke-width="7"/>')
    W = xs[-1] + 6
    H = 12 + nr * ch
    if spec.get('caption'):
        P.append(T(W / 2, H + 34, esc(spec['caption']), 28, weight=700))
        H += 44
    return wrap(P, W, H, spec.get('label', 'table of numbers'), w)


# ------------------------------------------------------------------------------------------------ cards
def cards(spec, w=None):
    items = spec['items']
    cw, chh, gap = spec.get('cw', 78), 96, 18
    P = []
    for i, d in enumerate(items):
        x = 6 + i * (cw + gap)
        P.append(f'<rect x="{x}" y="6" width="{cw}" height="{chh}" rx="12" fill="{SOFT}" stroke="{NAVY}" stroke-width="4"/>')
        P.append(T(x + cw / 2, 6 + chh / 2 + 18, esc(d), 54))
    W = 12 + len(items) * (cw + gap) - gap
    return wrap(P, W, chh + 12, 'digit cards ' + ' '.join(str(i) for i in items), w)


# ------------------------------------------------------------------------------------------------ number line
def nline(spec, w=None):
    """lo, hi, step (tick spacing), lab (label every `lab`), marks: [{at, text, kind: arrow|dot|cross|ring}], W (drawing width)."""
    lo, hi, step, lab = spec['lo'], spec['hi'], spec['step'], spec.get('lab', spec['step'])
    X0, X1 = 50, spec.get('W', 700) - 50
    y = 120
    def px(v):
        return X0 + (v - lo) / (hi - lo) * (X1 - X0)
    P = [f'<line x1="{X0 - 24}" y1="{y}" x2="{X1 + 24}" y2="{y}" stroke="{NAVY}" stroke-width="4"/>']
    v = lo
    while v <= hi + 1e-9:
        big = (v - lo) % lab == 0
        h = 22 if big else 13
        P.append(f'<line x1="{px(v):.1f}" y1="{y - h}" x2="{px(v):.1f}" y2="{y + h}" stroke="{NAVY}" stroke-width="{4 if big else 3}"/>')
        if big:
            P.append(T(px(v), y + 58, f'{v:g}', spec.get('fs', 28), weight=700))
        v += step
    for m in spec.get('marks', []):
        x = px(m['at']); k = m.get('kind', 'arrow')
        if k == 'arrow':
            P.append(f'<path d="M{x:.1f},{y - 8} L{x - 17:.1f},{y - 48} L{x + 17:.1f},{y - 48}Z" fill="{NAVY}" stroke="{NAVY}" stroke-width="2"/>')
            if m.get('text'):
                P.append(T(x, y - 58, esc(m['text']), 32))
        elif k == 'dot':
            P.append(f'<circle cx="{x:.1f}" cy="{y}" r="11" fill="{NAVY}"/>')
            if m.get('text'):
                P.append(T(x, y - 28, esc(m['text']), 32))
        elif k == 'ring':
            P.append(f'<circle cx="{x:.1f}" cy="{y}" r="13" fill="#fff" stroke="{NAVY}" stroke-width="4"/>')
            if m.get('text'):
                P.append(T(x, y - 28, esc(m['text']), 32))
        else:
            P.append(cross_path(x - 20, y - 20, 40))
            if m.get('text'):
                P.append(T(x, y - 34, esc(m['text']), 32))
    return wrap(P, X1 + 74, y + 78, 'number line', w)


# ------------------------------------------------------------------------------------------------ bar model
def bars(spec, w=None):
    """rows: [{label, segs: [{w, t, style: fill|sky|plain|blank|q}], braces: [{a, b, t, side: top|bottom}]}]
    seg w is a relative width (1 = unit); u = drawing units per width unit.  style blank = dashed empty box; q = '?' in a dashed box;
    ghost = dashed box with its text (the missing part of a comparison).  A row may have a `note` written after the bar."""
    rows = spec['rows']
    u = spec.get('u', 60)
    LAB = spec.get('lab', 120)
    BH = spec.get('bh', 56)
    P = []
    y = 8
    maxx = 0
    for row in rows:
        tops = [b for b in row.get('braces', []) if b.get('side', 'top') == 'top']
        bots = [b for b in row.get('braces', []) if b.get('side') == 'bottom']
        if tops:
            y += 62
        x = LAB
        xs = []
        for s in row['segs']:
            xs.append(x)
            wd = s['w'] * u
            st = s.get('style', 'plain')
            fill = {'fill': SOFT, 'sky': SKY}.get(st, '#fff')
            dash = ' stroke-dasharray="9 6"' if st in ('blank', 'q', 'ghost') else ''
            P.append(f'<rect x="{x}" y="{y}" width="{wd}" height="{BH}" fill="{fill}" stroke="{NAVY}" stroke-width="{SW}"{dash}/>')
            t = '?' if st == 'q' else s.get('t', '')
            if t != '':
                P.append(T(x + wd / 2, y + BH / 2 + 10, esc(t), s.get('size', 28)))
            x += wd
        xs.append(x)
        if row.get('note'):
            P.append(T(x + 14, y + BH / 2 + 10, esc(row['note']), 28, anchor='start'))
            x += 14 + 17 * len(str(row['note']))
        maxx = max(maxx, x)
        if row.get('label'):
            P.append(T(LAB - 12, y + BH / 2 + 10, esc(row['label']), 28, anchor='end'))
        for b in tops:
            a, c = xs[b['a']], xs[b['b'] + 1]
            P.append(f'<path d="M{a + 2},{y - 8} q0,-16 16,-16 H{(a + c) / 2 - 12} q10,0 12,-12 q2,12 12,12 H{c - 18} q16,0 16,16" fill="none" stroke="{NAVY}" stroke-width="3"/>')
            P.append(T((a + c) / 2, y - 46, esc(b['t']), 28))
        y += BH
        for b in bots:
            a, c = xs[b['a']], xs[b['b'] + 1]
            P.append(f'<path d="M{a + 2},{y + 8} q0,16 16,16 H{(a + c) / 2 - 12} q10,0 12,12 q2,-12 12,-12 H{c - 18} q16,0 16,-16" fill="none" stroke="{NAVY}" stroke-width="3"/>')
            P.append(T((a + c) / 2, y + 66, esc(b['t']), 28))
            y += 70
        y += 22
    return wrap(P, maxx + 16, y, 'bar model', w)


# ------------------------------------------------------------------------------------------------ array
def array(spec, w=None):
    """rows x cols of dots (shape dot) or squares; split_row / split_col draw a dashed line after that many rows / columns;
    hide: number of items missing at the end of the last row (drawn as empty rings)."""
    nr, nc = spec['rows'], spec['cols']
    S = spec.get('s', 48)
    shape = spec.get('shape', 'dot')
    P = []
    for r in range(nr):
        for c in range(nc):
            cx, cy = 14 + S / 2 + c * S + (10 if spec.get('split_col') and c >= spec['split_col'] else 0), 14 + S / 2 + r * S + (10 if spec.get('split_row') and r >= spec['split_row'] else 0)
            ghost = spec.get('ghost') and r * nc + c >= nr * nc - spec['ghost']
            if shape == 'dot':
                P.append(f'<circle cx="{cx}" cy="{cy}" r="{S * .36:.1f}" fill="{"#fff" if ghost else NAVY}" stroke="{NAVY}" stroke-width="3"{" stroke-dasharray=\"6 5\"" if ghost else ""}/>')
            else:
                P.append(f'<rect x="{cx - S * .42}" y="{cy - S * .42}" width="{S * .84}" height="{S * .84}" fill="{"#fff" if ghost else SOFT}" stroke="{NAVY}" stroke-width="3"/>')
    W = 28 + nc * S + (10 if spec.get('split_col') else 0)
    H = 28 + nr * S + (10 if spec.get('split_row') else 0)
    if spec.get('split_row'):
        y = 14 + spec['split_row'] * S + 5
        P.append(f'<line x1="2" y1="{y}" x2="{W - 2}" y2="{y}" stroke="{NAVY}" stroke-width="4" stroke-dasharray="12 7"/>')
    if spec.get('split_col'):
        x = 14 + spec['split_col'] * S + 5
        P.append(f'<line x1="{x}" y1="2" x2="{x}" y2="{H - 2}" stroke="{NAVY}" stroke-width="4" stroke-dasharray="12 7"/>')
    if spec.get('caption'):
        P.append(T(W / 2, H + 34, esc(spec['caption']), 28, weight=700)); H += 44
    return wrap(P, W, H, f'array of {nr} rows of {nc}', w)


# ------------------------------------------------------------------------------------------------ vertical sum
def vsum(spec, w=None):
    """lines: list of rows; each row is a list of cells (digit, letter, None = empty box) from the left; `sign` is drawn left of the row
    ('+', '-', or '').  A rule is drawn after the row whose `rule` is true.  heads: e.g. ['Th','H','T','O'] drawn above the first row.
    spec: {"heads": [...], "lines": [{"sign": "", "cells": [..]}, {"sign": "+", "cells": [...], "rule": true}, {"sign": "", "cells": [...]}]}"""
    L = spec['lines']
    n = max(len(l['cells']) for l in L)
    cw, ch = spec.get('cw', 72), spec.get('ch', 68)
    X0 = 60
    P = []
    y = 6
    if spec.get('heads'):
        for c, h in enumerate(spec['heads']):
            P.append(T(X0 + c * cw + cw / 2, y + 30, esc(h), 28, weight=700))
        y += 40
    for l in L:
        cells = l['cells']
        off = n - len(cells)
        for c, v in enumerate(cells):
            x = X0 + (c + off) * cw
            if v is None:
                P.append(f'<rect x="{x + 4}" y="{y + 4}" width="{cw - 8}" height="{ch - 8}" rx="5" fill="#fff" stroke="{NAVY}" stroke-width="{SW}"/>')
            else:
                P.append(T(x + cw / 2, y + ch / 2 + 15, esc(v), 44))
        if l.get('sign'):
            P.append(T(X0 - 24, y + ch / 2 + 15, l['sign'], 44))
        y += ch
        if l.get('rule'):
            P.append(f'<line x1="{X0 - 40}" y1="{y + 3}" x2="{X0 + n * cw + 4}" y2="{y + 3}" stroke="{NAVY}" stroke-width="4"/>')
            y += 8
    return wrap(P, X0 + n * cw + 16, y + 6, 'column sum', w)


# ------------------------------------------------------------------------------------------------ pyramid
def pyramid(spec, w=None):
    """rows from the top brick down; each row is a list of values (None = empty brick; "@P" = empty brick with the letter P)."""
    rows = spec['rows']
    bw, bh = spec.get('bw', 132), spec.get('bh', 68)
    n = len(rows[-1])
    W = n * bw + 20
    P = []
    for r, row in enumerate(rows):
        k = len(row)
        x0 = 10 + (n - k) * bw / 2
        for c, v in enumerate(row):
            x, y = x0 + c * bw, 8 + r * bh
            blank = v is None or (isinstance(v, str) and v.startswith('@'))
            P.append(f'<rect x="{x}" y="{y}" width="{bw}" height="{bh}" fill="{"#fff" if blank else SOFT}" stroke="{NAVY}" stroke-width="{SW}"{" stroke-dasharray=\"8 6\"" if blank else ""}/>')
            if v is not None:
                P.append(T(x + bw / 2, y + bh / 2 + 11, esc(v[1:] if blank else v), 34))
    return wrap(P, W, 16 + len(rows) * bh, 'number pyramid', w)


FIGS = {'l3_grid': grid, 'l3_cards': cards, 'l3_nline': nline, 'l3_bars': bars, 'l3_array': array, 'l3_vsum': vsum, 'l3_pyramid': pyramid}
