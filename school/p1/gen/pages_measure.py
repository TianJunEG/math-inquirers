"""Pages 6 and 15-20: shape riddles, money, length, time, shape count, picture graph."""
import random, itertools, re, math
from .common import *
from .pages_numbers import grid_table

# ---------------------------------------------------------------- P15
COIN_D = {5: 10, 10: 11, 20: 12.5, 50: 14.5}

def coins_svg(coins):
    p = []; x = 1
    for v in coins:
        d = COIN_D[v]; cx = x + d / 2
        p.append(f'<circle class="coin" cx="{cx:.1f}" cy="8" r="{d/2:.1f}" fill="#fff" stroke="#000" stroke-width="0.6"/>'
                 f'<circle cx="{cx:.1f}" cy="8" r="{d/2-1.1:.1f}" fill="none" stroke="#000" stroke-width="0.25"/>'
                 f'<text class="coinval" x="{cx:.1f}" y="9.6" text-anchor="middle" font-family="Nunito Sans" font-weight="800" font-size="4.6" fill="#000">{v}</text>')
        x += d + 1.5
    return svg(x + 1, 16.5, "".join(p))

def page15():
    rng = random.Random(1515)
    word = "PIANO"
    while True:
        purses = [sorted([rng.choice([5, 10, 20, 50]) for _ in range(rng.randint(3, 5))], reverse=True) for _ in range(5)]
        tot = [sum(p) for p in purses]
        if len(set(tot)) == 5 and max(tot) <= 95 and min(tot) >= 25 and all(len(set(p)) >= 2 for p in purses): break
    table = build_table(tot, word, rng, 5, 100, n_decoy=5, near=(5, -5, 10, -10, 15, -15))
    svgs = [coins_svg(p) for p in purses]
    rows = "".join(f'<div class="crow"><span class="no">{i+1}</span><div class="csvg">{s}</div><div class="cans"><span class="ab wide"></span> <b>&cent;</b></div></div>' for i, s in enumerate(svgs))
    body = f'<div class="crows">{rows}</div>{code_block(table)}'
    P = Page(no=15, title="Coin Purses", tier=1, topic="Money: counting coins in cents (up to $1)",
             strand="Number and Algebra - Money", syll="Money (count money in cents up to $1)",
             ptype="Code-breaker", mech="K1 code word (5 letters)",
             instr=["Add the coins in each purse.", "Write the total in cents.", "Use the code table."],
             body=body, check="Write the letters in order. They spell a word. Is it a music maker?", check_boxes=5,
             key=dict(answers=", ".join(f"{i+1}) {t}\u00a2" for i, t in enumerate(tot)), check_result=f"Code word: {word}"),
             note="Coins used: 5\u00a2, 10\u00a2, 20\u00a2, 50\u00a2, drawn by value as printed numbers. Totals stay below $1. Coin sizes grow with value but the number is what matters.",
             seed=1515)
    solved = [sum(int(m) for m in re.findall(r'class="coinval"[^>]*>(\d+)<', s)) for s in svgs]
    P.v("V1 coin values read from the drawing add to the key", solved == tot, solved)
    cv = code_verify(tot, table, word, 5, 100)
    P.v("V2 code word spells PIANO", cv["spelled_ok"])
    P.v("V3 single-slip detection >=98%", cv["rate"] >= .98, f'{cv["rate"]:.3f}')
    P.v("V7 totals below $1", max(tot) < 100)
    P["cv"] = cv
    P["model"] = code_model(tot, table, 5, 100)
    P["mech_plain"] = "Code word (5 letters)"
    return P

# ---------------------------------------------------------------- P16
def price_ok(price, c):
    k = c[0]
    if k == "price": return price[c[1]] == c[2]
    if k == "cheap": return price[c[1]] == min(price.values())
    if k == "dear": return price[c[1]] == max(price.values())
    if k == "more": return price[c[1]] > price[c[2]]
    if k == "diff": return price[c[1]] - price[c[2]] == c[3]

def price_text(c):
    c = tuple(c) + (0, 0)
    k = c[0]
    return {"price": f"The {c[1]} costs ${c[2]}.", "cheap": f"The {c[1]} costs the least.", "dear": f"The {c[1]} costs the most.",
            "more": f"The {c[1]} costs more than the {c[2]}.", "diff": f"The {c[1]} costs ${c[3]} more than the {c[2]}."}[k]

def solve_prices(items, prices, clues):
    out = []
    for perm in itertools.permutations(prices):
        pr = dict(zip(items, perm))
        if all(price_ok(pr, c) for c in clues): out.append(pr)
    return out

