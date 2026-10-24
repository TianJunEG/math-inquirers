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


def trees(nums, ops='+-*/'):
    """Every way of putting the operations and brackets in a row of numbers: (value, tree) pairs. A tree is a number or (op, left, right)."""
    if len(nums) == 1:
        return [(Fr(nums[0]), nums[0])]
    out = []
    for cut in range(1, len(nums)):
        for lv, lt in trees(nums[:cut], ops):
            for rv, rt in trees(nums[cut:], ops):
                for op in ops:
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


def sentences_for(numbers, target, ops='+-*/'):
    """Every number sentence that uses each of `numbers` once (any order), with + − × ÷ and optional brackets, and works out (by normal order of operations) to the target.
    Written the usual way, with or without extra brackets that do not change the answer."""
    found = set()
    for perm in set(itertools.permutations(numbers)):
        for v, t in trees(list(perm), ops):
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
    wid = {'n': lambda v: 17 * len(str(v)) + 14, 'c': lambda v: 44, 't': lambda v: 34}
    W = int(sum(wid[k](v) for k, v in toks) + 12)
    b, x = '', 6
    for kind, v in toks:
        w = wid[kind](v)
        if kind == 'c':
            b += Ci(x + w / 2, 28, 16, '#fff', NAVY, 2.6)
        else:
            b += T(x + w / 2, 38, v, 28)
        x += w
    return svg(W, 56, b, ' '.join(str(n) if k != 'c' else 'empty circle' for k, n in toks))


def machine_figure(first='?', last='30', mid=('× 6', '− 18', '÷ 4')):
    cells = [first] + list(mid) + [last]
    bw, gp = 50, 18
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
    left = 98
    W = left + max(top_units, bot_units) * unit + 124
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


def jar_halves_thirds(left=5):
    w = 270
    b = hbrace(10, 10 + w / 2, 40, 'Mei takes 1/2', True, 15) + hbrace(10 + 5 * w / 6, 10 + w, 40, f'{left} left', True, 15)
    b += Re(10, 46, w, 38, '#fff', NAVY, 2.4) + hbrace(10 + w / 2, 10 + 5 * w / 6, 84, 'Ali takes 1/3', False, 15)
    return svg(w + 20, 134, b, f'One undivided bar for the jar. A brace over the first half is Mei\'s one half, a brace under the next part is Ali\'s one third, and a brace at the end marks the {left} sweets left.')


def book_bar():
    w = 52
    b = hbrace(10, 10 + 5 * w, 50, '? pages in the book', True, 15) + cells_row(10, 56, 5, w, 38, 2, YEL, {0: 'Mon', 1: 'Mon'})
    b += hbrace(10 + 2 * w, 10 + 5 * w, 94, 'Tuesday: half of these.|45 pages still to read', False, 15)
    return svg(5 * w + 20, 160, b, 'A bar for the book cut into 5 equal parts. 2 parts are shaded for Monday. The other 3 parts are what was left. Tuesday takes half of those and 45 pages are still to read.')


# ---------------------------------------------------------------- typed fractions and lists of fractions
def _terminating(d):
    while d % 2 == 0:
        d //= 2
    while d % 5 == 0:
        d //= 5
    return d == 1


def frac_text(f):
    f = Fr(f)
    return str(f.numerator) if f.denominator == 1 else f'{f.numerator}/{f.denominator}'


def mixed_text(f):
    f = Fr(f)
    w, r = divmod(f.numerator, f.denominator)
    if f.denominator == 1 or w == 0:
        return frac_text(f)
    return f'{w} {r}/{f.denominator}' if r else str(w)


