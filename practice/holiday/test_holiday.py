#!/usr/bin/env python3
"""Browser test of a built holiday practice lesson (Playwright/Chromium) and screenshots.  Shared by every level.

    python3 practice/holiday/build_holiday.py p1 1 && python3 practice/holiday/test_holiday.py p1 1

1. re-reads the BUILT data file and recomputes every answer with the lesson's independent checkers again (the output file is checked, not the build);
2. opens the questions in REVERSE order in a real browser, types the correct answer into each (several accepted wordings for text answers), submits (with the
   'no answer' confirm only if a marked question is blank), and expects every auto-marked question right, every self-check shown as 'check yourself', and a worked
   solution for every question (and the correct-drawing figure for paper-only items);
3. a second child answers wrongly, skips some, reloads (answers survive), submits: wrong / no answer markers, solutions for skipped questions; solutions are
   hidden before submit and again after 'Change my answers'; wrong text wordings are marked wrong;
4. every variant family: forces each combination of the variables, checks the question shown equals the template and the ORACLE's answer is accepted;
   Shared-matcher fixes (week 2 audit) are covered here too: unit and notation forms, equal fractions (equiv_frac), algebra rules as polynomials (poly), number words only when
   declared, short distinct question buttons, label+box groups that never split at 390 and 360 px, solution figures at least 11 px and not clipped at 360 px, the typed explanation
   in the submission payload (trimmed, at most 500 characters) when sending is on, and the tutor-report marking_mode of every self-check item.
5. screenshots at 390 px and 900 px, light and dark, into practice/holiday/<key>/<NN>/proof/; checks there is no horizontal scroll, that every figure
   text is at least 11 px on screen at 390 px, and that no figure text is clipped.
"""
import functools, http.server, itertools, json, os, re, sys, threading
os.environ.setdefault('PLAYWRIGHT_BROWSERS_PATH', '/opt/pw-browsers')
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_holiday as H                      # noqa: E402
B = H.B
from playwright.sync_api import sync_playwright   # noqa: E402

key = sys.argv[1] if len(sys.argv) > 1 else 'p1'
n = int(sys.argv[2]) if len(sys.argv) > 2 else 1
lk = f'{key}l{n:02d}'
BASE = os.path.join(HERE, key, f'{n:02d}')
DIST = os.path.join(BASE, 'dist')
PROOF = os.path.join(BASE, 'proof'); os.makedirs(PROOF, exist_ok=True)
data = json.load(open(os.path.join(DIST, 'data', lk + '.json'), encoding='utf-8'))
items = data['items']
lesson = H.load_lesson(key, n)
src = {s['id']: s for s in lesson.ITEMS}
fails = []


def fail(msg):
    fails.append(msg); print('FAIL', msg)


# ---- 1. the built data against fresh independent checks
nchk = 0
for it in items:
    s = src[it['id']]
    chk = s.get('check')
    if chk is None:
        if not (s['type'] == 'selfcheck' and s.get('open')):
            fail(f'{it["id"]}: no checker')
        continue
    got = chk(); nchk += 1
    t = it['type']
    if t == 'fields':
        ok = [int(x) for x in got] == [f['answer'] for f in it['fields']]
    elif t == 'number':
        ok = int(got) == it['answer']
    elif t == 'choice':
        ok = got == it['answer']
    elif t == 'set':
        ok = (list(map(int, got)) == it['answer']) if it['ordered'] else sorted(map(int, got)) == sorted(it['answer'])
    elif t == 'text':
        ok = (tuple(got) == tuple(s['rule']) and it['answer'] == H.hlib.rule_accepts(*got)) if s.get('rule') else str(got).strip().lower() in [str(x).strip().lower() for x in it['answer']]
    else:
        ok = s.get('facts') is None or got == s['facts']
    if not ok:
        fail(f'{it["id"]}: built data differs from the independent check {got}')
print(f'1. {len(items)} built items; {nchk} re-checked against the independent checkers')

# ---- 1b. the build-time twins in hlib (poly_parse, frac_list_ok) agree with the shared matcher in practice/submit/mark.js on a battery of strings
import subprocess
_RULES = [('4n+12', ['(n+3)\u00d74', '4n+12', '4(n+3)', '4*(n+3)', '4x(n+3)', '(n+3)4', '12+4n', '(8n+24)\u00f72', '4n+16\u22124', '(n+3)\u00d74 = 4n+12', 'OUT = 4(n+3)', 'out=4n+12', '4n+12=OUT', '4n+12.', '  4 n + 12 ', '2(2n+6)',
                      '4n-12', 'n+3\u00d74', '(n+3)+4', '4n+3', '4(n+4)', '(n+3)\u00d75', '3n+12', '7n', '4n', '12', 'n+3 = 4n+12', '4n+12=', 'OUT', '4n+12 n', '4n 12', '4n\u00b2+12', 'fourn+12', '4n+12/0', '(4n+12', 'n^9', '(n+1)'*12]),
           ('n+3', ['(2n+6)\u00f72', '(2n+6)/2', '2n+6\u00f72', 'n+6', '3+n', 'n+3', '(n+3)']), ('0.5n', ['n/2', 'n\u00f72', '0.5n', '.5n', '-0.5n', '2n/4', 'n/3']), ('n^2+2n+1', ['(n+1)\u00b2', '(n+1)^2', 'n\u00d7n+2n+1', 'n\u00b2+1', 'n^2+2n+1', '(n+1)(n+1)'])]
_FRACS = [('7/12, 2/3, 5/6', ['7/12, 8/12, 10/12', '7/12 8/12 10/12', '14/24,2/3,5/6', '8/12, 7/12, 10/12', '7/12, 8/12', '7/12, 8/12, 10/12, 1', '7/0, 8/12, 10/12', '0.5, 2/3, 5/6', '7/12, 2/3, 5/6.', '7 out of 12, 2 out of 3, 5 out of 6', '7 out of 12, 8/12, 10/12', '1 out of 4']),
          ('1/4 < 1/2 < 3/4', ['2/8 < 4/8 < 6/8', '2/8 > 4/8 > 6/8', '2/8, 4/8, 6/8']), ('1 1/2', ['3/2', '6/4', '11/2', '1 1/2', '1 2/4'])]
_cases = [dict(rec=dict(marking_mode='auto', type='text', key=[k], poly='n'), v=v, py=H.hlib.poly_ok([k], v, 'n')) for k, vs in _RULES for v in vs]
_cases += [dict(rec=dict(marking_mode='auto', type='text', key=[k], equiv_frac=True), v=v, py=H.hlib.frac_list_ok([k], v)) for k, vs in _FRACS for v in vs]
_js = "const M=require(process.argv[1]);const c=JSON.parse(require('fs').readFileSync(0,'utf8'));console.log(JSON.stringify(c.map(x=>M.mark(x.rec,x.v).mark==='right')))"
_out = json.loads(subprocess.run(['node', '-e', _js, os.path.join(H.ROOT, 'practice', 'submit', 'mark.js')], input=json.dumps(_cases), capture_output=True, text=True, check=True).stdout)
for _c, _o in zip(_cases, _out):
    # mark.js also accepts the printed forms exactly; the python twin only the polynomial / fraction reading, so compare only where the python one says no and the string is not the key itself
    if _c['py'] != _o and not (not _c['py'] and _o and _c['v'].strip() in _c['rec']['key']): fail(f'hlib and mark.js disagree on {_c["rec"].get("poly") and "rule" or "fractions"} {_c["rec"]["key"]} typed {_c["v"]!r}: python {_c["py"]}, mark.js {_o}')
print(f'1b. hlib (build time) and mark.js (browser and server) agree on {len(_cases)} typed rules and fraction lists')


# ---- 1c. the builder sets clock automatically (stem or frame says o'clock and the key is a bare hour), honours clock=False, and passes dollars_ok / accept_by to the data and to the server keys
def _mk(**kw):
    d = dict(id='Z1', tier='core', no='1', q='q', hint='h', steps=['s'], skill='k', src=['x'], type='number', answer=3, check=lambda: 3, strand='t')
    d.update(kw); return d
def _flags(**kw):
    o, _ = H.make_item(_mk(**kw)); return o
