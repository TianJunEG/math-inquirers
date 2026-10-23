"""Extra figure types for Level 1 units 5 and 6 (working backwards; money).

Plugged into figs.render() through the FIGS table.  Types:
  chain    boxes joined by forward arcs (+5, -3); None = empty dashed box; optional `undo` labels drawn BELOW as dashed backward arcs
  in_out   a two-row IN / OUT table for a number machine; None = empty dashed cell
  coins    play money in a row (coins are circles, notes are rectangles, bigger value = bigger piece, value printed on each piece);
           `sets` = [{label, items}] gives one row per set (Set A, Set B)
  tags     small tags with a name and an amount (shop labels)
Palette: NAVY / TEAL / RED / SOFT / SKY only, so figs.recolour() gives the black-and-white print version: SOFT and SKY go white,
the text and lines go black.  Nothing depends on colour: pieces differ by size, shape and the printed value; undo arcs are dashed.
"""
import figs as F

NAVY, TEAL, RED, SKY, SOFT = F.NAVY, F.TEAL, F.RED, F.SKY, F.SOFT
SW = 3.2


def _t(x, y, txt, size=30, fill=NAVY, anchor='middle', weight=800):
    return F._t(x, y, txt, size, fill, anchor, weight)


# ------------------------------------------------------------------------------------------------ chain
def chain(spec, w=None):
    nodes, ops, undo = spec['nodes'], spec.get('ops') or [], spec.get('undo')
    bw, sp, bh = 104, 84, 84
    y0 = 78
    n = len(nodes)
    W = 12 + n * bw + (n - 1) * sp
    H = 78 + bh + (96 if undo else 24)
    P = []
    for i, v in enumerate(nodes):
        x = 6 + i * (bw + sp)
        dash = ' stroke-dasharray="9 6"' if v is None else ''
        P.append(f'<rect x="{x}" y="{y0}" width="{bw}" height="{bh}" rx="16" fill="#fff" stroke="{NAVY}" stroke-width="{SW}"{dash}/>')
        if v is not None:
            P.append(_t(x + bw / 2, y0 + bh / 2 + 16, v, 48, weight=700))
        if i < n - 1:
            xa, xb = x + bw / 2, x + bw + sp + bw / 2
            P.append(f'<path d="M{xa + 16},{y0} Q{(xa + xb) / 2},{y0 - 64} {xb - 16},{y0 - 2}" fill="none" stroke="{TEAL}" stroke-width="4.2" stroke-linecap="round"/>')
            P.append(f'<polygon points="{xb - 16},{y0 - 1} {xb - 32},{y0 - 6} {xb - 23},{y0 - 20}" fill="{TEAL}"/>')
            if i < len(ops) and ops[i]:
                P.append(_t((xa + xb) / 2, y0 - 36, ops[i], 32, TEAL))
            if undo and i < len(undo) and undo[i]:
                yb = y0 + bh
                P.append(f'<path d="M{xb - 16},{yb} Q{(xa + xb) / 2},{yb + 66} {xa + 16},{yb + 2}" fill="none" stroke="{RED}" stroke-width="4.2" stroke-linecap="round" stroke-dasharray="11 7"/>')
                P.append(f'<polygon points="{xa + 16},{yb + 1} {xa + 32},{yb + 6} {xa + 23},{yb + 20}" fill="{RED}"/>')
                P.append(_t((xa + xb) / 2, yb + 56, 'undo ' + undo[i], 28, RED))
    return F._wrap(''.join(P), W, H, 'number steps with arrows', w or 150)


# ------------------------------------------------------------------------------------------------ in_out
def in_out(spec, w=None):
    ins, outs = spec['in'], spec['out']
    cw, ch, lw = 104, 70, 96
    n = len(ins)
    W = lw + n * cw + 8
    H = 2 * ch + 20
    P = []
    for r, (lab, row) in enumerate((('IN', ins), ('OUT', outs))):
        y = 6 + r * (ch + 8)
        P.append(f'<rect x="4" y="{y}" width="{lw - 10}" height="{ch}" rx="10" fill="{SKY}" stroke="{NAVY}" stroke-width="{SW}"/>')
        P.append(_t(4 + (lw - 10) / 2, y + ch / 2 + 11, lab, 32))
        for i, v in enumerate(row):
            x = lw + i * cw
            dash = ' stroke-dasharray="9 6"' if v is None else ''
            P.append(f'<rect x="{x}" y="{y}" width="{cw - 6}" height="{ch}" rx="10" fill="#fff" stroke="{NAVY}" stroke-width="{SW}"{dash}/>')
            if v is not None:
                P.append(_t(x + (cw - 6) / 2, y + ch / 2 + 15, v, 42, weight=700))
    return F._wrap(''.join(P), W, H, 'in and out table of a number machine', w or 120)


