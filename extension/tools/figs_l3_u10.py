"""Level 3 Unit 10 (Puzzle day) figure types.

  l3_bargraph  a bar graph with a scale.  spec: cats [labels], values [numbers; None = no bar drawn (the child draws it)], max, step (labelled
               lines), minor (extra thin lines), unit_label (text above the axis), bar width and gap are fixed.
  l3_queue     children standing in a line.  spec: n, marks {position (1 = front): text}, front (bool: numbers from the front above), back
               (bool: numbers from the back below)
"""
import figs as F
from figs_l3_common import T, wrap, esc, NAVY, SOFT, SKY, YEL, SW

FIGS = {}


def bargraph(spec, w=None):
    cats, vals = spec['cats'], spec['values']
    mx, step = spec['max'], spec['step']
    minor = spec.get('minor', step)
    X0, Y0, H = 90, 50, spec.get('h', 300)
    bw, gap = 64, 40
    W = X0 + len(cats) * (bw + gap) + 20
    yy = lambda v: Y0 + H - H * v / mx
    P = []
    v = 0
    while v <= mx + 1e-9:
        major = abs(v / step - round(v / step)) < 1e-9
        P.append(f'<line x1="{X0}" y1="{yy(v):.1f}" x2="{W - 10}" y2="{yy(v):.1f}" stroke="{NAVY}" stroke-width="{2.4 if major else 1.2}" {"" if major else "stroke-dasharray=\"4 5\""}/>')
        if major:
            P.append(T(X0 - 12, yy(v) + 9, f'{v:g}', 26, anchor='end', weight=700))
        v += minor
    P.append(f'<line x1="{X0}" y1="{Y0 - 6}" x2="{X0}" y2="{Y0 + H}" stroke="{NAVY}" stroke-width="4"/>')
    if spec.get('unit_label'):
        P.append(T(X0 - 70, Y0 - 16, esc(spec['unit_label']), 26, anchor='start', weight=700))
    for i, (c, val) in enumerate(zip(cats, vals)):
        x = X0 + gap / 2 + i * (bw + gap)
        if val is not None:
            P.append(f'<rect x="{x}" y="{yy(val):.1f}" width="{bw}" height="{Y0 + H - yy(val):.1f}" fill="{YEL}" stroke="{NAVY}" stroke-width="{SW}"/>')
        P.append(T(x + bw / 2, Y0 + H + 36, esc(c), 26, weight=700))
    return wrap(P, W, Y0 + H + 56, 'bar graph', w)


def queue(spec, w=None):
    n = spec['n']
    marks = {int(k): v for k, v in spec.get('marks', {}).items()}
    D = 64
    X0 = 110
    P = []
    y = 70 if spec.get('front', True) else 40
    for i in range(1, n + 1):
        x = X0 + (i - 1) * D
        mark = i in marks
        P.append(f'<circle cx="{x}" cy="{y + 24}" r="24" fill="{YEL if mark else "#fff"}" stroke="{NAVY}" stroke-width="{SW}"/>')
        P.append(f'<rect x="{x - 18}" y="{y + 52}" width="36" height="44" rx="12" fill="{YEL if mark else "#fff"}" stroke="{NAVY}" stroke-width="{SW}"/>')
        if spec.get('front', True):
            P.append(T(x, y - 8, i, 26, weight=700))
        if spec.get('back', True):
            P.append(T(x, y + 128, n - i + 1, 26, weight=700))
        if mark:
            P.append(T(x, y + 166, esc(marks[i]), 28))
    H = y + 184
    if spec.get('front', True):
        P.append(T(X0 - 44, y - 8, 'front', 24, anchor='end', weight=700))
    return wrap(P, X0 + (n - 1) * D + 60, H, 'children in a queue', w)


FIGS.update({'l3_bargraph': bargraph, 'l3_queue': queue})
