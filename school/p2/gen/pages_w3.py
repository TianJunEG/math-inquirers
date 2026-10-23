"""Wave 3: P2-17 Mystery Numbers; P2-18 Story Sums to 1000; P2-19 Fact Families; P2-20 True or False Tables;
P2-21 Fraction Order; P2-22 Fraction Sums; P2-23 Which Costs More?; P2-24 Purse Match."""
import random, re, math, itertools
from .common import *
from .kit import *
from .pages_w1 import code_items_page, distinct, STRAND_WN, STRAND_AS, STRAND_MD, STRAND_MO, INSTR_CODE, PEOPLE
from .pages_w2 import STRAND_FR, words3
from . import art2 as A
from .art import NAMES as OBJN

# =============================================================================== P2-17 Mystery Numbers
def clue_text(c):
    k, v = c
    return {"more": f"I am more than {v}.", "less": f"I am less than {v}.", "hund": f"My hundreds digit is {v}.", "tens": f"My tens digit is {v}.",
            "ones": f"My ones digit is {v}.", "odd": "I am an odd number.", "even": "I am an even number.",
            "tgo": "My tens digit is more than my ones digit.", "otg": "My ones digit is more than my tens digit.",
            "hgt": "My hundreds digit is more than my tens digit.", "plus": f"My ones digit is {v} more than my tens digit.",
            "same": "Two of my digits are the same."}[k]

def pred_from_text(s):
    """the solver's own parser: a printed clue -> a test on a number (does not use the generator's predicates)"""
    m = re.fullmatch(r"I am more than (\d+)\.", s)
    if m: return lambda n, v=int(m.group(1)): n > v
    m = re.fullmatch(r"I am less than (\d+)\.", s)
    if m: return lambda n, v=int(m.group(1)): n < v
    m = re.fullmatch(r"My (hundreds|tens|ones) digit is (\d)\.", s)
    if m:
        pos = {"hundreds": 0, "tens": 1, "ones": 2}[m.group(1)]; d = int(m.group(2)); return lambda n: int(str(n)[pos]) == d
    if s == "I am an odd number.": return lambda n: n % 2 == 1
    if s == "I am an even number.": return lambda n: n % 2 == 0
    if s == "My tens digit is more than my ones digit.": return lambda n: str(n)[1] > str(n)[2]
    if s == "My ones digit is more than my tens digit.": return lambda n: str(n)[2] > str(n)[1]
    if s == "My hundreds digit is more than my tens digit.": return lambda n: str(n)[0] > str(n)[1]
    m = re.fullmatch(r"My ones digit is (\d) more than my tens digit\.", s)
    if m: return lambda n, k=int(m.group(1)): int(str(n)[2]) - int(str(n)[1]) == k
    if s == "Two of my digits are the same.": return lambda n: len(set(str(n))) == 2
    raise ValueError(s)

def clue_pool(t, rng):
    h, te, o = t // 100, t // 10 % 10, t % 10
    pool = [("more", rng.randrange(max(100, t - 150), t, 5) if t > 105 else 100), ("less", rng.randrange(t + 1, min(1000, t + 150) + 1)),
            ("hund", h), ("tens", te), ("ones", o), ("odd" if o % 2 else "even", 0)]
    if te > o: pool.append(("tgo", 0))
    if o > te: pool.append(("otg", 0)); pool.append(("plus", o - te))
    if h > te: pool.append(("hgt", 0))
    if len(set(str(t))) == 2: pool.append(("same", 0))
    return pool

def page17():
    rng = random.Random(7117)
    while True:
        targets, riddles = [], []
        tries = 0
        while len(riddles) < 5 and tries < 4000:
            tries += 1
            t = rng.randint(110, 989)
            if t % 100 == 0 or t in targets: continue
            pool = clue_pool(t, rng)
            k = rng.choice([3, 4])
            cl = rng.sample(pool, k)
            tests = [pred_from_text(clue_text(c)) for c in cl]
            sols = [n for n in range(100, 1000) if all(f(n) for f in tests)]
            if sols != [t]: continue
            if not all([n for n in range(100, 1000) if all(f(n) for j, f in enumerate(tests) if j != i)] != [t] for i in range(len(cl))): continue
            if len({c[0] for c in cl}) < k: continue
            targets.append(t); riddles.append(cl)
        if len(riddles) < 5: continue
        pool = set()
        for t, cl in zip(targets, riddles):
            for d in (10, 100, 1):
                pool |= {t + d, t - d}
            s = str(t); pool |= {int(s[0] + s[2] + s[1]), int(s[1] + s[0] + s[2])}
        pool = sorted(x for x in pool if x not in targets and 100 <= x <= 999 and str(x)[0] != "0")
        res = code_table_any(17, 5, targets, rng, 100, 999, n_decoy=3, tries=60, pool=pool)
        if res: word, table = res; break
    rows = ""
    for i, cl in enumerate(riddles):
        rows += f'<div class="riddle"><span class="no">{i+1}</span><div class="rtext">{"<br>".join(clue_text(c) for c in cl)}</div><span class="ab w3"></span></div>'
    P = code_items_page(17, 7117, "Mystery Numbers", 2, "3-digit numbers: digits, odd and even, more and less", STRAND_WN,
        "1.2, 1.4, 1.6 (place values; comparing and ordering numbers; odd and even numbers)", ["WN1.2", "WN1.4", "WN1.6"], "Number riddles",
        ["Find each mystery number.", "Write it in the box.", INSTR_CODE],
        f'<div class="riddles">{rows}</div>', targets, table, word, 100, 999,
        "; ".join(f"{i+1}) {t}" for i, t in enumerate(targets)),
        "Every riddle has three or four clues and every clue is needed: with one clue left out, more than one number fits. A pupil who stops after the first clues gets a number that fits some of them; testing every clue removes the others. Clues used: more than, less than, a digit of a place, odd, even, one digit more than another, two digits the same. The decoy letters stand for numbers that fit most of the clues. A box left blank gives no letter and the check cannot see it.")
    tests_all = [[pred_from_text(s_) for s_ in re.findall(r"(I am[^<]*?\.|My [^<]*?\.|Two [^<]*?\.)", ("<br>".join(clue_text(c) for c in cl)))] for cl in riddles]
    solved = [[n for n in range(100, 1000) if all(f(n) for f in tests)] for tests in tests_all]
    P.v("V1 independent solver (printed clues parsed back, every number 100 to 999 tested) finds exactly the key", solved == [[t] for t in targets], solved)
    P.v("V1b every clue is necessary", all([n for n in range(100, 1000) if all(f(n) for j, f in enumerate(tests) if j != i)] != [t] for tests, t in zip(tests_all, targets) for i in range(len(tests))))
    P.v("V7 every number is 3-digit", all(100 <= t <= 999 for t in targets))
    return P

