#!/usr/bin/env python3
"""Builds the MOCK reports from SYNTHETIC data only: docs/online_report_mock/mock_reports.html and .pdf.
    python3 practice/submit/mock_report.py
No real child, parent or answer is used. The names are invented nicknames. It shows the report designs described in docs/online_submission_design.md (section 4):
 A. parent summary for one child (kind words, no scores, no ranking, no streaks)
 B. tutor view of one child (every question, mistakes with the likely misconception from the item's 'slips')
 C. tutor view of a group (one row per child in alphabetical order, never sorted by result; skills as words; common slips for planning)
 D. owner funnel counts (admin page)
"""
import html, os, sys
os.environ.setdefault('PLAYWRIGHT_BROWSERS_PATH', '/opt/pw-browsers')
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(os.path.dirname(os.path.dirname(HERE)), 'docs', 'online_report_mock')
E = html.escape

# ---- synthetic unit: 12 items, 4 skills (strand label is tutor-facing only)
STRAND = 'Whole Numbers'
ITEMS = [  # id, skill, mode, text, slip (likely misconception) or None
 ('S01', 'Place value to 1000', 'auto', 'Write the number: 4 hundreds, 0 tens, 7 ones', 'Wrote 47: the zero tens was left out, so the digits were not kept in their places.'),
 ('S02', 'Place value to 1000', 'auto', 'What is the value of the 6 in 365?', 'Said 6: gave the digit, not the value (6 tens = 60).'),
 ('S03', 'Place value to 1000', 'auto', '10 more than 595', 'Said 505: changed only the tens digit and did not carry to the hundreds.'),
 ('S04', 'Comparing and ordering', 'auto', 'Which is greater: 745 or 754?', 'Chose by the last digit only instead of comparing hundreds, then tens.'),
 ('S05', 'Comparing and ordering', 'auto', 'Order smallest first: 508, 85, 580, 805', 'Treated 85 as bigger than 508: looked at the first digit only, not at how many digits.'),
 ('S06', 'Comparing and ordering', 'auto', 'Circle <, = or >: 399 ... 401', None),
 ('S07', 'Patterns on the 1000 chart', 'auto', 'Count on in 100s: 235, __, __', 'Counted on in 10s: changed the tens digit instead of the hundreds digit.'),
 ('S08', 'Patterns on the 1000 chart', 'auto', 'What comes 1 row below 347 on the chart?', None),
 ('S09', 'Making numbers from digit cards', 'auto', 'List every 3-digit number from the cards 9, 0, 3', 'Included 039 and 093: a 3-digit number cannot start with 0.'),
 ('S10', 'Making numbers from digit cards', 'auto', 'How many 3-digit numbers can you make from 2, 5, 8?', 'Listed only some: no system, so a number was missed.'),
 ('P01', 'Draw it on paper', 'self', 'Draw 3 hundreds, 2 tens and 5 ones with base-ten blocks (do this on paper)', None),
 ('O01', 'Make your own riddle', 'none', 'Write 3 clues so that only 372 fits. Many answers are right.', None),
]
# marks: R right, W wrong, S skipped, P partial wrong ; self: G got it, N not yet, C checked, '-' no tick
KIDS = {  # nicknames are invented
 'Maple (sample)':  dict(marks='R R R R R R R R W W', self='G', open=True),
 'Otter (sample)':  dict(marks='R W W R W R W S W S', self='N', open=True),
 'Pebble (sample)': dict(marks='W R R W W R R R S S', self='C', open=False),
 'Willow (sample)': dict(marks='R R W R R R R R R W', self='G', open=True),
}
SUBMITTED = ['Maple (sample)', 'Otter (sample)', 'Pebble (sample)']       # Willow has not submitted yet
SKILLS = list(dict.fromkeys(i[1] for i in ITEMS if i[2] == 'auto'))

def marks(k):
    out = {}
    for it, m in zip([i for i in ITEMS if i[2] == 'auto'], KIDS[k]['marks'].split()):
        out[it[0]] = m
    out['P01'] = 'self'; out['O01'] = 'open' if KIDS[k]['open'] else 'skipped'
    return out

