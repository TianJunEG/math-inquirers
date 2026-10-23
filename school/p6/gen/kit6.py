"""Primary 6 kit: fractions as stacked html, a small exact calculator that reads PRINTED text (the independent solvers use it),
and page builders for the mechanisms: code word, route (maze), lettered choices, matching, ordering and domino loop.
Everything is pure black and white. Each page module makes its items from a seed, re-solves them with separate code that reads the printed html (not the
generator's data), and hands validate.py a `model` for the independent wrong-answer enumeration."""
import random, itertools, re, html as _html
from fractions import Fraction as Fr
from decimal import Decimal
from .common import *
from .kit import *

BIG.update({"siring", "jailor"})
SY = lambda s: f'<span class="sy">{s}</span>'
PI = SY("π")
PIP = "π"
LITRE = SY("ℓ")
MLITRE = "m" + SY("ℓ")
SQRT = SY("√")
CBRT = SY("∛")
FSL = "⁄"          # fraction slash used in plain-text readings of stacked fractions

PEOPLE = ["Ali", "Mei", "Siti", "Ben", "Kumar", "Aisha", "Wei", "Ravi", "Jenny", "Lily", "Hana", "Tom", "Farid", "Grace", "Hui", "Nadia", "Daniel", "Priya", "Jun", "Alex"]
STRAND_FR = "Number and Algebra - Fractions"
STRAND_PC = "Number and Algebra - Percentage"
STRAND_RA = "Number and Algebra - Ratio"
STRAND_AL = "Number and Algebra - Algebra"
STRAND_AV = "Measurement and Geometry - Area and Volume"
STRAND_GE = "Measurement and Geometry - Geometry"
STRAND_ST = "Statistics"
STRAND_RV = "Revision of earlier years"

# ------------------------------------------------------------------------------------------------ fractions and numbers in html
def fh(n, d):
    return f'<span class="fr"><i>{n}</i><i>{d}</i></span>'

def frx(x):
    """a Fraction (or int) as html: a whole number or a stacked fraction"""
    x = Fr(x)
    return str(x.numerator) if x.denominator == 1 else fh(x.numerator, x.denominator)

def mixed(w, n, d):
    return f'<span class="mx">{w}</span>{fh(n, d)}'

def mxx(x):
    """a Fraction as a mixed number in html (a proper fraction or whole number stays as it is)"""
    x = Fr(x)
    if x.denominator == 1: return str(x.numerator)
    w = x.numerator // x.denominator
    return mixed(w, x.numerator - w * x.denominator, x.denominator) if w else fh(x.numerator, x.denominator)

def dec(x, places=None):
    """a decimal number as text without trailing noise: dec(Fr(157,2)) -> '78.5'"""
    x = Fr(x)
    if x.denominator == 1: return str(x.numerator)
    s = f"{float(x):.{places}f}" if places else format(Decimal(x.numerator) / Decimal(x.denominator), "f")
    return s.rstrip("0").rstrip(".") if "." in s and not places else s

def money(x):
    x = Fr(x)
    return f"${int(x)}" if x.denominator == 1 else f"${float(x):.2f}"

def ptxt(h):
    """the plain text a reader sees: stacked fractions become a⁄b, mixed numbers w_a⁄b; tags removed"""
    h = re.sub(r'<span class="mx">(\d+)</span>\s*<span class="fr"><i>(\d+)</i><i>(\d+)</i></span>', rf' \1_\2{FSL}\3 ', h)
    h = re.sub(r'<span class="fr"><i>(\d+)</i><i>(\d+)</i></span>', rf' \1{FSL}\2 ', h)
    h = re.sub(r'<span class="ab[^"]*"></span>', " ? ", h)           # an empty answer box reads as ?
    h = re.sub(r"<[^>]+>", " ", h)
    h = _html.unescape(h)
    return re.sub(r"\s+", " ", h).strip()

