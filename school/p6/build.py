#!/usr/bin/env python3
"""Build the two Primary 6 early-finisher booklets (Semester 1 and Semester 2).
  python3 build.py [--school "Name of School"] [--outdir out] [--booklet S1|S2|both] [--final]
Outputs (in out/), for each booklet X in S1, S2: P6_X_Puzzles.pdf (20 pupil pages), P6_X_FrontMatter.pdf (5), P6_X_Complete_Pack.pdf (25),
P6_X_Answer_Key.pdf, plus verification.json (all pages). Page order and the two page numbers (S1-07 and P6-17) come from gen/outcomes.py."""
import argparse, json, os, sys, re, subprocess
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from gen import outcomes
import render

# page modules (P6-01 to P6-40); a module not written yet is skipped, so a half-built tree still builds (validate.py --partial)
MODULES = []
for _m in ("pages_a", "pages_b", "pages_c", "pages_d", "pages_e", "pages_f", "pages_cbc"):
    try:
        MODULES.append(__import__("gen." + _m, fromlist=["PAGES"]))
    except ModuleNotFoundError as e:
        if e.name != "gen." + _m: raise

def all_pages():
    ps = []
    for m in MODULES:
        ps += [f() for f in m.PAGES]
    ps.sort(key=lambda p: p["no"])
    assert len({p["no"] for p in ps}) == len(ps), "duplicate page numbers"
    for p in ps:
        outcomes.PAGE_OC[p["no"]] = list(p["oc"])
        p["code"] = outcomes.code_of(p["no"])
        p["bk"], p["pos"] = outcomes.booklet_of(p["no"])
        p["ps"] = bool(p.get("ps"))
    return ps

def booklet_pages(pages, key):
    by = {p["no"]: p for p in pages}
    return [by[n] for n in outcomes.BOOKLETS[key]["order"] if n in by]

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

def build_booklet(key, pages, school, outdir):
    bk = outcomes.BOOKLETS[key]
    bp = booklet_pages(pages, key)
    W = lambda name, h: open(os.path.join(outdir, name), "w").write(h)
    title = f"Early Finisher Puzzles P6 {bk['name']}"
    W(f"{key}_pupil.html", render.doc("".join(render.pupil_page(p, school) for p in bp), title))
    W(f"{key}_front.html", render.doc(render.cover(school, bk) + render.licence(school, bk) + render.teacher_notes(bp, bk) + render.contents(bp, bk), title + " front matter"))
    W(f"{key}_key.html", render.doc(render.key_pages(bp, school, pack_key(bp, school, outdir), bk), title + " answer key"))
    names = {"pupil": "Puzzles", "front": "FrontMatter", "key": "Answer_Key"}
    for n in ("pupil", "front", "key"):
        to_pdf(os.path.join(outdir, f"{key}_{n}.html"), os.path.join(outdir, f"P6_{key}_{names[n]}.pdf"))
    from pypdf import PdfWriter, PdfReader
    w = PdfWriter()
    for f in (f"P6_{key}_FrontMatter.pdf", f"P6_{key}_Puzzles.pdf"):
        for pg in PdfReader(os.path.join(outdir, f)).pages: w.add_page(pg)
    w.write(os.path.join(outdir, f"P6_{key}_Complete_Pack.pdf"))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--school", default="", help="school name printed in every page footer")
    ap.add_argument("--outdir", default=os.path.join(HERE, "out"))
    ap.add_argument("--booklet", default="both", choices=["S1", "S2", "both"])
    ap.add_argument("--final", action="store_true", help="leave out the DRAFT stamps on the cover, licence and teacher notes (only after the owner and a lawyer approve the wording)")
    a = ap.parse_args()
    render.DRAFT = not a.final
    os.makedirs(a.outdir, exist_ok=True)
    pages = all_pages()
    for key in (["S1", "S2"] if a.booklet == "both" else [a.booklet]):
        build_booklet(key, pages, a.school, a.outdir)
    # verification record (all pages)
    rec = [dict(no=p["no"], code=p["code"], title=p["title"], tier=p["tier"], topic=p["topic"], strand=p["strand"], syll=p["syll"], outcomes=outcomes.PAGE_OC[p["no"]], ptype=p["ptype"], mech=p["mech"],
                seed=p["seed"], checks=[dict(name=n, ok=o, detail=d) for n, o, d in p["verify"]],
                generator_slip_test=(round(p["cv"]["rate"], 4), p["cv"]["single_detected"], p["cv"]["single_total"])) for p in pages]
    json.dump(rec, open(os.path.join(a.outdir, "verification.json"), "w"), indent=1)
    print("built", a.outdir, f"({len(pages)} pages generated)")

if __name__ == "__main__":
    main()