if not _flags(q="It is 8 o'clock. What time is it 7 hours later?").get('clock'): fail("clock not set automatically for a stem with o'clock and a bare hour")
if not _flags(q="It is 8 o\u2019clock. What time?").get('clock'): fail("clock not set for a curly apostrophe")
if _flags(q='What is 1 + 2?').get('clock'): fail('clock set without o\'clock in the stem')
if _flags(q="It is 8 o'clock.", answer=15, check=lambda: 15).get('clock'): fail("clock set for a key that is not a bare hour")
if _flags(q="From 3 o'clock to 8 o'clock is how many hours?", clock=False).get('clock'): fail('clock=False did not switch the automatic setting off')
if not _flags(q='A clock puzzle.', clock=True).get('clock'): fail('clock=True not passed on')
_fo = _flags(type='fields', q='What time?', frame="{f1} o'clock", answer=[3], check=lambda: [3])
if not _fo['fields'][0].get('clock'): fail("a box printed right before o'clock is not a clock box")
_fo = _flags(type='fields', q='What time?', frame='{f1}:{f2}', answer=[3, 30], check=lambda: [3, 30])
if any(f.get('clock') for f in _fo['fields']) or _fo.get('clock'): fail('a h:mm pair of boxes must not be a clock box')
_fo = _flags(type='fields', q='What time?', frame="{f1}:{f2} then {f3} o'clock", answer=[3, 30, 5], check=lambda: [3, 30, 5])
if [bool(f.get('clock')) for f in _fo['fields']] != [False, False, True]: fail('only the box before o\'clock is a clock box: ' + str(_fo['fields']))
if not _flags(dollars_ok=True).get('dollars_ok') or _flags().get('dollars_ok'): fail('dollars_ok default / pass-through')
_ta = dict(type='text', answer=None, accept=['6'], check=lambda: '6')
if not _flags(accept_by=True, **_ta).get('accept_by') or _flags(**_ta).get('accept_by'): fail('accept_by default / pass-through')
# time flag: automatic for hours / minutes labels, time=True for any two boxes, time=False off, paper_note
def _tm(frame, ans=(5, 25), **kw): return _flags(type='fields', q='What time?', frame=frame, answer=list(ans), check=lambda: list(ans), **kw)
def _tflags(o): return [bool(f.get('time')) for f in o['fields']]
for _fr in ('{f1} h {f2} min', '{f1} hours {f2} minutes', '{f1} hr {f2} mins', 'Hours: {f1} Minutes: {f2}', 'The film ends at {f1} h {f2} min.', '{f1} hour {f2} minute'):
    if _tflags(_tm(_fr)) != [True, False]: fail(f'time not set automatically for {_fr!r}')
if _tflags(_tm('{f1}:{f2}')) != [False, False]: fail('h:mm boxes must not get time automatically')
if _tflags(_tm('{f1} h {f2} min', time=False)) != [False, False]: fail('time=False did not switch off')
if _tflags(_tm('{f1}:{f2}', time=True)) != [True, False]: fail('time=True not passed on')
if _tflags(_tm('{f1} cm and {f2} m')) != [False, False]: fail('cm / m boxes must not be a time')
if _tflags(_tm('Add {f1} to {f2} h', ans=(3, 4))) != [False, False]: fail('only a labelled hours + minutes pair is a time')
try: _flags(time=True); fail('time=True on a number item must fail')
except H.Fail: pass
_pn = dict(type='selfcheck', paper=True, open=True, answer=None)
if 'paper_note' in _flags(**_pn) or 'paper_note' in _flags(paper_note='x', **_pn) and _flags(paper_note='x', **_pn)['paper_note'] != 'x': fail('paper_note default / pass-through')
if _flags(paper_note='Measure it with a ruler.', **_pn).get('paper_note') != 'Measure it with a ruler.': fail('paper_note not passed on')
print('1c. the builder sets clock automatically for o\'clock stems with a bare-hour key (not for h:mm boxes), clock=False turns it off, dollars_ok / accept_by are off by default')


class Q(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a): pass

srv = http.server.ThreadingHTTPServer(('127.0.0.1', 0), functools.partial(Q, directory=DIST))
threading.Thread(target=srv.serve_forever, daemon=True).start()
URL = f'http://127.0.0.1:{srv.server_address[1]}/index.html'

WRONG_TEXT = {'add': 'take away 7', 'take away': 'add 7'}


def enter(page, it, wrong=False, alt=0):
    t = it['type']
    if t == 'fields':
        a = [f['answer'] for f in it['fields']]
        if wrong: a = [x + 1 for x in a]
        boxes = page.locator('#ans input[data-f]')
        assert boxes.count() == len(a), (it['id'], boxes.count(), len(a))
        for i, x in enumerate(a): boxes.nth(i).fill(str(x))
    elif t == 'set':
        a = list(it['answer'])
        if wrong: a = a[:-1] + [a[-1] + 1]
        page.locator('#ans input[type=text]').fill(', '.join(map(str, a)))
    elif t == 'number':
        page.locator('#ans input[type=text]').fill(str(it['answer'] + (1 if wrong else 0)))
    elif t == 'choice':
        pick = it['answer'] if not wrong else [o for o in it['options'] if o != it['answer']][0]
        page.locator('#ans label.opt', has_text=re.compile('^' + re.escape(pick) + '$')).click()
    elif t == 'text':
        s = src[it['id']]
        txt = (WRONG_TEXT[s['rule'][0]] if s.get('rule') else 'zzz not it') if wrong else it['answer'][alt % len(it['answer'])]
        page.locator('#ans input[type=text]').fill(txt)
    elif t == 'selfcheck':
        if page.locator('#ans textarea').count():
            page.locator('#ans textarea').fill('my own words')


def dedupe_title(q):
    """The renderer's rule: 'Take-home. Take-home (if ...' shows as 'Take-home (if ...'."""
    m = re.match(r'(.{3,40}?)\.\s+(?=\1(?![A-Za-z0-9]))', q, re.I)
    return q[m.end():] if m else q


def goto(page, i):
    page.locator(f'#nav button[data-i="{i}"]').click()


def idx_of(item_id):
    return [k for k, x in enumerate(items) if x['id'] == item_id][0]


def fresh(br, w=800, h=900, dark=False):
    c = br.new_context(viewport={'width': w, 'height': h}, color_scheme='dark' if dark else 'light')
    p = c.new_page(); p.goto(URL); p.wait_for_selector('#card .q')
    return c, p


def figure_text_check(page, w, mn=11, sel='#card svg text'):
    """Every figure text on screen at least mn px, and none outside its svg."""
    return page.evaluate("""([MIN, SEL]) => {
      const bad = [];
      document.querySelectorAll(SEL).forEach(t => {
        const svg = t.ownerSVGElement, ctm = t.getScreenCTM(); if (!ctm) return;
        const fs = parseFloat(getComputedStyle(t).fontSize) * ctm.a;
        const r = t.getBoundingClientRect(), s = svg.getBoundingClientRect();
        if (fs < MIN) bad.push('small ' + t.textContent + ' ' + fs.toFixed(1));
        if (r.left < s.left - 1 || r.right > s.right + 1 || r.top < s.top - 1 || r.bottom > s.bottom + 1) bad.push('clipped ' + t.textContent);
      });
      return bad;
    }""", [mn, sel])


