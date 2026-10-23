"""Level 4 figure plug-in: angle and turn figures (angles, protractor, fan of rays, compass, clock faces, corner of a square).

Types (project palette only; no colour carries meaning):
  l4_angle    angles [{d1, d2, label}] each drawn as two long arms from a vertex (degrees counter-clockwise from the right-hand direction),
              cols, len (arm length in drawing units).  Arms are drawn long enough to put a protractor on.
  l4_proto    a 180-degree protractor with an angle on it: angle (the size), flip (False: baseline on the right, 0 on the right; True: baseline on the left),
              the two scales are numbered every 10 degrees.
  l4_fan      rays [{d, label}] from a point O; arcs [{i, j, text}] marks the angle between ray i and ray j (text may be '?').
  l4_compass  8-point compass; start (a direction word) draws a "facing" arrow; ring [directions] circles directions.
  l4_clock    clocks [{h, m, cap?}], r (radius).
  l4_corner   figs [{parts:[{deg, text}], len?}]  a square corner (90 degrees) split by rays into the given parts, each part labelled.
"""
import math
import figs as F

NAVY, TEAL, RED, SKY, SOFT, YEL = F.NAVY, F.TEAL, F.RED, F.SKY, F.SOFT, F.YEL


def _t(x, y, txt, size=26, fill=NAVY, anchor='middle', weight=700):
    return F._t(round(x, 1), round(y, 1), txt, size, fill, anchor, weight)


def _pt(cx, cy, r, deg):
    a = math.radians(deg)
    return cx + r * math.cos(a), cy - r * math.sin(a)


def _arc(cx, cy, r, d1, d2, width=3.4, dash=''):
    x1, y1 = _pt(cx, cy, r, d1)
    x2, y2 = _pt(cx, cy, r, d2)
    large = 1 if abs(d2 - d1) > 180 else 0
    sweep = 0 if d2 > d1 else 1
    return f'<path d="M{x1:.1f},{y1:.1f} A{r},{r} 0 {large} {sweep} {x2:.1f},{y2:.1f}" fill="none" stroke="{NAVY}" stroke-width="{width}"{dash}/>'


def _line(x1, y1, x2, y2, w=4, dash=''):
    return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{NAVY}" stroke-width="{w}" stroke-linecap="round"{dash}/>'


# ------------------------------------------------------------------------------------------------ angles
def l4_angle(spec, w=None):
    angs = spec['angles']
    cols = spec.get('cols', 2)
    L = spec.get('len', 190)
    cw = L + 50
    top = max(math.sin(math.radians(max(a['d1'], a['d2']))) for a in angs)
    ch = int(L * max(top, 0.6)) + 70
    rows = (len(angs) + cols - 1) // cols
    P = []
    for i, a in enumerate(angs):
        r, c = divmod(i, cols)
        ox = c * cw + a.get('ox', 28)
        oy = r * ch + ch - 40
        for d in (a['d1'], a['d2']):
            x, y = _pt(ox, oy, L, d)
            P.append(_line(ox, oy, x, y, 4.6))
        P.append(f'<circle cx="{ox}" cy="{oy}" r="6" fill="{NAVY}"/>')
        lo, hi = sorted((a['d1'], a['d2']))
        P.append(_arc(ox, oy, 34, lo, hi, 3))
        P.append(_t(ox - 4, oy + 34, _esc(a.get('label', '')), 28, anchor='middle', weight=800) if a.get('label') else '')
    return F._wrap(''.join(P), cols * cw, rows * ch, spec.get('label', 'angles'), w or spec.get('width_mm', 150))


def _esc(s):
    return str(s).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


# ------------------------------------------------------------------------------------------------ protractor
def _halo(x, y, txt, size, weight=700, anchor='middle'):
    """Text with a white outline so that a line passing behind it does not strike the digits through."""
    return (f'<text x="{round(x, 1)}" y="{round(y, 1)}" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" fill="{NAVY}" '
            f'stroke="#fff" stroke-width="7" paint-order="stroke" stroke-linejoin="round" font-family="{F.FONT}">{txt}</text>')


