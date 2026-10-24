"""Primary 6 topic banks for the colour-by-code library (copied into school/p6/cbc_vendor; the shared library school/colour_by_code is not changed).
Every form is form(answer, rng) -> Q or None and every printed question has a rule in textcheck.py (section 'Primary 6'): the independent evaluator re-solves it from its printed words.
Answers are whole numbers (ints). Wording: ratios written 3 : 5, percentages with %, fractions stacked, letters n and p, volume in cm³."""
import math
from fractions import Fraction
from qcore import *

LEVEL = 6
RULES = dict(allow_division_sign=True, time_words_only=False)
X, D = TIMES, DIVIDE
def ch(r, seq): return r.choice(list(seq))

def S(lines, a, form):
    return SEM(lines, lambda v, t_=a: v == t_, str(a), form=form)

# ------------------------------------------------------------------ ratio and percentage
def _ratio(tier):
    def missing_second(a, r):
        for _ in range(60):
            x, y = r.randint(1, 9), r.randint(2, 11)
            if x == y or math.gcd(x, y) != 1 or a % y: continue
            k = a // y
            if k < 2 or x * k > 150: continue
            return S([f"{x} : {y} = {x*k} : {BOX}"], a, "ratio missing second")
        return None
    def missing_first(a, r):
        for _ in range(60):
            x, y = r.randint(1, 9), r.randint(2, 11)
            if x == y or math.gcd(x, y) != 1 or a % x: continue
            k = a // x
            if k < 2 or y * k > 150: continue
            return S([f"{x} : {y} = {BOX} : {y*k}"], a, "ratio missing first")
        return None
    def share(kind):
        def f(p, r):
            for _ in range(80):
                a, b = r.sample(range(1, 9), 2)
                if math.gcd(a, b) != 1: continue
                part = max(a, b) if kind == "Larger" else min(a, b)
                if p % part: continue
                u = p // part; N = (a + b) * u
                if u < 2 or N > 400: continue
                return S([f"Share {N} in the ratio", f"{a} : {b}. {kind}: {BOX}"], p, f"share {kind.lower()}")
            return None
        f.__name__ = "share_" + kind.lower(); return f
    def pct_whole(a, r):
        for _ in range(60):
            p = ch(r, [10, 20, 25, 40, 50, 60, 75, 30])
            if (a * p) % 100: continue
            part = a * p // 100
            if part < 3: continue
            return S([f"{p}% of {BOX} is {part}"], a, "percent whole")
        return None
    def pct_of(a, r):
        for _ in range(60):
            p = ch(r, [10, 20, 25, 40, 50, 60, 75, 30, 15])
            if (a * 100) % p: continue
            N = a * 100 // p
            if N > 600: continue
            return S([f"{p}% of {N} = {BOX}"], a, "percent of")
        return None
    def after_change(a, r):
        for _ in range(60):
            p = ch(r, [10, 20, 25, 50]); old = a
            if (old * p) % 100: continue
            new = old + old * p // 100
            return S([f"Up {p}% to {new}.", f"Before: {BOX}"], a, "percent increase, before")
        return None
    return [missing_second, missing_first, share("Larger"), share("Smaller"), pct_whole, pct_of, after_change]

# ------------------------------------------------------------------ volume and average
def _volavg(tier):
    def prod(a, r):
        for _ in range(80):
            x, y = r.randint(2, 9), r.randint(2, 9)
            if a % (x * y): continue
            z = a // (x * y)
            if 2 <= z <= 12: return S(["Cuboid", f"{x}×{y}×{z} cm", f"Vol {BOX} cm³"], a, "cuboid volume")
        return None
    def height(a, r):
        for _ in range(60):
            A = r.choice([6, 8, 9, 10, 12, 15, 16, 18, 20, 24, 30]); V = A * a
            if V > 1500: continue
            return S([f"Vol {V} cm³", f"Base {A} cm²", f"Height {BOX} cm"], a, "cuboid height")
        return None
    def cube(a, r):
        e = round(a ** (1 / 3))
        if e ** 3 != a: return None
        return S(["Cube, edge", f"{e} cm", f"Vol {BOX} cm³"], a, "cube volume")
    def edge(a, r):
        if a > 12: return None
        return S(["Cube Vol", f"{a**3} cm³", f"Edge {BOX} cm"], a, "cube edge")
    def avg_list(a, r):
        for _ in range(60):
            x = r.randint(max(2, a - 14), a - 1); y = r.randint(a + 1, a + 14); z = 3 * a - x - y
            if z < 2 or len({x, y, z}) < 3: continue
            return S(["Average of", f"{x}, {y}, {z}", f"= {BOX}"], a, "average list")
        return None
    def avg_total(a, r):
        n = ch(r, [4, 5, 6, 8])
        return S([f"Total {a * n},", f"{n} numbers", f"Average {BOX}"], a, "average from total")
    def total_from_avg(a, r):
        for n in (4, 5, 6, 3):
            if a % n == 0 and a // n >= 5: return S([f"Average {a // n},", f"{n} numbers", f"Total {BOX}"], a, "total from average")
        return None
    # the same questions on two lines (for the wider, flatter parts of a picture)
    def prod2(a, r):
        q = prod(a, r)
        return None if q is None else S([f"Cuboid {q.lines[1]}", q.lines[2]], a, "cuboid volume, two lines")
    def height2(a, r):
        q = height(a, r)
        return None if q is None else S([q.lines[0] + ", " + q.lines[1].lower(), q.lines[2]], a, "cuboid height, two lines")
    def cube2(a, r):
        q = cube(a, r)
        return None if q is None else S([q.lines[0] + " " + q.lines[1], q.lines[2]], a, "cube volume, two lines")
    def edge2(a, r):
        q = edge(a, r)
        return None if q is None else S([q.lines[0] + " " + q.lines[1], q.lines[2]], a, "cube edge, two lines")
    def avg_list2(a, r):
        q = avg_list(a, r)
        return None if q is None else S([q.lines[0] + " " + q.lines[1], q.lines[2]], a, "average list, two lines")
    def avg_total2(a, r):
        q = avg_total(a, r)
        return None if q is None else S([q.lines[0] + " " + q.lines[1], q.lines[2]], a, "average from total, two lines")
    def total2(a, r):
        q = total_from_avg(a, r)
        return None if q is None else S([q.lines[0] + " " + q.lines[1], q.lines[2]], a, "total from average, two lines")
    for f_, n_ in ((prod2, "prod2"), (height2, "height2"), (cube2, "cube2"), (edge2, "edge2"), (avg_list2, "avg_list2"), (avg_total2, "avg_total2"), (total2, "total2")): f_.__name__ = n_
    return [prod, height, cube, edge, avg_list, avg_total, total_from_avg, prod2, height2, cube2, edge2, avg_list2, avg_total2, total2]