with sync_playwright() as pw:
    br = pw.chromium.launch()
    errors = []
    N = len(items)
    cls = lambda p, i: p.locator(f'#nav button[data-i="{i}"]').get_attribute('class').split()[-1]
    nself = sum(1 for it in items if it['type'] == 'selfcheck')
    npaper = sum(1 for it in items if it.get('paper'))

    # ---- 2: a child who answers everything, in reverse order
    ctx, page = fresh(br)
    page.on('pageerror', lambda e: errors.append(str(e)))
    page.on('console', lambda m: errors.append(m.text) if m.type == 'error' else None)
    page.reload(); page.wait_for_selector('#card .q')
    for i in reversed(range(N)):
        goto(page, i)
        if page.locator('#card .q').inner_text() != dedupe_title(items[i]['q']): fail(f'{items[i]["id"]}: shown question differs from data')
        if page.locator('#sol').count(): fail(f'{items[i]["id"]}: solution visible before submit')
        if items[i].get('paper'):
            if (items[i].get('paper_note') or 'Do this on paper (or with your own things), then check it against the answer shown on screen.') not in page.locator('#paper').inner_text(): fail(f'{items[i]["id"]}: no paper note')
            if page.locator('#ans textarea').count(): fail(f'{items[i]["id"]}: paper-only item has a text box')
        enter(page, items[i], alt=i)
    page.locator('#submit').click()
    # self-check and paper-only items are never 'unanswered': a child who has answered every marked question is not asked 'Submit anyway?'
    if page.locator('#yes').count() or page.locator('#askbox').count(): fail('"Submit anyway?" shown although every marked question has an answer')
    if page.evaluate("document.activeElement && document.activeElement.id") != 'summary': fail('focus not on the summary after Submit')
    summ = page.locator('#summary').inner_text()
    if f'{N - nself} of {N - nself} marked questions are right' not in summ: fail('summary: ' + summ)
    for i, it in enumerate(items):
        goto(page, i)
        c = cls(page, i)
        if c != ('self' if it['type'] == 'selfcheck' else 'right'): fail(f'{it["id"]}: marker {c}')
        if not page.locator('#sol li').count(): fail(f'{it["id"]}: no worked steps after submit')
        if it.get('sol_svg') and not page.locator('#solfig svg').count(): fail(f'{it["id"]}: no figure of the correct drawing')
        if it.get('paper') and not it.get('sol_svg'): fail(f'{it["id"]}: paper item without a solution figure')
        sol = page.locator('#sol').inner_text()
        if it['type'] in ('fields',) and not all(str(f['answer']) in sol for f in it['fields']): fail(f'{it["id"]}: answer not in solution')
    print(f'2. {N} questions opened in reverse order, all answered, submitted: {N - nself} marked right, {nself} to check yourself ({npaper} paper-only with a figure of the correct drawing), {N} worked solutions shown')
    page.locator('#again').click()
    if page.locator('#sol').count(): fail('solution still visible after "Change my answers"')
    ctx.close()

    # ---- 2b: the same answers typed the way children type them: no spaces after commas, a final full stop, .0, a unit word, a statement with its result
    ctx, page = fresh(br)
    for i, it in enumerate(items):
        t = it['type']
        goto(page, i)
        if t == 'set':
            big = any(abs(x) >= 10000 for x in it['answer'])
            page.locator('#ans input[type=text]').fill(','.join(map(str, it['answer'])) if not big else ', '.join(map(str, it['answer'])))
        elif t == 'number':
            page.locator('#ans input[type=text]').fill(f"{it['answer']}.0")
        elif t == 'fields':
            for k, f in enumerate(it['fields']): page.locator('#ans input[data-f]').nth(k).fill(f"{f.get('pre', '')}{f['answer']}" if k % 2 == 0 else f"{f['answer']}.")
        else:
            enter(page, it, alt=i)
    page.locator('#submit').click()
    if page.locator('#yes').count(): page.locator('#yes').click()
    summ = page.locator('#summary').inner_text()
    if f'{N - nself} of {N - nself} marked questions are right' not in summ: fail('2b (comma without space, 20.0, 6:20, 29.): ' + summ)
    ctx.close()
    print('2b. lists typed with commas and no spaces, whole numbers typed as 20.0 or 29., and clock boxes typed as 6:20 are all marked right')

    # ---- 2c: reading aids: focus, labels, input modes, helper line, footer, noindex, placeholder contrast
    ctx, page = fresh(br)
    act = lambda: page.evaluate("(document.activeElement.className||'') + '|' + (document.activeElement.id||'')")
    page.locator('#nav button[data-i="1"]').click()
    if 'q|' not in act(): fail('focus not on the question after choosing a question: ' + act())
    page.get_by_role('button', name='Skip to next').click()
    if 'q|' not in act(): fail('focus not on the question after Skip: ' + act())
    page.get_by_role('button', name='Give me a hint').click()
    if not act().endswith('|hintbox'): fail('focus not on the hint after Give me a hint: ' + act())
    page.get_by_role('button', name='Hide the hint').click()
    if not act().endswith('|hintbtn'): fail('focus lost after hiding the hint: ' + act())
    if page.locator('a.skip').count() != 1: fail('no skip link')
    page.reload(); page.wait_for_selector('#card .q'); page.keyboard.press('Tab')
    if page.evaluate("document.activeElement.className") != 'skip': fail('the skip link is not the first Tab stop')
    page.keyboard.press('Enter')
    if 'q|' not in act(): fail('the skip link does not move focus to the question')
    labs = []
    for i, it in enumerate(items):
        goto(page, i)
        no = it.get('no')
        lab = page.locator(f'#nav button[data-i="{i}"] b').inner_text()
        labs.append(lab)
        aria = page.locator(f'#nav button[data-i="{i}"]').get_attribute('aria-label')
        if not lab or len(lab) > 14: fail(f'{it["id"]}: nav label {lab!r} is empty or long')
        if lab in ('Investigation', 'Think', 'Go', 'Think harder', 'Go further', 'Start', 'Extra'): fail(f'{it["id"]}: nav label {lab!r} is only a group word (printed {no!r})')
        mm = re.match(r'(\d+\([a-z]\)|[A-Z]\d+)', no or '')
        if mm and mm.group(1) not in lab and not it.get('label'): fail(f'{it["id"]}: nav label {lab!r} lost the printed number {mm.group(1)!r} of {no!r}')
        if re.match(r'Investigation\b', no or '') and not lab.startswith('Inv'): fail(f'{it["id"]}: investigation label {lab!r}')
        if no and no not in aria: fail(f'{it["id"]}: accessible name {aria!r} lacks the full label {no!r}')
        if it['type'] in ('set', 'number', 'fields'):
            mode = page.locator('#ans input').first.get_attribute('inputmode')
            neg = any((x if isinstance(x, int) else 0) < 0 for x in ([f['answer'] for f in it['fields']] if it['type'] == 'fields' else (it['answer'] if it['type'] == 'set' else [it['answer']])))
            if (it['type'] == 'set' or neg) and mode != 'text': fail(f'{it["id"]}: list/negative item has inputmode {mode} (iPhone number pad has no comma or minus)')
            if not (it['type'] == 'set' or neg) and mode != 'numeric': fail(f'{it["id"]}: inputmode {mode}')
            if it['type'] == 'set' and 'Use commas between numbers' not in page.locator('#card').inner_text(): fail(f'{it["id"]}: no "Use commas between numbers" helper')
            for inp in page.locator('#ans input').all():
                if no and no.split(' ')[0] not in (inp.get_attribute('aria-label') or ''): fail(f'{it["id"]}: input label {inp.get_attribute("aria-label")!r} lacks the question number'); break
        if it['type'] == 'choice':
            if page.locator('#ans').evaluate("e => e.tagName") != 'FIELDSET' or not page.locator('#ans legend').inner_text().strip(): fail(f'{it["id"]}: radio group has no fieldset/legend')
    dup = sorted({l for l in labs if labs.count(l) > 1})
    if dup: fail(f'nav labels shared by two questions (the runner must add a/b): {dup}')
    # accessible names: unique, begin with the visible label (label in name, so 'why' / 'Ali' suffixes are in it), visible text readable, glyph at least 12 px, no 'Home' for take-home
    names = [page.locator(f'#nav button[data-i="{i}"]').get_attribute('aria-label') for i in range(N)]
    dn = sorted({x for x in names if names.count(x) > 1})
    if dn: fail(f'accessible names shared by two nav buttons: {dn}')
    for i, (lab, nm) in enumerate(zip(labs, names)):
        if not nm.startswith(lab): fail(f'{items[i]["id"]}: accessible name {nm!r} does not start with the visible label {lab!r}')
        if '?' in lab or lab == 'Home' or re.search(r'\d[a-z]\d', lab): fail(f'{items[i]["id"]}: nav label {lab!r} is cryptic (a number only, with the description in the accessible name)')
    small = page.evaluate("[...document.querySelectorAll('#nav .nb i')].filter(e => parseFloat(getComputedStyle(e).fontSize) < 12).length")
    if small: fail(f'{small} nav status glyphs are under 12 px')
    for i, it in enumerate(items):
        if re.search(r'(?i)^take-home\b', it.get('no') or '') and labs[i][:2] != 'TH': fail(f'{it["id"]}: take-home label {labs[i]!r} should start with TH')
        shown = dedupe_title(it['q'])
        mt = re.match(r'(.{3,40}?)\.\s+\1', shown, re.I)
        if mt: fail(f'{it["id"]}: card title repeats itself: {shown[:60]!r}')
    foot = page.locator('.foot').inner_text()
    if 'nothing is sent anywhere' in foot or 'Your answers stay on this device' not in foot: fail('footer wording (sending off): ' + foot)
    if page.locator('meta[name=robots][content*=noindex]').count() != 1: fail('no noindex meta')
    ctx.close()
    for dark in (False, True):
        ctx, page = fresh(br, 390, 900, dark)
        ti = [k for k, x in enumerate(items) if x['type'] == 'selfcheck' and not x.get('paper')]
        if ti:
            goto(page, ti[0])
            cr = page.evaluate(r"""() => { const t = document.querySelector('#ans textarea'), cs = getComputedStyle(t, '::placeholder');
              const p = s => (s.match(/[\d.]+/g) || []).slice(0, 3).map(Number), lum = c => { const [r, g, b] = c.map(v => { v /= 255; return v <= .03928 ? v / 12.92 : Math.pow((v + .055) / 1.055, 2.4); }); return .2126 * r + .7152 * g + .0722 * b; };
              let bg = null, e = t; while (e && !bg) { const c = getComputedStyle(e).backgroundColor; if (c && !/rgba\(.*, 0\)|transparent/.test(c)) bg = c; e = e.parentElement; }
              const a = lum(p(cs.color)), b = lum(p(bg || 'rgb(255,255,255)')); return (Math.max(a, b) + .05) / (Math.min(a, b) + .05); }""")
            if cr < 4.5: fail(f'placeholder contrast {cr:.2f} (dark={dark}) is below 4.5')
        ctx.close()
    # sending switched on (token present): the footer says so and the 'I checked / I got it / not yet' ticks are visible after submit
    ctx = br.new_context(viewport={'width': 800, 'height': 900})
    page = ctx.new_page()
    posted = []
    def _send(r):
        posted.append(json.loads(r.request.post_data or '{}'))
        r.fulfill(status=200, content_type='application/json', body='{"ok":true,"marks":{}}')
    page.route('**/hol-send/**', _send)
    page.add_init_script("window.MI_SUBMIT={endpoint:'http://127.0.0.1:9/hol-send/x',token:'t'.repeat(40),unit:'hol-test',version:'v1'}")
    page.goto(URL); page.wait_for_selector('#card .q')
    typed_ids = [x['id'] for x in items if x['type'] == 'selfcheck' and not x.get('paper')]
    if typed_ids:       # the typed explanation goes in the payload (trimmed, at most 500 characters); 'answers' still says only '(written)'
        goto(page, idx_of(typed_ids[0])); page.locator('#ans textarea').fill('   ' + 'Because it is so. ' * 40 + '   ')
        if len(typed_ids) > 1: goto(page, idx_of(typed_ids[1])); page.locator('#ans textarea').fill('short note')
    foot = page.locator('.foot').inner_text()
    if 'are sent to your tutor so they can help you' not in foot or 'explanation boxes' not in foot or 'nothing is sent' in foot: fail('footer wording (sending on): ' + foot)
    si = [k for k, x in enumerate(items) if x['type'] == 'selfcheck']
    page.locator('#submit').click()
    if page.locator('#yes').count(): page.locator('#yes').click()
    page.wait_for_timeout(600)
    if not posted: fail('sending on: nothing was posted')
    elif typed_ids:
        pl = posted[-1]; ex = pl.get('explain') or {}
        if set(ex) != set(typed_ids[:2]): fail(f'explain keys {sorted(ex)} != typed {typed_ids[:2]}')
        t0 = ex.get(typed_ids[0], '')
        if not (0 < len(t0) <= 500) or t0 != t0.strip() or not t0.startswith('Because it is so.'): fail(f'explanation not trimmed and capped at 500: {len(t0)} {t0[:30]!r}')
        if len(typed_ids) > 1 and ex.get(typed_ids[1]) != 'short note': fail('short explanation not sent as typed')
        if pl['answers'][typed_ids[0]] != '(written)': fail('answers[...] must stay "(written)"')
        if any(k in pl for k in ('correct', 'marks', 'client_marks')): fail('payload carries a mark')
        if set(pl) - {'v', 'unit', 'unit_version', 'sid', 'rev', 'answers', 'self', 'explain'}: fail('unexpected payload fields ' + str(set(pl)))
        if page.locator('#card').inner_text().count('Because it is so') > 0 and not page.locator('#ans textarea').count(): pass
    if si:
        goto(page, si[0])
        for lbl in ('I checked it', 'I got it', 'Not yet'):
            if not page.get_by_role('button', name=lbl).count(): fail(f'sending on: no "{lbl}" tick')
    ctx.close()
    print('2c. focus moves to the question / hint / confirm / summary; skip link; question numbers on the buttons; fieldset legends; input modes; helper line; footer for both modes; noindex; placeholder contrast')

    # ---- 2d: shared-runner fixes of the week 3 audits, on a small synthetic lesson (so every level gets the same checks): doubled titles, the picture of a variant, unit tails,
    #          natural wordings (with negatives), nav names; then the go-live switch (footer + ticks with an endpoint set), all in a scratch copy of this lesson's dist
    import shutil, tempfile
    scratch = tempfile.mkdtemp(prefix='hol-syn-', dir='/dev/shm' if os.path.isdir('/dev/shm') else None)
    sd = os.path.join(scratch, 'dist'); shutil.copytree(DIST, sd)
    FIG = '<svg viewBox="0 0 120 40" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="x"><text x="5" y="25" font-size="14">PIC {n}</text></svg>'
    def syn(i, tier, q, typ, ans, **kw):
        d = dict(id=i, tier=tier, type=typ, no=i, q=q, hint='Think.', steps=['Because.'], slips=[], tags={}, src=[], marking_mode='auto', answer=ans)
        d.update(kw); return d
    synitems = [
        syn('S1', 'core', 'S1. Take-home. Take-home (if you have time): do it.', 'number', 27),
        syn('S2', 'core', 'S2. Make up your own. Make up your own: a riddle.', 'number', 35),
        syn('S3', 'core', 'S3. How many litres?', 'number', 27),
        syn('S4', 'core', 'S4. How many cents change?', 'number', 35),
        syn('S5', 'core', 'S5. No unit please.', 'number', 35, unit=False),
        syn('S6', 'core', 'S6. Angle AOC?', 'number', 90),
        syn('S7', 'core', 'S7. Which day?', 'text', ['Wednesday', 'Wed']),
        syn('S8', 'core', 'S8. Which shapes?', 'text', ['A, B, D']),
        syn('S9', 'core', 'S9. What fraction?', 'text', ['1/4'], equiv_frac=True),
        syn('S10', 'core', 'S10. Compare.', 'text', ['a = b']),
        syn('S11', 'core', 'S11. Day, no lead-in.', 'text', ['Wednesday'], accept_prefix=False),
        syn('S12', 'core', 'S12. Variant with picture.', 'number', 7, svg='<svg viewBox="0 0 120 40" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="x"><text x="5" y="25" font-size="14">OLD 7</text></svg>',
            tpl=dict(vars=dict(n=[4, 5]), q='There are {n} sheep.', hint='Count.', answer='n', steps=['{n}.'], fig=FIG)),
        syn('S13', 'core', 'S13. Variant without a picture.', 'number', 7, svg='<svg viewBox="0 0 120 40" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="x"><text x="5" y="25" font-size="14">OLD 7</text></svg>',
            tpl=dict(vars=dict(n=[4, 5]), q='There are {n} cows.', hint='Count.', answer='n', steps=['{n}.'], paper=True)),
        syn('S14', 'invest', 'Inv 8c4 yes?', 'number', 1, label='Inv 8c4 yes?'), syn('S15', 'invest', 'Inv 8c2', 'number', 1, label='Inv 8c2 yes?'),
        syn('S16', 'challenge', 'G5', 'number', 1, label='G5 any no.?'), syn('S17', 'core', 'S17. A why.', 'selfcheck', None, label='2(b) why', open=True, steps=['x']),
        syn('S18', 'core', 'S18. A why.', 'selfcheck', None, label='2(b) Ali', open=True, steps=['x']),
        syn('S19', 'core', "S19. It is 8 o'clock. What time 7 hours later?", 'number', 3, clock=True),
        syn('S20', 'core', 'S20. A plain number 3, no clock flag.', 'number', 3),
        syn('S21', 'core', 'S21. Sides of the square?', 'text', ['6'], accept_by=True),
        syn('S22', 'core', 'S22. How many cents cheaper?', 'number', 48, dollars_ok=True),
        syn('S23', 'core', 'S23. Type the coded word.', 'text', ['CAT']),
        syn('S24', 'core', 'S24. Which letter?', 'text', ['E']),
        syn('S25', 'core', 'S25. Which shapes?', 'text', ['A, C, E, F']),
        syn('S26', 'core', 'S26. Angle sum rule.', 'text', ['(n-2)x180'], poly='n'),
        syn('S27', 'core', 'S27. A plain number 1, no unit.', 'number', 1, unit=False),
        syn('S28', 'core', 'S28. How long is the film?', 'fields', [5, 25], frame='{f1} h {f2} min', fields=[dict(id='f1', answer=5, time=True), dict(id='f2', answer=25)]),
    ]
    for it_ in synitems:
        if it_['type'] == 'selfcheck': it_.update(paper=False, paper_only=False, marking_mode='self', open=True); it_.pop('answer')
    synitems[0]['no'] = 'Take-home'; synitems[1]['no'] = 'Make up your own'
    synitems[0]['q'] = 'Take-home. Take-home (if you have time): do it.'; synitems[1]['q'] = 'Make up your own. Make up your own: a riddle.'
    synitems[13]['no'] = 'Investigation 8(c)4'; synitems[14]['no'] = 'Investigation 8(c)2'; synitems[15]['no'] = 'Go further 5'
    synitems[16]['no'] = '2(b)'; synitems[17]['no'] = '2(b)'
    d2 = json.loads(json.dumps(data)); d2['items'] = synitems
    json.dump(d2, open(os.path.join(sd, 'data', lk + '.json'), 'w', encoding='utf-8'), ensure_ascii=False)
    srv2 = http.server.ThreadingHTTPServer(('127.0.0.1', 0), functools.partial(Q, directory=sd))
    threading.Thread(target=srv2.serve_forever, daemon=True).start()
    URL2 = f'http://127.0.0.1:{srv2.server_address[1]}/index.html'
    ctx = br.new_context(viewport={'width': 390, 'height': 900}); pg = ctx.new_page(); pg.goto(URL2); pg.wait_for_selector('#card .q')
    def synq(k): pg.locator(f'#nav button[data-i="{k}"]').click(); return pg.locator('#card .q').inner_text()
    if synq(0).startswith('Take-home. Take-home') or not synq(0).startswith('Take-home (if you have time)'): fail('doubled title Take-home not removed: ' + synq(0))
    if synq(1) != 'Make up your own: a riddle.': fail('doubled title Make up your own not removed: ' + synq(1))
    labs2 = [pg.locator(f'#nav button[data-i="{k}"] b').inner_text() for k in range(len(synitems))]
    names2 = [pg.locator(f'#nav button[data-i="{k}"]').get_attribute('aria-label') for k in range(len(synitems))]
    if labs2[0] != 'TH' and not labs2[0].startswith('TH'): fail(f'take-home label {labs2[0]!r}')
    if labs2[13:16] != ['Inv 8c-a', 'Inv 8c-b', 'G5']: fail(f'cryptic labels not shortened to the number: {labs2[13:16]}')
    if len(set(names2)) != len(names2): fail(f'synthetic accessible names are not unique: {names2}')
    if not all(nm.startswith(lb) for lb, nm in zip(labs2, names2)): fail('an accessible name does not start with its visible label')
    if 'yes?' not in names2[13] or 'any no.?' not in names2[15]: fail('descriptive part missing from the accessible name: ' + str(names2[13:16]))
    if labs2[16] == labs2[17] or 'why' not in names2[16] or 'Ali' not in names2[17]: fail(f'2(b) why / 2(b) Ali: {labs2[16:18]} {names2[16:18]}')
    # unit tails and natural wordings through the page, right and wrong
    def typed(k, txt):
        synq(k); pg.locator('#ans input[type=text]').fill(txt)
    CASES = [(2, ['27 \u2113 of water', '27 liters of water', '27 litres', '27 l of water'], ['27 liters of water in the tank', '27 liters of water 3', '72 liters of water']),
             (3, ['35 cents change', '35 cents left', '35\u00a2 change'], ['35 cents change from the shop today', '35c change', '$0.35', '0.35', '35 5 cents']),
             (4, ['35'], ['35 cents change', '35 cents left', '35 coins', '35\u00a2']),
             (5, ['\u2220AOC = 90\u00b0', 'angle AOC is 90', '90'], ['\u2220AOC = 91\u00b0', 'AOC = 90\u00b0', '\u2220 = 90']),
             (6, ['It will be Wednesday', 'It will be Wednesday.', 'it is wed', 'The answer is Wednesday'], ['It is not Wednesday', 'It will be Thursday', 'It will beWednesday']),
             (7, ['A and B and D', 'A, B and D', 'A,B,D', 'a & b & d'], ['A and B', 'A and B and C', 'B and A and D', 'A and B and D and E']),
             (8, ['1 out of 4', '2 out of 8', '1/4', 'It is 1 out of 4'], ['1 out of 5', '4 out of 1', '3 out of 4', '1 out of 0']),
             (9, ['a is equal to b', 'a equals b', 'a = b'], ['a is not equal to b', 'a is equal to c', 'b is equal']),
             (10, ['Wednesday'], ['It is Wednesday', 'It will be Wednesday']),
             # week 4 audit fixes, through the page (the same strings are in mark.test.mjs through the server marker)
             (18, ['3', "3 o'clock", '3:00', '03:00', '3.00', '3 pm', '3 am'], ['3:30', '3:05', '4:00', "4 o'clock", '3:00:00', '13:00']),
             (19, ['3'], ["3 o'clock", '3:00', '03:00']),
             (20, ['6', '6 by 6 square', '6 by 6', '6 x 6', 'a 6 by 6 square'], ['5 by 5 square', '6 by 5', '5 x 5']),
             (21, ['48', '$0.48', '48 cents'], ['$0.84', '$1.48', '0.48']),
             (22, ['CAT', '"CAT"', '\u201ccat\u201d'], ['"DOG"', '"CAT', 'CAT"']),
             (23, ['E', 'the letter E', 'letter E'], ['the letter F', 'letter']),
             (24, ['A, C, E, F', 'Shapes A, C, E and F', 'A, C, E, F,', 'A, C, E, F.'], ['Shapes A, C and E', 'A, C, E', 'A, C, E, F, G']),
             (25, ['(n-2)x180', 'Total angle = (n-2)x180', 'Sum of angles = 180n - 360', 'Angle sum = (n - 2) x 180', 'total = (n-2)x180'], ['x = 3', 'n = 5', 'total = n - 2 x 180', 'Total angle = n', 'angle sum n = (n-2)x180'])]
    # mark each wording through the page: submit one at a time by re-typing then reading the marker
    def marked(k, txt):
        typed(k, txt); pg.locator('#submit').click()
        if pg.locator('#yes').count(): pg.locator('#yes').click()
        c = cls(pg, k); pg.locator('#again').click(); return c
    CASES.append((26, ['1', '+1', '+ 1'], ['+-1', '1+', '-1', '+']))
    def marked_f(k, vals):
        synq(k); ins = pg.locator('#ans input[type=text]')
        for j, v_ in enumerate(vals): ins.nth(j).fill(v_)
        pg.locator('#submit').click()
        if pg.locator('#yes').count(): pg.locator('#yes').click()
        c = cls(pg, k); pg.locator('#again').click(); return c
    for vals, want in ((['5', '25'], 'right'), (['5:25', ''], 'right'), (['5.25', ''], 'right'), (['5 25', ''], 'right'), (['5:30', ''], 'wrong'), (['5', ''], 'wrong'), (['5:25', '30'], 'wrong'), (['', '5:25'], 'wrong'), (['5:2', ''], 'wrong')):
        if marked_f(27, vals) != want: fail(f'time boxes {vals} should be marked {want} through the page')
    for k, good, badl in CASES:
        for g in good:
            if marked(k, g) != 'right': fail(f'wording {g!r} for synthetic item {k} should be marked right')
        for b in badl:
            if marked(k, b) != 'wrong': fail(f'wording {b!r} for synthetic item {k} should be marked wrong')
    # a variant under the first picture: the old picture is hidden; the variant brings its own picture or says to draw it
    pg.reload(); pg.wait_for_selector('#card .q')
    pg.locator('#submit').click(); pg.locator('#yes').click()
    for k, withfig in ((11, True), (12, False)):
        synq(k)
        if not pg.locator('#card .fig').count(): fail('the original picture is missing before the variant is asked for')
        pg.get_by_role('button', name=re.compile('similar one')).click()
        if pg.locator('#card > .fig').count(): fail(f'S{k + 1}: the original picture (old numbers) is still shown above the variant')
        if withfig:
            ft = pg.locator('#simq .fig svg text').text_content() if pg.locator('#simq .fig svg').count() else ''
            m_ = re.search(r'There are (\d+) sheep', pg.locator('#simq .q').inner_text())
            if not m_ or ft != f'PIC {m_.group(1)}': fail(f'variant picture {ft!r} does not match the variant question {pg.locator("#simq .q").inner_text()!r}')
        else:
            if pg.locator('#simq svg').count(): fail('a variant without a picture shows a picture')
            if 'Draw it on paper' not in pg.locator('#simq').inner_text(): fail('tpl.paper: no "Draw it on paper" note')
    pg.locator('#again').click(); synq(11)
    if not pg.locator('#card > .fig').count(): fail('the original picture did not come back after Change my answers')
    ctx.close()
    # go-live: build with an endpoint -> the footer says answers are sent to the tutor and the I checked / I got it / Not yet ticks show (token present); without a token or endpoint they do not
    ep_dist = os.path.join(scratch, 'ep'); H.build(key, n, dist=ep_dist, endpoint='http://127.0.0.1:9/hol-send/x')
    html_ = open(os.path.join(ep_dist, 'index.html'), encoding='utf-8').read()
    if 'MI_SUBMIT=' not in html_ or H.FOOT_ON not in html_ or H.FOOT_OFF not in html_: fail('the endpoint build does not carry MI_SUBMIT and both footer sentences')
    off_html = open(os.path.join(DIST, 'index.html'), encoding='utf-8').read()
    if 'MI_SUBMIT=' in off_html and not os.environ.get('MI_SUBMIT_ENDPOINT'): fail('the default build has sending switched on')
    srv3 = http.server.ThreadingHTTPServer(('127.0.0.1', 0), functools.partial(Q, directory=ep_dist))
    threading.Thread(target=srv3.serve_forever, daemon=True).start()
    URL3 = f'http://127.0.0.1:{srv3.server_address[1]}/index.html'
    sj = [k for k, x in enumerate(items) if x['type'] == 'selfcheck']
    for tokenised in (False, True):
        c3 = br.new_context(viewport={'width': 800, 'height': 900}); p3 = c3.new_page()
        p3.route('**/hol-send/**', lambda r: r.fulfill(status=200, content_type='application/json', body='{"ok":true,"marks":{}}'))
        if tokenised: p3.add_init_script("sessionStorage.setItem('mi-child', JSON.stringify({token: 't'.repeat(40)}))")
        p3.goto(URL3); p3.wait_for_selector('#card .q')
        ft = p3.locator('.foot').inner_text()
        if tokenised and (H.FOOT_ON not in ft or 'stay on this device' in ft): fail('endpoint build, signed in: footer is ' + ft)
        if not tokenised and (H.FOOT_OFF not in ft or 'sent to your tutor' in ft): fail('endpoint build, not signed in: footer is ' + ft)
        p3.locator('#submit').click()
        if p3.locator('#yes').count(): p3.locator('#yes').click()
        if sj:
            p3.locator(f'#nav button[data-i="{sj[0]}"]').click()
            for lbl in ('I checked it', 'I got it', 'Not yet'):
                if bool(p3.get_by_role('button', name=lbl).count()) != tokenised: fail(f'endpoint build (signed in={tokenised}): tick "{lbl}" shown={bool(p3.get_by_role("button", name=lbl).count())}')
        c3.close()
    srv2.shutdown(); srv3.shutdown(); shutil.rmtree(scratch, ignore_errors=True)
    print('2d. doubled titles removed; cryptic nav labels shortened with the description in the accessible name (unique, label in name, TH, glyph >= 12 px); variant picture replaced or hidden; unit tails, angle names, lead-ins, "and" lists, "out of", "is equal to" right and wrong; the endpoint build switches the footer and the ticks')

    # ---- 3: wrong answers, skips, reload
    ctx, page = fresh(br)
    skip = {3, 10, 20} if N > 21 else {1}
    for i in range(N):
        if i in skip: continue
        goto(page, i); enter(page, items[i], wrong=True)
    page.reload(); page.wait_for_selector('#card .q')
    page.locator('#submit').click()
    nblank = sum(1 for i, it in enumerate(items) if i in skip and it['type'] != 'selfcheck')
    if nblank:
        if page.evaluate("document.activeElement && document.activeElement.id") != 'askbox': fail('focus not on the Submit anyway? prompt')
        if not re.search(rf'\b{nblank} questions? (has|have) no answer', page.locator('#askbox').inner_text()): fail(f'confirm does not count exactly the {nblank} unanswered marked questions: ' + page.locator('#askbox').inner_text())
        page.locator('#keep').click()
        if page.evaluate("document.activeElement && document.activeElement.id") != 'submit' or page.locator('#summary').count(): fail('Keep working: focus not back on Submit, or it submitted')
        page.locator('#submit').click(); page.locator('#yes').click()
    elif page.locator('#askbox').count():
        fail('Submit anyway? shown although only self-check items are unanswered')
    for i, it in enumerate(items):
        c = cls(page, i)
        want = 'blank' if (i in skip and it['type'] != 'selfcheck') else ('self' if it['type'] == 'selfcheck' else ('blank' if i in skip else 'wrong'))
        if c != want: fail(f'{it["id"]}: marker {c}, expected {want}')
    for i in skip:
        if items[i]['type'] != 'selfcheck':
            goto(page, i)
            if 'skipped' not in page.locator('#sol').inner_text() or not page.locator('#sol li').count(): fail('skipped question has no solution')
    page.reload(); page.wait_for_selector('#summary')
    print(f'3. wrong answers (including wrong rule wordings) marked wrong, skipped questions marked "no answer" with solutions, answers and submitted state survive a reload')
    ctx.close()

    # ---- 4: variants through the page
    nvar = 0
    ctx, page = fresh(br)
    page.evaluate("window.__q=[];window.__orig=Math.random;Math.random=function(){return window.__q.length?window.__q.shift():0.5}")
    vitems = [(i, it) for i, it in enumerate(items) if 'tpl' in it]
    for i, it in vitems:
        goto(page, i); enter(page, it)
    page.locator('#submit').click()
    if page.locator('#yes').count(): page.locator('#yes').click()
    for i, it in vitems:
        tp = it['tpl']; names = list(tp['vars'])
        combos = list(itertools.product(*[tp['vars'][k] for k in names]))
        if len(combos) > 200:
            step = len(combos) / 150.0
            combos = [combos[int(k * step)] for k in range(150)] + [combos[0], combos[-1]]
        v = lesson.VARIANTS[it['id']]
        goto(page, i)
        for combo in combos:
            env = dict(zip(names, combo))
            fr = [(tp['vars'][nm].index(env[nm]) + 0.5) / len(tp['vars'][nm]) for nm in names]
            page.evaluate('q => { window.__q = q.slice(); }', fr)
            page.get_by_role('button', name=re.compile('similar one')).click()
            full = dict(env)
            for kk, e in tp.get('derive', {}).items(): full[kk] = B.ev(e, full)
            want_q = re.sub(r'\{(\w+)\}', lambda m: str(full[m.group(1)]) if m.group(1) in full else m.group(0), tp['q'])
            shown = page.locator('#simq .q').inner_text()
            if shown != want_q: fail(f'{it["id"]} {env}: shown "{shown}" != "{want_q}"')
            if 'frame' in tp:
                fr_txt = re.sub(r'\{(\w+)\}', lambda m: str(full[m.group(1)]) if m.group(1) in full else '', tp['frame'])
                row = page.locator('#simq .row').first.inner_text().replace('\n', '')
                if re.sub(r'\s+', '', row) != re.sub(r'\s+', '', fr_txt): fail(f'{it["id"]} {env}: frame "{row}" != "{fr_txt}"')
            ans = v['oracle'](env)
            if isinstance(ans, dict):
                boxes = page.locator('#simq input[data-sf]')
                for k, nm in enumerate(tp['answers']): boxes.nth(k).fill(str(ans[nm]))
            else:
                page.locator('#simq input[data-sf]').fill(str(int(ans)))
            if nvar % 25 == 0:      # a wrong first try shows the hint but not the answer; a second wrong try shows the answer
                for tryno in (1, 2):
                    if isinstance(ans, dict):
                        for k, nm in enumerate(tp['answers']): page.locator('#simq input[data-sf]').nth(k).fill('-77')
                    else:
                        page.locator('#simq input[data-sf]').fill('-77')
                    page.locator('#simq').get_by_role('button', name='Check').click()
                    txt = page.locator('#simfb').inner_text()
                    if tryno == 1 and ('The answer is' in txt or 'Hint:' not in txt): fail(f'{it["id"]}: first wrong try must show the hint only: {txt!r}')
                    if tryno == 2 and 'The answer is' not in txt: fail(f'{it["id"]}: second wrong try must show the answer')
                if isinstance(ans, dict):
                    for k, nm in enumerate(tp['answers']): page.locator('#simq input[data-sf]').nth(k).fill(str(ans[nm]))
                else:
                    page.locator('#simq input[data-sf]').fill(str(int(ans)))
            page.locator('#simq').get_by_role('button', name='Check').click()
            if 'Yes, that is right' not in page.locator('#simfb').inner_text(): fail(f'{it["id"]} {env}: oracle answer {ans} not accepted')
            nvar += 1
    print(f'4. {nvar} variants driven through the page: the question shown equals the template and the oracle answer is accepted')
    ctx.close()

    # ---- 5: layout checks and screenshots
    ctx, page = fresh(br, 390, 900)
    nsm = 0
    for i, it in enumerate(items):
        goto(page, i)
        if page.evaluate('document.documentElement.scrollWidth > window.innerWidth + 1'): fail(f'{it["id"]}: horizontal scroll at 390 px')
        for b in figure_text_check(page, 390): fail(f'{it["id"]}: figure text {b} at 390 px'); nsm += 1
    ctx.close()
    ctx, page = fresh(br, 360, 900)
    for i, it in enumerate(items):
        goto(page, i)
        if page.evaluate('document.documentElement.scrollWidth > window.innerWidth + 1'): fail(f'{it["id"]}: horizontal scroll at 360 px')
        for b in figure_text_check(page, 360, 11.5): fail(f'{it["id"]}: figure text {b} at 360 px (minimum 11.5 px)')
    ctx.close()
    # a label and its box never split at phone width: every box sits in one non-breaking group with the words just before it, and the label's last line is on the box's line
    GROUPS = """() => [...document.querySelectorAll('#ans .fg')].map(g => {
        const inp = g.querySelector('input'), lab = g.querySelector('.fl'), ib = inp.getBoundingClientRect(), card = document.querySelector('#card').getBoundingClientRect();
        const lb = lab ? lab.getBoundingClientRect() : null, gb = g.getBoundingClientRect();
        return { label: lab ? lab.textContent : '', ok_line: !lb || (ib.top + ib.height / 2 >= lb.top - 1 && ib.top + ib.height / 2 <= lb.bottom + 1), inside: gb.left >= card.left - 1 && gb.right <= card.right + 1, nowrap: getComputedStyle(g).flexWrap === 'nowrap' && ['flex', 'inline-flex'].includes(getComputedStyle(g).display) };
      }); """
    for w in (390, 360):
        ctx, page = fresh(br, w, 900)
        ng = 0
        for i, it in enumerate(items):
            if it['type'] != 'fields': continue
            goto(page, i)
            for g in page.evaluate(GROUPS):
                ng += 1
                if not g['ok_line']: fail(f'{it["id"]}: label {g["label"]!r} is not on the same line as its box at {w} px')
                if not g['inside']: fail(f'{it["id"]}: label group {g["label"]!r} leaves the card at {w} px')
                if not g['nowrap']: fail(f'{it["id"]}: box group is not a non-breaking flex group')
            want = {('p5', 4, '4b'): ['EBF', 'FCD'], ('p5', 4, '3a'): ['Height of triangle ABC', 'Area of ABC'], ('p5', 4, '3b'): ['Height of triangle ACD', 'Area of ACD'], ('p6', 4, '1c'): ['OUT =', 'IN for OUT 48'], ('p6', 4, 'C3'): ['IN 20 gives OUT', 'OUT 99 comes from IN']}.get((key, n, it['id']))
            if want:
                labs_ = [g['label'].replace('\xa0', ' ') for g in page.evaluate(GROUPS)]
                for wtxt in want:
                    if not any(wtxt in l for l in labs_): fail(f'{it["id"]}: no group labelled {wtxt!r} at {w} px (labels {labs_})')
        ctx.close()
    # solution figures (shown after Submit, inside the answer box): text at least 11 px at 360 px and 390 px, and not cut off by the figure's edge
    nsol = 0
    for w in (360, 390):
        ctx, page = fresh(br, w, 900)
        page.locator('#submit').click()
        if page.locator('#yes').count(): page.locator('#yes').click()
        for i, it in enumerate(items):
            if not it.get('sol_svg'): continue
            goto(page, i); nsol += 1
            if page.evaluate('document.documentElement.scrollWidth > window.innerWidth + 1'): fail(f'{it["id"]}: horizontal scroll with the solution figure at {w} px')
            for b in figure_text_check(page, w, 11, '#solfig svg text'): fail(f'{it["id"]}: solution figure text {b} at {w} px')
            if page.evaluate("[...document.querySelectorAll('#solfig svg')].some(s => getComputedStyle(s).overflow !== 'visible')"): fail(f'{it["id"]}: solution svg clips its overflow')
        ctx.close()
    print(f'5b. {nsol} solution figures at 360 and 390 px: text at least 11 px and inside the figure, no horizontal scroll')
    print(f'5c. {ng} label+box groups at 390 and 360 px: each in one nowrap flex group, label on the box line, inside the card')
    print(f'5. all {N} questions fit at 390 and 360 px with no horizontal scroll; figure text is at least 11 px (11.5 px at 360 px) and inside its figure')

    def shot(name, w, h, dark=False, steps=None, full=False):
        c, p = fresh(br, w, h, dark)
        if steps: steps(p)
        if p.evaluate('document.documentElement.scrollWidth > window.innerWidth + 1'): fail(f'{name}: horizontal scroll')
        p.wait_for_timeout(150); p.screenshot(path=os.path.join(PROOF, name), full_page=full); c.close()

    def idx(i):
        return [k for k, x in enumerate(items) if x['id'] == i][0]

    def answer_some(p, upto=None, wrong_at=()):
        for i, it in enumerate(items[:upto]):
            if it['type'] != 'selfcheck':
                goto(p, i); enter(p, it, wrong=(i in wrong_at))

    def submitted(p):
        answer_some(p, None, wrong_at=(2, 7)); p.locator('#submit').click()
        if p.locator('#yes').count(): p.locator('#yes').click()

    figs = [x['id'] for x in items if x.get('svg')]
    paper_ids = [x['id'] for x in items if x.get('paper')]
    text_ids = [x['id'] for x in items if x['type'] == 'text']
    fid = figs[0] if figs else items[0]['id']
    pid = paper_ids[0] if paper_ids else fid
    tid = text_ids[0] if text_ids else fid
    vid = vitems[0][1]['id'] if vitems else fid
    shot('01_top_phone_light.png', 390, 1000, steps=lambda p: (answer_some(p, 6), goto(p, idx(tid))))
    shot('02_figure_question_phone_dark.png', 390, 1000, dark=True, steps=lambda p: goto(p, idx(pid)), full=True)
    shot('03_question_desktop_light.png', 900, 1100, steps=lambda p: (answer_some(p, 8), goto(p, idx(fid)), p.get_by_role('button', name='Give me a hint').click()))
    shot('04_confirm_submit_desktop_dark.png', 900, 1100, dark=True, steps=lambda p: (answer_some(p, 20), p.locator('#submit').click()), full=True)
    shot('05_paper_solution_phone_light.png', 390, 1000, steps=lambda p: (submitted(p), goto(p, idx(pid))), full=True)
    shot('06_paper_solution_desktop_dark.png', 900, 1200, dark=True, steps=lambda p: (submitted(p), goto(p, idx(pid))), full=True)
    shot('07_marked_wrong_phone_dark.png', 390, 1000, dark=True, steps=lambda p: (submitted(p), goto(p, 2)), full=True)
    shot('08_similar_desktop_light.png', 900, 1100, steps=lambda p: (submitted(p), goto(p, idx(vid)), p.get_by_role('button', name='Try a similar one').click()), full=True)
    for name, ix in (('09_lastfig_phone_light.png', figs[-1] if figs else fid),):
        shot(name, 390, 1000, steps=lambda p, ix=ix: goto(p, idx(ix)), full=True)
    if errors: fail('browser errors: ' + '; '.join(sorted(set(errors))[:5]))
    br.close()