def page16():
    rng = random.Random(1616)
    items = ["pen", "book", "ball", "kite", "cup"]
    word = "BASKET"            # letters 1-5 sit beside the prices; letter 6 comes from the total
    while True:
        prices = sorted(rng.sample([3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 18, 20], 5))
        if prices[-1] - prices[0] >= 10: break
    perm = prices[:]; rng.shuffle(perm)
    truth = dict(zip(items, perm))
    while True:
        cl = []
        for _ in range(40):
            a, b = rng.sample(items, 2)
            k = rng.choice(["price", "cheap", "dear", "more", "diff", "diff", "more"])
            c = {"price": ("price", a, truth[a]), "cheap": ("cheap", a), "dear": ("dear", a),
                 "more": ("more", a, b), "diff": ("diff", a, b, truth[a] - truth[b])}[k]
            if k == "diff" and truth[a] - truth[b] <= 0: continue
            if price_ok(truth, c) and c not in cl: cl.append(c)
        rng.shuffle(cl)
        for c in cl[:]:
            rest = [x for x in cl if x != c]
            if len(solve_prices(items, prices, rest)) == 1: cl = rest
        if 4 <= len(cl) <= 6 and len(solve_prices(items, prices, cl)) == 1 and any(c[0] == "diff" for c in cl): break
    letter_of = {truth[it]: word[i] for i, it in enumerate(items)}
    chips = "".join(f'<span class="chip">${p} <i class="cl">{letter_of[p]}</i></span>' for p in prices)
    clues = "".join(f"<li>{price_text(c)}</li>" for c in cl)
    a, b = rng.sample(items, 2)
    total = truth[a] + truth[b]
    ttab = build_table([total], word[5], rng, 2, 40, n_decoy=3, near=(1, -1, 2, -2, 10, -10))
    ans = ('<div class="ansgrid"><span></span><b>price</b><b>letter</b>' +
           "".join(f'<span class="nm">{it}</span><span class="ab"></span><span class="ab"></span>' for it in items) + '</div>')
    q = (f'<div class="ansline">The {a} and the {b} cost $<span class="ab"></span> together. Code letter <span class="ab"></span></div>'
         f'<div class="codetable"><b class="ctl">Code table</b>' + "".join(f'<div class="ct"><span class="n">${k}</span><span class="eq">=</span><b>{v}</b></div>' for k, v in ttab.items()) + '</div>')
    body = (f'<div class="blk"><p class="lead">The prices are:</p><div class="chips">{chips}</div></div>'
            f'<ul class="clues">{clues}</ul>'
            f'<div class="twocol"><div>{grid_table(items, ["$%d" % p for p in prices])}</div><div>{ans}</div></div>{q}')
    diffs = [c for c in cl if c[0] == "diff"]
    P = Page(no=16, title="Shop Prices", tier=2, topic="Money: dollars, more and less",
             strand="Number and Algebra - Money", syll="Money (dollars up to $100) with 2.1 to 2.7 (add, subtract)",
             ptype="Logic grid + total", mech="K4 grid + K1 letter beside each price + code letter for the total (6 letters)",
             mech_plain="Letters beside the prices, then a code letter for the total, spell a word (6 letters)",
             instr=["Read the clues.", "Cross a box if a clue says no.", "Tick a box if it must be yes.", "Write each price, then its letter."],
             body=body, check="Read your six letters in order. Do they spell a word? You carry shopping in it.", check_boxes=6,
             key=dict(answers=", ".join(f"{i}: ${truth[i]} ({letter_of[truth[i]]})" for i in items) + f"; the {a} and the {b} cost ${total} together (code letter {word[5]})", check_result=f"Letters in order: {word}"),
             note="Five items, five prices, each price with a letter. " + " ".join(f"'${c[3]} more than' means a price ${c[3]} higher: pupils test each price against it." for c in diffs[:1]) + " The last answer is added from the grid and looked up in a small code table, so a wrong grid or a wrong sum changes the word.",
             seed=1616)
    sols = solve_prices(items, prices, cl)
    P.v("V1 exactly one price assignment satisfies all clues", len(sols) == 1 and sols[0] == truth, len(sols))
    P.v("V1b every clue needed", all(len(solve_prices(items, prices, [x for x in cl if x != c])) > 1 for c in cl))
    P.v("V2 letters beside the prices (item order) plus total letter spell BASKET", "".join(letter_of[truth[i]] for i in items) + ttab[total] == word)
    wrong = [pp for pp in itertools.permutations(prices) if list(pp) != perm]
    real = sum(("".join(letter_of[v] for v in pp) + word[5]).lower() in WORDS for pp in wrong)
    P.v("V3 wrong placements that still spell a word <= 5%", real / len(wrong) <= .05, f"{real}/{len(wrong)}")
    P.v("V7 prices within $100, total within $40", max(prices) <= 100 and total <= 40)
    P["cv"] = dict(rate=1 - real / len(wrong), single_total=len(wrong), single_detected=len(wrong) - real)
    letters = [letter_of[truth[i]] for i in items]
    def chk(ans):
        t = ttab.get(ans[5])
        return t is not None and ("".join(ans[:5]) + t).lower() in WORDS
    P["model"] = dict(truth=letters + [total], domains=[list(letter_of.values())] * 5 + [list(range(2, 41))], check=chk, perm=list(range(5)), numeric=False)
    P["mini"] = mini_ticks(5, 5, {(i, prices.index(truth[it])) for i, it in enumerate(items)})
    return P

