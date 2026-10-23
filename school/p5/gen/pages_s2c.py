"""Semester 2, part C (angles): P5-36 Angle Route; P5-37 Find the Angle; P5-38 Triangle Angles; P5-39 True, False or Not Sure; P5-40 Angle Chains."""
import random, re, math, itertools
from fractions import Fraction as Fr
from .common import *
from .kit import *
from .kit5 import *
from .art5 import *

DEG = "°"

def unknown_angle(h):
    """independent reader of line / point / opposite figures: the value of the angle marked ?"""
    kind, vals, rels = read_angle_fig(h)
    known = [int(v) for v in vals if v != "?"]
    if kind == "line": return 180 - sum(known)
    if kind == "point": return 360 - sum(known)
    if kind == "opp":
        r = rels[vals.index("?")]
        return known[0] if r == "opposite" else 180 - known[0]
    raise ValueError(kind)

# --------------------------------------------------------------------------- cells for the route and rows for the lettered choices
def make_fig(rng, V, kind=None, w=42, hh=34, scale_up=1.0):
    """an angle figure whose marked angle is V degrees; returns svg html"""
    kind = kind or rng.choice(["line", "line", "point", "opp", "opp"])
    for _ in range(300):
        if kind == "line":
            n = rng.choice([2, 3]); tot = 180 - V
            if n == 2: parts = [tot]
            else:
                a = rng.randint(25, tot - 25) if tot >= 50 else None
                if a is None: continue
                parts = [a, tot - a]
            if any(p < 25 or p > 155 for p in parts): continue
            parts.insert(rng.randrange(len(parts) + 1), "?")
            return line_fig(parts, w=w, hh=hh)
        if kind == "point":
            n = rng.choice([3, 4]); tot = 360 - V
            ks = [rng.randint(40, 150) for _ in range(n - 2)]
            last = tot - sum(ks)
            parts = ks + [last]
            if any(p < 40 or p > 170 for p in parts) or V < 30 or V > 170: continue
            parts.insert(rng.randrange(len(parts) + 1), "?")
            return point_fig(parts, w=w, hh=hh + 8)
        ask = rng.choice(["opposite", "adjacent"])
        g = V if ask == "opposite" else 180 - V
        if not 35 <= g <= 145 or g == 90: continue
        return opp_fig(g, g, ask, w=w, hh=hh + 8)
    return None

def page36():
    rng = random.Random(5136)
    T = rng.choice([55, 65, 70, 75])
    offs = [T + 10, T - 10, T + 20, T - 15, T + 5, 180 - T, T + 25, T - 20]
    offs = [o for o in offs if 35 <= o <= 140 and o != T]
    def on(i):
        while True:
            f = make_fig(rng, T)
            if f: return f
    def off():
        while True:
            f = make_fig(rng, rng.choice(offs))
            if f: return f
    rule = lambda c: unknown_angle(c) == T
    for _ in range(40):
        try:
            path, grid, dead = build_route(rng, 4, 8, on, off, 3, ok_text=rule); break
        except RuntimeError: continue
    else: raise RuntimeError("p36")
    P = route_page(36, 5136, "Angle Route", 1, "Geometry: angles on a straight line, at a point and vertically opposite angles", STRAND_GE,
        "angles on a straight line, angles at a point, vertically opposite angles, finding unknown angles", ["GE1.1", "GE1.2", "GE1.3", "GE1.4"], "Maze / path",
        ["Start at START. Move up, down, left or right.", f"Step only on figures where the angle marked ? is {T}{DEG}.", "Do not step on a box twice."],
        grid, path, dead, "", rule,
        f"A 4 by 4 grid of sixteen angle figures: angles on a straight line (they make a straight angle), angles at a point (a full turn) and two straight lines crossing (vertically opposite angles are equal; neighbouring angles make a straight angle). The angle marked ? is {T}{DEG} on the route. The boxes off the route give an answer a little more or less than {T}{DEG}, or the angle next to it; some extra boxes that do give {T}{DEG} are dead ends. Counting the boxes shows a line that takes a shortcut. Figures are not drawn to scale.",
        lambda c: f"? = {unknown_angle(c)}{DEG}", f"Does your line reach FINISH? Count its boxes: are there 8? Is every angle marked ? equal to {T}{DEG}?", extra_facts=str(T), cls="maze tall")
    return P

