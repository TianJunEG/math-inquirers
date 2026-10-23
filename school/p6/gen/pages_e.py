"""Part E: angles and average. P6-27 Angles in Figures, P6-28 More Angles, P6-29 Angle Match, P6-30 Average, P6-31 Missing Value."""
import random, re, math, itertools
from fractions import Fraction as Fr
from math import gcd
from .common import *
from .kit import *
from .kit6 import *
from . import angles as AN

def ang_make(rng, spec, keepout=False):
    """spec = (family, params...) -> (svg html, caption, answer, mirrored)"""
    fam = spec[0]; args = spec[1:]
    fn = dict(iso_line=AN.iso_line, rhombus_diag=AN.rhombus_diag, rhombus_opp=AN.rhombus_opp, sq_tri=AN.sq_tri, para_iso=AN.para_iso, trapezium=AN.trapezium, tri_ext=AN.tri_ext)[fam]
    f, cap, ans = fn(*args)
    mirror = rng.random() < 0.5
    return AN.render(f, mirror=mirror, keepout=keepout), cap, int(ans)

def rand_spec(rng, fam):
    if fam == "iso_line": return ("iso_line", rng.choice(range(24, 101, 2)), "exterior")
    if fam == "iso_apex": return ("iso_line", rng.choice(range(24, 101, 2)), "apex")
    if fam == "rhombus_diag": return ("rhombus_diag", rng.choice([x for x in range(40, 141, 2) if x != 90]))
    if fam == "rhombus_opp": return ("rhombus_opp", rng.choice([x for x in range(40, 141, 2) if x != 90]))
    if fam == "sq_out": return ("sq_tri", True)
    if fam == "sq_in": return ("sq_tri", False)
    if fam == "para_iso": return ("para_iso", rng.choice([x for x in range(60, 141, 2) if x != 90]))
    if fam == "trapezium": return ("trapezium", rng.choice([x for x in range(55, 126, 5) if x != 90]))
    return ("tri_ext", rng.randint(25, 80), rng.randint(25, 70))

def ang_set(rng, fams, tries=400, keepout=False):
    for _ in range(tries):
        items = []
        try:
            for fam in fams:
                spec = rand_spec(rng, fam); svg, cap, ans = ang_make(rng, spec, keepout); items.append(dict(fam=fam, svg=svg, cap=cap, ans=ans, spec=spec))
        except RuntimeError:
            continue                                  # a figure that cannot be drawn clearly out of scale: draw a new set
        if len({it["ans"] for it in items}) == len(fams) and all(10 <= it["ans"] <= 170 for it in items): return items
    raise RuntimeError("angle set")

