#!/usr/bin/env python3
"""Validate one lesson file.  Usage: python3 term/l1/tools/validate.py 01   (exit code 1 on any FAIL)

Checks: schema keys, timing (parts sum to exactly 90, script fits each part, slow-class scenario), slides <-> script links,
question completeness, tier rules, banned wording, REC cue length, link check, no copied contest text (7-word shingles
against docs/sasmo and docs/books), per-lesson answer verification (term/l1/verify/lNN_checks.py), practice-variant
verification (python oracle vs expression vs the runner's own JavaScript calc).
"""
import importlib.util, itertools, json, os, re, subprocess, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *  # noqa

FAILS, WARNS, PASSES = [], [], []


def ok(msg): PASSES.append(msg)
def fail(msg): FAILS.append(msg)
def warn(msg): WARNS.append(msg)


REQ_TOP = ['schema_version', 'id', 'level', 'term', 'lesson', 'title', 'big_idea', 'child_idea', 'moe', 'objectives', 'joining_cold',
           'materials', 'timing', 'sneak_peek', 'rec', 'script', 'slides', 'tiers', 'talk', 'exit', 'look_back', 'home_practice',
           'online_practice', 'parent', 'safeguarding', 'tutor_prep', 'spare_time']
Q_KEYS = ['id', 'tier', 'text', 'answer', 'val', 'hint', 'solution', 'mistakes', 'mins']
LINE_KINDS = {'SAY', 'READ', 'ASK', 'DO', 'SLIDE', 'WORK', 'HOLD', 'MOVE', 'REC', 'STUCK', 'NOTE'}
BLOCKS = {'chip', 'p', 'list', 'card', 'visual', 'qs', 'answers', 'say', 'cols', 'table', 'numrow', 'answer', 'lookback'}
BANNED_CHILD = [r'early finisher', r'gifted', r'genius', r'strong thinker', r'fast[- ]track', r'MOE[- ]aligned', r'\baligned\b', r'\bGEP\b',
                r'SASMO', r'olympiad', r'exam prep', r'\bchallenge\b', r'\bstretch\b', r'\bcore\b', r'high[- ]ability', r'ahead of', r'\branked?\b', r'top of the class']
MAX_REC_WORDS = 26


def child_strings(d):
    """Text that a child or parent sees (not the tutor-only notes)."""
    out = []
    for s in d['slides']:
        out.append(s['title']); out.append(s.get('subtitle', ''))
        def walk(b):
            for k, v in b.items():
                if k in ('t', 'type', 'style', 'size'):
                    continue
                if isinstance(v, str): out.append(v)
                elif isinstance(v, list):
                    for x in v:
                        if isinstance(x, str): out.append(x)
                        elif isinstance(x, dict): walk(x)
                        elif isinstance(x, list):
                            for y in x:
                                if isinstance(y, str): out.append(str(y))
                                elif isinstance(y, dict): walk(y)
        for b in s['blocks']:
            walk(b)
    for q in all_questions(d) + d['exit']:
        out.append(q.get('text', '')); out.append(q.get('first', ''))
        for p in q.get('parts', []): out.append(p['text'])
    for h in d['home_practice']: out.append(h['text'])
    for it in d['online_practice']['items']:
        out.append(it['q']); out.append(it.get('hint', '')); out += it.get('steps', [])
    pr = d['parent']
    for k in ('summary', 'when_stuck', 'next', 'report_line', 'term_line'): out.append(pr[k])
    for k in ('words', 'try_home', 'ask'): out += pr[k]
    out += list(d['look_back']['hardest']) + list(d['look_back']['helped']) + list(d['look_back']['next'])
    out.append(d['child_idea'])
    return [s for s in out if s]


# ------------------------------------------------------------------ checks

def check_schema(d):
    miss = [k for k in REQ_TOP if k not in d]
    if miss: fail('schema: missing top-level keys ' + ', '.join(miss)); return
    ok('schema: all top-level keys present')
    try:
        import jsonschema
        sc = json.load(open(os.path.join(L1, 'schema', 'lesson.schema.json')))
        errs = list(jsonschema.Draft202012Validator(sc).iter_errors({k: v for k, v in d.items() if not k.startswith('_')}))
        for e in errs[:6]: fail('json-schema: ' + '/'.join(map(str, e.absolute_path)) + ': ' + e.message[:120])
        if not errs: ok('schema: passes term/l1/schema/lesson.schema.json (JSON Schema 2020-12)')
    except ImportError:
        warn('schema: python jsonschema not installed; only key checks run')
    for tier in ('start', 'think', 'go'):
        for q in d['tiers'][tier]:
            m = [k for k in Q_KEYS if k not in q]
            if m: fail(f"question {q.get('id')}: missing {m}")
    inv = d['tiers']['investigation']
    for k in ('id', 'title', 'first', 'text', 'answer', 'look_for', 'mistakes'):
        if k not in inv: fail('investigation: missing ' + k)
    for q in d['exit']:
        for k in ('id', 'text', 'answer', 'val', 'solution', 'mistakes'):
            if k not in q: fail(f"exit {q.get('id')}: missing {k}")
    for s in d['slides']:
        for k in ('id', 'part', 'kind', 'title', 'blocks', 'note'):
            if k not in s: fail(f"slide {s.get('id')}: missing {k}")
        for b in s['blocks']:
            if b['t'] not in BLOCKS: fail(f"slide {s['id']}: unknown block {b['t']}")
        if len(s['note'].split()) < 12: fail(f"slide {s['id']}: speaker note too short")
    for seg in d['script']['segments']:
        for ln in seg['lines']:
            if ln['k'] not in LINE_KINDS: fail(f"script {seg['part']}: unknown line kind {ln['k']}")
    if not FAILS: ok('schema: questions, slides, script lines well formed')


