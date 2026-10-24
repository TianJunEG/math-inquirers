"""Level 6 helpers for holiday week 2 (lessons 3 and 4): figures and an independent interpreter for the block programs of p6/content/l3.js and l4.js.

* The code blocks are drawn by the workbook's own blocksSvg() (called through blocks_bridge2.js); a program is ONE list [[indent, kind, text], ...] and the same list
  is drawn and run, so the picture and the checked answer cannot disagree.  `[...]` in a block's text is a value pill.
* `run` is a small interpreter for those programs (set / change / repeat / repeat until / ask / say); every code question's checker runs the program as drawn.
* number lines, tables, machines, the sea-level picture and the age bars are plain inline SVG (no coin or note images).
"""
import json, os, re, subprocess
import p6lib as P
from p6lib import NAVY, YEL, TEAL, WARM, PALE, T, esc

HERE = os.path.dirname(os.path.abspath(__file__))
SKY, RED, GREY = '#DDEBF7', '#C03B3B', '#8A94AD'
MINUS = '−'


def neg(v):
    return (MINUS + str(-v)) if isinstance(v, int) and v < 0 else str(v)


# ---------------------------------------------------------------- code blocks (workbook drawing) and their interpreter
_cache = {}


def blocks(prog, label, fs=17, grow=1.3):
    """The workbook's block drawing of `prog`.  The red 'set / change' blocks are 4.4:1 with their white text in print; here a slightly darker red (5.3:1)."""
    key = json.dumps([prog, label, fs])
    if key not in _cache:
        r = subprocess.run(['node', os.path.join(HERE, 'blocks_bridge2.js')], input=json.dumps([dict(prog=prog, label=label, fs=fs)]), capture_output=True, text=True, check=True)
        _cache[key] = json.loads(r.stdout)[0]
    svg = _cache[key].replace('#D64545', RED)
    w = float(re.search(r'viewBox="0 0 ([\d.]+) ', svg).group(1))
    return re.sub(r'style="[^"]*"', f'style="width:100%;max-width:{w * grow:.0f}px;height:auto;display:block;margin:0 auto"', svg, count=1)


def _num(e, v):
    e = e.strip().replace(MINUS, '-')
    e = e.replace('x position', 'x').replace('×', '*').replace('÷', '//')
    e = re.sub(r'(?<![<>!=])=(?!=)', '==', e)
    for k in sorted(v, key=len, reverse=True):
        e = re.sub(r'\b%s\b' % re.escape(k), str(v[k]), e)
    if not re.fullmatch(r'[\d\s+\-*/()=<>!]*', e):
        raise ValueError('cannot evaluate: ' + e)
    return eval(e)


def _tree(prog):
    root, stack = [], [(-1, None)]
    out = []
    for ind, kind, text in prog:
        node = [kind, text, []]
        while stack[-1][0] >= ind:
            stack.pop()
        (root if stack[-1][1] is None else stack[-1][1][2]).append(node)
        stack.append((ind, node))
    return root


def run(prog, answer=None, v=None, limit=100000):
    """Runs the program as drawn. Returns (list of said values, final variables)."""
    v = dict(v or {})
    if answer is not None:
        v['answer'] = answer
    said = []
    steps = [0]

    def go(nodes):
        for kind, text, kids in nodes:
            steps[0] += 1
            if steps[0] > limit:
                raise ValueError('loop does not stop')
            t = text.strip()
            if t == 'when green flag clicked':
                continue
            m = re.fullmatch(r'ask \[.*\] and wait', t)
            if m:
                continue
            m = re.fullmatch(r'set (\w+) to \[(.+)\]', t)
            if m:
                v[m.group(1)] = _num(m.group(2), v); continue
            m = re.fullmatch(r'change (\w+) by \[(.+)\]', t)
            if m:
                v[m.group(1)] += _num(m.group(2), v); continue
            m = re.fullmatch(r'say \[(.+?)\](?: for \[\d+\] seconds)?', t)
            if m:
                said.append(_num(m.group(1), v)); continue
            m = re.fullmatch(r'repeat until \[(.+)\]', t)
            if m:
                while not _num(m.group(1), v):
                    go(kids)
                continue
            m = re.fullmatch(r'repeat \[(.+)\]', t)
            if m:
                for _ in range(_num(m.group(1), v)):
                    go(kids)
                continue
            raise ValueError('cannot run block: ' + t)
    go(_tree(prog))
    return said, v


