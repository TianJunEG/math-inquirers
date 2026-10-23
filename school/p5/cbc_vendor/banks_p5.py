"""Primary 5 topic banks for the two colour-by-code pages of the P5 booklets (level file: LEVEL, RULES, BANKS, GALLERY).
Wording: order of operations with brackets (Whole Numbers 2.2 and 2.3) and percentages (a percentage part of a whole, a part as a percentage, discount, GST).
Every form is form(answer, rng) -> Q or None."""
import math
from qcore import *

LEVEL = 5
RULES = dict(allow_division_sign=True, time_words_only=False)
X, D = TIMES, DIVIDE

def _eq(lines, a, form):
    return EQ(lines, a, form=form)

def _ops(tier):
    def f_add_mul(a, r):
        for _ in range(200):
            q_, s_ = r.randint(2, 9), r.randint(2, 9); p = a - q_ * s_
            if p >= 2: return _eq([f"{p} + {q_} {X} {s_} = {BOX}"], a, "a + b x c")
    def f_sub_div(a, r):
        for _ in range(200):
            c = r.randint(2, 9); b = c * r.randint(2, 9); p = a + b // c
            if p <= 99: return _eq([f"{p} {MINUS} {b} {D} {c} = {BOX}"], a, "a - b / c")
    def f_br_mul(a, r):
        divs = [d for d in range(2, 10) if a % d == 0]
        for _ in range(200):
            if not divs: return None
            c = r.choice(divs); s = a // c; p = r.randint(1, s - 1) if s > 1 else 0
            if p >= 1: return _eq([f"({p} + {s - p}) {X} {c} = {BOX}"], a, "(a + b) x c")
    def f_mul_br(a, r):
        divs = [d for d in range(2, 10) if a % d == 0]
        for _ in range(200):
            if not divs: return None
            c = r.choice(divs); s = a // c; q_ = r.randint(2, 12); p = q_ + s
            if s >= 2: return _eq([f"{c} {X} ({p} {MINUS} {q_}) = {BOX}"], a, "a x (b - c)")
    def f_div_br(a, r):
        for _ in range(300):
            s = r.randint(2, 6); t = r.randint(2, 6); n = (s + t) * r.randint(2, 9)
            c = n // (s + t)
            if a % c == 0 and a // c >= 2 and a // c <= 9: return _eq([f"{n} {D} ({s} + {t}) {X} {a // c} = {BOX}"], a, "a / (b + c) x d")
    def f_two_ops(a, r):
        for _ in range(300):
            c = r.randint(2, 9); b = c * r.randint(2, 9); d_ = r.randint(2, 9); e = a - b // c * 1
            if e >= 2: return _eq([f"{b} {D} {c} + {e}", f"= {BOX}"], a, "a / b + c")
    def f_br_div_add(a, r):
        for _ in range(300):
            c = r.randint(2, 6); s = r.randint(2, 9) * c; rest = a - s // c
            if rest >= 2:
                p = r.randint(1, s - 1); return _eq([f"({p} + {s - p}) {D} {c} + {rest}", f"= {BOX}"], a, "(a + b) / c + d")
    forms = [f_add_mul, f_sub_div, f_br_mul, f_mul_br, f_div_br, f_two_ops, f_br_div_add]
    return forms

PCTS = [5, 10, 15, 20, 25, 30, 40, 50, 60, 75]
def _pct(tier):
    def of(a, r):
        ps = [p for p in PCTS if (a * 100) % p == 0 and (a * 100) // p <= 1000 and (a * 100) // p > a]
        if not ps: return None
        p = r.choice(ps); n = a * 100 // p
        return SEM([f"{p}% of {n}", f"= {BOX}"], lambda v, t_=a: v == t_, str(a), form="p% of n")
    def out_of(a, r):
        if a > 100: return None
        ns = [n for n in (10, 20, 25, 40, 50, 100, 200, 250, 500) if (a * n) % 100 == 0 and a * n // 100 < n]
        if not ns: return None
        n = r.choice(ns); k = a * n // 100
        return SEM([f"{k} out of {n}", f"= {BOX}%"], lambda v, t_=a: v == t_, str(a), form="k out of n")
    def off(a, r):
        for _ in range(200):
            p = r.choice([10, 20, 25, 30, 40, 50]); n = r.choice([20, 40, 50, 60, 80, 100, 120, 150, 200, 240, 250, 300])
            if (n * p) % 100 == 0 and n - n * p // 100 == a: return SEM([f"{n} {MINUS} {p}% of {n}", f"= {BOX}"], lambda v, t_=a: v == t_, str(a), form="n - p% of n")
    def plus(a, r):
        for _ in range(200):
            p = r.choice([10, 20, 25, 50, 5, 15]); n = r.choice([20, 40, 60, 80, 100, 120, 160, 200, 240, 300])
            if (n * p) % 100 == 0 and n + n * p // 100 == a: return SEM([f"{n} + {p}% of {n}", f"= {BOX}"], lambda v, t_=a: v == t_, str(a), form="n + p% of n")
    return [of, out_of, off, plus]

BANKS = {
    "ops": Bank("ops", "Order of Operations", "Whole numbers: order of operations and brackets", "Work out the answer. Find it in the key. Colour the part with that colour.",
                {1: T([12, 18, 24, 30, 36], range(0, 301), _ops(1)), 2: T([14, 21, 28, 35, 42], range(0, 301), _ops(2))}),
    "pct": Bank("pct", "Percentages", "Percentage: a part of a whole, a percentage of a quantity, discount and GST", "Work out the answer. Find it in the key. Colour the part with that colour.",
                {1: T([12, 20, 25, 40, 60], range(0, 1001), _pct(1)), 2: T([15, 30, 45, 75, 90], range(0, 1001), _pct(2))}),
}
GALLERY = [dict(id="CBC-P5-01", picture="rocket", bank="ops", tier=1, seed=501), dict(id="CBC-P5-02", picture="house", bank="pct", tier=1, seed=502)]
