"""Level 1 (Primary 1, ages 6-8) helpers for the online holiday practice, weeks 2 onward: small drawn pictures (fruit, animals, shapes, counters, stars),
picture graphs, pattern rows and stick figures that the printed workbook draws, redrawn as plain SVG at a size that is readable on a 390 px phone.
No coin or note pictures.

Lesson files import this as  `from p1lib import *`  after putting this folder on sys.path.  Needs practice/holiday/hlib.py (shared, not edited here).
"""
import itertools, math, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from hlib import *      # noqa: E402,F401  (svg, T, Ln, Ci, Re, NAVY, YEL, TEAL, WARM, PALE ...)

_uid = itertools.count(1)


# ---------------------------------------------------------------- tiny pictures (each is drawn inside about s x s, centred on cx, cy)
def apple(cx, cy, s):
    r = s * 0.40
    return (Ci(cx, cy + 1, r, '#F28B82', NAVY, 1.8) + Ln(cx, cy + 1 - r, cx + 2, cy - r - 4, 1.8) +
            f'<ellipse cx="{cx + 6}" cy="{cy - r - 1}" rx="5" ry="2.6" fill="#7FC77F" stroke="{NAVY}" stroke-width="1.2" transform="rotate(-25 {cx + 6} {cy - r - 1})"/>')


def banana(cx, cy, s):
    a = s * 0.46
    return (f'<path d="M{cx - a} {cy - a * 0.5} Q{cx - a * 0.1} {cy + a * 0.95} {cx + a} {cy - a * 0.75} Q{cx + a * 0.15} {cy + a * 0.25} {cx - a} {cy - a * 0.5} Z" '
            f'fill="#FFE066" stroke="{NAVY}" stroke-width="1.8" stroke-linejoin="round"/>')


def orange(cx, cy, s):
    r = s * 0.40
    return Ci(cx, cy, r, '#FFB347', NAVY, 1.8) + ''.join(Ci(cx + dx * r, cy + dy * r, 1.4, '#C9741A', '#C9741A', 1) for dx, dy in ((-.3, -.2), (.25, -.3), (0, .25), (.4, .15), (-.35, .3)))


def grape(cx, cy, s):
    r = s * 0.13
    out = Ln(cx, cy - s * 0.42, cx, cy - s * 0.22, 1.6, '#6B8E23')
    for k, (dx, dy) in enumerate(((-1.6, -0.9), (0, -0.9), (1.6, -0.9), (-0.8, 0.5), (0.8, 0.5), (0, 1.9))):
        out += Ci(cx + dx * r * 1.15, cy + dy * r * 1.15 + 1, r, '#9B7FD1', NAVY, 1.2)
    return out


def melon(cx, cy, s):
    r = s * 0.46
    y = cy - r * 0.35
    return (f'<path d="M{cx - r} {y} A{r} {r} 0 0 0 {cx + r} {y} Z" fill="#F26B6B" stroke="{NAVY}" stroke-width="1.8"/>'
            f'<path d="M{cx - r + 3} {y + 2} A{r - 3} {r - 3} 0 0 0 {cx + r - 3} {y + 2}" fill="none" stroke="#5DB85D" stroke-width="3"/>'
            + ''.join(f'<ellipse cx="{cx + dx}" cy="{y + dy}" rx="1.3" ry="2" fill="{NAVY}"/>' for dx, dy in ((-6, 5), (0, 8), (6, 5))))


def star(cx, cy, s, half=False):
    R, r = s * 0.5, s * 0.21
    pts = []
    for k in range(10):
        ang = -math.pi / 2 + k * math.pi / 5
        rad = R if k % 2 == 0 else r
        pts.append((cx + rad * math.cos(ang), cy + rad * math.sin(ang)))
    poly = ' '.join(f'{x:.1f},{y:.1f}' for x, y in pts)
    if not half:
        return f'<polygon points="{poly}" fill="{YEL}" stroke="{NAVY}" stroke-width="1.8" stroke-linejoin="round"/>'
    cid = f'hs{next(_uid)}'
    return (f'<clipPath id="{cid}"><rect x="{cx - R - 2}" y="{cy - R - 2}" width="{R + 2}" height="{2 * R + 4}"/></clipPath>'
            f'<polygon points="{poly}" fill="#fff" stroke="{NAVY}" stroke-width="1.4" stroke-dasharray="3 2" stroke-linejoin="round"/>'
            f'<polygon points="{poly}" fill="{YEL}" stroke="{NAVY}" stroke-width="1.8" stroke-linejoin="round" clip-path="url(#{cid})"/>')


def cat_face(cx, cy, s):
    r = s * 0.36
    return (f'<polygon points="{cx - r},{cy - r * 0.3} {cx - r * 0.95},{cy - r * 1.25} {cx - r * 0.2},{cy - r * 0.8}" fill="#F4B183" stroke="{NAVY}" stroke-width="1.6" stroke-linejoin="round"/>'
            f'<polygon points="{cx + r},{cy - r * 0.3} {cx + r * 0.95},{cy - r * 1.25} {cx + r * 0.2},{cy - r * 0.8}" fill="#F4B183" stroke="{NAVY}" stroke-width="1.6" stroke-linejoin="round"/>'
            + Ci(cx, cy + 1, r, '#F4B183', NAVY, 1.8) + Ci(cx - r * 0.38, cy - 1, 1.8, NAVY, NAVY, 1) + Ci(cx + r * 0.38, cy - 1, 1.8, NAVY, NAVY, 1)
            + f'<polygon points="{cx - 2},{cy + 4} {cx + 2},{cy + 4} {cx},{cy + 7}" fill="{WARM}"/>')


