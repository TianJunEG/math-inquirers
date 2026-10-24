#!/usr/bin/env python3
"""HELD-BACK review sample: original redraw of Singapore coins and notes (style sample).
Drawn from scratch as SVG; not traced from any image. Writes SVG, PDF, PNG and spec.json.
Run: python3 make_sample.py   (needs cairosvg)
"""
import json, math, os
import cairosvg

HERE = os.path.dirname(os.path.abspath(__file__))
COIN_SCALE = 0.80   # same as school/p1, p2 pages (COINS-FIX-SIZE)
NOTE_SCALE = 0.60   # MAS: notes in books must be <= 60% (or >= 150%) of real size

# MAS coin diameters (mm), docs/school_books/coin_note_specs.md
COINS = [("5c", 16.75, "brass"), ("10c", 18.50, "nickel"), ("20c", 21.00, "nickel"),
         ("50c", 23.00, "nickel"), ("$1", 24.65, "bi")]
# Portrait series: size mm (Wikipedia table, MAS Portrait series), colour name
NOTES = [("$2", 126, 63, "purple", "#b9a4d8", "#6b4a9e", "#f1ebfa"),
         ("$5", 133, 66, "green", "#a9d8b0", "#2f8a4a", "#eaf7ec"),
         ("$10", 141, 69, "red", "#f0a6a0", "#c8372f", "#fdeceb"),
         ("$50", 156, 74, "blue", "#a6c8ee", "#2a62a8", "#e8f2fd"),
         ("$100", 162, 77, "orange", "#f6c48a", "#d9791c", "#fdf0df")]

texts = []   # ground truth of every string drawn: (kind, string)
out = []

def T(kind, s, x, y, size, fill="#333", anchor="start", weight="bold", family="DejaVu Sans",
      extra="", opacity=None):
    texts.append((kind, s))
    op = f' opacity="{opacity}"' if opacity else ""
    out.append(f'<text x="{x:.3f}" y="{y:.3f}" font-size="{size:.3f}" fill="{fill}" text-anchor="{anchor}" '
               f'font-weight="{weight}" font-family="{family}" {extra}{op}>{s}</text>')

def add(s): out.append(s)

