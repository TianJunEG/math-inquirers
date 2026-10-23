"""Level 5 geometry figure: l5_poly (polygons, lines, labels, angle arcs, right-angle marks, grids).  Coordinates are maths coordinates (y up).

spec = {
  type: 'l5_poly', width_mm: 120,
  pts:   {A: [x, y], ...}                          points (any real numbers; the drawing is scaled to fit width_mm)
  polys: [{v: ['A','B','C'], fill: 'shade'|'light'|None, dash: False, w: 3}]
  lines: [{a: 'A', b: 'B', dash: True, w: 2.4}]    extra segments (heights, cuts)
  vlab:  {A: 'bl', ...} or True                    vertex letters; position 'tl','t','tr','l','r','bl','b','br' (default: away from the centre)
  dims:  [{a, b, text, off: 1|-1, line: True}]     length labels beside a side (line: also a dimension line); off=-1 flips the side
  texts: [{t: 'P', at: [x, y], size: 22}]          free text at a point (maths coordinates)
  angles:[{at, a, b, text, r: 34, reflex: False}]  arc at vertex `at` between the rays to `a` and `b`, label `text` (use '?' for unknown)
  rights:[{at, a, b}]                              right-angle square mark
  ticks: [[A, B, n]]                               n small equal-length marks on side AB
  par:   [[A, B, n]]                               n arrowheads on side AB (parallel lines)
  grid:  {x0, y0, x1, y1, step: 1}                 light square grid behind the figure (1 unit = one square)
  dots:  [{at: 'A' or [x, y], r: 6, fill: 'shade'}]
}
Palette NAVY / TEAL / YEL / SKY / SOFT only; shaded = YEL (hatching in print), light = SOFT.  All meaning is also given by letters and labels.
"""
import math
import figs as F

NAVY, TEAL, YEL, SKY, SOFT, GREY = F.NAVY, F.TEAL, F.YEL, F.SKY, F.SOFT, F.GREY
U = 4.0
FILL = {'shade': YEL, 'light': SOFT, 'sky': SKY, None: 'none'}


def _t(x, y, txt, size=22, fill=NAVY, anchor='middle', weight=800):
    return F._t(round(x, 1), round(y, 1), txt, size, fill, anchor, weight)


