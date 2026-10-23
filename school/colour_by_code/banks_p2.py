"""Primary 2 topic banks (level file: LEVEL, RULES, BANKS, GALLERY). Wording follows docs/books/p2_school_paper_patterns.md:
"more than", "fewer than", "share equally", "n groups of m", money as $3.05 and 55¢, times as 3:25, 1/2 written with a slash.
Every form is form(answer, rng) -> Q or None; None means the answer cannot be made in this form."""
import math, re
import art as A
from qcore import *

LEVEL = 2
RULES = dict(allow_division_sign=True, time_words_only=False)
X, D = TIMES, DIVIDE
def sol_(lines, a, at): return [mark(l, at) for l in lines]
def ch(r, seq): return r.choice(list(seq))

# ------------------------------------------------------------------ numbers to 1000
ONES = "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split()
TENS = "x x twenty thirty forty fifty sixty seventy eighty ninety".split()
def below100(n): return ONES[n] if n < 20 else TENS[n // 10] + ("-" + ONES[n % 10] if n % 10 else "")
def words_lines(n):
    h, rest = divmod(n, 100)
    first = f"{ONES[h]} hundred"
    return [first] if rest == 0 else [first, "and " + below100(rest)]

def _numbers(tier):
    one = tier == 1
    def digs(n): return n // 100, n // 10 % 10, n % 10
    def expanded(a, r):
        h, t, o = digs(a)
        l2 = f"{t} tens" if o == 0 else f"{t} tens {o} ones"
        if o == 0 and t == 0: return None
        return SEM([f"{h} hundreds {l2}", f"= {BOX}"], lambda v, t_=a: v == t_, str(a), form="expanded")
    def plus(step, word, sign):
        def f(a, r):
            m = a - sign * step
            if m < 0 or m > 1000: return None
            return SEM([f"{step} {word} than {m}", f"is {BOX}"], lambda v, t_=a: v == t_, str(a), form=f"{step} {word}")
        f.__name__ = f"p{step}{word}"; return f
    def wrds(a, r):
        ls = words_lines(a); ls[-1] = ls[-1] + f" = {BOX}"
        return SEM(ls, lambda v, t_=a: v == t_, str(a), form="words to number")
    KEY = (120, 250, 340, 470, 560) if one else (105, 218, 346, 407, 639)       # the colour key of this tier
    def extreme(kind):
        def f(a, r):
            # every number offered is a key value, so the key alone does not answer the question
            pool = [k for k in KEY if (k < a if kind == "greatest" else k > a)]
            if len(pool) < 2: return None
            ns = r.sample(pool, 2) + [a]; r.shuffle(ns)
            p = max if kind == "greatest" else min
            return SEM([kind.capitalize() + ":", "  ".join(map(str, ns))], lambda v, ns=tuple(ns), p=p: v == p(ns), str(a), form=kind)
        f.__name__ = kind; return f
    def between(a, r): return SEM([f"Between {a - 1} and {a + 1}", f"is {BOX}"], lambda v, t_=a: v == t_, str(a), form="between")
    def count_on(a, r):
        s = ch(r, [10, 100] if a >= 300 else [10])
        terms = [a - s * k for k in (3, 2, 1)]
        if min(terms) < 0: return None
        return SEM([f"Count on in {s}s:", ", ".join(map(str, terms)) + f", {BOX}"], lambda v, t_=a: v == t_, str(a), form="count on")
    def blocks(a, r):
        h, t, o = digs(a)
        art = A.blocks(h, t, o)
        if art.w > 54 or (h + t + o) == 0: return None
        q = SEM(["What number?"], lambda v, t_=a: v == t_, str(a), art=art, form="base-ten blocks")
        q.lines = ["What number?", f"{BOX}"]; q.sol = ["What number?", f"⟦{a}⟧"]
        q.extra = lambda ans, h=h, t=t, o=o: 100 * h + 10 * t + o == ans
        return q
    def blocks_row(a, r):
        q = blocks(a, r)
        if q: q.layout = "row"; q.lines = [f"{BOX}"]; q.sol = [f"⟦{a}⟧"]; q.form = "base-ten blocks, answer only"
        return q
    forms = [expanded, plus(10, "more", 1), plus(10, "less", -1), plus(100, "more", 1), plus(100, "less", -1), wrds, extreme("greatest"), extreme("smallest"), between, count_on, blocks]
    if not one:
        def regroup(a, r):
            h, t, o = digs(a)
            if h < 2: return None
            return SEM([f"{h - 1} hundreds {t + 10} tens", f"{o} ones = {BOX}"], lambda v, t_=a: v == t_, str(a), form="regrouped")
        def middle(a, r):
            lo, hi = [k for k in KEY if k < a], [k for k in KEY if k > a]
            if not lo or not hi: return None
            ns = [r.choice(lo), a, r.choice(hi)]
            r.shuffle(ns)
            return SEM(["Middle number:", "  ".join(map(str, ns))], lambda v, ns=tuple(ns): v == sorted(ns)[1], str(a), form="middle")
        forms += [regroup, middle, plus(1, "more", 1), plus(1, "less", -1), blocks_row]
    else: forms += [plus(1, "more", 1)]
    return forms

# ------------------------------------------------------------------ number patterns
def _pattern(tier):
    steps = [2, 5, 10, 100] if tier == 1 else [3, 4, 5, 10, 100]
    def ap_holds(terms, blank):
        def holds(v):
            t = list(terms); t[blank] = v
            d = {t[i + 1] - t[i] for i in range(len(t) - 1)}
            return len(d) == 1 and 0 not in d and min(t) >= 0 and max(t) <= 1000
        return holds
    def mk(a, r, rule, back, pos):
        s = ch(r, steps); sg = -s if back else s
        terms = [a - sg * pos + sg * i for i in range(5)]
        if min(terms) < 0 or max(terms) > 1000: return None
        lines = []
        if rule: lines.append(("Count back in " if back else "Count in ") + f"{s}s:")
        lines.append(", ".join(BOX if i == pos else str(t) for i, t in enumerate(terms)))
        q = Q(lines, ap_holds(terms, pos), form=("back " if back else "") + f"{s}s")
        q.sol = [mark(l, str(a)) for l in lines]; q.a_text = str(a)
        q.extra = lambda ans, terms=terms, pos=pos: terms[pos] == ans
        return q
    def f_rule(a, r): return mk(a, r, True, False, ch(r, [2, 3]))
    def f_plain(a, r): return mk(a, r, False, False, ch(r, [1, 3, 4]))
    def f_back(a, r): return mk(a, r, True, True, ch(r, [2, 3]))
    def f_back2(a, r): return mk(a, r, False, True, ch(r, [0, 2, 4]))
    def start(a, r):
        s = ch(r, [5, 10, 100] if tier == 1 else [3, 4, 5, 10]); st = a - 4 * s
        if st < 0: return None
        return SEM([f"Start at {st}.", f"Count on 4 times in {s}s:", f"{BOX}"], lambda v, t_=a: v == t_, str(a), form="start and count on")
    def odd_one(a, r):
        s = ch(r, steps); k = r.randint(1, 3)
        x0 = r.randint(1, 4) * s
        terms = [x0 + s * i for i in range(5)]
        terms[k] = a
        if a % s == x0 % s or len(set(terms)) < 5 or max(terms) > 1000 or terms != sorted(terms): return None
        q = SEM(["Which does not belong?", ", ".join(map(str, terms))], lambda v, t_=a: v == t_, str(a), form="does not belong")
        q.sol = [q.lines[0], ", ".join(f"⟦{t}⟧" if t == a else str(t) for t in terms)]
        q.extra = lambda ans, terms=terms, s=s: sum(1 for t in terms if t % s != terms[0] % s or False) in (1, 4) and ans in terms
        return q
    def compact(a, r, n=3):
        s = ch(r, steps); back = r.random() < 0.4; sg = -s if back else s
        pos = r.randrange(n); terms = [a - sg * pos + sg * i for i in range(n)]
        if min(terms) < 0 or max(terms) > 1000: return None
        line = ", ".join(BOX if i == pos else str(t) for i, t in enumerate(terms))
        q = Q([line], ap_holds(terms, pos), form=f"compact {n}-term")
        q.sol = [mark(line, str(a))]; q.a_text = str(a); q.extra = lambda ans, terms=terms, pos=pos: terms[pos] == ans
        return q
    def compact4(a, r): return compact(a, r, 4)
    def compact_rule(a, r):
        s = ch(r, steps); pos = r.randrange(3); terms = [a - s * pos + s * i for i in range(3)]
        if min(terms) < 0 or max(terms) > 1000: return None
        lines = [f"+{s}:", ", ".join(BOX if i == pos else str(t) for i, t in enumerate(terms))]
        q = Q(lines, ap_holds(terms, pos), form="compact with rule")
        q.sol = [lines[0], mark(lines[1], str(a))]; q.a_text = str(a); q.extra = lambda ans, terms=terms, pos=pos: terms[pos] == ans
        return q
    forms = [f_rule, f_plain, f_back, f_back2, start, compact, compact4, compact_rule]
    if tier == 2: forms.append(odd_one)
    return forms

# ------------------------------------------------------------------ odd and even
def _oddeven(tier):
    lo = 0 if tier == 1 else 100
    def kind(a): return "odd" if a % 2 else "even"
    def nxt(a, r): return SEM([f"The {kind(a)} number", f"just after {a - 1} is {BOX}"], lambda v, t_=a: v == t_, str(a), form="just after")
    def prv(a, r): return SEM([f"The {kind(a)} number", f"just before {a + 1} is {BOX}"], lambda v, t_=a: v == t_, str(a), form="just before")
    def small(a, r): return SEM([f"Smallest {kind(a)} number", f"greater than {a - 2}: {BOX}"], lambda v, t_=a: v == t_, str(a), form="smallest greater")
    def great(a, r): return SEM([f"Greatest {kind(a)} number", f"less than {a + 2}: {BOX}"], lambda v, t_=a: v == t_, str(a), form="greatest less")
    KEY = (9, 12, 15, 18, 21) if tier == 1 else (200, 301, 402, 503, 604)
    def which(a, r):
        # two key values of the other kind and the answer: all three are on the key, so only the odd or even test picks one
        o = [k for k in KEY if k % 2 != a % 2]
        if len(o) < 2: return None
        ns = r.sample(o, 2) + [a]; r.shuffle(ns)
        return SEM([f"Which is {kind(a)}?", "  ".join(map(str, ns))], lambda v, ns=tuple(ns), p=a % 2: v in ns and v % 2 == p, str(a), form="which is")
    def between(a, r): return SEM([f"The {kind(a)} number between", f"{a - 1} and {a + 1}: {BOX}"], lambda v, t_=a: v == t_, str(a), form="between")
    def seq(a, r):
        if a - 6 < 0: return None
        return SEM([f"{kind(a).capitalize()} numbers:", f"{a - 6}, {a - 4}, {a - 2}, {BOX}"], lambda v, t_=a: v == t_, str(a), form="odd/even pattern")
    def nxt1(a, r): return SEM([f"Next {kind(a)} after {a - 1}: {BOX}"], lambda v, t_=a: v == t_, str(a), form="after, one line")
    def prv1(a, r): return SEM([f"{kind(a).capitalize()} just before {a + 1}: {BOX}"], lambda v, t_=a: v == t_, str(a), form="before, one line")
    def which1(a, r):
        q = which(a, r)
        if q: q.lines = [q.lines[0].replace("Which is ", "").replace("?", ":")] + q.lines[1:] if False else q.lines
        return q
    def seq1(a, r):
        if a - 4 < 0: return None
        return SEM([f"{a - 4}, {a - 2}, {BOX}"], lambda v, t_=a: v == t_, str(a), form="short pattern")
    return [nxt, prv, small, great, which, between, seq, nxt1, prv1, seq1]

# ------------------------------------------------------------------ addition and subtraction within 1000
def _carry_pair(a, r, lo_b, hi_b):
    """a = x + y with a carry in the ones (or tens) where possible"""
    for _ in range(60):
        y = r.randint(lo_b, min(hi_b, a - 1))
        x = a - y
        if x >= 1 and (x % 10 + y % 10 >= 10 or (x // 10 % 10 + y // 10 % 10 >= 10)): return x, y
    y = r.randint(lo_b, min(hi_b, a - 1)); return a - y, y
def _add(tier):
    lo, hi = (3, 99) if tier == 1 else (101, 600)
    def pair(a, r): return _carry_pair(a, r, lo, hi)
    def sum_(a, r): x, y = pair(a, r); return EQ([f"{x} + {y} = {BOX}"], a, form="sum")
    def rev(a, r): x, y = pair(a, r); return EQ([f"{BOX} = {x} + {y}"], a, form="sum reversed")
    def miss(a, r):
        x, y = pair(a, r); return EQ([f"{y} + {BOX} = {a + y}"], a, form="missing addend") if a + y <= 1000 else None
    def first(a, r): x, y = pair(a, r); return EQ([f"{BOX} + {y} = {a + y}"], a, form="missing first") if a + y <= 1000 else None
    def addto(a, r): x, y = pair(a, r); return SEM([f"Add {y} to {x}.", f"{BOX}"], lambda v, t_=a: v == t_, str(a), form="add to")
    def sumof(a, r): x, y = pair(a, r); return SEM([f"The sum of {x}", f"and {y} is {BOX}"], lambda v, t_=a: v == t_, str(a), form="sum of")
    def more(a, r): x, y = pair(a, r); return SEM([f"{y} more than {x}", f"is {BOX}"], lambda v, t_=a: v == t_, str(a), form="more than")
    def story(a, r):
        x, y = pair(a, r); return SEM([f"Sold {x}, then {y}.", f"Altogether {BOX}"], lambda v, t_=a: v == t_, str(a), form="story total")
    def atfirst(a, r):
        y = r.randint(lo, hi) if tier == 1 else r.randint(101, 400)
        if a - y < 1: return None
        return SEM([f"Sold {y}. Left {a - y}.", f"At first: {BOX}"], lambda v, t_=a: v == t_, str(a), form="at first")
    forms = [sum_, rev, miss, first, addto, sumof, more, story, atfirst]
    if tier == 2:
        def three(a, r):
            z = r.randint(5, 60); x, y = _carry_pair(a - z, r, 101, 500)
            return EQ([f"{x} + {y} + {z} = {BOX}"], a, form="three numbers") if a - z > 150 else None
        forms.append(three)
    return forms
def _sub(tier):
    lo, hi = (3, 99) if tier == 1 else (101, 600)
    def pair(a, r):
        for _ in range(80):
            y = r.randint(lo, hi); x = a + y
            if x <= 1000 and (x % 10 < y % 10 or (tier == 2 and x // 10 % 10 < y // 10 % 10)): return x, y
        y = r.randint(lo, hi); return a + y, y
    def diff(a, r): x, y = pair(a, r); return EQ([f"{x} {MINUS} {y} = {BOX}"], a, form="difference") if x <= 1000 else None
    def missing_sub(a, r):
        x, y = pair(a, r); return EQ([f"{x} {MINUS} {BOX} = {x - a}"], a, form="missing subtrahend") if x - a >= 1 else None
    def missing_min(a, r):
        y = r.randint(lo, hi)
        return EQ([f"{BOX} {MINUS} {y} = {a - y}"], a, form="missing start") if a - y >= 1 else None
    def subfrom(a, r): x, y = pair(a, r); return SEM([f"Subtract {y}", f"from {x}: {BOX}"], lambda v, t_=a: v == t_, str(a), form="subtract from")
    def findiff(a, r): x, y = pair(a, r); return SEM([f"Difference between", f"{x} and {y}: {BOX}"], lambda v, t_=a: v == t_, str(a), form="find the difference")
    def fewer(a, r): x, y = pair(a, r); return SEM([f"{y} fewer than {x}", f"is {BOX}"], lambda v, t_=a: v == t_, str(a), form="fewer than")
    def story(a, r): x, y = pair(a, r); return SEM([f"Had {x}. Gave {y}.", f"Left {BOX}"], lambda v, t_=a: v == t_, str(a), form="story left")
    def reversal(a, r):
        y = r.randint(lo, hi)
        return SEM([f"Ann has {a + y}, {y} more", f"than Jane. Jane: {BOX}"], lambda v, t_=a: v == t_, str(a), form="reversal trap") if a + y <= 1000 else None
    forms = [diff, missing_sub, missing_min, subfrom, findiff, fewer, story, reversal]
    if tier == 2:
        def two(a, r):
            y = r.randint(20, 200); z = r.randint(20, 150)
            return EQ([f"{a + y + z} {MINUS} {y}", f"{MINUS} {z} = {BOX}"], a, form="two steps") if a + y + z <= 1000 else None
        forms.append(two)
    return forms

# ------------------------------------------------------------------ multiplication tables 2, 3, 4, 5, 10
def pairs_for(n):
    """every way to write n as x times y with x and y from 2 to 10 and at least one of them in the tables of 2, 3, 4, 5 and 10; (3, 4) and (4, 3) are two facts"""
    T_ = (2, 3, 4, 5, 10)
    return [(x, n // x) for x in range(2, 11) if n % x == 0 and 2 <= n // x <= 10 and (x in T_ or n // x in T_)]
def _mult(tier):
    def pr(a, r):
        p = pairs_for(a); return r.choice(p) if p else None
    def times(a, r):
        p = pr(a, r)
        if not p: return None
        x, y = p if r.random() < 0.5 else p[::-1]
        q = EQ([f"{x} {X} {y} = {BOX}"], a, form="times"); q.sig = ("mult", x, y); return q
    def grp(a, r):
        p = pr(a, r)
        if not p: return None
        q = SEM([f"{p[0]} groups of {p[1]}", f"is {BOX}"], lambda v, t_=a: v == t_, str(a), form="groups of"); q.sig = ("mult", p[0], p[1]); return q
    def rep(a, r):
        p = [q for q in pairs_for(a) if q[0] <= 5] or None
        if not p: return None
        x, y = r.choice(p)
        q = SEM([" + ".join([str(y)] * x), f"= {BOX}"], lambda v, t_=a: v == t_, str(a), form="repeated addition")
        q.extra = lambda ans, x=x, y=y: x * y == ans
        q.sig = ("mult", x, y)
        return q
    def multiply(a, r):
        p = pr(a, r)
        if not p: return None
        q = SEM([f"Multiply {p[1]} by {p[0]}.", f"{BOX}"], lambda v, t_=a: v == t_, str(a), form="multiply"); q.sig = ("mult", p[1], p[0]); return q
    def arr(a, r):
        c = [(x, y) for x, y in pairs_for(a) if x <= 5 and y <= 10] + [(y, x) for x, y in pairs_for(a) if y <= 5 and x <= 10]
        if not c: return None
        rows, cols = r.choice(c)
        q = SEM(["How many stars?", f"{BOX}"], lambda v, t_=a: v == t_, str(a), art=A.array(rows, cols), form="array")
        q.extra = lambda ans, rows=rows, cols=cols: rows * cols == ans
        q.sig = ("mult", rows, cols)
        return q
    def grpart(a, r):
        c = [(x, y) for x, y in pairs_for(a) if x <= 5 and y <= 10]
        if not c: return None
        n, per = r.choice(c); art = A.groups(n, per)
        q = SEM(["How many stars", f"in all? {BOX}"], lambda v, t_=a: v == t_, str(a), art=art, form="equal groups")
        q.extra = lambda ans, n=n, per=per: n * per == ans
        q.sig = ("mult", n, per)
        return q
    def grp_short(a, r):
        q = grpart(a, r)
        if q: q.layout = "row"; q.lines = [f"{BOX}"]; q.sol = [f"⟦{a}⟧"]; q.form = "equal groups, answer only"
        return q
    def bags(a, r):
        p = pr(a, r)
        if not p: return None
        q = SEM([f"{p[0]} bags, {p[1]} in each.", f"Altogether {BOX}"], lambda v, t_=a: v == t_, str(a), form="bags"); q.sig = ("mult", p[0], p[1]); return q
    forms = [times, grp, rep, multiply, arr, grpart, grp_short, bags]
    if tier == 2:
        def plus(a, r):
            for _ in range(30):
                z = r.randint(1, 9); p = pairs_for(a - z)
                if p: x, y = r.choice(p); q = EQ([f"{x} {X} {y} + {z} = {BOX}"], a, form="times plus"); q.sig = ("multplus", x, y, z); return q
            return None
        def times_as(a, r):
            p = pr(a, r)
            if not p or p[0] == 10: return None
            q = SEM([f"A has {p[1]}. B has {p[0]}", f"times as many. B: {BOX}"], lambda v, t_=a: v == t_, str(a), form="times as many"); q.sig = ("timesas", p[1], p[0]); return q
        forms += [plus, times_as]
    return forms

# ------------------------------------------------------------------ division: sharing and grouping
def _div(tier):
    ds = (2, 3, 4, 5, 10)
    def mk(a, r, f_):
        d = ch(r, ds); n = a * d
        if n > 100: return None
        q = f_(a, d, n, r); q.sig = ("div", n, d); return q
    def div(a, r): return mk(a, r, lambda q, d, n, r: EQ([f"{n} {D} {d} = {BOX}"], q, form="divide"))
    def share(a, r): return mk(a, r, lambda q, d, n, r: SEM([f"Share {n} sweets equally", f"among {d} children. Each: {BOX}"], lambda v, t_=q: v == t_, str(q), form="share"))
    def group(a, r): return mk(a, r, lambda q, d, n, r: SEM([f"{n} pencils, {d} in a box.", f"Boxes: {BOX}"], lambda v, t_=q: v == t_, str(q), form="group"))
    def into(a, r): return mk(a, r, lambda q, d, n, r: SEM([f"Divide {n} apples into", f"{d} equal groups: {BOX}"], lambda v, t_=q: v == t_, str(q), form="divide into"))
    def mfac(a, r): return mk(a, r, lambda q, d, n, r: EQ([f"{BOX} {X} {d} = {n}"], q, form="missing factor"))
    def sharer(a, r):
        d = ch(r, (3, 4, 5)); n = a * d
        q = SEM([f"Mia shares {n} stickers", f"with her {d - 1} friends.", f"Each person: {BOX}"], lambda v, t_=a: v == t_, str(a), form="sharer counted"); q.sig = ("div", n, d); return q if n <= 100 else None
    def related(a, r): return mk(a, r, lambda q, d, n, r: SEM([f"{d} {X} {q} = {n}", f"so {n} {D} {d} = {BOX}"], lambda v, t_=q: v == t_, str(q), form="related facts"))
    def short(a, r): return mk(a, r, lambda q, d, n, r: SEM([f"{n} {D} {d}", f"= {BOX}"], lambda v, t_=q: v == t_, str(q), form="divide, two lines"))
    forms = [div, share, group, into, mfac, sharer, related, short]
    if tier == 2:
        def most(a, r): return mk(a, r, lambda q, d, n, r: SEM([f"{n} cookies, {d} each.", f"Most friends: {BOX}"], lambda v, t_=q: v == t_, str(q), form="most friends"))
        forms.append(most)
    return forms

# ------------------------------------------------------------------ fractions (stacked: numerator over denominator)
def frs(a, b): return f"{a}/{b}"                      # answer text for the teacher page
def _frac(tier):
    def shaded(a, r, shape=None):
        n, b = a
        sh = shape or ("bar" if r.random() < 0.6 else "circle")
        q = SEM(["Shaded:", FBOX], lambda v, t_=a: v == t_, frs(n, b), art=A.fraction(n, b, sh), form=f"shaded {sh}")
        q.extra = lambda ans, n=n, b=b: ans == (q.art.meta["shaded"], q.art.meta["parts"])
        return q
    def shaded_bar(a, r): return shaded(a, r, "bar")
    def shaded_row(a, r):
        q = shaded(a, r, "bar"); q.layout = "row"; q.lines = [FBOX]; q.sol = [AFRAC(*a)]; q.form = "shaded, answer only"; return q
    def unshaded(a, r):
        n, b = a
        art = A.fraction(b - n, b, "bar")
        q = SEM(["Not shaded:", FBOX], lambda v, t_=a: v == t_, frs(n, b), art=art, form="not shaded")
        q.extra = lambda ans, art=art: ans == (art.meta["parts"] - art.meta["shaded"], art.meta["parts"])
        return q
    def parts(a, r):
        n, b = a; return SEM([f"{n} of {b} equal parts", f"is {FBOX}"], lambda v, t_=a: v == t_, frs(n, b), form="words")
    def whole(a, r):
        n, b = a
        return SEM([f"{FRAC(b - n, b)} and {FBOX}", "make 1 whole"], lambda v, t_=a: v == t_, frs(n, b), form="make 1 whole")
    def add(a, r):
        n, b = a
        if n < 2: return None
        k = r.randint(1, n - 1)
        q = SEM([f"{FRAC(k, b)} + {FRAC(n - k, b)}", f"= {FBOX}"], lambda v, t_=a: v == t_, frs(n, b), form="add like fractions")
        q.extra = lambda ans, k=k, n=n, b=b: ans == (k + (n - k), b); return q
    def sub(a, r):
        n, b = a; ks = [k for k in range(1, b - n)]
        if not ks: return None
        k = r.choice(ks)
        q = SEM([f"{FRAC(n + k, b)} {MINUS} {FRAC(k, b)}", f"= {FBOX}"], lambda v, t_=a: v == t_, frs(n, b), form="subtract like fractions")
        q.extra = lambda ans, k=k, n=n, b=b: ans == (n + k - k, b); return q
    def cmp_unit(a, r):
        n, b = a
        if n != 1: return None
        greater = r.random() < 0.5
        o = r.randint(b + 1, min(12, b + 4)) if greater else (r.randint(max(2, b - 3), b - 1) if b > 2 else None)
        if not o: return None
        q = SEM([f"Which is {'greater' if greater else 'smaller'}:", f"{FRAC(1, b)} or {FRAC(1, o)}?"], lambda v, t_=a: v == t_, frs(n, b), form="compare unit fractions")
        q.sol = [q.lines[0], f"{AFRAC(1, b)} or {FRAC(1, o)}?"]
        q.extra = lambda ans, b=b, o=o, g=greater: ans == (1, b) and ((b < o) == g)
        return q
    def cmp_like(a, r):
        n, b = a
        greater = r.random() < 0.5
        o = (r.randint(1, n - 1) if n > 1 else None) if greater else (r.randint(n + 1, b - 1) if n + 1 < b else None)
        if not o: return None
        q = SEM([f"Which is {'greater' if greater else 'smaller'}:", f"{FRAC(n, b)} or {FRAC(o, b)}?"], lambda v, t_=a: v == t_, frs(n, b), form="compare like fractions")
        q.sol = [q.lines[0], f"{AFRAC(n, b)} or {FRAC(o, b)}?"]
        q.extra = lambda ans, n=n, o=o, g=greater: (n > o) == g
        return q
    return [shaded, shaded_bar, shaded_row, unshaded, parts, whole, add, sub, cmp_unit, cmp_like]

# ------------------------------------------------------------------ money (decimal notation); answers are in cents
def fm(c, r=None, cents_ok=True):
    """amount as the papers write it: $3.05, or 55¢ for less than a dollar"""
    if c < 100 and cents_ok and (r is None or r.random() < 0.5): return f"{c}¢"
    return f"${c // 100}.{c % 100:02d}"
def dec(c): return f"{c // 100}.{c % 100:02d}"
def _cash_set(n, r):
    den = [1000, 500, 200, 100, 50, 20, 10, 5]
    for _ in range(300):
        left, out = n, []
        while left > 0 and len(out) < 6:
            c = [d for d in den if d <= left]
            d = r.choice(c[:4] if len(c) > 4 else c); out.append(d); left -= d
        if left == 0 and 2 <= len(out) <= 5 and sum(1 for d in out if d >= 200) <= 3: return out
    return None
def _money(tier):
    cents_key = tier == 2
    def cashq(a, r, short=False):
        s = _cash_set(a, r)
        if not s: return None
        art = A.cash(s)
        if art.w > 54: return None
        unit = "¢" if cents_key else ""
        lines = [f"{BOX}{unit}"] if short else ["How much money?", f"{'' if cents_key else '$'}{BOX}{unit}"]
        q = SEM(lines, lambda v, t_=a: v == t_, str(a) if cents_key else dec(a), art=art, layout="row" if short else "stack", form="cash picture")
        q.extra = lambda ans, s=s: sum(s) == ans
        return q
    def cash_short(a, r): return cashq(a, r, True)
    def at(a): return str(a) if cents_key else dec(a)
    def blank(): return f"{BOX}¢" if cents_key else f"${BOX}"
    # Primary 2 money is dollars and cents, decimal notation, compare, and convert between decimal notation and cents: no sums or differences of
    # decimal amounts (that is Primary 3), so the sums below are whole cents only
    def add(a, r):
        if not cents_key or a <= 10: return None
        x = r.randrange(5, a - 4, 5)
        return EQ([f"{x}¢ + {a - x}¢ = {BOX}¢"], a, at(a), money=True, form="add cents")
    def two(a, r):
        if not cents_key or a <= 10: return None
        x = r.randrange(5, a - 4, 5)
        return SEM([f"Pen {x}¢, ruler {a - x}¢.", f"Both: {BOX}¢"], lambda v, t_=a: v == t_, at(a), form="two items")
    def more(a, r):
        if not cents_key or a <= 10: return None
        x = r.randrange(5, a - 4, 5)
        return SEM([f"Ann has {x}¢.", f"Ben has {a - x}¢ more.", f"Ben has {BOX}¢"], lambda v, t_=a: v == t_, at(a), form="more than")
    def convert(a, r):
        if cents_key:
            q = SEM([f"{fm(a, r, False)} = {BOX}¢"], lambda v, t_=a: v == t_, str(a), form="dollars to cents")
            q.extra = lambda ans, a=a: ans == a; return q
        return SEM([f"{a}¢ = ${BOX}"], lambda v, t_=a: v == t_, dec(a), form="cents to dollars")
    KEY = (35, 65, 135, 185, 250) if cents_key else (120, 235, 305, 450, 680)
    def great(a, r):
        pool = [k for k in KEY if k < a]                 # every amount offered is a key value: the key alone does not answer the question
        if len(pool) < 2: return None
        ns = r.sample(pool, 2) + [a]; r.shuffle(ns)
        return SEM(["Greatest:", "  ".join(fm(n, None, False) for n in ns)], lambda v, ns=tuple(ns): v == max(ns), at(a), form="greatest of three")
    def great_min(a, r):
        pool = [k for k in KEY if k > a]
        if len(pool) < 2: return None
        ns = r.sample(pool, 2) + [a]; r.shuffle(ns)
        return SEM(["Smallest:", "  ".join(fm(n, None, False) for n in ns)], lambda v, ns=tuple(ns): v == min(ns), at(a), form="smallest of three")
    forms = [cashq, cash_short, add, two, more, convert, great, great_min]
    if cents_key:
        def comp(a, r):
            if a >= 100 or a % 5: return None
            return SEM([f"{100 - a}¢ and {BOX}¢", "make $1"], lambda v, t_=a: v == t_, str(a), form="make $1")
        forms.append(comp)
    return forms

# ------------------------------------------------------------------ time: to the minute; durations
def hm(t): return f"{t[0]}:{t[1]:02d}"
def addm(t, d):
    tot = (t[0] % 12) * 60 + t[1] + d; tot %= 720
    h = tot // 60 or 12
    return (h, tot % 60)
def _time(tier):
    if tier == 1:
        def clock_stack(a, r): return None if A.hand_gap(*a) < A.CLOCK_MIN_GAP else SEM(["What time is it?"], lambda v, t_=a: v == t_, hm(a), art=A.clock(*a), form="clock face, stacked")
        def clock_row(a, r): return None if A.hand_gap(*a) < A.CLOCK_MIN_GAP else SEM(["What", "time", "is it?"], lambda v, t_=a: v == t_, hm(a), art=A.clock(*a), layout="row", form="clock face, beside")
        def clock_short(a, r): return None if A.hand_gap(*a) < A.CLOCK_MIN_GAP else SEM([f"{BOX}"], lambda v, t_=a: v == t_, hm(a), art=A.clock(*a), form="clock face, answer only")
        def wrap(f):
            def g(a, r):
                q = f(a, r)
                if q is None: return None
                q.extra = lambda ans: __import__("art").decode_clock(q.art.meta) == ans; return q
            g.__name__ = f.__name__; g.pref = 1; return g          # a clock sheet shows clock faces wherever one fits (one face per time)
        def pastto(a, r):
            h, m = a
            if m == 0: return None
            if m <= 30: k, w, hh = m, "after", h                       # the hour is always written as H:00, so "to" and "past" cannot be mixed up
            else: k, w, hh = 60 - m, "before", h % 12 + 1
            lines = r.choice([[f"{k} minutes {w} {hh}:00", f"is {BOX}"], ["Which time is", f"{k} minutes {w} {hh}:00? {BOX}"]])
            return SEM(lines, lambda v, t_=a: v == t_, hm(a), form="minutes after or before")
        def later(a, r):
            d = ch(r, [5, 10, 15, 20, 25, 30]); s = addm(a, -d)
            return SEM([f"It is {hm(s)}.", f"{d} minutes later: {BOX}"], lambda v, t_=a: v == t_, hm(a), form="minutes later")
        def before(a, r):
            d = ch(r, [5, 10, 15, 20, 25]); s = addm(a, d)
            return SEM([f"It is {hm(s)}.", f"{d} minutes before: {BOX}"], lambda v, t_=a: v == t_, hm(a), form="minutes before")
        def hour(a, r):
            k = ch(r, [1, 2, 3]); s = addm(a, -60 * k)
            return SEM([f"It is {hm(s)}.", f"{k} hour{'s' if k > 1 else ''} later: {BOX}"], lambda v, t_=a: v == t_, hm(a), form="hours later")
        def hmlater(a, r):
            k = ch(r, [1, 2]); d = ch(r, [5, 10, 15, 20, 25, 30, 40, 45]); s = addm(a, -(60 * k + d))
            return SEM([f"It is {hm(s)}.", f"{k} h {d} min later: {BOX}"], lambda v, t_=a: v == t_, hm(a), form="hours and minutes later")
        def clock_alone(a, r):
            if A.hand_gap(*a) < A.CLOCK_MIN_GAP: return None
            q = SEM([], lambda v, t_=a: v == t_, hm(a), art=A.clock(*a), form="clock face alone")
            q.sol = ["\u27e6" + hm(a) + "\u27e7"]
            return q
        def short_add(a, r):
            d = ch(r, [5, 10, 15, 20, 25, 30]); s_ = addm(a, -d)
            return SEM([f"{hm(s_)} + {d} min", f"= {BOX}"], lambda v, t_=a: v == t_, hm(a), form="time plus minutes")
        def short_sub(a, r):
            d = ch(r, [5, 10, 15, 20, 25]); s_ = addm(a, d)
            return SEM([f"{hm(s_)} {MINUS} {d} min", f"= {BOX}"], lambda v, t_=a: v == t_, hm(a), form="time minus minutes")
        return [wrap(clock_stack), wrap(clock_row), wrap(clock_short), wrap(clock_alone), pastto, later, before, hour, hmlater, short_add, short_sub]
    def conv(a, r):
        h, m = divmod(a, 60)
        if h == 0: return None
        return SEM([f"{h} h {m} min", f"= {BOX} min"] if m else [f"{h} h", f"= {BOX} min"], lambda v, t_=a: v == t_, str(a), form="hours to minutes")
    def fromto(a, r):
        s = (r.randint(1, 12), r.choice([0, 5, 10, 15, 20, 30, 40, 45, 50])); e = addm(s, a)
        return SEM([f"{hm(s)} to {hm(e)}", f"= {BOX} min"], lambda v, t_=a: v == t_, str(a), form="from to")
    def film(a, r):
        s = (r.randint(1, 11), ch(r, [0, 10, 15, 30])); e = addm(s, a)
        return SEM([f"A film starts at {hm(s)}", f"and ends at {hm(e)}.", f"It lasts {BOX} min"], lambda v, t_=a: v == t_, str(a), form="film")
    def ampm(a, r):
        s = (r.randint(1, 10), ch(r, [0, 5, 10, 25, 35, 40])); t2 = addm(s, a)
        if t2[0] < s[0]: return None
        return SEM([f"{hm(s)} am to {hm(t2)} am", f"takes {BOX} min"], lambda v, t_=a: v == t_, str(a), form="am to am")
    def hours_mins_in(a, r):
        h, m = divmod(a, 60)
        if h == 0: return None
        return SEM([f"{h} hour{'s' if h > 1 else ''}" + (f" {m} minutes" if m else ""), f"= {BOX} min"], lambda v, t_=a: v == t_, str(a), form="words")
    def ret(a, r):
        s_ = (r.randint(1, 12), ch(r, [0, 10, 15, 30, 45])); e = addm(s_, a)
        return SEM([f"{hm(s_)} to {hm(e)}:", f"{BOX} min"], lambda v, t_=a: v == t_, str(a), form="from to, short")
    def min_short(a, r):
        h, m = divmod(a, 60)
        if h == 0: return None
        return SEM([f"{h} h {m} min = {BOX}" if m else f"{h} h = {BOX}"], lambda v, t_=a: v == t_, str(a), form="to minutes, one line")
    return [conv, fromto, film, ampm, hours_mins_in, ret, min_short]

# ------------------------------------------------------------------ length, mass and volume
def _measure(tier):
    one = tier == 1
    def ruler(a, r):
        n, u = a
        if u != "cm" or not one: return None
        st = r.choice([0, 0, 1, 2]); end = st + n                    # starts at the arrow, at 0 or at a small offset
        
        if end > 14: return None
        q = SEM([f"{BOX} cm"], lambda v, t_=a: v == t_, str(n), art=A.ruler(st, end, top=end + 1), form="ruler")
        q.extra = lambda ans, st=st, end=end: ans == (end - st, "cm"); return q
    def cm_cut(a, r):
        n, u = a
        if u != "cm": return None
        s = r.randint(5, 40 if not one else 9)
        return SEM([f"A ribbon is {n + s} cm.", f"{s} cm is cut off.", f"Left: {BOX} cm"], lambda v, t_=a: v == t_, str(n), form="cut off")
    def cm_add(a, r):
        n, u = a
        if u != "cm" or n < 3: return None
        x = r.randint(1, n - 1)
        return SEM([f"{x} cm + {n - x} cm = {BOX} cm"], lambda v, t_=a: v == t_, str(n), form="add cm")
    def kg_add(a, r):
        n, u = a
        if u != "kg": return None
        x = r.randint(1, n - 1) if n > 1 else None
        return SEM([f"Rice {x} kg, flour {n - x} kg.", f"Together: {BOX} kg"], lambda v, t_=a: v == t_, str(n), form="kg together") if x else None
    def kg_heavier(a, r):
        n, u = a
        if u != "kg": return None
        x = r.randint(2, 9)
        return SEM([f"Melon {n + x} kg.", f"Pumpkin is {x} kg lighter.", f"Pumpkin: {BOX} kg"], lambda v, t_=a: v == t_, str(n), form="lighter than")
    def bal(a, r):
        n, u = a
        if u not in ("kg", "g"): return None
        k = r.choice([2, 3, 4])
        tot = n * k
        if (u == "kg" and tot > 40) or (u == "g" and tot > 1000): return None
        art = A.balance(k, tot, u)
        q = SEM(["Each one:", f"{BOX} {u}"], lambda v, t_=a: v == t_, str(n), art=art, form="balance")
        q.extra = lambda ans, k=k, tot=tot, u=u: ans == (tot // k, u) and tot % k == 0; return q
    def g_add(a, r):
        n, u = a
        if u != "g": return None
        x = r.randrange(50, n, 50) if n > 100 else None
        return SEM([f"{x} g + {n - x} g = {BOX} g"], lambda v, t_=a: v == t_, str(n), form="g add") if x else None
    def l_left(a, r):
        n, u = a
        if u != "l": return None
        s = r.randint(2, 9)
        return SEM([f"A pail holds {n + s} l.", f"{s} l is poured out.", f"Left: {BOX} l"], lambda v, t_=a: v == t_, str(n), form="litres left")
    def l_add(a, r):
        n, u = a
        if u != "l" or n < 2: return None
        x = r.randint(1, n - 1)
        return SEM([f"{x} l + {n - x} l = {BOX} l"], lambda v, t_=a: v == t_, str(n), form="l add")
    def l_share(a, r):
        n, u = a
        if u != "l": return None
        k = ch(r, [2, 3])
        return SEM([f"{n * k} l is shared into", f"{k} equal tanks: {BOX} l"], lambda v, t_=a: v == t_, str(n), form="share litres") if n * k <= 60 else None
    def short(a, r):
        n, u = a
        if n < 2 or u == "m": return None
        x = r.randint(1, n - 1) if u in ("cm", "kg", "l") else r.randrange(50, n, 50) if n > 100 else None
        if x is None: return None
        return SEM([f"{x} {u} + {n - x} {u}", f"= {BOX} {u}"], lambda v, t_=a: v == t_, str(n), form="add, two lines")
    def less(a, r):
        n, u = a
        if u == "m": return None
        s_ = r.randint(2, 9) if u != "g" else r.choice([50, 100])
        return SEM([f"{n + s_} {u} {MINUS} {s_} {u}", f"= {BOX} {u}"], lambda v, t_=a: v == t_, str(n), form="subtract, two lines")
    def one(a, r):
        n, u = a
        if u == "m": return None
        s_ = r.randint(2, 9) if u != "g" else r.choice([50, 100])
        return SEM([f"{n + s_} {MINUS} {s_} = {BOX} {u}"], lambda v, t_=a: v == t_, str(n), form="subtract, one line")
    for f_ in (ruler, cm_cut, kg_heavier, bal, g_add, l_left, l_share): f_.pref = 1      # real units (ruler, balance, word problems) before bare sums with a unit label; no m to cm or kg to g conversions (Primary 3)
    return [ruler, cm_cut, cm_add, kg_add, kg_heavier, bal, g_add, l_left, l_add, l_share, short, less, one]

# ------------------------------------------------------------------ picture graphs and tally
GRAPH_SETS = [["Cats", "Dogs", "Fish", "Hens"], ["Pies", "Buns", "Cakes", "Tarts"], ["Cars", "Dolls", "Balls", "Kites"], ["Pens", "Cups", "Hats", "Bags"]]
def _graph(tier):
    keys = [2, 5] if tier == 1 else [2, 3, 4, 5]
    def pick(r, n):
        labs = list(ch(r, GRAPH_SETS)); r.shuffle(labs); return labs[:n]
    def read(a, r, n=3):
        ks = [k for k in keys if a % k == 0 and 1 <= a // k <= 6]
        if not ks: return None
        k = r.choice(ks); labs = pick(r, n); i = r.randrange(n)
        rows = [(l, a // k if j == i else r.randint(1, 6)) for j, l in enumerate(labs)]
        art = A.picgraph(rows, k)
        q = SEM([f"How many {labs[i].lower()}?", f"{BOX}"], lambda v, t_=a: v == t_, str(a), art=art, form="read one row")
        q.extra = lambda ans, rows=rows, k=k, i=i: rows[i][1] * k == ans; return q
    def read4(a, r): return read(a, r, 4)
    def read2(a, r):          # two rows of at most 3 faces: small enough for the smaller regions
        ks = [k for k in keys if a % k == 0 and 1 <= a // k <= 3]
        if not ks: return None
        k = r.choice(ks); labs = pick(r, 2); i = r.randrange(2)
        rows = [(l, a // k if j == i else r.randint(1, 3)) for j, l in enumerate(labs)]
        q = SEM([f"How many {labs[i].lower()}?", f"{BOX}"], lambda v, t_=a: v == t_, str(a), art=A.picgraph(rows, k), form="read one row of two")
        q.extra = lambda ans, rows=rows, k=k, i=i: rows[i][1] * k == ans; return q
    def more(a, r):
        ks = [k for k in keys if a % k == 0 and 1 <= a // k <= 5]
        if not ks: return None
        k = r.choice(ks); labs = pick(r, 3); d = a // k
        cb = r.randint(1, 6 - d); ca = cb + d; i, j = r.sample(range(3), 2)
        rows = [(l, r.randint(1, 6)) for l in labs]; rows[i] = (labs[i], ca); rows[j] = (labs[j], cb)
        art = A.picgraph(rows, k)
        q = SEM([f"How many more {labs[i].lower()}", f"than {labs[j].lower()}? {BOX}"], lambda v, t_=a: v == t_, str(a), art=art, form="how many more")
        q.extra = lambda ans, rows=rows, k=k, i=i, j=j: (rows[i][1] - rows[j][1]) * k == ans; return q
    def two(a, r):
        ks = [k for k in keys if a % k == 0 and 2 <= a // k <= 10]
        if not ks: return None
        k = r.choice(ks); labs = pick(r, 3); s = a // k
        for _ in range(50):
            c1 = r.randint(1, min(6, s - 1)); c2 = s - c1
            if 1 <= c2 <= 6: break
        else: return None
        i, j = r.sample(range(3), 2)
        rows = [(l, r.randint(1, 6)) for l in labs]; rows[i] = (labs[i], c1); rows[j] = (labs[j], c2)
        q = SEM([f"How many {labs[i].lower()}", f"and {labs[j].lower()}? {BOX}"], lambda v, t_=a: v == t_, str(a), art=A.picgraph(rows, k), form="two rows")
        q.extra = lambda ans, rows=rows, k=k, i=i, j=j: (rows[i][1] + rows[j][1]) * k == ans; return q
    def total(a, r):
        ks = [k for k in keys if a % k == 0 and 3 <= a // k <= 14]
        if not ks: return None
        k = r.choice(ks); labs = pick(r, 3); s = a // k
        for _ in range(50):
            cs = [r.randint(1, min(6, s - 2)) for _ in range(2)]; c3 = s - sum(cs)
            if 1 <= c3 <= 6: break
        else: return None
        rows = list(zip(labs, cs + [c3])); r.shuffle(rows)
        q = SEM(["How many in all?", f"{BOX}"], lambda v, t_=a: v == t_, str(a), art=A.picgraph(rows, k), form="total")
        q.extra = lambda ans, rows=rows, k=k: sum(c for _, c in rows) * k == ans; return q
    def tallyf(a, r):
        if a > 30: return None
        art = A.tally(a)
        q = SEM(["Tally marks:", f"{BOX}"], lambda v, t_=a: v == t_, str(a), art=art, form="tally")
        q.extra = lambda ans, art=art: art.meta["n"] == ans; return q
    def tally1(a, r):
        q = tallyf(a, r)
        if q and q.art.w <= 36: q.layout = "row"; q.lines = [f"{BOX}"]; q.sol = [f"⟦{a}⟧"]; q.form = "tally, answer only"; return q
    def row1(a, r):
        ks = [k for k in keys if a % k == 0 and 1 <= a // k <= 6]
        if not ks: return None
        k = r.choice(ks); lab = ch(r, [x for g in GRAPH_SETS for x in g]); art = A.picgraph([(lab, a // k)], k, blank=True)
        q = SEM([], lambda v, t_=a: v == t_, str(a), art=art, form="one row with answer box")
        q.sol = [f"⟦{a}⟧"]
        q.extra = lambda ans, art=art: art.meta["rows"][0][1] * art.meta["key"] == ans; return q
    for f_ in (read, read2, read4, more, two, total): f_.pref = 1          # real multi-row graphs are preferred wherever one fits
    return [read, read2, read4, more, two, total, tallyf, tally1, row1]

# ------------------------------------------------------------------ shapes, solids and patterns
SOLIDS = list(A.SOLID_FLAT)
def _shape(tier):
    def flat(a, r):
        ks = [k for k in SOLIDS if A.SOLID_FLAT[k] == a]
        if not ks: return None
        k = r.choice(ks); q = SEM(["Flat surfaces:", f"{BOX}"], lambda v, t_=a: v == t_, str(a), art=A.solids([k]), form="flat surfaces")
        q.extra = lambda ans, k=k: A.SOLID_FLAT[k] == ans; return q
    def flat_row(a, r):
        q = flat(a, r)
        if q: q.layout = "row"; q.lines = ["Flat", "surfaces:", f"{BOX}"]; q.sol = ["Flat", "surfaces:", f"⟦{a}⟧"]; q.form = "flat surfaces, beside"
        return q
    def curved(a, r):
        ks = [k for k in SOLIDS if A.SOLID_CURVED[k] == a]
        if not ks: return None
        k = r.choice(ks); q = SEM(["Curved surfaces:", f"{BOX}"], lambda v, t_=a: v == t_, str(a), art=A.solids([k]), form="curved surfaces")
        q.extra = lambda ans, k=k: A.SOLID_CURVED[k] == ans; return q
    def flat_sum(a, r):
        for _ in range(80):
            ks = [r.choice(SOLIDS) for _ in range(r.choice([2, 3]))]
            if sum(A.SOLID_FLAT[k] for k in ks) == a and len(set(ks)) >= 2 or (sum(A.SOLID_FLAT[k] for k in ks) == a and a in (4, 5)):
                art = A.solids(ks)
                if art.w > 52: continue
                q = SEM(["Flat surfaces", f"in all: {BOX}"], lambda v, t_=a: v == t_, str(a), art=art, form="flat surfaces in all")
                q.extra = lambda ans, ks=ks: sum(A.SOLID_FLAT[k] for k in ks) == ans; return q
        return None
    def count2d(a, r):
        kinds = ["triangle", "square", "rectangle", "circle", "semicircle", "quarter"]
        tgt = r.choice(kinds[:4]); n_other = r.randint(2, 4)
        row = [tgt] * a + [r.choice([k for k in kinds if k != tgt]) for _ in range(n_other)]
        if len(row) > 9: return None
        r.shuffle(row); art = A.shapes_row(row)
        if art.w > 56: return None
        q = SEM([f"How many {tgt}s?" if tgt != "rectangle" else "How many rectangles?", f"{BOX}"], lambda v, t_=a: v == t_, str(a), art=art, form="count shapes")
        q.extra = lambda ans, row=row, tgt=tgt: row.count(tgt) == ans; return q
    def sides(a, r):
        for _ in range(60):
            ks = [r.choice(["triangle", "square", "rectangle", "semicircle", "quarter"]) for _ in range(r.choice([1, 2, 3]))]
            if sum(A.SIDES[k] for k in ks) == a:
                if tier == 1 and len(ks) > 1: continue
                art = A.shapes_row(ks)
                q = SEM(["Straight sides", f"in all: {BOX}"], lambda v, t_=a: v == t_, str(a), art=art, form="straight sides")
                q.extra = lambda ans, ks=ks: sum(A.SIDES[k] for k in ks) == ans; return q
        return None
    def pattern(a, r):
        sh = ["circle", "square", "triangle"]
        for _ in range(80):
            p = r.randint(2, 4); unit = [r.choice(sh) for _ in range(p)]; tgt = r.choice(sh); c = unit.count(tgt)
            if len(set(unit)) < 2 or c == 0: continue
            N = ch(r, [8, 9, 10, 12]); 
            if N % p: continue
            if c * (N // p) != a: continue
            art = A.pattern_row(unit * 2)
            q = SEM([f"Pattern of {N} shapes.", f"How many {tgt}s? {BOX}"], lambda v, t_=a: v == t_, str(a), art=art, form="pattern count")
            q.extra = lambda ans, unit=unit, N=N, tgt=tgt: (unit * (N // len(unit))).count(tgt) == ans; return q
        return None
    def flat_text(a, r):
        ks = [k for k in SOLIDS if A.SOLID_FLAT[k] == a]
        if not ks: return None
        k = r.choice(ks); return SEM([f"A {k} has", f"{BOX} flat surface{'' if a == 1 else 's'}"], lambda v, t_=a: v == t_, str(a), form="flat surfaces, words")
    def flat_text2(a, r):
        ks = [k for k in SOLIDS if A.SOLID_FLAT[k] == a]
        if not ks: return None
        k = r.choice(ks); return SEM(["Flat surfaces", f"{k}: {BOX}"], lambda v, t_=a: v == t_, str(a), form="flat surfaces, short")
    def curved_text(a, r):
        ks = [k for k in SOLIDS if A.SOLID_CURVED[k] == a]
        if not ks: return None
        k = r.choice(ks); return SEM([f"A {k} has", f"{BOX} curved surface"], lambda v, t_=a: v == t_, str(a), form="curved surfaces, words")
    def sides_text(a, r):
        ks = [k for k in ("triangle", "square", "rectangle") if A.SIDES[k] == a]
        if not ks: return None
        k = r.choice(ks); return SEM([f"A {k} has", f"{BOX} straight sides"], lambda v, t_=a: v == t_, str(a), form="straight sides, words")
    def sides_text2(a, r):
        ks = [k for k in ("triangle", "square", "rectangle") if A.SIDES[k] == a]
        if not ks: return None
        k = r.choice(ks); return SEM(["Sides of a", f"{k}: {BOX}"], lambda v, t_=a: v == t_, str(a), form="straight sides, short")
    def sum_line(a, r):
        for _ in range(100):
            ks = [r.choice(("cube", "cylinder", "cone", "sphere", "cuboid")) for _ in range(r.choice([2, 3]))]
            if len(set(ks)) == len(ks) and sum(A.SOLID_FLAT[k] for k in ks) == a:
                return SEM([" + ".join(ks) + f" = {BOX} flat"], lambda v, t_=a: v == t_, str(a), form="flat surfaces, one line")
        return None
    def flat_sum_row(a, r):
        for _ in range(80):
            ks = [r.choice(SOLIDS) for _ in range(r.choice([2, 3]))]
            if len(set(ks)) == len(ks) and sum(A.SOLID_FLAT[k] for k in ks) == a:
                q = SEM([f"{BOX}"], lambda v, t_=a: v == t_, str(a), art=A.solids(ks), layout="row", form="flat surfaces in all, answer only")
                q.extra = lambda ans, ks=ks: sum(A.SOLID_FLAT[k] for k in ks) == ans; return q
        return None
    def sides_row(a, r):
        for _ in range(80):
            ks = [r.choice(["triangle", "square", "rectangle", "semicircle", "quarter"]) for _ in range(2)]
            if sum(A.SIDES[k] for k in ks) == a:
                q = SEM([f"{BOX}"], lambda v, t_=a: v == t_, str(a), art=A.shapes_row(ks), layout="row", form="straight sides in all, answer only")
                q.extra = lambda ans, ks=ks: sum(A.SIDES[k] for k in ks) == ans; return q
        return None
    def sum_text(a, r):
        for _ in range(60):
            ks = [r.choice(("cube", "cylinder", "cone", "sphere", "cuboid")) for _ in range(2)]
            if ks[0] != ks[1] and sum(A.SOLID_FLAT[k] for k in ks) == a:
                return SEM([f"{ks[0]} + {ks[1]}:", f"{BOX} flat surfaces"], lambda v, t_=a: v == t_, str(a), form="two solids, words")
        return None
    forms = [flat, flat_row, curved, count2d, sides, pattern, flat_text, flat_text2, curved_text, sides_text, sides_text2]
    if tier == 2: forms += [flat_sum, sum_text, flat_sum_row, sides_row, sum_line]
    return forms

def build_banks():
    B = {}
    B["numbers"] = Bank("numbers", "Numbers to 1000", "Numbers to 1000: place value, order", "Find the number. Find it in the key. Colour the part with that colour.",
        {1: T([120, 250, 340, 470, 560], range(0, 1001), _numbers(1)), 2: T([105, 218, 346, 407, 639], range(0, 1001), _numbers(2))})
    B["pattern"] = Bank("pattern", "Number Patterns", "Number patterns: counting in steps up to 100", "Find the missing number. Find it in the key. Colour the part with that colour.",
        {1: T([210, 300, 350, 420, 500], range(0, 1001), _pattern(1)), 2: T([135, 248, 376, 480, 615], range(0, 1001), _pattern(2))})
    B["oddeven"] = Bank("oddeven", "Odd and Even", "Odd and even numbers", "Find the number. Find it in the key. Colour the part with that colour.",
        {1: T([9, 12, 15, 18, 21], range(0, 1001), _oddeven(1)), 2: T([200, 301, 402, 503, 604], range(0, 1001), _oddeven(2))})
    B["add"] = Bank("add", "Addition", "Addition within 1000, with renaming", "Add. Find the answer in the key. Colour the part with that colour.",
        {1: T([135, 252, 341, 428, 563], range(0, 1001), _add(1)), 2: T([412, 536, 653, 724, 841], range(0, 1001), _add(2))})
    B["sub"] = Bank("sub", "Subtraction", "Subtraction within 1000, with renaming", "Subtract. Find the answer in the key. Colour the part with that colour.",
        {1: T([125, 237, 346, 458, 569], range(0, 1001), _sub(1)), 2: T([158, 247, 364, 475, 586], range(0, 1001), _sub(2))})
    B["mult"] = Bank("mult", "Multiplication", "Multiplication: tables of 2, 3, 4, 5 and 10", "Multiply. Find the answer in the key. Colour the part with that colour.",
        {1: T([12, 15, 18, 20, 30], range(0, 101), _mult(1), maxuse={15: 2}), 2: T([24, 28, 35, 40, 45], range(0, 101), _mult(2))})   # 15 = 3 x 5 or 5 x 3 only
    B["div"] = Bank("div", "Sharing", "Division: sharing and grouping", "Share or group. Find the answer in the key. Colour the part with that colour.",
        {1: T([2, 3, 4, 5, 6], range(0, 101), _div(1)), 2: T([6, 7, 8, 9, 10], range(0, 101), _div(2))})
    fr_dom = [(a, b) for b in range(2, 13) for a in range(1, b)]
    B["frac"] = Bank("frac", "Fractions", "Fractions: parts, compare, add and subtract like fractions", "Find the fraction. Find it in the key. Colour the part with that colour.",
        {1: T([(1, 2), (1, 3), (1, 4), (2, 3), (3, 4)], fr_dom, _frac(1), lambda v: FRAC(*v)), 2: T([(1, 6), (3, 8), (5, 8), (7, 10), (5, 12)], fr_dom, _frac(2), lambda v: FRAC(*v))},
        parts=[("shaded parts", lambda f, a: f in ("shaded", "shaded_bar", "shaded_row", "unshaded")), ("parts of a whole", lambda f, a: f in ("parts", "whole")),
               ("add and subtract like fractions", lambda f, a: f in ("add", "sub")), ("compare", lambda f, a: f in ("cmp_unit", "cmp_like"))], prefix="Fractions: ")
    B["money"] = Bank("money", "Money", "Money: dollars, cents, decimal notation", "Find how much. Find it in the key. Colour the part with that colour.",
        {1: T([120, 235, 305, 450, 680], range(0, 2001), _money(1), lambda v: f"${dec(v)}"), 2: T([35, 65, 135, 185, 250], range(0, 2001), _money(2), lambda v: f"{v}¢")},
        {1: "Money in dollars and cents (decimal notation)", 2: "Money: cents and dollars, decimal notation"})
    tm = [(h, m) for h in range(1, 13) for m in range(60)]
    B["time"] = Bank("time", "Time", "Time to the minute; hours and minutes", "Find the time. Find it in the key. Colour the part with that colour.",
        {1: T([(2, 40), (4, 55), (6, 45), (8, 35), (10, 15)], tm, _time(1), hm), 2: T([45, 75, 90, 105, 135], range(0, 601), _time(2), lambda v: f"{v} min",
            instr="Find how many minutes. Find the answer in the key. Colour the part with that colour.")},
        {1: "Time: hours and minutes", 2: "Time: hours, minutes and how long"})
    md = [(n, u) for u in ("cm", "m", "g", "kg", "l") for n in range(0, 1001)]
    B["measure"] = Bank("measure", "Measures", "Length, mass and volume", "Find the measure (a ruler strip starts at its arrow). Find it in the key. Colour the part with that colour.",
        {1: T([(5, "cm"), (9, "cm"), (4, "kg"), (8, "kg"), (6, "l")], md, _measure(1), lambda v: f"{v[0]} {v[1]}"), 2: T([(35, "cm"), (60, "cm"), (250, "g"), (450, "g"), (12, "l")], md, _measure(2), lambda v: f"{v[0]} {v[1]}")},
        parts=[("cm", lambda f, a: a[1] == "cm"), ("g", lambda f, a: a[1] == "g"), ("kg", lambda f, a: a[1] == "kg"), ("l", lambda f, a: a[1] == "l")],
        prefix="Length, mass and volume: ")
    B["graph"] = Bank("graph", "Graphs", "Picture graphs and tally marks", "Read the graph. Find the answer in the key. Colour the part with that colour.",
        {1: T([4, 6, 8, 10, 12], range(0, 101), _graph(1)), 2: T([6, 8, 10, 12, 15], range(0, 101), _graph(2))})
    B["shape"] = Bank("shape", "Shapes", "2D and 3D shapes and shape patterns", "Look at the shapes. Find the answer in the key. Colour the part with that colour.",
        {1: T([1, 2, 3, 4, 6], range(0, 21), _shape(1)), 2: T([5, 7, 8, 9, 12], range(0, 21), _shape(2))})
    return B
BANKS = build_banks()

GALLERY = [
    dict(id="CBC-P2-01", picture="rocket", bank="numbers", tier=1, seed=301),
    dict(id="CBC-P2-02", picture="car", bank="add", tier=2, seed=302),
    dict(id="CBC-P2-03", picture="owl", bank="sub", tier=2, seed=303),
    dict(id="CBC-P2-04", picture="house", bank="mult", tier=1, seed=304),
    dict(id="CBC-P2-05", picture="castle", bank="div", tier=1, seed=305),
    dict(id="CBC-P2-06", picture="owl", bank="frac", tier=1, seed=4),
    dict(id="CBC-P2-07", picture="dinosaur", bank="money", tier=2, seed=1),
    dict(id="CBC-P2-08", picture="butterfly", bank="time", tier=1, seed=308),
    dict(id="CBC-P2-09", picture="sailboat", bank="measure", tier=2, seed=309),
    dict(id="CBC-P2-10", picture="butterfly", bank="graph", tier=2, seed=10),
    dict(id="CBC-P2-11", picture="butterfly", bank="shape", tier=1, seed=316),
    dict(id="CBC-P2-12", picture="icecream", bank="oddeven", tier=2, seed=323),
    dict(id="CBC-P2-13", picture="fish", bank="pattern", tier=1, seed=1),
    dict(id="CBC-P2-14", picture="dinosaur", bank="mult", tier=2, seed=1),
    dict(id="CBC-P2-15", picture="house", bank="frac", tier=2, seed=1),
]
