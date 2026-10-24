"""Largest label rectangles inside a region. For each height h a (cx, cy, w, h) box is found that lies inside the region
shrunk by MARGIN (outline half-width plus clearance) and away from decorations. Results are cached on disk."""
import json, hashlib, os
import numpy as np
from shapely import prepare, contains
from shapely.geometry import box

MARGIN = 1.0                       # mm between a label and any outline (outline is 0.9 mm wide, so 0.55 mm of white)
HEIGHTS = (10.5, 12, 14, 16, 18, 21, 25, 30)
CACHE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cache", "boxes.json")
_cache = None

def _load():
    global _cache
    if _cache is None:
        try: _cache = json.load(open(CACHE))
        except Exception: _cache = {}
    return _cache

def _save():
    os.makedirs(os.path.dirname(CACHE), exist_ok=True)
    json.dump(_cache, open(CACHE, "w"))

def find_boxes(geom, obstacles=(), step=1.0):
    key = hashlib.sha1((geom.wkt + "|" + "|".join(o.wkt for o in obstacles) + f"|{MARGIN}|{HEIGHTS}|{step}").encode()).hexdigest()
    c = _load()
    if key in c: return [tuple(b) for b in c[key]]
    g = geom.buffer(-MARGIN)
    for o in obstacles: g = g.difference(o.buffer(MARGIN))
    if g.is_empty: return []
    prepare(g)
    minx, miny, maxx, maxy = g.bounds
    xs, ys = np.meshgrid(np.arange(minx + step / 2, maxx, step), np.arange(miny + step / 2, maxy, step))
    xs, ys = xs.ravel(), ys.ravel()
    from shapely import points
    inside = contains(g, points(xs, ys))
    xs, ys = xs[inside], ys[inside]
    cen = geom.centroid
    out = []
    for h in HEIGHTS:
        best = None
        for cx, cy in zip(xs, ys):
            if not g.contains(box(cx - 6, cy - h / 2, cx + 6, cy + h / 2)): continue       # need at least 12 mm wide
            lo, hi = 12.0, 80.0
            for _ in range(9):
                mid = (lo + hi) / 2
                if g.contains(box(cx - mid / 2, cy - h / 2, cx + mid / 2, cy + h / 2)): lo = mid
                else: hi = mid
            score = (round(min(lo, 46) / 1.5), -((cx - cen.x) ** 2 + (cy - cen.y) ** 2))
            if best is None or score > best[0]: best = (score, (round(float(cx), 2), round(float(cy), 2), round(lo - 0.05, 2), h))
        if best: out.append(best[1])
    c[key] = out; _save()
    return [tuple(b) for b in out]
