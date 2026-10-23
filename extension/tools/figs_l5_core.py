"""Figure types for the Level 5 Extension Workbook (core set).  Every type name starts with l5_ so it cannot clash with another level.

  l5_cards   a row of digit (or symbol) cards: {items:[...], width_mm}; None = blank card the child fills in
  l5_table   a table: {cols:[...], rows:[[...]], widths?:[rel], first_bold?, width_mm, rowh?}; None = empty cell
  l5_numline number line: {ticks:[{v, lab?, box?}], min, max, marks:[{v, text, below?}], width_mm}
  l5_bars    bar models: {rows:[{label, cells:[{n, text?, shade?, dash?}], brace?:{a, b, text, below?}, note?}], unit?, width_mm}
  l5_grid100 hundred grid with shaded squares: {shaded:[indexes or count], width_mm}
Palette NAVY / TEAL / YEL / SKY / SOFT only, so figs.recolour() gives the print version (YEL becomes hatching, SKY and SOFT white).
Nothing depends on colour: shaded parts are also labelled in the text.  1 drawing unit = 0.25 mm at the default width (4 units per mm).
"""
import figs as F

NAVY, TEAL, YEL, SKY, SOFT = F.NAVY, F.TEAL, F.YEL, F.SKY, F.SOFT
SW = 2.8
U = 4.0   # drawing units per mm


def T(x, y, txt, size=22, fill=NAVY, anchor='middle', weight=700):
    return F._t(round(x, 1), round(y, 1), txt, size, fill, anchor, weight)


def esc(s):
    return str(s).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def _w(spec, w, default):
    return w or spec.get('width_mm') or default


# ---------------------------------------------------------------------------------------------- cards
def cards(spec, w=None):
    items = spec['items']
    cw, ch, gap = spec.get('cw', 56), 68, spec.get('gap', 14)
    P = []
    for i, d in enumerate(items):
        x = 6 + i * (cw + gap)
        if d is None:
            P.append(f'<rect x="{x}" y="6" width="{cw}" height="{ch}" rx="9" fill="#fff" stroke="{NAVY}" stroke-width="{SW}" stroke-dasharray="9 6"/>')
        else:
            P.append(f'<rect x="{x}" y="6" width="{cw}" height="{ch}" rx="9" fill="{YEL}" stroke="{NAVY}" stroke-width="{SW}"/>')
            P.append(T(x + cw / 2, 6 + ch / 2 + 13, d, 38))
    Wd = 12 + len(items) * (cw + gap) - gap
    H = ch + 12
    if spec.get('caption'):
        P.append(T(Wd / 2, H + 26, spec['caption'], 22, weight=700)); H += 36
    return F._wrap(''.join(P), Wd, H, spec.get('alt', 'cards'), _w(spec, w, round(Wd / U)))


# ---------------------------------------------------------------------------------------------- table
def table(spec, w=None):
    cols, rows = spec['cols'], spec['rows']
    n = len(cols)
    size = spec.get('size', 22)
    cw = []
    for j in range(n):
        longest = max([len(str(cols[j]))] + [len(str(r[j])) for r in rows if r[j] is not None])
        cw.append(max(spec.get('minw', 74), longest * size * 0.60 + 30))
    if spec.get('widths'):
        k = sum(cw) / sum(spec['widths'])
        cw = [x * k for x in spec['widths']]
    Wd = sum(cw) + 8
    tw = _w(spec, w, None)
    if tw:   # stretch columns to fill the requested width
        target = tw * U - 8
        if sum(cw) < target and spec.get('fill', False):
            k = target / sum(cw); cw = [x * k for x in cw]; Wd = sum(cw) + 8
    rh = spec.get('rowh', 46)
    P = []
    y = 4
    x = 4
    for j, c in enumerate(cols):
        P.append(f'<rect x="{x:.1f}" y="{y}" width="{cw[j]:.1f}" height="{rh}" fill="{SOFT}" stroke="{NAVY}" stroke-width="{SW}"/>')
        P.append(T(x + cw[j] / 2, y + rh / 2 + size * 0.35, esc(c), size, weight=800))
        x += cw[j]
    for r in rows:
        y += rh; x = 4
        for j, v in enumerate(r):
            P.append(f'<rect x="{x:.1f}" y="{y}" width="{cw[j]:.1f}" height="{rh}" fill="#fff" stroke="{NAVY}" stroke-width="{SW}"/>')
            if v is not None:
                P.append(T(x + cw[j] / 2, y + rh / 2 + size * 0.35, esc(v), size, weight=800 if (j == 0 and spec.get('first_bold')) else 700))
            x += cw[j]
    H = y + rh + 8
    if spec.get('caption'):
        P.append(T(Wd / 2, H + 20, esc(spec['caption']), 20, weight=700)); H += 30
    return F._wrap(''.join(P), round(Wd, 1), H, spec.get('alt', 'table'), tw or round(Wd / U, 1))


