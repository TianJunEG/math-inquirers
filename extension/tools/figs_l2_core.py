"""Figure types for the Level 2 extension workbook, core set (units 1 and 2 and generic helpers used by the later Level 2 plugins).

Plugged into figs.render() through the FIGS table.  All type names start with "l2_" so they never clash with other levels.
  l2_cards     a row of digit cards (a digit, or None = an empty dashed card)
  l2_blocks    base-ten pictures: groups of {flats, rods, ones}; a key line says what each piece is worth
  l2_chart     pieces cut from a 1000 chart: [{label, rows: [[cell, ...], ...]}], a cell is a number (printed), None (empty box to fill) or "" (not part of the piece)
  l2_nline     a number line with tick marks, a few printed labels and arrows (A, B) pointing at marks; the child reads them
  l2_table     a plain table: cols, rows (a cell is text, or None = empty box to fill), optional widths, bold first column
  l2_grid      a square grid of cells (magic squares): values, None = empty box, optional `hatch` cells and a `sums` caption
  l2_vsum      a vertical sum (column addition or subtraction) with some digits missing (shown as empty boxes)
Palette: NAVY / TEAL / SKY / SOFT / YEL only, so figs.recolour() gives the print version.  Objects are at least 8 mm on paper
(1 mm is about 5 drawing units when width_mm is left to the default).  Nothing depends on colour.
"""
import figs as F

NAVY, TEAL, RED, SKY, SOFT, YEL = F.NAVY, F.TEAL, F.RED, F.SKY, F.SOFT, F.YEL
SW = 3.0


def T(x, y, txt, size=34, fill=NAVY, anchor='middle', weight=700):
    return F._t(x, y, txt, size, fill, anchor, weight)


def box(x, y, w, h, fill='#fff', dash=False, sw=3.0, rx=8):
    d = ' stroke-dasharray="9 6"' if dash else ''
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{NAVY}" stroke-width="{sw}"{d}/>'


def line(x1, y1, x2, y2, sw=2.6, dash=None, col=NAVY):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{col}" stroke-width="{sw}"{d} stroke-linecap="round"/>'


def wrap(P, W, H, label, w, k=0.2):
    return F._wrap(''.join(P), W, H, label, w or round(W * k, 1))


# ------------------------------------------------------------------------------------------ l2_cards
def cards(spec, w=None):
    items = spec['items']
    cw, ch, gap = 80, 104, 26
    W = len(items) * cw + (len(items) - 1) * gap + 12
    P = []
    for i, d in enumerate(items):
        x = 6 + i * (cw + gap)
        if d is None:
            P.append(box(x, 6, cw, ch, dash=True, rx=12))
        else:
            P.append(box(x, 6, cw, ch, SOFT, rx=12, sw=3.4))
            P.append(T(x + cw / 2, 6 + ch / 2 + 20, d, 62, weight=700))
    return wrap(P, W, ch + 12, 'digit cards ' + ' '.join(str(d) for d in items if d is not None), w, 0.2)


# ------------------------------------------------------------------------------------------ l2_blocks
def _flat(x, y, s):
    P = [box(x, y, s, s, SKY, rx=3, sw=3)]
    for k in range(1, 10):
        P.append(line(x + k * s / 10, y, x + k * s / 10, y + s, 1.1))
        P.append(line(x, y + k * s / 10, x + s, y + k * s / 10, 1.1))
    return P


def _rod(x, y, w, h):
    P = [box(x, y, w, h, SKY, rx=3, sw=3)]
    for k in range(1, 10):
        P.append(line(x, y + k * h / 10, x + w, y + k * h / 10, 1.1))
    return P


