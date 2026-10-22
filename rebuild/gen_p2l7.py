"""Math Inquirers Level 2, Lesson 7: Fair Shares (fractions). Writes split/p2l7/project (deck.json + slides/*.html)."""
import json,os,sys,math,re
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,H)
from slidekit import *
import p2gaps
D=os.path.join(H,'..','split','p2l7','project'); os.makedirs(os.path.join(D,'slides'),exist_ok=True); S={}
def put(i,h): S[i]=h
RED='#D64545'; MINT='#D3F1E4'

# ---------- text with stacked fractions: write {3/8} in a string ----------
def fr(a,b,size):
    fs=max(24,round(size*0.8))
    return (f'<span style="display:inline-flex;flex-direction:column;align-items:center;vertical-align:middle;line-height:1;margin:0 5px;font-size:{fs}px">'
            f'<span style="padding:0 5px 3px;border-bottom:3px solid currentColor">{a}</span><span style="padding:3px 5px 0">{b}</span></span>')
def fx(s,size):
    out=''; last=0
    for m in re.finditer(r'\{(\d+)/(\d+)\}',s):
        out+=E(s[last:m.start()])+fr(m.group(1),m.group(2),size); last=m.end()
    return out+E(s[last:])
def P(s,size=40,weight=600,color=None): return p(fx(s,size),size,weight,color,raw=True)
def ansx(left,top,width,text,build='pop',size=40):
    return pin(left,top,width,f'<p style="font-size:{size}px;font-weight:800;line-height:1.2">{fx(text,size)}</p>',build,YEL,20,'18px 26px')
def qrowx(left,top,width,label,text,size=38):
    return pin(left,top,width,f'<p style="font-size:{size}px;font-weight:600;line-height:1.3"><span style="color:{TEAL};font-weight:800">{E(label)}</span>  {fx(text,size)}</p>',None,WHITE,20,'18px 28px')
def stepx(n,text,left=128,top=420,width=1664,build='rise',size=36,bg=WHITE):
    lab=f'<span style="color:{TEAL};font-weight:800">Step {n}.</span>  ' if n else ''
    return pin(left,top,width,f'<p style="font-size:{size}px;font-weight:600;line-height:1.3">{lab}{fx(text,size)}</p>',build,bg,20,'18px 28px')
def soft(left,top,width,text,size=34,build='fade'): return pin(left,top,width,P(text,size,700),build,SOFT,20,'18px 28px')
def stitle(t,size=34): return P(t,size,600,MUTED)
def try_x(sid,time,title,sub,rows,notes,size=38,top=330,gap=150):
    body=h2(title)+stitle(sub)
    for i,(a,b,c) in enumerate(rows): body+=qrowx(128,top+i*gap,1250,a,b,size)+ansx(1420,top+i*gap,372,c)
    return sec(sid,time,body,notes)
def check_x(sid,time,title,rows,notes,lw=200,gap=150,size=36):
    body=h2(title)
    for i,(a,b) in enumerate(rows):
        top=250+i*gap
        body+=pin(128,top,lw-20,f'<p style="font-size:36px;font-weight:800;color:{TEAL}">{E(a)}</p>',None,WHITE,20,'18px 24px')
        body+=ansx(128+lw,top,1664-lw,b,size=size)
    return sec(sid,time,body,notes)
def preview_x(sid,time,title,items,tip,notes):
    inner=''.join(p(f'<span style="color:{TEAL};font-weight:800">{E(a)}</span>  {fx(b,38)}',38,600,raw=True) for a,b in items)
    return sec(sid,time,h2(title)+card(inner)+card(P(tip,34,600,MUTED)),notes)

# ---------- SVG helpers ----------
def SV(w,h,body,label,dw=None,dh=None): return f'<svg aria-label="{E(label)}" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="width:{dw or w}px;height:{dh or h}px;flex:none">{body}</svg>'
def R(x,y,w,h,fill=WHITE,stroke=NAVY,sw=4,rx=0): return f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'
def T(x,y,s,size=40,fill=NAVY,weight=700,anchor='middle'): return f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" fill="{fill}" font-family="Fredoka, Arial">{E(str(s))}</text>'
def L(x1,y1,x2,y2,sw=4,col=NAVY,dash=''): return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{col}" stroke-width="{sw}"{f" stroke-dasharray=\"{dash}\"" if dash else ""} stroke-linecap="round"/>'
def PG(pts,fill=WHITE,stroke=NAVY,sw=4): return f'<polygon points="{" ".join(f"{a:.1f},{b:.1f}" for a,b in pts)}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round"/>'
def CI(x,y,r,fill=WHITE,stroke=NAVY,sw=4): return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'
def TICK(x,y,s=20,col=TEAL,sw=8): return f'<path d="M{x-s} {y} L{x-s/3:.1f} {y+s*0.7:.1f} L{x+s} {y-s*0.8:.1f}" fill="none" stroke="{col}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"/>'
def CROSS(x,y,s=30,col=RED,sw=9): return f'<path d="M{x-s} {y-s} L{x+s} {y+s} M{x+s} {y-s} L{x-s} {y+s}" fill="none" stroke="{col}" stroke-width="{sw}" stroke-linecap="round"/>'
def sfrac(x,yc,a,b,size=36,fill=NAVY):
    w=size*0.62*max(len(str(a)),len(str(b)))+10
    return T(x,yc-size*0.18,a,size,fill)+L(x-w/2,yc,x+w/2,yc,3,fill)+T(x,yc+size*0.86,b,size,fill)
def bar(x,y,w,h,n,shade=(),fill=YEL,fills=None,sw=4):
    """n EQUAL parts; shade = indices to fill; fills = {index: colour} overrides"""
    s=''; pw=w/n
    for i in range(n):
        f=(fills or {}).get(i, fill if i in shade else WHITE)
        s+=R(x+i*pw,y,pw,h,f,NAVY,sw)
    return s
def pol(cx,cy,r,a):  # angle in degrees, 0 = up, clockwise
    t=math.radians(a-90); return cx+r*math.cos(t),cy+r*math.sin(t)
def sector(cx,cy,r,a0,a1,fill,sw=4):
    x0,y0=pol(cx,cy,r,a0); x1,y1=pol(cx,cy,r,a1)
    return f'<path d="M{cx:.1f} {cy:.1f} L{x0:.1f} {y0:.1f} A{r} {r} 0 {1 if a1-a0>180 else 0} 1 {x1:.1f} {y1:.1f} Z" fill="{fill}" stroke="{NAVY}" stroke-width="{sw}" stroke-linejoin="round"/>'
