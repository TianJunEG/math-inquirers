"""Primary 2 pictures: place-value discs, coins and notes (original art), clocks to the minute, rulers and scales.
Pure black and white. Every picture has a reader function that recovers the value from the DRAWING only (used by the independent solvers)."""
import math, re
from .common import svg, OBJ_ST, obj_g
from . import art as _art     # registers extra objects
from .art import osz, opitch, COUNT_KINDS, NAMES as OBJN, count_objs

# ---------------------------------------------------------------- place-value discs and chart
DISC_R = 4.5         # mm radius: discs are 9 mm across

def disc(kind, cx, cy):
    lab = {"h": "100", "t": "10", "o": "1"}[kind]
    fs = {"h": 3.7, "t": 4.3, "o": 5.2}[kind]
    return (f'<g class="disc {kind}"><circle cx="{cx:.2f}" cy="{cy:.2f}" r="{DISC_R}" fill="#fff" stroke="#000" stroke-width="{0.9 if kind == "h" else 0.6}"/>'
            f'<text x="{cx:.2f}" y="{cy+0.1:.2f}" text-anchor="middle" dominant-baseline="central" font-family="Nunito Sans" font-weight="800" font-size="{fs}" fill="#000">{lab}</text></g>')

def pv_chart(h, t, o, per_row=3):
    """a place-value chart: three columns (Hundreds, Tens, Ones) with discs; at most 9 discs in a column, 3 per row"""
    colw = per_row * 10.4 + 2.5; gap = 2.0; head = 6.5
    rows = max(math.ceil(n / per_row) for n in (h, t, o)) or 1
    H = head + rows * 10.4 + 1.5; W = 3 * colw + 2 * gap
    p = []
    for ci, (name, kind, n) in enumerate((("Hundreds", "h", h), ("Tens", "t", t), ("Ones", "o", o))):
        x0 = ci * (colw + gap)
        p.append(f'<rect x="{x0:.2f}" y="0.3" width="{colw:.2f}" height="{H-0.6:.2f}" rx="1.2" fill="#fff" stroke="#000" stroke-width="0.5"/>'
                 f'<text x="{x0+colw/2:.2f}" y="3.6" text-anchor="middle" dominant-baseline="central" font-family="Nunito Sans" font-weight="800" font-size="3.6" fill="#000">{name}</text>'
                 f'<line x1="{x0:.2f}" y1="{head-0.8}" x2="{x0+colw:.2f}" y2="{head-0.8}" stroke="#000" stroke-width="0.4"/>')
        for i in range(n):
            p.append(disc(kind, x0 + 1.2 + DISC_R + 0.4 + (i % per_row) * 10.4, head + 0.6 + DISC_R + (i // per_row) * 10.4))
    return svg(round(W, 1), round(H, 1), "".join(p))

def read_pv_chart(s):
    return tuple(len(re.findall(r'class="disc %s"' % k, s)) for k in "hto")

# ---------------------------------------------------------------- coins and notes (original line art, inspired by Singapore money; much larger than real)
COIN_REAL = {5: 16.2, 10: 18.5, 20: 21.4, 50: 24.7, 100: 24.65}          # real diameters (mm): only the RATIOS are used (a fact, not a design)
COIN_D = {v: d * 0.78 for v, d in COIN_REAL.items()}
NOTE_W, NOTE_H = 27.0, 13.5

def _motif(v, cx, cy, u):
    k = u * 0.15; st = 'fill="none" stroke="#000" stroke-width="0.4" stroke-linejoin="round" stroke-linecap="round"'
    if v == 5:
        return f'<path d="M{cx-k*1.3:.2f},{cy+k*0.6:.2f} Q{cx-k*0.2:.2f},{cy-k*1.6:.2f} {cx+k*1.3:.2f},{cy-k*0.9:.2f} Q{cx+k*0.6:.2f},{cy+k*1.0:.2f} {cx-k*1.3:.2f},{cy+k*0.6:.2f} Z" {st}/>'
    if v == 10:
        pts = " ".join(f"{cx+(k*1.5 if i%2==0 else k*0.65)*math.sin(i*math.pi/5):.2f},{cy-(k*1.5 if i%2==0 else k*0.65)*math.cos(i*math.pi/5):.2f}" for i in range(10))
        return f'<polygon points="{pts}" {st}/>'
    if v == 20:
        return "".join(f'<circle cx="{cx+k*1.0*math.sin(i*math.pi*2/5):.2f}" cy="{cy-k*1.0*math.cos(i*math.pi*2/5):.2f}" r="{k*0.7:.2f}" {st}/>' for i in range(5)) + f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r="{k*0.45:.2f}" {st}/>'
    if v == 50:
        return f'<path d="M{cx:.2f},{cy-k*1.5:.2f} L{cx+k*1.2:.2f},{cy+k*0.5:.2f} L{cx:.2f},{cy+k*0.5:.2f} Z M{cx-k*1.5:.2f},{cy+k*0.9:.2f} L{cx+k*1.5:.2f},{cy+k*0.9:.2f} L{cx+k*0.9:.2f},{cy+k*1.6:.2f} L{cx-k*0.9:.2f},{cy+k*1.6:.2f} Z" {st}/>'
    # $1: a small sun
    return f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r="{k*0.9:.2f}" {st}/>' + "".join(f'<line x1="{cx+k*1.2*math.sin(i*math.pi/4):.2f}" y1="{cy-k*1.2*math.cos(i*math.pi/4):.2f}" x2="{cx+k*1.8*math.sin(i*math.pi/4):.2f}" y2="{cy-k*1.8*math.cos(i*math.pi/4):.2f}" {st}/>' for i in range(8))

def coin_g(v, x, cy):
    d = COIN_D[v]; r = d / 2; cx = x + r
    lab = str(v) if v < 100 else "$1"
    unit = "cents" if v < 100 else "dollar"
    return (f'<g class="coin" data-v="{v}"><circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" fill="#fff" stroke="#000" stroke-width="0.6"/>'
            + _motif(v, cx, cy - r * 0.62, r) +
            f'<text class="coinval" x="{cx:.1f}" y="{cy-r*0.08:.1f}" text-anchor="middle" dominant-baseline="central" font-family="Nunito Sans" font-weight="800" font-size="{r*0.58:.1f}" fill="#000">{lab}</text>'
            f'<text class="coinunit" x="{cx:.1f}" y="{cy+r*0.50:.1f}" text-anchor="middle" dominant-baseline="central" font-family="Nunito Sans" font-weight="800" font-size="2.7" fill="#000">{unit}</text></g>')

def note_g(v, x, y):
    """an original note design: a frame, the value in two corners, a simple bird in the middle; not a copy of any real note"""
    W, H = NOTE_W, NOTE_H
    bird = ('<path d="M-4.5,1.2 C-2.5,-3.5 2.5,-3.5 4.5,-0.5 L7,-1.5 L5.8,1.2 C3,3.8 -2,3.8 -4.5,1.2 Z M-4.5,1.2 L-7.5,3.2 L-4,3" fill="none" stroke="#000" stroke-width="0.45" stroke-linejoin="round"/>')
    return (f'<g class="note" data-v="{v}"><rect x="{x:.1f}" y="{y:.1f}" width="{W}" height="{H}" rx="1.2" fill="#fff" stroke="#000" stroke-width="0.7"/>'
            f'<rect x="{x+1.4:.1f}" y="{y+1.4:.1f}" width="{W-2.8}" height="{H-2.8}" rx="0.8" fill="none" stroke="#000" stroke-width="0.3"/>'
            f'<g transform="translate({x+W/2:.1f},{y+H/2:.1f}) scale(0.8)">{bird}</g>'
            f'<text class="noteval" x="{x+2.8:.1f}" y="{y+5.6:.1f}" font-family="Nunito Sans" font-weight="800" font-size="4.6" fill="#000">${v}</text>'
            f'<text class="noteval2" x="{x+W-2.8:.1f}" y="{y+H-2.8:.1f}" text-anchor="end" font-family="Nunito Sans" font-weight="800" font-size="4.6" fill="#000">${v}</text></g>')

def money_width(items, gap=2.0):
    return sum((COIN_D[i[1]] if i[0] == "c" else NOTE_W) + gap for i in items)

def money_svg(items, per_row=None, gap=2.0):
    """items: list of ('c', cents) coins and ('n', dollars) notes, drawn in reading order; wraps into rows of width <= 78 mm unless per_row"""
    maxw = 118.0
    rows = [[]]; w = 0
    for it in items:
        iw = (COIN_D[it[1]] if it[0] == "c" else NOTE_W) + gap
        if rows[-1] and (w + iw > maxw or (per_row and len(rows[-1]) >= per_row)): rows.append([]); w = 0
        rows[-1].append(it); w += iw
    p = []; y = 0; W = 0
    for row in rows:
        rh = max((COIN_D[i[1]] if i[0] == "c" else NOTE_H) for i in row)
        x = 0.8
        for it in row:
            if it[0] == "c": p.append(coin_g(it[1], x, y + rh / 2 + 0.8)); x += COIN_D[it[1]] + gap
            else: p.append(note_g(it[1], x, y + (rh - NOTE_H) / 2 + 0.8)); x += NOTE_W + gap
        W = max(W, x); y += rh + 1.6
    return svg(round(W + 0.8, 1), round(y + 0.4, 1), "".join(p))

def read_money(s):
    """independent reader: total in cents from the coins and notes drawn (values read from the printed numerals)"""
    tot = 0
    for m in re.finditer(r'class="coinval"[^>]*>(\$?\d+)<', s):
        v = m.group(1); tot += 100 if v == "$1" else int(v)
    for m in re.finditer(r'class="noteval"[^>]*>\$(\d+)<', s): tot += 100 * int(m.group(1))
    return tot

def dollars(c):
    return f"${c // 100}.{c % 100:02d}"

# ---------------------------------------------------------------- clock to the minute (numerals outside the ring so hands never cross them)
CK = 27

def clock_svg(h, m, size=54):
    cx = cy = CK; R = 19.0
    p = [f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="#fff" stroke="#000" stroke-width="0.7"/>']
    for k in range(60):
        a_ = math.radians(k * 6); L = 3.0 if k % 5 == 0 else 1.4
        p.append(f'<line x1="{cx+R*math.sin(a_):.2f}" y1="{cy-R*math.cos(a_):.2f}" x2="{cx+(R-L)*math.sin(a_):.2f}" y2="{cy-(R-L)*math.cos(a_):.2f}" stroke="#000" stroke-width="{0.5 if k % 5 == 0 else 0.3}"/>')
    for k in range(1, 13):
        a_ = math.radians(k * 30)
        p.append(f'<text x="{cx+23.4*math.sin(a_):.2f}" y="{cy-23.4*math.cos(a_)+0.2:.2f}" text-anchor="middle" dominant-baseline="central" font-family="Nunito Sans" font-weight="800" font-size="4.6" fill="#000">{k}</text>')
    ha = math.radians(30 * (h % 12) + m * 0.5); ma = math.radians(m * 6)
    p.append(f'<line class="hour" x1="{cx}" y1="{cy}" x2="{cx+10.5*math.sin(ha):.3f}" y2="{cy-10.5*math.cos(ha):.3f}" stroke="#000" stroke-width="2.1" stroke-linecap="round"/>')
    p.append(f'<line class="minute" x1="{cx}" y1="{cy}" x2="{cx+16.6*math.sin(ma):.3f}" y2="{cy-16.6*math.cos(ma):.3f}" stroke="#000" stroke-width="0.8" stroke-linecap="round"/>')
    p.append(f'<circle cx="{cx}" cy="{cy}" r="1.3" fill="#000"/>')
    return svg(54, 54, "".join(p))

def read_clock(s):
    """independent reader: the time from the hand end points of the drawing"""
    hx = re.search(r'class="hour" x1="27" y1="27" x2="([-\d.]+)" y2="([-\d.]+)"', s)
    mx = re.search(r'class="minute" x1="27" y1="27" x2="([-\d.]+)" y2="([-\d.]+)"', s)
    ang = lambda x, y: (math.degrees(math.atan2(float(x) - 27, 27 - float(y)))) % 360
    m = round(ang(*mx.groups()) / 6) % 60
    ha = ang(*hx.groups())
    h = round((ha - m * 0.5) / 30) % 12 or 12
    return h, m

def tstr(h, m): return f"{(h-1) % 12 + 1}:{m:02d}"

def hands_apart(h, m):
    ha = 30 * (h % 12) + m * 0.5; ma = m * 6
    return abs((ha - ma + 180) % 360 - 180)

# ---------------------------------------------------------------- arrays and groups of objects
def array_svg(kind, rows, cols):
    size = osz(kind); pitch = opitch(kind)
    inner = "".join(obj_g(kind, 0.5 + c * pitch, 0.5 + r * pitch, size) for r in range(rows) for c in range(cols))
    return svg(round(cols * pitch + 1, 1), round(rows * pitch + 1, 1), inner)
