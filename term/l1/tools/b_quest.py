#!/usr/bin/env python3
"""Mi's Challenge Quest builder (replaces the old end-of-term check files).

Usage:  bash term/l1/build.sh 10      (build.py runs this for any lesson with a `challenge_quest` block: 10, 20, and later last lessons of a term)
Stand-alone:  python3 term/l1/tools/b_quest.py 10

Owner decision of 22 Oct 2026 (late): the end-of-term slot is a game with Mi, not a test. No score or mark is shown to the child,
no ranking, no visible timer, and no test / exam / check-sheet wording on any child or parent page.

Why this file exists: the shared tool tools/b_check.py hard-codes test-like labels (TERM n CHECK, End-of-term check, marks R/P/N, point
bands, a percent rule for the ruler line) and the file names L1x_Check_*.pdf, and tools/build.py runs it for any lesson that has an
`end_of_term_check` block. Shared tools are not edited here, so a lesson using the quest names its block `challenge_quest` (build.py then
skips b_check) and THIS script builds three files into term/l1/out/lNN/:
  LNN_Quest_Log.pdf          the child's pages (question layout and pictures reused from b_check, labels replaced)
  LNN_Quest_Tutor_Notes.pdf  tutor only: gates, answers, what to look for, the private notes sheet, group advice, the one-line templates
  LNN_Quest_Parent_Note.pdf  one page for grown-ups, with the one-line 'what we saw' promise
and runs its own checks (page counts, printed 10 cm bar when present, banned words in the real PDF text). Exit code 1 on any FAIL.
"""
import glob, html, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
L1 = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(L1, 'tools'))
import common                                   # noqa: E402
import b_check as bc                            # noqa: E402  (read only: question layout, pictures, CSS)
import pdfcheck                                 # noqa: E402
from common import E, mi_uri, font_css          # noqa: E402

NAME = "Mi's Challenge Quest"
# words that must never appear in the text of the child or parent PDFs (the tutor notes may say "no scores" etc.)
BAN_FAMILY = [r'\btests?\b', r'\bexams?\b', r'check[- ]?sheet', r'\bend-of-term check\b', r'\btimer\b', r'\bpass(ed)? or fail', r'\branked?\b|\branking\b',
              r'\bscored?\b|\bscores\b', r'\bmarked\b|\bmarks\b|\bmarking\b', r'\bout of\b', r'\bgrades?\b']
BAN_TUTOR = [r'check[- ]?sheet', r'\bend-of-term check\b', r'\bR/P/N\b', r'\bmarking sheet\b', r'\brecord sheet\b']


# ------------------------------------------------------------------ child pages: Quest Log

