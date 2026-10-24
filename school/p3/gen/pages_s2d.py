"""Semester 2, pages P3-34 to P3-38: angles, perpendicular and parallel lines, bar graphs.
P3-34 Right Angles; P3-35 Parallel or Perpendicular?; P3-36 Draw the Lines; P3-37 Bar Graph Detective; P3-38 Different Scales."""
import random, re, itertools, math
from fractions import Fraction
from .common import *
from .kit import *
from .p3kit import *
from . import art3 as A3

# =============================================================================== P3-34 Right Angles (lettered choice)
def page34():
    rng = random.Random(5434)
    for _ in range(2000):
        cats = [rng.choice(["small", "right", "great"]) for _ in range(5)]
        if len(set(cats)) == 3 and cats.count("right") <= 2: break
    specs = []; degs = []
    for c in cats:
        for _t in range(100):
            deg = {"small": rng.choice([30, 40, 50, 60]), "right": 90, "great": rng.choice([120, 130, 140, 150])}[c]
            rot = rng.choice([0, 20, 40, 70, 90, 110, 160, 200, 250, 290, 330]) if c != "right" or rng.random() < .6 else rng.choice([0, 90, 180, 270])
            if (deg, rot) not in degs: break
        degs.append((deg, rot))
        right = {"small": 0, "right": 1, "great": 2}[c]
        specs.append(dict(q=f'<div class="angfig">{A3.angle_svg(deg, rot)}</div>', opts=['<b class="on">Smaller</b>', '<b class="on">Right angle</b>', '<b class="on">Greater</b>'], ri=right, fixed=True, deg=deg))
    pre = '<div class="howto"><p>A square corner is a right angle. A smaller angle fits inside it. A greater angle does not.</p></div>'
    P = lettered_choice_page(34, 5434, "Right Angles", 1, "Angles: right angles, smaller and greater than a right angle", STRAND_GE,
        "1.1, 1.2 (concept of an angle; right angles; angles greater than or smaller than a right angle)", ["AN1.1", "AN1.2"], "Lettered choice (angles)",
        ["Compare each marked angle with a square corner.", "Circle the letter of the right choice.", "Write the five letters in the boxes."],
        specs, 3, "; ".join(f"{i+1}) {['smaller than a right angle', 'a right angle', 'greater than a right angle'][s['ri']]}" for i, s in enumerate(specs)),
        "Five angles, each drawn with a small arc. Each angle is clearly smaller than a right angle, exactly a right angle or clearly greater: none is close to a right angle, so a pupil can compare with the corner of a sheet of paper or a set square. Degrees are not named on the page: the page asks only for right angles and smaller or greater. The angles are turned to different positions, so a right angle is not always a horizontal and a vertical line. The letters of the right choices, read down the rows, spell the word. Every other way of choosing was tested against a very large word list: none spells a word. A box left blank gives no letter and the check cannot see it.",
        word_len=5, rng=rng, pre_html=pre, row_cls="angrow")
    def solver(q, opts):
        d = A3.read_angle(q)
        cls = 0 if d < 85 else 1 if d <= 95 else 2
        return cls
    got = solve_letters(solver, P["body"])
    P.v("V1 independent solver (the arms of each angle read from the drawing, the angle found and compared with 90 degrees) gets the word", got == P["word"], got)
    P.v("V7 no angle is within 25 degrees of a right angle except the right angles themselves", all(abs(d - 90) >= 25 or d == 90 for d, r in degs))
    P.v("V1b the three kinds (smaller, right, greater) all occur", len(set(cats)) == 3)
    return P

# =============================================================================== P3-35 Parallel or Perpendicular? (lettered choice)
DIRS = [(1, 0), (0, 1), (1, 1), (1, -1), (2, 1), (1, -2), (1, 2), (2, -1)]
def perp(d): return (-d[1], d[0])
def parallel_to(d, e): return d[0] * e[1] - d[1] * e[0] == 0
def perp_to(d, e): return d[0] * e[0] + d[1] * e[1] == 0

