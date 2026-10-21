"""Placement diagnostic PDF. Usage: python3 diag/build_diag.py p3  (reads diag/content/p3.json; writes outputs/diagnostics/Math_Inquirers_P3_Placement_Check.pdf)
Pages: 1 child sheet intro+foundation, 2 level questions, 3 tutor key + scoring, 4 parent result page."""
import json,sys,os,html
from playwright.sync_api import sync_playwright
E=html.escape
LV=sys.argv[1]; R=os.path.dirname(os.path.abspath(__file__))+'/..'
d=json.load(open(f'{R}/diag/content/{LV}.json'))
NUM=int(LV[1:]); AGE=d['ageName']; SCH={1:'finishing Primary 1',2:'finishing Primary 2',3:'finishing Primary 3',4:'finishing Primary 4',5:'finishing Primary 5',6:'after the PSLE'}[NUM]
DOWN={1:None,2:('P1','Ages 6-8'),3:('P2','Ages 7-9'),4:('P3','Ages 8-10'),5:('P4','Ages 9-11'),6:('P5','Ages 10-12')}[NUM]
UP={1:('P2','Ages 7-9'),2:('P3','Ages 8-10'),3:('P4','Ages 9-11'),4:('P5','Ages 10-12'),5:('P6','Ages 11-13'),6:None}[NUM]
css=open(f'{R}/fonts/fonts.css').read()+'''
@page{size:A4;margin:0}
*{box-sizing:border-box}body{margin:0;font-family:'Nunito Sans',Arial,sans-serif;color:#1B2A49}
.pg{width:210mm;height:297mm;padding:16mm 16mm 14mm;page-break-after:always;position:relative;overflow:hidden}
.bar{position:absolute;left:0;top:0;width:100%;height:6mm;display:flex}.bar i{display:block;height:100%}
h1{font-family:Fredoka,Arial,sans-serif;font-size:26pt;margin:6mm 0 1mm;line-height:1.1}
.kick{font-size:9.5pt;font-weight:800;letter-spacing:.14em;color:#1F7A6F;text-transform:uppercase;margin-top:8mm}
.sub{font-size:11pt;color:#3B4A6B;margin:0 0 4mm}
.name{display:flex;gap:8mm;margin:2mm 0 5mm;font-size:11pt}.name span{flex:1;border-bottom:1.5px solid #1B2A49;padding-bottom:1mm}
.sec{font-family:Fredoka,Arial,sans-serif;font-size:13pt;background:#1B2A49;color:#FFF9EC;border-radius:6px;padding:1.5mm 4mm;margin:4mm 0 3mm;display:inline-block}
.q{display:flex;gap:4mm;margin-bottom:5mm;break-inside:avoid}.n{font-family:Fredoka,Arial,sans-serif;font-size:15pt;color:#D64545;min-width:8mm}
.qt{font-size:12pt;line-height:1.35}.box{margin-top:2mm;border:1.6px solid #1B2A49;border-radius:6px;height:12mm;width:78mm;background:#FBFCFE}
.foot{position:absolute;left:16mm;right:16mm;bottom:7mm;font-size:8pt;color:#5B6785;display:flex;justify-content:space-between}
table{border-collapse:collapse;width:100%;font-size:8.6pt}td,th{border:1px solid #C9D3E6;padding:1mm 2mm;vertical-align:top;text-align:left}th{background:#FFF0C2}
.card{border:2px solid #DCE4F0;border-radius:8px;padding:3.5mm 5mm;margin:3mm 0;background:#F6F8FC}
.rec{display:flex;gap:4mm;margin:3mm 0}.rec div{flex:1;border-radius:8px;padding:3.5mm 4mm;font-size:10.5pt}
.tip{font-size:10pt;color:#3B4A6B}
'''
BAR='<div class="bar"><i style="flex:5;background:#1B2A49"></i><i style="flex:3;background:#1F7A6F"></i><i style="flex:1;background:#FFC93C"></i></div>'
FOOT=lambda t:f'<div class="foot"><span>Math Inquirers {AGE} ({LV.upper()}) placement check</span><span>{t}</span></div>'
items=[('Warm-up',d['foundation']),('Main questions',d['core']),('Brain stretchers',d['stretch'])]
nums={};k=1
for name,L in items:
    for it in L: it['_n']=k;k+=1
