#!/usr/bin/env python3
"""Build the online practice page for one extension unit from extension/data (the same file the workbook is built from).

    python3 practice/ext/build_ext.py 2 1        # Level 2, unit 1 -> practice/ext/dist/l2u01/   (not deployed)
    python3 -m http.server -d practice/ext/dist/l2u01 8791

What it does, in this order (any failure stops the build and nothing is written):
 1. runs the unit's independent answer checks (extension/verify/lN_uXX_checks.py) and requires them to equal the answers in the JSON
    (the same gate as extension/verify/run_checks.py), and takes every online answer from the CHECKED value;
 2. turns each item / part into a runner item (type fields, set, choice or selfcheck) with its figure drawn by extension/tools/figs.py;
 3. attaches the variant families of the sidecar practice/ext/variants/lN_uXX.py, and runs each family's independent oracle over EVERY
    combination of its variables (and at the authored numbers) before anything is written;
 4. copies the Term 1 runner (term/l1/runner) with five small, asserted patches (see patch_runner) and writes data + page.
No timers, scores or streaks: that is the runner's rule and this build adds nothing to it.
"""
import html, importlib.util, itertools, json, os, re, shutil, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
EXT = os.path.join(ROOT, 'extension')
sys.path.insert(0, os.path.join(EXT, 'tools'))
import figs                                   # noqa: E402  extension figure specs -> SVG

TIER_MAP = {'start': 'core', 'think': 'stretch', 'go': 'challenge', 'quiz': 'check'}
TIER_LABEL = {'core': 'Start here', 'stretch': 'Think harder', 'challenge': 'Go further', 'check': 'Check yourself'}
BLANK = re.compile(r'\{(?:b|bw|l|ll)\}')
CIRC = re.compile(r'\{circ:([^}]*)\}')
FALLBACK_HINT = 'Read the question again slowly. The "Before you start" box at the top may help. Try a small example first.'


class Fail(Exception):
    pass


def load_mod(path, name):
    sys.path.insert(0, os.path.dirname(path))        # the checks import verify/common.py (their own 'common')
    sys.modules.pop('common', None)
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    sys.path.pop(0)
    return m


# ---------------------------------------------------------------- step 1: independent checks
NORM = load_mod(os.path.join(EXT, 'verify', 'common.py'), 'ext_verify_common').norm
norm = NORM


def checked_answers(unit, checks):
    """{key: value list} for every item / part, key = item id or item id-label. Fails unless the independent check equals the JSON."""
    out = {}
    for it in [dict(unit['learn']['try'], tier='start')] + unit['items']:
        i = it['id']
        if i not in checks:
            raise Fail(f'{i}: no independent check function')
        got = checks[i]()
        holders = [(f'{i}-{p["label"]}', p, got[p['label']] if isinstance(got, dict) else None) for p in it['parts']] if it.get('parts') else [(i, it, got)]
        for key, h, g in holders:
            if g is None:
                raise Fail(f'{key}: check returned no value')
            book = h['answer']['value']
            same = (sorted(norm(g)) == sorted(norm(book))) if h['answer'].get('unordered') else norm(g) == norm(book)
            if not same:
                raise Fail(f'{key}: independent check {g} differs from the book {book}')
            out[key] = [str(x) for x in g]
    return out


# ---------------------------------------------------------------- step 2: items
def tidy(t):
    return re.sub(r'\s+', ' ', t.replace('\n', ' ')).strip()


def split_steps(expl, label=None, labels=()):
    """The worked solution as a list of short steps; for one part of several, only that part's segment."""
    seg = expl
    if label and len(labels) > 1:
        m = list(re.finditer(r'\(([a-z])\)\s', expl))
        if [x.group(1) for x in m] == list(labels):
            i = labels.index(label)
            seg = expl[m[i].end(): m[i + 1].start() if i + 1 < len(m) else None].strip()
    parts = re.split(r'(?<=[.?!])\s+(?=[A-Z(0-9"])', seg)
    return [p.strip() for p in parts if p.strip()]


