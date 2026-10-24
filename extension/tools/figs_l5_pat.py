"""Level 5 pattern figure: l5_pat, a row of figures (panels) made of sticks, tiles, dots and chairs.

spec = {type: 'l5_pat', mm: 9 (mm per grid unit), gap: 1.2 (units between panels), label: 'Figure' (title under each panel, with its number),
        panels: [{segs: [[x1, y1, x2, y2], ...],        matchsticks (y up)
                  cells: [[col, row], [col, row, 's'], ...],   unit tiles; 's' = shaded tile
                  dots: [[x, y], ...],                  round dots of 0.55 units
                  chairs: [[x, y], ...],                small circles of 0.7 units (chairs)
                  title: 'Figure 4'  (optional, replaces the automatic title),
                  blank: [w, h]  (a dashed empty frame of that size in units, for the child to draw in)}]}
Palette NAVY / SOFT / SKY / YEL only: tiles are white (SKY), shaded tiles hatched in print (YEL); sticks are black lines with round ends.
"""
import figs as F

NAVY, YEL, SKY, SOFT = F.NAVY, F.YEL, F.SKY, F.SOFT
U = 4.0


def pat(spec, w=None):
    mm = spec.get('mm', 9)
    s = mm * U
    gap = spec.get('gap', 1.3) * s
    panels = spec['panels']
    boxes = []
    for p in panels:
        xs, ys = [], []
        for x1, y1, x2, y2 in p.get('segs', []):
            xs += [x1, x2]; ys += [y1, y2]
        for c in p.get('cells', []):
            xs += [c[0], c[0] + 1]; ys += [c[1], c[1] + 1]
        for x, y in p.get('dots', []):
            xs += [x - .3, x + .3]; ys += [y - .3, y + .3]
        for x, y in p.get('chairs', []):
            xs += [x - .4, x + .4]; ys += [y - .4, y + .4]
        if p.get('blank'):
            xs += [0, p['blank'][0]]; ys += [0, p['blank'][1]]
        lo, hi = min(xs), max(xs)
        if hi - lo < 3.6:           # keep room for the title
            d = (3.6 - (hi - lo)) / 2
            lo, hi = lo - d, hi + d
        boxes.append((lo, hi, min(ys), max(ys)))
    top = max(b[3] - b[2] for b in boxes)
    out = []
    x0 = 10
    H = top * s + 70
    for i, (p, (xa, xb, ya, yb)) in enumerate(zip(panels, boxes), 1):
        ox = x0 - xa * s
        base = 14 + top * s             # the bottoms of all panels sit on one line
        X = lambda x, ox=ox: ox + x * s
        Y = lambda y, ya=ya, base=base: base - (y - ya) * s
        if p.get('blank'):
            bw_, bh_ = p['blank']
            out.append(f'<rect x="{X(0):.1f}" y="{Y(bh_):.1f}" width="{bw_ * s:.1f}" height="{bh_ * s:.1f}" rx="8" fill="#fff" stroke="{NAVY}" stroke-width="2.6" stroke-dasharray="9 6"/>')
        for c in p.get('cells', []):
            fill = YEL if len(c) > 2 and c[2] == 's' else SKY
            out.append(f'<rect x="{X(c[0]):.1f}" y="{Y(c[1] + 1):.1f}" width="{s:.1f}" height="{s:.1f}" fill="{fill}" stroke="{NAVY}" stroke-width="2.6"/>')
        for x1, y1, x2, y2 in p.get('segs', []):
            out.append(f'<line x1="{X(x1):.1f}" y1="{Y(y1):.1f}" x2="{X(x2):.1f}" y2="{Y(y2):.1f}" stroke="{NAVY}" stroke-width="4.2" stroke-linecap="round"/>')
        for x, y in p.get('dots', []):
            out.append(f'<circle cx="{X(x):.1f}" cy="{Y(y):.1f}" r="{0.28 * s:.1f}" fill="{YEL}" stroke="{NAVY}" stroke-width="2.4"/>')
        for x, y in p.get('chairs', []):
            out.append(f'<circle cx="{X(x):.1f}" cy="{Y(y):.1f}" r="{0.34 * s:.1f}" fill="#fff" stroke="{NAVY}" stroke-width="2.6"/>')
        title = p.get('title') or f'{spec.get("label", "Figure")} {i}'
        wpx = (xb - xa) * s
        out.append(F._t(round(x0 + wpx / 2, 1), round(H - 18, 1), title, 20, NAVY, 'middle', 800))
        x0 += wpx + gap
    W = x0 - gap + 10
    return F._wrap(''.join(out), round(W, 1), round(H, 1), spec.get('alt', 'growing pattern'), round(W / U, 1))


FIGS = {'l5_pat': pat}
