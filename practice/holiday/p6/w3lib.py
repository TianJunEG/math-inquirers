"""Level 6 helpers for holiday week 3 (lessons 5 and 6): the workbook's own figures and independent interpreters for its block programs.

* Figures: blocks_bridge3.js loads p6/content/l5.js and l6.js and calls THEIR blocks(), cards(), grid(), spinner() and the FG.grid() tables as printed; the program that is
  drawn is the very list the checkers run (`program()` returns the workbook's own listCode / planCode / coinCode), so a picture and its checked answer cannot disagree.
* `run`: a small interpreter for the nested programs of lesson 5 (set / change / repeat / if / say, with join).  `expected_changes`: the exact expected count of the random
  programs of lesson 6, found by listing every equally likely outcome (no simulation, no copied answer).
* Plain-svg figures for the correct drawings (route counts, the table of ways to pay, the difference table, the winners grids).  No coin or note images.
"""
import copy, itertools, json, os, re, subprocess
from fractions import Fraction
import p6lib as P
from p6lib import NAVY, YEL, TEAL, WARM, PALE, T, esc

HERE = os.path.dirname(os.path.abspath(__file__))
SKY, RED, GREY = '#DDEBF7', '#C03B3B', '#8A94AD'
MINUS = '−'
_cache = {}


def bridge(req):
    key = json.dumps(req, sort_keys=True)
    if key not in _cache:
        r = subprocess.run(['node', os.path.join(HERE, 'blocks_bridge3.js')], input=json.dumps([req]), capture_output=True, text=True, check=True)
        _cache[key] = json.loads(r.stdout)[0]
    return _cache[key]


def program(lesson, named):
    """The workbook's own program list (kind, text, children) for listCode / planCode / coinCode."""
    return json.loads(bridge(dict(lesson=lesson, kind='prog', named=named)))


def _full_width(svg, grow=1.25):
    w = float(re.search(r'viewBox="0 0 ([\d.]+) ', svg).group(1))
    svg = re.sub(r'\swidth="[\d.]+"', '', svg, count=1)
    return re.sub(r'style="[^"]*"', f'style="width:100%;max-width:{w * grow:.0f}px;height:auto;display:block;margin:0 auto"', svg, count=1)


def blocks(lesson, prog, label, fs=17):
    """The workbook's block drawing of `prog` (a list as returned by program(), possibly with blanks filled)."""
    svg = bridge(dict(lesson=lesson, kind='blocks', prog=prog, label=label, fs=fs))
    svg = svg.replace('#D64545', RED)                      # white on the workbook's red is 4.4:1; this red is 5.3:1 (the printed colour is unchanged)
    return _full_width(re.sub(r'<text[^>]*>\s*</text>', '', svg))


def cards(digits):
    return _full_width(bridge(dict(lesson='l5', kind='cards', digits=list(digits))), 1.1)


def street_grid():
    return _full_width(bridge(dict(lesson='l5', kind='grid')), 1.2)


def spinner():
    return _full_width(bridge(dict(lesson='l6', kind='spinner')), 1.0)


def fg_grid(rows, cols, row_title, col_title, cell, label):
    svg = bridge(dict(lesson='l6', kind='fggrid', spec=dict(rows=rows, cols=cols, rowTitle=row_title, colTitle=col_title, cell=cell, label=label)))
    return _full_width(svg, 1.2)


# ---------------------------------------------------------------- the interpreter for the nested programs
def _strip(t):
    return t.replace('[', '').replace(']', '').strip()


def _expr(e, v):
    e = e.strip()
    m = re.fullmatch(r'join (\w+) (\w+)', e)
    if m:
        return int(str(v[m.group(1)]) + str(v[m.group(2)]))
    if re.fullmatch(r'-?\d+', e):
        return int(e)
    if re.fullmatch(r'\w+', e):
        return v[e]
    raise ValueError('cannot evaluate: ' + e)


