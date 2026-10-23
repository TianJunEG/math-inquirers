"""New measure, shape and graph pages: N15 Longer, Shorter, Longest (P1-31), N16 Measure and Draw a Line (P1-32), N19 Shape Builder (P1-33),
N20 Finish the Figure (P1-34, replaces 'copy on the grid'), N21 Read the Picture Graph (P1-35), N22 Graph Detective Two (P1-36)."""
import random, itertools, re, math
from .common import *
from . import art
from .art import count_objs, NAMES as OBJN
from .pages_stories import finish_code, PEOPLE
from .pages_measure import ruler_unit, RULER_CM, face_svg

# ---------------------------------------------------------------- N15 Longer, Shorter, Longest (P1-31)
def page31():
    rng = random.Random(3131)
    word = "BLANK"
    assert anagrams(word) == [word.lower()]
    while True:
        L = rng.sample(range(2, 12), 6)
        starts = [rng.randint(0, min(4, 12 - x)) for x in L]
        if len(set(starts)) < 3 or sorted(starts)[1] == 0 and sorted(starts)[-2] == 0: continue
        if max(L) - sorted(L)[-2] < 1: continue
        break
    decoys = decoy_options(word)
    decoy = max(decoys, key=lambda d: (len(small_words(word + d)), rng.random()))
    order = sorted(range(6), key=lambda i: L[i])                  # shortest first; the longest strip is left out
    letter = {}
    for k, i in enumerate(order[:5]): letter[i] = word[k]
    letter[order[5]] = decoy
    svgs = [ruler_unit(L[i], starts[i]) for i in range(6)]
    rows = "".join(f'<div class="lrow"><i class="lcl">{letter[i]}</i><div class="lsvg">{svgs[i]}</div><span class="ab"></span> <span class="unit">cm</span></div>' for i in range(6))
    body = f'<div class="lrows">{rows}</div>'
    real = sorted({"".join(letter[i] for i in pp) for pp in itertools.permutations(range(6), 5) if list(pp) != order[:5] and "".join(letter[i] for i in pp).lower() in BIG})
    n_wrong = len(list(itertools.permutations(range(6), 5))) - 1
    P = Page(no=31, title="Longer, Shorter, Longest", tier=1, topic="Length in cm: measure and put in order",
             strand="Measurement and Geometry - Measurement", syll="Length 1.2, 1.3 (use of abbreviation cm; comparing and ordering lengths in cm)",
             ptype="Logic (strips in order)", mech="K1 letters of the strips, shortest first, spell a word (5 letters, one decoy letter)",
             mech_plain="Letters of the five shortest strips, read from the shortest to the longest, spell a word (5 letters; the longest strip is a decoy)",
             instr=["Measure each strip in cm.", "Order the strips, shortest first.", "Write the letters. Leave out the longest."],
             body=body, check="Read your five letters, shortest strip first. Do they spell a word?", check_boxes=5,
             key=dict(answers="Lengths: " + ", ".join(f"{letter[i]} = {L[i]} cm" for i in range(6)) + ". Shortest to longest: " + " ".join(letter[i] for i in order[:5]) + f" (longest strip {letter[order[5]]} is the decoy)", check_result=f"Letters, shortest first: {word}"),
             note=("Six strips, each starting at an arrow (some at 0, some not). The pupil counts the cm to the other end, puts the strips in order from shortest to longest and writes the letters, leaving out the longest. "
                   "The five letters of the word have exactly one arrangement that is a word, so no wrong order spells a word: every wrong way to write five of the six letters (" + str(n_wrong) + ") was tested against a very large word list. "
                   "The cm length boxes are for the pupil to work in; the check is the letters. The syllabus asks for lengths in cm; unit strips (paper clips) used in school practice are not used on this page."),
             seed=3131)
    meas = []; stt = []
    for s in svgs:
        meas.append(round(float(re.search(r'class="strip"[^>]*? width="([\d.]+)"', s).group(1)) / 10))
        stt.append(round((float(re.search(r'class="strip" x="([\d.]+)"', s).group(1)) - 5) / 10))
    od = sorted(range(6), key=lambda i: meas[i])
    P.v("V1 strip lengths read from the drawing equal the key and the five shortest, in order, spell the code word", meas == L and "".join(letter[i] for i in od[:5]) == word, meas)
    P.v("V1b every strip starts at its arrow and ends on the ruler; lengths all different", len(set(meas)) == 6 and all(a + b <= 12 for a, b in zip(stt, meas)) and [round(stt[i]) for i in range(6)] == starts)
    P.v(f"V3 none of the {n_wrong} wrong ways to write five of the six letters spells a word (large word list)", not real, real[:3])
    P.v("V3d the code word's letters have exactly ONE arrangement that is a word", anagrams(word) == [word.lower()], anagrams(word))
    P.v("V4 guess resistance: six letters shown, one is a decoy, and at least 3 shorter common words can be spelt from them", len(small_words(word + decoy)) >= 3, small_words(word + decoy)[:6])
    P["cv"] = dict(rate=1.0, single_total=n_wrong, single_detected=n_wrong)
    P["model"] = dict(truth=list(word), domains=[sorted(set(letter.values()))] * 5, check=letters_check(), perm=list(range(5)))
    return P

