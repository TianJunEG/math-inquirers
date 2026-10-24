"""Placement diagnostic PDF. Usage: python3 diag/build_diag.py p3  (reads diag/content/p3.json; writes outputs/diagnostics/Math_Inquirers_P3_Placement_Check.pdf)
Child sheet (3 pages: warm-up, main+stretch, parent result) plus a separate tutor key PDF.
Placement rule printed here = docs/levels_and_placement.md: score = warm-up + main questions, out of 10 (Brain stretchers are a bonus, not counted).
70% or more (7-10) enrol; 40-69% (4-6) enrol with a support note or one level down; under 40% (0-3) one level down; 90%+ (9-10) may try the check one level up.
Level 1 (no level below): the under-40% advice is the free taster and a tutor chat. Content json holds level, ageName, minutes, foundation, core, stretch, topics and the optional text fields childNote (printed on the child sheet) and tutorKey (printed on the Tutor Key)."""
import json,sys,os,html
from playwright.sync_api import sync_playwright
E=html.escape
LV=sys.argv[1]; R=os.path.dirname(os.path.abspath(__file__))+'/..'
d=json.load(open(f'{R}/diag/content/{LV}.json'))
NUM=int(LV[1:]); AGE=d['ageName']; SCH={1:'Builds on Primary 1 maths',2:'Builds on Primary 2 maths',3:'Builds on Primary 3 maths',4:'Builds on Primary 4 maths',5:'Builds on Primary 5 maths',6:'For children after the PSLE'}[NUM]
DOWN={1:None,2:('Level 1','Ages 6-8'),3:('Level 2','Ages 7-9'),4:('Level 3','Ages 8-10'),5:('Level 4','Ages 9-11'),6:('Level 5','Ages 10-12')}[NUM]
UP={1:('Level 2','Ages 7-9'),2:('Level 3','Ages 8-10'),3:('Level 4','Ages 9-11'),4:('Level 5','Ages 10-12'),5:('Level 6','Ages 11-13'),6:None}[NUM]
css=open(f'{R}/fonts/fonts.css').read()+'''
@page{size:A4;margin:0}
*{box-sizing:border-box}body{margin:0;font-family:'Nunito Sans',Arial,sans-serif;color:#1B2A49}
.pg{width:210mm;height:297mm;padding:12mm 16mm 14mm;page-break-after:always;position:relative;overflow:hidden}
.bar{position:absolute;left:0;top:0;width:100%;height:6mm;display:flex}.bar i{display:block;height:100%}
h1{font-family:Fredoka,Arial,sans-serif;font-size:26pt;margin:6mm 0 1mm;line-height:1.1}
.kick{font-size:9.5pt;font-weight:800;letter-spacing:.14em;color:#1F7A6F;text-transform:uppercase;margin-top:8mm}
.sub{font-size:11pt;color:#3B4A6B;margin:0 0 4mm}
.name{display:flex;gap:8mm;margin:2mm 0 5mm;font-size:11pt}.name span{flex:1;border-bottom:1.5px solid #1B2A49;padding-bottom:1mm}
.sec{font-family:Fredoka,Arial,sans-serif;font-size:13pt;background:#1B2A49;color:#FFF9EC;border-radius:6px;padding:1.5mm 4mm;margin:3mm 0 2.5mm;display:inline-block}
.q{display:flex;gap:4mm;margin-bottom:3mm;break-inside:avoid}.n{font-family:Fredoka,Arial,sans-serif;font-size:15pt;color:#D64545;min-width:8mm}
.qt{font-size:12pt;line-height:1.35}.box{margin-top:2mm;border:1.6px solid #1B2A49;border-radius:6px;height:9.5mm;width:78mm;background:#FBFCFE}
.foot{position:absolute;left:16mm;right:16mm;bottom:7mm;font-size:8pt;color:#5B6785;display:flex;justify-content:space-between}
table{border-collapse:collapse;width:100%;font-size:8.6pt}td,th{border:1px solid #C9D3E6;padding:1mm 2mm;vertical-align:top;text-align:left}th{background:#FFF0C2}
.card{border:2px solid #DCE4F0;border-radius:8px;padding:3.5mm 5mm;margin:3mm 0;background:#F6F8FC}
.rec{display:flex;gap:4mm;margin:3mm 0}.rec div{flex:1;border-radius:8px;padding:3.5mm 4mm;font-size:10.5pt}
.nt{font-size:8pt;color:#5B6785;margin-left:auto;white-space:nowrap;align-self:flex-end}.nt i{display:inline-block;width:3.5mm;height:3.5mm;border:1.3px solid #5B6785;border-radius:2px;vertical-align:middle;margin-right:1.5mm}
.tip{font-size:10pt;color:#3B4A6B}
'''
BAR='<div class="bar"><i style="flex:5;background:#1B2A49"></i><i style="flex:3;background:#1F7A6F"></i><i style="flex:1;background:#FFC93C"></i></div>'
FOOT=lambda t:f'<div class="foot"><span>Math Inquirers Level {NUM} placement check ({AGE})</span><span>{t}</span></div>'
items=[('Warm-up',d['foundation']),('Main questions',d['core']),('Brain stretchers',d['stretch'])]
nums={};k=1
for name,L in items:
    for it in L: it['_n']=k;k+=1

