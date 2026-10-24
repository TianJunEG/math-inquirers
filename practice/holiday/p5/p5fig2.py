"""Figures for the Level 5 holiday lessons 3 (Before and After: bar models) and 4 (Triangle Areas: shapes drawn to scale).

Plain inline SVG built with the shared helpers in practice/holiday/hlib.py (viewBox only, so the figure scales to a 390 px phone; the builder lifts the text to at
least 12 px).  Every shape here is drawn from centimetre coordinates (y up), so a figure that is "to scale" in the workbook is to scale here too.
No answer is printed in a question figure; the solution figures are built from the CHECKED values passed in.
"""
import math, os, sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from hlib import svg, T, Ln, Ci, Re, NAVY, YEL, TEAL, WARM, PALE      # noqa: E402,F401

SKY = '#CDE8F7'
GREY = '#44506F'


# ---------------------------------------------------------------- shape helpers (screen coordinates; P() turns centimetres, y up, into screen points)
def P(ox, oy, s):
    return lambda x, y: (round(ox + x * s, 1), round(oy - y * s, 1))


def poly(pts, fill='none', sw=2.6):
    return f'<polygon points="{" ".join(f"{x},{y}" for x, y in pts)}" fill="{fill}" stroke="{NAVY}" stroke-width="{sw}" stroke-linejoin="round"/>'


def dash(p, q, sw=2.2):
    return Ln(p[0], p[1], q[0], q[1], sw, NAVY, '6 4')


def rmark(p, dx, dy, k=12):
    """A little square at the corner p; dx, dy are +1 or -1 (screen directions along the two arms)."""
    x, y = p
    return f'<path d="M{x + dx * k} {y} L{x + dx * k} {y + dy * k} L{x} {y + dy * k}" fill="none" stroke="{NAVY}" stroke-width="2"/>'


def side_label(p, q, cen, text, off=6, size=15, fill=NAVY):
    """A length written beside the side p-q, on the side away from the centre cen, clear of the line."""
    mx, my = (p[0] + q[0]) / 2, (p[1] + q[1]) / 2
    dx, dy = q[0] - p[0], q[1] - p[1]
    d = math.hypot(dx, dy)
    nx, ny = -dy / d, dx / d
    if (mx - cen[0]) * nx + (my - cen[1]) * ny < 0:
        nx, ny = -nx, -ny
    hw, hh = len(text) * size * 0.31, size * 0.5
    dist = off + hw * abs(nx) + hh * abs(ny)
    return T(round(mx + nx * dist, 1), round(my + ny * dist + size * 0.35, 1), text, size, 'middle', 700, fill)


def centroid(pts):
    return (sum(p[0] for p in pts) / len(pts), sum(p[1] for p in pts) / len(pts))


# ---------------------------------------------------------------- lesson 4 figures
def q1a():
    f = P(50, 190, 27)
    a, b, c = f(0, 0), f(8, 0), f(0, 6)
    body = poly([a, b, c], YEL) + rmark(a, 1, -1)
    body += T((a[0] + b[0]) / 2, a[1] + 26, '8 cm', 16) + T(a[0] - 8, (a[1] + c[1]) / 2 + 5, '6 cm', 16, 'end')
    body += side_label(c, b, centroid([a, b, c]), '10 cm', 8, 16)
    return svg(330, 226, body, 'Triangle (a), drawn to scale: a right-angled triangle with sides 8 cm, 6 cm and 10 cm. The right angle is at the bottom left.')


def q1b():
    f = P(34, 262, 19)
    a, b, c, foot = f(0, 0), f(14, 0), f(5, 12), f(5, 0)
    body = poly([a, b, c], SKY) + dash(c, foot) + rmark(foot, 1, -1, 11)
    body += T((a[0] + b[0]) / 2, a[1] + 26, '14 cm', 16)
    body += side_label(a, c, centroid([a, b, c]), '13 cm', 8, 16) + side_label(b, c, centroid([a, b, c]), '15 cm', 8, 16)
    body += T(foot[0] + 8, (c[1] + foot[1]) / 2 + 6, '12 cm', 16, 'start')
    return svg(330, 298, body, 'Triangle (b), drawn to scale: base 14 cm, slanting sides 13 cm and 15 cm, and a dashed height of 12 cm that meets the base at a right angle (marked with a little square).')


