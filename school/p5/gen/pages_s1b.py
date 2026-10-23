"""Semester 1, part B (fractions): P5-08 Sharing Equally; P5-09 Fractions as Decimals; P5-10 Mixed Number Magic; P5-11 Mixed Number Route;
P5-12 Fraction Chain; P5-13 Fraction of a Quantity."""
import random, re, math, itertools
from fractions import Fraction as Fr
from .common import *
from .kit import *
from .kit5 import *

FM = lambda f: frac_val(f, True)       # a value as a whole number, a mixed number or a fraction

def txt_ints_outside_fractions(t):
    return [int(x) for x in re.findall(r"\d+", re.sub(r"⟨[^⟩]*⟩", " ", t.replace(NB, "")))]

# =============================================================================== P5-08 Sharing Equally (code word)
STORY8 = [("{n} metres of ribbon are cut into {m} equal pieces. How long is each piece?", "m"),
          ("{n} kg of rice is shared equally among {m} bowls. How much rice is in each bowl?", "kg"),
          ("{n} litres of juice are poured equally into {m} jugs. How much juice is in each jug?", "ℓ"),
          ("{n} pizzas are shared equally by {m} children. How much pizza does each child get?", "pizza")]

def pick8(rng, kd):
    """(n, m) for a division n / m: proper or improper, already in simplest form or needing it"""
    while True:
        m = rng.randint(3, 9) if not kd.endswith("_s") else rng.choice([4, 6, 8, 9, 10, 12])
        n = rng.randint(1, m - 1) if kd.startswith(("bare_p", "story_p")) else m + rng.randint(1, m - 1) if rng.random() < .7 else 2 * m + rng.randint(1, m - 1)
        g = math.gcd(n, m)
        if kd.endswith("_s"):
            if g in (2, 3) and n % m: return n, m
        elif g == 1 and n != m: return n, m

