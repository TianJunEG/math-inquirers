#!/usr/bin/env python3
"""Apply the SPINE (tool of the day + common look-back) to the Term-time Level 1 pipeline (term/l1).  Design: term/l1/SPINE_TERM_DESIGN.md.

    python3 term/l1/tools/apply_spine_term.py                 # DRY RUN (default): prints the diffs it would make, writes nothing
    python3 term/l1/tools/apply_spine_term.py --apply         # writes the files below
    python3 term/l1/tools/apply_spine_term.py --lessons 1,2,7 # only these lessons (tool edits still planned)
    python3 term/l1/tools/apply_spine_term.py --only json     # or: --only tools

Touches ONLY: term/l1/lessons/lNN.json (40 files), term/l1/tools/{b_print,b_guide,b_deck,validate}.py, term/l1/schema/lesson.schema.json,
term/l1/AUTHORING.md.  It never touches out/, books, figs*.py, svg.py or anything else.  Run it in PHASE B, after the diagram-fix agent has finished
(it re-reads every file at run time and refuses to guess: an anchor that is not found is reported as ANCHOR MISSING and that edit is skipped).

IDEMPOTENT: every inserted script line carries the key "spine", every tool edit contains the token SPT/spine_term, the JSON `spine` object is
overwritten from term/l1/spine_term.json.  A second --apply changes 0 files (it prints "0 files would change" in dry-run).

What it does to a lesson file
  1. adds   "spine": {main, also, role, reason[, lean_now][, chip]}              (copied from spine_term.json; the only source of the choice)
  2. adds   Opening SAY + DO (or, if the opening is full, the same two lines at the start of Remember), and a Talk ASK (or a NOTE), all marked "spine"
  3. replaces the text of the look-back SAY and WORK lines with the common look-back words, and the s-look speaker note
  4. Lesson 1 only: a tutor_prep line about the Toolbox card
  Timing is tested with tools/common.py exactly as validate.py does (each part fits, scripted need <= 86 min, slow class <= 90 min); the richest
  variant that fits is chosen (see VARIANTS); the part minutes are NEVER changed.  A lesson where no variant fits is reported "NEEDS HUMAN" and gets only the
  spine object plus the look-back text.
"""
import argparse, copy, difflib, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
L1 = os.path.dirname(HERE)
ROOT = os.path.dirname(os.path.dirname(L1))
sys.path.insert(0, HERE)
import common as C  # noqa: E402

TERM = json.load(open(os.path.join(L1, 'spine_term.json'), encoding='utf-8'))
SPINE = json.load(open(os.path.join(ROOT, 'levels', 'spine.json'), encoding='utf-8'))
BAND = TERM['band']
TOOL = {t['id']: t for t in SPINE['tools']}
MARK = 'spine'

# ---------------------------------------------------------------------------------------------- JSON helpers

def dump_like(raw, d):
    """Re-dump d in the file's own style (indent 1 or 2, trailing newline, \\u00ad soft hyphens as written)."""
    m = re.search(r'\n( +)"', raw)
    ind = len(m.group(1)) if m else 2
    out = json.dumps(d, indent=ind, ensure_ascii=False)
    if '\\u00ad' in raw:
        out = out.replace('\xad', '\\u00ad')
    return out + ('\n' if raw.endswith('\n') else '')


def segment(d, part):
    return next(s for s in d['script']['segments'] if s['part'] == part)


def strip_spine_lines(d):
    """Remove the lines this tool inserted earlier (marked "spine") except the rewritten look-back lines, which are edited in place."""
    for seg in d['script']['segments']:
        seg['lines'] = [ln for ln in seg['lines'] if MARK not in ln or ln[MARK] == 'look']


def line(k, text, **kw):
    ln = {'k': k, 'text': text}
    ln.update(kw)
    ln[MARK] = kw.get(MARK, '1')
    return ln


def fill(s, t):
    return s.replace('{name}', t['name']).replace('{def}', t['def'][BAND])

# ---------------------------------------------------------------------------------------------- one lesson

