"""Extra figure types for Level 1 units 3 and 4 (picture graphs; repeating and growing patterns).

Plugged into figs.render() through the FIGS table (figs.py loads every tools/figs_*.py that defines FIGS).
All drawings use the project palette (NAVY, SKY, YEL) so figs.recolour() makes the black-and-white print version:
navy -> black, light fills -> white.  Nothing depends on colour: every shape is told apart by its outline, and
"dark" beads are solid (navy -> black), "white" beads are empty.
"""
import itertools
import figs as F

NAVY, SKY, YEL, GREY = F.NAVY, F.SKY, F.YEL, F.GREY
_uid = itertools.count(1)
SC = 0.14  # mm per viewBox unit when a spec gives no width_mm (keeps every figure the same scale)
GROW = 1.4  # picture graphs are drawn 1.4 times larger than first built (icons were too small for ages 6-8)
SW = 3.0   # stroke width in viewBox units (>= 0.5 pt when the figure is 100 to 170 mm wide)


def _t(x, y, txt, size=28, anchor='middle', weight=700, fill=NAVY):
    return F._t(x, y, txt, size, fill, anchor, weight)


# ---------------------------------------------------------------- icons (drawn in a 44 x 44 box at x, y)
def icon(name, x, y, s=44, clip=None):
    """One small picture.  clip='left' draws only the left half (a half picture)."""
    cx, cy = x + s / 2, y + s / 2
    st = f'stroke="{NAVY}" stroke-width="{SW}" stroke-linejoin="round" stroke-linecap="round"'
    r = s * 0.40
    if name == 'face':
        g = (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{SKY}" {st}/><circle cx="{cx - 7}" cy="{cy - 5}" r="2.6" fill="{NAVY}"/>'
             f'<circle cx="{cx + 7}" cy="{cy - 5}" r="2.6" fill="{NAVY}"/><path d="M{cx - 8} {cy + 5} Q{cx} {cy + 14} {cx + 8} {cy + 5}" fill="none" {st}/>')
    elif name == 'star':
        pts = []
        import math
        for k in range(10):
            ang = -math.pi / 2 + k * math.pi / 5
            rad = s * 0.47 if k % 2 == 0 else s * 0.2
            pts.append(f'{cx + rad * math.cos(ang):.1f},{cy + rad * math.sin(ang) + 1:.1f}')
        g = f'<polygon points="{" ".join(pts)}" fill="{YEL}" {st}/>'
    elif name == 'book':
        g = (f'<rect x="{x + 7}" y="{y + 5}" width="{s - 14}" height="{s - 10}" rx="3" fill="{SKY}" {st}/>'
             f'<line x1="{x + 15}" y1="{y + 6}" x2="{x + 15}" y2="{y + s - 6}" {st}/><line x1="{x + 21}" y1="{cy - 5}" x2="{x + s - 12}" y2="{cy - 5}" {st}/>'
             f'<line x1="{x + 21}" y1="{cy + 4}" x2="{x + s - 12}" y2="{cy + 4}" {st}/>')
    elif name == 'ball':
        g = (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{SKY}" {st}/><path d="M{cx - r} {cy} Q{cx} {cy - 11} {cx + r} {cy}" fill="none" {st}/>'
             f'<path d="M{cx - r * 0.5} {cy + r * 0.85} Q{cx} {cy + 2} {cx + r * 0.5} {cy + r * 0.85}" fill="none" {st}/>')
    elif name == 'kite':
        g = (f'<path d="M{cx} {y + 3} L{x + s - 6} {cy - 3} L{cx} {y + s - 9} L{x + 6} {cy - 3}Z" fill="{SKY}" {st}/>'
             f'<line x1="{cx}" y1="{y + 3}" x2="{cx}" y2="{y + s - 9}" {st}/><line x1="{x + 6}" y1="{cy - 3}" x2="{x + s - 6}" y2="{cy - 3}" {st}/>'
             f'<path d="M{cx} {y + s - 9} q-6 5 0 8" fill="none" {st}/>')
    elif name == 'heart':
        g = (f'<path d="M{cx} {y + s - 6} C{x - 4} {cy + 2} {x + 4} {y + 2} {cx} {y + 12} C{x + s - 4} {y + 2} {x + s + 4} {cy + 2} {cx} {y + s - 6}Z" '
             f'fill="{SKY}" {st}/>')
    elif name == 'cookie':
        g = (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{YEL}" {st}/>' + ''.join(
            f'<circle cx="{cx + dx}" cy="{cy + dy}" r="2.8" fill="{NAVY}"/>' for dx, dy in ((-8, -6), (7, -8), (0, 2), (-6, 9), (9, 7))))
    elif name == 'flag':
        g = (f'<line x1="{x + 11}" y1="{y + 4}" x2="{x + 11}" y2="{y + s - 3}" {st}/>'
             f'<path d="M{x + 11} {y + 5} L{x + s - 6} {y + 13} L{x + 11} {y + 22}Z" fill="{SKY}" {st}/>')
    else:
        raise ValueError('icon ' + name)
    if clip == 'left':
        cid = f'hf{next(_uid)}'
        return (f'<clipPath id="{cid}"><rect x="{x - 2}" y="{y - 2}" width="{s / 2 + 2}" height="{s + 4}"/></clipPath>'
                f'<g clip-path="url(#{cid})">{g}</g>'
                f'<line x1="{cx}" y1="{y + 1}" x2="{cx}" y2="{y + s - 1}" stroke="{NAVY}" stroke-width="1.8" stroke-dasharray="4 4"/>')
    return g