def quest_log_html(d):
    q = d['challenge_quest']
    t = d['term']
    shim = dict(d); shim['end_of_term_check'] = q            # b_check reads this key; the data lives under challenge_quest
    h = bc.sheet_html(shim)
    rep = [
        (f'Term {t} • Check', f'Term {t} • Quest'),
        ('End-of-term check • Start here level', NAME),
        (f'TERM {t} CHECK', "MI'S CHALLENGE QUEST"),
        (f'<title>Term {t} end-of-term check</title>', f'<title>{html.escape(NAME)}: Quest Log</title>'),
        ('<b class="t">Before you start</b>', '<b class="t">Mi says</b>'),
        ('Think harder (optional)', 'Secret cave (optional)'),
        ('You may skip this one. It is not marked.', 'You may skip this one. Mi will swim round it.'),
        ('Print check (for the grown-up):', 'Print-size bar (for the grown-up):'),
    ]
    for a, b in rep:
        if a.startswith('Print check'):                  # only present when the quest has a printed 10 cm bar
            h = h.replace(a, b); continue
        assert a in h, f'quest log: expected label not found in b_check output: {a!r}'
        h = h.replace(a, b)
    # a small quest map on page 1: eight stones and the cave; the child colours a stone for each gate they have had a go at
    stones = ''.join(f'<circle cx="{70 + i * 78}" cy="{34 + (8 if i % 2 else -8)}" r="18" fill="#fff" stroke="#1B2A49" stroke-width="3"/>'
                     f'<text x="{70 + i * 78}" y="{40 + (8 if i % 2 else -8)}" font-size="19" font-weight="700" text-anchor="middle" fill="#1B2A49" font-family="Fredoka, Arial, sans-serif">{i + 1}</text>' for i in range(8))
    cave = ('<path d="M664 56 Q664 6 692 6 Q720 6 720 56 Z" fill="#DDEBF7" stroke="#1B2A49" stroke-width="3"/>'
            '<circle cx="692" cy="40" r="7" fill="#FFF0C2" stroke="#1B2A49" stroke-width="2"/>')
    wave = '<path d="M20 38 Q45 18 70 34 T148 42 T226 34 T304 42 T382 34 T460 42 T538 34 T616 42 L664 38" fill="none" stroke="#1F7A6F" stroke-width="3" stroke-dasharray="3 7" stroke-linecap="round"/>'
    qmap = (f'<div style="margin:2px 4px 0 4px"><svg viewBox="0 0 740 66" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="quest map with {len(q["questions"])} stones and a cave" style="width:100%;height:auto;display:block">{wave}{stones}{cave}</svg>'
            '<div class="foot" style="margin:0 0 2px 2px">Colour a stone when you have had a go at that gate. If you skip a gate, Mi swims round it and you can still colour it.</div></div>')
    h = h.replace('</head>', '<style>.csheet .qbox .qn:before,.csheet .qn:before{content:"Gate "}</style></head>', 1)
    marker = '</ul></div>'
    assert marker in h
    if q.get('quest_map', True):                      # a lesson whose page 1 is full sets quest_map to false
        h = h.replace(marker, marker + qmap, 1)
    return h


# ------------------------------------------------------------------ tutor notes