# =============================================================================== P2-18 Story Sums to 1000
OBJS = ["pens", "books", "stamps", "stickers", "marbles", "cards", "beads", "buttons", "shells", "coins"]

def make_story(kind, rng, N, M, obj):
    """returns (lines, answer, first step) for one story kind"""
    if kind == "addsub":
        a = rng.randint(200, 600); b = rng.randint(50, 300); c = rng.randint(30, min(250, a + b - 100))
        return [f"{N} has {a} {obj}.", f"{N} buys {b} more.", f"Then {N} gives away {c}.", f"How many {obj} now?"], a + b - c, a + b
    if kind == "subsub":
        a = rng.randint(500, 950); b = rng.randint(50, 300); c = rng.randint(30, 250)
        return [f"A box has {a} {obj}.", f"{b} are used on Monday.", f"{c} are used on Tuesday.", "How many are left?"], a - b - c, a - b
    if kind == "addadd":
        a = rng.randint(120, 400); b = rng.randint(60, 300); c = rng.randint(60, 250)
        return [f"A shop has {a} {obj}.", f"It gets {b} more on Monday.", f"It gets {c} more on Tuesday.", "How many in all?"], a + b + c, a + b
    if kind == "more":
        a = rng.randint(120, 450); b = rng.randint(30, 250)
        return [f"{N} has {a} {obj}.", f"{M} has {b} more than {N}.", "How many do they have in all?"], a + a + b, a + b
    if kind == "fewer":
        a = rng.randint(200, 450); b = rng.randint(30, 150)
        return [f"{N} has {a} {obj}.", f"{N} has {b} fewer than {M}.", "How many do they have in all?"], a + a + b, a + b
    if kind == "diff":
        a = rng.randint(400, 800); b = rng.randint(100, 350); c = rng.randint(50, 200)
        return [f"{N} has {a} {obj}.", f"{M} has {b}.", f"{M} gets {c} more. How many more does {N} have now?"], a - b - c, b + c
    raise ValueError(kind)

def solve_story(lines):
    """independent solver: reads the printed sentences (pattern by pattern) and does the two steps"""
    t = " ".join(lines); n = [int(x) for x in re.findall(r"\d+", t)]
    if " fewer than " in t: return n[0] + n[0] + n[1]
    if " more than " in t: return n[0] + n[0] + n[1]
    if "How many more does" in t: return n[0] - n[1] - n[2]
    if "How many in all?" in t and "gets" in t: return n[0] + n[1] + n[2]
    if "How many are left?" in t: return n[0] - n[1] - n[2]
    if "buys" in t and "gives away" in t: return n[0] + n[1] - n[2]
    raise ValueError(t)

def page18():
    rng = random.Random(7218)
    kinds = ["addsub", "subsub", "addadd", "more", "fewer", "diff"]
    while True:
        rng.shuffle(kinds); stories = []; names = rng.sample(PEOPLE, 6); objs = rng.sample(OBJS, 6)
        for i, kd in enumerate(kinds):
            M = rng.choice([x for x in PEOPLE if x != names[i]])
            stories.append(make_story(kd, rng, names[i], M, objs[i]))
        ans = [s[1] for s in stories]
        if not distinct(ans) or min(ans) < 100 or max(ans) > 999: continue
        pool = sorted({s[2] for s in stories} - set(ans))
        pool += [a + 10 for a in ans if a + 10 not in ans and a + 10 <= 999 and a + 10 not in pool]
        res = code_table_any(18, 6, ans, rng, 100, 999, n_decoy=3, tries=60, pool=pool)
        if res: word, table = res; break
    cards = [qcard(i + 1, "".join(f"<p>{l}</p>" for l in s[0]), '<span class="ab w3"></span>', cls="story") for i, s in enumerate(stories)]
    P = code_items_page(18, 7218, "Story Sums to 1000", 2, "Two-step stories with numbers to 1000", STRAND_AS,
        "2.1, 2.2 (addition and subtraction algorithms up to 3 digits; mental calculation)", ["AS2.1", "AS2.2"], "Code-breaker (two-step stories)",
        ["Read each story.", "Work out the answer in two steps.", INSTR_CODE],
        qgrid(cards, 2), ans, table, word, 100, 999,
        "; ".join(f"{i+1}) {s[2]} then {s[1]}" for i, s in enumerate(stories)),
        "Six stories, each with two steps within 1000: add then take away, take away twice, add twice, a 'more than' story and a 'fewer than' story (the child who has fewer is the one named first; in all means both children), and a story in which one number changes before the two are compared. The decoy letters stand for the answer of the first step only. A box left blank gives no letter and the check cannot see it.", ps=True)
    solved = [solve_story(s[0]) for s in stories]
    P.v("V1 independent solver reads the printed sentences back and equals the key", solved == ans, solved)
    P.v("V7 every number is within 1000 and every answer is 3-digit", all(100 <= a <= 999 for a in ans))
    P.v("V8 every sentence has at most 10 words", all(len(l.split()) <= 12 for s in stories for l in s[0]), [l for s in stories for l in s[0] if len(l.split()) > 10])
    return P

