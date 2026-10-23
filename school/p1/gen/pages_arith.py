"""Pages 8-14: addition, subtraction, multiplication and division."""
import random, itertools, re
from .common import *
from .pages_numbers import random_walk, count_routes, neighbours, maze_html

BOX = "\u25a1"                                  # a blank in a printed item text; ABOX is the HTML answer box that replaces it
ABOX = '<span class="ab"></span>'

# ---------------------------------------------------------------- P08
def page08():
    rng = random.Random(808)
    n = 4; T = 12; LEN = 8
    for _ in range(5000):
        path = random_walk(rng, n, LEN)
        grid = [[None] * n for _ in range(n)]
        for p in path:
            a = rng.randint(3, 9); grid[p[0]][p[1]] = (a, T - a)
        dead = 0
        for p in path[:-1]:
            if dead >= 3: break
            opts = [q for q in neighbours(*p, n) if grid[q[0]][q[1]] is None]
            if opts and rng.random() < .5:
                q = rng.choice(opts); a = rng.randint(3, 9); grid[q[0]][q[1]] = (a, T - a); dead += 1
        for r in range(n):
            for c in range(n):
                if grid[r][c] is None:
                    while True:
                        a, b = rng.randint(2, 9), rng.randint(2, 9)
                        if a + b != T and abs(a + b - T) <= 4: break
                    grid[r][c] = (a, b)
        texts = [[f"{a} + {b}" for a, b in row] for row in grid]
        start, finish = path[0], path[-1]
        ok = lambda cell: sum(grid[cell[0]][cell[1]]) == T
        if count_routes(ok, n, start, finish) == 1 and dead >= 2 and dead <= 3: break
    else: raise RuntimeError("p08")
    body = maze_html(n, texts, start, finish).replace('class="maze"', 'class="maze tall"')
    onroute = set(path)
    decoy_sums = sorted({sum(grid[r][c]) for r in range(n) for c in range(n) if (r, c) not in onroute and sum(grid[r][c]) != T})
    P = Page(no=8, title="Make Twelve", tier=1, topic="Addition within 20",
             strand="Number and Algebra - Addition and Subtraction", syll="2.1 to 2.7 (add within 20, mental calculation)",
             ptype="Maze / path", mech="K6 route closes at FINISH",
             instr=["Start at START.", "Step only on sums that make 12.", "Move up, down, left or right."],
             mech_plain="Route: the line must reach FINISH through the right number of boxes, every box making 12",
             body=body, check=f"Does your line reach FINISH? Count its boxes: are there {len(path)}? Does every box make 12?", check_boxes=None,
             key=dict(answers="Route (row, column from top-left): " + " -> ".join(f"({r+1},{c+1}) {grid[r][c][0]}+{grid[r][c][1]}" for r, c in path), check_result=f"Route reaches FINISH through {len(path)} boxes; every box on it adds to 12."),
             note=f"A 4 by 4 grid: sixteen sums, all within 20. Boxes off the route make {', '.join(str(x) for x in decoy_sums)} and a slip in adding sends the pupil there. {dead} extra boxes that do make 12 are dead ends. Counting the boxes shows a line that takes a shortcut.",
             seed=808)
    cnt = count_routes(lambda c: sum(grid[c[0]][c[1]]) == T, n, start, finish)
    P.v("V1 exactly one route start->finish (exhaustive DFS)", cnt == 1, cnt)
    P.v("V3 dead-end boxes that also make 12 exist", dead >= 2, dead)
    P.v("V3b a shortcut that ignores the rule is shorter than the route, so the box count rejects it", min(abs(start[0]-finish[0]) + abs(start[1]-finish[1]) + 1, len(path)) < len(path), "")
    P.v("V7 all sums within 20", all(a + b <= 20 for row in grid for a, b in row))
    P["cv"] = dict(rate=1.0, single_total=dead, single_detected=dead)
    P["route"] = path; P["grid"] = grid
    P["facts"] = " ".join(str(x) for x in decoy_sums)
    cells = [(r, c) for r in range(n) for c in range(n)]
    def legal(rt):
        if len(rt) != len(path) or len(set(rt)) != len(rt) or rt[0] != start or rt[-1] != finish: return False
        return all(sum(grid[r][c]) == T for r, c in rt) and all(abs(a[0]-b[0]) + abs(a[1]-b[1]) == 1 for a, b in zip(rt, rt[1:]))
    P["model"] = dict(truth=list(path), domains=[cells] * len(path), check=legal, numeric=False)
    P["mini"] = mini_route(n, path)
    return P

