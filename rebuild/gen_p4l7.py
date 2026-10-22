"""Math Inquirers P4, Lesson 7: Area Architects II. Writes split/p4l7/project (deck.json + slides/*.html)."""
import json,os,sys,datetime
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,H)
import slidekit
from slidekit import *
slidekit.FOOT='Math Inquirers P4 Holiday Program  •  Notice it. Test it. Explain why.'
D=os.path.join(H,'..','split','p4l7','project'); os.makedirs(os.path.join(D,'slides'),exist_ok=True)
S={}
def put(i,h): S[i]=h
RED='#D64545'; MINT='#D3F1E4'; FOOTX=slidekit.FOOT

# ---------- shared slide shapes (same look as the approved decks) ----------
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

# ---------- SVG helpers (1 grid square = 1 cm) ----------
def SV(w,h,body,label): return f'<svg aria-label="{E(label)}" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="width:{w}px;height:{h}px;flex:none">{body}</svg>'
def T(x,y,s,size=34,fill=NAVY,anchor='middle',weight=700): return f'<text x="{x:.0f}" y="{y:.0f}" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" fill="{fill}" font-family="Fredoka, Arial">{E(str(s))}</text>'
def grid(x0,y0,cols,rows,c,op=0.25):
    d=''.join(f'M{x0+i*c} {y0} V{y0+rows*c} ' for i in range(cols+1))+''.join(f'M{x0} {y0+j*c} H{x0+cols*c} ' for j in range(rows+1))
    return f'<path d="{d}" stroke="{NAVY}" stroke-width="1.5" opacity="{op}" fill="none"/>'
def PL(ox,oy,c,pts,fill=SKY,stroke=NAVY,sw=5,dash=''):
    da=f' stroke-dasharray="{dash}"' if dash else ''
    return f'<polygon points="{" ".join(f"{ox+a*c:.0f},{oy+b*c:.0f}" for a,b in pts)}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round"{da}/>'
def RC(ox,oy,c,a,b,w,h,fill=SKY,stroke=NAVY,sw=5,dash='',op=1):
    da=f' stroke-dasharray="{dash}"' if dash else ''
    o=f' fill-opacity="{op}"' if op!=1 else ''
    return f'<rect x="{ox+a*c:.0f}" y="{oy+b*c:.0f}" width="{w*c:.0f}" height="{h*c:.0f}" fill="{fill}"{o} stroke="{stroke}" stroke-width="{sw}"{da}/>'
def LN(ox,oy,c,a,b,a2,b2,col=RED,sw=8,dash=''):
    da=f' stroke-dasharray="{dash}"' if dash else ''
    return f'<line x1="{ox+a*c:.0f}" y1="{oy+b*c:.0f}" x2="{ox+a2*c:.0f}" y2="{oy+b2*c:.0f}" stroke="{col}" stroke-width="{sw}" stroke-linecap="round"{da}/>'
def ostep(left,top,n,text,ov=None,ovw=0,ovh=0,dx=0,dy=0,tw=1000,size=34,build='fade'):
    """One click = overlay marks on the picture (same left/top as the base picture) + the step text box beside it."""
    lab=f'<span style="color:{TEAL};font-weight:800">Step {n}.</span>  ' if n else ''
    box=f'<div style="margin-top:{dy}px;width:{tw}px;box-sizing:border-box;background:{WHITE};border-radius:20px;padding:16px 28px;flex:none"><p style="font-size:{size}px;font-weight:600;line-height:1.3">{lab}{E(text)}</p></div>'
    if ov is None: return pin(left+dx,top,tw,box,build)
    o=f'<div style="width:{ovw}px;height:{ovh}px;flex:none">{ov}</div>'
    return pin(left,top,dx+tw,f'<div style="display:flex;align-items:flex-start;gap:{dx-ovw}px">{o}{box}</div>',build)
def soft(left,top,width,text,size=34,build='fade'): return pin(left,top,width-56,p(text,size,700),build,SOFT,20,'18px 28px')
def stitle(t,size=34): return p(t,size,600,MUTED)

# The teaching L-shape: 8 cm by 6 cm with a 3 cm by 2 cm piece missing at the top right (NOT the worksheet figure)
LPTS=[(0,0),(5,0),(5,2),(8,2),(8,6),(0,6)]
def lfig(c,label_steps=True,lab=True):
    ox,oy=2*c,c; g=grid(0,0,12,8,c)+PL(ox,oy,c,LPTS)
    if lab:
        g+=T(ox+2.5*c,oy-12,'5 cm')+T(ox-12,oy+3*c+12,'6 cm',34,NAVY,'end')+T(ox+4*c,oy+6*c+42,'8 cm')+T(ox+8*c+12,oy+4*c+12,'4 cm',34,NAVY,'start')
    if label_steps: g+=T(ox+6.5*c,oy+2*c+46,'?',38,RED)+T(ox+5*c+14,oy+1*c+14,'?',38,RED,'start')
    return g

# ---------- 1. title ----------
put('p4l7-title',title_slide('p4l7-title','LESSON 7  •  WEEK 4','Area Architects II','Area and perimeter, rectangles and squares',
 'Find the area and perimeter of tricky shapes the smart way, and find out why the same area can have different perimeters.',
 'Objective: Find the area of a composite figure by splitting it into rectangles or by taking away a missing piece, find its perimeter by pushing the steps out to a rectangle, find every rectangle with a given area and compare their perimeters, and explain what changes when a shape is cut and rearranged. '
 'Thinking strategies taught today: SPLIT IT or TAKE AWAY, PUSH THE STEPS OUT, and MAKE A LIST IN ORDER. '
 'Materials: 1 cm square tiles or 24 paper squares per child, 1 cm grid paper, scissors, a 30 cm ruler, mini whiteboards, a paper strip 8 squares by 2 squares for cutting. '
 'Online: children cut out paper squares and 1 cm grid strips before the lesson and build on camera; the tutor draws on the grid figures on the slides. '
 'Time plan: Warm-up check 1 to 4 (two questions on the key idea; children who get both right and can say why start on the Think Harder pages at minute 34), warm-up game 4 to 6 (one short round), quick questions 6 to 8, explore 8 to 18, teaching 18 to 30 (click to reveal each step and answer; the "your turn" slides are optional, skip them if short of time), brain break 30 to 34, worksheet page 1 from 34 to 50 and check together 50 to 53, short teaching before page 2 from 53 to 58, worksheet page 2 from 58 to 76 and check together 76 to 80, talk time 80 to 85, exit ticket 85 to 88, What was hard? reflection 88 to 90. The Challenge slides and the Think Harder pages are for early finishers and for take-home: they have no fixed time slot. Online: page 1 is pair work, so allow about 2 minutes to move into and out of breakout rooms (or run page 1 as a whole-group screen-share if there are only 8 children).'))

