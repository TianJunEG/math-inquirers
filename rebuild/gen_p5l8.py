"""Math Inquirers P5, Lesson 8: Angle Chasers. Writes split/p5l8/project (deck.json + slides/*.html).
Every angle figure is built from coordinates; chk() raises an error if a stated angle is not the real angle."""
import json,os,sys,datetime,math
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,H)
import slidekit
from slidekit import *
slidekit.FOOT='Math Inquirers P5 Holiday Program  •  Notice it. Test it. Explain why.'
D=os.path.join(H,'..','split','p5l8','project'); os.makedirs(os.path.join(D,'slides'),exist_ok=True)
S={}
def put(i,h): S[i]=h
RED='#D64545'; FOOTX=slidekit.FOOT; GREEN='#3DBE7A'; BLUE='#3A6EA5'

# ---------- shared slide shapes (same look as the other decks) ----------
def title_slide(sid,label,title,topic,today,notes):
    return (f'<section id="{sid}" data-transition="fade" style="background:{NAVY};color:{CREAM};font-family:{BF};padding:128px 128px 160px;display:flex;flex-direction:column;justify-content:center;gap:36px">\n'
            f'<p style="font-size:32px;font-weight:700;letter-spacing:4px;color:{YEL}">{E(label)}</p>\n'
            f'<h1 style="font-family:{HF};font-size:128px;font-weight:600;line-height:1.05">{E(title)}</h1>\n'
            f'<p style="font-size:44px;color:#C9D4EC">{E(topic)}</p>\n'
            f'<div style="background:#26385F;border-radius:24px;padding:40px;display:flex;flex-direction:column;gap:12px"><p style="font-size:28px;font-weight:700;letter-spacing:3px;color:{YEL}">TODAY WE WILL</p><p style="font-size:44px;font-weight:600">{E(today)}</p></div>\n'
            f'<p style="position:absolute;left:128px;bottom:64px;width:1400px;font-size:24px;color:#B7C3DD">{E(FOOTX)}</p>\n<aside>{E(notes)}</aside>\n</section>\n')
def break_slide(sid,time,text,notes):
    return (f'<section id="{sid}" data-transition="fade" style="background:{TEAL};color:{CREAM};font-family:{BF};padding:128px 128px 160px;display:flex;flex-direction:column;justify-content:center;gap:36px">\n'
            f'<p style="font-size:32px;font-weight:700;letter-spacing:4px;color:{YEL}">{E(time)}</p>\n'
            f'<h2 style="font-family:{HF};font-size:110px;font-weight:600;line-height:1.05">Brain break</h2>\n'
            f'<p style="font-size:48px;font-weight:600">{E(text)}</p>\n<p style="font-size:36px;color:#D7EFEA">Then: a drink of water and back to our seats.</p>\n'
            f'<p style="position:absolute;left:128px;bottom:64px;width:1400px;font-size:24px;color:#D7EFEA">{E(FOOTX)}</p>\n<aside>{E(notes)}</aside>\n</section>\n')
def numcards(items,size=38):
    return ''.join(card(p(f'<span style="color:{TEAL}">{a}</span>  {E(b)}',size,600,raw=True)) for a,b in items)
def checks(sid,time,title,rows,notes,top=250,gapy=150,size=34,lw=170):
    body=h2(title)
    for i,(a,b) in enumerate(rows):
        t=top+i*gapy
        body+=pin(128,t,lw-20,f'<p style="font-size:36px;font-weight:800;color:{TEAL}">{E(a)}</p>',None,WHITE,20,'18px 24px')
        body+=pin(128+lw,t,1664-lw,f'<p style="font-size:{size}px;font-weight:800;line-height:1.25">{E(b)}</p>','pop',YEL,20,'16px 26px')
    return sec(sid,time,body,notes)
def txt(x,y,s,size=40,fill=NAVY,anchor='middle',weight=700,font='Fredoka, Arial',halo=False):
    h=f' stroke="{WHITE}" stroke-width="7" paint-order="stroke" stroke-linejoin="round"' if halo else ''
    return f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" fill="{fill}" font-family="{font}"{h}>{E(str(s))}</text>'
PADX,PADY=30,36   # room for vertex labels outside the drawing
def svgwrap(w,h,label,inner,k=1.0):
    return f'<svg aria-label="{E(label)}" viewBox="{-PADX} {-PADY} {w+PADX} {h+PADY}" xmlns="http://www.w3.org/2000/svg" style="width:{round((w+PADX)*k)}px;height:{round((h+PADY)*k)}px;flex:none">{inner}</svg>'
def soft(left,top,width,text,size=34,build='fade'): return pin(left,top,width-56,p(text,size,700),build,SOFT,20,'18px 28px')
def ostep(left,top,n,text,ov=None,ovw=0,ovh=0,dx=0,dy=0,tw=1000,size=34,extra='',build='fade',lab=True):
    """One click = overlay marks (same left/top as the base picture) + the step text box beside it."""
    l=f'<span style="color:{TEAL};font-weight:800">Step {n}.</span>  ' if (n and lab) else ''
    tx=f'<p style="font-size:{size}px;font-weight:600;line-height:1.3">{l}{E(text)}</p>'
    box=f'<div style="margin-top:{dy}px;width:{tw}px;box-sizing:border-box;background:{WHITE};border-radius:20px;padding:16px 28px;display:flex;flex-direction:column;gap:10px;flex:none">{tx+extra}</div>'
    if ov is None: return pin(left+dx,top+dy,tw,box.replace(f'margin-top:{dy}px;',''),build)
    ovw+=PADX; ovh+=PADY
    o=f'<div style="width:{ovw}px;height:{ovh}px;flex:none">{ov}</div>'
    return pin(left,top,dx+tw,f'<div style="display:flex;align-items:flex-start;gap:{dx-ovw}px">{o}{box}</div>',build)

# ---------- geometry (maths angles in degrees, y up; SVG points are y down) ----------
def rad(d): return d*math.pi/180
def P(x,y,r,deg): return (x+r*math.cos(rad(deg)), y-r*math.sin(rad(deg)))
def ang(v,a,b):
    d=abs(math.atan2(a[1]-v[1],a[0]-v[0])-math.atan2(b[1]-v[1],b[0]-v[0]))*180/math.pi
    return 360-d if d>180 else d
def chk(v,a,b,exp,name=''):
    if abs(ang(v,a,b)-exp)>0.05: raise SystemExit(f'ANGLE {name}: drawn {ang(v,a,b):.2f}, stated {exp}')
def dist(a,b): return math.hypot(a[0]-b[0],a[1]-b[1])
def chkeq(a,b,c,d,name=''):
    if abs(dist(a,b)-dist(c,d))>0.05: raise SystemExit(f'SIDES {name} not equal')
def chkpar(a,b,c,d,name=''):
    if abs((b[0]-a[0])*(d[1]-c[1])-(b[1]-a[1])*(d[0]-c[0]))>0.5: raise SystemExit(f'NOT PARALLEL {name}')
def line(a,b,col=NAVY,sw=5,dash=''):
    d=f' stroke-dasharray="{dash}"' if dash else ''
    return f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" stroke="{col}" stroke-width="{sw}" stroke-linecap="round"{d}/>'
def poly(pts,fill=SKY,sw=5): return f'<polygon points="{" ".join(f"{x:.1f},{y:.1f}" for x,y in pts)}" fill="{fill}" stroke="{NAVY}" stroke-width="{sw}" stroke-linejoin="round"/>'
def arc(v,a,b,r,label='',col=RED,lr=0,fs=28,sw=5):
    a1=math.atan2(a[1]-v[1],a[0]-v[0]); a2=math.atan2(b[1]-v[1],b[0]-v[0]); d=a2-a1
    while d>math.pi: d-=2*math.pi
    while d<-math.pi: d+=2*math.pi
    p1=(v[0]+r*math.cos(a1),v[1]+r*math.sin(a1)); p2=(v[0]+r*math.cos(a2),v[1]+r*math.sin(a2))
    s=f'<path d="M{p1[0]:.1f} {p1[1]:.1f} A{r} {r} 0 0 {1 if d>0 else 0} {p2[0]:.1f} {p2[1]:.1f}" fill="none" stroke="{col}" stroke-width="{sw}"/>'
    if label:
        am=a1+d/2; rr=lr or r+30
        s+=txt(v[0]+rr*math.cos(am),v[1]+rr*math.sin(am)+fs*0.35,label,fs,col,halo=True)
    return s
