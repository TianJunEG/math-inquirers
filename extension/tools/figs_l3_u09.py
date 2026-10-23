"""Level 3 Unit 9 (Measure and money masters) figure types.

  l3_ruler     a centimetre ruler drawn at REAL SIZE (1 cm = 10 mm) with objects lying above it.  spec: max (cm), objects [{label, start, end}]
               (do not pass width_mm: the size is fixed by the scale; the soft copy must be printed at 100 percent)
  l3_clock     analogue clock faces.  spec: clocks [{h, m, label}], cols
  l3_timeline  a time line.  spec: points [{t}] (equal spacing), arcs [{a, b, text}] (text None = empty box for the child), total {a, b, text}
  l3_jug       measuring jugs with a scale.  spec: jugs [{cap, level, label}], major (labelled every `major` ml), minor (tick every `minor` ml)
"""
import math
import figs as F
from figs_l3_common import T, wrap, esc, NAVY, SOFT, SKY, YEL, SW, K

FIGS = {}


def ruler(spec, w=None):
    mx = spec.get('max', 14)
    CM = 50
    X0 = 30
    objs = spec.get('objects', [])
    OH, GAP = 44, 14
    top = 8
    ry = top + len(objs) * (OH + GAP) + 4
    RH = 78
    P = []
    for i, o in enumerate(objs):
        y = top + i * (OH + GAP)
        a, b = X0 + o['start'] * CM, X0 + o['end'] * CM
        P.append(f'<rect x="{a}" y="{y}" width="{b - a}" height="{OH}" rx="10" fill="{SOFT}" stroke="{NAVY}" stroke-width="{SW + 0.6}"/>')
        P.append(f'<line x1="{a}" y1="{y + OH}" x2="{a}" y2="{ry}" stroke="{NAVY}" stroke-width="2" stroke-dasharray="4 4"/>')
        P.append(f'<line x1="{b}" y1="{y + OH}" x2="{b}" y2="{ry}" stroke="{NAVY}" stroke-width="2" stroke-dasharray="4 4"/>')
        if o.get('label'):
            P.append(T((a + b) / 2, y + OH / 2 + 10, esc(o['label']), 28, weight=800))
    P.append(f'<rect x="{X0 - 14}" y="{ry}" width="{mx * CM + 28}" height="{RH}" rx="6" fill="{SKY}" stroke="{NAVY}" stroke-width="{SW}"/>')
    for mm in range(mx * 10 + 1):
        x = X0 + mm * CM / 10
        if mm % 10 == 0:
            h, sw = 34, 3
        elif mm % 5 == 0:
            h, sw = 24, 2.4
        else:
            h, sw = 14, 1.8
        P.append(f'<line x1="{x}" y1="{ry}" x2="{x}" y2="{ry + h}" stroke="{NAVY}" stroke-width="{sw}"/>')
        if mm % 10 == 0:
            P.append(T(x, ry + 66, mm // 10, 26, weight=700))
    W = X0 * 2 + mx * CM
    return F._wrap(''.join(P), W, ry + RH + 10, 'centimetre ruler at real size', w or round(W * K, 1))


def clock(spec, w=None):
    clocks = spec['clocks']
    cols = spec.get('cols', 3)
    CW, CH = 270, 270
    R = 108
    P = []
    for k, c in enumerate(clocks):
        r_, cc = divmod(k, cols)
        cx, cy = 20 + R + 10 + cc * CW, 20 + R + 4 + r_ * CH
        P.append(f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="#fff" stroke="{NAVY}" stroke-width="6"/>')
        for m in range(60):
            a = math.radians(m * 6)
            r1 = R - (14 if m % 5 == 0 else 7)
            P.append(f'<line x1="{cx + r1 * math.sin(a):.1f}" y1="{cy - r1 * math.cos(a):.1f}" x2="{cx + (R - 3) * math.sin(a):.1f}" y2="{cy - (R - 3) * math.cos(a):.1f}" stroke="{NAVY}" stroke-width="{3.4 if m % 5 == 0 else 1.6}"/>')
        for n in range(1, 13):
            a = math.radians(n * 30)
            P.append(T(cx + 78 * math.sin(a), cy - 78 * math.cos(a) + 9, n, 27, weight=800))
        hm = (c['h'] % 12) * 30 + c['m'] * 0.5
        mm_ = c['m'] * 6
        for ang, ln, wd in ((hm, 40, 12), (mm_, 62, 8)):
            a = math.radians(ang)
            P.append(f'<line x1="{cx}" y1="{cy}" x2="{cx + ln * math.sin(a):.1f}" y2="{cy - ln * math.cos(a):.1f}" stroke="{NAVY}" stroke-width="{wd}" stroke-linecap="round"/>')
        P.append(f'<circle cx="{cx}" cy="{cy}" r="8" fill="{NAVY}"/>')
        if c.get('label'):
            P.append(T(cx, cy + R + 36, esc(c['label']), 32))
    nr = (len(clocks) + cols - 1) // cols
    return wrap(P, 40 + cols * CW - 40, 20 + nr * CH + 20, 'clocks', w)


def timeline(spec, w=None):
    pts = spec['points']
    n = len(pts)
    X0, X1 = 70, spec.get('W', 760) - 70
    y = 150
    xs = [X0 + (X1 - X0) * i / (n - 1) for i in range(n)]
    P = [f'<line x1="{X0 - 30}" y1="{y}" x2="{X1 + 30}" y2="{y}" stroke="{NAVY}" stroke-width="4"/>']
    for x, p in zip(xs, pts):
        P.append(f'<line x1="{x:.1f}" y1="{y - 16}" x2="{x:.1f}" y2="{y + 16}" stroke="{NAVY}" stroke-width="4"/>')
        if p.get('t') is None:
            P.append(f'<rect x="{x - 44:.1f}" y="{y + 26}" width="88" height="50" rx="6" fill="#fff" stroke="{NAVY}" stroke-width="3" stroke-dasharray="8 6"/>')
        else:
            P.append(T(x, y + 56, esc(p['t']), 28, weight=800))
    for arc_list, up in ((spec.get('arcs', []), True),):
        for a in arc_list:
            xa, xb = xs[a['a']], xs[a['b']]
            P.append(f'<path d="M{xa + 4:.1f},{y - 22} Q{(xa + xb) / 2:.1f},{y - 92} {xb - 4:.1f},{y - 22}" fill="none" stroke="{NAVY}" stroke-width="3.4"/>')
            if a.get('text') is None:
                P.append(f'<rect x="{(xa + xb) / 2 - 42:.1f}" y="{y - 104}" width="84" height="46" rx="6" fill="#fff" stroke="{NAVY}" stroke-width="3" stroke-dasharray="8 6"/>')
            else:
                P.append(T((xa + xb) / 2, y - 62, esc(a['text']), 28))
    tot = spec.get('total')
    if tot:
        xa, xb = xs[tot['a']], xs[tot['b']]
        P.append(f'<path d="M{xa:.1f},{y + 88} v14 H{xb:.1f} v-14" fill="none" stroke="{NAVY}" stroke-width="3.4"/>')
        if tot.get('text') is None:
            P.append(f'<rect x="{(xa + xb) / 2 - 70:.1f}" y="{y + 110}" width="140" height="48" rx="6" fill="#fff" stroke="{NAVY}" stroke-width="3" stroke-dasharray="8 6"/>')
        else:
            P.append(T((xa + xb) / 2, y + 140, esc(tot['text']), 28))
    return wrap(P, X1 + 100, y + (170 if tot else 90), 'time line', w)


def jug(spec, w=None):
    jugs = spec['jugs']
    major, minor = spec.get('major', 100), spec.get('minor', 50)
    CW = 230
    top, bot = 30, 300
    P = []
    for k, j in enumerate(jugs):
        ox = 10 + k * CW
        bx0, bx1 = ox + 100, ox + 190
        cap = j.get('cap', 1000)
        yy = lambda ml: bot - (bot - top) * ml / cap
        lv = yy(j['level'])
        P.append(f'<rect x="{bx0}" y="{lv:.1f}" width="{bx1 - bx0}" height="{bot - lv:.1f}" fill="{YEL}"/>')
        P.append(f'<path d="M{bx0},{top} V{bot - 14} Q{bx0},{bot} {bx0 + 14},{bot} H{bx1 - 14} Q{bx1},{bot} {bx1},{bot - 14} V{top}" fill="none" stroke="{NAVY}" stroke-width="5" stroke-linejoin="round"/>')
        ml = 0
        while ml <= cap:
            y = yy(ml)
            big = ml % major == 0
            P.append(f'<line x1="{bx0 - (26 if big else 14)}" y1="{y:.1f}" x2="{bx0}" y2="{y:.1f}" stroke="{NAVY}" stroke-width="{3.4 if big else 2.4}"/>')
            if big and ml > 0:
                P.append(T(bx0 - 34, y + 9, ml, 24, anchor='end', weight=700))
            ml += minor
        if j.get('label'):
            P.append(T((bx0 + bx1) / 2, bot + 52, esc(j['label']), 32))
    return wrap(P, 20 + len(jugs) * CW, bot + 72, 'measuring jugs', w)


FIGS.update({'l3_ruler': ruler, 'l3_clock': clock, 'l3_timeline': timeline, 'l3_jug': jug})