def pv(tok):
    """value of a printed number token: 3, 2.5, 3⁄4, 1_1⁄2"""
    tok = tok.strip()
    m = re.fullmatch(rf"(\d+)_(\d+){FSL}(\d+)", tok)
    if m: return Fr(int(m.group(1))) + Fr(int(m.group(2)), int(m.group(3)))
    m = re.fullmatch(rf"(\d+){FSL}(\d+)", tok)
    if m: return Fr(int(m.group(1)), int(m.group(2)))
    return Fr(Decimal(tok.replace(",", "")))

_NUM = rf"\d+_\d+{FSL}\d+|\d+{FSL}\d+|\d+\.\d+|\d+"
_TOK = re.compile(rf"\s*({_NUM}|[A-Za-z]|[+\-−×÷()√∛])")

class CalcError(Exception): pass

def tokens(s):
    s = s.strip(); out = []; i = 0
    while i < len(s):
        m = _TOK.match(s, i)
        if not m: raise CalcError(f"cannot read {s[i:i+12]!r}")
        out.append(m.group(1)); i = m.end()
        while i < len(s) and s[i] == " ": i += 1
    return out

def calc(s, env=None):
    """exact value of a printed arithmetic expression over fractions, decimals and letters (env gives each letter a value).
    + - × ÷ with the usual order, brackets, and a number or letter written next to a letter or bracket means multiply (3a, 2(a))"""
    toks = tokens(s); pos = [0]; env = env or {}
    def peek(): return toks[pos[0]] if pos[0] < len(toks) else None
    def take(): pos[0] += 1; return toks[pos[0] - 1]
    def isnum(t): return t is not None and re.fullmatch(_NUM, t) is not None
    def factor():
        t = take()
        if t == "(":
            v = expr(); assert take() == ")"; return v
        if isnum(t): return pv(t)
        if t == "−" or t == "-": return -factor()
        if t in ("√", "∛"):
            v = factor(); n = 2 if t == "√" else 3
            if v < 0: raise CalcError("root of a negative number")
            r = Fr(round(float(v) ** (1.0 / n))) if v.denominator == 1 else None
            if r is None or r ** n != v: raise CalcError(f"{t}{v} is not exact")
            return r
        if t.isalpha():
            if t not in env: raise CalcError("unknown letter " + t)
            return Fr(env[t])
        raise CalcError("bad token " + t)
    def term():
        v = factor()
        while True:
            t = peek()
            if t in ("×", "÷"):
                take(); w = factor(); v = v * w if t == "×" else v / w
            elif t is not None and (t.isalpha() or t == "("):          # implicit multiplication: 3a, 2(a + 1)
                v = v * factor()
            else: return v
    def expr():
        v = term()
        while peek() in ("+", "−", "-"):
            t = take(); w = term(); v = v + w if t == "+" else v - w
        return v
    v = expr()
    if pos[0] != len(toks): raise CalcError("left over " + str(toks[pos[0]:]))
    return v

def calch(h, env=None):
    return calc(ptxt(h), env)

# ------------------------------------------------------------------------------------------------ answer boxes
def abx(cls=""): return ab(cls)
def ans_frac():
    return '<span class="fans"><span class="ab w2"></span><span class="fline"></span><span class="ab w2"></span></span>'
def ans_ratio(k=2, cls="w2"):
    return " : ".join(f'<span class="ab {cls}"></span>' for _ in range(k))
def unit(u): return f'<span class="unit">{u}</span>'

# ------------------------------------------------------------------------------------------------ code-word page
def distinct(xs): return len(set(xs)) == len(xs)

def code_page(no, seed, title, tier, topic, strand, syll, oc, ptype, instr, cards, answers, table, word, lo, hi, key_answers, note,
              domain=None, fmt=str, ps=False, plain_mech=None, cols=None, ncols=2, pre_body="", post_body="", mech=None, check=None, table_cols=None):
    body = pre_body + (qgrid(cards, ncols) if isinstance(cards, list) else cards) + post_body + table_block(table, fmt, cols or table_cols)
    P = new_page(no, seed, title, tier, topic, strand, syll, oc, ptype, mech or f"K1 code word ({len(word)} letters)", instr, body, key_answers,
                 f"Code word: {word}", note, check_boxes=len(word), ps=ps)
    finish_code(P, answers, table, word, lo, hi, domain, plain_mech)
    P["facts"] = " ".join(str(v) for v in table)
    return P

