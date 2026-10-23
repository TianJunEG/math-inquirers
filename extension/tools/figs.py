"""Figure renderer for the extension workbooks.

A figure spec is a small dict stored in the unit JSON ({"type": "tiles", ...}).  render(spec, theme) returns an inline
<svg> string.  theme is 'colour' (soft copy) or 'bw' (print).  Everything is drawn with the project palette (as in
term/l1/tools/svg.py, which is reused for tiles / number line / ten frame); the B&W theme is produced by recolour():
dark inks -> black, light tints -> white, mid fills -> a hatch pattern, so no meaning is carried by colour.
"""
import os, re, sys, itertools

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, 'term', 'l1', 'tools'))
import svg as legacy   # noqa: E402  (term/l1/tools/svg.py)

NAVY, TEAL, YEL, SKY, SOFT, RED, GREY = legacy.NAVY, legacy.TEAL, legacy.YEL, legacy.SKY, legacy.SOFT, legacy.RED, legacy.GREY
FONT = legacy.FONT
_ids = itertools.count(1)


def recolour(s):
    """Colour svg -> black and white svg (patterns instead of colour)."""
    n = next(_ids)
    pid = f'ht{n}'
    s = re.sub(r'(<circle[^>]*?)fill="' + YEL + '"', r'\1fill="#000"', s)   # small dots: solid
    s = s.replace(f'fill="{YEL}"', f'fill="url(#{pid})"')
    for c in (SKY, SOFT):
        s = s.replace(f'fill="{c}"', 'fill="#fff"')
    for c in (NAVY, TEAL, RED, GREY):
        s = s.replace(c, '#000')
    s = s.replace('#D64545', '#000')
    pat = (f'<defs><pattern id="{pid}" width="9" height="9" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
           f'<rect width="9" height="9" fill="#fff"/><rect width="2.2" height="9" fill="#000"/></pattern></defs>')
    return re.sub(r'(<svg[^>]*>)', lambda m: m.group(1) + pat, s, count=1)


def _wrap(inner, vb_w, vb_h, label, width_mm=None):
    st = 'display:block;height:auto;' + (f'width:{width_mm}mm' if width_mm else 'width:100%')
    return f'<svg viewBox="0 0 {vb_w} {vb_h}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{label}" style="{st}">{inner}</svg>'


def _t(x, y, txt, size=34, fill=NAVY, anchor='middle', weight=700):
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" fill="{fill}" font-family="{FONT}">{txt}</text>'


def numstrip(start, end, per_row=16, circle=(), width_mm=None):
    """Rows of numbered boxes (a number strip). `circle` numbers are drawn with a thick ring (shown in the worked example)."""
    cw, ch = 62, 62
    nums = list(range(start, end + 1))
    rows = [nums[i:i + per_row] for i in range(0, len(nums), per_row)]
    parts = []
    for r, row in enumerate(rows):
        for c, v in enumerate(row):
            x, y = 4 + c * cw, 4 + r * (ch + 10)
            parts.append(f'<rect x="{x}" y="{y}" width="{cw}" height="{ch}" fill="#fff" stroke="{NAVY}" stroke-width="2.6"/>')
            parts.append(_t(x + cw / 2, y + 42, v, 30))
            if v in circle:
                parts.append(f'<circle cx="{x + cw / 2}" cy="{y + ch / 2}" r="28" fill="none" stroke="{NAVY}" stroke-width="4.5"/>')
    W = per_row * cw + 8
    H = len(rows) * (ch + 10) + 2
    return _wrap(''.join(parts), W, H, f'number strip {start} to {end}', width_mm)


def dot_boxes(counts, labels=None, shape='square', width_mm=None):
    """Boxes of small squares (blocks) or dots, one box per step, for growing-pattern pictures."""
    bw, gap = 150, 40
    parts = []
    for i, n in enumerate(counts):
        x0 = 6 + i * (bw + gap)
        parts.append(f'<rect x="{x0}" y="6" width="{bw}" height="150" rx="10" fill="#fff" stroke="{NAVY}" stroke-width="3"/>')
        cols = 3
        for k in range(n):
            r, c = divmod(k, cols)
            cx, cy = x0 + 28 + c * 42, 30 + r * 42
            if shape == 'square':
                parts.append(f'<rect x="{cx - 15}" y="{cy - 15}" width="30" height="30" fill="{YEL}" stroke="{NAVY}" stroke-width="2.6"/>')
            else:
                parts.append(f'<circle cx="{cx}" cy="{cy}" r="15" fill="{YEL}" stroke="{NAVY}" stroke-width="2.6"/>')
        parts.append(_t(x0 + bw / 2, 196, (labels[i] if labels else f'Step {i + 1}'), 30))
    W = len(counts) * (bw + gap) - gap + 12
    return _wrap(''.join(parts), W, 212, 'growing pattern boxes', width_mm)


