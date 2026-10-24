"""Level 6 helpers for holiday week 5 (lessons 9 and 10): the workbook's own block, list-panel, dot-plot and hexagon drawings, plain svg figures, and independent checkers.

* Figures: blocks_bridge5.js loads p6/content/l9.js and l10.js and calls THEIR blocks(), codeFig(), hexChains() and the FG.dotPlot() specification of Q1 and Q4 as printed.
  The same program list (strings and {c, body} objects, as in the workbook) is drawn AND run by `run`, so a picture and its checked answer cannot disagree.
* Checkers: exact means with Fractions (total / how many), the median and the mode found by sorting and counting, a small interpreter for the list-and-loop programs of lesson 9,
  brute force for the primes, factors and sequences of lesson 10, and exact enumeration of the 64 spinner pairs (so no simulation is used to check a probability).
"""
import json, math, os, re, subprocess
from fractions import Fraction
from p6lib import NAVY, YEL, TEAL, WARM, PALE, T, esc
import w3lib

HERE = os.path.dirname(os.path.abspath(__file__))
RED = '#C03B3B'
MINUS = '−'
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
_cache = {}


def bridge(req):
    key = json.dumps(req, sort_keys=True)
    if key not in _cache:
        r = subprocess.run(['node', os.path.join(HERE, 'blocks_bridge5.js')], input=json.dumps([req]), capture_output=True, text=True, check=True)
        _cache[key] = json.loads(r.stdout)[0]
    return _cache[key]


def _full(svg, grow=1.25, role_label=None):
    """Make an svg from the workbook fill its box (width 100%, capped at grow x its natural width), text unchanged."""
    w = float(re.search(r'viewBox="0 0 ([\d.]+) ', svg).group(1))
    i = svg.index('>')
    head = re.sub(r'\swidth="[\d.]+"', '', svg[:i])
    head = re.sub(r'\sstyle="[^"]*"', '', head)
    head += f' style="width:100%;max-width:{w * grow:.0f}px;height:auto;display:block;margin:0 auto" role="img"'
    return head + svg[i:]


def blocks(lesson, prog, label, fs=16, grow=1.2):
    """The workbook's block drawing (lesson 'l9' or 'l10') of `prog`: a list of strings and {c, body[, else]} objects."""
    r = bridge(dict(kind='blocks', lesson=lesson, prog=prog, fs=fs))
    body = r['svg'].replace('#D64545', RED)             # white on the workbook's red is 4.4:1; this red is 5.3:1 (the printed colour is unchanged)
    body = re.sub(r'<text[^>]*>\s*</text>', '', body)
    return (f'<svg viewBox="0 0 {r["w"]} {r["h"]}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{esc(label)}" '
            f'style="width:100%;max-width:{r["w"] * grow:.0f}px;height:auto;display:block;margin:0 auto">{body}</svg>')


def codefig(prog, aria, name, vals, grow=1.15):
    """The workbook's code blocks with the list panel beside them (l9.js codeFig)."""
    s = bridge(dict(kind='codefig', prog=prog, aria=aria, list=[name, [str(v) for v in vals]]))
    return _full(s.replace('#D64545', RED), grow)


def dot1():
    return _full(bridge(dict(kind='dot1')), 1.3)


def dot4():
    return _full(bridge(dict(kind='dot4')), 1.3)


def hexfig():
    return _full(bridge(dict(kind='hex')), 1.3)


def fg_grid(rows, cols, row_title, col_title, label, cellw=34):
    head = [f'{row_title} ↓  {col_title} →'] + [str(c) for c in cols]
    body = [[str(r)] + [''] * len(cols) for r in rows]
    return w3lib.table_svg(head, body, label, [200] + [cellw] * len(cols), 15, 28)


def table_svg(head, rows, label, colw=None, fs=15, rh=30, shade=None):
    return w3lib.table_svg(head, rows, label, colw, fs, rh, shade)


def nb(frame, budget=14):
    return w3lib.nb(frame, budget)


# ---------------------------------------------------------------- statistics (exact)
def mean(vals):
    return Fraction(sum(vals), len(vals))


