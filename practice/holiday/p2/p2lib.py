"""Level 2 (P2) helpers for the online holiday practice: the printed workbook figures (taken from the workbook's own HTML so the picture is the printed one),
a few figures redrawn for a phone, and brute-force helpers for the independent checkers.  Imported by p2/NN/lesson.py (after `from hlib import *`)."""
import itertools, os, re
from hlib import svg as _svg, T, Ln, Ci, Re, NAVY, YEL, TEAL, WARM, PALE, esc

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
_BODY = None


def printed_fig(label_start, lesson_marker=None):
    """The figure of the printed workbook (p2/workbook_body.html, built from p2/content/lN.js) whose aria-label starts with label_start,
    made responsive (full width up to its own viewBox width)."""
    global _BODY
    if _BODY is None:
        _BODY = open(os.path.join(ROOT, 'p2', 'workbook_body.html'), encoding='utf-8').read()
    found = [s for s in re.findall(r'<svg.*?</svg>', _BODY, flags=re.S) if re.search(r'aria-label="' + re.escape(label_start), s)]
    if not found:
        raise ValueError('printed figure not found: ' + label_start)
    s = found[0]
    root = re.match(r'<svg[^>]*>', s).group(0)
    vb = re.search(r'viewBox="0 0 (\d+) (\d+)"', root)
    new = re.sub(r'\swidth="\d+"', '', root)
    new = re.sub(r'style="[^"]*"', f'style="width:100%;max-width:{vb.group(1)}px;height:auto;display:block;margin:0 auto"', new)
    return s.replace(root, new, 1)


