#!/usr/bin/env python3
"""Add the skill-gap slides and tutor-bank items (Levels 1 to 3) to the holiday decks. Idempotent.

    python3 rebuild/gen_skill_slides.py 1        # one level (1, 2 or 3)
    python3 rebuild/gen_skill_slides.py all

What it does (owner decision GAPS-SLIDES-NOW; nothing printed is touched):
  * writes one optional slide per (lesson, group) to split/<deck>/project/slides/<key>-skill<g>.html
    (pill 'Optional, if you finish early'; answers and SAY / ASK / LISTEN FOR only in the speaker notes)
  * inserts those slides in deck.json after <key>-chwalk (before Talk time) and drops stale ones
  * writes the bank file  hp/qbank_skills.json  or  pN/qbank_skills.json  (all items of the level, slide and bank)
  * writes the digital tutor sheet  outputs/skill_additions/Math_Inquirers_L<N>_Skill_Additions_Tutor_Sheet.html
After running, run levels/restyle.py on the changed decks (twice) and tutor/build_data.py N.
"""
import json, os, sys, html, re
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, H)
from slidekit import *
import skillkit as K
from skill_items_l1_3 import ITEMS, GROUPS, TOOLS

ROOT = os.path.join(H, '..')
OPT = 'Optional, if you finish early'
SPINE = json.load(open(os.path.join(ROOT, 'levels', 'spine.json')))


def key_of(level, n): return f'l{n}' if level == 1 else f'p{level}l{n}'
def deck_dir(level, n): return os.path.join(ROOT, 'split', key_of(level, n), 'project')


def fig_html(spec):
    name, kw = spec
    kw = dict(kw); z = kw.pop('zoom', None)
    h = _fig_html(name, kw)
    return f'<div style="zoom:{z}">{h}</div>' if z else h


def _fig_html(name, kw):
    if name == 'seq':
        return K.seq_table(**kw)
    if name == 'sym':
        return '<div style="display:flex;flex-direction:column;gap:14px">' + ''.join(K.sym_line(l, 72, 60) for l in kw['lines']) + '</div>'
    if name == 'letters': return K.letter_sum(**kw)
    if name == 'cards': return K.cards(w=110, h=150, **kw)
    if name == 'bars': return K.bars(unit=84, **kw)
    if name == 'week': return K.week_strip(**kw)
    if name == 'iso': return K.iso(**{'s': 64, **kw})
    if name == 'clock': return K.clock(size=400, **kw)
    if name == 'heights': return K.height_grid(cell=120, **kw)
    if name == 'window': return K.window(**{'cell': 130, **kw})
    if name == 'path': return K.path_posts(**kw)
    if name == 'faces':
        seq = [('open', 'smile'), ('closed', 'flat'), ('open', 'open'), ('closed', 'smile'), ('open', 'flat'), ('closed', 'open')][:kw['n']]
        return K.face_row(seq, 150)
    raise KeyError(name)


BELOW = {'week', 'seq', 'faces', 'path'}


def item_card(num, it, size):
    parts = ''.join(f'<p style="font-size:{size}px;font-weight:600;line-height:1.3">{E(x)}</p>' for x in it['parts'])
    txt = (f'<div style="display:flex;flex-direction:column;gap:8px;flex:1;min-width:0">'
           f'<p style="font-size:{size}px;font-weight:700;line-height:1.3"><span style="color:#1F7A6F;font-weight:800">{num}.</span>  {E(it["stem"])}</p>{parts}</div>')
    if not it['fig']:
        return card(txt)
    f = fig_html(it['fig'])
    if it['fig'][0] in BELOW:
        return card(txt + f'<div style="align-self:flex-start">{f}</div>')
    return card(f'<div style="display:flex;gap:40px;align-items:center">{txt}<div style="flex:none">{f}</div></div>')


def notes_for(items, title):
    out = ['Optional slide for pairs who finish early or ask for more. Show it only on request and never announce who is working on it. Children write the answer on their own paper and say it together on three; nothing is held up to the camera. Answers and tutor lines are for you only.']
    for k, it in enumerate(items, 1):
        out.append(f'Item {k} ({it["skill"]}; tool of the day idea: {TOOLS[it["tool"]]}). SAY: "{it["say"]}" ASK: "{it["ask"]}" LISTEN FOR: {it["listen"]} ANSWER: {it["a"]}')
    return ' '.join(out)


def build_slide(level, n, g, items):
    key = key_of(level, n); sid = f'{key}-skill{g[1:]}'
    title = GROUPS[(level, n, g)]
    total = sum(len(i['stem']) + sum(len(x) for x in i['parts']) for i in items)
    size = 46 if total < 200 else 42 if total < 300 else 38 if total < 420 else 34 if total < 560 else 30
    body = h2(title, 60)
    for k, it in enumerate(items, 1):
        body += item_card(k, it, size)
    return sid, sec(sid, OPT, body, notes_for(items, title))