def blocks(spec, w=None):
    """groups: [{label?, flats, rods, ones}].  Layout per group: flats in a row, rods in rows of `rods_per_row`, ones in rows of `ones_per_row`."""
    FS, RW, RH, OS, g = 120, 38, 120, 38, 14
    rpr = spec.get('rods_per_row', 5)
    opr = spec.get('ones_per_row', 3)
    gaps = 40
    P = []
    x0 = 6
    maxh = 0
    for gi, G in enumerate(spec['groups']):
        x = x0
        h = 0
        nf, nr, no = G.get('flats', 0), G.get('rods', 0), G.get('ones', 0)
        # flats stacked in 2 rows when many
        fcols = min(nf, spec.get('flats_per_row', 3)) if nf else 0
        for k in range(nf):
            r, c = divmod(k, fcols)
            P += _flat(x + c * (FS + g), 6 + r * (FS + g), FS)
        if nf:
            frows = (nf + fcols - 1) // fcols
            x += fcols * (FS + g) + 8
            h = max(h, frows * (FS + g) - g)
        if nr:
            rcols = min(nr, rpr)
            for k in range(nr):
                r, c = divmod(k, rcols)
                P += _rod(x + c * (RW + g), 6 + r * (RH + g), RW, RH)
            rrows = (nr + rcols - 1) // rcols
            x += rcols * (RW + g) + 8
            h = max(h, rrows * (RH + g) - g)
        if no:
            ocols = min(no, opr)
            for k in range(no):
                r, c = divmod(k, ocols)
                P.append(box(x + c * (OS + g), 6 + r * (OS + g), OS, OS, SKY, rx=3, sw=3))
            orows = (no + ocols - 1) // ocols
            x += ocols * (OS + g)
            h = max(h, orows * (OS + g) - g)
        if G.get('label'):
            P.append(T((x0 + x - g) / 2, 6 + h + 46, G['label'], 32))
            h += 52
        maxh = max(maxh, h)
        x0 = x + gaps
    W = x0 - gaps + 6
    H = maxh + 18
    if spec.get('key', True):
        ky = H + 34
        kx = 6
        P += _flat(kx, ky - 26, 40)
        P.append(T(kx + 50, ky + 8, '= 100', 30, anchor='start'))
        P += _rod(kx + 190, ky - 26, 16, 40)
        P.append(T(kx + 214, ky + 8, '= 10', 30, anchor='start'))
        P.append(box(kx + 340, ky - 26, 40, 40, SKY, rx=3, sw=3))
        P.append(T(kx + 390, ky + 8, '= 1', 30, anchor='start'))
        H = ky + 30
        W = max(W, 500)
    return wrap(P, W, H, 'base-ten blocks: flats (100), rods (10) and ones (1)', w, 0.2)


# ------------------------------------------------------------------------------------------ l2_chart
def chart(spec, w=None):
    cw, chh = 100, 62
    pieces = spec['pieces']
    P = []
    x0 = 6
    maxh = 0
    for pc in pieces:
        rows = pc['rows']
        ncol = max(len(r) for r in rows)
        top = 44 if pc.get('label') else 6
        if pc.get('label'):
            P.append(T(x0 + ncol * cw / 2, 32, pc['label'], 32))
        for r, row in enumerate(rows):
            for c, v in enumerate(row):
                if v == '' or v is None and False:
                    continue
                x, y = x0 + c * cw, top + r * chh
                if v is None:
                    P.append(box(x, y, cw, chh, '#fff', dash=True, sw=3, rx=0))
                else:
                    P.append(box(x, y, cw, chh, SKY, sw=3, rx=0))
                    P.append(T(x + cw / 2, y + chh / 2 + 12, v, 36))
        maxh = max(maxh, top + len(rows) * chh)
        x0 += ncol * cw + 60
    return wrap(P, x0 - 54, maxh + 8, '1000 chart pieces', w, 0.14)


# ------------------------------------------------------------------------------------------ l2_nline
def nline(spec, w=None):
    lo, hi, step = spec['lo'], spec['hi'], spec['step']
    labels = set(spec.get('labels', [lo, hi]))
    n = (hi - lo) // step
    L = 56
    sp = spec.get('spacing', 72)
    W = 2 * L + n * sp
    y0 = 118
    P = [line(L - 20, y0, W - L + 20, y0, 3.4)]
    for i in range(n + 1):
        v = lo + i * step
        x = L + i * sp
        big = v in labels
        P.append(line(x, y0 - (26 if big else 16), x, y0 + (26 if big else 16), 3.4 if big else 2.4))
        if big:
            P.append(T(x, y0 + 66, v, 34))
    for a in spec.get('arrows', []):
        x = L + (a['at'] - lo) / step * sp
        P.append(f'<path d="M{x} {y0 - 8} L{x - 14} {y0 - 44} L{x + 14} {y0 - 44} Z" fill="{NAVY}" stroke="{NAVY}" stroke-width="2"/>')
        P.append(T(x, y0 - 56, a['label'], 36))
    for d in spec.get('dots', []):
        x = L + (d['at'] - lo) / step * sp
        P.append(f'<circle cx="{x}" cy="{y0}" r="11" fill="{NAVY}"/>')
        if d.get('label'):
            P.append(T(x, y0 - 24, d['label'], 34))
    return wrap(P, W, y0 + 84, 'number line', w, 0.2)


