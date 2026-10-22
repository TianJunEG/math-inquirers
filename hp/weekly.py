# Weekly PDFs: student pages (from the designed workbook) and tutor scripts (from the designed tutor guide).
# Run in hp/ after the workbook and guide are rebuilt:  python3 weekly.py  ->  ../outputs/designed/Math_Inquirers_Level1_Weekly_PDFs.zip
import re, subprocess, zipfile, os, tempfile
from pypdf import PdfReader, PdfWriter
WB = '../outputs/workbook/Math_Inquirers_Level1_Student_Workbook_Designed.pdf'
TG = '../outputs/designed/Math_Inquirers_Level1_Tutor_Guide.pdf'
OUT = '../outputs/designed/Math_Inquirers_Level1_Weekly_PDFs.zip'

def texts(path):
    n = len(PdfReader(path).pages)
    return [subprocess.run(['pdftotext', '-f', str(i), '-l', str(i), '-layout', path, '-'], capture_output=True, text=True).stdout for i in range(1, n + 1)]

def first_line(t):
    for l in t.splitlines():
        if l.strip(): return l.strip()
    return ''

wb = texts(WB); tg = texts(TG)
# workbook: a lesson starts on the page whose first line is "Lesson N <topic>" (the lesson tab), and runs to the next lesson or the cut-outs
starts = {}
for i, t in enumerate(wb):
    m = re.match(r'Lesson (\d+)\b', first_line(t))
    if m and int(m.group(1)) not in starts: starts[int(m.group(1))] = i
special = {}
for i, t in enumerate(wb):
    fl = first_line(t)
    for key in ['My Inquiry Journal', 'Cut-outs', 'Play notes and $1 coins', 'Inquirer Kit', 'Number strips and sorting tiles', 'Puzzle cards', 'CERTIFICATE OF COMPLETION']:
        if fl.startswith(key): special.setdefault(key, i)
end_lessons = min(v for k, v in special.items() if k != 'My Inquiry Journal')
order = sorted(starts)
def lesson_pages(n):
    a = starts[n]; b = starts[n + 1] if n + 1 in starts else end_lessons
    return list(range(a, b))
# tutor guide: a lesson starts on the page whose first line is "Lesson N: ..."
tstart = {}
for i, t in enumerate(tg):
    m = re.match(r'Lesson (\d+):', first_line(t))
    if m: tstart.setdefault(int(m.group(1)), i)
tend = next(i for i, t in enumerate(tg) if first_line(t).startswith('Progress tracker'))
def guide_pages(n):
    return list(range(tstart[n], tstart[n + 1] if n + 1 in tstart else tend))

EXTRA = {1: (['My Inquiry Journal'], ['Inquirer Kit']), 3: ([], ['Cut-outs', 'Play notes and $1 coins']),
         5: ([], ['Number strips and sorting tiles', 'Puzzle cards', 'CERTIFICATE OF COMPLETION'])}

def write(src, pages, path):
    r = PdfReader(src); w = PdfWriter()
    for p in pages: w.add_page(r.pages[p])
    with open(path, 'wb') as f: w.write(f)

tmp = tempfile.mkdtemp()
with zipfile.ZipFile(OUT, 'w', zipfile.ZIP_DEFLATED) as z:
    for wk in range(1, 6):
        ls = [2 * wk - 1, 2 * wk]
        pre, post = EXTRA.get(wk, ([], []))
        sp = [special[k] for k in pre] + sum((lesson_pages(n) for n in ls), []) + [special[k] for k in post]
        f1 = os.path.join(tmp, f'Week{wk}_Student_Pages.pdf'); write(WB, sp, f1); z.write(f1, os.path.basename(f1))
        f2 = os.path.join(tmp, f'Week{wk}_Tutor_Scripts_and_Answers.pdf'); write(TG, sum((guide_pages(n) for n in ls), []), f2); z.write(f2, os.path.basename(f2))
        print(f'Week {wk}: student {len(sp)} pages, tutor {sum(len(guide_pages(n)) for n in ls)} pages')
print('zip written', OUT)