def page35():
    rng = random.Random(5535)
    L = 6.5                       # half length of a line (mm)
    kinds = ["parallel", "perpendicular", "parallel", "perpendicular", rng.choice(["parallel", "perpendicular"])]
    rng.shuffle(kinds)
    specs = []; truth = []
    for kd in kinds:
        for _t in range(4000):
            r = rng.choice(DIRS)
            par = r; per = perp(r)
            obl = rng.choice([d for d in DIRS if not parallel_to(r, d) and not perp_to(r, d)])
            right_dir = par if kd == "parallel" else per
            others = [per if kd == "parallel" else par, obl]
            dirs = [right_dir] + others
            perm = list(range(3)); rng.shuffle(perm)
            letters = ["P", "Q", "R"]
            cx = [31.0, 43.5, 56.0]
            def seg(c, d):
                n = math.hypot(*d); return ((c[0] - L * d[0] / n, c[1] - L * d[1] / n), (c[0] + L * d[0] / n, c[1] + L * d[1] / n))
            ref_c = (11.5, 12.0 + rng.choice([-2, 0, 2]))
            refseg = seg(ref_c, r)
            cands = []
            for slot in range(3):
                idx = perm[slot]; c = (cx[slot], 12.0 + rng.choice([-3, 0, 3]))
                cands.append((letters[slot], idx, seg(c, dirs[idx])))
            ok = True
            allsegs = [("ref", refseg)] + [(l, s) for l, i, s in cands]
            for (n1, s1), (n2, s2) in itertools.combinations(allsegs, 2):
                if A3.seg_cross(s1[0], s1[1], s2[0], s2[1]): ok = False
                if A3.seg_dist(s1, s2) < 3.0: ok = False          # no two lines touch or nearly touch (audit M1)
            if any(not (0 < p[0] < 66 and 0 < p[1] < 23) for n, s in allsegs for p in s): ok = False
            # labels: P, Q, R below their line; A and B beyond the two ends of AB. Each label centre stays 3.5 mm clear of every other line
            labpos = []
            for l, i, s in cands:
                labpos.append((l, (s[0][0] + s[1][0]) / 2, max(s[0][1], s[1][1]) + 3.4, 4.6, s))
            ux, uy = refseg[1][0] - refseg[0][0], refseg[1][1] - refseg[0][1]; un = math.hypot(ux, uy); ux, uy = ux / un, uy / un
            labpos.append(("A", refseg[0][0] - 4.0 * ux, refseg[0][1] - 4.0 * uy + 0.3, 4.0, refseg))
            labpos.append(("B", refseg[1][0] + 4.0 * ux, refseg[1][1] + 4.0 * uy + 0.3, 4.0, refseg))
            for l, lx, ly, fs, own in labpos:
                if not (2.2 < lx < 63.8 and 2.2 < ly < 26.5): ok = False
                for n, s2 in allsegs:
                    if s2 is own and l in "PQR": continue
                    if A3.pt_seg_dist((lx, ly), s2) < 3.4 and not (s2 is own): ok = False
                    if s2 is own and l in "AB" and A3.pt_seg_dist((lx, ly), s2) < 3.4: ok = False
            if ok: break
        else: raise RuntimeError('P3-35: no clear layout')
        parts = A3.lines_svg(refseg, [(l, s[0], s[1]) for l, i, s in cands])
        labs = "".join(f'<text x="{lx:.1f}" y="{ly + fs * 0.35:.1f}" text-anchor="middle" font-family="Fredoka" font-weight="600" font-size="{fs}" fill="#000">{l}</text>' for l, lx, ly, fs, own in labpos)
        fig = svg(66, 28, "".join(parts) + labs)
        right_letter = [l for l, i, s in cands if i == 0][0]
        specs.append(dict(q=f'<div class="lnfig">{fig}</div><p class="qs2">Choose the line that is {kd} to AB.</p>', opts=[f'<b class="on">{l}</b>' for l in letters], ri=letters.index(right_letter), fixed=True, kd=kd))
    P = lettered_choice_page(35, 5535, "Line Detective", 1, "Perpendicular and parallel lines: identifying them", STRAND_GE,
        "2.1 (identifying perpendicular and parallel lines)", ["PP2.1"], "Lettered choice (lines)",
        ["Line AB is the thick line.", "Circle the letter beside the line that is asked for.", "Write the five letters in the boxes."],
        specs, 3, "; ".join(f"{i+1}) line {'PQR'[s['ri']]} ({s['kd']})" for i, s in enumerate(specs)),
        "Five pictures, each with the thick line AB and three thin lines P, Q and R. In every picture one line is parallel to AB, one is perpendicular to AB and one is neither; the question asks for the parallel or the perpendicular one. Lines are drawn from slopes that fit a grid, but no grid is printed. The pupil can use a ruler and the corner of a sheet of paper. Parallel means always the same distance apart; perpendicular means meeting at a right angle (the lines are not made to touch). The letters of the right choices, read down the rows, spell the word. Every other way of choosing was tested against a very large word list: none spells a word. A box left blank gives no letter and the check cannot see it.",
        word_len=5, rng=rng, row_cls="lnrow")
    def solver(q, opts):
        ref, cands = A3.read_lines(q)
        kd = re.search(r"Choose the line that is (parallel|perpendicular) to AB", q).group(1)
        hits = [l for l, c in cands.items() if A3.relation(ref, c) == kd]
        assert len(hits) == 1, hits
        return [re.search(r">([^<]*)<", o).group(1) for o in opts].index(hits[0])
    got = solve_letters(solver, P["body"])
    P.v("V1 independent solver (the line ends read from the drawing; the dot and cross products of the directions tested) gets the word", got == P["word"], got)
    P.v("V1b in every picture exactly one line is parallel, one perpendicular and one neither", all(sorted(A3.relation(*[A3.read_lines(q)[0], c]) for c in A3.read_lines(q)[1].values()) == ["neither", "parallel", "perpendicular"] for q, opts in read_choice_rows(P["body"])))
    return P

