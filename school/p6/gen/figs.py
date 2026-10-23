"""Figures drawn as inline SVG (pure black and white, strokes at least 0.5 mm): circles, semicircles, quarter circles and composite figures.
Every figure carries a class naming its kind and text labels (class lab) that a reader sees; read_fig() recovers the kind and the labels from the PRINTED svg only."""
import math, re
from fractions import Fraction as Fr

SW = 0.55           # stroke width in mm

def _svg(w, h, inner, cls="fig-svg", defs=""):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" class="{cls}" viewBox="0 0 {w:.1f} {h:.1f}" width="{w:.1f}mm" height="{h:.1f}mm">'
            + (f"<defs>{defs}</defs>" if defs else "") + inner + "</svg>")

def _t(x, y, s, anchor="middle", size=3.9, cls="lab", bold=True):
    return (f'<text class="{cls}" x="{x:.2f}" y="{y:.2f}" text-anchor="{anchor}" dominant-baseline="central" font-family="Nunito Sans" '
            f'font-weight="{800 if bold else 400}" font-size="{size}" fill="#000" stroke="#fff" stroke-width="1.0" paint-order="stroke" stroke-linejoin="round">{s}</text>')

def _hatch_id(tag):
    return f"h{tag}"

def hatch_def(tag):
    return f'<pattern id="{_hatch_id(tag)}" width="2.0" height="2.0" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="2.0" stroke="#000" stroke-width="0.55"/></pattern>'

def lab(v, unit="cm", kind=""):
    return f"{kind}{v} {unit}"

# ------------------------------------------------------------------ circle, semicircle, quarter circle
def circle_fig(r_label, which="r", unit="cm", size=26):
    """a circle with its radius (or diameter) marked; the label is printed under the circle"""
    R = size * 0.36; cx = size / 2; cy = R + 1.5; H = cy + R + 5.6
    inner = f'<circle class="circ" cx="{cx}" cy="{cy}" r="{R}" fill="#fff" stroke="#000" stroke-width="{SW}"/><circle cx="{cx}" cy="{cy}" r="0.9" fill="#000"/>'
    if which == "r":
        inner += f'<line x1="{cx}" y1="{cy}" x2="{cx+R}" y2="{cy}" stroke="#000" stroke-width="{SW}"/>' + _t(cx, cy + R + 3.2, f"r = {r_label} {unit}")
    else:
        inner += f'<line x1="{cx-R}" y1="{cy}" x2="{cx+R}" y2="{cy}" stroke="#000" stroke-width="{SW}"/>' + _t(cx, cy + R + 3.2, f"d = {r_label} {unit}")
    return _svg(size, H, inner, "fig-svg fig-circle")

def semicircle_fig(d, unit="cm", w=34):
    R = w * 0.40; cx = w / 2; y0 = R + 4.5; H = y0 + 8
    inner = (f'<path class="semi" d="M{cx-R},{y0} A{R},{R} 0 0 1 {cx+R},{y0} Z" fill="#fff" stroke="#000" stroke-width="{SW}" stroke-linejoin="round"/>'
             + _t(cx, y0 + 4.6, f"d = {d} {unit}"))
    return _svg(w, H, inner, "fig-svg fig-semi")

def quarter_fig(r, unit="cm", w=28):
    R = w * 0.66; x0 = 4.5; y0 = R + 2.5; H = y0 + 6.2
    inner = (f'<path class="quarter" d="M{x0},{y0} L{x0},{y0-R} A{R},{R} 0 0 1 {x0+R},{y0} Z" fill="#fff" stroke="#000" stroke-width="{SW}" stroke-linejoin="round"/>'
             f'<path d="M{x0+2.6},{y0} L{x0+2.6},{y0-2.6} L{x0},{y0-2.6}" fill="none" stroke="#000" stroke-width="0.4"/>'
             + _t(x0 + R * 0.5, y0 + 3.6, f"r = {r} {unit}"))
    return _svg(x0 + R + 3, H, inner, "fig-svg fig-quarter")

# ------------------------------------------------------------------ composite figures
def rect_semi_fig(L, W, unit="cm", box=(48, 29)):
    """a rectangle L by W with a semicircle of diameter W on its right end; L is labelled on top, W on the left side"""
    bw, bh = box; k = min((bw - 17) / (L + W / 2), (bh - 10) / W)
    l, w = L * k, W * k; x0 = 13; y0 = (bh - w) / 2 + 1
    d = f"M{x0},{y0} L{x0+l},{y0} A{w/2},{w/2} 0 0 1 {x0+l},{y0+w} L{x0},{y0+w} Z"
    inner = (f'<path class="rsemi" d="{d}" fill="#fff" stroke="#000" stroke-width="{SW}" stroke-linejoin="round"/>'
             f'<line x1="{x0+l}" y1="{y0}" x2="{x0+l}" y2="{y0+w}" stroke="#000" stroke-width="0.35" stroke-dasharray="1.2 1"/>'
             + _t(x0 + l / 2, y0 - 2.6, f"{L} {unit}", cls="lab top", size=3.7) + _t(x0 - 1.2, y0 + w / 2, f"{W} {unit}", anchor="end", cls="lab left", size=3.7))
    return _svg(bw, bh, inner, "fig-svg fig-rsemi")

