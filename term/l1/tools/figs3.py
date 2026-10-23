"""Terms 3 and 4 figure engine: clock, money and price tags, calendar, stick patterns, 2D shapes, grids, cube stacks, fold and punch,
panels (spot the difference, odd one out, missing tile), networks, picture graphs, icons batch 2, and the matching kit pages.

Same conventions as figs2: every function returns an inline <svg> that scales to its container, flat palette, navy outline, answer boxes
as tokens ('[]' box). Nothing here relies on colour alone (shapes differ by size, pattern and label). Registered from figs2.render / render_kit.
"""
import math

import figs2
from figs2 import NAVY, TEAL, YEL, SKY, SOFT, RED, MINT, FONT, SW, _o, _svg, _esc, token_svg, icon

MM = 4.58          # kit pages: one mm on paper is about 4.58 units (700-unit viewBox at 84% of 182 mm)
CUT = '#777'


# ------------------------------------------------------------------ icons batch 2 (64 x 64 box)

def icon_body(n):
    o = _o
    if n == 'sun':
        rays = ''.join(f'<line x1="{32 + 19 * math.cos(a):.1f}" y1="{32 + 19 * math.sin(a):.1f}" x2="{32 + 29 * math.cos(a):.1f}" y2="{32 + 29 * math.sin(a):.1f}" stroke="{NAVY}" stroke-width="3.4" stroke-linecap="round"/>' for a in [k * math.pi / 4 for k in range(8)])
        return rays + f'<circle cx="32" cy="32" r="14" {o(YEL)}/>'
    if n == 'moon':
        return f'<path d="M40 8 A24 24 0 1 0 56 40 A19 19 0 0 1 40 8 Z" {o("#F4E7A8")}/>'
    if n == 'bed':
        return f'<rect x="6" y="30" width="52" height="16" rx="3" {o("#BFD0EE")}/><rect x="6" y="18" width="6" height="34" {o("#E8B66F")}/><rect x="52" y="34" width="6" height="18" {o("#E8B66F")}/><rect x="14" y="22" width="14" height="9" rx="4" {o("#fff")}/>'
    if n == 'bus':
        return (f'<rect x="6" y="14" width="52" height="34" rx="7" {o(YEL)}/><rect x="11" y="19" width="12" height="11" {o("#DDEBF7")}/><rect x="26" y="19" width="12" height="11" {o("#DDEBF7")}/><rect x="41" y="19" width="12" height="11" {o("#DDEBF7")}/>'
                f'<circle cx="18" cy="49" r="6" {o(NAVY)}/><circle cx="46" cy="49" r="6" {o(NAVY)}/>')
    if n == 'house':
        return f'<polygon points="6,30 32,8 58,30" {o("#D64545")}/><rect x="12" y="30" width="40" height="26" {o("#F1D9AE")}/><rect x="27" y="40" width="11" height="16" {o("#fff")}/>'
    if n == 'school':
        return f'<rect x="8" y="24" width="48" height="32" {o("#F1D9AE")}/><polygon points="4,26 32,8 60,26" {o("#3B6FC9")}/><rect x="26" y="38" width="12" height="18" {o("#fff")}/><rect x="13" y="32" width="8" height="8" {o("#DDEBF7")}/><rect x="43" y="32" width="8" height="8" {o("#DDEBF7")}/><line x1="32" y1="8" x2="32" y2="2" stroke="{NAVY}" stroke-width="2.4"/>'
    if n == 'shop':
        return f'<rect x="8" y="26" width="48" height="30" {o("#F1D9AE")}/><path d="M4 26 L10 10 H54 L60 26 Z" {o("#D64545")}/><rect x="14" y="36" width="14" height="14" {o("#DDEBF7")}/><rect x="36" y="36" width="12" height="20" {o("#fff")}/>'
    if n == 'bath':
        return f'<path d="M6 30 H58 V38 C58 48 50 54 40 54 H24 C14 54 6 48 6 38 Z" {o("#DDEBF7")}/><path d="M14 30 V16 C14 10 22 10 22 16" fill="none" stroke="{NAVY}" stroke-width="{SW}"/><line x1="16" y1="54" x2="14" y2="60" stroke="{NAVY}" stroke-width="3"/><line x1="48" y1="54" x2="50" y2="60" stroke="{NAVY}" stroke-width="3"/>'
    if n == 'rubber':
        return f'<g transform="rotate(-20 32 32)"><rect x="8" y="20" width="48" height="24" rx="4" {o("#fff")}/><rect x="8" y="20" width="20" height="24" rx="4" {o("#F28C9C")}/></g>'
    if n == 'ruler':
        ticks = ''.join(f'<line x1="{12 + k * 5.2:.1f}" y1="22" x2="{12 + k * 5.2:.1f}" y2="{29 if k % 2 else 33}" stroke="{NAVY}" stroke-width="2"/>' for k in range(9))
        return f'<rect x="6" y="20" width="52" height="24" rx="3" {o("#F4E7A8")}/>' + ticks
    if n == 'glue':
        return f'<rect x="20" y="22" width="24" height="34" rx="5" {o("#fff")}/><rect x="25" y="8" width="14" height="14" rx="3" {o(TEAL)}/><rect x="20" y="32" width="24" height="12" {o("#3B6FC9")}/>'
    if n == 'shell':
        spokes = ''.join(f'<line x1="32" y1="54" x2="{32 + 22 * math.cos(math.radians(a)):.1f}" y2="{54 - 40 * math.sin(math.radians(a)):.1f}" stroke="{NAVY}" stroke-width="2"/>' for a in (45, 70, 90, 110, 135))
        return f'<path d="M8 50 C8 16 56 16 56 50 Z" {o("#F6C9D0")}/>' + spokes
    if n == 'spoon':
        return f'<ellipse cx="32" cy="18" rx="11" ry="14" {o("#DDE3EA")}/><rect x="29" y="30" width="6" height="30" rx="3" {o("#DDE3EA")}/>'
    if n == 'sock':
        return f'<path d="M20 6 H40 V34 L54 44 C58 50 52 58 46 56 L22 44 C18 42 20 38 20 34 Z" {o("#3DBE7A")}/><rect x="20" y="6" width="20" height="8" {o("#fff")}/>'
    if n == 'shoe':
        return f'<path d="M6 40 L14 14 H26 L28 28 C36 30 52 32 58 42 V50 H6 Z" {o("#D64545")}/><rect x="6" y="46" width="52" height="6" rx="2" {o("#fff")}/>'
    if n == 'button':
        return f'<circle cx="32" cy="32" r="24" {o("#C9B6F0")}/><circle cx="24" cy="26" r="3.4" fill="{NAVY}"/><circle cx="40" cy="26" r="3.4" fill="{NAVY}"/><circle cx="24" cy="38" r="3.4" fill="{NAVY}"/><circle cx="40" cy="38" r="3.4" fill="{NAVY}"/>'
    # tool icons: one picture, one word under it on the card
    if n == 't_strip':
        return f'<rect x="6" y="16" width="52" height="14" {o(YEL)}/><rect x="6" y="34" width="34" height="14" {o(SKY)}/><line x1="23" y1="16" x2="23" y2="30" stroke="{NAVY}" stroke-width="2"/><line x1="40" y1="16" x2="40" y2="30" stroke="{NAVY}" stroke-width="2"/>'
    if n == 't_table':
        return f'<rect x="8" y="10" width="48" height="44" {o("#fff")}/><line x1="8" y1="24" x2="56" y2="24" stroke="{NAVY}" stroke-width="2.4"/><line x1="8" y1="38" x2="56" y2="38" stroke="{NAVY}" stroke-width="2.4"/><line x1="28" y1="10" x2="28" y2="54" stroke="{NAVY}" stroke-width="2.4"/>'
    if n == 't_list':
        return ''.join(f'<circle cx="14" cy="{18 + 16 * k}" r="4" fill="{NAVY}"/><line x1="24" y1="{18 + 16 * k}" x2="56" y2="{18 + 16 * k}" stroke="{NAVY}" stroke-width="4" stroke-linecap="round"/>' for k in range(3))
    if n == 't_draw':
        return f'<g transform="rotate(-45 32 32)"><rect x="26" y="6" width="12" height="40" {o(YEL)}/><polygon points="26,46 38,46 32,58" {o('#F6C9A0')}/></g>'
    if n == 't_back':
        return f'<path d="M54 20 H24 A14 14 0 0 0 24 48 H40" fill="none" stroke="{NAVY}" stroke-width="5" stroke-linecap="round"/><polygon points="14,20 28,8 28,32" {o(TEAL)}/>'
    if n == 't_find':
        return f'<circle cx="28" cy="28" r="16" {o("#fff")}/><line x1="40" y1="40" x2="56" y2="56" stroke="{NAVY}" stroke-width="7" stroke-linecap="round"/>'
    if n == 't_steps':
        return f'<polyline points="8,52 8,40 22,40 22,28 36,28 36,16 52,16" fill="none" stroke="{NAVY}" stroke-width="5" stroke-linejoin="round"/><polygon points="48,8 58,16 48,24" {o(TEAL)}/>'
    raise ValueError('unknown icon ' + n)


ICONS3 = ['sun', 'moon', 'bed', 'bus', 'house', 'school', 'shop', 'bath', 'rubber', 'ruler', 'glue', 'shell', 'spoon', 'sock', 'shoe', 'button',
          't_strip', 't_table', 't_list', 't_draw', 't_back', 't_find', 't_steps']


# ------------------------------------------------------------------ clock

