"""Inline SVG visuals shared by the deck, guide, workbook and home sheet.

Every function returns an <svg> string that scales to its container (width:100%).
Palette is the project palette (hp/wb_style.css, rebuild/slidekit.py).
"""
import random

NAVY = '#1B2A49'; TEAL = '#1F7A6F'; YEL = '#FFC93C'; SKY = '#DDEBF7'; SOFT = '#FFF0C2'; RED = '#D64545'; GREY = '#8A94AD'
FONT = "Fredoka, 'Nunito Sans', Arial, sans-serif"


def _stick(x, y, h=62, w=6, fill=YEL):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="3" fill="{fill}" stroke="{NAVY}" stroke-width="1.6"/>'


def bundles(tens, ones, label=None, style='sticks', stroke_scale=1.0):
    """tens bundles then ones singles, drawn with a band on every ten. style 'kit' draws bars and squares."""
    if style == 'kit':
        return kit_blocks(tens, ones, label)
    bw = 84                      # width of one bundle slot
    ow = 13                      # width of one single slot
    gap = 34 if tens and ones else 0
    width = max(40, tens * bw + gap + ones * ow + 10)
    # wrap long rows of singles: more than 14 singles go on a second line
    rows_ones = 1 if ones <= 14 else 2
    h = 96 + (30 if label else 0) + (70 if rows_ones == 2 else 0)
    parts = []
    x = 6
    for _ in range(tens):
        for i in range(10):
            parts.append(_stick(x + i * 7, 8))
        parts.append(f'<rect x="{x - 4}" y="28" width="78" height="14" rx="6" fill="{TEAL}" stroke="{NAVY}" stroke-width="1.6"/>')
        x += bw
    x += gap
    for i in range(ones):
        if i == 14:
            x = 6 + tens * bw + gap
        yy = 8 if i < 14 else 80
        xx = x + (i % 14) * ow
        parts.append(_stick(xx, yy, h=62, w=6))
    cap = ''
    if label:
        cap = f'<text x="{width / 2}" y="{h - 8}" font-size="26" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="{FONT}">{label}</text>'
    vw = max(width, 14 * ow + 10)
    return f'<svg viewBox="0 0 {vw} {h}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{tens} bundles of ten and {ones} single sticks" style="width:100%;height:auto;display:block">{"".join(parts)}{cap}</svg>'


