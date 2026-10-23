"""Level 6 figure types, part 1: code blocks, tables, number lines, machines, trees, cards.  All type names start with l6_ so that they cannot
clash with the plug-ins of other levels.  Every type: fn(spec, width_mm) -> svg.

Drawing unit: 1 unit = 0.25 mm (4 units = 1 mm), so a label of 16 to 18 units prints at 11 to 13 pt and a box 36 units wide is 9 mm.
Black-and-white rules (figs.recolour): only NAVY ink, SKY / SOFT light fills (they turn white), YEL for hatching (never behind text), "#fff".
Nothing is told by colour: code blocks are black text on a light fill, the kind of block is told by its shape and its words.

  l6_code   our own code blocks (not Scratch art).  spec: prog = list of [kind, text, children?, else_children?], kinds hat / var / look / ctl / op / list / pen;
            text may hold a slot "(n)", an empty slot "( )" (drawn as a dashed box to fill in), a test "<(n) {gt} (5)>"; {gt} {lt} are the signs > <.
            options: nums (number the lines at the left), fs (font units), gaps (list of line numbers drawn as a dashed empty block to fill in).
  l6_grid   a table.  spec: rows = list of rows of cells (str, '' for an empty box to write in, or {t, ring, bold, shade}); head = header row;
            rowhead (first column is a row heading); cw (mm per column, one number or a list); ch (mm row height); fs.
  l6_nline  horizontal number line.  spec: lo, hi, mm (mm per step), every (label every k steps), marks [{at, lab, kind: dot|ring|blank}],
            jumps [{a, b, lab, below}], unit (text after the last label), shade [(a, b)] draws a thick bar on the line.
  l6_vline  vertical number line (floors, depth, temperature).  spec: lo, hi, mm, marks [{at, lab}], side labels, every.
  l6_machine a chain IN -> rule -> value -> rule -> OUT.  spec: chain = [v0, op1, v1, ..., vk] (value: str, '' = empty box; op: str); undo (bool).
  l6_tree   factor tree.  spec: tree = {v: '60', kids: [{...}, {...}]}; a value '' is an empty circle to fill in; primes may be ringed with ring: true.
  l6_cards  digit / letter cards in a row.  spec: cards = [str], card (mm), gap.
"""
import html, re
import figs as F

NAVY, TEAL, YEL, SKY, SOFT = F.NAVY, F.TEAL, F.YEL, F.SKY, F.SOFT
U = 4.0
FS = 17


def esc(s):
    return html.escape(str(s), quote=False)


def T(x, y, txt, size=FS, anchor='middle', weight=700, fill=NAVY):
    return F._t(round(x, 1), round(y, 1), esc(txt), size, fill, anchor, weight)


