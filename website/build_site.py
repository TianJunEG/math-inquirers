#!/usr/bin/env python3
"""Assemble the deployable static site into website/dist/ .

    python3 lp_build.py && python3 level_pages.py && python3 shop_build.py && (cd hub && python3 build.py)   # regenerate the page sources first
    python3 build_site.py [--base https://example.com] [--with-portal] [--practice-dir DIR] [--out DIR]   # --with-portal also copies ../portal/public to dist/portal/
                                                                                                     # --practice-dir DIR copies DIR to dist/practice/ and moves inline scripts into files (strict CSP)

Takes the four page fragments (sign-up, parent questions hub, Weekly Dose online, referral is left out)
and wraps each in a full HTML document, self-hosts the Fredoka and Nunito Sans fonts (no request to Google),
drops the Claude preview meta tag, and writes robots.txt, sitemap.xml, 404.html, _headers and _redirects.
Nothing is invented: placeholders marked "to confirm" in the sources stay, and the build lists them.
"""
import os, re, shutil, sys, html

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DIST = os.path.abspath(sys.argv[sys.argv.index('--out') + 1]) if '--out' in sys.argv else os.path.join(HERE, 'dist')   # --out DIR builds somewhere else (previews); the default is dist/
FONTS = os.path.join(ROOT, 'fonts', 'node_modules', '@fontsource')
WITH_PORTAL = '--with-portal' in sys.argv or os.environ.get('MI_PORTAL') == '1'   # opt-in: copies ../portal/public to dist/portal
PORTAL_SRC = os.path.join(ROOT, 'portal', 'public')
SB_URL = os.environ.get('SUPABASE_URL', '').rstrip('/')
SB_KEY = os.environ.get('SUPABASE_ANON_KEY', '')
# The home page "Request another time" form saves to Supabase only in a --with-portal build that has real (public) values; otherwise it
# falls back to a prefilled WhatsApp message and the page loads no config and makes no network call.
INTEREST_PORTAL = WITH_PORTAL and bool(SB_URL and SB_KEY) and re.fullmatch(r'https://[a-z0-9-]+\.supabase\.co', SB_URL) is not None
BASE = (sys.argv[sys.argv.index('--base') + 1] if '--base' in sys.argv else '').rstrip('/')
# PRIVATE PREVIEW (default until launch): ask search engines not to index or archive the site (robots.txt Disallow, X-Robots-Tag header, robots meta).
# Build with --public (or MI_PUBLIC=1) at launch to allow indexing and write the sitemap. This is only a stopgap: it does not stop anyone who has the link.
PUBLIC = '--public' in sys.argv or os.environ.get('MI_PUBLIC') == '1'
# Practice pages (/practice/*) read the child's sign-in token from sessionStorage and send answers to the Worker. They get their OWN strict headers (see main()):
# script-src 'self' only, so a script injected into any page cannot run, plus connect-src 'self' and, if the Worker lives on another origin, that one origin.
PRACTICE_DIR = os.path.abspath(sys.argv[sys.argv.index('--practice-dir') + 1]) if '--practice-dir' in sys.argv else None
PRACTICE_ORIGIN = os.environ.get('PRACTICE_WORKER_ORIGIN', '').rstrip('/')
if not re.fullmatch(r'https://[a-z0-9.-]+(:[0-9]{2,5})?', PRACTICE_ORIGIN):
    PRACTICE_ORIGIN = ''

INLINE_SCRIPT = re.compile(r'<script(?![^>]*\bsrc=)(?![^>]*\btype=["\'](?!text/javascript|module))([^>]*)>(.*?)</script>', re.S | re.I)

def externalize_inline_scripts(root):
    """Strict CSP (script-src 'self') blocks <script>...</script> bodies. For every HTML file under root, move each inline script into a file next to the page
    (mi-inline-1.js, mi-inline-2.js ...) and point a <script src> at it, in the same position, so execution order is unchanged. Returns the number of scripts moved."""
    n = 0
    for dp, _, files in os.walk(root):
        for f in files:
            if not f.endswith('.html'):
                continue
            p = os.path.join(dp, f); page = open(p, encoding='utf-8').read(); k = [0]
            def move(m):
                if not m.group(2).strip():
                    return m.group(0)
                k[0] += 1; name = 'mi-inline-%d.js' % k[0]
                open(os.path.join(dp, name), 'w', encoding='utf-8').write(m.group(2).strip() + '\n')
                return '<script src="%s"></script>' % name
            new = INLINE_SCRIPT.sub(move, page)
            if k[0]:
                open(p, 'w', encoding='utf-8').write(new); n += k[0]
    return n

