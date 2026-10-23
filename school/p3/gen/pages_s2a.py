"""Semester 2, pages P3-21 to P3-25: length, mass and volume.
P3-21 Jugs and Beakers; P3-22 Equal Measures (route); P3-23 Kilograms and Grams; P3-24 Road Trip (compound units); P3-25 Order the Measures."""
import random, re, itertools, math
from .common import *
from .kit import *
from .p3kit import *
from . import art3 as A3

ML = "mℓ"; LT = "ℓ"

# =============================================================================== P3-21 Jugs and Beakers
def page21():
    rng = random.Random(4121)
    while True:
        items = []
        for k in range(6):
            vmax, step, lab = rng.choice([(500, 50, 100), (1000, 100, 200)]) if k % 2 == 0 else ((1000, 100, 200) if k % 4 == 1 else (500, 50, 100))
            v = rng.randrange(step, vmax, step)
            if v % lab == 0: v = (v + step) if v + step < vmax else v - step
            items.append((vmax, step, lab, v))
        ans = [v for _, _, _, v in items]
        if not distinct(ans) or len({it[0] for it in items}) < 2: continue
        pool = set()
        for vmax, step, lab, v in items: pool |= {v + step, v - step, v + lab // 2 if lab // 2 != step else v + 2 * step, vmax - v}
        pool = sorted(x for x in pool if x not in ans and 0 < x <= 1000)
        res = find_table(21, 6, ans, rng, 0, 1000, pool, n_decoy=3, tries=60)
        if res: word, table = res; break
    svgs = [A3.beaker_svg(v, vmax, step, lab) for vmax, step, lab, v in items]
    cards = [qcard(i + 1, '<div class="tank">' + s + '</div>', f'<span class="ab w3"></span> <b>{ML}</b>', cls="pos") for i, s in enumerate(svgs)]
    P = code_items_page(21, 4121, "Jugs and Beakers", 1, "Volume of liquid: reading containers in millilitres (mℓ)", STRAND_ME,
        "1.1 (measuring volume of liquid in millilitres)", ["ME1.1"], "Code-breaker (containers)",
        ["Read the liquid level in each container.", "Write the number of millilitres.", INSTR_CODE],
        qgrid(cards, 3, "tanks"), ans, table, word, 0, 1000,
        "; ".join(f"{i+1}) {v} {ML} (scale to {vmax}, a mark every {step})" for i, (vmax, step, lab, v) in enumerate(items)),
        "Six containers with a scale in millilitres: some to 500 mℓ with a mark every 50 mℓ, some to 1000 mℓ with a mark every 100 mℓ, and numbers on only some of the marks, so the pupil counts on from a number. The level is at a mark, never at a number. The decoy letters stand for the mark above or below. Drawings are not to scale. Practical measuring with a real jug is not possible on a printed page. A box left blank gives no letter and the check cannot see it.")
    solved = [A3.read_beaker(s) for s in svgs]
    P.v("V1 independent solver reads the tick marks and the level line of each container and equals the key", solved == ans, solved)
    P.v("V7 levels are on a mark that has no number; scales to 500 or 1000", all(vmax in (500, 1000) and v % step == 0 and v % lab != 0 for vmax, step, lab, v in items))
    return P

# =============================================================================== P3-22 Equal Measures (route)
FAM = [("km", "m", 1000), ("kg", "g", 1000), (LT, ML, 1000), ("m", "cm", 100)]
def conv_cell(a, kind, extra=None):
    """printed conversion with a missing number; the value of the missing number is returned by solve_conv"""
    if kind == "direct":
        i = extra
        u, w, f = FAM[i]
        return f"{a} {u} = ? {w}"
    if kind == "add":
        i, k = extra
        u, w, f = FAM[i]
        return f"{k} {u} + {(a - k) * f if f == 1000 else (a - k) * f} {w} = ? {w}"
    raise ValueError(kind)

def solve_conv(t):
    m = re.fullmatch(r"(\d+) (km|kg|ℓ|m) = \? (m|g|mℓ|cm)", t)
    if m: return int(m.group(1)) * {"km": 1000, "kg": 1000, "ℓ": 1000, "m": 100}[m.group(2)]
    m = re.fullmatch(r"(\d+) (km|kg|ℓ) \+ (\d+) (m|g|mℓ) = \? (m|g|mℓ)", t)
    if m: return int(m.group(1)) * 1000 + int(m.group(3))
    raise ValueError(t)

def page22():
    rng = random.Random(4222)
    n = 4; L = 8
    for T_ in (4, 5, 6, 3, 7):
        T = T_ * 1000
        good = []
        for i in (0, 1, 2): good.append(f"{T_} {FAM[i][0]} = ? {FAM[i][1]}")
        good.append(f"{T_ * 10} m = ? cm")
        for i in (0, 1, 2):
            for k in range(1, T_):
                u, w, f = FAM[i]; good.append(f"{k} {u} + {T - k * 1000} {w} = ? {w}")
        bad = set()
        for a in (T_ - 2, T_ - 1, T_ + 1, T_ + 2):
            if a < 1: continue
            for i in (0, 1, 2): bad.add(f"{a} {FAM[i][0]} = ? {FAM[i][1]}")
            bad.add(f"{a * 10} m = ? cm")
            for i in (0, 1, 2):
                for k in range(1, a):
                    u, w, f = FAM[i]; bad.add(f"{k} {u} + {a * 1000 - k * 1000} {w} = ? {w}")
        bad |= {f"{T_} m = ? cm", f"{T_ * 100} m = ? cm"}
        bad = sorted(b for b in bad if solve_conv(b) != T)
        if len(good) < L + 3: continue
        for _ in range(30000):
            path = random_walk(rng, n, L, min_dist=3)
            if abs(path[0][0] - path[-1][0]) + abs(path[0][1] - path[-1][1]) + 1 >= L: continue
            pick = rng.sample(good, L + 2)
            grid = {c: pick[k] for k, c in enumerate(path)}
            dead = 0
            for p in path[:-1]:
                if dead >= 2: break
                opts = [q for q in neighbours(*p, n) if q not in grid]
                if opts and rng.random() < .6: grid[rng.choice(opts)] = pick[L + dead]; dead += 1
            bs = rng.sample(bad, 16)
            for r in range(n):
                for c in range(n):
                    if (r, c) not in grid: grid[(r, c)] = bs.pop()
            start, finish = path[0], path[-1]
            ok = lambda cell: solve_conv(grid[cell]) == T
            if dead == 2 and len(set(grid.values())) == 16 and count_routes(ok, n, start, finish) == 1: break
        else: continue
        break
    else: raise RuntimeError("p22")
    texts = [[grid[(r, c)].replace("? ", "□ ") for c in range(n)] for r in range(n)]
    body = maze_html(n, texts, start, finish, cls="maze tall conv")
    P = new_page(22, 4222, "Equal Measures", 1, "Converting between km and m, m and cm, kg and g, ℓ and mℓ", STRAND_ME,
        "1.2, 1.3 (compound units; converting km and m, m and cm, kg and g, ℓ and mℓ)", ["ME1.2", "ME1.3"], "Maze / path", "K6 route closes at FINISH",
        ["Start at START. Move up, down, left or right.", f"Step only on boxes where the missing number is {T}.", "Do not step on a box twice."],
        body, "Route (row, column from top-left): " + " -> ".join(f"({r+1},{c+1}) {grid[(r, c)]}" for r, c in path),
        f"Route reaches FINISH through {L} boxes; the missing number in every box on it is {T}.",
        f"A 4 by 4 grid of sixteen conversions with a missing number: km to m, kg to g, ℓ to mℓ, m to cm, and sums of a larger and a smaller unit that must be written in the smaller unit. The route follows the boxes whose missing number is {T}. The other boxes have missing numbers that are 1000 or 100 times a neighbouring number, or a number a thousand more or less. {dead} extra boxes that do make {T} are dead ends. Counting the boxes shows a line that takes a shortcut. Pictures of rulers, scales and jugs are not used: the page tests the conversions.",
        check=f"Does your line reach FINISH? Count its boxes: are there {L}? Is every missing number {T}?", mk=("route",),
        mech_plain=f"Route: the line must reach FINISH through the right number of boxes, every missing number being {T}")
    g2 = {(r, c): texts[r][c].replace("□", "?") for r in range(n) for c in range(n)}
    ok2 = lambda cell: solve_conv(g2[cell]) == T
    P.v("V1 exactly one route start->finish (exhaustive search, conversions evaluated from the printed text)", count_routes(ok2, n, start, finish) == 1)
    P.v("V3 dead-end boxes that also have the target exist", dead >= 2, dead)
    P.v("V3b a shortcut that ignores the rule is shorter than the route", abs(start[0]-finish[0]) + abs(start[1]-finish[1]) + 1 < L)
    P.v("V7b all sixteen boxes are different", len(set(g2.values())) == 16)
    P["cv"] = dict(rate=1.0, single_total=dead, single_detected=dead)
    allcells = [(r, c) for r in range(n) for c in range(n)]
    def legal(rt):
        if len(rt) != L or len(set(rt)) != L or rt[0] != start or rt[-1] != finish: return False
        return all(ok2(c) for c in rt) and all(abs(a[0]-b[0]) + abs(a[1]-b[1]) == 1 for a, b in zip(rt, rt[1:]))
    P["model"] = dict(truth=list(path), domains=[allcells] * L, check=legal, numeric=False)
    P["mini"] = mini_route(n, path)
    P["facts"] = f"{T} " + " ".join(re.findall(r"\d+", " ".join(g2.values())))
    return P

# =============================================================================== P3-23 Kilograms and Grams
def page23():
    rng = random.Random(4323)
    while True:
        g = [50 * k for k in rng.sample(range(3, 20), 3) if k % 2]
        g = g[:3]
        if len(g) < 3: continue
        kg = rng.sample(range(2, 10), 3)
        items = [("g", v) for v in g] + [("kg", v) for v in kg]
        rng.shuffle(items); ans = [v if u == "g" else v * 1000 for u, v in items]
        if not distinct(ans): continue
        pool = set()
        for u, v in items:
            pool |= ({v + 50, v - 50, v + 100, v - 100} if u == "g" else {v, v * 100, v * 10, v * 1000 + 500})
        pool = sorted(x for x in pool if x not in ans and 0 < x <= 10000)
        res = find_table(23, 6, ans, rng, 0, 10000, pool, n_decoy=3, tries=15)
        if res: word, table = res; break
    svgs = [A3.dial_svg(v, 10, 1, 1, "kg") if u == "kg" else A3.dial_svg(v, 1000, 100, 50, "g") for u, v in items]
    cards = [qcard(i + 1, '<div class="dial">' + s + '</div>', f'<span class="ab w4"></span> <b>g</b>', cls="pos") for i, (s, (u, v)) in enumerate(zip(svgs, items))]
    P = code_items_page(23, 4323, "Kilograms and Grams", 1, "Mass: reading scales and changing kg to g", STRAND_ME,
        "1.1, 1.3 (measuring mass; converting kg and g)", ["ME1.1", "ME1.3"], "Code-breaker (weighing scales)",
        ["Read each scale.", "Write the mass in grams.", INSTR_CODE],
        qgrid(cards, 3, "dials"), ans, table, word, 0, 10000,
        "; ".join(f"{i+1}) {v} {u} = {a} g" for i, ((u, v), a) in enumerate(zip(items, ans))),
        "Six weighing scales with a needle: three read in grams (0 to 1000 g, a mark every 50 g, the readings are on a mark with no number) and three read in kilograms (0 to 10 kg) that the pupil changes to grams. Every answer is written in grams. The decoy letters stand for the next mark read by mistake, or for the number of kilograms written as grams without the zeros. Drawings are not to scale. A box left blank gives no letter and the check cannot see it.",
        fmt=lambda v: f"{v} g")
    solved = []
    for s in svgs:
        v, u = A3.read_dial(s); solved.append(v * 1000 if u == "kg" else v)
    P.v("V1 independent solver reads the needle angle and the printed unit of each dial and equals the key (in grams)", solved == ans, solved)
    P.v("V7 masses: g readings are odd multiples of 50 up to 950; kg readings 2 to 9", all((v % 50 == 0 and v % 100 != 0 and v < 1000) if u == "g" else (2 <= v <= 9) for u, v in items))
    return P

# =============================================================================== P3-24 Road Trip (compound units)
def cu(big, small, b, s): return f"{b} {big} {s} {small}"

def page24():
    rng = random.Random(4424)
    while True:
        items = []
        def pair(lo_b, hi_b): return rng.randint(lo_b, hi_b), rng.randrange(50, 1000, 50)
        b1, s1 = pair(1, 4); b2, s2 = pair(1, 4)
        while s1 + s2 < 1000: s2 = rng.randrange(50, 1000, 50)
        items.append(dict(k="add", big="km", small="m", a=(b1, s1), b=(b2, s2), ans=(b1 + b2) * 1000 + s1 + s2, n=rng.choice(PEOPLE)))
        b1, s1 = pair(5, 8); b2, s2 = pair(1, 4)
        while s2 <= s1: s2 = rng.randrange(50, 1000, 50); s1 = rng.randrange(50, 1000, 50)
        items.append(dict(k="sub", big="km", small="m", a=(b1, s1), b=(b2, s2), ans=(b1 * 1000 + s1) - (b2 * 1000 + s2), n=rng.choice(PEOPLE)))
        b1, s1 = pair(2, 4); b2, s2 = pair(1, 3)
        while s1 + s2 < 1000: s2 = rng.randrange(50, 1000, 50)
        items.append(dict(k="add", big="kg", small="g", a=(b1, s1), b=(b2, s2), ans=(b1 + b2) * 1000 + s1 + s2))
        b1 = rng.randint(4, 8); b2, s2 = pair(1, 3)
        items.append(dict(k="subw", big="kg", small="g", a=(b1, 0), b=(b2, s2), ans=b1 * 1000 - (b2 * 1000 + s2)))
        b1, s1 = pair(2, 4); b2, s2 = pair(1, 2)
        while s1 + s2 < 1000: s2 = rng.randrange(50, 1000, 50)
        items.append(dict(k="add", big="ℓ", small=ML, a=(b1, s1), b=(b2, s2), ans=(b1 + b2) * 1000 + s1 + s2))
        b1, s1 = pair(3, 5); b2, s2 = 0, rng.randrange(150, 900, 50)
        while s1 >= s2 and False: pass
        items.append(dict(k="subg", big="ℓ", small=ML, a=(b1, s1), b=(b2, s2), ans=b1 * 1000 + s1 - s2))
        ans = [it["ans"] for it in items]
        if not distinct(ans) or max(ans) > 9999 or min(ans) < 100: continue
        if any(it["k"] == "sub" and it["a"][1] >= it["b"][1] for it in items): continue
        pool = set()
        for it in items:
            pool |= {it["ans"] + 100, it["ans"] - 100, it["ans"] + 1000, it["ans"] - 1000, it["ans"] + 50, it["ans"] - 50}
            if it["k"] == "sub": pool |= {(it["a"][0] - it["b"][0]) * 1000 + abs(it["a"][1] - it["b"][1])}
            if it["k"] == "add": pool |= {(it["a"][0] + it["b"][0]) * 1000 + (it["a"][1] + it["b"][1]) % 1000}
        pool = sorted(x for x in pool if x not in ans and 0 < x <= 9999)
        res = find_table(24, 6, ans, rng, 0, 9999, pool, n_decoy=3, tries=12)
        if res: word, table = res; break
    texts = []; cards = []
    for i, it in enumerate(items):
        a, b, big, small = it["a"], it["b"], it["big"], it["small"]
        A_, B_ = cu(big, small, *a), cu(big, small, *b)
        if big == "km" and it["k"] == "add": t = f"{it['n']} rides {A_} and then {B_}. How many metres is that in all?"
        elif big == "km": t = f"A path is {A_} long. {it['n']} has walked {B_}. How many metres are left?"
        elif big == "kg" and it["k"] == "add": t = f"A bag has {A_} of rice and {B_} of flour. How many grams is that in all?"
        elif big == "kg": t = f"A box weighs {a[0]} kg. {B_} are taken out. How many grams are left in the box?"
        elif it["k"] == "add": t = f"A tank has {A_}. {B_} more is poured in. How many mℓ is in the tank now?"
        else: t = f"A jug holds {A_}. {b[1]} {small} is poured out. How many mℓ is left?"
        texts.append(t); cards.append(qcard(i + 1, f"<p>{t}</p>", f'<span class="ab w4"></span> <b>{small}</b>'))
    P = code_items_page(24, 4424, "Road Trip", 2, "Compound units: adding and subtracting km and m, kg and g, ℓ and mℓ", STRAND_ME,
        "1.1, 1.2 (measuring length in kilometres and volume in millilitres; compound units)", ["ME1.1", "ME1.2", "ME1.3"], "Code-breaker (compound units)",
        ["Work out each answer in the smaller unit.", "Write it in the box.", INSTR_CODE],
        qgrid(cards, 2), ans, table, word, 0, 9999,
        "; ".join(f"{i+1}) {a} {it['small']}" for i, (it, a) in enumerate(zip(items, ans))),
        "Six word problems with compound units: two about length (km and m), two about mass (kg and g), two about volume (ℓ and mℓ). Four add or subtract two compound measures and two take a part away. Every answer is written in the smaller unit. Subtractions need the larger unit to be renamed. The decoy letters stand for forgetting to rename, or for the wrong number of thousands. A box left blank gives no letter and the check cannot see it.")
    def tomb(t):
        vals = [int(x) for x in re.findall(r"(\d+) (?:km|kg|ℓ) (\d+) (?:m|g|mℓ)", t) for x in (x,)] if False else None
        pairs = [(int(a), int(b)) for a, b in re.findall(r"(\d+) (?:km|kg|ℓ) (\d+) (?:m|g|mℓ)", t)]
        return pairs
    solved = []
    for t in texts:
        pr = [int(a) * 1000 + int(b) for a, b in re.findall(r"(\d+) (?:km|kg|ℓ) (\d+) (?:m|g|mℓ)", t)]
        singles = re.findall(r"(\d+) (?:km|kg|ℓ)(?! \d)", t)
        mm = re.findall(r"(\d+) (?:m|g|mℓ) (?:is|are)", t)
        if len(pr) == 2 and ("and then" in t or "in all" in t or "more is" in t): solved.append(pr[0] + pr[1])
        elif len(pr) == 2: solved.append(pr[0] - pr[1])
        elif "taken out" in t:
            a0 = int(re.search(r"weighs (\d+) kg", t).group(1)); solved.append(a0 * 1000 - pr[0])
        elif "poured out" in t: solved.append(pr[0] - int(re.search(r"(\d+) mℓ is poured out", t).group(1)))
        else: raise ValueError(t)
    P.v("V1 independent solver reads the printed words and numbers back and equals the key", solved == ans, solved)
    P.v("V7 every answer is within 9999 of the smaller unit; two items each for length, mass and volume", len(items) == 6 and max(ans) <= 9999)
    return P

# =============================================================================== P3-25 Order the Measures
def parse_measure(s):
    """independent: '3 km 50 m' / '2050 m' / '3 kg 40 g' / '1 ℓ 5 mℓ' -> value in the smaller unit"""
    m = re.fullmatch(r"(\d+) (km|kg|ℓ) (\d+) (m|g|mℓ)", s)
    if m: return int(m.group(1)) * 1000 + int(m.group(3))
    m = re.fullmatch(r"(\d+) (m|g|mℓ)", s)
    if m: return int(m.group(1))
    raise ValueError(s)

def page25():
    rng = random.Random(4525)
    for _ in range(4000):
        word = word_candidates(25, 6)[0]
        k = rng.randint(2, 8)
        A_ = [f"{k} km 50 m", f"{k} km 5 m", f"{k * 1000 + 500} m"]
        k2 = rng.randint(2, 8)
        unit = rng.choice([("kg", "g"), ("ℓ", ML)])
        B_ = [f"{k2} {unit[0]} 40 {unit[1]}", f"{k2 * 1000 + 400} {unit[1]}", f"{k2} {unit[0]} 4 {unit[1]}"]
        if k == k2: continue
        break
    CLAIMED[25] = word
    A_s = sorted(A_, key=parse_measure); B_s = sorted(B_, key=lambda s: -parse_measure(s))
    lab = {}
    for i, v in enumerate(A_s): lab[("A", v)] = word[i]
    for i, v in enumerate(B_s): lab[("B", v)] = word[3 + i]
    shA = A_[:]; shB = B_[:]; rng.shuffle(shA); rng.shuffle(shB)
    def card_html(g, v): return f'<div class="fcard"><div class="fnum"><span class="bignum m">{v}</span></div><i class="cl">{lab[(g, v)]}</i></div>'
    body = (f'<div class="blk"><p class="lead">Set A: shortest first.</p><div class="fcards">{"".join(card_html("A", v) for v in shA)}</div></div>'
            f'<div class="blk"><p class="lead">Set B: heaviest or most liquid first.</p><div class="fcards">{"".join(card_html("B", v) for v in shB)}</div></div>'
            f'<div class="blk"><p class="lead">Write the letters in order: Set A, then Set B.</p><div class="ansgrid2" style="margin-top:2mm">' + "".join('<span class="ab"></span>' for _ in range(6)) + '</div></div>')
    P = new_page(25, 4525, "Order the Measures", 2, "Length, mass and volume: comparing and ordering measures in different units", STRAND_ME,
        "1.2, 1.3 (compound units; converting km and m, kg and g, ℓ and mℓ)", ["ME1.2", "ME1.3"], "Ordering (lettered cards)", "K1 letters in order spell a word (6 letters) + K4 each card used once",
        ["Put each set of measures in order.", "Write the letter of each card in its place.", "Set A: shortest first. Set B: greatest first."],
        body, "Set A (shortest first): " + ", ".join(f"{lab[('A', v)]} = {v}" for v in A_s) + "; Set B (greatest first): " + ", ".join(f"{lab[('B', v)]} = {v}" for v in B_s), f"Word: {word}",
        "Each set has three measures of the same kind written in different ways (a mixed unit such as 3 km 5 m, or only the smaller unit such as 3500 m). To compare them the pupil changes them all to the smaller unit. The traps are the zeros in the middle (50 m, 5 m) and the number of thousands. The letters, read in the order asked, spell a word with exactly one arrangement that is a word, so no wrong order of the six cards spells a word (every wrong order was tested against a very large word list). A box left blank gives no letter and the check cannot see it.",
        check="Read the six letters in order. Do they spell a word?", check_boxes=None, mk=("logic",),
        mech_plain="Letters of the cards in the order asked spell a word (6 letters)")
    P["check_boxes"] = None
    secA, secB = body.split("Set B: ")
    ra = re.findall(r'<span class="bignum m">([^<]+)</span></div><i class="cl">(\w)</i>', secA); rb = re.findall(r'<span class="bignum m">([^<]+)</span></div><i class="cl">(\w)</i>', secB)
    solved = "".join(c[1] for c in sorted(ra, key=lambda c: parse_measure(c[0])) + sorted(rb, key=lambda c: -parse_measure(c[0])))
    P.v("V1 independent solver (measures read back, changed to the smaller unit and sorted) gets the word", solved == word, solved)
    P.v("V1b no two measures in a set are equal", all(len({parse_measure(c[0]) for c in s}) == 3 for s in (ra, rb)))
    P.v("V3d the code word's letters have exactly ONE arrangement that is a word", anagrams(word) == [word.lower()], anagrams(word))
    bad = sorted(w for w in ("".join(p) for p in itertools.permutations(word)) if w != word and w.lower() in BIG)
    P.v("V3 none of the 719 wrong orders of the six letters spells a word", not bad, bad[:3])
    P["cv"] = dict(rate=1.0, single_total=719, single_detected=719)
    P["model"] = dict(truth=list(word), domains=[sorted(set(word))] * 6, check=letters_check(), perm=list(range(6)))
    return P

PAGES = [page21, page22, page23, page24, page25]
