"""Semester 2, part B (area of triangles, volume): P5-28 Height Hunt; P5-29 Triangle Areas; P5-30 Triangle Route; P5-31 Composite Figures;
P5-32 Count the Cubes; P5-33 Cuboid Volumes; P5-34 Tank Match; P5-35 Tank Tales."""
import random, re, math, itertools
from fractions import Fraction as Fr
from .common import *
from .kit import *
from .kit5 import *
from .art5 import *

SQ = "²"; CU = "³"; LIT = "ℓ"

# =============================================================================== P5-28 Height Hunt (lettered choices)
def hunt_fig(rng, names, w=64, hh=30):
    """returns (svg, base name, height segment name, slanted segment name, side name): triangle XYZ with base XY, the dashed height ZD and a dashed slanted line ZE"""
    X, Y, Z, D, E = names
    for _ in range(2000):
        Lb = 38.0; H = rng.uniform(20, 26)
        f = rng.choice([rng.uniform(0.3, 0.7), rng.uniform(0.3, 0.7), rng.uniform(0.3, 0.7), rng.uniform(-0.3, -0.18), rng.uniform(1.18, 1.3)])
        e = f + rng.choice([-1, 1]) * rng.uniform(0.3, 0.5)
        if not -0.1 <= e <= 1.1 or min(abs(e), abs(e - 1)) < 0.12: continue
        pts = {X: (0, 0), Y: (Lb, 0), Z: (f * Lb, -H), D: (f * Lb, 0), E: (e * Lb, 0)}
        th = math.radians(rng.choice([0, 0, 25, -25, 40, -40]))
        c, s = math.cos(th), math.sin(th)
        rot = {k: (x * c - y * s, x * s + y * c) for k, (x, y) in pts.items()}
        xs = [p[0] for p in rot.values()]; ys = [p[1] for p in rot.values()]
        sc = min((w - 14) / (max(xs) - min(xs)), (hh - 9) / (max(ys) - min(ys)), 1.3)
        P = {k: (7 + (x - min(xs)) * sc, 4.5 + (y - min(ys)) * sc) for k, (x, y) in rot.items()}
        ks = list(P)
        if min(math.hypot(P[a][0] - P[b][0], P[a][1] - P[b][1]) for i, a in enumerate(ks) for b in ks[i + 1:]) < 8.0: continue
        break
    else: raise RuntimeError("hunt")
    o = []
    lo = min((X, Y, D, E), key=lambda k: (P[k][0] - P[X][0]) * (P[Y][0] - P[X][0]) + (P[k][1] - P[X][1]) * (P[Y][1] - P[X][1]))
    hi = max((X, Y, D, E), key=lambda k: (P[k][0] - P[X][0]) * (P[Y][0] - P[X][0]) + (P[k][1] - P[X][1]) * (P[Y][1] - P[X][1]))
    if lo != X: o.append(LN(*P[lo], *P[X], dash="1.2 1.2"))
    if hi != Y: o.append(LN(*P[Y], *P[hi], dash="1.2 1.2"))
    for a, b in ((X, Y), (X, Z), (Y, Z)): o.append(LN(*P[a], *P[b], attrs=f'data-seg="{a}{b}"'))
    o.append(LN(*P[Z], *P[D], dash="2 1.4", attrs=f'data-seg="{Z}{D}"'))
    o.append(LN(*P[Z], *P[E], dash="2 1.4", attrs=f'data-seg="{Z}{E}"'))
    cx = sum(p[0] for p in P.values()) / 5; cy = sum(p[1] for p in P.values()) / 5
    for k, (x, y) in P.items():
        dx, dy = x - cx, y - cy; l = math.hypot(dx, dy) or 1
        up = 3.4 if k != Z else 3.4
        o.append(T(x + dx / l * up, y + dy / l * up, k, size=3.8, attrs=f'data-pt="{k}"'))
    return svg(w, hh, "".join(o), cls="fsvg", extra='data-fig="hunt"'), f"{X}{Y}", f"{Z}{D}", f"{Z}{E}", rng.choice([f"{X}{Z}", f"{Y}{Z}"])

def read_segs(h):
    return {m.group(5): tuple(float(m.group(i)) for i in (1, 2, 3, 4)) for m in re.finditer(r'<line x1="([\d.-]+)" y1="([\d.-]+)" x2="([\d.-]+)" y2="([\d.-]+)"[^>]*?data-seg="(\w\w)"', h)}

