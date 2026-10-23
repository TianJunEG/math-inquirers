#!/usr/bin/env python3
"""Make print-ready COMBINED term books (5 lessons per book) from the per-lesson PDFs in term/l<L>/out/lNN/.

    python3 print/make_term_books.py                       # Level 1, lessons 1-20, 5 per book, 10 lessons per term
    python3 print/make_term_books.py --level 1 --first 1 --last 10 --size 5   # only Term 1
    python3 print/make_term_books.py --level 2 --first 1 --last 20 --size 4 --per-term 10

Reads only term/l<L>/out/lNN/ (never edits it); re-run after any rebuild. For every book it writes to outputs/print/term/:
  * Workbook book  - cover (Math Inquirers, level, term, lesson range, Mi the dolphin, child name box), contents,
                     the lesson workbooks in order, a page number on every printed page.
  * Answer-key book (tutors only) - same grouping, own cover/contents.
  * Home-practice pack - the lessons' home sheets (a separate stapled pack, one sheet per lesson).
Print rules, as in print/make_print_pdfs.py: A4, double-sided, bound on the LEFT edge of each sheet (mirrored 12 mm gutter:
content is shrunk and shifted away from the binding edge on both sides of the sheet); even page count.
Extra rules: each lesson of a workbook book starts on a right-hand (front) page; every 'Kit' (cut-out) page sits on a front
page and gets a BLANK back, plus a dashed tear line and 'Tear out' note in the gutter strip, so removing it never removes
lesson content. Writes outputs/print/term/term_books_spec.json (pages and sheets per book) for printer quotes.
"""
import argparse, json, os, re, subprocess, sys
from io import BytesIO
from pypdf import PdfReader, PdfWriter, PageObject, Transformation
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, white
from reportlab.lib.utils import ImageReader

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'outputs', 'print', 'term')
MASCOT = os.path.join(ROOT, 'mascot', 'mi_dolphin_nocalc_transparent.png')   # owner-supplied Mi without the calculator
if not os.path.exists(MASCOT):
    MASCOT = os.path.join(ROOT, 'mascot', 'mi_dolphin_transparent.png')
GUTTER_MM = 12.0
TEAL, GOLD, INK = HexColor('#1B5E5A'), HexColor('#F2B705'), HexColor('#222222')
KINDS = {  # kind: (file suffix, label, recto-start, kit pages tear-out)
    'workbook': ('Workbook.pdf', 'Workbook', True, True),
    'key': ('Workbook_Answer_Key.pdf', 'Tutor Answer Key', False, False),
    'home': ('Home_Practice.pdf', 'Home Practice Pack', True, False),
}


def text_of(path, p):
    return subprocess.run(['pdftotext', '-f', str(p), '-l', str(p), '-layout', path, '-'],
                          capture_output=True, text=True).stdout


EXTRAS = {'workbook': ['Quest_Log'], 'key': ['Home_Answers', 'Quest_Tutor_Notes'], 'home': ['Quest_Parent_Note']}
NONCUT = {'hundred', 'hundred_square', 'groups_mat', 'array_mat', 'number_line', 'plates', 'grid_mat', 'graph_mat'}


def lesson_info(level, ln):
    """(kit types in page order, True if the lesson prints real-size content such as a ruler picture)"""
    try:
        raw = open(os.path.join(ROOT, 'term', f'l{level}', 'lessons', f'l{ln:02d}.json'), encoding='utf-8').read()
        d = json.loads(raw)
        ks = [k.get('type') for k in (d.get('workbook') or {}).get('kits', [{'type': 'base_ten'}])]
        return ks, '"type": "ruler"' in raw
    except Exception:
        return [], False


def is_kit(path, p):
    lines = [l.strip() for l in text_of(path, p).split('\n') if l.strip()]
    return bool(lines) and bool(re.search(r'\bKit$', lines[0]))


def lesson_title(path):
    """(topic, title) from the first workbook page, e.g. ('Whole numbers: tens and ones', 'Bundles and singles')."""
    lines = [re.split(r'\s{2,}', l.strip()) for l in text_of(path, 1).split('\n') if l.strip()]
    ti = next((i for i, l in enumerate(lines[1:], 1) if len(l) == 1 and l[0].isupper() and len(l[0]) > 3), None)
    head = lines[:ti] if ti else lines[:1]
    topic = ' '.join(l[1] for l in head if len(l) > 1).title()     # a long topic wraps onto a second header line
    title = lines[ti][0].rstrip('!').title() if ti else ''
    return topic, title


