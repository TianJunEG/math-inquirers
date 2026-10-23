"""Wave D: rectangles and squares, line symmetry, solids and nets (P4-31 to P4-36), tables, line graphs and pie charts (P4-37 to P4-39). P4-40 is colour by code.
Each pageNN() makes the puzzle from a seed, re-solves it with separate solver code that reads the PRINTED html or drawing, and gives validate.py a `model`."""
import random, re, math, itertools
from fractions import Fraction
from .common import *
from .kit import *
from .kit4 import *
from . import art6 as A6
from . import art7 as A7

ABX = '<span class="ab w4"></span>'
ABS = '<span class="ab w3"></span>'

def cards_of(body):
    return re.split(r'(?=<div class="qc )', body)[1:]

# =============================================================================== P4-31 Rectangle and Square Facts (true or false)
def fact_statement(rng, kind, true):
    s = rng.choice(["rectangle", "square"])
    if kind == "angles":
        n = 4 if true else rng.choice([2, 3, 1, 6]); return f"A {s} has {n} right angles."
    if kind == "parallel":
        n = 2 if true else rng.choice([1, 3, 4]); return f"A {s} has {n} pair{'s' if n != 1 else ''} of parallel sides."
    if kind == "equal4":
        return "All four sides of a square are equal." if true else f"Only {rng.choice(['two', 'three'])} sides of a square are equal."
    if kind == "pairs":
        n = 2 if true else rng.choice([1, 3, 4]); return f"A rectangle has {n} pair{'s' if n != 1 else ''} of equal sides."
    if kind == "opposite":
        rel = rng.choice(["parallel", "equal"]) if true else "perpendicular"; return f"Opposite sides of a {s} are {rel}."
    if kind == "meeting":
        rel = "perpendicular" if true else "parallel"; return f"Sides that meet at a corner of a {s} are {rel}."
    raise ValueError(kind)

def judge_statement(t):
    """independent evaluator: the printed statement against a small table of the properties of a rectangle and a square (diagonals are not used)"""
    m = re.fullmatch(r"A (rectangle|square) has (\d) right angles\.", t)
    if m: return int(m[2]) == 4
    m = re.fullmatch(r"A (rectangle|square) has (\d) pairs? of parallel sides\.", t)
    if m: return int(m[2]) == 2
    if re.fullmatch(r"All four sides of a square are equal\.", t): return True
    if re.fullmatch(r"Only (two|three) sides of a square are equal\.", t): return False
    m = re.fullmatch(r"A (rectangle) has (\d) pairs? of equal sides\.", t)
    if m: return int(m[2]) == 2
    m = re.fullmatch(r"Opposite sides of a (rectangle|square) are (parallel|equal|perpendicular)\.", t)
    if m: return m[2] in ("parallel", "equal")
    m = re.fullmatch(r"Sides that meet at a corner of a (rectangle|square) are (perpendicular|parallel|equal)\.", t)
    if m: return m[2] == "perpendicular" or (m[2] == "equal" and m[1] == "square")
    raise ValueError(t)

def page31():
    rng = random.Random(7131)
    kinds = ["angles", "parallel", "equal4", "pairs", "opposite", "meeting"]
    for _ in range(4000):
        word = word_candidates(31, 6)[rng.randrange(0, 3)]
        order = kinds[:]; rng.shuffle(order)
        truths = [rng.random() < .5 for _ in range(6)]
        if not 2 <= sum(truths) <= 4: continue
        qs = [fact_statement(rng, k, t) for k, t in zip(order, truths)]
        if len(set(qs)) < 6 or [judge_statement(q) for q in qs] != truths: continue
        try: rows_l = choice_letters(rng, word, 2)
        except RuntimeError: continue
        CLAIMED[31] = word
        break
    else: raise RuntimeError("p31")
    rows = []
    for i, (q, tr) in enumerate(zip(qs, truths)):
        right, other = rows_l[i]
        t_l, f_l = (right, other) if tr else (other, right)
        rows.append(choice_row(i + 1, f'<span class="yq">{q}</span>', ["True", "False"], [t_l, f_l], "tall"))
    P = choice_page(31, 7131, "Shape Facts", 1, "Properties of rectangles and squares", STRAND_GE,
        "2.1 (properties of rectangle and square, excluding diagonal properties)", ["RS2.1"], "Choice table (true or false)",
        ["Is each statement true or false?", "Circle the letter of the right answer.", "Write the six letters in the boxes."], rows, word, rows_l, [word[i] for i in range(6)],
        "; ".join(f"{i+1}) {'True' if t else 'False'}: {q}" for i, (q, t) in enumerate(zip(qs, truths))),
        "Six statements about rectangles and squares: right angles, pairs of parallel sides, equal sides, pairs of equal sides, opposite sides and sides that meet at a corner. Diagonals are not used. All four sides of a square are equal and a square has two pairs of parallel sides. Statements about pairs of equal sides are only made about rectangles, because the number of pairs in a square can be counted two ways. A statement about a square being a rectangle is not asked. Each row has a True and a False, each with a letter. The letters of the right answers, read down the rows, spell the word; every other way of choosing was tested against a very large word list and none spells a word. A box left blank gives no letter and the check cannot see it.")
    solved = []
    for content, opts in rows_of(P["body"]):
        d = {re.sub(r"<[^>]+>", "", t): l for t, l in opts}; q = re.sub(r"<[^>]+>", "", content)
        solved.append(d["True"] if judge_statement(q) else d["False"])
    P.v("V1 independent solver (each printed statement checked against the properties of a rectangle and a square) gets the word", "".join(solved) == word, solved)
    P.v("V4 between 2 and 4 statements are true", 2 <= sum(truths) <= 4)
    return P

# =============================================================================== P4-32 Complete the Corner (lettered points on a dot grid)
SHAPES32 = [((4, 0), (0, 3), "rectangle"), ((0, 4), (3, 0), "rectangle"), ((2, 2), (-1, 1), "rectangle"), ((2, 1), (-2, 4), "rectangle"), ((3, 1), (-1, 3), "square"),
            ((3, 3), (-3, 3), "square"), ((3, 0), (0, 3), "square"), ((2, 1), (-1, 2), "square"), ((4, 0), (0, 4), "square"), ((1, 1), (-3, 3), "rectangle"), ((3, 0), (0, 5), "rectangle")]

