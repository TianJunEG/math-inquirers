"""Semester 1, pages P3-10 to P3-13: true or false tables, remainders, fact families (loop), multiplication and division in columns."""
import random, re, itertools
from .common import *
from .kit import *
from .p3kit import *

# =============================================================================== P3-10 True or False Tables
def tf_statement(kind, rng, true):
    if kind == "groups":
        g = rng.choice([6, 7, 8, 9]); m = rng.randint(4, 9); p = g * m
        v = p if true else p + rng.choice([-m, m, g, -g, 6, -6, 10])
        return f"{g} groups of {m} is {v}.", v == p
    if kind == "mul":
        a = rng.choice([6, 7, 8, 9]); b = rng.randint(4, 9); p = a * b
        v = p if true else rng.choice([p + a, p - a, p + b, p - b, p + 10, p - 10, a + b + 20])
        return f"{a} × {b} = {v}", v == p
    if kind == "div":
        d = rng.choice([6, 7, 8, 9]); q = rng.randint(4, 9); n = d * q
        v = q if true else rng.choice([q + 1, q - 1, q + 2, n - d, d])
        return f"{n} ÷ {d} = {v}", v == q
    if kind == "rel":
        b = rng.choice([6, 7, 8, 9]); a = rng.randint(4, 9); p = a * b
        if true: return f"If {a} × {b} = {p}, then {p} ÷ {b} = {a}.", True
        w = rng.choice([x for x in (a + 1, a - 1, b, p - b) if x > 0 and x != a])
        return f"If {a} × {b} = {p}, then {p} ÷ {b} = {w}.", False
    if kind == "table":
        t = rng.choice([6, 7, 8, 9]); m = rng.randint(4, 9)
        if true: n = t * m
        else:
            n = t * m + rng.choice([1, 2, 3])
            if n % t == 0: n += 1
        return f"{n} is in the {t} times table.", n % t == 0
    raise ValueError(kind)

def solve_tf(t):
    m = re.fullmatch(r"(\d+) groups of (\d+) is (\d+)\.", t)
    if m: return int(m.group(1)) * int(m.group(2)) == int(m.group(3))
    m = re.fullmatch(r"(\d+) × (\d+) = (\d+)", t)
    if m: return int(m.group(1)) * int(m.group(2)) == int(m.group(3))
    m = re.fullmatch(r"(\d+) ÷ (\d+) = (\d+)", t)
    if m: return int(m.group(1)) == int(m.group(2)) * int(m.group(3))
    m = re.fullmatch(r"If (\d+) × (\d+) = (\d+), then (\d+) ÷ (\d+) = (\d+)\.", t)
    if m:
        a, b, p, p2, b2, w = map(int, m.groups()); return a * b == p and p2 == p and b2 == b and p // b2 == w
    m = re.fullmatch(r"(\d+) is in the (\d+) times table\.", t)
    if m: return int(m.group(1)) % int(m.group(2)) == 0
    raise ValueError(t)