# ---------------------------------------------------------------- P17
RULER_CM = 12

def ruler_unit(L):
    """strip of length L cm over a ruler 0..12 cm; scale 10 mm per cm. The ruler body extends 4.5 mm past 0 and 12
    so the labels 0 and 12 are not crossed by the ruler's border."""
    x0 = 5; p = []
    p.append(f'<rect class="strip" x="{x0}" y="0.5" width="{L*10}" height="5.5" fill="#fff" stroke="#000" stroke-width="0.5"/>')
    for k in range(0, L * 10, 3):
        p.append(f'<line x1="{x0+k}" y1="6" x2="{x0+min(k+3, L*10)}" y2="0.5" stroke="#000" stroke-width="0.25"/>')
    p.append(f'<rect x="0.5" y="7" width="{RULER_CM*10 + 2*x0 - 1}" height="8.5" fill="#fff" stroke="#000" stroke-width="0.5"/>')
    for k in range(RULER_CM * 10 + 1):
        h = 4.2 if k % 10 == 0 else (2.8 if k % 5 == 0 else 1.3)
        p.append(f'<line x1="{x0+k}" y1="7" x2="{x0+k}" y2="{7+h}" stroke="#000" stroke-width="{0.45 if k%10==0 else 0.3}"/>')
    for k in range(RULER_CM + 1):
        p.append(f'<text x="{x0+k*10}" y="14.4" text-anchor="middle" font-family="Nunito Sans" font-weight="700" font-size="3.3" fill="#000">{k}</text>')
    return svg(RULER_CM * 10 + 2 * x0, 16, "".join(p))

def page17():
    rng = random.Random(1717)
    word = "PENCIL"
    L = rng.sample(range(2, 12), 6)
    table = build_table(L, word, rng, 1, 12, n_decoy=4, near=(1, -1, 2, -2))
    svgs = [ruler_unit(x) for x in L]
    rows = "".join(f'<div class="lrow"><span class="no">{i+1}</span><div class="lsvg">{s}</div><span class="ab"></span> <span class="unit">cm</span></div>' for i, s in enumerate(svgs))
    body = f'<div class="lrows">{rows}</div>{code_block(table)}'
    P = Page(no=17, title="How Long?", tier=1, topic="Length: measure in centimetres",
             strand="Measurement and Geometry - Measurement", syll="Length 1.1 to 1.3 (measure in cm, abbreviation cm)",
             ptype="Code-breaker", mech="K1 code word (6 letters)",
             instr=["Each strip starts at 0 on its ruler.", "Write how long it is in cm.", "Use the code table."],
             body=body, check="Write the letters in order. They spell a word. Is it used for writing?", check_boxes=6,
             key=dict(answers=", ".join(f"{i+1}) {x} cm" for i, x in enumerate(L)), check_result=f"Code word: {word}"),
             note="A ruler is drawn under each strip at 10 mm to 1 cm. If the page is copied at a different scale the strip and ruler change together, so the reading from the drawn ruler stays right, but a real ruler laid on the page will not match: print at 100% (actual size) if pupils will use a real ruler. All strips start at 0 and are whole numbers of cm.",
             seed=1717)
    meas = []
    for s in svgs:
        w = float(re.search(r'class="strip"[^>]*? width="([\d.]+)"', s).group(1))
        meas.append(round(w / 10))
    P.v("V1 strip widths read against the 10 mm/cm scale equal the key", meas == L, meas)
    cv = code_verify(L, table, word, 1, 12)
    P.v("V2 code word spells PENCIL", cv["spelled_ok"])
    P.v("V3 single-slip detection >=98%", cv["rate"] >= .98, f'{cv["rate"]:.3f}')
    P["cv"] = cv
    P["model"] = code_model(L, table, 1, 12)
    P["mech_plain"] = "Code word (6 letters)"
    return P