# ------------------------------------------------------------------------------------------------ coins
COIN_R = {'5¢': 24, '10¢': 27, '20¢': 31, '50¢': 35, '$1': 40}
NOTE_WH = {'$2': (100, 54), '$5': (112, 58), '$10': (124, 62), '$50': (136, 66)}


def piece(v, x, y):
    """One coin or note centred at x, y; returns (svg, width)."""
    if v in COIN_R:
        r = COIN_R[v]
        fs = 22 if len(v) < 4 else 21
        s = (f'<circle cx="{x}" cy="{y}" r="{r}" fill="{SOFT}" stroke="{NAVY}" stroke-width="{SW}"/>'
             f'<circle cx="{x}" cy="{y}" r="{r - 5}" fill="none" stroke="{NAVY}" stroke-width="1.6"/>' + _t(x, y + 8, v, fs))
        return s, 2 * r
    wd, ht = NOTE_WH[v]
    s = (f'<rect x="{x - wd / 2}" y="{y - ht / 2}" width="{wd}" height="{ht}" rx="5" fill="{SKY}" stroke="{NAVY}" stroke-width="{SW}"/>'
         f'<rect x="{x - wd / 2 + 6}" y="{y - ht / 2 + 6}" width="{wd - 12}" height="{ht - 12}" rx="3" fill="none" stroke="{NAVY}" stroke-width="1.6" stroke-dasharray="5 4"/>'
         + _t(x, y + 11, v, 32))
    return s, wd


def coins(spec, w=None):
    sets = spec.get('sets') or [{'label': spec.get('label', ''), 'items': spec['items']}]
    P = []
    Wmax = 0
    y = 8
    for st in sets:
        ph = max((2 * COIN_R[v] if v in COIN_R else NOTE_WH[v][1]) for v in st['items'])
        cy = y + ph / 2 + 2
        x = 10
        if st.get('label'):
            P.append(_t(x + 4, cy + 12, st['label'], 36, anchor='start'))
            x += 24 + 20 * len(st['label']) + 22
        for v in st['items']:
            if v not in COIN_R and v not in NOTE_WH:
                raise ValueError('unknown money piece ' + v)
            wd = 2 * COIN_R[v] if v in COIN_R else NOTE_WH[v][0]
            s, _ = piece(v, x + wd / 2, cy)
            P.append(s)
            x += wd + 14
        Wmax = max(Wmax, x)
        y += ph + 14
    return F._wrap(''.join(P), Wmax + 2, y + 2, 'play money', w or 140)


# ------------------------------------------------------------------------------------------------ tags
def tags(spec, w=None):
    items = spec['items']
    tw, th, gap = 150, 118, 24
    P = []
    for i, d in enumerate(items):
        x = 8 + i * (tw + gap)
        P.append(f'<path d="M{x + 26},6 H{x + tw} V{th} H{x + 26} L{x + 4},{th / 2 + 4} Z" fill="{SOFT}" stroke="{NAVY}" stroke-width="{SW}" stroke-linejoin="round"/>')
        P.append(f'<circle cx="{x + 30}" cy="{th / 2 + 4}" r="6" fill="#fff" stroke="{NAVY}" stroke-width="2.4"/>')
        P.append(_t(x + 28 + (tw - 28) / 2 + 4, 44, d['name'], 26))
        P.append(_t(x + 28 + (tw - 28) / 2 + 4, 92, d['amount'], 40))
    W = 16 + len(items) * (tw + gap) - gap
    return F._wrap(''.join(P), W, th + 12, 'shop tags with amounts', w or 150)


FIGS = {'chain': chain, 'in_out': in_out, 'coins': coins, 'tags': tags}
