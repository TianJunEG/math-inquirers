"""Semester 2, part A (percentage and rate): P5-21 How Many Percent?; P5-23 Sale Prices; P5-24 GST Match; P5-25 Annual Interest; P5-26 Rate Cards; P5-27 Rate Stories.
(P5-22 is a colour-by-code page, in pages_cbc.py.)"""
import random, re, math, itertools
from fractions import Fraction as Fr
from decimal import Decimal
from .common import *
from .kit import *
from .kit5 import *
from .art5 import *

PEOPLE = [("Ali", "He"), ("Mei", "She"), ("Siti", "She"), ("Ben", "He"), ("Kumar", "He"), ("Hana", "She"), ("Wei", "He"), ("Ravi", "He"), ("Lily", "She"), ("Aisha", "She")]

def pct(n): return f"{n}%"
def terminating(v):
    d = Fr(v).denominator
    while d % 2 == 0: d //= 2
    while d % 5 == 0: d //= 5
    return d == 1
def money_val(t):
    return Fr(Decimal(t.replace("$", "").replace(NB, "").replace(",", "")))

# =============================================================================== P5-21 How Many Percent? (code word)
def bar_svg(parts, shaded, w=72, hh=11):
    pw = (w - 2) / parts; o = []
    for k in range(parts):
        x = 1 + k * pw
        if k < shaded: o.append(f'<rect class="pt sh" x="{x:.2f}" y="1.5" width="{pw:.2f}" height="{hh - 3}" fill="#000" stroke="#fff" stroke-width="0.9"/>')
        else: o.append(f'<rect class="pt" x="{x:.2f}" y="1.5" width="{pw:.2f}" height="{hh - 3}" fill="#fff" stroke="#000" stroke-width="0.5"/>')
    o.append(f'<rect x="1" y="1.5" width="{w - 2}" height="{hh - 3}" fill="none" stroke="#000" stroke-width="0.7"/>')
    return svg(w, hh, "".join(o), cls="fsvg", extra='data-fig="bar"')

def read_bar(h):
    return len(re.findall(r'class="pt sh"', h)), len(re.findall(r'class="pt', h))

