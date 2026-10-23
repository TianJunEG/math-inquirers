"""Level 3 Unit 6 (Fraction walls) figure types.

  l3_wall     a fraction wall: rows of equal pieces.  spec: dens [1, 2, 4 ...], labels (bool, default true: every piece shows its unit
              fraction), blank_dens (rows whose pieces are left empty), shade {den: [piece indexes]} (hatched in print, no text),
              mark {den: [piece indexes]} (thick outline), row_labels (bool: "1 whole" ... on the left)
  l3_fshapes  shapes cut into parts.  spec: items [{kind: bar|circle, n, shade: [indexes], cuts: [positions 0..1] (unequal bar),
              angles: [degrees] (unequal circle), label}], cols
  l3_fline    a number line from 0 to 1 cut into `den` equal steps with lettered arrows: marks [{at (numerator), text}], label_dens (bool)
Stacked fractions (numerator over a bar over denominator) are drawn by frac().  Never put text on a shaded piece (it is hatching in print).
"""
import math
import figs as F
from figs_l3_common import T, wrap, esc, NAVY, SOFT, SKY, YEL, SW

FIGS = {}


def frac(x, cy, n, d, size=26, fill=NAVY):
    """stacked fraction centred on x, vertical centre cy"""
    w = max(len(str(n)), len(str(d))) * size * 0.62 + 6
    return (T(x, cy - size * 0.1, n, size, fill, weight=800) + f'<line x1="{x - w / 2:.1f}" y1="{cy + size * 0.1:.1f}" x2="{x + w / 2:.1f}" y2="{cy + size * 0.1:.1f}" stroke="{fill}" stroke-width="2.6"/>'
            + T(x, cy + size * 0.98, d, size, fill, weight=800))


def wall(spec, w=None):
    dens = spec['dens']
    W0 = spec.get('W', 720)
    RH, GAP = spec.get('rh', 64), 6
    X0 = 6 + (spec.get('lab', 0))
    shade = {int(k): v for k, v in spec.get('shade', {}).items()}
    mark = {int(k): v for k, v in spec.get('mark', {}).items()}
    blank = set(spec.get('blank_dens', []))
    P = []
    for r, d in enumerate(dens):
        y = 6 + r * (RH + GAP)
        pw = W0 / d
        if spec.get('row_labels'):
            P.append(T(X0 - 12, y + RH / 2 + 9, esc(spec['row_labels'][r]) if isinstance(spec['row_labels'], list) else '', 24, anchor='end', weight=700))
        for i in range(d):
            x = X0 + i * pw
            sh = i in shade.get(d, [])
            P.append(f'<rect x="{x:.1f}" y="{y}" width="{pw:.1f}" height="{RH}" fill="{YEL if sh else (SOFT if d % 2 else SKY)}" stroke="{NAVY}" stroke-width="{SW}"/>')
            if not sh and d not in blank and spec.get('labels', True):
                P.append(frac(x + pw / 2, y + RH / 2 - 8, 1, d, 26 if d < 10 else 24) if d > 1 else T(x + pw / 2, y + RH / 2 + 10, '1 whole', 28))
        for i in mark.get(d, []):
            P.append(f'<rect x="{X0 + i * pw:.1f}" y="{y}" width="{pw:.1f}" height="{RH}" fill="none" stroke="{NAVY}" stroke-width="8"/>')
    H = 12 + len(dens) * (RH + GAP)
    return wrap(P, X0 + W0 + 12, H, 'fraction wall', w or round((X0 + W0 + 12) * 0.2, 1))


def _sector(cx, cy, r, a0, a1):
    x0, y0 = cx + r * math.cos(math.radians(a0)), cy + r * math.sin(math.radians(a0))
    x1, y1 = cx + r * math.cos(math.radians(a1)), cy + r * math.sin(math.radians(a1))
    large = 1 if (a1 - a0) > 180 else 0
    return f'M{cx},{cy} L{x0:.1f},{y0:.1f} A{r},{r} 0 {large} 1 {x1:.1f},{y1:.1f} Z'


def fshapes(spec, w=None):
    items = spec['items']
    cols = spec.get('cols', 2)
    CW, CH = spec.get('cw', 330), spec.get('ch', 150)
    P = []
    for k, it in enumerate(items):
        r, c = divmod(k, cols)
        ox, oy = 10 + c * CW, 6 + r * CH
        shade = set(it.get('shade', []))
        kind = it.get('kind', 'bar')
        if kind == 'bar':
            bw, bh = 250, 64
            cuts = it.get('cuts') or [i / it['n'] for i in range(1, it['n'])]
            edges = [0] + list(cuts) + [1]
            for i in range(len(edges) - 1):
                x = ox + 44 + edges[i] * bw
                P.append(f'<rect x="{x:.1f}" y="{oy + 12}" width="{(edges[i + 1] - edges[i]) * bw:.1f}" height="{bh}" fill="{YEL if i in shade else "#fff"}" stroke="{NAVY}" stroke-width="{SW}"/>')
            cx_lab, cy_lab = ox + 20, oy + 12 + bh / 2 + 10
        else:
            R = 58
            cx, cy = ox + 44 + R + 10, oy + 12 + R
            angs = it.get('angles') or [360 / it['n']] * it['n']
            a = -90.0
            for i, g in enumerate(angs):
                P.append(f'<path d="{_sector(cx, cy, R, a, a + g)}" fill="{YEL if i in shade else "#fff"}" stroke="{NAVY}" stroke-width="{SW}" stroke-linejoin="round"/>')
                a += g
            cx_lab, cy_lab = ox + 20, cy + 10
        if it.get('label'):
            P.append(T(cx_lab, cy_lab, esc(it['label']), 30))
    nr = (len(items) + cols - 1) // cols
    return wrap(P, 20 + cols * CW, 12 + nr * CH, 'shapes cut into parts', w)


def fline(spec, w=None):
    den = spec['den']
    X0, X1 = 40, spec.get('W', 700) - 40
    y = 110
    P = [f'<line x1="{X0 - 20}" y1="{y}" x2="{X1 + 20}" y2="{y}" stroke="{NAVY}" stroke-width="4"/>']
    for i in range(den + 1):
        x = X0 + (X1 - X0) * i / den
        big = i in (0, den)
        P.append(f'<line x1="{x:.1f}" y1="{y - (24 if big else 15)}" x2="{x:.1f}" y2="{y + (24 if big else 15)}" stroke="{NAVY}" stroke-width="{4 if big else 3}"/>')
        if i == 0:
            P.append(T(x, y + 64, '0', 30))
        if i == den:
            P.append(T(x, y + 64, '1', 30))
        if spec.get('label_all') and 0 < i < den:
            P.append(frac(x, y + 38, i, den, 24))
    for m in spec.get('marks', []):
        x = X0 + (X1 - X0) * m['at'] / den
        P.append(f'<path d="M{x:.1f},{y - 8} L{x - 17:.1f},{y - 48} L{x + 17:.1f},{y - 48}Z" fill="{NAVY}" stroke="{NAVY}" stroke-width="2"/>')
        if m.get('text'):
            P.append(T(x, y - 58, esc(m['text']), 32))
    return wrap(P, X1 + 60, y + 100, 'number line from 0 to 1', w)


FIGS.update({'l3_wall': wall, 'l3_fshapes': fshapes, 'l3_fline': fline})