def tutor_notes_html(d):
    c = d['challenge_quest']
    qs = c['questions']
    o = c['optional']
    smap = {s['id']: s for s in c['strands']}
    H = []
    H.append(f'<div class="cover"><img alt="Mi the dolphin" src="{mi_uri()}" style="position:absolute;right:18px;top:12px;width:90px">'
             f'<div class="k">TUTOR NOTES • LEVEL {d["level"]} • TERM {d["term"]} • {NAME.upper()}</div><h1>{E(c["title"])}</h1>'
             f'<p>{len(qs)} gates, one from each lesson of the term, all at Start here level, plus one optional secret cave item. {c["minutes"]} minutes after the break, played in pairs or as a group quest with Mi, working on private paper. '
             f'It is a game: no score or mark is shown to the child, no ranking, no visible timer. You keep private notes only. For the tutor: do not hand these notes to families.</p></div>')
    H.append(f'<div class="box t"><b>Where it sits.</b> {E(c["where"])}. <span class="small">{E(c["plan_note"])}</span></div>')
    H.append('<h2>1. The gates at a glance</h2><table><tr><th>Gate</th><th>From</th><th>Area (tutor label)</th><th>What it uses (Start here level)</th><th>Answer</th></tr>')
    for q in qs:
        H.append(f'<tr><td><b>{q["id"][1:]}</b></td><td>L{q["lesson"]}</td><td>{E(smap[q["strand"]]["moe_label"])}</td><td>{E(q["skill"])}</td><td class="ans">{E(q["answer"])}</td></tr>')
    H.append(f'<tr><td><b>Secret cave</b></td><td>L{o["lesson"]}</td><td>{E(smap[o["strand"]]["moe_label"])}</td><td>{E(o["skill"])} (optional)</td><td class="ans">{E(o["answer"])}</td></tr></table>')
    H.append('<p class="small">The area labels are for the tutor only and never appear on a child or parent page. Each gate is a fresh example of the Start here idea of its lesson (numbers chosen so that they do not repeat a lesson page), so a child who followed the lesson can open it. '
             'Before first use, read each gate against what the lesson actually taught.</p>')
    H.append('<h2>2. Playing it: before and during</h2><ol>' + ''.join(f'<li>{E(x)}</li>' for x in c['give']) + '</ol>')
    H.append('<h2>3. After the lesson: photos and your private notes</h2><ol>' + ''.join(f'<li>{E(x)}</li>' for x in c['after']) + '</ol>')
    H.append('<div class="box r"><b>Privacy checklist</b><ul>' + ''.join(f'<li>{E(x)}</li>' for x in c['privacy_checklist']) + '</ul></div>')
    H.append('<h3>Absent, late joiners, families who prefer not to, upset children</h3><ul>' + ''.join(f'<li>{E(x)}</li>' for x in c['late']) + '</ul>')
    H.append('<h2 class="pb">4. Answers and what to look for</h2><p class="small">Use these to understand what you see on camera and in the photos. Nothing is written on the child\'s paper, nothing is totalled and no gate is marked right or wrong in front of anyone. '
             'A child may write steps in any clear layout. Spelling and neatness do not matter.</p>')
    for q in qs + [dict(o, id='Optional', text=o['text'].replace('Think harder (optional). ', ''))]:
        lab = 'Secret cave (optional)' if q['id'] == 'Optional' else 'Gate ' + q['id'][1:]
        parts = '; '.join(f'({p["l"]}) {bc.keyclean(bc.minus(p["text"].replace("___", "__")))} = {p["ans"]}' if p['l'] else f'{bc.keyclean(bc.minus(p["text"].replace("___", "__")))} = {p["ans"]}' for p in q['parts'])
        right = q.get('right', 'The answer is as above.'); partly = q.get('partly', '-')
        H.append(f'<div class="box k1"><b>{lab}</b> (L{q["lesson"]}) {E(bc.keyclean(bc.minus(q["text"])))}<div class="ans">Answer: {E(bc.minus(q["answer"]))}</div><div class="small">{E(parts)}</div>'
                 f'<div class="small"><b>A secure answer looks like:</b> {E(right)} <b>Half way there:</b> {E(partly)}</div><div class="small"><b>Worked:</b> {E(bc.minus(q["solution"]))}</div>'
                 f'<div class="small"><b>Watch for:</b> {E("; ".join(q["mistakes"]))}</div></div>')
    if c.get('measure_note'):
        H.append(f'<div class="note">{E(c["measure_note"])}</div>')
    # --- the private notes sheet
    ns = c['notes_sheet']
    line = '<span style="display:inline-block;width:%s;border-bottom:1.5px dotted #8A94AD">&nbsp;</span>'
    H.append('<h2 class="pb">5. Tutor private notes (tutor only; one sheet per child; delete when the line is sent)</h2>')
    H.append(f'<p>Child (first name only): {line % "230px"} &nbsp; Date: {line % "110px"} &nbsp; Quest partner: {line % "150px"}</p>')
    H.append('<p class="small">' + E(ns['how']) + '</p>')
    H.append('<table class="rec"><tr><th style="width:56px">Gate</th><th style="width:40px">From</th><th>What I saw (words used, counters or drawing, how the partner helped, anything the child said)</th></tr>' + ''.join(
        f'<tr><td><b>{q["id"][1:]}</b></td><td>L{q["lesson"]}</td><td style="height:34px"></td></tr>' for q in qs) + f'<tr><td><b>Cave</b></td><td>L{o["lesson"]}</td><td style="height:34px"></td></tr></table>')
    H.append('<table><tr><th>Prompt</th><th>My notes</th></tr>' + ''.join(f'<tr><td style="width:36%">{E(p)}</td><td style="height:44px"></td></tr>' for p in ns['prompts']) + '</table>')
    H.append(f'<p>The one line for the grown-up (section 7), written from these notes:</p><div class="wl">&nbsp;</div><div class="wl">&nbsp;</div>')
    H.append('<h2 class="pb">6. Group advice for next term (tutor only; one sheet per class; no names)</h2>')
    H.append('<p class="small">' + E(ns['group_how']) + '</p>')
    H.append('<table><tr><th style="width:26%">Area</th><th>What several children were still working on (no names)</th><th>What I will do in the first two lessons of next term</th></tr>' + ''.join(
        f'<tr><td><b>{E(s["parent_name"])}</b><div class="small">Lessons {s["lessons"][0]} to {s["lessons"][-1]}: {E(s["looked_at"])}</div></td><td style="height:78px"></td><td></td></tr>' for s in c['strands']) + '</table>')
    H.append('<table><tr><th>Prompt</th><th>My notes</th></tr>' + ''.join(f'<tr><td style="width:36%">{E(p)}</td><td style="height:44px"></td></tr>' for p in ns['group_prompts']) + '</table>')
    # --- the one-line templates
    sl = c['saw_line']
    H.append('<h2 class="pb">7. The one line for the grown-up: what we saw</h2>')
    H.append(f'<div class="box t"><b>{E(sl["heading"])}</b><br>{E(sl["pattern"])}</div>')
    H.append('<p class="small">' + E(sl['how']) + '</p>')
    H.append('<table><tr><th>Area (parent wording)</th><th>Things you might have seen (pick the one your notes show; add the detail)</th><th>A next step that helps at home</th></tr>' + ''.join(
        f'<tr><td><b>{E(s["parent_name"])}</b><div class="small">{"Lessons" if len(s["lessons"]) > 1 else "Lesson"} {s["lessons"][0]}' + (f' to {s["lessons"][-1]}' if len(s["lessons"]) > 1 else '') + f'. We looked at {E(s["looked_at"])}.</div></td>'
        f'<td><ul>{"".join("<li>" + E(x) + "</li>" for x in s["saw_examples"])}</ul></td><td><ul>{"".join("<li>" + E(x) + "</li>" for x in s["next_examples"])}</ul></td></tr>' for s in c['strands']) + '</table>')
    H.append('<h3>A filled example (fictional child, Mei)</h3><div class="note">' + f'<b>{E(NAME)}: Mei</b><br>{E(sl["example"])}<br><br>{E(sl["closing"].replace("[Name]", "Mei"))}</div>')
    H.append('<p class="small">Words to avoid in the line: score, mark, out of, rank, top, below average, behind, ahead of, pass, fail, predicted, ready for. No claim about school exams, GEP or any contest, and no mention of other children. The line goes to the parent only. '
             'If the child skipped the secret cave or a gate, say nothing about it. If the child tried the secret cave, you may add: "[Name] also had a go at the secret cave."</p>')
    return f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{html.escape(NAME)}: tutor notes</title><style>{font_css()}{bc.KEY_CSS}ul{{margin:0 0 0 14px}}body{{font-size:11.6px;line-height:1.35}}h2{{margin:12px 0 5px}}</style></head><body>{"".join(H)}</body></html>'


