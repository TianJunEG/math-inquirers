"""Geometry helpers (shapely) for the picture library. All units are mm on a 180 x 200 canvas."""
import math
from shapely import affinity
from shapely.geometry import Point, Polygon, box, MultiPolygon
from shapely.ops import unary_union

W, H = 180.0, 200.0
AXIS = 90.0                      # mirror axis of symmetric pictures

def C(cx, cy, r):
    return Point(cx, cy).buffer(r, quad_segs=32)

def E(cx, cy, rx, ry, rot=0):
    g = affinity.scale(Point(cx, cy).buffer(1, quad_segs=32), rx, ry)
    return affinity.rotate(g, rot, origin=(cx, cy)) if rot else g

def P(*pts):
    return Polygon(pts)

def R(x0, y0, x1, y1):
    return box(x0, y0, x1, y1)

def mir(g, ax=AXIS):
    return affinity.scale(g, xfact=-1, yfact=1, origin=(ax, 0))

def smooth(pts, n=14, tension=0.5):
    """Closed Catmull-Rom spline through pts -> Polygon."""
    out = []
    m = len(pts)
    for i in range(m):
        p0, p1, p2, p3 = pts[(i - 1) % m], pts[i], pts[(i + 1) % m], pts[(i + 2) % m]
        for k in range(n):
            t = k / n
            t2, t3 = t * t, t * t * t
            x = 0.5 * ((2 * p1[0]) + (-p0[0] + p2[0]) * t + (2 * p0[0] - 5 * p1[0] + 4 * p2[0] - p3[0]) * t2 + (-p0[0] + 3 * p1[0] - 3 * p2[0] + p3[0]) * t3)
            y = 0.5 * ((2 * p1[1]) + (-p0[1] + p2[1]) * t + (2 * p0[1] - 5 * p1[1] + 4 * p2[1] - p3[1]) * t2 + (-p0[1] + 3 * p1[1] - 3 * p2[1] + p3[1]) * t3)
            out.append((x, y))
    return Polygon(out)

def clean(g, min_area=1.0):
    """Keep the largest polygon of a (multi)geometry; drop slivers."""
    if g.is_empty: return g
    if isinstance(g, MultiPolygon) or g.geom_type == "GeometryCollection":
        parts = [p for p in g.geoms if p.geom_type == "Polygon" and p.area >= min_area]
        g = max(parts, key=lambda p: p.area) if parts else Polygon()
    return g

def path_d(g):
    """SVG path data for a polygon (with holes, fill-rule evenodd)."""
    def ring(c):
        pts = list(c.coords)[:-1]
        return "M" + " L".join(f"{x:.2f},{y:.2f}" for x, y in pts) + " Z"
    d = ring(g.exterior)
    for h in g.interiors: d += " " + ring(h)
    return d
