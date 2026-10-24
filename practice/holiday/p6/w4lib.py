"""Level 6 helpers for holiday week 4 (lessons 7 and 8): the workbook's own block drawing and corner picture, plain svg figures, and independent checkers.

* Figures: blocks_bridge4.js loads p6/content/l7.js and calls ITS blocks() and cornerFig() as printed.  The star pictures, the ring of dots, the letter-number strip, the clock and
  week circles and the tables are inline svg drawn here (text kept horizontal and at a readable size on a 390 px phone).
* Checkers: a small turtle (`turtle`) that walks the drawn program and reports the corners it visits and the total it turns; the interior-angle formula (n - 2) x 180 / n for the regular
  polygons (so the 360 / n rule is never used to check itself); a Caesar coder/decoder written from the letter numbers; clock arithmetic by counting on.
"""
import json, math, os, re, subprocess
from fractions import Fraction
from p6lib import NAVY, YEL, TEAL, WARM, PALE, T, esc
import hlib

HERE = os.path.dirname(os.path.abspath(__file__))
SKY, RED, GREY = '#DDEBF7', '#C03B3B', '#8A94AD'
MINUS = '−'
ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
_cache = {}


def bridge(req):
    key = json.dumps(req, sort_keys=True)
    if key not in _cache:
        r = subprocess.run(['node', os.path.join(HERE, 'blocks_bridge4.js')], input=json.dumps([req]), capture_output=True, text=True, check=True)
        _cache[key] = json.loads(r.stdout)[0]
    return _cache[key]


def blocks(prog, label, fs=15, h=30, grow=1.25):
    """The workbook's block drawing of `prog` (list of [kind, text, children]), wrapped in one svg."""
    r = bridge(dict(kind='blocks', prog=prog, fs=fs, h=h))
    body = r['svg'].replace('#D64545', RED)                 # white on the workbook's red is 4.4:1; this red is 5.3:1 (the printed colour is unchanged)
    body = re.sub(r'<text[^>]*>\s*</text>', '', body)
    return (f'<svg viewBox="0 0 {r["w"]} {r["h"]}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{esc(label)}" '
            f'style="width:100%;max-width:{r["w"] * grow:.0f}px;height:auto;display:block;margin:0 auto">{body}</svg>')


def corner_fig():
    s = bridge(dict(kind='corner'))
    return s.replace('style="width:244px;max-width:100%"', 'style="width:100%;max-width:300px;height:auto;display:block;margin:0 auto" role="img"')


def nb(frame, budget=14):
    import w2lib
    return w2lib.nb(frame, budget)


# ---------------------------------------------------------------- the turtle (independent checker for every pen-drawing question)
def turtle(repeats, turn, step=100, start_heading=90):
    """Walks `repeats` times: move `step`, turn right by `turn` degrees.  Returns dict(corners=number of different places it stands on, total=total turning,
    rounds=total / 360 as a Fraction, home=True if it ends where it began, facing the way it began)."""
    x = y = 0.0
    h = float(start_heading)
    pts = {(0.0, 0.0)}
    for _ in range(repeats):
        x += step * math.sin(math.radians(h)); y += step * math.cos(math.radians(h))
        pts.add((round(x, 6), round(y, 6)))
        h = (h - turn) % 360
    total = repeats * turn
    home = abs(x) < 1e-6 and abs(y) < 1e-6 and (abs(h - start_heading) < 1e-9 or abs(abs(h - start_heading) - 360) < 1e-9)
    return dict(corners=len({(round(a, 4), round(b, 4)) for a, b in pts}), total=total, rounds=Fraction(total, 360), home=home)


def inside_of_regular(n):
    """Each inside angle of a regular n-gon, from the angle sum (n - 2) x 180 shared by n corners."""
    return Fraction((n - 2) * 180, n)


def sides_with_inside(angle):
    """The number of sides of the regular polygon whose inside angle is `angle` (None if there is none), found by trying 3, 4, 5, ..."""
    for n in range(3, 721):
        if inside_of_regular(n) == angle:
            return n
    return None


def sides_with_turn(angle):
    for n in range(3, 721):
        if 180 - inside_of_regular(n) == angle:
            return n
    return None


def whole(f):
    f = Fraction(f)
    assert f.denominator == 1, f
    return int(f)