def page28():
    rng = random.Random(5128)
    LET = "ABCDEFGHJKLMNPQRSTUVW"
    for _ in range(400):
        word = word_candidates(28, 6)[0]
        rows = []; keys = []
        for i in range(6):
            nm = rng.sample(LET, 5)
            fig, base, hgt, slant, side = hunt_fig(rng, nm)
            opts = [hgt, slant, side]
            rows.append(dict(q=f'<span class="qs">{base} is the base. Which line is the height?</span>', fig=fig, opts=opts, right=0)); keys.append(f"{hgt} (base {base})")
        break
    def solve_row(q, opts, qh):
        base = re.match(r"(\w\w) is the base", q).group(1)
        segs = read_segs(qh)
        def vec(n):
            a = segs.get(n) or segs.get(n[::-1])
            if a is None:
                a2 = segs.get(n[::-1]); a = (a2[2], a2[3], a2[0], a2[1])
            return (a[2] - a[0], a[3] - a[1])
        bv = vec(base)
        perp = []
        for i, t in enumerate(opts):
            v = vec(t)
            cosang = abs(bv[0] * v[0] + bv[1] * v[1]) / (math.hypot(*bv) * math.hypot(*v))
            if cosang < 0.02: perp.append(i)
        return perp[0] if len(perp) == 1 else -1
    P = mc_page(28, 5128, "Height Hunt", 1, "Area of a triangle: the base and its height", STRAND_AR,
        "area of a triangle: base and height (the height is at a right angle to the base)", ["AR1.1"], "Lettered choices (figures)",
        ["The height is at a right angle to the base. Circle its letter.", "The figures are drawn to scale: check with a corner of paper.", "Write the six letters in the boxes."],
        rng, rows, 3, word, "; ".join(f"{i+1}) {k}" for i, k in enumerate(keys)),
        "Six triangles, each with a named base. One dashed line from the opposite vertex meets the base line at a right angle (it is the height); a second dashed line and a side of the triangle do not. Some bases are tilted and some heights fall outside the triangle (the base is extended with a dotted line). The page says the figures are drawn to scale, so a pupil can check a right angle with the corner of a sheet of paper or a set square. This is the only page of the two booklets that relies on the drawing. The wrong choices are the slanted line and a side. Each choice has a letter and the right choices spell the word. Every other way of choosing was tested against a very large word list. A box left blank gives no letter and the check cannot see it.",
        solve_row, rows_cls="mcgrid", ps=False)
    return P

# =============================================================================== P5-29 Triangle Areas (code word)
def page29():
    rng = random.Random(5129)
    for _ in range(8000):
        items = []
        for k in range(6):
            b = rng.randint(6, 16); h = rng.randint(4, 11)
            if (b * h) % 2 or not 0.9 <= b / h <= 3.0: continue
            foot = rng.choice([0.3, 0.45, 0.6, 0.75, -0.2, 1.2, 0.001]) if k != 1 else 0.001
            side = rng.randint(max(b, h) + 1, max(b, h) + 6) if (rng.random() < .55 and b >= 8) else None
            items.append((b, h, foot, side))
        if len(items) < 6: continue
        ans = [Fr(b * h, 2) for b, h, _, _ in items]
        if not distinct(ans) or max(ans) > 99 or len({b for b, *_ in items}) < 5: continue
        pool = []
        for (b, h, f, s), a in zip(items, ans): pool += [Fr(b * h), Fr(b + h), a + b, a + h, Fr(s * b, 2) if s else Fr(b * h, 4) if (b * h) % 4 == 0 else Fr(b * h + 2)]
        pool = [p for p in dict.fromkeys(pool) if p not in ans and p.denominator == 1 and 0 < p <= 250]
        res = code_table_for(29, ans, rng, pool, n_decoy=2, tries=60)
        if res[0]: (word, table), dom = res; break
    else: raise RuntimeError("p29")
    cards = [qc(i + 1, f'<p class="qt">Area of the triangle</p>{tri_base_height(b, h, f, s, w=50, hh=40)}', abx("w4") + f'<span class="unit">cm{SQ}</span>') for i, (b, h, f, s) in enumerate(items)]
    solved = []
    for c in cards:
        b, h, s = read_tri(c); solved.append(Fr(b * h, 2))
    P = code_page(29, 5129, "Triangle Areas", 1, "Area of a triangle: base, height and area", STRAND_AR,
        "area of a triangle from its base and height", ["AR1.1", "AR1.2"], "Code-breaker (areas of triangles)",
        ["Find the area of each triangle.", "The height is the length at a right angle to the base. Write the area in the box.", "Use the code table."],
        cards, ans, word, table, dom, lambda k: num(int(k)), "; ".join(f"{i+1}) {int(a)} cm² (base {b}, height {h})" for i, (a, (b, h, f, s)) in enumerate(zip(ans, items))),
        "Six triangles with the base and the height (dashed, at a right angle to the base) labelled in cm; some figures have a length beside a slanted side that is not needed, and some have the height outside the triangle. The decoy letters stand for the usual slips: forgetting to halve, adding the base and the height, or using the slanted side instead of the height. A box left blank gives no letter and the check cannot see it. Figures are not drawn to scale (the page does not rely on the drawing).",
        solved, cols=4, layout="c3", checks=[("V7 every product base x height is even and every area is below 100 cm²", all((b * h) % 2 == 0 for b, h, _, _ in items) and max(ans) < 100, "")])
    return P

