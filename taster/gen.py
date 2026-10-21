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
CSS=open('../hp/parent_style.css').read()+"""
@page{size:A4;margin:0}
.page{width:794px;height:1123px;position:relative;overflow:hidden;break-after:page;background:#fff;padding:52px 56px}
.page .cover{height:100%}
.q{grid-template-columns:30px 1fr;margin-bottom:16px}
.q .txt{font-size:17px;font-weight:600;margin-bottom:6px}
.rl{margin-top:8px;font-size:16px;font-weight:700;color:#1F7A6F}
.two{display:grid;grid-template-columns:1fr 1fr;gap:20px}
.line{border-bottom:1.5px solid #B9C7DA;height:28px}
.intro{font-size:16.5px;color:#3B4A6B;margin:-6px 0 14px}
.foot{position:absolute;left:56px;right:56px;bottom:22px;font-size:11px;color:#5B6785;display:flex;justify-content:space-between;border-top:1px solid #D5DDEA;padding-top:6px}
.rc{display:grid;grid-template-columns:1fr 1fr;gap:14px}
.rc div{background:#F3F6FA;border-top:5px solid #1F7A6F;padding:12px 14px}
.rc b{font-family:'Fredoka',Arial,sans-serif;font-weight:600;color:#D64545;font-size:24px;margin-right:8px}
.rc h3{display:inline;font-size:19px}
.rc p{margin:6px 0 0;font-size:15px}
"""
def foot(n,dark=False): return f'<div class="foot"><span>Free taster  •  Math Inquirers  •  Parent edition</span><span>{n}</span></div>'
def head(num,topic,title,kick='Free taster  •  Puzzles to try at home'):
    return f'<div class="kick">{kick}</div><div class="hd"><div class="big">{num}</div><div><div class="tp">{topic}</div><h1>{title}</h1></div></div>'
def lv(t): return f'<div class="lv">{t}</div>'
def rule_cards():
    items=[('1','Notice it','What repeats? What changes?'),('2','Test it','Try it with coins, buttons or spoons.'),('3','Check it','Does your answer make sense?'),('4','Explain why','Say how you know.')]
    return '<div class="rc">'+''.join(f'<div><b>{a}</b><h3>{b}</h3><p>{c}</p></div>' for a,b,c in items)+'</div>'
def Q(n,text,svg='',extra=''):
    return f'<div class="q"><span class="n">{n}</span><div><div class="txt">{text}</div>{svg}{extra}</div></div>'
def cover_art():
    b='';pts=[(80,330),(240,250),(400,300),(560,190),(720,240)]
    for i,(x,y) in enumerate(pts[:-1]): b+=ARC(x,pts[i+1][0],y-34,50,'+3',TEAL)
    for i,(x,y) in enumerate(pts): b+=R(x-42,y-34,84,84,[YEL,'#DDEBF7',YEL,'#DDEBF7',YEL][i],NAVY,4,6)+T(x,y+22,str([3,6,9,12,15][i]),40)
    b+=R(668,330,92,92,'#FFFFFF',NAVY,4,6,True)+T(714,390,'?',48,'#D64545')
    return SVG(800,440,b,'width:100%')