# ---------------------------------------------------------------- Caesar codes and clocks (from the letter numbers; never the printed key)
def num(c):
    return ABC.index(c)


def shift_text(msg, k):
    out = ''
    for c in msg.upper():
        out += ABC[(ABC.index(c) + k) % 26] if c in ABC else c
    return out


def clock_after(start, hours, size=12):
    """Counts on one hour at a time round a clock face with `size` numbers (12 stands for 0)."""
    pos = start
    step = 1 if hours >= 0 else -1
    for _ in range(abs(hours)):
        pos += step
        if pos > size:
            pos = 1
        if pos < 1:
            pos = size
    return pos


DAYS = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']


def day_after(day, n):
    i = DAYS.index(day)
    step = 1 if n >= 0 else -1
    for _ in range(abs(n)):
        i = (i + step) % 7
    return DAYS[i]


# ---------------------------------------------------------------- figures
def ring_body(cx, cy, r, n, labels, dotr=9, edges=(), hl=(), fs=15, label_gap=None, ecol=TEAL, ew=3.2):
    pts = [(cx + r * math.sin(2 * math.pi * i / n), cy - r * math.cos(2 * math.pi * i / n)) for i in range(n)]
    b = f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{GREY}" stroke-width="1.5" stroke-dasharray="4 4"/>'
    for i, j in edges:
        b += f'<line x1="{pts[i][0]:.1f}" y1="{pts[i][1]:.1f}" x2="{pts[j][0]:.1f}" y2="{pts[j][1]:.1f}" stroke="{ecol}" stroke-width="{ew}" stroke-linecap="round"/>'
    for i, (x, y) in enumerate(pts):
        b += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{dotr}" fill="{YEL if i in hl else "#fff"}" stroke="{NAVY}" stroke-width="2"/>'
    gap = label_gap if label_gap is not None else dotr + fs * 0.9
    for i, (x, y) in enumerate(pts):
        lab = labels[i]
        if lab == '' or lab is None:
            continue
        lx = cx + (r + gap) * math.sin(2 * math.pi * i / n)
        ly = cy - (r + gap) * math.cos(2 * math.pi * i / n)
        b += T(f'{lx:.1f}', f'{ly + fs * 0.35:.1f}', lab, fs, 'middle', 700)
    return b


def star_fig(n, k, label, caption='', labels=True, dotr=8, r=62):
    """n dots round a circle, joined every k-th dot (k = how many times it goes round); k=0 draws the dots only."""
    edges = [(i, (i + k) % n) for i in range(n)] if k else []
    W = 2 * (r + 34)
    body = ring_body(W / 2, W / 2 + (24 if caption else 0), r, n, [str(i) for i in range(n)] if labels else [''] * n, dotr, edges, (0,))
    if caption:
        body += T(W / 2, 16, caption, 15, 'middle', 800)
    return hlib.svg(W, W + (28 if caption else 0), body, label)


def two_rings(n1, k1, n2, k2, cap1, cap2, label, dotr=8, r=56, labels1=True, labels2=True, every2=None):
    """Two rings of dots side by side (left joined every k1-th dot, right every k2-th dot)."""
    W1 = 2 * (r + 30)
    body = ''
    for ix, (n, k, cap, lab, ev) in enumerate(((n1, k1, cap1, labels1, None), (n2, k2, cap2, labels2, every2))):
        cx = W1 / 2 + ix * (W1 + 6)
        cy = W1 / 2 + 22
        names = [str(i) if (lab and (ev is None or i % ev == 0)) else '' for i in range(n)]
        body += ring_body(cx, cy, r, n, names, dotr if n < 15 else 5, [(i, (i + k) % n) for i in range(n)] if k else [], (0,))
        body += T(cx, 16, cap, 14, 'middle', 800)
    return hlib.svg(2 * W1 + 6, W1 + 28, body, label)


