"""Level 5 solid figures: l5_solid (oblique boxes, tanks, water) and l5_cubes (isometric cube stacks).

l5_solid spec = {type, mm: 3.0 (mm per unit of length on paper), boxes: [...], texts: [...], lines: [...]}
  box   {x, y, z, l, w, h, kind: 'solid'|'tank'|'water', fill: 'light'|'shade'|None, grid: False}
        x to the right, y into the page (drawn up and to the right), z up.  'tank' = an open transparent box (hidden edges dashed);
        'water' = a block of water (wave lines on the front and right faces); 'solid' = a filled block.  grid: draw the unit squares.
  text  {at: [x, y, z], t: '12 cm', dx: 0, dy: 0, size: 20}
  line  {a: [x, y, z], b: [x, y, z], dash: True}
l5_cubes spec = {type, mm: 8 (cube edge on paper), heights: [[..], ..]  (rows from the back to the front, columns left to right; number of cubes in each column),
                 mark: 'none'|'right'  (hatch the right-hand faces), texts: [{t, at: [col, row, level], dx, dy}]}
Palette NAVY / SOFT / SKY / YEL only (YEL becomes hatching in print).  Nothing depends on colour.
"""
import itertools
import figs as F

NAVY, TEAL, YEL, SKY, SOFT = F.NAVY, F.TEAL, F.YEL, F.SKY, F.SOFT
U = 4.0
K = 0.42      # depth shrink of the oblique projection
FILL = {'shade': YEL, 'light': SOFT, 'sky': SKY, None: '#fff'}
_pid = itertools.count(1)


def _t(x, y, txt, size=20):
    return F._t(round(x, 1), round(y, 1), txt, size, NAVY, 'middle', 800).replace('<text ', '<text stroke="#fff" stroke-width="6" stroke-linejoin="round" paint-order="stroke" ', 1)


def solid(spec, w=None):
    mm = spec.get('mm', 3.0)
    s = mm * U
    P = lambda x, y, z: ((x + K * y) * s, -(z + K * y) * s)
    boxes = spec['boxes']
    pid = f'wv{next(_pid)}'
    pts = []
    for b in boxes:
        for dx, dy, dz in itertools.product((0, b['l']), (0, b['w']), (0, b['h'])):
            pts.append(P(b['x'] + dx, b['y'] + dy, b['z'] + dz))
    for t in spec.get('texts', []):
        px, py = P(*t['at'])
        pts.append((px + t.get('dx', 0) - 40, py + t.get('dy', 0) - 14)); pts.append((px + t.get('dx', 0) + 40, py + t.get('dy', 0) + 10))
    xs, ys = [p[0] for p in pts], [p[1] for p in pts]
    x0, y0 = min(xs) - 10, min(ys) - 10
    Wd, H = max(xs) - x0 + 10, max(ys) - y0 + 10
    Q = lambda x, y, z: (P(x, y, z)[0] - x0, P(x, y, z)[1] - y0)
    out = [f'<defs><pattern id="{pid}" width="30" height="16" patternUnits="userSpaceOnUse"><rect width="30" height="16" fill="#fff"/>'
           f'<path d="M0,8 q7.5,-7 15,0 t15,0" fill="none" stroke="{NAVY}" stroke-width="2.2"/></pattern></defs>']

    def poly(pp, fill, sw=2.8, dash=None, stroke=NAVY):
        d = f' stroke-dasharray="{dash}"' if dash else ''
        return f'<polygon points="{" ".join(f"{a:.1f},{b:.1f}" for a, b in pp)}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round"{d}/>'

    def seg(a, b, sw=2.8, dash=None):
        (xa, ya), (xb, yb) = Q(*a), Q(*b)
        d = f' stroke-dasharray="{dash}"' if dash else ''
        return f'<line x1="{xa:.1f}" y1="{ya:.1f}" x2="{xb:.1f}" y2="{yb:.1f}" stroke="{NAVY}" stroke-width="{sw}"{d}/>'

    for b in boxes:
        x, y, z, l, wd, h = b['x'], b['y'], b['z'], b['l'], b['w'], b['h']
        kind = b.get('kind', 'solid')
        front = [Q(x, y, z), Q(x + l, y, z), Q(x + l, y, z + h), Q(x, y, z + h)]
        top = [Q(x, y, z + h), Q(x + l, y, z + h), Q(x + l, y + wd, z + h), Q(x, y + wd, z + h)]
        right = [Q(x + l, y, z), Q(x + l, y + wd, z), Q(x + l, y + wd, z + h), Q(x + l, y, z + h)]
        if kind == 'tank':
            out.append(seg((x, y + wd, z), (x, y + wd, z + h), 2, '8 6'))
            out.append(seg((x, y + wd, z), (x + l, y + wd, z), 2, '8 6'))
            out.append(seg((x, y, z), (x, y + wd, z), 2, '8 6'))
            out.append(poly(front, 'none')); out.append(poly(top, 'none')); out.append(poly(right, 'none'))
        elif kind == 'water':
            out.append(poly(front, f'url(#{pid})', 2.2)); out.append(poly(right, f'url(#{pid})', 2.2)); out.append(poly(top, '#fff', 2.2))
        else:
            fl = FILL[b.get('fill', 'light')]
            out.append(poly(front, fl)); out.append(poly(top, '#fff' if b.get('fill') != 'shade' else fl)); out.append(poly(right, fl))
            if b.get('grid'):
                for i in range(1, int(l)):
                    out.append(seg((x + i, y, z), (x + i, y, z + h), 1.3)); out.append(seg((x + i, y, z + h), (x + i, y + wd, z + h), 1.3))
                for j in range(1, int(h)):
                    out.append(seg((x, y, z + j), (x + l, y, z + j), 1.3)); out.append(seg((x + l, y, z + j), (x + l, y + wd, z + j), 1.3))
                for k in range(1, int(wd)):
                    out.append(seg((x, y + k, z + h), (x + l, y + k, z + h), 1.3)); out.append(seg((x + l, y + k, z), (x + l, y + k, z + h), 1.3))
    for ln in spec.get('lines', []):
        out.append(seg(ln['a'], ln['b'], 2.2, '8 6' if ln.get('dash', True) else None))
    for t in spec.get('texts', []):
        px, py = Q(*t['at'])
        out.append(_t(px + t.get('dx', 0), py + t.get('dy', 0) + 7, t['t'], t.get('size', 20)))
    return F._wrap(''.join(out), round(Wd, 1), round(H, 1), spec.get('alt', 'solid figure'), round(Wd / U, 1))


