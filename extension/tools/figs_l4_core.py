"""Level 4 figure plug-in: general tables, bar models, number lines and cell grids (used by several Level 4 units).

Types (all drawn with the project palette only, so figs.recolour() gives the black-and-white print edition; nothing relies on colour):
  l4_table  head [..], rows [[..]], widths (relative), cell_h, font, first_col_head (bool), blank_cells ([[r,c],..] drawn with a thick empty frame),
            hl_rows (rows drawn with a double border).  A cell that is None or '' is an empty cell for the child to fill in.
  l4_bars   bar model.  rows: [{label, offset?, segs:[{u, t?, k?}], brace?:{a,b,text,side?}, note?}], unit (drawing units per 1 u),
            seg kinds k: 'p' plain (white), 'q' unknown (dashed frame, "?" if no text), 'h' hatched (shaded part, no text), 's' soft.
            `cut` on a seg draws it with a dashed vertical cut line at its right edge.
  l4_numline min, max, minor, major, labels {value: text}, hide [values] (empty boxes under the line), marks [{v, text?, kind}] kind: dot | ring | box |
            arrow (label above with an arrow), jumps [[a,b,text]], shade [[a,b]], dec (decimals for auto labels), unit_text (suffix).
  l4_grid   rows, cols, cell (drawing units), text {"r,c": str}, shade [[r,c]], ring [[r,c]], cross [[r,c]], axis {kind:'v'|'h', at: cell index (half cells ok)},
            col_labels / row_labels (lists), dashed [[r,c]] (empty dashed cells for the child), thick (outer border width).
"""
import figs as F

NAVY, TEAL, RED, SKY, SOFT, YEL, GREY = F.NAVY, F.TEAL, F.RED, F.SKY, F.SOFT, F.YEL, F.GREY


def _t(x, y, txt, size=26, fill=NAVY, anchor='middle', weight=700):
    return F._t(x, y, txt, size, fill, anchor, weight)


def _esc(s):
    return str(s).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


# ------------------------------------------------------------------------------------------------ table
def l4_table(spec, w=None):
    head = spec.get('head')
    rows = spec['rows']
    ncol = len(head) if head else len(rows[0])
    wid = spec.get('widths') or [1] * ncol
    tot = float(sum(wid))
    TW = spec.get('W', 700)
    xs = [0]
    for k in wid:
        xs.append(xs[-1] + TW * k / tot)
    ch = spec.get('cell_h', 56)
    fs = spec.get('font', 28)
    nr = len(rows) + (1 if head else 0)
    H = nr * ch + 8
    P = []
    y = 4
    allrows = ([('H', head)] if head else []) + [('R', r) for r in rows]
    fch = spec.get('first_col_head', False)
    for ri, (kind, r) in enumerate(allrows):
        for ci, v in enumerate(r):
            x0, x1 = 4 + xs[ci], 4 + xs[ci + 1]
            fill = '#fff'
            if kind == 'H' or (fch and ci == 0):
                fill = SOFT
            P.append(f'<rect x="{x0:.1f}" y="{y}" width="{x1 - x0:.1f}" height="{ch}" fill="{fill}" stroke="{NAVY}" stroke-width="2.6"/>')
            if v not in (None, ''):
                P.append(_t(f'{(x0 + x1) / 2:.1f}', y + ch / 2 + fs * 0.35, _esc(v), fs, weight=800 if (kind == 'H' or (fch and ci == 0)) else 700))
        y += ch
    for rr in spec.get('hl_rows', []):
        yy = 4 + rr * ch + (ch if head else 0)
        P.append(f'<rect x="{4 + 5}" y="{yy + 5}" width="{TW - 10}" height="{ch - 10}" fill="none" stroke="{NAVY}" stroke-width="2"/>')
    return F._wrap(''.join(P), TW + 8, H, spec.get('label', 'table'), w or spec.get('width_mm', 150))


