#!/usr/bin/env python3
"""Similarity / duplicate check for the skill-gap items (Levels 1 to 3): same approach as extension/verify/dup_check.py.
Every item text (stem + parts) is compared, by shared runs of N consecutive words (default 7), with
  (1) the HOLIDAY program texts of all levels (hp/, pN/content, pN/data.js, gaps files, workbook html)   -> FAIL on a shared run
  (2) EXTERNAL source texts, if present on this machine (git-ignored docs/books/private_*, docs/sasmo/private_*) -> FAIL on a shared run
  (3) our own term lessons (term/l1/lessons/*.json)                                                      -> warning only
  (4) our extension data (extension/data/*.json)                                                         -> warning only
Also reports a 'skeleton' review line when the same N-word run appears after digits are masked (same sentence, new numbers) in the holiday bank.
The private files are only READ to compare; nothing from them is written anywhere.
    python3 rebuild/skill_items_dupcheck.py [--n 7]
"""
import argparse, glob, os, re, sys
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, H)
ROOT = os.path.join(H, '..')
from skill_items_l1_3 import ITEMS

STOCK = ['how many', 'in all', 'write the next two numbers', 'fill in the missing number', 'how do you know']


def toks(text, mask=False):
    t = text.lower().replace('’', "'")
    if mask: t = re.sub(r'\d+', '#', t)
    return re.findall(r"[a-z0-9#']+", t)


def grams(tokens, n): return {' '.join(tokens[i:i + n]) for i in range(len(tokens) - n + 1)}


def read(paths):
    out = []
    for p in paths:
        try: raw = open(p, encoding='utf-8', errors='ignore').read()
        except OSError: continue
        if p.endswith('.html'): raw = re.sub(r'<[^>]+>', ' ', raw)
        out.append(raw)
    return '\n'.join(out)


def corpora():
    hol = [os.path.join(ROOT, 'hp', f) for f in ('qbank.json', 'lessons.js', 'gaps.json', 'workbook_body.html', 'scripts.js')]
    for lv in range(1, 7):
        hol += glob.glob(os.path.join(ROOT, f'p{lv}', 'content', '*.js')) + [os.path.join(ROOT, f'p{lv}', f) for f in ('data.js', 'gaps.json', 'workbook_body.html')]
    hol += [f for f in glob.glob(os.path.join(ROOT, 'split', '*', 'project', 'slides', '*.html')) if '-skill' not in f and '-gap-' not in f]
    ext = [p for p in glob.glob(os.path.join(ROOT, 'docs', 'books', 'private_*', '**', '*'), recursive=True) + glob.glob(os.path.join(ROOT, 'docs', 'sasmo', 'private_*')) if os.path.isfile(p)]
    own = glob.glob(os.path.join(ROOT, 'term', 'l1', 'lessons', '*.json')) + glob.glob(os.path.join(ROOT, 'extension', 'data', '*.json'))
    return {'holiday': hol, 'external': ext, 'own (term/extension)': own}


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--n', type=int, default=7); n = ap.parse_args().n
    cs = corpora(); sets = {}; masked = {}
    for k, ps in cs.items():
        raw = read(ps); sets[k] = grams(toks(raw), n); masked[k] = grams(toks(raw, True), n)
        print(f'corpus {k}: {len(ps)} files, {len(sets[k])} {n}-grams')
    if not cs['external']: print('WARNING: no private external sources found: external check NOT run')
    ok = set().union(*[grams(toks(s), n) for s in STOCK]) if all(len(toks(s)) >= n for s in STOCK) else set()
    fails, warns, review = [], [], []
    for it in ITEMS:
        text = ' . '.join([it['stem']] + it['parts'])
        g = grams(toks(text), n) - ok; gm = grams(toks(text, True), n) - ok
        for k, bad in (('holiday', True), ('external', True), ('own (term/extension)', False)):
            hit = g & sets[k]
            if hit: (fails if bad else warns).append(f"{it['id']}: shares a {n}-word run with {k}: \"{sorted(hit)[0]}\"")
        hm = {x for x in (gm & masked['holiday']) - (g & sets['holiday']) if x.split().count('#') < 4}
        if hm: review.append(f"{it['id']}: same sentence skeleton as the holiday texts (numbers differ): \"{sorted(hm)[0]}\"")
    print(len(ITEMS), 'item texts checked')
    for w in warns: print('WARN', w)
    for r in review: print('REVIEW', r)
    for f in fails: print('FAIL', f)
    print('OK: no shared run with holiday or external sources' if not fails else f'{len(fails)} FAIL')
    sys.exit(1 if fails else 0)


if __name__ == '__main__':
    main()
