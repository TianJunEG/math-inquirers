"""Figure types for Level 2 unit 9 (measures: mass, volume, length, time).

  l2_scale   level balance scales: scales [{left: [obj, ...], right: [obj, ...], label?}], obj in apple, melon, lemon, plum, cup, box, or a weight such as "50 g".
             Each pan is captioned with the kind of object (names) so objects are never confused.  Both pans hang level.
  l2_clock   analogue clocks: clocks [{h, m, label?}], numbers 1 to 12 and minute marks; the hour hand sits where it should for the minutes.
  l2_jugs    jugs with a printed capacity and an optional fill level: jugs [{cap, level?, label?}]
Palette NAVY / SOFT / SKY / YEL only.  Pictures differ by shape and by their printed names, never by colour.
"""
import math
import figs as F
from figs_l2_core import T, box, line, wrap, NAVY, SKY, SOFT, YEL


def _obj(kind, cx, cy):
    P = []
    if kind == 'apple':
        P.append(f'<circle cx="{cx}" cy="{cy}" r="24" fill="{SOFT}" stroke="{NAVY}" stroke-width="3.2"/>')
        P.append(f'<path d="M{cx} {cy - 24} q4 -14 14 -16" fill="none" stroke="{NAVY}" stroke-width="3.2" stroke-linecap="round"/>')
    elif kind == 'melon':
        P.append(f'<circle cx="{cx}" cy="{cy}" r="34" fill="{SOFT}" stroke="{NAVY}" stroke-width="3.4"/>')
        for dx in (-16, 0, 16):
            P.append(f'<path d="M{cx + dx} {cy - 33 + abs(dx) * 0.2} Q{cx + dx * 1.4} {cy} {cx + dx} {cy + 33 - abs(dx) * 0.2}" fill="none" stroke="{NAVY}" stroke-width="2.2"/>')
    elif kind == 'lemon':
        P.append(f'<path d="M{cx - 26} {cy} Q{cx - 14} {cy - 20} {cx} {cy - 20} Q{cx + 14} {cy - 20} {cx + 26} {cy} Q{cx + 14} {cy + 20} {cx} {cy + 20} Q{cx - 14} {cy + 20} {cx - 26} {cy}Z" fill="{YEL}" stroke="{NAVY}" stroke-width="3"/>')
    elif kind == 'plum':
        P.append(f'<circle cx="{cx}" cy="{cy}" r="17" fill="{NAVY}" stroke="{NAVY}" stroke-width="2"/>')
    elif kind == 'cup':
        P.append(f'<path d="M{cx - 22} {cy - 20} H{cx + 22} L{cx + 15} {cy + 20} H{cx - 15}Z" fill="{SKY}" stroke="{NAVY}" stroke-width="3.2" stroke-linejoin="round"/>')
        P.append(f'<path d="M{cx + 22} {cy - 12} q16 2 12 14 q-3 6 -14 4" fill="none" stroke="{NAVY}" stroke-width="3"/>')
    elif kind == 'box':
        P.append(f'<rect x="{cx - 26}" y="{cy - 26}" width="52" height="52" fill="{SKY}" stroke="{NAVY}" stroke-width="3.4"/>')
        P.append(line(cx - 26, cy - 26, cx + 26, cy + 26, 2.4))
        P.append(line(cx + 26, cy - 26, cx - 26, cy + 26, 2.4))
    else:   # a weight such as "50 g"
        P.append(f'<rect x="{cx - 38}" y="{cy - 22}" width="76" height="44" rx="8" fill="{SKY}" stroke="{NAVY}" stroke-width="3.4"/>')
        P.append(f'<rect x="{cx - 38}" y="{cy - 22}" width="76" height="44" rx="8" fill="none" stroke="{NAVY}" stroke-width="1.4" transform="translate(0 0)"/>')
        P.append(T(cx, cy + 9, kind, 24))
    return P


def _w(kind):
    return {'apple': 56, 'melon': 76, 'lemon': 60, 'plum': 44, 'cup': 62, 'box': 60}.get(kind, 84)


def _plural(kind, n):
    if kind in ('apple', 'melon', 'lemon', 'plum', 'cup', 'box'):
        return kind + ('s' if n > 1 else '')
    return ''


