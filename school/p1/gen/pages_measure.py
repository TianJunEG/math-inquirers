"""Pages 6 and 15-20: o'clock clocks, money, length, time to 5 minutes, shape count, picture graph."""
import random, itertools, re, math
from .common import *
from .pages_numbers import grid_table, howto_grid

# ---------------------------------------------------------------- P15
COIN_REAL = {5: 16.2, 10: 18.5, 20: 21.4, 50: 24.7}        # real diameters in mm: only the RATIOS are used (a fact, not a design); the coins are drawn at 0.9 of these, bigger than real
COIN_D = {v: d * 0.76 for v, d in COIN_REAL.items()}

def _motif(v, cx, cy, u):
    """an ORIGINAL small picture per value (not any real coin design): leaf (5), star (10), flower (20), sailboat (50); u is the coin radius"""
    k = u * 0.15; st = 'fill="none" stroke="#000" stroke-width="0.35" stroke-linejoin="round" stroke-linecap="round"'
    if v == 5:
        return f'<path d="M{cx-k*1.3:.2f},{cy+k*0.6:.2f} Q{cx-k*0.2:.2f},{cy-k*1.6:.2f} {cx+k*1.3:.2f},{cy-k*0.9:.2f} Q{cx+k*0.6:.2f},{cy+k*1.0:.2f} {cx-k*1.3:.2f},{cy+k*0.6:.2f} Z" {st}/>'
    if v == 10:
        pts = " ".join(f"{cx+(k*1.5 if i%2==0 else k*0.65)*math.sin(i*math.pi/5):.2f},{cy-(k*1.5 if i%2==0 else k*0.65)*math.cos(i*math.pi/5):.2f}" for i in range(10))
        return f'<polygon points="{pts}" {st}/>'
    if v == 20:
        petals = "".join(f'<circle cx="{cx+k*1.0*math.sin(i*math.pi*2/5):.2f}" cy="{cy-k*1.0*math.cos(i*math.pi*2/5):.2f}" r="{k*0.7:.2f}" {st}/>' for i in range(5))
        return petals + f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r="{k*0.45:.2f}" {st}/>'
    return (f'<path d="M{cx:.2f},{cy-k*1.5:.2f} L{cx+k*1.2:.2f},{cy+k*0.5:.2f} L{cx:.2f},{cy+k*0.5:.2f} Z M{cx-k*1.5:.2f},{cy+k*0.9:.2f} L{cx+k*1.5:.2f},{cy+k*0.9:.2f} L{cx+k*0.9:.2f},{cy+k*1.6:.2f} L{cx-k*0.9:.2f},{cy+k*1.6:.2f} Z" {st}/>')

def coins_svg(coins):
    p = []; x = 1; H = COIN_D[50] + 2; cy = H / 2
    for v in coins:
        d = COIN_D[v]; r = d / 2; cx = x + r
        p.append(f'<circle class="coin" cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" fill="#fff" stroke="#000" stroke-width="0.6"/>'
                 f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r-1.0:.1f}" fill="none" stroke="#000" stroke-width="0.3" stroke-dasharray="0.9 0.6"/>'
                 + _motif(v, cx, cy - r * 0.60, r) +
                 f'<text class="coinval" x="{cx:.1f}" y="{cy+r*0.22:.1f}" text-anchor="middle" font-family="Nunito Sans" font-weight="800" font-size="{r*0.62:.1f}" fill="#000">{v}</text>'
                 f'<text class="coinunit" x="{cx:.1f}" y="{cy+r*0.68:.1f}" text-anchor="middle" font-family="Nunito Sans" font-weight="800" font-size="{r*0.28:.1f}" fill="#000">cents</text>')
        x += d + 2.0
    return svg(x + 1, H + 1, "".join(p))

