"""Level 4 (Primary 4, ages 9-11) helpers for the online holiday practice: number formatting, brute-force helpers for the INDEPENDENT checkers,
and the figures that the printed workbook draws (redrawn here at a size that is readable on a 390 px phone).

Lesson files import this as  `from p4lib import *`  after putting this folder on sys.path.
"""
import itertools, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from hlib import *      # noqa: E402,F401  (svg, T, Ln, Ci, Re, NAVY, YEL, TEAL, WARM, PALE ...)

SKY = '#DDEBF7'


def g(n):
    """The workbook way to print a whole number: a space between groups from 5 digits (4982, 5350, 47 285, 100 000)."""
    s = str(n)
    if len(s) < 5:
        return s
    out = []
    while s:
        out.insert(0, s[-3:]); s = s[:-3]
    return ' '.join(out)


# ---------------------------------------------------------------- independent checkers (loops over the numbers in the question)
def factors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def factor_pairs(n):
    """Pairs a x b = n with a <= b, found by trying 1, 2, 3 ... in order."""
    return [(a, n // a) for a in range(1, n + 1) if a * a <= n and n % a == 0]


def multiples_up_to(k, limit):
    out, v = [], k
    while v <= limit:
        out.append(v); v += k
    return out


def first_common_multiple(a, b):
    v = max(a, b)
    while v % a or v % b:
        v += 1
    return v


def common_factors(a, b):
    return [d for d in factors(a) if b % d == 0]


def greatest_common_factor(a, b):
    return max(common_factors(a, b))


def round_to(n, unit):
    """Round a whole number to the nearest `unit`; exactly halfway rounds UP (the rule children are taught)."""
    q, r = divmod(n, unit)
    return (q + 1) * unit if 2 * r >= unit else q * unit


def rounds_to(lo, hi, value, unit):
    """All whole numbers in [lo, hi] that round to `value` to the nearest `unit`."""
    return [n for n in range(lo, hi + 1) if round_to(n, unit) == value]


def digit_sum(n):
    return sum(int(c) for c in str(n))


def five_digit_numbers():
    return range(10000, 100000)


def card_numbers(cards):
    """Every 5-digit number made from the digit cards once each (no leading 0)."""
    out = []
    for p in itertools.permutations(cards):
        if p[0] != 0:
            out.append(int(''.join(map(str, p))))
    return sorted(out)


def is_palindrome(n):
    s = str(n)
    return s == s[::-1]


# ---------------------------------------------------------------- figures
def array_figure(rows, cols, highlight_rows=None, caption=''):
    """A rows x cols array of dots (trees), drawn small enough for a phone."""
    r, gap, x0, y0 = 7, 20, 14, 14
    W = max(x0 * 2 + (cols - 1) * gap + 2 * r, 290)
    xs = (W - ((cols - 1) * gap + 2 * r)) / 2
    b = ''
    for i in range(rows):
        for j in range(cols):
            b += Ci(xs + r + j * gap, y0 + r + i * gap, r, '#CDE8C8', NAVY, 1.8)
    H = y0 * 2 + (rows - 1) * gap + 2 * r + 24
    b += T(W / 2, H - 6, caption or f'{rows} rows of {cols} trees', 15, 'middle', 800, TEAL)
    return svg(W, H, b, f'An array of {rows * cols} trees: {rows} rows with {cols} trees in each row.')


def time_line(start_h=6, minutes=60, label_every=15, tick_every=5, suffix='am'):
    """A time line from start_h:00 for `minutes`, a tick every tick_every minutes, a label every label_every minutes."""
    x0, k = 24, 5.0
    W = int(2 * x0 + minutes * k + 30)
    y = 40
    b = Ln(x0 - 8, y, x0 + minutes * k + 8, y, 3)
    for m in range(0, minutes + 1, tick_every):
        big = m % label_every == 0
        x = x0 + m * k
        b += Ln(x, y - (11 if big else 6), x, y + (11 if big else 6), 3 if big else 2)
        if big:
            h, mm = start_h + m // 60, m % 60
            b += T(x, y + 32, f'{h}:{mm:02d}', 15)
    b += T(x0 + minutes * k + 24, y + 5, suffix, 15, 'middle', 800, TEAL)
    return svg(W, 84, b, f'A time line from {start_h}:00 {suffix} for {minutes} minutes, marked every {tick_every} minutes.')


def number_line_k(lo, hi, major, minor, cross=None, dots=(), caption='', label_fmt=g, extra_labels=()):
    """A number line lo..hi, ticks every `minor`, labelled every `major`. cross: a value marked with an X above the line. dots: values marked with a filled dot."""
    x0, x1 = 40, 332
    W = x1 + x0
    px = lambda v: x0 + (v - lo) * (x1 - x0) / (hi - lo)
    y = 58
    b = (T(6, 16, caption, 15, 'start', 800) if caption else '') + Ln(x0 - 14, y, x1 + 14, y, 3)
    v = lo
    while v <= hi:
        big = (v - lo) % major == 0
        b += Ln(px(v), y - (12 if big else 7), px(v), y + (12 if big else 7), 3 if big else 1.6)
        if big or v in extra_labels:
            b += T(px(v), y + 34, label_fmt(v), 14, 'middle', 700, NAVY)
        v += minor
    if cross is not None:
        b += T(px(cross), y - 16, '×', 30, 'middle', 800, WARM) + T(px(cross), y - 40, label_fmt(cross), 14, 'middle', 800, WARM)
    for d in dots:
        b += Ci(px(d), y, 6, YEL, NAVY, 2)
    return svg(W, 104, b, caption or f'A number line from {g(lo)} to {g(hi)} with a tick every {g(minor)} and a label every {g(major)}.')


def digit_cards(digits):
    w, gp = 46, 12
    W = len(digits) * w + (len(digits) - 1) * gp + 12
    b = ''
    for i, d in enumerate(digits):
        x = 6 + i * (w + gp)
        b += Re(x, 6, w, 62, YEL, NAVY, 2.6, 9) + T(x + w / 2, 49, d, 34)
    return svg(W, 76, b, 'Digit cards ' + ', '.join(map(str, digits)))


# ================================================================ WEEK 2 (lessons 3 and 4): number sentences, brackets, fractions
from fractions import Fraction as Fr      # noqa: E402

PY_OP = {'+': '+', '−': '-', '×': '*', '÷': '/'}
SHOW_OP = {'+': '+', '-': '−', '*': '×', '/': '÷'}


def value(expr):
    """The value of a number sentence written with + − × ÷ and brackets, worked out by Python's own order of operations (exact fractions)."""
    s = expr.replace('−', '-').replace('×', '*').replace('÷', '/')
    import re as _re
    if not _re.fullmatch(r'[\d\s+\-*/()]*', s):
        raise ValueError(expr)
    s = _re.sub(r'(\d+)', r'Fr(\1)', s)
    return eval(s, {'Fr': Fr})


def spaced_sentence(toks):
    out = ''
    for t in toks:
        if isinstance(t, int):
            out += str(t)
        elif t in '()':
            out += t
        else:
            out += f' {t} '
    return out.replace('( ', '(').replace(' )', ')').replace('  ', ' ').strip()


def sign_solutions(nums, total, signs='+−×÷'):
    """Every way to write a sign between neighbouring numbers so that the sentence equals the total (normal order of operations)."""
    out = []
    for combo in itertools.product(signs, repeat=len(nums) - 1):
        toks = []
        for i, n in enumerate(nums):
            toks.append(n)
            if i < len(combo):
                toks.append(combo[i])
        try:
            if value(spaced_sentence(toks)) == total:
                out.append(list(combo))
        except ZeroDivisionError:
            pass
    return out


def sign_sentence(nums, signs):
    toks = []
    for i, n in enumerate(nums):
        toks.append(n)
        if i < len(signs):
            toks.append(signs[i])
    return spaced_sentence(toks)


def sign_accepts(nums, signs, total):
    """The signs alone ('× −', '×−', '×, −') or the whole number sentence with or without '= total'. Case, spaces, x * for × and / for ÷ are matched loosely by the page."""
    out = {' '.join(signs), ''.join(signs), ', '.join(signs), ','.join(signs)}
    s = sign_sentence(nums, signs)
    out.update({s, f'{s} = {total}'})
    return sorted(out)


def with_brackets(nums, ops, i, j):
    toks = []
    for k, n in enumerate(nums):
        if k == i:
            toks.append('(')
        toks.append(n)
        if k == j:
            toks.append(')')
        if k < len(ops):
            toks.append(ops[k])
    return toks


def one_pair_solutions(nums, ops, target):
    """Every way to put ONE pair of brackets round two or more neighbouring numbers (not round the whole sentence) so that the sentence equals the target."""
    sols = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if i == 0 and j == len(nums) - 1:
                continue
            toks = with_brackets(nums, ops, i, j)
            if value(spaced_sentence(toks)) == target:
                sols.append(spaced_sentence(toks))
    return sols


def trees(nums):
    """Every way of putting + − × ÷ and brackets in a row of numbers: (value, tree) pairs. A tree is a number or (op, left, right)."""
    if len(nums) == 1:
        return [(Fr(nums[0]), nums[0])]
    out = []
    for cut in range(1, len(nums)):
        for lv, lt in trees(nums[:cut]):
            for rv, rt in trees(nums[cut:]):
                for op in '+-*/':
                    if op == '+':
                        v = lv + rv
                    elif op == '-':
                        v = lv - rv
                    elif op == '*':
                        v = lv * rv
                    else:
                        if rv == 0:
                            continue
                        v = lv / rv
                    out.append((v, (op, lt, rt)))
    return out


def _spell(t, bracket_inner):
    """A tree written out. bracket_inner = set of ids of inner nodes that get brackets (the root never does)."""
    if isinstance(t, int):
        return str(t)
    op, l, r = t
    ls, rs = _spell(l, bracket_inner), _spell(r, bracket_inner)
    if not isinstance(l, int) and id(l) in bracket_inner:
        ls = f'({ls})'
    if not isinstance(r, int) and id(r) in bracket_inner:
        rs = f'({rs})'
    return f'{ls} {SHOW_OP[op]} {rs}'


def inner_nodes(t, root=True):
    if isinstance(t, int):
        return []
    out = [] if root else [t]
    return out + inner_nodes(t[1], False) + inner_nodes(t[2], False)


def sentences_for(numbers, target):
    """Every number sentence that uses each of `numbers` once (any order), with + − × ÷ and optional brackets, and works out (by normal order of operations) to the target.
    Written the usual way, with or without extra brackets that do not change the answer."""
    found = set()
    for perm in set(itertools.permutations(numbers)):
        for v, t in trees(list(perm)):
            if v != target:
                continue
            inner = inner_nodes(t)
            for mask in range(1 << len(inner)):
                chosen = {id(n) for k, n in enumerate(inner) if mask >> k & 1}
                s = _spell(t, chosen)
                try:
                    ok = value(s) == target       # the sentence as written, read with the normal order of operations, must still give the target
                except ZeroDivisionError:
                    ok = False
                if ok:
                    found.add(s)
    return sorted(found)


def sentence_uses(s, numbers):
    import re as _re
    return sorted(int(x) for x in _re.findall(r'\d+', s)) == sorted(numbers)


def chain_terms(a, b, count):
    out = [a, b]
    while len(out) < count:
        out.append(out[-1] + out[-2])
    return out


# ---------------------------------------------------------------- figures for lessons 3 and 4
def signs_figure(nums, total):
    """7 (o) 6 (o) 4 = 38 with an empty circle for each missing sign."""
    toks = []
    for i, n in enumerate(nums):
        toks.append(('n', n))
        if i < len(nums) - 1:
            toks.append(('c', None))
    toks += [('t', '='), ('n', total)]
    step = min(46, 296 / len(toks))
    W = int(step * len(toks) + 12)
    b, x = '', 6 + step / 2
    for kind, v in toks:
        if kind == 'c':
            b += Ci(x, 28, 16, '#fff', NAVY, 2.6)
        else:
            b += T(x, 38, v, 28)
        x += step
    return svg(W, 56, b, ' '.join(str(n) if k != 'c' else 'empty circle' for k, n in toks))


def machine_figure(first='?', last='30', mid=('× 6', '− 18', '÷ 4')):
    cells = [first] + list(mid) + [last]
    bw, gp = 52, 14
    W = len(cells) * bw + (len(cells) - 1) * gp + 12
    b = ''
    for i, c in enumerate(cells):
        x = 6 + i * (bw + gp)
        fill = YEL if i == 0 else ('#CDE8F7' if i == len(cells) - 1 else '#EDEDED')
        b += Re(x, 8, bw, 46, fill, NAVY, 2.6, 9) + T(x + bw / 2, 38, c, 20)
        if i < len(cells) - 1:
            b += Ln(x + bw + 1, 31, x + bw + gp - 3, 31, 2.4) + f'<polygon points="{x + bw + gp},31 {x + bw + gp - 7},26 {x + bw + gp - 7},36" fill="{NAVY}"/>'
    return svg(W, 62, b, 'Number machine chain: a number goes in, then ' + ', '.join(mid) + ', and ' + last + ' comes out.')


def hbrace(x1, x2, y, label='', above=True, size=15, gap=8):
    """A curly brace along a bar from x1 to x2; `above` puts it over the bar at height y (the bar edge), else under it. Label (may have two lines separated by |)."""
    s = -1 if above else 1
    m = (x1 + x2) / 2
    d = (f'M{x1} {y} Q{x1} {y + s * gap} {x1 + gap} {y + s * gap} L{m - gap} {y + s * gap} Q{m} {y + s * gap} {m} {y + s * (gap + 6)} '
         f'Q{m} {y + s * gap} {m + gap} {y + s * gap} L{x2 - gap} {y + s * gap} Q{x2} {y + s * gap} {x2} {y}')
    out = f'<path d="{d}" fill="none" stroke="{TEAL}" stroke-width="2.4" stroke-linecap="round"/>'
    lines = label.split('|') if label else []
    for k, ln in enumerate(lines):
        ty = (y + s * (gap + 12) - (len(lines) - 1 - k) * (size + 2)) if above else (y + gap + 6 + size + k * (size + 2))
        out += T(m, ty, ln, size, 'middle', 800, TEAL)
    return out


def vbrace(x, y1, y2, label='', size=15, gap=8):
    """A curly brace to the right of bars, from y1 to y2 at x; label written to its right."""
    m = (y1 + y2) / 2
    d = (f'M{x} {y1} Q{x + gap} {y1} {x + gap} {y1 + gap} L{x + gap} {m - gap} Q{x + gap} {m} {x + gap + 6} {m} Q{x + gap} {m} {x + gap} {m + gap} '
         f'L{x + gap} {y2 - gap} Q{x + gap} {y2} {x} {y2}')
    out = f'<path d="{d}" fill="none" stroke="{TEAL}" stroke-width="2.4" stroke-linecap="round"/>'
    for k, ln in enumerate(label.split('|') if label else []):
        out += T(x + gap + 12, m + 5 + (k - (len(label.split('|')) - 1) / 2) * (size + 2), ln, size, 'start', 800, TEAL)
    return out


def cells_row(x, y, n, w, h, shaded=0, fill=YEL, labels=None, size=14):
    b = ''
    for k in range(n):
        b += Re(x + k * w, y, w, h, fill if k < shaded else '#fff', NAVY, 2.4)
        if labels and labels.get(k):
            b += T(x + k * w + w / 2, y + h / 2 + 5, labels[k], size)
    return b


def bar_pair(top_name, top_units, bot_name, bot_units, brace_label, unit=44, labels_top=None, labels_bot=None, caption=''):
    """Two bars one above the other (e.g. laksa 1 unit, chicken rice 3 units) and a brace on the right for the total."""
    left = 84
    W = left + max(top_units, bot_units) * unit + 100
    b = T(left - 8, 34, top_name, 15, 'end') + cells_row(left, 12, top_units, unit, 36, top_units, '#CDE8F7', labels_top)
    b += T(left - 8, 82, bot_name, 15, 'end') + cells_row(left, 60, bot_units, unit, 36, bot_units, YEL, labels_bot)
    b += vbrace(left + max(top_units, bot_units) * unit + 8, 12, 96, brace_label)
    return svg(W, 108, b, caption or f'{top_name}: {top_units} equal box{"es" if top_units != 1 else ""}. {bot_name}: {bot_units} equal boxes. A brace on the right marks {brace_label.replace("|", " ")}.')


def money_model():
    """Mei's money: half on a book, $6 lunch, half of what was left on a gift, $9 left. Not to scale."""
    u = 18
    def seg(x, y, w, t, fill='#fff'):
        return Re(x, y, w, 34, fill, NAVY, 2.4) + T(x + w / 2, y + 22, t, 14)
    b = T(6, 14, 'All her money', 14, 'start', 800)
    b += seg(6, 20, 8 * u, 'book (half)', '#CDE8F7') + seg(6 + 8 * u, 20, 8 * u, 'the rest (half)')
    b += T(6 + 8 * u, 72, 'The rest', 14, 'start', 800)
    b += seg(6 + 8 * u, 78, 1.5 * u, '$6', YEL) + seg(6 + 9.5 * u, 78, 6.5 * u, 'what was left')
    b += T(6 + 9.5 * u, 130, 'What was left', 14, 'start', 800)
    b += seg(6 + 9.5 * u, 136, 3.25 * u, 'gift', '#CDE8F7') + seg(6 + 12.75 * u, 136, 3.25 * u, '$9 left', YEL)
    return svg(6 + 16 * u + 6, 178, b + T(6, 174, 'Not drawn to scale', 13, 'start', 600, '#44506F', True),
               'Not to scale. The whole bar is cut in two halves: the book and the rest. The rest is $6 for lunch and what was left. What was left is cut in two halves: the gift and $9 left.')


def beads_model(red_units, blue_units, caption, total_label):
    return bar_pair('Red', red_units, 'Blue', blue_units, total_label, unit=44, caption=caption)


def whole_bars(total_cells, per_bar, shaded_total):
    """Bars that are each one whole, cut in `per_bar` equal parts, stacked; the first `shaded_total` parts are shaded (as many bars as needed)."""
    nbars = -(-total_cells // per_bar)
    w = 52
    W = per_bar * w + 20
    b, k = '', 0
    for i in range(nbars):
        y = 10 + i * 48
        b += cells_row(10, y, per_bar, w, 36, max(0, min(per_bar, shaded_total - i * per_bar)))
    return svg(W, nbars * 48 + 14, b, f'{nbars} bars, each cut into {per_bar} equal parts. The first {shaded_total} parts are shaded.')


def quarter_line(arrows=(), cross=None, whole=3, parts=4):
    """A number line from 0 to `whole`, ticks every 1/parts. arrows: ((letter, quarters),...) drawn above; cross: a value (in wholes) marked with an X."""
    x0, u, y = 22, 84, 92
    W = x0 * 2 + whole * u + 6
    b = Ln(x0 - 10, y, x0 + whole * u + 12, y, 3)
    for q in range(whole * parts + 1):
        x = x0 + q * u / parts
        big = q % parts == 0
        b += Ln(x, y - (14 if big else 8), x, y + (14 if big else 8), 3.6 if big else 2.2)
        if big:
            b += T(x, y + 38, q // parts, 20)
    for letter, q in arrows:
        x = x0 + q * u / parts
        b += Ci(x, 20, 15, YEL, NAVY, 2.4) + T(x, 27, letter, 18) + Ln(x, 36, x, y - 22, 2.8, TEAL) + f'<polygon points="{x},{y - 14} {x - 6},{y - 26} {x + 6},{y - 26}" fill="{TEAL}"/>'
    if cross is not None:
        x = x0 + cross * u
        b += T(x, y - 14, '×', 34, 'middle', 800, WARM)
    return svg(W, 138, b, f'A number line from 0 to {whole} with a tick every quarter' + (', with arrows ' + ', '.join(a for a, _ in arrows) if arrows else '') + ('. An X marks 2 and 1 quarter.' if cross is not None else '.'))


def set_bar(parts, total_label):
    w = 34
    W = parts * w + 20
    return svg(W, 92, hbrace(10, 10 + parts * w, 40, total_label, True, 15) + cells_row(10, 46, parts, w, 36), f'A bar cut into {parts} equal parts. A brace over the whole bar is marked {total_label}.')


def compare_bars():
    x0, W = 62, 250
    b = ''
    for n, k, y in ((9, 4, 8), (8, 5, 58)):
        b += cells_row(x0, y, n, W / n, 38, k) + T(30, y + 25, f'{k}/{n}', 17, 'middle', 800)
    return svg(x0 + W + 10, 104, b, 'Two bars of the same length. The top bar is cut into 9 equal parts with 4 shaded. The bottom bar is cut into 8 equal parts with 5 shaded.')


def jar_bar():
    w = 52
    b = hbrace(10, 10 + 5 * w, 40, '? sweets in the jar', True, 15) + cells_row(10, 46, 5, w, 38, 3) + hbrace(10, 10 + 3 * w, 84, '27 red sweets', False, 15)
    return svg(5 * w + 20, 134, b, 'A bar for the jar cut into 5 equal parts. 3 parts are shaded and marked 27 red sweets. A brace over all 5 parts is marked with a question mark.')


def twelfths_strip():
    w = 24
    b = ''
    for i in range(12):
        b += Re(10 + i * w, 8, w, 36, '#fff', NAVY, 2.4) + T(10 + i * w + w / 2, 62, i + 1, 13, 'middle', 700, TEAL)
    return svg(12 * w + 20, 72, b, 'A strip of 12 equal boxes numbered 1 to 12.')


def beads_eighths():
    w = 34
    b = hbrace(10, 10 + 8 * w, 40, '40 beads', True, 15) + cells_row(10, 46, 8, w, 36, 3) + hbrace(10, 10 + 3 * w, 82, 'blue', False, 15)
    return svg(8 * w + 20, 124, b, 'A bar of 8 equal parts for 40 beads. 3 parts are shaded blue.')


def jar_halves_thirds():
    w = 270
    b = hbrace(10, 10 + w / 2, 40, 'Mei takes 1/2', True, 15) + hbrace(10 + 5 * w / 6, 10 + w, 40, '5 left', True, 15)
    b += Re(10, 46, w, 38, '#fff', NAVY, 2.4) + hbrace(10 + w / 2, 10 + 5 * w / 6, 84, 'Ali takes 1/3', False, 15)
    return svg(w + 20, 134, b, 'One undivided bar for the jar. A brace over the first half is Mei\'s one half, a brace under the next part is Ali\'s one third, and a brace at the end marks the 5 sweets left.')


def book_bar():
    w = 52
    b = hbrace(10, 10 + 5 * w, 50, '? pages in the book', True, 15) + cells_row(10, 56, 5, w, 38, 2, YEL, {0: 'Mon', 1: 'Mon'})
    b += hbrace(10 + 2 * w, 10 + 5 * w, 94, 'Tuesday: half of these.|45 pages still to read', False, 15)
    return svg(5 * w + 20, 160, b, 'A bar for the book cut into 5 equal parts. 2 parts are shaded for Monday. The other 3 parts are what was left. Tuesday takes half of those and 45 pages are still to read.')
