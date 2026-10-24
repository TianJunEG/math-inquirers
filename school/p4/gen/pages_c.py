"""Wave C: decimals (P4-21 to P4-26), area and perimeter (P4-27 to P4-30). P4-40 is colour by code.
Each pageNN() makes the puzzle from a seed, re-solves it with separate solver code that reads the PRINTED html or drawing, and gives validate.py a `model`."""
import random, re, math, itertools
from fractions import Fraction
from .common import *
from .kit import *
from .kit4 import *
from . import art4 as A4
from . import art5 as A5
from shapely.geometry import Polygon

ABX = '<span class="ab w4"></span>'
ABS = '<span class="ab w3"></span>'
FR = lambda f: frac_html((f.numerator, f.denominator))

def cards_of(body):
    return re.split(r'(?=<div class="qc )', body)[1:]

def dstr(v, places=None): return dec_str(Fraction(v), places)

def dec_domain(answers, pool, rng, n=180):
    """the decimals a pupil could write, as canonical strings: the answers, the slips, and a sample of other decimals up to 20"""
    d = {dstr(a) for a in answers} | {dstr(p) for p in pool}
    for _ in range(n):
        p = rng.choice([0, 1, 2, 3]); d.add(dstr(Fraction(rng.randint(0, 2000 * 10 ** p), 10 ** p)))
    return sorted(d, key=Fraction)

def places(v):
    v = Fraction(v)
    for p in range(0, 5):
        if (v * 10 ** p).denominator == 1: return p
    return 9

def slips(v):
    """decimals a pupil might write instead of v: the point moved, a zero dropped, two digits swapped"""
    s = dstr(v); digs = s.replace(".", ""); pt = s.index(".") if "." in s else len(s); out = set()
    for k in range(0, len(digs) + 1): out.add(Fraction(int(digs), 10 ** (len(digs) - k)))
    if "0" in digs:
        d2 = digs.replace("0", "", 1); out.add(Fraction(int(d2), 10 ** max(len(d2) - pt, 0)))
    for i in range(len(digs) - 1):
        t = list(digs); t[i], t[i + 1] = t[i + 1], t[i]; out.add(Fraction(int("".join(t)), 10 ** (len(digs) - pt)))
    out.discard(Fraction(v))
    return {x for x in out if x > 0}