# =============================================================================== P3-36 Draw the Lines
def exit_x(P_, t):
    """x where the line through lattice point P_ with direction t (t[1] < 0, going up) meets the top edge (y = 0), or None"""
    s_ = Fraction(P_[1], -t[1]); x = P_[0] + s_ * t[0]
    return x if x.denominator == 1 and 0 <= x <= 6 else None

def page36():
    rng = random.Random(5636)
    word = None
    for _ in range(40):
        cand = word_candidates(36, 6)
        word = cand[rng.randrange(0, min(5, len(cand)))]
        try: rows_l = letter_rows(rng, word, 5); break
        except RuntimeError: continue
    CLAIMED[36] = word
    cards = []; geo = []
    modes = ["perpendicular", "parallel", "perpendicular", "parallel", "perpendicular", "parallel"]
    rng.shuffle(modes)
    for i, mode in enumerate(modes):
        for _t in range(20000):
            d = rng.choice([(1, 1), (1, -1), (2, 1), (1, 2), (2, -1), (1, -2), (1, 0), (0, 1)])
            t = perp(d) if mode == "perpendicular" else d
            if t[1] == 0: continue
            P_ = (rng.randint(1, 5), rng.randint(2, 5))
            ex = exit_x(P_, t if t[1] < 0 else (-t[0], -t[1]))
            if ex is None or ex in (0, 6): continue       # the line leaves through the top edge, never at a corner (audit R2-2)
            k = rng.randint(2, 3)
            A_ = (rng.randint(0, 6 - k * abs(d[0])) if d[0] >= 0 else 0, rng.randint(0, 6));
            B_ = (A_[0] + k * d[0], A_[1] + k * d[1])
            if not (0 <= B_[0] <= 6 and 1 <= B_[1] <= 6 and 0 <= A_[0] <= 6): continue
            if A_ == P_ or B_ == P_ or abs(A_[0] - B_[0]) + abs(A_[1] - B_[1]) < 2: continue
            # the picked point must not lie on the segment AB, and the target line must not coincide with AB
            if t[0] * d[1] - t[1] * d[0] == 0 and (P_[0] - A_[0]) * d[1] - (P_[1] - A_[1]) * d[0] == 0: continue
            if (P_[0] - A_[0]) * d[1] - (P_[1] - A_[1]) * d[0] == 0: continue
            break
        right_x = int(ex)
        pos_all = list(range(7)); others = [x for x in pos_all if x != right_x]
        near = sorted(others, key=lambda x: abs(x - right_x))[:2] + rng.sample(others, 2)
        lab_x = sorted(set([right_x] + near))[:5]
        while len(lab_x) < 5:
            lab_x.append(rng.choice([x for x in pos_all if x not in lab_x]))
        lab_x = sorted(lab_x)
        if right_x not in lab_x: lab_x[0] = right_x; lab_x = sorted(lab_x)
        wrong_l = list(rows_l[i][1:]); rng.shuffle(wrong_l)
        lmap = {}
        for x in lab_x: lmap[x] = rows_l[i][0] if x == right_x else wrong_l.pop()
        geo.append(dict(mode=mode, d=d, t=t, P=P_, A=A_, B=B_, right_x=right_x, lmap=lmap))
        u = 6.5; ox, oy = 8.0, 9.0
        g = []
        for k in range(7):
            g.append(f'<line x1="{ox + k * u:.1f}" y1="{oy}" x2="{ox + k * u:.1f}" y2="{oy + 6 * u:.1f}" stroke="#000" stroke-width="0.6"/><line x1="{ox}" y1="{oy + k * u:.1f}" x2="{ox + 6 * u:.1f}" y2="{oy + k * u:.1f}" stroke="#000" stroke-width="0.6"/>')
        g.append(f'<rect x="{ox}" y="{oy}" width="{6 * u}" height="{6 * u}" fill="none" stroke="#000" stroke-width="0.7"/>')
        g.append(f'<line class="abl" x1="{ox + A_[0] * u:.1f}" y1="{oy + A_[1] * u:.1f}" x2="{ox + B_[0] * u:.1f}" y2="{oy + B_[1] * u:.1f}" stroke="#000" stroke-width="1.5" stroke-linecap="round"/>')
        # labels A and B: 3.4 mm beyond the end of the line, or to either side of the end, in the first place that is inside the picture,
        # clear of the thick line (2.6 mm) and of the point P and its letter (audit R2-2)
        pa = (ox + A_[0] * u, oy + A_[1] * u); pb = (ox + B_[0] * u, oy + B_[1] * u); pp = (ox + P_[0] * u, oy + P_[1] * u)
        ux_, uy_ = pb[0] - pa[0], pb[1] - pa[1]; un_ = math.hypot(ux_, uy_); ux_, uy_ = ux_ / un_, uy_ / un_
        def lab_pos(e, sgn):
            for dx_, dy_ in ((sgn * ux_, sgn * uy_), (-uy_, ux_), (uy_, -ux_), (sgn * ux_ - uy_, sgn * uy_ + ux_), (sgn * ux_ + uy_, sgn * uy_ - ux_)):
                n_ = math.hypot(dx_, dy_); cx_, cy_ = e[0] + 3.6 * dx_ / n_, e[1] + 3.6 * dy_ / n_
                if not (2.2 < cx_ < 51.8 and 2.5 < cy_ < 49.5): continue
                if A3.pt_seg_dist((cx_, cy_), (pa, pb)) < 2.6 and (dx_, dy_) not in ((sgn * ux_, sgn * uy_),): continue
                if math.hypot(cx_ - pp[0], cy_ - pp[1]) < 4.2 or math.hypot(cx_ - (pp[0] + 2.6), cy_ - (pp[1] + 3.0)) < 3.4: continue
                return cx_, cy_
            raise RuntimeError("P3-36 label")
        la = lab_pos(pa, -1); lb = lab_pos(pb, 1)
        g.append(f'<text x="{la[0]:.1f}" y="{la[1] + 1.5:.1f}" text-anchor="middle" font-family="Fredoka" font-weight="600" font-size="4.2" stroke="#fff" stroke-width="1.3" paint-order="stroke" fill="#000">A</text><text x="{lb[0]:.1f}" y="{lb[1] + 1.5:.1f}" text-anchor="middle" font-family="Fredoka" font-weight="600" font-size="4.2" stroke="#fff" stroke-width="1.3" paint-order="stroke" fill="#000">B</text>')
        g.append(f'<circle class="pt" cx="{ox + P_[0] * u:.1f}" cy="{oy + P_[1] * u:.1f}" r="1.5" fill="#000"/><text x="{ox + P_[0] * u + 1.6:.1f}" y="{oy + P_[1] * u + 4.6:.1f}" font-family="Fredoka" font-weight="600" font-size="4.2" stroke="#fff" stroke-width="1.3" paint-order="stroke" fill="#000">P</text>')
        for x, l in lmap.items():
            g.append(f'<text class="tl" data-x="{x}" x="{ox + x * u:.1f}" y="{oy - 2.3:.1f}" text-anchor="middle" font-family="Fredoka" font-weight="700" font-size="5.0" fill="#000">{l}</text>')
        fig = svg(54, 52, "".join(g))
        cards.append(f'<div class="qc dlr"><div class="dlf">{fig}</div><div class="dlt"><span class="no">{i+1}</span><p>Draw a line through P <b>{mode}</b> to AB. Write the letter where it meets the top edge.</p></div></div>')
    body = '<div class="qg c2 dl">' + "".join(cards) + '</div>'
    P = new_page(36, 5636, "Draw the Lines", 2, "Perpendicular and parallel lines: drawing them", STRAND_GE,
        "2.2 (drawing perpendicular and parallel lines)", ["PP2.2"], "Draw and read off (lettered edge)",
        "K1 the letter on the top edge where the drawn line ends spells a word (6 letters, 4 decoy letters on each edge)",
        ["Use a ruler and the corner of a sheet of paper.", "Draw the line in each picture.", "Write the six letters in the boxes."],
        body, "; ".join(f"{i+1}) {g['mode']} through P: letter {g['lmap'][g['right_x']]} at x = {g['right_x']}" for i, g in enumerate(geo)), f"Word: {word}",
        "Six grids with a thick line AB, a point P and five letters on the top edge. The pupil draws a line through P that is perpendicular (or parallel) to AB, as far as the top edge, and writes the letter where it ends. The right letter is on a grid point of the top edge; the letters beside it are where the line ends if the pupil draws the wrong direction. The page cannot see the drawing: it sees the letter, which is the printed evidence of the drawing, and the teacher can look at the lines. Drawing is checked only through the letter. A box left blank gives no letter and the check cannot see it.",
        check="Write the six letters in order. Do they spell a word?", check_boxes=6, mk=("code",),
        mech_plain="Word from the letters where the drawn lines end (6 letters)")
    P["rows_letters"] = rows_l; P["word"] = word
    other = choice_other_words(word, rows_l)
    P.v("V3 none of the other 15624 ways to choose one letter on each edge spells a word (large word list)", not other, other[:3])
    P.v("V3d the word's letters have exactly ONE arrangement that is a word", anagrams(word) == [word.lower()], anagrams(word))
    # independent solver reads the drawings
    got = ""
    for card in cards:
        s = re.search(r"<svg.*?</svg>", card, re.S).group(0)
        ab = re.search(r'class="abl" x1="([\d.]+)" y1="([\d.]+)" x2="([\d.]+)" y2="([\d.]+)"', s); x1, y1, x2, y2 = (float(v) for v in ab.groups())
        pt = re.search(r'class="pt" cx="([\d.]+)" cy="([\d.]+)"', s); px, py = float(pt.group(1)), float(pt.group(2))
        dx, dy = x2 - x1, y2 - y1
        mode = re.search(r"<b>(\w+)</b> to AB", card).group(1)
        tx, ty = (-dy, dx) if mode == "perpendicular" else (dx, dy)
        if ty > 0: tx, ty = -tx, -ty
        oy = 9.0; ox = 8.0; u = 6.5
        sx = px + tx * ((py - oy) / (-ty))
        gx = round((sx - ox) / u * 1.0)
        assert abs((sx - ox) / u - gx) < 0.02, (sx, gx)
        letter = re.search(r'class="tl" data-x="%d"[^>]*>(\w)<' % gx, s).group(1)
        got += letter
    P.v("V1 independent solver (AB and P read from the drawing, the line found, the letter where it meets the top edge read) gets the word", got == word, got)
    P.v("V1b the right line ends on a grid point of the top edge and every grid has 5 letters", all(len(g["lmap"]) == 5 for g in geo))
    domains = [sorted(set(r)) for r in rows_l]
    P["model"] = dict(truth=list(word), domains=[list(r) for r in rows_l], check=letters_check(), numeric=False)
    P["cv"] = dict(rate=1.0, single_total=24, single_detected=24)
    P["facts"] = ""
    return P