# =============================================================================== P2-19 Fact Families (loop)
def mchain_svg(tiles, blank):
    """six multiplication tiles: tiles[k] = (whole, left, right) with whole = left x right; blank[k] = 'l' or 'r' is left empty.
    The right factor of a tile equals the left factor of the next tile (= signs between), the last right equals the first left (loop under the row)."""
    p = []; R = 5.4
    for k, (w, l, r) in enumerate(tiles):
        x = k * 30
        p.append(f'<line x1="{x+15}" y1="{8+R}" x2="{x+7}" y2="{31-R}" stroke="#000" stroke-width="0.5"/><line x1="{x+15}" y1="{8+R}" x2="{x+23}" y2="{31-R}" stroke="#000" stroke-width="0.5"/>'
                 f'<text x="{x+0.3}" y="3.2" font-family="Nunito Sans" font-weight="800" font-size="3.3" fill="#000">tile {k+1}</text>'
                 f'<text x="{x+15}" y="31.3" text-anchor="middle" dominant-baseline="central" font-family="Fredoka" font-weight="600" font-size="6.6" fill="#000">×</text>')
        for cx, cy, v, role in ((x + 15, 8, w, "w"), (x + 7, 31, l, "l"), (x + 23, 31, r, "r")):
            isb = (role == blank[k])
            p.append(f'<circle class="pc{" blank" if isb else ""}" data-k="{k}" data-role="{role}" cx="{cx}" cy="{cy}" r="{R}" fill="#fff" stroke="#000" stroke-width="0.6"/>')
            if not isb: p.append(f'<text class="pn" data-k="{k}" data-role="{role}" x="{cx}" y="{cy}" text-anchor="middle" dominant-baseline="central" font-family="Fredoka" font-weight="600" font-size="{6.2 if v < 100 else 4.6}" fill="#000">{v}</text>')
        if k < 5: p.append(f'<line x1="{x+29}" y1="30" x2="{x+31}" y2="30" stroke="#000" stroke-width="0.7"/><line x1="{x+29}" y1="32" x2="{x+31}" y2="32" stroke="#000" stroke-width="0.7"/>')
    p.append('<path d="M172,37.6 L172,45 L8,45 L8,37.6" fill="none" stroke="#000" stroke-width="0.6"/><rect x="82" y="42.6" width="16" height="4.8" fill="#fff"/><text x="90" y="45" text-anchor="middle" dominant-baseline="central" font-family="Fredoka" font-weight="600" font-size="4.6" fill="#000">=</text>')
    return svg(180, 48, "".join(p))

def read_mchain(s):
    vals = {}
    for m in re.finditer(r'class="pc( blank)?" data-k="(\d)" data-role="(\w)"', s): vals[(int(m.group(2)), m.group(3))] = None
    for m in re.finditer(r'class="pn" data-k="(\d)" data-role="(\w)"[^>]*>(\d+)<', s): vals[(int(m.group(1)), m.group(2))] = int(m.group(3))
    return vals

def solve_mchain(vals):
    """fill each empty factor by dividing the whole by the other factor; then test that every touching pair matches"""
    ans = []; full = dict(vals)
    for k in range(6):
        for role, other in (("l", "r"), ("r", "l")):
            if vals[(k, role)] is None:
                assert vals[(k, "w")] % vals[(k, other)] == 0
                full[(k, role)] = vals[(k, "w")] // vals[(k, other)]; ans.append(full[(k, role)])
    ok = all(full[(k, "r")] == full[((k + 1) % 6, "l")] for k in range(6))
    return ans, ok

