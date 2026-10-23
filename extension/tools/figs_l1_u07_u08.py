"""Extra figure types for Level 1 units 7 and 8 (2D shapes; logic and sorting).

Plugged into figs.render() through the FIGS table.  Types:
  shapes      a row (or rows) of named 2D shapes with a label under each (triangle, square, rectangle, tall_rectangle, circle,
              pentagon, hexagon, heptagon, octagon); sizes are fixed so shapes of one kind look alike
  grids       one or more plain rectangular grids of small squares, side by side, with a label under each
  draw        a free drawing: polygons, lines (solid or dashed), circles and text in a 0..W x 0..H box (used for joined squares,
              cut lines and the triangle-counting figures)
  loops       a two-loop (Venn) picture inside a frame; the four regions can hold small text (numbers); empty regions stay empty
  logic_grid  a table of names (rows) against things (columns); marks "r,c" -> "yes" (tick) or "no" (cross) are drawn in the cell
  latin       a 4 by 4 number grid: given numbers are printed, other cells are empty boxes
Palette: NAVY / TEAL / SKY / SOFT only, so figs.recolour() gives the black-and-white print version (SKY and SOFT go white, ink
goes black).  Nothing depends on colour: shapes are told apart by outline and label, ticks and crosses are drawn marks.
"""
import math
import figs as F

NAVY, TEAL, RED, SKY, SOFT, GREY = F.NAVY, F.TEAL, F.RED, F.SKY, F.SOFT, F.GREY
SW = 3.2


def _t(x, y, txt, size=26, fill=NAVY, anchor='middle', weight=700):
    return F._t(x, y, txt, size, fill, anchor, weight)


def _fillc(name):
    return {'sky': SKY, 'soft': SOFT, 'none': 'none', 'white': '#fff'}.get(name, name or SKY)


# ------------------------------------------------------------------------------------------------ shapes
SIDES = {'triangle': 3, 'square': 4, 'rectangle': 4, 'tall_rectangle': 4, 'pentagon': 5, 'hexagon': 6, 'heptagon': 7, 'octagon': 8,
         'circle': 0}


def shape_path(name, cx, cy, r=34):
    st = f'fill="{SKY}" stroke="{NAVY}" stroke-width="{SW}" stroke-linejoin="round"'
    if name == 'circle':
        return f'<circle cx="{cx}" cy="{cy}" r="{r}" {st}/>'
    if name == 'square':
        return f'<rect x="{cx - r + 3}" y="{cy - r + 3}" width="{2 * r - 6}" height="{2 * r - 6}" {st}/>'
    if name == 'rectangle':
        return f'<rect x="{cx - r - 6}" y="{cy - r * 0.62}" width="{2 * r + 12}" height="{r * 1.24}" {st}/>'
    if name == 'tall_rectangle':
        return f'<rect x="{cx - r * 0.62}" y="{cy - r - 6}" width="{r * 1.24}" height="{2 * r + 12}" {st}/>'
    if name == 'triangle':
        return f'<path d="M{cx} {cy - r} L{cx + r + 2} {cy + r * 0.8} L{cx - r - 2} {cy + r * 0.8}Z" {st}/>'
    n = SIDES[name]
    rr = r + 2
    pts = []
    for k in range(n):
        a = -math.pi / 2 + 2 * math.pi * k / n
        pts.append(f'{cx + rr * math.cos(a):.1f},{cy + rr * math.sin(a):.1f}')
    return f'<polygon points="{" ".join(pts)}" {st}/>'


def shapes(spec, w=None):
    items = spec['items']
    per = spec.get('per_row', 6)
    cw, rh = 100, 120 if spec.get('labels', True) else 96
    rows = [items[i:i + per] for i in range(0, len(items), per)]
    P = []
    for r, row in enumerate(rows):
        for c, it in enumerate(row):
            name = it['name'] if isinstance(it, dict) else it
            lab = it.get('label') if isinstance(it, dict) else None
            if lab is None and spec.get('labels', True):
                lab = str(r * per + c + 1) if spec.get('number', True) else ''
            cx, cy = 8 + c * cw + cw / 2, 8 + r * rh + 50
            P.append(shape_path(name, cx, cy))
            if lab:
                P.append(_t(cx, cy + 74, lab, 30))
    W = 16 + min(len(items), per) * cw
    H = 16 + len(rows) * rh - (0 if spec.get('labels', True) else 0)
    return F._wrap(''.join(P), W, H, 'shapes', w or round(W * 0.2, 1))


# ------------------------------------------------------------------------------------------------ grids
def grids(spec, w=None):
    cs = 46
    P = []
    x = 8
    H = 0
    for g in spec['grids']:
        c, r = g['cols'], g['rows']
        for i in range(c):
            for j in range(r):
                P.append(f'<rect x="{x + i * cs}" y="{8 + j * cs}" width="{cs}" height="{cs}" fill="{SKY}" stroke="{NAVY}" stroke-width="{SW}"/>')
        if g.get('label'):
            P.append(_t(x + c * cs / 2, 8 + r * cs + 38, g['label'], 30))
        H = max(H, 8 + r * cs + (48 if g.get('label') else 8))
        x += c * cs + 56
    return F._wrap(''.join(P), x - 56 + 8, H, 'grids of small squares', w or round((x - 48) * 0.2, 1))