def page15():
    rng = random.Random(1515)
    word = "PIANO"
    while True:
        purses = [sorted([rng.choice([5, 10, 20, 50]) for _ in range(rng.randint(3, 5))], reverse=True) for _ in range(5)]
        tot = [sum(p) for p in purses]
        if len(set(tot)) == 5 and max(tot) <= 95 and min(tot) >= 25 and all(len(set(p)) >= 2 for p in purses):
            table = make_code_table(tot, word, rng, 5, 100, n_decoy=5, near=(5, -5, 10, -10, 15, -15), tries=80)
            if table: break
    svgs = [coins_svg(p) for p in purses]
    rows = "".join(f'<div class="crow"><span class="no">{i+1}</span><div class="csvg">{s}</div><div class="cans"><span class="ab wide"></span> <b>&cent;</b></div></div>' for i, s in enumerate(svgs))
    body = f'<div class="crows">{rows}</div>{code_block(table)}'
    P = Page(no=15, title="Coin Purses", tier=1, topic="Money: counting coins in cents (up to $1)",
             strand="Number and Algebra - Money", syll="Money (count money in cents up to $1)",
             ptype="Code-breaker", mech="K1 code word (5 letters)",
             instr=["Add the coins in each purse.", "Write the total in cents.", "Use the code table."],
             body=body, check="Write the letters in order. Do they spell a word?", check_boxes=5,
             key=dict(answers=", ".join(f"{i+1}) {t}\u00a2" for i, t in enumerate(tot)), check_result=f"Code word: {word}"),
             note="Coins used: 5\u00a2, 10\u00a2, 20\u00a2, 50\u00a2. Each coin shows its value and the word cents. The coins are original line drawings (a small picture on each, not a copy of any real coin), with sizes in the true proportion of the real coins. Totals stay below $1.",
             seed=1515)
    solved = [sum(int(m) for m in re.findall(r'class="coinval"[^>]*>(\d+)<', s)) for s in svgs]
    P.v("V1 coin values read from the drawing add to the key", solved == tot, solved)
    cv = code_verify(tot, table, word, 5, 100)
    code_checks(P, cv, word)
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
    word = "MONDAY"            # letters 1-5 sit beside the prices; letter 6 comes from the total
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
    chips_letters = word[:5]
    a, b = rng.sample(items, 2)
    total = truth[a] + truth[b]
    # the total's code table: no slip of the total gives another real word, and the five price letters plus one table letter
    # can be arranged into at least two common words (so the word cannot be guessed from the six letters alone)
    free6 = [c for c in ALPHA if c not in word and (word[:5] + c).lower() not in BIG]
    for _ in range(3000):
        ttab = build_table([total], word[5], rng, 2, 40, n_decoy=3, near=(1, -1, 2, -2, 10, -10), weighted=True, letters=free6)
        bad = [v for v, L in ttab.items() if v != total and (word[:5] + L).lower() in BIG]
        comp = {"".join(pp).lower() for L in ttab.values() for pp in itertools.permutations(chips_letters + L) if "".join(pp).lower() in COMMON}
        if not bad and len(comp) >= 2: break
    else:
        raise RuntimeError("p16 total table")
    chips = "".join(f'<span class="chip">${p} <i class="cl">{letter_of[p]}</i></span>' for p in prices)
    clues = "".join(f"<li>{price_text(c)}</li>" for c in cl)
    ans = ('<div class="ansgrid"><span></span><b>price</b><b>letter</b>' +
           "".join(f'<span class="nm">{it}</span><span class="ab"></span><span class="ab"></span>' for it in items) + '</div>')
    q = (f'<div class="ansline">The {a} and the {b} cost $<span class="ab"></span> together. Code letter <span class="ab"></span></div>'
         f'<div class="codetable"><b class="ctl">Code table</b>' + "".join(f'<div class="ct"><span class="n">${k}</span><span class="eq">=</span><b>{v}</b></div>' for k, v in ttab.items()) + '</div>')
    body = (f'<div class="blk"><p class="lead">The prices are:</p><div class="chips">{chips}</div></div>'
            f'<div class="twocol"><ul class="clues">{clues}</ul>{howto_grid()}</div>'
            f'<div class="twocol"><div>{grid_table(items, ["$%d" % p for p in prices])}</div><div>{ans}</div></div>{q}')
    diffs = [c for c in cl if c[0] == "diff"]
    P = Page(no=16, title="Shop Prices", tier=2, topic="Money: dollars, more and less",
             strand="Number and Algebra - Money", syll="Money (dollars up to $100) with 2.1 to 2.7 (add, subtract)",
             ptype="Logic grid + total", mech="K4 grid + K1 letter beside each price + code letter for the total (6 letters)",
             mech_plain="Letters beside the prices, then a code letter for the total, spell a word (6 letters)",
             instr=["Read the clues.", "Use the grid to cross and tick.", "Write each price, then its letter."],
             body=body, check="Read your six letters in order. Do they spell a word?", check_boxes=6,
             key=dict(answers=", ".join(f"{i}: ${truth[i]} ({letter_of[truth[i]]})" for i in items) + f"; the {a} and the {b} cost ${total} together (code letter {word[5]})", check_result=f"Letters in order: {word}"),
             note="Five items, five prices, each price with a letter. The page shows a worked example of crosses and ticks. " + " ".join(f"'${c[3]} more than' means a price ${c[3]} higher: pupils test each price against it." for c in diffs[:1]) + " The last answer is added from the grid and looked up in a small code table, so a wrong grid or a wrong sum changes the word.",
             seed=1616)
    sols = solve_prices(items, prices, cl)
    P.v("V1 exactly one price assignment satisfies all clues", len(sols) == 1 and sols[0] == truth, len(sols))
    P.v("V1b every clue needed", all(len(solve_prices(items, prices, [x for x in cl if x != c])) > 1 for c in cl))
    P.v("V2 letters beside the prices (item order) plus total letter spell " + word, "".join(letter_of[truth[i]] for i in items) + ttab[total] == word)
    wrong = [pp for pp in itertools.permutations(prices) if list(pp) != perm]
    real = sum(("".join(letter_of[v] for v in pp) + word[5]).lower() in BIG for pp in wrong)
    P.v("V3 wrong placements that still spell a word <= 5% (large word list)", real / len(wrong) <= .05, f"{real}/{len(wrong)}")
    P.v("V3b a wrong total never spells a word", not bad, bad)
    P.v("V4 guess resistance: the price letters and one table letter can be arranged into at least 2 common words", len(comp) >= 2, sorted(comp)[:5])
    P.v("V7 prices within $100, total within $40", max(prices) <= 100 and total <= 40)
    P["cv"] = dict(rate=1 - real / len(wrong), single_total=len(wrong), single_detected=len(wrong) - real)
    letters = [letter_of[truth[i]] for i in items]
    def chk(ans):
        t = ttab.get(ans[5])
        return t is not None and ("".join(ans[:5]) + t).lower() in BIG
    P["model"] = dict(truth=letters + [total], domains=[list(letter_of.values())] * 5 + [list(range(2, 41))], check=chk, perm=list(range(5)), numeric=False)
    P["mini"] = mini_ticks(5, 5, {(i, prices.index(truth[it])) for i, it in enumerate(items)})
    return P

