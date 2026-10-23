"""Semester 1, part C: P5-14 Fraction Products; P5-15 Big Products; P5-16 Remainder Stories; P5-17 Point Shift; P5-18 True or False Decimals;
P5-19 Measures in Decimals; P5-20 Unit Switch."""
import random, re, math, itertools
from fractions import Fraction as Fr
from .common import *
from .kit import *
from .kit5 import *

FM = lambda f: frac_val(f, True)

def dec_of(t):
    return evaluate(t)

# =============================================================================== P5-14 Fraction Products (ordering)
def page14():
    rng = random.Random(5114)
    for _ in range(20000):
        word = word_candidates(14, 6)[0]
        cards = []
        for k in range(6):
            b, d = rng.choice([3, 4, 5, 6, 8, 9, 10]), rng.choice([3, 4, 5, 6, 7, 8, 9, 10])
            a = rng.randint(1, b - 1) if k != 5 else rng.randint(1, b - 1)
            c = rng.randint(1, d - 1) if k < 4 else rng.randint(d + 1, d + 3)
            if math.gcd(a, b) != 1 or math.gcd(c, d) != 1: break
            v = Fr(a, b) * Fr(c, d)
            if v.denominator == 1 or v > 3: break
            cards.append((f"{FR(a, b)} × {FR(c, d)}", v))
        else:
            vs = sorted(v for _, v in cards)
            if len(set(vs)) == 6 and min(y - x for x, y in zip(vs, vs[1:])) >= Fr(1, 40) and cards != sorted(cards, key=lambda c: c[1]) and sum(1 for _, v in cards if v >= 1) <= 2:
                break
    else: raise RuntimeError("p14")
    P = order_page(14, 5114, "Fraction Products", 2, "Fractions: multiplying a proper fraction by a proper or improper fraction", STRAND_FR,
        "multiplying a proper fraction by a proper or improper fraction", ["FR2.3"], "Ordering (lettered cards)",
        ["Work out the product on each card.", "Put the products in order, smallest first.", "Write the card letters in the boxes below."],
        rng, cards, word, True, "Order (smallest first): " + ", ".join(f"{to_text(c[0])} = {frac_txt(c[1])}" for c in sorted(cards, key=lambda c: c[1])),
        "Six cards, each the product of two fractions: a proper fraction times a proper fraction (four cards) or times an improper fraction (two cards). The cards are not in order: the pupil works out each product and puts the six products in order from smallest to greatest. The letters, read in that order, spell a word with exactly one arrangement that is a word, so no wrong order spells a word. A box left blank gives no letter and the check cannot see it.",
        lambda t: evaluate(t), cols=2, work=True)
    return P

# =============================================================================== P5-15 Big Products (lettered choices)
def slips_product(rng, a, b, c, d, right):
    """plausible wrong values for (a/b) x (c/d)"""
    s = [Fr(a * c, b + d), Fr(a + c, b * d), Fr(a * c + 1, b * d), right + 1, right - Fr(1, 2) if right > Fr(1, 2) else right + Fr(1, 2), Fr(a * d, b * c)]
    return [x for x in dict.fromkeys(s) if x != right and x > 0 and x.denominator <= 40]