# ---- 6. server-side marking: the keys made by practice/submit/make_keys.py, marked by the shared practice/submit/mark.js, agree with the page
import subprocess
sys.path.insert(0, os.path.join(H.ROOT, 'practice', 'submit'))
import make_keys                                   # noqa: E402
_k, _ver, _d, keys, _tags = make_keys.build(0, n, key)
nmodes = {}
for it, kr in zip(items, keys):      # every clock / accept_by / dollars_ok the lesson file sets reaches the built data and the server key (clock: True or per-box list)
    for fl in ('clock', 'time', 'accept_by', 'dollars_ok'):
        if src.get(it['id'], {}).get(fl) and not (it.get(fl) or kr.get(fl) or any(f.get(fl) for f in it.get('fields', []))):
            fail(f'{it["id"]}: the lesson file sets {fl} but it did not reach the built data')
        if src.get(it['id'], {}).get(fl) and not kr.get(fl): fail(f'{it["id"]}: the lesson file sets {fl} but it did not reach the server key')
for it, kr in zip(items, keys):      # the report mode is the item's own marking_mode: self = compare with a model answer / paper drawing, none = truly open
    if it['type'] != 'selfcheck':
        for fl in ('words', 'poly', 'equiv_frac', 'unit', 'dollars_ok', 'accept_by'):
            if it.get(fl) != kr.get(fl): fail(f'{it["id"]}: flag {fl} is {it.get(fl)!r} in the data but {kr.get(fl)!r} in the key')
        ck_want = True if it.get('clock') else ([bool(f.get('clock')) for f in it['fields']] if it['type'] == 'fields' and any(f.get('clock') for f in it['fields']) else None)
        if ck_want != kr.get('clock'): fail(f'{it["id"]}: clock is {ck_want!r} in the data but {kr.get("clock")!r} in the key')
        continue
    want = ('none', 'open') if it['marking_mode'] == 'none' and not it.get('paper') else ('self', 'selfcheck')
    if (kr['marking_mode'], kr['type']) != want: fail(f'{it["id"]}: self-check with marking_mode {it["marking_mode"]} exported as {kr["marking_mode"]}/{kr["type"]}')
    if it.get('paper') and kr['marking_mode'] != 'self': fail(f'{it["id"]}: paper-only item exported as {kr["marking_mode"]}')
    if re.search(r'\b(explain|why|how do you know)\b', (it['no'] + ' ' + it['q'][:60]).lower()) and kr['marking_mode'] != 'self' and not src[it['id']].get('marking_mode'):
        fail(f'{it["id"]}: an Explain item with no marking_mode of its own is exported as {kr["marking_mode"]}')
    nmodes[kr['marking_mode']] = nmodes.get(kr['marking_mode'], 0) + 1