def make_table(no, answers, rng, lo, hi, pool=None, domain=None, n_decoy=3, tries=60, n=None, **kw):
    res = code_table_any(no, n or len(answers), answers, rng, lo, hi, n_decoy=n_decoy, tries=tries, pool=pool, domain=domain, **kw)
    return res

# ------------------------------------------------------------------------------------------------ route (maze) page
def build_maze(rng, n, L, good, bad, ev, target, dead=2, tries=30000, min_dist=3, must=()):
    """good: list of html cells that equal `target`; bad: list of html cells that do not. ev(html) reads the printed cell.
    Returns (grid dict, path, start, finish) with exactly one simple route from START to FINISH over the cells equal to the target."""
    for _ in range(tries):
        path = random_walk(rng, n, L, min_dist=min_dist)
        if abs(path[0][0] - path[-1][0]) + abs(path[0][1] - path[-1][1]) + 1 >= L: continue
        pick = rng.sample(good, L + dead)
        grid = {c: pick[k] for k, c in enumerate(path)}
        d = 0
        for p in path[:-1]:
            if d >= dead: break
            opts = [q for q in neighbours(*p, n) if q not in grid]
            if opts and rng.random() < .6:
                q = rng.choice(opts); grid[q] = pick[L + d]; d += 1
        if d < dead: continue
        chosen = [rng.choice(g) for g in must]                      # one cell of each trap group is always on the grid
        rest = n * n - len(grid) - len(chosen)
        pool = [b for b in bad if b not in chosen]
        fill = chosen + (rng.sample(pool, rest) if len(pool) >= rest else [])
        if len(fill) != n * n - len(grid): raise RuntimeError("not enough bad cells")
        k = 0
        for r in range(n):
            for c in range(n):
                if (r, c) not in grid: grid[(r, c)] = fill[k]; k += 1
        if len(set(grid.values())) != n * n: continue
        ok = lambda cell: ev(grid[cell]) == target
        if count_routes(ok, n, path[0], path[-1]) == 1: return grid, path, path[0], path[-1]
    raise RuntimeError("maze")

def route_page(no, seed, title, tier, topic, strand, syll, oc, ptype, instr, rng, n, L, good, bad, ev, target, target_text, note, check=None, cls="maze tall", ps=False, dead=2, extra_note="", must=()):
    grid, path, start, finish = build_maze(rng, n, L, good, bad, ev, target, dead=dead, must=must)
    texts = [[grid[(r, c)] for c in range(n)] for r in range(n)]
    body = maze_html(n, texts, start, finish, cls=cls)
    P = new_page(no, seed, title, tier, topic, strand, syll, oc, ptype, "K6 route closes at FINISH", instr, body,
                 "Route (row, column from top-left): " + " -> ".join(f"({r+1},{c+1}) {ptxt(grid[(r, c)])}" for r, c in path),
                 f"Route reaches FINISH through {L} boxes; every box on it equals {target_text}.", note,
                 check=check or f"Does your line reach FINISH? Count its boxes: are there {L}? Does every box equal {target_text}?", mk=("route",), ps=ps,
                 mech_plain=f"Route: the line must reach FINISH through the right number of boxes, every box equal to {target_text}")
    g2 = {(r, c): grid[(r, c)] for r in range(n) for c in range(n)}
    ok2 = lambda cell: ev(g2[cell]) == target
    P.v("V1 exactly one route start->finish (exhaustive search, every cell evaluated from its printed text)", count_routes(ok2, n, start, finish) == 1)
    P.v("V3 dead-end boxes that also equal the target exist", dead >= 2)
    P.v("V3b a shortcut that ignores the rule is shorter than the route", abs(start[0]-finish[0]) + abs(start[1]-finish[1]) + 1 < L)
    P.v("V7b all boxes are different", len({ptxt(v) for v in g2.values()}) == n * n)
    P["cv"] = dict(rate=1.0, single_total=dead, single_detected=dead)
    allcells = [(r, c) for r in range(n) for c in range(n)]
    def legal(rt):
        if len(rt) != L or len(set(rt)) != L or rt[0] != start or rt[-1] != finish: return False
        return all(ok2(c) for c in rt) and all(abs(a[0]-b[0]) + abs(a[1]-b[1]) == 1 for a, b in zip(rt, rt[1:]))
    P["model"] = dict(truth=list(path), domains=[allcells] * L, check=legal, numeric=False)
    P["mini"] = mini_route(n, path)
    P["route_len"] = L
    return P