def tri_dots(counts, width_mm=None):
    """Triangles of dots (1, 3, 6, 10 ...): counts must be triangular numbers; the last may be None (draw nothing, ask)."""
    parts = []
    x0 = 10
    sp = 34
    maxrows = 0
    for n in counts:
        if n is None:
            continue
        r = 1
        while r * (r + 1) // 2 < n:
            r += 1
        maxrows = max(maxrows, r)
    base_y = 20 + maxrows * sp
    for n in counts:
        if n is None:
            continue
        rows = 1
        while rows * (rows + 1) // 2 < n:
            rows += 1
        w = rows * sp
        W = max(w, 110)
        for r in range(rows):
            for c in range(r + 1):
                cx = x0 + W / 2 + (c - r / 2) * sp
                cy = 24 + r * sp
                parts.append(f'<circle cx="{cx:.1f}" cy="{cy}" r="11" fill="{YEL}" stroke="{NAVY}" stroke-width="2.4"/>')
        parts.append(_t(x0 + W / 2, base_y + 26, f'Triangle {counts.index(n) + 1}', 24))
        x0 += W + 50
    return _wrap(''.join(parts), x0, base_y + 40, 'triangles of dots', width_mm)


def bonds(items, width_mm=None):
    """Part-whole diagrams: a whole circle on top, two part circles below. None = empty box to fill in."""
    parts = []
    for i, d in enumerate(items):
        ox = 10 + i * 270
        def node(x, y, v, r=44):
            if v is None:
                return f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff" stroke="{NAVY}" stroke-width="3.4" stroke-dasharray="9 6"/>'
            return f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff" stroke="{NAVY}" stroke-width="3.4"/>' + _t(x, y + 13, v, 40)
        parts.append(f'<line x1="{ox + 110}" y1="86" x2="{ox + 50}" y2="130" stroke="{NAVY}" stroke-width="3.4"/>')
        parts.append(f'<line x1="{ox + 110}" y1="86" x2="{ox + 170}" y2="130" stroke="{NAVY}" stroke-width="3.4"/>')
        parts.append(node(ox + 110, 50, d['whole']))
        parts.append(node(ox + 50, 170, d['a']))
        parts.append(node(ox + 170, 170, d['b']))
        parts.append(_t(ox + 110, 244, d.get('label', ''), 24))
    W = 10 + len(items) * 270
    return _wrap(''.join(parts), W, 256, 'number bond diagrams', width_mm)


def tiles(items, gaps=None, hl=(), width_mm=None):
    s = legacy.seq(items, gaps, hl)
    return re.sub(r'<text[^>]*>\?</text>', '', s)   # empty tiles stay empty: the child writes the number


def ten_frame(filled, extra=0, width_mm=None):
    return legacy.ten_frame(filled, extra)


def number_line(**kw):
    kw.pop('width_mm', None)
    return legacy.number_line(**kw)


def _plugin_figs():
    """Figure types added by the unit authors: every tools/figs_*.py that defines FIGS = {type: fn(spec, width_mm) -> svg}."""
    import glob, importlib
    out = {}
    for f in sorted(glob.glob(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'figs_*.py'))):
        m = importlib.import_module(os.path.basename(f)[:-3])
        out.update(getattr(m, 'FIGS', {}))
    return out


def render(spec, theme='colour'):
    t = spec['type']
    w = spec.get('width_mm')
    if t == 'tiles':
        w = w or 150
        s = tiles(spec['items'], spec.get('gaps'), spec.get('hl', ()), w)
    elif t == 'numstrip':
        s = numstrip(spec['start'], spec['end'], spec.get('per_row', 16), tuple(spec.get('circle', ())), w)
    elif t == 'dot_boxes':
        s = dot_boxes(spec['counts'], spec.get('labels'), spec.get('shape', 'square'), w)
    elif t == 'tri_dots':
        s = tri_dots(spec['counts'], w)
    elif t == 'bonds':
        s = bonds(spec['items'], w)
    elif t == 'ten_frame':
        s = ten_frame(spec['filled'], spec.get('extra', 0), w)
    elif t == 'number_line':
        s = number_line(**{k: v for k, v in spec.items() if k != 'type'})
    elif t in _plugin_figs():
        s = _plugin_figs()[t](spec, w)
    else:
        raise ValueError('unknown figure type ' + t)
    if w and 'width:' not in s.split('style="', 1)[1].split('"')[0]:
        s = s.replace('style="width:100%', f'style="width:{w}mm', 1)
    if w:
        s = re.sub(r'style="width:100%;', f'style="width:{w}mm;', s, count=1)
    return recolour(s) if theme == 'bw' else s
