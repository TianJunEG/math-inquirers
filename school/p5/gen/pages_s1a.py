"""Semester 1, part A: P5-01 Millions; P5-02 Seven Digits; P5-03 Ten, Hundred, Thousand; P5-04 Multiples Route; P5-06 Brackets Match; P5-07 Both Sides Equal.
(P5-05 is a colour-by-code page, in pages_cbc.py.)"""
import random, re, math, itertools
from fractions import Fraction
from .common import *
from .kit import *
from .kit5 import *
from .numwords import words, words_to_int

def ival(t):
    """the whole number written in a printed text (spaces between groups ignored)"""
    return int(re.sub(r"[^\d]", "", t))

def swap_variants(rng, n, k=2):
    """k different 7-digit numbers made from n by swapping two neighbouring different digits (never a leading zero)"""
    s = str(n); out = []
    pos = [i for i in range(len(s) - 1) if s[i] != s[i + 1]]
    rng.shuffle(pos)
    for i in pos:
        t = list(s); t[i], t[i + 1] = t[i + 1], t[i]
        if t[0] == "0": continue
        v = int("".join(t))
        if v != n and v not in out: out.append(v)
        if len(out) == k: break
    return out

# =============================================================================== P5-01 Millions (lettered choices)
PLACES = {10_000: "ten thousands", 100_000: "hundred thousands", 1000: "thousands", 100: "hundreds", 1_000_000: "millions"}

