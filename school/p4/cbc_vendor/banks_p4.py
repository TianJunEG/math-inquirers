"""Primary 4 topic banks for colour by code (level file: LEVEL, RULES, BANKS, GALLERY). Written for the Primary 4 school booklets from the Primary 2 file's design.
Three banks: numbers up to 100 000, multiplication and division with larger numbers, decimals. Every form is form(answer, rng) -> Q or None (None: this
answer cannot be made in this form). Numbers of 5 digits are written with a non-breaking space (45 280); 4-digit numbers have no gap.
Most forms have a one-line and a stacked variant (two or three short lines) so that a question fits the small parts of a picture."""
import math, re
from fractions import Fraction
import art as A
from qcore import *

LEVEL = 4
RULES = dict(allow_division_sign=True, time_words_only=False)
X, D = TIMES, DIVIDE
NB = " "
def ch(r, seq): return r.choice(list(seq))

def nb(n):
    """a whole number as printed: 5 digits or more have a gap"""
    s = str(n)
    return s[:-3] + NB + s[-3:] if len(s) >= 5 else s

# ------------------------------------------------------------------ number words (for the 'words' form)
ONES = "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split()
TENS = "x x twenty thirty forty fifty sixty seventy eighty ninety".split()
def below100(n): return ONES[n] if n < 20 else TENS[n // 10] + ("-" + ONES[n % 10] if n % 10 else "")
def below1000(n):
    h, r = divmod(n, 100)
    if h == 0: return below100(r)
    return ONES[h] + " hundred" + (" and " + below100(r) if r else "")
def words_of(n):
    t, r = divmod(n, 1000)
    s = below1000(t) + " thousand" if t else ""
    if r: s += (" and " + below100(r)) if (r < 100 and t) else ((", " if t else "") + below1000(r))
    return s

# ------------------------------------------------------------------ numbers up to 100 000
KEY_N = [400, 3000, 4500, 7000, 20000]
DOM_N = sorted(set(range(0, 25001, 10)) | set(KEY_N))

def _numbers4():
    def holds_eq(t): return lambda v, t_=t: v == t_
    def digit_value(a, r):
        for d in range(1, 10):
            for p in range(2, 5):
                if d * 10 ** p != a: continue
                for _ in range(80):
                    n = r.randint(10 ** 3, 99999); s = list(str(n)); pos = len(s) - 1 - p
                    if pos < 0: continue
                    s[pos] = str(d); n = int("".join(s))
                    if str(n).count(str(d)) == 1 and n >= 1000:
                        lines = r.choice([[f"Value of the digit {d}", f"in {nb(n)}: {BOX}"], [f"Value of {d} in", f"{nb(n)}", f"= {BOX}"]])
                        return SEM(lines, holds_eq(a), str(a), form="value of a digit")
        return None
    def round_to(a, r):
        ss = [s for s in (10, 100, 1000) if a % s == 0]
        if not ss: return None
        s = ch(r, ss[-2:]) if len(ss) >= 2 else ss[0]
        n = r.choice([a - s // 2, a + s // 2 - 1, r.randint(a - s // 2, a + s // 2 - 1)])
        if n == a or n < 1000: return None
        lines = r.choice([[f"Round {nb(n)} to", f"the nearest {s}: {BOX}"], [f"Round {nb(n)}", f"to nearest {s}", f"= {BOX}"]])
        return SEM(lines, holds_eq(a), str(a), form=f"round to {s}")
    def more_less(a, r):
        k = ch(r, [10, 100, 1000, 10000]); up = r.random() < .5
        base = a - k if up else a + k
        if base < 1000 or base > 99999 or k >= a: return None
        w = "more" if up else "less"
        lines = r.choice([[f"{nb(k)} {w} than", f"{nb(base)}: {BOX}"], [f"{nb(k)} {w}", f"than {nb(base)}", f"= {BOX}"]])
        return SEM(lines, holds_eq(a), str(a), form="more or less")
    def words(a, r):
        w = words_of(a); parts = w.split(", ")
        lines = [w, f"= {BOX}"] if len(parts) == 1 and len(w) <= 15 else (parts + [f"= {BOX}"] if len(parts) > 1 else [w, f"= {BOX}"])
        return SEM(lines, holds_eq(a), str(a), form="words to number")
    def expanded(a, r):
        if a >= 10000: return None
        if a < 1000: parts = [a - 100, 100]
        elif a % 1000 == 0: parts = [a - 1500, 1000, 500]
        else: th = a // 1000 * 1000; parts = [th, a - th]
        if r.random() < .5: parts = list(reversed(parts))
        return SEM([" + ".join(map(str, parts)), f"= {BOX}"], holds_eq(a), str(a), form="expanded")
    def greatest(a, r):
        o = [a - r.choice([1, 10, 100, 101, 90, 9]) for _ in range(2)]
        if len(set(o + [a])) < 3 or min(o) < 1000: return None
        ns = o + [a]; r.shuffle(ns)
        lines = r.choice([["Greatest of", ", ".join(nb(x) for x in ns) + f": {BOX}"], ["Greatest of", f"{nb(ns[0])}, {nb(ns[1])},", f"{nb(ns[2])}: {BOX}"]])
        return SEM(lines, holds_eq(a), str(a), form="greatest of three")
    def smallest(a, r):
        o = [a + r.choice([1, 10, 100, 101, 90, 9]) for _ in range(2)]
        if len(set(o + [a])) < 3 or a < 1000 or max(o) > 99999: return None
        ns = o + [a]; r.shuffle(ns)
        lines = r.choice([["Smallest of", ", ".join(nb(x) for x in ns) + f": {BOX}"], ["Smallest of", f"{nb(ns[0])}, {nb(ns[1])},", f"{nb(ns[2])}: {BOX}"]])
        return SEM(lines, holds_eq(a), str(a), form="smallest of three")
    def pattern(a, r):
        s = ch(r, [100, 500, 1000, 2500, 250]); pos = r.randrange(0, 4); sg = r.choice([1, -1]) * s
        terms = [a - sg * pos + sg * i for i in range(4)]
        if min(terms) < 1000 or max(terms) > 99999: return None
        items = [BOX if i == pos else nb(t) for i, t in enumerate(terms)]
        lines = [f"Pattern: {items[0]}, {items[1]},", f"{items[2]}, {items[3]}"]
        return SEM(lines, holds_eq(a), str(a), form="number pattern")
    return [digit_value, round_to, more_less, words, expanded, greatest, smallest, pattern]

# ------------------------------------------------------------------ multiplication and division of larger numbers
KEY_M = [1260, 1680, 2520, 3360, 5040]
DOM_M = list(range(0, 10001))

def _mult4():
    def pairs(a, ylo, yhi, xlo, xhi):
        return [(a // y, y) for y in range(ylo, yhi + 1) if a % y == 0 and xlo <= a // y <= xhi]
    def times1(a, r):
        p = pairs(a, 2, 9, 100, 9999)
        if not p: return None
        x, y = r.choice(p)
        lines = r.choice([[f"{x} {X} {y} = {BOX}"], [f"{x} {X} {y}", f"= {BOX}"], [f"{x}", f"{X} {y}", f"= {BOX}"]])
        q = EQ(lines, a, form="4 digits by 1 digit"); q.sig = ("mult", x, y); return q
    def times2(a, r):
        p = pairs(a, 11, 99, 100, 999)
        if not p: return None
        x, y = r.choice(p)
        lines = r.choice([[f"{x} {X} {y} = {BOX}"], [f"{x} {X} {y}", f"= {BOX}"], [f"{x}", f"{X} {y}", f"= {BOX}"]])
        q = EQ(lines, a, form="3 digits by 2 digits"); q.sig = ("mult", x, y); return q
    def times_rev(a, r):
        p = pairs(a, 2, 9, 100, 9999)
        if not p: return None
        x, y = r.choice(p)
        lines = r.choice([[f"{y} {X} {x} = {BOX}"], [f"{y} {X} {x}", f"= {BOX}"]])
        q = EQ(lines, a, form="1 digit by 4 digits"); q.sig = ("mult", x, y); return q
    def missing(a, r):
        y = ch(r, range(2, 10)); z = a * y
        if z > 9999: return None
        lines = r.choice([[f"{BOX} {X} {y} = {z}"], [f"{BOX} {X} {y}", f"= {z}"]])
        q = EQ(lines, a, form="missing factor"); q.sig = ("mult", a, y); return q
    def divide(a, r):
        d = ch(r, range(2, 10)); n = a * d
        if n > 9999: return None
        lines = r.choice([[f"{n} {D} {d} = {BOX}"], [f"{n} {D} {d}", f"= {BOX}"], [f"{n}", f"{D} {d}", f"= {BOX}"]])
        q = EQ(lines, a, form="divide"); q.sig = ("div", n, d); return q
    def story_mult(a, r):
        p = pairs(a, 3, 9, 100, 999)
        if not p: return None
        x, y = r.choice(p)
        q = SEM([f"{y} trays of", f"{x} eggs: {BOX}"], lambda v, t_=a: v == t_, str(a), form="story multiply"); q.sig = ("mult", x, y); return q
    def story_div(a, r):
        d = ch(r, range(3, 9)); n = a * d
        if n > 9999: return None
        q = SEM([f"{n} stickers shared", f"among {d}. Each: {BOX}"], lambda v, t_=a: v == t_, str(a), form="story share"); q.sig = ("div", n, d); return q
    def two_step(a, r):
        y = ch(r, range(2, 9)); z = r.randint(5, 95)
        if (a + z) % y or (a + z) // y < 100: return None
        x = (a + z) // y
        lines = r.choice([[f"{x} {X} {y} {MINUS} {z} = {BOX}"], [f"{x} {X} {y} {MINUS} {z}", f"= {BOX}"]])
        q = EQ(lines, a, form="multiply then subtract"); q.sig = ("multsub", x, y, z); return q
    return [times1, times2, times_rev, missing, divide, story_mult, story_div, two_step]

# ------------------------------------------------------------------ decimals
KEY_D = [Fraction(3, 5), Fraction(5, 4), Fraction(12, 5), Fraction(61, 20), Fraction(5)]
DOM_D = [Fraction(i, 1000) for i in range(0, 10001)]

def ds(v):
    """a decimal as printed: 0.6, 1.25, 3.05, 5 (no trailing zero)"""
    v = Fraction(v)
    for p in range(0, 4):
        if (v * 10 ** p).denominator == 1:
            q = int(v * 10 ** p)
            if p == 0: return str(q)
            s = str(q).rjust(p + 1, "0"); return s[:-p] + "." + s[-p:]
    raise ValueError(v)

def places(v):
    v = Fraction(v)
    for p in range(0, 4):
        if (v * 10 ** p).denominator == 1: return p
    return 9

def _dec4():
    def holds_eq(t): return lambda v, t_=Fraction(t): v == t_
    def two_dp(r, lo, hi): return Fraction(r.randint(int(lo * 100), int(hi * 100)), 100)
    def add(a, r):
        for _ in range(60):
            x = two_dp(r, Fraction(1, 20), a - Fraction(1, 20)); y = a - x
            if y > 0 and (places(x) == 2 or places(y) == 2):
                lines = r.choice([[f"{ds(x)} + {ds(y)} = {BOX}"], [f"{ds(x)} + {ds(y)}", f"= {BOX}"], [f"{ds(x)}", f"+ {ds(y)}", f"= {BOX}"]])
                return SEM(lines, holds_eq(a), ds(a), form="add decimals")
        return None
    def sub(a, r):
        for _ in range(60):
            y = two_dp(r, Fraction(1, 20), Fraction(3)); x = a + y
            if x < 10 and (places(x) == 2 or places(y) == 2):
                lines = r.choice([[f"{ds(x)} {MINUS} {ds(y)} = {BOX}"], [f"{ds(x)} {MINUS} {ds(y)}", f"= {BOX}"], [f"{ds(x)}", f"{MINUS} {ds(y)}", f"= {BOX}"]])
                return SEM(lines, holds_eq(a), ds(a), form="subtract decimals")
        return None
    def mult(a, r):
        dd = [d for d in range(2, 10) if places(a / d) <= 2]
        if not dd: return None
        d = r.choice(dd)
        lines = r.choice([[f"{ds(a / d)} {X} {d} = {BOX}"], [f"{ds(a / d)} {X} {d}", f"= {BOX}"], [f"{ds(a / d)}", f"{X} {d}", f"= {BOX}"]])
        return SEM(lines, holds_eq(a), ds(a), form="multiply decimal")
    def div(a, r):
        dd = [d for d in range(2, 10) if places(a * d) <= 2]
        if not dd: return None
        d = r.choice(dd)
        lines = r.choice([[f"{ds(a * d)} {D} {d} = {BOX}"], [f"{ds(a * d)} {D} {d}", f"= {BOX}"], [f"{ds(a * d)}", f"{D} {d}", f"= {BOX}"]])
        return SEM(lines, holds_eq(a), ds(a), form="divide to a decimal")
    def rounding(a, r):
        p = places(a)
        if p == 0:
            x = a + Fraction(r.randint(-49, 49), 100)
            if x == a or places(x) == 0: return None
            return SEM([f"Round {ds(x)} to the", f"nearest whole number: {BOX}"], holds_eq(a), ds(a), form="round to whole")
        if p == 1:
            x = a + Fraction(r.choice([-4, -3, -2, -1, 1, 2, 3, 4]), 100)
            return SEM([f"Round {ds(x)} to", f"1 decimal place: {BOX}"], holds_eq(a), ds(a), form="round to 1 d.p.")
        if p == 2:
            x = a + Fraction(r.choice([-4, -3, -2, -1, 1, 2, 3, 4]), 1000)
            return SEM([f"Round {ds(x)} to", f"2 decimal places: {BOX}"], holds_eq(a), ds(a), form="round to 2 d.p.")
        return None
    def frac_dec(a, r):
        opts = []
        for d in (2, 4, 5, 10, 20, 25, 50, 100):
            n = a * d
            if n.denominator == 1 and n > 0 and Fraction(n, d) != 1: opts.append((int(n), d))
        if not opts: return None
        n, d = r.choice(opts)
        return SEM([f"{FRAC(n, d)} = {BOX}"], holds_eq(a), ds(a), form="fraction to decimal")
    def greatest(a, r):
        o = []
        for _ in range(30):
            c = a - ch(r, [Fraction(1, 100), Fraction(2, 100), Fraction(1, 10), Fraction(11, 100), Fraction(1, 1000)])
            if c > 0 and c not in o and c != a and places(c) <= 3: o.append(c)
            if len(o) == 2: break
        if len(o) < 2: return None
        ns = o + [a]; r.shuffle(ns)
        lines = r.choice([["Greatest of", ", ".join(ds(x) for x in ns) + f": {BOX}"], ["Greatest of", f"{ds(ns[0])}, {ds(ns[1])},", f"{ds(ns[2])}: {BOX}"]])
        return SEM(lines, holds_eq(a), ds(a), form="greatest decimal")
    def tenth(a, r):
        k = ch(r, [Fraction(1, 10), Fraction(1, 100)]); up = r.random() < .5
        base = a - k if up else a + k
        if base <= 0: return None
        w = "more" if up else "less"
        lines = r.choice([[f"{ds(k)} {w} than {ds(base)}", f"is {BOX}"], [f"{ds(k)} {w}", f"than {ds(base)}", f"is {BOX}"]])
        return SEM(lines, holds_eq(a), ds(a), form="more or less decimal")
    return [add, sub, mult, div, rounding, frac_dec, greatest, tenth]

def build_banks():
    B = {}
    B["numbers4"] = Bank("numbers4", "Numbers", "Numbers up to 100 000: place value, order, rounding", "Find the number. Find it in the key. Colour the part with that colour.",
        {2: T(KEY_N, DOM_N, _numbers4(), lambda v: nb(v))},
        parts=[("place value", lambda f, a: f in ("value of a digit", "expanded", "words to number")), ("rounding", lambda f, a: f.startswith("round")),
               ("comparing and ordering", lambda f, a: f in ("greatest of three", "smallest of three")), ("number patterns", lambda f, a: f == "number pattern"),
               ("10, 100, 1000 and 10 000 more or less", lambda f, a: f == "more or less")], prefix="Numbers up to 100 000: ")
    B["mult4"] = Bank("mult4", "Multiplying", "Multiplication and division with larger numbers", "Work it out. Find the answer in the key. Colour the part with that colour.",
        {2: T(KEY_M, DOM_M, _mult4(), lambda v: nb(v), maxuse={5040: 3})},
        parts=[("multiplication, 4 digits by 1 digit", lambda f, a: f in ("4 digits by 1 digit", "1 digit by 4 digits", "story multiply", "multiply then subtract", "missing factor")),
               ("multiplication, 3 digits by 2 digits", lambda f, a: f == "3 digits by 2 digits"), ("division, 4 digits by 1 digit", lambda f, a: f in ("divide", "story share"))], prefix="Four operations: ")
    B["dec4"] = Bank("dec4", "Decimals", "Decimals: operations, rounding, fractions as decimals", "Work it out. Find the answer in the key. Colour the part with that colour.",
        {2: T(KEY_D, DOM_D, _dec4(), lambda v: ds(v), maxuse={Fraction(5): 3})},
        parts=[("adding and subtracting decimals", lambda f, a: f in ("add decimals", "subtract decimals", "more or less decimal")),
               ("multiplying and dividing decimals", lambda f, a: f in ("multiply decimal", "divide to a decimal")),
               ("rounding decimals", lambda f, a: f.startswith("round")), ("fractions as decimals", lambda f, a: f == "fraction to decimal"),
               ("comparing decimals", lambda f, a: f == "greatest decimal")], prefix="Decimals: ")
    return B
BANKS = build_banks()

GALLERY = [
    dict(id="CBC-P4-01", picture="bus", bank="numbers4", tier=2, seed=401),
    dict(id="CBC-P4-02", picture="lorry", bank="mult4", tier=2, seed=402),
    dict(id="CBC-P4-03", picture="ferry", bank="dec4", tier=2, seed=403),
]
