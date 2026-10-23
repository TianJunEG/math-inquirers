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
            if b == 0 or a >= b: continue
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
        ["Divide. Write each answer as a fraction in simplest form.", "Write the top number and the bottom number in the boxes.", "Use the code table."],
        cards, ans, table, word, 1, 1, "; ".join(f"{i+1}) {a}/{b}" for i, (a, b) in enumerate(ans)),
        "Six items: four divisions of a proper fraction by a whole number (the top divides exactly, the top does not divide, the answer needs simplifying, a unit fraction) and two stories. The decoy letters stand for the answers a pupil gets by multiplying instead of dividing, by dividing the bottom number, or by leaving the answer unsimplified (for example 2/12 for 1/6). A box left blank gives no letter and the check cannot see it.",
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
    return route_page(2, 6202, "Dividing by Fractions", 1, "Dividing a whole number or a fraction by a fraction", STRAND_FR,
        "1.2 (dividing a whole number or a proper fraction by a proper fraction)", ["FR1.2"], "Maze / path",
        ["Start at START. Move up, down, left or right.", f"Step only on boxes where the answer is {T}.", "Do not step on a box twice."],
        rng, 4, 8, good, bad, ev_cell, Fr(T), str(T),
        f"A 4 by 4 grid of sixteen divisions: a whole number or a proper fraction divided by a proper fraction. The route follows the boxes that equal {T}. The wrong boxes include answers close to {T} and boxes where the two numbers multiply to {T}, which tempts a pupil who multiplies instead of dividing. Two extra boxes that equal {T} are dead ends. Counting the boxes shows a line that takes a shortcut.",
        cls="maze sm tall")

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
        stem = f'{fh(p, q)} {th[1]} is shared equally among {n} children. What fraction of the whole {th[0]} does each child get?'
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

PAGES = [page01, page02, page03]
