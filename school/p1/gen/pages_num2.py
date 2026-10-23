"""New number pages: N10 Stack It Up (P1-23), N04 Words and Numbers (P1-24), N05 Count the Crowd (P1-25), N06 Hundred Chart Patterns (P1-26),
and later N09 Bonds and Families (P1-37), N03 More or Fewer (P1-38)."""
import random, itertools, re
from .common import *
from . import art
from .art import row_svg, count_objs, NAMES as OBJN
from .pages_numbers import random_walk, count_routes, neighbours, maze_html
from .pages_stories import finish_code, plain_text, PEOPLE

# ---------------------------------------------------------------- N10 Stack It Up (P1-23)
def vsum_html(top, bot, op, ans, miss=None):
    """a written (stacked) sum. top and bot are 2-digit numbers; ans is the printed result or None (the pupil writes it in two boxes).
    miss = ('top'|'bot', 'o') puts a box where that number's ones digit would be."""
    def digs(n, hide):
        t, o = divmod(n, 10)
        return [f'<i class="d">{t}</i>', '<i class="ab"></i>' if hide else f'<i class="d">{o}</i>']
    r1 = ["<i></i>"] + digs(top, miss == "top")
    r2 = [f'<i class="d">{"+" if op == "+" else "&minus;"}</i>'] + digs(bot, miss == "bot")
    if ans is None: r3 = ["<i></i>", '<i class="ab"></i>', '<i class="ab"></i>']
    else: r3 = ["<i></i>"] + digs(ans, False)
    lab = '<div class="vlab"><span></span><span>tens</span><span>ones</span></div>'
    return '<div class="vs" data-op="%s">%s<div class="rule"></div>%s</div>' % (op, "".join(r1 + r2), "".join(r3)) + lab

def parse_vsum(h):
    """independent reader of a vsum: rows of digits (None for a box) -> (op, rows)"""
    op = re.search(r'data-op="(.)"', h).group(1)
    toks = re.findall(r'<i class="d">(\d|\+|&minus;)</i>|<i class="ab"></i>|<i></i>', h)
    cells = re.findall(r'(<i class="d">(\d|\+|&minus;)</i>|<i class="ab"></i>|<i></i>)', h)
    out = []
    for full, val in cells:
        if full == "<i></i>": out.append("-")
        elif "ab" in full: out.append(None)
        else: out.append(val)
    rows = [out[0:3], out[3:6], out[6:9]]
    return op, rows

def solve_vsum(h):
    """returns the number the pupil must write: the 2-digit result (when the result is boxed) or the single missing digit"""
    op, rows = parse_vsum(h)
    def num(r):
        t, o = r[1], r[2]
        return (None if t is None or o is None else int(t) * 10 + int(o)), (t, o)
    a, (at, ao) = num(rows[0]); b, (bt, bo) = num(rows[1]); c, (ct, co) = num(rows[2])
    sgn = 1 if op == "+" else -1
    if c is None: return a + b if op == "+" else a - b
    if a is None:
        miss_digit = (c - sgn * b) if op == "+" else (c + b)       # a + b = c  ->  a = c - b ;  a - b = c  ->  a = c + b
        a_val = miss_digit
        return a_val % 10
    if b is None:
        b_val = (c - a) if op == "+" else (a - c)
        return b_val % 10
    raise ValueError("nothing to find")

def page23():
    rng = random.Random(2303)
    word = "DONKEY"
    while True:
        items = []
        kinds = ["add", "add", "sub", "sub", "missadd", "misssub"]
        rng.shuffle(kinds)
        for k in kinds:
            if k in ("add", "missadd"):
                at, bt = rng.randint(1, 5), rng.randint(1, 4); ao = rng.randint(1, 6); bo = rng.randint(1, 9 - ao)
                a, b = at * 10 + ao, bt * 10 + bo
                items.append(dict(k=k, op="+", a=a, b=b, res=a + b))
            else:
                at, bt = rng.randint(4, 9), rng.randint(1, 3); ao = rng.randint(3, 9); bo = rng.randint(1, ao)
                a, b = at * 10 + ao, bt * 10 + bo
                items.append(dict(k=k, op="-", a=a, b=b, res=a - b))
        ans = []
        for it in items:
            if it["k"] in ("add", "sub"): ans.append(it["res"])
            elif it["k"] == "missadd": ans.append(it["a"] % 10)
            else: ans.append(it["a"] % 10)
        # a missing digit in the top number's ones place: the printed numbers are (a with box), b, res
        if len(set(ans)) != 6 or len({(it["a"], it["b"]) for it in items}) != 6: continue
        if any(a_ in (0,) for a_ in ans): continue
        table = make_code_table(ans, word, rng, 1, 100, n_decoy=5, near=(1, -1, 10, -10, 2, -2), tries=60)
        if table: break
    cards = []; htmls = []
    for i, it in enumerate(items):
        if it["k"] in ("add", "sub"): h = vsum_html(it["a"], it["b"], it["op"], None)
        else: h = vsum_html(it["a"], it["b"], it["op"], it["res"], miss="top")
        htmls.append(h)
        cards.append(f'<div class="vcard"><span class="no">{i+1}</span>{h}</div>')
    body = f'<div class="vsums">{"".join(cards)}</div>{code_block(table)}'
    P = Page(no=23, title="Stack It Up", tier=1, topic="Adding and subtracting tens and ones, written in boxes (within 100)",
             strand="Number and Algebra - Whole Numbers", syll="2.5, 2.6 (adding and subtracting within 100 using algorithms; tens and ones, no renaming)",
             ptype="Code-breaker (written sums)", mech="K1 code word (6 letters) + K7 put the number back",
             instr=["Add or take away.", "Write tens and ones in the boxes.", "Use the code table."],
             body=body, check="Write the letters in order. Do they spell a word?", check_boxes=6,
             key=dict(answers=", ".join(f"{i+1}) {it['a']} {it['op']} {it['b']} = {it['res']}" + ("" if it["k"] in ("add", "sub") else f" (missing digit {it['a'] % 10})") for i, it in enumerate(items)), check_result=f"Code word: {word}"),
             note=("Four written sums (two adding, two taking away) have two boxes for the answer, tens then ones. Two sums have the answer printed and a box for the ones of the top number, so the pupil must undo the sum. "
                   "All sums are within 100 and none needs renaming: the ones always add to 9 or less and a take-away never needs a borrow. "
                   "The syllabus lists algorithms (written methods) for adding and subtracting within 100 without giving a limit; the safe reading used here is no renaming."),
             seed=2303)
    solved = [solve_vsum(h) for h in htmls]
    P.v("V1 independent reader of the printed boxes solves every sum and equals the key", solved == ans, solved)
    P.v("V1b no renaming: ones digits of adding sums total 9 or less; taking away never needs a borrow", all((it["a"] % 10 + it["b"] % 10 <= 9) if it["op"] == "+" else (it["a"] % 10 >= it["b"] % 10) for it in items))
    P.v("V7 every number within 100", all(max(it["a"], it["b"], it["res"]) <= 99 for it in items))
    finish_code(P, ans, table, word, 1, 100)
    P["facts"] = "100"
    return P


