"""Figure types for Level 2 unit 10 (puzzle day: graphs, tally, logic grids).

  l2_pgraph   picture graph: rows [{label, n}] with n pictures (a half picture is n = 3.5; None draws an empty dashed row for the child); `key` {value, unit} prints
              "Each o stands for <value> <unit>"; key None prints "Each o stands for ?" (a lost key).  Pictures are solid dots in print.
  l2_tally    tally chart: rows [{label, n}]; groups of five are four strokes with a slash through them.
  l2_lgrid    logic grid: rows (names) by cols (things); marks {"r,c": "tick" | "cross"} are drawn in the cells; empty cells are for the child.
"""
import figs as F
from figs_l2_core import T, box, line, wrap, NAVY, SKY, SOFT, YEL


def pgraph(spec, w=None):
    rows = spec['rows']
    LW = 30 + max(len(r['label']) for r in rows) * 19
    RH = 58
    D = 48
    P = []
    maxn = max((r['n'] or 0) for r in rows)
    maxn = max(maxn, spec.get('min_cols', 6))
    W = LW + int(maxn + 1) * D + 20
    for i, r in enumerate(rows):
        y = 8 + i * RH
        P.append(T(LW - 12, y + RH / 2 + 8, r['label'], 28, anchor='end'))
        P.append(box(LW, y, W - LW - 6, RH - 8, '#fff', sw=2.6, rx=0))
        n = r['n']
        if n is None:
            continue
        k = 0
        while k < n:
            cx = LW + 16 + D * k + D / 2 - 8
            cy = y + (RH - 8) / 2
            if n - k >= 1:
                P.append(f'<circle cx="{cx}" cy="{cy}" r="19" fill="{YEL}" stroke="{NAVY}" stroke-width="3"/>')
            else:
                P.append(f'<path d="M{cx} {cy - 19} A19 19 0 0 0 {cx} {cy + 19} Z" fill="{YEL}" stroke="{NAVY}" stroke-width="3"/>')
                P.append(f'<path d="M{cx} {cy - 19} A19 19 0 0 1 {cx} {cy + 19}" fill="none" stroke="{NAVY}" stroke-width="2" stroke-dasharray="4 4"/>')
            k += 1
    H = 8 + len(rows) * RH
    key = spec.get('key')
    kt = f'Each   stands for {key["value"]} {key.get("unit", "children")}' if key else 'Each   stands for ?'
    kx = LW
    P.append(T(kx, H + 36, 'Each', 28, anchor='start'))
    P.append(f'<circle cx="{kx + 92}" cy="{H + 26}" r="16" fill="{YEL}" stroke="{NAVY}" stroke-width="3"/>')
    P.append(T(kx + 120, H + 36, f'stands for {key["value"]} {key.get("unit", "children")}' if key else 'stands for ?', 28, anchor='start'))
    keyw = LW + 130 + (len(str(key['value'])) + len(key.get('unit', 'children')) + 10 if key else 12) * 16
    return wrap(P, max(W, keyw), H + 56, 'picture graph', w, 0.2)


def tally(spec, w=None):
    rows = spec['rows']
    LW = 30 + max(len(r['label']) for r in rows) * 19
    RH = 78
    P = []
    for i, r in enumerate(rows):
        y = 8 + i * RH
        P.append(T(LW - 12, y + RH / 2 + 8, r['label'], 28, anchor='end'))
        x = LW + 10
        n = r['n']
        while n > 0:
            g = min(n, 5)
            for k in range(min(g, 4)):
                P.append(line(x + k * 16, y + 10, x + k * 16, y + RH - 18, 5))
            if g == 5:
                P.append(line(x - 8, y + RH - 28, x + 4 * 16 + 4, y + 22, 5))
            elif g == 4:
                pass
            x += (4 * 16 if g >= 4 else g * 16) + 28 if g == 5 else g * 16 + 28
            n -= g
    Wd = max(LW + 10 + 400, 560)
    return wrap(P, Wd, 8 + len(rows) * RH + 6, 'tally chart', w, 0.2)


def lgrid(spec, w=None):
    rows, cols = spec['rows'], spec['cols']
    marks = spec.get('marks', {})
    cs = spec.get('cell', 106)
    LW = 30 + max(len(r) for r in rows) * 20
    HH = 50 if cs < 100 else 62
    P = []
    for j, c in enumerate(cols):
        P.append(f'<rect x="{LW + j * cs}" y="6" width="{cs}" height="{HH}" fill="{SOFT}" stroke="{NAVY}" stroke-width="3"/>')
        P.append(T(LW + j * cs + cs / 2, 6 + HH / 2 + 9, c, 20 if cs < 100 else 24, weight=800))
    for i, r in enumerate(rows):
        y = 6 + HH + i * cs
        P.append(f'<rect x="6" y="{y}" width="{LW - 6}" height="{cs}" fill="{SOFT}" stroke="{NAVY}" stroke-width="3"/>')
        P.append(T(6 + (LW - 6) / 2, y + cs / 2 + 9, r, 28, weight=800))
        for j in range(len(cols)):
            P.append(f'<rect x="{LW + j * cs}" y="{y}" width="{cs}" height="{cs}" fill="#fff" stroke="{NAVY}" stroke-width="3"/>')
            m = marks.get(f'{i},{j}')
            cx, cy = LW + j * cs + cs / 2, y + cs / 2
            if m == 'tick':
                P.append(f'<path d="M{cx - 20} {cy} l14 16 l28 -34" fill="none" stroke="{NAVY}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>')
            elif m == 'cross':
                P.append(line(cx - 18, cy - 18, cx + 18, cy + 18, 7))
                P.append(line(cx + 18, cy - 18, cx - 18, cy + 18, 7))
    return wrap(P, LW + len(cols) * cs + 8, 6 + HH + len(rows) * cs + 6, 'logic grid', w, 0.2)


FIGS = {'l2_pgraph': pgraph, 'l2_tally': tally, 'l2_lgrid': lgrid}
