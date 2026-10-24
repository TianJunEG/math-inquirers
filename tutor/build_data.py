"""Build the tutor console data for a level from the generated slide decks, the lesson scripts and the level's budget.json.

    python3 build_data.py 4            # one level
    python3 build_data.py all          # Levels 1 to 6 (default)

public.json  (the lesson screen may load this): slide order, titles, optional flags, part timeline
notes.json   (the tutor's phone only):          speaker notes per slide, SAY / DO / IF STUCK lines per part

Part budgets come from <level>/budget.json (hp/budget.json for Level 1), the same file the tutor guide reads, so the
console clock, the guide and the scheme of work agree. Times may be half minutes (7.5).
"""
import json, os, re, subprocess, sys, html

ROOT = os.path.dirname(os.path.abspath(__file__)) + '/..'
OUT = os.path.dirname(os.path.abspath(__file__)) + '/data'
NUM = r'(\d+(?:\.\d+)?)'          # whole or half-minute number, e.g. 7 or 7.5

def budget(level):
    d = 'hp' if level == 1 else 'p%d' % level
    return json.load(open('%s/%s/budget.json' % (ROOT, d)))['lessons']

def script_key(title):
    t = title.lower()
    if t.startswith('opening'): return 'hook'
    if 'warm' in t or 'game' in t: return 'warmIntro'
    if t.startswith('explore'): return 'predict'
    if t.startswith('mini'): return 'think'
    if ('worksheet' in t or 'workbook' in t) and 'teach' not in t: return 'circulate'
    if t.startswith('talk'): return 'talk'
    if t.startswith('exit'): return 'close'
    return None

def habit_line(level, n):
    """'Focus habit: Notice - <teaching move> Say: "<prompt>" <rule>' from levels/habits.json (same wording as the guide front page and the slide badge)."""
    H = json.load(open(ROOT + '/levels/habits.json', encoding='utf-8')); name = H['lessons']['%d.%d' % (level, n)]; h = H['habits'][name]
    return name, '%s: %s - %s Say: \u201c%s\u201d %s' % (H['badge_label'], name, h['move'], h['prompt'], H['rule'])

def strip(t): return html.unescape(re.sub(r'<[^>]+>', ' ', t)).replace(' ', ' ').strip()

def node(js):
    return json.loads(subprocess.run(['node', '-e', js], capture_output=True, text=True, cwd=ROOT).stdout or 'null')

def build(level):
    bud = budget(level)
    if level == 1:
        scripts = node("console.log(JSON.stringify(require('./hp/scripts.js')))") or {}
        lessons = node("console.log(JSON.stringify(require('./hp/lessons.js').lessons.map(l=>({n:l.n,title:l.title,topic:l.topic}))))") or []
    else:
        scripts = node("const d=require('./p%d/data.js');console.log(JSON.stringify(d.scripts))" % level) or {}
        lessons = node("const d=require('./p%d/data.js');console.log(JSON.stringify(d.lessons.map(l=>({n:l.n,title:l.title,topic:l.topic}))))" % level) or []
    index = []
    os.makedirs(OUT, exist_ok=True)
    for L in lessons:
        n = L['n']; cid = 'p%dl%d' % (level, n); deck = 'l%d' % n if level == 1 else cid
        base = '%s/split/%s/project' % (ROOT, deck)
        parts = [(p['start'], p['end'], p['title'], script_key(p['title'])) for p in bud[str(n)]['parts']]
        order = json.load(open(base + '/deck.json'))['order']
        slides, notes_slides, prev_part = [], {}, 0
        for sid in order:
            h = open('%s/slides/%s.html' % (base, sid), encoding='utf-8').read()
            m = re.search(r'border-radius:999px[^>]*>([^<]*)</p>', h); pill = html.unescape(m.group(1)) if m else ''
            t = re.search(r'<h[12][^>]*>(.*?)</h[12]>', h, re.S); title = strip(t.group(1)) if t else sid
            opt = bool(re.search(r'OPTIONAL|take-home|only if time', pill, re.I))
            st = re.match(r'\s*' + NUM, pill); part = None
            if st and not re.match(r'\s*Any', pill):
                mn = float(st.group(1)) + 1e-6
                part = next((i for i, p in enumerate(parts) if p[0] <= mn < p[1]), None)
            if sid.endswith('-title'): part = 0
            if sid.endswith('-break'):
                part = next((i for i, p in enumerate(parts) if p[2].lower().startswith('brain break')), part)
            if part is None: part = prev_part
            prev_part = part
            a = re.search(r'<aside[^>]*>(.*?)</aside>', h, re.S)
            slides.append({'id': sid, 'title': title, 'part': part, 'optional': opt})
            if a: notes_slides[sid] = {'note': re.sub(r'[ \t]+', ' ', strip(a.group(1)))}
        s = scripts.get(str(n)) or scripts.get(n) or {}
        np = {}
        for i, (a_, b_, ptitle, key) in enumerate(parts):
            say = list(s.get(key, [])) if key and isinstance(s.get(key), list) else []
            do, stuck = [], []
            if key == 'predict': stuck = list(s.get('exploreHints', []))
            if key == 'circulate': do = list(s.get('circulate', [])); say = []; stuck = list(s.get('hints', []))
            if key == 'think': say = list(s.get('think', []))
            ask = []
            if key == 'talk' and s.get('talkAns'): ask = [[q, s['talkAns']] for q in s.get('talk', [])[:1]]
            if i == 0: do = do + [habit_line(level, n)[1]]          # focus habit line, shown with the Opening part on the phone
            np[str(i)] = {'say': say, 'do': do, 'stuck': stuck, 'ask': ask}
        pub = {'id': cid, 'deck': deck, 'title': 'Level %d lesson %d: %s' % (level, n, L['title']), 'level': level, 'lesson': n,
               'parts': [{'title': p[2], 'min': round(p[1] - p[0], 2)} for p in parts], 'slides': slides}
        json.dump(pub, open('%s/%s.public.json' % (OUT, cid), 'w'), ensure_ascii=False)
        json.dump({'habit': habit_line(level, n)[0], 'habit_line': habit_line(level, n)[1], 'parts': np, 'slides': notes_slides}, open('%s/%s.notes.json' % (OUT, cid), 'w'), ensure_ascii=False)
        index.append({'id': cid, 'label': 'L%d.%d %s' % (level, n, L['title'])})
    prev = json.load(open(OUT + '/index.json'))['lessons'] if os.path.exists(OUT + '/index.json') else []
    keep = [x for x in prev if not x['id'].startswith('p%dl' % level)]
    allx = sorted(keep + index, key=lambda x: tuple(int(v) for v in re.findall(r'\d+', x['id'])))
    json.dump({'lessons': allx}, open(OUT + '/index.json', 'w'), ensure_ascii=False)
    print('built', len(index), 'lessons for level', level)

if __name__ == '__main__':
    arg = sys.argv[1] if len(sys.argv) > 1 else 'all'
    for lv in (range(1, 7) if arg == 'all' else [int(arg)]): build(lv)