def page32():
    rng = random.Random(7232)
    n = 8
    for _ in range(6000):
        word = word_candidates(32, 6)[rng.randrange(0, 3)]
        want = ["rectangle", "square", "rectangle", "square", "rectangle", "square"]
        figs = []
        ok = True
        for w_ in want:
            for _t in range(200):
                u, v, k = rng.choice([s for s in SHAPES32 if s[2] == w_])
                if rng.random() < .5: u, v = v, u
                if rng.random() < .5: u = (-u[0], -u[1])
                c0 = (rng.randint(0, n - 1), rng.randint(0, n - 1))
                c1 = (c0[0] + u[0], c0[1] + u[1]); c2 = (c0[0] + v[0], c0[1] + v[1]); c3 = (c1[0] + v[0], c1[1] + v[1])
                if all(0 <= x < n and 0 <= y < n for x, y in (c0, c1, c2, c3)):
                    figs.append((c0, c1, c2, c3, w_)); break
            else: ok = False; break
        if not ok: continue
        try: lay = choice_letters(rng, word, 3)
        except RuntimeError: continue
        # candidate points: the right corner and two grid points that are not corners, apart from each other
        cands = []
        for i, (c0, c1, c2, c3, w_) in enumerate(figs):
            taken = [c0, c1, c2, c3]; dec = []
            tries = 0
            while len(dec) < 2 and tries < 400:
                tries += 1; q = (rng.randint(0, n - 1), rng.randint(0, n - 1))
                if all(max(abs(q[0] - t[0]), abs(q[1] - t[1])) >= 2 for t in taken + dec) and math.dist(q, c3) <= 6: dec.append(q)
            if len(dec) < 2: ok = False; break
            pts = [c3] + dec; order = [0, 1, 2]; rng.shuffle(order)
            cands.append([(pts[j], word[i] if j == 0 else lay[i][j]) for j in order])
        if not ok: continue
        CLAIMED[32] = word
        break
    else: raise RuntimeError("p32")
    rows = []; truth_letters = []; letters = []
    for i, (c0, c1, c2, c3, w_) in enumerate(figs):
        fig = A6.corner_svg(n, c0, c1, c2, [(p[0], p[1], l) for p, l in cands[i]])
        rows.append(f'<div class="srow3 cc"><span class="no">{i+1}</span><div class="sq3"><div class="afig">{fig}<p class="aq">Make a {w_}.</p></div></div></div>')
        truth_letters.append(word[i]); letters.append([word[i]] + [l for p, l in cands[i] if l != word[i]])
    body = '<div class="srows3 tallrows grid2 corner">' + "".join(rows) + '</div>'
    P = new_page(32, 7232, "Complete the Corner", 2, "Rectangles and squares on a dot grid", STRAND_GE,
        "2.2 (drawing rectangles and squares), 2.1 (properties of rectangle and square)", ["RS2.1", "RS2.2"], "Choice figures (lettered points)",
        "K1 the letter of the point that completes each shape spells a word (6 letters, two decoy points in each figure)",
        ["Three corners of each shape are marked.", "Find the point that makes the fourth corner.", "Write the six letters in the boxes."],
        body, "; ".join(f"{i+1}) {word[i]}: fourth corner of the {w_}" for i, (c0, c1, c2, c3, w_) in enumerate(figs)), f"Word: {word}",
        "Six dot grids, each with two sides of a rectangle (three of the corners) drawn. Three points carry letters; one of them is the fourth corner of the rectangle or square the card names and the other two are ordinary grid points that do not complete it. Three shapes are squares and three are other rectangles, some of them turned on the grid. The letters of the right points, read down the cards, spell the word; every other way of choosing was tested against a very large word list and none spells a word. Drawing the fourth corner and the missing sides is not checked, only the choice of the point. A box left blank gives no letter and the check cannot see it.",
        check="Write the six letters in order. Do they spell a word?", check_boxes=6, mk=("code",), mech_plain="Word from the letters of the points that complete the shapes (6 letters)")
    other = choice_other_words(word, letters)
    solved = []
    for h in re.findall(r'<div class="afig">(<svg.*?</svg>)<p class="aq">Make a (\w+)\.</p></div>', P["body"], re.S):
        svg_, kind = h
        pts, cs = A6.read_corner(svg_)
        p1, p0, p2 = pts; c3 = (p1[0] + p2[0] - p0[0], p1[1] + p2[1] - p0[1])
        d1, d2 = math.dist(p1, p0), math.dist(p2, p0)
        dot = (p1[0] - p0[0]) * (p2[0] - p0[0]) + (p1[1] - p0[1]) * (p2[1] - p0[1])
        assert abs(dot) < 0.5 and ((abs(d1 - d2) < 0.3) == (kind == "square")), (kind, d1, d2, dot)
        found = [t for x, y, t in cs if math.dist((x, y), c3) < 0.6]
        solved.append(found[0] if len(found) == 1 else "?")
    P.v("V1 independent solver (the two arms read from the drawing, the fourth corner worked out, the lettered point found) gets the word", "".join(solved) == word, solved)
    P.v("V3 no other way of choosing one point in every figure spells a word (large word list)", not other, other[:3])
    P.v("V3d the code word's letters have exactly ONE arrangement that is a word", anagrams(word) == [word.lower()])
    P.v("V7 three squares and three other rectangles; no candidate letter is a letter of the word in another position", sum(1 for f in figs if f[4] == "square") == 3)
    P["cv"] = dict(rate=1.0, single_total=12, single_detected=12)
    P["model"] = dict(truth=list(word), domains=[list(l) for l in letters], check=letters_check(), numeric=False)
    return P

