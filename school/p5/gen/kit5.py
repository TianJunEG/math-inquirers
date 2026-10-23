"""Primary 5 helpers on top of kit.py: number and fraction formatting, an INDEPENDENT reader/evaluator of printed arithmetic (exact Fractions),
and the five page builders that most pages use (code word, lettered choices, ordering, matching, route).
Everything is pure black and white. Every page module builds a puzzle from a seed, re-solves it with separate code that reads the PRINTED text or drawing,
and hands validate.py a `model` for the independent wrong-answer enumeration."""
import random, itertools, re, html as _html
from fractions import Fraction
from decimal import Decimal, getcontext
from .common import *
from .kit import *

getcontext().prec = 40
NB = " "
STRAND_WN = "Number and Algebra - Whole Numbers"
STRAND_FR = "Number and Algebra - Fractions"
STRAND_DE = "Number and Algebra - Decimals"
STRAND_PC = "Number and Algebra - Percentage"
STRAND_RA = "Number and Algebra - Rate"
STRAND_AR = "Measurement and Geometry - Area and Volume"
STRAND_GE = "Measurement and Geometry - Geometry"

# --------------------------------------------------------------------------- formatting
def num(n):
    """a whole number as printed: a space between groups of three digits from 5 digits up (10 000, 4 305 070)"""
    n = int(n); s = str(abs(n))
    if len(s) >= 5: s = NB.join([s[max(0, i - 3):i] for i in range(len(s), 0, -3)][::-1])
    return ("−" if n < 0 else "") + s

def dec(f, places=None):
    """a Fraction (that is a terminating decimal) as a decimal string"""
    f = Fraction(f); d = Decimal(f.numerator) / Decimal(f.denominator)
    assert Fraction(d) == f, f
    s = format(d.normalize(), "f")
    if "." in s: s = s.rstrip("0").rstrip(".")
    if places is not None:
        s = format(d, f".{places}f")
    ip, _, fp = s.partition(".")
    if len(ip) >= 5: ip = num(int(ip))
    return ip + ("." + fp if fp else "")

def money(f):
    f = Fraction(f)
    return f"${int(f)}" if f.denominator == 1 else "$" + format(Decimal(f.numerator) / Decimal(f.denominator), ".2f")

def FR(n, d):
    return f'<span class="fr"><i>{n}</i><i>{d}</i></span>'

def MX(w, n, d):
    return f'<span class="mx"><b>{w}</b>{FR(n, d)}</span>'

def frac_val(f, mixed=True):
    """html for a Fraction: a whole number, a mixed number or a fraction"""
    f = Fraction(f)
    if f.denominator == 1: return str(f.numerator)
    if mixed and f.numerator > f.denominator:
        w = f.numerator // f.denominator
        return MX(w, f.numerator - w * f.denominator, f.denominator)
    return FR(f.numerator, f.denominator)

def frac_txt(f, mixed=True):
    f = Fraction(f)
    if f.denominator == 1: return str(f.numerator)
    if mixed and f.numerator > f.denominator:
        w = f.numerator // f.denominator
        return f"{w} {f.numerator - w * f.denominator}/{f.denominator}"
    return f"{f.numerator}/{f.denominator}"

def uf(u):
    return {"cm2": "cm<sup>2</sup>", "cm3": "cm<sup>3</sup>", "m2": "m<sup>2</sup>", "m3": "m<sup>3</sup>"}.get(u, u)

# --------------------------------------------------------------------------- the independent reader of printed arithmetic
def to_text(h):
    """printed html -> plain text: stacked fractions become <n|d>, mixed numbers <w n|d>, superscripts ^2 ^3"""
    h = re.sub(r'<span class="mx"><b>(\d+)</b><span class="fr"><i>(\d+)</i><i>(\d+)</i></span></span>', r"⟨\1 \2|\3⟩", h)
    h = re.sub(r'<span class="fr"><i>(\d+)</i><i>(\d+)</i></span>', r"⟨\1|\2⟩", h)
    h = re.sub(r"<sup>(\d)</sup>", r"^\1", h)
    h = re.sub(r"<[^>]+>", " ", h)
    return re.sub(r"[ \t\r\n]+", " ", _html.unescape(h)).strip(" \t\r\n")