# ------------------------------------------------------------------ the grown-up note

def parent_note_html(d):
    c = d['challenge_quest']
    n = c['parent_note']
    sl = c['saw_line']
    li = lambda xs: ''.join(f'<li>{E(x)}</li>' for x in xs)
    body = (f'<div class="hd"><img alt="Mi the dolphin" src="{mi_uri()}" style="width:20mm;height:auto"><div><div class="tp">Level {d["level"]} • Term {d["term"]} • For grown-ups</div><h1>{E(n["title"])}</h1></div></div>'
            f'<p style="margin:0 0 4px">{E(n["what"])}</p>'
            f'<h2>Before the lesson</h2><ul>{li(n["before"])}</ul>'
            f'<h2>During the quest</h2><ul>{li(n["during"])}</ul>'
            f'<h2>After the lesson: sending the Quest Log privately</h2><ul>{li(n["after"])}</ul>'
            f'<div class="panel"><b>What you get back.</b> {E(n["back"])}<br><i>{E(sl["parent_example"])}</i></div>'
            f'<p>{E(n["make_up"])}</p>'
            f'<p class="small">Your child\'s paper, photos and note are treated as private: we never show them to other children or families, and we never compare children. Math Inquirers by Preciouslyours Pte Ltd.</p>')
    return f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{html.escape(NAME)}: grown-up note</title><style>{font_css()}{bc.NOTE_CSS}</style></head><body>{body}</body></html>'


# ------------------------------------------------------------------ build and check

def pdf_text(path):
    return subprocess.run(['pdftotext', '-layout', path, '-'], capture_output=True, text=True).stdout