def pie(cx,cy,r,n,shade=(),fill=YEL,sw=4):
    """circle cut into n EQUAL sectors (each 360/n degrees)"""
    return ''.join(sector(cx,cy,r,360*i/n,360*(i+1)/n,fill if i in shade else WHITE,sw) for i in range(n))
def ostep(left,top,n,text,ov=None,ovw=0,ovh=0,dx=0,dy=0,tw=1000,size=34,build='fade'):
    """one click = overlay drawn over the base picture + a step box to its right"""
    lab=f'<span style="color:{TEAL};font-weight:800">Step {n}.</span>  ' if n else ''
    box=f'<div style="margin-top:{dy}px;width:{tw}px;box-sizing:border-box;background:{WHITE};border-radius:20px;padding:16px 28px;flex:none"><p style="font-size:{size}px;font-weight:600;line-height:1.3">{lab}{fx(text,size)}</p></div>'
    o=f'<div style="width:{ovw}px;height:{ovh}px;flex:none">{ov or ""}</div>'
    return pin(left,top,dx+tw,f'<div style="display:flex;align-items:flex-start;gap:{dx-ovw}px">{o}{box}</div>',build)
def colstep(left,top,width,n,text,ov,ovh,dy,size=34,build='fade'):
    """one click = overlay over a full-width picture + a step box under it"""
    lab=f'<span style="color:{TEAL};font-weight:800">Step {n}.</span>  ' if n else ''
    box=f'<div style="margin-top:{dy}px;width:{width}px;box-sizing:border-box;background:{WHITE};border-radius:20px;padding:14px 28px"><p style="font-size:{size}px;font-weight:600;line-height:1.3">{lab}{fx(text,size)}</p></div>'
    return pin(left,top,width,f'<div style="width:{width}px;height:{ovh}px">{ov or ""}</div>'+box,build,extra='gap:0px;')

# ---------- standard slides ----------
def title_slide(sid,label,title,topic,today,notes):
    return (f'<section id="{sid}" data-transition="fade" style="background:{NAVY};color:{CREAM};font-family:{BF};padding:128px 128px 160px;display:flex;flex-direction:column;justify-content:center;gap:36px">\n'
            f'<p style="font-size:32px;font-weight:700;letter-spacing:4px;color:{YEL}">{E(label)}</p>\n'
            f'<h1 style="font-family:{HF};font-size:128px;font-weight:600;line-height:1.05">{E(title)}</h1>\n'
            f'<p style="font-size:44px;color:#C9D4EC">{E(topic)}</p>\n'
            f'<div style="background:#26385F;border-radius:24px;padding:40px;display:flex;flex-direction:column;gap:12px"><p style="font-size:28px;font-weight:700;letter-spacing:3px;color:{YEL}">TODAY WE WILL</p><p style="font-size:44px;font-weight:600">{E(today)}</p></div>\n'
            f'<p style="position:absolute;left:128px;bottom:64px;width:1400px;font-size:24px;color:#B7C3DD">{E(FOOT)}</p>\n<aside>{E(notes)}</aside>\n</section>\n')
def break_slide(sid,time,text,sub,notes):
    return (f'<section id="{sid}" data-transition="fade" style="background:{TEAL};color:{CREAM};font-family:{BF};padding:128px 128px 160px;display:flex;flex-direction:column;justify-content:center;gap:36px">\n'
            f'<p style="font-size:32px;font-weight:700;letter-spacing:4px;color:{YEL}">{E(time)}</p>\n'
            f'<h2 style="font-family:{HF};font-size:110px;font-weight:600;line-height:1.05">Brain break</h2>\n'
            f'<p style="font-size:48px;font-weight:600">{E(text)}</p>\n<p style="font-size:36px;color:#D7EFEA">{E(sub)}</p>\n'
            f'<p style="position:absolute;left:128px;bottom:64px;width:1400px;font-size:24px;color:#D7EFEA">{E(FOOT)}</p>\n<aside>{E(notes)}</aside>\n</section>\n')
def qcards(items,size=38):
    return ''.join(card(p(f'<span style="color:{TEAL}">{a}</span>  {fx(b,size)}',size,600,raw=True)) for a,b in items)
def talk_slide(sid,time,q,notes):
    body=h2('Talk time')+card(chip('TALK TIME',YEL,NAVY)+P(q,42,600))+card(p('Sentence starters:',34,400,MUTED)+p('“I noticed that …”   “I tested it by …”   “I know because …”',38,600))
    return sec(sid,time,body,notes)
def exit_slide(sid,time,inner,notes):
    body=h2('Exit ticket')+card(chip('EXIT TICKET')+inner)+card(p('Write your answer on a slip of paper. Show it to your tutor. Then collect your stamp in your inquiry journal.',34,400))
    return sec(sid,time,body,notes)

# =====================================================================
# 1. title
put('p2l7-title',title_slide('p2l7-title','LEVEL 2  •  LESSON 7  •  WEEK 4','Fair Shares','Fractions',
 'Cut wholes into equal parts, name and compare fractions, and add fractions to share things fairly.',
 'Objective: Recognise equal parts and name fractions (halves, thirds, quarters, up to twelfths); compare unit fractions and like fractions; add and take away like fractions within one whole; solve fair-sharing stories with a bar. '
 'Materials: 4 paper strips of the same length per child (A4 cut lengthwise), paper circles, scissors, crayons, mini whiteboards. '
 'Online: each child has 4 paper strips, a crayon and scissors on camera; the tutor shows fraction bars on the slides. '
 'Time plan: warm-up 0 to 8, explore 8 to 20 (explore2 talk is 6 minutes), teaching 20 to 32 (click to reveal each step and answer), brain break 32 to 36, worksheet page 1 36 to 50 then check together 50 to 52, short teaching 52 to 57, worksheet page 2 57 to 69 then check together 69 to 72, talk time 72 to 80, exit ticket 80 to 90.'))

