#!/usr/bin/env python3
"""Independent verification of the released teaser batches.

    python3 website/teasers/verify_bank.py            # all months in manifest.json
    python3 website/teasers/verify_bank.py 11 12      # chosen months (the structure rules always look at every released month)

For every puzzle: re-solve with brute.py (never imports kinds.py), require exactly ONE valid answer equal to the bank's answer;
check the arithmetic written in the question/hint/explanation; wording rules (spelling, brand names, Singapore coins, doubled words,
hint must not name the answer); age fit (sub-structure allowed at that level, see taxonomy.json).

Originality and structure (owner policy "new story AND new frame", frame = maths structure):
  * taxonomy.json lists kinds (families) and sub-structures.  Every puzzle names its sub-structure; the sub-structure must be
    one the solver kind really implements (kind and parameter match) and allowed at that level.
  * within one level and one calendar quarter: at most 1 puzzle per sub-structure and 3 per family (kind).
  * no sub-structure used by the fixed puzzle on the level pages (taxonomy "fixed_fallback") appears anywhere in the bank.
  * no answer repeats within a level (across all released months); no two puzzles of a level share most of their numbers.
  * shared run of 7 words (the extension checker's threshold) with holiday, term, extension, external sources, the seven fixed
    website puzzles, or another puzzle of the same level = FAIL (generic stock phrases are listed in stock_phrases.txt).
  * structure similarity: the question with names, nouns and numbers masked is compared with every question in our holiday, term,
    extension, school, book-draft and catalogue sources; the same skeleton AND shared numbers = FAIL, the same skeleton alone = REVIEW.
Writes batches/m<MM>/VERIFY_REPORT.md and batches/STRUCTURE_REPORT.md.  Exit code 1 on any FAIL.
"""
import glob
import hashlib
import json
import os
import pickle
import re
import sys
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, 'extension', 'verify'))
import brute                                    # noqa: E402
import taxonomy as TAX                          # noqa: E402

try:
    import dup_check                            # noqa: E402
except Exception as e:                          # pragma: no cover
    dup_check = None
    print('dup_check not importable:', e)

NGF = TAX.RULES['run_words_fail']      # a shared run of this many words is a FAIL (7 = the extension checker's rule)
MAXQ = {1: 48, 2: 55, 3: 65, 4: 75, 5: 85, 6: 95}      # words in a question
MAXSENT = {1: 20, 2: 22, 3: 26, 4: 30, 5: 34, 6: 38}   # words in a sentence
US = re.compile(r'\b(color|meter|liter|kilometer|centimeter|math)\b', re.I)
BAD = re.compile(r'picture|image|photo|specimen|coin art|note art|look at the coin|[\U0001F300-\U0001FAFF]')
BRANDS = re.compile(r'\b(milo|coke|coca[- ]cola|pepsi|nescafe|maggi|lego|nintendo|pokemon|doraemon|kitkat|oreo|mcdonald|kfc|starbucks|ikea|'
                    r'nike|adidas|google|youtube|netflix|tiktok|roblox|minecraft|barbie|disney|samsung|iphone|ipad|hello kitty|yakult|'
                    r'ribena|horlicks|colgate|dettol|tupperware|ferrero|cadbury|nutella|chupa|haw par|ya kun|toast box|breadtalk|grab|'
                    r'foodpanda|shopee|lazada)\b', re.I)
COIN_OK = {5, 10, 20, 50}               # Singapore coins in everyday use (and stamps are not written in cents any more)
COIN = re.compile(r'(\d+)[- ]cents?[- ](coin|stamp|note)', re.I)
NUM = re.compile(r'\d[\d,]*\.?\d*')
DOUBLED = re.compile(r'\b([A-Za-z]{2,})\s+\1\b', re.I)
FUNC = set('''a an the of to in on at by for with from into and or but if then than so as is are was were be been am has have had do does
did will would can could how many much what which who whom whose when where why each every all both either neither some any no not only also just
too more most less fewer least same different other another others one ones twice thrice half halves third thirds quarter quarters times double
doubles triple altogether total sum difference product quotient remainder left over equal equally equals exactly first second last next before
after between above below under per it its his her their they them he she we you i me my our your this that these those there here now
together divided divide multiplied multiply added add subtract take takes taken away give gives gave get gets got keep keeps rest
number numbers digit digits'''.split())


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
    text = re.sub(r'\d+\s*/\s*\d+', 'F', text)
    t = text.replace('×', '*').replace('÷', '/').replace('−', '-').replace('$', '')
    for m in re.finditer(r'(?<![\w.])((?:\(?\d[\d,]*\.?\d*\)?\s*[-+*/]\s*)+\(?\d[\d,]*\.?\d*\)?)\s*=\s*(\d[\d,]*\.?\d*)(?!\s*[-+*/(\d])', t):
        if 'F' in m.group(0):
            continue
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