def check_timing(d):
    parts = d['timing']['parts']
    if parts[0]['start'] != 0: fail('timing: first part must start at 0')
    for a, b in zip(parts, parts[1:]):
        if a['end'] != b['start']: fail(f"timing: gap or overlap between {a['id']} and {b['id']}")
    total = sum(p['end'] - p['start'] for p in parts)
    if parts[-1]['end'] != 90 or total != 90: fail(f'timing: parts must sum to exactly 90 minutes (got {total}, last end {parts[-1]["end"]})')
    else: ok(f'timing: {len(parts)} parts, contiguous, sum = {total} minutes exactly')
    if parts[-1]['id'] != 'flex' or parts[-1]['end'] - parts[-1]['start'] < 4: fail('timing: last part must be a flex/buffer part of at least 4 minutes')
    segs = segment_timeline(d)
    ids = {s['part'] for s in segs}
    for p in parts:
        if p['id'] not in ids: fail(f"timing: no script segment for part {p['id']}")
        if p['id'] not in d['rec']: fail(f"rec: no recording cue for part {p['id']}")
    used = slow = 0.0
    rows = []
    for s in segs:
        u, a, sl = s['used'], s['alloc'], slow_used(s)
        used += u; slow += sl
        flag = 'ok'
        if u > a: flag = 'OVER'; fail(f"timing: {s['part']} script needs {mmss(u)} but only {mmss(a)} is allocated")
        elif sl > a and s['part'] != 'flex': flag = 'OVER (slow class)'; warn(f"timing: {s['part']} OVER in the slow-class scenario ({mmss(sl)} needed, {mmss(a)} allocated): the buffer absorbs it, keep it under the flex minutes")
        elif s['part'] != 'flex' and u < 0.70 * a: flag = 'LOOSE'; warn(f"timing: {s['part']} uses only {mmss(u)} of {mmss(a)}")
        elif u > 0.97 * a: flag = 'TIGHT'; warn(f"timing: {s['part']} is tight ({mmss(u)} of {mmss(a)})")
        rows.append((s['part'], a, u, sl, flag))
    d['_timing_rows'] = rows
    d['_timing_total'] = (used, slow)
    if used > 86 * 60: fail(f'timing: scripted need {mmss(used)} leaves under 4 minutes of buffer')
    else: ok(f'timing: scripted need {mmss(used)} of 90:00 (buffer {mmss(90 * 60 - used)})')
    if slow > 90 * 60: fail(f'timing: slow-class scenario needs {mmss(slow)} (more than 90:00)')
    else: ok(f'timing: slow-class scenario (speech x1.10, children and slide changes x1.20) needs {mmss(slow)}')
    # SAY lines must be short enough to listen to
    for s in segs:
        for (_, sec, ln) in s['lines']:
            if ln['k'] == 'SAY' and words(ln['text']) > 70: warn(f"script {s['part']}: SAY line over 70 words, split it: {ln['text'][:50]}")
    # tutor talk share
    tut = sum(sec for s in segs for (_, sec, ln) in s['lines'] if ln['k'] in ('SAY', 'READ', 'REC') or (ln['k'] == 'ASK'))
    d['_tutor_share'] = tut / used if used else 0


