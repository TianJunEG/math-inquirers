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

QUEST V2 (owner decisions of 23 Oct 2026, night: X10-BEFORE, PRIVACY-REWORD; plan docs/pedagogy/lesson_x10_consolidation_plan.md section 1). The Quest is hosted by lesson x.10, a
choose-the-tool lesson. Everything below is OPT-IN through the lesson data, so a lesson whose block has no `tool_row` builds exactly as before:
  challenge_quest.tool_row   list of tool ids from levels/spine.json (pattern, list, draw, table, backwards, guess, simpler, actout) or the string "term" for the default row of
                             the tools met by that term (TERM_TOOLS). Turns on: a tool row under every gate ("Tool I used (circle one)", the eight card names, plus "No tool"),
                             an "I checked" tick, a Mi-says rule line, a "because" line in the secret cave, and in the tutor notes a Tool column, the four habits and the PRIVATE
                             three-word scale (with help / with a prompt / on their own), the tool-words pattern for the line to the grown-up and one sentence in the grown-up note.
  challenge_quest.questions[].lesson == "mixed"     an unlabelled mixed gate (no lesson tag). Works with or without tool_row. `strand` may be omitted or "mixed".
  challenge_quest.questions[].tools                 optional list of tool ids that fit the gate well (tutor notes only; two good tools are fine).
  challenge_quest.optional.because (true)           the secret cave is a choose-the-tool problem: tool row plus an "I chose it because ___" line.