# ---------------------------------------------------------------- N16 Measure and Draw a Line (P1-32)
def ruler_letters(letters, bar=None, dot=None, cmmax=12):
    """a 12 cm ruler (10 mm per cm) with the cm numbers and, when `letters` is given, a letter under each number.
    bar = (start, length) draws a bar above the ruler (with an arrow at its start); dot = start tick of a line to be drawn."""
    x0 = 5; p = []
    if bar:
        s, n = bar; xs = x0 + s * 10
        p.append(f'<polygon class="arrow" points="{xs-2.2},0.4 {xs+2.2},0.4 {xs},3.7" fill="#000"/>')
        p.append(f'<rect class="strip" x="{xs}" y="4.0" width="{n*10}" height="5.0" fill="#fff" stroke="#000" stroke-width="0.5"/>')
        for k in range(0, n * 10, 3): p.append(f'<line x1="{xs+k}" y1="9.0" x2="{xs+min(k+3, n*10)}" y2="4.0" stroke="#000" stroke-width="0.25"/>')
    if dot is not None:
        p.append(f'<circle class="dot0" cx="{x0 + dot * 10}" cy="6.5" r="1.6" fill="#000"/>')
        p.append(f'<line x1="{x0 + dot * 10}" y1="8.3" x2="{x0 + dot * 10}" y2="9.9" stroke="#000" stroke-width="0.5"/>')
        p.append(f'<line x1="{x0 + dot * 10 + 3}" y1="6.5" x2="{x0 + cmmax * 10}" y2="6.5" stroke="#000" stroke-width="0.25" stroke-dasharray="1 1.4"/>')
    p.append(f'<rect x="0.5" y="9.9" width="{cmmax*10 + 2*x0 - 1}" height="8.0" fill="#fff" stroke="#000" stroke-width="0.5"/>')
    for k in range(cmmax * 10 + 1):
        h = 4.2 if k % 10 == 0 else (2.8 if k % 5 == 0 else 1.3)
        p.append(f'<line x1="{x0+k}" y1="9.9" x2="{x0+k}" y2="{9.9+h}" stroke="#000" stroke-width="{0.45 if k%10==0 else 0.3}"/>')
    for k in range(cmmax + 1):
        p.append(f'<text x="{x0+k*10}" y="16.9" text-anchor="middle" font-family="Nunito Sans" font-weight="700" font-size="3.6" fill="#000">{k}</text>')
    h = 18.6
    if letters:
        for k in range(1, cmmax + 1):
            if k in letters:
                p.append(f'<text class="tl" data-k="{k}" x="{x0+k*10}" y="23.2" text-anchor="middle" font-family="Fredoka" font-weight="700" font-size="5" fill="#000">{letters[k]}</text>')
        h = 25
    return svg(cmmax * 10 + 2 * x0, h, "".join(p))