# ---------------------------------------------------------------- notes
def note(x, y, key):
    d, W, H, cname, base, deep, light = next(n for n in NOTES if n[0] == key)
    nid = "n" + d[1:]
    s = NOTE_SCALE
    add(f'<defs><linearGradient id="g{nid}" x1="0" y1="0" x2="1" y2="0.35">'
        f'<stop offset="0" stop-color="#ffffff"/><stop offset="0.22" stop-color="{light}"/>'
        f'<stop offset="1" stop-color="{base}"/></linearGradient>'
        f'<clipPath id="c{nid}"><rect width="{W}" height="{H}" rx="3.2"/></clipPath></defs>')
    add(f'<g transform="translate({x:.3f} {y:.3f}) scale({s})">')
    # soft shadow
    add(f'<rect x="0.8" y="1.2" width="{W}" height="{H}" rx="3.2" fill="#000" opacity="0.12"/>')
    add(f'<g clip-path="url(#c{nid})">')
    add(f'<rect width="{W}" height="{H}" fill="url(#g{nid})"/>')
    # neutral wave lines (guilloche-like, no text)
    for i in range(7):
        yy = H * (0.10 + 0.085 * i)
        pts = " ".join(f"{(W*0.22 + k*2):.1f},{(yy + 1.6*math.sin(k/6.0 + i)):.2f}"
                       for k in range(int((W*0.42)/2)))
        add(f'<polyline points="{pts}" fill="none" stroke="{deep}" stroke-width="0.35" opacity="0.22"/>')
    # left margin: neutral rosette placeholder (not the coat of arms)
    rx, ry = W*0.105, H*0.34
    for k in range(10):
        add(f'<ellipse cx="{rx:.2f}" cy="{ry-H*0.07:.2f}" rx="{H*0.025:.2f}" ry="{H*0.075:.2f}" fill="{deep}" '
            f'opacity="0.45" transform="rotate({k*36} {rx:.2f} {ry:.2f})"/>')
    add(f'<circle cx="{rx:.2f}" cy="{ry:.2f}" r="{H*0.04:.2f}" fill="{deep}" opacity="0.65"/>')
    # plain dot pattern instead of small print (left margin and under numeral)
    for r in range(3):
        for c in range(6):
            add(f'<circle cx="{W*0.045 + c*W*0.03:.2f}" cy="{H*0.62 + r*H*0.065:.2f}" r="0.7" fill="{deep}" opacity="0.4"/>')
    for k in range(int(W*0.36/2.3)):
        add(f'<circle cx="{W*0.25 + k*2.3:.2f}" cy="{H*0.665:.2f}" r="0.55" fill="{deep}" opacity="0.5"/>')
    # small rounded patch (neutral)
    add(f'<rect x="{W*0.50:.2f}" y="{H*0.20:.2f}" width="{W*0.08:.2f}" height="{H*0.13:.2f}" rx="2" fill="{deep}" opacity="0.18"/>')
    # portrait placeholder: neutral silhouette, no features, no likeness
    fx, fy, fw, fh = W*0.64, H*0.07, W*0.32, H*0.62
    add(f'<clipPath id="p{nid}"><rect x="{fx:.2f}" y="{fy:.2f}" width="{fw:.2f}" height="{fh:.2f}" rx="5"/></clipPath>')
    add(f'<rect x="{fx:.2f}" y="{fy:.2f}" width="{fw:.2f}" height="{fh:.2f}" rx="5" fill="#ffffff" opacity="0.55"/>')
    add(f'<g clip-path="url(#p{nid})">')
    cx = fx + fw/2
    add(f'<circle cx="{cx:.2f}" cy="{fy+fh*0.38:.2f}" r="{fh*0.2:.2f}" fill="{deep}" opacity="0.38"/>')
    add(f'<ellipse cx="{cx:.2f}" cy="{fy+fh*1.02:.2f}" rx="{fw*0.42:.2f}" ry="{fh*0.36:.2f}" fill="{deep}" opacity="0.38"/>')
    add('</g>')
    add(f'<rect x="{fx:.2f}" y="{fy:.2f}" width="{fw:.2f}" height="{fh:.2f}" rx="5" fill="none" stroke="{deep}" stroke-width="0.9"/>')
    # words: SINGAPORE and the numeral
    T("note", "SINGAPORE", W*0.235, H*0.20, H*0.105, deep, extra=f'textLength="{W*0.37:.2f}" lengthAdjust="spacingAndGlyphs"')
    num = d[1:]
    size = H*(0.46 if len(num) < 3 else 0.37)
    T("note", num, W*0.235, H*0.60, size, deep, extra='stroke="#ffffff" stroke-width="1.6" paint-order="stroke" stroke-linejoin="round"')
    # SPECIMEN band across the full width BELOW the portrait area (does not cover it)
    add(f'<rect x="0" y="{H*0.725:.2f}" width="{W}" height="{H*0.2:.2f}" fill="#ffffff" opacity="0.6"/>')
    T("note", "SPECIMEN", W/2, H*0.725 + H*0.15, H*0.15, "#3b2f4f", anchor="middle",
      extra=f'textLength="{W*0.86:.2f}" lengthAdjust="spacingAndGlyphs"', opacity=0.85)
    add('</g>')
    add(f'<rect width="{W}" height="{H}" rx="3.2" fill="none" stroke="{deep}" stroke-width="1.2"/>')
    add(f'<rect x="2" y="2" width="{W-4}" height="{H-4}" rx="2.2" fill="none" stroke="{deep}" stroke-width="0.4" opacity="0.5"/>')
    add('</g>')
    return W*s, H*s