# ---------------------------------------------------------------- picture graph
def _one_graph(g, y0):
    """Draw a picture graph with its top at y0.  Returns (svg parts, height)."""
    LAB, CELL, RH = 150, 50, 56
    rows = g['rows']
    slots = max(int(r.get('n', 0) + 0.99) + r.get('slots', 0) for r in rows)
    slots = max(slots, g.get('min_slots', 8))
    W = LAB + slots * CELL + 4
    parts = []
    y = y0
    if g.get('title'):
        parts.append(_t(W / 2, y + 26, g['title'], 29))
        y += 42
    icon_name = g['icon']
    top = y
    for i, r in enumerate(rows):
        ry = y + i * RH
        parts.append(f'<rect x="2" y="{ry}" width="{LAB}" height="{RH}" fill="#fff" stroke="{NAVY}" stroke-width="{SW}"/>')
        parts.append(_t(2 + LAB / 2, ry + RH / 2 + 9, r['label'], 26 if len(r['label']) < 9 else 22))
        parts.append(f'<rect x="{2 + LAB}" y="{ry}" width="{slots * CELL}" height="{RH}" fill="#fff" stroke="{NAVY}" stroke-width="{SW}"/>')
        n = r.get('n', 0)
        full = int(n)
        for k in range(full):
            parts.append(icon(icon_name, 2 + LAB + k * CELL + 3, ry + 5, CELL - 6))
        if n - full >= 0.5:
            parts.append(icon(icon_name, 2 + LAB + full * CELL + 3, ry + 5, CELL - 6, clip='left'))
            full += 1
        for k in range(r.get('slots', 0)):
            x = 2 + LAB + (full + k) * CELL + 6
            parts.append(f'<rect x="{x}" y="{ry + 9}" width="{CELL - 12}" height="{RH - 18}" rx="5" fill="none" stroke="{GREY}" stroke-width="2" stroke-dasharray="5 5"/>')
    y += len(rows) * RH + 8
    # key
    kx = 2
    parts.append(_t(kx, y + 32, 'Key:', 26, 'start'))
    parts.append(icon(icon_name, kx + 64, y + 4, 40))
    parts.append(_t(kx + 112, y + 32, g['key'], 26, 'start'))
    if g.get('half_key'):
        parts.append(icon(icon_name, kx + 320, y + 4, 40, clip='left'))
        parts.append(_t(kx + 368, y + 32, g['half_key'], 26, 'start'))
    y += 50
    return parts, y - y0, W