def svg_of(fig):
    if not fig:
        return None
    s = figs.render(fig, 'colour')
    s = re.sub(r'width:(\d+)mm', r'width:100%;max-width:\1mm', s, count=1)
    return s


def int_values(vals, key):
    try:
        return [int(v) for v in vals]
    except ValueError:
        raise Fail(f'{key}: answer {vals} is not whole numbers (needs a sidecar rule)')


def make_items(unit, answers, ov, policy):
    items = []
    counts = {k: 0 for k in TIER_MAP}

    def add(src, h, label, labels, tier, number):
        key = f'{src["id"]}-{label}' if label else src['id']
        vals = answers[key]
        text = h['text'] if src.get('parts') else src['text']
        stem = tidy(BLANK.sub('', CIRC.sub('', src['text']))) if src.get('parts') else ''
        pre = f'{number}{"(" + label + ")" if label else ""}. ' if number else ''
        it = dict(id=key, tier=TIER_MAP[tier], src=src['id'], part=label or None,
                  hint=src.get('hint') or FALLBACK_HINT, slips=[])
        if src.get('figure'):
            it['svg'] = svg_of(src['figure'])
        steps = split_steps(src['explanation'], label, labels)
        circ = CIRC.search(h['text'])
        nblank = len(BLANK.findall(h['text']))
        if vals == ['open']:
            it.update(type='selfcheck', q=pre + tidy(CIRC.sub('', BLANK.sub('', h['text']))), button='Show me how to check it',
                      steps=[h['answer']['text']] + steps)
        elif circ:
            opts = circ.group(1).split('|')
            if vals[0] not in opts or len(vals) != 1:
                raise Fail(f'{key}: answer {vals} is not one of {opts}')
            q_text = tidy(CIRC.sub('...', h['text']))
            it.update(type='choice', options=opts, fixed=True, answer=vals[0],
                      q=pre + ((stem + ' ' if stem else '') + q_text), steps=steps)
        elif h['answer'].get('list'):
            pol = policy.get(key)
            if pol not in ('any', 'ordered'):
                raise Fail(f'{key}: list answer needs LIST_POLICY "any" or "ordered" in the variants sidecar')
            q = tidy(BLANK.sub('', h['text'])) if not src.get('parts') else (stem + ' ' + tidy(BLANK.sub('', h['text']))).strip()
            it.update(type='set', answer=int_values(vals, key), ordered=(pol == 'ordered'), q=pre + q, steps=steps)
        else:
            if nblank + (0 if src.get('parts') else 0) != len(vals):
                raise Fail(f'{key}: {nblank} blanks but {len(vals)} answers')
            fields = [dict(id=f'f{n + 1}', answer=a) for n, a in enumerate(int_values(vals, key))]
            raw = tidy(h['text'])
            if nblank == 1 and re.search(r'\{(?:b|bw)\}$', h['text'].rstrip()) and not src.get('parts'):
                q, frame = tidy(BLANK.sub('', h['text'])), '{f1}'
            else:
                n = iter(range(1, nblank + 1))
                frame = tidy(BLANK.sub(lambda m: '{f%d}' % next(n), h['text']))
                q = stem if src.get('parts') else 'Fill in the boxes.'
            it.update(type='fields', q=pre + q, frame=frame, fields=fields, steps=steps)
            it['answer'] = [f['answer'] for f in fields]
        if key in ov:
            it['q'] = pre + ov[key]
        items.append(it)

    # "Your turn" first, then the four sets
    tr = unit['learn']['try']
    order = [(dict(tr, tier='start'), 'start', 'Your turn')]
    for tier in ('start', 'think', 'go', 'quiz'):
        for n, src in enumerate([x for x in unit['items'] if x['tier'] == tier], 1):
            order.append((src, tier, n))
    for src, tier, n in order:
        labels = [p['label'] for p in src.get('parts', [])]
        number = '' if n == 'Your turn' else n
        if src.get('parts'):
            for p in src['parts']:
                add(src, p, p['label'], labels, tier, number)
        else:
            add(src, src, None, labels, tier, number)
        if n == 'Your turn':
            items[-1]['q'] = 'Your turn. ' + items[-1]['q']
    return items