def fill(prog, values):
    """Replaces the blanks of a plan, in order of appearance: an empty pill '[      ]' becomes '[value]', and '___' inside a pill becomes the value."""
    vals = list(values)
    out = []

    def sub(m):
        v = str(vals.pop(0)).replace('-', MINUS)
        return v if m.group(0) == '___' else '[' + v + ']'
    for ind, kind, text in prog:
        out.append([ind, kind, re.sub(r'\[ +\]|___', sub, text)])
    assert not vals, 'more values than blanks'
    return out


def nb(frame, budget=14):
    """The last few words before a box (about `budget` characters) get non-breaking spaces, so a label and its box stay together when the line wraps.
    Separators of 2 or more spaces stay breakable, and a unit never grows wider than a short label plus its box (that fits a 360 px phone)."""
    parts = re.split(r'(\{f\d+\})', frame)
    for i in range(len(parts) - 1):
        p = parts[i]
        if re.fullmatch(r'\{f\d+\}', p) or not p.endswith(' ') or p.endswith('  '):
            continue
        cut = p.rfind('  ') + 2 if '  ' in p else 0
        head, tail = p[:cut], p[cut:]
        toks = tail[:-1].split(' ')
        k, used = 0, 0
        while k < len(toks) and (k == 0 or used + len(toks[-1 - k]) <= budget):
            used += len(toks[-1 - k]) + 1
            k += 1
        keep, bound = toks[:len(toks) - k], toks[len(toks) - k:]
        parts[i] = head + (' '.join(keep) + ' ' if keep else '') + '\u00a0'.join(bound) + '\u00a0'
    return ''.join(parts)


def show(prog):
    """Display form: ASCII minus signs in numbers become the minus sign used in the workbook."""
    return [[i, k, re.sub(r'(?<![\w\)])-(?=\d)', MINUS, t)] for i, k, t in prog]


# ---------------------------------------------------------------- svg helpers
def wrap(body, W, H, label, maxw=None):
    return (f'<svg viewBox="0 0 {W:.0f} {H:.0f}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{esc(label)}" '
            f'style="width:100%;max-width:{maxw or W:.0f}px;height:auto;display:block;margin:0 auto" font-family="Nunito Sans, Arial, sans-serif">{body}</svg>')


def line(x1, y1, x2, y2, sw=2.5, c=NAVY, dash=None):
    return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{c}" stroke-width="{sw}" stroke-linecap="round"' + (f' stroke-dasharray="{dash}"' if dash else '') + '/>'


def rect(x, y, w, h, fill='#fff', stroke=NAVY, sw=2.2, rx=0):
    return f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'


def table_svg(head, rows, label, colw=None, fs=15, rh=32):
    """A table drawn as svg; head is the yellow header row (or None)."""
    allr = ([head] if head else []) + rows
    n = len(allr[0])
    colw = colw or [max(54, 9 * max(len(str(r[i])) for r in allr) + 18) for i in range(n)]
    W = sum(colw) + 8
    b = ''
    for ri, r in enumerate(allr):
        x = 4
        for ci, val in enumerate(r):
            hd = head and ri == 0
            b += rect(x, 4 + ri * rh, colw[ci], rh, YEL if hd else '#fff', NAVY, 2) + T(x + colw[ci] / 2, 4 + ri * rh + rh / 2 + fs * 0.35, val, fs, 'middle', 800 if hd else 600)
            x += colw[ci]
    return wrap(b, W, rh * len(allr) + 8, label)