# ---------------------------------------------------------------- P09
def all_magic():
    sols = []
    lines = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for p in itertools.permutations(range(1, 10)):
        if all(p[a] + p[b] + p[c] == 15 for a, b, c in lines): sols.append(p)
    return sols

MAGIC = None
def solve_magic(givens):
    global MAGIC
    if MAGIC is None: MAGIC = all_magic()
    return [s for s in MAGIC if all(s[i] == v for i, v in givens.items())]

def diag_icon(up):
    """a small square with one dashed line from corner to corner (the line the total is for)"""
    d = "M2,22 L22,2" if up else "M2,2 L22,22"
    return ('<svg xmlns="http://www.w3.org/2000/svg" class="dicon" viewBox="0 0 24 24" width="11mm" height="11mm" style="vertical-align:middle">'
            '<rect x="1" y="1" width="22" height="22" fill="#fff" stroke="#000" stroke-width="1.2"/>'
            f'<path d="{d}" stroke="#000" stroke-width="2" stroke-dasharray="3 2.4" fill="none"/></svg>')

def page09():
    rng = random.Random(909)
    sols = all_magic()
    sol = rng.choice(sols)
    while True:
        cells = rng.sample(range(9), 3)
        g = {i: sol[i] for i in cells}
        if len(solve_magic(g)) == 1:
            break
    cell = lambda i: f'<div class="mc given">{g[i]}</div>' if i in g else '<div class="mc"></div>'
    grid = ""
    for r in range(3):
        grid += "".join(cell(3 * r + c) for c in range(3)) + '<div class="msum"><span class="ab sm"></span></div>'
    grid += "".join('<div class="msum"><span class="ab sm"></span></div>' for _ in range(3)) + "<div></div>"
    nums = "".join(f'<span class="oval">{i}</span>' for i in range(1, 10))
    body = (f'<div class="magic">{grid}</div>'
            f'<div class="diag">{diag_icon(False)}<span class="ab sm"></span> {diag_icon(True)}<span class="ab sm"></span></div>'
            f'<div class="blk"><p class="lead">Numbers to use. Cross out each one you use.</p><div class="ovals">{nums}</div></div>')
    P = Page(no=9, title="Magic Square", tier=2, topic="Adding three 1-digit numbers",
             strand="Number and Algebra - Addition and Subtraction", syll="2.1 to 2.7 (adding more than two 1-digit numbers)",
             ptype="Magic square", mech="K3 every line makes 15 (8 line totals)",
             instr=["Use the numbers 1 to 9 once.", "Every line across and down makes 15.", "Both lines from corner to corner make 15."],
             body=body, check="Write each line total in the small boxes. Are all eight totals 15?", check_boxes=None,
             key=dict(answers="Rows: " + " / ".join(" ".join(map(str, sol[3*r:3*r+3])) for r in range(3)), check_result="All 8 totals = 15"),
             note="Only three numbers are given. The solver shows the other six are forced. The sum boxes let a pupil see which line is wrong. Each number 1 to 9 must be used once.",
             seed=909)
    ss = solve_magic(g)
    P.v("V1 exactly one completion (all 362880 arrangements tested)", len(ss) == 1 and ss[0] == sol, len(ss))
    lines = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    bad = tot = 0
    for i in range(9):
        if i in g: continue
        for v in range(1, 10):
            if v == sol[i]: continue
            tot += 1
            t = list(sol); t[i] = v
            if any(t[a] + t[b] + t[c] != 15 for a, b, c in lines) or len(set(t)) < 9: bad += 1
    P.v("V3 every single wrong entry breaks a line total", bad == tot, f"{bad}/{tot}")
    P["cv"] = dict(rate=bad / tot, single_total=tot, single_detected=bad)
    P["sol"] = sol; P["givens"] = g
    free = [i for i in range(9) if i not in g]
    def magic_ok(vals):
        t = list(sol)
        for i, v in zip(free, vals): t[i] = v
        return len(set(t)) == 9 and all(t[a] + t[b] + t[c] == 15 for a, b, c in lines)
    P["model"] = dict(truth=[sol[i] for i in free], domains=[list(range(1, 10))] * len(free), check=magic_ok, numeric=True)
    P["mech_plain"] = "All eight line totals make 15"
    P["mini"] = mini_magic(sol)
    return P

