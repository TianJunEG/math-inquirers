"""Term 2 figure engine: object icons, objects, groups, arrays, line_up, round_table, bar_model, table, picture_equation,
two-colour ten-frame, dominoes, kit pages (groups mat, unit strips, array mat, people strip).

Every function returns an inline <svg> string that scales to its container (width:100%), flat palette, navy outline.
Answer boxes inside figures: a text token '[]' draws an empty rounded box, '()' an empty circle, '[ ]' a tick box.
Registered with svg.render_visual at import time (see the bottom of svg.py).
"""
import math, re

NAVY = '#1B2A49'; TEAL = '#1F7A6F'; YEL = '#FFC93C'; SKY = '#DDEBF7'; SOFT = '#FFF0C2'; RED = '#D64545'; MINT = '#BFE3DC'
FONT = "Fredoka, 'Nunito Sans', Arial, sans-serif"
CHILD_COLOURS = ['#D64545', '#3B6FC9', '#3DBE7A', '#F28C38', '#7B4FB5', '#1F7A6F']
SKIN = '#F6C9A0'
SW = 2.4


def _o(fill, extra=''):
    return f'fill="{fill}" stroke="{NAVY}" stroke-width="{SW}" stroke-linejoin="round" {extra}'


# ------------------------------------------------------------------ icons (64 x 64 box)

def _icon_body(name):
    n = name
    if n.startswith('child'):
        k = int(n[5:] or 1) - 1
        c = CHILD_COLOURS[k % 6]
        return (f'<rect x="19" y="32" width="26" height="22" rx="8" {_o(c)}/><circle cx="32" cy="19" r="11" {_o(SKIN)}/>'
                f'<line x1="26" y1="54" x2="25" y2="62" stroke="{NAVY}" stroke-width="3.4" stroke-linecap="round"/><line x1="38" y1="54" x2="39" y2="62" stroke="{NAVY}" stroke-width="3.4" stroke-linecap="round"/>'
                f'<circle cx="28.5" cy="18" r="1.6" fill="{NAVY}"/><circle cx="35.5" cy="18" r="1.6" fill="{NAVY}"/>')
    if n == 'apple':
        return (f'<path d="M32 18 C20 10 6 20 8 38 C10 54 22 60 32 56 C42 60 54 54 56 38 C58 20 44 10 32 18 Z" {_o("#E4572E")}/>'
                f'<path d="M32 18 C32 12 34 8 38 6" fill="none" stroke="{NAVY}" stroke-width="3" stroke-linecap="round"/><path d="M36 12 C42 6 50 8 52 10 C48 16 40 16 36 12 Z" {_o("#3DBE7A")}/>')
    if n == 'cookie':
        return (f'<circle cx="32" cy="32" r="25" {_o("#E8B66F")}/>' + ''.join(f'<circle cx="{x}" cy="{y}" r="3.4" fill="#6B4226"/>' for x, y in ((22, 22), (40, 24), (30, 36), (44, 40), (20, 44), (34, 48))))
    if n == 'sweet':
        return (f'<polygon points="2,18 18,32 2,46" {_o("#FF8FB1")}/><polygon points="62,18 46,32 62,46" {_o("#FF8FB1")}/><ellipse cx="32" cy="32" rx="19" ry="15" {_o("#FF5C8A")}/>'
                f'<path d="M22 28 C28 22 36 22 42 28" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round"/>')
    if n == 'sticker':
        pts = ' '.join(f'{32 + (26 if i % 2 == 0 else 11) * math.sin(i * math.pi / 5):.1f},{33 - (26 if i % 2 == 0 else 11) * math.cos(i * math.pi / 5):.1f}' for i in range(10))
        return f'<polygon points="{pts}" {_o(YEL)}/>'
    if n == 'ball':        # a tennis ball: yellow-green with two curved seams (not a globe: no blue, no meridians or equator)
        return (f'<circle cx="32" cy="32" r="25" {_o("#C9E04A")}/><path d="M11 17 C26 25 26 39 11 47" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round"/>'
                f'<path d="M53 17 C38 25 38 39 53 47" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round"/><circle cx="32" cy="32" r="25" fill="none" stroke="{NAVY}" stroke-width="{SW}"/>')
    if n == 'marble':
        return f'<circle cx="32" cy="32" r="24" {_o("#7B4FB5")}/><path d="M20 24 C22 18 28 15 33 16" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round"/>'
    if n == 'pencil':
        return (f'<polygon points="6,50 14,42 54,10 58,14 26,54 10,58" {_o("#FFC93C")} transform="rotate(0)"/>' if False else
                f'<g transform="rotate(-45 32 32)"><rect x="6" y="25" width="40" height="14" {_o(YEL)}/><polygon points="46,25 60,32 46,39" {_o(SKIN)}/><polygon points="55,29.5 60,32 55,34.5" fill="{NAVY}"/><rect x="2" y="25" width="7" height="14" {_o("#F28C9C")}/></g>')
    if n == 'pen':
        return (f'<g transform="rotate(-45 32 32)"><rect x="8" y="27" width="40" height="10" rx="3" {_o("#3B6FC9")}/><rect x="2" y="27" width="10" height="10" rx="3" {_o("#fff")}/><polygon points="48,27 58,32 48,37" {_o("#BFD0EE")}/></g>')
    if n == 'book':
        return (f'<rect x="10" y="8" width="44" height="48" rx="4" {_o("#3B6FC9")}/><rect x="16" y="8" width="38" height="48" rx="3" {_o("#fff")}/><line x1="22" y1="22" x2="48" y2="22" stroke="{NAVY}" stroke-width="2.4"/><line x1="22" y1="32" x2="48" y2="32" stroke="{NAVY}" stroke-width="2.4"/><line x1="22" y1="42" x2="40" y2="42" stroke="{NAVY}" stroke-width="2.4"/>')
    if n == 'cup':
        return (f'<path d="M12 14 H44 L40 52 C40 56 36 58 32 58 H24 C20 58 16 56 16 52 Z" {_o("#fff")}/><path d="M44 22 C58 22 58 42 42 42" fill="none" stroke="{NAVY}" stroke-width="{SW}"/><path d="M14 24 H42" stroke="{TEAL}" stroke-width="5"/>')
    if n == 'plate':
        return f'<ellipse cx="32" cy="34" rx="29" ry="22" {_o("#fff")}/><ellipse cx="32" cy="34" rx="18" ry="12" fill="none" stroke="#B9C7DA" stroke-width="2.4"/>'
    if n == 'bag':
        return (f'<path d="M12 22 H52 L56 58 H8 Z" {_o("#E8B66F")}/><path d="M22 22 C22 6 42 6 42 22" fill="none" stroke="{NAVY}" stroke-width="{SW}"/>')
    if n == 'jar':
        return (f'<rect x="14" y="6" width="36" height="9" rx="3" {_o(TEAL)}/><path d="M16 15 H48 C54 20 54 30 54 36 V52 C54 57 50 60 46 60 H18 C14 60 10 57 10 52 V36 C10 30 10 20 16 15 Z" {_o("#EAF6FB")}/>')
    if n == 'flower':
        pet = ''.join(f'<circle cx="{32 + 14 * math.cos(a * math.pi / 3):.1f}" cy="{30 + 14 * math.sin(a * math.pi / 3):.1f}" r="9" {_o("#FF8FB1")}/>' for a in range(6))
        return f'<line x1="32" y1="40" x2="32" y2="62" stroke="#2F9E5B" stroke-width="4"/>{pet}<circle cx="32" cy="30" r="8" {_o(YEL)}/>'
    if n == 'fish':
        return (f'<polygon points="46,32 62,18 62,46" {_o("#F28C38")}/><ellipse cx="28" cy="32" rx="24" ry="16" {_o("#F28C38")}/><circle cx="17" cy="28" r="3.2" fill="{NAVY}"/>')
    if n == 'bird':
        return (f'<circle cx="30" cy="34" r="20" {_o("#5BA4E6")}/><polygon points="48,28 62,33 48,38" {_o(YEL)}/><circle cx="38" cy="28" r="3" fill="{NAVY}"/><path d="M14 36 C20 48 32 48 36 40 C28 40 20 38 14 36 Z" {_o("#3B6FC9")}/>')
    if n == 'spider':
        legs = ''.join(f'<path d="M32 32 Q{32 + s * 18} {32 + dy - 14} {32 + s * 28} {32 + dy}" fill="none" stroke="{NAVY}" stroke-width="2.4" stroke-linecap="round"/>' for s in (-1, 1) for dy in (-16, -5, 6, 17))
        return f'{legs}<circle cx="32" cy="34" r="12" {_o("#6B4226")}/><circle cx="32" cy="22" r="7" {_o("#6B4226")}/>'
    if n == 'ladybird':
        return (f'<circle cx="32" cy="36" r="22" {_o(RED)}/><path d="M32 14 V58" stroke="{NAVY}" stroke-width="2.4"/><circle cx="32" cy="14" r="8" {_o(NAVY)}/>' + ''.join(f'<circle cx="{x}" cy="{y}" r="3.6" fill="{NAVY}"/>' for x, y in ((22, 30), (42, 30), (20, 44), (44, 44))))
    if n == 'bike':
        return (f'<circle cx="14" cy="44" r="12" fill="none" stroke="{NAVY}" stroke-width="3.2"/><circle cx="50" cy="44" r="12" fill="none" stroke="{NAVY}" stroke-width="3.2"/><path d="M14 44 L28 24 H44 L50 44 M28 24 L34 44 H14 M44 24 L40 16 H48" fill="none" stroke="{TEAL}" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"/>')
    if n == 'car':
        return (f'<path d="M4 40 L10 28 C12 24 16 22 20 22 H40 C46 22 48 26 52 32 L60 36 V46 H4 Z" {_o("#D64545")}/><path d="M16 28 H28 V36 H12 Z M32 28 H42 L48 36 H32 Z" fill="#DDEBF7" stroke="{NAVY}" stroke-width="2"/><circle cx="18" cy="48" r="7" {_o(NAVY)}/><circle cx="48" cy="48" r="7" {_o(NAVY)}/>')
    if n == 'counter' or n == 'counter_red':
        return f'<circle cx="32" cy="32" r="24" {_o(RED)}/>'
    if n == 'counter_yellow':
        return f'<circle cx="32" cy="32" r="24" {_o(YEL)}/>'
    if n == 'coin':
        return f'<circle cx="32" cy="32" r="25" {_o("#EBD98A")}/><circle cx="32" cy="32" r="19" fill="none" stroke="#9A8A3A" stroke-width="2"/><text x="32" y="40" font-size="22" font-weight="800" text-anchor="middle" fill="{NAVY}" font-family="{FONT}">$1</text>'
    if n == 'dot':
        return f'<circle cx="32" cy="32" r="22" {_o(NAVY)}/>'
    if n == 'square':
        return f'<rect x="8" y="8" width="48" height="48" rx="4" {_o(SKY)}/>'
    import figs3
    return figs3.icon_body(name)