# ------------------------------------------------------------------------------------------------ lettered choices
def choice_letters_distinct(rng, word, n_opts, tries=800):
    """rows[i] = [right letter, wrong letters ...] with every decoy letter used in ONE row only (so a letter that is never right cannot be spotted by repetition) when
    the alphabet allows it; no other way of choosing one option per row spells a word of the large list"""
    avail = [c for c in ALPHA if c not in word]
    need = len(word) * (n_opts - 1)
    for _ in range(tries):
        pool = rng.sample(avail, need) if need <= len(avail) else [rng.choice(avail) for _ in range(need)]
        rows = [[word[i]] + pool[i * (n_opts - 1):(i + 1) * (n_opts - 1)] for i in range(len(word))]
        if not any(w2.lower() in BIG for w2 in ("".join(rows[i][c] for i, c in enumerate(combo)) for combo in itertools.product(range(n_opts), repeat=len(word)) if any(combo))):
            return rows
    return choice_letters(rng, word, n_opts)

def choice_page(no, seed, title, tier, topic, strand, syll, oc, ptype, instr, rng, rows, solve_row, note, word=None, n_opts=3, check=None, ps=False,
                key_rows=None, wide=False, grid=False):
    """rows: list of dict(stem=html, opts=[html,...], right=int). The letter beside the RIGHT option of row i is word[i]; wrong options carry decoy letters,
    chosen so that no other way of choosing one option in every row spells a word. solve_row(stem_html, [opt_html]) -> index reads the printed row."""
    if word is None:
        word = word_candidates(no, len(rows))[0]
    CLAIMED[no] = word
    letters = choice_letters_distinct(rng, word, n_opts)
    layout = []
    for r, lt in zip(rows, letters):
        opts = []
        for j, o in enumerate(r["opts"]):
            lab = lt[0] if j == r["right"] else lt[1 + (j if j < r["right"] else j - 1)]
            opts.append((o, lab, j == r["right"]))
        layout.append(opts)
    cards = []
    for i, (r, opts) in enumerate(zip(rows, layout)):
        o = "".join(f'<span class="chop"><i class="cl">{lab}</i><span class="cht">{h}</span></span>' for h, lab, _ in opts)
        cards.append(f'<div class="chrow"><span class="no">{i+1}</span><div class="chb"><div class="chs">{r["stem"]}</div><div class="cho{" wide" if wide else ""}">{o}</div></div></div>')
    body = f'<div class="chrows{" chgrid" if grid else ""}">' + "".join(cards) + '</div>'
    P = new_page(no, seed, title, tier, topic, strand, syll, oc, ptype, f"K1 the letter of the right choice in each row spells a word ({len(word)} letters, decoy letters on the other choices)", instr, body,
                 key_rows or "; ".join(f"{i+1}) {ptxt(r['opts'][r['right']])}" for i, r in enumerate(rows)), f"Word: {word}", note,
                 check=check or f"Write the {len(word)} letters in order. Do they spell a word?", check_boxes=len(word), mk=("code",), ps=ps,
                 mech_plain=f"Word from the letters of the right choices ({len(word)} letters)")
    solved = [solve_row(r["stem"], r["opts"]) for r in rows]
    P.v("V1 independent solver reads each printed row and picks the key's choice", solved == [r["right"] for r in rows], solved)
    other = choice_other_words(word, letters)
    P.v(f"V3 no other way of choosing spells a word (large word list, {len(BIG)} words)", not other, other[:3])
    P.v("V3d the code word's letters have exactly ONE arrangement that is a word", anagrams(word) == [word.lower()])
    P.v("V2 right choices read down the rows spell the word", "".join(l[0] for l in letters) == word)
    P["cv"] = dict(rate=1.0, single_total=len(rows) * (n_opts - 1), single_detected=len(rows) * (n_opts - 1))
    P["model"] = dict(truth=list(word), domains=[list(l) for l in letters], check=letters_check(), numeric=False)
    P["facts"] = ptxt(body)
    return P

