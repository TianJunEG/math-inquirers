#!/usr/bin/env python3
"""Build the extras package for level N (2..6):  python3 levels/mkextras.py 4   (or: all)

Makes, in outputs/designed/:
  Math_Inquirers_P<N>_Question_Bank.pdf
  Math_Inquirers_P<N>_Weekly_Email_Pack.pdf
  Math_Inquirers_P<N>_Free_Taster.pdf
  Math_Inquirers_P<N>_What_Learners_Get.pdf   (one page)
Everything is read from p<N>/data.js (via levels/extras_data.js), p<N>/parent_side.json and
outputs/deck_urls_all.json / deck_urls_p4_p6.md. No answers or numbers are written here: answers are copied
from the level's qbank and lesson keys, and a self-check at the end confirms each one is in the built pages.
Same look as the P1 documents (hp/doc_style.css, hp/wb_style.css, fonts/fonts.css).
Needs: node, python3, playwright + chromium, pypdf, reportlab.
"""
import html, io, json, os, re, subprocess, sys, tempfile
from collections import Counter
from playwright.sync_api import sync_playwright
from pypdf import PdfReader, PdfWriter

R = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
OUT = os.path.join(R, 'outputs', 'designed')
E = html.escape

# ---- per-level settings that are facts of the program (names from docs/levels_and_placement.md; kit from pN/kit.js) ----
LV = {
    2: dict(age='Ages 7-9', school='P2', long='Primary 2', kit=[
        ('Place-value cards', [1, 2, 10]), ('Digit cards', [1, 10]), ('Fraction strips', [7]), ('Paper clock', [9]),
        ('Paper strips of numbered squares', [9]), ('Cube nets', [8]), ('Play coins', [6]), ('Play notes and $1 coins', [6])]),
    3: dict(age='Ages 8-10', school='P3', long='Primary 3', kit=[
        ('Digit cards', [1, 2]), ('Fraction wall', [6]), ('Square grid', [7]), ('Right-angle testers', [8]),
        ('Play coins', [9]), ('Play notes and $1 coins', [9])]),
    4: dict(age='Ages 9-11', school='P4', long='Primary 4', kit=[
        ('Fraction wall', [4]), ('Square grid', [7, 8]), ('Dot grid', [8]), ('Cube net', [8]), ('Right-angle testers', [6])]),
    5: dict(age='Ages 10-12', school='P5', long='Primary 5', kit=[
        ('Fraction wall', [2, 3]), ('Square grid', [4]), ('Dot grid', [8]), ('Cube net', [5])]),
    6: dict(age='Ages 11-13', school='P6', long='Primary 6', kit=[
        ('Unplugged code cards', [1, 4, 7]), ('Square grid', [7, 9])]),
}


def load(n):
    r = subprocess.run(['node', os.path.join(R, 'levels', 'extras_data.js'), str(n)], capture_output=True, text=True, check=True, cwd=R)
    return json.loads(r.stdout)


def names(n):
    v = LV[n]
    if n == 6:
        return dict(short=f'P6 {v["age"]}', full='Ages 11-13 (maths + coding bridge, after PSLE)', head='Ages 11-13 (maths + coding bridge, after PSLE)', tag='Maths + coding bridge')
    return dict(short=f'P{n} {v["age"]}', full=f'{v["age"]} (builds on {v["long"]} maths)', head=f'{v["age"]} (builds on {v["long"]} maths)', tag='')


def css():
    return open(os.path.join(R, 'fonts', 'fonts.css')).read() + open(os.path.join(R, 'hp', 'doc_style.css')).read() + """
.bn{background:#fff;border:1.5px solid #1B2A49;border-left:8px solid #FFC93C;border-radius:10px;padding:5px 14px;margin:12px 0 6px;font:600 14px Fredoka,sans-serif;break-after:avoid}
.ql{display:flex;gap:10px;margin:5px 0;break-inside:avoid;font-size:14px;line-height:1.45}
.ql b{flex:none;width:38px;color:#1F7A6F}
.al{display:flex;gap:10px;margin:2px 0;font-size:12.6px;line-height:1.4;break-inside:avoid}
.al b{flex:none;width:38px;color:#D64545}
.lessonpage{break-before:page}
.sub2{font-style:italic;color:#555;margin:0 0 6px}
.mail{background:#fff;border:1.5px solid #C9D7E6;border-radius:12px;padding:10px 16px;margin:6px 0 12px;font-size:13.4px;line-height:1.5}
.mail p{margin:0 0 7px}
.mail .subj{font-weight:800}
.mail .att{font-style:italic;color:#4B5B7B}
.mail ol,.mail ul{margin:2px 0 7px;padding-left:20px}
.note{background:#FFF3CF;border-radius:10px;padding:6px 12px;font-size:13px;margin:6px 0}
"""


