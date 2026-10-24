#!/usr/bin/env python3
"""Independent verification of the released teaser batches.

    python3 website/teasers/verify_bank.py            # all months in manifest.json
    python3 website/teasers/verify_bank.py 11 12      # chosen months (the structure rules always look at every released month)
    python3 website/teasers/verify_bank.py --selftest # prove that every rule fires (synthetic and real-bank probes)
    python3 website/teasers/verify_bank.py --strict-capacity   # also exit 1 when the taxonomy cannot supply a full year (see below)

For every puzzle: re-solve with brute.py (never imports kinds*.py), require exactly ONE valid answer equal to the bank's answer;
check the arithmetic written in the question/hint/explanation; wording rules (spelling, brand names, Singapore coins, doubled words,
hint must not name the answer); age fit (sub-structure allowed at that level, see taxonomy.json).

Originality and structure (owner policy "new story AND new frame", frame = maths structure):
  * taxonomy.json lists kinds (families) and sub-structures.  Every puzzle names its sub-structure; the sub-structure must be
    one the solver kind really implements (kind and parameter match) and allowed at that level.
  * Levels 3 to 6 (TEASER-STRICT): at most 1 puzzle per sub-structure and 3 per family in a calendar quarter, and the same sub-structure
    never within 30 days of itself across a quarter boundary (circular over the year).
  * Levels 1 and 2 (L1L2-GAP60): the same sub-structure at least 60 days apart (circular, checked for a 365-day and a 366-day year),
    a family at most 3 times in any 60 consecutive days and never on two consecutive days, an answer not repeated within 60 days
    and a single-digit answer at most twice in any 60 days.
  * no sub-structure used by the fixed puzzle on the level pages (taxonomy "fixed_fallback") appears anywhere in the bank.
  * Levels 3 to 6 keep the full-year answer rule (answers of 10 or more once per level; a single digit at most 4 times).
  * no two puzzles of a level share most of their numbers or the same story.
  * shared run of 7 words (the extension checker's threshold) with holiday, term, extension, external sources, the seven fixed
    website puzzles, or another puzzle of the same level = FAIL (generic stock phrases are listed in stock_phrases.txt).
  * structure similarity: the question with names, nouns and numbers masked is compared with every question in our holiday, term,
    extension, school, book-draft and catalogue sources; the same skeleton AND shared numbers = FAIL, the same skeleton alone = REVIEW.
  * story similarity (round 2): the content words of the question (names and common words removed) compared with every sentence or
    pair of sentences in the ~20,000 source chunks; the same objects (almost all story words, or the same specific objects, or the
    same words plus two shared numbers) = FAIL, so a near-copy with new numbers can no longer pass.
Writes batches/m<MM>/VERIFY_REPORT.md and batches/STRUCTURE_REPORT.md (with the true capacity table).  Exit code 1 on any FAIL.
"""
import glob
from array import array
import hashlib
import html
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


SOURCE_ROOTS = ['hp', 'p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'extension', 'docs', 'practice', 'taster', 'review', 'tutor', 'school', 'outputs',
                'split', 'rebuild', 'website', 'levels', 'print', 'portal', 'k2', 'deck', 'ops', 'diag', 'mascot', 'releases', 'worker', 'term']
SOURCE_EXTS = ('.md', '.txt', '.json', '.js', '.py', '.html', '.csv', '.pdf')      # round 4: PDFs are read as text (pdftotext, cached by content hash)
SKIP_DIRS = ('node_modules', '.git', '__pycache__')
SKIP_PREFIX = ('website/teasers/', 'website/dist/', 'outputs/owner_review/teasers_preview/')      # our own teasers and their previews are not a "source"
LOCK_FILE = os.path.join(HERE, 'source_lock.json')


def source_files():
    """Every text file of the WHOLE working tree that could hold a question of ours (tracked or not, git-ignored private sources included).
    Round 3: the list is `SOURCE_ROOTS` x `SOURCE_EXTS`, so it now also covers outputs/ (the Skill Additions sheets), docs/audit/*.py,
    practice/**/*.py (all lesson.py and items), school booklets, the holiday week 1 to 5 sources, split/, rebuild/ and website/;
    plus the term lessons.  Sorted, so the digest below does not depend on the file system order."""
    files = []
    for root in SOURCE_ROOTS:
        base = os.path.join(ROOT, root)
        for dp, dns, fns in os.walk(base):
            dns[:] = sorted(d for d in dns if d not in SKIP_DIRS)
            for fn in fns:
                if fn.endswith(SOURCE_EXTS):
                    files.append(os.path.join(dp, fn))
    out = []
    for f in sorted(set(files)):
        rel = os.path.relpath(f, ROOT).replace(os.sep, '/')
        if rel.startswith(SKIP_PREFIX) or not os.path.isfile(f) or os.path.getsize(f) >= 30_000_000:
            continue
        out.append(f)
    return out


PDF_CACHE = os.path.join(os.environ.get('TMPDIR', '/tmp'), 'mi_pdf_text')


def _pdf_text_uncached(path):
    import subprocess
    try:
        r = subprocess.run(['pdftotext', '-q', '-enc', 'UTF-8', path, '-'], capture_output=True, timeout=300)
        raw = r.stdout.decode('utf-8', 'ignore')
    except Exception:
        return ''
    # one paragraph per blank-line block; line breaks inside a paragraph become spaces; hyphenated line ends are joined
    paras = []
    for blk in re.split(r'\n\s*\n', raw.replace('\f', '\n\n')):
        blk = re.sub(r'(\w)-\n(\w)', r'\1\2', blk)
        blk = ' '.join(blk.split())
        if blk:
            paras.append(blk)
    return '\n'.join(paras)


def pdf_text(path):
    """Text of a PDF (pdftotext), cached by the sha256 of the file's content (never by file time)."""
    try:
        data = open(path, 'rb').read()
    except OSError:
        return ''
    h = hashlib.sha256(data).hexdigest()
    cp = os.path.join(PDF_CACHE, h + '.txt')
    if os.path.exists(cp):
        try:
            return open(cp, encoding='utf-8').read()
        except OSError:
            pass
    txt = _pdf_text_uncached(path)
    try:
        os.makedirs(PDF_CACHE, exist_ok=True)
        tmp = cp + '.%d.tmp' % os.getpid()
        open(tmp, 'w', encoding='utf-8').write(txt)
        os.replace(tmp, cp)
    except OSError:
        pass
    return txt


def prefetch_pdfs(files):
    """Extract every PDF text in parallel so that the (serial, deterministic) index build only reads the cache."""
    from concurrent.futures import ThreadPoolExecutor
    pdfs = [f for f in files if f.endswith('.pdf')]
    with ThreadPoolExecutor(max_workers=8) as ex:
        list(ex.map(pdf_text, pdfs))


def read_source(path):
    if path.endswith('.pdf'):
        return pdf_text(path)
    try:
        return open(path, encoding='utf-8', errors='ignore').read()
    except OSError:
        return ''


_DIGEST = {}


def source_digest(files=None):
    """(sha256 over every source file's path and content, number of files, bytes, files per root).  The verdict of this verifier is a function of
    the bank, the rules and this digest, never of the checkout: two machines with the same digest give the same report."""
    files = files if files is not None else source_files()
    key = tuple(files)
    if key in _DIGEST:
        return _DIGEST[key]
    h = hashlib.sha256()
    total, per = 0, {}
    for f in files:
        rel = os.path.relpath(f, ROOT).replace(os.sep, '/')
        data = open(f, 'rb').read()
        h.update(rel.encode() + b'\0' + hashlib.sha256(data).digest())
        total += len(data)
        per[rel.split('/')[0]] = per.get(rel.split('/')[0], 0) + 1
    _DIGEST[key] = (h.hexdigest(), len(files), total, per)
    return _DIGEST[key]


def lock_problems(per_override=None):
    """The source lock (source_lock.json) holds the minimum number of files per source root.  A checkout that lacks them (for example a tracked-only
    export without the git-ignored private sources) cannot give a valid verdict, so the verifier refuses instead of printing '0 FAIL'."""
    if not os.path.exists(LOCK_FILE):
        return ['source_lock.json is missing: run verify_bank.py --update-lock on the full working tree']
    lock = json.load(open(LOCK_FILE, encoding='utf-8'))
    _, n, _, per = source_digest()
    per = per_override if per_override is not None else per
    bad = []
    for root, need in sorted(lock['min_files'].items()):
        if per.get(root, 0) < need:
            bad.append('source root %s has %d files, the lock needs at least %d (incomplete checkout?)' % (root, per.get(root, 0), need))
    npdf = sum(1 for f in source_files() if f.endswith('.pdf'))
    if npdf < lock.get('min_pdfs', 0):
        bad.append('only %d PDFs among the sources, the lock needs at least %d (PDFs are read as text since round 4; incomplete checkout?)' % (npdf, lock['min_pdfs']))
    for d in lock.get('must_exist', []):
        if not glob.glob(os.path.join(ROOT, d)):
            bad.append('required source %s is missing (git-ignored private sources not present?)' % d)
    return bad


def update_lock():
    _, n, total, per = source_digest()
    lock = {'note': 'Minimum number of source files per root for a valid verification (written by verify_bank.py --update-lock). The verifier refuses to give a verdict on a checkout with fewer.',
            'min_files': {r: int(c * 0.95) for r, c in sorted(per.items())},
            'min_pdfs': int(sum(1 for f in source_files() if f.endswith('.pdf')) * 0.95),
            'must_exist': ['docs/books/private_p1_papers', 'docs/books/private_p6_papers', 'docs/books/private_word_problems_notes.md', 'extension/data', 'outputs/skill_additions', 'practice/holiday', 'docs/audit', 'term/l1/lessons', 'term/l1/out', 'outputs/workbook/Math_Inquirers_P1_Student_Workbook_Designed.pdf', 'school/p3/out', 'p2/Math_Inquirers_P2_Tutor_Guide.html'],
            'files_at_update': n, 'bytes_at_update': total}
    json.dump(lock, open(LOCK_FILE, 'w', encoding='utf-8'), indent=1)
    print('source lock written:', lock['min_files'])