def frac_accepts(f, simplest=False, maxk=12):
    """Accepted ways to type the number f: the fraction (and equal fractions n*k / d*k unless simplest), the mixed number, the decimal when it ends."""
    f = Fr(f)
    n, d = f.numerator, f.denominator
    forms = set()
    ks = [1] if simplest else range(1, maxk + 1)
    if d == 1:
        forms.add(str(n))
    else:
        for k in ks:
            forms.add(f'{n * k}/{d * k}')
            if n > d:
                w, r = divmod(n, d)
                if r:
                    forms.add(f'{w} {r * k}/{d * k}')
        if n > d and n % d == 0:
            forms.add(str(n // d))
        if _terminating(d):
            sdec = ('%.10f' % float(f)).rstrip('0').rstrip('.')
            forms.add(sdec)
            if sdec.startswith('0.'):
                forms.add(sdec[1:])
    return sorted(forms)


def joined_forms(parts, ordered=True):
    """A list typed as 'a, b, c' (comma, semicolon, space, 'and' before the last; with '<' too when ordered). All orders if not ordered.
    The first form in the returned list is the plain 'a, b, c' used as the printed answer."""
    orders = [list(parts)] if ordered else [list(p) for p in itertools.permutations(parts)]
    out = []
    for o in orders:
        seps = [', ', ';', ' ']
        if ordered:
            seps.append(' < ')
        for sp in seps:
            out.append(sp.join(o))
        if len(o) > 1:
            out.append(', '.join(o[:-1]) + ' and ' + o[-1])
    first = ', '.join(parts)
    return [first] + sorted(set(out) - {first})


# ---------------------------------------------------------------- end-of-lesson housekeeping (lesson-owned items only)
def finish(items, sol_px=250):
    """Every self-check item gets an explicit marking_mode ('open' only for a truly open prompt, 'self' for explanations and paper-only items),
    and solution figures get their text sized for the narrower solution box (a 360 px phone shows them about sol_px wide)."""
    import re as _re
    for it in items:
        if it.get('type') == 'selfcheck' and not it.get('marking_mode'):
            it['marking_mode'] = 'self'
        g = it.get('sol_fig')
        if g:
            def wrap(x, g=g):
                s = g(x)
                m = _re.search(r'viewBox="[-\d.]+ [-\d.]+ ([\d.]+) [\d.]+"', s)
                if not m:
                    return s
                need = round(12.0 / min(1.0, sol_px / float(m.group(1))), 1)
                return _re.sub(r'font-size="([\d.]+)"', lambda k: 'font-size="%g"' % max(float(k.group(1)), need), s)
            it['sol_fig'] = wrap
    return items


# ================================================================ WEEK 3 (lessons 5 and 6): decimals, then angles and turns
import math                                                     # noqa: E402
from decimal import Decimal as Dec, ROUND_HALF_UP               # noqa: E402


def dtext(x, dp=None):
    """A decimal as text. dp=None: the shortest writing (6.30 -> '6.3', 10.00 -> '10'); dp=2: exactly 2 decimal places ('6.30')."""
    x = Dec(str(x))
    if dp is None:
        return format(x.normalize(), 'f')
    return format(x.quantize(Dec(1).scaleb(-dp)), 'f')


def round_half_up(x, dp):
    """Round a decimal to dp places; exactly halfway rounds UP (the rule children are taught)."""
    return Dec(str(x)).quantize(Dec(1).scaleb(-dp), rounding=ROUND_HALF_UP)


def grid(lo, hi, dp):
    """Every decimal from lo to hi (inclusive) with dp decimal places, found by stepping one place at a time."""
    step, v, out = Dec(1).scaleb(-dp), Dec(str(lo)), []
    while v <= Dec(str(hi)):
        out.append(v); v += step
    return out


def dec_forms(x, pad=3, lead_dot=True):
    """How a child may write the decimal x: the shortest way first, then the same number with trailing zeros (6.3, 6.30, 6.300) and without the leading 0 (.247)."""
    x = Dec(str(x))
    base = dtext(x)
    mindp = len(base.split('.')[1]) if '.' in base else 0
    out = [dtext(x, dp) for dp in range(mindp, max(pad, mindp) + 1)]
    if base.startswith('0.') and lead_dot:
        out.append(base[1:])
    return list(dict.fromkeys(out))


def dec_accepts(x, pad=3, money=False, unit=None):
    """Accepted ways to type one decimal answer. money: $5.30, 5.30, $5.3, 5.3 and '5.30 dollars'. unit ('kg', 'm'): '0.4 kg', '0.4kg' as well."""
    x = Dec(str(x))
    nums = dec_forms(x, 2 if money else pad)
    if money:
        canon = '$' + dtext(x, 2)
        forms = [canon] + ['$' + n for n in nums] + nums + [n + ' dollars' for n in nums]
    elif unit:
        us = [unit] if isinstance(unit, str) else list(unit)
        forms = nums + [f'{n} {u}' for u in us for n in nums] + [f'{n}{u}' for u in us for n in nums]
    else:
        forms = nums
    return list(dict.fromkeys(forms))


def dec_list_accepts(vals, ordered=True, pad=3, lead_dot=False):
    """A list of decimals typed as 'a, b, c' (comma, semicolon, space, 'and' before the last; with '<' too when ordered). Each number may carry trailing zeros (3.5, 3.50, 3.500).
    The first form is the plain 'a, b, c'. ordered=False: any order."""
    vals = [Dec(str(v)) for v in vals]
    out = []
    orders = [vals] if ordered else [list(p) for p in itertools.permutations(vals)]
    for o in orders:
        per = [dec_forms(v, pad, lead_dot) for v in o]
        for combo in itertools.product(*per):
            seps = [', ', ';', ' '] + ([' < '] if ordered else [])
            for sp in seps:
                out.append(sp.join(combo))
            if len(combo) > 1:
                out.append(', '.join(combo[:-1]) + ' and ' + combo[-1])
    out = list(dict.fromkeys(out))
    assert len(out) < 6000, len(out)
    return out


def between_forms(lo, hi, dps=(3, 4, 5)):
    """Every decimal strictly between lo and hi with at most max(dps) decimal places, in the shortest writing and (for 3 and 4 places) with trailing zeros."""
    lo, hi = Dec(str(lo)), Dec(str(hi))
    out = []
    for dp in range(min(dps), max(dps) + 1):
        for v in grid(lo, hi, dp):
            if lo < v < hi:
                out.append(dtext(v))
    return list(dict.fromkeys(out))


# ---------------------------------------------------------------- figures for lesson 5
def dec_line(lo, hi, arrows=(), label=''):
    """A number line cut into 10 equal steps; the two ends and the middle are labelled. arrows: ((letter, steps from the left end), ...), steps may be 8.5."""
    lo, hi = Dec(str(lo)), Dec(str(hi))
    x0, x1, y = 40, 300, 96
    k = (x1 - x0) / 10
    b = Ln(x0 - 14, y, x1 + 14, y, 3)
    for i in range(11):
        big = i in (0, 5, 10)
        b += Ln(x0 + i * k, y - (13 if big else 8), x0 + i * k, y + (13 if big else 8), 3.4 if big else 2)
    for i, v in ((0, lo), (5, (lo + hi) / 2), (10, hi)):
        b += T(x0 + i * k, y + 36, dtext(v), 16, 'middle', 700)
    for letter, st in arrows:
        x = round(x0 + float(Dec(str(st))) * k, 1)
        b += Ci(x, 20, 14, YEL, NAVY, 2.4) + T(x, 27, letter, 17) + Ln(x, 35, x, y - 26, 2.8, TEAL) + f'<polygon points="{x},{y - 15} {x - 6},{y - 27} {x + 6},{y - 27}" fill="{TEAL}"/>'
    return svg(340, 140, b, label or f'A number line from {dtext(lo)} to {dtext(hi)} cut into 10 equal steps, with the two ends and the middle labelled' + (', and arrows ' + ', '.join(a for a, _ in arrows) if arrows else '') + '.')


def round_line():
    x0, x1, y = 30, 310, 40
    k = (x1 - x0) / 20
    b = Ln(x0 - 12, y, x1 + 12, y, 3)
    for i in range(21):
        big = i % 10 == 0
        b += Ln(x0 + i * k, y - (14 if big else 8), x0 + i * k, y + (14 if big else 8), 4 if big else 2)
        if big:
            b += T(x0 + i * k, y + 36, f'7.{3 + i // 10}', 16)
    b += Ci(x0 + 10 * k, y, 9, YEL, NAVY, 3)
    return svg(340, 86, b, 'A number line from 7.30 to 7.50 marked in hundredths, with 7.3, 7.4 and 7.5 labelled and a dot at 7.4.')


def dec_cards(items):
    """Digit cards; the string '.' is drawn as the decimal point card."""
    w, gp = 46, 12
    W = len(items) * w + (len(items) - 1) * gp + 12
    b = ''
    for i, d in enumerate(items):
        x = 6 + i * (w + gp)
        if d == '.':
            b += Re(x, 6, w, 62, '#fff', NAVY, 2.6, 9) + Ci(x + w / 2, 46, 5.5, NAVY, NAVY, 1) + T(x + w / 2, 24, 'point', 13, 'middle', 700, TEAL)
        else:
            b += Re(x, 6, w, 62, YEL, NAVY, 2.6, 9) + T(x + w / 2, 49, d, 34)
    names = ', '.join('a decimal point card' if d == '.' else str(d) for d in items)
    return svg(W, 76, b, 'Cards: ' + names)


def money_bars(top_name, bot_name, units, extra_units, extra_label, total_label, unit=44):
    """Two bars: the top bar is `units` equal parts, the bottom bar the same plus an extra shaded part (labelled); a brace on the right marks the total."""
    left = 74
    b = T(left - 8, 36, top_name, 15, 'end') + cells_row(left, 12, units, unit, 36, units, '#CDE8F7')
    b += T(left - 8, 84, bot_name, 15, 'end') + cells_row(left, 60, units, unit, 36, units, YEL) + cells_row(left + units * unit, 60, extra_units, unit, 36, extra_units, '#F2B8A2')
    b += hbrace(left + units * unit, left + (units + extra_units) * unit, 96, extra_label, False, 15)
    b += vbrace(left + (units + extra_units) * unit + 8, 12, 96, total_label)
    return svg(left + (units + extra_units) * unit + 76, 136, b,
               f'Two bars. {top_name} has {units} equal parts. {bot_name} has the same {units} parts and one more shaded part marked {extra_label}. A brace on the right marks {total_label} altogether.')


def three_money_bars():
    """Ali: 3 units. Ben: 3 units + $0.50. Siti: Ben's bar + $1.30 more. A brace on the right marks $9.20."""
    u, left = 36, 56
    def row(y, name, parts):
        s, x = T(left - 8, y + 24, name, 15, 'end'), left
        for w, fill in parts:
            s += Re(x, y, w * u, 32, fill, NAVY, 2.4)
            x += w * u
        return s, x
    b, e1 = row(10, 'Ali', [(3, '#CDE8F7')])
    s, e2 = row(80, 'Ben', [(3, '#CDE8F7'), (0.8, '#F2B8A2')])
    b += s
    s, e3 = row(150, 'Siti', [(3, '#CDE8F7'), (0.8, '#F2B8A2'), (1.8, '#FFE08A')])
    b += s
    b += hbrace(left + 3 * u, left + 3.8 * u, 112, '$0.50 more than Ali', False, 15)
    b += hbrace(left + 3.8 * u, left + 5.6 * u, 182, '$1.30 more than Ben', False, 15)
    b += vbrace(left + 5.6 * u + 8, 10, 182, '$9.20')
    return svg(left + 5.6 * u + 80, 232, b, 'Three bars. Ali has a bar of 3 equal parts. Ben has the same bar and an extra part marked 50 cents more than Ali. Siti has Ben\'s bar and an extra part marked $1.30 more than Ben. A brace on the right marks $9.20 altogether.')


def can_scales():
    def scale(cx, title, reading, cans):
        s = T(cx, 18, title, 15, 'middle', 800, TEAL) + Re(cx - 62, 32, 124, 66, '#fff', NAVY, 2.6, 6)
        for i in range(cans):
            x, y = cx - 56 + (i % 3) * 38, 38 + (i // 3) * 28
            s += Re(x, y, 34, 24, '#E58C6B', NAVY, 2, 4) + Ln(x, y + 12, x + 34, y + 12, 1.6, '#fff')
        s += Re(cx - 76, 98, 152, 42, SKY, NAVY, 2.6, 8) + Re(cx - 46, 106, 92, 26, '#fff', NAVY, 2, 4) + T(cx, 125, reading, 16)
        return s
    return svg(340, 150, scale(90, 'box with 6 cans', '2.85 kg', 6) + scale(250, 'empty box', '0.45 kg', 0),
               'A box with 6 cans on a scale reads 2.85 kilograms. The empty box on a scale reads 0.45 kilograms.')


def can_bar():
    w = 48
    b = hbrace(10, 10 + 6 * w, 44, 'all 6 cans together', True, 15)
    for i in range(6):
        b += Re(10 + i * w, 44, w, 40, '#fff', NAVY, 2.6) + T(10 + i * w + w / 2, 69, 'can', 14, 'middle', 700, '#44506F')
    return svg(6 * w + 20, 96, b, 'A bar cut into 6 equal parts, one part for each can. The whole bar is the mass of all 6 cans together.')


def jugs():
    def jug(cx, level, cap, kg):
        top, h, w = 14, 100, 70
        s = Re(cx - w / 2, top, w, h, '#fff', NAVY, 3.2, 4)
        lv = level * h
        s += Re(cx - w / 2 + 2, top + h - lv, w - 4, lv - 2, '#BFE3F5', 'none', 0)
        s += f'<path d="M{cx + w / 2} {top + 18} q22 0 22 22 q0 22 -22 22" fill="none" stroke="{NAVY}" stroke-width="3.2"/>'
        return s + T(cx, top + h + 24, cap, 15, 'middle', 800) + T(cx, top + h + 46, 'scale reads ' + kg, 15, 'middle', 800, TEAL)
    return svg(340, 190, jug(86, 0.94, 'jug full of water', '1.45 kg') + jug(256, 0.5, 'jug half full', '0.85 kg'),
               'Two jugs. The first is full of water and the scale reads 1.45 kilograms. The second is half full and the scale reads 0.85 kilograms.')


# ---------------------------------------------------------------- figures for lesson 6
def _pt(cx, cy, r, deg):
    return cx + r * math.cos(math.radians(deg)), cy - r * math.sin(math.radians(deg))


def _arc(cx, cy, r, d0, d1, c=TEAL, w=2.5):
    a, b = _pt(cx, cy, r, d0), _pt(cx, cy, r, d1)
    return f'<path d="M{a[0]:.1f} {a[1]:.1f} A{r} {r} 0 {1 if d1 - d0 > 180 else 0} 0 {b[0]:.1f} {b[1]:.1f}" fill="none" stroke="{c}" stroke-width="{w}"/>'


def _ray(cx, cy, r, deg, w=3, c=NAVY):
    x, y = _pt(cx, cy, r, deg)
    return Ln(round(cx, 1), round(cy, 1), round(x, 1), round(y, 1), w, c)


# the four angles of Q1 (arms from d0 to d1 in maths degrees, arm length r): the size is d1 - d0
FOUR = {'a': (0, 40, 78), 'b': (20, 135, 66), 'c': (200, 275, 66), 'd': (12, 162, 66)}


def _panel(px, py, pw, ph, d0, d1, r, name, title=''):
    pts = [(0, 0), _pt(0, 0, r, d0), _pt(0, 0, r, d1)]
    xs, ys = [p[0] for p in pts], [p[1] for p in pts]
    cx, cy = px + pw / 2 - (min(xs) + max(xs)) / 2, py + ph / 2 - (min(ys) + max(ys)) / 2 + (8 if title else 0)
    lab = _pt(cx, cy, 50, (d0 + d1) / 2)
    s = _ray(cx, cy, r, d0) + _ray(cx, cy, r, d1) + _arc(cx, cy, 28, d0, d1) + T(round(lab[0], 1), round(lab[1] + 6, 1), name, 20, 'middle', 800, TEAL)
    s += Ci(round(cx, 1), round(cy, 1), 3.5, NAVY, NAVY, 1)
    if title:
        s += T(px + 10, py + 22, title, 17, 'start', 800, WARM)
    return s


def four_angles(sizes=False):
    """The four angles of Q1, drawn to size. sizes=True: the measured size is written in each corner of the panel (for the answer picture)."""
    pw, ph = 170, 150
    b = Re(2, 2, 2 * pw - 4, 2 * ph - 4, '#fff', '#C9D4EC', 2, 10) + Ln(pw, 8, pw, 2 * ph - 8, 2, '#C9D4EC') + Ln(8, ph, 2 * pw - 8, ph, 2, '#C9D4EC')
    for k, name in enumerate('abcd'):
        d0, d1, r = FOUR[name]
        b += _panel((k % 2) * pw, (k // 2) * ph, pw, ph, d0, d1, r, name, f'{name} = {d1 - d0}°' if sizes else '')
    return svg(2 * pw, 2 * ph, b, ('Four angles drawn to size. ' + ', '.join(f'{n} is {FOUR[n][1] - FOUR[n][0]} degrees' for n in 'abcd') if sizes else 'Four angles drawn to size: a, b, c and d.'))


FAN = [(0, 'A'), (30, 'B'), (90, 'C'), (135, 'D')]


def fan_figure():
    O, R = (112, 172), 132
    b = ''
    for d, n in FAN:
        q = _pt(O[0], O[1], R + 17, d)
        b += _ray(O[0], O[1], R, d) + T(round(q[0], 1), round(q[1] + 7, 1), n, 20, 'middle', 800)
    b += _arc(O[0], O[1], 98, 0, 30) + _arc(O[0], O[1], 48, 30, 90) + _arc(O[0], O[1], 72, 90, 135)
    for ang, rr, txt, dx in ((15, 114, '30°', 4), (60, 70, '60°', 6), (112.5, 92, '45°', -4)):
        q = _pt(O[0], O[1], rr, ang)
        b += T(round(q[0] + dx, 1), round(q[1] + 6, 1), txt, 16, 'middle', 800, TEAL)
    b += Ci(O[0], O[1], 4, NAVY, NAVY, 1) + T(O[0] - 8, O[1] + 24, 'O', 19)
    return svg(290, 200, b, 'Four rays OA, OB, OC and OD from one point O. The angle between OA and OB is 30 degrees, between OB and OC is 60 degrees, and between OC and OD is 45 degrees.')


def _cpt(cx, cy, L, theta):
    """A point at distance L from (cx, cy), theta degrees clockwise from 12 o'clock."""
    return cx + L * math.sin(math.radians(theta)), cy - L * math.cos(math.radians(theta))


def _clock(cx, cy, r, h, m, hands, shade, cap):
    s = Ci(cx, cy, r, '#fff', NAVY, 3)
    if shade:
        t0, t1 = shade
        a, b = _cpt(cx, cy, r * 0.62, t0), _cpt(cx, cy, r * 0.62, t1)
        s += f'<path d="M{cx} {cy} L{a[0]:.1f} {a[1]:.1f} A{r * 0.62:.1f} {r * 0.62:.1f} 0 {1 if t1 - t0 > 180 else 0} 1 {b[0]:.1f} {b[1]:.1f} Z" fill="{YEL}" fill-opacity="0.7" stroke="{WARM}" stroke-width="1.6"/>'
    for i in range(12):
        a, b = _cpt(cx, cy, r, 30 * i), _cpt(cx, cy, r - 6, 30 * i)
        s += Ln(round(a[0], 1), round(a[1], 1), round(b[0], 1), round(b[1], 1), 2)
        q = _cpt(cx, cy, r - 17, 30 * i)
        s += T(round(q[0], 1), round(q[1] + 4.5, 1), 12 if i == 0 else i, 13, 'middle', 700)
    if hands:
        hh, mm = _cpt(cx, cy, r * 0.5, 30 * (h % 12) + m / 2), _cpt(cx, cy, r * 0.76, 6 * m)
        s += Ln(cx, cy, round(hh[0], 1), round(hh[1], 1), 5, TEAL) + Ln(cx, cy, round(mm[0], 1), round(mm[1], 1), 3.4, NAVY)
    s += Ci(cx, cy, 4, NAVY, NAVY, 1)
    if cap:
        s += T(cx, cy + r + 24, cap, 15, 'middle', 800, TEAL)
    return s


def smaller_sector(h, m=0):
    """(from, to) in degrees clockwise from 12 for the smaller angle between the two hands."""
    a, b = sorted([30 * (h % 12) + m / 2, 6 * m])
    return (a, b) if b - a <= 180 else (b, a + 360)


def clocks(specs, r=66, label=''):
    """specs: dicts(h, m, hands=True, shade=False, cap=''). One svg with the clocks side by side."""
    n = len(specs)
    cw = 2 * r + 28
    b = ''
    desc = []
    for k, sp in enumerate(specs):
        cx = cw * k + cw / 2
        h, m, hands = sp.get('h', 12), sp.get('m', 0), sp.get('hands', True)
        sh = smaller_sector(h, m) if sp.get('shade') else None
        b += _clock(cx, r + 8, r, h, m, hands, sh, sp.get('cap', ''))
        desc.append((f'{h}:{m:02d}' if m else f'{h} o\'clock') if hands else 'a blank clock face')
    return svg(cw * n, 2 * r + 40, b, label or ('Clock faces showing ' + ' and '.join(desc) + '.'))


DIRS = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']      # clockwise from the top


def compass(hi=(), s=1.25):
    c = (120 * s, 110 * s)
    def P(r, mdeg):
        return _pt(c[0], c[1], r * s, mdeg)
    b = Ci(c[0], c[1], 84 * s, SKY, NAVY, 2.6)
    for i, n in enumerate(DIRS):
        md = 90 - 45 * i
        main = i % 2 == 0
        a = P(84, md)
        b += Ln(round(c[0], 1), round(c[1], 1), round(a[0], 1), round(a[1], 1), 3.4 if main else 2, NAVY if main else '#6F7FA3')
        q = P(104 if main else 103, md)
        if n in hi:
            b += Ci(round(q[0], 1), round(q[1], 1), (19 if main else 22) * s * 0.9, YEL, NAVY, 2)
        b += T(round(q[0], 1), round(q[1] + 8 * s, 1), n, round((26 if main else 22) * s * 0.85, 1), 'middle', 800 if main else 700, NAVY if main else TEAL)
    a0, a1 = P(66, -10 - 0), P(66, -50)
    b += f'<path d="M{a0[0]:.1f} {a0[1]:.1f} A{66 * s:.1f} {66 * s:.1f} 0 0 1 {a1[0]:.1f} {a1[1]:.1f}" fill="none" stroke="{TEAL}" stroke-width="3.6"/>'
    tip, b1, b2 = P(66, -58), P(74, -44), P(58, -44)
    b += f'<polygon points="{tip[0]:.1f},{tip[1]:.1f} {b1[0]:.1f},{b1[1]:.1f} {b2[0]:.1f},{b2[1]:.1f}" fill="{TEAL}"/>'
    b += _arc(c[0], c[1], 40 * s, 45, 90, WARM, 3.2)
    q = P(58, 67.5)
    b += T(round(q[0], 1), round(q[1] + 6, 1), '45°', round(17 * s * 0.85, 1), 'middle', 800, WARM)
    b += Ci(c[0], c[1], 6, YEL, NAVY, 2.5) + T(c[0], 246 * s, 'clockwise: like clock hands', 15, 'middle', 700, TEAL)
    return svg(round(240 * s), round(254 * s), b, 'An 8-point compass rose: N at the top, then NE, E, SE, S, SW, W, NW going clockwise. One step from a direction to the next is 45 degrees. An arrow shows the clockwise way.')


def rect_corner(a_known=58):
    A = (28, 24)
    t = math.radians(90 - a_known)         # the line makes (90 - a_known) degrees with the top side
    end = (178, 24 + 150 * math.tan(t))
    b = Re(28, 24, 150, 112, SKY, NAVY, 3) + Ln(A[0], A[1], round(end[0], 1), round(end[1], 1), 3.2)
    b += _arc(A[0], A[1], 36, -90, -(90 - a_known), TEAL) + _arc(A[0], A[1], 36, -(90 - a_known), 0, TEAL)
    q = _pt(A[0], A[1], 66, -(90 - (90 - a_known) / 2) + 0)
    q1 = _pt(A[0], A[1], 64, -(90 - a_known) - a_known / 2)
    q2 = _pt(A[0], A[1], 92, -(90 - a_known) / 2)
    b += T(round(q1[0] + 4, 1), round(q1[1] + 6, 1), f'{a_known}°', 17, 'middle', 800, TEAL) + T(round(q2[0], 1), round(q2[1] + 6, 1), 'a', 19, 'middle', 800, TEAL)
    return svg(210, 150, b, f'A rectangle with a line from its top left corner. The angle between the left side and the line is {a_known} degrees. Angle a is between the line and the top side.')


def square_corner(x1=15, x2=48):
    B = (28, 150)
    b = Re(28, 10, 140, 140, SKY, NAVY, 3)
    for ang in (x1, 90 - x2):
        e = (168, 150 - 140 * math.tan(math.radians(ang)))
        b += Ln(B[0], B[1], 168, round(e[1], 1), 3.2)
    b += _arc(B[0], B[1], 62, 0, x1) + _arc(B[0], B[1], 44, x1, 90 - x2) + _arc(B[0], B[1], 30, 90 - x2, 90)
    for ang, rr, txt in ((x1 / 2, 92, f'{x1}°'), ((x1 + 90 - x2) / 2, 66, 'b'), ((90 - x2 + 90) / 2, 50, f'{x2}°')):
        q = _pt(B[0], B[1], rr, ang)
        b += T(round(q[0], 1), round(q[1] + 6, 1), txt, 17, 'middle', 800, TEAL)
    return svg(210, 162, b, f'A square. Two lines from its bottom left corner make three angles: {x1} degrees, angle b, and {x2} degrees.')


def overlap_figure(outer=160):
    O, S = (130, 150), 96
    def poly(d0):
        pts = [O, _pt(O[0], O[1], S, d0), _pt(O[0], O[1], S * math.sqrt(2), d0 + 45), _pt(O[0], O[1], S, d0 + 90)]
        return ' '.join(f'{x:.1f},{y:.1f}' for x, y in pts)
    s2 = outer - 90
    b = f'<polygon points="{poly(0)}" fill="{SKY}" stroke="{NAVY}" stroke-width="3"/><polygon points="{poly(s2)}" fill="{YEL}" fill-opacity="0.5" stroke="{NAVY}" stroke-width="3"/>'
    b += _arc(O[0], O[1], 34, s2, 90, WARM, 3) + _arc(O[0], O[1], 72, 0, outer, TEAL, 3)
    a, c = _pt(O[0], O[1], 34, (s2 + 90) / 2), _pt(O[0], O[1], 112, (s2 + 90) / 2)
    b += Ln(round(a[0], 1), round(a[1], 1), round(c[0], 1), round(c[1], 1), 2, WARM)
    q = _pt(O[0], O[1], 128, (s2 + 90) / 2)
    b += T(round(q[0], 1), round(q[1] + 8, 1), '?', 26, 'middle', 800, WARM)
    q = _pt(O[0], O[1], 48, outer * 0.88)
    b += T(round(q[0], 1), round(q[1] + 5, 1), f'{outer}°', 16, 'middle', 800, TEAL) + Ci(O[0], O[1], 3.5, NAVY, NAVY, 1) + T(O[0] + 12, O[1] + 20, 'O', 17)
    return svg(270, 176, b, f'Two squares share the corner O and overlap. The angle between their outside sides is {outer} degrees. The angle where they overlap is marked with a question mark.')


def right_corner():
    O = (50, 120)
    b = _ray(O[0], O[1], 100, 0) + _ray(O[0], O[1], 100, 90) + Re(O[0], O[1] - 16, 16, 16, 'none', TEAL, 2.4) + T(O[0] + 36, O[1] - 30, '90°', 17, 'middle', 800, TEAL)
    return svg(180, 140, b, 'A square corner, a right angle of 90 degrees.')


def combine(figs, label, gap=10, target=340):
    """Several svg figures one above the other as ONE svg (the runner shows one svg per question). A figure wider than `target` is scaled down to it
    (its text is lifted first, so it is still readable on a phone); the others keep their size and are centred."""
    import re as _re
    parts = []
    for f in figs:
        root = _re.match(r'<svg[^>]*>', f).group(0)
        vb = [float(v) for v in _re.search(r'viewBox="([\d. -]+)"', root).group(1).split()]
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
    return svg(W, y - gap, body, label)


# ================================================================ WEEK 4 (lessons 7 and 8): area and perimeter, then symmetry and nets
GRIDC = '#C9D4EC'
RED = WARM


def gridlines(x0, y0, cols, rows, c, col=GRIDC, sw=1):
    d = ''.join(f'M{x0 + i * c:g} {y0:g}V{y0 + rows * c:g}' for i in range(cols + 1)) + ''.join(f'M{x0:g} {y0 + j * c:g}H{x0 + cols * c:g}' for j in range(rows + 1))
    return f'<path d="{d}" stroke="{col}" stroke-width="{sw}" fill="none"/>'


def ppoly(pts, c, x0, y0, fill=SKY, sw=3, dash=None, stroke=NAVY):
    p = ' '.join(f'{x0 + a * c:g},{y0 + b * c:g}' for a, b in pts)
    return f'<polygon points="{p}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round"' + (f' stroke-dasharray="{dash}"' if dash else '') + '/>'


def poly_area(pts):
    """Shoelace formula (INDEPENDENT of any 'split' or 'take away' method)."""
    s = sum(x1 * y2 - x2 * y1 for (x1, y1), (x2, y2) in zip(pts, pts[1:] + pts[:1]))
    return abs(s) / 2


def poly_perimeter(pts):
    return sum(abs(x2 - x1) + abs(y2 - y1) for (x1, y1), (x2, y2) in zip(pts, pts[1:] + pts[:1]))      # all sides are horizontal or vertical


def poly_cells(pts):
    """The unit cells (x, y) inside a rectilinear polygon with whole-number corners (tested at the centre of each cell by ray casting)."""
    xs, ys = [p[0] for p in pts], [p[1] for p in pts]
    out = set()
    for x in range(min(xs), max(xs)):
        for y in range(min(ys), max(ys)):
            cx, cy, inside = x + 0.5, y + 0.5, False
            for (x1, y1), (x2, y2) in zip(pts, pts[1:] + pts[:1]):
                if x1 == x2 and x1 > cx and min(y1, y2) < cy < max(y1, y2):
                    inside = not inside
            if inside:
                out.add((x, y))
    return out


def is_rect(cells):
    if not cells:
        return False
    xs, ys = [c[0] for c in cells], [c[1] for c in cells]
    return len(cells) == (max(xs) - min(xs) + 1) * (max(ys) - min(ys) + 1)


def rect_splits(cells):
    """Every way to cut a shape of unit cells into exactly two rectangles with ONE straight cut along a grid line: [((w1, h1), (w2, h2)), ...]."""
    xs, ys = [c[0] for c in cells], [c[1] for c in cells]
    out = []
    for k in range(min(xs) + 1, max(xs) + 1):
        a, b = {c for c in cells if c[0] < k}, {c for c in cells if c[0] >= k}
        if is_rect(a) and is_rect(b):
            out.append((dims_of(a), dims_of(b)))
    for k in range(min(ys) + 1, max(ys) + 1):
        a, b = {c for c in cells if c[1] < k}, {c for c in cells if c[1] >= k}
        if is_rect(a) and is_rect(b):
            out.append((dims_of(a), dims_of(b)))
    return out


def dims_of(cells):
    xs, ys = [c[0] for c in cells], [c[1] for c in cells]
    return (max(xs) - min(xs) + 1, max(ys) - min(ys) + 1)


def rectangles_with_area(area):
    """Whole-number rectangles (shorter side first) with this area, found by trying every length."""
    return [(a, area // a) for a in range(1, area + 1) if area % a == 0 and a <= area // a]


def rectangles_with_perimeter(per):
    return [(a, per // 2 - a) for a in range(1, per // 2) if a <= per // 2 - a]


def polyominoes(n):
    """All fixed polyominoes of n unit squares joined edge to edge (whole sides touching), as frozensets of cells."""
    cur = {frozenset([(0, 0)])}
    for _ in range(n - 1):
        nxt = set()
        for p in cur:
            for (x, y) in p:
                for q in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                    if q not in p:
                        s = set(p) | {q}
                        mx, my = min(a for a, _ in s), min(b for _, b in s)
                        nxt.add(frozenset((a - mx, b - my) for a, b in s))
        cur = nxt
    return cur


def cells_perimeter(cells):
    """Count the unit edges that have a square on one side only."""
    cells = set(cells)
    return sum(1 for (x, y) in cells for q in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)) if q not in cells)


def x_forms(a, b, flip=True):
    """Typed writings of a rectangle 'a by b' (the shared matcher ignores case and spaces and reads x, X and the times sign alike)."""
    out = []
    for p, q in ([(a, b), (b, a)] if flip else [(a, b)]):
        out += [f'{p} by {q}', f'{p}x{q}', f'{p} cm by {q} cm', f'{p}cm x {q}cm', f'{p}cm by {q}cm', f'{p} by {q} cm', f'{p}x{q} cm', f'{p} cm x {q} cm']
    return out


def sum_sentences(parts, sign, result):
    """Number sentences for an area: parts = [(w, h), (w, h)], sign '+' (split) or '-' (big rectangle take away the piece).
    The factors may be in either order, the two parts in either order for '+', with or without brackets, with the products written out, with or without '= result'."""
    import itertools as it
    out = []
    orders = list(it.permutations(parts)) if sign == '+' else [tuple(parts)]
    for o in orders:
        for fa in ((o[0][0], o[0][1]), (o[0][1], o[0][0])):
            for fb in ((o[1][0], o[1][1]), (o[1][1], o[1][0])):
                a, b = f'{fa[0]}x{fa[1]}', f'{fb[0]}x{fb[1]}'
                out += [f'{a}{sign}{b}', f'({a}){sign}({b})']
        pa, pb = o[0][0] * o[0][1], o[1][0] * o[1][1]
        out.append(f'{pa}{sign}{pb}')
    return list(dict.fromkeys(out))


def perm_accepts(tokens, seps=(', ', ' ', ' and ', '; ', ',')):
    """Typed lists of the given tokens in any order: 'A, C, E', 'C A E', 'E and A and C' ..."""
    out = []
    for p in itertools.permutations(tokens):
        for s in seps:
            out.append(s.join(p))
        out.append(', '.join(p[:-1]) + ' and ' + p[-1] if len(p) > 1 else p[0])
    return list(dict.fromkeys(out))


# ---------------------------------------------------------------- figures for lesson 7
def l_poly(W=9, H=7, cw=5, ch=3):
    """An L-shape: W by H with a cw by ch piece missing from the top right."""
    return [(0, 0), (W - cw, 0), (W - cw, ch), (W, ch), (W, H), (0, H)]


def l_shape_fig(W=9, H=7, cw=5, ch=3, label=''):
    c = 20 if W <= 10 else 16
    x0, y0 = 54, 24
    pts = l_poly(W, H, cw, ch)
    b = gridlines(x0, y0, W, H, c) + ppoly(pts, c, x0, y0)
    b += T(x0 + (W - cw) * c / 2, y0 - 7, f'{W - cw} cm', 16) + T(x0 - 8, y0 + H * c / 2 + 5, f'{H} cm', 16, 'end')
    b += T(x0 + W * c / 2, y0 + H * c + 20, f'{W} cm', 16) + T(x0 + W * c + 8, y0 + (ch + H) * c / 2 + 5, f'{H - ch} cm', 16, 'start')
    b += T(x0 + (W - cw / 2) * c, y0 + ch * c - 7, 'a', 20, 'middle', 800, RED) + T(x0 + (W - cw) * c + 9, y0 + ch * c / 2 + 6, 'b', 20, 'start', 800, RED)
    return svg(x0 + W * c + 60, y0 + H * c + 30, b, label or (f'An L-shaped figure on a 1 cm grid with only square corners: top {W - cw} cm, left side {H} cm, bottom {W} cm and right side {H - ch} cm. '
                                                              'The two step sides are marked a (across) and b (down).'))


def stair_poly(w=11, r=2):
    ws = [w - 8, w - 4, w]
    return [(0, 0), (ws[0], 0), (ws[0], r), (ws[1], r), (ws[1], 2 * r), (ws[2], 2 * r), (ws[2], 3 * r), (0, 3 * r)]


def stair_fig(w=11, r=2, label=''):
    c = 18 if w <= 11 else 15
    x0, y0 = 54, 8
    pts = stair_poly(w, r)
    b = gridlines(x0, y0, w, 3 * r, c) + ppoly(pts, c, x0, y0) + T(x0 + w * c / 2, y0 + 3 * r * c + 20, f'{w} cm', 16) + T(x0 - 8, y0 + 3 * r * c / 2 + 5, f'{3 * r} cm', 16, 'end')
    return svg(x0 + w * c + 12, y0 + 3 * r * c + 28, b, label or f'A staircase figure with three steps on a 1 cm grid, {w} cm along the bottom and {3 * r} cm up the left side.')


def cut_rect_fig(a=8, b_=2):
    c = 30
    x0, y0 = 40, 14
    b = gridlines(x0, y0, a, b_, c) + ppoly([(0, 0), (a, 0), (a, b_), (0, b_)], c, x0, y0)
    b += Ln(x0 + a * c / 2, y0 - 8, x0 + a * c / 2, y0 + b_ * c + 8, 3.5, RED, '9 6') + T(x0 + a * c / 2 + 8, y0 + 18, 'cut', 16, 'start', 800, RED)
    b += T(x0 + a * c / 2, y0 + b_ * c + 28, f'{a} cm', 16) + T(x0 - 8, y0 + b_ * c / 2 + 5, f'{b_} cm', 16, 'end')
    return svg(x0 + a * c + 24, y0 + b_ * c + 38, b, f'A {a} cm by {b_} cm rectangle on a grid with a dashed cut line down the middle.')


def square_from_pieces_fig(s=4):
    c = 30
    x0, y0 = 8, 10
    h = s // 2
    b = gridlines(x0, y0, s, s, c) + ppoly([(0, 0), (s, 0), (s, h), (0, h)], c, x0, y0, SKY) + ppoly([(0, h), (s, h), (s, s), (0, s)], c, x0, y0, YEL)
    b += T(x0 + s * c / 2, y0 + h * c / 2 + 6, 'piece 1', 16) + T(x0 + s * c / 2, y0 + (s - h / 2) * c + 6, 'piece 2', 16) + T(x0 + s * c / 2, y0 + s * c + 22, f'{s} cm', 16)
    b += T(x0 + s * c + 8, y0 + s * c / 2 + 5, f'{s} cm', 16, 'start')
    return svg(x0 + s * c + 62, y0 + s * c + 32, b, f'The two pieces put together make a square, {s} cm by {s} cm.')


def frame_fig(L=8, W=6, w=1, label=''):
    c = max(10, min(20, 220 // (L + 2 * w)))
    x0, y0 = 10, 8
    b = gridlines(x0, y0, L + 2 * w, W + 2 * w, c) + ppoly([(0, 0), (L + 2 * w, 0), (L + 2 * w, W + 2 * w), (0, W + 2 * w)], c, x0, y0, YEL) + ppoly([(w, w), (L + w, w), (L + w, W + w), (w, W + w)], c, x0, y0, SKY)
    b += T(x0 + (L + 2 * w) * c / 2, y0 + (W + 2 * w) * c / 2 + 5, 'photo', 16) + T(x0 + (L + 2 * w) * c / 2, y0 + (w + 0.0) * c + 18, f'{L} cm', 15, 'middle', 700, NAVY)
    b += T(x0 + w * c + 4, y0 + (W + 2 * w) * c / 2 + 26, f'{W} cm', 15, 'start', 700, NAVY)
    b += T(x0 + (L + 2 * w) * c + 8, y0 + w * c / 2 + 5, f'{w} cm', 15, 'start', 800, TEAL)
    return svg(x0 + (L + 2 * w) * c + 56, y0 + (W + 2 * w) * c + 14, b, label or f'A {L} cm by {W} cm photo inside a yellow frame that is {w} cm wide all round, on a 1 cm grid.')


def tiles_fig(n=6):
    c, g = 30, 12
    per = 3
    b = ''
    for k in range(n):
        x, y = 10 + (k % per) * (c + g), 8 + (k // per) * (c + g)
        b += Re(x, y, c, c, YEL, NAVY, 2.4)
    rows = (n + per - 1) // per
    return svg(20 + per * c + (per - 1) * g, 16 + rows * c + (rows - 1) * g, b, f'{n} separate square tiles, each 1 cm by 1 cm.')


def tile_shapes_fig():
    """The answer picture of 3(b): a 2 by 3 block (smallest perimeter) and a row of six (a largest perimeter)."""
    c = 30
    b = T(10, 18, 'Smallest: 10 cm', 16, 'start', 800, TEAL)
    for x in range(3):
        for y in range(2):
            b += Re(10 + x * c, 28 + y * c, c, c, YEL, NAVY, 2.4)
    b += T(10, 118, 'A largest: 14 cm', 16, 'start', 800, TEAL)
    for x in range(6):
        b += Re(10 + x * c, 128, c, c, YEL, NAVY, 2.4)
    return svg(10 + 6 * c + 12, 128 + c + 10, b, 'A block of 2 by 3 tiles with perimeter 10 cm, and a row of 6 tiles with perimeter 14 cm.')


def cut_corners_fig(a=12, b_=8, s=3, label=''):
    c = max(10, min(22, 230 // a))
    x0, y0 = 46, 20
    b = ppoly([(0, 0), (a, 0), (a, b_), (0, b_)], c, x0, y0, SKY)
    for (cx, cy) in ((0, 0), (a - s, 0), (0, b_ - s), (a - s, b_ - s)):
        b += ppoly([(cx, cy), (cx + s, cy), (cx + s, cy + s), (cx, cy + s)], c, x0, y0, '#fff', 2.4, '6 4', RED)
    b += T(x0 + s * c / 2, y0 + s * c / 2 + 5, f'{s} cm', 14, 'middle', 800, RED)
    b += T(x0 + a * c / 2, y0 - 7, f'{a} cm', 16) + T(x0 - 8, y0 + b_ * c / 2 + 5, f'{b_} cm', 16, 'end')
    return svg(x0 + a * c + 14, y0 + b_ * c + 12, b, label or f'A {a} cm by {b_} cm rectangle with a {s} cm by {s} cm square marked in each of the four corners to be cut off.')


def squares_row_poly(sides):
    """The outline of squares standing side by side on one line, smallest on the left (y goes down, the base line is y = top of the tallest)."""
    top = max(sides)
    pts = [(0, top)]
    x = 0
    for s in sides:
        pts += [(x, top - s), (x + s, top - s)]
        x += s
    pts += [(x, top)]
    return pts


def squares_row_fig(sides=(2, 3, 4), label=''):
    c = max(12, min(28, 250 // sum(sides)))
    x0, y0 = 10, 8
    top = max(sides)
    b = ''
    x = 0
    for s in sides:
        b += Re(x0 + x * c, y0 + (top - s) * c, s * c, s * c, YEL if s % 2 == 0 else SKY, NAVY, 3) + T(x0 + (x + s / 2) * c, y0 + (top - s / 2) * c + 6, f'{s} cm', 16)
        x += s
    return svg(x0 + sum(sides) * c + 12, y0 + top * c + 12, b, label or ('Squares with sides ' + ', '.join(f'{s} cm' for s in sides) + ' standing side by side on one line, smallest on the left.'))


def garden_fig(L=10, W=8, label=''):
    c = max(10, min(24, 250 // L))
    x0, y0 = 46, 22
    pr, pc = W // 2 - 1, L // 2 - 1
    b = ''
    for i in range(L):
        for j in range(W):
            path = i == pc or j == pr
            b += f'<rect x="{x0 + i * c}" y="{y0 + j * c}" width="{c}" height="{c}" fill="{YEL if path else "#CFE8CF"}" stroke="{GRIDC}" stroke-width="1"/>'
    b += Re(x0, y0, L * c, W * c, 'none', NAVY, 2.6) + T(x0 + L * c / 2, y0 - 7, f'{L} m', 16) + T(x0 - 8, y0 + W * c / 2 + 5, f'{W} m', 16, 'end')
    b += T(x0 + L * c / 2, y0 + W * c + 20, 'yellow = path, 1 m wide', 15, 'middle', 700, TEAL)
    return svg(x0 + L * c + 14, y0 + W * c + 30, b, label or f'A garden {L} m long and {W} m wide with two paths 1 m wide crossing it, one along its length and one across its width.')


def plain_rect_fig(L=9, W=4, label=''):
    c = max(12, min(26, 250 // L))
    x0, y0 = 46, 22
    b = gridlines(x0, y0, L, W, c) + ppoly([(0, 0), (L, 0), (L, W), (0, W)], c, x0, y0, SKY) + T(x0 + L * c / 2, y0 - 7, f'{L} cm', 16) + T(x0 - 8, y0 + W * c / 2 + 5, f'{W} cm', 16, 'end')
    return svg(x0 + L * c + 14, y0 + W * c + 12, b, label or f'A rectangle {L} cm long and {W} cm wide.')


# ---------------------------------------------------------------- the cube fold (lesson 8): INDEPENDENT of any rule about rows and steps
def roll(o, d):
    """The orientation (top, bottom, north, south, east, west) of a cube after rolling one square over its edge in direction d = 'N', 'S', 'E' or 'W'."""
    t, b, n, s, e, w = o
    return {'E': (w, e, n, s, t, b), 'W': (e, w, n, s, b, t), 'N': (s, n, t, b, e, w), 'S': (n, s, b, t, e, w)}[d]


def fold(cells):
    """Roll a cube over the net: each square gets the face that is on the bottom when the cube sits on it.  Returns {cell: face id} if the net folds into a cube
    (6 different faces and every shared edge agrees), else None.  Faces 0 and 1 are opposite, 2 and 3, 4 and 5."""
    cells = list(cells)
    start = cells[0]
    ori = {start: (0, 1, 2, 3, 4, 5)}
    todo = [start]
    while todo:
        cur = todo.pop()
        x, y = cur
        for d, q in (('E', (x + 1, y)), ('W', (x - 1, y)), ('N', (x, y - 1)), ('S', (x, y + 1))):
            if q in cells:
                o = roll(ori[cur], d)
                if q not in ori:
                    ori[q] = o
                    todo.append(q)
                elif ori[q] != o:
                    return None
    face = {c: o[1] for c, o in ori.items()}
    return face if len(set(face.values())) == 6 and len(face) == 6 else None


def opposite_cells(cells):
    """Pairs of squares that are opposite faces of the folded cube."""
    f = fold(cells)
    if f is None:
        return None
    inv = {v: k for k, v in f.items()}
    return sorted(tuple(sorted((inv[a], inv[a ^ 1]))) for a in (0, 2, 4))


def dice_fills(cells, given):
    """Every way to write 1 to 6 on the squares of a cube net so that opposite faces add up to 7 and the given squares keep their numbers."""
    pairs = opposite_cells(cells)
    out = []
    for perm in itertools.permutations(range(1, 7)):
        lab = dict(zip(sorted(cells), perm))
        if all(lab[c] == v for c, v in given.items()) and all(lab[a] + lab[b] == 7 for a, b in pairs):
            out.append(lab)
    return out


def sym_lines(cells):
    """The lines of symmetry of a shape made of unit squares: tries every up-down, across and corner-to-corner mirror line on the grid."""
    cells = set(cells)
    n = 0
    for a in range(-2, 2 * 12):
        n += cells == {(a - x, y) for x, y in cells}          # up-down line (a half-integer or integer position)
        n += cells == {(x, a - y) for x, y in cells}          # across line
    for k in range(-12, 13):
        n += cells == {(y + k, x - k) for x, y in cells}      # corner-to-corner, one way
        n += cells == {(k - y, k - x) for x, y in cells}      # corner-to-corner, the other way
    return n


# ---------------------------------------------------------------- figures for lesson 8
def dims_c(cells):
    return max(a for a, _ in cells) + 1, max(b for _, b in cells) + 1


def cells_g(cells, c, ox, oy, fill=SKY, labels=None, size=18, sw=2.4):
    b = ''
    for (x, y) in cells:
        b += Re(ox + x * c, oy + y * c, c, c, fill, NAVY, sw)
        t = (labels or {}).get((x, y))
        if t not in (None, ''):
            b += T(ox + x * c + c / 2, oy + y * c + c / 2 + size * 0.36, t, size)
    return b


def nets_fig(nets, c=21, label=''):
    """Several nets in a 2-column picture, each in a white panel with its letter."""
    pw, ph = 144, 3 * c + 24
    rows = (len(nets) + 1) // 2
    b = ''
    for i, (L, cells) in enumerate(nets):
        px, py = (i % 2) * pw, (i // 2) * ph
        w, h = dims_c(cells)
        b += Re(px + 3, py + 3, pw - 6, ph - 6, '#fff', GRIDC, 1.6, 9) + T(px + 17, py + 25, L, 20, 'middle', 800, TEAL)
        b += cells_g(cells, c, px + 30 + (112 - w * c) / 2, py + 12 + (3 * c - h * c) / 2 + 3, SKY)
    return svg(2 * pw if len(nets) > 1 else pw, rows * ph, b, label or ('Shapes made of squares: ' + ', '.join(L for L, _ in nets) + '.'))


def labelled_net_fig(cells, labels, c=40, size=22, fill=SKY, blank='?', label='', caption=''):
    w, h = dims_c(cells)
    top = 22 if caption else 4
    b = T(4, 16, caption, 17, 'start', 800, TEAL) if caption else ''
    for (x, y) in cells:
        t = labels.get((x, y), '')
        b += Re(4 + x * c, top + y * c, c, c, fill if t else '#fff', NAVY, 2.6)
        b += T(4 + x * c + c / 2, top + y * c + c / 2 + size * 0.36, t if t else blank, size, 'middle', 800, NAVY if t else RED)
    return svg(w * c + 8, top + h * c + 8, b, label or 'A net made of 6 squares.')


def half_fig(kind, solved=False):
    c = 24
    x0, y0 = 10, 22
    if kind == 'rocket':
        cols, rows, half, axis = 10, 7, [(5, 0), (3, 2), (3, 5), (1, 7), (4, 7), (5, 6)], ('v', 5)
        mir = lambda p: (10 - p[0], p[1])
    else:
        cols, rows, half, axis = 10, 8, [(1, 4), (0, 2), (3, 3), (6, 1), (9, 2), (10, 4)], ('h', 4)
        mir = lambda p: (p[0], 8 - p[1])
    full = list(half)
    for p in [mir(q) for q in reversed(half)]:
        if p != full[-1] and p != full[0]:
            full.append(p)
    b = gridlines(x0, y0, cols, rows, c)
    if solved:
        b += ppoly(full, c, x0, y0, '#CDE8F7', 3.4)
    if axis[0] == 'v':
        b += Ln(x0 + axis[1] * c, y0 - 14, x0 + axis[1] * c, y0 + rows * c + 14, 3.2, RED, '8 6')
    else:
        b += Ln(x0 - 14, y0 + axis[1] * c, x0 + cols * c + 14, y0 + axis[1] * c, 3.2, RED, '8 6')
    b += f'<polyline points="{" ".join(f"{x0 + p[0] * c:g},{y0 + p[1] * c:g}" for p in half)}" fill="none" stroke="{NAVY}" stroke-width="4.4" stroke-linejoin="round" stroke-linecap="round"/>'
    if solved:
        mp = [mir(q) for q in half]
        b += f'<polyline points="{" ".join(f"{x0 + p[0] * c:g},{y0 + p[1] * c:g}" for p in mp)}" fill="none" stroke="{TEAL}" stroke-width="4.4" stroke-linejoin="round" stroke-linecap="round"/>'
    name = 'half a rocket on the left of an up-down dashed line' if kind == 'rocket' else 'the top half of a fish above an across dashed line'
    return svg(x0 * 2 + cols * c, y0 * 2 + rows * c - 14, b, ('The finished figure, ' if solved else 'A half figure on a grid: ') + name + '.')


def grid_cells_fig(shaped, cols, rows, c=44, fill=YEL, colnames=True, rownames=True, lines=(), label='', fill_bg='#fff'):
    """A grid of squares with the given (col, row) cells shaded; columns A, B, C ... and rows 1, 2, 3 ... when named; lines: 'v' / 'h' dashed middle lines."""
    x0, y0 = (26 if rownames else 8), (26 if colnames else 8)
    b = ''
    for x in range(cols):
        for y in range(rows):
            b += Re(x0 + x * c, y0 + y * c, c, c, fill if (x, y) in shaped else fill_bg, NAVY, 2.2)
    for i in range(cols if colnames else 0):
        b += T(x0 + i * c + c / 2, y0 - 8, 'ABCDEFGH'[i], 17)
    for j in range(rows if rownames else 0):
        b += T(x0 - 10, y0 + j * c + c / 2 + 6, str(j + 1), 17)
    if 'v' in lines:
        b += Ln(x0 + cols * c / 2, y0 - 6, x0 + cols * c / 2, y0 + rows * c + 8, 3.2, RED, '8 6')
    if 'h' in lines:
        b += Ln(x0 - 6, y0 + rows * c / 2, x0 + cols * c + 8, y0 + rows * c / 2, 3.2, RED, '8 6')
    return svg(x0 + cols * c + 16, y0 + rows * c + 14, b, label or f'A grid of {cols} by {rows} squares.')


def side_by_side(figs, label, gap=16, target=330):
    """Several figures in one row (one svg), scaled down together if the row is wider than target."""
    import re as _re
    parts, W, H = [], 0, 0
    for f in figs:
        root = _re.match(r'<svg[^>]*>', f).group(0)
        vb = [float(v) for v in _re.search(r'viewBox="([\d. -]+)"', root).group(1).split()]
        parts.append((vb, f[len(root):f.rindex('</svg>')]))
        W += vb[2] + gap
        H = max(H, vb[3])
    W -= gap
    sc = min(1.0, target / W)
    body, x = '', 0
    for vb, inner in parts:
        if sc < 1.0:
            inner = lift_text(vb[2], inner)
        body += (f'<svg x="{x * sc:g}" y="0" width="{vb[2] * sc:g}" height="{vb[3] * sc:g}" viewBox="{vb[0]:g} {vb[1]:g} {vb[2]:g} {vb[3]:g}" overflow="visible" '
                 f'style="width:{vb[2] * sc:g}px;height:{vb[3] * sc:g}px;max-width:none">{inner}</svg>')
        x += vb[2] + gap
    return svg(W * sc, H * sc, body, label)


def cuboid_fig(a=3, b_=2, h=1, label=''):
    """A box a long, b_ deep (going back) and h high, drawn from the front and above."""
    u = max(16, min(40, 180 // max(a, b_ + 1, 1)))
    dx, dy = 0.55 * u, 0.42 * u
    x0, y0 = 38, 20 + b_ * dy
    F = [(0, 0), (a * u, 0), (a * u, h * u), (0, h * u)]
    s = ''
    # top face, right face, front face
    top = [(0, 0), (a * u, 0), (a * u + b_ * dx, -b_ * dy), (b_ * dx, -b_ * dy)]
    rgt = [(a * u, 0), (a * u + b_ * dx, -b_ * dy), (a * u + b_ * dx, h * u - b_ * dy), (a * u, h * u)]
    for pts, fill in ((top, '#CDE8F7'), (rgt, '#B8D4EA'), (F, SKY)):
        s += '<polygon points="' + ' '.join(f'{x0 + px:g},{y0 + py:g}' for px, py in pts) + f'" fill="{fill}" stroke="{NAVY}" stroke-width="2.6" stroke-linejoin="round"/>'
    s += T(x0 + a * u / 2, y0 + h * u + 21, f'{a} cm', 16) + T(x0 - 8, y0 + h * u / 2 + 5, f'{h} cm', 16, 'end')
    s += T(x0 + a * u + b_ * dx + 8, y0 - b_ * dy / 2 + 2, f'{b_} cm', 16, 'start')
    return svg(x0 + a * u + b_ * dx + 52, y0 + h * u + 30, s, label or f'A box {a} cm long, {b_} cm wide and {h} cm high.')


TETRAS = [('line', [(0, 0), (1, 0), (2, 0), (3, 0)]), ('square', [(0, 0), (1, 0), (0, 1), (1, 1)]), ('L', [(0, 0), (0, 1), (0, 2), (1, 2)]),
          ('T', [(0, 0), (1, 0), (2, 0), (1, 1)]), ('zigzag', [(0, 0), (1, 0), (1, 1), (2, 1)])]


def tetra_fig():
    c, pw, ph = 26, 90, 150
    b = ''
    for i, (name, cells) in enumerate(TETRAS):
        px, py = (i % 3) * pw, (i // 3) * ph
        w, h = dims_c(cells)
        b += cells_g(cells, c, px + (pw - w * c) / 2, py + 12 + (4 * c - h * c) / 2, YEL) + T(px + pw / 2, py + 4 * c + 36, name, 16, 'middle', 800, TEAL)
    return svg(3 * pw, 2 * ph, b, 'The five shapes made of 4 squares joined edge to edge: line, square, L, T and zigzag.')
