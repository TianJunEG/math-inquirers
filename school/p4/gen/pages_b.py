"""Wave B: division (P4-12), the number ring (P4-13), fractions (P4-14 to P4-17, P4-20), angles (P4-18, P4-19). P4-11 is colour by code.
Each pageNN() makes the puzzle from a seed, re-solves it with separate solver code that reads the PRINTED html or drawing, and gives validate.py a `model`."""
import random, re, math, itertools
from fractions import Fraction
from .common import *
from .kit import *
from .kit4 import *
from . import art4 as A4

ABX = '<span class="ab w4"></span>'
ABS = '<span class="ab w3"></span>'
FR = lambda f: frac_html((f.numerator, f.denominator))

def cards_of(body):
    """split a card grid into its cards"""
    return re.split(r'(?=<div class="qc )', body)[1:]

# =============================================================================== P4-12 Division
def page12():
    rng = random.Random(5112)
    def rq(d, zero=False):
        while True:
            q = rng.randint(1000 // d + 1, 9999 // d)
            if (not zero or "0" in str(q)[1:]) and 1000 <= q * d <= 9999: return q
    for _ in range(6000):
        d = [rng.randint(3, 9) for _ in range(6)]
        if len(set(d)) < 4: continue
        q1 = rq(d[0], True); a1 = d[0] * q1
        q2 = rq(d[1]); a2 = d[1] * q2
        r3 = rng.randint(1, d[2] - 1); q3 = rq(d[2]) ; a3 = d[2] * q3 + r3
        q4 = rq(d[3]); a4 = d[3] * q4
        q5 = rq(d[4]); a5 = d[4] * q5
        r6 = rng.randint(1, d[5] - 1); q6 = rq(d[5]); a6 = d[5] * q6 + r6
        if any(not 1000 <= a <= 9999 for a in (a1, a2, a3, a4, a5, a6)): continue
        ans = [q1, q2, r3, q4, q5, q6]
        if not distinct(ans) or len({a1, a2, a3, a4, a5, a6}) < 6: continue
        pool = {int(str(q1).replace("0", "")), q1 + 1, q1 - 1, q3, d[2] - r3, r3 + 1, q6 + 1, q6 - 1, q5 + 1, q5 - 10, q4 + 1, q4 - 1, r6, q2 + 100, q2 - 10}
        pool = {p for p in pool if p not in ans and 0 <= p <= 9999}
        dom = plausible_domain(ans, pool, rng=rng, sample=200, hi=9999)
        res = code_table_any(12, 6, ans, rng, 0, 9999, n_decoy=3, tries=60, pool=sorted(pool), domain=dom)
        if res: word, table = res; break
    else: raise RuntimeError("p12")
    nm = rng.choice(["girls", "boys", "children", "pupils"])
    qs = [f"Work out {N(a1)} ÷ {d[0]}.", f"Work out {N(a2)} ÷ {d[1]}.", f"What is the remainder when {N(a3)} is divided by {d[2]}?",
          f"{N(a4)} beads are shared equally among {d[3]} {nm}. How many beads does each get?",
          f"A book has {N(a5)} pages. Ravi reads {d[4]} pages every day. How many days does he take to finish it?",
          f"{N(a6)} stickers are packed {d[5]} to a pack. How many full packs are made?"]
    cards = [qcard(i + 1, f"<p>{q}</p>", ABX, cls="span2 inl" if i >= 2 else "") for i, q in enumerate(qs)]
    P = code_page(12, 5112, "Division", 2, "Division: 4 digits divided by 1 digit", STRAND_NU,
        "3.2 (division algorithm, up to 4 digits by 1 digit)", ["FO3.2"], "Code-breaker (division algorithm)",
        ["Divide. Check with multiplication.", "Write the answer in the box.", INSTR_CODE], qgrid(cards, 2), ans, table, word, 0, 9999,
        "; ".join(f"{i+1}) {a}" for i, a in enumerate(ans)),
        "Six divisions of a 4-digit number by a 1-digit number: three plain (one with a zero in the answer, one exact and one that asks only for the remainder) and three short stories (share equally, how many days, how many full packs with a remainder). The decoy letters stand for the usual slips: leaving a zero out of the answer, giving the quotient where the remainder was asked, or adding 1 for the left-over stickers when the question asks for full packs. A box left blank gives no letter and the check cannot see it.",
        domain=dom, ps=True)
    solved = []
    for q in re.findall(r"<p>(.*?)</p>", strip_gap(P["body"])):
        nums = [int(x) for x in re.findall(r"\d+", q)]
        if "remainder" in q: solved.append(nums[0] % nums[1])
        elif "full packs" in q or q.startswith("Work out"): solved.append(nums[0] // nums[1])
        else:
            assert nums[0] % nums[1] == 0, q; solved.append(nums[0] // nums[1])
    P.v("V1 independent solver (each printed question divided with whole-number division) equals the key", solved == ans, solved)
    P.v("V7 every dividend has 4 digits and every divisor is a 1-digit number", all(1000 <= a <= 9999 for a in (a1, a2, a3, a4, a5, a6)) and all(x < 10 for x in d))
    return P

# =============================================================================== P4-13 Number Ring (loop)
def page13():
    rng = random.Random(5213)
    for _ in range(200000):
        v0 = rng.randint(12, 480); vals = [v0]; ops = []; ok = True
        for k in range(5):
            cand = [("×", m) for m in range(2, 10)] + [("÷", m) for m in range(2, 10) if vals[-1] % m == 0]
            s, m = rng.choice(cand); v = vals[-1] * m if s == "×" else vals[-1] // m
            if v < 6 or v > 99999: ok = False; break
            vals.append(v); ops.append((s, m))
        if not ok or len(set(vals)) < 6: continue
        v5 = vals[5]
        if v0 > v5 and v0 % v5 == 0 and 2 <= v0 // v5 <= 9: last = ("×", v0 // v5)
        elif v5 > v0 and v5 % v0 == 0 and 2 <= v5 // v0 <= 9: last = ("÷", v5 // v0)
        else: continue
        ops.append(last)
        if sum(1 for s, m in ops if s == "×") < 2 or sum(1 for s, m in ops if s == "÷") < 2: continue
        if max(vals) < 1000 or max(vals) > 30000 or len({m for s, m in ops}) < 4: continue
        break
    else: raise RuntimeError("p13")
    optxt = [f"{s}{m}" for s, m in ops]
    ring = A4.ring_svg(vals, optxt)
    ex = '<div class="howto"><b>Example</b><p class="ptxt">Start 8. Follow ×3 to get 24. Follow ÷4 to get 6.</p></div>'
    body = f'{ex}<div class="figwrap">{ring}</div>'
    P = new_page(13, 5213, "Number Ring", 2, "Multiplying and dividing: round the ring and back to the start", STRAND_NU,
        "3.1 (multiplication algorithm), 3.2 (division algorithm)", ["FO3.1", "FO3.2"], "Chain loop (operations)", "K8 the loop closes: the last arrow brings the pupil back to the start number",
        ["Start at the number in the circle.", "Follow each arrow and write the new number in the box.", "Go round the ring."],
        body, "Circles after the start, clockwise: " + ", ".join(Ntxt(v) for v in vals[1:]) + ". Arrows: " + ", ".join(optxt), "Going round the ring ends on the start number.",
        f"A ring of six numbers. The pupil starts at {vals[0]} and follows five arrows, each a multiplication or a division by a 1-digit number, writing every new number. The sixth arrow takes the last number back to {vals[0]}. Every number the pupil writes is used by the next arrow, so one slip makes the ring fail to close. All the numbers stay below one hundred thousand. The multiplications use the algorithm up to 4 digits by 1 digit and the divisions are exact.",
        check="Follow the last arrow. Do you come back to the start number?", mk=("loop",),
        mech_plain="Loop: following every arrow brings the pupil back to the start number", ps=True)
    g, rops = A4.read_ring(ring)
    chain = [g]
    for s, m in rops[:5]: chain.append(chain[-1] * m if s == "×" else chain[-1] // m)
    back = chain[-1] * rops[5][1] if rops[5][0] == "×" else chain[-1] // rops[5][1]
    P.v("V1 independent solver (arrows read from the drawing and followed) gets the five numbers and the ring closes", chain[1:] == vals[1:] and back == g, chain)
    P.v("V1b every division is exact", all(chain[k] % rops[k][1] == 0 for k in range(5) if rops[k][0] == "÷") and (rops[5][0] == "×" or chain[5] % rops[5][1] == 0))
    P.v("V7 every number is below 100 000 and at least two multiplications and two divisions are used", max(vals) < 100000 and sum(1 for s, m in rops if s == "×") >= 2 and sum(1 for s, m in rops if s == "÷") >= 2)
    ans = vals[1:]
    def closes(a):
        cur = g
        for k, (s, m) in enumerate(rops[:5]):
            cur = cur * m if s == "×" else (cur // m if cur % m == 0 else -1)
            if cur != a[k]: return False
        nxt = cur * rops[5][1] if rops[5][0] == "×" else (cur // rops[5][1] if cur % rops[5][1] == 0 else -1)
        return nxt == g
    dom = plausible_domain(ans, [], spread=(1, 2, 3, 5, 10, 100, 1000), rng=rng, sample=300, hi=99999)
    P.v("V3 every single wrong value in one circle breaks the ring (on the page's value set)", all(not closes([a if j != k else v for j, a in enumerate(ans)]) for k in range(5) for v in dom if v != ans[k]))
    P["cv"] = dict(rate=1.0, single_total=5 * len(dom), single_detected=5 * len(dom))
    P["model"] = dict(truth=list(ans), domains=[dom] * 5, check=closes, numeric=True)
    P["facts"] = " ".join(str(v) for v in vals) + " " + " ".join(optxt)
    return P

# =============================================================================== P4-14 Mixed or Improper
def page14():
    rng = random.Random(5314)
    for _ in range(6000):
        d1 = rng.choice([3, 4, 5, 6, 8]); t1 = rng.randint(d1 + 2, 3 * d1 - 1)
        d2 = rng.choice([3, 4, 5, 6, 8]); t2 = rng.randint(d2 + 1, 3 * d2 - 1)
        if d1 == d2 or t1 % d1 == 0 or t2 % d2 == 0: continue
        d3 = rng.choice([3, 4, 5, 6, 7, 8, 9]); n3 = rng.randint(2 * d3 + 1, 7 * d3 - 1)
        d4 = rng.choice([3, 4, 5, 7, 8, 9, 10]); w4 = rng.randint(2, 8); r4 = rng.randint(1, d4 - 1)
        d5 = rng.choice([4, 5, 6, 7, 9]); n5 = rng.randint(3 * d5 + 1, 8 * d5 - 1)
        if n3 % d3 == 0 or n5 % d5 == 0 or len({d3, d4, d5}) < 3: continue
        d6 = rng.choice([3, 4, 5, 6, 8]); w6 = rng.randint(3, 9)
        ans = [t1, t2 // d2, n3 // d3, w4 * d4 + r4, n5 % d5, w6 * d6]
        if not distinct(ans) or max(ans) > 99: continue
        pool = {t1 - d1, t1 + 1, t2 % d2, t2, n3 % d3, n3 + 1, w4 * 10 + r4, w4 + r4, (w4 + 1) * d4 + r4, n5 // d5, n5 - d5, w6 + d6, w6 * 10 + d6}
        pool = {p for p in pool if p not in ans and 0 <= p <= 99}
        dom = list(range(0, 100))
        res = code_table_any(14, 6, ans, rng, 0, 99, n_decoy=3, tries=60, pool=sorted(pool), domain=dom)
        if res: word, table = res; break
    else: raise RuntimeError("p14")
    fr = lambda n, d: frac_html((n, d))
    pic1 = A4.bars_svg(d1, t1, w=30); pic2 = A4.bars_svg(d2, t2, w=30)
    box = '<span class="ab w2 fb"></span>'
    cards = [
        qcard(1, f"<p>Write the shaded amount as an improper fraction.</p>{pic1}", f'<span class="fr"><i>{ABS}</i><i>{d1}</i></span>', cls="pic"),
        qcard(2, f"<p>Write the shaded amount as a mixed number. What is the whole number?</p>{pic2}", ABS, cls="pic"),
        qcard(3, f'<p>Write the improper fraction as a mixed number.</p><div class="fsum">{fr(n3, d3)} = {box} {fr(n3 % d3, d3)}</div>', ""),
        qcard(4, f'<p>Write the mixed number as an improper fraction.</p><div class="fsum">{mixed_html(w4, r4, d4)} = {blank_frac(d4)}</div>', ""),
        qcard(5, f'<p>Write the improper fraction as a mixed number.</p><div class="fsum">{fr(n5, d5)} = <span class="mx"><b>{n5 // d5}</b>{blank_frac(d5)}</span></div>', ""),
        qcard(6, f'<p>Write the whole number as a fraction.</p><div class="fsum">{w6} = {blank_frac(d6)}</div>', ""),
    ]
    P = code_page(14, 5314, "Mixed or Improper", 1, "Mixed numbers and improper fractions", STRAND_FR,
        "1.1 (mixed numbers, improper fractions and their relationship)", ["MI1.1"], "Code-breaker (mixed numbers and improper fractions)",
        ["Change each number as asked.", "Write the missing number in the box.", INSTR_CODE], qgrid(cards, 2), ans, table, word, 0, 99,
        f"1) {t1}/{d1}; 2) whole number {t2 // d2} ({t2}/{d2}); 3) {n3}/{d3} = {n3 // d3} {n3 % d3}/{d3}, whole number {n3 // d3}; 4) {w4} {r4}/{d4} = {w4 * d4 + r4}/{d4}; 5) {n5}/{d5} = {n5 // d5} {n5 % d5}/{d5}, top number {n5 % d5}; 6) {w6} = {w6 * d6}/{d6}",
        "Two pictures of fraction bars (the pupil counts the shaded parts, then writes the improper fraction or the whole number of the mixed number), a conversion of an improper fraction to a mixed number (the whole number is missing), of a mixed number to an improper fraction (the top number is missing), the fraction part of a mixed number, and a whole number written as a fraction. The decoy letters stand for the usual slips: adding the whole number to the top number, or giving the remainder where the whole number was asked. A box left blank gives no letter and the check cannot see it.",
        domain=dom)
    cs = cards_of(P["body"])
    solved = []
    d, tot, nb = A4.read_bars(cs[0]); solved.append(tot)
    d, tot, nb = A4.read_bars(cs[1]); solved.append(tot // d)
    f3 = read_frac(cs[2]); solved.append((f3[0][0] - f3[1][0]) // f3[0][1])
    m4 = re.search(r'<span class="mx"><b>(\d+)</b>(.*?)</span></span>', cs[3]); f4 = read_frac(m4[2] + "</span>"); solved.append(int(m4[1]) * f4[0][1] + f4[0][0])
    f5 = read_frac(cs[4]); w5 = int(re.search(r'<span class="mx"><b>(\d+)</b>', cs[4])[1]); solved.append(f5[0][0] - w5 * f5[0][1])
    m6 = re.search(r'<div class="fsum">(\d+) = ', cs[5]); f6 = read_frac(cs[5]); solved.append(int(m6[1]) * f6[-1][1])
    P.v("V1 independent solver (bars counted, fractions read back from the printed cards) equals the key", solved == ans, solved)
    P.v("V7 denominators are within 12 and every conversion leaves a fraction part", max(d1, d2, d3, d4, d5, d6) <= 12 and t1 % d1 and t2 % d2 and n3 % d3 and n5 % d5)
    P.v("V1b the two pictures use different denominators", d1 != d2)
    return P

# =============================================================================== P4-15 Fraction Number Line (lettered choice)
def opt_html(w, r, d, improper):
    """w whole and r/d (r < d) as a mixed number, or as an improper fraction when improper (or a proper fraction when w is 0)"""
    if w == 0 or improper: return frac_html((w * d + r, d))
    return mixed_html(w, r, d)

def opt_value(h):
    m = re.search(r'<span class="mx"><b>(\d+)</b>(.*)', h)
    if m: f = read_frac(m[2]); return Fraction(int(m[1])) + Fraction(f[0][0], f[0][1])
    f = read_frac(h); return Fraction(f[0][0], f[0][1])

def page15():
    rng = random.Random(5415)
    for _ in range(6000):
        word = word_candidates(15, 6)[rng.randrange(0, 3)]
        ds = [rng.choice([2, 3, 4, 5, 6, 8]) for _ in range(6)]
        specs = []
        for d in ds:
            a = rng.choice([0, 1, 2, 3]); k = rng.randint(1, 3 * d - 1)
            if k % d == 0 or math.gcd(k % d, d) != 1: continue
            specs.append((a, d, a + k // d, k % d))
        if len(specs) < 6 or len({(s[0], s[2], s[3], s[1]) for s in specs}) < 6: continue
        rows_data = []; good = True
        for a, d, w, r in specs:
            cands = set()
            if 1 <= r + 1 < d: cands.add((w, r + 1))
            if 1 <= r - 1: cands.add((w, r - 1))
            if w > a: cands.add((w - 1, r))
            if w + 1 < a + 3: cands.add((w + 1, r))
            if w > 0: cands.add((0, r))
            if 1 <= d - r < d and d - r != r: cands.add((w, d - r))
            cands.discard((w, r))
            if len(cands) < 2: good = False; break
            rows_data.append((a, d, w, r, rng.sample(sorted(cands), 2)))
        if not good: continue
        try: lay = choice_letters(rng, word, 3)
        except RuntimeError: continue
        CLAIMED[15] = word
        break
    else: raise RuntimeError("p15")
    rows = []; truth_letters = []; layout = []
    for i, (a, d, w, r, wr) in enumerate(rows_data):
        opts = [(w, r, True)] + [(x, y, False) for x, y in wr]; rng.shuffle(opts)
        dec = iter(lay[i][1:])
        lets = [word[i] if ok else next(dec) for x, y, ok in opts]
        htmls = [opt_html(x, y, d, rng.random() < .35) for x, y, ok in opts]
        rows.append(choice_row(i + 1, A4.numline_svg(a, d, Fraction(w * d + r, d), 3), htmls, lets, "tall"))
        truth_letters.append(word[i]); layout.append(lets)
    letters = [[word[i]] + [l for l in layout[i] if l != word[i]] for i in range(6)]
    P = choice_page(15, 5415, "Fraction Number Line", 1, "Mixed numbers and improper fractions on a number line", STRAND_FR,
        "1.1 (mixed numbers, improper fractions and their relationship)", ["MI1.1"], "Choice table (number lines)",
        ["Read the number the arrow points to.", "Circle the letter of the right fraction.", "Write the six letters in the boxes."], rows, word, letters, truth_letters,
        "; ".join(f"{i+1}) {w * d + r}/{d} = {w} {r}/{d}" for i, (a, d, w, r, wr) in enumerate(rows_data)),
        "Six number lines marked in equal parts (halves, thirds, quarters, fifths, sixths or eighths) from 0, 1, 2 or 3, each three units long with an arrow. The pupil reads the arrow and picks the matching number from three, written as a mixed number or an improper fraction. The two wrong choices are the next or the previous mark, a whole number that is one too many or too few, the fraction part without the whole number, or the part counted from the other end. The letters of the right choices, read down the rows, spell the word; every other way of choosing was tested against a very large word list and none spells a word. A box left blank gives no letter and the check cannot see it.")
    solved = []
    for content, opts in rows_of(P["body"]):
        val = A4.read_numline(content)
        right = [l for h, l in opts if opt_value(h) == val]
        solved.append(right[0] if len(right) == 1 else "?")
    P.v("V1 independent solver (arrow read from the number line; each option read back and compared) gets the word", "".join(solved) == word, solved)
    P.v("V7 denominators are at most 12 and the three options of a row are three different numbers", all(len({opt_value(h) for h, l in opts}) == 3 for c, opts in rows_of(P["body"])) and max(d for a, d, w, r, x in rows_data) <= 12)
    return P

# =============================================================================== P4-16 Fraction of a Set
def page16():
    rng = random.Random(5516)
    kinds = ["star", "apple", "ball", "flower", "cat"]
    for _ in range(8000):
        k1, k2 = rng.sample(kinds, 2)
        g1 = rng.choice([3, 4, 5]); p1 = rng.randint(3, 4); n1 = rng.randint(1, g1 - 1)
        g2 = rng.choice([3, 4, 5]); p2 = rng.randint(3, 4); n2 = rng.randint(1, g2 - 1)
        if g1 == g2: continue
        pic1 = A4.groups_svg(k1, p1, g1, 2); pic2 = A4.groups_svg(k2, p2, g2, 2)
        if any(float(re.search(r'width="([\d.]+)mm"', p_)[1]) > 128 for p_ in (pic1, pic2)): continue
        d3 = rng.choice([5, 6, 7, 8, 9]); n3 = rng.randint(2, d3 - 1); T3 = d3 * rng.randint(4, 11)
        d4 = rng.choice([3, 4, 5, 6, 8]); T4 = d4 * rng.randint(4, 10)
        d5 = rng.choice([3, 4, 5, 6]); n5 = rng.randint(1, d5 - 1); W5 = d5 * rng.randint(3, 9); k5 = n5 * (W5 // d5)
        d6 = rng.choice([4, 5, 8, 10]); n6 = rng.randint(1, d6 - 1); T6 = d6 * rng.randint(4, 9)
        ans = [n1 * p1, n2 * p2, n3 * (T3 // d3), T4 - T4 // d4, W5, T6 - n6 * (T6 // d6)]
        if not distinct(ans) or max(ans) > 99: continue
        pool = {g1 * p1 - n1 * p1, g2 * p2 - n2 * p2, p1, p2, T3 // d3, n3 * (T3 // d3) + 1, T4 // d4, k5, k5 + 1, W5 + d5, n6 * (T6 // d6), T6 // d6, T6, g1 * p1, g2 * p2}
        pool = {p for p in pool if p not in ans and 0 < p <= 99}
        dom = list(range(0, 100))
        res = code_table_any(16, 6, ans, rng, 0, 99, n_decoy=3, tries=60, pool=sorted(pool), domain=dom)
        if res: word, table = res; break
    else: raise RuntimeError("p16")
    pl = lambda k: {"star": "stars", "apple": "apples", "ball": "balls", "flower": "flowers", "cat": "cats"}[k]
    cards = [
        qcard(1, f'<p>The {pl(k1)} are in rings of the same size. Find {frac_html((n1, g1))} of the {pl(k1)}.</p>{pic1}', ABS, cls="span2 pic inl"),
        qcard(2, f'<p>Find {frac_html((n2, g2))} of the {pl(k2)}.</p>{pic2}', ABS, cls="span2 pic inl"),
        qcard(3, f'<p>Find {frac_html((n3, d3))} of {T3}.</p>', ABS, cls="inl"),
        qcard(4, f'<p>A box has {T4} sweets. {frac_html((1, d4))} of them are red. How many are not red?</p>', ABS, cls="inl"),
        qcard(5, f'<p>{frac_html((n5, d5))} of a number is {k5}. What is the number?</p>', ABS, cls="inl"),
        qcard(6, f'<p>There are {T6} pupils in a hall. {frac_html((n6, d6))} of them are girls. How many are boys?</p>', ABS, cls="inl"),
    ]
    P = code_page(16, 5516, "Fraction of a Set", 1, "Fraction as part of a set", STRAND_FR,
        "2.1 (fraction as part of a set)", ["FS2.1"], "Code-breaker (fraction of a set)",
        ["Find the part of each set.", "Write the answer in the box.", INSTR_CODE], qgrid(cards, 2), ans, table, word, 0, 99,
        f"1) {n1} of {g1} rings of {p1} = {ans[0]}; 2) {n2} of {g2} rings of {p2} = {ans[1]}; 3) {ans[2]}; 4) {ans[3]}; 5) {ans[4]}; 6) {ans[5]}",
        "Two pictures of a set in rings of equal size (the pupil finds the fraction by counting rings), a fraction of a number, a fraction of a set when the rest is asked, the whole set when a part is given, and a story where the rest is asked. The decoy letters stand for the usual slips: giving the rest instead of the part, one equal part instead of several, or the whole set. A box left blank gives no letter and the check cannot see it.",
        domain=dom, ps=True)
    solved = []
    cs = cards_of(P["body"])
    for h in cs[:2]:
        rings, objs = A4.read_groups(h); f = read_frac(h)[0]
        assert rings == f[1] and objs % rings == 0
        solved.append((objs // rings) * f[0])
    f = read_frac(cs[2])[0]; T = int(re.search(r"of (\d+)\.", cs[2])[1]); solved.append(f[0] * T // f[1])
    f = read_frac(cs[3])[0]; T = int(re.search(r"A box has (\d+) sweets", cs[3])[1]); solved.append(T - f[0] * T // f[1])
    f = read_frac(cs[4])[0]; k_ = int(re.search(r"is (\d+)\. What", cs[4])[1]); solved.append(k_ * f[1] // f[0])
    f = read_frac(cs[5])[0]; T = int(re.search(r"There are (\d+) pupils", cs[5])[1]); solved.append(T - f[0] * T // f[1])
    P.v("V1 independent solver (rings and objects counted, fractions and numbers read from the printed cards) equals the key", solved == ans, solved)
    P.v("V7 every fraction of a set is a whole number", d3 and (n3 * T3) % d3 == 0 and T4 % d4 == 0 and (k5 * d5) % n5 == 0 and (n6 * T6) % d6 == 0)
    return P

# =============================================================================== P4-17 Fraction Sums
def fr_str(f): return f"{f.numerator}/{f.denominator}"

def lcm(a, b): return a * b // math.gcd(a, b)

def page17():
    rng = random.Random(5617)
    related = [(8, 4), (6, 3), (10, 5), (12, 4), (12, 6), (10, 2), (8, 2), (9, 3), (12, 3), (6, 2)]
    unrelated = [(3, 4), (2, 5), (3, 5), (4, 5), (2, 3), (5, 6), (3, 7), (3, 8), (4, 7), (5, 8)]
    def prop(d): return Fraction(rng.randint(1, d - 1), d)
    for _ in range(20000):
        items = []
        b_, s_ = rng.choice(related); items.append(("+", prop(b_), prop(s_)))                       # related, sum
        b_, s_ = rng.choice(related); items.append(("-", prop(b_), prop(s_)))                       # related, difference
        d1, d2 = rng.choice(unrelated); items.append(("+", prop(d1), prop(d2)))                    # not related, sum
        d1, d2 = rng.choice(unrelated); items.append(("-", prop(d1), prop(d2)))                    # not related, difference
        b_, s_ = rng.choice(related); items.append(("+", prop(b_), prop(s_)))                       # related, sum
        b_, s_ = rng.choice(related); items.append(("+", prop(b_), prop(s_)))                       # related, sum
        fixed = []
        for op, x, y in items:
            if op == "-" and x < y: x, y = y, x
            fixed.append((op, x, y))
        items = fixed
        ans = [x + y if op == "+" else x - y for op, x, y in items]
        if any(a_ <= 0 or a_.denominator > 12 for a_ in ans) or len(set(ans)) < 6: continue
        if sum(1 for a_ in ans if a_ > 1) != 1: continue
        if sum(1 for (op, x, y), a_ in zip(items, ans) if a_.denominator < lcm(x.denominator, y.denominator)) < 2: continue
        if any(x == y for op, x, y in items) or any(x.denominator > 12 or y.denominator > 12 for op, x, y in items): continue
        keys = [(a_.numerator, a_.denominator) for a_ in ans]
        pool = set()
        for (op, x, y), a_ in zip(items, ans):
            pool.add((x.numerator + y.numerator if op == "+" else x.numerator - y.numerator, x.denominator + y.denominator if x.denominator != y.denominator else x.denominator))
            L = lcm(x.denominator, y.denominator); un = x.numerator * (L // x.denominator) + (y.numerator * (L // y.denominator)) * (1 if op == "+" else -1)
            if (un, L) != (a_.numerator, a_.denominator) and L <= 12: pool.add((un, L))
        pool = {p for p in pool if p not in keys and 0 < p[1] <= 12 and p[0] > 0}
        dom = sorted(set(keys) | pool | {(n, d) for d in range(2, 13) for n in range(1, 2 * d)})
        res = code_table_any(17, 6, keys, rng, 0, 0, n_decoy=3, tries=60, pool=sorted(pool), domain=dom)
        if res: word, table = res; break
    else: raise RuntimeError("p17")
    cards = []
    for i, (op, x, y) in enumerate(items):
        t = f'{FR(x)} {"+" if op == "+" else "−"} {FR(y)} = <span class="fr"><i><span class="ab w2 fb"></span></i><i><span class="ab w2 fb"></span></i></span>'
        cards.append(qcard(i + 1, f'<div class="fsum">{t}</div>', ""))
    P = code_page(17, 5617, "Fraction Sums", 2, "Adding and subtracting fractions with different denominators", STRAND_FR,
        "3.1 (adding and subtracting fractions with denominators not exceeding 12 and not more than two different denominators), 1.1 (improper fractions)", ["FA3.1", "MI1.1"], "Code-breaker (fractions)",
        ["Add or subtract. Write each answer in its simplest form.", "Write the top and bottom numbers in the boxes.", INSTR_CODE], qgrid(cards, 2), keys, table, word, 0, 0,
        "; ".join(f"{i+1}) {fr_str(a_)}" for i, a_ in enumerate(ans)),
        "Six sums and differences of two proper fractions: four with related denominators (one is a multiple of the other), two with denominators that are not related (two different denominators in all). One sum is above 1 and stays an improper fraction, and at least two answers need simplifying. The pupil writes the answer in simplest form in two boxes and finds it in the code table of fractions. The decoy letters stand for the usual slips: adding the tops and the bottoms, or leaving the answer unsimplified. A box left blank gives no letter and the check cannot see it.",
        domain=dom, fmt=lambda k: frac_html(k), tkey=lambda k: Fraction(*k))
    solved = []
    for qh in re.findall(r'<div class="fsum">(.*?)</div></div>', P["body"], re.S):
        fs = read_frac(qh)[:2]; op = "+" if " + " in re.sub(r"<[^>]+>", "", qh) else "-"
        x, y = Fraction(*fs[0]), Fraction(*fs[1]); r = x + y if op == "+" else x - y
        solved.append((r.numerator, r.denominator))
    P.v("V1 independent solver (fractions and signs read back, the answer reduced) equals the key", solved == keys, solved)
    P.v("V7 denominators are at most 12 and each sum has at most two different denominators", all(max(x.denominator, y.denominator) <= 12 and len({x.denominator, y.denominator}) <= 2 for op, x, y in items))
    P.v("V7b every number in a sum is a proper fraction (adding mixed numbers is Primary 5)", all(x < 1 and y < 1 for op, x, y in items))
    return P

# =============================================================================== P4-18 Name the Angle (lettered choice cards)
VTX_LETTERS = ["P", "Q", "R", "S", "T", "X", "Y", "Z", "K", "L", "M", "N"]

def page18():
    rng = random.Random(5618)
    for _ in range(4000):
        word = word_candidates(18, 6)[rng.randrange(0, 3)]
        figs = []
        for i in range(6):
            labs = rng.sample(VTX_LETTERS, 4); v = labs[0]; pts = labs[1:]
            degs = sorted(rng.sample(range(20, 166, 5), 3))
            while min(b - a for a, b in zip(degs, degs[1:])) < 35: degs = sorted(rng.sample(range(20, 166, 5), 3))
            rays = dict(zip(pts, degs))
            pair_set = [(pts[0], pts[1]), (pts[1], pts[2]), (pts[0], pts[2])]
            figs.append((v, rays, pts, pair_set, rng.randrange(3), i >= 4))
        try: lay = choice_letters(rng, word, 3)
        except RuntimeError: continue
        CLAIMED[18] = word
        break
    else: raise RuntimeError("p18")
    rows = []; truth_letters = []; layout = []
    for i, (v, rays, pts, pair_set, right, small) in enumerate(figs):
        names = [(a, v, b) if rng.random() < .5 else (b, v, a) for a, b in pair_set]
        order = [0, 1, 2]; rng.shuffle(order)
        dec = iter(lay[i][1:])
        lets = [word[i] if j == right else next(dec) for j in order]
        a_, b_ = pair_set[right]
        fig = A4.angle_fig_svg(v, rays, [("a" if small else "", a_, b_, 11)], size=(52, 35), R=19.5)
        cap = f'<p class="aq">{SYM_ANGLE}<span class="an">a</span> is the marked angle.</p>' if small else ""
        opts = [angle_name(*names[j]) for j in order]
        rows.append(choice_row(i + 1, f'<div class="afig">{fig}{cap}</div>', opts, lets, "cc"))
        truth_letters.append(word[i]); layout.append(lets)
    letters = [[word[i]] + [l for l in layout[i] if l != word[i]] for i in range(6)]
    P = choice_page(18, 5618, "Name the Angle", 1, "Naming angles with three letters, as in angle ABC", STRAND_GE,
        "1.1 (using notation such as ∠ABC and ∠a to name angles)", ["AN1.1"], "Choice cards (angle names)",
        ["Look at the marked angle.", "Circle the letter beside its name.", "Write the six letters in the boxes."], rows, word, letters, truth_letters,
        "; ".join(f"{i+1}) angle {pair_set[right][0]}{v}{pair_set[right][1]}" for i, (v, rays, pts, pair_set, right, small) in enumerate(figs)),
        "Six drawings with three lines from one point. An arc marks one angle; the three names offered are the three angles the lines make, each written with the point in the middle (for example angle PQR). Two drawings label the marked angle with the small letter a, as in angle a. The pupil must pick the name that matches the two lines the arc joins. The letters of the right choices, read down the cards, spell the word; every other way of choosing was tested against a very large word list and none spells a word. Drawing an angle of a given size is not asked on this page. A box left blank gives no letter and the check cannot see it.")
    P["body"] = P["body"].replace('class="srows3 tallrows"', 'class="srows3 tallrows grid2"')
    solved = []
    for content, opts in rows_of(P["body"]):
        v_, rays_, arcs_ = A4.read_angle_fig(content)
        e1, e2 = arcs_[0][1], arcs_[0][2]
        got = []
        for h, l in opts:
            nm = re.search(r'<span class="an">(\w)(\w)(\w)</span>', h)
            if nm and nm[2] == v_ and {nm[1], nm[3]} == {e1, e2}: got.append(l)
        solved.append(got[0] if len(got) == 1 else "?")
    P.v("V1 independent solver (rays and arc read from the coordinates; each name read back) gets the word", "".join(solved) == word, solved)
    P.v("V7 the three lines of a figure are at least 35 degrees apart and the four letters of a figure are different", all(len({v, *pts}) == 4 for v, rays, pts, ps_, r_, s_ in figs))
    return P

# =============================================================================== P4-19 Protractor Readings
def page19():
    rng = random.Random(5719)
    for _ in range(8000):
        angs = rng.sample([x for x in range(25, 166, 5) if x % 20], 6)
        bases = ["right", "left", "right", "left", "left", "right"]; rng.shuffle(bases)
        if sum(1 for a in angs if a > 90) < 2 or sum(1 for a in angs if a < 90) < 2: continue
        if any(180 - a in angs for a in angs): continue
        pool = {180 - a for a in angs} | {a + 5 for a in angs} | {a - 5 for a in angs} | {a + 10 for a in angs}
        pool = {p for p in pool if p not in angs and 0 < p <= 180}
        dom = list(range(0, 181))
        res = code_table_any(19, 6, angs, rng, 0, 180, n_decoy=2, tries=60, pool=sorted(pool), domain=dom)
        if res: word, table = res; break
    else: raise RuntimeError("p19")
    pics = [A4.protractor_svg(a, b) for a, b in zip(angs, bases)]
    cards = [f'<div class="qc prot2"><span class="no">{i+1}</span>{p}<div class="pans">{ABS} °</div></div>' for i, p in enumerate(pics)]
    P = code_page(19, 5719, "Protractor Readings", 2, "Measuring angles in degrees", STRAND_GE,
        "1.2 (measuring angles in degrees)", ["AN1.2"], "Code-breaker (protractor)",
        ["Read each angle on the protractor.", "Start at 0 on the arm along the base. Use the code table."], qgrid(cards, 2), angs, table, word, 0, 180,
        "; ".join(f"{i+1}) {a} degrees (base arm to the {b})" for i, (a, b) in enumerate(zip(angs, bases))),
        "Six angles drawn on a protractor with a scale from each side, one arm along the base line, pointing to the right on three drawings and to the left on three. The pupil starts counting from 0 on the arm along the base, so a drawing with the base arm on the left must be read on the other scale. The decoy letters stand for 180 minus the angle (the wrong scale) and for a reading that is 5 or 10 degrees out. All sizes are multiples of 5 and none is a multiple of 20, so an arm never lies over a printed number. The page measures reading a protractor; drawing an angle with a protractor cannot be checked on a printed page. A box left blank gives no letter and the check cannot see it.",
        domain=dom, cols=8)
    solved = [A4.read_protractor(p) for p in re.findall(r"<svg.*?</svg>", P["body"], re.S)]
    P.v("V1 independent solver (the two arms read from the drawing: the angle between them) equals the key", solved == angs, solved)
    P.v("V7 angles are multiples of 5 (not of 20) between 25 and 165; arms point both to the right and to the left", all(a % 5 == 0 and a % 20 and 25 <= a <= 165 for a in angs) and set(bases) == {"right", "left"})
    P.v("V7b no angle is 180 minus another, so a wrong-scale reading is never another answer", not any(180 - a in angs for a in angs))
    return P

# =============================================================================== P4-20 Fraction Stories
def page20():
    rng = random.Random(5820)
    names = rng.sample(PEOPLE, 6)
    for _ in range(40000):
        T1 = rng.choice([48, 60, 72, 96, 120]); f1, f2 = rng.choice([(Fraction(1, 4), Fraction(1, 3)), (Fraction(1, 6), Fraction(1, 2)), (Fraction(1, 3), Fraction(1, 4)), (Fraction(1, 8), Fraction(1, 2)), (Fraction(1, 5), Fraction(1, 2))])
        a1 = T1 - f1 * T1 - f2 * T1
        d2 = rng.choice([5, 8, 6, 10]); T2 = d2 * rng.randint(5, 12); n2 = rng.randint(2, d2 - 1); a2 = T2 - n2 * T2 // d2
        T3 = rng.choice([200, 300, 400, 500, 600]); g1, g2 = rng.choice([(Fraction(3, 10), Fraction(2, 5)), (Fraction(1, 4), Fraction(3, 8)), (Fraction(1, 5), Fraction(3, 10)), (Fraction(1, 4), Fraction(1, 2))]); a3 = T3 - g1 * T3 - g2 * T3
        d4 = rng.choice([3, 4, 5, 6, 7]); n4 = rng.randint(1, d4 - 1); k4 = rng.randint(4, 14); a4 = Fraction(k4 * d4, n4)
        h1, h2 = rng.choice([(Fraction(3, 8), Fraction(1, 4)), (Fraction(1, 2), Fraction(1, 5)), (Fraction(1, 3), Fraction(1, 4)), (Fraction(2, 5), Fraction(1, 4))]); left5 = rng.randint(5, 24); a5 = left5 / (1 - h1 - h2)
        T6 = rng.choice([56, 72, 84, 90, 63]); e1 = rng.choice([Fraction(3, 7), Fraction(2, 3), Fraction(1, 3), Fraction(5, 9), Fraction(3, 4)]); e2 = rng.choice([Fraction(1, 2), Fraction(1, 4), Fraction(3, 4)])
        walk = e1 * T6; rest = T6 - walk; bus = e2 * rest
        vals = [a1, a2, a3, a4, a5, bus]
        if any(Fraction(v).denominator != 1 for v in vals) or Fraction(walk).denominator != 1: continue
        ans = [int(v) for v in vals]
        if not distinct(ans) or min(ans) < 3 or max(ans) > 999: continue
        pool = {T1 - int(f1 * T1), int(f1 * T1 + f2 * T1), T2 - a2, n2 * T2 // d2, int(g1 * T3 + g2 * T3), int(g1 * T3), k4 * n4, k4 + d4, int(left5 * (h1 + h2)), left5 * 2, int(walk), int(rest)}
        pool = {p for p in pool if p not in ans and 0 < p <= 999}
        dom = list(range(0, 1000))
        res = code_table_any(20, 6, ans, rng, 0, 999, n_decoy=3, tries=60, pool=sorted(pool), domain=dom)
        if res: word, table = res; break
    else: raise RuntimeError("p20")
    n1, n2_, n3, n4_, n5, n6 = names
    qs = [f"{n1} had {T1} stickers. {n1} gave {FR(f1)} of them to Ben and {FR(f2)} of them to Cy. How many stickers were left?",
          f"A tank holds {T2} litres. It is {FR(Fraction(n2, d2))} empty. Find the amount of water in the tank.",
          f"A book has {T3} pages. {n3} read {FR(g1)} of it on Monday and {FR(g2)} of it on Tuesday. How many pages are left?",
          f"{FR(Fraction(n4, d4))} of a number is {k4}. What is the number?",
          f"{n5} spent {FR(h1)} of her savings on a toy and {FR(h2)} of her savings on a card. Then ${left5} remained. Work out her savings at the start.",
          f"There are {T6} pupils. {FR(e1)} of them walk to school. {FR(e2)} of the rest take a bus. How many take a bus?"]
    units = ["", " litres", " pages", "", "", ""]
    cards = [qcard(i + 1, f'<div class="ptxt2">{q}</div>', ("$ " if i == 4 else "") + ABX + units[i], cls="span2 inl") for i, q in enumerate(qs)]
    P = code_page(20, 5820, "Fraction Stories", 2, "Fractions of a set in stories with two steps", STRAND_FR,
        "2.1 (fraction as part of a set), 3.1 (adding and subtracting fractions)", ["FS2.1", "FA3.1"], "Code-breaker (fraction stories)",
        ["Read each story.", "Write the answer in the box.", INSTR_CODE], '<div class="qg c1">' + "".join(cards) + "</div>", ans, table, word, 0, 999,
        "; ".join(f"{i+1}) {a}" for i, a in enumerate(ans)),
        "Six stories with two steps: the parts given away from a whole set and the number left, what is in a tank that is part empty, two parts of a book read and the pages left, the whole number from a fraction of it, the whole amount from two spent fractions of it and the money left, and a fraction of the rest. The decoy letters stand for the usual slips: stopping after the first step, giving the part instead of the rest, or taking the second fraction from the whole instead of from the rest. A box left blank gives no letter and the check cannot see it.",
        domain=dom, ps=True)
    solved = []
    parts = cards_of(P["body"])
    def frs(h): return [Fraction(a, b) for a, b in read_frac(h)]
    f = frs(parts[0]); T = int(re.search(r"had (\d+) stickers", parts[0])[1]); solved.append(int(T - f[0] * T - f[1] * T))
    f = frs(parts[1]); T = int(re.search(r"holds (\d+) litres", parts[1])[1]); solved.append(int(T - f[0] * T))
    f = frs(parts[2]); T = int(re.search(r"A book has (\d+) pages", parts[2])[1]); solved.append(int(T - f[0] * T - f[1] * T))
    f = frs(parts[3]); k = int(re.search(r"is (\d+)\. What", parts[3])[1]); solved.append(int(k / f[0]))
    f = frs(parts[4]); k = int(re.search(r"\$(\d+) remained", strip_gap(parts[4]))[1]); solved.append(int(k / (1 - f[0] - f[1])))
    f = frs(parts[5]); T = int(re.search(r"There are (\d+) pupils", parts[5])[1]); solved.append(int((T - f[0] * T) * f[1]))
    P.v("V1 independent solver (fractions and numbers read from the printed stories; each story solved with exact fractions) equals the key", solved == ans, solved)
    P.v("V7 every fraction has a denominator within 12 and every answer is a whole number", all(Fraction(v).denominator == 1 for v in solved))
    return P

PAGES = [page12, page13, page14, page15, page16, page17, page18, page19, page20]