The three-word scale is a word per habit per child, written in PRIVATE tutor notes only. It is never printed on a child or parent page (BAN_FAMILY bans "with a prompt"),
never counted or tabulated, never compared between children. The privacy checklist line that said "no tally ... not even in your own notes" is replaced at build time by
PRIVACY_TALLY_LINE for every lesson (see normalise_privacy), so a lesson file that still has the old line cannot print it.
"""
import glob, html, json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
L1 = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(L1, 'tools'))
import common                                   # noqa: E402
import b_check as bc                            # noqa: E402  (read only: question layout, pictures, CSS)
import pdfcheck                                 # noqa: E402
from common import E, mi_uri, font_css          # noqa: E402

NAME = "Mi's Challenge Quest"


_TERM = {'n': 0, 'off': 0}     # set per build: term-local lesson numbers (the books say "Term 3 Lesson 8")


def set_term(d):
    _TERM['n'] = d['term']; _TERM['off'] = (d['term'] - 1) * 10


def lesson_lab(x):
    """Lesson label for a gate: term-local, e.g. 'Term 3 Lesson 4', 'Term 3 Lessons 1, 2' (gate covers two lessons), 'mixed' or 'unseen' (the cave)."""
    if str(x) == 'mixed': return 'mixed'
    if str(x) == 'beyond': return 'unseen'
    t, off = _TERM['n'], _TERM['off']
    if isinstance(x, (list, tuple)): return f'Term {t} Lesson' + ('s ' if len(x) > 1 else ' ') + ', '.join(str(int(i) - off) for i in x)
    return f'Term {t} Lesson {int(x) - off}'


# words that must never appear in the text of the child or parent PDFs (the tutor notes may say "no scores" etc.)
BAN_FAMILY = [r'\btests?\b', r'\bexams?\b', r'check[- ]?sheet', r'\bend-of-term check\b', r'\btimer\b', r'\bpass(ed)? or fail', r'\branked?\b|\branking\b',
              r'\bscored?\b|\bscores\b', r'\bmarked\b|\bmarks\b|\bmarking\b', r'\bout of\b', r'\bgrades?\b']
BAN_TUTOR = [r'check[- ]?sheet', r'\bend-of-term check\b', r'\bR/P/N\b', r'\bmarking sheet\b', r'\brecord sheet\b']
BAN_FAMILY += [r'\bwith a prompt\b', r'independence scale']     # the three-word scale lives in the private tutor notes only

# ------------------------------------------------------------------ Quest v2: tools, scale, privacy wording
SPINE = os.path.normpath(os.path.join(L1, '..', '..', 'levels', 'spine.json'))
ICON_DIR = os.path.normpath(os.path.join(L1, '..', '..', 'levels', 'spine_icons'))
# tools met by the end of each term (plan section 1: only the tools met so far are shown; schedule from term review 2.2)
TERM_TOOLS = {1: ['draw', 'actout', 'pattern', 'list'],
              2: ['draw', 'actout', 'pattern', 'list', 'table', 'backwards'],
              3: ['draw', 'actout', 'pattern', 'list', 'table', 'backwards', 'guess'],
              4: ['pattern', 'list', 'draw', 'table', 'backwards', 'guess', 'simpler', 'actout']}
# the one line that replaces "no tally ... not even in your own notes" (owner decision PRIVACY-REWORD)
PRIVACY_TALLY_LINE = ('No score, no x out of {n}, no ranking, no comparison between children, and no tally or count of any kind on a child\'s page or anywhere a family can see. '
                      'In your own notes: words only. You may circle one of the three words (with help / with a prompt / on their own) for each habit in the private notes sheet (section 5); '
                      'never add the circles up, never compare children, and never say or show the words to a child or a grown-up.')
PARENT_TOOL_SENTENCE = ('Under each gate your child circles the tool they used and ticks I checked. The line we send may say which tool your child chose and how they checked, as something they did that day.')
SCALE_WORDS = ('with help', 'with a prompt', 'on their own')
HABITS = [('Chose a tool for a new problem', 'Which tool did they start with, and did they name it or point to it? Prompted if you had to ask "which tool?".'),
          ('Checked the answer', 'A second method, adding back, drawing it, reading it against the story. Prompted if you had to ask "can you check it another way?".'),
          ('Gave a reason in their own words', 'The "because" line or what they said. Look for the idea, not the grammar.'),
          ('Stayed with a stuck moment', 'Tried another tool, tried smaller numbers, asked, waited, or stopped. Note what they did.')]
# tool-words patterns for the one line to the grown-up (pick one that your notes show; always add your own detail)
TOOL_SAW = {'pattern': '[Name] chose to spot the pattern and said what repeats or grows.',
            'list': '[Name] chose to list every way and checked that none was missing.',
            'draw': '[Name] chose to draw it and checked the picture against the story.',
            'table': '[Name] chose to make a table and read the answer down a column.',
            'backwards': '[Name] chose to work backwards and checked by going forwards again.',
            'guess': '[Name] chose to guess and check and made a better guess each time.',
            'simpler': '[Name] chose to try smaller numbers first and then used the same idea for the real problem.',
            'actout': '[Name] chose to act it out with counters and checked by counting again.'}


def spine_tools():
    return {t['id']: t for t in json.load(open(SPINE, encoding='utf-8'))['tools']}


def tool_row_ids(c, term):
    """The tool ids of this block, in card order (spine numbers), or [] when the block is not Quest v2."""
    tr = c.get('tool_row')
    if not tr: return []
    ids = TERM_TOOLS[int(term)] if tr == 'term' else list(tr)
    sp = spine_tools()
    bad = [i for i in ids if i not in sp]
    assert not bad, f'challenge_quest.tool_row: unknown tool ids {bad} (levels/spine.json has {sorted(sp)})'
    return sorted(ids, key=lambda i: sp[i]['n'])


def icon_svg(tid, px=16):
    px = 13 if px == 'many' else px
    sv = open(os.path.join(ICON_DIR, tid + '.svg'), encoding='utf-8').read()
    sv = re.sub(r'\s(width|height)="64"', '', sv, count=2)
    return sv.replace('<svg ', f'<svg width="{px}" height="{px}" aria-hidden="true" focusable="false" ', 1)


def normalise_privacy(items):
    """Replace the old checklist line (no tally ... not even in your own notes) by PRIVACY_TALLY_LINE; returns (items, changed)."""
    out, changed = [], False
    for x in items:
        if re.search(r'no tally,|not even in your own notes', x, re.I) and 'no tally or count' not in x:
            m = re.search(r'x out of (\d+)', x)
            out.append(PRIVACY_TALLY_LINE.format(n=m.group(1) if m else '8')); changed = True
        else: out.append(x)
    return out, changed


# ------------------------------------------------------------------ child pages: Quest Log

TOOL_RULE = 'Under each gate, circle the tool you used. There is no wrong tool. Tick "I checked" when you have checked your answer.'
TOOL_CSS = ('.tstrip{margin:5px 0 0;padding-top:3px;border-top:1.5px dashed #C9D4EC;display:flex;flex-wrap:wrap;align-items:center;gap:2px 8px;font-size:12px;font-weight:700;color:#1B2A49;break-inside:avoid}'
            '.tstrip .tl{font-family:Fredoka,Arial,sans-serif;color:#1F7A6F;font-size:12px;margin-right:2px}'
            '.tstrip .tp{display:inline-flex;align-items:center;gap:4px;padding:0 2px;white-space:nowrap}.tstrip .tp svg{color:#1B2A49;flex:none}'
            '.tstrip.tmany{font-size:10.5px;gap:1px 4px;margin-top:3px;padding-top:2px}.tstrip.tmany .tl{font-size:10.5px}.tstrip.tmany .tp{gap:2px;padding:0 1px}.tstrip .ck{margin-left:4px;display:inline-flex;align-items:center;gap:5px;white-space:nowrap}'
            '.tstrip .cb{display:inline-block;width:14px;height:14px;border:2px solid #1B2A49;border-radius:3px;background:#fff}')


def tool_strip_html(ids, cave=False):
    """One compact row under a gate: the tool cards met so far (icon + card name) for the child to circle, then the "I checked" tick."""
    sp = spine_tools()
    pills = ''.join(f'<span class="tp">{icon_svg(i, 13 if len(ids) > 5 else 16)}{E(sp[i]["name"])}</span>' for i in ids) + '<span class="tp">No tool</span>'
    tick = '' if cave else '<span class="ck"><i class="cb"></i>I checked</span>'
    return f'<div class="tstrip{" tmany" if len(ids) > 5 else ""}"><span class="tl">{"My tool" if cave else "Tool I used"}</span>{pills}{tick}</div>'


def quest_log_html(d):
    set_term(d)
    q = d['challenge_quest']
    t = d['term']
    shim = dict(d); shim['end_of_term_check'] = q            # b_check reads this key; the data lives under challenge_quest
    tools = tool_row_ids(q, t)                                # Quest v2: a tool row under every gate (empty list: built as before)
    if tools:
        shim['end_of_term_check'] = q = dict(q, child_rules=list(q['child_rules']) + [q.get('tool_rule') or TOOL_RULE])
        strip = tool_strip_html(tools)
        orig = bc.qbox2
        bc.qbox2 = lambda *a, **k: (lambda b: b[:-len('</div>')] + strip + '</div>')(orig(*a, **k))
    try:
        h = bc.sheet_html(shim)
    finally:
        if tools: bc.qbox2 = orig
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
    if tools:
        cave_end = '<div class="foot">You may skip this one. Mi will swim round it.</div></div>'
        assert cave_end in h, 'quest log: secret cave block not found'
        because = ('<div class="sub2"><span class="sl">because</span><span>I chose it because <span class="wl2" style="width:62%"></span></span></div>' if q['optional'].get('because') else '')
        h = h.replace(cave_end, tool_strip_html(tools, cave=True) + because + cave_end, 1)
    h = h.replace('</head>', '<style>.csheet .qbox .qn:before,.csheet .qn:before{content:"Gate "}' + (TOOL_CSS if tools else '') + '</style></head>', 1)
    marker = '</ul></div>'
    assert marker in h
    if q.get('quest_map', True):                      # a lesson whose page 1 is full sets quest_map to false
        h = h.replace(marker, marker + qmap, 1)
    return h


# ------------------------------------------------------------------ tutor notes

def tutor_notes_html(d):
    set_term(d)
    c = d['challenge_quest']
    qs = c['questions']
    o = c['optional']
    smap = {s['id']: s for s in c['strands']}
    smap.setdefault('mixed', {'moe_label': 'mixed (tool choice, no single area)'})
    tools = tool_row_ids(c, d['term'])
    sp = spine_tools() if tools else {}
    tname = lambda ids: ', '.join(sp[i]['name'] for i in ids)
    H = []
    H.append(f'<div class="cover"><img alt="Mi the dolphin" src="{mi_uri()}" style="position:absolute;right:18px;top:12px;width:90px">'
             f'<div class="k">TUTOR NOTES • LEVEL {d["level"]} • TERM {d["term"]} • {NAME.upper()}</div><h1>{E(c["title"])}</h1>'
             f'<p>{len(qs)} gates, one from each lesson of the {'year' if c.get('scope') == 'year' else 'term'}, all at Start here level, plus one optional secret cave item. {c["minutes"]} minutes after the break, played in pairs or as a group quest with Mi, working on private paper. '
             f'It is a game: no score or mark is shown to the child, no ranking, no visible timer. You keep private notes only. For the tutor: do not hand these notes to families.'
             + (f' Under every gate the child circles the tool they used ({tname(tools)}, or No tool) and ticks I checked: a choose-the-tool habit, not a mark.' if tools else '') + '</p></div>')
    H.append(f'<div class="box t"><b>Where it sits.</b> {E(c["where"])}. <span class="small">{E(c["plan_note"])}</span></div>')
    H.append('<h2>1. The gates at a glance</h2><table><tr><th>Gate</th><th>From</th><th>Area (tutor label)</th><th>What it uses (Start here level)</th><th>Answer</th></tr>')
    for q in qs:
        H.append(f'<tr><td><b>{q["id"][1:]}</b></td><td>{lesson_lab(q["lesson"])}</td><td>{E(smap.get(q.get("strand", "mixed"), smap["mixed"])["moe_label"])}</td><td>{E(q["skill"])}</td><td class="ans">{E(q["answer"])}</td></tr>')
    H.append(f'<tr><td><b>Secret cave</b></td><td>{lesson_lab(o["lesson"])}</td><td>{E(smap.get(o["strand"], {'moe_label': 'unseen puzzle'})["moe_label"])}</td><td>{E(o["skill"])} (optional)</td><td class="ans">{E(o["answer"])}</td></tr></table>')
    H.append('<p class="small">The area labels are for the tutor only and never appear on a child or parent page. Each gate is a fresh example of the Start here idea of its lesson (numbers chosen so that they do not repeat a lesson page), so a child who followed the lesson can open it. '
             'Before first use, read each gate against what the lesson actually taught.</p>')
    H.append('<h2>2. Playing it: before and during</h2><ol>' + ''.join(f'<li>{E(x)}</li>' for x in c['give']) + '</ol>')
    if tools:
        H.append('<div class="box t"><b>The tool row and the I checked tick (on every gate).</b><ul>'
                 f'<li>The row shows only the tools this class has met: {E(tname(tools))}, and No tool. The child circles one. There is no right tool: two gates can be solved well in more than one way, and a child who circles In my head is telling you the truth.</li>'
                 '<li>Do not say or hint a tool while the quest is on. No gate question names a tool (the names fade at Start here and Think harder; the quest is where the child chooses).</li>'
                 '<li>The circle and the tick are never marked, added up or compared. They tell you what to ask in the lesson look-back and what to write in your notes, in words.</li>'
                 '<li>A gate with no circle is fine: write nothing about it.</li></ul></div>')
    H.append('<h2>3. After the lesson: photos and your private notes</h2><ol>' + ''.join(f'<li>{E(x)}</li>' for x in c['after']) + '</ol>')
    priv, _chg = normalise_privacy(c['privacy_checklist'])
    H.append('<div class="box r"><b>Privacy checklist</b><ul>' + ''.join(f'<li>{E(x)}</li>' for x in priv) + '</ul></div>')
    H.append('<h3>Absent, late joiners, families who prefer not to, upset children</h3><ul>' + ''.join(f'<li>{E(x)}</li>' for x in c['late']) + '</ul>')
    H.append('<h2 class="pb">4. Answers and what to look for</h2><p class="small">Use these to understand what you see on camera and in the photos. Nothing is written on the child\'s paper, nothing is totalled and no gate is marked right or wrong in front of anyone. '
             'A child may write steps in any clear layout. Spelling and neatness do not matter.</p>')
    for q in qs + [dict(o, id='Optional', text=o['text'].replace('Think harder (optional). ', ''))]:
        lab = 'Secret cave (optional)' if q['id'] == 'Optional' else 'Gate ' + q['id'][1:]
        parts = '; '.join(f'({p["l"]}) {bc.keyclean(bc.minus(p["text"].replace("___", "__")))} = {p["ans"]}' if p['l'] else f'{bc.keyclean(bc.minus(p["text"].replace("___", "__")))} = {p["ans"]}' for p in q['parts'])
        right = q.get('right', 'The answer is as above.'); partly = q.get('partly', '-')
        H.append(f'<div class="box k1"><b>{lab}</b> ({lesson_lab(q["lesson"])}) {E(bc.keyclean(bc.minus(q["text"])))}<div class="ans">Answer: {E(bc.minus(q["answer"]))}</div><div class="small">{E(parts)}</div>'
                 f'<div class="small"><b>A secure answer looks like:</b> {E(right)} <b>Half way there:</b> {E(partly)}</div><div class="small"><b>Worked:</b> {E(bc.minus(q["solution"]))}</div>'
                 f'<div class="small"><b>Watch for:</b> {E("; ".join(q["mistakes"]))}</div>'
                 + (f'<div class="small"><b>Tools that fit well (tutor only):</b> {E(tname(q["tools"]))}. Any tool that gets a secure answer is a good choice.</div>' if tools and q.get('tools') else '')
                 + (f'<div class="small"><b>Because line:</b> the child writes why they chose the tool. A reason in any words is a good one, for example "I could see it in the picture".</div>' if q['id'] == 'Optional' and q.get('because') else '') + '</div>')
    if c.get('measure_note'):
        H.append(f'<div class="note">{E(c["measure_note"])}</div>')
    # --- the private notes sheet
    ns = c['notes_sheet']
    line = '<span style="display:inline-block;width:%s;border-bottom:1.5px dotted #8A94AD">&nbsp;</span>'
    H.append('<h2 class="pb">5. Tutor private notes (tutor only; one sheet per child; delete when the line is sent)</h2>')
    H.append(f'<p>Child (first name only): {line % "230px"} &nbsp; Date: {line % "110px"} &nbsp; Quest partner: {line % "150px"}</p>')
    H.append('<p class="small">' + E(ns['how']) + '</p>')
    tc_h = '<th style="width:96px">Tool circled (a word)</th>' if tools else ''
    tc_c = '<td></td>' if tools else ''
    H.append(f'<table class="rec"><tr><th style="width:56px">Gate</th><th style="width:40px">From</th>{tc_h}<th>What I saw (words used, counters or drawing, how the partner helped, anything the child said)</th></tr>' + ''.join(
        f'<tr><td><b>{q["id"][1:]}</b></td><td>{lesson_lab(q["lesson"])}</td>{tc_c}<td style="height:34px"></td></tr>' for q in qs) + f'<tr><td><b>Cave</b></td><td>{lesson_lab(o["lesson"])}</td>{tc_c}<td style="height:34px"></td></tr></table>')
    if tools:
        w = ''.join(f'<th style="width:16%;text-align:center">{E(x)}</th>' for x in SCALE_WORDS)
        H.append('<div class="box r"><b>Habits and the private three-word scale (tutor only)</b>'
                 '<p class="small" style="margin:3px 0">For each habit, circle ONE word from the whole lesson and the quest, or leave the row empty if you did not see it (never guess). Words, not numbers: '
                 'never count the circles, never add them up, never compare children, never say or show the words to a child or a grown-up, and never put them in the line for the grown-up. '
                 'This strip stays on this child\'s sheet and is deleted with it when the line is sent.</p>'
                 f'<table><tr><th>Habit</th><th>What to look for</th>{w}</tr>' + ''.join(
                     f'<tr><td><b>{E(h)}</b></td><td class="small">{E(w_)}</td>' + ''.join('<td style="text-align:center;height:30px">&nbsp;</td>' for _ in SCALE_WORDS) + '</tr>' for h, w_ in HABITS) + '</table></div>')
    H.append('<table><tr><th>Prompt</th><th>My notes</th></tr>' + ''.join(f'<tr><td style="width:36%">{E(p)}</td><td style="height:44px"></td></tr>' for p in ns['prompts']) + '</table>')
    H.append(f'<p>The one line for the grown-up (section 7), written from these notes:</p><div class="wl">&nbsp;</div><div class="wl">&nbsp;</div>')
    H.append('<h2 class="pb">6. Group advice for next term (tutor only; one sheet per class; no names)</h2>')
    H.append('<p class="small">' + E(ns['group_how']) + '</p>')
    H.append('<table><tr><th style="width:26%">Area</th><th>What several children were still working on (no names)</th><th>What I will do in the first two lessons of next term</th></tr>' + ''.join(
        f'<tr><td><b>{E(s["parent_name"])}</b><div class="small">{"Lesson " + str(s["lessons"][0]) if s["lessons"][0] == s["lessons"][-1] else "Lessons " + str(s["lessons"][0]) + " to " + str(s["lessons"][-1])}: {E(s["looked_at"])}</div></td><td style="height:78px"></td><td></td></tr>' for s in c['strands']) + '</table>')
    H.append('<table><tr><th>Prompt</th><th>My notes</th></tr>' + ''.join(f'<tr><td style="width:36%">{E(p)}</td><td style="height:44px"></td></tr>' for p in ns['group_prompts']) + '</table>')
    # --- the one-line templates
    sl = c['saw_line']
    H.append('<h2 class="pb">7. The one line for the grown-up: what we saw</h2>')
    H.append(f'<div class="box t"><b>{E(sl["heading"])}</b><br>{E(sl["pattern"])}</div>')
    H.append('<p class="small">' + E(sl['how']) + '</p>')
    H.append('<table><tr><th>Area (parent wording)</th><th>Things you might have seen (pick the one your notes show; add the detail)</th><th>A next step that helps at home</th></tr>' + ''.join(
        f'<tr><td><b>{E(s["parent_name"])}</b><div class="small">{"Lessons" if len(s["lessons"]) > 1 else "Lesson"} {s["lessons"][0]}' + (f' to {s["lessons"][-1]}' if len(s["lessons"]) > 1 else '') + f'. We looked at {E(s["looked_at"])}.</div></td>'
        f'<td><ul>{"".join("<li>" + E(x) + "</li>" for x in s["saw_examples"])}</ul></td><td><ul>{"".join("<li>" + E(x) + "</li>" for x in s["next_examples"])}</ul></td></tr>' for s in c['strands']) + '</table>')
    if tools:
        H.append('<h3>Tool words for the line (use when your notes show it)</h3><ul>' + ''.join(f'<li>{E(TOOL_SAW[i])}</li>' for i in tools) + '</ul>'
                 '<p class="small">Say which tool the child chose and how they checked, as something they did that day. Write it in your own words and add one detail from your notes.</p>')
    H.append('<h3>A filled example (fictional child, Mei)</h3><div class="note">' + f'<b>{E(NAME)}: Mei</b><br>{E(sl["example"])}<br><br>{E(sl["closing"].replace("[Name]", "Mei"))}</div>')
    H.append('<p class="small">Words to avoid in the line: score, mark, out of, rank, top, below average, behind, ahead of, pass, fail, predicted, ready for' + (', independent, on their own, with help, with a prompt (the three-word scale is for your private notes only)' if tools else '') + '. No claim about school exams, GEP or any contest, and no mention of other children. The line goes to the parent only. '
             'If the child skipped the secret cave or a gate, say nothing about it. If the child tried the secret cave, you may add: "[Name] also had a go at the secret cave."</p>')
    return f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{html.escape(NAME)}: tutor notes</title><style>{font_css()}{bc.KEY_CSS}ul{{margin:0 0 0 14px}}body{{font-size:11.6px;line-height:1.35}}h2{{margin:12px 0 5px}}</style></head><body>{"".join(H)}</body></html>'


# ------------------------------------------------------------------ the grown-up note

def parent_note_html(d):
    set_term(d)
    c = d['challenge_quest']
    n = c['parent_note']
    sl = c['saw_line']
    li = lambda xs: ''.join(f'<li>{E(x)}</li>' for x in xs)
    body = (f'<div class="hd"><img alt="Mi the dolphin" src="{mi_uri()}" style="width:20mm;height:auto"><div><div class="tp">Level {d["level"]} • Term {d["term"]} • For grown-ups</div><h1>{E(n["title"])}</h1></div></div>'
            f'<p style="margin:0 0 4px">{E(n["what"])}</p>'
            f'<h2>Before the lesson</h2><ul>{li(n["before"])}</ul>'
            f'<h2>During the quest</h2><ul>{li(n["during"])}</ul>'
            f'<h2>After the lesson: sending the Quest Log privately</h2><ul>{li(n["after"])}</ul>'
            f'<div class="panel"><b>What you get back.</b> {E(n["back"])}' + (f' {E(PARENT_TOOL_SENTENCE)}' if tool_row_ids(c, d['term']) else '') + f'<br><i>{E(sl["parent_example"])}</i></div>'
            f'<p>{E(n["make_up"])}</p>'
            f'<p class="small">Your child\'s paper, photos and note are treated as private: we never show them to other children or families, and we never compare children. Math Inquirers by Preciouslyours Pte Ltd.</p>')
    return f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{html.escape(NAME)}: grown-up note</title><style>{font_css()}{bc.NOTE_CSS}</style></head><body>{body}</body></html>'


# ------------------------------------------------------------------ build and check

def pdf_text(path):
    return subprocess.run(['pdftotext', '-layout', path, '-'], capture_output=True, text=True).stdout


def build_quest(d, pw, out_root=None):
    c = d['challenge_quest']
    n = d['_num']
    if normalise_privacy(c.get('privacy_checklist', []))[1]:
        print(f'NOTE  lesson {n}: challenge_quest.privacy_checklist still has the old "no tally ... not even in your own notes" line; the tutor notes use PRIVACY_TALLY_LINE instead (reword the lesson file)')
    od = os.path.join(out_root or os.path.join(L1, 'out'), f'l{n}')
    os.makedirs(od, exist_ok=True)
    term = f'Math Inquirers Term {d["term"]}'
    log = bc.render(pw, quest_log_html(d), 'quest_log', od, f'L{n}_Quest_Log.pdf', f"{term} {NAME}.", {'top': '12mm', 'bottom': '15mm', 'left': '14mm', 'right': '14mm'})
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
    tools = tool_row_ids(c, d['term'])
    if tools:                                                      # Quest v2: the tool row is really printed, and the scale only in the tutor notes
        tx_log = re.sub(r'\s+', ' ', pdf_text(log)); sp = spine_tools()
        for i in tools:
            if sp[i]['name'] not in tx_log: fails.append(f'quest log: tool card name {sp[i]["name"]!r} not printed')
        if tx_log.count('I checked') < len(c['questions']): fails.append('quest log: the I checked tick is missing on some gate')
        tx_n = re.sub(r'\s+', ' ', pdf_text(notes))
        for w in SCALE_WORDS:
            if w not in tx_n: fails.append(f'tutor notes: three-word scale word {w!r} missing')
        if not re.search(r'no tally or count of any kind', tx_n): fails.append('tutor notes: reworded privacy line missing')
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