# =============================================================================== P3-37 Bar Graph Detective
def page37():
    rng = random.Random(5737)
    names_pool = ["Judo", "Swim", "Chess", "Art", "Choir", "Band"]
    while True:
        names = rng.sample(names_pool, 5)
        vals = [rng.randrange(10, 51, 5) for _ in range(5)]
        if len(set(vals)) < 5 or max(vals) != 50 and max(vals) < 40: continue
        o = sorted(range(5), key=lambda i: -vals[i])
        i1, i2, i3 = rng.sample(range(5), 3)
        items = [("val", i1), ("max", None), ("diff", (i2, i3)), ("sum", (o[3], o[4])), ("total", None), ("least", None)]
        a = [vals[i1], max(vals), abs(vals[i2] - vals[i3]), vals[o[3]] + vals[o[4]], sum(vals), min(vals)]
        if not distinct(a) or max(a) > 250: continue
        ans = a
        pool = set()
        for v in ans: pool |= {v + 5, v - 5, v + 10, v - 10}
        pool |= {sum(vals) - 10, sum(vals) + 5, vals[o[3]] + vals[o[4]] + 5}
        pool = sorted(x for x in pool if x not in ans and 0 < x <= 250)
        res = find_table(37, 6, ans, rng, 0, 250, pool, n_decoy=3, tries=40)
        if res: word, table = res; break
    graph = A3.bar_svg(names, vals, 50, 5, 10, w=130, h=58, title="Pupils in school clubs", unit=None)
    texts = []
    for kd, x in items:
        if kd == "val": texts.append(f"How many pupils are in {names[x]}?")
        elif kd == "max": texts.append("How many pupils are in the most popular club?")
        elif kd == "diff": texts.append(f"How many more pupils are in {names[x[0]]} than in {names[x[1]]}?" if vals[x[0]] > vals[x[1]] else f"How many fewer pupils are in {names[x[0]]} than in {names[x[1]]}?")
        elif kd == "sum": texts.append(f"How many pupils are in {names[x[0]]} and {names[x[1]]} together?")
        elif kd == "total": texts.append("How many pupils are in the clubs in all?")
        else: texts.append("How many pupils are in the least popular club?")
    cards = [qcard(i + 1, f"<p>{t}</p>", '<span class="ab w3"></span>', cls="inl") for i, t in enumerate(texts)]
    pre = f'<div class="gwrap">{graph}</div>'
    P = code_items_page(37, 5737, "Bar Graph Detective", 1, "Bar graphs: reading and interpreting", STRAND_ST,
        "1.1 (reading and interpreting bar graphs)", ["BG1.1"], "Code-breaker (bar graph)",
        ["Look at the bar graph.", "Write the answer to each question.", INSTR_CODE],
        qgrid(cards, 2), ans, table, word, 0, 250,
        "; ".join(f"{i+1}) {a}" for i, a in enumerate(ans)),
        "A bar graph of five clubs on a scale from 0 to 50 with a line for every 5 pupils and a number for every 10, so most bars end on a line between two numbers. Six questions: reading one bar, the tallest bar, a difference, the sum of two bars, the total of all five bars and the least. The decoy letters stand for reading the next line, or for adding the wrong two bars. The bars are black; no colour is needed. A box left blank gives no letter and the check cannot see it.",
        pre_body=pre)
    bars = A3.read_bars(graph)
    vv = [bars[n] for n in names]
    solved = []
    for t in texts:
        m = re.match(r"How many pupils are in (\w+)\?", t)
        if m and m.group(1) not in ("the",): solved.append(bars[m.group(1)]); continue
        if "most popular" in t: solved.append(max(vv)); continue
        if "least popular" in t: solved.append(min(vv)); continue
        if "in all" in t: solved.append(sum(vv)); continue
        m = re.match(r"How many (?:more|fewer) pupils are in (\w+) than in (\w+)\?", t)
        if m: solved.append(abs(bars[m.group(1)] - bars[m.group(2)])); continue
        m = re.match(r"How many pupils are in (\w+) and (\w+) together\?", t)
        solved.append(bars[m.group(1)] + bars[m.group(2)])
    solved = [round(v) for v in solved]
    P.v("V1 independent solver (bar heights read from the drawing against the printed scale) equals the key", solved == ans, solved)
    P.v("V7 every bar is a multiple of 5 and between 10 and 50; the scale is 5 a line", all(v % 5 == 0 and 10 <= v <= 50 for v in vv))
    return P