def poly(spec, w=None):
    wmm = w or spec.get('width_mm') or 120
    pts = {k: tuple(map(float, v)) for k, v in spec['pts'].items()}
    allp = list(pts.values())
    g = spec.get('grid')
    if g:
        allp += [(g['x0'], g['y0']), (g['x1'], g['y1'])]
    for t in spec.get('texts', []):
        allp.append(tuple(t['at']))
    xs, ys = [p[0] for p in allp], [p[1] for p in allp]
    xmin, xmax, ymin, ymax = min(xs), max(xs), min(ys), max(ys)
    padx = spec.get('padx', 56)
    pady = spec.get('pady', 46)
    padb = spec.get('padb', 66)
    Wd = wmm * U
    s = spec.get('scale') or (Wd - 2 * padx) / max(xmax - xmin, 1e-9)
    if spec.get('scale'):
        Wd = (xmax - xmin) * s + 2 * padx
    H = (ymax - ymin) * s + pady + padb
    X = lambda x: padx + (x - xmin) * s
    Y = lambda y: pady + (ymax - y) * s
    P = lambda name: (X(pts[name][0]), Y(pts[name][1]))
    cx = sum(X(p[0]) for p in pts.values()) / len(pts)
    cy = sum(Y(p[1]) for p in pts.values()) / len(pts)
    out = []
    for pl in spec.get('polys', []):
        pp = ' '.join(f'{P(n)[0]:.1f},{P(n)[1]:.1f}' for n in pl['v'])
        if FILL[pl.get('fill')] != 'none':
            out.append(f'<polygon points="{pp}" fill="{FILL[pl.get("fill")]}" stroke="none"/>')
    if g:
        st = g.get('step', 1)
        x = g['x0']
        while x <= g['x1'] + 1e-9:
            out.append(f'<line x1="{X(x):.1f}" y1="{Y(g["y0"]):.1f}" x2="{X(x):.1f}" y2="{Y(g["y1"]):.1f}" stroke="{NAVY}" stroke-width="1.3" stroke-dasharray="2 6"/>')
            x += st
        y = g['y0']
        while y <= g['y1'] + 1e-9:
            out.append(f'<line x1="{X(g["x0"]):.1f}" y1="{Y(y):.1f}" x2="{X(g["x1"]):.1f}" y2="{Y(y):.1f}" stroke="{NAVY}" stroke-width="1.3" stroke-dasharray="2 6"/>')
            y += st
    for pl in spec.get('polys', []):
        pp = ' '.join(f'{P(n)[0]:.1f},{P(n)[1]:.1f}' for n in pl['v'])
        dash = ' stroke-dasharray="10 7"' if pl.get('dash') else ''
        out.append(f'<polygon points="{pp}" fill="none" stroke="{NAVY}" stroke-width="{pl.get("w", 3)}" stroke-linejoin="round"{dash}/>')
    for ln in spec.get('lines', []):
        (x1, y1), (x2, y2) = P(ln['a']), P(ln['b'])
        dash = ' stroke-dasharray="10 7"' if ln.get('dash', True) else ''
        out.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{NAVY}" stroke-width="{ln.get("w", 2.6)}"{dash}/>')
    for r in spec.get('rights', []):
        (ax, ay), (bx, by), (cx_, cy_) = P(r['at']), P(r['a']), P(r['b'])
        d1 = _unit(bx - ax, by - ay); d2 = _unit(cx_ - ax, cy_ - ay)
        k = r.get('size', 22)
        p1 = (ax + d1[0] * k, ay + d1[1] * k); p2 = (ax + (d1[0] + d2[0]) * k, ay + (d1[1] + d2[1]) * k); p3 = (ax + d2[0] * k, ay + d2[1] * k)
        out.append(f'<polyline points="{p1[0]:.1f},{p1[1]:.1f} {p2[0]:.1f},{p2[1]:.1f} {p3[0]:.1f},{p3[1]:.1f}" fill="none" stroke="{NAVY}" stroke-width="2.4"/>')
    for t in spec.get('ticks', []):
        (x1, y1), (x2, y2) = P(t[0]), P(t[1])
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        d = _unit(x2 - x1, y2 - y1); nrm = (-d[1], d[0])
        n = t[2]
        for i in range(n):
            o = (i - (n - 1) / 2) * 9
            px, py = mx + d[0] * o, my + d[1] * o
            out.append(f'<line x1="{px - nrm[0] * 9:.1f}" y1="{py - nrm[1] * 9:.1f}" x2="{px + nrm[0] * 9:.1f}" y2="{py + nrm[1] * 9:.1f}" stroke="{NAVY}" stroke-width="2.6"/>')
    for t in spec.get('par', []):
        (x1, y1), (x2, y2) = P(t[0]), P(t[1])
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        d = _unit(x2 - x1, y2 - y1); nrm = (-d[1], d[0])
        for i in range(t[2]):
            o = (i - (t[2] - 1) / 2) * 11
            px, py = mx + d[0] * o, my + d[1] * o
            out.append(f'<polyline points="{px - d[0] * 7 + nrm[0] * 8:.1f},{py - d[1] * 7 + nrm[1] * 8:.1f} {px + d[0] * 7:.1f},{py + d[1] * 7:.1f} {px - d[0] * 7 - nrm[0] * 8:.1f},{py - d[1] * 7 - nrm[1] * 8:.1f}" fill="none" stroke="{NAVY}" stroke-width="2.4"/>')
    for a in spec.get('angles', []):
        ax, ay = P(a['at'])
        ta = math.atan2(-(P(a['a'])[1] - ay), P(a['a'])[0] - ax)     # maths angle of the ray to a
        tb = math.atan2(-(P(a['b'])[1] - ay), P(a['b'])[0] - ax)
        d = (tb - ta) % (2 * math.pi)
        s0 = ta
        if a.get('reflex'):
            if d < math.pi:
                s0, d = tb, 2 * math.pi - d
        elif d > math.pi:
            s0, d = tb, 2 * math.pi - d
        r = a.get('r', 34)
        x1, y1 = ax + r * math.cos(s0), ay - r * math.sin(s0)
        x2, y2 = ax + r * math.cos(s0 + d), ay - r * math.sin(s0 + d)
        large = 1 if d > math.pi else 0
        out.append(f'<path d="M{x1:.1f},{y1:.1f} A{r},{r} 0 {large} 0 {x2:.1f},{y2:.1f}" fill="{"#fff" if a.get("clear") else "none"}" stroke="{NAVY}" stroke-width="2.6"/>')
        if a.get('text') is not None:
            mid = s0 + d / 2
            rr = a.get('tr', r + 24)
            out.append(_t(ax + rr * math.cos(mid), ay - rr * math.sin(mid) + 8, a['text'], a.get('size', 22)))
    for dm in spec.get('dims', []):
        (x1, y1), (x2, y2) = P(dm['a']), P(dm['b'])
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        d = _unit(x2 - x1, y2 - y1)
        nrm = (-d[1], d[0])
        if (mx - cx) * nrm[0] + (my - cy) * nrm[1] < 0:
            nrm = (-nrm[0], -nrm[1])
        nrm = (nrm[0] * dm.get('off', 1), nrm[1] * dm.get('off', 1))
        off = dm.get('dist', 26 if not dm.get('line') else 22)
        if dm.get('line'):
            ox, oy = nrm[0] * 16, nrm[1] * 16
            out.append(f'<line x1="{x1 + ox:.1f}" y1="{y1 + oy:.1f}" x2="{x2 + ox:.1f}" y2="{y2 + oy:.1f}" stroke="{NAVY}" stroke-width="2"/>')
            for (px, py) in ((x1, y1), (x2, y2)):
                out.append(f'<line x1="{px + ox - nrm[0] * 7:.1f}" y1="{py + oy - nrm[1] * 7:.1f}" x2="{px + ox + nrm[0] * 7:.1f}" y2="{py + oy + nrm[1] * 7:.1f}" stroke="{NAVY}" stroke-width="2"/>')
            off = 38
        tx, ty = mx + nrm[0] * off, my + nrm[1] * off
        out.append(_t(tx, ty + 8, dm['text'], dm.get('size', 22)))
    for t in spec.get('texts', []):
        out.append(_t(X(t['at'][0]), Y(t['at'][1]) + 8, t['t'], t.get('size', 22), weight=800))
    vl = spec.get('vlab', True)
    if vl:
        place = vl if isinstance(vl, dict) else {}
        for name in pts:
            if isinstance(vl, dict) and name not in vl:
                continue
            x, y = P(name)
            pos = place.get(name)
            if pos is None:
                d = _unit(x - cx, y - cy)
                dx, dy = d[0] * 26, d[1] * 26 + 8
                anchor = 'middle'
            else:
                dxm = {'l': -26, 'r': 26, 't': 0, 'b': 0, 'tl': -22, 'tr': 22, 'bl': -22, 'br': 22}
                dym = {'l': 8, 'r': 8, 't': -22, 'b': 34, 'tl': -18, 'tr': -18, 'bl': 30, 'br': 30}
                dx, dy = dxm[pos], dym[pos]
                anchor = 'middle'
            out.append(_t(x + dx, y + dy, name, 24, TEAL if spec.get('tealv') else NAVY))
    for d in spec.get('dots', []):
        x, y = (P(d['at']) if isinstance(d['at'], str) else (X(d['at'][0]), Y(d['at'][1])))
        out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{d.get("r", 6)}" fill="{FILL[d.get("fill", "shade")]}" stroke="{NAVY}" stroke-width="2"/>')
    return F._wrap(''.join(out), round(Wd, 1), round(H, 1), spec.get('alt', 'geometry figure'), wmm)


def _unit(dx, dy):
    n = math.hypot(dx, dy) or 1
    return dx / n, dy / n


FIGS = {'l5_poly': poly}
