#!/usr/bin/env python3
"""Build the ONLINE PRACTICE for one holiday-program lesson, for any level (shared by all levels' agents).

    python3 practice/holiday/build_holiday.py p1 1      # level key p1, lesson 1 -> practice/holiday/p1/01/dist/   (git-ignored, not deployed)
    python3 -m http.server -d practice/holiday/p1/01/dist 8792

Each lesson is a hand-authored, structured item file  practice/holiday/<level key>/<NN>/lesson.py  (the printed workbook is hand-written code, not data,
so the questions are extracted from the workbook source into structured items; see practice/holiday/<level key>/STATUS.md).  A lesson file defines:

    META      dict(level=1, lesson=1, key='p1', title=..., topic=..., strand=..., intro=[...], sources=['hp/workbook_html.js', 'hp/qbank.json', 'hp/gaps.json'])
    ITEMS     list of item dicts (below), in workbook order: core (Start here), invest (Investigation), stretch (Think harder), challenge (Go further)
    VARIANTS  {item id: dict(tpl=..., base={...}, oracle=fn)}   variant families; every combination is run against the independent oracle

An item:  id, tier, no (printed label such as '1(a)', 'T3', 'C2'), type, q, hint, steps (worked solution, list of sentences), skill, src (list of printed
strings that must occur in the workbook source), plus by type
    fields    frame '2, 4, {f1}, 8', answer [6]            check() -> list          boxes inside the sentence, all must be right
    number    answer 29                                      check() -> int
    choice    options [...], answer '...'                    check() -> str           options are never shuffled
    set       answer [..], ordered False                     check() -> list          typed with commas; grouped=True|False says whether '12,500' / '12 500' may be typed with
              thousands separators (default: True when an answer has 5 or more digits). Otherwise a comma or space always separates numbers ('250,450').
    number / fields: unit=False = no unit word is accepted after the number (default: '301 sticks', '20 min', '29.', '20.0' are all accepted)
    text      rule=('add', 3)  or  accept=[...], check()    check() -> ('add', 3) / str   (a counting rule; the accepted wordings come from hlib.rule_accepts)
    selfcheck paper=True|False, facts=<value>, check()      shown only: the child compares with the worked solution; never auto-marked.
              paper=True = drawing / ruler / kit task: shown with 'Do this on paper, then check your drawing against the answer shown on screen.'
              open=True  = no objective fact to check (an explanation); the model answer is a worked example
    svg (question figure) and sol_fig (callable(facts) -> svg of the correct drawing, built from the CHECKED values)

The build stops, and writes nothing, unless: every checker equals the printed answer; every src string occurs in the workbook source; every variant
combination equals its oracle.  The runner is the one shared worksheet runner practice/ext/public/sheet.js (free choice of question, skip, submit,
marking, worked solutions after submit, autosave in the browser; submission to the server only when window.MI_SUBMIT is set).  No timers, scores or streaks.
"""
import importlib.util, json, os, re, shutil, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, 'practice', 'ext'))
import build_ext as B            # noqa: E402  (shared page head, css, variant engine)
import hlib                      # noqa: E402

Fail = B.Fail
TIER_LABEL = {'core': 'Start here', 'invest': 'Investigation', 'stretch': 'Think harder', 'challenge': 'Go further'}
TIER_ORDER = ['core', 'invest', 'stretch', 'challenge']
FALLBACK_HINT = 'Read the question again slowly. Use counters, draw it, or try a small example first.'


def load_lesson(key, n):
    path = os.path.join(HERE, key, f'{n:02d}', 'lesson.py')
    if not os.path.exists(path):
        raise Fail(f'no lesson file {os.path.relpath(path, ROOT)}')
    sys.path.insert(0, os.path.dirname(path))
    spec = importlib.util.spec_from_file_location(f'holiday_{key}_{n:02d}', path)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    sys.path.pop(0)
    return m


