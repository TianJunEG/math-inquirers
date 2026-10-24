"""Part A: fractions and ratio. P6-01 Fraction Shares, P6-02 Dividing by Fractions, P6-03 Fraction Stories, P6-04 Equal Ratios, P6-05 Missing Terms,
P6-06 Share in a Ratio, P6-07 Three Quantities, P6-08 Fractions and Ratios."""
import random, re, math, itertools
from fractions import Fraction as Fr
from math import gcd
from .common import *
from .kit import *
from .kit6 import *

def lcm(a, b): return a * b // gcd(a, b)
def fdomain(maxd=60):
    return [(n, d) for d in range(2, maxd + 1) for n in range(1, d)]
def ftup(x): x = Fr(x); return (x.numerator, x.denominator)

# =============================================================================== P6-01 Fraction Shares  (FR1.1)
def fs_items(rng):
    """6 items: four expressions (a/b ÷ n) and two stories; every answer a proper fraction in simplest form, all different"""
    kinds = ["exact", "inexact", "simplify", "unit", "storyA", "storyB"]
    items = []
    used = set()
    for k in kinds:
        for _ in range(500):
            if k == "exact":
                n = rng.choice([2, 3, 4, 5, 6]); m = rng.randint(1, 3); a = n * m; b = rng.choice([x for x in range(a + 1, 14) if gcd(m, x) == 1] or [0])
            elif k == "inexact":
                n = rng.choice([3, 4, 5, 6, 7]); b = rng.randint(3, 9); a = rng.randint(2, b - 1)
                if a % n == 0 or gcd(a, b * n) != 1: continue
            elif k == "simplify":
                n = rng.choice([4, 6, 8, 9, 10]); b = rng.randint(3, 9); a = rng.randint(2, b - 1)
                if gcd(a, n) == 1 or gcd(a, b * n) == 1 and Fr(a, b * n).denominator == b * n: continue
            elif k == "unit":
                a = 1; b = rng.randint(2, 8); n = rng.randint(3, 9)
            else:
                n = rng.choice([2, 3, 4, 5, 6]); b = rng.randint(3, 9); a = rng.randint(1, b - 1)
                if k == "storyB": pass
            if b == 0 or a >= b or gcd(a, b) != 1: continue
            ans = Fr(a, b) / n
            if ans.denominator > 60 or ans in used or ans >= 1: continue
            used.add(ans); items.append(dict(k=k, a=a, b=b, n=n, ans=ans)); break
    return items

def fs_card(i, it, rng, names):
    a, b, n = it["a"], it["b"], it["n"]
    if it["k"] in ("exact", "inexact", "simplify", "unit"):
        return qcard(i + 1, f'<div class="eqn">{fh(a, b)} ÷ {n} = {ans_frac()}</div>', "", cls="")
    N = names[i]
    if it["k"] == "storyA":
        t = f'{N} pours {fh(a, b)} {LITRE} of juice equally into {n} cups. How much juice is in each cup?'; u = LITRE
    else:
        t = f'A rope {fh(a, b)} m long is cut into {n} equal pieces. How long is each piece?'; u = "m"
    return qcard(i + 1, f'<p>{t}</p>', f'{ans_frac()}{unit(u)}')

def fs_solve(card):
    """independent reader of a printed card: the fraction token and the whole number (after ÷, 'into' or 'equal')"""
    t = ptxt(card)
    m = re.search(rf"(\d+){FSL}(\d+)", t)
    f = Fr(int(m.group(1)), int(m.group(2)))
    rest = t[m.end():]
    n = re.search(r"÷\s*(\d+)", rest) or re.search(r"into (\d+)", rest)
    return f / int(n.group(1))

