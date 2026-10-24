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
    return (f'<ellipse cx="{cx - r * 1.05}" cy="{cy + 1}" rx="{r * 0.42}" ry="{r * 0.85}" fill="#A9795A" stroke="{NAVY}" stroke-width="1.6"/>'
            f'<ellipse cx="{cx + r * 1.05}" cy="{cy + 1}" rx="{r * 0.42}" ry="{r * 0.85}" fill="#A9795A" stroke="{NAVY}" stroke-width="1.6"/>'
            + Ci(cx, cy + 1, r, '#E8CBA7', NAVY, 1.8) + Ci(cx - r * 0.36, cy - 2, 1.8, NAVY, NAVY, 1) + Ci(cx + r * 0.36, cy - 2, 1.8, NAVY, NAVY, 1)
            + Ci(cx, cy + 4, 2.6, NAVY, NAVY, 1))


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
    body = Re(2, 2, W - 4, rh, '#D9D9D9', NAVY, 1.6) + T(10, 2 + rh / 2 + 5, 'Fruit', 15, 'start', 800) + T(150, 2 + rh / 2 + 5, 'Tally', 15, 'middle', 800) + T(262, 2 + rh / 2 + 5, 'Total', 15, 'middle', 800)
    for k, nm in enumerate(names):
        y = 2 + rh * (k + 1)
        body += Re(2, y, W - 4, rh, '#fff', NAVY, 1.6) + T(10, y + rh / 2 + 5, nm, 15, 'start', 700)
        body += Ln(100, y, 100, y + rh, 1.6) + Ln(222, y, 222, y + rh, 1.6)
        if filled and nm in filled:
            c = filled[nm]
            x = 108
            for g in range(c // 5):
                for i in range(4):
                    body += Ln(x + i * 6, y + 7, x + i * 6, y + rh - 7, 2, NAVY)
                body += Ln(x - 3, y + rh - 9, x + 21, y + 9, 2, NAVY)
                x += 32
            for i in range(c % 5):
                body += Ln(x + i * 6, y + 7, x + i * 6, y + rh - 7, 2, NAVY)
            body += T(262, y + rh / 2 + 6, c, 17, 'middle', 800)
    return svg(W, 4 + rh * (len(names) + 1), body, 'A table with a row for each fruit and a tally column')


# ---------------------------------------------------------------- sticks
STICK = '#B8860B'


def _stick(x1, y1, x2, y2):
    return Ln(x1, y1, x2, y2, 6, STICK) + Ln(x1, y1, x2, y2, 2.2, NAVY)


def triangle_rows(counts=(1, 2, 3), s=44, caption=''):
    """Rows of n triangles in a line made of sticks (n triangles use 2n + 1 sticks): zigzag sticks along the top and bottom."""
    h = s * 0.87
    body, x = '', 8
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
    body, x, y0 = '', 8, 10
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
