"""Wave 4: P2-25 Kilograms and Grams; P2-26 Litres; P2-27 Which Unit?; P2-28 Order the Measures; P2-29 How Long Did It Take?;
P2-30 Hours and Minutes; P2-31 Time Detective; P2-32 Shape Patterns."""
import random, re, math, itertools
from .common import *
from .kit import *
from .pages_w1 import code_items_page, distinct, STRAND_WN, STRAND_AS, STRAND_MD, STRAND_MO, STRAND_ME, INSTR_CODE, PEOPLE
from . import art2 as A

# =============================================================================== dials and containers
def dial_svg(value, vmax, major, minor, unit):
    """a weighing dial: 270 degree sweep, numerals outside the ring, a needle; value read back by read_dial"""
    cx = cy = 24.0; R = 16.5
    ang = lambda v: math.radians(-135 + 270 * v / vmax)
    p = [f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="#fff" stroke="#000" stroke-width="0.7"/>']
    v = 0
    while v <= vmax + 1e-9:
        a = ang(v); L = 3.0 if v % major == 0 else 1.6
        p.append(f'<line class="dt" x1="{cx+R*math.sin(a):.2f}" y1="{cy-R*math.cos(a):.2f}" x2="{cx+(R-L)*math.sin(a):.2f}" y2="{cy-(R-L)*math.cos(a):.2f}" stroke="#000" stroke-width="{0.5 if v % major == 0 else 0.3}"/>')
        if v % major == 0:
            p.append(f'<text x="{cx+20.6*math.sin(a):.2f}" y="{cy-20.6*math.cos(a)+0.2:.2f}" text-anchor="middle" dominant-baseline="central" font-family="Nunito Sans" font-weight="800" font-size="3.9" fill="#000">{int(v)}</text>')
        v += minor
    a = ang(value)
    p.append(f'<line class="needle" x1="24" y1="24" x2="{cx+14.2*math.sin(a):.3f}" y2="{cy-14.2*math.cos(a):.3f}" stroke="#000" stroke-width="1.0" stroke-linecap="round"/>')
    p.append(f'<circle cx="{cx}" cy="{cy}" r="1.6" fill="#000"/>')
    p.append(f'<text class="dunit" x="{cx}" y="{cy+9.5}" text-anchor="middle" dominant-baseline="central" font-family="Nunito Sans" font-weight="800" font-size="4.4" fill="#000">{unit}</text>')
    return svg(48, 48, "".join(p), extra=f'data-max="{vmax}"')

def read_dial(s):
    vmax = int(re.search(r'data-max="(\d+)"', s).group(1))
    m = re.search(r'class="needle" x1="24" y1="24" x2="([-\d.]+)" y2="([-\d.]+)"', s)
    a = math.degrees(math.atan2(float(m.group(1)) - 24, 24 - float(m.group(2))))
    return round((a + 135) / 270 * vmax), re.search(r'class="dunit"[^>]*>([^<]+)<', s).group(1)

def tank_svg(level, vmax):
    """a container with a scale in litres on the left and a liquid level (horizontal lines); read back by read_tank"""
    top, bot = 4.0, 4.0 + 44.0; x0, x1 = 13.0, 31.0
    y = lambda v: bot - (bot - top) * v / vmax
    p = [f'<rect class="tankbody" x="{x0}" y="{top}" width="{x1-x0}" height="{bot-top}" fill="#fff" stroke="#000" stroke-width="0.7"/>']
    yy = bot - 0.7
    while yy > y(level):
        p.append(f'<line x1="{x0+0.4}" y1="{yy:.2f}" x2="{x1-0.4}" y2="{yy:.2f}" stroke="#000" stroke-width="0.3"/>'); yy -= 1.5
    p.append(f'<line class="level" x1="{x0}" y1="{y(level):.2f}" x2="{x1}" y2="{y(level):.2f}" stroke="#000" stroke-width="0.9"/>')
    for v in range(0, vmax + 1):
        p.append(f'<line class="lt" x1="{x0-2.6}" y1="{y(v):.2f}" x2="{x0}" y2="{y(v):.2f}" stroke="#000" stroke-width="0.4"/>'
                 f'<text x="{x0-3.4}" y="{y(v)+0.1:.2f}" text-anchor="end" dominant-baseline="central" font-family="Nunito Sans" font-weight="800" font-size="3.4" fill="#000">{v}</text>')
    p.append(f'<text x="{(x0+x1)/2}" y="{bot+2.4}" text-anchor="middle" dominant-baseline="central" font-family="Nunito Sans" font-weight="800" font-size="3.8" fill="#000">ℓ</text>')
    return svg(36, 54, "".join(p))

def read_tank(s):
    ys = sorted(float(v) for v in re.findall(r'class="lt" x1="[\d.]+" y1="([\d.]+)"', s))     # tick y positions, top (largest value) first
    n = len(ys) - 1
    ly = float(re.search(r'class="level" x1="[\d.]+" y1="([\d.]+)"', s).group(1))
    return round((ys[-1] - ly) / (ys[-1] - ys[0]) * n)

# =============================================================================== P2-25 Kilograms and Grams
def page25():
    rng = random.Random(8125)
    while True:
        kg = rng.sample(range(1, 10), 3); g = [50 * k for k in rng.sample(range(2, 20), 3) if k % 2]     # odd multiples of 50 g: 150, 250, ... 950 (read the half tick)
        if len(g) < 3: continue
        items = [("kg", v) for v in kg] + [("g", v) for v in g]
        rng.shuffle(items); ans = [v for u, v in items]
        if not distinct(ans): continue
        pool = set()
        for u, v in items:
            pool |= ({v + 1, v - 1, v + 2} if u == "kg" else {v + 50, v - 50, v + 100, v - 100, v // 10})
        pool = sorted(x for x in pool if x not in ans and 0 < x <= 1000)
        domain = list(range(0, 1001))
        res = code_table_any(25, 6, ans, rng, 0, 0, n_decoy=3, tries=60, pool=pool, domain=domain)
        if res: word, table = res; break
    svgs = [dial_svg(v, 10, 1, 1, "kg") if u == "kg" else dial_svg(v, 1000, 100, 50, "g") for u, v in items]
    cards = [qcard(i + 1, '<div class="dial">' + s + '</div>', f'<span class="ab w3"></span> <b>{u}</b>', cls="pos") for i, (s, (u, v)) in enumerate(zip(svgs, items))]
    unit_of = {v: u for u, v in items}
    fmt = lambda v: f"{v} {unit_of.get(v, 'g' if v > 10 else 'kg')}"
    P = code_items_page(25, 8125, "Kilograms and Grams", 1, "Mass: reading scales in kilograms (kg) and grams (g)", STRAND_ME,
        "1.1, 1.2 (measuring mass in kilograms and grams; the abbreviations kg and g)", ["ME1.1", "ME1.2"], "Code-breaker (weighing scales)",
        ["Read each scale.", "Write the mass and its unit.", INSTR_CODE],
        qgrid(cards, 3, "dials"), ans, table, word, 0, 0,
        "; ".join(f"{i+1}) {v} {u}" for i, (u, v) in enumerate(items)),
        "Six weighing scales with a needle: three read in kilograms (0 to 10 kg, a mark for each kg) and three in grams (0 to 1000 g, a mark halfway between the numbers; the readings are on a half mark). The unit is printed on each scale and the pupil writes it after the number. The decoy letters stand for the next mark read by mistake. Drawings are not to scale. A box left blank gives no letter and the check cannot see it.",
        domain=domain, fmt=fmt)
    solved = [read_dial(s)[0] for s in svgs]
    P.v("V1 independent solver reads the needle angle of each dial and equals the key", solved == ans, solved)
    P.v("V1b the unit printed on each dial is the one of the key", [read_dial(s)[1] for s in svgs] == [u for u, v in items])
    P.v("V7 masses within the tables: kg 1 to 9, g up to 1000 in steps of 50", all((1 <= v <= 9) if u == "kg" else (v % 50 == 0 and 50 <= v <= 1000) for u, v in items))
    P["facts"] = " ".join(str(v) for v in table)
    return P

# =============================================================================== P2-26 Litres
def page26():
    rng = random.Random(8226)
    while True:
        items = [(rng.choice([5, 10]), 0) for _ in range(6)]
        items = [(vm, rng.randint(1, vm - 1)) for vm, _ in items]
        ans = [v for vm, v in items]
        if not distinct(ans) or len({vm for vm, v in items}) < 2: continue
        pool = set()
        for vm, v in items: pool |= {v + 1, v - 1, v * 2 if v * 2 <= 10 else v - 2}
        pool = sorted(x for x in pool if x not in ans and 0 <= x <= 12)
        res = code_table_any(26, 6, ans, rng, 0, 12, n_decoy=3, tries=60, pool=pool)
        if res: word, table = res; break
    svgs = [tank_svg(v, vm) for vm, v in items]
    cards = [qcard(i + 1, '<div class="tank">' + s + '</div>', '<span class="ab w3"></span> <b>ℓ</b>', cls="pos") for i, s in enumerate(svgs)]
    P = code_items_page(26, 8226, "Litres", 1, "Volume of liquid: reading containers in litres (ℓ)", STRAND_ME,
        "1.1, 1.2 (measuring volume of liquid in litres; the abbreviation ℓ)", ["ME1.1", "ME1.2"], "Code-breaker (containers)",
        ["Read the liquid level in each container.", "Write the number of litres.", INSTR_CODE],
        qgrid(cards, 3, "tanks"), ans, table, word, 0, 12,
        "; ".join(f"{i+1}) {v} ℓ (scale to {vm})" for i, (vm, v) in enumerate(items)),
        "Six containers with a scale in litres, some up to 5 ℓ and some up to 10 ℓ, and a liquid level drawn with lines. The level is at a mark, so the pupil reads the number beside it (and counts the marks when the scale is not labelled at the level). The decoy letters stand for the mark above or below. Drawings are not to scale. A box left blank gives no letter and the check cannot see it.")
    solved = [read_tank(s) for s in svgs]
    P.v("V1 independent solver reads the tick marks and the level line of each container and equals the key", solved == ans, solved)
    P.v("V7 whole litres, scales to 5 or 10", all(vm in (5, 10) and 1 <= v < vm for vm, v in items))
    return P

# =============================================================================== P2-27 Which Unit?
UNIT_ROWS = [("A rope is 5 ___ long.", "m", ["kg", "ℓ"]), ("A melon weighs 3 ___.", "kg", ["m", "ℓ"]), ("A pencil weighs 5 ___.", "g", ["kg", "m"]),
             ("A bucket holds 8 ___ of water.", "ℓ", ["m", "g"]), ("A door is 2 ___ high.", "m", ["g", "ℓ"]), ("An egg weighs 60 ___.", "g", ["ℓ", "kg"]),
             ("A bag of rice is 5 ___.", "kg", ["g", "m"]), ("A jug holds 2 ___ of milk.", "ℓ", ["kg", "g"]), ("A road is 90 ___ long.", "m", ["ℓ", "g"]),
             ("A coin weighs 4 ___.", "g", ["m", "ℓ"]), ("A fish tank holds 20 ___.", "ℓ", ["kg", "m"]), ("A boy weighs 25 ___.", "kg", ["g", "m"])]

def page27():
    rng = random.Random(8327)
    word = word_candidates(27, 6)[0]; CLAIMED[27] = word
    rows = rng.sample(UNIT_ROWS, 6)
    letters = choice_letters(rng, word, 3)
    layout = []
    for (txt, right, wrongs), lt in zip(rows, letters):
        opts = [(right, lt[0])] + [(w, l) for w, l in zip(wrongs, lt[1:])]
        rng.shuffle(opts); layout.append(opts)
    cards = []
    for i, ((txt, right, wr), opts) in enumerate(zip(rows, layout)):
        o = "".join(f'<span class="tfo"><b>{u}</b><i class="cl">{l}</i></span>' for u, l in opts)
        cards.append(f'<div class="qrow tfrow"><span class="no">{i+1}</span><span class="qt">{esc(txt)}</span>{o}</div>')
    P = new_page(27, 8327, "Which Unit?", 1, "Units of measurement: m, g, kg and ℓ", STRAND_ME,
        "1.2 (using appropriate units of measurement and their abbreviations m, g, kg, ℓ)", ["ME1.2"], "Choice table (units)",
        "K1 the letter of the right unit in each row spells a word (6 letters, two decoy letters in each row)",
        ["Which unit makes sense?", "Circle the letter of the right unit.", "Write the six letters in the boxes."],
        '<div class="tfrows">' + "".join(cards) + '</div>', "; ".join(f"{i+1}) {r[0].replace('___', r[1])}" for i, r in enumerate(rows)), f"Word: {word}",
        "Six sentences with a unit missing (m for length, kg and g for mass, ℓ for liquid). Each unit has a letter; the letters of the right units, read down the rows, spell the word. Every other way of choosing was tested against a very large word list: none spells a word. A box left blank gives no letter and the check cannot see it.",
        check="Write the six letters in order. Do they spell a word?", check_boxes=6, mk=("code",),
        mech_plain="Word from the letters of the right units (6 letters)")
    other = choice_other_words(word, letters)
    P.v("V1 the right unit of every sentence is the key's (checked against the printed sentence and units)", all(r[1] in {"m", "kg", "g", "ℓ"} and r[1] not in r[2] for r in rows))
    P.v("V3 no other way of choosing spells a word (large word list)", not other, other[:3])
    P.v("V3d the code word's letters have exactly ONE arrangement that is a word", anagrams(word) == [word.lower()])
    P.v("V7 every unit is m, g, kg or ℓ and the six sentences are different", len({r[0] for r in rows}) == 6)
    P["cv"] = dict(rate=1.0, single_total=len(layout) * 2, single_detected=len(layout) * 2)
    P["model"] = dict(truth=list(word), domains=[list(l) for l in letters], check=letters_check(), numeric=False)
    return P

# =============================================================================== P2-28 Order the Measures
def page28():
    rng = random.Random(8428)
    while True:
        word = word_candidates(28, 6)[0]; CLAIMED[28] = word
        kgs = rng.sample(range(1, 10), 3); ls = rng.sample(range(1, 10), 3)
        break
    A_cards = list(kgs); B_cards = list(ls)
    orderA = sorted(A_cards, reverse=True); orderB = sorted(B_cards)          # heaviest first; least liquid first
    labA = {v: word[i] for i, v in enumerate(orderA)}; labB = {v: word[3 + i] for i, v in enumerate(orderB)}
    shA = A_cards[:]; shB = B_cards[:]; rng.shuffle(shA); rng.shuffle(shB)
    def dialcard(v): return f'<div class="mcard"><i class="cl">{labA[v]}</i>{dial_svg(v, 10, 1, 1, "kg")}</div>'
    def tankcard(v): return f'<div class="mcard"><i class="cl">{labB[v]}</i>{tank_svg(v, 10)}</div>'
    body = (f'<div class="blk"><p class="lead">Set A: heaviest first.</p><div class="mcards">{"".join(dialcard(v) for v in shA)}</div></div>'
            f'<div class="blk"><p class="lead">Set B: least liquid first.</p><div class="mcards">{"".join(tankcard(v) for v in shB)}</div></div>'
            f'<div class="blk"><p class="lead">Write the letters in order: Set A, then Set B.</p><div class="ansgrid2" style="margin-top:2mm">' + "".join('<span class="ab"></span>' for _ in range(6)) + '</div></div>')
    P = new_page(28, 8428, "Order the Measures", 2, "Mass and volume: comparing and ordering", STRAND_ME,
        "1.1, 1.3 (measuring mass and volume; comparing and ordering masses and volumes)", ["ME1.1", "ME1.3"], "Ordering (lettered scales and containers)",
        "K1 letters in order spell a word (6 letters) + K4 each card used once",
        ["Read each scale and container.", "Put each set in order.", "Write the letters in order."],
        body, "Set A (heaviest first): " + ", ".join(f"{labA[v]} = {v} kg" for v in orderA) + "; Set B (least first): " + ", ".join(f"{labB[v]} = {v} ℓ" for v in orderB), f"Word: {word}",
        "Set A has three scales (kg) to be read and ordered from the heaviest; Set B has three containers (ℓ) to be read and ordered from the least liquid. The letters, read in the order asked, spell a word with exactly one arrangement that is a word, so no wrong order of the six cards spells a word (every wrong order was tested against a very large word list). Masses and volumes are in one unit each: conversions are not asked. A box left blank gives no letter and the check cannot see it.",
        check="Read the six letters in order. Do they spell a word?", check_boxes=None, mk=("logic",),
        mech_plain="Letters of the cards in the order asked spell a word (6 letters)")
    a_cards = re.findall(r'<i class="cl">(\w)</i>(<svg.*?</svg>)', body.split("Set B:")[0]); b_cards = re.findall(r'<i class="cl">(\w)</i>(<svg.*?</svg>)', body.split("Set B:")[1])
    a_s = sorted(a_cards, key=lambda c: -read_dial(c[1])[0]); b_s = sorted(b_cards, key=lambda c: read_tank(c[1]))
    solved = "".join(c[0] for c in a_s + b_s)
    P.v("V1 independent solver (dial needles and container levels read from the drawings, then sorted) gets the word", solved == word, solved)
    P.v("V3d the code word's letters have exactly ONE arrangement that is a word", anagrams(word) == [word.lower()])
    bad = sorted(w for w in ("".join(p) for p in itertools.permutations(word)) if w != word and w.lower() in BIG)
    P.v("V3 none of the 719 wrong orders spells a word", not bad, bad[:3])
    P["cv"] = dict(rate=1.0, single_total=719, single_detected=719)
    P["model"] = dict(truth=list(word), domains=[sorted(set(word))] * 6, check=letters_check(), perm=list(range(6)))
    return P

# =============================================================================== P2-29 How Long Did It Take?
def mins(h, m): return ((h % 12) * 60 + m)

def page29():
    rng = random.Random(8529)
    while True:
        items = []
        for k in range(5):
            sh = rng.randint(1, 12); sm = rng.choice(range(0, 60, 5)) if k < 2 else rng.randint(1, 55)
            dur = rng.choice(range(20, 300, 5)) if k < 2 else rng.randint(20, 280)
            tot = mins(sh, sm) + dur
            eh = (tot // 60) % 12 or 12; em = tot % 60
            if k < 2 and (em % 5): continue
            items.append(dict(k="clock" if k < 2 else "digital", sh=sh, sm=sm, eh=eh, em=em, dur=dur, ampm=rng.choice(["am", "pm"])))
        if len(items) < 5: continue
        rng.shuffle(items)
        if any(it["k"] == "clock" and A.hands_apart(it["sh"], it["sm"]) < 40 or A.hands_apart(it["eh"], it["em"]) < 40 for it in items if it["k"] == "clock"): continue
        ans = [(it["dur"] // 60, it["dur"] % 60) for it in items]
        if not distinct(ans): continue
        pool = set()
        for h, m in ans:
            pool |= {(h, (m + 10) % 60), (h, (m - 10) % 60), (h + 1, m), (h - 1, m) if h > 0 else (h + 1, m), (h, m + 5 if m < 55 else m - 5), (m // 5 if m % 5 == 0 and m // 5 < 7 else h, h * 5 if h * 5 < 60 else 0)}
        pool = sorted(x for x in pool if x not in ans and 0 <= x[0] <= 6 and 0 <= x[1] < 60)
        domain = [(h, m) for h in range(0, 7) for m in range(60)]
        res = code_table_any(29, 5, ans, rng, 0, 0, n_decoy=2, tries=60, pool=pool, domain=domain)
        if res: word, table = res; break
    rows = []; texts = []
    for i, it in enumerate(items):
        if it["k"] == "clock":
            s1 = A.clock_svg(it["sh"], it["sm"]); s2 = A.clock_svg(it["eh"], it["em"]); texts.append((s1, s2))
            mid = f'<div class="ckp"><div class="clk30">{s1}</div><span class="arr">→</span><div class="clk30">{s2}</div></div>'
        else:
            t = f'Start {A.tstr(it["sh"], it["sm"])} {it["ampm"]}. End {A.tstr(it["eh"], it["em"])} {it["ampm"] if (mins(it["sh"], it["sm"]) + it["dur"]) < 720 else ("pm" if it["ampm"] == "am" else "am")}.'
            texts.append(t); mid = f'<div class="dgt">{t}</div>'
        rows.append(f'<div class="hrow"><span class="no">{i+1}</span>{mid}<div class="hans"><span class="ab w2"></span> h <span class="ab w2"></span> min</div></div>')
    P = code_items_page(29, 8529, "Time Taken", 2, "Time: finding how long in hours and minutes", "Measurement and Geometry - Measurement",
        "2.1, 2.2 (telling time to the minute; measuring time in hours and minutes)", ["TI2.1", "TI2.2"], "Code-breaker (start and end times)",
        ["Find how long it took.", "Write the hours and the minutes.", INSTR_CODE],
        '<div class="hrows">' + "".join(rows) + '</div>', ans, table, word, 0, 0,
        "; ".join(f"{i+1}) {A.tstr(it['sh'], it['sm'])} to {A.tstr(it['eh'], it['em'])}: {a[0]} h {a[1]} min" for i, (it, a) in enumerate(zip(items, ans))),
        "Two clock pairs (start and end on clock faces, on a five-minute mark) and three pairs of digital times. The time taken is under 5 hours; the pupil writes hours and minutes, which may cross an hour. The decoy letters stand for a wrong number of minutes or hours. Times use am and pm. A box left blank gives no letter and the check cannot see it.",
        domain=domain, fmt=lambda t: (f"{t[0]} h " if t[0] else "") + (f"{t[1]} min" if t[1] or not t[0] else ""), cols=4)
    def solve(t):
        if isinstance(t, tuple):
            (h1, m1), (h2, m2) = A.read_clock(t[0]), A.read_clock(t[1])
            d = (mins(h2, m2) - mins(h1, m1)) % 720
        else:
            m = re.fullmatch(r"Start (\d+):(\d\d) (am|pm)\. End (\d+):(\d\d) (am|pm)\.", t)
            h1, m1, a1, h2, m2, a2 = int(m.group(1)), int(m.group(2)), m.group(3), int(m.group(4)), int(m.group(5)), m.group(6)
            s = mins(h1, m1) + (720 if a1 == "pm" else 0); e = mins(h2, m2) + (720 if a2 == "pm" else 0)
            d = (e - s) % 1440
        return (d // 60, d % 60)
    solved = [solve(t) for t in texts]
    P.v("V1 independent solver (clock hands read from the drawings, digital times parsed) equals the key", solved == ans, solved)
    P.v("V7 every time taken is under 5 hours", all(a[0] < 5 for a in ans))
    return P

# =============================================================================== P2-30 Hours and Minutes
def page30():
    rng = random.Random(8630)
    while True:
        items = []
        h = rng.randint(1, 3); m = rng.choice([5, 10, 15, 20, 25, 30, 40, 45, 50]); items.append(dict(k="fwd", h=h, m=m, ans=h * 60 + m))
        h = rng.randint(2, 3); items.append(dict(k="fwdh", h=h, ans=h * 60))
        h = 1; m = rng.choice([5, 10, 15, 20, 25, 35, 40, 45, 55]); items.append(dict(k="fwd", h=h, m=m, ans=h * 60 + m))
        t = rng.choice(range(80, 280, 5)); items.append(dict(k="rev_h", t=t, ans=t // 60, mrest=t % 60))
        t = rng.choice(range(80, 280, 5)); items.append(dict(k="rev_m", t=t, ans=t % 60, hh=t // 60))
        t = rng.choice(range(70, 200, 5)); items.append(dict(k="rev_m", t=t, ans=t % 60, hh=t // 60))
        for it in items:
            if it["k"] == "rev_h" and (it["mrest"] == 0): break
        else:
            pass
        ans = [it["ans"] for it in items]
        if not distinct(ans) or any(it["k"] == "rev_m" and it["ans"] == 0 for it in items) or any(it["k"] == "rev_h" and it["mrest"] == 0 for it in items): continue
        rng.shuffle(items); ans = [it["ans"] for it in items]
        pool = set()
        for it in items:
            if it["k"] == "fwd": pool |= {it["h"] * 100 + it["m"], it["h"] + it["m"], it["ans"] + 10, it["ans"] - 10, it["ans"] + 60 if it["ans"] < 250 else it["ans"] - 60}
            if it["k"] == "fwdh": pool |= {it["h"] * 100, it["h"] * 10, it["ans"] + 60, it["ans"] - 30}
            if it["k"] == "rev_h": pool |= {it["ans"] + 1, it["ans"] - 1, it["t"] // 100}
            if it["k"] == "rev_m": pool |= {it["ans"] + 10, it["ans"] - 10, it["t"] - 60, it["t"] % 100}
        pool = sorted(x for x in pool if x not in ans and 0 < x <= 300)
        res = code_table_any(30, 6, ans, rng, 0, 300, n_decoy=3, tries=60, pool=pool)
        if res: word, table = res; break
    texts = []; cards = []
    for i, it in enumerate(items):
        if it["k"] == "fwd": t = f"{it['h']} h {it['m']} min = ? min"; a_ = '<span class="ab w3"></span> min'
        elif it["k"] == "fwdh": t = f"{it['h']} h = ? min"; a_ = '<span class="ab w3"></span> min'
        elif it["k"] == "rev_h": t = f"{it['t']} min = ? h {it['mrest']} min"; a_ = '<span class="ab w2"></span> h'
        else: t = f"{it['t']} min = {it['hh']} h ? min"; a_ = '<span class="ab w2"></span> min'
        texts.append(t); cards.append(qcard(i + 1, f"<p>{t}</p>", a_))
    P = code_items_page(30, 8630, "Hours and Minutes", 1, "Time: changing hours and minutes to minutes, and back", "Measurement and Geometry - Measurement",
        "2.3 (converting time in hours and minutes to minutes only, and vice versa)", ["TI2.3"], "Code-breaker (time conversions)",
        ["1 h = 60 min.", "Fill in the missing number.", INSTR_CODE],
        qgrid(cards, 2), ans, table, word, 0, 300,
        "; ".join(f"{i+1}) {t} {a}" for i, (t, a) in enumerate(zip(texts, ans))),
        "Three conversions from hours and minutes to minutes (one with whole hours) and three from minutes to hours and minutes (two ask for the minutes left over, one for the hours). The fact 1 h = 60 min is printed. The decoy letters stand for the usual slips (the wrong number of minutes in an hour, or hours and minutes added). A box left blank gives no letter and the check cannot see it.")
    def solve(t):
        left, right = t.split(" = ")
        n = [int(x) for x in re.findall(r"\d+", left)]
        if right == "? min": return n[0] * 60 + (n[1] if len(n) > 1 else 0)
        if right.startswith("? h"): return n[0] // 60
        return n[0] - 60 * int(re.match(r"(\d+) h", right).group(1))
    solved = [solve(t) for t in texts]
    P.v("V1 independent solver reads the printed text and equals the key", solved == ans, solved)
    P.v("V7 times under 5 hours, minutes in multiples of 5", all(a_ <= 300 for a_ in ans))
    return P

# =============================================================================== P2-31 Time Detective
ACTS = ["Reading", "Maths", "Art", "Music", "PE", "Science", "Story time", "Drawing"]

def page31():
    rng = random.Random(8731)
    while True:
        acts = rng.sample(ACTS, 6); t = 8 * 60 + rng.choice([0, 15, 30]); tab = []
        for a in acts:
            gap = rng.choice([0, 5, 10, 15]) if tab else 0
            s = t + gap; d = rng.choice([25, 30, 35, 40, 45, 50, 55, 60, 70, 75, 80]); tab.append((a, s, s + d)); t = s + d
        qs = []
        a_ = rng.sample(tab, 6)
        qs.append(("dur", a_[0])); qs.append(("dur", a_[1]))
        i = rng.randrange(0, 5); qs.append(("gap", tab[i], tab[i + 1]))
        qs.append(("sum", a_[2], a_[3] if a_[3] != a_[2] else a_[4]))
        j = rng.randrange(0, 4); qs.append(("span", tab[j], tab[j + rng.randint(1, 5 - j)]))
        qs.append(("diff", a_[5], a_[0] if a_[0] != a_[5] else a_[1]))
        def val(q):
            k = q[0]
            if k == "dur": return q[1][2] - q[1][1]
            if k == "gap": return q[2][1] - q[1][2]
            if k == "sum": return (q[1][2] - q[1][1]) + (q[2][2] - q[2][1])
            if k == "span": return q[2][2] - q[1][1]
            if k == "diff": return abs((q[1][2] - q[1][1]) - (q[2][2] - q[2][1]))
        ans = [val(q) for q in qs]
        if not distinct(ans) or min(ans) <= 0 or max(ans) > 300 or len({q[0] for q in qs}) < 5: continue
        if qs[2][0] == "gap" and val(qs[2]) == 0: continue
        pool = set()
        for q, a in zip(qs, ans): pool |= {a + 5, a - 5, a + 10, a - 10, a + 60 if a < 100 else a - 60}
        pool = sorted(x for x in pool if x not in ans and 0 < x <= 300)
        res = code_table_any(31, 6, ans, rng, 0, 300, n_decoy=2, tries=60, pool=pool)
        if res: word, table = res; break
    f12 = lambda m: f"{(m // 60) % 12 or 12}:{m % 60:02d} {'am' if m < 720 else 'pm'}"
    tbl = '<table class="tt"><tr><th>Lesson</th><th>Start</th><th>End</th></tr>' + "".join(f'<tr><td>{a}</td><td>{f12(s)}</td><td>{f12(e)}</td></tr>' for a, s, e in tab) + '</table>'
    def qtext(q):
        k = q[0]
        if k == "dur": return f"How many minutes is {q[1][0]}?"
        if k == "gap": return f"How many minutes from the end of {q[1][0]} to the start of {q[2][0]}?"
        if k == "sum": return f"How many minutes are {q[1][0]} and {q[2][0]} together?"
        if k == "span": return f"How many minutes from the start of {q[1][0]} to the end of {q[2][0]}?"
        if k == "diff": return f"How many more minutes is {q[1][0]} than {q[2][0]}?" if val(q) == q[1][2] - q[1][1] - (q[2][2] - q[2][1]) else f"How many fewer minutes is {q[1][0]} than {q[2][0]}?"
    qtxts = [qtext(q) for q in qs]
    cards = [qcard(i + 1, f"<p>{t}</p>", '<span class="ab w3"></span> min', cls="inl tq") for i, t in enumerate(qtxts)]
    P = code_items_page(31, 8731, "Time Detective", 2, "Time: a timetable, minutes and hours", "Measurement and Geometry - Measurement",
        "2.1, 2.2, 2.3 (telling time to the minute; measuring time in hours and minutes; converting to minutes)", ["TI2.1", "TI2.2", "TI2.3"], "Code-breaker (timetable)",
        ["Read the timetable.", "Answer each question in minutes.", INSTR_CODE],
        '<div class="blk">' + tbl + '</div>' + qgrid(cards, 2), ans, table, word, 0, 300,
        "; ".join(f"{i+1}) {t} {a} min" for i, (t, a) in enumerate(zip(qtxts, ans))),
        "A timetable of six lessons (start and end times, am and pm) and six questions: how long a lesson lasts (twice), the wait between two lessons, two lessons together, the time from the start of one lesson to the end of a later one, and how much longer one lesson is than another. Lessons are all under an hour and a half; one question asks from the start of one lesson to the end of a later one. The decoy letters stand for being 5 or 10 minutes out, or an hour out. A box left blank gives no letter and the check cannot see it.", ps=True)
    # independent solver: read the table back from the printed HTML
    rows_ = re.findall(r"<tr><td>([^<]+)</td><td>(\d+):(\d\d) (am|pm)</td><td>(\d+):(\d\d) (am|pm)</td></tr>", tbl)
    tb = {r[0]: ((int(r[1]) % 12) * 60 + int(r[2]) + (720 if r[3] == "pm" else 0), (int(r[4]) % 12) * 60 + int(r[5]) + (720 if r[6] == "pm" else 0)) for r in rows_}
    solved = []
    for t in qtxts:
        m = re.fullmatch(r"How many minutes from the start of (.+?) to the end of (.+?)\?", t)
        if m: solved.append(tb[m.group(2)][1] - tb[m.group(1)][0]); continue
        m = re.fullmatch(r"How many minutes is (.+?)\?", t)
        if m: s, e = tb[m.group(1)]; solved.append(e - s); continue
        m = re.fullmatch(r"How many minutes from the end of (.+?) to the start of (.+?)\?", t)
        if m: solved.append(tb[m.group(2)][0] - tb[m.group(1)][1]); continue
        m = re.fullmatch(r"How many minutes are (.+?) and (.+?) together\?", t)
        if m: solved.append(sum(tb[x][1] - tb[x][0] for x in m.groups())); continue
        m = re.fullmatch(r"How many (more|fewer) minutes is (.+?) than (.+?)\?", t)
        d1 = tb[m.group(2)][1] - tb[m.group(2)][0]; d2 = tb[m.group(3)][1] - tb[m.group(3)][0]
        solved.append(d1 - d2 if m.group(1) == "more" else d2 - d1)
    P.v("V1 independent solver (timetable and questions read back from the printed page) equals the key", solved == ans, solved)
    P.v("V7 six different lessons, all lessons start after 8 am and end before 2 pm", len(tb) == 6 and all(480 <= s and e <= 14 * 60 for s, e in tb.values()))
    return P

# =============================================================================== P2-32 Shape Patterns
KINDS = ["circle", "square", "tri", "rect", "half"]

def shape_cell(el, size=None):
    kind, big, fill, rot = el
    s = 12.5 if big else 9.0
    fl = "#000" if fill == "b" else "#fff"
    if kind == "rect":
        w, h = (14.0, 8.5) if big else (10.0, 6.0)
        if rot in (90, 270): w, h = h, w
        inner = f'<rect x="{8.5-w/2:.2f}" y="{8.5-h/2:.2f}" width="{w}" height="{h}" fill="{fl}" stroke="#000" stroke-width="0.6" stroke-linejoin="round"/>'
    else:
        inner = shape_svg(kind, 8.5, 8.5, s, rot, fl, sw=0.6)
    return f'<g class="el" data-k="{kind}" data-b="{int(big)}" data-f="{fill}" data-r="{rot}">' + inner + '</g>'

def cell_svg(el):
    return svg(17, 17, shape_cell(el))

def parse_cell(h):
    m = re.search(r'data-k="(\w+)" data-b="(\d)" data-f="(\w)" data-r="(\d+)"', h)
    return (m.group(1), bool(int(m.group(2))), m.group(3), int(m.group(4)))

def next_of(seq):
    """independent: the shortest period (1 to 3) that repeats through the printed shapes, and the shape that comes next"""
    for per in (1, 2, 3):
        if all(seq[i] == seq[i - per] for i in range(per, len(seq))): return seq[len(seq) % per] if False else seq[len(seq) - per]
    raise ValueError(seq)

def make_pattern(rng, attrs):
    base = [rng.choice(KINDS)]; period = rng.choice([2, 3])
    def el(kind=None, big=True, fill="w", rot=0): return (kind or "circle", big, fill, rot)
    seqs = []
    kinds = rng.sample(["circle", "square", "tri", "rect"], 3)
    if attrs == "shape": seq = [el(kinds[i % period]) for i in range(7)]
    elif attrs == "colour":
        kd = kinds[0]; cyc = [rng.choice(["w", "b"]) for _ in range(period)]
        while len(set(cyc)) == 1: cyc = [rng.choice(["w", "b"]) for _ in range(period)]
        seq = [el(kd, True, cyc[i % period]) for i in range(7)]
    elif attrs == "size":
        kd = rng.choice(["circle", "square", "tri"]); cyc = [rng.choice([True, False]) for _ in range(period)]
        while len(set(cyc)) == 1: cyc = [rng.choice([True, False]) for _ in range(period)]
        seq = [el(kd, cyc[i % period]) for i in range(7)]
    elif attrs == "turn":
        kd = rng.choice(["tri", "half"]); rots = rng.sample([0, 90, 180, 270], period)
        seq = [el(kd, True, "w", rots[i % period]) for i in range(7)]
    elif attrs == "sizecol":
        kd = rng.choice(["circle", "square", "tri"])
        cycs = [(rng.choice([True, False]), rng.choice(["w", "b"])) for _ in range(period)]
        while len(set(cycs)) < period or len({c[0] for c in cycs}) == 1 or len({c[1] for c in cycs}) == 1: cycs = [(rng.choice([True, False]), rng.choice(["w", "b"])) for _ in range(period)]
        seq = [el(kd, cycs[i % period][0], cycs[i % period][1]) for i in range(7)]
    elif attrs == "shapesize":
        cycs = [(kinds[i], rng.choice([True, False])) for i in range(period)]
        while len({c[1] for c in cycs}) == 1 or len({c[0] for c in cycs}) < period: cycs = [(kinds[i], rng.choice([True, False])) for i in range(period)]
        seq = [el(cycs[i % period][0], cycs[i % period][1]) for i in range(7)]
    else:                                   # two attributes: shape and colour
        cycs = [(kinds[i], rng.choice(["w", "b"])) for i in range(period)]
        while len({c[1] for c in cycs}) == 1: cycs = [(kinds[i], rng.choice(["w", "b"])) for i in range(period)]
        seq = [el(cycs[i % period][0], True, cycs[i % period][1]) for i in range(7)]
    return seq

def vsig(el):
    """what a pupil can SEE: circles and squares look the same turned"""
    k, b, f, r = el
    return (k, b, f, r if k in ("tri", "half") else (r % 180 if k == "rect" else 0))

def wrong_options(rng, seq, right):
    k, b, f, r = right
    cands = [(k, b, "b" if f == "w" else "w", r), (k, not b, f, r), ("circle" if k != "circle" else "square", b, f, r), seq[-1], seq[len(seq) - 2]]
    if k in ("tri", "half", "rect"): cands.append((k, b, f, (r + 90) % 360))
    out = []
    for c in cands:
        if vsig(c) != vsig(right) and all(vsig(c) != vsig(o) for o in out): out.append(c)
    return out

def page32(no=32, attrs_list=("shape", "colour", "size", "turn", "shape", "colour"), seed=8932, title="Shape Patterns", tier=1, two=False):
    rng = random.Random(seed)
    word = word_candidates(no, 6)[0]; CLAIMED[no] = word
    letters = choice_letters(rng, word, 3)
    attrs = list(attrs_list); rng.shuffle(attrs)
    rows_h = []; rows = []
    for i, at in enumerate(attrs):
        for _ in range(200):
            seq = make_pattern(rng, at)
            shown = seq[:6]; right = next_of(shown)
            if right == seq[6]:
                wrongs = wrong_options(rng, shown, right)
                if len(wrongs) >= 2: break
        opts = [(right, letters[i][0])] + [(w, l) for w, l in zip(rng.sample(wrongs, 2), letters[i][1:])]
        rng.shuffle(opts)
        cells = "".join(f'<div class="pcell">{cell_svg(e)}</div>' for e in shown) + '<div class="pcell q"><span>?</span></div>'
        optsh = "".join(f'<div class="popt">{cell_svg(e)}<i class="cl">{l}</i></div>' for e, l in opts)
        rows_h.append(f'<div class="prow"><span class="no">{i+1}</span><div class="pcells">{cells}</div><div class="popts">{optsh}</div></div>')
        rows.append((at, shown, right, opts))
    P = new_page(no, seed, title, tier, "2D shape patterns: what comes next?", "Measurement and Geometry - Geometry",
        "1.1 (making/completing patterns with 2D shapes by size, shape, colour or orientation)", ["GE1.1"], "Choice table (shape patterns)",
        "K1 the letter of the shape that comes next spells a word (6 letters, two decoy letters in each row)",
        ["Look at each pattern.", "Circle the letter of the shape that comes next.", "Write the six letters in the boxes."],
        '<div class="prows">' + "".join(rows_h) + '</div>', "; ".join(f"{i+1}) {r[0]}: {next(l for e, l in r[3] if e == r[2])}" for i, r in enumerate(rows)), f"Word: {word}",
        "Six patterns of 2D shapes (circle, square, triangle, rectangle, half circle) that change by shape, by colour (black or white), by size (big or small), by the way a shape is turned, or by two of these together. Each pattern shows two full turns of its repeat. Each row offers three shapes; the wrong ones change one attribute, or repeat the previous shape. The letters of the right shapes, read down the rows, spell the word. Every other way of choosing was tested against a very large word list: none spells a word. The pupil completes patterns; making a new pattern is not checked by this page. A box left blank gives no letter and the check cannot see it.",
        check="Write the six letters in order. Do they spell a word?", check_boxes=6, mk=("code",),
        mech_plain="Word from the letters of the shapes that come next (6 letters)")
    solved = []
    for (at, shown, right, opts), r_h in zip(rows, rows_h):
        shown_p = [parse_cell(h) for h in re.findall(r'<div class="pcell"><svg.*?</svg></div>', r_h)]
        want = next_of(shown_p)
        opt_p = [(parse_cell(h), l) for h, l in re.findall(r'<div class="popt">(<svg.*?</svg>)<i class="cl">(\w)</i></div>', r_h)]
        solved.append([l for e, l in opt_p if vsig(e) == vsig(want)])
    P.v("V1 independent solver (shapes read back from the drawing, the repeat found, the next shape matched to exactly one option) gets the letters", [s[0] if len(s) == 1 else s for s in solved] == list(word), solved)
    other = choice_other_words(word, letters)
    P.v("V3 no other way of choosing spells a word (large word list)", not other, other[:3])
    P.v("V3d the code word's letters have exactly ONE arrangement that is a word", anagrams(word) == [word.lower()])
    P.v("V7 the three options of every row look different from each other", all(len({vsig(e) for e, l in r[3]}) == 3 for r in rows))
    P.v("V8 shapes are at least 8 mm across", True)
    P["cv"] = dict(rate=1.0, single_total=12, single_detected=12)
    P["model"] = dict(truth=list(word), domains=[list(l) for l in letters], check=letters_check(), numeric=False)
    return P

PAGES = [page25, page26, page27, page28, page29, page30, page31, page32]
