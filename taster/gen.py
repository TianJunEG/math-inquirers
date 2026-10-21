import sys
sys.path.insert(0,'../diag')
from lib import *
def seq(vals,w=620,rule=True,arcs=None):
    n=len(vals);bw=64;gap=(w-n*bw)/(n-1) if n>1 else 0;b=''
    for i,v in enumerate(vals):
        x=i*(bw+gap);blank=(v=='')
        b+=R(x+3,38,bw,bw,WHITE if blank else YEL,NAVY,3,14,blank)+(T(x+3+bw/2,82,str(v),32) if not blank else '')
    if arcs:
        for i,l in enumerate(arcs):
            x1=i*(bw+gap)+3+bw/2;x2=(i+1)*(bw+gap)+3+bw/2
            b+=ARC(x1,x2,34,26,l,TEAL)
    return SVG(w+8,112,b,'width:100%%;max-width:%dpx'%(w+8))
def tenframe(a,w=330):
    b='';
    for r in range(2):
        for c in range(5):
            x=4+c*60;y=4+r*60;b+=R(x,y,60,60,WHITE,NAVY,3,0)
            i=r*5+c
            if i<a: b+=C(x+30,y+30,22,RED,NAVY,3)
    return SVG(308,128,b,'width:%dpx'%w)
def balance():
    b=L(210,170,210,60,NAVY,6)+L(60,70,360,70,NAVY,6)+PG([(170,185),(250,185),(210,150)],NAVY,NAVY)
    b+=R(60,76,130,60,'#FFF4D1',NAVY,3,10)+T(125,116,'5 + 4',30)
    b+=R(230,76,130,60,'#FFF4D1',NAVY,3,10)+T(295,116,'6 + ?',30)
    return SVG(420,200,b,'width:300px')
def triangle():
    A=(160,30);Bp=(40,230);Cp=(280,230)
    b=PG([A,Bp,Cp],WHITE,NAVY,4)
    pos=[(A,'1'),(Bp,'2'),(Cp,'3'),(((A[0]+Bp[0])/2,(A[1]+Bp[1])/2),'?'),(((A[0]+Cp[0])/2,(A[1]+Cp[1])/2),'?'),(((Bp[0]+Cp[0])/2,230),'?')]
    for (x,y),t in pos: b+=C(x,y,26,YEL if t!='?' else WHITE,NAVY,3,dash=(t=='?'))+T(x,y+10,t,28)
    return SVG(320,262,b,'width:400px')
def frogline():
    k=18;b=L(10,70,10+40*k,70,NAVY,4)
    for n in range(0,41,4): b+=L(10+n*k,60,10+n*k,80)+T(10+n*k,104,str(n),18)
    for n in range(3,41,3): b+=C(10+n*k,38,8,TEAL,TEAL,1)
    for n in range(4,41,4): b+=C(10+n*k,38-0,0.1,NAVY)
    for n in range(4,41,4): b+=T(10+n*k,142,'●',16,'#C9971F')
    b+=C(30,10,7,TEAL,TEAL,1)+T(44,16,'Frog A (3s)',15,anchor='start')+C(180,10,6,'#C9971F','#C9971F',1)+T(194,16,'Frog B (4s)',15,anchor='start')
    return SVG(740,150,b,'width:100%')
def frog(x,y,s=1):
    return f'<g transform="translate({x},{y}) scale({s})">'+C(0,0,60,TEAL,NAVY,4)+C(-24,-52,20,WHITE,NAVY,4)+C(24,-52,20,WHITE,NAVY,4)+C(-24,-52,8,NAVY,NAVY,1)+C(24,-52,8,NAVY,NAVY,1)+f'<path d="M-30,12 Q0,44 30,12" fill="none" stroke="{NAVY}" stroke-width="5"/></g>'