def page01():
    rng = random.Random(5101)
    for _attempt in range(400):
        word = word_candidates(1, 6)[0]
        rows = []
        # 1 value of a digit
        n1 = rng.choice([x for x in range(1_000_000, 9_999_999) if len(set(str(x))) == 7 and "0" not in str(x)])
        pos = rng.randint(3, 5); d = str(n1)[::-1][pos]; v = int(d) * 10 ** pos
        rows.append(dict(q=f"In {num(n1)}, what is the value of the digit {d}?", opts=[num(v), num(v * 10), num(v // 10)]))
        # 2 numeral to words
        digs = [rng.randint(1, 9)] + [rng.choice([0, 0, rng.randint(1, 9)]) for _ in range(6)]
        n2 = int("".join(map(str, digs)))
        vs = swap_variants(rng, n2)
        if n2 % 10 == 0 or len(vs) < 2 or "0" not in str(n2): continue
        rows.append(dict(q=f"Which is {num(n2)} in words?", opts=[words(n2)] + [words(x) for x in vs], col=True, wide=True))
        # 3 words to numeral
        n3 = int("".join(map(str, [rng.randint(1, 9)] + [rng.choice([0, rng.randint(1, 9)]) for _ in range(6)])))
        vs3 = swap_variants(rng, n3)
        if len(vs3) < 2 or n3 % 10 == 0 or "0" not in str(n3) or n3 in (n2,): continue
        rows.append(dict(q=f"Which number is {words(n3)}?", opts=[num(n3)] + [num(x) for x in vs3], wide=True))
        # 4 expanded form
        a = rng.randint(1, 9) * 1_000_000; b = rng.randint(1, 9) * rng.choice([10_000, 100_000]); c = rng.randint(1, 9) * 100; e = rng.randint(1, 9)
        n4 = a + b + c + e
        wrong = [a + b + c * 10 + e, a + (b * 10 if b * 10 < 1_000_000 else b // 10) + c + e]
        if len({n4, *wrong}) < 3 or max(n4, *wrong) >= 10_000_000: continue
        rows.append(dict(q=f"Which number is {num(a)} + {num(b)} + {c} + {e}?", opts=[num(n4)] + [num(x) for x in wrong], wide=True))
        # 5 greatest
        base = rng.randint(1_000_000, 8_999_999)
        s = str(base); i = rng.randint(2, 4)
        cands = {base}
        for dd in rng.sample("123456789", 9):
            t = s[:i] + dd + s[i + 1:]
            if t != s: cands.add(int(t))
            if len(cands) == 3: break
        if len(cands) < 3: continue
        cs = sorted(cands, reverse=True)
        rows.append(dict(q="Which number is the greatest?", opts=[num(cs[0]), num(cs[1]), num(cs[2])], wide=True))
        # 6 a digit in a place
        pl = rng.choice([10_000, 100_000, 1000]); k_ = int(math.log10(pl))
        dd = str(rng.randint(2, 9))
        def with_digit(at):
            while True:
                t = [rng.choice([c for c in "0123456789" if c != dd]) for _ in range(7)]
                t[-1 - at] = dd
                if t[0] != "0": return int("".join(t))
        good = with_digit(k_)
        bad = []
        for at in rng.sample([x for x in range(7) if x != k_], 6):
            v = with_digit(at)
            if v not in bad: bad.append(v)
            if len(bad) == 2: break
        rows.append(dict(q=f"Which number has the digit {dd} in the {PLACES[pl]} place?", opts=[num(good)] + [num(x) for x in bad], wide=True))
        break
    else: raise RuntimeError("p01")

    def solve_row(q, opts, qh):
        o_int = [ival(t) if re.search(r"\d", t) else None for t in opts]
        m = re.fullmatch(r"In ([\d ]+), what is the value of the digit (\d)\?", q.replace(NB, " "))
        if m:
            nn = m.group(1).replace(" ", ""); dg = m.group(2); v_ = int(dg) * 10 ** (len(nn) - 1 - nn.index(dg))
            return o_int.index(v_)
        m = re.fullmatch(r"Which is ([\d ]+) in words\?", q.replace(NB, " "))
        if m:
            nn = int(m.group(1).replace(" ", "")); return [words_to_int(t) for t in opts].index(nn)
        if q == "Which number is the greatest?": return o_int.index(max(o_int))
        m = re.fullmatch(r"Which number is ([a-z ,\-]+)\?", q)
        if m:
            nn = words_to_int(m.group(1)); return o_int.index(nn)
        m = re.fullmatch(r"Which number is ([\d + ]+)\?", q.replace(NB, ""))
        if m:
            return o_int.index(int(evaluate(m.group(1))))
        if q == "Which number is the greatest?": return o_int.index(max(o_int))
        m = re.fullmatch(r"Which number has the digit (\d) in the ([a-z ]+) place\?", q)
        if m:
            p_ = {v: k for k, v in PLACES.items()}[m.group(2)]; k = int(math.log10(p_))
            hit = [i for i, t in enumerate(opts) if str(ival(t))[-1 - k] == m.group(1)]
            return hit[0] if len(hit) == 1 else -1
        raise ValueError(q)

    key = "; ".join(f"{i+1}) {r['opts'][0]}" for i, r in enumerate(rows))
    P = mc_page(1, 5101, "Millions", 1, "Whole numbers: numbers to 10 million", STRAND_WN,
        "numbers to 10 million: reading and writing numbers in numerals and words, place value", ["WN1.1"], "Lettered choices (place value)",
        ["Read each question.", "Circle the letter of the right choice in each row.", "Write the six letters in the boxes."],
        rng, rows, 3, word, key,
        "Six place-value questions with numbers to 10 million: the value of a digit, a numeral in words, words as a numeral, an expanded number, the greatest of three and the number with a digit in a named place. The wrong choices are the usual slips (a place value one place too high or too low, two neighbouring digits swapped, a zero in the wrong place). Each choice has a letter; the right choices spell the word. Every other way of choosing was tested against a very large word list. A box left blank gives no letter and the check cannot see it.",
        solve_row, rows_cls="tfrows tight")
    return P


# =============================================================================== P5-02 Seven Digits (code word)
KINDS2 = ["smallest number", "greatest number", "greatest even number", "smallest odd number", "smallest number with {d} in the thousands place", "greatest number with {d} in the ten thousands place"]

def brute(digs, clue):
    """independent solver: try every arrangement of the seven digit cards (no leading zero) and keep those that fit the clue"""
    best = None
    ok = []
    for p in set(itertools.permutations(digs)):
        if p[0] == 0: continue
        n = int("".join(map(str, p)))
        if "even number" in clue and n % 2: continue
        if "odd number" in clue and n % 2 == 0: continue
        m = re.search(r"with (\d) in the (ten thousands|thousands) place", clue)
        if m:
            idx = 3 if m.group(2) == "thousands" else 2
            if p[idx] != int(m.group(1)): continue
        ok.append(n)
    return min(ok) if clue.startswith("Make the smallest") else max(ok)

def make2(digs, kind, d):
    """constructive answer (a different method from `brute`)"""
    ds = sorted(digs)
    if kind == "smallest":
        i = next(k for k, x in enumerate(ds) if x); ds[0], ds[i] = ds[i], ds[0]; return int("".join(map(str, ds)))
    if kind == "greatest": return int("".join(map(str, sorted(digs, reverse=True))))
    if kind == "greatest even":
        ev = min(x for x in digs if x % 2 == 0); rest = sorted(list(digs), reverse=True); rest.remove(ev); return int("".join(map(str, rest + [ev])))
    if kind == "smallest odd":
        best = None
        for od in sorted(set(x for x in digs if x % 2 == 1)):
            rest = sorted(list(digs)); rest.remove(od)
            i = next(k for k, x in enumerate(rest) if x); rest[0], rest[i] = rest[i], rest[0]
            v = int("".join(map(str, rest + [od])))
            if best is None or v < best: best = v
        return best
    raise ValueError(kind)

def page02():
    rng = random.Random(5102)
    for _ in range(4000):
        items = []
        kinds = KINDS2[:]; rng.shuffle(kinds)
        used = set()
        for kd in kinds:
            digs = rng.sample(range(10), 7)
            if 0 not in digs: digs[rng.randrange(7)] = 0
            if len(set(digs)) < 7 or not any(x % 2 for x in digs) or sum(1 for x in digs if x % 2 == 0) < 2: break
            d = rng.choice([x for x in digs if x not in (0,)])
            clue = "Make the " + kd.format(d=d) + "."
            items.append((digs, clue, kd, d))
        else:
            # computed answers (brute force is the independent solver and runs in the page check)
            ans = []
            for digs, clue, kd, d in items:
                m = re.search(r"with (\d) in the (ten thousands|thousands) place", clue)
                ans.append(brute(digs, clue))
            if not distinct(ans): continue
            pool = []
            for (digs, clue, kd, d), a in zip(items, ans):
                for other in ("smallest", "greatest", "greatest even", "smallest odd"):
                    if kd.startswith(other) and ("with" not in kd) and ((other in ("smallest", "greatest") and kd in (other + " number",)) or other in kd): continue
                    pool.append(make2(digs, other, d))
                z = sorted(digs); pool.append(int("".join(map(str, z))))           # arranged smallest-first with the leading zero left in
                pool.append(a + 9 if a % 10 == 0 else a - (a % 10) + 0)
            pool = [p for p in dict.fromkeys(pool) if p not in ans and p >= 1_000_000]
            res = code_table_for(2, ans, rng, pool, n_decoy=2, tries=60)
            if res[0]: (word, table), dom = res; break
    else: raise RuntimeError("p02")
    cards = []
    for i, (digs, clue, kd, d) in enumerate(items):
        tiles = '<div class="dtiles">' + "".join(f'<span class="dtile">{x}</span>' for x in digs) + "</div>"
        cards.append(qc(i + 1, f'<p class="ptxt">{clue}</p>{tiles}', abx("w6")))
    solved = []
    for c in cards:
        digs = [int(x) for x in re.findall(r'<span class="dtile">(\d)</span>', c)]
        clue = re.search(r'<p class="ptxt">(.*?)</p>', c).group(1)
        solved.append(brute(digs, clue))
    P = code_page(2, 5102, "Seven Digits", 2, "Whole numbers: making numbers to 10 million from digit cards", STRAND_WN,
        "numbers to 10 million: place value, reading and writing numbers", ["WN1.1"], "Code-breaker (digit cards)",
        ["Use all seven digit cards once.", "Make the number the question asks for.", "Write it in the box. Use the code table."],
        cards, ans, word, table, dom, lambda k: num(k), "; ".join(f"{i+1}) {num(a)}" for i, a in enumerate(ans)),
        "Six digit-card questions, each with seven different digit cards including a zero. The pupil makes the smallest or greatest number, the greatest even or smallest odd number, or the smallest or greatest number with a stated digit in the thousands or ten thousands place. A number cannot start with 0. The decoy letters stand for the answers a pupil gets by putting the cards in the wrong order, by forgetting the zero rule, or by answering a different question on the same cards. A box left blank gives no letter and the check cannot see it.",
        solved, cols=4, layout="c2",
        checks=[("V7 every answer is a 7-digit number below 10 million", all(1_000_000 <= a < 10_000_000 for a in ans), ""),
                ("V1b the constructive answer (sorting the cards) equals the brute-force answer for the first four kinds", all(make2(digs, kd.replace(" number", ""), d) == a for (digs, clue, kd, d), a in zip(items, ans) if "with" not in kd), "")])
    return P

# =============================================================================== P5-03 Ten, Hundred, Thousand (ordering)
def page03():
    rng = random.Random(5103)
    for _ in range(5000):
        word = word_candidates(3, 6)[0]
        cards = []
        vals = set()
        for _k in range(6):
            p = rng.choice([10, 100, 1000]); op = rng.choice(["\u00d7", "\u00f7"])
            if op == "\u00d7":
                a = rng.choice([rng.randint(2, 99), rng.randint(100, 999), rng.randint(1000, 9999)]); v = a * p
                if v >= 10_000_000: break
            else:
                v = rng.choice([rng.randint(2, 99), rng.randint(100, 999), rng.randint(1000, 9999)]); a = v * p
                if a >= 10_000_000: break
            if v in vals: break
            vals.add(v); cards.append((f"{num(a)} {op} {num(p)}", v))
        else:
            vs = sorted(vals)
            # keep the order puzzling: the numbers being multiplied must not already be in the same order as the answers
            if len({c[0].split()[0] for c in cards}) == 6 and sorted(cards, key=lambda c: ival(c[0].split()[0])) != sorted(cards, key=lambda c: c[1]):
                break
    else: raise RuntimeError("p03")
    P = order_page(3, 5103, "Zero Hunt", 1, "Whole numbers: multiplying and dividing by 10, 100 and 1000", STRAND_WN,
        "multiplying and dividing whole numbers by 10, 100 and 1000", ["WN2.1"], "Ordering (lettered cards)",
        ["Work out the answer on each card.", "Put the answers in order, smallest first.", "Write the card letters in the boxes below."],
        rng, cards, word, True,
        "Order (smallest first): " + ", ".join(f"{c[0]} = {num(c[1])}" for c in sorted(cards, key=lambda c: c[1])),
        "Six cards, each a whole number multiplied or divided by 10, 100 or 1000. The cards are not in the order of the numbers printed on them: the pupil has to work out each answer and then order the six answers from smallest to greatest. The letters, read in that order, spell a word with exactly one arrangement that is a word, so no wrong order of the six cards spells a word (every wrong order was tested against a very large word list). A box left blank gives no letter and the check cannot see it.",
        lambda t: evaluate(t), work=True, cols=2, checks=[("V7 every number printed and every answer is below 10 million", all(v < 10_000_000 for _, v in cards), "")])
    return P

# =============================================================================== P5-04 Multiples Route (route)
M4 = [20, 30, 40, 50, 60, 70, 80, 90, 200, 300, 400, 500, 600, 700, 800, 900, 2000, 3000, 4000]

def form4(rng, V, bias=None):
    """a cell 'a x m' or 'b / m' whose value is V (whole numbers below 10 million), m a multiple of 10, 100 or 1000"""
    opts = []
    for m in M4:
        if V % m == 0 and V // m >= 2: opts.append((f"{num(V // m)} \u00d7 {num(m)}"))
        if V * m < 10_000_000: opts.append(f"{num(V * m)} \u00f7 {num(m)}")
    return rng.choice(opts) if opts else None

def page04():
    rng = random.Random(5104)
    T = rng.choice([7200, 4800, 3600, 9600, 5400, 2400, 8400])
    n = 4; L = 8
    offs = [T * 10, T // 10, T * 100 if T * 100 < 10_000_000 else T * 5, T // 100, T * 2, T // 2, T + T // 4 if (T + T // 4) % 10 == 0 else T * 3, T - T // 4]
    def make_on(i):
        return form4(rng, T)
    def make_off():
        while True:
            t = form4(rng, rng.choice(offs))
            if t: return t
    path, grid, dead = build_route(rng, n, L, make_on, make_off, 3, ok_text=lambda t: evaluate(to_text(t)) == T)
    rule = lambda cell: evaluate(to_text(cell)) == T
    P = route_page(4, 5104, "Multiples Route", 2, "Whole numbers: multiplying and dividing by multiples of 10, 100 and 1000", STRAND_WN,
        "multiplying and dividing whole numbers by 10, 100, 1000 and their multiples", ["WN2.1"], "Maze / path",
        ["Start at START. Move up, down, left or right.", f"Step only on boxes with the answer {num(T)}.", "Do not step on a box twice."],
        grid, path, dead, "", rule,
        f"A 4 by 4 grid of sixteen calculations, each a whole number multiplied or divided by a multiple of 10, 100 or 1000 . The boxes off the route make answers that come from a slip in the zeros (ten or a hundred times too big or too small) and some other near misses; some extra boxes that do make {num(T)} are dead ends. Counting the boxes shows a line that takes a shortcut.",
        lambda c: to_text(c), f"Does your line reach FINISH? Count its boxes: are there {L}? Does every box make {num(T)}?",
        checks=[("V7 every number printed is below 10 million", all(evaluate(to_text(g)) < 10_000_000 and max(int(x.replace(NB, "")) for x in re.findall(r"[\d\u00a0]+", g)) < 10_000_000 for row in grid for g in row), "")],
        extra_facts=str(T))
    return P

# =============================================================================== P5-06 Brackets Match (matching)
TEMPL6 = [("({a} \u2212 {b}) \u00f7 {c} + {d}", lambda a, b, c, d: (a - b) % c == 0 and a > b),
          ("{a} \u00d7 ({b} + {c}) \u2212 {d}", lambda a, b, c, d: a * (b + c) > d),
          ("{a} \u00f7 ({b} + {c}) \u00d7 {d}", lambda a, b, c, d: a % (b + c) == 0 and a // (b + c) >= 2),
          ("({a} + {b}) \u00d7 ({c} \u2212 {d})", lambda a, b, c, d: c > d),
          ("{a} \u2212 ({b} + {c}) \u00d7 {d}", lambda a, b, c, d: a > (b + c) * d),
          ("({a} \u2212 {b}) \u00d7 {c} \u00f7 {d}", lambda a, b, c, d: a > b and (a - b) * c % d == 0),
          ("{a} + {b} \u00d7 ({c} \u2212 {d})", lambda a, b, c, d: c > d),
          ("({a} + {b}) \u00f7 {c} \u00d7 {d}", lambda a, b, c, d: (a + b) % c == 0)]

def nobracket(t):
    return evaluate(t.replace("(", "").replace(")", ""))

def page06():
    rng = random.Random(5106)
    for _ in range(6000):
        word = word_candidates(6, 6)[0]
        tmpl = rng.sample(TEMPL6, 6); cards = []
        for tp, okf in tmpl:
            for _t in range(60):
                a, b, c, d = rng.randint(2, 60), rng.randint(2, 20), rng.randint(2, 9), rng.randint(2, 9)
                if okf(a, b, c, d):
                    txt = tp.format(a=a, b=b, c=c, d=d)
                    try: v = evaluate(txt)
                    except Exception: continue
                    if v.denominator == 1 and 6 <= v <= 400 and nobracket(txt) != v and ("\u2212" not in txt or True):
                        cards.append((txt, int(v))); break
            else: break
        if len(cards) == 6 and distinct([v for _, v in cards]) and all(nobracket(t) >= 0 for t, _ in cards):
            if distinct([nobracket(t) for t, _ in cards]): break
    else: raise RuntimeError("p06")
    # tiles in the order of the word: the card with letter word[i] sits at tile i; the display order of tiles is by value so the tile order is not the card order
    order = sorted(range(6), key=lambda k: cards[k][1])
    pairs_by_tile = [cards[k] for k in order]
    pairs = [(c[0], str(c[1])) for c in pairs_by_tile]
    P = match_page(6, 5106, "Brackets Match", 2, "Whole numbers: order of operations and brackets", STRAND_WN,
        "order of operations and use of brackets, without a calculator", ["WN2.2", "WN2.3"], "Matching (lettered cards)",
        ["Work out the value of each card.", "Find the tile with that value.", "Write the card's letter in the box under the tile."],
        rng, pairs, word,
        "; ".join(f"{w}: {t} = {v}" for w, (t, v) in zip(word, pairs_by_tile)),
        "Six cards with brackets and the four operations; the value of each is a whole number found in the usual order (brackets first, then multiplication and division from left to right, then addition and subtraction). Every card gives a different value when the brackets are ignored, so a pupil who ignores them finds no matching tile or the wrong one. The tiles are in order of their values, smallest first; the letters, read from tile 1 to tile 6, spell a word with exactly one arrangement that is a word, so no wrong matching spells a word. A box left blank gives no letter and the check cannot see it.",
        lambda t: evaluate(t), lambda t: evaluate(t), left_title="Cards", right_title="Tiles",
        checks=[("V1c ignoring the brackets gives a different value on every card", all(nobracket(t) != evaluate(t) for t, _ in cards), ""),
                ("V7 all values whole numbers from 6 to 400", all(6 <= v <= 400 for _, v in cards), "")])
    return P

# =============================================================================== P5-07 Both Sides Equal (put the answer back)
FORMS7 = [("{a} \u00d7 ({X} + {b}) = {c}", lambda a, b, c, x: a * (x + b) == c),
          ("({X} \u2212 {a}) \u00f7 {b} = {c}", lambda a, b, c, x: (x - a) % b == 0 and (x - a) // b == c),
          ("{a} + {b} \u00d7 {X} = {c}", lambda a, b, c, x: a + b * x == c),
          ("{X} \u00f7 {a} \u2212 {b} = {c}", lambda a, b, c, x: x % a == 0 and x // a - b == c),
          ("({a} + {X}) \u00d7 {b} \u2212 {c} = {d}", None),
          ("{a} \u00d7 {X} + {b} \u00f7 {c} = {d}", None)]

def page07():
    rng = random.Random(5107)
    eqs = []
    while len(eqs) < 6:
        k = len(eqs)
        a, b, c = rng.randint(2, 9), rng.randint(2, 12), rng.randint(2, 12)
        x = rng.randint(3, 40)
        if k == 0: txt = f"{a} \u00d7 (\u25a1 + {b}) = {a * (x + b)}"
        elif k == 1: txt = f"(\u25a1 \u2212 {b}) \u00f7 {a} = {x}"; x = x * a + b
        elif k == 2: txt = f"{b} + {a} \u00d7 \u25a1 = {b + a * x}"
        elif k == 3: x = a * x; txt = f"\u25a1 \u00f7 {a} \u2212 {b} = {x // a - b}" if x // a > b else None
        elif k == 4: txt = f"({a} + \u25a1) \u00d7 {c} \u2212 {b} = {(a + x) * c - b}"
        else:
            cc = rng.choice([2, 3, 4, 5]); txt = f"{a} \u00d7 \u25a1 + {cc * b} \u00f7 {cc} = {a * x + b}"
        if txt is None: continue
        eqs.append((txt, x))
    ans = [x for _, x in eqs]
    P = None
    rows = []
    for i, (t, x) in enumerate(eqs):
        h = t.replace("\u25a1", '<span class="ab"></span>')
        rows.append(f'<div class="eqrow"><span class="no">{i+1}</span><span class="eqt">{h}</span></div>')
    body = '<div class="eqlist">' + "".join(rows) + "</div>"
    P = new_page(7, 5107, "Both Sides Equal", 2, "Whole numbers: order of operations and brackets in number sentences", STRAND_WN,
        "order of operations and use of brackets: finding the missing number", ["WN2.2", "WN2.3"], "Balance (put the answer back)",
        "K7 put the answers back: every line must be true",
        ["Find the number that goes in each box.", "Use the order of operations.", "Write the number in the box."],
        body, "; ".join(f"{i+1}) {x}" for i, x in enumerate(ans)), "Every line is true when its number is put back.",
        "Six number sentences, each with one empty box and brackets, multiplication, division, addition and subtraction. The pupil finds the number by working backwards or by trying numbers, then puts it back in the box to see whether both sides are equal. Each sentence has one answer. The page has no code word: a wrong number makes its line false, and a blank box is seen at once.",
        check="Put each number back in its box. Is every line true?", mk=("equal",), ps=True,
        mech_plain="Put every number back in its box: both sides of every line must be equal")
    solved = []
    for r in re.findall(r'<span class="eqt">(.*?)</span></div>', body, re.S):
        t = to_text(r.replace('<span class="ab"></span>', "\u25a1"))
        lhs, rhs = t.split("=")
        hit = [x for x in range(0, 1000) if evaluate(lhs.replace("\u25a1", f"({x})")) == evaluate(rhs.replace("\u25a1", f"({x})"))]
        solved.append(hit[0] if len(hit) == 1 else None)
    P.v("V1 independent solver (tries every whole number 0 to 999 in each printed line) finds exactly one answer per line and it equals the key", solved == ans, solved)
    def true_all(a):
        for (t, _), x in zip(eqs, a):
            lhs, rhs = t.replace("\u25a1", f"({x})").split("=")
            if evaluate(lhs) != evaluate(rhs): return False
        return True
    dom = list(range(0, 400))
    P.v("V3 every single wrong whole number (0 to 399) in one box makes its line false", all(not true_all([a if j != k else v for j, a in enumerate(ans)]) for k in range(6) for v in dom if v != ans[k]))
    P.v("V7 all answers are whole numbers from 3 to 400", all(3 <= a <= 400 for a in ans))
    P["cv"] = dict(rate=1.0, single_total=6 * 399, single_detected=6 * 399)
    P["model"] = dict(truth=list(ans), domains=[dom] * 6, check=true_all, numeric=True)
    P["facts"] = ""
    return P

PAGES = [page01, page02, page03, page04, page06, page07]