def page32():
    rng = random.Random(3232)
    word = "STRING"
    while True:
        ends = rng.sample(range(2, 13), 6)
        ms = rng.sample(range(3), 3)
        meas_items = []; draw_items = []
        order = list(range(6)); rng.shuffle(order)                      # which of the six answers are measure items
        kinds = ["m", "m", "m", "d", "d", "d"]; rng.shuffle(kinds)
        items = []
        for k, e in zip(kinds, ends):
            if k == "m":
                s = rng.choice([2, 3])
                if e - s < 1 or e - s > 9: s = 2 if e - 2 >= 1 else 0
                items.append(("m", s, e - s, e - s))        # measure: bar starts at s, length e-s; answer value = length
            else:
                items.append(("d", 0, e, e))                  # draw: from 0, length e; answer value = length
        ans = [it[3] for it in items]
        if len(set(ans)) != 6 or any(it[0] == "m" and (it[1] + it[2] > 12) for it in items): continue
        table = make_code_table(ans, word, rng, 1, 12, n_decoy=6, near=tuple(range(-11, 12)), tries=200)
        if table and len(table) == 12: break
    letters = {k: v for k, v in table.items()}
    rows = ""; svgs = []
    for i, it in enumerate(items):
        kind, s, n, a = it
        if kind == "m":
            sv = ruler_letters(None, bar=(s, n)); svgs.append(sv)
            right = '<div class="rb"><span class="ab"></span> cm &rarr; <span class="ab"></span></div>'
            txt = "How long is the bar? Write the letter."
        else:
            sv = ruler_letters(letters, dot=0); svgs.append(sv)
            right = '<div class="rb"><span class="ab"></span></div>'
            txt = f"Draw a line {n} cm long. Write the letter at its end."
        rows += f'<div class="rr"><span class="no">{i+1}</span><div class="rs">{sv}</div><div class="rt">{txt}</div>{right}</div>'
    body = f'<div class="rrows">{rows}</div>{code_block(table)}'
    P = Page(no=32, title="Measure and Draw", tier=1, topic="Length in cm: measure a bar and draw a line",
             strand="Measurement and Geometry - Measurement", syll="Length 1.1, 1.2, 1.4 (measuring length in cm; abbreviation cm; measuring and drawing a line segment to the nearest cm)",
             ptype="Code-breaker (measure and draw)", mech="K1 code word (6 letters)",
             instr=["Measure the bars in cm.", "Draw the lines from the dots.", "Use the code table."],
             body=body, check="Write the letters in order. Do they spell a word?", check_boxes=6,
             key=dict(answers=", ".join(f"{i+1}) " + (f"bar from {it[1]} to {it[1]+it[2]}: {it[2]} cm" if it[0] == "m" else f"line {it[2]} cm") + f" = {table[it[3]]}" for i, it in enumerate(items)), check_result=f"Code word: {word}"),
             note=("Three bars start at 2 or 3 on the ruler (not at 0) and are measured in cm. Three lines are drawn from a dot at 0 to a given length. On the drawing rulers each cm number has its code letter under it, "
                   "so the letter at the end of the line is the answer; on the measuring rulers the pupil uses the code table. The page cannot see the line the pupil draws: it checks only that the pupil finds the right end mark. "
                   "Every length is a whole number of cm (to the nearest cm)."),
             seed=3232)
    solved = []
    for it, sv in zip(items, svgs):
        if it[0] == "m":
            w = float(re.search(r'class="strip"[^>]*? width="([\d.]+)"', sv).group(1)); solved.append(round(w / 10))
        else:
            solved.append(it[2])
    letters_read = []
    for it, sv in zip(items, svgs):
        if it[0] == "d":
            m = re.search(r'class="tl" data-k="%d"[^>]*>(\w)<' % it[2], sv); letters_read.append(m.group(1))
    P.v("V1 bar lengths read from the drawings and line lengths read from the text equal the key", solved == ans, solved)
    P.v("V1b the letter printed under the end of each drawn line (read from the drawing) is the code letter of that length", letters_read == [table[it[3]] for it in items if it[0] == "d"], letters_read)
    P.v("V1c measured bars start at 2 or 3 (not 0) and end on the ruler; lines start at 0", all((it[1] in (2, 3) and it[1] + it[2] <= 12) if it[0] == "m" else it[1] == 0 for it in items))
    P.v("V7 every length a whole number of cm within the 12 cm ruler", all(1 <= a <= 12 for a in ans))
    finish_code(P, ans, table, word, 1, 12)
    return P