def page10():
    rng = random.Random(3010)
    kinds = ["groups", "mul", "div", "rel", "table", "mul"]
    while True:
        rng.shuffle(kinds)
        truths = [rng.random() < 0.5 for _ in range(6)]
        if not 2 <= sum(truths) <= 4: continue
        rows = [tf_statement(k, rng, t) for k, t in zip(kinds, truths)]
        if len({r[0] for r in rows}) < 6 or any(r[1] != t for r, t in zip(rows, truths)): continue
        break
    specs = []
    for txt, tr in rows:
        T_, F_ = '<b class="tf">True</b>', '<b class="tf">False</b>'
        specs.append(dict(q=f"<p>{esc(txt)}</p>", opts=[T_, F_], right=0 if tr else 1, fixed=True))
    P = lettered_choice_page(10, 3010, "True or False Tables", 1, "Multiplication and division facts: tables of 6, 7, 8 and 9", STRAND_MD,
        "3.1, 3.2, 3.5 (tables of 6, 7, 8 and 9; multiplying and dividing within the tables; mental calculation)", ["MD3.1", "MD3.2", "MD3.5"], "True or false table",
        ["Is each statement true or false?", "Circle the letter of the right choice.", "Write the six letters in the boxes."],
        specs, 2, "; ".join(f"{i+1}) {'True' if tr else 'False'} ({txt})" for i, (txt, tr) in enumerate(rows)),
        "Six statements from the tables of 6, 7, 8 and 9, including one about a times table and one that links a multiplication to a division. Each row has a True choice and a False choice, each with a letter. The letters of the right choices, read down the rows, spell the word. Every other way of choosing was tested against a very large word list: none spells a word. A box left blank gives no letter and the check cannot see it.",
        rng=rng, row_cls="tfrow2")
    def solver(q, opts):
        t = re.search(r"<p>(.*?)</p>", q).group(1).replace("&amp;", "&")
        return 0 if solve_tf(t) else 1
    got = solve_letters(solver, P["body"])
    P.v("V1 independent evaluator reads each printed statement and its letter and gets the word", got == P["word"], got)
    P.v("V4 between 2 and 4 statements are true", 2 <= sum(tr for t, tr in rows) <= 4)
    P.v("V7 every factor is from the tables of 6 to 9 with the other factor 4 to 9", all(any(int(x) in (6, 7, 8, 9) for x in re.findall(r"\d+", t)[:2]) for t, _ in rows))
    return P

# =============================================================================== P3-11 Remainders
def rem_item(kind, rng, N_, d):
    q, r = divmod(N_, d)
    th = rng.choice(["stickers", "marbles", "sweets", "cards", "beads"])
    nm = rng.choice(PEOPLE)
    if kind == "rem": return f"What is the remainder when {N_} is divided by {d}?", r
    if kind == "quo": return f"{N_} {th} are put in bags of {d}. How many full bags are there?", q
    if kind == "left": return f"{nm} shares {N_} {th} equally among {d} children. How many are left over?", r
    if kind == "boxes": return f"{N_} {th} are packed in boxes of {d}. What is the least number of boxes needed?", q + (1 if r else 0)
    if kind == "bare": return f"Divide {N_} by {d}. What is the quotient?", q
    if kind == "zero": return f"What is the remainder when {N_} is divided by {d}?", r
    raise ValueError(kind)

