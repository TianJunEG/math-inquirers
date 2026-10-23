"""Semester 1, pages P3-15 to P3-20: equivalent fractions, simplest form, missing numbers, ordering unlike fractions, fraction sums, money sums."""
import random, re, itertools, math
from fractions import Fraction
from .common import *
from .kit import *
from .p3kit import *
from . import art3 as A3
from . import art2 as A2

def fr(k, n): return frac_html((k, n))

def fracs_in(h):
    """independent reader: stacked fractions <i>top</i><i>bottom</i> in printed html -> list of (top, bottom)"""
    return [(int(a), int(b)) for a, b in re.findall(r'<span class="fr"><i>(\d+)</i><i>(\d+)</i></span>', h)]

# =============================================================================== P3-15 Equal Fractions (lettered choice)
def page15():
    rng = random.Random(3515)
    figs_n = [2, 3, 4, 5, 6, 8]
    for _ in range(4000):
        rows = []; used = set()
        for i in range(6):
            n = rng.choice(figs_n); k = rng.randint(1, n - 1)
            if math.gcd(k, n) != 1 and rng.random() < .5: continue
            m = rng.choice([2, 3, 4]) if n * 2 <= 12 else 1
            if n * m > 12 or m == 1: continue
            if Fraction(k, n) in used: continue
            used.add(Fraction(k, n)); rows.append((k, n, m))
        if len(rows) < 6: continue
        # shaded value k/n; the right option is k*m / n*m
        rows = rows[:6]
        break
    specs = []; kinds = ["bar", "circle", "bar", "bar", "circle", "bar"]
    for (k, n, m), kd in zip(rows, kinds):
        right = (k * m, n * m)
        wr = set()
        wr |= {(k * m, n * m + 1) if n * m + 1 <= 12 else (k * m, n * m - 1), (k * m + 1, n * m), (k + m, n + m), (k * m, n * (m + 1) if n * (m + 1) <= 12 else n * m - 1), (n * m - k * m, n * m)}
        wr = [w for w in wr if 0 < w[0] < w[1] <= 12 and Fraction(*w) != Fraction(k, n)]
        w2 = rng.sample(sorted(wr), 2)
        fig = A3.frac_fig(kd, n, set(rng.sample(range(n), k)), rng)
        specs.append(dict(q=f'<div class="ffig2">{fig}</div>', opts=[fr(*right), fr(*w2[0]), fr(*w2[1])], val=right))
    P = lettered_choice_page(15, 3515, "Equal Fractions", 1, "Fractions: equivalent fractions", STRAND_FR,
        "1.1 (equivalent fractions)", ["FR1.1"], "Lettered choice (equivalent fractions)",
        ["Each shape has equal parts.", "Circle the letter of the fraction equal to the shaded part.", "Write the six letters in the boxes."],
        specs, 3, "; ".join(f"{i+1}) {r['val'][0]}/{r['val'][1]}" for i, r in enumerate(specs)),
        "Six figures (bars and circles) cut into equal parts with some parts shaded. Each row offers three fractions and only one is equal to the shaded part (the shaded part written with more, smaller parts). The wrong ones are close in look: the same top with one more part, one more shaded part, or the top and bottom each increased by the same number instead of multiplied. The letters of the right fractions, read down the rows, spell the word. Every other way of choosing was tested against a very large word list: none spells a word. A box left blank gives no letter and the check cannot see it.",
        rng=rng, row_cls="fr2")
    def solver(q, opts):
        k_, n_ = A3.read_frac(q)
        vals = [fracs_in(o)[0] for o in opts]
        hits = [i for i, (a, b) in enumerate(vals) if Fraction(a, b) == Fraction(k_, n_)]
        assert len(hits) == 1, (k_, n_, vals)
        return hits[0]
    got = solve_letters(solver, P["body"])
    P.v("V1 independent solver (parts counted in the drawing, fractions compared by value) gets the word", got == P["word"], got)
    P.v("V1b exactly one option in every row equals the shaded part", True)
    P.v("V7 denominators within 12", all(b <= 12 for r in specs for a, b in [r["val"]]))
    return P