# =============================================================================== P5-37 Find the Angle (lettered choices)
def page37():
    rng = random.Random(5137)
    for _ in range(4000):
        word = word_candidates(37, 6)[0]
        kinds = ["line", "line", "point", "point", "opp", "opp"]; rng.shuffle(kinds)
        vs = rng.sample(range(35, 146, 5), 6)
        rows = []; keys = []
        for kd, V in zip(kinds, vs):
            f = make_fig(rng, V, kd, w=58, hh=24)
            if f is None: break
            cand = [180 - V, 360 - V if kd == "point" else V + 10, V + 10, V - 10, V + 20, 90 - V if V < 90 else V - 20]
            cand = [c for c in dict.fromkeys(cand) if 10 <= c <= 350 and c != V]
            if len(cand) < 2: break
            w2 = rng.sample(cand, 2)
            rows.append(dict(q='<span class="qs">Find the angle marked ?.</span>', fig=f, opts=[f"{V}{DEG}", f"{w2[0]}{DEG}", f"{w2[1]}{DEG}"], right=0)); keys.append(f"{V}{DEG}")
        else:
            if len({unknown_angle(r["fig"]) for r in rows}) == 6: break
    else: raise RuntimeError("p37")
    def solve_row(q, opts, qh):
        v = unknown_angle(qh)
        return [int(re.search(r"\d+", t).group(0)) for t in opts].index(v)
    P = mc_page(37, 5137, "Find the Angle", 1, "Geometry: finding unknown angles", STRAND_GE,
        "angles on a straight line, angles at a point, vertically opposite angles, finding unknown angles", ["GE1.1", "GE1.2", "GE1.3", "GE1.4"], "Lettered choices (figures)",
        ["Find the angle marked ? in each figure.", "Circle the letter of the right answer. Write the six letters in the boxes."],
        rng, rows, 3, word, "; ".join(f"{i+1}) {k}" for i, k in enumerate(keys)),
        f"Six figures, two of each kind: angles on a straight line (a straight angle), angles at a point (a full turn) and two crossing lines (vertically opposite angles equal, neighbours make a straight angle). The wrong choices are the usual slips: the angle next to the right one, a full turn used on a straight line, or the sum of the given angles. Each choice has a letter and the right choices spell the word. Every other way of choosing was tested against a very large word list. Figures are not drawn to scale. A box left blank gives no letter and the check cannot see it.",
        solve_row, rows_cls="mcgrid")
    return P