def spine_obj(n):
    r = TERM['lessons'][str(n)]
    o = {'main': r['main'], 'also': list(r['also']), 'role': r['role'], 'reason': r['reason']}
    if r.get('lean_now'):
        o['lean_now'] = list(r['lean_now'])
    if n in TERM.get('chip_compact_lessons', []):
        o['chip'] = 'compact'
    return o


def look_text(d):
    """Replace the look-back SAY and WORK words and the s-look note. Returns a list of what changed."""
    seg = segment(d, 'look')
    said = False
    say, do = TERM['look_back']['say'], TERM['look_back']['do']
    for ln in seg['lines']:
        if ln['k'] == 'SAY' and (MARK in ln or ln['text'].startswith('Look-back.')):
            ln['text'] = say; ln[MARK] = 'look'; said = True
        elif ln['k'] == 'WORK' and (MARK in ln or ln['text'].startswith('Children fill in the look-back box')):
            ln['text'] = do; ln[MARK] = 'look'
    notes = []
    for s in d['slides']:
        if s['kind'] == 'lookback':
            old = s['note']
            new = re.sub(r'Children tick or write the look-back box on page 5\.',
                         'Children pick one problem from today and fill in the look-back box on page 5: three questions, the Tool I used row, and the stuck and pass boxes.', old)
            new = re.sub(r'\s*The Next time I will try row is optional;[^.]*\.', '', new)
            new = re.sub(r'\s*At the start of the next lesson you may say[^.]*\.', '', new)
            if new != old:
                s['note'] = new; notes.append('note')
            elif 'three questions, the Tool I used row' not in old:
                notes.append('NOTE ANCHOR MISSING')
    return said, notes


def insert_after_last(seg, kinds, new_lines, before_kinds=('NOTE', 'STUCK')):
    """Insert after the last line of `kinds`; if none, after the first SLIDE/REC pair."""
    idx = None
    for i, ln in enumerate(seg['lines']):
        if ln['k'] in kinds and not ln.get('optional'):
            idx = i
    if idx is None:
        idx = 0
    seg['lines'][idx + 1:idx + 1] = new_lines


def fits(d):
    """Same tests as validate.check_timing: every part fits, scripted need <= 86 min, slow class <= 90 min. Returns (ok, why, used, slow)."""
    segs = C.segment_timeline(d)
    used = sum(s['used'] for s in segs)
    slow = sum(C.slow_used(s) for s in segs)
    for s in segs:
        if s['used'] > s['alloc']:
            return False, f"{s['part']} needs {C.mmss(s['used'])} of {C.mmss(s['alloc'])}", used, slow
    if used > 86 * 60:
        return False, f'scripted need {C.mmss(used)} over 86:00', used, slow
    if slow > 90 * 60:
        return False, f'slow class {C.mmss(slow)} over 90:00', used, slow
    return True, '', used, slow


def warns(d):
    """The timing warnings validate.check_timing would print: {(part, tag)} with tag slow (slow class over the part), loose (<70%), tight (>97%)."""
    out = set()
    for s in C.segment_timeline(d):
        u, a, sl = s['used'], s['alloc'], C.slow_used(s)
        if s['part'] == 'flex': continue
        if u > a: continue
        if sl > a: out.add((s['part'], 'slow'))
        elif u < 0.70 * a: out.add((s['part'], 'loose'))
        elif u > 0.97 * a: out.add((s['part'], 'tight'))
    return out


def tune_look(d):
    """Give the children the time the longer look-back needs: WORK seconds up to the most that keeps the slow class inside the part (never below the lesson's own value, at most 120 s)."""
    seg = segment(d, 'look')
    p = C.part_map(d)['look']
    alloc = (p['end'] - p['start']) * 60.0
    others = sum(C.slow_used({'lines': [(0, C.line_seconds(d, 'look', ln), ln)]}) for ln in seg['lines'] if ln['k'] != 'WORK')
    for ln in seg['lines']:
        if ln['k'] == 'WORK' and ln.get(MARK) == 'look':
            calc = int((alloc - others) / 1.2 / 5) * 5
            ln['s'] = max(ln['s'], min(120, calc))