def chunks_of(path):
    raw = read_source(path)
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
    key = hashlib.md5(('structure-v3|' + source_digest(files)[0]).encode()).hexdigest()
    cache = os.path.join(os.environ.get('TMPDIR', '/tmp'), 'mi_teaser_structure_%s.pkl' % key)
    if os.path.exists(cache):
        try:
            return pickle.load(open(cache, 'rb'))
        except Exception:
            pass
    prefetch_pdfs(files)
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
    for cid, c in sorted(score.items(), key=lambda kv: (-kv[1], kv[0]))[:12]:
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


# ------------------------------------------------------------------ story check (content words, round 2)
# The masked skeleton above cannot see a story: "a snail climbs a wall, up 5 down 2" has another skeleton from "a snail climbs 3 cm and
# slides back 1 cm" once the numbers change.  The story check compares the CONTENT WORDS of a teaser (names, number words and
# very common words removed) with every question-sized window (one sentence or two neighbours) of the ~20,000 source chunks.
NAMES = set('''mei ling ben siti kumar priya farhan wei jie aisha hui min xin yi jun hao ali sam amy raj dina arjun mira lena wen jia hakim
nurul ravi sue ann li lee tan lim ong ng zack zara noah nina omar ahmad aminah rina rahim sara sarah john mary david peter anna
ken kai lin lian meng yan yuan bao ying hong huiling jiayi kevin shan tom tim emma jack jill chen emily daniel farid mr mrs uncle aunty mum dad
xavier yusof zhi hui jing ming kiat siew mei-ling'''.split())
STORY_STOP_EXTRA = set('monday tuesday wednesday thursday friday saturday sunday january february march april june july august september october november december north south east west face turn left right clockwise cent coin pay buy sell money dollar circle triangle square rectangle pentagon hexagon cube cuboid cone cylinder sphere prism pyramid curved flat solid edge corner vertex probability fair dice roll fraction percentage ratio decimal angle average perimeter area volume binary prime factor multiple digit doe ha wa get got use make find work take give show tell try need want let put keep say ask think know see look '
                       'call name write read count list add check each first second third fourth then also still even only just '
                       'yes no true false answer question puzzle number numbers way ways kind different same new old big small '
                       'long short much many one two three four five six seven eight nine ten hundred thousand'.split())
DF_SCALE = 1.75       # round 4: the source index grew from 478,000 to about 814,000 sentences (PDFs, the whole term tree), so the document-frequency limits grow with it
DF_MAX = int(24000 * DF_SCALE)         # a word found in more source windows than this says nothing about the story
VERY_RARE_DF = int(100 * DF_SCALE)    # a word found in fewer than this many windows (pane, lolly, mooncake ...) is almost a signature
RARE_DF = int(400 * DF_SCALE)          # a word found in fewer source windows than this is a specific object (snail, lolly, jacket, carton ...)
STORY_VERSION = "story-v20"


_STEM_MEMO = {}


def stem(w):
    r = _STEM_MEMO.get(w)
    if r is not None:
        return r
    r = w
    if w.endswith('ies') and len(w) > 4:
        r = w[:-3] + 'y'
    elif (w.endswith('es') and len(w) > 4 and w[-3] in 'sxz') or w.endswith('ches') or w.endswith('shes'):
        r = w[:-2]
    elif w.endswith('s') and not w.endswith('ss') and len(w) > 3:
        r = w[:-1]
    elif w.endswith('ing') and len(w) > 5:
        r = w[:-3]
    elif w.endswith('ed') and len(w) > 4:
        r = w[:-2]
    _STEM_MEMO[w] = r
    return r


STORY_STOP = {stem(w) for w in FUNC} | {stem(w) for w in STORY_STOP_EXTRA} | {stem(w) for w in NAMES} | FUNC
_SW_MEMO = {}


def story_words(text, names_too=True):
    """Stemmed content words of a text: no function words, no numbers, no names."""
    t = re.sub(r"'s\b", '', text.replace('\u2019', "'").lower())
    out = set()
    for w in re.findall(r'[a-z]+', t):
        r = _SW_MEMO.get(w)
        if r is None:
            sw = stem(w)
            r = sw if (len(sw) > 2 and sw not in STORY_STOP) else ''
            _SW_MEMO[w] = r
        if r:
            out.add(r)
    return out


def sentences_of(path):
    """Every sentence of a source file (markup removed, html entities decoded), one entry per sentence; this is the unit of the story index.
    Round 3: ALL sentences are kept, not only those that end in a question mark, because a source can state a puzzle as a command
    ('Name the weekday of the return date.') and the round 2 index never saw those."""
    raw = read_source(path)
    if path.endswith('.html'):
        raw = re.sub(r'<script.*?</script>|<style.*?</style>', ' ', raw, flags=re.S)
        raw = re.sub(r'<[^>]+>', ' ', raw)
    raw = html.unescape(raw).replace('\\n', ' ').replace('\\"', '"')
    out = []
    for s_ in re.split(r'(?<=[.?!])\s+|\n+', raw):
        s_ = ' '.join(s_.split())
        if len(s_) >= 12 and len(s_.split()) >= 3:
            out.append(s_[:500])
    return out


class SIdx:
    """Sentence-level story index: texts, stem sets, numbers, file of every sentence; document frequency of every stem (counted in
    windows of up to three sentences, i.e. three times the sentence count); inverted lists of stems and of numbers."""

    def __init__(self):
        self.txt, self.words, self.nums, self.file, self.rels = [], [], [], array('H'), []
        self.df, self.inv, self.ninv = {}, {}, {}

    def add_file(self, rel, sents):
        fi = len(self.rels)
        self.rels.append(rel)
        for t in sents:
            self.txt.append(t)
            ws = frozenset(story_words(t))
            self.words.append(ws)
            self.nums.append(frozenset(n for n in numbers_in(t) if n not in ('0', '1', '2')))
            self.file.append(fi)
            for w in ws:
                self.df[w] = self.df.get(w, 0) + 3

    def finish(self):
        cap = DF_MAX
        inv, ninv = {}, {}
        for i, (ws, nums) in enumerate(zip(self.words, self.nums)):
            for w in ws:
                if self.df[w] <= cap:
                    inv.setdefault(w, array('I')).append(i)
            for n in nums:
                if n not in TRIVIAL_NUMS:
                    ninv.setdefault(n, array('I')).append(i)
        self.inv = inv
        self.ninv = {n: ids for n, ids in ninv.items() if len(ids) * 3 <= NUM_DF_MAX}

    def window(self, a, b):
        """Sentences a..b inclusive (same file): (text, words, numbers)."""
        ws = set()
        nums = set()
        for i in range(a, b + 1):
            ws |= self.words[i]
            nums |= self.nums[i]
        return ' '.join(self.txt[a:b + 1])[:600], ws, nums, self.rels[self.file[a]]

    def span_ok(self, a, b):
        return a >= 0 and b < len(self.txt) and self.file[a] == self.file[b]


def story_index():
    """The sentence index of the whole source tree, cached by the content digest of the tree (never by file times)."""
    files = source_files()
    key = hashlib.md5((STORY_VERSION + '|' + source_digest(files)[0]).encode()).hexdigest()
    cache = os.path.join(os.environ.get('TMPDIR', '/tmp'), 'mi_teaser_story_%s.pkl' % key)
    if os.path.exists(cache):
        try:
            return pickle.load(open(cache, 'rb'))
        except Exception:
            pass
    prefetch_pdfs(files)
    ix = SIdx()
    for f in files:
        ix.add_file(os.path.relpath(f, ROOT).replace(os.sep, '/'), sentences_of(f))
    ix.finish()
    try:
        pickle.dump(ix, open(cache, 'wb'), protocol=pickle.HIGHEST_PROTOCOL)
    except Exception:
        pass
    return ix


def mini_index(name, text, base):
    """A one-document index (a fixed website puzzle) that shares the document frequencies of `base`."""
    ix = SIdx()
    ix.add_file(name, [x for x in re.split(r'(?<=[.?!])\s+', ' '.join(text.split())) if len(x) >= 12])
    ix.df = base.df
    inv, ninv = {}, {}
    for i, (ws, nums) in enumerate(zip(ix.words, ix.nums)):
        for w in ws:
            inv.setdefault(w, array('I')).append(i)
        for n in nums:
            ninv.setdefault(n, array('I')).append(i)
    ix.inv, ix.ninv = inv, ninv
    return ix


TRIVIAL_NUMS = {'0', '1', '2', '10', '100', '1000'}     # never evidence of a copy
NUM_DF_MAX = int(24000 * DF_SCALE)      # a number found in more source windows than this is not used to find candidates
COMMON_NUMS = {'3', '4', '5', '6', '7', '8', '9', '10', '12', '15', '20', '24', '25', '30', '50', '60', '100', '1000'}
SPEC_DF = int(3000 * DF_SCALE)         # a word found in fewer source windows than this names something specific (not 'day' or 'box')


def wtoks(text):
    return re.findall(r"[a-z']+|#", re.sub(r'\d[\d,]*\.?\d*', '#', text.lower().replace('\u2019', "'")))


def wgrams(text):
    t = wtoks(text)
    return {' '.join(t[i:i + 3]) for i in range(len(t) - 2)}


def mgrams(text):
    """Word four-grams with numbers masked ('#') that carry at least two story words (names, function words and stock words do not count),
    so that 'how many more are' or 'give your answer as' cannot make a match."""
    t = wtoks(text)
    out = set()
    for i in range(len(t) - 3):
        g = t[i:i + 4]
        if len(story_words(' '.join(w for w in g if w != '#'))) >= 2:
            out.add(' '.join(g))
    return out


