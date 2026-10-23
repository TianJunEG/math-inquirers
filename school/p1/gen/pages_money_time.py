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
        kv = rng.choice([5, 10]); kn = kv * rng.randint(4, 9)
        if kv == 10: kn = kv * rng.randint(3, 8)
        target = rng.choice([20, 25, 30])
        right_pool = {20: [(20,), (10, 10), (10, 5, 5), (5, 5, 5, 5)], 25: [(20, 5), (10, 10, 5), (10, 5, 5, 5)], 30: [(20, 10), (10, 10, 10), (20, 5, 5), (10, 10, 5, 5)]}[target]
        wrong_pool = [c for c in [(10, 5), (20, 5), (10, 10, 5), (20, 10), (5, 5, 5), (10, 5, 5), (20, 20), (10, 10, 10), (20, 5, 5), (5, 5, 5, 5), (50,), (10, 10, 20)] if sum(c) != target and len(c) <= 4]
        nright = rng.randint(2, 4)
        right = rng.sample(right_pool, min(nright, len(right_pool))); nright = len(right)
        wrong = rng.sample(wrong_pool, 6 - nright)
        purses = right + wrong; rng.shuffle(purses)
        ans = [fewest_dp(fa), fewest_dp(fb), kn // kv, nright]
        # fifth answer: the ten coins page keeps a second fewest item with its own count
        fc = rng.choice([15, 25, 30, 40, 60, 70, 35, 45, 55, 65, 75, 80, 85, 95])
        ans.insert(2, fewest_dp(fc))
        if fc in (fa, fb) or len(set(ans)) != 5 or min(ans) < 2 or max(ans) > 12: continue
        table = make_code_table(ans, word, rng, 1, 12, n_decoy=5, near=(1, -1, 2, -2, 3, -3), tries=80)
        if table: break
    legend = coins_svg([5, 10, 20, 50])
    order = [(fa, "F"), (fb, "F"), (fc, "F")]
    rows = ""
    for i, (amt, _) in enumerate(order):
        rows += f'<div class="qrow"><span class="no">{i+1}</span><span class="qt">Pay {amt}¢ with the fewest coins. How many coins?</span><span class="ab"></span></div>'
    kcoin = coins_svg([kv])
    rows += f'<div class="qrow"><span class="no">4</span><span class="qt">How many {kv}¢ coins make {kn}¢?</span>{kcoin}<span class="ab"></span></div>'
    pcs = [coins_svg(list(p)) for p in purses]
    pur = "".join(f'<div class="purse">{s}<span class="ab"></span></div>' for s in pcs)
    rows += (f'<div class="qrow" style="border-bottom:none"><span class="no">5</span><span class="qt">Tick each purse that holds exactly {target}¢. How many ticks?</span><span class="ab"></span></div>'
             f'<div class="purses">{pur}</div>')
    body = f'<div class="blk"><p class="lead">Coins:</p><div class="legend2">{legend}</div></div><div>{rows}</div>{code_block(table)}'
    P = Page(no=28, title="Fewest Coins", tier=1, topic="Money: counting coins in cents; fewest coins and ways to pay",
             strand="Number and Algebra - Money", syll="Money 1.1 (counting amount of money in cents up to $1; fewest coins and ways to pay come from school tests: problem solving)",
             ptype="Code-breaker (coins)", mech="K1 code word (5 letters)",
             instr=["Look at the coins.", "Write how many.", "Use the code table."],
             body=body, check="Write the letters in order. Do they spell a word?", check_boxes=5,
             key=dict(answers=f"1) {ans[0]}, 2) {ans[1]}, 3) {ans[2]}, 4) {ans[3]}, 5) {ans[4]} (ticked purses: " + ", ".join(str(i + 1) for i, p in enumerate(purses) if sum(p) == target) + ")", check_result=f"Code word: {word}"),
             note=("Coins are 5¢, 10¢, 20¢ and 50¢ (original drawings with the value and the word cents). Three items ask for the fewest coins, one asks how many of one coin make an amount, and one asks the pupil to tick the purses that hold exactly the amount and say how many. "
                   "Fewest coins and ways to pay come from the kinds of question in school tests; the syllabus outcome is counting money."),
             seed=2808)
    got = [fewest_dp(int(m)) for m in re.findall(r"Pay (\d+)¢", rows)]
    km = re.search(r"How many (\d+)¢ coins make (\d+)¢", rows)
    tk = re.search(r"exactly (\d+)¢", rows)
    solved = got + [int(km.group(2)) // int(km.group(1)), sum(1 for s in pcs if purse_sum(s) == int(tk.group(1)))]
    P.v("V1 independent solver (coin-change search over the printed amounts; coin values summed from each drawn purse) equals the key", solved == ans, solved)
    P.v("V1b the coin shown beside question 4 has the value asked", purse_sum(kcoin) == kv)
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
    board = "".join(f'<div class="bitem">{common_svg_obj(icons[i], 11)}<span class="bn">{ITEM_NAMES[icons[i]]}<br><span class="bp">${prices[i]}</span></span><i class="cl">{letter[i]}</i></div>' for i in show)
    buyers = "".join(f'<div class="buyer"><span class="no">{k+1}</span><span class="bt">{who[k]} pays ${sums[k]} for 2 things.</span><span class="ab"></span><span class="ab"></span></div>' for k in range(3))
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
