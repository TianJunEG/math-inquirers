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
#pzMsg,#pzdMsg{margin-top:6px}
#pzdMsg:focus{outline:3px solid var(--ink);outline-offset:3px;border-radius:14px}
.pzdaily{display:contents}
.pzlab{font:800 13px var(--body);color:var(--muted)}
[hidden]{display:none!important}
/* light mode: the hint (red) and the worked answer (green) text need 4.5:1 on their tinted boxes; dark mode keeps the page colours */
.pzl{--pzno:#A82D2D;--pzok:#17655B}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]) .pzl{--pzno:var(--red);--pzok:var(--teal)}}
:root[data-theme="dark"] .pzl{--pzno:var(--red);--pzok:var(--teal)}
.pzl .msg.no{color:var(--pzno)}
.pzl .msg.ok{color:var(--pzok)}
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


def month_json(level, mm):
    """{ 'MM-DD': puzzle } for one level and one released month."""
    return {e['date']: compact(e) for e in load_month(mm)['levels'][str(level)]}


def export_public(dest):
    """Write the per-level, per-month files the pages can fetch (dest/teasers/L<n>-<MM>.json) for released months that are not built into the page."""
    d = os.path.join(dest, 'teasers')
    os.makedirs(d, exist_ok=True)
    n = 0
    for mm in released():
        for lv in range(1, 7):
            with open(os.path.join(d, 'L%d-%s.json' % (lv, mm)), 'w', encoding='utf-8') as f:
                json.dump(month_json(lv, mm), f, ensure_ascii=False, separators=(',', ':'))
            n += 1
    return n


INLINE_MONTHS = 2     # the latest released months are built into every page, so the day's puzzle never depends on the network


def inline_months():
    return sorted(released())[-INLINE_MONTHS:]


def widget_script(level, box_id='pzBox'):
    js = open(os.path.join(HERE, 'teasers.js'), encoding='utf-8').read()
    inline = {mm: month_json(level, mm) for mm in inline_months()}
    data = json.dumps(inline, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
    boot = ('(function(){var b=document.getElementById("%s");if(!b||!window.MiTeaser)return;'
            'try{MiTeaser.init({box:b,level:%d,ages:"%s",released:%s,inline:%s,base:"/teasers/"})}catch(e){}})();'
            % (box_id, level, LEVEL_AGES[level], json.dumps(sorted(released())), data))
    return '<script>\n' + js + '\n' + boot + '\n</script>'

