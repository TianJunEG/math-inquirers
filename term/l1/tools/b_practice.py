"""Online practice: writes out/lNN/practice/ (runner + data) in the format of practice/public (see practice/README.md)."""
import json, os, re, shutil, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *  # noqa


def _expr(s, env):
    """{=a+1} in a figure spec: arithmetic on the template numbers (+ - * // %)."""
    t = s
    for k in sorted(env, key=len, reverse=True): t = re.sub(r'\b%s\b' % re.escape(k), str(env[k]), t)
    assert re.fullmatch(r'[\d\s+\-*/%().]*', t), s
    return eval(t)


def _subst(obj, env):
    if isinstance(obj, str):
        m = re.fullmatch(r'\{=([^{}]+)\}', obj)
        if m: return _expr(m.group(1), env)
        obj = re.sub(r'\{=([^{}]+)\}', lambda mm: str(_expr(mm.group(1), env)), obj)
        m = re.fullmatch(r'\{(\w+)\}', obj)
        if m and m.group(1) in env: return env[m.group(1)]
        return re.sub(r'\{(\w+)\}', lambda mm: str(env.get(mm.group(1), mm.group(0))), obj)
    if isinstance(obj, list): return [_subst(x, env) for x in obj]
    if isinstance(obj, dict): return {k: _subst(v, env) for k, v in obj.items()}
    return obj


def _ph(x):
    import json as _j
    return bool(re.search(r'"[^"]*\{=?\w[^"]*\}[^"]*"', _j.dumps(x)))


def _prepare_items(items):
    """Render item.fig to inline SVG at build time (item.svg); a figure with {vars} is drawn for every variant (tpl.svgs, up to 80 combinations)."""
    import copy, itertools, json as _j, svg
    out = copy.deepcopy(items)
    warns = []
    for it in out:
        fig = it.pop('fig', None); base = it.pop('fig_base', None)
        if not fig: continue
        tp0 = it.get('tpl')
        if _ph(fig) and not (tp0 and tp0.get('vars')):      # no variants: draw the figure as written (or its base)
            it['svg'] = svg.render_visual(base or fig)
            continue
        if not _ph(fig):
            it['svg'] = svg.render_visual(fig)
            if it.get('tpl'): warns.append(f"{it['id']}: the picture is shown only for the authored numbers (variants have no picture); use fig with {{vars}} and fig_base")
        else:
            tp = it['tpl']; names = list(tp['vars'])
            combos = list(itertools.product(*[tp['vars'][n] for n in names]))
            if len(combos) > 80: warns.append(f"{it['id']}: {len(combos)} variants, pictures drawn for the first 80 only"); combos = combos[:80]
            svgs = {}
            first = None
            for combo in combos:
                env = dict(zip(names, combo))
                full = dict(env)
                for k, ex in tp.get('derive', {}).items():
                    full[k] = eval(re.sub(r'\b(%s)\b' % '|'.join(map(re.escape, full)), lambda m: str(full[m.group(1)]), ex).replace('//', '//'))
                svgs[_j.dumps(env, separators=(',', ':'))] = svg.render_visual(_subst(fig, full))
                if first is None: first = svgs[_j.dumps(env, separators=(',', ':'))]
            it['svg'] = svg.render_visual(base) if base else first
            tp['svgs'] = svgs
        if len(it['svg']) > 60000: warns.append(f"{it['id']}: picture is {len(it['svg']) // 1000} KB")
    return out, warns


def build_practice(d):
    op = d['online_practice']
    od = outdir(d, 'practice')
    os.makedirs(os.path.join(od, 'data'), exist_ok=True)
    items, pw = _prepare_items(op['items'])
    for w in pw: print('WARN  practice picture:', w)
    data = {'runner': 2, 'title': op['title'], 'level': d['level'], 'lesson': d['lesson_in_term'], 'term': d['term'], 'topic': op['topic'], 'items': items}
    json.dump(data, open(os.path.join(od, 'data', op['key'] + '.json'), 'w'), ensure_ascii=False)
    # the Term 1 runner (term/l1/runner): relative paths, answer-order aware, shuffled choices (the level-wide runner in practice/public is untouched)
    shutil.copy(os.path.join(L1, 'runner', 'practice.js'), os.path.join(od, 'practice.js'))
    html = open(os.path.join(L1, 'runner', 'index.html'), encoding='utf-8').read()
    html = html.replace('<script src="practice.js">', f'<script>window.MI_LESSON={json.dumps(op["key"])};</script><script src="practice.js">')
    open(os.path.join(od, 'index.html'), 'w', encoding='utf-8').write(html)
    fonts = os.path.join(ROOT, 'website', 'dist')
    if os.path.isdir(os.path.join(fonts, 'fonts')):
        shutil.copytree(os.path.join(fonts, 'fonts'), os.path.join(od, 'fonts'), dirs_exist_ok=True)
        css = open(os.path.join(fonts, 'fonts.css'), encoding='utf-8').read().replace("url('/fonts/", "url('fonts/")
        open(os.path.join(od, 'fonts.css'), 'w', encoding='utf-8').write(css)