def R(x, y, w, h, fill='#fff', sw=2.6, rx=5, dash=None, stroke=NAVY):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return (f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>')


def L(x1, y1, x2, y2, sw=2.6, dash=None, stroke=NAVY, cap='round'):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{stroke}" stroke-width="{sw}" stroke-linecap="{cap}"{d}/>'


def wrap(inner, W, H, label, w=None):
    return F._wrap(inner, round(W), round(H), label, w or round(W / U, 1))


MINUS = '−'


def neg(n):
    """A number as text with a real minus sign."""
    return (MINUS + str(-n)) if isinstance(n, int) and n < 0 else str(n)


# ================================================================================================ code blocks
KIND_FILL = {'hat': SOFT, 'ctl': SOFT, 'var': SKY, 'look': SKY, 'op': SKY, 'list': SKY, 'pen': SKY, 'move': SKY}


def _signs(s):
    return s.replace('{gt}', '>').replace('{lt}', '<')


def _tok(text):
    return [p for p in re.split(r'(<[^<>]*>|\([^()]*\))', text) if p != '']


class _Code:
    def __init__(self, fs):
        self.fs = fs
        self.H = fs * 2.15           # 36 units = 9 mm
        self.arm = fs * 1.2
        self.bot = fs * 1.0
        self.cw = fs * 0.6
        self.pad = fs * 0.6
        self.out = []
        self.mx = 0
        self.row = 0

    def seg_w(self, text):
        w = 0
        for s in _tok(text):
            if s[0] == '<':
                w += self.seg_w(s[1:-1]) + 3.2 * self.cw
            elif s[0] == '(':
                inner = _signs(s[1:-1])
                w += max(len(inner) * self.cw + 1.2 * self.cw, 2.4 * self.cw) if inner.strip() else 3.4 * self.cw
            else:
                w += len(_signs(s)) * self.cw
        return w

    def seg_draw(self, text, x, y, h=None):
        """draw one text line starting at x, vertically centred in a row of height H at y. returns the end x."""
        fs, cw = self.fs, self.cw
        h = h or self.H
        cy = y + h / 2
        for s in _tok(text):
            if s[0] == '<':
                inner = s[1:-1]
                w = self.seg_w(inner) + 3.2 * cw
                hh = h * 0.8
                y0 = cy - hh / 2
                pts = [(x + hh / 2, y0), (x + w - hh / 2, y0), (x + w, cy), (x + w - hh / 2, y0 + hh), (x + hh / 2, y0 + hh), (x, cy)]
                self.out.append('<polygon points="' + ' '.join(f'{a:.1f},{b:.1f}' for a, b in pts) + f'" fill="#fff" stroke="{NAVY}" stroke-width="2.2" stroke-linejoin="round"/>')
                self.seg_draw(inner, x + 1.6 * cw, y, h)
                x += w
            elif s[0] == '(':
                inner = _signs(s[1:-1])
                if inner.strip():
                    w = max(len(inner) * cw + 1.2 * cw, 2.4 * cw)
                    self.out.append(R(x, cy - h * 0.36, w, h * 0.72, '#fff', 2.0, h * 0.36))
                    self.out.append(T(x + w / 2, cy + fs * 0.36, inner, fs))
                else:
                    w = 3.4 * cw
                    self.out.append(R(x, cy - h * 0.36, w, h * 0.72, '#fff', 2.2, h * 0.36, dash='6 4'))
                x += w
            else:
                t = _signs(s)
                self.out.append(T(x, cy + fs * 0.36, t.replace(' ', '\u00a0'), fs, 'start', 700))
                x += len(t) * cw
        return x

    def measure(self, items, y):
        for it in items:
            y = self.measure_one(it, y)
        return y

    def measure_one(self, it, y):
        H = self.H
        if it[0] == 'hat':
            return y + self.fs * 0.8 + H
        if len(it) > 2 and it[2] is not None and not (isinstance(it[2], str)):
            arms = [it[2]] + ([it[3]] if len(it) > 3 else [])
            for ch in arms:
                y += H
                y0 = y
                y = self.measure(ch, y)
                if y == y0:
                    y += H * 0.7
            return y + self.bot
        return y + H

    def number(self, y):
        if self.nums:
            self.row += 1
            self.out.append(f'<circle cx="{self.fs * 0.85:.1f}" cy="{y + self.H / 2:.1f}" r="{self.fs * 0.8:.1f}" fill="#fff" stroke="{NAVY}" stroke-width="1.6"/>')
            self.out.append(T(self.fs * 0.85, y + self.H / 2 + self.fs * 0.34, self.row, self.fs * 0.85, weight=800))

    def walk(self, items, x, y):
        H, fs = self.H, self.fs
        for it in items:
            k, t = it[0], it[1]
            fill = KIND_FILL.get(k, SKY)
            gap_line = self.row + 1 in self.gaps and not (len(it) > 2 and not isinstance(it[2], str))
            if k == 'hat':
                w = max(self.seg_w(t) + 2 * self.pad, fs * 5)
                top = y + fs * 0.8
                self.out.append(f'<path d="M{x:.1f} {top:.1f} C{x + fs * 0.8:.1f} {y - fs * 0.5:.1f} {x + fs * 3.4:.1f} {y - fs * 0.5:.1f} {x + fs * 4:.1f} {top:.1f} '
                                f'L{x + w - 6:.1f} {top:.1f} Q{x + w:.1f} {top:.1f} {x + w:.1f} {top + 6:.1f} L{x + w:.1f} {top + H - 6:.1f} Q{x + w:.1f} {top + H:.1f} {x + w - 6:.1f} {top + H:.1f} '
                                f'L{x + 6:.1f} {top + H:.1f} Q{x:.1f} {top + H:.1f} {x:.1f} {top + H - 6:.1f} Z" fill="{fill}" stroke="{NAVY}" stroke-width="2.4" stroke-linejoin="round"/>')
                self.number(top)
                self.seg_draw(t, x + self.pad, top)
                self.mx = max(self.mx, x + w)
                y = top + H
                continue
            if len(it) > 2 and not isinstance(it[2], str) and it[2] is not None:
                arms = [it[2]] + ([it[3]] if len(it) > 3 else [])
                labels = [t, 'else']
                # layout: header rows and mouths
                segs = []
                yy = y
                for ch in arms:
                    top = yy
                    yy += H
                    c0 = yy
                    yy = self.measure(ch, yy)
                    if yy == c0:
                        yy += H * 0.7
                    segs.append((top, c0, yy))
                endy = yy + self.bot
                # width: widest header / contents (contents are measured by walking into a scratch list)
                w = max(self.seg_w(t) + 2 * self.pad, fs * 6)
                sub = _Code(self.fs); sub.nums = False; sub.gaps = set()
                for i, ch in enumerate(arms):
                    sub.out = []; sub.mx = 0
                    sub.walk(ch, 0, 0)
                    w = max(w, self.arm + sub.mx + 4)
                self.out.append(R(x, y, w, endy - y, fill, 2.4, 7))
                for i, (top, c0, c1) in enumerate(segs):
                    # white mouth
                    self.out.append(f'<rect x="{x + self.arm:.1f}" y="{c0:.1f}" width="{w - self.arm - 2:.1f}" height="{c1 - c0:.1f}" fill="#fff" stroke="{NAVY}" stroke-width="2.0"/>')
                    if i == 0:
                        self.number(top)
                    self.seg_draw(labels[i], x + self.pad, top)
                    self.walk_into(arms[i], x + self.arm, c0, c1)
                self.mx = max(self.mx, x + w)
                y = endy
                continue
            # simple block
            w = max(self.seg_w(t) + 2 * self.pad, fs * 5)
            if gap_line:
                self.out.append(R(x, y, max(w, fs * 8), H, '#fff', 2.4, 7, dash='8 5'))
                self.number(y)
                self.mx = max(self.mx, x + max(w, fs * 8))
            else:
                self.out.append(R(x, y, w, H, fill, 2.4, 7))
                self.number(y)
                self.seg_draw(t, x + self.pad, y)
                self.mx = max(self.mx, x + w)
            y += H
        return y

    def walk_into(self, items, x, y, y1):
        if items:
            self.walk(items, x, y)


def code(spec, w=None):
    fs = spec.get('fs', 16)
    c = _Code(fs)
    c.nums = bool(spec.get('nums'))
    c.gaps = set(spec.get('gaps', []))
    off = fs * 2.0 if c.nums else 0
    yend = c.walk(spec['prog'], 3 + off, 3)
    W = c.mx + 6
    H = yend + 6
    if c.nums:
        W += 0
    return wrap(''.join(c.out), W, H, spec.get('label', 'code blocks'), w or round(W / U, 1))


# ================================================================================================ grid / table
def grid(spec, w=None):
    rows = spec['rows']
    head = spec.get('head')
    ncol = max(len(r) for r in rows + ([head] if head else []))
    cw = spec.get('cw', 16)
    cws = cw if isinstance(cw, list) else [cw] * ncol
    ch = spec.get('ch', 9)
    fs = spec.get('fs', 17)
    rowhead = spec.get('rowhead', False)
    colhead_fill = SKY
    P = []
    y = 3
    allrows = ([('H', head)] if head else []) + [('R', r) for r in rows]
    W = sum(cws) * U + 6
    for kind, r in allrows:
        x = 3
        rh = ch * U
        for j in range(ncol):
            cell = r[j] if j < len(r) else ''
            d = cell if isinstance(cell, dict) else {'t': cell}
            tx = '' if d.get('t') is None else str(d.get('t'))
            wj = cws[j] * U
            shade = kind == 'H' or (rowhead and j == 0) or d.get('shade')
            P.append(R(x, y, wj, rh, SKY if shade else '#fff', 2.4, 2))
            if d.get('ring'):
                P.append(f'<ellipse cx="{x + wj / 2:.1f}" cy="{y + rh / 2:.1f}" rx="{min(wj / 2 - 3, rh * 0.62):.1f}" ry="{rh / 2 - 3:.1f}" fill="none" stroke="{NAVY}" stroke-width="3.4"/>')
            if d.get('box'):
                P.append(R(x + 3, y + 3, wj - 6, rh - 6, 'none', 4.2, 2))
            if tx:
                P.append(T(x + wj / 2, y + rh / 2 + fs * 0.35, _signs(tx), d.get('fs', fs), weight=800 if (kind == 'H' or (rowhead and j == 0) or d.get('bold')) else 600))
            x += wj
        y += rh
    return wrap(''.join(P), W, y + 3, spec.get('label', 'table'), w)


# ================================================================================================ number line
def nline(spec, w=None):
    lo, hi = spec['lo'], spec['hi']
    mm = spec.get('mm', 8)
    every = spec.get('every', 1)
    sp = mm * U
    X0 = 36
    W = X0 * 2 + (hi - lo) * sp + (spec.get('pad_right', 0) * U)
    ay = 44 + (spec.get('above', 0) * U) + (56 if any(not j.get('below') for j in spec.get('jumps', [])) else 0)
    below_jumps = any(j.get('below') for j in spec.get('jumps', []))
    H = ay + 70 + (56 if below_jumps else 0)
    P = []
    xs = lambda v: X0 + (v - lo) * sp
    P.append(L(xs(lo) - 22, ay, xs(hi) + 22, ay, 3.2))
    P.append(f'<path d="M{xs(hi) + 22:.1f} {ay} l-10 -7 v14 z" fill="{NAVY}" stroke="{NAVY}" stroke-width="1.5"/>')
    P.append(f'<path d="M{xs(lo) - 22:.1f} {ay} l10 -7 v14 z" fill="{NAVY}" stroke="{NAVY}" stroke-width="1.5"/>')
    for v in range(lo, hi + 1):
        major = (v - lo) % every == 0
        P.append(L(xs(v), ay - (12 if major else 8), xs(v), ay + (12 if major else 8), 3 if major else 2))
        if major and not spec.get('nolabels'):
            P.append(T(xs(v), ay + 40, neg(v) if v < 0 else v, 17, weight=700))
    for a, b in spec.get('shade', []):
        P.append(L(xs(a), ay, xs(b), ay, 9, stroke=NAVY, cap='butt'))
    for j in spec.get('jumps', []):
        a, b = xs(j['a']), xs(j['b'])
        if j.get('below'):
            yb = ay + 52
            P.append(f'<path d="M{a:.1f} {yb} Q{(a + b) / 2:.1f} {yb + 40} {b:.1f} {yb}" fill="none" stroke="{NAVY}" stroke-width="3.2"/>')
            P.append(f'<path d="M{b:.1f} {yb} l{-9 if b > a else 9} -12 M{b:.1f} {yb} l{-14 if b > a else 14} 5" stroke="{NAVY}" stroke-width="3" fill="none"/>')
            if j.get('lab'):
                P.append(T((a + b) / 2, yb + 32 + 17, j['lab'], 17))
        else:
            yt = ay - (46 if any(m.get('lab') for m in spec.get('marks', [])) else 18)
            P.append(f'<path d="M{a:.1f} {yt} Q{(a + b) / 2:.1f} {yt - 44} {b:.1f} {yt}" fill="none" stroke="{NAVY}" stroke-width="3.2"/>')
            P.append(f'<path d="M{b:.1f} {yt} l{-9 if b > a else 9} -12 M{b:.1f} {yt} l{-14 if b > a else 14} -5" stroke="{NAVY}" stroke-width="3" fill="none"/>')
            if j.get('lab'):
                P.append(T((a + b) / 2, yt - 36, j['lab'], 17))
    for m in spec.get('marks', []):
        x = xs(m['at'])
        k = m.get('kind', 'dot')
        if k == 'dot':
            P.append(f'<circle cx="{x:.1f}" cy="{ay}" r="9" fill="{NAVY}" stroke="{NAVY}"/>')
        elif k == 'ring':
            P.append(f'<circle cx="{x:.1f}" cy="{ay}" r="12" fill="#fff" stroke="{NAVY}" stroke-width="3.4"/>')
        elif k == 'blank':
            P.append(f'<circle cx="{x:.1f}" cy="{ay}" r="13" fill="#fff" stroke="{NAVY}" stroke-width="2.4" stroke-dasharray="5 4"/>')
        if m.get('lab'):
            P.append(T(x, ay - 22 - m.get('up', 0) * U, m['lab'], 17, weight=800))
    if spec.get('unit'):
        P.append(T(xs(hi) + 36, ay + 40, spec['unit'], 16, 'start', 600))
        W += len(spec['unit']) * 11
    return wrap(''.join(P), W, H, spec.get('label', 'number line'), w)


def vline(spec, w=None):
    lo, hi = spec['lo'], spec['hi']
    mm = spec.get('mm', 8)
    every = spec.get('every', 1)
    sp = mm * U
    X0 = 90
    H = 24 + (hi - lo) * sp + 24
    W = X0 + 230 + spec.get('right', 0) * U
    ys = lambda v: 24 + (hi - v) * sp
    P = [L(X0, ys(hi) - 14, X0, ys(lo) + 14, 3.2)]
    for v in range(lo, hi + 1):
        major = (v - lo) % every == 0
        P.append(L(X0 - (12 if major else 7), ys(v), X0 + (12 if major else 7), ys(v), 3 if major else 2))
        if major:
            P.append(T(X0 - 20, ys(v) + 6, neg(v) if v < 0 else v, 17, 'end'))
    for m in spec.get('marks', []):
        y = ys(m['at'])
        k = m.get('kind', 'dot')
        if k == 'blank':
            P.append(f'<circle cx="{X0}" cy="{y:.1f}" r="12" fill="#fff" stroke="{NAVY}" stroke-width="2.4" stroke-dasharray="5 4"/>')
        else:
            P.append(f'<circle cx="{X0}" cy="{y:.1f}" r="9" fill="{NAVY}"/>')
        if m.get('lab'):
            P.append(L(X0 + 12, y, X0 + 36, y, 2.2))
            P.append(T(X0 + 44, y + 6, m['lab'], 17, 'start', 700))
    if spec.get('title'):
        P.append(T(X0, 14, spec['title'], 16, 'middle', 800))
    return wrap(''.join(P), W, H, spec.get('label', 'vertical number line'), w)


# ================================================================================================ function machine chain
def machine(spec, w=None):
    ch = spec['chain']
    vw, vh, ow, oh = 14 * U, 10 * U, 0, 10 * U
    gapw = 8 * U
    P = []
    x = 3
    top = 30
    xs = []
    for i, c in enumerate(ch):
        isop = i % 2 == 1
        if isop:
            ww = max(len(str(c)) * 0.62 * 18 + 24, 11 * U)
            xs.append((x, ww, True))
        else:
            ww = max(vw, len(str(c)) * 0.62 * 20 + 20)
            xs.append((x, ww, False))
        x += ww + gapw
    W = x - gapw + 6
    for i, c in enumerate(ch):
        x0, ww, isop = xs[i]
        if isop:
            P.append(R(x0, top - 3, ww, oh + 6, SOFT, 2.8, 14))
            P.append(T(x0 + ww / 2, top + oh / 2 + 7, _signs(str(c)), 19, weight=800))
        else:
            P.append(R(x0, top, ww, vh, '#fff', 3, 4, dash=None))
            if str(c).strip():
                P.append(T(x0 + ww / 2, top + vh / 2 + 7, neg(c) if isinstance(c, int) else c, 20, weight=800))
        if i + 1 < len(ch):
            a = x0 + ww + 2
            b = xs[i + 1][0] - 2
            P.append(L(a, top + vh / 2, b - 6, top + vh / 2, 3))
            P.append(f'<path d="M{b:.1f} {top + vh / 2:.1f} l-11 -8 v16 z" fill="{NAVY}"/>')
    P.append(T(xs[0][0] + xs[0][1] / 2, 18, 'IN', 15, weight=800))
    P.append(T(xs[-1][0] + xs[-1][1] / 2, 18, 'OUT', 15, weight=800))
    H = top + vh + 14
    if spec.get('undo'):
        # dashed return arrows under the chain: from each value back to the one before it, with the opposite step written under (spec undo = list of labels)
        labs = spec['undo']
        yb = top + vh + 6
        for k, i in enumerate(range(0, len(ch) - 2, 2)):
            a = xs[i + 2][0] + xs[i + 2][1] / 2
            b = xs[i][0] + xs[i][1] / 2
            P.append(f'<path d="M{a:.1f} {yb} Q{(a + b) / 2:.1f} {yb + 44} {b:.1f} {yb}" fill="none" stroke="{NAVY}" stroke-width="2.6" stroke-dasharray="7 5"/>')
            P.append(f'<path d="M{b:.1f} {yb} l10 12 M{b:.1f} {yb} l15 -3" stroke="{NAVY}" stroke-width="2.8" fill="none"/>')
            if k < len(labs) and labs[k]:
                P.append(T((a + b) / 2, yb + 52, _signs(labs[k]), 17, weight=800))
        H += 62
    return wrap(''.join(P), W, H, spec.get('label', 'number machine'), w)


# ================================================================================================ factor tree
def tree(spec, w=None):
    R0 = 5.2 * U           # node radius (10.4 mm wide circles)
    gx, gy = 15 * U, 17 * U

    def width(n):
        return max(1, sum(width(k) for k in n.get('kids', []))) if n.get('kids') else 1

    P = []
    leaves = width(spec['tree'])
    W = leaves * gx + 20

    def draw(n, x0, y):
        ws = width(n)
        cx = x0 + ws * gx / 2
        kids = n.get('kids', [])
        px = x0
        pos = []
        for k in kids:
            wk = width(k)
            pos.append(px + wk * gx / 2)
            px += wk * gx
        for k, kx in zip(kids, pos):
            P.append(L(cx, y + R0, kx, y + gy - R0, 2.6))
        for k, kx in zip(kids, pos):
            pass
        v = n.get('v', '')
        ring = n.get('ring')
        P.append(f'<circle cx="{cx:.1f}" cy="{y:.1f}" r="{R0:.1f}" fill="#fff" stroke="{NAVY}" stroke-width="{4.2 if ring else 2.6}"/>')
        if ring:
            P.append(f'<circle cx="{cx:.1f}" cy="{y:.1f}" r="{R0 - 6:.1f}" fill="none" stroke="{NAVY}" stroke-width="1.6"/>')
        if str(v) != '':
            P.append(T(cx, y + 6.5, v, 19, weight=800))
        px = x0
        for k in kids:
            wk = width(k)
            draw(k, px, y + gy)
            px += wk * gx

    def depth(n):
        return 1 + max([depth(k) for k in n.get('kids', [])] or [0])

    draw(spec['tree'], 10, R0 + 6)
    H = depth(spec['tree']) * gy + 10
    return wrap(''.join(P), W, H, spec.get('label', 'factor tree'), w)


# ================================================================================================ cards
def cards(spec, w=None):
    cs = spec['cards']
    s = spec.get('card', 12) * U
    g = spec.get('gap', 4) * U
    P = []
    for i, c in enumerate(cs):
        x = 3 + i * (s + g)
        P.append(R(x, 3, s, s * 1.2, SOFT, 3, 8))
        P.append(T(x + s / 2, 3 + s * 0.6 + 14, c, 40, weight=800))
    W = len(cs) * (s + g) - g + 8
    return wrap(''.join(P), W, s * 1.2 + 8, 'cards', w)


FIGS = {'l6_code': code, 'l6_grid': grid, 'l6_nline': nline, 'l6_vline': vline, 'l6_machine': machine, 'l6_tree': tree, 'l6_cards': cards}