# =============================================================================== P5-38 Triangle Angles (code word)
def page38():
    rng = random.Random(5138)
    for _ in range(8000):
        items = []
        a, b = rng.randint(30, 80), rng.randint(30, 80)
        items.append(("sum", (a, b)))
        a, b = rng.randint(30, 90), rng.randint(30, 70)
        items.append(("sum", (a, b)))
        items.append(("apex", (rng.choice(range(30, 130, 2)),)))
        items.append(("base", (rng.randint(30, 75),)))
        items.append(("equi", (60,)))
        items.append(("right", (rng.randint(30, 65),)))
        def ans_of(kd, g):
            return {"sum": lambda: 180 - g[0] - g[1], "apex": lambda: Fr(180 - g[0], 2), "base": lambda: 180 - 2 * g[0], "equi": lambda: 60, "right": lambda: 90 - g[0]}[kd]()
        ans = [Fr(ans_of(*it)) for it in items]
        if not distinct(ans) or any(x.denominator != 1 or x < 20 for x in ans) or any(it[0] == "sum" and sum(it[1]) >= 160 for it in items): continue
        rng.shuffle(items); ans = [Fr(ans_of(*it)) for it in items]
        pool = []
        for (kd, g), v in zip(items, ans): pool += [Fr(180 - g[0]), Fr(180 - sum(g)) if kd == "sum" else Fr(g[0]), Fr(sum(g)) if kd == "sum" else Fr(90 - g[0] // 2), v + 10, v - 10, Fr(g[0], 2)]
        pool = [p for p in dict.fromkeys(pool) if p not in ans and p.denominator == 1 and 10 <= p <= 175]
        res = code_table_for(38, ans, rng, pool, n_decoy=2, tries=60)
        if res[0]: (word, table), dom = res; break
    else: raise RuntimeError("p38")
    cards = [qc(i + 1, '<p class="qt">Angle marked ?</p>' + tri_angles(kd, g, w=50, hh=38), abx("w3") + f'<span class="unit">{DEG}</span>', cls="figc") for i, (kd, g) in enumerate(items)]
    def solve(h):
        kind, labs, ticks, ra = read_tri_angles(h)
        d = {pos: v for v, pos in labs}
        known = [int(v) for v, pos in labs if v != "?"]
        if ra: return 90 - known[0]
        if ticks == 3: return 60
        if ticks == 2:
            if d.get("apex", "?") != "?": return Fr(180 - int(d["apex"]), 2)
            return 180 - 2 * [int(v) for v, pos in labs if v != "?" and pos != "apex"][0]
        return 180 - sum(known)
    solved = [Fr(solve(c)) for c in cards]
    P = code_page(38, 5138, "Triangle Angles", 1, "Geometry: angle sum of a triangle; isosceles, equilateral and right-angled triangles", STRAND_GE,
        "angle sum of a triangle; properties of isosceles, equilateral and right-angled triangles; finding unknown angles", ["GE2.1", "GE2.2", "GE2.3", "GE1.4"], "Code-breaker (angles in triangles)",
        ["Find the angle marked ? in each triangle.", "Ticks show sides of equal length. A square shows a right angle.", "Write the angle in the box. Use the code table."],
        cards, ans, word, table, dom, lambda k: f"{int(k)}{DEG}", "; ".join(f"{i+1}) {int(a)}{DEG} ({kd})" for i, (a, (kd, g)) in enumerate(zip(ans, items))),
        f"Six triangles: two with two angles given (the three angles of a triangle make a straight angle), an isosceles triangle with the angle at the top given, an isosceles triangle with a base angle given, an equilateral triangle and a right-angled triangle with one other angle given. Equal sides carry tick marks. The decoy letters stand for the usual slips: giving a straight angle minus one angle only, adding the angles, or not halving the base angles. The page does not rely on the drawing: the pupil should use the angle facts, not a protractor. A box left blank gives no letter and the check cannot see it.",
        solved, cols=4, layout="c3")
    return P

# =============================================================================== P5-39 True, False or Not Sure (lettered choices, three choices)
def statement39(rng, kind, names):
    """a shape, what is given and a claim about a second angle: (text, claim angle letter pair)"""
    A, B, C, D = names
    a = rng.randint(50, 80)
    adj = [(A, B), (B, C), (C, D), (D, A)]; opp = [(A, C), (B, D)]
    shape = {"para": "parallelogram", "rho": "rhombus", "trap": "trapezium"}[kind.split("_")[0]]
    leg = [(A, D), (D, A), (B, C), (C, B)]
    if kind == "para_adj_true": (x, y), b = rng.choice(adj), 180 - a
    elif kind == "para_adj_false": (x, y), b = rng.choice(adj), a
    elif kind == "para_opp_true": (x, y), b = rng.choice(opp), a
    elif kind == "para_opp_false": (x, y), b = rng.choice(opp), 180 - a
    elif kind == "rho_adj_true": (x, y), b = rng.choice(adj), 180 - a
    elif kind == "rho_opp_false": (x, y), b = rng.choice(opp), 180 - a
    elif kind == "trap_leg_true": (x, y), b = rng.choice(leg), 180 - a
    elif kind == "trap_leg_false": (x, y), b = rng.choice(leg), a
    elif kind == "trap_unsure": (x, y), b = rng.choice([(A, B), (D, C)]), a   # the two angles on one parallel side: unsure whether a trapezium has exactly one or at least one pair of parallel sides
    else: raise ValueError(kind)
    par = f" {A}{B} is parallel to {D}{C}. {A}{D} and {B}{C} are the other two sides." if shape == "trapezium" else ""
    return f"{names_s(names)} is a {shape}.{par} Given: \u2220{x} = {a}{DEG}. Claim: \u2220{y} = {b}{DEG}."

def names_s(n): return "".join(n)

def judge39(t):
    """independent judge of a printed row: is the CLAIM true, false or not possible to tell, from the shape and the given angle"""
    m = re.match(r"(\w{4}) is a (parallelogram|rhombus|trapezium)\.(?: (\w)(\w) is parallel to (\w)(\w)\. \w\w and \w\w are the other two sides\.)? Given: \u2220(\w) = (\d+)\u00b0\. Claim: \u2220(\w) = (\d+)\u00b0\.", t)
    nm, shape, p1, p2, p3, p4, x, vx, y, vy = m.groups()
    vx, vy = int(vx), int(vy)
    pos = {c: i for i, c in enumerate(nm)}
    d = (pos[x] - pos[y]) % 4
    if shape in ("parallelogram", "rhombus"):
        if d == 2: return "T" if vx == vy else "F"
        return "T" if vx + vy == 180 else "F"
    par = {p1 + p2, p2 + p1, p3 + p4, p4 + p3}
    legs = [(nm[i % 4], nm[(i + 1) % 4]) for i in range(4)]
    leg_pairs = [pr for pr in legs if "".join(pr) not in par]
    same_leg = any({x, y} == set(pr) for pr in leg_pairs)
    if same_leg: return "T" if vx + vy == 180 else "F"
    return "N"

def page39():
    rng = random.Random(5139)
    kinds_all = [["para_adj_true", "para_opp_false", "rho_adj_true", "trap_leg_true", "trap_unsure", "para_opp_true"],
                 ["para_adj_false", "rho_opp_false", "trap_leg_false", "trap_unsure", "para_adj_true", "trap_leg_true"],
                 ["para_opp_true", "para_adj_false", "trap_unsure", "trap_leg_true", "rho_adj_true", "trap_leg_false"]]
    for _ in range(4000):
        word = word_candidates(39, 6)[0]
        kinds = rng.choice(kinds_all)[:]; rng.shuffle(kinds)
        pool_names = ["ABCD", "PQRS", "KLMN", "EFGH", "WXYZ", "TUVW"]; rng.shuffle(pool_names)
        sts = [statement39(rng, k, tuple(pool_names[i])) for i, k in enumerate(kinds)]
        truth = [judge39(s) for s in sts]
        if len(set(truth)) == 3 and all(truth.count(t) <= 3 for t in "TFN") and len(set(sts)) == 6: break
    else: raise RuntimeError("p39")
    right = {"T": 0, "F": 1, "N": 2}
    rows = [dict(q=f'<span class="qs">{s}</span>', opts=["T", "F", "N"], right=right[t], fixed=True, wide=True) for s, t in zip(sts, truth)]
    def solve_row(q, opts, qh): return right[judge39(q.replace(NB, " "))]
    P = mc_page(39, 5139, "Shape Statements", 2, "Geometry: parallelogram, rhombus and trapezium", STRAND_GE,
        "properties of a parallelogram, rhombus and trapezium; finding unknown angles", ["GE3.1", "GE3.2"], "True or false table (three choices)",
        ["Use the shape and the given angle.", "Is the claim true (T), false (F) or not possible to tell (N)?", "Circle the letter. Write the six letters in the boxes."],
        rng, rows, 3, word, "; ".join(f"{i+1}) {t} ({s})" for i, (s, t) in enumerate(zip(sts, truth))),
        f"Six rows, each with a shape, one given angle and a claim about a second angle. A trapezium here has at least one pair of parallel sides; the rows marked N compare the two angles on the same parallel side, so the answer is the same if a trapezium is taken to have exactly one pair. The pupil decides whether the claim must be true, must be false, or cannot be told from the given facts. In a parallelogram or rhombus opposite angles are equal and neighbouring angles make a straight angle; in a trapezium the two angles on the same non-parallel side make a straight angle (the page names the parallel sides and the other two sides), and two angles that are not on the same non-parallel side cannot be found from each other, so the answer is N. Each choice (T, F, N) has a letter and the right choices spell the word. Every other way of choosing was tested against a very large word list. A box left blank gives no letter and the check cannot see it.",
        solve_row, ps=False, rows_cls="tfrows tight")
    return P

# =============================================================================== P5-40 Angle Chains (code word)
def page40():
    rng = random.Random(5140)
    for _ in range(8000):
        items = []
        for kd in ["ext", "ext", "isoext", "isoext", "ext2", "ext2"]:
            if kd == "ext": a, b = rng.randint(30, 80), rng.randint(30, 80); items.append((kd, (a, b), a + b))
            elif kd == "isoext": g = rng.choice(range(30, 130, 2)); items.append((kd, (g,), 180 - (180 - g) // 2))
            else:
                e, f = rng.randint(105, 150), rng.randint(105, 150)
                if not 35 <= e + f - 180 <= 110: continue
                items.append((kd, (e, f), e + f - 180))
        if len(items) < 6: continue
        ans = [Fr(i[2]) for i in items]
        if not distinct(ans) or any(i[0] == "ext" and i[2] >= 165 for i in items): continue
        rng.shuffle(items); ans = [Fr(i[2]) for i in items]
        pool = []
        for kd, g, v in items: pool += [Fr(180 - v), Fr(180 - sum(g)) if kd == "ext" else Fr((180 - g[0]) // 2) if kd == "isoext" else Fr(360 - sum(g)), Fr(v + 10), Fr(v - 10), Fr(g[0])]
        pool = [Fr(p) for p in dict.fromkeys(pool) if Fr(p) not in ans and 10 <= p <= 175]
        res = code_table_for(40, ans, rng, pool, n_decoy=2, tries=60)
        if res[0]: (word, table), dom = res; break
    else: raise RuntimeError("p40")
    figs = []
    for kd, g, v in items:
        figs.append(ext_fig(*g, w=50, hh=40) if kd == "ext" else isoext_fig(*g, w=50, hh=40) if kd == "isoext" else ext2_fig(*g, w=50, hh=40))
    cards = [qc(i + 1, '<p class="qt">Angle marked ?</p>' + f, abx("w3") + f'<span class="unit">{DEG}</span>', cls="figc") for i, f in enumerate(figs)]
    def solve(h):
        kind, d = read_labels(h)
        if kind == "ext": return Fr(180 - (180 - int(d["apex"]) - int(d["base1"])))
        if kind == "isoext": return Fr(180 - (180 - int(d["apex"])) // 2)
        e_, f_ = int(d["extB"]), int(d["extC"])      # two angles on straight lines give two angles of the triangle; the third is the rest of 180
        return Fr(180 - (180 - e_) - (180 - f_))
    solved = [solve(c) for c in cards]
    P = code_page(40, 5140, "Angle Chains", 2, "Geometry: unknown angles in two steps", STRAND_GE,
        "finding unknown angles in two steps: angle sum of a triangle with angles on a straight line or vertically opposite angles", ["GE1.4", "GE2.2", "GE2.3", "GE1.1", "GE1.3", "GE2.1"], "Code-breaker (angle chains)",
        ["Find the angle marked ? in each figure.", "Use two steps. Ticks show sides of equal length.", "Write the angle in the box. Use the code table."],
        cards, ans, word, table, dom, lambda k: f"{int(k)}{DEG}", "; ".join(f"{i+1}) {int(a)}{DEG} ({kd})" for i, (a, (kd, g, v)) in enumerate(zip(ans, items))),
        f"Six two-step figures, two of each kind: a triangle with two angles given and one side extended (find the third angle, then the angle on the straight line); an isosceles triangle with the top angle given and the base extended (find the base angle, then the angle on the straight line); and a triangle on a straight line with the two outside angles given (find the two inside angles on the line, then the third angle of the triangle). The decoy letters stand for the usual slips: the angle inside the triangle instead of the angle on the line, or stopping after the first step. Figures are not drawn to scale. A box left blank gives no letter and the check cannot see it.",
        solved, cols=4, layout="c3", ps=True)
    return P

PAGES = [page36, page37, page38, page39, page40]