def q1c():
    f = P(24, 190, 19)
    a, b, c, foot = f(0, 0), f(9, 0), f(15, 8), f(15, 0)
    body = dash(b, foot) + dash(c, foot) + poly([a, b, c], YEL) + rmark(foot, -1, -1, 11)
    body += T((a[0] + b[0]) / 2, a[1] + 26, '9 cm', 16)
    body += side_label(a, c, (b[0], b[1] + 30), '17 cm', 8, 16)
    body += T(foot[0] + 8, (c[1] + foot[1]) / 2 + 6, '8 cm', 16, 'start')
    return svg(380, 228, body, 'Triangle (c), drawn to scale: base 9 cm, a long side of 17 cm, and a dashed height of 8 cm that falls outside the triangle on the extended base (dashed). The height meets the extended base at a right angle.')


def rect_tri(px, fill, tag, size=28, with_heights=False):
    """Rectangle ABCD, 10 cm by 6 cm (A top left, B top right, C bottom right, D bottom left), with a point on AB joined to D and C."""
    f = P(58, 40 + 6 * size, size)
    A, B, C, D, Pt = f(0, 6), f(10, 6), f(10, 0), f(0, 0), f(px, 6)
    body = poly([A, B, C, D], 'none', 2.2) + poly([Pt, D, C], fill, 2.8)
    if with_heights:
        foot = f(px, 0)
        body += dash(Pt, foot, 2.4) + rmark(foot, 1, -1, 10)
    body += T(A[0] - 8, A[1] + 5, 'A', 17, 'end') + T(B[0] + 8, B[1] + 5, 'B', 17, 'start') + T(C[0] + 8, C[1] + 5, 'C', 17, 'start') + T(D[0] - 8, D[1] + 5, 'D', 17, 'end')
    body += T(Pt[0], Pt[1] - 10, tag, 17)
    body += T((D[0] + C[0]) / 2, D[1] + 27, '10 cm', 16) + T(D[0] - 10, (A[1] + D[1]) / 2 + 5, '6 cm', 16, 'end')
    return svg(390, 46 + 6 * size + 40, body, f'Rectangle ABCD, 10 cm by 6 cm. The point {tag} is on the top side AB. Triangle {tag}DC is shaded.')


def q2(which):
    return rect_tri({'P': 2, 'Q': 7}[which], {'P': YEL, 'Q': SKY}[which], which)


def q2_both(heights=False):
    return (rect_tri(2, YEL, 'P', 21, heights) + rect_tri(7, SKY, 'Q', 21, heights))


def q3():
    f = P(40, 148, 22)
    A, B, C, D = f(0, 0), f(4, 5), f(14, 0), f(9, -3)
    hb, hd = f(4, 0), f(9, 0)
    body = poly([A, B, C, D], SKY) + Ln(A[0], A[1], C[0], C[1], 2.6) + dash(B, hb) + dash(D, hd) + rmark(hb, 1, -1, 11) + rmark(hd, 1, 1, 11)
    body += T(A[0] - 8, A[1] + 5, 'A', 17, 'end') + T(B[0], B[1] - 10, 'B', 17) + T(C[0] + 8, C[1] + 5, 'C', 17, 'start') + T(D[0], D[1] + 24, 'D', 17)
    body += T(hb[0] + 8, (B[1] + hb[1]) / 2 + 6, '5 cm', 16, 'start') + T(hd[0] + 8, f(0, -1.0)[1] + 6, '3 cm', 16, 'start')
    body += T(C[0] + 6, 26, 'AC = 14 cm', 16, 'end', 800, TEAL)
    return svg(390, 246, body, 'Four-sided figure ABCD with the diagonal AC of 14 cm. The dashed height from B to AC is 5 cm. The dashed height from D to AC is 3 cm.')


