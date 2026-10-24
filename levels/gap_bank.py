#!/usr/bin/env python3
"""Tutor-bank files and digital tutor sheets for the Level 4-6 skill additions (levels/gap_items.py). Same file formats as the Level 1-3 job
(rebuild/gen_skill_slides.py): pN/qbank_skills.json and outputs/skill_additions/Math_Inquirers_L<N>_Skill_Additions_Tutor_Sheet.{html,pdf}.
    python3 levels/gap_bank.py [4|5|6|all]        (idempotent; nothing printed is touched; pN/content/*.js and hp/qbank.json are NOT edited)
Every slide item appears once (slot 'slide'); its same-skill variant (checked by levels/gap_verify.py) appears as a 'bank' item with id '<id>-V'."""
import json, os, sys, html
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.join(HERE, '..'); sys.path.insert(0, HERE)
import gap_items, gap_slides
E = html.escape; M = gap_slides.M
SPINE = json.load(open(os.path.join(HERE, 'spine.json')))
TID = {t['name']: t['id'] for t in SPINE['tools']}
def sid(it): return f"p{it['lv']}l{it['ln']}-gap-{it['id']}"
def rows(level):
    out = []
    for it in gap_items.ITEMS:
        if it['lv'] != level: continue
        base = dict(skill=it['skill'], tool=TID[it['tool']], tool_name=it['tool'], ln=it['ln'])
        out.append(dict(base, id=f"L{level}-{it['id'].upper()}", slot='slide', slide=sid(it), q=M(' '.join(it['q'])), a=M(' '.join(it['ans'])),
                        say=M(it['say']), ask=M(it['ask']), listen=M(it['listen']), kind=it['kind'], preview=bool(it.get('preview'))))
        if it.get('var'):
            out.append(dict(base, id=f"L{level}-{it['id'].upper()}-V", slot='bank', q=M(it['var'][0]), a=M(it['var'][1]),
                            say='Same skill, new numbers. Use the same tool and the same steps as the slide item (%s).' % it['skill'], ask=M(it['ask']), listen=M(it['listen']),
                            kind='Bank', preview=bool(it.get('preview'))))
    return out
def write_bank(level):
    d = {}
    for r in rows(level):
        d.setdefault(str(r['ln']), {'skills': []})['skills'].append({k: r[k] for k in ('id', 'slot', 'skill', 'tool', 'tool_name', 'q', 'a', 'say', 'ask', 'listen')} | ({'preview': True} if r['preview'] else {}))
    d = {k: d[k] for k in sorted(d, key=int)}
    path = os.path.join(ROOT, f'p{level}', 'qbank_skills.json')
    json.dump(d, open(path, 'w', encoding='utf-8'), indent=1, ensure_ascii=False); open(path, 'a').write('\n'); return path
def write_sheet(level):
    out_dir = os.path.join(ROOT, 'outputs', 'skill_additions'); os.makedirs(out_dir, exist_ok=True)
    css = ('body{font-family:Nunito Sans,Arial,sans-serif;color:#1B2A49;margin:24px auto;max-width:900px;line-height:1.4}h1{font-family:Fredoka,Arial;font-size:28px}'
           'h2{font-family:Fredoka,Arial;font-size:22px;border-bottom:3px solid #1F7A6F;margin-top:28px}.it{border:1px solid #ccd;border-radius:10px;padding:10px 14px;margin:10px 0;break-inside:avoid}'
           '.tag{display:inline-block;background:#FFC93C;border-radius:999px;padding:1px 10px;font-size:12px;font-weight:700;margin-right:6px}.bank{background:#DDEBF7}.pre{background:#1B2A49;color:#FFF9EC}'
           '.k{font-weight:800;color:#1F7A6F}p{margin:4px 0}')
    h = [f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Level {level} skill additions: tutor sheet</title><style>{css}</style></head><body>',
         f'<h1>Math Inquirers Level {level}: skill additions (tutor sheet)</h1>',
         '<p>Extra items for early finishers and for tutors to set live. They are additions: nothing here is in the printed workbook. '
         '<b>Slide</b> items are on an optional slide in the lesson deck (just before Talk time). <b>Bank</b> items are the same skill with new numbers: read or write them for the pair. '
         'Children write the answer on their own paper and say it together on three. Nothing is held up to the camera. Never announce who is working on which item.</p>']
    if level == 5:
        h.append('<p><b>Ratio previews.</b> Items marked PREVIEW teach ratio (a : b) from first principles. Ratio is a Primary 6 topic and is beyond Level 5: say "a first taste, not a test".</p>')
    cur = None
    for r in rows(level):
        if r['ln'] != cur:
            cur = r['ln']; h.append(f'<h2>Lesson {cur}: {E(SPINE["lessons"][f"{level}.{cur}"]["title"])}</h2>')
        cls = 'it bank' if r['slot'] == 'bank' else 'it'
        pre = '<span class="tag pre">PREVIEW</span>' if r['preview'] else ''
        h.append(f'<div class="{cls}"><p><span class="tag">{r["slot"].upper()}</span><span class="tag">Tool: {E(r["tool_name"])}</span>{pre}<b>{E(r["skill"])}</b> ({r["id"]})</p>'
                 f'<p>{E(r["q"])}</p><p><span class="k">Answer.</span> {E(r["a"])}</p><p><span class="k">Say.</span> {E(r["say"])}</p>'
                 f'<p><span class="k">Ask.</span> {E(r["ask"])}</p><p><span class="k">Listen for.</span> {E(r["listen"])}</p></div>')
    h.append('</body></html>')
    path = os.path.join(out_dir, f'Math_Inquirers_L{level}_Skill_Additions_Tutor_Sheet.html')
    open(path, 'w', encoding='utf-8').write('\n'.join(h))
    try:
        from playwright.sync_api import sync_playwright
        with sync_playwright() as pw:
            b = pw.chromium.launch(); pg = b.new_page(); pg.goto('file://' + os.path.abspath(path))
            pg.pdf(path=path[:-5] + '.pdf', format='A4', margin={'top': '14mm', 'bottom': '14mm', 'left': '12mm', 'right': '12mm'}, print_background=True); b.close()
    except Exception as e: print('PDF skipped:', e)
    return path
if __name__ == '__main__':
    arg = sys.argv[1] if len(sys.argv) > 1 else 'all'
    for lv in ([4, 5, 6] if arg == 'all' else [int(arg)]): print(lv, write_bank(lv), write_sheet(lv))
