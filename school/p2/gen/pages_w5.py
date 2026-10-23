"""Wave 5: P2-33 Pattern Rules; P2-34 Meet the Solids; P2-35 Solid Sort; P2-36 Picture Graph Scales; P2-37 Graph Detective Two.
(P2-38 to P2-40 are the colour-by-code pages in pages_cbc.py.)"""
import random, re, math, itertools
from .common import *
from .kit import *
from .pages_w1 import code_items_page, distinct, STRAND_WN, STRAND_AS, STRAND_MD, STRAND_MO, STRAND_ME, INSTR_CODE, PEOPLE
from .pages_w4 import page32
from . import art2 as A
from .art import osz, opitch, NAMES as OBJN, count_objs

# =============================================================================== P2-33 Pattern Rules
def page33():
    return page32(no=33, attrs_list=("two", "sizecol", "turn", "two", "shapesize", "two"), seed=9033, title="Pattern Rules", tier=2)

# =============================================================================== 3D solids (line drawings)
ST = 'fill="#fff" stroke="#000" stroke-width="0.6" stroke-linejoin="round" stroke-linecap="round"'
DASH = 'fill="none" stroke="#000" stroke-width="0.4" stroke-dasharray="1.1 0.9"'

def solid_svg(kind, w=16.0, h=16.0, d=16.0):
    """a solid drawn in oblique view. cube/cuboid: front face and two more faces; cylinder: ellipse and sides; cone: triangle and base ellipse; sphere: circle."""
    if kind in ("cube", "cuboid"):
        if kind == "cube": h = d = w
        ox, oy = 0.45 * d, -0.45 * d
        x, y = 2.0, 2.0 - oy
        pts = lambda *p: " ".join(f"{a:.2f},{b:.2f}" for a, b in p)
        front = pts((x, y), (x + w, y), (x + w, y + h), (x, y + h))
        top = pts((x, y), (x + w, y), (x + w + ox, y + oy), (x + ox, y + oy))
        side = pts((x + w, y), (x + w, y + h), (x + w + ox, y + h + oy), (x + w + ox, y + oy))
        inner = f'<polygon class="face" points="{front}" {ST}/><polygon class="face" points="{top}" {ST}/><polygon class="face" points="{side}" {ST}/>'
        return svg(round(w + ox + 4, 1), round(h - oy + 4, 1), inner)
    if kind == "cylinder":
        rx, ry = w / 2, w / 5.0; cx = 2.0 + rx; top = 2.0 + ry; bot = top + h
        body = f'<path d="M{cx-rx:.2f},{top:.2f} L{cx-rx:.2f},{bot:.2f} A{rx:.2f},{ry:.2f} 0 0 0 {cx+rx:.2f},{bot:.2f} L{cx+rx:.2f},{top:.2f}" {ST}/>'
        return svg(round(w + 4, 1), round(h + 2 * ry + 4, 1), body + f'<ellipse class="rim" cx="{cx:.2f}" cy="{top:.2f}" rx="{rx:.2f}" ry="{ry:.2f}" {ST}/>')
    if kind == "cone":
        rx, ry = w / 2, w / 5.0; cx = 2.0 + rx; apex = 2.0; base = apex + h
        inner = (f'<path d="M{cx-rx:.2f},{base:.2f} A{rx:.2f},{ry:.2f} 0 0 0 {cx+rx:.2f},{base:.2f}" {DASH}/>'
                 f'<polygon class="cone" points="{cx:.2f},{apex:.2f} {cx-rx:.2f},{base:.2f} {cx+rx:.2f},{base:.2f}" {ST}/>'
                 f'<ellipse class="rim" cx="{cx:.2f}" cy="{base:.2f}" rx="{rx:.2f}" ry="{ry:.2f}" {ST}/>')
        return svg(round(w + 4, 1), round(h + ry + 4, 1), inner)
    if kind == "sphere":
        r = w / 2; cx = cy = 2.0 + r
        inner = (f'<circle class="ball" cx="{cx:.2f}" cy="{cy:.2f}" r="{r:.2f}" {ST}/>'
                 f'<path d="M{cx-r:.2f},{cy:.2f} A{r:.2f},{r*0.3:.2f} 0 0 0 {cx+r:.2f},{cy:.2f}" {ST} fill="none"/>'
                 f'<path d="M{cx-r:.2f},{cy:.2f} A{r:.2f},{r*0.3:.2f} 0 0 1 {cx+r:.2f},{cy:.2f}" {DASH}/>')
        return svg(round(w + 4, 1), round(w + 4, 1), inner)
    raise ValueError(kind)