# ---------------------------------------------------------------- P17
RULER_CM = 12

def ruler_unit(L, start=0):
    """strip of length L cm lying on a ruler 0..12 cm from the arrow at `start`; scale 10 mm per cm. A bold arrow above the left end of the strip and a bold
    tick on the ruler show where it starts. The ruler body extends 4.5 mm past 0 and 12 so the labels 0 and 12 are not crossed by the ruler's border."""
    x0 = 5; p = []; xs = x0 + start * 10
    p.append(f'<polygon class="arrow" points="{xs-2.2},0.4 {xs+2.2},0.4 {xs},3.7" fill="#000"/>')
    p.append(f'<rect class="strip" x="{xs}" y="4.0" width="{L*10}" height="5.0" fill="#fff" stroke="#000" stroke-width="0.5"/>')
    for k in range(0, L * 10, 3):
        p.append(f'<line x1="{xs+k}" y1="9.0" x2="{xs+min(k+3, L*10)}" y2="4.0" stroke="#000" stroke-width="0.25"/>')
    p.append(f'<rect x="0.5" y="9.9" width="{RULER_CM*10 + 2*x0 - 1}" height="8.0" fill="#fff" stroke="#000" stroke-width="0.5"/>')
    for k in range(RULER_CM * 10 + 1):
        h = 4.2 if k % 10 == 0 else (2.8 if k % 5 == 0 else 1.3)
        bold = k == start * 10
        p.append(f'<line x1="{x0+k}" y1="9.9" x2="{x0+k}" y2="{9.9+h}" stroke="#000" stroke-width="{1.1 if bold else (0.45 if k%10==0 else 0.3)}"/>')
    for k in range(RULER_CM + 1):
        p.append(f'<text x="{x0+k*10}" y="16.9" text-anchor="middle" font-family="Nunito Sans" font-weight="700" font-size="3.3" fill="#000">{k}</text>')
    return svg(RULER_CM * 10 + 2 * x0, 18.6, "".join(p))

def page17():
    rng = random.Random(1717)
    word = "LENGTH"
    while True:
        L = rng.sample(range(2, 11), 6)
        zero = set(rng.sample(range(6), 2))                                   # two strips start at 0; the other four start at 1, 2, 3 or 4
        starts = [0 if i in zero else rng.randint(1, min(4, 12 - L[i])) for i in range(6)]
        if sorted(starts)[2] == 0 or len(set(starts[i] for i in range(6) if i not in zero)) < 2: continue
        table = make_code_table(L, word, rng, 1, 12, n_decoy=4, near=(1, -1, 2, -2), tries=200)
        if table: break
    svgs = [ruler_unit(x, st) for x, st in zip(L, starts)]
    rows = "".join(f'<div class="lrow"><span class="no">{i+1}</span><div class="lsvg">{s}</div><span class="ab"></span> <span class="unit">cm</span></div>' for i, s in enumerate(svgs))
    body = f'<div class="lrows">{rows}</div>{code_block(table)}'
    P = Page(no=17, title="How Long?", tier=1, topic="Length: measure in centimetres",
             strand="Measurement and Geometry - Measurement", syll="Length 1.1, 1.2 (measure in cm, abbreviation cm)",
             ptype="Code-breaker", mech="K1 code word (6 letters)",
             instr=["Each strip starts at the arrow.", "Count the cm to the other end.", "Write the length. Use the code table."],
             body=body, check="Write the letters in order. Do they spell a word?", check_boxes=6,
             key=dict(answers=", ".join(f"{i+1}) {x} cm" for i, x in enumerate(L)), check_result=f"Code word: {word}"),
             note="A ruler is drawn under each strip at 10 mm to 1 cm. If the page is copied at a different scale the strip and ruler change together, so the reading from the drawn ruler stays right, but a real ruler laid on the page will not match: print at 100% (actual size) if pupils will use a real ruler. Two strips start at 0 and four start at 1 to 4 on the ruler; a bold arrow and a bold tick show the start. The Primary 1 length outcomes list measuring in cm and do not list measuring from a mark other than 0, so the offset strips are a small extension: the pupil counts the cm from the arrow to the end of the strip. Every length is a whole number of cm.",
             seed=1717)
    meas = []
    for s in svgs:
        w = float(re.search(r'class="strip"[^>]*? width="([\d.]+)"', s).group(1))
        meas.append(round(w / 10))
    P.v("V1 strip widths read against the 10 mm/cm scale equal the key", meas == L, meas)
    def _start(s_): return (float(re.search(r'class="strip" x="([\d.]+)"', s_).group(1)) - 5) / 10
    ar = [(float(re.search(r'class="arrow" points="([\d.]+),', s_).group(1)) + 2.2 - 5) / 10 for s_ in svgs]
    P.v("V1c every strip starts at its arrow (read from the drawing); two start at 0, four start at 1 to 4 and every strip ends on the ruler", [round(_start(s_)) for s_ in svgs] == starts == [round(a_) for a_ in ar] and starts.count(0) == 2 and max(st + x for st, x in zip(starts, L)) <= 12, starts)
    cv = code_verify(L, table, word, 1, 12)
    code_checks(P, cv, word)
    P["cv"] = cv
    P["model"] = code_model(L, table, 1, 12)
    P["mech_plain"] = "Code word (6 letters)"
    return P