# ------------------------------------------------------------------------------------------------ matching
def match_other_words(word, letters):
    """words of the large list that can be written by giving every item a DIFFERENT card (the rule 'use each card once'), or by changing one letter of the right word to any card letter"""
    n = len(word); out = set()
    for p in itertools.permutations(letters, n):
        s = "".join(p)
        if s != word and s.lower() in BIG: out.add(s)
    for i in range(n):
        for c in set(letters):
            s = word[:i] + c + word[i + 1:]
            if s != word and s.lower() in BIG: out.add(s)
    return sorted(out)

def match_letters(rng, word, n_cards, tries=400):
    """decoy letters for the cards that carry no letter of the word: no way of giving every item a different card, and no single changed letter, spells another word"""
    extra = n_cards - len(word)
    avail = [c for c in ALPHA if c not in word]
    for _ in range(tries):
        dec = rng.sample(avail, extra)
        if not match_other_words(word, list(word) + dec): return dec
    raise RuntimeError("match letters")

def match_page(no, seed, title, tier, topic, strand, syll, oc, ptype, instr, rng, items, cards, right, solve_item, note, word=None, check=None, ps=False,
               item_cols=1, card_cols=4, lead_items="Items", lead_cards="Cards", key_text=None, compact=False, vert=False):
    """items: list of html (one letter box each); cards: list of html (len = len(items) + 2); right[i] = index of the card that matches item i.
    Cards are labelled with letters: the right cards carry the letters of the code word in item order."""
    n = len(items)
    if word is None: word = word_candidates(no, n)[0]
    CLAIMED[no] = word
    dec = match_letters(rng, word, len(cards))
    lab = [None] * len(cards)
    for i, ci in enumerate(right): lab[ci] = word[i]
    k = 0
    for ci in range(len(cards)):
        if lab[ci] is None: lab[ci] = dec[k]; k += 1
    crd = "".join(f'<div class="mcd"><i class="cl">{lab[j]}</i><div class="mct">{cards[j]}</div></div>' for j in range(len(cards)))
    def one(i):
        h = items[i]
        if vert and "<!--cap-->" in h:
            top, cap = h.split("<!--cap-->", 1)
            return f'<div class="mit"><div class="mtop"><span class="no">{i+1}</span><span class="ab"></span></div><div class="mtt">{top}</div><div class="mcap">{cap}</div></div>'
        return f'<div class="mit"><span class="no">{i+1}</span><div class="mtt">{h}</div><span class="ab"></span></div>'
    its = "".join(one(i) for i in range(n))
    body = (f'<p class="lead">{lead_items}</p><div class="mgrid{" cmp" if compact else ""}{" vert" if vert else ""}" style="grid-template-columns:repeat({item_cols},minmax(0,1fr))">{its}</div>'
            f'<p class="lead">{lead_cards}</p><div class="mcards2{" cmp" if compact else ""}" style="grid-template-columns:repeat({card_cols},minmax(0,1fr))">{crd}</div>')
    P = new_page(no, seed, title, tier, topic, strand, syll, oc, ptype, f"K1 the letters of the matching cards, read in the item order, spell a word ({n} letters) + K4 each card used once", instr, body,
                 key_text or "; ".join(f"{i+1}) card {lab[right[i]]}" for i in range(n)), f"Word: {word}", note,
                 check=check or f"Read the {n} letters in order. Do they spell a word?", check_boxes=None, mk=("logic",), ps=ps,
                 mech_plain=f"Letters of the matching cards, read in the order of the items, spell a word ({n} letters)")
    solved = [solve_item(items[i], cards) for i in range(n)]
    P.v("V1 independent solver matches every printed item with exactly one printed card, as the key does", solved == list(right), solved)
    P.v("V1b each item has exactly one matching card", all(sum(1 for c in cards if solve_item(items[i], [c]) == 0) == 1 for i in range(n)))
    other = match_other_words(word, list(word) + dec)
    P.v(f"V3 no way of giving every item a different card, and no single changed letter, spells another word ({len(BIG)} words)", not other, other[:3])
    P.v("V3d the code word's letters have exactly ONE arrangement that is a word", anagrams(word) == [word.lower()])
    P.v("V2 the letters of the right cards, in item order, spell the word", "".join(lab[right[i]] for i in range(n)) == word)
    P["cv"] = dict(rate=1.0, single_total=n * (len(cards) - 1), single_detected=n * (len(cards) - 1))
    all_l = sorted(set(lab))
    P["model"] = dict(truth=list(word), domains=[all_l] * n, check=letters_check(), numeric=False, perm=list(range(n)))
    P["card_letters"] = lab
    P["facts"] = ptxt(body)
    return P

