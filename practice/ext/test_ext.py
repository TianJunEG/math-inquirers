#!/usr/bin/env python3
"""Browser test of a built extension practice page (Playwright/Chromium), and screenshots.

    python3 practice/ext/build_ext.py 2 1 && python3 practice/ext/test_ext.py 2 1

1. re-reads the BUILT data file and recomputes every answer from the independent checks again (the output file is checked, not the build);
2. in a real browser, types the correct answer into every item and expects "Yes, that is right";
3. types a wrong answer twice into every item and expects the hint after the first and the worked solution after the second;
4. for every variant family, forces the runner to pick each combination of the variables (all of them, or 150 spread over a large family),
   checks the question the child sees equals the template filled in by Python, types the ORACLE's answer and expects "Yes, that is right";
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


def enter(page, it, vals=None, wrong=False):
    """Type / choose an answer. vals None = the stored correct answer; wrong = a different answer."""
    t = it['type']
    if t == 'fields':
        a = [f['answer'] for f in it['fields']] if vals is None else vals
        if wrong: a = [x + 1 for x in a]
        boxes = page.locator('#ans input[data-f]')
        assert boxes.count() == len(a), (it['id'], boxes.count(), len(a))
        for i, x in enumerate(a): boxes.nth(i).fill(str(x))
    elif t == 'set':
        a = list(it['answer']) if vals is None else vals
        if wrong: a = a[:-1] + [a[-1] + 1]
        page.locator('#ans input[type=text]').fill(', '.join(map(str, a)))
    elif t == 'number':
        a = vals if vals is not None else it['answer']
        page.locator('#ans input[type=text]').fill(str(a + (1 if wrong else 0)))
    elif t == 'choice':
        opts = it['options']
        pick = it['answer'] if not wrong else [o for o in opts if o != it['answer']][0]
        page.locator('#ans label.opt', has_text=re.compile('^' + re.escape(pick) + '$')).click()


def open_item(page, tier_label, n):
    page.get_by_role('button', name=tier_label, exact=True).click()
    page.locator('#dots button').nth(n).click()


with sync_playwright() as pw:
    br = pw.chromium.launch()
    ctx = br.new_context(viewport={'width': 800, 'height': 900})
    page = ctx.new_page()
    errors = []
    page.on('pageerror', lambda e: errors.append(str(e)))
    page.on('console', lambda m: errors.append(m.text) if m.type == 'error' else None)
    page.goto(URL); page.wait_for_selector('#card .q')

    by_tier = {}
    for it in items: by_tier.setdefault(it['tier'], []).append(it)
    LAB = {'core': 'Start here', 'stretch': 'Think harder', 'challenge': 'Go further', 'check': 'Check yourself'}

    # ---- 2 + 3: every item, right and wrong
    right = wrongs = 0
    for tier, lst in by_tier.items():
        for n, it in enumerate(lst):
            ctx.clear_cookies(); page.evaluate('localStorage.clear()'); page.goto(URL); page.wait_for_selector('#card .q')
            open_item(page, LAB[tier], n)
            qtxt = page.locator('#card .q').inner_text()
            if qtxt != it['q']: fail(f'{it["id"]}: shown question differs from data')
            if it['type'] == 'selfcheck':
                page.locator('#card textarea').fill('my riddle'); page.get_by_role('button', name='Show me how to check it').click()
                if not page.locator('.fb').count(): fail(f'{it["id"]}: no check text')
                continue
            enter(page, it); page.get_by_role('button', name='Check', exact=True).click()
            if 'Yes, that is right' not in page.locator('#fb').inner_text(): fail(f'{it["id"]}: correct answer not accepted')
            else: right += 1
            # wrong twice
            page.goto(URL); page.wait_for_selector('#card .q'); page.evaluate('localStorage.clear()'); page.goto(URL); page.wait_for_selector('#card .q')
            open_item(page, LAB[tier], n)
            enter(page, it, wrong=True); page.get_by_role('button', name='Check', exact=True).click()
            t1 = page.locator('#fb').inner_text()
            if 'Try once more' not in t1 or 'Hint:' not in t1: fail(f'{it["id"]}: first wrong answer gave {t1[:60]!r}')
            if it['type'] in ('fields', 'set'):
                enter(page, it, vals=None, wrong=True)
                # different wrong answer the second time (the runner asks for a different one if it is the same)
                if it['type'] == 'fields':
                    boxes = page.locator('#ans input[data-f]')
                    for i, f in enumerate(it['fields']): boxes.nth(i).fill(str(f['answer'] + 2))
                else:
                    page.locator('#ans input[type=text]').fill(', '.join(map(str, it['answer'][:-1] + [it['answer'][-1] + 2])))
            else:
                other = [o for o in it['options'] if o != it['answer']]
                page.locator('#ans label.opt', has_text=re.compile('^' + re.escape(other[-1]) + '$')).click()
            page.get_by_role('button', name='Check', exact=True).click()
            t2 = page.locator('#fb').inner_text()
            if 'Let us look at it together' not in t2 or 'Here is how to get it' not in t2: fail(f'{it["id"]}: second wrong answer gave {t2[:60]!r}')
            wrongs += 1
    print(f'2. {right} correct answers accepted in the browser; 3. {wrongs} items gave the hint then the worked solution')

    # ---- 4: variants, forced through every combination
    nvar = 0
    for it in items:
        if 'tpl' not in it: continue
        tp = it['tpl']; names = list(tp['vars'])
        combos = list(itertools.product(*[tp['vars'][k] for k in names]))
        if len(combos) > 200:
            step = len(combos) / 150.0
            combos = [combos[int(i * step)] for i in range(150)] + [combos[0], combos[-1]]
        v = side.VARIANTS[it['id']]
        tier = it['tier']; n = by_tier[tier].index(it)
        ctx.clear_cookies(); page.evaluate('localStorage.clear()'); page.goto(URL); page.wait_for_selector('#card .q')
        page.add_init_script("window.__q=[];Math.random=function(){return window.__q.length?window.__q.shift():0.5};") if False else None
        page.evaluate("window.__q=[];window.__orig=Math.random;Math.random=function(){return window.__q.length?window.__q.shift():0.5}")
        open_item(page, LAB[tier], n)
        enter(page, it); page.get_by_role('button', name='Check', exact=True).click()       # finish the authored one first so 'similar' shows
        prev = None
        for k, combo in enumerate(combos):
            if combo == prev: continue
            env = dict(zip(names, combo))
            fr = [(tp['vars'][nm].index(env[nm]) + 0.5) / len(tp['vars'][nm]) for nm in names]
            page.evaluate('q => { window.__q = q.slice(); }', fr)
            page.get_by_role('button', name='Try a similar one').click()
            full = dict(env)
            for kk, e in tp.get('derive', {}).items(): full[kk] = B.ev(e, full)
            want_q = re.sub(r'\{(\w+)\}', lambda m: str(full[m.group(1)]) if m.group(1) in full else m.group(0), tp['q'])
            shown = page.locator('#card .q').inner_text()
            if shown != want_q: fail(f'{it["id"]} {env}: shown "{shown}" != "{want_q}"')
            ans = v['oracle'](env)
            if isinstance(ans, dict):
                boxes = page.locator('#ans input[data-f]')
                order = list(tp['answers'])
                for i, nm in enumerate(order): boxes.nth(i).fill(str(ans[nm]))
            else:
                page.locator('#ans input[type=text]').fill(str(int(ans)))
            page.get_by_role('button', name='Check', exact=True).click()
            if 'Yes, that is right' not in page.locator('#fb').inner_text(): fail(f'{it["id"]} {env}: oracle answer {ans} not accepted')
            nvar += 1; prev = combo
        page.evaluate('Math.random = window.__orig')
    print(f'4. {nvar} variants driven through the runner: the shown question equals the template and the oracle answer is accepted')

    # ---- 5: screenshots
    def shot(name, w=800, h=1000, dark=False, setup=None, full=False):
        c = br.new_context(viewport={'width': w, 'height': h}, color_scheme='dark' if dark else 'light', device_scale_factor=1)
        p = c.new_page(); p.goto(URL); p.wait_for_selector('#card .q')
        if setup: setup(p)
        p.wait_for_timeout(200)
        p.screenshot(path=os.path.join(PROOF, name), full_page=full); c.close()

    def idx(tier, src, part=None):
        return [i for i, x in enumerate(by_tier[tier]) if x['src'] == src and x['part'] == part][0]

    def go(tier, src, part=None, answer=None, wrong=0, shown=False):
        def f(p):
            p.get_by_role('button', name=LAB[tier], exact=True).click()
            p.locator('#dots button').nth(idx(tier, src, part)).click()
            it = by_tier[tier][idx(tier, src, part)]
            if answer == 'right':
                enter(p, it); p.get_by_role('button', name='Check', exact=True).click()
            elif answer == 'wrong':
                enter(p, it, wrong=True); p.get_by_role('button', name='Check', exact=True).click()
        return f

    shot('01_top_phone.png', 390, 900, setup=lambda p: None, full=False)
    shot('02_top_desktop.png', 900, 1000)
    shot('03_number_line_phone.png', 390, 900, setup=go('core', 'L2U01-S09', 'a'))
    shot('04_choice_desktop.png', 800, 800, setup=go('core', 'L2U01-S03', 'c', 'right'))
    shot('05_wrong_hint_desktop.png', 800, 900, setup=go('stretch', 'L2U01-T01', 'a', 'wrong'))
    shot('06_right_worked_phone.png', 390, 1100, setup=go('core', 'L2U01-S02', None, 'right'), full=True)
    shot('07_chart_set_dark.png', 800, 1000, dark=True, setup=go('core', 'L2U01-S10', 'a'))
    shot('08_blocks_phone_dark.png', 390, 900, dark=True, setup=go('core', 'L2U01-S02'))
    if errors: fail('browser errors: ' + '; '.join(sorted(set(errors))[:5]))
    br.close()

print('RESULT:', 'OK' if not fails else f'{len(fails)} FAILURES')
sys.exit(1 if fails else 0)