ICON_NAMES = ['child1', 'child2', 'child3', 'child4', 'child5', 'child6', 'apple', 'cookie', 'sweet', 'sticker', 'ball', 'marble', 'pencil', 'pen', 'book', 'cup', 'plate',
              'bag', 'jar', 'flower', 'fish', 'bird', 'spider', 'ladybird', 'bike', 'car', 'counter', 'counter_red', 'counter_yellow', 'coin', 'dot', 'square']


def icon(name, cx, cy, size):
    s = size / 64.0
    return f'<g transform="translate({cx - size / 2:.1f},{cy - size / 2:.1f}) scale({s:.4f})">{_icon_body(name)}</g>'


# ------------------------------------------------------------------ tokens in figure text

def token_svg(tok, x, y, w, h, size=34, anchor='middle'):
    """Draw a cell token centred at (x, y): '[]' box, '()' circle, '[ ]' tick box, else text."""
    t = str(tok)
    if t == '[]':
        bw = min(w - 6, 72); bh = min(h - 6, 58)
        return f'<rect x="{x - bw / 2:.1f}" y="{y - bh / 2:.1f}" width="{bw:.1f}" height="{bh:.1f}" rx="8" fill="#fff" stroke="{NAVY}" stroke-width="3"/>'
    if t == '()':
        r = min(w, h) / 2 - 6
        return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="#fff" stroke="{NAVY}" stroke-width="3"/>'
    if t == '[ ]':
        return f'<rect x="{x - 16:.1f}" y="{y - 16:.1f}" width="32" height="32" rx="5" fill="#fff" stroke="{NAVY}" stroke-width="3"/>'
    m = re.fullmatch(r'\[(\d)\]', t)
    if m:
        k = int(m.group(1)); bw = 44
        x0 = x - (k * bw + (k - 1) * 3) / 2
        return ''.join(f'<rect x="{x0 + i * (bw + 3):.1f}" y="{y - 22:.1f}" width="{bw}" height="44" rx="6" fill="#fff" stroke="{NAVY}" stroke-width="3"/>' for i in range(k))
    return f'<text x="{x:.1f}" y="{y + size * 0.35:.1f}" font-size="{size}" font-weight="700" text-anchor="{anchor}" fill="{NAVY}" font-family="{FONT}">{_esc(t)}</text>'


