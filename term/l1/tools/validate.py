#!/usr/bin/env python3
"""Validate one lesson file.  Usage: python3 term/l1/tools/validate.py 01   (exit code 1 on any FAIL)

Checks: schema keys, timing (parts sum to exactly 90, script fits each part, slow-class scenario), slides <-> script links,
question completeness, tier rules, banned wording, REC cue length, link check, no copied contest text (7-word shingles
against docs/sasmo and docs/books), per-lesson answer verification (term/l1/verify/lNN_checks.py), practice-variant
verification (python oracle vs expression vs the runner's own JavaScript calc).
"""
import glob, importlib.util, itertools, json, os, re, subprocess, sys

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
                r'SASMO', r'olympiad', r'exam prep', r'\bchallenge\b(?!\s+Quest)', r'\bstretch\b', r'\bcore\b', r'high[- ]ability', r'ahead of', r'\branked?\b', r'top of the class']
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
    nk = max(1, kit_pages_total(d))
    if d.get('workbook', {}).get('exit_page'): pages = pages | {max(pages) + 1}        # exit ticket and look-back have their own page
    kp = set(range(6, 7 + nk)) | set(range(max(pages) + 1, max(pages) + 1 + nk))
    for m in re.finditer(r'\bpages? (\d+)', txt, re.I):
        if int(m.group(1)) not in pages | kp: fail(f'link: text mentions page {m.group(1)} which does not exist (pages {sorted(pages)} and kit pages {sorted(kp)})')


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
        vj = json.dumps([q.get('visual'), q.get('visuals')])
        on_picture = bool(vis.get('hide')) or vis.get('labels') == 'box' or any((x or {}).get('labels') == 'box' or (x or {}).get('hide') for x in (q.get('visuals') or [])) or bool(re.search(r'"(\[\]|\(\)|\[\d\]|\[ \])"', vj)) or '"hide": [' in vj or '"hide_price": true' in vj   # empty boxes, circles or hidden cells drawn in a picture are answer slots
        if q.get('tf') or q.get('mcq') or q.get('steps'): on_picture = True
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
                for m in re.finditer(r'(\d+)\s+(groups?|rows?|plates?|bags?)\s+of\s+(\d+)', t): est += int(m.group(1)) * int(m.group(3))
                t = re.sub(r'(\d+)\s+(groups?|rows?|plates?|bags?)\s+of\s+(\d+)', ' ', t)
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
    if 'challenge_quest' in d:      # the end-of-term slot is a game: no test / exam / score wording on child or parent pages (the program motto stays)
        QBAN = [r'\b(term|end-of-term|final|school|unit)\s+tests?\b', r'\btests?\s+(paper|sheet|day|score|result)s?\b', r'\btake (a|the) test\b', r'\bexams?\b', r'check[- ]?sheet', r'end-of-term check', r'\btimer\b', r'\bscored?\b|\bscores\b', r'\bmarked\b|\bmarks\b|\bmarking\b', r'\bgrades?\b', r'\bout of\b']
        for s in child_strings(d):
            t = re.sub(r'Notice it\. Test it\. Explain why\.?', ' ', s)
            for pat in QBAN:
                m = re.search(pat, t, re.I)
                if m and not re.search(r'\b(no|never|not|without)\b[^.]{0,40}' + pat, t, re.I): bad.append((pat, s[:70]))
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
    wbp = os.path.join(OUT, f"l{d['_num']}", f"L{d['_num']}_Workbook.pdf")
    if os.path.exists(wbp):      # the built PDF is the truth; the layout model can over-report (the builder tightens pages to fit)
        import pdfcheck
        allf = pdfcheck.pdf_fill(wbp, 14, 16)
        fills = allf[:len(allf) - kit_pages_total(d)] if kits(d) else allf
        d['_fills'] = fills
        for i, f in enumerate(fills, 1):
            if f < 0.80: warn(f'pages: workbook page {i} content ends at {f:.0%} of the page (target at least 85%): add a question or bigger writing space')
        ok('pages: workbook page fill (measured on the built PDF) ' + ', '.join(f'{f:.0%}' for f in fills) + ' (kit pages excluded)')
        return
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
    want = {'Workbook': (b_print.workbook_html(d).count('<div class="page'), (14, 16)), 'Home_Practice': (1, (14, 16)), 'Home_Answers': (1, (14, 16)), 'Parent_Summary': (1, (12, 12))}
    for name, (n, mg) in want.items():
        path = os.path.join(od, f"L{d['_num']}_{name}.pdf")
        if not os.path.exists(path):
            warn(f'outputs: {name} not built yet, real page check skipped'); continue
        got = pdfcheck.pdf_pages(path); fills = pdfcheck.pdf_fill(path, *mg)
        txt = ', '.join(f'{f:.0%}' for f in fills)
        if got != n: fail(f'outputs: {name} PDF has {got} pages but {n} are designed (a question block spilled onto an orphan page); fill {txt}')
        nk = kit_pages_total(d) if name == 'Workbook' else 0          # a kit page may be short (play money coins, sticks): only question pages must be full
        for i, f in enumerate(fills, 1):
            if f < 0.40 and not (nk and i > len(fills) - nk and got == n): fail(f'outputs: {name} page {i} is only {f:.0%} full (orphan or near-empty page)')
            elif f < 0.80 and name != 'Home_Answers': warn(f'outputs: {name} page {i} is {f:.0%} full (target at least 85%)')
        if name == 'Workbook':
            import subprocess
            for pgno in range(1, got + 1):
                tx = subprocess.run(['pdftotext', '-layout', '-f', str(pgno), '-l', str(pgno), path, '-'], capture_output=True, text=True).stdout
                lines = [l.strip() for l in tx.splitlines() if l.strip() and not l.strip().startswith('Math Inquirers') and not re.fullmatch(r'Page \d+', l.strip())]
                lines = [l for l in lines if not re.fullmatch(r'Page\s*\d+', l)]
                if lines and re.fullmatch(r'No\.?\s*[A-Z]?\d+', lines[-1]): fail(f'outputs: Workbook page {pgno} ends with a question tab ({lines[-1]}) and its body is on the next page')
        if name == 'Parent_Summary': pass
        if got == n and all(f >= 0.40 for f in (fills[:len(fills) - nk] if nk else fills)): ok(f'outputs: {name} PDF {got} pages, fill (measured on the PDF) {txt}')


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
    r"write a number sentence", r"find the total", r"complete the (table|pattern|number sentences?)", r"put a tick (\\(.\\) )?in the correct box", r"tick (\\(.\\) )?true or false", r"write a multiplication sentence", r"how many more to make equal groups", r"write the number", r"how many \w+ (are )?(there )?altogether\??", r"how many \w+ do (they|you|we|the children|the \w+) have altogether\??"]


