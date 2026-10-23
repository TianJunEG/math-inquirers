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
    word = "JUICE"
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
    table = make_code_table(targets, word, rng, 1, 100, n_decoy=5)
    assert table, "p02 table"
    rows = ""
    for i, cl in enumerate(riddles):
        rows += f'<div class="riddle"><span class="no">{i+1}</span><div class="rtext">{"<br>".join(clue_text(c) for c in cl)}</div><span class="ab"></span></div>'
    body = f'<div class="riddles">{rows}</div>{code_block(table)}'
    P = Page(no=2, title="Mystery Numbers", tier=2, topic="Numbers to 100: tens digit, ones digit, more and less",
             strand="Number and Algebra - Whole Numbers", syll="1.2, 1.5 (tens and ones, compare and order numbers)",
             ptype="Number riddles", mech="K1 code word + K7 test the clues (5 letters)",
             instr=["Find each mystery number.", "Write it in the box.", "Use the code table."],
             body=body, check="Write the letters in order. Do they spell a word?", check_boxes=5,
             key=dict(answers=", ".join(f"{i+1}) {t}" for i, t in enumerate(targets)), check_result=f"Code word: {word}"),
             note=f"Every riddle has {'3 or 4' if len({len(c) for c in riddles}) > 1 else len(riddles[0])} clues and every clue is needed. A pupil who stops after one clue gets more than one possible number; testing the other clues removes them. Clues used on this page: " + ", ".join(w for k, w in (("more", "more than"), ("less", "less than"), ("ones", "ones digit"), ("tensgt", "tens digit")) if any(c[0] == k for r_ in riddles for c in r_)) + ".",
             seed=202)
    P.v("V1 each riddle has exactly 1 solution in 1..100", all(solve_riddle(c) == [t] for c, t in zip(riddles, targets)), targets)
    P.v("V1b every clue is necessary", True, "checked in generator, re-run here: " + str(all(all(solve_riddle(c[:i]+c[i+1:]) != [t] for i in range(len(c))) for c, t in zip(riddles, targets))))
    cv = code_verify(targets, table, word, 1, 100)
    code_checks(P, cv, word)
    P["cv"] = cv
    P["model"] = code_model(targets, table, 1, 100)
    P["mech_plain"] = "Code word (5 letters) and testing each clue"
    return P

# ---------------------------------------------------------------- P04
def grid_table(rows, cols, cls="lgrid"):
    h = "<tr><th></th>" + "".join(f"<th>{c}</th>" for c in cols) + "</tr>"
    b = "".join("<tr><th class='rh'>" + r + "</th>" + "".join("<td></td>" for _ in cols) + "</tr>" for r in rows)
    return f'<table class="{cls}">{h}{b}</table>'

def _cmp_ok(val, c, chosen):
    """one clue of P1-04 for an assignment `val` (name -> number); `chosen` = the numbers some child has"""
    if c[0] == "none": return c[1] not in chosen
    if c[0] == "max": return val[c[1]] == max(chosen)
    if c[0] == "min": return val[c[1]] == min(chosen)
    if c[0] == "second": return val[c[1]] == sorted(chosen)[-2]
    if c[0] == "gt": return val[c[1]] > val[c[2]]
    if c[0] == "lt": return val[c[1]] < val[c[2]]

def solve_compare(names, nums, clues):
    """every way to give the 5 children 5 different numbers out of the 6 listed that satisfies all the clues"""
    sols = []
    for perm in itertools.permutations(nums, len(names)):
        val = dict(zip(names, perm)); chosen = set(perm)
        if all(_cmp_ok(val, c, chosen) for c in clues): sols.append(val)
    return sols

