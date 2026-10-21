# Parent practice pack in the A+D workbook style, built from qbank.json and lessons.js titles.
# Run in hp/:  python3 parent_pack.py   ->  Math_Inquirers_Parent_Practice_Pack.pdf
import json, html, os, subprocess
from playwright.sync_api import sync_playwright
E = html.escape
Q = json.load(open('qbank.json'))
# lesson titles and topics from lessons.js
info = json.loads(subprocess.run(['node', '-e', "const L=require('./lessons.js');console.log(JSON.stringify(L.lessons.map(l=>({n:l.n,title:l.title,topic:l.topic}))))"],
                                 capture_output=True, text=True, check=True).stdout)
PICK = {'core': 4, 'stretch': 3, 'challenge': 2}
LEVEL = {'core': 'Core', 'stretch': 'Think Harder', 'challenge': 'Challenge  (for strong thinkers)'}

def qbox(n, text, lines=2):
    ln = ''.join('<div class="ln"></div>' for _ in range(lines))
    return f'<div class="qwrap"><div class="qbox"><div class="p q kn"><span class="qn">{n}</span><span class="qt">{E(text)}</span></div>{ln}</div></div>'

B = []
# ---- cover and how-to page
shapes = ('<svg viewBox="0 0 680 230" width="100%" aria-label="shapes">'
          '<g transform="translate(80,70) rotate(-10)"><rect x="-38" y="-38" width="76" height="76" fill="#FFC93C" stroke="#1B2A49" stroke-width="4"/></g>'
          '<polygon points="250,30 300,120 200,120" fill="#1F7A6F" stroke="#1B2A49" stroke-width="4"/>'
          '<g transform="translate(420,80) rotate(8)"><rect x="-60" y="-30" width="120" height="60" fill="#DDEBF7" stroke="#1B2A49" stroke-width="4"/></g>'
          '<polygon points="590,40 640,90 590,140 540,90" fill="#D64545" stroke="#1B2A49" stroke-width="4"/>'
          '<g transform="translate(160,185) rotate(6)"><rect x="-50" y="-22" width="100" height="44" fill="#FFF9EC" stroke="#1B2A49" stroke-width="4"/></g>'
          '<polygon points="470,160 520,215 420,215" fill="#FFC93C" stroke="#1B2A49" stroke-width="4"/></svg>')
B.append(f'<div class="p">{shapes}</div>')
B.append('<div class="p lh"><span class="lbadge">For parents</span><span class="ltopic">Primary 1  •  Math Inquirers Holiday Program</span></div>')
B.append('<div class="p ltitle" style="font-size:48px">PRACTICE AT HOME</div>')
B.append('<div class="p" style="font-size:19px;margin-bottom:14px">Extra questions for every lesson, with answers at the back. <b>Notice it. Test it. Explain why.</b></div>')
B.append('<div class="banner kn">How to help</div>')
tips = ['Ask before you tell. Start with "What do you notice?" and let your child answer first.',
        'Use things you have at home: coins, notes, buttons, spoons, pasta, building blocks. Try it with objects before writing.',
        'If your child is stuck, give hints in three steps: look again, try it with objects, then try a smaller example. Say the answer last.',
        'Ask "How do you know?" even when the answer is right. The reason matters as much as the answer.',
        'Praise the thinking: "I like how you checked that." Avoid "You are clever".',
        'Keep it short. Ten minutes, two or three questions, is enough. Stop while it is still fun.',
        'Answers are at the back. Please look only after your child has tried.']
B.append('<div class="qbox" style="padding-top:14px">' + ''.join(f'<div class="p q"><span class="qn" style="position:static;transform:none">{i+1}</span><span class="qt" style="font-weight:500">{E(t)}</span></div>' for i, t in enumerate(tips)) + '</div>')
B.append('<div class="banner kn">The three levels</div>')
B.append('<div class="qbox" style="padding-top:14px"><div class="p" style="font-weight:500"><b>Core</b> is for everyone. <b>Think Harder</b> stretches the idea. '
         '<b>Challenge</b> is for strong thinkers, and it is fine to leave it for another day. Every question has space to draw or write how your child knows.</div></div>')

# ---- one section per lesson
for L in info:
    n = str(L['n']); b = Q[n]
    B.append(f'<div class="p lh pb"><span class="lbadge">Lesson {L["n"]}</span><span class="ltopic">{E(L["topic"])}</span></div>')
    B.append(f'<div class="p ltitle">{E(L["title"].upper())}</div>')
    k = 1
    for lev, cnt in PICK.items():
        B.append(f'<div class="banner kn">{LEVEL[lev]}</div>')
        for item in b[lev][:cnt]:
            B.append(qbox(k, item['q'], 2 if lev == 'core' else 3)); k += 1
    B.append('<div class="p" style="margin-top:10px;font-weight:700;color:#1F7A6F">Explain why: how do you know your answer is right?</div><div class="ln"></div>')

# ---- answers
B.append('<div class="p lh pb"><span class="lbadge">Answers</span><span class="ltopic">Look after your child has tried</span></div>')
B.append('<div class="p ltitle">ANSWERS</div>')
for L in info:
    n = str(L['n']); b = Q[n]; k = 1; rows = []
    for lev, cnt in PICK.items():
        for item in b[lev][:cnt]:
            rows.append(f'<div class="ar"><span class="an">{k}</span><span>{E(item["a"])}</span></div>'); k += 1
    B.append(f'<div class="abox"><div class="ah">Lesson {L["n"]}: {E(L["title"])}</div>{"".join(rows)}</div>')

css = open('../fonts/fonts.css').read() + open('wb_style.css').read() + '''
.qbox .qn{position:absolute}
.abox{background:#fff;border:2px solid #1B2A49;border-radius:4px;box-shadow:3px 3px 0 #1B2A49;padding:10px 14px;margin:0 4px 12px;break-inside:avoid;font-family:'Nunito Sans',sans-serif;font-size:14px}
.ah{font-family:Fredoka,sans-serif;font-weight:600;font-size:17px;color:#1F7A6F;margin-bottom:4px}
.ar{display:flex;gap:8px;padding:2px 0;border-top:1px dashed #C9D2E3}
.an{flex:none;width:22px;font-weight:800;color:#1B2A49}
'''
doc = f'<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body>{chr(10).join(B)}</body></html>'
open('parent_pack.html', 'w').write(doc)
foot = '<div style="width:100%;font-size:9px;color:#5B6785;padding:0 14mm;display:flex;justify-content:space-between;font-family:Arial"><span>Math Inquirers Holiday Program  •  Practice at Home</span><span>Page <span class="pageNumber"></span></span></div>'
with sync_playwright() as p:
    br = p.chromium.launch(); pg = br.new_page()
    pg.goto('file://' + os.path.abspath('parent_pack.html'), wait_until='networkidle'); pg.wait_for_timeout(800)
    pg.pdf(path='Math_Inquirers_Parent_Practice_Pack.pdf', format='A4', print_background=True, display_header_footer=True,
           header_template='<div></div>', footer_template=foot, margin={'top': '14mm', 'bottom': '16mm', 'left': '14mm', 'right': '14mm'})
    br.close()
os.remove('parent_pack.html')
print('parent pack built')
