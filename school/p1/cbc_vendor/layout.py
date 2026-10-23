"""Label layout: tokens, content size from real font metrics, fitting a label into the candidate boxes of a region,
and SVG output. All units are canvas mm (1 unit = 1 printed mm).
A text line is made of tokens: plain text, the blank box, a teacher answer (between the answer brackets) and a stacked fraction
written <numerator|denominator> whose parts are digits, the blank box or an answer."""
import html, re
import metrics
from banks import BOX
ANS_L, ANS_R = "⟦", "⟧"
FRL, FRR = "⟨", "⟩"
F_MAX, F_MIN, F_MIN_TEACHER = 4.9, 4.2, 3.4
LH = 1.22                                   # line height in em
LH_FRAC = 2.2                               # a line that holds a stacked fraction (numerator, bar, denominator)
FRAC_SCALE = 0.84                           # numerals of a stacked fraction relative to the line font size
PAD_W, PAD_H = 0.6, 0.2
BOX_SIDE = 6.0                              # the blank box a pupil writes in: a square at least 6 mm wide (audit 3, F-new 14); a blank inside a stacked fraction stays smaller
BOX_GAP = 0.9                               # space around it in a line
_TOK = re.compile(f"({FRL}[^{FRR}]*{FRR}|{BOX}|{ANS_L}[^{ANS_R}]*{ANS_R})")

def tokens(s):
    """-> list of (kind, text, source): kind box / ans / t / frac (text = (numerator token, denominator token))"""
    out = []
    for part in _TOK.split(s):
        if not part: continue
        if part == BOX: out.append(("box", "", part))
        elif part.startswith(ANS_L): out.append(("ans", part[1:-1], part))
        elif part.startswith(FRL):
            n, d = part[1:-1].split("|")
            out.append(("frac", (n, d), part))
        else: out.append(("t", part, part))
    return out

def plain(s):
    """a text with stacked fractions written the plain way (1/2) and without answer brackets"""
    return re.sub(f"{FRL}([^|{FRR}]*)\\|([^{FRR}]*){FRR}", r"\1/\2", s).replace(ANS_L, "").replace(ANS_R, "")

def ans_text(text):
    """teacher answer token for a key value written as text; a stacked fraction keeps its two parts as answers"""
    m = re.fullmatch(f"{FRL}(\\d+)\\|(\\d+){FRR}", text)
    return f"{FRL}{ANS_L}{m[1]}{ANS_R}|{ANS_L}{m[2]}{ANS_R}{FRR}" if m else ANS_L + text + ANS_R

def part_width(p, f):
    if p == BOX: return metrics.BOX * f
    if p.startswith(ANS_L): return metrics.width(p[1:-1], f, 700)
    return metrics.width(p, f, 600)

def tok_width(tk, f):
    kind, t = tk[0], tk[1]
    if kind == "box": return BOX_SIDE + BOX_GAP
    if kind == "frac": return max(part_width(p, f * FRAC_SCALE) for p in t) + 1.2
    return metrics.width(t, f, 700 if kind == "ans" else 600)

def line_width(line, f): return sum(tok_width(tk, f) for tk in tokens(line))
def line_height(line, f):
    if FRL in line: return LH_FRAC * f
    return max(LH * f, BOX_SIDE + 0.7) if BOX in line else LH * f

class Content:
    def __init__(self, lines, art=None, layout="stack"):
        self.lines, self.art, self.layout = list(lines), art, layout
    def size(self, f):
        tw = max((line_width(l, f) for l in self.lines), default=0)
        th = sum(line_height(l, f) for l in self.lines)
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

def _text(x, y, t, f, bold, i, src):
    cls = ' class="a"' if bold else ""
    return f'<text{cls} x="{x:.2f}" y="{y:.2f}" style="font-size:{f}px" data-l="{i}" data-t="{html.escape(src, quote=True)}" xml:space="preserve">{html.escape(t)}</text>'

def _part(p, cx, yc, f, i, src, out):
    """one numerator or denominator centred on cx"""
    if p == BOX:
        side = metrics.BOX * f * 0.86
        out.append(f'<rect class="bx" x="{cx - side / 2:.2f}" y="{yc - side / 2 - 0.05:.2f}" width="{side:.2f}" height="{side:.2f}" rx="0.5"/>')
    else:
        ans = p.startswith(ANS_L); t = p[1:-1] if ans else p
        w = part_width(p, f)
        out.append(f'<text{" class=\"a\"" if ans else ""} x="{cx - w / 2:.2f}" y="{yc:.2f}" style="font-size:{f}px" xml:space="preserve">{html.escape(t)}</text>')

def render(content, place, colour_line=None):
    """SVG for one label placed in its box"""
    f, (cx, cy, bw, bh), W, Hh, s = place["f"], place["box"], place["w"], place["h"], place["s"]
    out = []
    x0, y0 = cx - W / 2, cy - Hh / 2
    lines = content.lines
    th = sum(line_height(l, f) for l in lines)
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
    y = ty
    for i, ln in enumerate(lines):
        lh = line_height(ln, f); yc = y + lh / 2; y += lh
        lw = line_width(ln, f)
        x = tx + (tw - lw) / 2
        for tk in tokens(ln):
            kind, t, src = tk
            w = tok_width(tk, f)
            if kind == "box":
                side = BOX_SIDE
                out.append(f'<rect class="bx{" big" if BOX_SIDE > 7 else ""}" data-l="{i}" data-t="{BOX}" x="{x + (w - side) / 2:.2f}" y="{yc - side / 2 - 0.05:.2f}" width="{side:.2f}" height="{side:.2f}" rx="0.5"/>')
            elif kind == "frac":
                ff = f * FRAC_SCALE; mid = x + w / 2; gap = 0.62 * ff
                out.append(f'<g data-l="{i}" data-t="{html.escape(src, quote=True)}">')
                _part(t[0], mid, yc - gap, ff, i, src, out); _part(t[1], mid, yc + gap, ff, i, src, out)
                out.append(f'<line class="fb" x1="{x + 0.3:.2f}" y1="{yc:.2f}" x2="{x + w - 0.3:.2f}" y2="{yc:.2f}"/></g>')
            else:
                out.append(_text(x, yc, t, f, kind == "ans", i, src))
                if kind == "ans":
                    out.append(f'<line class="ul" x1="{x:.2f}" y1="{yc + 0.48 * f:.2f}" x2="{x + w:.2f}" y2="{yc + 0.48 * f:.2f}"/>')
            x += w
    return "".join(out)
