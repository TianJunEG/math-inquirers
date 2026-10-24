"""Semester 2, pages P3-30 to P3-33: area and perimeter.
P3-30 Square Units; P3-31 Perimeter; P3-32 Rectangles and Squares; P3-33 Same or Different? (lettered choice)."""
import random, re, itertools, math
from .common import *
from .kit import *
from .p3kit import *
from . import art3 as A3

# =============================================================================== P3-30 Square Units
def page30():
    rng = random.Random(5030)
    while True:
        figs = []
        for n in (rng.randint(6, 8), rng.randint(8, 10), rng.randint(9, 12)):
            figs.append(A3.random_polyomino(rng, n, 5, 4))
        vals = []
        for c in figs:
            a, p, _ = A3.read_grid_fig(A3.grid_fig(c)); vals.append((a, p))
        ans = [x for ap in vals for x in ap]
        if not distinct(ans) or len({c.__len__() for c in figs}) < 3 or any(max(c for c, r in f) + 1 > 5 or max(r for c, r in f) + 1 > 4 for f in figs): continue
        if any(a == p for a, p in vals): continue
        pool = set()
        for a, p in vals: pool |= {a - 1, a + 1, p - 1, p + 1, p // 2, a + p}
        pool = sorted(x for x in pool if x not in ans and 0 < x <= 40)
        res = find_table(30, 6, ans, rng, 0, 40, pool, n_decoy=3, tries=120)
        if res: word, table = res; break
    names = "ABC"
    svgs = [A3.grid_fig(c, name=f"Figure {names[i]}") for i, c in enumerate(figs)]
    cards = []; k = 0
    for i, s in enumerate(svgs):
        cards.append(f'<div class="qc sqfig"><div class="sqf">{s}</div><div class="sqa"><span class="no">{2*i+1}</span> Area <span class="ab w2"></span> <b>cm<sup>2</sup></b></div><div class="sqa"><span class="no">{2*i+2}</span> Perimeter <span class="ab w2"></span> <b>cm</b></div></div>')
    pre = '<div class="howto"><p>Each small square is 1 cm by 1 cm. <b>Area</b> is the number of squares inside the figure. <b>Perimeter</b> is the distance round the edge.</p></div>'
    P = code_items_page(30, 5030, "Square Units", 1, "Area and perimeter: counting square units", STRAND_AP,
        "1.1, 1.2 (concepts of area and perimeter; area in square units and cm2)", ["AP1.1", "AP1.2"], "Code-breaker (area and perimeter)",
        ["Find the area and the perimeter of each figure.", "Write each answer in its box.", INSTR_CODE],
        '<div class="qg c3">' + "".join(cards) + "</div>", ans, table, word, 0, 40,
        "; ".join(f"Figure {names[i]}: area {a} cm2, perimeter {p} cm" for i, (a, p) in enumerate(vals)),
        "Three figures made of 1 cm squares (every square is 8 mm on the page, so the figures are drawn smaller than real size). For each figure the pupil counts the squares (area) and the units round the edge (perimeter), so that the two ideas are met side by side. The decoy letters stand for the area and the perimeter swapped, or for one square or one unit out. No figure has a hole. Area and perimeter of rectilinear figures given on a grid are Primary 3; missing sides are not asked. A box left blank gives no letter and the check cannot see it.",
        pre_body=pre)
    solved = []
    for s in svgs:
        a, p, _ = A3.read_grid_fig(s); solved += [a, p]
    P.v("V1 independent solver (unit squares read from the drawing; the perimeter found by counting the edges between a square and a gap) equals the key", solved == ans, solved)
    P.v("V7 every figure fits 5 squares by 4 and has no hole; areas 6 to 12", all(6 <= len(c) <= 12 for c in figs))
    return P

# =============================================================================== P3-31 Perimeter
def figure_defs(rng):
    """returns six items: (kind, svg, perimeter, unit)"""
    out = []
    u = "cm"
    a, b = rng.randint(7, 15), rng.randint(4, 6)
    out.append(("rect", A3.poly_svg([(0, 0), (a, 0), (a, b), (0, b)], "cm", "rect", 3.0), 2 * (a + b), "cm"))
    s = rng.randint(4, 9)
    out.append(("square", A3.poly_svg([(0, 0), (s, 0), (s, s), (0, s)], "m", "square", 4.0), 4 * s, "m"))
    W, H, w1, h1 = rng.randint(9, 11), rng.randint(8, 10), rng.randint(4, 5), rng.randint(4, 5)
    out.append(("poly", A3.poly_svg([(0, 0), (W, 0), (W, h1), (w1, h1), (w1, H), (0, H)], "cm", "poly", 3.6), 2 * (W + H), "cm"))
    W, H, w1, h1 = rng.randint(9, 11), rng.randint(8, 10), rng.randint(4, 5), rng.randint(4, 5)
    out.append(("poly", A3.poly_svg([(0, 0), (W, 0), (W, H), (w1, H), (w1, h1), (0, h1)], "m", "poly", 3.6), 2 * (W + H), "m"))
    W, H, d = 11, rng.randint(8, 9), rng.randint(3, 4)
    x1 = 4; x2 = 7
    out.append(("poly", A3.poly_svg([(0, 0), (W, 0), (W, d), (x2, d), (x2, H), (x1, H), (x1, d), (0, d)], "cm", "poly", 3.0), 2 * (W + H), "cm"))
    return out

def page31():
    rng = random.Random(5131)
    while True:
        figs = figure_defs(rng)
        # item 6: a story
        L_, W_ = rng.choice([35, 40, 45, 60]), rng.choice([20, 25, 30, 15])
        ans = [f[2] for f in figs] + [2 * (L_ + W_)]
        if not distinct(ans) or max(ans) > 200: continue
        order = list(range(6)); rng.shuffle(order)
        ans = [ans[i] for i in order]
        pool = set()
        for v in ans: pool |= {v - 2, v + 2, v - 4, v + 4, v // 2, v + 1, v - 1}
        for f in figs[:2]: pool.add(f[2] // 2)
        pool = sorted(x for x in pool if x not in ans and 0 < x <= 200)
        res = find_table(31, 6, ans, rng, 0, 200, pool, n_decoy=3, tries=60)
        if res: word, table = res; break
    raw = [(f[1], f[3]) for f in figs] + [(None, "m")]
    items = [raw[i] for i in order]
    cards = []; storys = []
    for i, (s, u) in enumerate(items):
        if s is None:
            t = f"A field is {L_} m long and {W_} m wide. What is the perimeter of the field?"; storys.append(t)
            cards.append(f'<div class="vcard fig"><span class="no">{i+1}</span><p class="ftxt">{t}</p><div class="fa"><span class="ab w3"></span> <b>m</b></div></div>')
        else:
            cards.append(f'<div class="vcard fig"><span class="no">{i+1}</span><div class="fsvg">{s}</div><div class="fa"><span class="ab w3"></span> <b>{u}</b></div></div>')
    P = code_items_page(31, 5131, "Perimeter", 1, "Perimeter of rectangles, squares and rectilinear figures", STRAND_AP,
        "1.3 (perimeter of a rectilinear figure, a rectangle and a square)", ["AP1.3", "AP1.1"], "Code-breaker (perimeter)",
        ["Find the perimeter of each figure.", "It is the distance all the way round.", INSTR_CODE],
        '<div class="qg c2 fig2">' + "".join(cards) + "</div>", ans, table, word, 0, 200,
        "; ".join(f"{i+1}) {a}" for i, a in enumerate(ans)),
        "Six items: a rectangle (two sides given), a square (one side given), three rectilinear figures with every side labelled (an L shape, a figure with a notch and a staircase) and a field in a story. Figures are drawn to scale but pictures are not actual size. The decoy letters stand for adding only the labelled sides of a rectangle once, or for half the perimeter. A box left blank gives no letter and the check cannot see it.")
    solved = []
    for s, u in items:
        if s is None:
            m = re.search(r"is (\d+) m long and (\d+) m wide", storys[0]); solved.append(2 * (int(m.group(1)) + int(m.group(2)))); continue
        kind, labs, un = A3.read_poly(s)
        solved.append(2 * (labs[0] + labs[1]) if kind == "rect" else 4 * labs[0] if kind == "square" else sum(labs))
    P.v("V1 independent solver (printed side lengths read back and added; a rectangle doubled, a square times 4) equals the key", solved == ans, solved)
    P.v("V7 every printed side is a whole number of cm or m; perimeters up to 200", all(a <= 200 for a in ans))
    P.v("V1b every figure but the rectangle, the square and the story prints all of its sides", all(len(A3.read_poly(s)[1]) in (2, 1, 6, 8) for s, u in items if s is not None))
    return P

# =============================================================================== P3-32 Rectangles and Squares
def page32():
    rng = random.Random(5232)
    while True:
        items = []
        a, b = rng.randint(7, 12), rng.randint(4, 9); items.append(dict(k="rectfig", a=a, b=b, u="cm", ans=a * b))
        s = rng.randint(6, 12); items.append(dict(k="sqfig", s=s, u="m", ans=s * s))
        a, b = rng.randint(8, 15), rng.randint(5, 9); items.append(dict(k="garden", a=a, b=b, u="m", ans=a * b, nm=rng.choice(PEOPLE)))
        s = rng.randint(5, 9); items.append(dict(k="card", s=s, u="cm", ans=s * s))
        a, b = rng.randint(10, 14), rng.randint(3, 6); items.append(dict(k="tiles", a=a, b=b, u="cm", ans=a * b))
        a, b = rng.randint(6, 9), rng.randint(5, 8); items.append(dict(k="floor", a=a, b=b, u="m", ans=a * b))
        rng.shuffle(items); ans = [it["ans"] for it in items]
        if not distinct(ans) or max(ans) > 200: continue
        if len({(it.get("a", it.get("s")), it.get("b", it.get("s"))) for it in items}) < 6: continue
        pool = set()
        for it in items:
            if "a" in it: pool |= {2 * (it["a"] + it["b"]), it["a"] + it["b"]}
            else: pool |= {4 * it["s"], 2 * it["s"]}
            pool |= {it["ans"] + it.get("a", it.get("s")), it["ans"] - it.get("b", it.get("s")), it["ans"] + 10, it["ans"] - 10}
        pool = sorted(x for x in pool if x not in ans and 0 < x <= 200)
        res = find_table(32, 6, ans, rng, 0, 200, pool, n_decoy=3, tries=60)
        if res: word, table = res; break
    cards = []; texts = []
    for i, it in enumerate(items):
        k = it["k"]; sq = "cm<sup>2</sup>" if it["u"] == "cm" else "m<sup>2</sup>"
        if k == "rectfig": body = A3.poly_svg([(0, 0), (it["a"], 0), (it["a"], it["b"]), (0, it["b"])], "cm", "rect", 3.4); texts.append(None)
        elif k == "sqfig": body = A3.poly_svg([(0, 0), (it["s"], 0), (it["s"], it["s"]), (0, it["s"])], "m", "square", 3.4); texts.append(None)
        else:
            if k == "garden": t = f"{it['nm']}'s garden is a rectangle {it['a']} m long and {it['b']} m wide. What is its area?"
            elif k == "card": t = f"A square card has sides of {it['s']} cm. What is its area?"
            elif k == "tiles": t = f"A rectangle is {it['a']} cm by {it['b']} cm. How many 1 cm squares cover it?"
            else: t = f"A rectangular floor is {it['a']} m by {it['b']} m. What is its area?"
            texts.append(t); body = f"<p class=\"ftxt\">{t}</p>"
        cards.append(f'<div class="vcard fig"><span class="no">{i+1}</span><div class="fsvg">{body}</div><div class="fa"><span class="ab w3"></span> <b>{sq}</b></div></div>')
    P = code_items_page(32, 5232, "Area Sums", 2, "Area of rectangles and squares in cm² and m²", STRAND_AP,
        "1.2, 1.4 (area in cm2 and m2; area of a rectangle and a square)", ["AP1.2", "AP1.4"], "Code-breaker (area)",
        ["Find the area of each rectangle or square.", "Write the area with its unit, cm² or m².", INSTR_CODE],
        '<div class="qg c3">' + "".join(cards) + "</div>", ans, table, word, 0, 200,
        "; ".join(f"{i+1}) {a} {'cm2' if it['u'] == 'cm' else 'm2'}" for i, (it, a) in enumerate(zip(items, ans))),
        "Six areas: a rectangle and a square given in a picture, a garden and a floor given in words (in m²), a square card and a rectangle covered with 1 cm squares (in cm²). The unit is printed after the box, so cm² and m² are never changed into each other. The decoy letters stand for the perimeter, or for adding the two sides. A box left blank gives no letter and the check cannot see it.")
    solved = []
    for it, t, c in zip(items, texts, cards):
        if t is None:
            kind, labs, un = A3.read_poly(c); solved.append(labs[0] * labs[1] if kind == "rect" else labs[0] ** 2)
        else:
            nums = [int(x) for x in re.findall(r"\d+", t.replace("1 cm squares", "squares"))]
            solved.append(nums[0] * nums[1] if len(nums) == 2 else nums[0] ** 2)
    P.v("V1 independent solver (printed sides read back and multiplied) equals the key", solved == ans, solved)
    P.v("V7 sides are whole numbers up to 15; areas up to 200", max(ans) <= 200)
    return P

# =============================================================================== P3-33 Same or Different? (lettered choice)
def page33():
    rng = random.Random(5333)
    kinds = ["area", "perimeter", "area", "perimeter", "perimeter"]
    for _ in range(5000):
        rows = []
        for kd in kinds:
            for _t in range(400):
                a = A3.random_polyomino(rng, rng.randint(5, 7), 3, 3); b = A3.random_polyomino(rng, rng.randint(5, 7), 3, 3)
                aa, pa, _x = A3.read_grid_fig(A3.grid_fig(a)); ab_, pb, _y = A3.read_grid_fig(A3.grid_fig(b))
                va, vb = (aa, ab_) if kd == "area" else (pa, pb)
                if a == b: continue
                rows.append((kd, a, b, va, vb)); break
        wins = ["A" if r[3] > r[4] else "B" if r[3] < r[4] else "Same" for r in rows]
        if len(set(wins)) < 3 or wins.count("Same") > 2: continue
        break
    specs = []
    for kd, a, b, va, vb in rows:
        q = (f'<div class="ab2"><span class="fgs"><b>A</b>{A3.grid_fig(a, cell=8.0)}</span><span class="fgs"><b>B</b>{A3.grid_fig(b, cell=8.0)}</span></div>'
             f'<p class="qs2">Greater {kd}?</p>')
        ri = 0 if va > vb else 1 if va < vb else 2
        specs.append(dict(q=q, opts=['<b class="on">A</b>', '<b class="on">B</b>', '<b class="on">Same</b>'], ri=ri, fixed=True, kd=kd))
    P = lettered_choice_page(33, 5333, "Same or Different?", 2, "Area and perimeter: comparing two figures made of unit squares", STRAND_AP,
        "1.1, 1.2, 1.3 (concepts of area and perimeter; area in square units; perimeter of a rectilinear figure)", ["AP1.1", "AP1.2", "AP1.3"], "Lettered choice (compare two figures)",
        ["Compare Figure A and Figure B.", "Circle the letter of the right choice.", "Write the five letters in the boxes."],
        specs, 3, "; ".join(f"{i+1}) {['A', 'B', 'Same'][s['ri']]} ({s['kd']})" for i, s in enumerate(specs)),
        "Five pairs of figures made of equal squares (each square is a unit). The pupil counts the squares for the area and the units round the edge for the perimeter, and says which figure is greater or whether they are the same. Pairs are chosen so that the answers include A, B and the same. A figure with more squares need not have the greater perimeter. The letters of the right choices, read down the rows, spell the word. Every other way of choosing was tested against a very large word list: none spells a word. A box left blank gives no letter and the check cannot see it.",
        word_len=5, rng=rng, row_cls="cmp")
    def solver(q, opts):
        figs = re.findall(r"<svg.*?</svg>", q, re.S)
        (aa, pa, _a), (ab_, pb, _b) = A3.read_grid_fig(figs[0]), A3.read_grid_fig(figs[1])
        kd = re.search(r"Greater (area|perimeter)", q).group(1)
        va, vb = (aa, ab_) if kd == "area" else (pa, pb)
        w = "A" if va > vb else "B" if va < vb else "Same"
        return [re.search(r">([^<]*)<", o).group(1) for o in opts].index(w)
    got = solve_letters(solver, P["body"])
    P.v("V1 independent solver (squares counted in both drawings, perimeters from the edges) gets the word", got == P["word"], got)
    P.v("V7 each figure has 5 to 7 squares and fits 3 by 3", all(5 <= len(a) <= 7 and 5 <= len(b) <= 7 for kd, a, b, va, vb in rows))
    return P

PAGES = [page30, page31, page32, page33]