# ------------------------------------------------------------------------------------------ l2_table
def table(spec, w=None):
    cols = spec['cols']
    rows = spec['rows']
    cwid = spec.get('widths') or [1] * len(cols)
    tot = sum(cwid)
    TW = spec.get('width_units', 700)
    xs = [0]
    for c in cwid:
        xs.append(xs[-1] + c / tot * TW)
    rh = spec.get('row_h', 66)
    hh = spec.get('head_h', 66)
    fs = spec.get('size', 36)
    P = []
    x0, y0 = 6, 6
    for j, c in enumerate(cols):
        P.append(f'<rect x="{x0 + xs[j]}" y="{y0}" width="{xs[j + 1] - xs[j]}" height="{hh}" fill="{SOFT}" stroke="{NAVY}" stroke-width="3"/>')
        if c:
            P.append(T(x0 + (xs[j] + xs[j + 1]) / 2, y0 + hh / 2 + fs * 0.35, c, fs, weight=800))
    for i, r in enumerate(rows):
        y = y0 + hh + i * rh
        for j, v in enumerate(r):
            P.append(f'<rect x="{x0 + xs[j]}" y="{y}" width="{xs[j + 1] - xs[j]}" height="{rh}" fill="#fff" stroke="{NAVY}" stroke-width="3"/>')
            if v is not None:
                bold = 800 if (j == 0 and spec.get('first_bold')) else 600
                cwid_u = xs[j + 1] - xs[j] - 14
                f2 = max(24, min(fs, cwid_u / (max(len(str(v)), 1) * 0.62)))
                P.append(T(x0 + (xs[j] + xs[j + 1]) / 2, y + rh / 2 + f2 * 0.35, v, round(f2, 1), weight=bold))
    H = y0 + hh + len(rows) * rh + 8
    return wrap(P, TW + 12, H, spec.get('label', 'table'), w, 0.2)


# ------------------------------------------------------------------------------------------ l2_grid
def grid(spec, w=None):
    vals = spec['values']
    cs = spec.get('cell', 76)
    hatch = {tuple(h) for h in spec.get('hatch', [])}
    nr, nc = len(vals), len(vals[0])
    P = []
    for r in range(nr):
        for c in range(nc):
            v = vals[r][c]
            x, y = 6 + c * cs, 6 + r * cs
            if v is None:
                P.append(box(x, y, cs, cs, '#fff', dash=False, sw=3, rx=0))
            elif v == '':
                P.append(box(x, y, cs, cs, '#fff', sw=3, rx=0))
            else:
                P.append(box(x, y, cs, cs, YEL if (r, c) in hatch else SOFT, sw=3, rx=0))
                P.append(T(x + cs / 2, y + cs / 2 + 13, v, 40))
    cap = spec.get('caption')
    H = nr * cs + 12 + (46 if cap else 0)
    if cap:
        P.append(T(6 + nc * cs / 2, nr * cs + 48, cap, 30, weight=600))
    return wrap(P, nc * cs + 12, H, spec.get('label', 'grid of numbers'), w, 0.2)


# ------------------------------------------------------------------------------------------ l2_vsum
def vsum(spec, w=None):
    """A vertical sum.  rows: list of 3 strings (top, bottom, answer line) written as digits; '?' = an empty box for the child.
    op: '+' or '-'.  Example {"op":"+","rows":["3?7","?48","7?5"]}.  Several sums side by side: {"sums":[{...},{...}]}."""
    sums = spec.get('sums') or [spec]
    cw, rh = 66, 66
    P = []
    x0 = 6
    for s in sums:
        top, bot, res = s['rows']
        n = max(len(top), len(bot), len(res))
        def row(txt, y, boxed):
            out = []
            for i, ch in enumerate(txt.rjust(n)):
                if ch == ' ':
                    continue
                x = x0 + 44 + i * cw
                if ch == '?':
                    out.append(box(x + 4, y + 4, cw - 8, rh - 8, '#fff', dash=True, sw=3, rx=6))
                else:
                    out.append(T(x + cw / 2, y + rh / 2 + 16, ch, 46))
            return out
        P += row(top, 6, False)
        P += row(bot, 6 + rh, False)
        P.append(T(x0 + 22, 6 + rh + rh / 2 + 16, s.get('op', '+'), 46))
        P.append(line(x0 + 4, 6 + 2 * rh + 4, x0 + 44 + n * cw + 4, 6 + 2 * rh + 4, 4))
        P += row(res, 6 + 2 * rh + 8, True)
        if s.get('label'):
            P.append(T(x0 + (44 + n * cw) / 2, 6 + 3 * rh + 52, s['label'], 30))
        x0 += 44 + n * cw + 60
    H = 6 + 3 * rh + 8 + (60 if any(s.get('label') for s in sums) else 14)
    return wrap(P, x0 - 54, H, 'vertical sum with missing digits', w, 0.14)


FIGS = {'l2_cards': cards, 'l2_blocks': blocks, 'l2_chart': chart, 'l2_nline': nline, 'l2_table': table, 'l2_grid': grid, 'l2_vsum': vsum}