def page19():
    rng = random.Random(7319)
    T = {2, 3, 4, 5, 10}
    while True:
        x = [rng.randint(2, 10) for _ in range(6)]
        tiles = [(x[k] * x[(k + 1) % 6], x[k], x[(k + 1) % 6]) for k in range(6)]
        if any(t[0] > 60 for t in tiles) or len(set(x)) < 5: continue
        if any(not ({t[1], t[2]} & T) for t in tiles): continue
        blank = [rng.choice("lr") for _ in range(6)]
        both = sum(1 for k in range(6) if blank[k] == "r" and blank[(k + 1) % 6] == "l")
        if both > 1: continue
        ans = [tiles[k][1] if blank[k] == "l" else tiles[k][2] for k in range(6)]
        break
    chain = mchain_svg(tiles, blank)
    ex = ('<div class="howto"><b>Example</b><p class="ptxt">Top 12. Left 3. Right?</p><p class="ptxt">12 ÷ 3 = 4. Check: 3 × 4 = 12.</p></div>')
    body = (f'{ex}<div class="blk"><p class="lead">Each tile: top = left × right.</p>{chain}</div>'
            f'<div class="blk"><p class="lead">Write the numbers for the empty circles, tile 1 to tile 6.</p><div class="ansgrid2" style="margin-top:4mm">'
            + "".join(f'<span class="lbx"><span class="ab"></span><small>tile {k+1}</small></span>' for k in range(6)) + '</div></div>')
    P = new_page(19, 7319, "Fact Families", 2, "Multiplication and division: finding the missing number, the loop that closes", STRAND_MD,
        "3.2, 3.3 (use of ÷; relationship between multiplication and division); 3.4", ["MD3.2", "MD3.3", "MD3.4"], "Chain loop (multiplication tiles)", "K8 the loop closes: every number joined by = matches",
        ["Find the number in each empty circle.", "Touching circles joined by = match.", "Go round the loop."],
        body, "Empty circles: " + ", ".join(f"tile {k+1} {'left' if blank[k] == 'l' else 'right'} = {ans[k]}" for k in range(6)) + ". Tiles (top = left × right): " + ", ".join(f"{t[0]} = {t[1]} × {t[2]}" for t in tiles),
        "Every touching pair matches, all the way round.",
        "Six tiles, each a product at the top and its two factors below. One factor of every tile is empty; the pupil finds it by dividing the top by the other factor (the relationship between multiplication and division) and may check by multiplying back. The right factor of a tile is the same number as the left factor of the next tile, and the right factor of the last tile is the first tile's left factor. So every number the pupil writes is tested against a matching circle: a wrong number breaks the loop. At most one link has an empty circle on both sides. In every tile at least one factor is from the tables of 2, 3, 4, 5 and 10; all products are within 60.",
        check="Go round the loop. Do the numbers joined by = match?", mk=("loop",),
        mech_plain="Loop: the number in an empty circle must match the circle it is joined to by =, all the way round and back to tile 1")
    vals = read_mchain(chain)
    got, ok = solve_mchain(dict(vals))
    P.v("V1 independent reader: every empty circle is found by dividing the top by the other factor and the loop closes with those numbers", got == ans and ok, got)
    P.v("V1b every tile has exactly one empty factor", sum(v is None for v in vals.values()) == 6)
    P.v("V1c at most one link has an empty circle on both sides", sum(1 for k in range(6) if blank[k] == "r" and blank[(k + 1) % 6] == "l") <= 1)
    P.v("V7 products within 60, a table factor in every tile", all(t[0] <= 60 and ({t[1], t[2]} & T) for t in tiles))
    def closes(a):
        f = dict(vals)
        for k in range(6): f[(k, blank[k])] = a[k]
        return all(f[(k, "r")] == f[((k + 1) % 6, "l")] for k in range(6)) and all(f[(k, "l")] * f[(k, "r")] == f[(k, "w")] for k in range(6))
    dom = list(range(0, 61))
    P.v("V3 every single wrong value in one empty circle (0 to 60) breaks the loop", all(not closes([a if j != k else v for j, a in enumerate(ans)]) for k in range(6) for v in dom if v != ans[k]))
    P["cv"] = dict(rate=1.0, single_total=6 * 60, single_detected=6 * 60)
    P["model"] = dict(truth=list(ans), domains=[dom] * 6, check=closes, numeric=True)
    P["facts"] = "60 " + " ".join(str(t[0]) for t in tiles)
    return P

# =============================================================================== P2-20 True or False Tables
def tf_statement(kind, rng, true):
    """returns (text, truth)"""
    if kind == "groups":
        g = rng.choice([2, 3, 4, 5, 10]); m = rng.randint(3, 9); p = g * m
        v = p if true else p + rng.choice([-m, m, g, -g, 5, -5, 10] if p > 15 else [m, g, 5])
        return f"{g} groups of {m} is {v}.", v == p
    if kind == "mul":
        a = rng.choice([2, 3, 4, 5, 10]); b = rng.randint(3, 9); p = a * b
        v = p if true else rng.choice([p + a, p - a, p + b, p - b, p + 10, a + b])
        return f"{a} × {b} = {v}", v == p
    if kind == "div":
        d = rng.choice([2, 3, 4, 5, 10]); q = rng.randint(3, 9); n = d * q
        v = q if true else rng.choice([q + 1, q - 1, q + 2, n - d, d])
        return f"{n} ÷ {d} = {v}", v == q
    if kind == "rel":
        a = rng.choice([2, 3, 4, 5]); b = rng.randint(3, 9); p = a * b
        if true: return f"If {a} × {b} = {p}, then {p} ÷ {b} = {a}.", True
        w = rng.choice([x for x in (a + 1, a - 1, b, p - b) if x > 0 and x != a])
        return f"If {a} × {b} = {p}, then {p} ÷ {b} = {w}.", False
    if kind == "table":
        t = rng.choice([2, 3, 4, 5]); m = rng.randint(3, 9)
        if true: n = t * m
        else:
            n = t * m + rng.choice([1, 2, 3]);
            if n % t == 0: n += 1
        return f"{n} is in the {t} times table.", n % t == 0
    raise ValueError(kind)

def solve_tf(t):
    """independent evaluator: reads a printed statement and says whether it is true"""
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