def round_half_up(x, p):
    q = Fraction(x) * 10 ** p
    return Fraction(int((q + Fraction(1, 2)) // 1), 10 ** p)

def dec_code_table(no, rng, answers, pool, dom, n_decoy=3):
    keys = [dstr(a) for a in answers]
    poolk = sorted({dstr(p) for p in pool if dstr(p) not in keys}, key=Fraction)
    return code_table_any(no, 6, keys, rng, 0, 0, n_decoy=n_decoy, tries=60, pool=poolk, domain=dom), keys

# =============================================================================== P4-21 Decimal Place Value
def dec_table(o, t, h, th):
    heads = ["Ones", "", "Tenths", "Hundredths", "Thousandths"]
    return ('<table class="pvt4 dect"><tr>' + "".join(f"<th>{x}</th>" for x in heads) + "</tr><tr>"
            + f"<td>{o}</td><td class='pt'>.</td><td>{t}</td><td>{h}</td><td>{th}</td></tr></table>")

def page21():
    rng = random.Random(6121)
    for _ in range(8000):
        o, t, h, th = rng.randint(1, 9), rng.randint(0, 9), rng.randint(1, 9), rng.randint(1, 9)
        a1 = Fraction(o * 1000 + t * 100 + h * 10 + th, 1000)
        n2 = Fraction(rng.randint(1000, 9999), 1000); s2 = dstr(n2, 3); a2 = Fraction(int(s2[3]))
        n3 = Fraction(rng.randint(1000, 9999), 1000); s3 = dstr(n3, 3); k3 = rng.choice([2, 3, 4]); d3 = int(s3[k3]); a3 = Fraction(d3, 10 ** (k3 - 1))
        n4 = Fraction(rng.randint(11, 99), 1000); a4 = Fraction(int(n4 * 1000))
        x5 = rng.randint(1, 9); y5 = rng.randint(1, 9); a5 = Fraction(x5, 10) + Fraction(y5, 1000)
        n6 = Fraction(rng.randint(101, 999), 100); hund = int(n6 * 100) % 100
        if hund == 0: continue
        a6 = Fraction(hund)
        ans = [a1, a2, a3, a4, a5, a6]
        keys = [dstr(a) for a in ans]
        if len(set(keys)) < 6 or s3.count(str(d3)) != 1 or s2.count(s2[3]) != 1 or d3 == 0: continue
        pool = set()
        for a in ans: pool |= slips(a)
        pool |= {Fraction(o) + Fraction(h, 10) + Fraction(th, 100), Fraction(o) + Fraction(t, 10) + Fraction(h, 100)}
        pool = {p_ for p_ in pool if p_ > 0 and dstr(p_) not in keys}
        dom = dec_domain(ans, pool, rng)
        res = dec_code_table(21, rng, ans, pool, dom)[0]
        if res: word, table = res; break
    else: raise RuntimeError("p21")
    cards = [
        qcard(1, f"<p>Write the number shown in the chart.</p>{dec_table(o, t, h, th)}", ABX, cls="span2 inl"),
        qcard(2, f"<p>In {s2}, which digit is in the hundredths place?</p>", ABS),
        qcard(3, f"<p>What is the value of the digit {d3} in {s3}?</p>", ABX),
        qcard(4, f"<p>How many thousandths are in {dstr(n4, 3)}?</p>", ABX),
        qcard(5, f"<p>Write {x5} tenth{"s" if x5 != 1 else ""} and {y5} thousandth{"s" if y5 != 1 else ""} as a decimal.</p>", ABX),
        qcard(6, f"<p>{dstr(n6, 2)} is {int(n6)} ones and how many hundredths?</p>", ABX),
    ]
    P = code_page(21, 6121, "Decimal Place Value", 1, "Decimals: tenths, hundredths and thousandths", STRAND_DE,
        "1.1 (notation, representations and place values: tenths, hundredths, thousandths)", ["DP1.1"], "Code-breaker (decimal place value)",
        ["Work out each item.", "Write the answer in the box.", INSTR_CODE], qgrid(cards, 2), keys, table, word, 0, 0,
        "; ".join(f"{i+1}) {k}" for i, k in enumerate(keys)),
        "A place-value chart of ones, tenths, hundredths and thousandths, the digit in the hundredths place, the value of a digit as a decimal, the number of thousandths in a decimal, tenths and thousandths written as one decimal (the empty hundredths place needs a zero) and the number of hundredths after the ones. Answers are written without a final zero. The decoy letters stand for the usual slips: a zero left out, the decimal point put in the wrong place, or the digit instead of its value. A box left blank gives no letter and the check cannot see it.",
        domain=dom, fmt=lambda k: k, tkey=lambda k: Fraction(k))
    cs = cards_of(P["body"]); solved = []
    td = re.findall(r"<td[^>]*>([\d.]+)</td>", cs[0]); solved.append(dstr(Fraction(int(td[0]) * 1000 + int(td[2]) * 100 + int(td[3]) * 10 + int(td[4]), 1000)))
    m = re.search(r"In ([\d.]+), which digit is in the hundredths place", cs[1]); solved.append(m[1].split(".")[1][1])
    m = re.search(r"value of the digit (\d) in ([\d.]+)\?", cs[2]); solved.append(dstr(Fraction(int(m[1]), 10 ** (m[2].index(m[1]) - m[2].index(".")))))
    m = re.search(r"thousandths are in ([\d.]+)\?", cs[3]); solved.append(str(int(Fraction(m[1]) * 1000)))
    m = re.search(r"Write (\d) tenths? and (\d) thousandths?", cs[4]); solved.append(dstr(Fraction(int(m[1]), 10) + Fraction(int(m[2]), 1000)))
    m = re.search(r"([\d.]+) is (\d+) ones and how many hundredths", cs[5]); solved.append(str(int((Fraction(m[1]) - int(m[2])) * 100)))
    P.v("V1 independent solver (chart digits, place values and words read from the printed cards) equals the key", solved == keys, solved)
    P.v("V7 decimals have at most 3 decimal places and no decimal answer ends in a zero", all(not (k.endswith("0") and "." in k) for k in keys) and all(places(Fraction(x)) <= 3 for x in keys))
    P.v("V1b the digit asked about appears once in its number", s3.count(str(d3)) == 1 and s2.count(s2[3]) == 1)
    return P

# =============================================================================== P4-22 Order the Decimals
def dc_card(txt, letter):
    return f'<div class="dc"><b>{txt}</b><i class="cl">{letter}</i></div>'

def trap_set(rng, whole_lo=0, whole_hi=4):
    """three decimals with 1, 2 and 3 decimal places whose order by value is not the order by length and not the order of the digits read as whole numbers"""
    for _ in range(6000):
        w = rng.randint(whole_lo, whole_hi); vals = []
        for dp in rng.sample([1, 2, 3], 3):
            for _k in range(40):
                v = Fraction(w * 10 ** dp + rng.randint(0, 10 ** dp - 1), 10 ** dp)
                if places(v) == dp: vals.append(v); break
        if len(vals) != 3 or len(set(vals)) < 3: continue
        by_val = sorted(vals); by_len = sorted(vals, key=lambda v: (places(v), v)); by_int = sorted(vals, key=lambda v: int(dstr(v).replace(".", "")))
        if by_val != by_len and by_val != by_int and max(vals) - min(vals) < 1: return vals
    raise RuntimeError("trap set")

def page22():
    rng = random.Random(6222)
    for _ in range(2000):
        word = word_candidates(22, 6)[rng.randrange(0, 3)]
        A_ = trap_set(rng); B_ = trap_set(rng)
        if set(A_) & set(B_): continue
        orderA = sorted(A_); orderB = sorted(B_, reverse=True)
        lab = {}
        for i, v in enumerate(orderA + orderB): lab[("A" if i < 3 else "B", v)] = word[i]
        CLAIMED[22] = word
        break
    shA = A_[:]; rng.shuffle(shA); shB = B_[:]; rng.shuffle(shB)
    body = (f'<div class="blk"><p class="lead">Set A: smallest first.</p><div class="dcs big">{"".join(dc_card(dstr(v), lab[("A", v)]) for v in shA)}</div></div>'
            f'<div class="blk"><p class="lead">Set B: greatest first.</p><div class="dcs big">{"".join(dc_card(dstr(v), lab[("B", v)]) for v in shB)}</div></div>'
            f'<div class="blk"><p class="lead">Write the letters in order: Set A, then Set B.</p>{write_boxes(6)}</div>')
    P = new_page(22, 6222, "Order the Decimals", 1, "Comparing and ordering decimals up to 3 decimal places", STRAND_DE,
        "1.2 (comparing and ordering decimals)", ["DP1.2"], "Ordering (lettered decimal cards)", "K1 letters in order spell a word (6 letters) + each card used once",
        ["Put each set of decimals in order.", "Write the letter of each card in its place.", "Set A: smallest first. Set B: greatest first."],
        body, "Set A (smallest first): " + ", ".join(f"{lab[('A', v)]} = {dstr(v)}" for v in orderA) + "; Set B (greatest first): " + ", ".join(f"{lab[('B', v)]} = {dstr(v)}" for v in orderB), f"Word: {word}",
        "Two sets of three decimals with 1, 2 and 3 decimal places. In each set the order by value is not the order of length (the longest decimal is not always the greatest) and not the order of the digits read as whole numbers, so a pupil who compares only the digits goes wrong. Set A is read smallest first and Set B greatest first. The letters, read in the order asked, spell a word with exactly one arrangement that is a word, so no wrong order of the six cards spells a word (every wrong order was tested against a very large word list). A box left blank gives no letter and the check cannot see it.",
        check="Read the six letters in order. Do they spell a word?", mk=("logic",),
        mech_plain="Letters of the cards in the order asked spell a word (6 letters)")
    sections = re.split(r'<p class="lead">Set B', body)
    def cards(h): return [(Fraction(m[0]), m[1]) for m in re.findall(r'<div class="dc"><b>([\d.]+)</b><i class="cl">(\w)</i>', h)]
    a_s = sorted(cards(sections[0]), key=lambda c: c[0]); b_s = sorted(cards(sections[1]), key=lambda c: -c[0])
    solved = "".join(c[1] for c in a_s + b_s)
    P.v("V1 independent solver (decimals read back and sorted by value) gets the word", solved == word, solved)
    P.v("V3d the code word's letters have exactly ONE arrangement that is a word", anagrams(word) == [word.lower()])
    bad = no_wrong_order(word)
    P.v("V3 none of the 719 wrong orders of the six letters spells a word", not bad, bad[:3])
    P.v("V7 decimals have 1, 2 or 3 decimal places and are less than 5; no two cards are equal", all(0 <= v < 5 for v in A_ + B_) and len(set(A_ + B_)) == 6)
    P["cv"] = dict(rate=1.0, single_total=719, single_detected=719)
    P["model"] = dict(truth=list(word), domains=[sorted(set(word))] * 6, check=letters_check(), perm=list(range(6)))
    return P

# =============================================================================== P4-23 Fractions and Decimals (matching cards)
def page23():
    rng = random.Random(6323)
    FRACS = [(1, 2), (1, 4), (3, 4), (1, 5), (2, 5), (3, 5), (4, 5), (1, 10), (3, 10), (7, 10), (9, 10), (1, 20), (3, 20), (7, 20), (9, 20), (1, 25), (2, 25), (3, 25), (9, 25), (1, 50), (3, 50), (7, 50), (9, 100), (7, 100), (13, 100)]
    for _ in range(6000):
        word = word_candidates(23, 6)[rng.randrange(0, 3)]
        picks = rng.sample(FRACS, 6)
        vals = [Fraction(*p) for p in picks]
        if len(set(vals)) < 6: continue
        fd, df = picks[:3], picks[3:]                                     # fractions to decimals; decimals to fractions
        dec_right = vals[:3]; frac_right = [simplest(*p) for p in df]
        decoys_d = sorted({x for v in vals[:3] for x in slips(v) if places(x) <= 3 and x not in vals})
        decoys_f = []
        for v in vals[3:]:
            for s_ in slips(v):
                f_ = simplest(s_.numerator, s_.denominator)
                if 2 <= f_[1] <= 100 and Fraction(*f_) not in vals and Fraction(*f_) not in [Fraction(*x) for x in decoys_f]: decoys_f.append(f_)
        if len(decoys_d) < 2 or len(decoys_f) < 2: continue
        dd = rng.sample(decoys_d, 2); ff = rng.sample(decoys_f, 2)
        try: dl = letters_for_cards(rng, word, 4)
        except RuntimeError: continue
        CLAIMED[23] = word
        break
    else: raise RuntimeError("p23")
    poolA = [(v, word[i]) for i, v in enumerate(dec_right)] + [(v, dl[i]) for i, v in enumerate(dd)]
    poolB = [(f, word[3 + i]) for i, f in enumerate(frac_right)] + [(f, dl[2 + i]) for i, f in enumerate(ff)]
    shA = poolA[:]; rng.shuffle(shA); shB = poolB[:]; rng.shuffle(shB)
    rows = []
    for i, p in enumerate(fd):
        rows.append(f'<div class="mrow"><span class="no">{i+1}</span><span class="mq">{frac_html(p)} =</span><span class="mto">decimal card</span><span class="ab sm"></span></div>')
    for i, p in enumerate(df):
        rows.append(f'<div class="mrow"><span class="no">{i+4}</span><span class="mq">{dstr(Fraction(*p))} =</span><span class="mto">fraction card</span><span class="ab sm"></span></div>')
    cA = "".join(f'<div class="dc"><b>{dstr(v)}</b><i class="cl">{l}</i></div>' for v, l in shA)
    cB = "".join(f'<div class="dc">{frac_html(f)}<i class="cl">{l}</i></div>' for f, l in shB)
    body = (f'<div class="blk"><p class="lead">Decimal cards</p><div class="dcs five">{cA}</div></div><div class="blk"><p class="lead">Fraction cards</p><div class="dcs five">{cB}</div></div>'
            f'<div class="blk"><p class="lead">Write the letter of the matching card.</p><div class="mrows">{"".join(rows)}</div></div>')
    P = new_page(23, 6323, "Decimal Match", 1, "Writing fractions as decimals and decimals as fractions", STRAND_DE,
        "1.3 (expressing decimals as fractions), 1.4 (expressing fractions as decimals when the denominator is a factor of 10 or 100)", ["DP1.3", "DP1.4"], "Matching (fraction cards and decimal cards)",
        "K1 letters of the matching cards spell a word (6 letters), 4 decoy cards", ["Match each fraction to a decimal card.", "Match each decimal to a fraction card.", "Write the letter of the card in the box."],
        body, "; ".join(f"{i+1}) {p[0]}/{p[1]} = {dstr(Fraction(*p))} (card {word[i]})" for i, p in enumerate(fd + df)), f"Word: {word}",
        "Rows 1 to 3 give a fraction whose denominator is a factor of ten or of one hundred and ask for the matching decimal card; rows 4 to 6 give a decimal and ask for the matching fraction card (in simplest form). Each set has five cards: three that match and two decoys made by slips such as moving the decimal point. The letters of the matching cards, read down the six rows, spell the word. A decoy in any row gives a letter that does not spell a word (tested against a very large word list). A box left blank gives no letter and the check cannot see it.",
        check="Write the six letters in order. Do they spell a word?", check_boxes=6, mk=("code",), mech_plain="Word from the letters of the matching cards (6 letters)")
    decA = {Fraction(m[0]): m[1] for m in re.findall(r'<div class="dc"><b>([\d.]+)</b><i class="cl">(\w)</i>', body)}
    fracB = {}
    for m in re.finditer(r'<div class="dc"><span class="fr"><i>(\d+)</i><i>(\d+)</i></span><i class="cl">(\w)</i>', body): fracB[Fraction(int(m[1]), int(m[2]))] = m[3]
    got = ""
    for m in re.finditer(r'<span class="mq"><span class="fr"><i>(\d+)</i><i>(\d+)</i></span> =</span>', body): got += decA[Fraction(int(m[1]), int(m[2]))]
    for m in re.finditer(r'<span class="mq">([\d.]+) =</span>', body): got += fracB[Fraction(m[1])]
    P.v("V1 independent solver (each fraction and decimal read back and matched by value) gets the word", got == word, got)
    P.v("V3d the code word's letters have exactly ONE arrangement that is a word", anagrams(word) == [word.lower()])
    all_letters = sorted(set(word) | set(dl))
    bad_single = [(i, c) for i in range(6) for c in all_letters if c != word[i] and (word[:i] + c + word[i + 1:]).lower() in BIG]
    P.v("V3 no single wrong card in any row spells a word (large word list)", not bad_single, bad_single[:3])
    bad = no_wrong_order(word)
    P.v("V3e none of the 719 wrong orders of the six letters spells a word", not bad, bad[:3])
    P.v("V7 every denominator is a factor of 100 and every decimal has at most 2 decimal places", all(100 % d == 0 for n, d in fd + df) and all(places(Fraction(*p)) <= 2 for p in fd + df))
    P["cv"] = dict(rate=1.0, single_total=6 * (len(all_letters) - 1), single_detected=6 * (len(all_letters) - 1))
    P["model"] = dict(truth=list(word), domains=[all_letters] * 6, check=letters_check(), perm=list(range(6)), numeric=False)
    P["facts"] = " ".join(f"{n}/{d}" for n, d in fd + df)
    return P

# =============================================================================== P4-24 Rounding Decimals (lettered choice)
def rounding_item(rng, p):
    """a decimal x with 1 or 2 more places than p; its rounding to p places; three wrong answers"""
    for _ in range(400):
        dp = p + rng.choice([1, 2] if p < 2 else [1])
        x = Fraction(rng.randint(10 ** dp + 1, 9 * 10 ** dp + 10 ** dp - 1), 10 ** dp)
        if places(x) != dp or (x * 10 ** p) % 1 == Fraction(1, 2): continue
        r = round_half_up(x, p)
        if p > 0 and places(r) != p: continue
        trunc = Fraction(int(x * 10 ** p), 10 ** p)
        wrongs = {trunc, trunc + Fraction(1, 10 ** p), round_half_up(x, p + 1), round_half_up(x, p - 1) if p else trunc + 2, trunc - Fraction(1, 10 ** p) if trunc > 1 else trunc + 3}
        wrongs = sorted(w for w in wrongs if w != r)
        if len(wrongs) >= 3: return x, r, rng.sample(wrongs, 3)
    raise RuntimeError("rounding item")

def page24():
    rng = random.Random(6424)
    PLACES = [0, 0, 1, 1, 2, 2]
    for _ in range(4000):
        word = word_candidates(24, 6)[rng.randrange(0, 3)]
        order = PLACES[:]; rng.shuffle(order)
        rows = [(p,) + rounding_item(rng, p) for p in order]
        if len({r[2] for r in rows}) < 6 or len({r[1] for r in rows}) < 6: continue
        try: lay = choice_letters(rng, word, 4)
        except RuntimeError: continue
        CLAIMED[24] = word
        break
    else: raise RuntimeError("p24")
    html_rows = []; truth_letters = []; layout = []
    for i, (p, x, r_, wr) in enumerate(rows):
        opts = [(r_, True)] + [(w, False) for w in wr]; rng.shuffle(opts)
        dec = iter(lay[i][1:]); lets = [word[i] if ok_ else next(dec) for v, ok_ in opts]
        what = {0: "the nearest whole number", 1: "1 decimal place", 2: "2 decimal places"}[p]
        html_rows.append(choice_row(i + 1, f'<span class="yq">Round {dstr(x)} to {what}.</span>', [dstr(v) for v, ok_ in opts], lets, "tall"))
        truth_letters.append(word[i]); layout.append(lets)
    letters = [[word[i]] + [l for l in layout[i] if l != word[i]] for i in range(6)]
    P = choice_page(24, 6424, "Rounding Decimals", 1, "Rounding decimals to a whole number, 1 and 2 decimal places", STRAND_DE,
        "1.5 (rounding decimals to the nearest whole number, 1 decimal place, 2 decimal places)", ["DP1.5"], "Choice table (rounding)",
        ["Round each decimal as asked.", "Circle the letter of the right answer.", "Write the six letters in the boxes."], html_rows, word, letters, truth_letters,
        "; ".join(f"{i+1}) {dstr(x)} to {['the nearest whole number', '1 decimal place', '2 decimal places'][p]} = {dstr(r_)}" for i, (p, x, r_, wr) in enumerate(rows)),
        "Six roundings: two to the nearest whole number, two to 1 decimal place and two to 2 decimal places. Each row offers four numbers: the right one and three slips (cut off instead of rounded, rounded the wrong way, or rounded to a different place). Numbers exactly half way are not used. The letters of the right choices, read down the rows, spell the word; every other way of choosing was tested against a very large word list and none spells a word. A box left blank gives no letter and the check cannot see it.")
    solved = []
    for content, opts in rows_of(P["body"]):
        m = re.search(r"Round ([\d.]+) to (the nearest whole number|1 decimal place|2 decimal places)\.", content)
        pl = {"the nearest whole number": 0, "1 decimal place": 1, "2 decimal places": 2}[m[2]]
        want = round_half_up(Fraction(m[1]), pl)
        right = [l for h, l in opts if Fraction(re.sub(r"<[^>]+>", "", h)) == want]
        solved.append(right[0] if len(right) == 1 else "?")
    P.v("V1 independent solver (each decimal rounded exactly from the printed question) gets the word", "".join(solved) == word, solved)
    P.v("V7 the four options of a row are four different numbers", all(len({Fraction(re.sub(r"<[^>]+>", "", h)) for h, l in opts}) == 4 for c, opts in rows_of(P["body"])))
    P.v("V7b the three kinds of rounding each appear twice", sorted(r[0] for r in rows) == PLACES)
    return P


# =============================================================================== P4-25 Decimal Magic Square (every line makes the same total)
LINES3 = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
LOSHU = [2, 7, 6, 9, 5, 1, 4, 3, 8]

def solve_lines(cells, S):
    """independent solver: cells = 9 Fractions or None; every line of three adds to S. Returns the solution list when it is unique, else None"""
    unk = [i for i, c in enumerate(cells) if c is None]
    rows = []
    for ln in LINES3:
        coef = [Fraction(1) if i in ln else Fraction(0) for i in unk]; rhs = Fraction(S) - sum(cells[i] for i in ln if cells[i] is not None)
        rows.append(coef + [rhs])
    r = 0
    for c in range(len(unk)):
        piv = next((k for k in range(r, len(rows)) if rows[k][c] != 0), None)
        if piv is None: return None
        rows[r], rows[piv] = rows[piv], rows[r]
        rows[r] = [x / rows[r][c] for x in rows[r]]
        for k in range(len(rows)):
            if k != r and rows[k][c] != 0: rows[k] = [a - rows[k][c] * b for a, b in zip(rows[k], rows[r])]
        r += 1
    if any(all(x == 0 for x in row[:-1]) and row[-1] != 0 for row in rows): return None
    out = list(cells)
    for k, i in enumerate(unk): out[i] = rows[k][-1]
    return out

def page25():
    rng = random.Random(6525)
    for _ in range(4000):
        d = rng.choice([Fraction(1, 20), Fraction(3, 20), Fraction(1, 4), Fraction(7, 20), Fraction(1, 10) * 3]); a = Fraction(rng.randint(5, 140), 100)
        base = LOSHU[:]
        for _t in range(rng.randrange(4)): base = [base[6], base[3], base[0], base[7], base[4], base[1], base[8], base[5], base[2]]     # turn a quarter
        if rng.random() < .5: base = [base[2], base[1], base[0], base[5], base[4], base[3], base[8], base[7], base[6]]                 # mirror
        full = [a + d * k for k in base]; S = 3 * a + 15 * d
        if any(places(v) > 2 for v in full + [S]) or places(S) == 0: continue
        givens = rng.sample(range(9), 4)
        cells = [full[i] if i in givens else None for i in range(9)]
        sol = solve_lines(cells, S)
        if sol is None or sol != full: continue
        if 4 in givens: continue                                 # the middle number is S divided by 3, so it is left for the pupil
        blanks = [i for i in range(9) if i not in givens]
        keys = [dstr(full[i]) for i in blanks]
        if len(set(keys)) < 5: continue
        break
    else: raise RuntimeError("p25")
    cells_h = ""
    for i in range(9):
        cells_h += f'<div class="mq3">{dstr(full[i]) if i in givens else "<span class=\'ab w4 mb\'></span>"}</div>'
    body = f'<div class="msqwrap"><div class="msq">{cells_h}</div></div>'
    P = new_page(25, 6525, "Magic Decimals", 2, "Adding and subtracting decimals up to 2 decimal places", STRAND_DE,
        "2.1 (adding and subtracting decimals, up to 2 decimal places)", ["DA2.1"], "Magic square (decimals)", "K3 every row, column and corner-to-corner line makes the same total",
        [f"Every row, every column and both corner-to-corner lines make {dstr(S)}.", "Fill in the five empty boxes.", "Write each decimal in its box."],
        body, "Empty boxes, row by row: " + ", ".join(keys), f"Every line makes {dstr(S)}.",
        f"A 3 by 3 square of decimals with 4 numbers given and 5 empty boxes. Every row, every column and both corner-to-corner lines make {dstr(S)}. The pupil uses the total to find the missing numbers by adding and subtracting decimals (up to 2 decimal places). The middle number is never given. The solution was found by an independent solver and is the only one. Any single wrong number breaks at least two of the eight lines, so the check always shows a slip. A box left blank cannot add up.",
        check=f"Add each row, column and corner line. Does every line make {dstr(S)}?", mk=("total",),
        mech_plain="Total: all 3 rows, 3 columns and 2 corner-to-corner lines make the same total")
    # independent solver: read the printed cells and the total from the page
    read_cells = []
    for m in re.finditer(r'<div class="mq3">(.*?)</div>', body):
        t = m[1]; read_cells.append(None if "class='ab" in t or 'class="ab' in t else Fraction(t))
    S_read = Fraction(re.search(r"make ([\d.]+)\.", " ".join(P["instr"]))[1])
    sol = solve_lines(read_cells, S_read)
    unk = [i for i, c in enumerate(read_cells) if c is None]
    got = [dstr(sol[i]) for i in unk] if sol else None
    P.v("V1 independent solver (printed numbers and total, linear equations) finds exactly one solution and it equals the key", got == keys, got)
    def closes(ans):
        cur = list(read_cells)
        for i, v in zip(unk, ans):
            try: cur[i] = Fraction(v)
            except Exception: return False
        return all(sum(cur[i] for i in ln) == S_read for ln in LINES3)
    dom = dec_domain([full[i] for i in blanks], [], rng, n=300)
    dom = sorted(set(dom) | {dstr(Fraction(k, 100)) for k in range(0, 600, 5)})
    P.v("V2 the right answers make every line equal the total", closes(keys))
    wrong_ok = [(k, v) for k in range(5) for v in dom if v != keys[k] and closes([keys[j] if j != k else v for j in range(5)])]
    P.v("V3 every single wrong number in one box breaks at least one line", not wrong_ok, wrong_ok[:3])
    P.v("V7 all numbers are decimals with at most 2 decimal places and below 10; the middle number is not given", all(places(v) <= 2 and v < 10 for v in full) and 4 not in givens)
    P["cv"] = dict(rate=1.0, single_total=5 * len(dom), single_detected=5 * len(dom))
    P["model"] = dict(truth=list(keys), domains=[dom] * 5, check=closes, numeric=False)
    P["facts"] = " ".join(dstr(v) for v in full) + " " + dstr(S)
    P["mini"] = ""
    return P

# =============================================================================== P4-26 Decimal Products and Shares
def page26():
    rng = random.Random(6626)
    obj = rng.choice(["ribbon", "rope", "string", "plank"])
    for _ in range(40000):
        x1 = Fraction(rng.randint(105, 499), 100); d1 = rng.randint(3, 9); a1 = x1 * d1                      # decimal (2 places) times a 1-digit number
        d2 = rng.randint(3, 9); a2 = Fraction(rng.randint(105, 990), 100); x2 = a2 * d2                       # decimal divided by a 1-digit number
        m3 = 8; n3 = rng.randint(1, 30)                                                                      # whole number divided by 8: 3 decimal places
        a3 = Fraction(n3, m3)
        L4 = Fraction(rng.randint(60, 150), 10); d4 = rng.choice([4, 6, 8, 5]); a4 = L4 / d4                  # a length cut into equal pieces
        d5 = rng.choice([4, 5]); w5 = rng.randint(7, 60); a5 = Fraction(w5, d5)                               # whole number divided by 4 or 5
        d6 = rng.choice([3, 6, 7, 9]); w6 = rng.randint(5, 40); q6 = Fraction(w6, d6); a6 = round_half_up(q6, 1)   # a division rounded to 1 decimal place
        if places(x2) > 2 or places(a3) != 3 or places(L4) != 1 or places(a4) > 2 or places(a5) not in (1, 2) or places(q6) != 9 or places(a6) != 1: continue
        ans = [a1, a2, a3, a4, a5, a6]
        keys = [dstr(a) for a in ans]
        if len(set(keys)) < 6 or any(k.endswith("0") and "." in k for k in keys) or max(ans) > 90: continue
        pool = set()
        for a in ans: pool |= slips(a)
        pool |= {round_half_up(q6, 2), Fraction(int(q6 * 10), 10) + Fraction(1, 10), a1 + 1, a1 - 1, Fraction(d5, w5) if places(Fraction(d5, w5)) <= 3 else a5 + 1}
        pool = {p_ for p_ in pool if p_ > 0 and dstr(p_) not in keys}
        dom = dec_domain(ans, pool, rng)
        res = dec_code_table(26, rng, ans, pool, dom)[0]
        if res: word, table = res; break
    else: raise RuntimeError("p26")
    qs = [f"Work out {dstr(x1)} × {d1}.", f"Work out {dstr(x2)} ÷ {d2}.", f"Divide {n3} by {m3}. Write the answer as a decimal.",
          f"{dstr(L4)} m of {obj} is shared equally among {d4} children. How long is each share?", f"Divide {w5} by {d5}. Write the answer as a decimal.",
          f"Divide {w6} by {d6}. Round the answer to 1 decimal place."]
    cards = [qcard(i + 1, f"<p>{q}</p>", ABX + (" m" if i == 3 else ""), cls="span2 inl" if i in (2, 3, 5) else "") for i, q in enumerate(qs)]
    P = code_page(26, 6626, "Decimal Shares", 2, "Multiplying and dividing decimals by a 1-digit number", STRAND_DE,
        "3.1 (multiplying and dividing decimals by a 1-digit whole number), 3.2 (dividing a whole number by a whole number with a decimal quotient), 3.3 (rounding answers)", ["DM3.1", "DM3.2", "DM3.3"], "Code-breaker (decimal operations)",
        ["Work out each item.", "Write the answer in the box.", INSTR_CODE], qgrid(cards, 2), keys, table, word, 0, 0,
        "; ".join(f"{i+1}) {k}" for i, k in enumerate(keys)),
        "A decimal with 2 places times a 1-digit number, a decimal divided by a 1-digit number, a whole number divided by 8 (3 decimal places), a length cut into equal pieces, a whole number divided by 4 or 5 and a division that does not end, rounded to 1 decimal place. Answers are written without a final zero. The decoy letters stand for the usual slips: the decimal point put in the wrong place, the division the wrong way round, or the answer not rounded. A box left blank gives no letter and the check cannot see it.",
        domain=dom, fmt=lambda k: k, tkey=lambda k: Fraction(k), ps=True)
    solved = []
    for q in re.findall(r"<p>(.*?)</p>", P["body"]):
        nums = [Fraction(x) for x in re.findall(r"\d+(?:\.\d+)?", q.replace(" 1 decimal place", ""))]
        if "×" in q: solved.append(dstr(nums[0] * nums[1]))
        elif "Round the answer" in q: solved.append(dstr(round_half_up(nums[0] / nums[1], 1)))
        else: solved.append(dstr(nums[0] / nums[1]))
    P.v("V1 independent solver (each printed question worked out exactly, then rounded where asked) equals the key", solved == keys, solved)
    P.v("V7 decimals have at most 3 decimal places and every divisor is a 1-digit number", all(places(Fraction(k)) <= 3 for k in keys) and max(d1, d2, d4, d5, d6, m3) <= 9)
    return P


# =============================================================================== P4-27 Missing Sides
SQ = "²"

def rect_fig(W, H, label_side, qside, inner, unit_w=40.0):
    """a rectangle W by H cm drawn to scale (width unit_w mm); label_side: {side: text}; qside: sides marked ?"""
    unit = unit_w / W
    verts = [(0, 0), (W, 0), (W, H), (0, H)]
    names = {"top": 0, "right": 1, "bottom": 2, "left": 3}
    labels = {names[side]: txt for side, txt in label_side.items()}
    for side in qside: labels[names[side]] = "?"
    return A5.poly_svg(verts, unit, labels, inner), unit

def page27():
    rng = random.Random(6727)
    kinds = ["A", "B", "C", "D", "B", "A"]
    for _ in range(4000):
        order = kinds[:]; rng.shuffle(order)
        items = []; ans = []
        for k in order:
            if k == "A":
                while True:
                    w, l = rng.randint(4, 12), rng.randint(5, 16)
                    if w != l and 1.4 <= max(w, l) / min(w, l) <= 3: break
                items.append(("A", w, l, w * l)); ans.append(l)               # width given, area given: find the length
            elif k == "B":
                while True:
                    w, l = rng.randint(5, 14), rng.randint(8, 25)
                    if 1.4 <= max(w, l) / min(w, l) <= 3: break
                items.append(("B", w, l, 2 * (w + l))); ans.append(w)         # length given, perimeter given: find the width
            elif k == "C":
                s_ = rng.randint(5, 18); items.append(("C", s_, s_, 4 * s_)); ans.append(s_)
            else:
                s_ = rng.randint(4, 15); items.append(("D", s_, s_, s_ * s_)); ans.append(s_)
        if not distinct(ans) or len({it[3] for it in items}) < 6: continue
        pool = set()
        for k, w, l, v in items:
            pool |= {v // max(w, 1), v // 2 - w if k == "B" else v // 4, v - w, w + l, l * 2, v // 2, w * 2}
        pool = {p_ for p_ in pool if p_ not in ans and 0 < p_ <= 99}
        dom = list(range(0, 100))
        res = code_table_any(27, 6, ans, rng, 0, 99, n_decoy=3, tries=60, pool=sorted(pool), domain=dom)
        if res: word, table = res; break
    else: raise RuntimeError("p27")
    cards = []; texts = []
    for i, (k, w, l, v) in enumerate(items):
        if k == "A":
            fig, _ = rect_fig(l, w, {"left": f"{w} cm"}, ["bottom"], [(f"area {v} cm{SQ}", 0)], unit_w=25.0)
        elif k == "B":
            fig, _ = rect_fig(l, w, {"bottom": f"{l} cm"}, ["left"], [("perimeter", -2.4), (f"{v} cm", 2.4)], unit_w=30.0)
        elif k == "C":
            fig, _ = rect_fig(w, w, {}, ["bottom"], [("square", -4.5), ("perimeter", 0), (f"{v} cm", 4.5)], unit_w=26.0)
        else:
            fig, _ = rect_fig(w, w, {}, ["bottom"], [("square", -3), (f"area {v} cm{SQ}", 3)], unit_w=26.0)
        cards.append(qcard(i + 1, f'<div class="fgc">{fig}</div>', ABS + " cm", cls="inl fgq"))
    P = code_page(27, 6727, "Missing Sides", 1, "Finding a side of a rectangle or a square from its area or perimeter", STRAND_AP,
        "1.1 (finding one dimension of a rectangle given the other dimension and its area/perimeter), 1.2 (finding the length of one side of a square given its area/perimeter)", ["AP1.1", "AP1.2"], "Code-breaker (missing sides)",
        ["Find the side marked ?.", "Write its length in the box.", INSTR_CODE], qgrid(cards, 2), ans, table, word, 0, 99,
        "; ".join(f"{i+1}) {a} cm ({'rectangle, area' if k == 'A' else 'rectangle, perimeter' if k == 'B' else 'square, perimeter' if k == 'C' else 'square, area'} {v})" for i, ((k, w, l, v), a) in enumerate(zip(items, ans))),
        "Six figures drawn to scale: a rectangle with its area and one side given (find the other side), a rectangle with its perimeter and one side given, a square with its perimeter and a square with its area (find the side). The decoy letters stand for the usual slips: dividing the perimeter by 2 and stopping, using the perimeter as the area, or adding the two sides. A box left blank gives no letter and the check cannot see it. The figures are drawn to scale but a pupil is not asked to measure them.",
        domain=dom, ps=False)
    solved = []
    for h in re.findall(r'<svg.*?</svg>', P["body"], re.S):
        pts, dims, inner = A5.read_poly(h); lab = A5.side_labels(pts, dims)
        text = " ".join(t for t, x, y in inner)
        known = [(k_, re.fullmatch(r"(\d+) cm", t)) for k_, t in lab.items() if t != "?"]
        mv = [(k_, t) for k_, t in lab.items() if t == "?"]
        m = re.search(r"area (\d+)", text); mp = re.search(r"(\d+) cm", text.replace("perimeter", ""))
        if "square" in text:
            if "area" in text: solved.append(int(math.isqrt(int(m[1]))))
            else: solved.append(int(re.search(r"(\d+) cm", text)[1]) // 4)
        else:
            g = int(known[0][1][1])
            if "area" in text: solved.append(int(m[1]) // g)
            else: solved.append(int(re.search(r"perimeter (\d+)", text)[1]) // 2 - g)
    P.v("V1 independent solver (labels and the area or perimeter read from the drawing, then the formula used) equals the key", solved == ans, solved)
    P.v("V7 every side is a whole number of cm; areas and perimeters are within 650; sides are below 100", all(1 <= a <= 25 for a in ans) and all(it[3] <= 650 for it in items))
    return P

# =============================================================================== P4-28 L-Shapes (composite figures)
FS28 = 3.4

def make_figure(rng, kind):
    """a random rectilinear figure of the given kind with whole-number sides of at least 3 cm"""
    for _ in range(2000):
        if kind == "L":
            W, H = rng.randint(8, 13), rng.randint(6, 9); a, b = rng.randint(3, W - 3), rng.randint(3, H - 3); p = dict(W=W, H=H, a=a, b=b)
        elif kind == "T":
            W, H = rng.randint(9, 14), rng.randint(7, 10); t = rng.randint(3, 4); st = rng.randint(3, 4); x1 = rng.randint(3, (W - st) - 3) if W - st - 3 >= 3 else 3; p = dict(W=W, H=H, t=t, x1=x1, x2=x1 + st)
        elif kind == "U":
            W, H = rng.randint(9, 13), rng.randint(6, 9); a = rng.randint(3, 4); x1 = rng.randint(3, max(3, W - a - 3)); b = rng.randint(3, H - 3); p = dict(W=W, H=H, a=a, b=b, x1=x1)
        elif kind == "stair":
            W, H = rng.randint(10, 14), rng.randint(7, 10); w1 = rng.randint(3, 4); w2 = rng.randint(w1 + 3, W - 3); h1 = 3; h2 = rng.randint(h1 + 3, H - 3) if H - 3 >= h1 + 3 else None
            if h2 is None: continue
            p = dict(W=W, H=H, w1=w1, h1=h1, w2=w2, h2=h2)
        else: raise ValueError(kind)
        try: v = A5.shapes_verts(kind, **p)
        except KeyError: continue
        if all(A5.side_len(v, i) >= 3 for i in range(len(v))) and len(set(v)) == len(v): return v, p
    raise RuntimeError("figure")

def figure_card(rng, kind, tries=300):
    """a figure of this kind with every side labelled except one horizontal and one vertical side, and its labels clear of each other and of the figure.
    Returns (vertices, svg, omitted sides)"""
    for _ in range(tries):
        verts, p = make_figure(rng, kind)
        n = len(verts)
        hs = [i for i in range(n) if verts[i][1] == verts[(i + 1) % n][1]]; vs = [i for i in range(n) if verts[i][0] == verts[(i + 1) % n][0]]
        oh, ov = rng.choice(hs), rng.choice(vs)
        W = max(x for x, y in verts); H = max(y for x, y in verts)
        unit = min(34.0 / W, 24.0 / H, 4.2)
        labels = {i: A5.side_text(verts, i) for i in range(n) if i not in (oh, ov)}
        if A5.labels_clear(verts, unit, labels, FS28):
            return verts, A5.poly_svg(verts, unit, labels, None, fs=FS28), (oh, ov)
    raise RuntimeError("figure card")

def figure_value(h, what):
    """independent reader: the area (cm squared) or perimeter (cm) of a drawn figure, from the labels and the drawing"""
    pts, dims, inner = A5.read_poly(h); lab = A5.side_labels(pts, dims)
    lens = A5.figure_lengths(pts, lab)
    if what == "perimeter": return sum(lens)
    n = len(pts); mm = [math.dist(pts[i], pts[(i + 1) % n]) for i in range(n)]
    sc = {k: float(re.fullmatch(r"(\d+(?:\.\d+)?) cm", t)[1]) for k, t in lab.items()}
    k0 = next(iter(sc)); scale = mm[k0] / sc[k0]
    area_mm = Polygon(pts).area
    return Fraction(round(area_mm / scale ** 2, 4)).limit_denominator(10)

def page28():
    rng = random.Random(6828)
    plan = [("L", "area"), ("T", "perimeter"), ("U", "area"), ("stair", "perimeter"), ("L", "perimeter"), ("T", "area")]
    for _ in range(3000):
        items = []; ans = []; figs = []
        for kind, what in plan:
            v, svg_, om = figure_card(rng, kind)
            items.append((kind, what, v)); figs.append(svg_); ans.append(int(round(A5.poly_area(v))) if what == "area" else int(round(A5.poly_perim(v))))
        if not distinct(ans) or max(ans) > 400: continue
        pool = set()
        for (kind, what, v), a in zip(items, ans):
            W = max(x for x, y in v); H = max(y for x, y in v)
            pool |= {W * H, 2 * (W + H), a + 2, a - 2, a + 10, W + H, A5.poly_area(v) if what == "perimeter" else A5.poly_perim(v)}
        pool = {int(p_) for p_ in pool if int(p_) not in ans and 0 < p_ <= 400}
        dom = plausible_domain(ans, pool, rng=rng, sample=120, hi=400)
        res = code_table_any(28, 6, ans, rng, 0, 400, n_decoy=3, tries=60, pool=sorted(pool), domain=dom)
        if res: word, table = res; break
    else: raise RuntimeError("p28")
    cards = []
    for i, (kind, what, v) in enumerate(items):
        unit_txt = f"cm{SQ}" if what == "area" else "cm"
        cards.append(qcard(i + 1, f'<div class="fgc">{figs[i]}</div>', f'<div class="fq2">{what.capitalize()}:</div>' + ABS + " " + unit_txt, cls="inl fgq2"))
    P = code_page(28, 6828, "L-Shapes", 1, "Area and perimeter of figures made of rectangles", STRAND_AP,
        "1.3 (finding the area and perimeter of composite figures made up of rectangles and squares)", ["AP1.3"], "Code-breaker (composite figures)",
        ["Two sides are not marked. Find them first.", "Find the area or the perimeter.", INSTR_CODE], qgrid(cards, 2), ans, table, word, 0, 400,
        "; ".join(f"{i+1}) {what} = {a} ({kind} figure)" for i, ((kind, what, v), a) in enumerate(zip(items, ans))),
        "Six figures made of rectangles (two L-shapes, two T-shapes, a U-shape and a step shape), each with every side marked except one horizontal and one vertical side. The pupil finds the two missing sides, then the area (three figures) or the perimeter (three figures). The decoy letters stand for the usual slips: the area of the whole rectangle round the figure, the perimeter of that rectangle, or area and perimeter mixed up. A box left blank gives no letter and the check cannot see it. The figures are drawn to scale but a pupil is not asked to measure them.",
        domain=dom, ps=False)
    solved = []
    svgs = re.findall(r'<svg.*?</svg>', P["body"], re.S)
    for h, (kind, what, v) in zip(svgs, items): solved.append(int(figure_value(h, what)))
    P.v("V1 independent solver (labels read from the drawing, every other side measured with the scale of the labelled ones, area by the shoelace formula) equals the key", solved == ans, solved)
    P.v("V7 every figure is made of rectangles with whole-number sides and exactly two sides unmarked (one horizontal, one vertical)", all(len(re.findall(r'class="dim"', h)) == len(v) - 2 for h, (k, w, v) in zip(svgs, items)))
    P.v("V7b every side of every figure is at least 3 cm and the labels do not overlap one another or the figure", all(all(A5.side_len(v, i) >= 3 for i in range(len(v))) for k, w, v in items))
    return P


# =============================================================================== P4-29 Match the Figures
def page29():
    rng = random.Random(6933)
    kinds = ["L", "T", "U", "stair", "L", "T"]
    for _ in range(3000):
        figs = [figure_card(rng, k) for k in kinds]
        areas = [int(round(A5.poly_area(v))) for v, h, om in figs]; perims = [int(round(A5.poly_perim(v))) for v, h, om in figs]
        if len(set(areas + perims)) < 12 or max(areas) > 300: continue
        word = word_candidates(29, 6)[rng.randrange(0, 3)]
        metric = ["area", "perimeter"] * 3; rng.shuffle(metric)                  # the clue asked about figure j
        clue_order = list(range(6)); rng.shuffle(clue_order)                    # clue i is about figure clue_order[i]
        letter_of_fig = {clue_order[i]: word[i] for i in range(6)}
        CLAIMED[29] = word
        break
    else: raise RuntimeError("p29")
    figcards = ""
    for j, (v, h, om) in enumerate(figs):
        figcards += f'<div class="mfig"><i class="cl">{letter_of_fig[j]}</i><div class="fgc">{h}</div></div>'
    clues = []
    for i in range(6):
        j = clue_order[i]; m = metric[j]
        val = areas[j] if m == "area" else perims[j]
        clues.append(f'<div class="mrow"><span class="no">{i+1}</span><span class="mq2">{"Area" if m == "area" else "Perimeter"} {val} {"cm" + SQ if m == "area" else "cm"}</span><span class="ab sm"></span></div>')
    body = f'<div class="mfigs">{figcards}</div><div class="blk"><p class="lead">Write the letter of the figure for each clue.</p><div class="mrows2">{"".join(clues)}</div></div>'
    P = new_page(29, 6929, "Match the Figures", 2, "Area and perimeter of figures made of rectangles", STRAND_AP,
        "1.3 (finding the area and perimeter of composite figures made up of rectangles and squares)", ["AP1.3"], "Matching (clues to figures)",
        "K1 letters of the matching figures spell a word (6 letters), the letters are on the figures",
        ["Two sides of each figure are not marked.", "Find the area and the perimeter of each figure.", "Write the letter of the figure that fits each clue."],
        body, "; ".join(f"clue {i+1} ({'area' if metric[clue_order[i]] == 'area' else 'perimeter'} {areas[clue_order[i]] if metric[clue_order[i]] == 'area' else perims[clue_order[i]]}) -> figure {letter_of_fig[clue_order[i]]}" for i in range(6)), f"Word: {word}",
        "Six figures made of rectangles (L-shapes, T-shapes, a U-shape and a step shape), each with two sides not marked. The pupil finds the area and the perimeter of every figure, then matches six clues (three about an area and three about a perimeter) to the figures. The twelve numbers are all different, so each clue fits exactly one figure. The letters on the figures, read in the order of the clues, spell the word; a wrong match gives a letter that is another letter of the word, and no wrong order of the six letters spells a word (tested against a very large word list). A box left blank gives no letter and the check cannot see it. The figures are drawn to scale but a pupil is not asked to measure them.",
        check="Write the six letters in order. Do they spell a word?", mk=("code",), mech_plain="Word from the letters of the figures that fit the clues (6 letters)")
    figs_html = re.findall(r'<div class="mfig"><i class="cl">(\w)</i><div class="fgc">(<svg.*?</svg>)</div></div>', body, re.S)
    val = {}
    for letter, h in figs_html:
        val[letter] = (int(figure_value(h, "area")), int(figure_value(h, "perimeter")))
    got = ""
    for m in re.finditer(r'<span class="mq2">(Area|Perimeter) (\d+) cm', body):
        want = int(m[2]); idx = 0 if m[1] == "Area" else 1
        found = [l for l, v in val.items() if v[idx] == want]
        got += found[0] if len(found) == 1 else "?"
    P.v("V1 independent solver (every figure measured from its labels and drawing; each clue matched to the one figure that fits) gets the word", got == word, got)
    P.v("V3d the code word's letters have exactly ONE arrangement that is a word", anagrams(word) == [word.lower()])
    bad = no_wrong_order(word)
    P.v("V3 none of the 719 wrong orders of the six letters spells a word", not bad, bad[:3])
    P.v("V7 the six areas and six perimeters are twelve different numbers", len(set(areas + perims)) == 12)
    P["cv"] = dict(rate=1.0, single_total=719, single_detected=719)
    P["model"] = dict(truth=list(word), domains=[sorted(set(word))] * 6, check=letters_check(), perm=list(range(6)), numeric=False)
    P["facts"] = " ".join(str(x) for x in areas + perims)
    return P

# =============================================================================== P4-30 Joined Shapes (stories with rectangles and squares)
def page30():
    rng = random.Random(7030)
    for _ in range(40000):
        n1 = rng.choice([3, 4, 5]); s1 = rng.randint(3, 12); P1 = 2 * s1 * (n1 + 1); a1 = n1 * s1 * s1                     # squares joined in a row: perimeter given, find area
        A2, B2 = rng.randint(14, 24), rng.randint(9, 13); C2 = rng.randint(3, 6); a2 = 2 * (A2 + B2)                         # a square cut from a corner: perimeter left (unchanged)
        s3 = rng.choice([4, 5, 6, 8, 10]) * 2; P3 = 4 * s3 * 1; a3 = 4 * (s3 // 2)                                         # a square cut into 4 equal squares
        A4, B4 = rng.randint(12, 25), rng.randint(8, 15); a4 = (A4 + 4) * (B4 + 4) - A4 * B4                                 # a path 2 m wide round a garden
        L5, W5 = rng.randint(7, 14), rng.randint(3, 6); a5 = 2 * (L5 + 2 * W5)                                               # two rectangles joined along the long sides
        w6 = rng.randint(4, 12); P6 = 8 * w6; a6 = 3 * w6 * w6                                                              # length 3 times the width
        if L5 <= W5 or s3 % 2 or P1 == P3 or A4 == B4: continue
        ans = [a1, a2, a3, a4, a5, a6]
        if not distinct(ans) or max(ans) > 999 or min(ans) < 3: continue
        pool = {n1 * s1, 4 * s1, a2 - 2 * C2, A2 * B2 - C2 * C2 + 1, A2 * B2, A2 * B2 - C2 * C2, P3 // 2, 2 * (s3 // 2), s3 // 2, A4 * B4, (A4 + 4) * (B4 + 4), 2 * (L5 + W5), 2 * L5 + 2 * W5 * 2 - 4, L5 * 2 * W5, 3 * w6, 2 * (w6 + 3 * w6), 4 * w6 * w6}
        pool = {p_ for p_ in pool if p_ not in ans and 0 < p_ <= 999}
        dom = plausible_domain(ans, pool, rng=rng, sample=120, hi=999)
        res = code_table_any(30, 6, ans, rng, 0, 999, n_decoy=3, tries=60, pool=sorted(pool), domain=dom)
        if res: word, table = res; break
    else: raise RuntimeError("p30")
    qs = [f"{n1} identical squares are joined in a row to make a rectangle. Its perimeter is {P1} cm. Find its area.",
          f"A card is {A2} cm by {B2} cm. A corner piece, a square of side {C2} cm, is cut off. Find the perimeter of the card left.",
          f"A square has perimeter {P3} cm. It is cut into 4 identical small squares. Find the perimeter of one small square.",
          f"A pool is {A4} m long and {B4} m wide. Tiles 2 m wide surround it. Find the area of the tiles.",
          f"Two {L5} cm by {W5} cm tiles touch along their long sides. Find the perimeter of both together.",
          f"The length of a rectangle is 3 times its width. Its perimeter is {P6} cm. Find its area."]
    units = [f"cm{SQ}", "cm", "cm", f"m{SQ}", "cm", f"cm{SQ}"]
    cards = [qcard(i + 1, f'<div class="ptxt2">{q}</div>', ABX + " " + units[i], cls="span2 inl") for i, q in enumerate(qs)]
    P = code_page(30, 7030, "Joined Shapes", 2, "Area and perimeter when squares and rectangles are joined or cut", STRAND_AP,
        "1.3 (finding the area and perimeter of composite figures made up of rectangles and squares), 1.1 and 1.2 (missing sides)", ["AP1.1", "AP1.2", "AP1.3"], "Code-breaker (joined shapes)",
        ["Read each story. Draw the shape if it helps.", "Write the answer in the box.", INSTR_CODE], '<div class="qg c1">' + "".join(cards) + "</div>", ans, table, word, 0, 999,
        "; ".join(f"{i+1}) {a}" for i, a in enumerate(ans)),
        "Six stories about squares and rectangles that are joined, cut or put round another shape: identical squares in a row (find the side from the perimeter, then the area), a corner cut from a rectangle (the perimeter does not change), a square cut into four small squares, a path round a garden, two rectangles joined along their long sides and a rectangle whose length is 3 times its width. The decoy letters stand for the usual slips: giving the area when the perimeter was asked, forgetting that the cut corner leaves the perimeter the same, or using the width of the path once instead of twice. A box left blank gives no letter and the check cannot see it.",
        domain=dom, ps=True)
    solved = []
    for q in re.findall(r'<div class="ptxt2">(.*?)</div>', P["body"]):
        nums = [int(x) for x in re.findall(r"\d+", q)]
        if q.startswith("The length of a rectangle"): w = nums[1] // 8; solved.append(3 * w * w)
        elif "identical squares are joined in a row" in q: n, per = nums[0], nums[1]; s_ = per // (2 * (n + 1)); solved.append(n * s_ * s_)
        elif "corner piece" in q: solved.append(2 * (nums[0] + nums[1]))
        elif "cut into 4 identical" in q: solved.append(4 * (nums[0] // 4 // 2))
        elif "Tiles" in q: solved.append((nums[0] + 4) * (nums[1] + 4) - nums[0] * nums[1])
        else: solved.append(2 * (nums[0] + 2 * nums[1]))
    P.v("V1 independent solver (each printed story solved with the stated shapes) equals the key", solved == ans, solved)
    P.v("V7 every side is a whole number of cm or m and every answer is below 1000", all(a < 1000 for a in ans))
    return P

PAGES = [page21, page22, page23, page24, page25, page26, page27, page28, page29, page30]