# =============================================================================== P4-33 Mirror Lines (is this a line of symmetry?)
FIGS33 = {
    "rect":     [(4, 4), (42, 4), (42, 30), (4, 30)],
    "triangle": [(23, 3), (42, 31), (4, 31)],
    "house":    [(23, 2), (42, 13), (38, 31), (8, 31), (4, 13)],
    "tee":      [(4, 3), (42, 3), (42, 13), (28, 13), (28, 31), (18, 31), (18, 13), (4, 13)],
    "para":     [(12, 4), (44, 4), (34, 30), (2, 30)],
    "kite":     [(23, 2), (38, 14), (23, 32), (8, 14)],
    "scalene":  [(6, 30), (42, 24), (16, 4)],
    "trap":     [(14, 4), (32, 4), (42, 30), (4, 30)],
    "rtrap":    [(4, 4), (28, 4), (42, 30), (4, 30)],
    "ell":      [(4, 3), (16, 3), (16, 19), (42, 19), (42, 31), (4, 31)],
}
AXES33 = {
    ("rect", "v"): ((23, 0), (23, 34)), ("rect", "h"): ((0, 17), (46, 17)), ("rect", "d"): ((4, 4), (42, 30)),
    ("triangle", "v"): ((23, 0), (23, 34)), ("triangle", "s"): ((4, 31), (32.5, 17)),
    ("house", "v"): ((23, 0), (23, 34)), ("house", "o"): ((29, 0), (29, 34)),
    ("tee", "v"): ((23, 0), (23, 34)), ("tee", "h"): ((0, 17), (46, 17)),
    ("para", "v"): ((23, 0), (23, 34)), ("para", "m"): ((28, 4), (18, 30)),
    ("kite", "v"): ((23, 0), (23, 34)), ("kite", "h"): ((0, 14), (46, 14)),
    ("trap", "v"): ((23, 0), (23, 34)), ("ell", "d"): ((4, 31), (42, 3)),
}

def page33():
    rng = random.Random(7333)
    with_axis = [("rect", "v"), ("triangle", "s"), ("tee", "v"), ("para", "m"), ("house", "o"), ("kite", "v"), ("rect", "d"), ("tee", "h"), ("kite", "h"), ("house", "v"), ("triangle", "v"), ("rect", "h"), ("trap", "v")]
    no_axis = ["scalene", "rtrap", "trap", "house", "para", "tee"]
    for _ in range(4000):
        word = word_candidates(33, 6)[rng.randrange(0, 3)]
        picks = rng.sample(with_axis, 4); nos = rng.sample(no_axis, 2)
        items = [("axis", f, a) for f, a in picks] + [("fig", f, None) for f in nos]
        rng.shuffle(items)
        truths = []
        for kind, f, a in items:
            truths.append(A6.is_symmetric_about(FIGS33[f], *AXES33[(f, a)]) if kind == "axis" else A6.has_line_of_symmetry(FIGS33[f]))
        if not 2 <= sum(truths) <= 4 or len({(f, a) for k, f, a in items}) < 6: continue
        try: rows_l = choice_letters(rng, word, 2)
        except RuntimeError: continue
        CLAIMED[33] = word
        break
    else: raise RuntimeError("p33")
    rows = []
    for i, ((kind, f, a), tr) in enumerate(zip(items, truths)):
        fig = A6.mirror_svg(FIGS33[f], AXES33[(f, a)] if kind == "axis" else None)
        cap = "Is the dashed line a line of symmetry?" if kind == "axis" else "Does the figure have a line of symmetry?"
        right, other = rows_l[i]; yes_l, no_l = (right, other) if tr else (other, right)
        rows.append(choice_row(i + 1, f'<div class="afig mir">{fig}<p class="aq">{cap}</p></div>', ["Yes", "No"], [yes_l, no_l], "cc"))
    P = choice_page(33, 7333, "Mirror Lines", 1, "Line symmetry: is it a line of symmetry? is the figure symmetric?", STRAND_GE,
        "3.1 (identifying symmetric figures), 3.2 (determining whether a straight line is a line of symmetry of a symmetric figure)", ["LS3.1", "LS3.2"], "Choice cards (symmetry)",
        ["Look at each figure.", "Circle the letter of the right answer.", "Write the six letters in the boxes."], rows, word, rows_l, [word[i] for i in range(6)],
        "; ".join(f"{i+1}) {'Yes' if t else 'No'} ({f}{' with the line ' + a if k == 'axis' else ' without a line'})" for i, ((k, f, a), t) in enumerate(zip(items, truths))),
        "Six figures. Four show a dashed line and ask whether it is a line of symmetry (a rectangle cut along its middle, along its diagonal, a triangle cut from a corner to the middle of the opposite side, a figure with the line off centre, and similar). Two show no line and ask whether any line of symmetry exists (a scalene triangle and a trapezium with a right angle have none). The right answer was found by reflecting every figure in the line, or in every possible line through its middle, with a separate program. Each row has a Yes and a No, each with a letter. The letters of the right answers, read down the cards, spell the word; every other way of choosing was tested against a very large word list and none spells a word. A box left blank gives no letter and the check cannot see it.")
    P["body"] = P["body"].replace('class="srows3 tallrows"', 'class="srows3 tallrows grid2"')
    solved = []
    for content, opts in rows_of(P["body"]):
        poly, axis = A6.read_mirror(content)
        tr = A6.is_symmetric_about(poly, *axis) if axis else A6.has_line_of_symmetry(poly)
        d = {re.sub(r"<[^>]+>", "", t): l for t, l in opts}; solved.append(d["Yes"] if tr else d["No"])
    P.v("V1 independent solver (each drawn figure reflected in its dashed line, or in every line through its middle) gets the word", "".join(solved) == word, solved)
    P.v("V4 between 2 and 4 answers are Yes", 2 <= sum(truths) <= 4)
    return P

