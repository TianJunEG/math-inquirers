#!/usr/bin/env python3
"""Browser test of a built extension practice page (Playwright/Chromium), and screenshots.

    python3 practice/ext/build_ext.py 2 1 && python3 practice/ext/test_ext.py 2 1

1. re-reads the BUILT data file and recomputes every answer from the independent checks again (the output file is checked, not the build);
2. in a real browser opens the questions in REVERSE order, types the correct answer into each, submits (with the "unanswered" confirm for the
   open question), and expects every question marked right and a worked solution for each;
3. a second child answers wrongly, skips three, reloads (answers survive), submits, and sees wrong / no-answer marks and solutions for skipped ones;
   solutions are hidden before submit and again after "Change my answers";
4. for every variant family, forces the runner to pick each combination of the variables (all, or 150 spread over a large family),
   checks the question shown equals the template filled in by Python, types the ORACLE's answer and expects "Yes, that is right";
5. takes screenshots (phone and desktop, light and dark) into practice/ext/proof/.
"""
import functools, http.server, itertools, json, os, re, sys, threading
os.environ.setdefault('PLAYWRIGHT_BROWSERS_PATH', '/opt/pw-browsers')
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_ext as B                      # noqa: E402
from playwright.sync_api import sync_playwright   # noqa: E402

level = int(sys.argv[1]) if len(sys.argv) > 1 else 2
unit = int(sys.argv[2]) if len(sys.argv) > 2 else 1
base = f'l{level}_u{unit:02d}'; key = f'l{level}u{unit:02d}'
DIST = os.path.join(HERE, 'dist', key)
PROOF = os.path.join(HERE, 'proof'); os.makedirs(PROOF, exist_ok=True)
data = json.load(open(os.path.join(DIST, 'data', key + '.json'), encoding='utf-8'))
items = data['items']
checks = B.load_mod(os.path.join(B.EXT, 'verify', base + '_checks.py'), base + '_checks2').CHECKS
side = B.load_mod(os.path.join(HERE, 'variants', base + '.py'), base + '_variants2')
fails = []


def fail(msg):
    fails.append(msg); print('FAIL', msg)


# ---- 1. the built data against fresh independent checks
def expected_values(it):
    got = checks[it['src']]()
    v = got[it['part']] if it['part'] else got
    return [str(x) for x in v]

for it in items:
    exp = expected_values(it)
    if it['type'] == 'fields':
        mine = [str(f['answer']) for f in it['fields']]
    elif it['type'] == 'set':
        mine = [str(x) for x in it['answer']]
    elif it['type'] == 'choice':
        mine = [it['answer']]
    else:
        mine = ['open']
    if (it['type'] == 'set' and not it['ordered']) and sorted(mine) == sorted(exp):
        continue
    if mine != exp:
        fail(f'{it["id"]}: built data {mine} differs from the independent check {exp}')
print(f'1. {len(items)} built items re-checked against the independent check functions')


def answer_strings(it):
    if it['type'] == 'fields':
        return [str(f['answer']) for f in it['fields']]
    if it['type'] == 'set':
        return [str(x) for x in it['answer']]
    return None


class Q(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a): pass

srv = http.server.ThreadingHTTPServer(('127.0.0.1', 0), functools.partial(Q, directory=DIST))
threading.Thread(target=srv.serve_forever, daemon=True).start()
URL = f'http://127.0.0.1:{srv.server_address[1]}/index.html'



def enter(page, it, wrong=False):
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
    elif t == 'choice':
        pick = it['answer'] if not wrong else [o for o in it['options'] if o != it['answer']][0]
        page.locator('#ans label.opt', has_text=re.compile('^' + re.escape(pick) + '$')).click()
    elif t == 'selfcheck':
        pass


def goto(page, i):
    page.locator(f'#nav button[data-i="{i}"]').click()