def story_hits(q, ix, own_words=None, ans=None, sol=''):
    """Same story and same quantities as a window (one to three neighbouring sentences) of any source file.  Returns [(severity, detail)].
    Let S = the teaser's story words (stems, no names, no function words, no shape or money words), W = the words of one window,
    cov = |S & W| / |S|, rare = shared words found in fewer than RARE_DF windows (snail, lolly, library, pane ...), spec = shared words found in fewer than
    SPEC_DF windows, sn = shared numbers other than 0, 1, 2, nn = shared numbers other than 0, 1, 2, 10, 100, 1000, dn = shared numbers that are not very
    common (COMMON_NUMS).  FAIL when
      (F1) cov >= 0.8, >= 4 shared words, spec >= 2 and sn >= 2: same objects and two same quantities;
      (F2) cov >= 0.6, >= 3 shared words, (spec >= 3 or rare >= 1) and sn >= 3;
      (F4) >= 4 shared rare words and cov >= 0.6: the same specific story (snail ... wall, frog ... well);
      (F5) cov >= 0.5, >= 3 shared words (one of them rare, or 4 specific ones) and >= 2 shared distinctive numbers ($120 and 15%) in a short window;
      (W)  at least 45% of the question's word triples (numbers masked) and 6 or more are found in the window: the same wording with other numbers;
    and the independent auditor's rules (AUDIT_ROUND3 section 1), added in round 3:
      (A)  content words: cov >= 0.7, >= 4 shared words (the teaser has >= 4 story words) and >= 2 rare: the same story skeleton with other numbers;
      (A2) the same specific objects and a shared quantity: >= 3 shared words, cov >= 0.4 and either (>= 2 rare words, cov >= 0.6 and nn >= 2) or (at least half of the teaser's specific words, two shared specific words, nn >= 1, a window of at most 300 characters and one very rare shared word, found in fewer than VERY_RARE_DF windows): three panes across, two down ...; and at least 3 of the teaser's word triples (numbers masked) are in the window;
      (B)  numbers: nn >= 3 with dn >= 2, >= 3 shared words and cov >= 0.4;
      (C)  four-word runs with numbers masked: >= 3 shared four-grams that carry two story words, and at least 30% of the teaser's four-grams.
    REVIEW when cov >= 0.6 with >= 3 shared words and spec >= 2 and none of the above, or on two shared four-grams, or on nn >= 3 with 2 shared words."""
    df = ix.df
    S = {w for w in (own_words if own_words is not None else story_words(q)) if df.get(w, 0) <= DF_MAX}
    if len(S) < 2:
        return []
    mine = {n for n in numbers_in(q) if n not in ('0', '1', '2')}
    nn_mine = {n for n in mine if n not in TRIVIAL_NUMS}
    ans_n = None            # rule N (round 4): the answer, when it is a plain number other than 0, 1, 2
    if ans is not None and re.fullmatch(r'\d[\d,]*\.?\d*', str(ans)) and norm_num(str(ans)) not in ('0', '1', '2'):
        ans_n = norm_num(str(ans))
    pool = (mine | {ans_n}) if ans_n else set(mine)
    solnums = {n for n in numbers_in(sol) if n not in ('0', '1', '2')} if ans_n else set()
    S_SPEC = {w for w in S if df.get(w, 0) <= SPEC_DF}      # the specific words of the teaser (not 'day', 'across' ...)
    score = {}
    wt = {w: 1 + 4 * (df.get(w, 0) <= VERY_RARE_DF) + 2 * (df.get(w, 0) <= RARE_DF) + (df.get(w, 0) <= SPEC_DF) for w in S}      # rarer words rank a sentence higher
    for w in sorted(S):
        for i in ix.inv.get(w, ()):
            score[i] = score.get(i, 0) + wt[w]
    # a window starts at a sentence; sentence scores are spread to the (up to) two sentences before it
    wscore = {}
    for i, c in sorted(score.items()):
        for st in (i - 2, i - 1, i):
            wscore[st] = wscore.get(st, 0) + c
    starts = [i for i, c in sorted(wscore.items(), key=lambda kv: (-kv[1], kv[0]))[:300] if c >= 2]
    ncount = {}
    for n in sorted(nn_mine):
        for i in ix.ninv.get(n, ()):
            for st in (i - 2, i - 1, i):
                ncount[st] = ncount.get(st, 0) + 1
    have = set(starts)
    starts += [i for i, c in sorted(ncount.items()) if c >= 3 and i not in have]
    if len(S) <= 4:       # short questions: every sentence that has all the story words
        full = sorted((i for i in score if len(S & ix.words[i]) == len(S)), key=lambda i: (len(ix.words[i]), i))
        starts = list(dict.fromkeys(starts + [x - k for x in full[:3000] for k in (0,)]))
    G = wgrams(q)
    G4 = mgrams(q)
    review = None
    seen = set()
    for st in starts:
        for ln in (1, 2, 3):
            a, b = st, st + ln - 1
            if (a, b) in seen or a < 0 or not ix.span_ok(a, b):
                continue
            seen.add((a, b))
            txt, ws, nums, rel = ix.window(a, b)
            shared = S & ws
            if len(shared) < 2:
                continue
            cov = len(shared) / len(S)
            cov_spec = len(shared & S_SPEC) / max(1, len(S_SPEC))
            rare = [w for w in shared if df.get(w, 0) <= RARE_DF]
            spec = [w for w in shared if df.get(w, 0) <= SPEC_DF]
            sn = len(mine & nums)
            nn = len(nn_mine & nums)
            dn = len({n for n in mine & nums if n not in COMMON_NUMS})
            why = None
            if len(S) >= 3:
                if cov >= 0.8 and len(shared) >= 4 and len(spec) >= 2 and sn >= 2:
                    why = 'same objects (%d of %d story words) and %d same numbers' % (len(shared), len(S), sn)
                elif cov >= 0.6 and len(shared) >= 3 and (len(spec) >= 3 or rare) and sn >= 3:
                    why = 'same objects (%d of %d story words) and %d same numbers' % (len(shared), len(S), sn)
                elif len(rare) >= 4 and cov >= 0.6:
                    why = 'same specific objects (%s)' % ', '.join(sorted(rare))
            if not why and cov >= 0.5 and len(shared) >= 3 and dn >= 2 and len(txt.split()) <= 120 and (rare or len(spec) >= 4):
                why = 'same story (%d of %d words) and the same numbers %s' % (len(shared), len(S), sorted(n for n in mine & nums if n not in COMMON_NUMS))
            if not why and len(G) >= 6 and cov >= 0.5:
                common = G & wgrams(txt)
                if len(common) >= 6 and len(common) / len(G) >= 0.45:
                    why = 'same wording with other numbers (%d of %d word triples)' % (len(common), len(G))
            if not why and len(S) >= 4 and cov >= 0.7 and len(shared) >= 4 and len(rare) >= 2:
                why = 'rule A (content words): same story skeleton, %d of %d story words (%d rare) with other numbers' % (len(shared), len(S), len(rare))
            if not why and len(shared) >= 3 and cov >= 0.4 and nn >= 1 and ((len(rare) >= 2 and cov >= 0.6 and nn >= 2) or (cov_spec >= 0.5 and len(spec) >= 2 and len(txt) <= 300 and any(df.get(w, 0) <= VERY_RARE_DF for w in shared))) and len(G & wgrams(txt)) >= 3:
                why = 'rule A2 (specific objects and a quantity): %d of %d story words (%s) and the same number %s' % (len(shared), len(S), ', '.join(sorted(rare)), sorted(nn_mine & nums))
            if not why and ans_n and ans_n in nums and len(txt) <= 400 and len(shared) >= 2 and cov >= 0.25 and spec and len(nums) <= 12:
                core = pool                      # every number of the question and the answer
                got = (pool | solnums) & nums
                if (len(core) >= 3 and core <= nums) or (len(core) == 2 and core <= nums and len(got) >= 4):
                    why = 'rule N (the question\'s numbers and the answer all in one source window): %s with the shared story words' % sorted(got, key=lambda x: float(x))
            if not why and nn >= 3 and dn >= 2 and len(shared) >= 3 and cov >= 0.4:
                why = 'rule B (numbers): %d of the same numbers %s (%d distinctive) and %d shared story words' % (nn, sorted(nn_mine & nums), dn, len(shared))
            c4 = None
            if not why and len(G4) >= 4 and cov >= 0.3:
                c4 = G4 & mgrams(txt)
                if len(c4) >= 3 and len(c4) >= 0.3 * len(G4):
                    why = 'rule C (four-word runs, numbers masked): %d of %d shared, e.g. "%s"' % (len(c4), len(G4), sorted(c4)[0])
            if why:
                return [('FAIL', '%s: "%s ..." (%s) words %s' % (why, txt[:100], rel, ','.join(sorted(shared))))]
            if review is None and c4 and len(c4) >= 2:
                review = ('REVIEW', 'rule C: two four-word runs shared with "%s ..." (%s): %s' % (txt[:80], rel, ' / '.join(sorted(c4)[:2])))
            if review is None and nn >= 3 and cov >= 0.4:
                review = ('REVIEW', 'rule B: %d of the same numbers %s as "%s ..." (%s)' % (nn, sorted(nn_mine & nums), txt[:80], rel))
            if review is None and len(S) >= 3 and cov >= 0.6 and len(shared) >= 3 and len(spec) >= 2:
                review = ('REVIEW', 'story words %d of %d like "%s ..." (%s)' % (len(shared), len(S), txt[:90], rel))
    return [review] if review else []


