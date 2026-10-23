"""Extra figure types for Level 1 units 9 and 10 (length; puzzle day).

Plugged into figs.render() through the FIGS table.  Types:
  bars   rows of unit pieces laid end to end.  A row is {label, segs:[{n, w, gap?, overlap?}], start?, cuts?, note?}.
         A seg is n pieces, each w cubes wide (w=1 is a plain square cube; w>1 is a long rounded piece with a double
         border, so "clip", "stick" and "rod" differ from cubes by SHAPE, not colour).  `gap` (cubes) is blank space before the
         seg (used to show a measuring mistake); `overlap` pulls the seg left by that many cubes.  `start` shifts the whole row
         right by that many cubes.  `cuts` are positions (in cubes) of dashed cut lines.  `note` is text drawn after the row.
         `count` (bool, default false) numbers the cubes of a single-seg cube row 1, 2, 3...
  fence  posts in a row: {posts, label?}; label is written above the first gap
  ruler  a centimetre ruler (marks 0..max, numbers under the marks) with objects lying on top of it.  Objects are
         {label, start, end, hops?}; `hops` draws numbered hops between marks under the numbers (counting the spaces).
         About 1 cm on the drawing = 10 mm on paper when width_mm is left out, so a printed page is close to life size.
Palette: NAVY / TEAL / RED / SKY / SOFT / YEL only, so figs.recolour() gives the black-and-white print version (SKY / SOFT go white,
YEL becomes hatching).  Nothing depends on colour: pieces differ by shape and the printed labels.
"""
import figs as F

NAVY, TEAL, RED, SKY, SOFT, YEL = F.NAVY, F.TEAL, F.RED, F.SKY, F.SOFT, F.YEL
SW = 3.0


def _t(x, y, txt, size=28, fill=NAVY, anchor='middle', weight=800):
    return F._t(x, y, txt, size, fill, anchor, weight)


# ------------------------------------------------------------------------------------------------ bars
def bars(spec, w=None):
    U = 44                      # one cube
    LAB = 30 + 17 * max(len(r['label']) for r in spec['rows'])
    RH = 62
    rows = spec['rows']
    longest = 0
    for r in rows:
        x = r.get('start', 0)
        for s in r['segs']:
            x += s.get('gap', 0) - s.get('overlap', 0) + s['n'] * s.get('w', 1)
        longest = max(longest, x + (3.2 if r.get('note') else 0))
    W = LAB + longest * U + 12
    H = len(rows) * RH + 10
    P = []
    for i, r in enumerate(rows):
        y = 8 + i * RH
        P.append(_t(LAB - 14, y + 34, r['label'], 28, anchor='end'))
        x = LAB + r.get('start', 0) * U
        k = 0
        for s in r['segs']:
            x += (s.get('gap', 0) - s.get('overlap', 0)) * U
            pw = s.get('w', 1)
            for _ in range(s['n']):
                k += 1
                if pw == 1:
                    P.append(f'<rect x="{x:.1f}" y="{y}" width="{U}" height="{U}" fill="{SKY}" stroke="{NAVY}" stroke-width="{SW}"/>')
                    if r.get('count') and len(r['segs']) == 1:
                        P.append(_t(x + U / 2, y + 30, k, 22, weight=700))
                else:
                    P.append(f'<rect x="{x + 1.5:.1f}" y="{y}" width="{pw * U - 3:.1f}" height="{U}" rx="14" fill="{SOFT}" stroke="{NAVY}" stroke-width="{SW}"/>')
                    P.append(f'<rect x="{x + 8:.1f}" y="{y + 7}" width="{pw * U - 16:.1f}" height="{U - 14}" rx="9" fill="none" stroke="{NAVY}" stroke-width="1.8"/>')
                x += pw * U
        for c in r.get('cuts', []):
            cx = LAB + (r.get('start', 0) + c) * U
            P.append(f'<line x1="{cx:.1f}" y1="{y - 6}" x2="{cx:.1f}" y2="{y + U + 6}" stroke="{RED}" stroke-width="4" stroke-dasharray="7 5"/>')
        if r.get('note'):
            P.append(_t(x + 14, y + 33, r['note'], 26, anchor='start', weight=700))
    return F._wrap(''.join(P), W, H, 'bars of cubes', w or round(W * 0.2, 1))