def sq_semi_fig(s, unit="cm", box=(36, 38)):
    """a square of side s with a semicircle of diameter s on top; the side is dimensioned on the left and the lower part is labelled 'square'"""
    bw, bh = box; a = min(bw - 17, (bh - 8) / 1.5); x0 = bw - 3.5 - a; y0 = bh - 4 - a
    d = f"M{x0},{y0+a} L{x0},{y0} A{a/2},{a/2} 0 0 1 {x0+a},{y0} L{x0+a},{y0+a} Z"
    xd = x0 - 2.2
    inner = (f'<path class="ssemi" d="{d}" fill="#fff" stroke="#000" stroke-width="{SW}" stroke-linejoin="round"/>'
             f'<line x1="{x0}" y1="{y0}" x2="{x0+a}" y2="{y0}" stroke="#000" stroke-width="0.35" stroke-dasharray="1.2 1"/>'
             f'<line x1="{xd}" y1="{y0}" x2="{xd}" y2="{y0+a}" stroke="#000" stroke-width="0.4"/>'
             f'<line x1="{xd-1}" y1="{y0}" x2="{xd+1}" y2="{y0}" stroke="#000" stroke-width="0.4"/><line x1="{xd-1}" y1="{y0+a}" x2="{xd+1}" y2="{y0+a}" stroke="#000" stroke-width="0.4"/>'
             + _t(xd - 1.3, y0 + a / 2, f"{s} {unit}", anchor="end", cls="lab top", size=3.7)
             + f'<text class="sqw" x="{x0 + a / 2:.2f}" y="{y0 + a / 2 + 0.5:.2f}" text-anchor="middle" dominant-baseline="central" font-family="Nunito Sans" font-weight="700" font-size="3.6" fill="#000">square</text>')
    return _svg(bw, bh, inner, "fig-svg fig-ssemi")

def sq_minus_quarter_fig(s, tag, unit="cm", box=(36, 36)):
    """a square of side s; a quarter circle of radius s (centre at the lower-left corner) is cut away; the part left (hatched) is shaded"""
    bw, bh = box; k = (bw - 9) / s; a = s * k; x0 = 5.5; y0 = (bh - a) / 2
    sq = f"M{x0},{y0} L{x0+a},{y0} L{x0+a},{y0+a} L{x0},{y0+a} Z"
    shaded = f"M{x0},{y0} L{x0+a},{y0} L{x0+a},{y0+a} A{a},{a} 0 0 0 {x0},{y0} Z"
    inner = (f'<path d="{sq}" fill="#fff" stroke="#000" stroke-width="{SW}" stroke-linejoin="round"/>'
             f'<path class="sqq" d="{shaded}" fill="url(#{_hatch_id(tag)})" stroke="#000" stroke-width="{SW}" stroke-linejoin="round"/>'
             + _t(x0 + a / 2, y0 - 2.4, f"{s} {unit}", cls="lab top", size=3.6) )
    return _svg(bw, bh, inner, "fig-svg fig-sqq", defs=hatch_def(tag))

# ------------------------------------------------------------------ readers (from the PRINTED svg text only)
def read_fig(s):
    """{'kind': class of the figure, 'labels': [text of every lab text, in order]}"""
    kind = re.search(r'class="fig-svg (fig-\w+)"', s).group(1)
    texts = re.findall(r'<text class="lab ?(\w*)"[^>]*>(.*?)</text>', s)
    labels = [(pos, re.sub(r"<[^>]+>", "", t).strip()) for pos, t in texts]
    return dict(kind=kind, labels=[l for _, l in labels if l], pos={p or "main": l for p, l in labels if l})

def num_of(label):
    m = re.search(r"(\d+(?:\.\d+)?)", label)
    return Fr(m.group(1))