_TOK = re.compile(r"\s*(⟨[^⟩]*⟩|\d+(?:\.\d+)?|[()+−\-×*÷/%]|of\b)")

def _tokens(s):
    s = s.replace(NB, "").replace(" ", "").replace("$", "")
    pos, out = 0, []
    while pos < len(s):
        m = _TOK.match(s, pos)
        if not m:
            if s[pos].isspace(): pos += 1; continue
            raise ValueError(f"cannot read {s[pos:pos+12]!r} in {s!r}")
        out.append(m.group(1)); pos = m.end()
    return out

def evaluate(text):
    """exact value (Fraction) of a printed arithmetic expression: numbers, decimals, <n|d>, <w n|d>, + - x / brackets, 'p% of x'"""
    toks = _tokens(text); i = [0]
    def peek(): return toks[i[0]] if i[0] < len(toks) else None
    def take(): t = toks[i[0]]; i[0] += 1; return t
    def atom():
        t = take()
        if t == "(":
            v = expr(); assert take() == ")"; return pct(v)
        if t.startswith("⟨"):
            body = t[1:-1]; a, b = body.split("|"); parts = a.split()
            v = Fraction(int(parts[-1]), int(b)) + (int(parts[0]) if len(parts) == 2 else 0)
            return pct(v)
        if t in ("−", "-"): return -atom()
        return pct(Fraction(Decimal(t)))
    def pct(v):
        if peek() == "%": take(); return v / 100
        return v
    def term():
        v = atom()
        while peek() in ("×", "*", "÷", "/", "of"):
            o = take(); w = atom()
            v = v * w if o in ("×", "*", "of") else v / w
        return v
    def expr():
        v = term()
        while peek() in ("+", "−", "-"):
            o = take(); w = term(); v = v + w if o == "+" else v - w
        return v
    v = expr(); assert i[0] == len(toks), ("trailing", text, toks[i[0]:]); return v

def only_int(v):
    v = Fraction(v); return v.numerator if v.denominator == 1 else None

# --------------------------------------------------------------------------- answer boxes
def abx(cls="w4"): return f'<span class="ab {cls}"></span>'
def ab_frac(): return '<span class="fans"><span class="ab w2"></span><span class="fline"></span><span class="ab w2"></span></span>'
def ab_mixed(): return '<span class="ab w2"></span>' + ab_frac()
def qc(i, content, ans="", cls=""):
    return qcard(i, content, ans, cls)

def distinct(xs): return len(set(xs)) == len(xs)

# --------------------------------------------------------------------------- code-word page (K1)
def code_table_for(no, answers, rng, pool, n_decoy=3, tries=80, word_n=6, avoid=()):
    """(word, table) with every single slip in `pool` rejected, or None"""
    dom = sorted(set(pool) | set(answers))
    return code_table_any(no, word_n, answers, rng, 0, 0, avoid=avoid, n_decoy=n_decoy, tries=tries, pool=[p for p in pool if p not in answers], domain=dom), dom

def code_page(no, seed, title, tier, topic, strand, syll, oc, ptype, instr, cards_html, answers, word, table, dom, fmt, key_lines, note,
              solved, layout="c2", cols=None, ps=False, pre="", post="", checks=(), plain=None, cls=""):
    """standard code-word page: the cards, the code table, the six boxes in the check strip; V1 solved == answers; the finish_code record"""
    body = pre + qgrid(cards_html, int(layout[1:]), cls) + post + table_block(table, fmt, cols)
    P = new_page(no, seed, title, tier, topic, strand, syll, oc, ptype, f"K1 code word ({len(word)} letters)", instr, body, key_lines, f"Code word: {word}", note,
                 check_boxes=len(word), ps=ps)
    finish_code(P, answers, table, word, 0, 0, dom, plain)
    P["facts"] = " ".join(str(k) for k in table)
    P.v("V1 independent solver (reads the printed items, evaluates exactly) equals the key", list(solved) == list(answers), [str(s) for s in solved][:8])
    for n_, ok_, d_ in checks: P.v(n_, ok_, d_)
    return P

