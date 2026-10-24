"""Level 2 (P2) helpers for holiday week 5 (lesson 9 Measure Masters, lesson 10 Puzzle Day): the jug puzzles (a step simulator and a breadth-first search for the fewest steps),
the clocks, picture graph, cake strip and towers READ BACK from the printed figures (so the checkers do not use the answers), small figures drawn for a phone (jugs, clue cards with a
tick-and-cross table), typed forms of a time, subset sums of weights, the staircase ways and the logic-puzzle brute force.
Imported by p2/09/lesson.py and p2/10/lesson.py (after `from hlib import *` and `from p2lib import *`)."""
import itertools, math, re
from collections import deque
from hlib import svg as _svg, T, Ln, Ci, Re, NAVY, YEL, TEAL, WARM, PALE

SKY = '#DDEBF7'


# ---------------------------------------------------------------- jug puzzles
def jug_next(st, caps):
    """Every step from state st = (litres in jug 0, litres in jug 1): fill a jug, empty a jug, or pour one into the other until one is full or the other is empty.
    A step that changes nothing is not a step."""
    out = {}
    for i in (0, 1):
        j = 1 - i
        s = list(st); s[i] = caps[i]
        out[('fill', i)] = tuple(s)
        s = list(st); s[i] = 0
        out[('empty', i)] = tuple(s)
        amt = min(st[i], caps[j] - st[j])
        s = list(st); s[i] -= amt; s[j] += amt
        out[('pour', i, j)] = tuple(s)
    return {k: v for k, v in out.items() if v != st}


def jug_run(caps, moves, start=(0, 0)):
    """The states after every move of a list of moves (each must be a real step)."""
    st, seen = tuple(start), [tuple(start)]
    for mv in moves:
        nxt = jug_next(st, caps)
        if mv not in nxt:
            raise ValueError(f'not a real step: {mv} from {st}')
        st = nxt[mv]
        seen.append(st)
    return seen


def jug_fewest(caps, target, start=(0, 0), which=None):
    """(fewest steps, one shortest list of moves) to get `target` litres in a jug (jug `which`, or either jug when None), by breadth-first search over every state."""
    start = tuple(start)
    ok = (lambda s: s[which] == target) if which is not None else (lambda s: target in s)
    prev, dq = {start: None}, deque([start])
    while dq:
        s = dq.popleft()
        if ok(s):
            path = []
            while prev[s] is not None:
                s, mv = prev[s]
                path.append(mv)
            return len(path), list(reversed(path))
        for mv, n in jug_next(s, caps).items():
            if n not in prev:
                prev[n] = (s, mv)
                dq.append(n)
    return None, None


def jug_text(caps, moves, start=(0, 0)):
    """One sentence per move with the litres in each jug afterwards, written from the simulation (so it cannot be wrong)."""
    nm = [f'{c} ℓ jug' for c in caps]
    sts = jug_run(caps, moves, start)
    out = []
    for k, mv in enumerate(moves):
        a, b = sts[k + 1]
        if mv[0] == 'fill':
            s = f'Fill the {nm[mv[1]]}'
        elif mv[0] == 'empty':
            s = f'Empty the {nm[mv[1]]}'
        else:
            i, j = mv[1], mv[2]
            s = f'Pour the {nm[i]} into the {nm[j]} until ' + (f'the {nm[j]} is full' if sts[k + 1][j] == caps[j] else f'the {nm[i]} is empty')
        out.append(f'{k + 1}. {s}: {a} ℓ in the {nm[0]}, {b} ℓ in the {nm[1]}.')
    return out


