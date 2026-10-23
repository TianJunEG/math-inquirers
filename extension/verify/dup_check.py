#!/usr/bin/env python3
"""Duplicate / overlap checker: every question text of the extension data against
  (1) the HOLIDAY program of the same level (hp/ for Level 1, pN/ for Levels 2-6)         -> FAIL on any shared 7-word run
  (2) EXTERNAL source texts (gitignored private files: docs/books/private_*/, docs/sasmo/private_*)  -> FAIL on any shared 7-word run
  (3) our own term lesson files (term/l1/lessons/*.json)                                    -> warning only (shared phrasing is fine, identical questions are not)
Also reports a 'skeleton' warning: same 7-word run after digits are masked (same sentence, new numbers) against the holiday bank; these are
expected for 'similar question types' but must be reviewed by a person (review list, not a failure).
Our own catalogues (docs/books/pN_non_routine_catalogue.md) are original and are NOT used as a source. Stock command phrases are listed
in verify/stock_phrases.txt and ignored (wording guide commands).
    python3 extension/verify/dup_check.py [--level 1] [--n 7]
"""
import argparse, glob, json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from common import EXT, ROOT   # noqa: E402


def toks(text, mask=False):
    t = text.lower().replace('’', "'")
    if mask:
        t = re.sub(r'\d+', '#', t)
    return re.findall(r"[a-z0-9#']+", t)


def grams(tokens, n):
    return {' '.join(tokens[i:i + n]) for i in range(len(tokens) - n + 1)}


def strip_markup(t):
    t = re.sub(r'\{circ:([^}]*)\}', lambda m: ' '.join(m.group(1).split('|')), t)
    return t.replace('{b}', ' ').replace('{l}', ' ')


def question_texts(unit):
    out = []
    L = unit['learn']
    out.append((unit['id'] + '-example', L['example']['problem']))
    out.append((unit['id'] + '-L01', L['try']['text']))
    for it in unit['items']:
        parts = [strip_markup(it['text'])] + [strip_markup(p['text']) for p in it.get('parts', [])]
        out.append((it['id'], ' . '.join(parts)))   # the period splits grams between stem and parts
    return out


def read_corpus(paths):
    txt = []
    for p in paths:
        try:
            raw = open(p, encoding='utf-8', errors='ignore').read()
        except OSError:
            continue
        if p.endswith('.html'):
            raw = re.sub(r'<[^>]+>', ' ', raw)
        txt.append(raw)
    return '\n'.join(txt)


def corpora(level):
    hol = []
    if level == 1:
        hol = [os.path.join(ROOT, 'hp', f) for f in ('qbank.json', 'lessons.js', 'gaps.json', 'workbook_body.html')]
        hol += glob.glob(os.path.join(ROOT, 'p1', '**', '*.js'), recursive=True)
    else:
        hol = glob.glob(os.path.join(ROOT, f'p{level}', 'content', '*.js')) + glob.glob(os.path.join(ROOT, f'p{level}', 'data.js')) + glob.glob(os.path.join(ROOT, f'p{level}', 'cdata.js'))
    ext = glob.glob(os.path.join(ROOT, 'docs', 'books', 'private_*', '**', '*'), recursive=True) + glob.glob(os.path.join(ROOT, 'docs', 'sasmo', 'private_*'))
    ext = [p for p in ext if os.path.isfile(p)]
    own = glob.glob(os.path.join(ROOT, 'term', f'l{level}', 'lessons', '*.json'))
    return {'holiday': hol, 'external': ext, 'term': own}


def stock(n):
    p = os.path.join(HERE, 'stock_phrases.txt')
    ph = set()
    if os.path.exists(p):
        for line in open(p, encoding='utf-8'):
            line = line.strip().lower()
            if line and not line.startswith('#'):
                ph |= grams(toks(line), n)
    return ph


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--level', type=int, default=1); ap.add_argument('--n', type=int, default=7)
    a = ap.parse_args()
    n = a.n
    files = sorted(glob.glob(os.path.join(EXT, 'data', f'l{a.level}_u*.json')))
    cs = corpora(a.level)
    sets, masked = {}, {}
    for k, paths in cs.items():
        raw = read_corpus(paths)
        sets[k] = grams(toks(raw), n); masked[k] = grams(toks(raw, True), n)
        print(f'corpus {k}: {len(paths)} files, {len(sets[k])} {n}-grams')
    if not cs['external']:
        print('WARNING: no external private source files found (docs/books/private_*, docs/sasmo/private_*): external check NOT run')
    ok = stock(n)
    fails, warns, review = [], [], []
    ntext = 0
    for f in files:
        unit = json.load(open(f, encoding='utf-8'))
        for qid, text in question_texts(unit):
            ntext += 1
            g = grams(toks(text), n) - ok
            gm = grams(toks(text, True), n) - ok
            for k, bad in (('holiday', True), ('external', True), ('term', False)):
                hit = g & sets[k]
                if hit:
                    (fails if bad else warns).append(f'{qid}: shares a {n}-word run with {k}: "{sorted(hit)[0]}"')
            hm = {x for x in (gm & masked['holiday']) - (g & sets['holiday']) if x.split().count('#') < 4}
            if hm:
                review.append(f'{qid}: same sentence skeleton as the holiday bank (numbers differ): "{sorted(hm)[0]}"')
    print(f'{ntext} question texts checked')
    for w in warns: print('WARN', w)
    for r in review: print('REVIEW', r)
    for x in fails: print('FAIL', x)
    print('OK (no shared runs with holiday or external sources)' if not fails else f'{len(fails)} FAIL')
    sys.exit(1 if fails else 0)


if __name__ == '__main__':
    main()