def cuboid_fig(l, b, h, unit="cm", box=(40, 31)):
    """a cuboid in oblique view; each edge label is its length or ? when the length is wanted (class lab l / b / h)"""
    bw, bh = box; fw, fh_ = 18.0, 11.0; dx, dy = 7.0, -5.5; x0 = 12.5; y0 = bh - 5.0
    def pt(x, y): return f"{x:.2f},{y:.2f}"
    front = f"{pt(x0, y0)} {pt(x0+fw, y0)} {pt(x0+fw, y0-fh_)} {pt(x0, y0-fh_)}"
    top = f"{pt(x0, y0-fh_)} {pt(x0+dx, y0-fh_+dy)} {pt(x0+fw+dx, y0-fh_+dy)} {pt(x0+fw, y0-fh_)}"
    side = f"{pt(x0+fw, y0)} {pt(x0+fw+dx, y0+dy)} {pt(x0+fw+dx, y0-fh_+dy)} {pt(x0+fw, y0-fh_)}"
    s = lambda v: "?" if v is None else f"{v} {unit}"
    inner = (f'<polygon points="{front}" fill="#fff" stroke="#000" stroke-width="{SW}" stroke-linejoin="round"/>'
             f'<polygon points="{top}" fill="#fff" stroke="#000" stroke-width="{SW}" stroke-linejoin="round"/>'
             f'<polygon points="{side}" fill="#fff" stroke="#000" stroke-width="{SW}" stroke-linejoin="round"/>'
             + _t(x0 + fw / 2, y0 + 3.2, s(l), cls="lab l") + _t(x0 - 1.2, y0 - fh_ / 2, s(h), anchor="end", cls="lab h")
             + _t(x0 + fw + dx / 2, y0 - fh_ + dy - 2.6, s(b), anchor="middle", cls="lab b"))
    return _svg(bw, bh, inner, "fig-svg fig-cuboid")

def rect_tri_fig(L, W, h, unit="cm", box=(50, 38)):
    """a rectangle L by W with a triangle of height h on top of its side L; L is labelled under the figure, W on the left, and the height h on a
    dimension line to the right (so no label touches a drawn line)"""
    bw, bh = box; k = min((bw - 28) / L, (bh - 10) / (W + h)); l, w, t = L * k, W * k, h * k
    x0 = 13; y1 = bh - 5.5; y0 = y1 - w; ya = y0 - t; xd = x0 + l + 4
    d = f"M{x0},{y1} L{x0+l},{y1} L{x0+l},{y0} L{x0+l/2},{ya} L{x0},{y0} Z"
    inner = (f'<path class="rtri" d="{d}" fill="#fff" stroke="#000" stroke-width="{SW}" stroke-linejoin="round"/>'
             f'<line x1="{x0}" y1="{y0}" x2="{x0+l}" y2="{y0}" stroke="#000" stroke-width="0.35" stroke-dasharray="1.2 1"/>'
             f'<line x1="{x0+l/2}" y1="{ya}" x2="{xd+1.2}" y2="{ya}" stroke="#000" stroke-width="0.3"/>'
             f'<line x1="{x0+l}" y1="{y0}" x2="{xd+1.2}" y2="{y0}" stroke="#000" stroke-width="0.3"/>'
             f'<line x1="{xd}" y1="{ya}" x2="{xd}" y2="{y0}" stroke="#000" stroke-width="0.4"/>'
             f'<polyline points="{xd-0.9},{ya+1.8} {xd},{ya} {xd+0.9},{ya+1.8}" fill="none" stroke="#000" stroke-width="0.4"/>'
             f'<polyline points="{xd-0.9},{y0-1.8} {xd},{y0} {xd+0.9},{y0-1.8}" fill="none" stroke="#000" stroke-width="0.4"/>'
             + _t(x0 + l / 2, y1 + 3.3, f"{L} {unit}", cls="lab top") + _t(x0 - 1.2, y0 + w / 2, f"{W} {unit}", anchor="end", cls="lab left")
             + _t(xd + 1.8, (ya + y0) / 2, f"{h} {unit}", anchor="start", cls="lab hgt", size=3.6))
    return _svg(bw, bh, inner, "fig-svg fig-rtri")

def sq_minus_semi_fig(s, tag, unit="cm", box=(36, 36)):
    """a square of side s with a semicircle (diameter s, on the top side) cut away; the part left is hatched"""
    bw, bh = box; k = (bw - 9) / s; a = s * k; x0 = 5.5; y0 = (bh - a) / 2 + 1
    shaded = f"M{x0},{y0} A{a/2},{a/2} 0 0 0 {x0+a},{y0} L{x0+a},{y0+a} L{x0},{y0+a} Z"
    inner = (f'<rect x="{x0}" y="{y0}" width="{a}" height="{a}" fill="#fff" stroke="#000" stroke-width="{SW}"/>'
             f'<path class="sqs" d="{shaded}" fill="url(#{_hatch_id(tag)})" stroke="#000" stroke-width="{SW}" stroke-linejoin="round"/>'
             + _t(x0 + a / 2, y0 + a + 3.0, f"{s} {unit}", cls="lab top", size=3.6))
    return _svg(bw, bh + 2, inner, "fig-svg fig-sqs", defs=hatch_def(tag))

