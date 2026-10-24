#!/usr/bin/env python3
"""Browser tests (Chromium via Playwright) for the daily teaser on a BUILT site directory.

    MI_TEASERS=1 python3 website/lp_build.py && MI_TEASERS=1 python3 website/level_pages.py
    MI_TEASERS=1 python3 website/build_site.py --out /some/scratch/dir
    python3 website/teasers/test_site.py /some/scratch/dir [--shots DIR]

Checks: right puzzle for the Singapore date in several browser time zones, midnight rollover (23:59 / 00:00 / 00:01 SGT),
month, year and leap-day edges; a date with no released puzzle keeps the page's own fixed puzzle (no date label, no request);
the slow, failed and late fetch paths for a released month that is not built into the page; no-JS fallback; every released
puzzle's answer formats (including 21st, 0.96 for 96%, on Sunday, 1 h 30 min); wrong answers rejected; focus after "Show me how";
hint and answer-box text contrast of at least 4.5:1 in light and dark; phone and desktop layout (no sideways scroll);
no cookies / storage / third-party requests.
"""
import datetime as dt
import functools
import http.server
import json
import os
import re
import sys
import threading
import time

from playwright.sync_api import sync_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import teaser_html as TH   # noqa: E402

SITE = os.path.abspath(sys.argv[1])
SHOTS = sys.argv[sys.argv.index('--shots') + 1] if '--shots' in sys.argv else None
SGT = dt.timezone(dt.timedelta(hours=8))
PAGES = {1: '/', 2: '/ages-7-9/', 3: '/ages-8-10/', 4: '/ages-9-11/', 5: '/ages-10-12/', 6: '/ages-11-13/'}
LEVEL_PAGE = {1: '/ages-6-8/', 2: '/ages-7-9/', 3: '/ages-8-10/', 4: '/ages-9-11/', 5: '/ages-10-12/', 6: '/ages-11-13/'}
TZS = ['Asia/Singapore', 'America/Los_Angeles', 'Pacific/Kiritimati', 'Pacific/Pago_Pago', 'Europe/London', 'UTC']
results = []


def ok(name, cond, extra=''):
    results.append((name, bool(cond), extra))
    print(('PASS ' if cond else 'FAIL ') + name + ((' :: ' + str(extra)) if extra and not cond else ''))


class Quiet(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a):
        pass


def serve():
    h = functools.partial(Quiet, directory=SITE)
    srv = http.server.ThreadingHTTPServer(('127.0.0.1', 0), h)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return srv


def banks():
    out = {}
    for mm in TH.released():
        b = TH.load_month(mm)
        for lv, items in b['levels'].items():
            for e in items:
                out[(int(lv), e['date'])] = e
    return out


BANK = banks()


def expected(level, sgt_dt):
    """(puzzle id, source): a released puzzle for that Singapore date, or the page's own fixed puzzle."""
    key = '%02d-%02d' % (sgt_dt.month, sgt_dt.day)
    if (level, key) in BANK:
        return BANK[(level, key)]['id'], 'month'
    return None, 'fixed'


def load(ctx, url, when_sgt, block_fetch=False, wait=True):
    page = ctx.new_page()
    page.clock.set_fixed_time(when_sgt)
    if block_fetch:
        page.route('**/teasers/*', lambda r: r.abort())
    page.goto(url)
    if wait:
        try:
            page.wait_for_selector('#pzBox[data-teaser-state="done"]', timeout=12000)
        except Exception:
            pass
    return page


def shown(page):
    return page.evaluate("""() => { const b = document.getElementById('pzBox');
        return b ? {id: b.getAttribute('data-teaser'), date: b.getAttribute('data-teaser-date'), src: b.getAttribute('data-teaser-source'),
                    state: b.getAttribute('data-teaser-state'), text: b.innerText} : null }""")


def fixed_visible(page, level):
    """The page's own fixed puzzle is on screen and works."""
    if level == 1:
        return page.evaluate("() => { const c = document.getElementById('pzCheck'); return !!c && c.offsetParent !== null && /frog/i.test(document.getElementById('pzBox').innerText) }")
    return page.evaluate("() => { const d = document.querySelector('#pzBox details.ans'); return !!d && d.offsetParent !== null }")


