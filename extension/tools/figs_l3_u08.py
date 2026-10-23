"""Level 3 Unit 8 (Angle and line detectives) figure types.

  l3_angles  angles drawn as two rays with a small arc (or a square marker for a right angle).  spec: items [{deg, rot, label, mark}], cols
             deg: size in degrees (drawing only), rot: direction of the first ray (degrees anticlockwise from east), mark: draw the square marker
  l3_segs    straight line segments on a coordinate grid (y up).  spec: segs [[x1, y1, x2, y2] or {p: [...], dash, w}], dots [nx, ny] (a dot grid),
             labels [{x, y, t, anchor}], k (drawing units per coordinate unit, default 44), pad, caption
"""
import math
import figs as F
from figs_l3_common import T, wrap, esc, NAVY, SOFT, SKY, SW

FIGS = {}


def angles(spec, w=None):
    items = spec['items']
    cols = spec.get('cols', 3)
    CW, CH = spec.get('cw', 250), spec.get('ch', 190)
    L = 118
    P = []
    for k, it in enumerate(items):
        r, c = divmod(k, cols)
        vx, vy = 40 + c * CW, 20 + r * CH + 130
        a0 = math.radians(it.get('rot', 0))
        a1 = a0 + math.radians(it['deg'])
        # y axis points down on the page: use minus for the sine
        p0 = (vx + L * math.cos(a0), vy - L * math.sin(a0))
        p1 = (vx + L * math.cos(a1), vy - L * math.sin(a1))
        P.append(f'<path d="M{p0[0]:.1f},{p0[1]:.1f} L{vx},{vy} L{p1[0]:.1f},{p1[1]:.1f}" fill="none" stroke="{NAVY}" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>')
        if it.get('mark') and abs(it['deg'] - 90) < 0.5:
            s = 30
            q0 = (vx + s * math.cos(a0), vy - s * math.sin(a0)); q1 = (vx + s * math.cos(a1), vy - s * math.sin(a1))
            q2 = (q0[0] + q1[0] - vx, q0[1] + q1[1] - vy)
            P.append(f'<path d="M{q0[0]:.1f},{q0[1]:.1f} L{q2[0]:.1f},{q2[1]:.1f} L{q1[0]:.1f},{q1[1]:.1f}" fill="none" stroke="{NAVY}" stroke-width="3.4"/>')
        elif it.get('arc', True):
            r_ = 34
            ax0 = (vx + r_ * math.cos(a0), vy - r_ * math.sin(a0)); ax1 = (vx + r_ * math.cos(a1), vy - r_ * math.sin(a1))
            large = 1 if it['deg'] > 180 else 0
            P.append(f'<path d="M{ax0[0]:.1f},{ax0[1]:.1f} A{r_},{r_} 0 {large} 0 {ax1[0]:.1f},{ax1[1]:.1f}" fill="none" stroke="{NAVY}" stroke-width="3.4"/>')
        if it.get('label'):
            P.append(T(vx + 6, vy + 44, esc(it['label']), 32))
    nr = (len(items) + cols - 1) // cols
    return wrap(P, 60 + cols * CW - 40, 20 + nr * CH + 20, 'angles', w)


def segs(spec, w=None):
    k = spec.get('k', 44)
    pad = spec.get('pad', 40)
    items = [s if isinstance(s, dict) else {'p': s} for s in spec['segs']]
    xs = [v for s in items for v in (s['p'][0], s['p'][2])]
    ys = [v for s in items for v in (s['p'][1], s['p'][3])]
    nx, ny = spec.get('dots', [0, 0])
    x_min, y_min = min([0] + xs) if nx else min(xs), min([0] + ys) if ny else min(ys)
    x_max, y_max = max([nx - 1] + xs) if nx else max(xs), max([ny - 1] + ys) if ny else max(ys)
    X = lambda x: pad + (x - x_min) * k
    Y = lambda y: pad + (y_max - y) * k
    P = []
    if nx:
        for i in range(nx):
            for j in range(ny):
                P.append(f'<circle cx="{X(i):.1f}" cy="{Y(j):.1f}" r="5" fill="{NAVY}"/>')
    for s in items:
        x1, y1, x2, y2 = s['p']
        dash = ' stroke-dasharray="10 8"' if s.get('dash') else ''
        P.append(f'<line x1="{X(x1):.1f}" y1="{Y(y1):.1f}" x2="{X(x2):.1f}" y2="{Y(y2):.1f}" stroke="{NAVY}" stroke-width="{s.get("w", 7)}" stroke-linecap="round"{dash}/>')
    for lab in spec.get('labels', []):
        P.append(T(X(lab['x']) + lab.get('dx', 0), Y(lab['y']) + lab.get('dy', 10), esc(lab['t']), lab.get('size', 32), anchor=lab.get('anchor', 'middle')))
    W = 2 * pad + (x_max - x_min) * k
    H = 2 * pad + (y_max - y_min) * k
    if spec.get('caption'):
        P.append(T(W / 2, H + 18, esc(spec['caption']), 30)); H += 40
    return wrap(P, W, H, spec.get('label', 'lines'), w)


FIGS.update({'l3_angles': angles, 'l3_segs': segs})