def dog_face(cx, cy, s):
    r = s * 0.34
    return (f'<ellipse cx="{cx - r * 1.0}" cy="{cy + 1}" rx="{r * 0.36}" ry="{r * 0.85}" fill="#A9795A" stroke="{NAVY}" stroke-width="1.6"/>'
            f'<ellipse cx="{cx + r * 1.0}" cy="{cy + 1}" rx="{r * 0.36}" ry="{r * 0.85}" fill="#A9795A" stroke="{NAVY}" stroke-width="1.6"/>'
            + Ci(cx, cy + 1, r, '#E8CBA7', NAVY, 1.8) + Ci(cx - r * 0.36, cy - 2, 1.8, NAVY, NAVY, 1) + Ci(cx + r * 0.36, cy - 2, 1.8, NAVY, NAVY, 1)
            + Ci(cx, cy + 2, 2, NAVY, NAVY, 1)
            + f'<path d="M {cx - 3.2} {cy + 4.6} Q {cx} {cy + 8} {cx + 3.2} {cy + 4.6}" fill="none" stroke="{NAVY}" stroke-width="1.5" stroke-linecap="round"/>')


def fish(cx, cy, s):
    w = s * 0.34
    return (f'<polygon points="{cx + w * 0.8},{cy} {cx + w * 1.45},{cy - w * 0.6} {cx + w * 1.45},{cy + w * 0.6}" fill="#6FB7E9" stroke="{NAVY}" stroke-width="1.6" stroke-linejoin="round"/>'
            f'<ellipse cx="{cx - w * 0.15}" cy="{cy}" rx="{w}" ry="{w * 0.65}" fill="#6FB7E9" stroke="{NAVY}" stroke-width="1.8"/>' + Ci(cx - w * 0.6, cy - 1, 1.6, NAVY, NAVY, 1))


def shape(name, cx, cy, s):
    """circle, triangle, square, star as pattern shapes."""
    h = s * 0.42
    if name == 'circle':
        return Ci(cx, cy, h, '#BFE3E0', NAVY, 2.2)
    if name == 'triangle':
        return f'<polygon points="{cx},{cy - h} {cx + h * 1.1},{cy + h * 0.85} {cx - h * 1.1},{cy + h * 0.85}" fill="{YEL}" stroke="{NAVY}" stroke-width="2.2" stroke-linejoin="round"/>'
    if name == 'square':
        return Re(cx - h * 0.9, cy - h * 0.9, h * 1.8, h * 1.8, '#F6B8A4', NAVY, 2.2, 2)
    if name == 'star':
        return star(cx, cy, s * 0.95)
    raise ValueError(name)


def counter(colour, cx, cy, s):
    fill, letter = {'red': ('#F4A6A0', 'R'), 'blue': ('#A8D0F0', 'B'), 'green': ('#A8DDA0', 'G')}[colour]
    return Ci(cx, cy, s * 0.4, fill, NAVY, 2.2) + T(cx, cy + 5, letter, 14, 'middle', 800)


def letter_tile(ch, cx, cy, s):
    h = s * 0.42
    return Re(cx - h, cy - h, 2 * h, 2 * h, '#FFE08A', NAVY, 2.2, 5) + T(cx, cy + 6, ch, 18, 'middle', 800)


def draw_item(name, cx, cy, s):
    if name.startswith('L:'):
        return letter_tile(name[2:], cx, cy, s)
    if name in ('red', 'blue', 'green'):
        return counter(name, cx, cy, s)
    if name == 'cat':
        return cat_face(cx, cy, s)
    if name == 'dog':
        return dog_face(cx, cy, s)
    return shape(name, cx, cy, s)


ICONS = dict(Apple=apple, Banana=banana, Orange=orange, Grape=grape, Watermelon=melon, Cats=cat_face, Dogs=dog_face, Fish=fish)


# ---------------------------------------------------------------- picture graph
def picture_graph(rows, key_text, icon_for, maxn, size=26, label_w=92, half_key=None, caption=''):
    """rows: list of (name, n) where n may end in .5 (a half picture).  One picture per unit; a table with a row per name; a key under it.
    icon_for(name) -> function(cx, cy, s) used for that row."""
    pitch = size + 4
    W = label_w + maxn * pitch + 10
    row_h = size + 8
    body = ''
    for k, (name, n) in enumerate(rows):
        y = 4 + k * row_h
        body += Re(2, y, W - 4, row_h, '#fff' if k % 2 else '#FAF6EA', NAVY, 1.6)
        body += T(10, y + row_h / 2 + 5, name, 15, 'start', 800)
        fn = icon_for(name)
        whole = int(n)
        for i in range(whole):
            body += fn(label_w + i * pitch + pitch / 2, y + row_h / 2, size)
        if n - whole >= 0.5:
            body += star(label_w + whole * pitch + pitch / 2, y + row_h / 2, size, half=True)
    ky = 4 + len(rows) * row_h + 8
    kh = size + 12 + ((size + 4) if half_key else 0)
    body += Re(2, ky, W - 4, kh, PALE, NAVY, 1.6, 6)
    body += T(12, ky + (size + 12) / 2 + 5, 'Key:', 15, 'start', 800)
    fn0 = icon_for(rows[0][0])
    kx, cy0 = 62, ky + (size + 12) / 2
    body += fn0(kx + size / 2, cy0, size) + T(kx + size + 8, cy0 + 5, '= ' + key_text, 15, 'start', 700)
    if half_key:
        cy1 = cy0 + size + 4
        body += star(kx + size / 2, cy1, size, half=True) + T(kx + size + 8, cy1 + 5, '= ' + half_key, 15, 'start', 700)
    H = ky + kh + 6
    return svg(W, H, body, caption or 'Picture graph')


def fruit_icon(name):
    return ICONS[name]