def page21():
    rng = random.Random(5121)
    TX = ["{k} out of {n} pupils walk to school. What percentage of the pupils walk to school?",
          "A box has {n} pens. {k} of them are blue. What percentage of the pens are blue?"]
    for _ in range(8000):
        items = []
        bar_ns = [10, 20, 25, rng.choice([10, 20, 25])]; rng.shuffle(bar_ns)
        for kd in ["bar", "bar", "bar", "bar", "txt", "txt"]:
            if kd == "bar":
                n = bar_ns.pop(); k = rng.randint(1, n - 1)
            else:
                n = rng.choice([20, 25, 40, 50, 200 // 4]); k = rng.randint(2, n - 1)
                if (k * 100) % n: continue
            items.append((kd, n, k, k * 100 // n if (k * 100) % n == 0 else None))
        if len(items) < 6 or any(it[3] is None for it in items): continue
        ans = [Fr(it[3]) for it in items]
        if not distinct(ans): continue
        if sum(1 for it in items if it[1] == 25) > 2 or len({it[1] for it in items if it[0] == 'bar'}) < 3: continue
        pool = []
        for kd, n, k, a in items: pool += [Fr(k), Fr(100 - a), Fr(n - k), Fr(a + 10), Fr(a - 10) if a > 10 else Fr(a + 5), Fr(a * 2)]
        pool = [p for p in dict.fromkeys(pool) if p not in ans and 0 < p <= 100]
        res = code_table_for(21, ans, rng, pool, n_decoy=3, tries=60)
        if res[0]: (word, table), dom = res; break
    else: raise RuntimeError("p21")
    cards = []; ti = 0
    for i, (kd, n, k, a) in enumerate(items):
        if kd == "bar": cards.append(qc(i + 1, f'<p class="qt">What percentage is shaded?</p>{bar_svg(n, k)}', abx("w4") + '<span class="unit">%</span>'))
        else:
            cards.append(qc(i + 1, '<p class="qt">' + TX[ti % 2].format(k=k, n=n) + "</p>", abx("w4") + '<span class="unit">%</span>')); ti += 1
    solved = []
    for c in cards:
        body = re.search(r'<div class="qt">(.*?)</div></div><div class="qa">', c, re.S).group(1)
        if "<svg" in body: sh, tot = read_bar(body); solved.append(Fr(sh * 100, tot))
        else:
            nums = [int(x) for x in re.findall(r"\d+", to_text(body))]; solved.append(Fr(nums[0] * 100, nums[1]) if "out of" in body else Fr(nums[1] * 100, nums[0]))
    # in the box-of-pens story the total comes first
    P = code_page(21, 5121, "How Many Percent?", 1, "Percentage: a part of a whole as a percentage", STRAND_PC,
        "expressing a part of a whole as a percentage; the sign %", ["PC.PART"], "Code-breaker (percentages)",
        ["Find the percentage in each question.", "Write it in the box.", "Use the code table."],
        cards, ans, word, table, dom, lambda k: pct(int(k)), "; ".join(f"{i+1}) {int(a)}%" for i, a in enumerate(ans)),
        "Six questions: four bars divided into equal parts with some parts shaded, and two stories with a part and a whole. The pupil writes the part of the whole as a percentage. The decoy letters stand for the usual slips: giving the number of shaded parts, giving the percentage not shaded, or giving the number of parts left over. A box left blank gives no letter and the check cannot see it.",
        solved, cols=3, layout="c2", checks=[("V7 every answer is a whole percentage from 1 to 99", all(a.denominator == 1 and 1 <= a <= 99 for a in ans), "")])
    return P

# =============================================================================== P5-23 Sale Prices (ordering)
def page23():
    rng = random.Random(5123)
    for _ in range(8000):
        word = word_candidates(23, 6)[0]
        cards = []
        for k in range(6):
            p = rng.choice([20, 30, 40, 50, 60, 80, 100, 120, 150, 200, 250]); d = rng.choice([5, 10, 15, 20, 25, 30, 40, 50, 60, 75])
            v = Fr(p) * (100 - d) / 100
            if v.denominator not in (1, 2): break
            cards.append((f"Price: ${p}<br>Discount: {d}%", v))
        else:
            vs = [c[1] for c in cards]
            if len(set(vs)) == 6 and len({c[0].split("<br>")[1] for c in cards}) == 6 and cards != sorted(cards, key=lambda c: c[1]): break
    else: raise RuntimeError("p23")
    def solve(t):
        m = re.fullmatch(r"Price: \$(\d+) Discount: (\d+)%", t)
        return Fr(int(m.group(1))) - Fr(int(m.group(1)) * int(m.group(2)), 100)
    P = order_page(23, 5123, "Sale Prices", 2, "Percentage: finding the discount and the sale price", STRAND_PC,
        "finding discount and the price after discount", ["PC1.4", "PC.OF"], "Ordering (lettered cards)",
        ["Work out the sale price of each item.", "Put the sale prices in order, smallest first.", "Write the card letters in the boxes below."],
        rng, cards, word, True, "Order (smallest sale price first): " + ", ".join(f"{c[0].replace('<br>', ' ')} -> {money(c[1])}" for c in sorted(cards, key=lambda c: c[1])),
        "Six price tags, each with an original price and a percentage discount. The pupil finds the discount, takes it off the price and puts the six sale prices in order from smallest to greatest. The cards are not in order of sale price. The letters, read in that order, spell a word with exactly one arrangement that is a word, so no wrong order spells a word. A box left blank gives no letter and the check cannot see it.",
        solve, cols=2, work=True, ps=False)
    return P

# =============================================================================== P5-24 GST Match (matching)
def page24():
    rng = random.Random(5124)
    for _ in range(5000):
        word = word_candidates(24, 6)[0]
        prices = rng.sample(range(20, 205, 5), 6)
        vals = [Fr(p) * 109 / 100 for p in prices]
        if len(set(vals)) == 6: break
    order = sorted(range(6), key=lambda k: vals[k])
    pairs = [(f"Before GST: ${prices[k]}", f"With GST: ${float(vals[k]):.2f}") for k in order]
    def sl(t):
        m = re.fullmatch(r"Before GST: \$(\d+)", t); return Fr(int(m.group(1))) * 109 / 100
    def sr(t):
        m = re.fullmatch(r"With GST: \$([\d.]+)", t); return Fr(Decimal(m.group(1)))
    P = match_page(24, 5124, "GST Match", 2, "Percentage: GST", STRAND_PC,
        "finding GST and the price with GST", ["PC1.4", "PC.OF"], "Matching (lettered cards)",
        ["GST is 9% of the price before GST.", "Work out the price with GST for each card.", "Write the card's letter in the box under the matching tile."],
        rng, pairs, word, "; ".join(f"{w}: {a} -> {b}" for w, (a, b) in zip(word, pairs)),
        "Six cards with a price before GST (multiples of $5) and six tiles with the price with 9% GST, in order of size. The pupil finds 9% of the price, adds it, and matches the card with the tile. The letters, read from tile 1 to tile 6, spell a word with exactly one arrangement that is a word, so no wrong matching spells a word. GST is 9%; the page states the rate. A box left blank gives no letter and the check cannot see it.",
        sl, sr, left_title="Cards")
    return P

# =============================================================================== P5-25 Annual Interest (code word)
def page25():
    rng = random.Random(5125)
    T25 = "{nm} saves ${P} in a bank. The bank pays {r}% interest at the end of each year. {q}"
    Q = {"I1": "How much interest does {he} get after 1 year?", "T1": "How much money is in the bank after 1 year?", "In": "How much interest does {he} get after {n} years?", "Tn": "How much money is in the bank after {n} years?"}
    for _ in range(8000):
        kinds = ["I1", "T1", "In", "Tn", "I1", "In"]; rng.shuffle(kinds)
        names = rng.sample(PEOPLE, 6); items = []; ans = []
        for kd, (nm, he) in zip(kinds, names):
            P_ = rng.choice([200, 400, 500, 600, 800, 1000, 1200, 1500, 2000]); r = rng.choice([1, 2, 3, 4, 5, Fr(3, 2), Fr(5, 2)])
            n = rng.choice([2, 3, 4]) if kd in ("In", "Tn") else 1
            yr = Fr(P_) * Fr(r) / 100
            if yr.denominator != 1: break
            v = yr * n + (P_ if kd in ("T1", "Tn") else 0)
            items.append((T25.format(nm=nm, P=num(P_), r=dec(Fr(r)), q=Q[kd].format(he=he.lower(), n=n)), v, (kd, P_, Fr(r), n))); ans.append(v)
        else:
            if not distinct(ans) or max(ans) > 9999: continue
            pool = []
            for it in items:
                kd, P_, r, n = it[2]; yr = P_ * r / 100
                pool += [yr, yr * n, P_ + yr, P_ + yr * n, yr * (n + 1), P_ * (1 + r / 100) ** n if n > 1 else yr * 2, P_ - yr]
            pool = [Fr(p) for p in dict.fromkeys(pool) if p not in ans and Fr(p).denominator == 1 and p > 0]
            res = code_table_for(25, ans, rng, pool, n_decoy=2, tries=60)
            if res[0]: (word, table), dom = res; break
    else: raise RuntimeError("p25")
    cards = [qc(i + 1, f'<p class="qt">{t}</p>', '<span class="unit">$</span>' + abx("w4"), cls="inl") for i, (t, v, _) in enumerate(items)]
    def solve(t):
        t = t.replace(NB, "")
        P_ = int(re.search(r"saves \$(\d+)", t).group(1)); r = Fr(Decimal(re.search(r"pays ([\d.]+)%", t).group(1)))
        q = t.split("each year.")[1]
        n = int(re.search(r"after (\d+) years?", q).group(1))
        yr = P_ * r / 100
        return yr * n + (P_ if "money" in q else 0)
    solved = [solve(to_text(re.search(r'<div class="qt">(.*?)</div></div><div class="qa">', c, re.S).group(1))) for c in cards]
    P = code_page(25, 5125, "Annual Interest", 2, "Percentage: annual interest", STRAND_PC,
        "finding annual interest", ["PC1.4", "PC.OF"], "Code-breaker (interest in money stories)",
        ["Read each story.", "The interest is the same each year: the percentage of the money first saved.", "Write the answer in dollars. Use the code table."],
        cards, ans, word, table, dom, lambda k: money(k), "; ".join(f"{i+1}) ${int(a)}" for i, a in enumerate(ans)),
        "Six savings stories with a percentage interest paid at the end of each year, in whole dollars. The interest is a percentage of the first amount saved and is the same every year (the page says so); the pupil finds the interest for one year or several, or the money in the bank. The decoy letters stand for the usual slips: giving the interest when the total is asked, the total when the interest is asked, or the interest for one year too many or too few. Interest on interest (compound interest) is not used. A box left blank gives no letter and the check cannot see it.",
        solved, cols=4, layout="c1", ps=True, checks=[("V7 every amount a whole number of dollars", all(Fr(a).denominator == 1 for a in ans), "")])
    return P

# =============================================================================== P5-26 Rate Cards (lettered choices)
def page26():
    rng = random.Random(5126)
    for _ in range(6000):
        word = word_candidates(26, 6)[0]
        rows = []; keys = []; seen = {"rate": 0, "total": 0, "units": 0}
        for kd in ["rate", "total", "units", "rate", "total", "units"]:
            var = seen[kd]; seen[kd] += 1
            if kd == "rate":
                b = rng.choice([3, 4, 5, 6, 8]); a = b * rng.randint(3, 12)
                tmpl = [("A tap fills {a} ℓ of water in {b} minutes. How many ℓ does it fill in 1 minute?", "ℓ"), ("A worker packs {a} boxes in {b} hours. How many boxes does the worker pack in 1 hour?", "boxes")][var]
                q = tmpl[0].format(a=a, b=b); right = Fr(a, b); wrong = [Fr(b, a), Fr(a * b), Fr(a - b)]; u = tmpl[1]; fmt = lambda v: dec(v)
            elif kd == "total":
                if var == 0:
                    p = Fr(rng.choice([120, 150, 180, 240, 250, 320, 450]), 100); n = rng.randint(4, 9)
                    q = f"A pen costs ${dec(p, 2)}. How much do {n} pens cost?"; right = p * n; wrong = [p / n, p + n, right + 1]; u = ""; fmt = lambda v: "$" + dec(Fr(v), 2)
                else:
                    r = rng.randint(4, 9); m = rng.randint(6, 15)
                    q = f"Water flows from a pipe at {r} ℓ a minute. How many ℓ flow in {m} minutes?"; right = Fr(r * m); wrong = [Fr(m, r) if m % r == 0 else Fr(r + m), Fr(r * m + r), Fr(r * m - m)]; u = "ℓ"; fmt = lambda v: dec(v)
            else:
                if var == 0:
                    a = rng.choice([6, 8, 9, 12, 15, 20]); n = rng.randint(3, 9)
                    q = f"A machine makes {a} toys in 1 hour. How many hours does it take to make {a * n} toys?"; right = Fr(n); wrong = [Fr(a * a * n), Fr(a * n - a), Fr(n + a)]; u = "hours"; fmt = lambda v: dec(v)
                else:
                    p = rng.choice([2, 3, 4, 5, 6]); n = rng.randint(3, 9)
                    q = f"Rice costs ${p} for 1 kg. Mei has ${p * n}. How many kg can she buy?"; right = Fr(n); wrong = [Fr(p * p * n), Fr(p * n - p), Fr(n + p)]; u = "kg"; fmt = lambda v: dec(v)
            wrong = [w for w in dict.fromkeys(wrong) if w != right and w > 0 and terminating(w)]
            if len(wrong) < 2: break
            wrong = rng.sample(wrong, 2)
            rows.append(dict(q=q, opts=[fmt(right) + (" " + u if u else ""), fmt(wrong[0]) + (" " + u if u else ""), fmt(wrong[1]) + (" " + u if u else "")], wide=True)); keys.append(fmt(right) + (" " + u if u else ""))
        else:
            if len({r["q"] for r in rows}) == 6: break
    else: raise RuntimeError("p26")
    def solve_row(q, opts, qh):
        n = [Fr(Decimal(x)) for x in re.findall(r"\d+(?:\.\d+)?", q.replace(NB, ""))]
        if q.startswith("A tap") or q.startswith("A worker"): v = n[0] / n[1]
        elif q.startswith("A pen"): v = n[0] * n[1]
        elif q.startswith("Water"): v = n[0] * n[1]
        elif q.startswith("A machine"): v = n[2] / n[0]
        elif q.startswith("Rice"): v = n[2] / n[0]
        else: raise ValueError(q)
        ov = [Fr(Decimal(re.search(r"[\d.]+", t.replace(NB, "")).group(0))) for t in opts]
        return ov.index(v)
    P = mc_page(26, 5126, "Rate Cards", 1, "Rate: finding the rate, the total or the number of units", STRAND_RA,
        "rate as the amount of one quantity per unit of another quantity; finding the rate, the total or the number of units", ["RA"], "Lettered choices (rate)",
        ["Read each question.", "Circle the letter of the right answer in each row.", "Write the six letters in the boxes."],
        rng, rows, 3, word, "; ".join(f"{i+1}) {k}" for i, k in enumerate(keys)),
        "Six one-step rate questions: two ask for the rate (an amount for one unit), two for the total at a given rate and two for the number of units. The wrong choices are the usual slips (dividing the wrong way round, multiplying instead of dividing, adding or subtracting the two numbers). Each choice has a letter and the right choices spell the word. Every other way of choosing was tested against a very large word list. A box left blank gives no letter and the check cannot see it.",
        solve_row, ps=True)
    return P

# =============================================================================== P5-27 Rate Stories (code word)
def page27():
    rng = random.Random(5127)
    T27 = [("A tap fills {a} ℓ in {b} minutes. How many ℓ does it fill in {c} minutes?", "ℓ", lambda a, b, c: Fr(a, b) * c),
           ("A printer prints {a} pages in {b} minutes. How many minutes does it take to print {c} pages?", "min", lambda a, b, c: Fr(b, a) * c),
           ("{a} kg of rice cost ${b}. How much do {c} kg of rice cost?", "$", lambda a, b, c: Fr(b, a) * c),
           ("A machine makes {a} bolts in {b} hours. How many bolts does it make in {c} hours?", "bolts", lambda a, b, c: Fr(a, b) * c),
           ("A pump moves {a} ℓ of water in {b} minutes. How many minutes does it take to move {c} ℓ?", "min", lambda a, b, c: Fr(b, a) * c),
           ("Ali earns ${a} for {b} hours of work. How much does he earn for {c} hours?", "$", lambda a, b, c: Fr(a, b) * c)]
    for _ in range(8000):
        items = []; ans = []
        for t, u, f in T27:
            if t.startswith(("A printer", "A pump")):
                a = rng.randint(2, 9) * rng.choice([5, 6, 8, 10]); b = rng.randint(2, 9); c = a * rng.randint(2, 7)
                # time for c units: b * c / a
            elif t.startswith("{a} kg"):
                a = rng.randint(2, 9); b = rng.choice([5, 6, 8, 9, 10, 12]) * a // math.gcd(a, 1) // 1; c = rng.randint(3, 15)
            else:
                b = rng.randint(2, 9); a = b * rng.randint(3, 14); c = rng.randint(4, 15)
                if t.startswith("Ali"): a = b * rng.randint(4, 12)
            v = f(a, b, c)
            if v.denominator != 1 or a == b or c == a or c == b: break
            items.append((t.format(a=a, b=b, c=c), u)); ans.append(v)
        else:
            if not distinct(ans) or max(ans) > 999: continue
            pool = []
            for t, u in items:
                n = [int(x) for x in re.findall(r"\d+", t)]
                pool += [Fr(n[0], n[1]), Fr(n[1], n[0]), Fr(n[0] * n[2]), Fr(n[1] * n[2]), Fr(n[2], n[0]) if n[2] % n[0] == 0 else Fr(n[0] + n[2])]
            pool = [p for p in dict.fromkeys(pool) if p not in ans and p.denominator == 1 and p > 0]
            res = code_table_for(27, ans, rng, pool, n_decoy=2, tries=60)
            if res[0]: (word, table), dom = res; break
    else: raise RuntimeError("p27")
    cards = [qc(i + 1, f'<p class="qt">{t}</p>', abx("w4") + (f'<span class="unit">{u}</span>' if u != "$" else ""), cls="inl") for i, (t, u) in enumerate(items)]
    def solve(t):
        n = [int(x) for x in re.findall(r"\d+", t)]; a, b, c = n
        if t.startswith(("A printer", "A pump")): return Fr(b * c, a)
        if "kg of rice" in t: return Fr(b * c, a)
        return Fr(a * c, b)
    solved = [solve(to_text(re.search(r'<div class="qt">(.*?)</div></div><div class="qa">', c, re.S).group(1))) for c in cards]
    P = code_page(27, 5127, "Rate Stories", 2, "Rate: two-step problems", STRAND_RA,
        "rate: finding the rate, then the total or the number of units", ["RA"], "Code-breaker (rate stories)",
        ["Read each story.", "Find the amount for 1 unit, then answer the question.", "Write the answer in the box. Use the code table."],
        cards, ans, word, table, dom, lambda k: num(int(k)), "; ".join(f"{i+1}) {num(int(a))}{u if u != '$' else ' dollars'}" for i, (a, (t, u)) in enumerate(zip(ans, items))),
        "Six two-step rate stories: the pupil finds the rate for one unit (litres in one minute, price of one kilogram, pages in one minute) and then the total for a stated number of units, or the number of units for a stated total. All answers are whole numbers. The decoy letters stand for the usual slips: the rate turned upside down, or only the rate given. A box left blank gives no letter and the check cannot see it.",
        solved, cols=4, layout="c1", ps=True)
    return P

PAGES = [page21, page23, page24, page25, page26, page27]
