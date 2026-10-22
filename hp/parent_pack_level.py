# Weekly Dose of Thinking Math: the parent practice pack, parent edition style (B, "Magazine"; see parent_style.css). Built from qbank.json and lessons.js.
# Level version: run in hp/:  python3 parent_pack_level.py p2   ->  ../p2/Math_Inquirers_Level2_Weekly_Dose_of_Thinking_Math.pdf
# Needs ../pN/data.js and ../pN/parent_side.json ({"1":[learns, tip, ask], ...}).
import json, html, os, subprocess, sys
from playwright.sync_api import sync_playwright
E = html.escape
LV = sys.argv[1]; D = os.path.abspath(os.path.join('..', LV)); NUM = LV[1:]
data = json.loads(subprocess.run(['node', '-e', "const L=require(process.argv[1]);console.log(JSON.stringify({q:L.qbank,info:L.lessons.map(l=>({n:l.n,title:l.title,topic:l.topic}))}))", os.path.join(D, 'data.js')],
                                 capture_output=True, text=True, check=True).stdout)
Q = data['q']; info = data['info']
REAL = ('Paper, a pencil and, for coding lessons, a computer with Scratch (free at scratch.mit.edu). Let your child show you the program and explain what each block does.' if NUM == '6' else 'Coins, notes, cups, string, paper strips or blocks. Try it with objects or a drawing before writing.')
LEVELNAME = 'Level 6: Maths and coding bridge' if NUM == '6' else 'Level ' + NUM
PICK = {'core': 4, 'stretch': 3, 'challenge': 2}
LEVEL = {'core': 'Start here', 'stretch': 'Think harder', 'challenge': 'Go further'}
# per lesson: what your child learns, a tip for the parent, a question to ask
SIDE = {int(k): v for k, v in json.load(open(os.path.join(D, 'parent_side.json'))).items()}

def q(n, text, lines):
    return f'<div class="q"><span class="n">{n}</span><div>{E(text)}' + '<div class="ln"></div>' * lines + '</div></div>'

shapes = ('<svg viewBox="0 0 680 210" width="100%" aria-label="Shapes">'
          '<g transform="translate(70,80) rotate(-10)"><rect x="-44" y="-44" width="88" height="88" fill="#FFC93C" stroke="#1B2A49" stroke-width="4"/></g>'
          '<polygon points="230,30 290,140 170,140" fill="#1F7A6F" stroke="#1B2A49" stroke-width="4"/>'
          '<g transform="translate(420,90) rotate(8)"><rect x="-70" y="-34" width="140" height="68" fill="#DDEBF7" stroke="#1B2A49" stroke-width="4"/></g>'
          '<polygon points="600,30 655,90 600,150 545,90" fill="#D64545" stroke="#1B2A49" stroke-width="4"/></svg>')