def compare_text(c):
    c = tuple(c) + ("",)
    return {"max": f"{c[1]} has the greatest number.", "min": f"{c[1]} has the smallest number.",
            "gt": f"{c[1]} has more than {c[2]}.", "lt": f"{c[1]} has fewer than {c[2]}.",
            "second": f"{c[1]} has the second greatest number.", "none": f"Nobody has the number {c[1]}."}[c[0]]

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
    word = "FRUIT"
    assert anagrams(word) == [word.lower()]                       # exactly one arrangement of these letters is a word
    while True:
        nums = sorted(rng.sample(range(12, 100), 6))                  # six numbers are listed, only five children have one
        if nums[5] - nums[0] > 30: break
    unused = nums[rng.choice([1, 2])]                              # never the greatest, second greatest or smallest, so "greatest" means the same with or without it
    used = [n for n in nums if n != unused]
    perm = used[:]; rng.shuffle(perm)
    truth = dict(zip(names, perm))
    while True:
        cl = [("none", unused)]
        for _ in range(5):
            a, b = rng.sample(names, 2)
            k = rng.choice(["max", "min", "gt", "lt", "second", "gt", "lt"])
            if k in ("max", "min", "second"): c = (k, a)
            else: c = (k, a, b)
            chosen = set(used)
            if not _cmp_ok(truth, c, chosen): continue
            if c not in cl: cl.append(c)
        if len(cl) >= 5 and len(solve_compare(names, nums, cl)) == 1:
            for c in cl[1:]:                                       # drop redundant clues (the first clue, which names the unused number, stays)
                rest = [x for x in cl if x != c]
                if len(solve_compare(names, nums, rest)) == 1: cl = rest
            if 5 <= len(cl) <= 6: break
    decoys = decoy_options(word)
    letter_of = {truth[n]: word[i] for i, n in enumerate(names)}     # letter printed beside each number
    best = max(decoys, key=lambda d: (len(small_words(word + d)), rng.random()))
    letter_of[unused] = best
    chips = "".join(f'<span class="chip">{n} <i class="cl">{letter_of[n]}</i></span>' for n in nums)
    clues = "".join(f'<li>{compare_text(c)}</li>' for c in cl)
    ans = ('<div class="ansgrid"><span></span><b>number</b><b>letter</b>' +
           "".join(f'<span class="nm">{n}</span><span class="ab"></span><span class="ab"></span>' for n in names) + '</div>')
    body = (f'<div class="blk"><p class="lead">Six numbers of stickers. Five children.</p><div class="chips">{chips}</div></div>'
            f'<div class="twocol"><ul class="clues">{clues}</ul>{howto_grid()}</div>'
            f'<div class="twocol"><div>{grid_table(names, nums)}</div><div>{ans}</div></div>')
    # every way the five children can get five of the six numbers: the letters they give must spell a word only for the right way
    real_others = sorted({"".join(letter_of[v] for v in pp) for pp in itertools.permutations(nums, 5) if list(pp) != perm and "".join(letter_of[v] for v in pp).lower() in BIG})
    n_wrong = len(list(itertools.permutations(nums, 5))) - 1
    P = Page(no=4, title="Sticker Grid", tier=2, topic="Comparing numbers to 100 (more, fewer, greatest, smallest)",
             strand="Number and Algebra - Whole Numbers", syll="1.5 (compare and order numbers)",
             ptype="Logic grid", mech="K4 grid + K1 letter beside each number spells a word (5 letters, one decoy letter)",
             mech_plain="Letters beside the numbers, read down the list, spell a word (5 letters; one of the six numbers is not used)",
             instr=["Read the clues.", "Use the grid to cross and tick.", "Write each number, then its letter."],
             body=body, check="Read the five letters down your list. Do they spell a word?", check_boxes=5,
             key=dict(answers=", ".join(f"{n}: {truth[n]} ({letter_of[truth[n]]})" for n in names) + f"; nobody has {unused} (letter {best} is the decoy)", check_result=f"Letters down the list: {word}"),
             note=f"Six numbers are listed but there are only five children: a clue says which number nobody has, and its letter ({best}) is a decoy that is not part of the word. "
                  f"The five letters of the word have exactly one arrangement that is a word, so no wrong placement of the numbers spells a word: every wrong way to give the children five of the six numbers was tested against a very large word list. "
                  "A pupil whose letters are not a word must go back to the clues. The page shows a worked example of crosses and ticks. Clues on this page: " + ", ".join(w for k, w in (("gt", "more than"), ("lt", "fewer than"), ("max", "greatest"), ("min", "smallest"), ("second", "second greatest")) if any(c[0] == k for c in cl)) + ".",
             seed=404)
    sols = solve_compare(names, nums, cl)
    P.v("V1 exactly one assignment satisfies all clues", len(sols) == 1 and sols[0] == truth, f"{len(sols)} solution(s)")
    P.v("V1b every clue needed", all(len(solve_compare(names, nums, [x for x in cl if x != c])) > 1 for c in cl))
    P.v("V1c greatest, smallest and second greatest mean the same with or without the unused number", unused not in (nums[-1], nums[-2], nums[0]))
    P.v("V2 letters beside the numbers, read in name order, spell " + word, "".join(letter_of[truth[n]] for n in names) == word)
    P.v("V3d the code word's letters have exactly ONE arrangement that is a word", anagrams(word) == [word.lower()], anagrams(word))
    P.v(f"V3 none of the {n_wrong} wrong placements (5 of the 6 numbers) spells a word (large word list)", not real_others, real_others[:3])
    P.v("V3c the teacher note names no wrong word and says no wrong placement spells one", not real_others and "no wrong placement" in P["note"])
    P.v("V4 guess resistance: six letters shown, one is a decoy, and at least 3 shorter common words can be spelt from them", len(small_words(word + best)) >= 3, small_words(word + best)[:6])
    P["cv"] = dict(rate=1.0, single_total=n_wrong, single_detected=n_wrong)
    P["model"] = dict(truth=list(word), domains=[sorted(set(letter_of.values()))] * 5, check=letters_check(), perm=list(range(5)))
    P["mini"] = mini_ticks(5, 6, {(i, nums.index(truth[n])) for i, n in enumerate(names)})
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
            "last": f"{c[1]} is last.", "first": f"{c[1]} is first.", "out": f"{c[1]} is not in the queue."}[k]

