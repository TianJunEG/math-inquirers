"""Part C: circles. P6-17 Round and Round, P6-18 Circle Areas, P6-19 Half and Quarter, P6-20 Curves and Corners."""
import random, re, math, itertools
from fractions import Fraction as Fr
from math import gcd
from .common import *
from .kit import *
from .kit6 import *
from . import figs as F

PI22 = Fr(22, 7)
PI314 = Fr(314, 100)

# =============================================================================== P6-17 Round and Round  (AV1.1 circumference, π = 22/7, code)
def rr_items(rng):
    ms = rng.sample(range(1, 11), 6)
    kinds = ["fig_d", "fig_r", "fig_d", "story_d", "story_r", "story_d"]
    rng.shuffle(kinds)
    items = []
    for m, k in zip(ms, kinds):
        d = 7 * m
        if k == "fig_r" and d % 2: k = "fig_d"
        if k == "story_r" and d % 2: k = "story_d"
        items.append(dict(m=m, d=d, k=k, ans=Fr(22 * m)))
    names = [("round clock", "its edge"), ("round table", "its edge"), ("round mat", "its edge"), ("round pond", "its edge")]
    for it in items:
        ctx = rng.choice([("A round clock", "How long is its edge, in cm?", "cm"), ("A round mat", "How long is the edge of the mat, in cm?", "cm"), ("A circular pond", "How far is it round the pond, in m?", "m"), ("A wheel", "How far does it roll in one turn, in cm?", "cm")])
        it["ctx"] = ctx
    return items

def rr_card(i, it):
    d = it["d"]
    if it["k"] == "fig_d":
        return qcard(i + 1, f'<div class="figrow">{F.circle_fig(d, "d")}<p>Find the circumference.</p></div>', f'{abx("w4")}{unit("cm")}')
    if it["k"] == "fig_r":
        return qcard(i + 1, f'<div class="figrow">{F.circle_fig(d // 2, "r")}<p>Find the circumference.</p></div>', f'{abx("w4")}{unit("cm")}')
    a, q, u = it["ctx"]
    if it["k"] == "story_d":
        t = f'{a} has a diameter of {d} {u}. {q}'
    else:
        t = f'{a} has a radius of {d // 2} {u}. {q}'
    return qcard(i + 1, f'<p>{t}</p>', f'{abx("w4")}{unit(u)}')

def rr_solve(card):
    if "<svg" in card:
        lab = F.read_fig(card)["labels"][0]
        kind, v = lab[0], F.num_of(lab)
    else:
        m = re.search(r"(diameter|radius) of (\d+)", ptxt(card)); kind = "d" if m.group(1) == "diameter" else "r"; v = Fr(int(m.group(2)))
    d = v if kind == "d" else 2 * v
    return PI22 * d