def q4(areas=False):
    f = P(58, 38 + 8 * 22, 22)
    A, B, C, D, E, F = f(0, 8), f(12, 8), f(12, 0), f(0, 0), f(4, 8), f(12, 4)
    body = poly([A, B, C, D], 'none', 2.2) + poly([D, E, F], YEL, 2.8)
    body += T(A[0] - 8, A[1] + 5, 'A', 17, 'end') + T(B[0] + 8, B[1] + 5, 'B', 17, 'start') + T(C[0] + 8, C[1] + 5, 'C', 17, 'start') + T(D[0] - 8, D[1] + 5, 'D', 17, 'end')
    body += T(E[0], E[1] - 10, 'E', 17) + T(F[0] + 9, F[1] + 5, 'F', 17, 'start')
    body += T((A[0] + E[0]) / 2, A[1] - 10, '4 cm', 15) + T((E[0] + B[0]) / 2 + 10, B[1] - 10, '8 cm', 15)
    body += T(B[0] + 9, (B[1] + F[1]) / 2 + 5 - 12, '4 cm', 15, 'start') + T(F[0] + 9, (F[1] + C[1]) / 2 + 5 + 16, '4 cm', 15, 'start')
    body += T(A[0] - 10, (A[1] + D[1]) / 2 + 5, '8 cm', 15, 'end') + T((D[0] + C[0]) / 2, D[1] + 26, '12 cm', 16)
    if areas:
        body += T(*(f(1.35, 5.2)), '16', 15, 'middle', 800, TEAL) + T(*(f(9.4, 6.4)), '16', 15, 'middle', 800, TEAL) + T(*(f(8.0, 1.1)), '24', 15, 'middle', 800, TEAL)
        body += T(*(f(5.4, 3.9)), '40', 17, 'middle', 800, WARM)
    return svg(390, 274, body, 'Rectangle ABCD, 12 cm by 8 cm. E is on the top side AB with AE 4 cm and EB 8 cm. F is on the right side BC with BF 4 cm and FC 4 cm. Triangle DEF is shaded.')


def tri_right(legh, legv, hyp, s, fill=SKY):
    """A right-angled triangle with the right angle at the bottom left; legh along the bottom, legv up the left."""
    f = P(64, 24 + legv * s, s)
    a, b, c = f(0, 0), f(legh, 0), f(0, legv)
    body = poly([a, b, c], fill) + rmark(a, 1, -1, 12)
    body += T((a[0] + b[0]) / 2, a[1] + 26, f'{legh} cm', 16) + T(a[0] - 8, (a[1] + c[1]) / 2 + 5, f'{legv} cm', 16, 'end')
    body += side_label(c, b, centroid([a, b, c]), f'{hyp} cm', 8, 16)
    return body, int(legv * s + 24 + 40)


def a2():
    body, h = tri_right(16, 12, 20, 16)
    return svg(340, h, body, 'A right-angled triangle. The two short sides are 12 cm and 16 cm and the long side is 20 cm. The right angle is at the bottom left.')