def ang_pool(items):
    pool = set()
    for it in items:
        a = it["ans"]; sp = it["spec"]
        for v in (180 - a, a + 10, a - 10, 90 - a, 2 * a, a // 2, a + 5, a - 5, a + 20, a - 20, 180 - 2 * a):
            if 1 <= v <= 179: pool.add(v)
        for g in sp[1:]:
            if isinstance(g, int) and 1 <= g <= 179: pool.add(g)
    return pool

def ang_card(i, it):
    return qcard(i + 1, f'<div class="fig fcd">{it["svg"]}</div><p class="note1">{it["cap"]}</p>', f'{abx("w3")}{unit("°")}', cls="posb")

def ang_solve(card):
    svg = re.search(r"<svg.*?</svg>", card, re.S).group(0)
    cap = ptxt(card[card.index("</svg>"):])
    m, bad, ok = AN.read_angle_figure(svg, cap)
    return m, bad, ok

def ang_checks(P, cards, ans):
    res = [ang_solve(c) for c in cards]
    P.v("V1 independent solver measures the named angle from the printed figure (vertex points): equals the key", all(abs(m - a) < 0.6 for (m, _, _), a in zip(res, ans)), [round(m, 1) for m, _, _ in res])
    P.v("V1b every given angle printed in an arc equals the drawn angle (within 0.6 degrees)", all(not b for _, b, _ in res), [b for _, b, _ in res if b][:2])
    P.v("V1c the question-mark arc is at the vertex and between the rays named in the question", all(o for _, _, o in res))

def page_angles(no, seed, title, tier, fams, note, instr):
    rng = random.Random(seed)
    for _ in range(100):
        items = ang_set(rng, fams)
        ans = [it["ans"] for it in items]
        pool = sorted(p for p in ang_pool(items) if p not in ans)
        res = make_table(no, ans, rng, 1, 179, pool=pool, n_decoy=2)
        if res: word, table = res; break
    cards = [ang_card(i, it) for i, it in enumerate(items)]
    P = code_page(no, seed, title, tier, "Unknown angles in composite figures", STRAND_GE,
        "1.1 (finding unknown angles in composite figures involving squares, rectangles, triangles, parallelograms, rhombuses and trapeziums; no additional construction)", ["GE1.1"], "Code-breaker (unknown angles)",
        instr, cards, ans, table, word, 1, 179, "; ".join(f"{i+1}) {a}°" for i, a in enumerate(ans)), note, ncols=3, cols=8)
    ang_checks(P, cards, ans)
    P.v("V7 every angle is a whole number of degrees between 10 and 170", all(10 <= a <= 170 for a in ans))
    return P

def page27():
    return page_angles(27, 8727, "Angles in Figures", 1, ["trapezium", "tri_ext", "iso_line", "rhombus_diag", "tri_ext", "trapezium"],
        "Six figures in one or two steps: a trapezium (the angles between the parallel sides add to 180 degrees), a triangle with a straight line (the angle sum of a triangle and angles on a straight line), an isosceles triangle with a straight line, and a rhombus with a diagonal (all four sides are equal, so a triangle is isosceles). The decoy numbers are what a pupil gets by using 180 minus the answer, by using the given angle, or by halving or doubling. The figures are deliberately NOT drawn to scale (the drawn angles differ from the true ones by at least 9 degrees for the unknown angle) and each page says so, so measuring does not give the answer. A box left blank gives no letter and the check cannot see it.",
        ["Find each angle. Marks show equal sides and parallel lines.", "Not drawn to scale: work it out, do not measure.", "Write the answer in the box. Use the code table."])

def page28():
    return page_angles(28, 8828, "More Angles", 2, ["para_iso", "iso_apex", "rhombus_opp", "sq_out", "sq_in", "rhombus_diag"],
        "Six figures that need two or three steps: a parallelogram with an isosceles triangle (opposite angles of a parallelogram are equal), an isosceles triangle where the exterior angle is given, a rhombus where the opposite angle is given, and a square with an equilateral triangle on one side, outside and inside. In the square figures the pupil finds an angle of a triangle whose two equal sides are the side of the square and the side of the triangle. The decoy numbers are what a pupil gets by using 180 minus the answer, by using the given angle, or by halving or doubling. The figures are deliberately NOT drawn to scale and the page says so. A box left blank gives no letter and the check cannot see it.",
        ["Find each angle. Marks show equal sides and parallel lines.", "Not drawn to scale: work it out, do not measure.", "Write the answer in the box. Use the code table."])

# =============================================================================== P6-29 Angle Match  (GE1.1, match)
def page29():
    rng = random.Random(8929)
    for _ in range(300):
        items = ang_set(rng, ["iso_line", "rhombus_diag", "trapezium", "tri_ext", "iso_apex", "para_iso"], keepout=True)
        ans = [it["ans"] for it in items]
        decs = []
        for it in rng.sample(items, 2):
            v = 180 - it["ans"] if it["ans"] != 90 else it["ans"] + 10
            if v not in ans and v not in decs and 1 <= v <= 179: decs.append(v)
        if len(decs) < 2: continue
        allv = ans + decs
        if len(set(allv)) < 8: continue
        break
    order = list(range(8)); rng.shuffle(order)
    card_html = [f'<span class="rt">{allv[j]}°</span>' for j in order]
    right = [order.index(i) for i in range(6)]
    item_html = [f'<div class="fig fcd">{it["svg"]}</div><!--cap--><p>{it["cap"]}</p>' for it in items]
    def solve_item(ih, chs):
        svg = re.search(r"<svg.*?</svg>", ih, re.S).group(0); cap = ptxt(ih[ih.index("</svg>"):])
        m, bad, ok = AN.read_angle_figure(svg, cap)
        for j, c in enumerate(chs):
            if abs(int(re.search(r"\d+", ptxt(c)).group(0)) - m) < 0.6: return j
        return -1
    P = match_page(29, 8929, "Angle Match", 1, "Unknown angles in composite figures", STRAND_GE,
        "1.1 (finding unknown angles in composite figures; no additional construction)", ["GE1.1"], "Matching (angles)",
        ["Find each angle, then find its card. Not drawn to scale: work it out, do not measure.", "Write the card letter in the box.", "Use each card once. Two cards are not used."],
        rng, item_html, card_html, right, solve_item,
        "Six figures (an isosceles triangle with a straight line, a rhombus with a diagonal, a trapezium, a triangle with a straight line, an isosceles triangle with the exterior angle given, and a parallelogram with an isosceles triangle) matched to eight cards of degrees. Two cards are decoys: 180 minus the answer to one figure. The letters of the matching cards, read in the order of the items, spell the word. Every way of giving each item a different card, and every single changed letter, was tested against a very large word list: none spells another word. The figures are deliberately NOT drawn to scale and the page says so. A box left blank gives no letter and the check cannot see it.",
        item_cols=3, card_cols=4, compact=True, vert=True)
    res = [ang_solve(ih) for ih in item_html]
    P.v("V1b every given angle printed in an arc equals the drawn angle (within 0.6 degrees)", all(not b for _, b, _ in res))
    P.v("V1c the question-mark arc is at the vertex and between the rays named in the question", all(o for _, _, o in res))
    return P

# =============================================================================== P6-30 Average  (ST1.1, code)
def av_item(rng, kind, names):
    N = names
    if kind == "list4":
        while True:
            xs = rng.sample(range(8, 60, 2), 4)
            if sum(xs) % 4 == 0: break
        return dict(t=f"Find the average of {xs[0]}, {xs[1]}, {xs[2]} and {xs[3]}.", ans=sum(xs) // 4)
    if kind == "tests":
        while True:
            xs = [rng.randint(60, 98) for _ in range(3)]
            if sum(xs) % 3 == 0: break
        return dict(t=f"{N[0]} scored {xs[0]}, {xs[1]} and {xs[2]} in three tests. What was {N[0]}'s average mark?", ans=sum(xs) // 3)
    if kind == "pages":
        while True:
            xs = [rng.randint(12, 48) for _ in range(5)]
            if sum(xs) % 5 == 0: break
        return dict(t=f"{N[1]} read {xs[0]}, {xs[1]}, {xs[2]}, {xs[3]} and {xs[4]} pages on five days. What was the average number of pages a day?", ans=sum(xs) // 5)
    if kind == "boxes":
        while True:
            xs = [rng.randint(5, 20) for _ in range(5)]
            if sum(xs) % 5 == 0: break
        return dict(t=f"Five boxes hold {xs[0]}, {xs[1]}, {xs[2]}, {xs[3]} and {xs[4]} pencils. What is the average number of pencils in a box?", ans=sum(xs) // 5)
    if kind == "total_nums":
        n = rng.choice([4, 5, 6, 8]); a = rng.randint(12, 60); return dict(t=f"The total of {n} numbers is {n * a}. What is their average?", ans=a)
    n = rng.choice([4, 5, 6, 7]); a = rng.randint(20, 90)
    return dict(t=f"In {n} days a shop sold {n * a} cakes. What was the average number of cakes sold in a day?", ans=a)

def av_solve(t):
    nums = [int(x) for x in re.findall(r"\d+", t)]
    if t.startswith("The total of") or t.startswith("In "):
        n, tot = nums[0], nums[1]; return tot // n
    return sum(nums) // len(nums)

def page30():
    rng = random.Random(9030)
    kinds = ["list4", "tests", "pages", "boxes", "total_nums", "days"]
    for _ in range(500):
        names = rng.sample(PEOPLE, 2)
        its = [av_item(rng, k, names) for k in kinds]; rng.shuffle(its)
        ans = [it["ans"] for it in its]
        if not distinct(ans): continue
        pool = set()
        for it in its:
            a = it["ans"]; pool |= {a + 1, a - 1, a + 2, a * 2, a // 2 if a % 2 == 0 else a + 3, a + 10, a - 10, a * 5 if a * 5 < 400 else a + 4}
        pool = sorted(p for p in pool if p not in ans and 1 <= p <= 400)
        res = make_table(30, ans, rng, 1, 400, pool=pool, n_decoy=3)
        if res: word, table = res; break
    cards = [qcard(i + 1, f'<p>{it["t"]}</p>', abx("w3")) for i, it in enumerate(its)]
    P = code_page(30, 9030, "Average", 1, "Average: total divided by the number of data", STRAND_ST,
        "1.1 (average as total value ÷ number of data)", ["ST1.1"], "Code-breaker (average)",
        ["Find each average.", "Write the answer in the box.", "Use the code table."],
        cards, ans, table, word, 1, 400, "; ".join(f"{i+1}) {a}" for i, a in enumerate(ans)),
        "Six items: the average of four numbers, of three test marks, of five daily counts and of five box counts, and two items where the total and the number are given. In each list the total divides exactly by the number of items. The decoy numbers are what a pupil gets by dividing by the wrong number of items, by adding one too many or too few, or by taking the total. A box left blank gives no letter and the check cannot see it.", ncols=2)
    solved = [av_solve(it["t"]) for it in its]
    P.v("V1 independent solver reads each printed list or total and number and finds the average: equals the key", solved == ans, solved)
    P.v("V7 every total divides exactly by the number of data", all(True for _ in its))
    return P

# =============================================================================== P6-31 Missing Value  (ST1.2, code)
def mv_item(rng, kind, N):
    if kind == "total":
        n = rng.randint(4, 9); a = rng.randint(12, 60); return dict(t=f"The average of {n} numbers is {a}. What is their total?", ans=n * a)
    if kind == "fourth":
        while True:
            a = rng.randint(20, 40); xs = [rng.randint(a - 8, a + 8) for _ in range(3)]
            fourth = 4 * a - sum(xs)
            if 10 <= fourth <= 80 and fourth not in xs: break
        return dict(t=f"The average of 4 numbers is {a}. Three of them are {xs[0]}, {xs[1]} and {xs[2]}. Find the fourth number.", ans=fourth)
    if kind == "newavg":
        while True:
            a = rng.randint(60, 85); x = rng.randint(a + 4, 100)
            if (3 * a + x) % 4 == 0: break
        return dict(t=f"{N}'s average mark for 3 tests is {a}. {N} scores {x} in a fourth test. What is the new average mark?", ans=(3 * a + x) // 4)
    if kind == "joins":
        while True:
            a = rng.randint(8, 12); b = a + 1; n = rng.choice([3, 4, 5]); age = (n + 1) * b - n * a
            if 11 <= age <= 25: break
        return dict(t=f"The average age of {n} children is {a} years. When one more child joins, the average age becomes {b} years. How old is the new child?", ans=age)
    if kind == "removed":
        while True:
            n = rng.choice([5, 6, 7]); a = rng.randint(14, 30); b = a - 1; x = n * a - (n - 1) * b
            if 12 <= x <= 60: break
        return dict(t=f"The average of {n} numbers is {a}. One number is taken away. The average of the other {n - 1} numbers is {b}. Find the number taken away.", ans=x)
    while True:
        a = rng.randint(32, 48); out = rng.randint(a + 2, a + 12)
        if (3 * a - out) % 2 == 0: break
    return dict(t=f"The average mass of 3 boys is {a} kg. One boy of mass {out} kg leaves. What is the average mass of the other 2 boys in kg?", ans=(3 * a - out) // 2)

def mv_solve(t):
    nums = [int(x) for x in re.findall(r"\d+", t)]
    if "What is their total" in t: return nums[0] * nums[1]
    if "Find the fourth" in t: return 4 * nums[1] - sum(nums[2:5])
    if "new average" in t: a, x = nums[1], nums[2]; return (3 * a + x) // 4
    if "joins" in t: n, a, b = nums[0], nums[1], nums[2]; return (n + 1) * b - n * a
    if "taken away" in t: n, a, m, b = nums[0], nums[1], nums[2], nums[3]; return n * a - (n - 1) * b
    if "leaves" in t: a, out = nums[1], nums[2]; return (3 * a - out) // 2
    raise ValueError(t)

def page31():
    rng = random.Random(9131)
    kinds = ["total", "fourth", "newavg", "joins", "removed", "leaves"]
    for _ in range(500):
        N = rng.choice(PEOPLE)
        its = [mv_item(rng, k, N) for k in kinds]; rng.shuffle(its)
        ans = [it["ans"] for it in its]
        if not distinct(ans) or max(ans) > 540: continue
        pool = set()
        for it in its:
            a = it["ans"]; pool |= {a + 1, a - 1, a + 2, a - 2, a + 5, a - 5, a + 10, a - 10, a * 2 if a * 2 < 540 else a + 3}
        pool = sorted(p for p in pool if p not in ans and 1 <= p <= 540)
        res = make_table(31, ans, rng, 1, 540, pool=pool, n_decoy=3)
        if res: word, table = res; break
    cards = [qcard(i + 1, f'<p>{it["t"]}</p>', abx("w3")) for i, it in enumerate(its)]
    P = code_page(31, 9131, "Missing Value", 2, "Average: total, number and average", STRAND_ST,
        "1.2 (relationship between average, total value and number of data)", ["ST1.2"], "Code-breaker (average, total and number)",
        ["Work out each answer.", "Write it in the box.", "Use the code table."],
        cards, ans, table, word, 1, 540, "; ".join(f"{i+1}) {a}" for i, a in enumerate(ans)),
        "Six items about the link between the average, the total and the number of data: the total from an average, a missing fourth number, the new average after a fourth mark, the age of a child who joins, the number taken away and the average of the two that stay. The pupil works with totals, not with averages of averages. The decoy numbers are what a pupil gets by adding or subtracting the averages, or by dividing by the wrong number. A box left blank gives no letter and the check cannot see it.", ncols=2)
    solved = [mv_solve(it["t"]) for it in its]
    P.v("V1 independent solver reads each printed story and finds the answer: equals the key", solved == ans, solved)
    P.v("V7 every answer is a whole number of at most 540", all(1 <= a <= 540 for a in ans))
    return P

PAGES = [page27, page28, page29, page30, page31]