def std_strip(text):
    t = text.lower()
    for p in STANDARD_PHRASES: t = re.sub(p, ' ', t)
    return t


def is_external_source(name):
    """True for text we did NOT author: private extracts (private_*), contest/school-paper analyses and pattern notes.
    Our own original work (non-routine catalogues, *original* drafts) is never an external source."""
    n = name.lower()
    if 'original' in n or 'catalogue' in n: return False
    return n.startswith('private_') or n.endswith('_analysis.md') or 'patterns' in n or '/private_' in n


def external_sources(root=None):
    """Yield (relative name, text) for every external source text under docs/sasmo and docs/books (recursing into private_* folders)."""
    root = root or ROOT
    for folder in ('docs/sasmo', 'docs/books'):
        base = os.path.join(root, folder)
        if not os.path.isdir(base): continue
        for dp, dns, fns in os.walk(base):
            dns.sort()
            rel_dir = os.path.relpath(dp, root).replace(os.sep, '/')
            for f in sorted(fns):
                if not f.lower().endswith(('.md', '.txt')): continue
                rel = rel_dir + '/' + f
                in_private = '/private_' in rel
                if not (in_private or is_external_source(f)): continue
                if 'original' in f.lower() or 'catalogue' in f.lower(): continue
                yield rel, open(os.path.join(dp, f), encoding='utf-8', errors='ignore').read()


