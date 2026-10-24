"""Optional REAL-IMAGE money art (variant held for owner review; NOT used in the booklets).
Loaded only when MONEY_ART=real is set in the environment; the generators' default path never imports this file.
Coins and notes are the prepared greyscale versions of official MAS images (see prep_assets.py, ../source_mas/SOURCES.md)."""
import base64, os
HERE = os.path.dirname(os.path.abspath(__file__))
NOTE_SCALE = float(os.environ.get("MONEY_NOTE_SCALE", "0.30"))   # printed size of a note as a fraction of the real note (must be <= 0.60)
COIN_SCALE = 0.80                                                  # same as the booklets: coin drawn at 0.80 of real diameter
assert NOTE_SCALE <= 0.60
_cache = {}
def _uri(name):
    if name not in _cache:
        _cache[name] = "data:image/png;base64," + base64.b64encode(open(os.path.join(HERE, "assets", name), "rb").read()).decode()
    return _cache[name]
def _px(name):
    from PIL import Image
    return Image.open(os.path.join(HERE, "assets", name)).size

def coin(v, cx, cy, d):
    """coin value v (5,10,20,50,100) centred at cx,cy with printed diameter d (mm); the numerals are kept as invisible text so the generators' independent readers still work"""
    lab = str(v) if v < 100 else "$1"
    return (f'<g class="coin" data-v="{v}"><image href="{_uri(f"coin_{v}.png")}" x="{cx-d/2:.2f}" y="{cy-d/2:.2f}" width="{d:.2f}" height="{d:.2f}" preserveAspectRatio="xMidYMid meet"/>'
            f'<text class="coinval" x="{cx:.1f}" y="{cy:.1f}" opacity="0" font-size="1">{lab}</text></g>')

def note(v, x, y, real_w, real_h):
    """note v ($2,$5,$10) with its top-left at x,y; width = real width x NOTE_SCALE, height from the MAS image's own aspect (proportional); returns (svg, w, h)"""
    name = f"note_{v}.png"; pw, ph = _px(name)
    w = real_w * NOTE_SCALE; h = w * ph / pw
    return (f'<g class="note" data-v="{v}"><image href="{_uri(name)}" x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" height="{h:.2f}" preserveAspectRatio="none"/><rect x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" height="{h:.2f}" fill="none" stroke="#000" stroke-width="0.3"/>'
            f'<text class="noteval" x="{x:.1f}" y="{y+1:.1f}" opacity="0" font-size="1">${v}</text></g>', w, h)
