#!/usr/bin/env python3
"""Independent verification of the released teaser batches.

    python3 website/teasers/verify_bank.py            # all months in manifest.json
    python3 website/teasers/verify_bank.py 11 12      # chosen months

For every puzzle: re-solve with brute.py (never imports kinds.py), require exactly ONE valid answer equal to the
bank's answer; check the arithmetic written in the question/hint/explanation; frames unique per level across ALL
released months; wording rules; similarity to holiday, term, extension and external sources.
Writes batches/m<MM>/VERIFY_REPORT.md.  Exit code 1 on any FAIL.
"""
import glob
import json
import os
import re
import sys
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, 'extension', 'verify'))
import brute                                    # noqa: E402

try:
    import dup_check                            # noqa: E402
except Exception as e:                          # pragma: no cover
    dup_check = None
    print('dup_check not importable:', e)

NG = 7          # same rule as extension/verify/dup_check.py: a shared run of 7 words is a FAIL
MAXQ = {1: 48, 2: 55, 3: 65, 4: 75, 5: 85, 6: 95}      # words in a question
MAXSENT = {1: 20, 2: 22, 3: 26, 4: 30, 5: 34, 6: 38}   # words in a sentence
US = re.compile(r'\b(color|meter|liter|kilometer|centimeter|math)\b|\bmaths?\b', re.I)
BAD = re.compile(r'picture|image|photo|specimen|coin art|note art|look at the coin|[\U0001F300-\U0001FAFF]')
NUM = re.compile(r'\d[\d,]*\.?\d*')


def flat(x, out):
    if isinstance(x, (list, tuple)):
        for y in x:
            flat(y, out)
    elif isinstance(x, bool) or x is None:
        pass
    elif isinstance(x, (int, float)):
        out.add(str(x))
    elif isinstance(x, str):
        out.update(re.findall(r'\d+', x))
    elif isinstance(x, dict):
        for y in x.values():
            flat(y, out)


def norm_num(s):
    return s.replace(',', '').rstrip('.')


def check_arith(text):
    """Evaluate every 'a op b ... = c' chain written in the text."""
    bad = []
    t = text.replace('×', '*').replace('÷', '/').replace('−', '-').replace('$', '')
    for m in re.finditer(r'(?<![\w.])((?:\(?\d[\d,]*\.?\d*\)?\s*[-+*/]\s*)+\(?\d[\d,]*\.?\d*\)?)\s*=\s*(\d[\d,]*\.?\d*)', t):
        lhs, rhs = m.group(1).replace(',', ''), m.group(2).replace(',', '')
        try:
            v = eval(re.sub(r'(\d+\.?\d*)', r'Fr("\1")', lhs), {'Fr': Fr})
        except Exception:
            continue
        if v != Fr(rhs):
            bad.append(m.group(0))
    return bad


def toks(t):
    return re.findall(r"[a-z0-9#']+", re.sub(r'\d+', '#', t.lower().replace('’', "'")))