def l4_proto(spec, w=None):
    R = 250
    pad = 62
    cx, cy = R + pad + 20, R + 78
    ang = spec['angle']
    flip = spec.get('flip', False)
    step = spec.get('label_step', 20)
    W, H = 2 * (R + pad + 20), R + 78 + 70
    P = []
    P.append(f'<path d="M{cx - R - 18},{cy} A{R + 18},{R + 18} 0 0 1 {cx + R + 18},{cy} Z" fill="#fff" stroke="{NAVY}" stroke-width="3.4"/>')
    base_deg = 180 if flip else 0
    arm_deg = 180 - ang if flip else ang
    # the two arms first (the numbers are drawn on top with a white outline)
    bx, by = _pt(cx, cy, R + 70, base_deg)
    ax, ay = _pt(cx, cy, R + 70, arm_deg)
    P.append(_line(cx, cy, bx, by, 5))
    P.append(_line(cx, cy, ax, ay, 5))
    for d in range(0, 181):
        long_ = 22 if d % 10 == 0 else 15 if d % 5 == 0 else 8
        x1, y1 = _pt(cx, cy, R, d)
        x2, y2 = _pt(cx, cy, R - long_, d)
        P.append(_line(x1, y1, x2, y2, 2.6 if d % 10 == 0 else 1.6))
        if d % step == 0:
            xo, yo = _pt(cx, cy, R + 34, d)          # outer scale, 0 on the right (printed outside the rim)
            xi, yi = _pt(cx, cy, R - 52, d)          # inner scale, 0 on the left
            P.append(_halo(xo, yo + 8, str(d), 24, 800))
            P.append(_halo(xi, yi + 8, str(180 - d), 22, 600))
    P.append(f'<circle cx="{cx}" cy="{cy}" r="8" fill="{NAVY}"/>')
    # the angle: an arc between the two arms
    lo, hi = sorted((base_deg, arm_deg))
    P.append(_arc(cx, cy, 100, lo, hi, 5))
    return F._wrap(''.join(P), W, H, spec.get('label', 'protractor'), w or spec.get('width_mm', 120))


# ------------------------------------------------------------------------------------------------ fan
def l4_fan(spec, w=None):
    rays = spec['rays']
    L = spec.get('len', 330)
    xs = [L * math.cos(math.radians(r['d'])) for r in rays]
    ys = [L * math.sin(math.radians(r['d'])) for r in rays]
    ox = 60 + max(0, -min(xs)) + 10
    oy = 60 + max(ys)
    W = ox + max(max(xs), 0) + 70
    H = oy + 70
    P = []
    for r in rays:
        x, y = _pt(ox, oy, L, r['d'])
        P.append(_line(ox, oy, x, y, 4.6))
        lx, ly = _pt(ox, oy, L + 30, r['d'])
        P.append(_t(lx + 6, ly + 8, _esc(r['label']), 30, weight=800))
    P.append(f'<circle cx="{ox}" cy="{oy}" r="7" fill="{NAVY}"/>')
    P.append(_t(ox - 22, oy + 36, 'O', 30, weight=800))
    for k, a in enumerate(spec.get('arcs', [])):
        d1, d2 = rays[a['i']]['d'], rays[a['j']]['d']
        r = 90 + 44 * k if spec.get('stack', True) else 110
        P.append(_arc(ox, oy, r, min(d1, d2), max(d1, d2), 3))
        mx, my = _pt(ox, oy, r + 4, (d1 + d2) / 2)
        P.append(_halo(mx, my + 10, _esc(a['text']), 30, 800))
    return F._wrap(''.join(P), W, H, spec.get('label', 'rays from a point'), w or spec.get('width_mm', 100))


# ------------------------------------------------------------------------------------------------ compass
DIRS = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']