# ------------------------------------------------------------------------------------------------ draw
def draw(spec, w=None):
    P = []
    for e in spec['elements']:
        dash = ' stroke-dasharray="10 8"' if e.get('dash') else ''
        if 'poly' in e:
            pts = ' '.join(f'{x},{y}' for x, y in e['poly'])
            P.append(f'<polygon points="{pts}" fill="{_fillc(e.get("fill", "sky"))}" stroke="{NAVY}" stroke-width="{e.get("sw", SW)}" stroke-linejoin="round"{dash}/>')
        elif 'line' in e:
            x1, y1, x2, y2 = e['line']
            P.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{NAVY}" stroke-width="{e.get("sw", SW)}" stroke-linecap="round"{dash}/>')
        elif 'circle' in e:
            cx, cy, r = e['circle']
            P.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{_fillc(e.get("fill", "sky"))}" stroke="{NAVY}" stroke-width="{SW}"{dash}/>')
        elif 'text' in e:
            x, y, t = e['text'][:3]
            size = e['text'][3] if len(e['text']) > 3 else 30
            P.append(_t(x, y, t, size))
    return F._wrap(''.join(P), spec['w'], spec['h'], spec.get('label', 'drawing'), w or round(spec['w'] * spec.get('scale', 0.2), 1))


# ------------------------------------------------------------------------------------------------ loops
def loops(spec, w=None):
    """Two overlapping loops in a frame.  regions: {a, ab, b, out} -> list of strings (printed in small rows)."""
    W, H = 520, 330
    r = 110
    ax, bx, cy = 190, 330, 175
    reg = spec.get('regions') or {}
    P = [f'<rect x="6" y="6" width="{W - 12}" height="{H - 12}" rx="10" fill="#fff" stroke="{NAVY}" stroke-width="{SW}"/>']
    P.append(f'<circle cx="{ax}" cy="{cy}" r="{r}" fill="{SKY}" fill-opacity="0.55" stroke="none"/>')
    P.append(f'<circle cx="{bx}" cy="{cy}" r="{r}" fill="{SOFT}" fill-opacity="0.55" stroke="none"/>')
    P.append(f'<circle cx="{ax}" cy="{cy}" r="{r}" fill="none" stroke="{NAVY}" stroke-width="{SW + 0.6}"/>')   # outlines on top of the fills (no grey line in print)
    P.append(f'<circle cx="{bx}" cy="{cy}" r="{r}" fill="none" stroke="{NAVY}" stroke-width="{SW + 0.6}" stroke-dasharray="14 7"/>')
    P.append(_t(ax - 40, 36, spec['a'], 27))
    P.append(_t(bx + 40, 36, spec['b'], 27))

    def put(key, cx, cyy, per_row):
        vals = reg.get(key) or []
        if not vals:
            return
        rows = [vals[i:i + per_row] for i in range(0, len(vals), per_row)]
        y0 = cyy - (len(rows) - 1) * 17
        for k, row in enumerate(rows):
            P.append(_t(cx, y0 + k * 34 + 10, '  '.join(str(v) for v in row), 28))
    put('a', ax - 45, cy, 2)
    put('ab', (ax + bx) / 2, cy, 1)
    put('b', bx + 45, cy, 2)
    put('out', 460, 280, 2)
    return F._wrap(''.join(P), W, H, 'two-loop picture', w or round(W * 0.2, 1))


# ------------------------------------------------------------------------------------------------ logic grid
def logic_grid(spec, w=None):
    rows, cols = spec['rows'], spec['cols']
    marks = spec.get('marks') or {}
    cs = 66
    lw = 128
    top = 58
    P = []
    for j, c in enumerate(cols):
        P.append(_t(lw + j * cs + cs / 2, 38, c, 25))
    for i, rname in enumerate(rows):
        y = top + i * cs
        P.append(_t(lw - 10, y + cs / 2 + 9, rname, 28, anchor='end'))
        for j in range(len(cols)):
            x = lw + j * cs
            P.append(f'<rect x="{x}" y="{y}" width="{cs}" height="{cs}" fill="#fff" stroke="{NAVY}" stroke-width="{SW}"/>')
            m = marks.get(f'{i},{j}')
            if m == 'yes':
                P.append(f'<path d="M{x + 16},{y + 36} L{x + 29},{y + 50} L{x + 52},{y + 16}" fill="none" stroke="{NAVY}" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>')
            elif m == 'no':
                P.append(f'<path d="M{x + 17},{y + 17} L{x + 49},{y + 49} M{x + 49},{y + 17} L{x + 17},{y + 49}" fill="none" stroke="{NAVY}" stroke-width="5.5" stroke-linecap="round"/>')
    W = lw + len(cols) * cs + 8
    H = top + len(rows) * cs + 8
    return F._wrap(''.join(P), W, H, 'logic grid', w or round(W * 0.2, 1))


# ------------------------------------------------------------------------------------------------ latin square
def latin(spec, w=None):
    g = spec['rows']
    cs = 78
    P = []
    for i, row in enumerate(g):
        for j, v in enumerate(row):
            x, y = 8 + j * cs, 8 + i * cs
            fill = SOFT if v is not None else '#fff'
            P.append(f'<rect x="{x}" y="{y}" width="{cs}" height="{cs}" fill="{fill}" stroke="{NAVY}" stroke-width="{SW + 0.4}"/>')
            if v is not None:
                P.append(_t(x + cs / 2, y + cs / 2 + 16, v, 50, weight=800))
    n = len(g)
    return F._wrap(''.join(P), 16 + n * cs, 16 + len(g) * cs, 'number grid', w or round((16 + n * cs) * 0.2, 1))


FIGS = {'shapes': shapes, 'grids': grids, 'draw': draw, 'loops': loops, 'logic_grid': logic_grid, 'latin': latin}