def check_slides_links(d):
    sm = slide_map(d); seen = {}
    if len(sm) != len(d['slides']): fail('slides: duplicate slide ids')
    pm = part_map(d)
    for seg in d['script']['segments']:
        for ln in seg['lines']:
            if ln['k'] == 'SLIDE':
                sid = ln['slide']
                if sid not in sm: fail(f'link: script refers to missing slide {sid}'); continue
                if sm[sid]['part'] != seg['part']: fail(f"link: slide {sid} belongs to part {sm[sid]['part']} but is shown in {seg['part']}")
                seen[sid] = seen.get(sid, 0) + 1
    for sid, s in sm.items():
        n = seen.get(sid, 0)
        if n != 1: fail(f'link: slide {sid} appears {n} times in the script (must be exactly once)')
        if s['part'] not in pm: fail(f'link: slide {sid} part {s["part"]} unknown')
    if d['timing'].get('optional_slide') not in sm or not sm.get(d['timing'].get('optional_slide'), {}).get('optional'):
        fail('link: timing.optional_slide must be a slide marked optional')
    qm = qmap(d)
    refd = set()
    for s in d['slides']:
        def walk(blocks):
            for b in blocks:
                if b['t'] in ('qs', 'answers'):
                    for i in b['ids']:
                        refd.add(i)
                        if i not in qm: fail(f"link: slide {s['id']} refers to missing question {i}")
                if b['t'] == 'cols':
                    for c in b['cols']: walk(c)
        walk(s['blocks'])
    for q in d['tiers']['start'] + d['exit']:
        if q['id'] not in refd: fail(f"link: question {q['id']} is never shown on a slide")
    if not [f for f in FAILS if f.startswith('link')]: ok(f'link: {len(sm)} slides each shown exactly once, all question ids resolve')
    # page references in script/notes must match
    pages = {q['page'] for t in ('start', 'think', 'go') for q in d['tiers'][t]} | {d['tiers']['investigation']['page']}
    txt = ' '.join(ln.get('text', '') for seg in d['script']['segments'] for ln in seg['lines']) + ' ' + ' '.join(s['note'] for s in d['slides'])
    for m in re.finditer(r'page (\d)', txt, re.I):
        if int(m.group(1)) not in pages | {6}: fail(f'link: text mentions page {m.group(1)} which does not exist (pages {sorted(pages)} and kit page 6)')


def check_tiers(d):
    t = d['tiers']
    if not 5 <= len(t['start']) <= 8: fail(f"tiers: Start here has {len(t['start'])} questions (5 to 8)")
    if not 3 <= len(t['think']) <= 5: fail(f"tiers: Think harder has {len(t['think'])} questions (3 to 5)")
    if len(t['go']) != 3: fail('tiers: Go further must have exactly 3 questions')
    if len(d['exit']) != 3: fail('exit ticket must have exactly 3 questions')
    if len(d['home_practice']) != 5: fail('home practice must have exactly 5 questions')
    for tier in ('start', 'think', 'go'):
        for q in t[tier]:
            if q['tier'] != tier: fail(f"tiers: {q['id']} is in {tier} but says {q['tier']}")
            if not q['mistakes']: fail(f"tiers: {q['id']} has no common mistakes")
            if len(q['hint']) < 15 or len(q['solution']) < 25: fail(f"tiers: {q['id']} hint or worked solution too short")
    if sum(q['mins'] for q in t['start']) > 20: fail('tiers: Start here needs more than 20 minutes for a middle child')
    if len([x for x in d['home_practice'] if x['tier'] == 'start']) < 3: fail('home: at least 3 Start-here items')
    inv = t['investigation']
    if 'first' not in inv or len(inv['first']) < 10: fail('investigation: needs an easy first step')
    wb = [q['page'] for q in t['start']]
    if 1 not in wb or 2 not in wb: fail('tiers: Start here must fill workbook pages 1 and 2')
    # Start here must never be contest-style: see AUTHORING.md; flagged by field
    for q in t['start']:
        if q.get('contest'): fail(f"tiers: {q['id']} is contest-style and must be Think harder")
    ok('tiers: counts, completeness (answer, hint, worked solution, mistakes), exit 3, home 5')
    # online practice tiers
    items = d['online_practice']['items']
    for tier in ('core', 'stretch', 'challenge'):
        if len([i for i in items if i['tier'] == tier]) < 3: fail(f'online practice: fewer than 3 {tier} items')
    for i in items:
        if i['tier'] in ('stretch', 'challenge') and 'easier' not in i and i['type'] != 'selfcheck': fail(f"online practice: {i['id']} needs an 'easier' link")
        if 'easier' in i and i['easier'] not in {j['id'] for j in items}: fail(f"online practice: {i['id']} easier link broken")


def check_workbook_items(d):
    """Answer slots, printed choices and drawing size for every printed question."""
    import b_print
    qs = d['tiers']['start'] + d['tiers']['think'] + d['tiers']['go'] + d['exit']
    for q in qs:
        cw = b_print.choice_words(q['text'], q.get('choices')) or any(b_print.choice_words(p['text'], p.get('choices')) for p in q.get('parts', []))
        vis = q.get('visual') or {}
        on_picture = bool(vis.get('hide'))      # empty boxes drawn in the picture are the answer slots
        if not (q.get('parts') or q.get('lines', 0) > 0 or q.get('draw') or cw or on_picture):
            fail(f"workbook: {q['id']} has no answer slot (add parts with ___ or [], lines, draw, or choices)")
        if re.search(r'circle (the )?(correct|right) (answer|word|one)\b', q['text'], re.I) and not q.get('choices'):
            fail(f"workbook: {q['id']} says Circle but no choices are printed (add choices:[..])")
        if re.search(r'\bcircle\b[^.]*\b(yes|no|true|false|right|wrong)\b', q['text'] + ' '.join(p['text'] for p in q.get('parts', [])), re.I) and not cw and not any(' / ' in p['text'] for p in q.get('parts', [])) and ' / ' not in q['text']:
            fail(f"workbook: {q['id']} asks to circle a word but no choice words are printed")
        if q.get('draw'):
            t = q['text'] + ' ' + ' '.join(p['text'] for p in q.get('parts', []))
            est = q.get('draw_strokes')
            if est is None:
                est = 0
                for m in re.finditer(r'(\d+)\s+(bundles?|boxes|tens)\b', t): est += int(m.group(1)) * 10
                rest = re.sub(r'(\d+)\s+(bundles?|boxes|tens)\b', ' ', t)
                est += sum(int(n) for n in re.findall(r'\b(\d+)\b', rest) if int(n) < 100)
            if est > 25: warn(f"workbook: {q['id']} asks the child to draw about {est} strokes (over 25 is heavy for ages 6-8): draw a bundle as one bar, or lower the numbers (or set draw_strokes)")
    if not [f for f in FAILS if f.startswith('workbook:')]: ok('workbook: every question has an answer slot and printed choices')


