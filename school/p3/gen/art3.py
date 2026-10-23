"""Primary 3 pictures (original art, black and white). Every picture has a reader that recovers its values from the DRAWING only."""
import math, re
from .common import svg
from .art2 import DISC_R

# ---------------------------------------------------------------------------------------------------- place-value discs with thousands
def disc4(kind, cx, cy):
    lab = {"th": "1000", "h": "100", "t": "10", "o": "1"}[kind]
    fs = {"th": 3.0, "h": 3.7, "t": 4.3, "o": 5.2}[kind]
    sw = {"th": 1.3, "h": 0.9, "t": 0.6, "o": 0.6}[kind]
    return (f'<g class="disc {kind}"><circle cx="{cx:.2f}" cy="{cy:.2f}" r="{DISC_R}" fill="#fff" stroke="#000" stroke-width="{sw}"/>'
            f'<text x="{cx:.2f}" y="{cy+0.1:.2f}" text-anchor="middle" dominant-baseline="central" font-family="Nunito Sans" font-weight="800" font-size="{fs}" fill="#000">{lab}</text></g>')

def pv4_chart(th, h, t, o, per_row=2):
    """four columns (Thousands, Hundreds, Tens, Ones) of discs, `per_row` discs in a row"""
    colw = per_row * 10.4 + 2.5; gap = 2.0; head = 6.5
    rows = max(math.ceil(n / per_row) for n in (th, h, t, o)) or 1
    H = head + rows * 10.4 + 1.5; W = 4 * colw + 3 * gap
    p = []
    for ci, (name, kind, n) in enumerate((("Thousands", "th", th), ("Hundreds", "h", h), ("Tens", "t", t), ("Ones", "o", o))):
        x0 = ci * (colw + gap)
        p.append(f'<rect x="{x0:.2f}" y="0.3" width="{colw:.2f}" height="{H-0.6:.2f}" rx="1.2" fill="#fff" stroke="#000" stroke-width="0.5"/>'
                 f'<text x="{x0+colw/2:.2f}" y="3.6" text-anchor="middle" dominant-baseline="central" font-family="Nunito Sans" font-weight="800" font-size="3.4" fill="#000">{name}</text>'
                 f'<line x1="{x0:.2f}" y1="{head-0.8}" x2="{x0+colw:.2f}" y2="{head-0.8}" stroke="#000" stroke-width="0.4"/>')
        for i in range(n):
            p.append(disc4(kind, x0 + 1.2 + DISC_R + 0.4 + (i % per_row) * 10.4, head + 0.6 + DISC_R + (i // per_row) * 10.4))
    return svg(round(W, 1), round(H, 1), "".join(p))

def read_pv4(s):
    return tuple(len(re.findall(r'class="disc %s"' % k, s)) for k in ("th", "h", "t", "o"))