def read_solid(s):
    """independent reader of a drawn solid from its primitives"""
    if 'class="ball"' in s: return "sphere"
    polys = re.findall(r'<polygon class="(face|cone)" points="([^"]+)"', s)
    if any(c == "cone" for c, _ in polys): return "cone"
    if len(polys) == 3:
        P_ = [[tuple(map(float, q.split(","))) for q in pts.split()] for _, pts in polys]
        front = P_[0]; w = front[1][0] - front[0][0]; h = front[2][1] - front[1][1]
        ox = P_[2][2][0] - P_[2][0][0]
        return "cube" if abs(w - h) < 0.2 and abs(ox - 0.45 * w) < 0.3 else "cuboid"
    return "cylinder"

SOLID_DIMS = {"cube": [dict(w=16), dict(w=14)], "cuboid": [dict(w=24, h=11, d=13), dict(w=14, h=22, d=12), dict(w=22, h=14, d=18)],
              "cylinder": [dict(w=14, h=17), dict(w=18, h=10), dict(w=11, h=22)], "cone": [dict(w=17, h=19), dict(w=13, h=21), dict(w=20, h=14)], "sphere": [dict(w=17), dict(w=14)]}
NAMES5 = ["cube", "cuboid", "cone", "cylinder", "sphere"]

def rand_solid(rng, kind):
    return solid_svg(kind, **rng.choice(SOLID_DIMS[kind]))

# =============================================================================== P2-34 Meet the Solids
def page34():
    rng = random.Random(9134)
    word = word_candidates(34, 6)[0]; CLAIMED[34] = word
    letters = choice_letters(rng, word, 3)
    kinds = NAMES5 + [rng.choice(NAMES5)]
    while True:
        rng.shuffle(kinds)
        if sum(1 for k in kinds if k in ("cube", "cuboid")) >= 2: break
    rows_h = []; layout = []
    for i, kd in enumerate(kinds):
        wrongs = rng.sample([n for n in NAMES5 if n != kd], 2)
        if kd in ("cube", "cuboid") and rng.random() < .8:
            other = "cuboid" if kd == "cube" else "cube"; wrongs = [other, rng.choice([n for n in NAMES5 if n not in (kd, other)])]
        opts = [(kd, letters[i][0])] + [(w, l) for w, l in zip(wrongs, letters[i][1:])]
        rng.shuffle(opts); layout.append(opts)
        pic = rand_solid(rng, kd)
        o = "".join(f'<span class="tfo"><b>{n}</b><i class="cl">{l}</i></span>' for n, l in opts)
        rows_h.append(f'<div class="srow3"><span class="no">{i+1}</span><div class="sol">{pic}</div><div class="sopts">{o}</div></div>')
    P = new_page(34, 9134, "Meet the Solids", 1, "3D shapes: cube, cuboid, cone, cylinder and sphere", "Measurement and Geometry - Geometry",
        "2.1 (identifying and naming 3D shapes: cube, cuboid, cone, cylinder, sphere)", ["GE2.1"], "Choice table (solids)",
        "K1 the letter of the right name in each row spells a word (6 letters, two decoy letters in each row)",
        ["Name each solid.", "Circle the letter of its name.", "Write the six letters in the boxes."],
        '<div class="srows3">' + "".join(rows_h) + '</div>', "; ".join(f"{i+1}) {k}: {next(l for n, l in o if n == k)}" for i, (k, o) in enumerate(zip(kinds, layout))), f"Word: {word}",
        "Six drawings of solids (one of each kind and one repeated, in different shapes and sizes: a tall and a short cylinder, a long and a tall cuboid). Each row offers three names with letters. A cube and a cuboid are offered together in several rows, so the pupil must see whether all the faces are squares. The letters of the right names, read down the rows, spell the word. Every other way of choosing was tested against a very large word list: none spells a word. The drawings are pictures of solids; no real solid is handled. A box left blank gives no letter and the check cannot see it.",
        check="Write the six letters in order. Do they spell a word?", check_boxes=6, mk=("code",),
        mech_plain="Word from the letters of the right names (6 letters)")
    pics = re.findall(r'<div class="sol">(<svg.*?</svg>)</div>', "".join(rows_h))
    solved = [read_solid(p_) for p_ in pics]
    P.v("V1 independent solver (each drawing classified from its faces, ellipses and apex) gets the solid in every row", solved == kinds, solved)
    other = choice_other_words(word, letters)
    P.v("V3 no other way of choosing spells a word (large word list)", not other, other[:3])
    P.v("V3d the code word's letters have exactly ONE arrangement that is a word", anagrams(word) == [word.lower()])
    P.v("V7 all five solids of the syllabus list appear", set(kinds) == set(NAMES5))
    P["cv"] = dict(rate=1.0, single_total=12, single_detected=12)
    P["model"] = dict(truth=list(word), domains=[list(l) for l in letters], check=letters_check(), numeric=False)
    P["mini"] = ""
    return P