def overlay(W, H, fn):
    buf = BytesIO()
    c = canvas.Canvas(buf, pagesize=(W, H))
    fn(c)
    c.save()
    buf.seek(0)
    return PdfReader(buf).pages[0]


def cover_page(W, H, lvl, term, a, b, kind, bookno, ages):
    def draw(c):
        c.setFillColor(TEAL); c.rect(0, H - 250, W, 250, stroke=0, fill=1)
        c.setFillColor(GOLD); c.rect(0, H - 258, W, 8, stroke=0, fill=1)
        c.setFillColor(white); c.setFont('Helvetica-Bold', 40); c.drawCentredString(W / 2, H - 120, 'Math Inquirers')
        c.setFont('Helvetica', 17); c.drawCentredString(W / 2, H - 155, 'Think. Question. Prove.')
        c.setFont('Helvetica-Bold', 22); c.drawCentredString(W / 2, H - 215, f'Level {lvl}{ages}  -  Term {term}')
        c.setFillColor(TEAL); c.setFont('Helvetica-Bold', 34)
        c.drawCentredString(W / 2, H - 330, KINDS[kind][1] if kind != 'workbook' else 'Workbook')
        c.setFillColor(INK); c.setFont('Helvetica-Bold', 26); c.drawCentredString(W / 2, H - 375, f'Book {bookno}')
        c.setFont('Helvetica', 22); c.drawCentredString(W / 2, H - 410, f'Lessons {a} to {b}')
        if os.path.exists(MASCOT):
            img = ImageReader(MASCOT); iw, ih = img.getSize(); h = 190; w = h * iw / ih
            c.drawImage(img, (W - w) / 2, 230, w, h, mask='auto')
        if kind == 'key':
            c.setFillColor(HexColor('#B00020')); c.setFont('Helvetica-Bold', 15)
            c.drawCentredString(W / 2, 190, 'FOR THE TUTOR AND GROWN-UPS ONLY - keep away from the child')
        elif kind == 'home':
            c.setFillColor(INK); c.setFont('Helvetica', 13)
            c.drawCentredString(W / 2, 190, 'One sheet for each lesson. Tear out a sheet and do it at home.')
        else:
            c.setFillColor(INK); c.setFont('Helvetica-Bold', 16); c.drawString(70, 160, 'My name:')
            c.setStrokeColor(TEAL); c.setLineWidth(2); c.roundRect(150, 140, W - 220, 40, 8, stroke=1, fill=0)
    return overlay(W, H, draw)


def contents_page(W, H, lvl, term, kind, bookno, rows, kitnote):
    def draw(c):
        c.setFillColor(TEAL); c.setFont('Helvetica-Bold', 28); c.drawString(70, H - 90, 'Contents')
        c.setFillColor(INK); c.setFont('Helvetica', 12)
        c.drawString(70, H - 112, f'Math Inquirers Level {lvl}, Term {term}  -  {KINDS[kind][1]}, Book {bookno}')
        y = H - 160
        for lab, title, pg in rows:
            c.setFont('Helvetica-Bold', 15); c.setFillColor(TEAL); c.drawString(70, y, lab)
            c.setFont('Helvetica-Bold', 14); c.setFillColor(INK); c.drawString(160, y + 1, title[0][:46])
            c.setFont('Helvetica', 10); c.setFillColor(HexColor('#555555')); c.drawString(160, y - 13, title[1][:60])
            c.setFont('Helvetica-Bold', 14); c.drawRightString(W - 70, y, f'page {pg}')
            c.setStrokeColor(HexColor('#CCCCCC')); c.setDash(1, 3); c.line(70, y - 8, W - 70, y - 8); c.setDash()
            y -= 52
        if kitnote:
            c.setFillColor(INK); c.setFont('Helvetica-Bold', 12); c.drawString(70, 150, 'Kit pages (cut-outs)')
            c.setFont('Helvetica', 11)
            for i, t in enumerate(['Some lessons end with a kit page: tens bars, number lines, cards and so on.',
                                   'Each kit page has a blank back, so you can cut or tear it out without losing any work.',
                                   'Tear along the dashed line in the left margin. If the page says cut out, a grown-up cuts the pieces; keep them in an envelope.']):
                c.drawString(70, 132 - 15 * i, t)
    return overlay(W, H, draw)