def skill_state(k, skill):
    ms = [marks(k)[i[0]] for i in ITEMS if i[1] == skill and i[2] == 'auto']
    answered = [m for m in ms if m in 'RW']
    if len(answered) < 2: return 'few'
    r = answered.count('R') / len(answered)
    return 'strong' if r >= 0.75 else 'some' if r >= 0.4 else 'support'

CSS = """:root{--bg:#fff;--ink:#1B2A49;--mut:#5b6678;--line:#d7dce5;--card:#f6f8fb;--teal:#0f7a73;--warm:#9a4a00;--warmbg:#fff3e6;--ok:#e6f4f1}
@media (prefers-color-scheme:dark){:root{--bg:#10151f;--ink:#eef1f6;--mut:#a9b3c4;--line:#2b3547;--card:#182030;--teal:#5fd0c4;--warm:#ffb870;--warmbg:#2a2012;--ok:#12302c}}
@media print{:root{--bg:#fff;--ink:#1B2A49;--mut:#5b6678;--line:#d7dce5;--card:#f6f8fb;--teal:#0f7a73;--warm:#9a4a00;--warmbg:#fff3e6;--ok:#e6f4f1}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.5 'Nunito Sans',Arial,sans-serif}
main{max-width:46rem;margin:0 auto;padding:16px}section.page{border-top:4px solid var(--teal);padding:1rem 0 2rem;break-after:page}
h1{font-size:1.5rem;margin:.2rem 0}h2{font-size:1.15rem;margin:1.3rem 0 .4rem}h3{font-size:1rem;margin:.9rem 0 .2rem}
.banner{background:var(--warmbg);color:var(--warm);border:1px solid var(--warm);border-radius:10px;padding:.5rem .8rem;font-size:.9rem;margin:.5rem 0}
.sub{color:var(--mut);font-size:.9rem}.card{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:.7rem 1rem;margin:.5rem 0}
.ok{background:var(--ok)}table{border-collapse:collapse;width:100%;font-size:.92rem}th,td{border:1px solid var(--line);padding:.35rem .5rem;text-align:left;vertical-align:top}th{background:var(--card)}
.tag{font-size:.8rem;color:var(--mut)}.mk{font-weight:700;white-space:nowrap}ul{margin:.3rem 0 .3rem 1.2rem;padding:0}
@media(max-width:560px){table{font-size:.85rem}}"""

LBL = {'R': ('✓', 'right'), 'W': ('✗', 'to look at again'), 'S': ('–', 'left for later'), 'self': ('✎', 'checked on paper'), 'open': ('◇', 'open question, not marked'), 'skipped': ('–', 'left for later')}
WORD = {'strong': ('●', 'going well'), 'some': ('◐', 'some right, some to look at'), 'support': ('○', 'worth practising together'), 'few': ('·', 'not enough answers yet to say')}