def a3():
    s = 17
    f = P(24, 28 + 8 * s, s)
    sq = [f(0, 0), f(6, 0), f(6, 6), f(0, 6)]
    g = P(24 + 6 * s + 36, 28 + 8 * s, s)
    ta, tb, tc, foot = g(0, 0), g(9, 0), g(3, 7), g(3, 0)
    body = poly(sq, YEL) + T(*f(3, 3.4), 'square', 15, 'middle', 700) + T(*f(3, -1.5), '6 cm', 16)
    body += poly([ta, tb, tc], SKY) + dash(tc, foot) + rmark(foot, 1, -1, 10) + T((ta[0] + tb[0]) / 2, ta[1] + 26, '9 cm', 16)
    body += T(foot[0] + 8, g(0, 2.2)[1] + 5, 'height ?', 16, 'start')
    body += T(24, 28 + 8 * s + 52, 'The square and the triangle have the same area.', 14, 'start', 600, GREY) + T(24, 28 + 8 * s + 70, 'Not to scale.', 14, 'start', 600, GREY)
    return svg(390, 28 + 8 * s + 84, body, 'A square with sides of 6 cm and a triangle with a base of 9 cm and a dashed height that is not known. The square and the triangle have the same area. Not drawn to scale.')


def a4():
    s = 17
    body = ''
    f = P(54, 20 + 7 * s, s)
    R = [f(0, 0), f(12, 0), f(12, 7), f(0, 7)]
    body += poly(R, YEL) + T(*f(6, -1.5), '12 cm', 16) + T(R[0][0] - 8, (R[0][1] + R[3][1]) / 2 + 5, '7 cm', 16, 'end') + T(*f(6, 3.2), 'rectangle', 15, 'middle', 700)
    oy = 20 + 7 * s + 62
    g = P(54, oy + 7 * s, s)
    ta, tb, tc, foot = g(0, 0), g(12, 0), g(4, 7), g(4, 0)
    body += poly([ta, tb, tc], SKY) + dash(tc, foot) + rmark(foot, 1, -1, 10) + T((ta[0] + tb[0]) / 2, ta[1] + 26, '12 cm', 16)
    body += T(foot[0] + 8, (tc[1] + foot[1]) / 2 + 5, '7 cm', 16, 'start') + T(g(8, 5)[0], g(8, 5)[1], 'triangle', 15, 'start', 700)
    return svg(340, oy + 7 * s + 40, body, 'A rectangle 12 cm by 7 cm above a triangle with the same base, 12 cm, and the same height, 7 cm. The height of the triangle is a dashed line meeting the base at a right angle.')


def b1():
    body, h = tri_right(20, 15, 25, 12.5)
    return svg(340, h, body, 'A right-angled triangle. The two short sides are 15 cm and 20 cm and the long side is 25 cm. The right angle is at the bottom left.')


def b2(small=6):
    s = 17
    f = P(24, 24 + 10 * s, s)
    big = [f(0, 0), f(10, 0), f(10, 10), f(0, 10)]
    sm = [f(10, 0), f(10 + small, 0), f(10 + small, small), f(10, small)]
    tri = [f(0, 0), f(10, 10), f(10 + small, small)]
    body = poly(big, 'none', 2.2) + poly(sm, 'none', 2.2) + poly(tri, YEL, 2.8)
    body += T(*f(5, -1.5), '10 cm', 16) + T(*f(10 + small / 2, -1.5), f'{small} cm', 16)
    return svg(380, 24 + 10 * s + 40, body, f'Two squares side by side on a line, touching: a big square of side 10 cm and a small square of side {small} cm. A shaded triangle joins the bottom-left corner of the big square, the top-right corner of the big square and the top-right corner of the small square.')


def b3():
    f = P(34, 250, 24)
    B, C, A, D = f(0, 0), f(12, 0), f(5, 9), f(4, 0)
    body = poly([B, C, A], SKY) + Ln(A[0], A[1], D[0], D[1], 2.6)
    body += T(B[0] - 8, B[1] + 5, 'B', 17, 'end') + T(C[0] + 8, C[1] + 5, 'C', 17, 'start') + T(A[0], A[1] - 10, 'A', 17) + T(D[0], D[1] + 22, 'D', 17)
    body += T((B[0] + D[0]) / 2, B[1] + 46, '4 cm', 16) + T((D[0] + C[0]) / 2, C[1] + 46, '8 cm', 16)
    return svg(350, 306, body, 'Triangle ABC with D on the side BC. BD is 4 cm and DC is 8 cm. A is joined to D.')


