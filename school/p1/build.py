#!/usr/bin/env python3
"""Build the Primary 1 early-finisher pack.
  python3 build.py [--school "Name of School"] [--outdir out] [--seed-check]
Outputs (in out/): P1_Puzzles.pdf (20 pupil pages), P1_FrontMatter.pdf (5), P1_Complete_Pack.pdf (25),
P1_Answer_Key.pdf, verification.json."""
import argparse, json, os, sys, re, subprocess
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from gen import pages_numbers, pages_arith, pages_measure, pages_cbc
import render

LATER = {3, 5, 6, 12, 13, 15, 16, 17, 18, 19, 20}      # topics usually taught after number work (named in the teacher notes)

def all_pages():
    ps = []
    for m in (pages_numbers, pages_arith, pages_measure, pages_cbc):
        ps += [f() for f in m.PAGES]
    ps.sort(key=lambda p: p["no"])
    for p in ps: p["later"] = p["no"] in LATER
    return ps

def pack_key(pages, school, outdir, capacity_mm=257):
    """Measure every key entry in the browser and pack as many as fit on each key page (no half-empty pages)."""
    from playwright.sync_api import sync_playwright
    tmp = os.path.join(outdir, "keymeasure.html")
    open(tmp, "w").write(render.doc('<section class="page fm" style="height:auto;overflow:visible">' + "".join(render.key_entry(p) for p in pages) + "</section>", "measure"))
    with sync_playwright() as pw:
        br = pw.chromium.launch(); pg = br.new_page(viewport={"width": 900, "height": 1200})
        pg.goto("file://" + os.path.abspath(tmp)); pg.wait_for_timeout(500)
        hs = pg.evaluate("() => [...document.querySelectorAll('.kentry')].map(e => e.getBoundingClientRect().height * 25.4 / 96)")
        br.close()
    os.remove(tmp)
    groups, cur, h = [], [], 0
    for p, e in zip(pages, hs):
        e += 3                                  # margin below each entry
        if cur and h + e > capacity_mm: groups.append(cur); cur, h = [], 0
        cur.append(p); h += e
    if cur: groups.append(cur)
    return groups

def to_pdf(html_path, pdf_path):
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page()
        pg.goto("file://" + os.path.abspath(html_path), wait_until="load"); pg.wait_for_timeout(500)
        pg.pdf(path=pdf_path, prefer_css_page_size=True, print_background=True)
        b.close()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--school", default="", help="school name printed in every page footer")
    ap.add_argument("--outdir", default=os.path.join(HERE, "out"))
    ap.add_argument("--final", action="store_true", help="leave out the DRAFT stamps on the cover, licence and teacher notes (only after the owner and a lawyer approve the wording)")
    a = ap.parse_args()
    render.DRAFT = not a.final
    os.makedirs(a.outdir, exist_ok=True)
    pages = all_pages()
    assert [p["no"] for p in pages] == list(range(1, 21))
    W = lambda name, h: open(os.path.join(a.outdir, name), "w").write(h)
    W("pupil.html", render.doc("".join(render.pupil_page(p, a.school) for p in pages), "Early Finisher Puzzles P1"))
    W("front.html", render.doc(render.cover(a.school) + render.licence(a.school) + render.teacher_notes(pages) + render.contents(pages), "Early Finisher Puzzles P1 front matter"))
    W("key.html", render.doc(render.key_pages(pages, a.school, pack_key(pages, a.school, a.outdir)), "Early Finisher Puzzles P1 answer key"))
    for n in ("pupil", "front", "key"):
        to_pdf(os.path.join(a.outdir, n + ".html"), os.path.join(a.outdir, {"pupil": "P1_Puzzles", "front": "P1_FrontMatter", "key": "P1_Answer_Key"}[n] + ".pdf"))
    from pypdf import PdfWriter, PdfReader
    w = PdfWriter()
    for f in ("P1_FrontMatter.pdf", "P1_Puzzles.pdf"):
        for pg in PdfReader(os.path.join(a.outdir, f)).pages: w.add_page(pg)
    w.write(os.path.join(a.outdir, "P1_Complete_Pack.pdf"))
    # verification record
    rec = [dict(no=p["no"], title=p["title"], tier=p["tier"], topic=p["topic"], strand=p["strand"], syll=p["syll"], ptype=p["ptype"], mech=p["mech"],
                seed=p["seed"], checks=[dict(name=n, ok=o, detail=d) for n, o, d in p["verify"]],
                generator_slip_test=(round(p["cv"]["rate"], 4), p["cv"]["single_detected"], p["cv"]["single_total"])) for p in pages]
    json.dump(rec, open(os.path.join(a.outdir, "verification.json"), "w"), indent=1)
    print("built", a.outdir)

if __name__ == "__main__":
    main()