def cover_art():
    b=''
    k=1
    pts=[(80,420),(240,330),(400,380),(560,260),(720,320)]
    for i,(x,y) in enumerate(pts[:-1]): b+=ARC(x,pts[i+1][0],y+0,60,'+%d'%(i+1+0),YEL).replace(f'M{x},{y}',f'M{x},{y}')
    for i,(x,y) in enumerate(pts): b+=C(x,y+30,34,YEL,NAVY,4)+T(x,y+42,str([3,6,9,12,15][i]),30)
    b+=frog(560,150,1.0)
    return SVG(800,500,b,'width:100%')
CSS='''
@page{size:A4;margin:0}
*{box-sizing:border-box}
body{margin:0;font-family:'Fredoka','Inter',Arial,sans-serif;color:#1B2A49}
.page{width:794px;height:1123px;position:relative;overflow:hidden;page-break-after:always;background:#EAF3FB;padding:56px 56px}
.navy{background:#1B2A49;color:#FFF9EC}
h1{font-size:64px;line-height:1.02;margin:0;font-weight:700}
h2{font-size:34px;margin:0 0 14px;font-weight:700}
h3{font-size:22px;margin:0 0 6px}
p{font-size:18px;line-height:1.4;margin:0 0 10px}
.badge{display:inline-block;background:#FFC93C;color:#1B2A49;border-radius:999px;padding:10px 26px;font-weight:700;font-size:22px}
.card{background:#fff;border-radius:24px;padding:20px 24px;box-shadow:0 3px 0 #E5E9F2}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:18px}
.ribbon{background:#1F7A6F;color:#FFF9EC;border-radius:16px;padding:10px 22px;font-size:26px;font-weight:700;display:flex;justify-content:space-between;align-items:center;margin-bottom:18px}
.q{background:#fff;border-radius:20px;padding:14px 20px;margin-bottom:12px;box-shadow:0 3px 0 #E5E9F2}
.q .n{display:inline-flex;width:34px;height:34px;border-radius:50%;background:#FFC93C;align-items:center;justify-content:center;font-weight:700;margin-right:10px}
.q p{margin:0 0 6px;font-size:19px;font-weight:600}
.star{background:#FFC93C;border-radius:16px;padding:12px 20px}
.bubble{background:#fff;border:3px solid #1F7A6F;border-radius:24px;padding:12px 20px;font-size:18px;font-weight:600;color:#1F7A6F}
.foot{position:absolute;left:56px;right:56px;bottom:24px;font-size:13px;color:#5B6785;display:flex;justify-content:space-between}
.navy .foot{color:#C9D4EC}
.ans{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.ans div{background:#fff;border-radius:16px;padding:10px 16px;font-size:17px}
.line{border-bottom:3px dotted #8A94AD;height:30px}
'''
def foot(n,dark=False): return f'<div class="foot"><span>Math Inquirers  •  Notice it. Test it. Explain why.</span><span>{n}</span></div>'
def rule_cards():
    items=[('1','Notice it','What repeats? What changes?'),('2','Test it','Try it with coins, buttons or spoons.'),('3','Check it','Does your answer make sense?'),('4','Explain why','Say how you know.')]
    return '<div class="grid">'+''.join(f'<div class="card"><div style="display:flex;gap:12px;align-items:center"><div style="width:48px;height:48px;border-radius:50%;background:#FFC93C;display:flex;align-items:center;justify-content:center;font-size:26px;font-weight:700">{a}</div><div><h3>{b}</h3><p style="margin:0;font-size:16px">{c}</p></div></div></div>' for a,b,c in items)+'</div>'
def Q(n,text,svg='',extra=''):
    return f'<div class="q"><p><span class="n">{n}</span>{text}</p>{svg}{extra}</div>'