def number_line(lo, hi, marks=(), label_every=2, sp=16, label='Number line', hops=(), fs=14, arrows=True, height=None):
    """Number line lo..hi with a tick at every whole number and labels every `label_every`. marks: [(value, letter)] shown as a dot with a letter above.
    hops: [(from, to, colour, height)] drawn as arcs above the line."""
    pad = 22
    W = (hi - lo) * sp + 2 * pad
    top = height or (46 if marks else 30)
    ly = top + (0 if not hops else 0)
    X = lambda v: pad + (v - lo) * sp
    b = line(pad - 14, ly, W - pad + 14, ly, 2.5)
    if arrows:
        b += f'<polygon points="{pad - 20},{ly} {pad - 10},{ly - 5} {pad - 10},{ly + 5}" fill="{NAVY}"/><polygon points="{W - pad + 20},{ly} {W - pad + 10},{ly - 5} {W - pad + 10},{ly + 5}" fill="{NAVY}"/>'
    for v in range(lo, hi + 1):
        big = v % label_every == 0
        b += line(X(v), ly - (8 if big else 5), X(v), ly + (8 if big else 5), 3 if v == 0 else 1.8)
        if big:
            b += T(f'{X(v):.1f}', ly + 26, neg(v), fs, 'middle', 800 if v == 0 else 600, TEAL if v == 0 else NAVY)
    for v, t in marks:
        b += f'<circle cx="{X(v):.1f}" cy="{ly}" r="6" fill="{YEL}" stroke="{NAVY}" stroke-width="2.2"/>' + T(f'{X(v):.1f}', ly - 14, t, fs + 3, 'middle', 800)
    for a, c, col, hh in hops:
        x1, x2 = X(a), X(c)
        b += f'<path d="M{x1:.1f} {ly} C{x1:.1f} {ly - hh} {x2:.1f} {ly - hh} {x2:.1f} {ly}" fill="none" stroke="{col}" stroke-width="3"/>'
        b += f'<circle cx="{x1:.1f}" cy="{ly}" r="4.5" fill="{col}"/><circle cx="{x2:.1f}" cy="{ly}" r="4.5" fill="{col}" stroke="{NAVY}" stroke-width="1.5"/>'
    return wrap(b, W, ly + 38, label)


def hop_lines(lo, hi, groups, label):
    """Several stacked number lines: groups = [(caption, [(from, to), ...])]; the arcs go from b up to a."""
    cols = [TEAL, WARM, NAVY, '#7B3FA0']
    sp, pad = 22, 22
    W = (hi - lo) * sp + 2 * pad
    b, y = '', 0
    for cap, pairs in groups:
        b += T(6, y + 18, cap, 15, 'start', 800)
        hh = 40 + 22 * len(pairs)
        ly = y + 30 + hh
        X = lambda v: pad + (v - lo) * sp
        b += line(pad - 12, ly, W - pad + 12, ly, 2.5)
        for v in range(lo, hi + 1):
            b += line(X(v), ly - 5, X(v), ly + 5, 3 if v == 0 else 1.6) + T(f'{X(v):.1f}', ly + 24, neg(v), 13, 'middle', 800 if v == 0 else 600, TEAL if v == 0 else NAVY)
        for k, (a, c) in enumerate(pairs):
            col, h2 = cols[k % 4], 30 + 22 * k + 14
            b += f'<path d="M{X(a):.1f} {ly} C{X(a):.1f} {ly - h2} {X(c):.1f} {ly - h2} {X(c):.1f} {ly}" fill="none" stroke="{col}" stroke-width="3"/>'
            b += f'<circle cx="{X(a):.1f}" cy="{ly}" r="5" fill="{col}"/><circle cx="{X(c):.1f}" cy="{ly}" r="5" fill="{col}" stroke="{NAVY}" stroke-width="1.5"/>'
        y = ly + 36
    return wrap(b, W, y, label)


def vertical_line(lo, hi, step, marks, label, unit=' m', sc=8, width=300, extra=None):
    """Vertical number line (metres) with labelled marks: marks = [(value, text)]. Sea level is the 0 line, the sea shaded below it."""
    pad = 14
    Y = lambda v: pad + (hi - v) * sc
    H = (hi - lo) * sc + 2 * pad
    ax = 70
    b = rect(ax, Y(0), width - ax - 6, Y(lo) - Y(0), SKY, 'none', 0)
    b += line(ax, Y(0), width - 6, Y(0), 2, TEAL) + T(width - 10, Y(0) - 6, 'sea level', 14, 'end', 800, TEAL)
    b += line(ax, Y(hi), ax, Y(lo), 2.5)
    for v in range(lo, hi + 1):
        if v % step == 0:
            b += line(ax - 6, Y(v), ax + 6, Y(v), 2) + T(ax - 10, Y(v) + 5, neg(v) + unit, 14, 'end', 800 if v == 0 else 600, TEAL if v == 0 else NAVY)
    for v, t, kind in marks:
        cx = ax + 70
        b += line(ax + 6, Y(v), cx - 16, Y(v), 1.5, NAVY, '4 4')
        if kind == 'gull':
            b += f'<path d="M{cx - 20} {Y(v)} q10 -12 20 0 q10 -12 20 0" fill="none" stroke="{NAVY}" stroke-width="3"/>'
        elif kind == 'diver':
            b += f'<ellipse cx="{cx}" cy="{Y(v)}" rx="20" ry="7" fill="{YEL}" stroke="{NAVY}" stroke-width="2"/><circle cx="{cx + 26}" cy="{Y(v)}" r="7" fill="{YEL}" stroke="{NAVY}" stroke-width="2"/>'
        elif kind == 'crab':
            b += f'<ellipse cx="{cx}" cy="{Y(v)}" rx="14" ry="8" fill="{RED}" stroke="{NAVY}" stroke-width="2"/>'
        b += T(cx + 44, Y(v) + 5, t, 15, 'start', 800)
    return wrap(b, width, H, label)


