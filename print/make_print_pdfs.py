#!/usr/bin/env python3
"""Make print-ready workbook PDFs: double-sided, bound (spiral / wire-o) on the LEFT edge of the sheet.

    python3 print/make_print_pdfs.py

For each level it reads the designed student workbook and writes outputs/print/Math_Inquirers_P<N>_Workbook_PRINT.pdf:
  * every page is shrunk slightly and shifted away from the binding edge (a gutter on the left of front pages
    and on the right of back pages, so the same strip of every sheet is the bound edge);
  * the cut-out pages (from the page headed 'Cut-outs' up to the certificate) and the certificate each get a blank
    back, so cutting a piece out never destroys something on the other side;
  * a blank page is added at the end if needed, so the page count is even (a whole number of sheets).
It also writes outputs/print/print_spec.json (page and sheet counts) used for printer quotes.
"""
import json, os, re, subprocess
from pypdf import PdfReader, PdfWriter, PageObject, Transformation

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'outputs', 'print')
SRC = {1: 'hp/Math_Inquirers_P1_Student_Workbook_Designed.pdf'}
SRC.update({n: f'p{n}/Math_Inquirers_P{n}_Student_Workbook_Designed.pdf' for n in range(2, 7)})
GUTTER_MM = 12.0


def first_line(path, page_no):
    t = subprocess.run(['pdftotext', '-f', str(page_no), '-l', str(page_no), '-layout', path, '-'],
                       capture_output=True, text=True).stdout
    for ln in t.split('\n'):
        if ln.strip():
            return ln.strip()
    return ''


def build(n):
    src = os.path.join(ROOT, SRC[n])
    rd = PdfReader(src)
    total = len(rd.pages)
    W = float(rd.pages[0].mediabox.width)
    H = float(rd.pages[0].mediabox.height)
    cut_start = None
    cert = None
    for p in range(1, total + 1):
        fl = first_line(src, p)
        if cut_start is None and fl.startswith('Cut-outs'):
            cut_start = p
        if fl.startswith('CERTIFICATE'):
            cert = p
    single_sided = set()
    if cut_start:
        single_sided.update(range(cut_start, (cert or total + 1)))
    if cert:
        single_sided.add(cert)
    seq = []  # (source page index or None for blank)
    for p in range(1, total + 1):
        seq.append(p - 1)
        if p in single_sided:
            seq.append(None)
    if len(seq) % 2:
        seq.append(None)
    g = GUTTER_MM / 25.4 * 72
    s = (W - g) / W
    wr = PdfWriter()
    for i, idx in enumerate(seq, start=1):
        page = PageObject.create_blank_page(width=W, height=H)
        if idx is not None:
            tx = g if i % 2 == 1 else 0.0   # odd = front of a sheet: binding on its left
            ty = (H - s * H) / 2
            page.merge_transformed_page(rd.pages[idx], Transformation().scale(s, s).translate(tx, ty))
        wr.add_page(page)
    os.makedirs(OUT, exist_ok=True)
    out = os.path.join(OUT, f'Math_Inquirers_P{n}_Workbook_PRINT.pdf')
    wr.add_metadata({'/Title': f'Math Inquirers Level {n} workbook (print version, bound on the left)'})
    with open(out, 'wb') as f:
        wr.write(f)
    return dict(level=n, source_pages=total, print_pages=len(seq), sheets=len(seq) // 2,
                blank_pages=sum(1 for x in seq if x is None), cutout_pages=sorted(single_sided),
                content_scale=round(s, 4), file=os.path.relpath(out, ROOT),
                printed_as='black and white, double-sided, flip on long edge, left binding', bw_file=os.path.relpath(out, os.path.join(ROOT)).replace('outputs/print/', 'outputs/print/bw/'))


if __name__ == '__main__':
    rows = [build(n) for n in range(1, 7)]
    json.dump(rows, open(os.path.join(OUT, 'print_spec.json'), 'w'), indent=1)
    for r in rows:
        print(r['level'], r['source_pages'], '->', r['print_pages'], 'pages =', r['sheets'], 'sheets;', r['blank_pages'], 'blank;', 'cut-out/single-sided source pages', len(r['cutout_pages']))