# --------------------------------------------------------------------------- lettered choices (K1): the letter of the right choice in each row
def mc_rows(rng, word, n_opts, rows, tries=400):
    """rows: list of dict(q=html, opts=[html...], right=index of the right option (default 0), fixed=True keeps the printed order, fig='', wide, col).
    Letters are given by role (the right choice carries the word's letter, every wrong choice a decoy letter). Returns (html rows, letters per row [right, wrong...], info)"""
    lets = choice_letters(rng, word, n_opts, tries=tries)
    out, spec = [], []
    for i, r in enumerate(rows):
        right = r.get("right", 0)
        roles = {}; w = 1
        for j in range(n_opts):
            if j == right: roles[j] = lets[i][0]
            else: roles[j] = lets[i][w]; w += 1
        order = list(range(n_opts))
        if not r.get("fixed"): rng.shuffle(order)
        opts = ""
        for pos in order:
            opts += f'<span class="mo"><i class="cl">{roles[pos]}</i><span class="ot">{r["opts"][pos]}</span></span>'
        out.append(f'<div class="qrow mcrow{" wide" if r.get("wide") else ""}"><span class="no">{i+1}</span><div class="mq{" big" if r.get("big") else ""}">{r["q"]}{r.get("fig","")}</div><div class="mopts{" col" if r.get("col") else ""}">{opts}</div></div>')
        spec.append(roles)
    return out, lets, spec

def read_mc(body):
    """independent reader of the lettered-choice rows: [(question text, [(letter, option text)...]), ...]"""
    rows = []
    for m in re.finditer(r'<div class="qrow mcrow[^"]*"><span class="no">\d+</span><div class="mq[^"]*">(.*?)</div><div class="mopts[^"]*">(.*?)</div></div>(?=<div class="qrow|</div>|$)', body, re.S):
        q = to_text(m.group(1))
        opts = re.findall(r'<i class="cl">(\w)</i><span class="ot">(.*?)</span></span>(?=<span class="mo">|$)', m.group(2), re.S)
        rows.append((q, [(L, to_text(t)) for L, t in opts], m.group(1)))
    return rows

def mc_page(no, seed, title, tier, topic, strand, syll, oc, ptype, instr, rng, rows, n_opts, word, key_lines, note, solve_row, ps=False, checks=(), plain=None, check=None, rows_cls="tfrows"):
    """lettered-choice page. solve_row(question text, [option texts], question html) -> index of the right option, computed from the PRINTED text"""
    html_rows, lets, spec = mc_rows(rng, word, n_opts, rows)
    body = f'<div class="{rows_cls}">' + "".join(html_rows) + "</div>"
    P = new_page(no, seed, title, tier, topic, strand, syll, oc, ptype, f"K1 the letter of the right choice in each row spells a word ({len(word)} letters, one wrong letter per other choice)", instr, body, key_lines,
                 f"Word: {word}", note, check_boxes=len(word), ps=ps, mech_plain=plain or f"Word from the letters of the right choices ({len(word)} letters)")
    got = []
    for q, opts, qh in read_mc(body):
        got.append(opts[solve_row(q, [t for _, t in opts], qh)][0])
    P.v("V1 independent solver reads each printed row and picks the right choice: the letters equal the key word", "".join(got) == word, "".join(got))
    P.v("V2 right choices read down the rows spell the word", "".join(l[0] for l in lets) == word)
    other = [w for w in ("".join(lets[i][c] for i, c in enumerate(combo)) for combo in itertools.product(range(n_opts), repeat=len(word)) if any(combo)) if w.lower() in BIG]
    P.v(f"V3 none of the other {n_opts ** len(word) - 1} ways to choose spells a word (large word list)", not other, other[:3])
    P.v("V3d the word's letters have exactly ONE arrangement that is a word", anagrams(word) == [word.lower()])
    domains = [list(lets[i]) for i in range(len(word))]
    P["model"] = dict(truth=list(word), domains=domains, check=letters_check(), numeric=False)
    P["cv"] = dict(rate=1.0, single_total=len(word) * (n_opts - 1), single_detected=len(word) * (n_opts - 1))
    P["facts"] = ""
    if check: P["check"] = check
    for n_, ok_, d_ in checks: P.v(n_, ok_, d_)
    return P