# ------------------------------------------------------------------ round 4: listed sequences and retired frames
def listed_sequences(q):
    """Comma-listed runs of at least 4 short words in a question ('red, red, blue, green', 'Mon, Tue, Wed, Thu'): the same list in a source is the same figure."""
    out = []
    for m in re.finditer(r"[a-z]+(?: [a-z]+)?(?:, (?:and )?[a-z]+(?: [a-z]+)?){2,}(?:,? and [a-z]+(?: [a-z]+)?)?", q.lower()):
        items = [x.strip() for x in re.split(r',\s*(?:and\s+)?|\s+and\s+', m.group(0)) if x.strip()]
        items = [re.sub(r'^(?:a|an|the|is|are|goes|go|repeats|pattern|again)\s+', '', x) for x in items]
        if len(items) >= 4 and all(len(x.split()) <= 2 for x in items):
            out.append(items)
    return out


def list_hits(q, ix, ans=None):
    """Rule L (round 4): a listed sequence of the question found in the same order in one source sentence that also holds a number of the question or the answer."""
    nums = {n for n in numbers_in(q) if n not in ('0', '1', '2')}
    if ans is not None and re.fullmatch(r'\d+', str(ans)):
        nums.add(str(ans))
    out = []
    for items in listed_sequences(q):
        norm = ', '.join(items)
        if len(set(items)) == len(items) and len(items) < 5:
            continue                       # a plain list of four different things is a coincidence; a repeating pattern or a long list is a figure
        stems = sorted({stem(w) for it in items for w in it.split() if stem(w) in ix.inv}, key=lambda w: len(ix.inv[w]))[:2]
        if not stems:
            continue
        cand = set(ix.inv[stems[0]])
        for w in stems[1:]:
            cand &= set(ix.inv[w])
        for i in sorted(cand):
            t = ' '.join(ix.txt[i].lower().replace(' and ', ', ').replace(',,', ',').split())
            if norm in re.sub(r',\s+', ', ', t):
                got = nums & set(ix.nums[i] | (ix.nums[i + 1] if i + 1 < len(ix.nums) and ix.file[i + 1] == ix.file[i] else frozenset()))
                if got:
                    out.append(('FAIL', 'rule L (listed sequence): "%s" with the number %s in "%s ..." (%s)' % (norm, sorted(got)[0], ix.txt[i][:90], ix.rels[ix.file[i]])))
                    break
    return out


def frame_hits(q, frames):
    """Retired frames (taxonomy.json 'retired_frames'): a question written in the words of a frame that our books already use."""
    out = []
    ql = q.lower()
    for fr in frames:
        if all(re.search(p, ql) for p in fr['all']) and not (fr.get('none') and any(re.search(p, ql) for p in fr['none'])):
            out.append(('FAIL', 'retired frame %s: %s' % (fr['id'], fr['why'])))
    return out


# ------------------------------------------------------------------ date arithmetic for the gap rules
MLEN = {365: [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31], 366: [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]}


def daynum(date, N):
    """0-based day of the year of 'MM-DD' in a year of N days (365 = no 29 Feb, 366 = leap); None when the date does not exist that year."""
    mm, dd = int(date[:2]), int(date[3:5])
    lens = MLEN[N]
    if dd > lens[mm - 1]:
        return None
    return sum(lens[:mm - 1]) + dd - 1


def cdist(a, b, N):
    d = abs(a - b)
    return min(d, N - d)


_GROUP_OF = {}
for _g, _subs in (TAX.T.get('same_idea_groups') or {}).items():
    for _s in _subs:
        _GROUP_OF[_s] = 'group:' + _g


_GROUP_FAM = {'group:' + _g: _subs[0].split('.')[0] for _g, _subs in (TAX.T.get('same_idea_groups') or {}).items()}


def gsub(e):
    """The unit the repeat rules count: a sub-structure, or the group of sub-structures that a parent sees as one idea (taxonomy 'same_idea_groups')."""
    return _GROUP_OF.get(e['sub'], e['sub'])


def is_small(a):
    return a.lstrip('-').isdigit() and abs(int(a)) < 10


def gap_rules(lv, items, fails):
    """Levels 1 and 2 (owner L1L2-GAP60): circular gap per sub-structure, family window, family never on consecutive days, answer window."""
    R = TAX.RULES
    gap, win = R['min_gap_days'][str(lv)], R['answer_window_days']
    fwin, fmax, smax = R['family_window_days'], R['family_max_in_window'], R['answer_small_max_in_window']
    seen = set()

    def add(msg):
        if msg not in seen:
            seen.add(msg)
            fails.append(msg)
    for N in (365, 366):
        pos = [(daynum(e['date'], N), e) for _, e in items]
        pos = [(p, e) for p, e in pos if p is not None]
        by_sub, by_fam, by_ans = {}, {}, {}
        for p, e in pos:
            by_sub.setdefault(gsub(e), []).append((p, e['id']))
            by_fam.setdefault(e['family'], []).append((p, e['id']))
            by_ans.setdefault(e['ans'], []).append((p, e['id']))
        for s, us in by_sub.items():
            for i in range(len(us)):
                for j in range(i + 1, len(us)):
                    d = cdist(us[i][0], us[j][0], N)
                    if d < gap:
                        add('L%d: sub-structure %s returns after %d days (minimum %d, %d-day year): %s and %s' % (lv, s, d, gap, N, us[i][1], us[j][1]))
        for f, us in by_fam.items():
            for i in range(len(us)):
                for j in range(i + 1, len(us)):
                    if cdist(us[i][0], us[j][0], N) == 1:
                        add('L%d: family %s on two consecutive days (%s and %s)' % (lv, f, us[i][1], us[j][1]))
            for p0, id0 in us:
                inside = [x for x in us if (x[0] - p0) % N < fwin]
                if len(inside) > fmax:
                    add('L%d: family %s used %d times in %d days (cap %d, %d-day year): %s' % (lv, f, len(inside), fwin, fmax, N, ', '.join(x[1] for x in inside)))
        for a, us in by_ans.items():
            if is_small(a):
                for p0, id0 in us:
                    inside = [x for x in us if (x[0] - p0) % N < win]
                    if len(inside) > smax:
                        add('L%d: single-digit answer %s used %d times in %d days (cap %d): %s' % (lv, a, len(inside), win, smax, ', '.join(x[1] for x in inside)))
            else:
                for i in range(len(us)):
                    for j in range(i + 1, len(us)):
                        if cdist(us[i][0], us[j][0], N) < win:
                            add('L%d: answer %s repeats within %d days (%s and %s)' % (lv, a, win, us[i][1], us[j][1]))


def quarter_rules(lv, items, fails):
    """Levels 3 to 6 (owner TEASER-STRICT): per quarter caps, a minimum gap across quarter boundaries, full-year answers."""
    R = TAX.RULES
    by_q = {}
    for mm, e in items:
        by_q.setdefault(TAX.quarter(mm), []).append(e)
    for q, es in sorted(by_q.items()):
        subs, fams = {}, {}
        for e in es:
            subs.setdefault(gsub(e), []).append(e['id'])
            fams.setdefault(e['family'], []).append(e['id'])
        for s, ids in subs.items():
            if len(ids) > R['max_per_sub_per_quarter']:
                fails.append('L%d quarter %d: sub-structure %s used %d times: %s' % (lv, q, s, len(ids), ', '.join(ids)))
        for f, ids in fams.items():
            if len(ids) > R['max_per_family_per_quarter']:
                fails.append('L%d quarter %d: family %s used %d times (cap %d): %s' % (lv, q, f, len(ids), R['max_per_family_per_quarter'], ', '.join(ids)))
    gapq = R['min_gap_days_across_quarters']
    seen = set()
    for N in (365, 366):
        uses = {}
        for mm, e in items:
            p = daynum(e['date'], N)
            if p is not None:
                uses.setdefault(gsub(e), []).append((p, e['id'], TAX.quarter(mm)))
        for s, us in uses.items():
            for i in range(len(us)):
                for j in range(i + 1, len(us)):
                    if us[i][2] != us[j][2] and cdist(us[i][0], us[j][0], N) < gapq:
                        msg = 'L%d: sub-structure %s returns after %d days across a quarter boundary (minimum %d): %s and %s' % (
                            lv, s, cdist(us[i][0], us[j][0], N), gapq, us[i][1], us[j][1])
                        if msg not in seen:
                            seen.add(msg)
                            fails.append(msg)
    seen_ans = {}
    for mm, e in items:
        seen_ans.setdefault(e['ans'], []).append(e['id'])
    for a, ids in seen_ans.items():
        if (not is_small(a) and len(ids) > 1) or (is_small(a) and len(ids) > MAX_SMALL):
            fails.append('L%d: answer %s repeats (%s)' % (lv, a, ', '.join(ids)))


