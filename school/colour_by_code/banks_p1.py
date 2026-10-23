"""Primary 1 topic banks (level file: LEVEL, RULES, BANKS, GALLERY). See banks.py for how level files are found.
A bank knows nothing about pictures: it makes one question for any wanted answer (see qcore.py)."""
import random, re
import art as A
from qcore import *

LEVEL = 1
RULES = dict(allow_division_sign=False, time_words_only=True)   # wording rules the verifier applies to this level's pages

# ------------------------------------------------------------------ addition within 20
def _add1(a, r):
    out = []
    def sum_(a, r):
        x = r.randint(2, a - 2); return EQ([f"{x} + {a - x} = {BOX}"], a, form="sum")
    def rev(a, r):
        x = r.randint(2, a - 2); return EQ([f"{BOX} = {x} + {a - x}"], a, form="sum-reversed")
    def miss(a, r):
        x = r.randint(2, min(9, 20 - a)); return EQ([f"{x} + {BOX} = {a + x}"], a, form="missing addend")
    def more(a, r):
        x = r.randint(2, a - 2)
        return SEM([f"{x} more than {a - x}", f"is {BOX}"], lambda v, s=a: v == s, str(a), form="more than")
    def make(a, r):
        x = r.randint(2, a - 2)
        return SEM([f"{x} and {a - x}", f"make {BOX}"], lambda v, s=a: v == s, str(a), form="make")
    return [sum_, rev, miss, more, make]
def _add2(a, r):
    def sum_(a, r):
        x = r.randint(max(5, a - 9), min(9, a - 5)); return EQ([f"{x} + {a - x} = {BOX}"], a, form="sum, larger")
    def three(a, r):
        x = r.randint(3, 8); y = r.randint(3, 8); z = a - x - y
        if not 2 <= z <= 9: return None
        return EQ([f"{x} + {y} + {z} = {BOX}"], a, form="three numbers")
    def miss(a, r):
        x = r.randint(2, min(8, 20 - a)); return EQ([f"{x} + {BOX} = {a + x}"], a, form="missing addend")
    def more(a, r):
        x = r.randint(5, 9); return SEM([f"{x} more than {a - x}", f"is {BOX}"], lambda v, s=a: v == s, str(a), form="more than")
    def two(a, r):
        x = r.randint(3, 8); y = r.randint(2, 8); z = a - x - y
        if not 1 <= z <= 9: return None
        return EQ([f"{x} + {y}", f"+ {z} = {BOX}"], a, form="two-step")
    def three_miss(a, r):
        x = r.randint(3, 6); z = r.randint(3, 6)
        if a + x + z > 20: return None
        return EQ([f"{x} + {BOX} + {z} = {a + x + z}"], a, form="three, one missing")
    return [sum_, three, miss, more, two, three_miss]

# ------------------------------------------------------------------ subtraction within 20
def _sub1():
    def diff(a, r):
        s = r.randint(2, 9); return EQ([f"{a + s} {MINUS} {s} = {BOX}"], a, form="difference")
    def miss(a, r):
        m = r.randint(a + 3, 15); return EQ([f"{m} {MINUS} {BOX} = {m - a}"], a, form="missing number taken away")
    def first(a, r):
        s = r.randint(1, 5); return EQ([f"{BOX} {MINUS} {s} = {a - s}"], a, form="missing start") if a - s >= 1 else None
    def fewer(a, r):
        s = r.randint(2, 8); return SEM([f"{s} fewer than", f"{a + s} is {BOX}"], lambda v, t=a: v == t, str(a), form="fewer than")
    def take(a, r):
        s = r.randint(2, 8); return SEM([f"{a + s} take away {s}", f"is {BOX}"], lambda v, t=a: v == t, str(a), form="take away")
    return [diff, miss, first, fewer, take]
def _sub2():
    def diff(a, r):
        s = r.randint(5, 9); return EQ([f"{a + s} {MINUS} {s} = {BOX}"], a, form="difference, larger") if a + s <= 20 else None
    def two(a, r):
        s = r.randint(2, 6); t = r.randint(2, 5)
        return EQ([f"{a + s + t} {MINUS} {s}", f"{MINUS} {t} = {BOX}"], a, form="two-step subtract") if a + s + t <= 20 else None
    def mix(a, r):
        s = r.randint(3, 8); t = r.randint(2, 5)
        return EQ([f"{a - t + s} {MINUS} {s}", f"+ {t} = {BOX}"], a, form="subtract then add") if a - t + s <= 20 else None
    def miss(a, r):
        m = r.randint(max(a + 4, 14), 20); return EQ([f"{m} {MINUS} {BOX} = {m - a}"], a, form="missing number taken away")
    def fewer(a, r):
        s = r.randint(4, 9)
        return SEM([f"{s} fewer than", f"{a + s} is {BOX}"], lambda v, t=a: v == t, str(a), form="fewer than") if a + s <= 20 else None
    return [diff, two, mix, miss, fewer]

# ------------------------------------------------------------------ number bonds to 10 and 20
def _bond(total):
    def f1(a, r): return EQ([f"{total - a} + {BOX} = {total}"], a, form="b + _ = T")
    def f2(a, r): return EQ([f"{BOX} + {total - a} = {total}"], a, form="_ + b = T")
    def f3(a, r): return EQ([f"{total} {MINUS} {total - a} = {BOX}"], a, form="T - b = _")
    def f4(a, r): return EQ([f"{total} = {total - a} + {BOX}"], a, form="T = b + _")
    def f5(a, r): return EQ([f"{total} {MINUS} {BOX} = {total - a}"], a, form="T - _ = b")
    def f6(a, r): return SEM([f"{total - a} and {BOX}", f"make {total}"], lambda v, b=total - a, T=total: v + b == T, str(a), form="make T")
    def f7(a, r): return SEM([f"Make {total} with {total - a}:", f"{BOX}"], lambda v, b=total - a, T=total: v + b == T, str(a), form="make T with b")
    def f8(a, r): return SEM([f"{total - a} needs {BOX} more", f"to make {total}"], lambda v, b=total - a, T=total: v + b == T, str(a), form="b needs _ more")
    return [f1, f2, f3, f4, f5, f6, f7, f8]

