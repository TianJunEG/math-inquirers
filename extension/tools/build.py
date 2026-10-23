#!/usr/bin/env python3
"""Build the extension workbook of one level: a colour SOFT-COPY PDF and a black-and-white PRINT PDF.

    python3 extension/tools/build.py --level 1                 # units found in extension/data/l1_uNN.json
    python3 extension/tools/build.py --level 1 --units 1,2     # only these units (proof edition)

Pipeline: unit JSON -> HTML (render.py) -> Chromium PDF (Playwright).  Layout is a fixed A4 page grid: every unit is exactly
7 pages (learn it, 3 x Start here, Think harder, Go further, Check yourself).
Print edition: black and white only, double-sided, left binding: mirrored 12 mm gutter (recto: extra margin on the left, verso: on
the right), even page count, answer section last (starts on a right-hand page; dashed tear line in the margin).
Soft edition: colour theme, same pages and page numbers, symmetric margins, PDF bookmarks.
Reports (page fill and overflow) go to outputs/extension/L<N>/build_report.json; the exit code is 1 on overflow or fill below 85%.
"""
import argparse, glob, json, os, re, sys, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import render, figs   # noqa: E402
from render import esc, mk, data_uri, ICON, ROOT, EXT   # noqa: E402
from playwright.sync_api import sync_playwright   # noqa: E402
from PIL import Image   # noqa: E402
import numpy as np   # noqa: E402

CFG = json.load(open(os.path.join(EXT, 'config', 'levels.json'), encoding='utf-8'))
PG = CFG['page']


def font_css():
    out = []
    base = os.path.join(ROOT, 'fonts', 'node_modules', '@fontsource')
    for fam, d, ws in (('Fredoka', 'fredoka', (400, 500, 600, 700)), ('Nunito Sans', 'nunito-sans', (400, 500, 600, 700, 800))):
        for w in ws:
            p = os.path.join(base, d, 'files', f'{d}-latin-{w}-normal.woff2')
            out.append(f"@font-face{{font-family:'{fam}';font-weight:{w};src:url('file://{p}') format('woff2')}}")
    return '\n'.join(out)


