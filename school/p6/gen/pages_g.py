"""Part G (replacing the three earlier revision pages that the syllabus PDF puts outside Primary 6): P6-34 Fraction Order, P6-35 Ratio Stories, P6-36 Circle Choices (pi = 3.14)."""
import random, re, math, itertools
from fractions import Fraction as Fr
from math import gcd
from .common import *
from .kit import *
from .kit6 import *
from .pages_a import ftup, fdomain

def ans_text(x):
    x = Fr(x)
    if x.denominator == 1: return str(x.numerator)
    return ptxt(mxx(x)).replace("_", " ") if x > 1 else ptxt(frx(x))

# =============================================================================== P6-34 Fraction Order  (FR1.1, FR1.2, ordering)
def fo_item(rng, kind):
    while True:
        if kind == "fw":
            n = rng.choice([2, 3, 4, 5, 6]); b = rng.randint(3, 9); a = rng.randint(1, b - 1)
            if gcd(a, b) != 1: continue
            return dict(x=Fr(a, b) / n, h=f'{fh(a, b)} ÷ {n} =')
        if kind == "wf":
            q = rng.randint(3, 8); p = rng.randint(1, q - 1); n = rng.randint(2, 9)
            if gcd(p, q) != 1: continue
            return dict(x=Fr(n) / Fr(p, q), h=f'{n} ÷ {fh(p, q)} =')
        a, b = rng.randint(1, 8), rng.randint(2, 9); c, d = rng.randint(1, 8), rng.randint(2, 9)
        if not (a < b and c < d and gcd(a, b) == 1 and gcd(c, d) == 1 and Fr(a, b) != Fr(c, d)): continue
        return dict(x=Fr(a, b) / Fr(c, d), h=f'{fh(a, b)} ÷ {fh(c, d)} =')

def page34():
    rng = random.Random(9134)
    kinds = ["fw", "fw", "wf", "wf", "ff", "ff"]
    for _ in range(2000):
        its = [fo_item(rng, k) for k in kinds]
        vals = [it["x"] for it in its]
        if len(set(vals)) < 6 or min(abs(a - b) for a, b in itertools.combinations(vals, 2)) < Fr(1, 6): continue
        if any(v.denominator > 24 or v > 12 for v in vals): continue
        break
    rng.shuffle(its)
    cards = [f'<div class="mnc">{it["h"]}</div>' for it in its]
    order_idx = sorted(range(6), key=lambda j: its[j]["x"])
    read_card = lambda c: calc(ptxt(c).replace("=", "").strip())
    P = order_page(34, 9134, "Fraction Order", 1, "Fractions: dividing by a whole number and by a fraction", STRAND_FR,
        "1.1, 1.2 (dividing a proper fraction by a whole number; dividing a whole number or a proper fraction by a proper fraction)", ["FR1.1", "FR1.2"], "Ordering (fraction divisions)",
        ["Work out each answer.", "Put the answers in order, smallest first.", "Write the letters in order."],
        rng, cards, order_idx, read_card,
        "Six divisions: two of a proper fraction by a whole number, two of a whole number by a proper fraction, and two of a proper fraction by a proper fraction. The pupil works out all six answers and puts them in order, smallest first; the letters, read in that order, spell the word. The six answers differ by at least a sixth, so a slip in one answer usually changes its place. Every wrong order was tested against a very large word list: none spells a word. A box left blank gives no letter and the check cannot see it.",
        ncols=2, row_mm=34, lead="Write the letters in order, smallest answer first.",
        card_text=lambda ci: ans_text(its[ci]["x"]), direction="smallest answer first")
    P.v("V7 every answer is below 12 and has a bottom number of at most 24", all(it["x"] <= 12 and it["x"].denominator <= 24 for it in its))
    return P

