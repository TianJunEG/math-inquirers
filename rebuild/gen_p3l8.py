"""Math Inquirers P3 – Lesson 8: Angle and Line Detectives. Writes split/p3l8/project (deck.json + slides/*.html)."""
import json,os,sys,math,datetime
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,H)
from slidekit import *
D=os.path.join(H,'..','split','p3l8','project'); S={}
def put(i,h): S[i]=h
RED='#D64545'; LG='#B9C6DE'; PFX='p3l8-'
FOOT3='Math Inquirers P3 Holiday Program  •  Notice it. Test it. Explain why.'

# ---------- small SVG helpers (navy strokes, yellow/sky fills, Fredoka text) ----------
def SV(w,h,body,label): return f'<svg aria-label="{E(label)}" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="width:{w}px;height:{h}px">{body}</svg>'
def R(x,y,w,h,fill=WHITE,stroke=NAVY,sw=4,rx=0,extra=''): return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{extra}/>'
def T(x,y,s,size=36,fill=NAVY,weight=700,anchor='middle'): return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" fill="{fill}" font-family="Fredoka, Arial">{E(str(s))}</text>'
def PG(pts,fill=WHITE,stroke=NAVY,sw=5,extra=''): return f'<polygon points="{" ".join(f"{a:.1f},{b:.1f}" for a,b in pts)}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="miter"{extra}/>'
def LN(x1,y1,x2,y2,col=NAVY,sw=4,dash=''): return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{col}" stroke-width="{sw}"{f" stroke-dasharray={chr(34)}{dash}{chr(34)}" if dash else ""} stroke-linecap="round"/>'
def ARW(x1,y1,x2,y2,col=TEAL,sw=7,hs=20):
    L=math.hypot(x2-x1,y2-y1); ux,uy=(x2-x1)/L,(y2-y1)/L; bx,by=x2-ux*hs,y2-uy*hs; px,py=-uy*hs*0.6,ux*hs*0.6
    return LN(x1,y1,bx,by,col,sw)+f'<polygon points="{x2:.1f},{y2:.1f} {bx+px:.1f},{by+py:.1f} {bx-px:.1f},{by-py:.1f}" fill="{col}"/>'
def bgrid(x,y,cols,rows,c,col=LG,sw=2):
    d=''.join(f'M{x+i*c} {y}V{y+rows*c}' for i in range(cols+1))+''.join(f'M{x} {y+j*c}H{x+cols*c}' for j in range(rows+1))
    return f'<path d="{d}" stroke="{col}" stroke-width="{sw}" fill="none"/>'
def cellsfig(cells,x0,y0,c,fill=SKY,sw=6,inner=True):
    has=set(cells); r=''; d=''
    for a,b in cells:
        x=x0+a*c; y=y0+b*c
        r+=R(x,y,c,c,fill,NAVY if inner else fill,2 if inner else 0)
        if (a,b-1) not in has: d+=f'M{x} {y}H{x+c}'
        if (a,b+1) not in has: d+=f'M{x} {y+c}H{x+c}'
        if (a-1,b) not in has: d+=f'M{x} {y}V{y+c}'
        if (a+1,b) not in has: d+=f'M{x+c} {y}V{y+c}'
    return r+f'<path d="{d}" stroke="{NAVY}" stroke-width="{sw}" stroke-linecap="square" fill="none"/>'
def ostep(left,top,n,text,ov=None,ovw=0,ovh=0,dx=0,dy=0,tw=1000,size=34,extra='',row=False,twt=None,build='fade'):
    """One click = overlay marks (same left/top as the base picture) + the step text box beside it."""
    lab=f'<span style="color:{TEAL};font-weight:800">Step {n}.</span>  ' if n else ''
    ws=f'width:{twt}px;flex:none;' if row and twt else ''
    tx=f'<p style="{ws}font-size:{size}px;font-weight:600;line-height:1.3">{lab}{E(text)}</p>'
    inner=f'<div style="display:flex;align-items:center;gap:24px">{tx}{extra}</div>' if row else tx+extra
    box=f'<div style="margin-top:{dy}px;width:{tw}px;box-sizing:border-box;background:{WHITE};border-radius:20px;padding:16px 28px;display:flex;flex-direction:column;gap:10px;flex:none">{inner}</div>'
    if ov is None and ovw==0: return pin(left+dx,top+dy,tw,box.replace(f'margin-top:{dy}px;',''),build)
    o=f'<div style="width:{ovw}px;height:{ovh}px;flex:none">{ov or ""}</div>'
    return pin(left,top,dx+tw,f'<div style="display:flex;align-items:flex-start;gap:{dx-ovw}px">{o}{box}</div>',build)
def soft(left,top,width,text,size=34,build='fade'): return pin(left,top,width-56,p(text,size,700),build,SOFT,20,'18px 28px')
def stitle(t,size=34): return p(t,size,600,MUTED)
def foot(h): return h.replace(E(FOOT),E(FOOT3))
def S_(sid,time,body,notes,dark=False): return foot(sec(sid,time,body,notes,dark))
def checkrows(sid,time,title,rows,notes,lw=210,size=34,gap=118,top=250):
    body=h2(title)
    for i,(a,b) in enumerate(rows):
        t=top+i*gap
        body+=pin(128,t,lw-20,f'<p style="font-size:34px;font-weight:800;color:{TEAL}">{E(a)}</p>',None,WHITE,20,'16px 22px')
        body+=pin(128+lw,t,1664-lw,f'<p style="font-size:{size}px;font-weight:800;line-height:1.25">{E(b)}</p>','pop',YEL,20,'16px 24px')
    return S_(sid,time,body,notes)
def preview(sid,time,title,items,tip,notes):
    inner=''.join(p(f'<span style="color:{TEAL};font-weight:800">{E(a)}</span>  {E(b)}',36,600,raw=True) for a,b in items)
    return S_(sid,time,h2(title)+card(inner)+card(p(tip,34,600,MUTED)),notes)
def cards_slide(sid,time,title,items,notes,size=38,chip_=None):
    inner=''.join(card((chip(chip_) if (chip_ and i==0) else '')+p(f'<span style="color:{TEAL}">{E(a)}</span>  {E(b)}',size,600,raw=True)) for i,(a,b) in enumerate(items))
    return S_(sid,time,h2(title)+inner,notes)