def pdf(htmlpath, out, foot, landscape=False, margin=None):
    if foot == 'x': ft = '<div></div>'
    else: ft = ('<div style="width:100%%;font-size:8.5px;color:#5B6785;padding:0 14mm;display:flex;justify-content:space-between;font-family:Arial">'
          '<span>%s</span><span>Page <span class="pageNumber"></span> of <span class="totalPages"></span></span></div>' % E(foot))
    with sync_playwright() as pw:
        b = pw.chromium.launch(); pg = b.new_page()
        pg.goto('file://' + htmlpath, wait_until='networkidle'); pg.wait_for_timeout(800)
        pg.pdf(path=out, format='A4', landscape=landscape, print_background=True, display_header_footer=True,
               header_template='<div></div>', footer_template=ft, margin=margin or {'top': '13mm', 'bottom': '15mm', 'left': '13mm', 'right': '13mm'})
        b.close()


def cover(title, sub):
    return ('<div class="cover"><div class="tag">Math Inquirers Holiday Program</div><h1>%s</h1><div class="sub">%s</div>'
            '<div class="slog">Notice it. Test it. Explain why.</div></div>' % (E(title), E(sub)))


def page(body, tmp, name):
    p = os.path.join(tmp, name)
    open(p, 'w').write('<!doctype html><html><head><meta charset="utf-8"><style>%s</style></head><body>%s</body></html>' % (css(), body))
    return p


def pages_of(path):
    return len(PdfReader(path).pages)


# ============================================================ (a) QUESTION BANK
# Neutral tier labels (same as the workbook and the P1 bank). Nobody is placed in a tier; any child may try any tier.
TIERS = [('core', 'S', 'START HERE (open with objects, drawing or counting)', 'Start here'), ('stretch', 'T', 'THINK HARDER (the lesson idea in a new setting)', 'Think harder'), ('challenge', 'G', 'GO FURTHER (after the topic: extend, justify, make up your own)', 'Go further')]


def build_qbank(n, d, tmp):
    nm = names(n); Q = d['qbank']; Ls = d['lessons']
    b = [cover('Question Bank', 'Three tiers of questions for every lesson, with answers')]
    b.append('<h2>%s</h2><p class="sub2">Math Inquirers %s%s. Notice it. Test it. Explain why.</p>' % ('Question Bank  •  ' + E(nm['head']), E(nm['short']), ' • ' + nm['tag'] if nm['tag'] else ''))
    b.append('<div class="bn">How to use this bank</div>')
    foundation = ('START HERE questions are approachable for a child who has not yet been taught the topic. They can start with objects, a drawing, counting, guess and check or skills from earlier years, and they use no unexplained words. Use them for warm-ups and to build confidence.' if n != 6 else
                  'START HERE questions are approachable for a child who has not yet been taught the topic. They can start with objects, a drawing, counting, guess and check or reading and tracing a short program, and they use no unexplained words. Use them for warm-ups and to build confidence.')
    items = [
        'Each lesson has three tiers: Start here, Think harder and Go further. They are open to everyone. Nobody is placed in a tier: every child can start with Start here, and any child may try Think harder or Go further at any time. Go further questions are good ones to talk about together.',
        foundation,
        'THINK HARDER questions need the idea taught in the lesson, used in a new setting: two-step problems, patterns with a hidden rule, unknowns and larger numbers.',
        'GO FURTHER questions need the topic well understood, plus an extension: find every way, work backwards, test a case, justify an answer, change the problem or make up your own. This program is inspired by research-based approaches used in gifted education; it is not an official GEP standard and is not affiliated with MOE.',
        'Ask for the reason every time: "How do you know?" A correct answer with no reason is only half done.',
    ]
    if n == 6: items.append('Some questions ask you to predict, trace or plan a short program. Children can test their answer in Scratch (or Python) after they have written their prediction on paper.')
    items.append('Answers are at the back. Do not hand the answer pages to children.')
    b.append('<ul>' + ''.join('<li>%s</li>' % E(x) for x in items) + '</ul>')
    b.append('<div class="bn">What each lesson practises</div><table class="tb" style="font-size:12px;line-height:1.1"><colgroup><col style="width:14%"><col style="width:56%"><col style="width:30%"></colgroup>')
    for l in Ls:
        q = Q[str(l['n'])]
        b.append('<tr><td class="hd">Lesson %d</td><td>%s (%s)</td><td>%d + %d + %d questions</td></tr>' % (l['n'], E(l['title']), E(l['topic']), len(q['core']), len(q['stretch']), len(q['challenge'])))
    b.append('</table>')
    for l in Ls:
        q = Q[str(l['n'])]
        b.append('<div class="lessonpage"><h2>Lesson %d: %s</h2><p class="sub2">%s  •  Week %d</p>' % (l['n'], E(l['title']), E(l['topic']), l['week']))
        for key, tag, label, _ in TIERS:
            b.append('<div class="bn">%s</div>' % E(label))
            for i, x in enumerate(q[key]): b.append('<div class="ql"><b>%s%d.</b><span>%s</span></div>' % (tag, i + 1, E(x['q'])))
        b.append('</div>')
    b.append('<div class="lessonpage"><h2>Answer key (tutor only)</h2>')
    for l in Ls:
        q = Q[str(l['n'])]
        b.append('<h3>Lesson %d: %s</h3>' % (l['n'], E(l['title'])))
        for key, tag, _, _ in TIERS:
            for i, x in enumerate(q[key]): b.append('<div class="al"><b>%s%d.</b><span>%s</span></div>' % (tag, i + 1, E(x['a'])))
    b.append('</div>')
    body = ''.join(b)
    p = page(body, tmp, 'qb.html')
    out = os.path.join(OUT, f'Math_Inquirers_P{n}_Question_Bank.pdf')
    pdf(p, out, f'Math Inquirers {nm["short"]} • Question Bank • Notice it. Test it. Explain why.')
    return out, body


