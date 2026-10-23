"""Part D: composite figures, perimeter, volume. P6-21 Shaded Shapes, P6-22 Perimeter Pick, P6-23 Cuboid Corners, P6-24 Root Maze, P6-25 Base and Height, P6-26 Tank Stories."""
import random, re, math, itertools
from fractions import Fraction as Fr
from math import gcd
from .common import *
from .kit import *
from .kit6 import *
from . import figs as F
from .pages_c import PI22, semi_area, semi_perim, quarter_area, quarter_perim, cc_area

# =============================================================================== area / perimeter of the composite figures, read from the PRINTED figure
def fig_area(card):
    r = F.read_fig(card); k = r["kind"]; n = {p: F.num_of(v) for p, v in r["pos"].items()}
    if k == "fig-rsemi": return n["top"] * n["left"] + PI22 * (n["left"] / 2) ** 2 / 2
    if k == "fig-ssemi": return n["top"] ** 2 + PI22 * (n["top"] / 2) ** 2 / 2
    if k == "fig-sqq": return n["top"] ** 2 - PI22 * n["top"] ** 2 / 4
    if k == "fig-sqs": return n["top"] ** 2 - PI22 * (n["top"] / 2) ** 2 / 2
    if k == "fig-rtri": return n["top"] * n["left"] + n["top"] * n["hgt"] / 2
    raise ValueError(k)

def fig_perim(card):
    r = F.read_fig(card); k = r["kind"]; n = {p: F.num_of(v) for p, v in r["pos"].items()}
    if k == "fig-rsemi": return 2 * n["top"] + n["left"] + PI22 * n["left"] / 2
    if k == "fig-ssemi": return 3 * n["top"] + PI22 * n["top"] / 2
    if k == "fig-sqq": return 2 * n["top"] + PI22 * n["top"] / 2
    if k == "fig-semi": return PI22 * n["main"] / 2 + n["main"] if "main" in n else None
    raise ValueError(k)

# =============================================================================== P6-21 Shaded Shapes  (AV1.3, code)
def ss_figure(rng, kind, tag):
    if kind == "rsemi":
        W = rng.choice([14, 28]); L = rng.choice([x for x in (16, 18, 20, 21, 22, 24, 25, 26, 30, 35, 40) if x >= W - 2 and (x * W) < 900])
        return F.rect_semi_fig(L, W)
    if kind == "ssemi": return F.sq_semi_fig(rng.choice([14, 28]))
    if kind == "sqq": return F.sq_minus_quarter_fig(rng.choice([14, 28]), tag)
    if kind == "sqs": return F.sq_minus_semi_fig(rng.choice([14, 28]), tag)
    L = rng.choice([8, 10, 12, 14, 16]); W = rng.randint(4, 10); h = rng.choice([6, 8, 10, 12])
    return F.rect_tri_fig(L, W, h)