def inv_line(h=3):
    """Investigation (b), solution: the base is 4 cm, the top corner can be anywhere on the dashed line 3 cm above it."""
    s = 34
    f = P(30, 30 + h * s + 6, s)
    a, b = f(0, 0), f(4, 0)
    body = Ln(f(-0.6, h)[0], f(-0.6, h)[1], f(6.6, h)[0], f(6.6, h)[1], 2.4, TEAL, '8 5')
    for x in (0.0, 2.0, 5.0):
        body += poly([a, b, f(x, h)], 'none' if x != 2.0 else YEL, 2.2)
    for x in (0.0, 2.0, 5.0):
        p = f(x, h)
        body += Ci(p[0], p[1], 5, WARM, NAVY, 1.6)
    body += T((a[0] + b[0]) / 2, a[1] + 26, 'base 4 cm', 16) + T(f(6.6, h)[0], f(6.6, h)[1] - 10, f'{h} cm above the base', 15, 'end', 800, TEAL)
    return svg(330, 30 + h * s + 6 + 40, body, 'A base of 4 cm along the bottom and a dashed line 3 cm above it, parallel to the base. Three different triangles on the base have their top corner on the dashed line. Every one has an area of 6 square centimetres.')


# ---------------------------------------------------------------- lesson 3 figures (bar models)
def cell_row(x, y, cw, h, n, fills, labels=None, size=14):
    out = ''
    for k in range(n):
        out += Re(x + k * cw, y, cw, h, fills[k] if isinstance(fills, list) else fills, NAVY, 2.2)
        if labels and labels[k]:
            out += T(x + (k + 0.5) * cw, y + h / 2 + 5, labels[k], size, 'middle', 700)
    return out


def brace(x1, x2, y, text, up=True, size=15, fill=NAVY):
    d = -1 if up else 1
    path = f'<path d="M{x1} {y} V{y + d * 8} H{x2} V{y}" fill="none" stroke="{fill}" stroke-width="2.4"/>'
    ty = y + d * 14 if up else y + d * 24
    return path + T((x1 + x2) / 2, ty, text, size, 'middle', 800, fill)


def after_model():
    x0, cw, h = 62, 48, 34
    body = T(6, 18, 'After Siti gave Mei 12 stickers:', 15, 'start', 800, TEAL)
    body += T(x0 - 8, 58, 'Siti', 15, 'end') + cell_row(x0, 34, cw, h, 3, YEL) + T(x0 + 3 * cw + 8, 57, '3 units', 14, 'start', 700, GREY)
    body += T(x0 - 8, 106, 'Mei', 15, 'end') + cell_row(x0, 82, cw, h, 4, SKY) + T(x0 + 4 * cw + 8, 105, '4 units', 14, 'start', 700, GREY)
    return svg(340, 126, body, 'The After model. Siti has 3 equal units and Mei has 4 equal units, all the same size.')