# ============================================================ (b) WEEKLY EMAIL PACK
def deck_ids(n):
    ids = {}
    j = json.load(open(os.path.join(R, 'outputs', 'deck_urls_all.json')))
    for k in range(1, 11):
        if f'p{n}l{k}' in j: ids[k] = j[f'p{n}l{k}']
    if len(ids) < 10:   # P5 is only in the markdown list
        md = open(os.path.join(R, 'outputs', 'deck_urls_p4_p6.md')).read()
        sec = re.search(r'## P%d\b.*?(?=\n## |\Z)' % n, md, re.S)
        if sec:
            for m in re.finditer(r'L(\d+) ([A-Za-z0-9]{22})( \(empty\))?', sec.group(0)):
                if not m.group(3): ids.setdefault(int(m.group(1)), m.group(2))
    return ids


def build_email(n, d, tmp):
    nm = names(n); Ls = d['lessons']; side = d['side']; ids = deck_ids(n); kit = LV[n]['kit']
    b = [cover('Weekly Email Pack', f'Parent and tutor emails for the five weeks of the {nm["short"]} holiday program')]
    b.append('<h2>How to use this pack</h2><ul>')
    for x in [
        'Send the parent email and the Week N Student Pages PDF the day before the first lesson of that week.',
        'Send the tutor email with the Week N Tutor Scripts and Answers PDF at least two days before. Tutors only; the answers must not go to parents.',
        'Put parents in BCC so no one sees another family\'s email address. Get parents\' consent to email before you start (PDPA).',
        'Replace the words in [square brackets] before sending.',
        'The PDFs are in the weekly folder (Math_Inquirers_P%d_Weekly_PDFs.zip): Week1_Student_Pages.pdf to Week5_Student_Pages.pdf and Week1_Tutor_Scripts_and_Answers.pdf to Week5_Tutor_Scripts_and_Answers.pdf. The Week 1 student PDF also holds the inquiry journal page and all the cut-outs; the Week 5 PDF ends with the certificate.' % n,
        'The slide deck links in the tutor emails are private to you. Share each deck with the tutor first, or send them the file.']: b.append('<li>%s</li>' % E(x))
    if n == 6: b.append('<li>This level is online-first and children code on a computer, so the Week 1 parent email also asks for a laptop or desktop with Scratch open. Attach the Scratch warm-up handout to the Week 1 email if you have it ready.</li>')
    b.append('</ul>')
    for w in range(1, 6):
        la, lb = Ls[2 * w - 2], Ls[2 * w - 1]
        used = [nm_ for nm_, ls in kit if set(ls) & {la['n'], lb['n']}]
        if w == 1:
            kitp = ('The cut-out pages are at the end of the Week 1 PDF (%s). Please cut them out and keep them in one envelope; we use them through the program. The inquiry journal page is at the front.' % ', '.join(x.lower() if i else x for i, x in enumerate([k for k, _ in kit])))
            if used: kitp += ' This week\'s lessons use: %s.' % ', '.join(used).lower()
        elif used:
            kitp = 'Please keep the Week 1 envelope handy. This week\'s lessons use: %s.' % ', '.join(used).lower()
        else:
            kitp = 'No cut-outs are needed this week. Please keep the Week 1 envelope handy.'
        if w == 5: kitp += ' The Certificate of Completion is the last page of the Week 5 PDF.'
        if n == 5 and w == 5: kitp += ' Please note the changed day: Friday 25 December is a public holiday, so lesson 9 is on Wednesday 23 December (4:45 to 6:15 pm) and lesson 10 is on Sunday 27 December (4:15 to 5:45 pm). The two lessons are four days apart this week, not two, so there is time for the take-home questions between them.'
        if n == 6 and w == 1: kitp += ' Each child needs a laptop or desktop with internet for the coding parts (a tablet works for Scratch but is slower). Scratch is free at scratch.mit.edu and no account is needed; please let your child open it once before the first lesson. [Attach the Scratch warm-up handout if you have it.]'
        subj_topics = f'{la["topic"]} and {lb["topic"]}'
        learn = ''.join('<p><b>Lesson %d, %s (%s).</b> %s</p>' % (l['n'], E(l['title']), E(l['topic']), E(side[str(l['n'])][0])) for l in (la, lb))
        tip, ask = side[str(la['n'])][1], side[str(la['n'])][2]
        ask2 = side[str(lb['n'])][2]
        b.append('<div class="lessonpage"><h2>Week %d: Lessons %d and %d</h2><h3>Parent email</h3><div class="mail">' % (w, la['n'], lb['n']))
        b.append('<p class="subj">Subject: Math Inquirers %s Week %d: %s</p><p class="att">Attachment: Week%d_Student_Pages.pdf</p>' % (E(nm['short']), w, E(subj_topics), w))
        b.append('<p>Dear parents,</p><p>This week our Math Inquirers (%s) meet two topics, in lessons %d and %d.</p>%s' % (E(nm['head']), la['n'], lb['n'], learn))
        b.append('<p>Your child\'s workbook pages for this week are attached. Please print them single-sided if you can. Children will work on the pages in class, so there is no need to finish them in advance.</p>')
        b.append('<p>%s</p>' % E(kitp))
        b.append('<p>One thing to try at home (5 minutes): %s</p><p>Ask your child: %s or %s</p>' % (E(tip), E(ask), E(ask2)))
        b.append('<p>We are not looking for speed. We are looking for a child who can say what they noticed, test it, and explain why. If your child is stuck, please ask "What do you notice?" before you give the answer.</p>')
        b.append('<p>Warm regards,<br>[Your name]<br>Preciouslyours Pte Ltd<br>[Contact number]</p></div>')
        b.append('<h3 class="lessonpage">Week %d: Tutor email</h3><div class="mail">' % w + '<p class="subj">Subject: Math Inquirers %s Week %d tutor pack: Lessons %d and %d</p>' % (E(nm['short']), w, la['n'], lb['n']))
        b.append('<p class="att">Attachments: Week%d_Tutor_Scripts_and_Answers.pdf, Week%d_Student_Pages.pdf</p><p>Hi [tutor name],</p>' % (w, w))
        b.append('<p>Here is your pack for week %d: %s; %s.</p><p>Attached are the minute-by-minute scripts with answers for both lessons, and the student pages. The slide decks are linked below.</p><ul>' % (w, E(la['title']), E(lb['title'])))
        for l in (la, lb):
            u = ('https://claude.ai/artifact/' + ids[l['n']]) if l['n'] in ids else '[deck link to add: not yet published]'
            b.append('<li>Lesson %d deck: %s</li>' % (l['n'], E(u)))
        b.append('</ul><p>Before the lesson, please:</p><ol><li>Read both scripts once and try the Go further questions yourself.</li>')
        if n == 5 and w == 5: b.append('<li>Week 5 has a changed day: lesson 9 is on Wed 23 Dec (4:45 to 6:15 pm) and lesson 10 on Sun 27 Dec, four days apart instead of two. Confirm the Wednesday with every family early, and remind children at the end of lesson 9 that the take-home parts can be done in the four days.</li>')
        b.append('<li>Check your materials are ready. Lesson %d: %s Lesson %d: %s</li>' % (la['n'], E(la['materials']), lb['n'], E(lb['materials'])))
        b.append('<li>After each lesson, tick the Readiness Tracker for each child (four quick ticks) and send me the sheet.</li></ol>')
        b.append('<p>Please do not forward the answer pages to parents.</p><p>Thank you,<br>[Your name]</p></div></div>')
    b.append('<div class="lessonpage"><h2>Week 5 closing email to parents</h2><div class="mail"><p class="subj">Subject: Math Inquirers %s: thank you, and your child\'s certificate</p><p>Dear parents,</p>' % E(nm['short']))
    for para in ['Thank you for joining us for the Math Inquirers Holiday Program (%s). Your child\'s Certificate of Completion is the last page of the Week 5 PDF. Please print it and add your child\'s name.' % nm['head'],
                 'We would love your feedback in two minutes: [feedback form link]. What did your child enjoy most? What should we change?',
                 'If your child enjoyed the puzzles, tell us. Think harder and Go further questions are open to every child, and we will share more puzzles to try in the next holiday.']:
        b.append('<p>%s</p>' % E(para))
    b.append('<p>Warm regards,<br>[Your name]</p></div></div>')
    body = ''.join(b)
    p = page(body, tmp, 'em.html')
    out = os.path.join(OUT, f'Math_Inquirers_P{n}_Weekly_Email_Pack.pdf')
    pdf(p, out, f'Math Inquirers {nm["short"]} • Weekly Email Pack • Notice it. Test it. Explain why.')
    return out, body