def page21():
    rng = random.Random(8121)
    kinds = ["rsemi", "ssemi", "sqq", "sqs", "rtri", "rtri"]
    for _ in range(2000):
        figs_ = [ss_figure(rng, k, str(i)) for i, k in enumerate(kinds)]
        ans = [fig_area(f) for f in figs_]
        if len(set(ans)) < 6 or any(a.denominator != 1 or a > 1200 for a in ans): continue
        ans = [int(a) for a in ans]
        pool = set()
        for f, a in zip(figs_, ans):
            r = F.read_fig(f); n = {p: F.num_of(v) for p, v in r["pos"].items()}; k = r["kind"]
            if k == "fig-rsemi": w = [n["top"] * n["left"] + PI22 * (n["left"] / 2) ** 2, n["top"] * n["left"], n["top"] * n["left"] + PI22 * n["left"] / 2]
            elif k == "fig-ssemi": w = [n["top"] ** 2 + PI22 * (n["top"] / 2) ** 2, PI22 * (n["top"] / 2) ** 2 / 2, n["top"] ** 2]
            elif k == "fig-sqq": w = [PI22 * n["top"] ** 2 / 4, n["top"] ** 2, n["top"] ** 2 + PI22 * n["top"] ** 2 / 4]
            elif k == "fig-sqs": w = [PI22 * (n["top"] / 2) ** 2 / 2, n["top"] ** 2 + PI22 * (n["top"] / 2) ** 2 / 2, n["top"] ** 2 - PI22 * (n["top"] / 2) ** 2]
            else: w = [n["top"] * n["left"] + n["top"] * n["hgt"], n["top"] * n["hgt"] / 2, n["top"] * n["left"]]
            for v in w:
                if v.denominator == 1 and int(v) not in ans and 1 <= v <= 1250: pool.add(int(v))
        res = make_table(21, ans, rng, 1, 1250, pool=sorted(pool), n_decoy=3)
        if res: word, table = res; break
    cards = []
    for i, f in enumerate(figs_):
        cards.append(qcard(i + 1, f'<div class="fig fcd">{f}</div>', f'{abx("w3")}{unit("cm²")}', cls="posb"))
    P = code_page(21, 8121, "Shaded Shapes", 1, "Area of composite figures", STRAND_AV,
        "1.3 (composite figures made of squares, rectangles, triangles, semicircles and quarter circles)", ["AV1.3"], "Code-breaker (composite areas)",
        [f"Take {PIP} as 22/7; all lengths are in cm.", "Find the area of each figure (the hatched part, if there is hatching).", "Write the answer in the box. Use the code table."],
        cards, ans, table, word, 1, 1250, "; ".join(f"{i+1}) {a} cm²" for i, a in enumerate(ans)),
        "Six figures: a rectangle with a semicircle on one end, a square with a semicircle on one side, a square with a quarter circle cut away (hatched), a square with a semicircle cut out (hatched), and two rectangles with a triangle on top. Sizes are chosen so that every answer is a whole number with π as 22/7. The decoy numbers are what a pupil gets by using a full circle instead of a half, by forgetting the half in the triangle, or by adding instead of subtracting. A box left blank gives no letter and the check cannot see it.", ncols=3)
    solved = [int(fig_area(f)) for f in figs_]
    P.v("V1 independent solver reads every printed figure (kind and labelled lengths) and finds the area: equals the key", solved == ans, solved)
    P.v("V7 every answer is a whole number of at most 1200 cm²", all(1 <= a <= 1200 for a in ans))
    return P

# =============================================================================== P6-22 Perimeter Pick  (AV1.2, AV1.3, choice with figures)
def pp_options(rng, right, wrongs):
    vals = [right] + wrongs; order = list(range(3)); rng.shuffle(order)
    return [f'<span class="rt">{dec(vals[j])} cm</span>' for j in order], order.index(0)

def page22():
    rng = random.Random(8222)
    for _ in range(300):
        rows = []
        kinds = ["semi", "quarter", "rsemi", "ssemi", "sqq", "rsemi"]; rng.shuffle(kinds)
        for i, k in enumerate(kinds):
            if k == "semi":
                d = rng.choice([14, 28, 7, 21]); fig = F.semicircle_fig(d); right = semi_perim(d); wr = [PI22 * d / 2, PI22 * d + d]
            elif k == "quarter":
                r = rng.choice([14, 28, 7, 21]); fig = F.quarter_fig(r); right = quarter_perim(r); wr = [PI22 * r / 2, PI22 * r + 2 * r]
            elif k == "rsemi":
                W = rng.choice([14, 28]); L = rng.choice([x for x in (16, 18, 20, 21, 24, 25, 30, 35) if x > W - 2]); fig = F.rect_semi_fig(L, W)
                right = 2 * L + W + PI22 * W / 2; wr = [2 * L + 2 * W + PI22 * W / 2, 2 * L + W]
            elif k == "ssemi":
                s = rng.choice([14, 28]); fig = F.sq_semi_fig(s); right = 3 * s + PI22 * s / 2; wr = [4 * s + PI22 * s / 2, 3 * s]
            else:
                s = rng.choice([14, 28]); fig = F.sq_minus_quarter_fig(s, str(i)); right = 2 * s + PI22 * s / 2; wr = [4 * s, PI22 * s / 2 + s]
            opts, ri = pp_options(rng, right, wr)
            if len({right, *wr}) < 3: break
            rows.append(dict(stem=f'<div class="fig fcd">{fig}</div>', opts=opts, right=ri))
        else:
            break
    def solve_row(stem, opts):
        r = F.read_fig(stem); kd = r["kind"]; n = {p: F.num_of(v) for p, v in r["pos"].items()}
        if kd == "fig-semi": v = semi_perim(n["main"])
        elif kd == "fig-quarter": v = quarter_perim(n["main"])
        else: v = fig_perim(stem)
        for j, o in enumerate(opts):
            if Fr(re.search(r"(\d+(?:\.\d+)?)", ptxt(o)).group(1)) == v: return j
        return -1
    P = choice_page(22, 8222, "Perimeter Pick", 2, "Perimeter of figures with curved edges", STRAND_AV,
        "1.2, 1.3 (perimeter of a semicircle and a quarter circle; composite figures)", ["AV1.2", "AV1.3"], "Choice table (perimeters)",
        [f"Take {PIP} as 22/7; all lengths are in cm.", "Find the perimeter, of the hatched part if there is hatching. Only the outside counts.", "Circle the letter beside the right answer. Write the letters in the boxes."],
        rng, rows, solve_row,
        "Six figures: a semicircle, a quarter circle, two rectangles with a semicircle on one end, a square with a semicircle on one side and a square with a quarter circle cut away (the hatched part). Each row has three answers. The wrong answers are what a pupil gets by leaving out the straight edges, by counting a dashed line that is inside the figure, or by using the whole circle. The perimeter of a semicircle includes its diameter. The letters of the right answers, read down the rows, spell the word. Every other way of choosing was tested against a very large word list: none spells a word. A box left blank gives no letter and the check cannot see it.",
        key_rows=None, grid=True)
    return P