def holds(cond, v):
    """A test such as 'a < b' or 'a = b' with the variables in v (anything else is refused, nothing is run as code)."""
    c = cond.strip().replace('≠', '!=').replace('≤', '<=').replace('≥', '>=')
    c = re.sub(r'(?<![<>!=])=(?!=)', '==', c)
    if not re.fullmatch(r'[a-z\d\s<>=!]+', c):
        raise ValueError('cannot test: ' + cond)
    return bool(eval(c, {'__builtins__': {}}, dict(v)))


def run(prog, v=None, limit=200000):
    """Runs a nested program [[kind, text, kids?], ...]. Returns (said values in order, final variables)."""
    v = dict(v or {})
    said = []
    steps = [0]

    def go(items):
        for it in items:
            steps[0] += 1
            if steps[0] > limit:
                raise ValueError('loop does not stop')
            kind, text = it[0], _strip(it[1])
            kids = it[2] if len(it) > 2 else []
            if kind == 'hat':
                continue
            m = re.fullmatch(r'set (\w+) to (.+)', text)
            if m:
                v[m.group(1)] = _expr(m.group(2), v); continue
            m = re.fullmatch(r'change (\w+) by (.+)', text)
            if m:
                v[m.group(1)] += _expr(m.group(2), v); continue
            m = re.fullmatch(r'say (.+?)(?: for \d+ seconds)?', text)
            if m:
                said.append(_expr(m.group(1), v)); continue
            m = re.fullmatch(r'repeat (.+)', text)
            if m:
                for _ in range(_expr(m.group(1), v)):
                    go(kids)
                continue
            m = re.fullmatch(r'if (.+) then', text)
            if m:
                if holds(m.group(1), v):
                    go(kids)
                continue
            raise ValueError('cannot run block: ' + text)
    go(prog)
    return said, v


def fill(prog, values):
    """Fills the dashed gaps '[?]' of a plan with `values`, in order of appearance (top to bottom)."""
    vals = [str(x) for x in values]
    p2 = copy.deepcopy(prog)

    def walk(items):
        for it in items:
            it[1] = re.sub(r'\[\?\]', lambda m: '[' + vals.pop(0) + ']', it[1])
            if len(it) > 2:
                walk(it[2])
    walk(p2)
    assert not vals, 'more values than gaps'
    return p2


def expected_changes(prog):
    """Exact expected number the program ends with for the random programs of lesson 6: the outer 'repeat [N]' runs N times; each time every 'pick random 1 to K'
    (set to a variable, or inside the test) takes each of its K values with equal chance; the test is an 'if' that changes a counter by 1.
    The chance of the test is found by listing every combination of the random numbers, so the answer is N times a fraction (never simulated)."""
    outer = next(it for it in prog if it[0] == 'ctrl' and _strip(it[1]).startswith('repeat '))
    reps = int(_strip(outer[1]).split()[1])
    rand, cond = {}, None

    def walk(items):
        nonlocal cond
        for it in items:
            t = _strip(it[1])
            m = re.fullmatch(r'set (\w+) to pick random 1 to (\d+)', t)
            if m:
                rand[m.group(1)] = int(m.group(2))
            m = re.fullmatch(r'if (.+) then', t)
            if m:
                cond = m.group(1)
            if len(it) > 2:
                walk(it[2])
    walk(outer[2])
    inline = re.findall(r'pick random 1 to (\d+)', cond)
    c = cond
    for k, K in enumerate(inline):
        c = re.sub(r'pick random 1 to \d+', f'r{k}', c, count=1)
        rand[f'r{k}'] = int(K)
    names = list(rand)
    total = hits = 0
    for combo in itertools.product(*[range(1, rand[n] + 1) for n in names]):
        total += 1
        hits += holds(c, dict(zip(names, combo)))
    return Fraction(hits, total) * reps


