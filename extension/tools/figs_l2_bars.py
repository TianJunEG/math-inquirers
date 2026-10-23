"""Figure types for the Level 2 extension workbook: bar models and magic triangles (units 2, 5, 6, 7, 10).

  l2_bar       bar model.  rows: [{label, segs: [{w, t?, unknown?, hatch?}]}] -- w is the drawn width (relative, NOT the value, so a bar is
               never drawn to a scale that gives an answer away); t is the text inside; unknown=True draws the segment dashed with t (usually "?").
               Optional `brace`: {text, rows: [i, j]} a vertical bracket on the right spanning rows i..j with a label; `note` text under the bars.
               Optional `gapbar` on a row: {"after": seg index, "text"} not used by default.
  l2_triangle  magic triangle: 6 circles (corners 0, 1, 2 = top, bottom-left, bottom-right; sides 3, 4, 5 = between 0-1, 1-2, 2-0).
               values: six items, a number (printed) or None (empty circle for the child).  `caption` is printed below.
"""
import figs as F
from figs_l2_core import T, box, line, wrap, NAVY, SKY, SOFT, YEL


def bar(spec, w=None):
    rows = spec['rows']
    LW = 30 + max(len(r['label']) for r in rows) * 20
    RH, BH = 78, 54
    unit = spec.get('unit', 1.0)
    longest = max(sum(s['w'] for s in r['segs']) for r in rows) * unit
    BW = spec.get('width_units', 560)
    k = BW / longest
    P = []
    top = 14
    for i, r in enumerate(rows):
        y = top + i * RH
        P.append(T(LW - 12, y + BH / 2 + 11, r['label'], 30, anchor='end'))
        x = LW
        for s in r['segs']:
            sw = s['w'] * unit * k
            if s.get('unknown'):
                P.append(box(x, y, sw, BH, '#fff', dash=True, sw=3, rx=0))
            else:
                P.append(box(x, y, sw, BH, YEL if s.get('hatch') else SKY, sw=3, rx=0))
            if s.get('t'):
                if s.get('hatch'):
                    tw = len(str(s['t'])) * 19 + 14
                    P.append(f'<rect x="{x + sw / 2 - tw / 2}" y="{y + BH / 2 - 20}" width="{tw}" height="40" rx="6" fill="#fff"/>')
                P.append(T(x + sw / 2, y + BH / 2 + 11, s['t'], 30))
            x += sw
    H = top + len(rows) * RH
    W = LW + BW + 20
    b = spec.get('brace')
    if b:
        i, j = b['rows']
        y1, y2 = top + i * RH, top + j * RH + BH
        bx = LW + BW + 18
        P.append(f'<path d="M{bx - 8} {y1} L{bx} {y1} L{bx} {y2} L{bx - 8} {y2}" fill="none" stroke="{NAVY}" stroke-width="3.4"/>')
        P.append(T(bx + 14, (y1 + y2) / 2 + 11, b['text'], 30, anchor='start'))
        W = bx + 14 + len(b['text']) * 19 + 14
    if spec.get('note'):
        P.append(T(LW, H + 30, spec['note'], 28, anchor='start', weight=600))
        H += 44
    return wrap(P, W, H + 6, 'bar model', w, 0.2)


def triangle(spec, w=None):
    """One triangle (values, caption) or several side by side (triangles: [{values, caption}])."""
    tris = spec.get('triangles') or [spec]
    R = 44
    pts = [(300, 62), (70, 390), (530, 390)]
    mids = [((pts[0][0] + pts[1][0]) / 2, (pts[0][1] + pts[1][1]) / 2), ((pts[1][0] + pts[2][0]) / 2, (pts[1][1] + pts[2][1]) / 2), ((pts[2][0] + pts[0][0]) / 2, (pts[2][1] + pts[0][1]) / 2)]
    allp = pts + mids
    P = []
    H = 390 + R + 10
    for t, tri in enumerate(tris):
        ox = t * 650
        P.append(f'<polygon points="{" ".join(f"{x + ox},{y}" for x, y in pts)}" fill="none" stroke="{NAVY}" stroke-width="3.4"/>')
        for (x, y), val in zip(allp, tri['values']):
            if val is None:
                P.append(f'<circle cx="{x + ox}" cy="{y}" r="{R}" fill="#fff" stroke="{NAVY}" stroke-width="3.4" stroke-dasharray="9 6"/>')
            else:
                P.append(f'<circle cx="{x + ox}" cy="{y}" r="{R}" fill="{SOFT}" stroke="{NAVY}" stroke-width="3.4"/>')
                P.append(T(x + ox, y + 12, val, 34))
        if tri.get('caption'):
            P.append(T(300 + ox, H + 30, tri['caption'], 32, weight=700))
    if any(t.get('caption') for t in tris):
        H += 44
    return wrap(P, 600 + (len(tris) - 1) * 650, H, 'magic triangle', w, 0.24)


FIGS = {'l2_bar': bar, 'l2_triangle': triangle}