def kit_blocks(tens, ones, label=None):
    """Base-ten paper: a bar of ten squares is a ten; a square is a one."""
    sq = 26
    parts = []
    y = 6
    for _ in range(tens):
        for i in range(10):
            parts.append(f'<rect x="{6 + i * sq}" y="{y}" width="{sq}" height="{sq}" fill="{SKY}" stroke="{NAVY}" stroke-width="1.8"/>')
        y += sq + 6
    x0 = 6 + 10 * sq + 30
    for i in range(ones):
        parts.append(f'<rect x="{x0 + (i % 5) * (sq + 4)}" y="{6 + (i // 5) * (sq + 4)}" width="{sq}" height="{sq}" fill="{SOFT}" stroke="{NAVY}" stroke-width="1.8"/>')
    h = max(y, 6 + ((ones + 4) // 5) * (sq + 4)) + 4
    w = x0 + 5 * (sq + 4) + 6
    cap = ''
    if label:
        cap = f'<text x="{w / 2}" y="{h + 28}" font-size="24" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="{FONT}">{label}</text>'
        h += 36
    return f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{tens} tens bars and {ones} ones squares" style="width:100%;height:auto;display:block">{"".join(parts)}{cap}</svg>'


def scatter(n, seed=1, w=900, h=420, shape='star'):
    rnd = random.Random(seed)
    pts = []
    tries = 0
    while len(pts) < n and tries < 20000:
        tries += 1
        x, y = rnd.uniform(40, w - 40), rnd.uniform(40, h - 40)
        if all((x - a) ** 2 + (y - b) ** 2 > 78 ** 2 for a, b in pts):
            pts.append((x, y))
    assert len(pts) == n, 'could not place all points'
    out = []
    import math
    for (x, y) in pts:
        r1, r2 = 26, 11
        d = ' '.join(f'{x + (r1 if i % 2 == 0 else r2) * math.sin(i * math.pi / 5):.1f},{y - (r1 if i % 2 == 0 else r2) * math.cos(i * math.pi / 5):.1f}' for i in range(10))
        out.append(f'<polygon points="{d}" fill="{YEL}" stroke="{NAVY}" stroke-width="2.4" stroke-linejoin="round"/>')
    return f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{n} stars scattered" style="width:100%;height:auto;display:block">{"".join(out)}</svg>'


def ten_frame(filled, extra=0):
    cell = 64
    parts = []

    def frame(x0, k):
        for r in range(2):
            for c in range(5):
                x, y = x0 + c * cell, 6 + r * cell
                parts.append(f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" fill="#fff" stroke="{NAVY}" stroke-width="2.4"/>')
                if r * 5 + c < k:
                    parts.append(f'<circle cx="{x + cell / 2}" cy="{y + cell / 2}" r="22" fill="{RED}" stroke="{NAVY}" stroke-width="2"/>')
    frame(6, filled)
    w = 5 * cell + 12
    if extra:
        frame(6 + 5 * cell + 40, extra)
        parts.append(f'<text x="{5 * cell + 26 + 0}" y="{6 + cell + 14}" font-size="46" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="{FONT}">+</text>')
        w = 10 * cell + 52
    return f'<svg viewBox="0 0 {w} {2 * cell + 12}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="ten frame with {filled} counters" style="width:100%;height:auto;display:block">{"".join(parts)}</svg>'


def ten_to_bundle():
    parts = []
    for i in range(10):
        parts.append(_stick(10 + i * 26, 10, h=90, w=10))
    parts.append(f'<text x="290" y="178" font-size="30" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="{FONT}">10 singles</text>')
    parts.append(f'<line x1="330" y1="60" x2="470" y2="60" stroke="{NAVY}" stroke-width="6"/><polygon points="490,60 466,46 466,74" fill="{NAVY}"/>')
    x = 530
    for i in range(10):
        parts.append(_stick(x + i * 11, 10, h=90, w=10))
    parts.append(f'<rect x="{x - 8}" y="40" width="{10 * 11 + 6}" height="22" rx="8" fill="{TEAL}" stroke="{NAVY}" stroke-width="2"/>')
    parts.append(f'<text x="{x + 55}" y="178" font-size="30" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="{FONT}">1 bundle of ten</text>')
    return f'<svg viewBox="0 0 700 200" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="ten single sticks tied into one bundle" style="width:100%;height:auto;display:block">{"".join(parts)}</svg>'


def number_line(start, end, step=1, label_every=None, marks=None, hide=None, jumps=None, highlight=None, width=1000, big=True):
    """Clean number line for ages 6-8.  start/end inclusive; a tick every `step`; a number under every `label_every`-th tick
    (default: about 11 labels); `marks` = numbers always labelled; `hide` = numbers shown as an empty box (for 'fill the gap');
    `jumps` = [(from, to, '+10'), ...] curved arrows above the line (labels in teal); `highlight` = numbers shown as yellow tiles."""
    n = (end - start) // step
    if label_every is None:
        label_every = step * max(1, -(-n // 10))
    pad = 40
    x = lambda v: pad + (v - start) / (end - start) * (width - 2 * pad)
    jh = 130 if jumps else 30
    base = jh + 40
    h = base + 110
    fs = 34 if big else 26
    p = [f'<line x1="{pad - 14}" y1="{base}" x2="{width - pad + 14}" y2="{base}" stroke="{NAVY}" stroke-width="5" stroke-linecap="round"/>']
    hide = set(hide or []); marks = set(marks or []); hl = set(highlight or [])
    v = start
    while v <= end:
        major = (v - start) % label_every == 0 or v in marks or v in hl
        p.append(f'<line x1="{x(v):.1f}" y1="{base - (18 if major else 10)}" x2="{x(v):.1f}" y2="{base + (18 if major else 10)}" stroke="{NAVY}" stroke-width="{4 if major else 2.5}"/>')
        if v in hide:
            p.append(f'<rect x="{x(v) - 26:.1f}" y="{base + 30}" width="52" height="52" rx="10" fill="#fff" stroke="{NAVY}" stroke-width="3.5"/>')
        elif major:
            if v in hl:
                p.append(f'<rect x="{x(v) - 30:.1f}" y="{base + 28}" width="60" height="52" rx="12" fill="{YEL}" stroke="{NAVY}" stroke-width="3"/>')
            p.append(f'<text x="{x(v):.1f}" y="{base + 68}" font-size="{fs}" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="{FONT}">{v}</text>')
        v += step
    for (a, b, lab) in (jumps or []):
        xa, xb = x(a), x(b); mid = (xa + xb) / 2; hg = min(80, 24 + abs(xb - xa) * 0.25)
        p.append(f'<path d="M{xa:.1f} {base - 20} Q{mid:.1f} {base - 20 - 2 * hg:.1f} {xb:.1f} {base - 44}" fill="none" stroke="{TEAL}" stroke-width="5" stroke-linecap="round"/>')
        p.append(f'<polygon points="{xb:.1f},{base - 18} {xb - 13:.1f},{base - 44} {xb + 13:.1f},{base - 44}" fill="{TEAL}"/>')
        p.append(f'<text x="{mid:.1f}" y="{base - 20 - hg - 12:.1f}" font-size="{fs - 4}" font-weight="800" text-anchor="middle" fill="{TEAL}" font-family="{FONT}">{lab}</text>')
    return f'<svg viewBox="0 0 {width} {h}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="number line from {start} to {end}" style="width:100%;height:auto;display:block">{"".join(p)}</svg>'


def hundred_square(blank=False, cell=58):
    p = []
    for r in range(10):
        for c in range(10):
            n = r * 10 + c + 1
            p.append(f'<rect x="{c * cell + 2}" y="{r * cell + 2}" width="{cell}" height="{cell}" fill="{SOFT if n % 10 == 0 else "#fff"}" stroke="{NAVY}" stroke-width="2"/>')
            if not blank:
                p.append(f'<text x="{c * cell + 2 + cell / 2}" y="{r * cell + 2 + cell * 0.66}" font-size="{cell * 0.42:.0f}" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="{FONT}">{n}</text>')
    return f'<svg viewBox="0 0 {10 * cell + 4} {10 * cell + 4}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="100 square" style="width:100%;height:auto;display:block">{"".join(p)}</svg>'


def number_strip_kit(start=0, end=50, per_row=26):
    """Cut-out strips of numbered cells (tape end to end)."""
    cw = 28; vals = list(range(start, end + 1)); rows = [vals[i:i + per_row] for i in range(0, len(vals), per_row)]
    p = []; y = 10
    for row in rows:
        for k, v in enumerate(row):
            p.append(f'<rect x="{4 + k * cw}" y="{y}" width="{cw}" height="52" fill="#fff" stroke="{NAVY}" stroke-width="1.8"/><text x="{4 + k * cw + cw / 2}" y="{y + 33}" font-size="14" font-weight="800" text-anchor="middle" fill="{RED if v % 10 == 0 else NAVY}" font-family="Nunito Sans, Arial">{v}</text>')
        p.append(f'<rect x="2" y="{y - 3}" width="{len(row) * cw + 4}" height="58" fill="none" stroke="#777" stroke-width="1.4" stroke-dasharray="7 5"/>')
        y += 90
    return f'<svg viewBox="0 0 {per_row * cw + 8} {y}" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;display:block">{"".join(p)}</svg>'


def cards_kit(labels, cols=5, w=130, h=90, round_=False):
    """Cut-out cards (digit cards, number cards, words). labels: list of strings."""
    p = []
    for i, t in enumerate(labels):
        cx, cy = 6 + (i % cols) * (w + 10), 6 + (i // cols) * (h + 10)
        if round_:
            p.append(f'<circle cx="{cx + w / 2}" cy="{cy + h / 2}" r="{min(w, h) / 2}" fill="#fff" stroke="#777" stroke-width="2" stroke-dasharray="7 5"/>')
        else:
            p.append(f'<rect x="{cx}" y="{cy}" width="{w}" height="{h}" rx="10" fill="#fff" stroke="#777" stroke-width="2" stroke-dasharray="7 5"/>')
        p.append(f'<text x="{cx + w / 2}" y="{cy + h / 2 + h * 0.18}" font-size="{h * 0.5:.0f}" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="{FONT}">{t}</text>')
    rows = (len(labels) + cols - 1) // cols
    return f'<svg viewBox="0 0 {cols * (w + 10) + 6} {rows * (h + 10) + 6}" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;display:block">{"".join(p)}</svg>'


def shapes_kit(shapes, size=70):
    """shapes: [{'kind': 'circle|square|triangle|rect', 'color': '#hex', 'n': count}] drawn as cut-outs."""
    p = []; i = 0; cols = 8
    for sh in shapes:
        for _ in range(sh.get('n', 1)):
            cx, cy = 50 + (i % cols) * (size + 24), 50 + (i // cols) * (size + 24); i += 1
            c = sh.get('color', YEL); k = sh['kind']; a = size / 2
            st = f'fill="{c}" stroke="#555" stroke-width="2" stroke-dasharray="6 4"'
            if k == 'circle': p.append(f'<circle cx="{cx}" cy="{cy}" r="{a}" {st}/>')
            elif k == 'square': p.append(f'<rect x="{cx - a}" y="{cy - a}" width="{size}" height="{size}" {st}/>')
            elif k == 'rect': p.append(f'<rect x="{cx - a * 1.3}" y="{cy - a * 0.7}" width="{size * 1.3}" height="{size * 0.7}" {st}/>')
            else: p.append(f'<polygon points="{cx},{cy - a} {cx + a * 1.1},{cy + a * 0.8} {cx - a * 1.1},{cy + a * 0.8}" {st}/>')
    rows = (i + cols - 1) // cols
    return f'<svg viewBox="0 0 {cols * (size + 24) + 30} {rows * (size + 24) + 40}" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;display:block">{"".join(p)}</svg>'


def kit_figure(spec):
    t = spec['type']
    if t == 'base_ten': return kit_page_svg()
    if t == 'hundred': return hundred(cell=spec.get('cell', 64))
    if t == 'hundred_square': return hundred_square(spec.get('blank', False))
    if t == 'number_strip': return number_strip_kit(spec.get('start', 0), spec.get('end', 50))
    if t == 'cards': return cards_kit([str(x) for x in spec['labels']], spec.get('cols', 5), spec.get('w', 130), spec.get('h', 90), spec.get('round', False))
    if t == 'shapes': return shapes_kit(spec['shapes'], spec.get('size', 70))
    if t == 'number_line': return number_line(**{k: v for k, v in spec.items() if k not in ('type', 'title', 'intro')})
    raise ValueError('unknown kit type ' + t)


MINT = '#BFE3DC'


def hundred(shade=(), shade2=(), hide=(), mark=(), outline=(), arrows=(), rows=(1, 10), cols=(1, 10), per=10, cell=46, qmarks=False, tags=None):
    """A numbered number square.  Cell (row r, column c) holds (r-1)*per + c.  rows and cols pick a window of the square.
    shade = yellow cells, shade2 = mint cells, hide = cells left empty (for the child to fill, or '?' when qmarks),
    mark = a red counter sits on the cell, outline = thick teal border, arrows = [[from, to, label], ...]."""
    shade, shade2, hide, mark, outline = set(shade), set(shade2), set(hide), set(mark), set(outline)
    r0, r1 = rows; c0, c1 = cols
    pad = 8
    vert = any(abs(b - a) >= per for (a, b, _) in arrows)
    W = pad * 2 + (c1 - c0 + 1) * cell + (cell * 0.9 if vert else 0)
    H = pad * 2 + (r1 - r0 + 1) * cell + (cell * 0.45 if arrows else 0)
    P = []
    centre = {}
    for r in range(r0, r1 + 1):
        for c in range(c0, c1 + 1):
            n = (r - 1) * per + c
            x = pad + (c - c0) * cell; y = pad + (r - r0) * cell
            centre[n] = (x + cell / 2, y + cell / 2)
            fill = '#FFFFFF'
            if n in shade: fill = YEL
            elif n in shade2: fill = MINT
            if n in hide: fill = '#F3F6FB'
            P.append(f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" fill="{fill}" stroke="{NAVY}" stroke-width="1.8"/>')
            fs = cell * (0.30 if n >= 100 else 0.43)
            if n in hide:
                if tags and n in tags:
                    P.append(f'<text x="{x + cell / 2}" y="{y + cell / 2 + cell * 0.15}" font-size="{cell * 0.42}" font-weight="700" text-anchor="middle" fill="#8A94AD" font-family="{FONT}">{tags[n]}</text>')
                elif qmarks:
                    P.append(f'<text x="{x + cell / 2}" y="{y + cell / 2 + cell * 0.15}" font-size="{cell * 0.42}" font-weight="700" text-anchor="middle" fill="#8A94AD" font-family="{FONT}">?</text>')
            elif n in mark:
                P.append(f'<circle cx="{x + cell / 2}" cy="{y + cell / 2}" r="{cell * 0.38}" fill="{RED}" stroke="{NAVY}" stroke-width="2.2"/>')
                P.append(f'<text x="{x + cell / 2}" y="{y + cell / 2 + fs * 0.35}" font-size="{fs}" font-weight="700" text-anchor="middle" fill="#fff" font-family="{FONT}">{n}</text>')
            else:
                P.append(f'<text x="{x + cell / 2}" y="{y + cell / 2 + fs * 0.35}" font-size="{fs}" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="{FONT}">{n}</text>')
    for n in outline:
        if n in centre:
            cx, cy = centre[n]
            P.append(f'<rect x="{cx - cell / 2 + 2}" y="{cy - cell / 2 + 2}" width="{cell - 4}" height="{cell - 4}" fill="none" stroke="{TEAL}" stroke-width="5"/>')
    for (a, b, lab) in arrows:
        if a in centre and b in centre:
            (x1, y1), (x2, y2) = centre[a], centre[b]
            sw = cell * 0.09; hd = cell * 0.22
            if abs(x2 - x1) >= abs(y2 - y1):         # across: arrow along the lower part of the cells, label under the border
                sgn = 1 if x2 > x1 else -1
                ly = y1 + cell * 0.34
                sx, ex = x1 + sgn * cell * 0.10, x2 - sgn * cell * 0.12
                P.append(f'<line x1="{sx:.1f}" y1="{ly:.1f}" x2="{ex - sgn * hd * 0.6:.1f}" y2="{ly:.1f}" stroke="{RED}" stroke-width="{sw:.1f}" stroke-linecap="round"/>')
                P.append(f'<polygon points="{ex:.1f},{ly:.1f} {ex - sgn * hd:.1f},{ly - hd * 0.55:.1f} {ex - sgn * hd:.1f},{ly + hd * 0.55:.1f}" fill="{RED}"/>')
                P.append(f'<text x="{(x1 + x2) / 2:.1f}" y="{y1 + cell * 0.80:.1f}" font-size="{cell * 0.36:.1f}" font-weight="800" text-anchor="middle" fill="{RED}" stroke="#fff" stroke-width="{cell * 0.09:.1f}" paint-order="stroke" font-family="{FONT}">{lab}</text>')
            else:                                      # down or up: arrow along the right side of the cells, label beside it on the border line
                sgn = 1 if y2 > y1 else -1
                lx = x1 + cell * 0.36
                sy, ey = y1 + sgn * cell * 0.12, y2 - sgn * cell * 0.12
                P.append(f'<line x1="{lx:.1f}" y1="{sy:.1f}" x2="{lx:.1f}" y2="{ey - sgn * hd * 0.6:.1f}" stroke="{RED}" stroke-width="{sw:.1f}" stroke-linecap="round"/>')
                P.append(f'<polygon points="{lx:.1f},{ey:.1f} {lx - hd * 0.55:.1f},{ey - sgn * hd:.1f} {lx + hd * 0.55:.1f},{ey - sgn * hd:.1f}" fill="{RED}"/>')
                P.append(f'<text x="{lx + cell * 0.14:.1f}" y="{(y1 + y2) / 2 + cell * 0.13:.1f}" font-size="{cell * 0.36:.1f}" font-weight="800" text-anchor="start" fill="{RED}" stroke="#fff" stroke-width="{cell * 0.09:.1f}" paint-order="stroke" font-family="{FONT}">{lab}</text>')
    cnt = (r1 - r0 + 1) * (c1 - c0 + 1)
    return (f'<svg class="h100" viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="number square, {cnt} squares" '
            f'style="width:100%;height:auto;display:block">{"".join(P)}</svg>')


def seq(items, gaps=None, hl=()):
    """Number tiles in a row; None draws an empty tile; gaps = labels on the arcs between tiles (e.g. '+1')."""
    tw, sp, th = 118, 78, 92
    n = len(items)
    W = 16 + n * tw + (n - 1) * sp
    H = 178
    P = []
    y0 = 80
    for i, v in enumerate(items):
        x = 8 + i * (tw + sp)
        fill = YEL if i in hl else '#FFFFFF'
        dash = ' stroke-dasharray="9 6"' if v is None else ''
        P.append(f'<rect x="{x}" y="{y0}" width="{tw}" height="{th}" rx="16" fill="{fill}" stroke="{NAVY}" stroke-width="3.4"{dash}/>')
        P.append(f'<text x="{x + tw / 2}" y="{y0 + th / 2 + 17}" font-size="52" font-weight="700" text-anchor="middle" fill="{NAVY if v is not None else "#8A94AD"}" font-family="{FONT}">{"?" if v is None else v}</text>')
        if gaps and i < n - 1 and gaps[i] is not None:
            xa, xb = x + tw / 2, x + tw + sp + tw / 2
            P.append(f'<path d="M{xa + 18},{y0} Q{(xa + xb) / 2},{y0 - 62} {xb - 18},{y0 - 2}" fill="none" stroke="{TEAL}" stroke-width="4.2" stroke-linecap="round"/>')
            P.append(f'<polygon points="{xb - 18},{y0 - 1} {xb - 34},{y0 - 6} {xb - 24},{y0 - 20}" fill="{TEAL}"/>')
            P.append(f'<text x="{(xa + xb) / 2}" y="{y0 - 38}" font-size="34" font-weight="800" text-anchor="middle" fill="{TEAL}" font-family="{FONT}">{gaps[i]}</text>')
    return f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="number pattern" style="width:100%;height:auto;display:block">{"".join(P)}</svg>'


def ruler(start=0, end=15, objects=None, mark=None, true_scale=False):
    """A cm ruler strip with big numerals, 0 at the left start. Drawn at TRUE 1:1 scale when true_scale (print: 10 cm = 100 mm).
    objects = [{"label": "pencil", "from": 0, "to": 9, "color": "#FFC93C"}] drawn above the ruler (a `from` other than the 0 mark
    is a shifted start); mark = value of a dashed guide line. Not a cut-out: families use their own ruler (owner decision)."""
    M, R = 7, 6                                   # mm of ruler edge before the 0 mark and after the last mark
    n = end - start
    W = M + n * 10 + R
    objs = objects or []
    oh = 13 * len(objs)                           # mm above the ruler for the objects
    body_y, body_h = oh + 2, 19
    H = body_y + body_h + 2
    u = 10                                        # viewBox units per mm
    x = lambda v: (M + (v - start) * 10) * u
    p = [f'<rect x="0" y="{body_y * u}" width="{W * u}" height="{body_h * u}" rx="14" fill="#FFF3C4" stroke="{NAVY}" stroke-width="12"/>']
    for k in range(0, n * 10 + 1):
        v = start + k / 10
        tall = 7 if k % 10 == 0 else (5 if k % 5 == 0 else 3)
        p.append(f'<line x1="{x(v):.1f}" y1="{body_y * u}" x2="{x(v):.1f}" y2="{(body_y + tall) * u}" stroke="{NAVY}" stroke-width="{10 if k % 10 == 0 else 6}"/>')
    for c in range(start, end + 1):
        p.append(f'<text x="{x(c):.1f}" y="{(body_y + 16) * u}" font-size="62" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="{FONT}">{c}</text>')
    for i, o in enumerate(objs):
        y0 = (1 + i * 13) * u
        p.append(f'<rect x="{x(o["from"]):.1f}" y="{y0}" width="{(o["to"] - o["from"]) * 10 * u:.1f}" height="{9 * u}" rx="20" fill="{o.get("color", YEL)}" stroke="{NAVY}" stroke-width="10"/>')
        if o.get('label'):
            p.append(f'<text x="{(x(o["from"]) + x(o["to"])) / 2:.1f}" y="{y0 + 6.3 * u:.1f}" font-size="52" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="{FONT}">{o["label"]}</text>')
    if mark is not None:
        p.append(f'<line x1="{x(mark):.1f}" y1="0" x2="{x(mark):.1f}" y2="{(body_y + body_h) * u}" stroke="{RED}" stroke-width="8" stroke-dasharray="30 20"/>')
    size = f'width:{W}mm;height:{H}mm;max-width:none;' if true_scale else 'width:100%;height:auto;'
    return (f'<svg viewBox="0 0 {W * u} {H * u}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="centimetre ruler from {start} to {end}" data-mm="{W}" '
            f'style="{size}display:block">{"".join(p)}</svg>')


def render_visual(v):
    t = v['type']
    if t == 'bundles':
        return bundles(v['tens'], v['ones'], None, v.get('style', 'sticks'))
    if t == 'scatter':
        return scatter(v['n'], v.get('seed', 1))
    if t == 'ten_frame':
        return ten_frame(v['filled'], v.get('extra', 0))
    if t == 'number_line':
        return number_line(**{k: (([tuple(j) for j in x]) if k == 'jumps' else x) for k, x in v.items() if k in ('start', 'end', 'step', 'label_every', 'marks', 'hide', 'jumps', 'highlight', 'width', 'big')})
    if t == 'hundred_square':
        return hundred_square(v.get('blank', False))
    if t == 'ruler':
        return ruler(v.get('start', 0), v.get('end', 15), v.get('objects'), v.get('mark'))
    if t == 'hundred':
        kw = {k: v[k] for k in ('shade', 'shade2', 'hide', 'mark', 'outline', 'arrows', 'rows', 'cols', 'per', 'cell', 'qmarks', 'tags') if k in v}
        if 'tags' in kw: kw['tags'] = {int(a): b for a, b in kw['tags'].items()}
        if 'arrows' in kw: kw['arrows'] = [tuple(a) for a in kw['arrows']]
        if 'rows' in kw: kw['rows'] = tuple(kw['rows'])
        if 'cols' in kw: kw['cols'] = tuple(kw['cols'])
        out = hundred(**kw)
        return out.replace('class="h100"', 'class="h100 wide"') if v.get('wide') else out
    if t == 'seq':
        return seq(v['items'], v.get('gaps'), v.get('hl', ()))
    if t == 'ten_to_bundle':
        return ten_to_bundle()
    raise ValueError('unknown visual ' + t)


def place_table(tens, ones, big=False, blank=False):
    cls = 'pv big' if big else 'pv'
    t = '' if blank else tens
    o = '' if blank else ones
    return f'<table class="{cls}"><tr><th>Tens</th><th>Ones</th></tr><tr><td>{t}</td><td>{o}</td></tr></table>'


def kit_page_svg():
    """Cut-out sheet: 9 tens bars + 20 ones squares (A4 width)."""
    sq = 62
    parts = []
    y = 40
    parts.append(f'<text x="0" y="22" font-size="22" font-weight="800" fill="{NAVY}" font-family="Nunito Sans, Arial">Tens bars: cut out all 9 (each bar is one ten)</text>')
    for _ in range(9):
        for i in range(10):
            parts.append(f'<rect x="{i * sq + 2}" y="{y}" width="{sq}" height="{sq - 8}" fill="{SKY}" stroke="{NAVY}" stroke-width="2"/>')
        parts.append(f'<rect x="0" y="{y - 3}" width="{10 * sq + 4}" height="{sq - 2}" fill="none" stroke="#777" stroke-width="1.6" stroke-dasharray="7 5"/>')
        y += sq + 6
    y += 22
    parts.append(f'<text x="0" y="{y}" font-size="22" font-weight="800" fill="{NAVY}" font-family="Nunito Sans, Arial">Ones squares: cut out all 20 (each square is one one)</text>')
    y += 16
    for k in range(20):
        x = (k % 10) * sq + 2
        yy = y + (k // 10) * (sq + 4)
        parts.append(f'<rect x="{x}" y="{yy}" width="{sq - 6}" height="{sq - 6}" fill="{SOFT}" stroke="#777" stroke-width="1.6" stroke-dasharray="7 5"/>')
    y += 2 * (sq + 4) + 6
    return f'<svg viewBox="0 0 {10 * sq + 8} {y}" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;display:block">{"".join(parts)}</svg>'
