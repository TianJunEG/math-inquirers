import os
FONTS=open('../fonts/fonts.css').read()
N='#1B2A49'
def blank(w=46): return f'<span class="bl" style="width:{w}px"></span>'
def numline(col,mark):
    s='<svg viewBox="0 0 680 70" width="100%">'
    s+=f'<line x1="14" y1="30" x2="666" y2="30" stroke="{N}" stroke-width="3"/>'
    for i in range(21):
        x=14+i*32.6
        s+=f'<rect x="{x-13}" y="16" width="26" height="28" rx="{mark}" fill="#fff" stroke="{N}" stroke-width="2"/><text x="{x}" y="36" font-size="13" text-anchor="middle" font-family="Nunito Sans" font-weight="800" fill="{N}">{i}</text>'
    s+='</svg>'; return s
SUB=[('a','Counting in 2s:&nbsp; 2, 4, 6, '+blank()+', '+blank()+', 12, '+blank()+', 16'),
     ('b','Counting in 5s:&nbsp; 5, 10, '+blank()+', 20, '+blank()+', 30, '+blank()),
     ('c','Counting in 3s:&nbsp; 3, 6, '+blank()+', 12, '+blank()+', 18')]
SUB2=[('a','4, 7, 10, 13, '+blank()+', '+blank()+'&emsp;Rule: '+blank(120)),
      ('b','30, 27, 24, 21, '+blank()+', '+blank()+'&emsp;Rule: '+blank(120)),
      ('c','2, 6, 10, 14, '+blank()+', '+blank()+'&emsp;Rule: '+blank(120))]
Q=[(1,'Skip counting. Fill in the blanks.',SUB,''),
   (2,'What is the rule? Fill in the rule and the next two numbers.',SUB2,''),
   (3,'A frog starts at 0 and hops 4 steps each time. Colour the numbers where the frog lands.',[('a','A second frog starts at 0 but hops 5 steps each time. Mark where it lands with a cross (X).'),('b','Besides 0, which number do BOTH frogs land on?&emsp;Answer: '+blank(90))],'NL')]

