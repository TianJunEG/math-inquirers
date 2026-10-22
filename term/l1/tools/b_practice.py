"""Online practice: writes out/lNN/practice/ (runner + data) in the format of practice/public (see practice/README.md)."""
import json, os, shutil, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *  # noqa


def build_practice(d):
    op = d['online_practice']
    od = outdir(d, 'practice')
    os.makedirs(os.path.join(od, 'data'), exist_ok=True)
    data = {'title': op['title'], 'level': d['level'], 'lesson': d['lesson_in_term'], 'term': d['term'], 'topic': op['topic'], 'items': op['items']}
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