def parent_page(k):
    nick = k.split(' (')[0]; m = marks(k); name = E(nick)
    good = [s for s in SKILLS if skill_state(k, s) == 'strong']; next_ = [s for s in SKILLS if skill_state(k, s) in ('support', 'some')]
    left = [i for i in ITEMS if m[i[0]] in ('S', 'skipped') and i[2] == 'auto']
    wrong = [i for i in ITEMS if m[i[0]] == 'W' and i[4]]
    h = [f'<section class="page"><div class="banner">SAMPLE REPORT. Synthetic data, invented names. Not a real child.</div><h1>{name}’s practice: Digit detectives</h1>',
         '<p class="sub">Extension Workbook, Level 2, unit 1 · Numbers to 1000 · for a parent or guardian</p>',
         f'<p>Hello! {name} worked through this unit and sent the answers in. Here is a friendly picture of how it went. There are no scores or rankings here: every child learns at their own pace, and a mistake is simply a clue about what to look at next.</p>']
    h.append('<h2>What went well</h2>')
    h.append('<div class="card ok"><ul>' + ''.join(f'<li><b>{E(s)}</b>: {name} answered these confidently.</li>' for s in good) + '</ul></div>' if good else f'<div class="card ok"><p>{name} had a go at every kind of question, which is a good start. The next part shows where to look together.</p></div>')
    h.append('<h2>Worth looking at together</h2>')
    if next_:
        h.append('<div class="card"><ul>')
        for s in next_:
            clues = [i[4] for i in wrong if i[1] == s]
            h.append(f'<li><b>{E(s)}</b>' + (f'<ul>' + ''.join(f'<li>{E(c)}</li>' for c in clues[:2]) + '</ul>' if clues else '') + '</li>')
        h.append('</ul></div><p class="sub">A good way to help: ask your child to explain how they got one of these answers, and listen for the idea behind it. Please do not worry about the wrong answer itself.</p>')
    else: h.append(f'<div class="card"><p>Nothing in particular. Enjoy the next unit!</p></div>')
    if left:
        h.append('<h2>Left for later</h2><div class="card"><p>These questions were skipped. That is fine; skipping a question is a good choice when it feels too hard right now:</p><ul>' + ''.join(f'<li>{E(i[3])}</li>' for i in left) + '</ul></div>')
    h.append(f'<h2>Checked on paper</h2><div class="card"><p>One question was to do on paper and check against the picture on screen. {name} ' + {'G': 'ticked “I got it”.', 'N': 'ticked “not yet”, so it may be worth drawing it together.', 'C': 'ticked “I checked it”.'}[KIDS[k]['self']] + ' These are not counted as marked questions.</p></div>')
    h.append('<h2>A next step, if you would like one</h2><div class="card"><p>Based on this unit, a small group class could be a friendly next step for place value and comparing numbers. If you would like to try a free trial class, you can ask for one in your portal when you are ready. There is no deadline and no obligation. (This note only appears in your own report; we do not use your child’s answers to send you messages unless you have agreed to that.)</p></div>')
    h.append('<p class="sub">Questions or corrections about this report or your child’s data: please contact our data protection contact, listed on the Privacy page.</p></section>')
    return ''.join(h)

def tutor_child(k):
    m = marks(k); h = [f'<section class="page"><div class="banner">SAMPLE. Synthetic data. Tutor view of one child.</div><h1>{E(k)}: Digit detectives</h1><p class="sub">{STRAND} · received 24 Nov, 16:42 (server time) · revision 1</p>',
        '<table><tr><th>#</th><th>Skill</th><th>Question</th><th>Result</th><th>Likely misconception</th></tr>']
    for n, it in enumerate(ITEMS, 1):
        v = m[it[0]]; sym, word = LBL.get(v, LBL['R'])
        if it[2] == 'self': sym, word = '✎', {'G': 'checked on paper: got it', 'N': 'checked on paper: not yet', 'C': 'checked on paper'}[KIDS[k]['self']]
        note = it[4] if v == 'W' and it[4] else ''
        h.append(f'<tr><td>{n}</td><td>{E(it[1])}</td><td>{E(it[3])}</td><td class="mk">{sym} {word}</td><td>{E(note)}</td></tr>')
    h.append('</table><h2>By skill</h2><table><tr><th>Skill</th><th>Right</th><th>To look at</th><th>Skipped</th><th>Reading</th></tr>')
    for s in SKILLS:
        ms = [m[i[0]] for i in ITEMS if i[1] == s and i[2] == 'auto']; st = skill_state(k, s)
        h.append(f'<tr><td>{E(s)}</td><td>{ms.count("R")}</td><td>{ms.count("W")}</td><td>{ms.count("S")}</td><td>{WORD[st][0]} {WORD[st][1]}</td></tr>')
    h.append('</table><p class="sub">Percentages cover auto-marked questions only. Checked-on-paper and open questions are shown separately and are never in a percentage. “Skills” come from the MOE strand and skill tags on each item (tutor-facing labels).</p></section>')
    return ''.join(h)