def tick(a,b,n=1):
    m=((a[0]+b[0])/2,(a[1]+b[1])/2); l=dist(a,b); u=((b[0]-a[0])/l,(b[1]-a[1])/l); nn=(-u[1],u[0]); s=''
    for i in range(n):
        o=(i-(n-1)/2)*10; c=(m[0]+u[0]*o,m[1]+u[1]*o)
        s+=f'<line x1="{c[0]-nn[0]*11:.1f}" y1="{c[1]-nn[1]*11:.1f}" x2="{c[0]+nn[0]*11:.1f}" y2="{c[1]+nn[1]*11:.1f}" stroke="{RED}" stroke-width="5"/>'
    return s
def parr(a,b):
    m=((a[0]+b[0])/2,(a[1]+b[1])/2); l=dist(a,b); u=((b[0]-a[0])/l,(b[1]-a[1])/l); nn=(-u[1],u[0])
    t=(m[0]+u[0]*11,m[1]+u[1]*11); p1=(m[0]-u[0]*9+nn[0]*10,m[1]-u[1]*9+nn[1]*10); q=(m[0]-u[0]*9-nn[0]*10,m[1]-u[1]*9-nn[1]*10)
    return f'<polyline points="{p1[0]:.1f},{p1[1]:.1f} {t[0]:.1f},{t[1]:.1f} {q[0]:.1f},{q[1]:.1f}" fill="none" stroke="{TEAL}" stroke-width="5"/>'
def sq(v,a,b,s=22):
    u=(a[0]-v[0],a[1]-v[1]); w=(b[0]-v[0],b[1]-v[1]); lu=math.hypot(*u); lw=math.hypot(*w)
    p1=(v[0]+u[0]/lu*s,v[1]+u[1]/lu*s); p2=(p1[0]+w[0]/lw*s,p1[1]+w[1]/lw*s); p3=(v[0]+w[0]/lw*s,v[1]+w[1]/lw*s)
    return f'<path d="M{p1[0]:.1f} {p1[1]:.1f} L{p2[0]:.1f} {p2[1]:.1f} L{p3[0]:.1f} {p3[1]:.1f}" fill="none" stroke="{RED}" stroke-width="4"/>'
def pl(pt,name,dx,dy,size=34): return txt(pt[0]+dx,pt[1]+dy,name,size,NAVY)
def sector(c,r,a1,a2,fill):
    p1=P(c[0],c[1],r,a1); p2=P(c[0],c[1],r,a2)
    return f'<path d="M{c[0]:.1f} {c[1]:.1f} L{p1[0]:.1f} {p1[1]:.1f} A{r} {r} 0 0 0 {p2[0]:.1f} {p2[1]:.1f} Z" fill="{fill}" stroke="{NAVY}" stroke-width="4"/>'

# ---------- 1. title ----------
put('p5l8-title',title_slide('p5l8-title','LESSON 8  •  WEEK 4B','Angle Chasers','Angles, triangles and quadrilaterals',
 'Chase unknown angles through triangles, parallelograms, rhombuses and trapezia, giving a reason for every step.',
 'Objective: Use the angle facts (straight line 180°, point 360°, vertically opposite, triangle 180°, isosceles and equilateral triangles, parallelogram, rhombus, trapezium) to chase unknown angles through a figure, step by step, giving a reason for every step; list every case when only one angle of an isosceles triangle is given. '
 'Thinking strategies taught today: WRITE DOWN WHAT YOU KNOW, FIND ONE ANGLE AND SAY WHY, and TRY EVERY CASE. Drawings are not to scale: never measure. '
 'Materials: paper, ruler, pencil, scissors, protractor (only for the explore activity), red and blue pencils, mini whiteboards, workbook. '
 'Online: children tear or cut the corners of a paper triangle and quadrilateral on camera. The tutor screen-shares the slides and draws on the figures with the annotation tool. '
 'Time plan: sneak-peek puzzles 0 to 3 (private answers, nobody is marked), warm-up 3 to 9, explore 9 to 21 (a Go further what-if is on the explore slide for anyone who wants more), teaching 21 to 33 (click to reveal each step and answer), brain break 33 to 37, workbook page 1 37 to 49 (after question 3 you may choose: carry on, or try Think harder), check together 49 to 53, short teaching before page 2 53 to 58, workbook page 2 58 to 72 (alone: start with the questions named at the top, then choose; nobody has to finish), check together 72 to 76, talk time 76 to 82 (you may say pass; volunteers first; then everyone tries the first step of the Investigation), exit ticket 82 to 86, reflection 86 to 88 (pass is always OK), stamp and goodbye 88 to 90. Think harder, Go further and the Investigation are open to every child. The tutor never announces who is on which page, and never splits a pair unless both children agree. Invite the WHOLE group, never one child: "when you have finished Start here you can choose Think harder, Go further or the Investigation."'))

# ---------- 2. warm-up: guess the angle ----------
V=(190,250); cards=''
guess=[('A',120),('B',30),('C',150),('D',90)]
for i,(nm,th) in enumerate(guess):
    a=(V[0]+140,V[1]); b=P(V[0],V[1],170,th)
    g=line(V,a)+line(V,b)+f'<path d="M{V[0]+40} {V[1]} A40 40 0 0 0 {P(V[0],V[1],40,th)[0]:.1f} {P(V[0],V[1],40,th)[1]:.1f}" fill="none" stroke="{RED}" stroke-width="5"/>'+txt(20,44,nm,44,TEAL)
    chk(V,a,b,th,'warm '+nm)
    L=128+i*430
    cards+=pin(L,390,340,svgwrap(340,290,f'Angle {nm}, to be estimated',g),None,WHITE,24,'4px 12px')
    cards+=pin(L,790,340,p(f'{nm} = {th}°',44,800),'pop',YEL,20,'14px 24px')
body=h2('Warm-up: Guess the Angle')+card(p('No protractor! A paper corner is 90°. Fold it: 45°. Guess A, B, C, D.',36,700),extra='padding:24px 40px')+cards
put('p5l8-warm1',sec('p5l8-warm1','0–4 MIN',body,
 'Minutes 0 to 4. Guess the Angle. Children hold up a corner of paper (90°) and a folded corner (45°) to the screen to compare. They write four guesses on whiteboards. Click to reveal each true size. Answers: A = 120°, B = 30°, C = 150°, D = 90°. '
 'Ask: "Which was easiest? Why?" (90° is a square corner.) "Is C bigger or smaller than a straight line?" (smaller: a straight line is 180°.) Score: a guess within 10° is a point. '
 'Listen for children comparing with 90° and 45°: that is estimating with a benchmark, the same skill as in Lesson 1. Do not use the protractor yet.'))

# ---------- 3. quick questions ----------
qs=[('1.','Straight line: 180° − 125° = ?','55°'),('2.','At a point: 150°, 90°, 80° and one more. Find it.','40°'),('3.','A triangle has angles 90° and 35°. Third angle?','55°'),('4.','Isosceles triangle, top angle 40°. One base angle?','70°'),('5.','A parallelogram has a 70° angle. The angle next to it?','110°')]
body=h2('Quick questions')+''.join(qrow(128,250+i*125,1250,a,b,36) for i,(a,b,c) in enumerate(qs))+''.join(answer(1420,250+i*125,372,c) for i,(a,b,c) in enumerate(qs))
put('p5l8-warm2',sec('p5l8-warm2','4–9 MIN',body,'Minutes 4 to 9. Read each aloud, whiteboards up together, then click to show. Ask "What is your reason?" each time. 1) Angles on a straight line add up to 180°: 55°. 2) Angles at a point add up to 360°: 150 + 90 + 80 = 320, so 40°. 3) Angles in a triangle add up to 180°: 180 − 90 − 35 = 55°. 4) The two base angles are equal: (180 − 40) ÷ 2 = 70°. 5) Neighbouring angles of a parallelogram add up to 180°: 110°. Answers: 55°, 40°, 55°, 70°, 110°.'))

