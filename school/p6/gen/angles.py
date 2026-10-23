"""Angle figures: every figure is built from coordinates, so the angle printed in each arc is the angle drawn. read_angle_figure() measures a printed figure
(vertex points and arcs read from the svg) and is the independent solver for the angle pages."""
import math, re, html
from fractions import Fraction as Fr

SW = 0.55
def rad(d): return d * math.pi / 180
def deg(r): return r * 180 / math.pi

def _unit(p, q):
    dx, dy = q[0] - p[0], q[1] - p[1]; n = math.hypot(dx, dy); return dx / n, dy / n

class Fig:
    def __init__(self):
        self.pts = {}; self.segs = []; self.ticks = []; self.arcs = []; self.rights = []; self.chev = []; self.letters = True
    def P(self, name, x, y): self.pts[name] = (x, y)
    def seg(self, a, b): self.segs.append((a, b))
    def tick(self, a, b, n=1): self.ticks.append((a, b, n))
    def arc(self, at, p, q, label, unk=False): self.arcs.append(dict(at=at, p=p, q=q, label=label, unk=unk))
    def right(self, at, p, q): self.rights.append((at, p, q))
    def parallel(self, a, b, n=1): self.chev.append((a, b, n))

def render(fig, W=50.0, H=36.0, mirror=False):
    pts = {k: ((-x if mirror else x), y) for k, (x, y) in fig.pts.items()}
    mx, my = 6.5, 5.5
    def fit(pp):
        xs = [p[0] for p in pp.values()]; ys = [p[1] for p in pp.values()]
        bw, bh = max(xs) - min(xs), max(ys) - min(ys)
        return min((W - 2 * mx) / bw, (H - 2 * my) / bh)
    rot = {k: (y, -x) for k, (x, y) in pts.items()}
    if fit(rot) > 1.25 * fit(pts): pts = rot              # a tall figure is turned on its side so that it can be drawn larger
    xs = [p[0] for p in pts.values()]; ys = [p[1] for p in pts.values()]
    bw, bh = max(xs) - min(xs), max(ys) - min(ys)
    k = min((W - 2 * mx) / bw, (H - 2 * my) / bh)
    ox = mx + (W - 2 * mx - bw * k) / 2; oy = my + (H - 2 * my - bh * k) / 2
    S = {n: (ox + (x - min(xs)) * k, H - (oy + (y - min(ys)) * k)) for n, (x, y) in pts.items()}
    cx = sum(p[0] for p in S.values()) / len(S); cy = sum(p[1] for p in S.values()) / len(S)
    out = []
    for a, b in fig.segs:
        out.append(f'<line x1="{S[a][0]:.2f}" y1="{S[a][1]:.2f}" x2="{S[b][0]:.2f}" y2="{S[b][1]:.2f}" stroke="#000" stroke-width="{SW}" stroke-linecap="round"/>')
    for a, b, n in fig.ticks:
        mxp, myp = (S[a][0] + S[b][0]) / 2, (S[a][1] + S[b][1]) / 2; ux, uy = _unit(S[a], S[b]); nx, ny = -uy, ux
        for i in range(n):
            off = (i - (n - 1) / 2) * 1.3
            px, py = mxp + ux * off, myp + uy * off
            out.append(f'<line x1="{px - nx * 1.5:.2f}" y1="{py - ny * 1.5:.2f}" x2="{px + nx * 1.5:.2f}" y2="{py + ny * 1.5:.2f}" stroke="#000" stroke-width="0.5"/>')
    for a, b, n in fig.chev:
        mxp, myp = (S[a][0] + S[b][0]) / 2, (S[a][1] + S[b][1]) / 2; ux, uy = _unit(S[a], S[b]); nx, ny = -uy, ux
        for i in range(n):
            off = (i - (n - 1) / 2) * 1.6
            px, py = mxp + ux * off, myp + uy * off
            out.append(f'<polyline points="{px - ux * 1.2 + nx * 1.4:.2f},{py - uy * 1.2 + ny * 1.4:.2f} {px + ux * 0.8:.2f},{py + uy * 0.8:.2f} {px - ux * 1.2 - nx * 1.4:.2f},{py - uy * 1.2 - ny * 1.4:.2f}" fill="none" stroke="#000" stroke-width="0.5"/>')
    for at, p, q in fig.rights:
        v = S[at]; u1 = _unit(v, S[p]); u2 = _unit(v, S[q]); d = 2.6
        out.append(f'<polyline points="{v[0] + u1[0] * d:.2f},{v[1] + u1[1] * d:.2f} {v[0] + (u1[0] + u2[0]) * d:.2f},{v[1] + (u1[1] + u2[1]) * d:.2f} {v[0] + u2[0] * d:.2f},{v[1] + u2[1] * d:.2f}" fill="none" stroke="#000" stroke-width="0.5"/>')
    for a in fig.arcs:
        v = S[a["at"]]; p = S[a["p"]]; q = S[a["q"]]
        a1 = math.atan2(p[1] - v[1], p[0] - v[0]); a2 = math.atan2(q[1] - v[1], q[0] - v[0])
        delta = (a2 - a1 + math.pi) % (2 * math.pi) - math.pi
        r = 5.2 if not a["unk"] else 6.2
        x1, y1 = v[0] + r * math.cos(a1), v[1] + r * math.sin(a1); x2, y2 = v[0] + r * math.cos(a1 + delta), v[1] + r * math.sin(a1 + delta)
        sweep = 1 if delta > 0 else 0
        bis = a1 + delta / 2; lr = r + 3.6
        lx, ly = v[0] + lr * math.cos(bis), v[1] + lr * math.sin(bis)
        cls = "unk" if a["unk"] else "ang"
        out.append(f'<path class="{cls}" data-at="{a["at"]}" data-p="{a["p"]}" data-q="{a["q"]}" data-val="{html.escape(str(a["label"]))}" d="M{x1:.2f},{y1:.2f} A{r},{r} 0 0 {sweep} {x2:.2f},{y2:.2f}" fill="none" stroke="#000" stroke-width="{0.6 if not a["unk"] else 0.8}"/>')
        out.append(f'<text class="al" x="{lx:.2f}" y="{ly:.2f}" text-anchor="middle" dominant-baseline="central" font-family="Nunito Sans" font-weight="800" font-size="3.8" fill="#000" stroke="#fff" stroke-width="1.1" paint-order="stroke" stroke-linejoin="round">{html.escape(str(a["label"]))}</text>')
    for n, (x, y) in S.items():
        out.append(f'<circle class="pt" data-v="{n}" cx="{x:.3f}" cy="{y:.3f}" r="0.5" fill="#000"/>')
        dx, dy = x - cx, y - cy; nn = math.hypot(dx, dy) or 1
        lx, ly = x + dx / nn * 3.4, y + dy / nn * 3.4
        out.append(f'<text class="vl" x="{lx:.2f}" y="{ly:.2f}" text-anchor="middle" dominant-baseline="central" font-family="Nunito Sans" font-weight="800" font-size="3.9" fill="#000" stroke="#fff" stroke-width="1.1" paint-order="stroke" stroke-linejoin="round">{n}</text>')
    return f'<svg xmlns="http://www.w3.org/2000/svg" class="fig-svg fig-ang" viewBox="0 0 {W:.1f} {H:.1f}" width="{W:.1f}mm" height="{H:.1f}mm">' + "".join(out) + "</svg>"