# ------------------------------------------------------------------------------------------------ ordering
def order_page(no, seed, title, tier, topic, strand, syll, oc, ptype, instr, rng, cards, order_idx, read_card, note, word=None, check=None, ps=False,
               ncols=3, lead="Write the letters in order.", key_text=None, direction="smallest first", card_text=None, row_mm=None):
    """cards: list of html; order_idx = indices of the cards in the order asked. The card at order_idx[k] carries word[k]. read_card(card_html) -> sortable value."""
    n = len(cards)
    if word is None: word = word_candidates(no, n)[0]
    CLAIMED[no] = word
    lab = [None] * n
    for k, ci in enumerate(order_idx): lab[ci] = word[k]
    shown = list(range(n)); rng.shuffle(shown)
    while shown == list(order_idx): rng.shuffle(shown)
    crd = "".join(f'<div class="ocd"><i class="cl">{lab[j]}</i><div class="oct">{cards[j]}</div></div>' for j in shown)
    body = (f'<div class="ogrid" style="grid-template-columns:repeat({ncols},minmax(0,1fr));{f'grid-auto-rows:{row_mm}mm' if row_mm else ''}">{crd}</div>'
            f'<div class="blk"><p class="lead">{lead}</p><div class="ansgrid2" style="margin-top:2mm">' + "".join('<span class="ab"></span>' for _ in range(n)) + '</div></div>')
    P = new_page(no, seed, title, tier, topic, strand, syll, oc, ptype, f"K1 letters in order spell a word ({n} letters) + K4 each card used once", instr, body,
                 key_text or f"{direction}: " + ", ".join(f"{lab[ci]} = {card_text(ci) if card_text else ptxt(cards[ci])}" for ci in order_idx), f"Word: {word}", note,
                 check=check or f"Read the {n} letters in order. Do they spell a word?", check_boxes=None, mk=("logic",), ps=ps,
                 mech_plain=f"Letters of the cards in the order asked spell a word ({n} letters)")
    vals = [read_card(c) for c in cards]
    got = sorted(range(n), key=lambda j: vals[j])
    P.v("V1 independent solver (every printed card read and sorted) gets the key's order", got == list(order_idx), got)
    P.v("V1b all card values are different", len(set(vals)) == n)
    P.v("V3d the code word's letters have exactly ONE arrangement that is a word", anagrams(word) == [word.lower()])
    bad = sorted(w for w in ("".join(p) for p in itertools.permutations(word)) if w != word and w.lower() in BIG)
    P.v(f"V3 none of the {len(list(itertools.permutations(word))) - 1} wrong orders spells a word", not bad, bad[:3])
    P["cv"] = dict(rate=1.0, single_total=n * n, single_detected=n * n)
    P["model"] = dict(truth=list(word), domains=[sorted(set(word))] * n, check=letters_check(), perm=list(range(n)))
    P["facts"] = ptxt(body)
    return P