# ---------------------------------------------------------------- the workbook source (to prove the items are the printed questions)
def squash(s):
    s = str(s).replace('“', '"').replace('”', '"').replace('’', "'").replace('‘', "'").replace('…', '...').replace('−', '-')
    return re.sub(r'[^a-z0-9]', '', s.lower())


def flatten(o):
    if isinstance(o, dict):
        return ' '.join(flatten(v) for v in o.values())
    if isinstance(o, list):
        return ' '.join(flatten(v) for v in o)
    return str(o)


def corpus(paths):
    parts = []
    for p in paths:
        full = os.path.join(ROOT, p)
        raw = open(full, encoding='utf-8').read()
        parts.append(flatten(json.loads(raw)) if p.endswith('.json') else raw)
    return squash(' '.join(parts))


# ---------------------------------------------------------------- checks of one item against its independent checker
def same(it, got):
    t = it['type']
    ans = it['answer']
    if t == 'fields':
        return [int(x) for x in got] == [int(x) for x in ans]
    if t == 'number':
        return int(got) == int(ans)
    if t == 'choice':
        return got == ans
    if t == 'set':
        g, a = [int(x) for x in got], [int(x) for x in ans]
        return g == a if it.get('ordered') else sorted(g) == sorted(a)
    if t == 'text':
        return tuple(got) == tuple(it['rule']) if it.get('rule') else any(str(got).strip().lower() == str(x).strip().lower() for x in ans)
    raise Fail(f'{it["id"]}: unknown type {t}')


def make_item(src):
    it = dict(src)
    i, t = it['id'], it['type']
    for k in ('tier', 'no', 'q', 'hint', 'steps', 'skill', 'src'):
        if k not in it or it[k] in (None, '', []):
            if k == 'hint':
                it['hint'] = FALLBACK_HINT
            else:
                raise Fail(f'{i}: missing {k}')
    if it['tier'] not in TIER_ORDER:
        raise Fail(f'{i}: bad tier {it["tier"]}')
    out = dict(id=i, tier=it['tier'], type=t, no=it['no'], hint=it['hint'], steps=list(it['steps']), slips=[],
               tags=dict(strand=it.get('strand'), skill=it['skill']), src=it['src'])
    out['q'] = f'{it["no"]}. {it["q"]}'
    if it.get('unit') is False:                   # a number item whose answer must be typed with no unit word
        out['unit'] = False
    if it.get('svg'):
        out['svg'] = hlib.lift_svg(it['svg'])      # figure text at least 12 px on a 360 px phone (shared rule, also for figures a lesson draws itself)
    if t == 'selfcheck':
        out['paper'] = bool(it.get('paper'))
        out['paper_only'] = out['paper']
        out['marking_mode'] = 'self'
        facts = it.get('facts')
        chk = it.get('check')
        if chk is not None:
            got = chk()
            if facts is not None and got != facts:
                raise Fail(f'{i}: independent check {got} differs from the stated facts {facts}')
            facts = got
        elif not it.get('open'):
            raise Fail(f'{i}: a self-check item needs check() or open=True')
        out['open'] = bool(it.get('open'))
        if it.get('sol_fig'):
            out['sol_svg'] = hlib.lift_svg(it['sol_fig'](facts))
        return out, facts
    out['marking_mode'] = 'auto'
    if t == 'text':
        if it.get('rule'):
            out['answer'] = hlib.rule_accepts(*it['rule'])
            out['shown'] = ' '.join([it['rule'][0], str(it['rule'][1])])
        else:
            out['answer'] = list(it['accept']); out['shown'] = it.get('shown') or it['accept'][0]
        it = dict(it, answer=out['answer'])
    if 'check' not in it or it['check'] is None:
        raise Fail(f'{i}: no independent checker')
    got = it['check']()
    if t == 'fields':
        nbox = len(re.findall(r'\{f\d+\}', it['frame']))
        if len(it['answer']) != nbox:
            raise Fail(f'{i}: {nbox} boxes but {len(it["answer"])} answers')
        if not same(it, got):
            raise Fail(f'{i}: independent check {got} differs from the printed answer {it["answer"]}')
        out['frame'] = it['frame']
        out['fields'] = [dict(id=f'f{n + 1}', answer=int(a)) for n, a in enumerate(it['answer'])]
        for f in out['fields']:           # a box printed after a clock hour ('6:{f1}'): the child may also type '6:20'
            pm = re.search(r'(\d{1,2}:)\{' + f['id'] + r'\}', it['frame'])
            if pm:
                f['pre'] = pm.group(1)
        out['answer'] = [int(a) for a in it['answer']]
    elif t == 'number':
        if not same(it, got):
            raise Fail(f'{i}: independent check {got} differs from the printed answer {it["answer"]}')
        out['answer'] = int(it['answer'])
    elif t == 'choice':
        if it['answer'] not in it['options']:
            raise Fail(f'{i}: answer not among the options')
        if not same(it, got):
            raise Fail(f'{i}: independent check {got} differs from the printed answer {it["answer"]}')
        out.update(options=list(it['options']), fixed=True, answer=it['answer'])
    elif t == 'set':
        if not same(it, got):
            raise Fail(f'{i}: independent check {got} differs from the printed answer {it["answer"]}')
        out.update(answer=[int(a) for a in it['answer']], ordered=bool(it.get('ordered')))
        if it.get('grouped') is not None:         # default (sheet.js and mark.js): numbers of 5 or more digits expected => '12,500' / '12 500' may be typed with separators
            out['grouped'] = bool(it['grouped'])
    elif t == 'text':
        if not same(it, got):
            raise Fail(f'{i}: independent check {got} differs from the printed answer')
    else:
        raise Fail(f'{i}: unknown type {t}')
    if it.get('sol_fig'):
        out['sol_svg'] = hlib.lift_svg(it['sol_fig'](got))
    return out, None