# ------------------------------------------------------------------------------------------------ bars
def l4_bars(spec, w=None):
    U = spec.get('unit', 60)
    RH = spec.get('row_h', 46)
    rows = spec['rows']
    lab_w = spec.get('label_w', max([len(r.get('label', '')) for r in rows] + [0]) * 15 + 26)
    fs = spec.get('font', 26)
    longest = 0
    for r in rows:
        longest = max(longest, r.get('offset', 0) + sum(s['u'] for s in r['segs']))
    note_w = max([len(r.get('note', '')) for r in rows] + [0]) * 14 + (18 if any(r.get('note') for r in rows) else 0)
    vb = spec.get('vbrace')
    if vb:
        note_w = max(note_w, 36 + len(vb['text']) * 15)
    W = lab_w + longest * U + note_w + 16
    top = 8
    gap = spec.get('gap', 20)
    braces_top = [bool(r.get('brace') and r['brace'].get('side', 'top') == 'top') for r in rows]
    y = top
    P = []
    ys = []
    for i, r in enumerate(rows):
        if braces_top[i]:
            y += 44
        ys.append(y)
        y += RH + gap
        if r.get('brace') and r['brace'].get('side') == 'bottom':
            y += 40
    H = y - gap + 14
    for i, r in enumerate(rows):
        y0 = ys[i]
        if r.get('label'):
            P.append(_t(lab_w - 12, y0 + RH / 2 + fs * 0.35, _esc(r['label']), fs, anchor='end', weight=800))
        x = lab_w + r.get('offset', 0) * U
        xmap = [x]
        for s in r['segs']:
            sw = s['u'] * U
            k = s.get('k', 'p')
            if k == 'q':
                P.append(f'<rect x="{x:.1f}" y="{y0}" width="{sw:.1f}" height="{RH}" fill="#fff" stroke="{NAVY}" stroke-width="3" stroke-dasharray="10 7"/>')
            elif k == 'h':
                P.append(f'<rect x="{x:.1f}" y="{y0}" width="{sw:.1f}" height="{RH}" fill="{YEL}" stroke="{NAVY}" stroke-width="3"/>')
            elif k == 's':
                P.append(f'<rect x="{x:.1f}" y="{y0}" width="{sw:.1f}" height="{RH}" fill="{SOFT}" stroke="{NAVY}" stroke-width="3"/>')
            else:
                P.append(f'<rect x="{x:.1f}" y="{y0}" width="{sw:.1f}" height="{RH}" fill="{SKY}" stroke="{NAVY}" stroke-width="3"/>')
            t = s.get('t', '?' if k == 'q' else '')
            if t != '':
                P.append(_t(f'{x + sw / 2:.1f}', y0 + RH / 2 + fs * 0.35, _esc(t), fs, weight=800))
            if s.get('cut'):
                P.append(f'<line x1="{x + sw:.1f}" y1="{y0 - 8}" x2="{x + sw:.1f}" y2="{y0 + RH + 8}" stroke="{NAVY}" stroke-width="3.5" stroke-dasharray="7 5"/>')
            x += sw
            xmap.append(x)
        b = r.get('brace')
        if b:
            a, e = xmap[b['a']], xmap[b['b']]
            if b.get('side', 'top') == 'top':
                yb = y0 - 8
                P.append(f'<path d="M{a:.1f},{yb} L{a:.1f},{yb - 10} L{e:.1f},{yb - 10} L{e:.1f},{yb}" fill="none" stroke="{NAVY}" stroke-width="3"/>')
                P.append(_t(f'{(a + e) / 2:.1f}', yb - 18, _esc(b['text']), fs, weight=800))
            else:
                yb = y0 + RH + 8
                P.append(f'<path d="M{a:.1f},{yb} L{a:.1f},{yb + 10} L{e:.1f},{yb + 10} L{e:.1f},{yb}" fill="none" stroke="{NAVY}" stroke-width="3"/>')
                P.append(_t(f'{(a + e) / 2:.1f}', yb + 40, _esc(b['text']), fs, weight=800))
        if r.get('note'):
            P.append(_t(f'{x + 14:.1f}', y0 + RH / 2 + fs * 0.35, _esc(r['note']), fs, anchor='start', weight=800))
    if vb:
        xr = lab_w + longest * U + 14
        ya, yz = ys[vb.get('a', 0)], ys[vb.get('b', len(rows) - 1)] + RH
        P.append(f'<path d="M{xr},{ya} L{xr + 12},{ya} L{xr + 12},{yz} L{xr},{yz}" fill="none" stroke="{NAVY}" stroke-width="3"/>')
        P.append(_t(f'{xr + 22:.1f}', (ya + yz) / 2 + fs * 0.35, _esc(vb['text']), fs, anchor='start', weight=800))
    return F._wrap(''.join(P), W, H, spec.get('label', 'bar model'), w or spec.get('width_mm', 150))