STYLES={}
# ---------- A: Exercise book ----------
STYLES['A']=dict(name='A · Exercise book',desc='White squared paper like a maths exercise book. Square number tabs, a teal tab for the lesson.',css='''
.page{background:#fff;background-image:linear-gradient(#E6EEF7 1px,transparent 1px),linear-gradient(90deg,#E6EEF7 1px,transparent 1px);background-size:22px 22px}
.hd{display:flex;align-items:stretch;gap:0;margin:-56px -56px 22px;border-bottom:3px solid #1F7A6F}
.hd .tab{background:#1F7A6F;color:#fff;font:600 18px Fredoka;padding:14px 22px}
.hd .top{padding:12px 20px;background:#fff;flex:1}.hd .top small{font:800 12px 'Nunito Sans';letter-spacing:.08em;text-transform:uppercase;color:#1F7A6F}
h1{font:600 38px Fredoka;margin:2px 0 0;color:#1B2A49}
.meta{background:#fff;border:2px solid #1B2A49;padding:8px 12px;margin-bottom:14px}
.qn{background:#1F7A6F;color:#fff;width:32px;height:32px;border-radius:4px;font:600 18px Fredoka}
.q{background:#fff;border:2px solid #1B2A49;padding:14px 16px 10px;margin-bottom:14px}
.sl{font-weight:800;color:#1F7A6F}
.bl{border-bottom:2px solid #1B2A49}
.cover{background:#fff;background-image:linear-gradient(#E6EEF7 1px,transparent 1px),linear-gradient(90deg,#E6EEF7 1px,transparent 1px);background-size:22px 22px}
''',cover='''<div style="margin-top:120px"><div style="display:inline-block;background:#1F7A6F;color:#fff;font:800 14px 'Nunito Sans';letter-spacing:.1em;padding:8px 14px">PRIMARY 1 · HOLIDAY PROGRAM</div>
<h1 style="font:600 96px/0.95 Fredoka;margin:22px 0 0">Math<br><span style="background:linear-gradient(transparent 55%,#FFC93C 55%)">Inquirers</span></h1>
<p style="font:600 28px Fredoka;color:#1F7A6F;margin:18px 0 0">Notice it. Test it. Explain why.</p></div>
<svg viewBox="0 0 680 300" width="100%" style="margin-top:60px">'''+''.join(f'<rect x="{40+i*66}" y="{200-h}" width="50" height="{h}" fill="{c}" stroke="#1B2A49" stroke-width="3"/>' for i,(h,c) in enumerate([(40,'#FFC93C'),(70,'#7CC8F5'),(100,'#3DBE7A'),(130,'#FF7A59'),(160,'#FFC93C'),(190,'#7CC8F5'),(160,'#3DBE7A'),(130,'#FF7A59'),(100,'#FFC93C')]))+'''<line x1="20" y1="202" x2="660" y2="202" stroke="#1B2A49" stroke-width="3"/></svg>
<div style="border:2px solid #1B2A49;background:#fff;padding:14px 18px;margin-top:40px;font:700 18px 'Nunito Sans'">Name: ______________________________ &emsp; Group: __________</div>''',nl=3)
# ---------- B: Colour blocks ----------
STYLES['B']=dict(name='B · Colour blocks',desc='Each question sits on its own soft colour card with a Q1, Q2 flag. Light and friendly, no outlines.',css='''
.page{background:#F7FAFD}
.hd{margin-bottom:18px}.hd .tab{display:inline-block;background:#D6E9FB;color:#1B2A49;font:800 13px 'Nunito Sans';letter-spacing:.08em;text-transform:uppercase;padding:6px 12px;border-radius:8px}
.hd .top small{display:none}
h1{font:600 42px Fredoka;margin:8px 0 0;color:#1B2A49}
.meta{border-radius:12px;background:#fff;padding:10px 14px;margin-bottom:16px;box-shadow:0 2px 0 #E1E8F0}
.q{border-radius:18px;padding:30px 18px 12px;margin:0 0 16px;position:relative}
.q1{background:#E3F0FC}.q2{background:#E2F5EC}.q3{background:#FFEBE3}
.qn{position:absolute;left:16px;top:-12px;background:#1B2A49;color:#fff;border-radius:8px;padding:3px 12px;font:600 16px Fredoka;width:auto;height:auto}
.qn:before{content:"Q"}
.qrow{padding-top:2px}
.sl{font-weight:800;background:#fff;border-radius:6px;padding:0 7px}
.bl{background:#fff;border-radius:6px;height:26px!important;vertical-align:middle}
.cover{background:#E3F0FC}
''',cover='''<svg viewBox="0 0 680 420" width="100%" style="margin-top:20px">'''+''.join(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="18" fill="{c}"/>' for x,y,w,h,c in [(0,0,300,180,'#FFC93C'),(320,0,360,120,'#7CC8F5'),(320,140,170,180,'#3DBE7A'),(510,140,170,280,'#FF7A59'),(0,200,140,220,'#B9A6F2'),(160,200,330,220,'#fff')])+'''<text x="180" y="330" font-family="Fredoka" font-size="64" fill="#1B2A49">2 4 6 ?</text></svg>
<h1 style="font:600 92px/0.95 Fredoka;margin:40px 0 0;color:#1B2A49">Math<br>Inquirers</h1><p style="font:600 26px Fredoka;color:#1F7A6F;margin:16px 0 0">Notice it. Test it. Explain why.</p>
<div style="background:#fff;border-radius:16px;padding:16px 20px;margin-top:40px;font:700 18px 'Nunito Sans'">Name: ______________________________ &emsp; Group: __________</div>''',nl=6)
# ---------- C: Clean classic ----------
STYLES['C']=dict(name='C · Clean and classic',desc='White page, big question numbers in the margin, thin lines between questions. Calm, like a good assessment book.',css='''
.page{background:#fff}
.hd{border-bottom:4px solid #FFC93C;padding-bottom:12px;margin-bottom:16px}.hd .tab{font:800 13px 'Nunito Sans';letter-spacing:.1em;text-transform:uppercase;color:#1F7A6F}
h1{font:600 40px Fredoka;margin:4px 0 0;color:#1B2A49}
.meta{border-bottom:1px solid #C9D3DE;padding:6px 0 12px;margin-bottom:6px}
.q{position:relative;padding:16px 0 12px 62px;border-bottom:1px solid #D7DEE6}
.qn{position:absolute;left:0;top:12px;background:none;color:#1F7A6F;font:600 44px/1 Fredoka;width:auto;height:auto}
.sl{font-weight:800;color:#1F7A6F}
.bl{border-bottom:1.5px solid #1B2A49}
.cover{background:#fff}
''',cover='''<div style="height:26px;background:#FFC93C;margin:-56px -56px 0"></div><div style="margin-top:150px;border-left:8px solid #1F7A6F;padding-left:26px">
<div style="font:800 15px 'Nunito Sans';letter-spacing:.12em;color:#1F7A6F">PRIMARY 1 · HOLIDAY PROGRAM</div><h1 style="font:600 92px/0.95 Fredoka;margin:14px 0 0">Math<br>Inquirers</h1><p style="font:500 26px Fredoka;color:#56637A;margin:16px 0 0">Notice it. Test it. Explain why.</p></div>
<svg viewBox="0 0 680 160" width="100%" style="margin-top:110px"><line x1="20" y1="120" x2="660" y2="120" stroke="#1B2A49" stroke-width="3"/>'''+''.join(f'<line x1="{20+i*64}" y1="112" x2="{20+i*64}" y2="128" stroke="#1B2A49" stroke-width="3"/><text x="{20+i*64}" y="152" font-family="Fredoka" font-size="20" text-anchor="middle" fill="#1B2A49">{i*2}</text>' for i in range(11))+''.join(f'<path d="M{20+i*64} 112 Q{52+i*64} 50 {84+i*64} 112" fill="none" stroke="#FF7A59" stroke-width="3" stroke-dasharray="7 6"/>' for i in range(4))+'''</svg>
<div style="border-top:1.5px solid #1B2A49;margin-top:60px;padding-top:12px;font:700 18px 'Nunito Sans'">Name ________________________________ &emsp; Group __________</div>''',nl=0)
# ---------- D: Sticker labels ----------
STYLES['D']=dict(name='D · Sticker labels',desc='Pale yellow paper, question numbers on tilted tape labels, dashed answer boxes. The most playful.',css='''
.page{background:#FFFBEF}
.hd{margin-bottom:16px}.hd .tab{display:inline-block;background:#FF7A59;color:#1B2A49;font:600 16px Fredoka;padding:4px 14px;transform:rotate(-2deg);border:2px solid #1B2A49}
.hd .top small{display:none}
h1{font:600 44px Fredoka;margin:10px 0 0;color:#1B2A49;text-decoration:underline wavy #FFC93C 4px;text-underline-offset:10px}
.meta{border:2px dashed #1B2A49;border-radius:10px;padding:8px 12px;margin-bottom:16px;background:#fff}
.q{background:#fff;border:2.5px solid #1B2A49;border-radius:6px;padding:28px 16px 10px;margin:0 0 20px;position:relative;box-shadow:4px 4px 0 #1B2A49}
.qn{position:absolute;left:-8px;top:-14px;background:#FFC93C;color:#1B2A49;border:2px solid #1B2A49;font:600 17px Fredoka;width:auto;height:auto;padding:2px 12px;transform:rotate(-4deg);border-radius:2px}
.qn:before{content:"No. "}
.sl{font-weight:800;color:#1B2A49;background:#D6E9FB;padding:0 6px;border-radius:3px}
.bl{border:2px dashed #1B2A49;border-radius:6px;height:26px!important;vertical-align:middle;background:#FFFBEF}
.cover{background:#FFFBEF}
''',cover='''<svg viewBox="0 0 680 360" width="100%" style="margin-top:10px">'''+''.join(f'<g transform="translate({x},{y}) rotate({r})"><{t} fill="{c}" stroke="#1B2A49" stroke-width="3"/></g>' for x,y,r,t,c in [(60,60,-10,'rect x="-40" y="-40" width="80" height="80"','#FFC93C'),(250,90,8,'polygon points="0,-50 50,40 -50,40"','#7CC8F5'),(450,60,-6,'rect x="-70" y="-30" width="140" height="60"','#3DBE7A'),(600,170,12,'rect x="-40" y="-40" width="80" height="80"','#FF7A59'),(120,250,6,'polygon points="0,-46 44,34 -44,34"','#FF7A59'),(370,270,-8,'rect x="-60" y="-35" width="120" height="70"','#B9A6F2')])+'''</svg>
<div style="background:#fff;border:3px solid #1B2A49;box-shadow:6px 6px 0 #1B2A49;padding:26px 30px;transform:rotate(-1.5deg);margin-top:10px"><div style="display:inline-block;background:#FFC93C;border:2px solid #1B2A49;font:600 16px Fredoka;padding:2px 12px;transform:rotate(-3deg)">Primary 1 · Holiday Program</div><h1 style="font:600 88px/0.95 Fredoka;margin:14px 0 0">Math Inquirers</h1><p style="font:600 24px Fredoka;color:#1F7A6F;margin:12px 0 0">Notice it. Test it. Explain why.</p></div>
<div style="border:2px dashed #1B2A49;border-radius:10px;background:#fff;padding:14px 18px;margin-top:60px;font:700 18px 'Nunito Sans'">Name: ______________________________ &emsp; Group: __________</div>''',nl=4)

BASE='''*{box-sizing:border-box}body{margin:0;font-family:'Nunito Sans';color:#1B2A49}
.page{width:794px;height:1123px;padding:56px;position:relative;overflow:hidden;page-break-after:always;font-size:17px;line-height:1.45}
.meta{display:flex;gap:18px;font-weight:800;font-size:14px}.meta span{flex:1;border-bottom:1.5px solid #1B2A49}
.intro{margin:0 0 14px;font-size:16px}
.q{display:block}.qtop{display:flex;gap:12px;align-items:flex-start;font-weight:800;margin-bottom:8px}
.qn{flex:none;display:inline-flex;align-items:center;justify-content:center}
.sub{display:flex;gap:10px;margin:7px 0 7px 4px;align-items:baseline}
.bl{display:inline-block;height:20px;vertical-align:bottom}
.ft{position:absolute;left:56px;right:56px;bottom:26px;font-size:11px;color:#6B7890;display:flex;justify-content:space-between}
'''
def lesson(st):
    h='<div class="page"><div class="hd"><div class="tab">Lesson 1</div><div class="top"><small>Whole numbers · Number patterns</small><h1>Count with the Frog!</h1></div></div>'
    h+='<div class="meta">Name <span></span> Group <span style="flex:.4"></span> Date <span style="flex:.5"></span></div><p class="intro">Look for the pattern. Fill in the missing numbers.</p>'
    for n,t,subs,x in Q:
        h+=f'<div class="q q{n}"><div class="qtop"><span class="qn">{n}</span><span>{t}</span></div>'
        if x=='NL': h+='<div style="margin:4px 0 8px">'+numline('#fff',st['nl'])+'</div>'
        for l,s in subs: h+=f'<div class="sub"><span class="sl">{l}</span><span>{s}</span></div>'
        h+='</div>'
    h+='<div class="ft"><span>Math Inquirers Holiday Program</span><span>Page 3</span></div></div>'
    return h
os.makedirs('out',exist_ok=True)
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':794,'height':1123})
    allpages=[]
    for k,st in STYLES.items():
        body=f'<div class="page cover">{st["cover"]}</div>'+lesson(st)
        html=f'<html><head><meta charset="utf-8"><style>{FONTS}{BASE}{st["css"]}</style></head><body>{body}</body></html>'
        open(f'out/{k}.html','w').write(html); allpages.append((k,html))
        pg.goto('file://'+os.path.abspath(f'out/{k}.html'));pg.wait_for_timeout(250)
        pg.pdf(path=f'out/{k}.pdf',width='794px',height='1123px',print_background=True)
        for i,el in enumerate(pg.query_selector_all('.page')): el.screenshot(path=f'out/{k}{i}.png')
    b.close()
# comparison sheet
from PIL import Image,ImageDraw,ImageFont
sc=0.42;W=int(794*sc);H=int(1123*sc);pad=30
try: f=ImageFont.truetype('../fonts/node_modules/@fontsource/fredoka/files/fredoka-latin-600-normal.woff2',26)
except Exception: f=None
sheet=Image.new('RGB',(4*(2*W+20)+5*pad,H+120),'#EEF5FB');d=ImageDraw.Draw(sheet)
for j,(k,st) in enumerate(STYLES.items()):
    x0=pad+j*(2*W+20+pad)
    for i in range(2):
        im=Image.open(f'out/{k}{i}.png').resize((W,H));sheet.paste(im,(x0+i*(W+20),90))
    d.text((x0,30),st['name'],fill='#1B2A49',font=ImageFont.truetype('/usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf',28))
sheet.save('Workbook_Style_Options.png')
import subprocess
subprocess.run(['qpdf','--empty','--pages']+[f'out/{k}.pdf' for k in STYLES]+['--','Workbook_Style_Options.pdf'],check=True)
print('done',sheet.size)
