#!/usr/bin/env python3
"""The committed generated pages must be the flag-off (no teaser) pages while the teaser is not live.

    python3 website/teasers/test_flag_off.py            # exit 1 when a committed page differs from the flag-off generator output
    python3 website/teasers/test_flag_off.py --selftest # prove that the test fails when a page carries the teaser

website/mi_signup.html and website/level_pages/*.html are generated files (lp_build.py, level_pages.py).  build_site.py reads them as they are
committed, so a committed teaser-on page would go live with the next documented build even though manifest.json says "site_enabled": false.
The test copies website/ (without dist) to a scratch folder in /dev/shm (or the temp folder), runs both generators there WITHOUT MI_TEASERS, and compares
every generated file byte for byte with the committed one.  Nothing in the working tree is written, so nothing needs to be restored afterwards; the
other direction is checked as well: if manifest.json has "site_enabled": false, no committed page may contain the teaser code.
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
WEB = os.path.dirname(HERE)
ROOT = os.path.dirname(WEB)
GENERATED = ['mi_signup.html'] + ['level_pages/%s.html' % s for s in ('ages-6-8', 'ages-7-9', 'ages-8-10', 'ages-9-11', 'ages-10-12', 'ages-11-13')]
MARKERS = ('MiTeaser', 'pzdaily', 'pzBox')


def generate(scratch):
    """Copy website/ (no dist) to `scratch`/website and run the two generators without the teaser switch."""
    dst = os.path.join(scratch, 'website')
    shutil.copytree(WEB, dst, ignore=shutil.ignore_patterns('dist', '__pycache__', 'node_modules'))
    env = {k: v for k, v in os.environ.items() if k != 'MI_TEASERS'}
    for gen in ('lp_build.py', 'level_pages.py'):
        r = subprocess.run([sys.executable, gen], cwd=dst, env=env, capture_output=True, text=True)
        if r.returncode:
            raise RuntimeError('%s failed: %s' % (gen, r.stderr[-400:]))
    return dst


def compare(expected_dir, committed_dir):
    out = []
    for rel in GENERATED:
        a, b = os.path.join(expected_dir, rel), os.path.join(committed_dir, rel)
        if not os.path.exists(a) or not os.path.exists(b):
            out.append(('%s exists' % rel, False, 'missing'))
            continue
        same = open(a, 'rb').read() == open(b, 'rb').read()
        out.append(('committed %s equals the flag-off generator output' % rel, same, '' if same else 'differs'))
    return out


def check():
    """Returns [(name, ok, detail)]."""
    man = json.load(open(os.path.join(HERE, 'manifest.json'), encoding='utf-8'))
    results = []
    scratch = tempfile.mkdtemp(prefix='mi_flag_off_', dir='/dev/shm' if os.path.isdir('/dev/shm') else None)
    try:
        exp = generate(scratch)
        if man.get('site_enabled'):
            results.append(('manifest site_enabled is false (this test is for the not-live state)', False, 'site_enabled is true'))
        results += compare(exp, WEB)
    finally:
        shutil.rmtree(scratch, ignore_errors=True)
    if not man.get('site_enabled'):
        for rel in GENERATED:
            txt = open(os.path.join(WEB, rel), encoding='utf-8').read()
            hit = [m for m in MARKERS if m in txt]
            results.append(('committed %s has no teaser code while site_enabled is false' % rel, not hit, ','.join(hit)))
    # website/dist must be untouched by anything in this work
    try:
        st = subprocess.run(['git', 'status', '--porcelain', '--', 'website/dist'], cwd=ROOT, capture_output=True, text=True)
        if st.returncode == 0:
            results.append(('website/dist is untouched (git status is empty)', st.stdout.strip() == '', st.stdout.strip()[:200]))
    except OSError:
        pass
    return results


def selftest():
    """The comparison must fail for a page that carries the teaser, and pass for an identical copy."""
    scratch = tempfile.mkdtemp(prefix='mi_flag_off_self_', dir='/dev/shm' if os.path.isdir('/dev/shm') else None)
    try:
        exp = generate(scratch)
        alt = os.path.join(scratch, 'alt')
        shutil.copytree(exp, alt)
        good = all(ok for _, ok, _ in compare(exp, alt))
        p = os.path.join(alt, 'level_pages', 'ages-8-10.html')
        open(p, 'a', encoding='utf-8').write('<script>MiTeaser.init({})</script>')
        bad = [n for n, ok, _ in compare(exp, alt) if not ok]
        print('PASS identical pages compare equal' if good else 'FAIL identical pages compare equal')
        print('PASS a page with the teaser added is reported (%s)' % bad[0] if bad else 'FAIL a page with the teaser added is not reported')
        return 0 if good and bad else 1
    finally:
        shutil.rmtree(scratch, ignore_errors=True)


if __name__ == '__main__':
    if '--selftest' in sys.argv:
        sys.exit(selftest())
    res = check()
    for name, ok, extra in res:
        print(('PASS ' if ok else 'FAIL ') + name + ((' :: ' + extra) if extra and not ok else ''))
    bad = [n for n, ok, _ in res if not ok]
    print('%d checks, %d failed' % (len(res), len(bad)))
    sys.exit(1 if bad else 0)
