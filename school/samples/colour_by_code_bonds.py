"""Sample colour-by-code worksheet: Primary 1 number bonds to 10 (school edition, black-and-white print; pupils colour it).
Self-checks: (1) a tally of squares per colour is printed, (2) the picture must be the same on the left and right (mirror).
Run: python3 colour_by_code_bonds.py [--school "School name"]; writes out/*.html, *.pdf, verification.json"""
import argparse, html, json, os, itertools

# 6 x 6 picture. '.' = background (leave white). Digits are the ANSWER of the number-bond question in that square.
PIC = [
    "..22..",
    ".2112.",
    ".3553.",
    ".3553.",
    "433334",
    "4.11.4",
]
COLOURS = {1: "yellow", 2: "red", 3: "blue", 4: "green", 5: "orange"}

def question(a, k):
    b = 10 - a
    forms = [f"{b} + &#9633; = 10", f"&#9633; + {b} = 10", f"10 &minus; {b} = &#9633;", f"10 = {b} + &#9633;", f"10 &minus; &#9633; = {b}"]
    return forms[k % len(forms)]

def cells():
    out = []; k = 0
    for r, row in enumerate(PIC):
        for c, ch in enumerate(row):
            if ch != ".":
                out.append((r, c, int(ch), k)); k += 1
    return out

def tally():
    t = {v: 0 for v in COLOURS}
    for _, _, a, _ in cells(): t[a] += 1
    return t

def verify():
    cs = cells(); rep = {"cells": len(cs), "tally": {COLOURS[v]: n for v, n in tally().items()}}
    # mirror check on the picture itself
    rep["mirror_ok"] = all(row == row[::-1] for row in PIC)
    # every question evaluates to its answer
    import re
    ok = True
    for r, c, a, k in cs:
        q = html.unescape(question(a, k)).replace("−", "-")
        lhs, rhs = q.split("=")
        for guess in [a]:
            expr = (lhs + "==" + rhs).replace("□", str(guess)).replace("=", "==", 0)
            ok &= bool(eval(expr.replace("====", "==")))
        # uniqueness over 0..10
        sols = [g for g in range(0, 11) if eval((lhs + "==" + rhs).replace("□", str(g)))]
        ok &= sols == [a]
    rep["questions_correct_and_unique"] = bool(ok)
    # single-slip detection: change one square's answer to any wrong value 0..10; detected if colour tally differs, mirror breaks, or no colour exists
    det = tot = 0
    base = tally()
    for r, c, a, k in cs:
        for w in range(0, 11):
            if w == a: continue
            tot += 1
            if w not in COLOURS: det += 1; continue            # no colour in the key: pupil notices
            t = dict(base); t[a] -= 1; t[w] += 1
            row = list(PIC[r]); row[c] = str(w)
            mirror = all(("".join(row) if i == r else PIC[i]) == ("".join(row) if i == r else PIC[i])[::-1] for i in range(len(PIC)))
            if t != base or not mirror: det += 1
    rep["single_slip_detected"] = det; rep["single_slip_total"] = tot; rep["single_slip_rate"] = round(det / tot, 4)
    return rep