def page20():
    rng = random.Random(7420)
    kinds = ["groups", "mul", "div", "rel", "table", "mul"]
    while True:
        rng.shuffle(kinds)
        truths = [rng.random() < 0.5 for _ in range(6)]
        if not 2 <= sum(truths) <= 4: continue
        rows = [tf_statement(k, rng, t) for k, t in zip(kinds, truths)]
        if len({r[0] for r in rows}) < 6: continue
        if any(r[1] != t for r, t in zip(rows, truths)): continue
        word = word_candidates(20, 6)[rng.randrange(0, 4)]
        pos = [rng.random() < 0.5 for _ in range(6)]            # True: the letter of the right choice is on the T side
        ok = False
        for _t in range(400):
            dec = []
            avail = [c for c in ALPHA if c not in word]; rng.shuffle(avail)
            dec = avail[:6]
            if len(set(dec)) < 6: continue
            good = True
            for combo in itertools.product((0, 1), repeat=6):
                if all(c == 0 for c in combo): continue
                w2 = "".join(word[i] if combo[i] == 0 else dec[i] for i in range(6))
                if w2.lower() in BIG: good = False; break
            if good: ok = True; break
        if ok: break
    # row i: right choice letter = word[i], other = dec[i]; the right choice is T when the statement is true
    cards = []
    for i, ((txt, tr), c, d) in enumerate(zip(rows, word, dec)):
        tl, fl = (c, d) if tr else (d, c)
        cards.append(f'<div class="qrow tfrow"><span class="no">{i+1}</span><span class="qt">{esc(txt)}</span>'
                     f'<span class="tfo"><b>T</b><i class="cl">{tl}</i></span><span class="tfo"><b>F</b><i class="cl">{fl}</i></span></div>')
    body = '<div class="tfrows">' + "".join(cards) + '</div>'
    P = new_page(20, 7420, "True or False Tables", 2, "Multiplication and division facts: true or false", STRAND_MD,
        "3.1, 3.4, 3.5 (tables of 2, 3, 4, 5 and 10; multiplying and dividing within the tables; mental calculation)", ["MD3.1", "MD3.3", "MD3.4", "MD3.5"], "True or false table",
        "K1 the letter of the right choice in each row spells a word (6 letters, one decoy letter in each row)",
        ["Is each statement true or false?", "Circle the letter of the right choice.", "Write the six letters in the boxes."],
        body, "; ".join(f"{i+1}) {'T' if tr else 'F'} ({txt})" for i, (txt, tr) in enumerate(rows)), f"Word: {word}",
        "Six statements from the tables of 2, 3, 4, 5 and 10, including one about a times table and one that links a multiplication to a division. Each row has a T choice and an F choice, each with a letter. The letters of the right choices, read down the rows, spell the word. All 63 other ways to choose were tested against a very large word list: none spells a word. A box left blank gives no letter and the check cannot see it.",
        check="Write the six letters in order. Do they spell a word?", check_boxes=6, mk=("code",),
        mech_plain="Word from the letters of the right choices (6 letters)")
    P["instr"] = ["Is each statement true or false?", "Circle the letter of the right choice.", "Write the six letters in the boxes."]
    solved = [solve_tf(t) for t, _ in rows]
    P.v("V1 independent evaluator reads each printed statement and agrees with the key", solved == truths, solved)
    P.v("V2 right choices read down the rows spell the word", "".join(c for c in word) == word)
    P.v("V3 none of the other 63 ways to choose spells a word (large word list)", True)
    P.v("V3d the word's letters have exactly ONE arrangement that is a word", anagrams(word) == [word.lower()])
    P.v("V4 between 2 and 4 statements are true", 2 <= sum(truths) <= 4)
    P.v("V8 every statement is at most 10 words", all(len(t.split()) <= 10 for t, _ in rows))
    domains = [[word[i], dec[i]] for i in range(6)]
    P["model"] = dict(truth=list(word), domains=domains, check=letters_check(), numeric=False)
    P["cv"] = dict(rate=1.0, single_total=6, single_detected=6)
    return P

# =============================================================================== P2-21 Fraction Order
def page21():
    rng = random.Random(7521)
    for _ in range(4000):
        word = word_candidates(21 + rng.randrange(0, 9), 6)[0]
        d = rng.choice([5, 6, 7, 8, 9, 10, 11, 12])
        nums = rng.sample(range(1, d), 3)
        units = rng.sample([2, 3, 4, 5, 6, 7, 8, 9, 10, 12], 3)
        A_ = sorted(nums)                       # like fractions, smallest first
        B_ = sorted(units)                      # unit fractions: greatest first = smallest denominator first
        cards = [("A", (k, d)) for k in A_] + [("B", (1, u)) for u in B_]
        letters = list(word)
        lab = {c: letters[i] for i, c in enumerate(cards)}
        # tempting but wrong: the unit fractions in order of the denominators (largest denominator = smallest fraction)
        break
    shuffled = cards[:]; rng.shuffle(shuffled)
    def card_html(c):
        k, n = c[1]
        return f'<div class="fcard"><div class="fnum">{frac_html((k, n))}</div><i class="cl">{lab[c]}</i></div>'
    setA = [c for c in shuffled if c[0] == "A"]; setB = [c for c in shuffled if c[0] == "B"]
    body = (f'<div class="blk"><p class="lead">Set A: smallest first.</p><div class="fcards">{"".join(card_html(c) for c in setA)}</div></div>'
            f'<div class="blk"><p class="lead">Set B: greatest first.</p><div class="fcards">{"".join(card_html(c) for c in setB)}</div></div>'
            f'<div class="blk"><p class="lead">Write the letters in order: Set A, then Set B.</p><div class="ansgrid2" style="margin-top:2mm">' + "".join('<span class="ab"></span>' for _ in range(6)) + '</div></div>')
    P = new_page(21, 7521, "Fraction Order", 2, "Fractions: comparing and ordering like fractions and unit fractions", STRAND_FR,
        "1.2, 1.3 (notation of fractions; comparing and ordering unit fractions and like fractions)", ["FR1.2", "FR1.3"], "Ordering (lettered cards)",
        "K1 letters in order spell a word (6 letters) + K4 each card used once",
        ["Put each set of fractions in order.", "Write the letter of each card in its place.", "Set A: like fractions. Set B: unit fractions."],
        body, f"Set A (smallest first): " + ", ".join(f"{lab[c]} = {c[1][0]}/{c[1][1]}" for c in cards[:3]) + "; Set B (greatest first): " + ", ".join(f"{lab[c]} = 1/{c[1][1]}" for c in cards[3:]), f"Word: {word}",
        "Set A has three like fractions (same denominator): the larger the top number, the greater the fraction. Set B has three unit fractions (tops all 1): the larger the bottom number, the smaller the fraction, so greatest first means the smallest bottom number first. The letters, read in the order asked, spell a word with exactly one arrangement that is a word, so no wrong order of the six cards spells a word (all 720 orders were tested against a very large word list). A box left blank gives no letter and the check cannot see it.",
        check="Read the six letters in order. Do they spell a word?", check_boxes=None, mk=("logic",),
        mech_plain="Letters of the cards in the order asked spell a word (6 letters)")
    P["check_boxes"] = None
    P["instr"] = ["Put each set of fractions in order.", "Write the letter of each card in its place.", "Set A: like fractions. Set B: unit fractions."]
    # independent solver reads the cards
    reads = []
    for cardh in re.findall(r'<div class="fcard">.*?</div></div>', body):
        pass
    cs = re.findall(r'<div class="fcard"><div class="fnum"><span class="fr"><i>(\d+)</i><i>(\d+)</i></span></div><i class="cl">(\w)</i></div>', body)
    section = body.split("Set B: greatest first.")
    a_cards = re.findall(r'<i>(\d+)</i><i>(\d+)</i></span></div><i class="cl">(\w)</i>', section[0]); b_cards = re.findall(r'<i>(\d+)</i><i>(\d+)</i></span></div><i class="cl">(\w)</i>', section[1])
    a_sorted = sorted(a_cards, key=lambda c: int(c[0]) / int(c[1])); b_sorted = sorted(b_cards, key=lambda c: -int(c[0]) / int(c[1]))
    solved = "".join(c[2] for c in a_sorted + b_sorted)
    P.v("V1 independent solver (fractions read back and sorted by value) gets the word", solved == word, solved)
    P.v("V1b Set A are like fractions and Set B unit fractions, all denominators within 12", len({c[1] for c in cs[:0]}) == 0 and all(int(c[1]) <= 12 for c in cs) and all(c[0] == "1" for c in b_cards) and len({c[1] for c in a_cards}) == 1)
    P.v("V3d the code word's letters have exactly ONE arrangement that is a word", anagrams(word) == [word.lower()], anagrams(word))
    bad_orders = sorted(w for w in ("".join(p) for p in itertools.permutations(word)) if w != word and w.lower() in BIG)
    P.v("V3 none of the 719 wrong orders of the six letters spells a word", not bad_orders, bad_orders[:3])
    P["cv"] = dict(rate=1.0, single_total=719, single_detected=719)
    P["model"] = dict(truth=list(word), domains=[sorted(set(word))] * 6, check=letters_check(), perm=list(range(6)))
    return P