# =============================================================================== P6-23 Cuboid Corners  (VO2.1, code)
def cc_items(rng):
    items = []
    forms = ["h_fig", "l_fig", "b_fig", "h_txt", "b_txt", "l_txt"]
    for f in forms:
        while True:
            l, b, h = rng.randint(4, 15), rng.randint(3, 12), rng.randint(3, 12)
            if len({l, b, h}) == 3: break
        V = l * b * h; unk = f[0]
        ans = {"l": l, "b": b, "h": h}[unk]
        items.append(dict(f=f, l=l, b=b, h=h, V=V, ans=ans, unk=unk))
    return items

def cc_card(i, it):
    unk = it["unk"]; V = it["V"]
    if it["f"].endswith("fig"):
        fig = F.cuboid_fig(it["l"] if unk != "l" else None, it["b"] if unk != "b" else None, it["h"] if unk != "h" else None)
        name = {"l": "length", "b": "breadth", "h": "height"}[unk]
        return qcard(i + 1, f'<div class="figrow">{fig}<p>Volume = {V} cm³. Find the {name}.</p></div>', f'{abx("w3")}{unit("cm")}')
    kn = {"l": ("breadth", it["b"], "height", it["h"]), "b": ("length", it["l"], "height", it["h"]), "h": ("length", it["l"], "breadth", it["b"])}[unk]
    name = {"l": "length", "b": "breadth", "h": "height"}[unk]
    thing = rng_choice(i, ["box", "block", "tank", "case"])
    return qcard(i + 1, f'<p>A {thing} is a cuboid. Its volume is {V} cm³. Its {kn[0]} is {kn[1]} cm and its {kn[2]} is {kn[3]} cm. Find its {name}.</p>', f'{abx("w3")}{unit("cm")}')

def rng_choice(i, xs): return xs[i % len(xs)]

def cc_solve(card):
    t = ptxt(card)
    if "<svg" in card:
        r = F.read_fig(card); V = int(re.search(r"Volume = (\d+) cm", t).group(1))
        known = [F.num_of(v) for p, v in r["pos"].items() if v != "?"]
        return int(Fr(V) / (known[0] * known[1]))
    V = int(re.search(r"volume is (\d+) cm", t).group(1))
    dims = [int(x) for x in re.findall(r"is (\d+) cm", t)[0:]]
    dims = [int(x) for x in re.findall(r"(?:length|breadth|height) is (\d+) cm", t)]
    return V // (dims[0] * dims[1])