def picture_graph(spec, width_mm=None):
    graphs = spec['graphs'] if 'graphs' in spec else [spec]
    parts, y, W = [], 4, 0
    for gi, g in enumerate(graphs):
        p, h, w = _one_graph(g, y)
        parts += p
        y += h + (18 if gi < len(graphs) - 1 else 0)
        W = max(W, w)
    return F._wrap(''.join(parts), W, y + 2, 'picture graph', width_mm or round(W * spec.get('scale', SC) * GROW, 1))


# ---------------------------------------------------------------- a row of shapes with place numbers
def shape(name, cx, cy, r=22):
    st = f'stroke="{NAVY}" stroke-width="{SW}" stroke-linejoin="round" stroke-linecap="round"'
    if name == 'circle':
        return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{SKY}" {st}/>'
    if name == 'square':
        return f'<rect x="{cx - r}" y="{cy - r}" width="{2 * r}" height="{2 * r}" fill="{SKY}" {st}/>'
    if name == 'triangle':
        return f'<path d="M{cx} {cy - r - 2} L{cx + r + 3} {cy + r - 2} L{cx - r - 3} {cy + r - 2}Z" fill="{SKY}" {st}/>'
    if name == 'diamond':
        return f'<path d="M{cx} {cy - r - 3} L{cx + r} {cy} L{cx} {cy + r + 3} L{cx - r} {cy}Z" fill="{SKY}" {st}/>'
    if name == 'star':
        return icon('star', cx - 24, cy - 24, 48)
    if name == 'heart':
        return icon('heart', cx - 24, cy - 24, 48)
    if name == 'dark':
        return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{NAVY}" {st}/>'
    if name == 'white':
        return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#fff" {st}/>'
    if len(name) == 1 and name.isalpha():
        return _t(cx, cy + 12, name, 40)
    raise ValueError('shape ' + name)


def shape_row(items, start_no=1, per_row=10, numbers=True, width_mm=None, items2=None):
    """items: shape names, or None for an empty box the child fills in.  items2 (optional) is a second row drawn under the first
    (same places).  Place numbers sit under the boxes."""
    CW = 62
    rows = [items[i:i + per_row] for i in range(0, len(items), per_row)]
    rows2 = [items2[i:i + per_row] for i in range(0, len(items2), per_row)] if items2 else None
    block = CW * (2 if items2 else 1) + (34 if numbers else 10)
    parts = []
    for r, row in enumerate(rows):
        y = 4 + r * block
        for c, nm in enumerate(row):
            x = 4 + c * CW
            for k, rr in enumerate([row] + ([rows2[r]] if items2 else [])):
                nm = rr[c]
                yy = y + k * CW
                if nm is None:
                    parts.append(f'<rect x="{x + 3}" y="{yy + 3}" width="{CW - 6}" height="{CW - 6}" rx="6" fill="none" stroke="{GREY}" stroke-width="2.4" stroke-dasharray="6 5"/>')
                else:
                    parts.append(shape(nm, x + CW / 2, yy + CW / 2))
            if numbers:
                parts.append(_t(x + CW / 2, y + block - 10, start_no + r * per_row + c, 24))
    W = min(len(items), per_row) * CW + 8
    H = len(rows) * block + 4
    return F._wrap(''.join(parts), W, H, 'row of shapes', width_mm or round(W * SC, 1))


# ---------------------------------------------------------------- sticks
def _edges_tri(n, L, H):
    e = set()
    def add(a, b):
        e.add(tuple(sorted((a, b))))
    for i in range(n):
        j = i // 2
        if i % 2 == 0:
            a, b, ap = (j * L, H), ((j + 1) * L, H), ((j + 0.5) * L, 0)
            add(a, b); add(a, ap); add(b, ap)
        else:
            a, b, bt = ((j + 0.5) * L, 0), ((j + 1.5) * L, 0), ((j + 1) * L, H)
            add(a, b); add(a, bt); add(b, bt)
    return e


