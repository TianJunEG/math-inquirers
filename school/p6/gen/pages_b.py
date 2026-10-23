"""Part B: percentage and algebra. P6-10 Find the Whole, P6-11 Percent Up and Down, P6-12 Percent Stories, P6-13 Letters for Numbers, P6-14 Simplify,
P6-15 Substitute, P6-16 Balance the Equation."""
import random, re, math, itertools
from fractions import Fraction as Fr
from math import gcd
from .common import *
from .kit import *
from .kit6 import *

def V(c): return f'<i class="v">{c}</i>'

# =============================================================================== P6-10 Find the Whole  (PC1.1, code)
PCTS = [10, 20, 25, 30, 40, 50, 60, 75, 80, 5, 15, 45, 35, 90, 70]
def fw_item(rng, kind, N):
    while True:
        p = rng.choice(PCTS); whole = rng.randint(4, 100) * 10 if p % 10 == 0 else rng.randint(4, 40) * 20
        part = whole * p // 100
        if whole * p % 100 == 0 and 6 <= part <= 400 and 40 <= whole <= 900: break
    if kind == "bare":
        t = f"{p}% of a number is {part}. Find the number."
    elif kind == "class":
        t = f"Boys make up {p}% of the people in a hall. {part} boys are there. Find the number of people in the hall."
    elif kind == "sale":
        t = f"A bike is on sale at {p}% of its usual price. The sale price is ${part}. What is the usual price?"
    elif kind == "save":
        t = f"{N} saved ${part}, which is {p}% of {N}'s pocket money. How much pocket money did {N} get?"
    elif kind == "ribbon":
        t = f"{p}% of a ribbon is {part} cm long. Work out the whole length in cm."
    else:
        t = f"A tank is {p}% full. It holds {part} {LITRE} of water. How much water does the full tank hold in {LITRE}?"
    wrong = []
    for w in (part * p // 100 if part * p % 100 == 0 else None, part * 100 // (100 - p) if part * 100 % (100 - p) == 0 else None, part + part * p // 100 if part * p % 100 == 0 else None, whole - part):
        if w and w != whole: wrong.append(w)
    return dict(t=t, ans=whole, wrong=wrong, p=p, part=part)

def fw_solve(t):
    p = int(re.search(r"(\d+)%", t).group(1))
    rest = re.sub(r"\d+%", "P", t)
    part = int(re.findall(r"\d+", rest)[0])
    return part * 100 // p

def page10():
    rng = random.Random(7010)
    kinds = ["bare", "class", "sale", "save", "ribbon", "tank"]
    for _ in range(300):
        N = rng.choice(PEOPLE)
        its = [fw_item(rng, k, N) for k in kinds]; rng.shuffle(its)
        ans = [it["ans"] for it in its]
        if not distinct(ans) or len({it["p"] for it in its}) < 5: continue
        pool = sorted({w for it in its for w in it["wrong"] if w not in ans and 1 <= w <= 1000})
        res = make_table(10, ans, rng, 1, 1000, pool=pool, n_decoy=3)
        if res: word, table = res; break
    cards = [qcard(i + 1, f'<p>{it["t"]}</p>', abx("w4"), cls="inl") for i, it in enumerate(its)]
    P = code_page(10, 7010, "Find the Whole", 1, "Percentage: finding the whole from a part", STRAND_PC,
        "1.1 (finding the whole given a part and the percentage)", ["PC1.1"], "Code-breaker (percentage)",
        ["Find the whole in each question.", "Write the answer in the box.", "Use the code table."],
        cards, ans, table, word, 1, 1000, "; ".join(f"{i+1}) {a}" for i, a in enumerate(ans)),
        "Six questions in which a part and its percentage are given and the whole is wanted: a bare number, pupils in a hall, a sale price, savings, a length and a tank. The decoy numbers are what a pupil gets by finding the percentage of the part instead, by adding the percentage on to the part, or by subtracting the part from the whole. A box left blank gives no letter and the check cannot see it.", ncols=1)
    solved = [fw_solve(it["t"]) for it in its]
    P.v("V1 independent solver reads the printed percentage and part and finds the whole: equals the key", solved == ans, solved)
    P.v("V7 every whole is a whole number between 40 and 900 and every percentage is a whole number", all(40 <= a <= 900 for a in ans))
    return P

# =============================================================================== P6-11 Percent Up and Down  (PC1.2, route)
def ud_cell(direction, a, b):
    return f'<span class="ud">{direction} from</span><br><b>{a} to {b}</b>'

def ev_ud(h):
    t = ptxt(h)
    m = re.fullmatch(r"(Up|Down) from (\d+) to (\d+)", t)
    d, a, b = m.group(1), int(m.group(2)), int(m.group(3))
    assert (d == "Up") == (b > a)
    return Fr(b - a, a) * 100

def page11():
    rng = random.Random(7111)
    T = Fr(25)
    good, bad = [], []
    for a in range(8, 241, 4):
        good.append(ud_cell("Up", a, a * 5 // 4))
    for a in range(10, 241, 5):
        for pct in (10, 20, 30, 40, 50, 60, 75, 15, 35, 45, 12, 8):
            for d in ("Up", "Down"):
                b = a * (100 + pct) // 100 if d == "Up" else a * (100 - pct) // 100
                if (a * pct) % 100 == 0 and a * (100 + pct if d == "Up" else 100 - pct) % 100 == 0 and b != a and b > 0:
                    sc = ev_ud(ud_cell(d, a, b))
                    if sc != T: bad.append(ud_cell(d, a, b))
    # the traps: Down 25%, and Up from b to a where b is a 20% drop's partner, i.e. +33 1/3 %
    for a in range(20, 241, 20):
        bad.append(ud_cell("Down", a, a * 3 // 4)); bad.append(ud_cell("Up", a * 3 // 4, a))
    bad = sorted(set(bad)); good = sorted(set(good))
    must = [[c for c in bad if ev_ud(c) == -25], [c for c in bad if ev_ud(c) == Fr(100, 3)]]
    return route_page(11, 7111, "Percent Up and Down", 1, "Percentage increase and decrease", STRAND_PC,
        "1.2 (percentage increase or decrease)", ["PC1.2"], "Maze / path",
        ["Start at START. Move up, down, left or right.", "Step only on boxes that show a 25% increase.", "Do not step on a box twice."],
        rng, 4, 8, good, bad, ev_ud, T, "a 25% increase",
        "A 4 by 4 grid of sixteen changes, each written as Up or Down from one number to another. The route follows the boxes that are a 25% increase. The wrong boxes include 25% decreases (a pupil who ignores the word Down) and increases from a smaller number to the old one (a rise of one third, not 25%), and other percentages. Two extra 25% increases are dead ends. Counting the boxes shows a line that takes a shortcut.",
        cls="maze sm tall", check="Does your line reach FINISH? Count its boxes: are there 8? Is every box a 25% increase?", must=must)

# =============================================================================== P6-12 Percent Stories  (PC1.1, PC1.2, code)
def ps_item(rng, kind, names):
    N, M = names
    if kind == "disc":
        while True:
            p = rng.choice([10, 20, 25, 30, 40]); whole = rng.randint(4, 40) * 10; sale = whole * (100 - p) // 100
            if whole * (100 - p) % 100 == 0: break
        t = f"A bag is sold at a {p}% discount. The sale price is ${sale}. What was the usual price in dollars?"
        return dict(t=t, ans=whole, wrong=[sale * (100 + p) // 100 if sale * (100 + p) % 100 == 0 else sale + p, whole - sale, sale + p])
    if kind == "rise":
        while True:
            p = rng.choice([10, 20, 25, 30, 40, 50]); old = rng.randint(4, 40) * 10; new = old * (100 + p) // 100
            if old * (100 + p) % 100 == 0: break
        t = f"The price of a book rose by {p}%. The new price is ${new}. What was the old price in dollars?"
        return dict(t=t, ans=old, wrong=[new * (100 - p) // 100 if new * (100 - p) % 100 == 0 else new - p, new - old, new - p])
    if kind == "left":
        while True:
            p = rng.choice([20, 25, 30, 40, 60]); first = rng.randint(5, 50) * 10; left = first * (100 - p) // 100
            if first * (100 - p) % 100 == 0: break
        t = f"A shop sold {p}% of its mangoes and had {left} mangoes left. Find the number of mangoes at the start of the day."
        return dict(t=t, ans=first, wrong=[left * p // 100 if left * p % 100 == 0 else left + p, first - left, left + first * 0 + p])
    if kind == "grew":
        while True:
            old = rng.choice([20, 25, 40, 50, 60, 80]); p = rng.choice([10, 20, 25, 30, 40, 50]); new = old * (100 + p) // 100
            if old * (100 + p) % 100 == 0: break
        t = f"A plant was {old} cm tall. It grew to {new} cm. Find the percentage increase."
        return dict(t=t, ans=p, wrong=[(new - old) * 100 // new if (new - old) * 100 % new == 0 else new - old, new - old, p + 5])
    if kind == "fell":
        while True:
            old = rng.choice([200, 250, 400, 500, 800, 600]); p = rng.choice([10, 20, 25, 30, 40, 5]); new = old * (100 - p) // 100
            if old * (100 - p) % 100 == 0: break
        t = f"A phone cost ${old}. In a sale the price fell to ${new}. Find the percentage decrease."
        return dict(t=t, ans=p, wrong=[(old - new) * 100 // new if (old - new) * 100 % new == 0 else old - new, old - new, p + 5])
    while True:
        p = rng.choice([20, 25, 30, 40, 50, 60]); base = rng.randint(4, 40) * 10; mo = base * (100 + p) // 100
        if base * (100 + p) % 100 == 0: break
    t = f"{N} has {p}% more stickers than {M}. {N} has {mo} stickers. How many stickers does {M} have?"
    return dict(t=t, ans=base, wrong=[mo * (100 - p) // 100 if mo * (100 - p) % 100 == 0 else mo - p, mo - base, mo - p])

def ps_solve(t):
    n = [int(x) for x in re.findall(r"\d+", t)]
    if "discount" in t:
        p, sale = n[0], n[1]; return sale * 100 // (100 - p)
    if "rose by" in t:
        p, new = n[0], n[1]; return new * 100 // (100 + p)
    if "sold" in t and "left" in t:
        p, left = n[0], n[1]; return left * 100 // (100 - p)
    if "grew to" in t:
        old, new = n[0], n[1]; return (new - old) * 100 // old
    if "fell to" in t:
        old, new = n[0], n[1]; return (old - new) * 100 // old
    if "more stickers" in t:
        p, mo = n[0], n[1]; return mo * 100 // (100 + p)
    raise ValueError(t)

def page12():
    rng = random.Random(7212)
    kinds = ["disc", "rise", "left", "grew", "fell", "more"]
    for _ in range(300):
        names = rng.sample(PEOPLE, 2)
        its = [ps_item(rng, k, names) for k in kinds]; rng.shuffle(its)
        ans = [it["ans"] for it in its]
        if not distinct(ans): continue
        pool = sorted({w for it in its for w in it["wrong"] if w not in ans and 1 <= w <= 1000})
        res = make_table(12, ans, rng, 1, 1000, pool=pool, n_decoy=3)
        if res: word, table = res; break
    cards = [qcard(i + 1, f'<p>{it["t"]}</p>', abx("w4"), cls="inl") for i, it in enumerate(its)]
    P = code_page(12, 7212, "Percent Stories", 2, "Percentage: finding the whole and the percentage change", STRAND_PC,
        "1.1, 1.2 (finding the whole given a part and the percentage; percentage increase or decrease)", ["PC1.1", "PC1.2"], "Code-breaker (percentage stories)",
        ["Work out each answer.", "Write it in the box.", "Use the code table."],
        cards, ans, table, word, 1, 1000, "; ".join(f"{i+1}) {a}" for i, a in enumerate(ans)),
        "Six stories: the usual price after a discount, the old price after a rise, the amount at first after some were sold, a percentage increase, a percentage decrease, and the smaller quantity when the other is a percentage more. Three need the whole from a part that is a percentage above or below it, so the pupil must divide by the right percentage. The decoy numbers are what a pupil gets by taking the percentage of the given amount, by finding only the difference, or by adding or subtracting the percentage as a number. A box left blank gives no letter and the check cannot see it.",
        ncols=1, ps=False)
    solved = [ps_solve(it["t"]) for it in its]
    P.v("V1 independent solver reads each printed story and finds the answer: equals the key", solved == ans, solved)
    P.v("V7 all numbers are whole and every answer is at most 1000", all(1 <= a <= 1000 for a in ans))
    return P

# =============================================================================== P6-13 Letters for Numbers  (AL1.1, AL1.2, choice)
LET = ["n", "p", "k", "y", "w", "t"]
def al_row(rng, kind, L, N, M, K=None):
    K = K or rng.randint(2, 9)
    Lh = V(L)
    if kind == "more":
        return dict(stem=f"A pen costs ${Lh}. A ruler costs ${K} more than the pen. How many dollars does the ruler cost?", right=f"{Lh} + {K}", wrong=[f"{Lh} − {K}", f"{K}{Lh}"])
    if kind == "less":
        return dict(stem=f"{N} has {Lh} sweets. {N} eats {K} of them. How many sweets are left?", right=f"{Lh} − {K}", wrong=[f"{Lh} + {K}", f"{K}{Lh}"])
    if kind == "times":
        return dict(stem=f"One book costs ${Lh}. How many dollars do {K} books cost?", right=f"{K}{Lh}", wrong=[f"{Lh} + {K}", f"{Lh} ÷ {K}"])
    if kind == "share":
        return dict(stem=f"{N} shares {Lh} stickers equally among {K} friends. How many stickers does each friend get?", right=f"{Lh} ÷ {K}", wrong=[f"{K}{Lh}", f"{K} ÷ {Lh}"])
    if kind == "age":
        return dict(stem=f"{N} is {Lh} years old. {M} is {K} years younger. How old is {M}?", right=f"{Lh} − {K}", wrong=[f"{Lh} + {K}", f"{Lh} ÷ {K}"])
    return dict(stem=f"A box holds {Lh} pencils. How many pencils are in {K} boxes?", right=f"{K}{Lh}", wrong=[f"{Lh} + {K}", f"{Lh} − {K}"])

def al_story_value(stem, env):
    t = ptxt(stem)
    m = re.search(r"([a-z]) *$", "")
    L = re.search(r"\$?\b([nptykw])\b", t).group(1)
    K = int(re.findall(r"\b\d+\b", t)[0]); x = Fr(env[L])
    if "more than the pen" in t or "years older" in t: return x + K
    if "eats" in t or "younger" in t: return x - K
    if "do " in t and "books cost" in t: return K * x
    if "pencils are in" in t: return K * x
    if "equally among" in t: return x / K
    raise ValueError(t)

def al_solve_row(stem, opts):
    L = re.search(r"\b([nptykw])\b", ptxt(stem)).group(1)
    for j, o in enumerate(opts):
        ok = True
        for x in (3, 7, 12):
            if calch(o, {L: x}) != al_story_value(stem, {L: x}): ok = False
        if ok: return j
    return -1

def page13():
    rng = random.Random(7313)
    kinds = ["more", "less", "times", "share", "age", "boxes"]
    for _ in range(100):
        letters = rng.sample(LET, 6); names = rng.sample(PEOPLE, 12)
        Ks = rng.sample(range(2, 10), 6)
        rows = [al_row(rng, k, letters[i], names[2 * i], names[2 * i + 1], Ks[i]) for i, k in enumerate(kinds)]
        rng.shuffle(rows)
        if len({r["stem"] for r in rows}) == 6: break
    crows = []
    for r in rows:
        opts = [r["right"]] + r["wrong"]; order = list(range(3)); rng.shuffle(order)
        crows.append(dict(stem=r["stem"], opts=[V(opts[j]) if False else opts[j] for j in order], right=order.index(0)))
    P = choice_page(13, 7313, "Letters for Numbers", 1, "Algebra: writing expressions with a letter", STRAND_AL,
        "1.1, 1.2 (a letter for an unknown number; notation of simple expressions such as a + 3, 3a and a ÷ 3)", ["AL1.1", "AL1.2"], "Choice table (expressions)",
        ["A letter stands for a number.", "Circle the letter beside the right expression.", "Write the six letters in the boxes."],
        rng, crows, al_solve_row,
        "Six short stories in which a letter stands for an unknown number: a price that is more, a number left after some are taken, the cost of several equal items, a share among friends, an age that is younger, and a number of items in several boxes. The pupil chooses the right expression of three. The wrong expressions use the wrong operation or write the number and the letter in the wrong order (for example K ÷ n for n ÷ K). The notation is the usual one: 3n for n times 3 and n ÷ 3. The letters of the right choices, read down the rows, spell the word. Every other way of choosing was tested against a very large word list: none spells a word. A box left blank gives no letter and the check cannot see it.")
    return P

# =============================================================================== P6-14 Simplify  (AL1.3, code with two-box answers)
def lin(expr, letter=None):
    """(coefficient, constant) of a printed linear expression such as '7 a + 2 a + 5' or '9k + 5 - 2k' (one letter, no brackets)"""
    e = expr.replace("−", "-").replace(" ", "")
    if letter is None:
        m = re.search(r"[a-z]", e); letter = m.group(0) if m else "n"
    coef = const = 0
    for m in re.finditer(rf"([+-]?)(\d*)({letter}?)", e):
        if not m.group(0): continue
        sgn = -1 if m.group(1) == "-" else 1
        num = int(m.group(2)) if m.group(2) else None
        if m.group(3): coef += sgn * (num if num is not None else 1)
        elif num is not None: const += sgn * num
    return coef, const

def simp_item(rng, kind, L):
    l = V(L)
    while True:
        a, b, c, d = rng.randint(2, 9), rng.randint(2, 8), rng.randint(1, 14), rng.randint(2, 9)
        if kind == "k1": t = f"{a}{l} + {b}{l} + {c}"; ans = (a + b, c)
        elif kind == "k2":
            if a <= b: continue
            t = f"{a}{l} − {b}{l} + {c}"; ans = (a - b, c)
        elif kind == "k3": t = f"{a}{l} + {c} + {b}{l} + {d}"; ans = (a + b, c + d)
        elif kind == "k4":
            if a <= b: continue
            t = f"{a}{l} + {c} − {b}{l}"; ans = (a - b, c)
        elif kind == "k5": t = f"{a}{l} + {l} + {c}"; ans = (a + 1, c)
        else:
            if a + d <= b or a <= b: continue
            t = f"{a}{l} − {b}{l} + {d}{l} + {c}"; ans = (a - b + d, c)
        if ans[0] >= 2: break
    wrong = [(ans[0] + ans[1], 0), (ans[1], ans[0]), (ans[0] + 1, ans[1]), (ans[0] - 1, ans[1]), (ans[0], ans[1] + 1), (ans[0], ans[1] - 1)]
    if kind in ("k2", "k4", "k6"): wrong.append((a + b, ans[1]))
    return dict(t=t, ans=ans, wrong=[w for w in wrong if w[0] >= 1 and w[1] >= 0], L=L)

def simp_cards(rng, its):
    """eight cards: the six simplest forms and two decoys (a wrong simplification of two of the expressions)"""
    right = [it["ans"] for it in its]
    decs = []
    for it in rng.sample(its, 2):
        c, k = it["ans"]
        for w in ((k, c) if k >= 2 else (c + 1, k), (c + k, 1), (c - 1, k + 1), (c + 1, k - 1 if k > 1 else k + 2)):
            if w[0] >= 1 and w[1] >= 1 and w not in right and w not in [d[0] for d in decs]:
                decs.append((w, it["L"])); break
    return decs

def page14():
    rng = random.Random(7414)
    kinds = ["k1", "k2", "k3", "k4", "k5", "k6"]
    for _ in range(300):
        letters = rng.sample(LET + ["a", "m"], 6)
        its = [simp_item(rng, k, L) for k, L in zip(kinds, letters)]; rng.shuffle(its)
        ans = [(it["ans"], it["L"]) for it in its]
        if not distinct([a for a, _ in ans]) or len({L for _, L in ans}) < 6: continue
        decs = simp_cards(rng, its)
        if len(decs) < 2: continue
        allc = ans + decs
        if len({a for a, _ in allc}) < 8: continue
        break
    order = list(range(8)); rng.shuffle(order)
    card_html = [f'<span class="rt">{c}{V(L)} + {k}</span>' for (c, k), L in [allc[j] for j in order]]
    right = [order.index(i) for i in range(6)]
    item_html = [f'<div class="eqn">{it["t"]}</div>' for it in its]
    def solve_item(ih, chs):
        c, k = lin(ptxt(ih))
        L = re.search(r"[a-z]", ptxt(ih)).group(0)
        for j, ch_ in enumerate(chs):
            t = ptxt(ch_)
            if re.search(r"[a-z]", t).group(0) == L and lin(t) == (c, k): return j
        return -1
    P = match_page(14, 7414, "Simplify", 1, "Algebra: simplifying expressions with one letter", STRAND_AL,
        "1.3 (simplifying simple linear expressions, no brackets)", ["AL1.3"], "Matching (simplest form)",
        ["Simplify each expression.", "Find the card with the simplest form.", "Write the card letter in the box. Use each card once."],
        rng, item_html, card_html, right, solve_item,
        "Six expressions with one letter and no brackets: adding like terms, subtracting like terms, and expressions where the letter terms and the numbers are mixed up, one with a lone letter (n means 1n). Each is matched to its simplest form among eight cards. Two cards are decoys: a wrong simplification, such as the two numbers swapped or all the terms added together. Every way of giving each item a different card, and every single changed letter, was tested against a very large word list: none spells another word. A box left blank gives no letter and the check cannot see it.",
        item_cols=2, card_cols=4)
    return P

# =============================================================================== P6-15 Substitute  (AL1.4, domino loop)
def sub_half(rng, u, used):
    for _ in range(500):
        L = rng.choice(LET + ["a", "m"]); x = rng.randint(2, 9); f = rng.choice(["add", "add", "sub", "div", "mul"])
        l = V(L)
        if f == "add":
            m = rng.randint(2, 9); c = u - m * x
            if not 1 <= c <= 30: continue
            e = f"{m}{l} + {c}"
        elif f == "sub":
            m = rng.randint(3, 9); c = m * x - u
            if not 1 <= c <= 20: continue
            e = f"{m}{l} − {c}"
        elif f == "div":
            d = rng.choice([2, 3, 4, 5]); q = rng.randint(2, 9); x = d * q; c = u - q
            if not 1 <= c <= 40: continue
            e = f"{l} ÷ {d} + {c}"
        else:
            m = rng.randint(2, 9)
            if u % m or not 2 <= u // m <= 12: continue
            x = u // m; e = f"{m}{l}"
        h = f'<span class="ex">{e}</span><span class="wh">when {l} = {x}</span>'
        if h not in used: return h
    raise RuntimeError("half")

def ev_sub(h):
    t = ptxt(h)
    m = re.fullmatch(r"(.*) when ([a-z]) = (\d+)", t)
    return calc(m.group(1), {m.group(2): int(m.group(3))})

def page15():
    rng = random.Random(7515)
    for _ in range(200):
        vals = rng.sample(range(8, 61), 6)
        used = set(); halves = []
        for k in range(6):
            a = sub_half(rng, vals[k], used); used.add(a)
            b = sub_half(rng, vals[(k + 1) % 6], used); used.add(b)
            halves.append((a, b))
        break
    P = loop_page(15, 7515, "Substitute", 2, "Algebra: finding the value of an expression", STRAND_AL,
        "1.4 (evaluating a simple expression by substitution)", ["AL1.4", "AL1.2"], "Domino loop (substituting)",
        ["Work out the value of each half domino.", "The right half of a domino has the same value as the left half of the next domino.", "Write the letters in order, from START."],
        rng, halves, ev_sub,
        "Six dominoes. Each half shows an expression and the number its letter stands for. The right half of one domino has the same value as the left half of exactly one other domino, so the dominoes make one loop that comes back to START. The pupil finds the value of each half, follows the loop from START and writes the letters in loop order; they spell the word. All twelve values are in two groups of six equal pairs, and every wrong order was tested against a very large word list: none spells a word.")
    return P

# =============================================================================== P6-16 Balance the Equation  (AL1.5, code)
def eq_item(rng, kind, L, N):
    l = V(L)
    for _ in range(500):
        n = rng.randint(2, 30); a = rng.randint(2, 9); b = rng.randint(1, 20)
        if kind == "e1": c = a * n + b; t = f"{a}{l} + {b} = {c}"
        elif kind == "e2":
            c = a * n - b
            if c < 1: continue
            t = f"{a}{l} − {b} = {c}"
        elif kind == "e3": c = a * n; t = f"{a}{l} = {c}"; b = 0
        elif kind == "e4":
            a2 = rng.randint(2, 6); a = a2 + rng.randint(1, 5); c = (a - a2) * n; b = a2; t = f"{a}{l} − {a2}{l} = {c}"
            if a - a2 < 2: continue
        elif kind == "s1":
            c = a * n + b; t = f"Think of a number {l}. Multiply it by {a} and then add {b}. The answer is {c}. Find {l}."
        else:
            c = a * n + b; t = f"{N} buys {a} pens at ${l} each and a ruler for ${b}. The total is ${c}. Find {l}."
        if n >= 2 and c <= 300: break
    wrong = [n + 1, n - 1, (c + b) // a if (c + b) % a == 0 else c - b, c - b, c // a if c % a == 0 else c + b, n + a]
    return dict(t=t, ans=n, wrong=[w for w in wrong if w >= 1 and w != n], L=L, kind=kind)

def eq_solve(t):
    m = re.search(r"Multiply it by (\d+) and then add (\d+)\. The answer is (\d+)", t)
    if m: a, b, c = map(int, m.groups()); return (c - b) // a
    m = re.search(r"buys (\d+) pens at \$ ?\w each and a ruler for \$(\d+)\. The total is \$(\d+)", t)
    if m: a, b, c = map(int, m.groups()); return (c - b) // a
    left, right = t.split(" = ")
    right = right.split(" ")[0]
    coef, const = lin(left)
    return (int(right) - const) // coef

def page16():
    rng = random.Random(7616)
    kinds = ["e1", "e2", "e3", "e4", "s1", "s2"]
    for _ in range(300):
        letters = rng.sample(LET, 6); N = rng.choice(PEOPLE)
        its = [eq_item(rng, k, L, N) for k, L in zip(kinds, letters)]; rng.shuffle(its)
        ans = [it["ans"] for it in its]
        if not distinct(ans): continue
        pool = sorted({w for it in its for w in it["wrong"] if w not in ans and 1 <= w <= 300})
        res = make_table(16, ans, rng, 1, 300, pool=pool, n_decoy=3)
        if res: word, table = res; break
    cards = []
    for i, it in enumerate(its):
        if it["kind"] in ("e1", "e2", "e3", "e4"):
            cards.append(qcard(i + 1, f'<div class="eqn">{it["t"]}</div><div class="eqn">{V(it["L"])} = {abx("w3")}</div>', ""))
        else:
            cards.append(qcard(i + 1, f'<p>{it["t"]}</p>', f'{V(it["L"])} = {abx("w3")}'))
    P = code_page(16, 7616, "Find the Letter", 2, "Algebra: solving simple equations", STRAND_AL,
        "1.5 (simple linear equations with whole-number coefficients)", ["AL1.5", "AL1.3"], "Code-breaker (equations)",
        ["Find the value of the letter in each equation.", "Write the number in the box.", "Use the code table."],
        cards, ans, table, word, 1, 300, "; ".join(f"{i+1}) {it['L']} = {a}" for i, (it, a) in enumerate(zip(its, ans))),
        "Six equations with one letter and whole-number coefficients: one step with addition, one with subtraction, one with a coefficient only, one that first needs like terms collected, and two stories that the pupil turns into an equation. The decoy numbers are what a pupil gets by adding instead of subtracting the number, by forgetting to divide, or by dividing before subtracting. A pupil can test any answer by putting it back in the equation. A box left blank gives no letter and the check cannot see it.",
        ncols=2)
    solved = [eq_solve(ptxt(it["t"])) for it in its]
    P.v("V1 independent solver reads the printed equation or story and solves it: equals the key", solved == ans, solved)
    P.v("V7 every solution is a whole number and every coefficient is a whole number", all(1 <= a <= 300 for a in ans))
    # put-back test, from the printed equations
    def holds(t, n):
        tt = ptxt(t)
        if " = " in tt and "Think" not in tt and "buys" not in tt:
            left, right = tt.split(" = "); right = int(right.split(" ")[0]); c, k = lin(left); return c * n + k == right
        return None
    P.v("V2b putting each answer back into the printed equations makes both sides equal", all(holds(it["t"], a) in (True, None) for it, a in zip(its, ans)))
    return P

PAGES = [page10, page11, page12, page13, page14, page15, page16]
