"""Inline SVG visuals shared by the deck, guide, workbook and home sheet.

Every function returns an <svg> string that scales to its container (width:100%).
Palette is the project palette (hp/wb_style.css, rebuild/slidekit.py).
"""
import random

NAVY = '#1B2A49'; TEAL = '#1F7A6F'; YEL = '#FFC93C'; SKY = '#DDEBF7'; SOFT = '#FFF0C2'; RED = '#D64545'; GREY = '#8A94AD'
FONT = "Fredoka, 'Nunito Sans', Arial, sans-serif"


def _stick(x, y, h=62, w=6, fill=YEL):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="3" fill="{fill}" stroke="{NAVY}" stroke-width="1.6"/>'


def bundles(tens, ones, label=None, style='sticks', stroke_scale=1.0):
    """tens bundles then ones singles, drawn with a band on every ten. style 'kit' draws bars and squares."""
    if style == 'kit':
        return kit_blocks(tens, ones, label)
    bw = 84                      # width of one bundle slot
    ow = 13                      # width of one single slot
    gap = 34 if tens and ones else 0
    width = max(40, tens * bw + gap + ones * ow + 10)
    # wrap long rows of singles: more than 14 singles go on a second line
    rows_ones = 1 if ones <= 14 else 2
    h = 96 + (30 if label else 0) + (70 if rows_ones == 2 else 0)
    parts = []
    x = 6
    for _ in range(tens):
        for i in range(10):
            parts.append(_stick(x + i * 7, 8))
        parts.append(f'<rect x="{x - 4}" y="28" width="78" height="14" rx="6" fill="{TEAL}" stroke="{NAVY}" stroke-width="1.6"/>')
        x += bw
    x += gap
    for i in range(ones):
        if i == 14:
            x = 6 + tens * bw + gap
        yy = 8 if i < 14 else 80
        xx = x + (i % 14) * ow
        parts.append(_stick(xx, yy, h=62, w=6))
    cap = ''
    if label:
        cap = f'<text x="{width / 2}" y="{h - 8}" font-size="26" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="{FONT}">{label}</text>'
    vw = max(width, 14 * ow + 10)
    return f'<svg viewBox="0 0 {vw} {h}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{tens} bundles of ten and {ones} single sticks" style="width:100%;height:auto;display:block">{"".join(parts)}{cap}</svg>'