VARIANTS = ['say+do, ask', 'say+do, note', 'say only, note', 'notes only']


def build_variant(d, n, variant, prefer='opening'):
    """Return a deep copy of d with the spine script lines of the given variant (and the look-back text) applied."""
    d2 = copy.deepcopy(d)
    row = TERM['lessons'][str(n)]
    choose = row['main'] == 'choose'
    t = None if choose else dict(TOOL[row['main']])
    S = TERM['script']
    say = S['choose_say'] if choose else fill(S['opening_say'], t)
    do = S['choose_do'] if choose else S['opening_do']
    ask = S['choose_note'] if choose else fill(S['talk_ask'], t)
    note_t = S['choose_note'] if choose else S['talk_note']
    look_text(d2)
    tune_look(d2)
    # --- opening (or remember when the opening is full)
    place = 'opening'
    if variant in VARIANTS[:3]:
        lines = [line('SAY', say, **{MARK: 'opening'})] + ([line('DO', do, s=4, **{MARK: 'opening'})] if variant != 'say only, note' else [])
        seg = segment(d2, 'opening')
        insert_after_last(seg, ('SAY', 'ASK', 'READ'), lines)
        ok, _, _, _ = fits(d2)
        if not ok or prefer == 'remember':   # the start of Remember (after its SLIDE and REC lines)
            seg['lines'] = [ln for ln in seg['lines'] if MARK not in ln or ln[MARK] == 'look']
            rem = segment(d2, 'remember')
            pos = 0
            for i, ln in enumerate(rem['lines']):
                if ln['k'] in ('SLIDE', 'REC'):
                    pos = i + 1
                else:
                    break
            for ln in lines:
                ln[MARK] = 'remember'
            rem['lines'][pos:pos] = lines
            place = 'remember'
    if variant == 'notes only':
        insert_after_last(segment(d2, 'opening'), ('SAY', 'ASK', 'READ'), [line('NOTE', 'Say: ' + say + ' (no time modelled: the opening is full).', **{MARK: 'opening'})])
    # --- tool note for Lesson 1: the Toolbox card
    if n == 1:
        segment(d2, 'opening')['lines'].append(line('NOTE', S['kit_note'], **{MARK: 'opening'}))
    # --- talk
    tk = segment(d2, 'talk')
    if variant == 'say+do, ask' and not choose:
        new = [line('ASK', ask, resp=10, **{MARK: 'talk'}), line('NOTE', S['talk_note'], **{MARK: 'talk'})]
    else:
        new = [line('NOTE', note_t if choose else 'Ask the group where they used ' + t['name'] + ' today (about 20 seconds, no time modelled). ' + S['talk_note'], **{MARK: 'talk'})]
    last = max([i for i, ln in enumerate(tk['lines']) if ln['k'] not in ('NOTE', 'STUCK')] or [0])
    tk['lines'][last + 1:last + 1] = new
    return d2, place