RL='<div class="rl">The rule is: ____________________</div>'
pages=[]
pages.append(f'''<div class="page"><div class="cover"><div class="kick">Free taster  •  For parents and Primary 1 children</div>
<div class="ctitle">Think Like a<br><span>Mathematician</span></div>
<div class="lede">Six puzzles to try at home. About 10 minutes each. No shopping needed.</div>
<div class="rule"></div><div>{cover_art()}</div>
<div class="bottom"><div class="slogan">Notice it. Test it. Explain why.</div><div class="by">From the Math Inquirers Holiday Program<br>Preciouslyours Pte Ltd</div></div></div></div>''')
pages.append(f'''<div class="page">{head('00','Before you start','Four rules for every puzzle')}{rule_cards()}
<div class="lv" style="margin-top:26px">How to help (for grown-ups)</div>
<ol class="tips">
<li><div><b>Ask before you tell.</b> Start with "What do you notice?"</div></li>
<li><div><b>Use real things.</b> Coins, buttons, spoons or pasta make numbers easy to see.</div></li>
<li><div><b>Stuck?</b> Look again. Try it with objects. Try a smaller example. Say the answer last.</div></li>
<li><div><b>Ask "How do you know?"</b> even when the answer is right.</div></li>
<li><div><b>Praise the thinking,</b> not the cleverness: "I like how you checked that."</div></li>
<li><div><b>Keep it short.</b> Stop while it is still fun.</div></li></ol>
<div class="quote">Hard question? Great! Mathematicians get stuck all the time. That is when thinking happens.</div>
{foot(2)}</div>''')
pages.append(f'''<div class="page">{head('01','Puzzle set 1  •  Patterns','Frog Jumps')}
<p class="intro">Find the rule, then write the next two numbers. Try it with a number line, or hop a coin along the table.</p>
{lv('Core')}
{Q(1,'4, 7, 10, 13, __, __ <span style="color:#1F7A6F">What is the rule?</span>',seq([4,7,10,13,'',''],arcs=['+?','+?','+?']),RL)}
{Q(2,'5, 10, 15, 20, __, __',seq([5,10,15,20,'','']),RL)}
{Q(3,'1, 5, 9, 13, __, __',seq([1,5,9,13,'','']),RL)}
{foot(3)}</div>''')
pages.append(f'''<div class="page">{head('01','Puzzle set 1  •  Patterns','Frog Jumps: think harder')}
{lv('Think Harder')}
{Q(4,'3, 8, __, 18, __, 28',seq([3,8,'',18,'',28]))}
{Q(5,'40, __, 28, __, 16, 10',seq([40,'',28,'',16,10]))}
{lv('Challenge  (only if it is fun)')}
{Q(6,'<b>Frog A</b> jumps in 3s from 0. <b>Frog B</b> jumps in 4s from 0. Which numbers up to 40 do <b>both</b> frogs land on? (Do not count 0.)',frogline(),'<div class="line"></div>')}
<div class="quote">Explain why: how do you know you found them all?</div>
<div class="panel"><h3>Try it with objects</h3><p style="margin:0">Line up 40 pasta pieces. Put a coin on every 3rd piece, and a button on every 4th. Where do the coin and the button sit together?</p></div>
{foot(4)}</div>''')
pages.append(f'''<div class="page">{head('02','Puzzle set 2  •  Number bonds','Making 10')}
<p class="intro">Put 10 buttons or counters in two groups to help you.</p>
{lv('Core')}
<div class="two">{Q(1,'10 = 3 + __',tenframe(3,250))}{Q(2,'10 = __ + 8',tenframe(8,250))}</div>
{Q(3,'10 = 6 + __',tenframe(6,250))}
{lv('Think Harder: keep it balanced')}
<div class="two">{Q(4,'5 + 4 = 6 + __',balance())}{Q(5,'8 + 2 = 7 + __','<p style="font-size:15px;color:#3B4A6B;margin:6px 0 0">Both sides must be the same. Check by working out each side.</p>')}</div>
{foot(5)}</div>''')
pages.append(f'''<div class="page">{head('02','Puzzle set 2  •  Number bonds','The magic triangle')}
{lv('Challenge')}
{Q(6,'Put <b>1, 2, 3, 4, 5, 6</b> in the spaces so that <b>each side adds to 9</b>. The corners are 1, 2 and 3. What goes in the middle of each side?','<div style="text-align:center">'+triangle()+'</div>')}
<div class="quote">Explain why: how do you know each side adds to 9?</div>
<div class="panel"><h3>Try it with objects</h3><p style="margin:0">Write 1 to 6 on six bits of paper. Move them around until every side makes 9.</p></div>
{foot(6)}</div>''')
A1=['16, 19. Add 3.','25, 30. Add 5.','17, 21. Add 4.','13 and 23. Add 5.','34 and 22. Take away 6.','12, 24 and 36. Both frogs land there because we say 12 when counting in 3s and in 4s. After that it happens every 12.']
A2=['7','2','4','3 (5 + 4 = 9, 6 + 3 = 9)','3 (8 + 2 = 10, 7 + 3 = 10)','Between 1 and 2: 6. Between 2 and 3: 4. Between 3 and 1: 5. Each side adds to 9.']
blk=lambda t,a:f'<div class="ablk"><h3>{t}</h3>'+''.join(f'<div class="ar"><b>{i+1}</b><span>{x}</span></div>' for i,x in enumerate(a))+'</div>'
pages.append(f'''<div class="page">{head('✓','Look only after you have tried','Answers')}
<p class="intro">A different way of thinking is fine, as long as you can explain it.</p>
<div class="acols">{blk('Set 1: Frog Jumps',A1)}{blk('Set 2: Making 10',A2)}</div>
{foot(7)}</div>''')
pages.append(f'''<div class="page">{head('+','Keep thinking','Want more?')}
<div class="panel"><h3>Weekly Dose of Thinking Math</h3><p style="margin:0">Join our free list. Each week you get a new set of puzzles and a five-minute "explain why" question for the dinner table.</p><p style="margin:8px 0 0;font-weight:700;color:#1F7A6F">[Sign-up link or QR code]</p></div>
<div class="panel"><h3>Math Inquirers Holiday Program</h3><p style="margin:0">Ten 90-minute lessons over five weeks, live online in small groups of up to 8 children. Hands-on puzzles, a printed workbook posted to your home with a cut-out kit, a stamped Inquiry Journal and a certificate.</p><p style="margin:8px 0 0;font-weight:700;color:#1F7A6F">[Dates, fee and sign-up link]</p></div>
<div class="panel" style="border-top-color:#FFC93C"><h3 style="color:#1B2A49">Questions?</h3><p style="margin:0;font-weight:700">[Name, email or phone]</p></div>
<p style="font-size:12px;color:#5B6785;margin-top:26px">Math Inquirers is enrichment for thinking skills. It does not promise exam results and is not affiliated with the Ministry of Education or the Gifted Education Programme. We will only email you if you sign up, and you can unsubscribe at any time. Preciouslyours Pte Ltd, Singapore.</p>
{foot(8)}</div>''')
html='<!doctype html><html><head><meta charset="utf-8"><style>'+open('../fonts/fonts.css').read()+CSS+'</style></head><body>'+''.join(pages)+'</body></html>'
open('taster.html','w').write(html)
