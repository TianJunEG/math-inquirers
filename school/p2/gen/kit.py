"""Shared kit of the Primary 2 pages: safe code words, the standard code-word record, small HTML builders, route helpers.
Everything is pure black and white. Each page module builds a puzzle from a seed, re-solves it with separate solver code that reads
the PRINTED text or drawing, and hands validate.py a `model` for the independent wrong-answer enumeration."""
import random, itertools, re, html as _html
from .common import *

# --------------------------------------------------------------------------- code words
# child-friendly words with distinct letters and exactly ONE arrangement that is a word (tested against the 129 000-word list)
SAFE5 = "black brick bunch chalk child climb cloth clown crown drink flute fruit glory house juice lunch month mouth piano plant quilt ranch scarf shark snack stamp thumb truck tulip uncle watch world young light".split()
SAFE6 = "bucket budget cymbal garlic hunter jacket jumper locket market pencil pigeon piglet pocket rocket salmon shovel spring studio sundae tongue tumble turtle family jungle pastry safety".split()
SAFE4 = "band cake camp card comb desk dish drum duck fish flag fork frog gold jump milk mint pink pond sock swim wave wind wing worm".split()

def word_ok(w):
    return len(set(w)) == len(w) and anagrams(w) == [w.lower()] and w.lower() in COMMON

def pick_word(rng, n, avoid=()):
    pool = {4: SAFE4, 5: SAFE5, 6: SAFE6}[n]
    c = [w for w in pool if w not in avoid and word_ok(w)]
    return rng.choice(c).upper()

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

def table_block(table, fmt=str):
    items = "".join(f'<div class="ct"><span class="n">{fmt(k)}</span><span class="eq">=</span><b>{v}</b></div>' for k, v in table.items())
    return f'<div class="blk ctc"><p class="lead">Code table</p><div class="codetable">{items}</div></div>'

# vertical sums (algorithm layout): numbers right-aligned over a rule, answer box below
def vsum_html(top, bot, op, miss=None, ans_box=True):
    """top/bot are ints or strings of digits (a '?' marks a missing digit shown as a box)"""
    def digs(x):
        s = str(x)
        return "".join('<i class="ab"></i>' if ch == "?" else f"<i>{ch}</i>" for ch in s)
    return (f'<div class="vsum"><div class="vr"><em></em>{digs(top)}</div><div class="vr"><em>{op}</em>{digs(bot)}</div><div class="vrule"></div>'
            + ('<div class="vr vans"><em></em><span class="ab w3"></span></div>' if ans_box else '') + '</div>')

def parse_vsum(h):
    """independent reader of a vsum: returns (top, bottom, op)"""
    rows = re.findall(r'<div class="vr">(.*?)</div>', h)
    def num(r): return int("".join(re.findall(r"<i>(\d)</i>", r)))
    op = re.search(r"<em>(.*?)</em>", rows[1]).group(1)
    return num(rows[0]), num(rows[1]), op

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