# ---------- 4. explore: what to do ----------
Bp=(30,200); Cp=(Bp[0]+190,200)
# triangle with angles B=60, C=70, A=50: A from B at 60 deg and from C at 110 deg (maths)
cx=190*math.sin(rad(70))/math.sin(rad(50)); Ap=P(Bp[0],Bp[1],cx,60)
chk(Bp,Cp,Ap,60,'tri B'); chk(Cp,Bp,Ap,70,'tri C'); chk(Ap,Bp,Cp,50,'tri A')
def corner(v,a,b,r,fill):
    a1=math.atan2(a[1]-v[1],a[0]-v[0]); a2=math.atan2(b[1]-v[1],b[0]-v[0]); d=a2-a1
    while d>math.pi: d-=2*math.pi
    while d<-math.pi: d+=2*math.pi
    p1=(v[0]+r*math.cos(a1),v[1]+r*math.sin(a1)); p2=(v[0]+r*math.cos(a2),v[1]+r*math.sin(a2))
    return f'<path d="M{v[0]:.1f} {v[1]:.1f} L{p1[0]:.1f} {p1[1]:.1f} A{r} {r} 0 0 {1 if d>0 else 0} {p2[0]:.1f} {p2[1]:.1f} Z" fill="{fill}" stroke="{NAVY}" stroke-width="3"/>'
g=poly([Ap,Bp,Cp],WHITE,4)+corner(Ap,Bp,Cp,52,RED)+corner(Bp,Cp,Ap,52,BLUE)+corner(Cp,Bp,Ap,52,GREEN)
cen=(640,200); g+=sector(cen,130,0,70,GREEN)+sector(cen,130,70,130,BLUE)+sector(cen,130,130,180,RED)+line((cen[0]-160,cen[1]),(cen[0]+160,cen[1]),NAVY,5)
g+=txt(cen[0],cen[1]+40,'a straight line',26,TEAL,'middle',700,'Nunito Sans, Arial')
steps=''.join(f'<li>{E(s)}</li>' for s in ['Draw any triangle and colour its three corners red, blue and green.','Predict: what will happen when you tear off the three corners and put them side by side, points touching?','Tear them off and fit them together. Now do it with a four-sided shape (four corners).','Say what you notice. Does it work for every triangle?'])
body=h2('Explore: tear it up')+card(chip('EXPLORE')+f'<ol style="font-size:32px;font-weight:600;padding-left:52px;display:flex;flex-direction:column;gap:6px">{steps}</ol>')
body+=card(svgwrap(860,250,'A triangle with three coloured corners and, next to it, the three corners fitted side by side along a straight line',g,0.84),extra='padding:6px 32px')
put('p5l8-explore1',sec('p5l8-explore1','9–14 MIN',body,'Minutes 9 to 14. Children draw a triangle (any shape: one fat, one thin, one with a right angle is best), colour the corners and tear them off. They must predict first (thumbs: a straight line, a curve, a gap?). Then they fit the corners together with the points touching: the three corners make a straight line. '
 'Then the four-sided shape: the four corners fit round a point. Anyone who wants more (open to every pair): a different triangle. Is it still a straight line? Online: children hold the torn corners up to the camera. Protractor optional: measure the three corners of one triangle and add them up (they will be close to 180°, not exact: that is the nature of measuring).'))

# ---------- 5. explore: talk ----------
body=h2('Explore: talk about it')+numcards([('1.','Where did the three corners of the triangle fit? What does that tell you?'),('2.','Where did the four corners of the four-sided shape fit? What does that tell you?'),('3.','Does it work for every triangle? How could you find out?')],40)
put('p5l8-explore2',sec('p5l8-explore2','14–21 MIN',body,'Minutes 14 to 21. Let pairs share, then collect. Answers: 1) The three corners make a straight line, so the angles of a triangle add up to 180°. 2) The four corners fit round a point, so the angles of a four-sided shape add up to 360°. 3) Test very different triangles: a fat one, a thin one, a right-angled one. It works every time. Say: "This is a fact we can use to FIND angles without measuring." '
 'Extension: why is it 360°? Draw a line from one corner to the opposite corner: two triangles, 2 × 180° = 360°. Do not teach the method for the worksheet yet: the next slides do that.'))

# ---------- 6. teach: the toolkit ----------
def mini(kind):
    if kind=='line':
        a=(30,150); b=(330,150); O=(180,150); r=P(180,150,130,65)
        chk(O,a,r,115,'t1'); chk(O,b,r,65,'t1b')
        return line(a,b)+line(O,r)+arc(O,b,r,46,'65°',RED,84,28)+arc(O,a,r,46,'115°',RED,100,28),'two angles on a straight line'
    if kind=='point':
        O=(180,90); rs=[P(*O,80,0),P(*O,80,100),P(*O,80,200),P(*O,80,290)]
        chk(O,rs[0],rs[1],100,'t2');chk(O,rs[1],rs[2],100,'t2b');chk(O,rs[2],rs[3],90,'t2c');chk(O,rs[3],rs[0],70,'t2d')
        return ''.join(line(O,r) for r in rs)+arc(O,rs[0],rs[1],24,'100°',RED,58,26)+arc(O,rs[1],rs[2],24,'100°',RED,60,26)+arc(O,rs[2],rs[3],24,'90°',RED,60,26)+arc(O,rs[3],rs[0],24,'?',RED,54,26),'four angles round a point'
    if kind=='vo':
        O=(180,90); A=P(*O,100,210); B=P(*O,100,30); C=P(*O,100,140); Dd=P(*O,100,320)
        chk(O,A,C,70,'t3'); chk(O,B,Dd,70,'t3b'); 
        return line(A,B)+line(C,Dd)+arc(O,A,C,26,'70°',RED,64,26)+arc(O,B,Dd,26,'70°',RED,64,26),'two crossing lines'
    if kind=='tri':
        B=(90,165); C=(270,165); A=P(*B,180*math.sin(rad(70))/math.sin(rad(50)),60)
        chk(A,B,C,50,'t4'); chk(B,C,A,60,'t4b'); chk(C,B,A,70,'t4c')
        return poly([A,B,C],WHITE,4)+arc(A,B,C,34,'50°',RED,66,26)+arc(B,C,A,34,'60°',RED,66,26)+arc(C,B,A,34,'70°',RED,66,26),'a triangle'
    if kind=='iso':
        A=(180,12); h=140; hb=h*math.tan(rad(36)); B=(180-hb,12+h); C=(180+hb,12+h)
        chk(A,B,C,72,'t5'); chk(B,A,C,54,'t5b')
        return poly([A,B,C],WHITE,4)+tick(A,B)+tick(A,C)+arc(A,B,C,34,'72°',RED,68,26)+arc(B,A,C,34,'54°',RED,68,26)+arc(C,B,A,34,'54°',RED,68,26),'isosceles triangle'
    if kind=='eq':
        A=(180,12); h=140; hb=h*math.tan(rad(30)); B=(180-hb,12+h); C=(180+hb,12+h)
        chk(A,B,C,60,'t6')
        return poly([A,B,C],WHITE,4)+tick(A,B)+tick(A,C)+tick(B,C)+arc(A,B,C,34,'60°',RED,66,26)+arc(B,A,C,34,'60°',RED,66,26)+arc(C,B,A,34,'60°',RED,66,26),'equilateral triangle'