# =============================================================================== P6-35 Ratio Stories  (RA1.2, RA1.3, RA1.6, RA1.7, code)
def rs_item(rng, kind, X, Y):
    while True:
        a, b = rng.sample(range(2, 10), 2)
        if gcd(a, b) == 1: break
    u = rng.randint(3, 15)
    if kind == "known":
        return dict(t=f"The ratio of {X}'s stickers to {Y}'s stickers is {a} : {b}. {X} has {a * u} stickers. How many stickers does {Y} have?", ans=b * u, wrong=[a * u, u, (a + b) * u])
    if kind == "diff":
        a, b = max(a, b), min(a, b)
        return dict(t=f"{X} has ${(a - b) * u} more than {Y}. The ratio of {X}'s money to {Y}'s money is {a} : {b}. How much money does {Y} have?", ans=b * u, wrong=[(a - b) * u, a * u, (a + b) * u])
    if kind == "girls":
        return dict(t=f"The ratio of boys to girls in a hall is {a} : {b}. There are {(a + b) * u} pupils in the hall. How many girls are there?", ans=b * u, wrong=[a * u, u, b * u - a * u if b > a else (a + b)])
    if kind == "inall":
        return dict(t=f"The ratio of red beads to blue beads is {a} : {b}. There are {a * u} red beads. How many beads are there in all?", ans=(a + b) * u, wrong=[b * u, a * u + b, u])
    if kind == "three":
        while True:
            a, b, c = sorted(rng.sample(range(2, 9), 3))
            if gcd(gcd(a, b), c) == 1: break
        u = rng.randint(2, 12)
        return dict(t=f"A bag has red, blue and green beads in the ratio {a} : {b} : {c}. There are {a * u} red beads. How many beads are in the bag?", ans=(a + b + c) * u, wrong=[c * u, (b + c) * u, u])
    s = rng.choice([(1, 3), (1, 4), (3, 7), (2, 3), (1, 9), (3, 17), (1, 1)]); a, b = s
    if a == b: a, b = 2, 3
    tot = a + b
    for cand in ((1, 3), (1, 4), (3, 7), (2, 3), (3, 2), (1, 9), (7, 3), (4, 1)):
        if 100 % (cand[0] + cand[1]) == 0 and cand != (a, b): pass
    pairs = [(1, 3), (1, 4), (3, 2), (3, 7), (7, 3), (1, 9), (9, 11), (4, 1), (3, 1)]
    a, b = rng.choice([p for p in pairs if 100 % (p[0] + p[1]) == 0])
    return dict(t=f"The ratio of boys to girls in a class is {a} : {b}. What percentage of the class are boys?", ans=100 * a // (a + b), wrong=[100 * b // (a + b), a * 10, 100 // a])

def rs_solve(t):
    nums = [int(x) for x in re.findall(r"\d+", t)]
    if "percentage" in t:
        a, b = nums[0], nums[1]; return 100 * a // (a + b)
    if "more than" in t:
        d, a, b = nums[0], nums[1], nums[2]; return d // (a - b) * b
    if "stickers to" in t:
        a, b, k = nums[0], nums[1], nums[2]; return k // a * b
    if "boys to girls" in t:
        a, b, n = nums[0], nums[1], nums[2]; return n // (a + b) * b
    if "red beads to blue" in t:
        a, b, k = nums[0], nums[1], nums[2]; return k // a * (a + b)
    a, b, c, k = nums[0], nums[1], nums[2], nums[3]; return k // a * (a + b + c)

def page35():
    rng = random.Random(9235)
    kinds = ["known", "diff", "girls", "inall", "three", "pct"]
    for _ in range(400):
        X, Y = rng.sample(PEOPLE, 2)
        its = [rs_item(rng, k, X, Y) for k in kinds]; rng.shuffle(its)
        ans = [it["ans"] for it in its]
        if not distinct(ans) or max(ans) > 400: continue
        pool = sorted({w for it in its for w in it["wrong"] if 0 < w <= 400 and w not in ans})
        res = make_table(35, ans, rng, 1, 400, pool=pool, n_decoy=3)
        if res: word, table = res; break
    cards = [qcard(i + 1, f'<p>{it["t"]}</p>', ans_ratio(1, "w4")) for i, it in enumerate(its)]
    P = code_page(35, 9235, "Ratio Stories", 2, "Ratio: finding a quantity from a ratio and one known amount", STRAND_RA,
        "1.2, 1.3, 1.6, 1.7 (equivalent ratios; dividing a quantity in a ratio; finding the missing term; the link between fraction and ratio)", ["RA1.2", "RA1.3", "RA1.6", "RA1.7"], "Code-breaker (ratio stories)",
        ["Work out each answer.", "Write the answer in the box.", "Use the code table."],
        cards, ans, table, word, 1, 400, "; ".join(f"{i+1}) {a}" for i, a in enumerate(ans)),
        "Six stories: the other quantity when one quantity and the ratio are known, one quantity when the difference is known, one part of a total shared in a ratio, the total when one part is known, the same with three parts, and the percentage that one part of a ratio is. The decoy numbers are what a pupil gets by giving the known quantity, the value of one part, or the total. A box left blank gives no letter and the check cannot see it.", ncols=2)
    solved = [rs_solve(it["t"]) for it in its]
    P.v("V1 independent solver reads each printed story and equals the key", solved == ans, solved)
    P.v("V7 every ratio uses whole numbers and every answer is a whole number of at most 400", max(ans) <= 400)
    return P

# =============================================================================== P6-36 Circle Choices  (AV1.1, AV1.2, pi = 3.14, lettered choices)
P314 = Fr(314, 100)
def cc_row(rng, kind, r):
    d = 2 * r
    if kind == "area":
        v = P314 * r * r; return dict(stem=f"A circle has a radius of {r} cm. Find its area.", right=(v, "cm²"), wrong=[(P314 * d, "cm²"), (P314 * d * d, "cm²"), (v / 2, "cm²")])
    if kind == "circ":
        v = P314 * d; return dict(stem=f"A round table has a diameter of {d} cm. Find the distance round its edge.", right=(v, "cm"), wrong=[(v * 2, "cm"), (P314 * r * r, "cm"), (v / 2, "cm")])
    if kind == "semi":
        v = P314 * r * r / 2; return dict(stem=f"A semicircle has a radius of {r} cm. Find its area.", right=(v, "cm²"), wrong=[(P314 * r * r, "cm²"), (P314 * r, "cm²"), (v / 2, "cm²")])
    if kind == "semip":
        v = P314 * r + d; return dict(stem=f"A semicircle has a diameter of {d} cm. Find its perimeter.", right=(v, "cm"), wrong=[(P314 * r, "cm"), (P314 * d + d, "cm"), (P314 * r + r, "cm")])
    if kind == "quarter":
        v = P314 * r * r / 4; return dict(stem=f"A quarter circle has a radius of {r} cm. Find its area.", right=(v, "cm²"), wrong=[(P314 * r * r / 2, "cm²"), (P314 * r * r, "cm²"), (P314 * r / 2, "cm²")])
    v = Fr(r); return dict(stem=f"The distance round a circle is {dec(P314 * d)} cm. Find its radius.", right=(v, "cm"), wrong=[(Fr(d), "cm"), (v / 2, "cm"), (v * v, "cm")])

def cc_solve(stem, opts):
    t = stem; n = Fr(re.search(r"(\d+(?:\.\d+)?)", t.replace("3.14", "")).group(1))
    if "round a circle" in t: want = n / (2 * P314)
    elif "semicircle" in t and "area" in t: want = P314 * n * n / 2
    elif "semicircle" in t: want = P314 * n / 2 + n
    elif "quarter" in t: want = P314 * n * n / 4
    elif "round its edge" in t: want = P314 * n
    else: want = P314 * n * n
    vals = [Fr(re.search(r"(\d+(?:\.\d+)?)", ptxt(o)).group(1)) for o in opts]
    return vals.index(want) if want in vals else -1

def page36():
    rng = random.Random(9336)
    kinds = ["area", "circ", "semi", "semip", "quarter", "radius"]
    for _ in range(400):
        rs = [rng.choice([4, 6, 8, 10, 12, 14, 16, 20]) for _ in kinds]
        rows = []
        for k, r in zip(kinds, rs):
            c = cc_row(rng, k, r)
            allv = [c["right"]] + c["wrong"]
            if len({v for v, _ in allv}) < 4: break
            opts = [f"{dec(v)} {u}" for v, u in allv]
            order = list(range(4)); rng.shuffle(order); order = order[:3] if 0 in order[:3] else [0] + order[:2]
            rng.shuffle(order)
            rows.append(dict(stem=c["stem"], opts=[opts[j] for j in order], right=order.index(0)))
        else:
            if len({r["stem"] for r in rows}) == 6:
                rng.shuffle(rows); break
    P = choice_page(36, 9336, "Circle Choices", 1, "Circles: area and circumference with pi as 3.14", STRAND_AV,
        "1.1, 1.2 (area and circumference of a circle; area and perimeter of a semicircle and a quarter circle)", ["AV1.1", "AV1.2"], "Choice table (circles)",
        [f"Take {PIP} as 3.14.", "Work out each answer.", "Circle the letter beside the right answer.", "Write the six letters in the boxes."],
        rng, rows, cc_solve,
        "Six short questions on circles with pi as 3.14: the area of a circle, the distance round a circle, the area of a semicircle, the perimeter of a semicircle, the area of a quarter circle and the radius from the distance round. The pupil chooses the right answer of three. The wrong answers are what a pupil gets by using the diameter for the radius, by forgetting to square, or by halving or doubling. The letters of the right choices, read down the rows, spell the word. Every other way of choosing was tested against a very large word list: none spells a word. A box left blank gives no letter and the check cannot see it.")
    return P

PAGES = [page34, page35, page36]
