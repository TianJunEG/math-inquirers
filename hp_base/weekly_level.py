# Weekly PDFs for any level: python3 weekly_level.py <workbook.pdf> <tutor_guide.pdf> <out.zip>
# Week 1 gets the journal (if any) and the cut-outs; week 5 gets the certificate.
import re, subprocess, zipfile, os, tempfile, sys
from pypdf import PdfReader, PdfWriter
WB, TG, OUT = sys.argv[1:4]

def texts(path):
    n = len(PdfReader(path).pages)
    return [subprocess.run(['pdftotext', '-f', str(i), '-l', str(i), '-layout', path, '-'], capture_output=True, text=True).stdout for i in range(1, n + 1)]
def first_line(t):
    for l in t.splitlines():
        if l.strip(): return l.strip()
    return ''

wb = texts(WB); tg = texts(TG); fl = [first_line(t) for t in wb]
starts = {}
for i, f in enumerate(fl):
    m = re.match(r'Lesson (\d+)\b', f)
    if m and int(m.group(1)) not in starts: starts[int(m.group(1))] = i
journal = [i for i, f in enumerate(fl) if f.startswith('My Inquiry Journal')]
cert = [i for i, f in enumerate(fl) if f.startswith('CERTIFICATE')]
kit0 = next((i for i, f in enumerate(fl) if i > starts[10] and (f.startswith('Cut-outs') or f.startswith('Inquirer Kit'))), cert[0] if cert else len(wb))
kit = list(range(kit0, cert[0] if cert else len(wb)))
def lesson_pages(n):
    b = starts[n + 1] if n + 1 in starts else kit0
    return [p for p in range(starts[n], b) if p not in journal]
tstart = {}
for i, t in enumerate(tg):
    m = re.match(r'Lesson (\d+):', first_line(t))
    if m: tstart.setdefault(int(m.group(1)), i)
tend = next(i for i, t in enumerate(tg) if first_line(t).startswith('Progress tracker'))
def guide_pages(n): return list(range(tstart[n], tstart[n + 1] if n + 1 in tstart else tend))
def write(src, pages, path):
    r = PdfReader(src); w = PdfWriter()
    for p in pages: w.add_page(r.pages[p])
    with open(path, 'wb') as f: w.write(f)
tmp = tempfile.mkdtemp()
with zipfile.ZipFile(OUT, 'w', zipfile.ZIP_DEFLATED) as z:
    for wk in range(1, 6):
        ls = [2 * wk - 1, 2 * wk]
        sp = (journal + [] if wk == 1 else []) + sum((lesson_pages(n) for n in ls), []) + (kit if wk == 1 else []) + (cert if wk == 5 else [])
        f1 = os.path.join(tmp, f'Week{wk}_Student_Pages.pdf'); write(WB, sp, f1); z.write(f1, os.path.basename(f1))
        gp = sum((guide_pages(n) for n in ls), [])
        f2 = os.path.join(tmp, f'Week{wk}_Tutor_Scripts_and_Answers.pdf'); write(TG, gp, f2); z.write(f2, os.path.basename(f2))
        print(f'Week {wk}: student {len(sp)} pages, tutor {len(gp)} pages')
print('zip written', OUT)