def page01():
    rng = random.Random(6101)
    names = rng.sample(PEOPLE, 6)
    for _ in range(300):
        items = fs_items(rng)
        if len(items) < 6: continue
        rng.shuffle(items)
        ans = [ftup(it["ans"]) for it in items]
        if not distinct(ans): continue
        pool = set()
        for it in items:
            a, b, n = it["a"], it["b"], it["n"]
            for w in (Fr(a, b) * n, Fr(a, b * n), Fr(a * n, b * n) if False else Fr(a, b * n)):
                pass
            x = Fr(a, b)
            cands = [(a, b * n), (a * n, b), (a, b - n if b > n else b + n), (a // n if a % n == 0 else a + n, b), (a, b + n), (n, b), (a + 1, b * n), (a, b * n + 1),
                     (a, b * n - 1), (a, b * n + n)]
            for (p, q) in cands:
                if 0 < p < q <= 60 and (p, q) not in ans: pool.add((p, q))
            sf = ftup(x / n)
            for mlt in (2, 3):                      # unsimplified forms of the right answer
                if sf[1] * mlt <= 60 and (sf[0] * mlt, sf[1] * mlt) not in ans: pool.add((sf[0] * mlt, sf[1] * mlt))
        pool = sorted(pool)
        res = make_table(1, ans, rng, 1, 1, pool=pool, domain=fdomain(60), n_decoy=3)
        if res: word, table = res; break
    cards = [fs_card(i, it, rng, names) for i, it in enumerate(items)]
    P = code_page(1, 6101, "Fraction Shares", 1, "Dividing a fraction by a whole number", STRAND_FR,
        "1.1 (dividing a proper fraction by a whole number)", ["FR1.1"], "Code-breaker (fractions)",
        ["Divide. Write each answer in simplest form.", "Use the code table."],
        cards, ans, table, word, 1, 1, "; ".join(f"{i+1}) {a}/{b}" for i, (a, b) in enumerate(ans)),
        "Six items: four divisions of a proper fraction by a whole number (the top divides exactly, the top does not divide, the answer needs simplifying, a unit fraction) and two stories. The decoy letters stand for the answers a pupil gets by multiplying instead of dividing, by dividing the bottom number, or by leaving the answer unsimplified. A box left blank gives no letter and the check cannot see it.",
        domain=fdomain(60), fmt=lambda k: fh(*k), ncols=2, cols=6)
    solved = [ftup(fs_solve(c)) for c in cards]
    P.v("V1 independent solver reads each printed card (fraction, whole number) and divides: equals the key", solved == ans, solved)
    P.v("V7 every answer is a proper fraction in simplest form, denominator at most 60", all(gcd(a, b) == 1 and a < b <= 60 for a, b in ans))
    P.v("V3e the unsimplified form of an answer is not in the code table", all((a * 2, b * 2) not in table for a, b in ans))
    return P

# =============================================================================== P6-02 Dividing by Fractions  (FR1.2, route)
def fdiv_cell(dividend, divisor):
    d = Fr(dividend); v = Fr(divisor)
    return f'{frx(d)} ÷ {frx(v)}'

def fdiv_pairs(T):
    """all (dividend, divisor) where the dividend is a whole number up to 12 or a proper fraction (denominator up to 12), the divisor a proper fraction (denominator up to 12), quotient T"""
    out = []
    for q in range(2, 13):
        for p in range(1, q):
            if gcd(p, q) != 1: continue
            dv = Fr(T) * Fr(p, q)
            if (dv.denominator == 1 and 1 <= dv <= 12) or (dv.denominator != 1 and dv < 1 and dv.denominator <= 12):
                out.append((dv, Fr(p, q)))
    return out

def ev_cell(h):
    return calch(h)

def page02():
    rng = random.Random(6202)
    T = 6
    good = [fdiv_cell(a, b) for a, b in fdiv_pairs(T)]
    bad = []
    for q in range(2, 13):
        for p in range(1, q):
            if gcd(p, q) != 1: continue
            for dv in list(range(1, 13)) + [Fr(x, y) for y in range(2, 13) for x in range(1, y) if gcd(x, y) == 1]:
                v = Fr(dv) / Fr(p, q)
                if v != T and (3 <= v <= 10 or Fr(dv) * Fr(p, q) == T):
                    bad.append(fdiv_cell(dv, Fr(p, q)))
    bad = sorted(set(bad))
    def prod_of(c):
        a_, b_ = ptxt(c).split(" ÷ "); return pv(a_) * pv(b_)
    must = [[c for c in bad if prod_of(c) == T], [c for c in bad if ev_cell(c) in (T - 1, T + 1)]]
    return route_page(2, 6202, "Dividing by Fractions", 1, "Dividing a whole number or a fraction by a fraction", STRAND_FR,
        "1.2 (dividing a whole number or a proper fraction by a proper fraction)", ["FR1.2"], "Maze / path",
        ["Start at START. Move up, down, left or right.", f"Step only on boxes where the answer is {T}.", "Do not step on a box twice."],
        rng, 4, 8, good, bad, ev_cell, Fr(T), str(T),
        f"A 4 by 4 grid of sixteen divisions: a whole number or a proper fraction divided by a proper fraction. The route follows the boxes that equal {T}. The wrong boxes include answers close to {T} and boxes where the two numbers multiply to {T}, which tempts a pupil who multiplies instead of dividing. Two extra boxes that equal {T} are dead ends. Counting the boxes shows a line that takes a shortcut.",
        cls="maze sm tall", must=must)

# =============================================================================== P6-03 Fraction Stories  (FR1.1, FR1.2, choice)
THINGS = [("cake", "of the cake"), ("garden", "of the garden"), ("pizza", "of the pizza"), ("field", "of the field"), ("wall", "of the wall")]

def fs3_row(rng, kind, N):
    """one story: returns (dict(stem, right), [wrong values]); every value a Fraction"""
    if kind == "pieces":
        while True:
            q = rng.choice([2, 3, 4, 5, 6, 8]); p = rng.randint(1, q - 1)
            if gcd(p, q) != 1: continue
            k = rng.randint(3, 9); W = Fr(p, q) * k
            if W.denominator == 1 and 2 <= W <= 12: break
        thing = rng.choice(["ribbon", "rope", "wire", "string"])
        stem = f'{N} has {int(W)} m of {thing}. Each piece must be {fh(p, q)} m long. How many pieces can {N} cut?'
        return dict(stem=stem, right=Fr(k)), [W * Fr(p, q), Fr(p, q) / W]
    if kind == "share":
        while True:
            q = rng.randint(3, 9); p = rng.randint(1, q - 1); n = rng.choice([2, 3, 4, 5, 6])
            if gcd(p, q) != 1: continue
            r = Fr(p, q) / n
            if r.denominator <= 40: break
        w1 = Fr(p * n, q) if p * n < q else Fr(p, q) + Fr(1, n)
        th = rng.choice(THINGS)
        stem = f'{fh(p, q)} {th[1]} is split into {n} equal portions for {n} children. What fraction of the whole {th[0]} is one portion?'
        return dict(stem=stem, right=r), [w1, Fr(1, n)]
    if kind == "glasses":
        while True:
            small = Fr(rng.choice([1, 1, 2, 3]), rng.choice([8, 10, 12, 16])); k = rng.randint(2, 6)
            tot = small * k
            if tot < 1 and tot.denominator <= 16 and small < 1: break
        stem = f'A jug has {frx(tot)} {LITRE} of milk. Each glass takes {frx(small)} {LITRE}. How many glasses can be filled?'
        return dict(stem=stem, right=Fr(k)), [tot * small, small / tot]
    raise ValueError(kind)

def page03():
    rng = random.Random(6303)
    for _ in range(2000):
        names = rng.sample(PEOPLE, 6)
        kinds = ["pieces", "share", "glasses", "pieces", "share", "glasses"]; rng.shuffle(kinds)
        rows = []; ok = True
        for N, k in zip(names, kinds):
            row, wrongs = fs3_row(rng, k, N)
            vals = [row["right"]] + wrongs
            if len(set(vals)) < 3 or any(v <= 0 for v in vals): ok = False; break
            rows.append((row, wrongs))
        if not ok or len({r[0]["stem"] for r in rows}) < 6: continue
        break
    layout = []
    crows = []
    for row, wrongs in rows:
        opts = [row["right"]] + wrongs
        order = list(range(3)); rng.shuffle(order)
        crows.append(dict(stem=row["stem"], opts=[mxx(opts[j]) for j in order], right=order.index(0)))
    def solve_row(stem, opts):
        t = ptxt(stem)
        nums = [pv(x) for x in re.findall(rf"\d+{FSL}\d+|\d+\.\d+|\d+", t)]
        # drop the numbers that are names of things (none) ; first two quantities
        if "How many" in t:
            a, b = nums[0], nums[1]; q = max(a, b) / min(a, b)
        else:
            f = nums[0]; n = nums[1]; q = f / n
        for j, o in enumerate(opts):
            if pv(ptxt(o)) == q: return j
        return -1
    P = choice_page(3, 6303, "Fraction Stories", 2, "Fraction stories: dividing by a whole number or by a fraction", STRAND_FR,
        "1.1, 1.2 (dividing a proper fraction by a whole number; dividing by a proper fraction)", ["FR1.1", "FR1.2"], "Choice table (stories)",
        ["Work out each answer.", "Circle the letter beside the right answer.", "Write the six letters in the boxes."],
        rng, crows, solve_row,
        "Six stories: how many pieces of a given fraction of a metre fit into a whole number of metres, what fraction of a whole each child gets when a fraction is shared, and how many glasses of a fraction of a litre a jug fills. Each row has three answers. The wrong answers are what a pupil gets by multiplying instead of dividing, or by dividing the other way round. The letters of the right answers, read down the rows, spell the word. Every other way of choosing was tested against a very large word list: none spells a word. A box left blank gives no letter and the check cannot see it.",
        ps=False, check="Write the six letters in order. Do they spell a word?")
    return P


# =============================================================================== ratio helpers
def rtxt(*parts): return " : ".join(str(x) for x in parts)
def rh(*parts): return f'<span class="rt">{rtxt(*parts)}</span>'
def simp(parts):
    g = 0
    for x in parts: g = gcd(g, x)
    return tuple(x // g for x in parts)
def read_ratio(t):
    """the numbers of the first ratio a : b (: c) in plain text"""
    m = re.search(r"(\d+(?: : \d+)+)", t)
    return tuple(int(x) for x in m.group(1).split(" : "))

# =============================================================================== P6-04 Equal Ratios  (RA1.1, RA1.2, RA1.4, match)
def page04():
    rng = random.Random(6404)
    for _ in range(3000):
        simp_list = []
        while len(simp_list) < 6:
            k = rng.choice([2, 2, 3])
            t = tuple(rng.randint(1, 9) for _ in range(k))
            if simp(t) != t or len(set(t)) < len(t) or any(set(t) == set(u) for u in simp_list): continue
            simp_list.append(t)
        if sum(1 for t in simp_list if len(t) == 3) != 2: continue
        items = []; cards = []
        for t in simp_list:
            f1 = rng.choice([2, 3, 4, 5, 6]); f2 = rng.choice([x for x in (1, 2, 3, 4, 5) if x != f1])
            items.append(tuple(x * f1 for x in t)); cards.append(tuple(x * f2 for x in t))
        decs = []
        for t in rng.sample(simp_list, 2):
            d = tuple(reversed(t)) if len(decs) == 0 else tuple(x + 1 for x in t)
            d = tuple(y * rng.choice([1, 2, 3]) for y in d)
            if all(simp(d) != s_ for s_ in simp_list): decs.append(d)
        if len(decs) < 2: continue
        allc = cards + decs
        if len({simp(c) for c in allc}) < 8: continue
        break
    order = list(range(8)); rng.shuffle(order)
    card_html = [rh(*allc[j]) for j in order]
    right = [order.index(i) for i in range(6)]
    item_html = [rh(*it) for it in items]
    def solve_item(ih, chs):
        a = simp(read_ratio(ptxt(ih)))
        for j, c in enumerate(chs):
            if simp(read_ratio(ptxt(c))) == a: return j
        return -1
    P = match_page(4, 6404, "Equal Ratios", 1, "Ratios: equivalent ratios and simplest form", STRAND_RA,
        "1.1, 1.2, 1.4 (ratio a : b and a : b : c; equivalent ratios; simplest form)", ["RA1.1", "RA1.2", "RA1.4"], "Matching (equal ratios)",
        ["Match each ratio to an equal ratio.", "Write the card letter in the box.", "Use each card once. Two cards are not used."],
        rng, item_html, card_html, right, solve_item,
        "Six ratios (four with two parts, two with three parts) are matched to eight cards. A card is the item in simplest form or multiplied by a different number, so the pupil must simplify or scale. Two cards are decoys: a ratio with the parts written the other way round, or with a part changed. The letters of the matching cards, read in the order of the items, spell the word. Every way of giving each item a different card, and every single changed letter, was tested against a very large word list: none spells another word. A box left blank gives no letter and the check cannot see it.",
        item_cols=2, card_cols=4)
    return P

# =============================================================================== P6-05 Missing Terms  (RA1.2, RA1.6, code)
STUFF = ["stickers", "marbles", "coins", "shells", "cards", "stamps"]
def ratio_eq_html(left, right):
    """a ratio equation; None stands for the blank (an answer box)"""
    side = lambda parts: " : ".join('<span class="ab w3"></span>' if x is None else str(x) for x in parts)
    return f'<div class="eqn">{side(left)} = {side(right)}</div>'

def solve_ratio_eq(t):
    L, R = [s.split(" : ") for s in t.split(" = ")]
    k = None
    for l, r in zip(L, R):
        if l.isdigit() and r.isdigit(): k = Fr(int(r), int(l)); break
    for i, (l, r) in enumerate(zip(L, R)):
        if r == "?": return int(l * 1) * k if False else int(Fr(int(l)) * k)
        if l == "?": return int(Fr(int(r)) / k)
    raise ValueError(t)

def mt_item(rng, kind):
    while True:
        a, b = rng.randint(1, 9), rng.randint(2, 11)
        if a == b or gcd(a, b) != 1: continue
        k = rng.randint(2, 9); c, d = a * k, b * k
        if d > 120 or c > 120 or k == 1: continue
        break
    if kind == "first":
        return dict(html=ratio_eq_html([a, b], [c, None]), ans=d, wrong=[b + (c - a)], cells=(a, b, c, d))
    if kind == "second":
        return dict(html=ratio_eq_html([a, b], [None, d]), ans=c, wrong=[a + (d - b)], cells=(a, b, c, d))
    if kind == "mid":
        return dict(html=ratio_eq_html([a, None], [c, d]), ans=b, wrong=[d - (c - a)], cells=(a, b, c, d))
    if kind == "three":
        a, b, e = rng.sample(range(1, 8), 3); k = rng.randint(2, 7)
        return dict(html=ratio_eq_html([a, b, e], [a * k, None, e * k]), ans=b * k, wrong=[b + (a * k - a)], cells=(a, b, e, k))
    X, Y = rng.sample(PEOPLE, 2); thing = rng.choice(STUFF)
    if kind == "storyA":
        return dict(html=f'<p>{X} and {Y} share some {thing} in the ratio {a} : {b}. {Y} gets {d}. How many {thing} does {X} get?</p>' + f'<p>{ans_ratio(1, "w3")}</p>', ans=c, wrong=[a + (d - b)], cells=(a, b, c, d))
    return dict(html=f'<p>{X} and {Y} share some {thing} in the ratio {a} : {b}. {X} gets {c}. How many {thing} does {Y} get?</p>' + f'<p>{ans_ratio(1, "w3")}</p>', ans=d, wrong=[b + (c - a)], cells=(a, b, c, d))

def mt_solve(h):
    t = ptxt(h)
    if " = " in t: return solve_ratio_eq(t)
    m = re.search(r"(\w+) and (\w+) share some \w+ in the ratio (\d+) : (\d+)\. (\w+) gets (\d+)\. How many \w+ does (\w+) get\?", t)
    X, Y, a, b, known, v, asked = m.groups(); part = {X: int(a), Y: int(b)}
    return part[asked] * int(v) // part[known]

def page05():
    rng = random.Random(6505)
    kinds = ["first", "second", "mid", "three", "storyA", "storyB"]
    for _ in range(300):
        its = [mt_item(rng, k) for k in kinds]; rng.shuffle(its)
        ans = [it["ans"] for it in its]
        if not distinct(ans) or max(ans) > 130 or any(w in ans for it in its for w in it["wrong"]): continue
        pool = {w for it in its for w in it["wrong"] if w > 0 and w not in ans}
        pool |= {a + 1 for a in ans} | {a - 1 for a in ans if a > 1} | {a * 2 for a in ans if a * 2 <= 130} | {a + 10 for a in ans}
        pool = sorted(p for p in pool if p not in ans and 1 <= p <= 130)
        res = make_table(5, ans, rng, 1, 130, pool=pool, n_decoy=3)
        if res: word, table = res; break
    cards = [qcard(i + 1, it["html"], "") for i, it in enumerate(its)]
    P = code_page(5, 6505, "Missing Terms", 1, "Equivalent ratios: finding the missing term", STRAND_RA,
        "1.2, 1.6 (equivalent ratios; finding the missing term in equivalent ratios)", ["RA1.2", "RA1.6"], "Code-breaker (equivalent ratios)",
        ["Find the missing number in each box.", "Use the code table."],
        cards, ans, table, word, 1, 130, "; ".join(f"{i+1}) {a}" for i, a in enumerate(ans)),
        "Six items: three two-part equations with the missing number in a different place, one three-part equation and two sharing stories. The decoy numbers are the answers a pupil gets by adding the same number to both terms instead of multiplying. A box left blank gives no letter and the check cannot see it.", ncols=2)
    solved = [mt_solve(c) for c in [it["html"] for it in its]]
    P.v("V1 independent solver reads each printed equation or story and finds the missing term (equal ratios): equals the key", solved == ans, solved)
    P.v("V7 ratios use whole numbers only, answers at most 130", all(1 <= a <= 130 for a in ans))
    P.v("V3e the additive slip (adding the same number to both terms) is a decoy or has no letter", all(w not in table or table[w] not in word for it in its for w in it["wrong"] if w != it["ans"]))
    return P

# =============================================================================== P6-06 Share in a Ratio  (RA1.3, RA1.5, code)
def sr_item(rng, kind, X, Y):
    if kind == "larger" or kind == "smaller":
        while True:
            a, b = rng.sample(range(1, 10), 2)
            if gcd(a, b) != 1: continue
            u = rng.randint(4, 30); N = (a + b) * u
            if N <= 600: break
        word = "larger" if kind == "larger" else "smaller"
        ans = max(a, b) * u if kind == "larger" else min(a, b) * u
        thing = rng.choice(["sweets", "stickers", "beads", "cards"])
        t = f'Share {N} {thing} in the ratio {a} : {b}. How many {thing} are in the {word} share?'
        return dict(t=t, ans=ans, wrong=[N // (a + b), N - ans, (a + b) * u // 2], N=N, parts=(a, b))
    if kind == "diff":
        while True:
            a, b = rng.sample(range(2, 10), 2)
            if gcd(a, b) != 1: continue
            u = rng.randint(5, 40); N = (a + b) * u
            if N <= 900: break
        t = f'{X} and {Y} share ${N} in the ratio {a} : {b}. How much more does {X if a > b else Y} get than {Y if a > b else X}?'
        ans = abs(a - b) * u
        return dict(t=t, ans=ans, wrong=[N // (a + b), max(a, b) * u, min(a, b) * u], N=N, parts=(a, b))
    if kind == "three":
        while True:
            a, b, c = sorted(rng.sample(range(1, 8), 3))
            if gcd(gcd(a, b), c) != 1: continue
            u = rng.randint(4, 40); N = (a + b + c) * u
            if N <= 900: break
        t = f'Share {N} in the ratio {a} : {b} : {c}. What is the largest share?'
        return dict(t=t, ans=c * u, wrong=[a * u, b * u, N // (a + b + c)], N=N, parts=(a, b, c))
    if kind == "rope":
        while True:
            a, b, c = rng.sample(range(2, 8), 3)
            if gcd(gcd(a, b), c) != 1: continue
            u = rng.randint(2, 12); N = (a + b + c) * u
            if N <= 300: break
        t = f'A rope {N} m long is cut into three pieces in the ratio {a} : {b} : {c}. How long is the shortest piece?'
        return dict(t=t, ans=min(a, b, c) * u, wrong=[N // (a + b + c), max(a, b, c) * u, N - min(a, b, c) * u], N=N, parts=(a, b, c))
    # school: ratio of boys to girls, total pupils; how many girls
    while True:
        a, b = rng.sample(range(2, 10), 2)
        if gcd(a, b) != 1: continue
        u = rng.randint(5, 30); N = (a + b) * u
        if N <= 500: break
    who = rng.choice([("boys", "girls"), ("men", "women"), ("cats", "dogs")])
    t = f'The ratio of {who[0]} to {who[1]} is {a} : {b}. There are {N} in all. How many {who[1]} are there?'
    return dict(t=t, ans=b * u, wrong=[a * u, N // (a + b), N - b * u + 0 if False else (a + b) * u // 2], N=N, parts=(a, b))

def sr_solve(t):
    nums = [int(x) for x in re.findall(r"\d+", re.sub(r"\d+ : \d+(?: : \d+)*", "R", t))]
    parts = read_ratio(t); N = nums[0]; u = N // sum(parts)
    if "ratio of" in t and " to " in t.split("ratio of")[1][:20]:
        return parts[1] * u                                  # ratio of A to B ... how many B
    if "How much more" in t:
        return abs(parts[0] - parts[1]) * u
    if "larger" in t or "largest" in t: return max(parts) * u
    if "smaller" in t or "shortest" in t: return min(parts) * u
    raise ValueError(t)

def page06():
    rng = random.Random(6606)
    kinds = ["larger", "smaller", "diff", "three", "rope", "school"]
    for _ in range(300):
        X, Y = rng.sample(PEOPLE, 2)
        its = [sr_item(rng, k, X, Y) for k in kinds]; rng.shuffle(its)
        ans = [it["ans"] for it in its]
        if not distinct(ans) or max(ans) > 900: continue
        pool = {w for it in its for w in it["wrong"] if w > 0}
        pool = sorted(p for p in pool if p not in ans and p <= 900)
        res = make_table(6, ans, rng, 1, 900, pool=pool, n_decoy=3)
        if res: word, table = res; break
    cards = [qcard(i + 1, f'<p>{it["t"]}</p>', ans_ratio(1, "w4")) for i, it in enumerate(its)]
    P = code_page(6, 6606, "Share in a Ratio", 1, "Ratio: sharing a quantity in a given ratio", STRAND_RA,
        "1.3, 1.5 (dividing a quantity in a given ratio; ratio of two or three quantities)", ["RA1.3", "RA1.5"], "Code-breaker (sharing in a ratio)",
        ["Find each share.", "Write the answer in the box.", "Use the code table."],
        cards, ans, table, word, 1, 900, "; ".join(f"{i+1}) {a}" for i, a in enumerate(ans)),
        "Six items: the larger share, the smaller share, how much more one share is than the other, the largest share of a three-part ratio, the shortest piece of a rope, and one part of a total given as a ratio of two groups. The decoy numbers are what a pupil gets by dividing the total by the number of parts only, by finding the wrong share, or by taking the other part. A box left blank gives no letter and the check cannot see it.", ncols=2)
    solved = [sr_solve(it["t"]) for it in its]
    P.v("V1 independent solver reads each printed story (total, ratio, which share is asked) and equals the key", solved == ans, solved)
    P.v("V7 every share is a whole number and all totals are divisible by the number of parts", all(it["N"] % sum(it["parts"]) == 0 for it in its))
    return P


# =============================================================================== P6-07 Three Quantities  (RA1.1, RA1.4, RA1.5, code with three-part answers)
UNITS_TO_BASE = {"mℓ": 1, "ℓ": 1000, "cm": 1, "m": 100, "g": 1, "kg": 1000}
def three_item(rng, kind, names, system=None):
    N1, N2, N3 = names
    while True:
        t = tuple(rng.randint(1, 9) for _ in range(3))
        if simp(t) == t and len(set(t)) == 3: break
    if kind == "count":
        k = rng.randint(2, 6); a, b, c = (x * k for x in t)
        thing = rng.choice([("A bag has {a} red, {b} blue and {c} green counters. Write red : blue : green in simplest form.", ""),
                            (f"{N1}, {N2} and {N3} collect {{a}}, {{b}} and {{c}} stamps. Write the ratio of their stamps in simplest form.", ""),
                            ("A box has {a} pens, {b} pencils and {c} rulers. Write pens : pencils : rulers in simplest form.", "")])[0]
        return dict(t=thing.format(a=a, b=b, c=c), ans=t, wrong=[tuple(x * 2 for x in t), tuple(reversed(t)), (a, b, c)])
    if kind == "units":
        sysn = rng.choice([x for x in [("mℓ", "ℓ", 250, 4), ("cm", "m", 25, 4), ("g", "kg", 250, 4), ("mℓ", "ℓ", 500, 2), ("g", "kg", 500, 2)] if x[0] == system])
        small, big, s, one = sysn
        t = rng.choice([(1, one, 2), (3, one, 1), (one, 3, 5), (5, one, 3), (one, 1, 3), (7, one, 1)])
        if simp(t) != t or len(set(t)) < 3: t = (1, one, 2) if one != 1 else (3, 1, 2)
        vals = [x * s for x in t]
        who = rng.choice([("A fruit drink has", ["juice", "water", "syrup"]), ("A paint mix has", ["red", "white", "blue"]), ("A rope is cut into pieces that are", ["a", "b", "c"])])
        def shown(v):
            return f"{v // UNITS_TO_BASE[big]} {big}" if v % UNITS_TO_BASE[big] == 0 and v >= UNITS_TO_BASE[big] else f"{v} {small}"
        parts = [shown(v) for v in vals]
        if small in ("mℓ", "cm", "g") and small != big:
            what = {"mℓ": "juice", "cm": "wood", "g": "flour"}[small]
        names3 = {"mℓ": ("juice", "water", "syrup"), "cm": ("red", "blue", "green"), "g": ("flour", "sugar", "butter")}[small]
        if small == "cm":
            tx = f"Three ribbons are {parts[0]}, {parts[1]} and {parts[2]} long. Write the ratio of their lengths in simplest form."
        elif small == "mℓ":
            tx = f"A drink has {parts[0]} of {names3[0]}, {parts[1]} of {names3[1]} and {parts[2]} of {names3[2]}. Write {names3[0]} : {names3[1]} : {names3[2]} in simplest form."
        else:
            tx = f"A cake needs {parts[0]} of {names3[0]}, {parts[1]} of {names3[1]} and {parts[2]} of {names3[2]}. Write {names3[0]} : {names3[1]} : {names3[2]} in simplest form."
        raw = tuple(vals)
        return dict(t=tx, ans=t, wrong=[tuple(reversed(t)), tuple(x * 2 for x in t)])
    if kind == "link1":
        a, b, c = t
        tx = f"The ratio of {N1}'s money to {N2}'s money is {a} : {b}. The ratio of {N2}'s money to {N3}'s money is {b} : {c}. Write {N1} : {N2} : {N3}."
        return dict(t=tx, ans=(a, b, c), wrong=[(a, b, b), (a, c, b), tuple(x * 2 for x in (a, b, c))])
    # link2: the middle terms differ
    while True:
        a, b = rng.randint(1, 5), rng.randint(2, 6); c, d = rng.randint(2, 6), rng.randint(1, 7)
        if a == b or c == d or b == c: continue
        L = lcm(b, c); ans = simp((a * L // b, L, d * L // c))
        if gcd(a, b) == 1 and gcd(c, d) == 1 and max(ans) <= 15 and len(set(ans)) == 3: break
    tx = f"The ratio of {N1}'s money to {N2}'s money is {a} : {b}. The ratio of {N2}'s money to {N3}'s money is {c} : {d}. Write {N1} : {N2} : {N3} in simplest form."
    return dict(t=tx, ans=ans, wrong=[(a, b, d), (a * c, b * c, b * d) if max(a * c, b * c, b * d) <= 15 else (a, c, d), tuple(reversed(ans))])

def three_solve(t):
    ratios = re.findall(r"(\d+) : (\d+)\.", t)
    if "ratio of" in t and len(ratios) == 2:
        (a, b), (c, d) = [tuple(map(int, r)) for r in ratios]
        L = lcm(b, c); return simp((a * L // b, L, d * L // c))
    uq = re.findall(r"(\d+) (mℓ|ℓ|cm|kg|g|m)\b", t)
    if len(uq) == 3:
        return simp(tuple(int(n) * UNITS_TO_BASE[u] for n, u in uq))
    nums = [int(x) for x in re.findall(r"\d+", t)]
    return simp(tuple(nums[:3]))

def page07():
    rng = random.Random(6707)
    kinds = [("count", None), ("count", None), ("units", "mℓ"), ("units", "g"), ("link1", None), ("link2", None)]
    for _ in range(500):
        names = rng.sample(PEOPLE, 3)
        its = [three_item(rng, k, names, sy) for k, sy in kinds]; rng.shuffle(its)
        ans = [it["ans"] for it in its]
        if not distinct(ans) or len({it["t"] for it in its}) < 6 or any(max(a) > 15 for a in ans): continue
        pool = sorted({w for it in its for w in it["wrong"] if max(w) <= 15 and w not in ans and min(w) >= 1})
        dom = [(a, b, c) for a in range(1, 16) for b in range(1, 16) for c in range(1, 16)]
        res = make_table(7, ans, rng, 1, 1, pool=pool, domain=dom, n_decoy=3)
        if res: word, table = res; break
    cards = [qcard(i + 1, f'<p>{it["t"]}</p>', ans_ratio(3, "w2"), cls="inl") for i, it in enumerate(its)]
    P = code_page(7, 6707, "Three Quantities", 2, "Ratio of three quantities in simplest form", STRAND_RA,
        "1.1, 1.4, 1.5 (ratio a : b : c; simplest form; ratio of two or three quantities)", ["RA1.1", "RA1.4", "RA1.5"], "Code-breaker (ratio of three quantities)",
        ["Write each ratio in simplest form.", "Put one number in each box.", "Use the code table."],
        cards, ans, table, word, 1, 1, "; ".join(f"{i+1}) {a} : {b} : {c}" for i, (a, b, c) in enumerate(ans)),
        "Six items: three counts, two quantities with units that must first be changed to the same unit, and two linked ratios (the middle quantity appears in both). The decoy ratios are what a pupil gets by leaving the ratio unsimplified, by writing the quantities in the wrong order, by not changing the units, or by not matching the middle term of two linked ratios. A box left blank gives no letter and the check cannot see it.",
        domain=dom, fmt=lambda k: " : ".join(map(str, k)), ncols=1, cols=3)
    solved = [three_solve(it["t"]) for it in its]
    P.v("V1 independent solver reads the printed quantities (changing units, linking two ratios) and equals the key", solved == ans, solved)
    P.v("V7 every answer is a three-part ratio of whole numbers in simplest form, parts at most 15", all(simp(a) == a and max(a) <= 15 for a in ans))
    return P

# =============================================================================== P6-08 Fractions and Ratios  (RA1.7, choice)
def fr_rows(rng, names):
    rows = []
    def pick_pq():
        while True:
            q = rng.randint(4, 11); p = rng.randint(1, q - 1)
            if gcd(p, q) == 1 and p != 1: return p, q
    N, M = names[0], names[1]
    p, q = pick_pq()
    rows.append(dict(stem=f"{N} has {fh(p, q)} of the stickers. {M} has the rest. Find the ratio of {N}'s stickers to {M}'s stickers.", right=("r", (p, q - p)), wrong=[("r", (p, q)), ("r", (q - p, p))]))
    while True:
        a, b = rng.sample(range(1, 8), 2)
        if gcd(a, b) == 1: break
    col = rng.choice([("red", "blue"), ("white", "black")]); ask = rng.choice([0, 1])
    rows.append(dict(stem=f"The ratio of {col[0]} beads to {col[1]} beads is {a} : {b}. What fraction of the beads is {col[ask]}?", right=("f", Fr((a, b)[ask], a + b)),
                     wrong=[("f", Fr((a, b)[ask], (a, b)[1 - ask])) if (a, b)[ask] < (a, b)[1 - ask] else ("f", Fr((a, b)[1 - ask], a + b)), ("f", Fr((a, b)[1 - ask], a + b))]))
    p, q = pick_pq()
    rows.append(dict(stem=f"{names[2]}'s pencil is {fh(p, q)} as long as {names[3]}'s pencil. Find the ratio of {names[2]}'s pencil to {names[3]}'s pencil.", right=("r", (p, q)), wrong=[("r", (q, p)), ("r", (p, q - p))]))
    while True:
        a, b = rng.randint(1, 6), rng.randint(3, 11)
        if a < b and gcd(a, b) == 1 and a != 1: break
    rows.append(dict(stem=f"The ratio of {names[4]}'s age to {names[4]}'s father's age is {a} : {b}. {names[4]}'s age is what fraction of the father's age?", right=("f", Fr(a, b)),
                     wrong=[("f", Fr(a, a + b)), ("f", Fr(b - a, b))]))
    while True:
        a, b = rng.sample(range(2, 9), 2)
        if gcd(a, b) == 1: break
    who = rng.choice([("boys", "girls"), ("cats", "dogs")]); ask = rng.choice([0, 1])
    rows.append(dict(stem=f"The ratio of {who[0]} to {who[1]} is {a} : {b}. What fraction of the animals or pupils are {who[ask]}?".replace("the animals or pupils", "the pupils" if who[0] == "boys" else "the pets"),
                     right=("f", Fr((a, b)[ask], a + b)), wrong=[("f", Fr((a, b)[1 - ask], a + b)), ("f", Fr((a, b)[ask], (a, b)[1 - ask]) if (a, b)[ask] < (a, b)[1 - ask] else Fr((a, b)[ask] , a + b + 1))]))
    p, q = pick_pq()
    rows.append(dict(stem=f"{names[5]} spent {fh(p, q)} of the money. Find the ratio of the money spent to the money left.", right=("r", (p, q - p)), wrong=[("r", (q - p, p)), ("r", (p, q))]))
    return rows

def fr_opt(o):
    kind, v = o
    return rh(*v) if kind == "r" else frx(v)

def fr_solve_row(stem, opts):
    t = ptxt(stem)
    m = re.search(rf"has (\d+){FSL}(\d+) of the stickers", t)
    if m: p, q = int(m.group(1)), int(m.group(2)); want = ("r", simp((p, q - p)))
    elif "as long as" in t:
        m = re.search(rf"(\d+){FSL}(\d+) as long as", t); want = ("r", simp((int(m.group(1)), int(m.group(2)))))
    elif "spent" in t:
        m = re.search(rf"spent (\d+){FSL}(\d+)", t); p, q = int(m.group(1)), int(m.group(2)); want = ("r", simp((p, q - p)))
    elif "father's age" in t:
        a, b = map(int, re.search(r"is (\d+) : (\d+)", t).groups()); want = ("f", Fr(a, b))
    else:
        a, b = map(int, re.search(r"is (\d+) : (\d+)", t).groups())
        nm = re.search(r"ratio of (\w+) \w* ?to (\w+)", t)
        first, second = re.search(r"ratio of (\w+)(?: beads)? to (\w+)", t).groups()
        asked = re.search(r"are (\w+)\?|is (\w+)\?", t); asked = [g for g in asked.groups() if g][0]
        want = ("f", Fr(a if asked == first else b, a + b))
    for j, o in enumerate(opts):
        s = ptxt(o)
        got = ("r", simp(tuple(int(x) for x in s.split(" : ")))) if ":" in s else ("f", pv(s))
        if got == want: return j
    return -1

def page08():
    rng = random.Random(6808)
    for _ in range(200):
        names = rng.sample(PEOPLE, 6)
        rows = fr_rows(rng, names)
        ok = all(len({repr(r["right"][1]), repr(r["wrong"][0][1]), repr(r["wrong"][1][1])}) == 3 for r in rows)
        if ok: break
    crows = []
    for r in rows:
        opts = [r["right"]] + r["wrong"]; order = list(range(3)); rng.shuffle(order)
        crows.append(dict(stem=r["stem"], opts=[fr_opt(opts[j]) for j in order], right=order.index(0)))
    rng.shuffle(crows)
    P = choice_page(8, 6808, "Fractions and Ratios", 2, "Ratio and fraction: how they are linked", STRAND_RA,
        "1.7 (relationship between fraction and ratio), 1.5 (finding the ratio of two or three given quantities)", ["RA1.7", "RA1.5"], "Choice table (ratio and fraction)",
        ["Read each question.", "Circle the letter beside the right answer.", "Write the six letters in the boxes."],
        rng, crows, fr_solve_row,
        "Six questions that link a fraction and a ratio: a fraction of a quantity to a ratio of the part to the rest, a ratio to the fraction one part makes of the whole, a fraction taken as a ratio of two quantities, and one part as a fraction of the other part. Each row has three answers. The wrong answers are what a pupil gets by using the whole instead of the rest, by writing the parts the wrong way round, or by writing a ratio as a fraction of the other part. The letters of the right answers, read down the rows, spell the word. Every other way of choosing was tested against a very large word list: none spells a word. A box left blank gives no letter and the check cannot see it.")
    return P

PAGES = [page01, page02, page03, page04, page05, page06, page07, page08]
