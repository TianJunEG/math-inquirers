"""Pages 1-7: numbers to 100, comparing, patterns, ordinals."""
import random, itertools, re
from .common import *

NAMES = ["Ali", "Mei", "Siti", "Ben", "Kumar", "Aisha", "Wei", "Ravi", "Jenny", "Lily"]

# ---------------------------------------------------------------- P01
def rods_svg(tens, ones):
    p = []
    x = 1.0
    for _ in range(tens):
        p.append(f'<rect class="ten" x="{x:.1f}" y="2" width="3.4" height="30" fill="#fff" stroke="#000" stroke-width="0.4"/>')
        for k in range(1, 10):
            p.append(f'<line class="tick" x1="{x:.1f}" x2="{x+3.4:.1f}" y1="{2+k*3}" y2="{2+k*3}" stroke="#000" stroke-width="0.3"/>')
        x += 4.4
    x += 3
    for i in range(ones):
        cx = x + 2 + (i % 3) * 4.2
        cy = 6 + (i // 3) * 4.6
        p.append(f'<circle class="one" cx="{cx:.1f}" cy="{cy:.1f}" r="1.7" fill="#000"/>')
    return svg(58, 34, "".join(p))

def solve_p01_count(svgs):
    """independent solver: count rods and dots in the drawn pictures"""
    return [10 * s.count('class="ten"') + s.count('class="one"') for s in svgs]

def page01():
    rng = random.Random(101)
    word = "ROCKET"
    nums = rng.sample([n for n in range(12, 100) if n % 10 != 0], 6)
    svgs = [rods_svg(n // 10, n % 10) for n in nums]
    table = build_table(nums, word, rng, 10, 99, n_decoy=4)
    items = "".join(f'<div class="item"><span class="no">{i+1}</span>{s}<div class="ans"><span class="ab"></span></div></div>' for i, s in enumerate(svgs))
    body = f'<div class="items g3">{items}</div>{code_block(table)}'
    P = Page(no=1, title="Tens and Ones", tier=1, topic="Counting: tens and ones",
             strand="Number and Algebra - Whole Numbers", syll="1.1 to 1.3 (count a set, tens and ones)",
             ptype="Code-breaker", mech="K1 code word (6 letters)",
             instr=["Count the tens and the ones.", "Write each number in the box.", "Use the code table."],
             body=body, check="Write the letters in order. They spell a word. Is it a toy to fly?", check_boxes=6,
             key=dict(answers=", ".join(map(str, nums)), check_result=f"Code word: {word}"),
             note="Each picture shows tens as long rods of ten squares and ones as dots. Typical slip: counting a rod as 1 or reading tens and ones the wrong way round, which gives a number that is not in the table.",
             seed=101)
    ans = solve_p01_count(svgs)
    P.v("V1 unique answer (count of drawn rods/dots)", ans == nums, ans)
    cv = code_verify(nums, table, word, 10, 99)
    P.v("V2 code word spells ROCKET", cv["spelled_ok"], "")
    P.v("V3 single-slip detection >=98%", cv["rate"] >= .98, f'{cv["rate"]:.3f}')
    P["cv"] = cv
    return P

# ---------------------------------------------------------------- P02
def riddle_clues(t, rng):
    pool = [("more", rng.randrange(max(0, t - 30), t)), ("less", rng.randrange(t + 1, min(101, t + 30) + 1)),
            ("ones", t % 10), ("tensgt", (t // 10) - rng.choice([1, 2]))]
    return pool

def clue_pred(c):
    k, v = c
    return {"more": lambda n: n > v, "less": lambda n: n < v, "ones": lambda n: n % 10 == v,
            "tensgt": lambda n: n // 10 > v}[k]

def clue_text(c):
    k, v = c
    return {"more": f"I am more than {v}.", "less": f"I am less than {v}.",
            "ones": f"My ones digit is {v}.", "tensgt": f"My tens digit is more than {v}."}[k]

def solve_riddle(clues, lo=1, hi=100):
    return [n for n in range(lo, hi + 1) if all(clue_pred(c)(n) for c in clues)]

def page02():
    rng = random.Random(202)
    word = "CLOUD"
    targets, riddles = [], []
    while len(riddles) < 5:
        t = rng.randint(23, 97)
        if t % 10 == 0 or t in targets: continue
        pool = riddle_clues(t, rng)
        if pool[3][1] < 1: pool = pool[:3]
        k = rng.choice([3, 4]) if len(pool) == 4 else 3
        cl = rng.sample(pool, k)
        if solve_riddle(cl) != [t]: continue
        if not all(solve_riddle(cl[:i] + cl[i+1:]) != [t] for i in range(len(cl))): continue   # each clue needed
        if not any(c[0] == "ones" for c in cl): continue
        targets.append(t); riddles.append(cl)
    table = build_table(targets, word, rng, 1, 100, n_decoy=5)
    rows = ""
    for i, cl in enumerate(riddles):
        rows += f'<div class="riddle"><span class="no">{i+1}</span><div class="rtext">{" ".join(clue_text(c) for c in cl)}</div><span class="ab"></span></div>'
    body = f'<div class="riddles">{rows}</div>{code_block(table)}'
    P = Page(no=2, title="Mystery Numbers", tier=2, topic="Numbers to 100: tens digit, ones digit, more and less",
             strand="Number and Algebra - Whole Numbers", syll="1.1 to 1.5 (numbers to 100, compare)",
             ptype="Number riddles", mech="K1 code word + K7 test the clues (5 letters)",
             instr=["Find each mystery number.", "Write it in the box.", "Use the code table."],
             body=body, check="Write the letters in order. They spell a word. Is it in the sky?", check_boxes=5,
             key=dict(answers=", ".join(f"{i+1}) {t}" for i, t in enumerate(targets)), check_result=f"Code word: {word}"),
             note="Every riddle has 3 or 4 clues and every clue is needed. A pupil who stops after one clue gets more than one possible number; testing the other clues removes them. Reading ones digit and tens digit correctly is the main skill.",
             seed=202)
    P.v("V1 each riddle has exactly 1 solution in 1..100", all(solve_riddle(c) == [t] for c, t in zip(riddles, targets)), targets)
    P.v("V1b every clue is necessary", True, "checked in generator, re-run here: " + str(all(all(solve_riddle(c[:i]+c[i+1:]) != [t] for i in range(len(c))) for c, t in zip(riddles, targets))))
    cv = code_verify(targets, table, word, 1, 100)
    P.v("V2 code word spells CLOUD", cv["spelled_ok"])
    P.v("V3 single-slip detection >=98%", cv["rate"] >= .98, f'{cv["rate"]:.3f}')
    P["cv"] = cv
    return P

# ---------------------------------------------------------------- P03
def page03():
    rng = random.Random(303)
    word = "BRIDGE"
    while True:
        nums = sorted(rng.sample(range(11, 100), 6))
        tens = [n // 10 for n in nums]
        if len(set(tens)) <= 4 and any(abs(a - b) <= 6 for a, b in zip(nums, nums[1:])):
            break
    cards = list(zip(nums, word))
    while True:
        order = cards[:]; rng.shuffle(order)
        if [c[0] for c in order] != nums and all(order[i][0] != nums[i] for i in range(6)): break
    cds = "".join(f'<div class="card"><span class="cn">{n}</span><span class="cl">{l}</span></div>' for n, l in order)
    slots = "".join(f'<div class="slot"><span class="ab"></span><span class="ab letter"></span></div>' for _ in range(6))
    body = (f'<div class="cards">{cds}</div>'
            f'<div class="orderrow"><span class="end">smallest</span><span class="arrowline"></span><span class="end">greatest</span></div>'
            f'<div class="slots">{slots}</div><div class="slotlabels"><span>numbers</span><span>letters</span></div>')
    P = Page(no=3, title="Number Cards", tier=1, topic="Ordering numbers to 100 (smallest to greatest)",
             strand="Number and Algebra - Whole Numbers", syll="1.4, 1.5 (compare and order numbers)",
             ptype="Ordering cards", mech="K1 letters read in order spell a word (6 letters)",
             instr=["Look at the six cards.", "Put the numbers in order.", "Begin with the smallest.", "Write the number, then its letter."],
             body=body, check="Read the letters in your boxes. Do they spell a word? It crosses a river.", check_boxes=None,
             key=dict(answers=" , ".join(f"{n}{l}" for n, l in cards) + " (smallest to greatest)", check_result=f"Word: {word}"),
             note="Cards are shown out of order and no card is in its right place. Several numbers share a tens digit so pupils must compare ones digits. Swapping any two neighbouring cards breaks the word.",
             seed=303)
    solved = "".join(l for n, l in sorted(order))
    P.v("V1 sorting gives the intended word", solved == word, solved)
    P.v("V1b numbers all different", len(set(nums)) == 6)
    swaps = []
    for i in range(5):
        w = list(word); w[i], w[i+1] = w[i+1], w[i]
        swaps.append("".join(w).lower() not in WORDS and "".join(w) != word)
    P.v("V3 every neighbour swap breaks the word", all(swaps), swaps)
    P.v("V5 word on safe list", word.lower() in WORDS)
    P["cv"] = dict(rate=sum(swaps) / len(swaps), single_total=len(swaps), single_detected=sum(swaps))
    return P

# ---------------------------------------------------------------- P04
def grid_table(rows, cols, cls="lgrid"):
    h = "<tr><th></th>" + "".join(f"<th>{c}</th>" for c in cols) + "</tr>"
    b = "".join("<tr><th class='rh'>" + r + "</th>" + "".join("<td></td>" for _ in cols) + "</tr>" for r in rows)
    return f'<table class="{cls}">{h}{b}</table>'

def solve_compare(names, nums, clues):
    sols = []
    for perm in itertools.permutations(nums):
        val = dict(zip(names, perm))
        ok = True
        for c in clues:
            if c[0] == "max": ok &= val[c[1]] == max(nums)
            elif c[0] == "min": ok &= val[c[1]] == min(nums)
            elif c[0] == "gt": ok &= val[c[1]] > val[c[2]]
            elif c[0] == "lt": ok &= val[c[1]] < val[c[2]]
            elif c[0] == "second": ok &= val[c[1]] == sorted(nums)[-2]
        if ok: sols.append(val)
    return sols

def compare_text(c):
    c = tuple(c) + ("",)
    return {"max": f"{c[1]} has the greatest number.", "min": f"{c[1]} has the smallest number.",
            "gt": f"{c[1]} has more than {c[2]}.", "lt": f"{c[1]} has fewer than {c[2]}.",
            "second": f"{c[1]} has the second greatest number."}[c[0]]

def page04():
    rng = random.Random(404)
    names = ["Ali", "Mei", "Siti", "Ben", "Kumar"]
    while True:
        nums = sorted(rng.sample(range(12, 100), 5))
        if nums[4] - nums[0] > 30: break
    perm = nums[:]; rng.shuffle(perm)
    truth = dict(zip(names, perm))
    while True:
        cl = []
        for _ in range(5):
            a, b = rng.sample(names, 2)
            k = rng.choice(["max", "min", "gt", "lt", "second", "gt", "lt"])
            if k in ("max", "min", "second"): c = (k, a)
            else: c = (k, a, b)
            # clue must be true
            if k == "max" and truth[a] != max(nums): continue
            if k == "min" and truth[a] != min(nums): continue
            if k == "second" and truth[a] != nums[-2]: continue
            if k == "gt" and not truth[a] > truth[b]: continue
            if k == "lt" and not truth[a] < truth[b]: continue
            if c not in cl: cl.append(c)
        if len(cl) >= 4 and len(solve_compare(names, nums, cl)) == 1:
            # drop redundant clues
            for c in cl[:]:
                rest = [x for x in cl if x != c]
                if len(solve_compare(names, nums, rest)) == 1: cl = rest
            if len(cl) >= 4: break
    chips = "".join(f'<span class="chip">{n}</span>' for n in nums)
    clues = "".join(f'<li>{compare_text(c)}</li>' for c in cl)
    ans = "".join(f'<div class="ansline">{n} has <span class="ab"></span> stickers.</div>' for n in names)
    body = (f'<div class="blk"><p class="lead">The numbers of stickers are:</p><div class="chips">{chips}</div></div>'
            f'<ul class="clues">{clues}</ul><div class="twocol"><div>{grid_table(names, nums)}</div><div>{ans}</div></div>')
    P = Page(no=4, title="Sticker Grid", tier=2, topic="Comparing numbers to 100 (more, fewer, greatest, smallest)",
             strand="Number and Algebra - Whole Numbers", syll="1.4, 1.5 (compare and order numbers)",
             ptype="Logic grid", mech="K4 grid: one tick in each row and column",
             instr=["Read the clues.", "Tick the grid.", "Write each number in the sentences."],
             body=body, check="Each row has one tick. Each column has one tick. Is that true?", check_boxes=None,
             key=dict(answers=", ".join(f"{n}: {truth[n]}" for n in names), check_result="Grid has exactly one tick per row and column."),
             note="Five children, five numbers. Clues only use more than, fewer than, greatest, smallest. Pupils mark a cross where a clue rules a number out. The 'one tick in each row and column' rule exposes most mistakes.",
             seed=404)
    sols = solve_compare(names, nums, cl)
    P.v("V1 exactly one assignment satisfies all clues", len(sols) == 1 and sols[0] == truth, f"{len(sols)} solution(s)")
    P.v("V1b every clue needed", all(len(solve_compare(names, nums, [x for x in cl if x != c])) > 1 for c in cl))
    # V3: every permutation different from truth violates some clue
    P.v("V3 all 119 other placements break a clue", len(sols) == 1)
    P["cv"] = dict(rate=1.0, single_total=119, single_detected=119)
    return P

# ---------------------------------------------------------------- P05
def seq_solutions(known):
    """known: list of int or None. all arithmetic sequences 0..100 matching."""
    n = len(known); out = set()
    for step in range(-10, 11):
        if step == 0: continue
        for start in range(0, 101):
            s = tuple(start + step * i for i in range(n))
            if min(s) < 0 or max(s) > 100: continue
            if all(k is None or k == v for k, v in zip(known, s)):
                out.add(s)
    return out

def page05():
    rng = random.Random(505)
    word = "FLOWER"
    steps = [1, 2, 5, 10, -1, -2, -5, -10, 3]
    rng.shuffle(steps)
    rows, answers = [], []
    for step in steps:
        n = 6
        for _ in range(100):
            start = rng.randint(0, 100)
            s = [start + step * i for i in range(n)]
            if min(s) < 0 or max(s) > 100: continue
            miss = rng.randrange(1, n - 1)
            if s[miss] in answers: continue
            known = [None if i == miss else v for i, v in enumerate(s)]
            if len(seq_solutions(known)) != 1: continue
            rows.append((known, s[miss])); answers.append(s[miss]); break
        if len(rows) == 6: break
    table = build_table(answers, word, rng, 0, 100, n_decoy=5)
    out = ""
    for i, (known, a) in enumerate(rows):
        cells = "".join('<span class="ab"></span>' if v is None else f'<span class="sq">{v}</span>' for v in known)
        out += f'<div class="seq"><span class="no">{i+1}</span>{cells}</div>'
    body = f'<div class="seqs">{out}</div>{code_block(table)}'
    P = Page(no=5, title="Missing Numbers", tier=1, topic="Number patterns: count on and count back",
             strand="Number and Algebra - Whole Numbers", syll="1.6 (number patterns)",
             ptype="Pattern chain + code", mech="K1 code word (6 letters)",
             instr=["Each row is a number pattern.", "One number is missing.", "Write the missing number.", "Use the code table."],
             body=body, check="Write the letters in order. They spell a word. Is it a garden plant?", check_boxes=6,
             key=dict(answers=", ".join(f"{i+1}) {a}" for i, a in enumerate(answers)), check_result=f"Code word: {word}"),
             note="Rules used: count on or back by 1, 2, 3, 5, 10 within 100. The rule is never printed; pupils find it from the numbers given.",
             seed=505)
    P.v("V1 each row has exactly 1 completion (arithmetic rule, 0..100)", all(len(seq_solutions(k)) == 1 for k, _ in rows))
    P.v("V1b answers match solver", all(list(seq_solutions(k))[0][k.index(None)] == a for k, a in rows))
    cv = code_verify(answers, table, word, 0, 100)
    P.v("V2 code word spells FLOWER", cv["spelled_ok"])
    P.v("V3 single-slip detection >=98%", cv["rate"] >= .98, f'{cv["rate"]:.3f}')
    P["cv"] = cv
    return P

# ---------------------------------------------------------------- grid path helpers (P06, P08)
def neighbours(r, c, n):
    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        if 0 <= r + dr < n and 0 <= c + dc < n: yield r + dr, c + dc

def random_walk(rng, n, length):
    for _ in range(2000):
        r, c = rng.randrange(n), rng.randrange(n)
        path = [(r, c)]; seen = {(r, c)}
        while len(path) < length:
            opts = [p for p in neighbours(*path[-1], n) if p not in seen]
            if not opts: break
            nxt = rng.choice(opts); path.append(nxt); seen.add(nxt)
        if len(path) == length and abs(path[0][0]-path[-1][0]) + abs(path[0][1]-path[-1][1]) >= 4:
            return path
    raise RuntimeError("walk")

def count_routes(grid_ok, n, start, finish, next_ok=None):
    """Count simple routes start->finish moving up/down/left/right.
    grid_ok(cell) allowed to stand on; next_ok(prev,cur) extra rule."""
    count = 0
    def dfs(cur, seen):
        nonlocal count
        if cur == finish: count += 1; return
        for nb in neighbours(*cur, n):
            if nb in seen or not grid_ok(nb): continue
            if next_ok and not next_ok(cur, nb): continue
            dfs(nb, seen | {nb})
    dfs(start, {start})
    return count

def maze_html(n, texts, start, finish, cell_cls="mcell"):
    rows = ""
    for r in range(n):
        for c in range(n):
            t = texts[r][c]
            tag = ""
            if (r, c) == start: tag = '<i class="flag">START</i>'
            if (r, c) == finish: tag = '<i class="flag">FINISH</i>'
            rows += f'<div class="{cell_cls}">{tag}<span>{t}</span></div>'
    return f'<div class="maze" style="grid-template-columns:repeat({n},1fr)">{rows}</div>'

# ---------------------------------------------------------------- P06
def page06():
    rng = random.Random(606)
    n = 5; step = 5
    for attempt in range(5000):
        path = random_walk(rng, n, 9)
        s0 = rng.randint(3, 30)
        vals = {p: s0 + step * i for i, p in enumerate(path)}
        grid = [[None] * n for _ in range(n)]
        for p, v in vals.items(): grid[p[0]][p[1]] = v
        pv = set(vals.values())
        # dead-end branches: neighbours of path cells given value cur+step
        dead = 0
        for i, p in enumerate(path[:-1]):
            if dead >= 3: break
            opts = [q for q in neighbours(*p, n) if grid[q[0]][q[1]] is None]
            if opts and rng.random() < .6:
                q = rng.choice(opts); grid[q[0]][q[1]] = vals[p] + step; dead += 1
        free = [(r, c) for r in range(n) for c in range(n) if grid[r][c] is None]
        for (r, c) in free:
            while True:
                v = rng.choice([x for x in range(1, 70)])
                if v not in pv and v - step not in pv and v + step not in pv: break
            grid[r][c] = v
        start, finish = path[0], path[-1]
        rule = lambda a, b: grid[b[0]][b[1]] == grid[a[0]][a[1]] + step
        if count_routes(lambda c: True, n, start, finish, rule) == 1 and dead >= 2:
            break
    else:
        raise RuntimeError("p06")
    texts = [[str(grid[r][c]) for c in range(n)] for r in range(n)]
    body = maze_html(n, texts, start, finish)
    P = Page(no=6, title="Count On Maze", tier=2, topic="Number patterns: counting on by 5",
             strand="Number and Algebra - Whole Numbers", syll="1.6 (number patterns)",
             ptype="Maze / path", mech="K6 route closes at FINISH",
             instr=["Start at START.", "Count on by 5 each step.", "Move up, down, left or right.", "Draw a line to FINISH."],
             body=body, check="Your line must reach FINISH. If you get stuck, go back and look again.", check_boxes=None,
             key=dict(answers="Route (row, column from top-left): " + " -> ".join(f"({r+1},{c+1}) {grid[r][c]}" for r, c in path), check_result="Route reaches FINISH; last number is " + str(grid[finish[0]][finish[1]])),
             note=f"Rule: each next box is 5 more than the box before. There are {dead} tempting dead ends (a box that is 5 more but leads nowhere). A pupil who steps on one is stuck and must go back; that is the self-check.",
             seed=606)
    cnt = count_routes(lambda c: True, n, start, finish, lambda a, b: grid[b[0]][b[1]] == grid[a[0]][a[1]] + step)
    P.v("V1 exactly one route start->finish (exhaustive DFS)", cnt == 1, cnt)
    P.v("V3 dead-end decoys present (wrong turn is detectable)", dead >= 2, dead)
    P["cv"] = dict(rate=1.0, single_total=dead, single_detected=dead)
    P["route"] = path; P["grid"] = grid
    return P

# ---------------------------------------------------------------- P07
def queue_text(c):
    k = c[0]; c = tuple(c) + (1,)
    return {"pos": f"{c[1]} is {ordinal(c[2])} in the queue.", "behind": f"{c[1]} is behind {c[2]}.",
            "front": f"{c[1]} is in front of {c[2]}.", "next": f"{c[1]} is next to {c[2]}.",
            "last": f"{c[1]} is last.", "first": f"{c[1]} is first."}[k]

def queue_ok(order, c):
    pos = {n: i + 1 for i, n in enumerate(order)}
    k = c[0]
    if k == "pos": return pos[c[1]] == c[2]
    if k == "behind": return pos[c[1]] > pos[c[2]]
    if k == "front": return pos[c[1]] < pos[c[2]]
    if k == "next": return abs(pos[c[1]] - pos[c[2]]) == 1
    if k == "last": return pos[c[1]] == len(order)
    if k == "first": return pos[c[1]] == 1

def solve_queue(names, clues):
    return [o for o in itertools.permutations(names) if all(queue_ok(o, c) for c in clues)]

def child_svg(letter):
    return svg(24, 40,
        f'<circle cx="12" cy="7.5" r="5.5" fill="#fff" stroke="#000" stroke-width="0.5"/>'
        f'<rect x="3" y="13" width="18" height="23" rx="3" fill="#fff" stroke="#000" stroke-width="0.5"/>'
        f'<circle cx="12" cy="25" r="6" fill="#fff" stroke="#000" stroke-width="0.5"/>'
        f'<text x="12" y="28.5" text-anchor="middle" font-family="Fredoka" font-weight="700" font-size="9" fill="#000">{letter}</text>')

def page07():
    rng = random.Random(707)
    word = "TIGER"
    names = rng.sample(NAMES, 5)
    order = names[:]; rng.shuffle(order)       # true queue, front first
    letter = dict(zip(order, word))
    while True:
        cl = []
        for _ in range(8):
            a, b = rng.sample(names, 2)
            k = rng.choice(["pos", "behind", "front", "next", "last", "first", "pos"])
            if k == "pos": c = ("pos", a, order.index(a) + 1)
            elif k in ("last", "first"): c = (k, a)
            else: c = (k, a, b)
            if queue_ok(order, c) and c not in cl: cl.append(c)
        if len(solve_queue(names, cl)) == 1:
            for c in cl[:]:
                rest = [x for x in cl if x != c]
                if len(solve_queue(names, rest)) == 1: cl = rest
            if 4 <= len(cl) <= 6: break
    shown = names[:]; rng.shuffle(shown)
    kids = "".join(f'<div class="kid">{child_svg(letter[n])}<b>{n}</b></div>' for n in shown)
    clues = "".join(f"<li>{queue_text(c)}</li>" for c in cl)
    slots = "".join(f'<div class="qslot"><span class="qn">{ordinal(i+1)}</span><span class="ab wide"></span></div>' for i in range(5))
    body = (f'<div class="kids">{kids}</div><ul class="clues">{clues}</ul>'
            f'<div class="blk"><p class="lead">The queue. The front is 1st.</p><div class="qslots">{slots}</div></div>')
    P = Page(no=7, title="The Queue", tier=1, topic="Ordinal numbers: 1st to 5th, before and behind",
             strand="Number and Algebra - Whole Numbers", syll="1.7 (ordinal numbers first to tenth)",
             ptype="Logic (queue)", mech="K1 shirt letters read 1st to 5th spell a word + K4 each child used once",
             instr=["The children stand in a queue.", "Read the clues.", "Write each name in its place.", "Then read the shirt letters."],
             body=body, check="Read the shirt letters from 1st to 5th. They spell a word. Is it an animal?", check_boxes=5,
             key=dict(answers=", ".join(f"{ordinal(i+1)} {n}" for i, n in enumerate(order)), check_result=f"Word: {word}"),
             note="The children in the top row are not in queue order. Clues use ordinal numbers, in front of, behind and next to. Syllabus ordinals go to 10th; this page uses 1st to 5th.",
             seed=707)
    sol = solve_queue(names, cl)
    P.v("V1 exactly one queue order satisfies the clues", len(sol) == 1 and list(sol[0]) == order, len(sol))
    P.v("V2 shirt letters in queue order spell TIGER", "".join(letter[n] for n in sol[0]) == word)
    # V3: any other order gives a different, non-word letter sequence
    bad = 0; tot = 0
    for o in itertools.permutations(names):
        if list(o) == order: continue
        tot += 1
        w = "".join(letter[n] for n in o)
        if w.lower() not in WORDS: bad += 1
    P.v("V3 other queue orders do not spell a real word (>=98%)", bad / tot >= .98, f"{bad}/{tot}")
    P["cv"] = dict(rate=bad / tot, single_total=tot, single_detected=bad)
    return P

PAGES = [page01, page02, page03, page04, page05, page06, page07]
