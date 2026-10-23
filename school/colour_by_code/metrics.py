"""Conservative text widths from the real font files (Fredoka 600 / 700), so label fit can be computed without a browser.
Kerning is ignored and every width is inflated by 4 %; the render check in verify.py then measures the real browser output."""
import os
from fontTools.ttLib import TTFont
FONTS = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "fonts", "node_modules", "@fontsource"))
_f = {}
SAFETY = 1.04
def _font(w):
    if w not in _f:
        t = TTFont(os.path.join(FONTS, "fredoka", "files", f"fredoka-latin-{w}-normal.woff2"))
        _f[w] = (t.getBestCmap(), t["hmtx"], t["head"].unitsPerEm)
    return _f[w]
BOX = 0.82                          # blank-box width in em (drawn as a square, not a font glyph)
def width(text, size, weight=600):
    cm, hm, upm = _font(weight)
    tot = 0.0
    for ch in text:
        g = cm.get(ord(ch))
        tot += (hm[g][0] / upm) if g else 0.62          # unknown glyph: generous 0.62 em
    return tot * size * SAFETY