def kit_blocks(tens, ones, label=None):
    """Base-ten paper: a bar of ten squares is a ten; a square is a one."""
    sq = 26
    parts = []
    y = 6
    for _ in range(tens):
        for i in range(10):
            parts.append(f'<rect x="{6 + i * sq}" y="{y}" width="{sq}" height="{sq}" fill="{SKY}" stroke="{NAVY}" stroke-width="1.8"/>')
        y += sq + 6
    x0 = 6 + 10 * sq + 30
    for i in range(ones):
        parts.append(f'<rect x="{x0 + (i % 5) * (sq + 4)}" y="{6 + (i // 5) * (sq + 4)}" width="{sq}" height="{sq}" fill="{SOFT}" stroke="{NAVY}" stroke-width="1.8"/>')
    h = max(y, 6 + ((ones + 4) // 5) * (sq + 4)) + 4
    w = x0 + 5 * (sq + 4) + 6
    cap = ''
    if label:
        cap = f'<text x="{w / 2}" y="{h + 28}" font-size="24" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="{FONT}">{label}</text>'
        h += 36
    return f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{tens} tens bars and {ones} ones squares" style="width:100%;height:auto;display:block">{"".join(parts)}{cap}</svg>'


def scatter(n, seed=1, w=900, h=420, shape='star'):
    rnd = random.Random(seed)
    pts = []
    tries = 0
    while len(pts) < n and tries < 20000:
        tries += 1
        x, y = rnd.uniform(40, w - 40), rnd.uniform(40, h - 40)
        if all((x - a) ** 2 + (y - b) ** 2 > 78 ** 2 for a, b in pts):
            pts.append((x, y))
    assert len(pts) == n, 'could not place all points'
    out = []
    import math
    for (x, y) in pts:
        r1, r2 = 26, 11
        d = ' '.join(f'{x + (r1 if i % 2 == 0 else r2) * math.sin(i * math.pi / 5):.1f},{y - (r1 if i % 2 == 0 else r2) * math.cos(i * math.pi / 5):.1f}' for i in range(10))
        out.append(f'<polygon points="{d}" fill="{YEL}" stroke="{NAVY}" stroke-width="2.4" stroke-linejoin="round"/>')
    return f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{n} stars scattered" style="width:100%;height:auto;display:block">{"".join(out)}</svg>'


def ten_frame(filled, extra=0):
    cell = 64
    parts = []

    def frame(x0, k):
        for r in range(2):
            for c in range(5):
                x, y = x0 + c * cell, 6 + r * cell
                parts.append(f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" fill="#fff" stroke="{NAVY}" stroke-width="2.4"/>')
                if r * 5 + c < k:
                    parts.append(f'<circle cx="{x + cell / 2}" cy="{y + cell / 2}" r="22" fill="{RED}" stroke="{NAVY}" stroke-width="2"/>')
    frame(6, filled)
    w = 5 * cell + 12
    if extra:
        frame(6 + 5 * cell + 40, extra)
        parts.append(f'<text x="{5 * cell + 26}" y="{6 + cell + 12}" font-size="46" font-weight="700" fill="{NAVY}" font-family="{FONT}">+</text>')
        w = 10 * cell + 52
    return f'<svg viewBox="0 0 {w} {2 * cell + 12}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="ten frame with {filled} counters" style="width:100%;height:auto;display:block">{"".join(parts)}</svg>'


def ten_to_bundle():
    parts = []
    for i in range(10):
        parts.append(_stick(10 + i * 26, 10, h=90, w=10))
    parts.append(f'<text x="290" y="178" font-size="30" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="{FONT}">10 singles</text>')
    parts.append(f'<line x1="330" y1="60" x2="470" y2="60" stroke="{NAVY}" stroke-width="6"/><polygon points="490,60 466,46 466,74" fill="{NAVY}"/>')
    x = 530
    for i in range(10):
        parts.append(_stick(x + i * 11, 10, h=90, w=10))
    parts.append(f'<rect x="{x - 8}" y="40" width="{10 * 11 + 6}" height="22" rx="8" fill="{TEAL}" stroke="{NAVY}" stroke-width="2"/>')
    parts.append(f'<text x="{x + 55}" y="178" font-size="30" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="{FONT}">1 bundle of ten</text>')
    return f'<svg viewBox="0 0 700 200" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="ten single sticks tied into one bundle" style="width:100%;height:auto;display:block">{"".join(parts)}</svg>'


def render_visual(v):
    t = v['type']
    if t == 'bundles':
        return bundles(v['tens'], v['ones'], None, v.get('style', 'sticks'))
    if t == 'scatter':
        return scatter(v['n'], v.get('seed', 1))
    if t == 'ten_frame':
        return ten_frame(v['filled'], v.get('extra', 0))
    if t == 'ten_to_bundle':
        return ten_to_bundle()
    raise ValueError('unknown visual ' + t)


def place_table(tens, ones, big=False, blank=False):
    cls = 'pv big' if big else 'pv'
    t = '' if blank else tens
    o = '' if blank else ones
    return f'<table class="{cls}"><tr><th>Tens</th><th>Ones</th></tr><tr><td>{t}</td><td>{o}</td></tr></table>'


def kit_page_svg():
    """Cut-out sheet: 9 tens bars + 20 ones squares (A4 width)."""
    sq = 62
    parts = []
    y = 40
    parts.append(f'<text x="0" y="22" font-size="22" font-weight="800" fill="{NAVY}" font-family="Nunito Sans, Arial">Tens bars: cut out all 9 (each bar is one ten)</text>')
    for _ in range(9):
        for i in range(10):
            parts.append(f'<rect x="{i * sq + 2}" y="{y}" width="{sq}" height="{sq - 8}" fill="{SKY}" stroke="{NAVY}" stroke-width="2"/>')
        parts.append(f'<rect x="0" y="{y - 3}" width="{10 * sq + 4}" height="{sq - 2}" fill="none" stroke="#777" stroke-width="1.6" stroke-dasharray="7 5"/>')
        y += sq + 6
    y += 22
    parts.append(f'<text x="0" y="{y}" font-size="22" font-weight="800" fill="{NAVY}" font-family="Nunito Sans, Arial">Ones squares: cut out all 20 (each square is one one)</text>')
    y += 16
    for k in range(20):
        x = (k % 10) * sq + 2
        yy = y + (k // 10) * (sq + 4)
        parts.append(f'<rect x="{x}" y="{yy}" width="{sq - 6}" height="{sq - 6}" fill="{SOFT}" stroke="#777" stroke-width="1.6" stroke-dasharray="7 5"/>')
    y += 2 * (sq + 4) + 6
    return f'<svg viewBox="0 0 {10 * sq + 8} {y}" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;display:block">{"".join(parts)}</svg>'