def _esc(s):
    return str(s).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def _svg(w, h, body, label):
    return f'<svg viewBox="0 0 {w:.0f} {h:.0f}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{_esc(label)}" style="width:100%;height:auto;display:block">{body}</svg>'


# ------------------------------------------------------------------ objects, groups, array

def objects(icon_name=None, n=0, per_row=5, size='m', cross=(), hide=(), label=None, items=None, cell=None):
    """Rows of icons. items=[{"icon":"pen","n":4},...] draws mixed rows (one row per item)."""
    cs = cell or {'s': 50, 'm': 64, 'l': 80}.get(size, 64)
    rows = []
    if items:
        for it in items: rows.append((it['icon'], it['n']))
    else:
        rows.append((icon_name, n))
    body = []; y = cs / 2 + 4; maxw = 0
    k = 0
    for (ic, cnt) in rows:
        pr = per_row
        r = 0
        for i in range(cnt):
            rr, cc = divmod(i, pr)
            cx = 8 + cs / 2 + cc * cs; cy = y + rr * cs
            idx = k + i + 1
            if idx in hide:
                body.append(f'<rect x="{cx - cs * 0.38:.1f}" y="{cy - cs * 0.38:.1f}" width="{cs * 0.76:.1f}" height="{cs * 0.76:.1f}" rx="8" fill="#fff" stroke="{NAVY}" stroke-width="2.6" stroke-dasharray="7 5"/>')
            else:
                body.append(icon(ic, cx, cy, cs * 0.84))
            if idx in cross:
                body.append(f'<line x1="{cx - cs * 0.4:.1f}" y1="{cy - cs * 0.4:.1f}" x2="{cx + cs * 0.4:.1f}" y2="{cy + cs * 0.4:.1f}" stroke="{RED}" stroke-width="5" stroke-linecap="round"/><line x1="{cx + cs * 0.4:.1f}" y1="{cy - cs * 0.4:.1f}" x2="{cx - cs * 0.4:.1f}" y2="{cy + cs * 0.4:.1f}" stroke="{RED}" stroke-width="5" stroke-linecap="round"/>')
        nrows = (cnt + pr - 1) // pr
        maxw = max(maxw, min(cnt, pr) * cs)
        y += nrows * cs + (cs * 0.15 if items else 0)
        k += cnt
    H = y - cs / 2 + (34 if label else 6)
    if label: body.append(f'<text x="{(maxw + 16) / 2:.1f}" y="{H - 8:.1f}" font-size="28" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="{FONT}">{_esc(label)}</text>')
    return _svg(maxw + 16, H, ''.join(body), f'{sum(c for _, c in rows)} objects')


def _container(kind, x, y, w, h):
    if kind == 'plate':
        return f'<ellipse cx="{x + w / 2:.1f}" cy="{y + h / 2:.1f}" rx="{w / 2:.1f}" ry="{h / 2:.1f}" {_o("#fff")}/><ellipse cx="{x + w / 2:.1f}" cy="{y + h / 2:.1f}" rx="{w * 0.36:.1f}" ry="{h * 0.34:.1f}" fill="none" stroke="#B9C7DA" stroke-width="2.4"/>'
    if kind == 'bag':
        return f'<path d="M{x + w * 0.1:.1f} {y + h * 0.18:.1f} H{x + w * 0.9:.1f} L{x + w:.1f} {y + h:.1f} H{x:.1f} Z" {_o("#F1D9AE")}/><path d="M{x + w * 0.3:.1f} {y + h * 0.18:.1f} C{x + w * 0.3:.1f} {y - h * 0.12:.1f} {x + w * 0.7:.1f} {y - h * 0.12:.1f} {x + w * 0.7:.1f} {y + h * 0.18:.1f}" fill="none" stroke="{NAVY}" stroke-width="{SW}"/>'
    if kind == 'box':
        return f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="6" {_o("#F1D9AE")}/>'
    if kind == 'jar':
        return f'<rect x="{x + w * 0.15:.1f}" y="{y:.1f}" width="{w * 0.7:.1f}" height="{h * 0.12:.1f}" rx="3" {_o(TEAL)}/><rect x="{x:.1f}" y="{y + h * 0.12:.1f}" width="{w:.1f}" height="{h * 0.88:.1f}" rx="14" {_o("#EAF6FB")}/>'
    if kind == 'cup':
        return f'<path d="M{x:.1f} {y:.1f} H{x + w:.1f} L{x + w * 0.85:.1f} {y + h:.1f} H{x + w * 0.15:.1f} Z" {_o("#fff")}/>'
    raise ValueError('unknown container ' + kind)


def groups(container='plate', n=3, each=3, icon_name='apple', counts=None, empty=False, label_each=None, total=None, per_row=4):
    """n containers each holding `each` items (or `counts` for unequal groups). empty=True draws blank containers to draw in."""
    cnts = list(counts) if counts else [each] * n
    n = len(cnts)
    cw, ch = 210, 160 if container != 'plate' else 130
    gap = 18
    body = []
    rows = (n + per_row - 1) // per_row
    for g, cnt in enumerate(cnts):
        r, c = divmod(g, per_row)
        x = 10 + c * (cw + gap); y = 10 + r * (ch + 56 + gap)
        body.append(_container(container, x, y, cw, ch))
        if not empty:
            isz = 42 if cnt <= 6 else 32
            cols = 3 if cnt <= 6 else 4
            rws = (cnt + cols - 1) // cols
            for i in range(cnt):
                ri, ci = divmod(i, cols)
                inrow = cols if ri < rws - 1 or cnt % cols == 0 else cnt % cols
                ix = x + cw / 2 - (inrow - 1) * (isz + 4) / 2 + ci * (isz + 4)
                iy = y + ch / 2 + (ri - (rws - 1) / 2) * (isz + 4) + (6 if container in ('bag', 'cup') else 0)
                body.append(icon(icon_name, ix, iy, isz))
        if label_each:
            body.append(token_svg(label_each, x + cw / 2, y + ch + 26, cw, 44, 30))
    W = 20 + min(n, per_row) * (cw + gap) - gap
    H = 20 + rows * (ch + 56 + gap) - gap + (62 if total else 0)
    if total is not None:
        body.append(f'<text x="14" y="{H - 14:.0f}" font-size="30" font-weight="800" fill="{NAVY}" font-family="{FONT}">Total: </text>')
        body.append(token_svg(total, 150, H - 24, 80, 50, 38))
    return _svg(W, H, ''.join(body), f'{n} {container}s')