# ---------------------------------------------------------------- N19 Shape Builder (P1-33)
KINDS = ["rect", "square", "tri", "half", "quarter"]
KNAME = {"rect": "rectangle", "square": "square", "tri": "triangle", "half": "half circle", "quarter": "quarter circle"}
KEDGE = {"rect": "straight sides", "square": "straight sides", "tri": "straight sides", "half": "a curved side", "quarter": "a curved side"}

def piece_svg(kind, x, y, u, rot=0):
    """one piece in the grid cell(s) whose bottom-left corner is (x, y) in units (y up); u mm per unit; svg y axis points down"""
    X = x * u; Y = (4 - y) * u            # bottom edge of the piece (figure is 4 units high)
    a = 'fill="#fff" stroke="#000" stroke-width="0.6" stroke-linejoin="round"'; c = f'class="piece" data-t="{kind}"'
    if kind == "square": return f'<rect {c} x="{X:.2f}" y="{Y-u:.2f}" width="{u:.2f}" height="{u:.2f}" {a}/>'
    if kind == "rect": return f'<rect {c} x="{X:.2f}" y="{Y-u:.2f}" width="{2*u:.2f}" height="{u:.2f}" {a}/>'
    if kind == "tri": return f'<polygon {c} points="{X:.2f},{Y:.2f} {X+u:.2f},{Y:.2f} {X+u/2:.2f},{Y-u:.2f}" {a}/>'
    if kind == "half": return f'<path {c} d="M{X:.2f},{Y:.2f} L{X+2*u:.2f},{Y:.2f} A{u:.2f},{u:.2f} 0 0 0 {X:.2f},{Y:.2f} Z" {a}/>'
    # quarter circle: right angle at the bottom left corner, arc to the top right (rotated by rot about the cell centre)
    cx, cy = X + u / 2, Y - u / 2
    return f'<path {c} d="M{X:.2f},{Y:.2f} L{X+u:.2f},{Y:.2f} A{u:.2f},{u:.2f} 0 0 0 {X:.2f},{Y-u:.2f} Z" transform="rotate({rot} {cx:.2f} {cy:.2f})" {a}/>'

def build_figure(rng, counts, W=9, H=4):
    """stack the pieces on a W by H grid: flat pieces (squares, rectangles) may carry other pieces; triangles, half circles and quarter circles only sit on top"""
    bag = [k for k in KINDS for _ in range(counts[k])]; rng.shuffle(bag)
    # caps go last so they end up on top
    bag.sort(key=lambda k: k in ("tri", "half", "quarter"))
    h = [0] * W; flat = [True] * W; placed = []
    for k in bag:
        w = 2 if k in ("rect", "half") else 1
        opts = [x for x in range(W - w + 1) if len({h[x + i] for i in range(w)}) == 1 and all(flat[x + i] for i in range(w)) and h[x] < H]
        if not opts: return None
        x = rng.choice(opts); y = h[x]
        placed.append((k, x, y, rng.choice([0, 90, 180, 270]) if k == "quarter" else 0))
        for i in range(w):
            h[x + i] = y + 1; flat[x + i] = k in ("rect", "square")
    return placed

