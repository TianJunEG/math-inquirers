"""Figure types for Level 2 unit 6 (money with dollars and cents).

  l2_money  play money in a row: items such as "5¢", "10¢", "20¢", "50¢", "$1" (round coins; the $1 coin has a double rim) and "$2", "$5", "$10", "$50"
            (notes: rectangles with a double border, bigger notes are longer).  The value is printed on every piece.  `sets` = [{label, items}] gives a row per set.
  l2_tags   price tags: items [{name, price}] where price is printed as given (for example "$4.50" or "85¢").
Palette NAVY / SOFT / SKY only, so print edition is clean black and white.  Pieces differ by shape, size and printed value, never by colour.
"""
import figs as F
from figs_l2_core import T, box, line, wrap, NAVY, SKY, SOFT, YEL

R = {'5¢': 36, '10¢': 38, '20¢': 42, '50¢': 46, '$1': 46}
NW = {'$2': 156, '$5': 170, '$10': 184, '$50': 198, '$100': 212}


def _piece(it, x, y, rowh):
    """Return (svg list, width) for a piece whose left edge is x and which is centred vertically in a row of height rowh."""
    if it in R:
        r = R[it]
        cx, cy = x + r, y + rowh / 2
        P = [f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{SOFT}" stroke="{NAVY}" stroke-width="3.6"/>']
        if it == '$1':
            P.append(f'<circle cx="{cx}" cy="{cy}" r="{r - 9}" fill="none" stroke="{NAVY}" stroke-width="2.2"/>')
        else:
            P.append(f'<circle cx="{cx}" cy="{cy}" r="{r - 6}" fill="none" stroke="{NAVY}" stroke-width="1.4" stroke-dasharray="3 4"/>')
        P.append(T(cx, cy + 10, it, 28 if len(it) > 2 else 32))
        return P, 2 * r
    w = NW[it]
    h = 82
    ny = y + (rowh - h) / 2
    P = [box(x, ny, w, h, SKY, sw=3.4, rx=8), box(x + 7, ny + 7, w - 14, h - 14, 'none', sw=1.6, rx=5)]
    P.append(T(x + w / 2, ny + h / 2 + 11, it, 34))
    return P, w


def money(spec, w=None):
    sets = spec.get('sets') or [{'items': spec['items']}]
    rowh = 104
    LW = 90 if any(s.get('label') for s in sets) else 0
    P = []
    maxw = 0
    for ri, st in enumerate(sets):
        y = 6 + ri * (rowh + 10)
        x = 6 + LW
        if st.get('label'):
            P.append(T(6 + 38, y + rowh / 2 + 10, st['label'], 30))
        for it in st['items']:
            pcs, ww = _piece(it, x, y, rowh)
            P += pcs
            x += ww + 16
        maxw = max(maxw, x)
    return wrap(P, maxw, 12 + len(sets) * (rowh + 10), 'play money', w, 0.2)


def tags(spec, w=None):
    its = spec['items']
    tw, th = 188, 124
    gap = 26
    per = spec.get('per_row', len(its))
    P = []
    for i, it in enumerate(its):
        r, c = divmod(i, per)
        x, y = 8 + c * (tw + gap), 8 + r * (th + gap)
        P.append(f'<path d="M{x + 26} {y} H{x + tw - 8} Q{x + tw} {y} {x + tw} {y + 8} V{y + th - 8} Q{x + tw} {y + th} {x + tw - 8} {y + th} H{x + 26} L{x} {y + th / 2}Z" fill="{SOFT}" stroke="{NAVY}" stroke-width="3.4" stroke-linejoin="round"/>')
        P.append(f'<circle cx="{x + 30}" cy="{y + th / 2}" r="7" fill="#fff" stroke="{NAVY}" stroke-width="2.6"/>')
        P.append(T(x + 38 + (tw - 46) / 2, y + 48, it['name'], 28, weight=600))
        P.append(T(x + 38 + (tw - 46) / 2, y + 98, it['price'], 40, weight=800))
    cols = min(per, len(its))
    rows = (len(its) + per - 1) // per
    return wrap(P, 16 + cols * (tw + gap) - gap, 16 + rows * (th + gap) - gap, 'price tags', w, 0.2)


FIGS = {'l2_money': money, 'l2_tags': tags}
