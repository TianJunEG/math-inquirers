"""Lesson 4 build extension (The 100 Square Explorer).  NOT a shared tool: it only patches the template modules in memory.

Why this file exists
--------------------
Lesson 4 needs a numbered, colourable 100-square picture with counters, arrows, hidden cells and a window, and a growing-gap
number strip.  The shared template (term/l1/tools/*) has `hundred_square` (a fixed picture whose tens are pre-shaded, so it
cannot be used for a "colour the 10s" question) but no such picture.  The brief for this lesson forbids editing shared tool
files, so the new picture types are applied at run time.  Run the lesson through the wrapper until the template owner merges them:

    python3 term/l1/verify/l04_build.py            # validate, then build every output (same as build.sh 04)
    python3 term/l1/verify/l04_build.py validate   # validate only

TEMPLATE CHANGES THIS FILE IS A PATCH FOR (for the template owner)
  1. tools/svg.py: visual types `hundred` (numbered square with shade, shade2, hide, tags, mark, outline, arrows, rows, cols, per)
     and `seq` (number tiles with gap arcs), dispatched by render_visual(); kit type `hundred` in kit_figure().
  2. tools/b_deck.py: cols blocks need optional `weights` (unequal column widths, e.g. [3, 2] for a big square beside text); visual() sizes for `hundred` and `seq` (a 100 square is square: about 700 px, not 1000); qs_block() should not
     draw a 100-square question picture inside a slide row.
  3. tools/b_print.py: (a) CSS so that a question with a 100 square puts the picture beside the answer lines (see CSS below);
     (b) the page 1 line 'After question 3 you may choose' and the home sheet phrases 'Use real things or draw bundles' and
     'drawing the bundles' are still Lesson 1 wording: they should come from the lesson file like workbook.hint_p1 does.
"""
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
TOOLS = os.path.join(os.path.dirname(HERE), 'tools')
if TOOLS not in sys.path:
    sys.path.insert(0, TOOLS)

NAVY = '#1B2A49'; TEAL = '#1F7A6F'; YEL = '#FFC93C'; SOFT = '#FFF0C2'; RED = '#D64545'; MINT = '#BFE3DC'
FONT = "Fredoka, 'Nunito Sans', Arial, sans-serif"


# ------------------------------------------------------------------ pictures

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


HOME_HINT = {'04': ('Use real things or draw bundles.', 'Use your 100 square or draw it.')}
PAGE1_CHOICE = {'04': ('After question 3 you may choose', 'After question 2 you may choose')}

CSS = """
.qbox:has(svg.h100){display:grid;grid-template-columns:1fr 292px;column-gap:8px;align-items:start}
.qbox:has(svg.h100)>.q{grid-column:1 / span 2}
.qbox:has(svg.h100)>.vis{grid-column:2;grid-row:2 / span 8;width:292px!important;margin:0!important}
.qbox:has(svg.h100)>.sub,.qbox:has(svg.h100)>.ln,.qbox:has(svg.h100)>.draw{grid-column:1}
.qbox:has(svg.h100.wide){display:block}
.qbox:has(svg.h100.wide)>.vis{width:100%!important;margin:4px 0!important}
.p1 .qbox:has(svg.h100)>.vis{width:292px!important}
"""


def _swap(html, old, new):
    if old in html:
        html = html.replace(old, new)
    return html


def install():
    import svg, b_deck, b_print
    from common import E

    # ---- pictures
    orig = svg.render_visual

    def render_visual(v):
        t = v['type']
        if t == 'hundred':
            kw = {k: v[k] for k in ('shade', 'shade2', 'hide', 'mark', 'outline', 'arrows', 'rows', 'cols', 'per', 'cell', 'qmarks', 'tags') if k in v}
            if 'tags' in kw: kw['tags'] = {int(a): b for a, b in kw['tags'].items()}
            if 'arrows' in kw: kw['arrows'] = [tuple(a) for a in kw['arrows']]
            if 'rows' in kw: kw['rows'] = tuple(kw['rows'])
            if 'cols' in kw: kw['cols'] = tuple(kw['cols'])
            s = hundred(**kw)
            if v.get('wide'): s = s.replace('class="h100"', 'class="h100 wide"')
            return s
        if t == 'seq':
            return seq(v['items'], v.get('gaps'), v.get('hl', ()))
        return orig(v)
    svg.render_visual = render_visual
    svg.hundred = hundred; svg.seq = seq

    # ---- deck: sizes for the new pictures, and no 100 square inside a workbook question row on a slide
    orig_visual = b_deck.visual

    def visual(b, ctx_cols=1):
        if b['type'] in ('hundred', 'seq'):
            if b['type'] == 'seq':
                w = b.get('w', 1500 if ctx_cols == 1 else 760)
            else:
                nc = b.get('cols', [1, 10])[1] - b.get('cols', [1, 10])[0] + 1
                w = b.get('w', (b.get('cellpx', 70) if ctx_cols == 1 else b.get('cellpx', 50)) * nc + 20)
            cap = ''
            if b.get('label'):
                cap = f'<p style="font-size:38px;font-weight:700;color:{NAVY};text-align:center">{E(b["label"])}</p>'
            return f'<div style="{b_deck.CARD}padding:18px 30px;display:flex;flex-direction:column;align-items:center;gap:6px"><div style="width:{w}px;max-width:100%">{svg.render_visual(b)}</div>{cap}</div>'
        return orig_visual(b, ctx_cols)
    b_deck.visual = visual
    orig_qs = b_deck.qs_block

    def qs_block(d, ids, short):
        import copy
        d2 = dict(d); t = dict(d['tiers'])
        def strip(q):
            if q.get('visual', {}).get('type') == 'hundred':
                q = dict(q); q.pop('visual')
            return q
        t['start'] = [strip(q) for q in t['start']]; d2['tiers'] = t
        return orig_qs(d2, ids, short)
    b_deck.qs_block = qs_block

    orig_rb = b_deck.render_blocks

    def render_blocks(d, blocks, cols=1):
        out = []
        for b in blocks:
            if b['t'] == 'cols' and b.get('weights'):
                n = len(b['cols'])
                inner = ''.join(f'<div style="flex:{w};display:flex;flex-direction:column;gap:16px;align-items:stretch;min-width:0">{render_blocks(d, c, n)}</div>' for c, w in zip(b['cols'], b['weights']))
                out.append(f'<div style="display:flex;gap:32px;align-items:flex-start">{inner}</div>')
            else:
                out.append(orig_rb(d, [b], cols))
        return ''.join(out)
    b_deck.render_blocks = render_blocks

    # ---- kit page figure of type `hundred`
    orig_kit = svg.kit_figure

    def kit_figure(spec):
        if spec.get('type') == 'hundred':
            return hundred(cell=spec.get('cell', 64))
        return orig_kit(spec)
    svg.kit_figure = kit_figure

    # ---- print: CSS, and the two Lesson-1 phrases the template still hard-codes
    orig_wb, orig_home = b_print.workbook_html, b_print.home_html
    b_print.EXTRA += CSS

    def workbook_html(d, key=False):
        h = orig_wb(d, key)
        if d['_num'] in PAGE1_CHOICE: h = _swap(h, *PAGE1_CHOICE[d['_num']])
        return h

    def home_html(d):
        h = orig_home(d); num = d['_num']
        if num in HOME_HINT: h = _swap(h, *HOME_HINT[num])
        h = _swap(h, 'drawing the bundles', 'drawing it')
        return h
    b_print.workbook_html, b_print.home_html = workbook_html, home_html
    return True
