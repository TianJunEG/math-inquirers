"""Level 4 figure plug-in: line graphs (one or two lines, one or two panels with their own scales).

  l4_line  panels [{title?, ymin, ymax, step, label_every?, ylabel?, series:[{name, values:[..|None], style?:'solid'|'dash'}]}], xlabels [..], xlabel?,
           width_mm.  A panel whose ymin is above 0 shows a zigzag on the axis.  The two lines of a panel differ by dash and by marker shape (circle, square),
           never by colour only.
"""
import figs as F

NAVY, TEAL, RED, SKY, SOFT, YEL = F.NAVY, F.TEAL, F.RED, F.SKY, F.SOFT, F.YEL


def _t(x, y, txt, size=24, fill=NAVY, anchor='middle', weight=700):
    return F._t(round(x, 1), round(y, 1), txt, size, fill, anchor, weight)


def _esc(s):
    return str(s).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def _panel(sp, xlabels, ox, oy, PW, PH, P):
    ymin, ymax, step = sp['ymin'], sp['ymax'], sp['step']
    every = sp.get('label_every', 1)
    n = len(xlabels)
    Y = lambda v: oy + PH - (v - ymin) / (ymax - ymin) * PH
    X = lambda i: ox + (i + 0.5) * PW / n
    if sp.get('title'):
        P.append(_t(ox + PW / 2, oy - 22, _esc(sp['title']), 28, weight=800))
    k = 0
    v = ymin
    while v <= ymax + 1e-9:
        y = Y(v)
        P.append(f'<line x1="{ox}" y1="{y:.1f}" x2="{ox + PW}" y2="{y:.1f}" stroke="{NAVY}" stroke-width="1.8" stroke-dasharray="2 6"/>')
        if k % every == 0:
            lab = f'{v:g}'
            P.append(_t(ox - 12, y + 8, lab, 24, anchor='end', weight=700))
        v += step
        k += 1
    P.append(f'<line x1="{ox}" y1="{oy - 6}" x2="{ox}" y2="{oy + PH}" stroke="{NAVY}" stroke-width="4"/>')
    P.append(f'<line x1="{ox}" y1="{oy + PH}" x2="{ox + PW}" y2="{oy + PH}" stroke="{NAVY}" stroke-width="4"/>')
    if ymin > 0:      # zigzag: the scale does not start at 0
        P.append(f'<path d="M{ox - 14},{oy + PH - 30} L{ox + 14},{oy + PH - 42} L{ox - 14},{oy + PH - 54} L{ox + 14},{oy + PH - 66}" fill="none" stroke="{NAVY}" stroke-width="4"/>')
    for i, lab in enumerate(xlabels):
        P.append(_t(X(i), oy + PH + 32, _esc(lab), 24, weight=700))
        P.append(f'<line x1="{X(i):.1f}" y1="{oy + PH}" x2="{X(i):.1f}" y2="{oy + PH + 8}" stroke="{NAVY}" stroke-width="3"/>')
    leg_x = ox + 10
    for si, s in enumerate(sp['series']):
        if s.get('name'):
            ly = oy - 30
            dash = ' stroke-dasharray="14 9"' if s.get('style', 'solid' if si == 0 else 'dash') == 'dash' else ''
            P.append(f'<line x1="{leg_x}" y1="{ly}" x2="{leg_x + 70}" y2="{ly}" stroke="{NAVY}" stroke-width="4.4"{dash}/>')
            if si == 0:
                P.append(f'<circle cx="{leg_x + 35}" cy="{ly}" r="9" fill="#fff" stroke="{NAVY}" stroke-width="4"/>')
            else:
                P.append(f'<rect x="{leg_x + 26}" y="{ly - 9}" width="18" height="18" fill="#fff" stroke="{NAVY}" stroke-width="4"/>')
            P.append(_t(leg_x + 82, ly + 8, _esc(s['name']), 26, anchor='start', weight=800))
            leg_x += 82 + 16 * len(s['name']) + 60
    for si, s in enumerate(sp['series']):
        pts = [(X(i), Y(v)) for i, v in enumerate(s['values']) if v is not None]
        dash = ' stroke-dasharray="14 9"' if s.get('style', 'solid' if si == 0 else 'dash') == 'dash' else ''
        P.append(f'<polyline points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in pts)}" fill="none" stroke="{NAVY}" stroke-width="4.4"{dash} stroke-linejoin="round"/>')
        for (x, y) in pts:
            if si == 0:
                P.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="9" fill="#fff" stroke="{NAVY}" stroke-width="4"/>')
            else:
                P.append(f'<rect x="{x - 9:.1f}" y="{y - 9:.1f}" width="18" height="18" fill="#fff" stroke="{NAVY}" stroke-width="4"/>')


def l4_line(spec, w=None):
    panels = spec['panels']
    xl = spec['xlabels']
    PW = spec.get('plot_w', 520 if len(panels) == 1 else 330)
    PH = spec.get('plot_h', 300)
    gap = 90
    left = 74
    P = []
    top = 56 if any(p.get('title') for p in panels) or any(s.get('name') for p in panels for s in p['series']) or spec.get('ylabel') else 24
    for k, sp in enumerate(panels):
        _panel(sp, xl, left + k * (PW + gap), top, PW, PH, P)
    W = left + len(panels) * PW + (len(panels) - 1) * gap + 40
    H = top + PH + 100 if spec.get('xlabel') else top + PH + 56
    if spec.get('xlabel'):
        P.append(_t(left + PW / 2 + (len(panels) - 1) * (PW + gap) / 2, top + PH + 84, _esc(spec['xlabel']), 24, weight=700))
    if spec.get('ylabel'):
        P.append(_t(left - 60, top - 22, _esc(spec['ylabel']), 24, anchor='start', weight=800))
    return F._wrap(''.join(P), W, H, spec.get('label', 'line graph'), w or spec.get('width_mm', 140))


FIGS = {'l4_line': l4_line}
