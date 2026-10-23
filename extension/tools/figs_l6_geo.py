"""Level 6 figure types, part 2: matchstick patterns, turtle paths, dots and routes, clocks, spinners, counters, bars, cipher strips.
Type names start with l6_.  Drawing unit: 1 unit = 0.25 mm (see figs_l6_core).  Fills are only SKY / SOFT / '#fff' (white in print); YEL (hatching in
print) is used only where no text sits on top of it.

  l6_sticks  matchstick patterns.  spec: shape 'sq' (rows x k squares), 'tri' (k triangles in a row), 'stairs' (steps 1..k), ks [pattern numbers], rows (for 'sq'),
             side (mm), label_fmt ("Pattern {k}"), blank (list of pattern numbers drawn as a dashed empty frame)
"""
import math
import figs as F
from figs_l6_core import NAVY, SKY, SOFT, YEL, U, T, R, L, wrap, esc, neg

FIGS = {}


def _edges_sq(k, rows):
    E = set()
    for i in range(k):
        for j in range(rows):
            a, b, c, d = (i, j), (i + 1, j), (i + 1, j + 1), (i, j + 1)
            for p, q in ((a, b), (b, c), (d, c), (a, d)):
                E.add((p, q))
    return E


def _edges_tri(k):
    E = set()
    for i in range(k):
        m = i // 2
        if i % 2 == 0:
            A, B, C = (m, 0), (m + 1, 0), (m + .5, 1)
        else:
            A, B, C = (m + .5, 1), (m + 1.5, 1), (m + 1, 0)
        for p, q in ((A, B), (B, C), (A, C)):
            E.add(tuple(sorted((p, q))))
    return E


def _edges_stairs(k):
    E = set()
    for c in range(k):
        for r in range(c + 1):
            a, b, cc, d = (c, r), (c + 1, r), (c + 1, r + 1), (c, r + 1)
            for p, q in ((a, b), (b, cc), (d, cc), (a, d)):
                E.add((p, q))
    return E


def sticks(spec, w=None):
    shape = spec.get('shape', 'sq')
    side = spec.get('side', 9) * U
    ks = spec['ks']
    rows = spec.get('rows', 1)
    fmt = spec.get('label_fmt', 'Staircase {k}' if shape == 'stairs' else 'Pattern {k}')
    gap = spec.get('gap', 4) * U
    P = []
    x0 = 8
    H = 0
    for k in ks:
        if shape == 'sq':
            E = _edges_sq(k, rows); wk = k * side; hk = rows * side
        elif shape == 'stairs':
            E = _edges_stairs(k); wk = k * side; hk = k * side
        else:
            E = _edges_tri(k); wk = (k + 1) / 2 * side; hk = side * 0.866
        label = fmt.format(k=k)
        slot = max(wk, len(label) * 10.5 + 6)      # the label must fit under the drawing
        xo = x0 + (slot - wk) / 2
        pt = (lambda p_: (xo + p_[0] * side, 10 + hk - p_[1] * hk)) if shape == 'tri' else (lambda p_: (xo + p_[0] * side, 10 + hk - p_[1] * side))
        for (p, q) in E:
            ax, ay = pt(p); bx, by = pt(q)
            P.append(L(ax, ay, bx, by, 6.5))
        for (p, q) in E:      # heads: a small solid dot at one end of every stick
            ax, ay = pt(p)
            P.append(f'<circle cx="{ax:.1f}" cy="{ay:.1f}" r="5.6" fill="{NAVY}"/>')
        P.append(T(x0 + slot / 2, 10 + hk + 34, label, 17))
        x0 += slot + gap
        H = max(H, hk)
    W = x0 - gap + 8
    return wrap(''.join(P), W, H + 56, 'matchstick patterns', w)


FIGS['l6_sticks'] = sticks


# ================================================================================================ bar model
def model(spec, w=None):
    """Bar model.  spec: rows [{label, segs:[{w (mm), t (text), dash (bool)}]}], brace {t} draws a bracket at the right of all rows with a text,
    unit_h (mm, row height), lab (mm, label column width)."""
    rows = spec['rows']
    rh = spec.get('unit_h', 9) * U
    gap = 3 * U
    lab = spec.get('lab', 26) * U
    P = []
    maxw = 0
    for i, r in enumerate(rows):
        y = 6 + i * (rh + gap)
        P.append(T(lab - 10, y + rh / 2 + 6, r['label'], 17, 'end', 800))
        x = lab
        for sg in r['segs']:
            ww = sg['w'] * U
            P.append(R(x, y, ww, rh, SKY if not sg.get('dash') else '#fff', 2.8, 3, dash='7 5' if sg.get('dash') else None))
            if sg.get('t'):
                P.append(T(x + ww / 2, y + rh / 2 + 6.5, sg['t'], 19, weight=800))
            x += ww
        maxw = max(maxw, x - lab)
    H = 6 + len(rows) * (rh + gap) - gap + 6
    W = lab + maxw + 8
    if spec.get('brace'):
        bx = lab + maxw + 12
        y0, y1 = 6, H - 6
        P.append(f'<path d="M{bx} {y0} q14 0 14 14 v{(y1 - y0) / 2 - 28:.1f} q0 14 14 14 q-14 0 -14 14 v{(y1 - y0) / 2 - 28:.1f} q0 14 -14 14" fill="none" stroke="{NAVY}" stroke-width="3"/>')
        tx = bx + 40
        P.append(T(tx, (y0 + y1) / 2 + 6, spec['brace']['t'], 18, 'start', 800))
        W = tx + len(spec['brace']['t']) * 11 + 10
    return wrap(''.join(P), W, H, 'bar model', w)