def check_words(d):
    bad = []
    for s in child_strings(d):
        for pat in BANNED_CHILD:
            if re.search(pat, s, re.I): bad.append((pat, s[:70]))
        for m in re.finditer(r'private (chat|message)', s, re.I):
            if not re.search(r'\b(no|never|not)\b[^.]*private (chat|message)', s, re.I): bad.append(('private chat', s[:70]))
    if bad: fail('wording: banned or risky child-facing phrases: ' + '; '.join(f'{p!r} in "{t}"' for p, t in bad[:8]))
    else: ok('wording: no banned labels or claims in child and parent text')
    # tutor-facing notes: no public naming, no boards, no private chat instructions
    notes = ' '.join(ln.get('text', '') for seg in d['script']['segments'] for ln in seg['lines']) + ' ' + ' '.join(s['note'] for s in d['slides'])
    for m in re.finditer(r'private (chat|message)', notes, re.I):
        ctx = notes[max(0, m.start() - 80):m.end() + 20]
        if not re.search(r'\b(no|never|not|without)\b', ctx, re.I): fail('wording: tutor text suggests private chat: ' + ctx)
    for pat in (r'whiteboards? up', r'hold(s)? up (the|your) board', r'early finisher'):
        if re.search(pat, notes, re.I): fail('wording: tutor text uses banned phrase ' + pat)
    ar = [w for w in re.findall(r'\b(colour|color|program|programme|centre|center)\b', ' '.join(child_strings(d)), re.I)]
    if any(w.lower() in ('color', 'programme', 'center') for w in ar): warn('spelling: use British/Singapore spelling (colour, program, centre)')
    # no unicode shape/box glyphs
    allt = json.dumps(d, ensure_ascii=False)
    if re.search('[■-◿☀-➿\U0001F300-\U0001FAFF]', allt): fail('wording: unicode shape/emoji glyphs found (use drawn shapes)')
    # materials
    m = d['materials']
    if 'ruler' in json.dumps(m['child']).lower() and not m.get('ruler'): fail('materials: a ruler is listed but materials.ruler is false')
    if re.search(r'\b(buy|purchase|order online)\b', json.dumps(m), re.I): fail('materials: items must be findable at home (no buying)')
    # reading load: sentences in child text
    lim = d.get('limits', {})
    pr = d['parent']; pstr = {pr['summary'], pr['when_stuck'], pr['next'], pr['report_line'], pr['term_line']} | set(pr['try_home'])
    cl = [s for s in child_strings(d) if s not in pstr and len(s.split()) > lim.get('max_child_words', 40)]
    if cl: warn(f"reading load: {len(cl)} child-facing strings over {lim.get('max_child_words', 40)} words (e.g. {cl[0][:60]}...)")
    pl = [s for s in pstr if len(s.split()) > lim.get('max_parent_words', 90)]
    if pl: warn(f"parent text: {len(pl)} parent strings over {lim.get('max_parent_words', 90)} words (set limits.max_parent_words to change)")


def check_spare(d):
    sp = d.get('spare_time')
    if not sp: fail('spare: missing spare_time'); return
    if not 2 <= len(sp['menu']) <= 3: fail('spare: menu needs 2 or 3 activities')
    for m in sp['menu']:
        if not 3 <= m['minutes'] <= 5: fail(f"spare: {m['id']} must be 3 to 5 minutes")
        if words(m['rec']) > MAX_REC_WORDS: fail(f"spare: {m['id']} cue over {MAX_REC_WORDS} words")
        for k in ('tutor', 'answer', 'title'):
            if not m.get(k): fail(f"spare: {m['id']} missing {k}")
    txt = ' '.join(sp['rules']).lower()
    for must in ('whole class', 'few children', 'how do you know', 'next lesson'):
        if must not in txt: fail(f"spare: rules must mention '{must}'")
    alltxt = json.dumps(sp)
    if re.search(r'early finisher|fast finisher|fast[- ]track|gifted|strong thinker', alltxt, re.I): fail('spare: banned label in spare_time')
    if not any(s.get('optional') and 'menu' in s['id'] for s in d['slides']): fail('spare: needs an optional menu slide (id contains menu)')
    ok(f"spare: {len(sp['menu'])} spare-time activities, {sum(m['minutes'] for m in sp['menu'])} optional minutes (not in the 90 sum), rules present")