def page15():
    rng = random.Random(5115)
    for _attempt in range(3000):
        word = word_candidates(15, 6)[0]
        rows = []; qs = []
        ok = True
        for kind in ["ii", "mw", "iw", "pi", "mw", "ii"]:
            if kind in ("ii", "pi"):
                b, d = rng.choice([3, 4, 5, 6, 8]), rng.choice([3, 4, 5, 6, 7])
                a = rng.randint(b + 1, 2 * b + 1) if kind == "ii" else rng.randint(1, b - 1)
                c = rng.randint(d + 1, 2 * d + 1)
                if math.gcd(a, b) != 1 or math.gcd(c, d) != 1: ok = False; break
                right = Fr(a, b) * Fr(c, d)
                if right.denominator == 1: ok = False; break
                wr = slips_product(rng, a, b, c, d, right)
                q = f"{FR(a, b)} × {FR(c, d)} ="
            elif kind == "mw":
                w, d = rng.randint(1, 4), rng.choice([3, 4, 5, 6, 8]); n = rng.randint(1, d - 1); W = rng.randint(3, 9)
                if math.gcd(n, d) != 1 or W % d == 0: ok = False; break
                right = (w + Fr(n, d)) * W
                wr = [w * W + Fr(n, d), (w + 1) * W + Fr(n, d) if False else w * W + Fr(n, d) * (W - 1), right + 1, right - Fr(1, 2) if right > 1 else right + 1, Fr(w * n, d) * W]
                wr = [x for x in dict.fromkeys(wr) if x != right and x > 0]
                q = f"{MX(w, n, d)} × {W} ="
            else:
                b = rng.choice([3, 4, 5, 6, 8]); a = rng.randint(b + 1, 2 * b + 2); W = rng.randint(3, 9)
                if math.gcd(a, b) != 1 or W % b == 0: ok = False; break
                right = Fr(a, b) * W
                wr = [Fr(a, b * W), Fr(a * W, b * W + 1) if False else Fr(a + W, b), right + 1, right - 1, Fr(a, b) + W]
                wr = [x for x in dict.fromkeys(wr) if x != right and x > 0 and x.denominator <= 40]
                q = f"{FR(a, b)} × {W} ="
            if len(wr) < 2: ok = False; break
            wr = rng.sample(wr, 2)
            if len({right, *wr}) < 3: ok = False; break
            rows.append(dict(q=q, opts=[FM(right), FM(wr[0]), FM(wr[1])], right=0, big=True)); qs.append(right)
        if ok and len({str(x) for x in qs}) == 6: break
    else: raise RuntimeError("p15")
    def solve_row(q, opts, qh):
        v = evaluate(q.replace("=", "").strip())
        ov = [evaluate(t) for t in opts]
        return ov.index(v)
    P = mc_page(15, 5115, "Big Products", 2, "Fractions: multiplying improper fractions and mixed numbers", STRAND_FR,
        "multiplying a proper fraction by an improper fraction, two improper fractions, a mixed number by a whole number", ["FR2.3", "FR2.4", "FR2.5"], "Lettered choices (fraction products)",
        ["Work out each product.", "Circle the letter of the right answer in each row.", "Write the six letters in the boxes."],
        rng, rows, 3, word, "; ".join(f"{i+1}) {frac_txt(x)}" for i, x in enumerate(qs)),
        "Six products: two improper fractions times each other (two rows), a proper fraction times an improper fraction, an improper fraction times a whole number and a mixed number times a whole number (two rows). The wrong choices are the usual slips (adding the denominators, adding the numerators, not multiplying the fraction part of a mixed number, or answers one whole or one half away). Each choice has a letter and the right choices spell the word. Every other way of choosing was tested against a very large word list. A box left blank gives no letter and the check cannot see it.",
        solve_row, ps=False)
    return P

# =============================================================================== P5-16 Remainder Stories (code word)
FRAMES16 = [("stickers", "Ali", "He", "gave {f1} of them to Ben and {f2} of the rest to Cara", "Ben", "Cara", "stickers"),
            ("sweets", "Mei", "She", "ate {f1} of them on Monday and {f2} of the rest on Tuesday", "Monday", "Tuesday", "sweets"),
            ("$", "Hana", "She", "spent {f1} of it on a book and {f2} of the rest on a pen", "book", "pen", "money"),
            ("cm", "Ravi", "He", "cut off {f1} of it, then {f2} of what was left", "", "", "ribbon"),
            ("pages", "Siti", "She", "read {f1} of the pages on Friday and {f2} of the rest on Saturday", "Friday", "Saturday", "pages"),
            ("marbles", "Kumar", "He", "lost {f1} of them and gave {f2} of the rest to his sister", "", "sister", "marbles")]

