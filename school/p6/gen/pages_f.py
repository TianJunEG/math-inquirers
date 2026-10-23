"""Part F: Primary 6 Foundation pages and mixed pages. P6-33 Pie Chart, P6-37 Decimal Maze,
P6-38 GST and Discount, P6-39 Mixed Bag."""
import random, re, math, itertools
from fractions import Fraction as Fr
from math import gcd
from collections import deque
from .common import *
from .kit import *
from .kit6 import *
from . import figs as F
from .pages_b import V

# =============================================================================== P6-33 Pie Chart  (Primary 6 Foundation pie charts; percentage)
PIE_SETS = [((35, 25, 20, 15, 5), 240), ((40, 25, 15, 15, 5), 400), ((30, 25, 20, 20, 5), 200), ((45, 20, 15, 10, 10), 400)]
PIE_NAMES = ["Football", "Swimming", "Badminton", "Tennis", "Others"]

def page33():
    rng = random.Random(9333)
    for _ in range(500):
        pcts, N = rng.choice(PIE_SETS); pcts = list(pcts); rng.shuffle(pcts)
        names = PIE_NAMES[:]
        hid = rng.randrange(4)                       # a named sector, not 'Others'
        sectors = [(n, p, i == hid) for i, (n, p) in enumerate(zip(names, pcts))]
        H = names[hid]; others = [i for i in range(5) if i != hid]
        A = rng.choice([i for i in others if i != 4]); B, C = rng.sample(others, 2)
        ratio_pair = [(i, j) for i in range(5) for j in range(5) if i != j and pcts[i] % pcts[j] == 0 and pcts[i] // pcts[j] >= 2 and hid not in (i, j)]
        if not ratio_pair: continue
        R1, R2 = rng.choice(ratio_pair)
        D = rng.choice([i for i in others if i != A])
        items = [f"What percentage of the pupils chose {H}?",
                 f"How many pupils chose {names[A]}?",
                 f"How many more pupils chose {names[B]} than {names[C]}?" if pcts[B] > pcts[C] else f"How many more pupils chose {names[C]} than {names[B]}?",
                 f"How many pupils did not choose {names[D]}?",
                 f"How many pupils chose {H}?",
                 f"The number who chose {names[R1]} is how many times the number who chose {names[R2]}?"]
        ans = [pcts[hid], N * pcts[A] // 100, N * abs(pcts[B] - pcts[C]) // 100, N * (100 - pcts[D]) // 100, N * pcts[hid] // 100, pcts[R1] // pcts[R2]]
        if len(set(ans)) < 6 or any(a < 1 or a > 400 for a in ans): continue
        order = list(range(6)); rng.shuffle(order)
        items = [items[i] for i in order]; ans = [ans[i] for i in order]
        pool = set()
        for a in ans: pool |= {a + 5, a - 5, a * 2, a + 10, a - 10, a + 1, a - 1, 100 - a if a < 100 else a + 1}
        pool = sorted(p for p in pool if p not in ans and 1 <= p <= 400)
        res = make_table(33, ans, rng, 1, 400, pool=pool, n_decoy=3)
        if res: word, table = res; break
    pie = F.pie_fig(sectors, H=52.0, R=15.5)
    cards = [qcard(i + 1, f'<p>{t}</p>', abx("w3"), cls="inl") for i, t in enumerate(items)]
    head = f'<p class="lead" style="text-align:center">{N} pupils each chose their favourite sport.</p><div class="fig">{pie}</div>'
    P = code_page(33, 9333, "Pie Chart", 2, "Pie charts: reading percentages and finding amounts", STRAND_PF,
        "Primary 6 Foundation (reading and interpreting data from pie charts; finding a percentage part of a whole)", ["PF.ST", "PF.PC"], "Code-breaker (pie chart)",
        ["Read the pie chart. The sectors add up to 100%.", "Write each answer in the box. Use the code table."],
        cards, ans, table, word, 1, 400, "; ".join(f"{i+1}) {a}" for i, a in enumerate(ans)),
        "A pie chart with five sectors (percentages shown, one hidden). Six questions: the hidden percentage (the sectors add up to 100%), the number of pupils in a sector, a difference of two sectors, the number who did not choose one sport, the number in the hidden sector (which needs the first answer) and how many times one sector is another. The decoy numbers are what a pupil gets by using the percentage as the number, by adding or taking 10 or 5, or by using 100 minus the answer. A box left blank gives no letter and the check cannot see it.",
        pre_body=head, ncols=2, cols=5)
    def solve():
        pm = F.read_pie(pie); out = []
        for t in items:
            def pct(name): return round(pm[name][0])
            if t.startswith("What percentage"): out.append(pct(re.search(r"chose (\w+)\?", t).group(1)))
            elif t.startswith("How many pupils chose"): out.append(N * pct(re.search(r"chose (\w+)\?", t).group(1)) // 100)
            elif "more pupils" in t:
                a, b = re.search(r"chose (\w+) than (\w+)\?", t).groups(); out.append(N * (pct(a) - pct(b)) // 100)
            elif "did not choose" in t: out.append(N * (100 - pct(re.search(r"choose (\w+)\?", t).group(1))) // 100)
            else:
                a, b = re.search(r"chose (\w+) is how many times the number who chose (\w+)\?", t).groups(); out.append(pct(a) // pct(b))
        return out
    P.v("V1 independent solver measures each sector of the printed pie chart from its end points and answers every printed question: equals the key", solve() == ans, solve())
    pm = F.read_pie(pie)
    P.v("V1b the four printed percentages agree with the drawn sectors, and all five sectors add up to 100%", all(lab is None or abs(m - lab) < 0.1 for m, lab in pm.values()) and abs(sum(m for m, _ in pm.values()) - 100) < 0.1, pm)
    P.v("V7 every answer is a whole number of at most 400", all(1 <= a <= 400 for a in ans))
    return P

# =============================================================================== P6-37 Decimal Maze  (Primary 6 Foundation decimals, route)
def dtxt(x):
    return dec(Fr(x))

def dec_cells(T):
    good, bad = set(), set()
    def add(v, h): (good if v == T else bad).add(h)
    for k in range(2, 11):
        for a in [Fr(x, 100) for x in range(5, 1500, 5)]:
            if a.denominator <= 100 and a * k <= 40: add(a * k, f"{dtxt(a)} × {k}")
    for k in range(2, 11):
        for a in [Fr(x, 10) for x in range(2, 400, 2)]:
            add(a / k, f"{dtxt(a)} ÷ {k}")
    for a in [Fr(x, 20) for x in range(1, 80)]:
        for b in [Fr(x, 20) for x in range(1, 80)]:
            if a.denominator <= 20 and b.denominator <= 20 and abs(a + b - T) <= 1 and a >= b:
                add(a + b, f"{dtxt(a)} + {dtxt(b)}"); add(a - b, f"{dtxt(a)} − {dtxt(b)}")
    for a in (T, T / 10, T * 10, T / 100, T * 100, Fr(24, 100) * 1, Fr(204, 100), Fr(25, 10), Fr(23, 10), Fr(3, 10)):
        for m, op in ((10, "×"), (100, "×"), (10, "÷"), (100, "÷")):
            v = a * m if op == "×" else a / m
            if abs(v - T) < 3 or v in (T,): add(v, f"{dtxt(a)} {op} {m}")
    return sorted(good), sorted(bad)

def page37():
    rng = random.Random(9737)
    T = Fr(12, 5)
    good, bad = dec_cells(T)
    good = [g for g in good if len(g) <= 12]; bad = [b for b in bad if len(b) <= 12]
    rng.shuffle(bad); rng.shuffle(good)
    ten = [b for b in bad if calc(ptxt(b)) in (T * 10, T / 10)]
    good = good[:60]; bad = bad[:120]
    must = [ten] if ten else []
    return route_page(37, 9737, "Decimal Maze", 1, "Decimals: adding, subtracting, multiplying and dividing", STRAND_PF,
        "Primary 6 Foundation (multiplying and dividing decimals)", ["PF.DE"], "Maze / path",
        ["Start at START. Move up, down, left or right.", f"Step only on boxes where the answer is {dtxt(T)}.", "Do not step on a box twice."],
        rng, 4, 8, good, bad, lambda h: calc(ptxt(h)), T, dtxt(T),
        f"A 4 by 4 grid of sixteen decimal sums: adding, subtracting, multiplying by a whole number, dividing by a whole number, and multiplying or dividing by 10 or 100. The route follows the boxes that equal {dtxt(T)}. The wrong boxes have answers close to {dtxt(T)}, such as a value ten times too big or too small, which a pupil gets by misplacing the decimal point. Two extra boxes that equal {dtxt(T)} are dead ends. Counting the boxes shows a line that takes a shortcut.",
        cls="maze sm tall", must=must)

# =============================================================================== P6-38 GST and Discount  (Primary 6 Foundation percentage)
def gd_item(rng, kind, N):
    if kind == "with_gst":
        p = rng.choice([100, 200, 300, 400, 500, 600]); return dict(t=f"A bag costs ${p} before GST. What is the price with GST?", ans=p * 109 // 100)
    if kind == "sale":
        p, d = rng.choice([(80, 15), (60, 25), (120, 30), (150, 20), (240, 25), (90, 10)]); return dict(t=f"A shirt costs ${p}. It is sold at a {d}% discount. What is the sale price?", ans=p * (100 - d) // 100)
    if kind == "gst":
        p = rng.choice([100, 200, 300, 400, 500, 700, 800]); return dict(t=f"A TV costs ${p} before GST. How much is the GST?", ans=p * 9 // 100)
    if kind == "interest":
        p, r = rng.choice([(500, 2), (800, 3), (400, 5), (1000, 2), (600, 4), (300, 5)]); return dict(t=f"{N} puts ${p} in a bank. The annual interest rate is {r}%. How much interest does {N} get in 1 year?", ans=p * r // 100)
    if kind == "discount":
        p, d = rng.choice([(150, 20), (250, 12), (320, 25), (480, 15), (350, 40), (180, 30)]); return dict(t=f"A jacket costs ${p}. The discount is {d}%. How much money is the discount?", ans=p * d // 100)
    p, d = rng.choice([(300, 20), (400, 20), (150, 25), (270, 10), (360, 10), (210, 30)]); return dict(t=f"A phone costs ${p} after a {d}% discount. How much money was the discount?", ans=p * 100 // (100 - d) - p)

def gd_solve(t):
    t = ptxt(t); n = [int(x) for x in re.findall(r"\d+", t)]
    if "with GST" in t: return n[0] * 109 // 100
    if "sale price" in t: return n[0] * (100 - n[1]) // 100
    if "How much is the GST" in t: return n[0] * 9 // 100
    if "interest" in t: return n[0] * n[1] // 100
    if "after a" in t: return n[0] * 100 // (100 - n[1]) - n[0]
    return n[0] * n[1] // 100

def page38():
    rng = random.Random(9838)
    kinds = ["with_gst", "sale", "gst", "interest", "discount", "usual"]
    for _ in range(500):
        N = rng.choice(PEOPLE)
        its = [gd_item(rng, k, N) for k in kinds]; rng.shuffle(its)
        ans = [it["ans"] for it in its]
        if not distinct(ans) or max(ans) > 1000: continue
        pool = set()
        for it in its:
            a = it["ans"]; pool |= {a + 9, a - 9, a + 10, a - 10, a * 10, a + 1, a - 1, a + 50, a - 5}
        pool = sorted(p for p in pool if p not in ans and 1 <= p <= 1000)
        res = make_table(38, ans, rng, 1, 1000, pool=pool, n_decoy=3)
        if res: word, table = res; break
    cards = [qcard(i + 1, f'<p>{it["t"]}</p>', f'{unit("$")}{abx("w3")}') for i, it in enumerate(its)]
    P = code_page(38, 9838, "GST and Discount", 1, "Percentage: GST, discount and interest", STRAND_PF,
        "Primary 6 Foundation (finding a percentage part of a whole; finding discount, GST and annual interest)", ["PF.PC"], "Code-breaker (GST, discount, interest)",
        ["GST is 9%.", "Work out each amount in dollars.", "Write it in the box. Use the code table."],
        cards, ans, table, word, 1, 1000, "; ".join(f"{i+1}) ${a}" for i, a in enumerate(ans)),
        "Six items on percentage in money: the price with GST, a sale price after a discount, the amount of GST, a year's interest, the amount of a discount, and a discount found from the usual price and the price after it. The GST rate used is 9% and is printed on the page; the teacher may change it if the rate changes. The decoy numbers are what a pupil gets by adding 9 or 10 instead of 9%, by giving the discount instead of the sale price (or the reverse), or by being ten times out. A box left blank gives no letter and the check cannot see it.", ncols=2)
    solved = [gd_solve(it["t"]) for it in its]
    P.v("V1 independent solver reads each printed money question and finds the answer: equals the key", solved == ans, solved)
    P.v("V7 every amount is a whole number of dollars and at most $1000", all(1 <= a <= 1000 for a in ans))
    return P

# =============================================================================== P6-39 Mixed Bag  (spiral revision, domino loop)
def mix_half(rng, u, used, kinds):
    for _ in range(2000):
        k = rng.choice(kinds)
        if k == "pct":
            p = rng.choice([10, 20, 25, 40, 50, 60, 75]); N = Fr(100 * u, p)
            if N.denominator != 1 or not 20 <= N <= 480: continue
            h = f"{p}% of {int(N)}"
        elif k == "fdiv":
            if u > 12: continue
            d = rng.choice([2, 3, 4, 5, 6, 8]); n = rng.randint(1, d - 1)
            if gcd(n, d) != 1: continue
            dv = Fr(u) * Fr(n, d)
            if dv.denominator == 1 and 1 <= dv <= 12: h = f"{int(dv)} ÷ {fh(n, d)}"
            elif dv < 1 and dv.denominator <= 12: h = f"{fh(dv.numerator, dv.denominator)} ÷ {fh(n, d)}"
            else: continue
        elif k == "avg":
            a = rng.randint(max(1, u - 15), u); b = rng.randint(max(1, u - 12), u + 12); c = 3 * u - a - b
            if c < 1 or len({a, b, c}) < 3: continue
            h = f"average of {a}, {b} and {c}"
        elif k == "share":
            a, b = rng.sample(range(1, 8), 2)
            if gcd(a, b) != 1: continue
            big = max(a, b); N = Fr(u * (a + b), big)
            if N.denominator != 1 or N > 500: continue
            h = f"larger share of {int(N)} in the ratio {a}\u00a0:\u00a0{b}"
        elif k == "root":
            if u < 4 or u > 30: continue
            r = rng.choice([("√", 2), ("∛", 3)]); m = rng.randint(1, u - 1)
            base = (u - m) ** r[1]
            if base > 1000: continue
            h = f"{SY(r[0]) if False else r[0]}{base} + {m}"
        elif k == "subst":
            L = rng.choice(["a", "n", "p", "k", "t", "w"]); x = rng.randint(2, 9); m = rng.randint(2, 9); c = u - m * x
            if not 1 <= c <= 30: continue
            h = f'<span class="ex">{m}{V(L)} + {c}</span><span class="wh">when {V(L)} = {x}</span>'
        else:
            l, b, hh = rng.randint(2, 12), rng.randint(2, 10), rng.randint(2, 10)
            if l * b * hh != u: continue
            h = f"volume of a cuboid {l} cm by {b} cm by {hh} cm"
        if h not in used: return h, k
    return None

def ev_mix(h):
    t = ptxt(h)
    m = re.fullmatch(r"(\d+)% of (\d+)", t)
    if m: return Fr(int(m.group(1)) * int(m.group(2)), 100)
    m = re.fullmatch(r"average of (\d+), (\d+) and (\d+)", t)
    if m: return Fr(sum(int(x) for x in m.groups()), 3)
    m = re.fullmatch(r"larger share of (\d+) in the ratio (\d+) : (\d+)", t)
    if m: N, a, b = map(int, m.groups()); return Fr(N * max(a, b), a + b)
    m = re.fullmatch(r"volume of a cuboid (\d+) cm by (\d+) cm by (\d+) cm", t)
    if m: a, b, c = map(int, m.groups()); return Fr(a * b * c)
    m = re.fullmatch(r"(.*) when ([a-z]) = (\d+)", t)
    if m: return calc(m.group(1), {m.group(2): int(m.group(3))})
    return calc(t)

def page39():
    rng = random.Random(9939)
    kinds = ["pct", "fdiv", "avg", "share", "root", "subst", "vol"]
    for _ in range(300):
        vals = rng.sample(range(4, 61), 6)
        used = set(); halves = []; ok = True; seen_kinds = []
        for k in range(6):
            a = mix_half(rng, vals[k], used, kinds)
            if a is None: ok = False; break
            used.add(a[0]); seen_kinds.append(a[1])
            b = mix_half(rng, vals[(k + 1) % 6], used, kinds)
            if b is None: ok = False; break
            used.add(b[0]); seen_kinds.append(b[1]); halves.append((a[0], b[0]))
        if ok and len(set(seen_kinds)) >= 6 and "fdiv" in seen_kinds: break
    P = loop_page(39, 9939, "Mixed Bag", 2, "Mixed practice: percentages, fractions, ratio, average, roots, letters and volume", STRAND_PF,
        "Mixed practice: Fractions 1.2, Ratio 1.3, Algebra 1.4, Statistics 1.1, Volume 2.5 and Primary 6 Foundation percentage and volume", ["FR1.2", "RA1.3", "AL1.4", "ST1.1", "VO2.5", "PF.PC", "PF.VO"], "Domino loop (mixed)",
        ["Work out the value of each half domino.", "The right half of a domino has the same value as the left half of the next domino.", "Write the letters in order, from START."],
        rng, halves, ev_mix,
        "Six dominoes with twelve halves. Each half is a short question with a whole-number answer: a percentage of a number, a fraction divided by a fraction, an average of three numbers, a larger share in a ratio, a root with a number added, an expression with a letter, or the volume of a cuboid. The right half of one domino has the same value as the left half of exactly one other domino, so the dominoes make one loop that comes back to START. The pupil finds the value of each half, follows the loop from START and writes the letters in loop order; they spell the word. Every wrong order was tested against a very large word list: none spells a word.", ps=True)
    return P

PAGES = [page33, page37, page38, page39]
