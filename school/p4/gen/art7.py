"""Primary 4 pictures, part 3: a line graph and a pie chart. Pure black and white. Each has a reader that recovers its data from the DRAWING only."""
import math, re
from .common import svg

def line_graph_svg(cats, vals, ymax=60, step=10, w=150.0, h=74.0, ylabel="Number of books"):
    """a line graph: x categories (names), y axis from 0 to ymax in steps of `step` with a dotted line half way between; points joined by a line"""
    L, T, R, B = 20.0, 5.0, 4.0, 14.0
    pw, ph = w - L - R, h - T - B
    X = lambda i: L + (i + 0.5) * pw / len(cats)
    Y = lambda v: T + ph - v * ph / ymax
    p = [f'<rect x="{L}" y="{T}" width="{pw}" height="{ph}" fill="#fff" stroke="#000" stroke-width="0.6"/>']
    k = 0
    while k * step <= ymax:
        v = k * step; y = Y(v)
        p.append(f'<line x1="{L}" y1="{y:.2f}" x2="{L + pw}" y2="{y:.2f}" stroke="#000" stroke-width="{0.5 if v else 0.7}"/>')
        p.append(f'<text class="yl" x="{L - 2.2}" y="{y:.2f}" text-anchor="end" dominant-baseline="central" font-family="Nunito Sans" font-weight="700" font-size="3.4" fill="#000">{v}</text>')
        if v + step / 2 < ymax: p.append(f'<line x1="{L}" y1="{Y(v + step / 2):.2f}" x2="{L + pw}" y2="{Y(v + step / 2):.2f}" stroke="#000" stroke-width="0.25" stroke-dasharray="0.8 1.2"/>')
        k += 1
    for i, c in enumerate(cats):
        p.append(f'<text class="xl" x="{X(i):.2f}" y="{T + ph + 4.4:.2f}" text-anchor="middle" dominant-baseline="central" font-family="Nunito Sans" font-weight="700" font-size="3.6" fill="#000">{c}</text>')
    pts = " ".join(f"{X(i):.2f},{Y(v):.2f}" for i, v in enumerate(vals))
    p.append(f'<polyline class="ln" points="{pts}" fill="none" stroke="#000" stroke-width="0.8" stroke-linejoin="round"/>')
    for i, v in enumerate(vals): p.append(f'<circle class="pt" cx="{X(i):.2f}" cy="{Y(v):.2f}" r="1.2" fill="#000"/>')
    p.append(f'<text x="{L + pw / 2:.2f}" y="{h - 1.8:.2f}" text-anchor="middle" font-family="Nunito Sans" font-weight="700" font-size="3.4" fill="#000"></text>')
    return svg(w, h, "".join(p))

def read_line_graph(s):
    """independent reader: {category: value}, the values read from the point heights against the labelled ticks"""
    yl = [(float(y), float(v)) for y, v in re.findall(r'class="yl" x="[\d.]+" y="([\d.]+)"[^>]*>(\d+)<', s)]
    (y0, v0), (y1, v1) = yl[0], yl[-1]
    cats = [(float(x), t) for x, t in re.findall(r'class="xl" x="([\d.]+)" y="[\d.]+"[^>]*>(.*?)<', s)]
    out = {}
    for cx, cy in re.findall(r'class="pt" cx="([\d.]+)" cy="([\d.]+)"', s):
        val = v0 + (float(cy) - y0) * (v1 - v0) / (y1 - y0)
        name = min(cats, key=lambda c: abs(c[0] - float(cx)))[1]
        out[name] = round(val)
    return out

def pie_svg(sectors, wedges=8, r=36.0, size=92.0):
    """a pie chart of `wedges` equal slices (thin spokes), the sectors drawn with thick edges and named; sectors = [(name, number of slices)], from the top, clockwise"""
    cx = cy = size / 2
    p = []; a0 = -90.0
    for name, k in sectors:
        a1 = a0 + 360.0 * k / wedges
        x0, y0 = cx + r * math.cos(math.radians(a0)), cy + r * math.sin(math.radians(a0)); x1, y1 = cx + r * math.cos(math.radians(a1)), cy + r * math.sin(math.radians(a1))
        large = 1 if (a1 - a0) > 180 else 0
        p.append(f'<path class="sector" d="M{cx:.2f},{cy:.2f} L{x0:.2f},{y0:.2f} A{r},{r} 0 {large} 1 {x1:.2f},{y1:.2f} Z" fill="#fff" stroke="#000" stroke-width="0.9" stroke-linejoin="round"/>')
        am = math.radians(a0 + 180.0 / wedges if k % 2 == 0 else (a0 + a1) / 2); rr = r * (0.62 if k > 1 else 0.7)
        p.append(f'<text class="sn" x="{cx + rr * math.cos(am):.2f}" y="{cy + rr * math.sin(am):.2f}" text-anchor="middle" dominant-baseline="central" font-family="Nunito Sans" font-weight="800" font-size="3.7" fill="#000">{name}</text>')
        a0 = a1
    for j in range(wedges):
        a = math.radians(-90.0 + 360.0 * j / wedges)
        p.append(f'<line class="spoke" x1="{cx:.2f}" y1="{cy:.2f}" x2="{cx + r * math.cos(a):.2f}" y2="{cy + r * math.sin(a):.2f}" stroke="#000" stroke-width="0.3" stroke-dasharray="0.9 1.1"/>')
    return svg(size, size, "".join(p))

def read_pie(s):
    """independent reader: [(name, angle of the sector in degrees)] from the sector paths"""
    out = []
    secs = re.findall(r'class="sector" d="M([\d.]+),([\d.]+) L([\d.]+),([\d.]+) A[\d.]+,[\d.]+ 0 [01] 1 ([\d.]+),([\d.]+) Z"', s)
    names = re.findall(r'class="sn"[^>]*>(.*?)<', s)
    for (cx, cy, x0, y0, x1, y1), nm in zip(secs, names):
        a0 = math.degrees(math.atan2(float(y0) - float(cy), float(x0) - float(cx))); a1 = math.degrees(math.atan2(float(y1) - float(cy), float(x1) - float(cx)))
        out.append((nm, round((a1 - a0) % 360)))
    return out