# --------------------------------------------------------------------------- ordering (K1 + K4): the letters of the cards in the order asked spell a word
def order_page(no, seed, title, tier, topic, strand, syll, oc, ptype, instr, rng, cards, word, ascending, key_lines, note, solve_card, ps=False, checks=(), plain=None, cols=3, work=False):
    """cards: list of html contents. Card with the k-th smallest (greatest, if not ascending) value carries letter word[k].
    values are computed by the caller's `values` list kept in cards as (html, value). solve_card(html text)->value is the independent reader."""
    n = len(cards); assert n == len(word)
    order = sorted(range(n), key=lambda k: cards[k][1], reverse=not ascending)
    assert len({cards[k][1] for k in range(n)}) == n, "cards must have different values"
    letter = {}
    for rank, k in enumerate(order): letter[k] = word[rank]
    disp = list(range(n)); rng.shuffle(disp)
    items = "".join(f'<div class="ocard"><i class="cl">{letter[k]}</i><div class="oc">{cards[k][0]}</div>{'<div class="wk">= <span class="ab w5"></span></div>' if work else ''}</div>' for k in disp)
    body = f'<div class="ocards c{cols}">{items}</div>'
    P = new_page(no, seed, title, tier, topic, strand, syll, oc, ptype, f"K1 letters in order spell a word ({n} letters) + K4 each card used once", instr, body, key_lines, f"Word: {word}", note,
                 check_boxes=n, mk=("logic",), ps=ps, mech_plain=plain or f"Letters of the cards in the order asked spell a word ({n} letters)")
    read = re.findall(r'<div class="ocard"><i class="cl">(\w)</i><div class="oc">(.*?)</div>', body, re.S)
    vals = [(solve_card(to_text(h)), L) for L, h in read]
    P.v("V1 independent solver (reads each card, evaluates exactly, sorts) gets the word", "".join(L for _, L in sorted(vals, reverse=not ascending)) == word, "".join(L for _, L in sorted(vals, reverse=not ascending)))
    P.v("V1b all card values are different", len({v for v, _ in vals}) == n)
    P.v("V3d the word's letters have exactly ONE arrangement that is a word", anagrams(word) == [word.lower()], anagrams(word))
    bad = sorted(w for w in ("".join(p) for p in itertools.permutations(word)) if w != word and w.lower() in BIG)
    P.v(f"V3 none of the {len(list(itertools.permutations(range(n)))) - 1} wrong orders of the letters spells a word", not bad, bad[:3])
    P["cv"] = dict(rate=1.0, single_total=1, single_detected=1)
    P["model"] = dict(truth=list(word), domains=[sorted(set(word))] * n, check=letters_check(), perm=list(range(n)))
    P["facts"] = ""
    for n_, ok_, d_ in checks: P.v(n_, ok_, d_)
    return P