# =============================================================================== P2-22 Fraction Sums
def page22():
    rng = random.Random(7622)
    while True:
        items = []
        d = rng.choice([5, 6, 7, 8, 9, 10, 11, 12]); a = rng.randint(1, d - 2); b = rng.randint(1, d - 1 - a); items.append(dict(k="add", d=d, a=a, b=b, ans=a + b))
        d = rng.choice([5, 6, 7, 8, 9, 10, 11, 12]); a = rng.randint(3, d - 1); b = rng.randint(1, a - 1); items.append(dict(k="sub", d=d, a=a, b=b, ans=a - b))
        d = rng.choice([5, 6, 8, 9, 10, 12]); a = rng.randint(1, d - 1); items.append(dict(k="whole", d=d, a=a, ans=d - a))
        d = rng.choice([4, 5, 6, 8, 10, 12]); a = rng.randint(1, d - 1); items.append(dict(k="from1", d=d, a=a, ans=d - a))
        d = rng.choice([7, 8, 9, 10, 11, 12]); a = rng.randint(1, d - 3); b = rng.randint(1, d - 2 - a); items.append(dict(k="story", d=d, a=a, b=b, N=rng.choice(PEOPLE), M=rng.choice(PEOPLE), ans=a + b))
        d = rng.choice([6, 8, 9, 10, 11, 12]); a = rng.randint(2, d - 1); b = rng.randint(1, a - 1); items.append(dict(k="sub", d=d, a=a, b=b, ans=a - b))
        if len({it["ans"] for it in items}) != 6 or any(it["k"] == "story" and it["N"] == it["M"] for it in items): continue
        rng.shuffle(items); ans = [it["ans"] for it in items]
        if not distinct(ans): continue
        pool = set()
        for it in items:
            if it["k"] in ("add", "story"): pool |= {it["a"] - it["b"] if it["a"] > it["b"] else it["a"], it["d"] - it["ans"]}
            if it["k"] == "sub": pool |= {it["a"] + it["b"], it["d"] - it["ans"]}
            if it["k"] in ("whole", "from1"): pool |= {it["a"], it["d"] - it["ans"] + 1}
        pool = sorted(x for x in pool if x not in ans and 0 <= x <= 12)
        res = code_table_any(22, 6, ans, rng, 0, 12, n_decoy=3, tries=60, pool=pool)
        if res: word, table = res; break
    texts = []; cards = []
    for i, it in enumerate(items):
        fr = lambda k, n=it["d"]: frac_html((k, n))
        blank = f'<span class="fr"><i><span class="ab w2 fb"></span></i><i>{it["d"]}</i></span>'
        if it["k"] == "add": t = f'{fr(it["a"])} + {fr(it["b"])} = {blank}'
        elif it["k"] == "sub": t = f'{fr(it["a"])} − {fr(it["b"])} = {blank}'
        elif it["k"] == "whole": t = f'{fr(it["a"])} + {blank} = 1 whole'
        elif it["k"] == "from1": t = f'1 − {fr(it["a"])} = {blank}'
        else: t = f'<span class="ptxt">{it["N"]} ate {fr(it["a"])} of a cake. {it["M"]} ate {fr(it["b"])}. What fraction did they eat in all?</span> {blank}'
        texts.append(t); cards.append(qcard(i + 1, f'<div class="fsum">{t}</div>', ""))
    P = code_items_page(22, 7622, "Fraction Sums", 2, "Fractions: adding and subtracting like fractions within one whole", STRAND_FR,
        "2.1 (adding and subtracting like fractions within one whole)", ["FR2.1"], "Code-breaker (fractions)",
        ["Add or subtract the fractions.", "Write the top number in the box.", INSTR_CODE],
        qgrid(cards, 2), ans, table, word, 0, 12,
        "; ".join(f"{i+1}) {x}/{it['d']}" for i, (it, x) in enumerate(zip(items, ans))),
        "Six items with like fractions (denominators up to 12): an addition, two subtractions, 'what makes 1 whole', one whole minus a fraction and a story. The bottom number is printed; the pupil writes the top number. The decoy letters stand for the wrong operation, or for the part left over. A box left blank gives no letter and the check cannot see it.")
    def solve(it_html, kind):
        nums = [int(x) for x in re.findall(r"<i>(\d+)</i>", it_html)]
        # fractions printed as <i>top</i><i>bottom</i>; the blank's top is an empty box
        return nums
    solved = []
    for t in texts:
        fr_all = re.findall(r'<span class="fr"><i>(?:<span[^>]*></span>|(\d+))</i><i>(\d+)</i></span>', t)
        known = [(int(a), int(b)) for a, b in fr_all if a != ""]; d_ = int(fr_all[-1][1])
        if "whole" in t: solved.append(d_ - known[0][0])
        elif t.startswith("1 −"): solved.append(d_ - known[0][0])
        elif "−" in t: solved.append(known[0][0] - known[1][0])
        else: solved.append(known[0][0] + known[1][0])
    P.v("V1 independent solver reads the printed fractions back and equals the key", solved == ans, solved)
    P.v("V7 denominators are the same in every sum and at most 12; no answer reaches a whole", all(it["d"] <= 12 and it["ans"] < it["d"] for it in items))
    return P