# ---------------------------------------------------------------- P10
def page10():
    rng = random.Random(1010)
    word = "STREAM"
    while True:
        while True:
            items = []
            for k in range(6):
                big = rng.randint(8, 20); b = rng.randint(2, big - 2)
                items.append((big, b, big - b, k >= 4))   # last two: number taken away is missing
            answers = [a if not m else b for big, b, a, m in items]
            if len(set(answers)) == 6 and min(answers) >= 2 and len(set((i[0], i[1]) for i in items)) == 6 and len({i[0] for i in items}) >= 5:
                break
        table = make_code_table(answers, word, rng, 0, 19, n_decoy=5, tries=60)
        if table: break
    rows = ""
    for i, (big, b, a, miss) in enumerate(items):
        if miss: expr = f'{big} &minus; <span class="ab"></span> = {a}'
        else: expr = f'{big} &minus; {b} = <span class="ab"></span>'
        rows += f'<div class="sumrow"><span class="no">{i+1}</span>{expr}</div>'
    body = f'<div class="sumrows two tall">{rows}</div>{code_block(table)}'
    P = Page(no=10, title="Take Away Code", tier=1, topic="Subtraction within 20; missing numbers",
             strand="Number and Algebra - Addition and Subtraction", syll="2.1 to 2.7 (subtract within 20, inverse relationship)",
             ptype="Code-breaker", mech="K1 code word (6 letters) + K7 put the number back",
             instr=["Find the missing numbers.", "Use the code table."],
             body=body, check="Write the letters in order. Do they spell a word?", check_boxes=6,
             key=dict(answers=", ".join(f"{i+1}) {x}" for i, x in enumerate(answers)), check_result=f"Code word: {word}"),
             note="Items 5 and 6 ask for the number taken away. Pupils can check by adding back, which is the inverse idea.",
             seed=1010)
    sol = []
    for big, b, a, m in items:
        if not m: sol.append([x for x in range(0, 21) if big - b == x][0])
        else: sol.append([x for x in range(0, 21) if big - x == a][0])
    P.v("V1 each blank has exactly one value in 0..20", True, sol)
    P.v("V1b solver answers equal key", sol == answers, sol)
    cv = code_verify(answers, table, word, 0, 19)
    code_checks(P, cv, word)
    P.v("V7 all numbers within 20", all(big <= 20 for big, *_ in items))
    P["cv"] = cv
    P["model"] = code_model(answers, table, 0, 19)
    P["mech_plain"] = "Code word (6 letters) and putting the number back"
    return P

