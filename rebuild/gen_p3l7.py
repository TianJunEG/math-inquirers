"""Math Inquirers P3 – Lesson 7: Area Architects. Writes split/p3l7/project (deck.json + slides/*.html)."""
import json,os,sys,math,datetime
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,H)
from slidekit import *
D=os.path.join(H,'..','split','p3l7','project'); S={}
def put(i,h): S[i]=h
RED='#D64545'; LG='#B9C6DE'; PFX='p3l7-'
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

# ================= 1. title =================
put(PFX+'title',title_slide(PFX+'title','LESSON 7  •  WEEK 4','Area Architects','Area and Perimeter',
 'Find every rectangle with the same fence, push steps out to find perimeters fast, and cut up or fill in shapes to find their area.',
 'Objective: Find the area and perimeter of figures made of squares and rectangles, list every rectangle with a given perimeter in order, and change the shape (push the steps out; cut it up or fill it in) to find perimeters and areas quickly. Heuristics taught today: (1) make a list in order, (2) change the shape. '
 'Materials: 12 square tiles (or 12 squares cut from 1 cm grid paper) per child, 1 cm grid paper, mini whiteboards, a ruler. '
 'Online: children cut 12 squares from squared paper (or draw on squared paper) and hold their rectangles up to the camera; annotate the grid slides with the pen tool. '
 'Time plan: warm-up 0 to 10, explore 10 to 25, teaching 25 to 35 (click to reveal each step and answer), brain break 35 to 40, worksheet 40 to 70 with short teaching before each page and a check-together slide after it, talk time 70 to 80, exit ticket 80 to 90. Stretch and Challenge are for early finishers. If the class is behind, children finish the last question of each page at home; the check slides cover it.'))

# ================= 2. warm-up game =================
jobs=[('1','Put a fence round a garden','Perimeter'),('2','Cover a floor with tiles','Area'),('3','Stick ribbon round the edge of a card','Perimeter'),
      ('4','Paint a wall','Area'),('5','Put a frame round a photo','Perimeter'),('6','Cover a book with plastic','Area')]
