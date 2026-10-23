#!/usr/bin/env python3
"""Build the gallery: pupil page and teacher-answers page for every worksheet, plus the contact sheet.
   python3 build.py [--school "School name"] [--only CBC-03] [--out out]
Pages are black and white; pupils colour them with their own crayons. Needs: shapely, fonttools+brotli, playwright(chromium), poppler (pdftoppm)."""
import argparse, base64, glob, html, os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import sheet as S
from worksheets import GALLERY

FONTS = os.path.normpath(os.path.join(HERE, "..", "..", "fonts", "node_modules", "@fontsource"))

def slug(spec): return f'{spec["id"]}_{spec["picture"]}_{spec["bank"]}'

def to_pdf(pw_browser, html_path, pdf_path):
    pg = pw_browser.new_page(); pg.goto("file://" + os.path.abspath(html_path)); pg.wait_for_timeout(500)
    pg.pdf(path=pdf_path, prefer_css_page_size=True, print_background=True); pg.close()

def build(out, school="", only=None):
    from playwright.sync_api import sync_playwright
    os.makedirs(os.path.join(out, "html"), exist_ok=True)
    sheets = []
    with sync_playwright() as pw:
        br = pw.chromium.launch()
        for spec in GALLERY:
            if only and spec["id"] != only: continue
            sh = S.make_sheet(spec, school); sheets.append(sh)
            for kind in ("pupil", "teacher"):
                hp = os.path.join(out, "html", f"{slug(spec)}_{kind}.html")
                rel = os.path.relpath(FONTS, os.path.dirname(hp))
                open(hp, "w").write(f"<!doctype html><html><head><meta charset=utf-8><title>{spec['id']} {kind}</title><style>{S.css(rel)}</style></head><body>{S.page_html(sh, kind == 'teacher')}</body></html>")
                to_pdf(br, hp, os.path.join(out, f"{slug(spec)}_{kind}.pdf"))
            print("built", spec["id"], spec["picture"], spec["bank"], "stars", spec["tier"])
        br.close()
    return sheets

def contact_sheet(out, sheets):
    from playwright.sync_api import sync_playwright
    th = os.path.join(out, "html", "thumbs"); os.makedirs(th, exist_ok=True)
    pages = []
    for kind in ("pupil", "teacher"):
        cells = []
        for sh in sheets:
            sp = sh["spec"]; pdf = os.path.join(out, f"{slug(sp)}_{kind}.pdf")
            base = os.path.join(th, f"{slug(sp)}_{kind}")
            subprocess.run(["pdftoppm", "-r", "70", "-png", "-singlefile", "-gray", pdf, base], check=True)
            b64 = base64.b64encode(open(base + ".png", "rb").read()).decode()
            stars = "1 star" if sp["tier"] == 1 else "2 stars"
            cells.append(f'<figure><img src="data:image/png;base64,{b64}"><figcaption><b>{sp["id"]}</b> {html.escape(sh["pic"].title)} &middot; {html.escape(sh["bank"].topic_for(sp["tier"]))} &middot; {stars}</figcaption></figure>')
        pages.append(f'<div class="sheet"><h1>Colour by Code: gallery, {"pupil pages" if kind == "pupil" else "teacher answer pages"}</h1><div class="grid">{"".join(cells)}</div></div>')
    doc = ("<!doctype html><meta charset=utf-8><style>@page{size:A4 landscape;margin:0}*{box-sizing:border-box}html,body{margin:0;background:#fff;font-family:Arial,sans-serif;color:#000}"
           ".sheet{width:297mm;height:210mm;padding:8mm 10mm;page-break-after:always;overflow:hidden}h1{font-size:13pt;margin:0 0 3mm}"
           ".grid{display:grid;grid-template-columns:repeat(5,1fr);gap:3mm 4mm}figure{margin:0}img{width:100%;border:0.3mm solid #000;display:block}"
           "figcaption{font-size:7pt;line-height:1.25;padding-top:0.8mm}</style>" + "".join(pages))
    hp = os.path.join(out, "html", "contact_sheet.html"); open(hp, "w").write(doc)
    with sync_playwright() as pw:
        br = pw.chromium.launch(); to_pdf(br, hp, os.path.join(out, "contact_sheet.pdf")); br.close()

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--school", default=""); ap.add_argument("--only"); ap.add_argument("--out", default=os.path.join(HERE, "out")); a = ap.parse_args()
    sheets = build(a.out, a.school, a.only)
    if not a.only: contact_sheet(a.out, sheets)
