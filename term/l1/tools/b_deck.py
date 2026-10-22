"""Lesson slide deck builder: JSON -> Claude Slides source (1920x1080 <section> files + deck.json), a single viewing HTML and a PDF.

Same look as the holiday decks (rebuild/slidekit.py + levels/restyle.py 'modern2'): light slides #F3F6FB with a top bar,
navy gradient for title/break/end slides, Fredoka headings, Nunito Sans body, teal accent, yellow answers.
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import *  # noqa
import svg

BF = "'Nunito Sans', Arial, sans-serif"
HF = "'Fredoka', Arial, sans-serif"
SOFTBG = '#F3F6FB'
CARD = 'background:#FFFFFF;border:2px solid #DCE4F0;box-shadow:0 6px 18px rgba(27,42,73,0.08);border-radius:24px;'
FOOT = FOOT_PARENT


def bar():
    return (f'<div data-deco="bar" style="position:absolute;left:0;top:0;width:1920px;height:18px;display:flex"><div style="flex:5;background:{NAVY}"></div>'
            f'<div style="flex:3;background:{TEAL}"></div><div style="flex:1;background:{YEL}"></div></div>')


def bubbles():
    return ('<div data-deco="bubbles" style="position:absolute;left:0;top:0;width:1920px;height:1080px;overflow:hidden"><svg width="1920" height="1080" viewBox="0 0 1920 1080" xmlns="http://www.w3.org/2000/svg" style="position:absolute;left:0;top:0">'
            '<g transform="translate(1920,0) scale(0.72) translate(-1920,0)"><path d="M1500 80 C1420 80 1380 150 1410 210 C1340 230 1330 330 1410 360 C1400 440 1500 480 1570 430 C1630 480 1760 470 1790 390 C1880 380 1900 280 1840 230 C1880 150 1810 70 1730 100 C1690 40 1560 40 1500 80 Z" fill="#1F7A6F"/>'
            '<text x="1610" y="340" font-size="250" font-weight="800" text-anchor="middle" fill="#FFF9EC" font-family="Fredoka, Arial, sans-serif">?</text>'
            '<g transform="translate(-590,-680)"><path d="M1640 800 Q1640 740 1700 740 L1800 740 Q1860 740 1860 800 L1860 850 Q1860 910 1800 910 L1740 910 L1690 960 L1700 910 Q1640 910 1640 850 Z" fill="#FFC93C"/>'
            '<text x="1750" y="868" font-size="120" font-weight="800" text-anchor="middle" fill="#1B2A49" font-family="Fredoka, Arial, sans-serif">!</text></g></g></svg></div>')


def chip(text, size=30, bg=TEAL, fg=CREAM):
    return f'<p style="align-self:flex-start;background:{bg};color:{fg};border-radius:999px;padding:8px 26px;font-size:{size}px;font-weight:700;line-height:1.25">{E(text)}</p>'


def para(text, size=44, weight=600, color=None):
    c = f'color:{color};' if color else ''
    return f'<p style="font-size:{size}px;font-weight:{weight};{c}line-height:1.3">{E(text)}</p>'


def card(head, items, size=40):
    inner = chip(head, 26) if head else ''
    inner += ''.join(f'<p style="font-size:{size}px;font-weight:600;line-height:1.3;color:{NAVY}">{E(i)}</p>' for i in items)
    return f'<div style="{CARD}padding:24px 40px;display:flex;flex-direction:column;gap:12px">{inner}</div>'


def listing(items, ordered, size=42):
    out = []
    for n, it in enumerate(items, 1):
        mark = (f'<span style="flex:none;width:52px;height:52px;border-radius:50%;background:{YEL};border:3px solid {NAVY};display:flex;align-items:center;justify-content:center;font-family:{HF};font-size:30px;font-weight:700">{n}</span>'
                if ordered else f'<span style="flex:none;width:18px;height:18px;border-radius:50%;background:{TEAL};margin-top:16px"></span>')
        out.append(f'<div style="display:flex;gap:22px;align-items:flex-start"><p style="font-size:{size}px;font-weight:600;line-height:1.3;display:flex;gap:22px;align-items:flex-start">{mark}<span>{E(it)}</span></p></div>')
    return f'<div style="{CARD}padding:26px 40px;display:flex;flex-direction:column;gap:14px">{"".join(out)}</div>'


def visual(b, ctx_cols=1):
    v = {k: b[k] for k in b if k not in ('t',)}
    small = b.get('size') == 's' or ctx_cols > 1
    w = 560 if small else (900 if b['type'] in ('bundles', 'scatter') else 1000)
    if b['type'] == 'ten_frame': w = 640 if not b.get('extra') else 1000
    if b['type'] == 'scatter': w = 760
    if b['type'] == 'number_line': w = 1500 if ctx_cols == 1 else 760
    if b['type'] == 'hundred_square': w = 640
    s = svg.render_visual(b)
    inner = f'<div style="width:{w}px;max-width:100%">{s}</div>'
    if b.get('table'):
        inner += svg.place_table(b['tens'], b['ones'], big=True).replace('<table class="pv big">', '<table style="border-collapse:collapse;font-family:' + HF + ';font-size:60px;text-align:center;margin-top:8px">').replace('<th>', f'<th style="border:3px solid {NAVY};padding:6px 40px;background:{YEL};font-size:34px">').replace('<td>', f'<td style="border:3px solid {NAVY};padding:6px 40px;background:#fff;font-weight:700">')
    if b.get('label') and not b.get('table'):
        pass
    if b.get('label') and b.get('table'):
        inner += f'<p style="font-size:38px;font-weight:700;color:{TEAL}">{E(b["label"])}</p>'
    if b.get('label') and b['type'] == 'bundles' and not b.get('table'):
        inner += f'<p style="font-size:38px;font-weight:700;color:{NAVY};text-align:center">{E(b["label"])}</p>'
    return f'<div style="{CARD}padding:18px 30px;display:flex;flex-direction:column;align-items:center;gap:6px">{inner}</div>'


def numrow(items):
    size = 54 if all(len(str(i)) <= 3 for i in items) else 46
    tiles = ''.join(f'<span style="min-width:96px;padding:10px 24px;border-radius:18px;border:3px solid {NAVY};color:{NAVY};background:{YEL if k % 2 == 0 else "#FFFFFF"};font-family:{HF};font-size:{size}px;font-weight:700;text-align:center">{E(str(i))}</span>' for k, i in enumerate(items))
    return f'<div style="display:flex;flex-wrap:wrap;gap:16px;align-items:center">{tiles}</div>'


def table(rows, header):
    out = []
    for r, row in enumerate(rows):
        hd = header and r == 0
        cells = []
        for c, t in enumerate(row):
            w = 520 if c == 0 else 1000
            cells.append(f'<div style="width:{w}px;padding:12px 24px;font-size:{34 if not hd else 30}px;font-weight:{800 if (hd or c == 0) else 600};{"color:%s;" % TEAL if c == 0 and not hd else ""}">{E(t)}</div>')
        bg = YEL if hd else '#FFFFFF'
        out.append(f'<div style="display:flex;background:{bg};border-top:{"0" if r == 0 else "2px solid #DCE4F0"}">{"".join(cells)}</div>')
    return f'<div style="{CARD}overflow:hidden;width:1560px">{"".join(out)}</div>'


def answer_box(text, size=40):
    return f'<div style="background:{YEL};border-radius:20px;padding:16px 28px"><p style="font-size:{size}px;font-weight:800;line-height:1.25">{E(text)}</p></div>'


def say(text):
    return f'<div style="background:{NAVY};color:{CREAM};border-radius:24px;padding:22px 40px;align-self:flex-start"><p style="font-family:{HF};font-size:56px;font-weight:600;line-height:1.2">{E(text)}</p></div>'


def qs_block(d, ids, short):
    qm = qmap(d)
    rows = []
    for i in ids:
        q = qm[i]
        text = q['text']
        parts = ''
        for p in q.get('parts', []):
            if short: continue
            parts += f'<p style="font-size:34px;font-weight:600;color:{MUTED}">{E(p["l"] + ")  " if p["l"] else "")}{blanks_dash(p["text"])}</p>'
        vis = ''
        if q.get('visual'):
            vis = f'<div style="width:340px;flex:none">{svg.render_visual(q["visual"])}</div>'
        rows.append(f'<div style="{CARD}padding:16px 30px;display:flex;gap:26px;align-items:center"><span style="flex:none;background:{YEL};border:3px solid {NAVY};border-radius:6px;padding:2px 16px;font-family:{HF};font-size:36px;font-weight:700">{E(i)}</span>'
                    f'<div style="flex:1;display:flex;flex-direction:column;gap:4px"><p style="font-size:36px;font-weight:700;line-height:1.25">{E(text)}</p>{parts}</div>{vis}</div>')
    return f'<div style="display:flex;flex-direction:column;gap:16px">{"".join(rows)}</div>'


def blanks_dash(t):
    return E(t).replace('___', '______').replace('[]', f'<span style="display:inline-block;width:44px;height:44px;border:3px solid {NAVY};border-radius:10px;background:#fff;vertical-align:middle;margin:0 6px"></span>')


def answers_block(d, ids):
    qm = qmap(d)
    rows = []
    for i in ids:
        q = qm[i]
        rows.append(f'<div style="display:flex;gap:24px;align-items:center"><span style="flex:none;width:120px;text-align:center;background:#FFFFFF;border:3px solid {NAVY};border-radius:6px;padding:8px 0;font-family:{HF};font-size:38px;font-weight:700">{E(i)}</span>'
                    f'<div style="flex:1">{answer_box(q["answer"], 36)}</div></div>')
    return f'<div style="display:flex;flex-direction:column;gap:20px">{"".join(rows)}</div>'


def lookback(d):
    lb = d['look_back']
    def opts(items):
        return ''.join(f'<span style="display:inline-flex;align-items:center;margin-right:30px;white-space:nowrap"><span style="display:inline-block;width:0.8em;height:0.8em;border:3px solid {NAVY};border-radius:8px;background:#fff;margin-right:12px"></span>{E(o)}</span>' for o in items)
    rows = [('Something I did well', '<span style="color:%s">write or draw one thing</span>' % MUTED),
            ('The hardest part was ...', opts(lb['hardest'])),
            ('What helped me', opts(lb['helped'])),
            ('Next time I will try', opts(lb['next'])),
            ('', opts(['I am still stuck (my tutor will come and help)', 'I would like to pass']))]
    inner = ''
    for k, (a, b) in enumerate(rows):
        inner += (f'<div style="display:flex;gap:28px;align-items:center;padding:12px 0;{"border-top:2px solid #DCE4F0;" if k else ""}"><p style="width:430px;flex:none;font-size:32px;font-weight:800;color:{TEAL}">{E(a)}</p>'
                  f'<p style="font-size:27px;font-weight:600;line-height:1.55">{b}</p></div>')
    return chip('Three minutes. There are no right answers. You can pass. Nobody reads it out.', 28) + f'<div style="{CARD}padding:26px 40px;display:flex;flex-direction:column">{inner}</div>'


def render_blocks(d, blocks, cols=1):
    out = []
    for b in blocks:
        t = b['t']
        if t == 'chip': out.append(chip(b['text']))
        elif t == 'p': out.append(para(b['text'], 40 if cols > 1 else 44))
        elif t == 'list': out.append(listing(b['items'], b.get('ordered', False)))
        elif t == 'card': out.append(card(b.get('head'), b['items']))
        elif t == 'visual': out.append(visual(b, cols))
        elif t == 'qs': out.append(qs_block(d, b['ids'], b.get('short', False)))
        elif t == 'answers': out.append(answers_block(d, b['ids']))
        elif t == 'say': out.append(say(b['text']))
        elif t == 'numrow': out.append(numrow(b['items']))
        elif t == 'table': out.append(table(b['rows'], b.get('header', False)))
        elif t == 'answer': out.append(answer_box(b['text']))
        elif t == 'lookback': out.append(lookback(d))
        elif t == 'cols':
            n = len(b['cols'])
            inner = ''.join(f'<div style="flex:1;display:flex;flex-direction:column;gap:16px;align-items:stretch;min-width:0">{render_blocks(d, c, n)}</div>' for c in b['cols'])
            out.append(f'<div style="display:flex;gap:32px;align-items:flex-start">{inner}</div>')
    return ''.join(out)


def slide_html(d, s):
    kind = s['kind']
    time = slide_time(d, s) if not s.get('optional') else 'OPTIONAL'
    if s['kind'] == 'title': time = ''
    dark = kind in ('title', 'dark')
    if dark:
        bg = f'background:linear-gradient(135deg,{NAVY} 0%,#101B33 100%);color:{CREAM}'
        deco = bubbles() if kind == 'title' else bar()
        pill = f'<p style="position:absolute;right:128px;top:64px;font-size:28px;font-weight:700;letter-spacing:2px;color:{YEL}">{time}</p>'
        foot = f'<p style="position:absolute;left:128px;bottom:64px;width:1400px;font-size:24px;color:#B7C3DD">{E(FOOT)}</p>'
    else:
        bg = f'background:{SOFTBG};color:{NAVY}'
        deco = bar()
        pill = f'<p style="position:absolute;right:128px;top:52px;font-size:26px;font-weight:800;letter-spacing:2px;color:{TEAL};background:#FFFFFF;border:2px solid {TEAL};border-radius:999px;padding:6px 22px">{time}</p>'
        foot = f'<p style="position:absolute;left:128px;bottom:48px;width:1400px;font-size:24px;color:#5B6785">{E(FOOT)}</p>'
    if kind == 'title':
        body = (f'<p style="font-size:32px;font-weight:700;letter-spacing:4px;color:{YEL}">LESSON {d["lesson_in_term"]}  •  TERM {d["term"]}  •  LEVEL {d["level"]}</p>'
                f'<h1 style="font-family:{HF};font-size:128px;font-weight:600;line-height:1.05">{E(s["title"])}</h1>'
                f'<p style="font-size:44px;color:#C9D4EC">{E(s.get("subtitle", ""))}</p>'
                + ''.join(f'<div style="background:#26385F;border-radius:24px;padding:40px;max-width:880px;display:flex;flex-direction:column;gap:12px"><p style="font-size:28px;font-weight:700;letter-spacing:3px;color:{YEL}">{E(b["head"])}</p>' + ''.join(f'<p style="font-size:44px;font-weight:600">{E(i)}</p>' for i in b['items']) + '</div>' for b in s['blocks'] if b['t'] == 'card'))
        style = f'{bg};font-family:{BF};padding:128px 128px 160px;display:flex;flex-direction:column;justify-content:center;gap:36px;position:relative;overflow:hidden'
    else:
        if dark:
            h = f'<h2 style="font-family:{HF};font-size:80px;font-weight:600;line-height:1.1;color:{CREAM}">{E(s["title"])}</h2>'
        else:
            h = f'<h2 style="border-left:14px solid {TEAL};padding-left:28px;font-family:{HF};font-size:68px;font-weight:600;line-height:1.1">{E(s["title"])}</h2>'
        inner = render_blocks(d, s['blocks'])
        body = h + inner
        style = f'{bg};font-family:{BF};padding:72px 128px 100px;display:flex;flex-direction:column;gap:22px;position:relative;overflow:hidden'
    mi = s.get('mascot')
    if mi:
        w = 420 if mi['size'] == 'l' else 170
        left = mi.get('side') == 'left'
        edge = 110 if mi['size'] == 'l' else 128
        mbot = 70 if mi['size'] == 'l' else 60
        h = int(w * 834 / 826)
        pos = f'left:{edge}px' if left else f'right:{edge}px'
        bub = ''
        if mi.get('say'):
            bw = 450 if mi['size'] == 'l' else 400
            fs = 34 if mi['size'] == 'l' else 28
            if mi['size'] == 'l':      # above Mi, tail pointing down at Mi's head
                bx = (f'left:{edge + int(w * 0.30)}px' if left else f'right:{edge + 10}px')
                by = f'bottom:{mbot + h + 40}px'
                tail = (f'<svg width="70" height="48" viewBox="0 0 70 48" style="position:absolute;bottom:-44px;{"left" if left else "right"}:70px" xmlns="http://www.w3.org/2000/svg"><path d="M0 0 L70 0 {"L10 48" if left else "L56 48"} Z" fill="#FFFFFF"/></svg>')
            else:                      # beside small Mi, tail pointing sideways at Mi
                bx = (f'left:{edge + w + 36}px' if left else f'right:{edge + w + 36}px')
                by = f'bottom:{mbot + 40}px'
                tail = (f'<svg width="40" height="44" viewBox="0 0 40 44" style="position:absolute;bottom:24px;{"left" if left else "right"}:-34px" xmlns="http://www.w3.org/2000/svg"><path d="{"M40 0 L40 44 L0 30 Z" if left else "M0 0 L0 44 L40 30 Z"}" fill="#FFFFFF"/></svg>')
            bub = (f'<div data-mi-bubble="1" style="position:absolute;{bx};{by};width:{bw}px;background:#FFFFFF;color:{NAVY};border-radius:36px;padding:20px 30px;font-size:{fs}px;font-weight:700;line-height:1.25;text-align:center">{E(mi["say"])}{tail}</div>')
        body += f'{bub}<img data-mi="1" alt="Mi the dolphin" src="{mi_uri()}" style="position:absolute;{pos};bottom:{mbot}px;width:{w}px;height:auto">'
    return (f'<section id="{s["id"]}" data-transition="fade" data-theme="modern2" style="{style}">\n{deco}\n{pill}\n{body}\n{foot}\n<aside>{E(s["note"])}</aside>\n</section>\n')


def build_deck(d, pw=None):
    od = outdir(d, 'deck')
    sl = os.path.join(od, 'project', 'slides')
    os.makedirs(sl, exist_ok=True)
    for f in os.listdir(sl): os.remove(os.path.join(sl, f))
    order = [s['id'] for s in d['slides']]
    html_all = []
    for s in d['slides']:
        h = slide_html(d, s)
        open(os.path.join(sl, s['id'] + '.html'), 'w', encoding='utf-8').write(h)
        html_all.append(h)
    sections = {}
    first = {}
    for i, s in enumerate(d['slides']):
        first.setdefault(s['part'], s['id'])
    for i, (part, sid) in enumerate(first.items(), 1):
        sections[f's{i}'] = {'description': part_map(d)[part]['title'], 'start': sid}
    deck = {'v': 4, 'createdOnFiles': {'v': 1, 'at': '2026-10-22T00:00:00Z'}, 'lists': 'css',
            'title': f"Math Inquirers Level {d['level']} Term {d['term']}: Lesson {d['lesson_in_term']} – {d['title']}",
            'order': order, 'cover': order[0], 'sections': sections,
            'faces': {'fredoka': {'family': 'Fredoka', 'href': 'https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&display=swap'},
                      'nunito-sans': {'family': 'Nunito Sans', 'href': 'https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@400;600;700;800&display=swap'}},
            'designSystems': []}
    json.dump(deck, open(os.path.join(od, 'project', 'deck.json'), 'w'), indent=1)
    # viewing html (all slides, fixed 1920x1080) + pdf
    css = font_css() + '@page{size:1920px 1080px;margin:0}html,body{margin:0;background:#fff}section{width:1920px;height:1080px;box-sizing:border-box;break-after:page;overflow:hidden}aside{display:none}*{box-sizing:border-box}p{margin:0}h1,h2{margin:0}'
    page = f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{E(deck["title"])}</title><style>{css}</style></head><body>{"".join(html_all)}</body></html>'
    hp = os.path.join(od, f"L{d['_num']}_Deck.html")
    open(hp, 'w', encoding='utf-8').write(page)
    problems = []
    if pw:
        pg = pw.new_page(viewport={'width': 1920, 'height': 1080})
        pg.goto('file://' + hp, wait_until='networkidle'); pg.wait_for_timeout(500)
        # overflow check: every non-absolute child must end above y=1030 inside its slide
        res = pg.evaluate("""() => Array.from(document.querySelectorAll('section')).map(s => {
            const top = s.getBoundingClientRect().top; let max = 0, worst = '';
            s.querySelectorAll('*').forEach(e => { const cs = getComputedStyle(e); if (cs.position === 'absolute' || e.closest('aside') || e.closest('[data-deco]') || (e.closest('svg') && e.tagName !== 'svg')) return;
              const r = e.getBoundingClientRect(); const b = r.bottom - top; if (b > max) { max = b; worst = e.tagName; } });
            const right = Math.max(...Array.from(s.querySelectorAll('*')).filter(e => getComputedStyle(e).position !== 'absolute' && !e.closest('svg') && !e.closest('[data-deco]') && !e.closest('aside')).map(e => e.getBoundingClientRect().right - s.getBoundingClientRect().left));
            return {id: s.id, bottom: Math.round(max), right: Math.round(right)}; })""")
        for r in res:
            if r['bottom'] > 1035 or r['right'] > 1800: problems.append(f"slide {r['id']} overflows (bottom {r['bottom']}, right {r['right']})")
        hits = pg.evaluate("""() => { const out = [];
          document.querySelectorAll('section').forEach(sec => { const sr = sec.getBoundingClientRect();
            const bub = sec.querySelector('[data-mi-bubble]'), img = sec.querySelector('img[data-mi]'); if (!img && !sec.querySelector('[data-deco] path')) return;
            const boxes = []; sec.querySelectorAll('[data-deco] path').forEach(pp => boxes.push(['decoration', pp.getBoundingClientRect()])); if (bub) boxes.push(['bubble', bub.getBoundingClientRect()]); if (img) boxes.push(['Mi', img.getBoundingClientRect()]);
            boxes.forEach(([nm, r]) => { if (r.left < sr.left || r.right > sr.right || r.top < sr.top || r.bottom > sr.bottom) out.push(sec.id + ': ' + nm + ' is clipped by the slide edge'); });
            const w = document.createTreeWalker(sec, NodeFilter.SHOW_TEXT);
            while (w.nextNode()) { const n = w.currentNode; if (!n.textContent.trim()) continue; const p = n.parentElement;
              if (p.closest('aside') || p.closest('svg') || (bub && bub.contains(p))) continue;
              const rg = document.createRange(); rg.selectNodeContents(n);
              Array.from(rg.getClientRects()).forEach(t => { boxes.forEach(([nm, r]) => { if (t.width > 2 && t.left < r.right && t.right > r.left && t.top < r.bottom && t.bottom > r.top) out.push(sec.id + ': ' + nm + ' overlaps text "' + n.textContent.trim().slice(0, 30) + '"'); }); }); }
            if (bub && img) { const a = bub.getBoundingClientRect(), c = img.getBoundingClientRect(); if (a.left < c.right && a.right > c.left && a.top < c.bottom - 0.35 * c.height && a.bottom > c.top) out.push(sec.id + ': bubble covers Mi'); } });
          return out; }""")
        problems += ['mascot ' + h for h in hits]
        pg.pdf(path=os.path.join(od, f"L{d['_num']}_Deck.pdf"), width='1920px', height='1080px', print_background=True)
        pg.close()
    return problems