# ---------------------------------------------------------------- clocks (P06 and P18)
def clock_svg(h, m):
    cx = cy = 22; p = [f'<circle cx="{cx}" cy="{cy}" r="20" fill="#fff" stroke="#000" stroke-width="0.7"/>']
    for k in range(0, 60, 5):                      # twelve long ticks (2.6 units, about 2 mm) at the hour marks
        a_ = math.radians(k * 6)
        p.append(f'<line x1="{cx+20*math.sin(a_):.2f}" y1="{cy-20*math.cos(a_):.2f}" x2="{cx+17.4*math.sin(a_):.2f}" y2="{cy-17.4*math.cos(a_):.2f}" stroke="#000" stroke-width="0.5"/>')
    for k in range(1, 13):
        a_ = math.radians(k * 30)
        p.append(f'<text x="{cx+14.2*math.sin(a_):.2f}" y="{cy-14.2*math.cos(a_)+1.3:.2f}" text-anchor="middle" font-family="Nunito Sans" font-weight="800" font-size="3.7" fill="#000">{k}</text>')
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

def time_table(answers, word, wrong_pool, domain, rng, tries=3000):
    """code table for times: answers get the word's letters; decoys are wrong readings (from wrong_pool); the safe-letter rules of make_code_table"""
    t = make_code_table(answers, word, rng, 0, 0, n_decoy=4, tries=tries, pool=wrong_pool, domain=domain)
    return t

def clock_items(qs, svgs, qtext):
    items = ""
    for i, ((h, m, *rest), s_) in enumerate(zip(qs, svgs)):
        q = qtext(qs[i])
        items += (f'<div class="citem"><span class="no">{i+1}</span>{s_}<div class="cmid"><div class="cq">{q}</div>'
                  f'<div class="ctime"><span class="ab"></span> : <span class="ab"></span></div></div></div>')
    return items

# ---------------------------------------------------------------- P06 (one star: o'clock and half past)
def page06():
    rng = random.Random(606)
    word = "SECOND"
    domain = [tstr(h, m) for h in range(1, 13) for m in (0, 30)]
    while True:
        hours = rng.sample([h for h in range(1, 13)], 6)
        kinds = [0, 0, 0, 30, 30, 30]; rng.shuffle(kinds)
        qs = [(h, m) for h, m in zip(hours, kinds)]
        if any(hands_apart(h, m) < 25 or (h, m) == (12, 0) for h, m in qs): continue
        ans = [tstr(h, m) for h, m in qs]
        # wrong readings a pupil makes: hour one too early or late, o'clock read as half past and the other way, hands swapped
        wrong = set()
        for h, m in qs:
            wrong |= {tstr(h % 12 + 1, m), tstr((h - 2) % 12 + 1, m), tstr(h, 30 - m)}
        wrong -= set(ans)
        table = time_table(ans, word, sorted(wrong), domain, rng, tries=400)
        if table: break
    svgs = [clock_svg(h, m) for h, m in qs]
    items = clock_items([(h, m) for h, m in qs], svgs, lambda q: "What is the time?")
    keys = list(table.items()); rng.shuffle(keys)
    ct = "".join(f'<div class="ct"><span class="n">{k}</span><span class="eq">=</span><b>{v}</b></div>' for k, v in keys)
    body = f'<div class="items g2">{items}</div><div class="blk"><p class="lead">Code table</p><div class="codetable">{ct}</div></div>'
    tt = set(table)
    cats = []
    if any(tstr(h % 12 + 1, m) in tt for h, m in qs): cats.append("the hour one too late")
    if any(tstr((h - 2) % 12 + 1, m) in tt for h, m in qs): cats.append("the hour one too early")
    if any(tstr(h, 30 - m) in tt for h, m in qs): cats.append("o'clock read as half past, or the other way round")
    P = Page(no=6, title="What Time Is It?", tier=1, topic="Time: o'clock and half past",
             strand="Measurement and Geometry - Measurement", syll="Time 2.1 (tell time: o'clock and half past)",
             ptype="Code-breaker", mech="K1 code word (6 letters)",
             instr=["Read each clock.", "Write the time in the boxes.", "Use the code table."],
             body=body, check="Write the letters in order. Do they spell a word?", check_boxes=6,
             key=dict(answers=", ".join(f"{i+1}) {tkey(h, m)}" for i, (h, m) in enumerate(qs)), check_result=f"Code word: {word}"),
             note="Three o'clock times and three half past times; the short hand is never close to the long hand. The code table holds the six right times and four wrong readings (" + ", ".join(cats) + "). Times to 5 minutes are on the Clock Time page.",
             seed=606)
    read = [read_clock(s_) for s_ in svgs]
    P.v("V1 clock hands read back from the drawing equal the intended times", read == [(((h - 1) % 12) + 1, m) for h, m in qs], read)
    P.v("V1b only o'clock and half past, no hands closer than 25 degrees", all(m in (0, 30) for h, m in read) and min(hands_apart(h, m) for h, m in qs) >= 25, round(min(hands_apart(h, m) for h, m in qs)))
    solved = [tstr(h, m) for h, m in read]
    cv = code_verify(solved, table, word, 0, 0, domain)
    code_checks(P, cv, word)
    P.v("V1c the table spells the word from the times read off the drawing", "".join(table[t] for t in solved) == word)
    P["cv"] = cv
    P["model"] = code_model(solved, table, 0, 0, domain)
    P["mech_plain"] = "Code word (6 letters)"
    P["min_apart"] = round(min(hands_apart(h, m) for h, m in qs))
    return P