def title_slide(sid,top,title,topic,today,notes):
    return (f'<section id="{sid}" data-transition="fade" style="background:{NAVY};color:{CREAM};font-family:{BF};padding:128px 128px 160px;display:flex;flex-direction:column;justify-content:center;gap:36px">\n'
            f'<p style="font-size:32px;font-weight:700;letter-spacing:4px;color:{YEL}">{E(top)}</p>\n'
            f'<h1 style="font-family:{HF};font-size:128px;font-weight:600;line-height:1.05">{E(title)}</h1>\n'
            f'<p style="font-size:44px;color:#C9D4EC">{E(topic)}</p>\n'
            f'<div style="background:#26385F;border-radius:24px;padding:40px;display:flex;flex-direction:column;gap:12px"><p style="font-size:28px;font-weight:700;letter-spacing:3px;color:{YEL}">TODAY WE WILL</p><p style="font-size:44px;font-weight:600">{E(today)}</p></div>\n'
            f'<p style="position:absolute;left:128px;bottom:64px;width:1400px;font-size:24px;color:#B7C3DD">{E(FOOT3)}</p>\n<aside>{E(notes)}</aside>\n</section>\n')
def break_slide(sid,time,big,small,notes):
    return (f'<section id="{sid}" data-transition="fade" style="background:{TEAL};color:{CREAM};font-family:{BF};padding:128px 128px 160px;display:flex;flex-direction:column;justify-content:center;gap:36px">\n'
            f'<p style="font-size:32px;font-weight:700;letter-spacing:4px;color:{YEL}">{E(time)}</p>\n'
            f'<h2 style="font-family:{HF};font-size:110px;font-weight:600;line-height:1.05">Brain break</h2>\n'
            f'<p style="font-size:48px;font-weight:600">{E(big)}</p>\n<p style="font-size:36px;color:#D7EFEA">{E(small)}</p>\n'
            f'<p style="position:absolute;left:128px;bottom:64px;width:1400px;font-size:24px;color:#D7EFEA">{E(FOOT3)}</p>\n<aside>{E(notes)}</aside>\n</section>\n')


# ---------- angle helpers ----------
def pt(v,deg,L): return (v[0]+L*math.cos(math.radians(deg)), v[1]-L*math.sin(math.radians(deg)))
def arc(v,d1,d2,r,col=TEAL,sw=5):
    a=pt(v,d1,r); b=pt(v,d2,r); large=1 if (d2-d1)%360>180 else 0
    return f'<path d="M{a[0]:.1f} {a[1]:.1f} A{r} {r} 0 {large} 0 {b[0]:.1f} {b[1]:.1f}" fill="none" stroke="{col}" stroke-width="{sw}"/>'
def ray(v,deg,L,col=NAVY,sw=6): b=pt(v,deg,L); return LN(v[0],v[1],round(b[0],1),round(b[1],1),col,sw)
def sector(v,d1,d2,r,fill=YEL): a=pt(v,d1,r); b=pt(v,d2,r); return f'<path d="M{v[0]} {v[1]} L{a[0]:.1f} {a[1]:.1f} A{r} {r} 0 0 0 {b[0]:.1f} {b[1]:.1f} Z" fill="{fill}" stroke="{TEAL}" stroke-width="3"/>'
def rmark(v,a,b,s=26,col=TEAL,sw=4):
    """right-angle marker at v between the directions towards points a and b"""
    def u(q): dx,dy=q[0]-v[0],q[1]-v[1]; L=math.hypot(dx,dy); return dx/L,dy/L
    (ax,ay),(bx,by)=u(a),u(b)
    return f'<path d="M{v[0]+ax*s:.1f} {v[1]+ay*s:.1f} L{v[0]+ax*s+bx*s:.1f} {v[1]+ay*s+by*s:.1f} L{v[0]+bx*s:.1f} {v[1]+by*s:.1f}" fill="none" stroke="{col}" stroke-width="{sw}"/>'
def dotc(x,y,r=12,fill=YEL): return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="{NAVY}" stroke-width="3"/>'
def clock(cx,cy,r,hour):
    g=f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{WHITE}" stroke="{NAVY}" stroke-width="5"/>'
    for k in range(12):
        a=math.radians(90-30*k); g+=LN(round(cx+r*0.82*math.cos(a),1),round(cy-r*0.82*math.sin(a),1),round(cx+r*0.95*math.cos(a),1),round(cy-r*0.95*math.sin(a),1),NAVY,4 if k%3==0 else 2)
    g+=ray((cx,cy),90,r*0.78,TEAL,7)+ray((cx,cy),90-30*hour,r*0.5,NAVY,9)+f'<circle cx="{cx}" cy="{cy}" r="7" fill="{NAVY}"/>'
    return g
def letter_svg(chars,w=100,h=150,gap=60,sw=12,label='letters'):
    g=''; x=10; top=10
    for c_ in chars:
        L_={'E':[(0,0,0,1),(0,0,1,0),(0,.5,.8,.5),(0,1,1,1)],'H':[(0,0,0,1),(1,0,1,1),(0,.5,1,.5)],'T':[(0,0,1,0),(.5,0,.5,1)],'L':[(0,0,0,1),(0,1,1,1)],
            'Z':[(0,0,1,0),(1,0,0,1),(0,1,1,1)],'N':[(0,1,0,0),(0,0,1,1),(1,1,1,0)],'F':[(0,0,0,1),(0,0,1,0),(0,.5,.8,.5)],'V':[(0,0,.5,1),(.5,1,1,0)]}[c_]
        for a,b,c2,d in L_: g+=LN(x+a*w,top+b*h,x+c2*w,top+d*h,NAVY,sw)
        x+=w+gap
    return SV(x-gap+20,h+20,g,label)