def check_copy(d):
    own = set()
    for q in all_questions(d) + d['exit'] + d['home_practice']:
        own |= shingles(std_strip(q.get('text', '') + ' ' + ' '.join(p['text'] for p in q.get('parts', []))))
    own |= shingles(std_strip(d['sneak_peek']['q1'] + ' ' + d['sneak_peek']['q2']))
    for it in d['online_practice']['items']: own |= shingles(std_strip(it['q']))
    hits = []
    for f, txt in external_sources():
        common = own & shingles(std_strip(txt))
        if common: hits.append((f, sorted(common)[:2]))
    if hits: fail('copy: 7-word overlaps with reference contest/book text: ' + str(hits))
    else: ok('copy: no 7-word overlap with external source text (contest/book/school-paper analyses and private extracts; our own catalogues and drafts excluded)')


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
            exp = oracles[it['id']](env)
            if tp.get('answers'):                                   # R2: several ordered boxes, one expression per field
                got = {f: eval_expr(ex, full) for f, ex in tp['answers'].items()}
                if got != exp: fail(f"practice: {it['id']} variant {env}: fields give {got} but oracle gives {exp}")
                for f, ex in tp['answers'].items(): js_cases.append((it['id'] + '.' + f, ex, full, got[f]))
            elif tp.get('options') is not None:                      # R5: templated choice, answer_index is an expression
                idx = int(eval_expr(tp['answer_index'], full))
                if not 0 <= idx < len(tp['options']): fail(f"practice: {it['id']} variant {env}: answer_index {idx} outside the options")
                elif tp['options'][idx] != exp: fail(f"practice: {it['id']} variant {env}: option {tp['options'][idx]!r} but oracle gives {exp!r}")
                js_cases.append((it['id'], tp['answer_index'], full, idx))
            else:
                a = eval_expr(tp['answer'], full)
                if a != exp: fail(f"practice: {it['id']} variant {env}: expression gives {a} but oracle gives {exp}")
                if not isinstance(a, list) and (a != int(a) or a < 0): fail(f"practice: {it['id']} variant {env}: answer {a} is not a whole number >= 0")
                js_cases.append((it['id'], tp['answer'], full, a))
            texts = [tp.get('q', ''), tp.get('hint', '')] + list(tp.get('steps', [])) + list(tp.get('options') or []) + [tp.get('frame', '')]
            for txt in texts:
                miss = [x for x in re.findall(r'\{(\w+)(?:\|\w+)?\}', txt) if x not in full and x != 'ans' and x not in (tp.get('answers') or {})]
                if miss: fail(f"practice: {it['id']} placeholder {miss} not defined")
            total += 1
        base = oracles[it['id']]
        if it['id'] in getattr(m, 'BASE_ENV', {}) and it['type'] in ('number', 'choice', 'set'):
            env = m.BASE_ENV[it['id']]
            exp0 = base(env)
            if it['type'] == 'number' and it['answer'] != exp0: fail(f"practice: {it['id']} authored answer {it['answer']} differs from oracle at its own numbers")
    for it in items:                                                 # slips must be wrong; shapes of the new types
        for s in it.get('slips', []):
            for a in s['a']:
                if it['type'] == 'number' and a == it['answer']: fail(f"practice: {it['id']} has a slip equal to the right answer")
                if it['type'] == 'choice' and a == it['answer']: fail(f"practice: {it['id']} slip equals right answer")
        if it.get('ordered') and it['type'] != 'set': fail(f"practice: {it['id']} ordered only applies to set items")
        if it['type'] == 'choice' and 'tpl' not in it and it['answer'] not in it['options']: fail(f"practice: {it['id']} answer not among options")
        if it['type'] == 'fields':
            fr = it.get('frame', '')
            ids = [f['id'] for f in it.get('fields', [])]
            if not ids or any('{' + i + '}' not in fr for i in ids): fail(f"practice: {it['id']} fields item: every field id must appear as {{id}} in the frame")
            stray = [m for m in re.findall(r'\{(\w+)\}', fr) if m not in ids]
            if stray: warn(f"practice: {it['id']} fields item: frame has {{{stray[0]}}} which is not a field (write the number in the frame, or add a field)")
        if it.get('fig'):
            import svg
            try: svg.render_visual(it['fig'] if not has_placeholder(it['fig']) else it['fig_base'])
            except Exception as e: fail(f"practice: {it['id']} fig does not render: {e}")
    # cross-check with the runner's JavaScript calc() (same helpers as the python oracle)
    js = os.path.join(L1, 'runner', 'practice.js')
    src = open(js, encoding='utf-8').read()
    a = src.index('function calc'); b = src.index('function fill')
    calc = src[a:b]
    helpers = src[src.index('var HELP'):src.index('function calc')] if 'var HELP' in src else ''
    harness = helpers + calc + '\nconst cases=JSON.parse(process.argv[1]);const bad=[];cases.forEach(c=>{try{const v=calc(c[1],c[2]);if(JSON.stringify(v)!==JSON.stringify(c[3]))bad.push([c[0],c[2],v,c[3]]);}catch(e){bad.push([c[0],String(e)])}});console.log(JSON.stringify(bad));'
    try:
        r = subprocess.run(['node', '-e', harness, json.dumps(js_cases)], capture_output=True, text=True, timeout=120)
        bad = json.loads(r.stdout.strip() or '["node failed: ' + r.stderr[:200].replace('"', "'") + '"]')
        if bad: fail(f'practice: runner JS calc disagrees with python on {len(bad)} cases, e.g. {bad[:2]}')
        else: ok(f'practice: {total} template variants verified three ways (expression, brute-force oracle, runner JavaScript calc)')
    except Exception as e:
        warn('practice: could not run node cross-check: ' + str(e))