# ---------------------------------------------------------------------------------------------- number line
def numline(spec, w=None):
    lo, hi = spec['min'], spec['max']
    Wd = 600
    x0, x1 = 40, Wd - 40
    y = spec.get('y', 70)
    sx = lambda v: x0 + (v - lo) / (hi - lo) * (x1 - x0)
    P = [f'<line x1="{x0 - 22}" y1="{y}" x2="{x1 + 22}" y2="{y}" stroke="{NAVY}" stroke-width="{SW + .4}"/>',
         f'<polygon points="{x1 + 30},{y} {x1 + 16},{y - 8} {x1 + 16},{y + 8}" fill="{NAVY}"/>',
         f'<polygon points="{x0 - 30},{y} {x0 - 16},{y - 8} {x0 - 16},{y + 8}" fill="{NAVY}"/>']
    for t in spec['ticks']:
        x = sx(t['v'])
        h = 15 if t.get('minor') else 22
        P.append(f'<line x1="{x:.1f}" y1="{y - h}" x2="{x:.1f}" y2="{y + h}" stroke="{NAVY}" stroke-width="{SW}"/>')
        if t.get('box'):
            P.append(f'<rect x="{x - 33:.1f}" y="{y + 28}" width="66" height="38" rx="6" fill="#fff" stroke="{NAVY}" stroke-width="{SW}"/>')
        elif t.get('lab') is not None:
            P.append(T(x, y + 56, esc(t['lab']), t.get('size', 22)))
    for m in spec.get('marks', []):
        x = sx(m['v'])
        up = not m.get('below')
        P.append(f'<circle cx="{x:.1f}" cy="{y}" r="9" fill="{YEL}" stroke="{NAVY}" stroke-width="{SW}"/>')
        P.append(T(x, y - 22 if up else y + 90, esc(m['text']), 24, weight=800))
    H = spec.get('h', 128)
    return F._wrap(''.join(P), Wd, H, spec.get('alt', 'number line'), _w(spec, w, 150))


# ---------------------------------------------------------------------------------------------- bar models
def _brace(x0, x1, y, down, text, size=22):
    d = 10 if not down else -10
    mid = (x0 + x1) / 2
    p = (f'M{x0:.1f},{y} q0,{-d:.0f} 10,{-d:.0f} L{mid - 10:.1f},{y - d:.0f} q10,0 10,{-d:.0f} q0,{d:.0f} 10,{d:.0f} L{x1 - 10:.1f},{y - d:.0f} q10,0 10,{d:.0f}')
    # simple bracket: two end ticks and a bar, plus a little centre tick
    ty = y - d if not down else y - d
    out = (f'<path d="M{x0:.1f},{y} L{x0:.1f},{y - d * 1.2:.1f} L{x1:.1f},{y - d * 1.2:.1f} L{x1:.1f},{y}" fill="none" stroke="{NAVY}" stroke-width="{SW}"/>'
           f'<line x1="{mid:.1f}" y1="{y - d * 1.2:.1f}" x2="{mid:.1f}" y2="{y - d * 2.2:.1f}" stroke="{NAVY}" stroke-width="{SW}"/>')
    ty = y - d * 2.2 - (6 if not down else -size * 0.9)
    out += T(mid, ty, esc(text), size, weight=800)
    return out


def bars(spec, w=None):
    rows = spec['rows']
    tw = _w(spec, w, 150)
    Wd = tw * U
    lab_w = max([len(r.get('label', '')) for r in rows] + [0]) * 14 + (22 if any(r.get('label') for r in rows) else 0)
    tot = max(sum(c['n'] for c in r['cells']) + r.get('start', 0) for r in rows)
    note_w = max([len(r.get('note', '')) for r in rows] + [0]) * 13
    unit = spec.get('unit') or (Wd - lab_w - note_w - 16) / tot
    BH = spec.get('bh', 50)
    gapy = spec.get('gap', 22)
    P = []
    y = 8
    for r in rows:
        top_brace = r.get('brace') and not r['brace'].get('below')
        if top_brace:
            y += 52
        x = 8 + lab_w + r.get('start', 0) * unit
        if r.get('label'):
            P.append(T(8 + lab_w - 12, y + BH / 2 + 8, esc(r['label']), 22, anchor='end', weight=800))
        x_start = x
        for c in r['cells']:
            cwid = c['n'] * unit
            fill = YEL if c.get('shade') else '#fff'
            dash = f' stroke-dasharray="9 6"' if c.get('dash') else ''
            P.append(f'<rect x="{x:.1f}" y="{y}" width="{cwid:.1f}" height="{BH}" fill="{fill}" stroke="{NAVY}" stroke-width="{SW}"{dash}/>')
            if c.get('text') is not None:
                tcol = NAVY
                P.append(T(x + cwid / 2, y + BH / 2 + 8, esc(c['text']), c.get('size', 22), tcol, weight=800))
            x += cwid
        if r.get('note'):
            P.append(T(x + 12, y + BH / 2 + 8, esc(r['note']), 22, anchor='start', weight=800))
        b = r.get('brace')
        if b:
            bx0, bx1 = x_start + b['a'] * unit, x_start + b['b'] * unit
            if b.get('below'):
                P.append(_brace(bx0, bx1, y + BH + 4, True, b['text']))
                y += 52
            else:
                P.append(_brace(bx0, bx1, y - 4, False, b['text']))
        y += BH + gapy
    H = y - gapy + 14
    return F._wrap(''.join(P), round(Wd, 1), round(H, 1), spec.get('alt', 'bar model'), tw)


# ---------------------------------------------------------------------------------------------- hundred grid
def grid100(spec, w=None):
    sh = spec['shaded']
    sh = set(range(sh)) if isinstance(sh, int) else set(sh)
    c = 34
    P = []
    for i in range(100):
        r, k = divmod(i, 10)
        fill = YEL if i in sh else '#fff'
        P.append(f'<rect x="{4 + k * c}" y="{4 + r * c}" width="{c}" height="{c}" fill="{fill}" stroke="{NAVY}" stroke-width="2"/>')
    P.append(f'<rect x="4" y="4" width="{10 * c}" height="{10 * c}" fill="none" stroke="{NAVY}" stroke-width="{SW + 1}"/>')
    return F._wrap(''.join(P), 10 * c + 8, 10 * c + 8, spec.get('alt', 'hundred grid'), _w(spec, w, 80))


FIGS = {'l5_cards': cards, 'l5_table': table, 'l5_numline': numline, 'l5_bars': bars, 'l5_grid100': grid100}