def visual(it):
    v=it.get('visual')
    if not v: return ''
    if v['type']=='dotgraph':
        rows=v['rows'];h=len(rows)*8+2
        o=f'<svg width="210" height="{int(210*h/65)}" viewBox="0 0 65 {h}" style="margin:2mm 0">'
        for i,(n,c) in enumerate(rows):
            y=5+i*8;o+=f'<text x="1" y="{y+1.5}" font-size="3.6" fill="#1B2A49">{E(n)}</text>'
            for j in range(c): o+=f'<circle cx="{24+j*6}" cy="{y}" r="2.3" fill="#D64545"/>'
        return o+'</svg>'
    if v['type']=='ruler':
        a,b=v['from'],v['to'];W=10*(b-a)+20
        o=f'<svg width="240" height="62" viewBox="0 0 {W} 30" style="margin:2mm 0"><rect x="5" y="12" width="{W-10}" height="14" fill="#FFF0C2" stroke="#1B2A49" stroke-width=".5"/>'
        for k in range(a,b+1):
            x=10+(k-a)*10;o+=f'<line x1="{x}" y1="12" x2="{x}" y2="19" stroke="#1B2A49" stroke-width=".5"/><text x="{x}" y="25" font-size="4" text-anchor="middle">{k}</text>'
        x1=10+(v['pencilStart']-a)*10;x2=10+(v['pencilEnd']-a)*10
        return o+f'<rect x="{x1}" y="3" width="{x2-x1}" height="6" fill="#FFC93C" stroke="#1B2A49" stroke-width=".5"/><polygon points="{x2},3 {x2+4},6 {x2},9" fill="#E8B4A0" stroke="#1B2A49" stroke-width=".5"/></svg>'
    return ''
def qhtml(L): return ''.join(f'<div class="q"><span class="n">{it["_n"]}</span><div><div class="qt">{E(it["q"])}</div>{visual(it)}<div class="box"></div></div><span class="nt"><i></i>not learnt yet</span></div>' for it in L)
P=[]
P.append(f'''<div class="pg">{BAR}<div class="kick">Math Inquirers Placement Check</div><h1>{AGE}</h1><p class="sub">{SCH}. Free placement check for this level  •  About {d["minutes"]} minutes  •  No calculator</p>
<div class="name"><span>Name or username:</span><span>Age:</span><span>Date:</span></div>
<div class="card"><b>How it works.</b> This is a friendly check, not a test. Your child answers on their own. {E(d.get("childNote") or "Read a question aloud if they ask, but do not help with the maths.")} If they are stuck, say "Try your best, or skip it". Working on scrap paper is fine.<br><b>Not learnt it yet?</b> Some questions may use ideas your child has not met at school. That is fine and useful to know. Tick "not learnt yet" and move on.</div>
<span class="sec">Warm-up</span>{qhtml(d["foundation"])}{FOOT("Page 1")}</div>''')
P.append(f'''<div class="pg">{BAR}<span class="sec" style="margin-top:2mm">Main questions</span>{qhtml(d["core"])}<span class="sec">Brain stretchers</span><p class="tip" style="margin:0 0 3mm">Optional. These are meant to be tricky, and most children will not finish them. Have a go at any that look fun.</p>{qhtml(d["stretch"])}{FOOT("Page 2")}</div>''')
def rows(L): return ''.join(f'<tr><td>{it["_n"]}</td><td>{E(it["q"])}</td><td><b>{E(it["a"])}</b></td><td>{E(it["work"])}</td></tr>' for it in L)
T=lambda t,L:f'<span class="sec">{t}</span><table><tr><th>#</th><th>Question</th><th>Answer</th><th>Watch for</th></tr>{rows(L)}</table>'
EQ='for example 70 cents and 70c' if NUM==1 else 'for example 70 cents and 70c, or 3/4 and three quarters'
TK=f'<p class="tip"><b>Tutor note.</b> {E(d["tutorKey"])}</p>' if d.get('tutorKey') else ''
KEY=f'''<div class="pg" style="height:auto;min-height:297mm;padding-top:9mm;padding-bottom:6mm">{BAR}<div class="kick">For the tutor or parent</div><h1 style="margin-top:2mm">Answer key: {AGE}</h1><p class="sub">Accept equivalent forms ({EQ}). One mark per question. Add the warm-up and main marks to get a score out of 10; the Brain stretchers are a bonus and are not counted. Keep this key away from the child until they have finished.</p>
{T("Warm-up (4 marks)",d["foundation"])}{T("Main questions (6 marks)",d["core"])}{T("Brain stretchers (bonus, not counted)",d["stretch"])}
{TK}<p class="tip">Questions the child ticked "not learnt yet" score 0 but tell you what to teach first. They do not count against the child.</p></div>'''
down=f'{DOWN[1]} ({DOWN[0]})' if DOWN else None
up=f'{UP[1]} ({UP[0]})' if UP else None
mid=(f'Join <b>{AGE} (Level {NUM})</b> and we will note that your child may need some support, or choose <b>{down}</b>.' if down else
     f'Join <b>{AGE} (Level {NUM})</b> and we will note that your child may need some support. A short tutor chat and the free taster lesson will show what helps.')