def structure_rules(all_by_level, stock):
    """The per-level structure rules over every released month.  all_by_level = {level: [(month, entry), ...]}.
    Levels 1 and 2 follow the gap rules (L1L2-GAP60), Levels 3 to 6 the quarter rules (TEASER-STRICT).  Returns (failures, report lines)."""
    global_fails, struct_lines = [], []
    levels = sorted(all_by_level)
    R = TAX.RULES
    for lv in levels:
        items = all_by_level[lv]
        if str(lv) in R['min_gap_days']:
            gap_rules(lv, items, global_fails)
            fams, subs = {}, {}
            for mm, e in items:
                fams.setdefault(e['family'], []).append(e['id'])
                subs.setdefault(e['sub'], []).append(e['id'])
            struct_lines.append('- Level %d (gap rule, %d days): %d puzzles, %d distinct sub-structures (none twice within the gap), %d families, most in one family %d' % (
                lv, R['min_gap_days'][str(lv)], len(items), len(subs), len(fams), max(len(v) for v in fams.values())))
        else:
            quarter_rules(lv, items, global_fails)
            by_q = {}
            for mm, e in items:
                by_q.setdefault(TAX.quarter(mm), []).append(e)
            for q, es in sorted(by_q.items()):
                fams = {}
                for e in es:
                    fams.setdefault(e['family'], []).append(e['id'])
                struct_lines.append('- Level %d, quarter %d: %d puzzles, %d distinct sub-structures, %d families, most in one family %d' % (
                    lv, q, len(es), len({e['sub'] for e in es}), len(fams), max(len(v) for v in fams.values())))
        # numbers shared between two puzzles of the same level
        nums = [(e['id'], {n for n in numbers_in(e['q']) if n not in ('0', '1', '2') and not (n in ('5', '10', '20', '50') and 'cent' in e['q'])}) for _, e in items]
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                a, b = nums[i][1], nums[j][1]
                sh = a & b
                big = [n for n in sh if int(float(n)) >= 10]
                if (len(sh) >= 4 or (len(sh) >= TAX.RULES['number_overlap_fail'] and len(big) >= 2)) and len(sh) >= 0.6 * min(len(a), len(b)):
                    global_fails.append('L%d: %s and %s share the numbers %s' % (lv, nums[i][0], nums[j][0], sorted(sh)))
        # frames unique
        fr = {}
        for mm, e in items:
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
    # the same story twice in one level (content words, as against the sources)
    for lv in levels:
        ws = [(e['id'], story_words(e['q']), {n for n in numbers_in(e['q']) if n not in ('0', '1', '2')}) for _, e in all_by_level[lv]]
        for i in range(len(ws)):
            for j in range(i + 1, len(ws)):
                a, b = ws[i][1], ws[j][1]
                if len(a) < 3 or len(b) < 3:
                    continue
                sh = a & b
                cov = len(sh) / min(len(a), len(b))
                sn = len(ws[i][2] & ws[j][2])
                if (len(sh) >= 4 and cov >= 0.85) or (len(sh) >= 3 and cov >= 0.6 and sn >= 2):
                    global_fails.append('L%d: %s and %s tell the same story (shared words %s, shared numbers %d)' % (lv, ws[i][0], ws[j][0], ','.join(sorted(sh)), sn))
    # round 4 (owner ruling C3): puzzles at DIFFERENT levels may not share numbers and answer, nor the same story skeleton
    flat_all = [(lv, e) for lv in levels for _, e in all_by_level[lv]]
    info = {}
    for lv, e in flat_all:
        info[e['id']] = ({n for n in numbers_in(e['q']) if n not in ('0', '1', '2')}, story_words(e['q']))
    for i in range(len(flat_all)):
        for j in range(i + 1, len(flat_all)):
            (la, a), (lb, b) = flat_all[i], flat_all[j]
            if la == lb:
                continue
            na, wa = info[a['id']]
            nb, wb = info[b['id']]
            sh = na & nb
            if a['type'] == 'n' and a['ans'] == b['ans'] and a['ans'] not in ('0', '1', '2') and (len(sh) >= (2 if Fr(a['ans']) >= 10 else 3)):
                global_fails.append('%s (L%d) and %s (L%d): same answer %s and shared numbers %s at two levels' % (a['id'], la, b['id'], lb, a['ans'], sorted(sh, key=float)))
            elif len(na) >= 3 and na == nb and (len(na) >= 4 or max(float(x) for x in na) > 12):
                global_fails.append('%s (L%d) and %s (L%d): the same numbers %s at two levels' % (a['id'], la, b['id'], lb, sorted(na, key=float)))
            if len(wa) >= 3 and len(wb) >= 3:
                w = wa & wb
                cov = len(w) / min(len(wa), len(wb))
                if (len(w) >= 4 and cov >= 0.75) or (len(w) >= 5 and cov >= 0.6):
                    global_fails.append('%s (L%d) and %s (L%d): the same story skeleton at two levels (shared words %s)' % (a['id'], la, b['id'], lb, ','.join(sorted(w))))
    return global_fails, struct_lines