def main():
    man = json.load(open(os.path.join(HERE, 'manifest.json')))
    months = sys.argv[1:] or man['released']
    banks = {}
    for mm in man['released']:
        banks[mm] = json.load(open(os.path.join(HERE, 'batches', 'm%s' % mm, 'bank.json'), encoding='utf-8'))
    fails_all = 0
    # corpora for similarity
    corp = {}
    if dup_check:
        for lv in range(1, 7):
            cs = dup_check.corpora(lv)
            corp[lv] = {k: dup_check.grams(dup_check.toks(dup_check.read_corpus(v)), NG) for k, v in cs.items()}
            corp[lv]['_ext_missing'] = not cs['external']
        ext_texts = []
        for f in glob.glob(os.path.join(ROOT, 'extension', 'data', 'l*_u*.json')):
            try:
                ext_texts.append(' . '.join(t for _, t in dup_check.question_texts(json.load(open(f, encoding='utf-8')))))
            except Exception:
                pass
        ext_grams = dup_check.grams(dup_check.toks(' . '.join(ext_texts)), NG)
        stock = dup_check.stock(NG)
    seen_frames = {lv: {} for lv in range(1, 7)}
    seen_q = {lv: {} for lv in range(1, 7)}
    for mm in man['released']:
        for lv, items in banks[mm]['levels'].items():
            for e in items:
                if e['frame'] in seen_frames[int(lv)]:
                    print('FAIL frame repeated in level %s: %s (%s and %s)' % (lv, e['frame'], seen_frames[int(lv)][e['frame']], mm))
                    fails_all += 1
                seen_frames[int(lv)][e['frame']] = mm
    for mm in months:
        fails, reviews, lines = [], [], []
        stats = {}
        for lv, items in banks[mm]['levels'].items():
            lv = int(lv)
            kinds_ct, topics = {}, {}
            dates = [e['date'] for e in items]
            if len(set(dates)) != len(dates):
                fails.append('L%d duplicate dates' % lv)
            for e in items:
                tag = '%s [%s]' % (e['id'], e['date'])
                # 1. independent solve
                try:
                    sols = brute.BRUTE[e['kind']](**e['p'])
                except Exception as ex:
                    fails.append('%s: brute-force crashed: %r' % (tag, ex))
                    continue
                if e['type'] == 's':
                    got = {str(s).lower() for s in sols}
                    want = {e['ans']}
                else:
                    got = {Fr(s) for s in sols}
                    want = {Fr(e['ans'])}
                if len(got) != 1:
                    fails.append('%s: %d valid answers found by brute force: %s' % (tag, len(got), sorted(map(str, got))[:6]))
                elif got != want:
                    fails.append('%s: brute force says %s but bank says %s' % (tag, got, want))
                if e['type'] == 'n' and any(Fr(w) == Fr(e['ans']) for w in e['wrong'] if re.fullmatch(r'[\d./]+', w)):
                    fails.append('%s: a listed wrong answer equals the answer' % tag)
                # 2. wording
                words = len(e['q'].split())
                sents = [len(s.split()) for s in re.split(r'(?<=[.?!])\s+', e['q']) if s.strip()]
                if words > MAXQ[lv]:
                    reviews.append('%s: question has %d words (limit %d)' % (tag, words, MAXQ[lv]))
                if sents and max(sents) > MAXSENT[lv]:
                    reviews.append('%s: longest sentence %d words (limit %d)' % (tag, max(sents), MAXSENT[lv]))
                for fld in ('q', 'hint', 'why'):
                    if US.search(e[fld]):
                        fails.append('%s: non-Singapore spelling/word in %s: %s' % (tag, fld, US.search(e[fld]).group(0)))
                    if BAD.search(e[fld]):
                        fails.append('%s: forbidden word in %s: %s' % (tag, fld, BAD.search(e[fld]).group(0)))
                    for b in check_arith(e[fld]):
                        fails.append('%s: arithmetic in %s is wrong: %s' % (tag, fld, b))
                if e['ans'].lower() in e['hint'].lower().split() and e['type'] == 's':
                    fails.append('%s: hint gives the answer away' % tag)
                if e['type'] == 'n' and re.search(r'(?<![\d.,])' + re.escape(e['ans']) + r'(?![\d.,])', e['hint']):
                    reviews.append('%s: hint contains the answer number %s' % (tag, e['ans']))
                # 3. numbers in the question should come from the parameters
                known = set()
                flat(e['p'], known)
                flat(e['t'], known)
                for n in NUM.findall(e['q']):
                    n = norm_num(n)
                    if n not in known and n.replace('.', '') not in known:
                        reviews.append('%s: number %s in the question is not a parameter (written in the wording; check)' % (tag, n))
                if e['q'] in seen_q[lv]:
                    fails.append('%s: same question text as %s' % (tag, seen_q[lv][e['q']]))
                seen_q[lv][e['q']] = tag
                kinds_ct[e['kind']] = kinds_ct.get(e['kind'], 0) + 1
                topics[e['topic']] = topics.get(e['topic'], 0) + 1
                # 4. similarity (6-word runs) with other sources
                if dup_check:
                    g = dup_check.grams(dup_check.toks(e['q'] + ' . ' + e['hint']), NG) - stock
                    for k in ('holiday', 'external', 'term'):
                        hit = g & corp[lv][k]
                        if hit:
                            (reviews if k == 'term' else fails).append('%s: shares a %d-word run with %s: "%s"' % (tag, NG, k, sorted(hit)[0]))
                    hit = g & ext_grams
                    if hit:
                        fails.append('%s: shares a %d-word run with the extension workbooks: "%s"' % (tag, NG, sorted(hit)[0]))
            # within-level skeleton overlap (this month vs every released month)
            sk = {}
            for m2 in man['released']:
                for e in banks[m2]['levels'][str(lv)]:
                    t = toks(e['q'])
                    for i in range(len(t) - 5):
                        sk.setdefault(' '.join(t[i:i + 6]), set()).add(e['id'])
            for g, ids in sk.items():
                if len(ids) > 1 and g.count('#') < 3:
                    reviews.append('L%d: wording skeleton "%s" is shared by %s' % (lv, g, sorted(ids)))
            stats[lv] = (len(items), len(kinds_ct), max(kinds_ct.values()), len(topics))
        lines.append('# Teaser batch m%s verification report' % mm)
        lines.append('')
        lines.append('Method: every puzzle is re-solved by `brute.py` (independent of the author solver `kinds.py`) over its whole search space; exactly one valid answer must exist and equal the bank answer.')
        lines.append('')
        lines.append('| Level | Puzzles | Distinct kinds | Most uses of one kind | Topics |')
        lines.append('|---|---|---|---|---|')
        for lv, s in stats.items():
            lines.append('| %d | %d | %d | %d | %d |' % ((lv,) + s))
        lines.append('')
        miss = [lv for lv in corp if corp[lv].get('_ext_missing')] if dup_check else []
        lines.append('Similarity sources checked: holiday banks, own term lessons, all extension workbook data, %s.' % (
            'external private source files NOT present in this checkout (not checked)' if miss else 'external private source files'))
        lines.append('')
        lines.append('FAIL count: %d. REVIEW items: %d.' % (len(fails), len(reviews)))
        lines.append('')
        for f in fails:
            lines.append('- FAIL ' + f)
        for r in reviews:
            lines.append('- REVIEW ' + r)
        open(os.path.join(HERE, 'batches', 'm%s' % mm, 'VERIFY_REPORT.md'), 'w', encoding='utf-8').write('\n'.join(lines) + '\n')
        print('month %s: %d FAIL, %d REVIEW' % (mm, len(fails), len(reviews)))
        for f in fails[:60]:
            print('  FAIL', f)
        fails_all += len(fails)
    sys.exit(1 if fails_all else 0)


if __name__ == '__main__':
    main()
