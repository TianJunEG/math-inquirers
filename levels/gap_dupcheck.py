"""7-word-run duplicate check of levels/gap_items.py question texts (logic copied from extension/verify/dup_check.py).
Checks each item (question lines, and the variant question) against: the HOLIDAY text of every level (hp/, p1..p6 content/data), our term lessons,
the extension data, and the git-ignored PRIVATE source files (docs/sasmo/private_*, docs/books/private_*) if present. A hit in a private file prints only
the file name and the hit count, never the matching words. Stock command phrases (extension/verify/stock_phrases.txt) are ignored.
    python3 levels/gap_dupcheck.py [--n 7]       exit 1 on any shared run with holiday, extension, term or private text"""
import argparse, glob, json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.join(HERE, '..')
sys.path.insert(0, HERE)
import gap_items
def toks(t): return re.findall(r"[a-z0-9']+", t.lower().replace('’', "'"))
def grams(tk, n): return {' '.join(tk[i:i + n]) for i in range(len(tk) - n + 1)}
def read(paths):
    out = []
    for p in paths:
        try: raw = open(p, encoding='utf-8', errors='ignore').read()
        except OSError: continue
        if p.endswith('.html'): raw = re.sub(r'<[^>]+>', ' ', raw)
        out.append(raw)
    return '\n'.join(out)
def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--n', type=int, default=7); n = ap.parse_args().n
    G = lambda *pat: [f for pp in pat for f in glob.glob(os.path.join(ROOT, pp), recursive=True) if os.path.isfile(f)]
    holiday = G('hp/qbank.json', 'hp/lessons.js', 'hp/gaps.json', 'hp/*.js', 'p[1-6]/content/*.js', 'p[1-6]/data.js', 'p[1-6]/cdata.js', 'p[1-6]/*.js', 'p1/**/*.js')
    sources = {'holiday': holiday, 'term': G('term/l*/lessons/*.json'), 'extension': G('extension/data/*.json'),
               'private': G('docs/sasmo/private_*', 'docs/books/private_*/**/*', 'docs/books/private_*')}
    sets = {}
    for k, ps in sources.items():
        sets[k] = grams(toks(read(ps)), n); print(f'corpus {k}: {len(ps)} files, {len(sets[k])} {n}-grams')
    if not sources['private']: print('WARNING: no private source files found; private check NOT run')
    ok = set()
    sp = os.path.join(ROOT, 'extension', 'verify', 'stock_phrases.txt')
    if os.path.exists(sp):
        for line in open(sp, encoding='utf-8'):
            line = line.strip().lower()
            if line and not line.startswith('#'): ok |= grams(toks(line), n)
    bad = 0; nt = 0
    for it in gap_items.ITEMS:
        texts = [(f"{it['lv']}:{it['id']}", ' . '.join(it['q']))]
        if it.get('var'): texts.append((f"{it['lv']}:{it['id']}:var", it['var'][0]))
        for tid, t in texts:
            nt += 1; g = grams(toks(t), n) - ok
            for k, st in sets.items():
                hit = g & st
                if hit:
                    bad += 1
                    print(f'FAIL {tid}: shares {len(hit)} {n}-word run(s) with {k}' + ('' if k == 'private' else f': "{sorted(hit)[0]}"'))
    print(f'{nt} texts checked against {sum(len(v) for v in sources.values())} files'); print('OK: no shared run' if not bad else f'{bad} hit(s)')
    sys.exit(1 if bad else 0)
if __name__ == '__main__': main()
