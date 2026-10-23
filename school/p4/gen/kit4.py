"""Shared builders of the Primary 4 pages: number formatting, code-word pages, lettered-choice pages, card pages (matching and ordering),
fractions and mixed numbers, and the small readers the independent solvers use. Everything is pure black and white."""
import random, itertools, re, math
from fractions import Fraction
from .common import *
from .kit import *

STRAND_NU = "Number and Algebra - Whole Numbers"
STRAND_FR = "Number and Algebra - Fractions"
STRAND_DE = "Number and Algebra - Decimals"
STRAND_AP = "Measurement and Geometry - Area and Volume"
STRAND_GE = "Measurement and Geometry - Geometry"
STRAND_ST = "Statistics - Data Representation and Interpretation"
INSTR_CODE = "Use the code table."
PEOPLE = ["Ali", "Mei", "Siti", "Ben", "Kumar", "Aisha", "Wei", "Ravi", "Jenny", "Lily", "Hana", "Tom", "Farah", "Daniel", "Priya", "Jun", "Zara", "Omar"]

# --------------------------------------------------------------------------- numbers
GAP = '<span class="g"></span>'            # the small gap of a 5-digit number (10 000 and over); 4-digit numbers have no gap

def N(n):
    """a whole number as printed in the booklet: 5-digit numbers have a gap (45 280), 4-digit numbers do not (4280)"""
    s = str(n)
    if len(s) >= 5: return s[:-3] + GAP + s[-3:]
    return s

def Nt(n):
    """the same number for plain text that is printed (instructions, check strips): the gap is a thin space"""
    s = str(n)
    return s[:-3] + "\u2009" + s[-3:] if len(s) >= 5 else s

def Ntxt(n):
    """the same number for plain text such as a teacher key: 45 280"""
    s = str(n)
    return s[:-3] + " " + s[-3:] if len(s) >= 5 else s

def strip_gap(h): return h.replace(GAP, "")

def num_of(h):
    """independent reader: the whole number printed in a piece of html (gap and tags removed)"""
    return int(re.sub(r"\D", "", re.sub(r"<[^>]+>", "", strip_gap(h))))

def nums_in(h):
    """all whole numbers printed in a piece of html, in order (gaps joined; decimals are not meant for this)"""
    t = re.sub(r"<[^>]+>", " ", strip_gap(h))
    return [int(x) for x in re.findall(r"\d+", t)]

def dec_str(v, places=None):
    """a decimal as a canonical string, for example dec_str(Fraction(5, 4)) = '1.25' (no trailing zero unless places is given)"""
    v = Fraction(v)
    if places is None:
        for p in range(0, 5):
            if (v * 10 ** p).denominator == 1: places = p; break
        else: raise ValueError(v)
    q = v * 10 ** places
    assert q.denominator == 1, (v, places)
    s = str(abs(int(q))).rjust(places + 1, "0")
    out = s[:-places] + "." + s[-places:] if places else s
    return ("-" if v < 0 else "") + out

def dec_val(s): return Fraction(s)

# --------------------------------------------------------------------------- fractions and mixed numbers
def mixed_html(w, n, d):
    return f'<span class="mx"><b>{w}</b>' + frac_html((n, d)) + '</span>'

def blank_frac(d=None, w=False):
    """an empty fraction: two answer boxes, one over the other (the bottom number can be given)"""
    bot = f"<i>{d}</i>" if d else '<i><span class="ab w2 fb"></span></i>'
    return f'<span class="fr"><i><span class="ab w2 fb"></span></i>{bot}</span>'

def read_frac(h):
    """independent reader: every fraction <span class="fr"><i>a</i><i>b</i></span> printed in a piece of html, as (a, b) with None for an empty box"""
    out = []
    for m in re.finditer(r'<span class="fr"><i>(.*?)</i><i>(.*?)</i></span>', h):
        a = re.sub(r"<[^>]+>", "", m.group(1)); b = re.sub(r"<[^>]+>", "", m.group(2))
        out.append((int(a) if a.strip() else None, int(b) if b.strip() else None))
    return out

def simplest(n, d):
    g = math.gcd(n, d); return n // g, d // g

# the symbols that the two fonts do not have are drawn
SYM_ANGLE = ('<svg class="sym" xmlns="http://www.w3.org/2000/svg" width="3.6mm" height="3.6mm" viewBox="0 0 10 10"><path d="M9.5,9 L0.8,9 L8,1.6" fill="none" stroke="#000" stroke-width="1.15" stroke-linejoin="round" stroke-linecap="round"/></svg>')
SYM_APPROX = ('<svg class="sym" xmlns="http://www.w3.org/2000/svg" width="4.4mm" height="3.6mm" viewBox="0 0 12 10"><path d="M1,3.6 Q3.5,0.6 6,3.6 T11,3.6 M1,7.6 Q3.5,4.6 6,7.6 T11,7.6" fill="none" stroke="#000" stroke-width="1.15" stroke-linecap="round"/></svg>')