# ============================================================ (c) FREE TASTER
def shorten_sheet(lines, keep=4):
    """Lesson 1 workbook sheet (same HTML the workbook uses), first `keep` questions, grouped in boxes like pN/wb_pdf.py."""
    body = '\n'.join(lines)
    out = []; openb = False; n_seen = 0
    INBOX = ('class="p sub', 'class="p ans', 'class="ln"', '<table class="tb"', 'class="p img', '<div style="height:')
    for line in body.split('\n'):
        core = line.replace('<div class="brk"></div>', '')
        m = re.search(r'<span class="qn">(\d+)</span>', core) if core.startswith('<div class="p q') else None
        if m:
            if int(m.group(1)) > keep: break
            if openb: out.append('</div></div>')
            out.append('<div class="qwrap"><div class="qbox">' + core); openb = True; continue
        if openb and any(core.startswith(x) or x in core[:40] for x in INBOX): out.append(core); continue
        if openb: out.append('</div></div>'); openb = False
        out.append(core)
    if openb: out.append('</div></div>')
    return '\n'.join(out), keep


def build_taster(n, d, tmp):
    nm = names(n); l1 = d['lessons'][0]; s1 = d['scripts']['1']; Q = d['qbank']
    sheet, keep = shorten_sheet(d['wb1'], 4)
    keys = [k for k in l1['key'] if int(k[0][1:]) <= keep]
    assert len(keys) == keep, 'lesson key does not cover the kept questions'
    wbcss = open(os.path.join(R, 'fonts', 'fonts.css')).read() + open(os.path.join(R, 'hp', 'wb_style.css')).read()
    hdr = ('<div class="p lh"><span class="lbadge">Free taster  •  Lesson 1</span><span class="ltopic">%s</span></div><div class="p ltitle">%s</div>'
           '<div class="p namer"><b>Name</b><span></span><b>Group</b><span style="max-width:90px"></span><b>Date</b><span style="max-width:110px"></span></div>' % (E(l1['topic']), E(l1['title'].upper())))
    sh = os.path.join(tmp, 'sheet.html')
    open(sh, 'w').write('<!doctype html><html><head><meta charset="utf-8"><style>%s</style></head><body>%s%s</body></html>' % (wbcss, hdr, sheet))
    sheet_pdf = os.path.join(tmp, 'sheet.pdf')
    with sync_playwright() as pw:
        b = pw.chromium.launch(); pg = b.new_page()
        pg.goto('file://' + sh, wait_until='networkidle'); pg.wait_for_timeout(1000)
        pg.pdf(path=sheet_pdf, format='A4', print_background=True, margin={'top': '14mm', 'bottom': '16mm', 'left': '14mm', 'right': '14mm'})
        b.close()

    # parent / tutor front page
    plan = [('Warm-up', l1['warmup']), ('Explore', l1['explore']), ('Mini-lesson', l1['mini']),
            ('Worksheet', 'The child works on questions 1 to %d of the Lesson 1 sheet (next pages), then checks them with the tutor.' % keep),
            ('Exit ticket', l1['exit']['q'])]
    mins = ['5 min', '8 min', '5 min', '9 min', '3 min']   # the 30-minute split; the content itself is Lesson 1 as published
    f = [cover('Free 30-minute taster', f'Lesson 1: {l1["title"]} ({l1["topic"]})  •  Math Inquirers {nm["short"]}{" • " + nm["tag"] if nm["tag"] else ""}')]
    f.append('<h2>What this is</h2><p>A short sample of a real Math Inquirers lesson for %s. It is Lesson 1 of the %s holiday program (%s), shortened to about 30 minutes: a warm-up, a hands-on explore, a mini-lesson, a few worksheet questions and an exit ticket. The same routine runs through all ten 90-minute lessons.</p>' % (E(nm['head']), E(LV[n]['long']), E(l1['title'])))
    f.append('<h2>The 30 minutes</h2><table class="tb"><colgroup><col style="width:9%"><col style="width:14%"><col style="width:77%"></colgroup>')
    f.append('<tr><td class="hd">Time</td><td class="hd">Part</td><td class="hd">What happens</td></tr>')
    for (a, t), m in zip(plan, mins): f.append('<tr><td>%s</td><td><b>%s</b></td><td>%s</td></tr>' % (m, a, E(t)))
    f.append('</table>')
    f.append('<h2>What you need</h2><p>%s</p><p><i>Online:</i> %s</p>' % (E(l1['materials']), E(l1['online'])))
    f.append('<div class="note">Pages in this file: this page, the child\'s worksheet (about two pages), then tutor notes with the answers. Do not give the tutor-notes pages to the child. This taster is enrichment for thinking skills; it does not promise exam results and is not affiliated with MOE or the Gifted Education Programme.</div>')
    front = page('<div style="zoom:.86">' + ''.join(f) + '</div>', tmp, 'front.html'); front_pdf = os.path.join(tmp, 'front.pdf')
    pdf(front, front_pdf, 'x')
    # tutor notes
    t = ['<h2>Tutor notes: Lesson 1, %s</h2>' % E(l1['title']), '<p class="sub2">%s  •  %s</p>' % (E(l1['topic']), E(nm['head']))]
    t.append('<h3>Goal</h3><p>%s</p><p><b>Skills:</b> %s</p>' % (E(l1['objective']), E(l1['skills'])))
    t.append('<h3>Opening</h3>' + ''.join('<p>%s</p>' % E(x) for x in s1['hook']))
    t.append('<h3>Warm-up (about 5 minutes)</h3><p>%s</p>' % E(l1['warmup']) + ''.join('<p>%s</p>' % E(x) for x in s1['warmIntro']))
    t.append('<h3>Explore (about 8 minutes)</h3><p>%s</p>' % E(l1['explore']) + ''.join('<p><i>Predict:</i> %s</p>' % E(x) for x in s1['predict']) + '<ul>' + ''.join('<li>%s</li>' % E(x) for x in s1['exploreHints']) + '</ul>')
    t.append('<h3>Mini-lesson (about 5 minutes)</h3><p>%s</p>' % E(l1['mini']))
    t.append('<h3>Worksheet answers (questions 1 to %d)</h3><table class="tb"><colgroup><col style="width:9%%"><col style="width:91%%"></colgroup>' % keep + ''.join('<tr><td class="hd">%s</td><td>%s</td></tr>' % (E(k), E(v)) for k, v in keys) + '</table>')
    t.append('<h3>Talk time</h3><p>%s</p><p><b>Answer:</b> %s</p>' % (E(l1['share']), E(s1['talkAns'])))
    t.append('<h3>Exit ticket (about 3 minutes)</h3><p>%s</p><p><b>Answer:</b> %s</p>' % (E(l1['exit']['q']), E(l1['exit']['a'])))
    t.append('<h3>Watch for these mistakes</h3><ul>' + ''.join('<li>%s</li>' % E(x) for x in l1['mistakes']) + '</ul>')
    t.append('<h3>Go further (open to every child)</h3><p>%s</p>' % E(l1['extension']))
    t.append('<h3>After the taster</h3><p>Tell the parent one thing their child noticed and one thing they explained well. Then share the next steps: [dates, fee and sign-up link]. The free Placement Check for %s confirms the level: 70%% or more, enrol at that level; 40-69%%, enrol with a support note or choose one level down; under 40%%, one level down; 90%%+ may also try the check one level up. The parent has the final say.</p>' % E(nm['head']))
    notes = page(''.join(t), tmp, 'notes.html'); notes_pdf = os.path.join(tmp, 'notes.pdf')
    pdf(notes, notes_pdf, 'x')
    # merge + stamp footers with page numbers
    w = PdfWriter()
    for src in (front_pdf, sheet_pdf, notes_pdf):
        for pg_ in PdfReader(src).pages: w.add_page(pg_)
    buf = io.BytesIO(); w.write(buf); buf.seek(0)
    r = PdfReader(buf); total = len(r.pages)
    from reportlab.pdfgen import canvas
    w2 = PdfWriter()
    for i, pg_ in enumerate(r.pages):
        pw_, ph_ = float(pg_.mediabox.width), float(pg_.mediabox.height)
        ob = io.BytesIO(); c = canvas.Canvas(ob, pagesize=(pw_, ph_)); c.setFillColorRGB(.357, .404, .522); c.setFont('Helvetica', 8)
        c.drawString(40, 20, f'Free 30-minute taster  •  Math Inquirers {nm["short"]}  •  Notice it. Test it. Explain why.')
        c.drawRightString(pw_ - 40, 20, f'Page {i + 1} of {total}'); c.save(); ob.seek(0)
        pg_.merge_page(PdfReader(ob).pages[0]); w2.add_page(pg_)
    out = os.path.join(OUT, f'Math_Inquirers_P{n}_Free_Taster.pdf')
    with open(out, 'wb') as fh: w2.write(fh)
    return out, ''.join(f) + sheet + ''.join(t)


