#!/usr/bin/env python3
"""Header generation test for website/build_site.py (round-1 audit M10). Builds into a scratch --out directory; never touches website/dist.

    python3 website/tests/headers_test.py

Checks the generated _headers: /practice/* has its own strict CSP (script-src 'self', no unsafe-inline, connect-src 'self' + the Worker origin when given,
frame-ancestors 'none', object-src 'none'), Referrer-Policy no-referrer and Cache-Control no-store; /portal/* keeps its own CSP; no site-wide rule (/*) carries a CSP
(Cloudflare would join two CSPs); every site page path still has the site CSP; and --practice-dir moves inline scripts into files so the strict CSP holds.
"""
import os, re, subprocess, sys, tempfile, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.dirname(HERE)
n = 0

def ok(cond, msg):
    global n
    assert cond, msg
    n += 1

def rules(text):
    out, cur = {}, None
    for line in text.splitlines():
        if line and not line.startswith(' '):
            cur = line.strip(); out[cur] = []
        elif cur and line.strip():
            out[cur].append(line.strip())
    return out

def build(extra, env=None):
    out = tempfile.mkdtemp(prefix='mi-headers-')
    e = dict(os.environ); e.update(env or {})
    r = subprocess.run([sys.executable, os.path.join(SITE, 'build_site.py'), '--out', out] + extra, capture_output=True, text=True, env=e, cwd=SITE)
    assert r.returncode == 0, r.stderr[-800:]
    return out, r.stdout

def header(rule, name):
    return [l for l in rule if l.lower().startswith(name.lower() + ':')]

# fixture: one practice page with the generators' inline config script
prac = tempfile.mkdtemp(prefix='mi-practice-')
os.makedirs(os.path.join(prac, 'holiday', 'p1', '03'))
open(os.path.join(prac, 'holiday', 'p1', '03', 'index.html'), 'w').write(
    '<!doctype html><html><head><script type="application/ld+json">{"a":1}</script></head><body><script>window.MI_LESSON="p1l03";window.MI_SUBMIT={"endpoint":"/api/practice/submit"};</script><script src="sheet.js"></script></body></html>')
open(os.path.join(prac, 'holiday', 'p1', '03', 'sheet.js'), 'w').write('/* stand-in */')

for label, extra, env in (('with portal + practice', ['--with-portal', '--practice-dir', prac], {'SUPABASE_URL': 'https://abcd.supabase.co', 'SUPABASE_ANON_KEY': 'anon', 'PRACTICE_WORKER_ORIGIN': 'https://worker.example.workers.dev'}),
                          ('plain build', [], {})):
    out, stdout = build(extra, env)
    try:
        R = rules(open(os.path.join(out, '_headers')).read())
        ok('/practice/*' in R and '/practice' in R, label + ': /practice and /practice/* rules exist')
        for k in ('/practice', '/practice/*'):
            csp = header(R[k], 'Content-Security-Policy')
            ok(len(csp) == 1, label + ': one CSP on ' + k)
            c = csp[0]
            ok("default-src 'self'" in c and "script-src 'self';" in c and "'unsafe-inline'" not in c.split('style-src')[0], label + ': strict script-src on ' + k + ': ' + c)
            ok("frame-ancestors 'none'" in c and "object-src 'none'" in c and "base-uri 'self'" in c and "form-action 'self'" in c, label + ': framing/object/base/form locked')
            ok(re.search(r"connect-src 'self'( https://worker\.example\.workers\.dev)?;", c) is not None, label + ': connect-src is self (+ the Worker origin): ' + c)
            if 'PRACTICE_WORKER_ORIGIN' in env:
                ok('https://worker.example.workers.dev' in c, 'worker origin is in connect-src')
            else:
                ok('workers.dev' not in c, 'no stray origin without the env var')
            ok(header(R[k], 'Referrer-Policy') == ['Referrer-Policy: no-referrer'], label + ': Referrer-Policy no-referrer on ' + k)
            ok(header(R[k], 'Cache-Control') == ['Cache-Control: no-store'], label + ': no-store on ' + k)
        ok('/*' in R and not header(R['/*'], 'Content-Security-Policy') and not header(R['/*'], 'Referrer-Policy'), label + ': the /* rule carries no CSP and no Referrer-Policy (would be joined with the section rules)')
        ok(any(l.startswith('X-Frame-Options') for l in R['/*']) and any(l.startswith('X-Content-Type-Options') for l in R['/*']), label + ': common security headers stay on /*')
        for k in ('/', '/index.html', '/terms/*', '/privacy/*', '/shop/*'):
            ok(k in R and len(header(R[k], 'Content-Security-Policy')) == 1 and len(header(R[k], 'Referrer-Policy')) == 1, label + ': site path ' + k + ' has the site CSP and its Referrer-Policy')
        if '--with-portal' in extra:
            p = R['/portal/*']
            ok("script-src 'self';" in header(p, 'Content-Security-Policy')[0] and 'abcd.supabase.co' in header(p, 'Content-Security-Policy')[0] and header(p, 'Cache-Control') == ['Cache-Control: no-store'], '/portal/* keeps its strict CSP and no-store')
            ok(len(R) < 100, 'fewer than 100 header rules (Cloudflare limit): %d' % len(R))
            page = open(os.path.join(out, 'practice', 'holiday', 'p1', '03', 'index.html')).read()
            ok(re.search(r'<script>[^<]', page) is None and 'mi-inline-1.js' in page and 'type="application/ld+json">{"a":1}' in page, 'inline script moved to a file, data block left alone')
            ok('window.MI_LESSON="p1l03"' in open(os.path.join(out, 'practice', 'holiday', 'p1', '03', 'mi-inline-1.js')).read(), 'the moved script keeps its content')
            ok('--practice-dir' not in stdout and 'moved into mi-inline' in stdout, 'build notes say what was moved')
        else:
            ok('moved into mi-inline' not in stdout and 'strict CSP' in stdout, 'without --practice-dir the build notes warn about the inline config scripts')
    finally:
        shutil.rmtree(out, ignore_errors=True)
shutil.rmtree(prac, ignore_errors=True)
assert not os.path.exists(os.path.join(SITE, 'dist', 'practice', 'holiday')), 'website/dist must not have been touched'
print('headers_test: %d checks passed' % n)