def tutor_group():
    h = ['<section class="page"><div class="banner">SAMPLE. Synthetic data. Tutor view of a group (alphabetical, never sorted by result).</div><h1>Group L2A: Digit detectives</h1><p class="sub">4 children in the group · 3 have sent answers · 1 not yet</p>',
         '<table><tr><th>Child</th>' + ''.join(f'<th>{E(s)}</th>' for s in SKILLS) + '<th>Checked on paper</th></tr>']
    for k in sorted(KIDS):
        if k not in SUBMITTED: h.append(f'<tr><td>{E(k)}</td><td colspan="{len(SKILLS) + 1}" class="tag">has not sent answers yet</td></tr>'); continue
        h.append(f'<tr><td>{E(k)}</td>' + ''.join(f'<td>{WORD[skill_state(k, s)][0]} {WORD[skill_state(k, s)][1]}</td>' for s in SKILLS) + f'<td>{ {"G": "got it", "N": "not yet", "C": "checked"}[KIDS[k]["self"]] }</td></tr>')
    h.append('</table><p class="sub">● going well · ◐ some right, some to look at · ○ worth practising together · · not enough answers to say</p>')
    common = {}
    for k in SUBMITTED:
        for it in ITEMS:
            if marks(k)[it[0]] == 'W' and it[4]: common[it] = common.get(it, 0) + 1
    h.append('<h2>For planning the next lesson: the most common misconceptions</h2><table><tr><th>Question</th><th>Likely misconception</th><th>Children</th></tr>')
    for it, n in sorted(common.items(), key=lambda x: -x[1])[:4]:
        h.append(f'<tr><td>{E(it[3])}</td><td>{E(it[4])}</td><td>{n} of {len(SUBMITTED)}</td></tr>')
    h.append('</table><p class="sub">Children are listed alphabetically on purpose. This page is for the tutor only. It is not shown to families and is not a league table.</p></section>')
    return ''.join(h)

def owner_page():
    return ('<section class="page"><div class="banner">SAMPLE. Synthetic numbers.</div><h1>Owner view: practice and trial class funnel</h1><p class="sub">Counts only, from rows that already exist. No cookies, no tracking of visitors.</p>'
            '<table><tr><th>Step</th><th>Count</th></tr><tr><td>Extension books paid (online or both)</td><td>18</td></tr><tr><td>Children who started the online practice</td><td>14</td></tr>'
            '<tr><td>Trial class requests (from the book page / after a unit / the report / the website)</td><td>5 (2 / 1 / 2 / 0)</td></tr><tr><td>Trial class attended</td><td>3</td></tr><tr><td>Enrolled afterwards</td><td>1</td></tr></table>'
            '<h2>Children with no group (extension-only families)</h2><table><tr><th>Child</th><th>Unit</th><th>Sent</th><th>Group</th></tr><tr><td>Maple (sample)</td><td>Digit detectives</td><td>24 Nov</td><td>none</td></tr><tr><td>Pebble (sample)</td><td>Digit detectives</td><td>25 Nov</td><td>none</td></tr></table>'
            '<p class="sub">The owner sees these reports because there is no tutor group. Parents see only their own child’s summary.</p></section>')

def build():
    os.makedirs(OUT, exist_ok=True)
    body = parent_page('Otter (sample)') + parent_page('Maple (sample)') + tutor_child('Otter (sample)') + tutor_group() + owner_page()
    doc = f'<!doctype html><html lang="en-SG"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Mock reports</title><style>{CSS}</style></head><body><main><h1 style="margin-top:0">Mock reports (synthetic data)</h1><p class="sub">A. Parent summary (two children) · B. Tutor view of one child · C. Tutor view of a group · D. Owner funnel. Made by practice/submit/mock_report.py. Nothing here is real.</p>{body}</main></body></html>'
    p = os.path.join(OUT, 'mock_reports.html'); open(p, 'w', encoding='utf-8').write(doc)
    from playwright.sync_api import sync_playwright
    with sync_playwright() as pw:
        b = pw.chromium.launch(); pg = b.new_page(); pg.goto('file://' + p); pg.pdf(path=os.path.join(OUT, 'mock_reports.pdf'), format='A4', margin=dict(top='14mm', bottom='14mm', left='14mm', right='14mm'), print_background=True)
        pg.set_viewport_size({'width': 390, 'height': 900}); pg.screenshot(path=os.path.join(OUT, 'mock_parent_phone.png'), full_page=False); b.close()
    print('written', p)

if __name__ == '__main__': build()
