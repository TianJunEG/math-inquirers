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

CLOCK_MIN_GAP = 40.0                # degrees: a clock a pupil must read keeps its two hands at least this far apart (audit 3, M5)
def hand_gap(h, m):
    """angle in degrees between the hour hand and the minute hand of h:m"""
    d = abs(((h % 12) + m / 60.0) * 30.0 - m * 6.0) % 360.0
    return min(d, 360.0 - d)

def clock(h, m):
    """a clock face 25 mm across: numerals 3.4 mm, a short thick hour hand and a long thin minute hand"""
    r = 12.0; cx = cy = r + 0.5
    s = [f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#fff" stroke="#000" stroke-width="0.6"/>']
    for k in range(60):                                  # minute ticks: long every five minutes (the numerals sit inside them)
        a = math.radians(k * 6); l = 1.6 if k % 5 == 0 else 0.8
        s.append(f'<line x1="{cx + (r - l) * math.sin(a):.2f}" y1="{cy - (r - l) * math.cos(a):.2f}" x2="{cx + r * math.sin(a):.2f}" y2="{cy - r * math.cos(a):.2f}" stroke="#000" stroke-width="{0.5 if k % 5 == 0 else 0.3}"/>')
    for k in range(1, 13):
        a = math.radians(k * 30)
        s.append(f'<text x="{cx + 7.9 * math.sin(a):.2f}" y="{cy - 7.9 * math.cos(a):.2f}" style="font-size:3.5px;font-weight:700;text-anchor:middle;dominant-baseline:central">{k}</text>')
    ha = ((h % 12) + m / 60.0) * 30.0
    ma = m * 6.0
    def hand(ang, ln, wd):
        a = math.radians(ang)
        return f'<line x1="{cx}" y1="{cy}" x2="{cx + ln * math.sin(a):.2f}" y2="{cy - ln * math.cos(a):.2f}" stroke="#000" stroke-width="{wd}" stroke-linecap="round"/>'
    s.append(hand(ma, 9.6, 0.7)); s.append(hand(ha, 5.0, 1.5))
    s.append(f'<circle cx="{cx}" cy="{cy}" r="1.0" fill="#000"/>')
    return Art("".join(s), 2 * r + 1, 2 * r + 1, 0.9, dict(kind="clock", hour_angle=ha, minute_angle=ma))

def decode_clock(meta):
    """(hour, minute) from the drawn hand angles"""
    mm = round(meta["minute_angle"] / 6.0) % 60
    hh = int(round(meta["hour_angle"] - mm * 0.5) / 30) % 12 or 12
    return hh, mm

COIN_R = {5: 4.2, 10: 4.8, 20: 5.6, 50: 6.4, 100: 6.4}      # radii in the real ratio of the diameters (5c 16.2, 10c 18.5, 20c 21.4, 50c 24.7, $1 24.65 mm), drawn much larger than real size
def _coin(cx, cy, v, r):
    """an ORIGINAL coin (not a copy of any real coin): a ring, a dashed ridge ring as an edge hint, the value large and a small cents sign under it ($1 has no cents sign)"""
    s = [f'<circle cx="{cx:.2f}" cy="{cy}" r="{r}" fill="#fff" stroke="#000" stroke-width="0.5"/>',
         f'<circle cx="{cx:.2f}" cy="{cy}" r="{r - 0.75:.2f}" fill="none" stroke="#000" stroke-width="0.3" stroke-dasharray="0.7 0.5"/>']
    if v < 100:
        s.append(f'<text x="{cx:.2f}" y="{cy - 0.7:.2f}" style="font-size:3.4px;font-weight:700;text-anchor:middle;dominant-baseline:central">{v}</text>')
        s.append(f'<text x="{cx:.2f}" y="{cy + r * 0.52:.2f}" style="font-size:2.3px;font-weight:700;text-anchor:middle;dominant-baseline:central">¢</text>')
    else:
        s.append(f'<text x="{cx:.2f}" y="{cy}" style="font-size:3.8px;font-weight:700;text-anchor:middle;dominant-baseline:central">$1</text>')
    return "".join(s)
def coins(values):
    x = 0.0; s = []; h = 2 * 6.4 + 1
    for v in values:
        r = COIN_R[v]; x += r
        s.append(_coin(x, h / 2, v, r))
        x += r + 1.2
    return Art("".join(s), x - 1.2, h, 0.85, dict(kind="coins", values=list(values)))

def notes(values):
    """dollar notes ($2, $5, $10) drawn as small rectangles; a $1 coin is a circle"""
    x = 0.0; s = []; h = 12.8
    for v in values:
        if v == 1:
            s.append(_coin(x + 6.4, 6.4, 100, 6.4))
            x += 12.8 + 1.2
        else:
            s.append(f'<rect x="{x:.2f}" y="2.9" width="13" height="7" rx="0.8" fill="#fff" stroke="#000" stroke-width="0.5"/>'
                     f'<text x="{x + 6.5:.2f}" y="6.4" style="font-size:3.6px;font-weight:700;text-anchor:middle;dominant-baseline:central">${v}</text>')
            x += 13 + 1.2
    return Art("".join(s), x - 1.2, h, 0.85, dict(kind="notes", values=list(values)))

def ruler(start, end, top=None):
    """a strip lying on a ruler marked in cm (not to scale). A bold arrow above the left end of the strip and a bold tick on the ruler show where it starts:
    the length is the number of cm from the arrow to the other end, whether the strip starts at 0 or at another mark."""
    top = top or max(end + 1, 6)
    u, pad = 3.9, 2.0
    w = top * u + 2 * pad + 1.0
    s = []
    xs = 0.5 + pad + start * u
    s.append(f'<polygon points="{xs - 1.5:.2f},0.4 {xs + 1.5:.2f},0.4 {xs:.2f},3.2" fill="#000"/>')                 # start arrow
    s.append(f'<rect x="{xs:.2f}" y="3.6" width="{(end - start) * u:.2f}" height="3.8" rx="0.6" fill="#fff" stroke="#000" stroke-width="0.5"/>')
    y0 = 8.6
    s.append(f'<rect x="0.5" y="{y0}" width="{top * u + 2 * pad:.2f}" height="7.0" fill="#fff" stroke="#000" stroke-width="0.5"/>')
    for k in range(0, top + 1):
        x = 0.5 + pad + k * u
        bold = k == start
        s.append(f'<line x1="{x:.2f}" y1="{y0}" x2="{x:.2f}" y2="{y0 + (3.0 if bold else 1.7)}" stroke="#000" stroke-width="{1.0 if bold else 0.4}"/>')
        s.append(f'<text x="{x:.2f}" y="{y0 + 5.0}" style="font-size:{3.0}px;font-weight:{700 if bold else 600};text-anchor:middle;dominant-baseline:central">{k}</text>')
    return Art("".join(s), w, 16.2, 0.9, dict(kind="ruler", start=start, end=end, top=top, arrow=True))

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


# ---------------------------------------------------------------------------------------------- Primary 2 art
# Every helper returns an Art (local mm coordinates, origin top-left) and records in `meta` what a reader would decode from the
# picture, so that verify.py can check the picture against the intended answer without trusting the question generator.
_ST = 'stroke="#000" stroke-width="0.5" stroke-linejoin="round" stroke-linecap="round"'
_TXT = 'style="font-size:{fs}px;font-weight:{fw};text-anchor:{an};dominant-baseline:central"'
def _text(x, y, s, fs=3.0, fw=700, an="middle"):
    return f'<text x="{x:.2f}" y="{y:.2f}" ' + _TXT.format(fs=fs, fw=fw, an=an) + f'>{s}</text>'

def _hatch(poly, spacing=1.2):
    """diagonal hatch lines clipped to a polygon (shapely), as SVG path data; black and white copies keep hatching, solid black hides the parts"""
    from shapely.geometry import LineString
    g = poly.buffer(-0.45)
    if g.is_empty: return ""
    minx, miny, maxx, maxy = g.bounds
    d = []; c = minx + miny + spacing / 2
    while c < maxx + maxy:
        seg = g.intersection(LineString([(minx - 1, c - (minx - 1)), (maxx + 1, c - (maxx + 1))]))
        for ln in ([seg] if seg.geom_type == "LineString" else list(getattr(seg, "geoms", []))):
            if ln.geom_type == "LineString" and ln.length > 0.4:
                (x0, y0), (x1, y1) = ln.coords[0], ln.coords[-1]
                d.append(f"M{x0:.2f},{y0:.2f} L{x1:.2f},{y1:.2f}")
        c += spacing * 1.4142
    return f'<path d="{" ".join(d)}" stroke="#000" stroke-width="0.3" fill="none"/>' if d else ""

def fraction(a, b, shape="bar"):
    """a of b equal parts shaded; every part has its own outline and the shaded parts are hatched (never solid black), so the equal parts can be counted"""
    from shapely.geometry import box as sbox, Polygon
    s = []
    if shape == "bar":
        W, H = max(18.0, min(36.0, 3.4 * b + 8.0)), 7.0
        pw = W / b
        for i in range(b):
            if i < a: s.append(_hatch(sbox(0.5 + i * pw, 0.5, 0.5 + (i + 1) * pw, 0.5 + H)))
        for i in range(b):
            s.append(f'<rect x="{0.5 + i * pw:.2f}" y="0.5" width="{pw:.2f}" height="{H}" fill="none" {_ST}/>')
        return Art("".join(s), W + 1, H + 1, 0.9, dict(kind="fraction", parts=b, shaded=a, shape="bar"))
    r = 8.5; cx = cy = r + 0.5
    for i in range(b):
        a0 = -math.pi / 2 + 2 * math.pi * i / b; a1 = -math.pi / 2 + 2 * math.pi * (i + 1) / b
        x0, y0, x1, y1 = cx + r * math.cos(a0), cy + r * math.sin(a0), cx + r * math.cos(a1), cy + r * math.sin(a1)
        if i < a:
            pts = [(cx, cy)] + [(cx + r * math.cos(a0 + (a1 - a0) * k / 12), cy + r * math.sin(a0 + (a1 - a0) * k / 12)) for k in range(13)]
            s.append(_hatch(Polygon(pts)))
        s.append(f'<path d="M{cx},{cy} L{x0:.2f},{y0:.2f} A{r},{r} 0 {1 if (a1 - a0) > math.pi else 0} 1 {x1:.2f},{y1:.2f} Z" fill="none" {_ST}/>')
    return Art("".join(s), 2 * r + 1, 2 * r + 1, 0.9, dict(kind="fraction", parts=b, shaded=a, shape="circle"))

def _star(cx, cy, r=1.5):
    """a small outline star: the countable object used instead of a bare black dot (audit 3 follow-up: friendlier pictures for 6 and 7 year olds)"""
    pts = " ".join(f"{cx + (r if i % 2 == 0 else r * 0.42) * math.sin(i * math.pi / 5):.2f},{cy - (r if i % 2 == 0 else r * 0.42) * math.cos(i * math.pi / 5):.2f}" for i in range(10))
    return f'<polygon points="{pts}" fill="#fff" stroke="#000" stroke-width="0.32" stroke-linejoin="round"/>'

def groups(n, per):
    """n boxes with `per` stars in each (equal groups)"""
    P_ = 3.3                                                   # star pitch
    cols = max(1, math.ceil(per / 2)); rows = 2 if per > 1 else 1
    bw, bh = cols * P_ + 1.6, rows * P_ + 1.6
    per_row = max(1, min(n, int(50 // (bw + 2.2))))
    s = []
    for g in range(n):
        gx = (g % per_row) * (bw + 2.2) + 0.5; gy = (g // per_row) * (bh + 2.2) + 0.5
        s.append(f'<rect x="{gx:.2f}" y="{gy:.2f}" width="{bw:.2f}" height="{bh:.2f}" rx="1.2" fill="#fff" {_ST}/>')
        for k in range(per):
            s.append(_star(gx + 0.8 + P_ / 2 + (k % cols) * P_, gy + 0.8 + P_ / 2 + (k // cols) * P_))
    nrows = math.ceil(n / per_row)
    return Art("".join(s), per_row * (bw + 2.2) - 1.2, nrows * (bh + 2.2) - 1.2, 0.9, dict(kind="groups", n=n, per=per))

def array(r, c):
    """r rows of c stars"""
    s = [_star(1.8 + j * 3.6, 1.8 + i * 3.6) for i in range(r) for j in range(c)]
    return Art("".join(s), c * 3.6 + 0.2, r * 3.6 + 0.2, 0.9, dict(kind="array", rows=r, cols=c))

def balance(n, total, unit):
    """n identical objects on the left pan balance one block of `total` units on the right pan"""
    s = ['<line x1="8" y1="5" x2="36" y2="5" stroke="#000" stroke-width="0.6" stroke-linecap="round"/>',
         '<line x1="22" y1="5" x2="22" y2="19" stroke="#000" stroke-width="0.6"/><line x1="16" y1="19" x2="28" y2="19" stroke="#000" stroke-width="0.7" stroke-linecap="round"/>']
    for cx in (8, 36):
        s.append(f'<path d="M{cx},5 L{cx - 7},14 M{cx},5 L{cx + 7},14" fill="none" {_ST}/><line x1="{cx - 8}" y1="14" x2="{cx + 8}" y2="14" stroke="#000" stroke-width="0.7" stroke-linecap="round"/>')
    per = 3 if n > 3 else n
    for k in range(n):
        s.append(f'<circle cx="{8 - (per - 1) * 2.4 + (k % per) * 4.8:.2f}" cy="{14 - 2.0 - (k // per) * 4.0:.2f}" r="1.9" fill="#fff" {_ST}/>')
    s.append(f'<rect x="29" y="7.6" width="14" height="6.4" rx="0.8" fill="#fff" {_ST}/>' + _text(36, 10.9, f"{total} {unit}", 3.1))
    return Art("".join(s), 44, 20, 0.9, dict(kind="balance", n=n, total=total, unit=unit))

GRAPH_FONT = 3.8                                  # mm: row labels and the key of a picture graph (never smaller than 3.5 mm on the page; the art is not scaled down)
SYM_R = 2.1                                       # half the size of one picture symbol: a symbol is 4.2 mm across

def _sym(name, cx, cy, r=SYM_R):
    """one ORIGINAL picture symbol (a simple black-line drawing of the thing counted, white inside) about 2r mm across; no two things share a drawing"""
    w = 0.38
    def P(x, y): return f"{cx + x * r:.2f},{cy + y * r:.2f}"
    def C(x, y, rr, fill="#fff"): return f'<circle cx="{cx + x * r:.2f}" cy="{cy + y * r:.2f}" r="{rr * r:.2f}" fill="{fill}" stroke="#000" stroke-width="{w}"/>'
    def dot(x, y, rr=0.13): return C(x, y, rr, "#000")
    def poly(pts, fill="#fff"): return f'<polygon points="{" ".join(P(x, y) for x, y in pts)}" fill="{fill}" stroke="#000" stroke-width="{w}" stroke-linejoin="round"/>'
    def line(x1, y1, x2, y2, sw=w): return f'<line x1="{cx + x1 * r:.2f}" y1="{cy + y1 * r:.2f}" x2="{cx + x2 * r:.2f}" y2="{cy + y2 * r:.2f}" stroke="#000" stroke-width="{sw}" stroke-linecap="round"/>'
    def path(d, fill="none"): return f'<path d="{d}" fill="{fill}" stroke="#000" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>'
    def E(x, y, rx, ry, fill="#fff"): return f'<ellipse cx="{cx + x * r:.2f}" cy="{cy + y * r:.2f}" rx="{rx * r:.2f}" ry="{ry * r:.2f}" fill="{fill}" stroke="#000" stroke-width="{w}"/>'
    def rect(x, y, ww, hh, fill="#fff"): return f'<rect x="{cx + x * r:.2f}" y="{cy + y * r:.2f}" width="{ww * r:.2f}" height="{hh * r:.2f}" rx="{0.12 * r:.2f}" fill="{fill}" stroke="#000" stroke-width="{w}" stroke-linejoin="round"/>'
    if name == "cat":                     # round head, two pointed ears, eyes, whiskers
        return poly([(-0.85, -0.05), (-0.8, -1.0), (-0.2, -0.55)]) + poly([(0.85, -0.05), (0.8, -1.0), (0.2, -0.55)]) + C(0, 0.2, 0.85) + dot(-0.33, 0.05) + dot(0.33, 0.05) + line(-1.0, 0.45, -0.45, 0.4, 0.25) + line(1.0, 0.45, 0.45, 0.4, 0.25)
    if name == "dog":                     # head with two long black hanging ears and a black nose
        return poly([(-0.6, -0.8), (-1.05, 0.35), (-0.4, -0.05)], "#000") + poly([(0.6, -0.8), (1.05, 0.35), (0.4, -0.05)], "#000") + C(0, 0.1, 0.72) + dot(-0.27, -0.05) + dot(0.27, -0.05) + E(0, 0.38, 0.26, 0.18, "#000")
    if name == "fish":                    # body, three-corner tail, eye
        return E(-0.2, 0, 0.7, 0.5) + poly([(0.45, 0), (1.0, -0.55), (1.0, 0.55)]) + dot(-0.55, -0.1, 0.12)
    if name == "hen":                     # round body, small head with comb and beak, tail
        return poly([(0.55, 0.25), (1.0, -0.4), (0.9, 0.55)]) + C(0.05, 0.3, 0.7) + C(-0.5, -0.45, 0.35) + poly([(-0.65, -0.78), (-0.5, -1.05), (-0.35, -0.78)], "#000") + poly([(-0.82, -0.45), (-1.1, -0.35), (-0.82, -0.28)], "#000") + dot(-0.45, -0.5, 0.07)
    if name == "pie":                     # round pie with a wavy crust ring and three cut lines
        return C(0, 0, 0.95) + C(0, 0, 0.65) + line(0, -0.65, 0, 0.65, 0.3) + line(-0.56, -0.32, 0.56, 0.32, 0.3) + line(-0.56, 0.32, 0.56, -0.32, 0.3)
    if name == "bun":                     # dome on a flat base with a black dot top
        return path(f"M{P(-0.95, 0.6)} A{0.95 * r:.2f},{1.2 * r:.2f} 0 0 1 {P(0.95, 0.6)} Z", "#fff") + dot(0, -0.55, 0.16) + line(-0.3, 0.05, 0.3, 0.05, 0.3)
    if name == "cake":                    # two layers and a candle with a flame
        return rect(-0.95, 0.0, 1.9, 0.85) + rect(-0.6, -0.55, 1.2, 0.55) + line(0, -0.55, 0, -0.95, 0.5) + poly([(0, -1.2), (-0.15, -0.95), (0.15, -0.95)], "#000")
    if name == "tart":                    # a small cup shape with a black cherry on top
        return poly([(-0.95, -0.1), (0.95, -0.1), (0.6, 0.85), (-0.6, 0.85)]) + path(f"M{P(-0.95, -0.1)} Q{P(0, -0.8)} {P(0.95, -0.1)}") + dot(0, -0.62, 0.2)
    if name == "car":                     # body, cabin with window, two black wheels
        return poly([(-1.0, 0.45), (-1.0, 0.0), (-0.55, -0.1), (-0.3, -0.6), (0.4, -0.6), (0.7, -0.1), (1.0, 0.0), (1.0, 0.45)]) + line(0.05, -0.6, 0.05, -0.1, 0.3) + C(-0.55, 0.5, 0.3, "#000") + C(0.55, 0.5, 0.3, "#000")
    if name == "doll":                    # round head with hair dots and a triangle dress
        return poly([(0, -0.1), (-0.8, 1.0), (0.8, 1.0)]) + C(0, -0.65, 0.4) + dot(-0.12, -0.7, 0.06) + dot(0.12, -0.7, 0.06) + line(-0.4, -0.4, -0.85, 0.2, 0.4) + line(0.4, -0.4, 0.85, 0.2, 0.4)
    if name == "ball":                    # a ball with two curved seams
        return C(0, 0, 0.95) + path(f"M{P(-0.67, -0.67)} Q{P(0, 0)} {P(-0.67, 0.67)}") + path(f"M{P(0.67, -0.67)} Q{P(0, 0)} {P(0.67, 0.67)}")
    if name == "kite":                    # diamond, cross and a tail with bows
        return poly([(0, -1.0), (0.7, -0.2), (0, 0.5), (-0.7, -0.2)]) + line(0, -1.0, 0, 0.5, 0.25) + line(-0.7, -0.2, 0.7, -0.2, 0.25) + path(f"M{P(0, 0.5)} Q{P(0.4, 0.7)} {P(0, 0.85)} T{P(0, 1.1)}") + dot(0.18, 0.72, 0.1)
    if name == "pen":                     # a slanted pen: body, clip line and a black tip
        return poly([(-0.95, 0.95), (-0.95, 0.55), (0.55, -0.95), (0.95, -0.55), (-0.55, 0.95)], "#fff") + poly([(-0.95, 0.95), (-0.95, 0.55), (-0.55, 0.95)], "#000") + line(0.35, -0.75, 0.75, -0.35, 0.3)
    if name == "cup":                     # tall cup with a handle
        return path(f"M{P(0.7, -0.4)} Q{P(1.3, -0.4)} {P(1.0, 0.25)} Q{P(0.9, 0.5)} {P(0.5, 0.4)}") + poly([(-0.85, -0.7), (0.75, -0.7), (0.55, 0.85), (-0.65, 0.85)]) + line(-0.8, -0.3, 0.7, -0.3, 0.3)
    if name == "hat":                     # a hat: tall crown with a black band and a wide brim
        return rect(-0.55, -0.85, 1.1, 1.1) + rect(-0.55, -0.1, 1.1, 0.35, "#000") + E(0, 0.45, 1.05, 0.3)
    if name == "bag":                     # a bag with a handle arc and a flap line
        return path(f"M{P(-0.45, -0.35)} C{P(-0.45, -1.2)} {P(0.45, -1.2)} {P(0.45, -0.35)}") + poly([(-0.85, -0.35), (0.85, -0.35), (0.95, 0.95), (-0.95, 0.95)]) + line(-0.9, 0.1, 0.9, 0.1, 0.3)
    return _face(cx, cy, r * 0.8)

def _face(cx, cy, r=1.8):
    """a small face: the fallback symbol for a label without a drawing"""
    return (f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r="{r}" fill="#fff" stroke="#000" stroke-width="0.4"/>'
            f'<circle cx="{cx - r * 0.38:.2f}" cy="{cy - r * 0.22:.2f}" r="0.28" fill="#000"/><circle cx="{cx + r * 0.38:.2f}" cy="{cy - r * 0.22:.2f}" r="0.28" fill="#000"/>'
            f'<path d="M{cx - r * 0.5:.2f},{cy + r * 0.25:.2f} Q{cx:.2f},{cy + r * 0.85:.2f} {cx + r * 0.5:.2f},{cy + r * 0.25:.2f}" fill="none" stroke="#000" stroke-width="0.3" stroke-linecap="round"/>')

SYM_NAME = {"cats": "cat", "dogs": "dog", "fish": "fish", "hens": "hen", "pies": "pie", "buns": "bun", "cakes": "cake", "tarts": "tart",
            "cars": "car", "dolls": "doll", "balls": "ball", "kites": "kite", "pens": "pen", "cups": "cup", "hats": "hat", "bags": "bag"}

def picgraph(rows, key, blank=False, pitch=5.2, font=None):
    """picture graph: rows = [(label, icons)]; every row is drawn with the thing it counts (a car for Cars, a pie for Pies), 4.2 mm across, and each symbol stands for `key`.
    Labels are 3.5 to 3.8 mm; one row is 5.2 mm high. The key reads "Each picture = key" under the rows, with the first row's symbol drawn once as an example."""
    import metrics
    RH, PITCH, F = 5.2, pitch, (font or GRAPH_FONT)
    LW = max(metrics.width(lab, F, 600) for lab, _ in rows) + 1.6
    mx = max(c for _, c in rows)
    w = LW + mx * PITCH + 0.8
    s = []
    for i, (lab, c) in enumerate(rows):
        y = 0.5 + i * RH + RH / 2
        s.append(_text(0.5, y, lab, F, 600, "start"))
        sym = SYM_NAME.get(lab.lower(), "")
        for k in range(c): s.append(_sym(sym, LW + 2.8 + k * PITCH, y))
        s.append(f'<line x1="0.5" y1="{0.5 + (i + 1) * RH:.2f}" x2="{w:.2f}" y2="{0.5 + (i + 1) * RH:.2f}" stroke="#000" stroke-width="0.3"/>')
    if blank:       # a drawn answer box after the last symbols (a one-row graph whose answer is written beside it)
        bx = LW + 2.8 + (rows[0][1] - 0.5) * PITCH + 1.8
        s.append(f'<rect x="{bx:.2f}" y="{0.5 + RH / 2 - 2.0:.2f}" width="4.0" height="4.0" rx="0.5" fill="#fff" stroke="#000" stroke-width="0.45"/>')
        w = max(w, bx + 4.6)
    yk = 0.5 + len(rows) * RH + 3.0
    s.append(_text(0.5, yk, f"Each picture = {key}", F, 700, "start"))
    w = max(w, 0.5 + metrics.width(f"Each picture = {key}", F, 700) + 0.5)
    return Art("".join(s), w, len(rows) * RH + 6.0, 0.95, dict(kind="picgraph", rows=[list(r) for r in rows], key=key, blank=blank, font=F))

def queue(n, k):
    """a row of n children (small squares with a round head), the k-th from the left drawn black: ordinal position"""
    s = []
    for i in range(n):
        x = 0.5 + i * 3.9; fill = "#000" if i + 1 == k else "#fff"
        s.append(f'<circle cx="{x + 1.6:.2f}" cy="1.5" r="1.2" fill="{fill}" {_ST}/><rect x="{x:.2f}" y="3.0" width="3.2" height="3.6" rx="0.5" fill="{fill}" {_ST}/>')
    return Art("".join(s), n * 3.9 + 0.1, 7.2, 0.85, dict(kind="queue", n=n, k=k))

def tally(n):
    """tally marks in fives (four strokes and a slash)"""
    s = []; x = 0.5
    for g in range(n // 5):
        for k in range(4): s.append(f'<line x1="{x + k * 1.6:.2f}" y1="0.8" x2="{x + k * 1.6:.2f}" y2="6.2" stroke="#000" stroke-width="0.55" stroke-linecap="round"/>')
        s.append(f'<line x1="{x - 0.8:.2f}" y1="5.2" x2="{x + 5.6:.2f}" y2="1.8" stroke="#000" stroke-width="0.55" stroke-linecap="round"/>'); x += 8.0
    for k in range(n % 5): s.append(f'<line x1="{x + k * 1.6:.2f}" y1="0.8" x2="{x + k * 1.6:.2f}" y2="6.2" stroke="#000" stroke-width="0.55" stroke-linecap="round"/>')
    w = x + (n % 5) * 1.6 + (0.5 if n % 5 else -1.5)
    return Art("".join(s), max(w, 4.0), 7.0, 0.9, dict(kind="tally", n=n))

def _solid(kind):
    f = f'fill="#fff" {_ST}'
    if kind == "cube":
        return (f'<polygon points="0.5,4.5 9.5,4.5 13,1 4,1" {f}/><polygon points="9.5,4.5 13,1 13,10 9.5,13.5" {f}/><rect x="0.5" y="4.5" width="9" height="9" {f}/>', 13.5, 14.0)
    if kind == "cuboid":
        return (f'<polygon points="0.5,5 13,5 17,1.5 4.5,1.5" {f}/><polygon points="13,5 17,1.5 17,9 13,12.5" {f}/><rect x="0.5" y="5" width="12.5" height="7.5" {f}/>', 17.5, 13.0)
    if kind == "cylinder":
        return (f'<path d="M0.5,3.5 L0.5,12 A6.5,2.5 0 0 0 13.5,12 L13.5,3.5" {f}/><ellipse cx="7" cy="3.5" rx="6.5" ry="2.5" {f}/>', 14.0, 15.0)
    if kind == "cone":
        return (f'<path d="M7,0.5 L0.5,12 A6.5,2.5 0 0 0 13.5,12 Z" {f}/>', 14.0, 15.0)
    if kind == "sphere":
        return (f'<circle cx="7" cy="7" r="6.5" {f}/><path d="M0.5,7 A6.5,2 0 0 0 13.5,7" fill="none" {_ST}/>', 14.0, 14.0)
    raise KeyError(kind)
SOLID_FLAT = {"cube": 6, "cuboid": 6, "cylinder": 2, "cone": 1, "sphere": 0}
SOLID_CURVED = {"cube": 0, "cuboid": 0, "cylinder": 1, "cone": 1, "sphere": 1}
def solids(kinds):
    x = 0.0; s = []; h = 15.0; k_ = 0.74            # drawn at 74 % so that a solid is 11 mm high and fits the small labels
    for k in kinds:
        svg, w, hh = _solid(k)
        s.append(f'<g transform="translate({x:.2f},{(h - hh) * k_:.2f}) scale({k_})">{svg}</g>'); x += (w + 3.0) * k_
    return Art("".join(s), x - 3.0 * k_, h * k_, 0.9, dict(kind="solids", kinds=list(kinds)))

def _mini(kind):
    f = f'fill="#fff" {_ST}'
    if kind == "triangle": return f'<polygon points="0.4,6.6 7.6,6.6 4,0.4" {f}/>', 8.0, 7.0
    if kind == "square": return f'<rect x="0.4" y="0.4" width="6.4" height="6.4" {f}/>', 7.2, 7.2
    if kind == "rectangle": return f'<rect x="0.4" y="1.4" width="9.6" height="5.2" {f}/>', 10.4, 7.2
    if kind == "circle": return f'<circle cx="3.8" cy="3.8" r="3.4" {f}/>', 7.6, 7.6
    if kind == "semicircle": return f'<path d="M0.4,6.4 A3.8,3.8 0 0 1 8,6.4 Z" {f}/>', 8.4, 6.8
    if kind == "quarter": return f'<path d="M0.4,6.8 L0.4,0.4 A6.4,6.4 0 0 1 6.8,6.8 Z" {f}/>', 7.2, 7.2
    raise KeyError(kind)
# straight sides and corners of the flat shapes (a semicircle has one straight side and two corners; a quarter circle two straight sides and three corners)
SIDES = {"triangle": 3, "square": 4, "rectangle": 4, "circle": 0, "semicircle": 1, "quarter": 2}
def shapes_row(kinds):
    x = 0.0; s = []
    for k in kinds:
        svg, w, h = _mini(k)
        s.append(f'<g transform="translate({x:.2f},{(7.6 - h) / 2:.2f})">{svg}</g>'); x += w + 1.8
    return Art("".join(s), x - 1.8, 7.6, 0.85, dict(kind="shapes_row", kinds=list(kinds)))

def pattern_row(seq):
    """the first shapes of a repeating pattern (circle, square, triangle) followed by three dots"""
    x = 0.0; s = []
    for k in seq:
        svg, w, h = _mini(k)
        s.append(f'<g transform="translate({x + (8.4 - w) / 2:.2f},{(7.6 - h) / 2:.2f})">{svg}</g>'); x += 9.4
    s.append(_text(x + 1.2, 6.2, "...", 4.2, 700, "start"))
    return Art("".join(s), x + 7.0, 7.6, 0.85, dict(kind="pattern_row", seq=list(seq)))

def blocks(h, t, o):
    """base-ten blocks: h flats, t tens sticks, o ones"""
    s = []; x = 0.5
    f = f'fill="#fff" {_ST}'
    for _ in range(h):
        s.append(f'<rect x="{x:.2f}" y="0.5" width="6" height="6" {f}/><path d="M{x + 2:.2f},0.5 V6.5 M{x + 4:.2f},0.5 V6.5 M{x:.2f},2.5 H{x + 6:.2f} M{x:.2f},4.5 H{x + 6:.2f}" stroke="#000" stroke-width="0.3" fill="none"/>'); x += 7.0
    if h: x += 1.5
    for _ in range(t):
        s.append(f'<rect x="{x:.2f}" y="0.5" width="1.9" height="6" {f}/><path d="M{x:.2f},2.5 H{x + 1.9:.2f} M{x:.2f},4.5 H{x + 1.9:.2f}" stroke="#000" stroke-width="0.3" fill="none"/>'); x += 2.9
    if t: x += 1.5
    for _ in range(o):
        s.append(f'<rect x="{x:.2f}" y="3.9" width="2.0" height="2.0" {f}/>'); x += 2.8
    return Art("".join(s), x - 0.3, 7.0, 0.9, dict(kind="blocks", h=h, t=t, o=o))

def cash(values):
    """money in cents: coins 5, 10, 20, 50, 100 and notes 200, 500, 1000, drawn as plain labelled shapes"""
    x = 0.0; s = []; hh = 13.8
    for v in sorted(values, reverse=True):
        if v >= 200:
            s.append(f'<rect x="{x + 0.5:.2f}" y="3.4" width="13" height="7" rx="0.8" fill="#fff" {_ST}/>' + _text(x + 7, 6.9, f"${v // 100}", 3.6)); x += 14.2
        else:
            r = COIN_R[v]; x += r
            s.append(_coin(x, hh / 2, v, r)); x += r + 1.2
    return Art("".join(s), x - 1.2, hh, 0.85, dict(kind="cash", values=sorted(values, reverse=True)))
