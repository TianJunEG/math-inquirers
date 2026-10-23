"""Small figure helpers for the skill-gap slides (Levels 1 to 3). Inline SVG / HTML only, no images.
Used by rebuild/gen_skill_slides.py. Colours follow rebuild/slidekit.py."""
import math
from slidekit import NAVY, TEAL, YEL, WHITE, SKY, SOFT, GREY, E

RED = '#D1495B'; BLUE = '#2E86C1'; GREEN = '#3E8E41'; ORANGE = '#E67E22'
F = "Fredoka, Arial, sans-serif"


def svg(inner, w, h, label):
    return (f'<svg aria-label="{E(label)}" viewBox="0 0 {w} {h}" width="{w}" height="{h}" xmlns="http://www.w3.org/2000/svg" '
            f'style="width:{w}px;height:{h}px;flex:none">{inner}</svg>')


# ---------------------------------------------------------------- shapes used in picture equations
def shape(kind, size=56):
    """Inline svg of one symbol: tri, circ, sq, star."""
    s = size
    col = {'tri': BLUE, 'circ': RED, 'sq': GREEN, 'star': ORANGE}[kind]
    if kind == 'tri':
        g = f'<polygon points="{s/2},4 {s-4},{s-6} 4,{s-6}" fill="{col}" stroke="{NAVY}" stroke-width="4" stroke-linejoin="round"/>'
    elif kind == 'circ':
        g = f'<circle cx="{s/2}" cy="{s/2}" r="{s/2-5}" fill="{col}" stroke="{NAVY}" stroke-width="4"/>'
    elif kind == 'sq':
        g = f'<rect x="6" y="6" width="{s-12}" height="{s-12}" rx="5" fill="{col}" stroke="{NAVY}" stroke-width="4"/>'
    else:
        pts = []
        for i in range(10):
            r = s / 2 - 4 if i % 2 == 0 else s / 4.2
            a = -math.pi / 2 + i * math.pi / 5
            pts.append(f'{s/2 + r*math.cos(a):.1f},{s/2 + r*math.sin(a):.1f}')
        g = f'<polygon points="{" ".join(pts)}" fill="{col}" stroke="{NAVY}" stroke-width="4" stroke-linejoin="round"/>'
    return f'<svg viewBox="0 0 {s} {s}" width="{s}" height="{s}" style="width:{s}px;height:{s}px;vertical-align:middle" xmlns="http://www.w3.org/2000/svg" aria-label="{kind}">{g}</svg>'


def sym_line(tokens, size=56, fs=48):
    """tokens: list of 'tri'|'circ'|'sq'|'star' or text such as '+', '= 11'."""
    out = []
    for t in tokens:
        if t in ('tri', 'circ', 'sq', 'star'):
            out.append(shape(t, size))
        else:
            out.append(f'<span style="font-size:{fs}px;font-weight:800;font-family:{F}">{E(t)}</span>')
    return f'<div style="display:flex;align-items:center;gap:14px;flex-wrap:nowrap">{"".join(out)}</div>'