# ---------------------------------------------------------------- figures redrawn for a phone
def tens_blocks(ali_tens, siti_hundreds, siti_tens):
    """Ten-blocks (rods) and hundred-blocks (squares), counts written in the labels."""
    def rod(x, y):
        b = Re(x, y, 8, 34, '#fff', NAVY, 1.4)
        for k in range(1, 10):
            b += Ln(x, y + k * 3.4, x + 8, y + k * 3.4, 0.6, NAVY)
        return b
    per = 23
    b = T(2, 18, f'Ali: {ali_tens} ten-blocks', 16, 'start', 800)
    rows = (ali_tens + per - 1) // per
    for i in range(ali_tens):
        b += rod(2 + (i % per) * 14.4, 28 + (i // per) * 44)
    y = 28 + rows * 44 + 22
    b += T(2, y, f'Siti: {siti_hundreds} hundred-blocks and {siti_tens} ten-blocks', 16, 'start', 800)
    y += 10
    for i in range(siti_hundreds):
        x = 2 + i * 38
        b += Re(x, y, 34, 34, '#CDE8F7', NAVY, 1.6)
        for k in range(1, 10):
            b += Ln(x + k * 3.4, y, x + k * 3.4, y + 34, 0.5, NAVY) + Ln(x, y + k * 3.4, x + 34, y + k * 3.4, 0.5, NAVY)
    x0 = 2 + siti_hundreds * 38 + 8
    for i in range(siti_tens):
        b += rod(x0 + i * 14.4, y)
    return _svg(340, y + 44, b, f'Ali has {ali_tens} ten-blocks. Siti has {siti_hundreds} hundred-blocks and {siti_tens} ten-blocks.')


def magic_square(grid, caption=''):
    """3 by 3 magic square; '' = empty square, numbers shown; the given numbers on a pale blue tile."""
    c = 64
    b = ''
    for r in range(3):
        for k in range(3):
            v = grid[r][k]
            b += Re(10 + k * c, 8 + r * c, c, c, '#DDEBF7' if v != '' else '#fff', NAVY, 2.6)
            if v != '':
                b += T(10 + k * c + c / 2, 8 + r * c + c / 2 + 8, v, 24)
    return _svg(10 + 3 * c + 10, 8 + 3 * c + 8, b, caption or 'A magic square with 3 rows and 3 columns')


# ---------------------------------------------------------------- brute-force helpers (independent checkers)
def numbers_from_cards(digits):
    """Every different 3-digit number made with each card once; a number cannot start with 0.  Sorted."""
    out = set()
    for p in itertools.permutations(digits):
        if p[0] != 0:
            out.add(p[0] * 100 + p[1] * 10 + p[2])
    return sorted(out)


def digit_sum(n):
    t = 0
    for ch in str(n):
        t += int(ch)
    return t


def split_two(digits6):
    """All (x, y) of two 3-digit numbers that use the six cards once each."""
    for p in set(itertools.permutations(digits6)):
        yield p[0] * 100 + p[1] * 10 + p[2], p[3] * 100 + p[4] * 10 + p[5]


def two_bars_model(total, diff):
    """The model of 'two numbers add up to <total>, the long one is <diff> more': the long bar is the short bar plus a hatched piece.  Readable on a phone (340 wide)."""
    sw, ew, x0 = 120, 56, 84
    b = ('<defs><pattern id="hz2" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="6" height="6" fill="#fff"/>'
         f'<line x1="0" y1="0" x2="0" y2="6" stroke="{NAVY}" stroke-width="2"/></pattern></defs>')
    b += T(4, 30, 'short bar', 15, 'start', 800) + T(4, 76, 'long bar', 15, 'start', 800)
    b += Re(x0, 10, sw, 30, '#FFE08A', NAVY, 2.4) + T(x0 + sw / 2, 31, '?', 18)
    b += Re(x0, 56, sw, 30, '#FFE08A', NAVY, 2.4) + T(x0 + sw / 2, 77, '?', 18)
    b += Re(x0 + sw, 56, ew, 30, 'url(#hz2)', NAVY, 2.4) + Re(x0 + sw + 8, 62, ew - 16, 18, '#fff', 'none', 0) + T(x0 + sw + ew / 2, 77, diff, 15, 'middle', 800, NAVY)
    b += Ln(x0, 100, x0 + sw + ew, 100, 2.4) + T(x0 + (sw + ew) / 2, 122, f'{total} altogether', 15, 'middle', 800, TEAL)
    return _svg(340, 130, b, f'Two bars: the long bar is {diff} longer than the short bar; together they make {total}')


# ---------------------------------------------------------------- week 2 additions: small tables drawn for a phone, and figure readers for the checkers
def grid_table(rows, col_w=46, label_w=92, caption='', head=None):
    """A table as a figure: rows = [(label, [cell, ...])]; a cell '' is an empty white box to fill in; given cells are on a pale tile.
    head = optional header row (label, [cells]) drawn on a navy-tinted band (e.g. 'Flowers', [1, 2, 3, 4, 5, 6])."""
    allrows = ([head] if head else []) + list(rows)
    n = max(len(c) for _, c in allrows)
    rh = 40
    w = label_w + n * col_w + 8
    b = ''
    for r, (lab, cells) in enumerate(allrows):
        y = 4 + r * rh
        hd = bool(head) and r == 0
        b += Re(4, y, label_w, rh, '#D9D9D9', NAVY, 2.2) + T(4 + label_w / 2, y + 26, lab, 16, 'middle', 800)
        for k, v in enumerate(cells):
            x = 4 + label_w + k * col_w
            fill = '#D9D9D9' if hd else ('#fff' if v == '' else '#DDEBF7')
            b += Re(x, y, col_w, rh, fill, NAVY, 2.2)
            if v != '':
                b += T(x + col_w / 2, y + 27, v, 18, 'middle', 800 if hd else 700)
    return _svg(w, 8 + len(allrows) * rh, b, caption or 'A table: ' + '; '.join(f'{lab}: ' + ', '.join(str(c) if c != '' else 'empty' for c in cells) for lab, cells in allrows))


def circles_of(fig):
    """(distinct rows, distinct columns, count) of the <circle> counters in a drawn array (read from the picture, not from the question)."""
    cs = re.findall(r'<circle cx="([\d.]+)" cy="([\d.]+)"', fig)
    return len({y for _, y in cs}), len({x for x, _ in cs}), len(cs)


def tray_counts(fig):
    """(cups altogether, cups still visible) read from the tray picture: cups are the white <path> shapes, the cloth is the red <rect>."""
    cups = re.findall(r'<path d="M([\d.]+) ([\d.]+) L([\d.]+) ([\d.]+) L([\d.]+) ([\d.]+) L([\d.]+) ([\d.]+) Z"', fig)
    cloth = re.search(r'<rect x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" height="([\d.]+)" rx="12" fill="#D64545"', fig)
    cx, cy, cw, ch = (float(v) for v in cloth.groups())
    seen = 0
    for c in cups:
        xs = [float(c[i]) for i in (0, 2, 4, 6)]
        ys = [float(c[i]) for i in (1, 3, 5, 7)]
        covered = min(xs) >= cx and max(xs) <= cx + cw and min(ys) >= cy and max(ys) <= cy + ch
        seen += 0 if covered else 1
    return len(cups), seen


def combine(figs, label, gap=10, target=340):
    """Several svg figures one above the other as ONE svg (the runner shows one svg per question). A figure wider than `target` is scaled down to it (its text
    is lifted first, so it is still readable on a phone); the others keep their size and are centred."""
    from hlib import lift_text
    parts = []
    for f in figs:
        root = re.match(r'<svg[^>]*>', f).group(0)
        vb = [float(v) for v in re.search(r'viewBox="([\d. -]+)"', root).group(1).split()]
        inner = f[len(root):f.rindex('</svg>')]
        sc = min(1.0, target / vb[2])
        if sc < 1.0:
            inner = lift_text(vb[2], inner)
        parts.append((vb, inner, sc))
    W = max(vb[2] * sc for vb, _, sc in parts)
    y, body = 0, ''
    for vb, inner, sc in parts:
        w, h = vb[2] * sc, vb[3] * sc
        body += (f'<svg x="{(W - w) / 2:g}" y="{y:g}" width="{w:g}" height="{h:g}" viewBox="{vb[0]:g} {vb[1]:g} {vb[2]:g} {vb[3]:g}" overflow="visible" '
                 f'style="width:{w:g}px;height:{h:g}px;max-width:none">{inner}</svg>')
        y += h + gap
    return _svg(W, y - gap, body, label)


def van_fig(children=28, seats=5):
    """One van with its seats, and the children waiting in rows of 7."""
    b = T(150, 20, f'one van: {seats} seats', 15, 'middle', 800)
    b += Re(75, 30, 150, 44, PALE, NAVY, 2.6, 10)
    for k in range(seats):
        b += Re(82 + k * 28, 38, 22, 28, YEL, NAVY, 2)
    b += Ci(110, 82, 9, NAVY, NAVY, 1) + Ci(190, 82, 9, NAVY, NAVY, 1)
    b += T(150, 120, f'{children} children', 15, 'middle', 800, TEAL)
    for k in range(children):
        b += Ci(66 + (k % 7) * 28, 140 + (k // 7) * 28, 10, '#CDE8F7', NAVY, 2)
    return _svg(300, 140 + ((children - 1) // 7) * 28 + 18, b, f'A van with {seats} seats, and {children} children waiting in rows of 7')


def sharing_fig(total=23, friends=4):
    """The stickers (yellow dots), one plate for each friend, and a box for the stickers left over."""
    rows = (total + 9) // 10
    box_h = 36 + rows * 26
    b = Re(4, 4, 332, box_h, PALE, NAVY, 2.4, 8) + T(14, 24, f'{total} stickers', 15, 'start', 800)
    for k in range(total):
        b += Ci(24 + (k % 10) * 30, 48 + (k // 10) * 26, 10, YEL, NAVY, 1.8)
    y = 4 + box_h + 44
    for f in range(friends):
        cx = 36 + f * 70
        b += Ci(cx, y, 30, '#fff', NAVY, 2.4).replace('/>', ' stroke-dasharray="5 4"/>') + T(cx, y + 52, f'Friend {f + 1}', 14, 'middle', 800)
    b += Re(284, y - 30, 52, 60, '#fff', NAVY, 2.4, 8, '5 4') + T(310, y + 52, 'left over', 14, 'middle', 800, TEAL)
    return _svg(340, y + 64, b, f'{total} stickers, {friends} empty plates for the friends and a box for the stickers left over')


def hens_fig(n=7):
    """A pen with n hens (a yellow body, a beak and two legs each) and the key: a hen has 2 legs, a goat has 4 legs."""
    b = Re(4, 28, 332, 78, PALE, NAVY, 2.4, 10, '6 4') + T(14, 20, f'the pen: {n} animals', 15, 'start', 800)
    for k in range(n):
        cx = 36 + k * 44
        b += Ci(cx, 56, 14, YEL, NAVY, 2) + f'<polygon points="{cx + 13},{56} {cx + 22},{59} {cx + 13},{62}" fill="{WARM}" stroke="{NAVY}" stroke-width="1.5"/>'
        b += Ln(cx - 4, 70, cx - 4, 90, 2.4) + Ln(cx + 4, 70, cx + 4, 90, 2.4) + Ln(cx - 8, 90, cx, 90, 2.4) + Ln(cx, 90, cx + 8, 90, 2.4)
    b += T(14, 126, 'a hen has 2 legs, a goat has 4 legs', 15, 'start', 800, TEAL)
    return _svg(340, 136, b, f'A pen with {n} hens. A hen has 2 legs and a goat has 4 legs.')


def towers_fig(cubes=(2, 5, 8)):
    """Towers of cubes, 1 cube = one square, with their numbers, and 'and so on'."""
    u = 22
    top = 8 + max(cubes) * u
    b = ''
    for i, n in enumerate(cubes):
        x = 32 + i * 66
        for k in range(n):
            b += Re(x, top - (k + 1) * u, u, u, YEL, NAVY, 1.8)
        b += T(x + u / 2, top + 20, f'Tower {i + 1}', 14, 'middle', 800) + T(x + u / 2, top + 38, f'{n} cubes', 14, 'middle', 700, TEAL)
    b += T(32 + len(cubes) * 66 + 6, top - 40, '... and so on', 15, 'start', 800, TEAL, True)
    return _svg(340, top + 48, b, 'Towers of cubes: tower 1 has ' + ', tower '.join(f'{i + 1} has {n}' for i, n in enumerate(cubes)) + ' cubes; the towers keep growing in the same way')