def _edges_sq(n, L):
    e = set()
    for i in range(n):
        a, b, c, d = (i * L, 0), ((i + 1) * L, 0), ((i + 1) * L, L), (i * L, L)
        for p, q in ((a, b), (b, c), (c, d), (d, a)):
            e.add(tuple(sorted((p, q))))
    return e


def stick_rows(rows, width_mm=None):
    """rows: [{'kind': 'tri'|'sq'|'tri_sep', 'n': int, 'label': str}] drawn one under the other as sticks.
    Returns sticks per row through count_sticks()."""
    L, H = 56, 49
    parts, y = [], 6
    W = 10
    for r in rows:
        n, kind = r['n'], r['kind']
        if kind == 'tri':
            edges = _edges_tri(n, L, H); h = H; w = (n // 2 + 1) * L + (L / 2 if n % 2 == 0 else 0)
            w = (n + 1) * L / 2
        elif kind == 'sq':
            edges = _edges_sq(n, H); h = H; w = n * H
        elif kind == 'tri_sep':
            edges = set()
            for i in range(n):
                ox = i * (L + 16)
                a, b, ap = (ox, H), (ox + L, H), (ox + L / 2, 0)
                for p, q in ((a, b), (a, ap), (b, ap)):
                    edges.add(tuple(sorted((p, q))))
            h = H; w = n * (L + 16) - 16
        else:
            raise ValueError(kind)
        x0 = 175
        for (p, q) in sorted(edges):
            parts.append(f'<line x1="{x0 + p[0]:.1f}" y1="{y + 8 + p[1]:.1f}" x2="{x0 + q[0]:.1f}" y2="{y + 8 + q[1]:.1f}" stroke="{NAVY}" stroke-width="6.5" stroke-linecap="round"/>')
        if r.get('label'):
            parts.append(_t(2, y + h / 2 + 18, r['label'], 24, 'start'))
        W = max(W, x0 + w + 12)
        y += h + 22
    return F._wrap(''.join(parts), W, y, 'sticks', width_mm or round(W * SC, 1))


def count_sticks(kind, n):
    """Sticks needed, counted from the drawn edges (independent of the rule 2n+1 / 3n+1 / 3n)."""
    if kind == 'tri':
        return len(_edges_tri(n, 56, 49))
    if kind == 'sq':
        return len(_edges_sq(n, 49))
    if kind == 'tri_sep':
        return 3 * n
    raise ValueError(kind)


# ---------------------------------------------------------------- towers of blocks
def towers(counts, width_mm=None):
    """Towers of square blocks, one tower per step (a growing pattern).  None = an empty dashed place for the child to draw."""
    B, G = 34, 46
    top = 4
    mx = max(c for c in counts if c) + (3 if None in counts else 0)
    H = mx * B + 52
    parts = []
    for i, n in enumerate(counts):
        x = 8 + i * (3 * B + G)
        if n is None:
            parts.append(f'<rect x="{x + B}" y="{top}" width="{B}" height="{mx * B}" rx="6" fill="none" stroke="{GREY}" stroke-width="2.4" stroke-dasharray="6 5"/>')
        else:
            for k in range(n):
                parts.append(f'<rect x="{x + B}" y="{top + (mx - 1 - k) * B}" width="{B}" height="{B}" fill="{SKY}" stroke="{NAVY}" stroke-width="{SW}"/>')
        parts.append(_t(x + 1.5 * B, top + mx * B + 28, f'Tower {i + 1}', 24))
    W = 8 + len(counts) * (3 * B + G) - G + 8
    return F._wrap(''.join(parts), W, H, 'towers of blocks', width_mm or round(W * SC, 1))


# ---------------------------------------------------------------- tally marks
def tally(rows, width_mm=None):
    """rows: [{'label','n'}]: groups of 4 upright strokes crossed by a fifth."""
    RH, LAB = 58, 170
    parts = []
    mx = max(r['n'] for r in rows)
    groups = (mx + 4) // 5
    W = LAB + groups * 76 + 20
    for i, r in enumerate(rows):
        y = 4 + i * RH
        parts.append(f'<rect x="2" y="{y}" width="{LAB}" height="{RH}" fill="#fff" stroke="{NAVY}" stroke-width="{SW}"/>')
        parts.append(_t(2 + LAB / 2, y + RH / 2 + 9, r['label'], 26))
        parts.append(f'<rect x="{2 + LAB}" y="{y}" width="{W - LAB - 4}" height="{RH}" fill="#fff" stroke="{NAVY}" stroke-width="{SW}"/>')
        n, gx = r['n'], 2 + LAB + 16
        while n > 0:
            k = min(5, n)
            for j in range(min(k, 4)):
                parts.append(f'<line x1="{gx + j * 13}" y1="{y + 10}" x2="{gx + j * 13}" y2="{y + RH - 10}" stroke="{NAVY}" stroke-width="4.4" stroke-linecap="round"/>')
            if k == 5:
                parts.append(f'<line x1="{gx - 6}" y1="{y + RH - 14}" x2="{gx + 45}" y2="{y + 14}" stroke="{NAVY}" stroke-width="4.4" stroke-linecap="round"/>')
            gx += 76
            n -= k
    return F._wrap(''.join(parts), W, 4 * 0 + len(rows) * RH + 8, 'tally chart', width_mm or round(W * SC, 1))


def grow_table(spec, width_mm=None):
    """A growing pattern as a table: top row 'head' (day, week...) 1, 2, 3...; second row 'label' (leaves...) with the values;
    small arcs and the step (+3) drawn between neighbouring values under the table."""
    vals = spec['values']
    n = len(vals)
    LAB, CW, RH = 170, 78, 56
    W = LAB + n * CW + 6
    P = []
    for r, (lab, row) in enumerate(((spec['head'], list(range(1, n + 1))), (spec['label'], vals))):
        y = 4 + r * RH
        P.append(f'<rect x="3" y="{y}" width="{LAB}" height="{RH}" fill="{SKY if r == 0 else '#fff'}" stroke="{NAVY}" stroke-width="{SW}"/>')
        P.append(_t(3 + LAB / 2, y + RH / 2 + 10, lab, 28))
        for c, v in enumerate(row):
            x = 3 + LAB + c * CW
            P.append(f'<rect x="{x}" y="{y}" width="{CW}" height="{RH}" fill="{SKY if r == 0 else '#fff'}" stroke="{NAVY}" stroke-width="{SW}"/>')
            P.append(_t(x + CW / 2, y + RH / 2 + 10, v, 30))
    yb = 4 + 2 * RH + 4
    for c in range(n - 1):
        a = 3 + LAB + c * CW + CW / 2 + 6
        b = 3 + LAB + (c + 1) * CW + CW / 2 - 6
        P.append(f'<path d="M{a},{yb} Q{(a + b) / 2},{yb + 30} {b},{yb}" fill="none" stroke="{NAVY}" stroke-width="3" stroke-linecap="round"/>')
        P.append(_t((a + b) / 2, yb + 52, spec['step'], 26))
    return F._wrap(''.join(P), W, yb + 62, 'growing pattern table', width_mm or round(W * 0.17, 1))


FIGS = {'grow_table': grow_table, 
    'picture_graph': lambda s, w: picture_graph(s, w),
    'shape_row': lambda s, w: shape_row(s['items'], s.get('start_no', 1), s.get('per_row', 10), s.get('numbers', True), w, s.get('items2')),
    'stick_rows': lambda s, w: stick_rows(s['rows'], w),
    'towers': lambda s, w: towers(s['counts'], w),
    'tally': lambda s, w: tally(s['rows'], w),
}