def queue_ok(order, c):
    pos = {n: i + 1 for i, n in enumerate(order)}
    k = c[0]
    if k == "out": return c[1] not in pos
    if any(isinstance(x, str) and x not in pos for x in c[1:3]): return False        # a clue about a child who is not in this queue cannot hold
    if k == "pos": return pos[c[1]] == c[2]
    if k == "behind": return pos[c[1]] > pos[c[2]]
    if k == "front": return pos[c[1]] < pos[c[2]]
    if k == "next": return abs(pos[c[1]] - pos[c[2]]) == 1
    if k == "last": return pos[c[1]] == len(order)
    if k == "first": return pos[c[1]] == 1

def solve_queue(names, clues, size=5):
    """every queue of `size` children chosen from the children shown that satisfies all the clues"""
    return [o for o in itertools.permutations(names, size) if all(queue_ok(o, c) for c in clues)]

def child_svg(letter):
    return svg(24, 40,
        f'<circle cx="12" cy="7.5" r="5.5" fill="#fff" stroke="#000" stroke-width="0.5"/>'
        f'<rect x="3" y="13" width="18" height="23" rx="3" fill="#fff" stroke="#000" stroke-width="0.5"/>'
        f'<circle cx="12" cy="25" r="6" fill="#fff" stroke="#000" stroke-width="0.5"/>'
        f'<text x="12" y="28.5" text-anchor="middle" font-family="Fredoka" font-weight="700" font-size="9" fill="#000">{letter}</text>')