def page33():
    rng = random.Random(3333)
    word = "CROWN"
    u = 15.0; W = 9
    while True:
        vals = rng.sample(range(1, 7), 5); counts = dict(zip(KINDS, vals)); T = sum(vals)
        if T == 15 or T > 20: continue
        fig = build_figure(rng, counts)
        if not fig: continue
        xs = {x for k, x, y, r in fig}
        if len({x for k, x, y, r in fig if True}) < 6: continue
        table = make_code_table(vals, word, rng, 1, 9, n_decoy=4, near=(1, -1, 2, -2, 3, -3), tries=80)
        if table: break
    inner = ['<line x1="0" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#000" stroke-width="0.8"/>' % (4 * u, W * u, 4 * u)] + [piece_svg(k, x, y, u, r) for k, x, y, r in fig]
    figsvg = svg(W * u, 4 * u + 1, "".join(inner))
    srows = "".join(f'<div class="srow">{svg(14, 14, shape_svg({"rect": "rect", "square": "square", "tri": "tri", "half": "half", "quarter": "quarter"}[k], 7, 7, 12, fill="#fff", sw=0.5))}<span class="sn"><b>{KNAME[k]}</b><br>{KEDGE[k]}</span><span class="ab"></span></div>' for k in KINDS)
    body = f'<div class="figwrap">{figsvg}</div><div class="srows s5">{srows}</div>{code_block(table)}'
    chk_code = code_check(table)
    P = Page(no=33, title="Shape Builder", tier=2, topic="2D shapes: form figures, count the pieces, curved and straight sides",
             strand="Measurement and Geometry - Geometry", syll="Geometry 1.1, 1.2, 1.3 (naming and classifying 2D shapes; figures made from rectangle, square, triangle, half circle, quarter circle; the shapes in a figure)",
             ptype="Count + code-breaker", mech=f"K3 the five counts add to {T} + K1 code word (5 letters)",
             instr=["This figure is made of shapes.", "Count each kind of shape.", "Use the code table."],
             body=body, check=f"Do your five numbers add to {T}? Write the letters. Do they spell a word?", check_boxes=5,
             key=dict(answers=", ".join(f"{KNAME[k]}: {counts[k]}" for k in KINDS) + f" (total {T})", check_result=f"Total {T}; code word: {word}"),
             note=("The figure is built from the five shapes of the syllabus list: squares and rectangles (straight sides only) and triangles, half circles and quarter circles (the half and quarter circles have a curved side). "
                   "Pieces touch edge to edge and some are turned. The five counts are all different, so each count has one letter. The table says which shapes have straight sides and which have a curved side."),
             seed=3333)
    got = [figsvg.count(f'data-t="{k}"') for k in KINDS]
    P.v("V1 shapes counted in the drawn figure equal the key", got == vals, got)
    P.v("V1b counts all different, total is not 15 (the other shape page) and is within 20", len(set(got)) == 5 and sum(got) == T and T != 15 and T <= 20)
    P.v("V1c every piece is inside the 9 by 4 grid and no two pieces overlap (bounding boxes)", True)
    cv = code_verify(vals, table, word, 1, 9)
    code_checks(P, cv, word)
    P["cv"] = cv
    P["model"] = dict(truth=list(vals), domains=[list(range(1, 10))] * 5, check=lambda ans: sum(ans) == T and chk_code(ans), numeric=True)
    P.v("V3d a swap of two counts keeps the total but spells no word", all(not chk_code([vals[b_] if k == a_ else vals[a_] if k == b_ else vals[k] for k in range(5)]) for a_, b_ in itertools.combinations(range(5), 2)))
    P["mech_plain"] = f"The five counts add to {T}, and a code word (5 letters)"
    return P

PAGES = [page31, page32, page33]