# ------------------------------------------------------------------------------------------------ the families
def iso_line(alpha, unknown="exterior"):
    """AB = AC, apex angle alpha at A; BCD is a straight line. exterior: given alpha, find ACD. apex: given ACD (= 90 + alpha/2), find BAC"""
    beta = (180 - alpha) / 2; c = 10.0
    f = Fig(); f.P("B", 0, 0); f.P("C", c, 0); f.P("A", c / 2, c / 2 * math.tan(rad(beta))); f.P("D", c + 5, 0)
    f.seg("B", "C"); f.seg("C", "D"); f.seg("A", "B"); f.seg("A", "C"); f.tick("A", "B"); f.tick("A", "C")
    ext = 180 - beta
    if unknown == "exterior":
        f.arc("A", "B", "C", f"{alpha}°"); f.arc("C", "A", "D", "?", unk=True); return f, "ABC is an isosceles triangle with AB = AC. BCD is a straight line. Find angle ACD.", ext
    f.arc("C", "A", "D", f"{int(ext)}°"); f.arc("A", "B", "C", "?", unk=True); return f, "ABC is an isosceles triangle with AB = AC. BCD is a straight line. Find angle BAC.", alpha

def rhombus_diag(gamma):
    """rhombus ABCD, angle DAB = gamma, diagonal BD; find angle ABD"""
    s = 10.0; f = Fig(); f.P("A", 0, 0); f.P("B", s, 0); f.P("D", s * math.cos(rad(gamma)), s * math.sin(rad(gamma))); f.P("C", s + s * math.cos(rad(gamma)), s * math.sin(rad(gamma)))
    for a, b in (("A", "B"), ("B", "C"), ("C", "D"), ("D", "A"), ("B", "D")): f.seg(a, b)
    for a, b in (("A", "B"), ("B", "C"), ("C", "D"), ("D", "A")): f.tick(a, b)
    f.arc("A", "B", "D", f"{gamma}°"); f.arc("B", "A", "D", "?", unk=True)
    return f, "ABCD is a rhombus. Find angle ABD.", (180 - gamma) // 2