def page17():
    rng = random.Random(7717)
    for _ in range(300):
        its = rr_items(rng)
        if len({it["m"] for it in its}) < 6: continue
        ans = [int(it["ans"]) for it in its]
        if not distinct(ans): continue
        pool = set()
        for it in its:
            d = it["d"]
            for w in (PI22 * (d // 2) ** 2 if d % 2 == 0 else None, PI22 * d / 2, Fr(d), 2 * d, PI22 * d * d // 1 if False else None, PI22 * d + d):
                if w and w.denominator == 1 and int(w) not in ans and 1 <= w <= 400: pool.add(int(w))
        pool = sorted(pool)
        res = make_table(17, ans, rng, 1, 400, pool=pool, n_decoy=3)
        if res: word, table = res; break
    cards = [rr_card(i, it) for i, it in enumerate(its)]
    P = code_page(17, 7717, "Round and Round", 1, "Circles: circumference", STRAND_AV,
        "1.1 (area and circumference of a circle)", ["AV1.1"], "Code-breaker (circumference)",
        [f"Take {PIP} as 22/7.", "Find the distance round each circle.", "Write the answer in the box. Use the code table."],
        cards, ans, table, word, 1, 400, "; ".join(f"{i+1}) {a} cm" if it["ctx"][2] == "cm" or "fig" in it["k"] else f"{i+1}) {a} m" for i, (it, a) in enumerate(zip(its, ans))),
        f"Six circles: three drawn, with the diameter or the radius marked, and three stories. Every diameter is a multiple of 7, so with π as 22/7 every answer is a whole number. The pupil has to use the diameter or double the radius. The decoy numbers are what a pupil gets by finding the area, by using the radius instead of the diameter, or by halving. A box left blank gives no letter and the check cannot see it.", ncols=2)
    solved = [int(rr_solve(c)) for c in cards]
    P.v("V1 independent solver reads each printed circle label or story (radius or diameter) and finds the circumference: equals the key", solved == ans, solved)
    P.v("V7 every diameter is a multiple of 7 and every answer a whole number of at most 400", all(it["d"] % 7 == 0 for it in its) and max(ans) <= 400)
    return P

# =============================================================================== P6-18 Circle Areas  (AV1.1 area, π = 3.14, code with decimal answers)
def ca_items(rng):
    rs = rng.sample(range(2, 11), 6)
    kinds = ["fig_r", "fig_d", "story_r", "story_d", "circ", "story_r"]
    rng.shuffle(kinds); items = []
    for r, k in zip(rs, kinds):
        if k in ("fig_d", "story_d") and r < 3: r = 3
        items.append(dict(r=r, k=k, ans=PI314 * r * r))
    return items

def ca_card(i, it, rng):
    r = it["r"]
    if it["k"] == "fig_r": return qcard(i + 1, f'<div class="figrow">{F.circle_fig(r, "r")}<p>Find the area.</p></div>', f'{abx("w4")}{unit("cm²")}')
    if it["k"] == "fig_d": return qcard(i + 1, f'<div class="figrow">{F.circle_fig(2 * r, "d")}<p>Find the area.</p></div>', f'{abx("w4")}{unit("cm²")}')
    if it["k"] == "story_r": return qcard(i + 1, f'<p>A round pond has a radius of {r} m. Find the area of the pond.</p>', f'{abx("w4")}{unit("m²")}')
    if it["k"] == "story_d": return qcard(i + 1, f'<p>A round pizza has a diameter of {2 * r} cm. Find its area.</p>', f'{abx("w4")}{unit("cm²")}')
    c = PI314 * 2 * r
    return qcard(i + 1, f'<p>The circumference of a circle is {dec(c)} cm. Find its area.</p>', f'{abx("w4")}{unit("cm²")}')

def ca_solve(card):
    if "<svg" in card:
        lab = F.read_fig(card)["labels"][0]; kind, v = lab[0], F.num_of(lab); r = v if kind == "r" else v / 2
    else:
        t = ptxt(card)
        m = re.search(r"(radius|diameter) of (\d+)", t)
        if m: v = Fr(int(m.group(2))); r = v if m.group(1) == "radius" else v / 2
        else:
            c = Fr(re.search(r"circumference of a circle is (\d+(?:\.\d+)?)", t).group(1)); r = c / (2 * PI314)
    return PI314 * r * r

def page18():
    rng = random.Random(7818)
    dom = [PI314 * k for k in range(1, 401)]
    for _ in range(300):
        its = ca_items(rng)
        ans = [it["ans"] for it in its]
        if not distinct(ans): continue
        pool = set()
        for it in its:
            r = it["r"]
            for k in (r, 2 * r, 4 * r * r, r * r * 2, (2 * r) * (2 * r) // 2 if False else r * r * 2):
                w = PI314 * k
                if w not in ans: pool.add(w)
        pool = sorted(pool)
        res = make_table(18, ans, rng, 1, 1, pool=pool, domain=dom, n_decoy=3)
        if res: word, table = res; break
    cards = [ca_card(i, it, rng) for i, it in enumerate(its)]
    P = code_page(18, 7818, "Circle Areas", 2, "Circles: area", STRAND_AV,
        "1.1 (area and circumference of a circle)", ["AV1.1"], "Code-breaker (area)",
        [f"Take {PIP} as 3.14.", "Find the area of each circle.", "Write the answer in the box. Use the code table."],
        cards, ans, table, word, 1, 1, "; ".join(f"{i+1}) {dec(a)}" for i, a in enumerate(ans)),
        "Six circles: two drawn (one with the radius, one with the diameter), three stories and one two-step item that gives the circumference, so the pupil first finds the radius. Every radius is a whole number from 2 to 10, so every answer has at most two decimal places. The decoy numbers are what a pupil gets by using 2 × π × r (the circumference) or π × r instead of π × r × r, or by squaring the diameter. A box left blank gives no letter and the check cannot see it.",
        domain=dom, fmt=lambda k: dec(k), ncols=2, cols=5)
    solved = [ca_solve(c) for c in cards]
    P.v("V1 independent solver reads the printed circle or story (radius, diameter or circumference) and finds the area: equals the key", solved == ans, [dec(s) for s in solved])
    P.v("V7 every radius is a whole number from 2 to 10 and every answer has at most 2 decimal places", all((a * 100).denominator == 1 for a in ans) and all(2 <= it["r"] <= 10 for it in its))
    return P

# =============================================================================== P6-19 Half and Quarter  (AV1.2, π = 22/7, match)
def semi_area(d): return PI22 * (Fr(d) / 2) ** 2 / 2
def semi_perim(d): return PI22 * Fr(d) / 2 + d
def quarter_area(r): return PI22 * Fr(r) ** 2 / 4
def quarter_perim(r): return PI22 * Fr(r) / 2 + 2 * r

def hq_value_text(v, unit_):
    s = dec(v)
    return f"{s} {unit_}" + ("²" if unit_ == "cm2" else "")

def hq_card_html(v, sq):
    return f'<span class="rt">{dec(v)} cm{"²" if sq else ""}</span>'

def hq_item_html(fig, ask):
    return f'<div class="figrow hq">{fig}<div class="cap">{ask.capitalize()}</div></div>'

def hq_solve_item(item_html, chs):
    r = F.read_fig(item_html); ask = re.search(r'class="cap">(Area|Perimeter)<', item_html).group(1).lower()
    lab = r["labels"][0]; v = F.num_of(lab)
    if r["kind"] == "fig-semi":
        val = semi_area(v) if ask == "area" else semi_perim(v)
    else:
        val = quarter_area(v) if ask == "area" else quarter_perim(v)
    sq = ask == "area"
    for j, c in enumerate(chs):
        t = ptxt(c); m = re.fullmatch(r"(\d+(?:\.\d+)?) cm(²?)", t)
        if m and Fr(m.group(1)) == val and (m.group(2) == "²") == sq: return j
    return -1

def page19():
    rng = random.Random(7919)
    for _ in range(2000):
        combos = []
        for kind in ("semi", "quarter"):
            for size in ((7, 14, 28, 21) if kind == "semi" else (7, 14, 21, 28)):
                for ask in ("area", "perimeter"):
                    if kind == "semi" and size % 7 or (kind == "semi" and size == 21 and False): continue
                    combos.append((kind, size, ask))
        pick = rng.sample(combos, 6)
        if sum(1 for c in pick if c[0] == "semi") != 3 or sum(1 for c in pick if c[2] == "area") not in (3,): continue
        def val(c):
            kind, size, ask = c
            return (semi_area if ask == "area" else semi_perim)(size) if kind == "semi" else (quarter_area if ask == "area" else quarter_perim)(size)
        vals = [(val(c), c[2] == "area") for c in pick]
        if len({v for v, _ in vals}) < 6 or any(v > 700 for v, _ in vals): continue
        # decoys: the right number with the wrong unit, and an arc length without the straight edges
        k0 = next(i for i, c in enumerate(pick) if c[2] == "perimeter")
        dec1 = (vals[k0][0], True)
        k1 = next(i for i, c in enumerate(pick) if c[0] == "semi" and c[2] == "perimeter")
        d1 = PI22 * pick[k1][1] / 2
        dec2 = (d1, False)
        allv = vals + [dec1, dec2]
        if len(set(allv)) < 8: continue
        break
    order = list(range(8)); rng.shuffle(order)
    card_html = [hq_card_html(*allv[j]) for j in order]
    right = [order.index(i) for i in range(6)]
    items = []
    for (kind, size, ask) in pick:
        fig = F.semicircle_fig(size) if kind == "semi" else F.quarter_fig(size)
        items.append(hq_item_html(fig, ask))
    P = match_page(19, 7919, "Half and Quarter", 2, "Semicircles and quarter circles: area and perimeter", STRAND_AV,
        "1.2 (area and perimeter of a semicircle and a quarter circle)", ["AV1.2"], "Matching (areas and perimeters)",
        [f"Take {PIP} as 22/7.", "Find the area or the perimeter of each shape, as the word says.", "Write the card letter in the box. Use each card once. Two cards are not used."],
        rng, items, card_html, right, hq_solve_item,
        "Three semicircles and three quarter circles, three asking for the area and three for the perimeter, with sizes that are multiples of 7 so that every answer is exact. Two cards are decoys: a card with the number of a perimeter but the unit cm², and the length of the curved edge alone. The perimeter of a semicircle or quarter circle includes its straight edges. The letters of the matching cards, read in the order of the items, spell the word. Every way of giving each item a different card, and every single changed letter, was tested against a very large word list: none spells another word. A box left blank gives no letter and the check cannot see it.",
        item_cols=2, card_cols=4)
    return P

# =============================================================================== P6-20 Curves and Corners  (AV1.3, π = 22/7, order)
def cc_area(kind, p):
    if kind == "rsemi": L, W = p; return L * W + PI22 * (Fr(W) / 2) ** 2 / 2
    if kind == "ssemi": s = p[0]; return s * s + PI22 * (Fr(s) / 2) ** 2 / 2
    s = p[0]; return s * s - PI22 * s * s / 4

def cc_read(card):
    r = F.read_fig(card)
    nums = {k: F.num_of(v) for k, v in r["pos"].items()}
    kind = r["kind"]
    if kind == "fig-rsemi": return cc_area("rsemi", (nums["top"], nums["left"]))
    if kind == "fig-ssemi": return cc_area("ssemi", (nums["top"],))
    if kind == "fig-sqq": return cc_area("sqq", (nums["top"],))
    raise ValueError(kind)

def page20():
    rng = random.Random(8020)
    for _ in range(3000):
        figsel = []
        for L, W in rng.sample([(L, W) for W in (14, 28) for L in (16, 18, 20, 21, 22, 24, 26, 28, 30, 35, 40) if L > W - 1], 2): figsel.append(("rsemi", (L, W)))
        for s in rng.sample((7, 14, 21, 28), 2): figsel.append(("ssemi", (s,)))
        for s in rng.sample((7, 14, 21, 28), 2): figsel.append(("sqq", (s,)))
        areas = [cc_area(k, p) for k, p in figsel]
        if len(set(areas)) < 6 or min(abs(a - b) for a, b in itertools.combinations(areas, 2)) < 6: continue
        break
    cards = []
    for i, (k, p) in enumerate(figsel):
        if k == "rsemi": cards.append(f'<div class="fig">{F.rect_semi_fig(*p)}</div>')
        elif k == "ssemi": cards.append(f'<div class="fig">{F.sq_semi_fig(*p)}</div>')
        else: cards.append(f'<div class="fig">{F.sq_minus_quarter_fig(p[0], str(i))}</div>')
    order_idx = sorted(range(6), key=lambda j: areas[j])
    P = order_page(20, 8020, "Curves and Corners", 2, "Composite figures with semicircles and quarter circles", STRAND_AV,
        "1.3 (area and perimeter of composite figures), 1.2 (area and perimeter of a semicircle and a quarter circle)", ["AV1.3", "AV1.2"], "Ordering (areas of composite figures)",
        [f"Take {PIP} as 22/7.", "Find the area of each figure. For a hatched figure, find the hatched part.", "Put the areas in order, smallest first. Write the letters."],
        rng, cards, order_idx, cc_read,
        "Six figures: a rectangle with a semicircle on one end, a square with a semicircle on one side, and a square with a quarter circle cut away (the hatched part). All sizes are chosen so that the areas are exact. The areas of the six figures are all different and differ by at least 6. The letters, read from the smallest area to the greatest, spell the word; every wrong order was tested against a very large word list and none spells a word. A box left blank gives no letter and the check cannot see it.",
        ncols=2, lead="Write the letters in order, smallest area first.", direction="smallest area first",
        card_text=lambda ci: f"{dec(areas[ci])} cm² ({ {'rsemi': 'rectangle and semicircle', 'ssemi': 'square and semicircle', 'sqq': 'square less quarter circle'}[figsel[ci][0]] } {'x'.join(str(x) for x in figsel[ci][1])})")
    return P

PAGES = [page17, page18, page19, page20]