def numbers_in(text):
    return {norm_num(n) for n in NUM.findall(text)}


# ------------------------------------------------------------------ structure skeletons
def skeleton(text):
    """Question with every number -> '#', every word that is not a structure word -> '_' (runs of '_' collapse); sentence ends kept."""
    t = text.lower().replace('’', "'")
    out = []
    for tok in re.findall(r"\d[\d,]*\.?\d*|[a-z']+|[.?!]", t):
        if tok[0].isdigit():
            tok = '#'
        elif tok in '.?!':
            pass
        elif tok not in FUNC:
            tok = '_'
        if tok == '_' and out and out[-1] == '_':
            continue
        out.append(tok)
    return out


def shingles(sk, n=4):
    return {' '.join(sk[i:i + n]) for i in range(len(sk) - n + 1)}


def source_files():
    pats = [('hp', ['json', 'js', 'py', 'html']), ('p1', ['json', 'js', 'py']), ('p2', ['js', 'json']), ('p3', ['js', 'json']),
            ('p4', ['js', 'json']), ('p5', ['js', 'json']), ('p6', ['js', 'json']), ('extension/data', ['json']),
            ('docs/books', ['md', 'txt', 'json', 'py', 'html']), ('docs/sasmo', ['md', 'txt', 'json', 'py', 'html']),
            ('practice', ['json', 'js']), ('taster', ['json', 'html', 'js']), ('review', ['json', 'html', 'md']),
            ('tutor', ['md', 'json', 'txt']), ('school', ['md', 'json', 'txt', 'html'])]
    files = []
    for d, exts in pats:
        for e in exts:
            files += glob.glob(os.path.join(ROOT, d, '**', '*.' + e), recursive=True)
    files += glob.glob(os.path.join(ROOT, 'term', 'l*', 'lessons', '*.json'))
    files += glob.glob(os.path.join(ROOT, 'docs', 'books', 'private_*', '**', '*'), recursive=True)
    return sorted({f for f in files if os.path.isfile(f) and os.path.getsize(f) < 30_000_000})


def chunks_of(path):
    try:
        raw = open(path, encoding='utf-8', errors='ignore').read()
    except OSError:
        return []
    if path.endswith('.html'):
        raw = re.sub(r'<script.*?</script>|<style.*?</style>', ' ', raw, flags=re.S)
        raw = re.sub(r'<[^>]+>', ' ', raw)
    raw = raw.replace('\\n', ' ').replace('\\"', '"')
    sents = re.split(r'(?<=[.?!])\s+|\n+|\\n', raw)
    out, window = [], []
    for s in sents:
        s = s.strip()
        if not s:
            continue
        window.append(s)
        window = window[-4:]
        if re.search(r"\?['\"\)\]]*[,;]?$", s):
            out.append(' '.join(window))
    return out


def structure_index():
    """Inverted index of masked-skeleton 4-grams over every question in our own sources (cached in the temp folder)."""
    files = source_files()
    key = hashlib.md5('|'.join('%s:%d:%d' % (f, os.path.getmtime(f), os.path.getsize(f)) for f in files).encode()).hexdigest()
    cache = os.path.join(os.environ.get('TMPDIR', '/tmp'), 'mi_teaser_structure_%s.pkl' % key)
    if os.path.exists(cache):
        try:
            return pickle.load(open(cache, 'rb'))
        except Exception:
            pass
    texts, index = [], {}
    for f in files:
        for ch in chunks_of(f):
            cid = len(texts)
            texts.append((os.path.relpath(f, ROOT), ch[:300]))
            for sh in shingles(skeleton(ch)):
                index.setdefault(sh, []).append(cid)
    data = (texts, index)
    try:
        pickle.dump(data, open(cache, 'wb'))
    except Exception:
        pass
    return data