# ---------------------------------------------------------------- isometric cubes
def iso(heights, s=44, walls=False, label='Stack of cubes', pad=14):
    """heights[i][j] = cubes in the stack at column i (to the right) and row j (j larger = nearer the viewer).
    walls=True draws a floor and two walls behind (a room corner): wall A on the i=0 side, wall B on the j=0 side."""
    ni = len(heights); nj = len(heights[0]); H = max(max(r) for r in heights)
    c = s * 0.866; hh = s * 0.5
    wallh = H + (1 if walls else 0)
    # origin so that everything fits
    minx = -nj * c; maxx = ni * c
    miny = -wallh * s if walls else -H * s
    maxy = (ni + nj) * hh
    ox = pad - minx; oy = pad - miny
    P = lambda i, j, k: (ox + (i - j) * c, oy + (i + j) * hh - k * s)
    pts = lambda L: ' '.join(f'{x:.1f},{y:.1f}' for x, y in L)
    out = ''
    if walls:
        W = max(ni, nj)
        out += f'<polygon points="{pts([P(0,0,0),P(0,nj,0),P(ni,nj,0),P(ni,0,0)])}" fill="#F4E9C8" stroke="{NAVY}" stroke-width="3"/>'
        out += f'<polygon points="{pts([P(0,0,0),P(0,nj,0),P(0,nj,wallh),P(0,0,wallh)])}" fill="#CFE3F5" stroke="{NAVY}" stroke-width="3"/>'
        out += f'<polygon points="{pts([P(0,0,0),P(ni,0,0),P(ni,0,wallh),P(0,0,wallh)])}" fill="#E1ECF8" stroke="{NAVY}" stroke-width="3"/>'
        lx, ly = P(0, nj * 0.5, wallh * 0.85); rx, ry = P(ni * 0.5, 0, wallh * 0.85)
        out += f'<text x="{lx:.0f}" y="{ly:.0f}" font-size="22" font-weight="800" text-anchor="middle" fill="{TEAL}" font-family="Nunito Sans, Arial">left wall</text>'
        out += f'<text x="{rx:.0f}" y="{ry:.0f}" font-size="22" font-weight="800" text-anchor="middle" fill="{TEAL}" font-family="Nunito Sans, Arial">right wall</text>'
    cubes = [(i, j, k) for i in range(ni) for j in range(nj) for k in range(heights[i][j])]
    cubes.sort(key=lambda t: (t[0] + t[1], t[2], t[0]))
    for i, j, k in cubes:
        top = [P(i, j, k + 1), P(i + 1, j, k + 1), P(i + 1, j + 1, k + 1), P(i, j + 1, k + 1)]
        right = [P(i + 1, j, k), P(i + 1, j + 1, k), P(i + 1, j + 1, k + 1), P(i + 1, j, k + 1)]
        left = [P(i, j + 1, k), P(i + 1, j + 1, k), P(i + 1, j + 1, k + 1), P(i, j + 1, k + 1)]
        out += (f'<polygon points="{pts(left)}" fill="{YEL}" stroke="{NAVY}" stroke-width="2.5" stroke-linejoin="round"/>'
                f'<polygon points="{pts(right)}" fill="#E0A800" stroke="{NAVY}" stroke-width="2.5" stroke-linejoin="round"/>'
                f'<polygon points="{pts(top)}" fill="#FFE49A" stroke="{NAVY}" stroke-width="2.5" stroke-linejoin="round"/>')
    w = int(maxx - minx + 2 * pad); h = int(maxy - miny + 2 * pad)
    return svg(out, w, h, label)


# ---------------------------------------------------------------- top-view number grid
def height_grid(rows, cell=92, label='Top view: numbers show how many cubes are in each stack'):
    nr = len(rows); nc = len(rows[0]); w = nc * cell + 8; h = nr * cell + 8
    out = ''
    for r in range(nr):
        for c in range(nc):
            x = 4 + c * cell; y = 4 + r * cell
            out += f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" fill="{SKY}" stroke="{NAVY}" stroke-width="4"/>'
            out += f'<text x="{x+cell/2}" y="{y+cell/2+16}" font-size="48" font-weight="800" text-anchor="middle" fill="{NAVY}" font-family="{F}">{rows[r][c]}</text>'
    out += f'<text x="{w/2}" y="{h+30}" font-size="26" font-weight="800" text-anchor="middle" fill="{TEAL}" font-family="Nunito Sans, Arial">FRONT</text>'
    return svg(out, w, h + 40, label)


# ---------------------------------------------------------------- clock
def clock(hour, minute, size=300, label=None):
    r = size / 2 - 8; cx = cy = size / 2
    out = f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{WHITE}" stroke="{NAVY}" stroke-width="7"/>'
    for n in range(1, 13):
        a = math.radians(n * 30 - 90)
        out += f'<text x="{cx + (r-34)*math.cos(a):.1f}" y="{cy + (r-34)*math.sin(a) + 11:.1f}" font-size="32" font-weight="800" text-anchor="middle" fill="{NAVY}" font-family="{F}">{n}</text>'
    for m in range(60):
        a = math.radians(m * 6 - 90); l = 12 if m % 5 == 0 else 6
        out += f'<line x1="{cx + (r-4)*math.cos(a):.1f}" y1="{cy + (r-4)*math.sin(a):.1f}" x2="{cx + (r-4-l)*math.cos(a):.1f}" y2="{cy + (r-4-l)*math.sin(a):.1f}" stroke="{NAVY}" stroke-width="3"/>'
    ha = math.radians(((hour % 12) + minute / 60) * 30 - 90); ma = math.radians(minute * 6 - 90)
    out += f'<line x1="{cx}" y1="{cy}" x2="{cx + r*0.5*math.cos(ha):.1f}" y2="{cy + r*0.5*math.sin(ha):.1f}" stroke="{NAVY}" stroke-width="12" stroke-linecap="round"/>'
    out += f'<line x1="{cx}" y1="{cy}" x2="{cx + r*0.78*math.cos(ma):.1f}" y2="{cy + r*0.78*math.sin(ma):.1f}" stroke="{TEAL}" stroke-width="8" stroke-linecap="round"/>'
    out += f'<circle cx="{cx}" cy="{cy}" r="9" fill="{NAVY}"/>'
    return svg(out, size, size, label or f'Clock showing {hour}:{minute:02d}')