# ---------------------------------------------------------------- step 3: variants and their oracles
def ev(expr, env):
    s = expr
    for k in sorted(env, key=len, reverse=True):
        s = re.sub(r'\b%s\b' % re.escape(k), str(env[k]), s)
    if not re.fullmatch(r'[\d\s+\-*/%().]*', s):
        raise Fail(f'bad expression {expr}')
    return eval(s)


def attach_variants(items, variants):
    by = {i['id']: i for i in items}
    report = []
    for key, v in variants.items():
        if key not in by:
            raise Fail(f'variant for unknown item {key}')
        it, tp = by[key], v['tpl']
        names = list(tp['vars'])
        n = 0
        for combo in itertools.product(*[tp['vars'][k] for k in names]):
            env = dict(zip(names, combo))
            full = dict(env)
            for k, e in tp.get('derive', {}).items():
                full[k] = ev(e, full)
            got = {k: ev(e, full) for k, e in tp['answers'].items()} if 'answers' in tp else ev(tp['answer'], full)
            want = v['oracle'](env)
            if got != want:
                raise Fail(f'{key}: template gives {got} but the oracle gives {want} at {env}')
            n += 1
        full = dict(v['base'])
        for k, e in tp.get('derive', {}).items():
            full[k] = ev(e, full)
        got = [ev(e, full) for e in tp['answers'].values()] if 'answers' in tp else ev(tp['answer'], full)
        auth = it['answer']
        if got != (auth if isinstance(auth, list) else auth) and not (isinstance(got, (int, float)) and [got] == auth):
            raise Fail(f'{key}: the template at the authored numbers gives {got}, the checked book answer is {auth}')
        it['tpl'] = tp
        report.append((key, n))
    return report


# ---------------------------------------------------------------- step 4: runner copy and page
def patch_runner(js):
    """Five asserted patches to the copy of term/l1/runner/practice.js; the original file is not touched."""
    def sub(old, new):
        nonlocal js
        if js.count(old) != 1:
            raise Fail('runner changed, patch no longer applies: ' + old[:50])
        js = js.replace(old, new)
    sub("var TIER = { core: 'Start here', stretch: 'Think harder', challenge: 'Go further' };",
        "var TIER = { core: 'Start here', stretch: 'Think harder', challenge: 'Go further', check: 'Check yourself' };")
    sub("['core', 'stretch', 'challenge'].forEach(function (k) { t.appendChild(", "Object.keys(TIER).forEach(function (k) { t.appendChild(")
    sub("' · Lesson ' + L.lesson + ' · ' + L.topic;", "' · ' + (L.unit_label || 'Lesson ' + L.lesson) + ' · ' + L.topic;")
    sub("function shuffled(item) {\n", "function shuffled(item) {\n    if (item.fixed) return item.options;\n")
    # a True/False (or any two-choice) item has only one wrong answer, so "that is the same answer as before" would trap the child
    sub("if (s.tries === 1 && s.last === sig) {", "if (s.tries === 1 && s.last === sig && !(item.type === 'choice' && item.options.length < 3)) {")
    return js


def learn_block(unit):
    ln = unit['learn']; ex = ln['example']; e = html.escape
    parts = [f'<details class="learn" open><summary>Before you start: {e(unit["title"])}</summary>', f'<p>{e(ln["intro"])}</p>']
    parts.append(f'<h2>Worked example</h2><p>{e(ex["problem"])}</p>')
    if ex.get('figure'):
        parts.append(f'<div class="lf">{svg_of(ex["figure"])}</div>')
    parts.append('<ol>' + ''.join(f'<li>{e(s)}</li>' for s in ex['steps']) + '</ol>')
    parts.append(f'<p><b>Answer:</b> {e(ex["answer"])}</p>')
    if ln.get('howto'):
        parts.append(f'<h2>{e(ln["howto"]["title"])}</h2><ol>' + ''.join(f'<li>{e(s)}</li>' for s in ln['howto']['steps']) + '</ol>')
    if ln.get('facts'):
        parts.append(f'<h2>{e(ln["facts"]["title"])}</h2><ul>' + ''.join(f'<li>{e(s)}</li>' for s in ln['facts']['lines']) + '</ul>')
    parts.append('</details>')
    css = ('<style>details.learn{background:var(--card);border:2px solid var(--line);border-radius:16px;padding:.6rem 1rem;margin:0 0 1rem}'
           'details.learn summary{font-weight:800;cursor:pointer;min-height:44px;display:flex;align-items:center}'
           'details.learn h2{font:600 17px Fredoka,Arial;margin:.8rem 0 .2rem}details.learn p{margin:.3rem 0}'
           'details.learn .lf svg{max-width:100%;height:auto}.card svg{max-width:100%;height:auto}</style>')
    return css + ''.join(parts)