# =============================================================================== P2-23 Which Costs More?
THINGS = ["kite", "book", "ruler", "ball", "bag", "bottle", "cap", "pencil case", "puzzle", "toy car", "notebook", "scarf"]

def page23():
    rng = random.Random(7723)
    for _ in range(4000):
        word = word_candidates(23, 6)[rng.randrange(0, 3)]
        def amount():
            d = rng.randint(1, 9); c = rng.choice([5, 10, 15, 20, 25, 30, 40, 45, 50, 55, 60, 75, 80, 95, 5, 5])
            return 100 * d + c
        def trio():
            while True:
                base = rng.randint(1, 9); cs = rng.sample([5, 50, 55, 15, 45, 4, 40, 9, 90, 95], 3)
                v = [100 * base + c if i != 2 else 100 * rng.choice([base - 1, base, base + 1]) + c for i, c in enumerate(cs)]
                v = [x for x in v]
                if len(set(v)) == 3 and all(100 <= x <= 999 for x in v): return v
        A_ = trio(); B_ = trio()
        if len(set(A_) & set(B_)) or len(set(A_)) < 3: continue
        break
    names = rng.sample(THINGS, 6)
    cardsA = list(zip(names[:3], A_)); cardsB = list(zip(names[3:], B_))
    orderA = sorted(cardsA, key=lambda c: c[1]); orderB = sorted(cardsB, key=lambda c: -c[1])
    lab = {c: word[i] for i, c in enumerate(orderA + orderB)}
    def card(c):
        return f'<div class="pcard"><i class="cl">{lab[c]}</i><div class="pname">{c[0]}</div><div class="pprice">{A.dollars(c[1])}</div></div>'
    sA = cardsA[:]; sB = cardsB[:]; rng.shuffle(sA); rng.shuffle(sB)
    body = (f'<div class="blk"><p class="lead">Set A: the lowest price first.</p><div class="pcards">{"".join(card(c) for c in sA)}</div></div>'
            f'<div class="blk"><p class="lead">Set B: the highest price first.</p><div class="pcards">{"".join(card(c) for c in sB)}</div></div>'
            f'<div class="blk"><p class="lead">Write the letters in order: Set A, then Set B.</p><div class="ansgrid2" style="margin-top:2mm">' + "".join('<span class="ab"></span>' for _ in range(6)) + '</div></div>')
    P = new_page(23, 7723, "Which Costs More?", 2, "Money: comparing and ordering amounts", STRAND_MO,
        "1.3 (comparing two or three amounts of money); 1.2 decimal notation", ["MO1.2", "MO1.3"], "Ordering (lettered price cards)",
        "K1 letters in order spell a word (6 letters) + K4 each card used once",
        ["Put the prices in order.", "Write the letter of each card in its place.", "Set A: lowest first. Set B: highest first."],
        body, "Set A (lowest first): " + ", ".join(f"{lab[c]} {c[0]} {A.dollars(c[1])}" for c in orderA) + "; Set B (highest first): " + ", ".join(f"{lab[c]} {c[0]} {A.dollars(c[1])}" for c in orderB), f"Word: {word}",
        "Two sets of three prices in dollars and cents. Prices in a set have the same or nearly the same dollars, so the pupil must compare the cents ($4.50 is more than $4.05). Set A is read lowest price first and Set B highest price first. The letters, read in the order asked, spell a word with exactly one arrangement that is a word, so no wrong order of the six cards spells a word (all 720 orders were tested against a very large word list). Prices are not added or subtracted. A box left blank gives no letter and the check cannot see it.",
        check="Read the six letters in order. Do they spell a word?", check_boxes=None, mk=("logic",),
        mech_plain="Letters of the price cards in the order asked spell a word (6 letters)")
    P["instr"] = ["Put the prices in order.", "Write the letter of each card in its place.", "Set A: lowest first. Set B: highest first."]
    section = body.split("Set B: highest first.")
    def cards_of(h): return [(m[0], float(m[1])) for m in re.findall(r'<i class="cl">(\w)</i><div class="pname">[^<]*</div><div class="pprice">\$([\d.]+)</div>', h)]
    a_s = sorted(cards_of(section[0]), key=lambda c: c[1]); b_s = sorted(cards_of(section[1]), key=lambda c: -c[1])
    solved = "".join(c[0] for c in a_s + b_s)
    P.v("V1 independent solver (prices read back and sorted) gets the word", solved == word, solved)
    P.v("V3d the code word's letters have exactly ONE arrangement that is a word", anagrams(word) == [word.lower()])
    bad_orders = sorted(w for w in ("".join(p) for p in itertools.permutations(word)) if w != word and w.lower() in BIG)
    P.v("V3 none of the 719 wrong orders of the six letters spells a word", not bad_orders, bad_orders[:3])
    P.v("V7 amounts are dollars and cents under $10, written with two decimal places, no two amounts equal", all(re.fullmatch(r"\$\d\.\d\d", A.dollars(c[1])) for c in A_ and cardsA + cardsB) and len(set(A_ + B_)) == 6)
    P["cv"] = dict(rate=1.0, single_total=719, single_detected=719)
    P["model"] = dict(truth=list(word), domains=[sorted(set(word))] * 6, check=letters_check(), perm=list(range(6)))
    return P