low=(f'We suggest <b>{down}</b>. Ideas build step by step, and a confident start matters more than a fast one.' if down else
     'We suggest the <b>free taster and a chat with a tutor</b> first. Ideas build step by step, and a confident start matters more than a fast one.')
top=f'Join <b>{AGE} (Level {NUM})</b>. Your child has the foundations and will enjoy the thinking.'
easy=(f'<tr><td><b>Also, 9 or 10</b> (90% or more)</td><td>That was easy. Your child may also try the <b>{up}</b> check, as well as joining {AGE}.</td></tr>' if up else
      '<tr><td><b>Also, 9 or 10</b> (90% or more)</td><td>That was easy. Every level has open investigations and Go further questions for children who want more.</td></tr>')
P.append(f'''<div class="pg">{BAR}<div class="kick">Your child's result</div><h1>Which level fits?</h1><p class="sub">Mark the answers with the key (ask us for it, or use the tutor key). Add the warm-up and main marks to get a score out of 10. The Brain stretchers are a bonus and are not counted. This is a guide. You make the final choice, and you can change level free of charge before lesson 1.</p>
<div class="card"><b>Warm-up:</b> ____ / 4 &nbsp;&nbsp; <b>Main questions:</b> ____ / 6 &nbsp;&nbsp; <b>Score (warm-up + main):</b> ____ / 10 &nbsp;&nbsp; <b>Brain stretchers (bonus):</b> ____ / 2 &nbsp;&nbsp; <b>Ticked "not learnt yet":</b> ____</div>
<table><tr><th>Score out of 10</th><th>What it suggests</th></tr>
<tr><td><b>7 to 10</b> (70% or more)</td><td>{top}</td></tr>
<tr><td><b>4 to 6</b> (40-69%)</td><td>{mid}</td></tr>
<tr><td><b>0 to 3</b> (under 40%)</td><td>{low} If many questions were ticked "not learnt yet", that simply means the topics have not been taught yet.</td></tr>{easy}</table>
<div class="rec"><div style="background:#E6F4F1"><b>Finding it easy?</b><br>{("Try the "+up+" check as well if the score is 9 or 10. ") if up else ""}Every level has open investigations for children who want more.</div><div style="background:#FFF0C2"><b>Found it hard?</b><br>That is useful to know, and it says nothing about how clever your child is. A level that feels comfortable builds confidence, and you can change level free of charge before lesson 1.</div></div>
<span class="sec">Skills covered</span><p class="tip">{E("; ".join(d["topics"]))}</p>
<div class="card"><b>Next step.</b> Send us the scores and your preferred level when you enrol. Prices are the same at every level, and a tutor can talk it through first. Small groups of up to 8, live online.</div>
{FOOT("Page 3")}</div>''')
def pdf(body,out,h=None):
    htm=f'<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body>{body}</body></html>'
    hp=out+'.html';open(hp,'w').write(htm)
    with sync_playwright() as p:
        b=p.chromium.launch();pg=b.new_page();pg.goto('file://'+os.path.abspath(hp),wait_until='networkidle');pg.wait_for_timeout(600)
        pg.pdf(path=out,format='A4',print_background=True,margin={'top':'0','bottom':'0','left':'0','right':'0'});b.close()
    os.remove(hp);print('built',out)
os.makedirs(f'{R}/outputs/diagnostics',exist_ok=True)
base=f'{R}/outputs/diagnostics/Math_Inquirers_{"Level"+str(NUM)}_'
pdf(''.join(P),base+'Placement_Check.pdf'); pdf(KEY,base+'Tutor_Key.pdf')