PAGES = [  # (source, output path, title, description)
    ('mi_signup.html', 'index.html', 'Math Inquirers Holiday Program',
     'Live online maths enrichment for children, in small groups of up to 8. Notice it. Test it. Explain why.'),
    ('hub/parent_questions.html', 'parent-questions/index.html', 'Parent questions about Primary maths',
     'Answers to common questions from Singapore parents about Primary maths, helping at home and stretching strong learners.'),
    ('terms.html', 'terms/index.html', 'Terms and refund policy',
     'Terms, fees and refund policy for the Math Inquirers November beta.'),
    ('privacy.html', 'privacy/index.html', 'Privacy and recording notice',
     'How Math Inquirers handles your details, lesson recordings and your child\'s work.'),
    ('shop/shop.html', 'shop/index.html', 'Shop: extension workbooks coming soon',
     'Extension workbooks for Math Inquirers Levels 1 to 6, coming soon. Add what you want to your list and we will tell you when it is ready.'),
    ('weekly_dose_online.html', 'weekly-dose/index.html', 'Weekly Dose of Thinking Math online',
     'Sixty puzzles for children to try on screen, with hints and answers.'),
]
# six per-level pages, generated by level_pages.py (python3 level_pages.py) into level_pages/
from level_pages import LEVELS, register_by
import json
import shop_build
sys.path.insert(0, os.path.join(HERE, 'teasers'))
import teaser_html as TH   # daily teaser batches (copied only when the teaser is enabled)
_SHOP_PRODUCTS, SHOP_WARNINGS = shop_build.load()   # data/products.json; any price_cents is reported in the build notes
REGBY_LABEL, REGBY_SET = register_by(json.load(open(os.path.join(HERE, 'data', 'beta_schedule.json'), encoding='utf-8')))
for _L in LEVELS:
    PAGES.append(('level_pages/%s.html' % _L['slug'], '%s/index.html' % _L['slug'],
                  'Ages %s maths holiday program' % _L['ages'],
                  'Math Inquirers Level %d for ages %s, building on %s: ten live online lessons, kit, placement guidance and November beta class times.' % (_L['n'], _L['ages'], _L['builds'])))
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
    s = s.replace('<!--REGBY-->', ('<b>%s</b>' % REGBY_LABEL) if REGBY_SET else '<span class="ph">%s</span>' % REGBY_LABEL)
    s = s.replace('<!--PORTAL_CONFIG-->', '<script src="/portal/config.js"></script>' if INTEREST_PORTAL else '')
    s = re.sub(r'<meta name="claude:[^>]*>\s*', '', s)
    s = re.sub(r'<link rel="preconnect"[^>]*>\s*', '', s)
    s = re.sub(r'<link rel="stylesheet" href="https://fonts\.googleapis\.com[^>]*>\s*', '', s)
    s = re.sub(r'<title>.*?</title>\s*', '', s, count=1, flags=re.S)
    s = re.sub(r'<meta name="description"[^>]*>\s*', '', s)
    canon = f'<link rel="canonical" href="{BASE}/{path.replace("index.html", "")}">' if BASE else ''
    head = ('<!doctype html>\n<html lang="en"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
            f'<title>{html.escape(title)}</title><meta name="description" content="{html.escape(desc)}">' + ('' if PUBLIC else '<meta name="robots" content="noindex,nofollow,noarchive">') +
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
    # shop: page source is generated by shop_build.py (data/products.json); the cart, page and checkout-stub scripts and Mi are static files
    for f in ('cart.js', 'shop.js', 'checkout.js', 'mi.png'):
        shutil.copy(os.path.join(HERE, 'shop', f), os.path.join(DIST, 'shop', f))
    # product names only (no prices, no notes): the portal admin 'Shop interest' tab reads this to show names instead of ids
    json.dump({p['id']: p['name'] for p in _SHOP_PRODUCTS}, open(os.path.join(DIST, 'shop-products.json'), 'w', encoding='utf-8'), indent=1)
    if TH.enabled():
        todo.append(('teasers/', 'Daily teaser files written: %d (released months %s)' % (TH.export_public(DIST), ', '.join(TH.released()))))
    # third-party licence notices (SIL OFL texts for the shipped fonts): must travel with the font files
    shutil.copytree(os.path.join(HERE, 'licenses'), os.path.join(DIST, 'licenses'))
    # syllabus map is a self-contained full document: copy it, do not wrap it
    os.makedirs(os.path.join(DIST, 'syllabus'), exist_ok=True)
    shutil.copy(os.path.join(HERE, 'syllabus', 'index.html'), os.path.join(DIST, 'syllabus', 'index.html'))
    open(os.path.join(DIST, '404.html'), 'w').write(
        '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
        '<title>Page not found | Math Inquirers</title><meta name="robots" content="noindex"><link rel="stylesheet" href="/fonts.css">'
        '<style>:root{--bg:#FFF8E7;--fg:#1B2A49}@media (prefers-color-scheme:dark){:root{--bg:#101a30;--fg:#f3efe2}}'
        'body{font:18px/1.5 "Nunito Sans",sans-serif;background:var(--bg);color:var(--fg);display:grid;place-items:center;min-height:100vh;margin:0;padding:16px;text-align:center}'
        'h1{font:600 clamp(28px,7vw,40px) Fredoka,sans-serif;margin:8px 0}p{margin:10px 0}img{display:block;margin:0 auto}'
        'a{color:inherit;font-weight:800;display:inline-block;padding:10px 8px;min-height:44px}a:focus-visible{outline:3px solid #C9372C;outline-offset:2px}</style></head>'
        '<body><main><img src="/shop/mi.png" width="126" height="150" alt="Mi the dolphin"><h1>Hmm, we cannot find that page.</h1>'
        '<p>The link may be old or mistyped. Here is where to go next.</p>'
        '<p><a href="/">Math Inquirers home</a> · <a href="/#levels">Choose a level</a> · <a href="/shop/">Shop</a> · <a href="/parent-questions/">Parent questions</a></p></main></body></html>\n')
    # placeholder slot labels (public data, no personal data): the portal admin Interest tab reads this to show names instead of ids
    shutil.copy(os.path.join(HERE, 'data', 'interest_slots.json'), os.path.join(DIST, 'interest-slots.json'))
    open(os.path.join(DIST, 'robots.txt'), 'w').write(('User-agent: *\nAllow: /\n' + (f'Sitemap: {BASE}/sitemap.xml\n' if BASE else '')) if PUBLIC else 'User-agent: *\nDisallow: /\n')
    if BASE and PUBLIC:
        urls = ''.join(f'<url><loc>{BASE}/{o.replace("index.html", "")}</loc></url>' for _, o, _, _ in PAGES) + f'<url><loc>{BASE}/syllabus/</loc></url>'
        open(os.path.join(DIST, 'sitemap.xml'), 'w').write(
            '<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + urls + '</urlset>\n')
    # _headers / _redirects work on Cloudflare Pages and Netlify
    # Cloudflare JOINS the same header from every matching rule, so a header that differs between sections (Referrer-Policy) is NOT in the /* block: each
    # section (site pages, /portal/*, /practice/*) states its own once.
    sec = ('  X-Content-Type-Options: nosniff\n  X-Frame-Options: DENY\n'
           "  Permissions-Policy: camera=(), microphone=(), geolocation=()\n")
    referrer = '  Referrer-Policy: strict-origin-when-cross-origin\n'
    if not PUBLIC:
        sec += '  X-Robots-Tag: noindex, nofollow, noarchive\n'
    site_csp = ("  Content-Security-Policy: default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; font-src 'self'; connect-src 'self'; form-action 'self' https://wa.me; base-uri 'self'; frame-ancestors 'none'\n")
    if INTEREST_PORTAL:   # the site pages (not only /portal/*) may POST the interest form to the Supabase origin
        site_csp = site_csp.replace("connect-src 'self';", "connect-src 'self' %s;" % SB_URL)
    # Cloudflare joins the same header from every matching rule, so two CSPs would BOTH apply. /portal/* and /practice/* therefore must not
    # match the site-wide CSP rule: the common security headers stay on /*, the site CSP (and Referrer-Policy) is listed per site path.
    hdr = '/*\n' + sec
    tops = sorted({o.split('/')[0] for _, o, _, _ in PAGES if o != 'index.html'} | {'syllabus'})
    for pth in ['/', '/index.html', '/404.html'] + [p for t in tops for p in ('/%s' % t, '/%s/*' % t)]:
        hdr += pth + '\n' + referrer + site_csp
    # /practice/*: the child's sign-in token is read here and answers are sent from here. Strict: no inline script (script-src 'self'; the generators' inline
    # config script is moved to a file by externalize_inline_scripts), no object/embed, no framing, no form posts off-site, connect only to this origin (+ the
    # Worker origin if it is a different one: PRACTICE_WORKER_ORIGIN), never send a Referer, never cache (a shared tablet must not keep a page that held a token).
    # style-src keeps 'unsafe-inline' because the pages carry inline style attributes (no script can come from a style).
    practice_hdr = ("  Content-Security-Policy: default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; font-src 'self'; "
                    "connect-src 'self'%s; object-src 'none'; form-action 'self'; base-uri 'self'; frame-ancestors 'none'\n"
                    "  Referrer-Policy: no-referrer\n  Cache-Control: no-store\n") % ((' ' + PRACTICE_ORIGIN) if PRACTICE_ORIGIN else '')
    hdr += '/practice\n' + practice_hdr + '/practice/*\n' + practice_hdr
    if not WITH_PORTAL:
        hdr += '/fonts/*\n  Cache-Control: public, max-age=31536000, immutable\n'
    else:
        origin = os.environ.get('SUPABASE_URL', '').rstrip('/')
        origin = origin if re.fullmatch(r'https://[a-z0-9-]+\.supabase\.co', origin) else 'https://*.supabase.co'
        # Stripe needs no entry: the Pay button calls our own /api/stripe-create-checkout ('self') and then does a top-level navigation
        # (location.href) to checkout.stripe.com, which connect-src, form-action and frame-src do not govern. We use Stripe-hosted Checkout,
        # not Stripe.js or an embedded element, so js.stripe.com is NOT allowed. Card/PayNow details never touch our pages.
        # If an embedded Stripe element is ever added, script-src/frame-src/connect-src must be widened deliberately (js.stripe.com, api.stripe.com).
        hdr += ('/portal/*\n  Content-Security-Policy: default-src \'self\'; script-src \'self\'; style-src \'self\' \'unsafe-inline\'; img-src \'self\' data:; font-src \'self\'; '
                'connect-src \'self\' %s; form-action \'self\'; base-uri \'self\'; frame-ancestors \'none\'\n  Referrer-Policy: strict-origin-when-cross-origin\n  Cache-Control: no-store\n' % origin)
        hdr += '/fonts/*\n  Cache-Control: public, max-age=31536000, immutable\n'
    if TH.enabled():   # per-level, per-month teaser files are static JSON; one hour of caching so a new month shows up promptly
        hdr += '/teasers/*\n  Cache-Control: public, max-age=3600\n'
    open(os.path.join(DIST, '_headers'), 'w').write(hdr)
    if PRACTICE_DIR:   # optional: bring the built practice pages into the site and make them satisfy the strict CSP above
        shutil.copytree(PRACTICE_DIR, os.path.join(DIST, 'practice'))
        todo.append(('practice/', 'Practice pages copied from %s; %d inline script(s) moved into mi-inline-N.js files so script-src \'self\' holds' % (PRACTICE_DIR, externalize_inline_scripts(os.path.join(DIST, 'practice')))))
    else:
        todo.append(('practice/', "_headers gives /practice/* a strict CSP (script-src 'self'). The practice generators currently write one inline <script>window.MI_LESSON=...</script> per page, which that CSP blocks: build with --practice-dir DIR (moves it into a file), or change the generators, before the practice pages go live"))
    if WITH_PORTAL:
        shutil.copytree(PORTAL_SRC, os.path.join(DIST, 'portal'))
        url, key = os.environ.get('SUPABASE_URL', ''), os.environ.get('SUPABASE_ANON_KEY', '')
        cfg = os.path.join(DIST, 'portal', 'config.js')
        if url and key:   # both values are public by design; the service_role key must never be set for this build
            c = open(cfg, encoding='utf-8').read().replace("'SUPABASE_URL'", repr(url)).replace("'ANON_KEY'", repr(key))
            for env_name, ph in (('PORTAL_PAYMENT_MODE', "PAYMENT_MODE: 'paynow_manual'"), ('PORTAL_PAYNOW_TO', "PAYNOW_TO: 'PayNow number or UEN (to confirm)'")):
                if os.environ.get(env_name):
                    c = c.replace(ph, ph.split(':')[0] + ': ' + repr(os.environ[env_name]))
            open(cfg, 'w', encoding='utf-8').write(c)
        else:
            todo.append(('portal/config.js', 'SUPABASE_URL / ANON_KEY still placeholders (set env SUPABASE_URL and SUPABASE_ANON_KEY for the build)'))
    open(os.path.join(DIST, '_redirects'), 'w').write('/shop /shop/ 301\n/syllabus /syllabus/ 301\n/terms /terms/ 301\n/privacy /privacy/ 301\n/parent-questions /parent-questions/ 301\n/weekly-dose /weekly-dose/ 301\n'
                                                  + ''.join('/%s /%s/ 301\n' % (L['slug'], L['slug']) for L in LEVELS))
    todo.append(('payments', 'Payment gateway is STRIPE (owner decision, replaces HitPay). Beta default stays manual PayNow (PORTAL_PAYMENT_MODE unset = paynow_manual). To go online: follow the Stripe checklist in portal/README.md, review and apply portal/supabase/stripe_migration.sql, set Cloudflare secrets STRIPE_SECRET_KEY / STRIPE_WEBHOOK_SECRET / SUPABASE_SERVICE_ROLE_KEY, test in Stripe test mode, then set PORTAL_PAYMENT_MODE=stripe. Fees: check Stripe\'s current Singapore pricing (not stated anywhere on the site).'))
    todo.append(('terms.html / privacy.html', 'Stripe wording is a draft for the lawyer: Stripe as payment processor, card details handled by Stripe and never stored by us, possible processing outside Singapore (see the [bracket] notes); who is the PDPA data intermediary/controller for payment data'))
    todo.append(('index.html', 'Request-another-time form: retention default (12 months) and consent wording are drafts for the owner/lawyer; privacy.html carries the matching [bracket] note. Placeholder slots live in data/interest_slots.json.'))
    todo.append(('index.html', 'Request-another-time form mode: ' + ('saves to Supabase (submit_interest_request); apply portal/supabase/interest_requests.sql first' if INTEREST_PORTAL else 'WhatsApp fallback only (build with --with-portal and SUPABASE_URL/SUPABASE_ANON_KEY to save requests)')))
    todo.append(('shop/', 'Shop: all products are COMING SOON with NO prices (owner: prices on hold). Interest form mode: ' + ('saves to Supabase (submit_product_interest); review and apply portal/supabase/product_interest.sql first' if INTEREST_PORTAL else 'WhatsApp fallback only') + '. Consent wording and 12-month retention are drafts for the owner/lawyer (privacy.html (product interest rows) carries the [bracket] note). Checkout is a stub (shop/checkout.js): hidden until a product is available with a price and the Stripe /api/shop/checkout function exists.'))
    for w in SHOP_WARNINGS:
        todo.append(('shop/', 'PRICE WARNING: ' + w))
    for t in ('[register-by date] not set: set delivery.register_by once in data/beta_schedule.json (shown on the home page, level pages, terms and the FAQ); default: order the print run by about 9 Nov for a 24 Nov start, from the printer lead time' if not REGBY_SET else None,
              '[who pays printing/postage] CONFIRMED by owner 23 Oct: included in the S$250 beta fee (nothing to do)',
              '[parcel policy] draft default: report within 7 days, we reprint and resend once at no cost; a lawyer to confirm (terms.html section 3, home FAQ)',
              '[address retention] draft default: delivery name/address/phone deleted 30 days after the parcel is confirmed delivered, or after any resend is finished, whichever is later (owner decision 23 Oct); lawyer to confirm; also name the printer and courier in privacy.html',
              'delivery fields (address, postal code, parcel phone) and the delivery consent are on the WhatsApp registration form only; the portal sign-up does not collect them yet (see portal/README.md)'):
        if t:
            todo.append(('delivery', t))
    print('built', DIST)
    for p in sorted(os.listdir(DIST)):
        print(' ', p)
    print('\nTo confirm before launch:')
    for o, t in todo:
        print(f'  [{o}] {t}')


if __name__ == '__main__':
    main()
