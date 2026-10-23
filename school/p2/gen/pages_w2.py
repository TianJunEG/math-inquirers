"""Wave 2: P2-09 Words and Numbers; P2-10 Digit Cards; P2-11 Number Patterns; P2-12 Odd or Even; P2-13 Missing Digits;
P2-14 Times Table Maze; P2-15 Parts of a Whole; P2-16 Writing Money."""
import random, re, math, itertools
from .common import *
from .kit import *
from .pages_w1 import code_items_page, distinct, STRAND_WN, STRAND_AS, STRAND_MD, STRAND_MO, INSTR_CODE, PEOPLE
from . import art2 as A

STRAND_FR = "Number and Algebra - Fractions"

# =============================================================================== P2-09 Words and Numbers (route)
ONES_W = "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split()
TENS_W = {2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}

def words3(n):
    h, r = divmod(n, 100)
    out = ONES_W[h] + " hundred"
    if r:
        out += " and " + (ONES_W[r] if r < 20 else TENS_W[r // 10] + ("-" + ONES_W[r % 10] if r % 10 else ""))
    return out

_W2N = {w: i for i, w in enumerate(ONES_W)}; _T2N = {w: t for t, w in TENS_W.items()}
def parse_words3(s):
    """the solver's own parser: 'three hundred and forty-one' -> 341 (shares nothing with words3)"""
    toks = s.replace("-", " ").split(); v = 0; i = 0
    h = _W2N[toks[0]]; assert toks[1] == "hundred"; v = 100 * h; i = 2
    if i < len(toks):
        assert toks[i] == "and"; i += 1
        for t in toks[i:]:
            v += _T2N[t] * 10 if t in _T2N else _W2N[t]
    return v

def confusers3(n):
    """what a careless pupil might match: the last two digits swapped, the first two swapped, teen and ty mixed up, a zero moved, one hundred more or less"""
    h, t, o = n // 100, n // 10 % 10, n % 10; out = set()
    if t != o: out.add(100 * h + 10 * o + t)
    if h != t: out.add(100 * t + 10 * h + o)
    if t == 1 and o >= 3: out.add(100 * h + 10 * o)
    if t >= 3 and o == 0: out.add(100 * h + 10 + t)
    if t == 0 and o: out.add(100 * h + 10 * o)
    out |= {n + 10, n - 10, n + 1, n - 1, n + 100 if n < 900 else n - 100}
    return {x for x in out if 100 <= x <= 999 and x != n}

def page09():
    rng = random.Random(5909)
    n = 4; L = 8
    vals = [v for v in range(101, 1000) if v % 100 != 0]
    for _ in range(40000):
        path = random_walk(rng, n, L)
        toks = [rng.choice(vals) for _ in range(L)]
        if len(set(toks)) < L: continue
        top = {}; bot = {}
        for k, c in enumerate(path):
            bot[c] = toks[k]
            if k > 0: top[c] = toks[k - 1]
        top[path[0]] = rng.choice(vals); bot[path[-1]] = rng.choice(vals)
        pool = sorted({x for t in toks for x in confusers3(t)} - set(toks))
        for r in range(n):
            for c in range(n):
                if (r, c) not in top: top[(r, c)] = rng.choice(pool) if rng.random() < .75 else rng.choice(toks)
                if (r, c) not in bot: bot[(r, c)] = rng.choice(vals + pool)
        start, finish = path[0], path[-1]
        nxt = lambda cur, nb: bot[cur] == top[nb]
        if count_routes(lambda c: True, n, start, finish, nxt) != 1: continue
        dead = sum(1 for k, c in enumerate(path[:-1]) for nb in neighbours(*c, n) if nb not in path and nxt(c, nb))
        if not 2 <= dead <= 5: continue
        if len({top[(r, c)] for r in range(n) for c in range(n)}) < 14: continue
        break
    else: raise RuntimeError("p09")
    def wtxt(v):
        w = words3(v)
        if " and " in w: a, b = w.split(" and ", 1); return f"{a}<br>and {b}"
        return w
    texts = [[f'<div class="dm"><span class="dw">{wtxt(top[(r, c)])}</span><span class="dl"></span><span class="dn">{bot[(r, c)]}</span></div>' for c in range(n)] for r in range(n)]
    body = maze_html(n, texts, start, finish)
    P = new_page(9, 5909, "Words and Numbers", 1, "Reading and writing numbers in words and in numerals", STRAND_WN,
        "1.3 (reading and writing numbers in numerals and in words)", ["WN1.3"], "Maze / path", "K6 route closes at FINISH through the stated number of boxes",
        ["Start at START. Move up, down, left or right.", "Go to the box with the word for your number.", "The number is at the foot of the box."],
        body, "Route (row, column from top-left): " + " -> ".join(f"({r+1},{c+1}) {words3(top[(r, c)])} / {bot[(r, c)]}" for r, c in path),
        f"Route reaches FINISH through {L} boxes; every top word names the number at the foot of the box before it.",
        f"A 4 by 4 grid. Each box has a number in words on top and a numeral at the foot. From a box the pupil moves to a touching box whose top words say the numeral at the foot of the box being left. All numbers are 3-digit. Wrong turns are boxes that look right but are not: digits swapped (341 and three hundred and fourteen), teen and ty mixed up (313 and three hundred and thirty), a zero in the wrong place (305 and three hundred and fifty). {dead} wrong turns can be entered from the route and lead nowhere, so the box count and the words matter. Pupils read numbers in words and match them with numerals; writing number words by hand is not checked by this page.",
        check=f"Does your line reach FINISH? Count its boxes: are there {L}? Does each top word match?", mk=("route",),
        mech_plain="Route: each step goes to a box whose top words say the numeral at the foot of the box you leave; the line must reach FINISH through the right number of boxes")
    cells = {}
    for r in range(n):
        for c in range(n):
            m = re.search(r'class="dw">(.*?)</span><span class="dl"></span><span class="dn">(\d+)<', texts[r][c])
            cells[(r, c)] = (parse_words3(m.group(1).replace("<br>", " ")), int(m.group(2)))
    nxt2 = lambda cur, nb: cells[cur][1] == cells[nb][0]
    P.v("V1 exactly one route start->finish when every word and numeral is read back from the printed text (exhaustive search)", count_routes(lambda c: True, n, start, finish, nxt2) == 1)
    P.v("V1b the printed words mean what the generator meant (round trip for all 32 strings)", all(cells[c] == (top[c], bot[c]) for c in cells))
    P.v("V3 wrong turns exist (route boxes with a legal step to an off-route box)", dead >= 2, dead)
    P.v("V3c a shortcut that ignores the rule is shorter than the route, so the box count rejects it", abs(start[0]-finish[0]) + abs(start[1]-finish[1]) + 1 < L)
    P.v("V7 all numbers are 3-digit", all(100 <= x <= 999 for c in cells for x in cells[c]))
    P["cv"] = dict(rate=1.0, single_total=dead, single_detected=dead)
    allcells = [(r, c) for r in range(n) for c in range(n)]
    def legal(rt):
        if len(rt) != L or len(set(rt)) != L or rt[0] != start or rt[-1] != finish: return False
        return all(abs(a[0]-b[0]) + abs(a[1]-b[1]) == 1 for a, b in zip(rt, rt[1:])) and all(cells[a][1] == cells[b][0] for a, b in zip(rt, rt[1:]))
    P["model"] = dict(truth=list(path), domains=[allcells] * L, check=legal, numeric=False)
    P["mini"] = mini_route(n, path)
    P["facts"] = "999 " + " ".join(str(v) for v in range(100, 1000))
    return P

# =============================================================================== P2-10 Digit Cards
def best_numbers(cards, kind):
    """independent brute force over every arrangement of the three digit cards (no leading zero)"""
    nums = sorted({100 * a + 10 * b + c for a, b, c in itertools.permutations(cards) if a != 0})
    if kind == "greatest": return nums[-1]
    if kind == "smallest": return nums[0]
    if kind == "second greatest": return nums[-2]
    if kind == "greatest even": return max(x for x in nums if x % 2 == 0)
    if kind == "smallest odd": return min(x for x in nums if x % 2 == 1)
    if kind == "second smallest": return nums[1]
    raise ValueError(kind)

QTXT = {"greatest": "Make the greatest number.", "smallest": "Make the smallest number.", "second greatest": "Make the second greatest number.",
        "greatest even": "Make the greatest even number.", "smallest odd": "Make the smallest odd number.", "second smallest": "Make the second smallest number."}

def page10():
    rng = random.Random(6010)
    kinds = ["greatest", "smallest", "second greatest", "greatest even", "smallest odd", "second smallest"]
    while True:
        rng.shuffle(kinds); items = []
        for kd in kinds:
            while True:
                cards = rng.sample(range(10), 3)
                if sum(1 for c in cards if c == 0) > 1: continue
                if kd in ("greatest even",) and not any(c % 2 == 0 for c in cards): continue
                if kd == "smallest odd" and not any(c % 2 == 1 for c in cards): continue
                break
            items.append((kd, cards))
        ans = [best_numbers(c, k) for k, c in items]
        if not distinct(ans): continue
        if sum(1 for k, c in items if 0 in c) < 2: continue
        pool = set()
        for k, c in items:
            pool |= {100 * a + 10 * b + cc for a, b, cc in itertools.permutations(c) if a != 0}
        pool = sorted(x for x in pool if x not in ans)
        res = code_table_any(10, 6, ans, rng, 100, 999, n_decoy=3, tries=60, pool=pool)
        if res: word, table = res; break
    cards_h = []
    for i, (kd, cs) in enumerate(items):
        dc = '<div class="dcards">' + "".join(f'<span class="dcard">{c}</span>' for c in cs) + '</div>'
        cards_h.append(qcard(i + 1, dc + f"<p>{QTXT[kd]}</p>", '<span class="ab w3"></span>'))
    P = code_items_page(10, 6010, "Digit Cards", 2, "Numbers to 1000: make, compare and order numbers from digit cards", STRAND_WN,
        "1.2, 1.4 (place values; comparing and ordering numbers); odd and even numbers 1.6", ["WN1.2", "WN1.4", "WN1.6"], "Code-breaker (digit cards)",
        ["Use all three cards once each.", "Make the number. Write it in the box.", INSTR_CODE],
        qgrid(cards_h, 3), ans, table, word, 100, 999,
        "; ".join(f"{i+1}) {k}: {a}" for i, ((k, c), a) in enumerate(zip(items, ans))),
        "Six sets of three digit cards: greatest, smallest, second greatest, second smallest, greatest even and smallest odd. A zero card cannot be the hundreds digit. The decoy letters stand for the other arrangements of the same cards, so a pupil who makes a different number from the same cards still gets a letter, but not the right one. A box left blank gives no letter and the check cannot see it.")
    solved = []
    for h, (kd, cs) in zip(cards_h, items):
        digs = [int(x) for x in re.findall(r'class="dcard">(\d)<', h)]
        q = re.search(r"Make the ([a-z ]+) number", h).group(1)
        solved.append(best_numbers(digs, q))
    P.v("V1 independent solver (every arrangement of the printed cards tried) equals the key", solved == ans, solved)
    P.v("V1b cards in one item are all different digits", all(len(set(c)) == 3 for k, c in items))
    P.v("V7 answers are 3-digit numbers", all(100 <= a <= 999 for a in ans))
    return P

# =============================================================================== P2-11 Number Patterns
def pattern_row(rng, step, start, length=6):
    return [start + step * i for i in range(length)]

def solve_pattern(cells):
    """independent: read a printed sequence with one '?' and return the missing number (constant difference)"""
    known = [(i, int(c)) for i, c in enumerate(cells) if c != "?"]
    (i1, v1), (i2, v2) = known[0], known[1]
    d = (v2 - v1) // (i2 - i1)
    j = cells.index("?")
    return v1 + d * (j - i1)

def page11():
    rng = random.Random(6111)
    steps = [2, 3, 4, 5, 10, 100, -2, -5, -10, -100]
    while True:
        rows = []
        chosen = rng.sample(steps, 6)
        for st in chosen:
            for _ in range(200):
                s0 = rng.randint(120, 880) if abs(st) == 100 else rng.randint(100, 900)
                if abs(st) in (10, 100): s0 = s0 // 10 * 10
                seq = [s0 + st * i for i in range(6)]
                if min(seq) >= 0 and max(seq) <= 1000 and min(seq) >= 10: break
            gap = rng.choice([1, 2, 3, 4])
            if abs(st) == 100: gap = rng.choice([1, 2, 3, 4])
            rows.append((st, seq, gap))
        ans = [seq[gap] for st, seq, gap in rows]
        if not distinct(ans) or max(ans) > 1000: continue
        if sum(1 for st, seq, g in rows if (seq[g] // 100 != seq[g - 1] // 100 or seq[g] // 100 != seq[g + 1] // 100 if 0 < g < 5 else False)) < 2: continue
        pool = set()
        for st, seq, g in rows:
            pool |= {seq[g] + 10, seq[g] - 10, seq[g] + 100, seq[g] - 100, seq[g] + 1, seq[g] - 1, seq[g] + st, seq[g] - st}
        pool = sorted(x for x in pool if x not in ans and 0 <= x <= 1000)
        res = code_table_any(11, 6, ans, rng, 0, 1000, n_decoy=3, tries=60, pool=pool)
        if res: word, table = res; break
    items = []; cells_all = []
    for i, (st, seq, g) in enumerate(rows):
        cells = ["?" if j == g else str(v) for j, v in enumerate(seq)]; cells_all.append(cells)
        seqh = '<div class="seq">' + "".join(('<span class="ab w3"></span>' if c == "?" else f'<span class="sq">{c}</span>') for c in cells) + '</div>'
        items.append(f'<div class="srow"><span class="no">{i+1}</span>{seqh}</div>')
    P = code_items_page(11, 6111, "Number Patterns", 2, "Number patterns: counting on and back in 2s, 3s, 4s, 5s, 10s and 100s", STRAND_WN,
        "1.1, 1.5 (counting in tens and hundreds; patterns in number sequences)", ["WN1.1", "WN1.5"], "Code-breaker (sequences)",
        ["Find the rule. Write the missing number.", "Each row counts on or back by the same amount.", INSTR_CODE],
        '<div class="sqrows">' + "".join(items) + '</div>', ans, table, word, 0, 1000,
        "; ".join(f"{i+1}) {'+' if st > 0 else '-'}{abs(st)}: missing {a}" for i, ((st, seq, g), a) in enumerate(zip(rows, ans))),
        "Six rows, each counting on or back by 2, 3, 4, 5, 10 or 100 (one rule per row, all different). Several rows cross a hundred, so the hundreds digit changes. The decoy letters stand for the usual slips: the step added twice, or only one digit changed. A box left blank gives no letter and the check cannot see it.")
    solved = [solve_pattern(c) for c in cells_all]
    P.v("V1 independent solver (constant difference from the printed numbers) equals the key", solved == ans, solved)
    P.v("V1b at least two known numbers are printed in every row, so the rule is fixed", all(sum(1 for c in cs if c != "?") >= 5 for cs in cells_all))
    P.v("V1c the six rules are all different", len({abs(st) if st > 0 else -abs(st) for st, s, g in rows}) == 6)
    P.v("V7 numbers within 1000", all(0 < v <= 1000 for st, seq, g in rows for v in seq))
    return P

# =============================================================================== P2-12 Odd or Even (route)
def page12():
    rng = random.Random(6212)
    n = 4; L = 8
    for _ in range(40000):
        want = rng.choice(["EVEN", "ODD"])
        par = 0 if want == "EVEN" else 1
        path = random_walk(rng, n, L)
        grid = {}
        def num(p):
            while True:
                v = rng.randint(100, 998)
                if v % 2 == p and v % 10 != 0 or (p == 0 and v % 10 == 0 and rng.random() < .15): return v
        for c in path: grid[c] = num(par)
        dead = 0
        for p in path[:-1]:
            if dead >= 3: break
            opts = [q for q in neighbours(*p, n) if q not in grid]
            if opts and rng.random() < .5:
                q = rng.choice(opts); grid[q] = num(par); dead += 1
        for r in range(n):
            for c in range(n):
                if (r, c) not in grid: grid[(r, c)] = num(1 - par)
        # make wrong boxes tempting: some wrong numbers have the other parity in the tens place or end in 0/5 patterns
        start, finish = path[0], path[-1]
        ok = lambda cell: grid[cell] % 2 == par
        if count_routes(ok, n, start, finish) == 1 and 2 <= dead <= 3 and len(set(grid.values())) == 16: break
    else: raise RuntimeError("p12")
    texts = [[str(grid[(r, c)]) for c in range(n)] for r in range(n)]
    body = maze_html(n, texts, start, finish)
    P = new_page(12, 6212, "Odd or Even", 1, f"Odd and even numbers: {want.lower()} numbers", STRAND_WN,
        "1.6 (odd and even numbers)", ["WN1.6"], "Maze / path", "K6 route closes at FINISH",
        ["Start at START. Move up, down, left or right.", f"Step only on {want} numbers.", "Do not step on a box twice."],
        body, "Route (row, column from top-left): " + " -> ".join(f"({r+1},{c+1}) {grid[(r, c)]}" for r, c in path),
        f"Route reaches FINISH through {L} boxes; every box on it is {want.lower()}.",
        f"A 4 by 4 grid of sixteen 3-digit numbers. The route follows {want.lower()} numbers: the pupil looks at the last digit. The other boxes hold the other kind of number; {dead} extra {want.lower()} boxes are dead ends. Counting the boxes shows a line that takes a shortcut.",
        check=f"Does your line reach FINISH? Count its boxes: are there {L}? Is every box {want.lower()}?", mk=("route",),
        mech_plain=f"Route: the line must reach FINISH through the right number of boxes, every box {want.lower()}")
    g2 = {(r, c): int(texts[r][c]) for r in range(n) for c in range(n)}
    ok2 = lambda cell: (g2[cell] % 2 == 0) == (want == "EVEN")
    P.v("V1 exactly one route start->finish (exhaustive search, parity read from the printed numbers)", count_routes(ok2, n, start, finish) == 1)
    P.v("V3 dead-end boxes of the right kind exist", dead >= 2, dead)
    P.v("V3b a shortcut that ignores the rule is shorter than the route", abs(start[0]-finish[0]) + abs(start[1]-finish[1]) + 1 < L)
    P.v("V7 all sixteen numbers are different 3-digit numbers", len(set(g2.values())) == 16 and all(100 <= v <= 999 for v in g2.values()))
    P["cv"] = dict(rate=1.0, single_total=dead, single_detected=dead)
    allcells = [(r, c) for r in range(n) for c in range(n)]
    def legal(rt):
        if len(rt) != L or len(set(rt)) != L or rt[0] != start or rt[-1] != finish: return False
        return all(ok2(c) for c in rt) and all(abs(a[0]-b[0]) + abs(a[1]-b[1]) == 1 for a, b in zip(rt, rt[1:]))
    P["model"] = dict(truth=list(path), domains=[allcells] * L, check=legal, numeric=False)
    P["mini"] = mini_route(n, path)
    P["facts"] = " ".join(str(v) for v in g2.values())
    return P

# =============================================================================== P2-13 Missing Digits
def page13():
    rng = random.Random(6313)
    while True:
        items = []
        for k in range(6):
            op = "+" if k % 2 == 0 else "-"
            if op == "+":
                a = rng.randint(120, 690); b = rng.randint(110, 999 - a); r = a + b
            else:
                a = rng.randint(400, 990); b = rng.randint(110, a - 100); r = a - b
            which = rng.choice([0, 1, 2]); pos = rng.randint(0, 2)
            sa, sb, sr = str(a), str(b), str(r)
            rows = [list(sa), list(sb), list(sr)]
            dig = int(rows[which][pos]); rows[which][pos] = "?"
            items.append(dict(op=op, rows=["".join(x) for x in rows], dig=dig, a=a, b=b, r=r))
        ans = [it["dig"] for it in items]
        rng.shuffle(items); ans = [it["dig"] for it in items]
        def unique(it):
            sols = []
            for d in range(10):
                rr = [x.replace("?", str(d)) for x in it["rows"]]
                if any(x[0] == "0" and len(x) > 1 for x in rr): continue
                a_, b_, r_ = map(int, rr)
                if (a_ + b_ == r_ if it["op"] == "+" else a_ - b_ == r_): sols.append(d)
            return sols == [it["dig"]]
        if not distinct(ans) or not all(unique(it) for it in items): continue
        pool = [d for d in range(10) if d not in ans]
        res = code_table_any(13, 6, ans, rng, 0, 9, n_decoy=2, tries=80, pool=pool)
        if res: word, table = res; break
    hs = [vsum_html(it["rows"][0], it["rows"][1], "+" if it["op"] == "+" else "−", res=it["rows"][2]) for it in items]
    cards = "".join(f'<div class="vcard"><span class="no">{i+1}</span>{h}</div>' for i, h in enumerate(hs))
    P = code_items_page(13, 6313, "Missing Digits", 2, "Add and subtract in columns: find the missing digit", STRAND_AS,
        "2.1 (addition and subtraction algorithms, up to 3 digits)", ["AS2.1"], "Code-breaker (written methods)",
        ["One digit is missing from each sum.", "Write the missing digit in the box.", INSTR_CODE],
        f'<div class="vcards">{cards}</div>', ans, table, word, 0, 9,
        "; ".join(f"{i+1}) {it['rows'][0].replace('?', str(it['dig']))} {it['op']} {it['rows'][1].replace('?', str(it['dig']))} = {it['rows'][2].replace('?', str(it['dig']))}: digit {it['dig']}" for i, it in enumerate(items)),
        "Six column sums with one digit missing (three additions, three subtractions, the missing digit in the top number, the bottom number or the answer). Each has exactly one digit that makes it true. The pupil writes the missing digit, then looks it up. A digit that is wrong either has a decoy letter or no letter. A box left blank gives no letter and the check cannot see it.")
    solved = []
    for h in hs:
        t, b, r, op = parse_vsum3(h)
        sols = []
        for d in range(10):
            rr = [x.replace("?", str(d)) for x in (t, b, r)]
            if any(x[0] == "0" for x in rr): continue
            a_, b_, r_ = map(int, rr)
            if (a_ + b_ == r_ if op == "+" else a_ - b_ == r_): sols.append(d)
        solved.append(sols[0] if len(sols) == 1 else sols)
    P.v("V1 independent solver (every digit tried in the printed sum) finds exactly one digit and it equals the key", solved == ans, solved)
    P.v("V7 every number has 3 digits", all(len(x) == 3 for it in items for x in it["rows"]))
    return P

# =============================================================================== P2-14 Times Table Maze
def facts_equal(T):
    """every multiplication and division fact from the tables of 2, 3, 4, 5, 10 with answer T (factors and quotients up to 10, no x 1)"""
    out = set()
    for f in (2, 3, 4, 5, 10):
        for q in range(1 if f == 10 else 2, 11):
            if f * q == T: out |= {f"{f} \u00d7 {q}", f"{q} \u00d7 {f}"}
        if T <= 10: out.add(f"{T * f} \u00f7 {f}")
    return sorted(out)

def eval_fact(s):
    m = re.fullmatch(r"(\d+) ([×÷]) (\d+)", s)
    a, op, b = int(m.group(1)), m.group(2), int(m.group(3))
    return a * b if op == "×" else a // b

def page14():
    rng = random.Random(6414)
    n = 4; L = 7
    T = 10; good = facts_equal(T)
    others = {}
    for f in (2, 3, 4, 5, 10):
        for q in range(2, 11):
            v = f * q
            if v != T and 4 <= v <= 40 and abs(v - T) <= 8: others.setdefault(v, []).extend([f"{f} × {q}", f"{q} × {f}"])
            if v != T and q <= 10 and 3 <= q <= 14 and abs(q - T) <= 3 and v <= 100: others.setdefault(q, []).append(f"{v} ÷ {f}")
    bad = sorted({x for lst in others.values() for x in lst if eval_fact(x) != T and "× 1 " not in x})
    for _ in range(40000):
        path = random_walk(rng, n, L, min_dist=3)
        if abs(path[0][0] - path[-1][0]) + abs(path[0][1] - path[-1][1]) + 1 >= L: continue
        grid = {}
        pick = rng.sample(good, len(good))
        if len(pick) < L + 2: continue
        for k, c in enumerate(path): grid[c] = pick[k]
        used = set(pick[:L]); dead = 0
        for p in path[:-1]:
            if dead >= 2: break
            opts = [q for q in neighbours(*p, n) if q not in grid]
            if opts and rng.random() < .6:
                q = rng.choice(opts); grid[q] = pick[L + dead]; dead += 1
        for r in range(n):
            for c in range(n):
                if (r, c) not in grid: grid[(r, c)] = rng.choice(bad)
        start, finish = path[0], path[-1]
        ok = lambda cell: eval_fact(grid[cell]) == T
        if count_routes(ok, n, start, finish) == 1 and dead == 2 and len(set(grid.values())) == 16: break
    else: raise RuntimeError("p14")
    texts = [[grid[(r, c)] for c in range(n)] for r in range(n)]
    body = maze_html(n, texts, start, finish)
    P = new_page(14, 6414, "Times Table Maze", 1, "Multiplication and division facts: tables of 2, 3, 4, 5 and 10", STRAND_MD,
        "3.1, 3.5 (tables of 2, 3, 4, 5, 10; mental calculation within the tables); 3.2 ÷", ["MD3.1", "MD3.2", "MD3.5"], "Maze / path", "K6 route closes at FINISH",
        ["Start at START. Move up, down, left or right.", f"Step only on boxes with the answer {T}.", "Do not step on a box twice."],
        body, "Route (row, column from top-left): " + " -> ".join(f"({r+1},{c+1}) {grid[(r, c)]}" for r, c in path),
        f"Route reaches FINISH through {L} boxes; every box on it makes {T}.",
        f"A 4 by 4 grid of sixteen multiplication and division facts from the tables of 2, 3, 4, 5 and 10. The route follows the boxes that make {T}. Wrong boxes have answers close to {T}. {dead} extra boxes that do make {T} are dead ends. Counting the boxes shows a line that takes a shortcut.",
        check=f"Does your line reach FINISH? Count its boxes: are there {L}? Does every box make {T}?", mk=("route",),
        mech_plain=f"Route: the line must reach FINISH through the right number of boxes, every box making {T}")
    g2 = {(r, c): texts[r][c] for r in range(n) for c in range(n)}
    ok2 = lambda cell: eval_fact(g2[cell]) == T
    P.v("V1 exactly one route start->finish (exhaustive search, facts evaluated from the printed text)", count_routes(ok2, n, start, finish) == 1)
    P.v("V3 dead-end boxes that also make the target exist", dead >= 2, dead)
    P.v("V3b a shortcut that ignores the rule is shorter than the route", abs(start[0]-finish[0]) + abs(start[1]-finish[1]) + 1 < L)
    P.v("V7 every fact uses a table of 2, 3, 4, 5 or 10 and the quotient or factor is at most 10", all(any(int(x) in (2, 3, 4, 5, 10) for x in re.findall(r"\d+", t)[:2]) or re.findall(r"\d+", t)[1] in ("2", "3", "4", "5", "10") for t in g2.values()))
    P.v("V7b all sixteen boxes are different", len(set(g2.values())) == 16)
    P["cv"] = dict(rate=1.0, single_total=dead, single_detected=dead)
    allcells = [(r, c) for r in range(n) for c in range(n)]
    def legal(rt):
        if len(rt) != L or len(set(rt)) != L or rt[0] != start or rt[-1] != finish: return False
        return all(ok2(c) for c in rt) and all(abs(a[0]-b[0]) + abs(a[1]-b[1]) == 1 for a, b in zip(rt, rt[1:]))
    P["model"] = dict(truth=list(path), domains=[allcells] * L, check=legal, numeric=False)
    P["mini"] = mini_route(n, path)
    P["facts"] = f"{T} " + " ".join(re.findall(r"\d+", " ".join(g2.values())))
    return P

# =============================================================================== P2-15 Parts of a Whole
def frac_fig(kind, n, shaded, rng):
    """a figure cut into n EQUAL parts with the parts in `shaded` black (white separators inside black areas); kind: bar, circle, grid (rows x cols)"""
    def part(tag, geom, i):
        sh = i in shaded
        return f'<{tag} class="part{" sh" if sh else ""}" {geom} fill="{"#000" if sh else "#fff"}" stroke="{"#fff" if sh else "#000"}" stroke-width="{0.9 if sh else 0.6}" stroke-linejoin="round"/>'
    items = []; outline = ""
    if kind == "bar":
        w = 48.0; h = 13.0; u = w / n
        for i in range(n): items.append((i, part("rect", f'x="{1+i*u:.2f}" y="1" width="{u:.2f}" height="{h}"', i)))
        outline = f'<rect x="1" y="1" width="{w}" height="{h}" fill="none" stroke="#000" stroke-width="0.8"/>'; W, H = w + 2, h + 2
    elif kind == "circle":
        r = 12.5; cx = cy = r + 1
        for i in range(n):
            a0 = -math.pi / 2 + 2 * math.pi * i / n; a1 = -math.pi / 2 + 2 * math.pi * (i + 1) / n
            x0, y0 = cx + r * math.cos(a0), cy + r * math.sin(a0); x1, y1 = cx + r * math.cos(a1), cy + r * math.sin(a1)
            items.append((i, part("path", f'd="M{cx},{cy} L{x0:.2f},{y0:.2f} A{r},{r} 0 0 1 {x1:.2f},{y1:.2f} Z"', i)))
        outline = f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="#000" stroke-width="0.8"/>'; W = H = 2 * r + 2
    else:
        rows, cols = {4: (2, 2), 6: (2, 3), 8: (2, 4), 9: (3, 3), 10: (2, 5), 12: (3, 4)}[n]
        u = 9.5
        for i in range(n):
            rr, cc = divmod(i, cols)
            items.append((i, part("rect", f'x="{1+cc*u:.2f}" y="{1+rr*u:.2f}" width="{u}" height="{u}"', i)))
        outline = f'<rect x="1" y="1" width="{cols*u}" height="{rows*u}" fill="none" stroke="#000" stroke-width="0.8"/>'; W, H = cols * u + 2, rows * u + 2
    ordered = [x for i, x in items if i in shaded] + [x for i, x in items if i not in shaded]      # white parts last, so their outlines stay visible
    return svg(round(W, 1), round(H, 1), "".join(ordered) + outline)

def read_frac(s):
    parts = re.findall(r'class="part( sh)?"', s)
    return len(re.findall(r'class="part sh"', s)), len(parts)

def page15():
    rng = random.Random(6515)
    fr_pool = [(k, n) for n in (3, 4, 5, 6, 8, 10, 12) for k in range(1, n) if math.gcd(k, n) == 1]
    while True:
        picks = rng.sample(fr_pool, 6)
        kinds = [rng.choice(["bar", "circle", "grid"]) for _ in range(6)]
        for i, (k, n) in enumerate(picks):
            if kinds[i] == "grid" and n not in (4, 6, 8, 9, 10, 12): kinds[i] = rng.choice(["bar", "circle"])
        if len({n for k, n in picks}) < 4 or len({k for k, n in picks}) < 4: continue
        ans = list(picks)
        pool = set()
        for k, n in picks:
            pool |= {(n - k, n), (k + 1, n) if k + 1 < n else (k - 1, n), (k - 1, n) if k > 1 else (k + 1, n), (k, n + 1) if n < 12 else (k, n - 1)}
        pool = sorted(x for x in pool if x not in ans and 1 <= x[0] < x[1] <= 12)
        domain = [(k, n) for n in range(2, 13) for k in range(1, n)]
        res = code_table_any(15, 6, ans, rng, 0, 0, n_decoy=4, tries=80, pool=pool, domain=domain)
        if res: word, table = res; break
    figs = []
    for (k, n), kd in zip(picks, kinds):
        figs.append(frac_fig(kd, n, set(rng.sample(range(n), k)), rng))
    ansbox = '<div class="fans"><span class="ab w2"></span><span class="fline"></span><span class="ab w2"></span></div>'
    cards = [qcard(i + 1, f'<div class="ffig">{f}</div>', ansbox, cls="inl") for i, f in enumerate(figs)]
    P = code_items_page(15, 6515, "Parts of a Whole", 1, "Fractions: parts of a whole, shaded parts", STRAND_FR,
        "1.1, 1.2 (fraction as part of a whole; notation and representations of fractions)", ["FR1.1", "FR1.2"], "Code-breaker (fractions)",
        ["Each shape has equal parts.", "Write the shaded part as a fraction.", INSTR_CODE],
        qgrid(cards, 2), ans, table, word, 0, 0,
        "; ".join(f"{i+1}) {k}/{n}" for i, (k, n) in enumerate(picks)),
        "Six figures (bars, circles and grids) cut into equal parts, with some parts shaded black. The pupil writes the shaded part as a fraction (top box: shaded parts, bottom box: all the equal parts). No fraction is one that can be written in simpler parts (no 2/4 or 3/6): equivalent fractions are Primary 3. The decoy letters stand for reading the unshaded parts, or counting one part too many. A box left blank gives no letter and the check cannot see it.",
        domain=domain, fmt=frac_html)
    solved = [read_frac(f) for f in figs]
    P.v("V1 independent solver counts the shaded and all parts in each drawing and equals the key", solved == picks, solved)
    P.v("V1b every fraction is in simplest form", all(math.gcd(k, n) == 1 for k, n in picks))
    P.v("V7 denominators within 12", all(n <= 12 for k, n in picks))
    P["facts"] = " ".join(f"{k} {n}" for k, n in list(table))
    return P

# =============================================================================== P2-16 Writing Money
def page16():
    rng = random.Random(6616)
    while True:
        items = []
        d = rng.randint(2, 9); c = rng.choice([x for x in range(11, 99) if x % 10 and x % 5]); items.append(dict(k="d2c", d=d, c=c))
        d = rng.randint(2, 9); c = rng.randint(1, 9); items.append(dict(k="d2c", d=d, c=c))                                    # $4.05: the zero place holder
        v = rng.choice([x for x in range(210, 980) if x % 10 and x % 100 > 9]); items.append(dict(k="c2d", v=v))
        v = rng.choice([x for x in range(105, 909) if x % 100 in (5, 6, 7, 8, 9, 2, 3, 4)]); items.append(dict(k="c2d", v=v))   # 608 cents: $6.08
        d = rng.randint(2, 9); c = rng.choice([x for x in range(10, 99) if x % 10]); items.append(dict(k="words", d=d, c=c))
        v = rng.choice([x for x in range(45, 99) if x % 5 == 0 or x % 2]); items.append(dict(k="c2d", v=v))                      # 85 cents: $0.85
        vals = [it["d"] * 100 + it["c"] if "d" in it else it["v"] for it in items]
        rng.shuffle(items); vals = [it["d"] * 100 + it["c"] if "d" in it else it["v"] for it in items]
        if not distinct(vals) or max(vals) > 999: continue
        style = {}
        for it, v in zip(items, vals): style[v] = "c" if it["k"] == "d2c" else "d"
        pool = {}
        for it, v in zip(items, vals):
            st = style[v]
            d_, c_ = divmod(v, 100)
            for w in {v * 10 if v < 100 else v // 10, d_ * 10 + c_, c_ * 100 + d_ if c_ >= 10 else v + 5, (d_ * 100 + (c_ % 10) * 10 + c_ // 10), v + 10, v - 10, v + 100, v - 100, c_ if c_ else v}:
                if w not in vals and 1 <= w <= 999 and w not in pool: pool[w] = st
        res = code_table_any(16, 6, vals, rng, 1, 999, n_decoy=3, tries=60, pool=sorted(pool), domain=list(range(1, 1000)))
        if res: word, table = res; break
    fmt = lambda v: A.dollars(v) if style.get(v, pool.get(v, "c")) == "d" else f"{v}¢"
    texts = []; cards = []
    for i, it in enumerate(items):
        if it["k"] == "d2c": t = f"${it['d']}.{it['c']:02d} = ? ¢"; ans_h = '<span class="ab w3"></span> ¢'
        elif it["k"] == "c2d": t = f"{it['v']}¢ = $ ?"; ans_h = '<span class="dl">$</span><span class="ab w4"></span>'
        else: t = f"{it['d']} dollars and {it['c']} cents = $ ?"; ans_h = '<span class="dl">$</span><span class="ab w4"></span>'
        texts.append(t); cards.append(qcard(i + 1, f"<p>{t}</p>", ans_h))
    P = code_items_page(16, 6616, "Writing Money", 2, "Money: decimal notation and cents", STRAND_MO,
        "1.2, 1.4 (reading and writing money in decimal notation; converting decimal notation to cents only, and vice versa)", ["MO1.2", "MO1.4"], "Code-breaker (money notation)",
        ["Write each amount a different way.", "Cents: write a number. Dollars: write like $2.50.", INSTR_CODE],
        qgrid(cards, 2), vals, table, word, 1, 999,
        "; ".join(f"{i+1}) {t.replace(' ?', '')} {fmt(v)}" for i, (t, v) in enumerate(zip(texts, vals))),
        "Three amounts in dollars and cents are changed to cents (one has a zero in the cents, as in $4.05) and three amounts in cents or in words are written in decimal notation (one is under 100 cents, as in 85¢ = $0.85). The decoy letters stand for slips with a zero or the point in the wrong place. The table shows each answer in the form the pupil writes. A box left blank gives no letter and the check cannot see it.",
        domain=list(range(1, 1000)), fmt=fmt)
    def solve(t):
        m = re.fullmatch(r"\$(\d+)\.(\d\d) = \? ¢", t)
        if m: return 100 * int(m.group(1)) + int(m.group(2))
        m = re.fullmatch(r"(\d+)¢ = \$ \?", t)
        if m: return int(m.group(1))
        m = re.fullmatch(r"(\d+) dollars and (\d+) cents = \$ \?", t)
        return 100 * int(m.group(1)) + int(m.group(2))
    solved = [solve(t) for t in texts]
    P.v("V1 independent solver reads the printed text and equals the key", solved == vals, solved)
    P.v("V7 amounts under $10", max(vals) < 1000)
    P["facts"] = " ".join(str(v) for v in table) + " " + " ".join(A.dollars(v) for v in table)
    return P

PAGES = [page09, page10, page11, page12, page13, page14, page15, page16]