cases = []
for it, kr in zip(items, keys):
    if kr['marking_mode'] != 'auto':
        cases.append(dict(rec=kr, v=None, want='self' if kr['marking_mode'] == 'self' else 'open')); continue
    t = it['type']
    right = [str(f['answer']) for f in it['fields']] if t == 'fields' else (', '.join(map(str, it['answer'])) if t == 'set' else (it['answer'][0] if t == 'text' else str(it['answer'])))
    wrong = [str(f['answer'] + 1) for f in it['fields']] if t == 'fields' else (str(it['answer'][0] + 100) if t == 'set' else ('zzz' if t == 'text' else ('No' if it['answer'] == 'Yes' else 'Yes') if t == 'choice' else str(it['answer'] + 1)))
    if t == 'choice':
        wrong = [o for o in it['options'] if o != it['answer']][0]
    cases.append(dict(rec=kr, v=right, want='right')); cases.append(dict(rec=kr, v=wrong, want='wrong')); cases.append(dict(rec=kr, v='', want='skipped'))
    if t == 'text' and it.get('poly'):      # the same rule written in other ways is right; changed rules are wrong
        a0 = it['answer'][0].replace('OUT = ', '').replace('out=', '')
        for v in (f'({a0})*1', f'0+{a0}', f'{a0}+0', f'OUT = {a0}', f'{a0} = {a0}'): cases.append(dict(rec=kr, v=v, want='right'))
        for v in (f'{a0}+1', f'{a0}-1', f'2*({a0})', f'({a0})+n'): cases.append(dict(rec=kr, v=v, want='wrong'))
    if t == 'text' and it.get('equiv_frac'):
        tk, rest = H.hlib.frac_tokens(it['answer'][0])
        if not rest and len(tk) > 1:
            cases.append(dict(rec=kr, v=', '.join(f'{2 * a}/{2 * b}' for a, b in tk), want='right')); cases.append(dict(rec=kr, v=', '.join(f'{a}/{b}' for a, b in reversed(tk)), want='wrong'))
            cases.append(dict(rec=kr, v=', '.join(f'{a + 1}/{b}' for a, b in tk), want='wrong'))
    if t in ('number', 'fields') and not it.get('unit') is False:      # unit and bracket forms of a whole number answer
        vals = [f['answer'] for f in it['fields']] if t == 'fields' else [it['answer']]
        if t == 'number': cases.append(dict(rec=kr, v=f'{vals[0]} cm2', want='right')); cases.append(dict(rec=kr, v=f'({vals[0]})', want='right')); cases.append(dict(rec=kr, v=f'{vals[0]}°C', want='right'))
    if t == 'number' and it.get('clock'):      # a clock hour: o'clock / :00 / pm forms are right, other minutes and other hours are wrong
        h_ = it['answer']
        for v in (f"{h_} o'clock", f'{h_}:00', f'{h_:02d}:00', f'{h_}.00', f'{h_} pm', f'{h_} am'): cases.append(dict(rec=kr, v=v, want='right'))
        for v in (f'{h_}:30', f'{h_}:05', f"{h_ % 12 + 1} o'clock", f'{h_ % 12 + 1}:00', f'{h_}:000'): cases.append(dict(rec=kr, v=v, want='wrong'))
    if t == 'fields' and kr.get('clock'):
        cl_ = kr['clock'] if isinstance(kr['clock'], list) else [True] * len(it['fields'])
        for k_, f in enumerate(it['fields']):
            if cl_[k_]:
                base = [str(g['answer']) for g in it['fields']]
                ok_ = base[:]; ok_[k_] = f"{f['answer']} o'clock"; cases.append(dict(rec=kr, v=ok_, want='right'))
                no_ = base[:]; no_[k_] = f"{f['answer']}:30"; cases.append(dict(rec=kr, v=no_, want='wrong'))
    if t == 'fields' and kr.get('time'):      # hours box + minutes box: a whole time in the first box alone is right, a wrong minute stays wrong
        th_ = kr['time'].index(True); hh_, mm_ = it['fields'][th_]['answer'], it['fields'][th_ + 1]['answer']
        base = [str(g['answer']) for g in it['fields']]
        for sep in (':', '.', ' '):
            ok_ = base[:]; ok_[th_] = f'{hh_}{sep}{mm_:02d}'; ok_[th_ + 1] = ''; cases.append(dict(rec=kr, v=ok_, want='right'))
        no_ = base[:]; no_[th_] = f'{hh_}:{(mm_ + 5) % 60:02d}'; no_[th_ + 1] = ''; cases.append(dict(rec=kr, v=no_, want='wrong'))
    if t in ('number', 'fields'):       # number words never count unless the item declares words
        w1 = [f['answer'] for f in it['fields']] if t == 'fields' else [it['answer']]
        if all(0 <= x <= 9 for x in w1) and not it.get('words'):
            W = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
            cases.append(dict(rec=kr, v=[W[x] for x in w1] if t == 'fields' else W[w1[0]], want='wrong'))
js = "const M=require(process.argv[1]);const c=JSON.parse(require('fs').readFileSync(0,'utf8'));console.log(JSON.stringify(c.map(x=>M.mark(x.rec,x.v).mark)))"
out = json.loads(subprocess.run(['node', '-e', js, os.path.join(H.ROOT, 'practice', 'submit', 'mark.js')], input=json.dumps(cases), capture_output=True, text=True, check=True).stdout)
bad = [(c['rec']['id'], c['want'], o) for c, o in zip(cases, out) if c['want'] != o]
if bad: fail(f'server marking differs: {bad[:5]}')
print(f'6. self-check items exported as {nmodes}; {len(keys)} server keys made; mark.js marks {len(cases)} right / wrong / blank / self answers as expected')

print('RESULT:', 'OK' if not fails else f'{len(fails)} FAILURES')
sys.exit(1 if fails else 0)