# =============================================================================== P3-16 Simplest Form (route)
def page16():
    rng = random.Random(3616)
    n = 4; L = 8
    simple = [(k, d) for d in range(2, 13) for k in range(1, d) if math.gcd(k, d) == 1 and d >= 3]
    notsimple = [(k, d) for d in range(4, 13) for k in range(2, d) if math.gcd(k, d) > 1]
    for _ in range(40000):
        path = random_walk(rng, n, L, min_dist=3)
        if abs(path[0][0] - path[-1][0]) + abs(path[0][1] - path[-1][1]) + 1 >= L: continue
        grid = {}
        pick = rng.sample(simple, L + 2)
        for k, c in enumerate(path): grid[c] = pick[k]
        dead = 0
        for p in path[:-1]:
            if dead >= 2: break
            opts = [q for q in neighbours(*p, n) if q not in grid]
            if opts and rng.random() < .6: grid[rng.choice(opts)] = pick[L + dead]; dead += 1
        ns = rng.sample(notsimple, 16)
        for r in range(n):
            for c in range(n):
                if (r, c) not in grid: grid[(r, c)] = ns.pop()
        start, finish = path[0], path[-1]
        ok = lambda cell: math.gcd(*grid[cell]) == 1
        if dead == 2 and count_routes(ok, n, start, finish) == 1 and len(set(grid.values())) == 16 and len({Fraction(*v) for v in grid.values()}) >= 14: break
    else: raise RuntimeError("p16")
    texts = [[fr(*grid[(r, c)]) for c in range(n)] for r in range(n)]
    body = maze_html(n, texts, start, finish).replace('class="maze tall"', 'class="maze tall fm"')
    P = new_page(16, 3616, "Simplest Form", 1, "Fractions: simplest form", STRAND_FR,
        "1.2 (simplest form)", ["FR1.2"], "Maze / path", "K6 route closes at FINISH",
        ["Start at START. Move up, down, left or right.", "Step only on fractions in simplest form.", "Do not step on a box twice."],
        body, "Route (row, column from top-left): " + " -> ".join(f"({r+1},{c+1}) {grid[(r, c)][0]}/{grid[(r, c)][1]}" for r, c in path),
        f"Route reaches FINISH through {L} boxes; every fraction on it is in simplest form.",
        f"A 4 by 4 grid of sixteen fractions. A fraction is in simplest form when no whole number except 1 divides both the top and the bottom number (so 4/6 is not, 3/5 is). The pupil steps only on those. The boxes off the route are fractions that can still be made simpler (such as 6/8 or 4/12). {dead} extra boxes in simplest form are dead ends. Counting the boxes shows a line that takes a shortcut. Denominators are at most 12.",
        check=f"Does your line reach FINISH? Count its boxes: are there {L}? Is every fraction in simplest form?", mk=("route",),
        mech_plain=f"Route: the line must reach FINISH through the right number of boxes, every fraction being in simplest form")
    g2 = {(r, c): fracs_in(texts[r][c])[0] for r in range(n) for c in range(n)}
    ok2 = lambda cell: all(Fraction(g2[cell][0], g2[cell][1]) != Fraction(a, b) for a in range(1, g2[cell][1]) for b in range(1, g2[cell][1]) if b < g2[cell][1] and b > 0 and a < b)
    ok3 = lambda cell: not any(Fraction(g2[cell][0], g2[cell][1]) == Fraction(a, b) for b in range(2, g2[cell][1]) for a in range(1, b))
    P.v("V1 exactly one route start->finish (exhaustive search; 'simplest form' tested by looking for an equal fraction with a smaller bottom number)", count_routes(ok3, n, start, finish) == 1)
    P.v("V3 dead-end boxes in simplest form exist", dead >= 2, dead)
    P.v("V3b a shortcut that ignores the rule is shorter than the route", abs(start[0]-finish[0]) + abs(start[1]-finish[1]) + 1 < L)
    P.v("V7 proper fractions, denominators at most 12; all sixteen boxes different", all(a < b <= 12 for a, b in g2.values()) and len(set(g2.values())) == 16)
    P["cv"] = dict(rate=1.0, single_total=dead, single_detected=dead)
    allcells = [(r, c) for r in range(n) for c in range(n)]
    def legal(rt):
        if len(rt) != L or len(set(rt)) != L or rt[0] != start or rt[-1] != finish: return False
        return all(ok3(c) for c in rt) and all(abs(a[0]-b[0]) + abs(a[1]-b[1]) == 1 for a, b in zip(rt, rt[1:]))
    P["model"] = dict(truth=list(path), domains=[allcells] * L, check=legal, numeric=False)
    P["mini"] = mini_route(n, path)
    P["facts"] = " ".join(str(x) for v in g2.values() for x in v)
    return P

