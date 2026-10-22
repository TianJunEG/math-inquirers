"""P4 pagination test: every lesson must print exactly 2 core pages (page 1 = Start here, page 2 = on your own)
before its Investigation + Looking back page. Usage: python3 rebuild/p4_pagecheck.py [workbook.pdf]
Exit code 1 if a lesson spills onto a third core page, or page 1 / page 2 notes are not where expected."""
import sys, re
from pypdf import PdfReader
f = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/math-inquirers/p4/Math_Inquirers_Level4_Student_Workbook_Designed.pdf'
r = PdfReader(f)
txt = [(p.extract_text() or '') for p in r.pages]
start = {}; look = {}
for i, t in enumerate(txt):
    m = re.match(r'\s*Lesson (\d+)\s', t)
    if m and 'Name' in t[:200] and 'Looking back' not in t[:200] and int(m.group(1)) not in start: start[int(m.group(1))] = i
    m = re.match(r'\s*Lesson (\d+) •', t)
    if m and 'Looking back' in t[:200] and int(m.group(1)) not in look: look[int(m.group(1))] = i
bad = 0
for n in range(1, 11):
    core = look[n] - start[n]
    p1 = txt[start[n]]; p2 = txt[start[n] + 1] if core >= 2 else ''
    ok = core == 2 and 'Page 1' in p1 and 'Page 2 is on your own' in p2[:200]
    print(f'Lesson {n}: core pages {core} (PDF pages {start[n]+1}-{look[n]})', 'OK' if ok else 'FAIL')
    bad += (not ok)
sys.exit(1 if bad else 0)