def sol_swap(siti_before, mei_before, gift):
    """Solution picture, built from the checked numbers: Before and After bars with the same unit."""
    siti_after, mei_after = siti_before - gift, mei_before + gift
    # the units are the After parts: Siti 3, Mei 4
    unit = siti_after // 3
    assert siti_after == 3 * unit and mei_after == 4 * unit
    cw, x0, h = 30, 62, 28
    n = lambda v: v // unit
    body = T(6, 16, 'Before', 15, 'start', 800, TEAL)
    body += T(x0 - 8, 44, 'Siti', 15, 'end') + cell_row(x0, 24, cw, h, n(siti_before), YEL) + T(x0 + n(siti_before) * cw + 8, 43, str(siti_before), 15, 'start', 800)
    body += T(x0 - 8, 80, 'Mei', 15, 'end') + cell_row(x0, 60, cw, h, n(mei_before), SKY) + T(x0 + n(mei_before) * cw + 8, 79, str(mei_before), 15, 'start', 800)
    body += T(6, 120, 'After (12 moved from Siti to Mei)', 15, 'start', 800, TEAL)
    body += T(x0 - 8, 148, 'Siti', 15, 'end') + cell_row(x0, 128, cw, h, n(siti_after), YEL) + T(x0 + n(siti_after) * cw + 8, 147, str(siti_after), 15, 'start', 800)
    body += T(x0 - 8, 184, 'Mei', 15, 'end') + cell_row(x0, 164, cw, h, n(mei_after), SKY) + T(x0 + n(mei_after) * cw + 8, 183, str(mei_after), 15, 'start', 800)
    body += T(6, 214, f'1 unit = ${unit}', 15, 'start', 800, WARM)
    return svg(340, 224, body, f'Before: Siti {siti_before} stickers, Mei {mei_before} stickers. After: Siti {siti_after}, Mei {mei_after}. One unit is {unit} stickers.')


def sol_ravi(total, book, pen, left):
    """Q1 solution: the bar cut into 6 equal units: book 2, pen 1, left 3."""
    unit = total // 6
    assert book == 2 * unit and pen == unit and left == 3 * unit
    x0, cw, h = 14, 52, 38
    body = brace(x0, x0 + 6 * cw, 36, f'${total} at first', True, 16)
    body += cell_row(x0, 44, cw, h, 6, [SKY, SKY, YEL, '#fff', '#fff', '#fff'], ['', '', '', '', '', ''])
    body += T(x0 + cw, 44 + h + 22, 'book', 15, 'middle', 800) + T(x0 + cw, 44 + h + 40, f'${book}', 15, 'middle', 800, TEAL)
    body += T(x0 + 2.5 * cw, 44 + h + 22, 'pen', 15, 'middle', 800) + T(x0 + 2.5 * cw, 44 + h + 40, f'${pen}', 15, 'middle', 800, TEAL)
    body += T(x0 + 4.5 * cw, 44 + h + 22, 'left', 15, 'middle', 800) + T(x0 + 4.5 * cw, 44 + h + 40, f'${left}', 15, 'middle', 800, TEAL)
    return svg(340, 44 + h + 54, body, f'A bar cut into 6 equal units for ${total}. The book is 2 units (${book}), the pen is 1 unit (${pen}) and 3 units (${left}) are left.')


def fig_a1():
    x0, cw, h = 20, 75, 36
    body = brace(x0, x0 + 4 * cw, 30, '? at first', True, 16)
    body += cell_row(x0, 38, cw, h, 4, [YEL, SKY, SKY, SKY], ['Mon', '', 'remainder', ''], 13)
    y2 = 38 + h + 30
    body += dash((x0 + cw, 38 + h), (x0 + cw, y2), 1.8) + dash((x0 + 4 * cw, 38 + h), (x0 + 4 * cw, y2), 1.8)
    rw = 3 * cw / 5
    for k in range(5):
        body += Re(x0 + cw + k * rw, y2, rw, h, YEL if k < 2 else '#fff', NAVY, 2.2)
    body += T(x0 + cw + rw, y2 + h + 20, 'Tue', 15, 'middle', 800) + T(x0 + cw + 3.5 * rw, y2 + h + 20, 'left', 15, 'middle', 800)
    return svg(340, y2 + h + 30, body, 'Ravi\'s money as a bar cut into 4 equal parts. Monday takes the first part. The other 3 parts are the remainder; below, the remainder is cut into 5 equal pieces. Tuesday takes 2 of the 5 pieces and the other 3 pieces are left.')