# ---------- 2. warm-up game ----------
jobs=[('A fence round a school field','P','goes round the edge'),('Carpet for a bedroom floor','A','covers the inside'),('Lace round a tablecloth','P','goes round the edge'),
      ('Tiles for a kitchen floor','A','covers the inside'),('Wood for a photo frame','P','goes round the edge'),('Paint for one wall','A','covers the inside')]
def jobicon(kind):
    if kind=='P': g=f'<rect x="14" y="14" width="92" height="64" fill="{WHITE}" stroke="{RED}" stroke-width="9"/>'
    else: g=f'<rect x="14" y="14" width="92" height="64" fill="{YEL}" stroke="{NAVY}" stroke-width="4"/>'
    return SV(120,92,g,'perimeter: the edge' if kind=='P' else 'area: the inside')
body=h2('Warm-up: Area or Perimeter?')+p('Hold up A or P. Then say why.',36,600,MUTED)
CW=533; cards=''; ans=''
for i,(t,k,why) in enumerate(jobs):
    L=128+(i%3)*(CW+32); Tp=290+(i//3)*300
    cards+=pin(L,Tp,CW,f'<p style="font-size:24px;font-weight:800;color:{TEAL}">JOB {i+1}</p><p style="font-family:{HF};font-size:38px;font-weight:600;line-height:1.15">{E(t)}</p>',None,WHITE,24,'18px 28px',f'box-sizing:border-box;height:270px;border:4px solid {NAVY};box-shadow:8px 8px 0 {NAVY}')
    ans+=pin(L+20,Tp+156,CW-40,f'<div style="display:flex;align-items:center;gap:18px">{jobicon(k)}<p style="font-size:32px;font-weight:800;line-height:1.2">{k}: {E(why)}</p></div>','pop',SOFT,16,'8px 16px',f'box-sizing:border-box;border:3px solid {NAVY}')
put('p4l7-warm1',sec('p4l7-warm1','4–6 MIN',body+cards+ans,
 'Minutes 4 to 6 (one short round, about 2 minutes: the Warm-up check came first). Area or Perimeter? Children make two cards (or write A and P on two halves of a whiteboard). Read each job aloud. Count 3, 2, 1 and everyone shows A or P. Then click to reveal (clicks go job 1 to job 6). '
 'Ask each time: "Why?" Listen for "it covers the floor" (area, square units like m²) and "it goes round the edge" (perimeter, units like m). '
 'Job 5 is the one to argue about: the wood goes round the photo, so it is perimeter; the glass in the frame would be area. Quick finisher: "Make up a job where you need BOTH." (A garden: grass seed for the area, a fence for the perimeter.) '
 'Watch for children who say "area is length times breadth" without knowing what it measures: ask them to point to the area on the slide.'))

# ---------- 3. quick questions ----------
qs=[('1.','Area of a rectangle 7 cm by 6 cm?','42 cm²'),('2.','Perimeter of a square with sides of 9 cm?','36 cm'),('3.','Area 48 cm², length 8 cm. Breadth?','6 cm'),('4.','Perimeter of a rectangle 12 cm by 5 cm?','34 cm'),('5.','A square has perimeter 28 cm. Its area?','49 cm²')]
body=h2('Quick questions')+''.join(qrow(128,250+i*125,1250,a,b) for i,(a,b,c) in enumerate(qs))+''.join(answer(1420,250+i*125,372,c) for i,(a,b,c) in enumerate(qs))
put('p4l7-warm2',sec('p4l7-warm2','6–8 MIN',body,'Minutes 6 to 8. Whiteboards up together, then click. Insist on units: cm for perimeter, cm² for area. After 3 ask: "How did you find the breadth?" (48 ÷ 8, or which number times 8 makes 48). After 5: "Why is the side 7?" (28 ÷ 4 = 7, all four sides are equal), then 7 × 7 = 49. Answers: 42 cm², 36 cm, 6 cm, 34 cm, 49 cm².'))

# ---------- 4. explore ----------
c=40; g=''
for i in range(12): g+=f'<rect x="{20+(i%6)*52}" y="{30+(i//6)*52}" width="44" height="44" rx="5" fill="{YEL}" stroke="{NAVY}" stroke-width="3"/>'
g+=f'<g transform="translate(400,10)">'+grid(0,0,10,4,c)+RC(c,c,c,0,0,6,2)+T(3*c+c,c*3+34,'2 by 6',30,TEAL)+'</g>'
tbl=''.join(f'<rect x="{900+i*230}" y="20" width="230" height="56" fill="{SOFT}" stroke="{NAVY}" stroke-width="3"/>'+T(1015+i*230,58,h,28) for i,h in enumerate(['length','breadth','perimeter']))
tbl+=''.join(f'<rect x="{900+i*230}" y="76" width="230" height="56" fill="{WHITE}" stroke="{NAVY}" stroke-width="3"/>' for i in range(3))+''.join(f'<rect x="{900+i*230}" y="132" width="230" height="56" fill="{WHITE}" stroke="{NAVY}" stroke-width="3"/>' for i in range(3))
steps=''.join(f'<li>{E(s)}</li>' for s in ['Take 12 square tiles. Each is 1 cm by 1 cm.','Use all 12 to make a rectangle. Write its length, breadth and perimeter.','Make every different rectangle you can.','Which has the longest perimeter? The shortest? What do you notice?'])
body=h2('Explore: what to do')+card(chip('EXPLORE')+f'<ol style="font-size:36px;font-weight:600;padding-left:52px;display:flex;flex-direction:column;gap:8px">{steps}</ol>')
body+=card(SV(1600,210,g+tbl,'Twelve square tiles, a 2 by 6 rectangle drawn on a grid, and a table for length, breadth and perimeter').replace('style="width:1600px;height:210px;flex:none"','style="width:100%;height:auto"'),extra='padding:20px 32px')
put('p4l7-explore1',sec('p4l7-explore1','8–13 MIN',body,'Minutes 8 to 13. Pairs build rectangles with 12 tiles (online: paper squares on camera, or draw on 1 cm grid paper). Ask them to predict first: "How many rectangles? Will they all have the same perimeter?" Many children think the same tiles must give the same perimeter. Let them find out. Early finishers: try 16 tiles. Which rectangle has the smallest perimeter now? (4 by 4, 16 cm.)'))
body=h2('Explore: talk about it')+numcards([('1.','How many different rectangles did you make with 12 tiles?'),('2.','Which has the longest perimeter? The shortest?'),('3.','All of them have the same area. Why are the perimeters different?')],40)
put('p4l7-explore2',sec('p4l7-explore2','13–18 MIN',body,'Minutes 13 to 18. Gather the rectangles on the board in the order children say them, then ask "Is any missing? Is any the same as another, just turned?" Answers: 1) 3 rectangles: 1 by 12, 2 by 6, 3 by 4 (12 by 1 is the same as 1 by 12 turned). 2) 1 by 12 has 26 cm; 3 by 4 has 14 cm (2 by 6 has 16 cm). 3) The area is the number of tiles, which never changes. The perimeter counts the outside edges: in a long row most tiles show two edges; squashed together, more edges are hidden inside. Close to a square hides the most edges. Do NOT give the rule yet if nobody says it: the teaching part comes back to it.'))

# ---------- 6. teach: missing lengths ----------
c=48; W_,H_=12*c,8*c; ox,oy=2*c,c
base=SV(W_,H_,lfig(c),'An L-shaped figure on a grid: top 5 cm, left 6 cm, bottom 8 cm, right 4 cm, and two step sides marked with question marks')
ov1=SV(W_,H_,LN(ox,oy,c,5,2,8,2,TEAL,10)+LN(ox,oy,c,0,6,8,6,TEAL,6,'14 10')+LN(ox,oy,c,0,0,5,0,TEAL,6,'14 10')+f'<rect x="{ox+5.5*c:.0f}" y="{oy+2*c+8:.0f}" width="{c*2:.0f}" height="48" fill="{SKY}"/>'+T(ox+6.5*c,oy+2*c+46,'3 cm',34,TEAL),'the step across is 3 cm')
ov2=SV(W_,H_,LN(ox,oy,c,5,0,5,2,RED,10)+f'<rect x="{ox+5*c+8:.0f}" y="{oy+0.4*c:.0f}" width="{c*2.2:.0f}" height="48" fill="{CREAM}"/>'+T(ox+5*c+14,oy+1*c+14,'2 cm',34,RED,'start'),'the step down is 2 cm')
body=h2('Find the missing lengths first')+stitle('Every corner is a square corner. Two sides have no label.')
body+=pin(128,300,W_,base)
body+=ostep(128,300,1,'Across: the bottom is 8 cm and the top is 5 cm. So the step across is 8 − 5 = 3 cm.',ov1,W_,H_,dx=620,dy=0,tw=1044)
body+=ostep(128,300,2,'Down: the left is 6 cm and the right is 4 cm. So the step down is 6 − 4 = 2 cm.',ov2,W_,H_,dx=620,dy=170,tw=1044)
body+=soft(748,640,1044,'Opposite sides: the short pieces on one side add up to the long side opposite.')
put('p4l7-teach1',sec('p4l7-teach1','18–20 MIN',body,'Teach. Ask first: "Can we find the area yet?" (No: we do not know every length.) Click 1: run a finger along the bottom (8 cm) and then along the top: 5 cm plus the step across. Think-aloud: "The bottom goes all the way across. The top and the step across together go the same distance. 8 − 5 = 3." Click 2: the same going down: 6 = 4 + the step, so 2 cm. Click 3: the general idea. Check by counting grid squares: 3 and 2.'))

# ---------- 7. worked example: area two ways ----------
c=34; W_,H_=13*c,8*c; ox,oy=2*c,c
def lsmall(c): ox,oy=2*c,c; return grid(0,0,13,8,c)+PL(ox,oy,c,LPTS)+T(ox+2.5*c,oy-9,'5 cm',24)+T(ox-8,oy+3*c+9,'6 cm',24,NAVY,'end')+T(ox+4*c,oy+6*c+28,'8 cm',24)+T(ox+8*c+8,oy+4*c+9,'4 cm',24,NAVY,'start')
b1=SV(W_,H_,lsmall(c),'The L-shape, ready to split'); b2=SV(W_,H_,lsmall(c),'The L-shape, ready to take away')
o1=SV(W_,H_,RC(ox,oy,c,0,0,5,6,YEL,NAVY,4)+RC(ox,oy,c,5,2,3,4,MINT,NAVY,4)+T(ox+2.5*c,oy+3*c+14,'30',44)+T(ox+6.5*c,oy+4*c+14,'12',44),'split into a 5 by 6 rectangle and a 3 by 4 rectangle')
o2=SV(W_,H_,RC(ox,oy,c,5,0,3,2,'#F6D5D5',RED,5,'12 8')+RC(ox,oy,c,0,0,8,6,'none',TEAL,7,'16 10')+T(ox+6.5*c,oy+1*c+12,'6',40,RED)+T(ox+3*c,oy+3.5*c,'48',44,TEAL),'the big 8 by 6 rectangle with the 3 by 2 piece taken away')
body=h2('Worked example: area two ways')+stitle('The same L-shape. The missing sides are 3 cm and 2 cm.')
body+=pin(128,290,W_,b1)+pin(990,290,W_,b2)
body+=pin(128,290,W_,o1,'fade')+pin(128+W_+20,330,330,p('Split it: 5 × 6 = 30 and 3 × 4 = 12. 30 + 12 = 42 cm²',34,700),'fade',WHITE,20,'16px 24px')
body+=pin(990,290,W_,o2,'fade')+pin(990+W_+20,330,290,p('Take away: 8 × 6 = 48. 48 − 6 = 42 cm²',34,700),'fade',WHITE,20,'16px 24px')
body+=answer(128,640,1664,'Both ways give 42 cm². Two ways that agree: a good check!')
body+=pin(128,760,1664,p('Take away is quickest when the missing piece is small. Splitting works for any shape with square corners.',32,600,MUTED),'fade',None)
put('p4l7-we1',sec('p4l7-we1','20–22 MIN',body,'Click 1: colour the two rectangles: "I split the shape with one line. Left part 5 by 6, right part 3 by 4. I need the lengths of EACH part: the right part is 8 − 5 = 3 wide and 4 tall." Click 2: "Or I draw the big rectangle round the whole shape: 8 by 6 = 48. The piece that is missing is 3 by 2 = 6. 48 − 6 = 42." Click 3: both agree. Ask: "Could we split it a different way?" (Yes: across, into 5 by 2 on top and 8 by 4 underneath: 10 + 32 = 42.)'))

# ---------- 8. your turn: area ----------
c=30
X=2*c
fa=SV(11*c,7*c,grid(0,0,11,7,c)+PL(X,c,c,[(0,0),(3,0),(3,2),(7,2),(7,5),(0,5)])+T(X+1.5*c,c-8,'3 cm',26)+T(X+3.5*c,c+5*c+28,'7 cm',26)+T(X-6,c+2.5*c+9,'5 cm',24,NAVY,'end')+T(X+7*c+8,c+3.5*c+9,'3 cm',26,NAVY,'start'),'Figure A: a 7 cm by 5 cm L-shape with a corner piece missing')
fb=SV(9*c,6*c,grid(0,0,9,6,c)+PL(X,c,c,[(0,0),(2,0),(2,2),(4,2),(4,0),(6,0),(6,4),(0,4)])+T(X+3*c,c+4*c+28,'6 cm',26)+T(X-6,c+2*c+9,'4 cm',24,NAVY,'end')+T(X+3*c,c+2*c+28,'2 cm',24,RED)+T(X+4*c+8,c+1*c+9,'2 cm',24,RED,'start'),'Figure B: a 6 cm by 4 cm rectangle with a gap 2 cm wide and 2 cm deep cut into the middle of the top')
body=h2('Your turn: find the area')+stitle('Split it, or take away. Use the other way to check.')
body+=pin(128,290,11*c,fa)+qrow(490,320,890,'A','Find the area of figure A.',36)+answer(1420,320,372,'27 cm²')
body+=pin(128,520,9*c,fb)+qrow(490,540,890,'B','Find the area of figure B.',36)+answer(1420,540,372,'20 cm²')
body+=qrow(128,760,1252,'C','A 10 cm square has a 3 cm square cut from one corner. Area left?',34)+answer(1420,760,372,'91 cm²')
put('p4l7-try1',sec('p4l7-try1','22–23 MIN • OPTIONAL',body,'Whiteboards, then click. A: the missing piece is 4 cm by 2 cm (7 − 3 = 4 across, 5 − 3 = 2 down). Take away: 35 − 8 = 27. Split: 3 × 5 + 4 × 3 = 15 + 12 = 27. B: take away the gap: 24 − 4 = 20. Or split into 3 pieces: 2 × 4 + 2 × 2 + 2 × 4 = 8 + 4 + 8 = 20. C: 100 − 9 = 91. Ask: "Which way was quicker for B?"'))

# ---------- 9. worked example: perimeter, push out ----------
c=48; W_,H_=12*c,8*c; ox,oy=2*c,c
base=SV(W_,H_,lfig(c,False)+T(ox+6.5*c,oy+2*c+46,'3 cm',30,NAVY)+T(ox+5*c+14,oy+1*c+14,'2 cm',30,NAVY,'start'),'The L-shape with all six sides labelled')
ov1=SV(W_,H_,LN(ox,oy,c,5,2,8,2,RED,10)+LN(ox,oy,c,5,0,5,2,RED,10)+LN(ox,oy,c,5,-0.12,8,-0.12,RED,6,'12 9')+LN(ox,oy,c,8.12,0,8.12,2,RED,6,'12 9')
          +f'<path d="M{ox+7.5*c:.0f} {oy+1.8*c:.0f} V{oy+0.35*c:.0f}" stroke="{RED}" stroke-width="5" marker-end="url(#ah)"/><path d="M{ox+5.2*c:.0f} {oy+1.7*c:.0f} H{ox+7.0*c:.0f}" stroke="{RED}" stroke-width="5" marker-end="url(#ah)"/>'
          +f'<defs><marker id="ah" markerWidth="10" markerHeight="10" refX="6" refY="5" orient="auto"><path d="M0 0 L10 5 L0 10 Z" fill="{RED}"/></marker></defs>','the two step sides slide out to the edges')
ov2=SV(W_,H_,RC(ox,oy,c,0,0,8,6,'none',TEAL,8,'18 10'),'the outline is now an 8 by 6 rectangle')
body=h2('Perimeter: push the steps out')+stitle('Going round: 5 + 2 + 3 + 4 + 8 + 6 = 28 cm. Is there a quicker way?')
body+=pin(128,300,W_,base)
body+=ostep(128,300,1,'Slide the 3 cm step up to the top edge. Slide the 2 cm step across to the right edge.',ov1,W_,H_,dx=620,dy=0,tw=1044)
body+=ostep(128,300,2,'Now the outline is an 8 cm by 6 cm rectangle. Nothing was added or lost.',ov2,W_,H_,dx=620,dy=150,tw=1044)
body+=answer(748,610,1044,'8 + 6 + 8 + 6 = 28 cm ✓')
body+=soft(748,730,1044,'Careful: this works when the steps all go one way. A gap in the middle of a side has extra sides you cannot push out.',30)
put('p4l7-we2',sec('p4l7-we2','23–26 MIN',body,'Ask first: "We know all six sides now. How do we find the perimeter?" Add them going round, starting at the top left corner: 5 + 2 + 3 + 4 + 8 + 6 = 28. Then: "Is there a quicker way?" Click 1: slide the step sides with your finger. Think-aloud: "The 3 cm side is level with the top, so if I slide it up it fills the gap in the top edge: 5 + 3 = 8. The 2 cm side slides right to sit on top of the 4 cm side: 2 + 4 = 6." Click 2: the dashed rectangle. Click 3: same answer. Click 4: the warning, which comes back before page 2. Note: the AREA did change (48 versus 42); only the outline length is the same.'))
put('p4l7-try2',try_slide('p4l7-try2','26–27 MIN • OPTIONAL','Your turn: perimeter','Push the steps out. Then check by adding every side.',[('a','A 9 cm by 6 cm rectangle has a 2 cm square cut from one corner. Perimeter?','30 cm'),('b','Figure A from before (7 cm by 5 cm, corner piece missing). Perimeter?','24 cm'),('c','True or false: cutting a corner off a rectangle makes its perimeter smaller.','False')],'Whiteboards, then click. a) 9 + 6 + 9 + 6 = 30: the corner sides push back out. b) 7 + 5 + 7 + 5 = 24; check: 3 + 2 + 4 + 3 + 7 + 5 = 24. c) False: the two sides you lose are replaced by two new sides of the same length, so the perimeter stays the same (but the area gets smaller).',size=34))

# ---------- 11. same area, different perimeters ----------
W4=[220,220,260,280]
body=h2('Same area, different perimeters')+card(p('Find every rectangle with whole-cm sides and an area of 20 cm².',40,700))
body+=trow(128,380,['Length','Breadth','Area','Perimeter'],W4,None,True)
for i,r in enumerate([['1 cm','20 cm','20 cm²','42 cm'],['2 cm','10 cm','20 cm²','24 cm'],['4 cm','5 cm','20 cm²','18 cm']]): body+=trow(128,470+i*90,r,W4,'rise')
body+=pin(1300,380,492,p('List in order: length 1, 2, 3 … 3 does not work (20 ÷ 3 has a remainder). Stop at 5 by 4: it is 4 by 5 again.',32,700),'fade',WHITE,20,'22px 26px')
body+=soft(128,770,1664,'Long and thin: the biggest perimeter. Closest to a square: the smallest perimeter.')
put('p4l7-we3',sec('p4l7-we3','27–29 MIN',body,'Make a list in order (the factor pairs from Lesson 1). Click to add each row while children say the breadth: "1 times what is 20?" Then the note: why 3 is missing and why we stop. Then the pattern. Think-aloud: "Every rectangle has the same 20 squares inside, but the long thin one has 42 cm of edge and the squashed-up one only 18." Ask: "Could a rectangle with area 20 cm² have a perimeter of 30 cm?" (No: with whole-cm sides only 42, 24 and 18 are possible.)'))

# ---------- 12. key ----------
body=h2('Key idea: split, take away, push out')+card(p('Area: split into rectangles, or take the missing piece away from a big rectangle. Perimeter: push the steps out to make a rectangle.',42,700))+card(p('The same area can have different perimeters. Close to a square gives the smallest perimeter.',38,600,MUTED))
put('p4l7-key',sec('p4l7-key','29–30 MIN',body,'Say the key ideas together. Common mistakes to watch for during the worksheet: (1) Adding only the labelled sides of an L-shape, or giving a missing side the wrong length instead of using the opposite sides. (2) Thinking the same area means the same perimeter, or that cutting a corner off makes the perimeter smaller. (3) Finding the area of a border as 2 × (length + breadth) and forgetting the 4 corner squares.'))
put('p4l7-break',break_slide('p4l7-break','30–34 MIN','Body shapes! "Long and thin": stretch your arms out wide. "Square": hug yourself tight. Which shape has the shorter way round?','Four minutes. Call out "long and thin", "square", "long and thin" faster and faster. Then: "Everyone stand up tall and stretch: is your area or your perimeter changing?" (Neither is a real rectangle, it is just for fun.)'))

# ---------- worksheet page 1 ----------
put('p4l7-ws1',ws_preview('p4l7-ws1','34–50 MIN','Worksheet page 1: with your partner',[('Q1','The L-shape. Missing lengths first, then the area two ways, then the perimeter.'),('Q2','Every rectangle with area 24 cm². List in order, starting with a length of 1 cm.'),('Q3','Six tiles. Find the smallest and the largest perimeter.')],'Stuck? Build it with tiles, or draw it on 1 cm grid paper.','Minutes 34 to 50. Walk around. Ask "How do you know?" before giving any help. Q3 is the most open: give pairs 6 tiles. Ask: "Which tiles hide the most edges?" and "Can you find a shape with an even bigger perimeter?" Every shape without a 2 by 2 block has 14 cm.'))
put('p4l7-ws1ans',checks('p4l7-ws1ans','50–53 MIN','Page 1: check together',[('Q1','a) 5 cm across, 3 cm down   b) 28 + 20 = 48 cm²  and  63 − 15 = 48 cm²   c) 32 cm'),('Q2','1 by 24: 50 cm,  2 by 12: 28,  3 by 8: 22,  4 by 6: 20.   a) Largest 1 by 24, smallest 4 by 6'),('Q3','a) 6 cm²   b) Smallest 10 cm: only the 2 by 3 rectangle.  Largest 14 cm, e.g. a row of 6.')],
 'Click after a pair explains. Q1b: split into 4 by 7 and 5 by 4, or 9 by 7 take away 5 by 3. Q1c: push out: 9 + 7 + 9 + 7 = 32. Q2: the rectangle closest to a square has the smallest perimeter. (The 36 cm² question, 6 by 6 with perimeter 24 cm, is in the question bank.) Q3: each pair of tiles that share a side hides 2 cm of edge. 6 tiles have 24 cm of edge; a row hides 5 × 2 = 10, leaving 14; the 2 by 3 hides 7 × 2 = 14, leaving 10.',gapy=170))

# ---------- teach before page 2: staircase ----------
c=50; W_,H_=11*c,7*c; ox,oy=2*c,c
SP=[(0,0),(2,0),(2,1),(5,1),(5,3),(8,3),(8,5),(0,5)]
base=SV(W_,H_,grid(0,0,11,7,c)+PL(ox,oy,c,SP)+T(ox+4*c,oy+5*c+42,'8 cm')+T(ox-12,oy+2.5*c+12,'5 cm',34,NAVY,'end'),'A staircase figure 8 cm along the bottom and 5 cm up the left side')
acr=[(0,2),(2,5),(5,8)]; dwn=[(2,0,1),(5,1,3),(8,3,5)]
ov1=SV(W_,H_,''.join(LN(ox,oy,c,a,b0,b,b0,RED,10) for (a,b),b0 in zip([(0,2),(2,5),(5,8)],[0,1,3])),'the three across sides: together they are as long as the bottom')
ov2=SV(W_,H_,''.join(LN(ox,oy,c,x,a,x,b,TEAL,10) for x,a,b in dwn),'the three down sides: together they are as tall as the left side')
ov3=SV(W_,H_,RC(ox,oy,c,0,0,8,5,'none',TEAL,7,'16 10'),'the staircase pushed out to an 8 by 5 rectangle')
body=h2('Staircases: push every step out')+stitle('Only two lengths are given. Can we still find the perimeter?')
body+=pin(128,300,W_,base)
body+=ostep(128,300,1,'The across sides (red) push up to the top. Together they are as long as the bottom: 8 cm.',ov1,W_,H_,dx=590,dy=0,tw=1074)
body+=ostep(128,300,2,'The down sides (green) push across to the right. Together they are as tall as the left: 5 cm.',ov2,W_,H_,dx=590,dy=150,tw=1074)
body+=ostep(128,300,3,'So the perimeter is the same as an 8 cm by 5 cm rectangle: 8 + 5 + 8 + 5 = 26 cm.',ov3,W_,H_,dx=590,dy=300,tw=1074)
put('p4l7-teachstair',sec('p4l7-teachstair','53–54 MIN',body,'Teach before worksheet page 2 (Q4 is a staircase with different numbers). Ask first: "Can we find the perimeter when the steps have no labels?" Click 1: trace the three red sides and push them up with your finger: "however long each step is, together they reach all the way across, 8 cm." Click 2: the same for the green sides: "together they go all the way down, 5 cm." Click 3: the rectangle. Then check by counting the grid: 2 + 1 + 3 + 2 + 3 + 2 + 8 + 5 = 26. Remind them of the warning from before: a gap in the middle of a side adds extra.'))

# ---------- teach before page 2: cut and rearrange ----------
c=56
before=SV(9*c,4*c,grid(0,0,9,4,c)+RC(2*c,c,c,0,0,6,2)+LN(2*c,c,c,3,-0.3,3,2.3,RED,6,'12 9')+T(2*c+3*c,c+2*c+42,'6 cm',32)+T(2*c-10,c+1*c+12,'2 cm',32,NAVY,'end'),'A 6 cm by 2 cm rectangle with a cut line down the middle')
after=SV(6*c,6*c,grid(0,0,6,6,c)+RC(c,c,c,0,0,3,2,SKY)+RC(c,c,c,0,2,3,2,YEL)+T(c+1.5*c,c+4*c+42,'3 cm',32)+T(c+3*c+10,c+2*c+12,'4 cm',32,NAVY,'start'),'The two halves stacked to make a 3 cm by 4 cm rectangle')
body=h2('Cut it and move it: what changes?')+stitle('Cut a 6 cm by 2 cm rectangle in half. Stack the halves.')
body+=pin(128,300,9*c,before)+pin(128,560,700,p('Area 12 cm².  Perimeter 16 cm.',34,700),'fade',WHITE,20,'14px 24px')
body+=pin(1000,250,6*c,after,'fade')+pin(1000+6*c+30,330,440,p('Area: still 12 cm². Nothing was added or lost.',34,700),'fade',WHITE,20,'16px 24px')
body+=pin(1000+6*c+30,520,440,p('Perimeter: 3 + 4 + 3 + 4 = 14 cm. It changed!',34,700),'fade',WHITE,20,'16px 24px')
body+=answer(128,780,1664,'Cutting and moving keeps the area the same. The perimeter can change.')
put('p4l7-teachcut',sec('p4l7-teachcut','54–56 MIN',body,'Teach before worksheet page 2 (Q5 cuts a different rectangle). Use a real paper strip and scissors. Click 1: area and perimeter of the strip (6 × 2 = 12; 6 + 2 + 6 + 2 = 16). Click 2: cut and stack. Click 3: the area. Click 4: the perimeter. Click 5: the big idea. Ask: "Why did the perimeter go DOWN?" (The two halves now share a long side inside, so 3 cm of edge on each piece is hidden. The new shape is closer to a square.)'))

# ---------- teach before page 2: border ----------
c=50; W_,H_=12*c,9*c
fr=grid(0,0,12,9,c)+RC(c,c,c,0,0,9,7,'#BFE3B4')+RC(c,c,c,1,1,7,5,'#7CC08A')+T(c+4.5*c,c+3.5*c+12,'garden',36)+T(c+4.5*c,c+1*c+40,'7 m',30)+T(c+1*c+14,c+3.5*c+48,'5 m',30,NAVY,'start')+T(c+9*c+10,c+0.5*c+10,'1 m',30,TEAL,'start')
base=SV(W_,H_,fr,'A 7 m by 5 m garden with a path 1 m wide all round it')
ov=SV(W_,H_,''.join(RC(c,c,c,a,b,1,1,YEL,RED,5) for a,b in [(0,0),(8,0),(0,6),(8,6)]),'the four corner squares of the path')
body=h2('Borders: big rectangle take away the inside')
body+=pin(128,240,W_,base)
body+=ostep(128,240,1,'Whole thing: add 1 m on EACH side. 7 + 2 = 9 m long, 5 + 2 = 7 m wide.',dx=630,dy=0,tw=1034)
body+=ostep(128,240,2,'Path = whole take away garden: 9 × 7 − 7 × 5 = 63 − 35 = 28 m².',dx=630,dy=0,tw=1034).replace('top:240px','top:390px')
body+=ostep(128,240,3,'Check: four strips 7 + 7 + 5 + 5 = 24, plus the 4 corner squares: 24 + 4 = 28 m² ✓',ov,W_,H_,dx=630,dy=300,tw=1034)
put('p4l7-teachframe',sec('p4l7-teachframe','56–57 MIN',body,'Teach before worksheet page 2 (Q6 is a photo frame with different numbers). Click 1: "The path is on BOTH ends, so the length grows by 1 + 1." Many children add only 1. Click 2: big take away small. Click 3: the check, with the corner squares lit up: "If I only count the four strips beside the garden, I miss the corners."'))
put('p4l7-try3',try_slide('p4l7-try3','57–58 MIN • OPTIONAL','Your turn: page 2 warm-up','Push out, cut and move, or take away.',[('a','A staircase is 9 cm wide and 6 cm high. Perimeter?','30 cm'),('b','A 10 cm by 2 cm strip is cut in half and stacked: 5 cm by 4 cm. Perimeter now?','18 cm'),('c','A 4 cm by 3 cm card has a border 1 cm wide all round. Area of the border?','18 cm²')],'Whiteboards, then click. a) 9 + 6 + 9 + 6 = 30. b) 5 + 4 + 5 + 4 = 18 (it was 24; the area stays 20 cm²). c) The whole thing is 6 cm by 5 cm = 30; take away 12: 18 cm².',size=34))

put('p4l7-ws2',ws_preview('p4l7-ws2','58–76 MIN','Worksheet page 2: on your own',[('Q4','The staircase. Push the steps out, then check by counting.'),('Q5','Cut and rearrange. Draw the square, then compare area and perimeter.'),('Q6','The photo frame. Big rectangle take away the photo.')],'Finished early? Stretch and Challenge come next.','Children work alone. Note who needs a short catch-up next lesson, especially children who still think cutting a corner off makes the perimeter smaller.'))
put('p4l7-ws2ans',checks('p4l7-ws2ans','76–80 MIN','Page 2: check together',[('Q4','a) 11 + 6 + 11 + 6 = 34 cm   b) 6 + 14 + 22 = 42 cm²'),('Q5','A 4 by 4 square.  Area 16 and 16 cm².  Perimeter 20 and 16 cm.  c) No: only the area stayed the same.'),('Q6','a) 10 cm by 8 cm   b) 80 − 48 = 32 cm²   c) the 4 corner squares (28 + 4 = 32)')],
 'Click after a child explains. Q4a: the across sides add up to the bottom (11 cm) and the down sides add up to the left (6 cm). Counting: 3 + 2 + 4 + 2 + 4 + 2 + 11 + 6 = 34. Q5: stack the two 4 by 2 halves. Q6c: Mei counted only the strips beside the photo.',gapy=170))

# ---------- stretch / challenge ----------
st=[('1.','A path 2 m wide goes all round a lawn 10 m by 6 m. Find the area of the path.'),('2.','Ali joins 8 square tiles (1 cm by 1 cm) edge to edge. What is the smallest perimeter? The largest?'),('3.','A rectangle has whole-cm sides, an area of 40 cm² and a perimeter of 26 cm. Find its length and breadth.')]
put('p4l7-stretch',sec('p4l7-stretch','Early finishers / take-home',h2('Stretch')+numcards(st),'Answers: 1) 80 m²: the whole thing is 14 m by 10 m = 140 m², take away the lawn 60 m² (watch for 12 m by 8 m: the path is on both sides). 2) Smallest 12 cm (a 2 by 4 rectangle, or a 3 by 3 square with one corner missing); largest 18 cm (any shape without a 2 by 2 block, such as a row of 8). 3) 8 cm by 5 cm: list the pairs for 40 (1 by 40, 2 by 20, 4 by 10, 5 by 8); only 5 by 8 has perimeter 26.'))
ch=[('1.','A garden is 10 m long and 8 m wide. Two paths 1 m wide cross it: one along its length and one across its width. What area of the garden is NOT path?'),('2.','A rectangle 9 cm long and 4 cm wide is cut into 2 pieces. The pieces fit together exactly to make a square. How long is a side of the square? Did the perimeter go up or down?')]
put('p4l7-challenge',sec('p4l7-challenge','Any time • take-home',h2('Challenge')+numcards(ch,36),'Pairs try first, then use the "see it" slide if stuck, then the walk-through. These are Think Harder Q6 and Q7. Answers: 1) 63 m² (slide the paths to the edges: the grass is 9 m by 7 m). 2) 6 cm (the area is 36 cm² and 6 × 6 = 36); the perimeter went down from 26 cm to 24 cm.'))
c=40
X=2*c
gq=grid(0,0,14,10,c)+RC(X,c,c,0,0,10,8,'#7CC08A')+RC(X,c,c,0,4,10,1,'#E8D9B5',NAVY,3)+RC(X,c,c,5,0,1,8,'#E8D9B5',NAVY,3)+T(X+5*c,c+8*c+34,'10 m',30)+T(X-8,c+2*c+10,'8 m',30,NAVY,'end')+T(X+7.5*c,c+4.5*c+11,'path 1 m',26)
g2=grid(0,0,18,10,c)+RC(X,c,c,0,0,9,4)+f'<path d="M{X+3*c} {c} V{c+2*c} H{X+6*c} V{c+4*c}" stroke="{RED}" stroke-width="6" stroke-dasharray="12 8" fill="none"/>'+T(X+4.5*c,c+4*c+36,'9 cm',30)+T(X-8,c+2*c+10,'4 cm',30,NAVY,'end')
g2+=RC(X,c,c,9.6,2.6,6,6,'none',TEAL,5,'14 10')+T(X+12.6*c,c+5.6*c+12,'square: ? cm',30,TEAL)
body=h2('Challenge: see it',60)+'<div style="display:flex;gap:32px;align-items:flex-start">'
body+=card(f'<p style="font-size:30px;font-weight:700;color:{TEAL}">Q1: Two paths cross the garden</p>'+SV(14*c,10*c,gq,'A 10 m by 8 m garden with a path 1 m wide along its length and another across its width').replace(f'style="width:{14*c}px;height:{10*c}px;flex:none"','style="width:100%;height:auto;display:block"'),extra='flex:1;min-width:0;padding:20px 24px')
body+=card(f'<p style="font-size:30px;font-weight:700;color:{TEAL}">Q2: Two pieces make a square</p>'+SV(18*c,10*c,g2,'A 9 cm by 4 cm rectangle with a staircase cut line, and a dashed square of unknown side').replace(f'style="width:{18*c}px;height:{10*c}px;flex:none"','style="width:100%;height:auto;display:block"'),extra='flex:1;min-width:0;padding:20px 24px')+'</div>'
put('p4l7-chdiag',sec('p4l7-chdiag','Early finishers / take-home',body,'Show after pairs have tried the Challenge, or if they are stuck. The pictures show the problem, not the answer. Ask: Q1 "Would the grass area change if the paths were moved?" Q2 "What stays the same when we cut and move pieces? So what is the area of the square?" Answers are in the Challenge slide notes.'))
body=h2('Challenge: walk-through')+pin(128,250,800,p('Q1: slide the paths to the edges',38,800,TEAL))
for i,t in enumerate(['Moving the paths does not change the grass.','Grass: 10 − 1 = 9 m by 8 − 1 = 7 m','9 × 7 = 63 m²','Check: 80 − 10 − 8 + 1 = 63 ✓ (the crossing was counted twice)']): body+=pin(128,330+i*120,800,p(t,32),'rise',WHITE)
body+=pin(992,250,800,p('Q2: the area stays the same',38,800,TEAL))
for i,t in enumerate(['Rectangle: 9 × 4 = 36 cm²','The square also has 36 cm². 6 × 6 = 36, so a side is 6 cm.','Perimeter: 9 + 4 + 9 + 4 = 26 cm, then 6 × 4 = 24 cm','It went DOWN by 2 cm: a square is the most squashed-up shape.']): body+=pin(992,330+i*120,800,p(t,32),'rise',WHITE)
put('p4l7-chwalk',sec('p4l7-chwalk','Early finishers / take-home',body,'Use after pairs have tried. Q1: sliding pieces without overlapping keeps the area, the same idea as Q5. The check needs care: 10 + 8 = 18 counts the 1 m square where the paths cross twice. Q2: if anyone wants to see the cut, it is a staircase: from the top at 3 cm, down 2 cm, across 3 cm, down to the bottom. Slide the right piece 3 cm left and 2 cm up and it makes the 6 cm square. Draw it on 1 cm grid paper to check.'))

# ---------- talk / exit ----------
body=h2('Talk time')+card(chip('TALK TIME',YEL,NAVY)+p('Ben says: "A bigger area always means a bigger perimeter." Do you agree? Use rectangles to test it.',42,600))+card(p('Sentence starters:',34,400,MUTED)+p('“I noticed that …”   “I tested it by …”   “I know because …”',38,600))
put('p4l7-talk',sec('p4l7-talk','80–85 MIN',body,'Minutes 80 to 85. Pairs talk for 2 minutes, then share. Answer: Ben is wrong. A 1 cm by 12 cm rectangle has area 12 cm² and perimeter 26 cm; a 4 cm by 4 cm square has a bigger area (16 cm²) but a smaller perimeter (16 cm). One counter-example is enough to show a rule is not always true. Second question if time: "When we cut a shape and move the pieces, which stays the same?" (The area, because nothing is added or lost; the perimeter can change.) Praise the reasons, not only the answers.'))
c=46
X=2*c
ex=SV(10*c,7*c,grid(0,0,10,7,c)+PL(X,c,c,[(0,0),(5,0),(5,2),(7,2),(7,5),(0,5)])+T(X+3.5*c,c+5*c+40,'7 cm',30)+T(X-10,c+2.5*c+10,'5 cm',30,NAVY,'end')+T(X+6*c,c+2*c+36,'2 cm',28,RED)+T(X+5*c+10,c+1*c+10,'2 cm',28,RED,'start'),'A 7 cm by 5 cm rectangle with a 2 cm square cut from one corner')
body=h2('Exit ticket')+card(chip('EXIT TICKET')+f'<div style="display:flex;gap:40px;align-items:center">{ex}'+p('A 7 cm by 5 cm rectangle has a 2 cm by 2 cm square cut from one corner. Find the area and the perimeter of the shape left.',42,600)+'</div>')+card(p('Write your answer on a slip of paper. Show it to your tutor. Then collect your stamp in your inquiry journal.',34,400))
put('p4l7-exit',sec('p4l7-exit','85–88 MIN',body,'Minutes 85 to 88. Answer: area 35 − 4 = 31 cm²; perimeter 24 cm, the same as the 7 by 5 rectangle (push the corner back out). Children who write 20 cm for the perimeter forgot the two new sides; children who write 31 cm mixed up area and perimeter. Extension: Ravi has 24 m of fencing for a rectangular pen with whole-metre sides. One side is a wall and needs no fence. What is the largest area? (72 m²: 6 m, 12 m, 6 m.)'))

# ---------- write ----------
# ---------- fix pass (rebuild/p4_fix.py): sneak-peek puzzles, looking back, neutral names, go further, minute labels ----------
import subprocess as _sp, p4_fix
_G=json.loads(_sp.check_output(['node','-e',"process.stdout.write(JSON.stringify(require('"+os.path.join(H,'..','p4','content','l7.js')+"').gaps))"]))
_ID='p4l7'
_PIC={0:'''<svg viewBox="0 0 220 136" width="220" height="136" xmlns="http://www.w3.org/2000/svg" aria-label="A rectangle 5 squares long and 3 squares high with the top right square removed"><rect x="10" y="8" width="40" height="40" fill="#DDEBF7" stroke="#1B2A49" stroke-width="2.5"/><rect x="50" y="8" width="40" height="40" fill="#DDEBF7" stroke="#1B2A49" stroke-width="2.5"/><rect x="90" y="8" width="40" height="40" fill="#DDEBF7" stroke="#1B2A49" stroke-width="2.5"/><rect x="130" y="8" width="40" height="40" fill="#DDEBF7" stroke="#1B2A49" stroke-width="2.5"/><rect x="10" y="48" width="40" height="40" fill="#DDEBF7" stroke="#1B2A49" stroke-width="2.5"/><rect x="50" y="48" width="40" height="40" fill="#DDEBF7" stroke="#1B2A49" stroke-width="2.5"/><rect x="90" y="48" width="40" height="40" fill="#DDEBF7" stroke="#1B2A49" stroke-width="2.5"/><rect x="130" y="48" width="40" height="40" fill="#DDEBF7" stroke="#1B2A49" stroke-width="2.5"/><rect x="170" y="48" width="40" height="40" fill="#DDEBF7" stroke="#1B2A49" stroke-width="2.5"/><rect x="10" y="88" width="40" height="40" fill="#DDEBF7" stroke="#1B2A49" stroke-width="2.5"/><rect x="50" y="88" width="40" height="40" fill="#DDEBF7" stroke="#1B2A49" stroke-width="2.5"/><rect x="90" y="88" width="40" height="40" fill="#DDEBF7" stroke="#1B2A49" stroke-width="2.5"/><rect x="130" y="88" width="40" height="40" fill="#DDEBF7" stroke="#1B2A49" stroke-width="2.5"/><rect x="170" y="88" width="40" height="40" fill="#DDEBF7" stroke="#1B2A49" stroke-width="2.5"/></svg>'''}

order=['p4l7-title','p4l7-warm1','p4l7-warm2','p4l7-explore1','p4l7-explore2','p4l7-teach1','p4l7-we1','p4l7-try1','p4l7-we2','p4l7-try2','p4l7-we3','p4l7-key','p4l7-break','p4l7-ws1','p4l7-ws1ans','p4l7-teachstair','p4l7-teachcut','p4l7-teachframe','p4l7-try3','p4l7-ws2','p4l7-ws2ans','p4l7-stretch','p4l7-challenge','p4l7-chdiag','p4l7-chwalk','p4l7-talk','p4l7-exit']
p4_fix.finish(S,7,_G,pic=_PIC)
order=p4_fix.order(order,7)
assert set(order)==set(S), set(order)^set(S)
sd=os.path.join(D,'slides')
for f in os.listdir(sd):
    if f.endswith('.html') and f[:-5] not in S: os.remove(os.path.join(sd,f))
for i,h in S.items(): open(os.path.join(sd,i+'.html'),'w').write(h)
deck={'v':4,'createdOnFiles':{'v':1,'at':datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')},'lists':'css',
 'title':'Math Inquirers P4: Lesson 7 – Area Architects II','order':order,'cover':'p4l7-title',
 'sections':{'s1':{'description':'Warm-up and explore','start':'p4l7-title'},'s2':{'description':'Teach: split, take away, push out, same area','start':'p4l7-teach1'},'s3':{'description':'Worksheet with teaching before each page','start':'p4l7-break'},'s4':{'description':'Stretch, challenge, talk and exit','start':'p4l7-stretch'}},
 'faces':{'fredoka':{'family':'Fredoka','href':'https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&display=swap'},'nunito-sans':{'family':'Nunito Sans','href':'https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@400;600;700&display=swap'}},
 'designSystems':[]}
json.dump(deck,open(os.path.join(D,'deck.json'),'w'),indent=1,ensure_ascii=False)
print(len(order),'slides')