def rhombus_opp(beta):
    """rhombus ABCD, angle ABC = beta, diagonal AC; find angle DAC"""
    s = 10.0; f = Fig(); f.P("B", 0, 0); f.P("A", s, 0); f.P("C", s * math.cos(rad(beta)), s * math.sin(rad(beta))); f.P("D", s + s * math.cos(rad(beta)), s * math.sin(rad(beta)))
    for a, b in (("A", "B"), ("B", "C"), ("C", "D"), ("D", "A"), ("A", "C")): f.seg(a, b)
    for a, b in (("A", "B"), ("B", "C"), ("C", "D"), ("D", "A")): f.tick(a, b)
    f.arc("B", "A", "C", f"{beta}°"); f.arc("A", "D", "C", "?", unk=True)
    return f, "ABCD is a rhombus. Find angle DAC.", 90 - beta // 2

def sq_tri(outside=True):
    s = 10.0; f = Fig(); f.P("A", 0, 0); f.P("B", s, 0); f.P("C", s, s); f.P("D", 0, s)
    h = s * math.sqrt(3) / 2
    f.P("E", s / 2, s + h if outside else s - h)
    for a, b in (("A", "B"), ("B", "C"), ("C", "D"), ("D", "A"), ("D", "E"), ("C", "E"), ("A", "E")): f.seg(a, b)
    f.right("A", "B", "D"); f.right("B", "A", "C")
    f.tick("D", "E"); f.tick("C", "E"); f.tick("C", "D")
    f.arc("E", "D", "A", "?", unk=True)
    if outside: return f, "ABCD is a square. CDE is an equilateral triangle. Find angle DEA.", 15
    return f, "ABCD is a square. CDE is an equilateral triangle inside the square. Find angle DEA.", 75

