"""Figure types for Level 2 unit 3 (arrays, equal groups, legs and wheels).

  l2_array   rows x cols of counters in a frame.  Optional `cloth`: {r0, c0, r1, c1} (inclusive cells) hides those counters under a hatched cloth.
  l2_groups  equal groups: `groups`: list of counts (None = a dashed empty plate for the child to fill); `per_row` counters inside a plate; optional `labels`.
  l2_legs    a row of animals or cycles: items [{kind, n}] with kind dog, duck, bike, trike; n copies.  Legs and wheels are drawn so they can be counted.
Palette NAVY / SOFT / YEL only (counters are YEL circles, solid black in print).
"""
import figs as F
from figs_l2_core import T, box, line, wrap, NAVY, SKY, SOFT, YEL


def array(spec, w=None):
    R, C = spec['rows'], spec['cols']
    cs = 46
    cl = spec.get('cloth')
    P = [box(4, 4, C * cs + 16, R * cs + 16, '#fff', sw=3.4, rx=10)]
    for r in range(R):
        for c in range(C):
            if cl and cl['r0'] <= r <= cl['r1'] and cl['c0'] <= c <= cl['c1']:
                continue
            cx, cy = 12 + c * cs + cs / 2, 12 + r * cs + cs / 2
            P.append(f'<circle cx="{cx}" cy="{cy}" r="15" fill="{YEL}" stroke="{NAVY}" stroke-width="2.6"/>')
    if cl:
        x, y = 12 + cl['c0'] * cs + 3, 12 + cl['r0'] * cs + 3
        cw, ch = (cl['c1'] - cl['c0'] + 1) * cs - 6, (cl['r1'] - cl['r0'] + 1) * cs - 6
        P.append(f'<rect x="{x}" y="{y}" width="{cw}" height="{ch}" rx="8" fill="{YEL}" stroke="{NAVY}" stroke-width="3.4"/>')
        P.append(f'<rect x="{x + cw / 2 - 52}" y="{y + ch / 2 - 20}" width="104" height="40" rx="8" fill="#fff"/>')
        P.append(T(x + cw / 2, y + ch / 2 + 11, cl.get('label', 'cloth'), 30))
    return wrap(P, C * cs + 24, R * cs + 24, 'array of counters', w, 0.2)


def groups(spec, w=None):
    gs = spec['groups']
    pr = spec.get('per_row', 3)
    labels = spec.get('labels')
    cs = 40
    D = max(pr, 2) * cs + 30
    rows_max = max(((g or 0) + pr - 1) // pr for g in gs)
    H0 = max(rows_max * cs + 30, D)
    P = []
    x = 6
    for i, g in enumerate(gs):
        cx = x + D / 2
        cy = 6 + H0 / 2
        if g is None:
            P.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{D / 2}" ry="{H0 / 2}" fill="#fff" stroke="{NAVY}" stroke-width="3.4" stroke-dasharray="9 6"/>')
        else:
            P.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{D / 2}" ry="{H0 / 2}" fill="{SOFT}" stroke="{NAVY}" stroke-width="3.4"/>')
            rows = (g + pr - 1) // pr
            for k in range(g):
                r, c = divmod(k, pr)
                n_in_row = pr if r < rows - 1 else g - r * pr
                x0 = cx - (n_in_row - 1) * cs / 2
                y0 = cy - (rows - 1) * cs / 2
                P.append(f'<circle cx="{x0 + c * cs}" cy="{y0 + r * cs}" r="14" fill="{YEL}" stroke="{NAVY}" stroke-width="2.6"/>')
        if labels:
            P.append(T(cx, 6 + H0 + 40, labels[i], 30))
        x += D + 30
    H = 6 + H0 + (52 if labels else 8)
    return wrap(P, x - 24, H, 'equal groups of counters', w, 0.2)


def _dog(x, y, legs):
    P = []
    spread = {4: [-26, -10, 10, 26], 2: [-10, 10]}[legs]
    for dx in spread:
        P.append(line(x + dx, y + 18, x + dx, y + 52, 5))
    P.append(f'<ellipse cx="{x}" cy="{y}" rx="38" ry="24" fill="{SOFT}" stroke="{NAVY}" stroke-width="3.2"/>')
    P.append(f'<circle cx="{x - 40}" cy="{y - 18}" r="15" fill="{SOFT}" stroke="{NAVY}" stroke-width="3.2"/>')
    P.append(f'<circle cx="{x - 44}" cy="{y - 21}" r="3.5" fill="{NAVY}"/>')
    if legs == 4:
        P.append(line(x + 38, y - 6, x + 54, y - 20, 4.5))
    else:
        P.append(f'<path d="M{x - 55} {y - 16} l-14 4 l14 5z" fill="{NAVY}"/>')
        P.append(f'<path d="M{x + 36} {y - 4} q18 -6 22 -22 q-14 6 -22 8z" fill="{SOFT}" stroke="{NAVY}" stroke-width="2.6"/>')
    return P


def _wheel(x, y, r):
    return [f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff" stroke="{NAVY}" stroke-width="4.4"/>', f'<circle cx="{x}" cy="{y}" r="3.5" fill="{NAVY}"/>']


def _bike(x, y):
    P = _wheel(x - 34, y + 22, 20) + _wheel(x + 34, y + 22, 20)
    P.append(f'<path d="M{x - 34} {y + 22} L{x - 6} {y - 14} L{x + 24} {y - 14} L{x + 34} {y + 22} M{x - 6} {y - 14} L{x + 4} {y + 22} L{x - 34} {y + 22} M{x + 24} {y - 14} L{x + 18} {y - 28} L{x + 32} {y - 28}" fill="none" stroke="{NAVY}" stroke-width="3.6" stroke-linejoin="round"/>')
    return P


def _trike(x, y):
    P = _wheel(x - 30, y + 22, 20) + _wheel(x + 22, y + 24, 14) + _wheel(x + 50, y + 24, 14)
    P.append(f'<path d="M{x - 30} {y + 22} L{x - 22} {y - 16} L{x + 6} {y - 16} L{x + 36} {y + 24} M{x - 22} {y - 16} L{x - 30} {y - 28} L{x - 14} {y - 28} M{x + 6} {y - 16} L{x + 22} {y + 24} M{x + 36} {y + 8} L{x + 50} {y + 24}" fill="none" stroke="{NAVY}" stroke-width="3.6" stroke-linejoin="round"/>')
    return P


def legs(spec, w=None):
    P = []
    x = 20
    gap = spec.get('gap', 108)
    for it in spec['items']:
        for _ in range(it.get('n', 1)):
            cx = x + 64
            k = it['kind']
            if k == 'dog':
                P += _dog(cx, 70, 4)
            elif k == 'duck':
                P += _dog(cx, 70, 2)
            elif k == 'bike':
                P += _bike(cx, 70)
            elif k == 'trike':
                P += _trike(cx, 70)
            if spec.get('names'):
                P.append(T(cx, 142, {'dog': 'dog', 'duck': 'duck', 'bike': 'bicycle', 'trike': 'tricycle'}[k], 26, weight=700))
            x += gap
    return wrap(P, x + 40, 160 if spec.get('names') else 150, 'animals or cycles in a row', w, 0.2)


FIGS = {'l2_array': array, 'l2_groups': groups, 'l2_legs': legs}