def build_quest(d, pw):
    c = d['challenge_quest']
    n = d['_num']
    od = os.path.join(L1, 'out', f'l{n}')
    os.makedirs(od, exist_ok=True)
    term = f'Math Inquirers Term {d["term"]}'
    log = bc.render(pw, quest_log_html(d), 'quest_log', od, f'L{n}_Quest_Log.pdf', f"{term} {NAME}. Print at 100% (actual size).", {'top': '12mm', 'bottom': '15mm', 'left': '14mm', 'right': '14mm'})
    notes = bc.render(pw, tutor_notes_html(d), 'quest_tutor_notes', od, f'L{n}_Quest_Tutor_Notes.pdf', f'{term} {NAME}. Tutor notes and private return plan. Tutor only.', {'top': '14mm', 'bottom': '16mm', 'left': '13mm', 'right': '13mm'})
    note = bc.render(pw, parent_note_html(d), 'quest_parent_note', od, f'L{n}_Quest_Parent_Note.pdf', '', {'top': '12mm', 'bottom': '12mm', 'left': '15mm', 'right': '15mm'})
    fails = []
    n_log = pdfcheck.pdf_pages(log)
    fills = pdfcheck.pdf_fill(log, 12.0, 15.0)
    print('quest log pages', n_log, 'fill', ', '.join(f'{f:.0%}' for f in fills))
    if n_log != c['sheet_pages']:
        fails.append(f'quest log has {n_log} pages, designed {c["sheet_pages"]}')
    for i, f in enumerate(fills, 1):
        if f < 0.40: fails.append(f'quest log page {i} only {f:.0%} full')
        elif f < 0.80: print(f'WARN quest log page {i} only {f:.0%} full')
        if f > 1.0: print(f'WARN quest log page {i} over full')
    nn = pdfcheck.pdf_pages(note)
    print('tutor notes pages', pdfcheck.pdf_pages(notes), 'fill', ', '.join(f'{f:.0%}' for f in pdfcheck.pdf_fill(notes, 14.0, 16.0)), '| parent note pages', nn)
    if nn != 1: fails.append('parent note must be one page')
    if c.get('sheet_check_bar_mm'):
        bar, _ = bc.measure_sheet(log, c)
        print('printed 10 cm bar measures', None if bar is None else f'{bar:.2f} mm')
        if bar is None or abs(bar - c['sheet_check_bar_mm']) > 0.6: fails.append(f'printed bar is {bar} mm, should be {c["sheet_check_bar_mm"]} mm')
    # banned words in the real PDF text
    for path, ban, who in ((log, BAN_FAMILY, 'child page'), (note, BAN_FAMILY, 'parent page'), (notes, BAN_TUTOR, 'tutor notes')):
        tx = pdf_text(path)
        for pat in ban:
            m = re.search(pat, tx, re.I)
            if m: fails.append(f'{os.path.basename(path)} ({who}) contains banned wording {pat!r}: ...{tx[max(0, m.start() - 40):m.end() + 40]!r}')
        if who != 'tutor notes' and 'Challenge Quest' not in re.sub(r'\s+', ' ', tx).title().replace("Mi'S", "Mi's"):
            fails.append(f'{os.path.basename(path)} ({who}) does not say {NAME}')
    # no leftover old files for this lesson
    for old in glob.glob(os.path.join(od, f'L{n}_Check_*.pdf')) + glob.glob(os.path.join(od, 'html', 'check_*.html')):
        fails.append(f'old end-of-term check file still present: {os.path.basename(old)} (delete it)')
    for f in fails: print('FAIL', f)
    if not fails: print('PASS  quest: Quest Log %d pages, tutor notes %d pages, grown-up note 1 page, no banned wording in the child and parent PDFs' % (n_log, pdfcheck.pdf_pages(notes)))
    print('built quest files in', od)
    return not fails


def main():
    num = sys.argv[1] if len(sys.argv) > 1 else '10'
    d = common.load(num)
    if 'challenge_quest' not in d:
        sys.exit(f'lesson {num} has no challenge_quest block')
    from playwright.sync_api import sync_playwright
    with sync_playwright() as pw:
        b = pw.chromium.launch()
        ok = build_quest(d, b)
        b.close()
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