MAX_SMALL = 4       # single-digit answers: the same digit may be the answer of at most this many puzzles of a level (only 10 values exist for 61 puzzles)
GENERIC = 120       # a skeleton 4-gram found in more than this many source questions says nothing about structure


def structure_hits(q, texts, index):
    sk = shingles(skeleton(q))
    if not sk:
        return []
    score = {}
    for sh in sk:
        ids = index.get(sh)
        if ids and len(ids) <= GENERIC:
            for cid in set(ids):
                score[cid] = score.get(cid, 0) + 1
    mine = {n for n in numbers_in(q) if n not in ('0', '1', '2')}
    res = []
    for cid, c in sorted(score.items(), key=lambda kv: -kv[1])[:12]:
        sc = c / len(sk)
        if sc < 0.5:
            break
        theirs = {n for n in numbers_in(texts[cid][1]) if n not in ('0', '1', '2')}
        res.append((sc, len(mine & theirs), texts[cid][0], texts[cid][1]))
    return res


def fixed_puzzles():
    """The seven fixed puzzles (home page and six level pages): their question text."""
    out = {}
    pages = {1: os.path.join(ROOT, 'website', 'mi_signup.html')}
    for lv, f in {1: 'ages-6-8', 2: 'ages-7-9', 3: 'ages-8-10', 4: 'ages-9-11', 5: 'ages-10-12', 6: 'ages-11-13'}.items():
        pages['L%d' % lv] = os.path.join(ROOT, 'website', 'level_pages', f + '.html')
    for k, f in pages.items():
        try:
            h = open(f, encoding='utf-8').read()
        except OSError:
            continue
        m = re.search(r'class="pzl"[^>]*>.*?<p style="font-size:18px">(.*?)</p>', h, re.S)
        if m:
            out[str(k)] = re.sub(r'<[^>]+>', '', m.group(1))
    return out


def stock_local():
    p = os.path.join(HERE, 'stock_phrases.txt')
    ph = set()
    if os.path.exists(p):
        for line in open(p, encoding='utf-8'):
            line = line.strip().lower()
            if line and not line.startswith('#'):
                ph |= dup_check.grams(dup_check.toks(line), NGF)
    return ph