def page08():
    rng = random.Random(5108)
    spec = ["bare_p", "bare_p_s", "bare_i", "bare_i_s", "story_p", "story_i"]
    for _ in range(6000):
        items = [(kd,) + pick8(rng, kd) for kd in spec]
        ans = [Fr(n, m) for _, n, m in items]
        if not distinct(ans) or any(a.denominator == 1 for a in ans) or len({m for _, _, m in items}) < 5: continue
        pool = []
        for (kd, n, m), a in zip(items, ans):
            pool += [Fr(m, n), Fr(n % m, m) if n > m else Fr(1, m), Fr(n, m + 1), Fr(n // m) if n > m else Fr(n - 1, m)]
        pool = [p for p in dict.fromkeys(pool) if p not in ans and p > 0 and p.denominator <= 12]
        res = code_table_for(8, ans, rng, pool, n_decoy=2, tries=60)
        if res[0]: (word, table), dom = res; break
    else: raise RuntimeError("p08")
    cards = []; tmpl = rng.sample(STORY8, 2); ti = 0
    for i, (kd, n, m) in enumerate(items):
        if kd.startswith("bare"):
            content = f'<p class="qt big">{n} ÷ {m} = </p>'; unit = ""
        else:
            t, unit = tmpl[ti]; ti += 1
            content = f'<p class="qt">{t.format(n=n, m=m)}</p>'
        cards.append(qc(i + 1, content, ab_mixed() + (f'<span class="unit">{unit}</span>' if unit and unit != "pizza" else ""), cls="fr8"))
    solved = []
    for c in cards:
        t = to_text(re.search(r'<div class="qt">(.*?)</div></div><div class="qa">', c, re.S).group(1))
        nums = [int(x) for x in re.findall(r"\d+", t)]
        solved.append(Fr(nums[0], nums[1]))
    P = code_page(8, 5108, "Sharing Equally", 1, "Fractions: dividing a whole number by a whole number", STRAND_FR,
        "dividing a whole number by a whole number: the quotient as a fraction or a mixed number", ["FR1.1"], "Code-breaker (division as a fraction)",
        ["Divide. Write the answer as a fraction or a mixed number.", "Give each answer in its simplest form.", "Use the code table."],
        cards, ans, word, table, dom, FM, "; ".join(f"{i+1}) {frac_txt(a)}" for i, a in enumerate(ans)),
        "Six divisions where the quotient is a fraction or a mixed number: four bare divisions (two that need simplifying) and two sharing stories. The decoy letters stand for the usual slips: the fraction turned upside down, the whole number part only, or the remainder only. A box left blank gives no letter and the check cannot see it.",
        solved, cols=4, layout="c2", checks=[("V7 no quotient is a whole number; divisors at most 12", all(a.denominator > 1 for a in ans) and all(m <= 12 for _, _, m in items), "")])
    return P

# =============================================================================== P5-09 Fractions as Decimals (matching)
CAND9 = [Fr(1, 2), Fr(1, 4), Fr(3, 4), Fr(1, 5), Fr(2, 5), Fr(3, 5), Fr(4, 5), Fr(1, 8), Fr(3, 8), Fr(5, 8), Fr(7, 8), Fr(1, 20), Fr(3, 20), Fr(7, 20), Fr(9, 20),
         Fr(11, 20), Fr(1, 25), Fr(3, 25), Fr(9, 25), Fr(12, 25), Fr(1, 40), Fr(3, 40), Fr(7, 50), Fr(1, 50), Fr(3, 50)]

def page09():
    rng = random.Random(5109)
    for _ in range(5000):
        word = word_candidates(9, 6)[0]
        pr = rng.sample(CAND9, 4)
        mixed = [rng.choice([1, 2]) + f for f in rng.sample([f for f in CAND9 if f.denominator in (4, 8, 20, 5, 25)], 2)]
        vals = pr + mixed
        if not distinct(vals) or len({f.denominator for f in vals}) < 4: continue
        # the tiles are in order of value; decimals must have at most 3 places
        break
    order = sorted(vals)
    pairs = [(frac_val(v, False) if v < 1 else frac_val(v, True), dec(v)) for v in order]
    P = match_page(9, 5109, "Fractions as Decimals", 1, "Fractions: expressing fractions as decimals", STRAND_FR,
        "expressing fractions as decimals", ["FR1.2"], "Matching (lettered cards)",
        ["Write each fraction as a decimal.", "Find the tile with that decimal.", "Write the card's letter in the box under the tile."],
        rng, pairs, word, "; ".join(f"{w}: {frac_txt(v)} = {dec(v)}" for w, v in zip(word, order)),
        "Six cards with fractions and mixed numbers (denominators 2, 4, 5, 8, 20, 25, 40 and 50) and six tiles with decimals of one, two or three places, in order of size. A pupil finds each decimal by dividing the numerator by the denominator or by making an equivalent fraction with denominator 10, 100 or 1000. The letters, read from tile 1 to tile 6, spell a word with exactly one arrangement that is a word, so no wrong matching spells a word. A box left blank gives no letter and the check cannot see it.",
        lambda t: evaluate(t), lambda t: evaluate(t), left_title="Cards",
        checks=[("V7 every decimal has at most 3 decimal places and every fraction has a denominator of 2 to 50", all(len(dec(v).partition(".")[2]) <= 3 and v.denominator <= 50 for v in order), "")])
    return P

# =============================================================================== P5-10 Mixed Number Magic (K3)
LS = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
def transforms(g):
    out = []
    for flip in (False, True):
        h = [r[::-1] for r in g] if flip else g
        for _ in range(4):
            h = [list(r) for r in zip(*h[::-1])]; out.append(h)
    return out
LINES = [[(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)], [(0, 0), (1, 0), (2, 0)], [(0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)],
         [(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 0)]]

def propagate(grid, S):
    """fill empty cells (None) by a line with exactly one empty cell; returns the full grid or None (the independent solver of the page)"""
    g = [list(r) for r in grid]
    while True:
        changed = False
        for ln in LINES:
            empty = [c for c in ln if g[c[0]][c[1]] is None]
            if len(empty) == 1:
                g[empty[0][0]][empty[0][1]] = S - sum(g[r][c] for r, c in ln if (r, c) != empty[0]); changed = True
        if not changed: break
    return g if all(x is not None for r in g for x in r) else None

def page10():
    rng = random.Random(5110)
    for _ in range(3000):
        fam = rng.choice(["q", "q", "t"])
        step = rng.choice([Fr(3, 4), Fr(5, 4), Fr(7, 4), Fr(1, 4) * 5, Fr(3, 2)]) if fam == "q" else rng.choice([Fr(2, 3), Fr(4, 3), Fr(5, 3), Fr(7, 3)])
        base = rng.choice([Fr(1, 4), Fr(1, 2), Fr(3, 4), Fr(1, 1)]) if fam == "q" else rng.choice([Fr(1, 3), Fr(2, 3), Fr(1, 1)])
        T = rng.choice(transforms(LS))
        M = [[base + step * T[i][j] for j in range(3)] for i in range(3)]
        S = 3 * base + 15 * step
        if max(max(r) for r in M) > 14 or sum(1 for r in M for x in r if x.denominator > 1) < 6: continue
        cells = [(i, j) for i in range(3) for j in range(3)]
        given = rng.sample(cells, 4)
        grid = [[M[i][j] if (i, j) in given else None for j in range(3)] for i in range(3)]
        full = propagate(grid, S)
        if full is None or full != M: continue
        unk = [c for c in cells if c not in given]
        if len({M[i][j] for i, j in unk}) < 5: continue
        break
    else: raise RuntimeError("p10")
    cellh = []
    for i in range(3):
        for j in range(3):
            if M[i][j] is not None and (i, j) in given: cellh.append(f'<div class="mq3">{FM(M[i][j])}</div>')
            else: cellh.append(f'<div class="mq3 blank"><span class="mxa">{ab_mixed()}</span></div>')
    body = ('<div class="msq" data-s="1">' + "".join(cellh) + '</div>'
            f'<p class="lead" style="text-align:center;margin-top:3mm">Every row, every column and both long diagonals make <em class="msum">{FM(S)}</em></p>')
    truth = [M[i][j] for i, j in unk]
    P = new_page(10, 5110, "Mixed Number Magic", 2, "Fractions: adding and subtracting mixed numbers", STRAND_FR,
        "adding and subtracting mixed numbers", ["FR2.1"], "Magic square (mixed numbers)", "K3 check-sum: every row, column and diagonal makes the printed total",
        ["Fill the empty squares with whole or mixed numbers.", "Every row, every column and both long diagonals make the same total.", "The total is printed under the square."],
        body, "Empty squares, row by row: " + ", ".join(frac_txt(v) for v in truth) + ". Full square: " + " / ".join(" ".join(frac_txt(x) for x in r) for r in M), f"Every line makes {frac_txt(S)}.",
        "A 3 by 3 magic square with mixed numbers in quarters and halves (or in thirds). Four squares are given and the total of every line is printed. Each empty square is found by subtracting the numbers already in a line from the total, one line at a time; every empty square can be reached this way. The check is the total: a wrong number makes at least one of the eight lines wrong. All numbers in the square are different.",
        check=f"Add each row, column and diagonal. Does every line make {frac_txt(S)}?", mk=("total",), ps=False,
        mech_plain="Total: all eight lines of the square must make the printed total")
    # independent reader: read the printed grid and the printed total, then propagate
    gh = re.findall(r'<div class="mq3( blank)?">(.*?)</div>(?=<div class="mq3|</div><p)', body, re.S)
    rd = []
    for blank, h in gh:
        rd.append(None if blank else evaluate(to_text(h)))
    S_read = evaluate(to_text(re.search(r'<em class="msum">(.*?)</em>', body, re.S).group(1)))
    full = propagate([rd[0:3], rd[3:6], rd[6:9]], S_read)
    got = [full[i][j] for i, j in unk] if full else None
    P.v("V1 independent solver (reads the printed square and total, fills each line with one gap) equals the key", got == truth, [str(g) for g in (got or [])])
    P.v("V1b all nine numbers are different and the total is printed", len({x for r in M for x in r}) == 9)
    P.v("V7 denominators 2, 4 or 3 only; numbers below 14", all(x.denominator in (1, 2, 3, 4) for r in M for x in r) and max(max(r) for r in M) < 14)
    dom = sorted({Fr(k, 12) for k in range(0, 12 * 14)})
    def lines_ok(a):
        g = [list(r) for r in M]
        for (i, j), v in zip(unk, a): g[i][j] = v
        return all(sum(g[r][c] for r, c in ln) == S for ln in LINES)
    P.v("V3 every single wrong value (any multiple of 1/12 below 14) in one empty square breaks a line", all(not lines_ok([a if j != k else v for j, a in enumerate(truth)]) for k in range(5) for v in dom if v != truth[k]))
    P["cv"] = dict(rate=1.0, single_total=5 * len(dom), single_detected=5 * len(dom))
    P["model"] = dict(truth=truth, domains=[dom] * 5, check=lines_ok, numeric=False)
    P["facts"] = ""
    P["mini"] = '<div class="kmini kmagic" style="grid-template-columns:repeat(3,13mm)">' + "".join(f'<i class="num" style="width:13mm;font-size:8pt">{frac_txt(M[i][j])}</i>' for i in range(3) for j in range(3)) + "</div>"
    return P

# =============================================================================== P5-11 Mixed Number Route (route)
def mixed_h(v):
    return FM(v)

def expr_for(rng, V, dens=(2, 3, 4, 6, 8)):
    """an addition or subtraction of two mixed numbers (or a whole number and a mixed number) with value V, as (html text)"""
    for _ in range(400):
        d = rng.choice(dens)
        b = Fr(rng.randint(1, 3 * d - 1), d)
        if b.denominator == 1: continue
        kind = rng.choice(["+", "−", "−w"])
        if kind == "+":
            a = V - b
            if a <= 0: continue
            if a.denominator > 12 or a.denominator == 1 or (a.denominator % b.denominator and b.denominator % a.denominator): continue
            if a < 1 and rng.random() < .5: continue
            return f"{FM(a)} + {FM(b)}" if rng.random() < .5 else f"{FM(b)} + {FM(a)}"
        a = V + b
        if a.denominator > 12 or a > 9: continue
        if kind == "−w":
            a = Fr(int(a) + 1)
            b2 = a - V
            if b2.denominator == 1 or b2 <= 0 or b2.denominator > 12: continue
            return f"{a.numerator} − {FM(b2)}"
        if a.denominator == 1 or (a.denominator % b.denominator and b.denominator % a.denominator): continue
        return f"{FM(a)} − {FM(b)}"
    return None

def page11():
    rng = random.Random(5111)
    for _ in range(400):
        T = rng.choice([Fr(4, 1) + Fr(1, 4), Fr(3, 1) + Fr(3, 4), Fr(2, 1) + Fr(5, 6), Fr(3, 1) + Fr(1, 2), Fr(5, 1) + Fr(3, 8), Fr(2, 1) + Fr(2, 3)])
        offs = [T + Fr(1, 4), T - Fr(1, 4), T + Fr(1, 2), T - Fr(1, 2), T + 1, T - 1, T + Fr(1, 3) if T.denominator % 3 == 0 else T + Fr(3, 4), T - Fr(1, 8) if T.denominator == 8 else T - Fr(3, 4)]
        offs = [o for o in offs if o > 1]
        n = 4; L = 8
        try:
            def on(i):
                while True:
                    e = expr_for(rng, T)
                    if e: return e
            def off():
                while True:
                    e = expr_for(rng, rng.choice(offs))
                    if e: return e
            path, grid, dead = build_route(rng, n, L, on, off, 3, ok_text=lambda t: evaluate(to_text(t)) == T)
            break
        except RuntimeError:
            continue
    else: raise RuntimeError("p11")
    P = route_page(11, 5111, "Mixed Number Route", 1, "Fractions: adding and subtracting mixed numbers", STRAND_FR,
        "adding and subtracting mixed numbers", ["FR2.1"], "Maze / path",
        ["Start at START. Move up, down, left or right.", "Step only on boxes with the answer shown below.", "Do not step on a box twice."],
        grid, path, dead, "", lambda c: evaluate(to_text(c)) == T,
        f"A 4 by 4 grid of sixteen additions and subtractions of mixed numbers (denominators 2, 3, 4, 6 and 8, never more than two different ones in one box). The boxes off the route make answers one quarter, one half, one third or one whole away from {frac_txt(T)}; some extra boxes that do make {frac_txt(T)} are dead ends. Counting the boxes shows a line that takes a shortcut.",
        lambda c: to_text(c), f"Does your line reach FINISH? Count its boxes: are there {L}? Does every box make {frac_txt(T)}?", extra_facts=frac_txt(T))
    # the target is printed in the instructions
    P["instr"] = ["Start at START. Move up, down, left or right.", f"Step only on boxes with the answer {frac_txt(T)}.", "Do not step on a box twice."]
    P["instr_html"] = ["Start at START. Move up, down, left or right.", f"Step only on boxes with the answer {FM(T)}.", "Do not step on a box twice."]
    P["check_html_lines"] = [f"Does your line reach FINISH? Count its boxes: are there {L}? Does every box make {FM(T)}?"]
    return P

# =============================================================================== P5-12 Fraction Chain (loop)
def chain_html(xs, ops):
    """a ring of six circles: x0 (printed), x1..x5 (empty), and six arrows. Row 1: x0 -> x1 -> x2, down to x3, row 2: x3 -> x4 -> x5 (right to left), up to x0."""
    def node(i):
        return (f'<div class="cn" data-i="{i}">{xs[i]}</div>' if i == 0 else f'<div class="cn blank" data-i="{i}"><span class="ab"></span></div>')
    def arr(k, back=False):
        n, d = ops[k]
        return f'<div class="car{" back" if back else ""}" data-k="{k}"><span class="opl">× {FR(n, d)}</span><span class="arrow"></span></div>'
    def vcon(k, up):
        n, d = ops[k]
        return f'<div class="vcon {"up" if up else "dn"}" data-k="{k}"><span class="opl">× {FR(n, d)}</span><span class="vline"></span></div>'
    e = "<div></div>"
    cells = [node(0), arr(0), node(1), arr(1), node(2),
             vcon(5, True), e, e, e, vcon(2, False),
             node(5), arr(4, True), node(4), arr(3, True), node(3)]
    return '<div class="cloop">' + "".join(cells) + "</div>"

def read_chain(h):
    x0 = int(re.search(r'<div class="cn" data-i="0">(\d+)</div>', h).group(1))
    ops = {}
    for m in re.finditer(r'data-k="(\d)"><span class="opl">(.*?)</span><span class="(?:arrow|vline)"></span></div>', h, re.S):
        ops[int(m.group(1))] = evaluate(to_text(m.group(2)).replace("×", "").strip())
    return x0, [ops[k] for k in range(6)]

def page12():
    rng = random.Random(5112)
    for _ in range(20000):
        x0 = rng.choice([24, 30, 36, 40, 48, 60, 72, 80, 90, 120, 18, 20, 45, 54, 64, 96])
        xs = [x0]; ops = []
        ok = True
        for k in range(5):
            cands = []
            for n in range(2, 13):
                for d in range(2, 13):
                    if math.gcd(n, d) != 1 or n == d: continue
                    v = Fr(xs[-1]) * Fr(n, d)
                    if v.denominator == 1 and 6 <= v <= 150 and v not in xs: cands.append((n, d, int(v)))
            if not cands: ok = False; break
            n, d, v = rng.choice(cands); ops.append((n, d)); xs.append(v)
        if not ok: continue
        f = Fr(x0, xs[5])
        if f.numerator > 12 or f.denominator > 12 or f == 1: continue
        ops.append((f.numerator, f.denominator))
        improper = sum(1 for n, d in ops if n > d)
        if improper < 2 or improper > 4: continue
        break
    else: raise RuntimeError("p12")
    body = chain_html(xs, ops) + '<p class="lead" style="text-align:center;margin-top:4mm">The last arrow takes you back to the start number.</p>'
    P = new_page(12, 5112, "Fraction Chain", 1, "Fractions: multiplying a fraction by a whole number", STRAND_FR,
        "multiplying a proper or improper fraction by a whole number", ["FR2.2"], "Number chain (loop)", "K8 the loop closes: the last arrow returns to the start number",
        ["Follow the arrows round the loop.", "Each arrow multiplies the number by a fraction.", "Write each answer in its circle."],
        body, "Circles in order: " + ", ".join(str(x) for x in xs) + f"; last arrow x {ops[5][0]}/{ops[5][1]} returns to {x0}", "The loop closes at the start number.",
        "A ring of six circles joined by arrows. The start number is printed; each arrow multiplies the number in one circle by a fraction (some fractions are greater than 1) and gives a whole number in the next circle. The pupil fills five circles. The last arrow must bring the chain back to the start number: a wrong number in any circle carries on round the loop and the chain does not close. Two slips that cancel out are not detected.",
        check=f"Does the last arrow take you back to {x0}?", mk=("loop",),
        mech_plain="Loop: following the arrows round, the last arrow must give the start number again")
    x0r, opsr = read_chain(body)
    xr = [x0r]
    for k in range(5): xr.append(xr[-1] * opsr[k])
    P.v("V1 independent solver (reads the start number and the six printed arrows, multiplies round the ring) equals the key", [int(x) for x in xr[1:]] == xs[1:] and all(x.denominator == 1 for x in xr), [str(x) for x in xr])
    P.v("V1b the last arrow gives the start number", xr[5] * opsr[5] == x0r)
    P.v("V7 every circle is a whole number from 6 to 150; fractions have denominators 2 to 12", all(6 <= x <= 150 for x in xs) and all(d <= 12 and n <= 12 for n, d in ops), "")
    def closes(a):
        bad = [k for k in range(5) if a[k] != xs[k + 1]]
        if not bad: return True
        k = bad[0]; v = Fr(a[k])
        for j in range(k + 1, 6): v *= Fr(*ops[j])
        return v == x0                  # the pupil goes on from the number written in circle k+1
    dom = list(range(0, 301))
    P.v("V3 a slip in any circle (every value 0 to 300), carried round the loop, does not return to the start number", all(not closes([a if j != k else v for j, a in enumerate(xs[1:])]) for k in range(5) for v in dom if v != xs[k + 1]))
    P["cv"] = dict(rate=1.0, single_total=5 * 300, single_detected=5 * 300)
    P["model"] = dict(truth=list(xs[1:]), domains=[dom] * 5, check=closes, numeric=True)
    P["facts"] = ""
    return P

# =============================================================================== P5-13 Fraction of a Quantity (code word)
STORY13 = ["What is {f} of {N} {u}?", "A rope is {N} m long. {f} of it is cut off. How long is the piece cut off?", "Mei has ${N}. She spends {f} of it. How much does she spend?",
           "{f} of the {N} pupils wear glasses. How many pupils wear glasses?", "A tank holds {N} ℓ. It is {f} full. How much water is in it?",
           "A film lasts {N} minutes. {f} of it is over. How many minutes are over?"]
UNITS13 = [("kg", "kg"), ("m", "m"), ("", ""), ("", ""), ("ℓ", "ℓ"), ("min", "min")]

def page13():
    rng = random.Random(5113)
    for _ in range(6000):
        fr, ans, Ns = [], [], []
        for k in range(6):
            d = rng.choice([3, 4, 5, 6, 8, 9, 10, 12])
            n = d + rng.randint(1, d - 1) if k == 0 else rng.randint(1, d - 1)
            if math.gcd(n, d) != 1: break
            N = d * rng.randint(2, 9)
            fr.append((n, d)); Ns.append(N); ans.append(Fr(n * N, d))
        else:
            if not distinct(ans) or max(ans) > 300 or len({d for _, d in fr}) < 5: continue
            order = list(range(6)); rng.shuffle(order)
            fr = [fr[k] for k in order]; Ns = [Ns[k] for k in order]; ans = [ans[k] for k in order]
            pool = []
            for (n, d), N, a in zip(fr, Ns, ans):
                pool += [Fr(N, d), N - a if N > a else a - N, Fr(n * N), Fr(N + n), a + n, a - n if a > n else a + d]
            pool = [p for p in dict.fromkeys(pool) if p not in ans and p > 0 and p.denominator == 1]
            res = code_table_for(13, ans, rng, pool, n_decoy=3, tries=60)
            if res[0]: (word, table), dom = res; break
    else: raise RuntimeError("p13")
    cards = []
    for i, k in enumerate(order):
        n, d = fr[i]; N = Ns[i]
        u = UNITS13[k][0]
        t = STORY13[k].format(f=FR(n, d), N=N, u=u)
        cards.append(qc(i + 1, f'<p class="qt">{t}</p>', abx("w4") + (f'<span class="unit">{u}</span>' if k in (0, 1, 4, 5) else "")))
    ans2 = list(ans)
    solved = []
    for c in cards:
        t = to_text(re.search(r'<div class="qt">(.*?)</div></div><div class="qa">', c, re.S).group(1))
        m = re.search(r"⟨(\d+)\|(\d+)⟩", t); n, d = int(m.group(1)), int(m.group(2))
        rest = txt_ints_outside_fractions(t)
        solved.append(Fr(n * rest[0], d))
    P = code_page(13, 5113, "Fraction of a Quantity", 1, "Fractions: multiplying a fraction by a whole number", STRAND_FR,
        "multiplying a proper or improper fraction by a whole number (a fraction of a quantity)", ["FR2.2"], "Code-breaker (fractions of quantities)",
        ["Find the fraction of each quantity.", "Write the answer in the box.", "Use the code table."],
        cards, ans2, word, table, dom, lambda k: num(int(k)), "; ".join(f"{i+1}) {a}" for i, a in enumerate(ans2)),
        "Six fractions of a quantity, in a bare question and in short stories (length, money, a class, water, time). One fraction is greater than 1. The decoy letters stand for the usual slips: dividing by the denominator only, multiplying by the numerator only, or taking the answer away from the whole. Every quantity divides exactly by the denominator. A box left blank gives no letter and the check cannot see it.",
        solved, cols=3, layout="c2", ps=True, checks=[("V7 answers are whole numbers up to 300", all(a.denominator == 1 and a <= 300 for a in ans), "")])
    return P

PAGES = [page08, page09, page10, page11, page12, page13]