def plan_lesson(n):
    """(path, old_raw, new_raw, report) for one lesson, or (path, raw, raw, report) with a reason if it cannot be done."""
    path = os.path.join(L1, 'lessons', f'l{n:02d}.json')
    raw = open(path, encoding='utf-8').read()
    d = json.loads(raw)
    if dump_like(raw, d) != raw:
        return path, raw, raw, {'n': n, 'status': 'SKIPPED: the file is not re-dumpable byte for byte (format changed); fix by hand'}
    strip_spine_lines(d)
    base_ok, base_why, u0, s0 = fits(d)
    w0 = warns(d)
    rep = {'n': n, 'baseline_ok': base_ok}
    cands = []
    for v in VARIANTS:
        for pref in (('opening', 'remember') if v in VARIANTS[:3] else ('opening',)):
            d2, place = build_variant(d, n, v, pref)
            ok, why, u, sl = fits(d2)
            if not ok:
                rep.setdefault('tried', []).append(f'{v}/{pref}: {why}'); continue
            new_w = warns(d2) - w0
            cands.append((VARIANTS.index(v), len(new_w), v, d2, place, u, sl, new_w))
    if cands:
        best = min(cands, key=lambda c: (c[0], c[1]))      # the richest variant that fits; for the same variant the placement with the fewest new warnings
        _, _, v, d2, place, u, sl, new_w = best
        rep['new_warns'] = sorted(f'{a}:{b}' for a, b in new_w)
    else:
        d2, _ = build_variant(d, n, 'notes only')
        v, place, u, sl = 'NEEDS HUMAN', '-', fits(d2)[2], fits(d2)[3]
    d2['spine'] = spine_obj(n)
    d3 = {}
    for k, val in d2.items():              # place `spine` right after `skill`
        if k == 'spine':
            continue
        d3[k] = val
        if k == 'skill':
            d3['spine'] = d2['spine']
    if 'spine' not in d3:
        d3['spine'] = d2['spine']
    if n == 1:
        tp = d3['tutor_prep']
        item = 'Toolbox card: print the A5 card for ages 6-8 (outputs/kit/Math_Inquirers_Toolbox_Card_A_6-8_PRINT_BW.pdf), one for each child, or send the colour PDF (..._SCREEN_colour.pdf) with the welcome message. Children use it from Lesson 1.'
        tp[:] = [x for x in tp if not x.startswith('Toolbox card:')] + [item]
    new = dump_like(raw, d3)
    rep.update({'variant': v, 'place': place, 'used_before': round(u0 / 60, 2), 'used_after': round(u / 60, 2), 'slow_before': round(s0 / 60, 2), 'slow_after': round(sl / 60, 2)})
    rep['status'] = 'changed' if new != raw else 'unchanged'
    return path, raw, new, rep

# ---------------------------------------------------------------------------------------------- tool edits (text anchors, no line numbers)

def TE(path, marker, old, new):
    return {'path': os.path.join(L1, 'tools', path) if not path.startswith('/') else path, 'marker': marker, 'old': old, 'new': new}