def scale(spec, w=None):
    sc = spec['scales']
    SW = 330
    maxw = spec.get('max_w', 2 * SW + 70)
    BEAM, PAN, BASE = 46, 200, 262
    P = []
    x = 6
    y = 6
    totw = 0
    for s in sc:
        if x > 6 and x + SW > maxw:
            x = 6
            y += BASE + 90
        cx = x + SW / 2
        P.append(line(cx, y + BEAM, cx, y + BASE, 6))
        P.append(line(cx - 46, y + BASE, cx + 46, y + BASE, 6))
        P.append(line(x + 85, y + BEAM, x + SW - 85, y + BEAM, 7))
        P.append(f'<circle cx="{cx}" cy="{y + BEAM}" r="9" fill="{NAVY}"/>')
        for side, objs in ((0, s['left']), (1, s['right'])):
            px = x + 85 + side * (SW - 170)
            pw = 118
            P.append(line(px, y + BEAM, px - pw / 2, y + PAN, 2.6))
            P.append(line(px, y + BEAM, px + pw / 2, y + PAN, 2.6))
            P.append(f'<path d="M{px - pw / 2 - 8} {y + PAN} H{px + pw / 2 + 8} Q{px + pw / 2} {y + PAN + 16} {px} {y + PAN + 16} Q{px - pw / 2} {y + PAN + 16} {px - pw / 2 - 8} {y + PAN}Z" fill="{SOFT}" stroke="{NAVY}" stroke-width="3.2" stroke-linejoin="round"/>')
            rows = [objs[i:i + 2] for i in range(0, len(objs), 2)]
            ry = y + PAN
            for row in rows:
                tw = sum(_w(o) for o in row)
                ox = px - tw / 2
                rh = 70 if any(o == 'melon' for o in row) else 52
                for o in row:
                    ww = _w(o)
                    P += _obj(o, ox + ww / 2, ry - rh / 2 - 1)
                    ox += ww
                ry -= rh
            names = {}
            for o in objs:
                if not o.endswith(' g'):
                    names[o] = names.get(o, 0) + 1
            nm = ' + '.join(_plural(k, 2) if n > 1 else k for k, n in names.items())
            if nm:
                P.append(T(px, y + PAN + 46, nm, 26, weight=700))
        if s.get('label'):
            P.append(T(cx, y + BASE + 44, s['label'], 30))
        x += SW + 30
        totw = max(totw, x - 30)
    H = y + BASE + 70
    return wrap(P, totw + 6, H, 'balance scales', w, 0.2)


def clock(spec, w=None):
    cl = spec['clocks']
    R = 92
    P = []
    x = 6
    for c in cl:
        cx, cy = x + R + 10, 6 + R + 10
        P.append(f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="#fff" stroke="{NAVY}" stroke-width="5"/>')
        for m in range(60):
            a = math.radians(m * 6 - 90)
            r1 = R - (14 if m % 5 == 0 else 7)
            P.append(line(cx + r1 * math.cos(a), cy + r1 * math.sin(a), cx + (R - 3) * math.cos(a), cy + (R - 3) * math.sin(a), 3 if m % 5 == 0 else 1.6))
        for hnum in range(1, 13):
            a = math.radians(hnum * 30 - 90)
            P.append(T(cx + (R - 32) * math.cos(a), cy + (R - 32) * math.sin(a) + 10, hnum, 28))
        ah = math.radians((c['h'] % 12) * 30 + c['m'] * 0.5 - 90)
        am = math.radians(c['m'] * 6 - 90)
        P.append(line(cx, cy, cx + 44 * math.cos(ah), cy + 44 * math.sin(ah), 8))
        P.append(line(cx, cy, cx + 70 * math.cos(am), cy + 70 * math.sin(am), 4.6))
        P.append(f'<circle cx="{cx}" cy="{cy}" r="6" fill="{NAVY}"/>')
        if c.get('label'):
            P.append(T(cx, cy + R + 46, c['label'], 32))
        x += 2 * R + 50
    return wrap(P, x - 20, 2 * R + 20 + (56 if any(c.get('label') for c in cl) else 0), 'analogue clocks', w, 0.2)


def jugs(spec, w=None):
    P = []
    x = 20
    scale = 16
    for j in spec['jugs']:
        cap = j['cap']
        hgt = cap * scale + 20
        top = 20
        bw = 76
        P.append(f'<path d="M{x} {top} V{top + hgt} H{x + bw} V{top}" fill="none" stroke="{NAVY}" stroke-width="4"/>')
        lvl = j.get('level')
        if lvl:
            ly = top + hgt - lvl * scale
            P.append(f'<rect x="{x + 2}" y="{ly}" width="{bw - 4}" height="{lvl * scale}" fill="{SKY}"/>')
            P.append(line(x + 2, ly, x + bw - 2, ly, 3))
        P.append(T(x + bw / 2, top + hgt + 40, f'{cap} ℓ jug', 28))
        x += bw + 70
    H = 20 + max(j['cap'] for j in spec['jugs']) * scale + 20 + 60
    return wrap(P, x - 40, H, 'jugs', w, 0.2)


FIGS = {'l2_scale': scale, 'l2_clock': clock, 'l2_jugs': jugs}