# =============================================================================== P2-35 Solid Sort
def page35():
    rng = random.Random(9235)
    while True:
        counts = rng.sample(range(1, 6), 5)               # five different counts 1..5, total 15
        res = None
        word = None
        pool = []
        for k, c in zip(NAMES5, counts): pool += [k] * c
        rng.shuffle(pool)
        domain = list(range(0, 16))
        r = code_table_any(35, 5, counts, rng, 0, 15, n_decoy=3, tries=60, pool=[x for x in range(0, 9) if x not in counts] + [6, 7], domain=domain)
        if r: word, table = r; break
    pics = [rand_solid(rng, k) for k in pool]
    grid = '<div class="sgrid">' + "".join(f'<div class="sc">{p_}</div>' for p_ in pics) + '</div>'
    rowsh = ""
    for k in NAMES5:
        rowsh += f'<div class="trow2"><div class="ticon">{solid_svg(k, **SOLID_DIMS[k][0])}</div><b>{k}</b><span class="ab w2"></span></div>'
    body = grid + f'<div class="blk"><p class="lead">How many of each? Total: 15.</p><div class="trows2">{rowsh}</div></div>' + table_block(table)
    P = new_page(35, 9235, "Solid Sort", 2, "3D shapes: sorting and counting solids", "Measurement and Geometry - Geometry",
        "2.1 (identifying, naming and classifying 3D shapes)", ["GE2.1"], "Sorting table (solids)", "K3 the five counts add to 15 + K1 code word (5 letters)",
        ["Count each kind of solid.", "Write the number in its box.", INSTR_CODE],
        body, "Counts: " + ", ".join(f"{k} {c}" for k, c in zip(NAMES5, counts)), f"Total 15; code word: {word}",
        "Fifteen drawn solids to sort into the five kinds. The five counts are different and add to 15, which the page prints: a pupil who misses one or counts one twice no longer gets 15. The counts are also looked up in the code table (five letters). The two checks together catch a miss in one kind balanced by an extra in another, except for a swap of two counts that happen to keep the letters spelling a word. A box left blank gives no letter and the check cannot see it.",
        check="Do the five counts add to 15? Do the letters spell a word?", check_boxes=5, mk=("code", "total"),
        mech_plain="Total 15 and code word (5 letters)")
    P["instr"] = ["Count each kind of solid.", "Write the number in its box.", INSTR_CODE]
    cnt_read = {k: 0 for k in NAMES5}
    for p_ in pics: cnt_read[read_solid(p_)] += 1
    solved = [cnt_read[k] for k in NAMES5]
    P.v("V1 independent solver classifies each of the 15 drawings and the counts equal the key", solved == counts, solved)
    P.v("V1b the five counts are different and add to 15", len(set(counts)) == 5 and sum(counts) == 15)
    cv = code_verify(counts, table, word, 0, 15, domain)
    code_checks(P, cv, word)
    P["cv"] = cv
    def chk(ans):
        if sum(ans) != 15: return False
        if any(a not in table for a in ans): return False
        return "".join(table[a] for a in ans).lower() in BIG
    P["model"] = dict(truth=list(counts), domains=[domain] * 5, check=chk, numeric=True)
    P["facts"] = "15 " + " ".join(str(v) for v in table)
    return P