def fresh(br, w=800, h=900, dark=False):
    c = br.new_context(viewport={'width': w, 'height': h}, color_scheme='dark' if dark else 'light')
    p = c.new_page(); p.goto(URL); p.wait_for_selector('#card .q')
    return c, p


with sync_playwright() as pw:
    br = pw.chromium.launch()
    errors = []
    N = len(items)
    cls = lambda p, i: p.locator(f'#nav button[data-i="{i}"]').get_attribute('class').split()[-1]

    # ---- 2: a child who answers everything, in reverse order
    ctx, page = fresh(br)
    page.on('pageerror', lambda e: errors.append(str(e)))
    page.on('console', lambda m: errors.append(m.text) if m.type == 'error' else None)
    page.reload(); page.wait_for_selector('#card .q')
    mi = next(k for k, x in enumerate(items) if x['type'] != 'selfcheck')     # one marked question is left blank on purpose: Submit asks first (a self-check item is never 'unanswered')
    for i in reversed(range(N)):
        goto(page, i)
        if page.locator('#card .q').inner_text() != items[i]['q']: fail(f'{items[i]["id"]}: shown question differs from data')
        if page.locator('#sol').count(): fail(f'{items[i]["id"]}: solution visible before submit')
        if i != mi: enter(page, items[i])
    page.locator('#submit').click()
    if 'no answer' not in page.locator('#bar').inner_text(): fail('no confirm for the unanswered question')
    page.locator('#keep').click()
    if page.locator('#summary').count(): fail('submitted although the child kept working')
    goto(page, mi); enter(page, items[mi])
    page.locator('#submit').click()
    if page.locator('#yes').count(): fail('Submit anyway? shown although every marked question has an answer')
    summ = page.locator('#summary').inner_text()
    nself = sum(1 for it in items if it['type'] == 'selfcheck')
    if f'{N - nself} of {N - nself} marked questions are right' not in summ: fail('summary: ' + summ)
    bad = 0
    for i, it in enumerate(items):
        goto(page, i)
        c = cls(page, i)
        if c != ('self' if it['type'] == 'selfcheck' else 'right'): fail(f'{it["id"]}: marker {c}')
        sol = page.locator('#sol').inner_text()
        if not page.locator('#sol li').count(): fail(f'{it["id"]}: no worked steps after submit')
        if it['type'] != 'selfcheck':
            want = str(B.NORM and (it['answer'] if it['type'] != 'fields' else ', '.join(str(f['answer']) for f in it['fields'])))
            if it['type'] == 'choice' and it['answer'] not in sol: fail(f'{it["id"]}: answer not in solution')
            if it['type'] == 'fields' and not all(str(f['answer']) in sol for f in it['fields']): fail(f'{it["id"]}: answer not in solution')
        bad += 0
    print(f'2. {N} questions opened in reverse order, all answered, submitted: {N - nself} marked right, {N} worked solutions shown')
    page.locator('#again').click()
    if page.locator('#sol').count(): fail('solution still visible after "Change my answers"')
    ctx.close()

    # ---- 3: wrong answers, skips, reload
    ctx, page = fresh(br)
    skip = {3, 10, 20}
    for i in range(N):
        if i in skip: continue
        goto(page, i); enter(page, items[i], wrong=True)
    page.reload(); page.wait_for_selector('#card .q')
    goto(page, 0)
    first = items[0]
    if first['type'] == 'fields' and page.locator('#ans input[data-f]').first.input_value() != str(first['fields'][0]['answer'] + 1): fail('answers did not survive a reload')
    page.locator('#submit').click(); page.locator('#yes').click()
    for i, it in enumerate(items):
        c = cls(page, i)
        want = 'blank' if i in skip else ('self' if it['type'] == 'selfcheck' else 'wrong')
        if c != want: fail(f'{it["id"]}: marker {c}, expected {want}')
    goto(page, 3)
    if 'skipped' not in page.locator('#sol').inner_text() or not page.locator('#sol li').count(): fail('skipped question has no solution')
    page.reload(); page.wait_for_selector('#summary')
    print('3. wrong answers marked wrong, 3 skipped questions marked "no answer" with solutions, answers and submitted state survive a reload')
    ctx.close()

    # ---- 4: variants through the page
    nvar = 0
    ctx, page = fresh(br)
    page.evaluate("window.__q=[];window.__orig=Math.random;Math.random=function(){return window.__q.length?window.__q.shift():0.5}")
    for i, it in enumerate(items):
        if 'tpl' not in it: continue
        goto(page, i); enter(page, it)
    page.locator('#submit').click(); page.locator('#yes').click()
    for i, it in enumerate(items):
        if 'tpl' not in it: continue
        tp = it['tpl']; names = list(tp['vars'])
        combos = list(itertools.product(*[tp['vars'][k] for k in names]))
        if len(combos) > 200:
            step = len(combos) / 150.0
            combos = [combos[int(k * step)] for k in range(150)] + [combos[0], combos[-1]]
        v = side.VARIANTS[it['id']]
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
            ans = v['oracle'](env)
            if isinstance(ans, dict):
                boxes = page.locator('#simq input[data-sf]')
                for k, nm in enumerate(tp['answers']): boxes.nth(k).fill(str(ans[nm]))
            else:
                page.locator('#simq input[data-sf]').fill(str(int(ans)))
            page.locator('#simq').get_by_role('button', name='Check').click()
            if 'Yes, that is right' not in page.locator('#simfb').inner_text(): fail(f'{it["id"]} {env}: oracle answer {ans} not accepted')
            nvar += 1
    print(f'4. {nvar} variants driven through the page: the question shown equals the template and the oracle answer is accepted')
    ctx.close()

    # ---- 5: screenshots
    def shot(name, w, h, dark=False, steps=None, full=False):
        c, p = fresh(br, w, h, dark)
        if steps: steps(p)
        p.wait_for_timeout(150); p.screenshot(path=os.path.join(PROOF, name), full_page=full); c.close()

    def idx(src, part=None):
        return [i for i, x in enumerate(items) if x['src'] == src and x['part'] == part][0]

    def answer_some(p, n=14, wrong_at=(2, 7)):
        for i in range(n):
            if items[i]['type'] != 'selfcheck':
                goto(p, i); enter(p, items[i], wrong=(i in wrong_at))

    def submitted(p):
        answer_some(p); p.locator('#submit').click(); p.locator('#yes').click()

    shot('01_top_phone.png', 390, 1000, steps=lambda p: (answer_some(p, 6), goto(p, idx('L2U01-S09', 'a'))))
    shot('02_question_desktop.png', 900, 1100, steps=lambda p: (answer_some(p, 8), goto(p, idx('L2U01-S10', 'a')), p.get_by_role('button', name='Give me a hint').click()))
    shot('03_confirm_submit_desktop.png', 900, 1100, steps=lambda p: (answer_some(p, 20), p.locator('#submit').click()), full=True)
    shot('04_marked_solution_desktop.png', 900, 1200, steps=lambda p: (submitted(p), goto(p, 2)), full=True)
    shot('05_skipped_solution_phone.png', 390, 1000, steps=lambda p: (submitted(p), goto(p, 30)), full=True)
    shot('06_similar_dark.png', 800, 1100, dark=True, steps=lambda p: (submitted(p), goto(p, 0), p.get_by_role('button', name='Try a similar one').click()), full=True)
    shot('07_blocks_phone_dark.png', 390, 1000, dark=True, steps=lambda p: goto(p, idx('L2U01-S02')))
    if errors: fail('browser errors: ' + '; '.join(sorted(set(errors))[:5]))
    br.close()

print('RESULT:', 'OK' if not fails else f'{len(fails)} FAILURES')
sys.exit(1 if fails else 0)
