#!/usr/bin/env python3
"""Build the tutor console data for a level from the generated slide decks and the lesson scripts.

    python3 build_data.py 4            # writes data/p4l1..p4l10 .public.json / .notes.json and data/index.json

public.json  (the lesson screen may load this): slide order, titles, optional flags, part timeline
notes.json   (the tutor's phone only):          speaker notes per slide, SAY / DO / IF STUCK lines per part

Part budgets (PARTS) are the current guide tables. When the re-budget pass lands, change PARTS only.
"""
import json, os, re, subprocess, sys, html

ROOT = os.path.dirname(os.path.abspath(__file__)) + '/..'
OUT = os.path.dirname(os.path.abspath(__file__)) + '/data'

# (start, end, title, script key) per level; mirrors pN/guide.js seg() calls (lesson 10 varies slightly)
PARTS = {
 4: [(0,1,'Opening','hook'),(1,4,'Sneak-peek puzzles',None),(4,8,'Warm-up','warmIntro'),(8,18,'Explore (in pairs)','predict'),
     (18,30,'Mini-lesson','think'),(30,34,'Brain break',None),(34,80,'Worksheet','circulate'),(80,85,'Talk time','talk'),(85,88,'Exit ticket','close'),(88,90,'Looking back',None)],
}

def strip(t): return html.unescape(re.sub(r'<[^>]+>', ' ', t)).replace(' ', ' ').strip()

def node(js):
    return json.loads(subprocess.run(['node', '-e', js], capture_output=True, text=True, cwd=ROOT).stdout or 'null')

def build(level):
    parts = PARTS[level]
    scripts = node("const d=require('./p%d/data.js');console.log(JSON.stringify(d.scripts))" % level) or {}
    lessons = node("const d=require('./p%d/data.js');console.log(JSON.stringify(d.lessons.map(l=>({n:l.n,title:l.title,topic:l.topic}))))" % level) or []
    index = []
    os.makedirs(OUT, exist_ok=True)
    for L in lessons:
        n = L['n']; deck = 'p%dl%d' % (level, n); base = '%s/split/%s/project' % (ROOT, deck)
        order = json.load(open(base + '/deck.json'))['order']
        slides, notes_slides, prev_part = [], {}, 0
        for sid in order:
            h = open('%s/slides/%s.html' % (base, sid), encoding='utf-8').read()
            m = re.search(r'border-radius:999px[^>]*>([^<]*)</p>', h); pill = html.unescape(m.group(1)) if m else ''
            t = re.search(r'<h[12][^>]*>(.*?)</h[12]>', h, re.S); title = strip(t.group(1)) if t else sid
            opt = bool(re.search(r'OPTIONAL|take-home|only if time', pill, re.I))
            st = re.match(r'\s*(\d+)', pill); part = None
            if st and not re.match(r'\s*Any', pill):
                mn = int(st.group(1))
                part = next((i for i, p in enumerate(parts) if p[0] <= mn < p[1]), None)
            if sid.endswith('-title'): part = 0
            if sid.endswith('-break'): part = next(i for i, p in enumerate(parts) if p[2] == 'Brain break')
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
            if ptitle.startswith('Explore'): stuck = list(s.get('exploreHints', []))
            if ptitle == 'Worksheet': do = list(s.get('circulate', [])); say = []; stuck = list(s.get('hints', []))
            if ptitle == 'Mini-lesson': say = list(s.get('think', []))
            ask = []
            if ptitle == 'Talk time' and s.get('talkAns'): ask = [[q, s['talkAns']] for q in s.get('talk', [])[:1]]
            np[str(i)] = {'say': say, 'do': do, 'stuck': stuck, 'ask': ask}
        pub = {'id': deck, 'deck': deck, 'title': 'Level %d lesson %d: %s' % (level, n, L['title']), 'level': level, 'lesson': n,
               'parts': [{'title': p[2], 'min': p[1] - p[0]} for p in parts], 'slides': slides}
        json.dump(pub, open('%s/%s.public.json' % (OUT, deck), 'w'), ensure_ascii=False)
        json.dump({'parts': np, 'slides': notes_slides}, open('%s/%s.notes.json' % (OUT, deck), 'w'), ensure_ascii=False)
        index.append({'id': deck, 'label': 'L%d.%d %s' % (level, n, L['title'])})
    prev = json.load(open(OUT + '/index.json'))['lessons'] if os.path.exists(OUT + '/index.json') else []
    keep = [x for x in prev if not x['id'].startswith('p%dl' % level)]
    json.dump({'lessons': keep + index}, open(OUT + '/index.json', 'w'), ensure_ascii=False)
    print('built', len(index), 'lessons for level', level)

if __name__ == '__main__':
    build(int(sys.argv[1]) if len(sys.argv) > 1 else 4)
