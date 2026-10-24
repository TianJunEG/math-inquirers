"""Glue between the teaser batches and the page generators (lp_build.py, level_pages.py, build_site.py).

The daily teaser is OFF by default: the generators produce exactly the same pages as before unless
manifest.json has "site_enabled": true or the environment variable MI_TEASERS=1 is set (used for previews).
Nothing here touches website/dist.
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
LEVEL_AGES = {1: '6-8', 2: '7-9', 3: '8-10', 4: '9-11', 5: '10-12', 6: '11-13'}

CSS = '''
.pzcode{font:600 17px/1.5 ui-monospace,Menlo,Consolas,monospace;background:var(--bg);border:2px dashed var(--line);border-radius:12px;padding:10px 14px;margin:8px 0;white-space:pre;overflow-x:auto;max-width:100%}
.pzmeta{margin-top:10px}
.pzl .msg b{font-weight:800}
#pzMsg{margin-top:6px}
'''


def manifest():
    return json.load(open(os.path.join(HERE, 'manifest.json'), encoding='utf-8'))


def enabled():
    return bool(manifest().get('site_enabled')) or os.environ.get('MI_TEASERS') == '1'


def compact(e):
    """The fields the browser needs (no parameters, no wrong-answer lists)."""
    d = dict(i=e['id'], g=e['topic'], q=e['q'], a=e['ans'], t=e['type'], s=e['shown'], h=e['hint'], w=e['why'])
    if e.get('big'):
        d['b'] = e['big']
    if e.get('code'):
        d['c'] = e['code']
    if e['units']:
        d['u'] = e['units']
    if e['prefix']:
        d['p'] = e['prefix']
    if e['accept']:
        d['x'] = e['accept']
    if e['exact']:
        d['e'] = 1
    return d


def load_month(mm):
    return json.load(open(os.path.join(HERE, 'batches', 'm%s' % mm, 'bank.json'), encoding='utf-8'))


def released():
    return manifest()['released']


def fallback_pool(level):
    """Used when the visitor's month has no released batch (or the batch file cannot be fetched):
    the puzzles of the first released month for this level, in date order."""
    first = sorted(released())[0]
    return [compact(e) for e in load_month(first)['levels'][str(level)]]


def month_json(level, mm):
    """{ 'MM-DD': puzzle } for one level and one released month."""
    return {e['date']: compact(e) for e in load_month(mm)['levels'][str(level)]}


def export_public(dest):
    """Write the per-level, per-month files the pages fetch (dest/teasers/L<n>-<MM>.json)."""
    d = os.path.join(dest, 'teasers')
    os.makedirs(d, exist_ok=True)
    n = 0
    for mm in released():
        for lv in range(1, 7):
            with open(os.path.join(d, 'L%d-%s.json' % (lv, mm)), 'w', encoding='utf-8') as f:
                json.dump(month_json(lv, mm), f, ensure_ascii=False, separators=(',', ':'))
            n += 1
    return n


def widget_script(level, box_id='pzBox'):
    js = open(os.path.join(HERE, 'teasers.js'), encoding='utf-8').read()
    pool = json.dumps(fallback_pool(level), ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
    boot = ('(function(){var b=document.getElementById("%s");if(!b||!window.MiTeaser)return;'
            'try{MiTeaser.init({box:b,level:%d,ages:"%s",pool:%s,base:"/teasers/"})}catch(e){}})();'
            % (box_id, level, LEVEL_AGES[level], pool))
    return '<script>\n' + js + '\n' + boot + '\n</script>'