def jugs_fig(a, b, caption=''):
    """Two jugs with no marks, drawn to scale by their size (a litres and b litres), big enough for a phone."""
    def dims(l):
        return 44 + l * 7, 26 + l * 11                         # width, height
    (w1, h1), (w2, h2) = dims(a), dims(b)
    base = 8 + max(h1, h2) + 14
    def jug(x, litres, w, h):
        y = base - h
        s = Re(x, y, w, h, SKY, NAVY, 3)
        s += f'<path d="M{x + w:g} {y + 10:g} q16 4 16 {h / 3:g} q0 {h / 4:g} -16 {h / 3:g}" fill="none" stroke="{NAVY}" stroke-width="3"/>'
        s += Ln(x, y, x - 9, y - 7, 3)
        s += T(x + w / 2, y + h / 2 + 7, f'{litres} ℓ', 22, 'middle', 800)
        return s
    x1 = 30
    x2 = x1 + w1 + 16 + 46
    W = x2 + w2 + 16 + 30
    body = jug(x1, a, w1, h1) + jug(x2, b, w2, h2) + T(W / 2, base + 26, 'No marks on the jugs!', 15, 'middle', 700, TEAL)
    return _svg(W, base + 36, body, caption or f'A {a} litre jug and a {b} litre jug with no marks on them')


# ---------------------------------------------------------------- reading the printed figures back
def read_clocks(fig):
    """[(hour, minute), ...] read from the angles of the hands of the printed clocks: the thick navy line is the hour hand, the thin red line is the minute hand."""
    hs = re.findall(r'<line x1="([\d.]+)" y1="([\d.]+)" x2="([\d.]+)" y2="([\d.]+)" stroke="#1B2A49" stroke-width="7"', fig)
    ms = re.findall(r'<line x1="([\d.]+)" y1="([\d.]+)" x2="([\d.]+)" y2="([\d.]+)" stroke="#D64545" stroke-width="3"', fig)
    out = []
    for (hx1, hy1, hx2, hy2), (mx1, my1, mx2, my2) in zip(hs, ms):
        ang = lambda x1, y1, x2, y2: (math.degrees(math.atan2(float(x2) - float(x1), -(float(y2) - float(y1)))) + 360) % 360
        minute = round(ang(mx1, my1, mx2, my2) / 6) % 60
        past12 = ang(hx1, hy1, hx2, hy2) * 2                      # the hour hand moves 0.5 degree a minute: minutes past 12 o'clock
        hour = round((past12 - minute) / 60) % 12 or 12
        if abs(((hour % 12) * 60 + minute) - past12) > 4 and abs(((hour % 12) * 60 + minute) - past12 + 720) > 4 and abs(((hour % 12) * 60 + minute) - past12 - 720) > 4:
            raise ValueError('the hour hand and the minute hand do not agree')
        out.append((hour, minute))
    return out


def clock_captions(fig):
    return re.findall(r'<text[^>]*>(Ali is [^<]*)</text>', fig)