def qhtml(L): return ''.join(f'<div class="q"><span class="n">{it["_n"]}</span><div><div class="qt">{E(it["q"])}</div><div class="box"></div></div></div>' for it in L)
P=[]
P.append(f'''<div class="pg">{BAR}<div class="kick">Math Inquirers Placement Check</div><h1>{AGE}</h1><p class="sub">Typically children {SCH}, and open to a year either side  •  About {d["minutes"]} minutes  •  No calculator</p>
<div class="name"><span>Name:</span><span>Date:</span></div>
<div class="card"><b>How it works.</b> Your child answers on their own. Read a question aloud if they ask, but do not help with the maths. If they are stuck, say "Try your best, or skip it", and move on. Write the answer in the box. Working on scrap paper is fine.</div>
<span class="sec">Warm-up</span>{qhtml(d["foundation"])}{FOOT("Page 1")}</div>''')
P.append(f'''<div class="pg">{BAR}<span class="sec" style="margin-top:8mm">Main questions</span>{qhtml(d["core"])}<span class="sec">Brain stretchers</span>{qhtml(d["stretch"])}{FOOT("Page 2")}</div>''')
def rows(L,lab): return ''.join(f'<tr><td>{it["_n"]}</td><td>{E(it["q"])}</td><td><b>{E(it["a"])}</b></td><td>{E(it["work"])}</td></tr>' for it in L)
P.append(f'''<div class="pg">{BAR}<div class="kick">For the tutor or parent</div><h1 style="margin-top:2mm">Answer key and scoring</h1><p class="sub">Accept equivalent forms (for example $2.05 and 2.05). One mark per question.</p>
<span class="sec">Warm-up (4 marks)</span><table><tr><th>#</th><th>Question</th><th>Answer</th><th>Watch for</th></tr>{rows(d["foundation"],"")}</table>
<span class="sec">Main questions (6 marks)</span><table><tr><th>#</th><th>Question</th><th>Answer</th><th>Watch for</th></tr>{rows(d["core"],"")}</table>
<span class="sec">Brain stretchers (2 marks)</span><table><tr><th>#</th><th>Question</th><th>Answer</th><th>Watch for</th></tr>{rows(d["stretch"],"")}</table>
{FOOT("Page 3")}</div>''')
down=f'{DOWN[1]} ({DOWN[0]})' if DOWN else 'a tutor chat and the free taster first'
up=f'{UP[1]} ({UP[0]})' if UP else None
P.append(f'''<div class="pg">{BAR}<div class="kick">Your child's result</div><h1>Which level fits?</h1><p class="sub">Add up the marks, then find your row. This is a guide. You make the final choice, and you can change level free of charge before lesson 1.</p>
<div class="card"><b>Warm-up marks:</b> ______ / 4 &nbsp;&nbsp;&nbsp; <b>Main + stretch marks:</b> ______ / 8</div>
<table><tr><th>Main + stretch</th><th>What it suggests</th></tr>
<tr><td><b>6 to 8</b></td><td>Join <b>{AGE} ({LV.upper()})</b>. Your child has the foundations and will be well challenged.{(" If they scored 8 of 8 and all 4 warm-up marks, you can also try the "+up+" check.") if up else ""}</td></tr>
<tr><td><b>4 or 5</b></td><td>Join <b>{AGE} ({LV.upper()})</b>, and expect some support. If the warm-up score is 2 or less, {down} may be the more comfortable start.</td></tr>
<tr><td><b>0 to 3</b></td><td>We suggest <b>{down}</b>. The ideas build step by step, and a confident start matters more than a fast one.</td></tr></table>
<div class="rec"><div style="background:#E6F4F1"><b>Strong?</b><br>Choose the level that fits the score, not the school year. A child who finds this easy will enjoy the challenge questions in class.</div><div style="background:#FFF0C2"><b>Not yet?</b><br>That is useful to know, not a failure. Starting one level down means more success and more joy in class.</div></div>
<span class="sec">Skills covered</span><p class="tip">{E("; ".join(d["topics"]))}</p>
<div class="card"><b>Next step.</b> Send the score and your preferred level to us when you enrol. Prices are the same at every level, and your tutor can talk it through first. Small groups of up to 8, live online.</div>
{FOOT("Page 4")}</div>''')
html_=f'<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body>{"".join(P)}</body></html>'
os.makedirs(f'{R}/outputs/diagnostics',exist_ok=True)
hp=f'{R}/outputs/diagnostics/_{LV}.html'; open(hp,'w').write(html_)
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page();pg.goto('file://'+os.path.abspath(hp),wait_until='networkidle');pg.wait_for_timeout(600)
    out=f'{R}/outputs/diagnostics/Math_Inquirers_{LV.upper()}_Placement_Check.pdf'
    pg.pdf(path=out,format='A4',print_background=True,margin={'top':'0','bottom':'0','left':'0','right':'0'});b.close()
os.remove(hp); print('built',out)