# ------------------------------------------------------------------------------------------------ domino loop
def domino_html(code, left, right, start=False):
    tag = '<i class="dstart">START</i>' if start else ""
    return f'<div class="dom"><i class="cl">{code}</i>{tag}<div class="dh"><span class="dt">{left}</span></div><div class="dh r"><span class="dt">{right}</span></div></div>'

def loop_page(no, seed, title, tier, topic, strand, syll, oc, ptype, instr, rng, halves, ev, note, word=None, check=None, ps=False, key_text=None):
    """halves: list of (left_html, right_html) in LOOP ORDER: ev(right of k) == ev(left of k+1), the last right equals the first left. Domino k carries word[k];
    the dominoes are shown in scrambled places; the first (START) domino is marked. The pupil writes the letters in loop order from START."""
    n = len(halves)
    if word is None: word = word_candidates(no, n)[0]
    CLAIMED[no] = word
    pos = list(range(n)); rng.shuffle(pos)
    while pos[0] == 0: rng.shuffle(pos)                       # START domino not first on the page
    doms = [domino_html(word[k], halves[k][0], halves[k][1], start=(k == 0)) for k in range(n)]
    shown = "".join(doms[k] for k in pos)
    body = (f'<div class="doms">{shown}</div><div class="blk"><p class="lead">Write the letters in order, from START.</p><div class="ansgrid2" style="margin-top:2mm">'
            + "".join('<span class="ab"></span>' for _ in range(n)) + '</div></div>')
    P = new_page(no, seed, title, tier, topic, strand, syll, oc, ptype, f"K8 the loop closes (the right half of each domino equals the left half of the next) + K1 letters in order spell a word ({n} letters)", instr, body,
                 key_text or "Loop from START: " + " -> ".join(f"{word[k]} ({ptxt(halves[k][0])} | {ptxt(halves[k][1])})" for k in range(n)), f"Word: {word}", note,
                 check=check or f"Does the loop close, back at START? Read the {n} letters in order: do they spell a word?", check_boxes=None, mk=("loop",), ps=ps,
                 mech_plain=f"Loop: the right half of each domino equals the left half of the next, all the way round to START; the letters in loop order spell a word ({n} letters)")
    L = [ev(h[0]) for h in halves]; R = [ev(h[1]) for h in halves]
    # independent solver: from START follow right value = left value of the next domino
    order = [0]; seen = {0}
    while True:
        nxt = [j for j in range(n) if j not in seen and L[j] == R[order[-1]]]
        if len(nxt) != 1: break
        order.append(nxt[0]); seen.add(nxt[0])
    P.v("V1 independent solver follows the printed halves from START round the loop and visits every domino once", order == list(range(n)) and R[-1] == L[0], order)
    P.v("V1b all left values are different, so every join has exactly one partner", len(set(L)) == n and len(set(R)) == n)
    P.v("V3d the code word's letters have exactly ONE arrangement that is a word", anagrams(word) == [word.lower()])
    bad = sorted(w for w in ("".join([word[0]] + list(p)) for p in itertools.permutations(word[1:])) if w != word and w.lower() in BIG)
    P.v("V3 none of the wrong orders after START spells a word", not bad, bad[:3])
    P["cv"] = dict(rate=1.0, single_total=n * n, single_detected=n * n)
    P["model"] = dict(truth=list(word), domains=[sorted(set(word))] * n, check=letters_check(), perm=list(range(1, n)) if False else list(range(n)))
    P["facts"] = ptxt(body)
    return P

# ------------------------------------------------------------------------------------------------ small helpers
def wrap_words(s): return len(s.split())

def recount(h):
    return len(re.findall(r"<", h))