cardsd=[('line','Angles on a straight line add up to 180°.'),('point','Angles at a point add up to 360°.'),('vo','Vertically opposite angles are equal.'),('tri','Angles in a triangle add up to 180°.'),('iso','Isosceles: the two base angles are equal.'),('eq','Equilateral: all three angles are 60°.')]
body=h2('Your angle toolkit: facts we can give as reasons')
for i,(k,t) in enumerate(cardsd):
    g,lab=mini(k); L=128+(i%3)*567; T=225+(i//3)*340
    inner=svgwrap(360,170,lab,g)+p(t,30,700)
    body+=pin(L,T,486,inner,None,WHITE,24,'8px 24px','gap:4px;height:300px;box-sizing:content-box;align-items:center;text-align:center')
put('p5l8-teach1',sec('p5l8-teach1','21–23 MIN',body,'Teach. These six facts are the reasons children will give all lesson. Read each card and ask children to say it back before you move on. '
 '1) Straight line: 65° and 115° make 180°. 2) Point: 100 + 100 + 90 = 290, so the missing angle is 360 − 290 = 70°. 3) Vertically opposite: lines that cross make two pairs of equal angles (show it by folding paper or by turning a pair of sticks). 4) Triangle: 50 + 60 + 70 = 180 (like the corners we tore). '
 '5) Isosceles: two equal sides, and the two angles at the bottom (the base angles) are equal. 36 + 72 + 72 = 180 is another example; here 72 + 54 + 54 = 180. 6) Equilateral: three equal sides and three 60° angles. '
 'Say: "A reason is one of these facts. Today every angle we find gets a reason."'))

# ---------- 7. worked example: PQR ----------
Q=(40,250); s=250
Sp=(Q[0]+s,Q[1]); QP=s*math.sin(rad(75))/math.sin(rad(55)); Pp=P(*Q,QP,50)
PS=s*math.sin(rad(50))/math.sin(rad(55)); SR=PS*math.sin(rad(45))/math.sin(rad(30)); Rp=(Sp[0]+SR,Q[1])
chk(Q,Sp,Pp,50,'Q');chk(Sp,Q,Pp,75,'PSQ');chk(Rp,Sp,Pp,30,'R');chk(Pp,Q,Sp,55,'QPS');chk(Pp,Sp,Rp,45,'SPR');chk(Sp,Pp,Rp,105,'PSR');chk(Pp,Q,Rp,100,'QPR')
W1,H1=700,300
base=(poly([Pp,Q,Rp],SKY,5)+line(Pp,Sp)+arc(Q,Sp,Pp,50,'50°',RED,84,28)+arc(Sp,Q,Pp,34,'75°',RED,70,28)+arc(Rp,Sp,Pp,60,'30°',RED,100,28)
      +pl(Pp,'P',0,-14)+pl(Q,'Q',-18,30)+pl(Sp,'S',0,40)+pl(Rp,'R',22,30))
ov1=svgwrap(W1,H1,'angle QPS marked 55 degrees',arc(Pp,Q,Sp,70,'55°',BLUE,116,28))
ov2=svgwrap(W1,H1,'angle PSR marked 105 degrees',arc(Sp,Pp,Rp,36,'105°',BLUE,76,28))
ov3=svgwrap(W1,H1,'angle SPR marked 45 degrees',arc(Pp,Sp,Rp,70,'45°',BLUE,112,28))
ov4=svgwrap(W1,H1,'the check: angle QPR is 100 degrees',arc(Pp,Q,Rp,100,'',TEAL,0,28,4))
body=h2('Worked example: an angle chase with reasons')+p('P is a corner. S is a point on the line QR. Find angles QPS, PSR and SPR.',34,600,MUTED)
body+=pin(128,330,W1,svgwrap(W1,H1,'Triangle PQR with S a point on QR and the line PS drawn. Angle Q is 50 degrees, angle PSQ is 75 degrees and angle R is 30 degrees.',base),None)
body+=ostep(128,330,1,'Angle QPS = 180° − 50° − 75° = 55°.   Reason: angles in a triangle add up to 180°.',ov1,W1,H1,dx=740,dy=0,tw=924,size=30)
body+=ostep(128,330,2,'Angle PSR = 180° − 75° = 105°.   Reason: angles on a straight line add up to 180°.',ov2,W1,H1,dx=740,dy=125,tw=924,size=30)
body+=ostep(128,330,3,'Angle SPR = 180° − 105° − 30° = 45°.   Reason: angles in a triangle add up to 180°.',ov3,W1,H1,dx=740,dy=250,tw=924,size=30)
body+=ostep(128,330,4,'Check: angle QPR = 55° + 45° = 100°, and 50° + 100° + 30° = 180° ✓',ov4,W1,H1,dx=740,dy=375,tw=924,size=30)
put('p5l8-we1',sec('p5l8-we1','23–26 MIN',body,'Click to reveal each step and its arc on the figure. Ask children to say the step before each click. Write the reason every time: that is the whole lesson. '
 'Think-aloud: "I know two angles in triangle PQS: 50 and 75. The three angles in a triangle add up to 180, so the third one, QPS, is 55. Reason: angles in a triangle." Step 2: "S is on the line QR, so angle PSQ and angle PSR sit on a straight line: 180 − 75 = 105." Step 3: "Now triangle PSR has 105 and 30, so SPR is 180 − 135 = 45." '
 'Step 4 is a check: the whole angle at P (QPR) is 55 + 45 = 100, so triangle PQR has 50 + 100 + 30 = 180. Ask: "Is the drawing to scale?" (No: never measure. We use facts.)'))
put('p5l8-try1',try_slide('p5l8-try1','26–27 MIN','Your turn: give the reason','Find the angle. Say which fact you used. Click to check.',[('a','Two angles on a straight line. One is 112°. The other?','68°'),('b','An isosceles triangle has a top angle of 36°. Each base angle?','72°'),('c','A parallelogram has a 65° angle. The angle next to it?','115°')],
 'Whiteboards: answer AND reason. a) 180° − 112° = 68° (straight line). b) 180° − 36° = 144°, 144° ÷ 2 = 72° (isosceles: base angles equal; triangle 180°). c) 180° − 65° = 115° (neighbouring angles of a parallelogram add up to 180°). Ask: "Which reason did you give?" Accept any correct fact.',size=36))

# ---------- 9. the shapes ----------
def shapes(kind):
    if kind=='para':
        A=(34,190); B=(A[0]+250,190); Dd=P(*A,150,70); C=(Dd[0]+250,Dd[1])
        chk(A,B,Dd,70,'p1'); chk(B,A,C,110,'p2'); chk(C,B,Dd,70,'p3'); chk(Dd,A,C,110,'p4')
        return (poly([A,B,C,Dd],SKY,4)+tick(A,B)+tick(Dd,C)+tick(A,Dd,2)+tick(B,C,2)+arc(A,B,Dd,32,'70°',RED,66,26)+arc(C,B,Dd,32,'70°',RED,62,26)
                +arc(Dd,A,C,32,'110°',RED,70,26)+arc(B,A,C,32,'110°',RED,70,26)),'a parallelogram with angles 70 and 110 degrees'
    if kind=='rh':
        s=170; A=(100,190); B=(A[0]+s,190); Dd=P(*A,s,76); C=(Dd[0]+s,Dd[1])
        chk(A,B,Dd,76,'r1'); chk(B,A,C,104,'r2')
        return (poly([A,B,C,Dd],SKY,4)+tick(A,B)+tick(B,C)+tick(C,Dd)+tick(Dd,A)+arc(A,B,Dd,32,'76°',RED,70,26)+arc(B,A,C,32,'104°',RED,72,26)),'a rhombus with angles 76 and 104 degrees'
    A=(110,34); Bq=(A[0]+230,A[1]); Dd=P(*A,150,260)  # AD leaves A at 260 maths-degrees: angle DAB = 100
    L2=(Dd[1]-Bq[1])/math.sin(rad(65)); BC=P(*Bq,L2,245); Cc=(BC[0],Dd[1])
    chk(A,Bq,Dd,100,'t1'); chk(Bq,A,Cc,65,'t2'); chkpar(A,Bq,Dd,Cc,'trap'); chk(Dd,A,Cc,80,'t3'); chk(Cc,Bq,Dd,115,'t4')
    return (poly([A,Bq,Cc,Dd],SKY,4)+parr(A,Bq)+parr(Dd,Cc)+arc(A,Bq,Dd,32,'100°',RED,76,26)+arc(Bq,A,Cc,32,'65°',RED,62,26)+arc(Dd,A,Cc,32,'80°',RED,60,26)+arc(Cc,Bq,Dd,32,'115°',RED,74,26)),'a trapezium with one pair of parallel sides'
body=h2('Four-sided shapes: what do we know?')
texts=[('para','Parallelogram','Opposite angles are equal. Neighbouring angles add up to 180°.'),('rh','Rhombus','A parallelogram with 4 equal sides. Neighbouring angles add up to 180°.'),('trap','Trapezium','One pair of parallel sides. Angles between the parallel sides add up to 180°.')]
for i,(k,nm,t) in enumerate(texts):
    g,lab=shapes(k); L=128+i*567
    body+=pin(L,250,486,p(nm,44,800,TEAL)+svgwrap(400,230,lab,g,0.98)+p(t,30,700),None,WHITE,24,'14px 24px','gap:6px;box-sizing:content-box;height:480px')
body+=soft(128,810,1664,'Between the parallel sides, the angles on one slanted side add up to 180°: for example 100° + 80° = 180°.',32,'fade')
put('p5l8-teachshapes',sec('p5l8-teachshapes','27–28 MIN',body,'Teach. Show each shape and ask: "What do you notice about the angles?" Parallelogram: opposite angles are equal (70° and 70°, 110° and 110°) and neighbouring angles add up to 180° (70 + 110). Rhombus: it is a parallelogram with all four sides equal, so the same angle facts, AND its equal sides make isosceles triangles when we draw a diagonal. '
 'Trapezium: only one pair of parallel sides (the arrows). Each slanted side joins the two parallel sides, and the two angles on it add up to 180°: 100 + 80 and 65 + 115. Check: 100 + 65 + 115 + 80 = 360, the angles in any four-sided shape. Click to show the last line.'))

# ---------- 10. worked example: rhombus ----------
s=300; A=(30,270); B=(A[0]+s,A[1]); Dd=P(*A,s,50); C=(Dd[0]+s,Dd[1])
chk(A,B,Dd,50,'rh A'); chk(B,A,C,130,'rh B'); chk(B,A,Dd,65,'ABD'); chk(B,Dd,C,65,'DBC'); chkeq(A,B,A,Dd,'AB AD')
W2,H2=560,310
base=(poly([A,B,C,Dd],SKY,5)+line(B,Dd,TEAL,5,'10 7')+tick(A,B)+tick(B,C)+tick(C,Dd)+tick(Dd,A)+arc(A,B,Dd,50,'50°',RED,88,28)
      +pl(A,'A',-20,34)+pl(B,'B',22,34)+pl(C,'C',26,10)+pl(Dd,'D',-22,10))
ov1=svgwrap(W2,H2,'angle ABC marked 130 degrees',arc(B,A,C,100,'130°',BLUE,138,28))
ov2=svgwrap(W2,H2,'angles ABD and ADB marked 65 degrees',arc(B,A,Dd,44,'65°',GREEN,76,28)+arc(Dd,A,B,52,'65°',GREEN,92,28))
ov3=svgwrap(W2,H2,'angle DBC marked 65 degrees',arc(B,Dd,C,44,'65°',GREEN,76,28))
body=h2('Worked example: the rhombus and its diagonal')+p('ABCD is a rhombus. Angle DAB = 50°. The diagonal BD is drawn. Find angle ABC, then angle ABD, then angle DBC.',32,600,MUTED)
body+=pin(128,330,W2,svgwrap(W2,H2,'Rhombus ABCD with angle DAB 50 degrees, all four sides equal, and the diagonal BD drawn dashed',base),None)
body+=ostep(128,330,1,'Angle ABC = 180° − 50° = 130°.   Reason: neighbouring angles of a rhombus add up to 180°.',ov1,W2,H2,dx=640,dy=0,tw=1024,size=30)
body+=ostep(128,330,2,'Triangle ABD: AB = AD (all sides of a rhombus are equal). Angle ABD = (180° − 50°) ÷ 2 = 65°.   Reason: base angles of an isosceles triangle.',ov2,W2,H2,dx=640,dy=120,tw=1024,size=30)
body+=ostep(128,330,3,'Angle DBC = 130° − 65° = 65°.   The diagonal cuts the 130° angle into two equal parts.',ov3,W2,H2,dx=640,dy=270,tw=1024,size=30)
put('p5l8-we2',sec('p5l8-we2','28–31 MIN',body,'Click to reveal each step. Step 1: neighbouring angles of a rhombus (a parallelogram) add up to 180°. Step 2: ask first "Which sides are equal?" All four sides of a rhombus are equal, so AB = AD and triangle ABD is isosceles with apex A = 50°. The base angles are (180 − 50) ÷ 2 = 65° each. '
 'Step 3: angle ABC is 130° and ABD is 65°, so DBC = 65° too. Notice the diagonal cuts the angle into two equal parts: true for every rhombus. Think-aloud: "A diagonal turns a four-sided shape into triangles. Triangles are where my facts live." Check: triangle BCD is also isosceles (BC = CD): angle C = 50°, so 50 + 65 + 65 = 180 ✓.'))
put('p5l8-try2',try_slide('p5l8-try2','31–32 MIN','Your turn: shapes','Find the angles. Say your reasons. Click to check.',[('a','Parallelogram with a 65° angle. The other three angles?','115°, 65°, 115°'),('b','Trapezium ABCD, AB parallel to DC. Angle A = 95°, angle B = 60°. Find D and C.','D = 85°, C = 120°'),('c','Rhombus with a 120° angle. The other three angles?','60°, 120°, 60°')],
 'Whiteboards: angles AND reasons. a) 65° opposite, and 180° − 65° = 115° twice. b) D = 180° − 95° = 85°; C = 180° − 60° = 120° (angles between the parallel sides add up to 180°). Check: 95 + 60 + 120 + 85 = 360 ✓. c) 180° − 120° = 60°, and opposite angles equal: 60°, 120°, 60°.',size=34))

# ---------- 11. key ----------
body=h2('Key idea: one angle, one reason')+card(p('Find one angle. Say WHY. Use it to find the next one. That is an angle chase.',44,700))+card(p('Do not measure the drawing. Use the facts: straight line 180°, point 360°, triangle 180°, equal base angles, and the shape facts.',38,600,MUTED))
put('p5l8-key',sec('p5l8-key','32–33 MIN',body,'Say the key idea together. Common mistakes to watch for during the worksheet: (1) Measuring or guessing from the picture instead of using an angle fact: drawings are not to scale. (2) Calling the wrong angles equal in an isosceles triangle: the equal angles are the base angles, opposite the equal sides, not the angle between the equal sides. (3) Giving only one case when one angle of an isosceles triangle is known (the given angle could be the top angle or a base angle).'))
put('p5l8-break',break_slide('p5l8-break','33–37 MIN','Angle statues. The tutor calls an angle and children make it with their arms: 90° is an L, 180° is arms straight out, 45° is half an L. Then: 360°, a full turn!','Five minutes. Online: children make the angle with their arms on camera. Ask: "Show me 180° with ONE arm and the floor." Let a child be the caller. Call 270° (three quarters of a turn) as a surprise. Then a drink of water.'))

# ---------- worksheet page 1 ----------
put('p5l8-ws1',ws_preview('p5l8-ws1','37–49 MIN','Worksheet page 1: with your partner',[('Q1','Crossing lines and four angles round a point. Say the angle fact you used.'),('Q2','A parallelogram, a rhombus with a diagonal, and a trapezium.')],'Stuck? Write down every angle you know first. Then look for a straight line, a triangle or equal sides.','Minutes 37 to 49. Walk around. Ask "What is your reason?" before giving any help. Q2b: the hint says PQ = QR, so triangle PQR is isosceles with the 116° angle at the top. Remind children that the drawings are not to scale.'))
put('p5l8-ws1ans',checks('p5l8-ws1ans','49–51 MIN','Page 1: check together',[('Q1','a) 112°   b) 68°   c) 112°   d) 65° (360° − 95° − 130° − 70°)'),('Q2','a) B = 108°, C = 72°, D = 108°   b) PQR = 116°, QPR = 32°   c) D = 70°, C = 100°')],
 'Click after a pair explains theirs, with the REASON. Q1a: 180° − 68° = 112° (straight line). Q1b: vertically opposite angle to AOC. Q1c: vertically opposite BOC. Q1d: angles at a point add up to 360°. Q2a: neighbouring angles add up to 180° (108°), opposite angles equal (72°, 108°). Q2b: neighbouring angles of the rhombus: 180° − 64° = 116°; triangle PQR has PQ = QR, so the base angles are equal: (180° − 116°) ÷ 2 = 32°. Q2c: angles between the parallel sides AB and DC add up to 180°: D = 180° − 110° = 70°, C = 180° − 80° = 100°. Check: 110 + 80 + 100 + 70 = 360.',gapy=190,size=34))

# ---------- teach: chain, isosceles inside a triangle ----------
L=260; Dd=(230,290); Cc=(Dd[0]+L,290); Aa=P(*Dd,L,110); DB=L*math.sin(rad(45))/math.sin(rad(65)); Bb=(Dd[0]-DB,290)
chkeq(Dd,Aa,Dd,Cc,'DA DC'); chk(Cc,Dd,Aa,35,'C'); chk(Aa,Bb,Dd,45,'BAD'); chk(Dd,Aa,Cc,110,'ADC'); chk(Dd,Aa,Bb,70,'ADB'); chk(Bb,Aa,Dd,65,'B'); chk(Aa,Dd,Cc,35,'DAC')
W3,H3=560,330
base=(poly([Aa,Bb,Cc],SKY,5)+line(Aa,Dd)+tick(Dd,Aa)+tick(Dd,Cc)+arc(Cc,Dd,Aa,48,'35°',RED,92,28)+arc(Aa,Bb,Dd,60,'45°',RED,96,28)
      +pl(Aa,'A',0,-16)+pl(Bb,'B',-18,32)+pl(Dd,'D',0,42)+pl(Cc,'C',22,32))
ov1=svgwrap(W3,H3,'angle DAC marked 35 degrees',arc(Aa,Dd,Cc,80,'35°',BLUE,128,28))
ov2=svgwrap(W3,H3,'angle ADC marked 110 degrees',arc(Dd,Aa,Cc,40,'110°',BLUE,78,28))
ov3=svgwrap(W3,H3,'angle ADB marked 70 degrees',arc(Dd,Aa,Bb,40,'70°',GREEN,74,28))
ov4=svgwrap(W3,H3,'angle ABD marked 65 degrees',arc(Bb,Aa,Dd,48,'65°',BLUE,92,28))
body=h2('Chain: an isosceles triangle inside')+p('D is on BC. DA = DC. Angle C = 35° and angle BAD = 45°. Find angle DAC, ADC, ADB and ABD.',32,600,MUTED)
body+=pin(128,330,W3,svgwrap(W3,H3,'Triangle ABC. D is a point on BC with DA equal to DC. Angle C is 35 degrees and angle BAD is 45 degrees.',base),None)
body+=ostep(128,330,1,'Angle DAC = 35°.   Reason: DA = DC, so the base angles are equal.',ov1,W3,H3,dx=620,dy=0,tw=1044,size=30)
body+=ostep(128,330,2,'Angle ADC = 180° − 35° − 35° = 110°.   Reason: angles in a triangle.',ov2,W3,H3,dx=620,dy=105,tw=1044,size=30)
body+=ostep(128,330,3,'Angle ADB = 180° − 110° = 70°.   Reason: angles on a straight line.',ov3,W3,H3,dx=620,dy=210,tw=1044,size=30)
body+=ostep(128,330,4,'Angle ABD = 180° − 45° − 70° = 65°.   Reason: angles in a triangle.',ov4,W3,H3,dx=620,dy=315,tw=1044,size=30)
put('p5l8-teachchain',sec('p5l8-teachchain','51–53 MIN',body,'Teach before worksheet page 2 (Q3 is a chain with an isosceles triangle; this one has different angles and the equal sides are different). Ask first: "Which two sides are equal? So which two angles are equal?" DA = DC, so the equal angles are the ones opposite them: angle C and angle DAC. '
 'Click 1: DAC = 35°. Click 2: triangle ADC: 180 − 35 − 35 = 110°. Click 3: B, D, C are on a straight line, so ADB + ADC = 180°: 70°. Click 4: triangle ABD has 45° and 70°, so ABD = 65°. Check: triangle ABC has B = 65, C = 35 and angle BAC = 45 + 35 = 80: 65 + 35 + 80 = 180 ✓. '
 'Say: "A chain: each angle helps me find the next, and each has a reason."'))

# ---------- teach: parallelogram with an isosceles triangle ----------
Z=(200,290); Y=(560,290); X=(380,290-180*math.tan(rad(55))); Wp=(20,X[1])
chkeq(X,Y,X,Z,'XY XZ'); chkpar(Wp,X,Z,Y,'WX ZY'); chkpar(X,Y,Wp,Z,'XY WZ')
chk(Y,X,Z,55,'Y'); chk(Z,X,Y,55,'XZY'); chk(X,Y,Z,70,'YXZ'); chk(X,Wp,Y,125,'WXY'); chk(X,Wp,Z,55,'WXZ'); chk(Wp,X,Z,55,'W')
W4,H4=600,345
base=(poly([Wp,X,Y,Z],SKY,5)+line(X,Z,TEAL,5,'10 7')+tick(X,Y)+tick(X,Z)+arc(Y,X,Z,48,'55°',RED,92,28)
      +pl(Wp,'W',-20,10)+pl(X,'X',0,-16)+pl(Y,'Y',24,34)+pl(Z,'Z',-4,44))
ov1=svgwrap(W4,H4,'angle XZY marked 55 degrees',arc(Z,X,Y,56,'55°',BLUE,96,28))
ov2=svgwrap(W4,H4,'angle YXZ marked 70 degrees',arc(X,Y,Z,52,'70°',BLUE,92,28))
ov3=svgwrap(W4,H4,'angle WXY marked 125 degrees',arc(X,Wp,Y,86,'125°',GREEN,128,28,4))
ov4=svgwrap(W4,H4,'angle WXZ marked 55 degrees',arc(X,Wp,Z,40,'55°',BLUE,72,28))
body=h2('A parallelogram with an isosceles triangle')+p('WXYZ is a parallelogram. XY = XZ. Angle XYZ = 55°. Find angle XZY, YXZ, WXY and WXZ.',32,600,MUTED)
body+=pin(128,330,W4,svgwrap(W4,H4,'Parallelogram WXYZ with the diagonal XZ drawn. XY equals XZ and angle XYZ is 55 degrees.',base),None)
body+=ostep(128,330,1,'Angle XZY = 55°.   Reason: XY = XZ, so the base angles are equal.',ov1,W4,H4,dx=660,dy=0,tw=1004,size=30)
body+=ostep(128,330,2,'Angle YXZ = 180° − 55° − 55° = 70°.   Reason: angles in a triangle.',ov2,W4,H4,dx=660,dy=115,tw=1004,size=30)
body+=ostep(128,330,3,'Angle WXY = 180° − 55° = 125°.   Reason: neighbouring angles of a parallelogram.',ov3,W4,H4,dx=660,dy=230,tw=1004,size=30)
body+=ostep(128,330,4,'Angle WXZ = 125° − 70° = 55°.   The big angle WXY is made of WXZ and ZXY.',ov4,W4,H4,dx=660,dy=345,tw=1004,size=30)
put('p5l8-teachcombo',sec('p5l8-teachcombo','53–55 MIN',body,'Teach before worksheet page 2 (Q4 is a parallelogram with an isosceles triangle; the shape here is different). Ask first: "Which two sides are equal, XY and XZ. Which angles are opposite them?" Angle XZY (opposite XY) and angle XYZ (opposite XZ): both 55°. '
 'Click 1: 55°. Click 2: triangle XYZ: 180 − 110 = 70°. Click 3: in the parallelogram neighbouring angles add up to 180°, so angle WXY = 180 − 55 = 125°. Click 4: angle WXY is made of two smaller angles, WXZ and ZXY, so WXZ = 125 − 70 = 55°. '
 'Check: triangle WXZ: angle W is 55° (opposite angle to Y), and 55 + 55 = 110, so angle WZX = 70°, which with XZY = 55° makes angle Z = 125° ✓ (neighbouring angles Y and Z add up to 180°).'))

# ---------- teach: find every case ----------
A1=(150,20); h=200; hb=h*math.tan(rad(35)); B1=(150-hb,20+h); C1=(150+hb,20+h)
chk(A1,B1,C1,70,'c1'); chk(B1,A1,C1,55,'c1b')
g1=poly([A1,B1,C1],SKY,5)+tick(A1,B1)+tick(A1,C1)+arc(A1,B1,C1,40,'70°',RED,72,28)+arc(B1,A1,C1,44,'55°',BLUE,86,28)+arc(C1,B1,A1,44,'55°',BLUE,86,28)
B2=(60,262); C2=(240,262); A2=(150,262-90*math.tan(rad(70)))
chk(B2,A2,C2,70,'c2'); chk(A2,B2,C2,40,'c2b')
g2=poly([A2,B2,C2],SKY,5)+tick(A2,B2)+tick(A2,C2)+arc(B2,A2,C2,30,'70°',RED,64,28)+arc(C2,B2,A2,30,'70°',BLUE,64,28)+arc(A2,B2,C2,40,'40°',BLUE,72,28)
body=h2('Only one angle given: try every case')+p('An isosceles triangle has one angle of 70°. What could the other two angles be?',34,700)
body+=pin(128,330,816,svgwrap(300,270,'Isosceles triangle with the top angle 70 degrees and two base angles of 55 degrees',g1)+p('Case 1: 70° is the TOP angle.',32,800,TEAL)+p('180° − 70° = 110°, and 110° ÷ 2 = 55° each.',30,600)+p('55°, 55°, 70°',36,800),'rise',WHITE,24,'16px 28px','align-items:center;gap:8px;box-sizing:border-box;height:480px')
body+=pin(976,330,816,svgwrap(300,270,'Isosceles triangle with two base angles of 70 degrees and a top angle of 40 degrees',g2)+p('Case 2: 70° is a BASE angle.',32,800,TEAL)+p('The other base angle is 70° too: 180° − 140° = 40°.',30,600)+p('70°, 70°, 40°',36,800),'rise',WHITE,24,'16px 28px','align-items:center;gap:8px;box-sizing:border-box;height:480px')
body+=pin(128,830,1664,p('Both work, so there are TWO answers. Check each: 70° + 55° + 55° = 180°, and 70° + 70° + 40° = 180°.',32,700),'fade',SOFT,20,'18px 28px')
put('p5l8-teachcases',sec('p5l8-teachcases','55–57 MIN',body,'Teach before worksheet page 2 (Q5 gives one angle of an isosceles triangle and asks for every case; this example uses a different angle). Ask first: "Is the 70° the top angle or a base angle? We are not told, so we must try both." Click 1: top angle 70°: the other two share 110°, 55° each. Click 2: base angle 70°: the other base angle is also 70°, and the top angle is 180 − 140 = 40°. '
 'Click 3: check both add up to 180°. Your turn (say aloud): "One angle is 80°: list both triangles." Answers: 80°, 80°, 20° and 80°, 50°, 50°. Ask: "Is there always a second case?" (Not always: sometimes a case is impossible. On the worksheet, think about what happens when the given angle is big.) '
 'Strategy to write on the board: TRY EVERY CASE, THEN CHECK EACH ONE.'))

# ---------- worksheet page 2 ----------
put('p5l8-ws2',ws_preview('p5l8-ws2','57–72 MIN','Worksheet page 2: on your own',[('Q3','A chain in triangle ABC with AB = AD. Write a reason (letter A to F) only for (b) and (d).'),('Q4','A parallelogram with an isosceles triangle on its side.'),('Q5','One angle of 50° or 100°: find every isosceles triangle.')],'Want more? Think harder and Go further are at the back of your workbook.','Children work alone. The strip of reasons A to F is printed at the top of page 2: children write a letter (or words) for Q3(b) and (d) only. Note who needs a short catch-up next lesson, especially children who measure, and children who give only one case in Q5.'))
put('p5l8-ws2ans',checks('p5l8-ws2ans','72–76 MIN','Page 2: check together',[('Q3','ADB 62° (AB = AD), BAD 56°, ADC 118° (straight line), ACD 24°'),('Q4','ADC 56°, DEA 62°, AEC 118°, EAB 62°'),('Q5','a) 50°, 50°, 80° and 50°, 65°, 65°   b) Only 100°, 40°, 40°: two 100° angles are too big')],
 'Click after a child explains WITH reasons. Q3: AB = AD, so the base angles ADB and B are equal: 62°. BAD = 180° − 62° − 62° = 56°. ADC = 180° − 62° = 118° (straight line). ACD = 180° − 118° − 38° = 24°. Check: angle BAC = 56° + 38° = 94° and 62° + 94° + 24° = 180° ✓. '
 'Q4: ADC = ABC = 56° (opposite angles). DA = DE: DEA = (180° − 56°) ÷ 2 = 62°. AEC = 180° − 62° = 118° (straight line). Angle DAB = 180° − 56° = 124°; DAE = 62°, so EAB = 124° − 62° = 62°. Q5a: 50° as a base angle gives 50°, 50°, 80°; 50° as the top angle gives 65°, 65°. Q5b: 100° cannot be a base angle (two of them make 200°), so only 100°, 40°, 40°.',gapy=170,size=32))

# ---------- stretch / challenge ----------
st=[('1.','Rhombus ABCD has angle ADC = 130°. The diagonal AC is drawn. Find angle DAC.'),('2.','In a parallelogram one angle is 30° less than the angle next to it. Find all four angles.'),('3.','Two angles of a triangle add up to 110°. What is the third angle? The triangle is isosceles: list every possible set of three angles.')]
put('p5l8-stretch',sec('p5l8-stretch','37–72 MIN  •  OPTION',h2('Think harder')+numcards(st),'Answers: 1) 25°. DA = DC (rhombus), so triangle ADC is isosceles with top angle 130° and base angles (180° − 130°) ÷ 2 = 25°. 2) 75°, 105°, 75°, 105°. Neighbouring angles add up to 180°. 180° − 30° = 150°, 150° ÷ 2 = 75°, so the smaller angle is 75° and the bigger is 105°. '
 '3) The third angle is 180° − 110° = 70°. Isosceles: either the two angles that add up to 110° are equal (55°, 55°, 70°), or one of them equals the third angle, 70°, which makes the other 110° − 70° = 40° (70°, 70°, 40°). Two sets: 55°, 55°, 70° and 40°, 70°, 70°.'))
ch=[('1.','ABC is an isosceles triangle with AB = AC and angle BAC = 40°. D is a point on AC with BD = BC. Find angle ABD.'),('2.','ABCD is a square. E is a point inside it so that ABE is an equilateral triangle. Find angle DEC.')]
put('p5l8-challenge',sec('p5l8-challenge','37–72 MIN  •  OPTION',h2('Go further')+numcards(ch,36),'Pairs try first, then use the "see it" slide if stuck, then the walk-through. These are Go further Q5 and Q6 (Q7, "one angle is 30° bigger than another", is only in the workbook: answer 50°, 50°, 80° or 40°, 70°, 70°). Answers: 1) 30°. 2) 150°.'))
# chdiag
Bc=(100,330); Cc=(320,330); Ac=(210,330-110/math.tan(rad(20)))
chk(Ac,Bc,Cc,40,'A'); chk(Bc,Ac,Cc,70,'B')
u=((Ac[0]-Cc[0])/dist(Ac,Cc),(Ac[1]-Cc[1])/dist(Ac,Cc)); Dc=(Cc[0]+u[0]*2*220*math.cos(rad(70)),Cc[1]+u[1]*2*220*math.cos(rad(70)))
chkeq(Bc,Dc,Bc,Cc,'BD BC'); chkeq(Ac,Bc,Ac,Cc,'AB AC')
g1=poly([Ac,Bc,Cc],SKY,5)+line(Bc,Dc,TEAL,5)+tick(Ac,Bc)+tick(Ac,Cc)+tick(Bc,Dc,2)+tick(Bc,Cc,2)+arc(Ac,Bc,Cc,50,'40°',RED,92,28)+arc(Bc,Ac,Dc,70,'?',RED,100,34)
g1+=pl(Ac,'A',0,-14)+pl(Bc,'B',-22,30)+pl(Cc,'C',24,30)+pl(Dc,'D',30,2)
sidew=300; Aq=(40,340); Bq=(Aq[0]+sidew,340); Cq=(Bq[0],340-sidew); Dq=(Aq[0],340-sidew); Eq=(Aq[0]+sidew/2,340-sidew*math.sin(rad(60)))
chk(Eq,Dq,Cq,150,'DEC'); chkeq(Aq,Bq,Aq,Eq,'AB AE'); chkeq(Aq,Bq,Bq,Eq,'AB BE')
g2=poly([Aq,Bq,Cq,Dq],WHITE,5)+line(Aq,Eq,TEAL,5)+line(Bq,Eq,TEAL,5)+line(Dq,Eq,NAVY,4)+line(Cq,Eq,NAVY,4)+tick(Aq,Eq)+tick(Bq,Eq)+tick(Aq,Bq)+sq(Aq,Bq,Dq)+sq(Bq,Cq,Aq)+sq(Cq,Dq,Bq)+sq(Dq,Aq,Cq)
g2+=arc(Eq,Dq,Cq,30,'?',RED,14,34)+pl(Aq,'A',-22,30)+pl(Bq,'B',24,30)+pl(Cq,'C',24,-8)+pl(Dq,'D',-24,-8)+pl(Eq,'E',0,44)
body=h2('Go further: see it',60)+'<div style="display:flex;gap:32px;align-items:flex-start">'
body+=card(f'<p style="font-size:30px;font-weight:700;color:{TEAL}">Q1: Equal sides everywhere</p>'+svgwrap(440,370,'Isosceles triangle ABC with AB equal to AC and angle A 40 degrees, and D on AC with BD equal to BC',g1,1.12),extra='flex:1;min-width:0;padding:20px 24px;align-items:center')
body+=card(f'<p style="font-size:30px;font-weight:700;color:{TEAL}">Q2: A square and an equilateral triangle</p>'+svgwrap(400,370,'Square ABCD with an equilateral triangle ABE inside it. The lines ED and EC are drawn.',g2,1.12),extra='flex:1;min-width:0;padding:20px 24px;align-items:center')+'</div>'
put('p5l8-chdiag',sec('p5l8-chdiag','37–72 MIN  •  OPTION',body,'Show after pairs have tried Go further, or if they are stuck. The pictures show the problem, not the answer. The tick marks show equal sides. Ask: What do you notice? Which triangles are isosceles? Which angles must be equal? In Q2, how long is AE compared with AD? Answers are in the Go further slide notes.'))
body=h2('Go further: walk-through')+pin(128,250,800,p('Q1: spot the isosceles triangles',34,800,TEAL))
for i,t in enumerate(['AB = AC: angles B and C = (180° − 40°) ÷ 2 = 70°','BD = BC: angle BDC = angle C = 70°','Angle CBD = 180° − 70° − 70° = 40°','Angle ABD = 70° − 40° = 30°']): body+=pin(128,330+i*110,800,p(t,30),'rise',WHITE)
body+=pin(992,250,800,p('Q2: AE = AB = AD, so ADE is isosceles',34,800,TEAL))
for i,t in enumerate(['Angle DAE = 90° − 60° = 30°','Angle AED = (180° − 30°) ÷ 2 = 75°; same for BEC = 75°','Angle AEB = 60° (equilateral)','Round E: 360° − 75° − 75° − 60° = 150°']): body+=pin(992,330+i*110,800,p(t,30),'rise',WHITE)
put('p5l8-chwalk',sec('p5l8-chwalk','37–72 MIN  •  OPTION',body,'Use after pairs have tried. Q1: the tick marks tell us which triangles are isosceles. Triangle ABC: AB = AC with top angle 40°, so B = C = 70°. Triangle BCD: BD = BC, so the angles opposite them are equal: angle BDC = angle BCD = 70°. Then angle CBD = 180° − 140° = 40°. Angle ABD = angle ABC − CBD = 70° − 40° = 30°. '
 'Q2: AB = AE (equilateral) and AB = AD (square), so AE = AD and triangle ADE is isosceles. Angle DAE = angle DAB − angle EAB = 90° − 60° = 30°, so each base angle is 75°. The same happens on the right: BEC = 75°. The four angles round E add up to 360°: DEA 75° + AEB 60° + BEC 75° + the angle DEC: 360° − 210° = 150°.'))

# ---------- talk / exit ----------
body=h2('Talk time')+card(chip('TALK TIME',YEL,NAVY)+p('Ravi says an isosceles triangle can have an angle bigger than 90°. Mei says it cannot. Who is right? Can it have a right angle?',40,600))+card(p('Sentence starters:',34,400,MUTED)+p('“I noticed that …”   “I tested it by …”   “I know because …”',38,600))
put('p5l8-talk',sec('p5l8-talk','76–82 MIN',body,'Minutes 76 to 82. Pairs talk for 2 minutes, then share. Answer: Ravi is right. An isosceles triangle can have one big angle: for example 120°, 30°, 30°. It can also have one right angle: 90°, 45°, 45°. It cannot have two angles of 90° or more, because they would already add up to 180° or more. The two equal BASE angles are always less than 90°, so Mei is right about those. '
 'Second question if time: "How do you know you have found every case?" (we tried the given angle as the top angle and as a base angle). Praise the reasons, not only the answers.'))
body=h2('Exit ticket')+card(chip('EXIT TICKET')+p('In triangle PQR, PQ = PR and angle QPR = 44°. Find angle PQR. Write the reason for each step.',46,600))+card(p('Write your answer on a slip of paper. Show it to your tutor. Then collect your stamp in your inquiry journal.',34,400))
put('p5l8-exit',sec('p5l8-exit','82–90 MIN',body,'Minutes 82 to 90. Answer: 68°. Angles in a triangle add up to 180°: 180° − 44° = 136°. PQ = PR, so the base angles are equal: 136° ÷ 2 = 68°. Accept any clear reasons. Extension: draw a triangle and put the three angle labels 40°, 60° and 80° on the corners. Cut the corners off and fit them together. Now do the same with any four-sided shape. Explain in one sentence why a four-sided shape always gives 360°. (Draw a line from one corner to the opposite corner: two triangles, 2 × 180° = 360°.)'))

# ---------- write ----------
order=['p5l8-title','p5l8-warm1','p5l8-warm2','p5l8-explore1','p5l8-explore2','p5l8-teach1','p5l8-we1','p5l8-try1','p5l8-teachshapes','p5l8-we2','p5l8-try2','p5l8-key','p5l8-break','p5l8-ws1','p5l8-ws1ans','p5l8-teachchain','p5l8-teachcombo','p5l8-teachcases','p5l8-ws2','p5l8-ws2ans','p5l8-stretch','p5l8-challenge','p5l8-chdiag','p5l8-chwalk','p5l8-talk','p5l8-exit']
assert set(order)==set(S), set(order)^set(S)
sd=os.path.join(D,'slides')
for f in os.listdir(sd):
    if f.endswith('.html') and f[:-5] not in S: os.remove(os.path.join(sd,f))
for i,h in S.items(): open(os.path.join(sd,i+'.html'),'w').write(h)
deck={'v':4,'createdOnFiles':{'v':1,'at':datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')},'lists':'css',
 'title':'Math Inquirers P5: Lesson 8 – Angle Chasers','order':order,'cover':'p5l8-title',
 'sections':{'s1':{'description':'Warm-up and explore','start':'p5l8-title'},'s2':{'description':'Teach: angle facts and angle chases','start':'p5l8-teach1'},'s3':{'description':'Worksheet with teaching before page 2','start':'p5l8-break'},'s4':{'description':'Think harder, Go further, talk and exit','start':'p5l8-stretch'}},
 'faces':{'fredoka':{'family':'Fredoka','href':'https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&display=swap'},'nunito-sans':{'family':'Nunito Sans','href':'https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@400;600;700&display=swap'}},
 'designSystems':[]}
json.dump(deck,open(os.path.join(D,'deck.json'),'w'),indent=1,ensure_ascii=False)
print(len(order),'slides')

import p5_gaps; p5_gaps.apply(8)