def gutter_mark(W, H, g, cut=True):
    def draw(c):
        c.setStrokeColor(HexColor('#888888')); c.setDash(3, 3); c.setLineWidth(0.7)
        x = g - 1.5; c.line(x, 20, x, H - 20); c.setDash()
        c.setFillColor(HexColor('#666666')); c.setFont('Helvetica', 6.5)
        c.saveState(); c.translate(x - 3, H / 2); c.rotate(90)
        c.drawCentredString(0, 0, 'TEAR OUT here (blank on the back)  -  then cut out the pieces' if cut else 'TEAR OUT here if you like (blank on the back)  -  do not cut this page'); c.restoreState()
    return overlay(W, H, draw)


def folio(W, H, n, g, odd):
    def draw(c):
        c.setFillColor(HexColor('#444444')); c.setFont('Helvetica-Bold', 9)
        c.drawCentredString(g + (W - g) / 2 if odd else (W - g) / 2, 10, f'- {n} -')
    return overlay(W, H, draw)


def build_book(level, term, bookno, lessons, kind, ages=''):
    suffix, label, recto, kitmode = KINDS[kind]
    g = GUTTER_MM / 25.4 * 72
    items = []  # ('cover'|'contents'|('src',reader,idx,kit)|None)
    toc = []
    first = None
    for ln in lessons:
        path = os.path.join(ROOT, 'term', f'l{level}', 'out', f'l{ln:02d}', f'L{ln:02d}_{suffix}')
        if not os.path.exists(path):
            raise SystemExit(f'missing {path}')
    W = H = None
    seq = ['cover', 'contents']
    for ln in lessons:
        path = os.path.join(ROOT, 'term', f'l{level}', 'out', f'l{ln:02d}', f'L{ln:02d}_{suffix}')
        rd = PdfReader(path)
        if W is None:
            W, H = float(rd.pages[0].mediabox.width), float(rd.pages[0].mediabox.height)
        if recto and len(seq) % 2 == 1:
            seq.append(None)           # start each lesson on a front page
        wbpath = os.path.join(ROOT, 'term', f'l{level}', 'out', f'l{ln:02d}', f'L{ln:02d}_Workbook.pdf')
        topic, title = lesson_title(wbpath)
        toc.append((f'Lesson {ln}', (re.sub(r'\b(And|Of|The|To|In|On|A)\b', lambda m: m.group(1).lower(), title) or topic, topic), len(seq) + 1))
        toc[-1] = (toc[-1][0], (toc[-1][1][0][:1].upper() + toc[-1][1][0][1:], toc[-1][1][1]), toc[-1][2])
        ktypes, realsize = lesson_info(level, ln)
        kn = 0
        for i in range(len(rd.pages)):
            kit = kitmode and is_kit(path, i + 1)
            if kit and len(seq) % 2 == 1:
                seq.append(None)       # kit page must be a front page (its back is blank)
            cut = True
            if kit:
                cut = not (kn < len(ktypes) and ktypes[kn] in NONCUT); kn += 1
            # kit pages and real-size pages (a ruler picture) print at 100%: the page already has 14 mm margins, more than the 12 mm binding strip
            seq.append(('src', rd, i, kit, cut, bool(kit or (realsize and kind == 'workbook'))))
        for extra in EXTRAS.get(kind, []):          # Quest Log (child, 100%), tutor notes (key book), grown-up note and home answers
            xp = os.path.join(ROOT, 'term', f'l{level}', 'out', f'l{ln:02d}', f'L{ln:02d}_{extra}.pdf')
            if not os.path.exists(xp): continue
            xr = PdfReader(xp)
            if recto and len(seq) % 2 == 1: seq.append(None)
            for j in range(len(xr.pages)):
                seq.append(('src', xr, j, False, True, extra == 'Quest_Log'))
            if kit:
                seq.append(None)
    if len(seq) % 2:
        seq.append(None)
    s = (W - g) / W
    ty = (H - s * H) / 2
    a, b = lessons[0], lessons[-1]
    cover = cover_page(W, H, level, term, a, b, kind, bookno, ages)
    cont = contents_page(W, H, level, term, kind, bookno, toc, kitmode and any(x and x != 'cover' and x != 'contents' and x[3] for x in seq))
    wr = PdfWriter()
    kits = []
    for i, item in enumerate(seq, start=1):
        page = PageObject.create_blank_page(width=W, height=H)
        odd = i % 2 == 1
        tx = g if odd else 0.0
        src = None
        if item == 'cover':
            src = cover
        elif item == 'contents':
            src = cont
        elif item:
            src = item[1].pages[item[2]]
        if src is not None:
            if isinstance(item, tuple) and item[5]:
                page.merge_page(src)               # 100%, no shift
            else:
                page.merge_transformed_page(src, Transformation().scale(s, s).translate(tx, ty))
            if item not in ('cover',):
                page.merge_page(folio(W, H, i, g, odd))
            if isinstance(item, tuple) and item[3]:
                page.merge_page(gutter_mark(W, H, g, item[4])); kits.append(i)
        wr.add_page(page)
    os.makedirs(OUT, exist_ok=True)
    name = f'Math_Inquirers_L{level}_T{term}_Book{bookno}_Lessons{a:02d}-{b:02d}_{ {"workbook":"Workbook","key":"AnswerKey_TUTOR","home":"HomePack"}[kind] }_PRINT.pdf'
    out = os.path.join(OUT, name)
    wr.add_metadata({'/Title': f'Math Inquirers Level {level} Term {term} Book {bookno} lessons {a}-{b}: {label} (print version, bound on the left)'})
    with open(out, 'wb') as f:
        wr.write(f)
    return dict(level=level, term=term, book=bookno, kind=kind, lessons=f'{a}-{b}', print_pages=len(seq), sheets=len(seq) // 2,
                blank_pages=sum(1 for x in seq if x is None), kit_pages=kits, content_scale=round(s, 4), file=os.path.relpath(out, ROOT))


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--level', type=int, default=1)
    ap.add_argument('--first', type=int, default=1)
    ap.add_argument('--last', type=int, default=0, help='default: the last built lesson that is not a stub (up to 40)')
    ap.add_argument('--size', type=int, default=5, help='lessons per book')
    ap.add_argument('--per-term', type=int, default=10, help='lessons per term (term number = (lesson-1)//per_term + 1)')
    ap.add_argument('--ages', default=' (ages 6-8)')
    ap.add_argument('--kinds', default='workbook,key,home')
    ap.add_argument('--bw', action='store_true', help='afterwards also write the black-and-white print versions (outputs/print/bw/term/) via print/make_bw_print.py')
    a = ap.parse_args()
    if not a.last:                       # Terms 3 and 4: stop at the last real built lesson, skipping stubs (data `stub: true`)
        last = 0
        for n in range(a.first, 41):
            lp = os.path.join(ROOT, 'term', f'l{a.level}', 'lessons', f'l{n:02d}.json')
            op = os.path.join(ROOT, 'term', f'l{a.level}', 'out', f'l{n:02d}', f'L{n:02d}_Workbook.pdf')
            if not (os.path.exists(lp) and os.path.exists(op)): break
            if json.load(open(lp, encoding='utf-8')).get('stub'): break
            last = n
        a.last = last or 20
    rows = []
    for k, start in enumerate(range(a.first, a.last + 1, a.size), start=1):
        ls = list(range(start, min(start + a.size, a.last + 1)))
        term = (ls[0] - 1) // a.per_term + 1
        for kind in a.kinds.split(','):
            r = build_book(a.level, term, (ls[0] - 1) // a.size + 1, ls, kind, a.ages)
            rows.append(r)
            print(r['file'].split('/')[-1], r['print_pages'], 'pages', r['sheets'], 'sheets', r['blank_pages'], 'blank', 'kit', r['kit_pages'])
    json.dump(rows, open(os.path.join(OUT, 'term_books_spec.json'), 'w'), indent=1)
    if a.bw:
        subprocess.run([sys.executable, os.path.join(ROOT, 'print', 'make_bw_print.py'), '--only', 'L%d_T' % a.level, '--check'], check=True)