# ============================================================ (d) WHAT LEARNERS GET (one page)
def build_wlg(n, d, tmp):
    nm = names(n); Ls = d['lessons']; kit = LV[n]['kit']
    wbpages = pages_of(os.path.join(R, f'p{n}', f'Math_Inquirers_P{n}_Student_Workbook_Designed.pdf'))
    skills = Counter()
    for l in Ls:
        for s in set(x.strip() for x in re.split(r',\s*(?![^()]*\))', l['skills'])): skills[s] += 1
    common = [s for s, c in skills.most_common() if c >= 2][:6]
    kitnames = ', '.join(x.lower() if i else x for i, x in enumerate(k for k, _ in kit))
    rows = [('Student workbook', f'{wbpages} printable pages: 10 lessons with Start here, Think harder and Go further questions', 'Weekly pages by email; full book at the start'),
            ('Inquirer Kit (cut-outs)', kitnames + '. Nothing needs to be bought.', 'Week 1 pages'),
            ('Inquiry Journal', 'A stamp page at the front of the workbook. The tutor stamps a box after each lesson.', 'Every lesson'),
            ('Exit ticket', 'One short question at the end of each lesson to show what they understood', 'Every lesson'),
            ('Certificate of Completion', 'A printable certificate with the child\'s name', 'Week 5'),
            ('Weekly parent email', 'That week\'s workbook pages plus one thing to try at home', 'Weekly')]
    if n == 6: rows.insert(2, ('Python option', 'An optional Python version of each lesson\'s coding task, for children who already know Python', 'Optional'))
    routine = 'warm-up, explore with objects, mini-lesson, brain break, worksheet, talk time and exit ticket'
    hw = ('Each child needs a laptop or desktop with internet (a tablet works for Scratch but is slower). Scratch is free and needs no account.' if n == 6 else '')
    rule1 = 'Notice the pattern. Test it with objects. Check your answer. Explain why.' if n != 6 else 'Notice the pattern. Test it, often in code. Check your answer. Explain why.'
    topics = ''.join('<span class="chip"><b>%d</b> %s</span>' % (l['n'], E(l['title'])) for l in Ls)
    b = f'''<div class="wl">
<div class="top"><div class="tg">Math Inquirers Holiday Program</div><h1>What Learners Get</h1>
<div class="sb">{E(nm['head'])}{' • ' + E(nm['tag']) if nm['tag'] else ''}  •  10 lessons  •  5 weeks  •  small groups (up to 8 per tutor)  •  live online from home</div></div>
<h2>In one line</h2><p>Your child gets 15 hours of hands-on maths thinking with a tutor, a printed workbook and cut-out kit, a stamped Inquiry Journal, and the chance to move on to harder puzzles when they are ready.</p>
<div class="cols"><div><h2>In the lessons</h2><ul>
<li><b>Teaching time.</b> Ten lessons of 90 minutes, two a week for five weeks (15 hours in all).</li>
<li><b>A clear routine.</b> Every lesson: {routine}.</li>
<li><b>Small group.</b> Up to 8, so the tutor can ask each child "How do you know?"</li>
<li><b>A way of thinking.</b> The four Inquirer rules: {rule1}</li>
<li><b>Three tiers of questions.</b> Start here, Think harder and Go further, plus an open Investigation. All are open to every child; nobody is placed in a tier.</li></ul>
{('<p class="hw">' + E(hw) + '</p>') if hw else ''}</div>
<div><h2>Progress and feedback</h2><ul>
<li><b>Progress marks</b> after every exit ticket: secure, developing, or needs help.</li>
<li><b>Readiness tracker:</b> four signs of readiness for harder work, noted after each lesson.</li>
<li><b>Room to go further:</b> Think harder and Go further questions and an open Investigation are there for any child who wants more.</li>
<li><b>Parent feedback:</b> a short, honest note about how your child thinks, not just a score.</li></ul></div></div>
<h2>Ten topics</h2><div class="chips">{topics}</div>
<h2>What the child takes home</h2><table class="tb"><tr><td class="hd">Item</td><td class="hd">What it is</td><td class="hd">When</td></tr>
{''.join('<tr><td><b>%s</b></td><td>%s</td><td>%s</td></tr>' % (E(a), E(b_), E(c)) for a, b_, c in rows)}</table>
<div class="cols"><div><h2>Skills your child builds</h2><ul>{''.join('<li>%s</li>' % E(s[0].upper() + s[1:]) for s in common)}<li>Explaining thinking out loud, in words and drawings</li></ul></div>
<div><h2>What is not included</h2><ul><li>It is enrichment. It does not replace school maths or follow a school syllabus, and it is not linked to MOE or the Gifted Education Programme.</li><li>No exam or ranking. Readiness notes are private to your family.</li></ul>
<h2>Planned price (to confirm)</h2><p>S$650 per child for the 15-hour programme (S$65 a lesson), with the printed workbook, cut-out kit and all materials included. Introductory price for the first intake: S$500 (S$50 a lesson). Same price at every level.</p></div></div></div>'''
    extra = '''
@page{size:A4;margin:0}
.wl{font-size:10.6px;line-height:1.38}
.wl .top{background:#1B2A49;color:#FFF9EC;border-radius:16px;padding:12px 18px;margin-bottom:6px;position:relative;overflow:hidden}
.wl .top:after{content:"";position:absolute;right:-24px;top:-24px;width:90px;height:90px;border-radius:50%;background:#FFC93C}
.wl .tg{display:inline-block;background:#FFC93C;color:#1B2A49;font:700 9px 'Nunito Sans';letter-spacing:.08em;text-transform:uppercase;border-radius:999px;padding:2px 10px}
.wl h1{font:600 24px Fredoka;margin:6px 0 2px}.wl .sb{font-size:11px;color:#C9D3E6;max-width:78%}
.wl h2{font:600 13.5px Fredoka;margin:7px 0 3px;padding:2px 10px;border-left:6px solid #FFC93C;background:#fff;border-radius:8px}
.wl p{margin:0 0 4px}.wl ul{margin:1px 0 3px;padding-left:15px}.wl li{margin:1px 0}
.wl .cols{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.wl .chips{display:flex;flex-wrap:wrap;gap:4px}.wl .chip{background:#fff;border:1px solid #1B2A49;border-radius:999px;padding:1px 9px;font-size:10px}.wl .chip b{color:#1F7A6F}
.wl .tb{font-size:9.8px;margin:2px 0 4px}.wl .tb td{padding:3px 6px}
.wl .hw{background:#FFF3CF;border-radius:8px;padding:3px 8px}
'''
    p = os.path.join(tmp, 'wl.html')
    open(p, 'w').write('<!doctype html><html><head><meta charset="utf-8"><style>%s%s</style></head><body style="padding:12mm 13mm 0">%s</body></html>' % (css().replace('@page{size:A4;margin:13mm 13mm 15mm}', ''), extra, b))
    out = os.path.join(OUT, f'Math_Inquirers_P{n}_What_Learners_Get.pdf')
    ft = '<div style="width:100%%;font-size:8px;color:#5B6785;padding:0 13mm;display:flex;justify-content:space-between;font-family:Arial"><span>Math Inquirers %s • What Learners Get • Notice it. Test it. Explain why.</span><span></span></div>' % E(nm['short'])
    with sync_playwright() as pw:
        br = pw.chromium.launch(); pg = br.new_page()
        pg.goto('file://' + p, wait_until='networkidle'); pg.wait_for_timeout(800)
        pg.pdf(path=out, format='A4', print_background=True, display_header_footer=True, header_template='<div></div>', footer_template=ft, margin={'top': '0', 'bottom': '10mm', 'left': '0', 'right': '0'})
        br.close()
    return out, b