# ---------------------------------------------------------------- P18
def clock_svg(h, m):
    cx = cy = 22; p = [f'<circle cx="{cx}" cy="{cy}" r="20" fill="#fff" stroke="#000" stroke-width="0.7"/>']
    for k in range(60):
        a = math.radians(k * 6); r1 = 20 if k % 5 else 18.2
        p.append(f'<line x1="{cx+r1*math.sin(a)-0:.2f}" y1="{cy-r1*math.cos(a):.2f}" x2="{cx+17.2*math.sin(a):.2f}" y2="{cy-17.2*math.cos(a):.2f}" stroke="#000" stroke-width="{0.4 if k%5==0 else 0.2}"/>' if k % 5 == 0 else "")
    for k in range(1, 13):
        a = math.radians(k * 30)
        p.append(f'<text x="{cx+14.6*math.sin(a):.2f}" y="{cy-14.6*math.cos(a)+1.3:.2f}" text-anchor="middle" font-family="Nunito Sans" font-weight="800" font-size="3.7" fill="#000">{k}</text>')
    ha = math.radians(30 * (h % 12) + m * 0.5); ma = math.radians(m * 6)
    p.append(f'<line class="hour" x1="{cx}" y1="{cy}" x2="{cx+8*math.sin(ha):.3f}" y2="{cy-8*math.cos(ha):.3f}" stroke="#000" stroke-width="2.0" stroke-linecap="round"/>')
    p.append(f'<line class="minute" x1="{cx}" y1="{cy}" x2="{cx+12*math.sin(ma):.3f}" y2="{cy-12*math.cos(ma):.3f}" stroke="#000" stroke-width="0.7" stroke-linecap="round"/>')
    p.append(f'<circle cx="{cx}" cy="{cy}" r="1.2" fill="#000"/>')
    return svg(44, 44, "".join(p))

def read_clock(s):
    """independent reader: recover time from hand end points in the drawing"""
    hx = re.search(r'class="hour" x1="22" y1="22" x2="([-\d.]+)" y2="([-\d.]+)"', s)
    mx = re.search(r'class="minute" x1="22" y1="22" x2="([-\d.]+)" y2="([-\d.]+)"', s)
    ang = lambda x, y: (math.degrees(math.atan2(float(x) - 22, 22 - float(y)))) % 360
    m = round(ang(*mx.groups()) / 6) % 60
    ha = ang(*hx.groups())
    h = round((ha - m * 0.5) / 30) % 12 or 12
    return h, m

def tstr(h, m): return f"{(h-1) % 12 + 1}:{m:02d}"

def tkey(h, m):
    """time in digits, with o'clock / half past in words when it applies (used in the teacher key)"""
    h = (h - 1) % 12 + 1
    if m == 0: return f"{h}:00 ({h} o'clock)"
    if m == 30: return f"{h}:30 (half past {h})"
    return f"{h}:{m:02d}"

def hands_apart(h, m):
    ha = 30 * (h % 12) + m * 0.5; ma = m * 6
    return abs((ha - ma + 180) % 360 - 180)

