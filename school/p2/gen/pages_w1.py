"""Wave 1: P2-01 Hundreds, Tens, Ones; P2-02 Column Sums; P2-03 Mental Jumps; P2-04 Equal Groups; P2-05 Share It Out;
P2-06 Dollars and Cents; P2-07 Time to the Minute; P2-08 Metres."""
import random, re, math, itertools
from .common import *
from .kit import *
from . import art2 as A
from .art import osz, opitch, COUNT_KINDS, NAMES as OBJN, count_objs
from .common import obj_g, svg

PEOPLE = ["Ali", "Mei", "Siti", "Ben", "Kumar", "Aisha", "Wei", "Ravi", "Jenny", "Lily", "Hana", "Tom"]
STRAND_WN = "Number and Algebra - Whole Numbers"
STRAND_AS = "Number and Algebra - Addition and Subtraction"
STRAND_MD = "Number and Algebra - Multiplication and Division"
STRAND_MO = "Number and Algebra - Money"
STRAND_ME = "Measurement and Geometry - Measurement"
INSTR_CODE = "Use the code table."

def code_items_page(no, seed, title, tier, topic, strand, syll, oc, ptype, instr, items_html, answers, table, word, lo, hi, key_answers, note,
                    domain=None, fmt=str, ps=False, pre_body="", mech=None, plain=None):
    body = pre_body + items_html + table_block(table, fmt)
    P = new_page(no, seed, title, tier, topic, strand, syll, oc, ptype, mech or f"K1 code word ({len(word)} letters)", instr, body, key_answers,
                 f"Code word: {word}", note, check_boxes=len(word), ps=ps)
    finish_code(P, answers, table, word, lo, hi, domain, plain)
    P["facts"] = " ".join(str(v) for v in table)
    return P

def distinct(xs): return len(set(xs)) == len(xs)

# =============================================================================== P2-01 Hundreds, Tens, Ones
def page01():
    rng = random.Random(5101)
    for _ in range(3000):
        items = []
        for _k in range(3):
            items.append(dict(k="chart", h=rng.randint(1, 8), t=rng.randint(0, 8), o=rng.randint(0, 8)))
        n = rng.choice([x for x in range(120, 990) if len(set(str(x))) == 3 and "0" not in str(x)])
        d = rng.choice(str(n))
        items.append(dict(k="digit", n=n, d=int(d)))
        items.append(dict(k="regroup", h=rng.randint(2, 6), t=rng.randint(11, 15), o=rng.randint(1, 8)))
        items.append(dict(k="zero", h=rng.randint(2, 9), o=rng.randint(1, 9)))
        ans = []
        for it in items:
            ans.append({"chart": lambda i: i["h"] * 100 + i["t"] * 10 + i["o"], "digit": lambda i: i["d"] * 10 ** (2 - str(i["n"]).index(str(i["d"]))),
                        "regroup": lambda i: i["h"] * 100 + i["t"] * 10 + i["o"], "zero": lambda i: i["h"] * 100 + i["o"]}[it["k"]](it))
        if not distinct(ans) or max(ans) > 999: continue
        if any(it["k"] == "chart" and it["h"] * 100 + it["t"] * 10 + it["o"] < 100 for it in items): continue
        pool = set()
        for it, a in zip(items, ans):
            s = str(a).zfill(3)
            for p in itertools.permutations(s): pool.add(int("".join(p)))
            if it["k"] == "digit": pool |= {it["d"], it["d"] * 100, it["d"] * 10, it["n"]}
            if it["k"] == "zero": pool |= {it["h"] * 10 + it["o"], int(f"{it['h']}{it['o']}0")}
            if it["k"] == "regroup": pool |= {it["h"] * 100 + it["t"] + it["o"], int(f"{it['h']}{it['t']}{it['o']}") % 1000}
        pool = sorted(p for p in pool if p not in ans and 0 <= p <= 999)
        res = code_table_any(1, 6, ans, rng, 0, 999, n_decoy=3, tries=60, pool=pool)
        if res: word, table = res; break
    cards = []; texts = []
    for i, it in enumerate(items):
        if it["k"] == "chart":
            cards.append(qcard(i + 1, A.pv_chart(it["h"], it["t"], it["o"], per_row=4), '<span class="ab w3"></span>', cls="inl"))
        else:
            if it["k"] == "digit": t = f"In {it['n']}, what is the value of the digit {it['d']}?"
            elif it["k"] == "regroup": t = f"{it['h']} hundreds, {it['t']} tens and {it['o']} ones make which number?"
            else: t = f"{it['h']} hundreds, 0 tens and {it['o']} ones make which number?"
            texts.append(t); cards.append(qcard(i + 1, f"<p>{t}</p>", '<span class="ab w3"></span>'))
    body = '<div class="qg c1">' + "".join(cards[:3]) + '</div><div class="qg c3">' + "".join(cards[3:]) + "</div>"
    P = code_items_page(1, 5101, "Hundreds, Tens, Ones", 1, "Place value: hundreds, tens and ones", STRAND_WN,
        "1.2 (number notation, representations and place values: hundreds, tens, ones)", ["WN1.2"], "Code-breaker (place value)",
        ["Look at each item.", "Write the number in the box.", INSTR_CODE],
        body, ans, table, word, 0, 999,
        "; ".join(f"{i+1}) {a}" for i, a in enumerate(ans)),
        "Three place-value charts (discs marked 100, 10 and 1), then the value of a digit, a regrouped number (more than 10 tens) and a number with a zero tens place. The wrong numbers a pupil gets by writing the digits in a different order, or by giving the digit instead of its value, have decoy letters in the table or no letter. A box left blank gives no letter and the check cannot see it.")
    # independent solver: read the discs and the printed words back
    solved = []
    ci = 0
    for it in items:
        if it["k"] == "chart":
            h, t, o = A.read_pv_chart(cards[ci]); solved.append(100 * h + 10 * t + o)
        elif it["k"] == "digit":
            tx = texts[[x for x in texts if x.startswith("In ")].index(f"In {it['n']}, what is the value of the digit {it['d']}?")]
            nn, dd = re.match(r"In (\d+), what is the value of the digit (\d)\?", tx).groups()
            solved.append(int(dd) * 10 ** (len(nn) - 1 - nn.index(dd)))
        else:
            tx = [x for x in texts if x.startswith(f"{it['h']} hundreds")][0]
            a_, b_, c_ = map(int, re.findall(r"\d+", tx)); solved.append(100 * a_ + 10 * b_ + c_)
        ci += 1
    P.v("V1 independent solver (discs counted in the drawing, words read back) equals the key", solved == ans, solved)
    P.v("V7 every chart, regrouped and zero-place answer is 3-digit and below 1000", all(100 <= a <= 999 for a, it in zip(ans, items) if it["k"] != "digit") and all(a <= 999 for a in ans))
    P.v("V1b the digit asked about appears once in its number", all(str(it["n"]).count(str(it["d"])) == 1 for it in items if it["k"] == "digit"))
    P.v("V1c at most 8 discs in a chart column", all(max(it["h"], it["t"], it["o"]) <= 8 for it in items if it["k"] == "chart"))
    P["key"]["answers"] = "; ".join(
        (f"{i+1}) {it['h']} hundreds {it['t']} tens {it['o']} ones = {a}" if it["k"] == "chart" else f"{i+1}) {a}") for i, (it, a) in enumerate(zip(items, ans)))
    return P

