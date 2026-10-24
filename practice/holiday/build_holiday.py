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
              marking_mode='self' | 'open'  how the TUTOR REPORT counts it (make_keys.py reads it): 'self' = the child compares with a model answer (every paper-only drawing, every
              'Explain / why / how do you know' item); 'open' = truly open, no objective fact (make up your own, many answers are right). Paper-only is always 'self'.
              Default when the lesson file does not say: 'self', except an open=True item that is plainly make-up-your-own ('make up', 'your own', 'invent', 'design', or a model
              answer that starts 'Open' / 'Answers vary'), which is 'open'.
    label     optional (any item): the short label on the question button (up to about 8 characters, such as '2(b) P'). Default: derived from `no` by sheet.js
              ('Investigation 2' -> 'Inv 2', 'Think harder 3 (why)' -> 'T3', 'Go further 6' -> 'G6', '3(d)' twice -> '3(d)-a', '3(d)-b'). Set it only for an unusual `no`.
    text answers: three optional flags, all off unless stated
              poly='n' | False   the typed rule is compared with the accepted writings as a POLYNOMIAL in n ('=' chains allowed: '(n+3)x4 = 4n+12', 'OUT = 4(n+3)'; (2n+6)/2 equals n+3).
                                 DEFAULT: on automatically when EVERY accepted writing is an expression in n and they are all the same polynomial (so every algebra-rule item is on); poly=False turns it off.
              accept_prefix=False | ['so it is']  (default: on) 'It is 12' / 'It will be Wednesday.' / 'The answer is 12' are read as the answer after the lead-in; False turns it off, a list adds lead-ins.
                                 The shared matcher also reads 'a is equal to b' as 'a = b', 'A and B and D' as 'A, B, D' (single letters, numbers or fractions only) and, with equiv_frac, '1 out of 4' as 1/4.
              equiv_frac=True | False  every fraction in a typed list may be written in any equal form, in the same order ('7/12, 8/12, 10/12' for '7/12, 2/3, 5/6').
                                 DEFAULT: on when the hint says "same bottom number" / "same denominator" and the accepted writings are fractions; otherwise off (only the printed forms).
    number / fields: words=True  number words ('five', 'twenty-five', 'minus five') are also accepted. DEFAULT off: words are wrong unless an item declares it.
    svg (question figure) and sol_fig (callable(facts) -> svg of the correct drawing, built from the CHECKED values)

