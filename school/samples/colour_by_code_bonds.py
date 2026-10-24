"""Sample colour-by-code worksheet: Primary 1 number bonds to 10 (school edition; printed black and white, pupils colour it).
A rocket outline: every region holds a number-bond question; the answer (1 to 5) tells the colour.
Self-checks printed on the page: (1) how many regions of each colour, (2) matching left/right parts must be the same colour.
Run: python3 colour_by_code_bonds.py [--school "School name"]; writes out/*.html, *.pdf, verification.json"""
import argparse, html, json, os, re

COLOURS = {1: "yellow", 2: "red", 3: "blue", 4: "green", 5: "orange"}
# id, SVG shape, label centre (x, y) in mm on a 180 x 200 canvas, answer, mirror partner id (or None)
R = [
 ("nose_l", '<path d="M40,45 C40,20 70,3 90,0 V45 Z"/>', (66, 33), 2, "nose_r"),
 ("nose_r", '<path d="M140,45 C140,20 110,3 90,0 V45 Z"/>', (114, 33), 2, "nose_l"),
 ("top_l", '<path d="M40,45 H90 V70 H40 Z"/>', (65, 58), 3, "top_r"),
 ("top_r", '<path d="M90,45 H140 V70 H90 Z"/>', (115, 58), 3, "top_l"),
 ("mid_l", '<path d="M40,70 H90 A20,20 0 0 0 90,110 H40 Z"/>', (55, 91), 5, "mid_r"),
 ("mid_r", '<path d="M90,70 H140 V110 H90 A20,20 0 0 0 90,70 Z"/>', (125, 91), 5, "mid_l"),
 ("window", '<circle cx="90" cy="90" r="20"/>', (90, 91), 1, None),
 ("bot_l", '<path d="M40,110 H90 V135 H40 Z"/>', (65, 123), 3, "bot_r"),
 ("bot_r", '<path d="M90,110 H140 V135 H90 Z"/>', (115, 123), 3, "bot_l"),
 ("fin_l", '<path d="M40,100 L8,138 V160 L40,135 Z"/>', (25, 133), 2, "fin_r"),
 ("fin_r", '<path d="M140,100 L172,138 V160 L140,135 Z"/>', (155, 133), 2, "fin_l"),
 ("base", '<path d="M52,135 H128 L122,152 H58 Z"/>', (90, 145), 4, None),
 ("flame", '<path d="M58,152 H122 L90,200 Z"/>', (90, 166), 1, None),
 ("planet", '<circle cx="22" cy="35" r="20"/>', (22, 36), 4, None),
 ("moon", '<circle cx="160" cy="35" r="18"/>', (160, 36), 1, None),
]

def form(a, k):
    b = 10 - a
    f = [(f"{b} + □ = 10", f"{b} + {a} = 10"), (f"□ + {b} = 10", f"{a} + {b} = 10"), (f"10 − {b} = □", f"10 − {b} = {a}"),
         (f"10 = {b} + □", f"10 = {b} + {a}"), (f"10 − □ = {b}", f"10 − {a} = {b}")]
    return f[k % len(f)]

def tally():
    t = {v: 0 for v in COLOURS}
    for _, _, _, a, _ in R: t[a] += 1
    return t

def evaluates(text, g):
    lhs, rhs = text.replace("□", str(g)).replace("−", "-").split("=")
    return eval(lhs) == eval(rhs)

def verify():
    ans = {r[0]: r[3] for r in R}
    rep = {"regions": len(R), "tally": {COLOURS[v]: n for v, n in tally().items()}}
    rep["mirror_pairs_same_colour"] = all(ans[i] == ans[p] for i, _, _, _, p in R if p)
    ok = True
    for k, (i, _, _, a, _) in enumerate(R):
        q = form(a, k)[0]
        ok &= [g for g in range(0, 11) if evaluates(q, g)] == [a]
    rep["questions_correct_and_unique"] = bool(ok)
    base = tally(); det = tot = 0
    for i, _, _, a, p in R:
        for w in range(0, 11):
            if w == a: continue
            tot += 1
            if w not in COLOURS: det += 1; continue                       # no colour in the key
            t = dict(base); t[a] -= 1; t[w] += 1
            if t != base or p is not None: det += 1                        # tally changes, or the mirror partner no longer matches
    rep.update(single_slip_detected=det, single_slip_total=tot, single_slip_rate=round(det / tot, 4))
    # the weakest case: regions with no mirror partner rely on the tally alone; the tally always changes when the colour changes
    return rep