# =============================================================================== P2-02 Column Sums
def column_pairs(rng):
    """6 vertical sums: add without renaming, add with ones renamed, add with tens renamed, subtract without, subtract with tens borrowed, subtract with hundreds borrowed"""
    out = []
    def rd(): return rng.randint(1, 9)
    a = rng.randint(1, 4) * 100 + rng.randint(1, 4) * 10 + rd(); b = rng.randint(1, 4) * 100 + rng.randint(1, 4) * 10 + rng.randint(1, 9 - a % 10) if a % 10 < 9 else 0
    out.append(("+", a, b))                                                                       # no renaming
    while True:
        a = rng.randint(100, 600); b = rng.randint(100, 300)
        if a % 10 + b % 10 >= 10 and (a // 10 % 10 + b // 10 % 10) < 9: break
    out.append(("+", a, b))                                                                       # ones renamed
    while True:
        a = rng.randint(100, 500); b = rng.randint(100, 400)
        if a % 10 + b % 10 < 10 and (a // 10) % 10 + (b // 10) % 10 >= 10 and a + b < 1000: break
    out.append(("+", a, b))                                                                       # tens renamed
    while True:
        a = rng.randint(300, 900); b = rng.randint(100, a - 100)
        if all(int(x) <= int(y) for x, y in zip(str(b), str(a))): break
    out.append(("-", a, b))                                                                       # no renaming
    while True:
        a = rng.randint(300, 900); b = rng.randint(100, a - 100)
        if a % 10 < b % 10 and (a // 10) % 10 >= (b // 10) % 10: break
    out.append(("-", a, b))                                                                       # ones renamed
    while True:
        a = rng.randint(300, 900); b = rng.randint(100, a - 100)
        if a % 10 >= b % 10 and (a // 10) % 10 < (b // 10) % 10: break
    out.append(("-", a, b))                                                                       # tens renamed
    return out

def wrong_column(op, a, b):
    """what a pupil gets by not renaming: digit by digit without carrying or borrowing"""
    sa, sb = str(a).zfill(3), str(b).zfill(3)
    if op == "+": return int("".join(str((int(x) + int(y)) % 10) for x, y in zip(sa, sb)))
    return int("".join(str(abs(int(x) - int(y))) for x, y in zip(sa, sb)))

def page02():
    rng = random.Random(5202)
    while True:
        sums = column_pairs(rng); rng.shuffle(sums)
        ans = [a + b if op == "+" else a - b for op, a, b in sums]
        if not distinct(ans) or max(ans) > 999: continue
        pool = sorted({wrong_column(*s) for s in sums} | {a + 10 for a in ans} | {a - 100 for a in ans if a > 100} | {a + 100 for a in ans if a < 900})
        pool = [p for p in pool if p not in ans and p > 0]
        res = code_table_any(2, 6, ans, rng, 0, 999, n_decoy=3, tries=60, pool=pool)
        if res: word, table = res; break
    hs = [vsum_html(a, b, "+" if op == "+" else "−") for op, a, b in sums]
    cards = "".join(f'<div class="vcard"><span class="no">{i+1}</span>{h}</div>' for i, h in enumerate(hs))
    P = code_items_page(2, 5202, "Column Sums", 1, "Add and subtract in columns, 3-digit numbers", STRAND_AS,
        "2.1 (addition and subtraction algorithms, up to 3 digits)", ["AS2.1"], "Code-breaker (written methods)",
        ["Work out each sum in columns.", "Write the answer in the box.", INSTR_CODE],
        f'<div class="vcards">{cards}</div>', ans, table, word, 0, 999,
        "; ".join(f"{i+1}) {a} {op} {b} = {x}" for i, ((op, a, b), x) in enumerate(zip(sums, ans))),
        "Six vertical sums within 1000: three additions (no renaming, ones renamed, tens renamed) and three subtractions (no renaming, ones renamed, tens renamed). The decoy letters stand for the answers a pupil gets by not renaming (adding or subtracting digit by digit). A box left blank gives no letter and the check cannot see it.")
    solved = []
    for h in hs:
        a, b, op = parse_vsum(h); solved.append(a + b if op == "+" else a - b)
    P.v("V1 independent solver reads the printed columns back and equals the key", solved == ans, solved)
    P.v("V7 all numbers 3-digit, answers within 999", all(100 <= x <= 999 for x in ans))
    P.v("V3e answers without renaming (the usual slip) are decoy letters or have no letter", all(wrong_column(*s) not in table or table[wrong_column(*s)] not in word for s in sums if wrong_column(*s) != (s[1] + s[2] if s[0] == '+' else s[1] - s[2])))
    return P

# =============================================================================== P2-03 Mental Jumps
def jump_expr(rng, T, kind):
    """an expression a +/- b with value T where b is ones, tens or hundreds"""
    if kind == "ones": b = rng.randint(1, 9)
    elif kind == "tens": b = rng.randint(1, 9) * 10
    else: b = rng.randint(1, 4) * 100
    if rng.random() < 0.5 and T - b >= 100: return f"{T-b} + {b}"
    if T + b <= 999: return f"{T+b} − {b}"
    return f"{T-b} + {b}"

def eval_expr(s):
    m = re.fullmatch(r"\s*(\d+)\s*([+−-])\s*(\d+)\s*", s)
    a, op, b = int(m.group(1)), m.group(2), int(m.group(3))
    return a + b if op == "+" else a - b

def page03():
    rng = random.Random(5303)
    n = 4; LEN = 8
    for _ in range(6000):
        T = rng.randint(30, 85) * 10 + rng.choice([0, 5])
        path = random_walk(rng, n, LEN)
        grid = [[None] * n for _ in range(n)]
        kinds = ["ones", "tens", "hundreds"] * 4
        rng.shuffle(kinds)
        for i, p in enumerate(path): grid[p[0]][p[1]] = jump_expr(rng, T, kinds[i])
        dead = 0
        for p in path[:-1]:
            if dead >= 3: break
            opts = [q for q in neighbours(*p, n) if grid[q[0]][q[1]] is None]
            if opts and rng.random() < .5:
                q = rng.choice(opts); grid[q[0]][q[1]] = jump_expr(rng, T, rng.choice(["ones", "tens", "hundreds"])); dead += 1
        decoys = []
        for r in range(n):
            for c in range(n):
                if grid[r][c] is None:
                    wrong = T + rng.choice([-100, -10, 10, 100, -1, 1, -5, 5, -20, 20])
                    kind = rng.choice(["ones", "tens", "hundreds"]); e = jump_expr(rng, wrong, kind)
                    grid[r][c] = e; decoys.append(eval_expr(e))
        start, finish = path[0], path[-1]
        ok = lambda cell: eval_expr(grid[cell[0]][cell[1]]) == T
        if count_routes(ok, n, start, finish) == 1 and 2 <= dead <= 3 and len(set(grid[r][c] for r in range(n) for c in range(n))) == 16: break
    else: raise RuntimeError("p03")
    texts = [[grid[r][c] for c in range(n)] for r in range(n)]
    body = maze_html(n, texts, start, finish)
    P = new_page(3, 5303, "Mental Jumps", 1, "Mental sums: 3-digit numbers with ones, tens and hundreds", STRAND_AS,
        "2.2 (mental calculation: a 3-digit number with ones, tens or hundreds)", ["AS2.2"], "Maze / path", "K6 route closes at FINISH",
        ["Start at START. Move up, down, left or right.", f"Step only on boxes with the answer {T}.", "Do not step on a box twice."],
        body, "Route (row, column from top-left): " + " -> ".join(f"({r+1},{c+1}) {grid[r][c]}" for r, c in path),
        f"Route reaches FINISH through {len(path)} boxes; every box on it makes {T}.",
        f"A 4 by 4 grid of sixteen mental sums with a 3-digit number and ones, tens or hundreds. The boxes off the route make answers near {T} ({', '.join(str(x) for x in sorted(set(decoys)))}); a slip in adding or taking away sends the pupil there. {dead} extra boxes that do make {T} are dead ends. Counting the boxes shows a line that takes a shortcut.",
        check=f"Does your line reach FINISH? Count its boxes: are there {len(path)}? Does every box make {T}?", mk=("route",),
        mech_plain="Route: the line must reach FINISH through the right number of boxes, every box making the target")
    P["instr"] = ["Start at START. Move up, down, left or right.", f"Step only on boxes with the answer {T}.", "Do not step on a box twice."]
    P.v("V1 exactly one route start->finish (exhaustive search, answers evaluated from the printed sums)", count_routes(ok, n, start, finish) == 1)
    P.v("V3 dead-end boxes that also make the target exist", dead >= 2, dead)
    P.v("V3b a shortcut that ignores the rule is shorter than the route, so the box count rejects it", abs(start[0]-finish[0]) + abs(start[1]-finish[1]) + 1 < len(path))
    P.v("V7 every sum uses a 3-digit number with ones, tens or hundreds", all(100 <= max(map(int, re.findall(r"\d+", grid[r][c]))) <= 999 for r in range(n) for c in range(n)))
    P.v("V7b all sixteen boxes are different", len({grid[r][c] for r in range(n) for c in range(n)}) == 16)
    P["cv"] = dict(rate=1.0, single_total=dead, single_detected=dead)
    P["facts"] = f"{T} " + " ".join(str(x) for x in decoys)
    cells = [(r, c) for r in range(n) for c in range(n)]
    def legal(rt):
        if len(rt) != len(path) or len(set(rt)) != len(rt) or rt[0] != start or rt[-1] != finish: return False
        return all(eval_expr(grid[r][c]) == T for r, c in rt) and all(abs(a[0]-b[0]) + abs(a[1]-b[1]) == 1 for a, b in zip(rt, rt[1:]))
    P["model"] = dict(truth=list(path), domains=[cells] * len(path), check=legal, numeric=False)
    P["mini"] = mini_route(n, path)
    return P

# =============================================================================== P2-04 Equal Groups
def page04():
    rng = random.Random(5404)
    kinds = rng.sample(COUNT_KINDS, 2)
    while True:
        items = []
        f1 = rng.choice([2, 3, 4, 5]); f2 = rng.choice([2, 3, 4, 5]); items.append(dict(k="array", kind=kinds[0], r=f1, c=f2))
        f1 = rng.choice([2, 3, 4, 5]); f2 = rng.choice([3, 4, 5]); items.append(dict(k="array", kind=kinds[1], r=f1, c=f2))
        a, b = rng.choice([2, 3, 4, 5, 10]), rng.choice([2, 3, 4, 5, 6, 7, 8, 9]); items.append(dict(k="times", a=a, b=b))
        g, m = rng.choice([2, 3, 4, 5, 10]), rng.choice([4, 5, 6, 7, 8, 9]); items.append(dict(k="groups", g=g, m=m, N=rng.choice(PEOPLE), thing=rng.choice(["pencils", "stickers", "sweets", "marbles"])))
        t = rng.choice([2, 3, 4, 5, 10]); q = rng.choice([3, 4, 6, 7, 8, 9]); items.append(dict(k="missing", t=t, q=q))
        t = rng.choice([4, 5, 10, 3]); u = rng.choice([4, 5, 6, 7, 8, 9]); items.append(dict(k="story", t=t, u=u))
        ans = [it["r"] * it["c"] if it["k"] == "array" else it["a"] * it["b"] if it["k"] == "times" else it["g"] * it["m"] if it["k"] == "groups" else it["q"] if it["k"] == "missing" else it["t"] * it["u"] for it in items]
        if not distinct(ans) or max(ans) > 50 or min(ans) < 4: continue
        rng.shuffle(items); ans = [it["r"] * it["c"] if it["k"] == "array" else it["a"] * it["b"] if it["k"] == "times" else it["g"] * it["m"] if it["k"] == "groups" else it["q"] if it["k"] == "missing" else it["t"] * it["u"] for it in items]
        pool = set()
        for it in items:
            if it["k"] == "array": pool |= {it["r"] + it["c"]}
            if it["k"] == "times": pool |= {it["a"] + it["b"]}
            if it["k"] == "groups": pool |= {it["g"] + it["m"]}
            if it["k"] == "missing": pool |= {it["t"] * it["q"], it["t"] + it["q"], it["t"] * it["q"] // it["t"] + 1}
            if it["k"] == "story": pool |= {it["t"] + it["u"]}
        pool |= {a + 1 for a in ans} | {a - 1 for a in ans} | {a + 2 for a in ans}
        pool = sorted(p for p in pool if p not in ans and 1 <= p <= 50)
        res = code_table_any(4, 6, ans, rng, 1, 50, n_decoy=3, tries=60, pool=pool)
        if res: word, table = res; break
    cards = []; texts = []; svgs = []
    for i, it in enumerate(items):
        if it["k"] == "array":
            s = A.array_svg(it["kind"], it["r"], it["c"]); svgs.append(s)
            cards.append(qcard(i + 1, f'<p>How many {OBJN[it["kind"]][1]} in all?</p>' + s, '<span class="ab w3"></span>'))
            texts.append(None)
        else:
            if it["k"] == "times": t = f"{it['a']} \u00d7 {it['b']} = ?"
            elif it["k"] == "groups": t = f"{it['N']} has {it['g']} groups of {it['m']} {it['thing']}. How many {it['thing']} in all?"
            elif it["k"] == "missing": t = f"{it['t']} \u00d7 ? = {it['t'] * it['q']}"
            else: t = f"There are {it['t']} tables. {it['u']} children sit at each table. How many children?"
            texts.append(t); svgs.append(None); cards.append(qcard(i + 1, f"<p>{t}</p>", '<span class="ab w3"></span>'))
    P = code_items_page(4, 5404, "Equal Groups", 1, "Multiplication: tables of 2, 3, 4, 5 and 10", STRAND_MD,
        "3.1, 3.4 (multiplication tables of 2, 3, 4, 5 and 10; multiplying within the tables)", ["MD3.1", "MD3.4"], "Code-breaker (equal groups)",
        ["Find how many in all.", "Write the answer in the box.", INSTR_CODE],
        qgrid(cards, 2), ans, table, word, 1, 50,
        "; ".join(f"{i+1}) {x}" for i, x in enumerate(ans)),
        "Two arrays of objects (count rows and columns or count all), a bare multiplication, a groups-of story, a missing factor and a table-top story. Every product uses a table of 2, 3, 4, 5 or 10 and stays within 50. The decoy letters stand for adding the two numbers instead of multiplying. A box left blank gives no letter and the check cannot see it.")
    def solve(i, it):
        if it["k"] == "array":
            return sum(count_objs(svgs[i]).values())
        t = texts[i]
        nums = list(map(int, re.findall(r"\d+", t)))
        if "\u00d7 ?" in t: return nums[1] // nums[0]
        return nums[0] * nums[1]
    solved = [solve(i, it) for i, it in enumerate(items)]
    P.v("V1 independent solver (objects counted in the drawing, printed text read back) equals the key", solved == ans, solved)
    P.v("V7 every product within 50, each from a table of 2, 3, 4, 5 or 10", max(ans) <= 50 and all(bool({it["r"], it["c"]} & {2, 3, 4, 5, 10}) for it in items if it["k"] == "array"))
    P.v("V8 objects are at least 8 mm across", all(osz(it["kind"]) >= 9.0 for it in items if it["k"] == "array"))
    return P

# =============================================================================== P2-05 Share It Out
def page05():
    rng = random.Random(5505)
    while True:
        items = []
        for _k in range(2):
            d = rng.choice([2, 3, 4, 5, 10]); qq = rng.randint(3, 9); items.append(dict(k="bare", n=d * qq, d=d))
        d = rng.choice([2, 3, 4, 5]); qq = rng.randint(3, 9); items.append(dict(k="share", n=d * qq, d=d, thing=rng.choice(["stickers", "marbles", "sweets", "cards"])))
        d = rng.choice([2, 3, 4, 5, 10]); qq = rng.randint(3, 9); items.append(dict(k="boxes", n=d * qq, d=d, thing=rng.choice(["pencils", "eggs", "buns", "balloons"])))
        fr = rng.choice([2, 3, 4]); qq = rng.randint(2, 9); items.append(dict(k="friends", N=rng.choice(PEOPLE), fr=fr, d=fr + 1, n=(fr + 1) * qq, thing=rng.choice(["sweets", "grapes", "stickers"])))
        d = rng.choice([2, 3, 4, 5]); qq = rng.randint(3, 9); items.append(dict(k="how", n=d * qq, d=d))
        rng.shuffle(items)
        ans = [it["n"] // it["d"] for it in items]
        if not distinct(ans) or max(ans) > 10 or min(ans) < 2: continue
        pool = set()
        for it in items:
            pool |= {it["n"] - it["d"], it["n"] // it["d"] + 1}
            if it["k"] == "friends": pool |= {it["n"] // it["fr"]}
        pool |= {a + 1 for a in ans} | {a - 1 for a in ans if a > 2}
        pool = sorted(p for p in pool if p not in ans and 1 <= p <= 50)
        res = code_table_any(5, 6, ans, rng, 1, 50, n_decoy=4, tries=60, pool=pool)
        if res: word, table = res; break
    texts = []; cards = []
    for i, it in enumerate(items):
        k = it["k"]
        if k == "bare": t = f"{it['n']} \u00f7 {it['d']} = ?"
        elif k == "share": t = f"{it['n']} {it['thing']} are shared equally among {it['d']} children. How many does each child get?"
        elif k == "boxes": t = f"{it['n']} {it['thing']} are put in boxes of {it['d']}. How many boxes are needed?"
        elif k == "friends": t = f"{it['N']} shares {it['n']} {it['thing']} equally with {it['fr']} friends. How many does each person get?"
        else: t = f"How many {it['d']}s are in {it['n']}?"
        texts.append(t); cards.append(qcard(i + 1, f"<p>{t}</p>", '<span class="ab w3"></span>'))
    P = code_items_page(5, 5505, "Share It Out", 1, "Division: sharing and grouping, the sign ÷", STRAND_MD,
        "3.2, 3.4 (use of ÷; dividing within the multiplication tables)", ["MD3.2", "MD3.4"], "Code-breaker (division)",
        ["Share or group. Find each answer.", "Write the answer in the box.", INSTR_CODE],
        qgrid(cards, 2), ans, table, word, 1, 50,
        "; ".join(f"{i+1}) {it['n']} ÷ {it.get('d', it.get('fr', 0) + 1)} = {x}" for i, (it, x) in enumerate(zip(items, ans))),
        "Division by 2, 3, 4, 5 and 10 within the tables: two bare sums with the sign ÷, equal sharing, grouping into boxes, a 'how many 3s in 12' item and one story where the sharer also gets a share ('shares with 3 friends' means 4 people). The decoy letters stand for subtracting or for using the number of friends instead of the number of people. A box left blank gives no letter and the check cannot see it.")
    def solve(t):
        nums = list(map(int, re.findall(r"\d+", t)))
        if "÷" in t: return nums[0] // nums[1]
        if "shares" in t and "friends" in t: return nums[0] // (nums[1] + 1)
        if "boxes of" in t or "shared equally among" in t: return nums[0] // nums[1]
        if t.startswith("How many") and "s are in" in t: return nums[1] // nums[0]
        raise ValueError(t)
    solved = [solve(t) for t in texts]
    P.v("V1 independent solver reads the printed text back and equals the key", solved == ans, solved)
    P.v("V7 divisors are 2, 3, 4, 5 or 10 (people count 3, 4 or 5 in the friends item) and every division is exact", all(it["n"] % it["d"] == 0 for it in items))
    return P

# =============================================================================== P2-06 Dollars and Cents
def page06():
    rng = random.Random(5606)
    COINS = [5, 10, 20, 50, 100]
    while True:
        purses = []
        for i in range(6):
            n_notes = rng.choice([0, 0, 1, 1, 2]); n_coins = rng.randint(3, 5)
            notes = [("n", rng.choice([2, 5, 10])) for _ in range(n_notes)]
            coins = [("c", rng.choice(COINS)) for _ in range(n_coins)]
            items = sorted(notes, key=lambda x: -x[1]) + sorted(coins, key=lambda x: -x[1])
            purses.append(items)
        tot = [sum(100 * v if t == "n" else v for t, v in p) for p in purses]
        if all(A.money_width(p) <= 104 for p in purses) and distinct(tot) and 150 <= min(tot) and max(tot) <= 2500 and all(len({v for t, v in p if t == "c"}) >= 2 for p in purses):
            pool = set()
            for p, t in zip(purses, tot):
                pool |= {t + 5, t - 5, t + 10, t - 10, t + 50, t - 50, t + 100, t - 100}
            pool = sorted(x for x in pool if x not in tot and 5 <= x <= 2500 and x % 5 == 0)
            domain = list(range(5, 2501, 5))
            res = code_table_any(6, 6, tot, rng, 5, 2500, n_decoy=4, tries=80, pool=pool, domain=domain)
            if res: word, table = res; break
    svgs = [A.money_svg(p) for p in purses]
    cards = [qcard(i + 1, s, '<span class="dl">$</span><span class="ab w4"></span>', cls="inl") for i, s in enumerate(svgs)]
    P = code_items_page(6, 5606, "Dollars and Cents", 1, "Money: counting coins and notes, decimal notation", STRAND_MO,
        "1.1, 1.2 (counting money in dollars and cents; reading and writing money in decimal notation)", ["MO1.1", "MO1.2"], "Code-breaker (money)",
        ["Count the money in each purse.", "Write the total, like $3.45.", INSTR_CODE],
        qgrid(cards, 1), tot, table, word, 5, 2500,
        "; ".join(f"{i+1}) {A.dollars(t)}" for i, t in enumerate(tot)),
        "Coins (5¢, 10¢, 20¢, 50¢, $1) and notes ($2, $5, $10) are original line drawings, inspired by Singapore money but not copies of any coin or note, drawn larger than real and in black and white. Each coin shows its value and the word cents; each note shows its value twice. Totals are written in dollars and cents ($3.45). The decoy letters stand for a coin missed or counted twice. A box left blank gives no letter and the check cannot see it.",
        domain=domain, fmt=lambda c: A.dollars(c))
    solved = [A.read_money(s) for s in svgs]
    P.v("V1 independent solver adds the values printed on the drawn coins and notes and equals the key", solved == tot, solved)
    P.v("V7 totals between $1.50 and $25.00, whole multiples of 5 cents", all(150 <= t <= 2500 and t % 5 == 0 for t in tot))
    P["facts"] = " ".join(A.dollars(t) for t in tot) + " " + " ".join(A.dollars(t) for t in table)
    return P

# =============================================================================== P2-07 Time to the Minute
def page07():
    rng = random.Random(5707)
    while True:
        times = []
        while len(times) < 6:
            h = rng.randint(1, 12); m = rng.randint(6, 54)
            if A.hands_apart(h, m) < 45: continue
            if m % 5 == 0 and len(times) < 4: continue          # most clocks are not on a five-minute mark
            if (h, m) in times: continue
            times.append((h, m))
        if len({h for h, m in times}) < 5: continue
        pool = set()
        for h, m in times:
            pool |= {(h, (m + 1) % 60), (h, (m - 1) % 60), ((h % 12) + 1, m), (((h - 2) % 12) + 1, m), (m // 5 or 12, (h % 12) * 5), (h, (m + 5) % 60), (h, (m - 5) % 60)}
        pool = sorted(x for x in pool if x not in times)
        domain = [(h, m) for h in range(1, 13) for m in range(60)]
        res = code_table_any(7, 6, times, rng, 0, 0, n_decoy=4, tries=80, pool=pool, domain=domain)
        if res: word, table = res; break
    svgs = [A.clock_svg(h, m) for h, m in times]
    cards = [qcard(i + 1, '<div class="clk">' + s + '</div>', '<span class="ab w3"></span>', cls="pos") for i, s in enumerate(svgs)]
    P = code_items_page(7, 5707, "Time to the Minute", 1, "Time: telling time to the minute", "Measurement and Geometry - Measurement",
        "2.1 (telling time to the minute)", ["TI2.1"], "Code-breaker (clocks)",
        ["Read each clock.", "Write the time, like 3:47.", INSTR_CODE],
        qgrid(cards, 3, "clocks"), times, table, word, 0, 0,
        "; ".join(f"{i+1}) {A.tstr(h, m)}" for i, (h, m) in enumerate(times)),
        "Clock faces with a mark for every minute; the numerals sit outside the ring so the hands never cross them. Most times are not on a five-minute mark. The decoy letters stand for the usual misreadings: one minute out, the hour hand read as the next or the earlier hour, the hands swapped. A box left blank gives no letter and the check cannot see it.",
        domain=domain, fmt=lambda t: A.tstr(*t))
    solved = [A.read_clock(s) for s in svgs]
    P.v("V1 independent solver reads the hand end points of each drawn clock and equals the key", solved == times, solved)
    P.v("V7 the two hands are at least 45 degrees apart on every clock", all(A.hands_apart(h, m) >= 45 for h, m in times))
    P.v("V7b no clock is within 5 minutes of the hour (the hour hand is then easy to misread)", all(6 <= m <= 54 for h, m in times))
    return P

# =============================================================================== P2-08 Metres
def tape_row(label, start, end, scale_max=12, w=104.0):
    """one row: a word label, a bar from start to end (metres) drawn above a tape of 0..scale_max m"""
    u = w / scale_max; x0 = 3.0; H = 17.0
    p = [f'<rect class="bar" x="{x0+start*u:.2f}" y="1.2" width="{(end-start)*u:.2f}" height="4.6" fill="#fff" stroke="#000" stroke-width="0.7"/>']
    if start > 0:
        p.append(f'<polygon class="st" points="{x0+start*u-2.2:.2f},0.2 {x0+start*u+2.2:.2f},0.2 {x0+start*u:.2f},2.6" fill="#000"/>')
    p.append(f'<rect x="{x0:.2f}" y="7.2" width="{scale_max*u:.2f}" height="7.2" fill="#fff" stroke="#000" stroke-width="0.5"/>')
    for k in range(scale_max + 1):
        p.append(f'<line class="tk" x1="{x0+k*u:.2f}" y1="7.2" x2="{x0+k*u:.2f}" y2="{10.4:.2f}" stroke="#000" stroke-width="0.5"/>'
                 f'<text x="{x0+k*u:.2f}" y="12.6" text-anchor="middle" dominant-baseline="central" font-family="Nunito Sans" font-weight="800" font-size="3.8" fill="#000">{k}</text>')
    return svg(round(x0 * 2 + scale_max * u, 1), H, "".join(p))

def read_tape(s):
    ticks = sorted(float(x) for x in re.findall(r'class="tk" x1="([\d.]+)"', s))
    u = ticks[1] - ticks[0]; x0 = ticks[0]
    m = re.search(r'class="bar" x="([\d.]+)" y="[\d.]+" width="([\d.]+)"', s)
    st = (float(m.group(1)) - x0) / u; ln = float(m.group(2)) / u
    return round(st), round(ln)

def page08():
    rng = random.Random(5808)
    things = ["rope", "ribbon", "path", "fence", "hedge", "slide", "ladder", "bench", "snake", "bridge", "net", "wall"]
    while True:
        rows = []; used = []
        for i in range(5):
            st = rng.choice([0, 0, 0, 1, 2, 3]) if i >= 2 else 0
            ln = rng.randint(2, 9)
            if st + ln > 12: continue
            rows.append((st, ln))
        if len(rows) != 5 or not distinct([l for s, l in rows]) or sum(1 for s, l in rows if s > 0) != 2: continue
        lens = [l for s, l in rows]
        pool = set()
        for s, l in rows: pool |= {l + 1, l - 1, s + l, l + s + 1}
        pool = sorted(x for x in pool if x not in lens and 1 <= x <= 12)
        res = code_table_any(8, 5, lens, rng, 0, 20, n_decoy=4, tries=80, pool=pool)
        if res: word, table = res; break
    labels = rng.sample(things, 5)
    svgs = [tape_row(labels[i], s, s + l) for i, (s, l) in enumerate(rows)]
    cards = [f'<div class="trow"><span class="no">{i+1}</span><div class="tl">{labels[i]}</div><div class="ts">{s}</div><div class="ta"><span class="ab w3"></span> m</div></div>' for i, s in enumerate(svgs)]
    P = code_items_page(8, 5808, "Metres", 1, "Length: measuring in metres (m)", STRAND_ME,
        "1.1, 1.2 (measuring length in metres; the abbreviation m)", ["ME1.1", "ME1.2"], "Code-breaker (metre tape)",
        ["Each tape shows metres.", "How long is each thing? Write it in metres.", INSTR_CODE],
        '<div class="trows">' + "".join(cards) + '</div>', lens, table, word, 0, 20,
        "; ".join(f"{i+1}) {l} m" + (f" (starts at the arrow, {s} m)" if s else "") for i, (s, l) in enumerate(rows)),
        "Five things measured with a metre tape (0 to 12 m). Three bars start at 0; two start at the black arrow, so the pupil counts the metres between the start and the end of the bar (a small extension of measuring). The decoy letters stand for counting to the end of the bar instead of from the start, or one metre out. A box left blank gives no letter and the check cannot see it.")
    solved = [read_tape(s)[1] for s in svgs]
    P.v("V1 independent solver reads the bar and the tape ticks back and equals the key", solved == lens, solved)
    P.v("V7 tape marks are 12.5 mm apart (a real metre tape cannot be copied at this size: drawings are not to scale)", True)
    P["facts"] = " ".join(str(x) for x in table)
    return P

PAGES = [page01, page02, page03, page04, page05, page06, page07, page08]