def l4_compass(spec, w=None):
    R = 170
    cx = cy = 220
    P = [f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="#fff" stroke="{NAVY}" stroke-width="3.4"/>']
    for k, d in enumerate(DIRS):
        deg = 90 - 45 * k
        x1, y1 = _pt(cx, cy, 24 if False else 0, deg)
        x2, y2 = _pt(cx, cy, R, deg)
        P.append(_line(cx, cy, x2, y2, 2.4 if k % 2 else 3.4))
        lx, ly = _pt(cx, cy, R + 34, deg)
        P.append(_t(lx, ly + 10, d, 30 if k % 2 == 0 else 26, weight=800))
    for d in spec.get('ring', []):
        k = DIRS.index(d)
        x, y = _pt(cx, cy, R, 90 - 45 * k)
        P.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="15" fill="none" stroke="{NAVY}" stroke-width="4"/>')
    if spec.get('start'):
        k = DIRS.index(spec['start'])
        x, y = _pt(cx, cy, R - 24, 90 - 45 * k)
        P.append(_line(cx, cy, x, y, 9))
        hx, hy = _pt(cx, cy, R - 2, 90 - 45 * k)
        a1x, a1y = _pt(hx, hy, 34, 90 - 45 * k + 160)
        a2x, a2y = _pt(hx, hy, 34, 90 - 45 * k - 160)
        P.append(f'<polygon points="{hx:.1f},{hy:.1f} {a1x:.1f},{a1y:.1f} {a2x:.1f},{a2y:.1f}" fill="{NAVY}"/>')
    P.append(f'<circle cx="{cx}" cy="{cy}" r="11" fill="{NAVY}"/>')
    return F._wrap(''.join(P), 440, 440, spec.get('label', 'compass'), w or spec.get('width_mm', 62))


# ------------------------------------------------------------------------------------------------ clocks
def l4_clock(spec, w=None):
    clocks = spec['clocks']
    R = spec.get('r', 130)
    gap = 36
    cw = 2 * R + 30
    W = len(clocks) * cw + (len(clocks) - 1) * gap
    H = 2 * R + 30 + (46 if any(c.get('cap') for c in clocks) else 0)
    P = []
    for i, c in enumerate(clocks):
        cx = i * (cw + gap) + cw / 2
        cy = R + 15
        P.append(f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="#fff" stroke="{NAVY}" stroke-width="4"/>')
        for k in range(60):
            deg = 90 - 6 * k
            long_ = 14 if k % 5 == 0 else 6
            x1, y1 = _pt(cx, cy, R - 3, deg)
            x2, y2 = _pt(cx, cy, R - 3 - long_, deg)
            P.append(_line(x1, y1, x2, y2, 3 if k % 5 == 0 else 1.5))
        for k in range(1, 13):
            x, y = _pt(cx, cy, R - 42, 90 - 30 * k)
            P.append(_t(x, y + 9, k, 26, weight=700))
        if 'h' in c:
            hh = (c['h'] % 12) * 30 + c['m'] * 0.5
            mm = c['m'] * 6
            hx, hy = _pt(cx, cy, R * 0.5, 90 - hh)
            mx, my = _pt(cx, cy, R * 0.78, 90 - mm)
            P.append(_line(cx, cy, hx, hy, 9))
            P.append(_line(cx, cy, mx, my, 5))
        P.append(f'<circle cx="{cx}" cy="{cy}" r="8" fill="{NAVY}"/>')
        if c.get('cap'):
            P.append(_t(cx, 2 * R + 30 + 30, _esc(c['cap']), 28, weight=800))
    return F._wrap(''.join(P), W, H, spec.get('label', 'clock faces'), w or spec.get('width_mm', 110))


# ------------------------------------------------------------------------------------------------ corner of a square
def l4_corner(spec, w=None):
    figs = spec['figs']
    L = spec.get('len', 250)
    cw = L + 80
    W = len(figs) * cw
    H = L + 70
    P = []
    for i, f in enumerate(figs):
        ox, oy = i * cw + 40, L + 30
        P.append(_line(ox, oy, ox + L, oy, 4.6))
        P.append(_line(ox, oy, ox, oy - L, 4.6))
        P.append(f'<path d="M{ox + 26},{oy} L{ox + 26},{oy - 26} L{ox},{oy - 26}" fill="none" stroke="{NAVY}" stroke-width="3"/>')
        tot = 0
        cum = [0]
        for p in f['parts']:
            tot += p['deg']
            cum.append(tot)
        for d in cum[1:-1]:
            x, y = _pt(ox, oy, L, d)
            P.append(_line(ox, oy, x, y, 3.6))
        for k, p in enumerate(f['parts']):
            mid = (cum[k] + cum[k + 1]) / 2
            r = L * (0.82 if k % 2 == 0 else 0.62)
            tx, ty = _pt(ox, oy, r, mid)
            P.append(_halo(tx, ty + 10, _esc(p['text']), 28, 800))
    return F._wrap(''.join(P), W, H, spec.get('label', 'corners'), w or spec.get('width_mm', 140))


FIGS = {'l4_angle': l4_angle, 'l4_proto': l4_proto, 'l4_fan': l4_fan, 'l4_compass': l4_compass, 'l4_clock': l4_clock, 'l4_corner': l4_corner}