HELPERS = {'multiples': lambda k, lim: [k * i for i in range(1, lim // k + 1)], 'common': lambda a, b, lim: [n for n in range(1, lim + 1) if n % a == 0 and n % b == 0],
           'divisors': lambda n: [i for i in range(1, n + 1) if n % i == 0]}


def eval_expr(expr, env):
    """Template expression: arithmetic (+ - * // % ( )) or one list helper multiples(k,limit) / common(a,b,limit) / divisors(n)."""
    m = re.fullmatch(r'\s*(multiples|common|divisors)\(([^)]*)\)\s*', expr)
    if m:
        args = [py_eval(x, env) for x in m.group(2).split(',')]
        return HELPERS[m.group(1)](*[int(x) for x in args])
    a = py_eval(expr.replace('//', '/'), env) if '//' not in expr else py_eval(expr, env)
    if '//' in expr and a == int(a): a = int(a)
    return a


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
    bar = line = None
    if c.get('sheet_check_bar_mm'):
        bar, line = m.measure_sheet(sheet, c)
        for name, got, want in (('10 cm bar', bar, c['sheet_check_bar_mm']),):
            if got is None or abs(got - want) > 0.6: fail(f'term check: printed {name} measures {got} mm, must be {want} mm (within 0.6 mm)')
    if not [f for f in FAILS if f.startswith('term check')]:
        ok(f"term check: student sheet {n} pages, key {pdfcheck.pdf_pages(key)} pages, note 1 page" + (f"; printed bar {bar:.2f} mm (want {c['sheet_check_bar_mm']}), measured on the PDF" if bar else ''))


def check_quest(d):
    """Mi's Challenge Quest lessons: the three Quest files exist, the Quest Log has its designed pages, no test/exam/score words in the child and parent PDFs."""
    c = d.get('challenge_quest')
    if not c: return
    import pdfcheck, subprocess, b_quest
    od = os.path.join(OUT, f"l{d['_num']}")
    log, notes, note = (os.path.join(od, f"L{d['_num']}_Quest_{x}.pdf") for x in ('Log', 'Tutor_Notes', 'Parent_Note'))
    if not all(os.path.exists(p) for p in (log, notes, note)):
        fail('quest: Quest_Log / Quest_Tutor_Notes / Quest_Parent_Note PDFs not built (run build.sh)'); return
    n = pdfcheck.pdf_pages(log)
    if n != c['sheet_pages']: fail(f"quest: Quest Log has {n} pages, designed {c['sheet_pages']}")
    if pdfcheck.pdf_pages(note) != 1: fail('quest: grown-up note must be one page')
    for p in glob.glob(os.path.join(od, f"L{d['_num']}_Check_*.pdf")): fail('quest: old check file still present: ' + os.path.basename(p))
    for p in (log, note):
        tx = subprocess.run(['pdftotext', p, '-'], capture_output=True, text=True).stdout
        for pat in b_quest.BAN_FAMILY:
            m = re.search(pat, tx, re.I)
            if m: fail(f"quest: {os.path.basename(p)} contains banned wording {pat!r}")
    if not [f for f in FAILS if f.startswith('quest')]: ok(f"quest: Quest Log {n} pages, tutor notes {pdfcheck.pdf_pages(notes)}, grown-up note 1 page, no test/exam/score wording")


def check_beyond(d):
    """Terms 3 and 4: the tutor-only `beyond` field names what goes past Primary 1: {"name", "where": [ids in Think harder or Go further], "text", optional "parent"}.
    It is never in Start here and never in the Explore or Quest-style class numbers. Required from Term 3 (a warning for Terms 1 and 2)."""
    b = d.get('beyond')
    if not b:
        if d['term'] >= 3: fail('beyond: Terms 3 and 4 lessons need a `beyond` field (name, where, text)')
        return
    for k in ('name', 'where', 'text'):
        if not b.get(k): fail(f'beyond: missing {k}')
    qm = {q['id']: t for t in ('start', 'think', 'go') for q in d['tiers'][t]}
    for i in b.get('where', []):
        if i not in qm: fail(f'beyond: {i} is not a workbook question')
        elif qm[i] == 'start': fail(f'beyond: {i} is a Start here question; beyond-P1 material belongs in Think harder or Go further')
    for t in ('name', 'text', 'parent'):
        if re.search(r'\b(early finisher|gifted|genius|GEP|SASMO|olympiad|aligned)\b', str(b.get(t, '')), re.I): fail(f'beyond: banned label in {t}')
    if not [f for f in FAILS if f.startswith('beyond')]: ok(f"beyond: {b['name']!r} sits at {', '.join(b['where'])}, not in Start here")


def check_kit_contract(d):
    """materials.kit_contract = [{piece, supplied, max_used, used_by: [ids]}]: what the kit page prints against the most any task uses (the cut-out audit's two Reworks)."""
    kc = d.get('materials', {}).get('kit_contract')
    if not kc:
        if kits(d) and d['term'] >= 3 and any(k.get('type') not in ('hundred', 'hundred_square', 'groups_mat', 'array_mat', 'grid_mat', 'graph_mat') for k in kits(d)):
            warn('kit contract: materials.kit_contract is missing (piece, supplied, max_used, used_by); needed so the kit page matches the tasks')
        return
    ids = {q['id'] for q in all_questions(d) + d['exit']}
    for r in kc:
        for k in ('piece', 'supplied', 'max_used'):
            if k not in r: fail(f"kit contract: {r.get('piece', '?')} missing {k}")
        if r.get('supplied', 0) < r.get('max_used', 0): fail(f"kit contract: {r['piece']}: the page supplies {r['supplied']} but a task uses {r['max_used']}")
        for i in r.get('used_by', []):
            if i not in ids and not str(i).startswith(('explore', 'mini', 'script')): fail(f"kit contract: {r['piece']} used_by {i} is not a question id")
    if not [f for f in FAILS if f.startswith('kit contract')]: ok(f'kit contract: {len(kc)} pieces, supplied is never less than the most any task uses')


def check_handoff(d):
    """The previous lesson's parent.next_materials must tell the family to cut or prepare this lesson's kit pages (cut-out audit F21)."""
    n = int(d['_num'])
    if n < 2: return
    pp = os.path.join(L1, 'lessons', f'l{n - 1:02d}.json')
    if not os.path.exists(pp): return
    try: prev = json.load(open(pp, encoding='utf-8'))
    except Exception: return
    cutkits = [k for k in kits(d) if k.get('type') not in ('hundred', 'hundred_square', 'groups_mat', 'array_mat', 'grid_mat', 'graph_mat', 'number_line')]
    nm = ' '.join(prev.get('parent', {}).get('next_materials', []))
    if cutkits and not re.search(r'\b(cut|kit|page|envelope|cards?|pieces)\b', nm, re.I): warn(f"hand-off: lesson {n - 1} next_materials does not mention this lesson's cut-out kit page")


def check_plural_guard(d):
    """Online practice variants must never print '1 hours', '1 stickers' and the like."""
    bad = []
    pat = re.compile(r'\b1 (hours|minutes|stickers|marbles|sweets|dollars|cents|children|cousins|plates|cookies|apples|pencils|books|coins|notes|sticks|days|tags|tokens|cups|bags|rows|groups)\b')
    for it in d['online_practice']['items']:
        tp = it.get('tpl')
        if not tp: continue
        names = list(tp['vars'])
        for combo in itertools.product(*[tp['vars'][n] for n in names]):
            env = dict(zip(names, combo)); full = dict(env)
            try:
                for k, ex in tp.get('derive', {}).items(): full[k] = py_eval(ex, full)
            except Exception: continue
            txt = ' '.join([tp.get('q', ''), tp.get('hint', ''), tp.get('frame', '')] + list(tp.get('steps', [])))
            txt = re.sub(r'\{(\w+)(?:\|(\w+))?\}', lambda m: str(full.get(m.group(1), m.group(0))), txt)
            m = pat.search(txt)
            if m: bad.append(f"{it['id']} {env}: '{m.group(0)}'")
            if re.search(r'(?<![.\s])\.\.(?!\.)', txt): bad.append(f"{it['id']} {env}: double full stop")
    if bad: (fail if d['term'] >= 3 else warn)('practice: plural or punctuation slips in variants: ' + '; '.join(bad[:5]))


def check_cover(d):
    import b_guide
    from playwright.sync_api import sync_playwright
    hp = os.path.join(OUT, f"l{d['_num']}", f"L{d['_num']}_Tutor_Guide.html")
    if not os.path.exists(hp): return
    with sync_playwright() as pw:
        b = pw.chromium.launch(); pr = b_guide.cover_overlap(b, hp); b.close()
    if pr: fail('guide cover: ' + '; '.join(pr))
    else: ok('guide cover: Mi does not overlap the title or text')


def check_identity(d):
    n = int(d['_num'])
    exp_term = (n - 1) // 10 + 1; exp_in = (n - 1) % 10 + 1
    if d['term'] != exp_term or d['lesson_in_term'] != exp_in or d['lesson'] != n:
        fail(f"identity: file l{d['_num']} should have term {exp_term}, lesson {n}, lesson_in_term {exp_in} (found {d['term']}, {d['lesson']}, {d['lesson_in_term']})")
    if d['id'] != f"l1-t{d['term']}-{exp_in:02d}" and d['id'] != f"l1-t{d['term']}-{n:02d}": fail(f"identity: id {d['id']} does not match term/lesson")
    if d['online_practice']['key'] != f"t{d['term']}l{d['_num']}": fail(f"identity: practice key must be t{d['term']}l{d['_num']} (found {d['online_practice']['key']})")
    if not [f for f in FAILS if f.startswith('identity')]: ok(f"identity: term {d['term']}, lesson {n}, lesson_in_term {exp_in}, practice key {d['online_practice']['key']}")


def check_figures(d):
    """Every figure spec in slides, questions and practice items must render (registered type, valid fields)."""
    import svg
    specs = []
    def walk(x):
        if isinstance(x, dict):
            if x.get('t') == 'visual' or ('type' in x and x.get('type') in FIGURE_TYPES): specs.append(x)
            for k, y in x.items():
                if k in ('visual', 'fig'): specs.append(y)
                walk(y)
        elif isinstance(x, list):
            for y in x: walk(y)
    for s in d['slides']: walk(s['blocks'])
    for q in all_questions(d) + d['exit']: walk(q)
    walk(d['tiers']['investigation'])
    for it in d['online_practice']['items']:
        if it.get('fig') and not has_placeholder(it['fig']): specs.append(it['fig'])
    n = 0
    for sp in specs:
        if not isinstance(sp, dict) or 'type' not in sp: continue
        try: svg.render_visual(sp); n += 1
        except Exception as e: fail(f"figures: {sp.get('type')} does not render: {type(e).__name__}: {e}")
    if not [f for f in FAILS if f.startswith('figures')]: ok(f'figures: {n} figure specs render')


def has_placeholder(x):
    """True if a figure spec holds a template placeholder such as "{n}" or "{=n+1}" (a plain JSON object does not count)."""
    return bool(re.search(r'"[^"]*\{=?\w[^"]*\}[^"]*"', json.dumps(x)))


FIGURE_TYPES = {'bundles', 'scatter', 'ten_frame', 'ten_to_bundle', 'hundred_square', 'hundred', 'seq', 'number_line', 'ruler', 'plates', 'objects', 'groups', 'array', 'line_up',
                'round_table', 'bar_model', 'table', 'picture_equation', 'domino', 'combos', 'jump_lines', 'balance', 'shelf',
                'clock', 'money', 'price_tag', 'calendar', 'stick_pattern', 'shapes2d', 'grid', 'cube_stack', 'fold_punch', 'panel', 'network', 'picture_graph'}


def check_glyphs(d):
    """x and division signs used in the lesson must survive into the built PDFs (text extraction) and the font files must be the latin subset."""
    import subprocess
    allt = json.dumps(d, ensure_ascii=False, default=str)
    used = [g for g in ('\u00d7', '\u00f7', '\u2212', '\u00a2') if g in allt]
    if not used: return
    od = os.path.join(OUT, f"l{d['_num']}")
    css = font_css()
    if 'latin-ext' in css.split('Fredoka')[1][:400] and 'latin-400' not in css: warn('glyphs: fonts.css may not be the latin subset')
    bad = []
    for name in ('Workbook', 'Home_Practice', 'Tutor_Guide'):
        p = os.path.join(od, f"L{d['_num']}_{name}.pdf")
        if not os.path.exists(p): continue
        tx = subprocess.run(['pdftotext', p, '-'], capture_output=True, text=True).stdout
        src = {'Workbook': {'t': d['tiers'], 'e': d['exit']}, 'Home_Practice': d['home_practice']}.get(name) or {k: v for k, v in d.items() if not k.startswith('_')}
        def strip(x):
            if isinstance(x, dict): return {k: strip(v) for k, v in x.items() if k not in ('answer', 'answers', 'hint', 'solution', 'look_for', 'mistakes', 'note', 'explain', 'why')}
            if isinstance(x, list): return [strip(v) for v in x]
            return x
        stext = json.dumps(strip(src) if name != 'Tutor_Guide' else src, ensure_ascii=False, default=str)
        for g in used:
            if g not in tx and g in stext: bad.append(f'{name}: {g!r} missing from the PDF text')
    if bad: fail('glyphs: ' + '; '.join(bad))
    else: ok('glyphs: x and division signs present in the built PDFs')


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
            try:
                o = json.load(open(f))
                if o.get('term') == d['term']: others[n] = o['title']      # only lessons of the same term are compared
            except Exception: pass
    own = json.dumps({k: v for k, v in d.items() if not k.startswith('_')}, ensure_ascii=False, default=str).lower()
    try:    # a lesson title that is also a tool name of the toolbox card (Lesson 28 'Make a Table') is not a leak when the tool is named
        tool_names = {t['name'].lower() for t in json.load(open(os.path.join(L1, '..', '..', 'levels', 'spine.json'), encoding='utf-8'))['tools']}
    except Exception: tool_names = set()
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
                if title.lower() == d['title'].lower() or title.lower() in own or title.lower() in tool_names: continue    # a phrase this lesson uses itself (e.g. 'equal groups') is not a leak
                before = t1[max(0, m.start() - 45):m.start()].lower()
                if re.search(r'next lesson|lesson \d+:?\s*$|lessons? \d+', before): continue   # a pointer to the next lesson is allowed
                bad.append(f"{os.path.basename(f)} mentions lesson {n} title '{title}'"); break
        if d['lesson_in_term'] != 1 and re.search(r'\bLesson 1\b(?!\d)', t1):
            hits = [m.start() for m in re.finditer(r'\bLesson 1\b(?!\d)', t1)]
            for h in hits:
                ctx = t1[max(0, h - 40):h + 30]
                tm = re.search(r'Term (\d) \u2022 Lesson 1', t1[max(0, h - 12):h + 9])
                if tm and int(tm.group(1)) != d['term']: continue          # a pointer to the first lesson of another term
                if not re.search(r'previous|earlier|Lesson 1 to|Lessons? 1,|from Lesson 1|in Lesson 1|Term \d,? (its )?Lesson 1|its Lesson 1', ctx, re.I): bad.append(f"{os.path.basename(f)} contains 'Lesson 1' ({ctx.strip()})")
        if d['term'] != 1 and re.search(r'Math Inquirers Term 1\b|\bTERM 1 (CHECK|\u2022)', t1): bad.append(f"{os.path.basename(f)} still says Term 1 (this is Term {d['term']})")
    if bad: fail('template leak: ' + '; '.join(sorted(set(bad))[:6]))
    else: ok('template leak: no other lesson title or stray Lesson 1 text in the built files')


def check_spine(d):
    """A lesson with a `spine` object: valid tool ids, at most 2 'also', the same row as spine_term.json, the Opening and look-back words present."""
    sp = d.get('spine')
    if not sp: return
    import spine_term as SPT
    ids = {t['id'] for t in SPT.TOOLS}
    tr = SPT._TERM['lessons'].get(str(d['lesson']))
    if sp.get('main') not in ids | {'choose'}: fail(f"spine: unknown main tool {sp.get('main')!r}")
    if any(a not in ids for a in sp.get('also', [])) or len(sp.get('also', [])) > 2 or sp.get('main') in sp.get('also', []): fail('spine: also must be 0-2 other tool ids')
    mt = set(SPT._TERM['tools_met'][str(d['term'])])
    if (sp.get('main') != 'choose' and sp.get('main') not in mt) or any(a not in mt for a in sp.get('also', [])): fail(f"spine: tools must be among those met in Term {d['term']}: {sorted(mt)}")
    if tr and (tr['main'] != sp.get('main') or tr['also'] != sp.get('also')): fail('spine: differs from term/l1/spine_term.json (rerun tools/apply_spine_term.py)')
    marks = {ln.get('spine') for seg in d['script']['segments'] for ln in seg['lines'] if 'spine' in ln}
    if 'look' not in marks: fail('spine: the common look-back words are missing from the look-back script')
    if not marks & {'opening', 'remember'}: warn('spine: no Opening line about the tool of the day (timing was full: see SPINE_TERM_DESIGN.md)')
    ok('spine: tool of the day ' + sp['main'] + ', common look-back present')


def check_all(num, built=True):
    d = load(num)
    for fn in (check_schema, check_identity, check_figures, check_timing, check_slides_links, check_tiers, check_workbook_items, check_words, check_pages, check_next_materials, check_slide_privacy, check_mascot, check_rec, check_spare, check_copy, check_answers, check_beyond, check_kit_contract, check_handoff, check_plural_guard, check_spine):
        try:
            fn(d)
        except Exception as e:
            fail(f'{fn.__name__} crashed: {type(e).__name__}: {e}')
    if built:
        for fn in (check_outputs, check_glyphs, check_key_pdf, check_cover, check_term_check, check_quest, check_foreign):
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