def story16(rng, frame, kind):
    th, name, he, act, x, y, what = frame
    while True:
        b = rng.choice([3, 4, 5, 6, 8]); a = rng.randint(1, b - 1)
        d = rng.choice([3, 4, 5, 6]); c = rng.randint(1, d - 1)
        if math.gcd(a, b) != 1 or math.gcd(c, d) != 1: continue
        k = rng.randint(2, 6); N = b * k
        R1 = N - a * k
        if R1 % d: continue
        N = N * (d // math.gcd(d, 1)) if False else N
        second = Fr(c, d) * R1; first = a * k
        if N > 200 or second.denominator != 1: continue
        break
    unit = "$" if th == "$" else ""
    nt = f"{unit}{N}" + ("" if th == "$" else (f" {th}" if th not in ("cm",) else " cm"))
    s1 = f"{name} had {nt}." if th != "cm" else f"{name} had a ribbon {N} cm long."
    s2 = f"{he} " + act.format(f1=FR(a, b), f2=FR(c, d)) + "."
    thing = {"stickers": "stickers", "sweets": "sweets", "$": "money", "cm": "ribbon", "pages": "pages", "marbles": "marbles"}[th]
    if kind == "left":
        q = {"$": f"How much money was left?", "cm": "How many cm of ribbon were left?"}.get(th, f"How many {thing} were left?"); ans = N - first - int(second)
    elif kind == "second":
        q = {"$": "How much money did she spend on the pen?", "cm": "How many cm were cut off the second time?"}.get(th, f"How many {thing} were taken the second time?"); ans = int(second)
    else:
        q = {"$": "How much money did she spend in all?", "cm": "How many cm were cut off in all?"}.get(th, f"How many {thing} were taken in all?"); ans = first + int(second)
    pool = [N - first, first, int(second), N - first - int(second), first + int(second), int(Fr(c, d) * N), N - int(Fr(c, d) * N)]
    return f"{s1} {s2} {q}", ans, pool, (N, a, b, c, d)

def solve16(t):
    """independent reader of a story: the start amount, the two fractions and what is asked"""
    fr = re.findall(r"⟨(\d+)\|(\d+)⟩", t)
    (a, b), (c, d) = [(int(x), int(y)) for x, y in fr]
    N = [int(x) for x in re.findall(r"\d+", re.sub(r"⟨[^⟩]*⟩", " ", t))][0]
    first = Fr(a, b) * N; rest = N - first; second = Fr(c, d) * rest
    last = t.split("?")[0].split(".")[-1]
    if "left" in last: return int(rest - second)
    if "in all" in last: return int(first + second)
    return int(second)

def page16():
    rng = random.Random(5116)
    kinds = ["left", "second", "total", "left", "second", "total"]
    for _ in range(4000):
        frames = rng.sample(FRAMES16, 6); ks = kinds[:]; rng.shuffle(ks)
        sts = [story16(rng, f, k) for f, k in zip(frames, ks)]
        ans = [s[1] for s in sts]
        if not distinct(ans) or max(ans) > 200 or min(ans) < 3: continue
        pool = [p for s in sts for p in s[2]]
        pool = [Fr(p) for p in dict.fromkeys(pool) if p not in ans and p > 0]
        pool = [int(p) for p in pool]
        res = code_table_for(16, ans, rng, pool, n_decoy=2, tries=60)
        if res[0]: (word, table), dom = res; break
    else: raise RuntimeError("p16")
    cards = [qc(i + 1, f'<p class="qt">{s[0]}</p>', abx("w4") + ('<span class="unit">cm</span>' if "cm" in s[0].split("?")[0][-30:] else ""), cls="inl") for i, s in enumerate(sts)]
    solved = []
    for c in cards:
        t = to_text(re.search(r'<div class="qt">(.*?)</div></div><div class="qa">', c, re.S).group(1))
        solved.append(solve16(t))
    P = code_page(16, 5116, "Remainder Stories", 2, "Fractions: a fraction of the remainder", STRAND_FR,
        "multiplying a fraction by a whole number: a fraction of a quantity, then a fraction of what is left", ["FR2.2", "FR2.3"], "Code-breaker (two-step fraction stories)",
        ["Read each story.", "Take the fraction of the whole, then the fraction of the rest.", "Write the answer in the box. Use the code table."],
        cards, ans, word, table, dom, lambda k: num(int(k)), "; ".join(f"{i+1}) {a}" for i, a in enumerate(ans)),
        "Six two-step stories. The pupil takes a fraction of the starting amount, then a fraction of what is left, and answers one of three questions: what is left, what was taken the second time, or what was taken in all. The decoy letters stand for the usual slips: taking the second fraction of the whole instead of the rest, or answering a different one of the three questions. Every step divides exactly. A box left blank gives no letter and the check cannot see it.",
        solved, cols=4, layout="c1", ps=True, checks=[("V7 starting amounts up to 200, every step a whole number", all(s[3][0] <= 200 for s in sts), "")])
    return P

# =============================================================================== P5-17 Point Shift (code word)
def page17():
    rng = random.Random(5117)
    for _ in range(8000):
        items = []
        for k in range(6):
            p = rng.choice([10, 100, 1000]); op = rng.choice(["×", "÷"])
            places = rng.choice([0, 1, 2, 3]) if op == "×" else rng.choice([0, 1, 2])
            x = Fr(rng.randint(2, 999), 10 ** places) if places else Fr(rng.randint(2, 99))
            if op == "÷":
                v = x / p
                if len(dec(v).partition(".")[2]) > 3: break
            else: v = x * p
            if x.denominator == 1 and op == "×": break
            items.append((x, op, p, v))
        else:
            ans = [v for *_, v in items]
            if not distinct(ans) or len({it[1] for it in items}) < 2 or any(len(dec(a).partition(".")[2]) > 3 for a in ans): continue
            pool = []
            for x, op, p, v in items:
                pool += [v * 10, v / 10, v * 100 if v < 1000 else v / 100, v / 100, x * p if op == "÷" else x / p]
            pool = [q for q in dict.fromkeys(pool) if q not in ans and q > 0 and len(dec(q).partition(".")[2]) <= 3]
            res = code_table_for(17, ans, rng, pool, n_decoy=3, tries=60)
            if res[0]: (word, table), dom = res; break
    else: raise RuntimeError("p17")
    cards = [qc(i + 1, f'<p class="qt big">{dec(x)} {op} {num(p)} =</p>', abx("w4")) for i, (x, op, p, v) in enumerate(items)]
    solved = []
    for c in cards:
        t = to_text(re.search(r'<div class="qt">(.*?)</div></div><div class="qa">', c, re.S).group(1)).rstrip("= ").strip()
        solved.append(evaluate(t))
    P = code_page(17, 5117, "Point Shift", 1, "Decimals: multiplying and dividing by 10, 100 and 1000", STRAND_DE,
        "multiplying and dividing decimals (up to 3 decimal places) by 10, 100 and 1000", ["DE1.1"], "Code-breaker (decimal point shifts)",
        ["Work out each answer.", "Write it in the box.", "Use the code table."],
        cards, ans, word, table, dom, lambda k: dec(k), "; ".join(f"{i+1}) {dec(a)}" for i, a in enumerate(ans)),
        "Six calculations: a whole number or a decimal of up to three places multiplied or divided by 10, 100 or 1000. No answer has more than three decimal places. The decoy letters stand for the usual slips: the decimal point moved one place too many or too few, or moved the wrong way. A box left blank gives no letter and the check cannot see it.",
        solved, cols=3, layout="c2", checks=[("V7 every number has at most 3 decimal places", all(len(dec(v).partition(".")[2]) <= 3 and len(dec(x).partition(".")[2]) <= 3 for x, op, p, v in items), "")])
    return P

# =============================================================================== P5-18 True or False Decimals (lettered choices, two choices)
def statement18(rng, true):
    kind = rng.choice(["x10", "d10", "xm", "dm"])
    if kind in ("x10", "d10"):
        p = rng.choice([10, 100, 1000])
        x = Fr(rng.randint(2, 999), 10 ** rng.choice([0, 1, 2, 3]))
        if x.denominator == 1 and kind == "x10": x = Fr(rng.randint(2, 99), 10 ** rng.choice([1, 2]))
        if kind == "x10":
            v = x * p; op = "×"
        else:
            x = Fr(rng.randint(2, 999), 10 ** rng.choice([0, 1])); v = x / p; op = "÷"
            if len(dec(v).partition(".")[2]) > 3: return None
        shown = v if true else rng.choice([v * 10, v / 10, v * 100, v / 100])
        if shown == v and not true: return None
        if len(dec(shown).partition(".")[2]) > 4: return None
        return f"{dec(x)} {op} {num(p)} = {dec(shown)}", shown == v
    m = rng.choice([20, 30, 40, 50, 60, 200, 300, 400, 500, 600, 2000, 3000])
    if kind == "xm":
        x = Fr(rng.randint(2, 99), 10 ** rng.choice([1, 2])); v = x * m; op = "×"
    else:
        v = Fr(rng.randint(2, 99), 10 ** rng.choice([1, 2])); x = v * m; op = "÷"
        if x.denominator != 1 and len(dec(x).partition(".")[2]) > 2: return None
    if len(dec(v).partition(".")[2]) > 3: return None
    shown = v if true else rng.choice([v * 10, v / 10, v * 2 if v * 2 != v else v + 1])
    if shown == v and not true: return None
    if len(dec(shown).partition(".")[2]) > 4: return None
    return f"{dec(x)} {op} {num(m)} = {dec(shown)}", shown == v

def page18():
    rng = random.Random(5118)
    for _ in range(4000):
        word = word_candidates(18, 6)[0]
        truths = [rng.random() < .5 for _ in range(6)]
        if not 2 <= sum(truths) <= 4: continue
        sts = [statement18(rng, t) for t in truths]
        if any(s is None for s in sts) or len({s[0] for s in sts}) < 6 or [s[1] for s in sts] != truths: continue
        if sum(1 for s in sts if re.search(r"× \d{2,}0 |÷ \d{2,}0 ", s[0]) and not re.search(r"[×÷] (10|100|1000) ", s[0])) < 2: continue
        break
    else: raise RuntimeError("p18")
    rows = [dict(q=f'<span class="qs">{t}</span>', opts=["T", "F"], right=0 if tr else 1, fixed=True, big=True) for t, tr in sts]
    def solve_row(q, opts, qh):
        lhs, rhs = q.split("=")
        return 0 if evaluate(lhs) == evaluate(rhs) else 1
    P = mc_page(18, 5118, "True or False", 2, "Decimals: multiplying and dividing by 10, 100, 1000 and their multiples", STRAND_DE,
        "multiplying and dividing decimals by 10, 100, 1000 and their multiples", ["DE1.1"], "True or false table",
        ["Is each statement true or false?", "Circle the letter of the right choice in each row.", "Write the six letters in the boxes."],
        rng, rows, 2, word, "; ".join(f"{i+1}) {'T' if tr else 'F'} ({t})" for i, (t, tr) in enumerate(sts)),
        "Six statements with decimals multiplied or divided by 10, 100, 1000 or a multiple such as 20, 300 or 2000. Each row has a T choice and an F choice with a letter. The false statements are the usual slips (the decimal point one place out, or the wrong number of zeros). The letters of the right choices spell the word. Every other way of choosing was tested against a very large word list. A box left blank gives no letter and the check cannot see it.",
        solve_row, rows_cls="tfrows")
    return P

# =============================================================================== P5-19 Measures in Decimals (lettered choices)
UN = {"km": ("m", 1000), "m": ("cm", 100), "kg": ("g", 1000), "ℓ": ("mℓ", 1000)}
def page19():
    rng = random.Random(5119)
    for _ in range(4000):
        word = word_candidates(19, 6)[0]
        us = rng.sample(list(UN), 4) + rng.sample(list(UN), 2)
        rows = []; keys = []
        for i, big in enumerate(us):
            small, f = UN[big]
            if i < 3:
                w = rng.randint(1, 9); r = rng.choice([x for x in range(1, f) if x % (5 if f == 1000 else 1) == 0 and x % 10 != 0 or (f == 100 and x % 5 == 0)])
                r = rng.choice([x for x in range(1, f) if not (f == 1000 and x % 10 == 0 and rng.random() < .5)])
                val = Fr(w) + Fr(r, f)
                right = dec(val)
                wrong = [dec(Fr(w) + Fr(r, f // 10 if f // 10 else 1)), dec(Fr(w) + Fr(r, 10 ** len(str(r)))), dec(Fr(w * 10) + Fr(r, f))]
                wrong = [x for x in dict.fromkeys(wrong) if x != right]
                if len(wrong) < 2: break
                rows.append(dict(q=f"{w} {big} {r} {small} = ___ {big}", opts=[right] + rng.sample(wrong, 2), big=True)); keys.append(f"{right} {big}")
            else:
                d = rng.choice([1, 2, 3]) if f == 1000 else rng.choice([1, 2])
                val = Fr(rng.randint(11, 999), 10 ** d) if rng.random() < .6 else Fr(rng.randint(2, 99), 10 ** d)
                right_v = val * f
                if right_v.denominator != 1: break
                wrong = [right_v * 10, right_v / 10, right_v * 100 if right_v < 10000 else right_v / 100]
                wrong = [x for x in dict.fromkeys(wrong) if x != right_v and x.denominator == 1 and x >= 1]
                if len(wrong) < 2: break
                rows.append(dict(q=f"{dec(val)} {big} = ___ {small}", opts=[num(int(right_v))] + [num(int(x)) for x in rng.sample(wrong, 2)], big=True)); keys.append(f"{num(int(right_v))} {small}")
        else:
            if len({r["q"] for r in rows}) == 6: break
    else: raise RuntimeError("p19")
    def solve_row(q, opts, qh):
        q = q.replace(NB, "")
        m = re.fullmatch(r"(\d+) (km|m|kg|ℓ) (\d+) (m|cm|g|mℓ) = ___ (km|m|kg|ℓ)", q)
        if m:
            w, big, r, small, tgt = m.groups(); f = {"m": 1000, "cm": 100, "g": 1000, "mℓ": 1000}[small]
            if big == "km" and small != "m" or big == "m" and small != "cm": pass
            v = Fr(int(w)) + Fr(int(r), f)
            return [evaluate(t) for t in opts].index(v)
        m = re.fullmatch(r"([\d.]+) (km|m|kg|ℓ) = ___ (m|cm|g|mℓ)", q)
        big, small = m.group(2), m.group(3)
        f = {"km": 1000, "m": 100, "kg": 1000, "ℓ": 1000}[big]
        v = evaluate(m.group(1)) * f
        return [evaluate(t) for t in opts].index(v)
    P = mc_page(19, 5119, "Measures in Decimals", 1, "Decimals: converting measures to a larger or smaller unit", STRAND_DE,
        "converting a measure to a larger or smaller unit in decimal form (km and m, m and cm, kg and g, ℓ and mℓ)", ["DE1.2"], "Lettered choices (units)",
        ["Change each measure to the unit shown.", "Circle the letter of the right choice in each row.", "Write the six letters in the boxes."],
        rng, rows, 3, word, "; ".join(f"{i+1}) {k}" for i, k in enumerate(keys)),
        "Six conversions in km and m, m and cm, kg and g, and ℓ and mℓ: three from two units to a decimal in the larger unit and three from a decimal to the smaller unit. The wrong choices are the usual slips (the point one or two places out, the digits of the smaller unit put in the wrong places). Each choice has a letter and the right choices spell the word. Every other way of choosing was tested against a very large word list. A box left blank gives no letter and the check cannot see it.",
        solve_row)
    return P

# =============================================================================== P5-20 Unit Switch (code word)
def page20():
    rng = random.Random(5120)
    T20 = [("A bottle holds {x} ℓ. How many mℓ do {k} bottles hold?", "mℓ"),
           ("A rope is {x} m long. {y} cm is cut off. How many cm of rope are left?", "cm"),
           ("Ali walks {x} km to school and {y} m more to the shop. How many metres is that in all?", "m"),
           ("{k} packets of rice weigh {x} kg each. What is the total mass in g?", "g"),
           ("A jug holds {x} ℓ of juice. {y} mℓ is poured out. How many mℓ are left?", "mℓ"),
           ("A ribbon {x} m long is cut into {k} equal pieces. How many cm is each piece?", "cm")]
    for _ in range(6000):
        items = []; ans = []
        for t, u in T20:
            if t.startswith("A bottle"):
                x = Fr(rng.randint(11, 99), 100) if rng.random() < .5 else Fr(rng.randint(101, 999), 1000); k = rng.randint(3, 9); v = x * 1000 * k; items.append((t.format(x=dec(x), k=k), u)); ans.append(v)
            elif t.startswith("A rope"):
                x = Fr(rng.randint(21, 99), 10) if rng.random() < .5 else Fr(rng.randint(201, 499), 100); y = rng.randint(15, 190); v = x * 100 - y; items.append((t.format(x=dec(x), y=y), u)); ans.append(v)
            elif t.startswith("Ali"):
                x = Fr(rng.randint(11, 99), 10) if rng.random() < .5 else Fr(rng.randint(101, 499), 100); y = rng.randint(120, 950); v = x * 1000 + y; items.append((t.format(x=dec(x), y=y), u)); ans.append(v)
            elif t.startswith("{k} packets"):
                x = Fr(rng.randint(11, 99), 100) if rng.random() < .5 else Fr(rng.randint(101, 499), 1000); k = rng.randint(3, 9); v = x * 1000 * k; items.append((t.format(x=dec(x), k=k), u)); ans.append(v)
            elif t.startswith("A jug"):
                x = Fr(rng.randint(11, 29), 10) if rng.random() < .5 else Fr(rng.randint(101, 299), 100); y = rng.randint(120, 950); v = x * 1000 - y; items.append((t.format(x=dec(x), y=y), u)); ans.append(v)
            else:
                k = rng.choice([2, 3, 4, 5, 6, 8]); x = Fr(rng.randint(2, 9) * k * rng.randint(1, 9), 10) if False else Fr(k * rng.randint(11, 59), 100) ; v = x * 100 / k; items.append((t.format(x=dec(x), k=k), u)); ans.append(v)
        if any(a.denominator != 1 or a <= 0 or a > 9999 for a in ans) or not distinct(ans): continue
        pool = []
        for a, (t, u) in zip(ans, items): pool += [a * 10, a / 10, a * 100 if a < 100 else a / 100]
        pool = [Fr(p) for p in dict.fromkeys(pool) if p not in ans and p.denominator == 1 and p > 0]
        res = code_table_for(20, ans, rng, pool, n_decoy=2, tries=60)
        if res[0]: (word, table), dom = res; break
    else: raise RuntimeError("p20")
    cards = [qc(i + 1, f'<p class="qt">{t}</p>', abx("w4") + f'<span class="unit">{u}</span>') for i, (t, u) in enumerate(items)]
    def solve(t):
        t = t.replace(NB, "")
        nums = [evaluate(x) for x in re.findall(r"\d+(?:\.\d+)?", t)]
        if t.startswith("A bottle"): return nums[0] * 1000 * nums[1]
        if t.startswith("A rope"): return nums[0] * 100 - nums[1]
        if t.startswith("Ali"): return nums[0] * 1000 + nums[1]
        if "packets" in t: return nums[1] * 1000 * nums[0]
        if t.startswith("A jug"): return nums[0] * 1000 - nums[1]
        return nums[0] * 100 / nums[1]
    solved = [solve(to_text(re.search(r'<div class="qt">(.*?)</div></div><div class="qa">', c, re.S).group(1))) for c in cards]
    P = code_page(20, 5120, "Unit Switch", 2, "Decimals: converting measures and solving problems", STRAND_DE,
        "converting a measure to a larger or smaller unit in decimal form, then solving a short problem", ["DE1.2"], "Code-breaker (measures in stories)",
        ["Read each story.", "Change the unit, then work out the answer in the unit shown.", "Use the code table."],
        cards, ans, word, table, dom, lambda k: num(int(k)), "; ".join(f"{i+1}) {num(int(a))} {u}" for i, (a, (t, u)) in enumerate(zip(ans, items))),
        "Six short stories with decimal measures (ℓ, m, km, kg): the pupil changes one measure to the smaller unit and then multiplies, adds, subtracts or divides. The decoy letters stand for the usual slips: the unit changed by the wrong power of ten. All answers are whole numbers of the unit shown. A box left blank gives no letter and the check cannot see it.",
        solved, cols=4, layout="c2", ps=True)
    return P

PAGES = [page14, page15, page16, page17, page18, page19, page20]