def star_icon(name):
    return star


# ---------------------------------------------------------------- pattern row (numbered places; '?' = an empty dashed box)
def pattern_row(items, size=30, pitch=40, per_row=9, caption=''):
    """items: names for draw_item, or '?' for an empty place. More than per_row places are wrapped into two rows (places stay numbered)."""
    n = len(items)
    rows = [items] if n <= per_row else None
    if rows is None:
        half = (n + 1) // 2
        rows = [items[:half], items[half:]]
    cols = max(len(r) for r in rows)
    W = cols * pitch + 12
    body, num = '', 1
    for k, r in enumerate(rows):
        y = 8 + k * (size + 48)
        for i, it in enumerate(r):
            cx = 6 + i * pitch + pitch / 2
            if it == '?':
                body += Re(cx - size * 0.45, y + size * 0.05, size * 0.9, size * 0.9, '#fff', NAVY, 2, 5, '4 3') + T(cx, y + size * 0.62, '?', 17, 'middle', 800, '#44506F')
            else:
                body += draw_item(it, cx, y + size / 2, size)
            body += T(cx, y + size + 22, num, 15, 'middle', 700, '#44506F')
            num += 1
    return svg(W, 8 + len(rows) * (size + 48) - 10, body, caption or 'A pattern with numbered places')


def repeat(core, n):
    """The first n items of a pattern that repeats `core`, built by going round the core one place at a time (no formula)."""
    out, i = [], 0
    while len(out) < n:
        out.append(core[i]); i += 1
        if i == len(core):
            i = 0
    return out