# ---------------------------------------------------------------- counting helpers (brute force)
def routes(n_right, n_up, blocked=()):
    """Routes from (0,0) to (n_right, n_up) going only right or up, avoiding the points in `blocked`: counted by walking every sequence of moves."""
    n = 0
    for pos in set(itertools.permutations('R' * n_right + 'U' * n_up)):
        x = y = 0
        ok = (0, 0) not in blocked
        for m in pos:
            x, y = (x + 1, y) if m == 'R' else (x, y + 1)
            if (x, y) in blocked:
                ok = False
                break
        n += ok
    return n


def corner_counts(size, blocked=()):
    """The numbers written in the circles: routes from A=(0,0) to every point (x, y) of a size-by-size grid of streets, by brute force."""
    return {(x, y): routes(x, y, blocked) for x in range(size + 1) for y in range(size + 1)}


def routes_fig(size=3, blocked=(), label=''):
    """The 4 by 4 circles of the street grid, each with its number of routes from A (the correct drawing)."""
    cnt = corner_counts(size, blocked)
    c, x0, y0 = 56, 40, 24
    b = ''
    for i in range(size + 1):
        b += f'<line x1="{x0}" y1="{y0 + i * c}" x2="{x0 + size * c}" y2="{y0 + i * c}" stroke="{NAVY}" stroke-width="3.5"/><line x1="{x0 + i * c}" y1="{y0}" x2="{x0 + i * c}" y2="{y0 + size * c}" stroke="{NAVY}" stroke-width="3.5"/>'
    for (x, y), v in cnt.items():
        cx, cy = x0 + x * c, y0 + (size - y) * c
        hit = (x, y) in blocked
        b += f'<circle cx="{cx}" cy="{cy}" r="19" fill="{YEL if (x, y) == (size, size) else ("#E9D9D2" if hit else "#fff")}" stroke="{NAVY}" stroke-width="{3.5 if hit else 2.5}"/>' + T(cx, cy + 6, v, 17, 'middle', 800)
    b += T(x0 - 28, y0 + size * c + 30, 'A', 22, 'middle', 800, TEAL) + T(x0 + size * c + 24, y0 - 8, 'B', 22, 'middle', 800, TEAL)
    W, H = x0 * 2 + size * c, y0 + size * c + 40
    return (f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{esc(label)}" '
            f'style="width:100%;max-width:{W}px;height:auto;display:block;margin:0 auto" font-family="Nunito Sans, Arial, sans-serif">{b}</svg>')


def table_svg(head, rows, label, colw=None, fs=15, rh=30, shade=None):
    """A table drawn as svg; head is the yellow header row; shade(r, c) -> fill colour or None for a body cell."""
    allr = ([head] if head else []) + rows
    n = len(allr[0])
    colw = colw or [max(46, 9 * max(len(str(r[i])) for r in allr) + 18) for i in range(n)]
    W = sum(colw) + 8
    b = ''
    for ri, r in enumerate(allr):
        x = 4
        for ci, val in enumerate(r):
            hd = head and ri == 0
            fill = YEL if hd else ((shade(ri - (1 if head else 0), ci) if shade else None) or '#fff')
            b += (f'<rect x="{x}" y="{4 + ri * rh}" width="{colw[ci]}" height="{rh}" fill="{fill}" stroke="{NAVY}" stroke-width="2"/>'
                  + T(x + colw[ci] / 2, 4 + ri * rh + rh / 2 + fs * 0.35, val, fs, 'middle', 800 if hd else 600))
            x += colw[ci]
    H = rh * len(allr) + 8
    return (f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{esc(label)}" '
            f'style="width:100%;max-width:{W}px;height:auto;display:block;margin:0 auto" font-family="Nunito Sans, Arial, sans-serif">{b}</svg>')


def nb(frame, budget=14):
    """Keeps the last few words before a box (about `budget` characters) together with the box (non-breaking spaces), as in week 2."""
    import w2lib as W
    return W.nb(frame, budget)