# ------------------------------------------------------------------ place value
def tn(t): return "1 ten" if t == 1 else f"{t} tens"
def on(o): return "1 one" if o == 1 else f"{o} ones"
def _pv(tier):
    lo, hi = (1, 5) if tier == 1 else (5, 9)
    def tens_a(a, r):
        o = r.randint(0, 9); n = 10 * a + o
        return SEM(["How many tens", f"in {n}? {BOX}"], lambda v, n=n: v == n // 10, str(a), form="how many tens")
    def tens_b(a, r):
        o = r.randint(0, 9); n = 10 * a + o
        return SEM([f"{n} = {BOX} tens", on(o)], lambda v, n=n, o=o: 10 * v + o == n, str(a), form="n = _ tens _ ones")
    def tens_c(a, r):
        o = r.randint(1, 9)
        return SEM([f"{10 * a} + {o}", f"= {BOX} tens {on(o)}"], lambda v, a=a: 10 * v == 10 * a, str(a), form="expanded to tens")
    def ones_a(a, r):
        t = r.randint(1, 5 if tier == 1 else 9); n = 10 * t + a
        return SEM(["How many ones", f"in {n}? {BOX}"], lambda v, n=n: v == n % 10, str(a), form="how many ones")
    def ones_b(a, r):
        t = r.randint(1, 5 if tier == 1 else 9); n = 10 * t + a
        return SEM([f"{n} = {tn(t)}", f"{BOX} ones"], lambda v, n=n, t=t: 10 * t + v == n, str(a), form="n = t tens _ ones")
    def ones_c(a, r):
        t = r.randint(1, 5 if tier == 1 else 9); n = 10 * t + a
        return EQ([f"{10 * t} + {BOX} = {n}"], a, form="tens + _ = n")
    forms = [tens_a, tens_b, tens_c, ones_a, ones_b, ones_c]
    if tier == 2:
        def more10(a, r):
            o = r.randint(0, 9); m = 10 * (a - 1) + o
            return SEM([f"10 more than {m}:", f"tens digit {BOX}"], lambda v, m=m: v == (m + 10) // 10, str(a), form="10 more, tens digit")
        def less10(a, r):
            if a == 9: return None
            o = r.randint(0, 9); m = 10 * (a + 1) + o
            return SEM([f"10 less than {m}:", f"tens digit {BOX}"], lambda v, m=m: v == (m - 10) // 10, str(a), form="10 less, tens digit")
        forms += [more10, less10]
    return forms

# ------------------------------------------------------------------ counting in 2s, 5s and 10s
def _count(tier):
    def seq_line(terms, blank):
        return ", ".join(BOX if i == blank else str(t) for i, t in enumerate(terms))
    def ap(terms_blank):
        terms, blank, desc = terms_blank
        def holds(v):
            t = list(terms); t[blank] = v
            d = {t[i + 1] - t[i] for i in range(len(t) - 1)}
            return len(d) == 1 and 0 not in d and min(t) >= 0 and max(t) <= 100
        return holds
    def mk(a, r, rule, back, blank_pos):
        steps = [5] + ([10] if a % 10 == 0 else []) + ([2] if a % 2 == 0 else [])
        s = r.choice(steps)
        sign = -s if back else s
        start = a - sign * blank_pos
        terms = [start + sign * i for i in range(4)]
        if min(terms) < 0 or max(terms) > 100: return None
        blank = blank_pos
        lines = []
        if rule: lines.append(("Count back in " if back else "Count in ") + f"{s}s:")
        lines.append(seq_line(terms, blank))
        q = Q(lines, ap((terms, blank, "")), form=("back " if back else "") + f"{s}s" + (", rule shown" if rule else ""))
        q.sol = [mark(l, str(a)) for l in lines]
        q.seq = (terms, blank)
        return q
    def f_rule(a, r): return mk(a, r, True, False, r.choice([1, 2, 3]))
    def f_norule(a, r): return mk(a, r, False, False, r.choice([0, 2, 3]))
    def f_back(a, r): return mk(a, r, True, True, r.choice([1, 2, 3]))
    def f_back2(a, r): return mk(a, r, False, True, r.choice([0, 1, 3]))
    def f_steps(a, r):
        steps = [5] + ([10] if a % 10 == 0 else [])
        s = r.choice(steps); start = a - 4 * s
        if start < 0: return None
        return SEM([f"Start at {start}.", f"Count on 4 times in {s}s:", f"{BOX}"], lambda v, t=a: v == t, str(a), form="start and count on")
    forms = [f_rule, f_norule, f_back, f_back2]
    if tier == 2: forms.append(f_steps)
    return forms

# ------------------------------------------------------------------ comparing and ordering numbers to 100
def _cmp(tier):
    KEY = (20, 30, 40, 50, 60) if tier == 1 else (55, 60, 65, 70, 75)         # the colour key of this tier
    def three(a, r, greatest):
        # every number offered is a key value, so finding the number on the key does not answer the question: the pupil has to compare
        pool = [k for k in KEY if (k < a if greatest else k > a)]
        if len(pool) < 2: return None
        nums = r.sample(pool, 2) + [a]; r.shuffle(nums)
        pick = max if greatest else min
        return SEM(["Greatest:" if greatest else "Smallest:", "  ".join(map(str, nums))], lambda v, ns=tuple(nums), p=pick: v == p(ns), str(a), form="greatest" if greatest else "smallest")
    def greatest(a, r): return three(a, r, True)
    def smallest(a, r): return three(a, r, False)
    def more1(a, r): return SEM([f"1 more than {a - 1}", f"is {BOX}"], lambda v, t=a: v == t, str(a), form="1 more")
    def less1(a, r): return SEM([f"1 less than {a + 1}", f"is {BOX}"], lambda v, t=a: v == t, str(a), form="1 less")
    def more10(a, r): return SEM([f"10 more than {a - 10}", f"is {BOX}"], lambda v, t=a: v == t, str(a), form="10 more")
    def less10(a, r): return SEM([f"10 less than {a + 10}", f"is {BOX}"], lambda v, t=a: v == t, str(a), form="10 less")
    def between(a, r): return SEM([f"Between {a - 1} and {a + 1}", f"is {BOX}"], lambda v, t=a: a - 1 < v < a + 1 and v == t, str(a), form="between")
    forms = [greatest, smallest, more1, less1, more10, less10]
    if tier == 2:
        def middle(a, r):
            lo, hi = [k for k in KEY if k < a], [k for k in KEY if k > a]
            if not lo or not hi: return None
            nums = [r.choice(lo), a, r.choice(hi)]                       # all three are key values
            r.shuffle(nums)
            return SEM(["Middle number:", "  ".join(map(str, nums))], lambda v, ns=tuple(nums): v == sorted(ns)[1], str(a), form="middle number")
        def two(a, r):
            return SEM([f"10 more than {a - 11},", f"then 1 more: {BOX}"], lambda v, t=a: v == t, str(a), form="10 more then 1 more")
        def two_b(a, r):
            return SEM([f"10 less than {a + 9},", f"then 1 more: {BOX}"], lambda v, t=a: v == t, str(a), form="10 less then 1 more") if a + 9 <= 100 else None   # a + 9 - 10 + 1 = a
        forms += [middle, two, two_b]
    else:
        forms.append(between)
    return forms

# ------------------------------------------------------------------ money (cents at one star, dollars at two stars)
def _coin_sets(a):
    vals = [5, 10, 20, 50]
    out = []
    def rec(left, cur, mx):
        if left == 0:
            if 2 <= len(cur) <= 4 or (len(cur) == 1): out.append(list(cur)); return
        if len(cur) >= 4: return
        for v in vals:
            if v <= left and v <= mx: rec(left - v, cur + [v], v)
    rec(a, [], 50)
    return [c for c in out if len(c) >= 2] or out

def _money1():
    S = "¢"
    def coins_(a, r):
        cs = r.choice(_coin_sets(a)); r.shuffle(cs)
        art = A.coins(cs)
        return SEM(["How much?", f"{BOX}{S}"], lambda v, t=a: v == t, str(a), art=art, form="count the coins")
    def coins_row(a, r):
        cs = r.choice(_coin_sets(a)); r.shuffle(cs)
        return SEM([f"{BOX}{S}"], lambda v, t=a: v == t, str(a), art=A.coins(cs), form="coins, answer only")
    def sum_(a, r):
        x = r.choice([v for v in range(5, a, 5)]); return EQ([f"{x}{S} + {a - x}{S} = {BOX}{S}"], a, str(a), form="add cents")
    def miss(a, r):
        x = r.choice([v for v in range(5, 50, 5)]); return EQ([f"{x}{S} + {BOX}{S} = {a + x}{S}"], a, str(a), form="missing cents")
    def spend(a, r):
        s = r.choice([v for v in range(5, 55, 5)]); return EQ([f"{a + s}{S} {MINUS} {s}{S} = {BOX}{S}"], a, str(a), form="cents left")
    def more(a, r):
        x = r.choice([v for v in range(5, a, 5)])
        return SEM([f"I have {x}{S}.", f"I get {a - x}{S} more.", f"Now {BOX}{S}"], lambda v, t=a: v == t, str(a), form="get more")
    def fewer(a, r):
        s = r.choice([5, 10, 20]); return SEM([f"Ann has {a + s}{S}.", f"Ben has {s}{S} fewer.", f"Ben: {BOX}{S}"], lambda v, t=a: v == t, str(a), form="fewer than")
    return [coins_, coins_row, sum_, miss, spend, more, fewer]
def _money2():
    def notes_(a, r):
        sets = {12: [[10, 2]], 14: [[10, 2, 2], [5, 5, 2, 2]], 16: [[10, 5, 1], [10, 2, 2, 2]], 18: [[10, 5, 2, 1], [10, 2, 2, 2, 2]], 20: [[10, 10], [10, 5, 5]]}
        ns = r.choice([s for s in sets[a] if len(s) <= 4]); ns = list(ns); r.shuffle(ns)
        return SEM(["How much?", f"${BOX}"], lambda v, t=a: v == t, str(a), art=A.notes(ns), form="count the notes")
    def sum_(a, r):
        x = r.randint(5, a - 5); return EQ([f"${x} + ${a - x} = ${BOX}"], a, str(a), form="add dollars")
    def more(a, r):
        x = r.randint(5, 9)
        return SEM([f"Ann has ${a - x}.", f"Ben has ${x} more.", f"Ben has ${BOX}"], lambda v, t=a: v == t, str(a), form="more than")
    def both(a, r):
        x = r.randint(4, a - 4)
        return SEM([f"A toy costs ${x}.", f"A ball costs ${a - x}.", f"Both cost ${BOX}"], lambda v, t=a: v == t, str(a), form="two prices")
    def left(a, r):
        s = r.randint(3, 8)
        return EQ([f"${a + s} {MINUS} ${s} = ${BOX}"], a, str(a), form="dollars left") if a + s <= 28 else None
    def fewer(a, r):
        s = r.randint(3, 8)
        return SEM([f"Ann has ${a + s}.", f"Tom has ${s} fewer.", f"Tom: ${BOX}"], lambda v, t=a: v == t, str(a), form="fewer than") if a + s <= 28 else None
    return [notes_, sum_, more, both, left, fewer]

# ------------------------------------------------------------------ time (o'clock and half past only)
def cyc(x): return (x - 1) % 12 + 1
def tword(t): return f"{t[0]} o'clock" if t[1] == 0 else f"half past {t[0]}"
def _time(tier):
    def clock_stack(a, r):
        if A.hand_gap(*a) < A.CLOCK_MIN_GAP: return None
        return SEM(["What time is it?"], lambda v, t=a: v == t, tword(a), art=A.clock(*a), form="clock face, stacked")
    def clock_row(a, r):
        if A.hand_gap(*a) < A.CLOCK_MIN_GAP: return None
        return SEM(["What", "time", "is it?"], lambda v, t=a: v == t, tword(a), art=A.clock(*a), layout="row", form="clock face, beside text")
    def digital(a, r):
        h, m = a
        lines = r.choice([["Which time is", f"{h}:{m:02d}? {BOX}"], [f"{h}:{m:02d} is", f"which time? {BOX}"], [f"{h}:{m:02d} is the same as", f"which time? {BOX}"]])      # always a blank, so the teacher page shows the time as well as the colour
        return SEM(lines, lambda v, t=a: v == t, tword(a), form="digital time")
    def later(a, r):
        h, m = a
        if m == 0: return SEM([f"It is {cyc(h - 1)} o'clock.", f"1 hour later: {BOX}"], lambda v, t=a: v == t, tword(a), form="1 hour later")
        return SEM([f"It is {h} o'clock.", f"Half an hour later: {BOX}"], lambda v, t=a: v == t, tword(a), form="half an hour later")
    def later1(a, r):
        h, m = a
        if m == 0: return SEM([f"It is half past {cyc(h - 1)}.", f"Half an hour later: {BOX}"], lambda v, t=a: v == t, tword(a), form="half an hour after half past")
        return SEM([f"It is {cyc(h + 1)} o'clock.", f"Half an hour before: {BOX}"], lambda v, t=a: v == t, tword(a), form="half an hour before")
    def clock_alone(a, r):
        if A.hand_gap(*a) < A.CLOCK_MIN_GAP: return None
        q = SEM([], lambda v, t=a: v == t, tword(a), art=A.clock(*a), form="clock face alone")
        q.sol = ["\u27e6" + tword(a) + "\u27e7"]
        return q
    def clock_short(a, r):
        if A.hand_gap(*a) < A.CLOCK_MIN_GAP: return None
        return SEM([f"{BOX}"], lambda v, t=a: v == t, tword(a), art=A.clock(*a), form="clock face, answer only")
    forms = [clock_stack, clock_row, clock_alone, clock_short, digital, later, later1]
    if tier == 2:
        def later2(a, r):
            h, m = a
            if m == 0: return SEM([f"It is half past {cyc(h - 1)}.", f"Half an hour later: {BOX}"], lambda v, t=a: v == t, tword(a), form="half an hour after half past")
            return SEM([f"It is half past {cyc(h - 1)}.", f"1 hour later: {BOX}"], lambda v, t=a: v == t, tword(a), form="1 hour after half past")
        def before(a, r):
            h, m = a
            if m == 30: return SEM([f"It is {cyc(h + 1)} o'clock.", f"Half an hour before: {BOX}"], lambda v, t=a: v == t, tword(a), form="half an hour before")
            return SEM([f"It is {cyc(h + 1)} o'clock.", f"1 hour before: {BOX}"], lambda v, t=a: v == t, tword(a), form="1 hour before")
        forms += [later2, before]
    return forms

# ------------------------------------------------------------------ length in cm
def _len(tier):
    top_max = 10 if tier == 1 else 13
    def rl(a, r, start):
        end = start + a
        if end > top_max: return None
        art = A.ruler(start, end, top=end + 1)
        return SEM([f"{BOX} cm"], lambda v, t=a: v == t, str(a), art=art, form="ruler from %d" % start)
    def ruler0(a, r): return rl(a, r, 0)
    def ruler_cap(a, r):
        q = rl(a, r, 0)
        if q: q.lines = ["How long?", f"{BOX} cm"]; q.sol = ["How long?", f"⟦{a}⟧ cm"]; q.form += ", caption"
        return q
    def sum_(a, r):
        x = r.randint(1, a - 1); return EQ([f"{x} cm + {a - x} cm = {BOX} cm"], a, form="add cm")
    def longer(a, r):
        x = r.randint(1, a - 1)
        return SEM([f"Pencil: {x} cm", f"Pen is {a - x} cm longer.", f"Pen: {BOX} cm"], lambda v, t=a: v == t, str(a), form="longer than")
    def shorter(a, r):
        s = r.randint(2, 5)
        return SEM([f"Line A: {a + s} cm", f"B is {s} cm shorter.", f"Line B: {BOX} cm"], lambda v, t=a: v == t, str(a), form="shorter than")
    def cut(a, r):
        s = r.randint(2, 5)
        return SEM([f"A ribbon is {a + s} cm.", f"{s} cm is cut off.", f"Left: {BOX} cm"], lambda v, t=a: v == t, str(a), form="cut off")
    def sum_c(a, r):
        x = r.randint(1, a - 1); return EQ([f"{x} + {a - x} = {BOX} cm"], a, form="add, compact")
    def sub_c(a, r):
        s = r.randint(2, 6); return EQ([f"{a + s} {MINUS} {s} = {BOX} cm"], a, form="subtract, compact")
    return [ruler0, ruler_cap, sum_, longer, shorter, cut, sum_c, sub_c]

# ------------------------------------------------------------------ shapes: corners and straight sides (triangle, square, rectangle, circle)
def _combos(k_range, total):
    out = []
    def rec(cur, left):
        if left == 0 and len(cur) in k_range: out.append(list(cur)); return
        if len(cur) >= max(k_range): return
        for n, v in A.SHAPES.items():
            if v <= left: rec(cur + [n], left - v)
    rec([], total)
    return [c for c in out if sorted(c) != ["circle"]]
def _shapes(tier):
    ks = range(1, 4)
    mult = 1 if tier == 1 else 2          # two stars: corners and sides together, so the answer is twice the corner count
    def mk(words, layout):
        def f(a, r):
            if a % mult: return None
            cs = _combos(ks, a // mult)
            if not cs: return None
            small = [x for x in cs if len(x) <= 2]
            c = r.choice(small if small and r.random() < 0.8 else cs); c = list(c); r.shuffle(c)
            lines, sol = words(a)
            q = SEM(lines, lambda v, t=a: v == t, str(a), art=A.shapes(c), layout=layout, form=words.__name__)
            q.sol = sol
            return q
        return f
    def corners2(a): return ["How many corners", f"in all? {BOX}"], ["How many corners", f"in all? \u27e6{a}\u27e7"]
    def sides2(a): return ["How many straight", f"sides in all? {BOX}"], ["How many straight", f"sides in all? \u27e6{a}\u27e7"]
    def corners1(a): return [f"Corners: {BOX}"], [f"Corners: \u27e6{a}\u27e7"]
    def sides1(a): return [f"Straight sides: {BOX}"], [f"Straight sides: \u27e6{a}\u27e7"]
    def cornersq(a): return ["Corners?"], [f"Corners: \u27e6{a}\u27e7"]
    def sidesq(a): return ["Straight sides?"], [f"Straight sides: \u27e6{a}\u27e7"]
    def corners_short(a): return ["Corners:", f"{BOX}"], ["Corners:", f"\u27e6{a}\u27e7"]
    def sides_short(a): return ["Straight sides:", f"{BOX}"], ["Straight sides:", f"\u27e6{a}\u27e7"]
    def both2(a): return ["Corners and sides", f"in all? {BOX}"], ["Corners and sides", f"in all? \u27e6{a}\u27e7"]
    def both1(a): return [f"Corners + sides: {BOX}"], [f"Corners + sides: \u27e6{a}\u27e7"]
    def bothq(a): return ["Corners + sides?"], [f"Corners + sides: \u27e6{a}\u27e7"]
    def both_short(a): return ["Corners and sides:", f"{BOX}"], ["Corners and sides:", f"\u27e6{a}\u27e7"]
    def blank(a): return [f"{BOX}"], [f"\u27e6{a}\u27e7"]
    plan = ((corners2, "stack"), (corners1, "stack"), (corners1, "row"), (cornersq, "stack"), (corners_short, "row"), (blank, "row"), (blank, "stack")) if tier == 1 else \
           ((both2, "stack"), (both1, "stack"), (both1, "row"), (bothq, "stack"), (both_short, "row"), (blank, "row"), (blank, "stack"))
    forms = []
    for words, layout in plan:
        f = mk(words, layout); f.__name__ = f"{words.__name__}_{layout}"; forms.append(f)
    return forms

# ------------------------------------------------------------------ multiplication within 40 (equal groups, repeated addition, tables of 2, 3, 4, 5, 10)
def _ch(r, seq): return r.choice(list(seq))
def _pairs(n): return [(x, n // x) for x in (2, 3, 4, 5, 10) if n % x == 0 and 1 <= n // x <= 10]
def _mult1(tier):
    def pr(a, r):
        p = _pairs(a); return r.choice(p) if p else None
    def times(a, r):
        p = pr(a, r)
        if not p: return None
        x, y = p if r.random() < 0.5 else p[::-1]
        return EQ([f"{x} {TIMES} {y} = {BOX}"], a, form="times")
    def grp(a, r):
        p = pr(a, r)
        if not p: return None
        return SEM([f"{p[0]} groups of {p[1]}", f"is {BOX}"], lambda v, t_=a: v == t_, str(a), form="groups of")
    def rep(a, r):
        p = [q for q in _pairs(a) if q[0] <= 5] or None
        if not p: return None
        x, y = r.choice(p)
        q = SEM([" + ".join([str(y)] * x), f"= {BOX}"], lambda v, t_=a: v == t_, str(a), form="repeated addition")
        q.extra = lambda ans, x=x, y=y: x * y == ans
        return q
    def bags(a, r):
        p = pr(a, r)
        if not p: return None
        return SEM([f"{p[0]} bags, {p[1]} in each.", f"Altogether {BOX}"], lambda v, t_=a: v == t_, str(a), form="bags")
    def arr(a, r):
        c = [(x, y) for x, y in _pairs(a) if x <= 5 and y <= 10] + [(y, x) for x, y in _pairs(a) if y <= 5 and x <= 10]
        if not c: return None
        rows, cols = r.choice(c)
        q = SEM(["How many dots?", f"{BOX}"], lambda v, t_=a: v == t_, str(a), art=A.array(rows, cols), form="array")
        q.extra = lambda ans, rows=rows, cols=cols: rows * cols == ans
        return q
    def grpart(a, r):
        c = [(x, y) for x, y in _pairs(a) if x <= 5 and y <= 10]
        if not c: return None
        n, per = r.choice(c); art = A.groups(n, per)
        q = SEM(["How many dots", f"in all? {BOX}"], lambda v, t_=a: v == t_, str(a), art=art, form="equal groups")
        q.extra = lambda ans, n=n, per=per: n * per == ans
        return q
    def grp_short(a, r):
        q = grpart(a, r)
        if q: q.layout = "row"; q.lines = [f"{BOX}"]; q.sol = [f"\u27e6{a}\u27e7"]; q.form = "equal groups, answer only"
        return q
    return [times, grp, rep, bags, arr, grpart, grp_short]

# ------------------------------------------------------------------ sharing and grouping within 20 (no division sign at Primary 1)
def _share1(tier):
    ds = (2, 3, 4, 5)
    def mk(a, r, f_):
        d = _ch(r, ds); n = a * d
        return f_(a, d, n, r) if n <= 20 else None
    def share(a, r): return mk(a, r, lambda q, d, n, r: SEM([f"Share {n} sweets equally", f"among {d} children. Each: {BOX}"], lambda v, t_=q: v == t_, str(q), form="share"))
    def group(a, r): return mk(a, r, lambda q, d, n, r: SEM([f"{n} pencils, {d} in a box.", f"Boxes: {BOX}"], lambda v, t_=q: v == t_, str(q), form="group"))
    def into(a, r): return mk(a, r, lambda q, d, n, r: SEM([f"Divide {n} apples into", f"{d} equal groups: {BOX}"], lambda v, t_=q: v == t_, str(q), form="divide into"))
    def sharer(a, r):
        d = _ch(r, (3, 4, 5)); n = a * d
        return SEM([f"Mia shares {n} stickers", f"with her {d - 1} friends.", f"Each person: {BOX}"], lambda v, t_=a: v == t_, str(a), form="sharer counted") if n <= 20 else None
    def most(a, r): return mk(a, r, lambda q, d, n, r: SEM([f"{n} cookies, {d} each.", f"Most friends: {BOX}"], lambda v, t_=q: v == t_, str(q), form="most friends"))
    def gart(a, r):
        d = _ch(r, (2, 3, 4, 5)); n = a * d
        if n > 20: return None
        art = A.groups(d, a)
        q = SEM(["How many dots", f"in each box? {BOX}"], lambda v, t_=a: v == t_, str(a), art=art, form="dots in each box")
        q.extra = lambda ans, art=art: art.meta["per"] == ans
        return q
    def share_s(a, r): return mk(a, r, lambda q, d, n, r: SEM([f"Share {n} by {d}.", f"Each: {BOX}"], lambda v, t_=q: v == t_, str(q), form="share, short"))
    def into_s(a, r): return mk(a, r, lambda q, d, n, r: SEM([f"{n} in {d} equal", f"groups. Each: {BOX}"], lambda v, t_=q: v == t_, str(q), form="equal groups, short"))
    def group_s(a, r): return mk(a, r, lambda q, d, n, r: SEM([f"{n} pens, {d} in", f"a box. Boxes: {BOX}"], lambda v, t_=q: v == t_, str(q), form="boxes, short"))
    return [share, group, into, sharer, most, gart, share_s, into_s, group_s]

# ------------------------------------------------------------------ picture graphs (one face is one child, pet or thing), read and compare
P1_GRAPH_SETS = [["Cats", "Dogs", "Fish", "Hens"], ["Pies", "Buns", "Cakes", "Tarts"], ["Cars", "Dolls", "Balls", "Kites"], ["Pens", "Cups", "Hats", "Bags"]]
def _pgraph(tier):
    PG = dict(pitch=3.6, font=3.5)
    def pick(r, n):
        labs = list(_ch(r, P1_GRAPH_SETS)); r.shuffle(labs); return labs[:n]
    def G(rows): return A.picgraph(rows, 1, **PG)
    def read(a, r, n=3):
        labs = pick(r, n); i = r.randrange(n)
        rows = [(l, a if j == i else r.randint(1, 7)) for j, l in enumerate(labs)]
        q = SEM([f"How many {labs[i].lower()}?", f"{BOX}"], lambda v, t_=a: v == t_, str(a), art=G(rows), form="read one row")
        q.extra = lambda ans, rows=rows, i=i: rows[i][1] == ans; return q
    def read2(a, r):
        if a > 6: return None
        labs = pick(r, 2); i = r.randrange(2)
        rows = [(l, a if j == i else r.randint(1, 6)) for j, l in enumerate(labs)]
        q = SEM([f"How many {labs[i].lower()}?", f"{BOX}"], lambda v, t_=a: v == t_, str(a), art=G(rows), form="read one row of two")
        q.extra = lambda ans, rows=rows, i=i: rows[i][1] == ans; return q
    def more(a, r):
        if a > 5: return None
        labs = pick(r, 3); cb = r.randint(1, 7 - a); ca = cb + a; i, j = r.sample(range(3), 2)
        rows = [(l, r.randint(1, 7)) for l in labs]; rows[i] = (labs[i], ca); rows[j] = (labs[j], cb)
        q = SEM([f"How many more {labs[i].lower()}", f"than {labs[j].lower()}? {BOX}"], lambda v, t_=a: v == t_, str(a), art=G(rows), form="how many more")
        q.extra = lambda ans, rows=rows, i=i, j=j: rows[i][1] - rows[j][1] == ans; return q
    def two(a, r):
        if a < 2 or a > 12: return None
        labs = pick(r, 3); c1 = r.randint(max(1, a - 7), min(7, a - 1)); c2 = a - c1
        if not (1 <= c2 <= 7): return None
        i, j = r.sample(range(3), 2)
        rows = [(l, r.randint(1, 7)) for l in labs]; rows[i] = (labs[i], c1); rows[j] = (labs[j], c2)
        q = SEM([f"How many {labs[i].lower()}", f"and {labs[j].lower()}? {BOX}"], lambda v, t_=a: v == t_, str(a), art=G(rows), form="two rows")
        q.extra = lambda ans, rows=rows, i=i, j=j: rows[i][1] + rows[j][1] == ans; return q
    def row1(a, r):
        if a > 6: return None
        lab = _ch(r, [x for g in P1_GRAPH_SETS for x in g]); art = G([(lab, a)])
        q = SEM([f"{BOX}"], lambda v, t_=a: v == t_, str(a), art=art, form="one row, answer below")
        q.sol = [f"\u27e6{a}\u27e7"]
        q.extra = lambda ans, art=art: art.meta["rows"][0][1] == ans; return q
    def row1b(a, r):
        q = row1(a, r)
        if q: q.layout = "row"; q.form = "one row, answer beside"
        return q
    for f_ in (read, read2, more, two): f_.pref = 1
    return [read, read2, more, two, row1, row1b]

# ------------------------------------------------------------------ ordinals: first to tenth (1st, 2nd, 3rd, 4th ...)
def ordw(n): return f"{n}" + ("th" if 10 <= n % 100 <= 20 else {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th"))
def _ord(tier):
    def row_l(a, r):
        if a > 8: return None
        n = r.randint(a, 8); q = SEM(["From left:", f"{BOX}th"], lambda v, t_=a: v == t_, str(a), art=A.queue(n, a), form="from the left")
        q.extra = lambda ans, a=a: a == ans; return q
    def row_r(a, r):
        if a > 8: return None
        n = r.randint(a, 8); k = n + 1 - a
        q = SEM(["From right:", f"{BOX}th"], lambda v, t_=a: v == t_, str(a), art=A.queue(n, k), form="from the right")
        q.extra = lambda ans, n=n, k=k: n + 1 - k == ans; return q
    def before(a, r): return SEM([f"{a - 1} children are in", f"front of Mia. Mia is {BOX}th."], lambda v, t_=a: v == t_, str(a), form="children in front")
    def after(a, r):
        s_ = r.randint(1, a - 1); d = a - s_
        return SEM([f"Ann is {ordw(s_)}. Bo is {d}", f"places after Ann. Bo is {BOX}th."], lambda v, t_=a: v == t_, str(a), form="places after")
    def beforek(a, r):
        d = r.randint(1, 4); t = a + d
        return SEM([f"Sam is {ordw(t)}. Jo is {d}", f"places before Sam. Jo is {BOX}th."], lambda v, t_=a: v == t_, str(a), form="places before") if t <= 10 else None
    def seq(a, r): return SEM([f"{ordw(a - 2)}, {ordw(a - 1)},", f"{BOX}th"], lambda v, t_=a: v == t_, str(a), form="ordinal sequence")
    def seq_down(a, r): return SEM([f"{ordw(a + 2)}, {ordw(a + 1)},", f"{BOX}th"], lambda v, t_=a: v == t_, str(a), form="ordinal sequence down") if a + 2 <= 10 else None
    def gap(a, r): return SEM([f"{ordw(a - 1)}, {BOX}th,", f"{ordw(a + 1)}"], lambda v, t_=a: v == t_, str(a), form="ordinal gap") if a + 1 <= 10 else None
    def between(a, r): return SEM([f"Between {ordw(a - 1)} and {ordw(a + 1)}", f"is {BOX}th"], lambda v, t_=a: v == t_, str(a), form="between") if a + 1 <= 10 else None
    def next_(a, r): return SEM([f"Just after {ordw(a - 1)}:", f"{BOX}th"], lambda v, t_=a: v == t_, str(a), form="just after")
    def prev_(a, r): return SEM([f"Just before {ordw(a + 1)}:", f"{BOX}th"], lambda v, t_=a: v == t_, str(a), form="just before") if a + 1 <= 10 else None
    return [row_l, row_r, before, after, beforek, seq, seq_down, gap, between, next_, prev_]

def build_banks():
    B = {}
    B["add"] = Bank("add", "Addition", "Addition within 20", "Add. Find the answer in the key. Colour the part with that colour.",
        {1: T([8, 9, 10, 11, 12], range(0, 21), _add1(0, 0)), 2: T([13, 14, 15, 16, 17], range(0, 21), _add2(0, 0))})
    B["sub"] = Bank("sub", "Subtraction", "Subtraction within 20", "Take away. Find the answer in the key. Colour the part with that colour.",
        {1: T([2, 3, 4, 5, 6], range(0, 21), _sub1()), 2: T([7, 8, 9, 10, 11], range(0, 21), _sub2())})
    B["bonds"] = Bank("bonds", "Number Bonds", "Number bonds to 10 and 20", "Find the missing number. Find it in the key. Colour the part with that colour.",
        {1: T([1, 2, 3, 4, 5], range(0, 11), _bond(10)), 2: T([5, 6, 7, 8, 9], range(0, 21), _bond(20))}, {1: "Number bonds to 10", 2: "Number bonds to 20"})
    B["place"] = Bank("place", "Tens and Ones", "Place value: tens and ones", "Find the missing number. Find it in the key. Colour the part with that colour.",
        {1: T([1, 2, 3, 4, 5], range(0, 11), _pv(1)), 2: T([5, 6, 7, 8, 9], range(0, 11), _pv(2))})
    B["count"] = Bank("count", "Counting Patterns", "Counting in 2s, 5s and 10s", "Find the missing number in each pattern. Find it in the key. Colour the part with that colour.",
        {1: T([10, 15, 20, 25, 30], range(0, 101), _count(1)), 2: T([60, 65, 70, 75, 80], range(0, 101), _count(2))})
    B["compare"] = Bank("compare", "Compare Numbers", "Comparing and ordering numbers to 100", "Find the number. Find it in the key. Colour the part with that colour.",
        {1: T([20, 30, 40, 50, 60], range(0, 101), _cmp(1)), 2: T([55, 60, 65, 70, 75], range(0, 101), _cmp(2))})
    B["money"] = Bank("money", "Money", "Money: coins and cents", "Find how much. Find it in the key. Colour the part with that colour.",
        {1: T([10, 20, 30, 40, 50], range(0, 101, 5), _money1(), lambda v: f"{v}¢"),
         2: T([12, 14, 16, 18, 20], range(0, 31), _money2(), lambda v: f"${v}", kind="dollars")}, {1: "Money: coins and cents", 2: "Money: notes and dollars"})
    times = lambda: [(h, m) for h in range(1, 13) for m in (0, 30)]
    B["time"] = Bank("time", "Time", "Time: o'clock and half past", "Find the time. Find it in the key. Colour the part with that colour.",
        {1: T([(2, 0), (4, 0), (6, 0), (3, 30), (7, 30)], times(), _time(1), tword),
         2: T([(8, 30), (9, 0), (10, 30), (11, 0), (12, 30)], times(), _time(2), tword)})
    B["length"] = Bank("length", "Length in cm", "Length in centimetres", "Find the length. Find it in the key. Colour the part with that colour.",
        {1: T([2, 3, 4, 5, 6], range(0, 21), _len(1), lambda v: f"{v} cm"), 2: T([7, 8, 9, 10, 11], range(0, 21), _len(2), lambda v: f"{v} cm")})
    B["shapes"] = Bank("shapes", "Shapes", "Shapes: corners", "Count the corners.",
        {1: T([3, 4, 6, 7, 8], range(0, 13), _shapes(1), instr="Count the corners of the shapes in each part. Find the answer in the key. Colour the part with that colour."),
         2: T([6, 8, 12, 14, 16], range(0, 21), _shapes(2), instr="Count the corners and the straight sides of the shapes in each part. Add them. Find the answer in the key. Colour the part with that colour.")}, {1: "Shapes: corners", 2: "Shapes: corners and straight sides"})
    B["mult"] = Bank("mult", "Multiplication", "Multiplication within 40", "Multiply. Find the answer in the key. Colour the part with that colour.",
        {1: T([4, 6, 8, 10, 12], range(0, 41), _mult1(1)), 2: T([12, 15, 20, 30, 40], range(0, 41), _mult1(2))}, {1: "Multiplication within 40: equal groups", 2: "Multiplication within 40"})
    B["share"] = Bank("share", "Sharing", "Sharing and grouping within 20", "Share or group equally. Find the answer in the key. Colour the part with that colour.",
        {1: T([2, 3, 4, 5, 6], range(0, 21), _share1(1)), 2: T([4, 5, 6, 7, 8], range(0, 21), _share1(2))})
    B["pgraph"] = Bank("pgraph", "Picture Graphs", "Picture graphs", "Read the picture graph. Find the answer in the key. Colour the part with that colour.",
        {1: T([1, 2, 3, 4, 5], range(0, 21), _pgraph(1)), 2: T([4, 5, 6, 7, 8], range(0, 21), _pgraph(2))})
    B["ordinal"] = Bank("ordinal", "Ordinal Numbers", "Ordinal numbers: first to tenth", "Write the missing number. Find it in the key. Colour the part with that colour.",
        {1: T([4, 5, 6, 7, 8], range(0, 11), _ord(1), lambda v: ordw(v)), 2: T([6, 7, 8, 9, 10], range(0, 11), _ord(2), lambda v: ordw(v))})
    return B

BANKS = build_banks()

GALLERY = [
    dict(id="CBC-01", picture="rocket",    bank="bonds",   tier=1, seed=101),
    dict(id="CBC-02", picture="fish",      bank="add",     tier=2, seed=102),
    dict(id="CBC-03", picture="butterfly", bank="sub",     tier=2, seed=103),
    dict(id="CBC-04", picture="house",     bank="place",   tier=1, seed=104),
    dict(id="CBC-05", picture="icecream",  bank="count",   tier=2, seed=105),
    dict(id="CBC-06", picture="owl",       bank="compare", tier=2, seed=106),
    dict(id="CBC-07", picture="sailboat",  bank="money",   tier=1, seed=107),
    dict(id="CBC-08", picture="butterfly", bank="time",    tier=1, seed=10),
    dict(id="CBC-09", picture="icecream",  bank="length",  tier=1, seed=109),
    dict(id="CBC-10", picture="house",     bank="shapes",  tier=1, seed=114),
    dict(id="CBC-11", picture="car",       bank="mult",    tier=2, seed=1),
    dict(id="CBC-12", picture="castle",    bank="share",   tier=1, seed=1),
    dict(id="CBC-13", picture="icecream",  bank="pgraph",  tier=1, seed=20),
    dict(id="CBC-14", picture="sailboat",  bank="ordinal", tier=1, seed=1),
]