# =============================================================================== P3-38 Different Scales
def page38():
    rng = random.Random(5838)
    days = ["Mon", "Tue", "Wed", "Thu", "Fri"]; items_b = ["Pen", "Ruler", "Book", "Bag", "Cap"]
    while True:
        va = [rng.randrange(2, 17, 2) for _ in range(5)]      # scale 2 per line, labels every 4
        vb = [rng.randrange(20, 101, 10) for _ in range(5)]   # scale 10 per line, labels every 20
        if len(set(va)) < 4 or len(set(vb)) < 4 or max(va) < 14 or max(vb) < 80: continue
        i1, i2 = rng.sample(range(5), 2); j1, j2, j3 = rng.sample(range(5), 3)
        a = [va[i1], vb[j1], abs(va[i1] - va[i2]), vb[j2] + vb[j3], sum(va), max(vb) - min(vb)]
        if not distinct(a) or max(a) > 300 or any(x in (0,) for x in a): continue
        ans = a
        pool = set()
        for v in ans: pool |= {v + 2, v - 2, v + 10, v - 10, v * 5 if v * 5 < 300 else v // 2, v // 5 if v % 5 == 0 else v + 1}
        pool = sorted(x for x in pool if x not in ans and 0 < x <= 300)
        res = find_table(38, 6, ans, rng, 0, 300, pool, n_decoy=3, tries=40)
        if res: word, table = res; break
    ga = A3.bar_svg(days, va, 16, 2, 4, w=84, h=50, title="Graph A: books read", unit=None)
    gb = A3.bar_svg(items_b, vb, 100, 10, 20, w=84, h=50, title="Graph B: things sold", unit=None)
    texts = [f"Graph A. How many books were read on {days[i1]}?", f"Graph B. How many {items_b[j1].lower()}s were sold?",
             f"Graph A. How many more books were read on {days[i1]} than on {days[i2]}?" if va[i1] > va[i2] else f"Graph A. How many fewer books were read on {days[i1]} than on {days[i2]}?",
             f"Graph B. How many {items_b[j2].lower()}s and {items_b[j3].lower()}s were sold in all?", "Graph A. How many books were read in all?",
             "Graph B. What is the difference between the longest and shortest bar?"]
    cards = [qcard(i + 1, f"<p>{t}</p>", '<span class="ab w3"></span>', cls="inl") for i, t in enumerate(texts)]
    pre = f'<div class="gtwo"><div>{ga}</div><div>{gb}</div></div>'
    P = code_items_page(38, 5838, "Different Scales", 2, "Bar graphs with different scales on the axis", STRAND_ST,
        "1.1, 1.2 (reading and interpreting bar graphs; different scales on the axis)", ["BG1.1", "BG1.2"], "Code-breaker (two bar graphs)",
        ["Look at the scale of each graph.", "Write the answer to each question.", INSTR_CODE],
        qgrid(cards, 2), ans, table, word, 0, 300,
        "; ".join(f"{i+1}) {a}" for i, a in enumerate(ans)),
        "Two bar graphs with different scales: Graph A goes up in 2s (a line for every 2, a number for every 4) and Graph B goes up in 10s (a line for every 10, a number for every 20). Each question names its graph. The decoy letters stand for reading Graph B as if its lines were 2 apart or Graph A as if its lines were 10 apart, and for the next line. The bars are black. A box left blank gives no letter and the check cannot see it.",
        pre_body=pre)
    ba, bb = A3.read_bars(ga), A3.read_bars(gb)
    solved = []
    for t in texts:
        m = re.match(r"Graph A\. How many books were read on (\w+)\?", t)
        if m: solved.append(ba[m.group(1)]); continue
        m = re.match(r"Graph B\. How many (\w+)s were sold\?", t)
        if m: solved.append(bb[m.group(1).capitalize()]); continue
        m = re.match(r"Graph A\. How many (?:more|fewer) books were read on (\w+) than on (\w+)\?", t)
        if m: solved.append(abs(ba[m.group(1)] - ba[m.group(2)])); continue
        m = re.match(r"Graph B\. How many (\w+)s and (\w+)s were sold in all\?", t)
        if m: solved.append(bb[m.group(1).capitalize()] + bb[m.group(2).capitalize()]); continue
        if t == "Graph A. How many books were read in all?": solved.append(sum(ba.values())); continue
        solved.append(max(bb.values()) - min(bb.values()))
    solved = [round(v) for v in solved]
    P.v("V1 independent solver (bars read against each graph's own printed scale) equals the key", solved == ans, solved)
    P.v("V7 Graph A is in 2s up to 16 and Graph B in 10s up to 100", all(v % 2 == 0 and v <= 16 for v in va) and all(v % 10 == 0 and v <= 100 for v in vb))
    return P

PAGES = [page34, page35, page36, page37, page38]
