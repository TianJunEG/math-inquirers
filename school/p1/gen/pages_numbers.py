"""Pages 1-5 and 7: numbers to 100, comparing, patterns, ordinals (page 6 is in pages_measure.py)."""
import random, itertools, re
from .common import *

NAMES = ["Ali", "Mei", "Siti", "Ben", "Kumar", "Aisha", "Wei", "Ravi", "Jenny", "Lily"]

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
        rows += f'<div class="riddle"><span class="no">{i+1}</span><div class="rtext">{"<br>".join(clue_text(c) for c in cl)}</div><span class="ab"></span></div>'
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
    P["model"] = code_model(targets, table, 1, 100)
    P["mech_plain"] = "Code word (5 letters) and testing each clue"
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
    nrow = '<span class="rl">number</span>' + "".join('<span class="ab"></span>' for _ in range(6))
    lrow = '<span class="rl">letter</span>' + "".join('<span class="ab letter"></span>' for _ in range(6))
    body = (f'<div class="cards">{cds}</div>'
            f'<div class="orderrow"><span class="end">smallest</span><span class="arrowline"></span><span class="end">greatest</span></div>'
            f'<div class="slots">{nrow}{lrow}</div>')
    P = Page(no=3, title="Number Cards", tier=1, topic="Ordering numbers to 100 (smallest to greatest)",
             strand="Number and Algebra - Whole Numbers", syll="1.4, 1.5 (compare and order numbers)",
             ptype="Ordering cards", mech="K1 letters read in order spell a word (6 letters)",
             instr=["Look at the six cards.", "Arrange the numbers in order.", "Begin with the smallest.", "Write each number, then its letter below."],
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
    P["model"] = dict(truth=list(word), domains=[list(word)] * 6, check=letters_check(), perm=list(range(6)))
    P["mech_plain"] = "Code word from the letters in order (6 letters)"
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

def howto_grid():
    """Small worked example that teaches how to use a logic grid (no content from the real puzzle)."""
    tick = '<svg viewBox="0 0 10 10" width="5mm" height="5mm"><polyline points="1.5,5.5 4,8 8.5,2" fill="none" stroke="#000" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/></svg>'
    cross = '<svg viewBox="0 0 10 10" width="4mm" height="4mm"><path d="M2,2 L8,8 M8,2 L2,8" stroke="#000" stroke-width="1.2" stroke-linecap="round"/></svg>'
    t = (f'<table class="lgrid mini"><tr><th></th><th>5</th><th>9</th></tr>'
         f'<tr><th class="rh">Zed</th><td>{tick}</td><td>{cross}</td></tr>'
         f'<tr><th class="rh">Yan</th><td>{cross}</td><td></td></tr></table>')
    return ('<div class="howto"><b>How to use the grid</b><div class="hw">' + t +
            '<div class="hwt"><p>Clue: Zed has 5.</p><p>Tick Zed under 5.</p><p>Cross out the rest of that line across and down.</p></div></div></div>')

def page04():
    rng = random.Random(404)
    names = ["Ali", "Mei", "Siti", "Ben", "Kumar"]
    word = "HOUSE"
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
    letter_of = {truth[n]: word[i] for i, n in enumerate(names)}     # letter printed beside each number
    chips = "".join(f'<span class="chip">{n} <i class="cl">{letter_of[n]}</i></span>' for n in nums)
    clues = "".join(f'<li>{compare_text(c)}</li>' for c in cl)
    ans = ('<div class="ansgrid"><span></span><b>number</b><b>letter</b>' +
           "".join(f'<span class="nm">{n}</span><span class="ab"></span><span class="ab"></span>' for n in names) + '</div>')
    body = (f'<div class="blk"><p class="lead">The numbers of stickers are:</p><div class="chips">{chips}</div></div>'
            f'<div class="twocol"><ul class="clues">{clues}</ul>{howto_grid()}</div>'
            f'<div class="twocol"><div>{grid_table(names, nums)}</div><div>{ans}</div></div>')
    P = Page(no=4, title="Sticker Grid", tier=2, topic="Comparing numbers to 100 (more, fewer, greatest, smallest)",
             strand="Number and Algebra - Whole Numbers", syll="1.4, 1.5 (compare and order numbers)",
             ptype="Logic grid", mech="K4 grid + K1 letter beside each number spells a word (5 letters)",
             mech_plain="Letters beside the numbers, read down the list, spell a word (5 letters)",
             instr=["Read the clues.", "Cross a box if a clue says no.", "Tick a box if it must be yes.", "Write each number, then its letter."],
             body=body, check="Read the five letters down your list. Do they spell a word? You live in it.", check_boxes=5,
             key=dict(answers=", ".join(f"{n}: {truth[n]} ({letter_of[truth[n]]})" for n in names), check_result=f"Letters down the list: {word}"),
             note="Five children, five numbers, and each number has a letter. A wrong placement puts the letters in the wrong order, so the word does not appear. The page shows a worked example of crosses and ticks. Clues use more than, fewer than, greatest, smallest, second greatest.",
             seed=404)
    sols = solve_compare(names, nums, cl)
    P.v("V1 exactly one assignment satisfies all clues", len(sols) == 1 and sols[0] == truth, f"{len(sols)} solution(s)")
    P.v("V1b every clue needed", all(len(solve_compare(names, nums, [x for x in cl if x != c])) > 1 for c in cl))
    P.v("V2 letters beside the numbers, read in name order, spell HOUSE", "".join(letter_of[truth[n]] for n in names) == word)
    # V3: of the 119 wrong placements, count those that spell a real word (must be <=5%)
    wrong = [pp for pp in itertools.permutations(nums) if list(pp) != perm]
    real = sum("".join(letter_of[v] for v in pp).lower() in WORDS for pp in wrong)
    P.v("V3 wrong placements that still spell a word <= 5%", real / len(wrong) <= .05, f"{real}/{len(wrong)}")
    P["cv"] = dict(rate=1 - real / len(wrong), single_total=len(wrong), single_detected=len(wrong) - real)
    P["model"] = dict(truth=list(word), domains=[list(word)] * 5, check=letters_check(), perm=list(range(5)))
    P["mini"] = mini_ticks(5, 5, {(i, nums.index(truth[n])) for i, n in enumerate(names)})
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
    P["model"] = code_model(answers, table, 0, 100)
    P["mech_plain"] = "Code word (6 letters)"
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
    P = Page(no=7, title="The Queue", tier=2, topic="Ordinal numbers: 1st to 5th, before and behind",
             strand="Number and Algebra - Whole Numbers", syll="1.7 (ordinal numbers first to tenth)",
             ptype="Logic (queue)", mech="K1 shirt letters read 1st to 5th spell a word + K4 each child used once",
             instr=["The children stand in a queue.", "Read the clues.", "Write each name in its place.", "Then read the shirt letters."],
             mech_plain="Shirt letters read from 1st to 5th spell a word (5 letters)",
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
    P["model"] = dict(truth=list(word), domains=[list(word)] * 5, check=letters_check(), perm=list(range(5)))
    return P

PAGES = [page02, page03, page04, page05, page07]
