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
            f'<div>{ICON["think"].replace("<svg", "<svg fill=\"currentColor\" stroke=\"currentColor\"")}<span><b>Think harder.</b> Longer problems. Hints are upside down.</span></div>'
            f'<div>{ICON["go"].replace("<svg", "<svg fill=\"currentColor\" stroke=\"currentColor\"")}<span><b>Go further.</b> Big challenges, just for fun.</span></div>'
            f'<div>{ICON["quiz"].replace("<svg", "<svg fill=\"none\" stroke=\"currentColor\"")}<span><b>Check yourself.</b> Four quick questions at the end.</span></div></div>')


def welcome(book, theme, ctx):
    return (f'<div class="pbody"><div style="display:flex;align-items:flex-end"><div><div class="h1">Welcome!</div>'
            f'<div class="lead">This book is for you to explore at your own pace. Every unit has 7 pages. You do not need a teacher.</div></div>'
            f'<img class="welcome-mi" alt="Mi the dolphin" src="{mi_uri("mi_writing_desk", theme)}"></div>'
            '<div class="two"><div class="box"><h3>For the child</h3><ol>'
            '<li>Read <b>Learn it</b>. Look at the worked example.</li><li>Do <b>Start here</b>. Write in the boxes and on the lines.</li>'
            '<li>Try <b>Think harder</b>. Stuck? Read the hint. It is upside down!</li><li>Try <b>Go further</b> when you want a big challenge.</li>'
            '<li>Do <b>Check yourself</b> and count your score.</li></ol></div>'
            '<div class="box"><h3>For the grown-up</h3><ul>'
            '<li>Practice for the same ideas as the Holiday Program, with new numbers and stories.</li>'
            '<li>About 3 short sessions a week, 20 to 25 minutes each (see the pace plan).</li>'
            '<li>Let your child try before looking at the answers.</li>'
            f'<li>Answers are at the back, from page {ctx["divider_pg"]}, with a short reason for each. Read the reason together.</li>'
            '<li>Check yourself score 2 or less? Repeat Learn it and one Start here page.</li></ul></div></div>'
            '<div class="box"><h3>The four labels</h3>' + legend() + '</div>'
            '<div class="box"><h3>Tips</h3><ul><li>Use a pencil. Mistakes help you learn.</li><li>Read each question twice before you write.</li>'
            '<li>Think harder and Go further are not a race. Come back another day.</li></ul></div></div>')


def contents(book, theme, ctx):
    rows = []
    for n, title in enumerate(book['unit_titles'], 1):
        built = n in ctx['unit_start']
        if built:
            rows.append(f'<tr><td class="n">{n}</td><td class="t"><b>{esc(title)}</b><small>Learn it, practice and check &middot; answers on page {ctx["ans_start"][n]}</small></td><td class="p">page {ctx["unit_start"][n]}</td></tr>')
        else:
            rows.append(f'<tr class="later"><td class="n">{n}</td><td class="t"><b>{esc(title)}</b><small>Not in this proof edition</small></td><td class="p">&ndash;</td></tr>')
    extra = (f'<tr><td class="n"></td><td class="t"><b>My progress</b></td><td class="p">page {ctx["progress_pg"]}</td></tr>'
             f'<tr><td class="n"></td><td class="t"><b>My certificate</b></td><td class="p">page {ctx["progress_pg"] + 1}</td></tr>'
             f'<tr><td class="n"></td><td class="t"><b>Answers</b><small>For grown-ups, with short reasons</small></td><td class="p">page {ctx["divider_pg"]}</td></tr>')
    return f'<div class="pbody"><div class="h1">Contents</div><table class="toc">{"".join(rows)}{extra}</table></div>'


def pace(book, theme, ctx):
    rows = []
    for n, title in enumerate(book['unit_titles'], 1):
        if n in ctx['unit_start']:
            s = ctx['unit_start'][n]
            rows.append(f'<tr><td><b>{n}</b></td><td class="l"><b>{esc(title)}</b></td><td>Pages {s}-{s + 1}<br>Learn it, Start here</td><td>Pages {s + 2}-{s + 3}<br>Start here</td><td>Pages {s + 4}-{s + 6}<br>Think harder, Go further, Check yourself</td>'
                        '<td><span class="tick"></span></td></tr>')
        else:
            rows.append(f'<tr><td><b>{n}</b></td><td class="l"><b>{esc(title)}</b></td><td colspan="3">Not in this proof edition</td><td><span class="tick"></span></td></tr>')
    return ('<div class="pbody"><div class="h1">My pace plan</div>'
            '<div class="lead">One unit a week for 10 weeks. Three short sessions a week, about 20 to 25 minutes each. Tick the box when the week is done.</div>'
            '<table class="grid"><tr><th>Week</th><th>Unit</th><th>Session 1</th><th>Session 2</th><th>Session 3</th><th>Done</th></tr>' + ''.join(rows) +
            '<tr><td><b>11</b></td><td class="l"><b>Catch-up week</b></td><td colspan="3">Repeat any Check yourself where your score was 2 or less.</td><td><span class="tick"></span></td></tr></table>'
            '<div class="box"><h3>Tips for the grown-up</h3><ul><li>Short and often works better than one long session. Stop while your child still wants more.</li>'
            '<li>Sessions 1 and 2 are the main path. Session 3 has the harder pages: it is fine to do only some of them.</li>'
            '<li>Missed a week? Just carry on. There is no deadline.</li></ul></div></div>')