# ---------------------------------------------------------------- bars (twice as many)
def bars(rows, unit=64, label='Bars'):
    """rows: list of (name, n_blocks, colour)."""
    gap = 12; lab = 130; h = len(rows) * (unit + gap) + 4; w = lab + max(n for _, n, _ in rows) * (unit + 6) + 10
    out = ''
    for r, (name, n, col) in enumerate(rows):
        y = 4 + r * (unit + gap)
        out += f'<text x="{lab-14}" y="{y+unit/2+10}" font-size="32" font-weight="800" text-anchor="end" fill="{NAVY}" font-family="{F}">{E(name)}</text>'
        for b in range(n):
            out += f'<rect x="{lab + b*(unit+6)}" y="{y}" width="{unit}" height="{unit}" rx="8" fill="{col}" stroke="{NAVY}" stroke-width="4"/>'
    return svg(out, w, h, label)


# ---------------------------------------------------------------- days of the week strip
def week_strip(start_idx=0, days=14, label='Days of the week, repeating'):
    names = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    bw = 100; w = days * (bw + 6); out = ''
    for d in range(days):
        n = names[(start_idx + d) % 7]
        col = SKY if d < 7 else SOFT
        out += f'<rect x="{d*(bw+6)+2}" y="4" width="{bw}" height="70" rx="12" fill="{col}" stroke="{NAVY}" stroke-width="3"/>'
        out += f'<text x="{d*(bw+6)+2+bw/2}" y="50" font-size="32" font-weight="800" text-anchor="middle" fill="{NAVY}" font-family="{F}">{n}</text>'
    return svg(out, w, 80, label)


# ---------------------------------------------------------------- number cards
def cards(nums, w=84, h=116):
    out = ''
    for i, n in enumerate(nums):
        x = 4 + i * (w + 18)
        out += f'<rect x="{x}" y="4" width="{w}" height="{h}" rx="12" fill="{WHITE}" stroke="{NAVY}" stroke-width="5"/>'
        out += f'<text x="{x+w/2}" y="{h/2+24}" font-size="70" font-weight="800" text-anchor="middle" fill="{NAVY}" font-family="{F}">{n}</text>'
    return svg(out, 8 + len(nums) * (w + 18), h + 8, 'Digit cards ' + ' '.join(map(str, nums)))


# ---------------------------------------------------------------- html table for sequences with a gap row
def seq_table(terms, gaps, blanks_from, fs=46):
    """terms: list; entries from index blanks_from on are shown as empty boxes. gaps: list shown under the terms (None = empty box)."""
    box = f'<span style="display:inline-block;width:{int(fs*1.4)}px;height:{int(fs*1.2)}px;border:4px solid {NAVY};border-radius:8px;background:{YEL};vertical-align:middle"></span>'
    def cell(v, bold=True, bg=WHITE):
        return f'<td style="border:3px solid {NAVY};background:{bg};padding:6px 10px;min-width:{int(fs*1.8)}px;text-align:center;font-size:{fs}px;font-weight:{800 if bold else 600}">{v}</td>'
    r1 = f'<td style="padding:6px 12px;font-size:32px;font-weight:800;color:{TEAL}">Number</td>' + ''.join(cell(box if i >= blanks_from else t) for i, t in enumerate(terms))
    r2 = f'<td style="padding:6px 12px;font-size:32px;font-weight:800;color:{TEAL}">Gap</td><td></td>' + ''.join(cell(box if g is None else f'+{g}', False, SKY) for g in gaps)
    return f'<table style="border-collapse:separate;border-spacing:6px"><tr>{r1}</tr><tr>{r2}</tr></table>'


