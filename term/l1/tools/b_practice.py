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
    for f in ('index.html', 'practice.js'):
        shutil.copy(os.path.join(ROOT, 'practice', 'public', f), os.path.join(od, f))
    fonts = os.path.join(ROOT, 'website', 'dist')
    if os.path.isdir(os.path.join(fonts, 'fonts')):
        shutil.copytree(os.path.join(fonts, 'fonts'), os.path.join(od, 'fonts'), dirs_exist_ok=True)
        shutil.copy(os.path.join(fonts, 'fonts.css'), os.path.join(od, 'fonts.css'))