TOOL_EDITS = [
    # ---- b_print.py (workbook, home sheet)
    TE('b_print.py', 'import spine_term as SPT', "import svg\n\nWB_CSS", "import svg\nimport spine_term as SPT      # tool of the day + common look-back (term/l1/SPINE_TERM_DESIGN.md)\n\nWB_CSS"),
    TE('b_print.py', 'SPT.wb_chip', "+ head[i:] + f'</div>{img}</div>'", "+ head[i:] + SPT.wb_chip(d, (d.get('spine') or {}).get('chip') == 'compact') + f'</div>{img}</div>'"),
    TE('b_print.py', 'SPT.wb_lookback', "    if wb(d, 'exit_page', False):      # opt-in", "    look = SPT.wb_lookback(d) or look      # spine: the common look-back box replaces the old one when the lesson has a `spine` object\n    if wb(d, 'exit_page', False):      # opt-in"),
    TE('b_print.py', 'SPT.home_line', '{E(wb(d, "home_hint", "Use real things or draw it."))} A grown-up may read', '{E(wb(d, "home_hint", "Use real things or draw it."))} {E(SPT.home_line(d))} A grown-up may read'),
    # ---- b_guide.py (tutor guide)
    TE('b_guide.py', 'import spine_term as SPT', "import svg\n\nCSS", "import svg\nimport spine_term as SPT\n\nCSS"),
    TE('b_guide.py', 'SPT.guide_row', "    for a, b in rows: H.append(f'<tr><th style=\"width:110px\">{a}</th><td>{b}</td></tr>')", "    _sr = SPT.guide_row(d)\n    if _sr: rows.insert(1, _sr)      # spine: Tool of the day row\n    for a, b in rows: H.append(f'<tr><th style=\"width:110px\">{a}</th><td>{b}</td></tr>')"),
    TE('b_guide.py', 'SPT.guide_lookback', "A child who ticks still stuck gets a check-in in the open session next lesson.</div>')\n", "A child who ticks still stuck gets a check-in in the open session next lesson.</div>')\n    if SPT.row(d): H[-1] = f'<h3>Look-back ({rng(\"look\")})</h3><div class=\"q\">{SPT.guide_lookback(d)}</div>'      # spine: the three common prompts\n"),
    # ---- b_deck.py (slides)
    TE('b_deck.py', 'import spine_term as SPT', "import svg\n\nBF = ", "import svg\nimport spine_term as SPT\n\nBF = "),
    TE('b_deck.py', 'SPT.deck_lookback', "def lookback(d):\n    lb = d['look_back']\n", "def lookback(d):\n    _sp = SPT.deck_lookback(d, NAVY, TEAL, MUTED, CARD, chip)      # spine: three common prompts, Tool I used row, stuck and pass\n    if _sp: return _sp\n    lb = d['look_back']\n"),
    TE('b_deck.py', 'SPT.deck_chip', "for b in s['blocks'] if b['t'] == 'card'))\n        style = ", "for b in s['blocks'] if b['t'] == 'card') + SPT.deck_chip(d))      # spine: TODAY'S TOOL chip\n        style = "),
    # ---- validate.py
    TE('validate.py', 'def check_spine', "def check_all(num, built=True):", '''def check_spine(d):
    """A lesson with a `spine` object: valid tool ids, at most 2 'also', the same row as spine_term.json, the Opening and look-back words present."""
    sp = d.get('spine')
    if not sp: return
    import spine_term as SPT
    ids = {t['id'] for t in SPT.TOOLS}
    tr = SPT._TERM['lessons'].get(str(d['lesson']))
    if sp.get('main') not in ids | {'choose'}: fail(f"spine: unknown main tool {sp.get('main')!r}")
    if any(a not in ids for a in sp.get('also', [])) or len(sp.get('also', [])) > 2 or sp.get('main') in sp.get('also', []): fail('spine: also must be 0-2 other tool ids')
    if tr and (tr['main'] != sp.get('main') or tr['also'] != sp.get('also')): fail('spine: differs from term/l1/spine_term.json (rerun tools/apply_spine_term.py)')
    marks = {ln.get('spine') for seg in d['script']['segments'] for ln in seg['lines'] if 'spine' in ln}
    if 'look' not in marks: fail('spine: the common look-back words are missing from the look-back script')
    if not marks & {'opening', 'remember'}: warn('spine: no Opening line about the tool of the day (timing was full: see SPINE_TERM_DESIGN.md)')
    ok('spine: tool of the day ' + sp['main'] + ', common look-back present')


def check_all(num, built=True):'''),
    TE('validate.py', 'check_spine)', "check_handoff, check_plural_guard):", "check_handoff, check_plural_guard, check_spine):"),
]

AUTH_MARK = '## Spine: tool of the day and common look-back'
AUTH_TEXT = f'''

{AUTH_MARK}

Every lesson file carries a `spine` object (`main`, `also`, `role`, `reason`; copied from `term/l1/spine_term.json` by `tools/apply_spine_term.py`, never edit it by hand). The workbook shows a tool chip on page 1 and the common look-back box on the last page, the guide has a Tool of the day row and the three look-back prompts, the deck shows a TODAY'S TOOL chip on the title slide and the common look-back slide. Script lines that the tool adds carry the key `"spine"`; leave them where they are (the timing check includes them). Wording of tool names and prompts: `levels/spine.json` only. Lessons 10, 20, 30 and 40 (and 39) are choose-the-tool lessons: `main` is `choose`. Do not call a method a "tool" in lesson text (Lesson 7 does: see `SPINE_TERM_DESIGN.md`). A new lesson needs a row in `spine_term.json` first.
'''

SCHEMA_PATH = os.path.join(L1, 'schema', 'lesson.schema.json')
SCHEMA_PROP = {'type': 'object', 'required': ['main'], 'properties': {'main': {'type': 'string'}, 'also': {'type': 'array', 'items': {'type': 'string'}, 'maxItems': 2},
               'role': {'type': 'string', 'enum': ['I', 'P', 'A', 'C']}, 'reason': {'type': 'string'}, 'lean_now': {'type': 'array', 'items': {'type': 'string'}}, 'chip': {'type': 'string', 'enum': ['compact']}}}