# ============================================================ self-check
def plain(s): return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', s))).strip()


def check(n, d, bodies):
    """Every qbank answer must be in the question bank HTML; every lesson-1 key entry in the taster; counts match the data."""
    problems = []
    qb = plain(bodies['qb']); ta = plain(bodies['ta'])
    for l in d['lessons']:
        q = d['qbank'][str(l['n'])]
        for t in ('core', 'stretch', 'challenge'):
            for x in q[t]:
                if plain(E(x['a'])) not in qb: problems.append(f'L{l["n"]} {t}: answer missing: {x["a"][:40]}')
                if plain(E(x['q'])) not in qb: problems.append(f'L{l["n"]} {t}: question missing: {x["q"][:40]}')
    for k, v in d['lessons'][0]['key'][:4]:
        if plain(E(v)) not in ta: problems.append(f'taster key missing {k}')
    if plain(E(d['lessons'][0]['exit']['a'])) not in ta: problems.append('taster exit answer missing')
    # numbers in the emails and sheet come from data: lesson numbers and counts only
    return problems


def main(n):
    d = load(n); os.makedirs(OUT, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        qb, qbb = build_qbank(n, d, tmp); em, _ = build_email(n, d, tmp); ta, tab = build_taster(n, d, tmp); wl, _ = build_wlg(n, d, tmp)
    probs = check(n, d, {'qb': qbb, 'ta': tab})
    for f in (qb, em, ta, wl): print(f'P{n}', os.path.basename(f), pages_of(f), 'pages')
    print(f'P{n} self-check:', 'OK' if not probs else probs)
    if pages_of(wl) != 1: print(f'WARNING P{n} What Learners Get is {pages_of(wl)} pages')
    return not probs


if __name__ == '__main__':
    arg = sys.argv[1] if len(sys.argv) > 1 else 'all'
    ok = all([main(n) for n in (range(2, 7) if arg == 'all' else [int(arg)])])
    sys.exit(0 if ok else 1)
