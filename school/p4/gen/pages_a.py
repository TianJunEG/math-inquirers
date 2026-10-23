"""Wave A: Numbers up to 100 000 (P4-01 to P4-04; P4-05 is colour by code), factors and multiples (P4-06 to P4-09), multiplication (P4-10).
Each pageNN() makes the puzzle from a seed, re-solves it with separate solver code that reads the PRINTED html, and gives validate.py a `model`."""
import random, re, math, itertools
from .common import *
from .kit import *
from .kit4 import *

# =============================================================================== P4-01 Place Value
def pv_table(counts):
    heads = ["Ten thousands", "Thousands", "Hundreds", "Tens", "Ones"]
    return ('<table class="pvt4"><tr>' + "".join(f"<th>{h}</th>" for h in heads) + "</tr><tr>" + "".join(f"<td>{c}</td>" for c in counts) + "</tr></table>")

def page01():
    rng = random.Random(4101)
    for _ in range(4000):
        counts = [rng.randint(1, 8), rng.randint(10, 18), rng.randint(0, 9), rng.randint(0, 9), rng.randint(0, 9)]
        v1 = counts[0] * 10000 + counts[1] * 1000 + counts[2] * 100 + counts[3] * 10 + counts[4]
        if v1 > 99999 or counts[2] == 0: continue
        # value of a digit (appears once)
        n2 = rng.choice([x for x in range(10000, 99999) if len(set(str(x))) == 5 and "0" not in str(x)])
        d2 = int(str(n2)[rng.choice([1, 2])]); a2 = d2 * 10 ** (4 - str(n2).index(str(d2)))
        n3 = rng.randrange(1000, 9999, 100) + rng.choice([0, 0, 0]); n3 = rng.randint(31, 98) * 100 + rng.choice([0, 0, 0]); a3 = n3 // 100
        n4 = rng.randint(21, 89) * 1000 + rng.randint(2, 8) * 100 + rng.randint(1, 9) * 10; a4 = n4 + 10000
        n5 = rng.choice([x for x in range(10000, 99999) if len(set(str(x))) == 5 and "0" not in str(x)])
        d5 = int(str(n5)[0]); a5 = d5 * 10000
        parts = [rng.randint(2, 9) * 10000, rng.randint(1, 9) * 1000, rng.randint(1, 9) * 100, rng.randint(1, 9) * 10, rng.randint(1, 9)]
        sel = rng.sample(parts, 4); a6 = sum(sel); order = sel[:]; rng.shuffle(order)
        ans = [v1, a2, a3, a4, a5, a6]
        if not distinct(ans) or max(ans) > 99999 or a6 == n2 or order == sorted(order, reverse=True): continue
        pool = {int("".join(str(c) for c in counts[:1] + [counts[1] % 10]) ) if False else counts[0] * 10000 + (counts[1] % 10) * 1000 + counts[2] * 100 + counts[3] * 10 + counts[4],
                v1 - 9000, v1 + 9000, d2, d2 * 10, d2 * 100, d2 * 1000 if d2 * 1000 != a2 else d2 * 100, a2 * 10 if a2 * 10 < 100000 else a2 // 10,
                n3 // 10, n3 // 1000, n3 // 100 + 1, a4 - 10000 + 1000, a4 - 9000, a4 + 1000 - 10000, n4 + 1000, n4 + 100,
                d5, d5 * 1000, a5 // 10, a6 - 10000, a6 + 1000 if a6 + 1000 < 100000 else a6 - 1000}
        pool = {p for p in pool if p not in ans and 0 <= p <= 99999}
        dom = plausible_domain(ans, pool, rng=rng, sample=150)
        res = code_table_any(1, 6, ans, rng, 0, 99999, n_decoy=3, tries=60, pool=sorted(pool), domain=dom)
        if res: word, table = res; break
    else: raise RuntimeError("p01")
    abx = '<span class="ab w4"></span>'
    cards = [
        qcard(1, f'<p>Write the number shown in the chart.</p>{pv_table(counts)}', abx, cls="span2 inl"),
        qcard(2, f"<p>In {N(n2)}, what is the value of the digit {d2}?</p>", abx),
        qcard(3, f"<p>How many hundreds are in {N(n3 * 1)}?</p>", abx),
        qcard(4, f"<p>What is 10{GAP}000 more than {N(n4)}?</p>", abx),
        qcard(5, f"<p>What is the value of the digit {d5} in {N(n5)}?</p>", abx),
        qcard(6, "<p>Write the number: " + " + ".join(N(x) for x in order) + "</p>", abx, cls="span2 inl"),
    ]
    body = qgrid(cards, 2)
    P = code_page(1, 4101, "Place Value", 1, "Place value: ten thousands, thousands, hundreds, tens and ones", STRAND_NU,
        "1.1 (number notation, representations and place values), 1.2 (reading and writing numbers)", ["NU1.1", "NU1.2"], "Code-breaker (place value)",
        ["Work out each item.", "Write the number in the box.", INSTR_CODE], body, ans, table, word, 0, 99999,
        "; ".join(f"{i+1}) {Ntxt(a)}" for i, a in enumerate(ans)),
        "A place-value chart whose thousands column holds more than 9 (regrouping), the value of a digit, the number of hundreds in a number, 10 000 more, the value of a digit in the ten-thousands place and the sum of four parts given in a mixed-up order. Decoy letters stand for slips such as giving the digit instead of its value, a wrong place, or forgetting to regroup. A box left blank gives no letter and the check cannot see it.",
        domain=dom)
    # independent solver: reads the printed cards
    solved = []
    cs = body
    tds = [int(x) for x in re.findall(r"<td>(\d+)</td>", cs)]
    solved.append(sum(c * 10 ** (4 - i) for i, c in enumerate(tds)))
    m = re.search(r"In ([\d]+), what is the value of the digit (\d)\?", strip_gap(cs)); solved.append(int(m[2]) * 10 ** (len(m[1]) - 1 - m[1].index(m[2])))
    m = re.search(r"How many hundreds are in (\d+)\?", strip_gap(cs)); solved.append(int(m[1]) // 100)
    m = re.search(r"What is 10000 more than (\d+)\?", strip_gap(cs)); solved.append(10000 + int(m[1]))
    m = re.search(r"value of the digit (\d) in (\d+)\?", strip_gap(cs)); solved.append(int(m[1]) * 10 ** (len(m[2]) - 1 - m[2].index(m[1])))
    m = re.search(r"Write the number: ([^<]*)</p>", strip_gap(cs)); solved.append(sum(int(x) for x in m[1].split("+")))
    P.v("V1 independent solver (chart, digit values and parts read back from the printed cards) equals the key", solved == ans, solved)
    P.v("V7 every number is below 100 000", max(ans) < 100000 and n2 < 100000 and n5 < 100000)
    P.v("V1b the digit asked about appears once in its number", str(n2).count(str(d2)) == 1 and str(n5).count(str(d5)) == 1)
    P["key"]["answers"] = f"1) chart: {counts[0]} ten thousands, {counts[1]} thousands, {counts[2]} hundreds, {counts[3]} tens, {counts[4]} ones = {Ntxt(v1)}; " + "; ".join(f"{i+2}) {Ntxt(a)}" for i, a in enumerate(ans[1:]))
    return P

# =============================================================================== P4-02 Words and Numerals (matching cards)
ONES = "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split()
TENS = "x x twenty thirty forty fifty sixty seventy eighty ninety".split()
def below100(n): return ONES[n] if n < 20 else TENS[n // 10] + ("-" + ONES[n % 10] if n % 10 else "")
def below1000(n):
    h, r = divmod(n, 100)
    if h == 0: return below100(r)
    return ONES[h] + " hundred" + (" and " + below100(r) if r else "")
def words_of(n):
    th_, r = divmod(n, 1000)
    if th_ == 0: return below1000(r)
    out = below1000(th_) + " thousand"
    if r == 0: return out
    return out + (" and " + below100(r) if r < 100 else ", " + below1000(r)) if r >= 100 else out + " and " + below100(r)
def words_of2(n):
    th_, r = divmod(n, 1000)
    s = below1000(th_) + " thousand" if th_ else ""
    if r:
        if r < 100 and th_: s += " and " + below100(r)
        else: s += (", " if th_ else "") + below1000(r)
    return s
def num_from_words(s):
    """independent reader of a number written in words"""
    tot = 0; cur = 0
    for w in re.split(r"[\s,\-]+", s.lower()):
        if w in ("and", ""): continue
        if w in ONES: cur += ONES.index(w)
        elif w in TENS and w != "x": cur += TENS.index(w) * 10
        elif w == "hundred": cur *= 100
        elif w == "thousand": tot += cur * 1000; cur = 0
        else: raise ValueError(w)
    return tot + cur

def misreads(n):
    """numerals a pupil could confuse with n: a zero moved, digits swapped, the thousands read as hundreds"""
    s = str(n); out = set()
    for i in range(len(s) - 1):
        t = list(s); t[i], t[i + 1] = t[i + 1], t[i]; out.add(int("".join(t)))
    for i in range(len(s)):
        if s[i] == "0":
            out.add(int(s[:i] + s[i + 1:])) if len(s) > 1 else None
    out.add(int(s[:-3] + "0" + s[-3:]) if len(s) >= 4 and False else n)
    return {x for x in out if x != n and 1000 <= x <= 99999}

def page02():
    rng = random.Random(4202)
    for _ in range(4000):
        word = word_candidates(2, 6)[rng.randrange(0, 4)]; CLAIMED[2] = word
        base = []
        for k in range(6):
            while True:
                n = rng.choice([rng.randint(10, 99) * 1000 + rng.choice([0, 0, 5, 50, 500, 6, 60, 600, 8, 80, 800, 4, 40, 400]) + rng.choice([0, 0, 0, 20, 30, 7, 9, 40]),
                                rng.randint(1, 9) * 1000 + rng.choice([0, 5, 50, 500, 6, 60, 600]) + rng.choice([0, 20, 4, 70])])
                if 1000 <= n <= 99999 and n % 1000 != 0 or rng.random() < 0.1:
                    if n <= 99999 and n >= 1000: break
            base.append(n)
        if not distinct(base): continue
        dec = []
        for n in rng.sample(base, 6):
            m = sorted(x for x in misreads(n) if x not in base and x not in dec)
            if m: dec.append(rng.choice(m))
            if len(dec) == 4: break
        if len(dec) < 4 or not distinct(dec): continue
        # numerals on the page: 10 cards; one word is an extreme example (zeros inside)
        letters_dec = letters_for_cards(rng, word, 4)
        break
    cards = [(n, word[i]) for i, n in enumerate(base)] + [(n, letters_dec[i]) for i, n in enumerate(dec)]
    shown = cards[:]; rng.shuffle(shown)
    wr = base[:]; rng.shuffle(wr)
    row_letter = {n: l for n, l in cards}
    order_letters = [row_letter[n] for n in wr]
    # the code word is spelt by the letters in the order of the word rows; choose rows so the right letters read as the word: reorder the words to follow the word
    wr = list(base)       # row i holds the number whose card carries word[i]
    rows = "".join(f'<div class="wrow"><span class="no">{i+1}</span><span class="wtxt">{esc(words_of2(n)).capitalize()}</span><span class="ab sm"></span></div>' for i, n in enumerate(wr))
    cardsh = '<div class="ncards">' + "".join(f'<div class="ncard"><b>{N(n)}</b><i class="cl">{l}</i></div>' for n, l in shown) + "</div>"
    body = f'<div class="blk"><p class="lead">Numbers</p>{cardsh}</div><div class="blk"><p class="lead">Words: write the letter of the matching number.</p><div class="wrows">{rows}</div></div>'
    P = new_page(2, 4202, "Words and Numerals", 1, "Reading and writing numbers up to 100 000 in numerals and in words", STRAND_NU,
        "1.2 (reading and writing numbers in numerals and in words)", ["NU1.2"], "Matching (number words to numeral cards)",
        "K1 letters of the matching cards spell a word (6 letters) + decoy cards", ["Read each number in words.", "Find its numeral on a card.", "Write the letter of the card in the box."],
        body, "; ".join(f"{i+1}) {esc(words_of2(n))} = {Ntxt(n)} ({word[i]})" for i, n in enumerate(wr)), f"Word: {word}",
        "Six numbers in words (thousands, hundreds, tens and ones, with zeros in the middle in some). Ten numeral cards are printed: six match, four are decoys made by moving a zero or swapping two digits (the common slips when a number in words is written as a numeral). The letters of the matching cards, read down the six rows, spell the word. A decoy card put in any row gives a letter that does not spell a word, and no swap of two rows does either (all tested against a very large word list). A box left blank gives no letter and the check cannot see it.",
        check="Write the six letters in order. Do they spell a word?", check_boxes=6, mk=("code",), mech_plain="Word from the letters of the matching cards (6 letters)")
    # independent solver: read the words and the cards, match by value
    cardl = {int(strip_gap(m[0])): m[1] for m in re.findall(r'<div class="ncard"><b>([^<]*)</b><i class="cl">(\w)</i>', body)}
    wtxt = re.findall(r'<span class="wtxt">([^<]*)</span>', body)
    solved = "".join(cardl[num_from_words(w)] for w in wtxt)
    P.v("V1 independent solver (words converted to numbers and matched to the cards) gets the word", solved == word, solved)
    P.v("V3d the code word's letters have exactly ONE arrangement that is a word", anagrams(word) == [word.lower()])
    P.v("V3 no single wrong card in any row, and no swap of two rows, spells a word (large word list)", all(not ("".join(word[:i]) + c + word[i + 1:]).lower() in BIG for i in range(6) for c in set(word) | set(letters_dec) if c != word[i]))
    bad_orders = no_wrong_order(word)
    P.v("V3e none of the 719 wrong orders of the six letters spells a word", not bad_orders, bad_orders[:3])
    P.v("V7 all numbers are between 1000 and 99 999; decoys differ from every right card", all(1000 <= n <= 99999 for n in base + dec) and not (set(dec) & set(base)))
    P.v("V8 every number in words is read back to its numeral", all(num_from_words(words_of2(n)) == n for n in base))
    all_letters = sorted(set(word) | set(letters_dec))
    P["cv"] = dict(rate=1.0, single_total=6 * (len(all_letters) - 1), single_detected=6 * (len(all_letters) - 1))
    P["model"] = dict(truth=list(word), domains=[all_letters] * 6, check=letters_check(), perm=list(range(6)), numeric=False)
    P["facts"] = " ".join(str(n) for n in base + dec)
    return P

# =============================================================================== P4-03 Number Patterns
def seq_html(terms, blank, label=None):
    cells = ""
    for i, t in enumerate(terms):
        cells += '<span class="sq4 ab-in"><span class="ab w4"></span></span>' if i == blank else f'<span class="sq4">{N(t)}</span>'
    return f'<div class="seq4">{cells}</div>'

def page03():
    rng = random.Random(4303)
    for _ in range(6000):
        items = []
        # 1 constant step up, last term missing
        st = rng.choice([1000, 2500, 500, 1500, 750, 3000]); a = rng.randint(1, 20) * 100 + rng.randint(1, 9) * 1000
        items.append(dict(k="end", t=[a + st * i for i in range(5)], blank=4))
        # 2 step down, missing middle
        st = rng.choice([250, 600, 1200, 4000, 800, 350]); a = rng.randint(30, 85) * 1000 + rng.randint(0, 9) * 100
        t = [a - st * i for i in range(5)]; items.append(dict(k="mid", t=t, blank=2))
        # 3 missing first
        st = rng.choice([1500, 2000, 4500, 6000, 750]); a = rng.randint(2, 9) * 1000 + rng.randint(1, 9) * 100
        items.append(dict(k="first", t=[a + st * i for i in range(5)], blank=0))
        # 4 alternating +p, -q: ask next term
        p = rng.choice([2000, 3000, 5000, 1500]); q = rng.choice([500, 1000, 250, 800]); a = rng.randint(2, 9) * 1000 + rng.choice([0, 500])
        t = [a]
        for i in range(6): t.append(t[-1] + (p if i % 2 == 0 else -q))
        items.append(dict(k="alt", t=t, p=p, q=q, blank=6, shown=6))
        # 5 the nth term
        a = rng.randint(2, 9) * 100; d = rng.choice([700, 600, 900, 1200, 450]); n = rng.choice([8, 9, 12])
        items.append(dict(k="nth", a=a, d=d, n=n))
        # 6 doubling
        a = rng.choice([125, 250, 375, 500, 625, 800, 1250, 1500]); items.append(dict(k="dbl", t=[a * 2 ** i for i in range(5)], blank=4))
        ans = []
        for it in items:
            if it["k"] in ("end", "mid", "first", "dbl"): ans.append(it["t"][it["blank"]])
            elif it["k"] == "alt": ans.append(it["t"][it["blank"]])
            else: ans.append(it["a"] + it["d"] * (it["n"] - 1))
        if not distinct(ans) or max(ans) > 99999 or min(ans) < 0: continue
        if any(max(it.get("t", [0])) > 99999 for it in items): continue
        pool = set()
        for it in items:
            if it["k"] in ("end", "dbl"): pool |= {it["t"][3] + (it["t"][3] - it["t"][2]) // 2 if it["k"] == "end" else it["t"][3] * 2 - 1, it["t"][3]}
            if it["k"] == "alt": pool |= {it["t"][5] + it["p"], it["t"][5] - it["q"]}
            if it["k"] == "nth": pool |= {it["a"] + it["d"] * it["n"], it["a"] + it["d"] * (it["n"] - 2), it["d"] * it["n"]}
            if it["k"] == "mid": pool |= {it["t"][1] - (it["t"][0] - it["t"][1]) // 2, it["t"][1]}
            if it["k"] == "first": pool |= {it["t"][1] - (it["t"][2] - it["t"][1]) * 2 if it["t"][1] > (it["t"][2] - it["t"][1]) * 2 else it["t"][1] // 2}
        pool = {p for p in pool if p not in ans and 0 < p <= 99999}
        dom = plausible_domain(ans, pool, rng=rng, sample=150)
        res = code_table_any(3, 6, ans, rng, 0, 99999, n_decoy=3, tries=60, pool=sorted(pool), domain=dom)
        if res: word, table = res; break
    else: raise RuntimeError("p03")
    cards = []
    for i, it in enumerate(items):
        if it["k"] in ("end", "mid", "first", "dbl"):
            txt = {"dbl": "Each number is double the one before.", "first": "", "end": "", "mid": ""}[it["k"]]
            cards.append(qcard(i + 1, (f"<p>{txt}</p>" if txt else "") + seq_html(it["t"], it["blank"]), "", cls="span2 sqc"))
        elif it["k"] == "alt":
            sh = it["t"][:6]
            cards.append(qcard(i + 1, "<p>Add, then take away, then add, then take away. Find the next number.</p>" + seq_html(sh + [0], 6), "", cls="span2 sqc"))
        else:
            cards.append(qcard(i + 1, f"<p>The first number is {N(it['a'])}. Each number is {N(it['d'])} more than the one before. What is number {it['n']}?</p>", '<span class="ab w4"></span>', cls="span2 inl"))
    P = code_page(3, 4303, "Number Patterns", 2, "Number patterns: find the missing number", STRAND_NU,
        "1.4 (patterns in number sequences)", ["NU1.4"], "Code-breaker (number patterns)",
        ["Find the rule of each pattern.", "Write the missing number in the box.", INSTR_CODE], '<div class="qg c1">' + "".join(cards) + "</div>", ans, table, word, 0, 99999,
        "; ".join(f"{i+1}) {Ntxt(a)}" for i, a in enumerate(ans)),
        "Six patterns with numbers up to 100 000: a step up, a step down with the missing number in the middle, a missing first number, a pattern that adds one amount and takes away another in turn (the next number is asked), a long pattern where the pupil finds the 8th, 9th or 12th number from the first number and the step, and a doubling pattern. The decoy letters stand for the usual slips: using half the step, stopping one number early or one number late, or forgetting to take away. A box left blank gives no letter and the check cannot see it.",
        domain=dom)
    solved = []
    cs = strip_gap(P["body"])
    seqs = re.findall(r'<div class="seq4">(.*?)</div>', cs)
    def terms(s): return [None if 'class="ab' in c else int(re.sub(r"<[^>]+>", "", c)) for c in re.findall(r'<span class="sq4[^"]*">(.*?)</span>(?=<span class="sq4|$)', s)]
    def terms2(s):
        out = []
        for m in re.finditer(r'<span class="sq4( ab-in)?">(.*?)</span>(?=<span class="sq4|\Z)', s):
            out.append(None if m.group(1) else int(re.sub(r"<[^>]+>", "", m.group(2))))
        return out
    cards_txt = re.findall(r'<div class="qc[^"]*">.*?</div></div>', P["body"])
    ti = 0
    for it_html in re.findall(r'<div class="qh"><span class="no">(\d)</span><div class="qt">(.*?)</div></div>', P["body"]):
        no_, h = it_html; h = strip_gap(h)
        if 'seq4' in h:
            t = terms2(re.search(r'<div class="seq4">(.*)</div>', h)[1])
            known = [x for x in t if x is not None]; bi = t.index(None)
            if "double" in h: solved.append(known[-1] * 2)
            elif "Add, then take away" in h:
                # the printed terms alternate +p, -q: p = t1 - t0, q = t1 - t2
                p_ = t[1] - t[0]; q_ = t[1] - t[2]; solved.append(t[5] + p_ if (6 % 2 == 0) else t[5] - q_)
            else:
                d = (known[-1] - known[0]) // (len(known) - 1) if bi in (0, len(t) - 1) else (known[-1] - known[0]) // (len(t) - 2)
                if bi == 0: solved.append(known[0] - d)
                elif bi == len(t) - 1: solved.append(known[-1] + d)
                else: solved.append(known[0] + d * bi)
        else:
            m = re.search(r"first number is (\d+)\. Each number is (\d+) more than the one before\. What is number (\d+)\?", h)
            solved.append(int(m[1]) + int(m[2]) * (int(m[3]) - 1))
    P.v("V1 independent solver (rule found from the printed terms, then applied) equals the key", solved == ans, solved)
    P.v("V7 every number is below 100 000", max(ans) < 100000)
    P["key"]["answers"] = "; ".join(f"{i+1}) {Ntxt(a)}" for i, a in enumerate(ans))
    return P