def build(level, u):
    base = f'l{level}_u{u:02d}'
    unit = json.load(open(os.path.join(EXT, 'data', base + '.json'), encoding='utf-8'))
    cpath = os.path.join(EXT, 'verify', base + '_checks.py')
    checks = load_mod(cpath, base + '_checks').CHECKS
    answers = checked_answers(unit, checks)
    side = load_mod(os.path.join(HERE, 'variants', base + '.py'), base + '_variants')
    ov = side.q_override(checks)
    items = make_items(unit, answers, ov, side.LIST_POLICY)
    for k in ov:
        if k not in {i['id'] for i in items}:
            raise Fail(f'q_override for unknown item {k}')
    report = attach_variants(items, side.VARIANTS)
    key = f'l{level}u{u:02d}'
    data = dict(runner=2, title=unit['title'], level=level, lesson=u, unit_label=f'Extension unit {u}', topic=unit['topic'], source=base + '.json', items=items)
    dist = os.path.join(HERE, 'dist', key)
    shutil.rmtree(dist, ignore_errors=True)
    os.makedirs(os.path.join(dist, 'data'))
    json.dump(data, open(os.path.join(dist, 'data', key + '.json'), 'w', encoding='utf-8'), ensure_ascii=False)
    js = patch_runner(open(os.path.join(ROOT, 'term', 'l1', 'runner', 'practice.js'), encoding='utf-8').read())
    open(os.path.join(dist, 'practice.js'), 'w', encoding='utf-8').write(js)
    page = open(os.path.join(ROOT, 'term', 'l1', 'runner', 'index.html'), encoding='utf-8').read()
    page = page.replace('<script src="practice.js">', f'<script>window.MI_LESSON={json.dumps(key)};</script><script src="practice.js">')
    page = page.replace('<div class="tiers"', learn_block(unit) + '<div class="tiers"', 1)
    page = page.replace('<title>Practice | Math Inquirers</title>', f'<title>Practice: {html.escape(unit["title"])} | Math Inquirers</title>')
    if 'Before you start' not in page:
        raise Fail('page template changed')
    open(os.path.join(dist, 'index.html'), 'w', encoding='utf-8').write(page)
    fonts = os.path.join(ROOT, 'website', 'dist')
    if os.path.isdir(os.path.join(fonts, 'fonts')):
        shutil.copytree(os.path.join(fonts, 'fonts'), os.path.join(dist, 'fonts'))
        css = open(os.path.join(fonts, 'fonts.css'), encoding='utf-8').read().replace("url('/fonts/", "url('fonts/")
        open(os.path.join(dist, 'fonts.css'), 'w', encoding='utf-8').write(css)
    kinds = {}
    for i in items:
        kinds[i['type']] = kinds.get(i['type'], 0) + 1
    print(f'{base}: {len(answers)} answers equal their independent checks; {len(items)} online items {kinds};',
          f'{len(report)} variant families ({sum(n for _, n in report)} combinations all equal their oracle)')
    print('written', os.path.relpath(dist, ROOT))
    return key


if __name__ == '__main__':
    try:
        build(int(sys.argv[1]) if len(sys.argv) > 1 else 2, int(sys.argv[2]) if len(sys.argv) > 2 else 1)
    except Fail as e:
        print('BUILD FAILED:', e)
        sys.exit(1)