def median(vals):
    s = sorted(vals)
    n = len(s)
    return Fraction(s[n // 2]) if n % 2 else Fraction(s[n // 2 - 1] + s[n // 2], 2)


def modes(vals):
    """Values that occur most often; [] when every value occurs once (no mode)."""
    cnt = {}
    for v in vals:
        cnt[v] = cnt.get(v, 0) + 1
    top = max(cnt.values())
    if top == 1:
        return []
    return sorted(v for v, c in cnt.items() if c == top)


def whole(f):
    f = Fraction(f)
    assert f.denominator == 1, f
    return int(f)


def dec(f):
    """A Fraction as a short decimal string ('6.6', '10')."""
    f = Fraction(f)
    if f.denominator == 1:
        return str(f.numerator)
    s = f'{float(f):.4f}'.rstrip('0').rstrip('.')
    assert Fraction(s) == f, f
    return s


# ---------------------------------------------------------------- the interpreter for the lesson 9 list programs (strings and {c, body} objects, as the workbook draws them)
def _expr(e, v, lists):
    s = e.strip()
    s = re.sub(r'\(\s*item (\w+) of (\w+)\s*\)', lambda m: f'ITEM({m.group(2)}, {m.group(1)})', s)
    s = re.sub(r'\(\s*length of (\w+)\s*\)', lambda m: f'len({m.group(1)})', s)
    s = re.sub(r'\b(\d+)\b', r'F(\1)', s)
    ns = dict(v)
    ns.update(lists)
    ns.update(F=Fraction, ITEM=lambda L, i: L[int(i) - 1], len=len, __builtins__={})
    return eval(s, ns)


def run(prog, v=None, lists=None, trace=None, limit=100000):
    """Runs a lesson 9 program. Returns (said values in order, final variables).  `trace`, if a list, gets a copy of the variables at the end of every pass of the first repeat loop."""
    v = {k: Fraction(x) for k, x in (v or {}).items()}
    lists = {k: list(x) for k, x in (lists or {}).items()}
    said, steps, top = [], [0], [True]

    def go(items, depth=0):
        for it in items:
            steps[0] += 1
            if steps[0] > limit:
                raise ValueError('loop does not stop')
            if isinstance(it, dict):
                head = it['c']
                m = re.fullmatch(r'repeat (.+)', head)
                if m:
                    for _ in range(int(_expr(m.group(1), v, lists))):
                        go(it['body'], depth + 1)
                        if trace is not None and depth == 0:
                            trace.append({k: x for k, x in v.items()})
                    continue
                m = re.fullmatch(r'if (.+) then', head)
                if m:
                    if _cond(m.group(1), v, lists):
                        go(it['body'], depth + 1)
                    elif it.get('else'):
                        go(it['else'], depth + 1)
                    continue
                raise ValueError('cannot run block: ' + head)
            text = it
            if text.startswith('when '):
                continue
            m = re.fullmatch(r'set (\w+) to (.+)', text)
            if m:
                v[m.group(1)] = Fraction(_expr(m.group(2), v, lists)); continue
            m = re.fullmatch(r'change \(?(\w+)\)? by (.+)', text)
            if m:
                v[m.group(1)] = v[m.group(1)] + _expr(m.group(2), v, lists); continue
            m = re.fullmatch(r'say (.+)', text)
            if m:
                said.append(Fraction(_expr(m.group(1), v, lists))); continue
            raise ValueError('cannot run block: ' + text)

    def _cond(c, v, lists):
        m = re.fullmatch(r'(.+?) ([<>=]) (.+)', c)
        a, op, b = _expr(m.group(1), v, lists), m.group(2), _expr(m.group(3), v, lists)
        return a > b if op == '>' else a < b if op == '<' else a == b
    go(prog)
    return said, v


# ---------------------------------------------------------------- number helpers (plain loops)
def factors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def is_prime(n):
    return len(factors(n)) == 2


def primes_between(lo, hi):
    return [k for k in range(lo, hi + 1) if is_prime(k)]


def prime_factors(n):
    out, d = [], 2
    while n > 1:
        while n % d == 0:
            out.append(d); n //= d
        d += 1
    return out


def sticks_of_hexagons(n):
    """Sticks in a chain of n hexagons: the first hexagon needs 6 and every new one shares one side with the one before."""
    total = 6
    for _ in range(n - 1):
        total += 6 - 1
    return total


def clock_after(start, hours, size=12):
    pos = start
    step = 1 if hours >= 0 else -1
    for _ in range(abs(hours)):
        pos += step
        if pos > size:
            pos = 1
        if pos < 1:
            pos = size
    return pos


def interior_angle(n):
    return Fraction((n - 2) * 180, n)
