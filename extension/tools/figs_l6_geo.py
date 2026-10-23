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