# ------------------------------------------------------------------------------------------------ ruler
def ruler(spec, w=None):
    mx = spec.get('max', 12)
    CM = 48
    X0 = 36
    objs = spec.get('objects', [])
    OH = 50                     # object bar height
    gap = 16
    nobj = len(objs)
    hop = any(o.get('hops') for o in objs)
    top = 8
    ry = top + nobj * (OH + gap) + 4       # top of ruler
    RHt = 74
    W = X0 * 2 + mx * CM
    H = ry + RHt + (66 if hop else 12)
    P = []
    for i, o in enumerate(objs):
        y = top + i * (OH + gap)
        a, b = X0 + o['start'] * CM, X0 + o['end'] * CM
        P.append(f'<rect x="{a}" y="{y}" width="{b - a}" height="{OH}" rx="12" fill="{YEL}" stroke="{NAVY}" stroke-width="{SW + 0.6}"/>')
        P.append(f'<line x1="{a}" y1="{y + OH}" x2="{a}" y2="{ry}" stroke="{NAVY}" stroke-width="2" stroke-dasharray="4 4"/>')
        P.append(f'<line x1="{b}" y1="{y + OH}" x2="{b}" y2="{ry}" stroke="{NAVY}" stroke-width="2" stroke-dasharray="4 4"/>')
        if o.get('label'):
            lw = len(o['label']) * 15 + 18
            lx = (a + b) / 2
            P.append(f'<rect x="{lx - lw / 2}" y="{y + 8}" width="{lw}" height="{OH - 16}" rx="8" fill="#fff"/>')
            P.append(_t(lx, y + OH / 2 + 9, o['label'], 26, weight=800))
    P.append(f'<rect x="{X0 - 14}" y="{ry}" width="{mx * CM + 28}" height="{RHt}" rx="6" fill="{SOFT}" stroke="{NAVY}" stroke-width="{SW}"/>')
    for m in range(mx + 1):
        x = X0 + m * CM
        P.append(f'<line x1="{x}" y1="{ry}" x2="{x}" y2="{ry + 30}" stroke="{NAVY}" stroke-width="3"/>')
        if m < mx:
            P.append(f'<line x1="{x + CM / 2}" y1="{ry}" x2="{x + CM / 2}" y2="{ry + 16}" stroke="{NAVY}" stroke-width="2"/>')
        P.append(_t(x, ry + 62, m, 26, weight=700))
    for o in objs:
        if not o.get('hops'):
            continue
        for k in range(o['end'] - o['start']):
            a = X0 + (o['start'] + k) * CM + 5
            b = X0 + (o['start'] + k + 1) * CM - 5
            yb = ry + RHt + 6
            P.append(f'<path d="M{a},{yb} Q{(a + b) / 2},{yb + 36} {b},{yb}" fill="none" stroke="{TEAL}" stroke-width="3.4" stroke-linecap="round"/>')
            P.append(_t((a + b) / 2, yb + 54, k + 1, 22, TEAL, weight=800))
    return F._wrap(''.join(P), W, H, 'centimetre ruler', w or round(W * 10 / CM, 1))


# ------------------------------------------------------------------------------------------------ fence
def fence(spec, w=None):
    """A row of fence posts with equal gaps.  spec: posts (count), label (text written once above the first gap, e.g. "3 cubes")."""
    n = spec['posts']
    SP = 92
    W = 40 + (n - 1) * SP + 40
    H = 168
    P = []
    for y in (66, 96):
        P.append(f'<line x1="26" y1="{y + 22}" x2="{W - 26}" y2="{y + 22}" stroke="{NAVY}" stroke-width="3.4"/>')
    for i in range(n):
        x = 40 + i * SP
        P.append(f'<rect x="{x - 9}" y="46" width="18" height="86" rx="6" fill="{SOFT}" stroke="{NAVY}" stroke-width="{SW}"/>')
    if spec.get('label'):
        P.append(f'<path d="M40,44 L40,32 L{40 + SP},32 L{40 + SP},44" fill="none" stroke="{NAVY}" stroke-width="2.6"/>')
        P.append(_t(40 + SP / 2, 24, spec['label'], 24, weight=700))
    return F._wrap(''.join(P), W, H, 'fence posts', w or round(W * 0.2, 1))


FIGS = {'bars': bars, 'ruler': ruler, 'fence': fence}