# 2. warm1: fair or not fair?
def snack(i):
    c=90
    if i==0: g=CI(c,c,80,YEL)+L(c,10,c,170)
    elif i==1: g=CI(c,c,80,'#F3D9B1')+L(52,c-math.sqrt(80**2-38**2),52,c+math.sqrt(80**2-38**2))
    elif i==2: g=R(15,15,150,150,'#F3D9B1')+L(15,165,165,15)
    elif i==3: g=R(8,45,164,90,'#8B5A3C')+L(40,45,40,135,4,CREAM)+L(92,45,92,135,4,CREAM)
    elif i==4: g=pie(c,c,80,3,(),WHITE).replace(f'fill="{WHITE}"',f'fill="{SOFT}"')
    else: g=''.join(sector(c,c,80,a0,a1,YEL) for a0,a1 in [(0,60),(60,180),(180,240),(240,360)])
    return SV(180,180,g,['pizza cut into 2 equal halves','prata cut into 2 parts that are not the same size','toast cut corner to corner into 2 same-size triangles','chocolate bar cut into 3 parts of different sizes','cake cut into 3 equal parts','pancake cut into 4 parts: 2 small and 2 big'][i],170,170)
names=['Pizza','Roti prata','Kaya toast','Chocolate bar','Cake','Pancake']
labs=['Fair: 2 equal parts, halves','Not fair: different sizes','Fair: 2 same-size triangles','Not fair: different sizes','Fair: 3 equal parts, thirds','Not fair: 2 small, 2 big']
body=h2('Warm-up: fair or not fair?')+stitle('Is each snack cut into EQUAL parts? Thumbs up for fair, thumbs down for not fair.')
CW=533
for i in range(6):
    Lf=128+(i%3)*(CW+32); Tp=290+(i//3)*300
    inner=f'<div style="display:flex;align-items:center;gap:20px">{snack(i)}<p style="font-family:{HF};font-size:40px;font-weight:600">{E(names[i])}</p></div>'
    body+=pin(Lf,Tp,CW,inner,None,WHITE,24,'16px 22px',f'box-sizing:border-box;height:276px;border:4px solid {NAVY};box-shadow:8px 8px 0 {NAVY}')
for i in range(6):
    Lf=128+(i%3)*(CW+32); Tp=290+(i//3)*300
    body+=pin(Lf+20,Tp+190,CW-40,f'<p style="font-size:30px;font-weight:800;line-height:1.2">{E(labs[i])}</p>','pop',SOFT if labs[i].startswith('Fair') else '#F6D2D2',16,'12px 18px',f'box-sizing:border-box;border:3px solid {NAVY}')
put('p2l7-warm1',sec('p2l7-warm1','0–5 MIN',body,
 'Minutes 0 to 5. Fair or not fair? Point to one snack at a time: "Ali and Mei share this. Is it fair? Thumbs up or thumbs down." Then click to show the answer (clicks go pizza, prata, toast, chocolate, cake, pancake). '
 'Ask every time: "How do you know?" Listen for "the parts are the same size" (fair) and "one part is bigger" (not fair). '
 'Answers: pizza fair (cut through the middle: 2 halves); prata not fair (the cut is not through the middle); kaya toast fair (corner to corner makes 2 same-size triangles: fold one onto the other to check); chocolate bar not fair (3 different widths); cake fair (3 equal parts: thirds); pancake not fair (all cuts go through the middle, but 2 pieces are small and 2 are big). '
 'The pancake is the tricky one: cutting through the middle is not enough, the pieces must be the same size. Today\'s big word: EQUAL parts.'))

# 3. warm2 quick questions
qs=[('1.','A pizza is cut into 4 equal slices. What is 1 slice called?','one quarter, {1/4}'),('2.','How many halves make 1 whole?','2'),('3.','How many thirds make 1 whole?','3'),
    ('4.','A cake is cut into 5 equal pieces. What is 1 piece called?','one fifth, {1/5}'),('5.','2 of 7 equal parts are shaded. What fraction is shaded?','{2/7}')]
body=h2('Quick questions')+''.join(qrowx(128,250+i*128,1250,a,b,36) for i,(a,b,c) in enumerate(qs))+''.join(ansx(1420,250+i*128,372,c,size=34) for i,(a,b,c) in enumerate(qs))
put('p2l7-warm2',sec('p2l7-warm2','5–8 MIN',body,
 'Minutes 5 to 8. Read each question aloud, give thinking time, take answers on whiteboards, then click to show. Ask "How do you know?" each time. '
 'Answers: 1) one quarter, written 1/4 ("1 of 4 equal parts")  2) 2  3) 3  4) one fifth, 1/5  5) 2/7. '
 'For 5, show how we write it: the bottom number is how many EQUAL parts the whole has (7), the top number is how many we take (2). Watch for children who write 2/5 (shaded over not shaded): ask "How many parts are there altogether?"'))

# 4. explore1: fold strips
sw_=1260; x0=330
rows=[('1 whole',1),('halves',2),('quarters',4),('eighths',8)]
g=''
for k,(lab,n) in enumerate(rows):
    y=12+k*78
    g+=T(x0-24,y+46,lab,32,NAVY,700,'end')+bar(x0,y,sw_,62,n,(),WHITE,{0:[SKY,YEL,MINT,SOFT][k]})
    if n>1:
        for i in range(n): g+=sfrac(x0+sw_/n*(i+0.5),y+31,1,n,24)
pic=SV(1620,330,g,'Four paper strips the same length: one whole, one folded into halves, one into quarters and one into eighths, with each part labelled')
body=h2('Explore: fold fair shares')+card(chip('EXPLORE')+'<ol style="font-size:32px;font-weight:600;padding-left:48px;display:flex;flex-direction:column;gap:6px;margin:0"><li>Take 4 paper strips that are the same length.</li><li>Keep one whole. Fold one in half, one into quarters and one into eighths.</li><li>Open them out. Write the fraction on every part.</li><li>Line them up. Then try to fold a strip into 3 equal parts!</li></ol>',extra='padding:24px 40px')
body+=pin(128,560,1664,pic,None,WHITE,24,'8px 22px')
put('p2l7-explore1',sec('p2l7-explore1','8–14 MIN',body,
 'Minutes 8 to 14. Each child folds their own strips; pairs compare. Show how to fold in half by matching the ends. Quarters: fold in half, then in half again. Eighths: in half three times. '
 'Children write 1/2, 1/4 or 1/8 on each part and line the strips up under each other, left ends together. '
 'Thirds are hard on purpose: there is no "fold in half" trick. Let them try (roll the strip into an S and flatten it, then check the 3 parts are the same length). Online: the same with paper strips on camera. Say before they start: "Thirds are tricky for everybody, grown-ups too. A strip that does not come out equal is a good try, not a mistake: tell me what you notice." Nothing is marked. Fractions are written as 1/2 on slides and as stacked fractions in the workbook: both mean the same.'))

# 5. explore2
items=[('1.','Which part is bigger, {1/4} or {1/8}? How do you know?'),('2.','How many eighths fit on one quarter? How many quarters make 1 whole?'),('3.','How did you fold 3 equal parts? How do you know they are equal?')]
put('p2l7-explore2',sec('p2l7-explore2','14–20 MIN',h2('Explore: talk about it')+qcards(items,40),
 'Minutes 14 to 20. Let pairs keep working, then gather them. Answers: 1) 1/4 is bigger. The strip is the same length, but cut into 4 parts instead of 8, so each part is longer. Put the strips together to show it. '
 '2) 2 eighths fit on 1 quarter; 4 quarters make 1 whole (and 8 eighths make 1 whole). '
 '3) Any fair method: fold and adjust until the 3 parts are the same length, then check by folding one part on top of another. Praise checking. '
 'Ask: "Is 1/8 bigger because 8 is bigger than 4?" No! More parts means each part is smaller. We use this idea all lesson.'))

# 6. teach1: equal parts
def thirds_pic(stage):
    g=''
    if stage==0:
        g=T(30,82,'A',44)+bar(70,20,560,100,3)+T(30,302,'B',44)+R(70,240,100,100)+R(170,240,300,100)+R(470,240,160,100)
    if stage==1:
        g=''.join(T(70+560/3*(i+0.5),84,i+1,44,TEAL) for i in range(3))+''.join(T(x,304,i+1,44,TEAL) for i,x in enumerate([120,320,550]))
    if stage==2:
        g=TICK(675,70,22)+CROSS(675,290,24)
    if stage==3:
        g=''.join(sfrac(70+560/3*(i+0.5),165,1,3,36,TEAL) for i in range(3))
    return SV(710,350,g,['bar A cut into 3 equal parts and bar B cut into 3 parts of different sizes','parts numbered 1 to 3','tick for bar A, cross for bar B','each part of bar A labelled one third'][stage])
halves=''
for k in range(3):
    x=20+k*230
    halves+=R(x,10,180,110,WHITE)
    if k==0: halves+=R(x,10,90,110,YEL)+L(x+90,10,x+90,120)
    if k==1: halves+=R(x,10,180,55,YEL)+L(x,65,x+180,65)
    if k==2: halves+=PG([(x,10),(x,120),(x+180,120)],YEL)+L(x,10,x+180,120)
halfpic=SV(700,130,halves,'Three rectangles each cut into 2 equal halves in a different way: down the middle, across the middle, and corner to corner')
body=h2('Fair shares: the parts must be equal')+stitle('Each bar is cut into 3 parts. Is each bar cut into thirds?')
body+=pin(128,320,710,thirds_pic(0))
body+=ostep(128,320,1,'Count the parts. Both bars have 3 parts.',thirds_pic(1),710,350,dx=770,dy=0,tw=894)
body+=ostep(128,320,2,'Are the parts the same size? Bar A: yes. Bar B: no.',thirds_pic(2),710,350,dx=770,dy=92,tw=894)
body+=ostep(128,320,3,'Only EQUAL parts have a fraction name. Each part of bar A is {1/3}. Bar B is not cut into thirds.',thirds_pic(3),710,350,dx=770,dy=228,tw=894)
body+=pin(128,700,1664,f'<div style="display:flex;align-items:center;gap:30px"><p style="width:860px;flex:none;font-size:34px;font-weight:700;line-height:1.3">Equal parts can look different. All of these rectangles are cut into halves.</p>{halfpic}</div>','fade',SOFT,20,'14px 28px')
put('p2l7-teach1',sec('p2l7-teach1','20–22 MIN',body,
 'Teach. Ask first: "Ali says both bars are cut into thirds. Do you agree?" Take votes. Click 1: count the parts together: 3 and 3. Click 2: "Are they the same size?" Bar A yes, bar B no: one part is much bigger. Click 3: only equal parts get a fraction name. "One third means 1 of 3 EQUAL parts." '
 'Click 4: equal parts can look different. Each rectangle is cut into 2 equal parts: down the middle, across the middle, or corner to corner (fold one triangle onto the other: they match). '
 'Think-aloud: "Before I name a fraction, I check two things: how many parts, and are they all the same size? If they are not the same size, I cannot use a fraction name."'))

# 7. we1: name the fraction
base=SV(900,150,bar(10,10,880,120,5,(0,1,2)),'A bar cut into 5 equal parts with 3 parts shaded')
ov1=SV(900,150,''.join(T(10+176*(i+0.5),88,i+1,48,TEAL if i>2 else NAVY) for i in range(5)),'parts numbered 1 to 5')
body=h2('Worked example: name the fraction')+card(P('What fraction of the bar is shaded? What fraction is NOT shaded?',40,700),extra='padding:22px 40px')
body+=pin(128,370,900,base)
body+=ostep(128,370,1,'Are the parts equal? Yes. Count them: 5 equal parts. They are fifths, so the bottom number is 5.',ov1,900,150,dx=960,dy=0,tw=704,size=32)
body+=stepx(2,'Count the shaded parts: 3. The top number is 3. Shaded: {3/5}',top=560,width=1664,size=36,build='fade')
body+=stepx(3,'Not shaded: 2 parts. Not shaded: {2/5}',top=680,width=1664,size=36,build='fade')
body+=ansx(128,800,1100,'Check: {3/5} and {2/5} make {5/5}, 1 whole ✓',size=36)
put('p2l7-we1',sec('p2l7-we1','22–25 MIN',body,
 'Click to reveal each step; ask the group to predict before each click. Think-aloud: "First I check the parts are equal. They are. I count all the parts: 1, 2, 3, 4, 5. Five equal parts are called fifths, so 5 goes at the bottom. Now I count the shaded parts: 3. That goes on top: three fifths. The parts that are not shaded: 2, so two fifths." '
 'Say: "The bottom number tells us how many equal parts make the whole. The top number tells us how many parts we are talking about." The check: 3 fifths and 2 fifths make 5 fifths, the whole bar. Watch for 3/2 (shaded over not shaded).'))

# 8. try1
p_a=SV(200,200,pie(100,100,90,3,(0,1)),'A circle cut into 3 equal parts with 2 shaded')
p_b=SV(300,100,bar(4,20,292,60,12,(0,1,4,7,10)),'A bar cut into 12 equal parts with 5 shaded')
p_c=SV(300,100,R(4,10,60,80,YEL)+R(64,10,90,80)+R(154,10,142,80),'A rectangle cut into 3 parts of different sizes with 1 shaded')
body=h2('Your turn: name the fraction')+stitle('Whiteboards: what fraction is shaded? What fraction is not shaded?')
tops=[300,520,680]
for k,(pic,ph,q,a) in enumerate([(p_a,200,'Shaded? Not shaded?','{2/3}  and  {1/3}'),(p_b,100,'Shaded? Not shaded?','{5/12}  and  {7/12}'),(p_c,100,'Is the shaded part {1/3}?','No: the parts are not equal')]):
    body+=pin(128,tops[k],300,pic,None,WHITE,20,'8px 20px')+qrowx(500,tops[k]+(40 if k==0 else 0),860,'abc'[k],q,36)+ansx(1400,tops[k]+(40 if k==0 else 0),392,a,size=34)
put('p2l7-try1',sec('p2l7-try1','25–26 MIN',body,
 'Whiteboards up together, then click. a) 3 equal parts, 2 shaded: 2/3 shaded, 1/3 not shaded. b) 12 equal parts (twelfths); count the shaded ones carefully, they are not next to each other: 5, so 5/12 shaded and 7/12 not shaded (5 + 7 = 12). '
 'c) The trap: 3 parts, 1 shaded, but the parts are not the same size, so the shaded part is NOT one third. Ask: "What would we need to change to make it thirds?"'))

# 9. we2: compare unit fractions
g=''
for k,n in enumerate([1,2,3,6]):
    y=8+k*92
    g+=(T(120,y+52,'1 whole',30,NAVY,700,'end') if n==1 else sfrac(95,y+34,1,n,30))+bar(160,y,780,70,n,(0,),[SOFT,YEL,YEL,YEL][k] if n>1 else SOFT)
pic=SV(950,370,g,'Four bars the same length: 1 whole, halves, thirds and sixths, with one part of each shaded')
body=h2('Compare: one part of the same whole')+stitle('Which is bigger: {1/2}, {1/3} or {1/6}?')
body+=pin(128,330,950,pic)
body+=stepx(1,'Same whole: all the bars are the same length.',left=1130,top=330,width=662,size=32,build='fade')
body+=stepx(2,'{1/2} is 1 of 2 parts. {1/6} is 1 of 6 parts.',left=1130,top=470,width=662,size=32,build='fade')
body+=stepx(3,'More equal parts: each part is smaller.',left=1130,top=610,width=662,size=32,build='fade')
body+=ansx(128,760,950,'Smallest to biggest: {1/6}, {1/3}, {1/2}',size=36)
body+=soft(1130,760,662,'A pizza shared by 6, not 2: each slice is smaller.',32)
put('p2l7-we2',sec('p2l7-we2','26–28 MIN',body,
 'Click through. Hold up the folded strips from Explore. Think-aloud: "All the bars are the same length, so it is the same whole. One half is 1 of 2 parts. One sixth is 1 of 6 parts. When I cut the same whole into more parts, each part gets smaller. So one sixth is the smallest and one half is the biggest." '
 'Story: "One pizza for 2 children, or one pizza for 6 children: when do you get a bigger slice?" Common mistake: "1/6 is bigger because 6 is bigger than 2". Answer with the strips, not just words. Only compare like this when the wholes are the same size.'))

# 10. we3: compare like fractions
g=sfrac(60,52,2,7,34)+bar(120,15,820,80,7,(0,1))+sfrac(60,172,5,7,34)+bar(120,135,820,80,7,(0,1,2,3,4))
pic=SV(950,230,g,'Two bars cut into 7 equal parts: 2 sevenths shaded and 5 sevenths shaded')
body=h2('Compare: same bottom number')+stitle('Which is bigger: {2/7} or {5/7}?')
body+=pin(128,330,950,pic)
body+=stepx(1,'Both are sevenths: the parts are the same size.',left=1130,top=330,width=662,size=32,build='fade')
body+=stepx(2,'Count the parts: 2 sevenths and 5 sevenths.',left=1130,top=470,width=662,size=32,build='fade')
body+=ansx(1130,610,662,'{5/7} is bigger than {2/7}',size=36)
body+=soft(128,760,1664,'Same bottom number? The parts are the same size, so compare the top numbers.',34)
put('p2l7-we3',sec('p2l7-we3','28–30 MIN',body,
 'Click through. Think-aloud: "Both are sevenths, so every part is the same size. Then it is just like counting apples: 5 sevenths is more than 2 sevenths." '
 'Contrast with the last slide: there the top numbers were all 1 and the parts were different sizes; here the bottom numbers are the same and only the number of parts changes. Ask: "Which is bigger, 4/9 or 7/9? How do you know?" (7/9, more ninths).'))

# 11. try2
put('p2l7-try2',try_x('p2l7-try2','30–31 MIN','Your turn: which is bigger?','Draw bars if it helps. Same whole every time.',
 [('a','Which is bigger: {1/5} or {1/10}?','{1/5}'),('b','Which is bigger: {3/11} or {8/11}?','{8/11}'),('c','Smallest first: {1/3}, {1/12}, {1/6}','{1/12}, {1/6}, {1/3}')],
 'Whiteboards, then click. a) 1/5: the same whole cut into 5 parts gives bigger parts than cut into 10. b) 8/11: both are elevenths, and 8 elevenths is more than 3 elevenths. c) 1/12, 1/6, 1/3: more parts, smaller part. Ask a child to explain c without using the words "bigger number".',size=36,gap=160))

# 12. key
body=h2('Key idea: equal parts')+card(P('A fraction names EQUAL parts of a whole. The bottom number: how many equal parts. The top number: how many we take.',44,700))+card(P('Same whole: more equal parts means smaller parts. So {1/8} is smaller than {1/4}.',38,600,MUTED))
put('p2l7-key',sec('p2l7-key','31–32 MIN',body,
 'Say the key idea together. Common mistakes to watch for during the worksheet: (1) Naming a fraction when the parts are not equal (Q1 B and D): ask "Are all 4 parts the same size?" '
 '(2) Thinking 1/6 is bigger than 1/4 because 6 is bigger than 4 (Q3): fold or draw the strips. '
 '(3) Adding the bottom numbers too: 2/5 + 1/5 written as 3/10 (Q4). The parts are still fifths, so only the top numbers are added. '
 '(4) Writing shaded over not shaded (3/5 instead of 3/8).'))

# 13. break
put('p2l7-break',break_slide('p2l7-break','32–36 MIN','Fraction turns. Stand up! When the tutor calls a turn, turn that much and freeze: a whole turn, a half turn, a quarter turn, three quarter turns.','Then: a drink of water and back to our seats.',
 'Four minutes. Face the screen to start. A half turn: you face the back. A quarter turn: you face the side. Three quarter turns: the other side. Try "two quarter turns" (the same as a half turn!). Online: children stay in view of the camera.'))

# 14-15. worksheet page 1
put('p2l7-ws1',preview_x('p2l7-ws1','36–50 MIN','Worksheet page 1: with your partner',[('Q1','Fair shares? Circle the shapes cut into quarters. Check the parts are equal.'),('Q2','Name the fraction that is shaded and the fraction that is not.'),('Q3','Compare and order fractions. Draw bars to help.')],'Stuck? Fold a paper strip, or draw the bars the same length.',
 'Minutes 36 to 50. Pairs work together. Ask "How do you know?" before giving any help. For Q1, give pairs a paper square to fold if they are unsure about E (corner to corner). For Q3c ask "What does the 6 tell us?"'))
put('p2l7-ws1ans',check_x('p2l7-ws1ans','50–52 MIN','Page 1: check together',[('Q1','A, C, E and F.   B and D: the 4 parts are not equal.'),('Q2','a) {3/8}, {5/8}    b) {5/6}, {1/6}    c) {7/10}, {3/10}'),('Q3 a, b','a) {1/3} and {7/9}     b) {1/10}, {1/5}, {1/4}, {1/2}'),('Q3 c','No. 6 equal parts are smaller than 4 equal parts of the same whole.')],
 'Click each answer after a pair explains theirs. Q1: F surprises many children: the triangle cut by joining the middles of its sides makes 4 triangles that are all the same size, the middle one is just turned upside down. E: the 4 triangles of a square cut corner to corner are all the same. '
 'B: the cuts do not go through the middle. D: the strips are different widths. Q2c: count the shaded squares one by one: 7 of 10. Q3b: more parts means smaller parts, so tenths are smallest.',lw=230,gap=160,size=34))

# 16. teach before page 2: adding
def add_ov(stage):
    if stage==1: return SV(1100,140,bar(10,10,1080,110,9,(),WHITE,{0:YEL,1:YEL}).replace(f'fill="{WHITE}"','fill="none"'),'2 ninths coloured yellow')
    if stage==2: return SV(1100,140,''.join(R(10+120*i,10,120,110,TEAL) for i in range(2,6)),'4 more ninths coloured green')
    return SV(1100,140,''.join(T(10+120*(i+0.5),82,i+1,44,NAVY if i<2 else CREAM) for i in range(6)),'6 parts numbered')
base=SV(1100,140,bar(10,10,1080,110,9),'A bar cut into 9 equal parts')
body=h2('Add fractions with the same bottom number')+card(P('{2/9} + {4/9} = ?',44,700),extra='padding:20px 40px')
body+=pin(128,360,1100,base)
body+=colstep(128,360,1100,1,'Colour {2/9}: 2 ninths.',add_ov(1),140,0)
body+=colstep(128,360,1100,2,'Colour {4/9} more: 4 more ninths.',add_ov(2),140,-140+70).replace('margin-top:-70px','margin-top:70px')
body+=colstep(128,360,1100,3,'Count: 6 ninths. The parts are still ninths, so the bottom number stays 9.',add_ov(3),140,140)
body+=ansx(128,800,1100,'{2/9} + {4/9} = {6/9}',size=40)
body+=pin(1290,360,502,P('How much more makes 1 whole?',34,700),'fade',SOFT,20,'18px 28px')
body+=pin(1290,520,502,P('3 more ninths. {6/9} + {3/9} = {9/9} = 1 whole',34,700),'fade',WHITE,20,'18px 28px')
put('p2l7-teachadd',sec('p2l7-teachadd','52–54 MIN',body,
 'Teach before worksheet page 2 (Q4 adds and takes away fractions). Click 1: colour 2 ninths. Click 2: colour 4 more. Click 3: count the coloured parts: 6. Think-aloud: "Two ninths and four ninths. Ninths are the name of the parts, like apples. 2 apples and 4 apples are 6 apples. 2 ninths and 4 ninths are 6 ninths. The parts do not change size, so it stays ninths." '
 'Then the side question: 9 ninths make the whole bar, so 3 more ninths are needed. Taking away works the same way: 6/9 − 2/9 = 4/9. Big mistake to stop: 2/9 + 4/9 = 6/18. Show that 6/18 would mean the parts became smaller, which did not happen.'))
put('p2l7-tryadd',try_x('p2l7-tryadd','54–55 MIN','Your turn: add and take away','Draw a bar. Count the parts.',
 [('a','{1/4} + {2/4} = ?','{3/4}'),('b','{3/10} + {6/10} = ?','{9/10}'),('c','{5/12} + ? = 1 whole','{7/12}'),('d','{8/11} − {3/11} = ?','{5/11}')],
 'Whiteboards, then click. a) 3 quarters. b) 9 tenths. c) 12 twelfths make 1 whole; 12 − 5 = 7, so 7/12. d) 8 elevenths take away 3 elevenths: 5/11. Ask: "Why does the bottom number not change?"',size=36,top=310,gap=145))

# 17. story
base=SV(1100,140,bar(10,10,1080,110,10),'A bar for a cake cut into 10 equal pieces')
def tag(x,y,t,w=110): return R(x-w/2,y-30,w,46,WHITE,NAVY,3,12)+T(x,y+6,t,32)
ov1=SV(1100,140,''.join(R(10+108*i,10,108,110,YEL) for i in range(4))+tag(10+108*2,65,'Ben'),'4 pieces coloured for Ben')
ov2=SV(1100,140,''.join(R(10+108*i,10,108,110,SKY) for i in range(4,7))+tag(10+108*5.5,65,'Siti'),'3 pieces coloured for Siti')
body=h2('Fair-sharing stories: draw a bar')+card(P('A cake is cut into 10 equal pieces. Ben eats 4 pieces. Siti eats 3 pieces. What fraction of the cake is eaten? What fraction is left?',36,700),extra='padding:20px 40px')
body+=pin(128,400,1100,base)
body+=colstep(128,400,1100,1,'Draw a bar of 10 equal parts. Colour Ben\'s 4: {4/10}.',ov1,140,0,32)
body+=colstep(128,400,1100,2,'Colour Siti\'s 3: {3/10}.',ov2,140,96,32)
body+=pin(1290,400,502,P('Eaten: {4/10} + {3/10} = {7/10}',36,700),'fade',WHITE,20,'18px 28px')
body+=pin(1290,560,502,P('Left: 3 white parts, {3/10}',36,700),'fade',WHITE,20,'18px 28px')
body+=soft(128,780,1664,'Check: {7/10} eaten and {3/10} left make {10/10}, the whole cake ✓',34)
put('p2l7-teachstory',sec('p2l7-teachstory','55–56 MIN',body,
 'Teach before worksheet page 2 (Q5 is a cake story with different numbers). Click through. Think-aloud: "The cake has 10 equal pieces, so I draw a bar of 10 parts: each part is one tenth. Ben eats 4: I colour 4. Siti eats 3: I colour 3 more in a new colour. Eaten: 4 tenths and 3 tenths make 7 tenths. Left: the white parts: 3 tenths." '
 'Ask: "Who ate more? How much more?" (Ben, 1/10 more). Always check that eaten and left make the whole.'))

# 18. same whole
g=T(150,62,'Mei',36,NAVY,700,'end')+bar(170,10,900,90,2,(0,))+T(150,192,'Ben',36,NAVY,700,'end')+bar(170,140,900,90,8,(0,1,2))
base=SV(1100,250,g,'Two bars the same length: halves with 1 half shaded, and eighths with 3 eighths shaded')
ov=SV(1100,250,L(620,0,620,245,6,RED,'14 10')+''.join(T(170+112.5*(i+0.5),200,i+1,36,NAVY) for i in range(4)),'a dashed line shows that one half lines up with 4 eighths')
body=h2('Different parts? Line up the same whole')+card(P('Mei eats {1/2} of a pizza. Ben eats {3/8} of a pizza the same size. Who eats more?',38,700),extra='padding:20px 40px')
body+=pin(128,370,1100,base)
body+=colstep(128,370,1100,1,'Line them up: {1/2} is the same as 4 eighths.',ov,250,0,32)
body+=pin(1290,370,502,P('Draw both wholes the same length.',34,700),None,SOFT,20,'18px 28px')
body+=ansx(1290,560,502,'4 eighths is more than 3 eighths. Mei eats more.',size=34)
put('p2l7-teachsame',sec('p2l7-teachsame','56–57 MIN',body,
 'Teach before worksheet page 2 (Q6 compares a quarter with eighths). Use the folded strips from Explore: lay the halves strip on the eighths strip. Click 1: one half covers 4 eighths. Click 2: Ben ate 3 eighths, Mei ate the same as 4 eighths, so Mei ate more. '
 'Think-aloud: "Halves and eighths are different parts, so I cannot just look at the numbers. I draw the same whole twice, the same length, and line the parts up." Ask: "What if Mei\'s pizza were tiny?" Then we cannot compare like this: the wholes must be the same size. Equivalent fractions are a P3 topic: show that one half covers 4 eighths with the lined-up strips only, and do not write 1/2 = 4/8 as a rule.'))

# 19-20. worksheet page 2
put('p2l7-ws2',preview_x('p2l7-ws2','57–69 MIN','Worksheet page 2: on your own',[('Q4','Add and take away. Colour the bars.'),('Q5','The cake story. Draw a bar.'),('Q6','Who eats more pizza? Line up the same whole.')],'Finished early? Stretch and Challenge come next.',
 'Children work alone. Note who needs a short catch-up next lesson. For Q6, check children draw both bars the same length.'))
put('p2l7-ws2ans',check_x('p2l7-ws2ans','69–72 MIN','Page 2: check together',[('Q4','a) {3/5}   b) {7/8}   c) {9/12}   d) {5/6}   e) {4/10}'),('Q5','a) {5/8}    b) {3/8}    c) Mei, by {1/8}'),('Q6','Siti. {1/4} is 2 eighths, and 3 eighths is more.')],
 'Click each answer after a child explains. Q4d: 6 sixths make 1 whole, so 5/6 more. Q4e: 7 tenths take away 3 tenths is 4 tenths. Q5: 2 + 3 = 5 slices eaten (5/8); 8 − 5 = 3 left (3/8); Mei ate 3 slices, Ali 2: Mei ate 1/8 more. '
 'Q6: the pizzas are the same size; Ravi\'s 1 quarter covers 2 eighths, Siti ate 3 eighths.',lw=200,gap=160,size=34))

# 21. stretch (new items)
st=[('1.','Ali\'s ribbon and Mei\'s ribbon are each cut into thirds. Mei\'s {1/3} is longer than Ali\'s {1/3}. How can that be?'),('2.','Write all the fractions with bottom number 5 that are bigger than {2/5} and smaller than 1 whole.'),('3.','A bar has 12 equal parts. Ben shades {1/12}, then {2/12} more, then {3/12} more. How much is not shaded?')]
put('p2l7-stretch',sec('p2l7-stretch','For early finishers',h2('Stretch')+qcards(st,36),
 'For children who finish early. Answers: 1) Mei\'s whole ribbon is longer than Ali\'s. A third of a long ribbon is longer than a third of a short one: fractions only compare like this when the wholes are the same size. '
 '2) 3/5 and 4/5. 3) 1 + 2 + 3 = 6 twelfths shaded, so 6/12 is not shaded.'))

# 22. challenge
ch=[('1.','I am a fraction with 1 on top. I am smaller than {1/4} but bigger than {1/7}. What could I be? Find all the answers.'),('2.','A cake is cut into 12 equal pieces. Mei gets {4/12}. Ali and Ben share the rest, but Ali gets {2/12} more than Ben. What fraction does Ben get?')]
put('p2l7-challenge',sec('p2l7-challenge','Challenge',h2('Challenge')+qcards(ch,36),
 'Use as a pair challenge or in talk time. Ask for the reason every time. More are in the question bank. Answers: 1) 1/5 and 1/6.  2) Ben gets 3/12 (and Ali 5/12).'))

# 23. chdiag
g=''
for k,n in enumerate([4,7]):
    y=20+k*250
    g+=sfrac(60,y+35,1,n,30)+bar(120,y,560,70,n,(0,))
g+=T(400,150,'Which fractions with 1 on top',28,MUTED)+T(400,186,'fit in between?',28,MUTED)+R(340,200,120,46,WHITE,NAVY,3,10)+T(400,234,'?',30,TEAL)
d1=SV(700,360,g,'Bars for one quarter and one seventh of the same whole, with blank cards for the fractions in between')
g=bar(20,30,660,90,12,(0,1,2,3),SKY)+R(65,52,90,46,WHITE,NAVY,3,12)+T(110,86,'Mei',30)+T(240,162,'Ali and Ben share these 8 pieces',28,MUTED,700,'start')
g+=R(40,220,300,80,YEL,NAVY,4,10)+T(190,272,'Ben: ?',34)+R(360,220,300,80,YEL,NAVY,4,10)+T(510,272,'Ali: Ben + 2',32)
d2=SV(700,360,g,'A bar of 12 pieces: 4 for Mei; the other 8 shared by Ben and Ali, where Ali has 2 more than Ben')
def chcol(t,svg): return f'<div style="background:{WHITE};border-radius:24px;padding:20px 24px;display:flex;flex-direction:column;gap:10px;flex:1;min-width:0"><p style="font-size:28px;font-weight:700;color:{TEAL}">{E(t)}</p>{svg}</div>'
body=h2('Challenge: see it',60)+f'<div style="display:flex;gap:32px;align-items:flex-start">{chcol("Q1: between one seventh and one quarter",d1)}{chcol("Q2: sharing a cake of 12 pieces",d2)}</div>'
put('p2l7-chdiag',sec('p2l7-chdiag','Challenge',body,'Show after pairs have tried the Challenge, or if they are stuck. The diagrams show the problem, not the answer. Ask: What do you notice? What do we know? What do we not know yet? Can you draw it? Answers are in the Challenge slide notes.'))

# 24. chwalk
body=h2('Challenge: walk-through')+pin(128,250,800,p('Q1: list them in order',38,800,TEAL))
for i,t in enumerate(['Same whole: bigger bottom number, smaller part.','Smaller than {1/4}: bottom number more than 4.','Bigger than {1/7}: bottom number less than 7.','So 5 or 6: {1/5} and {1/6} ✓']): body+=pin(128,330+i*125,800,P(t,32),'rise',WHITE)
body+=pin(992,250,800,p('Q2: take away the extra',38,800,TEAL))
for i,t in enumerate(['12 − 4 = 8 pieces for Ali and Ben.','Take away Ali\'s extra 2: 6 pieces left.','Share 6 fairly: 3 and 3. Ben 3, Ali 3 + 2 = 5.','Ben gets {3/12}. Check: 4 + 5 + 3 = 12 ✓']): body+=pin(992,330+i*125,800,P(t,32),'rise',WHITE)
put('p2l7-chwalk',sec('p2l7-chwalk','Challenge',body,
 'Use after pairs have tried. Q1: list the unit fractions in order with bars: 1/4, 1/5, 1/6, 1/7. Only 1/5 and 1/6 are between. Children who say 1/3 or 1/8 have turned the rule round: show the strips. '
 'Q2 uses the "take away the extra, share, give it back" idea: 8 pieces, take away 2, share 6 as 3 and 3, give the 2 to Ali. Ben 3/12, Ali 5/12, Mei 4/12.'))

# 25. talk
put('p2l7-talk',talk_slide('p2l7-talk','72–80 MIN','Is {1/2} always bigger than {1/4}? Can you think of a time when it is not?',
 'Minutes 72 to 80. Pairs talk for 2 minutes, then share. Answer: when the wholes are the same size, yes, 1/2 is bigger. But half of a small cupcake is less than a quarter of a big cake! Fractions only compare like this when the wholes are the same. Praise the reasons, not only the answers.'))

# 26. exit
put('p2l7-exit',exit_slide('p2l7-exit','80–90 MIN',P('Which is bigger, {1/7} or {1/9}? Then work out {2/9} + {5/9}.',46,600),
 'Minutes 80 to 90. Answers: 1/7 is bigger (the same whole cut into fewer parts, so each part is bigger). 2/9 + 5/9 = 7/9. Children who write 7/18 added the bottom numbers: ask "What size are the parts?" Extension: How much more than 7/9 makes 1 whole? (2/9).'))

p2gaps.add(S,7)
# ---------- write ----------
for f in os.listdir(os.path.join(D,'slides')):
    if f.endswith('.html') and f[:-5] not in S: os.remove(os.path.join(D,'slides',f))
for i,h in S.items(): open(os.path.join(D,'slides',i+'.html'),'w').write(h)
order=['p2l7-title','p2l7-warm1','p2l7-warm2','p2l7-explore1','p2l7-explore2','p2l7-teach1','p2l7-we1','p2l7-try1','p2l7-we2','p2l7-we3','p2l7-try2','p2l7-key','p2l7-break','p2l7-ws1','p2l7-ws1ans','p2l7-teachadd','p2l7-tryadd','p2l7-teachstory','p2l7-teachsame','p2l7-ws2','p2l7-ws2ans','p2l7-stretch','p2l7-challenge','p2l7-chdiag','p2l7-chwalk','p2l7-talk','p2l7-exit']
order=p2gaps.order(order,7)
deck={'v':4,'createdOnFiles':{'v':1,'at':'2026-10-21T12:00:00Z'},'lists':'css','title':'Math Inquirers Level 2: Lesson 7 – Fair Shares','order':order,'cover':'p2l7-title',
 'sections':{'s1':{'description':'Warm-up and explore','start':'p2l7-title'},'s2':{'description':'Teach: equal parts, naming and comparing fractions','start':'p2l7-teach1'},'s3':{'description':'Worksheet with teaching before page 2','start':'p2l7-break'},'s4':{'description':'Think harder, go further, talk and exit','start':'p2l7-stretch'}},
 'faces':{'fredoka':{'family':'Fredoka','href':'https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&display=swap'},'nunito-sans':{'family':'Nunito Sans','href':'https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@400;600;700&display=swap'}},'designSystems':[]}
json.dump(deck,open(os.path.join(D,'deck.json'),'w'),indent=1,ensure_ascii=False)
missing=[i for i in order if i not in S]
print(len(order),'slides; wrote',len(S),'missing',missing)