# ------------------------------------------------------------------------------------------------ number line
def _fmt(v, dec):
    return f'{v:.{dec}f}' if dec else f'{int(round(v))}'


def l4_numline(spec, w=None):
    lo, hi = spec['min'], spec['max']
    minor = spec.get('minor', 1)
    major = spec.get('major', minor)
    dec = spec.get('dec', 0)
    unit_text = spec.get('unit_text', '')
    labels = {float(k): v for k, v in spec.get('labels', {}).items()}
    hide = [float(v) for v in spec.get('hide', [])]
    marks = spec.get('marks', [])
    jumps = spec.get('jumps', [])
    shade = spec.get('shade', [])
    W = spec.get('W', 760)
    pad = 56
    X = lambda v: pad + (v - lo) / (hi - lo) * (W - 2 * pad)
    top = 20
    if jumps:
        top += 90
    if any(m.get('kind') in ('arrow', 'box') for m in marks):
        top += 50
    base = top + 30
    fs = spec.get('font', 28)
    P = []
    for a, b in shade:
        P.append(f'<rect x="{X(a):.1f}" y="{base - 9}" width="{X(b) - X(a):.1f}" height="18" fill="{YEL}" stroke="{NAVY}" stroke-width="2.4"/>')
    P.append(f'<line x1="{pad - 22}" y1="{base}" x2="{W - pad + 22}" y2="{base}" stroke="{NAVY}" stroke-width="4.5" stroke-linecap="round"/>')
    n = int(round((hi - lo) / minor))
    eps = 1e-9
    for i in range(n + 1):
        v = lo + i * minor
        is_major = abs(round((v - lo) / major) * major - (v - lo)) < eps
        x = X(v)
        P.append(f'<line x1="{x:.1f}" y1="{base - (17 if is_major else 10)}" x2="{x:.1f}" y2="{base + (17 if is_major else 10)}" stroke="{NAVY}" stroke-width="{4 if is_major else 2.6}"/>')
        key = min(list(labels) + [1e18], key=lambda q: abs(q - v))
        hidden = any(abs(h - v) < eps for h in hide)
        if hidden:
            P.append(f'<rect x="{x - 36:.1f}" y="{base + 26}" width="72" height="50" rx="6" fill="#fff" stroke="{NAVY}" stroke-width="3.2"/>')
        elif abs(key - v) < eps:
            P.append(_t(f'{x:.1f}', base + 62, _esc(labels[key]), fs))
        elif is_major and not spec.get('labels_only'):
            P.append(_t(f'{x:.1f}', base + 62, _fmt(v, dec) + unit_text, fs))
    for m in marks:
        x = X(m['v'])
        kind = m.get('kind', 'dot')
        if kind == 'dot':
            P.append(f'<circle cx="{x:.1f}" cy="{base}" r="11" fill="{NAVY}"/>')
            if m.get('text'):
                P.append(_t(f'{x:.1f}', base - 24, _esc(m['text']), fs, weight=800))
        elif kind == 'ring':
            P.append(f'<circle cx="{x:.1f}" cy="{base}" r="11" fill="#fff" stroke="{NAVY}" stroke-width="4"/>')
            if m.get('text'):
                P.append(_t(f'{x:.1f}', base - 24, _esc(m['text']), fs, weight=800))
        else:   # arrow or box: label above with an arrow pointing down at the place
            yb = base - 112
            if kind == 'box':
                P.append(f'<rect x="{x - 46:.1f}" y="{yb}" width="92" height="50" rx="6" fill="#fff" stroke="{NAVY}" stroke-width="3.2"/>')
            else:
                P.append(_t(f'{x:.1f}', yb + 40, _esc(m.get('text', '')), fs + 4, weight=800))
            P.append(f'<line x1="{x:.1f}" y1="{yb + 54}" x2="{x:.1f}" y2="{base - 16}" stroke="{NAVY}" stroke-width="3.4"/>')
            P.append(f'<polygon points="{x:.1f},{base - 10} {x - 9:.1f},{base - 28} {x + 9:.1f},{base - 28}" fill="{NAVY}"/>')
    for a, b, text in jumps:
        xa, xb = X(a), X(b)
        mid = (xa + xb) / 2
        hg = 52
        P.append(f'<path d="M{xa:.1f},{base - 20} Q{mid:.1f},{base - 20 - 2 * hg} {xb:.1f},{base - 26}" fill="none" stroke="{NAVY}" stroke-width="4" stroke-linecap="round"/>')
        P.append(f'<polygon points="{xb:.1f},{base - 18} {xb - 11:.1f},{base - 36} {xb + 11:.1f},{base - 34}" fill="{NAVY}"/>')
        P.append(_t(f'{mid:.1f}', base - 20 - hg - 12, _esc(text), fs, weight=800))
    H = base + 96
    return F._wrap(''.join(P), W, H, spec.get('label', 'number line'), w or spec.get('width_mm', 160))