FIGS['l6_model'] = model


# ================================================================================================ dots joined by lines, and route grids
def _node(x, y, label='', r=18, fill='#fff', sw=2.8, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    s_ = f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{fill}" stroke="{NAVY}" stroke-width="{sw}"{d}/>'
    if label != '':
        s_ += T(x, y + 6.5, label, 19, weight=800)
    return s_


def dots(spec, w=None):
    """People or points joined by lines.  spec: groups = [{n (regular polygon of n nodes) or pts [[x_mm, y_mm, label]], all (join every pair), edges [[i, j]], labels [..], caption, r (mm)}]."""
    import math
    P = []
    x0 = 6
    H = 0
    for g in spec['groups']:
        r = g.get('r', 15) * U
        if g.get('pts'):
            raw = [(p_[0] * U, p_[1] * U) for p_ in g['pts']]
            labs = [p_[2] for p_ in g['pts']]
            gw = max(p_[0] for p_ in raw) + 44
            gh = max(p_[1] for p_ in raw) + 44
            pts = [(18 + p_[0], 18 + p_[1]) for p_ in raw]
        else:
            n = g['n']
            labs = g.get('labels') or [chr(65 + i) for i in range(n)]
            c = (r + 24, r + 24)
            pts = [(c[0] + r * math.sin(2 * math.pi * k / n), c[1] - r * math.cos(2 * math.pi * k / n)) for k in range(n)]
            gw = 2 * r + 48
            gh = 2 * r + 48
        if g.get('caption'):
            cw = len(g['caption']) * 10.5 + 16
            if cw > gw:
                pts = [(p_[0] + (cw - gw) / 2, p_[1]) for p_ in pts]
                gw = cw
        pts = [(x0 + p_[0], p_[1]) for p_ in pts]
        edges = g.get('edges')
        if g.get('all'):
            edges = [[i, j] for i in range(len(pts)) for j in range(i + 1, len(pts))]
        for i, j in edges or []:
            P.append(L(pts[i][0], pts[i][1], pts[j][0], pts[j][1], 2.8))
        for (px, py), lab in zip(pts, labs):
            P.append(_node(px, py, lab))
        if g.get('caption'):
            P.append(T(x0 + gw / 2, gh + 26, g['caption'], 17))
            gh += 30
        x0 += gw + g.get('gap', 6) * U
        H = max(H, gh)
    W = x0 - 6 * U + 6
    return wrap(''.join(P), W, H + 8, 'dots joined by lines', w)


def routes(spec, w=None):
    """A lattice of streets.  spec: cols, rows, cell (mm), nums {"c,r": value or null (empty node to fill)}, mark ["c,r"] (a node ringed and labelled X),
    start / end labels.  Node (0, 0) is the bottom left."""
    cols, rows = spec['cols'], spec['rows']
    cell = spec.get('cell', 15) * U
    nums = spec.get('nums', {})
    mark = spec.get('mark', [])
    X0, Y0 = 44, 50
    W = X0 * 2 + cols * cell
    H = Y0 + rows * cell + 50
    xy = lambda c, r: (X0 + c * cell, Y0 + (rows - r) * cell)
    P = []
    for r in range(rows + 1):
        P.append(L(*xy(0, r), *xy(cols, r), 3))
    for c in range(cols + 1):
        P.append(L(*xy(c, 0), *xy(c, rows), 3))
    for r in range(rows + 1):
        for c in range(cols + 1):
            key = f'{c},{r}'
            x, y = xy(c, r)
            if key in nums:
                v = nums[key]
                if v is None:
                    P.append(_node(x, y, '', 17, dash='5 4', sw=2.4))
                else:
                    P.append(_node(x, y, str(v), 17))
            else:
                P.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="7" fill="{NAVY}"/>')
            if key in mark:
                P.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="23" fill="none" stroke="{NAVY}" stroke-width="4.2"/>')
                P.append(T(x + 30, y - 24, 'X', 19, weight=800))
    sx, sy = xy(0, 0)
    ex, ey = xy(cols, rows)
    P.append(T(sx, sy + 46, spec.get('start', 'Start'), 17))
    P.append(T(ex, ey - 28, spec.get('end', 'End'), 17))
    return wrap(''.join(P), W, H, 'grid of streets', w)


FIGS['l6_dots'] = dots
FIGS['l6_routes'] = routes


# ================================================================================================ spinner and bag of counters
def spinner(spec, w=None):
    """A spinner with equal parts.  spec: parts [labels] (clockwise from the top), r (mm), title."""
    import math
    parts = spec['parts']
    n = len(parts)
    r = spec.get('r', 22) * U
    cx, cy = r + 10, r + 10 + (24 if spec.get('title') else 0)
    P = []
    P.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#fff" stroke="{NAVY}" stroke-width="3.4"/>')
    for k in range(n):
        a = 2 * math.pi * k / n
        P.append(L(cx, cy, cx + r * math.sin(a), cy - r * math.cos(a), 2.8))
    for k, lab in enumerate(parts):
        a = 2 * math.pi * (k + 0.5) / n
        rr = r * (0.68 if n <= 8 else 0.72)
        P.append(T(cx + rr * math.sin(a), cy - rr * math.cos(a) + 7, lab, 20, weight=800))
    P.append(f'<circle cx="{cx}" cy="{cy}" r="7" fill="{NAVY}"/>')
    if spec.get('title'):
        P.append(T(cx, 16, spec['title'], 17))
    return wrap(''.join(P), 2 * r + 20, 2 * r + 20 + (24 if spec.get('title') else 0), 'spinner', w)


def bag(spec, w=None):
    """A bag of counters.  spec: counters [letters] (a letter in each round counter), cols (counters per row)."""
    cs = spec['counters']
    cols = spec.get('cols', 6)
    d = 38
    rows = (len(cs) + cols - 1) // cols
    W = cols * (d + 8) + 28
    H = rows * (d + 8) + 34
    P = [f'<path d="M{W * 0.18:.0f} 8 Q{W / 2:.0f} 22 {W * 0.82:.0f} 8" fill="none" stroke="{NAVY}" stroke-width="3.4"/>',
         R(6, 14, W - 12, H - 20, SOFT, 3.4, 26)]
    for k, c in enumerate(cs):
        r_, c_ = divmod(k, cols)
        x = 20 + d / 2 + c_ * (d + 8)
        y = 30 + d / 2 + r_ * (d + 8)
        P.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{d / 2}" fill="#fff" stroke="{NAVY}" stroke-width="2.8"/>')
        P.append(T(x, y + 7, c, 19, weight=800))
    return wrap(''.join(P), W, H, 'bag of counters', w)


FIGS['l6_spinner'] = spinner
FIGS['l6_bag'] = bag


# ================================================================================================ turtle path
def turtle(spec, w=None):
    """The path a turtle draws.  spec: cmds = list of ['move', n] / ['turn', deg] / ['repeat', k, [cmds]]; heading 90 = right, 0 = up (as in Scratch), turn = clockwise;
    step_mm = mm per step; dots (corners as dots, default true); labels {corner_index: text} written outside the corner (0 = the start); arrow (a start arrow)."""
    import math
    step = spec.get('step_mm', 0.3) * U
    x, y, h = 0.0, 0.0, spec.get('heading', 90)
    pts = [(x, y)]

    def run_(cmds):
        nonlocal x, y, h
        for c in cmds:
            if c[0] == 'move':
                x += c[1] * step * math.sin(math.radians(h))
                y -= c[1] * step * math.cos(math.radians(h))
                pts.append((x, y))
            elif c[0] == 'turn':
                h += c[1]
            elif c[0] == 'repeat':
                for _ in range(c[1]):
                    run_(c[2])
    run_(spec['cmds'])
    xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
    pad = 34
    x0, y0 = min(xs) - pad, min(ys) - pad
    W = max(xs) - min(xs) + 2 * pad
    H = max(ys) - min(ys) + 2 * pad
    P = []
    sh = lambda p_: (p_[0] - x0, p_[1] - y0)
    P.append('<polyline fill="none" stroke="' + NAVY + '" stroke-width="3.6" stroke-linejoin="round" stroke-linecap="round" points="' + ' '.join(f'{sh(p_)[0]:.1f},{sh(p_)[1]:.1f}' for p_ in pts) + '"/>')
    if spec.get('dots', True):
        seen = set()
        for p_ in pts:
            key = (round(p_[0]), round(p_[1]))
            if key in seen:
                continue
            seen.add(key)
            P.append(f'<circle cx="{sh(p_)[0]:.1f}" cy="{sh(p_)[1]:.1f}" r="6" fill="{NAVY}"/>')
    sx, sy = sh(pts[0])
    a0 = math.radians(spec.get('heading', 90))
    ax, ay = sx + 16 * math.sin(a0), sy - 16 * math.cos(a0)
    if spec.get('arrow', True):
        P.append(f'<circle cx="{sx:.1f}" cy="{sy:.1f}" r="12" fill="#fff" stroke="{NAVY}" stroke-width="3.4"/>')
        P.append(T(sx, sy + 6, 'S', 17, weight=800))
    cx = sum(xs) / len(xs) - x0
    cy = sum(ys) / len(ys) - y0
    for k, txt in (spec.get('labels') or {}).items():
        px, py = sh(pts[int(k)])
        dx, dy = px - cx, py - cy
        d = math.hypot(dx, dy) or 1
        P.append(T(px + dx / d * 26, py + dy / d * 26 + 6, txt, 17, weight=800))
    return wrap(''.join(P), W, H, 'path of a turtle', w)


FIGS['l6_turtle'] = turtle


# ================================================================================================ clock face
def clock(spec, w=None):
    """A 12-hour clock face.  spec: hand (hour 1-12, drawn as one hand), ring [hours] (numbers drawn with a ring), r (mm), title."""
    import math
    r = spec.get('r', 19) * U
    cx, cy = r + 14, r + 14 + (22 if spec.get('title') else 0)
    P = [f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#fff" stroke="{NAVY}" stroke-width="3.6"/>']
    for h in range(1, 13):
        a = math.radians(h * 30)
        P.append(L(cx + (r - 8) * math.sin(a), cy - (r - 8) * math.cos(a), cx + r * math.sin(a), cy - r * math.cos(a), 3))
        tx, ty = cx + (r - 25) * math.sin(a), cy - (r - 25) * math.cos(a)
        if h in spec.get('ring', []):
            P.append(f'<circle cx="{tx:.1f}" cy="{ty:.1f}" r="15" fill="none" stroke="{NAVY}" stroke-width="3.4"/>')
        P.append(T(tx, ty + 6, h, 17, weight=800))
    if spec.get('hand'):
        a = math.radians(spec['hand'] * 30)
        P.append(L(cx, cy, cx + (r - 40) * math.sin(a), cy - (r - 40) * math.cos(a), 5.5))
    P.append(f'<circle cx="{cx}" cy="{cy}" r="6" fill="{NAVY}"/>')
    if spec.get('title'):
        P.append(T(cx, 18, spec['title'], 17))
    return wrap(''.join(P), 2 * r + 28, 2 * r + 28 + (22 if spec.get('title') else 0), 'clock face', w)


FIGS['l6_clock'] = clock


# ================================================================================================ bar chart / towers
def bars(spec, w=None):
    """A bar chart.  spec: values [numbers], labels [text under each bar], unit_mm (mm per 1 of value), ymax, ytick, bar_mm (bar width), gap_mm,
    mean (draw a dashed level line at this value), show (write the value above each bar), blank [indexes] (an empty dashed bar for the child to draw)."""
    vals = spec['values']
    labs = spec.get('labels') or [''] * len(vals)
    um = spec.get('unit_mm', 3.5) * U
    ymax = spec.get('ymax', max(v for v in vals if v is not None))
    ytick = spec.get('ytick', 5)
    bw = spec.get('bar_mm', 11) * U
    gap = spec.get('gap_mm', 5) * U
    X0, Y0 = 60, 20
    H = Y0 + ymax * um + 52
    W = X0 + len(vals) * (bw + gap) + 16
    base = Y0 + ymax * um
    P = [L(X0, Y0 - 6, X0, base, 3), L(X0, base, W - 10, base, 3)]
    t = 0
    while t <= ymax:
        y = base - t * um
        P.append(L(X0 - 9, y, X0, y, 2.6))
        P.append(T(X0 - 14, y + 6, t, 16, 'end', 700))
        t += ytick
    for i, v in enumerate(vals):
        x = X0 + gap / 2 + i * (bw + gap)
        if v is None:
            P.append(R(x, Y0, bw, ymax * um, '#fff', 2.4, 3, dash='7 5'))
        else:
            P.append(R(x, base - v * um, bw, v * um, SKY, 3, 3))
            if spec.get('show'):
                P.append(T(x + bw / 2, base - v * um - 8, v, 17, weight=800))
        P.append(T(x + bw / 2, base + 24, labs[i], 17, weight=700))
    if spec.get('mean') is not None:
        y = base - spec['mean'] * um
        P.append(L(X0, y, W - 10, y, 3, dash='10 6'))
        P.append(T(W - 12, y - 8, 'mean', 16, 'end', 800))
    return wrap(''.join(P), W, H, 'bar chart', w)


FIGS['l6_bars'] = bars
