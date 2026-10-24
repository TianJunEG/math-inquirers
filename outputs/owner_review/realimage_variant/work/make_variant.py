#!/usr/bin/env python3
"""Build the four real-image money pages (VARIANT, not in the booklets).
  python3 make_variant.py            -> builds both schools' pages in subprocesses with MONEY_ART=real and merges them
  (internal) python3 make_variant.py one p1|p2 OUTDIR
Pages: P2 S2-01 Dollars and Cents (P2-06), P2 S2-04 Purse Match (P2-24), P1 S2-10 Coin Purses (P1-15), P1 S2-11 Fewest Coins (P1-28)."""
import os, sys, subprocess
HERE = os.path.dirname(os.path.abspath(__file__)); REPO = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))
WANT = {"p2": [6, 24], "p1": [15, 28]}
FOOT = "REAL-IMAGE VARIANT for owner and lawyer review: not part of the booklets. MAS images, greyscale."

def one(sch, outdir):
    sys.path.insert(0, os.path.join(REPO, "school", sch)); os.chdir(os.path.join(REPO, "school", sch))
    import build, render
    pages = [p for p in build.all_pages() if p["no"] in WANT[sch]]
    pages.sort(key=lambda p: WANT[sch].index(p["no"]))
    os.makedirs(outdir, exist_ok=True)
    html = render.doc("".join(render.pupil_page(p, "") for p in pages), "real-image variant " + sch)
    html = html.replace("Photocopy licence. School (write name):", "REAL-IMAGE VARIANT, not for use. School:")
    h = os.path.join(outdir, f"{sch}_money_real.html"); open(h, "w").write(html)
    build.to_pdf(h, os.path.join(outdir, f"{sch}_money_real.pdf"))
    print("ok", sch, [p["code"] for p in pages], [(n, ok) for p in pages for n, ok, d in p["verify"] if not ok])

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "one":
        one(sys.argv[2], sys.argv[3])
    else:
        env = dict(os.environ, MONEY_ART="real", MONEY_ART_MODULE=os.path.join(HERE, "realart.py"))
        out = os.path.join(HERE, "build")
        for sch in ("p2", "p1"):
            subprocess.run([sys.executable, __file__, "one", sch, out], env=env, check=True)
        from pypdf import PdfWriter, PdfReader
        w = PdfWriter()
        for sch in ("p2", "p1"):
            for pg in PdfReader(os.path.join(out, f"{sch}_money_real.pdf")).pages: w.add_page(pg)
        dst = os.path.join(HERE, "..", "money_pages_real_variant.pdf"); w.write(dst); print("wrote", dst)