def check_pages(d):
    try:
        import b_print
        from playwright.sync_api import sync_playwright
        with sync_playwright() as pw:
            b = pw.chromium.launch(); fills = b_print.page_fill(pw if False else b, d); b.close()
    except Exception as e:
        warn('pages: could not measure workbook page fill: ' + str(e)); return
    d['_fills'] = fills
    for i, f in enumerate(fills, 1):
        if f < 0.80: warn(f'pages: workbook page {i} content ends at {f:.0%} of the page (target at least 85%): add a question or bigger writing space')
        if f > 1.04: warn(f'pages: workbook page {i} overflows ({f:.0%}): it will spill onto an extra page')
    ok('pages: workbook page fill ' + ', '.join(f'{f:.0%}' for f in fills) + ' (kit page excluded)')


def check_next_materials(d):
    p = d['parent']
    if re.search(r'pencil and paper|only a pencil', p.get('next', ''), re.I) and not p.get('next_materials'):
        warn('parent: "Next lesson" says pencil and paper only but parent.next_materials is not set (list what the NEXT lesson needs)')
    if d['lesson_in_term'] < 10 and not p.get('next_materials'):
        warn('parent: set parent.next_materials (a list of what the next lesson needs) so the Parent Summary tells families what to have ready')


def check_slide_privacy(d):
    """No phone number or contact detail on any slide or tool footer (slides are recorded and shared)."""
    bad = []
    for s in d['slides']:
        t = json.dumps(s['blocks']) + ' ' + s['title']
        if re.search(r'\+?\d{2}\s?\d{4}\s?\d{4}|\b\d{8}\b|@[a-z0-9.-]+\.[a-z]{2,}|https?://', t): bad.append(s['id'])
    if bad: fail('privacy: phone number, email or link on recorded slide(s) ' + ', '.join(bad) + ' (say it aloud or put it in the grown-up note instead)')
    else: ok('privacy: no phone number, email or link on any slide')


def check_mascot(d):
    ms = [s for s in d['slides'] if s.get('mascot')]
    if len(ms) > 5: fail(f'mascot: Mi appears on {len(ms)} slides (max 5, modest use)')
    for s in ms:
        say = s['mascot'].get('say', '')
        if re.search(r'\d', say) or len(say.split()) > 14: fail(f"mascot: Mi's line on {s['id']} must be short and say nothing about answers or numbers")
    if not os.path.exists(os.path.join(L1, 'assets', 'mi_dolphin_transparent.png')): fail('mascot: term/l1/assets/mi_dolphin_transparent.png missing')
    else: ok(f'mascot: Mi on {len(ms)} slides, short friendly lines only')


def check_outputs(d):
    """Measure the REAL rendered PDFs (page count and ink fill), if built. FAIL on orphan or near-empty pages."""
    import pdfcheck, b_print
    od = os.path.join(OUT, f"l{d['_num']}")
    want = {'Workbook': (b_print.workbook_html(d).count('<div class="page'), (14, 16)), 'Home_Practice': (2, (14, 16)), 'Parent_Summary': (1, (12, 12))}
    for name, (n, mg) in want.items():
        path = os.path.join(od, f"L{d['_num']}_{name}.pdf")
        if not os.path.exists(path):
            warn(f'outputs: {name} not built yet, real page check skipped'); continue
        got = pdfcheck.pdf_pages(path); fills = pdfcheck.pdf_fill(path, *mg)
        txt = ', '.join(f'{f:.0%}' for f in fills)
        if got != n: fail(f'outputs: {name} PDF has {got} pages but {n} are designed (a question block spilled onto an orphan page); fill {txt}')
        for i, f in enumerate(fills, 1):
            if f < 0.40: fail(f'outputs: {name} page {i} is only {f:.0%} full (orphan or near-empty page)')
            elif f < 0.80 and not (name == 'Home_Practice' and i == 2): warn(f'outputs: {name} page {i} is {f:.0%} full (target at least 85%)')
        if name == 'Workbook':
            import subprocess
            for pgno in range(1, got + 1):
                tx = subprocess.run(['pdftotext', '-layout', '-f', str(pgno), '-l', str(pgno), path, '-'], capture_output=True, text=True).stdout
                lines = [l.strip() for l in tx.splitlines() if l.strip() and not l.strip().startswith('Math Inquirers') and not re.fullmatch(r'Page \d+', l.strip())]
                lines = [l for l in lines if not re.fullmatch(r'Page\s*\d+', l)]
                if lines and re.fullmatch(r'No\.?\s*[A-Z]?\d+', lines[-1]): fail(f'outputs: Workbook page {pgno} ends with a question tab ({lines[-1]}) and its body is on the next page')
        if name == 'Parent_Summary': pass
        if got == n and all(f >= 0.40 for f in fills): ok(f'outputs: {name} PDF {got} pages, fill (measured on the PDF) {txt}')