# ---------------------------------------------------------------- tally table (empty) for a vote
def tally_table(names, filled=None):
    """Empty table: Fruit | Tally | Total.  filled: dict name -> count draws tally marks and the total."""
    W, rh = 300, 34
    body = Re(2, 2, W - 4, rh, '#D9D9D9', NAVY, 1.6) + T(10, 2 + rh / 2 + 5, 'Fruit', 15, 'start', 800) + T(171, 2 + rh / 2 + 5, 'Tally', 15, 'middle', 800) + T(264, 2 + rh / 2 + 5, 'Total', 15, 'middle', 800)
    for k, nm in enumerate(names):
        y = 2 + rh * (k + 1)
        body += Re(2, y, W - 4, rh, '#fff', NAVY, 1.6) + T(10, y + rh / 2 + 5, nm, 15, 'start', 700)
        body += Ln(114, y, 114, y + rh, 1.6) + Ln(228, y, 228, y + rh, 1.6)
        if filled and nm in filled:
            c = filled[nm]
            x = 122
            for g in range(c // 5):
                for i in range(4):
                    body += Ln(x + i * 6, y + 7, x + i * 6, y + rh - 7, 2, NAVY)
                body += Ln(x - 3, y + rh - 9, x + 21, y + 9, 2, NAVY)
                x += 32
            for i in range(c % 5):
                body += Ln(x + i * 6, y + 7, x + i * 6, y + rh - 7, 2, NAVY)
            body += T(264, y + rh / 2 + 6, c, 17, 'middle', 800)
    return svg(W, 4 + rh * (len(names) + 1), body, 'A table with a row for each fruit and a tally column')


# ---------------------------------------------------------------- sticks
STICK = '#B8860B'


def _stick(x1, y1, x2, y2):
    return Ln(x1, y1, x2, y2, 6, STICK) + Ln(x1, y1, x2, y2, 2.2, NAVY)


def triangle_rows(counts=(1, 2, 3), s=44, caption=''):
    """Rows of n triangles in a line made of sticks (n triangles use 2n + 1 sticks): zigzag sticks along the top and bottom."""
    h = s * 0.87
    body, x = '', 16
    for n in counts:
        pts = [(x + i * s / 2, (8 + h) if i % 2 == 0 else 8) for i in range(n + 2)]
        for i in range(n + 1):
            body += _stick(*pts[i], *pts[i + 1])
        for i in range(n):
            body += _stick(*pts[i], *pts[i + 2])
        body += T(x + (n + 1) * s / 4, 8 + h + 26, f'{n} triangle' + ('s' if n > 1 else ''), 15, 'middle', 700)
        x += (n + 1) * s / 2 + 24
    return svg(x - 8, 8 + h + 36, body, caption or 'Rows of triangles made with sticks: 1, 2 and 3 triangles')


def square_rows(counts=(1, 2, 3), s=34, caption=''):
    """Rows of n squares in a line made of sticks (n squares use 3n + 1 sticks)."""
    body, x, y0 = '', 20, 10
    for n in counts:
        for i in range(n + 1):
            body += _stick(x + i * s, y0, x + i * s, y0 + s)
        for i in range(n):
            body += _stick(x + i * s, y0, x + (i + 1) * s, y0) + _stick(x + i * s, y0 + s, x + (i + 1) * s, y0 + s)
        body += T(x + n * s / 2, y0 + s + 24, f'{n} square' + ('s' if n > 1 else ''), 15, 'middle', 700)
        x += n * s + 26
    return svg(x - 10, y0 + s + 34, body, caption or 'Rows of squares made with sticks: 1, 2 and 3 squares')


def dot_triangles(k_max=5, d=17, caption=''):
    """Dots arranged in triangles with 1, 3, 6, 10, 15 ... dots."""
    body, x, tops = '', 10, []
    for k in range(1, k_max + 1):
        w = k * d
        n = 0
        for r in range(k):
            for c in range(r + 1):
                body += Ci(x + (k - 1 - r) * d / 2 + c * d + d / 2, 10 + r * d + d / 2, 5.5, NAVY, NAVY, 1)
                n += 1
        body += T(x + w / 2, 10 + k_max * d + 22, n, 16, 'middle', 700)
        x += w + 18
    return svg(x - 8, 10 + k_max * d + 32, body, caption or 'Dots in triangles: 1, 3, 6, 10 and 15')


# ================================================================ weeks 3 on (lessons 5 and 6): number machines, bars, queue, snail wall, ways tables
# No coin or note pictures anywhere: coins appear only as words and numbers.
def _arrow(x1, x2, y):
    return Ln(x1, y, x2 - 6, y, 2.4) + f'<polygon points="{x2},{y} {x2 - 9},{y - 5.5} {x2 - 9},{y + 5.5}" fill="{NAVY}"/>'


def machine(cells, caption=''):
    """A number machine strip, left to right. cells: list of (text, kind) with kind 'q' (the number to find, yellow), 'op' (a step, grey) or 'out' (the result, blue)."""
    w, h, gap = 58, 44, 24
    fill = dict(q=YEL, op='#EDEDED', out='#DDEBF7')
    body, x = '', 4
    for i, (t, k) in enumerate(cells):
        body += Re(x, 6, w, h, fill[k], NAVY, 2.4, 7) + T(x + w / 2, 6 + h / 2 + 8, t, 22, 'middle', 800)
        if i < len(cells) - 1:
            body += _arrow(x + w + 3, x + w + gap - 2, 6 + h / 2)
        x += w + gap
    return svg(x - gap + 4, h + 12, body, caption or 'A number machine: ' + ', '.join(t for t, _ in cells))


def in_out_table(ins, outs, caption=''):
    """IN and OUT rows; None is drawn as a yellow '?' box."""
    n = len(ins)
    lw, cw, rh = 66, 52, 40
    W = lw + n * cw + 4
    body = ''
    for r, (lab, vals) in enumerate((('IN', ins), ('OUT', outs))):
        y = 4 + r * rh
        body += Re(2, y, lw, rh, '#EDEDED', NAVY, 2, 0) + T(2 + lw / 2, y + rh / 2 + 7, lab, 20, 'middle', 800)
        for i, v in enumerate(vals):
            x = 2 + lw + i * cw
            body += Re(x, y, cw, rh, YEL if v is None else '#fff', NAVY, 2, 0) + T(x + cw / 2, y + rh / 2 + 7, '?' if v is None else v, 21, 'middle', 800)
    return svg(W, 2 * rh + 8, body, caption or 'A number machine table. IN: ' + ', '.join('?' if v is None else str(v) for v in ins) + '. OUT: ' + ', '.join('?' if v is None else str(v) for v in outs))


def queue_fig(n=20, mei=7, caption=''):
    """A queue of n children in two rows of n/2 circles, numbered from the front; one child is marked."""
    per = (n + 1) // 2
    pitch = 28
    W = per * pitch + 14
    body = T(6, 16, 'front of the queue', 14, 'start', 700, TEAL, True)
    for k in range(n):
        r, i = divmod(k, per)
        cx, cy = 7 + i * pitch + pitch / 2, 44 + r * 58
        is_mei = (k + 1 == mei)
        body += Ci(cx, cy, 11.5, YEL if is_mei else '#fff', NAVY, 2.2) + T(cx, cy + 27, k + 1, 13, 'middle', 700, '#44506F')
        if is_mei:
            body += T(cx, cy - 18, 'Mei', 14, 'middle', 800)
    return svg(W, 44 + 58 + 34, body, caption or f'A queue of {n} children numbered from the front. Mei is number {mei}')


def marble_bars(shaded=(('Ali', 8), ('Mei', 0), ('Ben', 0)), boxes=14, caption=''):
    """Bars of empty boxes, one per child; the shaded boxes are the marbles already shown."""
    bw = 16
    lw = 40
    W = lw + boxes * bw + 6
    body = ''
    for r, (nm, k) in enumerate(shaded):
        y = 4 + r * 30
        body += T(2, y + 18, nm, 15, 'start', 800)
        for i in range(boxes):
            body += Re(lw + i * bw, y + 2, bw, 22, '#D9D9D9' if i < k else '#fff', NAVY, 1.6)
    return svg(W, 4 + len(shaded) * 30 + 2, body, caption or 'Bars of boxes for Ali, Mei and Ben. Ali has 8 boxes shaded, one for each marble')


def snail_wall(height=9, up=3, back=1, caption=''):
    """A wall with a 0 to height cm scale and a snail at the bottom."""
    k = 22
    y0 = 20 + height * k
    body = Re(60, y0 - height * k, 52, height * k, '#F4F1E8', NAVY, 2.4)
    for v in range(height + 1):
        body += Ln(52, y0 - v * k, 112, y0 - v * k, 2 if v % 3 == 0 else 1.2) + T(44, y0 - v * k + 5, v, 14, 'end', 700)
    body += T(86, y0 - height * k - 8, 'top', 14, 'middle', 800, TEAL) + T(86, y0 + 20, 'bottom', 14, 'middle', 800, TEAL)
    body += f'<ellipse cx="152" cy="{y0 - 11}" rx="24" ry="13" fill="#9BD39B" stroke="{NAVY}" stroke-width="2.2"/>' + Ci(152, y0 - 13, 7, '#fff', NAVY, 2.2)
    body += Ln(172, y0 - 20, 182, y0 - 34, 2.2) + Ci(182, y0 - 36, 3, NAVY, NAVY, 1)
    body += T(130, y0 - 110, 'The snail starts at the bottom.', 14, 'start', 700) + T(130, y0 - 88, f'Each day: up {up} cm.', 14, 'start', 700) + T(130, y0 - 66, f'Each night: back {back} cm.', 14, 'start', 700)
    return svg(330, y0 + 30, body, caption or f'A wall {height} cm high with a scale from 0 to {height} and a snail at the bottom')


def ways_table(ways, coins, caption=''):
    """A table of ways to pay: one row per way, a column for each coin, the number of that coin (counts are written in the cells)."""
    nc = len(coins)
    wc, cw, rh = 44, (280 - 44) // nc, 30
    W = wc + nc * cw + 4
    body = Re(2, 2, W - 4, rh, '#D9D9D9', NAVY, 1.8) + T(2 + wc / 2, 2 + rh / 2 + 6, 'Way', 15, 'middle', 800)
    for j, c in enumerate(coins):
        body += T(2 + wc + j * cw + cw / 2, 2 + rh / 2 + 6, f'{c}¢', 16, 'middle', 800)
    for r, w in enumerate(ways):
        y = 2 + (r + 1) * rh
        body += Re(2, y, W - 4, rh, '#fff' if r % 2 else '#FAF6EA', NAVY, 1.4) + T(2 + wc / 2, y + rh / 2 + 6, chr(65 + r), 16, 'middle', 800)
        for j in range(nc):
            body += T(2 + wc + j * cw + cw / 2, y + rh / 2 + 6, w[j], 17, 'middle', 700)
    return svg(W, 2 + (len(ways) + 1) * rh + 4, body, caption or 'A table of ways to pay: ' + str(len(ways)) + ' ways, with the number of each coin')


# ================================================================ week 4 (lessons 7 and 8): shapes, segments, grids, Venn loops, pet grid, polyominoes
def Po(pts, fill='none', stroke=NAVY, sw=2.4):
    return f'<polygon points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in pts)}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round"/>'


def regular_pts(n, cx, cy, r, rot=-90):
    return [(cx + r * math.cos(math.radians(rot + 360 * k / n)), cy + r * math.sin(math.radians(rot + 360 * k / n))) for k in range(n)]


def picture_parts(parts, w, h, caption):
    """A flat picture drawn from parts: ('poly', pts, fill) | ('circle', cx, cy, r, fill) | ('line', x1, y1, x2, y2).  Coordinates are the drawing's own units."""
    body = ''
    for p in parts:
        if p[0] == 'poly':
            body += Po(p[1], p[2], NAVY, 4)
        elif p[0] == 'circle':
            body += Ci(p[1], p[2], p[3], p[4], NAVY, 4)
        else:
            body += Ln(p[1], p[2], p[3], p[4], 5)
    return svg(w, h, body, caption)


def shape_gallery(caption=''):
    """The six named shapes of the printed 'shapes6' picture: circle, triangle, square, pentagon, hexagon, octagon (two rows of three)."""
    names = ['circle', 'triangle', 'square', 'pentagon', 'hexagon', 'octagon']
    body = ''
    for k, nm in enumerate(names):
        cx, cy = 50 + (k % 3) * 100, 40 + (k // 3) * 96
        if nm == 'circle':
            body += Ci(cx, cy, 30, '#fff', NAVY, 2.6)
        elif nm == 'triangle':
            body += Po([(cx, cy - 32), (cx + 34, cy + 26), (cx - 34, cy + 26)], '#fff')
        elif nm == 'square':
            body += Po([(cx - 28, cy - 28), (cx + 28, cy - 28), (cx + 28, cy + 28), (cx - 28, cy + 28)], '#fff')
        else:
            body += Po(regular_pts({'pentagon': 5, 'hexagon': 6, 'octagon': 8}[nm], cx, cy, 32, -90 if nm != 'octagon' else -67.5), '#fff')
        body += T(cx, cy + 52, nm, 16, 'middle', 800)
    return svg(300, 200, body, caption or 'Six shapes: circle, triangle, square, pentagon, hexagon, octagon')


def seg_body(segs, ox, oy, scale, H, sw=3.4, c=NAVY):
    """Segments given in a y-up drawing grid, drawn at (ox, oy) with the given scale; H = the drawing height in the same units."""
    return ''.join(Ln(ox + a[0] * scale, oy + (H - a[1]) * scale, ox + b[0] * scale, oy + (H - b[1]) * scale, sw, c) for a, b in segs)


def seg_svg(segs, W, H, scale, caption, fills=()):
    """One drawing from segments (y up).  fills: polygons (list of points) shaded first."""
    body = ''.join(Po([(x * scale + 4, (H - y) * scale + 4) for x, y in f], '#FDF3D0', 'none', 0) for f in fills)
    body += seg_body(segs, 4, 4, scale, H)
    return svg(W * scale + 8, H * scale + 8, body, caption)


def tri_lines_fig(counts):
    """Three triangles with lines from the top corner to the bottom edge, as printed: counts = [(lines, triangles), ...] with the captions '1 line' and '3 triangles'."""
    body, x = '', 4
    pw = 96
    for lines, tris in counts:
        W, Hh = 12, 8
        apex = (W / 2, Hh)
        segs = [((0, 0), (W, 0)), ((0, 0), apex), ((W, 0), apex)] + [(apex, (W * i / (lines + 1), 0)) for i in range(1, lines + 1)]
        sc = (pw - 8) / W
        body += Po([(x, 6 + Hh * sc), (x + W * sc, 6 + Hh * sc), (x + W * sc / 2, 6)], '#FDF3D0', 'none', 0) + seg_body(segs, x, 6, sc, Hh, 3)
        body += T(x + (pw - 8) / 2, 82, f'{lines} line' + ('s' if lines > 1 else ''), 14, 'middle', 800) + T(x + (pw - 8) / 2, 100, f'{tris} triangles', 14, 'middle', 700, TEAL)
        x += pw + 6
    return svg(x - 2, 108, body, 'Triangles with lines drawn from the top corner to the bottom: ' + ', '.join(f'{a} line' + ('s' if a > 1 else '') + f' gives {b} triangles' for a, b in counts))


def tri_lines_plain(n, caption=''):
    """One big triangle with n lines from the top corner to the bottom edge (no counts written)."""
    W, Hh = 12, 8
    apex = (W / 2, Hh)
    segs = [((0, 0), (W, 0)), ((0, 0), apex), ((W, 0), apex)] + [(apex, (W * i / (n + 1), 0)) for i in range(1, n + 1)]
    return seg_svg(segs, W, Hh, 24, caption or f'A big triangle with {n} lines from the top corner to the bottom', fills=[[(0, 0), (W, 0), apex]])


def grid_fig(a, b, cell=44, caption=''):
    """A grid of a squares long and b squares high."""
    segs = [((0, y), (a, y)) for y in range(b + 1)] + [((x, 0), (x, b)) for x in range(a + 1)]
    return seg_svg(segs, a, b, cell, caption or f'A grid {a} squares long and {b} squares high')


def edges_fig(edges, W, H, cell, fills=(), caption=''):
    """Unit edges of a square drawing ((x1, y1), (x2, y2)), y up; fills: (x, y, w, h, colour) rectangles shaded first."""
    body = ''.join(Re(4 + x * cell, 4 + (H - y - h) * cell, w * cell, h * cell, col, 'none', 0) for x, y, w, h, col in fills)
    body += seg_body(sorted(edges), 4, 4, cell, H, 3.4)
    return svg(W * cell + 8, H * cell + 8, body, caption)


def venn(left, right, groups=None, caption=''):
    """Two overlapping loops in a box (empty), or with the numbers placed: groups = dict(left=[..], both=[..], right=[..], out=[..])."""
    body = Re(2, 2, 296, 198, '#fff', '#7F8AA3', 1.8)
    body += T(86, 24, left, 15, 'middle', 800) + T(216, 24, right, 15, 'middle', 800)
    body += f'<ellipse cx="112" cy="110" rx="90" ry="68" fill="none" stroke="{NAVY}" stroke-width="3"/><ellipse cx="188" cy="110" rx="90" ry="68" fill="none" stroke="{NAVY}" stroke-width="3"/>'
    if groups:
        def put(nums, cx, cy, per):
            out = ''
            rows = [nums[i:i + per] for i in range(0, len(nums), per)]
            y0 = cy - (len(rows) - 1) * 10
            for r, row in enumerate(rows):
                out += T(cx, y0 + r * 21 + 6, ' '.join(map(str, row)), 17, 'middle', 800)
            return out
        body += put(groups.get('left', []), 68, 110, 2) + put(groups.get('both', []), 150, 110, 2) + put(groups.get('right', []), 232, 110, 2) + put(groups.get('out', []), 150, 188, 6)
        body += T(150, 168, '', 12)
    return svg(300, 204, body, caption or f'Two loops in a box: "{left}" and "{right}"')


def pets_grid(caption=''):
    """Clue grid: rows Ali, Mei, Ben; columns Cat, Dog, Fish; Ali's cat and dog are crossed (clue 1), as printed."""
    cw, rw, nw = 66, 36, 80
    W = nw + 3 * cw + 4
    body = Re(2, 2, nw, rw, '#EDEDED', NAVY, 2) + ''.join(Re(2 + nw + j * cw, 2, cw, rw, '#EDEDED', NAVY, 2) + T(2 + nw + j * cw + cw / 2, 2 + rw / 2 + 6, nm, 16, 'middle', 800) for j, nm in enumerate(['Cat', 'Dog', 'Fish']))
    for i, nm in enumerate(['Ali', 'Mei', 'Ben']):
        y = 2 + (i + 1) * rw
        body += Re(2, y, nw, rw, '#EDEDED', NAVY, 2) + T(2 + nw / 2, y + rw / 2 + 6, nm, 16, 'middle', 800)
        for j in range(3):
            body += Re(2 + nw + j * cw, y, cw, rw, '#fff', NAVY, 2)
            if nm == 'Ali' and j < 2:
                body += T(2 + nw + j * cw + cw / 2, y + rw / 2 + 9, '×', 28, 'middle', 800, WARM)
    return svg(W, 4 * rw + 6, body, caption or 'Clue grid. Rows Ali, Mei and Ben. Columns cat, dog and fish. Ali has crosses under cat and dog.')


def line_boxes(labels=('1st', '2nd', '3rd', '4th'), filled=None, caption=''):
    bw = 72
    body = ''
    for i, lab in enumerate(labels):
        x = 2 + i * bw
        body += Re(x, 22, bw - 4, 46, '#fff' if not (filled and filled.get(i)) else PALE, NAVY, 2.2, 6) + T(x + (bw - 4) / 2, 15, lab, 16, 'middle', 800)
        if filled and filled.get(i):
            body += T(x + (bw - 4) / 2, 52, filled[i], 17, 'middle', 800)
    return svg(len(labels) * bw, 74, body, caption or 'Four places in a line: ' + ', '.join(labels))


def tiles(nums, caption=''):
    body = ''.join(Re(4 + i * 62, 4, 54, 54, '#FFE08A', NAVY, 2.4, 8) + T(4 + i * 62 + 27, 40, n, 26, 'middle', 800) for i, n in enumerate(nums))
    return svg(len(nums) * 62 + 4, 62, body, caption or 'Number tiles ' + ', '.join(map(str, nums)))


def poly_row(items, box=92, per_row=3, caption=''):
    """Small drawings in a row.  items: (polys, label) with polys = [(points, fill)], points in any units (each drawing is scaled to fit one box)."""
    body, rows = '', (len(items) + per_row - 1) // per_row
    cw = box + 22
    for k, (polys, label) in enumerate(items):
        xs = [x for p, _ in polys for x, _ in p]
        ys = [y for p, _ in polys for _, y in p]
        w, h = max(xs) - min(xs), max(ys) - min(ys)
        s = min(box / (w or 1), box / (h or 1), 40)
        r, c = divmod(k, per_row)
        ox = 6 + c * cw + (box - w * s) / 2 - min(xs) * s
        oy = 6 + r * (box + 52) + (box - h * s) / 2 - min(ys) * s
        for p, fill in polys:
            body += Po([(ox + x * s, oy + y * s) for x, y in p], fill, NAVY, 2.6)
        for li, line in enumerate(label.split('|')):
            body += T(6 + c * cw + box / 2, 6 + r * (box + 52) + box + 20 + li * 17, line, 14, 'middle', 700)
    return svg(6 + per_row * cw if len(items) >= per_row else 6 + len(items) * cw, 6 + rows * (box + 52) - 8, body, caption or 'Shapes made from two triangles')


def polyomino_row(shapes, cell=20, per_row=5, caption=''):
    """Shapes made of joined squares (each shape = list of (x, y) cells), drawn in rows."""
    body, x, y, rowh = '', 6, 6, 0
    gap = 26
    for sh in shapes:
        w = (max(c[0] for c in sh) + 1) * cell
        h = (max(c[1] for c in sh) + 1) * cell
        if x + w > 288 and x > 6:
            x, y, rowh = 6, y + rowh + gap, 0
        for cx, cy in sh:
            body += Re(x + cx * cell, y + cy * cell, cell, cell, '#BFE3E0', NAVY, 2)
        x += w + gap
        rowh = max(rowh, h)
    return svg(300, y + rowh + 8, body, caption or 'Shapes made of joined squares')


# ================================================================ Week 5 (lessons 9 and 10): length and puzzle-day figures
RIB_COL = {'A': '#8CC8F0', 'B': '#F6C27A', 'C': '#8EDDA0'}


def ribbon_cells(lens):
    """The squares of each ribbon, one (x, y) place per square, row by row: the figure is drawn from these and the checkers count them."""
    return {nm: [(i, k) for i in range(n)] for k, (nm, n) in enumerate(lens.items())}


def ribbons_fig(lens, sq=26, caption=''):
    """Ribbons made of equal squares, lined up at the left end, one under the other (no numbers written)."""
    cells = ribbon_cells(lens)
    mx = max(len(v) for v in cells.values())
    body = ''
    for k, (nm, cs) in enumerate(cells.items()):
        y = 4 + k * (sq + 12)
        body += T(10, y + sq / 2 + 6, nm, 18, 'middle', 800)
        for i, _ in cs:
            body += Re(26 + i * sq, y, sq, sq, RIB_COL.get(nm, '#CFE8D5'), NAVY, 2)
    return svg(26 + mx * sq + 6, 4 + len(cells) * (sq + 12), body, caption or 'Ribbons made of equal squares: ' + ', '.join(lens))


def span_cells(parts, width):
    """Cut a length `width` into `parts` equal spans: the left end of every span."""
    return [width * i / parts for i in range(parts)]


def desk_fig(ali=6, mei=8, width=300, caption=''):
    """The same desk measured with Ali's spans and with Mei's spans (equal spans, no gaps)."""
    body = Re(2, 2, width, 26, '#FFF3C4', NAVY, 2.4) + T(10, 21, 'the desk', 15, 'start', 800)
    for k, (nm, parts, col) in enumerate((('Ali', ali, '#FFC93C'), ('Mei', mei, '#BFE0F5'))):
        y = 40 + k * 56
        w = width / parts
        for x in span_cells(parts, width):
            body += Re(2 + x, y, w, 24, col, NAVY, 2.2)
        body += T(2, y + 42, f'{nm}: {parts} spans', 15, 'start', 800)
    return svg(width + 4, 40 + 56 + 50, body, caption or f'The same desk measured by Ali with {ali} spans and by Mei with {mei} spans')


def clip_eraser_fig(clips=5, erasers=12, per=2, caption=''):
    """Bars: 1 clip is as long as `per` erasers; a desk of `clips` clips; a pencil of `erasers` erasers."""
    u, lw = 20, 84
    rows = [('1 clip', [('c', per)], ''), (f'{per} erasers', [('e', 1)] * per, ''), ('desk', [('c', per)] * clips, '? erasers'), ('pencil', [('e', 1)] * erasers, '? clips')]
    W = lw + max(sum(w for _, w in segs) for _, segs, _ in rows) * u + 76
    body = ''
    for k, (lab, segs, tail) in enumerate(rows):
        y = 4 + k * 34
        body += T(2, y + 20, lab, 14, 'start', 800)
        x = lw
        for kind, w in segs:
            body += Re(x, y + 2, w * u, 24, '#8CC8F0' if kind == 'c' else '#F6B8A4', NAVY, 2)
            x += w * u
        if tail:
            body += T(x + 8, y + 20, tail, 14, 'start', 800, TEAL)
    return svg(W, 4 + len(rows) * 34, body, caption or f'1 clip is as long as {per} erasers. A desk of {clips} clips. A pencil of {erasers} erasers.')


def pencil_cubes_fig(mei=8, ali_more=3, ben_less=2, caption=''):
    """Mei's pencil in cubes; Ali's is the same length and then `ali_more` more (one dashed box); Ben's is `ben_less` cubes shorter than Mei's."""
    u, lw = 30, 44
    body = ''
    rows = [('Mei', mei, None), ('Ali', mei, f'{ali_more} more'), ('Ben', mei - ben_less, f'{ben_less} fewer')]
    for k, (nm, n, extra) in enumerate(rows):
        y = 4 + k * 46
        body += T(lw - 6, y + 20, nm, 16, 'end', 800)
        for i in range(n):
            body += Re(lw + i * u, y, u, 26, '#FFE08A', NAVY, 2)
        if extra:
            k_extra = ali_more if nm == 'Ali' else ben_less
            body += Re(lw + n * u, y, k_extra * u, 26, '#fff', TEAL, 2.4, 0, '5 3') + T(lw + n * u + k_extra * u + 8, y + 19, extra, 14, 'start', 800, TEAL)
    W = lw + (mei + ali_more) * u + 70
    return svg(W, 4 + 3 * 46 - 14, body, caption or f'Mei: {mei} cubes. Ali: the same and {ali_more} more. Ben: {ben_less} fewer than Mei.')


BAR_COL = ['#FFE08A', '#8EDDA0', '#F4A6A0', '#8CC8F0']


def ruler_fig(bars, lo=0, hi=12, cm=26, caption=''):
    """A centimetre ruler lo..hi with bars (from, to, label) lying above it, lined up with the marks (one bar per line)."""
    lw = 20
    W = lw * 2 + (hi - lo) * cm
    nb = len(bars)
    top = 6 + nb * 34
    body = ''
    for k, (a, b, lab) in enumerate(bars):
        y = 6 + k * 34
        body += Re(lw + (a - lo) * cm, y, (b - a) * cm, 26, BAR_COL[k % 4], NAVY, 2.2) + T(lw + (a - lo) * cm + (b - a) * cm / 2, y + 19, lab, 15, 'middle', 800)
    body += Re(lw, top, (hi - lo) * cm, 26, '#FFF9E8', NAVY, 2.4)
    for v in range(lo, hi + 1):
        x = lw + (v - lo) * cm
        body += Ln(x, top, x, top + (22 if v % 5 == 0 else 15), 2) + T(x, top + 44, v, 14, 'middle', 700)
    return svg(W, top + 52, body, caption or ('A centimetre ruler from %d to %d with ' % (lo, hi) + ', '.join(f'{lab} from {a} to {b}' for a, b, lab in bars)))


def bird(cx, cy, s):
    """A small bird in profile (a round body, a head with a beak, a short tail, two legs); about 0.86 s wide so neighbours in a row never touch."""
    u = s * 0.9
    bx, by = cx - 0.04 * u, cy + 0.08 * u
    return (f'<line x1="{bx - 0.06 * u}" y1="{by + 0.2 * u}" x2="{bx - 0.06 * u}" y2="{by + 0.36 * u}" stroke="{NAVY}" stroke-width="1.8" stroke-linecap="round"/>'
            f'<line x1="{bx + 0.1 * u}" y1="{by + 0.2 * u}" x2="{bx + 0.1 * u}" y2="{by + 0.36 * u}" stroke="{NAVY}" stroke-width="1.8" stroke-linecap="round"/>'
            f'<polygon points="{bx - 0.26 * u},{by - 0.02 * u} {bx - 0.48 * u},{by - 0.18 * u} {bx - 0.48 * u},{by + 0.12 * u}" fill="#F4D35E" stroke="{NAVY}" stroke-width="1.6" stroke-linejoin="round"/>'
            f'<ellipse cx="{bx}" cy="{by}" rx="{0.3 * u}" ry="{0.24 * u}" fill="#F4D35E" stroke="{NAVY}" stroke-width="1.8"/>'
            f'<path d="M {bx - 0.2 * u} {by - 0.02 * u} Q {bx - 0.02 * u} {by + 0.2 * u} {bx + 0.16 * u} {by - 0.02 * u}" fill="#E8B930" stroke="{NAVY}" stroke-width="1.3"/>'
            f'<circle cx="{bx + 0.2 * u}" cy="{by - 0.24 * u}" r="{0.15 * u}" fill="#F4D35E" stroke="{NAVY}" stroke-width="1.8"/>'
            f'<polygon points="{bx + 0.33 * u},{by - 0.3 * u} {bx + 0.48 * u},{by - 0.24 * u} {bx + 0.33 * u},{by - 0.18 * u}" fill="{WARM}" stroke="{NAVY}" stroke-width="1.2" stroke-linejoin="round"/>'
            + Ci(bx + 0.22 * u, by - 0.27 * u, 1.5, NAVY, NAVY, 1))


PET_ICON = dict(Dog=dog_face, Cat=cat_face, Fish=fish, Bird=bird)


def pets_street_fig(pets, caption=''):
    """Picture graph of pets in a street: one picture for each pet; pets = list of (name, number)."""
    return picture_graph(pets, '1 pet (each picture)', lambda nm: PET_ICON[nm], max(n for _, n in pets), caption=caption or 'Picture graph of pets in a street, one picture for each pet')


def example_table(rows, caption='', fit=False):
    """A small table: first row = column titles, then rows of cells (text).  fit=True sizes each column to its longest text (so titles never touch)."""
    nc = len(rows[0])
    cw = [96] + [80] * (nc - 2) + [100]
    if fit:
        cw = [max(58, int(max(len(str(r[c])) for r in rows) * 9.8 + 24)) for c in range(nc)]
    W = sum(cw) + 4
    body = ''
    for r, row in enumerate(rows):
        y = 2 + r * 30
        x = 2
        for c, cell in enumerate(row):
            body += Re(x, y, cw[c], 30, '#D9D9D9' if r == 0 else ('#fff' if r % 2 else '#FAF6EA'), NAVY, 1.6) + T(x + cw[c] / 2, y + 20, cell, 14 if r == 0 else 15, 'middle', 800 if r == 0 else 700)
            x += cw[c]
    return svg(W, 2 + len(rows) * 30 + 4, body, caption or 'An example table')