# ---------------------------------------------------------------- N04 Words and Numbers (P1-24)
ONES_W = "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split()
TENS_W = {2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}
ORD_W = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]

def card_word(n):
    if n < 20: return ONES_W[n]
    t, o = divmod(n, 10)
    return TENS_W[t] + ("-" + ONES_W[o] if o else "")

def ord_sym(n):
    return f"{n}" + ("st" if n == 1 else "nd" if n == 2 else "rd" if n == 3 else "th")

def token_word(tok):  # printed word form
    k, v = tok
    return ORD_W[v - 1] if k == "o" else card_word(v)

def token_num(tok):   # printed numeral form
    k, v = tok
    return ord_sym(v) if k == "o" else str(v)

# the solver's own parsers (strings -> (kind, value)); they share nothing with the generator's printers
_W2N = {w: i for i, w in enumerate(ONES_W)}; _T2N = {w: t for t, w in TENS_W.items()}; _O2N = {w: i + 1 for i, w in enumerate(ORD_W)}
def parse_word(s):
    if s in _O2N: return ("o", _O2N[s])
    if s in _W2N: return ("c", _W2N[s])
    a, _, b = s.partition("-")
    return ("c", _T2N[a] * 10 + (_W2N[b] if b else 0))
def parse_num(s):
    m = re.fullmatch(r"(\d+)(st|nd|rd|th)", s)
    return ("o", int(m.group(1))) if m else ("c", int(s))