# ---------------------------------------------------------------- P18 (two stars: times to 5 minutes, 1 hour or half an hour later)
def page18():
    rng = random.Random(1818)
    word = "CROWN"
    domain = [tstr(h, m) for h in range(1, 13) for m in range(0, 60, 5)]
    while True:
        qs = []
        for k in range(5):
            while True:
                h = rng.randint(1, 12); m = rng.choice([0, 30, 0, 30, 5, 10, 15, 20, 25, 35, 40, 45, 50, 55])
                if hands_apart(h, m) >= 25 and (h, m) != (12, 0): break          # keep the two hands easy to tell apart
            kind = "hour" if k % 2 == 0 else "half"
            qs.append((h, m, kind))
        ans = []
        for h, m, kind in qs:
            if kind == "hour": ans.append(((h % 12) + 1, m))
            else:
                mm = m + 30; hh = h + (1 if mm >= 60 else 0); ans.append((((hh - 1) % 12) + 1, mm % 60))
        if not (len({tstr(*a) for a in ans}) == 5 and len({tstr(h, m) for h, m, _ in qs}) == 5 and not any((h, m) in ans for h, m, _ in qs)): continue
        if sum(m not in (0, 30) for h, m, _ in qs) < 3: continue          # the five-minute reading is what the page is about
        shown = {tstr(h, m) for h, m, _ in qs}
        wrong = set()
        for (h, m, kind), a in zip(qs, ans):
            wrong |= {tstr(h, m), tstr(a[0], (a[1] + 5) % 60), tstr((a[0] % 12) + 1, a[1]), tstr(m // 5 if m >= 5 else 12, (h * 5) % 60)}
        wrong -= {tstr(*a) for a in ans}
        table = time_table([tstr(*a) for a in ans], word, sorted(wrong), domain, rng, tries=400)
        if table: break
    svgs = [clock_svg(h, m) for h, m, k in qs]
    items = clock_items(qs, svgs, lambda q: "What is the time<br><b>%s</b>?" % ("1 hour later" if q[2] == "hour" else "half an hour later"))
    keys = list(table.items()); rng.shuffle(keys)
    ct = "".join(f'<div class="ct"><span class="n">{k}</span><span class="eq">=</span><b>{v}</b></div>' for k, v in keys)
    body = f'<div class="items g2">{items}</div><div class="blk"><p class="lead">Code table</p><div class="codetable">{ct}</div></div>'
    crossing = [(h, m) for h, m, k in qs if k == "half" and m + 30 >= 60]
    tbl_times = set(table)
    cats = []
    if any(tstr(h, m) in tbl_times for h, m, _ in qs): cats.append("the time shown on the clock")
    if any(tstr(a[0], (a[1] + 5) % 60) in tbl_times for a in ans): cats.append("the right hour with the minutes 5 too many")
    if any(tstr((a[0] % 12) + 1, a[1]) in tbl_times for a in ans): cats.append("the hour one too late")
    if any(tstr(m // 5 if m >= 5 else 12, (h * 5) % 60) in tbl_times for h, m, _ in qs): cats.append("the hands read the wrong way round")
    P = Page(no=18, title="Clock Time", tier=2, topic="Time to 5 minutes: 1 hour and half an hour later",
             strand="Measurement and Geometry - Measurement", syll="Time 2.1 and 2.4 (tell time to 5 minutes; durations of 1 hour or half an hour)",
             ptype="Code-breaker", mech="K1 code word (5 letters)",
             instr=["Read each clock.", "Find the time later.", "Write it in the boxes."],
             body=body, check="Write the letters in order. Do they spell a word?", check_boxes=5,
             key=dict(answers=", ".join(f"{i+1}) shows {tkey(h,m)}, {'1 hour' if k == 'hour' else 'half an hour'} later {tkey(*a)}" for i, ((h, m, k), a) in enumerate(zip(qs, ans))), check_result=f"Code word: {word}"),
             note="Times to 5 minutes are usually taught late in Primary 1 (use the What Time Is It? page for o'clock and half past). Each item is two steps: read the clock, then add 1 hour or half an hour. "
                  + (f"{len(crossing)} of the half-hour additions cross the hour. " if crossing else "None of the half-hour additions cross the hour. ")
                  + (("The decoy times in the table are " + ", ".join(cats) + ". ") if cats else "")
                  + f"The hands are never closer than {int(min(hands_apart(h, m) for h, m, _ in qs))} degrees. a.m. and p.m. are not used on this page.",
             seed=1818)
    read = [read_clock(s_) for s_ in svgs]
    P.v("V1 clock hands read back from the drawing equal the intended times", read == [(((h - 1) % 12) + 1, m) for h, m, _ in qs], read)
    solved = []
    for (h, m), (_, _, kind) in zip(read, qs):
        solved.append(tstr(h % 12 + 1, m) if kind == "hour" else tstr(h + (1 if m + 30 >= 60 else 0), (m + 30) % 60))
    P.v("V1b later times computed from drawing equal the key", solved == [tstr(*a) for a in ans], solved)
    cv = code_verify(solved, table, word, 0, 0, domain)
    code_checks(P, cv, word)
    P.v("V1c the table spells the word from the later times", "".join(table[t] for t in solved) == word)
    P.v("V1d at least three of the five clocks show a time that is not o'clock or half past (what the page is for)", sum(m not in (0, 30) for h, m in read) >= 3)
    P["cv"] = cv
    P["model"] = dict(truth=[tstr(*a) for a in ans], domains=[domain] * 5, check=code_check(table), numeric=False)
    P["mech_plain"] = "Code word (5 letters)"
    return P

# ---------------------------------------------------------------- P19
def page19():
    rng = random.Random(1919)
    word = "PLANT"
    types = ["rect", "tri", "circle", "half", "quarter"]
    while True:
        counts = [1, 2, 3, 4, 5]; rng.shuffle(counts)
        table = make_code_table(counts, word, rng, 1, 9, n_decoy=4, near=(1, -1, 2, -2, 3, -3), tries=80, min_cand=3)
        if table: break
    pieces = [t for t, c in zip(types, counts) for _ in range(c)]
    rng.shuffle(pieces)
    rots = {"rect": [0, 90], "tri": [0, 90, 180, 270], "circle": [0], "half": [0, 90, 180, 270], "quarter": [0, 90, 180, 270]}
    inner = ['<rect x="0.5" y="0.5" width="169" height="101" fill="#fff" stroke="#000" stroke-width="0.7" rx="3"/>']
    for i, t in enumerate(pieces):
        r, c = divmod(i, 5)
        cx = 17 + c * 34 + rng.uniform(-1.5, 1.5); cy = 17 + r * 34 + rng.uniform(-1.5, 1.5)
        inner.append(shape_svg(t, round(cx, 1), round(cy, 1), 25, rot=rng.choice(rots[t]), fill="#fff", sw=0.6, cls="piece"))
    fig = svg(170, 102, "".join(inner))
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
    code_checks(P, cv, word)
    P["cv"] = cv
    chk_code = code_check(table)
    P["model"] = dict(truth=list(counts), domains=[list(range(1, 10))] * 5, check=lambda ans: sum(ans) == 15 and chk_code(ans), numeric=True)
    P.v("V3d the total 15 alone does not accept a swap of two counts, and the letters then spell no word", all(not chk_code(sw) for sw in [[counts[b_] if k == a_ else counts[a_] if k == b_ else counts[k] for k in range(5)] for a_, b_ in itertools.combinations(range(5), 2)]))
    P["mech_plain"] = "The five counts add to 15, and a code word (5 letters)"
    return P

# ---------------------------------------------------------------- P20
FRUIT = ["Apple", "Banana", "Orange", "Grape", "Pear"]

def face_svg(mm=10.5):
    """the picture symbol for 1 child: a smiley face (circle, two eyes, a smile)"""
    return (f'<svg class="face" xmlns="http://www.w3.org/2000/svg" width="{mm}mm" height="{mm}mm" viewBox="0 0 20 20"><circle cx="10" cy="10" r="9" fill="#fff" stroke="#000" stroke-width="1.1"/>'
            '<circle cx="7" cy="8" r="1.3" fill="#000"/><circle cx="13" cy="8" r="1.3" fill="#000"/>'
            '<path d="M5.6,12 Q10,17 14.4,12" fill="none" stroke="#000" stroke-width="1.1" stroke-linecap="round"/></svg>')

def fruit_icon(name, mm=9):
    """a simple line-art fruit beside a row label"""
    st = 'fill="#fff" stroke="#000" stroke-width="1" stroke-linejoin="round" stroke-linecap="round"'
    body = {
        "Apple": f'<path d="M10,5.5 C4,2.5 1.5,9 4.5,14 C6.5,17.5 8.5,17 10,16.2 C11.5,17 13.5,17.5 15.5,14 C18.5,9 16,2.5 10,5.5 Z" {st}/><path d="M10,5.5 C10,3.5 10.5,2.5 11.5,1.5" {st} fill="none"/><path d="M11,3.5 C13,1.5 15.5,2 15.5,2 C15,4 13,4.5 11,3.5 Z" {st}/>',
        "Banana": f'<path d="M3,5 C3,13 8,18 17,16 C12,16.5 6.5,12.5 5.5,4.5 Z" {st}/><path d="M3,5 L4,3 L6,4 L5.5,4.5" {st}/>',
        "Orange": f'<circle cx="10" cy="11" r="7" {st}/><path d="M10,4 C10,2.5 11,1.8 12.5,1.8 C12.5,3.5 11.5,4.2 10,4 Z" {st}/>',
        "Grape": f'<circle cx="6.5" cy="8" r="2.8" {st}/><circle cx="13.5" cy="8" r="2.8" {st}/><circle cx="10" cy="12.5" r="2.8" {st}/><circle cx="6.8" cy="13.5" r="0" {st}/><circle cx="10" cy="17" r="0" {st}/><path d="M10,5 C10,3 11,2 12.5,1.5" {st} fill="none"/>',
        "Pear": f'<path d="M10,3.5 C13,3.5 13.5,7 14.5,10 C16.5,13.5 14,17.5 10,17.5 C6,17.5 3.5,13.5 5.5,10 C6.5,7 7,3.5 10,3.5 Z" {st}/><path d="M10,3.5 C10,2.5 10.5,1.8 11.5,1.3" {st} fill="none"/>',
    }[name]
    return f'<svg class="fruit" xmlns="http://www.w3.org/2000/svg" width="{mm}mm" height="{mm}mm" viewBox="0 0 20 20">{body}</svg>' 

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

def reversed_clues(cl):
    """every non-empty subset of the clues with more and fewer exchanged: yields the graph a pupil gets after those misreadings"""
    for r in range(1, len(cl) + 1):
        for sub in itertools.combinations(range(len(cl)), r):
            yield sub

def misreadings(known, cl):
    """every way a pupil can misread the clues, as the rows they would draw: each of the three clues has its more/fewer exchanged or not, and its
    starting fruit exchanged (Apple for Banana and the other way round) or not; the correct reading (no change at all) is left out"""
    other = {"Apple": "Banana", "Banana": "Apple"}
    for flips in itertools.product((0, 1), repeat=len(cl)):
        for swaps in itertools.product((0, 1), repeat=len(cl)):
            if not any(flips) and not any(swaps): continue
            alt = dict(known)
            for i, c in enumerate(cl):
                base = other[c[2]] if swaps[i] else c[2]
                d = c[3] if c[0] == "more" else -c[3]
                alt[c[1]] = alt[base] + (-d if flips[i] else d)
            yield flips, swaps, alt

def passes_checks(alt, total, comb, xb, yb):
    """does a pupil who drew `alt` and answers a) and b) from it pass both checks of the strip? (any of the fruits tied for most may be named)"""
    if min(alt.values()) < 0 or sum(alt.values()) != total: return False
    top = max(alt.values()); bans = alt[xb] - alt[yb]
    return any(alt[f] + bans == comb for f in alt if alt[f] == top)

def page20():
    rng = random.Random(2020)
    while True:
        a = rng.randint(2, 5); b = rng.randint(3, 5)
        d1 = rng.randint(2, 4); d2 = rng.randint(1, 2); d3 = rng.randint(1, 2)
        if d1 == d2: continue                              # the first two clues must add different amounts, or Apple and Banana can be exchanged unseen
        if d2 == d3: continue                              # Grape = Banana + d2 and Pear = Banana - d3 must not be mirror images
        cnt = {"Apple": a, "Banana": b, "Orange": a + d1, "Grape": b + d2, "Pear": b - d3}
        if min(cnt.values()) < 1 or max(cnt.values()) > 9: continue
        vals = sorted(cnt.values())
        if vals[-1] == vals[-2] or vals[0] == vals[1]: continue
        known = {"Apple": a, "Banana": b}
        # three difference clues, one for each missing row; the total is NOT a clue (it is the check)
        cl = [("more", "Orange", "Apple", d1), ("more", "Grape", "Banana", d2), ("less", "Pear", "Banana", d3)]
        if len(solve_graph(known, cl)) != 1: continue
        total = sum(cnt.values())
        most = max(cnt, key=cnt.get); least = min(cnt, key=cnt.get)
        others = [f for f in FRUIT if f != most]
        pairs_ = [(x, y) for x in others for y in others if cnt[x] - cnt[y] >= 2]       # b) must not name the fruit that answers a)
        if not pairs_: continue
        xb, yb = rng.choice(pairs_); bans = cnt[xb] - cnt[yb]
        comb = cnt[most] + bans                                              # row of a) plus the answer to b)
        # a pupil who reads more as fewer (or the other way) on any set of the clues must fail the total or the second check
        ok = True
        for sub in reversed_clues(cl):
            alt = dict(known)
            for i, c in enumerate(cl):
                sgn = -1 if i in sub else 1
                base = alt[c[2]]
                alt[c[1]] = base + sgn * (c[3] if c[0] == "more" else -c[3])
            if min(alt.values()) < 0: continue                              # cannot be drawn: the pupil notices at once
            if sum(alt.values()) == total: ok = False
        if ok and any(passes_checks(alt, total, comb, xb, yb) for fl, sw, alt in misreadings(known, cl)): ok = False       # no misreading of more/fewer or of the starting fruit gets through
        if ok: break
    rows = ""
    for f in FRUIT:
        cells = "".join(f'<span class="gc">{face_svg(10.5) if f in known and k < known[f] else ""}</span>' for k in range(9))
        rows += f'<div class="grow2"><b class="gl">{fruit_icon(f)}<span>{f}</span></b>{cells}</div>'
    clues = "".join(f"<li>{graph_text(c)}</li>" for c in cl)
    body = (f'<div class="blk"><p class="lead">Children chose a fruit. {face_svg(6)} = 1 child. Draw a face or a circle.</p><div class="pgraph">{rows}</div></div>'
            f'<ul class="clues">{clues}</ul>'
            f'<div class="ansline">a) Most children chose <span class="ab wide"></span>.</div>'
            f'<div class="ansline">b) <b>{xb}</b> has <span class="ab"></span> more than <b>{yb}</b>.</div>')
    chk_lines = [f"Count all the faces. Is the total {total}?",
                 f"Add the faces in your a) row to your b) answer. Is the sum {comb}?"]
    P = Page(no=20, title="Fruit Graph", tier=2, topic="Picture graphs: read, complete and answer",
             strand="Statistics - Data Analysis", syll="Picture graphs (read and interpret picture graphs)",
             ptype="Graph detective", mech="K3 the total of all faces, and a second sum that uses the answers to a) and b) (neither is a clue)",
             mech_plain="Two sums: the total of all the faces, and the row chosen in a) plus the answer to b) (neither is used to find any row)",
             instr=["Two rows are done.", "Draw one face for each child.", "Use the clues. Answer a and b."],
             body=body, check=" ".join(chk_lines), check_lines=chk_lines, check_boxes=None,
             key=dict(answers=", ".join(f"{f}: {cnt[f]}" for f in FRUIT) + f"; a) {most}; b) {bans}", check_result=f"Total {total} faces; second sum {cnt[most]} + {bans} = {comb}"),
             note=f"Each smiley face stands for one child (a scale of 1: one picture symbol for one child). A pupil who draws a plain circle instead of a face counts the same, so the checks do not change. The three clues fix the three missing rows one by one. The total of {total} is printed only in the check strip, so it is a separate test: a pupil who misreads a clue or draws one circle too many or too few gets a different total. The second sum tests a) and b): it is {comb} only when the right row is chosen and b) is right. The three clues start from Apple or Banana; a pupil who starts a clue from the wrong one of the two, or who reads more as fewer, also gets a wrong total or a wrong second sum (every such mix was tried). Question b) names two other fruits, so it does not give away the answer to a). More and fewer are not mirror images here (the Grape clue is {d2} and the Pear clue is {d3}), and the first two clues add different amounts ({d1} and {d2}), so a pupil who swaps the two words or swaps Apple and Banana gets a different total or a different second sum.",
             seed=2020)
    sols = solve_graph(known, cl)
    P.v("V1 exactly one set of row counts satisfies the clues (total not used; all combinations tested)", len(sols) == 1 and sols[0] == cnt, len(sols))
    P.v("V1b the most/least answers are unique", sorted(cnt.values())[-1] != sorted(cnt.values())[-2] and sorted(cnt.values())[0] != sorted(cnt.values())[1])
    P.v("V2 total of all rows equals the total in the check strip", sum(sols[0].values()) == total)
    P.v("V2b the total is not one of the clues", all(c[0] != "total" for c in cl))
    P.v("V2c the second sum is right for the right answers", cnt[most] + (cnt[xb] - cnt[yb]) == comb)
    P.v("V2d question b) does not name the fruit that answers a)", most not in (xb, yb))
    P.v("V7 every row fits in 9 boxes", max(cnt.values()) <= 9)
    # V3: a clue misread by 1 or 2 changes the total
    tot = det = 0
    for f in ["Orange", "Grape", "Pear"]:
        for dlt in (-1, 1, -2, 2):
            tot += 1
            alt = dict(cnt); alt[f] += dlt
            if sum(alt.values()) != total: det += 1
    P.v("V3 one wrong row breaks the total", det == tot, f"{det}/{tot}")
    # V3e: more and fewer exchanged on any of the clues (7 combinations) is rejected by the total
    rev_ok = []
    for sub in reversed_clues(cl):
        alt = dict(known)
        for i, c in enumerate(cl):
            sgn = -1 if i in sub else 1
            alt[c[1]] = alt[c[2]] + sgn * (c[3] if c[0] == "more" else -c[3])
        rev_ok.append(min(alt.values()) < 0 or sum(alt.values()) != total)
    P.v("V3e reading more as fewer (or fewer as more) on any set of clues never passes the total", all(rev_ok), rev_ok)
    mis = [(fl, sw) for fl, sw, alt in misreadings(known, cl) if passes_checks(alt, total, comb, xb, yb)]
    n_mis = sum(1 for _ in misreadings(known, cl))
    P.v("V3f every misreading of the three clues (more/fewer exchanged, Apple and Banana exchanged, any mix: %d readings) fails the total or the second sum" % n_mis, not mis, mis[:3])
    sw12 = {k: v for k, v in known.items()}
    alt12 = dict(known); alt12["Orange"] = known["Banana"] + d1; alt12["Grape"] = known["Apple"] + d2; alt12["Pear"] = known["Banana"] - d3
    P.v("V3g the first two clues read with Apple and Banana exchanged do not pass both checks (the +%d and +%d clues differ)" % (d1, d2), not passes_checks(alt12, total, comb, xb, yb) and d1 != d2)
    P["cv"] = dict(rate=det / tot, single_total=tot, single_detected=det)
    P["counts"] = cnt
    unk = ["Orange", "Grape", "Pear"]
    # enumerated model: the three drawn rows, the fruit chosen in a) and the number written in b); the pupil's checks are the total and the second sum
    rows_ = [cnt[f] for f in unk]
    def chk(ans):
        r1, r2, r3, fa, nb = ans
        c2 = dict(cnt); c2.update(dict(zip(unk, (r1, r2, r3))))
        if sum(c2.values()) != total: return False
        return c2[fa] + nb == comb
    P["model"] = dict(truth=rows_ + [most, bans], domains=[list(range(0, 10))] * 3 + [list(FRUIT), list(range(0, 10))], check=chk, numeric=False)
    P["mini"] = mini_graph([(f, cnt[f]) for f in FRUIT])
    return P

PAGES = [page06, page15, page16, page17, page18, page19, page20]