def cubes(spec, w=None):
    """Isometric stack of unit cubes. heights[y][x]: number of cubes standing on cell (x, y); x goes right-down, y goes left-down
    (row 0 is the back row; the last row is nearest to the viewer on the left)."""
    c = spec.get('mm', 8) * U
    hm = spec['heights']
    cx, cy = c * 0.866, c * 0.5
    Pi = lambda x, y, z: ((x - y) * cx, (x + y) * cy - z * c)
    cells = sorted(((x, y, z) for y, row in enumerate(hm) for x, n in enumerate(row) for z in range(n)), key=lambda t: (t[0] + t[1], t[2]))
    polys, allp = [], []
    for x, y, z in cells:
        top = [Pi(x, y, z + 1), Pi(x + 1, y, z + 1), Pi(x + 1, y + 1, z + 1), Pi(x, y + 1, z + 1)]
        left = [Pi(x, y + 1, z), Pi(x + 1, y + 1, z), Pi(x + 1, y + 1, z + 1), Pi(x, y + 1, z + 1)]
        right = [Pi(x + 1, y, z), Pi(x + 1, y + 1, z), Pi(x + 1, y + 1, z + 1), Pi(x + 1, y, z + 1)]
        polys.append((top, left, right))
        allp += top + left + right
    for t in spec.get('texts', []):
        px, py = Pi(*t['at'])
        allp += [(px + t.get('dx', 0) - 30, py + t.get('dy', 0) - 14), (px + t.get('dx', 0) + 30, py + t.get('dy', 0) + 10)]
    xs, ys = [p[0] for p in allp], [p[1] for p in allp]
    x0, y0 = min(xs) - 8, min(ys) - 8
    Wd, H = max(xs) - x0 + 8, max(ys) - y0 + 8
    out = []
    mark = spec.get('mark', 'right')
    f = lambda pp, fill: f'<polygon points="{" ".join(f"{a - x0:.1f},{b - y0:.1f}" for a, b in pp)}" fill="{fill}" stroke="{NAVY}" stroke-width="2.4" stroke-linejoin="round"/>'
    for top, left, right in polys:
        out.append(f(left, SKY)); out.append(f(right, YEL if mark == 'right' else SKY)); out.append(f(top, SOFT))
    for t in spec.get('texts', []):
        px, py = Pi(*t['at'])
        out.append(_t(px - x0 + t.get('dx', 0), py - y0 + t.get('dy', 0) + 7, t['t'], t.get('size', 20)))
    return F._wrap(''.join(out), round(Wd, 1), round(H, 1), spec.get('alt', 'cubes'), round(Wd / U, 1))


FIGS = {'l5_solid': solid, 'l5_cubes': cubes}