def sol_a1(total, mon, tue, left, spent):
    unit = spent // 11
    x0, cw, h = 10, 16, 36
    body = brace(x0, x0 + 20 * cw, 34, f'20 units = ${total}', True, 16)
    fills = [YEL] * 5 + [SKY] * 6 + ['#fff'] * 9
    body += cell_row(x0, 42, cw, h, 20, fills)
    body += T(x0 + 2.5 * cw, 42 + h + 20, 'Mon', 14, 'middle', 800) + T(x0 + 2.5 * cw, 42 + h + 36, '5 units', 14, 'middle', 700, GREY)
    body += T(x0 + 8 * cw, 42 + h + 20, 'Tue', 14, 'middle', 800) + T(x0 + 8 * cw, 42 + h + 36, '6 units', 14, 'middle', 700, GREY)
    body += T(x0 + 15.5 * cw, 42 + h + 20, 'left', 14, 'middle', 800) + T(x0 + 15.5 * cw, 42 + h + 36, '9 units', 14, 'middle', 700, GREY)
    body += brace(x0, x0 + 11 * cw, 42 + h + 52, f'11 units = ${spent}', False, 15, WARM)
    body += T(x0 + 14 * cw, 42 + h + 82, f'1 unit = ${unit}', 15, 'middle', 800, WARM)
    return svg(340, 42 + h + 96, body, f'A bar cut into 20 equal units for ${total}. Monday is 5 units, Tuesday is 6 units and 9 units are left. 11 units are the ${spent} spent, so 1 unit is ${unit}.')


def fig_a4():
    xn, u, h, y1, y2 = 56, 92, 34, 50, 116
    body = T(xn - 8, y1 + 22, 'Ben', 15, 'end') + Re(xn, y1, u, h, YEL) + T(xn + u / 2, y1 + 22, 'spent half', 14) + Re(xn + u, y1, u, h, '#fff') + T(xn + 1.5 * u, y1 + 22, 'left', 14)
    body += T(xn - 8, y2 + 22, 'Siti', 15, 'end') + Re(xn + u, y2, u, h, '#fff') + T(xn + 1.5 * u, y2 + 22, 'left', 14) + Re(xn + 2 * u, y2, 44, h, SKY) + T(xn + 2 * u + 22, y2 + 22, '$20', 14)
    body += dash((xn + u, y1 + h), (xn + u, y2), 1.8) + dash((xn + 2 * u, y1 + h), (xn + 2 * u, y2), 1.8)
    body += T(10, 16, 'Not to scale.', 14, 'start', 600, GREY) + T(10, 32, 'The two "left" parts are equal.', 14, 'start', 600, GREY)
    body += T(10, y2 + h + 28, 'Ben and Siti had $140 altogether.', 15, 'start', 800)
    return svg(350, y2 + h + 40, body, 'Not to scale. Ben\'s bar: half spent, half left. Siti\'s bar: an amount left, equal to Ben\'s left part, and $20 spent. Ben and Siti had $140 altogether.')


def fig_b1():
    xn, lw, pw, h, y1, y2 = 56, 86, 66, 34, 50, 112
    body = T(xn - 8, y1 + 22, 'Mei', 15, 'end') + Re(xn, y1, lw, h, '#fff') + T(xn + lw / 2, y1 + 22, 'left', 14)
    body += cell_row(xn + lw, y1, pw, h, 3, YEL, ['1 part', '1 part', '1 part'], 14)
    body += T(xn - 8, y2 + 22, 'Siti', 15, 'end') + Re(xn, y2, lw, h, '#fff') + T(xn + lw / 2, y2 + 22, 'left', 14)
    body += Re(xn + lw, y2, pw, h, SKY) + T(xn + lw + pw / 2, y2 + 22, '1 part', 14)
    body += dash((xn + lw, y1 + h), (xn + lw, y2), 1.8)
    body += T(10, 16, 'Not to scale.', 14, 'start', 600, GREY) + T(10, 32, 'The two "left" parts are equal.', 14, 'start', 600, GREY)
    return svg(350, y2 + h + 14, body, 'Not to scale. Mei\'s bar: an amount left and 3 equal parts spent. Siti\'s bar: the same amount left and 1 part spent.')