# ------------------------------------------------------------------------------------------------ grid
def l4_grid(spec, w=None):
    R, C = spec['rows'], spec['cols']
    cs = spec.get('cell', 56)
    text = spec.get('text', {})
    shade = {tuple(x) for x in spec.get('shade', [])}
    ring = {tuple(x) for x in spec.get('ring', [])}
    cross = {tuple(x) for x in spec.get('cross', [])}
    dashed = {tuple(x) for x in spec.get('dashed', [])}
    fs = spec.get('font', 28)
    left = 46 if spec.get('row_labels') else 6
    top = 40 if spec.get('col_labels') else 6
    W = left + C * cs + 10 + (spec.get('extra_w', 0))
    H = top + R * cs + 10
    P = []
    for r in range(R):
        for c in range(C):
            x, y = left + c * cs, top + r * cs
            if (r, c) in dashed:
                P.append(f'<rect x="{x}" y="{y}" width="{cs}" height="{cs}" fill="#fff" stroke="{NAVY}" stroke-width="2.6" stroke-dasharray="8 6"/>')
                continue
            fill = YEL if (r, c) in shade else '#fff'
            P.append(f'<rect x="{x}" y="{y}" width="{cs}" height="{cs}" fill="{fill}" stroke="{NAVY}" stroke-width="{spec.get("line", 2.2)}"/>')
            t = text.get(f'{r},{c}')
            if t not in (None, ''):
                if (r, c) in shade and spec.get('plate', True):
                    P.append(f'<rect x="{x + cs * 0.12:.1f}" y="{y + cs * 0.2:.1f}" width="{cs * 0.76:.1f}" height="{cs * 0.6:.1f}" rx="6" fill="#fff"/>')
                P.append(_t(f'{x + cs / 2:.1f}', y + cs / 2 + fs * 0.35, _esc(t), fs))
            if (r, c) in ring:
                P.append(f'<circle cx="{x + cs / 2:.1f}" cy="{y + cs / 2:.1f}" r="{cs * 0.44:.1f}" fill="none" stroke="{NAVY}" stroke-width="4"/>')
            if (r, c) in cross:
                P.append(f'<path d="M{x + 8},{y + 8} L{x + cs - 8},{y + cs - 8} M{x + cs - 8},{y + 8} L{x + 8},{y + cs - 8}" stroke="{NAVY}" stroke-width="3.6" stroke-linecap="round"/>')
    P.append(f'<rect x="{left}" y="{top}" width="{C * cs}" height="{R * cs}" fill="none" stroke="{NAVY}" stroke-width="{spec.get("thick", 4)}"/>')
    for i, t in enumerate(spec.get('col_labels', [])):
        P.append(_t(left + i * cs + cs / 2, top - 10, _esc(t), 26))
    for i, t in enumerate(spec.get('row_labels', [])):
        P.append(_t(left - 10, top + i * cs + cs / 2 + 9, _esc(t), 26, anchor='end'))
    axes = list(spec.get('axes', []))
    if spec.get('axis'):
        axes.append(spec['axis'])
    for ax in axes:
        if ax['kind'] == 'v':
            x = left + ax['at'] * cs
            P.append(f'<line x1="{x}" y1="{top - 8}" x2="{x}" y2="{top + R * cs + 8}" stroke="{NAVY}" stroke-width="5" stroke-dasharray="14 8"/>')
        elif ax['kind'] == 'd':
            P.append(f'<line x1="{left - 8}" y1="{top - 8}" x2="{left + C * cs + 8}" y2="{top + R * cs + 8}" stroke="{NAVY}" stroke-width="5" stroke-dasharray="14 8"/>')
        else:
            y = top + ax['at'] * cs
            P.append(f'<line x1="{left - 8}" y1="{y}" x2="{left + C * cs + 8}" y2="{y}" stroke="{NAVY}" stroke-width="5" stroke-dasharray="14 8"/>')
    return F._wrap(''.join(P), W, H, spec.get('label', 'grid'), w or spec.get('width_mm', 100))


