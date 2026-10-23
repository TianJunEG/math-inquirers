"""Level 4 figure plug-in: figures with square corners on a grid (area and perimeter, symmetry, nets).

Types:
  l4_poly   shapes [{pts:[[x,y],..] (grid units, y down), labels:[{seg, text, in?}], dashed:[[[x1,y1],[x2,y2]],..], fill?, grid?, texts:[{x,y,text}], ox, oy}],
            cell (drawing units per grid unit).  `labels` write a text beside edge number seg (from pts[seg] to pts[seg+1]), outside the shape unless in=True.
            fill: 'sky' (default, prints white), 'hatch' (shaded) or 'none'.  grid draws the unit squares inside (thin lines).
  l4_tiles  tiles: for each named shape a list of [col,row] cells; drawn as joined unit squares with full borders (a shape of tiles); shapes laid in a row with gaps.
"""
import figs as F

NAVY, TEAL, RED, SKY, SOFT, YEL = F.NAVY, F.TEAL, F.RED, F.SKY, F.SOFT, F.YEL


def _t(x, y, txt, size=26, fill=NAVY, anchor='middle', weight=700):
    return F._t(round(x, 1), round(y, 1), txt, size, fill, anchor, weight)


def _esc(s):
    return str(s).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def _inside(px, py, pts):
    inside = False
    n = len(pts)
    for i in range(n):
        x1, y1 = pts[i]
        x2, y2 = pts[(i + 1) % n]
        if (y1 > py) != (y2 > py):
            xi = x1 + (py - y1) * (x2 - x1) / (y2 - y1)
            if xi > px:
                inside = not inside
    return inside


def l4_poly(spec, w=None):
    c = spec.get('cell', 36)
    P = []
    maxx = maxy = 0
    minx = miny = 0
    fs = spec.get('font', 26)
    padx = spec.get('padx', 96)
    pady = spec.get('pady', 48)
    for sh in spec['shapes']:
        pts = sh['pts']
        ox, oy = sh.get('ox', 0) * c + padx, sh.get('oy', 0) * c + pady
        xs = [ox + x * c for x, y in pts]
        ys = [oy + y * c for x, y in pts]
        maxx = max(maxx, max(xs) + padx)
        maxy = max(maxy, max(ys) + pady)
        fill = {'sky': SKY, 'hatch': YEL, 'none': 'none'}[sh.get('fill', 'sky')]
        d = 'M' + ' L'.join(f'{x:.1f},{y:.1f}' for x, y in zip(xs, ys)) + ' Z'
        if sh.get('hole'):
            hp = sh['hole']
            hx = [ox + x * c for x, y in hp]
            hy = [oy + y * c for x, y in hp]
            d += ' M' + ' L'.join(f'{x:.1f},{y:.1f}' for x, y in zip(hx, hy)) + ' Z'
            P.append(f'<path d="{d}" fill="{fill}" fill-rule="evenodd" stroke="{NAVY}" stroke-width="4" stroke-linejoin="round"/>')
        else:
            P.append(f'<path d="{d}" fill="{fill}" stroke="{NAVY}" stroke-width="4" stroke-linejoin="round"/>')
        if sh.get('grid'):
            gx0, gx1 = int(min(x for x, y in pts)), int(max(x for x, y in pts))
            gy0, gy1 = int(min(y for x, y in pts)), int(max(y for x, y in pts))
            for gx in range(gx0, gx1):
                for gy in range(gy0, gy1):
                    if _inside(gx + 0.5, gy + 0.5, pts) and not (sh.get('hole') and _inside(gx + 0.5, gy + 0.5, sh['hole'])):
                        P.append(f'<rect x="{ox + gx * c}" y="{oy + gy * c}" width="{c}" height="{c}" fill="none" stroke="{NAVY}" stroke-width="1.4"/>')
        for seg in sh.get('dashed', []):
            (x1, y1), (x2, y2) = seg
            P.append(f'<line x1="{ox + x1 * c:.1f}" y1="{oy + y1 * c:.1f}" x2="{ox + x2 * c:.1f}" y2="{oy + y2 * c:.1f}" stroke="{NAVY}" stroke-width="3.4" stroke-dasharray="11 8"/>')
        def put(ptlist, lab, inward):
            n = len(ptlist)
            (x1, y1), (x2, y2) = ptlist[lab['seg']], ptlist[(lab['seg'] + 1) % n]
            mx, my = (x1 + x2) / 2, (y1 + y2) / 2
            dx, dy = x2 - x1, y2 - y1
            ln = (dx * dx + dy * dy) ** 0.5
            nx, ny = dy / ln, -dx / ln
            if _inside(mx + nx * 0.05, my + ny * 0.05, ptlist) != inward:
                nx, ny = -nx, -ny
            off = lab.get('off', 30 if abs(ny) > abs(nx) else 12 + 9 * len(str(lab['text'])))
            tx, ty = ox + mx * c + nx * off, oy + my * c + ny * off
            P.append(_t(tx, ty + fs * 0.35, _esc(lab['text']), fs, weight=800))
        for lab in sh.get('labels', []):
            put(pts, lab, bool(lab.get('in', False)))
        for lab in sh.get('hole_labels', []):
            put(sh['hole'], lab, not lab.get('out', False))
        for t in sh.get('texts', []):
            P.append(_t(ox + t['x'] * c, oy + t['y'] * c + fs * 0.35, _esc(t['text']), t.get('size', fs), weight=800))
    return F._wrap(''.join(P), maxx, maxy, spec.get('label', 'figure'), w or spec.get('width_mm', 100))


def l4_tiles(spec, w=None):
    c = spec.get('cell', 46)
    gap = spec.get('gap', 1.2)
    P = []
    x0 = 12
    H = 0
    for sh in spec['shapes']:
        cells = sh['cells']
        mx = min(x for x, y in cells)
        my = min(y for x, y in cells)
        wd = max(x for x, y in cells) - mx + 1
        ht = max(y for x, y in cells) - my + 1
        for (x, y) in cells:
            P.append(f'<rect x="{x0 + (x - mx) * c:.1f}" y="{10 + (y - my) * c:.1f}" width="{c}" height="{c}" fill="{YEL if sh.get("shade", True) else SKY}" stroke="{NAVY}" stroke-width="3.4"/>')
        if sh.get('name'):
            P.append(_t(x0 + wd * c / 2, 10 + ht * c + 40, _esc(sh['name']), 28, weight=800))
        H = max(H, 10 + ht * c + (56 if sh.get('name') else 14))
        x0 += wd * c + gap * c
    return F._wrap(''.join(P), x0 - gap * c + 12, H, spec.get('label', 'shapes made of square tiles'), w or spec.get('width_mm', 140))


FIGS = {'l4_poly': l4_poly, 'l4_tiles': l4_tiles}