def main():
    man = json.load(open(os.path.join(HERE, 'manifest.json')))
    months = sys.argv[1:] or man['released']
    banks = {}
    for mm in man['released']:
        banks[mm] = json.load(open(os.path.join(HERE, 'batches', 'm%s' % mm, 'bank.json'), encoding='utf-8'))
    levels = sorted({int(lv) for b in banks.values() for lv in b['levels']})
    fails_all = 0
    global_fails = []
    # ---------------------------------------------------------------- corpora for the wording check
    corp = {}
    if dup_check:
        for lv in range(1, 7):
            cs = dup_check.corpora(lv)
            corp[lv] = {k: dup_check.grams(dup_check.toks(dup_check.read_corpus(v)), NGF) for k, v in cs.items()}
            corp[lv]['_ext_missing'] = not cs['external']
        ext_texts = []
        for f in glob.glob(os.path.join(ROOT, 'extension', 'data', 'l*_u*.json')):
            try:
                ext_texts.append(' . '.join(t for _, t in dup_check.question_texts(json.load(open(f, encoding='utf-8')))))
            except Exception:
                pass
        ext_grams = dup_check.grams(dup_check.toks(' . '.join(ext_texts)), NGF)
        stock = dup_check.stock(NGF) | stock_local()
    fixed = fixed_puzzles()
    fixed_grams = {k: dup_check.grams(dup_check.toks(v), NGF) for k, v in fixed.items()} if dup_check else {}
    texts, index = structure_index()
    print('structure index: %d source questions, %d skeleton 4-grams' % (len(texts), len(index)))
    reserved_kinds = {}
    for lv, sid in TAX.FIXED.items():
        reserved_kinds[sid] = TAX.SUBS[sid]['kinds'] if sid in TAX.SUBS else []

    # ---------------------------------------------------------------- structure rules over all released months (per level and quarter)
    struct_lines = ['# Structure report (taxonomy.json)', '',
                    'Rules: per level and calendar quarter at most %d puzzle per sub-structure and %d per family (kind); no answer repeats inside a level; '
                    'the sub-structures used by the fixed puzzles on the level pages (%s) are never used by the bank.' % (
                        TAX.RULES['max_per_sub_per_quarter'], TAX.RULES['max_per_family_per_quarter'], ', '.join(sorted(TAX.FIXED.values()))), '']
    all_by_level = {lv: [] for lv in levels}
    for mm in man['released']:
        for lv, items in banks[mm]['levels'].items():
            for e in items:
                all_by_level[int(lv)].append((mm, e))
    for lv in levels:
        by_q = {}
        for mm, e in all_by_level[lv]:
            by_q.setdefault(TAX.quarter(mm), []).append(e)
        for q, items in sorted(by_q.items()):
            subs, fams = {}, {}
            for e in items:
                subs.setdefault(e['sub'], []).append(e['id'])
                fams.setdefault(e['family'], []).append(e['id'])
            for s, ids in subs.items():
                if len(ids) > TAX.RULES['max_per_sub_per_quarter']:
                    global_fails.append('L%d quarter %d: sub-structure %s used %d times: %s' % (lv, q, s, len(ids), ', '.join(ids)))
            for f, ids in fams.items():
                if len(ids) > TAX.RULES['max_per_family_per_quarter']:
                    global_fails.append('L%d quarter %d: family %s used %d times (cap %d): %s' % (
                        lv, q, f, len(ids), TAX.RULES['max_per_family_per_quarter'], ', '.join(ids)))
            struct_lines.append('- Level %d, quarter %d: %d puzzles, %d distinct sub-structures, %d families, most in one family %d' % (
                lv, q, len(items), len(subs), len(fams), max(len(v) for v in fams.values())))
        # answers: 10 and above (and every text answer) may appear once per level; a single digit at most MAX_SMALL times
        seen_ans = {}
        for mm, e in all_by_level[lv]:
            seen_ans.setdefault(e['ans'], []).append(e['id'])
        for a, ids in seen_ans.items():
            small = a.lstrip('-').isdigit() and abs(int(a)) < 10
            if (not small and len(ids) > 1) or (small and len(ids) > MAX_SMALL):
                global_fails.append('L%d: answer %s repeats (%s)' % (lv, a, ', '.join(ids)))
        # numbers shared between two puzzles of the same level
        nums = [(e['id'], {n for n in numbers_in(e['q']) if n not in ('0', '1', '2') and not (n in ('5', '10', '20', '50') and 'cent' in e['q'])}) for _, e in all_by_level[lv]]
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                a, b = nums[i][1], nums[j][1]
                sh = a & b
                big = [n for n in sh if int(float(n)) >= 10]
                if (len(sh) >= 4 or (len(sh) >= TAX.RULES['number_overlap_fail'] and len(big) >= 2)) and len(sh) >= 0.6 * min(len(a), len(b)):
                    global_fails.append('L%d: %s and %s share the numbers %s' % (lv, nums[i][0], nums[j][0], sorted(sh)))
        # frames unique
        fr = {}
        for mm, e in all_by_level[lv]:
            if e['frame'] in fr:
                global_fails.append('L%d: frame %s repeated (%s and %s)' % (lv, e['frame'], fr[e['frame']], mm))
            fr[e['frame']] = mm
    # a puzzle must not share a 7-word run with another puzzle of the same level
    if dup_check:
        for lv in levels:
            seen = {}
            for mm, e in all_by_level[lv]:
                g = dup_check.grams(dup_check.toks(e['q']), NGF) - stock
                for x in g:
                    if x in seen and seen[x] != e['id']:
                        global_fails.append('L%d: %s and %s share the %d-word run "%s"' % (lv, seen[x], e['id'], NGF, x))
                    seen[x] = e['id']

    review_struct = []
    for mm in months:
        fails, reviews, lines, generic = [], [], [], []
        stats = {}
        for lv, items in banks[mm]['levels'].items():
            lv = int(lv)
            kinds_ct, fam_ct, topics = {}, {}, {}
            dates = [e['date'] for e in items]
            if len(set(dates)) != len(dates):
                fails.append('L%d duplicate dates' % lv)
            want_n = {'01': 31, '02': 29, '03': 31, '04': 30, '05': 31, '06': 30, '07': 31, '08': 31, '09': 30, '10': 31, '11': 30, '12': 31}[mm]
            if len(items) != want_n:
                fails.append('L%d has %d puzzles, month %s needs %d' % (lv, len(items), mm, want_n))
            for e in items:
                tag = '%s [%s]' % (e['id'], e['date'])
                # 0. taxonomy
                sub = e.get('sub')
                if sub not in TAX.SUBS:
                    fails.append('%s: unknown sub-structure %r' % (tag, sub))
                else:
                    okm, why = TAX.matches(sub, e)
                    if not okm:
                        fails.append('%s: not an instance of sub-structure %s (%s)' % (tag, sub, why))
                    if lv not in TAX.SUBS[sub]['levels']:
                        fails.append('%s: sub-structure %s is not allowed at level %d (levels %s)' % (tag, sub, lv, TAX.SUBS[sub]['levels']))
                for rsid, rk in reserved_kinds.items():
                    if e['kind'] in rk:
                        fails.append('%s: same structure as the fixed puzzle on the level pages (%s)' % (tag, rsid))
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
                sents = [len(s.split()) for s in re.split(r'(?<=[.?!])"?\s+', e['q']) if s.strip()]
                if words > MAXQ[lv]:
                    reviews.append('%s: question has %d words (limit %d)' % (tag, words, MAXQ[lv]))
                if sents and max(sents) > MAXSENT[lv]:
                    reviews.append('%s: longest sentence %d words (limit %d)' % (tag, max(sents), MAXSENT[lv]))
                for fld in ('q', 'hint', 'why'):
                    if US.search(e[fld]):
                        fails.append('%s: non-Singapore spelling/word in %s: %s' % (tag, fld, US.search(e[fld]).group(0)))
                    if BAD.search(e[fld]):
                        fails.append('%s: forbidden word in %s: %s' % (tag, fld, BAD.search(e[fld]).group(0)))
                    if BRANDS.search(e[fld]):
                        fails.append('%s: brand name in %s: %s' % (tag, fld, BRANDS.search(e[fld]).group(0)))
                    for c in COIN.finditer(e[fld]):
                        if int(c.group(1)) not in COIN_OK:
                            fails.append('%s: a %s-cent %s does not exist in Singapore (%s)' % (tag, c.group(1), c.group(2), fld))
                    if re.search(r'\b[12][- ]cents?\b(?! (?:of|more|less|each))', e[fld]) and 'coin' in e[fld]:
                        fails.append('%s: 1-cent or 2-cent coins in %s' % (tag, fld))
                    for d in DOUBLED.finditer(e[fld]):
                        fails.append('%s: doubled word "%s" in %s' % (tag, d.group(0), fld))
                    for b in check_arith(e[fld]):
                        fails.append('%s: arithmetic in %s is wrong: %s' % (tag, fld, b))
                qnums = numbers_in(e['q'] + ' ' + (e.get('code') or ''))
                if e['type'] == 's':
                    if re.search(r'\b' + re.escape(e['ans'].lower()) + r'\b', e['hint'].lower()):
                        fails.append('%s: hint gives the answer away' % tag)
                else:
                    a = e['ans'].lstrip('-')
                    if a not in qnums and re.search(r'(?<![\d.,/])' + re.escape(a) + r'(?![\d.,/]|\s*/)', e['hint']):
                        fails.append('%s: hint contains the answer %s' % (tag, e['ans']))
                if e['kind'] == 'repeat_pattern':   # the pattern printed in the wording must be the pattern that was solved
                    at = 0
                    for item in e['p']['unit']:
                        k = e['q'].find(item, at)
                        if k < 0:
                            fails.append('%s: pattern item %r is not in the question in order' % (tag, item))
                            break
                        at = k + len(item)
                # 3. numbers in the question should come from the parameters
                known = set()
                flat(e['p'], known)
                flat(e['t'], known)
                known.update(norm_num(x) for x in NUM.findall(e['why'] + ' ' + e['hint']))
                for n in NUM.findall(e['q']):
                    n = norm_num(n)
                    if n not in known and n.replace('.', '') not in known:
                        reviews.append('%s: number %s in the question is not a parameter (written in the wording; check)' % (tag, n))
                kinds_ct[e['kind']] = kinds_ct.get(e['kind'], 0) + 1
                fam_ct[e['family']] = fam_ct.get(e['family'], 0) + 1
                topics[e['topic']] = topics.get(e['topic'], 0) + 1
                # 4. similarity: shared word runs
                if dup_check:
                    toks_q = dup_check.toks(e['q'] + ' . ' + e['hint'])
                    g = dup_check.grams(toks_q, NGF) - stock
                    for k in ('holiday', 'external', 'term'):
                        if g & corp[lv][k]:
                            fails.append('%s: shares a %d-word run with %s: "%s"' % (tag, NGF, k, sorted(g & corp[lv][k])[0]))
                    if g & ext_grams:
                        fails.append('%s: shares a %d-word run with the extension workbooks: "%s"' % (tag, NGF, sorted(g & ext_grams)[0]))
                    for k, fg in fixed_grams.items():
                        if g & fg and (k == 'L%d' % lv or (k == '1' and lv == 1) or True):
                            fails.append('%s: shares a %d-word run with the fixed website puzzle %s: "%s"' % (tag, NGF, k, sorted(g & fg)[0]))
                # 5. structure similarity (masked skeleton) with our sources and the fixed puzzles
                for sc, shared, src, text in structure_hits(e['q'], texts, index):
                    line = '%s: skeleton %.2f like "%s ..." (%s), shared numbers %d' % (tag, sc, text[:110].replace('\n', ' '), src, shared)
                    if (sc >= 0.6 and shared >= 2) or (sc >= 0.8 and shared >= 1):
                        fails.append('same structure and same numbers: ' + line)
                    elif sc >= 0.6:
                        review_struct.append(line)
                    break
                for k, text in fixed.items():
                    a, b = shingles(skeleton(e['q'])), shingles(skeleton(text))
                    if a and b and len(a & b) / len(a) >= 0.45 and numbers_in(e['q']) & numbers_in(text) - {'0', '1', '2'}:
                        fails.append('%s: same skeleton and numbers as the fixed website puzzle %s' % (tag, k))
            stats[lv] = (len(items), len(kinds_ct), max(kinds_ct.values()), len(fam_ct), max(fam_ct.values()), len({e['sub'] for e in items}))
        lines.append('# Teaser batch m%s verification report' % mm)
        lines.append('')
        lines.append('Method: every puzzle is re-solved by `brute.py` (independent of the author solver `kinds.py`) over its whole search space; exactly one valid answer must exist and equal the bank answer. '
                     'Structure rules (taxonomy, caps, repeated answers and numbers, word runs, skeleton similarity) are in `batches/STRUCTURE_REPORT.md`.')
        lines.append('')
        lines.append('| Level | Puzzles | Solver kinds | Most uses of one solver kind | Families | Most in one family | Sub-structures |')
        lines.append('|---|---|---|---|---|---|---|')
        for lv, s in stats.items():
            lines.append('| %d | %d | %d | %d | %d | %d | %d |' % ((lv,) + s))
        lines.append('')
        miss = [lv for lv in corp if corp[lv].get('_ext_missing')] if dup_check else []
        lines.append('Similarity sources checked: holiday banks, own term lessons, all extension workbook data, the school booklets, our book drafts and catalogues, %s, and the seven fixed website puzzles.' % (
            'external private source files NOT present in this checkout (not checked)' if miss else 'external private source files'))
        lines.append('')
        lines.append('FAIL count: %d. REVIEW items: %d.' % (len(fails), len(reviews)))
        lines.append('')
        for f in fails:
            lines.append('- FAIL ' + f)
        lines.append('')
        for r in reviews:
            lines.append('- REVIEW ' + r)
        open(os.path.join(HERE, 'batches', 'm%s' % mm, 'VERIFY_REPORT.md'), 'w', encoding='utf-8').write('\n'.join(lines) + '\n')
        print('month %s: %d FAIL, %d REVIEW' % (mm, len(fails), len(reviews)))
        for f in fails[:80]:
            print('  FAIL', f)
        fails_all += len(fails)
    struct_lines.append('')
    struct_lines.append('Structure FAIL count (all released months): %d' % len(global_fails))
    for f in global_fails:
        struct_lines.append('- FAIL ' + f)
    struct_lines.append('')
    struct_lines.append('Skeleton matches with our own sources that were reviewed by hand (same masked wording, but no shared numbers): %d' % len(review_struct))
    for r in review_struct:
        struct_lines.append('- REVIEW ' + r)
    open(os.path.join(HERE, 'batches', 'STRUCTURE_REPORT.md'), 'w', encoding='utf-8').write('\n'.join(struct_lines) + '\n')
    print('structure rules: %d FAIL' % len(global_fails))
    for f in global_fails[:80]:
        print('  FAIL', f)
    fails_all += len(global_fails)
    sys.exit(1 if fails_all else 0)


if __name__ == '__main__':
    main()