B = []
B.append(f'''<div class="cover"><div class="kick">For parents  •  {'Level 6, after the PSLE' if NUM == '6' else 'Level ' + NUM + ' holiday program'}</div>
<div class="ctitle">Weekly Dose of<br><span>Thinking Math</span></div>
<div class="lede">One dose a week for five weeks: short sets of questions for every Math Inquirers lesson, a tip for you, and the answers at the back.</div>
<div class="rule"></div>{shapes}
<div class="bottom"><div class="slogan">Notice it. Test it. Explain why.</div><div class="by">Math Inquirers Holiday Program<br>Preciouslyours Pte Ltd</div></div></div>''')
B.append(f'''<div class="pb"><div class="kick">Before you start</div><div class="hd"><div class="big">00</div><div><div class="tp">For grown-ups</div><h1>How to help</h1></div></div>
<ol class="tips">
<li><div><b>Ask before you tell.</b> Start with "What do you notice?" and let your child answer first.</div></li>
<li><div><b>Use real things.</b> {REAL}</div></li>
<li><div><b>Give hints in three steps.</b> Look again. Try it with objects. Try a smaller example. Say the answer last.</div></li>
<li><div><b>Ask "How do you know?"</b> even when the answer is right. The reason matters as much as the answer.</div></li>
<li><div><b>Praise the thinking.</b> "I like how you checked that" works better than "You are clever".</div></li>
<li><div><b>Keep it short.</b> Ten minutes and two or three questions is enough. Stop while it is still fun.</div></li>
<li><div><b>Answers are at the back.</b> Look only after your child has tried.</div></li>
</ol>
<div class="quote">Hard question? Great. Getting stuck is where the thinking happens.</div>
<div class="panel"><h3>One dose a week</h3><p style="margin:0">Each week has two lessons and about 18 questions. Do two or three a day, Monday to Friday, and keep the weekend for the Go further questions if your child enjoys them.</p></div>
<div class="panel"><h3>The three levels</h3><p style="margin:0"><b>Start here</b> is for everyone. <b>Think harder</b> stretches the idea. <b>Go further</b> and the <b>Investigation</b> are for when your child wants more, and it is fine to leave them for another day.</p></div>
<div class="panel"><h3>What your child is doing in class</h3><p style="margin:0">Ten 90-minute live online lessons over five weeks, in small groups. Each lesson starts with a hands-on puzzle, then a short teaching part, then the workbook. These pages practise the same ideas at home.</p></div></div>''')
for L in info:
    n = L['n']; b = Q[str(n)]; learn, tip, ask = SIDE[n]
    h = f'<div class="pb"><div class="kick">Weekly Dose of Thinking Math  •  Week {(n+1)//2}</div><div class="hd"><div class="big">W{(n+1)//2}</div><div><div class="tp">Lesson {n}  •  {E(L["topic"])}</div><h1>{E(L["title"])}</h1></div></div><div class="cols"><div>'
    k = 1
    for lev, cnt in PICK.items():
        h += f'<div class="lv">{LEVEL[lev]}</div>'
        for item in b[lev][:cnt]:
            h += q(k, item['q'], 2 if lev == 'core' else 3); k += 1
    h += f'</div><div class="side"><h3>What your child learns</h3><p>{E(learn)}</p><h3>Tip for you</h3><p>{E(tip)}</p><h3>Ask</h3><p>{E(ask)}</p></div></div></div>'
    B.append(h)
h = '<div class="pb"><div class="kick">Look after your child has tried</div><div class="hd"><div class="big">✓</div><div><div class="tp">All lessons</div><h1>Answers</h1></div></div><div class="acols">'
for L in info:
    b = Q[str(L['n'])]; k = 1; rows = ''
    for lev, cnt in PICK.items():
        for item in b[lev][:cnt]:
            rows += f'<div class="ar"><b>{k}</b><span>{E(item["a"])}</span></div>'; k += 1
    h += f'<div class="ablk"><h3>Week {(L["n"]+1)//2}  •  Lesson {L["n"]}: {E(L["title"])}</h3>{rows}</div>'
B.append(h + '</div></div>')

css = open('../fonts/fonts.css').read() + open('parent_style.css').read()
HT = os.path.join(D, 'parent_pack.html')
open(HT, 'w').write(f'<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body>{chr(10).join(B)}</body></html>')
foot = f'<div style="width:100%;font-size:9px;color:#5B6785;padding:0 16mm;display:flex;justify-content:space-between;font-family:Arial"><span>Weekly Dose of Thinking Math  •  Math Inquirers {LEVELNAME}</span><span>Page <span class="pageNumber"></span></span></div>'
with sync_playwright() as p:
    br = p.chromium.launch(); pg = br.new_page()
    pg.goto('file://' + HT, wait_until='networkidle'); pg.wait_for_timeout(800)
    pg.pdf(path=os.path.join(D, f'Math_Inquirers_Level{NUM}_Weekly_Dose_of_Thinking_Math.pdf'), format='A4', print_background=True, display_header_footer=True,
           header_template='<div></div>', footer_template=foot, margin={'top': '16mm', 'bottom': '18mm', 'left': '16mm', 'right': '16mm'})
    br.close()
os.remove(HT)
print('weekly dose built')
