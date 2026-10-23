"""Wave A: Numbers up to 100 000 (P4-01 to P4-04; P4-05 is colour by code), factors and multiples (P4-06 to P4-09), multiplication (P4-10).
Each pageNN() makes the puzzle from a seed, re-solves it with separate solver code that reads the PRINTED html, and gives validate.py a `model`."""
import random, re, math, itertools
from .common import *
from .kit import *
from .kit4 import *

ABX = '<span class="ab w4"></span>'

def rand_digit_number(rng, lo=10000, hi=99999):
    """a 5-digit number whose digits are all different and not zero"""
    while True:
        n = rng.randint(lo, hi)
        if len(set(str(n))) == len(str(n)) and "0" not in str(n): return n

# =============================================================================== P4-01 Place Value
def pv_table(counts):
    heads = ["Ten thousands", "Thousands", "Hundreds", "Tens", "Ones"]
    return ('<table class="pvt4"><tr>' + "".join(f"<th>{h}</th>" for h in heads) + "</tr><tr>" + "".join(f"<td>{c}</td>" for c in counts) + "</tr></table>")

def page01():
    rng = random.Random(4101)
    for _ in range(4000):
        counts = [rng.randint(1, 8), rng.randint(10, 18), rng.randint(1, 9), rng.randint(0, 9), rng.randint(0, 9)]
        v1 = sum(c * 10 ** (4 - i) for i, c in enumerate(counts))
        n2 = rand_digit_number(rng); d2 = int(str(n2)[rng.choice([1, 2, 3])]); a2 = d2 * 10 ** (4 - str(n2).index(str(d2)))
        n3 = rng.randint(31, 98) * 100; a3 = n3 // 100
        n4 = rng.randint(21, 89) * 1000 + rng.randint(2, 8) * 100 + rng.randint(1, 9) * 10; a4 = n4 + 10000
        n5 = rand_digit_number(rng); d5 = int(str(n5)[0]); a5 = d5 * 10000
        parts = [rng.randint(2, 9) * 10000, rng.randint(1, 9) * 1000, rng.randint(1, 9) * 100, rng.randint(1, 9) * 10, rng.randint(1, 9)]
        sel = rng.sample(parts, 4); a6 = sum(sel); order = sel[:]; rng.shuffle(order)
        ans = [v1, a2, a3, a4, a5, a6]
        if not distinct(ans) or max(ans) > 99999 or order == sorted(order, reverse=True): continue
        pool = {v1 - 9000, v1 + 9000, v1 - 900, d2, d2 * 10, d2 * 100, d2 * 1000, a2 * 10 if a2 * 10 < 100000 else a2 // 10, n3 // 10, n3 // 1000,
                a4 - 9000, n4 + 1000, n4 + 100, d5, d5 * 1000, a5 // 10, a6 - 10000, a6 + 1000}
        pool = {p for p in pool if p not in ans and 0 <= p <= 99999}
        dom = plausible_domain(ans, pool, rng=rng, sample=150)
        res = code_table_any(1, 6, ans, rng, 0, 99999, n_decoy=3, tries=60, pool=sorted(pool), domain=dom)
        if res: word, table = res; break
    else: raise RuntimeError("p01")
    cards = [
        qcard(1, f'<p>Write the number shown in the chart.</p>{pv_table(counts)}', ABX, cls="span2 inl"),
        qcard(2, f"<p>In {N(n2)}, what is the value of the digit {d2}?</p>", ABX),
        qcard(3, f"<p>How many hundreds are in {N(n3)}?</p>", ABX),
        qcard(4, f"<p>What is 10{GAP}000 more than {N(n4)}?</p>", ABX),
        qcard(5, f"<p>What is the value of the digit {d5} in {N(n5)}?</p>", ABX),
        qcard(6, "<p>Write the number: " + " + ".join(N(x) for x in order) + "</p>", ABX, cls="span2 inl"),
    ]
    body = qgrid(cards, 2)
    P = code_page(1, 4101, "Place Value", 1, "Place value: ten thousands, thousands, hundreds, tens and ones", STRAND_NU,
        "1.1 (number notation, representations and place values), 1.2 (reading and writing numbers)", ["NU1.1", "NU1.2"], "Code-breaker (place value)",
        ["Work out each item.", "Write the number in the box.", INSTR_CODE], body, ans, table, word, 0, 99999,
        "1) chart: " + f"{counts[0]} ten thousands, {counts[1]} thousands, {counts[2]} hundreds, {counts[3]} tens, {counts[4]} ones = {Ntxt(v1)}; " + "; ".join(f"{i+2}) {Ntxt(a)}" for i, a in enumerate(ans[1:])),
        "A place-value chart whose thousands column holds more than 9 (regrouping), the value of a digit, the number of hundreds in a number, 10 000 more, the value of a digit in the ten-thousands place and the sum of four parts given in a mixed-up order. Decoy letters stand for slips such as giving the digit instead of its value, a wrong place, or forgetting to regroup. A box left blank gives no letter and the check cannot see it.",
        domain=dom)
    cs = strip_gap(body)
    solved = []
    tds = [int(x) for x in re.findall(r"<td>(\d+)</td>", cs)]
    solved.append(sum(c * 10 ** (4 - i) for i, c in enumerate(tds)))
    m = re.search(r"In (\d+), what is the value of the digit (\d)\?", cs); solved.append(int(m[2]) * 10 ** (len(m[1]) - 1 - m[1].index(m[2])))
    m = re.search(r"How many hundreds are in (\d+)\?", cs); solved.append(int(m[1]) // 100)
    m = re.search(r"What is 10000 more than (\d+)\?", cs); solved.append(10000 + int(m[1]))
    m = re.search(r"value of the digit (\d) in (\d+)\?", cs); solved.append(int(m[1]) * 10 ** (len(m[2]) - 1 - m[2].index(m[1])))
    m = re.search(r"Write the number: ([^<]*)</p>", cs); solved.append(sum(int(x) for x in m[1].split("+")))
    P.v("V1 independent solver (chart, digit values and parts read back from the printed cards) equals the key", solved == ans, solved)
    P.v("V7 every number is below 100 000", max(ans) < 100000 and n2 < 100000 and n5 < 100000)
    P.v("V1b the digit asked about appears once in its number", str(n2).count(str(d2)) == 1 and str(n5).count(str(d5)) == 1)
    return P

# =============================================================================== P4-02 Words and Numerals (matching cards)
ONES = "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split()
TENSW = "x x twenty thirty forty fifty sixty seventy eighty ninety".split()
def below100(n): return ONES[n] if n < 20 else TENSW[n // 10] + ("-" + ONES[n % 10] if n % 10 else "")
def below1000(n):
    h, r = divmod(n, 100)
    if h == 0: return below100(r)
    return ONES[h] + " hundred" + (" and " + below100(r) if r else "")
def words_of(n):
    """a number from 1000 to 99 999 in words, British style: forty-eight thousand, two hundred and six"""
    t, r = divmod(n, 1000)
    s = below1000(t) + " thousand"
    if r:
        s += (" and " + below100(r)) if r < 100 else (", " + below1000(r))
    return s

def num_from_words(s):
    """independent reader of a number written in words"""
    tot = 0; cur = 0
    for w in re.split(r"[\s,\-]+", s.lower()):
        if w in ("and", ""): continue
        if w in ONES: cur += ONES.index(w)
        elif w in TENSW and w != "x": cur += TENSW.index(w) * 10
        elif w == "hundred": cur *= 100
        elif w == "thousand": tot += cur * 1000; cur = 0
        else: raise ValueError(w)
    return tot + cur

def misreads(n):
    """numerals that a pupil could mistake for n: two neighbouring digits swapped, or a zero dropped"""
    s = str(n); out = set()
    for i in range(len(s) - 1):
        t = list(s); t[i], t[i + 1] = t[i + 1], t[i]
        if t[0] != "0": out.add(int("".join(t)))
    for i, ch in enumerate(s):
        if ch == "0": out.add(int(s[:i] + s[i + 1:]))
    return {x for x in out if x != n and 1000 <= x <= 99999}

def rand_wordy_number(rng):
    t = rng.randint(2, 98)
    r = rng.choice([lambda: rng.randint(1, 9), lambda: rng.randint(2, 9) * 10, lambda: rng.randint(11, 99), lambda: rng.randint(1, 9) * 100,
                    lambda: rng.randint(1, 9) * 100 + rng.randint(1, 9), lambda: rng.randint(1, 9) * 100 + rng.randint(2, 9) * 10, lambda: rng.randint(101, 999)])()
    return t * 1000 + r

def page02():
    rng = random.Random(4202)
    for _ in range(4000):
        word = word_candidates(2, 6)[rng.randrange(0, 4)]
        base = [rand_wordy_number(rng) for _ in range(6)]
        if not distinct(base): continue
        dec = []
        for n in rng.sample(base, 6):
            m = sorted(x for x in misreads(n) if x not in base and x not in dec)
            if m: dec.append(rng.choice(m))
            if len(dec) == 4: break
        if len(dec) < 4: continue
        try: letters_dec = letters_for_cards(rng, word, 4)
        except RuntimeError: continue
        CLAIMED[2] = word
        break
    cards = [(n, word[i]) for i, n in enumerate(base)] + [(n, letters_dec[i]) for i, n in enumerate(dec)]
    shown = cards[:]; rng.shuffle(shown)
    rows = "".join(f'<div class="wrow"><span class="no">{i+1}</span><span class="wtxt">{esc(words_of(n)).capitalize()}</span><span class="ab sm"></span></div>' for i, n in enumerate(base))
    cardsh = '<div class="ncards">' + "".join(f'<div class="ncard"><b>{N(n)}</b><i class="cl">{l}</i></div>' for n, l in shown) + "</div>"
    body = f'<div class="blk"><p class="lead">Number cards</p>{cardsh}</div><div class="blk"><p class="lead">Write the letter of the matching card.</p><div class="wrows">{rows}</div></div>'
    P = new_page(2, 4202, "Words and Numerals", 1, "Reading and writing numbers up to 100 000 in numerals and in words", STRAND_NU,
        "1.2 (reading and writing numbers in numerals and in words)", ["NU1.2"], "Matching (number words to numeral cards)",
        "K1 letters of the matching cards spell a word (6 letters), 4 decoy cards", ["Read each number in words.", "Find its numeral on a card.", "Write the letter of the card in the box."],
        body, "; ".join(f"{i+1}) {words_of(n)} = {Ntxt(n)} (card {word[i]})" for i, n in enumerate(base)), f"Word: {word}",
        "Six numbers written in words (thousands, hundreds, tens and ones, with a zero in the middle of some). Ten numeral cards are printed: six match, four are decoys made by swapping two digits or dropping a zero (the usual slips when a number in words is written as a numeral). The letters of the matching cards, read down the six rows, spell the word. A decoy card put in any row gives a letter that does not spell a word, and a swap of two rows does not either (all tested against a very large word list). The pupil writes a letter, not a number, so writing a number word as numerals by hand is not asked. A box left blank gives no letter and the check cannot see it.",
        check="Write the six letters in order. Do they spell a word?", check_boxes=6, mk=("code",), mech_plain="Word from the letters of the matching cards (6 letters)")
    cardl = {int(strip_gap(m[0])): m[1] for m in re.findall(r'<div class="ncard"><b>(.*?)</b><i class="cl">(\w)</i>', body)}
    wtxt = re.findall(r'<span class="wtxt">([^<]*)</span>', body)
    solved = "".join(cardl[num_from_words(w)] for w in wtxt)
    P.v("V1 independent solver (words converted to numbers and matched to the cards) gets the word", solved == word, solved)
    P.v("V3d the code word's letters have exactly ONE arrangement that is a word", anagrams(word) == [word.lower()])
    all_letters = sorted(set(word) | set(letters_dec))
    bad_single = [(i, c) for i in range(6) for c in all_letters if c != word[i] and (word[:i] + c + word[i + 1:]).lower() in BIG]
    P.v("V3 no single wrong card in any row spells a word (large word list)", not bad_single, bad_single[:3])
    bad_orders = no_wrong_order(word)
    P.v("V3e none of the 719 wrong orders of the six letters spells a word", not bad_orders, bad_orders[:3])
    P.v("V7 all numbers are between 1000 and 99 999; no decoy equals a right card", all(1000 <= n <= 99999 for n in base + dec) and not (set(dec) & set(base)))
    P.v("V8 every number in words reads back to its numeral", all(num_from_words(words_of(n)) == n for n in base))
    P["cv"] = dict(rate=1.0, single_total=6 * (len(all_letters) - 1), single_detected=6 * (len(all_letters) - 1))
    P["model"] = dict(truth=list(word), domains=[all_letters] * 6, check=letters_check(), perm=list(range(6)), numeric=False)
    P["facts"] = " ".join(str(n) for n in base + dec)
    return P

# =============================================================================== P4-03 Number Patterns
def seq_html(terms, blank):
    cells = ""
    for i, t in enumerate(terms):
        cells += '<span class="sq4 bl"><span class="ab w4"></span></span>' if i == blank else f'<span class="sq4">{N(t)}</span>'
    return f'<div class="seq4">{cells}</div>'

def read_seq(h):
    """independent reader: the terms of a printed sequence, None for the empty box"""
    s = re.search(r'<div class="seq4">(.*)', strip_gap(h), re.S)
    body = re.sub(r"</div>\s*$", "", s[1])
    out = []
    for m in re.finditer(r'<span class="sq4( bl)?">(.*?)</span>(?=<span class="sq4|$)', body):
        out.append(None if m[1] else int(re.sub(r"<[^>]+>", "", m[2])))
    return out

def fit_ap(t):
    """fill the one empty term of a pattern with a constant step"""
    known = [(i, v) for i, v in enumerate(t) if v is not None]; b = t.index(None)
    (i0, v0), (i1, v1) = known[0], known[-1]
    d = (v1 - v0) / (i1 - i0)
    assert d == int(d) and all(v - v0 == d * (i - i0) for i, v in known), t
    return int(v0 + d * (b - i0))

def page03():
    rng = random.Random(4303)
    for _ in range(8000):
        items = []
        st = rng.choice([1000, 2500, 500, 1500, 750, 3000]); a = rng.randint(2, 9) * 1000 + rng.randint(1, 9) * 100
        up = rng.random() < 0.5
        items.append(dict(k="end", t=[a + (1 if up else -1) * st * i + (0 if up else 25000) for i in range(5)], blank=4))
        st = rng.choice([250, 600, 1200, 4000, 800, 350]); a = rng.randint(30, 85) * 1000 + rng.randint(0, 9) * 100
        items.append(dict(k="mid", t=[a - st * i for i in range(5)], blank=2))
        st = rng.choice([1500, 2000, 4500, 6000, 750]); a = rng.randint(2, 9) * 1000 + rng.randint(1, 9) * 100
        items.append(dict(k="first", t=[a + st * i for i in range(5)], blank=0))
        p = rng.choice([2000, 3000, 5000, 1500]); q = rng.choice([500, 1000, 250, 800]); a = rng.randint(2, 9) * 1000 + rng.choice([0, 500])
        t = [a]
        for i in range(6): t.append(t[-1] + (p if i % 2 == 0 else -q))
        items.append(dict(k="alt", t=t, blank=6))
        a = rng.randint(2, 9) * 100; d = rng.choice([700, 600, 900, 1200, 450]); n = rng.choice([8, 9, 12])
        items.append(dict(k="nth", a=a, d=d, n=n))
        a = rng.choice([125, 250, 375, 500, 625, 800, 1250, 1500])
        items.append(dict(k="dbl", t=[a * 2 ** i for i in range(5)], blank=4))
        ans = []
        for it in items:
            if it["k"] == "nth": ans.append(it["a"] + it["d"] * (it["n"] - 1))
            else: ans.append(it["t"][it["blank"]])
        if not distinct(ans) or max(ans) > 99999 or min(ans) < 0: continue
        if any(max(it.get("t", [0])) > 99999 or min(it.get("t", [1])) < 0 for it in items): continue
        pool = set()
        for it in items:
            if it["k"] in ("end", "mid", "first"):
                t = it["t"]; b = it["blank"]; d = t[2] - t[1] if b != 2 else t[3] - t[1]
                d1 = (t[1] - t[0]) if b != 0 else (t[2] - t[1])
                pool |= {ans[items.index(it)] + d1 // 2, ans[items.index(it)] - d1 // 2, ans[items.index(it)] + d1, ans[items.index(it)] - d1}
            if it["k"] == "alt": pool |= {it["t"][5] + (it["t"][1] - it["t"][0]), it["t"][5] - (it["t"][1] - it["t"][2]) * 2}
            if it["k"] == "nth": pool |= {it["a"] + it["d"] * it["n"], it["a"] + it["d"] * (it["n"] - 2), it["d"] * it["n"]}
            if it["k"] == "dbl": pool |= {it["t"][3] + it["t"][1], it["t"][3] * 3 // 2 if (it["t"][3] * 3) % 2 == 0 else it["t"][3] + 1}
        pool = {p for p in pool if p not in ans and 0 < p <= 99999}
        dom = plausible_domain(ans, pool, rng=rng, sample=150)
        res = code_table_any(3, 6, ans, rng, 0, 99999, n_decoy=3, tries=60, pool=sorted(pool), domain=dom)
        if res: word, table = res; break
    else: raise RuntimeError("p03")
    cards = []
    for i, it in enumerate(items):
        if it["k"] in ("end", "mid", "first"):
            cards.append(qcard(i + 1, seq_html(it["t"], it["blank"]), "", cls="span2 sqc"))
        elif it["k"] == "dbl":
            cards.append(qcard(i + 1, "<p>Each number is double the one before.</p>" + seq_html(it["t"], it["blank"]), "", cls="span2 sqc"))
        elif it["k"] == "alt":
            cards.append(qcard(i + 1, "<p>The pattern goes up, then down, then up, then down. Find the next number.</p>" + seq_html(it["t"], 6), "", cls="span2 sqc"))
        else:
            cards.append(qcard(i + 1, f"<p>The first number is {N(it['a'])}. Each number is {N(it['d'])} more than the one before. What is number {it['n']}?</p>", ABX, cls="span2 inl"))
    P = code_page(3, 4303, "Number Patterns", 2, "Number patterns: find the missing number", STRAND_NU,
        "1.4 (patterns in number sequences)", ["NU1.4"], "Code-breaker (number patterns)",
        ["Find the rule of each pattern.", "Write the missing number in the box.", INSTR_CODE], '<div class="qg c1">' + "".join(cards) + "</div>", ans, table, word, 0, 99999,
        "; ".join(f"{i+1}) {Ntxt(a)}" for i, a in enumerate(ans)),
        "Six patterns with numbers up to 100 000: a step up or down with the last number missing, a step down with a number missing in the middle, a missing first number, a pattern that goes up by one amount and down by another in turn (the next number is asked), the 8th, 9th or 12th number found from the first number and the step, and a doubling pattern. The decoy letters stand for the usual slips: half the step, one step too many or too few, or forgetting the take-away step. A box left blank gives no letter and the check cannot see it.",
        domain=dom)
    solved = []
    for h in re.findall(r'<div class="qh"><span class="no">\d</span><div class="qt">(.*?)</div></div>', body_of := P["body"], re.S):
        if 'class="seq4"' in h:
            t = read_seq(h)
            if "double" in h: solved.append(t[t.index(None) - 1] * 2)
            elif "up, then down" in h:
                b = t.index(None); p_ = t[1] - t[0]; q_ = t[1] - t[2]
                solved.append(t[b - 1] + (p_ if (b - 1) % 2 == 0 else -q_))
            else: solved.append(fit_ap(t))
        else:
            m = re.search(r"first number is (\d+)\. Each number is (\d+) more than the one before\. What is number (\d+)\?", strip_gap(h))
            solved.append(int(m[1]) + int(m[2]) * (int(m[3]) - 1))
    P.v("V1 independent solver (rule found from the printed terms, then applied) equals the key", solved == ans, solved)
    P.v("V7 every number is below 100 000", max(ans) < 100000 and all(max(it.get("t", [0])) < 100000 for it in items))
    return P


# =============================================================================== P4-04 Round It (route)
def round_to(v, s):
    """round half up to the nearest s"""
    return (v + s // 2) // s * s

def page04():
    rng = random.Random(4404)
    n, LEN = 5, 11
    cells = [(r, c) for r in range(n) for c in range(n)]
    def claim(v, s, true):
        r = round_to(v, s)
        if true: return r
        opts = [x for x in {(v // s) * s, (v // s + 1) * s, r - s, r + s} if x != r and x >= 10000]
        return rng.choice(sorted(opts))
    for _ in range(20000):
        path = induced_path(rng, n, LEN, min_dist=6)
        extra = dead_ends(rng, n, path, 3); dead = len(extra)
        scales = [10] * 4 + [100] * 3 + [1000] * 4; rng.shuffle(scales)
        grid = {}
        for i, cell in enumerate(path): grid[cell] = (scales[i], True)
        for cell in extra: grid[cell] = (rng.choice([10, 100, 1000]), True)
        for cell in cells:
            if cell not in grid: grid[cell] = (rng.choice([10, 100, 1000]), False)
        data = {}
        for cell, (s_, tr) in grid.items():
            v = rng.randrange(10000, 99999)
            if rng.random() < .3: v = v // s_ * s_ + s_ // 2        # half way: rounds up
            data[cell] = (v, s_, claim(v, s_, tr))
        if len({d[0] for d in data.values()}) < 25: continue
        texts = [[f'<b class="mn">{N(data[(r, c)][0])}</b><small>{SYM_APPROX} {N(data[(r, c)][2])}<br>nearest {data[(r, c)][1]}</small>' for c in range(n)] for r in range(n)]
        start, finish = path[0], path[-1]
        def ok(cell, texts=texts):
            m = re.fullmatch(r'<b class="mn">(\d+)</b><small>.*?</svg> (\d+)<br>nearest (\d+)</small>', strip_gap(texts[cell[0]][cell[1]]))
            return round_to(int(m[1]), int(m[3])) == int(m[2])
        if count_routes(ok, n, start, finish) == 1 and 2 <= dead <= 3: break
    else: raise RuntimeError("p04")
    key = " -> ".join(f"({r+1},{c+1}) {Ntxt(data[(r, c)][0])} = {Ntxt(data[(r, c)][2])} to {data[(r, c)][1]}" for r, c in path)
    P = route_page(4, 4404, "Round It", 1, "Rounding numbers to the nearest 10, 100 or 1000; the sign for about", STRAND_NU,
        "1.5, 1.6 (rounding numbers to the nearest 10, 100 or 1000; use of the sign for about)", ["NU1.5", "NU1.6"], "Maze / path (rounding, true statements)",
        ["Each box says: number, about, rounded number.", "Start at START. Move up, down, left or right.", "Step only on boxes where the statement is true. Do not step on a box twice."],
        n, texts, start, finish, path, ok, "Route (row, column from top-left): " + key,
        f"Does your line reach FINISH? Are there {len(path)} boxes? Is every box a true statement?",
        f"A 5 by 5 grid of boxes, each with a number, the sign for about, a rounded number and the place it is rounded to (10, 100 or 1000). On the route every statement is true. Boxes off the route are false: they give the number rounded down when it should round up, up when it should round down, or one step too far. {dead} extra boxes with true statements are dead ends. Counting the boxes shows a line that takes a shortcut. Pupils round half way numbers up. The pupil reads the sign for about as is about.",
        dead, facts=" ".join(str(d[0]) + " " + str(d[2]) for d in data.values()), cls="maze")
    P.v("V7 every number is 5 digits and every box names 10, 100 or 1000", all(10000 <= d[0] <= 99999 and d[1] in (10, 100, 1000) for d in data.values()))
    P.v("V7b all 25 numbers are different", len({d[0] for d in data.values()}) == 25)
    P.v("V7c each of 10, 100 and 1000 is used on the route at least three times", all(sum(1 for c in path if data[c][1] == s_) >= 3 for s_ in (10, 100, 1000)))
    P.v("V7d at least two half way numbers are on boxes (they round up)", sum(1 for d in data.values() if d[0] % d[1] == d[1] // 2) >= 2)
    return P

# =============================================================================== P4-06 Factor or Not? (lettered Yes / No)
def yn_question(rng, kind, true):
    d = rng.choice([3, 4, 6, 7, 8, 9])
    if kind == "factor":
        if true: n = d * rng.randint(30 // d + 1, 99 // d)
        else:
            n = rng.randint(30, 99)
            while n % d == 0: n = rng.randint(30, 99)
        return f"Is {d} a factor of {n}?"
    if kind == "multiple":
        n = d * rng.randint(1000 // d + 1, 9999 // d - 1)
        if not true: n += rng.randint(1, d - 1)
        return f"Is {N(n)} a multiple of {d}?"
    if kind == "rel_ok":      # a true statement first; the question asks the same fact the other way round, or reversed
        n = d * rng.randint(30 // d + 1, 99 // d)
        return f"{n} is a multiple of {d}. Is {d} a factor of {n}?" if true else f"{n} is a multiple of {d}. Is {n} a factor of {d}?"
    raise ValueError(kind)

def solve_yn(t):
    """independent evaluator of the printed question (the last sentence is the question)"""
    t = strip_gap(re.sub(r"<[^>]+>", "", t)).split(". ")[-1]
    m = re.fullmatch(r"Is (\d+) a factor of (\d+)\?", t)
    if m: return int(m[2]) % int(m[1]) == 0
    m = re.fullmatch(r"Is (\d+) a multiple of (\d+)\?", t)
    if m: return int(m[1]) % int(m[2]) == 0
    raise ValueError(t)

def page06():
    rng = random.Random(4606)
    kinds = ["factor", "factor", "multiple", "multiple", "rel_ok", "rel_ok"]
    for _ in range(4000):
        word = word_candidates(6, 6)[rng.randrange(0, 3)]
        truths = [rng.random() < .5 for _ in range(6)]
        if not 2 <= sum(truths) <= 4: continue
        order = kinds[:]; rng.shuffle(order)
        qs = [yn_question(rng, k, t) for k, t in zip(order, truths)]
        if len(set(qs)) < 6 or [solve_yn(q) for q in qs] != truths: continue
        try: rows_l = choice_letters(rng, word, 2)
        except RuntimeError: continue
        CLAIMED[6] = word
        break
    rows = []
    for i, (q, tr) in enumerate(zip(qs, truths)):
        right, other = rows_l[i]
        yes_l, no_l = (right, other) if tr else (other, right)
        rows.append(choice_row(i + 1, f'<span class="yq">{q}</span>', ["Yes", "No"], [yes_l, no_l], "tall"))
    P = choice_page(6, 4606, "Factor or Not?", 1, "Factors and multiples: is it a factor? is it a multiple?", STRAND_NU,
        "2.1 (factors, multiples and their relationship), 2.2 (a 1-digit number as a factor of a number within 100), 2.4 (a multiple of a 1-digit number)", ["FM2.1", "FM2.2", "FM2.4"], "Choice table (yes or no)",
        ["Read each question.", "Circle the letter of the right answer.", "Write the six letters in the boxes."], rows, word, rows_l, [word[i] for i in range(6)],
        "; ".join(f"{i+1}) {'Yes' if t else 'No'} ({q})" for i, (q, t) in enumerate(zip(qs, truths))),
        "Six yes or no questions: two ask whether a 1-digit number is a factor of a number within 100, two ask whether a 4-digit number is a multiple of a 1-digit number (the pupil divides), and two start from a true statement and ask the same fact the other way round or reversed (the relationship between factor and multiple). Each row has a Yes and a No, each with a letter. The letters of the right answers, read down the rows, spell the word; every other way of choosing was tested against a very large word list and none spells a word. A box left blank gives no letter and the check cannot see it.")
    solved = []
    for content, opts in rows_of(P["body"]):
        d = {re.sub(r"<[^>]+>", "", t): l for t, l in opts}; solved.append(d["Yes"] if solve_yn(content) else d["No"])
    P.v("V1 independent solver (each printed question evaluated, the letter of the right answer read from the row) gets the word", "".join(solved) == word, solved)
    P.v("V4 between 2 and 4 answers are Yes", 2 <= sum(truths) <= 4)
    return P

# =============================================================================== P4-07 Multiples Maze (route)
def page07():
    rng = random.Random(4707)
    n, LEN = 4, 8
    cells = [(r, c) for r in range(n) for c in range(n)]
    m = 7
    def on(): return m * rng.randint(1000 // m + 1, 9999 // m - 1)
    def off():
        a = on()
        if rng.random() < .5: return a + rng.choice([1, -1, 2, -2, 3, -3])
        s = list(str(a)); i = rng.randrange(0, 3); s[i], s[i + 1] = s[i + 1], s[i]; return int("".join(s))
    for _ in range(20000):
        path = induced_path(rng, n, LEN, min_dist=4)
        grid = {cell: on() for cell in path}
        extra = dead_ends(rng, n, path, 3); dead = len(extra)
        for cell in extra: grid[cell] = on()
        for cell in cells:
            if cell not in grid:
                v = off()
                while v % m == 0 or not 1000 <= v <= 9999: v = off()
                grid[cell] = v
        if len(set(grid.values())) < 16: continue
        texts = [[str(grid[(r, c)]) for c in range(n)] for r in range(n)]
        start, finish = path[0], path[-1]
        ok = lambda cell, texts=texts: int(texts[cell[0]][cell[1]]) % m == 0
        if count_routes(ok, n, start, finish) == 1 and 2 <= dead <= 3: break
    else: raise RuntimeError("p07")
    P = route_page(7, 4707, "Multiples Maze", 1, "Multiples of a 1-digit number", STRAND_NU,
        "2.4 (determining if a number is a multiple of a given 1-digit number), 2.1 (factors, multiples and their relationship)", ["FM2.1", "FM2.4"], "Maze / path (multiples)",
        ["Start at START. Move up, down, left or right.", f"Step only on multiples of {m}.", "Do not step on a box twice."],
        n, texts, start, finish, path, ok, "Route (row, column from top-left): " + " -> ".join(f"({r+1},{c+1}) {grid[(r, c)]} = {m} x {grid[(r, c)] // m}" for r, c in path),
        f"Does your line reach FINISH? Count its boxes: are there {len(path)}? Is every box a multiple of {m}?",
        f"A 4 by 4 grid of 4-digit numbers. On the route every number is a multiple of {m} (the pupil divides). The boxes off the route are numbers near a multiple of {m} (one to three more or fewer) or a multiple with two digits swapped, so a slip in dividing sends the pupil there. {dead} extra boxes that are multiples of {m} are dead ends. Counting the boxes shows a line that takes a shortcut.",
        dead, facts=f"{m} " + " ".join(str(v) for v in grid.values()), cls="maze tall")
    P.v("V7 every number has 4 digits and the multiplier is a 1-digit number", all(1000 <= v <= 9999 for v in grid.values()) and m < 10)
    P.v("V7b all sixteen numbers are different", len(set(grid.values())) == 16)
    return P

# =============================================================================== P4-08 Common Factors (code word)
def factors_of(n): return [d for d in range(1, n + 1) if n % d == 0]

def cf_pair(rng, gmin, gmax, lo=12, hi=100):
    while True:
        g = rng.randint(gmin, gmax); a = g * rng.randint(2, hi // g); b = g * rng.randint(2, hi // g)
        if a != b and lo <= a <= hi and lo <= b <= hi and math.gcd(a, b) == g and a % b and b % a: return a, b

def page08():
    rng = random.Random(4808)
    for _ in range(6000):
        a1, b1 = cf_pair(rng, 4, 18)                                         # greatest common factor
        a2, b2 = cf_pair(rng, 6, 20)                                         # how many common factors
        a3, b3 = cf_pair(rng, 6, 20)                                         # sum of the common factors
        a4, b4 = cf_pair(rng, 8, 24)                                         # story: longest equal pieces
        a5, b5 = cf_pair(rng, 12, 30)                                        # second greatest common factor
        a6, b6 = cf_pair(rng, 8, 20)                                         # a common factor between two limits
        cf6 = [d for d in factors_of(math.gcd(a6, b6)) if d > 1]
        if len(cf6) < 3: continue
        lo6, mid, hi6 = cf6[0], cf6[1], cf6[2]
        if len(factors_of(math.gcd(a2, b2))) not in (4, 5, 6): continue
        cm = lambda a, b: [d for d in factors_of(a) if b % d == 0]
        ans = [math.gcd(a1, b1), len(cm(a2, b2)), sum(cm(a3, b3)), cm(a5, b5)[-2], math.gcd(a4, b4), mid]
        if not distinct(ans) or len({(a1, b1), (a2, b2), (a3, b3), (a4, b4), (a5, b5), (a6, b6)}) < 6: continue
        pool = set()
        for a, b in ((a1, b1), (a2, b2), (a3, b3), (a4, b4), (a5, b5), (a6, b6)):
            g = math.gcd(a, b); pool |= {g, g // 2 if g % 2 == 0 else g + 1, len(factors_of(g)), a * b // g if a * b // g <= 100 else g * 2, len(factors_of(a)), len(factors_of(b))}
        pool = {p for p in pool if p not in ans and 1 <= p <= 100}
        dom = list(range(0, 101))
        res = code_table_any(8, 6, ans, rng, 0, 100, n_decoy=3, tries=60, pool=sorted(pool), domain=dom)
        if res: word, table = res; break
    else: raise RuntimeError("p08")
    qs = [f"What is the greatest common factor of {a1} and {b1}?",
          f"How many common factors do {a2} and {b2} have?",
          f"Add all the common factors of {a3} and {b3}.",
          f"What is the second greatest common factor of {a5} and {b5}?",
          f"Two ribbons are {a4} cm and {b4} cm long. Cut them into equal pieces, as long as possible. How long is each piece?",
          f"Pick the common factor of {a6} and {b6} between {lo6} and {hi6}."]
    cards = [qcard(i + 1, f"<p>{q}</p>", ABX + (" cm" if i == 4 else ""), cls="span2 inl" if i >= 4 else "") for i, q in enumerate(qs)]
    P = code_page(8, 4808, "Common Factors", 2, "Common factors of two numbers", STRAND_NU,
        "2.3 (finding the common factors of two given numbers), 2.1 (factors, multiples and their relationship)", ["FM2.1", "FM2.3"], "Code-breaker (common factors)",
        ["Find the factors of both numbers.", "Write the answer in the box.", INSTR_CODE], qgrid(cards, 2), ans, table, word, 0, 100,
        "; ".join(f"{i+1}) {a}" for i, a in enumerate(ans)),
        "Six questions about the common factors of two numbers within 100: the greatest common factor, how many common factors, the sum of all the common factors (the pupil must find every one), the longest equal pieces of two ribbons, the second greatest common factor and the one common factor between two limits. Decoy letters stand for slips such as giving the number of factors of one number only, a common multiple, or missing a common factor. A box left blank gives no letter and the check cannot see it.",
        domain=dom, ps=True)
    solved = []
    for q in re.findall(r"<p>(.*?)</p>", P["body"]):
        nums = [int(x) for x in re.findall(r"\d+", q.replace(" cm", ""))]
        a, b = nums[0], nums[1]
        com = [d for d in range(1, a + 1) if a % d == 0 and b % d == 0]
        if q.startswith("What is the greatest") or q.startswith("Two ribbons"): solved.append(max(com))
        elif q.startswith("How many"): solved.append(len(com))
        elif q.startswith("Add all"): solved.append(sum(com))
        elif q.startswith("What is the second"): solved.append(sorted(com)[-2])
        else:
            c = [d for d in com if nums[2] < d < nums[3]]; assert len(c) == 1; solved.append(c[0])
    P.v("V1 independent solver (common factors listed from the printed numbers) equals the key", solved == ans, solved)
    P.v("V7 every number is within 100 and every pair has a common factor greater than 1", all(max(p) <= 100 and math.gcd(*p) > 1 for p in ((a1, b1), (a2, b2), (a3, b3), (a4, b4), (a5, b5), (a6, b6))))
    return P

# =============================================================================== P4-09 Number Riddles (code word)
def clue_fn(c):
    k = c[0]
    return {"mult": lambda x: x % c[1] == 0, "factor": lambda x: c[1] % x == 0, "cm": lambda x: x % c[1] == 0 and x % c[2] == 0,
            "cf": lambda x: c[1] % x == 0 and c[2] % x == 0, "gt": lambda x: x > c[1], "lt": lambda x: x < c[1], "even": lambda x: x % 2 == 0,
            "odd": lambda x: x % 2 == 1, "ones": lambda x: x % 10 == c[1]}[k]

def clue_text(c):
    k = c[0]
    if k == "mult": return f"I am a multiple of {c[1]}."
    if k == "factor": return f"I am a factor of {c[1]}."
    if k == "cm": return f"I am a common multiple of {c[1]} and {c[2]}."
    if k == "cf": return f"I am a common factor of {c[1]} and {c[2]}."
    if k == "gt": return f"I am greater than {c[1]}."
    if k == "lt": return f"I am less than {c[1]}."
    if k == "even": return "I am an even number."
    if k == "odd": return "I am an odd number."
    if k == "ones": return f"My ones digit is {c[1]}."
    raise ValueError(k)

def read_clue(t):
    """independent reader of a printed clue: returns a predicate on whole numbers"""
    t = t.strip()
    for rx, mk in ((r"I am a multiple of (\d+)\.", lambda m: lambda x: x % int(m[1]) == 0),
                   (r"I am a factor of (\d+)\.", lambda m: lambda x: int(m[1]) % x == 0),
                   (r"I am a common multiple of (\d+) and (\d+)\.", lambda m: lambda x: x % int(m[1]) == 0 and x % int(m[2]) == 0),
                   (r"I am a common factor of (\d+) and (\d+)\.", lambda m: lambda x: int(m[1]) % x == 0 and int(m[2]) % x == 0),
                   (r"I am greater than (\d+)\.", lambda m: lambda x: x > int(m[1])),
                   (r"I am less than (\d+)\.", lambda m: lambda x: x < int(m[1])),
                   (r"I am an even number\.", lambda m: lambda x: x % 2 == 0),
                   (r"I am an odd number\.", lambda m: lambda x: x % 2 == 1),
                   (r"My ones digit is (\d)\.", lambda m: lambda x: x % 10 == int(m[1]))):
        m = re.fullmatch(rx, t)
        if m: return mk(m)
    raise ValueError(t)

def make_riddle(rng, a):
    """three true clues about a that leave exactly one number from 1 to 999 (None when a try fails)"""
    pool = []
    ms = [m for m in range(2, 10) if a % m == 0]
    if ms: pool.append(("mult", rng.choice(ms)))
    fs = [N_ for N_ in range(a + 1, 101) if N_ % a == 0]
    if fs and a <= 50: pool.append(("factor", rng.choice(fs)))
    cms = [(p, q) for p in range(2, 10) for q in range(p + 1, 10) if a % p == 0 and a % q == 0 and q % p != 0]
    if cms: pool.append(("cm",) + rng.choice(cms))
    cfs = [(p, q) for p in range(a, 101, a) for q in range(p + a, 101, a) if p != q]
    if cfs and a >= 4: pool.append(("cf",) + rng.choice(cfs))
    pool.append(("gt", a - rng.randint(2, 9))); pool.append(("lt", a + rng.randint(2, 14)))
    pool.append(("even",) if a % 2 == 0 else ("odd",)); pool.append(("ones", a % 10))
    kinds = {}
    for c in pool: kinds.setdefault(c[0], c)
    for _ in range(60):
        cs = rng.sample(list(kinds.values()), 3)
        ks = {c[0] for c in cs}
        if not ks & {"mult", "factor", "cm", "cf"}: continue
        if not ks & {"factor", "cf", "lt"}: continue
        if ks & {"even", "odd"} and ks & {"ones"}: continue
        sol = [x for x in range(1, 1000) if all(clue_fn(c)(x) for c in cs)]
        if sol == [a]: return cs
    return None

def page09():
    rng = random.Random(4909)
    for _ in range(3000):
        answers = rng.sample(range(12, 100), 5) + [rng.randint(100, 240)]
        riddles = [make_riddle(rng, a) for a in answers]
        if any(r is None for r in riddles) or not distinct(answers): continue
        if sum(1 for r in riddles if any(c[0] in ("cm", "cf") for c in r)) < 2: continue
        if not any(c[0] == "cm" for r in riddles for c in r): continue
        pool = set()
        for r, a in zip(riddles, answers):
            for x in range(1, 1000):
                if x != a and sum(clue_fn(c)(x) for c in r) == 2: pool.add(x)
        pool = {p for p in pool if p not in answers}
        dom = list(range(0, 1000))
        res = code_table_any(9, 6, answers, rng, 0, 999, n_decoy=3, tries=60, pool=sorted(pool), domain=dom)
        if res: word, table = res; break
    else: raise RuntimeError("p09")
    cards = [qcard(i + 1, "".join(f"<p>{clue_text(c)}</p>" for c in r), ABX) for i, r in enumerate(riddles)]
    P = code_page(9, 4909, "Number Riddles", 2, "Factors and multiples: who am I?", STRAND_NU,
        "2.1 (factors, multiples and their relationship), 2.3 (common factors), 2.4 (multiples), 2.5 (common multiples of two 1-digit numbers)", ["FM2.1", "FM2.3", "FM2.4", "FM2.5"], "Number riddles",
        ["Use all three clues.", "Write the number in the box.", INSTR_CODE], qgrid(cards, 2), answers, table, word, 0, 999,
        "; ".join(f"{i+1}) {a}" for i, a in enumerate(answers)),
        "Six riddles with three clues each, drawn from: a multiple of a 1-digit number, a factor of a number within 100, a common multiple of two 1-digit numbers, a common factor of two numbers within 100, greater than, less than, odd or even and the ones digit. Each riddle was solved by trying every whole number from 1 to 999: exactly one number fits all three clues. The decoy letters stand for numbers that fit two of the three clues. A box left blank gives no letter and the check cannot see it.",
        domain=dom, ps=True)
    solved = []
    for qh in re.findall(r'<div class="qt">(.*?)</div></div>', P["body"], re.S):
        preds = [read_clue(c) for c in re.findall(r"<p>(.*?)</p>", qh)]
        sol = [x for x in range(1, 1000) if all(p(x) for p in preds)]
        solved.append(sol[0] if len(sol) == 1 else sol)
    P.v("V1 independent solver (clues read back, every number from 1 to 999 tried) finds exactly one number in every riddle and equals the key", solved == answers, solved)
    P.v("V7 every riddle has three clues and a clue about factors or multiples; the numbers in factor clues are within 100", all(len(r) == 3 for r in riddles))
    return P

# =============================================================================== P4-10 Long Multiplication (code word)
def vmul_html(top, bot):
    """vertical multiplication: numbers right-aligned, the sign beside the lower number, a rule, a wide answer box"""
    ncol = 4
    def row(n, op=""):
        s = str(n).rjust(ncol)
        return f'<div class="vr"><em>{op}</em>' + "".join(f"<i>{ch}</i>" if ch != " " else "<i></i>" for ch in s) + "</div>"
    return (f'<div class="vsum vmul" style="--n:{ncol}">' + row(top) + row(bot, "×") + '<div class="vrule"></div>'
            + '<div class="vr vans"><em></em><span class="ab w5"></span></div></div>')

def page10():
    rng = random.Random(5010)
    for _ in range(6000):
        sums = []
        for _k in range(3):
            sums.append((rng.randint(1100, 9999), rng.randint(3, 9)))
        for _k in range(3):
            sums.append((rng.randint(130, 999), rng.randint(12, 98)))
        # carries needed everywhere: reject sums that have no carry
        def has_carry(a, b):
            return any(int(x) * (b % 10) >= 10 for x in str(a))
        if not all(has_carry(a, b) for a, b in sums): continue
        if any(b % 10 == 0 for a, b in sums[3:]): continue
        ans = [a * b for a, b in sums]
        if not distinct(ans) or max(ans) > 99999: continue
        def nocarry(a, b): return int("".join(str(int(x) * b % 10) for x in str(a)))
        pool = set()
        for (a, b) in sums[:3]: pool |= {nocarry(a, b), a * b + 1000 * rng.choice([-1, 1]), a * b - 10 if a * b > 10 else 0}
        for (a, b) in sums[3:]:
            p1 = a * (b % 10); p2 = a * (b // 10)
            pool |= {p1 + p2, p1 * 10 + p2 * 10, p1 + p2 * 100}
        pool = {p for p in pool if p not in ans and 0 < p <= 99999}
        dom = plausible_domain(ans, pool, rng=rng, sample=150)
        res = code_table_any(10, 6, ans, rng, 0, 99999, n_decoy=3, tries=60, pool=sorted(pool), domain=dom)
        if res: word, table = res; break
    else: raise RuntimeError("p10")
    cards = "".join(f'<div class="vcard"><span class="no">{i+1}</span>{vmul_html(a, b)}</div>' for i, (a, b) in enumerate(sums))
    P = code_page(10, 5010, "Long Multiplication", 1, "Multiplying: 4 digits by 1 digit, 3 digits by 2 digits", STRAND_NU,
        "3.1 (multiplication algorithm: up to 4 digits by 1 digit; up to 3 digits by 2 digits)", ["FO3.1"], "Code-breaker (multiplication algorithm)",
        ["Work out each product in columns.", "Write the answer in the box.", INSTR_CODE], f'<div class="vcards vc3">{cards}</div>', ans, table, word, 0, 99999,
        "; ".join(f"{i+1}) {a} x {b} = {Ntxt(x)}" for i, ((a, b), x) in enumerate(zip(sums, ans))),
        "Three multiplications of 4 digits by 1 digit and three of 3 digits by 2 digits, each needing renaming (carrying). The decoy letters stand for the usual slips: forgetting to carry, and adding the two partial products of a 3-digit by 2-digit sum without shifting the second one. A box left blank gives no letter and the check cannot see it.",
        domain=dom)
    solved = []
    for h in re.findall(r'<div class="vsum vmul".*?</div></div></div>', P["body"], re.S):
        a, b, op = parse_vsum(h); assert op == "×"; solved.append(a * b)
    P.v("V1 independent solver (columns read back from the printed digits) equals the key", solved == ans, solved)
    P.v("V7 four 4-digit by 1-digit and 3-digit by 2-digit sums; every product is below 100 000", all(1000 <= a <= 9999 and 2 <= b <= 9 for a, b in sums[:3]) and all(100 <= a <= 999 and 10 <= b <= 99 for a, b in sums[3:]) and max(ans) < 100000)
    return P

PAGES = [page01, page02, page03, page04, page06, page07, page08, page09, page10]