# =============================================================================== P3-17 Fraction Gaps (equivalent fractions, missing numbers)
def page17():
    rng = random.Random(3717)
    while True:
        items = []
        for kind in ("top", "top", "bottom", "bottom", "top", "bottom"):
            n = rng.choice([2, 3, 4, 5, 6]); m = rng.choice([x for x in (2, 3, 4, 5, 6) if n * x <= 12]); k = rng.randint(1, n - 1)
            items.append(dict(kind=kind, k=k, n=n, m=m))
        rng.shuffle(items)
        ans = [it["k"] * it["m"] if it["kind"] == "top" else it["n"] * it["m"] for it in items]
        if not distinct(ans) or len({Fraction(it["k"], it["n"]) for it in items}) < 6: continue
        pool = set()
        for it in items:
            d = it["n"] * it["m"] - it["n"]
            pool |= {it["k"] + d if it["kind"] == "top" else it["n"] + d, it["k"] * it["m"] + 1, it["n"] * it["m"] - 1}
        pool = sorted(x for x in pool if x not in ans and 1 <= x <= 12)
        res = find_table(17, 6, ans, rng, 1, 12, pool, n_decoy=3, tries=80)
        if res: word, table = res; break
    cards = []; texts = []
    for i, it in enumerate(items):
        k, n, m = it["k"], it["n"], it["m"]
        box = '<span class="ab w2 fb"></span>'
        if it["kind"] == "top": eq = f'{fr(k, n)} = <span class="fr"><i>{box}</i><i>{n * m}</i></span>'
        else: eq = f'{fr(k, n)} = <span class="fr"><i>{k * m}</i><i>{box}</i></span>'
        texts.append(eq); cards.append(qcard(i + 1, f'<div class="fsum">{eq}</div>', ""))
    P = code_items_page(17, 3717, "Fraction Gaps", 2, "Fractions: finding an equivalent fraction when the top or bottom number is given", STRAND_FR,
        "1.1, 1.4 (equivalent fractions; finding an equivalent fraction given the denominator or numerator)", ["FR1.1", "FR1.4"], "Code-breaker (equivalent fractions)",
        ["Write the missing number in each box.", "The two fractions are equal.", INSTR_CODE],
        qgrid(cards, 2), ans, table, word, 1, 12,
        "; ".join(f"{i+1}) {it['k']}/{it['n']} = " + (f"{it['k'] * it['m']}/{it['n'] * it['m']}" if True else "") for i, it in enumerate(items)),
        "Six pairs of equal fractions with one number missing: three with the top number missing and three with the bottom number missing. The pupil multiplies the top and the bottom by the same number. The decoy letters stand for adding the same number to the top and the bottom instead of multiplying. All numbers are within 12. A box left blank gives no letter and the check cannot see it.")
    solved = []
    for it, t in zip(items, texts):
        fs = re.findall(r'<span class="fr"><i>(.*?)</i><i>(.*?)</i></span>', t)
        (a, b), (c, d) = fs
        a, b = int(a), int(b)
        if "ab w2" in c: solved.append(a * int(d) // b)            # missing top: a/b = ?/d
        else: solved.append(b * int(c) // a)                         # missing bottom: a/b = c/?
    P.v("V1 independent solver (cross-multiplying the printed fractions) equals the key", solved == ans, solved)
    P.v("V7 every number printed or written is within 12", max(ans) <= 12 and all(it["n"] <= 6 for it in items))
    P.v("V1b three top-missing and three bottom-missing items", sum(1 for it in items if it["kind"] == "top") == 3)
    return P

# =============================================================================== P3-18 Fraction Order (unlike fractions)
def page18():
    rng = random.Random(3818)
    fams = [(2, 4, 8), (3, 6, 12), (2, 3, 6), (2, 5, 10), (3, 4, 12), (2, 4, 6), (4, 6, 12), (2, 3, 4)]
    for _ in range(5000):
        word = word_candidates(18, 6)[0]
        def make():
            fam = rng.choice(fams); ds = list(fam); rng.shuffle(ds)
            vals = []
            for d in ds:
                k = rng.randint(1, d - 1); vals.append((k, d))
            return vals
        A_ = make(); B_ = make()
        if len({Fraction(*v) for v in A_}) < 3 or len({Fraction(*v) for v in B_}) < 3: continue
        if {Fraction(*v) for v in A_} & {Fraction(*v) for v in B_}: continue
        if any(math.gcd(k, d) > 1 and d > 6 for k, d in A_ + B_): continue
        break
    CLAIMED[18] = word
    A_s = sorted(A_, key=lambda v: Fraction(*v)); B_s = sorted(B_, key=lambda v: -Fraction(*v))
    lab = {}
    for i, v in enumerate(A_s): lab[("A", v)] = word[i]
    for i, v in enumerate(B_s): lab[("B", v)] = word[3 + i]
    shA = A_[:]; shB = B_[:]; rng.shuffle(shA); rng.shuffle(shB)
    def card_html(g, v): return f'<div class="fcard"><div class="fnum">{fr(*v)}</div><i class="cl">{lab[(g, v)]}</i></div>'
    body = (f'<div class="blk"><p class="lead">Set A: smallest first.</p><div class="fcards">{"".join(card_html("A", v) for v in shA)}</div></div>'
            f'<div class="blk"><p class="lead">Set B: greatest first.</p><div class="fcards">{"".join(card_html("B", v) for v in shB)}</div></div>'
            f'<div class="blk"><p class="lead">Write the letters in order: Set A, then Set B.</p><div class="ansgrid2" style="margin-top:2mm">' + "".join('<span class="ab"></span>' for _ in range(6)) + '</div></div>')
    P = new_page(18, 3818, "Fraction Order", 2, "Fractions: comparing and ordering unlike fractions", STRAND_FR,
        "1.3 (comparing and ordering unlike fractions; denominators not exceeding 12)", ["FR1.3", "FR1.1"], "Ordering (lettered cards)", "K1 letters in order spell a word (6 letters) + K4 each card used once",
        ["Put each set of fractions in order.", "Write the letter of each card in its place.", "Set A: smallest first. Set B: greatest first."],
        body, "Set A (smallest first): " + ", ".join(f"{lab[('A', v)]} = {v[0]}/{v[1]}" for v in A_s) + "; Set B (greatest first): " + ", ".join(f"{lab[('B', v)]} = {v[0]}/{v[1]}" for v in B_s), f"Word: {word}",
        "Each set has three unlike fractions whose denominators are related (for example 2, 4 and 8, or 3, 6 and 12), so the pupil can change them to equal fractions with the same bottom number and compare the tops. No two fractions in a set are equal. The letters, read in the order asked, spell a word with exactly one arrangement that is a word, so no wrong order of the six cards spells a word (every wrong order was tested against a very large word list). A box left blank gives no letter and the check cannot see it.",
        check="Read the six letters in order. Do they spell a word?", check_boxes=None, mk=("logic",),
        mech_plain="Letters of the cards in the order asked spell a word (6 letters)")
    P["check_boxes"] = None
    secA, secB = body.split("Set B: greatest first.")
    ra = re.findall(r'<span class="fr"><i>(\d+)</i><i>(\d+)</i></span></div><i class="cl">(\w)</i>', secA); rb = re.findall(r'<span class="fr"><i>(\d+)</i><i>(\d+)</i></span></div><i class="cl">(\w)</i>', secB)
    solved = "".join(c[2] for c in sorted(ra, key=lambda c: Fraction(int(c[0]), int(c[1]))) + sorted(rb, key=lambda c: -Fraction(int(c[0]), int(c[1]))))
    P.v("V1 independent solver (fractions read back and sorted by exact value) gets the word", solved == word, solved)
    P.v("V1b no two fractions in a set are equal, denominators within 12", all(len({Fraction(int(a), int(b)) for a, b, _ in s}) == 3 for s in (ra, rb)) and all(int(b) <= 12 for a, b, _ in ra + rb))
    P.v("V3d the code word's letters have exactly ONE arrangement that is a word", anagrams(word) == [word.lower()], anagrams(word))
    bad = sorted(w for w in ("".join(p) for p in itertools.permutations(word)) if w != word and w.lower() in BIG)
    P.v("V3 none of the 719 wrong orders of the six letters spells a word", not bad, bad[:3])
    P["cv"] = dict(rate=1.0, single_total=719, single_detected=719)
    P["model"] = dict(truth=list(word), domains=[sorted(set(word))] * 6, check=letters_check(), perm=list(range(6)))
    return P

# =============================================================================== P3-19 Fraction Sums
def page19():
    rng = random.Random(3919)
    def related():
        d1 = rng.choice([2, 3, 4, 5]); f = rng.choice([x for x in (2, 3, 4) if d1 * x <= 12]); return d1, d1 * f, f
    while True:
        items = []
        d1, d2, f = related(); a = rng.randint(1, d1 - 1); b = rng.randint(1, d2 - 1)
        while a * f + b >= d2: b = rng.randint(1, d2 - 1) if d2 > 2 else 1; a = rng.randint(1, d1 - 1)
        items.append(dict(k="add", d1=d1, d2=d2, a=a, b=b, D=d2, ans=a * f + b))
        d1, d2, f = related(); a = rng.randint(1, d1 - 1); b = rng.randint(1, d2 - 1)
        while a * f + b >= d2: b = rng.randint(1, d2 - 1); a = rng.randint(1, d1 - 1)
        items.append(dict(k="add2", d1=d1, d2=d2, a=a, b=b, D=d2, ans=a * f + b))
        for _ in range(2):
            d1, d2, f = related(); a = rng.randint(1, d1 - 1)
            top = a * f; b = rng.randint(1, top - 1) if top > 1 else None
            if b is None: break
            items.append(dict(k="sub", d1=d1, d2=d2, a=a, b=b, D=d2, ans=top - b))
        if len(items) != 4: continue
        d1, d2, f = related(); a = rng.randint(1, d1 - 1)
        items.append(dict(k="whole", d1=d1, d2=d2, a=a, D=d2, ans=d2 - a * f))
        d1, d2, f = related(); a = rng.randint(1, d1 - 1); b = rng.randint(1, d2 - 1)
        if a * f + b >= d2: continue
        items.append(dict(k="story", d1=d1, d2=d2, a=a, b=b, D=d2, N=rng.choice(PEOPLE), M=rng.choice(PEOPLE), ans=a * f + b))
        if len(items) != 6 or any(it["k"] == "story" and it["N"] == it["M"] for it in items): continue
        rng.shuffle(items); items.sort(key=lambda it: it["k"] == "story"); ans = [it["ans"] for it in items]
        if not distinct(ans) or any(it["ans"] <= 0 for it in items): continue
        if len({(it["k"], it["a"], it["d1"], it.get("b")) for it in items}) < 6: continue
        pool = set()
        for it in items:
            pool |= {it["D"] - it["ans"], it["a"] + it.get("b", 0), abs(it["a"] - it.get("b", 0)), it["a"]}
        pool = sorted(x for x in pool if x not in ans and 1 <= x <= 12)
        res = find_table(19, 6, ans, rng, 0, 12, pool, n_decoy=3, tries=80)
        if res: word, table = res; break
    cards = []; texts = []
    for i, it in enumerate(items):
        box = '<span class="ab w2 fb"></span>'
        blank = f'<span class="fr"><i>{box}</i><i>{it["D"]}</i></span>'
        if it["k"] in ("add", "add2"): t = f'{fr(it["a"], it["d1"])} + {fr(it["b"], it["d2"])} = {blank}'
        elif it["k"] == "sub": t = f'{fr(it["a"], it["d1"])} − {fr(it["b"], it["d2"])} = {blank}'
        elif it["k"] == "whole": t = f'1 − {fr(it["a"], it["d1"])} = {blank}'
        else: t = f'<span class="ptxt">{it["N"]} ate {fr(it["a"], it["d1"])} of a pizza. {it["M"]} ate {fr(it["b"], it["d2"])}. What fraction did they eat in all?</span> {blank}'
        texts.append(t); cards.append(qcard(i + 1, f'<div class="fsum">{t}</div>', "", cls="span2" if it["k"] == "story" else ""))
    P = code_items_page(19, 3919, "Fraction Sums", 2, "Fractions: adding and subtracting two related fractions within one whole", STRAND_FR,
        "2.1 (adding and subtracting two related fractions within one whole)", ["FR2.1"], "Code-breaker (fractions)",
        ["Add or subtract the fractions.", "The answer's bottom number is printed. Write the top number in the box.", INSTR_CODE],
        qgrid(cards, 2), ans, table, word, 0, 12,
        "; ".join(f"{i+1}) {x}/{it['D']}" for i, (it, x) in enumerate(zip(items, ans))),
        "Six items with two related fractions, that is, one bottom number is made from the other by multiplying (for example halves and quarters, thirds and ninths). Two additions, two subtractions, one whole minus a fraction and a story. Every answer is smaller than one whole. The bottom number of the answer is printed (the larger one); the pupil changes the other fraction to equal parts and writes the top number. The decoy letters stand for adding or subtracting the top numbers without changing parts, or for the part left over. A box left blank gives no letter and the check cannot see it.")
    solved = []
    for t in texts:
        fs = re.findall(r'<span class="fr"><i>(\d+)</i><i>(\d+)</i></span>', t)
        D = int(re.findall(r'<i>(?:<span[^>]*></span>)</i><i>(\d+)</i>', t)[0])
        vals = [Fraction(int(a), int(b)) for a, b in fs]
        if t.startswith("1 "): res = 1 - vals[0]
        elif "−" in t: res = vals[0] - vals[1]
        else: res = vals[0] + vals[1]
        solved.append(int(res * D))
    P.v("V1 independent solver (fractions read back, exact arithmetic) equals the key", solved == ans, solved)
    P.v("V7 every answer is less than one whole; denominators at most 12; the two bottom numbers are related (one a multiple of the other)", all(it["ans"] < it["D"] <= 12 and it["D"] % it["d1"] == 0 for it in items))
    return P

# =============================================================================== P3-20 Money Sums
def page20():
    rng = random.Random(3020)
    things = ["pen", "ruler", "book", "bag", "cap", "scarf", "ball", "kite", "puzzle", "notebook"]
    def price(lo, hi): return rng.randrange(lo, hi, 5)
    while True:
        a1, b1 = price(150, 600), price(100, 500)
        a2 = price(700, 1500); b2 = price(210, a2 - 100)
        pay = rng.choice([1000, 2000, 5000]); c3 = price(pay // 3, pay - 100)
        a4, b4 = price(900, 1900), price(400, 800)
        t1, t2, t3 = price(150, 500), price(150, 500), price(150, 500)
        coins = [("n", 5), ("n", 2), ("c", 50), ("c", 20), ("c", 10)]
        rng.shuffle(coins)
        coin_total = sum(100 * v if k == "n" else v for k, v in coins)
        nm = rng.sample(PEOPLE, 6)
        th = rng.sample(things, 6)
        items = [dict(k="add", a=a1, b=b1, n=nm[0], th=th[:2], ans=a1 + b1),
                 dict(k="left", a=a2, b=b2, n=nm[1], th=th[2], ans=a2 - b2),
                 dict(k="change", pay=pay, p=c3, n=nm[2], th=th[3], ans=pay - c3),
                 dict(k="pic", coins=coins, ans=coin_total),
                 dict(k="more", a=a4, b=b4, th=th[4:6], ans=a4 - b4),
                 dict(k="three", a=t1, b=t2, c=t3, n=nm[5], ans=t1 + t2 + t3)]
        rng.shuffle(items); items.sort(key=lambda it: it["k"] == "pic"); ans = [it["ans"] for it in items]
        if not distinct(ans) or max(ans) > 9999: continue
        pool = set()
        for it in items:
            if it["k"] in ("add", "three"): pool |= {it["ans"] + 10, it["ans"] - 100, it["ans"] + 100}
            if it["k"] in ("left", "more"): pool |= {it["a"] + it["b"], it["ans"] + 100, it["ans"] - 10}
            if it["k"] == "change": pool |= {it["pay"] + it["p"], it["ans"] + 100, it["ans"] - 100, 2000 - it["p"]}
            if it["k"] == "pic": pool |= {it["ans"] - 100, it["ans"] + 5, it["ans"] - 50}
        pool = sorted(p for p in pool if p not in ans and 0 < p <= 9999)
        res = find_table(20, 6, ans, rng, 0, 9999, pool, n_decoy=3, tries=20)
        if res: word, table = res; break
    cards = []; texts = []
    for i, it in enumerate(items):
        box = '<span class="dl">$</span><span class="ab w4"></span>'
        k = it["k"]
        if k == "add": t = f"{it['n']} buys a {it['th'][0]} for {money(it['a'])} and a {it['th'][1]} for {money(it['b'])}. How much does {it['n']} pay in all?"
        elif k == "left": t = f"{it['n']} has {money(it['a'])}. {it['n']} buys a {it['th']} for {money(it['b'])}. How much money is left?"
        elif k == "change": t = f"{it['n']} pays {money(it['pay'])} for a {it['th']} that costs {money(it['p'])}. How much change does {it['n']} get?"
        elif k == "more": t = f"A {it['th'][0]} costs {money(it['a'])}. A {it['th'][1]} costs {money(it['b'])}. How much more does the {it['th'][0]} cost?"
        elif k == "three": t = f"{it['n']} buys 3 stickers: {money(it['a'])}, {money(it['b'])} and {money(it['c'])}. How much is the total?"
        else: t = "How much money is shown?"
        texts.append(t)
        if k == "pic":
            cards.append(qcard(i + 1, f"<p>{t}</p>" + A2.money_svg(it["coins"]), '<span class="dl">$</span><span class="ab w4"></span>', cls="span2 inl"))
        else:
            cards.append(qcard(i + 1, f"<p>{t}</p>", '<span class="dl">$</span><span class="ab w4"></span>'))
    P = code_items_page(20, 3020, "Money Sums", 1, "Money: adding and subtracting in dollars and cents", STRAND_MO,
        "1.1 (adding and subtracting money in decimal notation)", ["MO1.1"], "Code-breaker (money)",
        ["Work out each amount. Write it like this: $3.45.", INSTR_CODE],
        '<div class="qg c2">' + "".join(cards) + "</div>", ans, table, word, 0, 9999,
        "; ".join(f"{i+1}) {money(a)}" for i, a in enumerate(ans)),
        "Six money items in decimal notation: an addition, a subtraction (money left), change from a note, 'how much more', a total of three prices and a count of the notes and coins drawn. Prices are in dollars and cents ($3.45); every answer is written with a dollar sign, a point and two cents digits. The decoy letters stand for adding where the item subtracts, or for a dollar too many or too few. Pictures are not actual size. A box left blank gives no letter and the check cannot see it.",
        domain=None, fmt=money)
    P["facts"] = " ".join(re.findall(r"\d+", " ".join(texts))) + " " + " ".join(str(a) for a in ans) + " " + " ".join(re.findall(r"\d+", " ".join(money(k) for k in table)))
    solved = []
    for t, c in zip(texts, cards):
        ms = [unmoney(x) for x in re.findall(r"\$\d+\.\d\d", t)]
        if t.startswith("How much money is shown"): solved.append(A2.read_money(c))
        elif "How much does" in t and "pay in all" in t or "total" in t: solved.append(sum(ms))
        elif "change" in t: solved.append(ms[0] - ms[1])
        elif "left" in t or "How much more" in t: solved.append(ms[0] - ms[1])
        else: raise ValueError(t)
    P.v("V1 independent solver (prices read from the text, coins and notes read from their printed values) equals the key", solved == ans, solved)
    P.v("V7 every amount is below $100 and written with two decimal places", all(a < 10000 for a in ans) and all(re.fullmatch(r"\$\d+\.\d\d", x) for t in texts for x in re.findall(r"\$\d+\.\d*", t)))
    return P

PAGES = [page15, page16, page17, page18, page19, page20]
