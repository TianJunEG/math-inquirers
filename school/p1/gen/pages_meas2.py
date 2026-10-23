"""New measure, shape and graph pages: N15 Shortest to Longest (P1-31), N16 Measure and Draw a Line (P1-32), N19 Shape Builder (P1-33),
N20 Finish the Figure (P1-34, replaces 'copy on the grid'), N21 Read the Picture Graph (P1-35), N22 Graph Detective Two (P1-36)."""
import random, itertools, re, math
from .common import *
from . import art
from .art import count_objs, NAMES as OBJN
from .pages_stories import finish_code, PEOPLE
from .pages_measure import ruler_unit, RULER_CM, face_svg

# ---------------------------------------------------------------- N15 Shortest to Longest (P1-31)
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
    P = Page(no=31, title="Shortest to Longest", tier=1, topic="Length in cm: measure and put in order",
             strand="Measurement and Geometry - Measurement", syll="Length 1.2, 1.3 (use of abbreviation cm; comparing and ordering lengths in cm)",
             ptype="Logic (strips in order)", mech="K1 letters of the strips, shortest first, spell a word (5 letters, one decoy letter)",
             mech_plain="Letters of the five shortest strips, read from the shortest to the longest, spell a word (5 letters; the longest strip is a decoy)",
             instr=["Measure each strip in cm.", "Order the strips, shortest first.", "Write the letters. Leave out the longest."],
             body=body, check="Read your five letters, shortest strip first. Do they spell a word?", check_boxes=5,
             key=dict(answers="Lengths: " + ", ".join(f"{letter[i]} = {L[i]} cm" for i in range(6)) + ". Shortest to longest: " + " ".join(letter[i] for i in order[:5]) + f" (longest strip {letter[order[5]]} is the decoy)", check_result=f"Letters, shortest first: {word}"),
             note=("Six strips, each starting at an arrow (some at 0, some not). The pupil counts the cm to the other end, puts the strips in order from shortest to longest and writes the letters, leaving out the longest. "
                   "The five letters of the word have exactly one arrangement that is a word, so no wrong order spells a word: every wrong way to write five of the six letters was tested against a very large word list. "
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
            right = '<div class="rt2"><span class="lbx"><span class="ab"></span><small>cm</small></span><span class="lbx"><span class="ab"></span><small>letter</small></span></div>'
        else:
            sv = ruler_letters(letters, dot=0); svgs.append(sv)
            right = f'<div class="rt2"><span class="lbx"><b>Draw {n} cm</b><span class="ab"></span><small>letter</small></span></div>'
        rows += f'<div class="rr"><span class="no">{i+1}</span><div class="rs">{sv}</div>{right}</div>'
    ctrow = '<div class="ctrow">' + "".join(f'<div><span>{k}</span><b>{table[k]}</b></div>' for k in sorted(table)) + '</div>'
    body = f'<div class="rrows">{rows}</div><div class="blk">{ctrow}</div>'
    P = Page(no=32, title="Measure and Draw", tier=1, topic="Length in cm: measure a bar and draw a line",
             strand="Measurement and Geometry - Measurement", syll="Length 1.1, 1.2, 1.4 (measuring length in cm; abbreviation cm; measuring and drawing a line segment to the nearest cm)",
             ptype="Code-breaker (measure and draw)", mech="K1 code word (6 letters)",
             instr=["Measure the bars in cm.", "Draw the lines from the dots.", "Use the code ruler."],
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

# the "form a figure" task: a silhouette (outline only) is made of two pieces; which set of pieces makes it?
FORM_TEMPLATES = {"house": [("square", 0, 0, 0), ("tri", 0, 1, 0)], "dome": [("rect", 0, 0, 0), ("half", 0, 1, 0)],
                  "step": [("rect", 0, 0, 0), ("quarter", 0, 1, 0)], "block": [("square", 0, 0, 0), ("quarter", 0, 1, 0)]}
PIECE_AREA = {"square": 1.0, "rect": 2.0, "tri": 0.5, "half": math.pi / 2, "quarter": math.pi / 4}

def piece_poly(kind, x, y, rot=0):
    """polygon (unit coordinates, y up) of a piece whose bottom left corner is (x, y)"""
    if kind == "square": return [(x, y), (x + 1, y), (x + 1, y + 1), (x, y + 1)]
    if kind == "rect": return [(x, y), (x + 2, y), (x + 2, y + 1), (x, y + 1)]
    if kind == "tri": return [(x, y), (x + 1, y), (x + 0.5, y + 1)]
    if kind == "half": return [(x + 1 + math.cos(math.pi * i / 16), y + math.sin(math.pi * i / 16)) for i in range(17)]
    return [(x, y), (x + 1, y)] + [(x + math.cos(math.pi / 2 * (1 - i / 12)), y + math.sin(math.pi / 2 * (1 - i / 12))) for i in range(13)]

def silhouette_svg(tpl, u=13.0):
    from shapely.geometry import Polygon
    from shapely.ops import unary_union
    polys = [Polygon(piece_poly(k, x, y)) for k, x, y, r in FORM_TEMPLATES[tpl]]
    un = unary_union([p.buffer(0.001) for p in polys]).buffer(-0.001)
    pts = list(un.exterior.coords)
    h = 2 * u
    d = "M" + " L".join(f"{px * u + 1:.2f},{h - py * u + 1:.2f}" for px, py in pts) + " Z"
    return svg(round(2 * u + 2, 1), round(h + 2, 1), f'<path class="silh" d="{d}" fill="#fff" stroke="#000" stroke-width="0.9" stroke-linejoin="round"/>')

def silhouette_area(svg_text):
    pts = [tuple(float(v) for v in m.split(",")) for m in re.findall(r"[ML]?([\d.]+,[\d.]+)", re.search(r'class="silh" d="([^"]+)"', svg_text).group(1))]
    a = 0.0
    for (x1, y1), (x2, y2) in zip(pts, pts[1:] + pts[:1]): a += x1 * y2 - x2 * y1
    return abs(a) / 2

def option_pieces_svg(kinds, u=9.0):
    parts = []; x = 0.5
    for k in kinds:
        w = 2 * u if k in ("rect", "half") else u
        parts.append(piece_svg(k, x / u, 0.0, u, 0).replace("4 * u", "")) if False else None
        parts.append(piece_svg_flat(k, x, u)); x += w + 3
    return svg(round(x, 1), round(u + 2, 1), "".join(parts))

def piece_svg_flat(kind, x, u):
    a = 'fill="#fff" stroke="#000" stroke-width="0.6" stroke-linejoin="round"'; c = f'class="opiece" data-t="{kind}"'
    Y = u + 1
    if kind == "square": return f'<rect {c} x="{x:.2f}" y="1" width="{u}" height="{u}" {a}/>'
    if kind == "rect": return f'<rect {c} x="{x:.2f}" y="{1 + u / 2:.2f}" width="{2*u}" height="{u}" {a} transform="translate(0,{-u / 2:.2f})"/>'
    if kind == "tri": return f'<polygon {c} points="{x:.2f},{Y} {x+u:.2f},{Y} {x+u/2:.2f},1" {a}/>'
    if kind == "half": return f'<path {c} d="M{x:.2f},{Y} L{x+2*u:.2f},{Y} A{u},{u} 0 0 0 {x:.2f},{Y} Z" {a}/>'
    return f'<path {c} d="M{x:.2f},{Y} L{x+u:.2f},{Y} A{u},{u} 0 0 0 {x:.2f},{Y-u} Z" {a}/>'

def page33():
    rng = random.Random(3333)
    word = "BUDGIE"
    assert anagrams(word) == [word.lower()]
    pre = word[:5]
    u = 12.0; W = 9
    while True:
        vals = rng.sample(range(1, 7), 5); counts = dict(zip(KINDS, vals)); T = sum(vals)
        if T == 15 or T > 20: continue
        fig = build_figure(rng, counts)
        if not fig: continue
        if len({x for k, x, y, r in fig}) < 6: continue
        t = build_table(vals, pre, rng, 1, 9, 3, (1, -1, 2, -2, 3, -3), weighted=True)
        bad_l = bad_letters(word)
        if any(L in bad_l for v, L in t.items() if v not in vals): continue
        # no single slip and no swap of the five answers spells a word of the large list (tested on the whole six-letter word)
        okk = True
        for i in range(5):
            for v in range(1, 10):
                if v != vals[i]:
                    L = t.get(v)
                    if L is not None and (word[:i] + L + word[i + 1:]).lower() in BIG: okk = False
        if not okk: continue
        if len(candidates(list(t.values()) + [word[5]], 6)) < 3: continue
        table = t; break
    tpls = list(FORM_TEMPLATES); rng.shuffle(tpls)
    target = tpls[0]; wrongs = tpls[1:3]
    sets = [target] + wrongs
    slot = rng.randrange(3); order = wrongs[:]; order.insert(slot, target)
    last = [c for c in ALPHA if c != word[5] and (pre + c).lower() not in BIG and c not in pre]
    for _ in range(200):
        decs = rng.sample(last, 2)
        if len(candidates(list(table.values()) + decs + [word[5]], 6)) >= 3: break
    opt_letters = []; di = iter(decs)
    for s_ in range(3): opt_letters.append(word[5] if s_ == slot else next(di))
    inner = ['<line x1="0" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#000" stroke-width="0.8"/>' % (4 * u, W * u, 4 * u)] + [piece_svg(k, x, y, u, r) for k, x, y, r in fig]
    figsvg = svg(W * u, 4 * u + 1, "".join(inner))
    srows = "".join(f'<div class="srow">{svg(14, 14, shape_svg(k, 7, 7, 12, fill="#fff", sw=0.5))}<span class="sn"><b>{KNAME[k]}</b><br>{KEDGE[k]}</span><span class="ab"></span></div>' for k in KINDS)
    silh = silhouette_svg(target, 10.0)
    opts = "".join(f'<div class="fopt"><i class="cl">{opt_letters[s_]}</i>{option_pieces_svg([k for k, x, y, r in FORM_TEMPLATES[order[s_]]])}</div>' for s_ in range(3))
    form = (f'<div class="formtask"><div class="fg"><small>make this figure</small>{silh}</div><div class="fo"><p class="ptxt">Which pieces make this figure? Write that letter last.</p><div class="fopts">{opts}</div></div></div>')
    body = f'<div class="figwrap">{figsvg}</div><div class="srows s5">{srows}</div><div class="ctc">{code_block(table)}</div>{form}'
    chk_code = code_check(table)
    P = Page(no=33, title="Shape Builder", tier=2, topic="2D shapes: count the shapes in a figure and form a figure",
             strand="Measurement and Geometry - Geometry", syll="Geometry 1.1, 1.2, 1.3 (naming and classifying 2D shapes; forming a figure from rectangle, square, triangle, half circle, quarter circle; the shapes in a figure)",
             ptype="Count + form a figure + code-breaker", mech=f"K3 the five counts add to {T} + K1 code word (6 letters: five counts and the letter of the pieces that form the figure)",
             instr=["Count each kind of shape.", "Which pieces form the small figure?", "Use the code table."],
             body=body, check=f"Do the five numbers add to {T}? Write six letters. Do they spell a word?", check_boxes=6,
             key=dict(answers=", ".join(f"{KNAME[k]}: {counts[k]}" for k in KINDS) + f" (total {T}); the small figure is made of " + " and ".join(KNAME[k] for k, x, y, r in FORM_TEMPLATES[target]) + f" (letter {word[5]})", check_result=f"Total {T}; code word: {word}"),
             note=("The big figure is built from the five shapes of the syllabus list: squares and rectangles (straight sides only) and triangles, half circles and quarter circles (the half and quarter circles have a curved side). "
                   "Pieces touch edge to edge and some are turned. The five counts are all different, so each count has one letter. The table says which shapes have straight sides and which have a curved side. "
                   "The small figure task is forming a figure: the pupil sees an outline and picks which two pieces fit together to make it; the three sets have different total areas, so only one set can form the outline. Its letter is the sixth letter of the word."),
             seed=3333)
    got = [figsvg.count(f'data-t="{k}"') for k in KINDS]
    P.v("V1 shapes counted in the drawn figure equal the key", got == vals, got)
    P.v("V1b counts all different, total is not 15 (the other shape page) and is within 20", len(set(got)) == 5 and sum(got) == T and T != 15 and T <= 20)
    # independent check of the forming task: area of the silhouette (from the drawn outline) against the area of each option's pieces (from the drawn pieces)
    sa = silhouette_area(silh) / (10.0 ** 2)
    oareas = []
    for s_ in range(3):
        ks = re.findall(r'data-t="(\w+)"', option_pieces_svg([k for k, x, y, r in FORM_TEMPLATES[order[s_]]]))
        oareas.append(sum(PIECE_AREA[k] for k in ks))
    fits = [abs(a_ - sa) < 0.03 for a_ in oareas]
    P.v("V1c forming task: exactly one option's pieces have the same total area as the drawn outline, and its letter is the sixth letter of the word", sum(fits) == 1 and opt_letters[fits.index(True)] == word[5], str([round(a_, 2) for a_ in oareas]) + " vs " + str(round(sa, 2)))
    P.v("V1d the two wrong sets differ from the right one in kinds of pieces and in area (by at least 0.2)", all(abs(a_ - sa) > 0.2 for a_, f_ in zip(oareas, fits) if not f_))
    letters5 = [table[v] for v in vals]
    P.v("V2 the five count letters then the form letter spell " + word, "".join(letters5) + word[5] == word)
    nsl = 0; ndet = 0
    for i in range(5):
        for v in range(1, 10):
            if v == vals[i]: continue
            nsl += 1; L = table.get(v); w_ = word[:i] + (L or "?") + word[i + 1:]
            ndet += not (L is not None and w_.lower() in BIG)
    swaps = [x for i, j in itertools.combinations(range(5), 2) for x in ["".join(word[k] if k not in (i, j) else word[j if k == i else i] for k in range(6))] if x != word and x.lower() in BIG]
    P.v("V3 no single slip of a count spells another word (large word list)", ndet == nsl, f"{ndet}/{nsl}")
    P.v("V3c no swap of two counts spells a word", not swaps, swaps[:3])
    P.v("V3d the code word's letters have exactly ONE arrangement that is a word", anagrams(word) == [word.lower()], anagrams(word))
    P.v("V4 guess resistance: at least 3 common words fit the table letters and the three option letters", len(candidates(list(table.values()) + opt_letters, 6)) >= 3)
    P["cv"] = dict(rate=ndet / nsl, single_total=nsl, single_detected=ndet)
    def chk(ans):
        nums, last_ = ans[:5], ans[5]
        if sum(nums) != T or any(a_ not in table for a_ in nums): return False
        return ("".join(table[a_] for a_ in nums) + last_).lower() in BIG
    P["model"] = dict(truth=list(vals) + [word[5]], domains=[list(range(1, 10))] * 5 + [list(opt_letters)], check=chk, numeric=False)
    P["mech_plain"] = f"The five counts add to {T}; their letters and the letter of the pieces that form the small figure spell a word (6 letters)"
    return P


# ---------------------------------------------------------------- N20 Finish the Figure (P1-34): complete the half figure, with a printed match
TRI = {"bl": [(0, 0), (1, 0), (0, 1)], "br": [(0, 0), (1, 0), (1, 1)], "tl": [(0, 0), (0, 1), (1, 1)], "tr": [(1, 0), (1, 1), (0, 1)]}
FULL = [(0, 0), (1, 0), (1, 1), (0, 1)]
GC, GR = 6, 4                      # grid columns and rows; the left half is columns 0 to 2, the right half columns 3 to 5

def figure_edges(cells):
    """boundary edges of a figure given {(col,row): 'full'|'bl'|'br'|'tl'|'tr'} (row 0 at the bottom): edges shared by two cells cancel"""
    cnt = {}
    for (c, r), t in cells.items():
        pts = [(c + x, r + y) for x, y in (FULL if t == "full" else TRI[t])]
        for i in range(len(pts)):
            e = frozenset((pts[i], pts[(i + 1) % len(pts)])); cnt[e] = cnt.get(e, 0) + 1
    return {e for e, n in cnt.items() if n == 1}

def random_figure(rng):
    while True:
        cells = {(rng.randrange(GC), rng.randrange(GR)): "full"}
        target = rng.randint(9, 13)
        while len(cells) < target:
            c, r = rng.choice(list(cells))
            nb = [(c + dc, r + dr) for dc, dr in ((1, 0), (-1, 0), (0, 1), (0, -1)) if 0 <= c + dc < GC and 0 <= r + dr < GR and (c + dc, r + dr) not in cells]
            if nb: cells[rng.choice(nb)] = "full"
        for _ in range(rng.randint(2, 3)):                       # turn some cells into half squares (a triangle)
            k = rng.choice(list(cells)); cells[k] = rng.choice(list(TRI))
        left = sum(1 for (c, r) in cells if c < 3); right = sum(1 for (c, r) in cells if c >= 3)
        if left >= 3 and right >= 4 and any(c >= 3 and t != "full" for (c, r), t in cells.items()): return cells

def edges_right(e): return {x for x in e if all(p[0] >= 3 for p in x)}
def edges_left(e): return {x for x in e if all(p[0] <= 3 for p in x)}

def edge_svg(edges, cell, cols, x0, rows=GR, grid=True, thick=0.9, cls="edge"):
    """edges on a grid of `cols` x `rows` unit cells drawn `cell` mm each; x0 = first grid column shown (shifts x); y up"""
    out = []
    if grid:
        for i in range(cols + 1): out.append(f'<line x1="{i*cell:.2f}" y1="0" x2="{i*cell:.2f}" y2="{rows*cell:.2f}" stroke="#000" stroke-width="0.25"/>')
        for j in range(rows + 1): out.append(f'<line x1="0" y1="{j*cell:.2f}" x2="{cols*cell:.2f}" y2="{j*cell:.2f}" stroke="#000" stroke-width="0.25"/>')
    for e in sorted(edges, key=lambda e: sorted(e)):
        (xa, ya), (xb, yb) = sorted(e)
        out.append(f'<line class="{cls}" x1="{(xa-x0)*cell:.2f}" y1="{(rows-ya)*cell:.2f}" x2="{(xb-x0)*cell:.2f}" y2="{(rows-yb)*cell:.2f}" stroke="#000" stroke-width="{thick}" stroke-linecap="round"/>')
    return svg(cols * cell + 1, rows * cell + 1, '<g transform="translate(0.5,0.5)">' + "".join(out) + "</g>")

def read_edges(svg_text, cell, x0, rows=GR):
    """independent reader: the thick edges of a drawn figure back to lattice segments"""
    out = set()
    for m in re.finditer(r'class="edge" x1="([\d.]+)" y1="([\d.]+)" x2="([\d.]+)" y2="([\d.]+)"', svg_text):
        a = (round(float(m[1]) / cell) + x0, rows - round(float(m[2]) / cell)); b = (round(float(m[3]) / cell) + x0, rows - round(float(m[4]) / cell))
        out.add(frozenset((a, b)))
    return out

def page34():
    rng = random.Random(3434)
    word = "FROG"
    assert anagrams(word) == [word.lower()]
    NF = 4; cell_big = 6.0; cell_opt = 6.0
    while True:
        figs = []; ok = True
        for i in range(NF):
            cells = random_figure(rng); E = figure_edges(cells); R = edges_right(E)
            wrongs = []
            tries = 0
            while len(wrongs) < 2 and tries < 200:
                tries += 1
                c2 = dict(cells)
                k = rng.choice([(c, r) for c in range(3, GC) for r in range(GR)])
                if k in c2 and c2[k] != "full" and rng.random() < .6: c2[k] = rng.choice([t for t in TRI if t != c2[k]])
                elif k in c2 and len(c2) > 8 and rng.random() < .5: del c2[k]
                elif k not in c2:
                    c2[k] = rng.choice(["full"] + list(TRI))
                else: continue
                R2 = edges_right(figure_edges(c2))
                if R2 != R and R2 not in [w[1] for w in wrongs] and R2: wrongs.append((c2, R2))
            if len(wrongs) < 2: ok = False; break
            slot = rng.randrange(3)
            figs.append(dict(cells=cells, E=E, R=R, wrongs=wrongs, slot=slot))
        if not ok: continue
        # letters: the correct option of figure i has word[i]; the wrong options get decoy letters so that no other pick of one letter per figure spells a word
        pool = [c for c in ALPHA if c not in word]
        for _ in range(400):
            dl = rng.sample(pool, 8); letters = []; it = iter(dl)
            for i, f in enumerate(figs):
                row = []; 
                for s in range(3): row.append(word[i] if s == f["slot"] else next(it))
                letters.append(row)
            bad = [pp for pp in itertools.product(*letters) if "".join(pp) != word and "".join(pp).lower() in BIG]
            if not bad and len(set(sum(letters, []))) == 12: break
        else: continue
        break
    # drawing
    rows = ""; model_svgs = []; copy_svgs = []; opt_svgs = []
    for i, f in enumerate(figs):
        ms = edge_svg(f["E"], cell_big, GC, 0); model_svgs.append(ms)
        cs = edge_svg(edges_left(f["E"]), cell_big, GC, 0); copy_svgs.append(cs)
        opts = []
        wi = iter(f["wrongs"]); osv = []
        for s in range(3):
            R = f["R"] if s == f["slot"] else next(wi)[1]
            osv.append(edge_svg(R, cell_opt, 3, 3))
            opts.append(f'<div class="opt">{osv[-1]}<i class="cl">{letters[i][s]}</i></div>')
        opt_svgs.append(osv)
        rows += (f'<div class="frow"><span class="no">{i+1}</span><div class="fg"><small>copy this</small>{ms}</div><div class="fg"><small>finish it here</small>{cs}</div>'
                 f'<div class="fo"><small>which right half matches?</small><div class="opts">{"".join(opts)}</div></div></div>')
    body = f'<div class="frows">{rows}</div>'
    P = Page(no=34, title="Finish the Figure", tier=2, topic="Copy figures on a square grid",
             strand="Measurement and Geometry - Geometry", syll="Geometry 1.4 (copying figures on a dot grid or square grid)",
             ptype="Copy + matching pictures", mech="K1 letter of the matching right half in each row spells a word (4 letters)",
             mech_plain="The pupil finishes each copy, then picks the printed right half that matches; the four letters spell a word (4 letters)",
             instr=["Copy the figure on the grid.", "Finish the right half.", "Find the matching right half."],
             body=body, check="Write each matching letter. Do they spell a word?", check_boxes=4,
             key=dict(answers=", ".join(f"{i+1}) option {'ABC'[f['slot']]} (letter {word[i]})" for i, f in enumerate(figs)), check_result=f"Letters in order: {word}"),
             note=("Each figure is drawn on a square grid with straight lines along the grid and across some squares. The left half of each copy is already drawn; the pupil copies the right half from the figure above it. "
                   "Then the pupil compares their drawing with three printed right halves (each lettered) and writes the letter of the one that is the same. The wrong halves differ by one square or one slanting line. "
                   "No wrong pick of one letter in each row spells a word. The page cannot see the pupil's drawing: it checks that the pupil can tell which printed half matches the figure."),
             seed=3434)
    # independent solver: read the thick edges of the drawn model and options back from the svg text
    solved = ""
    for i, f in enumerate(figs):
        Rm = {e for e in read_edges(model_svgs[i], cell_big, 0) if all(p[0] >= 3 for p in e)}
        hit = [s for s in range(3) if read_edges(opt_svgs[i][s], cell_opt, 3) == Rm]
        assert len(hit) == 1
        solved += letters[i][hit[0]]
    P.v("V1 independent reader: exactly one printed right half matches the right half of each drawn figure (edges read back from the drawings); its letters spell the code word", solved == word, solved)
    P.v("V1b the three options of every figure are all different", all(len({frozenset(read_edges(o, cell_opt, 3)) for o in os_}) == 3 for os_ in opt_svgs))
    P.v("V1c the copy grid shows exactly the left half of the figure (the edges up to column 3)", all(read_edges(copy_svgs[i], cell_big, 0) == edges_left(f["E"]) for i, f in enumerate(figs)))
    n_combo = 3 ** NF - 1
    P.v(f"V3 none of the {n_combo} wrong picks (one option per figure) spells a word (large word list)", not bad, bad[:3])
    P.v("V3d the code word's letters have exactly ONE arrangement that is a word", anagrams(word) == [word.lower()], anagrams(word))
    P.v("V4 guess resistance: twelve letters shown, 3 per figure; shorter common words can be spelt from them", len(small_words("".join(sum(letters, [])))) >= 3)
    P["cv"] = dict(rate=1.0, single_total=n_combo, single_detected=n_combo)
    P["model"] = dict(truth=list(word), domains=[sorted(letters[i]) for i in range(NF)], check=letters_check(), numeric=False)
    P["facts"] = "3 4"
    return P


# ---------------------------------------------------------------- picture graph helpers (N21, N22)
def icon_small(kind, mm=9):
    return ('<svg class="gicon" xmlns="http://www.w3.org/2000/svg" width="%smm" height="%smm" viewBox="0 0 20 20">%s</svg>' % (mm, mm, art.OBJ_PATHS[kind]))

def star_symbol(mm=10.5):
    return ('<svg class="sym" xmlns="http://www.w3.org/2000/svg" width="%smm" height="%smm" viewBox="0 0 20 20"><polygon points="10,1.5 12.4,7.4 18.7,7.8 13.8,11.8 15.4,18 10,14.6 4.6,18 6.2,11.8 1.3,7.8 7.6,7.4" fill="#fff" stroke="#000" stroke-width="1.1" stroke-linejoin="round"/></svg>' % (mm, mm))

def graph_rows(rows, symbol, shown=None, small=False):
    """rows: list of (label, kind, count); shown: set of labels whose symbols are drawn (None = all). A row not shown has empty boxes."""
    out = ""
    for lab, kind, n in rows:
        cells = "".join(f'<span class="gc">{symbol if (shown is None or lab in shown) and k < n else ""}</span>' for k in range(9))
        out += f'<div class="grow2" data-row="{lab}"><b class="gl">{icon_small(kind)}<span>{lab}</span></b>{cells}</div>'
    return f'<div class="pgraph{" sm" if small else ""}">{out}</div>'

def read_graph(h):
    """independent reader: counts of drawn symbols per row label"""
    out = {}
    for m in re.finditer(r'<div class="grow2" data-row="([^"]+)">(.*?)</div>(?=<div class="grow2"|</div>)', h, re.S):
        out[m.group(1)] = len(re.findall(r'class="(?:face|sym)"', m.group(2)))
    return out

PET_KINDS = [("Cat", "cat"), ("Dog", "dog"), ("Rabbit", "rabbit"), ("Fish", "fish"), ("Bird", "bird"), ("Turtle", "turtle")]

# ---------------------------------------------------------------- N21 Read the Picture Graph (P1-35)
def page35():
    rng = random.Random(3535)
    word = "TURKEY"
    while True:
        pets = rng.sample(PET_KINDS, 5); vals = rng.sample(range(1, 10), 5)
        rows = [(n, k, v) for (n, k), v in zip(pets, vals)]
        cnt = {n: v for n, k, v in rows}; names = [n for n, k, v in rows]
        most = max(cnt, key=cnt.get); least = min(cnt, key=cnt.get)
        rest = [n for n in names]
        x = rng.choice(names); y, z = rng.sample([n for n in names if n != x], 2)
        a, b = rng.sample(names, 2)
        if cnt[a] - cnt[b] < 2: a, b = b, a
        if cnt[a] - cnt[b] < 2: continue
        total = sum(vals)
        ans = [most, least, str(cnt[x]), str(cnt[y] + cnt[z]), str(cnt[a] - cnt[b]), str(total)]
        if len(set(ans)) != 6: continue
        nums = [str(i) for i in range(0, 46)]
        domain = names + [p for p, _ in PET_KINDS if p not in names] + nums
        domain = list(dict.fromkeys(domain))
        pool = [n for n in names if n not in ans] + [str(v) for v in set(vals) | {cnt[y], cnt[z]} | {cnt[a], cnt[b]} if str(v) not in ans] + [str(int(t) + d) for t in ans if t.isdigit() for d in (1, -1) if str(int(t) + d) not in ans and int(t) + d > 0]
        pool = list(dict.fromkeys(pool))
        table = make_code_table(ans, word, rng, 0, 0, n_decoy=4, tries=300, pool=pool, domain=domain)
        if table: break
    order = sorted([k for k in table if k.isdigit()], key=int) + sorted(k for k in table if not k.isdigit())
    tab = {k: table[k] for k in order}
    face = face_svg(8)
    g = graph_rows(rows, face, small=True)
    qs = [("Which pet got the most votes?", None), ("Which pet got the fewest votes?", None), (f"How many children chose {x}?", None),
          (f"How many chose {y} and {z} in all?", None), (f"How many more chose {a} than {b}?", None), ("How many children chose in all?", None)]
    qrows = "".join(f'<div class="qrow"><span class="no">{i+1}</span><span class="qt">{q}</span><span class="ab"></span></div>' for i, (q, _) in enumerate(qs))
    body = (f'<div class="blk"><p class="lead">Children chose a pet. {face_svg(6)} = 1 child.</p>{g}</div><div class="qgrid">{qrows}</div>{code_block(tab)}')
    P = Page(no=35, title="Read the Picture Graph", tier=1, topic="Picture graphs: read the graph and answer questions",
             strand="Statistics - Data Representation and Interpretation", syll="Statistics 1.1 (reading and interpreting data from picture graphs; one picture stands for one child)",
             ptype="Code-breaker (picture graph)", mech="K1 code word (6 letters)",
             instr=["Look at the picture graph.", "Answer each question.", "Use the code table."],
             body=body, check="Write the letters in order. Do they spell a word?", check_boxes=6,
             key=dict(answers=", ".join(f"{i+1}) {ans[i]}" for i in range(6)), check_result=f"Code word: {word}"),
             note=("A finished graph with one face for one child (never a scale) and five rows. Two questions ask which pet (most, fewest) and four ask for a number: one row, two rows together, how many more, and the total. "
                   "The code table has pet names and numbers, so a pupil who writes a number where a pet is wanted gets no letter. The total of all rows is read from the graph, not given."),
             seed=3535)
    got = read_graph(g)
    sol = [max(got, key=got.get), min(got, key=got.get), str(got[x]), str(got[y] + got[z]), str(got[a] - got[b]), str(sum(got.values()))]
    P.v("V1 independent reader: symbols counted in each drawn row answer all six questions and equal the key", sol == ans, sol)
    P.v("V1b every row has a different number of symbols (0 to 9), so most and fewest are unique; 4 to 6 rows", len(set(got.values())) == 5 and max(got.values()) <= 9)
    P.v("V1c answers distinct; two are pet names and four are numbers", len(set(ans)) == 6 and sum(not t.isdigit() for t in ans) == 2)
    finish_code(P, ans, table, word, 0, 0, domain)
    P["model"] = dict(truth=ans, domains=[domain] * 6, check=code_check(table), numeric=False)
    P["facts"] = " ".join(str(i) for i in range(0, 46))
    return P

# ---------------------------------------------------------------- N22 Graph Detective Two (P1-36)
TOYS = [("Kite", "kite"), ("Ball", "ball"), ("Drum", "drum"), ("Car", "car"), ("Boat", "boat"), ("Cup", "cup")]

def page36():
    rng = random.Random(3636)
    star = star_symbol(10.5)
    while True:
        toys = rng.sample(TOYS, 5); names = [t[0] for t in toys]
        K1, K2, U1, U2, U3 = names
        k1, k2 = rng.randint(2, 7), rng.randint(2, 7)
        u1 = k1                                           # same as K1
        u2 = rng.randint(1, 8 - 1); S = u2 + k2           # U2 and K2 have S in all
        d = rng.randint(1, 3); sign = rng.choice(["more", "less"])
        u3 = u2 + d if sign == "more" else u2 - d
        cnt = {K1: k1, K2: k2, U1: u1, U2: u2, U3: u3}
        if min(cnt.values()) < 1 or max(cnt.values()) > 9 or S > 14: continue
        vals = sorted(cnt.values())
        if vals[-1] == vals[-2] or u1 == u2 or u3 == u1: continue
        total = sum(cnt.values())
        most = max(cnt, key=cnt.get)
        others = [n for n in names if n != most]
        pairs_ = [(x, y) for x in others for y in others if x != y and cnt[x] - cnt[y] >= 2]
        if not pairs_: continue
        xb, yb = rng.choice(pairs_); bans = cnt[xb] - cnt[yb]; comb = cnt[most] + bans
        clues = [("same", U1, K1), ("pair", U2, K2, S), (sign, U3, U2, d)]
        # every misreading of the three clues (three readings each): the pupil's graph must fail the total or the second sum
        rd1 = [k1, k2, d]; rd2 = [S - k2, S, S - k1]; rd3 = [(u2 + d if sign == "more" else u2 - d), (u2 - d if sign == "more" else u2 + d), d]
        ok = True; n_mis = 0
        for i1, v1 in enumerate(rd1):
            for i2, v2 in enumerate(rd2):
                for i3, v3 in enumerate(rd3):
                    if (i1, i2, i3) == (0, 0, 0): continue
                    n_mis += 1
                    # clue 3 is read from the pupil's own U2 (v2) in the flipped readings
                    v3 = (v2 + d if sign == "more" else v2 - d) if i3 == 0 else (v2 - d if sign == "more" else v2 + d) if i3 == 1 else d
                    alt = dict(cnt); alt[U1], alt[U2], alt[U3] = v1, v2, v3
                    if min(alt.values()) < 0 or max(alt.values()) > 9: continue
                    if sum(alt.values()) != total: continue
                    top = max(alt.values())
                    if any(alt[f] == top and alt[f] + (alt[xb] - alt[yb]) == comb for f in alt): ok = False
        if ok: break
    rows = [(n, k, cnt[n]) for n, k in toys if n in cnt]
    rows = [(n, dict(toys)[n], cnt[n]) for n in names]
    g = graph_rows(rows, star, shown={K1, K2})
    ctext = {"same": lambda c: f"{c[1]} has the same as {c[2]}.", "pair": lambda c: f"{c[1]} and {c[2]} have {c[3]} in all.",
             "more": lambda c: f"{c[1]} has {c[3]} more than {c[2]}.", "less": lambda c: f"{c[1]} has {c[3]} fewer than {c[2]}."}
    clue_html = "".join(f"<li>{ctext[c[0]](c)}</li>" for c in clues)
    body = (f'<div class="blk"><p class="lead">Children chose a toy. {star_symbol(6)} = 1 child. Draw a star.</p>{g}</div><ul class="clues">{clue_html}</ul>'
            f'<div class="ansline">a) Most children chose <span class="ab wide"></span>.</div><div class="ansline">b) <b>{xb}</b> has <span class="ab"></span> more than <b>{yb}</b>.</div>')
    chk = [f"Count all the stars. Is the total {total}?", f"Add the stars in your a) row to your b) answer. Is the sum {comb}?"]
    P = Page(no=36, title="Graph Detective Two", tier=2, topic="Picture graphs: read, complete and answer from clues",
             strand="Statistics - Data Representation and Interpretation", syll="Statistics 1.1 (reading and interpreting data from picture graphs; completing a graph from clues)",
             ptype="Graph detective", mech="K3 the total of all stars, and a second sum that uses the answers to a) and b) (neither is a clue)",
             mech_plain="Two sums: the total of all the stars, and the row chosen in a) plus the answer to b) (neither is used to find any row)",
             instr=["Two rows are done.", "Draw one star for each child.", "Use the clues. Answer a and b."],
             body=body, check=" ".join(chk), check_lines=chk, check_boxes=None,
             key=dict(answers=", ".join(f"{n}: {cnt[n]}" for n in names) + f"; a) {most}; b) {bans}", check_result=f"Total {total} stars; second sum {cnt[most]} + {bans} = {comb}"),
             note=(f"Each star stands for one child (one picture for one child, no scale). Two rows are drawn and three are found from three clues: one says two rows have the same, one gives the total of two rows, and one gives a difference between two rows. "
                   f"The total of {total} is printed only in the check strip, so it is a separate test, not a clue. The second sum tests the answers to a) and b). "
                   f"All the ways of misreading the three clues (the wrong row used, the total read as one row, more and fewer exchanged) were tried; every one fails the total or the second sum."),
             seed=3636)
    # solver: brute force over the three unknown rows from the printed clues only
    got = read_graph(g)
    known = {n: got[n] for n in (K1, K2)}
    def clue_ok(c, v):
        if c[0] == "same": return v[c[1]] == v[c[2]]
        if c[0] == "pair": return v[c[1]] + v[c[2]] == c[3]
        if c[0] == "more": return v[c[1]] == v[c[2]] + c[3]
        return v[c[1]] == v[c[2]] - c[3]
    sols = []
    for t in itertools.product(range(0, 10), repeat=3):
        v = dict(known); v.update(zip((U1, U2, U3), t))
        if all(clue_ok(c, v) for c in clues): sols.append(v)
    P.v("V1 exactly one set of row counts satisfies the printed clues (total not used; all 1000 combinations tested)", len(sols) == 1 and sols[0] == cnt, len(sols))
    P.v("V1b the most answer is unique, the total is not a clue, b) does not name the fruit that answers a)", sorted(cnt.values())[-1] != sorted(cnt.values())[-2] and all(c[0] != "total" for c in clues) and most not in (xb, yb))
    P.v("V2 total and second sum are right for the right answers", sum(cnt.values()) == total and cnt[most] + bans == comb)
    P.v("V3f every misreading of the three clues (%d readings) fails the total or the second sum" % n_mis, ok)
    unk = [U1, U2, U3]
    def chkf(ans):
        r1, r2, r3, fa, nb = ans
        c2 = dict(cnt); c2.update(dict(zip(unk, (r1, r2, r3))))
        return sum(c2.values()) == total and c2[fa] + nb == comb
    tot = det = 0
    for f_ in unk:
        for dl in (-2, -1, 1, 2):
            tot += 1; alt = dict(cnt); alt[f_] += dl; det += sum(alt.values()) != total
    P.v("V3 one wrong row breaks the total", det == tot, f"{det}/{tot}")
    P["cv"] = dict(rate=det / tot, single_total=tot, single_detected=det)
    P["model"] = dict(truth=[cnt[u] for u in unk] + [most, bans], domains=[list(range(0, 10))] * 3 + [list(names), list(range(0, 10))], check=chkf, numeric=False)
    P["counts"] = cnt
    P["mini"] = mini_graph([(n, cnt[n]) for n in names])
    return P

PAGES = [page31, page32, page33, page34, page35, page36]