def angle_name(a, b, c):
    """the angle sign and three letters: the drawn symbol, then ABC"""
    return f'{SYM_ANGLE}<span class="an">{a}{b}{c}</span>'

# --------------------------------------------------------------------------- code table block (sorted sensibly, 5-digit gaps)
def table_block4(table, fmt=None, cols=None, key=None, lead="Code table"):
    items = sorted(table.items(), key=(lambda kv: key(kv[0])) if key else (lambda kv: kv[0]))
    fmt = fmt or (lambda k: N(k) if isinstance(k, int) else str(k))
    n = len(items); cols = cols or (n if n <= 5 else (n + 1) // 2)
    cells = "".join(f'<div class="ct"><span class="n">{fmt(k)}</span><span class="eq">=</span><b>{v}</b></div>' for k, v in items)
    return f'<div class="blk ctc"><p class="lead">{lead}</p><div class="codetable" style="grid-template-columns:repeat({cols},1fr)">{cells}</div></div>'

# --------------------------------------------------------------------------- the standard code-word page
def code_page(no, seed, title, tier, topic, strand, syll, oc, ptype, instr, body, answers, table, word, lo, hi, key_answers, note,
              domain=None, fmt=None, ps=False, plain=None, cols=None, tkey=None, mech=None, check=None, mk=("code",), extra_check=None):
    body = body + table_block4(table, fmt, cols, tkey)
    P = new_page(no, seed, title, tier, topic, strand, syll, oc, ptype, mech or f"K1 code word ({len(word)} letters)", instr, body, key_answers,
                 f"Code word: {word}", note, check_boxes=len(word), ps=ps, mk=mk, **({"check": check} if check else {}))
    finish_code(P, answers, table, word, lo, hi, domain, plain)
    P["facts"] = " ".join(str(v) for v in table)
    return P

def distinct(xs): return len(set(xs)) == len(xs)

def plausible_domain(answers, extra=(), spread=(1, 2, 3, 4, 5, 10, 100, 1000), cap=None, rng=None, sample=250, lo=0, hi=99999):
    """the values a pupil could write: the answers, a few slips on each (+-1 ... +-1000), the extra values, and a sample of other numbers"""
    d = set(answers) | set(extra)
    for a in answers:
        for s in spread:
            for v in (a - s, a + s):
                if lo <= v <= hi: d.add(v)
    if rng:
        for _ in range(sample): d.add(rng.randint(lo, hi))
    return sorted(d)

# --------------------------------------------------------------------------- lettered choices
def choice_row(i, content_html, opts, letters, extra_cls=""):
    """one row: number, the question (picture or text), and the options each with its letter in a circle. opts = list of html labels; letters = list of letters"""
    o = "".join(f'<span class="tfo"><b>{h}</b><i class="cl">{l}</i></span>' for h, l in zip(opts, letters))
    return f'<div class="srow3 {extra_cls}"><span class="no">{i}</span><div class="sq3">{content_html}</div><div class="sopts">{o}</div></div>'

def make_choice_letters(rng, word, n_opts):
    """letters[i] = [letter of option 0, 1 ...] with the right letter word[i] placed at random; returns (rows, pos) where pos[i] is the right option's index"""
    rows = choice_letters(rng, word, n_opts)
    pos = []; out = []
    for i, r in enumerate(rows):
        k = rng.randrange(n_opts); rest = r[1:]
        lay = rest[:k] + [r[0]] + rest[k:]
        out.append(lay); pos.append(k)
    return out, pos

def choice_page(no, seed, title, tier, topic, strand, syll, oc, ptype, instr, rows_html, word, letters, truth_letters, key_answers, note,
                mech=None, plain=None, ps=False, check="Write the letters in order. Do they spell a word?", body_pre="", mk=("code",)):
    body = body_pre + '<div class="srows3 tallrows">' + "".join(rows_html) + '</div>'
    P = new_page(no, seed, title, tier, topic, strand, syll, oc, ptype, mech or f"K1 the letter of the right choice in each row spells a word ({len(word)} letters)", instr,
                 body, key_answers, f"Word: {word}", note, check=check, check_boxes=len(word), ps=ps, mk=mk,
                 mech_plain=plain or f"Word from the letters of the right choices ({len(word)} letters)")
    other = choice_other_words(word, letters)
    P.v("V2 the letters of the right choices read down the rows spell the word", "".join(truth_letters) == word)
    P.v("V3 no other way of choosing one option in every row spells a word (large word list)", not other, other[:3])
    P.v("V3d the code word's letters have exactly ONE arrangement that is a word", anagrams(word) == [word.lower()], anagrams(word))
    P["cv"] = dict(rate=1.0, single_total=sum(len(l) - 1 for l in letters), single_detected=sum(len(l) - 1 for l in letters))
    P["model"] = dict(truth=list(truth_letters), domains=[list(l) for l in letters], check=letters_check(), numeric=False)
    return P

# --------------------------------------------------------------------------- cards (matching and ordering)
def letters_for_cards(rng, word, n_decoy, tries=3000):
    """letters for len(word) right cards (the letters of the word, in order) and n_decoy decoy cards: no single wrong card and no swap of two rows
    spells a word of the large list. Returns the decoy letters."""
    avail = [c for c in ALPHA if c not in word]
    allv = list(word)
    for _ in range(tries):
        dec = rng.sample(avail, n_decoy)
        pool = list(word) + dec
        ok = True
        for i in range(len(word)):
            for c in pool:
                if c == word[i]: continue
                w2 = word[:i] + c + word[i + 1:]
                if w2.lower() in BIG: ok = False; break
            if not ok: break
        if ok: return dec
    raise RuntimeError("cards letters")

def write_boxes(n, cls="ab"):
    return '<div class="ansgrid2" style="margin-top:2mm">' + "".join(f'<span class="{cls}"></span>' for _ in range(n)) + "</div>"

def no_wrong_order(word):
    return sorted(w for w in ("".join(p) for p in itertools.permutations(word)) if w != word and w.lower() in BIG)

# --------------------------------------------------------------------------- routes
def route_grid_ok(rng, n, length, min_dist):
    return random_walk(rng, n, length, min_dist)

def route_page(no, seed, title, tier, topic, strand, syll, oc, ptype, instr, n, texts, start, finish, path, ok_cell, key_answers, check, note, dead, facts="", ps=False, extra_checks=(), cls="maze tall"):
    body = maze_html(n, texts, start, finish, cls=cls)
    P = new_page(no, seed, title, tier, topic, strand, syll, oc, ptype, "K6 route closes at FINISH", instr, body, key_answers,
                 f"Route reaches FINISH through {len(path)} boxes.", note, check=check, mk=("route",), ps=ps,
                 mech_plain="Route: the line must reach FINISH through the right number of boxes, every box following the rule")
    P.v("V1 exactly one route start->finish (exhaustive search, every box evaluated from its printed text)", count_routes(ok_cell, n, start, finish) == 1)
    P.v("V3 dead-end boxes that also follow the rule exist", dead >= 2, dead)
    P.v("V3b a shortcut that ignores the rule is shorter than the route, so the box count rejects it", abs(start[0] - finish[0]) + abs(start[1] - finish[1]) + 1 < len(path))
    P["cv"] = dict(rate=1.0, single_total=dead, single_detected=dead)
    P["facts"] = facts
    cells = [(r, c) for r in range(n) for c in range(n)]
    def legal(rt):
        if len(rt) != len(path) or len(set(rt)) != len(rt) or rt[0] != start or rt[-1] != finish: return False
        return all(ok_cell(c) for c in rt) and all(abs(a[0] - b[0]) + abs(a[1] - b[1]) == 1 for a, b in zip(rt, rt[1:]))
    P["model"] = dict(truth=list(path), domains=[cells] * len(path), check=legal, numeric=False)
    P["mini"] = mini_route(n, path)
    return P


def rows_of(body):
    """independent reader of lettered-choice rows: [(content html, [(option html, letter)])]"""
    out = []
    for m in re.finditer(r'<div class="srow3[^"]*"><span class="no">\d+</span><div class="sq3">(.*?)</div><div class="sopts">(.*?)</div></div>(?=<div class="srow3|</div>\s*$|</div><|$)', body, re.S):
        opts = [(a, b) for a, b in re.findall(r'<span class="tfo"><b>(.*?)</b><i class="cl">(\w)</i></span>', m[2], re.S)]
        out.append((m[1], opts))
    return out

def induced_path(rng, n, length, min_dist, tries=3000):
    """a self-avoiding route of `length` cells in an n x n grid in which no two cells that are not neighbours on the route touch (so a valid
    cell next to the route can only be a dead end, never a shortcut)"""
    for _ in range(tries):
        path = [(rng.randrange(n), rng.randrange(n))]
        def dfs():
            if len(path) == length: return True
            opts = [q for q in neighbours(*path[-1], n) if q not in path and all(nb == path[-1] or nb not in path for nb in neighbours(*q, n))]
            rng.shuffle(opts)
            for q in opts:
                path.append(q)
                if dfs(): return True
                path.pop()
            return False
        if dfs() and abs(path[0][0] - path[-1][0]) + abs(path[0][1] - path[-1][1]) >= min_dist: return path
    raise RuntimeError("induced path")

def dead_ends(rng, n, path, k):
    """k extra cells that follow the rule but are leaves: each touches exactly one valid cell, which is on the route (not its last cell)"""
    chosen = []
    for _ in range(50):
        valid = set(path) | set(chosen)
        cand = [q for q in [(r, c) for r in range(n) for c in range(n)] if q not in valid and sum(1 for nb in neighbours(*q, n) if nb in valid) == 1
                and next(nb for nb in neighbours(*q, n) if nb in valid) in path[:-1]]
        if not cand or len(chosen) == k: break
        chosen.append(rng.choice(cand))
    return chosen