def update_deck(level, n, new_ids):
    D = deck_dir(level, n); dj = os.path.join(D, 'deck.json'); deck = json.load(open(dj))
    key = key_of(level, n)
    order = [s for s in deck['order'] if not re.match(rf'^{re.escape(key)}-skill\d+$', s)]
    anchor = f'{key}-chwalk' if f'{key}-chwalk' in order else f'{key}-challenge'
    at = order.index(anchor) + 1
    order[at:at] = new_ids
    deck['order'] = order
    json.dump(deck, open(dj, 'w'), indent=1, ensure_ascii=False)


def bank_q(it):
    return ' '.join([it['stem']] + it['parts'])


def write_bank(level):
    items = [i for i in ITEMS if i['level'] == level]
    d = {}
    for n in range(1, 11):
        rows = [dict(id=i['id'], slot=i['slot'], skill=i['skill'], tool=i['tool'], tool_name=TOOLS[i['tool']], q=bank_q(i), a=i['a'],
                     say=i['say'], ask=i['ask'], listen=i['listen']) for i in items if i['lesson'] == n]
        if rows: d[str(n)] = {'skills': rows}
    path = os.path.join(ROOT, 'hp' if level == 1 else f'p{level}', 'qbank_skills.json')
    json.dump(d, open(path, 'w'), indent=1, ensure_ascii=False); open(path, 'a').write('\n')
    return path


def lesson_title(level, n):
    return SPINE['lessons'][f'{level}.{n}']['title']


def write_sheet(level):
    items = [i for i in ITEMS if i['level'] == level]
    out_dir = os.path.join(ROOT, 'outputs', 'skill_additions'); os.makedirs(out_dir, exist_ok=True)
    css = ('body{font-family:Nunito Sans,Arial,sans-serif;color:#1B2A49;margin:24px auto;max-width:900px;line-height:1.4}h1{font-family:Fredoka,Arial;font-size:28px}'
           'h2{font-family:Fredoka,Arial;font-size:22px;border-bottom:3px solid #1F7A6F;margin-top:28px}.it{border:1px solid #ccd;border-radius:10px;padding:10px 14px;margin:10px 0;break-inside:avoid}'
           '.tag{display:inline-block;background:#FFC93C;border-radius:999px;padding:1px 10px;font-size:12px;font-weight:700;margin-right:6px}.bank{background:#DDEBF7}'
           '.k{font-weight:800;color:#1F7A6F}p{margin:4px 0}')
    h = [f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Level {level} skill additions: tutor sheet</title><style>{css}</style></head><body>',
         f'<h1>Math Inquirers Level {level}: skill additions (tutor sheet)</h1>',
         '<p>Extra items for early finishers and for tutors to set live. They are additions: nothing here is in the printed workbook. '
         '<b>Slide</b> items are on an optional slide in the lesson deck (after the Go further walk-through). <b>Bank</b> items are not on a slide: read or write them for the pair. '
         'Children write the answer on their own paper and say it together on three. Nothing is held up to the camera. Never announce who is working on which item.</p>']
    for n in range(1, 11):
        rows = [i for i in items if i['lesson'] == n]
        if not rows: continue
        h.append(f'<h2>Lesson {n}: {E(lesson_title(level, n))}</h2>')
        for i in rows:
            cls = 'it bank' if i['slot'] == 'bank' else 'it'
            h.append(f'<div class="{cls}"><p><span class="tag">{i["slot"].upper()}</span><span class="tag">Tool: {E(TOOLS[i["tool"]])}</span><b>{E(i["skill"])}</b> ({i["id"]})</p>'
                     f'<p>{E(i["stem"])}</p>' + ''.join(f'<p>{E(x)}</p>' for x in i['parts']) +
                     f'<p><span class="k">Answer.</span> {E(i["a"])}</p><p><span class="k">Say.</span> {E(i["say"])}</p>'
                     f'<p><span class="k">Ask.</span> {E(i["ask"])}</p><p><span class="k">Listen for.</span> {E(i["listen"])}</p></div>')
    h.append('</body></html>')
    path = os.path.join(out_dir, f'Math_Inquirers_L{level}_Skill_Additions_Tutor_Sheet.html')
    open(path, 'w', encoding='utf-8').write('\n'.join(h))
    return path


def run(level):
    items = [i for i in ITEMS if i['level'] == level]
    changed = []
    for n in sorted({i['lesson'] for i in items if i['slot'] == 'slide'}):
        D = deck_dir(level, n); ids = []
        groups = sorted({i['group'] for i in items if i['lesson'] == n and i['slot'] == 'slide'})
        for g in groups:
            its = [i for i in items if i['lesson'] == n and i['slot'] == 'slide' and i['group'] == g]
            sid, htm = build_slide(level, n, g, its)
            open(os.path.join(D, 'slides', sid + '.html'), 'w', encoding='utf-8').write(htm); ids.append(sid)
        update_deck(level, n, ids); changed.append(key_of(level, n))
    print('level', level, 'decks changed:', ', '.join(changed))
    print('bank:', write_bank(level)); print('sheet:', write_sheet(level))
    return changed


if __name__ == '__main__':
    arg = sys.argv[1] if len(sys.argv) > 1 else 'all'
    for lv in ([1, 2, 3] if arg == 'all' else [int(arg)]): run(lv)