# --------------------------------------------------------------------------- matching (K1 + K4): write the letter of the matching card under each tile
def match_page(no, seed, title, tier, topic, strand, syll, oc, ptype, instr, rng, pairs, word, key_lines, note, solve_left, solve_right, ps=False, checks=(), plain=None, left_title="Cards", right_title="Tiles"):
    """pairs: list of (left_html, right_html) in the ORDER OF THE TILES; the left card of tile i carries word[i].
    solve_left(text)->value and solve_right(text)->value are the independent readers; a card matches the tile with the same value."""
    n = len(pairs); assert n == len(word)
    disp = list(range(n)); rng.shuffle(disp)
    left = "".join(f'<div class="mcard2"><i class="cl">{word[k]}</i><div class="mc2">{pairs[k][0]}</div></div>' for k in disp)
    right = "".join(f'<div class="tile"><div class="tn"><span class="no">{i+1}</span></div><div class="tv">{pairs[i][1]}</div><span class="ab letter"></span></div>' for i in range(n))
    body = (f'<div class="blk"><p class="lead">{left_title}</p><div class="mcards2">{left}</div></div>'
            f'<div class="blk"><p class="lead">{right_title}: write the matching letter in each box.</p><div class="tiles">{right}</div></div>')
    P = new_page(no, seed, title, tier, topic, strand, syll, oc, ptype, f"K1 letters of the matching cards spell a word ({n} letters) + K4 each card used once", instr, body, key_lines, f"Word: {word}", note,
                 check="Read the boxes from tile 1 to tile %d. Do the letters spell a word?" % n, check_boxes=None, mk=("logic",), ps=ps,
                 mech_plain=plain or f"Letters of the matching cards, tile 1 to {n}, spell a word")
    lcards = re.findall(r'<div class="mcard2"><i class="cl">(\w)</i><div class="mc2">(.*?)</div></div>', body, re.S)
    tiles = re.findall(r'<div class="tv">(.*?)</div><span class="ab letter">', body, re.S)
    lv = [(solve_left(to_text(h)), L) for L, h in lcards]
    got = ""
    for t in tiles:
        v = solve_right(to_text(t)); m = [L for x, L in lv if x == v]
        got += m[0] if len(m) == 1 else "?"
    P.v("V1 independent solver (evaluates every card and every tile, matches equal values) gets the word", got == word, got)
    P.v("V1b every card matches exactly one tile and every tile exactly one card", len({v for v, _ in lv}) == n and sorted(solve_right(to_text(t)) for t in tiles) == sorted(v for v, _ in lv))
    P.v("V3d the word's letters have exactly ONE arrangement that is a word", anagrams(word) == [word.lower()], anagrams(word))
    bad = sorted(w for w in ("".join(p) for p in itertools.permutations(word)) if w != word and w.lower() in BIG)
    P.v(f"V3 none of the wrong matchings (every other arrangement of the letters) spells a word", not bad, bad[:3])
    P["cv"] = dict(rate=1.0, single_total=1, single_detected=1)
    P["model"] = dict(truth=list(word), domains=[sorted(set(word))] * n, check=letters_check(), perm=list(range(n)))
    P["facts"] = ""
    for n_, ok_, d_ in checks: P.v(n_, ok_, d_)
    return P

# --------------------------------------------------------------------------- routes (K6)
def cell_html(c):
    return f'<span class="rc">{c}</span>'

def route_grid(n, texts, start, finish, cls="maze"):
    cells = ""
    for r in range(n):
        for c in range(n):
            tag = '<i class="flag">START</i>' if (r, c) == start else '<i class="flag">FINISH</i>' if (r, c) == finish else ""
            cells += f'<div class="mcell">{tag}<span class="rc">{texts[r][c]}</span></div>'
    return f'<div class="{cls}" style="grid-template-columns:repeat({n},1fr)">{cells}</div>'

def read_route(body):
    """independent reader of a route grid: n and the html of every cell"""
    cells = re.findall(r'<div class="mcell">(?:<i class="flag">\w+</i>)?<span class="rc">(.*?)</span></div>(?=<div class="mcell"|</div>)', body, re.S)
    n = int(round(len(cells) ** 0.5)); assert n * n == len(cells)
    return n, cells