FONT = "../../../fonts/node_modules/@fontsource"
CSS = """
@font-face{font-family:'Fredoka';font-weight:600;src:url('FONT/fredoka/files/fredoka-latin-600-normal.woff2') format('woff2')}
@font-face{font-family:'Fredoka';font-weight:700;src:url('FONT/fredoka/files/fredoka-latin-700-normal.woff2') format('woff2')}
@font-face{font-family:'Nunito Sans';font-weight:400;src:url('FONT/nunito-sans/files/nunito-sans-latin-400-normal.woff2') format('woff2')}
@font-face{font-family:'Nunito Sans';font-weight:800;src:url('FONT/nunito-sans/files/nunito-sans-latin-800-normal.woff2') format('woff2')}
@page{size:A4;margin:0}*{box-sizing:border-box}
html,body{margin:0;background:#fff;color:#000;font-family:'Nunito Sans',Arial,sans-serif}
.page{width:210mm;height:297mm;padding:14mm 15mm;display:flex;flex-direction:column;overflow:hidden;break-after:page}
header{display:flex;align-items:center;gap:4mm;border-bottom:0.8mm solid #000;padding-bottom:2.5mm}
h1{font-family:'Fredoka';font-weight:600;font-size:25pt;margin:0;flex:1;line-height:1.05}
.nm{font-size:11pt;line-height:1.9;text-align:right;white-space:nowrap}.nm span{display:inline-block;border-bottom:0.4mm solid #000;width:38mm}
.instr{font-size:14pt;line-height:1.3;margin:3mm 0 2mm}
.key{display:flex;gap:3mm;flex-wrap:wrap;margin:1mm 0 3mm}
.k{border:0.6mm solid #000;border-radius:2mm;padding:1.2mm 3.5mm;font-size:15pt;display:flex;gap:2.5mm;align-items:center}
.k b{font-family:'Fredoka';font-weight:700;font-size:19pt;border-right:0.4mm solid #000;padding-right:2.5mm}
.grid{display:grid;grid-template-columns:repeat(6,29mm);grid-auto-rows:26mm;gap:0;margin:0 auto}
.cell{border:0.5mm solid #000;display:flex;align-items:center;justify-content:center;font-family:'Fredoka';font-weight:600;font-size:14pt;text-align:center;line-height:1.1}
.cell.bg{border:none}
.chk{border:0.8mm solid #000;border-radius:3mm;padding:2.5mm 4mm;margin-top:4mm;font-size:12.5pt;line-height:1.3}
.chk b{font-family:'Fredoka';font-weight:600}
.tl{display:flex;gap:5mm;flex-wrap:wrap;margin-top:1mm;font-size:13pt}
footer{margin-top:auto;display:flex;justify-content:space-between;font-size:8pt;padding-top:2mm}
.a{font-family:'Fredoka';font-weight:700;font-size:17pt;border-bottom:0.5mm solid #000;padding:0 1mm}
"""

def page(school, key=False):
    t = tally()
    keyhtml = "".join(f'<div class="k"><b>{v}</b>{COLOURS[v]}</div>' for v in COLOURS)
    grid = []
    for r, row in enumerate(PIC):
        for c, ch in enumerate(row):
            if ch == ".": grid.append('<div class="cell bg"></div>'); continue
            a = int(ch); k = sum(1 for rr in range(r) for x in PIC[rr] if x != ".") + sum(1 for x in PIC[r][:c] if x != ".")
            q = question(a, k)
            if key: q = q.replace("&#9633;", f'<span class="a">{a}</span>')
            grid.append(f'<div class="cell">{q}</div>')
    tl = "".join(f"<span><b>{COLOURS[v]}</b>: {t[v]} squares</span>" for v in COLOURS)
    title = "Rocket Number Bonds" + (" &ndash; Teacher Answers" if key else "")
    instr = ("Find the missing number in each square. Then colour the square with the colour for that number. Leave the empty squares white."
             if not key else "Answers in the boxes. Colour for each answer shown in the key. Check: left side and right side match.")
    return f"""<div class="page"><header><h1>{title}</h1><div class="nm">Name <span></span><br>Class <span></span></div></header>
<p class="instr">{instr}</p><div class="key">{keyhtml}</div>
<div class="grid">{''.join(grid)}</div>
<div class="chk"><b>Check your work.</b> Your rocket must look the same on the left and on the right. Count your colours:
<div class="tl">{tl}</div></div>
<footer><span>{html.escape(school)}</span><span>Number bonds to 10 &middot; sample page</span></footer></div>"""

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--school", default="School name: ____________________"); ap.add_argument("--out", default=os.path.join(os.path.dirname(__file__), "out")); a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    rep = verify(); json.dump(rep, open(os.path.join(a.out, "verification.json"), "w"), indent=1); print(rep)
    assert rep["mirror_ok"] and rep["questions_correct_and_unique"] and rep["single_slip_rate"] >= 0.95, "verification failed"
    for name, key in (("pupil", False), ("teacher", True)):
        doc = f"<!doctype html><meta charset=utf-8><style>{CSS.replace('FONT', FONT)}</style>{page(a.school, key)}"
        p = os.path.join(a.out, f"colour_by_code_bonds_{name}.html"); open(p, "w").write(doc)
        from playwright.sync_api import sync_playwright
        with sync_playwright() as pw:
            b = pw.chromium.launch(); pg = b.new_page(); pg.goto("file://" + os.path.abspath(p)); pg.wait_for_timeout(600)
            pg.pdf(path=p.replace(".html", ".pdf"), prefer_css_page_size=True, print_background=True); b.close()
