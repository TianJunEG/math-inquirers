"""New money and time pages: N13 Which Two Items? (P1-27), N14 Fewest Coins (P1-28), N17 How Long Does It Last? (P1-29), N18 Morning or Evening? (P1-30)."""
import random, itertools, re, math
from .common import *
from . import art
from .art import count_objs
from .pages_numbers import random_walk, count_routes, neighbours, maze_html
from .pages_stories import finish_code, PEOPLE
from .pages_measure import coins_svg, COIN_D, clock_svg, read_clock, tstr, hands_apart

# ---------------------------------------------------------------- N14 Fewest Coins (P1-28)
def fewest_dp(amount, coins=(5, 10, 20, 50)):
    best = [0] + [10 ** 9] * amount
    for a in range(1, amount + 1):
        for c in coins:
            if c <= a and best[a - c] + 1 < best[a]: best[a] = best[a - c] + 1
    return best[amount]

def purse_sum(svg_text):
    return sum(int(v) for v in re.findall(r'class="coinval"[^>]*>(\d+)<', svg_text))

def page28():
    rng = random.Random(2808)
    word = "STAMP"
    while True:
        fa = rng.choice([15, 25, 30, 40, 60, 70, 35, 45, 55, 65, 75, 80, 85, 95]); fb = rng.choice([15, 25, 30, 40, 60, 70, 35, 45, 55, 65, 75, 80, 85, 95])
        if fa == fb or fewest_dp(fa) == fewest_dp(fb): continue
        k5 = rng.randint(4, 9) * 5; k10 = rng.randint(3, 8) * 10
        target = rng.choice([20, 25, 30])
        right_pool = {20: [(20,), (10, 10), (10, 5, 5), (5, 5, 5, 5)], 25: [(20, 5), (10, 10, 5), (10, 5, 5, 5)], 30: [(20, 10), (10, 10, 10), (20, 5, 5), (10, 10, 5, 5)]}[target]
        wrong_pool = [c for c in [(10, 5), (20, 5), (10, 10, 5), (20, 10), (5, 5, 5), (10, 5, 5), (20, 20), (10, 10, 10), (20, 5, 5), (5, 5, 5, 5), (50,), (10, 10, 20)] if sum(c) != target and len(c) <= 4]
        nright = rng.randint(2, 4)
        right = rng.sample(right_pool, min(nright, len(right_pool))); nright = len(right)
        wrong = rng.sample(wrong_pool, 6 - nright)
        purses = right + wrong; rng.shuffle(purses)
        ans = [fewest_dp(fa), fewest_dp(fb), k5 // 5, k10 // 10, nright]
        if len(set(ans)) != 5 or min(ans) < 2 or max(ans) > 12: continue
        table = make_code_table(ans, word, rng, 1, 12, n_decoy=5, near=(1, -1, 2, -2, 3, -3), tries=80)
        if table: break
    legend = coins_svg([5, 10, 20, 50])
    order = [(fa, "F"), (fb, "F")]
    rows = ""
    for i, (amt, _) in enumerate(order):
        rows += f'<div class="qrow"><span class="no">{i+1}</span><span class="qt">Pay {amt}\u00a2 with the fewest coins. How many coins?</span><span class="ab"></span></div>'
    k5c = coins_svg([5]); k10c = coins_svg([10])
    rows += f'<div class="qrow"><span class="no">3</span><span class="qt">How many 5\u00a2 coins make {k5}\u00a2?</span>{k5c}<span class="ab"></span></div>'
    rows += f'<div class="qrow"><span class="no">4</span><span class="qt">How many 10\u00a2 coins make {k10}\u00a2?</span>{k10c}<span class="ab"></span></div>'
    pcs = [coins_svg(list(p)) for p in purses]
    pur = "".join(f'<div class="purse">{s}<span class="ab"></span></div>' for s in pcs)
    rows = f'<div class="qgrid">{rows}</div>'
    rows += (f'<div class="qrow" style="border-bottom:none"><span class="no">5</span><span class="qt">Tick each purse that holds exactly {target}¢. How many ticks?</span><span class="ab"></span></div>'
             f'<div class="purses">{pur}</div>')
    body = f'<div class="legend2"><span>Coins:</span>{legend}</div><div>{rows}</div>{code_block(table)}'
    P = Page(no=28, title="Fewest Coins", tier=1, topic="Money: counting coins in cents; fewest coins and ways to pay",
             strand="Number and Algebra - Money", syll="Money 1.1 (counting amount of money in cents up to $1; fewest coins and ways to pay come from school tests: problem solving)",
             ptype="Code-breaker (coins)", mech="K1 code word (5 letters)",
             instr=["Look at the coins.", "Write how many.", "Use the code table."],
             body=body, check="Write the letters in order. Do they spell a word?", check_boxes=5,
             key=dict(answers=f"1) {ans[0]}, 2) {ans[1]}, 3) {ans[2]}, 4) {ans[3]}, 5) {ans[4]} (ticked purses: " + ", ".join(str(i + 1) for i, p in enumerate(purses) if sum(p) == target) + ")", check_result=f"Code word: {word}"),
             note=("Coins are 5¢, 10¢, 20¢ and 50¢ (original drawings with the value and the word cents). Two items ask for the fewest coins, two ask how many of one coin make an amount, and one asks the pupil to tick the purses that hold exactly the amount and say how many. "
                   "Fewest coins and ways to pay come from the kinds of question in school tests; the syllabus outcome is counting money."),
             seed=2808)
    got = [fewest_dp(int(m)) for m in re.findall(r"Pay (\d+)¢", rows)]
    km = re.findall(r"How many (\d+)\u00a2 coins make (\d+)\u00a2", rows)
    tk = re.search(r"exactly (\d+)\u00a2", rows)
    solved = got + [int(n_) // int(v_) for v_, n_ in km] + [sum(1 for s in pcs if purse_sum(s) == int(tk.group(1)))]
    P.v("V1 independent solver (coin-change search over the printed amounts; coin values summed from each drawn purse) equals the key", solved == ans, solved)
    P.v("V1b the coins shown beside questions 3 and 4 have the values asked", purse_sum(k5c) == 5 and purse_sum(k10c) == 10)
    P.v("V1c answers distinct and within 12", len(set(ans)) == 5 and max(ans) <= 12)
    P.v("V1d the purses show 2 to 4 exact ones and several near-miss ones", 2 <= nright <= 4 and all(sum(p) != target for p in wrong))
    finish_code(P, ans, table, word, 1, 12, plain="Code word (5 letters)")
    return P

# ---------------------------------------------------------------- N13 Which Two Items? (P1-27)
ITEM_ICONS = ["kite", "ball", "drum", "car", "cup", "boat"]
ITEM_NAMES = {"kite": "kite", "ball": "ball", "drum": "drum", "car": "toy car", "cup": "cup", "boat": "boat"}

def icon_svg(kind, mm=11):
    return common_svg_obj(kind, mm)

def common_svg_obj(kind, mm):
    return ('<svg xmlns="http://www.w3.org/2000/svg" width="%smm" height="%smm" viewBox="0 0 20 20"><g class="obj" data-k="%s">%s</g></svg>' % (mm, mm, kind, art.OBJ_PATHS[kind]))

def page27():
    rng = random.Random(2707)
    word = "MAGNET"
    while True:
        prices = sorted(rng.sample(range(2, 26), 6))
        idx = list(range(6)); rng.shuffle(idx)
        pairs = [tuple(sorted(idx[0:2])), tuple(sorted(idx[2:4])), tuple(sorted(idx[4:6]))]      # item numbers in price order: lower index = cheaper
        sums = [prices[i] + prices[j] for i, j in pairs]
        if len(set(sums)) != 3: continue
        allpairs = list(itertools.combinations(range(6), 2))
        if any(sum(1 for i, j in allpairs if prices[i] + prices[j] == s) != 1 for s in sums): continue
        order = [i for p in pairs for i in p]                           # item sequence the pupil writes
        letter = {item: word[k] for k, item in enumerate(order)}        # letter of item (in price order index)
        # display order of the board is a shuffle of the six items
        show = list(range(6)); rng.shuffle(show)
        icons = rng.sample(ITEM_ICONS, 6)
        # all single wrong pairs: the six letters read out must not spell a word
        bad = 0
        for b in range(3):
            for i in range(6):
                for j in range(6):
                    if i == j or (i, j) == pairs[b]: continue
                    seq = [letter[x] for p in pairs for x in p]; seq[2 * b] = letter[i]; seq[2 * b + 1] = letter[j]
                    if "".join(seq).lower() in BIG: bad += 1
        if bad == 0: break
    who = rng.sample(PEOPLE, 3)
    board = "".join(f'<div class="bitem">{common_svg_obj(icons[i], 17)}<span class="bn">{ITEM_NAMES[icons[i]]}<br><span class="bp">${prices[i]}</span></span><i class="cl">{letter[i]}</i></div>' for i in show)
    buyers = "".join(f'<div class="buyer"><span class="no">{k+1}</span><span class="bt">{who[k]} pays ${sums[k]} for 2 things.</span><span class="wk">$<span class="ab"></span> + $<span class="ab"></span></span><span class="lt">letters</span><span class="ab"></span><span class="ab"></span></div>' for k in range(3))
    body = f'<div class="blk"><p class="lead">The shop sells 6 things.</p><div class="board">{board}</div></div><div>{buyers}</div>'
    P = Page(no=27, title="Which Two Items?", tier=2, topic="Money in dollars: which two things cost exactly the amount paid",
             strand="Number and Algebra - Money", syll="Money 1.1 (dollars up to $100), 2.5 (adding within 100); guess and check, problem solving",
             ptype="Logic (price board)", mech="K1 letters of the chosen items, cheaper first, spell a word (6 letters)",
             mech_plain="The letters of the two things each buyer pays for, cheaper thing first, spell a word (6 letters)",
             instr=["Each person buys 2 things.", "Find which 2 things.", "Write their letters, cheaper first."],
             body=body, check="Read your six letters in order. Do they spell a word?", check_boxes=6,
             key=dict(answers="; ".join(f"{who[k]} pays ${sums[k]}: {ITEM_NAMES[icons[pairs[k][0]]]} ${prices[pairs[k][0]]} ({letter[pairs[k][0]]}) and {ITEM_NAMES[icons[pairs[k][1]]]} ${prices[pairs[k][1]]} ({letter[pairs[k][1]]})" for k in range(3)), check_result=f"Letters in order: {word}"),
             note=("Six things with prices in dollars. Each of three people pays an exact amount for two of them; for each amount only one pair of things works, and the three pairs use all six things. "
                   "The pupil tries pairs (guess and check), then writes the letter of the cheaper thing and then the dearer one. The six letters have exactly one arrangement that is a word, and every single wrong pair was tested: none spells a word. Prices are whole dollars within $100."),
             seed=2707)
    # independent solver from the printed board and sentences
    items = re.findall(r'data-k="(\w+)".*?<br><span class="bp">\$(\d+)</span></span><i class="cl">(\w)</i>', board, re.S)
    amounts = [int(x) for x in re.findall(r"pays \$(\d+) for 2 things", buyers)]
    seqs = ""
    for amt in amounts:
        found = [(a, b) for a, b in itertools.combinations(items, 2) if int(a[1]) + int(b[1]) == amt]
        assert len(found) == 1
        a, b = sorted(found[0], key=lambda t: int(t[1])); seqs += a[2] + b[2]
    P.v("V1 independent solver reads the printed board and amounts: exactly one pair per amount, and the letters read cheaper first spell the code word", seqs == word, seqs)
    P.v("V1b the three pairs are different things (all six used once)", len({x for p in pairs for x in p}) == 6)
    P.v("V3 none of the %d single wrong pairs spells a word" % (3 * 29), bad == 0)
    P.v("V3d the code word's letters have exactly ONE arrangement that is a word", anagrams(word) == [word.lower()], anagrams(word))
    P.v("V7 prices whole dollars, all within $100", max(prices) <= 100 and all(isinstance(p, int) for p in prices))
    P["cv"] = dict(rate=1.0, single_total=3 * 29, single_detected=3 * 29)
    pair_dom = [(i, j) for i in range(6) for j in range(6) if i != j]
    def chk(ans):
        s = "".join(letter[x] for pr in ans for x in pr)
        return s.lower() in BIG
    P["model"] = dict(truth=list(pairs), domains=[pair_dom] * 3, check=chk, numeric=False)
    P["facts"] = "100"
    return P

# ---------------------------------------------------------------- N17 How Long Does It Last? (P1-29)
def add_min(h, m, d):
    t = h * 60 + m + d
    return ((t // 60 - 1) % 12 + 1, t % 60)

def fmt(h, m): return f"{h}:{m:02d}"

def page29():
    rng = random.Random(2909)
    word = "SAILOR"
    ms = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55]
    domain = [fmt(h, m) for h in range(1, 13) for m in ms] + ["1 h", "30 min"]
    def pick():
        while True:
            h = rng.randint(1, 11); m = rng.choice(ms)
            if hands_apart(h, m) >= 25: return h, m
    while True:
        s1, s2, s3, s4, s5, s6 = (pick() for _ in range(6))
        e1 = add_min(*s1, 60); e2 = add_min(*s2, 30)
        a3 = add_min(*s3, 60); a4 = add_min(*s4, -30); a5 = add_min(*s5, 30); a6 = add_min(*s6, -60)
        ans = ["1 h", "30 min", fmt(*a3), fmt(*a4), fmt(*a5), fmt(*a6)]
        if len(set(ans)) != 6 or hands_apart(*e1) < 25 or hands_apart(*e2) < 25: continue
        if not any(m + 30 >= 60 for h, m in (s2, s5)) and not (a4[1] + 30 >= 60): continue
        wrong = set()
        for (h, m), kind in ((s3, 60), (s4, -30), (s5, 30), (s6, -60)):
            other = {60: 30, -30: -60, 30: 60, -60: -30}[kind]
            wrong |= {fmt(*add_min(h, m, other)), fmt(*add_min(h, m, -kind)), fmt(*add_min(h, m, kind + (5 if kind > 0 else -5)))}
        wrong -= set(ans)
        table = make_code_table(ans, word, rng, 0, 0, n_decoy=4, tries=300, pool=sorted(wrong), domain=domain)
        if table: break
    def two_clocks(no, a, b):
        return (f'<div class="tcard"><div class="th"><span class="no">{no}</span>How long does it last?</div><div class="tclk"><div>{clock_svg(*a)}<small>start</small></div><span class="op">&rarr;</span><div>{clock_svg(*b)}<small>end</small></div></div>'
                f'<div class="ta">It lasts <span class="ab wide"></span></div></div>')
    cards = [two_clocks(1, s1, e1), two_clocks(2, s2, e2)]
    B = '<span class="ab"></span>'
    tt = ('<table class="tt"><tr><th></th><th>Show</th><th>Starts</th><th>Ends</th><th>Lasts</th></tr>'
          f'<tr><td><span class="no">3</span></td><td>Magic</td><td>{fmt(*s3)}</td><td>{B}</td><td>1 h</td></tr>'
          f'<tr><td><span class="no">4</span></td><td>Music</td><td>{B}</td><td>{fmt(*s4)}</td><td>30 min</td></tr>'
          f'<tr><td><span class="no">5</span></td><td>Puppets</td><td>{fmt(*s5)}</td><td>{B}</td><td>30 min</td></tr>'
          f'<tr><td><span class="no">6</span></td><td>Film</td><td>{B}</td><td>{fmt(*s6)}</td><td>1 h</td></tr></table>')
    body = (f'<div class="tcards">{"".join(cards)}</div><div class="blk">{tt}</div>{code_block(table)}')
    P = Page(no=29, title="How Long Does It Last?", tier=1, topic="Time: how long a thing lasts (1 h or 30 min) and when it ends",
             strand="Measurement and Geometry - Measurement", syll="Time 2.1, 2.3, 2.4 (telling time to 5 minutes; abbreviations h and min; duration of one hour or half hour)",
             ptype="Code-breaker (clocks and a timetable)", mech="K1 code word (6 letters)",
             instr=["Read the clocks and the table.", "Write 1 h, 30 min or a time.", "Use the code table."],
             body=body, check="Write the letters in order. Do they spell a word?", check_boxes=6,
             key=dict(answers=f"1) 1 h (starts {fmt(*s1)}, ends {fmt(*e1)}), 2) 30 min (starts {fmt(*s2)}, ends {fmt(*e2)}), 3) {fmt(*a3)}, 4) {fmt(*a4)}, 5) {fmt(*a5)}, 6) {fmt(*a6)}", check_result=f"Code word: {word}"),
             note=("Times are read to 5 minutes and written with digits. Durations are always 1 h (one hour) or 30 min (half an hour); h and min are the syllabus abbreviations and are used on this page only. "
                   "Questions 1 and 2 give the start and end clocks and ask how long. In the show table, two rows ask for an end time (add 1 h or 30 min) and two ask for a start time (go back 1 h or 30 min). "
                   "A 30 min step may pass the next whole hour. The table's decoys are the usual slips: adding when the pupil should go back, or using the wrong length."),
             seed=2909)
    rd = lambda s: read_clock(s)
    def dur(a, b): return ((b[0] % 12) * 60 + b[1] - (a[0] % 12) * 60 - a[1]) % 720
    solved = []
    for a_, b_ in ((s1, e1), (s2, e2)):
        d = dur(rd(clock_svg(*a_)), rd(clock_svg(*b_))); solved.append("1 h" if d == 60 else "30 min" if d == 30 else "?")
    rows_ = re.findall(r"<tr><td><span class=\"no\">\d</span></td><td>\w+</td><td>(.*?)</td><td>(.*?)</td><td>(1 h|30 min)</td></tr>", tt)
    for st, en, ln in rows_:
        d = 60 if ln == "1 h" else 30
        if "ab" in st: t = en.split(":"); solved.append(fmt(*add_min(int(t[0]), int(t[1]), -d)))
        else: t = st.split(":"); solved.append(fmt(*add_min(int(t[0]), int(t[1]), d)))
    P.v("V1 independent solver: clock hands read back from the drawings give the durations, the table rows are solved from their printed times; all equal the key", solved == ans, solved)
    P.v("V1b every clock shows a 5-minute time with hands at least 25 degrees apart", all(hands_apart(*t) >= 25 for t in (s1, e1, s2, e2)))
    P.v("V1c at least one 30 min step passes the next whole hour", any(m + 30 >= 60 for h, m in (s2, s5)) or a4[1] + 30 >= 60, "")
    finish_code(P, ans, table, word, 0, 0, domain)
    P["model"] = dict(truth=ans, domains=[domain] * 6, check=code_check(table), numeric=False)
    return P

# ---------------------------------------------------------------- N18 Morning or Evening? (P1-30)
# the solver's own table: event -> (suffix, earliest minute, latest minute) on a 24-hour count of minutes after midnight
SENSIBLE = {"wake up": ("am", 5 * 60, 8 * 60), "breakfast": ("am", 6 * 60, 9 * 60 + 30), "school starts": ("am", 7 * 60, 8 * 60 + 30),
            "recess": ("am", 9 * 60 + 30, 11 * 60), "lunch": ("pm", 12 * 60, 14 * 60), "play outside": ("pm", 15 * 60, 17 * 60 + 30),
            "dinner": ("pm", 18 * 60, 20 * 60), "bedtime": ("pm", 20 * 60, 21 * 60 + 30)}
# the generator's own table: event -> (suffix, list of (hour, minute) times as written)
GEN_TIMES = {"wake up": ("am", [(5, 30), (6, 0), (6, 30), (7, 0), (7, 30)]), "breakfast": ("am", [(6, 30), (7, 0), (7, 30), (8, 0), (8, 30), (9, 0)]),
             "school starts": ("am", [(7, 30), (8, 0), (8, 30)]), "recess": ("am", [(9, 30), (10, 0), (10, 30)]),
             "lunch": ("pm", [(12, 0), (12, 30), (1, 0), (1, 30)]), "play outside": ("pm", [(3, 0), (3, 30), (4, 0), (4, 30), (5, 0)]),
             "dinner": ("pm", [(6, 0), (6, 30), (7, 0), (7, 30), (8, 0)]), "bedtime": ("pm", [(8, 0), (8, 30), (9, 0)])}

def parse_cell(text):
    m = re.fullmatch(r"(\d+):(\d\d) (am|pm)", text[0]); h, mi, suf = int(m.group(1)), int(m.group(2)), m.group(3)
    t24 = (h % 12) * 60 + mi + (720 if suf == "pm" else 0)
    return t24, text[1]

def sensible(cell):
    t24, ev = cell; suf, lo, hi = SENSIBLE[ev]
    return lo <= t24 <= hi

def page30():
    rng = random.Random(3030)
    n = 4; L = 8
    evs = list(GEN_TIMES)
    for _ in range(20000):
        path = random_walk(rng, n, L)
        cellmap = {}; used = set()
        def good_cell():
            ev = rng.choice(evs); suf, ts = GEN_TIMES[ev]; h, m = rng.choice(ts)
            return (f"{h}:{m:02d} {suf}", ev)
        def bad_cell():
            ev = rng.choice(evs); suf, ts = GEN_TIMES[ev]; h, m = rng.choice(ts)
            if rng.random() < .7: return (f"{h}:{m:02d} {'pm' if suf == 'am' else 'am'}", ev)
            ev2 = rng.choice([e for e in evs if GEN_TIMES[e][0] != suf]); return (f"{h}:{m:02d} {suf}", ev2) if False else (f"{h}:{m:02d} {suf}", ev2)
        cells = {}
        for c in path:
            cells[c] = good_cell()
        dead = 0
        for c in path[:-1]:
            if dead >= 3: break
            opts = [q for q in neighbours(*c, n) if q not in cells]
            if opts and rng.random() < .5: cells[rng.choice(opts)] = good_cell(); dead += 1
        for r in range(n):
            for c in range(n):
                if (r, c) not in cells: cells[(r, c)] = bad_cell()
        if len(set(cells.values())) != 16: continue
        parsed = {c: parse_cell(v) for c, v in cells.items()}
        ok = lambda c: sensible(parsed[c])
        if sum(ok(c) for c in parsed) != L + dead: continue            # every off-route cell must be not sensible
        if not 2 <= dead <= 3: continue
        start, finish = path[0], path[-1]
        if count_routes(ok, n, start, finish) != 1: continue
        break
    else: raise RuntimeError("n18")
    texts = [[f'<span class="tm">{cells[(r, c)][0]}</span><span class="ev">{cells[(r, c)][1]}</span>' for c in range(n)] for r in range(n)]
    cellhtml = [[f'<div class="dm" style="gap:1mm">{texts[r][c]}</div>' for c in range(n)] for r in range(n)]
    body = maze_html(n, cellhtml, start, finish).replace('class="maze"', 'class="maze tall"')
    P = Page(no=30, title="Morning or Evening?", tier=1, topic="Time: am and pm with times to 5 minutes",
             strand="Measurement and Geometry - Measurement", syll="Time 2.1, 2.2 (telling time to 5 minutes; use of am and pm)",
             ptype="Maze / path", mech="K6 route closes at FINISH through the stated number of boxes",
             instr=["Start at START.", "Step only on boxes that make sense.", "Move up, down, left or right."],
             mech_plain="Route: the line must reach FINISH through the right number of boxes, and every box must make sense (the right am or pm for the event)",
             body=body, check=f"Does your line reach FINISH? Count its boxes: are there {L}? Does each box make sense?", check_boxes=None,
             key=dict(answers="Route (row, column from top-left): " + " -> ".join(f"({r+1},{c+1}) {cells[(r, c)][0]} {cells[(r, c)][1]}" for r, c in path), check_result=f"Route reaches FINISH through {L} boxes; every box is a sensible time for its event."),
             note=(f"A 4 by 4 grid of times with an event, for example a time for breakfast. am is the morning and pm is the afternoon and evening; times are written in digits with am or pm and no full stops. "
                   f"{L + dead} boxes make sense and {16 - L - dead} do not (the same time with the wrong am or pm, or a time that does not fit the event). {dead} sensible boxes beside the route lead nowhere, so the box count and FINISH catch a wrong turn."),
             seed=3030)
    allc = [(r, c) for r in range(n) for c in range(n)]
    parsed2 = {}
    for r in range(n):
        for c in range(n):
            m = re.search(r'class="tm">([^<]+)</span><span class="ev">([^<]+)<', texts[r][c]); parsed2[(r, c)] = parse_cell((m.group(1), m.group(2)))
    ok2 = lambda c: sensible(parsed2[c])
    P.v("V1 exactly one route start->finish over the boxes that make sense (times read back from the printed text, own 24-hour table, exhaustive DFS)", count_routes(ok2, n, start, finish) == 1)
    P.v("V3 dead-end boxes that make sense exist, and every off-route box does not", dead >= 2 and sum(ok2(c) for c in allc) == L + dead, dead)
    P.v("V3c a shortcut that ignores the rule is shorter than the route", abs(start[0] - finish[0]) + abs(start[1] - finish[1]) + 1 < L)
    P.v("V3d no time is written with full stops or o'clock/half past wording; all times are digits with am or pm", all(re.fullmatch(r"\d+:\d\d (am|pm)", cells[c][0]) for c in allc))
    P["cv"] = dict(rate=1.0, single_total=dead, single_detected=dead)
    P["route"] = path
    def legal(rt):
        if len(rt) != L or len(set(rt)) != L or rt[0] != start or rt[-1] != finish: return False
        return all(abs(a[0]-b[0]) + abs(a[1]-b[1]) == 1 for a, b in zip(rt, rt[1:])) and all(ok2(c) for c in rt)
    P["model"] = dict(truth=list(path), domains=[allc] * L, check=legal, numeric=False)
    P["mini"] = mini_route(n, path)
    P["facts"] = "12 11 10 9 8 7 6 5 4 3 2 1"
    return P

PAGES = [page27, page28, page29, page30]