def machine_rows(rows, label):
    """rows: [(name, [ops])]. Each row: name above, then n -> op -> op -> OUT."""
    b, y = '', 0
    for name, ops in rows:
        b += T(6, y + 18, name, 16, 'start', 800, TEAL)
        x, yy = 6, y + 28
        b += rect(x, yy, 40, 34, YEL, NAVY, 2, 8) + T(x + 20, yy + 23, 'n', 17, 'middle', 800)
        x += 40
        for o in ops + ['OUT']:
            b += line(x, yy + 17, x + 20, yy + 17, 2.5) + f'<polygon points="{x + 28},{yy + 17} {x + 18},{yy + 11} {x + 18},{yy + 23}" fill="{NAVY}"/>'
            x += 28
            w = 58 if o == 'OUT' else 52
            b += rect(x, yy, w, 34, SKY if o == 'OUT' else '#fff', NAVY, 2, 8) + T(x + w / 2, yy + 23, o, 17, 'middle', 800)
            x += w
        y += 76
    return wrap(b, x + 8, y - 8, label)


def age_bars(label):
    """Mei and her mother, now and in 12 years (bars not to scale)."""
    u, sh = 52, 70
    rows = [('Mei now', [(u, '#fff', '')]), ('Mother now', [(u, '#fff', '')] * 3),
            ('Mei in 12 years', [(u, '#fff', ''), (sh, YEL, '+ 12')]), ('Mother in 12 years', [(u, '#fff', '')] * 3 + [(sh, YEL, '+ 12')])]
    b, y = '', 0
    for name, segs in rows:
        b += T(6, y + 16, name, 15, 'start', 800, TEAL)
        x = 6
        for w, f, t in segs:
            b += rect(x, y + 22, w, 28, f, NAVY, 2) + (T(x + w / 2, y + 42, t, 15, 'middle', 800) if t else '')
            x += w
        y += 60
    return wrap(b, 6 + 3 * u + sh + 8, y, label)


def in_out(ins, outs, label):
    cells = [['IN'] + [str(i) for i in ins], ['OUT'] + [('?' if o is None else str(o)) for o in outs]]
    return table_svg(None, cells, label, colw=[52] + [48] * len(ins), fs=17, rh=36)


# ---------------------------------------------------------------- accepted writings of an algebra rule, each one CHECKED by evaluation
def _eval_form(s, n):
    t = s.lower().replace(' ', '').replace('out=', '').replace('×', '*').replace('·', '*').replace('−', '-')
    t = re.sub(r'(?<=\d)(?=[n(])', '*', t)
    t = re.sub(r'(?<=n)(?=[\d(n])', '*', t)
    t = re.sub(r'(?<=\))(?=[\dn(])', '*', t)
    t = t.replace('n', f'({n})')
    if not re.fullmatch(r'[\d+\-*/()]*', t):
        raise ValueError('bad form ' + s)
    return eval(t)


def verified_forms(forms, fn):
    """Keeps the writings in `forms`, after checking that every one equals fn(n) for n = -6..30."""
    for f in forms:
        for n in range(-6, 31):
            if _eval_form(f, n) != fn(n):
                raise AssertionError(f'{f!r} does not equal the rule at n={n}')
    out = []
    for f in forms:
        out += [f, 'OUT = ' + f, 'out=' + f.replace(' ', '')]
    seen = []
    for f in out:
        if f not in seen:
            seen.append(f)
    return seen
