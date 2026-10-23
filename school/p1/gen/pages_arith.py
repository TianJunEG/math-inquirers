"""Pages 8-14: addition, subtraction, multiplication and division."""
import random, itertools, re
from .common import *
from .pages_numbers import random_walk, count_routes, neighbours, maze_html

# ---------------------------------------------------------------- P08
def page08():
    rng = random.Random(808)
    n = 5; T = 12
    for _ in range(5000):
        path = random_walk(rng, n, 10)
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
        if count_routes(ok, n, start, finish) == 1 and dead >= 2: break
    else: raise RuntimeError("p08")
    body = maze_html(n, texts, start, finish)
    P = Page(no=8, title="Make Twelve", tier=1, topic="Addition within 20",
             strand="Number and Algebra - Addition and Subtraction", syll="2.1 to 2.4, 2.7 (add within 20, mental calculation)",
             ptype="Maze / path", mech="K6 route closes at FINISH",
             instr=["Start at START.", "Step only on sums that make 12.", "Move up, down, left or right.", "Draw a line to FINISH."],
             body=body, check="Your line must reach FINISH. If you get stuck, go back and look again.", check_boxes=None,
             key=dict(answers="Route (row, column from top-left): " + " -> ".join(f"({r+1},{c+1}) {grid[r][c][0]}+{grid[r][c][1]}" for r, c in path), check_result="Route reaches FINISH; every box on it adds to 12."),
             note=f"All sums are within 20. Decoy boxes make 10, 11, 13 or 14 so a slip in adding sends the pupil off the route. {dead} extra boxes that do make 12 are dead ends.",
             seed=808)
    cnt = count_routes(lambda c: sum(grid[c[0]][c[1]]) == T, n, start, finish)
    P.v("V1 exactly one route start->finish (exhaustive DFS)", cnt == 1, cnt)
    P.v("V3 dead-end boxes that also make 12 exist", dead >= 2, dead)
    P.v("V7 all sums within 20", all(a + b <= 20 for row in grid for a, b in row))
    P["cv"] = dict(rate=1.0, single_total=dead, single_detected=dead)
    P["route"] = path; P["grid"] = grid
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
            f'<div class="diag">Corner to corner: <span class="ab sm"></span> and <span class="ab sm"></span></div>'
            f'<div class="blk"><p class="lead">Numbers to use. Cross out each one you use.</p><div class="ovals">{nums}</div></div>')
    P = Page(no=9, title="Magic Square", tier=2, topic="Adding three 1-digit numbers",
             strand="Number and Algebra - Addition and Subtraction", syll="2.4 (add more than two 1-digit numbers)",
             ptype="Magic square", mech="K3 every line makes 15 (8 line totals)",
             instr=["Use the numbers 1 to 9 once.", "Every row makes 15.", "Every column makes 15.", "Both corner lines make 15."],
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
    return P

# ---------------------------------------------------------------- P10
def page10():
    rng = random.Random(1010)
    word = "CASTLE"
    while True:
        items = []
        for k in range(6):
            big = rng.randint(8, 20); b = rng.randint(2, big - 2)
            items.append((big, b, big - b, k >= 4))   # last two: number taken away is missing
        answers = [a if not m else b for big, b, a, m in items]
        if len(set(answers)) == 6 and min(answers) >= 2 and len(set((i[0], i[1]) for i in items)) == 6:
            break
    rows = ""
    for i, (big, b, a, miss) in enumerate(items):
        if miss: expr = f'{big} &minus; <span class="ab"></span> = {a}'
        else: expr = f'{big} &minus; {b} = <span class="ab"></span>'
        rows += f'<div class="sumrow"><span class="no">{i+1}</span>{expr}</div>'
    # missing type: pupil writes b, so answer for those is b
    table = build_table(answers, word, rng, 0, 19, n_decoy=5)
    body = f'<div class="sumrows two">{rows}</div>{code_block(table)}'
    P = Page(no=10, title="Take Away Code", tier=1, topic="Subtraction within 20; missing numbers",
             strand="Number and Algebra - Addition and Subtraction", syll="2.1 to 2.3, 2.7 (subtract within 20, inverse)",
             ptype="Code-breaker", mech="K1 code word (6 letters) + K7 put the number back",
             instr=["Find the missing numbers.", "Use the code table."],
             body=body, check="Write the letters in order. They spell a word. Is it where a king lives?", check_boxes=6,
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
    P.v("V2 code word spells CASTLE", cv["spelled_ok"])
    P.v("V3 single-slip detection >=98%", cv["rate"] >= .98, f'{cv["rate"]:.3f}')
    P.v("V7 all numbers within 20", all(big <= 20 for big, *_ in items))
    P["cv"] = cv
    return P

def page10_retry():
    raise RuntimeError("p10 duplicates")

# ---------------------------------------------------------------- P11
def shape_icon(kind, s=9):
    return svg(s, s, shape_svg(kind, s / 2, s / 2, s * 0.9, fill="#000" if kind in ("circle", "star") else "#fff", sw=0.45))

def solve_shapes(eqs):
    sols = []
    for a, b, c in itertools.product(range(1, 10), repeat=3):
        v = (a, b, c)
        if all(sum(v[i] for i in e) == n for e, n in eqs): sols.append(v)
    return sols

def page11():
    rng = random.Random(1111)
    word = "SPRING"
    sets = [("circle", "square", "tri"), ("star", "diamond", "pent")]
    while True:
        vals = rng.sample(range(1, 10), 6)
        setvals = [vals[:3], vals[3:]]
        eqsets = []
        for sv in setvals:
            for _ in range(300):
                eqs = []
                for _ in range(3):
                    size = rng.choice([2, 2, 3])
                    e = tuple(sorted(rng.choice([0, 1, 2]) for _ in range(size)))
                    if len(set(e)) == 1 and size == 3 and False: continue
                    eqs.append((e, sum(sv[i] for i in e)))
                if len({e for e, _ in eqs}) < 3: continue
                if any(n > 20 for _, n in eqs): continue
                if len(solve_shapes(eqs)) == 1 and {i for e, _ in eqs for i in e} == {0, 1, 2}: break
            else: eqsets = None; break
            eqsets.append(eqs)
        if eqsets: break
    blocks = ""
    for si, (shp, eqs) in enumerate(zip(sets, eqsets)):
        lines = ""
        for e, n in eqs:
            lines += '<div class="eq">' + ' <span class="op">+</span> '.join(shape_icon(shp[i]) for i in e) + f' <span class="op">=</span> <b>{n}</b></div>'
        ans = "".join(f'<div class="shans">{shape_icon(shp[i], 11)} <span class="op">=</span> <span class="ab"></span></div>' for i in range(3))
        blocks += f'<div class="shblock"><div class="eqs">{lines}</div><div class="shansw">{ans}</div></div>'
    table = build_table(vals, word, rng, 1, 9, n_decoy=3, near=(1, -1, 2, -2, 3, -3))
    for v in range(1, 10):          # make a complete 1..9 table so nothing is blank
        pass
    body = f'{blocks}{code_block(table)}'
    P = Page(no=11, title="Shape Sums", tier=2, topic="Add and subtract within 20: find the missing number",
             strand="Number and Algebra - Addition and Subtraction", syll="2.1 to 2.4 (add, subtract, inverse, more than two 1-digit numbers)",
             ptype="Balance / picture equations", mech="K7 put the numbers back + K1 code word (6 letters)",
             instr=["Each shape stands for a number.", "Same shape, same number.", "Find the number for each shape.", "Use the code table."],
             body=body, check="Put your numbers back in each sum. Then write the letters. Is it a season?", check_boxes=6,
             key=dict(answers="; ".join(f"Set {k+1}: " + ", ".join(f"{shp[i]}={sv[i]}" for i in range(3)) for k, (shp, sv) in enumerate(zip(sets, setvals))), check_result=f"Code word: {word}"),
             note="Each set has three sums and three shapes; the three sums fix all three numbers. All six numbers are different so the code table has one letter per number.",
             seed=1111)
    ok = all(solve_shapes(eqs) == [tuple(sv)] for eqs, sv in zip(eqsets, setvals))
    P.v("V1 each set has exactly one solution (all 729 triples tested)", ok)
    cv = code_verify(vals, table, word, 1, 9)
    P.v("V2 code word spells SPRING", cv["spelled_ok"])
    P.v("V3 single-slip detection >=98%", cv["rate"] >= .98, f'{cv["rate"]:.3f}')
    P.v("V7 all sums within 20", all(n <= 20 for eqs in eqsets for _, n in eqs))
    P["cv"] = cv
    return P

# ---------------------------------------------------------------- colour-by-answer (P12, P14)
def evaluate(expr):
    e = expr.replace("&minus;", "-").replace("&times;", "*").replace("&divide;", "/")
    a = re.match(r"^(\d+) ([-+*/]) (\d+)$", e)
    x, op, y = int(a.group(1)), a.group(2), int(a.group(3))
    return {"+": x + y, "-": x - y, "*": x * y, "/": x / y}[op]

def exprs_for_add(v, rng):
    o = []
    for b in range(1, v % 10 + 1): o.append(f"{v-b} + {b}")
    for k in range(1, 8):
        if v - 10 * k >= 10: o.append(f"{v-10*k} + {10*k}")
    for b in range(1, 10):
        if v % 10 + b <= 9 and v + b <= 99: o.append(f"{v+b} &minus; {b}")
    for k in range(1, 8):
        if v + 10 * k <= 99: o.append(f"{v+10*k} &minus; {10*k}")
    return o

def exprs_for_muldiv(v, rng):
    o = []
    for a in range(2, 11):
        if v % a == 0 and 2 <= v // a <= 10: o.append(f"{a} &times; {v//a}")
    for q in range(2, 11):
        if v * q <= 20: o.append(f"{v*q} &divide; {q}")
    return o

def colour_page(rng, mask, S, mkexprs, near_vals):
    n = len(mask)
    cells, exprs = [], []
    for r in range(n):
        for c in range(n):
            if mask[r][c] == "#":
                v = rng.choice(S)
            else:
                v = rng.choice(near_vals)
            e = rng.choice(mkexprs(v, rng))
            exprs.append(e)
    return exprs

def colour_body(mask, exprs):
    n = len(mask)
    cells = "".join(f'<div class="ccell"><span class="ex">{e}</span><span class="eqsign">=</span><span class="ln"></span></div>' for e in exprs)
    return f'<div class="cgrid" style="grid-template-columns:repeat({n},1fr)">{cells}</div>'

def solve_colour(exprs, S, n):
    vals = [evaluate(e) for e in exprs]
    return ["".join("#" if vals[r * n + c] in S else "." for c in range(n)) for r in range(n)], vals

def colour_verify(P, mask, exprs, S, n, slip_vals):
    got, vals = solve_colour(exprs, S, n)
    P.v("V1 evaluating every box gives exactly the intended picture", got == mask)
    flips = tot = 0
    for v in vals:
        for d in slip_vals:
            tot += 1
            if (v in S) != ((v + d) in S): flips += 1
    P.v("V3 slips of +-1 or +-10 that change the picture (informational, see README)", flips / tot >= .15, f"{flips}/{tot} = {flips/tot:.2f}")
    P["cv"] = dict(rate=flips / tot, single_total=tot, single_detected=flips)
    P["mask"] = mask; P["exprs"] = exprs; P["S"] = S

HEART = [".#.#.", "#####", "#####", ".###.", "..#.."]
HOUSE = ["..##..", ".####.", "######", "######", "##..##", "##..##"]

def page12():
    rng = random.Random(1212)
    S = [35, 46, 58]
    mask = HEART
    near = [34, 36, 45, 47, 57, 59, 25, 56, 48, 68, 36, 44, 49, 38, 55]
    exprs = colour_page(rng, mask, S, exprs_for_add, near)
    body = colour_body(mask, exprs)
    shaded = sum(r.count("#") for r in mask)
    P = Page(no=12, title="Shade the Picture", tier=1, topic="Add and subtract within 100 (no renaming)",
             strand="Number and Algebra - Addition and Subtraction", syll="2.5 to 2.7 (add and subtract within 100, 2-digit and ones, 2-digit and tens)",
             ptype="Picture-fill (colour by answer)", mech="K2 hidden picture appears",
             instr=["Work out each sum.", "Write the answer on the line.", "Shade boxes with answer 35, 46 or 58."],
             body=body, check=f"A picture appears. It has {shaded} shaded boxes. Is it a shape for love?", check_boxes=None,
             key=dict(answers="Answers by row: " + " | ".join(", ".join(str(int(evaluate(e))) for e in exprs[r*5:r*5+5]) for r in range(5)), check_result=f"Picture: heart, {shaded} shaded boxes"),
             note="Only 2-digit plus or minus a 1-digit number or a whole ten, with no renaming. Distractor answers sit next to the shaded values (such as 34, 36, 45, 47) so a slip leaves a gap or an extra box in the picture.",
             seed=1212)
    colour_verify(P, mask, exprs, S, 5, [1, -1, 10, -10])
    P.v("V7 all answers within 100", all(0 <= evaluate(e) <= 100 for e in exprs))
    return P

def page14():
    rng = random.Random(1414)
    S = [8, 12, 20]
    mask = HOUSE
    near = [6, 7, 9, 10, 14, 15, 16, 18, 24, 5, 4, 21, 9, 7, 16]
    exprs = colour_page(rng, mask, S, exprs_for_muldiv, near)
    body = colour_body(mask, exprs)
    shaded = sum(r.count("#") for r in mask)
    P = Page(no=14, title="Times and Share", tier=2, topic="Multiplication within 40 and division within 20",
             strand="Number and Algebra - Multiplication and Division", syll="3.2 to 3.4 (multiplying within 40, dividing within 20)",
             ptype="Picture-fill (colour by answer)", mech="K2 hidden picture appears",
             instr=["Work out each box.", "Write the answer on the line.", "Shade boxes with answer 8, 12 or 20."],
             body=body, check=f"A picture appears. It has {shaded} shaded boxes. Is it a place to live?", check_boxes=None,
             key=dict(answers="Answers by row: " + " | ".join(", ".join(str(int(evaluate(e))) for e in exprs[r*6:r*6+6]) for r in range(6)), check_result=f"Picture: house with a door gap, {shaded} shaded boxes"),
             note="Products are within 40 and every division has a dividend within 20. Decoy answers such as 7, 9, 10, 14 and 16 sit near the shaded values.",
             seed=1414)
    colour_verify(P, mask, exprs, S, 6, [1, -1, 2, -2])
    P.v("V7 products <= 40, dividends <= 20", all((("&times;" in e) and evaluate(e) <= 40) or (("&divide;" in e) and int(e.split()[0]) <= 20) for e in exprs))
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
    word = "PLANET"
    while True:
        items = [(rng.randint(2, 5), rng.randint(2, 8)) for _ in range(6)]
        tot = [g * m for g, m in items]
        if len(set(tot)) == 6 and max(tot) <= 40 and min(tot) >= 6 and len(set(items)) == 6: break
    table = build_table(tot, word, rng, 1, 40, n_decoy=5)
    rows = ""; svgs = []
    for i, (g, m) in enumerate(items):
        s, h = groups_svg(g, m); svgs.append(s)
        rows += (f'<div class="grow"><span class="no">{i+1}</span><div class="gsvg">{s}</div>'
                 f'<div class="geq"><span class="ab"></span> <span class="op">&times;</span> <span class="ab"></span> <span class="op">=</span> <span class="ab"></span></div></div>')
    body = f'<div class="grows">{rows}</div>{code_block(table)}'
    P = Page(no=13, title="Equal Groups", tier=1, topic="Multiplication: equal groups",
             strand="Number and Algebra - Multiplication and Division", syll="3.1, 3.2 (concept of multiplication, multiplying within 40)",
             ptype="Code-breaker", mech="K1 code word (6 letters)",
             instr=["Each bag has the same number of dots.", "Write: bags, dots in each bag, total.", "Use the code table."],
             body=body, check="Write the letters in order. They spell a word. Is it in space?", check_boxes=6,
             key=dict(answers=", ".join(f"{i+1}) {g} x {m} = {g*m}" for i, (g, m) in enumerate(items)), check_result=f"Code word: {word}"),
             note="Pictures of equal groups. Pupils write the number of groups, the number in each group and the total. Totals are within 40.",
             seed=1313)
    ok = True
    for s, (g, m) in zip(svgs, items):
        bags = s.count('class="bag"'); dots = s.count('class="dot"')
        ok &= bags == g and dots == g * m
    P.v("V1 counted bags x dots equals the key (from drawn SVG)", ok)
    cv = code_verify(tot, table, word, 1, 40)
    P.v("V2 code word spells PLANET", cv["spelled_ok"])
    P.v("V3 single-slip detection >=98%", cv["rate"] >= .98, f'{cv["rate"]:.3f}')
    P.v("V7 totals within 40", max(tot) <= 40)
    P["cv"] = cv
    return P

PAGES = [page08, page09, page10, page11, page12, page13, page14]
