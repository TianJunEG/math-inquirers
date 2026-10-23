"""Shared kit of the Primary 3 pages: safe code words, the standard code-word record, small HTML builders, route helpers.
Everything is pure black and white. Each page module builds a puzzle from a seed, re-solves it with separate solver code that reads
the PRINTED text or drawing, and hands validate.py a `model` for the independent wrong-answer enumeration."""
import random, itertools, re, html as _html
from .common import *

BIG.update({"siring", "jailor"})      # words found by the P1 and P3 audits that the 129 000-word list lacked

# --------------------------------------------------------------------------- code words
# child-friendly words with distinct letters, exactly ONE arrangement that is a word, and no single letter of the word put in another slot
# making another word (tested against the 129 000-word list). The word of page `no` is the (no mod pool size)-th of its length.
SAFE5 = "birch biome saucy vault topaz motif wharf audio blank blimp blown blunt bound chimp climb cloth clown count cramp crazy crumb curve decoy depth doubt drank drift drown dwarf enjoy fable fault flank flask flora flown fluid force forum frank fruit gleam glory graph gravy grind growl grunt guild hound humid image ivory jumpy juice juicy knife logic maize mixed moved noisy omega opera piano picky pivot plank pound print prize quick round scowl shaft shove skimp sling smack snuck spicy squid stamp swamp swift swung thief think thumb trunk tulip uncle valet video vital voice wafer waltz width woman works wound woven yield young".split()
SAFE6 = "gopher junior knight meadow melody public quiver scribe spruce swivel thrive tricky tuxedo update volume voyage wisdom answer backup bounce bright buckle budgie campus canopy clouds cousin crafty creamy donkey dainty family figure flight fridge frozen fruity guitar hungry length magnet mighty monkey number peanut police safety sailor shadow shrimp sponge square string strong studio subway sunday teacup tongue turkey walnut walrus wizard wombat bandit behind botany bowman cherub cobalt cougar curfew devour fabric fathom".split()
_SAFE = {}

def inner_ok(w):
    """no letter of the word, written in another slot, makes another word"""
    w = w.lower()
    for i in range(len(w)):
        for c in set(w):
            if c != w[i] and (w[:i] + c + w[i + 1:]) in BIG: return False
    return True

def swap_ok(w):
    """no two letters of the word swapped make another word"""
    w = w.lower()
    for i in range(len(w)):
        for j in range(i + 1, len(w)):
            l = list(w); l[i], l[j] = l[j], l[i]
            if "".join(l) in BIG: return False
    return True

def word_ok(w):
    return len(set(w)) == len(w) and anagrams(w) == [w.lower()] and w.lower() in COMMON and inner_ok(w) and swap_ok(w)

def safe_pool(n):
    if n not in _SAFE: _SAFE[n] = [w for w in {5: SAFE5, 6: SAFE6}[n] if word_ok(w)]
    return _SAFE[n]

CLAIMED = {}      # page number -> code word, so that no two pages of one build share a word

def word_candidates(no, n, avoid=()):
    pool = safe_pool(n); k = (no * 5) % len(pool)
    taken = {w for p, w in CLAIMED.items() if p != no}
    return [pool[(k + o) % len(pool)].upper() for o in range(len(pool)) if pool[(k + o) % len(pool)].upper() not in avoid and pool[(k + o) % len(pool)].upper() not in taken]

def code_table_any(no, n, answers, rng, lo, hi, avoid=(), max_words=6, **kw):
    """(word, table): the first word of this page's sequence for which a code table with no undetected slip exists"""
    for w in word_candidates(no, n, avoid)[:max_words]:
        t = make_code_table(answers, w, rng, lo, hi, **kw)
        if t: CLAIMED[no] = w; return w, t
    return None

def finish_code(P, answers, table, word, lo, hi, domain=None, plain=None):
    """the standard record every code-word page keeps: V2/V3/V3c/V3d/V4 and the model for validate.py's enumeration"""
    cv = code_verify(answers, table, word, lo, hi, domain)
    code_checks(P, cv, word)
    P["cv"] = cv
    P["model"] = code_model(answers, table, lo, hi, domain)
    P["mech_plain"] = plain or f"Code word ({len(word)} letters)"
    return cv

def plain_text(h):
    return re.sub(r"\s+", " ", _html.unescape(re.sub(r"<[^>]+>", " ", h))).strip()

def esc(s): return s.replace("&", "&amp;").replace("<", "&lt;")

# --------------------------------------------------------------------------- page record
def new_page(no, seed, title, tier, topic, strand, syll, oc, ptype, mech, instr, body, key_answers, check_result, note,
             check="Write the letters in order. Do they spell a word?", check_boxes=None, mk=("code",), ps=False, mech_plain=None, **extra):
    P = Page(no=no, title=title, tier=tier, topic=topic, strand=strand, syll=syll, oc=list(oc), ptype=ptype, mech=mech,
             instr=instr, body=body, check=check, check_boxes=check_boxes, mk=tuple(mk), ps=ps, seed=seed,
             key=dict(answers=key_answers, check_result=check_result), note=note)
    if mech_plain: P["mech_plain"] = mech_plain
    P.update(extra)
    return P

# --------------------------------------------------------------------------- html builders
def ab(cls=""):
    return '<span class="ab' + (" " + cls if cls else "") + '"></span>'

def qcard(no, content, ans="", cls=""):
    """one question card: number circle, content, answer area"""
    return f'<div class="qc {cls}"><div class="qh"><span class="no">{no}</span><div class="qt">{content}</div></div>' + (f'<div class="qa">{ans}</div>' if ans else "") + '</div>'

def qgrid(cards, cols=2, cls=""):
    return f'<div class="qg c{cols} {cls}">' + "".join(cards) + '</div>'

