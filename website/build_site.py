#!/usr/bin/env python3
"""Assemble the deployable static site into website/dist/ .

    python3 lp_build.py && (cd hub && python3 build.py)   # regenerate the page sources first
    python3 build_site.py [--base https://example.com]

Takes the four page fragments (sign-up, parent questions hub, Weekly Dose online, referral is left out)
and wraps each in a full HTML document, self-hosts the Fredoka and Nunito Sans fonts (no request to Google),
drops the Claude preview meta tag, and writes robots.txt, sitemap.xml, 404.html, _headers and _redirects.
Nothing is invented: placeholders marked "to confirm" in the sources stay, and the build lists them.
"""
import os, re, shutil, sys, html

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DIST = os.path.join(HERE, 'dist')
FONTS = os.path.join(ROOT, 'fonts', 'node_modules', '@fontsource')
BASE = (sys.argv[sys.argv.index('--base') + 1] if '--base' in sys.argv else '').rstrip('/')

PAGES = [  # (source, output path, title, description)
    ('mi_signup.html', 'index.html', 'Math Inquirers Holiday Program',
     'Live online maths enrichment for children, in small groups of up to 8. Notice it. Test it. Explain why.'),
    ('hub/parent_questions.html', 'parent-questions/index.html', 'Parent questions about Primary maths',
     'Answers to common questions from Singapore parents about Primary maths, helping at home and stretching strong learners.'),
    ('terms.html', 'terms/index.html', 'Terms and refund policy',
     'Terms, fees and refund policy for the Math Inquirers November beta.'),
    ('privacy.html', 'privacy/index.html', 'Privacy and recording notice',
     'How Math Inquirers handles your details, lesson recordings and your child\'s work.'),
    ('weekly_dose_online.html', 'weekly-dose/index.html', 'Weekly Dose of Thinking Math online',
     'Sixty puzzles for children to try on screen, with hints and answers.'),
]
FONT_FILES = [('fredoka', 'fredoka', w, 'normal') for w in (500, 600)] + \
             [('nunito-sans', 'nunito-sans', w, s) for w in (400, 600, 700, 800) for s in ('normal', 'italic')]


def fonts_css():
    out = []
    for fam, pkg, w, style in FONT_FILES:
        fn = f'{pkg}-latin-{w}-{style}.woff2'
        shutil.copy(os.path.join(FONTS, pkg, 'files', fn), os.path.join(DIST, 'fonts', fn))
        name = 'Fredoka' if fam == 'fredoka' else 'Nunito Sans'
        out.append("@font-face{font-family:'%s';font-style:%s;font-weight:%d;font-display:swap;src:url('/fonts/%s') format('woff2')}" % (name, style, w, fn))
    return '\n'.join(out)


def wrap(src, title, desc, path):
    s = open(os.path.join(HERE, src), encoding='utf-8').read()
    s = s.replace('<!--STYLE-->', open(os.path.join(HERE, 'legal_style.txt'), encoding='utf-8').read())
    s = re.sub(r'<meta name="claude:[^>]*>\s*', '', s)
    s = re.sub(r'<link rel="preconnect"[^>]*>\s*', '', s)
    s = re.sub(r'<link rel="stylesheet" href="https://fonts\.googleapis\.com[^>]*>\s*', '', s)
    s = re.sub(r'<title>.*?</title>\s*', '', s, count=1, flags=re.S)
    s = re.sub(r'<meta name="description"[^>]*>\s*', '', s)
    canon = f'<link rel="canonical" href="{BASE}/{path.replace("index.html", "")}">' if BASE else ''
    head = ('<!doctype html>\n<html lang="en"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
            f'<title>{html.escape(title)}</title><meta name="description" content="{html.escape(desc)}">'
            f'<meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}">'
            '<meta property="og:type" content="website"><meta name="theme-color" content="#1B2A49">'
            '<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 32 32%27%3E%3Crect width=%2732%27 height=%2732%27 rx=%278%27 fill=%27%231B2A49%27/%3E%3Ctext x=%2716%27 y=%2724%27 font-size=%2722%27 text-anchor=%27middle%27 fill=%27%23FFD23F%27 font-family=%27sans-serif%27 font-weight=%27700%27%3E?%3C/text%3E%3C/svg%3E">'
            f'{canon}<link rel="stylesheet" href="/fonts.css"></head><body>\n')
    # sources start with <title>/<style> fragments; keep everything after the stripped head bits
    return head + s + '\n</body></html>\n'


def main():
    if os.path.isdir(DIST):
        shutil.rmtree(DIST)
    os.makedirs(os.path.join(DIST, 'fonts'))
    open(os.path.join(DIST, 'fonts.css'), 'w').write(fonts_css() + '\n')
    todo = []
    for src, out, title, desc in PAGES:
        page = wrap(src, title, desc, out)
        p = os.path.join(DIST, out)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        open(p, 'w', encoding='utf-8').write(page)
        for m in re.finditer(r'[^\n"<>]{0,60}\(?to confirm\)?[^\n"<>]{0,40}', page):
            todo.append((out, m.group(0).strip()))
        if 'class="draft"' in page:
            todo.append((out, 'draft banner for Jasmine still on the page'))
    open(os.path.join(DIST, '404.html'), 'w').write(
        '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
        '<title>Page not found | Math Inquirers</title><link rel="stylesheet" href="/fonts.css">'
        '<style>body{font:18px/1.5 "Nunito Sans",sans-serif;background:#FFF8E7;color:#1B2A49;display:grid;place-items:center;min-height:100vh;margin:0;text-align:center}'
        'h1{font:600 40px Fredoka,sans-serif}a{color:#1B2A49;font-weight:800}</style></head><body><main><h1>Hmm, that page is missing.</h1>'
        '<p>Notice it. Test it. Explain why.</p><p><a href="/">Back to Math Inquirers</a></p></main></body></html>\n')
    open(os.path.join(DIST, 'robots.txt'), 'w').write('User-agent: *\nAllow: /\n' + (f'Sitemap: {BASE}/sitemap.xml\n' if BASE else ''))
    if BASE:
        urls = ''.join(f'<url><loc>{BASE}/{o.replace("index.html", "")}</loc></url>' for _, o, _, _ in PAGES)
        open(os.path.join(DIST, 'sitemap.xml'), 'w').write(
            '<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + urls + '</urlset>\n')
    # _headers / _redirects work on Cloudflare Pages and Netlify
    open(os.path.join(DIST, '_headers'), 'w').write(
        '/*\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n  X-Frame-Options: DENY\n'
        "  Permissions-Policy: camera=(), microphone=(), geolocation=()\n"
        "  Content-Security-Policy: default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; font-src 'self'; connect-src 'self'; form-action 'self' https://wa.me; base-uri 'self'; frame-ancestors 'none'\n"
        '/fonts/*\n  Cache-Control: public, max-age=31536000, immutable\n')
    open(os.path.join(DIST, '_redirects'), 'w').write('/terms /terms/ 301\n/privacy /privacy/ 301\n/parent-questions /parent-questions/ 301\n/weekly-dose /weekly-dose/ 301\n')
    print('built', DIST)
    for p in sorted(os.listdir(DIST)):
        print(' ', p)
    print('\nTo confirm before launch:')
    for o, t in todo:
        print(f'  [{o}] {t}')


if __name__ == '__main__':
    main()