def letter_strip(label='Letter numbers: A is 0, B is 1, C is 2 and so on up to Z, which is 25'):
    cw, rh = 25, 44
    W = cw * 13 + 8
    b = ''
    for row in range(2):
        y0 = 4 + row * (rh + 10)
        b += f'<rect x="4" y="{y0}" width="{cw * 13}" height="{rh}" fill="#fff" stroke="{NAVY}" stroke-width="2"/><rect x="4" y="{y0}" width="{cw * 13}" height="{rh / 2}" fill="{YEL}" stroke="{NAVY}" stroke-width="2"/>'
        for i in range(13):
            idx = row * 13 + i
            x = 4 + cw * i
            if i:
                b += f'<line x1="{x}" y1="{y0}" x2="{x}" y2="{y0 + rh}" stroke="{NAVY}" stroke-width="1"/>'
            b += T(x + cw / 2, y0 + 16, ABC[idx], 15, 'middle', 800) + T(x + cw / 2, y0 + 38, idx, 14, 'middle', 600)
    return hlib.svg(W, 2 * rh + 18, b, label)


def clock_week(label, week_hl=6):
    """A 12-hour clock circle and a 7-day week circle side by side (as printed)."""
    r = 52
    body = ring_body(88, 116, r, 12, ['12'] + [str(i) for i in range(1, 12)], 6, (), (0,), 16)
    body += ring_body(268, 116, r, 7, ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'], 6, (), (week_hl,), 15, 22)
    body += T(88, 16, 'a 12-hour clock', 14, 'middle', 800) + T(268, 16, 'a week of 7 days', 14, 'middle', 800)
    return hlib.svg(356, 208, body, label)


def jump_rings(label, jump=None, cap=True, which=None):
    """12-hour clock circles with 12 at the top marked as the start (both side by side, or only ring `which`); with `jump` (a pair of hour jumps) the visited numbers are joined."""
    r = 54
    body = ''
    rings = (0, 1) if which is None else (which,)
    for k, ix in enumerate(rings):
        cx = 92 + k * 190
        edges = []
        if jump:
            j = jump[ix]
            pos = 0
            while True:
                nxt = (pos + j) % 12
                edges.append((pos, nxt))
                pos = nxt
                if pos == 0:
                    break
        body += ring_body(cx, 116, r, 12, ['12'] + [str(i) for i in range(1, 12)], 6, edges, (0,), 15)
        if cap:
            body += T(cx, 16, ('jumps of 5 hours', 'jumps of 4 hours')[ix], 14, 'middle', 800)
    return hlib.svg(380 if which is None else 190, 208, body, label)


def table_svg(head, rows, label, colw=None, fs=15, rh=30, shade=None):
    import w3lib
    return w3lib.table_svg(head, rows, label, colw, fs, rh, shade)


def finish_figs(items):
    return items


def code_stack(blocks, label, fs=15, grow=1.2):
    """Red variable blocks drawn like the workbook's (rounded, navy outline, white text); each block is a list of rows, each row a list of ('t', text) on the block or ('s', text) in a white slot.
    Long blocks are broken into rows so the text stays readable on a phone."""
    cw = lambda s: len(s) * fs * 0.56
    pad, gap, rh = 10, 6, fs + 12
    W = max(sum(cw(t) + (18 if k == 's' else 0) + gap for k, t in row) - gap for blk in blocks for row in blk) + 2 * pad
    y, body = 3, ''
    for blk in blocks:
        h = len(blk) * rh + 4
        body += f'<rect x="2" y="{y}" width="{W:.1f}" height="{h}" rx="7" fill="{RED}" stroke="{NAVY}" stroke-width="2"/>'
        for ri, row in enumerate(blk):
            x, ty = 2 + pad, y + 2 + ri * rh
            for k, t in row:
                w = cw(t)
                if k == 's':
                    body += f'<rect x="{x:.1f}" y="{ty + 3}" width="{w + 18:.1f}" height="{rh - 6}" rx="{(rh - 6) / 2}" fill="#fff" stroke="{NAVY}" stroke-width="1.5"/>'
                    body += T(f'{x + 9 + w / 2:.1f}', f'{ty + rh / 2 + fs * 0.35:.1f}', t, fs, 'middle', 700)
                    x += w + 18 + gap
                else:
                    body += T(f'{x:.1f}', f'{ty + rh / 2 + fs * 0.35:.1f}', t, fs, 'start', 700, '#fff')
                    x += w + gap
        y += h + 3
    return (f'<svg viewBox="0 0 {W + 4:.0f} {y + 2:.0f}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{esc(label)}" '
            f'style="width:100%;max-width:{(W + 4) * grow:.0f}px;height:auto;display:block;margin:0 auto" font-family="Nunito Sans, Arial, sans-serif">{body}</svg>')