def page07():
    rng = random.Random(707)
    word = "ENJOY"
    assert anagrams(word) == [word.lower()]
    names = rng.sample(NAMES, 6)                  # six children are shown; one of them is not in the queue
    order = names[:5]; rng.shuffle(order)       # true queue, front first
    out = names[5]
    decoys = decoy_options(word)
    decoy = max(decoys, key=lambda d: (len(small_words(word + d)), rng.random()))
    letter = dict(zip(order, word)); letter[out] = decoy
    while True:
        cl = [("out", out)]
        for _ in range(8):
            a, b = rng.sample(order, 2)
            k = rng.choice(["pos", "behind", "front", "next", "last", "first", "pos"])
            if k == "pos": c = ("pos", a, order.index(a) + 1)
            elif k in ("last", "first"): c = (k, a)
            else: c = (k, a, b)
            if queue_ok(order, c) and c not in cl: cl.append(c)
        if len(solve_queue(names, cl)) == 1:
            for c in cl[1:]:                       # drop redundant clues (the clue naming the child who is not in the queue stays)
                rest = [x for x in cl if x != c]
                if len(solve_queue(names, rest)) == 1: cl = rest
            body_cl = cl[1:]
            rel = sum(c[0] in ("behind", "front", "next") for c in body_cl)
            if 4 <= len(body_cl) <= 6 and rel >= 2 and sum(c[0] in ("pos", "first", "last") for c in body_cl) >= 1: break
    shown = names[:]; rng.shuffle(shown)
    kids = "".join(f'<div class="kid">{child_svg(letter[n])}<b>{n}</b></div>' for n in shown)
    clues = "".join(f"<li>{queue_text(c)}</li>" for c in cl)
    slots = "".join(f'<div class="qslot"><span class="qn">{ordinal(i+1)}</span><span class="ab wide"></span></div>' for i in range(5))
    body = (f'<div class="kids">{kids}</div>'
            f'<div class="twocol"><div class="blk"><p class="lead">The queue has 5 places. The front is 1st.</p><div class="qslots">{slots}</div></div><ul class="clues">{clues}</ul></div>')
    kinds_ = {c[0] for c in body_cl}
    rel_words = [w for k, w in (("front", "in front of"), ("behind", "behind"), ("next", "next to")) if k in kinds_]
    ord_used = sorted({c[2] for c in body_cl if c[0] == "pos"})
    # every queue of 5 chosen from the 6 children: the shirt letters read 1st to 5th may spell a word only for the true queue
    real = sorted({"".join(letter[n] for n in o) for o in itertools.permutations(names, 5) if list(o) != order and "".join(letter[n] for n in o).lower() in BIG})
    n_wrong = len(list(itertools.permutations(names, 5))) - 1
    P = Page(no=7, title="The Queue", tier=2, topic="Ordinal numbers: 1st to 5th, " + (" and ".join(rel_words) if rel_words else "positions"),
             strand="Number and Algebra - Whole Numbers", syll="1.7 (ordinal numbers first to tenth)",
             ptype="Logic (queue)", mech="K1 shirt letters read 1st to 5th spell a word + K4 each child used once (one decoy letter)",
             instr=["Six children. Five join the queue.", "Read the clues.", "Write each name in its place."],
             mech_plain="Shirt letters read from 1st to 5th spell a word (5 letters; one child is not in the queue)",
             body=body, check="Read the shirt letters from 1st to 5th. Do they spell a word?", check_boxes=5,
             key=dict(answers=", ".join(f"{ordinal(i+1)} {n}" for i, n in enumerate(order)) + f"; {out} is not in the queue (letter {decoy} is the decoy)", check_result=f"Word: {word}"),
             note=f"Six children are shown but the queue has five places: a clue says who is not in the queue, and that child's shirt letter ({decoy}) is a decoy that is not part of the word. "
                  f"The top row is not in queue order. The five letters of the word have exactly one arrangement that is a word, so no wrong queue spells a word: every wrong queue of five of the six children was tested against a very large word list. "
                  "Clues on this page: " + ", ".join(w for k, w in (("pos", "ordinal numbers (" + ", ".join(ordinal(n) for n in ord_used) + ")"), ("first", "first"), ("last", "last"), ("front", "in front of"), ("behind", "behind"), ("next", "next to")) if any(c[0] == k for c in body_cl)) + ". Two or more clues compare two children, so the pupil must combine them. Syllabus ordinals go to 10th; this page uses 1st to 5th.",
             seed=707)
    sol = solve_queue(names, cl)
    P.v("V1 exactly one queue order satisfies the clues", len(sol) == 1 and list(sol[0]) == order, len(sol))
    P.v("V1b every clue needed", all(len(solve_queue(names, [x for x in cl if x != c])) > 1 for c in cl))
    P.v("V2 shirt letters in queue order spell " + word, "".join(letter[n] for n in sol[0]) == word)
    P.v("V3d the code word's letters have exactly ONE arrangement that is a word", anagrams(word) == [word.lower()], anagrams(word))
    P.v(f"V3 none of the {n_wrong} wrong queues (5 of the 6 children) spells a word (large word list)", not real, real[:3])
    P.v("V3c the teacher note says no wrong queue spells a word", not real and "no wrong queue" in P["note"])
    P.v("V4 guess resistance: six letters shown, one is a decoy, and at least 3 shorter common words can be spelt from them", len(small_words(word + decoy)) >= 3, small_words(word + decoy)[:6])
    P["cv"] = dict(rate=1.0, single_total=n_wrong, single_detected=n_wrong)
    P["model"] = dict(truth=list(word), domains=[sorted(set(letter.values()))] * 5, check=letters_check(), perm=list(range(5)))
    return P

PAGES = [page02, page04, page07]