def mirror_report(srcitems, items, cp):
    """Every src string must occur in the workbook source; also reports whether the question text on screen is the printed text (exact) or reworded."""
    exact = reword = 0
    for s, o in zip(srcitems, items):
        for frag in s['src']:
            if squash(frag) not in cp:
                raise Fail(f'{s["id"]}: printed text not found in the workbook source: {frag!r}')
        shown = squash(o['q'] + ' ' + re.sub(r'\{f\d+\}', '', o.get('frame', '')))
        if all(squash(frag) in shown for frag in s['src']):
            exact += 1; o['mirror'] = 'exact'
        else:
            reword += 1; o['mirror'] = 'reworded'
    return exact, reword


def build(key, n):
    m = load_lesson(key, n)
    meta = m.META
    srcitems = m.ITEMS
    ids = [s['id'] for s in srcitems]
    if len(set(ids)) != len(ids):
        raise Fail('duplicate item ids')
    order = [TIER_ORDER.index(s['tier']) for s in srcitems]
    if order != sorted(order):
        raise Fail('items must be in workbook order: core, invest, stretch, challenge')
    items, facts = [], {}
    for s in srcitems:
        o, f = make_item(s)
        items.append(o); facts[o['id']] = f
    cp = corpus(meta['sources'])
    exact, reword = mirror_report(srcitems, items, cp)
    report = B.attach_variants(items, getattr(m, 'VARIANTS', {}))
    lk = f'{key}l{n:02d}'
    data = dict(runner=2, title=meta['title'], level=meta['level'], lesson=n, unit_label=f'Holiday lesson {n}', topic=meta['topic'],
                source=meta['sources'], items=items)
    dist = os.path.join(HERE, key, f'{n:02d}', 'dist')
    shutil.rmtree(dist, ignore_errors=True)
    os.makedirs(os.path.join(dist, 'data'))
    json.dump(data, open(os.path.join(dist, 'data', lk + '.json'), 'w', encoding='utf-8'), ensure_ascii=False)
    shutil.copy(os.path.join(ROOT, 'practice', 'ext', 'public', 'sheet.js'), os.path.join(dist, 'sheet.js'))
    page = open(os.path.join(ROOT, 'term', 'l1', 'runner', 'index.html'), encoding='utf-8').read()
    css = B.SHEET_CSS + ('details.learn{background:var(--card);border:2px solid var(--line);border-radius:16px;padding:.6rem 1rem;margin:0 0 1rem}'
                         'details.learn summary{font-weight:800;cursor:pointer;min-height:44px;display:flex;align-items:center}details.learn p{margin:.3rem 0}'
                         '.card .q{white-space:pre-line}.card svg,.fb svg{max-width:100%;height:auto}.fig{background:#fff;border-radius:12px;padding:4px}@media(max-width:480px){.card{padding:1rem .75rem 1.2rem}}')
    head = page[:page.index('</style>')] + css + '</style></head>'
    head = head.replace('<meta charset="utf-8">', '<meta charset="utf-8"><meta name="robots" content="noindex,nofollow">', 1)
    head = head.replace('<title>Practice | Math Inquirers</title>', f'<title>Practice: {B.html.escape(meta["title"])} | Math Inquirers</title>')
    e = B.html.escape
    learn = (f'<details class="learn"><summary>About this page</summary><p>These are the questions of Lesson {n} in your printed holiday workbook '
             f'({e(meta["workbook_title"])}). You can do them here instead of writing on the page.</p>' +
             ''.join(f'<p>{e(x)}</p>' for x in meta.get('intro', [])) + '</details>')
    # sending to the tutor is OFF unless the builder is run with MI_SUBMIT_ENDPOINT=<url>; then sheet.js shows the 'I checked / I got it / not yet' ticks and the footer says the answers are sent
    ep = os.environ.get('MI_SUBMIT_ENDPOINT', '').strip()
    submit_cfg = f'window.MI_SUBMIT={json.dumps({"endpoint": ep, "unit": "hol-" + lk})};' if ep else ''
    body = ('<body><main><h1 id="title">Practice</h1><p class="sub" id="sub"></p>' + learn +
            '<p class="sub" id="count" aria-live="polite"></p><nav class="nav" id="nav" aria-label="Choose a question"></nav>'
            '<section class="card" id="card"></section><div id="bar" class="barwrap"></div>'
            '<p class="foot">There is no score and no timer. Open any question in any order, skip what you like, then submit. '
            '<span id="footpriv">Your answers stay on this device.</span> A grown-up can read along.</p></main>'
            f'<script>window.MI_LESSON={json.dumps(lk)};{submit_cfg}</script><script src="sheet.js"></script></body></html>')
    open(os.path.join(dist, 'index.html'), 'w', encoding='utf-8').write(head + body)
    fonts = os.path.join(ROOT, 'website', 'dist')
    if os.path.isdir(os.path.join(fonts, 'fonts')):
        shutil.copytree(os.path.join(fonts, 'fonts'), os.path.join(dist, 'fonts'))
        fc = open(os.path.join(fonts, 'fonts.css'), encoding='utf-8').read().replace("url('/fonts/", "url('fonts/")
        open(os.path.join(dist, 'fonts.css'), 'w', encoding='utf-8').write(fc)
    kinds = {}
    for i in items:
        kinds[i['type']] = kinds.get(i['type'], 0) + 1
    auto = sum(1 for i in items if i['marking_mode'] == 'auto')
    paper = sum(1 for i in items if i.get('paper'))
    print(f'{lk}: {len(items)} items {kinds}; {auto} auto-marked, {len(items) - auto - paper} self-check, {paper} paper-only; '
          f'{sum(1 for i in items if i.get("open"))} open (no objective fact to check); mirror: {exact} as printed, {reword} reworded')
    print(f'  every checker equals the printed answer; every src string is in the workbook source; {len(report)} variant families '
          f'({sum(c for _, c in report)} combinations all equal their oracle)')
    print('written', os.path.relpath(dist, ROOT))
    return lk


if __name__ == '__main__':
    try:
        build(sys.argv[1] if len(sys.argv) > 1 else 'p1', int(sys.argv[2]) if len(sys.argv) > 2 else 1)
    except Fail as ex:
        print('BUILD FAILED:', ex)
        sys.exit(1)