# =============================================================================== P4-34 Complete the Figure (symmetry grids and counts)
def page34():
    rng = random.Random(7434)
    for _ in range(20000):
        word = word_candidates(34, 6)[rng.randrange(0, 3)]
        # figure A: a vertical line in a 10 by 8 grid, the left half shaded; figure B: a horizontal line in an 8 by 10 grid, the top half shaded
        A_on = {(r, c) for r in range(8) for c in range(5) if rng.random() < .42}
        B_on = {(r, c) for r in range(5) for c in range(8) if rng.random() < .42}
        if not (10 <= len(A_on) <= 24 and 10 <= len(B_on) <= 24): continue
        fullA = A6.mirror_cells(A_on, 10, 8, ("v", 5)); fullB = A6.mirror_cells(B_on, 8, 10, ("h", 5))
        rA = rng.randint(1, 8); cA = rng.randint(6, 10); cB = rng.randint(1, 8); rB = rng.randint(6, 10)
        ans = [len(fullA), sum(1 for r, c in fullA if r == rA - 1), sum(1 for r, c in fullA if c == cA - 1),
               len(fullB), sum(1 for r, c in fullB if c == cB - 1), sum(1 for r, c in fullB if r == rB - 1)]
        if not distinct(ans) or min(ans) < 1: continue
        pool = {len(A_on), len(B_on), sum(1 for r, c in A_on if r == rA - 1), sum(1 for r, c in B_on if c == cB - 1), len(fullA) // 2 + 1, len(fullB) - 2}
        pool = {p_ for p_ in pool if p_ not in ans and 0 <= p_ <= 60}
        dom = list(range(0, 61))
        res = code_table_any(34, 6, ans, rng, 0, 60, n_decoy=3, tries=60, pool=sorted(pool), domain=dom)
        if res: word, table = res; break
    else: raise RuntimeError("p34")
    figA = A6.symm_svg(10, 8, A_on, ("v", 5)); figB = A6.symm_svg(8, 10, B_on, ("h", 5))
    qA = [f"How many squares are shaded in the whole figure?", f"How many are shaded in row {rA} of the whole figure?", f"How many are shaded in column {cA} of the whole figure?"]
    qB = [f"How many squares are shaded in the whole figure?", f"How many are shaded in column {cB} of the whole figure?", f"How many are shaded in row {rB} of the whole figure?"]
    def block(fig, qs, start):
        lines = "".join(f'<div class="qrow2"><span class="no">{start + i}</span><span class="qt">{q}</span>{ABS}</div>' for i, q in enumerate(qs))
        return f'<div class="sblock"><div class="sfig">{fig}</div><div class="sqs">{lines}</div></div>'
    body = f'<p class="lead">Figure 1: complete it with the dashed line as the mirror.</p>{block(figA, qA, 1)}<p class="lead">Figure 2: complete it with the dashed line as the mirror.</p>{block(figB, qB, 4)}'
    P = code_page(34, 7434, "Complete the Figure", 2, "Completing a symmetric figure on a square grid", STRAND_GE,
        "3.3 (completing a symmetric figure with respect to a given line of symmetry on square grid), 3.1 (identifying symmetric figures)", ["LS3.1", "LS3.3"], "Code-breaker (symmetry grids)",
        ["Shade the other side so the figure is symmetric.", "Count the shaded squares as asked.", INSTR_CODE], body, ans, table, word, 0, 60,
        f"1) {ans[0]}; 2) row {rA}: {ans[1]}; 3) column {cA}: {ans[2]}; 4) {ans[3]}; 5) column {cB}: {ans[4]}; 6) row {rB}: {ans[5]}",
        "Two square grids with half of a figure shaded and a dashed line as the mirror (a vertical line in figure 1, a horizontal line in figure 2). The pupil shades the other half so that the whole figure is symmetric, then answers three counting questions about each whole figure (the total, a row and a column, taken on the side that was empty). The answers can only be right if the mirror image is right, so they check the drawing indirectly: a pupil who shades the wrong squares usually gets different counts. The pupil's own shading is not seen, so a lucky wrong drawing with the right counts is possible. The decoy letters stand for the counts of the half that was already shaded. A box left blank gives no letter and the check cannot see it.",
        domain=dom)
    solved = []
    figs = re.findall(r'<div class="sfig">(<svg.*?</svg>)</div>', P["body"], re.S)
    qs_all = re.findall(r'<span class="qt">(.*?)</span>', P["body"])
    for fi, h in enumerate(figs):
        nc, nr, on, axis = A6.read_symm(h); full = A6.mirror_cells(on, nc, nr, axis)
        for q in qs_all[fi * 3:(fi + 1) * 3]:
            if "whole figure?" in q and "row" not in q and "column" not in q: solved.append(len(full))
            else:
                m = re.search(r"(row|column) (\d+)", q); k = int(m[2]) - 1
                solved.append(sum(1 for r, c in full if (r if m[1] == "row" else c) == k))
    P.v("V1 independent solver (shaded squares and the dashed line read from the drawing, the figure completed by reflection, the counts made) equals the key", solved == ans, solved)
    P.v("V7 figure 1 has a vertical line and figure 2 a horizontal line, and the row or column asked about lies on the side that was empty", cA >= 6 and rB >= 6 and fullA != A_on and fullB != B_on)
    return P

# =============================================================================== P4-35 Name the Solid
SOLID_NAMES = ["cube", "cuboid", "cone", "cylinder", "triangular prism", "square pyramid"]
CONFUSE = {"cube": ["cuboid", "square pyramid"], "cuboid": ["cube", "triangular prism"], "cone": ["square pyramid", "cylinder"], "cylinder": ["cone", "triangular prism"],
           "triangular prism": ["cuboid", "square pyramid"], "square pyramid": ["cone", "triangular prism"]}
DIMS35 = {"cube": dict(w=15), "cuboid": dict(w=24, h=11, d=13), "cone": dict(w=15, h=19), "cylinder": dict(w=13, h=18),
          "prism": dict(w=26, h=11, d=17), "pyramid": dict(w=15, h=19, d=15)}
KIND_OF = {"cube": "cube", "cuboid": "cuboid", "cone": "cone", "cylinder": "cylinder", "triangular prism": "prism", "square pyramid": "pyramid"}

def page35():
    rng = random.Random(7535)
    for _ in range(4000):
        word = word_candidates(35, 6)[rng.randrange(0, 3)]
        order = SOLID_NAMES[:]; rng.shuffle(order)
        try: lay = choice_letters(rng, word, 3)
        except RuntimeError: continue
        CLAIMED[35] = word
        break
    rows = []; layout = []
    for i, nm in enumerate(order):
        fig = A6.solid_svg(KIND_OF[nm], **DIMS35[KIND_OF[nm]])
        names = [nm] + CONFUSE[nm]; rng.shuffle(names)
        dec = iter(lay[i][1:]); lets = [word[i] if n == nm else next(dec) for n in names]
        rows.append(choice_row(i + 1, f'<div class="afig">{fig}</div>', names, lets, "cc"))
        layout.append(lets)
    letters = [[word[i]] + [l for l in layout[i] if l != word[i]] for i in range(6)]
    P = choice_page(35, 7535, "Name the Solid", 1, "Cube, cuboid, cone, cylinder, prism and pyramid", STRAND_GE,
        "4.1 (identifying 2D representations of cube, cuboid, cone, cylinder, prism, pyramid)", ["NT4.1"], "Choice cards (drawings of solids)",
        ["Look at each drawing of a solid.", "Circle the letter beside its name.", "Write the six letters in the boxes."], rows, word, letters, [word[i] for i in range(6)],
        "; ".join(f"{i+1}) {nm}" for i, nm in enumerate(order)),
        "Six drawings of solids: a cube, a cuboid, a cone, a cylinder, a triangular prism and a square pyramid, each with three names to choose from. The wrong names are the solids that look most alike (cube and cuboid, prism and pyramid, cone and pyramid, cylinder and prism). The cuboid is drawn at least twice as long as it is high and the cube has equal sides. The letters of the right choices, read down the cards, spell the word; every other way of choosing was tested against a very large word list and none spells a word. The pictures are drawings of solids; no real solid is handled. A box left blank gives no letter and the check cannot see it.")
    P["body"] = P["body"].replace('class="srows3 tallrows"', 'class="srows3 tallrows grid2 solids"')
    solved = []
    for content, opts in rows_of(P["body"]):
        kind = A6.read_solid(re.search(r"<svg.*?</svg>", content, re.S)[0])
        d = {re.sub(r"<[^>]+>", "", t): l for t, l in opts}; solved.append(d[kind])
    P.v("V1 independent solver (each drawing classified from its faces, ellipses and apex; the letter of that name read from the card) gets the word", "".join(solved) == word, solved)
    P.v("V7 all six solids of the syllabus list appear once", sorted(order) == sorted(SOLID_NAMES))
    return P

# =============================================================================== P4-36 Which Net?
NET_OPTIONS = ["cube", "cuboid", "triangular prism", "square pyramid", "no solid"]

def random_hexomino(rng, valid):
    while True:
        cells = {(0, 0)}
        while len(cells) < 6:
            x, y = rng.choice(sorted(cells)); d = rng.choice([(1, 0), (-1, 0), (0, 1), (0, -1)]); cells.add((x + d[0], y + d[1]))
        xs = [c[0] for c in cells]; ys = [c[1] for c in cells]
        if max(xs) - min(xs) > 3 or max(ys) - min(ys) > 3: continue
        cells = {(x - min(xs), y - min(ys)) for x, y in cells}
        if A6.cube_net_ok(cells) == valid:
            if not valid and (max(x for x, y in cells) < 2 or max(y for x, y in cells) < 1): continue
            return cells

def page36():
    rng = random.Random(7636)
    for _ in range(4000):
        word = word_candidates(36, 6)[rng.randrange(0, 3)]
        n1 = random_hexomino(rng, True); n6 = random_hexomino(rng, True); n5 = random_hexomino(rng, False)
        if n1 == n6: continue
        nets = [("cube", A6.net_svg(A6.squares_net(n1, 4.4))), ("cuboid", A6.net_svg(A6.cuboid_net(4, 2, 3, 3.6))), ("triangular prism", A6.net_svg(A6.prism_net(3, 4, 3.8))),
                ("square pyramid", A6.net_svg(A6.pyramid_net(3, 3.8))), ("no solid", A6.net_svg(A6.squares_net(n5, 4.4))), ("cube", A6.net_svg(A6.squares_net(n6, 4.4)))]
        order = list(range(6)); rng.shuffle(order); nets = [nets[i] for i in order]
        try: lay = choice_letters(rng, word, 3)
        except RuntimeError: continue
        CLAIMED[36] = word
        break
    else: raise RuntimeError("p36")
    rows = []; layout = []
    for i, (nm, fig) in enumerate(nets):
        others = [o for o in NET_OPTIONS if o != nm]
        names = [nm] + rng.sample(others, 2); rng.shuffle(names)
        dec = iter(lay[i][1:]); lets = [word[i] if n == nm else next(dec) for n in names]
        rows.append(choice_row(i + 1, f'<div class="afig netfig">{fig}</div>', names, lets, "cc"))
        layout.append(lets)
    letters = [[word[i]] + [l for l in layout[i] if l != word[i]] for i in range(6)]
    P = choice_page(36, 7636, "Which Net?", 2, "Nets of a cube, a cuboid, a prism and a pyramid", STRAND_GE,
        "4.3 (identifying the nets of 3D solids), 4.4 (identifying the solid which can be formed by a given net)", ["NT4.3", "NT4.4"], "Choice cards (nets)",
        ["Imagine folding each net.", "Circle the letter beside the solid it makes.", "Write the six letters in the boxes."], rows, word, letters, [word[i] for i in range(6)],
        "; ".join(f"{i+1}) {nm}" for i, (nm, fig) in enumerate(nets)),
        "Six nets: two nets of a cube (six squares that fold into a cube), a net of a cuboid, a net of a triangular prism, a net of a square pyramid and a set of six squares that does NOT fold into a cube (the answer is 'no solid'). Each net has three names to choose from. Whether six squares fold into a cube was decided by rolling a cube over them with a separate program. The cuboid net has six rectangles, the prism net two triangles and three rectangles, the pyramid net one square and four triangles. The letters of the right choices, read down the cards, spell the word; every other way of choosing was tested against a very large word list and none spells a word. Making the net by drawing and cutting is not asked. A box left blank gives no letter and the check cannot see it.")
    P["body"] = P["body"].replace('class="srows3 tallrows"', 'class="srows3 tallrows grid2 solids"')
    solved = []
    for content, opts in rows_of(P["body"]):
        kind = A6.read_net(re.search(r"<svg.*?</svg>", content, re.S)[0])
        d = {re.sub(r"<[^>]+>", "", t): l for t, l in opts}; solved.append(d[kind])
    P.v("V1 independent solver (faces counted from the drawing; six squares folded over a cube) gets the word", "".join(solved) == word, solved)
    P.v("V7 the nets are of a cube (twice), a cuboid, a prism, a pyramid and one that is not a net of a solid", sorted(n for n, f in nets) == sorted(["cube", "cube", "cuboid", "triangular prism", "square pyramid", "no solid"]))
    return P

# =============================================================================== P4-37 Complete the Table
ROWS37 = ["Red", "Blue", "Green"]; COLS37 = ["Week 1", "Week 2", "Week 3"]

def solve_table(cells, row_tot, col_tot, grand):
    """independent solver: cells[r][c], row_tot[r], col_tot[c], grand are numbers or None; fills every blank by using the sums of rows and columns. Returns the filled tables or None"""
    C = [list(r) for r in cells]; R = list(row_tot); Cc = list(col_tot); Gt = [grand]
    changed = True
    while changed:
        changed = False
        for r in range(3):
            unk = [c for c in range(3) if C[r][c] is None]
            if R[r] is None and not unk: R[r] = sum(C[r]); changed = True
            elif R[r] is not None and len(unk) == 1: C[r][unk[0]] = R[r] - sum(x for x in C[r] if x is not None); changed = True
        for c in range(3):
            unk = [r for r in range(3) if C[r][c] is None]
            if Cc[c] is None and not unk: Cc[c] = sum(C[r][c] for r in range(3)); changed = True
            elif Cc[c] is not None and len(unk) == 1: C[unk[0]][c] = Cc[c] - sum(C[r][c] for r in range(3) if C[r][c] is not None); changed = True
        if Gt[0] is None and all(x is not None for x in R): Gt[0] = sum(R); changed = True
        if Gt[0] is None and all(x is not None for x in Cc): Gt[0] = sum(Cc); changed = True
        if Gt[0] is not None:
            if sum(1 for x in R if x is None) == 1: k = R.index(None); R[k] = Gt[0] - sum(x for x in R if x is not None); changed = True
            if sum(1 for x in Cc if x is None) == 1: k = Cc.index(None); Cc[k] = Gt[0] - sum(x for x in Cc if x is not None); changed = True
    ok = all(x is not None for r in C for x in r) and None not in R and None not in Cc and Gt[0] is not None
    return (C, R, Cc, Gt[0]) if ok else None

def table_html(cells, rt, ct, g, blank):
    """blank: set of positions ('c', r, c), ('r', r), ('k', c), ('g',) left empty"""
    box = '<span class="ab w2 tb"></span>'
    def cell(v, key): return f"<td>{box}</td>" if key in blank else f"<td>{v}</td>"
    h = "<table class=\"tt37\"><tr><th></th>" + "".join(f"<th>{c}</th>" for c in COLS37) + "<th>Total</th></tr>"
    for r in range(3):
        h += f"<tr><th>{ROWS37[r]}</th>" + "".join(cell(cells[r][c], ("c", r, c)) for c in range(3)) + cell(rt[r], ("r", r)) + "</tr>"
    h += "<tr><th>Total</th>" + "".join(cell(ct[c], ("k", c)) for c in range(3)) + cell(g, ("g",)) + "</tr></table>"
    return h

def read_table(h):
    """independent reader: the 4 by 4 body of the printed table: numbers, None for a blank"""
    rows = re.findall(r"<tr>(.*?)</tr>", h, re.S)[1:]
    grid = []
    for r in rows:
        tds = re.findall(r"<td>(.*?)</td>", r, re.S)
        grid.append([None if "class=" in t else int(t) for t in tds])
    return grid

def page37():
    rng = random.Random(7751)
    for _ in range(20000):
        cells = [[rng.randint(4, 15) for _ in range(3)] for _ in range(3)]
        rt = [sum(r) for r in cells]; ct = [sum(cells[r][c] for r in range(3)) for c in range(3)]; g = sum(rt)
        positions = [("c", r, c) for r in range(3) for c in range(3)] + [("r", r) for r in range(3)] + [("k", c) for c in range(3)] + [("g",)]
        blank = rng.sample(positions, 6)
        def val(k): return cells[k[1]][k[2]] if k[0] == "c" else rt[k[1]] if k[0] == "r" else ct[k[1]] if k[0] == "k" else g
        cp = [[None if ("c", r, c) in blank else cells[r][c] for c in range(3)] for r in range(3)]
        rp = [None if ("r", r) in blank else rt[r] for r in range(3)]; kp = [None if ("k", c) in blank else ct[c] for c in range(3)]; gp = None if ("g",) in blank else g
        if solve_table(cp, rp, kp, gp) is None: continue
        if sum(1 for k in blank if k[0] == "c") < 3 or ("g",) in blank: continue
        blank.sort(key=lambda k: (k[1], k[2]) if k[0] == "c" else (k[1], 3) if k[0] == "r" else (3, k[1]))        # reading order: row by row, left to right, then the bottom row
        ans = [val(k) for k in blank]
        if not distinct(ans): continue
        pool = {a + d for a in ans for d in (-1, 1, -10, 10)}
        pool = {p_ for p_ in pool if p_ not in ans and 0 <= p_ <= 99}
        dom = list(range(0, 100))
        res = code_table_any(37, 6, ans, rng, 0, 99, n_decoy=3, tries=60, pool=sorted(pool), domain=dom)
        if res: word, table = res; break
    else: raise RuntimeError("p37")
    th = table_html(cells, rt, ct, g, set(blank))
    body = f'<p class="lead">Stickers won by three teams in three weeks</p>{th}'
    P = code_page(37, 7751, "Complete the Table", 2, "Completing a table from given data", STRAND_ST,
        "1.1 (completing a table from given data), 1.2 (reading and interpreting data from tables)", ["ST1.1", "ST1.2"], "Code-breaker (table with totals)",
        ["Some numbers in the table are missing.", "Use the totals to find them.", "Write the six numbers in order, row by row. " + INSTR_CODE], body, ans, table, word, 0, 99,
        "; ".join(f"{i+1}) {a}" for i, a in enumerate(ans)),
        "A table of three teams and three weeks with a total for each row, each column and the whole table. Six of the sixteen numbers are missing (never the grand total, at least three inside the table). Every missing number can be found by subtracting or adding along a row or a column. The pupil writes the six numbers in reading order and looks them up in the code table. A wrong number makes the rows or columns fail to add up and a letter that does not spell the word. The decoy letters stand for the numbers one or ten away. A box left blank gives no letter and the check cannot see it.",
        domain=dom, mk=("code", "total"), check="Do all rows and columns add up to their totals? Do the six letters spell a word?",
        mech="K3 rows and columns add to their totals + K1 code word (6 letters)", plain="Totals and code word (6 letters)")
    P["check_boxes"] = 6
    grid = read_table(body)
    cp = [row[:3] for row in grid[:3]]; rp = [row[3] for row in grid[:3]]; kp = grid[3][:3]; gp = grid[3][3]
    sol = solve_table(cp, rp, kp, gp)
    unk = []
    for r in range(3):          # the pupil's order, read from the printed table: row by row, left to right, then the bottom row
        unk += [("c", r, c) for c in range(3) if cp[r][c] is None] + ([("r", r)] if rp[r] is None else [])
    unk += [("k", c) for c in range(3) if kp[c] is None]
    got = [sol[0][k[1]][k[2]] if k[0] == "c" else sol[1][k[1]] if k[0] == "r" else sol[2][k[1]] for k in unk]
    P.v("V1 independent solver (printed table read back, every blank found from row and column totals) equals the key, in reading order", got == ans, got)
    def consistent(a):
        cur_c = [list(r) for r in cp]; cur_r = list(rp); cur_k = list(kp); cur_g = gp
        for k, v in zip(unk, a):
            if k[0] == "c": cur_c[k[1]][k[2]] = v
            elif k[0] == "r": cur_r[k[1]] = v
            else: cur_k[k[1]] = v
        return all(sum(cur_c[r]) == cur_r[r] for r in range(3)) and all(sum(cur_c[r][c] for r in range(3)) == cur_k[c] for c in range(3)) and sum(cur_r) == cur_g
    def chk(a):
        if any(x not in table for x in a) or not consistent(a): return False
        return "".join(table[x] for x in a).lower() in BIG
    dom_set = P["model"]["domains"][0]
    P.v("V2 the right answers make every row and column add up", consistent(ans))
    P.v("V3b every single wrong number breaks a row or a column total", all(not consistent([a if j != k else v for j, a in enumerate(ans)]) for k in range(6) for v in dom_set if v != ans[k]))
    P["model"] = dict(truth=list(ans), domains=[dom_set] * 6, check=chk, numeric=True)
    return P

# =============================================================================== P4-38 Line Graph Detective
def page38():
    rng = random.Random(7861)
    cats = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
    for _ in range(20000):
        vals = [rng.randrange(10, 60, 5) for _ in range(6)]
        if len(set(vals)) < 5 or vals[0] in (30, 45) or vals[1] in (30, 45): continue
        ia, ib, ic, id_ = rng.sample(range(6), 4); ix, iy = rng.sample(range(6), 2)
        q = [vals[ia], vals[ib], abs(vals[ic] - vals[id_]), None, vals[ix] + vals[iy], max(vals) - min(vals)]
        # a rise between two neighbouring days
        rises = [(i, i + 1) for i in range(5) if vals[i + 1] > vals[i]]
        if not rises: continue
        ri = rng.choice(rises); q[3] = vals[ri[1]] - vals[ri[0]]
        ans = q
        if vals[ic] == vals[id_] or not distinct(ans) or max(ans) > 100: continue
        pool = {a + d for a in ans for d in (-5, 5, -10, 10)} | {vals[ic] + vals[id_], vals[ri[1]] + vals[ri[0]]}
        pool = {p_ for p_ in pool if p_ not in ans and 0 <= p_ <= 120}
        dom = list(range(0, 121))
        res = code_table_any(38, 6, ans, rng, 0, 120, n_decoy=3, tries=60, pool=sorted(pool), domain=dom)
        if res: word, table = res; break
    else: raise RuntimeError("p38")
    fig = A7.line_graph_svg(cats, vals, h=66.0)
    qs = [f"How many pupils joined in {cats[ia]}?", f"How many pupils joined in {cats[ib]}?", f"How many more pupils joined in {cats[max((ic, id_), key=lambda i: vals[i])]} than in {cats[min((ic, id_), key=lambda i: vals[i])]}?",
          f"From {cats[ri[0]]} to {cats[ri[1]]}, the number went up by how many?", f"How many pupils joined in {cats[ix]} and {cats[iy]} together?", "How many more joined in the busiest month than the quietest?"]
    lines = "".join(f'<div class="qrow2"><span class="no">{i+1}</span><span class="qt">{q_}</span>{ABS}</div>' for i, q_ in enumerate(qs))
    body = f'<p class="lead">Pupils who joined the swimming club each month</p><div class="lgraph">{fig}</div><div class="lqs">{lines}</div>'
    P = code_page(38, 7838, "Line Graph Detective", 1, "Reading a line graph", STRAND_ST,
        "1.2 (reading and interpreting data from line graphs)", ["ST1.2"], "Code-breaker (line graph)",
        ["Read the line graph.", "Write each answer in its box.", INSTR_CODE], body, ans, table, word, 0, 120,
        "; ".join(f"{i+1}) {a}" for i, a in enumerate(ans)) + f". Data: " + ", ".join(f"{c} {v}" for c, v in zip(cats, vals)),
        "A line graph of the pupils who joined a club in six months, scale 0 to 60 with a dotted line half way between the numbers (so every point is a multiple of 5). Six questions: two readings, a difference between two days, a rise between two neighbouring days, a total of two days and the difference between the busiest and the quietest day. The decoy letters stand for the usual slips: reading one line too high or too low, or adding when the question asks for the difference. A box left blank gives no letter and the check cannot see it.",
        domain=dom, mk=("code",))
    gdata = A7.read_line_graph(re.search(r"<svg.*?</svg>", body, re.S)[0])
    solved = []
    for q_ in re.findall(r'<span class="qt">(.*?)</span>', body):
        days = re.findall(r"\b(Jan|Feb|Mar|Apr|May|Jun)\b", q_)
        if q_.startswith("How many pupils joined in") and "together" not in q_: solved.append(gdata[days[0]])
        elif "together" in q_: solved.append(gdata[days[0]] + gdata[days[1]])
        elif "the busiest month" in q_: solved.append(max(gdata.values()) - min(gdata.values()))
        elif "went up" in q_: solved.append(gdata[days[1]] - gdata[days[0]])
        else: solved.append(gdata[days[0]] - gdata[days[1]])
    P.v("V1 independent solver (every point read from the drawing against the labelled scale) equals the key", solved == ans, solved)
    P.v("V7 every value is a multiple of 5 between 10 and 55 and the scale goes to 60", all(v % 5 == 0 and 10 <= v <= 55 for v in vals))
    P["key"]["answers"] += ""
    return P

# =============================================================================== P4-39 Pie Chart
def page39():
    rng = random.Random(7939)
    names = ["Rice", "Noodles", "Bread", "Pasta", "Soup", "Salad"]
    for _ in range(20000):
        k = rng.choice([4, 5]); cuts = sorted(rng.sample(range(1, 8), k - 1)); ws = [b - a for a, b in zip([0] + cuts, cuts + [8])]
        if max(ws) > 4 or min(ws) < 1 or len(set(ws)) < 3: continue
        sec = list(zip(rng.sample(names, k), ws)); total = rng.choice([240, 320, 400, 480]); unit = total // 8
        ia, ib = rng.sample(range(k), 2)
        ic, id_ = [(i, j) for i in range(k) for j in range(k) if ws[i] > ws[j]][rng.randrange(0, 1)] if any(ws[i] > ws[j] for i in range(k) for j in range(k)) else (0, 1)
        iy, iz = rng.sample(range(k), 2)
        ans = [ws[ia] * unit, ws[ib] * unit, (ws[ic] - ws[id_]) * unit, (ws[iy] + ws[iz]) * unit, total - ws[ia] * unit, total // 2]
        if not distinct(ans) or max(ans) > 480: continue
        pool = {ws[ia], ws[ib] * unit // 2, ws[ia] * unit + unit, total // 8, (ws[ic] + ws[id_]) * unit, ws[ia] * unit - unit, total // 4, ws[ib] * unit + unit}
        pool = {p_ for p_ in pool if p_ not in ans and 0 < p_ <= 600}
        dom = plausible_domain(ans, pool, rng=rng, sample=100, hi=600, spread=(10, 20, 30, 40, 50, 60))
        res = code_table_any(39, 6, ans, rng, 0, 600, n_decoy=3, tries=60, pool=sorted(pool), domain=dom)
        if res: word, table = res; break
    else: raise RuntimeError("p39")
    fig = A7.pie_svg(sec)
    nm = lambda i: sec[i][0]
    qs = [f"How many pupils chose {nm(ia)}?", f"How many pupils chose {nm(ib)}?", f"How many more pupils chose {nm(ic)} than {nm(id_)}?",
          f"How many pupils chose {nm(iy)} or {nm(iz)}?", f"How many pupils did not choose {nm(ia)}?", "How many pupils are in half of the pie chart?"]
    lines = "".join(f'<div class="qrow2"><span class="no">{i+1}</span><span class="qt">{q_}</span>{ABS}</div>' for i, q_ in enumerate(qs))
    body = f'<div class="sblock pieb"><div class="sfig">{fig}</div><div class="sqs"><p class="lead">There are {total} pupils. Each pupil chose one food.</p>{lines}</div></div>'
    P = code_page(39, 7939, "Pie Chart", 2, "Reading a pie chart", STRAND_ST,
        "1.2 (reading and interpreting data from pie charts)", ["ST1.2", "FS2.1"], "Code-breaker (pie chart)",
        ["The pie chart is cut into 8 equal slices.", "Use the number of pupils to answer.", INSTR_CODE], body, ans, table, word, 0, 600,
        "; ".join(f"{i+1}) {a}" for i, a in enumerate(ans)) + f". Slices: " + ", ".join(f"{n} {w}" for n, w in sec) + f"; one slice is {unit} pupils",
        "A pie chart cut into 8 equal slices (thin dotted lines) with four or five sectors, and the total number of pupils. The pupil counts the slices of a sector, finds what fraction of the pie it is, and finds that fraction of the total. Six questions: two sectors, a difference between two sectors, two sectors together, the pupils who did not choose one food and half of the pie. The decoy letters stand for the usual slips: giving the number of slices instead of pupils, or one slice too many or too few. A box left blank gives no letter and the check cannot see it.",
        domain=dom, ps=True, mk=("code",))
    pie = A7.read_pie(re.search(r"<svg.*?</svg>", body, re.S)[0]); tot = int(re.search(r"There are (\d+) pupils", body)[1])
    cnt = {n: tot * a // 360 for n, a in pie}
    solved = []
    for q_ in re.findall(r'<span class="qt">(.*?)</span>', body):
        found = [n for n in cnt if re.search(r"\b" + n + r"\b", q_)]
        if q_.startswith("How many pupils chose") and " or " not in q_: solved.append(cnt[found[0]])
        elif " or " in q_: solved.append(sum(cnt[n] for n in found))
        elif "more pupils chose" in q_:
            a_, b_ = re.search(r"chose (\w+) than (\w+)", q_)[1], re.search(r"chose (\w+) than (\w+)", q_)[2]; solved.append(cnt[a_] - cnt[b_])
        elif "did not choose" in q_: solved.append(tot - cnt[found[0]])
        else: solved.append(tot // 2)
    P.v("V1 independent solver (each sector's angle read from the drawing, its share of the total worked out) equals the key", solved == ans, solved)
    P.v("V7 the slices are 8 equal slices; every sector is a whole number of slices; every number of pupils is a whole number", all(a % 45 == 0 for n, a in pie) and sum(a for n, a in pie) == 360 and total % 8 == 0)
    return P

PAGES = [page31, page32, page33, page34, page35, page36, page37, page38, page39]