def progress(book, theme, ctx):
    rows = []
    for n, title in enumerate(book['unit_titles'], 1):
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
    return ('<div class="divider"><h1>Answers</h1><p>For grown-ups. Please let your child try each question first, then read the short reason together.</p>'
            '<p>Printed copy: this section is at the end of the book. If you want to keep the answers apart while your child works, take these pages out along the dashed line in the margin.</p></div>')


def ans_head(book):
    return f'<div class="ph"><span class="lv">Level {book["level"]}</span><span class="un">Answers</span><span class="nm" style="font-weight:700">for grown-ups</span></div>'


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
    gl = ''
    if edition == 'print' and gutter_note:
        gl = '<div class="gutterline"></div>' + ('<div class="gutternote">Answer pages: tear or cut along the dashed line to take them out</div>' if kind == 'divider' else '')
    if blank:
        return f'<section class="page {par} blank" data-kind="blank" data-no="{no}" data-exempt="1"></section>'
    foot = f'<div class="pf"><span class="folio">{no}</span><span>Math Inquirers &middot; Extension Workbook &middot; {esc(label)}</span></div>' if kind not in ('cover', 'cert', 'divider') else ''
    return (f'<section class="page {par} k-{kind}" data-kind="{kind}" data-no="{no}" data-exempt="{1 if exempt else 0}" data-label="{esc(label)}">'
            f'{gl}<div class="pg">{body}</div>{foot}</section>')


def build(level, unit_ids, outdir):
    lv = CFG['levels'][str(level)]
    units = [json.load(open(os.path.join(EXT, 'data', f'l{level}_u{u:02d}.json'), encoding='utf-8')) for u in unit_ids]
    book = {'level': level, 'unit_titles': lv['units'], 'proof': len(units) < 10}
    cfg_vars = (f"--fs:{lv['font_px']}px;--line:{lv['line_mm']}mm;--boxw:{lv['box_mm'][0]}mm;--boxh:{lv['box_mm'][1]}mm")
    css = font_css() + open(os.path.join(HERE, 'ext.css'), encoding='utf-8').read()
    os.makedirs(outdir, exist_ok=True)
    report = {'level': level, 'units': unit_ids, 'pages': [], 'problems': []}
    with sync_playwright() as p:
        br = p.chromium.launch(); page = br.new_page()
        # ---- answers
        blocks, block_unit = [], []
        for u in units:
            bl = render.answer_blocks(u)
            blocks += bl; block_unit += [u['unit']] * len(bl)
        apages = paginate_answers(page, blocks, css, cfg_vars)
        U = len(units)
        F = 4
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
                return {no: +s.dataset.no, kind: s.dataset.kind, label: s.dataset.label, exempt: s.dataset.exempt === '1', fill: (bottom - top) / pb.clientHeight, over: over};
            })''')
            # the page is a flex column: natural heights (children are not stretched yet)
            page.evaluate("document.body.classList.add('stretch')"); page.wait_for_timeout(200)
            after_over = page.evaluate("Array.from(document.querySelectorAll('.page')).filter(s=>{const pg=s.querySelector('.pg');return pg&&pg.scrollHeight>pg.clientHeight+1}).map(s=>+s.dataset.no)")
            for m in meas:
                m['edition'] = edition
                if m['over'] or m['no'] in after_over:
                    report['problems'].append(f'{edition} page {m["no"]} ({m["label"]}): content overflows the page')
                if m['fill'] is not None and not m['exempt'] and m['fill'] < PG['min_fill']:
                    report['problems'].append(f'{edition} page {m["no"]} ({m["label"]}): natural fill {m["fill"]:.2f} < {PG["min_fill"]}')
            report['pages'] += meas
            name = f'Math_Inquirers_L{level}_Extension_Workbook_' + ('Soft_Copy_Colour.pdf' if edition == 'soft' else 'Print_BW.pdf')
            pdf = os.path.join(outdir, name)
            page.pdf(path=pdf, width='210mm', height='297mm', print_background=True, margin={'top': '0', 'bottom': '0', 'left': '0', 'right': '0'}, prefer_css_page_size=True)
            built[edition] = pdf
            os.unlink(fn)
            # in print: record pages
            report[edition + '_pages'] = no - 1
        br.close()
    finalise(built, units, ctx, level, lv)
    json.dump(report, open(os.path.join(outdir, 'build_report.json'), 'w'), indent=1)
    return report, built


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
            w.add_outline_item('Contents', 2)
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
    a = ap.parse_args()
    ids = [int(x) for x in a.units.split(',')] if a.units else sorted(int(re.search(r'_u(\d+)\.json', f).group(1)) for f in glob.glob(os.path.join(EXT, 'data', f'l{a.level}_u*.json')))
    out = a.out or os.path.join(ROOT, 'outputs', 'extension', f'L{a.level}')
    rep, built = build(a.level, ids, out)
    for ed, f in built.items():
        print(ed, f, rep[ed + '_pages'], 'pages')
    for pr in rep['problems']:
        print('PROBLEM:', pr)
    sys.exit(1 if rep['problems'] else 0)
