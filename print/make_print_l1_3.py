#!/usr/bin/env python3
"""Rebuild only the Level 1-3 holiday print PDFs (colour + B&W) and update only their rows in print_spec.json / bw_spec.json.
    python3 print/make_print_l1_3.py [--check]
Written so a Level 1-3 diagram fix does not touch the Level 4-6 print files."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import make_print_pdfs as MP
import make_bw_print as MB
import fitz

LEVELS = (1, 2, 3)
rows = {n: MP.build(n) for n in LEVELS}
spec_path = os.path.join(MP.OUT, 'print_spec.json')
spec = json.load(open(spec_path))
spec = [rows.get(r['level'], r) for r in spec]
json.dump(spec, open(spec_path, 'w'), indent=1)
for r in rows.values():
    print(r['level'], r['source_pages'], '->', r['print_pages'], 'pages =', r['sheets'], 'sheets;', r['blank_pages'], 'blank')
bw_rows = {}
for n in LEVELS:
    src = os.path.join(MB.PRINT, f'Math_Inquirers_P{n}_Workbook_PRINT.pdf')
    dst = os.path.join(MB.BW, f'Math_Inquirers_P{n}_Workbook_PRINT.pdf')
    pages, dropped = MB.convert_pdf(src, dst)
    bw_rows[os.path.relpath(dst, MB.ROOT)] = dict(file=os.path.relpath(dst, MB.ROOT), pages=pages, sheets=pages // 2, mb=round(os.path.getsize(dst) / 1e6, 2), pale_tint_dropped_max=max(dropped))
    print(bw_rows[os.path.relpath(dst, MB.ROOT)], flush=True)
bw_path = os.path.join(MB.BW, 'bw_spec.json')
bw = json.load(open(bw_path))
bw = [bw_rows.get(r['file'], r) for r in bw]
json.dump(bw, open(bw_path, 'w'), indent=1)
if '--check' in sys.argv:
    from check_bw import check
    check([os.path.join(MB.ROOT, r['file']) for r in bw_rows.values()])