# ---------------------------------------------------------------- coins
def coin(cx, cy, key):
    d, dia, mat = next(c for c in COINS if c[0] == key)
    r = dia * COIN_SCALE / 2
    cid = "k" + d.replace("$", "d")
    if mat == "brass":
        hi, lo, edge, inkc = "#f4dc8a", "#cf9f33", "#8a6414", "#6b4a0c"
    else:
        hi, lo, edge, inkc = "#f6f7f9", "#aab1ba", "#6a727c", "#4b5560"
    add(f'<defs><radialGradient id="r{cid}" cx="0.35" cy="0.3" r="0.85"><stop offset="0" stop-color="{hi}"/>'
        f'<stop offset="1" stop-color="{lo}"/></radialGradient>')
    add(f'<radialGradient id="b{cid}" cx="0.35" cy="0.3" r="0.85"><stop offset="0" stop-color="#f6f7f9"/>'
        f'<stop offset="1" stop-color="#aab1ba"/></radialGradient></defs>')
    add(f'<ellipse cx="{cx+0.5:.2f}" cy="{cy+0.8:.2f}" rx="{r:.2f}" ry="{r:.2f}" fill="#000" opacity="0.14"/>')
    if d == "50c":   # scalloped edge: 12 gentle lobes, maximum radius = r
        pts = []
        for i in range(721):
            a = math.radians(i/2)
            rr = (r - 0.17)*(0.985 + 0.015*math.cos(12*a))
            pts.append(f"{cx+rr*math.cos(a):.3f},{cy+rr*math.sin(a):.3f}")
        add(f'<polygon points="{" ".join(pts)}" fill="url(#r{cid})" stroke="{edge}" stroke-width="0.35"/>')
    else:
        add(f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r="{r - 0.17:.3f}" fill="url(#r{cid})" stroke="{edge}" stroke-width="0.35"/>')
    # edge hint on the face rim
    if d == "10c":    # interrupted reeding: 6 groups with gaps
        for g in range(6):
            for k in range(7):
                a = math.radians(g*60 + k*6.5 + 4)
                add(f'<line x1="{cx+r*0.90*math.cos(a):.2f}" y1="{cy+r*0.90*math.sin(a):.2f}" '
                    f'x2="{cx+r*0.97*math.cos(a):.2f}" y2="{cy+r*0.97*math.sin(a):.2f}" stroke="{edge}" stroke-width="0.22" opacity="0.7"/>')
    elif d in ("20c", "$1"):   # reeded
        for k in range(72):
            a = math.radians(k*5)
            add(f'<line x1="{cx+r*0.91*math.cos(a):.2f}" y1="{cy+r*0.91*math.sin(a):.2f}" '
                f'x2="{cx+r*0.975*math.cos(a):.2f}" y2="{cy+r*0.975*math.sin(a):.2f}" stroke="{edge}" stroke-width="0.2" opacity="0.7"/>')
    if d == "$1":
        # brass outer ring already filled; silver centre disc, inner circle 16 mm of 24.65
        ri = r * 16.0 / 24.65
        add(f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r="{ri:.3f}" fill="url(#b{cid})" stroke="{edge}" stroke-width="0.35"/>')
        add(f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r="{r*0.88:.3f}" fill="none" stroke="{edge}" stroke-width="0.18" opacity="0.5"/>')
        T("coin", "$1", cx, cy + ri*0.36, ri*1.0, inkc, anchor="middle")
    else:
        add(f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r="{r*0.84:.3f}" fill="none" stroke="{edge}" stroke-width="0.18" opacity="0.5"/>')
        num = d[:-1]
        T("coin", num, cx, cy + r*0.12, r*0.78, inkc, anchor="middle")
        T("coin", "CENTS", cx, cy + r*0.58, r*0.27, inkc, anchor="middle")
    return r

# ---------------------------------------------------------------- page
add('<svg xmlns="http://www.w3.org/2000/svg" width="210mm" height="297mm" viewBox="0 0 210 297">')
add('<rect width="210" height="297" fill="#fffaf0"/>')
T("furniture", "Singapore money: style sample", 10, 13, 6.2, "#3b2f4f")
T("furniture", "Original illustration for owner review. Not traced from any image.", 10, 19, 3.1, "#5b5368", weight="normal")
add('<rect x="10" y="22" width="190" height="8" rx="3" fill="#fde2e0" stroke="#c8372f" stroke-width="0.5"/>')
T("furniture", "HELD BACK: not for use in any book until the lawyer answers question 10", 105, 27.3, 3.7, "#9c1f19", anchor="middle")

layout = {"$2": (10, 36), "$5": (108, 36), "$10": (10, 86), "$50": (108, 86), "$100": (10, 138)}
spec = {"coins": [], "notes": [], "coin_scale": COIN_SCALE, "note_scale": NOTE_SCALE}
cap = {"$2": "purple", "$5": "green", "$10": "red", "$50": "blue", "$100": "orange"}
for k, (x, y) in layout.items():
    w, h = note(x, y, k)
    n = next(n for n in NOTES if n[0] == k)
    T("furniture", f"{k} {cap[k]}: {n[1]} x {n[2]} mm real", x, y + h + 4.6, 3.0, "#5b5368", weight="normal")
    spec["notes"].append({"key": k, "x_mm": x, "y_mm": y, "w_mm": w, "h_mm": h, "real_w": n[1], "real_h": n[2],
                          "colour": cap[k], "base": n[4], "deep": n[5]})

# legend block, bottom right of the notes area
lx, ly = 108, 142
for i, line in enumerate(["Pictures are not actual size.",
                          "Notes are drawn at 60% of real size.",
                          "Coins are drawn at 80% of real size.",
                          "Portrait area: neutral placeholder, no likeness.",
                          "Plain dots and lines stand in for small print."]):
    T("furniture", line, lx, ly + i*6, 3.5 if i == 0 else 3.1, "#3b2f4f" if i == 0 else "#5b5368",
      weight="bold" if i == 0 else "normal")

# coin row
radii = [c[1]*COIN_SCALE/2 for c in COINS]
total = sum(2*r for r in radii)
gap = (190 - total) / (len(COINS)-1)
x = 10
cy = 218
for (d, dia, mat), r in zip(COINS, radii):
    cx = x + r
    coin(cx, cy, d)
    T("furniture", f"{d}  {dia:.2f} mm real", cx, cy + 17, 2.9, "#5b5368", anchor="middle", weight="normal")
    spec["coins"].append({"key": d, "cx_mm": cx, "cy_mm": cy, "r_mm": r, "real_dia": dia, "material": mat})
    x += 2*r + gap

for i, line in enumerate([
    "Coins: brass-plated 5c; nickel-plated 10c, 20c, 50c; bi-metallic $1 (brass ring, nickel centre).",
    "Edge hints on the face rim: 5c plain, 10c interrupted reeding, 20c reeded, 50c scalloped, $1 reeded.",
    "Sizes and colours: see README.md. Sheet drawn for review only."]):
    T("furniture", line, 10, 248 + i*5.2, 2.9, "#5b5368", weight="normal")
add('</svg>')

svg = "\n".join(out)
with open(os.path.join(HERE, "coin_note_style_sample.svg"), "w") as f: f.write(svg)
cairosvg.svg2pdf(bytestring=svg.encode(), write_to=os.path.join(HERE, "coin_note_style_sample.pdf"))
cairosvg.svg2png(bytestring=svg.encode(), write_to=os.path.join(HERE, "coin_note_style_sample.png"), dpi=200)
cairosvg.svg2png(bytestring=svg.encode(), write_to=os.path.join(HERE, "_verify_400dpi.png"), dpi=400)
spec["texts"] = texts
with open(os.path.join(HERE, "spec.json"), "w") as f: json.dump(spec, f, indent=1)
print("ok", len(texts), "text strings")