def check_rec(d):
    for k, r in d['rec'].items():
        n = words(r['say'])
        if n > MAX_REC_WORDS: fail(f'rec: cue for {k} is {n} words (max {MAX_REC_WORDS})')
        if not r.get('action'): fail(f'rec: cue for {k} has no action line')
    if not [f for f in FAILS if f.startswith('rec')]: ok(f'rec: {len(d["rec"])} cues, each at most {MAX_REC_WORDS} words, each with an action line')
    # each REC line in script must exist at part start
    for seg in d['script']['segments']:
        if seg['part'] in ('opening', 'flex'): continue
        if not any(ln['k'] == 'REC' for ln in seg['lines'][:3]): fail(f"rec: segment {seg['part']} must start with a REC line")


def shingles(text, n=7):
    w = re.findall(r'[a-z0-9]+', text.lower())
    return {' '.join(w[i:i + n]) for i in range(len(w) - n + 1)}


STANDARD_PHRASES = [  # standard school-paper command wording (WORDING_GUIDE.md): allowed, never counted as copied problem text
    r"arrange the numbers in order\.?(\s*begin with the (smallest|greatest|biggest|largest)\.?)?", r"begin with the (smallest|greatest|biggest|largest)\.?",
    r"make the (greatest|smallest|biggest|largest) number( and the (greatest|smallest|biggest|largest) number)?", r"is \w+ correct\?\s*circle yes or no\.?",
    r"circle yes or no", r"circle (the correct|the right) answer", r"fill in the (missing numbers?|blanks?|correct answers? in the spaces provided)",
    r"write your answers? in the boxes provided", r"show all your workings clearly", r"tick \W?.?\W? ?true or false", r"count and write",
    r"write a number sentence", r"find the total", r"complete the (table|pattern|number sentences?)", r"write the number", r"how many \w+ (are )?(there )?altogether\??"]


def std_strip(text):
    t = text.lower()
    for p in STANDARD_PHRASES: t = re.sub(p, ' ', t)
    return t


def check_copy(d):
    own = set()
    for q in all_questions(d) + d['exit'] + d['home_practice']:
        own |= shingles(std_strip(q.get('text', '') + ' ' + ' '.join(p['text'] for p in q.get('parts', []))))
    own |= shingles(std_strip(d['sneak_peek']['q1'] + ' ' + d['sneak_peek']['q2']))
    for it in d['online_practice']['items']: own |= shingles(std_strip(it['q']))
    hits = []
    for folder in ('docs/sasmo', 'docs/books'):
        full = os.path.join(ROOT, folder)
        for f in sorted(os.listdir(full)):
            if not f.endswith('.md') or 'original' in f: continue
            src = shingles(std_strip(open(os.path.join(full, f), encoding='utf-8', errors='ignore').read()))
            common = own & src
            if common: hits.append((f, sorted(common)[:2]))
    if hits: fail('copy: 7-word overlaps with reference contest/book text: ' + str(hits))
    else: ok('copy: no 7-word overlap with docs/sasmo analysis/solution notes or docs/books (originals only)')


def load_checks(d):
    path = os.path.join(L1, 'verify', f"l{d['_num']}_checks.py")
    if not os.path.exists(path):
        fail('verify: no term/l1/verify/lNN_checks.py'); return None
    spec = importlib.util.spec_from_file_location('checks' + d['_num'], path)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m


def py_eval(expr, env):
    s = expr
    for k in sorted(env, key=len, reverse=True): s = re.sub(r'\b%s\b' % re.escape(k), str(env[k]), s)
    assert re.fullmatch(r'[\d\s+\-*/%().]*', s), expr
    return eval(s)


