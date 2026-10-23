"""Primary 3 topic banks for the colour-by-code pages of the school booklets (level file: LEVEL, RULES, BANKS, GALLERY).
Written for school/p3 (vendored copy; school/colour_by_code is not edited). Every question is an equation or a short sentence that
textcheck.py re-solves from the printed text. Money is written $3.45; units km, m, cm, kg, g, ℓ, mℓ; the sign ÷ is allowed."""
import math, re
import art as A
from qcore import *

LEVEL = 3
RULES = dict(allow_division_sign=True, time_words_only=False)
X, D = TIMES, DIVIDE
def ch(r, seq): return r.choice(list(seq))

# ------------------------------------------------------------------ tables of 6, 7, 8 and 9: multiplication and division facts
def _mult3(tier):
    def facts(n):
        return [(x, n // x) for x in range(2, 10) if n % x == 0 and 2 <= n // x <= 9 and (x >= 6 or n // x >= 6)]
    def times(a, r):
        p = facts(a)
        if not p: return None
        x, y = r.choice(p)
        q = EQ([f"{x} {X} {y} = {BOX}"], a, form="times"); q.sig = ("mult", min(x, y), max(x, y)); return q
    def times2(a, r):
        p = facts(a)
        if not p: return None
        x, y = r.choice(p)
        q = SEM([f"{x} groups of {y}", f"is {BOX}"], lambda v, t_=a: v == t_, str(a), form="groups of"); q.sig = ("mult2", min(x, y), max(x, y)); return q
    def times3(a, r):
        p = facts(a)
        if not p: return None
        x, y = r.choice(p)
        q = SEM([f"Multiply {y} by {x}.", f"{BOX}"], lambda v, t_=a: v == t_, str(a), form="multiply"); q.sig = ("mult3", min(x, y), max(x, y)); return q
    def missing(a, r):                         # x x [] = p with the answer a (a is a factor)
        if a > 9: return None
        x = r.randint(6, 9) if r.random() < .6 else r.randint(2, 9)
        if a * x > 81: return None
        q = EQ([f"{x} {X} {BOX} = {a * x}"], a, form="missing factor"); q.sig = ("mf", x, a * x); return q
    def missing2(a, r):
        if a > 9: return None
        x = r.randint(6, 9) if r.random() < .6 else r.randint(2, 9)
        if a * x > 81: return None
        q = EQ([f"{BOX} {X} {x} = {a * x}"], a, form="missing factor first"); q.sig = ("mf", x, a * x); return q
    def div(a, r):
        if a > 9: return None
        y = r.randint(6, 9) if r.random() < .7 else r.randint(2, 9)
        if a * y > 81: return None
        q = EQ([f"{a * y} {D} {y} = {BOX}"], a, form="divide"); q.sig = ("div", a * y, y); return q
    def div2(a, r):
        if a > 9: return None
        y = r.randint(6, 9) if r.random() < .7 else r.randint(2, 9)
        if a * y > 81: return None
        q = SEM([f"{a * y} {D} {y}", f"= {BOX}"], lambda v, t_=a: v == t_, str(a), form="divide, two lines"); q.sig = ("div2", a * y, y); return q
    def div3(a, r):
        if a > 9 or a < 3: return None
        y = r.randint(6, 9) if r.random() < .7 else r.randint(3, 9)
        if a * y > 81: return None
        q = EQ([f"{a * y} {D} {BOX} = {y}"], a, form="missing divisor"); q.sig = ("dd", a * y, y); return q
    def bags(a, r):
        p = facts(a)
        if not p: return None
        x, y = r.choice(p)
        q = SEM([f"{x} bags, {y} in each.", f"Altogether {BOX}"], lambda v, t_=a: v == t_, str(a), form="bags"); q.sig = ("mult4", min(x, y), max(x, y)); return q
    forms = [times, times2, times3, bags, missing, missing2, div, div2]
    return forms

# ------------------------------------------------------------------ units: km and m, m and cm, kg and g, l and ml
def _conv3(tier):
    def km_m(a, r):
        if a % 1000 == 0 and 1000 <= a <= 9000:
            k = a // 1000; q = SEM([f"{k} km = {BOX} m"], lambda v, t_=a: v == t_, str(a), form="km to m"); q.sig = ("conv", "km", k); return q
        return None
    def km_m_add(a, r):
        if a % 1000 in (250, 500, 750) and a >= 1250:
            k, m = divmod(a, 1000)
            q = SEM([f"{k} km + {m} m", f"= {BOX} m"], lambda v, t_=a: v == t_, str(a), form="km and m, two lines"); q.sig = ("convadd", "km", a); return q
        return None
    def m_cm(a, r):
        if a % 100 == 0 and 500 <= a <= 9000:
            k = a // 100; q = SEM([f"{k} m = {BOX} cm"], lambda v, t_=a: v == t_, str(a), form="m to cm"); q.sig = ("conv", "m", k); return q
        return None
    def kg_g(a, r):
        if a % 1000 == 0 and 1000 <= a <= 9000:
            k = a // 1000; q = SEM([f"{k} kg = {BOX} g"], lambda v, t_=a: v == t_, str(a), form="kg to g"); q.sig = ("conv", "kg", k); return q
        return None
    def kg_g_add(a, r):
        if a % 1000 in (250, 500, 750) and a >= 1250:
            k, m = divmod(a, 1000)
            q = SEM([f"{k} kg + {m} g", f"= {BOX} g"], lambda v, t_=a: v == t_, str(a), form="kg and g, two lines"); q.sig = ("convadd", "kg", a); return q
        return None
    def l_ml(a, r):
        if a % 1000 == 0 and 1000 <= a <= 9000:
            k = a // 1000; q = SEM([f"{k} ℓ = {BOX} mℓ"], lambda v, t_=a: v == t_, str(a), form="l to ml"); q.sig = ("conv", "l", k); return q
        return None
    def l_ml_add(a, r):
        if a % 1000 in (250, 500, 750) and a >= 1250:
            k, m = divmod(a, 1000)
            q = SEM([f"{k} ℓ + {m} mℓ", f"= {BOX} mℓ"], lambda v, t_=a: v == t_, str(a), form="l and ml, two lines"); q.sig = ("convadd", "l", a); return q
        return None
    def take(a, r):
        s = r.choice([("km", "m", 1000), ("kg", "g", 1000), ("ℓ", "mℓ", 1000)])
        top = a + r.choice([250, 500, 750])
        if top % 1000 or top // 1000 > 9: return None
        q = SEM([f"{top // 1000} {s[0]} {MINUS} {top - a} {s[1]}", f"= {BOX} {s[1]}"], lambda v, t_=a: v == t_, str(a), form="take away a part"); q.sig = ("take", s[0], top, a); return q
    return [km_m, km_m_add, m_cm, kg_g, kg_g_add, l_ml, l_ml_add, take]

# ------------------------------------------------------------------ money in decimal notation: adding and subtracting
def dec(c): return f"{c // 100}.{c % 100:02d}"
def usd(c): return f"${c // 100}.{c % 100:02d}"
def _money3(tier):
    def add(a, r):
        x = r.randrange(50, a - 45, 5)
        if a - x < 50: return None
        q = EQ([f"{usd(x)} + {usd(a - x)}", f"= ${BOX}"], a, dec(a), money=True, form="add"); q.sig = ("add", min(x, a - x)); return q
    def add3(a, r):
        x = r.randrange(50, a - 100, 5) if a > 160 else None
        if x is None: return None
        y = r.randrange(50, a - x - 49, 5) if a - x - 49 > 50 else None
        if y is None: return None
        q = EQ([f"{usd(x)} + {usd(y)} + {usd(a - x - y)} = ${BOX}"], a, dec(a), money=True, form="add three"); q.sig = ("add3", x, y); return q
    def sub(a, r):
        b = r.randrange(50, 1000, 5)
        q = EQ([f"{usd(a + b)} {MINUS} {usd(b)}", f"= ${BOX}"], a, dec(a), money=True, form="subtract"); q.sig = ("sub", a + b, b); return q
    def change(a, r):
        for top in (500, 1000, 2000, 5000):
            if a < top - 45 and r.random() < .6:
                q = EQ([f"{usd(top)} {MINUS} {usd(top - a)}", f"= ${BOX}"], a, dec(a), money=True, form="change"); q.sig = ("chg", top, a); return q
        return None
    def left(a, r):
        b = r.randrange(50, 800, 5)
        q = SEM([f"Has {usd(a + b)}. Spends {usd(b)}.", f"Left: ${BOX}"], lambda v, t_=a: v == t_, dec(a), form="has and spends"); q.sig = ("left", a + b, b); return q
    def both(a, r):
        x = r.randrange(50, a - 45, 5)
        if a - x < 50: return None
        q = SEM([f"Pen {usd(x)}, ruler {usd(a - x)}.", f"Both: ${BOX}"], lambda v, t_=a: v == t_, dec(a), form="two items"); q.sig = ("both", min(x, a - x)); return q
    return [add, sub, change, left, both]

def build_banks():
    B = {}
    B["mult3"] = Bank("mult3", "Tables", "Multiplication and division: tables of 6, 7, 8 and 9", "Work out the answer. Find it in the key. Colour the part with that colour.",
        {2: T([6, 7, 9, 24, 36], range(0, 101), _mult3(2), maxuse={24: 2, 36: 2})})
    B["conv3"] = Bank("conv3", "Measures", "Changing units: km, m, cm, kg, g, ℓ and mℓ", "Change the units. Find the answer in the key. Colour the part with that colour.",
        {2: T([1500, 2500, 3000, 4500, 6000], range(0, 10001), _conv3(2), lambda v: str(v))})
    B["money3"] = Bank("money3", "Money", "Money: adding and subtracting in dollars and cents", "Find how much. Find it in the key. Colour the part with that colour.",
        {2: T([235, 450, 680, 805, 1275], range(0, 3001), _money3(2), lambda v: f"${dec(v)}")})
    return B
BANKS = build_banks()

GALLERY = [
    dict(id="CBC-P3-01", picture="castle", bank="mult3", tier=2, seed=3401),
    dict(id="CBC-P3-02", picture="sailboat", bank="conv3", tier=2, seed=3402),
    dict(id="CBC-P3-03", picture="butterfly", bank="money3", tier=2, seed=3403),
]