def clock(h=12, m=0, hide_hands=False, labels='all', digital=None, sector=None, mirror=False, ampm=None, ticks=True):
    """Analog clock. The hour hand sits at h + m/60 of the way round (the picture does not lie). Hour hand short and wide, minute hand long and thin.
    labels: 'all' (1-12) | 'quarters' (12, 3, 6, 9) | 'none'. sector=[from_min, to_min] shades that part of the face. mirror reflects the face left-right.
    digital: True or text under the clock ('[]' = an answer box 124 x 48 units: about 24 x 9 mm at the usual clock size); ampm adds 'a.m.' or 'p.m.'.
    Numerals are drawn after the hands with a white halo, and when numerals are printed the minute hand stops just inside the numeral ring, so the
    numeral a hand points at is never covered."""
    cx = cy = 110; R = 98
    body = []
    flip = -1 if mirror else 1
    ang = lambda deg: math.radians(deg - 90)
    X = lambda r, deg: cx + flip * r * math.cos(ang(deg))
    Y = lambda r, deg: cy + r * math.sin(ang(deg))
    body.append(f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="#fff" stroke="{NAVY}" stroke-width="5"/>')
    if sector:
        a0, a1 = sector[0] * 6, sector[1] * 6
        large = 1 if (a1 - a0) % 360 > 180 else 0
        body.append(f'<path d="M{cx} {cy} L{X(R - 4, a0):.1f} {Y(R - 4, a0):.1f} A{R - 4} {R - 4} 0 {large} {1 if not mirror else 0} {X(R - 4, a1):.1f} {Y(R - 4, a1):.1f} Z" fill="{YEL}" fill-opacity="0.65" stroke="{NAVY}" stroke-width="2"/>')
    if ticks:
        for k in range(60):
            L = 9 if k % 5 == 0 else 4
            body.append(f'<line x1="{X(R - 4, k * 6):.1f}" y1="{Y(R - 4, k * 6):.1f}" x2="{X(R - 4 - L, k * 6):.1f}" y2="{Y(R - 4 - L, k * 6):.1f}" stroke="{NAVY}" stroke-width="{3.2 if k % 5 == 0 else 1.4}"/>')
    numerals = labels != 'none'
    if not hide_hands:
        ha = ((h % 12) + m / 60.0) * 30; ma = m * 6
        hl, ml = (36, 54) if numerals else (46, 78)       # with numerals the minute hand tip stops inside the numeral ring
        body.append(f'<line x1="{cx}" y1="{cy}" x2="{X(hl, ha):.1f}" y2="{Y(hl, ha):.1f}" stroke="{NAVY}" stroke-width="10" stroke-linecap="round"/>')
        body.append(f'<line x1="{cx}" y1="{cy}" x2="{X(ml, ma):.1f}" y2="{Y(ml, ma):.1f}" stroke="{NAVY}" stroke-width="4.4" stroke-linecap="round"/>')
    if numerals:
        for k in range(1, 13):
            if labels == 'quarters' and k % 3: continue
            body.append(f'<text x="{X(71, k * 30):.1f}" y="{Y(71, k * 30) + 8:.1f}" font-size="23" font-weight="700" text-anchor="middle" fill="{NAVY}" stroke="#fff" stroke-width="4" paint-order="stroke" stroke-linejoin="round" font-family="{FONT}">{k}</text>')
    body.append(f'<circle cx="{cx}" cy="{cy}" r="7" fill="{NAVY}"/>')
    H = 220
    if digital:
        txt = digital if isinstance(digital, str) else f'{h}:{m:02d}'
        if ampm: txt += f' {ampm}'
        H = 280
        if txt == '[]':
            body.append(f'<rect x="{cx - 62}" y="228" width="124" height="48" rx="9" fill="#fff" stroke="{NAVY}" stroke-width="3.4"/>')
        else:
            body.append(f'<text x="{cx}" y="270" font-size="40" font-weight="800" text-anchor="middle" fill="{NAVY}" font-family="{FONT}">{_esc(txt)}</text>')
    return _svg(220, H, ''.join(body), 'clock' if hide_hands else f'clock showing {h}:{m:02d}')


# ------------------------------------------------------------------ money

COIN_SIZE = {'5c': 64, '10c': 70, '20c': 76, '50c': 82, '$1': 90}                         # one coin scale for every picture (viewBox is a fixed 620 wide)
NOTE_SIZE = {'$2': (128, 68), '$5': (140, 72), '$10': (152, 76), '$50': (164, 80), '$100': (176, 84)}
MONEY_W = 620                                                                              # same width for every money picture, so a coin is the same size in all of them


def _canon(v):
    """'50¢' and '50c' are the same coin; amounts are shown with the cent sign."""
    return str(v).replace('\u00a2', 'c')


def _show(v):
    return str(v).replace('c', '\u00a2') if str(v).endswith('c') else str(v)


def _coin(v, x, y, s=None):
    v = _canon(v); s = s or COIN_SIZE[v]
    fs = s * (0.40 if len(v) < 4 else 0.34)
    return (f'<rect x="{x - s / 2:.1f}" y="{y - s / 2:.1f}" width="{s:.1f}" height="{s:.1f}" rx="{s * 0.28:.1f}" fill="#F3E6B0" stroke="{NAVY}" stroke-width="2.6"/>'
            f'<rect x="{x - s / 2 + 4:.1f}" y="{y - s / 2 + 4:.1f}" width="{s - 8:.1f}" height="{s - 8:.1f}" rx="{s * 0.22:.1f}" fill="none" stroke="{NAVY}" stroke-width="1.2"/>'
            f'<text x="{x:.1f}" y="{y + fs * 0.36:.1f}" font-size="{fs:.1f}" font-weight="800" text-anchor="middle" fill="{NAVY}" font-family="{FONT}">{_show(v)}</text>')


def _note(v, x, y, wh=None):
    w, h = wh or NOTE_SIZE[v]
    return (f'<rect x="{x - w / 2:.1f}" y="{y - h / 2:.1f}" width="{w:.1f}" height="{h:.1f}" rx="4" fill="#E4F1E8" stroke="{NAVY}" stroke-width="2.6"/>'
            f'<rect x="{x - w / 2 + 5:.1f}" y="{y - h / 2 + 5:.1f}" width="{w - 10:.1f}" height="{h - 10:.1f}" rx="3" fill="none" stroke="{NAVY}" stroke-width="1.2" stroke-dasharray="4 3"/>'
            f'<text x="{x:.1f}" y="{y + h * 0.12:.1f}" font-size="{h * 0.46:.1f}" font-weight="800" text-anchor="middle" fill="{NAVY}" font-family="{FONT}">{v}</text>'
            f'<text x="{x:.1f}" y="{y + h / 2 - 7:.1f}" font-size="{max(8, h * 0.13):.1f}" font-weight="700" text-anchor="middle" fill="#3B4A6B" font-family="{FONT}">PLAY MONEY</text>')


def money(items=None, per_row=6, total=None, label=None):
    """Stylised play money. items=[{'v':'50c','n':2},{'v':'$5'}] (or plain strings). Coins are rounded squares of growing size, notes are
    rectangles of growing size, each with its amount printed (coins print the cent sign), so nothing depends on colour.
    Every picture is MONEY_W wide, so a coin has the same size in every picture; rows wrap when full (per_row caps the pieces in a row).
    total: text under the money ('[]' box)."""
    items = [(({'v': it} if isinstance(it, str) else it)) for it in (items or [])]
    flat = []
    for it in items: flat += [_canon(it['v'])] * int(it.get('n', 1))
    rows = [[]]; x = 20
    for v in flat:
        wv = (NOTE_SIZE[v][0] if v in NOTE_SIZE else COIN_SIZE[v])
        if rows[-1] and (len(rows[-1]) >= per_row or x + wv > MONEY_W - 20):
            rows.append([]); x = 20
        rows[-1].append(v); x += wv + 14
    rh = 100 if any(v in NOTE_SIZE for v in flat) else 96
    body = []
    for r, row in enumerate(rows):
        x = 20
        for v in row:
            wv = (NOTE_SIZE[v][0] if v in NOTE_SIZE else COIN_SIZE[v])
            x += wv / 2
            body.append(_note(v, x, 52 + r * rh) if v in NOTE_SIZE else _coin(v, x, 52 + r * rh))
            x += wv / 2 + 14
    W = MONEY_W
    H = 52 + (len(rows) - 1) * rh + 54
    if label: body.append(f'<text x="{W / 2:.0f}" y="{H + 18}" font-size="30" font-weight="800" text-anchor="middle" fill="{NAVY}" font-family="{FONT}">{_esc(label)}</text>'); H += 34
    if total is not None:
        H += 66
        body.append(token_svg(total, W / 2, H - 34, 170, 60, 40) if total in ('[]',) else f'<text x="{W / 2:.0f}" y="{H - 26}" font-size="44" font-weight="800" text-anchor="middle" fill="{NAVY}" font-family="{FONT}">{_esc(total)}</text>')
    return _svg(W, H, ''.join(body), 'play money ' + ', '.join(_show(x) for x in flat))


def price_tag(item='pencil', price='$5', hide_price=False, w=150):
    """A tag on a string with an item picture and a price. hide_price draws an answer box instead of the price."""
    body = [f'<path d="M20 20 H{w - 8} V{w + 20} H20 L6 {w / 2 + 6} Z" fill="#fff" stroke="{NAVY}" stroke-width="3.4" stroke-linejoin="round"/>',
            f'<circle cx="26" cy="{w / 2 + 6}" r="5" fill="{SOFT}" stroke="{NAVY}" stroke-width="2.4"/>',
            f'<path d="M26 {w / 2 + 6} C26 8 60 6 {w * 0.55} 6" fill="none" stroke="{NAVY}" stroke-width="2"/>']
    body.append(icon(item, w * 0.58, w * 0.38, w * 0.5))
    body.append(token_svg('[]', w * 0.58, w * 0.86, w * 0.7, 44, 30) if hide_price else f'<text x="{w * 0.58:.0f}" y="{w * 0.86 + 11:.0f}" font-size="34" font-weight="800" text-anchor="middle" fill="{NAVY}" font-family="{FONT}">{_esc(price)}</text>')
    return _svg(w + 10, w + 30, ''.join(body), f'price tag {item} {price}')


# ------------------------------------------------------------------ calendar

DAYS = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']


def calendar(start='Wed', days=31, highlight=(), hide=(), mark=(), week=None, labels=True, cell=52):
    """A generic month (no year, no holidays). start = weekday of day 1. highlight = yellow days, hide = answer boxes, mark = ringed days.
    week=k (0-based) shows only that week row."""
    s = DAYS.index(start[:3].title())
    hl, hd, mk = set(highlight), set(hide), set(mark)
    rows = (s + days + 6) // 7
    show = range(rows) if week is None else [week]
    W = 14 + 7 * cell; H = 14 + (len(show) + 1) * cell
    body = []
    for c, dn in enumerate(DAYS):
        body.append(f'<rect x="{7 + c * cell}" y="7" width="{cell}" height="{cell}" fill="{SKY}" stroke="{NAVY}" stroke-width="2.4"/><text x="{7 + c * cell + cell / 2}" y="{7 + cell / 2 + 8}" font-size="19" font-weight="800" text-anchor="middle" fill="{NAVY}" font-family="{FONT}">{dn}</text>')
    for ri, r in enumerate(show):
        for c in range(7):
            n = r * 7 + c - s + 1
            x = 7 + c * cell; y = 7 + (ri + 1) * cell
            ok = 1 <= n <= days
            fill = YEL if n in hl else ('#fff' if ok else '#F0F3F8')
            body.append(f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" fill="{fill}" stroke="{NAVY}" stroke-width="2"/>')
            if not ok: continue
            if n in hd: body.append(token_svg('[]', x + cell / 2, y + cell / 2, cell, cell, 26))
            else: body.append(f'<text x="{x + cell / 2}" y="{y + cell / 2 + 9}" font-size="26" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="{FONT}">{n}</text>')
            if n in mk: body.append(f'<circle cx="{x + cell / 2}" cy="{y + cell / 2}" r="{cell * 0.42}" fill="none" stroke="{RED}" stroke-width="3.4"/>')
    return _svg(W, H, ''.join(body), 'calendar month starting on ' + start)


# ------------------------------------------------------------------ stick patterns

def stick_pattern(shape='triangle', n=3, hide_last=False, label_each=False, side=80, show_count=False):
    """Triangles (3, 5, 7 sticks) or squares (4, 7, 10 sticks) in a row, drawn with sticks (lines). hide_last draws the next pattern as a dashed ghost with '?'."""
    body = []; k = n + (1 if hide_last else 0)
    def stick(x1, y1, x2, y2, ghost=False):
        # each stick is its own bar: pulled in by GAP at both ends so neighbouring sticks never merge into one line
        L = math.hypot(x2 - x1, y2 - y1) or 1.0
        ux, uy = (x2 - x1) / L, (y2 - y1) / L
        g = 5.5
        x1, y1, x2, y2 = x1 + ux * g, y1 + uy * g, x2 - ux * g, y2 - uy * g
        dash = ' stroke-dasharray="7 6"' if ghost else ''
        col = '#8A94AD' if ghost else NAVY
        body.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{col}" stroke-width="7" stroke-linecap="butt"{dash}/>')
        if not ghost:
            body.append(f'<circle cx="{x1:.1f}" cy="{y1:.1f}" r="4" fill="{YEL}" stroke="{NAVY}" stroke-width="1.6"/><circle cx="{x2:.1f}" cy="{y2:.1f}" r="4" fill="{YEL}" stroke="{NAVY}" stroke-width="1.6"/>')
    x0 = 24; yb = 20 + side * 0.9 + 6
    if shape == 'triangle':
        h = side * 0.866; half = side / 2
        # zigzag row: points alternate bottom (y=yb) and top (y=yb-h) every half side; triangle j uses points j, j+1, j+2
        P = [(x0 + j * half, yb if j % 2 == 0 else yb - h) for j in range(k + 2)]
        drawn = set()
        for j in range(k):
            g = hide_last and j == k - 1
            for a, b in ((j, j + 1), (j + 1, j + 2), (j, j + 2)):
                if (a, b) in drawn: continue
                drawn.add((a, b)); stick(P[a][0], P[a][1], P[b][0], P[b][1], g)
        W = x0 * 2 + (k + 1) * half
        if hide_last: body.append(f'<text x="{P[k][0] + 6:.0f}" y="{yb - h / 2 + 12:.0f}" font-size="34" font-weight="800" text-anchor="middle" fill="{NAVY}" font-family="{FONT}">?</text>')
    else:
        s_ = side * 0.9
        for j in range(k):
            g = hide_last and j == k - 1
            x = x0 + j * s_
            for (x1, y1, x2, y2) in ((x, yb, x + s_, yb), (x, yb - s_, x + s_, yb - s_), (x + s_, yb, x + s_, yb - s_)) + (((x, yb, x, yb - s_),) if j == 0 else ()):
                stick(x1, y1, x2, y2, g)
        W = x0 * 2 + k * s_
        if hide_last: body.append(f'<text x="{x0 + (k - 0.5) * s_:.0f}" y="{yb - s_ / 2 + 12:.0f}" font-size="34" font-weight="800" text-anchor="middle" fill="{NAVY}" font-family="{FONT}">?</text>')
    H = yb + 50
    if label_each:
        for j in range(n):
            xx = (x0 + j * (side / 2 * 2 if shape == 'triangle' else side * 0.9) + (side / 2 if shape == 'triangle' else side * 0.45)) if shape != 'triangle' else x0 + j * side / 2 + side / 2
            body.append(f'<text x="{xx:.0f}" y="{H - 14}" font-size="26" font-weight="800" text-anchor="middle" fill="{TEAL}" font-family="{FONT}">{j + 1}</text>')
    return _svg(max(W, 240), H, ''.join(body), f'{n} {shape}s made of sticks')


# ------------------------------------------------------------------ 2D shapes

def shapes2d(shape='circle', parts=1, shade=(), fold=None, compose=None, size=150, equal_marks=False, label=None):    # size = drawing size in units; the page percentage is the figure's own 'size' (svg.render_visual)
    """shape: circle | half_circle | quarter_circle | square | rectangle | triangle. parts: 1, 2 (halves) or 4 (quarters) equal parts drawn as lines;
    shade = part numbers (1-based) shaded; fold = 'v' | 'h' draws a dashed fold line; compose='house'|'boat' draws a figure made from shapes."""
    S = size; cx = cy = S / 2 + 12; W = S + 24
    sh = set(shade); body = []
    def fill(i): return YEL if i in sh else '#fff'
    if compose == 'house':
        body.append(f'<rect x="{cx - 50}" y="{cy - 10}" width="100" height="70" {_o("#F1D9AE")}/><polygon points="{cx - 62},{cy - 10} {cx},{cy - 62} {cx + 62},{cy - 10}" {_o("#D64545")}/><rect x="{cx - 12}" y="{cy + 22}" width="24" height="38" {_o("#fff")}/><rect x="{cx - 40}" y="{cy + 4}" width="20" height="20" {_o(SKY)}/>')
        return _svg(W, S + 24, ''.join(body), 'a house made of shapes')
    if compose == 'boat':
        body.append(f'<path d="M{cx - 66} {cy + 20} H{cx + 66} L{cx + 40} {cy + 56} H{cx - 40} Z" {_o("#3B6FC9")}/><polygon points="{cx},{cy - 60} {cx + 44},{cy + 14} {cx},{cy + 14}" {_o("#fff")}/><polygon points="{cx - 4},{cy - 40} {cx - 4},{cy + 14} {cx - 40},{cy + 14}" {_o(YEL)}/>')
        return _svg(W, S + 24, ''.join(body), 'a boat made of shapes')
    R = S / 2 - 4
    if shape == 'circle':
        if parts == 1: body.append(f'<circle cx="{cx}" cy="{cy}" r="{R}" {_o(fill(1))}/>')
        else:
            n = parts
            for i in range(n):
                a0 = -90 + i * 360 / n; a1 = a0 + 360 / n
                x0_, y0_ = cx + R * math.cos(math.radians(a0)), cy + R * math.sin(math.radians(a0)); x1_, y1_ = cx + R * math.cos(math.radians(a1)), cy + R * math.sin(math.radians(a1))
                body.append(f'<path d="M{cx} {cy} L{x0_:.1f} {y0_:.1f} A{R} {R} 0 {1 if n == 1 else 0} 1 {x1_:.1f} {y1_:.1f} Z" {_o(fill(i + 1))}/>')
    elif shape == 'half_circle':
        body.append(f'<path d="M{cx - R} {cy + R / 2} A{R} {R} 0 0 1 {cx + R} {cy + R / 2} Z" {_o(fill(1))}/>')
        if parts == 2: body.append(f'<line x1="{cx}" y1="{cy + R / 2}" x2="{cx}" y2="{cy - R / 2}" stroke="{NAVY}" stroke-width="{SW}"/>')
    elif shape == 'quarter_circle':
        body.append(f'<path d="M{cx - R / 2} {cy + R / 2} V{cy - R / 2} A{R} {R} 0 0 1 {cx + R / 2} {cy + R / 2} Z" {_o(fill(1))}/>')
    elif shape in ('square', 'rectangle'):
        w = R * 2; h = R * 2 if shape == 'square' else R * 1.3
        x0 = cx - w / 2; y0 = cy - h / 2
        if parts == 1: body.append(f'<rect x="{x0}" y="{y0}" width="{w}" height="{h}" {_o(fill(1))}/>')
        elif parts == 2:
            vertical = fold != 'h'
            for i in range(2):
                rx, ry, rw, rh = (x0 + i * w / 2, y0, w / 2, h) if vertical else (x0, y0 + i * h / 2, w, h / 2)
                body.append(f'<rect x="{rx}" y="{ry}" width="{rw}" height="{rh}" {_o(fill(i + 1))}/>')
        else:
            for i in range(4):
                rx, ry = x0 + (i % 2) * w / 2, y0 + (i // 2) * h / 2
                body.append(f'<rect x="{rx}" y="{ry}" width="{w / 2}" height="{h / 2}" {_o(fill(i + 1))}/>')
    elif shape == 'triangle':
        body.append(f'<polygon points="{cx},{cy - R} {cx + R},{cy + R * 0.8} {cx - R},{cy + R * 0.8}" {_o(fill(1))}/>')
    else:
        raise ValueError('unknown shape ' + shape)
    if fold and parts == 1:
        body.append(f'<line x1="{cx}" y1="{cy - R - 6}" x2="{cx}" y2="{cy + R + 6}" stroke="{RED}" stroke-width="3.4" stroke-dasharray="9 6"/>' if fold == 'v' else f'<line x1="{cx - R - 6}" y1="{cy}" x2="{cx + R + 6}" y2="{cy}" stroke="{RED}" stroke-width="3.4" stroke-dasharray="9 6"/>')
    H = S + 24 + (30 if label else 0)
    if label: body.append(f'<text x="{cx}" y="{H - 10}" font-size="26" font-weight="800" text-anchor="middle" fill="{NAVY}" font-family="{FONT}">{_esc(label)}</text>')
    return _svg(W, H, ''.join(body), f'{shape} in {parts} parts')


# ------------------------------------------------------------------ grid

def grid(rows=3, cols=3, kind='dots', poly=None, route=None, start=None, end=None, squares=(), counts=None, mirror=None, mark=(), cell=64, blank=False):
    """kind='dots': (cols+1) x (rows+1) dots; kind='squares': rows x cols squares. Coordinates are (x, y) from the top-left dot.
    poly=[[x,y],...] a filled polygon through dots; route=[[x,y],...] arrows along a path; start/end=[x,y] markers; squares=[[r,c],...] yellow;
    counts={'r,c': text} written in a square ('[]' for an answer box); mirror=k draws a dashed mirror line after column k; blank=True leaves the right half empty."""
    pad = 30; W = pad * 2 + cols * cell; H = pad * 2 + rows * cell
    P = lambda x, y: (pad + x * cell, pad + y * cell)
    body = []
    for (r, c) in [tuple(s) for s in squares]:
        x, y = P(c, r); body.append(f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" fill="{YEL}"/>')
    for k, t in (counts or {}).items():
        r, c = [int(z) for z in k.split(',')]; x, y = P(c, r)
        body.append(token_svg(t, x + cell / 2, y + cell / 2, cell, cell, 30))
    if poly:
        pts = ' '.join('%.1f,%.1f' % P(*p) for p in poly)
        body.append(f'<polygon points="{pts}" fill="{SKY}" stroke="{NAVY}" stroke-width="4.4" stroke-linejoin="round"/>')
    if kind == 'squares':
        for r in range(rows + 1): body.append(f'<line x1="{pad}" y1="{pad + r * cell}" x2="{pad + cols * cell}" y2="{pad + r * cell}" stroke="{NAVY}" stroke-width="2.4"/>')
        for c in range(cols + 1): body.append(f'<line x1="{pad + c * cell}" y1="{pad}" x2="{pad + c * cell}" y2="{pad + rows * cell}" stroke="{NAVY}" stroke-width="2.4"/>')
    else:
        for r in range(rows + 1):
            for c in range(cols + 1):
                x, y = P(c, r); body.append(f'<circle cx="{x}" cy="{y}" r="5.5" fill="{NAVY}"/>')
    if route:
        for a, b in zip(route, route[1:]):
            (x1, y1), (x2, y2) = P(*a), P(*b)
            ang = math.atan2(y2 - y1, x2 - x1); hx, hy = x2 - 12 * math.cos(ang), y2 - 12 * math.sin(ang)
            body.append(f'<line x1="{x1}" y1="{y1}" x2="{hx:.1f}" y2="{hy:.1f}" stroke="{RED}" stroke-width="6" stroke-linecap="round"/>')
            lx, ly = -math.sin(ang), math.cos(ang)
            body.append(f'<polygon points="{x2:.1f},{y2:.1f} {x2 - 16 * math.cos(ang) + 9 * lx:.1f},{y2 - 16 * math.sin(ang) + 9 * ly:.1f} {x2 - 16 * math.cos(ang) - 9 * lx:.1f},{y2 - 16 * math.sin(ang) - 9 * ly:.1f}" fill="{RED}"/>')
    for p in mark:
        x, y = P(*p); body.append(f'<circle cx="{x}" cy="{y}" r="12" fill="none" stroke="{TEAL}" stroke-width="4.4"/>')
    if start:
        x, y = P(*start); body.append(f'<circle cx="{x}" cy="{y}" r="13" fill="{TEAL}" stroke="{NAVY}" stroke-width="2.6"/><text x="{x}" y="{y + 6}" font-size="17" font-weight="800" text-anchor="middle" fill="#fff" font-family="{FONT}">S</text>')
    if end:
        x, y = P(*end); body.append(f'<rect x="{x - 13}" y="{y - 13}" width="26" height="26" rx="4" fill="{YEL}" stroke="{NAVY}" stroke-width="2.6"/><text x="{x}" y="{y + 6}" font-size="17" font-weight="800" text-anchor="middle" fill="{NAVY}" font-family="{FONT}">E</text>')
    if mirror is not None:
        x = pad + mirror * cell; body.append(f'<line x1="{x}" y1="{pad - 16}" x2="{x}" y2="{pad + rows * cell + 16}" stroke="{TEAL}" stroke-width="4" stroke-dasharray="10 7"/>')
    return _svg(W, H, ''.join(body), f'{kind} grid {cols} by {rows}')


def _badge(letter, x=26, y=26, r=21):
    """A round letter tag (A, B, C ...) for pictures that are chosen between: cube stacks, folded papers, networks."""
    return (f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff" stroke="{NAVY}" stroke-width="3"/>'
            f'<text x="{x}" y="{y + r * 0.38:.1f}" font-size="{r * 1.15:.1f}" font-weight="800" text-anchor="middle" fill="{NAVY}" font-family="{FONT}">{_esc(letter)}</text>')


def _tagged(svgtxt, letter):
    """Add a letter badge at the top-left of an already built figure (the viewBox grows 50 units to the left so the badge never covers the picture)."""
    if not letter: return svgtxt
    import re as _re
    m = _re.search(r'viewBox="0 0 (\d+) (\d+)"', svgtxt)
    w, h = int(m.group(1)), int(m.group(2))
    inner = svgtxt[svgtxt.index('>') + 1:svgtxt.rindex('</svg>')]
    head = svgtxt[:svgtxt.index('>') + 1].replace(m.group(0), f'viewBox="0 0 {w + 52} {max(h, 56)}"')
    return head + _badge(letter, 26, 26) + f'<g transform="translate(52,0)">{inner}</g></svg>'


# ------------------------------------------------------------------ cube stack

def cube_stack(heights=((1,),), mode='iso', s=46, hide_count=False):
    """heights: rows (back to front) of columns (left to right), each 0-3. mode 'iso' = isometric picture; 'top' = numbered top view; 'views' = front view
    (tallest in each column) beside a numbered top view."""
    R = len(heights); C = max(len(r) for r in heights)
    body = []
    def top_view(x0, y0, c=40):
        for r in range(R):
            for k in range(C):
                h = heights[r][k] if k < len(heights[r]) else 0
                body.append(f'<rect x="{x0 + k * c}" y="{y0 + r * c}" width="{c}" height="{c}" fill="#fff" stroke="{NAVY}" stroke-width="2.4"/><text x="{x0 + k * c + c / 2}" y="{y0 + r * c + c / 2 + 9}" font-size="26" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="{FONT}">{h}</text>')
        return x0 + C * c, y0 + R * c
    if mode == 'top':
        w, h = top_view(10, 10)
        return _svg(w + 10, h + 10, ''.join(body), 'top view of a stack')
    if mode == 'views':
        # front view: bars of squares, then the numbered top view
        for k in range(C):
            col = max((heights[r][k] if k < len(heights[r]) else 0) for r in range(R))
            for z in range(col):
                body.append(f'<rect x="{10 + k * 40}" y="{10 + (2 - z) * 40}" width="40" height="40" fill="{SKY}" stroke="{NAVY}" stroke-width="2.4"/>')
        body.append(f'<text x="{10 + C * 20}" y="146" font-size="19" font-weight="800" text-anchor="middle" fill="{NAVY}" font-family="{FONT}">FRONT</text>')
        x1 = 10 + C * 40 + 40
        w, h = top_view(x1, 10)
        body.append(f'<text x="{(x1 + w) / 2:.0f}" y="146" font-size="19" font-weight="800" text-anchor="middle" fill="{NAVY}" font-family="{FONT}">TOP</text>')
        return _svg(w + 10, 160, ''.join(body), 'front and top views of a stack')
    w3, h3 = s * 0.866, s * 0.5
    mh = max([h for r_ in heights for h in r_] + [1])
    ox = 20 + R * w3; oy = 20 + mh * s
    cells = [(r + c, r, c) for r in range(R) for c in range(len(heights[r]))]
    for _, r, c in sorted(cells):
        for z in range(heights[r][c]):
            x = ox + (c - r) * w3; y = oy + (c + r) * h3 - z * s
            top = f'M{x:.1f} {y - s:.1f} l{w3:.1f} {h3:.1f} l{-w3:.1f} {h3:.1f} l{-w3:.1f} {-h3:.1f} Z'
            left = f'M{x - w3:.1f} {y - s + h3:.1f} l{w3:.1f} {h3:.1f} v{s:.1f} l{-w3:.1f} {-h3:.1f} Z'
            right = f'M{x + w3:.1f} {y - s + h3:.1f} l{-w3:.1f} {h3:.1f} v{s:.1f} l{w3:.1f} {-h3:.1f} Z'
            body.append(f'<path d="{left}" fill="#9FB6DE" stroke="{NAVY}" stroke-width="2.4" stroke-linejoin="round"/><path d="{right}" fill="#C8D6EF" stroke="{NAVY}" stroke-width="2.4" stroke-linejoin="round"/><path d="{top}" fill="#EEF3FB" stroke="{NAVY}" stroke-width="2.4" stroke-linejoin="round"/>')
    W = 40 + (R + C) * w3; H = oy + (R + C) * h3 + 20        # tight to the stack: a low stack is drawn larger
    return _svg(W, H, ''.join(body), 'a stack of cubes')


# ------------------------------------------------------------------ fold and punch

def fold_punch(stage='paper', fold='v', holes=(), size=150):
    """stage 'paper': a square with dashed fold line(s) (fold 'v', 'h' or 'quarter'); 'folded': the folded paper with hole marks (hole = [u, v] in 0..1 of the folded
    paper); 'unfolded': the opened square with every hole, mirrored (for the answer key)."""
    S = size; o = 14; body = []
    X = lambda u: o + u * S; Y = lambda v: o + v * S
    if stage == 'paper':
        body.append(f'<rect x="{o}" y="{o}" width="{S}" height="{S}" {_o("#fff")}/>')
        if fold in ('v', 'quarter'): body.append(f'<line x1="{X(.5)}" y1="{o - 6}" x2="{X(.5)}" y2="{o + S + 6}" stroke="{RED}" stroke-width="3.4" stroke-dasharray="9 6"/>')
        if fold in ('h', 'quarter'): body.append(f'<line x1="{o - 6}" y1="{Y(.5)}" x2="{o + S + 6}" y2="{Y(.5)}" stroke="{RED}" stroke-width="3.4" stroke-dasharray="9 6"/>')
        return _svg(S + 2 * o, S + 2 * o, ''.join(body), 'paper with a fold line')
    fw = S / 2 if fold in ('v', 'quarter') else S; fh = S / 2 if fold in ('h', 'quarter') else S
    if stage == 'folded':
        body.append(f'<rect x="{o}" y="{o}" width="{fw}" height="{fh}" {_o("#fff")}/>')
        for (u, v) in holes: body.append(f'<circle cx="{o + u * fw:.1f}" cy="{o + v * fh:.1f}" r="9" fill="{NAVY}"/>')
        return _svg(fw + 2 * o, fh + 2 * o, ''.join(body), 'folded paper with a hole')
    body.append(f'<rect x="{o}" y="{o}" width="{S}" height="{S}" {_o("#fff")}/>')
    for (u, v) in holes:
        xs = [u * fw + (S - fw if fold in ('v', 'quarter') else 0)]; ys = [v * fh + (S - fh if fold in ('h', 'quarter') else 0)]
        pts = {(xs[0], ys[0])}
        if fold in ('v', 'quarter'): pts |= {(S - x, y) for x, y in list(pts)}
        if fold in ('h', 'quarter'): pts |= {(x, S - y) for x, y in list(pts)}
        for (x, y) in pts: body.append(f'<circle cx="{o + x:.1f}" cy="{o + y:.1f}" r="9" fill="{NAVY}"/>')
    return _svg(S + 2 * o, S + 2 * o, ''.join(body), 'opened paper with holes')


# ------------------------------------------------------------------ panels (odd one out, spot the difference, missing tile)

FILLS = ['#F6C9D0', '#BFE3DC', '#FFE59A', '#C9B6F0']


def _tile_shape(shape, x, y, r, fillc, pat, turn, pid, shadow=False):
    f = '#2B3552' if shadow else (f'url(#{pid}{pat})' if pat else fillc)       # shadow: a solid dark silhouette (shadow match)
    st = f'stroke="{NAVY}" stroke-width="3" stroke-linejoin="round"'
    t = f'transform="rotate({turn} {x:.1f} {y:.1f})"'
    if shape == 'circle': return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="{f}" {st}/>'
    if shape == 'square': return f'<rect x="{x - r:.1f}" y="{y - r:.1f}" width="{2 * r:.1f}" height="{2 * r:.1f}" fill="{f}" {st} {t}/>'
    if shape == 'triangle': return f'<polygon points="{x:.1f},{y - r:.1f} {x + r * 1.1:.1f},{y + r * 0.85:.1f} {x - r * 1.1:.1f},{y + r * 0.85:.1f}" fill="{f}" {st} {t}/>'
    if shape == 'star':
        pts = ' '.join(f'{x + (r if j % 2 == 0 else r * 0.45) * math.sin(j * math.pi / 5):.1f},{y - (r if j % 2 == 0 else r * 0.45) * math.cos(j * math.pi / 5):.1f}' for j in range(10))
        return f'<polygon points="{pts}" fill="{f}" {st} {t}/>'
    raise ValueError('unknown panel shape ' + shape)


_PANEL_N = 0


def panel(tiles=None, cols=None, hide=(), labels=None, cell=130, tag='p'):
    """A row or grid of tiles. tile = {shape: circle|square|triangle|star, n: 1-4, size: s|m|l, colour: 0-3, pattern: 0-3, turn: degrees}.
    colour and pattern together show a feature in grey print (pattern 0 plain, 1 stripes, 2 dots, 3 cross-hatch). hide=[index] draws a '?' tile.
    labels=['A','B',...] prints a letter under each tile (or a '[]' answer box). tile 'shadow': true draws that tile as a dark silhouette (shadow match);
    a tile may also set 'turn'. Every tile with shadow keeps its shape, size, number and turn, so only the inside is hidden."""
    tiles = tiles or []
    cols = cols or len(tiles)
    rows = (len(tiles) + cols - 1) // cols
    global _PANEL_N
    _PANEL_N += 1
    pid = f'{tag}pat{_PANEL_N}x'
    body = []
    dl = []
    def _pats(i, x0, y0):
        # patterns are anchored to the tile's own corner, so identical tiles always show identical stripes and dots
        o = f'patternUnits="userSpaceOnUse" x="0" y="0"'
        return (f'<pattern id="{pid}{i}_1" width="14" height="14" {o} patternTransform="translate({x0} {y0}) rotate(45)"><rect width="14" height="14" fill="#fff"/><rect x="0" y="0" width="5.5" height="14" fill="{NAVY}"/></pattern>'
                f'<pattern id="{pid}{i}_2" width="19" height="19" {o} patternTransform="translate({x0 + 2} {y0 + 2})"><rect width="19" height="19" fill="#fff"/><circle cx="9.5" cy="9.5" r="4.6" fill="{NAVY}"/></pattern>'
                f'<pattern id="{pid}{i}_3" width="16" height="16" {o} patternTransform="translate({x0} {y0})"><rect width="16" height="16" fill="#fff"/><path d="M0 0 L16 16 M16 0 L0 16" stroke="{NAVY}" stroke-width="3.4"/></pattern>')
    rsz = {'s': 0.2, 'm': 0.3, 'l': 0.42}
    lab_h = 36 if labels else 0
    for i, t in enumerate(tiles):
        r, c = divmod(i, cols); x0 = 10 + c * (cell + 12); y0 = 10 + r * (cell + 12 + lab_h)
        dl.append(_pats(i, x0, y0))
        body.append(f'<rect x="{x0}" y="{y0}" width="{cell}" height="{cell}" rx="10" fill="#fff" stroke="{NAVY}" stroke-width="3"/>')
        if i in hide:
            body.append(f'<text x="{x0 + cell / 2}" y="{y0 + cell / 2 + 20}" font-size="64" font-weight="800" text-anchor="middle" fill="#8A94AD" font-family="{FONT}">?</text>')
        else:
            n = int(t.get('n', 1)); rad = rsz[t.get('size', 'm')] * cell * (1 if n == 1 else 0.72 if n == 2 else 0.58)
            if n == 1: pos = [(0.5, 0.5)]
            elif n == 2: pos = [(0.3, 0.5), (0.7, 0.5)]
            elif n == 3: pos = [(0.5, 0.28), (0.28, 0.7), (0.72, 0.7)]
            else: pos = [(0.3, 0.3), (0.7, 0.3), (0.3, 0.7), (0.7, 0.7)]
            for (px, py) in pos:
                body.append(_tile_shape(t.get('shape', 'circle'), x0 + px * cell, y0 + py * cell, rad, FILLS[int(t.get('colour', 0)) % 4], int(t.get('pattern', 0)), t.get('turn', 0), pid + str(i) + '_', bool(t.get('shadow'))))
        if labels:
            lt = labels[i] if i < len(labels) else ''
            body.append(token_svg(lt, x0 + cell / 2, y0 + cell + 24, 60, 40, 28) if lt == '[]' else f'<text x="{x0 + cell / 2}" y="{y0 + cell + 30}" font-size="28" font-weight="800" text-anchor="middle" fill="{NAVY}" font-family="{FONT}">{_esc(lt)}</text>')
    W = 20 + cols * (cell + 12); H = 20 + rows * (cell + 12 + lab_h)
    return _svg(W, H, '<defs>' + ''.join(dl) + '</defs>' + ''.join(body), 'a row of picture tiles')


# ------------------------------------------------------------------ network (handshakes)

def network(n=4, lines=None, all_lines=False, labels=None, r=95, count=None, tag=None):
    """n dots on a ring; lines=[[a,b],...] (0-based) or all_lines=True for every pair. count='[]' writes an answer box in the middle."""
    nr = 24 if labels else 17                   # node radius: big enough for a letter or a name that a child can read
    cx = cy = r + 40; body = []
    pts = [(cx + r * math.cos(-math.pi / 2 + 2 * math.pi * k / n), cy + r * math.sin(-math.pi / 2 + 2 * math.pi * k / n)) for k in range(n)]
    ls = [(a, b) for a in range(n) for b in range(a + 1, n)] if all_lines else [tuple(x) for x in (lines or [])]
    for a, b in ls: body.append(f'<line x1="{pts[a][0]:.1f}" y1="{pts[a][1]:.1f}" x2="{pts[b][0]:.1f}" y2="{pts[b][1]:.1f}" stroke="{TEAL}" stroke-width="4"/>')
    for k, (x, y) in enumerate(pts):
        body.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{nr}" fill="{YEL}" stroke="{NAVY}" stroke-width="3"/>')
        if labels: body.append(f'<text x="{x:.1f}" y="{y + nr * 0.38:.1f}" font-size="{nr * 1.15:.1f}" font-weight="800" text-anchor="middle" fill="{NAVY}" font-family="{FONT}">{_esc(labels[k])}</text>')
    if count is not None: body.append(token_svg(count, cx, cy, 70, 52, 34))
    return _tagged(_svg(2 * cx, 2 * cy, ''.join(body), f'{n} dots joined by lines'), tag)


# ------------------------------------------------------------------ picture graph

def picture_graph(rows=None, icon_name='apple', each=1, title=None, orient='rows', key=True, tally=False, cell=None, label_w=None):
    """rows=[{'label':'Cats','n':5,'hide':[4]}]; n may end in .5 (half picture). each = how many each picture means (shown in the key). orient 'rows' (bars go right)
    or 'cols' (bars go up). tally=True draws tally marks (groups of five) instead of pictures. hide=[k] draws an empty dashed place for picture k.
    cell=None picks the largest picture that keeps the figure about 640 units wide (at most 76, so a short graph has big pictures)."""
    rows = rows or []
    body = []; mx = max([math.ceil(r.get('n', 0)) for r in rows] + [1])
    if label_w is None: label_w = max(100, 15 * max([len(str(r.get('label', ''))) for r in rows] + [4]) + 18) if orient == 'rows' else 0
    if cell is None:
        cell = min(76, (640 - label_w) / mx) if orient == 'rows' else min(76, 640 / max(len(rows), 1) - 20)
        cell = max(cell, 44)
    top = 50 if title else 12
    def pic(i, x, y, r, k):
        if k in r.get('hide', ()):
            return f'<rect x="{x - cell * .4:.1f}" y="{y - cell * .4:.1f}" width="{cell * .8:.1f}" height="{cell * .8:.1f}" rx="8" fill="#fff" stroke="#8A94AD" stroke-width="2.6" stroke-dasharray="6 5"/>'
        frac = r['n'] - k
        if 0 < frac < 1:
            cid = f'cl{i}_{k}'
            return f'<clipPath id="{cid}"><rect x="{x - cell / 2:.1f}" y="{y - cell / 2:.1f}" width="{cell / 2:.1f}" height="{cell:.1f}"/></clipPath><g clip-path="url(#{cid})">{icon(icon_name, x, y, cell * .9)}</g>'
        return icon(icon_name, x, y, cell * .9)
    if title: body.append(f'<text x="{(label_w + mx * cell) / 2 + 10:.0f}" y="32" font-size="30" font-weight="800" text-anchor="middle" fill="{NAVY}" font-family="{FONT}">{_esc(title)}</text>')
    if orient == 'rows':
        for i, r in enumerate(rows):
            y = top + i * (cell + 10) + cell / 2
            body.append(f'<text x="{label_w - 12}" y="{y + 9:.1f}" font-size="26" font-weight="800" text-anchor="end" fill="{NAVY}" font-family="{FONT}">{_esc(r["label"])}</text>')
            body.append(f'<line x1="{label_w}" y1="{y + cell / 2 + 4:.1f}" x2="{label_w + mx * cell + 8}" y2="{y + cell / 2 + 4:.1f}" stroke="#C9D2E3" stroke-width="2"/>')
            if tally:
                for g in range(math.ceil(r['n'] / 5)):
                    k5 = min(5, int(r['n']) - 5 * g)
                    gx = label_w + 12 + g * 52
                    for t in range(min(4, k5)): body.append(f'<line x1="{gx + t * 10}" y1="{y - 18}" x2="{gx + t * 10}" y2="{y + 18}" stroke="{NAVY}" stroke-width="4" stroke-linecap="round"/>')
                    if k5 == 5: body.append(f'<line x1="{gx - 6}" y1="{y + 12}" x2="{gx + 44}" y2="{y - 12}" stroke="{NAVY}" stroke-width="4" stroke-linecap="round"/>')
            else:
                for k in range(math.ceil(r['n'])): body.append(pic(i, label_w + k * cell + cell / 2 + 4, y, r, k))
        W = label_w + mx * cell + 20; H = top + len(rows) * (cell + 10) + 8
    else:
        bw = cell + 20
        base = top + mx * cell + 6
        for i, r in enumerate(rows):
            x = 20 + i * bw + bw / 2
            for k in range(math.ceil(r['n'])): body.append(pic(i, x, base - k * cell - cell / 2, r, k))
            body.append(f'<text x="{x:.1f}" y="{base + 32}" font-size="24" font-weight="800" text-anchor="middle" fill="{NAVY}" font-family="{FONT}">{_esc(r["label"])}</text>')
        body.append(f'<line x1="14" y1="{base + 2}" x2="{26 + len(rows) * bw}" y2="{base + 2}" stroke="{NAVY}" stroke-width="3"/>')
        W = 40 + len(rows) * bw; H = base + 48
    if key:
        kx = 12; ky = H + 6
        body.append(icon(icon_name, kx + 24, ky + 26, 40) if not tally else '')
        body.append(f'<text x="{kx + 54}" y="{ky + 34}" font-size="24" font-weight="800" fill="{NAVY}" font-family="{FONT}">{"each tally = 1" if tally else "= " + str(each)}</text>')
        H += 56
    return _svg(max(W, 300), H, ''.join(body), 'picture graph')


# ------------------------------------------------------------------ dispatch

def _draw_size(v):
    """Drawing size of a shapes2d / fold_punch figure. 'draw' is the drawing size; 'size' is only the share of the page column
    (svg.render_visual). Old lessons that gave a number in 'size' and no 'draw' keep drawing at that size."""
    if v.get('draw') is not None: return v['draw']
    sz = v.get('size')
    return sz if isinstance(sz, (int, float)) and not isinstance(sz, bool) and sz >= 60 else 150


def render(v):
    t = v['type']
    if t == 'clock': return clock(v.get('h', 12), v.get('m', 0), v.get('hide_hands', False), v.get('labels', 'all'), v.get('digital'), v.get('sector'), v.get('mirror', False), v.get('ampm'))
    if t == 'money': return money(v.get('items'), v.get('per_row', 6), v.get('total'), v.get('label'))
    if t == 'price_tag': return price_tag(v.get('item', 'pencil'), v.get('price', '$5'), v.get('hide_price', False))
    if t == 'calendar': return calendar(v.get('start', 'Wed'), v.get('days', 31), v.get('highlight', ()), v.get('hide', ()), v.get('mark', ()), v.get('week'))
    if t == 'stick_pattern': return stick_pattern(v.get('shape', 'triangle'), v.get('n', 3), v.get('hide_last', False), v.get('label_each', False))
    if t == 'shapes2d': return _tagged(shapes2d(v.get('shape', 'circle'), v.get('parts', 1), v.get('shade', ()), v.get('fold'), v.get('compose'), _draw_size(v), label=v.get('label')), v.get('tag'))
    if t == 'grid': return grid(v.get('rows', 3), v.get('cols', 3), v.get('kind', 'dots'), v.get('poly'), v.get('route'), v.get('start'), v.get('end'), v.get('squares', ()), v.get('counts'), v.get('mirror'), v.get('mark', ()), v.get('cell', 64))
    if t == 'cube_stack': return _tagged(cube_stack([tuple(r) for r in v.get('heights', [[1]])], v.get('mode', 'iso')), v.get('tag'))
    if t == 'fold_punch': return _tagged(fold_punch(v.get('stage', 'paper'), v.get('fold', 'v'), [tuple(h) for h in v.get('holes', ())], v.get('draw') or 150), v.get('tag'))
    if t == 'panel': return _tagged(panel(v.get('tiles'), v.get('cols'), tuple(v.get('hide', ())), v.get('labels'), v.get('cell', 130)), v.get('tag'))
    if t == 'network': return network(v.get('n', 4), v.get('lines'), v.get('all', False), v.get('labels'), count=v.get('count'), tag=v.get('tag'))
    if t == 'picture_graph': return picture_graph(v.get('rows'), v.get('icon', 'apple'), v.get('each', 1), v.get('title'), v.get('orient', 'rows'), v.get('key', True), v.get('tally', False))
    return None


FIGURES3 = {'clock', 'money', 'price_tag', 'calendar', 'stick_pattern', 'shapes2d', 'grid', 'cube_stack', 'fold_punch', 'panel', 'network', 'picture_graph'}


# ================================================================== kit pages
# Every kit is drawn on a 700-unit wide viewBox that prints at kit_pct(spec) percent of the 182 mm text width, so a size in millimetres is exact:
# u = units per mm = 700 / (182 * pct / 100). Cut lines are at least 6 mm apart (KIT_GAP). A kit may need more than one page: the pages are joined with
# KIT_SEP and b_print.kit_pages prints one page for each.

PAGE_MM = 182.0
KIT_GAP = 6.0                       # mm between neighbouring cut lines
KIT_SEP = '<!--KITPAGE-->'
KIT_AVAIL_MM = 200.0                # height left on a kit page under the header, title, intro and note
FOLD_D_MM = 88                      # default circle / square size for the fold-shapes kit ("about 9 cm"); any d_mm is honoured
KIT_PCT = {'clock_kit': 100, 'event_cards': 100, 'play_money': 100, 'price_tags': 100, 'grid_tiles': 100, 'mistake_cards': 100,
           'stick_strips': 100, 'calendar_cards': 100}
# kits that a later lesson uses again (the kit note says "We use them again" only for these): clock (Term 3 Lessons 2, 3), play money (Lessons 5, 6), price tags (Lesson 6)
KIT_REUSED = {'clock_kit', 'play_money', 'price_tags'}


def kit_pct(spec):
    """Share of the text width a kit prints at. A kit whose pieces are too wide for 182 mm (two 95 mm shapes in a row) prints a little wider."""
    if spec.get('width'): return spec['width']
    if spec.get('type') == 'fold_shapes':
        d = spec.get('d_mm', FOLD_D_MM)
        return 100 if 2 * d + KIT_GAP <= PAGE_MM else min(110, round((2 * d + KIT_GAP) / PAGE_MM * 100 + 0.5))
    return KIT_PCT.get(spec.get('type'), 84)


def kit_style(spec):
    """CSS for the box that holds the kit drawing: a wider kit is centred on the page."""
    p = kit_pct(spec)
    return f'width:{p}%;margin-left:{-(p - 100) / 200 * PAGE_MM:.1f}mm' if p > 100 else f'width:{p}%'


def kit_reused(spec):
    """True when a later lesson uses these pieces again. spec['reused'] (true or false) overrides the built-in list."""
    if 'reused' in spec: return bool(spec['reused'])
    return spec.get('type') in KIT_REUSED


def kit_unit(spec):
    return 700.0 / (PAGE_MM * kit_pct(spec) / 100.0)


def kit_page_count(spec):
    r = render_kit(spec)
    return (r.count(KIT_SEP) + 1) if r else 1


def _kit(w, h, body, label=''):
    return f'<svg viewBox="0 0 {w:.0f} {h:.0f}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{_esc(label)}" style="width:100%;height:auto;display:block">{"".join(body)}</svg>'


def _cutbox(x, y, w, h, rx=8, fill='#fff'):
    return f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" fill="{fill}" stroke="{CUT}" stroke-width="2" stroke-dasharray="7 5"/>'


def _cutcircle(cx, cy, r, fill='#fff'):
    return f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" fill="{fill}" stroke="{CUT}" stroke-width="2" stroke-dasharray="7 5"/>'


def _head(txt, y=22):
    return f'<text x="4" y="{y}" font-size="20" font-weight="800" fill="{NAVY}" font-family="Nunito Sans, Arial">{_esc(txt)}</text>'


def _inner(svgtxt):
    return svgtxt[svgtxt.index('>') + 1:svgtxt.rindex('</svg>')]


def _words(txt, maxch):
    """Split a short label into lines of at most maxch characters."""
    out, cur = [], ''
    for w in str(txt).split():
        if cur and len(cur) + 1 + len(w) > maxch: out.append(cur); cur = w
        else: cur = (cur + ' ' + w).strip()
    return out + ([cur] if cur else [])


def clock_kit(faces=2, hour_hands=3, minute_hands=3, labels='all', u=None):
    """Cut-out clock faces (80 mm across, two in a row) and loose hands: hour hands short and wide (24 mm), minute hands long and thin (36 mm, shorter than the
    face radius so a laid hand never overhangs). Each hand has a dot at the end that goes in the middle. No fastener (D4): lay the hands on the face."""
    u = u or 700 / PAGE_MM
    gap = KIT_GAP * u
    b = [_head(f'Cut out {faces} clock faces and {hour_hands + minute_hands} hands: {faces + hour_hands + minute_hands} pieces in all.')]
    r = 40 * u; rc = r + 1.6 * u                       # face radius and its cut line
    per = 2
    y = 34 + rc
    for k in range(faces):
        c = k % per; row = k // per
        nrow = min(per, faces - row * per)
        wtot = nrow * 2 * rc + (nrow - 1) * gap
        cx = (700 - wtot) / 2 + rc + c * (2 * rc + gap); cy = y + row * (2 * rc + gap)
        inner = clock(12, 0, True, labels, ticks=True)
        sc = 2 * r / 196.0
        b.append(f'<g transform="translate({cx - 110 * sc:.1f},{cy - 110 * sc:.1f}) scale({sc:.4f})">{_inner(inner)}</g>')
        b.append(_cutcircle(cx, cy, rc, 'none'))
    rows_f = (faces + per - 1) // per
    y = 34 + rows_f * (2 * rc + gap) + 4
    b.append(_head(f'Hour hands (short, wide): cut out {hour_hands}', y)); y += 8
    hw, hh = 28 * u, 8 * u
    for k in range(hour_hands):
        x = 4 + k * (hw + gap)
        b.append(_cutbox(x, y, hw, hh, 12))
        b.append(f'<line x1="{x + 4 * u:.1f}" y1="{y + hh / 2:.1f}" x2="{x + 4 * u + 24 * u:.1f}" y2="{y + hh / 2:.1f}" stroke="{NAVY}" stroke-width="{2.4 * u:.1f}" stroke-linecap="round"/>')
        b.append(f'<circle cx="{x + 4 * u:.1f}" cy="{y + hh / 2:.1f}" r="{1.0 * u:.1f}" fill="#fff"/>')
    y += hh + gap + 8
    b.append(_head(f'Minute hands (long, thin): cut out {minute_hands}', y)); y += 8
    mw, mh = 40 * u, 7 * u
    for k in range(minute_hands):
        x = 4 + k * (mw + gap)
        b.append(_cutbox(x, y, mw, mh, 10))
        b.append(f'<line x1="{x + 2 * u:.1f}" y1="{y + mh / 2:.1f}" x2="{x + 2 * u + 36 * u:.1f}" y2="{y + mh / 2:.1f}" stroke="{NAVY}" stroke-width="{1.2 * u:.1f}" stroke-linecap="round"/>')
        b.append(f'<circle cx="{x + 2 * u:.1f}" cy="{y + mh / 2:.1f}" r="{1.0 * u:.1f}" fill="#fff" stroke="{NAVY}" stroke-width="1.2"/>')
    y += mh + gap + 6
    for i, t in enumerate(('Lay an hour hand and a minute hand on a face, with the dotted ends', 'together at the middle. No pins: keep the hands flat.')):
        b.append(f'<text x="4" y="{y + 18 * i:.1f}" font-size="17" fill="#3B4A6B" font-family="Nunito Sans, Arial">{t}</text>')
    return _kit(700, y + 40, b, 'clock faces and hands')


COIN_MM = {'5c': 20, '10c': 22, '20c': 24, '50c': 26, '$1': 28}
NOTE_MM = {'$2': (50, 25), '$5': (51, 25.5), '$10': (52, 26), '$50': (53, 26.5)}     # up to three notes in a row


def play_money(page=1, counts=None, u=None):
    """Two pages of stylised PLAY MONEY. page 1 = coins (5c x4, 10c x6, 20c x4, 50c x2), page 2 = notes ($2 x5, $5 x4, $10 x3, $50 x1). `counts` overrides {value: n}.
    Coins are 20 to 26 mm, notes about 50 by 25 mm (three in a row), 6 mm between cut lines."""
    u = u or 700 / PAGE_MM
    default = {1: {'5c': 4, '10c': 6, '20c': 4, '50c': 2}, 2: {'$2': 5, '$5': 4, '$10': 3, '$50': 1}}[page]
    cnt = {_canon(k): n for k, n in (counts or default).items()}
    b = [_head('Play money: a grown-up cuts out every piece. It is not real money.')]
    gap = KIT_GAP * u; pad = 1.5 * u
    x = 4 * u; y = 36; rowh = 0
    for v, n in cnt.items():
        for _ in range(n):
            w, h = ((NOTE_MM[v][0] * u, NOTE_MM[v][1] * u) if v in NOTE_MM else (COIN_MM[v] * u, COIN_MM[v] * u))
            cw, ch = w + 2 * pad, h + 2 * pad
            if x + cw > 700 - 4 * u + 0.1: x = 4 * u; y += rowh + gap; rowh = 0
            cx, cy = x + cw / 2, y + ch / 2
            b.append(_cutbox(x, y, cw, ch, 10 if v not in NOTE_MM else 6, '#fff'))
            b.append(_note(v, cx, cy, (w, h)) if v in NOTE_MM else _coin(v, cx, cy, w))
            x += cw + gap; rowh = max(rowh, ch)
    return _kit(700, y + rowh + 20, b, 'play money')


def price_tags(prices=None, items=None, blank=3, u=None):
    """12 tags (each 54 by 44 mm, 6 mm between cut lines, the grid centred on the page): 9 priced, `blank` blank ones to write on."""
    u = u or 700 / PAGE_MM
    prices = prices or ['$2', '$3', '$4', '$5', '$6', '$7', '$8', '$9', '$10']
    items = items or ['pencil', 'rubber', 'ruler', 'glue', 'bag', 'book', 'cup', 'ball', 'pen']
    b = [_head('Price tags: a grown-up cuts out all 12. Write a price on the blank ones.')]
    cw, ch, gap = 54 * u, 44 * u, KIT_GAP * u
    x0 = (700 - (3 * cw + 2 * gap)) / 2
    for i in range(len(prices) + blank):
        c, r = i % 3, i // 3
        x, y = x0 + c * (cw + gap), 34 + r * (ch + gap)
        b.append(_cutbox(x, y, cw, ch, 14))
        if i < len(prices):
            inner = price_tag(items[i % len(items)], prices[i], False, 130)
            b.append(f'<g transform="translate({x + (cw - 140) / 2:.1f},{y + (ch - 160) / 2:.1f})">{_inner(inner)}</g>')
        else:
            b.append(f'<line x1="{x + 30}" y1="{y + ch * 0.7:.1f}" x2="{x + cw - 30}" y2="{y + ch * 0.7:.1f}" stroke="{NAVY}" stroke-width="2.4"/><text x="{x + cw / 2:.1f}" y="{y + ch * 0.45:.1f}" font-size="20" text-anchor="middle" fill="#5B6785" font-family="Nunito Sans, Arial">write here</text>')
    rows = (len(prices) + blank + 2) // 3
    return _kit(700, 34 + rows * (ch + gap) - gap + 2, b, 'price tags')


def grid_tiles(symbols=('circle', 'square', 'triangle', 'star'), per=4, digits=True, u=None):
    """16 tiles (22 mm, 6 mm between cut lines; 4 symbols x 4, each with a digit 1-4) and two mats (3 x 3 and 4 x 4, 24 mm squares, side by side: not cut)."""
    u = u or 700 / PAGE_MM
    b = [_head('Tiles: cut out all 16 (a grown-up cuts). The mats are not cut.')]
    t = 22 * u; gap = KIT_GAP * u
    n_row = 6
    x0 = (700 - (n_row * t + (n_row - 1) * gap)) / 2
    k = 0
    for si, sym in enumerate(symbols):
        for d in range(per):
            x = x0 + (k % n_row) * (t + gap); y = 34 + (k // n_row) * (t + gap); k += 1
            b.append(_cutbox(x, y, t, t, 8))
            b.append(_sym_shape(sym, x + t * 0.4, y + t * 0.42, t * 0.26))
            if digits: b.append(f'<text x="{x + t * 0.78:.1f}" y="{y + t * 0.88:.1f}" font-size="{t * 0.3:.1f}" font-weight="800" text-anchor="middle" fill="{NAVY}" font-family="{FONT}">{d + 1}</text>')
    rows = (k + n_row - 1) // n_row
    y0 = 34 + rows * (t + gap) + 20
    cs = 24 * u
    xm = (700 - (7 * cs + gap)) / 2
    b.append(_head('Mat 1 (3 by 3)', y0).replace('x="4"', f'x="{xm:.0f}"'))
    for r in range(3):
        for c in range(3): b.append(f'<rect x="{xm + c * cs:.1f}" y="{y0 + 10 + r * cs:.1f}" width="{cs:.1f}" height="{cs:.1f}" fill="#fff" stroke="{NAVY}" stroke-width="2.6"/>')
    x2 = xm + 3 * cs + gap
    b.append(f'<text x="{x2:.0f}" y="{y0}" font-size="20" font-weight="800" fill="{NAVY}" font-family="Nunito Sans, Arial">Mat 2 (4 by 4)</text>')
    for r in range(4):
        for c in range(4): b.append(f'<rect x="{x2 + c * cs:.1f}" y="{y0 + 10 + r * cs:.1f}" width="{cs:.1f}" height="{cs:.1f}" fill="#fff" stroke="{NAVY}" stroke-width="2.6"/>')
    return _kit(700, y0 + 20 + 4 * cs + 10, b, 'grid tiles and mats')


def _sym_shape(sym, x, y, r):
    return {'circle': f'<circle cx="{x}" cy="{y}" r="{r}" {_o("#F6C9D0")}/>',
            'square': f'<rect x="{x - r}" y="{y - r}" width="{2 * r}" height="{2 * r}" {_o("#BFE3DC")}/>',
            'triangle': f'<polygon points="{x},{y - r} {x + r * 1.1},{y + r * 0.85} {x - r * 1.1},{y + r * 0.85}" {_o("#FFE59A")}/>',
            'star': _tile_shape('star', x, y, r, '#C9B6F0', 0, 0, 'k'),
            'heart': f'<path d="M{x} {y + r} C{x - r * 1.6} {y - r * .2} {x - r * .7} {y - r * 1.1} {x} {y - r * .3} C{x + r * .7} {y - r * 1.1} {x + r * 1.6} {y - r * .2} {x} {y + r}" {_o("#FF8FB1")}/>'}[sym]


def mistake_cards(cards=None, u=None):
    """8 cards (85 by 16 mm, 6 mm between cut lines; text from `cards`, 4 right and 4 wrong sums) and a two-pocket mat (RIGHT / WRONG; the mat is not cut)."""
    u = u or 700 / PAGE_MM
    cards = cards or ['23 + 14 = 37', '45 + 12 = 56', '60 - 20 = 40', '38 + 5 = 44', '17 + 3 = 20', '52 - 9 = 42', '30 + 40 = 70', '81 - 6 = 74']
    b = [_head('Cards: a grown-up cuts out all 8. The mat is not cut.')]
    cw, ch, gap = 85 * u, 16 * u, KIT_GAP * u
    x0 = (700 - (2 * cw + gap)) / 2
    for i, t in enumerate(cards[:8]):
        x = x0 + (i % 2) * (cw + gap); y = 34 + (i // 2) * (ch + gap)
        b.append(_cutbox(x, y, cw, ch, 10)); b.append(f'<text x="{x + cw / 2:.1f}" y="{y + ch / 2 + 10:.1f}" font-size="30" font-weight="800" text-anchor="middle" fill="{NAVY}" font-family="{FONT}">{_esc(t)}</text>')
    y = 34 + 4 * (ch + gap) + 14
    for k, lab in enumerate(('RIGHT', 'WRONG')):
        x = x0 + k * (cw + gap)
        b.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{cw:.1f}" height="{55 * u:.1f}" rx="14" fill="#fff" stroke="{NAVY}" stroke-width="3.4"/><text x="{x + cw / 2:.1f}" y="{y + 55 * u / 2 + 14:.1f}" font-size="44" font-weight="800" text-anchor="middle" fill="{NAVY}" font-family="{FONT}">{lab}</text>')
    return _kit(700, y + 55 * u + 10, b, 'mistake cards')


def fold_shapes(circles=4, squares=4, rects=2, d_mm=FOLD_D_MM, u=None):
    """Circles and squares (d_mm across, any size is honoured) and long rectangles (d_mm by d_mm / 2, drawn as a 4 by 2 grid of faint lines) for folding.
    A grown-up cuts them out; children only fold. Two shapes per row; the kit runs over as many pages as it needs."""
    d_mm = d_mm or FOLD_D_MM
    if u is None: u = kit_unit({'type': 'fold_shapes', 'd_mm': d_mm})
    width_mm = 700 / u
    d = d_mm * u; gap = KIT_GAP * u
    cols = max(1, int((width_mm + KIT_GAP) // (d_mm + KIT_GAP)))
    rows = []                                           # (kind, count in this row)
    for kind, n in (('c', circles), ('s', squares), ('r', rects)):
        while n > 0: rows.append((kind, min(cols, n))); n -= cols
    pages, cur, ymm = [], [], 0.0
    for kind, k in rows:
        hmm = d_mm / 2 if kind == 'r' else d_mm
        if cur and ymm + hmm > KIT_AVAIL_MM: pages.append(cur); cur, ymm = [], 0.0
        cur.append((kind, k, ymm, hmm)); ymm += hmm + KIT_GAP
    if cur: pages.append(cur)
    out = []
    for pi, pg in enumerate(pages):
        b = [_head('Shapes to fold: a grown-up cuts them out.' + (f' (page {pi + 1} of {len(pages)})' if len(pages) > 1 else ''))]
        for kind, k, ymm_, hmm in pg:
            x0 = (700 - (k * d + (k - 1) * gap)) / 2
            for c in range(k):
                x = x0 + c * (d + gap); y = 36 + ymm_ * u
                if kind == 'c': b.append(_cutcircle(x + d / 2, y + d / 2, d / 2))
                elif kind == 's': b.append(_cutbox(x, y, d, d, 4))
                else:
                    h = hmm * u
                    b.append(_cutbox(x, y, d, h, 4))
                    for g in range(1, 4): b.append(f'<line x1="{x + g * d / 4:.1f}" y1="{y:.1f}" x2="{x + g * d / 4:.1f}" y2="{y + h:.1f}" stroke="#8A94AD" stroke-width="1.8"/>')
                    b.append(f'<line x1="{x:.1f}" y1="{y + h / 2:.1f}" x2="{x + d:.1f}" y2="{y + h / 2:.1f}" stroke="#8A94AD" stroke-width="1.8"/>')
        last = pg[-1]
        out.append(_kit(700, 36 + (last[2] + last[3]) * u + 10, b, 'shapes to fold'))
    return KIT_SEP.join(out)


def shape_pieces(counts=None, unit_mm=30, page=None, u=None):
    """Pieces on a 3 cm unit: squares, rectangles (1 x 2), triangles (half a square), half circles, quarter circles, one circle. A grown-up cuts them out."""
    counts = counts or {'square': 6, 'rectangle': 3, 'triangle': 6, 'half_circle': 2, 'quarter_circle': 2, 'circle': 1}
    if page == 1: counts = {k: v for k, v in counts.items() if k in ('square', 'rectangle')}
    elif page == 2: counts = {k: v for k, v in counts.items() if k not in ('square', 'rectangle')}
    u = u or MM
    uu = unit_mm * u; gap = KIT_GAP * u
    b = [_head('Pieces: a grown-up cuts out all of them. Each square is 3 cm.')]
    x = 14; y = 40; rowh = 0
    for kind, n in counts.items():
        for _ in range(n):
            w, h = {'square': (uu, uu), 'rectangle': (2 * uu, uu), 'triangle': (uu, uu), 'half_circle': (uu * 1.4, uu * 0.8), 'quarter_circle': (uu * 0.9, uu * 0.9), 'circle': (uu * 1.2, uu * 1.2)}[kind]
            if x + w + 10 > 690: x = 14; y += rowh + gap; rowh = 0
            if kind in ('square', 'rectangle'): b.append(_cutbox(x, y, w, h, 3, SOFT))
            elif kind == 'triangle': b.append(f'<polygon points="{x},{y + h} {x + w},{y + h} {x},{y}" fill="{SKY}" stroke="{CUT}" stroke-width="2" stroke-dasharray="7 5"/>')
            elif kind == 'half_circle': b.append(f'<path d="M{x} {y + h} A{w / 2} {h} 0 0 1 {x + w} {y + h} Z" fill="{MINT}" stroke="{CUT}" stroke-width="2" stroke-dasharray="7 5"/>')
            elif kind == 'quarter_circle': b.append(f'<path d="M{x} {y + h} V{y} A{w} {h} 0 0 1 {x + w} {y + h} Z" fill="#F6C9D0" stroke="{CUT}" stroke-width="2" stroke-dasharray="7 5"/>')
            else: b.append(_cutcircle(x + w / 2, y + h / 2, w / 2, '#FFE59A'))
            x += w + gap; rowh = max(rowh, h)
    return _kit(700, y + rowh + 20, b, 'shape pieces')


_SUN_N = 0


def _sun_card(spec, x, y, cw, ch):
    """A pair-card face that really shows what a set differs in: 'sun:N:size:pattern' = N suns (1-5), size big|mid|small|few, pattern plain|striped|dotted."""
    global _SUN_N
    _, n, size, pat = spec.split(':'); n = int(n)
    _SUN_N += 1; pid = f'sunpat{_SUN_N}'
    R = {'big': 0.30, 'mid': 0.17, 'small': 0.10, 'few': 0.095}[size] * cw
    if n == 1: pos = [(0.5, 0.5)]
    elif n == 2: pos = [(0.3, 0.5), (0.7, 0.5)]
    elif n == 5: pos = [(0.17, 0.25), (0.5, 0.25), (0.83, 0.25), (0.33, 0.75), (0.67, 0.75)]
    else: raise ValueError('sun card: N must be 1, 2 or 5')
    fill = {'plain': YEL, 'striped': f'url(#{pid}s)', 'dotted': f'url(#{pid}d)'}[pat]
    out = [f'<defs><pattern id="{pid}s" width="10" height="10" patternUnits="userSpaceOnUse" patternTransform="translate({x:.1f} {y:.1f}) rotate(45)"><rect width="10" height="10" fill="#fff"/><rect width="4" height="10" fill="{NAVY}"/></pattern>'
           f'<pattern id="{pid}d" width="13" height="13" patternUnits="userSpaceOnUse" patternTransform="translate({x:.1f} {y:.1f})"><rect width="13" height="13" fill="#fff"/><circle cx="6.5" cy="6.5" r="3.3" fill="{NAVY}"/></pattern></defs>']
    for (px, py) in pos:
        cx, cy = x + px * cw, y + py * ch
        for k in range(8):
            a = k * math.pi / 4
            out.append(f'<line x1="{cx + R * 1.25 * math.cos(a):.1f}" y1="{cy + R * 1.25 * math.sin(a):.1f}" x2="{cx + R * 1.6 * math.cos(a):.1f}" y2="{cy + R * 1.6 * math.sin(a):.1f}" stroke="{NAVY}" stroke-width="{3.4 if size != "small" else 2.6}" stroke-linecap="round"/>')
        out.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{R:.1f}" fill="{fill}" stroke="{NAVY}" stroke-width="3"/>')
    return ''.join(out)


def _card_face(t, x, y, cw, ch):
    """The face of a card: an icon ('icon:apple'), text ('3'), or both: 'icon:apple+3' / ['icon:apple', '3'] / {'icon': 'apple', 'text': '3'} puts the picture above the words."""
    icon_name = text = None
    if isinstance(t, str) and t.startswith('sun:'): return _sun_card(t, x, y, cw, ch)
    if isinstance(t, dict): icon_name, text = t.get('icon'), t.get('text')
    elif isinstance(t, (list, tuple)):
        for p in t:
            if str(p).startswith('icon:'): icon_name = str(p)[5:]
            else: text = str(p)
    else:
        t = str(t)
        if '+' in t and t.startswith('icon:'): a, _, c = t.partition('+'); icon_name, text = a[5:], c
        elif t.startswith('icon:'): icon_name = t[5:]
        else: text = t
    cx = x + cw / 2
    if icon_name and text:
        return icon(icon_name, cx, y + ch * 0.4, ch * 0.5) + f'<text x="{cx:.1f}" y="{y + ch * 0.9:.1f}" font-size="{ch * 0.22:.1f}" font-weight="800" text-anchor="middle" fill="{NAVY}" font-family="{FONT}">{_esc(text)}</text>'
    if icon_name: return icon(icon_name, cx, y + ch / 2, ch * 0.64)
    return f'<text x="{cx:.1f}" y="{y + ch * 0.64:.1f}" font-size="{ch * 0.35:.1f}" font-weight="800" text-anchor="middle" fill="{NAVY}" font-family="{FONT}">{_esc(text or "")}</text>'


def pair_cards(labels=None, sets=3, per=4, u=None):
    """12 cards in 3 sets of 4 (a grown-up cuts them out). labels: list of card faces: text, 'icon:house', or a mixed card ('icon:apple+3', ['icon:apple', '3'], {'icon':..,'text':..}).
    6 mm between cut lines."""
    u = u or MM
    n = sets * per
    labels = labels or [str(i + 1) for i in range(n)]
    gap = KIT_GAP * u
    cw = (700 - 8 - (per - 1) * gap) / per; ch = cw * 0.88
    b = [_head(f'Cards: a grown-up cuts out all {n}.')]
    for i in range(n):
        x = 4 + (i % per) * (cw + gap); y = 36 + (i // per) * (ch + gap)
        b.append(_cutbox(x, y, cw, ch, 10))
        b.append(_card_face(labels[i % len(labels)], x, y, cw, ch))
    return _kit(700, 36 + ((n + per - 1) // per) * (ch + gap) + 10, b, 'pair cards')


def grid_mat(routes=3, copies=2, rows=3, cols=3, u=None):
    """Printed grids to draw on (not cut): `routes` numbered dot grids and `copies` numbered square-dot grids with a dashed mirror line, each in its own frame."""
    b = [_head('Grids: keep this page flat to draw on. No cutting.')]
    sp = 54; pad = 22; fw = cols * sp + 2 * pad; fh = rows * sp + 2 * pad + 22; gp = (700 - 8 - routes * fw) / max(routes - 1, 1) if routes > 1 else 0
    for i in range(routes):
        x0 = 4 + i * (fw + gp); y0 = 38
        b.append(f'<rect x="{x0:.1f}" y="{y0}" width="{fw}" height="{fh}" rx="12" fill="#fff" stroke="{NAVY}" stroke-width="2.6"/><text x="{x0 + 12:.1f}" y="{y0 + 22}" font-size="18" font-weight="800" fill="{NAVY}" font-family="Nunito Sans, Arial">Grid {i + 1}</text>')
        for r in range(rows + 1):
            for c in range(cols + 1): b.append(f'<circle cx="{x0 + pad + c * sp:.1f}" cy="{y0 + pad + 22 + r * sp}" r="5" fill="{NAVY}"/>')
    y1 = 38 + fh + 40
    sp2 = 44; cfw = 6 * sp2 + 2 * 26
    for i in range(copies):
        x0 = 4 + i * (cfw + 16); cfh = 3 * sp2 + 2 * 22 + 22
        b.append(f'<rect x="{x0}" y="{y1}" width="{cfw}" height="{cfh}" rx="12" fill="#fff" stroke="{NAVY}" stroke-width="2.6"/><text x="{x0 + 12}" y="{y1 + 22}" font-size="18" font-weight="800" fill="{NAVY}" font-family="Nunito Sans, Arial">Copy grid {i + 1}: draw the other half</text>')
        for r in range(4):
            for c in range(7): b.append(f'<circle cx="{x0 + 26 + c * sp2}" cy="{y1 + 22 + 24 + r * sp2}" r="4.6" fill="{NAVY}"/>')
        b.append(f'<line x1="{x0 + 26 + 3 * sp2}" y1="{y1 + 30}" x2="{x0 + 26 + 3 * sp2}" y2="{y1 + cfh - 10}" stroke="{TEAL}" stroke-width="4" stroke-dasharray="10 7"/>')
    return _kit(700, y1 + 3 * sp2 + 2 * 22 + 22 + 14, b, 'grid mat')


def graph_mat(cols_=5, rows_=8, cell=62, u=None):
    """An empty picture-graph mat: `cols_` columns by `rows_` rows and a key box (not cut). Nothing else is printed under the squares."""
    b = [_head('Graph mat: keep this page flat. Draw one picture in a square.')]
    x0 = 70; y0 = 50
    for r in range(rows_):
        for c in range(cols_): b.append(f'<rect x="{x0 + c * cell}" y="{y0 + r * cell}" width="{cell}" height="{cell}" fill="#fff" stroke="{NAVY}" stroke-width="2.4"/>')
    b.append(f'<rect x="{x0 + cols_ * cell + 20}" y="{y0}" width="120" height="110" rx="10" fill="#fff" stroke="{NAVY}" stroke-width="3"/><text x="{x0 + cols_ * cell + 80}" y="{y0 + 40}" font-size="24" font-weight="800" text-anchor="middle" fill="{NAVY}" font-family="{FONT}">KEY</text><text x="{x0 + cols_ * cell + 80}" y="{y0 + 84}" font-size="20" text-anchor="middle" fill="#5B6785" font-family="Nunito Sans, Arial">1 picture =</text>')
    return _kit(700, y0 + rows_ * cell + 20, b, 'graph mat')


def tool_cards(tools=None, problems=None, u=None):
    """7 tool cards (picture and word) and 8 problem cards (a grown-up cuts them out), 6 mm between cut lines."""
    u = u or MM
    gap = KIT_GAP * u
    tools = tools or [('t_strip', 'Strip'), ('t_table', 'Table'), ('t_list', 'List'), ('t_draw', 'Draw'), ('t_back', 'Work backwards'), ('t_find', 'Find one'), ('t_steps', 'Steps')]
    problems = problems or ['Problem %d' % (i + 1) for i in range(8)]
    b = [_head('Tool cards and problem cards: a grown-up cuts out all 15.')]
    cw, chh = (700 - 8 - 3 * gap) / 4, 150
    for i, (ic, nm) in enumerate(tools):
        x = 4 + (i % 4) * (cw + gap); y = 36 + (i // 4) * (chh + gap)
        b.append(_cutbox(x, y, cw, chh, 12)); b.append(icon(ic, x + cw / 2, y + 56, 70))
        fs = 26 if len(nm) < 9 else (20 if len(nm) <= 11 else 17)
        b.append(f'<text x="{x + cw / 2:.1f}" y="{y + 126}" font-size="{fs}" font-weight="800" text-anchor="middle" fill="{NAVY}" font-family="{FONT}">{_esc(nm)}</text>')
    y0 = 36 + 2 * (chh + gap) + 6
    pw = (700 - 8 - gap) / 2
    for i, t in enumerate(problems):
        x = 4 + (i % 2) * (pw + gap); y = y0 + (i // 2) * (80 + gap)
        b.append(_cutbox(x, y, pw, 80, 10)); b.append(f'<text x="{x + pw / 2:.1f}" y="{y + 46}" font-size="18" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="Nunito Sans, Arial">{_esc(t)[:52]}</text>')
    return _kit(700, y0 + 4 * (80 + gap) + 4, b, 'tool and problem cards')


def event_cards(events=None, u=None):
    """8 event cards (38 by 36 mm, a picture and a few words, 6 mm between cut lines) and an am / pm mat (two boxes 85 by 100 mm: big enough to hold four cards each; not cut)."""
    u = u or 700 / PAGE_MM
    events = events or [('sun', 'wake up'), ('bus', 'go to school'), ('school', 'maths class'), ('shop', 'buy bread'), ('bath', 'have a bath'), ('bed', 'go to bed'), ('moon', 'look at the moon'), ('house', 'come home')]
    b = [_head('Event cards: a grown-up cuts out all 8. The mat is not cut.')]
    cw, ch, gap = 38 * u, 36 * u, KIT_GAP * u
    x0 = (700 - (4 * cw + 3 * gap)) / 2
    for i, (ic, t) in enumerate(events[:8]):
        x = x0 + (i % 4) * (cw + gap); y = 34 + (i // 4) * (ch + gap)
        b.append(_cutbox(x, y, cw, ch, 10)); b.append(icon(ic, x + cw / 2, y + ch * 0.32, ch * 0.42))
        lines = _words(t, 11)
        if len(lines) > 2: lines = [' '.join(lines[:-1]), lines[-1]]
        for j, ln in enumerate(lines[:2]):
            b.append(f'<text x="{x + cw / 2:.1f}" y="{y + ch * (0.68 + 0.19 * j):.1f}" font-size="{ch * 0.15:.1f}" font-weight="800" text-anchor="middle" fill="{NAVY}" font-family="Nunito Sans, Arial">{_esc(ln)}</text>')
    y = 34 + 2 * (ch + gap) + 8
    bw, bh = 85 * u, 100 * u
    xm = (700 - (2 * bw + gap)) / 2
    for k, (lab, ic) in enumerate((('am (night and morning)', 'sun'), ('pm (afternoon and evening)', 'moon'))):
        x = xm + k * (bw + gap)
        b.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{bw:.1f}" height="{bh:.1f}" rx="14" fill="#fff" stroke="{NAVY}" stroke-width="3.4"/>' + icon(ic, x + 34, y + 36, 44)
                 + f'<text x="{x + bw / 2 + 24:.1f}" y="{y + 48:.1f}" font-size="17" font-weight="800" text-anchor="middle" fill="{NAVY}" font-family="Nunito Sans, Arial">{lab}</text>')
    return _kit(700, y + bh + 10, b, 'event cards and mat')


def stick_strips(n=14, length_mm=60, u=None):
    """Short strips to use as sticks (a grown-up cuts them out): 8 mm wide, 6 mm between cut lines. Never matchsticks."""
    u = u or 700 / PAGE_MM
    b = [_head(f'Sticks: a grown-up cuts out all {n}.')]
    L, h, gap = length_mm * u, 8 * u, KIT_GAP * u
    x0 = (700 - (2 * L + gap)) / 2
    for i in range(n):
        x = x0 + (i % 2) * (L + gap); y = 36 + (i // 2) * (h + gap)
        b.append(_cutbox(x, y, L, h, 14, SOFT)); b.append(f'<line x1="{x + 14:.1f}" y1="{y + h / 2:.1f}" x2="{x + L - 14:.1f}" y2="{y + h / 2:.1f}" stroke="{NAVY}" stroke-width="5" stroke-linecap="round"/>')
    return _kit(700, 36 + ((n + 1) // 2) * (h + gap) + 4, b, 'sticks')


def calendar_cards(start='Wed', days=31, u=None):
    """A month page (not cut) and 7 day-name cards (a grown-up cuts them out, 6 mm between cut lines)."""
    u = u or 700 / PAGE_MM
    cell = 82
    cal = calendar(start, days, cell=cell)
    b = [_head('Month page: keep it flat. Day cards: a grown-up cuts out all 7.')]
    rows = (DAYS.index(start[:3].title()) + days + 6) // 7
    b.append(f'<g transform="translate({(700 - (14 + 7 * cell)) / 2:.1f},36)">{_inner(cal)}</g>')
    gap = KIT_GAP * u
    y = 36 + 14 + (rows + 1) * cell + 26
    cw = (700 - 8 - 3 * gap) / 4
    for i, d in enumerate(DAYS):
        x = 4 + (i % 4) * (cw + gap); yy = y + (i // 4) * (62 + gap)
        b.append(_cutbox(x, yy, cw, 62, 10)); b.append(f'<text x="{x + cw / 2:.1f}" y="{yy + 42}" font-size="30" font-weight="800" text-anchor="middle" fill="{NAVY}" font-family="{FONT}">{d}</text>')
    return _kit(700, y + 2 * (62 + gap), b, 'calendar and day cards')


def render_kit(spec):
    t = spec['type']
    if t not in KITS3: return None
    u = kit_unit(spec)
    if t == 'clock_kit': return clock_kit(spec.get('faces', 2), spec.get('hour_hands', 3), spec.get('minute_hands', 3), spec.get('labels', 'all'), u)
    if t == 'play_money': return play_money(spec.get('page', 1), spec.get('counts'), u)
    if t == 'price_tags': return price_tags(spec.get('prices'), spec.get('items'), spec.get('blank', 3), u)
    if t == 'grid_tiles': return grid_tiles(u=u)
    if t == 'mistake_cards': return mistake_cards(spec.get('cards'), u)
    if t == 'fold_shapes': return fold_shapes(spec.get('circles', 4), spec.get('squares', 4), spec.get('rects', 2), spec.get('d_mm', FOLD_D_MM), u)
    if t == 'shape_pieces': return shape_pieces(spec.get('counts'), spec.get('unit_mm', 30), spec.get('page'), u)
    if t == 'pair_cards': return pair_cards(spec.get('labels'), spec.get('sets', 3), spec.get('per', 4), u)
    if t == 'grid_mat': return grid_mat(spec.get('routes', 3), spec.get('copies', 2), u=u)
    if t == 'graph_mat': return graph_mat(spec.get('cols', 5), spec.get('rows', 8), spec.get('cell', 62), u=u)
    if t == 'tool_cards': return tool_cards(spec.get('tools'), spec.get('problems'), u)
    if t == 'event_cards': return event_cards(spec.get('events'), u)
    if t == 'stick_strips': return stick_strips(spec.get('n', 14), spec.get('length_mm', 60), u)
    if t == 'calendar_cards': return calendar_cards(spec.get('start', 'Wed'), spec.get('days', 31), u)
    return None


KITS3 = {'clock_kit', 'play_money', 'price_tags', 'grid_tiles', 'mistake_cards', 'fold_shapes', 'shape_pieces', 'pair_cards', 'grid_mat', 'graph_mat', 'tool_cards', 'event_cards', 'stick_strips', 'calendar_cards'}
NONCUT3 = {'grid_mat', 'graph_mat'}       # all-uncut kit pages (the mixed ones say so on the page: month page, mats)