def check_answers(d):
    m = load_checks(d)
    if not m: return
    try:
        n = m.run(d)
        ok(f'verify: {n} answer checks by independent script passed (term/l1/verify/l{d["_num"]}_checks.py)')
    except AssertionError as e:
        fail('verify: answer check FAILED: ' + str(e))
    # practice variants
    oracles = getattr(m, 'ORACLES', {})
    items = d['online_practice']['items']
    js_cases = []
    total = 0
    for it in items:
        tp = it.get('tpl')
        if not tp: continue
        if it['id'] not in oracles: fail(f"practice: {it['id']} has a template but no brute-force oracle in the checks file"); continue
        names = list(tp['vars'])
        for combo in itertools.product(*[tp['vars'][n] for n in names]):
            env = dict(zip(names, combo))
            full = dict(env)
            for k, ex in tp.get('derive', {}).items(): full[k] = py_eval(ex, full)
            a = py_eval(tp['answer'].replace('//', '/'), full) if '//' not in tp['answer'] else py_eval(tp['answer'], full)
            if '//' in tp['answer']: a = int(a) if a == int(a) else a
            else: a = a
            exp = oracles[it['id']](env)
            if a != exp: fail(f"practice: {it['id']} variant {env}: expression gives {a} but oracle gives {exp}")
            if a != int(a) or a < 0: fail(f"practice: {it['id']} variant {env}: answer {a} is not a whole number >= 0")
            for txt in [tp['q'], tp['hint']] + tp['steps']:
                miss = [x for x in re.findall(r'\{(\w+)\}', txt) if x not in full and x != 'ans']
                if miss: fail(f"practice: {it['id']} placeholder {miss} not defined")
            total += 1
            js_cases.append((it['id'], tp['answer'], full, a))
        # authored value equals the template at its own numbers
        base = oracles[it['id']]
        if it['type'] == 'number':
            assert isinstance(it['answer'], int), it['id']
        if it['id'] in getattr(m, 'BASE_ENV', {}):
            env = m.BASE_ENV[it['id']]
            if base(env) != it['answer']: fail(f"practice: {it['id']} authored answer {it['answer']} differs from oracle at its own numbers")
    # slips must be wrong
    for it in items:
        for s in it.get('slips', []):
            for a in s['a']:
                if it['type'] == 'number' and a == it['answer']: fail(f"practice: {it['id']} has a slip equal to the right answer")
                if it['type'] == 'choice' and a == it['answer']: fail(f"practice: {it['id']} slip equals right answer")
        if it.get('ordered') and it['type'] != 'set': fail(f"practice: {it['id']} ordered only applies to set items")
        if it['type'] == 'choice' and it['answer'] not in it['options']: fail(f"practice: {it['id']} answer not among options")
    # cross-check with the runner's JavaScript calc()
    js = os.path.join(L1, 'runner', 'practice.js')
    src = open(js, encoding='utf-8').read()
    a = src.index('function calc'); b = src.index('function fill')
    calc = src[a:b]
    harness = calc + '\nconst cases=JSON.parse(process.argv[1]);const bad=[];cases.forEach(c=>{try{const v=calc(c[1],c[2]);if(v!==c[3])bad.push([c[0],c[2],v,c[3]]);}catch(e){bad.push([c[0],String(e)])}});console.log(JSON.stringify(bad));'
    try:
        r = subprocess.run(['node', '-e', harness, json.dumps(js_cases)], capture_output=True, text=True, timeout=60)
        bad = json.loads(r.stdout.strip() or '["node failed: ' + r.stderr[:200].replace('"', "'") + '"]')
        if bad: fail(f'practice: runner JS calc disagrees with python on {len(bad)} cases, e.g. {bad[:2]}')
        else: ok(f'practice: {total} template variants verified three ways (expression, brute-force oracle, runner JavaScript calc)')
    except Exception as e:
        warn('practice: could not run node cross-check: ' + str(e))


def check_key_pdf(d):
    """Answer key PDF: no section heading may end a page with its block on the next page."""
    import subprocess
    path = os.path.join(OUT, f"l{d['_num']}", f"L{d['_num']}_Workbook_Answer_Key.pdf")
    if not os.path.exists(path): return
    import pdfcheck
    for pg in range(1, pdfcheck.pdf_pages(path) + 1):
        tx = subprocess.run(['pdftotext', '-layout', '-f', str(pg), '-l', str(pg), path, '-'], capture_output=True, text=True).stdout
        lines = [l.strip() for l in tx.splitlines() if l.strip() and not l.strip().startswith('Math Inquirers') and not re.fullmatch(r'Page\s*\d+', l.strip())]
        if lines and re.match(r'^(Start here|Think harder|Go further|Investigation|Exit ticket|Sneak-peek)\b.{0,60}$', lines[-1]) and not re.search(r'\d', lines[-1][-6:]):
            fail(f'outputs: answer key page {pg} ends with the heading "{lines[-1]}" and its block is on the next page')


def check_term_check(d):
    """Lesson 10 end-of-term check: page counts and the printed 10 cm bar and 9 cm line measured on the rendered PDF."""
    c = d.get('end_of_term_check')
    if not c: return
    import pdfcheck, b_check
    od = os.path.join(OUT, f"l{d['_num']}")
    sheet = os.path.join(od, f"L{d['_num']}_Check_Student.pdf"); key = os.path.join(od, f"L{d['_num']}_Check_Tutor_Key.pdf"); note = os.path.join(od, f"L{d['_num']}_Check_Parent_Note.pdf")
    if not all(os.path.exists(p) for p in (sheet, key, note)):
        fail('term check: Check_Student / Check_Tutor_Key / Check_Parent_Note PDFs not built (run build.sh)'); return
    m = b_check
    n = pdfcheck.pdf_pages(sheet)
    if n != c['sheet_pages']: fail(f"term check: student sheet has {n} pages, designed {c['sheet_pages']}")
    if pdfcheck.pdf_pages(note) != 1: fail('term check: grown-up note must be one page')
    fills = pdfcheck.pdf_fill(sheet, 12.0, 15.0)
    for i, f in enumerate(fills, 1):
        if f < 0.40: fail(f'term check: student sheet page {i} only {f:.0%} full')
    bar, line = m.measure_sheet(sheet, c)
    for name, got, want in (('10 cm bar', bar, c['sheet_check_bar_mm']),):
        if got is None or abs(got - want) > 0.6: fail(f'term check: printed {name} measures {got} mm, must be {want} mm (within 0.6 mm)')
    if bar is not None and not [f for f in FAILS if f.startswith('term check')]:
        ok(f"term check: student sheet {n} pages, key {pdfcheck.pdf_pages(key)} pages, note 1 page; printed bar {bar:.2f} mm (want {c['sheet_check_bar_mm']}), measured on the PDF")