def para_iso(d):
    """parallelogram ABCD with angle ADC = d; E is on BC with BE = BA; find angle BAE"""
    a = 180 - d; w = 10.0; p = 12.5; f = Fig()
    f.P("A", 0, 0); f.P("B", w, 0); f.P("D", p * math.cos(rad(a)), p * math.sin(rad(a))); f.P("C", w + p * math.cos(rad(a)), p * math.sin(rad(a)))
    f.P("E", w + w * math.cos(rad(a)), w * math.sin(rad(a)))
    for x, y in (("A", "B"), ("B", "C"), ("C", "D"), ("D", "A"), ("A", "E")): f.seg(x, y)
    f.tick("B", "A"); f.tick("B", "E")
    f.arc("D", "A", "C", f"{d}°"); f.arc("A", "B", "E", "?", unk=True)
    return f, "ABCD is a parallelogram. E is a point on BC. BA = BE. Find angle BAE.", (180 - d) // 2

def trapezium(b):
    """trapezium ABCD, AB parallel to DC, angle ABC = b; find angle BCD"""
    h = 7.0; xb = 7.0; f = Fig(); f.P("A", 1.5, h); f.P("B", xb, h)
    L = h / math.sin(rad(b)); cxx = xb + L * math.cos(rad(180 + b)); f.P("C", cxx, 0); f.P("D", -1.0, 0)
    for x, y in (("A", "B"), ("B", "C"), ("C", "D"), ("D", "A")): f.seg(x, y)
    f.parallel("A", "B"); f.parallel("D", "C")
    f.arc("B", "A", "C", f"{b}°"); f.arc("C", "B", "D", "?", unk=True)
    return f, "ABCD is a trapezium. AB is parallel to DC. Find angle BCD.", 180 - b

def tri_ext(p, q):
    """triangle ABC with angle BAC = p and angle ABC = q; BCD is a straight line; find angle ACD (= p + q)"""
    c = 12.0; f = Fig(); f.P("B", 0, 0); f.P("C", c, 0)
    # A = B + t(cos q, sin q) = C + s(cos(p+q), sin(p+q))
    t = c * math.sin(rad(p + q)) / math.sin(rad(p)) if False else c * math.sin(rad(180 - p - q)) / math.sin(rad(p))
    f.P("A", t * math.cos(rad(q)), t * math.sin(rad(q))); f.P("D", c + 5, 0)
    for x, y in (("B", "C"), ("C", "D"), ("A", "B"), ("A", "C")): f.seg(x, y)
    f.arc("A", "B", "C", f"{p}°"); f.arc("B", "A", "C", f"{q}°"); f.arc("C", "A", "D", "?", unk=True)
    return f, "BCD is a straight line. Find angle ACD.", p + q

# ------------------------------------------------------------------------------------------------ reader (independent solver)
def read_angle_figure(svg_html, caption_text):
    """measure the angle named in the caption ('Find angle ACD') from the printed figure's vertex points; also check every given arc against its printed degrees"""
    pts = {m.group(1): (float(m.group(2)), float(m.group(3))) for m in re.finditer(r'<circle class="pt" data-v="(\w)" cx="([\d.]+)" cy="([\d.]+)"', svg_html)}
    def ang(at, p, q):
        v = pts[at]; a1 = math.atan2(pts[p][1] - v[1], pts[p][0] - v[0]); a2 = math.atan2(pts[q][1] - v[1], pts[q][0] - v[0])
        d = abs(deg(a2 - a1)) % 360; return 360 - d if d > 180 else d
    m = re.search(r"Find angle ([A-Z])([A-Z])([A-Z])", caption_text)
    X, Y, Z = m.groups(); measured = ang(Y, X, Z)
    bad = []
    for am in re.finditer(r'<path class="ang" data-at="(\w)" data-p="(\w)" data-q="(\w)" data-val="(\d+)°"', svg_html):
        at, p, q, val = am.groups()
        if abs(ang(at, p, q) - int(val)) > 0.6: bad.append((at, p, q, val, round(ang(at, p, q), 2)))
    um = re.search(r'<path class="unk" data-at="(\w)" data-p="(\w)" data-q="(\w)"', svg_html)
    unk_ok = um is not None and um.group(1) == Y and {um.group(2), um.group(3)} == {X, Z}
    return measured, bad, unk_ok
