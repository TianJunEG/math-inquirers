#!/usr/bin/env python3
"""Build the Primary 1 early-finisher pack.
  python3 build.py [--school "Name of School"] [--outdir out] [--seed-check]
Outputs (in out/): P1_Puzzles.pdf (20 pupil pages), P1_FrontMatter.pdf (4), P1_Complete_Pack.pdf (24),
P1_Answer_Key.pdf, verification.json."""
import argparse, json, os, sys, re, subprocess
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from gen import pages_numbers, pages_arith, pages_measure
import render

def all_pages():
    ps = []
    for m in (pages_numbers, pages_arith, pages_measure):
        ps += [f() for f in m.PAGES]
    ps.sort(key=lambda p: p["no"])
    return ps

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
    a = ap.parse_args()
    os.makedirs(a.outdir, exist_ok=True)
    pages = all_pages()
    assert [p["no"] for p in pages] == list(range(1, 21))
    W = lambda name, h: open(os.path.join(a.outdir, name), "w").write(h)
    W("pupil.html", render.doc("".join(render.pupil_page(p, a.school) for p in pages), "Early Finisher Puzzles P1"))
    W("front.html", render.doc(render.cover(a.school) + render.licence(a.school) + render.teacher_notes(pages) + render.contents(pages), "Early Finisher Puzzles P1 front matter"))
    W("key.html", render.doc(render.key_pages(pages, a.school), "Early Finisher Puzzles P1 answer key"))
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
                slip_detect=(round(p["cv"]["rate"], 4), p["cv"]["single_detected"], p["cv"]["single_total"])) for p in pages]
    json.dump(rec, open(os.path.join(a.outdir, "verification.json"), "w"), indent=1)
    print("built", a.outdir)

if __name__ == "__main__":
    main()