# ================= 1. title =================
put(PFX+'title',title_slide(PFX+'title','LESSON 8  •  WEEK 4','Angle and Line Detectives','Angles, Perpendicular and Parallel Lines',
 'Check angles with a right-angle checker, count angles without missing any, and spot perpendicular and parallel lines.',
 'Objective: Compare angles with a right angle using a folded-paper checker, count the angles at a point and the right angles in shapes and figures in an organised way, find a pattern in the counts, and find and draw perpendicular and parallel lines. Heuristics taught today: (1) count in an organised way (small angles first; visit every corner or meeting point), (2) look for a pattern. '
 'Materials: scrap paper to fold a right-angle checker (one per child), a ruler, mini whiteboards, square grid paper. '
 'Online: each child folds a checker on camera and does the right-angle hunt at home; annotate the grid slides with the pen tool. Print the workbook before the lesson. Pairs work in one breakout room for 10 minutes, then return for the check slide. '
 'Time plan: warm-up 0 to 10, explore 10 to 25, teaching 25 to 35 (click to reveal each step and answer), brain break 35 to 40, worksheet 40 to 70 with short teaching before page 2 and a check-together slide after each page, talk time 70 to 80, exit ticket 80 to 90. Stretch and Challenge are for early finishers. If the class is behind, children finish the last question of each page at home; the check slides cover it.'))

