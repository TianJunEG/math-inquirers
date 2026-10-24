"""Semester 1, pages P3-06 to P3-09: addition and subtraction to 4 digits, mental sums of two 2-digit numbers, the tables of 6 to 9.
P3-06 Big Sums; P3-07 Mental Pairs (route); P3-08 Missing Digits; P3-09 Tables Maze (route)."""
import random, re, itertools
from .common import *
from .kit import *
from .p3kit import *

# =============================================================================== P3-06 Big Sums
def wrong_column(op, a, b):
    """what a pupil gets by not renaming: digit by digit without carrying or borrowing"""
    sa, sb = str(a).zfill(4), str(b).zfill(4)
    if op == "+": return int("".join(str((int(x) + int(y)) % 10) for x, y in zip(sa, sb)))
    return int("".join(str(abs(int(x) - int(y))) for x, y in zip(sa, sb)))

def big_sums(rng):
    out = []
    def r4(lo, hi): return rng.randint(lo, hi)
    while True:                                                         # add, no renaming
        a = r4(1000, 4999); b = r4(1000, 4999)
        if all(int(x) + int(y) < 10 for x, y in zip(str(a), str(b))): break
    out.append(("+", a, b))
    while True:                                                         # add, ones and tens renamed
        a = r4(1200, 6900); b = r4(1100, 2900)
        if a % 10 + b % 10 >= 10 and (a // 10 % 10 + b // 10 % 10 + 1) >= 10 and (a // 100 % 10 + b // 100 % 10 + 1) < 10 and a + b < 10000: break
    out.append(("+", a, b))
    while True:                                                         # add, hundreds renamed into the thousands
        a = r4(2000, 6900); b = r4(1000, 3900)
        if a // 100 % 10 + b // 100 % 10 >= 10 and a % 100 + b % 100 < 100 and a + b < 10000: break
    out.append(("+", a, b))
    while True:                                                         # subtract, no renaming
        a = r4(4000, 9900); b = r4(1000, a - 1000)
        if all(int(x) >= int(y) for x, y in zip(str(a), str(b))) and a % 10 != b % 10: break
    out.append(("-", a, b))
    while True:                                                         # subtract, renaming tens and hundreds
        a = r4(3000, 9900); b = r4(1000, a - 500)
        if a % 10 >= b % 10 and a // 10 % 10 < b // 10 % 10 and a // 100 % 10 >= b // 100 % 10 and a // 1000 > b // 1000: break
    out.append(("-", a, b))
    while True:                                                         # subtract across a zero (a zero in the tens place of the top number)
        a = rng.randint(4, 9) * 1000 + rng.choice([0, 3, 4, 5, 6, 7, 8]) * 100 + rng.randint(1, 5)
        b = r4(1100, a - 1000)
        if a % 10 < b % 10 and b // 10 % 10 > 0: break
    out.append(("-", a, b))
    return out

def page06():
    rng = random.Random(3606)
    while True:
        sums = big_sums(rng); rng.shuffle(sums)
        ans = [a + b if op == "+" else a - b for op, a, b in sums]
        if not distinct(ans) or max(ans) > 9999 or min(ans) < 100: continue
        pool = sorted({wrong_column(*s) for s in sums} | {a + 10 for a in ans} | {a - 100 for a in ans if a > 1100} | {a + 100 for a in ans if a < 9800} | {a - 1000 for a in ans if a > 2000} | {a + 1000 for a in ans if a < 8900})
        pool = [p for p in pool if p not in ans and p > 0]
        res = find_table(6, 6, ans, rng, 0, 9999, pool, n_decoy=3, tries=30)
        if res: word, table = res; break
    hs = [vsum4(a, b, "+" if op == "+" else "−") for op, a, b in sums]
    cards = "".join(f'<div class="vcard"><span class="no">{i+1}</span>{h}</div>' for i, h in enumerate(hs))
    P = code_items_page(6, 3606, "Big Sums", 1, "Add and subtract in columns, 4-digit numbers", STRAND_AS,
        "2.1 (addition and subtraction algorithms, up to 4 digits)", ["AS2.1"], "Code-breaker (written methods)",
        ["Work out each sum in columns.", "Write the answer in the box.", INSTR_CODE],
        f'<div class="vcards">{cards}</div>', ans, table, word, 0, 9999,
        "; ".join(f"{i+1}) {a} {op} {b} = {x}" for i, ((op, a, b), x) in enumerate(zip(sums, ans))),
        "Six vertical sums within 10 000: three additions (no renaming, ones and tens renamed, hundreds renamed into the thousands) and three subtractions (no renaming, tens and hundreds renamed, and one with a zero in the top number). The decoy letters stand for the answers a pupil gets by not renaming (adding or subtracting digit by digit). A box left blank gives no letter and the check cannot see it.")
    solved = []
    for h in hs:
        (a, b), op = [x for x in parse_vsum4(h)[0][:2]], parse_vsum4(h)[1]
        a, b = int(a), int(b); solved.append(a + b if op == "+" else a - b)
    P.v("V1 independent solver reads the printed columns back and equals the key", solved == ans, solved)
    P.v("V7 all numbers 4-digit, answers within 9999", all(1000 <= a <= 9999 for op, a, b in sums for a in (a,)) and all(100 <= x <= 9999 for x in ans))
    P.v("V3e the usual slip (no renaming) gives a decoy letter or no letter", all(wrong_column(*s) not in table or table[wrong_column(*s)] not in word for s in sums if wrong_column(*s) != (s[1] + s[2] if s[0] == '+' else s[1] - s[2])))
    return P

# =============================================================================== P3-07 Mental Pairs (route)
def mexpr(rng, T):
    """a two-digit number plus or minus a two-digit number with value T (both numbers two-digit)"""
    for _ in range(200):
        if rng.random() < 0.5:
            a = rng.randint(max(10, T - 99), min(99, T - 10)) if T - 10 >= 10 else None
            if a is None: continue
            b = T - a
            if 10 <= a <= 99 and 10 <= b <= 99 and a % 10 + b % 10 >= 10: return f"{a} + {b}"
        else:
            b = rng.randint(10, 99 - T) if 99 - T >= 10 else None
            if b is None: continue
            a = T + b
            if 10 <= a <= 99 and a % 10 < b % 10: return f"{a} − {b}"
    return None

def meval(s):
    m = re.fullmatch(r"\s*(\d+)\s*([+−-])\s*(\d+)\s*", s)
    a, op, b = int(m.group(1)), m.group(2), int(m.group(3))
    return a + b if op == "+" else a - b

def page07():
    rng = random.Random(3707)
    n = 4; L = 8
    for _ in range(8000):
        T = rng.randint(41, 78)
        path = random_walk(rng, n, L)
        grid = {}
        for c in path:
            e = mexpr(rng, T)
            if e is None: break
            grid[c] = e
        else:
            dead = 0
            for p in path[:-1]:
                if dead >= 3: break
                opts = [q for q in neighbours(*p, n) if q not in grid]
                if opts and rng.random() < .5:
                    e = mexpr(rng, T)
                    if e: grid[rng.choice(opts)] = e; dead += 1
            decoys = []
            fail = False
            for r in range(n):
                for c in range(n):
                    if (r, c) not in grid:
                        e = None
                        for _k in range(50):
                            wrong = T + rng.choice([-20, -10, -2, -1, 1, 2, 10, 20, 9, -9, 11, -11])
                            if 12 <= wrong <= 98: e = mexpr(rng, wrong)
                            if e: break
                        if not e: fail = True; break
                        grid[(r, c)] = e; decoys.append(meval(e))
                if fail: break
            if fail: continue
            start, finish = path[0], path[-1]
            ok = lambda cell: meval(grid[cell]) == T
            if count_routes(ok, n, start, finish) == 1 and 2 <= dead <= 3 and len(set(grid.values())) == 16 and abs(start[0]-finish[0]) + abs(start[1]-finish[1]) + 1 < L: break
    else: raise RuntimeError("p07")
    texts = [[grid[(r, c)] for c in range(n)] for r in range(n)]
    body = maze_html(n, texts, start, finish)
    P = new_page(7, 3707, "Mental Pairs", 1, "Mental sums: adding and subtracting two 2-digit numbers", STRAND_AS,
        "2.2 (mental calculation: addition and subtraction of two 2-digit numbers)", ["AS2.2"], "Maze / path", "K6 route closes at FINISH",
        ["Start at START. Move up, down, left or right.", f"Step only on boxes with the answer {T}.", "Do not step on a box twice."],
        body, "Route (row, column from top-left): " + " -> ".join(f"({r+1},{c+1}) {grid[(r, c)]}" for r, c in path),
        f"Route reaches FINISH through {L} boxes; every box on it makes {T}.",
        f"A 4 by 4 grid of sixteen mental sums, each the sum or difference of two 2-digit numbers (every sum and every difference needs renaming, so the pupil must think about tens and ones). The boxes off the route make answers near {T} ({', '.join(str(x) for x in sorted(set(decoys)))}); a slip in the tens or the ones sends the pupil there. {dead} extra boxes that do make {T} are dead ends. Counting the boxes shows a line that takes a shortcut.",
        check=f"Does your line reach FINISH? Count its boxes: are there {L}? Does every box make {T}?", mk=("route",),
        mech_plain=f"Route: the line must reach FINISH through the right number of boxes, every box making {T}")
    g2 = {(r, c): texts[r][c] for r in range(n) for c in range(n)}
    ok2 = lambda cell: meval(g2[cell]) == T
    P.v("V1 exactly one route start->finish (exhaustive search, sums evaluated from the printed text)", count_routes(ok2, n, start, finish) == 1)
    P.v("V3 dead-end boxes that also make the target exist", dead >= 2, dead)
    P.v("V3b a shortcut that ignores the rule is shorter than the route", abs(start[0]-finish[0]) + abs(start[1]-finish[1]) + 1 < L)
    P.v("V7 every box is a sum or difference of two 2-digit numbers", all(len(re.findall(r"\d+", t)) == 2 and all(10 <= int(x) <= 99 for x in re.findall(r"\d+", t)) for t in g2.values()))
    P.v("V7b all sixteen boxes are different", len(set(g2.values())) == 16)
    P["cv"] = dict(rate=1.0, single_total=dead, single_detected=dead)
    allcells = [(r, c) for r in range(n) for c in range(n)]
    def legal(rt):
        if len(rt) != L or len(set(rt)) != L or rt[0] != start or rt[-1] != finish: return False
        return all(ok2(c) for c in rt) and all(abs(a[0]-b[0]) + abs(a[1]-b[1]) == 1 for a, b in zip(rt, rt[1:]))
    P["model"] = dict(truth=list(path), domains=[allcells] * L, check=legal, numeric=False)
    P["mini"] = mini_route(n, path)
    P["facts"] = f"{T} " + " ".join(str(x) for x in decoys) + " " + " ".join(re.findall(r"\d+", " ".join(g2.values())))
    return P

# =============================================================================== P3-08 Missing Digits
def page08():
    rng = random.Random(3808)
    while True:
        items = []
        for k in range(6):
            op = "+" if k % 2 == 0 else "-"
            if op == "+":
                a = rng.randint(1200, 6990); b = rng.randint(1100, 9999 - a); r = a + b
            else:
                a = rng.randint(4000, 9990); b = rng.randint(1100, a - 1000); r = a - b
            which = rng.choice([0, 1, 2]); pos = rng.randint(0, 3)
            sa, sb, sr = str(a), str(b), str(r)
            rows = [list(sa), list(sb), list(sr)]
            if pos >= len(rows[which]): continue
            dig = int(rows[which][pos]); rows[which][pos] = "?"
            items.append(dict(op=op, rows=["".join(x) for x in rows], dig=dig, a=a, b=b, r=r))
        if len(items) < 6: continue
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
        res = find_table(8, 6, ans, rng, 0, 9, pool, n_decoy=2, tries=80)
        if res: word, table = res; break
    hs = [vsum4(it["rows"][0], it["rows"][1], "+" if it["op"] == "+" else "−", res=it["rows"][2], width=4) for it in items]
    cards = "".join(f'<div class="vcard"><span class="no">{i+1}</span>{h}</div>' for i, h in enumerate(hs))
    P = code_items_page(8, 3808, "Missing Digits", 2, "Add and subtract in columns: find the missing digit", STRAND_AS,
        "2.1 (addition and subtraction algorithms, up to 4 digits)", ["AS2.1"], "Code-breaker (written methods)",
        ["One digit is missing from each sum.", "Write the missing digit in the box.", INSTR_CODE],
        f'<div class="vcards">{cards}</div>', ans, table, word, 0, 9,
        "; ".join(f"{i+1}) {it['rows'][0].replace('?', str(it['dig']))} {it['op']} {it['rows'][1].replace('?', str(it['dig']))} = {it['rows'][2].replace('?', str(it['dig']))}: digit {it['dig']}" for i, it in enumerate(items)),
        "Six column sums with one digit missing (three additions, three subtractions, the missing digit in the top number, the bottom number or the answer). Each has exactly one digit that makes it true. The pupil writes the missing digit, then looks it up. A digit that is wrong either has a decoy letter or no letter. A box left blank gives no letter and the check cannot see it.")
    solved = []
    for h in hs:
        (t, b, r), op = parse_vsum4(h)
        sols = []
        for d in range(10):
            rr = [x.replace("?", str(d)) for x in (t, b, r)]
            if any(x[0] == "0" for x in rr): continue
            a_, b_, r_ = map(int, rr)
            if (a_ + b_ == r_ if op == "+" else a_ - b_ == r_): sols.append(d)
        solved.append(sols[0] if len(sols) == 1 else sols)
    P.v("V1 independent solver (every digit tried in the printed sum) finds exactly one digit and it equals the key", solved == ans, solved)
    P.v("V7 every number has 4 digits (an answer may have 4)", all(len(it["rows"][0]) == 4 and len(it["rows"][1]) == 4 and len(it["rows"][2]) == 4 for it in items))
    return P

# =============================================================================== P3-09 Tables Maze (route)
def tfact(rng, T):
    """a printed fact from the tables of 6 to 9 (and the tables they link to) whose missing number is T"""
    a = rng.randint(2, 9)
    p = a * T
    form = rng.choice(["x?", "?x", "div", "divq"])
    if form == "x?": return f"{a} × ? = {p}"
    if form == "?x": return f"? × {a} = {p}"
    if form == "div": return f"{p} ÷ {a} = ?"
    return f"{p} ÷ ? = {a}"

def tsolve(s):
    """independent: the missing number of a printed fact"""
    m = re.fullmatch(r"(\d+) × \? = (\d+)", s)
    if m: return int(m.group(2)) // int(m.group(1))
    m = re.fullmatch(r"\? × (\d+) = (\d+)", s)
    if m: return int(m.group(2)) // int(m.group(1))
    m = re.fullmatch(r"(\d+) ÷ (\d+) = \?", s)
    if m: return int(m.group(1)) // int(m.group(2))
    m = re.fullmatch(r"(\d+) ÷ \? = (\d+)", s)
    if m: return int(m.group(1)) // int(m.group(2))
    raise ValueError(s)

def page09():
    rng = random.Random(3909)
    n = 4; L = 8
    T = rng.choice([6, 7, 8, 9])
    for _ in range(40000):
        path = random_walk(rng, n, L, min_dist=3)
        if abs(path[0][0] - path[-1][0]) + abs(path[0][1] - path[-1][1]) + 1 >= L: continue
        grid = {}
        for c in path: grid[c] = tfact(rng, T)
        dead = 0
        for p in path[:-1]:
            if dead >= 2: break
            opts = [q for q in neighbours(*p, n) if q not in grid]
            if opts and rng.random() < .6: grid[rng.choice(opts)] = tfact(rng, T); dead += 1
        for r in range(n):
            for c in range(n):
                if (r, c) not in grid:
                    w = rng.choice([x for x in range(4, 11) if x != T and abs(x - T) <= 3])
                    grid[(r, c)] = tfact(rng, w)
        start, finish = path[0], path[-1]
        ok = lambda cell: tsolve(grid[cell]) == T
        if count_routes(ok, n, start, finish) == 1 and dead == 2 and len(set(grid.values())) == 16 and all(tsolve(v) <= 10 for v in grid.values()) and len({tsolve(v) for v in grid.values()}) >= 4: break
    else: raise RuntimeError("p09")
    texts = [[grid[(r, c)] for c in range(n)] for r in range(n)]
    body = maze_html(n, texts, start, finish)
    P = new_page(9, 3909, "Tables Maze", 1, "Multiplication and division facts: tables of 6, 7, 8 and 9", STRAND_MD,
        "3.1, 3.2 (tables of 6, 7, 8 and 9; multiplying and dividing within the tables)", ["MD3.1", "MD3.2", "MD3.5"], "Maze / path", "K6 route closes at FINISH",
        ["Start at START. Move up, down, left or right.", f"Step only on boxes where the missing number is {T}.", "Do not step on a box twice."],
        body, "Route (row, column from top-left): " + " -> ".join(f"({r+1},{c+1}) {grid[(r, c)]}" for r, c in path),
        f"Route reaches FINISH through {L} boxes; the missing number in every box on it is {T}.",
        f"A 4 by 4 grid of sixteen multiplication and division facts with one missing number, from the tables of 6 to 9 and the tables they link to (2 to 5). The route follows the boxes whose missing number is {T}. The other boxes have missing numbers near {T}. {dead} extra boxes that do make {T} are dead ends. Counting the boxes shows a line that takes a shortcut.",
        check=f"Does your line reach FINISH? Count its boxes: are there {L}? Is every missing number {T}?", mk=("route",),
        mech_plain=f"Route: the line must reach FINISH through the right number of boxes, every missing number being {T}")
    g2 = {(r, c): texts[r][c] for r in range(n) for c in range(n)}
    ok2 = lambda cell: tsolve(g2[cell]) == T
    P.v("V1 exactly one route start->finish (exhaustive search, missing numbers found from the printed facts)", count_routes(ok2, n, start, finish) == 1)
    P.v("V3 dead-end boxes that also have the target exist", dead >= 2, dead)
    P.v("V3b a shortcut that ignores the rule is shorter than the route", abs(start[0]-finish[0]) + abs(start[1]-finish[1]) + 1 < L)
    P.v("V7 every missing number is 10 or less; every number printed is within 90", all(tsolve(t) <= 10 for t in g2.values()) and all(int(x) <= 90 for t in g2.values() for x in re.findall(r"\d+", t)))
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

PAGES = [page06, page07, page08, page09]