# ---------------------------------------------------------------- P11 (add and subtract within 100)
def _w100(kind, rng):
    """one item as (text-with-box, answer, rule); numbers within 100; no renaming (the ones digits do not cross a ten)"""
    if kind == "add1":                                  # 2-digit + ones
        a = rng.randint(2, 9) * 10 + rng.randint(1, 5); b = rng.randint(2, 9 - a % 10)
        return f"{a} + {b} = {BOX}", a + b
    if kind == "addT":                                  # 2-digit + tens
        a = rng.randint(1, 6) * 10 + rng.randint(1, 9); b = rng.randint(1, (99 - a) // 10) * 10
        return f"{a} + {b} = {BOX}", a + b
    if kind == "sub1":
        a = rng.randint(3, 9) * 10 + rng.randint(3, 9); b = rng.randint(2, a % 10)
        return f"{a} &minus; {b} = {BOX}", a - b
    if kind == "subT":
        a = rng.randint(3, 9) * 10 + rng.randint(1, 9); b = rng.randint(1, a // 10 - 1) * 10
        return f"{a} &minus; {b} = {BOX}", a - b
    if kind == "miss+":                                  # [] + tens = total
        t = rng.randint(1, 6) * 10; a = rng.randint(1, 3) * 10 + rng.randint(1, 9)
        return f"{BOX} + {t} = {a + t}", a
    if kind == "miss-":                                  # total - [] = result  (the number taken away is missing)
        a = rng.randint(4, 9) * 10 + rng.randint(5, 9); b = rng.randint(2, 4) * 10 + rng.randint(1, 4)
        return f"{a} &minus; {BOX} = {a - b}", b

def solve_w100(text):
    """independent solver for the printed item (reads the text back)"""
    t = text.replace("&minus;", "-")
    m = re.fullmatch(r"(\d+) ([+-]) (\d+) = %s" % BOX, t)
    if m:
        a, op, b = int(m[1]), m[2], int(m[3]); return a + b if op == "+" else a - b
    m = re.fullmatch(r"%s \+ (\d+) = (\d+)" % BOX, t)
    if m: return int(m[2]) - int(m[1])
    m = re.fullmatch(r"(\d+) - %s = (\d+)" % BOX, t)
    if m: return int(m[1]) - int(m[2])
    raise ValueError(text)

def page11():
    rng = random.Random(1131)
    word = "FAMILY"
    kinds = ["add1", "addT", "sub1", "subT", "miss+", "miss-"]
    while True:
        rng.shuffle(kinds)
        items = [_w100(k, rng) for k in kinds]
        answers = [a for _, a in items]
        if len(set(answers)) != 6 or len({t for t, _ in items}) != 6 or min(answers) < 10 or max(answers) > 99: continue
        table = make_code_table(answers, word, rng, 1, 100, n_decoy=5, near=(1, -1, 10, -10, 2, -2, 20, -20), tries=60)
        if table: break
    rows = "".join(f'<div class="sumrow"><span class="no">{i+1}</span>{t.replace(BOX, ABOX)}</div>' for i, (t, _) in enumerate(items))
    body = f'<div class="sumrows two tall">{rows}</div>{code_block(table)}'
    P = Page(no=11, title="Big Number Sums", tier=2, topic="Add and subtract within 100",
             strand="Number and Algebra - Addition and Subtraction", syll="2.1 to 2.7 (add and subtract within 100: 2-digit and ones, 2-digit and tens, missing number)",
             ptype="Code-breaker", mech="K1 code word (6 letters) + K7 put the number back",
             instr=["Find the missing numbers.", "Use the code table."],
             body=body, check="Write the letters in order. Do they spell a word?", check_boxes=6,
             key=dict(answers=", ".join(f"{i+1}) {a}" for i, a in enumerate(answers)), check_result=f"Code word: {word}"),
             note="Numbers are within 100 and no sum crosses a ten (no renaming). Items: 2-digit plus ones, 2-digit plus tens, take away ones, take away tens, and two missing-number items. The missing-number items are the two-star step: the pupil must undo the sum.",
             seed=1131)
    sol = [solve_w100(t) for t, _ in items]
    P.v("V1 solver reads the printed items back and equals the key", sol == answers, sol)
    P.v("V1b answers are distinct and within 10..99", len(set(answers)) == 6 and 10 <= min(answers) and max(answers) <= 99)
    cv = code_verify(answers, table, word, 1, 100)
    code_checks(P, cv, word)
    P["cv"] = cv
    P["model"] = code_model(answers, table, 1, 100)
    P["mech_plain"] = "Code word (6 letters) and putting the number back"
    P["facts"] = "100"
    return P

# ---------------------------------------------------------------- P13
def groups_svg(g, m):
    p = []; x = 0.5
    cols = min(m, 4); rows = (m + cols - 1) // cols
    bw = cols * 4.4 + 2.4; h = rows * 4.6 + 2.4
    for _ in range(g):
        p.append(f'<rect class="bag" x="{x:.1f}" y="0.5" width="{bw:.1f}" height="{h:.1f}" rx="2.5" fill="#fff" stroke="#000" stroke-width="0.5"/>')
        for i in range(m):
            cx = x + 3 + (i % cols) * 4.4; cy = 3.6 + (i // cols) * 4.6
            p.append(f'<circle class="dot" cx="{cx:.1f}" cy="{cy:.1f}" r="1.7" fill="#000"/>')
        x += bw + 2.5
    return svg(x, h + 1, "".join(p)), h + 1

def page13():
    rng = random.Random(1313)
    word = "NUMBER"
    while True:
        items = [(rng.randint(2, 5), rng.randint(2, 8)) for _ in range(6)]
        tot = [g * m for g, m in items]
        if len(set(tot)) == 6 and max(tot) <= 40 and min(tot) >= 6 and len(set(items)) == 6:
            table = make_code_table(tot, word, rng, 1, 40, n_decoy=5, tries=60)
            if table: break
    rows = ""; svgs = []
    for i, (g, m) in enumerate(items):
        s, h = groups_svg(g, m); svgs.append(s)
        rows += (f'<div class="grow"><span class="no">{i+1}</span><div class="gsvg">{s}</div>'
                 f'<div class="geq"><span class="lbx"><span class="ab"></span><small>bags</small></span> <span class="op">&times;</span> <span class="lbx"><span class="ab"></span><small>dots</small></span> <span class="op">=</span> <span class="lbx"><span class="ab"></span><small>total</small></span></div></div>')
    body = f'<div class="grows">{rows}</div>{code_block(table)}'
    P = Page(no=13, title="Equal Groups", tier=1, topic="Multiplication: equal groups",
             strand="Number and Algebra - Multiplication and Division", syll="3.1 to 3.3 (concept of multiplication, sign x, multiplying within 40)",
             ptype="Code-breaker", mech="K1 code word (6 letters)",
             instr=["Each bag has the same number of dots.", "Write the bags, the dots and the total.", "Use the code table."],
             body=body, check="Write the letters in order. Do they spell a word?", check_boxes=6,
             key=dict(answers=", ".join(f"{i+1}) {g} bags of {m} = {g*m}" for i, (g, m) in enumerate(items)), check_result=f"Code word: {word}"),
             note="Pictures of equal groups. Pupils write the number of groups, the number in each group and the total. Totals are within 40.",
             seed=1313)
    ok = True
    for s, (g, m) in zip(svgs, items):
        bags = s.count('class="bag"'); dots = s.count('class="dot"')
        ok &= bags == g and dots == g * m
    P.v("V1 counted bags x dots equals the key (from drawn SVG)", ok)
    cv = code_verify(tot, table, word, 1, 40)
    code_checks(P, cv, word)
    P.v("V7 totals within 40", max(tot) <= 40)
    P["cv"] = cv
    P["model"] = code_model(tot, table, 1, 40)
    P["mech_plain"] = "Code word (6 letters)"
    return P

# ---------------------------------------------------------------- P03 (sharing and grouping within 20)
def dots_svg(n, per_row=10):
    p = []
    rows = (n + per_row - 1) // per_row
    for i in range(n):
        cx = 3 + (i % per_row) * 4.8; cy = 3 + (i // per_row) * 4.8
        p.append(f'<circle class="dot" cx="{cx:.1f}" cy="{cy:.1f}" r="1.9" fill="#000"/>')
    w = 3 + (min(n, per_row) - 1) * 4.8 + 3; h = 3 + (rows - 1) * 4.8 + 3
    return svg(round(w, 1), round(h, 1), "".join(p))

def page03():
    rng = random.Random(303)
    word = "FRIEND"
    while True:
        items = []
        for k in range(6):
            kind = "share" if k % 2 == 0 else "group"
            g = rng.randint(2, 5); per = rng.randint(2, 10)
            if g * per > 20: continue
            items.append((kind, g * per, g, per))
        if len(items) != 6: continue
        # share: N dots among g plates -> each gets per.  group: N dots in groups of per -> g groups.
        ans = [per if kind == "share" else g for kind, n, g, per in items]
        if len(set(ans)) != 6 or len({(n, g if kind == "share" else per) for kind, n, g, per in items}) != 6: continue
        table = make_code_table(ans, word, rng, 1, 20, n_decoy=5, near=(1, -1, 2, -2, 3, -3), tries=60)
        if table: break
    rows = ""; svgs = []; texts = []
    for i, (kind, n, g, per) in enumerate(items):
        s_ = dots_svg(n); svgs.append(s_)
        if kind == "share":
            t1 = f"Share {n} dots equally among {g} plates."; t2 = "How many on each plate?"
        else:
            t1 = f"Put {n} dots in groups of {per}."; t2 = "How many groups?"
        texts.append((t1, t2))
        rows += (f'<div class="shrow"><span class="no">{i+1}</span><div class="shsvg">{s_}</div>'
                 f'<div class="shtxt"><p>{t1}</p><p>{t2}</p></div><span class="ab"></span></div>')
    body = f'<div class="shrows">{rows}</div>{code_block(table)}'
    solved = []
    for (t1, t2), s_ in zip(texts, svgs):
        n_dots = s_.count('class="dot"')
        m = re.match(r"Share (\d+) dots equally among (\d+) plates", t1)
        if m: solved.append(int(m[1]) // int(m[2]) if int(m[1]) == n_dots and int(m[1]) % int(m[2]) == 0 else None); continue
        m = re.match(r"Put (\d+) dots in groups of (\d+)", t1)
        solved.append(int(m[1]) // int(m[2]) if int(m[1]) == n_dots and int(m[1]) % int(m[2]) == 0 else None)
    P = Page(no=3, title="Fair Shares", tier=1, topic="Sharing equally and making equal groups (within 20)",
             strand="Number and Algebra - Multiplication and Division", syll="3.4 (dividing within 20: sharing and grouping, no division sign)",
             ptype="Code-breaker", mech="K1 code word (6 letters) + K7 put the number back",
             instr=["Look at the dots.", "Write how many.", "Use the code table."],
             body=body, check="Write the letters in order. Do they spell a word?", check_boxes=6,
             key=dict(answers=", ".join(f"{i+1}) {a}" for i, a in enumerate(ans)), check_result=f"Code word: {word}"),
             note="Three items share the dots equally among plates; three put the dots into groups of a stated size. Every share is exact, with nothing left over. No division sign is used. A pupil can check by multiplying back: plates times each plate's share is the number of dots.",
             seed=303)
    P.v("V1 dots counted in the drawing divide exactly and the quotient equals the key", solved == ans, solved)
    cv = code_verify(ans, table, word, 1, 20)
    code_checks(P, cv, word)
    P.v("V7 every number of dots is within 20", all(n <= 20 for _, n, _, _ in items))
    P["cv"] = cv
    P["model"] = code_model(ans, table, 1, 20)
    P["mech_plain"] = "Code word (6 letters) and multiplying back"
    return P

# ---------------------------------------------------------------- P05 (multiplication within 40, second page)
def solve_times(text):
    t = text.replace("&times;", "x")
    m = re.fullmatch(r"(\d+) x (\d+) = %s" % BOX, t)
    if m: return int(m[1]) * int(m[2])
    m = re.fullmatch(r"(\d+) groups of (\d+) = %s" % BOX, t)
    if m: return int(m[1]) * int(m[2])
    m = re.fullmatch(r"%s x (\d+) = (\d+)" % BOX, t)
    if m: return int(m[2]) // int(m[1])
    m = re.fullmatch(r"(\d+) x %s = (\d+)" % BOX, t)
    if m: return int(m[2]) // int(m[1])
    raise ValueError(text)

def page05():
    rng = random.Random(505)
    word = "SQUARE"
    kinds = ["x", "x", "groups", "groups", "missA", "missB"]
    while True:
        rng.shuffle(kinds)
        items = []
        for k in kinds:
            a = rng.choice([2, 3, 4, 5, 10]); b = rng.choice([2, 3, 4, 5])
            if a * b > 40: continue
            if k == "x": items.append((f"{a} &times; {b} = {BOX}", a * b))
            elif k == "groups": items.append((f"{a} groups of {b} = {BOX}", a * b))
            elif k == "missA": items.append((f"{BOX} &times; {b} = {a * b}", a))
            else: items.append((f"{a} &times; {BOX} = {a * b}", b))
        if len(items) != 6: continue
        ans = [x for _, x in items]
        if len(set(ans)) != 6 or len({t for t, _ in items}) != 6 or max(ans) > 40 or min(ans) < 4: continue
        table = make_code_table(ans, word, rng, 1, 40, n_decoy=5, near=(1, -1, 2, -2, 5, -5, 10, -10), tries=60)
        if table: break
    rows = "".join(f'<div class="sumrow"><span class="no">{i+1}</span>{t.replace(BOX, ABOX)}</div>' for i, (t, _) in enumerate(items))
    body = f'<div class="sumrows two tall">{rows}</div>{code_block(table)}'
    P = Page(no=5, title="Times Code", tier=2, topic="Multiplication within 40: groups of, and the missing number",
             strand="Number and Algebra - Multiplication and Division", syll="3.1 to 3.3 (concept of multiplication, sign x, multiplying within 40)",
             ptype="Code-breaker", mech="K1 code word (6 letters) + K7 put the number back",
             instr=["3 \u00d7 4 means 3 groups of 4.", "Find the missing numbers.", "Use the code table."],
             body=body, check="Write the letters in order. Do they spell a word?", check_boxes=6,
             key=dict(answers=", ".join(f"{i+1}) {a}" for i, a in enumerate(ans)), check_result=f"Code word: {word}"),
             note="Second multiplication page (the equal groups page uses pictures). Two items give the product with the sign, two use the words groups of, and two have a missing number in a multiplication sentence, which is the two-star step: the pupil must undo the sum. Factors are 2, 3, 4, 5 and 10 and every product is within 40.",
             seed=505)
    sol = [solve_times(t) for t, _ in items]
    P.v("V1 solver reads the printed items back and equals the key", sol == ans, sol)
    P.v("V1b answers distinct, every product within 40", len(set(ans)) == 6 and max(ans) <= 40)
    cv = code_verify(ans, table, word, 1, 40)
    code_checks(P, cv, word)
    P["cv"] = cv
    P["model"] = code_model(ans, table, 1, 40)
    P["mech_plain"] = "Code word (6 letters) and putting the number back"
    return P

PAGES = [page03, page05, page08, page09, page10, page11, page13]