# ================= 2. warm-up: clock angles =================
cl=[(3,'Right angle'),(1,'Smaller'),(5,'Bigger'),(9,'Right angle'),(10,'Smaller'),(4,'Bigger')]
body=h2('Warm-up: clock angles')+stitle('Make the two hands with your arms. A right angle, smaller, or bigger?')
CW=533; cards=''; ans=''
for i,(hr,a) in enumerate(cl):
    L=128+(i%3)*(CW+32); Tp=300+(i//3)*300
    csvg=SV(200,200,clock(100,100,90,hr),f'A clock showing {hr} o’clock')
    cards+=pin(L,Tp,CW,f'<div style="display:flex;align-items:center;gap:22px">{csvg}<p style="font-family:{HF};font-size:42px;font-weight:600;line-height:1.1">{hr} o’clock</p></div>',None,WHITE,24,'16px 22px',f'box-sizing:border-box;height:270px;border:4px solid {NAVY};box-shadow:8px 8px 0 {NAVY}')
    ans+=pin(L+250,Tp+170,CW-270,f'<p style="font-size:34px;font-weight:800;line-height:1.2">{E(a)}</p>','pop',SOFT,16,'10px 18px',f'box-sizing:border-box;border:3px solid {NAVY}')
put(PFX+'warm1',S_(PFX+'warm1','0–5 MIN',body+cards+ans,
 'Minutes 0 to 5. Everyone stands. For each clock children make the hands with their arms (one arm straight up for the minute hand at 12, the other arm for the hour hand), then say "right angle", "smaller" or "bigger". Click to show the answer (clicks go clock by clock). '
 'Answers: 3 o’clock right angle; 1 o’clock smaller; 5 o’clock bigger; 9 o’clock right angle; 10 o’clock smaller; 4 o’clock bigger. '
 'Ask: "Why are 3 o’clock and 9 o’clock both right angles?" (The hour hand is a quarter of the way round, one way or the other.) "Which is bigger: 4 o’clock or 5 o’clock?" (5). Watch for children who think 9 o’clock is bigger because 9 is a bigger number.'))

# ================= 3. quick questions =================
qs=[('1.','How many right angles does a rectangle have?','4'),('2.','How many sides does a hexagon have?','6'),('3.','Name a capital letter made of 2 lines that meet at a right angle.','L (or T)'),('4.','Do the two long edges of a ruler ever meet?','No: parallel')]
body=h2('Quick questions')+''.join(qrow(128,260+i*150,1250,a,b) for i,(a,b,c) in enumerate(qs))+''.join(answer(1420,260+i*150,372,c) for i,(a,b,c) in enumerate(qs))
put(PFX+'warm2',S_(PFX+'warm2','5–10 MIN',body,'Minutes 5 to 10. Whiteboards, then click. Answers: 1) 4  2) 6  3) L or T (V has 2 lines that meet, but not at a right angle)  4) No: they stay the same distance apart all the way along. Lines like that are called parallel. We will meet them again today.'))

# ================= 4. explore: what to do =================
g=PG([(40,60),(150,20),(250,48),(300,140),(240,220),(120,232),(30,170)],SKY,NAVY,4)+LN(20,140,320,140,RED,4,'12 8')+T(170,268,'1. fold once',28)
g+=ARW(340,130,420,130,TEAL,7,22)
g+=PG([(460,140),(760,140),(700,58),(600,30),(480,70)],SKY,NAVY,4)+LN(600,140,600,30,RED,4,'12 8')+T(610,268,'2. fold the fold onto itself',28)
g+=ARW(790,130,870,130,TEAL,7,22)
g+=PG([(920,140),(1060,140),(1040,70),(980,40),(920,40)],YEL,NAVY,4)+rmark((920,140),(1060,140),(920,40),34,RED,5)+T(990,268,'3. your checker',28)
g+=ARW(1100,130,1180,130,TEAL,7,22)
g+=R(1230,60,300,160,WHITE,NAVY,4,8)+PG([(1230,220),(1340,220),(1325,170),(1290,140),(1230,140)],YEL,NAVY,3)+T(1380,268,'4. test a corner',28)
exsvg=SV(1600,284,g,'Fold a scrap of paper once, then fold the fold onto itself: the folded corner is a right-angle checker. Test the corner of a book with it.')
steps='<ol style="font-size:32px;font-weight:600;padding-left:48px;display:flex;flex-direction:column;gap:4px;margin:0"><li>Take any scrap of paper, even a torn one.</li><li>Fold it once. Then fold the fold exactly onto itself.</li><li>The folded corner is your right-angle checker.</li><li>Hunt: find 3 right angles, 1 smaller angle and 1 bigger angle.</li></ol>'
body=h2('Explore: what to do')+card(chip('EXPLORE')+steps,extra='padding:20px 40px')+card(exsvg,extra='padding:10px 32px')
put(PFX+'explore1',S_(PFX+'explore1','10–15 MIN',body,'Minutes 10 to 15. Predict first: "If I fold a torn, wiggly piece of paper twice, will the corner be a right angle?" Then everyone folds a checker (show it under the visualiser or on camera). Children hunt round the room (or at home) and record on a whiteboard: 3 right angles, 1 smaller, 1 bigger. Hints: "Put the corner of the checker into the angle. Do both arms line up?" "If one arm is hidden under the checker, the angle is smaller." Ready for more: find an angle that is exactly 2 right angles (a straight line).'))

# ================= 5. explore talk =================
put(PFX+'explore2',cards_slide(PFX+'explore2','15–25 MIN','Explore: talk about it',[('1.','Why is the folded corner a right angle, even with torn paper?'),('2.','Is an angle bigger if its arms are longer?'),('3.','Where did you find angles bigger than a right angle?')],
 'Minutes 15 to 25. Gather the group. Answers: 1) The first fold makes a straight line (a straight angle). Folding that line exactly onto itself cuts the straight angle into 2 equal parts, and each part is a right angle. The wiggly edges do not matter. 2) No. The size of an angle is how far the arms open (how much one arm turns to reach the other), not how long the arms are. Show two pencils opened the same amount, then slide one pencil out: the angle does not change. 3) For example a door opened wide, an open laptop, a clock at 5 o’clock, the corners of a hexagon tile.',size=40))

# ================= 6. teach 1: size of an angle =================
vP=(60,330); vQ=(600,330)
base=SV(860,380,ray(vP,0,300)+ray(vP,60,300)+arc(vP,0,60,50)+T(30,370,'P',40)+ray(vQ,0,140)+ray(vQ,100,140)+arc(vQ,0,100,40)+T(570,370,'Q',40),'Angle P has long arms and opens a little. Angle Q has short arms and opens more.')
def checker(v): return f'<rect x="{v[0]}" y="{v[1]-130}" width="130" height="130" fill="{YEL}" opacity=".55" stroke="{RED}" stroke-width="4"/>'+rmark(v,(v[0]+10,v[1]),(v[0],v[1]-10),30,RED,5)
ov1=SV(860,380,checker(vP),'the checker on P')
ov2=SV(860,380,checker(vQ),'the checker on Q')
body=h2('What makes an angle bigger?')+stitle('Which angle is bigger, P or Q? Guess first.')
body+=pin(128,310,860,base)
body+=ostep(128,310,1,'Put the checker on P. The second arm is under the checker: P is smaller than a right angle.',ov1,860,380,dx=890,dy=0,tw=774,size=32)
body+=ostep(128,310,2,'Put the checker on Q. The second arm is outside the checker: Q is bigger than a right angle.',ov2,860,380,dx=890,dy=170,tw=774,size=32)
body+=answer(128,720,1664,'Q is bigger, even with short arms. Size = how far the arms open.')
put(PFX+'teach1',S_(PFX+'teach1','25–27 MIN',body,'Teach. Ask first: "Which angle is bigger?" Many children choose P because its arms are long. Do not correct yet. Click 1: the checker on P (one arm along the bottom arm): the other arm is hidden under the checker, so P is smaller than a right angle. Click 2: the checker on Q: the other arm is outside, so Q is bigger than a right angle. Click 3: the conclusion. Think-aloud: "An angle shows how much one arm turns to reach the other. Long arms or short arms, the turn is the same. To compare, I always line the checker up with one arm and look where the other arm goes."'))

# ================= 7. worked example: count angles at a point =================
v0=(230,270); dirs=[20,65,110,160]
base=SV(460,300,''.join(ray(v0,d,220) for d in dirs)+f'<circle cx="{v0[0]}" cy="{v0[1]}" r="8" fill="{NAVY}"/>','4 lines going out from one point')
def fan_th(pairs):
    def f(x,i):
        v=(x+75,82); a,b=pairs[i]
        return sector(v,dirs[a],dirs[b],62)+''.join(ray(v,d,70,NAVY,3) for d in dirs)
    return f
def thumbs(n,w,h,draw,gap=16,label='thumbnails'): return SV(n*w+(n-1)*gap,h,''.join(draw(i*(w+gap),i) for i in range(n)),label)
body=h2('Count the angles: small ones first')+stitle('4 lines start at one point. How many angles can you find?')
body+=pin(128,300,460,base)
for k,(t,pairs) in enumerate([('Made of 1 small angle: 3',[(0,1),(1,2),(2,3)]),('Made of 2 small angles: 2',[(0,2),(1,3)]),('Made of 3 small angles: 1',[(0,3)])]):
    tt=thumbs(len(pairs),150,92,fan_th(pairs),14,t)
    body+=pin(640,290+k*140,1152,f'<div style="display:flex;align-items:center;gap:24px"><p style="width:500px;flex:none;font-size:34px;font-weight:600;line-height:1.3"><span style="color:{TEAL};font-weight:800">Step {k+1}.</span>  {E(t)}</p>{tt}</div>','fade',WHITE,20,'12px 28px')
body+=answer(640,720,1124,'3 + 2 + 1 = 6 angles')
put(PFX+'we1',S_(PFX+'we1','27–29 MIN',body,'Teach heuristic 1: count in an organised way. Ask first: "How many angles?" Most children say 3. Click through the sizes. Think-aloud: "There are 3 small angles between neighbouring lines. But two small angles side by side also make an angle: the first two together, the last two together: 2. And all three together make 1 big angle. I count by size, smallest first, so I never miss one or count one twice: 3 + 2 + 1 = 6." This is a parallel example: the worksheet has 6 lines.'))

# ================= 8. try 1: pattern =================
put(PFX+'try1',foot(try_slide(PFX+'try1','29–30 MIN','Your turn: look for a pattern','Draw the lines on your whiteboard. Count small angles first.',[('a','3 lines start at one point. How many angles?','3'),('b','2 lines start at one point. How many angles?','1'),('c','2 lines: 1.  3 lines: 3.  4 lines: 6. What are the jumps?','+2, +3, next +4')],
 'Whiteboards, then click. a) 2 small + 1 made of both = 3. b) 1. c) 1 to 3 is +2, 3 to 6 is +3, so the next jump is +4. Teach heuristic 2: look for a pattern. Ask: "Why does the jump grow by 1 each time?" (A new line makes a new angle with every line already there.) Do not give the answers for 6 or 8 lines: they are on the worksheet.',size=36)))

# ================= 9. teach 2: right angles inside a shape =================
u=105; ox=50; oy=40
Lpts=[(0,0),(3,0),(3,1),(1,1),(1,3),(0,3)]
Ps=[(ox+x*u, oy+(3-y)*u) for x,y in Lpts]
base=SV(420,400,PG(Ps,SKY,NAVY,6),'An L-shape with 6 corners')
marks=''
for i in range(6):
    if i==3: continue
    marks+=rmark(Ps[i],Ps[i-1],Ps[(i+1)%6],28,TEAL,5)
ov1=SV(420,400,dotc(*Ps[0],13,RED)+marks,'start dot and 5 right-angle marks')
v=Ps[3]; r_=32
ov2=SV(420,400,f'<path d="M{v[0]} {v[1]-r_} A{r_} {r_} 0 1 0 {v[0]+r_} {v[1]}" fill="none" stroke="{RED}" stroke-width="6"/>','the dent corner is bigger than a right angle inside')
body=h2('Right angles inside a shape')+stitle('How many right angles are inside this L-shape?')
body+=pin(128,300,420,base)
body+=ostep(128,300,1,'Put a dot where you start. Go round and check every corner with your checker: 5 corners are right angles inside.',ov1,420,400,dx=480,dy=0,tw=1184)
body+=ostep(128,300,2,'The dent corner: inside the shape, the angle is bigger than a right angle (3 right angles put together!).',ov2,420,400,dx=480,dy=150,tw=1184)
body+=answer(608,620,1184,'6 corners, but only 5 right angles inside.')
put(PFX+'teach2',S_(PFX+'teach2','30–31 MIN',body,'Ask first: "How many corners? How many right angles inside?" Many children say 6 and 6. Click 1: the start dot and the 5 square corners, checked one by one. Click 2: the dent corner: put the checker INSIDE the shape at that corner: the inside angle is much bigger (it goes three-quarters of the way round). Click 3: the answer. Think-aloud: "I put a dot where I start so I visit every corner once. I check each one: is the inside a right angle? A dent corner points into the shape, so inside it is bigger." Parallel example: the worksheet shapes are different.'))

# ================= 10. worked example: right angles where lines meet =================
rx,ry,rw,rh=40,30,500,300
pts=[(rx,ry),(rx+rw,ry),(rx+rw,ry+rh),(rx,ry+rh)]; mt=(rx+rw/2,ry); mb=(rx+rw/2,ry+rh)
base=SV(580,360,R(rx,ry,rw,rh,SKY,NAVY,6)+LN(mt[0],mt[1],mb[0],mb[1],NAVY,6),'A rectangle with one line from the middle of the top to the middle of the bottom')
ov1=SV(580,360,''.join(dotc(x,y,14) for x,y in pts+[mt,mb]),'dots on the 6 meeting points')
ov2=SV(580,360,rmark(pts[0],pts[1],pts[3])+rmark(pts[1],pts[0],pts[2])+rmark(pts[2],pts[1],pts[3])+rmark(pts[3],pts[0],pts[2]),'one right angle at each corner')
ov3=SV(580,360,rmark(mt,(mt[0]-10,mt[1]),mb,26,RED)+rmark(mt,(mt[0]+10,mt[1]),mb,26,RED)+rmark(mb,(mb[0]-10,mb[1]),mt,26,RED)+rmark(mb,(mb[0]+10,mb[1]),mt,26,RED),'two right angles at each middle point')
body=h2('Right angles where lines meet')+stitle('How many right angles can you find in this picture?')
body+=pin(128,300,580,base)
body+=ostep(128,300,1,'List every point where lines meet: 4 corners and 2 middle points.',ov1,580,360,dx=620,dy=0,tw=1044,size=32)
body+=ostep(128,300,2,'Each corner has 1 right angle: 4.',ov2,580,360,dx=620,dy=135,tw=1044,size=32)
body+=ostep(128,300,3,'Each middle point has 2 right angles, one on each side of the line: 2 + 2 = 4.',ov3,580,360,dx=620,dy=245,tw=1044,size=32)
body+=answer(748,700,1044,'4 + 4 = 8 right angles')
put(PFX+'we2',S_(PFX+'we2','31–33 MIN',body,'Click through. Think-aloud: "If I look at the whole picture I will lose count. So I make a list of the meeting points and visit them one by one. At a corner, 1 right angle. Where the middle line meets the top, there is a right angle on its left and one on its right: 2." Ask: "At the middle of the top, is there an angle made of both right angles together?" (That is a straight line, 2 right angles: we do not count it as a right angle.) Parallel example: the worksheet window has two lines.'))

# ================= 11. try 2 =================
def tiny(g,w,h,l): return SV(w,h,g,l)
plus=tiny(LN(60,8,60,112,NAVY,7)+LN(8,60,112,60,NAVY,7),120,120,'two lines crossing like a plus sign')
Tsh=[(0,2),(0,3),(3,3),(3,2),(2,2),(2,0),(1,0),(1,2)]
Tp_=tiny(PG([(8+x*34,8+(3-y)*34) for x,y in Tsh],SKY,NAVY,5),120,120,'a T-shape')
Hs=tiny(LN(20,10,20,110,NAVY,8)+LN(100,10,100,110,NAVY,8)+LN(20,60,100,60,NAVY,8),120,120,'the letter H')
rows=[('a',plus,'2 lines cross like this, at a right angle. How many right angles?','4'),('b',Tp_,'How many right angles are INSIDE this T-shape?','6'),('c',Hs,'How many right angles are there in the letter H?','4')]
body=h2('Your turn: count the right angles')+stitle('Visit every corner or meeting point.')
for i,(l,pic,t,a) in enumerate(rows):
    tp=300+i*190
    body+=pin(128,tp,1250,f'<div style="display:flex;align-items:center;gap:28px"><p style="font-size:38px;font-weight:800;color:{TEAL};flex:none">{l}</p><div style="flex:none">{pic}</div><p style="font-size:34px;font-weight:600;line-height:1.3">{E(t)}</p></div>',None,WHITE,20,'14px 28px')
    body+=answer(1420,tp+30,372,a)
put(PFX+'try2',S_(PFX+'try2','33–34 MIN',body,'Whiteboards, then click. a) 4: one in each quarter where the lines cross. b) 6: the T has 8 corners; the 2 corners under the arms are dents, bigger than a right angle inside. c) 4: the middle line meets each upright line in its middle, making 2 right angles at each meeting point. The ends of the lines are not corners.'))

# ================= 12. teach 3: perpendicular and parallel =================
perp=SV(200,150,LN(30,130,180,130,NAVY,7)+LN(70,20,70,130,NAVY,7)+rmark((70,130),(180,130),(70,20),26,RED,5),'two perpendicular lines')
para=SV(200,150,LN(20,120,150,30,NAVY,7)+LN(60,140,190,50,NAVY,7)+LN(150,30,190,4,NAVY,3,'8 8')+LN(190,50,200,43,NAVY,3,'8 8'),'two parallel lines')
Fsvg=SV(260,330,LN(50,20,50,310,NAVY,10)+LN(50,20,220,20,NAVY,10)+LN(50,165,190,165,NAVY,10)+T(24,190,'a',40,TEAL)+T(140,70,'b',40,TEAL)+T(130,215,'c',40,TEAL),'The letter F made of 3 lines: a is upright, b is the top line, c is the middle line')
defbox=lambda svg_,t: f'<div style="display:flex;align-items:center;gap:20px"><div style="flex:none">{svg_}</div><p style="font-size:32px;font-weight:600;line-height:1.3">{t}</p></div>'
body=h2('Perpendicular and parallel lines')
body+=pin(128,230,760,defbox(perp,'<b>Perpendicular</b> lines meet at a right angle.'),None,WHITE,20,'16px 24px')
body+=pin(128,440,760,defbox(para,'<b>Parallel</b> lines stay the same distance apart. They never meet, even if we make them longer.'),None,WHITE,20,'16px 24px')
body+=pin(940,230,260,Fsvg)
body+=pin(1230,230,562,p('<span style="color:#1F7A6F;font-weight:800">Step 1.</span>  List every pair: a and b, a and c, b and c.',32,600,raw=True),'fade',WHITE,20,'14px 22px')
body+=pin(1230,390,562,p('<span style="color:#1F7A6F;font-weight:800">Step 2.</span>  a and b: perpendicular. a and c: perpendicular.',32,600,raw=True),'fade',WHITE,20,'14px 22px')
body+=pin(1230,550,562,p('<span style="color:#1F7A6F;font-weight:800">Step 3.</span>  b and c: parallel.',32,600,raw=True),'fade',WHITE,20,'14px 22px')
body+=answer(128,690,1664,'The letter F: 1 pair of parallel lines and 2 pairs of perpendicular lines.')
put(PFX+'teach3',S_(PFX+'teach3','34–35 MIN',body,'Teach the two words with arms: one arm up, one arm out sideways: perpendicular. Both arms up: parallel. On the parallel picture, the dotted ends show the lines carrying on: they never meet. Then the F: click through. Think-aloud: "To find every pair I make a list: a with b, a with c, b with c. That is all of them. Then I test each pair: do they meet at a right angle? Are they always the same distance apart?" Parallel example: the worksheet asks about E.'))

# ================= 13. key idea =================
body=h2('Key idea: count in order, look for a pattern')+card(p('Visit every corner or meeting point, and count small angles first. When the counts grow, look for a pattern.',42,700))+card(p('An angle’s size is how far it opens, not how long its arms are. Check with your checker.',38,600,MUTED))
put(PFX+'key',S_(PFX+'key','35 MIN',body,'Say the key ideas together. Common mistakes to watch for during the worksheet: (1) Thinking a turned right angle (Q1 a) is not a right angle, or that longer arms make a bigger angle (Q1 d and f). Use the checker every time. (2) Counting every corner as a right angle in Q2: dent corners are bigger inside. The roof top of the house IS a right angle: check it. (3) Counting angles at random in Q3: count by size. (4) In Q6, counting only the 4 small squares\' corners and missing angles, or counting a straight line as a right angle.'))

# ================= 14. break =================
put(PFX+'break',break_slide(PFX+'break','35–40 MIN','Body angles. Make a right angle with your arms, then a smaller angle, then a bigger one. Now hold your arms parallel, then perpendicular. Faster!','Then: a drink of water and back to our seats.','Five minutes. Online: children stay in view of the camera and move in place.'))

# ================= 15/16. page 1 =================
put(PFX+'ws1',preview(PFX+'ws1','40–52 MIN','Worksheet page 1: with your partner',[('Q1','Sort six angles. Use your checker on every one.'),('Q2','Right angles INSIDE four shapes. Put a dot where you start.'),('Q3','Angles at a point. Small ones first, then look for a pattern.')],'Stuck? Line the checker up with one arm and look where the other arm goes.','Minutes 40 to 52. Walk around. Ask "How do you know?" before giving any help. Q1: insist on the checker, especially for a (turned) and d (short arm). Q2: the house roof top is a right angle; let them discover it with the checker. Q3: "How many small angles are there? Now 2 together?"'))
put(PFX+'ws1ans',checkrows(PFX+'ws1ans','52–54 MIN','Page 1: check together',[('Q1','Smaller: b, f.   Right angle: a, d.   Bigger: c, e.'),('Q2','A 8,   B 6,   C 3,   D 2'),('Q3','a) 5 + 4 + 3 + 2 + 1 = 15     b) 7 + 6 + 5 + 4 + 3 + 2 + 1 = 28')],
 'Click each answer after a pair explains theirs. Q1: a is a right angle that is turned; d is a right angle with one short arm; f has long arms but is smaller. Q2: A has 12 corners but 4 are dents; B has 8 corners with 2 dents; C: the 2 bottom corners and the roof top (the corners where the walls meet the roof are bigger); D: the 2 left corners. Q3: 6 lines make 5 small angles. The pattern of jumps: 1, 3, 6, 10, 15, 21, 28.',lw=200,size=34,gap=140))

# ================= 17. teach before page 2: lines on a grid =================
c=52; gx=30; gy=20
G_=lambda a,b: (gx+a*c, gy+b*c)
P1,Q1=G_(1,5),G_(7,3); S0=G_(4,4); Rr=G_(8,7)
base=SV(800,460,bgrid(gx,gy,14,8,c)+LN(*P1,*Q1,NAVY,6)+dotc(*P1,9,NAVY)+dotc(*Q1,9,NAVY)+dotc(*S0,9,NAVY)+dotc(*Rr,9,NAVY)+T(P1[0]-20,P1[1]+32,'P',30)+T(Q1[0]+18,Q1[1]-14,'Q',30)+T(S0[0]-6,S0[1]-18,'S',30)+T(Rr[0]-22,Rr[1]+8,'R',30),'A square grid with line PQ, point S on PQ and point R')
ov1=SV(800,460,ARW(*G_(1,5),*G_(4,5),YEL,8,20)+ARW(*G_(4,5),*G_(4,4),YEL,8,20)+T(G_(2.5,5)[0],G_(2.5,5)[1]+36,'3 right',26,TEAL)+T(G_(4,4.5)[0]+40,G_(4,4.5)[1]+10,'1 up',26,TEAL),'3 right and 1 up')
ov2=SV(800,460,LN(*G_(8,7),*G_(14,5),TEAL,6),'a parallel line through R')
ov3=SV(800,460,LN(*G_(3,1),*G_(5,7),RED,6)+rmark(S0,Q1,G_(5,7),24,RED,4),'a perpendicular line through S')
body=h2('Parallel and perpendicular on a square grid')
body+=pin(128,230,800,base)
body+=ostep(128,230,1,'PQ goes 3 squares right and 1 square up, again and again.',ov1,800,460,dx=830,dy=0,tw=834,size=32)
body+=ostep(128,230,2,'Parallel: use the SAME steps from R: 3 right, 1 up.',ov2,800,460,dx=830,dy=130,tw=834,size=32)
body+=ostep(128,230,3,'Perpendicular: swap the numbers and turn: 1 right, 3 down from S. Check it with your checker ✓',ov3,800,460,dx=830,dy=260,tw=834,size=32)
body+=soft(128,720,1664,'Lines that go along the grid lines are easy: across is perpendicular to up and down.',32)
put(PFX+'teachgrid',S_(PFX+'teachgrid','54–57 MIN',body,'Teach before worksheet page 2 (Q5 asks for parallel and perpendicular lines on a grid; these lines use different steps). Click 1: count the steps along PQ. Click 2: from R, copy the same steps: the new line never meets PQ. Click 3: swap 3 and 1 and turn: 1 right and 3 down. Put a paper checker on S to show the right angle. Think-aloud: "Parallel lines go the same way, so they have the same steps. For perpendicular, I swap the two numbers and turn the line round." Watch for children who swap but do not turn (1 right, 3 up): check it with the checker, it is not a right angle.'))

# ================= 18/19. page 2 =================
put(PFX+'ws2',preview(PFX+'ws2','57–68 MIN','Worksheet page 2: on your own',[('Q4','Parallel and perpendicular lines in letters. Then list every pair in E.'),('Q5','Draw parallel and perpendicular lines on a grid. Count the steps. Q5c is Think Harder, if you have time.'),('Q6','Right angles in a window. Visit every meeting point.')],'Ready for more? Stretch and Challenge come next.','Children work alone. Note who needs a short catch-up next lesson. Q4b: "List the pairs first." Q6: "Which points have you visited?"'))
put(PFX+'ws2ans',checkrows(PFX+'ws2ans','68–70 MIN','Page 2: check together',[('Q4','E, H: both.   T, L: perpendicular only.   Z, N: parallel only.   E: 3 and 3.'),('Q5','a) 1 right, 1 up through C   b) 1 right, 1 down through D   c) 1 right, 2 down through G'),('Q6','16 right angles: corners 4 + side points 4 × 2 + middle 4')],
 'Click each answer after a child explains. Q4: in Z and N the slanted line is not at a right angle to the others. Q4b: E has an upright line and 3 short lines: the 3 short lines make 3 parallel pairs, and each one with the upright line is a perpendicular pair. Q5: check each drawn line with the checker. Q6: 4 corners × 1 = 4; 4 points where the lines meet the sides × 2 = 8; the middle crossing has 4. 4 + 8 + 4 = 16.',lw=200,size=32,gap=150))

# ================= 20. stretch =================
put(PFX+'stretch',cards_slide(PFX+'stretch','For early finishers','Stretch',[('1.','Draw a 4-sided shape with exactly 1 right angle.'),('2.','Can a triangle have 2 right angles? Explain.'),('3.','The letter H is made of 3 straight lines. List every pair of lines. Which pairs are parallel? Which are perpendicular?')],
 'For children who finish early. Answers: 1) For example, on a grid with the bottom-left corner at (0, 0): corners at 0 across 0 up, 4 across 0 up, 3 across 2 up, 0 across 3 up. Only the bottom-left corner is a right angle (check the other three with the checker). 2) No. If two corners on the bottom side were right angles, both other sides would go straight up and be parallel, so they would never meet to close the triangle. 3) 3 pairs: the two upright lines are parallel; the line across is perpendicular to each upright line. So 1 pair of parallel lines and 2 pairs of perpendicular lines.',size=38))

# ================= 21. challenge =================
put(PFX+'challenge',cards_slide(PFX+'challenge','65–80 MIN','Challenge',[('1.','A long rectangle is cut into 6 squares in a row by 5 lines. How many right angles can you find?'),('2.','Can a 6-sided shape have 6 right angles inside it? What is the most right angles a 6-sided shape can have inside?')],
 'Use as a pair challenge or in talk time. Ask for the reason every time. Answers: 1) 24 (4 at the corners; each of the 5 lines makes 2 right angles at the top and 2 at the bottom: 4 + 5 × 4 = 24). 2) No. The most is 5, for example an L shape. More are in the question bank.',size=36))

# ================= 22. challenge: see it =================
g1=R(30,60,600,100,SKY,NAVY,5)+''.join(LN(30+k*100,60,30+k*100,160,NAVY,5) for k in range(1,6))+T(330,230,'6 squares in a row, 5 lines inside.',30)+T(330,290,'Visit every point where lines meet.',28,TEAL)
g1+=R(130,340,400,90,WHITE,NAVY,3,10)+T(330,380,'Points:  corners ___  others ___',26)+T(330,418,'Right angles at each?',26,TEAL)
g2=bgrid(110,40,8,6,55)+T(330,420,'Draw 6 sides along the grid lines.',30)+T(330,470,'Check every corner inside the shape.',28,TEAL)
pan=lambda t,s_: f'<div style="background:{WHITE};border-radius:24px;padding:20px 24px;display:flex;flex-direction:column;gap:10px;flex:1;min-width:0"><p style="font-size:30px;font-weight:700;color:{TEAL}">{E(t)}</p>{s_}</div>'
body=h2('Challenge: see it',60)+f'<div style="display:flex;gap:32px;align-items:flex-start">{pan("Q1: six squares in a row",SV(660,500,g1,"A long rectangle cut into 6 squares by 5 lines"))}{pan("Q2: a 6-sided shape",SV(660,500,g2,"An empty square grid to draw a 6-sided shape on"))}</div>'
put(PFX+'chdiag',S_(PFX+'chdiag','65–80 MIN',body,'Show after pairs have tried the Challenge, or if they are stuck. The pictures show the problem, not the answer. Ask: What do you notice? Which heuristic could help: count in order, or look for a pattern (try 1 square, 2 squares, 3 squares first)? Answers are in the Challenge slide notes.'))

# ================= 23. challenge walk-through =================
body=h2('Challenge: walk-through')+pin(128,250,800,p('Q1: try smaller ones, find a pattern',34,800,TEAL))
for i,t in enumerate(['1 square: 4 right angles. 2 squares: 8.','3 squares: 12. Each new line adds 4.','6 squares have 5 lines: 4 + 5 × 4','= 24 right angles ✓']): body+=pin(128,330+i*120,800,p(t,32),'rise',WHITE)
body+=pin(992,250,800,p('Q2: draw it and check',34,800,TEAL))
for i,t in enumerate(['Try it: draw 6 square corners on grid paper. What do you always get?','You always get a dent (a corner that is bigger inside).','An L shape: 6 corners, 5 right angles.','So the most is 5 ✓']): body+=pin(992,330+i*120,800,p(t,32),'rise',WHITE)
put(PFX+'chwalk',S_(PFX+'chwalk','Challenge',body,'Use after pairs have tried. Q1: when a problem is big, try smaller ones and look for a pattern: 4, 8, 12 … goes up by 4 because each new line meets the top and the bottom, with 2 right angles at each. Q2: let children try to draw 6 square corners along the grid lines: they always get a dent. A proof is not expected: children see that 6 square corners always give a dent, and the best they can draw is the L shape with 5 square corners and 1 dent.'))

# ================= 24. talk =================
body=h2('Talk time')+card(chip('TALK TIME',YEL,NAVY)+p('Mei says: “An angle with longer arms is a bigger angle.” Do you agree? How can you test it?',42,600))+card(p('Sentence starters:',34,400,MUTED)+p('“I noticed that …”   “I tested it by …”   “I know because …”',38,600))
put(PFX+'talk',S_(PFX+'talk','70–80 MIN',body,'Minutes 70 to 80. Pairs talk for 2 minutes, then share. Answer: No. The size of an angle is how far the arms open. Test: draw the same angle twice, once with long arms and once with short arms, and put the checker on both: it fits the same way. Or open two pencils the same amount, then slide one out. Follow-up: "How did you make sure you did not miss any angles?" (Count small ones first; visit every meeting point.)'))

# ================= 25. exit =================
lets=letter_svg('FVHZ',90,130,70,12,'The letters F, V, H and Z')
body=h2('Exit ticket')+card(chip('EXIT TICKET')+p('Which letters have BOTH a pair of parallel lines and a pair of perpendicular lines?',44,600)+lets)+card(p('Write your answer on a slip of paper. Show it to your tutor. Then collect your stamp in your inquiry journal.',34,400))
put(PFX+'exit',S_(PFX+'exit','80–90 MIN',body,'Minutes 80 to 90. Answer: F and H. F: the top and middle lines are parallel, and each meets the upright line at a right angle. H: the two upright lines are parallel, and the middle line is perpendicular to both. V: two lines that meet, not at a right angle. Z: the top and bottom are parallel, but the slanted line is not perpendicular to them. Extension: how many right angles are in a square drawn as a noughts-and-crosses grid? (36)'))

# ---------- write ----------
order=['title','warm1','warm2','explore1','explore2','teach1','teach2','we2','try2','teach3','key','break','we1','try1','ws1','ws1ans','teachgrid','ws2','ws2ans','stretch','challenge','chdiag','chwalk','talk','exit']
order=[PFX+o for o in order]
os.makedirs(os.path.join(D,'slides'),exist_ok=True)
import p3_gifted; order[:]=p3_gifted.add(S,order,8)  # close-the-gaps: warm-up check + look-back slides
for f in os.listdir(os.path.join(D,'slides')):
    if f.startswith(PFX) and f[:-5] not in order: os.remove(os.path.join(D,'slides',f))
for i,h in S.items(): open(os.path.join(D,'slides',i+'.html'),'w').write(h)
deck={'v':4,'createdOnFiles':{'v':1,'at':datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')},'lists':'css',
      'title':'Math Inquirers P3: Lesson 8 – Angle and Line Detectives','order':order,'cover':PFX+'title',
      'sections':{'s1':{'description':'Warm-up and explore','start':PFX+'title'},'s2':{'description':'Teach: count in order, look for a pattern, perpendicular and parallel','start':PFX+'teach1'},
                  's3':{'description':'Worksheet with teaching before page 2','start':PFX+'break'},'s4':{'description':'Think harder, go further, talk and exit','start':PFX+'stretch'}},
      'faces':{'fredoka':{'family':'Fredoka','href':'https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&display=swap'},'nunito-sans':{'family':'Nunito Sans','href':'https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@400;600;700&display=swap'}},
      'designSystems':[]}
json.dump(deck,open(os.path.join(D,'deck.json'),'w'),indent=1,ensure_ascii=False)
missing=[i for i in order if not os.path.exists(os.path.join(D,'slides',i+'.html'))]
print(len(order),'slides; wrote',len(S),'missing',missing)