# ------------------------------------------------------------------ pie chart
def pie_fig(sectors, tag="p", W=100.0, H=52.0, R=17.0):
    """sectors: list of (name, pct, hidden); drawn clockwise from the top. A hidden sector prints ? instead of its percentage.
    Each sector is a path whose end points give its angle; the name and percentage are text labels outside the pie."""
    cx, cy = W / 2, H / 2 + 2.0
    out = []; a = -math.pi / 2
    for name, pct, hidden in sectors:
        span = 2 * math.pi * pct / 100; a0, a1 = a, a + span
        x1, y1 = cx + R * math.cos(a0), cy + R * math.sin(a0); x2, y2 = cx + R * math.cos(a1), cy + R * math.sin(a1)
        large = 1 if span > math.pi else 0
        out.append(f'<path class="sec" data-name="{name}" d="M{cx:.2f},{cy:.2f} L{x1:.3f},{y1:.3f} A{R},{R} 0 {large} 1 {x2:.3f},{y2:.3f} Z" fill="#fff" stroke="#000" stroke-width="{SW}" stroke-linejoin="round"/>')
        mid = (a0 + a1) / 2; lr = R + 4.5
        lx, ly = cx + lr * math.cos(mid), cy + lr * math.sin(mid)
        anchor = "start" if math.cos(mid) > 0.15 else "end" if math.cos(mid) < -0.15 else "middle"
        dy = -2.0 if math.sin(mid) < -0.5 else 2.0 if math.sin(mid) > 0.5 else 0
        out.append(f'<text class="slab" data-n="{name}" x="{lx:.2f}" y="{ly + dy - 1.8:.2f}" text-anchor="{anchor}" dominant-baseline="central" font-family="Nunito Sans" font-weight="800" font-size="3.9" fill="#000">{name}</text>')
        out.append(f'<text class="spc" data-n="{name}" x="{lx:.2f}" y="{ly + dy + 2.3:.2f}" text-anchor="{anchor}" dominant-baseline="central" font-family="Nunito Sans" font-weight="800" font-size="3.9" fill="#000">{"?" if hidden else str(pct) + "%"}</text>')
        a = a1
    return _svg(W, H, "".join(out), "fig-svg fig-pie")

def read_pie(s):
    """name -> (percentage measured from the sector's end points, printed percentage or None when it prints ?)"""
    cx_cy = {}
    res = {}
    for m in re.finditer(r'<path class="sec" data-name="([^"]+)" d="M([\d.]+),([\d.]+) L([\d.]+),([\d.]+) A[\d.]+,[\d.]+ 0 \d 1 ([\d.]+),([\d.]+) Z"', s):
        n, cx, cy, x1, y1, x2, y2 = m.group(1), *(float(v) for v in m.groups()[1:])
        a0 = math.atan2(y1 - cy, x1 - cx); a1 = math.atan2(y2 - cy, x2 - cx)
        d = (a1 - a0) % (2 * math.pi)
        res[n] = [d / (2 * math.pi) * 100, None]
    for m in re.finditer(r'<text class="spc" data-n="([^"]+)"[^>]*>(.*?)</text>', s):
        t = m.group(2).strip()
        res[m.group(1)][1] = None if t == "?" else int(t.rstrip("%"))
    return {k: (round(v[0], 2), v[1]) for k, v in res.items()}

# ------------------------------------------------------------------ nets
def net_fig(cells, size=8.4):
    rs = [r for r, c in cells]; cs = [c for r, c in cells]
    r0, c0 = min(rs), min(cs); h = (max(rs) - r0 + 1) * size; w = (max(cs) - c0 + 1) * size
    pad = 1.0
    out = "".join(f'<rect class="nc" data-r="{r - r0}" data-c="{c - c0}" x="{pad + (c - c0) * size:.2f}" y="{pad + (r - r0) * size:.2f}" width="{size}" height="{size}" fill="#fff" stroke="#000" stroke-width="{SW}" stroke-linejoin="round"/>' for r, c in sorted(cells))
    return _svg(w + 2 * pad, h + 2 * pad, out, "fig-svg fig-net")

def read_net(s):
    return {(int(r), int(c)) for r, c in re.findall(r'<rect class="nc" data-r="(\d+)" data-c="(\d+)"', s)}