# ------------------------------------------------------------------ mixed practice
def _mixed(tier):
    def pct(a, r):
        for _ in range(60):
            p = ch(r, [10, 20, 25, 40, 50, 60, 75]); 
            if (a * 100) % p: continue
            N = a * 100 // p
            if N <= 400: return S([f"{p}% of {N} = {BOX}"], a, "mixed percent")
        return None
    def fdiv(a, r):
        for _ in range(60):
            d = ch(r, [2, 3, 4, 5, 6]); n = r.randint(1, d - 1)
            if math.gcd(n, d) != 1: continue
            W = Fraction(a * n, d)
            if W.denominator == 1 and 2 <= W <= 80: return S([f"{int(W)} {DIVIDE} {FRAC(n, d)} = {BOX}"], a, "whole divided by fraction")
        return None
    def subst(a, r):
        for _ in range(60):
            m = r.randint(2, 9); n = r.randint(2, 9); c = a - m * n
            if 1 <= c <= 30: return S([f"{m}n + {c}, n = {n}", f"Value: {BOX}"], a, "substitute")
        return None
    def equ(a, r):
        for _ in range(60):
            m = r.randint(2, 9); b = r.randint(1, 20); c = m * a + b
            if c <= 300: return S([f"{m}n + {b} = {c}", f"n = {BOX}"], a, "equation")
        return None
    def share(a, r):
        for _ in range(80):
            p, q = r.sample(range(1, 8), 2)
            if math.gcd(p, q) != 1 or a % max(p, q): continue
            u = a // max(p, q); N = (p + q) * u
            if u >= 2 and N <= 400: return S([f"Share {N} in the ratio", f"{p} : {q}. Larger: {BOX}"], a, "mixed share")
        return None
    def avg(a, r):
        for _ in range(60):
            x = r.randint(max(2, a - 12), a - 1); y = r.randint(a + 1, a + 12); z = 3 * a - x - y
            if z >= 2 and len({x, y, z}) == 3: return S([f"Average of {x}, {y}", f"and {z}: {BOX}"], a, "mixed average")
        return None
    return [pct, fdiv, subst, equ, share, avg]

def build_banks():
    B = {}
    B["ratio"] = Bank("ratio", "Ratio and Percentage", "Ratio and percentage", "Work out the answer. Find it in the key. Colour the part with that colour.",
        {2: T([12, 20, 36, 45, 60], range(0, 401), _ratio(2))}, parts=[("equivalent ratios", lambda f, a: f.startswith("ratio missing")), ("sharing in a ratio", lambda f, a: f.startswith("share")),
        ("percentage", lambda f, a: f.startswith("percent"))], prefix="Ratio and percentage: ")
    B["volavg"] = Bank("volavg", "Volume and Average", "Volume and average", "Work out the answer. Find it in the key. Colour the part with that colour.",
        {2: T([27, 36, 48, 64, 72], range(0, 401), _volavg(2))}, parts=[("volume of a cuboid or cube", lambda f, a: f.startswith("cu")), ("average", lambda f, a: "average" in f or f == "total from average")], prefix="Volume and average: ")
    B["mixed"] = Bank("mixed", "Mixed Practice", "Mixed Primary 6 practice", "Work out the answer. Find it in the key. Colour the part with that colour.",
        {2: T([15, 24, 35, 48, 60], range(0, 401), _mixed(2))})
    return B
BANKS = build_banks()

GALLERY = [
    dict(id="CBC-P6-01", picture="rocket", bank="ratio", tier=2, seed=601),
    dict(id="CBC-P6-02", picture="house", bank="volavg", tier=2, seed=602),
    dict(id="CBC-P6-03", picture="butterfly", bank="mixed", tier=2, seed=603),
]