FONT = "../../../fonts/node_modules/@fontsource"
CSS = """
@font-face{font-family:'Fredoka';font-weight:600;src:url('FONT/fredoka/files/fredoka-latin-600-normal.woff2') format('woff2')}
@font-face{font-family:'Fredoka';font-weight:700;src:url('FONT/fredoka/files/fredoka-latin-700-normal.woff2') format('woff2')}
@font-face{font-family:'Nunito Sans';font-weight:400;src:url('FONT/nunito-sans/files/nunito-sans-latin-400-normal.woff2') format('woff2')}
@font-face{font-family:'Nunito Sans';font-weight:800;src:url('FONT/nunito-sans/files/nunito-sans-latin-800-normal.woff2') format('woff2')}
@page{size:A4;margin:0}*{box-sizing:border-box}
html,body{margin:0;background:#fff;color:#000;font-family:'Nunito Sans',Arial,sans-serif}
.page{width:210mm;height:297mm;padding:13mm 15mm;display:flex;flex-direction:column;overflow:hidden}
header{display:flex;align-items:center;gap:4mm;border-bottom:0.8mm solid #000;padding-bottom:2mm}
h1{font-family:'Fredoka';font-weight:600;font-size:24pt;margin:0;flex:1;line-height:1.05}
.nm{font-size:11pt;line-height:1.8;text-align:right;white-space:nowrap}.nm span{display:inline-block;border-bottom:0.4mm solid #000;width:38mm}
.instr{font-size:13.5pt;line-height:1.25;margin:2.5mm 0 1.5mm}
.key{display:flex;gap:2.5mm;flex-wrap:wrap;margin:0 0 1mm}
.k{border:0.6mm solid #000;border-radius:2mm;padding:0.8mm 3mm;font-size:14pt;display:flex;gap:2.5mm;align-items:center}
.k b{font-family:'Fredoka';font-weight:700;font-size:18pt;border-right:0.4mm solid #000;padding-right:2.5mm}
svg{display:block;margin:0 auto;width:172mm;height:auto}
svg .r{fill:#fff;stroke:#000;stroke-width:0.9;stroke-linejoin:round}
svg text{font-family:'Fredoka';font-weight:600;font-size:4.9px;text-anchor:middle;dominant-baseline:central;fill:#000}
svg text .a{font-weight:700;font-size:5.2px;text-decoration:underline}
.chk{border:0.8mm solid #000;border-radius:3mm;padding:2mm 4mm;margin-top:1.5mm;font-size:12pt;line-height:1.3}
.chk b{font-family:'Fredoka';font-weight:600}.tl{display:flex;gap:4mm;flex-wrap:wrap;font-size:12pt}
footer{margin-top:auto;display:flex;justify-content:space-between;font-size:8pt;padding-top:1.5mm}
"""

def page(school, key=False):
    t = tally()
    keyhtml = "".join(f'<div class="k"><b>{v}</b>{COLOURS[v]}</div>' for v in COLOURS)
    parts = []
    for k, (i, shape, (x, y), a, _) in enumerate(R):
        q, full = form(a, k)
        label = html.escape(full if key else q)
        if key:
            label = label.replace(str(a), f'<tspan class="a">{a}</tspan>', 1) if False else html.escape(full)
        parts.append(f'<g class="r">{shape}</g><text x="{x}" y="{y}">{label}</text>')
    svg = f'<svg viewBox="0 0 180 200" xmlns="http://www.w3.org/2000/svg">{"".join(parts)}</svg>'
    svg = svg.replace('<g class="r">', '<g class="r" style="fill:#fff">').replace("<path ", "<path class='r' ").replace("<circle ", "<circle class='r' ")
    tl = "".join(f"<span><b>{COLOURS[v]}</b>: {t[v]}</span>" for v in COLOURS)
    title = "Rocket Number Bonds" + (" &ndash; Teacher Answers" if key else "")
    instr = ("Find the missing number in each part of the rocket. Colour the part with the colour for that number."
             if not key else "The missing numbers are shown. Colours: see the key. The two sides of the rocket match.")
    return f"""<div class="page"><header><h1>{title}</h1><div class="nm">Name <span></span><br>Class <span></span></div></header>
<p class="instr">{instr}</p><div class="key">{keyhtml}</div>{svg}
<div class="chk"><b>Check your work.</b> The left and right sides of the rocket must match. Parts of each colour:
<div class="tl">{tl}</div></div>
<footer><span>{html.escape(school)}</span><span>Number bonds to 10 &middot; sample page</span></footer></div>"""

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--school", default="School name: ____________________"); ap.add_argument("--out", default=os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")); a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    rep = verify(); json.dump(rep, open(os.path.join(a.out, "verification.json"), "w"), indent=1); print(rep)
    assert rep["mirror_pairs_same_colour"] and rep["questions_correct_and_unique"] and rep["single_slip_rate"] >= 0.95, "verification failed"
    from playwright.sync_api import sync_playwright
    for name, key in (("pupil", False), ("teacher", True)):
        doc = f"<!doctype html><meta charset=utf-8><style>{CSS.replace('FONT', FONT)}</style>{page(a.school, key)}"
        p = os.path.join(a.out, f"colour_by_code_bonds_{name}.html"); open(p, "w").write(doc)
        with sync_playwright() as pw:
            b = pw.chromium.launch(); pg = b.new_page(); pg.goto("file://" + os.path.abspath(p)); pg.wait_for_timeout(600)
            pg.pdf(path=p.replace(".html", ".pdf"), prefer_css_page_size=True, print_background=True); b.close()