The build stops, and writes nothing, unless: every checker equals the printed answer; every src string occurs in the workbook source; every variant
combination equals its oracle.  The runner is the one shared worksheet runner practice/ext/public/sheet.js (free choice of question, skip, submit,
marking, worked solutions after submit, autosave in the browser; submission to the server only when window.MI_SUBMIT is set).  No timers, scores or streaks.
"""
import importlib.util, itertools, json, os, re, shutil, sys

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


# ---------------------------------------------------------------- footer wording: THE ONE PLACE (go-live switch)
# Sending answers to the tutor is OFF unless the builder is run with MI_SUBMIT_ENDPOINT=<url> (SUBMIT-TO-TUTOR go-live).  The two privacy sentences below are written into every page
# (window.MI_FOOT) and sheet.js shows the one that is true: FOOT_OFF while nothing is sent, FOOT_ON when the child is signed in and the endpoint is set (then the 'I checked / I got it /
# Not yet' ticks show too).  THE WORDING NEEDS THE OWNER'S (AND A LAWYER'S) SIGN-OFF BEFORE GO-LIVE: see practice/holiday/README.md.
FOOT_OFF = 'Your answers stay on this device.'
FOOT_ON = 'Your answers, and what you write in the explanation boxes, are sent to your tutor so they can help you.'


MAKEUP = re.compile(r'make up|make your own|invent|design your|create your|your own (riddle|pattern|number|puzzle|question|problem|rule|example|sentence|story)', re.I)


def self_mode(it):
    """How a self-check item is counted in the tutor report: 'self' (compare with a model answer) or 'none' (truly open). See the module docstring."""
    mm = it.get('marking_mode')
    if mm is not None:
        if mm not in ('self', 'open', 'none'):
            raise Fail(f'{it["id"]}: marking_mode must be "self" or "open"')
        mm = 'none' if mm in ('open', 'none') else 'self'
    elif it.get('check') is not None or it.get('facts') is not None:
        mm = 'self'                                 # there is an objective fact (a checked model answer): the child compares with it
    elif it.get('open'):
        first = (it.get('steps') or [''])[0].lstrip().lower()
        mm = 'none' if MAKEUP.search(it.get('q', '')) or first.startswith(('open', 'answers vary')) else 'self'
    else:
        mm = 'self'
    return 'self' if it.get('paper') else mm      # a paper-only drawing is always compared with the shown answer


def text_flags(i, it, out):
    """poly / equiv_frac for a text item (defaults in the module docstring); every accepted writing is checked with the build-time parsers in hlib."""
    acc = out['answer']
    poly = it.get('poly')
    if poly is None:
        poly = hlib.auto_poly(acc)
    elif poly:
        poly = poly if isinstance(poly, str) and len(poly) == 1 else 'n'
        if hlib.auto_poly(acc, poly) != poly:
            raise Fail(f'{i}: poly={poly!r} but the accepted writings are not all the same polynomial in {poly}: {acc}')
    if poly:
        out['poly'] = poly
    ap = it.get('accept_prefix')      # lead-ins such as 'It is' / 'It will be' / 'The answer is' are ignored in a text answer; accept_prefix=False turns that off, a list adds more lead-ins
    if ap is False or (isinstance(ap, (list, tuple)) and ap and all(isinstance(x, str) and x.strip() for x in ap)):
        out['accept_prefix'] = ap if ap is False else [str(x) for x in ap]
    elif ap not in (None, True):
        raise Fail(f'{i}: accept_prefix must be False or a list of lead-in strings')
    eq = it.get('equiv_frac')
    parsable = all(hlib.frac_tokens(a)[0] and all(d > 0 for _, d in hlib.frac_tokens(a)[0]) for a in acc)
    if eq is None:
        eq = bool(re.search(r'same (bottom number|denominator)', it.get('hint', ''), re.I)) and parsable and not poly
    if eq:
        if not parsable:
            raise Fail(f'{i}: equiv_frac=True but not every accepted writing is a list of fractions: {acc}')
        out['equiv_frac'] = True


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
    if it.get('words'):                           # number words ('five') accepted only when the item declares it (no default)
        if t not in ('number', 'fields'):
            raise Fail(f'{i}: words=True is only for number and fields items')
        out['words'] = True
    if it.get('label'):
        if not isinstance(it['label'], str) or len(it['label']) > 12:
            raise Fail(f'{i}: label must be a short string (at most 12 characters)')
        out['label'] = it['label']
    if it.get('svg'):
        out['svg'] = hlib.lift_svg(it['svg'])      # figure text at least 12 px on a 360 px phone (shared rule, also for figures a lesson draws itself)
    if t == 'selfcheck':
        out['paper'] = bool(it.get('paper'))
        out['paper_only'] = out['paper']
        out['marking_mode'] = self_mode(it)
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
            out['sol_svg'] = hlib.lift_svg(it['sol_fig'](facts), solution=True)
        return out, facts
    out['marking_mode'] = 'auto'
    if t == 'text':
        if it.get('rule'):
            out['answer'] = hlib.rule_accepts(*it['rule'])
            out['shown'] = ' '.join([it['rule'][0], str(it['rule'][1])])
        else:
            out['answer'] = list(it['accept']); out['shown'] = it.get('shown') or it['accept'][0]
        it = dict(it, answer=out['answer'])
        text_flags(i, it, out)
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
        out['sol_svg'] = hlib.lift_svg(it['sol_fig'](got), solution=True)
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


def attach_variant_figs(items, variants):
    """A variant family may bring its own figure so the picture under 'Try a similar one' matches the new numbers.  In the lesson file either
         VARIANTS[id]['tpl']['fig'] = '<svg ...>{n} ...</svg>'   an SVG template with the same {name} places as the question (variables and derived values), or
         VARIANTS[id]['fig'] = function(env) -> svg text          drawn for every combination here at build time (at most 600 combinations; stored as tpl['figs']).
       Without either, sheet.js hides the first question's picture while the variant is shown; VARIANTS[id]['tpl']['paper'] = True adds 'Draw it on paper if it helps.'"""
    by = {i['id']: i for i in items}
    for k, v in variants.items():
        it, tp = by[k], dict(by[k]['tpl'])
        if v.get('fig') is not None:
            f = v['fig']
            if isinstance(f, str):
                tp['fig'] = f
            else:
                names = list(tp['vars'])
                combos = list(itertools.product(*[tp['vars'][x] for x in names]))
                if len(combos) > 600:
                    raise Fail(f'{k}: fig() would be stored for {len(combos)} combinations (at most 600): give tpl["fig"] as an SVG template instead')
                tp['figs'] = {'|'.join(str(c) for c in combo): hlib.lift_svg(f(dict(zip(names, combo)))) for combo in combos}
        if tp.get('fig'):
            tp['fig'] = hlib.lift_svg(tp['fig'])
        it['tpl'] = tp


