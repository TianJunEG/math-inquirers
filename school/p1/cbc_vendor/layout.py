"""Label layout: tokens, content size from real font metrics, fitting a label into the candidate boxes of a region,
and SVG output. All units are canvas mm (1 unit = 1 printed mm)."""
import html, re
import metrics
from banks import BOX
ANS_L, ANS_R = "⟦", "⟧"
F_MAX, F_MIN, F_MIN_TEACHER = 4.9, 4.2, 3.4
LH = 1.22                                   # line height in em
PAD_W, PAD_H = 0.6, 0.2

def tokens(s):
    out = []
    for part in re.split(f"({BOX}|{ANS_L}[^{ANS_R}]*{ANS_R})", s):
        if not part: continue
        if part == BOX: out.append(("box", ""))
        elif part.startswith(ANS_L): out.append(("ans", part[1:-1]))
        else: out.append(("t", part))
    return out

def tok_width(tk, f):
    kind, t = tk
    if kind == "box": return metrics.BOX * f
    return metrics.width(t, f, 700 if kind == "ans" else 600)

def line_width(line, f): return sum(tok_width(tk, f) for tk in tokens(line))

class Content:
    def __init__(self, lines, art=None, layout="stack"):
        self.lines, self.art, self.layout = list(lines), art, layout
    def size(self, f):
        tw = max((line_width(l, f) for l in self.lines), default=0)
        th = len(self.lines) * LH * f
        if self.art is None: return tw, th, 1.0
        s = min(1.0, max(self.art.min_scale, f / F_MAX))
        aw, ah = self.art.w * s, self.art.h * s
        if self.layout == "row": return aw + 2.2 + tw, max(ah, th), s
        return max(aw, tw), ah + (1.3 if self.lines else 0) + th, s

def fit(content, boxes, fmax=F_MAX, fmin=F_MIN, ref=None):
    """largest font size (step 0.1) at which the content fits one of the boxes -> dict or None"""
    f = fmax
    while f >= fmin - 1e-9:
        W, Hh, s = content.size(f)
        ok = [b for b in boxes if W <= b[2] - 2 * PAD_W and Hh <= b[3] - 2 * PAD_H]
        if ok:
            b = min(ok, key=(lambda b: (b[0] - ref[0]) ** 2 + (b[1] - ref[1]) ** 2) if ref else (lambda b: b[2] * b[3]))
            return dict(f=round(f, 2), box=b, w=W, h=Hh, s=s)
        f -= 0.1
    return None

def render(content, place, colour_line=None):
    """SVG for one label placed in its box"""
    f, (cx, cy, bw, bh), W, Hh, s = place["f"], place["box"], place["w"], place["h"], place["s"]
    out = []
    x0, y0 = cx - W / 2, cy - Hh / 2
    lines = content.lines
    th = len(lines) * LH * f
    if content.art is None:
        tx, ty, tw = x0, y0, W
    elif content.layout == "row":
        aw, ah = content.art.w * s, content.art.h * s
        out.append(f'<g transform="translate({x0:.2f},{cy - ah / 2:.2f}) scale({s:.3f})">{content.art.svg}</g>')
        tx, ty, tw = x0 + aw + 2.2, cy - th / 2, W - aw - 2.2
    else:
        aw, ah = content.art.w * s, content.art.h * s
        out.append(f'<g transform="translate({cx - aw / 2:.2f},{y0:.2f}) scale({s:.3f})">{content.art.svg}</g>')
        tx, ty, tw = x0, y0 + ah + (1.3 if lines else 0), W
    centred = content.layout != "row"
    for i, ln in enumerate(lines):
        lw = line_width(ln, f)
        x = tx + ((tw - lw) / 2 if centred else (tw - lw) / 2)
        yc = ty + (i + 0.5) * LH * f
        for kind, t in tokens(ln):
            w = tok_width((kind, t), f)
            if kind == "box":
                side = metrics.BOX * f * 0.86
                out.append(f'<rect class="bx" x="{x + (w - side) / 2:.2f}" y="{yc - side / 2 - 0.05:.2f}" width="{side:.2f}" height="{side:.2f}" rx="0.5"/>')
            else:
                cls = ' class="a"' if kind == "ans" else ""
                out.append(f'<text{cls} x="{x:.2f}" y="{yc:.2f}" style="font-size:{f}px" xml:space="preserve">{html.escape(t)}</text>')
                if kind == "ans":
                    out.append(f'<line class="ul" x1="{x:.2f}" y1="{yc + 0.48 * f:.2f}" x2="{x + w:.2f}" y2="{yc + 0.48 * f:.2f}"/>')
            x += w
    return "".join(out)