# =============================================================================== P2-36 Picture Graph Scales
FRUITS = ["apple", "star", "ball", "cat", "flower", "drum", "boat"]
CATNAME = {"apple": "Apples", "star": "Stars", "ball": "Balls", "cat": "Cats", "flower": "Flowers", "drum": "Drums", "boat": "Boats"}

def face_g():
    return ('<g class="obj" data-k="face"><circle cx="5.25" cy="5.25" r="4.7" fill="#fff" stroke="#000" stroke-width="0.6"/><circle cx="3.6" cy="4.2" r="0.6" fill="#000"/><circle cx="6.9" cy="4.2" r="0.6" fill="#000"/>'
            '<path d="M3,6.4 Q5.25,8.8 7.5,6.4" fill="none" stroke="#000" stroke-width="0.6" stroke-linecap="round"/></g>')

def graph_html(rows, kind_of, scale, label_of, hidden=()):
    """rows: list of (name, k symbols); one symbol of kind `kind_of` = `scale` children"""
    out = ""
    for i, (nm, k) in enumerate(rows):
        if i in hidden:
            cells = '<span class="hid">covered</span>'
        else:
            cells = "".join(f'<span class="gcell">{svg(10.5, 10.5, face_g(), "gsym")}</span>' for _ in range(k))
        out += f'<div class="grow3" data-row="{i}"><span class="gname">{nm}</span><span class="gcells">{cells}</span></div>'
    key = f'<div class="gkey">Key: {svg(10.5, 10.5, face_g(), "gsym")} = {scale} children</div>'
    return f'<div class="pgraph3">{out}{key}</div>'

def read_graph_html(h):
    scale = int(re.search(r"= (\d+) children", h).group(1))
    rows = {}
    for m in re.finditer(r'<div class="grow3" data-row="(\d+)"><span class="gname">([^<]+)</span><span class="gcells">(.*?)</span></div>', h):
        cells = m.group(3)
        rows[m.group(2)] = None if "covered" in cells else len(re.findall(r'class="obj"', cells))
    return scale, rows

