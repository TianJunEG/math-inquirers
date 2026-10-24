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