def page23():
    rng = random.Random(8323)
    for _ in range(300):
        its = cc_items(rng); ans = [it["ans"] for it in its]
        if not distinct(ans): continue
        pool = set()
        for it in its:
            for w in (it["V"] // it["ans"] // max(1, min(it["l"], it["b"], it["h"])) if False else None, it["V"] // (it["l"] * it["b"]) if False else None, it["l"] + it["b"] + it["h"] if False else None):
                pass
            others = [x for x in (it["l"], it["b"], it["h"]) if x != it["ans"]]
            pool |= {it["V"] // others[0] if it["V"] % others[0] == 0 else others[0] * others[1], others[0] * others[1], it["V"] - others[0] * others[1], it["ans"] + 1, it["ans"] - 1}
        pool = sorted(p for p in pool if p not in ans and 1 <= p <= 100)
        res = make_table(23, ans, rng, 1, 100, pool=pool, n_decoy=3)
        if res: word, table = res; break
    cards = [cc_card(i, it) for i, it in enumerate(its)]
    P = code_page(23, 8323, "Cuboid Corners", 1, "Volume: finding a missing length of a cuboid", STRAND_AV,
        "2.1 (finding a missing dimension of a cuboid given its volume and the other dimensions)", ["VO2.1"], "Code-breaker (missing dimension)",
        ["Each shape is a cuboid.", "Find the length, breadth or height that is missing.", "Write the answer in the box. Use the code table."],
        cards, ans, table, word, 1, 100, "; ".join(f"{i+1}) {it['unk']} = {a} cm" for i, (it, a) in enumerate(zip(its, ans))),
        "Six cuboids: three drawn with one edge marked by a question mark and three in words. The volume is given and two of the three edges; the pupil divides the volume by the product of the two edges. The decoy numbers are what a pupil gets by dividing the volume by only one edge, by multiplying the two edges, or by taking the volume less the product of the edges. A box left blank gives no letter and the check cannot see it.", ncols=2)
    solved = [cc_solve(c) for c in cards]
    P.v("V1 independent solver reads each printed cuboid or sentence (volume and two edges) and finds the third edge: equals the key", solved == ans, solved)
    P.v("V7 every edge is a whole number from 3 to 15 and the three edges of a cuboid are different", all(len({it["l"], it["b"], it["h"]}) == 3 and max(it["l"], it["b"], it["h"]) <= 15 for it in its))
    return P

# =============================================================================== P6-24 Root Maze  (VO2.2, VO2.5, route)
def root_cells(T, rng):
    good, bad = [], []
    def add(v, h):
        (good if v == T else bad).append(h)
    for a in range(2, 13):
        add(Fr(a), f"{SQRT}{a * a}")
        for k in range(1, 7):
            add(Fr(a + k), f"{SQRT}{a * a} + {k}"); 
            if a - k > 0: add(Fr(a - k), f"{SQRT}{a * a} − {k}")
        if a % 2 == 0:
            add(Fr(a // 2), f"{SQRT}{a * a} ÷ 2")
        for k in (2, 3):
            add(Fr(a * k), f"{k} × {SQRT}{a * a}")
    for a in range(2, 11):
        add(Fr(a), f"{CBRT}{a ** 3}")
        for k in range(1, 7):
            add(Fr(a + k), f"{CBRT}{a ** 3} + {k}")
            if a - k > 0: add(Fr(a - k), f"{CBRT}{a ** 3} − {k}")
        for k in (2, 3):
            add(Fr(a * k), f"{k} × {CBRT}{a ** 3}")
        add(Fr(a), f"edge of a {a ** 3} cm³ cube")
    for a in range(2, 13):
        add(Fr(a), f"side of a {a * a} cm² square")
    return sorted(set(good)), sorted(set(bad))

def ev_root(h):
    t = ptxt(h)
    m = re.fullmatch(r"edge of a (\d+) cm³ cube", t)
    if m: return calc(f"∛ {m.group(1)}")
    m = re.fullmatch(r"side of a (\d+) cm² square", t)
    if m: return calc(f"√ {m.group(1)}")
    return calc(t)

def page24():
    rng = random.Random(8424)
    T = Fr(6)
    good, bad = root_cells(T, rng)
    return route_page(24, 8424, "Root Maze", 1, "Square roots and cube roots", STRAND_AV,
        "2.5 (use of the square-root and cube-root signs)", ["VO2.5"], "Maze / path",
        ["Start at START. Move up, down, left or right.", f"Step only on boxes where the answer is {T}.", "Do not step on a box twice."],
        rng, 4, 8, good, bad, ev_root, T, str(T),
        f"A 4 by 4 grid of sixteen boxes: square roots, cube roots, and a root with a number added, taken away or multiplied. The route follows the boxes that equal {T}. The wrong boxes include answers close to {T}. Two extra boxes that equal {T} are dead ends. Counting the boxes shows a line that takes a shortcut.",
        cls="maze xs tall")

# =============================================================================== P6-25 Base and Height  (VO2.3, VO2.4, match)
def bh_item(rng, kind):
    if kind == "h_from_base":
        while True:
            A, h = rng.randint(6, 80), rng.randint(3, 15)
            if A * h <= 1500: break
        return dict(t=f"A cuboid has a volume of {A * h} cm³ and a base area of {A} cm². Find its height.", val=Fr(h), sq=False)
    if kind == "base_from_h":
        while True:
            A, h = rng.randint(6, 80), rng.randint(3, 15)
            if A * h <= 1500: break
        return dict(t=f"A cuboid has a volume of {A * h} cm³ and a height of {h} cm. Find the area of its base.", val=Fr(A), sq=True)
    if kind == "face":
        while True:
            l, h, b = rng.randint(4, 16), rng.randint(3, 12), rng.randint(3, 12)
            if len({l, h, b}) == 3: break
        return dict(t=f"A cuboid has a volume of {l * h * b} cm³ and a breadth of {b} cm. Find the area of its front face (length × height).", val=Fr(l * h), sq=True)
    if kind == "tank":
        while True:
            A, h = rng.choice([200, 250, 400, 500, 600, 800]), rng.randint(5, 30)
            if A * h <= 30000: break
        return dict(t=f"A tank has a base area of {A} cm². It holds {A * h} cm³ of water. How deep is the water?", val=Fr(h), sq=False)
    if kind == "cube_face":
        e = rng.randint(3, 11)
        return dict(t=f"A cube has a volume of {e ** 3} cm³. Find the area of one face of the cube.", val=Fr(e * e), sq=True)
    while True:
        l, b, h = rng.randint(4, 14), rng.randint(3, 12), rng.randint(3, 12)
        if len({l, b, h}) == 3: break
    return dict(t=f"A cuboid has a volume of {l * b * h} cm³. Its base is {l} cm by {b} cm. Find its height.", val=Fr(h), sq=False)

def bh_solve(item_html, chs):
    t = ptxt(item_html)
    mV = re.search(r"volume of (\d+) cm", t); V = int(mV.group(1)) if mV else None
    if "deep" in t:
        A = int(re.search(r"base area of (\d+) cm", t).group(1)); V2 = int(re.search(r"holds (\d+) cm", t).group(1)); v = Fr(V2, A); sq = False
    elif "base area of" in t and "height" in t.split("Find")[-1]:
        v = Fr(V, int(re.search(r"base area of (\d+) cm", t).group(1))); sq = False
    elif "height of" in t and "area of its base" in t:
        v = Fr(V, int(re.search(r"height of (\d+) cm", t).group(1))); sq = True
    elif "front face" in t:
        v = Fr(V, int(re.search(r"breadth of (\d+) cm", t).group(1))); sq = True
    elif "cube" in t:
        e = round(V ** (1 / 3)); assert e ** 3 == V; v = Fr(e * e); sq = True
    else:
        a, b = map(int, re.search(r"base is (\d+) cm by (\d+) cm", t).groups()); v = Fr(V, a * b); sq = False
    for j, c in enumerate(chs):
        m = re.fullmatch(r"(\d+(?:\.\d+)?) cm(²?)", ptxt(c))
        if m and Fr(m.group(1)) == v and (m.group(2) == "²") == sq: return j
    return -1

def page25():
    rng = random.Random(8525)
    kinds = ["h_from_base", "base_from_h", "face", "tank", "cube_face", "box"]
    for _ in range(500):
        its = [bh_item(rng, k) for k in kinds]; rng.shuffle(its)
        vals = [(it["val"], it["sq"]) for it in its]
        if len(set(vals)) < 6: continue
        # decoys: the number of an answer with the wrong unit; and a plausible slip (volume divided by the other number)
        k0 = next(i for i, v in enumerate(vals) if not v[1]); d1 = (vals[k0][0], True)
        k1 = next(i for i, it in enumerate(its) if it["sq"]); d2 = (vals[k1][0] * 2 if vals[k1][0] % 2 == 0 else vals[k1][0] + 1, True)
        allv = vals + [d1, d2]
        if len(set(allv)) < 8: continue
        break
    order = list(range(8)); rng.shuffle(order)
    card_html = [f'<span class="rt">{dec(allv[j][0])} cm{"²" if allv[j][1] else ""}</span>' for j in order]
    right = [order.index(i) for i in range(6)]
    items = [f'<p style="margin:0;font-size:12.5pt;font-family:Nunito Sans;font-weight:400">{it["t"]}</p>' for it in its]
    P = match_page(25, 8525, "Base and Height", 2, "Volume: base area, height and faces", STRAND_AV,
        "2.3, 2.4, 2.2 (height of a cuboid from volume and base area; area of a face from volume and one dimension; edge of a cube)", ["VO2.3", "VO2.4", "VO2.2"], "Matching (base area, height, face)",
        ["Work out each answer.", "Find the card with that answer and its unit.", "Write the card letter in the box. Use each card once. Two cards are not used."],
        rng, items, card_html, right, bh_solve,
        "Six questions: the height from the volume and the base area, the base area from the volume and the height, the area of a face from the volume and one edge, the depth of water in a tank, the face of a cube from its volume, and the height from the volume and a base given by its two edges. Two cards are decoys. A card carries a number and a unit: lengths are in cm and areas in cm². The letters of the matching cards, read in the order of the items, spell the word. Every way of giving each item a different card, and every single changed letter, was tested against a very large word list: none spells another word. A box left blank gives no letter and the check cannot see it.",
        item_cols=1, card_cols=4, compact=True)
    return P

# =============================================================================== P6-26 Tank Stories  (VO2.3, revisits volume of liquid: litres and cm³, code)
def tank_item(rng, kind):
    if kind == "depth":
        while True:
            l, b, V = rng.choice([40, 50, 60, 80]), rng.choice([25, 30, 40, 50]), rng.randint(6, 60)
            d = Fr(V * 1000, l * b)
            if d.denominator == 1 and 5 <= d <= 60: break
        return dict(t=f"A tank is {l} cm long and {b} cm wide. It holds {V} {LITRE} of water. How deep is the water, in cm?", ans=int(d))
    if kind == "litres":
        while True:
            l, b, d = rng.choice([40, 50, 60, 80]), rng.choice([25, 30, 40, 50]), rng.randint(8, 40)
            if (l * b * d) % 1000 == 0: break
        return dict(t=f"A tank has a base {l} cm by {b} cm. The water in it is {d} cm deep. How many {LITRE} of water are in the tank?", ans=l * b * d // 1000)
    if kind == "half":
        while True:
            l, b, h = rng.choice([40, 60, 90]), rng.choice([25, 30, 40, 50]), rng.choice([20, 30, 40])
            if (l * b * h) % 2000 == 0: break
        return dict(t=f"A tank {l} cm long, {b} cm wide and {h} cm high is half full of water. How many {LITRE} of water are in it?", ans=l * b * h // 2000)
    if kind == "pour":
        while True:
            l, b, V = rng.choice([40, 50, 60]), rng.choice([25, 30, 50]), rng.randint(6, 40)
            d = Fr(V * 1000, l * b)
            if d.denominator == 1 and 4 <= d <= 40: break
        return dict(t=f"{V} {LITRE} of water is poured into an empty tank with a base {l} cm by {b} cm. How high does the water reach, in cm?", ans=int(d))
    if kind == "full":
        while True:
            A, q = rng.choice([400, 500, 600, 800]), rng.choice([(3, 4), (2, 3), (4, 5), (1, 2)])
            V = rng.randint(6, 40)
            h = Fr(V * 1000, A) / Fr(*q)
            if h.denominator == 1 and 10 <= h <= 80: break
        return dict(t=f"A tank has a base area of {A} cm². It is {fh(*q)} full with {V} {LITRE} of water. How high is the tank in cm?", ans=int(h))
    e = rng.choice([20, 30, 40, 50])
    return dict(t=f"A cube-shaped tank has an edge of {e} cm. How many {LITRE} of water does it hold when it is full?", ans=e ** 3 // 1000)

def tank_solve(t):
    t = ptxt(t)
    nums = lambda s: [Fr(x) for x in re.findall(rf"\d+{FSL}\d+|\d+", s)]
    if "cube-shaped" in t:
        e = int(re.search(r"edge of (\d+) cm", t).group(1)); return e ** 3 // 1000
    if "How deep" in t:
        l, b, V = map(int, re.search(r"(\d+) cm long and (\d+) cm wide. It holds (\d+) ", t).groups()); return V * 1000 // (l * b)
    if "How many" in t and "half full" in t:
        l, b, h = map(int, re.search(r"tank (\d+) cm long, (\d+) cm wide and (\d+) cm high", t).groups()); return l * b * h // 2000
    if "How many" in t:
        l, b, d = map(int, re.search(r"base (\d+) cm by (\d+) cm. The water in it is (\d+) cm", t).groups()); return l * b * d // 1000
    if "poured" in t:
        V, l, b = map(int, re.search(r"(\d+) ℓ? ?of water is poured into an empty tank with a base (\d+) cm by (\d+) cm", t.replace("ℓ", "ℓ")).groups()); return V * 1000 // (l * b)
    m = re.search(rf"base area of (\d+) cm². It is (\d+){FSL}(\d+) full with (\d+) ", t)
    A, p, q, V = int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4))
    return int(Fr(V * 1000, A) / Fr(p, q))

def page26():
    rng = random.Random(8626)
    kinds = ["depth", "litres", "half", "pour", "full", "cube"]
    for _ in range(500):
        its = [tank_item(rng, k) for k in kinds]; rng.shuffle(its)
        ans = [it["ans"] for it in its]
        if not distinct(ans) or max(ans) > 130: continue
        pool = set()
        for it in its:
            a = it["ans"]
            pool |= {a * 10, a // 10 if a % 10 == 0 else a + 1, a + 5, a - 5, a * 2, a + 10, a - 1}
        pool = sorted(p for p in pool if p not in ans and 1 <= p <= 130)
        res = make_table(26, ans, rng, 1, 130, pool=pool, n_decoy=3)
        if res: word, table = res; break
    cards = [qcard(i + 1, f'<p>{it["t"]}</p>', abx("w3")) for i, it in enumerate(its)]
    P = code_page(26, 8626, "Tank Stories", 2, "Volume of water in a tank: litres and cm³", STRAND_AV,
        "2.3 (height from volume and base area); Primary 6 Foundation Area and Volume 2.2 and 2.3 (liquid in a tank; litres and cm³)", ["VO2.3", "PF.VO"], "Code-breaker (tanks)",
        ["1 ℓ = 1000 cm³.", "Work out each answer.", "Write it in the box. Use the code table."],
        cards, ans, table, word, 1, 130, "; ".join(f"{i+1}) {a}" for i, a in enumerate(ans)),
        "Six tank stories that need litres changed to cm³ or back: the depth of water, the litres in a tank, half a tank, the height reached by water poured in, the height of a tank that is part full, and a full cube-shaped tank. The decoy numbers are what a pupil gets by forgetting to change litres to cm³ (an answer ten times or a thousand times too big or small), by forgetting the fraction, or by using one edge instead of the base area. The relationship 1 litre = 1000 cm³ is printed on the page. A box left blank gives no letter and the check cannot see it.", ncols=2)
    solved = [tank_solve(it["t"]) for it in its]
    P.v("V1 independent solver reads each printed tank story and finds the answer: equals the key", solved == ans, solved)
    P.v("V7 every answer is a whole number of at most 130", all(1 <= a <= 130 for a in ans))
    return P

PAGES = [page21, page22, page23, page24, page25, page26]