def capacity_lines(levels, bank_counts=None):
    """What the taxonomy can supply per level against what a year (Levels 1, 2: gap rule) or a quarter (Levels 3 to 6) needs.
    Returns (lines, capacity_fails)."""
    R = TAX.RULES
    out = ['', '## Capacity of the taxonomy (true numbers, after merging look-alike sub-structures)', '',
           'Levels 1 and 2 (gap rule): a sub-structure may be used floor(365 / gap) times a year, so 365 puzzles need ceil(365 / uses) sub-structures; the owner-chosen minimum '
           'slack is %d (a removed or retired sub-structure must not break a year). A family may supply at most %d puzzles in any %d days, so the families must also be wide enough: '
           'sum over families of min(subs, cap) per %d days must reach the number of days.' % (
               R['capacity_min_slack'], R['family_max_in_window'], R['family_window_days'], R['family_window_days']),
           'Levels 3 to 6 (quarter rule): one use per sub-structure and at most %d per family per quarter, so a quarter of up to 92 days needs sum over families of min(%d, subs in the family) >= 92.' % (
               R['max_per_family_per_quarter'], R['max_per_family_per_quarter']), '',
           '| Level | Sub-structures | Families | Rule | Uses per sub a year | Needed | Slack | True capacity (family-capped) | Verdict |', '|---|---|---|---|---|---|---|---|---|']
    fails = []
    for lv in range(1, 7):
        subs = sorted({_GROUP_OF.get(s, s) for s, d in TAX.SUBS.items() if lv in d['levels']})      # round 4: sub-structures a parent sees as one idea count once
        fam = {}
        for s in subs:
            fam.setdefault(_GROUP_FAM.get(s) or s.split('.')[0], []).append(s)
        if str(lv) in R['min_gap_days']:
            gap = R['min_gap_days'][str(lv)]
            uses = 365 // gap
            need = -(-365 // uses)
            slack = len(subs) - need
            cap = sum(min(R['family_max_in_window'], len(v)) for v in fam.values())      # distinct puzzles one family-window of 60 days can show
            famyear = sum(min(uses * len(v), 365 * R['family_max_in_window'] // R['family_window_days']) for v in fam.values())
            verdict = 'ok' if slack >= R['capacity_min_slack'] and famyear >= 365 else 'FAIL: slack %d below %d (needs %d or more sub-structures)%s' % (
                slack, R['capacity_min_slack'], need + R['capacity_min_slack'], '' if famyear >= 365 else '; families too narrow (%d a year)' % famyear)
            if verdict != 'ok':
                fails.append('Level %d: %d sub-structures, %d needed for 365 days at gap %d, slack %d; families allow %d puzzles a year' % (lv, len(subs), need, gap, slack, famyear))
            out.append('| %d | %d | %d | gap %d days | %d | %d | %d | %d a year | %s |' % (lv, len(subs), len(fam), gap, uses, need, slack, famyear, verdict))
        else:
            cap = sum(min(R['max_per_family_per_quarter'], len(v)) for v in fam.values())
            verdict = 'ok' if cap >= 92 else 'FAIL: short by %d' % (92 - cap)
            if cap < 92:
                fails.append('Level %d: quarter capacity %d, a quarter needs 92' % (lv, cap))
            out.append('| %d | %d | %d | once a quarter | 1 per quarter | 92 | %d | %d per quarter | %s |' % (lv, len(subs), len(fam), cap - 92, cap, verdict))
    return out, fails


def answer_feasibility(all_by_level):
    """Levels 3 to 6 keep the full-year answer rule (an answer of 10 or more once per level, a single digit at most MAX_SMALL times): report whether a year can fit."""
    out = ['', '## Full-year answer rule at Levels 3 to 6 (feasibility)', '',
           '| Level | Puzzles so far | Single-digit answers so far | Share | Projected single-digit answers in 365 | Allowed (9 values x %d) | Verdict |' % MAX_SMALL, '|---|---|---|---|---|---|---|']
    warn = []
    for lv in sorted(all_by_level):
        if lv < 3:
            continue
        items = all_by_level[lv]
        small = sum(1 for _, e in items if is_small(e['ans']))
        share = small / len(items)
        proj = round(share * 365)
        ok = proj <= 9 * MAX_SMALL
        if not ok:
            warn.append('Level %d: %d%% single-digit answers so far, a year would need about %d (limit %d)' % (lv, round(share * 100), proj, 9 * MAX_SMALL))
        out.append('| %d | %d | %d | %d%% | %d | %d | %s |' % (lv, len(items), small, round(share * 100), proj, 9 * MAX_SMALL, 'ok' if ok else 'WARNING: aim for fewer single-digit answers'))
    return out, warn


def mk(lv, date, sub, fam, ans, n, q=None):
    """A synthetic bank entry for the self-test (nothing else about it matters to the structure rules)."""
    return (date[:2], dict(id='L%d-t%d' % (lv, n), date=date, level=lv, frame='t%d_%d' % (lv, n), sub=sub, family=fam, ans=ans,
                           q=q or 'Item %d for test %d zebra%d.' % (n * 7 + 11, n, n)))


def selftest():
    """Break the rules in known ways and check that they notice (python3 verify_bank.py --selftest)."""
    import copy
    man = json.load(open(os.path.join(HERE, 'manifest.json')))
    base = {}
    for mm in man['released']:
        for lv, items in json.load(open(os.path.join(HERE, 'batches', 'm%s' % mm, 'bank.json'), encoding='utf-8'))['levels'].items():
            for e in items:
                base.setdefault(int(lv), []).append((mm, e))
    stock = (dup_check.stock(NGF) | stock_local()) if dup_check else set()
    clean, _ = structure_rules(base, stock)
    cases, bad = [], []

    def synth(lv, rows, qs=None):
        """rows = [(date, sub, family, ans)] -> structure failures for a synthetic level."""
        d = {lv: [mk(lv, dt, sub, fam, ans, i, qs[i] if qs else None) for i, (dt, sub, fam, ans) in enumerate(rows)]}
        f, _ = structure_rules(d, stock)
        return f

    def expect(name, fails, want):
        good = (any(want in x for x in fails)) if want else (not fails)
        cases.append((name, good, fails[:2]))
    # --- Levels 1 and 2: gap 60, circular, both year lengths
    S, F = 'a.s1', 'a'
    expect('L1 sub 59 days apart fails', synth(1, [('03-01', S, F, '11'), ('04-29', S, F, '12')]), 'returns after 59 days')
    expect('L1 sub 60 days apart passes', synth(1, [('03-01', S, F, '11'), ('04-30', S, F, '12')]), None)
    expect('L1 sub 31 Oct / next year 59 days apart (circular) fails', synth(1, [('11-04', S, F, '11'), ('01-02', S, F, '12')]), 'returns after 59 days')
    expect('L1 sub 60 days apart across the new year (circular) passes', synth(1, [('11-03', S, F, '11'), ('01-02', S, F, '12')]), None)
    expect('L1 sub 1 Jan and 1 Mar fails only because a non-leap year has no 29 Feb', synth(1, [('01-01', S, F, '11'), ('03-01', S, F, '12')]), 'returns after 59 days')
    expect('L1 sub 28 Feb and 1 Mar are counted', synth(1, [('02-28', S, F, '11'), ('03-01', S, F, '12')]), 'returns after')
    expect('L2 sub 59 days apart fails', synth(2, [('05-01', S, F, '11'), ('06-29', S, F, '12')]), 'returns after 59 days')
    expect('L1 family on two consecutive days fails', synth(1, [('03-01', 'a.s1', F, '11'), ('03-02', 'a.s2', F, '12')]), 'consecutive days')
    expect('L1 family twice with a day between passes', synth(1, [('03-01', 'a.s1', F, '11'), ('03-03', 'a.s2', F, '12')]), None)
    expect('L1 family 4 times in 60 days fails', synth(1, [('03-01', 'a.s1', F, '11'), ('03-10', 'a.s2', F, '12'), ('03-20', 'a.s3', F, '13'), ('03-30', 'a.s4', F, '14')]), 'times in 60 days')
    expect('L1 family 3 times in 60 days passes', synth(1, [('03-01', 'a.s1', F, '11'), ('03-10', 'a.s2', F, '12'), ('03-20', 'a.s3', F, '13')]), None)
    expect('L1 the same answer (10 or more) 59 days apart fails', synth(1, [('03-01', 'a.s1', 'a', '41'), ('04-29', 'b.s2', 'b', '41')]), 'repeats within 60 days')
    expect('L1 the same answer 60 days apart passes', synth(1, [('03-01', 'a.s1', 'a', '41'), ('04-30', 'b.s2', 'b', '41')]), None)
    expect('L1 a single-digit answer 3 times in 60 days fails', synth(1, [('03-01', 'a.s1', 'a', '7'), ('03-12', 'b.s2', 'b', '7'), ('03-23', 'c.s3', 'c', '7')]), 'single-digit answer')
    expect('L1 a single-digit answer twice in 60 days passes', synth(1, [('03-01', 'a.s1', 'a', '7'), ('03-12', 'b.s2', 'b', '7')]), None)
    expect('L1 the same sub twice in one quarter is NOT a quarter-rule failure when 60 days apart', synth(1, [('01-01', S, F, '11'), ('03-02', S, F, '12')]), None)
    # --- Levels 3 to 6: once per quarter, 30 days across quarter boundaries
    expect('L3 sub 30 days apart across a quarter boundary passes', synth(3, [('12-31', S, F, '11'), ('01-30', S, F, '12')]), None)
    expect('L3 sub 29 days apart across a quarter boundary (31 Dec / 29 Jan) fails', synth(3, [('12-31', S, F, '11'), ('01-29', S, F, '12')]), 'across a quarter boundary')
    expect('L4 sub 29 days apart across 31 Mar / 29 Apr fails', synth(4, [('03-31', S, F, '11'), ('04-29', S, F, '12')]), 'across a quarter boundary')
    expect('L4 sub 30 days apart across 31 Mar / 30 Apr passes', synth(4, [('03-31', S, F, '11'), ('04-30', S, F, '12')]), None)
    expect('L5 the same sub twice in a quarter fails', synth(5, [('05-01', S, F, '11'), ('06-30', S, F, '12')]), 'sub-structure')
    expect('L6 four puzzles of one family in a quarter fails', synth(6, [('05-01', 'a.s1', F, '11'), ('05-09', 'a.s2', F, '12'), ('05-17', 'a.s3', F, '13'), ('05-25', 'a.s4', F, '14')]), 'family')
    expect('L3 the same answer (10 or more) twice in a level fails', synth(3, [('05-01', 'a.s1', 'a', '55'), ('09-01', 'b.s2', 'b', '55')]), 'answer')

    # --- the real bank: break it in known ways (the old probes)
    def mutate(name, fn, want):
        d = copy.deepcopy(base)
        fn(d)
        f, _ = structure_rules(d, stock)
        new = [x for x in f if x not in clean]
        cases.append((name, any(want in x for x in new), new[:2]))
    two = [('05-01', 'a.s1', 'a', '41'), ('09-01', 'b.s2', 'b', '42')]
    expect('a 7-word run shared by two puzzles of a level fails',
           synth(4, two, ['Quince umbrellas travel beyond violet harbours before sunrise tomorrow morning at 17.', 'Cedar lanterns drift beyond violet harbours before sunrise tomorrow morning at 19.']), 'word run')
    expect('two puzzles of a level with the same four numbers fail',
           synth(6, two, ['Alder kites hold 14 pearls and 25 shells and 36 acorns and 47 stones.', 'Birch drums keep 14 coins, 25 beads, 36 nails and 47 pins tonight.']), 'share the numbers')
    expect('two puzzles of a level with different numbers pass',
           synth(6, two, ['Alder kites hold 14 pearls and 25 shells.', 'Birch drums keep 63 coins and 8 beads tonight.']), None)
    # --- the story check
    sidx = story_index()
    for name, q, want in (
        ('story: the snail-and-wall puzzle with new numbers is caught', 'A snail climbs a 20 cm wall. Each day it climbs 5 cm. Each night it slides back 2 cm. On which day does it first reach the top?', 'FAIL'),
        ('story: lolly sticks and a row of triangles with new numbers is at least a REVIEW', 'Sam makes a row of triangles with lolly sticks. One triangle uses 3 sticks. Two triangles joined side by side use 5 sticks. How many sticks do 8 triangles use?', 'ANY'),
        ('story: "Today is Wednesday ... what day of the week" is caught', 'Today is Wednesday. What day of the week will it be 365 days from today?', 'FAIL'),
        ('story: a fan at 15% off with 9% GST on $120 is caught', 'A fan costs $120 before GST. It is sold at 15% off. What is the sale price before GST?', 'FAIL'),
        ('story: a new story (a bakery sells tarts in trays) is not flagged', 'A bakery bakes tarts on trays. Every tray holds 12 tarts. The baker fills 7 trays and sells 30 tarts. How many tarts are left?', None)):
        got = [sev for sev, _ in story_hits(q, sidx)]
        cases.append((name, bool(got) if want == 'ANY' else ((want in got) if want else ('FAIL' not in got)), got))
    # --- round 3: the near-copies of AUDIT_ROUND3 (their round-2 wording) against the widened sources
    probes = json.load(open(os.path.join(HERE, 'selftest_probes.json'), encoding='utf-8'))
    for pid, text in probes['must_fail_text'].items():
        got = [sev for sev, _ in story_hits(text, sidx)]
        cases.append(('round 3 probe %s (round-2 wording) is a FAIL of the text rules' % pid, 'FAIL' in got, got))
    # round 4: the four High items of AUDIT_ROUND4 (round-3 wording) and the fan at Level 4, which the round-3 verifier passed
    for pid, pr in probes.get('round4_high', {}).items():
        got = [sev for sev, _ in (story_hits(pr['q'], sidx, ans=pr['ans'], sol=pr['sol']) + list_hits(pr['q'], sidx, ans=pr['ans']) + frame_hits(pr['q'], TAX.T.get('retired_frames', [])))]
        cases.append(('round 4 probe %s (round-3 wording) is a FAIL of the round-4 text rules' % pid, 'FAIL' in got, got))
        cases.append(('round 4 probe %s: its frame %s is not allowed at Level %d any more' % (pid, pr['sub'], pr['level']), pr['sub'] in TAX.SUBS and pr['level'] not in TAX.SUBS[pr['sub']]['levels'], TAX.SUBS.get(pr['sub'], {}).get('levels')))
    for pid, sub in probes['retired_sub'].items():
        cases.append(('round 3 probe %s: sub-structure %s is retired (no level allows it)' % (pid, sub), TAX.SUBS[sub]['levels'] == [], TAX.SUBS[sub]['levels']))
    rels = {os.path.relpath(f, ROOT).replace(os.sep, '/') for f in source_files()}
    for r in probes['sources_must_include']:
        cases.append(('source list includes %s' % r, r in rels, ''))
    cases.append(('source list is the same on a second run (sorted, reproducible)', [os.path.relpath(f, ROOT) for f in source_files()] == [os.path.relpath(f, ROOT) for f in source_files()], ''))
    cases.append(('the source lock is satisfied on this tree', not lock_problems(), lock_problems()))
    cases.append(('the source lock refuses a tracked-only tree (no docs, no private sources)', bool(lock_problems({'docs': 3, 'extension': 1})), ''))
    a1 = story_hits(probes['must_fail_text']['L3-nightbus'], sidx)
    a2 = story_hits(probes['must_fail_text']['L3-nightbus'], sidx)
    cases.append(('the same question gives the same verdict twice', a1 == a2, ''))
    for c in cases:
        print(('PASS ' if c[1] else 'FAIL ') + c[0], '' if c[1] else c[2])
        if not c[1]:
            bad.append(c[0])
    # --- taxonomy matching
    ent = dict(kind='scan', p=dict(preds=[['palindrome', None]]))
    for sid, e, want in (('digit_puzzles.palindromes', ent, True), ('digit_puzzles.count_by_digit_rule', ent, False), ('money.shopping', ent, False)):
        got = TAX.matches(sid, e)[0]
        print(('PASS ' if got == want else 'FAIL ') + 'taxonomy match %s -> %s' % (sid, got))
        if got != want:
            bad.append(sid)
    # --- every round-2 kind: solver and independent checker agree on a worked instance, with exactly one answer
    import kinds
    import samples_r2
    import samples_r3
    allsamples = dict(samples_r2.SAMPLES)
    allsamples.update(samples_r3.SAMPLES)
    for k, plist in allsamples.items():
        for p in plist:
            try:
                a, _ = kinds.SOLVE[k](**p)
                b = brute.BRUTE[k](**p)
                good = len(b) == 1 and ({str(x).lower() for x in b} == {str(a).lower()} if isinstance(a, str) else {Fr(x) for x in b} == {Fr(a)})
            except Exception as ex:
                good = False
                a = b = repr(ex)
            if not good:
                print('FAIL kind %s %s: solver %s checker %s' % (k, p, a, b))
                bad.append('kind ' + k)
    print('kinds checked: %d (round 2: %d, round 3: %d)' % (len(allsamples), len(samples_r2.SAMPLES), len(samples_r3.SAMPLES)))
    for d in TAX.SUBS.values():
        if d.get('round') in (2, 3) and not any(k in allsamples for k in d['kinds']) and d['kinds'] != ['rect']:
            print('FAIL no sample for', d['name'])
            bad.append(d['name'])
    print('selftest: %d problems' % len(bad))
    sys.exit(1 if bad else 0)


# ------------------------------------------------------------------ round 5 (audit C2): one-sentence questions, numbers with units, the answer counted
# Rules S, G and N2 use DOMAIN-AWARE content words (probability, angle, dice, fraction ... are kept; they are dropped from the story words of rules A..C),
# so a short question such as "At 5 o'clock, what is the smaller angle between a clock's hour hand and its minute hand?" can still be matched to a
# source sentence.  Replayed in --selftest with the round-3 and round-5 wordings of L6-dice8, L4-clockfive, L5-tank and L4-chairs24.
GLUE = set('find write give answer numbers number many much work out calculate show tell one two three four five six seven eight nine ten eleven twelve'.split())
CW_CAP = 6000            # a word found in more source sentences than this does not retrieve candidates (it still counts in the overlap)
_CW_MEMO = {}


def cwords(text):
    """Domain-aware content words of a text: stems of the words that are not function words, glue words ('find', 'write' ...) or names."""
    t = text.replace('’', "'").lower()
    out = set()
    for w in re.findall(r"[a-z]+(?:'[a-z]+)?", t):
        r = _CW_MEMO.get(w)
        if r is None:
            w2 = re.sub(r"'s$", '', w)
            sw = stem(w2)
            r = sw if (len(sw) > 2 and w2 not in FUNC and sw not in FUNC and w2 not in NAMES and w2 not in GLUE) else ''
            _CW_MEMO[w] = r
        if r:
            out.add(r)
    return out


class CWIdx:
    """Sentence index with domain-aware content words: per-sentence word sets and inverted lists for the words that are not too common."""

    def __init__(self, ix):
        self.ix = ix
        self.words = [None] * len(ix.txt)
        df = {}
        for i, t in enumerate(ix.txt):
            ws = frozenset(cwords(t))
            self.words[i] = ws
            for w in ws:
                df[w] = df.get(w, 0) + 1
        self.df = df
        inv = {}
        for i, ws in enumerate(self.words):
            for w in ws:
                if df[w] <= CW_CAP:
                    inv.setdefault(w, array('I')).append(i)
        self.inv = inv


_CWIDX = {}


def cw_index(ix):
    k = id(ix)
    if k not in _CWIDX:
        _CWIDX[k] = CWIdx(ix)
    return _CWIDX[k]


def wtoks2(text):
    return re.findall(r"[a-z]+(?:'[a-z]+)?|#", re.sub(r'\d[\d,]*\.?\d*', '#', text.lower().replace('\u2019', "'")))


def split_sentences(q):
    return [s for s in re.split(r'(?<=[.?!])"?\s+', q.strip()) if s.strip()]


def num_unit_grams(sentence):
    """Word three-grams of one sentence that contain a number (kept as written): '30 cm by', 'cm by 25', '2 m 45', 'm 45 cm'."""
    t = re.findall(r"\d[\d,]*\.?\d*|[a-z°²³%$]+(?:'[a-z]+)?", sentence.lower().replace('’', "'"))
    t = [x.replace(',', '') if x[0].isdigit() else x for x in t]
    out = set()
    for i in range(len(t) - 2):
        g = t[i:i + 3]
        if any(x[0].isdigit() for x in g) and any((not x[0].isdigit()) and x not in FUNC for x in g):
            out.add(' '.join(g))
    return out


def extra_hits(q, ans, sol, cw):
    """Rules S, G and N2 of AUDIT_ROUND5 (C2).  Returns [(severity, detail)].
      S  : a question sentence with >= 4 content words whose Jaccard similarity with ONE source sentence is >= 0.6 (>= 4 shared words) is a FAIL, unless
           that sentence is a stock phrase; and the whole question against a window of up to three source sentences: >= 70% of its content words
           (>= 5 shared) and every one of its numbers other than 0, 1, 2, 10, 100, 1000 in the window is a FAIL (one-sentence questions have too few
           story words for rules A to C);
      G  : three-word grams that contain a number ('30 cm by 25 cm', '2 m 45 cm') shared with a window: >= 3 is a REVIEW, >= 5 a FAIL;
      N2 : the answer and at least two other numbers of the question (the conversion numbers 10, 100, 1000 are not counted) in a window of up to three
           sentences (at most 400 characters) that shares >= 3 content words with the question is a FAIL."""
    ix = cw.ix
    S = cwords(q)
    qs = [(s, cwords(s)) for s in split_sentences(q)]
    mine = {n for n in numbers_in(q) if n not in TRIVIAL_NUMS and n not in ('0', '1', '2')}
    ans_n = norm_num(str(ans)) if ans is not None and re.fullmatch(r'\d[\d,]*\.?\d*', str(ans)) and norm_num(str(ans)) not in TRIVIAL_NUMS and norm_num(str(ans)) not in ('0', '1', '2') else None
    pool = mine | ({ans_n} if ans_n else set())
    grams = {}
    for s, _ in qs:
        for g in num_unit_grams(s):
            grams[g] = 1
    score = {}
    for w in S:
        lst = cw.inv.get(w)
        if lst is None:
            continue
        wt = 1.0 + 8.0 / (1.0 + cw.df.get(w, 1) / 40.0)
        for i in lst:
            score[i] = score.get(i, 0) + wt
    # candidate windows start at the best scoring sentences (and the two before them)
    wscore = {}
    for i, c in score.items():
        for st in (i - 2, i - 1, i):
            wscore[st] = wscore.get(st, 0) + c
    starts = [i for i, c in sorted(wscore.items(), key=lambda kv: (-kv[1], kv[0]))[:1500] if c >= 1.2]
    # windows that hold the numbers of the question and the answer
    ncount = {}
    for n in sorted(pool):
        for i in ix.ninv.get(n, ()):
            for st in (i - 2, i - 1, i):
                ncount.setdefault(st, set()).add(n)
    have = set(starts)
    starts += [i for i, c in sorted(ncount.items()) if len(c) >= 3 and i not in have][:400]
    # windows that hold number-unit grams of the question (G): sentences that contain one of its numbers
    if grams:
        gnums = {n for n in numbers_in(q) if n not in TRIVIAL_NUMS and n not in ('0', '1', '2')}
        hits = set()
        for n in sorted(gnums):
            for i in ix.ninv.get(n, ()):
                if i not in hits and any(g in grams for g in num_unit_grams(ix.txt[i])):
                    hits.add(i)
        have = set(starts)
        for i in sorted(hits):
            for st in (i - 1, i):
                if st not in have:
                    starts.append(st)
                    have.add(st)
    review = None
    seen = set()
    for st in starts:
        for ln in (1, 2, 3):
            a, b = st, st + ln - 1
            if (a, b) in seen or a < 0 or not ix.span_ok(a, b):
                continue
            seen.add((a, b))
            ws = set()
            nums = set()
            for i in range(a, b + 1):
                ws |= cw.words[i]
                nums |= ix.nums[i]
            txt = ' '.join(ix.txt[a:b + 1])
            shared = S & ws
            why = None
            # S, one sentence against one sentence (content-word Jaccard >= 0.6 and the words really are the same words)
            if ln == 1:
                tb = wtoks2(ix.txt[a])
                for s, sw in qs:
                    ta = wtoks2(s)
                    short, long_ = (ta, tb) if len(ta) <= len(tb) else (tb, ta)
                    ssh = set(short)
                    contain = len(ssh & set(long_)) / max(1, len(ssh))
                    ratio = len(short) / max(1, len(long_))
                    has_num = '#' in ta
                    # S3: the same long sentence with other numbers
                    if len(ssh) >= 7 and len(ssh & set(long_)) >= 7 and contain >= 0.85 and len(sw & cw.words[a]) >= 3:
                        named = bool({t for t in ssh & set(long_) if t in NAMES})
                        if ratio >= 0.7 and contain >= 0.9 and len(ssh) >= 8 and has_num and (named or (len(ssh) >= 11 and ratio >= 0.8)):
                            why = 'rule S3 (the same sentence with other numbers, %d words): "%s" is like "%s"' % (len(short), s[:80], ix.txt[a][:90])
                            break
                        elif ratio >= 0.65 and review is None:
                            review = ('REVIEW', 'rule S3: the sentence "%s" is like "%s" (%s)' % (s[:80], ix.txt[a][:80], ix.rels[ix.file[a]]))
                    if len(sw) >= 4:
                        sh = sw & cw.words[a]
                        union = len(sw | cw.words[a])
                        if len(sh) >= 4 and len(sh) / union >= 0.6 and len(cw.words[a]) >= 4:
                            if contain >= 0.8 and ratio >= 0.5 and has_num and len(ta) >= 10 and len(sh) >= 5:
                                why = 'rule S (one sentence, Jaccard %.2f, %d shared content words): "%s" is like "%s"' % (len(sh) / union, len(sh), s[:80], ix.txt[a][:90])
                                break
                            elif review is None:
                                review = ('REVIEW', 'rule S: sentence "%s" shares %d content words with "%s" (%s)' % (s[:70], len(sh), ix.txt[a][:70], ix.rels[ix.file[a]]))
            # S, whole question against a window
            if not why and len(S) >= 5 and len(shared) >= 5 and len(shared) / len(S) >= 0.7 and (not mine or mine <= nums):
                spec_n = len([w for w in shared if cw.df.get(w, 0) <= 2500])
                if len(txt) <= 400 and spec_n >= 3 and (mine or len(shared) >= 7) and '?' in txt:
                    why = 'rule S (window): %d of %d content words (%s) and all the numbers in "%s ..."' % (len(shared), len(S), ','.join(sorted(shared)), txt[:90])
                elif review is None:
                    review = ('REVIEW', 'rule S (window): %d of %d content words (%s) in "%s ..." (%s)' % (len(shared), len(S), ','.join(sorted(shared)), txt[:70], ix.rels[ix.file[a]]))
            # N2: the answer and two more numbers
            if not why and ans_n and ans_n in nums and len(txt) <= 400 and len(shared) >= 4 and len(nums) <= 14 and '|' not in txt:
                big = [n for n in mine & nums if float(n) >= 12]
                if len(big) >= 2:
                    why = 'rule N2 (the answer %s and the numbers %s in one source window with %d shared content words): "%s ..."' % (ans_n, sorted(mine & nums, key=float), len(shared), txt[:90])
            # G
            if not why and grams:
                got = set()
                for i in range(a, b + 1):
                    got |= {g for g in num_unit_grams(ix.txt[i]) if g in grams}
                if len(got) >= 5:
                    why = 'rule G (numbers with units): %d shared grams, e.g. "%s" in "%s ..."' % (len(got), sorted(got)[0], txt[:90])
                elif len(got) >= 3 and review is None and len(shared) >= 1:
                    review = ('REVIEW', 'rule G: %d shared number-unit grams (%s) in "%s ..." (%s)' % (len(got), ' / '.join(sorted(got)[:3]), txt[:80], ix.rels[ix.file[a]]))
            if why:
                if STOCK_SENT and (why.startswith('rule S (one sentence') or why.startswith('rule S3')):
                    qsent = [s for s, _ in qs if s[:80] in why][0] if any(s[:80] in why for s, _ in qs) else ''
                    if qsent and re.sub(r'\d+', '#', qsent.lower().rstrip('.?!')) in STOCK_SENT:
                        continue
                return [('FAIL', '%s (%s)' % (why, ix.rels[ix.file[a]]))]
    return [review] if review else []


STOCK_SENT = set()      # whole sentences of stock_phrases.txt (numbers masked) that may repeat


def load_stock_sentences():
    p = os.path.join(HERE, 'stock_phrases.txt')
    STOCK_SENT.clear()
    if os.path.exists(p):
        for line in open(p, encoding='utf-8'):
            line = line.strip().lower()
            if line and not line.startswith('#'):
                STOCK_SENT.add(re.sub(r'\d+', '#', line.rstrip('.?!')))


def main():
    if '--update-lock' in sys.argv:
        update_lock()
        return
    if '--selftest' in sys.argv:
        selftest()
    man = json.load(open(os.path.join(HERE, 'manifest.json')))
    digest, nfiles, nbytes, per_root = source_digest()
    print('sources: %d files, %.1f MB, digest %s' % (nfiles, nbytes / 1e6, digest[:16]))
    problems = lock_problems()
    if problems:
        print('INVALID VERIFICATION: the source tree is incomplete, so a "0 FAIL" would mean nothing.')
        for p in problems:
            print('  ', p)
        sys.exit(2)
    SRC_LINE = ('Sources searched (whole working tree, tracked or not): %d files, %.1f MB, sha256 %s.  Files per root: %s.' % (
        nfiles, nbytes / 1e6, digest[:24], ', '.join('%s %d' % kv for kv in sorted(per_root.items()))))
    months = [a for a in sys.argv[1:] if not a.startswith('--')] or man['released']
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
    R = TAX.RULES
    struct_lines = ['# Structure report (taxonomy.json)', '', SRC_LINE, '',
                    'Rules. Levels 3 to 6 (TEASER-STRICT): per level and calendar quarter at most %d puzzle per sub-structure and %d per family; the same sub-structure never within %d days of itself across a quarter boundary; '
                    'an answer of 10 or more appears once per level and a single digit at most %d times. '
                    'Levels 1 and 2 (L1L2-GAP60): the same sub-structure at least %d days apart (circular, 365- and 366-day year), a family at most %d times in any %d days and never on consecutive days, '
                    'an answer not repeated within %d days and a single-digit answer at most %d times in %d days. '
                    'All levels: no repeated frame, no two puzzles with most numbers or the same story in common; '
                    'the sub-structures used by the fixed puzzles on the level pages (%s) are never used by the bank.' % (
                        R['max_per_sub_per_quarter'], R['max_per_family_per_quarter'], R['min_gap_days_across_quarters'], MAX_SMALL,
                        R['min_gap_days']['1'], R['family_max_in_window'], R['family_window_days'], R['answer_window_days'], R['answer_small_max_in_window'], R['answer_window_days'],
                        ', '.join(sorted(TAX.FIXED.values()))), '']
    all_by_level = {lv: [] for lv in levels}
    for mm in man['released']:
        for lv, items in banks[mm]['levels'].items():
            for e in items:
                all_by_level[int(lv)].append((mm, e))
    global_fails, more_lines = structure_rules(all_by_level, stock)
    struct_lines += more_lines
    cap_lines, cap_fails = capacity_lines(levels)
    struct_lines += cap_lines
    ret = [(sid, d['retired']) for sid, d in sorted(TAX.SUBS.items()) if d.get('retired')]
    struct_lines += ['', '## Retired sub-structures (the frame is in our own books, so no level may use it)', ''] + ['- `%s`: %s' % kv for kv in ret]
    notyet = sorted(sid for sid, d in TAX.SUBS.items() if d['levels'] and d.get('round') == 3 and not any(e['sub'] == sid for items in all_by_level.values() for _, e in items))
    struct_lines += ['', 'Usable sub-structures of round 3 that no released puzzle uses yet (each has a solver, an independent checker, a sample and a citation; their stories are checked when a month uses them): %d.' % len(notyet)]
    ans_lines, ans_warn = answer_feasibility(all_by_level)
    struct_lines += ans_lines
    sidx = story_index()
    cwidx = cw_index(sidx)
    load_stock_sentences()
    fixed_mini = {k: mini_index('fixed puzzle ' + k, text, sidx) for k, text in fixed.items()}
    print('story index: %d source sentences in %d files' % (len(sidx.txt), len(sidx.rels)))

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
                if e['type'] == 's' and any(w.lower() == e['ans'] for w in e['wrong']):
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
                # 6. story similarity (content words) with our sources
                for sev, detail in story_hits(e['q'], sidx, ans=e['ans'] if e['type'] == 'n' else None, sol=e['hint'] + ' ' + e['why']):
                    if sev == 'FAIL':
                        fails.append('%s: same story as a source: %s' % (tag, detail))
                    else:
                        reviews.append('%s: %s' % (tag, detail))
                for sev, detail in list_hits(e['q'], sidx, ans=e['ans'] if e['type'] == 'n' else None) + frame_hits(e['q'], TAX.T.get('retired_frames', [])):
                    fails.append('%s: %s' % (tag, detail))
                for sev, detail in extra_hits(e['q'], e['ans'] if e['type'] == 'n' else None, e['hint'] + ' ' + e['why'], cwidx):
                    if sev == 'FAIL':
                        fails.append('%s: %s' % (tag, detail))
                    else:
                        reviews.append('%s: %s' % (tag, detail))
                for k, mini in fixed_mini.items():
                    for sev, detail in story_hits(e['q'], mini):
                        if sev == 'FAIL':
                            fails.append('%s: same story as the fixed website puzzle %s: %s' % (tag, k, detail))
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
        lines.append(SRC_LINE)
        lines.append('')
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
    struct_lines.append('Capacity verdict for the full year (a plan for January to October, not a defect of the released months): %d CAPACITY FAIL' % len(cap_fails))
    for f in cap_fails:
        struct_lines.append('- CAPACITY FAIL ' + f)
    for w in ans_warn:
        struct_lines.append('- WARNING ' + w)
    struct_lines.append('')
    struct_lines.append('Skeleton matches with our own sources that were reviewed by hand (same masked wording, but no shared numbers): %d' % len(review_struct))
    for r in review_struct:
        struct_lines.append('- REVIEW ' + r)
    open(os.path.join(HERE, 'batches', 'STRUCTURE_REPORT.md'), 'w', encoding='utf-8').write('\n'.join(struct_lines) + '\n')
    print('structure rules: %d FAIL' % len(global_fails))
    for f in global_fails[:80]:
        print('  FAIL', f)
    fails_all += len(global_fails)
    print('capacity (full-year plan): %d CAPACITY FAIL' % len(cap_fails))
    for f in cap_fails:
        print('  CAPACITY FAIL', f)
    for w in ans_warn:
        print('  WARNING', w)
    if '--strict-capacity' in sys.argv and cap_fails:
        fails_all += len(cap_fails)
    sys.exit(1 if fails_all else 0)


if __name__ == '__main__':
    main()
