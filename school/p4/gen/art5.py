"""Primary 4 pictures: rectilinear figures with labelled sides (area and perimeter), square-grid figures for symmetry, solids and nets, line graphs, pie charts.
Pure black and white. Every picture has a reader function that recovers its values from the DRAWING only (used by the independent solvers).
Figures are drawn to scale (the scale is the same in both directions), but a pupil is never asked to measure them."""
import math, re
from fractions import Fraction
from shapely.geometry import Polygon, Point
from .common import svg

FS = 3.8                     # label font size in mm
LW = 0.6                     # outline width in mm
LOFF = 2.2                   # distance in mm from the middle of a side to its label's anchor point (the label sits on the outside of the side)

def _fmt(v):
    return str(v) if isinstance(v, int) else (str(int(v)) if float(v).is_integer() else str(v))

# ---------------------------------------------------------------- rectilinear figures
def shapes_verts(kind, **p):
    """vertices (cm, y downwards, clockwise from the top left) of a rectilinear figure"""
    if kind == "rect": W, H = p["W"], p["H"]; return [(0, 0), (W, 0), (W, H), (0, H)]
    if kind == "L":    W, H, a, b = p["W"], p["H"], p["a"], p["b"]; return [(0, 0), (W - a, 0), (W - a, b), (W, b), (W, H), (0, H)]
    if kind == "T":    W, H, t, x1, x2 = p["W"], p["H"], p["t"], p["x1"], p["x2"]; return [(0, 0), (W, 0), (W, t), (x2, t), (x2, H), (x1, H), (x1, t), (0, t)]
    if kind == "U":    W, H, a, b, x1 = p["W"], p["H"], p["a"], p["b"], p["x1"]; return [(0, 0), (x1, 0), (x1, b), (x1 + a, b), (x1 + a, 0), (W, 0), (W, H), (0, H)]
    if kind == "stair": W, H, w1, h1, w2, h2 = p["W"], p["H"], p["w1"], p["h1"], p["w2"], p["h2"]; return [(0, 0), (w1, 0), (w1, h1), (w2, h1), (w2, h2), (W, h2), (W, H), (0, H)]
    raise ValueError(kind)

def poly_area(v): return abs(sum(v[i][0] * v[(i + 1) % len(v)][1] - v[(i + 1) % len(v)][0] * v[i][1] for i in range(len(v)))) / 2
def poly_perim(v): return sum(math.dist(v[i], v[(i + 1) % len(v)]) for i in range(len(v)))
def side_len(v, i): return math.dist(v[i], v[(i + 1) % len(v)])

def _outward(pts, i, poly):
    n = len(pts); (x1, y1), (x2, y2) = pts[i], pts[(i + 1) % n]
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2; dx, dy = x2 - x1, y2 - y1; L = math.hypot(dx, dy)
    nx, ny = dy / L, -dx / L
    if poly.contains(Point(mx + nx * 0.2, my + ny * 0.2)): nx, ny = -nx, -ny
    return mx, my, nx, ny

def label_place(pts, i, txt, fs, poly):
    """anchor point, anchor kind, baseline and the bounding box (minx, miny, maxx, maxy) of the label of side i"""
    mx, my, nx, ny = _outward(pts, i, poly)
    ax, ay = mx + nx * LOFF, my + ny * LOFF
    tw = 0.58 * fs * len(txt)
    if abs(nx) > 0.5:
        anchor, base = ("start" if nx > 0 else "end"), "central"
        box = (ax, ay - fs / 2, ax + tw, ay + fs / 2) if nx > 0 else (ax - tw, ay - fs / 2, ax, ay + fs / 2)
    else:
        anchor = "middle"
        if ny < 0: base = "alphabetic"; box = (ax - tw / 2, ay - fs * 0.95, ax + tw / 2, ay)
        else: base = "hanging"; box = (ax - tw / 2, ay, ax + tw / 2, ay + fs * 0.95)
    return ax, ay, anchor, base, box

def labels_clear(verts, unit, labels, fs=FS, gap=0.8):
    """True when no two labels overlap and no label crosses the figure"""
    pts = [(x * unit, y * unit) for x, y in verts]; poly = Polygon(pts); boxes = []
    for i, t in labels.items():
        b = label_place(pts, i, t, fs, poly)[4]
        from shapely.geometry import box as _box
        bb = _box(b[0] - gap / 2, b[1] - gap / 2, b[2] + gap / 2, b[3] + gap / 2)
        if poly.intersection(bb).area > 0.02: return False
        if any(bb.intersects(o) for o in boxes): return False
        boxes.append(bb)
    return True