def confusers(tok):
    """what a careless pupil might match: the digits swapped, teen and ty mixed up, an ordinal with its plain number, or 10 more/less"""
    k, v = tok; out = set()
    if k == "o":
        out.add(("c", v)); out.add(("o", v + 1 if v < 10 else v - 1)); out.add(("o", v - 1 if v > 1 else v + 1))
    else:
        t, o = divmod(v, 10)
        if v > 10 and o and t: out.add(("c", o * 10 + t))
        if 13 <= v <= 19: out.add(("c", (v - 10) * 10))
        if v % 10 == 0 and 30 <= v <= 90: out.add(("c", v // 10 + 10))
        out.add(("c", v + 10 if v + 10 < 100 else v - 10)); out.add(("c", v - 1)); out.add(("c", v + 1))
        out.add(("o", v) if v <= 10 else ("c", v + 1))
    return {x for x in out if (x[0] == "c" and 1 <= x[1] <= 99) or (x[0] == "o" and 1 <= x[1] <= 10)}

def page24():
    rng = random.Random(2404)
    n = 4; L = 8
    card_vals = [v for v in range(11, 100) if v % 10 != 0 or v >= 20]
    for _ in range(20000):
        path = random_walk(rng, n, L)
        ordlinks = rng.sample(range(L - 1), 2)
        toks = []
        for k in range(L):
            toks.append(("o", rng.randint(1, 10)) if k in ordlinks else ("c", rng.choice(card_vals)))
        if len(set(toks)) < L: continue
        top = {}; bot = {}
        for k, c in enumerate(path):
            bot[c] = toks[k]
            if k > 0: top[c] = toks[k - 1]
        top[path[0]] = rng.choice([("c", rng.choice(card_vals)), ("o", rng.randint(1, 10))])
        bot[path[-1]] = rng.choice([("c", rng.choice(card_vals)), ("o", rng.randint(1, 10))])
        pool = sorted({x for t in toks for x in confusers(t)} - set(toks))
        for r in range(n):
            for c in range(n):
                if (r, c) in top and (r, c) in bot: continue
                if (r, c) not in top:
                    top[(r, c)] = rng.choice(pool) if rng.random() < .75 else rng.choice(sorted(set(toks)))
                if (r, c) not in bot:
                    bot[(r, c)] = rng.choice([("c", rng.choice(card_vals)), ("o", rng.randint(1, 10)), rng.choice(pool)])
        start, finish = path[0], path[-1]
        nxt = lambda cur, nb: bot[cur] == top[nb]
        if count_routes(lambda c: True, n, start, finish, nxt) != 1: continue
        # dead ends: legal steps from a route cell to an off-route cell
        dead = sum(1 for k, c in enumerate(path[:-1]) for nb in neighbours(*c, n) if nb not in path and nxt(c, nb))
        if not 2 <= dead <= 5: continue
        # a route cell that could be entered from a wrong route cell would shorten the line: the unique-route test above already excludes it
        break
    else: raise RuntimeError("n04")
    texts = [[f'<div class="dm"><span class="dw">{token_word(top[(r, c)])}</span><span class="dl"></span><span class="dn">{token_num(bot[(r, c)])}</span></div>' for c in range(n)] for r in range(n)]
    body = maze_html(n, texts, start, finish).replace('class="maze"', 'class="maze tall"')
    ords = [t for t in toks if t[0] == "o"]
    P = Page(no=24, title="Words and Numbers", tier=1, topic="Number words, numerals and ordinals",
             strand="Number and Algebra - Whole Numbers", syll="1.3, 1.7 (reading and writing numbers in numerals and in words; ordinal numbers and symbols)",
             ptype="Maze / path", mech="K6 route closes at FINISH through the stated number of boxes",
             instr=["Start at START.", "Go to the box saying your number.", "Move up, down, left or right."],
             mech_plain="Route: each step goes to a box whose top word says the number at the foot of the box you leave; the line must reach FINISH through the right number of boxes",
             body=body, check=f"Does your line reach FINISH? Count its boxes: are there {L}? Does each top word match?", check_boxes=None,
             key=dict(answers="Route (row, column from top-left): " + " -> ".join(f"({r+1},{c+1}) {token_word(top[(r, c)])} / {token_num(bot[(r, c)])}" for r, c in path), check_result=f"Route reaches FINISH through {L} boxes; every top word names the number at the foot of the box before it."),
             note=(f"A 4 by 4 grid. Each box has a number word on top and a numeral at the foot. From a box, the pupil moves to a touching box whose top word says the numeral at the foot of the box they are leaving. "
                   f"{len(ords)} of the {L - 1} steps are ordinals (a word such as {token_word(ords[0])} against its symbol {token_num(ords[0])}); the rest are numbers to 99 in words and numerals. "
                   f"Wrong turns are boxes that look right but are not: digits swapped (35 and fifty-three), teen and ty mixed up (13 and thirty), an ordinal against its plain number. {dead} wrong turns can be entered from the route and lead nowhere, so the box count and FINISH catch them."),
             seed=2404)
    # independent solver: parse the printed words and numerals back and count routes
    cells = {}
    for r in range(n):
        for c in range(n):
            m = re.search(r'class="dw">([^<]+)</span><span class="dl"></span><span class="dn">([^<]+)<', texts[r][c])
            cells[(r, c)] = (parse_word(m.group(1)), parse_num(m.group(2)))
    nxt2 = lambda cur, nb: cells[cur][1] == cells[nb][0]
    P.v("V1 exactly one route start->finish when every word and numeral is read back from the printed text (exhaustive DFS)", count_routes(lambda c: True, n, start, finish, nxt2) == 1)
    P.v("V1b the printed words and numerals mean what the generator meant (round trip for all 32 strings)", all(cells[c] == (top[c], bot[c]) for c in cells))
    P.v("V3 wrong turns exist (route boxes with a legal step to an off-route box)", dead >= 2, dead)
    P.v("V3b at least two ordinal steps and at least four number-word steps on the route", len(ords) >= 2 and L - 1 - len(ords) >= 4)
    P.v("V3c a shortcut that ignores the rule is shorter than the route, so the box count rejects it", abs(start[0]-finish[0]) + abs(start[1]-finish[1]) + 1 < L)
    P.v("V7 numbers within 99 and ordinals to 10th", all(1 <= t[1] <= (10 if t[0] == "o" else 99) for c in cells for t in cells[c]))
    P["cv"] = dict(rate=1.0, single_total=dead, single_detected=dead)
    P["route"] = path
    allcells = [(r, c) for r in range(n) for c in range(n)]
    def legal(rt):
        if len(rt) != L or len(set(rt)) != L or rt[0] != start or rt[-1] != finish: return False
        return all(abs(a[0]-b[0]) + abs(a[1]-b[1]) == 1 for a, b in zip(rt, rt[1:])) and all(cells[a][1] == cells[b][0] for a, b in zip(rt, rt[1:]))
    P["model"] = dict(truth=list(path), domains=[allcells] * L, check=legal, numeric=False)
    P["mini"] = mini_route(n, path)
    P["facts"] = "99 " + " ".join(str(v) for v in range(1, 100))
    return P


# ---------------------------------------------------------------- N05 Count the Crowd (P1-25)
def scene_svg(kind, n, rng, cols=5, rows=3, pitch=10.2, size=8.0):
    cells = rng.sample([(r, c) for r in range(rows) for c in range(cols)], n)
    inner = "".join(art.obj_g(kind, 1 + c * pitch + rng.uniform(-0.6, 0.6), 1 + r * (pitch - 1.2) + rng.uniform(-0.5, 0.5), size) for r, c in cells)
    return common_svg(cols * pitch + 1, rows * (pitch - 1.2) + 1.5, inner)

def common_svg(w, h, inner):
    from .common import svg
    return svg(round(w, 1), round(h, 1), inner)

def frame_svg(kind, k, pitch=9.0, size=7.4):
    """a ten frame (5 by 2, full of objects) and k loose objects below"""
    inner = '<rect class="frame" x="0.8" y="0.8" width="%.1f" height="%.1f" fill="#fff" stroke="#000" stroke-width="0.6"/>' % (5 * pitch, 2 * pitch)
    inner += '<line x1="0.8" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#000" stroke-width="0.35"/>' % (pitch + 0.8, 5 * pitch + 0.8, pitch + 0.8)
    for i in range(1, 5): inner += '<line x1="%.1f" y1="0.8" x2="%.1f" y2="%.1f" stroke="#000" stroke-width="0.35"/>' % (i * pitch + 0.8, i * pitch + 0.8, 2 * pitch + 0.8)
    for i in range(10): inner += art.obj_g(kind, 0.8 + (i % 5) * pitch + 0.8, 0.8 + (i // 5) * pitch + 0.8, size)
    for i in range(k): inner += art.obj_g(kind, 1 + i * (pitch - 1), 2 * pitch + 3.2, size)
    return common_svg(5 * pitch + 2, 2 * pitch + 3.2 + size + 1.5, inner)

def compare_svg(ka, a, kb, b, pitch=8.0, size=6.6, gap=11):
    top = "".join(art.obj_g(ka, 1 + i * pitch, 0.5, size) for i in range(a))
    bot = "".join(art.obj_g(kb, 1 + i * pitch, size + gap, size) for i in range(b))
    lines = "".join('<line class="mline" x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#000" stroke-width="0.4" stroke-dasharray="1 0.8"/>' % (1 + i * pitch + size / 2, size + 1.2, 1 + i * pitch + size / 2, size + gap - 0.6) for i in range(min(a, b)))
    return common_svg(max(a, b) * pitch + 1.5, 2 * size + gap + 1.5, top + bot + lines)

def solve_compare_svg(s, ka, kb, mode):
    objs = count_objs(s); a, b = objs.get(ka, 0), objs.get(kb, 0); m = s.count('class="mline"')
    assert m == min(a, b)
    return (a - m) if a >= b else (b - m)     # the unmatched objects: how many more (or fewer) than the shorter row

def page25():
    rng = random.Random(2505)
    word = "CLOTH"
    kinds = ["apple", "bird", "star", "fish", "balloon", "sweet", "flower", "ball", "car", "kite"]
    while True:
        k = rng.sample(kinds, 7)
        c1, c2 = rng.randint(6, 9), rng.randint(10, 12); fk = rng.randint(3, 8)
        a1, b1 = rng.randint(6, 10), rng.randint(2, 5); a2, b2 = rng.randint(5, 10), rng.randint(2, 4)
        d1, d2 = a1 - b1, a2 - b2
        ans = [c1, c2, 10 + fk, d1, d2]
        if len(set(ans)) != 5 or d1 == d2: continue
        table = make_code_table(ans, word, rng, 0, 20, n_decoy=5, near=(1, -1, 2, -2, 3, -3), tries=80)
        if table: break
    s1 = scene_svg(k[0], c1, rng); s2 = scene_svg(k[1], c2, rng); s3 = frame_svg(k[2], fk)
    cmp1 = compare_svg(k[3], a1, k[4], b1); cmp2 = compare_svg(k[5], a2, k[6], b2)
    n_ = lambda kd: OBJN[kd][1]
    def card(no, q, svg_, cls="cc"):
        return f'<div class="{cls}"><div class="ch"><span class="no">{no}</span><span class="cq">{q}</span><span class="ab"></span></div>{svg_}</div>'
    row1 = "".join([card(1, f"How many {n_(k[0])}?", s1), card(2, f"How many {n_(k[1])}?", s2), card(3, f"How many {n_(k[2])}?", s3)])
    q4 = f"How many more {n_(k[3])} than {n_(k[4])}?"
    q5 = f"How many fewer {n_(k[6])} than {n_(k[5])}?"
    row2 = card(4, q4, cmp1) + card(5, q5, cmp2)
    body = f'<div class="cc3">{row1}</div><div class="cc2">{row2}</div>{code_block(table)}'
    P = Page(no=25, title="Count the Crowd", tier=1, topic="Counting a set and comparing two sets",
             strand="Number and Algebra - Whole Numbers", syll="1.1, 1.4 (counting to tell the number of objects in a given set; comparing the number of objects in two sets)",
             ptype="Code-breaker (counting)", mech="K1 code word (5 letters)",
             instr=["Count each set.", "Match the pictures with lines.", "Use the code table."],
             body=body, check="Write the letters in order. Do they spell a word?", check_boxes=5,
             key=dict(answers=f"1) {c1}, 2) {c2}, 3) 10 + {fk} = {10 + fk}, 4) {a1} - {b1} = {d1} more, 5) {a2} - {b2} = {d2} fewer", check_result=f"Code word: {word}"),
             note=("Three counting items (the third is a full ten frame and some more) and two comparing items. In the comparing items every picture in the shorter row is joined by a line to one in the longer row; the pictures with no line are the answer to how many more or how many fewer. "
                   "Pictures are objects, never bare dots. Sets are 12 or fewer except the ten frame item, which has over 12."),
             seed=2505)
    solved = [sum(count_objs(s1).values()), sum(count_objs(s2).values()), sum(count_objs(s3).values()),
              solve_compare_svg(cmp1, k[3], k[4], "more"), solve_compare_svg(cmp2, k[5], k[6], "fewer")]
    P.v("V1 objects counted in the drawings (and unmatched objects in the two comparing pictures) equal the key", solved == ans, solved)
    P.v("V1b the questions name the sets the right way round (more than: the longer row first; fewer than: the shorter row first)", a1 > b1 and a2 > b2 and k[3] != k[4] and k[5] != k[6])
    P.v("V1c at most one set has more than 12 objects", sum(1 for x in solved[:3] if x > 12) <= 1)
    finish_code(P, ans, table, word, 0, 20, plain="Code word (5 letters)")
    return P


# ---------------------------------------------------------------- N06 Hundred Chart Patterns (P1-26)
def chart_html(base, blanks):
    cells = ""
    for r in range(5):
        for c in range(10):
            v = base + 10 * r + c
            cells += '<div class="hc ab"></div>' if (r, c) in blanks else f'<div class="hc">{v}</div>'
    return f'<div class="hchart">{cells}</div>'

def read_chart(h):
    """independent reader: the 50 cells as ints (None for a box)"""
    toks = re.findall(r'<div class="hc( ab)?">(\d*)</div>', h)
    return [None if a else int(v) for a, v in toks]

def table_html(vals, blanks):
    th = "".join(f"<th>Day {i+1}</th>" for i in range(len(vals)))
    td = "".join('<td><span class="ab"></span></td>' if i in blanks else f"<td>{v}</td>" for i, v in enumerate(vals))
    return f'<table class="dtable"><tr>{th}</tr><tr>{td}</tr></table>'

def page26():
    rng = random.Random(2606)
    word = "PEANUT"
    while True:
        base = rng.choice([1, 11, 21, 31, 41, 51])
        pos = rng.sample([(r, c) for r in range(1, 5) for c in range(1, 9)], 2)
        if abs(pos[0][0] - pos[1][0]) + abs(pos[0][1] - pos[1][1]) < 3: continue
        pos.sort()
        ans_chart = [base + 10 * r + c for r, c in pos]
        up_r, up_c = rng.randint(0, 3), rng.randint(0, 9); dn_r, dn_c = rng.randint(1, 4), rng.randint(0, 9)
        x = base + 10 * up_r + up_c; y = base + 10 * dn_r + dn_c
        if (up_r, up_c) in pos or (up_r + 1, up_c) in pos or (dn_r, dn_c) in pos or (dn_r - 1, dn_c) in pos: continue
        step = rng.choice([2, 3, 4, 5]); days = [step * (i + 1) for i in range(6)]
        tb = rng.sample([2, 3, 4, 5], 2); tb = sorted(tb)
        ans = ans_chart + [x + 10, y - 10] + [days[i] for i in tb]
        if len(set(ans)) != 6 or max(ans) > 100: continue
        table = make_code_table(ans, word, rng, 1, 100, n_decoy=5, near=(1, -1, 10, -10, 2, -2), tries=60)
        if table: break
    ch = chart_html(base, set(pos)); tb_html = table_html(days, set(tb))
    mq = (f'<div class="mq"><span class="mqi"><span class="no">3</span>10 more than {x} is <span class="ab"></span></span>'
          f'<span class="mqi"><span class="no">4</span>10 less than {y} is <span class="ab"></span></span></div>')
    body = (f'<div class="blk"><p class="lead">1 and 2: fill the empty boxes, reading order.</p>{ch}</div>{mq}'
            f'<div class="blk"><p class="lead">5 and 6: Mei gets sweets each day. Write the missing numbers.</p>{tb_html}</div>{code_block(table)}')
    P = Page(no=26, title="Chart Patterns", tier=2, topic="Number patterns on a chart: 10 more, 10 less, and a growing table",
             strand="Number and Algebra - Whole Numbers", syll="1.6, 1.2, 1.5 (patterns in number sequences; tens and ones; comparing and ordering numbers)",
             ptype="Code-breaker (chart and pattern)", mech="K1 code word (6 letters)",
             instr=["Use the chart and the table.", "Write the missing numbers.", "Use the code table."],
             body=body, check="Write the letters in order. Do they spell a word?", check_boxes=6,
             key=dict(answers=f"1) {ans[0]}, 2) {ans[1]}, 3) {ans[2]}, 4) {ans[3]}, 5) {ans[4]}, 6) {ans[5]}", check_result=f"Code word: {word}"),
             note=("A piece of a 100 chart with two boxes, two questions about 10 more and 10 less (one box down or up the chart), and a growing table: the sweets go up by "
                   f"{step} each day. The two table answers continue the pattern. The syllabus asks for patterns in number sequences; the chart makes the 10 more, 10 less pattern visible. "
                   "The plan drew this page as a hidden picture; a hidden picture can reject only about two thirds of wrong numbers, so it is a code word page to meet the 95% rule."),
             seed=2606)
    cells = read_chart(ch)
    def deduce(i):
        r, c = divmod(i, 10)
        cand = set()
        if c > 0 and cells[i - 1] is not None: cand.add(cells[i - 1] + 1)
        if r > 0 and cells[i - 10] is not None: cand.add(cells[i - 10] + 10)
        if c < 9 and cells[i + 1] is not None: cand.add(cells[i + 1] - 1)
        if r < 4 and cells[i + 10] is not None: cand.add(cells[i + 10] - 10)
        return cand
    blanks_i = [i for i, v in enumerate(cells) if v is None]
    got = [deduce(i) for i in blanks_i]
    solved = [next(iter(g)) for g in got]
    m = re.findall(r"10 more than (\d+) is.*?10 less than (\d+) is", plain_text(mq).replace("  ", " ") if False else mq, re.S)
    xm, ym = (int(v) for v in re.search(r"more than (\d+) is.*?less than (\d+) is", mq, re.S).groups())
    solved += [cells[cells.index(xm) + 10], cells[cells.index(ym) - 10]]
    vals = [int(v) if v else None for v in re.findall(r"<td>(\d*)", tb_html)]
    known = [v for v in vals if v is not None]; d_ = known[1] - known[0]
    solved += [vals[i - 1] if False else known[0] + d_ * i for i in tb]
    P.v("V1 independent reader: each box in the chart is deduced from its printed neighbours (all agree), 10 more and 10 less are read from the chart, the table continues its pattern; all equal the key", solved == ans and all(len(g) == 1 for g in got), solved)
    P.v("V1b the 10 more and 10 less answers are printed cells (not boxes), answers distinct and within 100", cells[cells.index(xm) + 10] is not None and cells[cells.index(ym) - 10] is not None and len(set(ans)) == 6 and max(ans) <= 100)
    finish_code(P, ans, table, word, 1, 100)
    P["facts"] = "100 " + " ".join(map(str, range(1, 101)))
    return P


# ---------------------------------------------------------------- N09 Bonds and Families (P1-37)
def bond_chain_svg(tiles, blank):
    """six part-whole tiles in a row. tiles[k] = (whole, left, right); blank[k] = 'l' or 'r' (that part is left empty for the pupil).
    The right part of a tile must match the left part of the next tile (= signs between), and the last right part must match the first left part (loop under the row)."""
    p = []; R = 5.4
    for k, (w, l, r) in enumerate(tiles):
        x = k * 30
        p.append(f'<line x1="{x+15}" y1="{6+R}" x2="{x+7}" y2="{19-R}" stroke="#000" stroke-width="0.5"/><line x1="{x+15}" y1="{6+R}" x2="{x+23}" y2="{19-R}" stroke="#000" stroke-width="0.5"/>')
        for cx, cy, v, role in ((x + 15, 6, w, "w"), (x + 7, 19, l, "l"), (x + 23, 19, r, "r")):
            isb = (role == blank[k])
            p.append(f'<circle class="pc{" blank" if isb else ""}" data-k="{k}" data-role="{role}" cx="{cx}" cy="{cy}" r="{R}" fill="#fff" stroke="#000" stroke-width="0.6"/>')
            if not isb: p.append(f'<text class="pn" data-k="{k}" data-role="{role}" x="{cx}" y="{cy}" text-anchor="middle" dominant-baseline="central" font-family="Fredoka" font-weight="600" font-size="6.2" fill="#000">{v}</text>')
        if k < 5: p.append(f'<line x1="{x+29}" y1="18" x2="{x+31}" y2="18" stroke="#000" stroke-width="0.7"/><line x1="{x+29}" y1="20" x2="{x+31}" y2="20" stroke="#000" stroke-width="0.7"/>')
    p.append('<path d="M172,24.6 L172,31 L8,31 L8,24.6" fill="none" stroke="#000" stroke-width="0.6"/><rect x="82" y="28.6" width="16" height="4.8" fill="#fff"/><text x="90" y="31" text-anchor="middle" dominant-baseline="central" font-family="Fredoka" font-weight="600" font-size="4.6" fill="#000">=</text>')
    return svg(180, 34, "".join(p))

def read_chain(svg_text):
    """independent reader: {(tile, role): printed number or None for an empty circle}"""
    vals = {}
    for m in re.finditer(r'class="pc( blank)?" data-k="(\d)" data-role="(\w)"', svg_text): vals[(int(m.group(2)), m.group(3))] = None
    for m in re.finditer(r'class="pn" data-k="(\d)" data-role="(\w)"[^>]*>(\d+)<', svg_text): vals[(int(m.group(1)), m.group(2))] = int(m.group(3))
    return vals

def solve_chain(vals):
    """fill each empty part from its tile (whole minus the other part), then test that every touching pair matches"""
    ans = []
    full = dict(vals)
    for k in range(6):
        for role, other in (("l", "r"), ("r", "l")):
            if vals[(k, role)] is None:
                full[(k, role)] = vals[(k, "w")] - vals[(k, other)]; ans.append(full[(k, role)])
    ok = all(full[(k, "r")] == full[((k + 1) % 6, "l")] for k in range(6))
    return ans, ok

def page37():
    rng = random.Random(3737)
    while True:
        x = [rng.randint(2, 10) for _ in range(6)]
        tiles = [(x[k] + x[(k + 1) % 6], x[k], x[(k + 1) % 6]) for k in range(6)]
        if any(t[0] > 20 for t in tiles) or len(set(x)) < 5: continue
        blank = [rng.choice("lr") for _ in range(6)]
        both = sum(1 for k in range(6) if blank[k] == "r" and blank[(k + 1) % 6] == "l")
        if both > 1: continue
        ans = [tiles[k][1] if blank[k] == "l" else tiles[k][2] for k in range(6)]
        break
    chain = bond_chain_svg(tiles, blank)
    body = (f'<div class="blk"><p class="lead">Each tile: the top number is the whole. The two below are its parts.</p>{chain}</div>'
            f'<div class="blk"><p class="lead">Write the numbers for the empty circles, tile 1 to tile 6.</p><div class="ansgrid2">'
            + "".join(f'<span class="lbx"><span class="ab"></span><small>tile {k+1}</small></span>' for k in range(6)) + '</div></div>')
    chk = ["Go round the loop. Do the numbers joined by = match?", "Do the six numbers you wrote fill the six empty circles?"]
    P = Page(no=37, title="Bonds and Families", tier=2, topic="Number bonds to 20: parts, wholes and the loop that closes",
             strand="Number and Algebra - Whole Numbers", syll="2.1, 2.2, 2.3 (concepts of addition and subtraction; use of +, - and =; relationship between addition and subtraction)",
             ptype="Chain loop (bond tiles)", mech="K8 the loop closes: every number joined by = matches",
             mech_plain="Loop: the number in an empty circle must match the circle it is joined to by =, all the way round and back to tile 1",
             instr=["Find the number in each empty circle.", "Touching circles joined by = match.", "Go round the loop."],
             body=body, check=" ".join(chk[:1]), check_lines=chk[:1], check_boxes=None,
             key=dict(answers="Empty circles: " + ", ".join(f"tile {k+1} {'left' if blank[k] == 'l' else 'right'} = {ans[k]}" for k in range(6)) + ". Tiles (whole = left + right): " + ", ".join(f"{t[0]} = {t[1]} + {t[2]}" for t in tiles), check_result="Every touching pair matches, all the way round."),
             note=("Six tiles, each a whole (the top circle) with two parts. One part of every tile is empty; the pupil finds it from the whole and the other part (adding up to the whole, or taking the part away from it). "
                   "The right part of a tile is the same number as the left part of the next tile, and the right part of the last tile is the first tile's left part. So every number the pupil writes is tested against a matching circle: a wrong number breaks the loop. "
                   "The syllabus asks for the relationship between addition and subtraction; the pupil uses it each time a part is found from the whole. The plan also had a list of pairs that make 10 and a second sentence for each tile: both were dropped because a self-check at 95% could not be made for them."),
             seed=3737)
    vals = read_chain(chain)
    got, ok = solve_chain({k: v for k, v in vals.items()})
    P.v("V1 independent reader: every empty circle is found from its tile (whole minus the other part) and the loop closes with those numbers", got == ans and ok, got)
    P.v("V1b every tile has exactly one empty part and all wholes are within 20", sum(v is None for v in vals.values()) == 6 and all(t[0] <= 20 for t in tiles))
    P.v("V1c at most one link has an empty circle on both sides", sum(1 for k in range(6) if blank[k] == "r" and blank[(k + 1) % 6] == "l") <= 1)
    full0 = {(k, role): tiles[k][i] for k in range(6) for i, role in enumerate("wlr")}
    def closes(a):
        f = dict(vals)
        j = 0
        for k in range(6):
            role = blank[k]; f[(k, role)] = a[k]
        return all(f[(k, "r")] == f[((k + 1) % 6, "l")] for k in range(6)) and all(f[(k, "l")] + f[(k, "r")] == f[(k, "w")] for k in range(6))
    P.v("V3 every single wrong value in one empty circle (0 to 20) breaks the loop", all(not closes([a if j != k else v for j, a in enumerate(ans)]) for k in range(6) for v in range(0, 21) if v != ans[k]))
    P["cv"] = dict(rate=1.0, single_total=6 * 20, single_detected=6 * 20)
    P["model"] = dict(truth=list(ans), domains=[list(range(0, 21))] * 6, check=closes, numeric=True)
    P["facts"] = "20"
    return P

# ---------------------------------------------------------------- N03 More or Fewer (P1-38)
def _more_ok(val, c, chosen):
    k = c[0]
    if k == "none": return c[1] not in chosen
    if k == "more": return val[c[1]] - val[c[2]] == c[3]
    if k == "fewer": return val[c[2]] - val[c[1]] == c[3]
    if k == "equal": return val[c[1]] - c[3] == val[c[2]] + c[3]
    if k == "gt": return val[c[1]] > val[c[2]]

def more_text(c):
    return {"none": f"Nobody has {c[1]}.", "more": f"{c[1]} has {c[3]} more than {c[2]}.", "fewer": f"{c[1]} has {c[3]} fewer than {c[2]}.",
            "equal": f"{c[1]} gives {c[2]} {c[3]}: the same.", "gt": f"{c[1]} has more than {c[2]}."}[c[0]]

def solve_more(names, nums, clues):
    sols = []
    for perm in itertools.permutations(nums, len(names)):
        val = dict(zip(names, perm)); chosen = set(perm)
        if all(_more_ok(val, c, chosen) for c in clues): sols.append(val)
    return sols

def page38():
    from .pages_numbers import grid_table, howto_grid
    rng = random.Random(3838)
    names = ["Ali", "Mei", "Siti", "Ben", "Kumar"]
    word = "GLORY"
    assert anagrams(word) == [word.lower()]
    while True:
        nums = sorted(rng.sample(range(2, 21), 6))
        unused = nums[rng.choice([1, 2, 3])]
        used = [n for n in nums if n != unused]
        perm = used[:]; rng.shuffle(perm); truth = dict(zip(names, perm))
        cl = [("none", unused)]
        pool = []
        for a in names:
            for b in names:
                if a == b: continue
                d = truth[a] - truth[b]
                if d > 0: pool += [("more", a, b, d), ("fewer", b, a, d)]
                if d > 0 and d % 2 == 0: pool.append(("equal", a, b, d // 2))
        rng.shuffle(pool)
        for c in pool:
            if len(cl) >= 7: break
            if any(c[:3] == x[:3] for x in cl): continue
            cl.append(c)
        if len(solve_more(names, nums, cl)) != 1: continue
        for c in cl[1:]:
            rest = [x for x in cl if x != c]
            if len(solve_more(names, nums, rest)) == 1: cl = rest
        kinds = {c[0] for c in cl}
        if len(cl) < 5 or not {"more", "fewer"} <= kinds or "equal" not in kinds: continue
        break
    decoy = max(decoy_options(word), key=lambda d: (len(small_words(word + d)), rng.random()))
    letter_of = {truth[n]: word[i] for i, n in enumerate(names)}; letter_of[unused] = decoy
    chips = "".join(f'<span class="chip">{n} <i class="cl">{letter_of[n]}</i></span>' for n in nums)
    clues = "".join(f"<li>{more_text(c)}</li>" for c in cl)
    ans = ('<div class="ansgrid"><span></span><b>number</b><b>letter</b>' + "".join(f'<span class="nm">{n}</span><span class="ab"></span><span class="ab"></span>' for n in names) + '</div>')
    body = (f'<div class="blk"><p class="lead">Six amounts of stickers. Five children.</p><div class="chips six">{chips}</div></div>'
            f'<div class="twocol"><ul class="clues">{clues}</ul>{howto_grid()}</div>'
            f'<div class="twocol"><div>{grid_table(names, nums)}</div><div>{ans}</div></div>')
    real = sorted({"".join(letter_of[v] for v in pp) for pp in itertools.permutations(nums, 5) if list(pp) != perm and "".join(letter_of[v] for v in pp).lower() in BIG})
    n_wrong = len(list(itertools.permutations(nums, 5))) - 1
    P = Page(no=38, title="More or Fewer", tier=2, topic="Comparing amounts: more than, fewer than and making the same",
             strand="Number and Algebra - Whole Numbers", syll="1.4, 2.1 (comparing the number of objects in sets; concepts of addition and subtraction; make equal and fewer than: problem solving)",
             ptype="Logic grid", mech="K4 grid + K1 letter beside each amount spells a word (5 letters, one decoy letter)",
             mech_plain="Letters beside the amounts, read down the list, spell a word (5 letters; one of the six amounts is not used)",
             instr=["Read the clues.", "Use the grid to cross and tick.", "Write each amount, then its letter."],
             body=body, check="Read the five letters down your list. Do they spell a word?", check_boxes=5,
             key=dict(answers=", ".join(f"{n}: {truth[n]} ({letter_of[truth[n]]})" for n in names) + f"; nobody has {unused} (letter {decoy} is the decoy)", check_result=f"Letters down the list: {word}"),
             note=("Six amounts are listed but there are only five children: a clue says which amount nobody has, and its letter is a decoy that is not part of the word. The clues are exact (a number more than, a number fewer than) and one clue says what a child gives so that two children have the same. "
                   "The five letters of the word have exactly one arrangement that is a word, so no wrong placement spells a word: every wrong way to give five children five of the six amounts was tested against a very large word list. "
                   "A fewer than clue is the other way round from a more than clue, so the pupil must read who has the greater amount. The page shows a worked example of crosses and ticks."),
             seed=3838)
    sols = solve_more(names, nums, cl)
    P.v("V1 exactly one assignment satisfies all clues (the clue texts evaluated by brute force over 720 ways)", len(sols) == 1 and sols[0] == truth, len(sols))
    P.v("V1b every clue needed", all(len(solve_more(names, nums, [x for x in cl if x != c])) > 1 for c in cl))
    P.v("V1c the clues include more than, fewer than (the reversed one) and a give-to-make-the-same clue", {"more", "fewer", "equal"} <= {c[0] for c in cl})
    P.v("V2 letters beside the amounts, in name order, spell " + word, "".join(letter_of[truth[n]] for n in names) == word)
    P.v("V3d the code word's letters have exactly ONE arrangement that is a word", anagrams(word) == [word.lower()], anagrams(word))
    P.v(f"V3 none of the {n_wrong} wrong placements (5 of the 6 amounts) spells a word (large word list)", not real, real[:3])
    P.v("V4 guess resistance: six letters shown, one is a decoy, and at least 3 shorter common words can be spelt from them", len(small_words(word + decoy)) >= 3, small_words(word + decoy)[:6])
    P["cv"] = dict(rate=1.0, single_total=n_wrong, single_detected=n_wrong)
    P["model"] = dict(truth=list(word), domains=[sorted(set(letter_of.values()))] * 5, check=letters_check(), perm=list(range(5)))
    P["mini"] = mini_ticks(5, 6, {(i, nums.index(truth[n])) for i, n in enumerate(names)})
    return P

PAGES = [page23, page24, page25, page26, page37, page38]
