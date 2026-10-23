"""Figure types for Level 2 unit 5 (number machines, working backwards).

  l2_machine  one or more number machines drawn as a chain: value box -> operation box(es) -> value box.
              spec: steps [v0, op1, op2, ..., vn] or rows [{label?, steps}].  The first and last entries are value boxes (a number, "?" or None = an empty dashed box);
              the entries between are operation boxes (text such as "x 3", "+ 5", "half" is drawn as written; use the real signs).
Operation boxes have a double border so they differ from value boxes without colour.
"""
import figs as F
from figs_l2_core import T, box, line, wrap, NAVY, SKY, SOFT, YEL


def machine(spec, w=None):
    rows = spec.get('rows') or [{'steps': spec['steps']}]
    VW, OW, H, G = 120, 150, 76, 62
    LW = 70 if any(r.get('label') for r in rows) else 0
    P = []
    maxw = 0
    for ri, r in enumerate(rows):
        steps = r['steps']
        y = 8 + ri * (H + 26)
        x = 6 + LW
        if r.get('label'):
            P.append(T(6 + 24, y + H / 2 + 11, r['label'], 30, anchor='middle'))
        for si, st in enumerate(steps):
            end = si in (0, len(steps) - 1)
            ww = VW if end else OW
            if end:
                if st is None or st == '?':
                    P.append(box(x, y, ww, H, '#fff', dash=True, sw=3.2, rx=10))
                    if st == '?':
                        P.append(T(x + ww / 2, y + H / 2 + 12, '?', 36))
                else:
                    P.append(box(x, y, ww, H, SOFT, sw=3.2, rx=10))
                    P.append(T(x + ww / 2, y + H / 2 + 12, st, 36))
            else:
                P.append(box(x, y, ww, H, SKY, sw=3.4, rx=14))
                P.append(box(x + 7, y + 7, ww - 14, H - 14, 'none', sw=1.8, rx=9))
                P.append(T(x + ww / 2, y + H / 2 + 12, st, 36))
            x += ww
            if si < len(steps) - 1:
                P.append(line(x + 6, y + H / 2, x + G - 12, y + H / 2, 3.6))
                P.append(f'<path d="M{x + G - 8} {y + H / 2} l-16 -10 l0 20z" fill="{NAVY}"/>')
                x += G
        maxw = max(maxw, x)
    Ht = 8 + len(rows) * (H + 26)
    return wrap(P, maxw + 6, Ht, 'number machine', w, 0.2)


FIGS = {'l2_machine': machine}