def mi_uri(pose, theme):
    src = os.path.join(ROOT, 'mascot', 'poses', pose + '.png')
    if theme == 'colour':
        return data_uri(src)
    cache = os.path.join(EXT, 'assets', 'bw'); os.makedirs(cache, exist_ok=True)
    dst = os.path.join(cache, pose + '_bw.png')
    if not os.path.exists(dst):
        im = Image.open(src).convert('RGBA')
        bg = Image.new('RGBA', im.size, (255, 255, 255, 255)); bg.alpha_composite(im)
        a = np.array(bg.convert('L'), dtype=float)
        B = np.array([[0, 8, 2, 10], [12, 4, 14, 6], [3, 11, 1, 9], [15, 7, 13, 5]]) / 16.0
        h, w = a.shape
        thr = np.tile(B, (h // 4 + 1, w // 4 + 1))[:h, :w]
        mid = (a >= 110) & (a < 235)
        out = np.where((a < 110) | (mid & ((235 - a) / 125.0 * 0.6 > thr)), 0, 255).astype(np.uint8)
        Image.fromarray(out).convert('1').save(dst)
    return data_uri(dst)


# ---------------------------------------------------------------- front / back pages
def cover(book, theme):
    return (f'<div class="cover"><div class="brand">Math Inquirers</div><h1>Extension<br>Workbook<span>with answers</span></h1>'
            f'<div class="lvl">Level {book["level"]}</div><div class="tags"><span>Self-study</span><span>Ages {CFG["levels"][str(book["level"])]["ages"]}</span></div>'
            f'<img alt="Mi the dolphin waving" src="{mi_uri("mi_hello_wave", theme)}">'
            f'<div class="namebox">My name<i></i></div></div>')


def legend():
    return ('<div class="legend">'
            f'<div>{ICON["start"].replace("<svg", "<svg fill=\"currentColor\" stroke=\"currentColor\"")}<span><b>Start here.</b> The main path. Do these first.</span></div>'
            f'<div>{ICON["think"].replace("<svg", "<svg fill=\"currentColor\" stroke=\"currentColor\"")}<span><b>Think harder.</b> Longer problems. Hints are printed upside down.</span></div>'
            f'<div>{ICON["go"].replace("<svg", "<svg fill=\"currentColor\" stroke=\"currentColor\"")}<span><b>Go further.</b> A weekend page. Big challenges, just for fun.</span></div>'
            f'<div>{ICON["quiz"].replace("<svg", "<svg fill=\"none\" stroke=\"currentColor\"")}<span><b>Check yourself.</b> Four quick questions at the end.</span></div></div>')


def licence(book, theme, ctx):
    # DRAFT wording for the owner; to be reviewed by the lawyer (docs/legal/review.md, item L4). No price, no syllabus claim.
    return ('<div class="pbody lic"><div class="h1">About this book</div>'
            f'<p><b>Math Inquirers Extension Workbook, Level {book["level"]}</b><br>Self-study practice with answers.</p>'
            '<div class="box"><h3>Copyright</h3><p>&copy; 2026 Preciouslyours Pte Ltd (UEN 201507566K), trading as Math Inquirers. All rights reserved. '
            'Text, questions, drawings and the Mi the dolphin character are our own work.</p></div>'
            '<div class="box"><h3>Licence for personal use</h3><p>You may use this book for the learning of one child or one family. '
            'You may make copies of single pages for that child only, for example to redo a page.</p>'
            '<p>Please do not share, post, sell, lend out in bulk, upload or copy the book (print or PDF) for other people, other families, '
            'classes, tuition centres or schools. If you would like to use it with a group, please contact us first.</p>'
            f'<p>{"This soft copy" if theme == "colour" else "This printed book"} is licensed to the buyer. It is not a transfer of ownership.</p></div>'
            '<div class="box"><h3>Good to know</h3><ul><li>This is a private-enrichment book. It is not an official school or examination book, '
            'and it makes no promise about any test result.</li>'
            '<li>We have checked the answers with care. If you find a mistake, please tell us so we can fix it.</li>'
            '<li>Printed copies are black and white. The soft copy has the same pages in colour.</li></ul></div>'
            '<div class="box"><h3>Contact</h3><p>Math Inquirers, business WhatsApp +65 9880 5962. Email: pypteltd@gmail.com. Registered office: [address, owner to add].</p></div>'
            '<p class="note">Edition 1, 2026. First printing.</p>'
            '<p class="note">DRAFT licence text, for owner and lawyer approval. Not final.</p></div>')


def welcome(book, theme, ctx):
    steps = ['Read the <b>Learn it</b> page first. It shows how the idea works.',
             'Do the <b>Start here</b> pages. Take your time.',
             'Stuck? Find the hint. It is printed upside down.',
             'Do <b>Check yourself</b>. Check the answers at the back. Wrong? Read the <b>Why</b>.']
    kid = ('<div class="box kid"><h3>How to use this book</h3><ol class="steps">' + ''.join(f'<li><span>{t}</span></li>' for t in steps) + '</ol></div>')
    return (f'<div class="pbody"><div style="display:flex;align-items:flex-end"><div><div class="h1">Welcome!</div>'
            f'<div class="lead">This book is for you to explore at your own pace. Every unit has 7 pages. You can start on your own. A grown-up can help if you like.</div></div>'
            f'<img class="welcome-mi" alt="Mi the dolphin" src="{mi_uri("mi_writing_desk", theme)}"></div>'
            + kid +
            '<div class="box"><h3>For the grown-up</h3><ul>'
            '<li>Practice for the same ideas as the Holiday Program (our school-holiday maths course), with new numbers and stories. '
            'You do not need to have joined it: every unit starts with a worked example.</li>'
            '<li>3 short sessions a week, 20 to 25 minutes each. <b>Go further</b> is a weekend page: a big challenge for another day (see the pace plan).</li>'
            '<li>This is a self-study book. Your child marks their own work: each answer at the back says the answer first, then a short reason (Why) in plain words, '
            'and the page of the question. A child who reads slowly may like a helper to read the Why with them.</li>'
            f'<li>Answers are at the back, from page {ctx["divider_pg"]}. Please ask your child to try first.</li>'
            '<li>Check yourself score 2 or less? Read the Learn it page again and redo one Start here page.</li>'
            + ('<li>Printing the soft copy? Print at 100 percent (actual size) so the rulers are true size.</li>' if theme == 'colour' else '<li>The rulers in Unit 9 are printed at real size.</li>') + '</ul></div>'
            '<div class="box"><h3>The four page names</h3>' + legend() + '</div>'
            '<p class="note" style="margin:0"><b>Tip:</b> use a pencil. Mistakes help you learn. Read each question twice before you write.</p></div>')


def contents(book, theme, ctx):
    rows = []
    for n, topic in enumerate(book['unit_titles'], 1):
        title = book['titles'].get(n, topic)
        hl = book['lessons'].get(n)
        if n in ctx['unit_start']:
            rows.append(f'<tr><td class="n">{n}</td><td class="t"><b>{esc(title)}</b><small>{esc(topic)}'
                        f'{" &middot; follows Holiday Program Lesson " + str(hl) if hl else ""} &middot; answers on page {ctx["ans_start"][n]}</small></td>'
                        f'<td class="p">page {ctx["unit_start"][n]}</td></tr>')
        else:
            rows.append(f'<tr class="later"><td class="n">{n}</td><td class="t"><b>{esc(title)}</b><small>Not in this proof edition</small></td><td class="p">&ndash;</td></tr>')
    extra = (f'<tr><td class="n"></td><td class="t"><b>My progress</b></td><td class="p">page {ctx["progress_pg"]}</td></tr>'
             f'<tr><td class="n"></td><td class="t"><b>My certificate</b></td><td class="p">page {ctx["progress_pg"] + 1}</td></tr>'
             f'<tr><td class="n"></td><td class="t"><b>Answers</b><small>Check your work, with short reasons</small></td><td class="p">page {ctx["divider_pg"]}</td></tr>')
    front = ('<tr><td class="n"></td><td class="t"><b>About this book</b><small>Copyright and licence</small></td><td class="p">page 2</td></tr>'
             '<tr><td class="n"></td><td class="t"><b>Welcome</b></td><td class="p">page 3</td></tr>'
             '<tr><td class="n"></td><td class="t"><b>My pace plan</b></td><td class="p">page 5</td></tr>')
    return f'<div class="pbody"><div class="h1">Contents</div><table class="toc">{front}{"".join(rows)}{extra}</table></div>'


def pace(book, theme, ctx):
    rows = []
    for n, topic in enumerate(book['unit_titles'], 1):
        title = book['titles'].get(n, topic)
        if n in ctx['unit_start']:
            s = ctx['unit_start'][n]
            rows.append(f'<tr><td><b>{n}</b></td><td class="l"><b>{esc(title)}</b></td><td>{s}-{s + 1}</td><td>{s + 2}-{s + 3}</td><td>{s + 4} and {s + 6}</td><td>{s + 5}</td>'
                        '<td><span class="tick"></span></td></tr>')
        else:
            rows.append(f'<tr><td><b>{n}</b></td><td class="l"><b>{esc(title)}</b></td><td colspan="4">Not in this proof edition</td><td><span class="tick"></span></td></tr>')
    return ('<div class="pbody"><div class="h1">My pace plan</div>'
            '<div class="lead">Numbers in the table are page numbers. One unit a week for 10 weeks. Three short sessions a week, about 20 to 25 minutes each. '
            '<b>Go further</b> is a weekend page: do it on a weekend, when there is time to think. Tick the box when the week is done.</div>'
            '<table class="grid pace"><tr><th>Week</th><th>Unit</th><th>Session 1<br><small>Learn it, Start here</small></th><th>Session 2<br><small>Start here</small></th><th>Session 3<br><small>Think harder, Check yourself</small></th><th>Weekend page<br><small>Go further</small></th><th>Done</th></tr>' + ''.join(rows) +
            '<tr><td><b>11</b></td><td class="l"><b>Catch-up week</b></td><td colspan="4">Repeat any Check yourself where your score was 2 or less.</td><td><span class="tick"></span></td></tr></table>'
            '<div class="box"><h3>Tips for the grown-up</h3><ul><li>Short and often beats one long session. Stop while your child still wants more.</li>'
            '<li>Go further has big challenges. It is fine to skip it, or to do only one question. Missed a week? Carry on.</li></ul></div></div>')


def progress(book, theme, ctx):
    rows = []
    for n, topic in enumerate(book['unit_titles'], 1):
        title = book['titles'].get(n, topic)
        rows.append(f'<tr><td><b>{n}</b></td><td class="l">{esc(title)}</td>' + '<td><span class="tick"></span></td>' * 4 +
                    '<td>&nbsp;&nbsp;&nbsp;/ 4</td><td style="width:22mm"></td></tr>')
    return ('<div class="pbody"><div class="h1">My progress</div><div class="lead">Tick each box when you finish. Write your Check yourself score.</div>'
            '<table class="grid prog"><tr><th>Unit</th><th>Topic</th><th>Learn it</th><th>Start here</th><th>Think harder</th><th>Go further</th><th>Score</th><th>Date</th></tr>' + ''.join(rows) + '</table>'
            '<div class="box"><h3>Look back</h3><div class="rows"><div class="rw"><span class="rl">My favourite unit was</span><span class="rln"></span></div>'
            '<div class="rw"><span class="rl">The hardest idea was</span><span class="rln"></span></div>'
            '<div class="rw"><span class="rl">Next I want to try</span><span class="rln"></span></div></div></div></div>')


def certificate(book, theme, ctx):
    return (f'<div class="cert"><img alt="Mi the dolphin with trophies" src="{mi_uri("mi_trophy", theme)}"><h1>Certificate<br>of Completion</h1>'
            '<div class="big">Well done,</div><div class="nameline"></div>'
            f'<div class="big" style="font-size:17pt;line-height:1.3">You finished the Math Inquirers<br>Extension Workbook, Level {book["level"]}.</div>'
            '<div class="sigs"><div>Date</div><div>Signed by a grown-up</div></div></div>')


def divider(book, theme, ctx):
    return ('<div class="divider"><h1>Answers</h1><p>Try each question first. Then check your work here.</p>'
            '<p>Each answer says <b>Answer</b> first, then <b>Why</b>, and the page of the question. Got one wrong? Read the Why, then try it again. '
            'Stuck on the Why? Ask someone to read it with you.</p>'
            '<p>Cover this part of the book with a folded sheet of paper while you work, so you do not see the answers by mistake.</p></div>')


def ans_head(book):
    return f'<div class="ph"><span class="lv">Level {book["level"]}</span><span class="un">Answers</span><span class="nm" style="font-weight:700">check your work</span></div>'


# ---------------------------------------------------------------- pagination of the answers
def paginate_answers(page, blocks, css, cfg_vars):
    """blocks: list of html. Returns list of pages (list of block indexes) using real browser heights."""
    probe = (f'<html><head><meta charset="utf-8"><style>{css}</style></head><body class="colour print" style="{cfg_vars}">'
             f'<section class="page recto"><div class="pg"><div class="ph"><span class="lv">x</span></div><div class="pbody answers" id="pb"></div></div></section>'
             f'<div id="meas" style="position:absolute;left:0;top:300mm;width:172mm">' + ''.join(f'<div class="blk" style="display:flow-root">{b}</div>' for b in blocks) + '</div></body></html>')
    tmp = tempfile.NamedTemporaryFile('w', suffix='.html', delete=False, encoding='utf-8'); tmp.write(probe); tmp.close()
    page.goto('file://' + tmp.name); page.evaluate('document.fonts.ready'); page.wait_for_timeout(300)
    avail = page.evaluate('document.getElementById("pb").clientHeight')
    hs = page.evaluate('Array.from(document.querySelectorAll(".blk")).map(e=>e.getBoundingClientRect().height)')
    os.unlink(tmp.name)
    pages, cur, used = [], [], 0.0
    for i, h in enumerate(hs):
        if cur and used + h > avail - 8:
            pages.append(cur); cur, used = [], 0.0
        cur.append(i); used += h
    if cur:
        pages.append(cur)
    return pages


# ---------------------------------------------------------------- compose + render
def section(kind, body, no, edition, gutter_note=False, blank=False, exempt=False, label=''):
    par = 'recto' if no % 2 == 1 else 'verso'
    gl = ''   # no margin dash or tear note: the answer pages are printed double-sided and cannot be torn out (audit L17)
    if blank:
        return f'<section class="page {par} blank" data-kind="blank" data-no="{no}" data-exempt="1"></section>'
    foot = f'<div class="pf"><span class="folio">{no}</span><span>Math Inquirers &middot; Extension Workbook &middot; {esc(label)}</span></div>' if kind not in ('cover', 'cert', 'divider') else ''
    return (f'<section class="page {par} k-{kind}" data-kind="{kind}" data-no="{no}" data-exempt="{1 if exempt else 0}" data-label="{esc(label)}">'
            f'{gl}<div class="pg">{body}</div>{foot}</section>')


def build(level, unit_ids, outdir, bw=True):
    lv = CFG['levels'][str(level)]
    units = [json.load(open(os.path.join(EXT, 'data', f'l{level}_u{u:02d}.json'), encoding='utf-8')) for u in unit_ids]
    book = {'level': level, 'unit_titles': lv['units'], 'proof': len(units) < 10,
            'titles': {u['unit']: u['title'] for u in units}, 'lessons': {u['unit']: u.get('holiday_lesson') for u in units}}
    cfg_vars = (f"--fs:{lv['font_px']}px;--line:{lv['line_mm']}mm;--boxw:{lv['box_mm'][0]}mm;--boxh:{lv['box_mm'][1]}mm")
    css = font_css() + open(os.path.join(HERE, 'ext.css'), encoding='utf-8').read()
    os.makedirs(outdir, exist_ok=True)
    report = {'level': level, 'units': unit_ids, 'pages': [], 'problems': []}
    with sync_playwright() as p:
        br = p.chromium.launch(); page = br.new_page()
        # ---- answers
        blocks, block_unit = [], []
        for ui, u in enumerate(units):
            bl = render.answer_blocks(u, 5 + 1 + PG['pages_per_unit'] * ui)
            blocks += bl; block_unit += [u['unit']] * len(bl)
        apages = paginate_answers(page, blocks, css, cfg_vars)
        U = len(units)
        F = 5
        PPU = PG['pages_per_unit']
        unit_start = {u['unit']: F + 1 + PPU * i for i, u in enumerate(units)}
        progress_pg = F + PPU * U + 1
        pre_blank = (progress_pg + 2) % 2 == 0
        divider_pg = progress_pg + 2 + (1 if pre_blank else 0)
        ans_start = {}
        for pi, idxs in enumerate(apages):
            for i in idxs:
                ans_start.setdefault(block_unit[i], divider_pg + 1 + pi)
        ctx = {'unit_start': unit_start, 'progress_pg': progress_pg, 'divider_pg': divider_pg, 'ans_start': ans_start}
        assert divider_pg % 2 == 1, 'answer section must start on a right-hand page'
        built = {}
        for theme, edition in (('colour', 'soft'), ('bw', 'print')):
            secs = []
            no = 1
            def add(kind, body, **kw):
                nonlocal no
                secs.append(section(kind, body, no, edition, **kw)); no += 1
            add('cover', cover(book, theme), exempt=True, label='Cover')
            add('front', head_front('About this book', book) + licence(book, theme, ctx), label='About this book', exempt=True)
            add('front', head_front('Welcome', book) + welcome(book, theme, ctx), label='Welcome', exempt=True)
            add('front', head_front('Contents', book) + contents(book, theme, ctx), label='Contents', exempt=True)
            add('front', head_front('Pace plan', book) + pace(book, theme, ctx), label='Pace plan', exempt=True)
            for u in units:
                for pg in render.unit_pages(u, theme, lv):
                    add(pg['kind'], pg['body'], label=f'Unit {u["unit"]} &middot; {pg["label"]}'.replace('&middot;', '·'))
            add('front', head_front('My progress', book) + progress(book, theme, ctx), label='My progress', exempt=True)
            add('cert', certificate(book, theme, ctx), exempt=True, label='Certificate')
            if pre_blank:
                secs.append(section('blank', '', no, edition, blank=True)); no += 1
            add('divider', divider(book, theme, ctx), exempt=True, gutter_note=True, label='Answers')
            for idxs in apages:
                body = ans_head(book) + '<div class="pbody answers">' + ''.join(blocks[i] for i in idxs) + '</div>'
                add('answers', body, exempt=True, gutter_note=True, label='Answers')
            if edition == 'print' and (no - 1) % 2 == 1:
                secs.append(section('blank', '', no, edition, blank=True)); no += 1
            htm = (f'<!doctype html><html><head><meta charset="utf-8"><title>Math Inquirers Extension Workbook Level {level}</title>'
                   f'<style>{css}</style></head><body class="{theme} {edition}" style="{cfg_vars}">' + ''.join(secs) + '</body></html>')
            fn = os.path.join(outdir, f'_build_{edition}.html')
            open(fn, 'w', encoding='utf-8').write(htm)
            page.goto('file://' + fn); page.evaluate('document.fonts.ready'); page.wait_for_timeout(400)
            # natural fill + overflow, before stretching
            meas = page.evaluate('''() => Array.from(document.querySelectorAll('.page')).map(s => {
                const pb = s.querySelector('.pbody'); const pg = s.querySelector('.pg');
                if (!pb) return {no: +s.dataset.no, kind: s.dataset.kind, label: s.dataset.label, exempt: s.dataset.exempt === '1', fill: null, over: false};
                const top = pb.getBoundingClientRect().top; let bottom = top;
                Array.from(pb.children).forEach(c => { bottom = Math.max(bottom, c.getBoundingClientRect().bottom); });
                const hasSpace = pb.classList.contains('practice');
                const over = (bottom - top) > pb.clientHeight + 1 || pg.scrollHeight > pg.clientHeight + 1;
                return {no: +s.dataset.no, kind: s.dataset.kind, label: s.dataset.label, exempt: s.dataset.exempt === '1', fill: (bottom - top) / pb.clientHeight, over: over, excess_mm: Math.round(((bottom - top) - pb.clientHeight) / 3.7795 * 10) / 10};
            })''')
            # the page is a flex column: natural heights (children are not stretched yet)
            page.evaluate("document.body.classList.add('stretch')"); page.wait_for_timeout(200)
            after_over = page.evaluate("Array.from(document.querySelectorAll('.page')).filter(s=>{const pg=s.querySelector('.pg');return pg&&pg.scrollHeight>pg.clientHeight+1}).map(s=>+s.dataset.no)")
            for m in meas:
                m['edition'] = edition
                if m['over'] or m['no'] in after_over:
                    report['problems'].append(f'{edition} page {m["no"]} ({m["label"]}): content overflows the page (natural height minus body {m.get("excess_mm")} mm)')
                if m['fill'] is not None and not m['exempt'] and m['fill'] < PG['min_fill']:
                    report['problems'].append(f'{edition} page {m["no"]} ({m["label"]}): natural fill {m["fill"]:.2f} < {PG["min_fill"]}')
            report['pages'] += meas
            if edition == 'print':   # every hint must fit on one line (audit M6)
                wraps = page.evaluate('''() => Array.from(document.querySelectorAll('.hint')).filter(h => h.getBoundingClientRect().height > 30).map(h => h.parentElement.id)''')
                for w_ in wraps:
                    report['problems'].append(f'hint wraps to two lines: {w_}')
            name = f'Math_Inquirers_L{level}_Extension_Workbook_' + ('Soft_Copy_Colour.pdf' if edition == 'soft' else 'Print_BW.pdf')
            pdf = os.path.join(outdir, name)
            page.pdf(path=pdf, width='210mm', height='297mm', print_background=True, margin={'top': '0', 'bottom': '0', 'left': '0', 'right': '0'}, prefer_css_page_size=True)
            built[edition] = pdf
            os.unlink(fn)
            # in print: record pages
            report[edition + '_pages'] = no - 1
        br.close()
    finalise(built, units, ctx, level, lv)
    if bw:
        report['bw_pipeline'] = bw_print(built, outdir, level)
    json.dump(report, open(os.path.join(outdir, 'build_report.json'), 'w'), indent=1)
    return report, built


def bw_print(built, outdir, level):
    """Run the native black-and-white print PDF through the project print pipeline (print/make_bw_print.py: 1-bit, 600 dpi, CCITT G4,
    docs/printing/README_bw.md) and check it (print/check_bw.py).  The native vector PDF is kept as ..._Print_BW_vector.pdf (source and
    smaller reference); ..._Print_BW.pdf is the 1-bit file for the printer."""
    from pypdf import PdfReader, PdfWriter
    sys.path.insert(0, os.path.join(ROOT, 'print'))
    import make_bw_print as mb, check_bw
    vec = os.path.join(outdir, f'Math_Inquirers_L{level}_Extension_Workbook_Print_BW_vector.pdf')
    final = os.path.join(outdir, f'Math_Inquirers_L{level}_Extension_Workbook_Print_BW.pdf')
    os.replace(built['print'], vec)
    tmp = final[:-4] + '_tmp.pdf'
    n, dropped = mb.convert_pdf(vec, tmp)
    r = PdfReader(tmp); w = PdfWriter()
    for pg in r.pages:
        w.add_page(pg)
    w.add_metadata({'/Title': f'Math Inquirers Extension Workbook Level {level} (print, black and white, 1-bit 600 dpi)', '/Author': 'Math Inquirers',
                    '/Subject': 'Self-study extension workbook with answers'})
    with open(final, 'wb') as f:
        w.write(f)
    os.unlink(tmp)
    built['print'] = final; built['print_vector'] = vec
    bad = check_bw.check([final])
    return {'pages': n, 'dpi': mb.DPI, 'mb': round(os.path.getsize(final) / 1e6, 2), 'check_bw_failures': bad, 'pale_tint_dropped_max': max(dropped)}


def head_front(title, book):
    return f'<div class="ph"><span class="lv">Level {book["level"]}</span><span class="un">Extension Workbook</span></div>'


def finalise(built, units, ctx, level, lv):
    """PDF metadata and bookmarks (soft copy)."""
    from pypdf import PdfReader, PdfWriter
    for ed, pdf in built.items():
        r = PdfReader(pdf); w = PdfWriter()
        for pg in r.pages:
            w.add_page(pg)
        w.add_metadata({'/Title': f'Math Inquirers Extension Workbook Level {level} ({"soft copy, colour" if ed == "soft" else "print, black and white"})',
                        '/Author': 'Math Inquirers', '/Subject': 'Self-study extension workbook with answers'})
        if ed == 'soft':
            w.add_outline_item('Contents', 3)
            for u in units:
                w.add_outline_item(f'Unit {u["unit"]}: {u["title"]}', ctx['unit_start'][u['unit']] - 1)
            w.add_outline_item('My progress', ctx['progress_pg'] - 1)
            w.add_outline_item('Answers', ctx['divider_pg'] - 1)
        with open(pdf, 'wb') as f:
            w.write(f)


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--level', type=int, default=1)
    ap.add_argument('--units', default='')
    ap.add_argument('--out', default='')
    ap.add_argument('--no-bw', action='store_true', help='skip the 1-bit 600 dpi conversion (quick builds)')
    a = ap.parse_args()
    ids = [int(x) for x in a.units.split(',')] if a.units else sorted(int(re.search(r'_u(\d+)\.json', f).group(1)) for f in glob.glob(os.path.join(EXT, 'data', f'l{a.level}_u*.json')))
    out = a.out or os.path.join(ROOT, 'outputs', 'extension', f'L{a.level}')
    rep, built = build(a.level, ids, out, bw=not a.no_bw)
    for ed, f in built.items():
        print(ed, f, rep.get(ed + '_pages', ''), 'pages')
    for pr in rep['problems']:
        print('PROBLEM:', pr)
    sys.exit(1 if rep['problems'] or rep.get('bw_pipeline', {}).get('check_bw_failures') else 0)