def check_cover(d):
    import b_guide
    from playwright.sync_api import sync_playwright
    hp = os.path.join(OUT, f"l{d['_num']}", f"L{d['_num']}_Tutor_Guide.html")
    if not os.path.exists(hp): return
    with sync_playwright() as pw:
        b = pw.chromium.launch(); pr = b_guide.cover_overlap(b, hp); b.close()
    if pr: fail('guide cover: ' + '; '.join(pr))
    else: ok('guide cover: Mi does not overlap the title or text')


def check_foreign(d):
    """Built outputs of lesson NN must not contain another lesson's title or 'Lesson 1' text (template leaks)."""
    import glob, subprocess
    num = d['_num']
    od = os.path.join(OUT, f'l{num}')
    if not os.path.isdir(od): return
    others = {}
    for f in glob.glob(os.path.join(L1, 'lessons', 'l*.json')):
        n = os.path.basename(f)[1:3]
        if n != num:
            try: others[n] = json.load(open(f))['title']
            except Exception: pass
    texts = []
    for f in glob.glob(os.path.join(od, '*.html')) + glob.glob(os.path.join(od, 'html', '*.html')):
        texts.append((f, re.sub(r'<style.*?</style>|<[^>]+>', ' ', open(f, encoding='utf-8').read(), flags=re.S)))
    for f in glob.glob(os.path.join(od, '*.pdf')):
        try: texts.append((f, subprocess.run(['pdftotext', f, '-'], capture_output=True, text=True).stdout))
        except Exception: pass
    bad = []
    for f, t in texts:
        t1 = re.sub(r'\s+', ' ', t)
        for n, title in others.items():
            for m in re.finditer(re.escape(title.lower()), t1.lower()):
                if title.lower() == d['title'].lower(): continue
                before = t1[max(0, m.start() - 45):m.start()].lower()
                if re.search(r'next lesson|lesson \d+:?\s*$|lessons? \d+', before): continue   # a pointer to the next lesson is allowed
                bad.append(f"{os.path.basename(f)} mentions lesson {n} title '{title}'"); break
        if num != '01' and re.search(r'\bLesson 1\b(?!\d)', t1) and not re.search(r'Lesson 1 (of|onwards)', t1[:0]):
            hits = [m.start() for m in re.finditer(r'\bLesson 1\b(?!\d)', t1)]
            for h in hits:
                ctx = t1[max(0, h - 40):h + 30]
                if not re.search(r'previous|earlier|Lesson 1 to|Lessons? 1,|from Lesson 1|in Lesson 1', ctx, re.I): bad.append(f"{os.path.basename(f)} contains 'Lesson 1' ({ctx.strip()})")
        if re.search(r'bundles and singles', t1, re.I) and 'bundle' not in d['title'].lower() and num != '01': bad.append(f"{os.path.basename(f)} mentions Bundles and Singles")
    if bad: fail('template leak: ' + '; '.join(sorted(set(bad))[:6]))
    else: ok('template leak: no other lesson title or stray Lesson 1 text in the built files')


def check_all(num, built=True):
    d = load(num)
    for fn in (check_schema, check_timing, check_slides_links, check_tiers, check_workbook_items, check_words, check_pages, check_next_materials, check_slide_privacy, check_mascot, check_rec, check_spare, check_copy, check_answers):
        try:
            fn(d)
        except Exception as e:
            fail(f'{fn.__name__} crashed: {type(e).__name__}: {e}')
    if built:
        for fn in (check_outputs, check_key_pdf, check_cover, check_term_check, check_foreign):
            try: fn(d)
            except Exception as e: fail(f'{fn.__name__} crashed: {type(e).__name__}: {e}')
    return d


def main():
    num = sys.argv[1] if len(sys.argv) > 1 else '01'
    d = check_all(num, built='--no-built' not in sys.argv)
    print(f"== validate lesson {num}: {d['title']}")
    for p in PASSES: print('PASS  ' + p)
    for w in WARNS: print('WARN  ' + w)
    for f in FAILS: print('FAIL  ' + f)
    if '_timing_rows' in d:
        print('\npart        alloc   script  slow    flag')
        for (p, a, u, sl, fl) in d['_timing_rows']:
            print(f'{p:<10}  {mmss(a):>5}  {mmss(u):>6}  {mmss(sl):>5}   {fl}')
        u, sl = d['_timing_total']
        print(f"{'TOTAL':<10}  {'90:00':>5}  {mmss(u):>6}  {mmss(sl):>5}")
    print(f'\n{len(PASSES)} pass, {len(WARNS)} warn, {len(FAILS)} FAIL')
    sys.exit(1 if FAILS else 0)


if __name__ == '__main__':
    main()