def solve_rem(t):
    nums = list(map(int, re.findall(r"\d+", t)))
    N_, d = nums[0], nums[1]
    if t.startswith("What is the remainder"): return N_ % d
    if "How many full bags" in t: return N_ // d
    if "left over" in t: return N_ % d
    if "least number of boxes" in t: return -(-N_ // d)
    if "quotient" in t: return N_ // d
    raise ValueError(t)

def page11():
    rng = random.Random(3111)
    kinds = ["rem", "quo", "left", "boxes", "bare", "zero"]
    while True:
        rng.shuffle(kinds); items = []
        for k in kinds:
            d = rng.choice([4, 5, 6, 7, 8, 9]);
            if k == "zero": N_ = d * rng.randint(4, 9)
            else:
                N_ = rng.randint(30, 85)
                if N_ % d == 0: N_ += 1
            t, a = rem_item(k, rng, N_, d); items.append((k, N_, d, t, a))
        ans = [x[4] for x in items]
        if not distinct(ans) or len({x[3] for x in items}) < 6: continue
        pool = set()
        for k, N_, d, t, a in items:
            q, r = divmod(N_, d); pool |= {q, r, q + 1, r + 1, r - 1 if r else 1}
        pool = sorted(p for p in pool if p not in ans and 0 <= p <= 15)
        res = find_table(11, 6, ans, rng, 0, 15, pool, n_decoy=3, tries=80)
        if res: word, table = res; break
    cards = [qcard(i + 1, f"<p>{t}</p>", '<span class="ab w3"></span>') for i, (k, N_, d, t, a) in enumerate(items)]
    P = code_items_page(11, 3111, "Remainders", 1, "Division with remainder", STRAND_MD,
        "3.3 (division with remainder)", ["MD3.3"], "Code-breaker (division with remainder)",
        ["Divide. Read what is asked.", "Write the answer in the box.", INSTR_CODE],
        qgrid(cards, 2), ans, table, word, 0, 15,
        "; ".join(f"{i+1}) {N_} ÷ {d}: quotient {N_ // d}, remainder {N_ % d}; answer {a}" for i, (k, N_, d, t, a) in enumerate(items)),
        "Six division items, each asking for a different part of the same kind of answer: a remainder, a number of full bags, the number left over when sharing, the least number of boxes (the quotient plus one when there is a remainder), a quotient, and one remainder that is zero. The decoy letters stand for the quotient when the remainder was asked for, the remainder when the quotient was asked for, and the least number of boxes without the extra box. A box left blank gives no letter and the check cannot see it.",
        domain=None)
    solved = [solve_rem(t) for k, N_, d, t, a in items]
    P.v("V1 independent solver reads the printed words and numbers back and equals the key", solved == ans, solved)
    P.v("V7 divisors 4 to 9, dividends within 90", all(4 <= d <= 9 and N_ <= 90 for k, N_, d, t, a in items))
    P.v("V1b exactly one item has remainder zero", sum(1 for k, N_, d, t, a in items if N_ % d == 0) == 1)
    return P

# =============================================================================== P3-12 Fact Families (loop)
def mchain_svg(tiles, blank):
    p = []; R = 5.4
    for k, (w, l, r) in enumerate(tiles):
        x = k * 30
        p.append(f'<line x1="{x+15}" y1="{8+R}" x2="{x+7}" y2="{31-R}" stroke="#000" stroke-width="0.5"/><line x1="{x+15}" y1="{8+R}" x2="{x+23}" y2="{31-R}" stroke="#000" stroke-width="0.5"/>'
                 f'<text x="{x+0.3}" y="3.2" font-family="Nunito Sans" font-weight="800" font-size="3.3" fill="#000">tile {k+1}</text>'
                 f'<text x="{x+15}" y="31.3" text-anchor="middle" dominant-baseline="central" font-family="Fredoka" font-weight="600" font-size="6.6" fill="#000">×</text>')
        for cx, cy, v, role in ((x + 15, 8, w, "w"), (x + 7, 31, l, "l"), (x + 23, 31, r, "r")):
            isb = (role == blank[k])
            p.append(f'<circle class="pc{" blank" if isb else ""}" data-k="{k}" data-role="{role}" cx="{cx}" cy="{cy}" r="{R}" fill="#fff" stroke="#000" stroke-width="0.6"/>')
            if not isb: p.append(f'<text class="pn" data-k="{k}" data-role="{role}" x="{cx}" y="{cy}" text-anchor="middle" dominant-baseline="central" font-family="Fredoka" font-weight="600" font-size="6.2" fill="#000">{v}</text>')
        if k < 5: p.append(f'<line x1="{x+29}" y1="30" x2="{x+31}" y2="30" stroke="#000" stroke-width="0.7"/><line x1="{x+29}" y1="32" x2="{x+31}" y2="32" stroke="#000" stroke-width="0.7"/>')
    p.append('<path d="M172,37.6 L172,45 L8,45 L8,37.6" fill="none" stroke="#000" stroke-width="0.6"/><rect x="82" y="42.6" width="16" height="4.8" fill="#fff"/><text x="90" y="45" text-anchor="middle" dominant-baseline="central" font-family="Fredoka" font-weight="600" font-size="4.6" fill="#000">=</text>')
    return svg(180, 48, "".join(p))

def read_mchain(s):
    vals = {}
    for m in re.finditer(r'class="pc( blank)?" data-k="(\d)" data-role="(\w)"', s): vals[(int(m.group(2)), m.group(3))] = None
    for m in re.finditer(r'class="pn" data-k="(\d)" data-role="(\w)"[^>]*>(\d+)<', s): vals[(int(m.group(1)), m.group(2))] = int(m.group(3))
    return vals

def solve_mchain(vals):
    ans = []; full = dict(vals)
    for k in range(6):
        for role, other in (("l", "r"), ("r", "l")):
            if vals[(k, role)] is None:
                assert vals[(k, "w")] % vals[(k, other)] == 0
                full[(k, role)] = vals[(k, "w")] // vals[(k, other)]; ans.append(full[(k, role)])
    ok = all(full[(k, "r")] == full[((k + 1) % 6, "l")] for k in range(6))
    return ans, ok

def page12():
    rng = random.Random(3212)
    while True:
        x = [rng.randint(3, 9) for _ in range(6)]
        tiles = [(x[k] * x[(k + 1) % 6], x[k], x[(k + 1) % 6]) for k in range(6)]
        if len(set(x)) < 5 or any(not ({t[1], t[2]} & {6, 7, 8, 9}) for t in tiles): continue
        blank = [rng.choice("lr") for _ in range(6)]
        if sum(1 for k in range(6) if blank[k] == "r" and blank[(k + 1) % 6] == "l") > 1: continue
        ans = [tiles[k][1] if blank[k] == "l" else tiles[k][2] for k in range(6)]
        break
    chain = mchain_svg(tiles, blank)
    ex = ('<div class="howto"><b>Example</b><p class="ptxt">Top 56. Left 7. Right?</p><p class="ptxt">56 ÷ 7 = 8. Check: 7 × 8 = 56.</p></div>')
    body = (f'{ex}<div class="blk"><p class="lead">Each tile: top = left × right.</p>{chain}</div>'
            f'<div class="blk"><p class="lead">Write the numbers for the empty circles, tile 1 to tile 6.</p><div class="ansgrid2" style="margin-top:4mm">'
            + "".join(f'<span class="lbx"><span class="ab"></span><small>tile {k+1}</small></span>' for k in range(6)) + '</div></div>')
    P = new_page(12, 3212, "Fact Families", 2, "Multiplication and division: finding the missing number, the loop that closes", STRAND_MD,
        "3.1, 3.2, 3.3 (tables of 6, 7, 8 and 9; multiplying and dividing within the tables)", ["MD3.1", "MD3.2"], "Chain loop (multiplication tiles)", "K8 the loop closes: every number joined by = matches",
        ["Find the number in each empty circle.", "Touching circles joined by = match.", "Go round the loop."],
        body, "Empty circles: " + ", ".join(f"tile {k+1} {'left' if blank[k] == 'l' else 'right'} = {ans[k]}" for k in range(6)) + ". Tiles (top = left × right): " + ", ".join(f"{t[0]} = {t[1]} × {t[2]}" for t in tiles),
        "Every touching pair matches, all the way round.",
        "Six tiles, each a product at the top and its two factors below. One factor of every tile is empty; the pupil finds it by dividing the top by the other factor and may check by multiplying back. The right factor of a tile is the same number as the left factor of the next tile, and the right factor of the last tile is the first tile's left factor. So every number the pupil writes is tested against a matching circle: a wrong number breaks the loop. At most one link has an empty circle on both sides. In every tile at least one factor is from the tables of 6 to 9; all products are within 81.",
        check="Go round the loop. Do the numbers joined by = match?", mk=("loop",),
        mech_plain="Loop: the number in an empty circle must match the circle it is joined to by =, all the way round and back to tile 1")
    vals = read_mchain(chain)
    got, ok = solve_mchain(dict(vals))
    P.v("V1 independent reader: every empty circle is found by dividing the top by the other factor and the loop closes with those numbers", got == ans and ok, got)
    P.v("V1b every tile has exactly one empty factor", sum(v is None for v in vals.values()) == 6)
    P.v("V7 products within 81, a factor from 6 to 9 in every tile", all(t[0] <= 81 and ({t[1], t[2]} & {6, 7, 8, 9}) for t in tiles))
    def closes(a):
        f = dict(vals)
        for k in range(6): f[(k, blank[k])] = a[k]
        return all(f[(k, "r")] == f[((k + 1) % 6, "l")] for k in range(6)) and all(f[(k, "l")] * f[(k, "r")] == f[(k, "w")] for k in range(6))
    dom = list(range(0, 82))
    P.v("V3 every single wrong value in one empty circle (0 to 81) breaks the loop", all(not closes([a if j != k else v for j, a in enumerate(ans)]) for k in range(6) for v in dom if v != ans[k]))
    P["cv"] = dict(rate=1.0, single_total=6 * 81, single_detected=6 * 81)
    P["model"] = dict(truth=list(ans), domains=[dom] * 6, check=closes, numeric=True)
    P["facts"] = "81 " + " ".join(str(t[0]) for t in tiles)
    return P

# =============================================================================== P3-13 Columns: multiplication and division
def nocarry_mul(a, d):
    return int("".join(str(int(c) * d % 10) for c in str(a)))

def page13():
    rng = random.Random(3313)
    while True:
        items = []
        # three multiplications (3-digit by 1-digit, renaming) and three divisions (3-digit by 1-digit)
        for _ in range(3):
            while True:
                a = rng.randint(120, 499); d = rng.choice([3, 4, 5, 6, 7, 8, 9])
                if a * d < 4000 and any(int(c) * d >= 10 for c in str(a)) and a % 10 != 0: break
            items.append(("mul", a, d))
        for z in range(3):
            d = rng.choice([3, 4, 5, 6, 7, 8, 9])
            if z == 0: q = rng.randint(101, 109)
            else:
                q = rng.randint(21, 999 // d)
                while q % 10 == 0: q = rng.randint(21, 999 // d)
            items.append(("div", d * q, d))
        rng.shuffle(items)
        ans = [a * d if k == "mul" else a // d for k, a, d in items]
        if not distinct(ans) or max(ans) > 9999: continue
        pool = set()
        for (k, a, d), r in zip(items, ans):
            if k == "mul": pool |= {nocarry_mul(a, d), r + 10, r - 100}
            else: pool |= {r + 10, r - 10, int(str(r).replace("0", "")) if "0" in str(r) else r + 1}
        pool = sorted(p for p in pool if p not in ans and 0 < p <= 9999)
        res = find_table(13, 6, ans, rng, 0, 9999, pool, n_decoy=3, tries=25)
        if res: word, table = res; break
    cards = []
    for i, (k, a, d) in enumerate(items):
        if k == "mul": cards.append(f'<div class="vcard"><span class="no">{i+1}</span>{vsum4(a, d, chr(215))}</div>')
        else: cards.append(f'<div class="vcard dv"><span class="no">{i+1}</span><div class="dvt">Divide {a} by {d}.</div><span class="ab w4"></span></div>')
    P = code_items_page(13, 3313, "Multiply and Divide", 2, "Multiplication and division of 3-digit numbers by 1-digit numbers", STRAND_MD,
        "3.4 (multiplication and division algorithms, up to 3 digits by 1 digit)", ["MD3.4"], "Code-breaker (written methods)",
        ["Work out each sum. Use columns.", "Write the answer in the box.", INSTR_CODE],
        f'<div class="vcards">{"".join(cards)}</div>', ans, table, word, 0, 9999,
        "; ".join(f"{i+1}) {a} {chr(215) if k == 'mul' else chr(247)} {d} = {x}" for i, ((k, a, d), x) in enumerate(zip(items, ans))),
        "Three multiplications of a 3-digit number by a 1-digit number (renaming in the ones or tens) and three exact divisions of a 3-digit number by a 1-digit number, one of them with a zero in the quotient. The decoy letters stand for the answers a pupil gets by not renaming in a multiplication, or by leaving out the zero of a quotient. A box left blank gives no letter and the check cannot see it.")
    solved = []
    for h in cards:
        if "vsum" in h:
            rows_, op = parse_vsum4(h.split("</span>", 1)[1]); solved.append(int(rows_[0]) * int(rows_[1]))
        else:
            m = re.search(r"Divide (\d+) by (\d+)\.", h); solved.append(int(m.group(1)) // int(m.group(2)))
    P.v("V1 independent solver reads the printed items back and equals the key", solved == ans, solved)
    P.v("V7 3-digit numbers by 1-digit numbers; every division is exact", all(100 <= a <= 999 and 3 <= d <= 9 for k, a, d in items) and all(a % d == 0 for k, a, d in items if k == "div"))
    P.v("V7b three multiplications and three divisions", sum(1 for k, a, d in items if k == "mul") == 3)
    return P

PAGES = [page10, page11, page12, page13]