def poly_svg(verts, unit, labels=None, inner=None, shade=False, fs=FS, cls="fig", margin=0.8):
    """verts in cm, drawn at `unit` mm per cm. labels: {side index: text} (the side from vertex i to vertex i+1); a label sits outside the side, its anchor
    point LOFF mm from the middle of the side. inner: [(text, dy)] lines of text centred in the figure. The picture is as large as the figure and its labels."""
    pts0 = [(x * unit, y * unit) for x, y in verts]; poly0 = Polygon(pts0)
    minx = min(x for x, y in pts0); miny = min(y for x, y in pts0); maxx = max(x for x, y in pts0); maxy = max(y for x, y in pts0)
    placed = {}
    for i, txt in (labels or {}).items():
        placed[i] = label_place(pts0, i, txt, fs, poly0) + (txt,)
        b = placed[i][4]; minx, miny, maxx, maxy = min(minx, b[0]), min(miny, b[1]), max(maxx, b[2]), max(maxy, b[3])
    sx, sy = margin - minx, margin - miny
    W, H = maxx - minx + 2 * margin, maxy - miny + 2 * margin
    pts = [(x + sx, y + sy) for x, y in pts0]
    p = [f'<polygon class="shape" points="{" ".join(f"{x:.2f},{y:.2f}" for x, y in pts)}" fill="#fff" stroke="#000" stroke-width="{LW}" stroke-linejoin="miter"/>']
    for i, (ax, ay, anchor, base, box, txt) in placed.items():
        p.append(f'<text class="dim" x="{ax + sx:.2f}" y="{ay + sy:.2f}" text-anchor="{anchor}" dominant-baseline="{base}" font-family="Nunito Sans" font-weight="800" font-size="{fs}" fill="#000">{txt}</text>')
    cx = (min(x for x, y in pts) + max(x for x, y in pts)) / 2
    cy = (min(y for x, y in pts) + max(y for x, y in pts)) / 2
    for txt, dy in (inner or []):
        p.append(f'<text class="inner" x="{cx:.2f}" y="{cy + dy:.2f}" text-anchor="middle" dominant-baseline="central" font-family="Nunito Sans" font-weight="700" font-size="{fs}" fill="#000">{txt}</text>')
    return svg(round(W, 1), round(H, 1), "".join(p), cls=cls)

def read_poly(s):
    """independent reader: (vertices in mm, [(label text, x, y)], [(inner text, x, y)])"""
    m = re.search(r'class="shape" points="([^"]+)"', s)
    pts = [tuple(map(float, q.split(","))) for q in m.group(1).split()]
    dims = [(t, float(x), float(y)) for x, y, t in re.findall(r'class="dim" x="([\d.\-]+)" y="([\d.\-]+)"[^>]*>(.*?)</text>', s)]
    inner = [(t, float(x), float(y)) for x, y, t in re.findall(r'class="inner" x="([\d.\-]+)" y="([\d.\-]+)"[^>]*>(.*?)</text>', s)]
    return pts, dims, inner

def side_labels(pts, dims):
    """which side each printed label belongs to: the label's anchor point lies LOFF mm outside the middle of its side"""
    out = {}
    n = len(pts); poly = Polygon(pts)
    cand = []
    for i in range(n):
        (x1, y1), (x2, y2) = pts[i], pts[(i + 1) % n]
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2; dx, dy = x2 - x1, y2 - y1; L = math.hypot(dx, dy)
        nx, ny = dy / L, -dx / L
        if poly.contains(Point(mx + nx * 0.2, my + ny * 0.2)): nx, ny = -nx, -ny
        cand.append((mx + nx * LOFF, my + ny * LOFF))
    for t, x, y in dims:
        k = min(range(n), key=lambda i: (cand[i][0] - x) ** 2 + (cand[i][1] - y) ** 2)
        assert (cand[k][0] - x) ** 2 + (cand[k][1] - y) ** 2 < 0.05, (t, x, y, cand[k])
        out[k] = t
    return out

def figure_lengths(pts, labels):
    """each side's length in cm, from the drawing and the printed labels: the scale (mm per cm) comes from the labelled sides, every other side is measured on the drawing"""
    n = len(pts); known = {}
    for k, t in labels.items():
        mm = re.fullmatch(r"(\d+(?:\.\d+)?) cm", t)
        if mm: known[k] = (math.dist(pts[k], pts[(k + 1) % n]), Fraction(mm.group(1)))
    scales = [d / float(v) for d, v in known.values()]
    assert max(scales) - min(scales) < 0.05, scales
    sc = sum(scales) / len(scales)
    return [Fraction(round(math.dist(pts[i], pts[(i + 1) % n]) / sc, 6)).limit_denominator(100) for i in range(n)]

def rectilinear_questions(verts, labels_known):
    """labels for all sides except one horizontal and one vertical side (the pupil finds those two)"""
    n = len(verts); hs = [i for i in range(n) if verts[i][1] == verts[(i + 1) % n][1]]; vs = [i for i in range(n) if verts[i][0] == verts[(i + 1) % n][0]]
    return hs, vs

def side_text(v, i):
    return f"{_fmt(side_len(v, i))} cm"