# =============================================================================== P5-30 Triangle Route (route)
def page30():
    rng = random.Random(5130)
    T = 30
    pairs = [(b, 2 * T // b) for b in range(4, 2 * T) if (2 * T) % b == 0 and 4 <= 2 * T // b <= 30 and b <= 30 and 0.4 <= b / (2 * T // b) <= 2.6]
    def cell(b, h):
        return tri_base_height(b, h, rng.choice([0.2, 0.4, 0.5, 0.6, 0.8, -0.2, 1.2]), None, w=40, hh=31)
    def make_on(i):
        b, h = rng.choice(pairs); return cell(b, h)
    def make_off():
        while True:
            prod = rng.choice([T, 4 * T, 2 * T + 6, 2 * T - 8, 3 * T, 2 * T + 12, T + 6, 2 * T - 4])
            ps = [(b, prod // b) for b in range(4, 31) if prod % b == 0 and 4 <= prod // b <= 30 and 0.4 <= b / (prod // b) <= 2.6]
            if ps:
                b, h = rng.choice(ps); return cell(b, h)
    n = 4; L = 8
    rule = lambda c: (lambda r: Fr(r[0] * r[1], 2) == T)(read_tri(c))
    for _ in range(50):
        try:
            path, grid, dead = build_route(rng, n, L, make_on, make_off, 3, ok_text=rule)
            break
        except RuntimeError: continue
    else: raise RuntimeError("p30")
    P = route_page(30, 5130, "Triangle Route", 2, "Area of a triangle: base, height and area", STRAND_AR,
        "area of a triangle from its base and height", ["AR1.2"], "Maze / path",
        ["Start at START. Move up, down, left or right.", f"Step only on triangles with area {T} cm{SQ}.", "Do not step on a box twice."],
        grid, path, dead, "", rule,
        f"A 4 by 4 grid of sixteen triangles, each with its base and its height (dashed) labelled in cm. The boxes on the route have area {T} cm{SQ}; some have a length beside a slanted side that is not needed. The boxes off the route have a product base x height that gives the area without halving, or an area a little more or less than {T} cm{SQ}; some extra boxes that do have area {T} cm{SQ} are dead ends. Counting the boxes shows a line that takes a shortcut. Figures are not drawn to scale (the page does not rely on the drawing).",
        lambda c: "{} x {} / 2 = {}".format(*read_tri(c)[:2], read_tri(c)[0] * read_tri(c)[1] // 2) if True else "", f"Does your line reach FINISH? Count its boxes: are there {L}? Does every triangle have area {T} cm{SQ}?", extra_facts=str(T), cls="maze tall tri")
    return P

# =============================================================================== P5-31 Composite Figures (code word)
def page31():
    rng = random.Random(5131)
    for _ in range(8000):
        kinds = ["house", "notch", "side", "house", "notch", "side"]; rng.shuffle(kinds)
        items = []
        for kd in kinds:
            if kd == "side": ln = rng.choice([4, 6, 8]); wd = rng.randint(3, 8); th = rng.randint(3, 6)
            else: wd = rng.choice([4, 6, 8, 10]); ln = rng.randint(3, 6); th = rng.randint(3, 6)
            items.append((kd, wd, ln, th))
        def area(kd, wd, ln, th):
            return {"house": wd * ln + Fr(wd * th, 2), "notch": wd * ln - Fr(wd * th, 2), "side": wd * ln + Fr(ln * th, 2)}[kd]
        ans = [Fr(area(*it)) for it in items]
        if not distinct(ans) or max(ans) > 250 or any(a.denominator != 1 for a in ans): continue
        if any(kd == "notch" and th >= ln for kd, wd, ln, th in items): continue
        pool = []
        for (kd, wd, ln, th), a in zip(items, ans): pool += [Fr(wd * ln), Fr(wd * ln + wd * th) if kd == "house" else Fr(wd * ln - wd * th) if kd == "notch" else Fr(wd * ln + ln * th), Fr(wd * th, 2), a + th, a - th if a > th else a + wd]
        pool = [p for p in dict.fromkeys(pool) if p not in ans and p.denominator == 1 and 0 < p <= 300]
        res = code_table_for(31, ans, rng, pool, n_decoy=2, tries=60)
        if res[0]: (word, table), dom = res; break
    else: raise RuntimeError("p31")
    cards = [qc(i + 1, f'<p class="qt">Area of the figure</p>{composite(kd, wd, ln, th, w=50, hh=44)}', abx("w4") + f'<span class="unit">cm{SQ}</span>') for i, (kd, wd, ln, th) in enumerate(items)]
    solved = []
    for c in cards:
        kd, wd, ln, th = read_composite(c)
        solved.append({"house": Fr(wd * ln) + Fr(wd * th, 2), "notch": Fr(wd * ln) - Fr(wd * th, 2), "side": Fr(wd * ln) + Fr(ln * th, 2)}[kd])
    P = code_page(31, 5131, "Composite Figures", 2, "Area of composite figures: rectangles and triangles", STRAND_AR,
        "area of composite figures made of rectangles and triangles", ["AR1.2", "AR1.3"], "Code-breaker (composite areas)",
        ["Find the area of each whole figure.", "Dashed lines are not edges. Write the area in the box.", "Use the code table."],
        cards, ans, word, table, dom, lambda k: num(int(k)), "; ".join(f"{i+1}) {int(a)} cm² ({kd})" for i, (a, (kd, wd, ln, th)) in enumerate(zip(ans, items))),
        "Six figures: a rectangle with a triangle on top (two figures), a rectangle with a triangular notch cut from its top edge (two figures) and a rectangle with a right-angled triangle joined to one side (two figures). The pupil finds the area of the rectangle and of the triangle and adds or subtracts. The decoy letters stand for the usual slips: forgetting to halve the triangle, or adding where the notch must be taken away. Dashed lines are not edges of the figure. Figures are not drawn to scale (the page does not rely on the drawing). A box left blank gives no letter and the check cannot see it.",
        solved, cols=4, layout="c3")
    return P

# =============================================================================== P5-32 Count the Cubes (code word)
def page32():
    rng = random.Random(5132)
    for _ in range(8000):
        dims = []
        for k in range(6):
            a, b = rng.randint(1, 4), rng.randint(1, 4)
            c = rng.randint(1, 3)
            if a + b < 3 or (a + b) * 4 + c * 8 > 40: break
            dims.append((a, b, c))
        else:
            ans = [Fr(a * b * c) for a, b, c in dims]
            if not distinct(ans) or len({tuple(sorted(d)) for d in dims}) < 6 or any(a < 6 for a in ans[:0]): continue
            pool = []
            for (a, b, c), v in zip(dims, ans): pool += [Fr(a * b + a * c + b * c), Fr(a + b + c), Fr(a * b + b * c), Fr(a * c + b * c), v + a, v - a if v > a else v + b]
            pool = [p for p in dict.fromkeys(pool) if p not in ans and p > 0]
            res = code_table_for(32, ans, rng, pool, n_decoy=2, tries=60)
            if res[0]: (word, table), dom = res; break
    else: raise RuntimeError("p32")
    cards = [qc(i + 1, f'{iso_units(a, b, c, u=8.0)}', abx("w3") + '<span class="unit">cubes</span>') for i, (a, b, c) in enumerate(dims)]
    solved = []
    for cc in cards:
        v, f = read_units(cc); solved.append(Fr(v))
    P = code_page(32, 5132, "Count the Cubes", 1, "Volume: building cuboids with unit cubes", STRAND_AR,
        "building cubes and cuboids with unit cubes; reading drawings of cuboids on an isometric grid; volume of a cuboid", ["VO2.1", "VO2.3", "VO2.4"], "Code-breaker (cubes in a cuboid)",
        ["Each cuboid is made of unit cubes with none missing inside.", "How many unit cubes make each cuboid? Write the number in the box.", "Use the code table."],
        cards, ans, word, table, dom, lambda k: num(int(k)), "; ".join(f"{i+1}) {a} x {b} x {c} = {int(v)}" for i, ((a, b, c), v) in enumerate(zip(dims, ans))),
        "Six cuboids built of unit cubes, drawn from above in isometric view with every unit face visible on the top and two sides. The pupil counts the cubes in one layer and the layers, or multiplies the three edges. The decoy letters stand for the usual slips: counting only the faces that can be seen, adding the three edges, or leaving a layer out. Drawing a cuboid on an isometric grid cannot be checked on a printed page: this page practises reading such a drawing. A box left blank gives no letter and the check cannot see it.",
        solved, cols=4, layout="c3", checks=[("V7 every cuboid is at most 4 cubes long, 4 wide and 3 high, drawn within 40 mm", all((a + b) * 4 + c * 8 <= 40 for a, b, c in dims), "")])
    return P

# =============================================================================== P5-33 Cuboid Volumes (code word)
def page33():
    rng = random.Random(5133)
    for _ in range(8000):
        items = []
        for k in range(6):
            un = "m" if k in (2, 5) else "cm"
            if k == 4: e = rng.randint(3, 9); items.append((e, e, e, un)); continue
            a, b, c = (rng.randint(2, 9), rng.randint(2, 9), rng.randint(2, 9)) if un == "m" else (rng.randint(3, 15), rng.randint(2, 12), rng.randint(2, 10))
            items.append((a, b, c, un))
        ans = [Fr(a * b * c) for a, b, c, _ in items]
        if not distinct(ans) or max(ans) > 1800 or len({(a, b, c) for a, b, c, _ in items}) < 6: continue
        pool = []
        for (a, b, c, u), v in zip(items, ans): pool += [Fr(a + b + c), Fr(2 * (a * b + b * c + a * c)), Fr(a * b + c), v * 2 if v * 2 < 2500 else v - a, Fr(a * b * c, 2) if (a * b * c) % 2 == 0 else v + a, Fr(a * b)]
        pool = [p for p in dict.fromkeys(pool) if p not in ans and p.denominator == 1 and 0 < p <= 2500]
        res = code_table_for(33, ans, rng, pool, n_decoy=2, tries=60)
        if res[0]: (word, table), dom = res; break
    else: raise RuntimeError("p33")
    cards = []
    for i, (a, b, c, u) in enumerate(items):
        cube = a == b == c
        fig = iso_dims(a, b, c, (f"{a} {u}", f"{b} {u}", f"{c} {u}"), w=52, hh=38)
        cards.append(qc(i + 1, f'<p class="qt">{"Cube volume" if cube else "Cuboid volume"}</p>{fig}', abx("w4") + f'<span class="unit">{u}{CU}</span>'))
    solved = []
    for cc in cards:
        d = read_dims(cc); solved.append(Fr(Decimal_(d[0][0])) * Fr(Decimal_(d[1][0])) * Fr(Decimal_(d[2][0])))
    P = code_page(33, 5133, "Cuboid Volumes", 1, "Volume of a cube and a cuboid; cm³ and m³", STRAND_AR,
        "volume of a cube or cuboid in cubic units (cm³ and m³)", ["VO2.4", "VO2.2"], "Code-breaker (volumes)",
        ["Find the volume of each solid.", "Write the number in the box. The unit is printed.", "Use the code table."],
        cards, ans, word, table, dom, lambda k: num(int(k)), "; ".join(f"{i+1}) {int(a)} {u}³" for i, (a, (_, _, _, u)) in enumerate(zip(ans, items))),
        "Six solids with their edges labelled: four cuboids and one cube in cm (the cube has the same edge on all three labels) and, on two figures, in m. The pupil multiplies the three edges; the unit of the answer is cm³ or m³ (the page prints it; there is no conversion between them). The decoy letters stand for the usual slips: adding the edges, the area of a face, or leaving one edge out. Figures are not drawn to scale (the page does not rely on the drawing). A box left blank gives no letter and the check cannot see it.",
        solved, cols=4, layout="c3", checks=[("V7 every volume is below 1800 and in a single unit", max(ans) < 1800, "")])
    return P

def Decimal_(s):
    from decimal import Decimal as D
    return D(s)

# =============================================================================== P5-34 Tank Match (matching)
def page34():
    rng = random.Random(5134)
    for _ in range(8000):
        word = word_candidates(34, 6)[0]
        ds = []
        for k in range(6):
            a, b, c = rng.choice([20, 25, 30, 40, 50, 60, 80]), rng.choice([10, 15, 20, 25, 30, 40]), rng.choice([10, 12, 15, 20, 25, 30, 40])
            V = a * b * c
            if V % 100 or not 1000 <= V <= 60000: break
            ds.append((a, b, c, V))
        else:
            if len({d[3] for d in ds}) == 6 and len({tuple(sorted(d[:3])) for d in ds}) == 6: break
    else: raise RuntimeError("p34")
    order = sorted(range(6), key=lambda k: ds[k][3])
    pairs = []
    for k in order:
        a, b, c, V = ds[k]
        pairs.append((iso_dims(a, b, c, (f"{a} cm", f"{b} cm", f"{c} cm"), w=52, hh=38), f"{dec(Fr(V, 1000))} {LIT}"))
    P = match_page(34, 5134, "Tank Match", 2, "Volume: litres and cubic centimetres", STRAND_AR,
        "volume of a cuboid; the relationship between litres and cm³ (1 ℓ = 1000 cm³)", ["VO2.4", "VO2.6"], "Matching (lettered cards)",
        ["1 ℓ = 1000 cm³. Each tank is full.", "Find how many ℓ each tank holds.", "Write the card's letter in the box under the matching tile."],
        rng, pairs, word, "; ".join(f"{w}: {ds[k][0]} x {ds[k][1]} x {ds[k][2]} = {ds[k][3]} cm³ = {dec(Fr(ds[k][3], 1000))} ℓ" for w, k in zip(word, order)),
        "Six tanks drawn with their length, width and height in cm, and six tiles with a capacity in litres, in order of size. The pupil multiplies the three edges to find the volume in cm³ and changes it to litres (1 ℓ = 1000 cm³). The letters, read from tile 1 to tile 6, spell a word with exactly one arrangement that is a word, so no wrong matching spells a word. Figures are not drawn to scale (the page does not rely on the drawing). A box left blank gives no letter and the check cannot see it.",
        None, None, left_title="Tanks", right_title="Capacities", raw_left=lambda h: (lambda d: Fr(Decimal_(d[0][0])) * Fr(Decimal_(d[1][0])) * Fr(Decimal_(d[2][0])) / 1000)(read_dims(h)), raw_right=lambda t: evaluate(t.replace(LIT, "").strip()))
    return P

# =============================================================================== P5-35 Tank Tales (code word)
def page35():
    rng = random.Random(5135)
    for _ in range(8000):
        items = []; ans = []
        l, w, h = rng.choice([40, 50, 60, 80]), rng.choice([25, 30, 40, 50]), rng.choice([20, 30, 40])
        if (l * w * h) % 1000: continue
        items.append((f"The base of a tub measures {l} cm by {w} cm. The tub is {h} cm high and is filled to the brim. How many {LIT} of water are in the tub?", LIT)); ans.append(Fr(l * w * h, 1000))
        l2, w2, h2 = rng.choice([50, 60, 80, 100]), rng.choice([30, 40, 50]), rng.choice([30, 40, 50]); d = rng.choice([10, 15, 20, 25])
        if (l2 * w2 * d) % 1000: continue
        items.append((f"A pond has a base {l2} cm by {w2} cm and walls {h2} cm high. Water fills it to a height of {d} cm. How many {LIT} of water are in the pond?", LIT)); ans.append(Fr(l2 * w2 * d, 1000))
        a = rng.randint(30, 90); b = rng.randint(8, a - 12)
        items.append((f"A paddling pool holds {a} {LIT} when full. It has {b} {LIT} of water in it. How many more {LIT} are needed to fill it?", LIT)); ans.append(Fr(a - b))
        l4, w4, h4 = rng.randint(8, 15), rng.randint(5, 12), rng.randint(4, 10)
        items.append((f"A box is {l4} cm by {w4} cm by {h4} cm. How many m{LIT} of water does it hold when full?", f"m{LIT}")); ans.append(Fr(l4 * w4 * h4))
        e = rng.choice([20, 30, 40, 50])
        items.append((f"A storage bin is a cube with edges of {e} cm. How many {LIT} of water does it hold when full?", LIT)); ans.append(Fr(e ** 3, 1000))
        A_ = rng.randint(20, 60); l6, w6, h6 = rng.choice([50, 60, 80]), rng.choice([40, 50]), rng.choice([30, 40, 50])
        if (l6 * w6 * h6) % 1000 or l6 * w6 * h6 // 1000 <= A_: continue
        items.append((f"A jug holds {A_} {LIT}. A sink measures {l6} cm by {w6} cm by {h6} cm. How many more {LIT} does the sink hold than the jug?", LIT)); ans.append(Fr(l6 * w6 * h6, 1000) - A_)
        if not distinct(ans) or any(a_.denominator != 1 or a_ > 999 for a_ in ans): continue
        order = list(range(6)); rng.shuffle(order)
        items = [items[k] for k in order]; ans = [ans[k] for k in order]
        pool = []
        for (t, u), a_ in zip(items, ans):
            n = [int(x) for x in re.findall(r"\d+", t)]
            pool += [a_ * 1000 if a_ < 999 else a_ // 1000, a_ * 10, Fr(a_, 10) if a_ % 10 == 0 else a_ + 10, Fr(n[0] * n[1] * n[2]) if len(n) >= 3 and a_ != n[0] * n[1] * n[2] and n[0] * n[1] * n[2] < 100000 else a_ + 5]
        pool = [Fr(p) for p in dict.fromkeys(pool) if Fr(p) not in ans and Fr(p).denominator == 1 and 0 < p <= 20000]
        res = code_table_for(35, ans, rng, pool, n_decoy=2, tries=60)
        if res[0]: (word, table), dom = res; break
    else: raise RuntimeError("p35")
    cards = [qc(i + 1, f'<p class="qt">{t}</p>', abx("w4") + f'<span class="unit">{u}</span>', cls="inl") for i, (t, u) in enumerate(items)]
    def solve(t):
        t = t.replace(NB, "")
        n = [int(x) for x in re.findall(r"\d+", t)]
        if t.startswith("The base of a tub"): return Fr(n[0] * n[1] * n[2], 1000)
        if t.startswith("A pond"): return Fr(n[0] * n[1] * n[3], 1000)
        if t.startswith("A paddling"): return Fr(n[0] - n[1])
        if t.startswith("A box"): return Fr(n[0] * n[1] * n[2])
        if t.startswith("A storage bin"): return Fr(n[0] ** 3, 1000)
        return Fr(n[1] * n[2] * n[3], 1000) - n[0]
    solved = [solve(to_text(re.search(r'<div class="qt">(.*?)</div></div><div class="qa">', c, re.S).group(1))) for c in cards]
    P = code_page(35, 5135, "Tank Tales", 2, "Volume of liquid in a rectangular tank; litres and cm³", STRAND_AR,
        "volume of liquid in a rectangular tank; the relationship between ℓ, mℓ and cm³", ["VO2.5", "VO2.6", "VO2.4"], "Code-breaker (tank stories)",
        ["1 ℓ = 1000 cm³ and 1 mℓ = 1 cm³.", "Read each story. Write the answer in the unit shown.", "Use the code table."],
        cards, ans, word, table, dom, lambda k: num(int(k)), "; ".join(f"{i+1}) {int(a)} {u}" for i, (a, (t, u)) in enumerate(zip(ans, items))),
        "Six tank stories: the capacity of a full tank, the water in a tank filled to a stated depth, the water still needed to fill a tank, the capacity of a small box in mℓ, a cube-shaped tank, and the difference between two tanks. Every step goes forward from the lengths to the volume; no story asks for a missing length or for a water level from a volume. The decoy letters stand for the usual slips: the answer left in cm³ or changed by the wrong power of ten. A box left blank gives no letter and the check cannot see it.",
        solved, cols=4, layout="c1", ps=True)
    return P

PAGES = [page28, page29, page30, page31, page32, page33, page34, page35]