def build_route(rng, n, length, make_on, make_off, n_dead, tries=8000, min_dist=4, ok_text=None, dup=True):
    """make_on(i) -> text of an on-target cell; make_off() -> text of an off-target cell. Returns (path, grid texts, dead count) with exactly one route"""
    for _ in range(tries):
        path = random_walk(rng, n, length, min_dist)
        grid = [[None] * n for _ in range(n)]
        for i, p in enumerate(path): grid[p[0]][p[1]] = make_on(i)
        dead = 0
        for p in path[:-1]:
            if dead >= n_dead: break
            opts = [q for q in neighbours(*p, n) if grid[q[0]][q[1]] is None]
            if opts and rng.random() < .5:
                q = rng.choice(opts); grid[q[0]][q[1]] = make_on(rng.randrange(length)); dead += 1
        for r in range(n):
            for c in range(n):
                if grid[r][c] is None: grid[r][c] = make_off()
        texts = [x for row in grid for x in row]
        if dup and len(set(texts)) != len(texts): continue
        if ok_text is None: return path, grid, dead
        okc = lambda cell: ok_text(grid[cell[0]][cell[1]])
        if count_routes(okc, n, path[0], path[-1]) == 1 and dead >= min(n_dead, 2): return path, grid, dead
    raise RuntimeError("route")

def route_page(no, seed, title, tier, topic, strand, syll, oc, ptype, instr, grid, path, dead, rule_text, cell_ok, note, key_cells, check, ps=False, checks=(), extra_facts=""):
    """cell_ok(cell html) -> bool is the independent reader of the PRINTED cell: does it follow the rule?"""
    n = len(grid); start, finish = path[0], path[-1]
    body = route_grid(n, [[grid[r][c] for c in range(n)] for r in range(n)], start, finish)
    P = new_page(no, seed, title, tier, topic, strand, syll, oc, ptype, "K6 route closes at FINISH through the stated number of boxes", instr, body,
                 "Route (row, column from top-left): " + " -> ".join(f"({r+1},{c+1}) {key_cells(grid[r][c])}" for r, c in path),
                 f"Route reaches FINISH through {len(path)} boxes; every box on it follows the rule.", note, check=check, mk=("route",), ps=ps,
                 mech_plain="Route: the line must reach FINISH through the right number of boxes, every box following the rule")
    nn, cells = read_route(body)
    okc = lambda cell: cell_ok(cells[cell[0] * nn + cell[1]])
    cnt = count_routes(okc, nn, start, finish)
    P.v("V1 exactly one route start->finish (exhaustive search; every cell is read from the printed page)", cnt == 1, cnt)
    P.v("V3 dead-end boxes that also follow the rule exist", dead >= 2, dead)
    P.v("V3b a shortcut ignoring the rule is shorter than the route, so the box count rejects it", abs(start[0] - finish[0]) + abs(start[1] - finish[1]) + 1 < len(path))
    P.v("V7b all boxes are different", len(set(cells)) == len(cells))
    P["cv"] = dict(rate=1.0, single_total=max(dead, 1), single_detected=max(dead, 1))
    P["facts"] = extra_facts
    allc = [(r, c) for r in range(nn) for c in range(nn)]
    def legal(rt):
        if len(rt) != len(path) or len(set(rt)) != len(rt) or rt[0] != start or rt[-1] != finish: return False
        return all(okc(c) for c in rt) and all(abs(a[0] - b[0]) + abs(a[1] - b[1]) == 1 for a, b in zip(rt, rt[1:]))
    P["model"] = dict(truth=list(path), domains=[allc] * len(path), check=legal, numeric=False)
    P["mini"] = mini_route(nn, path)
    for n_, ok_, d_ in checks: P.v(n_, ok_, d_)
    return P

# --------------------------------------------------------------------------- numbers: plausible wrong answers
def wrong_pool(vals, extra=()):
    """a pool of plausible wrong values: the given extras (the typical slips), kept apart from the answers"""
    return [v for v in dict.fromkeys(extra) if v not in vals]