# ---------------------------------------------------------------- faces for picture patterns
def face(eyes, mouth, size=130):
    """eyes: 'open'|'closed'; mouth: 'smile'|'flat'|'open'."""
    s = size; cx = cy = s / 2
    out = f'<circle cx="{cx}" cy="{cy}" r="{s/2-5}" fill="{SOFT}" stroke="{NAVY}" stroke-width="5"/>'
    for dx in (-s * 0.18, s * 0.18):
        if eyes == 'open':
            out += f'<circle cx="{cx+dx}" cy="{cy-s*0.12}" r="{s*0.07}" fill="{NAVY}"/>'
        else:
            out += f'<path d="M{cx+dx-s*0.09} {cy-s*0.12} Q{cx+dx} {cy-s*0.04} {cx+dx+s*0.09} {cy-s*0.12}" fill="none" stroke="{NAVY}" stroke-width="5" stroke-linecap="round"/>'
    my = cy + s * 0.2
    if mouth == 'smile':
        out += f'<path d="M{cx-s*0.22} {my-s*0.05} Q{cx} {my+s*0.2} {cx+s*0.22} {my-s*0.05}" fill="none" stroke="{NAVY}" stroke-width="6" stroke-linecap="round"/>'
    elif mouth == 'flat':
        out += f'<line x1="{cx-s*0.2}" y1="{my+s*0.03}" x2="{cx+s*0.2}" y2="{my+s*0.03}" stroke="{NAVY}" stroke-width="6" stroke-linecap="round"/>'
    else:
        out += f'<ellipse cx="{cx}" cy="{my+s*0.03}" rx="{s*0.13}" ry="{s*0.1}" fill="{NAVY}"/>'
    return f'<svg viewBox="0 0 {s} {s}" width="{s}" height="{s}" style="width:{s}px;height:{s}px;flex:none" xmlns="http://www.w3.org/2000/svg" aria-label="Face with {eyes} eyes and {mouth} mouth">{out}</svg>'


def face_row(seq, size=130, start=1):
    """seq: list of (eyes, mouth); numbers shown under each face."""
    cells = ''.join(f'<div style="display:flex;flex-direction:column;align-items:center;gap:2px">{face(e, m, size)}<span style="font-size:30px;font-weight:800;color:{TEAL}">{start+i}</span></div>' for i, (e, m) in enumerate(seq))
    return f'<div style="display:flex;gap:14px;align-items:flex-start">{cells}<span style="font-size:60px;font-weight:800;align-self:center">...</span></div>'


# ---------------------------------------------------------------- path with lamp posts (both sides)
def path_posts(length_label='24 m', gap_label='3 m', w=1100):
    h = 230; out = ''
    out += f'<rect x="40" y="80" width="{w-80}" height="70" fill="#E9E1CF" stroke="{NAVY}" stroke-width="3"/>'
    def post(x, y):
        return f'<circle cx="{x}" cy="{y}" r="15" fill="{YEL}" stroke="{NAVY}" stroke-width="4"/>'
    xs = [40, 40 + 150, 40 + 300]
    for y in (66, 164):
        for x in xs: out += post(x, y)
        out += post(w - 40, y)
        out += f'<text x="{(40 + w - 40)/2 + 70}" y="{y+8}" font-size="34" font-weight="800" text-anchor="middle" fill="{NAVY}" font-family="{F}">. . . . .</text>'
    out += f'<line x1="40" y1="195" x2="190" y2="195" stroke="{TEAL}" stroke-width="4"/><text x="115" y="226" font-size="28" font-weight="800" text-anchor="middle" fill="{TEAL}" font-family="Nunito Sans, Arial">{E(gap_label)}</text>'
    out += f'<line x1="40" y1="30" x2="{w-40}" y2="30" stroke="{NAVY}" stroke-width="4"/><text x="{w/2}" y="22" font-size="30" font-weight="800" text-anchor="middle" fill="{NAVY}" font-family="{F}">{E(length_label)}</text>'
    return svg(out, w, h, 'A path with lamp posts on both sides')


# ---------------------------------------------------------------- window (grid of panes)
def window(cols, rows, cell=100):
    w = cols * cell + 16; h = rows * cell + 16
    out = f'<rect x="8" y="8" width="{cols*cell}" height="{rows*cell}" fill="#CFE3F5" stroke="{NAVY}" stroke-width="8"/>'
    for c in range(1, cols):
        out += f'<line x1="{8+c*cell}" y1="8" x2="{8+c*cell}" y2="{8+rows*cell}" stroke="{NAVY}" stroke-width="6"/>'
    for r in range(1, rows):
        out += f'<line x1="8" y1="{8+r*cell}" x2="{8+cols*cell}" y2="{8+r*cell}" stroke="{NAVY}" stroke-width="6"/>'
    return svg(out, w, h, f'A window with {cols} by {rows} panes')


# ---------------------------------------------------------------- column addition with letters
def letter_sum(top, bot, res):
    row = lambda s, op='': (f'<div style="display:flex;gap:10px;justify-content:flex-end;align-items:center;font-size:64px;font-weight:800;font-family:{F}">'
                            f'<span style="width:50px;color:{TEAL}">{op}</span>' + ''.join(f'<span style="width:66px;text-align:center;border:4px solid {NAVY};border-radius:10px;background:{WHITE}">{c}</span>' for c in s) + '</div>')
    return (f'<div style="display:flex;flex-direction:column;gap:8px;align-items:flex-end">{row(top)}'
            f'{row(bot, "+")}<div style="border-top:5px solid {NAVY};width:100%"></div>{row(res, "=")}</div>')