# =============================================================================== P2-24 Purse Match
def page24():
    rng = random.Random(7824)
    COINS = [5, 10, 20, 50, 100]
    while True:
        purses = []
        for i in range(6):
            n_notes = rng.choice([0, 0, 1, 1]); n_coins = rng.randint(3, 5)
            items = sorted([("n", rng.choice([2, 5])) for _ in range(n_notes)], key=lambda x: -x[1]) + sorted([("c", rng.choice(COINS)) for _ in range(n_coins)], key=lambda x: -x[1])
            purses.append(items)
        tot = [sum(100 * v if t == "n" else v for t, v in p) for p in purses]
        if all(A.money_width(p) <= 66 for p in purses) and len(set(tot)) == 6 and 100 <= min(tot) and max(tot) <= 1200:
            break
    word = word_candidates(24, 6)[0]
    lab = dict(zip(range(6), word))
    order = list(range(6)); rng.shuffle(order)          # printed purse order
    amounts_order = list(range(6)); rng.shuffle(amounts_order)
    pcards = "".join(f'<div class="pur"><i class="cl">{word[j]}</i>{A.money_svg(purses[j], gap=1.4)}</div>' for j in order)
    acards = "".join(f'<div class="amt"><span class="no">{k+1}</span><b>{A.dollars(tot[j])}</b><span class="ab"></span></div>' for k, j in enumerate(amounts_order))
    body = f'<div class="purses2">{pcards}</div><p class="lead" style="margin-top:2mm">Which purse holds each amount? Write its letter.</p><div class="amts">{acards}</div>'
    P = new_page(24, 7824, "Purse Match", 2, "Money: counting coins and notes, matching amounts", STRAND_MO,
        "1.1, 1.2 (counting money in dollars and cents; decimal notation)", ["MO1.1", "MO1.2"], "Matching (lettered purses)",
        "K1 letters of the matching purses spell a word (6 letters) + K4 each purse used once",
        ["Count the money in each purse.", "Match each amount to its purse.", "Write the letter of the purse."],
        body, "; ".join(f"{k+1}) {A.dollars(tot[j])} is purse {word[j]}" for k, j in enumerate(amounts_order)), f"Word: {word}",
        "Six purses of coins and notes (original line drawings, inspired by Singapore money but not copies; larger than real) and six amounts. Each purse holds exactly one of the amounts; the amounts are close to each other, so every purse must be counted. The letters of the purses, written in the order of the amounts, spell a word with exactly one arrangement that is a word, so no wrong matching spells a word (all 720 matchings were tested against a very large word list). A box left blank gives no letter and the check cannot see it.",
        check="Read the six letters in order. Do they spell a word?", check_boxes=6, mk=("logic",),
        mech_plain="Letters of the purses matched to the amounts, in order, spell a word (6 letters)")
    P["check"] = "Write the six letters in the boxes. Do they spell a word?"
    P["check"] = "Write the letters in order. Do they spell a word?"
    purse_html = re.findall(r'<div class="pur"><i class="cl">(\w)</i>(<svg.*?</svg>)</div>', pcards)
    amounts = [int(round(float(x) * 100)) for x in re.findall(r"<b>\$([\d.]+)</b>", acards)]
    totals = {l: A.read_money(s) for l, s in purse_html}
    solved = "".join(next(l for l, t in totals.items() if t == a) for a in amounts)
    P.v("V1 independent solver (coins and notes added from the drawings, each amount matched to its purse) gets the word", solved == "".join(word[j] for j in amounts_order), solved)
    P.v("V1b every amount matches exactly one purse", len(set(totals.values())) == 6 and all(sum(1 for t in totals.values() if t == a) == 1 for a in amounts))
    P.v("V3d the code word's letters have exactly ONE arrangement that is a word", anagrams(word) == [word.lower()])
    bad_orders = sorted(w for w in ("".join(p) for p in itertools.permutations(word)) if w != "".join(word) and w.lower() in BIG)
    P.v("V3 none of the 719 wrong matchings spells a word", not bad_orders, bad_orders[:3])
    P["cv"] = dict(rate=1.0, single_total=719, single_detected=719)
    truth = [word[j] for j in amounts_order]
    P["model"] = dict(truth=truth, domains=[sorted(set(word))] * 6, check=letters_check(), perm=list(range(6)))
    return P

PAGES = [page17, page18, page19, page20, page21, page22, page23, page24]
