"""Semester 1, pages P3-01 to P3-05: numbers to 10 000.
P3-01 Thousands, Hundreds, Tens, Ones; P3-02 Words and Numbers (route); P3-03 Digit Cards; P3-04 Compare and Order; P3-05 Number Patterns (lettered choice)."""
import random, re, itertools
from .common import *
from .kit import *
from .p3kit import *
from . import art3 as A3

# =============================================================================== P3-01 Thousands, Hundreds, Tens, Ones
def page01():
    rng = random.Random(3101)
    for _ in range(4000):
        c1 = (rng.randint(1, 4), rng.randint(1, 4), rng.randint(1, 4), rng.randint(1, 4))
        c2 = (rng.randint(2, 4), 0, rng.randint(1, 4), rng.randint(1, 4)) if rng.random() < .5 else (rng.randint(2, 4), rng.randint(1, 4), 0, rng.randint(1, 4))
        n = rng.choice([x for x in range(1200, 9900) if len(set(str(x))) == 4 and "0" not in str(x)])
        d = int(rng.choice(str(n)))
        reg = (rng.randint(2, 6), rng.randint(11, 15), rng.randint(1, 8))          # thousands, hundreds (more than 9), ones
        zero = (rng.randint(2, 9), rng.randint(1, 9))                              # thousands and tens
        hn = rng.choice([x for x in range(1200, 9700, 100)])
        items = [dict(k="chart", c=c1), dict(k="chart", c=c2), dict(k="digit", n=n, d=d), dict(k="regroup", th=reg[0], h=reg[1], o=reg[2]),
                 dict(k="zero", th=zero[0], t=zero[1]), dict(k="hundreds", n=hn)]
        rng.shuffle(items)
        def val(it):
            return {"chart": lambda i: 1000 * i["c"][0] + 100 * i["c"][1] + 10 * i["c"][2] + i["c"][3], "digit": lambda i: i["d"] * 10 ** (3 - str(i["n"]).index(str(i["d"]))),
                    "regroup": lambda i: 1000 * i["th"] + 100 * i["h"] + i["o"], "zero": lambda i: 1000 * i["th"] + 10 * i["t"], "hundreds": lambda i: i["n"] // 100}[it["k"]](it)
        ans = [val(it) for it in items]
        if not distinct(ans) or max(ans) > 9999: continue
        pool = set()
        for it, a in zip(items, ans):
            if it["k"] in ("chart", "regroup", "zero"):
                s = str(a).zfill(4)
                for p in itertools.permutations(s):
                    if p[0] != "0": pool.add(int("".join(p)))
            if it["k"] == "digit": pool |= {it["d"], it["d"] * 10, it["d"] * 100, it["d"] * 1000, it["n"]}
            if it["k"] == "regroup": pool |= {1000 * it["th"] + 100 * it["h"] % 1000 + it["o"], int(f"{it['th']}{it['h']}{it['o']}")}
            if it["k"] == "zero": pool |= {1000 * it["th"] + 100 * it["t"], 100 * it["th"] + it["t"], int(f"{it['th']}{it['t']}")}
            if it["k"] == "hundreds": pool |= {it["n"], it["n"] // 10, it["n"] // 1000}
        pool = sorted(p for p in pool if p not in ans and 0 <= p <= 9999)
        res = find_table(1, 6, ans, rng, 0, 9999, pool, n_decoy=3, tries=30)
        if res: word, table = res; break
    cards = []; texts = []; charts = []
    for i, it in enumerate(items):
        if it["k"] == "chart":
            s = A3.pv4_chart(*it["c"]); charts.append(s)
            cards.append(qcard(i + 1, s, '<span class="ab w4"></span>', cls="inl span2"))
        else:
            if it["k"] == "digit": t = f"In {it['n']}, what is the value of the digit {it['d']}?"
            elif it["k"] == "regroup": t = f"{it['th']} thousands, {it['h']} hundreds and {it['o']} ones make which number?"
            elif it["k"] == "zero": t = f"{it['th']} thousands and {it['t']} tens make which number?"
            else: t = f"How many hundreds are in {it['n']}?"
            texts.append(t); cards.append(qcard(i + 1, f"<p>{t}</p>", '<span class="ab w4"></span>'))
    P = code_items_page(1, 3101, "Thousands, Hundreds, Tens, Ones", 1, "Place value: numbers to 10 000", STRAND_WN,
        "1.1, 1.2 (counting in hundreds; number notation, representations and place values)", ["WN1.1", "WN1.2"], "Code-breaker (place value)",
        ["Look at each item.", "Write the number in the box.", INSTR_CODE],
        '<div class="qg c2">' + "".join(cards) + "</div>", ans, table, word, 0, 9999,
        "; ".join(f"{i+1}) {a}" for i, a in enumerate(ans)),
        "Two place-value charts (discs marked 1000, 100, 10 and 1; one chart has a column with no discs), the value of a digit, a regrouped number (more than 9 hundreds), a number with a zero hundreds place and the number of hundreds in a number. The wrong numbers a pupil gets by writing the digits in a different order, or the digit instead of its value, have decoy letters in the table or no letter. A box left blank gives no letter and the check cannot see it.")
    solved = []; ci = 0; ti = 0
    for it in items:
        if it["k"] == "chart":
            th, h, t, o = A3.read_pv4(charts[ci]); ci += 1; solved.append(1000 * th + 100 * h + 10 * t + o)
        else:
            tx = texts[ti]; ti += 1
            m = re.match(r"In (\d+), what is the value of the digit (\d)\?", tx)
            if m: solved.append(int(m.group(2)) * 10 ** (len(m.group(1)) - 1 - m.group(1).index(m.group(2)))); continue
            m = re.match(r"(\d) thousands, (\d+) hundreds and (\d+) ones", tx)
            if m: a_, b_, c_ = map(int, m.groups()); solved.append(1000 * a_ + 100 * b_ + c_); continue
            m = re.match(r"(\d) thousands and (\d) tens", tx)
            if m: a_, b_ = map(int, m.groups()); solved.append(1000 * a_ + 10 * b_); continue
            m = re.match(r"How many hundreds are in (\d+)\?", tx)
            solved.append(int(m.group(1)) // 100)
    P.v("V1 independent solver (discs counted in the drawing, printed words read back) equals the key", solved == ans, solved)
    P.v("V7 every answer is below 10 000", all(0 < a < 10000 for a in ans))
    P.v("V1b the digit asked about appears once in its number", all(str(it["n"]).count(str(it["d"])) == 1 for it in items if it["k"] == "digit"))
    P.v("V1c at most 4 discs in a chart column", all(max(it["c"]) <= 4 for it in items if it["k"] == "chart"))
    P["key"]["answers"] = "; ".join(
        (f"{i+1}) {it['c'][0]} thousands {it['c'][1]} hundreds {it['c'][2]} tens {it['c'][3]} ones = {a}" if it["k"] == "chart" else f"{i+1}) {a}") for i, (it, a) in enumerate(zip(items, ans)))
    return P

# =============================================================================== P3-02 Words and Numbers (route)
ONES_W = "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split()
TENS_W = {2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}

def below100(r):
    return ONES_W[r] if r < 20 else TENS_W[r // 10] + ("-" + ONES_W[r % 10] if r % 10 else "")

def words4(n):
    th, r = divmod(n, 1000); h, r2 = divmod(r, 100)
    parts = [ONES_W[th] + " thousand"]
    if h: parts.append(ONES_W[h] + " hundred")
    if r2: parts.append("and " + below100(r2))
    return " ".join(parts)

_W2N = {w: i for i, w in enumerate(ONES_W)}; _T2N = {w: t for t, w in TENS_W.items()}
def parse_words4(s):
    """the solver's own parser: 'four thousand two hundred and six' -> 4206 (shares nothing with words4)"""
    toks = s.replace("-", " ").split(); v = 0; cur = 0
    for t in toks:
        if t == "and": continue
        if t == "thousand": v += cur * 1000; cur = 0
        elif t == "hundred": cur *= 100
        elif t in _T2N: cur += _T2N[t] * 10
        else: cur += _W2N[t]
    return v + cur

def confusers4(n):
    """what a careless pupil might match: two digits swapped, teen and ty mixed up, a zero moved or dropped, one digit different by 1"""
    s = str(n); out = set()
    for i in range(3):
        l = list(s); l[i], l[i + 1] = l[i + 1], l[i]; out.add(int("".join(l)))
    t, o = int(s[2]), int(s[3])
    if s[2] == "1" and o >= 3: out.add(int(s[:2] + str(o) + "0"))
    if t >= 3 and o == 0: out.add(int(s[:2] + "1" + str(t)))
    if s[1] == "0": out.add(int(s[0] + s[2:] + "0"))
    if s[2] == "0" and o: out.add(int(s[:2] + str(o) + "0"))
    out |= {n + 10, n - 10, n + 100, n - 100, n + 1000 if n < 9000 else n - 1000}
    return {x for x in out if 1000 <= x <= 9999 and x != n}

def page02():
    rng = random.Random(3202)
    n = 4; L = 8
    vals = [v for v in range(1001, 10000) if v % 1000 != 0]
    for _ in range(60000):
        path = random_walk(rng, n, L)
        toks = [rng.choice(vals) for _ in range(L)]
        if len(set(toks)) < L: continue
        top = {}; bot = {}
        for k, c in enumerate(path):
            bot[c] = toks[k]
            if k > 0: top[c] = toks[k - 1]
        top[path[0]] = rng.choice(vals); bot[path[-1]] = rng.choice(vals)
        pool = sorted({x for t in toks for x in confusers4(t)} - set(toks))
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
    else: raise RuntimeError("p02")
    texts = [[f'<div class="dm"><span class="dw">{words4(top[(r, c)])}</span><span class="dl"></span><span class="dn">{bot[(r, c)]}</span></div>' for c in range(n)] for r in range(n)]
    body = maze_html(n, texts, start, finish)
    P = new_page(2, 3202, "Words and Numbers", 1, "Reading and writing numbers in words and in numerals", STRAND_WN,
        "1.3 (reading and writing numbers in numerals and in words)", ["WN1.3"], "Maze / path", "K6 route closes at FINISH through the stated number of boxes",
        ["Start at START. Move up, down, left or right.", "Go to the box with the words for the number at the foot of your box.", "Do not step on a box twice."],
        body, "Route (row, column from top-left): " + " -> ".join(f"({r+1},{c+1}) {words4(top[(r, c)])} / {bot[(r, c)]}" for r, c in path),
        f"Route reaches FINISH through {L} boxes; every top word names the number at the foot of the box before it.",
        f"A 4 by 4 grid. Each box has a number in words on top and a numeral at the foot. From a box the pupil moves to a touching box whose top words say the numeral at the foot of the box being left. All numbers are 4-digit. Wrong turns are boxes that look right but are not: digits swapped, teen and ty mixed up, a zero in the wrong place, a hundred or a thousand more or less. Sometimes two touching boxes have the same words on top, so the pupil may meet two choices; only one leads on to FINISH. {dead} wrong turns can be entered from the route and lead nowhere, so the box count and the words matter. Pupils read numbers in words and match them with numerals; writing number words by hand is not checked by this page.",
        check=f"Does your line reach FINISH? Count its boxes: are there {L}? Does each top word match?", mk=("route",),
        mech_plain="Route: each step goes to a box whose top words say the numeral at the foot of the box you leave; the line must reach FINISH through the right number of boxes")
    cells = {}
    for r in range(n):
        for c in range(n):
            m = re.search(r'class="dw">(.*?)</span><span class="dl"></span><span class="dn">(\d+)<', texts[r][c])
            cells[(r, c)] = (parse_words4(m.group(1)), int(m.group(2)))
    nxt2 = lambda cur, nb: cells[cur][1] == cells[nb][0]
    P.v("V1 exactly one route start->finish when every word and numeral is read back from the printed text (exhaustive search)", count_routes(lambda c: True, n, start, finish, nxt2) == 1)
    P.v("V1b the printed words mean what the generator meant (round trip for all 32 strings)", all(cells[c] == (top[c], bot[c]) for c in cells))
    P.v("V3 wrong turns exist (route boxes with a legal step to an off-route box)", dead >= 2, dead)
    P.v("V3c a shortcut that ignores the rule is shorter than the route, so the box count rejects it", abs(start[0]-finish[0]) + abs(start[1]-finish[1]) + 1 < L)
    P.v("V7 all numbers are 4-digit", all(1000 <= x <= 9999 for c in cells for x in cells[c]))
    P["cv"] = dict(rate=1.0, single_total=dead, single_detected=dead)
    allcells = [(r, c) for r in range(n) for c in range(n)]
    def legal(rt):
        if len(rt) != L or len(set(rt)) != L or rt[0] != start or rt[-1] != finish: return False
        return all(abs(a[0]-b[0]) + abs(a[1]-b[1]) == 1 for a, b in zip(rt, rt[1:])) and all(cells[a][1] == cells[b][0] for a, b in zip(rt, rt[1:]))
    P["model"] = dict(truth=list(path), domains=[allcells] * L, check=legal, numeric=False)
    P["mini"] = mini_route(n, path)
    P["facts"] = "9999 " + " ".join(str(v) for v in range(1000, 10000)[:0])
    return P

# =============================================================================== P3-03 Digit Cards
QTXT = {"greatest": "Make the greatest number.", "smallest": "Make the smallest number.", "greatest even": "Make the greatest even number.",
        "smallest odd": "Make the smallest odd number.", "smallest even": "Make the smallest even number.", "greatest odd": "Make the greatest odd number."}

def best_numbers(cards, kind):
    perms = sorted({int("".join(map(str, p))) for p in itertools.permutations(cards) if p[0] != 0})
    if kind == "greatest": return perms[-1]
    if kind == "smallest": return perms[0]
    if kind == "greatest even": return max(x for x in perms if x % 2 == 0)
    if kind == "smallest even": return min(x for x in perms if x % 2 == 0)
    if kind == "greatest odd": return max(x for x in perms if x % 2 == 1)
    if kind == "smallest odd": return min(x for x in perms if x % 2 == 1)
    raise ValueError(kind)

def page03():
    rng = random.Random(3303)
    kinds = ["greatest", "smallest", "greatest even", "smallest odd", "smallest even", "greatest odd"]
    for _ in range(4000):
        rng.shuffle(kinds); items = []
        for kd in kinds:
            for _t in range(200):
                cards = rng.sample(range(10), 4)
                if cards.count(0) > 1: continue
                if "even" in kd and not any(c % 2 == 0 for c in cards if True): continue
                if "odd" in kd and not any(c % 2 == 1 for c in cards): continue
                try: best_numbers(cards, kd)
                except ValueError: continue
                except Exception: continue
                break
            items.append((kd, cards))
        try: ans = [best_numbers(c, k) for k, c in items]
        except Exception: continue
        if not distinct(ans): continue
        if sum(1 for k, c in items if 0 in c) < 2: continue
        pool = set()
        for k, c in items:
            pool |= {int("".join(map(str, p))) for p in itertools.permutations(c) if p[0] != 0}
        pool = sorted(x for x in pool if x not in ans)
        res = find_table(3, 6, ans, rng, 1000, 9999, pool, n_decoy=3, tries=30)
        if res: word, table = res; break
    cards_h = []
    for i, (kd, cs) in enumerate(items):
        dc = '<div class="dcards">' + "".join(f'<span class="dcard">{c}</span>' for c in cs) + '</div>'
        cards_h.append(qcard(i + 1, dc + f"<p>{QTXT[kd]}</p>", '<span class="ab w4"></span>'))
    P = code_items_page(3, 3303, "Digit Cards", 2, "Numbers to 10 000: make, compare and order numbers from digit cards", STRAND_WN,
        "1.2, 1.4 (place values; comparing and ordering numbers)", ["WN1.2", "WN1.4"], "Code-breaker (digit cards)",
        ["Use all four cards once each.", "Make a 4-digit number. A number cannot start with 0.", INSTR_CODE],
        qgrid(cards_h, 3), ans, table, word, 1000, 9999,
        "; ".join(f"{i+1}) {k}: {a}" for i, ((k, c), a) in enumerate(zip(items, ans))),
        "Six sets of four digit cards: greatest, smallest, greatest even, smallest even, greatest odd and smallest odd. A zero card cannot be the thousands digit. The decoy letters stand for the other arrangements of the same cards, so a pupil who makes a different number from the same cards still gets a letter, but not the right one. A box left blank gives no letter and the check cannot see it.")
    solved = []
    for h in cards_h:
        digs_ = [int(x) for x in re.findall(r'class="dcard">(\d)<', h)]
        q = re.search(r"Make the ([a-z ]+) number", h).group(1)
        solved.append(best_numbers(digs_, q))
    P.v("V1 independent solver (every arrangement of the printed cards tried) equals the key", solved == ans, solved)
    P.v("V1b cards in one item are all different digits", all(len(set(c)) == 4 for k, c in items))
    P.v("V7 answers are 4-digit numbers", all(1000 <= a <= 9999 for a in ans))
    return P

# =============================================================================== P3-04 Compare and Order
def page04():
    rng = random.Random(3404)
    for _ in range(4000):
        word = word_candidates(4, 6)[0]
        base = rng.sample(range(1, 10), 4)
        permA = set()
        while len(permA) < 3:
            p = base[:]; rng.shuffle(p); permA.add(int("".join(map(str, p))))
        A_ = sorted(permA)                      # smallest first
        # B: greatest first; one 3-digit number, two 4-digit numbers close together
        big = rng.randint(2000, 9000); near = big + rng.choice([-90, -9, 9, 90, 900, -900])
        small3 = rng.randint(900, 999)
        B_ = sorted({big, near, small3}, reverse=True)
        if len(B_) < 3 or len({abs(a - b) for a in A_ for b in A_ if a != b}) < 2: continue
        if not all(1000 <= a <= 9999 for a in A_): continue
        break
    CLAIMED[4] = word
    cards = [("A", v) for v in A_] + [("B", v) for v in B_]
    lab = {c: word[i] for i, c in enumerate(cards)}
    shA = A_[:]; shB = B_[:]; rng.shuffle(shA); rng.shuffle(shB)
    def card_html(grp, v):
        return f'<div class="fcard"><div class="fnum"><span class="bignum">{v}</span></div><i class="cl">{lab[(grp, v)]}</i></div>'
    body = (f'<div class="blk"><p class="lead">Set A: smallest first.</p><div class="fcards">{"".join(card_html("A", v) for v in shA)}</div></div>'
            f'<div class="blk"><p class="lead">Set B: greatest first.</p><div class="fcards">{"".join(card_html("B", v) for v in shB)}</div></div>'
            f'<div class="blk"><p class="lead">Write the letters in order: Set A, then Set B.</p><div class="ansgrid2" style="margin-top:2mm">' + "".join('<span class="ab"></span>' for _ in range(6)) + '</div></div>')
    P = new_page(4, 3404, "Compare and Order", 2, "Numbers to 10 000: comparing and ordering", STRAND_WN,
        "1.4 (comparing and ordering numbers)", ["WN1.4"], "Ordering (lettered cards)", "K1 letters in order spell a word (6 letters) + K4 each card used once",
        ["Put each set of numbers in order.", "Write the letter of each card in its place.", "Set A: smallest first. Set B: greatest first."],
        body, "Set A (smallest first): " + ", ".join(f"{lab[('A', v)]} = {v}" for v in A_) + "; Set B (greatest first): " + ", ".join(f"{lab[('B', v)]} = {v}" for v in B_), f"Word: {word}",
        "Set A has three 4-digit numbers made from the same four digits, so the pupil must compare place by place from the thousands. Set B has two 4-digit numbers that differ in one digit and one 3-digit number, which is the smallest although its digits look large. The letters, read in the order asked, spell a word with exactly one arrangement that is a word, so no wrong order of the six cards spells a word (every wrong order was tested against a very large word list). A box left blank gives no letter and the check cannot see it.",
        check="Read the six letters in order. Do they spell a word?", check_boxes=None, mk=("logic",),
        mech_plain="Letters of the cards in the order asked spell a word (6 letters)")
    P["check_boxes"] = None
    secA, secB = body.split("Set B: greatest first.")
    a_cards = re.findall(r'<span class="bignum">(\d+)</span></div><i class="cl">(\w)</i>', secA); b_cards = re.findall(r'<span class="bignum">(\d+)</span></div><i class="cl">(\w)</i>', secB)
    solved = "".join(c[1] for c in sorted(a_cards, key=lambda c: int(c[0])) + sorted(b_cards, key=lambda c: -int(c[0])))
    P.v("V1 independent solver (numbers read back and sorted by value) gets the word", solved == word, solved)
    P.v("V1b every number has the digits asked: Set A made from the same four digits, Set B two 4-digit and one 3-digit number", len({tuple(sorted(c[0])) for c in a_cards}) == 1 and sorted(len(c[0]) for c in b_cards) == [3, 4, 4])
    P.v("V3d the code word's letters have exactly ONE arrangement that is a word", anagrams(word) == [word.lower()], anagrams(word))
    bad_orders = sorted(w for w in ("".join(p) for p in itertools.permutations(word)) if w != word and w.lower() in BIG)
    P.v("V3 none of the 719 wrong orders of the six letters spells a word", not bad_orders, bad_orders[:3])
    P["cv"] = dict(rate=1.0, single_total=719, single_detected=719)
    P["model"] = dict(truth=list(word), domains=[sorted(set(word))] * 6, check=letters_check(), perm=list(range(6)))
    return P

# =============================================================================== P3-05 Number Patterns (lettered choice)
def seq_text(cells):
    return '<div class="seq">' + "".join(('<span class="sqm">?</span>' if c is None else f'<span class="sq">{N(c)}</span>') for c in cells) + '</div>'

def read_seq(q):
    return [None if m == "?" else int(m.replace("\u00a0", "")) for m in re.findall(r'<span class="sq[m]?">([^<]*)</span>', q)]

def missing_of(cells):
    """independent solver: the missing number of a printed sequence of 5 cells, one constant step or two steps that take turns"""
    j = cells.index(None)
    steps = {i: cells[i + 1] - cells[i] for i in range(len(cells) - 1) if cells[i] is not None and cells[i + 1] is not None}
    if len(set(steps.values())) == 1:
        d = next(iter(steps.values()))
        return cells[j - 1] + d if j > 0 else cells[1] - d
    par = {}
    for i, d in steps.items(): par.setdefault(i % 2, set()).add(d)
    assert all(len(v) == 1 for v in par.values()) and len(par) == 2, steps
    d_of = lambda i: next(iter(par[i % 2]))
    return cells[j - 1] + d_of(j - 1) if j > 0 else cells[1] - d_of(0)

def page05():
    rng = random.Random(3505)
    specs = [("up", 100), ("down", 1000), ("up", 1000), ("alt", (100, 10)), ("down", 100), ("alt", (200, 20))]
    for _ in range(3000):
        rows = []
        order = specs[:]; rng.shuffle(order)
        for kind, st in order:
            for _t in range(300):
                if kind == "alt":
                    a, b = st
                    s0 = rng.randrange(1000, 5000, 10); seq = [s0]
                    for i in range(4): seq.append(seq[-1] + (a if i % 2 == 0 else b))
                elif kind == "up":
                    s0 = rng.randrange(1000, 5000, 100) + (rng.choice([0, 500, 250]) if st == 1000 else 0)
                    seq = [s0 + st * i for i in range(5)]
                else:
                    s0 = rng.randrange(6000, 9900, 100) if st == 100 else rng.randint(6, 9) * 1000 + rng.choice([0, 500, 300])
                    seq = [s0 - st * i for i in range(5)]
                if min(seq) >= 1000 and max(seq) <= 9999: break
            gap = rng.choice([2, 3, 4])
            rows.append(dict(kind=kind, st=st, seq=seq, gap=gap))
        ans = [r["seq"][r["gap"]] for r in rows]
        if not distinct(ans): continue
        if len({r["gap"] for r in rows}) < 3: continue
        break
    specs_rows = []
    for r in rows:
        right = r["seq"][r["gap"]]
        wrongs = {right + 10, right - 10, right + 100, right - 100, right + 1000, right - 1000, right + 1, right - 1}
        if r["kind"] == "alt":
            a, b = r["st"]; wrongs |= {right + (a - b), right - (a - b)}
        wrongs = sorted(w for w in wrongs if 1000 <= w <= 9999 and w != right and w not in r["seq"])
        w2 = rng.sample(wrongs, 2)
        cells = [None if i == r["gap"] else v for i, v in enumerate(r["seq"])]
        specs_rows.append(dict(q=seq_text(cells), opts=[f'<b class="on">{N(right)}</b>'] + [f'<b class="on">{N(w)}</b>' for w in w2], right=right))
    P = lettered_choice_page(5, 3505, "Number Patterns", 2, "Number patterns: counting in hundreds and thousands, two-step patterns", STRAND_WN,
        "1.1, 1.5 (counting in hundreds and thousands; patterns in number sequences)", ["WN1.1", "WN1.5"], "Lettered choice (patterns)",
        ["Find the rule. Find the missing number.", "Circle the letter beside the missing number.", "Write the six letters in the boxes."],
        specs_rows, 3, "; ".join(f"{i+1}) {r['right']}" for i, r in enumerate(specs_rows)),
        "Six number patterns with one missing number: counting on and back in 100s and 1000s, and two patterns whose two steps take turns. Each row offers three numbers; the wrong ones are the usual slips (the wrong place changed, or the wrong step). The letters of the right numbers, read down the rows, spell the word. Every other way of choosing was tested against a very large word list: none spells a word. A box left blank gives no letter and the check cannot see it.",
        rng=rng)
    def solver(q, opts):
        v = missing_of(read_seq(q))
        return [int(re.search(r">([^<]*)<", o).group(1).replace("\u00a0", "")) for o in opts].index(v)
    got = solve_letters(solver, P["body"])
    P.v("V1 independent solver (the printed pattern read back, its rule found, each option tried) gets the word", got == P["word"], got)
    P.v("V1b exactly one option of every row continues the pattern", all(sum(1 for o in opts if int(re.search(r">([^<]*)<", o[0]).group(1)) == missing_of(read_seq(q))) == 1 for q, opts in read_choice_rows(P["body"])))
    P.v("V7 numbers are 4-digit and below 10 000", all(1000 <= r["right"] <= 9999 for r in specs_rows))
    return P

PAGES = [page01, page02, page03, page04, page05]