def build(key, n, dist=None, endpoint=None):
    """dist / endpoint are for tests; normally dist = <lesson>/dist and the endpoint is the MI_SUBMIT_ENDPOINT environment variable."""
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
    attach_variant_figs(items, getattr(m, 'VARIANTS', {}))
    lk = f'{key}l{n:02d}'
    data = dict(runner=2, title=meta['title'], level=meta['level'], lesson=n, unit_label=f'Holiday lesson {n}', topic=meta['topic'],
                source=meta['sources'], items=items)
    dist = dist or os.path.join(HERE, key, f'{n:02d}', 'dist')
    shutil.rmtree(dist, ignore_errors=True)
    os.makedirs(os.path.join(dist, 'data'))
    json.dump(data, open(os.path.join(dist, 'data', lk + '.json'), 'w', encoding='utf-8'), ensure_ascii=False)
    shutil.copy(os.path.join(ROOT, 'practice', 'ext', 'public', 'sheet.js'), os.path.join(dist, 'sheet.js'))
    page = open(os.path.join(ROOT, 'term', 'l1', 'runner', 'index.html'), encoding='utf-8').read()
    css = B.SHEET_CSS + ('details.learn{background:var(--card);border:2px solid var(--line);border-radius:16px;padding:.6rem 1rem;margin:0 0 1rem}'
                         'details.learn summary{font-weight:800;cursor:pointer;min-height:44px;display:flex;align-items:center}details.learn p{margin:.3rem 0}'
                         '.card .q{white-space:pre-line}.card svg,.fb svg{max-width:100%;height:auto;overflow:visible}.fig{background:#fff;border-radius:12px;padding:4px}@media(max-width:480px){.card{padding:1rem .75rem 1.2rem}}')
    head = page[:page.index('</style>')] + css + '</style></head>'
    head = head.replace('<meta charset="utf-8">', '<meta charset="utf-8"><meta name="robots" content="noindex,nofollow">', 1)
    head = head.replace('<title>Practice | Math Inquirers</title>', f'<title>Practice: {B.html.escape(meta["title"])} | Math Inquirers</title>')
    e = B.html.escape
    learn = (f'<details class="learn"><summary>About this page</summary><p>These are the questions of Lesson {n} in your printed holiday workbook '
             f'({e(meta["workbook_title"])}). You can do them here instead of writing on the page.</p>' +
             ''.join(f'<p>{e(x)}</p>' for x in meta.get('intro', [])) + '</details>')
    # sending to the tutor is OFF unless the builder is run with MI_SUBMIT_ENDPOINT=<url>; then sheet.js shows the 'I checked / I got it / not yet' ticks and the footer says the answers are sent
    ep = (os.environ.get('MI_SUBMIT_ENDPOINT', '') if endpoint is None else endpoint).strip()
    submit_cfg = f'window.MI_SUBMIT={json.dumps({"endpoint": ep, "unit": "hol-" + lk})};' if ep else ''
    body = ('<body><main><h1 id="title">Practice</h1><p class="sub" id="sub"></p>' + learn +
            '<p class="sub" id="count" aria-live="polite"></p><nav class="nav" id="nav" aria-label="Choose a question"></nav>'
            '<section class="card" id="card"></section><div id="bar" class="barwrap"></div>'
            '<p class="foot">There is no score and no timer. Open any question in any order, skip what you like, then submit. '
            f'<span id="footpriv">{B.html.escape(FOOT_OFF)}</span> A grown-up can read along.</p></main>'
            f'<script>window.MI_LESSON={json.dumps(lk)};window.MI_FOOT={json.dumps({"off": FOOT_OFF, "on": FOOT_ON})};{submit_cfg}</script><script src="sheet.js"></script></body></html>')
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