body=h2('Warm-up: area or perimeter?')+stitle('Round the edge? Trace it with a finger: PERIMETER.  Covers the inside? Wipe a flat palm: AREA.')
CW=533; cards=''; ans=''
for i,(n,job,a) in enumerate(jobs):
    L=128+(i%3)*(CW+32); Tp=320+(i//3)*290
    cards+=pin(L,Tp,CW,f'<p style="font-family:{HF};font-size:30px;font-weight:600;color:{TEAL}">JOB {n}</p><p style="font-family:{HF};font-size:40px;font-weight:600;line-height:1.15">{E(job)}</p>',None,WHITE,24,'18px 26px',f'box-sizing:border-box;height:262px;border:4px solid {NAVY};box-shadow:8px 8px 0 {NAVY}')
    ans+=pin(L+20,Tp+176,CW-40,f'<p style="font-size:36px;font-weight:800;line-height:1.2">{E(a)}</p>','pop',SOFT,16,'10px 18px',f'box-sizing:border-box;border:3px solid {NAVY}')
put(PFX+'warm1',S_(PFX+'warm1','0–5 MIN',body+cards+ans,
 'Minutes 0 to 5. Everyone stands. Read each job aloud. Children show with their hands: trace a finger round an imaginary edge for perimeter, wipe a flat palm across for area. Then click to show the answer (clicks reveal jobs 1 to 6 in order). '
 'Answers: 1 fence: perimeter. 2 tiles: area. 3 ribbon round the edge: perimeter. 4 paint: area. 5 frame: perimeter. 6 cover a book: area. '
 'Ask each time: "Does the job go ROUND the edge, or does it COVER the inside?" Quick finisher: "Which unit would you use for the fence: m or m²? For the tiles?" (m for the fence, m² for the floor). Watch for children who think a frame is area because it is a flat thing: it only goes round the edge.'))

# ================= 3. quick questions =================
qs=[('1.','8 × 7 = ?','56'),('2.','A square has sides of 6 cm. What is its perimeter?','24 cm'),('3.','A rectangle is 8 cm by 3 cm. What is its area?','24 cm²'),('4.','A square has an area of 49 cm². How long is each side?','7 cm')]
body=h2('Quick questions')+''.join(qrow(128,260+i*150,1250,a,b) for i,(a,b,c) in enumerate(qs))+''.join(answer(1420,260+i*150,372,c) for i,(a,b,c) in enumerate(qs))
put(PFX+'warm2',S_(PFX+'warm2','5–10 MIN',body,'Minutes 5 to 10. Whiteboards. Read each question, give thinking time, then click to show the answer. Answers: 1) 56  2) 24 cm (6 + 6 + 6 + 6, or 4 × 6)  3) 24 cm² (8 × 3)  4) 7 cm (7 × 7 = 49). Ask after 2 and 3: "Both answers are 24. Are they the same?" No: 24 cm is a length round the edge; 24 cm² is 24 squares of space inside. Check every child writes cm² for an area.'))

# ================= 4. explore: what to do =================
ex=''
import random
random.seed(7)
for i in range(12):
    x=40+(i%4)*100+random.randint(-8,8); y=22+(i//4)*72+random.randint(-6,6); r=random.randint(-14,14)
    ex+=f'<g transform="rotate({r} {x+28} {y+28})">'+R(x,y,56,56,SKY,NAVY,3)+'</g>'
ex+=ARW(470,120,600,120,TEAL,8,26)
tx=640; cw_=190
for j,hd in enumerate(['Length','Breadth','Perimeter']):
    ex+=R(tx+j*cw_,20,cw_,54,YEL,NAVY,3)+T(tx+j*cw_+cw_/2,57,hd,28)
    for k in range(3): ex+=R(tx+j*cw_,74+k*50,cw_,50,WHITE,NAVY,3)
ex+=R(1250,40,320,150,SOFT,NAVY,3,14)+T(1410,100,'Use ALL 12.',32)+T(1410,150,'Every rectangle?',30,TEAL)
exsvg=SV(1600,236,ex,'Twelve loose squares, an arrow, and an empty table with columns Length, Breadth and Perimeter')
steps='<ol style="font-size:34px;font-weight:600;padding-left:48px;display:flex;flex-direction:column;gap:4px;margin:0"><li>Take 12 squares.</li><li>Make a rectangle using ALL 12 squares.</li><li>Record its length, breadth and perimeter in a table.</li><li>Make every different rectangle. Which has the longest perimeter?</li></ol>'
body=h2('Explore: what to do')+card(chip('EXPLORE')+steps,extra='padding:22px 40px')+card(exsvg,extra='padding:14px 32px')
put(PFX+'explore1',S_(PFX+'explore1','10–15 MIN',body,'Minutes 10 to 15. Pairs (or each child online) build rectangles with exactly 12 squares and fill in the table on a whiteboard or squared paper. Predict first: "Will every rectangle have the same perimeter?" Remind: a rectangle turned round is the same rectangle. Hints: "Put 2 squares in each row. How many rows?" "Run your finger round the edge and count every side you pass." Ready for more: "Can you make a 12-square rectangle with a perimeter of 20 cm?" (No.) Online: cut squares from squared paper, or just draw the rectangles on squared paper.'))

# ================= 5. explore: talk =================
put(PFX+'explore2',cards_slide(PFX+'explore2','15–25 MIN','Explore: talk about it',[('1.','How many different rectangles did you make with 12 squares?'),('2.','They all have the same area. Do they have the same perimeter?'),('3.','Which has the longest perimeter? Why do you think so?')],
 'Minutes 15 to 25. Let pairs keep working, then gather the group. Make a class table in order: 1 by 12, 2 by 6, 3 by 4. Answers: 1) 3 rectangles (12 by 1, 6 by 2, 4 by 3; turning one round does not make a new one). 2) No: 26 cm, 16 cm and 14 cm. Same area, different perimeters! 3) The long thin 12 by 1: when squares are in a long line, fewer of their sides touch, so more sides are on the outside. The fattest one (4 by 3, closest to a square) has the shortest perimeter. Ask: "How do you know you have them all?" (We tried 1 row, 2 rows, 3 rows; 4 rows is the 3 by 4 turned round; 5 rows does not work.) That is listing in order: today\'s first heuristic.',size=40))

# ================= 6. teach 1: list in order =================
body=h2('Same fence, different gardens')+stitle('Ravi has 20 m of fence for a rectangular garden. Each side is a whole number of metres. Which gardens can he make?')
body+=step(1,'Half the fence goes on one length and one breadth: 20 ÷ 2 = 10 m. So length + breadth = 10.',top=330,size=34)
W3=[220,220,300]
body+=trow(128,460,['Breadth','Length','Area'],W3,None,True,32)
for k,(b_,l_) in enumerate([(1,9),(2,8),(3,7),(4,6),(5,5)]):
    body+=trow(128,532+k*72,[f'{b_} m',f'{l_} m',f'{b_*l_} m²'],W3,'rise',False,32)
body+=soft(1010,460,782,'Step 2. List in order: breadth 1, 2, 3 … Stop at 5 and 5. After that the gardens are the same ones turned round.',32)
body+=answer(1010,720,782,'5 gardens. Same fence, different areas. Biggest: 5 m by 5 m = 25 m²')
put(PFX+'teach1',S_(PFX+'teach1','25–27 MIN',body,'Teach heuristic 1: make a list in order. Click 1: half the fence. Ask: "Why half?" (The fence goes length, breadth, length, breadth: one length and one breadth is half of it.) Clicks 2 to 6: build the table row by row; children call out each row. Click 7: the stop rule. Click 8: the answer. '
 'Think-aloud: "If I guess gardens at random I might miss one or write one twice. So I start with breadth 1 and go up by 1 each time. When breadth and length are both 5 I stop, because 6 and 4 is just 4 and 6 turned round." Point at the Area column: "Same fence, but the areas go 9, 16, 21, 24, 25. The closer to a square, the bigger the area." This is a parallel example: the worksheet uses 18 m.'))

# ================= 7. try 1 =================
put(PFX+'try1',foot(try_slide(PFX+'try1','27–28 MIN','Your turn: list in order','Whiteboards. Halve the perimeter first.',[('a','Perimeter 12 cm, whole-cm sides. How many rectangles?','3'),('b','Which of those rectangles has the biggest area?','3 by 3: 9 cm²'),('c','A rectangle has perimeter 14 cm and area 12 cm². Its sides?','4 cm and 3 cm')],
 'Whiteboards together, then click. a) Length + breadth = 6: 5 and 1, 4 and 2, 3 and 3. That is 3 rectangles. b) Areas 5, 8, 9 cm²: the 3 by 3 square is biggest. c) Length + breadth = 7: list 6 and 1 (area 6), 5 and 2 (10), 4 and 3 (12). So 4 cm and 3 cm. Ask a child to explain how the list helped in c.',size=36)))

# ================= 8. teach 2: push the steps out (grid) =================
c=100; o=40
stair=[(0,0),(0,1),(0,2),(1,1),(1,2),(2,2)]
base=SV(380,380,bgrid(o-c*0+0,o,3,3,c)+cellsfig(stair,o,o,c),'A staircase of 6 squares: columns of 3, 2 and 1 squares')
poly=[(0,0),(1,0),(1,1),(2,1),(2,2),(3,2),(3,3),(0,3)]
labs=''; k=0
for i in range(len(poly)):
    (x1,y1),(x2,y2)=poly[i],poly[(i+1)%len(poly)]
    n_=int(abs(x2-x1)+abs(y2-y1)); dx_=(x2-x1)/n_; dy_=(y2-y1)/n_
    for s_ in range(n_):
        k+=1; mx=x1+dx_*(s_+0.5); my=y1+dy_*(s_+0.5); nx,ny=dy_,-dx_
        labs+=T(o+mx*c+nx*24,o+my*c+ny*24+10,k,28,TEAL,800)
ov1=SV(380,380,labs,'the 12 edges numbered')
ov2=SV(380,380,R(o,o,300,300,'none',TEAL,6,0,' stroke-dasharray="16 10"')+ARW(o+125,o+100,o+125,o+12,RED,6,18)+ARW(o+225,o+200,o+225,o+12,RED,6,18)+ARW(o+100,o+25,o+288,o+25,RED,6,18)+ARW(o+200,o+125,o+288,o+125,RED,6,18),'steps pushed out to a 3 by 3 square')
body=h2('Change the shape: push the steps out')+stitle('Each square is 1 cm. What is the perimeter of this staircase?')
body+=pin(128,310,380,base)
body+=ostep(128,310,1,'Walk round and count every edge: 12 edges, so 12 cm.',ov1,380,380,dx=440,dy=10,tw=1224)
body+=ostep(128,310,2,'Push the steps out: slide the top pieces up and the side pieces right. Now it is a 3 by 3 square.',ov2,380,380,dx=440,dy=120,tw=1224)
body+=ostep(128,310,3,'Pushing out does not change any lengths. Perimeter = 3 + 3 + 3 + 3 = 12 cm ✓',dx=440,dy=270,tw=1224)
body+=soft(128,730,1664,'Careful: this works for steps. A dent going into the shape has two extra walls. Look out for dents!',32)
put(PFX+'teach2',S_(PFX+'teach2','28–30 MIN',body,'Teach heuristic 2: change the shape. Ask first: "What is the perimeter?" Let them count. Click 1: the 12 edges numbered (walk round with your finger). Click 2: the red arrows slide each step piece out to the dashed square. Click 3: same lengths, so same perimeter as the 3 by 3 square. '
 'Think-aloud: "Counting edges works, but it is slow and I can lose my place. When a shape goes down in steps, I can push the steps out. The pieces facing up slide up and make the top. The pieces facing right slide right and make the right side. Nothing gets longer or shorter, so the perimeter is the same as the big square." Click 4: the warning about dents (we test it in Your turn c). This is a parallel example: the worksheet staircase has 4 steps.'))

# ================= 9. worked example: no grid, steps unmarked =================
s_=50; ox=120; oy=34
def P(x,y): return (ox+x*s_, oy+(6-y)*s_)
pts=[(0,0),(8,0),(8,2),(5,2),(5,4),(3,4),(3,6),(0,6)]
base=SV(580,400,PG([P(*q) for q in pts],SKY,NAVY,6)+T(ox+200,oy+300+46,'8 cm',34)+T(ox-14,oy+162,'6 cm',34,NAVY,700,'end'),'A staircase shape 8 cm wide and 6 cm tall with three steps. The step lengths are not marked.')
up=[((0,6),(3,6)),((3,4),(5,4)),((5,2),(8,2))]; rt=[((3,6),(3,4)),((5,4),(5,2)),((8,2),(8,0))]
ov1=SV(580,400,''.join(LN(*P(*a),*P(*b),YEL,12) for a,b in up)+LN(*P(0,6),*P(8,6),TEAL,5,'14 10')+ARW(*P(4,4.1),*P(4,5.9),RED,6,16)+ARW(*P(6.5,2.1),*P(6.5,5.9),RED,6,16),'pieces facing up slide to the top')
ov2=SV(580,400,''.join(LN(*P(*a),*P(*b),RED,12) for a,b in rt)+LN(*P(8,6),*P(8,0),TEAL,5,'14 10')+ARW(*P(3.1,5),*P(7.9,5),RED,6,16)+ARW(*P(5.1,3),*P(7.9,3),RED,6,16),'pieces facing right slide to the right side')
body=h2('Worked example: the steps have no numbers!')+stitle('Find the perimeter of this staircase.')
body+=pin(128,300,580,base)
body+=ostep(128,300,1,'Slide every piece that faces up to the top. Together they are as long as the bottom: 8 cm.',ov1,580,400,dx=620,dy=0,tw=1044)
body+=ostep(128,300,2,'Slide every piece that faces right. Together they are as tall as the left side: 6 cm.',ov2,580,400,dx=620,dy=150,tw=1044)
body+=answer(748,610,1044,'Perimeter = 8 + 6 + 8 + 6 = 28 cm')
put(PFX+'we2',S_(PFX+'we2','30–31 MIN',body,'Ask first: "Can we find the perimeter when we do not know how long each step is?" Many will say no. Click 1: the yellow pieces all face up; they slide up and make a top side as long as the bottom, 8 cm. Click 2: the red pieces face right; they slide right and make a right side as tall as the left, 6 cm. Click 3: 8 + 6 + 8 + 6 = 28 cm. '
 'Think-aloud: "I do not need the step lengths. The up-facing pieces must add up to the bottom, because the shape goes all the way across. The right-facing pieces must add up to the left side, because the shape goes all the way up." (Check: the steps are 3, 2, 3 cm across and 2, 2, 2 cm up.)'))

# ================= 10. try 2 (with dent) =================
def mini(cells,c,lab):
    W_=max(a for a,b in cells)+1; H_=max(b for a,b in cells)+1
    return SV(W_*c+10,H_*c+10,cellsfig(cells,5,5,c,SKY,5,False),lab)
st7=[(x,y) for x,h in enumerate([4,4,3,3,2,1,1]) for y in range(4-h,4)]
sqc=[(x,y) for x in range(6) for y in range(6) if not (x>=4 and y<2)]
sqn=[(x,y) for x in range(6) for y in range(6) if not (2<=x<4 and y<2)]
rows=[('a',mini(st7,18,'a staircase 7 wide and 4 tall'),'A staircase is 7 cm wide and 4 cm tall. Perimeter?','22 cm'),
      ('b',mini(sqn if False else sqc,20,'a 6 by 6 square with a 2 by 2 corner cut away'),'A 6 cm square has a 2 cm square cut from one corner. Perimeter?','24 cm'),
      ('c',mini(sqn,20,'a 6 by 6 square with a 2 by 2 dent cut from the middle of the top'),'Now the 2 cm square is cut from the middle of a side. Perimeter?','28 cm')]
body=h2('Your turn: push out, but watch for dents')+stitle('Whiteboards. Draw it first.')
for i,(l,pic,t,a) in enumerate(rows):
    tp=300+i*190
    body+=pin(128,tp,1250,f'<div style="display:flex;align-items:center;gap:28px"><p style="font-size:38px;font-weight:800;color:{TEAL};flex:none">{l}</p><div style="flex:none;width:140px;display:flex;justify-content:center">{pic}</div><p style="font-size:34px;font-weight:600;line-height:1.3">{E(t)}</p></div>',None,WHITE,20,'14px 28px')
    body+=answer(1420,tp+20,372,a)
put(PFX+'try2',S_(PFX+'try2','31–32 MIN',body,'Whiteboards, then click. a) Push out: a 7 by 4 rectangle, 7 + 4 + 7 + 4 = 22 cm, whatever the steps are. b) A cut corner pushes out: still 6 + 6 + 6 + 6 = 24 cm (the area drops to 32 cm², but the perimeter stays the same!). c) A dent: pushing out gives 24 cm, but the dent has two walls of 2 cm inside it, so 24 + 2 + 2 = 28 cm. Ask: "Why are b and c different?" In b the cut pieces face out and slide out; in c the two walls of the dent face each other and cannot slide anywhere.'))

# ================= 11. teach 3: area two ways =================
k_=45; ox=110; oy=40
def Q(x,y): return (ox+x*k_, oy+(6-y)*k_)
Lp=[(0,0),(8,0),(8,4),(5,4),(5,6),(0,6)]
base=SV(540,370,PG([Q(*q) for q in Lp],SKY,NAVY,6)+T(ox+112,oy-12,'5 cm',30)+T(ox-12,oy+146,'6 cm',30,NAVY,700,'end')+T(ox+180,oy+270+40,'8 cm',30)+T(ox+360+12,oy+182,'4 cm',30,NAVY,700,'start'),'An L-shape: bottom 8 cm, left 6 cm, top 5 cm, right 4 cm, with a corner missing at the top right')
ov1=SV(540,370,f'<rect x="{ox}" y="{oy}" width="{5*k_}" height="{6*k_}" fill="{YEL}" opacity=".55"/><rect x="{ox+5*k_}" y="{oy+2*k_}" width="{3*k_}" height="{4*k_}" fill="{TEAL}" opacity=".3"/>'+LN(ox+5*k_,oy+2*k_,ox+5*k_,oy+6*k_,RED,5,'12 8')+T(ox+112,oy+150,'5 × 6',30)+T(ox+292,oy+195,'3 × 4',28),'cut into a 5 by 6 rectangle and a 3 by 4 rectangle')
fill=SV(300,210,PG([(20+x*24,10+(6-y)*24) for x,y in Lp],SKY,NAVY,4)+R(20+5*24,10,3*24,2*24,YEL,RED,4,0,' stroke-dasharray="8 6"')+T(20+6.5*24,10+24+9,'3 × 2',24)+T(130,200,'8 × 6 − 3 × 2',26,TEAL),'the missing corner filled in')
body=h2('Area: cut it up, or fill it in')+stitle('Find the area of this L-shape in two ways.')
body+=pin(128,300,540,base)
body+=ostep(128,300,1,'Cut it into two rectangles: 5 × 6 = 30 and 3 × 4 = 12.  30 + 12 = 42 cm².',ov1,540,370,dx=590,dy=0,tw=1074)
body+=ostep(128,300,2,'Or fill in the missing corner: 8 × 6 = 48. Take away the corner: 3 × 2 = 6.  48 − 6 = 42 cm².',None,0,0,dx=590,dy=150,tw=1074,row=True,twt=680,extra=fill)
body+=answer(128,700,1664,'Both ways give 42 cm². Two ways agree, so we can trust our answer.')
put(PFX+'teach3',S_(PFX+'teach3','32–34 MIN',body,'Teach: change the shape for area. First ask: "Which sides do we know? Which are missing?" (The step is 3 cm across, 8 − 5, and 2 cm down, 6 − 4.) Click 1: cut along the red line into a 5 by 6 and a 3 by 4 rectangle. Click 2: the second way: fill in the corner to make an 8 by 6 rectangle, then take the corner away. Click 3: both give 42. '
 'Think-aloud: "I cannot find the area of an L-shape in one go, so I change it into rectangles. I can cut it up, or fill it in and take away. If both ways give the same answer, I know I am right." Also ask: "What is its perimeter?" (Push out: 8 + 6 + 8 + 6 = 28 cm.) Parallel example: the worksheet L-shape is 10 cm by 7 cm.'))

# ================= 12. key idea =================
body=h2('Key idea: list in order, change the shape')+card(p('Perimeter: push the steps out, but add the walls of a dent. Area: cut it into rectangles, or fill it in and take away.',42,700))+card(p('Same perimeter does not mean same area. List rectangles in order so none are missed.',38,600,MUTED))
put(PFX+'key',S_(PFX+'key','34–35 MIN',body,'Say the key ideas together. Common mistakes to watch for during the worksheet: (1) Mixing up area and perimeter, or writing cm for an area (it is cm²). (2) Counting squares along the edge instead of edges for perimeter: a corner square has 2 edges on the outside, so count edges, not squares. (3) Pushing out a shape with a dent and forgetting the dent\'s two walls. (4) In Q2, listing a garden twice (5 by 4 and 4 by 5) or missing one because the list is not in order. (5) Finding the missing sides of the L-shape wrongly: take away, do not add.'))

# ================= 13. break =================
put(PFX+'break',break_slide(PFX+'break','35–40 MIN','Perimeter march. March on the spot and trace a big square in the air, counting its 4 sides. Now stretch tall and thin like a 9 by 1 garden, then wide like a 5 by 5 garden.','Then: a drink of water and back to our seats.','Five minutes. Online: children stay in view of the camera and move in place.'))

# ================= 14. teach before page 1: square with the same perimeter =================
rect=SV(560,330,R(20,20,270,90,SKY,NAVY,5)+T(155,150,'9 cm by 3 cm',28)+R(330,20,180,180,YEL,NAVY,5)+T(420,240,'square',28)+T(420,120,'?',60,NAVY),'A 9 cm by 3 cm rectangle and a square')
body=h2('Same perimeter: a square and a rectangle')+card(p('A square has the same perimeter as a rectangle 9 cm by 3 cm. What is the area of the square?',38,700),extra='padding:24px 40px')
body+=pin(1232,400,560,rect)
body+=step(1,'Perimeter of the rectangle: 9 + 3 + 9 + 3 = 24 cm.',top=400,width=1060,size=34)
body+=step(2,'A square has 4 equal sides: 24 ÷ 4 = 6 cm each.',top=520,width=1060,size=34)
body+=step(3,'Area of the square: 6 × 6 = 36 cm².',top=640,width=1060,size=34)
body+=soft(128,760,1664,'The rectangle\'s area is only 9 × 3 = 27 cm². Same perimeter, different area again!',32)
put(PFX+'teachsq',S_(PFX+'teachsq','40–41 MIN',body,'Teach before worksheet page 1 (Q3 asks the same kind of question with different numbers). Click through the steps. Ask before step 2: "What do we know about the sides of a square?" (all 4 the same). Think-aloud: "Same perimeter means the same fence. I find the fence of the rectangle, then share it equally among the 4 sides of the square." Point out the link to teach 1: the square has the bigger area.'))

# ================= 15/16. page 1 =================
put(PFX+'ws1',preview(PFX+'ws1','41–52 MIN','Worksheet page 1: with your partner',[('Q1','Area and perimeter on a grid. Then compare the four figures.'),('Q2','Every garden with an 18 m fence. Halve it, then list in order.'),('Q3','A square with the same perimeter as a rectangle.')],'Stuck? Count the edges with your pencil tip, and write cm² for area.','Minutes 41 to 52. Walk around. Ask "How do you know?" before giving any help. Q1: check children count edges, not squares, for the perimeter, and push out where they can (B is a staircase). Q2: "What do length and breadth add up to?" (9).'))
put(PFX+'ws1ans',checkrows(PFX+'ws1ans','52–54 MIN','Page 1: check together',[('Q1','A: 8 cm², 12 cm.  B: 8 cm², 14 cm.  C: 9 cm², 12 cm.  D: 5 cm², 12 cm.'),('Q1 a, b','a) A and B: same area 8 cm².   b) A, C and D: all 12 cm.'),('Q2','8 by 1: 8 m²,  7 by 2: 14 m²,  6 by 3: 18 m²,  5 by 4: 20 m².  Biggest: 5 m by 4 m.'),('Q3','20 cm round the rectangle, so the square has 5 cm sides: 5 × 5 = 25 cm².')],
 'Click each answer after a pair explains theirs. Q1: B pushes out to a 5 by 2 rectangle: 5 + 2 + 5 + 2 = 14. D has a dent: pushing out gives a 3 by 2 rectangle (10 cm), plus the 2 walls of the dent: 12 cm. Q1b is surprising: three very different figures, one perimeter. Q2: length + breadth = 9. Q3: 7 + 3 + 7 + 3 = 20, 20 ÷ 4 = 5.',lw=230,size=32,gap=140))

# ================= 17. teach before page 2: add one square =================
c=70
L3=[(0,0),(0,1),(1,1)]
def panel(x,extra_cells,title,sub,col=SKY):
    g=bgrid(x+40,10,4,3,c)+cellsfig(L3,x+40+c,10,c)
    if extra_cells: g+=cellsfig(L3+extra_cells,x+40+c,10,c,SKY)+R(x+40+c+extra_cells[0][0]*c,10+extra_cells[0][1]*c,c,c,YEL,NAVY,6)
    return g+T(x+180,262,title,30)+T(x+180,302,sub,28,TEAL)
pA=SV(540,320,panel(0,None,'Start: 3 squares','perimeter 8 cm'),'An L of 3 squares, perimeter 8 cm')
pB=SV(540,320,panel(0,[(2,1)],'Touches 1 side','8 + 4 − 2 = 10 cm'),'A new square touching 1 side: perimeter 10 cm')
pC=SV(540,320,panel(0,[(1,0)],'Touches 2 sides','8 + 4 − 4 = 8 cm'),'A new square touching 2 sides: perimeter stays 8 cm')
body=h2('Add one square: what happens to the perimeter?')+stitle('Each square is 1 cm. The new square is yellow.')
body+=pin(128,290,540,pA)+pin(690,290,540,pB,'fade')+pin(1252,290,540,pC,'fade')
body+=soft(128,640,1664,'A new square brings 4 new edges. Every side it touches hides 2 edges: one of its own and one of the shape\'s.',32)
body+=answer(128,790,1664,'Touch 1 side: + 2 cm.   Touch 2 sides: no change.   Touch 3 sides: − 2 cm.')
put(PFX+'teachadd',S_(PFX+'teachadd','54–56 MIN',body,'Teach before worksheet page 2 (Q6 adds one square to an L of 4 squares; this L has 3). Show panel 1 and count the edges together: 8. Click 1: the yellow square touches the L along 1 side. Count: 10. Click 2: the yellow square fills the gap and touches 2 sides: still 8, and now it is a 2 by 2 square. Click 3 and 4: the reason and the rule. '
 'Think-aloud: "The new square has 4 edges. Where it touches the shape, that edge is inside now, and so is the shape\'s edge it touches. So each touch hides 2 edges." Ask: "What would a square that touches 3 sides do?" (take away 2). "Where would it have to go?" (into a gap with walls on 3 sides).'))

# ================= 18/19. page 2 =================
put(PFX+'ws2',preview(PFX+'ws2','56–68 MIN','Worksheet page 2: on your own',[('Q4','An L-shape: find the missing sides, then the area and the perimeter.'),('Q5','A staircase. Push the steps out.'),('Q6','If time: add one square to an L. Count the sides it touches.')],'Ready for more? Stretch and Challenge come next.','Children work alone. Note who needs a short catch-up next lesson. Q4: check the missing sides first (take away). Q6b has only one answer: ask "How many sides must the new square touch?"'))
put(PFX+'ws2ans',checkrows(PFX+'ws2ans','68–70 MIN','Page 2: check together',[('Q4','Missing sides 4 cm and 3 cm.  Area 58 cm².  Perimeter 34 cm.'),('Q5','a) 10 cm²   b) 16 cm   c) perimeter stays 16 cm; area goes up by 6 cm² to 16 cm²'),('Q6','a) any square touching 1 side   b) only the gap beside the middle square   c) no')],
 'Click each answer after a child explains. Q4: 10 − 6 = 4 and 7 − 4 = 3. Area: 6 × 7 + 4 × 4 = 42 + 16 = 58, or 10 × 7 − 4 × 3 = 70 − 12 = 58. Perimeter: push the step out: 10 + 7 + 10 + 7 = 34. Q5: pushing out the steps gives the 4 by 4 square, so filling it in does not change the perimeter; 16 − 10 = 6 more squares. Q6: the only empty square touching 2 sides of the L is the one to the right of the middle square. For 8 cm the new square would need to touch 3 sides: there is no gap like that.',lw=200,size=32,gap=170))

# ================= 20. stretch (new items) =================
put(PFX+'stretch',cards_slide(PFX+'stretch','For early finishers','Stretch',[('1.','Find all the rectangles with whole-cm sides and an area of 16 cm². Which has the shortest perimeter?'),('2.','A square has a perimeter of 32 cm. It is cut into two same-size rectangles. What is the perimeter of each rectangle?'),('3.','Draw a figure of 7 squares (each 1 cm) with a perimeter of 12 cm.')],
 'For children who finish early. Answers: 1) 16 by 1 (34 cm), 8 by 2 (20 cm), 4 by 4 (16 cm): the 4 by 4 square has the shortest perimeter. 2) Side 32 ÷ 4 = 8 cm, so each rectangle is 8 cm by 4 cm: perimeter 24 cm. 3) For example a 2 by 4 rectangle with one corner square missing, or a 3 by 3 square with two corners missing (corners pushed out: still 12 cm). Squeeze the squares together as much as you can.',size=36))

# ================= 21. challenge =================
put(PFX+'challenge',cards_slide(PFX+'challenge','65–80 MIN','Challenge',[('1.','Ali joins 5 same-size squares with sides of 2 cm, whole sides touching. What is the biggest perimeter his shape can have? The smallest?'),('2.','A rectangle 7 cm by 5 cm has a 1 cm square cut out of each of its 4 corners. Find the new area and the new perimeter.')],
 'Use as a pair challenge or in talk time. Ask for the reason every time. Answers: 1) Biggest 24 cm (12 edges of 2 cm, e.g. a row of 5); smallest 20 cm (10 edges: a 2 by 2 square with one more square on a side). 2) Area 35 − 4 = 31 cm². Perimeter 24 cm, the same as before. More are in the question bank.',size=36))

# ================= 22. challenge: see it =================
g1=''.join(R(40+i*120,40,90,90,SKY,NAVY,4) for i in range(5))+T(85,165,'2 cm',26)+T(330,240,'Join whole sides.',30)+T(330,290,'Push them apart or squeeze them together.',26,TEAL)
g1+=bgrid(140,320,8,3,48)+T(330,500,'Biggest perimeter?  Smallest?',30)
k2=48; ox2=160; oy2=80
g2=R(ox2,oy2,7*k2,5*k2,SKY,NAVY,5)+''.join(R(ox2+a*k2,oy2+b*k2,k2,k2,WHITE,RED,4,0,' stroke-dasharray="8 6"') for a,b in [(0,0),(6,0),(0,4),(6,4)])
g2+=T(ox2+3.5*k2,oy2-18,'7 cm',30)+T(ox2-14,oy2+2.5*k2+10,'5 cm',30,NAVY,700,'end')+T(ox2-14,oy2+k2/2+9,'1 cm',24,RED,700,'end')+T(330,420,'Cut out the 4 corner squares.',30)+T(330,470,'New area?  New perimeter?',30,TEAL)
pan=lambda t,s_: f'<div style="background:{WHITE};border-radius:24px;padding:20px 24px;display:flex;flex-direction:column;gap:10px;flex:1;min-width:0"><p style="font-size:30px;font-weight:700;color:{TEAL}">{E(t)}</p>{s_}</div>'
body=h2('Challenge: see it',60)+f'<div style="display:flex;gap:32px;align-items:flex-start">{pan("Q1: five 2 cm squares",SV(660,520,g1,"Five separate 2 cm squares and an empty grid to arrange them on"))}{pan("Q2: corners cut out",SV(660,520,g2,"A 7 cm by 5 cm rectangle with a 1 cm square marked at each corner to be cut out"))}</div>'
put(PFX+'chdiag',S_(PFX+'chdiag','65–80 MIN',body,'Show after pairs have tried the Challenge, or if they are stuck. The pictures show the problem, not the answer. Ask: What do you notice? What do we know? Which heuristic could help: push out, or count the touching sides? Answers are in the Challenge slide notes.'))

# ================= 23. challenge walk-through =================
body=h2('Challenge: walk-through')+pin(128,250,800,p('Q1: count the touching sides',36,800,TEAL))
for i,t in enumerate(['5 squares have 20 edges. Each touch hides 2.','A row of 5: 4 touches, 12 edges: 24 cm.','2 by 2 square + 1: 5 touches, 10 edges: 20 cm.','Biggest 24 cm, smallest 20 cm ✓']): body+=pin(128,330+i*120,800,p(t,32),'rise',WHITE)
body+=pin(992,250,800,p('Q2: change the shape',36,800,TEAL))
for i,t in enumerate(['Area: 7 × 5 = 35.  35 − 4 = 31 cm²','Perimeter: push each cut corner out.','It is the 7 by 5 rectangle again.','7 + 5 + 7 + 5 = 24 cm: no change ✓']): body+=pin(992,330+i*120,800,p(t,32),'rise',WHITE)
put(PFX+'chwalk',S_(PFX+'chwalk','Challenge',body,'Use after pairs have tried. Q1: 5 squares joined need at least 4 touches, so at most 20 − 8 = 12 edges. The most touches we can get is 5 (a 2 by 2 block uses 4 touches, the fifth square adds 1), so at least 20 − 10 = 10 edges. Each edge is 2 cm. Q2: cutting a corner square out takes away area but the two new edges are just the old edges pushed in, so the perimeter does not change.'))

# ================= 24. talk =================
body=h2('Talk time')+card(chip('TALK TIME',YEL,NAVY)+p('Two gardens have the same perimeter. Must they have the same area? Show an example.',42,600))+card(p('Sentence starters:',34,400,MUTED)+p('“I noticed that …”   “I tested it by …”   “I know because …”',38,600))
put(PFX+'talk',S_(PFX+'talk','70–80 MIN',body,'Minutes 70 to 80. Pairs talk for 2 minutes, then share. Answer: No. A 9 m by 1 m garden and a 5 m by 5 m garden both have a 20 m fence, but the areas are 9 m² and 25 m². Follow-up: "When does pushing out the steps NOT work?" (When the shape has a dent: the walls of the dent are extra.) Praise the reasons, not only the answers.'))

# ================= 25. exit =================
body=h2('Exit ticket')+card(chip('EXIT TICKET')+p('A rectangle has a perimeter of 12 cm. Its length is 4 cm. What is its area?',46,600))+card(p('Write your answer on a slip of paper. Show it to your tutor. Then collect your stamp in your inquiry journal.',34,400))
put(PFX+'exit',S_(PFX+'exit','80–90 MIN',body,'Minutes 80 to 90. Answer: 8 cm². Length + breadth = 12 ÷ 2 = 6, so the breadth is 2 cm; 4 × 2 = 8. Children who write 48 multiplied 12 × 4; children who write 8 cm found the breadth as 12 − 4. Extension: find all the rectangles with whole-cm sides and a perimeter of 24 cm. Which has the biggest area? (6 rectangles; 6 by 6, 36 cm²)'))

# ---------- write ----------
order=['title','warm1','warm2','explore1','explore2','teach1','try1','teach2','we2','try2','teach3','key','break','teachsq','ws1','ws1ans','teachadd','ws2','ws2ans','stretch','challenge','chdiag','chwalk','talk','exit']
order=[PFX+o for o in order]
os.makedirs(os.path.join(D,'slides'),exist_ok=True)
import p3_gifted; order[:]=p3_gifted.add(S,order,7)  # close-the-gaps: warm-up check + look-back slides
import p3_stories; order[:]=p3_stories.add(S,order,7)  # mathematician story break (optional)
for f in os.listdir(os.path.join(D,'slides')):
    if f.startswith(PFX) and f[:-5] not in order: os.remove(os.path.join(D,'slides',f))
for i,h in S.items(): open(os.path.join(D,'slides',i+'.html'),'w').write(h)
deck={'v':4,'createdOnFiles':{'v':1,'at':datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')},'lists':'css',
      'title':'Math Inquirers P3: Lesson 7 – Area Architects','order':order,'cover':PFX+'title',
      'sections':{'s1':{'description':'Warm-up and explore','start':PFX+'title'},'s2':{'description':'Teach: list in order, and change the shape','start':PFX+'teach1'},
                  's3':{'description':'Worksheet with teaching before each page','start':PFX+'break'},'s4':{'description':'Think harder, go further, talk and exit','start':PFX+'stretch'}},
      'faces':{'fredoka':{'family':'Fredoka','href':'https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&display=swap'},'nunito-sans':{'family':'Nunito Sans','href':'https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@400;600;700&display=swap'}},
      'designSystems':[]}
json.dump(deck,open(os.path.join(D,'deck.json'),'w'),indent=1,ensure_ascii=False)
missing=[i for i in order if not os.path.exists(os.path.join(D,'slides',i+'.html'))]
print(len(order),'slides; wrote',len(S),'missing',missing)