# ------------------------------------------------------------------------------------------------ flow
def l4_flow(spec, w=None):
    """A chain of boxes joined by arrows: items [value | None (empty box)], ops [label above each arrow], back [labels of the undo arrows drawn
    underneath, right to left, dashed] (back is drawn only when given)."""
    items, ops = spec['items'], spec['ops']
    n = len(items)
    BW, BH, GAP = 120, 70, 120
    W = 20 + n * BW + (n - 1) * GAP + 20
    top = 56
    P = []
    back = spec.get('back')
    xs = [20 + i * (BW + GAP) for i in range(n)]
    for i, v in enumerate(items):
        dash = ' stroke-dasharray="9 6"' if v is None else ''
        P.append(f'<rect x="{xs[i]}" y="{top}" width="{BW}" height="{BH}" rx="10" fill="#fff" stroke="{NAVY}" stroke-width="3.4"{dash}/>')
        if v is not None:
            P.append(_t(xs[i] + BW / 2, top + BH / 2 + 11, _esc(v), 34, weight=800))
    for i, o in enumerate(ops):
        a, b = xs[i] + BW + 6, xs[i + 1] - 8
        y = top + BH / 2
        P.append(f'<line x1="{a}" y1="{y}" x2="{b - 6}" y2="{y}" stroke="{NAVY}" stroke-width="4"/>')
        P.append(f'<polygon points="{b},{y} {b - 18},{y - 11} {b - 18},{y + 11}" fill="{NAVY}"/>')
        P.append(_t((a + b) / 2, top + 16, _esc(o), 30, weight=800))
    H = top + BH + 20
    if back:
        yb = top + BH + 24
        for i, o in enumerate(back):       # back[i] undoes ops[len-1-i]; arrows run right to left
            j = n - 1 - i
            a, b = xs[j] + BW / 2, xs[j - 1] + BW / 2
            P.append(f'<path d="M{a},{yb} Q{(a + b) / 2},{yb + 60} {b + 6},{yb + 6}" fill="none" stroke="{NAVY}" stroke-width="3.6" stroke-dasharray="9 6"/>')
            P.append(f'<polygon points="{b},{yb} {b + 17},{yb + 20} {b + 22},{yb - 2}" fill="{NAVY}"/>')
            P.append(_t((a + b) / 2, yb + 62, _esc(o), 28, weight=800))
        H = yb + 90
    return F._wrap(''.join(P), W, H, spec.get('label', 'number machine'), w or spec.get('width_mm', 150))


FIGS = {'l4_flow': l4_flow, 'l4_table': l4_table, 'l4_bars': l4_bars, 'l4_numline': l4_numline, 'l4_grid': l4_grid}