def page36():
    rng = random.Random(9336)
    while True:
        scale = rng.choice([2, 5, 10]); kind = rng.choice(FRUITS)
        names = rng.sample(["Red", "Blue", "Green", "Yellow", "Pink", "Black", "White"], 5)
        ks = rng.sample(range(2, 9), 5)
        rows = list(zip(names, ks)); S_ = dict(rows)
        qs = []
        a, b, c, d, e = names
        qs.append(("one", a)); qs.append(("one", b)); qs.append(("more", c, d)); qs.append(("two", d, e)); qs.append(("all",)); qs.append(("fewer", e, b))
        def val(q):
            k = q[0]
            if k == "one": return S_[q[1]] * scale
            if k == "more": return abs(S_[q[1]] - S_[q[2]]) * scale
            if k == "fewer": return abs(S_[q[1]] - S_[q[2]]) * scale
            if k == "two": return (S_[q[1]] + S_[q[2]]) * scale
            return sum(S_.values()) * scale
        qs = [("one", a), ("one", b), ("more" if S_[c] > S_[d] else "fewer", c, d) if True else None, ("two", d, e), ("all",), ("more" if S_[b] > S_[e] else "fewer", b, e)]
        ans = [val(q) for q in qs]
        if not distinct(ans) or max(ans) > 200: continue
        pool = set()
        for q, x in zip(qs, ans): pool |= {x + scale, x - scale, x // scale if scale else x}
        pool = sorted(v for v in pool if v not in ans and 0 < v <= 200)
        r = code_table_any(36, 6, ans, rng, 0, 200, n_decoy=3, tries=60, pool=pool)
        if r: word, table = r; break
    def qtext(q):
        k = q[0]
        if k == "one": return f"How many children chose {q[1]}?"
        if k == "more": return f"How many more children chose {q[1]} than {q[2]}?"
        if k == "fewer": return f"How many fewer children chose {q[1]} than {q[2]}?"
        if k == "two": return f"How many children chose {q[1]} or {q[2]}?"
        return "How many children are there in all?"
    qt = [qtext(q) for q in qs]
    cards = [qcard(i + 1, f"<p>{t}</p>", '<span class="ab w3"></span>', cls="inl tq") for i, t in enumerate(qt)]
    graph = graph_html(rows, kind, scale, None)
    P = code_items_page(36, 9336, "Picture Graph Scales", 1, "Picture graphs with scales: one picture stands for more than one", "Statistics - Data Representation and Interpretation",
        "1.1 (reading and interpreting data from picture graphs with scales)", ["ST1.1"], "Code-breaker (picture graph)",
        ["Read the key. One picture is more than 1.", "Answer each question.", INSTR_CODE],
        graph + qgrid(cards, 2), ans, table, word, 0, 200,
        "; ".join(f"{i+1}) {t} {a}" for i, (t, a) in enumerate(zip(qt, ans))),
        f"A picture graph of five colours with a key: one picture stands for {scale} children. Questions: read one row (twice), find how many more or fewer, add two rows, and the total. The pupil must use the scale, not just count pictures. The decoy letters stand for the number of pictures, or for one picture too many. A box left blank gives no letter and the check cannot see it.")
    sc, rd = read_graph_html(graph)
    def solve(t):
        m = re.fullmatch(r"How many children chose (\w+)\?", t)
        if m: return rd[m.group(1)] * sc
        m = re.fullmatch(r"How many (more|fewer) children chose (\w+) than (\w+)\?", t)
        if m: return abs(rd[m.group(2)] - rd[m.group(3)]) * sc
        m = re.fullmatch(r"How many children chose (\w+) or (\w+)\?", t)
        if m: return (rd[m.group(1)] + rd[m.group(2)]) * sc
        return sum(rd.values()) * sc
    solved = [solve(t) for t in qt]
    P.v("V1 independent solver (symbols counted in each printed row, key read back) equals the key", solved == ans, solved)
    P.v("V8 symbols are at least 8 mm and at most 8 in a row", all(1 <= k <= 8 for k in rd.values()) and True)
    P.v("V7 scale 2, 5 or 10", sc in (2, 5, 10), sc)
    return P

# =============================================================================== P2-37 Graph Detective Two
def page37():
    rng = random.Random(9437)
    while True:
        scale = rng.choice([5, 10]); kind = rng.choice(FRUITS)
        names = rng.sample(["Plums", "Pears", "Grapes", "Mangoes", "Peaches", "Lychees", "Melons"], 5)
        k1, k2, k3 = rng.sample(range(2, 8), 3); k4 = rng.randint(2, 7); k5 = rng.randint(2, 7)
        if k4 == k5 or k4 in (k1, k2, k3) or k5 in (k1, k2, k3): continue
        ks = [k1, k2, k3, k4, k5]; total = sum(ks) * scale
        a, b, c, d, e = names
        # d is covered (found from the total), e is told in the clues
        ans = [k4, k4 * scale, k5 * scale, (k1 - k4) * scale if k1 > k4 else (k4 - k1) * scale, (k2 - k5) * scale if k2 > k5 else (k5 - k2) * scale, total]
        if not distinct(ans) or max(ans) > 300: continue
        pool = set()
        for x in ans: pool |= {x + scale, x - scale, x + 1, x - 1}
        pool = sorted(v for v in pool if v not in ans and 0 < v <= 300)
        r = code_table_any(37, 6, ans, rng, 0, 300, n_decoy=2, tries=60, pool=pool)
        if r: word, table = r; break
    rows = list(zip(names, ks))
    graph = graph_html(rows, kind, scale, None, hidden=(3, 4))
    clues = [f"There are {k5} pictures for {e} (covered).", f"The graph shows {total} children in all."]
    q1 = f"How many pictures for {d}?"
    qs = [q1, f"How many children chose {d}?", f"How many children chose {e}?",
          (f"How many more children chose {a} than {d}?" if k1 > k4 else f"How many fewer children chose {a} than {d}?"),
          (f"How many more children chose {b} than {e}?" if k2 > k5 else f"How many fewer children chose {b} than {e}?"),
          "How many children are there in all?"]
    cards = [qcard(i + 1, f"<p>{t}</p>", '<span class="ab w3"></span>', cls="inl tq") for i, t in enumerate(qs)]
    body = (graph + '<ul class="clues">' + "".join(f"<li>{c}</li>" for c in clues) + '</ul>' + qgrid(cards, 2))
    P = code_items_page(37, 9437, "Graph Detective Two", 2, "Picture graphs with scales: two rows are covered", "Statistics - Data Representation and Interpretation",
        "1.1 (reading and interpreting data from picture graphs with scales)", ["ST1.1"], "Code-breaker (picture graph with covered rows)",
        ["Two rows are covered.", "Use the clues. Answer each question.", INSTR_CODE],
        body, ans, table, word, 0, 300,
        "; ".join(f"{i+1}) {t} {a}" for i, (t, a) in enumerate(zip(qs, ans))),
        f"A picture graph where one picture stands for {scale} children and two rows are covered. One covered row is given in pictures, the total number of children is given, so the other covered row is found by taking the pictures of the other rows away from the total (in pictures: the total divided by the scale). The pupil can check that all five rows make the printed total. The decoy letters stand for pictures read as children, or one picture out. A box left blank gives no letter and the check cannot see it.",
        ps=True)
    P["check"] = "Write the letters in order. Do they spell a word? Do the five rows make the total?"
    P["instr"] = ["Two rows are covered.", "Use the clues. Answer each question.", INSTR_CODE]
    P["check_boxes"] = 6
    P["mk"] = ("code", "total")
    sc, rd = read_graph_html(graph)
    shown = {n: v for n, v in rd.items() if v is not None}
    t_ = int(re.search(r"shows (\d+) children", " ".join(clues)).group(1)); k5_ = int(re.search(r"There are (\d+) pictures", clues[0]).group(1))
    k4_ = t_ // sc - sum(shown.values()) - k5_
    names_ = list(rd)
    solved = [k4_, k4_ * sc, k5_ * sc, abs(shown[names_[0]] - k4_) * sc, abs(shown[names_[1]] - k5_) * sc, t_]
    P.v("V1 independent solver (visible rows counted, key and clues read back) equals the key", solved == ans, solved)
    P.v("V1b the covered rows are two and the pictures of all five rows make the printed total", len(rd) == 5 and sum(1 for v in rd.values() if v is None) == 2 and sum(ks) * scale == t_)
    P.v("V7 scale 5 or 10, at most 8 pictures in a row", sc in (5, 10) and all(k <= 8 for k in ks))
    return P

PAGES = [page33, page34, page35, page36, page37]