pages=[]
# cover
pages.append(f'''<div class="page navy" style="padding:64px 60px"><span class="badge">FREE TASTER • PRIMARY 1</span>
<h1 style="margin-top:26px;font-size:76px">Think Like a<br><span style="color:#FFC93C">Mathematician</span></h1>
<p style="font-size:24px;margin-top:20px;color:#C9D4EC">Six puzzles to try at home. About 10 minutes each. No shopping needed.</p>
<div style="margin-top:20px">{cover_art()}</div>
<div style="position:absolute;left:60px;bottom:64px;font-size:30px;font-weight:700;color:#FFC93C">Notice it. Test it. Explain why.</div>
<div class="foot" style="color:#C9D4EC"><span>From the Math Inquirers Holiday Program</span><span>Preciouslyours Pte Ltd</span></div></div>''')
# rules + how to help
pages.append(f'''<div class="page"><h2>Four rules for every puzzle</h2>{rule_cards()}
<h2 style="margin-top:30px">How to help (for grown-ups)</h2>
<div class="card" style="font-size:18px;line-height:1.5">
<p><b>Ask before you tell.</b> Start with "What do you notice?"</p>
<p><b>Use real things.</b> Coins, buttons, spoons or pasta make numbers easy to see.</p>
<p><b>Stuck?</b> Look again. Try it with objects. Try a smaller example. Say the answer last.</p>
<p><b>Ask "How do you know?"</b> even when the answer is right.</p>
<p><b>Praise the thinking,</b> not the cleverness: "I like how you checked that."</p>
<p style="margin:0"><b>Keep it short.</b> Stop while it is still fun.</p></div>
<div style="margin-top:26px" class="bubble">Hard question? Great! Mathematicians get stuck all the time. That is when thinking happens.</div>
{foot(2)}</div>''')
# set 1
pages.append(f'''<div class="page"><div class="ribbon"><span>Puzzle set 1: Frog Jumps</span><span style="font-size:20px">Patterns</span></div>
<p style="font-size:20px;color:#3B4A6B">Find the rule, then write the next two numbers. Try it with a number line, or hop a coin along the table.</p>
{Q(1,'4, 7, 10, 13, __, __ <span style="color:#1F7A6F">What is the rule?</span>',seq([4,7,10,13,'',''],arcs=['+?','+?','+?']),'<div style="margin-top:8px;font-size:18px;font-weight:700;color:#1F7A6F">The rule is: ____________________</div>')}
{Q(2,'5, 10, 15, 20, __, __',seq([5,10,15,20,'','']),'<div style="margin-top:8px;font-size:18px;font-weight:700;color:#1F7A6F">The rule is: ____________________</div>')}
{Q(3,'1, 5, 9, 13, __, __',seq([1,5,9,13,'','']),'<div style="margin-top:8px;font-size:18px;font-weight:700;color:#1F7A6F">The rule is: ____________________</div>')}
{foot(3)}</div>''')
pages.append(f'''<div class="page"><div class="ribbon" style="background:#FFC93C;color:#1B2A49"><span>Think harder</span><span style="font-size:20px">Fill the gaps</span></div>
{Q(4,'3, 8, __, 18, __, 28',seq([3,8,'',18,'',28]))}
{Q(5,'40, __, 28, __, 16, 10',seq([40,'',28,'',16,10]))}
<div class="ribbon" style="background:#D64545;margin-top:26px">★ Challenge ★ <span style="font-size:18px">only if it is fun</span></div>
{Q(6,'<b>Frog A</b> jumps in 3s from 0. <b>Frog B</b> jumps in 4s from 0. Which numbers up to 40 do <b>both</b> frogs land on? (Do not count 0.)',frogline(),'<div class="line"></div>')}
<div class="bubble" style="margin-top:20px">Explain why: How do you know you found them all?</div>
<div class="card" style="margin-top:22px"><h3>Try it with objects</h3><p style="margin:0">Line up 40 pasta pieces. Put a coin on every 3rd piece, and a button on every 4th. Where do the coin and the button sit together?</p></div>
{foot(4)}</div>''')
# set 2
pages.append(f'''<div class="page"><div class="ribbon"><span>Puzzle set 2: Number Bonds</span><span style="font-size:20px">Making 10</span></div>
<p style="font-size:17px;color:#3B4A6B">Put 10 buttons or counters in two groups to help you.</p>
<div class="grid">
{Q(1,'10 = 3 + __',tenframe(3,260))}
{Q(2,'10 = __ + 8',tenframe(8,260))}
</div>
{Q(3,'10 = 6 + __',tenframe(6,260))}
<div class="ribbon" style="background:#FFC93C;color:#1B2A49;margin-top:14px"><span>Think harder</span><span style="font-size:20px">Keep it balanced</span></div>
<div class="grid">
{Q(4,'5 + 4 = 6 + __',balance())}
{Q(5,'8 + 2 = 7 + __','<div style="height:10px"></div>'+'<p style="font-size:16px;color:#3B4A6B;margin-top:8px">Both sides must be the same. Check by working out each side.</p>')}
</div>
{foot(5)}</div>''')
pages.append(f'''<div class="page"><div class="ribbon" style="background:#D64545">★ Challenge ★ <span style="font-size:18px">Magic triangle</span></div>
<div class="q"><p><span class="n">6</span>Put <b>1, 2, 3, 4, 5, 6</b> in the circles so that <b>each side adds to 9</b>. The corners are 1, 2 and 3. What goes in the middle of each side?</p>
<div style="text-align:center">{triangle()}</div></div>
<div class="bubble" style="margin-top:20px">Explain why: How do you know each side adds to 9?</div>
<div class="card" style="margin-top:22px"><h3>Try it with objects</h3><p style="margin:0">Write 1 to 6 on six bits of paper. Move them around until every side makes 9.</p></div>
{foot(6)}</div>''')
# answers
pages.append(f'''<div class="page navy"><h2 style="color:#FFC93C">Answers</h2><p style="color:#C9D4EC">Look only after you have tried. A different way of thinking is fine, as long as you can explain it.</p>
<div class="ans" style="color:#1B2A49">
<div><b>Set 1</b></div><div><b>Set 2</b></div>
<div>1. 16, 19. Add 3.</div><div>1. 7</div>
<div>2. 25, 30. Add 5.</div><div>2. 2</div>
<div>3. 17, 21. Add 4.</div><div>3. 4</div>
<div>4. 13 and 23. Add 5.</div><div>4. 3 (5 + 4 = 9, 6 + 3 = 9)</div>
<div>5. 34 and 22. Take away 6.</div><div>5. 3 (8 + 2 = 10, 7 + 3 = 10)</div>
<div>6. 12, 24 and 36. Both frogs land there because 12 is in the 3s and the 4s. Then it repeats every 12.</div><div>6. Between 1 and 2: 6. Between 2 and 3: 4. Between 3 and 1: 5. Each side adds to 9.</div></div>
{foot(7)}</div>''')
# more
pages.append(f'''<div class="page"><h2>Want more?</h2>
<div class="card" style="margin-bottom:18px"><h3>Free weekly puzzles</h3><p style="margin:0">Join our free list. Each week you get a new set of puzzles and a five-minute "explain why" question for the dinner table.</p><p style="margin:8px 0 0;font-weight:700;color:#1F7A6F">[Sign-up link or QR code]</p></div>
<div class="card" style="margin-bottom:18px"><h3>Math Inquirers Holiday Program</h3><p style="margin:0">Ten 90-minute lessons over five weeks, in small groups of up to 8 children. Face to face or online. Hands-on puzzles, a printed workbook with a cut-out kit, a stamped Inquiry Journal and a certificate.</p><p style="margin:8px 0 0;font-weight:700;color:#1F7A6F">[Dates, fee and sign-up link]</p></div>
<div class="star"><p style="margin:0;font-weight:700;font-size:20px">Questions? [Name, email or phone]</p></div>
<p style="font-size:13px;color:#5B6785;margin-top:30px">Math Inquirers is enrichment for thinking skills. It does not promise exam results and is not affiliated with the Ministry of Education or the Gifted Education Programme. We will only email you if you sign up, and you can unsubscribe at any time. Preciouslyours Pte Ltd, Singapore.</p>
{foot(8)}</div>''')
html='<!doctype html><html><head><meta charset="utf-8"><style>'+open('../fonts/fonts.css').read()+CSS+'</style></head><body>'+''.join(pages)+'</body></html>'
open('taster.html','w').write(html)