def table_block(table, fmt=str, cols=None):
    """the code table: one row of up to 6 boxes, two rows when there are more (three-digit numbers need room)"""
    n = len(table); cols = cols or (n if n <= 6 else (n + 1) // 2)
    items = "".join(f'<div class="ct"><span class="n">{fmt(k)}</span><span class="eq">=</span><b>{v}</b></div>' for k, v in table.items())
    return f'<div class="blk ctc"><p class="lead">Code table</p><div class="codetable" style="grid-template-columns:repeat({cols},1fr)">{items}</div></div>'

# vertical sums (algorithm layout): numbers right-aligned over a rule, answer box (or the result row) below
def _digs(x):
    return "".join('<i class="ab"></i>' if ch == "?" else f"<i>{ch}</i>" for ch in str(x))

def vsum_html(top, bot, op, res=None, ans_box=True):
    """top/bot/res are ints or strings of digits ('?' marks a missing digit, drawn as an answer box); without res a wide answer box is drawn"""
    last = (f'<div class="vr"><em></em>{_digs(res)}</div>' if res is not None else ('<div class="vr vans"><em></em><span class="ab w3"></span></div>' if ans_box else ""))
    return f'<div class="vsum"><div class="vr"><em></em>{_digs(top)}</div><div class="vr"><em>{op}</em>{_digs(bot)}</div><div class="vrule"></div>{last}</div>'

def parse_vsum(h):
    """independent reader of a vsum: returns (top, bottom, op) as ints"""
    rows = re.findall(r'<div class="vr">(.*?)</div>', h)
    def num(r): return int("".join(re.findall(r"<i>(\d)</i>", r)))
    op = re.search(r"<em>(.*?)</em>", rows[1]).group(1)
    return num(rows[0]), num(rows[1]), op

def parse_vsum3(h):
    """independent reader of a vsum with a result row: returns (top, bottom, result, op) as strings of digits with '?' for a missing digit"""
    rows = re.findall(r'<div class="vr">(.*?)</div>', h)
    def num(r): return "".join("?" if t.startswith('<i class="ab"') else t[3] for t in re.findall(r"<i[^>]*>(?:\d)?</i>", r))
    op = re.search(r"<em>(.*?)</em>", rows[1]).group(1)
    return num(rows[0]), num(rows[1]), num(rows[2]), op

def frac_html(f):
    k, n = f
    return f'<span class="fr"><i>{k}</i><i>{n}</i></span>'

# --------------------------------------------------------------------------- routes (grid mazes)
def neighbours(r, c, n):
    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        if 0 <= r + dr < n and 0 <= c + dc < n: yield r + dr, c + dc

def random_walk(rng, n, length, min_dist=4):
    for _ in range(4000):
        r, c = rng.randrange(n), rng.randrange(n)
        path = [(r, c)]; seen = {(r, c)}
        while len(path) < length:
            opts = [p for p in neighbours(*path[-1], n) if p not in seen]
            if not opts: break
            nxt = rng.choice(opts); path.append(nxt); seen.add(nxt)
        if len(path) == length and abs(path[0][0] - path[-1][0]) + abs(path[0][1] - path[-1][1]) >= min_dist:
            return path
    raise RuntimeError("walk")

def count_routes(grid_ok, n, start, finish, next_ok=None, limit=50):
    """simple routes start -> finish moving up/down/left/right through cells with grid_ok(cell)"""
    count = 0
    def dfs(cur, seen):
        nonlocal count
        if cur == finish: count += 1; return
        if count >= limit: return
        for nb in neighbours(*cur, n):
            if nb in seen or not grid_ok(nb): continue
            if next_ok and not next_ok(cur, nb): continue
            dfs(nb, seen | {nb})
    dfs(start, {start})
    return count

def all_routes(grid_ok, n, start, finish):
    out = []
    def dfs(cur, path):
        if cur == finish: out.append(list(path)); return
        for nb in neighbours(*cur, n):
            if nb in path or not grid_ok(nb): continue
            path.append(nb); dfs(nb, path); path.pop()
    dfs(start, [start])
    return out

def maze_html(n, texts, start, finish, cls="maze tall"):
    cells = ""
    for r in range(n):
        for c in range(n):
            tag = '<i class="flag">START</i>' if (r, c) == start else '<i class="flag">FINISH</i>' if (r, c) == finish else ""
            cells += f'<div class="mcell">{tag}<span>{texts[r][c]}</span></div>'
    return f'<div class="{cls}" style="grid-template-columns:repeat({n},1fr)">{cells}</div>'

def route_model(path, n):
    cells = [(r, c) for r in range(n) for c in range(n)]
    return cells

def mini_route_key(n, path):
    return mini_route(n, path)

# --------------------------------------------------------------------------- rows of lettered choices (the right choice of each row carries a letter of the word)
def choice_letters(rng, word, n_opts, tries=600):
    """rows[i] = [right letter, wrong letter, ...]: no other way of choosing one option in every row spells a word of the large list"""
    avail = [c for c in ALPHA if c not in word]
    for _ in range(tries):
        rows = []
        for i in range(len(word)):
            rows.append([word[i]] + rng.sample(avail, n_opts - 1))
        ok = True
        for combo in itertools.product(range(n_opts), repeat=len(word)):
            if not any(combo): continue
            w2 = "".join(rows[i][c] for i, c in enumerate(combo))
            if w2.lower() in BIG: ok = False; break
        if ok: return rows
    raise RuntimeError("choice letters")

def choice_other_words(word, rows):
    n = len(rows[0]); out = []
    for combo in itertools.product(range(n), repeat=len(word)):
        if not any(combo): continue
        w2 = "".join(rows[i][c] for i, c in enumerate(combo))
        if w2.lower() in BIG: out.append(w2)
    return out