def page18():
    rng = random.Random(1818)
    word = "TIMER"
    while True:
        qs = []
        for k in range(5):
            while True:
                h = rng.randint(1, 12); m = rng.choice([0, 30, 0, 30, 5, 10, 15, 20, 25, 35, 40, 45, 50, 55])
                if hands_apart(h, m) >= 25: break          # keep the two hands easy to tell apart
            kind = "hour" if k % 2 == 0 else "half"
            qs.append((h, m, kind))
        ans = []
        for h, m, kind in qs:
            if kind == "hour": ans.append(((h % 12) + 1, m))
            else:
                mm = m + 30; hh = h + (1 if mm >= 60 else 0); ans.append((((hh - 1) % 12) + 1, mm % 60))
        if len({tstr(*a) for a in ans}) == 5 and len({tstr(h, m) for h, m, _ in qs}) == 5 and not any((h, m) in ans for h, m, _ in qs): break
    # table: times -> letters (answers) plus wrong readings as decoys (read time itself, hands swapped, minute +-5)
    table = {tstr(*a): l for a, l in zip(ans, word)}
    junk = [c for c in JUNK if c not in word]; rng.shuffle(junk)
    dec = []
    for (h, m, kind), a in zip(qs, ans):
        dec += [tstr(h, m), tstr(*a[:1], (a[1] + 5) % 60), tstr(((a[0] % 12) + 1), a[1]), tstr(m // 5 if m >= 5 else 12, (h * 5) % 60)]
    rng.shuffle(dec)
    for d in dec:
        if d not in table and len(table) < 11: table[d] = junk.pop()
    items = ""
    svgs = []
    for i, (h, m, kind) in enumerate(qs):
        s = clock_svg(h, m); svgs.append(s)
        q = "1 hour later" if kind == "hour" else "half an hour later"
        items += (f'<div class="citem"><span class="no">{i+1}</span>{s}<div class="cmid"><div class="cq">What is the time<br><b>{q}</b>?</div>'
                  f'<div class="ctime"><span class="ab"></span> : <span class="ab"></span></div></div></div>')
    keys = list(table.items()); rng.shuffle(keys)
    ct = "".join(f'<div class="ct"><span class="n">{k}</span><span class="eq">=</span><b>{v}</b></div>' for k, v in keys)
    body = f'<div class="items g2">{items}</div><div class="blk"><p class="lead">Code table</p><div class="codetable">{ct}</div></div>'
    P = Page(no=18, title="Clock Time", tier=2, topic="Time: tell time to 5 minutes; 1 hour and half an hour later",
             strand="Measurement and Geometry - Measurement", syll="Time 2.1 to 2.4 (tell time to 5 minutes, durations of 1 hour or half an hour)",
             ptype="Code-breaker", mech="K1 code word (5 letters)",
             instr=["Read each clock.", "Find the time later.", "Write it in the boxes.", "Use the code table."],
             body=body, check="Write the letters in order. They spell a word. Does it count the time?", check_boxes=5,
             key=dict(answers=", ".join(f"{i+1}) shows {tkey(h,m)}, {'1 hour' if k == 'hour' else 'half an hour'} later {tkey(*a)}" for i, ((h, m, k), a) in enumerate(zip(qs, ans))), check_result=f"Code word: {word}"),
             note="Tell the time to 5 minutes, then add 1 hour or half an hour. This is the two-star step: some half-hour additions cross the hour. The decoy times in the table are the time shown, the wrong hour and the wrong minute, so a misread clock or a missed step gives a letter that does not belong. The hands are never closer than 25 degrees (except at o'clock). a.m. and p.m. are not used on this page.",
             seed=1818)
    read = [read_clock(s) for s in svgs]
    P.v("V1 clock hands read back from the drawing equal the intended times", read == [(((h - 1) % 12) + 1, m) for h, m, _ in qs], read)
    solved = []
    for (h, m), (_, _, kind) in zip(read, qs):
        solved.append(tstr(h % 12 + 1, m) if kind == "hour" else tstr(h + (1 if m + 30 >= 60 else 0), (m + 30) % 60))
    P.v("V1b later times computed from drawing equal the key", solved == [tstr(*a) for a in ans], solved)
    spelled = "".join(table[s] for s in solved)
    P.v("V2 code word spells TIMER", spelled == word)
    # V3: single slip = any other time on the 5-minute grid, 1:00..12:55
    alltimes = [tstr(h, m) for h in range(1, 13) for m in range(0, 60, 5)]
    tot = det = 0
    for i, a in enumerate(solved):
        for t in alltimes:
            if t == a: continue
            tot += 1
            L = table.get(t)
            if L is None: det += 1; continue
            w = word[:i] + L + word[i+1:]
            if w != word and w.lower() not in WORDS: det += 1
    P.v("V3 single-slip detection >=98%", det / tot >= .98, f"{det}/{tot}")
    P["cv"] = dict(rate=det / tot, single_total=tot, single_detected=det)
    P["model"] = dict(truth=[tstr(*a) for a in ans], domains=[alltimes] * 5, check=code_check(table), numeric=False)
    P["mech_plain"] = "Code word (5 letters)"
    return P

# ---------------------------------------------------------------- P19
def page19():
    rng = random.Random(1919)
    word = "SHAPE"
    types = ["rect", "tri", "circle", "half", "quarter"]
    counts = [1, 2, 3, 4, 5]; rng.shuffle(counts)
    pieces = [t for t, c in zip(types, counts) for _ in range(c)]
    rng.shuffle(pieces)
    rots = {"rect": [0, 90], "tri": [0, 90, 180, 270], "circle": [0], "half": [0, 90, 180, 270], "quarter": [0, 90, 180, 270]}
    inner = ['<rect x="0.5" y="0.5" width="169" height="101" fill="#fff" stroke="#000" stroke-width="0.7" rx="3"/>']
    for i, t in enumerate(pieces):
        r, c = divmod(i, 5)
        cx = 17 + c * 34 + rng.uniform(-1.5, 1.5); cy = 17 + r * 34 + rng.uniform(-1.5, 1.5)
        inner.append(shape_svg(t, round(cx, 1), round(cy, 1), 25, rot=rng.choice(rots[t]), fill="#fff", sw=0.6, cls="piece"))
    fig = svg(170, 102, "".join(inner))
    table = build_table(counts, word, rng, 1, 9, n_decoy=4, near=(1, -1, 2, -2, 3, -3))
    rows = ""
    for t in types:
        rows += f'<div class="srow">{svg(14, 14, shape_svg(t, 7, 7, 12, fill="#fff", sw=0.5))}<span class="op">=</span><span class="ab"></span></div>'
    body = (f'<div class="figwrap">{fig}</div><div class="srows">{rows}</div>'
            f'{code_block(table)}')
    P = Page(no=19, title="Shape Count", tier=1, topic="2D shapes: rectangle, triangle, circle, half circle, quarter circle",
             strand="Measurement and Geometry - Geometry", syll="Geometry 1.1, 1.3 (name 2D shapes; identify the shapes in a figure)",
             ptype="Count + code-breaker", mech="K3 the five counts add to 15 + K1 code word (5 letters)",
             instr=["Count each kind of shape in the picture.", "Write how many in the box.", "Use the code table."],
             body=body, check="Do your five numbers add to 15? Write the letters. Do they spell a word?", check_boxes=5,
             key=dict(answers=", ".join(f"{t}: {c}" for t, c in zip(["rectangles", "triangles", "circles", "half circles", "quarter circles"], counts)) + " (total 15)", check_result=f"Total 15; code word: {word}"),
             note="The picture has no squares so there is no 'is a square a rectangle?' question. Shapes are turned in different directions on purpose. The five counts are all different (1 to 5) so each count gives one letter.",
             seed=1919)
    figs = fig
    got = [figs.count(f'data-t="{t}"') for t in types]
    P.v("V1 shapes counted in the drawn picture equal the key", got == counts, got)
    P.v("V1b counts are all different and total 15", len(set(got)) == 5 and sum(got) == 15)
    cv = code_verify(counts, table, word, 1, 9)
    P.v("V2 code word spells SHAPE", cv["spelled_ok"])
    P.v("V3 single-slip detection >=98%", cv["rate"] >= .98, f'{cv["rate"]:.3f}')
    P["cv"] = cv
    chk_code = code_check(table)
    P["model"] = dict(truth=list(counts), domains=[list(range(1, 10))] * 5, check=lambda ans: sum(ans) == 15 and chk_code(ans), numeric=True)
    P["mech_plain"] = "The five counts add to 15, and a code word (5 letters)"
    return P

# ---------------------------------------------------------------- P06 (placed here with the other geometry page)
SHAPE_PROPS = {   # straight sides, curved sides, corners, all sides equal, two long + two short
    "circle":  dict(straight=0, curved=1, corners=0, equal=False, longshort=False),
    "half":    dict(straight=1, curved=1, corners=2, equal=False, longshort=False),
    "quarter": dict(straight=2, curved=1, corners=3, equal=False, longshort=False),
    "tri":     dict(straight=3, curved=0, corners=3, equal=False, longshort=False),
    "square":  dict(straight=4, curved=0, corners=4, equal=True,  longshort=False),
    "rect":    dict(straight=4, curved=0, corners=4, equal=False, longshort=True),
}
SHAPE_WORD = {"circle": "circle", "half": "half circle", "quarter": "quarter circle", "tri": "triangle", "square": "square", "rect": "rectangle"}

def sclause(c):
    k, v = c
    if k == "straight": return "I have no straight sides." if v == 0 else (f"I have {v} straight side." if v == 1 else f"I have {v} straight sides.")
    if k == "curved": return "I have 1 curved side."
    if k == "corners": return "I have no corners." if v == 0 else f"I have {v} corners."
    if k == "equal": return "All my sides are the same length."
    if k == "longshort": return "Two sides are long and two are short."

def sclause_ok(shape, c):
    k, v = c
    return SHAPE_PROPS[shape][k] == v

RIDDLES = {   # two clauses each, chosen so that the pair names exactly one shape
    "circle":  [("curved", 1), ("straight", 0)],
    "square":  [("straight", 4), ("equal", True)],
    "rect":    [("straight", 4), ("longshort", True)],
    "half":    [("curved", 1), ("straight", 1)],
    "quarter": [("curved", 1), ("straight", 2)],
    "tri":     [("corners", 3), ("straight", 3)],
}

def solve_riddle_shape(clauses):
    return [sh for sh in SHAPE_PROPS if all(sclause_ok(sh, c) for c in clauses)]

def page06():
    rng = random.Random(606)
    word = "JACKET"
    order = list(SHAPE_PROPS); rng.shuffle(order)               # riddle i is about order[i]
    letter = dict(zip(order, word))
    shown = list(SHAPE_PROPS); rng.shuffle(shown)
    rots = {"circle": [0], "half": [0, 90, 180, 270], "quarter": [0, 90, 180, 270], "tri": [0, 180], "square": [0, 45], "rect": [0, 90]}
    cards = ""
    for sh in shown:
        rot = rng.choice(rots[sh])
        cards += (f'<div class="card"><span class="shp">{svg(22, 22, shape_svg(sh, 11, 11, 19, rot=rot, fill="#fff", sw=0.6))}</span>'
                  f'<span class="cl">{letter[sh]}</span></div>')
    rows = ""
    for i, sh in enumerate(order):
        txt = "<br>".join(sclause(c) for c in RIDDLES[sh])
        rows += f'<div class="riddle"><span class="no">{i+1}</span><div class="rtext">{txt}</div><span class="ab"></span></div>'
    body = f'<div class="cards">{cards}</div><div class="riddles">{rows}</div>'
    P = Page(no=6, title="Shape Riddles", tier=2, topic="2D shapes: name and describe (straight and curved sides)",
             strand="Measurement and Geometry - Geometry", syll="Geometry 1.1 (identify, name, describe and classify 2D shapes)",
             ptype="Riddles + code-breaker", mech="K1 shape letters in riddle order spell a word (6 letters)",
             mech_plain="Letters of the six shapes, in riddle order, spell a word (6 letters)",
             instr=["Each riddle is about one shape.", "Find the shape it describes.", "Write that shape's letter in the box."],
             body=body, check="Read your six letters in order. Do they spell a word? You can wear it.", check_boxes=6,
             key=dict(answers=", ".join(f"{i+1}) {SHAPE_WORD[sh]} ({letter[sh]})" for i, sh in enumerate(order)), check_result=f"Word: {word}"),
             note="Pupils match each description to a shape picture. Each description has two parts, and both are needed to tell similar shapes apart (for example square and rectangle, half circle and quarter circle). The shapes are turned so pupils read the shape, not its position.",
             seed=606)
    P.v("V1 every riddle names exactly one shape", all(solve_riddle_shape(RIDDLES[sh]) == [sh] for sh in order))
    P.v("V1b the first part of every riddle alone fits more than one shape", all(len(solve_riddle_shape([c])) > 1 for sh in order for c in RIDDLES[sh][:1]))
    P.v("V2 letters in riddle order spell JACKET", "".join(letter[sh] for sh in order) == word)
    wrong = [pp for pp in itertools.permutations(word) if "".join(pp) != word]
    real = sum("".join(pp).lower() in WORDS for pp in wrong)
    P.v("V3 wrong orders that still spell a word <= 5%", real / len(wrong) <= .05, f"{real}/{len(wrong)}")
    P.v("V5 word on safe list", word.lower() in WORDS)
    P["cv"] = dict(rate=1 - real / len(wrong), single_total=len(wrong), single_detected=len(wrong) - real)
    P["model"] = dict(truth=list(word), domains=[list(word)] * 6, check=letters_check(), perm=list(range(6)))
    return P

# ---------------------------------------------------------------- P20
FRUIT = ["Apple", "Banana", "Orange", "Grape", "Pear"]

def graph_clue_ok(cnt, c):
    k = c[0]
    if k == "less": return cnt[c[1]] == cnt[c[2]] - c[3]
    if k == "more": return cnt[c[1]] == cnt[c[2]] + c[3]
    if k == "same": return cnt[c[1]] == cnt[c[2]]
    if k == "total": return sum(cnt.values()) == c[1]

def graph_text(c):
    c = tuple(c) + (0, 0)
    k = c[0]
    if k == "less": return f"{c[1]} has {c[3]} fewer than {c[2]}."
    if k == "more": return f"{c[1]} has {c[3]} more than {c[2]}."
    if k == "same": return f"{c[1]} has the same as {c[2]}."
    return f"{c[1]} children chose in all."

def solve_graph(known, clues):
    out = []
    unk = [f for f in FRUIT if f not in known]
    for vals in itertools.product(range(0, 10), repeat=len(unk)):
        cnt = dict(known); cnt.update(zip(unk, vals))
        if all(graph_clue_ok(cnt, c) for c in clues): out.append(cnt)
    return out

def page20():
    rng = random.Random(2020)
    while True:
        a = rng.randint(2, 5); b = rng.randint(3, 5)
        d1 = rng.randint(2, 4); d2 = rng.randint(1, 2); d3 = rng.randint(1, 2)
        cnt = {"Apple": a, "Banana": b, "Orange": a + d1, "Grape": b + d2, "Pear": b - d3}
        if min(cnt.values()) < 1 or max(cnt.values()) > 9: continue
        vals = sorted(cnt.values())
        if vals[-1] == vals[-2] or vals[0] == vals[1]: continue
        known = {"Apple": a, "Banana": b}
        # three difference clues, one for each missing row; the total is NOT a clue (it is the check)
        cl = [("more", "Orange", "Apple", d1), ("more", "Grape", "Banana", d2), ("less", "Pear", "Banana", d3)]
        if len(solve_graph(known, cl)) != 1: continue
        break
    total = sum(cnt.values())
    most = max(cnt, key=cnt.get); least = min(cnt, key=cnt.get)
    rows = ""
    for f in FRUIT:
        cells = "".join(f'<span class="gc">{"<i class=dotc></i>" if f in known and k < known[f] else ""}</span>' for k in range(9))
        rows += f'<div class="grow2"><b class="gl">{f}</b>{cells}</div>'
    clues = "".join(f"<li>{graph_text(c)}</li>" for c in cl)
    body = (f'<div class="blk"><p class="lead">Children chose a fruit. <span class="dotc inl"></span> = 1 child.</p><div class="pgraph">{rows}</div></div>'
            f'<ul class="clues">{clues}</ul>'
            f'<div class="ansline">a) Most children chose <span class="ab wide"></span>.</div>'
            f'<div class="ansline">b) <b>{most}</b> has <span class="ab"></span> more than <b>{least}</b>.</div>')
    P = Page(no=20, title="Fruit Graph", tier=2, topic="Picture graphs: read, complete and answer",
             strand="Statistics - Data Analysis", syll="Picture graphs (read and interpret picture graphs)",
             ptype="Graph detective", mech="K3 total circles equals the stated total (the total is not a clue)",
             mech_plain="Total of all the circles must equal the stated total (the total is not used to find any row)",
             instr=["Two rows are done.", "Use the clues to draw the other rows.", "Draw one circle for each child.", "Then answer a and b."],
             body=body, check=f"Count all the circles. Is the total {total}?", check_boxes=None,
             key=dict(answers=", ".join(f"{f}: {cnt[f]}" for f in FRUIT) + f"; a) {most}; b) {cnt[most]-cnt[least]}", check_result=f"Total {total} circles"),
             note=f"Each circle stands for one child (a scale of 1). The three clues fix the three missing rows one by one. The total of {total} is printed only in the check strip, so it is a separate test: a pupil who misreads a clue or draws one circle too many or too few gets a different total.",
             seed=2020)
    sols = solve_graph(known, cl)
    P.v("V1 exactly one set of row counts satisfies the clues (total not used; all combinations tested)", len(sols) == 1 and sols[0] == cnt, len(sols))
    P.v("V1b the most/least answers are unique", sorted(cnt.values())[-1] != sorted(cnt.values())[-2] and sorted(cnt.values())[0] != sorted(cnt.values())[1])
    P.v("V2 total of all rows equals the total in the check strip", sum(sols[0].values()) == total)
    P.v("V2b the total is not one of the clues", all(c[0] != "total" for c in cl))
    P.v("V7 every row fits in 9 boxes", max(cnt.values()) <= 9)
    # V3: a clue misread by 1 or 2 changes the total
    tot = det = 0
    for f in ["Orange", "Grape", "Pear"]:
        for dlt in (-1, 1, -2, 2):
            tot += 1
            alt = dict(cnt); alt[f] += dlt
            if sum(alt.values()) != total: det += 1
    P.v("V3 one wrong row breaks the total", det == tot, f"{det}/{tot}")
    P["cv"] = dict(rate=det / tot, single_total=tot, single_detected=det)
    P["counts"] = cnt
    unk = ["Orange", "Grape", "Pear"]
    P["model"] = dict(truth=[cnt[f] for f in unk], domains=[list(range(0, 10))] * 3, check=lambda ans: sum(ans) + a + b == total, numeric=True)
    P["mini"] = mini_graph([(f, cnt[f]) for f in FRUIT])
    return P

PAGES = [page06, page15, page16, page17, page18, page19, page20]