def array(rows=3, cols=4, icon_name='dot', hide=(), shade_rows=(), pairs=False, ring_left_over=False, row_label=None, col_label=None, cell=48):
    """rows x cols grid of dots, squares or icons. pairs=True draws counters two by two (rows=1, cols=n) and rings the left-over one."""
    body = []
    n = rows * cols
    if pairs:
        cnt = cols
        for i in range(cnt):
            pr, pos = divmod(i, 2)
            cx = 30 + (i % 8 // 2) * (cell * 2 + 20) + (i % 2) * cell
            cy = 30 + (i // 8) * (cell + 26)
            body.append(icon(icon_name, cx, cy, cell * 0.8))
        # pair outlines
        for p in range(cnt // 2):
            cx0 = 30 + (p % 4) * (cell * 2 + 20) - cell * 0.5; cy0 = 30 + (p // 4) * (cell + 26)
            body.append(f'<rect x="{cx0 - 2:.1f}" y="{cy0 - cell * 0.46:.1f}" width="{cell * 2 + 4:.1f}" height="{cell * 0.92:.1f}" rx="{cell * 0.4:.1f}" fill="none" stroke="{TEAL}" stroke-width="3"/>')
        if ring_left_over and cnt % 2:
            i = cnt - 1
            cx = 30 + (i % 8 // 2) * (cell * 2 + 20) + (i % 2) * cell; cy = 30 + (i // 8) * (cell + 26)
            body.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{cell * 0.52:.1f}" fill="none" stroke="{RED}" stroke-width="4" stroke-dasharray="8 5"/>')
        W = 60 + min((cnt + 1) // 2, 4) * (cell * 2 + 20)
        H = 30 + ((cnt - 1) // 8 + 1) * (cell + 26)
        return _svg(W, H, ''.join(body), f'{cnt} counters in pairs')
    ox = 52 if row_label else 10; oy = 10
    for r in range(rows):
        for c in range(cols):
            k = r * cols + c + 1
            cx = ox + c * cell + cell / 2; cy = oy + r * cell + cell / 2
            if (r + 1) in shade_rows:
                body.append(f'<rect x="{cx - cell / 2:.1f}" y="{cy - cell / 2:.1f}" width="{cell}" height="{cell}" fill="{SOFT}"/>')
            if k in hide:
                body.append(f'<rect x="{cx - cell * 0.36:.1f}" y="{cy - cell * 0.36:.1f}" width="{cell * 0.72:.1f}" height="{cell * 0.72:.1f}" rx="6" fill="#fff" stroke="{NAVY}" stroke-width="2.6" stroke-dasharray="6 4"/>')
            else:
                body.append(icon(icon_name, cx, cy, cell * 0.78))
    if shade_rows:   # a dark box round the shaded rows, so the cue survives black-and-white printing
        r0, r1 = min(shade_rows), max(shade_rows)
        body.append(f'<rect x="{ox - 3:.1f}" y="{oy + (r0 - 1) * cell - 3:.1f}" width="{cols * cell + 6:.1f}" height="{(r1 - r0 + 1) * cell + 6:.1f}" rx="10" fill="none" stroke="{NAVY}" stroke-width="3.5"/>')
    W = ox + cols * cell + 10 + (60 if col_label and False else 0)
    H = oy + rows * cell + (62 if col_label else 10)
    if row_label: body.append(token_svg(row_label, 24, oy + rows * cell / 2, 44, 52, 28))
    if col_label: body.append(token_svg(col_label, ox + cols * cell / 2, oy + rows * cell + 32, 70, 52, 28))
    return _svg(W, H, ''.join(body), f'array of {rows} rows and {cols} columns')


# ------------------------------------------------------------------ line_up and round_table

def line_up(n=8, names=None, front='left', marker='door', labels='ordinal', highlight=(), between=None, icons=None, cell=84):
    """Children in a line with a labelled front. labels: ordinal | number | box | none. between=[a,b] brackets the places strictly between."""
    names = {int(k): v for k, v in (names or {}).items()}
    W = 30 + n * cell + 100; H = 230
    body = []
    order = list(range(1, n + 1))
    pos = lambda k: 100 + ((k - 1) if front == 'left' else (n - k)) * cell + cell / 2
    # marker at front
    mx = 58 if front == 'left' else W - 58
    if marker == 'door':
        body.append(f'<rect x="{mx - 24:.1f}" y="40" width="48" height="104" rx="4" {_o("#E8B66F")}/><circle cx="{mx + (12 if front == "left" else -12):.1f}" cy="94" r="4" fill="{NAVY}"/>')
    else:
        d = 1 if front == 'left' else -1
        body.append(f'<polygon points="{mx - d * 14:.1f},70 {mx + d * 18:.1f},94 {mx - d * 14:.1f},118" {_o(TEAL)}/>')
    body.append(f'<text x="{mx:.1f}" y="30" font-size="30" font-weight="800" text-anchor="middle" fill="{TEAL}" font-family="{FONT}">FRONT</text>')
    for k in order:
        cx = pos(k)
        ic = (icons or {}).get(str(k)) or f'child{(k - 1) % 6 + 1}'
        if k in set(highlight):
            body.append(f'<ellipse cx="{cx:.1f}" cy="96" rx="{cell * 0.46:.1f}" ry="58" fill="{SOFT}" stroke="{TEAL}" stroke-width="3.4"/>')
        body.append(icon(ic, cx, 96, cell * 0.92))
        lab = ''
        if labels == 'ordinal': lab = _ord(k)
        elif labels == 'number': lab = str(k)
        elif labels == 'box': lab = '[]'
        if lab:
            body.append(token_svg(lab, cx, 172, cell, 62, 36))
        if k in names:
            body.append(f'<text x="{cx:.1f}" y="{26:.0f}" font-size="30" font-weight="800" text-anchor="middle" fill="{NAVY}" font-family="{FONT}">{_esc(names[k])}</text>')
    if between:
        a, b = sorted(between)
        xa, xb = pos(a), pos(b)
        x0, x1 = min(xa, xb), max(xa, xb)
        body.append(f'<path d="M{x0:.1f} 210 V222 H{x1:.1f} V210" fill="none" stroke="{RED}" stroke-width="4"/>')
    return _svg(W, H + 12, ''.join(body), f'{n} children in a line, front on the {front}')


def _ord(k):
    if 10 <= k % 100 <= 20: s = 'th'
    else: s = {1: 'st', 2: 'nd', 3: 'rd'}.get(k % 10, 'th')
    return f'{k}{s}'


def round_table(seats=6, names=None, hide=(), cell=70):
    """Seats around a round table; names={'1':'Ben'}; hide=[4] shows an empty answer box on that seat."""
    names = {int(k): v for k, v in (names or {}).items()}
    R = 120; cx = cy = 190; W = H = 380
    body = [f'<circle cx="{cx}" cy="{cy}" r="{R * 0.62:.1f}" {_o("#F1D9AE")}/>']
    for k in range(1, seats + 1):
        a = -math.pi / 2 + (k - 1) * 2 * math.pi / seats
        x = cx + R * math.cos(a); y = cy + R * math.sin(a)
        if k in hide:
            body.append(token_svg('[]', x, y, cell, cell, 32))
        else:
            body.append(icon(f'child{(k - 1) % 6 + 1}', x, y, cell * 0.9))
        lab = names.get(k, '')
        if lab:
            lx = cx + (R + 52) * math.cos(a); ly = cy + (R + 52) * math.sin(a)
            body.append(f'<text x="{lx:.1f}" y="{ly + 10:.1f}" font-size="32" font-weight="800" text-anchor="middle" fill="{NAVY}" font-family="{FONT}">{_esc(lab)}</text>')
    return _svg(W, H, ''.join(body), f'{seats} seats round a table')


# ------------------------------------------------------------------ bar model

BAR_COL = {'yellow': YEL, 'sky': SKY, 'mint': MINT, 'soft': SOFT, 'white': '#FFFFFF', 'rose': '#F6C9D0'}


def _bar_label(text, cx, cy, w, h, size):
    """A number or word on a coloured bar sits on a white pill, so it stays readable on a dithered fill in black and white."""
    t = str(text)
    if t in ('[]', '()', '[ ]') or t.startswith('['): return token_svg(t, cx, cy, w, h, size)
    bw = min(max(len(t), 1) * size * 0.62 + 22, max(w - 6, 24)); bh = min(h - 12, size + 14)
    return f'<rect x="{cx - bw / 2:.1f}" y="{cy - bh / 2:.1f}" width="{bw:.1f}" height="{bh:.1f}" rx="{bh / 2:.1f}" fill="#fff" stroke="{NAVY}" stroke-width="2"/>' + token_svg(t, cx, cy, w, h, size)


def bar_model(mode='compare', bars=None, brace=None, gap=None, units=None, arrow=None, unit_px=None, name_w=120, bar_h=64, vgap=34):
    """Strips drawn to scale (length proportional to value). bars=[{name,len,segments:[{v,text,colour}],colour}].
    brace={'text':'[]','over':'all'|index}: a bracket over the bars with a label; gap={'between':[0,1],'text':'?'}: dashed guide and
    bracket for the difference; units={'n':4,'text':'5'}: one bar of n equal cells; arrow={'from':0,'to':1,'v':6}: a transfer arrow."""
    bars = bars or []
    name_w = max(name_w, max([len(str(b.get('name', ''))) for b in bars] + [0]) * 22 + 30)
    mx = max([b['len'] for b in bars] + [1])
    ux = unit_px or (860.0 / mx)
    oy = 70 if brace else 24
    body = []
    ys = []
    for i, b in enumerate(bars):
        y = oy + i * (bar_h + vgap); ys.append(y)
        body.append(f'<text x="{name_w - 14}" y="{y + bar_h / 2 + 12:.1f}" font-size="38" font-weight="800" text-anchor="end" fill="{NAVY}" font-family="{FONT}">{_esc(b.get("name", ""))}</text>')
        segs = b.get('segments') or [{'v': b['len'], 'text': b.get('text', '')}]
        x = name_w
        for s in segs:
            w = s['v'] * ux
            col = BAR_COL.get(s.get('colour') or b.get('colour', 'yellow'), YEL)
            body.append(f'<rect x="{x:.1f}" y="{y}" width="{w:.1f}" height="{bar_h}" fill="{col}" stroke="{NAVY}" stroke-width="3.2"/>')
            if s.get('text') not in (None, ''):
                body.append(_bar_label(s['text'], x + w / 2, y + bar_h / 2, w, bar_h, 40))
            x += w
        if units:
            pass
    if units:                                           # equal units: split the (first) bar into n cells
        b = bars[0]; n = units['n']; y = ys[0]; w = b['len'] * ux / n
        for k in range(1, n):
            body.append(f'<line x1="{name_w + k * w:.1f}" y1="{y}" x2="{name_w + k * w:.1f}" y2="{y + bar_h}" stroke="{NAVY}" stroke-width="3.2"/>')
        if units.get('text') not in (None, ''):
            for k in range(n): body.append(_bar_label(units['text'], name_w + k * w + w / 2, y + bar_h / 2, w, bar_h, 38))
    if gap:
        a, c = gap['between']
        xa = name_w + bars[a]['len'] * ux; xc = name_w + bars[c]['len'] * ux
        lo, hi = min(xa, xc), max(xa, xc)
        ya = ys[a] + bar_h; yc = ys[c]
        ytop, ybot = (ya, yc) if ys[a] < ys[c] else (ys[c] + bar_h, ys[a])
        body.append(f'<line x1="{xa:.1f}" y1="{ys[a] + bar_h}" x2="{xa:.1f}" y2="{ys[c]}" stroke="{NAVY}" stroke-width="2.4" stroke-dasharray="8 6"/>' if ys[a] < ys[c] else f'<line x1="{xc:.1f}" y1="{ys[c] + bar_h}" x2="{xc:.1f}" y2="{ys[a]}" stroke="{NAVY}" stroke-width="2.4" stroke-dasharray="8 6"/>')
        body.append(f'<path d="M{lo:.1f} {ys[max(a, c)] + bar_h + 12} V{ys[max(a, c)] + bar_h + 22} H{hi:.1f} V{ys[max(a, c)] + bar_h + 12}" fill="none" stroke="{RED}" stroke-width="4"/>')
        body.append(token_svg(gap.get('text', '?'), (lo + hi) / 2, ys[max(a, c)] + bar_h + 52, max(hi - lo, 60), 50, 40))
    if brace:
        over = brace.get('over', 'all')
        idxs = range(len(bars)) if over == 'all' else [over]
        wmax = max(bars[i]['len'] for i in idxs) * ux
        y0 = ys[min(idxs)] - 14
        body.append(f'<path d="M{name_w} {y0 + 10} V{y0} H{name_w + wmax:.1f} V{y0 + 10}" fill="none" stroke="{TEAL}" stroke-width="4"/>')
        body.append(token_svg(brace.get('text', '?'), name_w + wmax / 2, y0 - 22, wmax, 50, 40))
    if arrow:
        a, c = arrow['from'], arrow['to']
        xs = name_w + bars[a]['len'] * ux - 12; ys0 = ys[a] + bar_h + 4
        xe = name_w + bars[c]['len'] * ux + 14; ye = ys[c] - 6
        mid = (ys0 + ye) / 2
        body.append(f'<path d="M{xs:.1f} {ys0:.1f} C{xs:.1f} {mid:.1f} {xe:.1f} {mid:.1f} {xe:.1f} {ye - 14:.1f}" fill="none" stroke="{RED}" stroke-width="4.5" stroke-linecap="round"/>')
        body.append(f'<polygon points="{xe:.1f},{ye + 2:.1f} {xe - 11:.1f},{ye - 16:.1f} {xe + 11:.1f},{ye - 16:.1f}" fill="{RED}"/>')
        if arrow.get('v') is not None:
            body.append(token_svg(str(arrow['v']), max(xs, xe) + 62, mid, 80, 50, 38))
    W = name_w + mx * ux + (120 if arrow else 40)
    H = oy + len(bars) * (bar_h + vgap) + (50 if gap else 0)
    return _svg(W, H, ''.join(body), 'bar model: ' + ', '.join(f'{b.get("name", "")} {b["len"]}' for b in bars))


# ------------------------------------------------------------------ table

ICON_ROW_H = 112      # table rows that hold pictures (viewBox is 900 wide: an icon of 96 units is about 14 mm on a 137 mm wide table)
ICON_MAX = 96


def table(head=None, rows=None, col_w=None, first_col=None, cell_h=64, font=32, width=900):
    """A drawn table. Cells: text, '[]' answer box, '[2]' linked boxes, '()' circle, '[ ]' tick box, or {"icon":"apple","n":3}."""
    head = head or []
    rows = rows or []
    ncol = len(head) if head else len(rows[0])
    cw = col_w or [1] * ncol
    tot = float(sum(cw))
    xs = [0.0]
    for w in cw: xs.append(xs[-1] + w / tot * width)
    body = []
    y = 4
    allrows = ([('head', head)] if head else []) + [('row', r) for r in rows]
    for kind, r in allrows:
        h = cell_h * (0.85 if kind == 'head' else 1)
        if kind == 'row' and any(isinstance(c, dict) and 'icon' in c for c in r): h = max(h, ICON_ROW_H)     # picture rows are tall enough for icons of about 14 mm on paper
        for c in range(ncol):
            x0, x1 = xs[c] + 4, xs[c + 1] + 4
            fill = YEL if kind == 'head' else ('#F3F6FB' if (c == 0 and first_col == 'label') else '#fff')
            body.append(f'<rect x="{x0:.1f}" y="{y}" width="{x1 - x0:.1f}" height="{h:.1f}" fill="{fill}" stroke="{NAVY}" stroke-width="3"/>')
            cell = r[c] if c < len(r) else ''
            cx, cy = (x0 + x1) / 2, y + h / 2
            if isinstance(cell, dict) and 'icon' in cell:
                n = cell.get('n', 1); sz = min(h - 14, (x1 - x0) / max(n, 1) - 4, ICON_MAX)
                for i in range(n):
                    body.append(icon(cell['icon'], cx - (n - 1) * (sz + 4) / 2 + i * (sz + 4), cy, sz))
            else:
                body.append(token_svg(cell, cx, cy, x1 - x0, h, font - (4 if kind == 'head' else 0), 'middle'))
        y += h
    return _svg(width + 8, y + 6, ''.join(body), 'table')


# ------------------------------------------------------------------ picture equation (symbols that read in grey print)

def _sym(kind, x, y, s=44):
    a = s / 2
    pat = f'<line x1="{x - a}" y1="{y}" x2="{x + a}" y2="{y}" stroke="{NAVY}" stroke-width="2" opacity="0"/>'
    if kind == 'circle':
        return f'<circle cx="{x}" cy="{y}" r="{a}" fill="#F6C9D0" stroke="{NAVY}" stroke-width="3"/><circle cx="{x}" cy="{y}" r="{a * 0.4}" fill="{NAVY}"/>'
    if kind == 'square':
        return f'<rect x="{x - a}" y="{y - a}" width="{s}" height="{s}" fill="#BFE3DC" stroke="{NAVY}" stroke-width="3"/><rect x="{x - a * 0.45}" y="{y - a * 0.45}" width="{a * 0.9}" height="{a * 0.9}" fill="{NAVY}"/>'
    if kind == 'triangle':
        return f'<polygon points="{x},{y - a} {x + a * 1.1},{y + a * 0.85} {x - a * 1.1},{y + a * 0.85}" fill="#FFE59A" stroke="{NAVY}" stroke-width="3"/><line x1="{x - a * 0.6}" y1="{y + a * 0.3}" x2="{x + a * 0.6}" y2="{y + a * 0.3}" stroke="{NAVY}" stroke-width="2.4"/>'
    if kind == 'star':
        pts = ' '.join(f'{x + (a if i % 2 == 0 else a * 0.45) * math.sin(i * math.pi / 5):.1f},{y - (a if i % 2 == 0 else a * 0.45) * math.cos(i * math.pi / 5):.1f}' for i in range(10))
        return f'<polygon points="{pts}" fill="#C9B6F0" stroke="{NAVY}" stroke-width="3"/>'
    if kind == 'heart':
        return f'<path d="M{x} {y + a} C{x - a * 1.6} {y - a * 0.2} {x - a * 0.7} {y - a * 1.1} {x} {y - a * 0.3} C{x + a * 0.7} {y - a * 1.1} {x + a * 1.6} {y - a * 0.2} {x} {y + a}" fill="#FF8FB1" stroke="{NAVY}" stroke-width="3"/><circle cx="{x}" cy="{y}" r="3" fill="{NAVY}"/>'
    if kind == 'diamond':
        return f'<polygon points="{x},{y - a} {x + a},{y} {x},{y + a} {x - a},{y}" fill="#9FD0F5" stroke="{NAVY}" stroke-width="3"/><line x1="{x - a * 0.5}" y1="{y}" x2="{x + a * 0.5}" y2="{y}" stroke="{NAVY}" stroke-width="2.4"/>'
    raise ValueError('unknown symbol ' + kind)


def picture_equation(rows=None, values=None, sym=60):
    """rows=[{"items":[{"sym":"circle","n":2},{"num":"5"},{"sym":"triangle"}],"op":"+","total":"17"}]; an item {"num": 5} (or "[]") puts a number or answer box in the line.
    values={"circle":"[]"} draws a legend with answer boxes. sym = symbol size (default 60, large enough for A4 print)."""
    rows = rows or []
    body = []; y = sym * 0.75; maxw = 0
    gap = 26
    for r in rows:
        x = 16
        op = r.get('op', '+')
        first = True
        for it in r['items']:
            reps = it.get('n', 1) if 'sym' in it else 1
            for _ in range(reps):
                if not first:
                    body.append(f'<text x="{x + 22}" y="{y + 17}" font-size="54" font-weight="800" text-anchor="middle" fill="{NAVY}" font-family="{FONT}">{it.get("op", op)}</text>'); x += 44 + 8
                if 'sym' in it:
                    body.append(_sym(it['sym'], x + sym / 2, y, sym)); x += sym + gap * 0.4
                else:
                    t = str(it.get('num', it.get('text', '[]')))
                    w = max(sym, 34 * len(t) + 28) if t != '[]' else sym * 1.2
                    body.append(token_svg(t, x + w / 2, y, w, sym, 48)); x += w + gap * 0.4
                first = False
        body.append(f'<text x="{x + 24}" y="{y + 18}" font-size="56" font-weight="800" text-anchor="middle" fill="{NAVY}" font-family="{FONT}">=</text>')
        t = str(r.get('total', '[]')); tw = max(sym * 1.4, 34 * len(t) + 30) if t != '[]' else sym * 1.6
        body.append(token_svg(t, x + 64 + tw / 2, y, tw, sym, 50)); x += 64 + tw
        maxw = max(maxw, x); y += sym + 36
    if values:
        x = 16; y += 10
        for k, v in values.items():
            body.append(_sym(k, x + sym / 2, y, sym)); body.append(f'<text x="{x + sym + 30}" y="{y + 18}" font-size="52" font-weight="800" text-anchor="middle" fill="{NAVY}" font-family="{FONT}">=</text>')
            body.append(token_svg(v, x + sym + 100, y, 90, sym, 48)); x += sym + 200
        maxw = max(maxw, x); y += sym + 20
    return _svg(max(maxw + 16, 560), y + 4, ''.join(body), 'picture equation')


# ------------------------------------------------------------------ ten-frame in two colours, dominoes

def ten_frame2(filled=(0, 0), extra=(0, 0), cols=(RED, YEL), ring=0, dash=0):
    """Two-colour ten-frame: filled=[red, yellow] counters in the first frame (red first), extra=[red, yellow] in a second frame.
    ring=k rings the last k counters (the '1 more'); dash=k draws the last k counters dashed and empty (the '1 less', taken away). Both act on the last frame that has counters."""
    cell = 64; body = []

    def frame(x0, cnts, last=False):
        seq = [cols[0]] * cnts[0] + [cols[1]] * cnts[1]
        for r in range(2):
            for c in range(5):
                x, y = x0 + c * cell, 6 + r * cell
                body.append(f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" fill="#fff" stroke="{NAVY}" stroke-width="2.4"/>')
                i = r * 5 + c
                if i < len(seq):
                    from_end = len(seq) - i
                    if last and dash and from_end <= dash:
                        body.append(f'<circle cx="{x + cell / 2}" cy="{y + cell / 2}" r="22" fill="#fff" stroke="{RED}" stroke-width="3.4" stroke-dasharray="6 4"/><line x1="{x + cell * 0.25}" y1="{y + cell * 0.75}" x2="{x + cell * 0.75}" y2="{y + cell * 0.25}" stroke="{RED}" stroke-width="3.4"/>')
                    else:
                        body.append(f'<circle cx="{x + cell / 2}" cy="{y + cell / 2}" r="22" fill="{seq[i]}" stroke="{NAVY}" stroke-width="2"/>')
                        if last and ring and from_end <= ring: body.append(f'<circle cx="{x + cell / 2}" cy="{y + cell / 2}" r="29" fill="none" stroke="{TEAL}" stroke-width="4.5"/>')
    two = bool(sum(extra))
    frame(6, filled, not two); W = 5 * cell + 12
    if two:
        frame(6 + 5 * cell + 40, extra, True); W = 10 * cell + 52
        body.append(f'<text x="{5 * cell + 26}" y="{6 + cell + 14}" font-size="46" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="{FONT}">+</text>')
    return _svg(W, 2 * cell + 12, ''.join(body), 'ten frame')


_PIPS = {0: [], 1: [(0, 0)], 2: [(-1, -1), (1, 1)], 3: [(-1, -1), (0, 0), (1, 1)], 4: [(-1, -1), (1, -1), (-1, 1), (1, 1)], 5: [(-1, -1), (1, -1), (0, 0), (-1, 1), (1, 1)],
         6: [(-1, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (1, 1)], 7: [(-1, -1), (1, -1), (-1, 0), (0, 0), (1, 0), (-1, 1), (1, 1)],
         8: [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)], 9: [(-1, -1), (0, -1), (1, -1), (-1, 0), (0, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]}


def domino(left=0, right=0):
    """A domino with true pip patterns (0 to 9 on a half)."""
    s = 150; body = [f'<rect x="6" y="6" width="{2 * s}" height="{s}" rx="16" fill="#fff" stroke="{NAVY}" stroke-width="4"/><line x1="{s + 6}" y1="16" x2="{s + 6}" y2="{s - 4}" stroke="{NAVY}" stroke-width="4"/>']
    for half, n in ((0, left), (1, right)):
        cx = 6 + s / 2 + half * s; cy = 6 + s / 2
        for (dx, dy) in _PIPS[n]:
            body.append(f'<circle cx="{cx + dx * 34:.1f}" cy="{cy + dy * 34:.1f}" r="11" fill="{NAVY}"/>')
    return _svg(2 * s + 12, s + 12, ''.join(body), f'domino {left} and {right}')


# ------------------------------------------------------------------ kit pages

def groups_mat(n=6, container='plate'):
    """Cut-out/lay-out mat: n big plates (or bags) to put counters on."""
    cw, ch = 330, 250 if container == 'plate' else 280
    body = []
    for i in range(n):
        r, c = divmod(i, 2)
        body.append(_container(container, 20 + c * (cw + 30), 20 + r * (ch + 30), cw, ch))
        body.append(f'<text x="{20 + c * (cw + 30) + cw / 2}" y="{20 + r * (ch + 30) + ch / 2 + 12}" font-size="44" font-weight="800" text-anchor="middle" fill="#7F90AD" font-family="{FONT}">{i + 1}</text>')
    rows = (n + 1) // 2
    return _svg(40 + 2 * cw + 30, 40 + rows * (ch + 30), ''.join(body), 'groups mat')


def unit_strips(rows=8, cells=10):
    """Strips of equal cells in two colours, with dotted lines between cells so a strip can be cut to any length."""
    cw, ch = 66, 62
    body = []
    for r in range(rows):
        y = 12 + r * (ch + 20)
        col = YEL if r % 2 == 0 else SKY
        for c in range(cells):
            body.append(f'<rect x="{6 + c * cw}" y="{y}" width="{cw}" height="{ch}" fill="{col}" stroke="{NAVY}" stroke-width="2.4"/>')
            if c: body.append(f'<line x1="{6 + c * cw}" y1="{y - 8}" x2="{6 + c * cw}" y2="{y + ch + 8}" stroke="#777" stroke-width="1.4" stroke-dasharray="4 4"/>')
    return _svg(cells * cw + 12, 24 + rows * (ch + 20), ''.join(body), 'unit strips')


def array_mat(rows=5, cols=8, cell=84):
    body = []
    for r in range(rows):
        for c in range(cols):
            body.append(f'<rect x="{6 + c * cell}" y="{6 + r * cell}" width="{cell}" height="{cell}" fill="#fff" stroke="{NAVY}" stroke-width="2.6"/>')
    return _svg(cols * cell + 12, rows * cell + 12, ''.join(body), 'array mat')


def people_strip(n=10):
    """A strip of n cut-out people in five colours (for queue and ordinal work)."""
    cell = 120; body = []
    for i in range(n):
        r, c = divmod(i, 5)
        x = 10 + c * cell; y = 10 + r * 150
        body.append(f'<rect x="{x}" y="{y}" width="{cell - 8}" height="138" fill="none" stroke="#777" stroke-width="1.6" stroke-dasharray="6 4"/>')
        body.append(icon(f'child{i % 5 + 1}', x + (cell - 8) / 2, y + 66, 108))
        # white marks on the two dark shirts (blue, purple) so they stay different when printed in black and white
        k = i % 5; ox = x + (cell - 8) / 2 - 54; oy = y + 66 - 54; sc = 108 / 64.0
        if k == 1:
            body.append(''.join(f'<rect x="{ox + 22 * sc:.1f}" y="{oy + yy * sc:.1f}" width="{20 * sc:.1f}" height="{2.6 * sc:.1f}" fill="#fff"/>' for yy in (37, 43, 49)))
        if k == 4:
            body.append(''.join(f'<circle cx="{ox + xx * sc:.1f}" cy="{oy + yy * sc:.1f}" r="{2.2 * sc:.1f}" fill="#fff"/>' for xx, yy in ((26, 38), (38, 38), (32, 44), (26, 50), (38, 50))))
    rows = (n + 4) // 5
    return _svg(5 * cell + 20, rows * 150 + 16, ''.join(body), 'cut-out people')


def render(v):
    """Dispatch for figure types added in Term 2 (and, through figs3, Terms 3 and 4); returns None if v['type'] is not one of them."""
    t = v['type']
    import figs3
    if t in figs3.FIGURES3: return figs3.render(v)
    if t == 'objects':
        return objects(v.get('icon'), v.get('n', 0), v.get('per_row', 5), v.get('size', 'm'), tuple(v.get('cross', ())), tuple(v.get('hide', ())), v.get('label'), v.get('items'))
    if t == 'groups':
        return groups(v.get('container', 'plate'), v.get('n', 3), v.get('each', 3), v.get('icon', 'apple'), v.get('counts'), v.get('empty', False), v.get('label_each'), v.get('total'), v.get('per_row', 4))
    if t == 'array':
        return array(v.get('rows', 3), v.get('cols', 4), v.get('icon', 'dot'), tuple(v.get('hide', ())), tuple(v.get('shade_rows', ())), v.get('pairs', False), v.get('ring_left_over', False), v.get('row_label'), v.get('col_label'), v.get('cell', 48))
    if t == 'line_up':
        return line_up(v.get('n', 8), v.get('names'), v.get('front', 'left'), v.get('marker', 'door'), v.get('labels', 'ordinal'), tuple(v.get('highlight', ())), v.get('between'), v.get('icons'))
    if t == 'round_table':
        return round_table(v.get('seats', 6), v.get('names'), tuple(v.get('hide', ())))
    if t == 'bar_model':
        return bar_model(v.get('mode', 'compare'), v.get('bars'), v.get('brace'), v.get('gap'), v.get('units'), v.get('arrow'))
    if t == 'table':
        return table(v.get('head'), v.get('rows'), v.get('col_w'), v.get('first_col'))
    if t == 'picture_equation':
        return picture_equation(v.get('rows'), v.get('values'), v.get('sym', 60))
    if t == 'domino':
        return domino(v.get('left', 0), v.get('right', 0))
    return None


def render_kit(spec):
    t = spec['type']
    import figs3
    if t in figs3.KITS3: return figs3.render_kit(spec)
    if t == 'groups_mat': return groups_mat(spec.get('n', 6), spec.get('container', 'plate'))
    if t == 'unit_strips': return unit_strips(spec.get('rows', 8), spec.get('cells', 10))
    if t == 'array_mat': return array_mat(spec.get('rows', 5), spec.get('cols', 8))
    if t == 'people': return people_strip(spec.get('n', 10))
    return None