def parse_rgb(s):
    nums = [float(x) for x in re.findall(r'[\d.]+', s)[:4]]
    return nums


def lum(rgb):
    def f(c):
        c = c / 255
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    return 0.2126 * f(rgb[0]) + 0.7152 * f(rgb[1]) + 0.0722 * f(rgb[2])


def contrast(fg, bg):
    a, b = lum(fg), lum(bg)
    if a < b:
        a, b = b, a
    return (a + 0.05) / (b + 0.05)


def strip_inline(route):
    """Serve the page with its built-in months removed, so the page has to fetch the month file."""
    resp = route.fetch()
    body = resp.text()
    body = re.sub(r'inline:\{.*?\},base:', 'inline:{},base:', body, flags=re.S)
    route.fulfill(response=resp, body=body)


def main():
    srv = serve()
    base = 'http://127.0.0.1:%d' % srv.server_address[1]
    with sync_playwright() as pw:
        br = pw.chromium.launch()
        # 1. date -> puzzle, in several browser time zones, for every level page
        instants = [
            dt.datetime(2026, 11, 24, 10, 0, tzinfo=SGT),
            dt.datetime(2026, 11, 30, 23, 59, 30, tzinfo=SGT),
            dt.datetime(2026, 12, 1, 0, 0, 0, tzinfo=SGT),
            dt.datetime(2026, 12, 1, 0, 0, 30, tzinfo=SGT),
            dt.datetime(2026, 12, 31, 23, 59, 59, tzinfo=SGT),
            dt.datetime(2027, 1, 1, 0, 0, 1, tzinfo=SGT),       # year end: January has no batch yet -> the page's fixed puzzle
            dt.datetime(2027, 2, 28, 23, 59, 59, tzinfo=SGT),
            dt.datetime(2027, 3, 1, 0, 0, 1, tzinfo=SGT),
            dt.datetime(2028, 2, 29, 12, 0, tzinfo=SGT),        # leap day
            dt.datetime(2026, 10, 24, 12, 0, tzinfo=SGT),       # before the first batch month -> the page's fixed puzzle
        ]
        for tz in TZS:
            ctx = br.new_context(timezone_id=tz, viewport={'width': 1100, 'height': 900})
            for when in instants:
                for lv in (1, 2, 3, 4, 5, 6):
                    url = base + (PAGES[1] if lv == 1 else LEVEL_PAGE[lv])
                    if lv == 1 and when != instants[0] and tz not in ('Asia/Singapore', 'America/Los_Angeles', 'Pacific/Kiritimati'):
                        continue
                    pg = load(ctx, url, when)
                    got = shown(pg)
                    want_id, want_src = expected(lv, when)
                    if want_src == 'month':
                        good = got and got['id'] == want_id and got['src'] == 'month' and got['date'] == '%02d-%02d' % (when.month, when.day)
                        good = good and ('puzzle for' in got['text'].lower())
                    else:
                        good = got and got['src'] == 'fixed' and not got['id'] and 'puzzle for' not in got['text'].lower() and fixed_visible(pg, lv)
                    ok('%s %s L%d -> %s' % (tz, when.strftime('%Y-%m-%d %H:%M:%S SGT'), lv, want_id or 'fixed puzzle'), good, got)
                    pg.close()
            ctx.close()
        # 2. same instant in different browser time zones shows the same puzzle (home page, Ages 6-8)
        ids = set()
        for tz in TZS:
            ctx = br.new_context(timezone_id=tz)
            pg = load(ctx, base + '/', dt.datetime(2026, 12, 15, 0, 0, 1, tzinfo=SGT))
            ids.add(shown(pg)['id'])
            ctx.close()
        ok('same puzzle in every browser time zone at 00:00:01 SGT 15 Dec', len(ids) == 1, ids)
        # 3. the latest released months are built into the page: blocking the network changes nothing, and no request is made for them
        ctx = br.new_context(timezone_id='America/Los_Angeles')
        pg = load(ctx, base + '/ages-9-11/', dt.datetime(2026, 12, 9, 12, 0, tzinfo=SGT), block_fetch=True)
        got = shown(pg)
        ok('fetch blocked, month built into the page -> the date\'s puzzle is still shown', got and got['src'] == 'month' and got['id'] == expected(4, dt.datetime(2026, 12, 9, tzinfo=SGT))[0], got)
        ctx.close()
        ctx = br.new_context(timezone_id='Asia/Singapore')
        reqs = []
        pg = ctx.new_page()
        pg.on('request', lambda r: reqs.append(r.url))
        pg.clock.set_fixed_time(dt.datetime(2027, 1, 20, 12, 0, tzinfo=SGT))
        pg.goto(base + '/ages-8-10/')
        pg.wait_for_selector('#pzBox[data-teaser-state="done"]')
        ok('unreleased month (January): no request for a month file (no 404 on the page)', not [u for u in reqs if '/teasers/' in u], [u for u in reqs if '/teasers/' in u])
        ctx.close()
        # 4. a released month that is not built into the page is fetched: slow, late, failed
        when = dt.datetime(2026, 12, 9, 12, 0, tzinfo=SGT)
        want = expected(4, when)[0]
        ctx = br.new_context(timezone_id='Asia/Singapore')
        pg = ctx.new_page()
        pg.clock.set_fixed_time(when)
        pg.route('**/ages-9-11/', strip_inline)
        held = []
        pg.route('**/teasers/*', lambda r: held.append(r))     # the month file is held back for 3.5 seconds
        pg.goto(base + '/ages-9-11/')
        pg.wait_for_timeout(3500)
        mid = shown(pg)
        ok('slow fetch: while waiting, the fixed puzzle is on screen with no date', mid and mid['src'] == 'fixed' and 'puzzle for' not in mid['text'].lower() and fixed_visible(pg, 4), mid)
        for r in held:
            r.continue_()
        try:
            pg.wait_for_selector('#pzBox[data-teaser-state="done"]', timeout=15000)
        except Exception:
            pass
        got = shown(pg)
        ok('slow fetch (3.5 s): the reply is accepted when it arrives and the date\'s puzzle is shown, with its date', got and got['id'] == want and 'puzzle for' in got['text'].lower(), got)
        ctx.close()
        ctx = br.new_context(timezone_id='Asia/Singapore')
        pg = ctx.new_page()
        pg.clock.set_fixed_time(when)
        pg.route('**/ages-9-11/', strip_inline)
        pg.route('**/teasers/*', lambda r: r.abort())
        pg.goto(base + '/ages-9-11/')
        pg.wait_for_selector('#pzBox[data-teaser-state="done"]', timeout=15000)
        got = shown(pg)
        ok('failed fetch: the fixed puzzle stays and no date is claimed', got and got['src'] == 'fixed' and 'puzzle for' not in got['text'].lower() and fixed_visible(pg, 4), got)
        ctx.close()
        ctx = br.new_context(timezone_id='Asia/Singapore')
        pg = ctx.new_page()
        pg.clock.set_fixed_time(when)
        pg.route(re.compile(r'^http://127\.0\.0\.1:\d+/$'), strip_inline)
        held = []
        pg.route('**/teasers/*', lambda r: held.append(r))
        pg.goto(base + '/')
        pg.fill('#pzA', '7')            # the visitor starts the fixed puzzle while the month file is on its way
        pg.wait_for_timeout(500)
        for r in held:
            r.continue_()
        try:
            pg.wait_for_selector('#pzBox[data-teaser-state="done"]', timeout=15000)
        except Exception:
            pass
        pg.wait_for_timeout(300)
        got = shown(pg)
        ok('late reply is not swapped in over a fixed puzzle the visitor has started', got and got['src'] == 'fixed' and pg.input_value('#pzA') == '7', got)
        ctx.close()
        # 5. no-JS fallback keeps the fixed puzzle
        ctx = br.new_context(java_script_enabled=False)
        pg = ctx.new_page()
        pg.goto(base + '/')
        txt = pg.inner_text('#tryit')
        ok('no JS: home shows the fixed frog-hops puzzle', 'frog hops' in txt.lower() and 'check' in txt.lower(), txt[:80])
        pg.goto(base + '/ages-8-10/')
        txt = pg.inner_text('#puzzle')
        ok('no JS: level page shows the fixed puzzle with its answer button', 'Show the answer' in txt, txt[:80])
        ctx.close()
        # 6. answer checking for every released puzzle, in the real page code
        ctx = br.new_context()
        pg = ctx.new_page()
        pg.goto(base + '/')
        jobs = []
        for (lv, date), e in sorted(BANK.items()):
            c = TH.compact(e)
            pos = [e['ans']] if e['type'] == 's' else [e['ans'], ' %s ' % e['ans']]
            if e['type'] == 'n':
                pos.append(e['shown'])                                        # as displayed, e.g. "12 cm", "$10.40", "4 3/8 cups"
                pos.append(e['shown'].replace('−', '-'))
                if e['fmt'] == 'money':
                    pos += ['$' + e['ans'], e['ans'] + ' dollars']
                if e['fmt'] == 'int' and int(e['ans']) >= 1000:
                    pos.append('{:,}'.format(int(e['ans'])))
                if e['units']:
                    pos.append('%s %s' % (e['ans'], e['units'][0]))
                    pos.append('%s%s' % (e['ans'], e['units'][0]))
                if e['ans'].isdigit():
                    pos.append('+' + e['ans'])
                    n = int(e['ans'])
                    if e['kind'] == 'calendar_nth' or e['frame'] in ('saturday', 'secondthursday', 'fourthwednesday'):
                        pos.append('%d%s' % (n, 'th' if 10 <= n % 100 <= 20 else {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')))
                if '%' in (e['units'] or []):
                    pos.append('%s' % (float(e['ans']) / 100))
                if 'minutes' in (e['units'] or []) and int(e['ans']) >= 60:
                    pos.append('%d h %d min' % (int(e['ans']) // 60, int(e['ans']) % 60))
            else:
                pos += [e['ans'].upper(), 'The ' + e['ans'], e['ans'] + '.', 'on ' + e['ans'], e['ans'].replace(' ', '')] + list(e['accept'])
            wrongs = list(e['wrong'])
            if e['type'] == 'n' and e['fmt'] in ('int', 'plain'):
                a = int(e['ans'])
                if a < 5000:
                    wrongs += [str(x) for x in range(0, max(300, 3 * a + 5)) if x != a]
            if e['type'] == 'n' and e['units']:
                wrongs.append('%s %s' % (e['ans'], 'zorkles'))
            if e['type'] == 'n' and e['fmt'] in ('int', 'dec', 'money', 'plain'):
                wrongs.append(e['ans'] + '1')
            jobs.append({'id': e['id'], 'p': c, 'pos': pos, 'neg': [str(w) for w in wrongs]})
        res = pg.evaluate("""(jobs) => { const bad = []; let n = 0;
            for (const j of jobs) {
              for (const s of j.pos) { n++; const r = MiTeaser.check(j.p, s); if (r !== 'ok') bad.push([j.id, s, r]); }
              for (const s of j.neg) { n++; const r = MiTeaser.check(j.p, s); if (r === 'ok') bad.push([j.id, 'WRONG ACCEPTED: ' + s, r]); }
            } return [n, bad]; }""", jobs)
        n_checked, bad = res
        ok('answer matcher: %d accept/reject checks over %d puzzles' % (n_checked, len(BANK)), not bad, bad[:10])
        # unit and format edge cases
        edge = [
            ({'a': '12', 't': 'n', 'u': ['cm', 'centimetres']}, '12 cm', 'ok'), ({'a': '12', 't': 'n', 'u': ['cm']}, '12 m', 'no'),
            ({'a': '12', 't': 'n', 'u': ['cm']}, '12', 'ok'), ({'a': '12', 't': 'n', 'u': ['cm']}, ' 12 ', 'ok'),
            ({'a': '12', 't': 'n'}, '12.0', 'ok'), ({'a': '12', 't': 'n'}, '12a', 'no'), ({'a': '12', 't': 'n'}, '', 'empty'),
            ({'a': '1/2', 't': 'n', 'e': 1}, '2/4', 'simplify'), ({'a': '1/2', 't': 'n', 'e': 1}, '0.5', 'ok'),
            ({'a': '-6', 't': 'n', 'u': ['m']}, '−6 m', 'ok'), ({'a': '-6', 't': 'n'}, '6', 'no'),
            ({'a': '3500000', 't': 'n'}, '3,500,000', 'ok'), ({'a': '3500000', 't': 'n'}, '3 500 000', 'ok'),
            ({'a': 'sunday', 't': 's', 'x': ['sun']}, ' SUNDAY. ', 'ok'), ({'a': 'sunday', 't': 's'}, 'monday', 'no'),
            ({'a': 'sunday', 't': 's'}, 'on Sunday', 'ok'), ({'a': 'jun hao', 't': 's'}, 'junhao', 'ok'), ({'a': 'jun hao', 't': 's'}, 'jun', 'no'),
            ({'a': '21', 't': 'n'}, '21st', 'ok'), ({'a': '21', 't': 'n'}, '21 st', 'ok'), ({'a': '21', 't': 'n'}, '22nd', 'no'),
            ({'a': '96', 't': 'n', 'u': ['%', 'percent']}, '96%', 'ok'), ({'a': '96', 't': 'n', 'u': ['%', 'percent']}, '0.96', 'ok'),
            ({'a': '96', 't': 'n', 'u': ['%', 'percent']}, '0.69', 'no'), ({'a': '96', 't': 'n'}, '0.96', 'no'),
            ({'a': '7', 't': 'n'}, '+7', 'ok'), ({'a': '3/4', 't': 'n', 'e': 1}, '3⁄4', 'ok'),
            ({'a': '90', 't': 'n', 'u': ['minutes', 'min']}, '1 h 30 min', 'ok'), ({'a': '90', 't': 'n', 'u': ['minutes', 'min']}, '1 h 20 min', 'no'),
        ]
        bad = []
        for p, s, want in edge:
            r = pg.evaluate('([p,s]) => MiTeaser.check(p, s)', [p, s])
            if r != want:
                bad.append((p, s, r, want))
        ok('answer matcher edge cases (units, commas, spaces, fractions, negatives, text, ordinals, percentages, on Sunday, 1 h 30 min)', not bad, bad)
        ctx.close()
        # 7. UI flow: wrong -> hint + show me how (focus moves to the explanation); right -> explanation; Enter key; contrast; no storage; no third-party requests
        for scheme in ('light', 'dark'):
            ctx = br.new_context(viewport={'width': 390, 'height': 844}, timezone_id='Asia/Singapore', color_scheme=scheme)
            reqs = []
            pg = ctx.new_page()
            pg.on('request', lambda r: reqs.append(r.url))
            pg.clock.set_fixed_time(dt.datetime(2026, 11, 2, 9, 0, tzinfo=SGT))
            pg.goto(base + '/ages-8-10/')
            pg.wait_for_selector('#pzBox[data-teaser-state="done"]')
            pg.fill('#pzdA', '99999')
            pg.press('#pzdA', 'Enter')
            t = pg.inner_text('#pzdMsg')
            ok('UI (%s): wrong answer shows the hint and a Show me how button' % scheme, 'Not yet. Hint:' in t and 'Show me how' in t, t)
            col = pg.evaluate("""() => { const m = document.querySelector('#pzdMsg .msg.no'); const cs = getComputedStyle(m);
                return [cs.color, cs.backgroundColor] }""")
            c1 = contrast(parse_rgb(col[0]), parse_rgb(col[1]))
            ok('contrast (%s): hint text %.2f:1 is at least 4.5:1' % (scheme, c1), c1 >= 4.5, col)
            pg.click('text=Show me how')
            t = pg.inner_text('#pzdMsg')
            ok('UI (%s): Show me how reveals the answer and explanation' % scheme, 'The answer is' in t, t)
            focus_id = pg.evaluate('() => document.activeElement && document.activeElement.id')
            ok('UI (%s): after Show me how, focus is on the explanation (not lost to the page)' % scheme, focus_id == 'pzdMsg', focus_id)
            pid = shown(pg)['id']
            right = [e for (lv, d), e in BANK.items() if e['id'] == pid][0]
            pg.fill('#pzdA', right['shown'])
            pg.click('#pzdCheck')
            t = pg.inner_text('#pzdMsg')
            ok('UI (%s): correct answer shows Correct and the worked explanation' % scheme, t.startswith('Correct!') and right['why'][:20] in t, t)
            col = pg.evaluate("""() => { const m = document.querySelector('#pzdMsg .msg.ok'); const cs = getComputedStyle(m);
                return [cs.color, cs.backgroundColor] }""")
            c2 = contrast(parse_rgb(col[0]), parse_rgb(col[1]))
            ok('contrast (%s): correct-answer text %.2f:1 is at least 4.5:1' % (scheme, c2), c2 >= 4.5, col)
            if scheme == 'light':
                cookies = ctx.cookies()
                stor = pg.evaluate('() => [localStorage.length, sessionStorage.length]')
                ok('no cookies, no localStorage, no sessionStorage', not cookies and stor == [0, 0], (cookies, stor))
                external = [u for u in reqs if not u.startswith(base)]
                ok('no third-party requests', not external, external[:5])
                ok('month built into the page: no request for a month file', not [u for u in reqs if '/teasers/' in u], [u for u in reqs if '/teasers/' in u])
            ctx.close()
        # 8. layout and screenshots
        if SHOTS:
            os.makedirs(SHOTS, exist_ok=True)
        for name, vw in (('phone', {'width': 390, 'height': 844}), ('desktop', {'width': 1280, 'height': 900})):
            ctx = br.new_context(viewport=vw, timezone_id='Asia/Singapore')
            for lv in (1, 2, 3, 4, 5, 6):
                url = base + (PAGES[1] if lv == 1 else LEVEL_PAGE[lv])
                for day, when in ((1, dt.datetime(2026, 11, 3, 8, 0, tzinfo=SGT)), (2, dt.datetime(2026, 12, 19, 8, 0, tzinfo=SGT)), (3, dt.datetime(2027, 1, 12, 8, 0, tzinfo=SGT))):
                    pg = load(ctx, url, when)
                    sel = '#tryit' if lv == 1 else '#puzzle'
                    over = pg.evaluate('() => document.documentElement.scrollWidth - window.innerWidth')
                    ok('%s L%d %s: no sideways scroll' % (name, lv, when.strftime('%d %b')), over <= 0, over)
                    boxw = pg.evaluate("() => { const b=document.getElementById('pzBox'); const r=b.getBoundingClientRect(); return [r.left, r.right, window.innerWidth] }")
                    ok('%s L%d %s: puzzle box inside the viewport' % (name, lv, when.strftime('%d %b')), boxw[0] >= 0 and boxw[1] <= boxw[2] + 1, boxw)
                    if SHOTS:
                        pg.locator(sel).scroll_into_view_if_needed()
                        pg.locator(sel).screenshot(path=os.path.join(SHOTS, '%s_L%d_%s.png' % (name, lv, when.strftime('%m%d'))))
                    pg.close()
            ctx.close()
        br.close()
    srv.shutdown()
    failed = [r for r in results if not r[1]]
    print('\n%d checks, %d failed' % (len(results), len(failed)))
    json.dump([{'name': n, 'ok': o} for n, o, _ in results], open(os.path.join(SITE, '..', 'teaser_test_results.json'), 'w'))
    sys.exit(1 if failed else 0)


if __name__ == '__main__':
    main()