def graph_counts(fig):
    """Pictures (red scoops) in each row of the printed picture graph, read from the figure; the key picture under the graph is not a row."""
    rows = {}
    for cy in re.findall(r'<circle cx="[\d.]+" cy="([\d.]+)" r="10" fill="#D64545"', fig):
        r = int((float(cy) - 4) // 37)
        rows[r] = rows.get(r, 0) + 1
    return [rows.get(r, 0) for r in range(4)]


def graph_blank(fig):
    """The printed picture graph without the paper words 'Draw the pictures for Thursday here.' (the row is left empty)."""
    return re.sub(r'<text[^>]*>Draw the pictures for Thursday here\.</text>', '', fig)


def graph_solved(fig, n):
    """The graph with the Thursday row filled with n pictures (cones drawn the same way as the printed ones)."""
    y = 4 + 3 * 37
    cones = ''
    for j in range(n):
        x = 130 + j * 36
        cones += (f'<polygon points="{x + 4},{y + 13} {x + 24},{y + 13} {x + 14},{y + 35}" fill="{YEL}" stroke="{NAVY}" stroke-width="2"/>'
                  f'<circle cx="{x + 14}" cy="{y + 10}" r="10" fill="#D64545" stroke="{NAVY}" stroke-width="2"/>')
    g = graph_blank(fig)
    return g.replace('</svg>', cones + '</svg>')


def tower_counts(fig):
    """Cubes in each printed tower, counted from the figure (the cubes at the same x are one tower), left to right."""
    cols = {}
    for x in re.findall(r'<rect x="([\d.]+)" y="[\d.]+" width="36" height="18"', fig):
        cols[float(x)] = cols.get(float(x), 0) + 1
    return [cols[k] for k in sorted(cols)]


def cake_pieces(fig):
    """Pieces of the printed cake strip: the dividing lines plus one."""
    return len(re.findall(r'<line ', fig)) + 1


# ---------------------------------------------------------------- times
def minutes_of(h, m, suffix=None):
    """Minutes since midnight of h:m am / pm (12 am = 0, 12 pm = 12 o'clock noon)."""
    if suffix is None:
        return h * 60 + m
    return (h % 12 + (12 if suffix == 'pm' else 0)) * 60 + m


def clock_text(t):
    """(h, m, 'am' or 'pm') of minutes since midnight."""
    t %= 1440
    h, m = divmod(t, 60)
    return (h % 12 or 12), m, ('am' if h < 12 else 'pm')


def time_forms(h, m, suffix, bare_ok=False):
    """The ways a child may type a time: 7:25 am, 7:25am, 7.25 am, 7:25 a.m. (case is ignored by the marker); with bare_ok also 7:25 and 7.25."""
    base = f'{h}:{m:02d}'
    out = [f'{base} {suffix}', f'{base}{suffix}', f'{h}.{m:02d} {suffix}', f'{h}.{m:02d}{suffix}', f'{base} {suffix[0]}.m.', f'{base}{suffix[0]}.m.', f'{h}.{m:02d} {suffix[0]}.m.']
    if bare_ok:
        out += [base, f'{h}.{m:02d}']
    seen, res = set(), []
    for x in out:
        if x not in seen:
            seen.add(x); res.append(x)
    return res


# ---------------------------------------------------------------- weights (lesson 9 investigation)
def masses(ws):
    """Every mass that can be made by putting some (at least one) of the weights on one pan."""
    out = set()
    for r in range(1, len(ws) + 1):
        for c in itertools.combinations(ws, r):
            out.add(sum(c))
    return out


def good_weight_sets(lo=1, hi=5, k=3, need=6):
    """Every set of k different weights from lo to hi that can make EVERY mass from 1 to need, each set smallest first, in counting order."""
    return [c for c in itertools.combinations(range(lo, hi + 1), k) if set(range(1, need + 1)) <= masses(c)]


# ---------------------------------------------------------------- staircase (lesson 10 investigation)
def stair_ways(n):
    """Every way to climb n steps taking 1 or 2 at a time, as tuples, in counting order (1s first)."""
    out = []
    def go(left, so_far):
        if left == 0:
            out.append(tuple(so_far)); return
        for s in (1, 2):
            if s <= left:
                go(left - s, so_far + [s])
    go(n, [])
    return out


def ways_text(ways):
    return ', '.join('+'.join(str(s) for s in w) for w in ways)


# ---------------------------------------------------------------- logic puzzles (brute force over every arrangement)
def assignments(people, things, ok):
    """Every way to give each person a different thing so that ok(dict) is true."""
    return [dict(zip(people, p)) for p in itertools.permutations(things) if ok(dict(zip(people, p)))]


# ---------------------------------------------------------------- figures drawn for a phone
def clue_fig(lines, cols=None, rows=None, caption='', W=340):
    """A card of clue sentences and, when cols and rows are given, an empty tick-and-cross table (the printed workbook page has both)."""
    lh = 26
    b = Re(2, 2, W - 4, 12 + len(lines) * lh + 4, '#fff', NAVY, 2.2, 8)
    for i, s in enumerate(lines):
        b += T(14, 28 + i * lh, s, 16, 'start', 700)
    y = 12 + len(lines) * lh + 18
    if cols:
        lw = 62
        cw = (W - 8 - lw) / len(cols)
        rh = 36
        b += Re(4, y, lw, rh, '#D9D9D9', NAVY, 2.2)
        for k, c in enumerate(cols):
            b += Re(4 + lw + k * cw, y, cw, rh, '#D9D9D9', NAVY, 2.2) + T(4 + lw + k * cw + cw / 2, y + 24, c, 15, 'middle', 800)
        for r, name in enumerate(rows):
            yy = y + (r + 1) * rh
            b += Re(4, yy, lw, rh, '#D9D9D9', NAVY, 2.2) + T(4 + lw / 2, yy + 24, name, 15, 'middle', 800)
            for k in range(len(cols)):
                b += Re(4 + lw + k * cw, yy, cw, rh, '#fff', NAVY, 2.2)
        y += (len(rows) + 1) * rh
    return _svg(W, y + 8, b, caption or ' '.join(lines))


# ---------------------------------------------------------------- balance scales and clocks redrawn for a phone (the printed ones are too small and their labels collide at 390 px)
APPLE, LEMON, MELON, CUBE_C, BALL_C = '#F5B7A8', '#FFC93C', '#CFEAD8', '#DDEBF7', '#F5B7A8'


def _icon(kind, x, base):
    """One thing sitting on a pan with its bottom at y = base; returns (svg, width)."""
    if kind == 'apple':
        return (f'<circle cx="{x + 11}" cy="{base - 11}" r="11" fill="{APPLE}" stroke="{NAVY}" stroke-width="2.2"/><line x1="{x + 11}" y1="{base - 22}" x2="{x + 14}" y2="{base - 28}" stroke="{NAVY}" stroke-width="2.2"/>', 22)
    if kind == 'lemon':
        return (f'<ellipse cx="{x + 10}" cy="{base - 8}" rx="10" ry="8" fill="{LEMON}" stroke="{NAVY}" stroke-width="2.2"/>', 20)
    if kind in ('melon', 'pomelo'):
        return (f'<ellipse cx="{x + 17}" cy="{base - 14}" rx="17" ry="14" fill="{MELON}" stroke="{NAVY}" stroke-width="2.2"/><path d="M{x + 8} {base - 20} Q{x + 17} {base - 14} {x + 8} {base - 8}" fill="none" stroke="{NAVY}" stroke-width="1.8"/>', 34)
    if kind == 'cube':
        return (f'<rect x="{x}" y="{base - 22}" width="22" height="22" fill="{CUBE_C}" stroke="{NAVY}" stroke-width="2.2"/>', 22)
    if kind == 'ball':
        return (f'<circle cx="{x + 11}" cy="{base - 11}" r="11" fill="{BALL_C}" stroke="{NAVY}" stroke-width="2.2"/><path d="M{x + 1} {base - 11} Q{x + 11} {base - 6} {x + 21} {base - 11}" fill="none" stroke="{NAVY}" stroke-width="1.6"/>', 22)
    if kind.startswith('w'):                                   # a weight: w100, w300, w500
        g = kind[1:]
        return (f'<path d="M{x} {base} L{x + 3} {base - 22} L{x + 41} {base - 22} L{x + 44} {base} Z" fill="#fff" stroke="{NAVY}" stroke-width="2"/>' + T(x + 22, base - 6, f'{g} g', 13, 'middle', 800), 44)
    raise ValueError(kind)


def _pan(cx, py, things, pw=112):
    rows, cur, curw = [], [], 0
    for k in things:
        w = _icon(k, 0, 0)[1]
        if cur and curw + w + 4 > pw - 10:
            rows.append(cur); cur, curw = [], 0
        cur.append(k); curw += w + 4
    rows.append(cur)
    out = ''
    for r, row in enumerate(rows):
        tw = sum(_icon(k, 0, 0)[1] + 4 for k in row) - 4
        x = cx - tw / 2
        for k in row:
            g, w = _icon(k, x, py - r * 30)
            out += g; x += w + 4
    return out + f'<path d="M{cx - pw / 2} {py} L{cx + pw / 2} {py} L{cx + pw / 2 - 10} {py + 9} L{cx - pw / 2 + 10} {py + 9} Z" fill="{SKY}" stroke="{NAVY}" stroke-width="2.4"/>'


def scales_fig(scales, caption=''):
    """Level balance scales one under the other. scales = [(title, left things, left label, right things, right label)], things are 'apple', 'lemon', 'melon', 'pomelo', 'cube', 'ball', 'w100'.
    The labels say what is on each pan, the same words as the question."""
    W, bh = 340, 138
    arm, pw = 84, 112
    body = ''
    for n, (title, left, ll, right, rl) in enumerate(scales):
        top = 4 + n * bh
        cx, by, py = W / 2, top + 28, top + 94
        lx, rx = cx - arm, cx + arm
        body += T(cx, top + 14, title, 16, 'middle', 800, TEAL)
        body += Ln(lx, by, rx, by, 5)
        for px in (lx, rx):
            body += Ln(px, by, px - pw / 2, py, 1.8) + Ln(px, by, px + pw / 2, py, 1.8)
        body += Ln(cx, by, cx, py + 10, 6) + Re(cx - 20, py + 10, 40, 7, NAVY, NAVY, 2, 3)
        body += f'<polygon points="{cx},{by - 6} {cx - 7},{by + 5} {cx + 7},{by + 5}" fill="{YEL}" stroke="{NAVY}" stroke-width="2"/>'
        body += _pan(lx, py, left, pw) + _pan(rx, py, right, pw)
        body += T(lx, py + 36, ll, 14, 'middle', 800) + T(rx, py + 36, rl, 14, 'middle', 800)
    cap = caption or 'Level scales: ' + '; '.join(f'{t}: {l} balances {r}' for t, _, l, _, r in scales)
    return _svg(W, 8 + len(scales) * bh, body, cap)


def clock_face(cx, cy, h, m, R=56):
    """A clock face with minute marks, numerals outside the ring, a short thick navy hour hand and a long thin red minute hand."""
    s = Ci(cx, cy, R, '#fff', NAVY, 3.5)
    for i in range(60):
        a = i * math.pi / 30
        r1 = R - (11 if i % 5 == 0 else 6)
        s += Ln(f'{cx + r1 * math.sin(a):.1f}', f'{cy - r1 * math.cos(a):.1f}', f'{cx + (R - 2) * math.sin(a):.1f}', f'{cy - (R - 2) * math.cos(a):.1f}', 2.2 if i % 5 == 0 else 1)
    for n in range(1, 13):
        a = n * math.pi / 6
        s += T(f'{cx + (R + 13) * math.sin(a):.1f}', f'{cy - (R + 13) * math.cos(a) + 5:.1f}', n, 14, 'middle', 800)
    ha, ma = ((h % 12) * 30 + m * 0.5) * math.pi / 180, m * 6 * math.pi / 180
    s += (f'<line x1="{cx}" y1="{cy}" x2="{cx + R * 0.45 * math.sin(ha):.1f}" y2="{cy - R * 0.45 * math.cos(ha):.1f}" stroke="#1B2A49" stroke-width="7" stroke-linecap="round"/>'
          f'<line x1="{cx}" y1="{cy}" x2="{cx + (R - 4) * math.sin(ma):.1f}" y2="{cy - (R - 4) * math.cos(ma):.1f}" stroke="#D64545" stroke-width="3" stroke-linecap="round"/>')
    return s + Ci(cx, cy, 5, NAVY, NAVY, 1)


def clocks_fig(times, captions, caption=''):
    """Two clocks side by side with a letter above each and a two-line caption below; times = [(h, m), ...]."""
    W = 340
    body = ''
    for k, ((h, m), (c1, c2)) in enumerate(zip(times, captions)):
        cx = 85 + k * 170
        body += T(cx - 52, 24, 'AB'[k], 26, 'middle', 800, TEAL) + clock_face(cx, 110, h, m) + T(cx, 206, c1, 14, 'middle', 800) + T(cx, 224, c2, 14, 'middle', 800)
    body += T(W / 2, 252, 'short thick hand = hour', 14, 'middle', 700, TEAL) + T(W / 2, 270, 'long thin hand = minute', 14, 'middle', 700, TEAL)
    return _svg(W, 280, body, caption or 'Two clocks')


def time_line_fig(stops, hops, caption=''):
    """A time line on a phone: stops = [(x, 'label')] left to right, hops = [(i, j, 'text')] arcs over the line from stop i to stop j."""
    W = 340
    y = 62
    b = Ln(10, y, W - 12, y, 3) + f'<polygon points="{W - 6},{y} {W - 18},{y - 6} {W - 18},{y + 6}" fill="{NAVY}"/>'
    for x, lab in stops:
        b += Ln(x, y - 9, x, y + 9, 3) + T(x, y + 28, lab, 14, 'middle', 800)
    for i, j, tx in hops:
        x1, x2 = stops[i][0], stops[j][0]
        b += f'<path d="M{x1} {y - 11} Q{(x1 + x2) / 2:g} {y - 46} {x2} {y - 11}" fill="none" stroke="{NAVY}" stroke-width="2.4"/>' + T((x1 + x2) / 2, y - 38, tx, 14, 'middle', 800, TEAL)
    return _svg(W, y + 40, b, caption or 'A time line')


def ribbon_fig(red, diff, ov, W=340):
    """A red ribbon and a shorter blue ribbon glued end to end with an overlap, drawn to scale; the length of the blue ribbon and of the new ribbon are NOT written."""
    blue = red - diff
    total = red + blue - ov
    sc = (W - 24) / total
    x0 = 12
    rx2 = x0 + red * sc
    bx1 = x0 + (red - ov) * sc
    bx2 = bx1 + blue * sc
    b = Re(x0, 34, red * sc, 26, '#D64545', NAVY, 2.4, 5) + T(x0 + (red * sc - ov * sc) / 2, 52, f'red: {red} cm', 15, 'middle', 800, '#fff')
    b += Re(bx1, 54, blue * sc, 26, SKY, NAVY, 2.4, 5) + T(bx1 + ov * sc + (blue * sc - ov * sc) / 2, 72, 'blue', 15, 'middle', 800)
    b += Re(bx1, 54, ov * sc, 6, YEL, NAVY, 1.5)
    b += Ln((bx1 + rx2) / 2, 30, (bx1 + rx2) / 2, 24, 2) + T((bx1 + rx2) / 2, 18, f'overlap {ov} cm', 14, 'middle', 700, TEAL)
    yl = 100
    b += Ln(x0, yl, bx2, yl, 2) + Ln(x0, yl - 7, x0, yl + 7, 2) + Ln(bx2, yl - 7, bx2, yl + 7, 2) + T((x0 + bx2) / 2, yl + 24, 'new ribbon: ? cm', 15, 'middle', 800)
    return _svg(W, 132, b, f'A red ribbon {red} centimetres long and a blue ribbon glued end to end, overlapping by {ov} centimetres; the new ribbon is how long?')


# ---------------------------------------------------------------- lesson 10: picture graph and towers redrawn for a phone, read back from the new drawing
GRAPH_RH = 36


def _scoop(x, y):
    """An ice-cream (cone and scoop), top-left at (x, y), 20 wide."""
    return (f'<polygon points="{x + 2},{y + 14} {x + 18},{y + 14} {x + 10},{y + 32}" fill="{YEL}" stroke="{NAVY}" stroke-width="2"/>'
            f'<circle class="scoop" cx="{x + 10}" cy="{y + 10}" r="9" fill="#D64545" stroke="{NAVY}" stroke-width="2"/>')


def picture_graph_fig(rows, key, caption=''):
    """rows = [(label, pictures or None)]; None = an empty row; key = number each picture stands for.  Drawn for a phone."""
    W, lw = 340, 104
    b = ''
    for i, (lab, k) in enumerate(rows):
        y = 4 + i * GRAPH_RH
        b += f'<rect x="4" y="{y}" width="{W - 8}" height="{GRAPH_RH}" fill="{"#fff" if i % 2 else SKY}"/>' + T(12, y + 24, lab, 15, 'start', 800)
        for j in range(k or 0):
            b += _scoop(lw + 8 + j * 25, y + 2)
    n = len(rows)
    b += Re(4, 4, W - 8, n * GRAPH_RH, 'none', NAVY, 2.2) + Ln(lw, 4, lw, 4 + n * GRAPH_RH, 2.2)
    ky = 4 + n * GRAPH_RH + 10
    b += _scoop(lw + 8, ky) + T(lw + 36, ky + 24, f'= {key} ice-creams', 15, 'start', 800)
    cap = caption or 'Picture graph of ice-creams sold. ' + ', '.join(f'{l}: {k if k is not None else "blank"}' for l, k in rows) + f'. Each picture stands for {key} ice-creams.'
    return _svg(W, ky + 42, b, cap)


def picture_graph_counts(fig):
    """Pictures in each row, counted from the drawing (the scoops are circles; the key picture is below the rows)."""
    rows = {}
    for cy in re.findall(r'<circle class="scoop" cx="[\d.]+" cy="([\d.]+)"', fig):
        r = int((float(cy) - 4) // GRAPH_RH)
        rows[r] = rows.get(r, 0) + 1
    n = max(rows) + 1 if rows else 0
    return [rows.get(r, 0) for r in range(n)]


def towers_fig(counts, caption=''):
    """Towers of cubes side by side, drawn to scale on a phone (cube 30 wide, 13 high); counts = cubes in each tower."""
    cw, ch = 30, 13
    hmax = max(counts)
    base = 8 + hmax * ch
    W = 340
    gap = (W - 20) / len(counts)
    b = ''
    for t, n in enumerate(counts):
        x = 10 + t * gap + (gap - cw) / 2
        for i in range(n):
            b += f'<rect class="cube" x="{x:g}" y="{base - (i + 1) * ch}" width="{cw}" height="{ch}" fill="{YEL}" stroke="{NAVY}" stroke-width="2"/>'
        b += T(x + cw / 2, base + 22, f'Tower {t + 1}', 15, 'middle', 800)
    return _svg(W, base + 32, b, caption or 'Towers of cubes: ' + ', '.join(f'Tower {t + 1} has {n} cubes' for t, n in enumerate(counts)))


def towers_read(fig):
    cols = {}
    for x in re.findall(r'<rect class="cube" x="([\d.]+)"', fig):
        cols[float(x)] = cols.get(float(x), 0) + 1
    return [cols[k] for k in sorted(cols)]


def jug_table_fig(rows, caption=''):
    """The printed jug table: Step | What I do | 3 l jug | 5 l jug. rows = [(step, text, litres_a, litres_b)]; '' = an empty box to fill on paper."""
    cols = [40, 186, 56, 56]
    W = sum(cols) + 8
    rh = 32
    b = ''
    heads = ['Step', 'What I do', '3 ℓ jug', '5 ℓ jug']
    x = 4
    for c, h in zip(cols, heads):
        b += Re(x, 4, c, rh, '#D9D9D9', NAVY, 2.2) + T(x + c / 2, 4 + 22, h, 13 if c < 60 else 15, 'middle', 800)
        x += c
    for r, row in enumerate(rows):
        y = 4 + (r + 1) * rh
        x = 4
        for k, (c, v) in enumerate(zip(cols, row)):
            fill = '#fff' if v == '' else '#DDEBF7'
            b += Re(x, y, c, rh, fill, NAVY, 2.2)
            if v != '':
                b += T(x + 8, y + 22, v, 14, 'start', 700) if k == 1 else T(x + c / 2, y + 22, v, 14, 'middle', 700)
            x += c
    return _svg(W, 8 + (len(rows) + 1) * rh, b, caption or 'The jug table: steps 1 to 3 done, rows 4 to 7 empty')