def plan_tools():
    """{path: (old_text, new_text, [report lines])}"""
    out = {}
    for e in TOOL_EDITS:
        p = e['path']
        if p not in out:
            t = open(p, encoding='utf-8').read()
            out[p] = [t, t, []]
        orig, cur, rep = out[p]
        if e['marker'] in cur:
            rep.append(f"already applied: {e['marker']!r}")
        elif cur.count(e['old']) != 1:
            rep.append(f"ANCHOR MISSING or not unique ({cur.count(e['old'])}x): {e['old'][:70]!r}")
        else:
            cur = cur.replace(e['old'], e['new']); rep.append(f"edit: {e['marker']!r}")
        out[p] = [orig, cur, rep]
    raw = open(SCHEMA_PATH, encoding='utf-8').read()
    sc = json.loads(raw)
    if dump_like(raw, sc) != raw:
        out[SCHEMA_PATH] = (raw, raw, ['schema NOT re-dumpable: add the "spine" property by hand'])
    else:
        sc2 = copy.deepcopy(sc)
        sc2['properties']['spine'] = SCHEMA_PROP
        out[SCHEMA_PATH] = (raw, dump_like(raw, sc2), ['schema: spine property'])
    ap = os.path.join(L1, 'AUTHORING.md')
    a = open(ap, encoding='utf-8').read()
    out[ap] = (a, a if AUTH_MARK in a else a.rstrip('\n') + '\n' + AUTH_TEXT, ['authoring note'])
    return {k: tuple(v) for k, v in out.items()}

# ---------------------------------------------------------------------------------------------- main

def udiff(path, old, new, n=1):
    rel = os.path.relpath(path, ROOT)
    return ''.join(f'{l}\n' for l in difflib.unified_diff(old.splitlines(), new.splitlines(), 'a/' + rel, 'b/' + rel, lineterm='', n=n))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--apply', action='store_true', help='write the files (default: dry run, nothing is written)')
    ap.add_argument('--lessons', default='', help='comma list, default all 40')
    ap.add_argument('--only', choices=['json', 'tools'], default='')
    ap.add_argument('--diff-context', type=int, default=1)
    ap.add_argument('--quiet', action='store_true', help='summary only, no diffs')
    a = ap.parse_args()
    nums = [int(x) for x in a.lessons.split(',') if x] or list(range(1, 41))
    changed = 0
    print(('APPLY' if a.apply else 'DRY RUN (nothing is written)') + f': {len(nums)} lessons' + ('' if a.only != 'tools' else ' (skipped)'))
    rows = []
    if a.only != 'tools':
        for n in nums:
            path, old, new, rep = plan_lesson(n)
            rows.append(rep)
            if new != old:
                changed += 1
                if not a.quiet: print(udiff(path, old, new, a.diff_context))
                if a.apply: open(path, 'w', encoding='utf-8').write(new)
    if a.only != 'json':
        for p, (old, new, rep) in plan_tools().items():
            print(f'# {os.path.relpath(p, ROOT)}: ' + '; '.join(rep))
            if new != old:
                changed += 1
                if not a.quiet: print(udiff(p, old, new, a.diff_context))
                if a.apply: open(p, 'w', encoding='utf-8').write(new)
    print('\nlesson   status      variant           placed     used min (before>after)  slow min (before>after)')
    for r in rows:
        print(f"L{r['n']:<6} {r.get('status', '?')[:10]:<11} {r.get('variant', '-'):<17} {r.get('place', '-'):<10} {r.get('used_before', '-')}>{r.get('used_after', '-')}".ljust(76) + f"{r.get('slow_before', '-')}>{r.get('slow_after', '-')}" + ('   NEW WARNS ' + ','.join(r['new_warns']) if r.get('new_warns') else '') + ('   tried: ' + '; '.join(r['tried']) if r.get('tried') else ''))
    need = [r['n'] for r in rows if r.get('variant') == 'NEEDS HUMAN' or str(r.get('status', '')).startswith('SKIPPED')]
    if need: print('\nNEEDS HUMAN (timing too full or format changed):', need)
    print(f'\n{changed} files {"changed" if a.apply else "would change"}' + ('' if a.apply else '   (run with --apply in Phase B)'))


if __name__ == '__main__':
    main()
