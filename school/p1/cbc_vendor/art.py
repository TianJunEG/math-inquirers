"""Small SVG pictures that can sit inside a region: clocks, coins, notes, a ruler with a strip, flat shapes.
Every Art has local coordinates (origin top-left, mm at scale 1), a width and a height, and `meta` so that the
verification script can decode the picture independently of the question generator."""
import math
from dataclasses import dataclass, field

@dataclass
class Art:
    svg: str
    w: float
    h: float
    min_scale: float = 0.85
    meta: dict = field(default_factory=dict)

K = 'fill="none" stroke="#000" stroke-linecap="round" stroke-linejoin="round"'

def clock(h, m):
    r = 9.0; cx = cy = r + 0.5
    s = [f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#fff" stroke="#000" stroke-width="0.55"/>']
    for k in range(1, 13):
        a = math.radians(k * 30)
        s.append(f'<text x="{cx + 6.75 * math.sin(a):.2f}" y="{cy - 6.75 * math.cos(a):.2f}" style="font-size:2.5px;font-weight:600;text-anchor:middle;dominant-baseline:central">{k}</text>')
    ha = ((h % 12) + m / 60.0) * 30.0
    ma = m * 6.0
    def hand(ang, ln, wd):
        a = math.radians(ang)
        return f'<line x1="{cx}" y1="{cy}" x2="{cx + ln * math.sin(a):.2f}" y2="{cy - ln * math.cos(a):.2f}" stroke="#000" stroke-width="{wd}" stroke-linecap="round"/>'
    s.append(hand(ha, 3.3, 1.25)); s.append(hand(ma, 5.0, 0.75))
    s.append(f'<circle cx="{cx}" cy="{cy}" r="0.9" fill="#000"/>')
    return Art("".join(s), 2 * r + 1, 2 * r + 1, 0.9, dict(kind="clock", hour_angle=ha, minute_angle=ma))

def decode_clock(meta):
    """(hour, minute) from the drawn hand angles"""
    mm = round(meta["minute_angle"] / 6.0) % 60
    hh = int(round(meta["hour_angle"] - mm * 0.5) / 30) % 12 or 12
    return hh, mm

COIN_R = {5: 4.2, 10: 4.6, 20: 5.0, 50: 5.5, 100: 5.8}
def coins(values):
    x = 0.0; s = []; h = 2 * 5.8 + 1
    for v in values:
        r = COIN_R[v]; x += r
        label = f"{v}¢" if v < 100 else "$1"
        s.append(f'<circle cx="{x:.2f}" cy="{h / 2}" r="{r}" fill="#fff" stroke="#000" stroke-width="0.5"/>'
                 f'<text x="{x:.2f}" y="{h / 2}" style="font-size:3.2px;font-weight:700;text-anchor:middle;dominant-baseline:central">{label}</text>')
        x += r + 1.2
    return Art("".join(s), x - 1.2, h, 0.85, dict(kind="coins", values=list(values)))

def notes(values):
    """dollar notes ($2, $5, $10) drawn as small rectangles; a $1 coin is a circle"""
    x = 0.0; s = []; h = 8.0
    for v in values:
        if v == 1:
            s.append(f'<circle cx="{x + 4:.2f}" cy="{h / 2}" r="4" fill="#fff" stroke="#000" stroke-width="0.5"/><text x="{x + 4:.2f}" y="{h / 2}" style="font-size:3.2px;font-weight:700;text-anchor:middle;dominant-baseline:central">$1</text>')
            x += 8 + 1.2
        else:
            s.append(f'<rect x="{x:.2f}" y="0.5" width="13" height="7" rx="0.8" fill="#fff" stroke="#000" stroke-width="0.5"/>'
                     f'<text x="{x + 6.5:.2f}" y="4" style="font-size:3.6px;font-weight:700;text-anchor:middle;dominant-baseline:central">${v}</text>')
            x += 13 + 1.2
    return Art("".join(s), x - 1.2, h, 0.85, dict(kind="notes", values=list(values)))

def ruler(start, end, top=None):
    """a strip lying on a ruler marked in cm; the strip runs from `start` to `end` (not to scale)"""
    top = top or max(end + 1, 6)
    u, pad = 3.7, 2.0
    w = top * u + 2 * pad + 1.0
    s = []
    s.append(f'<rect x="{0.5 + pad + start * u:.2f}" y="0.5" width="{(end - start) * u:.2f}" height="3.6" rx="0.6" fill="#fff" stroke="#000" stroke-width="0.5"/>')
    y0 = 5.2
    s.append(f'<rect x="0.5" y="{y0}" width="{top * u + 2 * pad:.2f}" height="6.6" fill="#fff" stroke="#000" stroke-width="0.5"/>')
    for k in range(0, top + 1):
        x = 0.5 + pad + k * u
        s.append(f'<line x1="{x:.2f}" y1="{y0}" x2="{x:.2f}" y2="{y0 + 1.7}" stroke="#000" stroke-width="0.4"/>')
        s.append(f'<text x="{x:.2f}" y="{y0 + 4.5}" style="font-size:2.7px;font-weight:600;text-anchor:middle;dominant-baseline:central">{k}</text>')
    return Art("".join(s), w, 12.0, 0.9, dict(kind="ruler", start=start, end=end, top=top))

def _shape(kind):
    st = 'fill="#fff" stroke="#000" stroke-width="0.55" stroke-linejoin="round"'
    if kind == "triangle": return f'<polygon points="0.3,10 12.3,10 6.3,0.3" {st}/>', 12.6, 10.3
    if kind == "square": return f'<rect x="0.3" y="0.3" width="9.6" height="9.6" {st}/>', 10.2, 10.2
    if kind == "rectangle": return f'<rect x="0.3" y="2.2" width="15.4" height="7.8" {st}/>', 16.0, 10.3
    if kind == "circle": return f'<circle cx="5.2" cy="5.2" r="4.9" {st}/>', 10.4, 10.4
    raise KeyError(kind)

SHAPES = {"triangle": 3, "square": 4, "rectangle": 4, "circle": 0}   # number of corners = number of straight sides
def shapes(kinds):
    x = 0.0; s = []
    for k in kinds:
        svg, w, h = _shape(k)
        s.append(f'<g transform="translate({x:.2f},0)">{svg}</g>'); x += w + 3.0
    return Art("".join(s), x - 3.0, 10.3, 0.72, dict(kind="shapes", kinds=list(kinds)))
