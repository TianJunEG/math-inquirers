#!/usr/bin/env python3
"""Browser tests (Chromium via Playwright) for the daily teaser on a BUILT site directory.

    MI_TEASERS=1 python3 website/lp_build.py && MI_TEASERS=1 python3 website/level_pages.py
    MI_TEASERS=1 python3 website/build_site.py --out /some/scratch/dir
    python3 website/teasers/test_site.py /some/scratch/dir [--shots DIR]

Checks: right puzzle for the Singapore date in several browser time zones, midnight rollover (23:59 / 00:00 / 00:01 SGT),
month, year and leap-day edges, fallback when a month has no batch or the fetch fails, no-JS fallback, every released puzzle's
answer formats, wrong answers rejected, phone and desktop layout (no sideways scroll), no cookies / storage / third-party requests.
"""
import datetime as dt
import functools
import http.server
import json
import os
import sys
import threading

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
    key = '%02d-%02d' % (sgt_dt.month, sgt_dt.day)
    if (level, key) in BANK:
        return BANK[(level, key)]['id'], 'month'
    pool = TH.fallback_pool(level)
    day = (sgt_dt.date() - dt.date(1970, 1, 1)).days
    return pool[day % len(pool)]['i'], 'pool'


def load(ctx, url, when_sgt, block_fetch=False):
    page = ctx.new_page()
    page.clock.set_fixed_time(when_sgt)
    if block_fetch:
        page.route('**/teasers/*', lambda r: r.abort())
    page.goto(url)
    try:
        page.wait_for_selector('[data-teaser]', timeout=6000)
    except Exception:
        pass
    return page


def shown(page):
    return page.evaluate("""() => { const b = document.getElementById('pzBox');
        return b ? {id: b.getAttribute('data-teaser'), date: b.getAttribute('data-teaser-date'), src: b.getAttribute('data-teaser-source')} : null }""")


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
            dt.datetime(2027, 1, 1, 0, 0, 1, tzinfo=SGT),       # year end: January has no batch yet -> fallback pool
            dt.datetime(2027, 2, 28, 23, 59, 59, tzinfo=SGT),
            dt.datetime(2027, 3, 1, 0, 0, 1, tzinfo=SGT),
            dt.datetime(2028, 2, 29, 12, 0, tzinfo=SGT),        # leap day
            dt.datetime(2026, 10, 24, 12, 0, tzinfo=SGT),       # before the first batch month -> fallback pool
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
                    ok('%s %s L%d -> %s' % (tz, when.strftime('%Y-%m-%d %H:%M:%S SGT'), lv, want_id),
                       got and got['id'] == want_id and got['src'] == want_src and got['date'] == '%02d-%02d' % (when.month, when.day), got)
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
        # 3. fetch failure -> pool fallback; still a valid puzzle
        ctx = br.new_context(timezone_id='America/Los_Angeles')
        pg = load(ctx, base + '/ages-9-11/', dt.datetime(2026, 12, 9, 12, 0, tzinfo=SGT), block_fetch=True)
        got = shown(pg)
        ok('fetch blocked -> fallback pool puzzle shown', got and got['src'] == 'pool', got)
        ctx.close()
        # 4. no-JS fallback keeps the fixed puzzle
        ctx = br.new_context(java_script_enabled=False)
        pg = ctx.new_page()
        pg.goto(base + '/')
        txt = pg.inner_text('#tryit')
        ok('no JS: home shows the fixed frog-hops puzzle', 'frog hops' in txt.lower() and 'check' in txt.lower(), txt[:80])
        pg.goto(base + '/ages-8-10/')
        txt = pg.inner_text('#puzzle')
        ok('no JS: level page shows the fixed puzzle with its answer button', 'Show the answer' in txt, txt[:80])
        ctx.close()
        # 5. answer checking for every released puzzle, in the real page code
        ctx = br.new_context()
        pg = ctx.new_page()
        pg.goto(base + '/')
        jobs = []
        for (lv, date), e in sorted(BANK.items()):
            c = TH.compact(e)
            pos = [e['ans']] if e['type'] == 's' else [e['ans'], ' %s ' % e['ans']]
            if e['type'] == 'n':
                pos.append(e['shown'])                                        # as displayed, e.g. "12 cm", "$10.40", "4 3/8 cups"
                pos.append(e['shown'].replace('\u2212', '-'))
                if e['fmt'] == 'money':
                    pos += ['$' + e['ans'], e['ans'] + ' dollars']
                if e['fmt'] == 'int' and int(e['ans']) >= 1000:
                    pos.append('{:,}'.format(int(e['ans'])))
                if e['units']:
                    pos.append('%s %s' % (e['ans'], e['units'][0]))
                    pos.append('%s%s' % (e['ans'], e['units'][0]))
            else:
                pos += [e['ans'].upper(), 'The ' + e['ans'], e['ans'] + '.'] + list(e['accept'])
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
        ]
        bad = []
        for p, s, want in edge:
            r = pg.evaluate('([p,s]) => MiTeaser.check(p, s)', [p, s])
            if r != want:
                bad.append((p, s, r, want))
        ok('answer matcher edge cases (units, commas, spaces, fractions, negatives, text)', not bad, bad)
        ctx.close()
        # 6. UI flow: wrong -> hint + show me how; right -> explanation; Enter key; no storage; no third-party requests
        ctx = br.new_context(viewport={'width': 390, 'height': 844}, timezone_id='Asia/Singapore')
        reqs = []
        pg = ctx.new_page()
        pg.on('request', lambda r: reqs.append(r.url))
        pg.clock.set_fixed_time(dt.datetime(2026, 11, 2, 9, 0, tzinfo=SGT))
        pg.goto(base + '/ages-8-10/')
        pg.wait_for_selector('[data-teaser]')
        pg.fill('#pzA', '99999')
        pg.press('#pzA', 'Enter')
        t = pg.inner_text('#pzMsg')
        ok('UI: wrong answer shows the hint and a Show me how button', 'Not yet. Hint:' in t and 'Show me how' in t, t)
        pg.click('text=Show me how')
        t = pg.inner_text('#pzMsg')
        ok('UI: Show me how reveals the answer and explanation', 'The answer is' in t, t)
        pid = shown(pg)['id']
        right = [e for (lv, d), e in BANK.items() if e['id'] == pid][0]
        pg.fill('#pzA', right['shown'])
        pg.click('#pzCheck')
        t = pg.inner_text('#pzMsg')
        ok('UI: correct answer shows Correct and the worked explanation', t.startswith('Correct!') and right['why'][:20] in t, t)
        cookies = ctx.cookies()
        stor = pg.evaluate('() => [localStorage.length, sessionStorage.length]')
        ok('no cookies, no localStorage, no sessionStorage', not cookies and stor == [0, 0], (cookies, stor))
        external = [u for u in reqs if not u.startswith(base)]
        ok('no third-party requests', not external, external[:5])
        ctx.close()
        # 7. layout and screenshots
        if SHOTS:
            os.makedirs(SHOTS, exist_ok=True)
        for name, vw in (('phone', {'width': 390, 'height': 844}), ('desktop', {'width': 1280, 'height': 900})):
            ctx = br.new_context(viewport=vw, timezone_id='Asia/Singapore')
            for lv in (1, 2, 3, 4, 5, 6):
                url = base + (PAGES[1] if lv == 1 else LEVEL_PAGE[lv])
                for day, when in ((1, dt.datetime(2026, 11, 3, 8, 0, tzinfo=SGT)), (2, dt.datetime(2026, 12, 19, 8, 0, tzinfo=SGT))):
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
