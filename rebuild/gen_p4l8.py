"""Math Inquirers P4, Lesson 8: Symmetry and Nets. Writes split/p4l8/project (deck.json + slides/*.html)."""
import json,os,sys,datetime
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,H)
import slidekit
from slidekit import *
slidekit.FOOT='Math Inquirers P4 Holiday Program  •  Notice it. Test it. Explain why.'
D=os.path.join(H,'..','split','p4l8','project'); os.makedirs(os.path.join(D,'slides'),exist_ok=True)
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


MINTC='#D3F1E4'; PINK='#F6D5D5'
# ---------- square-net helpers ----------
def cellsq(cells,c,ox=0,oy=0,fill=SKY,labels=None,size=30,stroke=NAVY,sw=4,lcol=NAVY):
    g=''
    for (x,y) in cells:
        g+=f'<rect x="{ox+x*c}" y="{oy+y*c}" width="{c}" height="{c}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'
        if labels and (x,y) in labels: g+=T(ox+x*c+c/2,oy+y*c+c/2+size*0.36,labels[(x,y)],size,lcol)
    return g
def row4(y): return [(0,y),(1,y),(2,y),(3,y)]
TEE=row4(1)+[(1,0),(2,2)]            # valid net (teaching)
UBAD=row4(1)+[(0,0),(3,0)]           # not a net (teaching)
ENDC=row4(1)+[(0,0),(0,2)]           # valid net, opposite faces (teaching)
CROSSN=row4(1)+[(1,0),(1,2)]         # dice net (your turn)

# ---------- 1. title ----------
put('p4l8-title',title_slide('p4l8-title','LESSON 8  •  WEEK 4','Symmetry and Nets','Symmetry, nets of a cube',
 'Find out which shapes fold into a cube, find opposite faces on a dice net, and complete symmetric figures.',
 'Objective: Decide whether a shape made of 6 squares folds into a cube by folding it in your head, find which faces of a net are opposite (and use it for dice), complete a figure so that a given line is a line of symmetry, find all the lines of symmetry of a shape, and shade squares to make a pattern symmetric. '
 'Thinking strategies taught today: FOLD IT IN YOUR HEAD (base, walls, lid), TEST EVERY CASE, and COUNT THE SQUARES FROM THE LINE. '
 'Materials: squared paper (2 cm squares), scissors, sticky tape, 6 paper squares per child, a dice, a small mirror (optional), mini whiteboards, coloured pencils. '
 'Online: children cut out 6 paper squares before the lesson and fold on camera; the tutor clicks to reveal each fold on the slides and shades the grids. '
 'Time plan: Warm-up check 1 to 4 (two questions on the key idea; children who get both right and can say why start on the Think Harder pages at minute 34), warm-up game 4 to 6 (one short round), quick questions 6 to 8, explore 8 to 18, teaching 18 to 30 (click to reveal each step and answer; the "your turn" slides are optional, skip them if short of time), brain break 30 to 34, worksheet page 1 from 34 to 50 and check together 50 to 53, short teaching before page 2 from 53 to 58, worksheet page 2 from 58 to 76 and check together 76 to 80, talk time 80 to 85, exit ticket 85 to 88, What was hard? reflection 88 to 90. The Challenge slides and the Think Harder pages are for early finishers and for take-home: they have no fixed time slot. Online: page 1 is pair work, so allow about 2 minutes to move into and out of breakout rooms (or run page 1 as a whole-group screen-share if there are only 8 children).'))

# ---------- 2. warm-up ----------
LET={'H':['#.#','#.#','###','#.#','#.#'],'T':['###','.#.','.#.','.#.','.#.'],'E':['###','#..','###','#..','###'],
     'L':['#..','#..','#..','#..','###'],'U':['#.#','#.#','#.#','#.#','###'],'Z':['###','..#','.#.','#..','###']}
LANS={'H':'2 lines','T':'1 line','E':'1 line','L':'0 lines','U':'1 line','Z':'0 lines'}
LWHY={'H':'up-down and across','T':'up-down','E':'across','L':'none fit','U':'up-down','Z':'none fit'}
def letter(k,c=30):
    cells=[(x,y) for y,r in enumerate(LET[k]) for x,ch in enumerate(r) if ch=='#']
    return SV(3*c+8,5*c+8,cellsq(cells,c,4,4,YEL,None,20,NAVY,2),f'The letter {k} made of squares')
body=h2('Warm-up: Fold It in Your Head')+p('How many lines of symmetry? Show with your fingers.',36,600,MUTED)
CW=533; cards=''; ans=''
for i,k in enumerate('HTELUZ'):
    L=128+(i%3)*(CW+32); Tp=320+(i//3)*300
    cards+=pin(L,Tp,CW,f'<div style="display:flex;align-items:center;gap:24px">{letter(k)}<p style="font-family:{HF};font-size:80px;font-weight:700">{k}</p></div>',None,WHITE,24,'14px 28px',f'box-sizing:border-box;height:280px;border:4px solid {NAVY};box-shadow:8px 8px 0 {NAVY}')
    ans+=pin(L+250,Tp+60,CW-280,f'<p style="font-size:34px;font-weight:800;line-height:1.2">{LANS[k]}</p><p style="font-size:26px;font-weight:600;color:{MUTED}">{LWHY[k]}</p>','pop',SOFT,16,'10px 16px',f'box-sizing:border-box;border:3px solid {NAVY}')
put('p4l8-warm1',sec('p4l8-warm1','4–6 MIN',body+cards+ans,
 'Minutes 4 to 6 (one short round, about 2 minutes: the Warm-up check came first). Fold It in Your Head. Show one letter at a time (the clicks reveal H, T, E, L, U, Z in order). Count 3, 2, 1: fingers up for the number of lines of symmetry. Then a child shows with a finger where the fold line goes. '
 'Answers: H 2 (up-down and across), T 1 (up-down), E 1 (across), L 0, U 1 (up-down), Z 0. A line of symmetry is a fold line where the two halves match exactly. '
 'Z is the surprise: it looks balanced, but folding it never makes the halves match (it turns upside down onto itself, which is a different idea). Hold up a small mirror along a line if you have one: if the picture in the mirror looks like the whole letter, it is a line of symmetry.'))
qs=[('1.','How many faces does a cube have?','6'),('2.','How many edges does a cube have?','12'),('3.','How many corners does a cube have?','8'),('4.','On a dice 1 is opposite 6 and 2 is opposite 5. What is opposite 3?','4'),('5.','A rectangle (not a square) is folded so the halves match. How many different folds?','2')]
body=h2('Quick questions')+''.join(qrow(128,250+i*125,1250,a,b,34) for i,(a,b,c) in enumerate(qs))+''.join(answer(1420,250+i*125,372,c) for i,(a,b,c) in enumerate(qs))
put('p4l8-warm2',sec('p4l8-warm2','6–8 MIN',body,'Minutes 6 to 8. Hold up a real cube or dice if you can. Whiteboards up together, then click. After 3 ask: "Where do the corners meet? How many faces meet at one corner?" (3.) After 4: "Why must opposite faces add up to 7 on a dice?" (It is how dice are made: 1 and 6, 2 and 5, 3 and 4.) After 5: "Show me the two folds." Answers: 6, 12, 8, 4, 2.'))

# ---------- 4. explore ----------
g=''.join(f'<rect x="{20+i*60}" y="50" width="48" height="48" rx="4" fill="{YEL}" stroke="{NAVY}" stroke-width="3"/>' for i in range(6))
g+=f'<g transform="translate(470,10)">'+cellsq(CROSSN,38,0,0,SKY,None,20,NAVY,3)+'</g>'
g+=f'<g transform="translate(900,20)"><polygon points="20,50 100,50 100,130 20,130" fill="{SKY}" stroke="{NAVY}" stroke-width="4"/><polygon points="20,50 60,20 140,20 100,50" fill="{WHITE}" stroke="{NAVY}" stroke-width="4"/><polygon points="100,50 140,20 140,100 100,130" fill="{MINTC}" stroke="{NAVY}" stroke-width="4"/></g>'
g+=T(1280,90,'No gaps.',34,TEAL)+T(1280,140,'No overlaps.',34,TEAL)
steps=''.join(f'<li>{E(s)}</li>' for s in ['Take 6 paper squares.','Join them edge to edge (whole sides touching). Tape them.','Try to fold your shape into a cube: no gaps, no overlaps.','Draw every shape that works. Did any fail? Why?'])
body=h2('Explore: what to do')+card(chip('EXPLORE')+f'<ol style="font-size:36px;font-weight:600;padding-left:52px;display:flex;flex-direction:column;gap:8px">{steps}</ol>')
body+=card(SV(1600,170,g,'Six loose squares, a cross-shaped net of six squares and a folded cube').replace('style="width:1600px;height:170px;flex:none"','style="width:100%;height:auto"'),extra='padding:20px 32px')
put('p4l8-explore1',sec('p4l8-explore1','8–13 MIN',body,'Minutes 8 to 13. Pairs join 6 paper squares and try to fold them into a cube (online: fold on camera, or draw the shape on squared paper and fold in their heads). Ask them to predict first: "Will every shape work?" Let them find out. Early finishers: find a shape that does NOT fold into a cube, and say why it fails.'))
body=h2('Explore: talk about it')+numcards([('1.','How many different shapes that fold into a cube did your group find?'),('2.','What made a shape fail?'),('3.','Do all the shapes that work have 4 squares in a row?')],40)
put('p4l8-explore2',sec('p4l8-explore2','13–18 MIN',body,'Minutes 13 to 18. Gather the shapes on the board; ask "Is this one the same as that one, just turned or flipped?" Answers: 1) There are 11 different nets of a cube altogether (turned or flipped copies count as the same); most groups find 4 to 7. 2) Two squares landed on the same face: for example a 2 by 2 block (4 squares meeting at a corner, but only 3 faces meet at a cube corner), 5 squares in a row, or two squares closing the same end. 3) No: some nets have a row of 3 and no row of 4 (the staircase and the 3-3 net). Do NOT give the method yet if nobody finds it; the teaching part comes next.'))

# ---------- 6. teach: fold in your head ----------
c=100; W_,H_=4*c+20,3*c+20
base=SV(W_,H_,cellsq(TEE,c,10,10,WHITE,None,30),'A net of 6 squares: a row of 4 with one square above the second and one below the third')
def ov(cells,fill,lab):
    return SV(W_,H_,cellsq(cells,c,10,10,fill,{k:lab for k in cells},26),'coloured squares')
o1=ov([(1,1)],YEL,'base')
o2=SV(W_,H_,cellsq([(0,1),(2,1),(1,0)],c,10,10,MINTC,{(0,1):'left',(2,1):'right',(1,0):'back'},24),'the three walls')
o3=SV(W_,H_,cellsq([(2,2)],c,10,10,PINK,{(2,2):'front'},24),'the front wall')
o4=SV(W_,H_,cellsq([(3,1)],c,10,10,SKY,{(3,1):'lid'},28),'the lid')
body=h2('Fold it in your head: base, walls, lid')+stitle('Is this a net of a cube? Pick a base, then fold the other squares round it.')
body+=pin(128,300,W_,base)+pin(128,300,W_,o1,'fade')+pin(128,300,W_,o2,'fade')+pin(128,300,W_,o3,'fade')+pin(128,300,W_,o4,'fade')
for k,t in enumerate(['Choose a base: a square with lots of neighbours. Colour it.','The squares touching it fold UP to be walls: left, right and back.','This square hangs from the right wall. When the wall stands up, it swings round to the FRONT.','The last square is joined to the right wall too: it folds over the top. It is the lid.']):
    body+=ostep(128,300,k+1,t,None,0,0,dx=480+20,dy=0,tw=1164,size=32).replace('top:300px',f'top:{300+k*125}px')
body+=answer(628,830,1164,'1 base + 4 walls + 1 lid, no overlaps: it IS a net.')
put('p4l8-teach1',sec('p4l8-teach1','18–21 MIN',body,'Use 6 paper squares, tape and a real cube if possible. Ask first: "Do you think this folds into a cube?" Take guesses. Click 1: the base (yellow). Click 2: fold the left, right and back squares up with your finger: they stand like walls. Click 3: "This square hangs from the RIGHT wall, so when the wall stands up it swings round to the front." Click 4: the lid. Think-aloud: "A cube has 6 faces: one base, one lid and four walls. I check I have all four walls: left, right, back, front, and nothing is in the same place twice." Then fold the paper model to prove it.'))

# ---------- 7. worked example: a net that fails ----------
W_,H_=4*c+20,3*c+20
base=SV(W_,H_,cellsq(UBAD,c,10,10,WHITE,None,30),'A row of 4 squares with one square above each end of the row')
o2=SV(W_,H_,cellsq([(0,1),(2,1)],c,10,10,MINTC,{(0,1):'left',(2,1):'right'},24)+cellsq([(1,1)],c,10,10,YEL,{(1,1):'base'},26),'the base and two walls')
o3=SV(W_,H_,cellsq([(0,0),(3,0)],c,10,10,PINK,{(0,0):'back',(3,0):'back'},24)+cellsq([(3,1)],c,10,10,SKY,{(3,1):'lid'},26),'two squares both land on the back, and the lid')
body=h2('A shape that does not fold')+stitle('A row of 4 with a square above each end. Fold it in your head.')
body+=pin(128,300,W_,base)+pin(128,300,W_,o2,'fade')+pin(128,300,W_,o3,'fade')
for k,t in enumerate(['Base: the second square. The squares next to it become the left and right walls.','The square on the end of the row is the lid. The square above the left wall swings to the BACK.','The square above the lid also swings to the BACK. Two squares in the same place, and nothing at the FRONT.']):
    body+=ostep(128,300,k+1,t,None,0,0,dx=500,dy=0,tw=1164,size=32).replace('top:300px',f'top:{300+k*130}px')
body+=answer(628,700,1164,'Not a net: two squares overlap and the front is missing.')
body+=soft(628,800,1164,'Test every case: if any face is covered twice, it fails.',32)
put('p4l8-we1',sec('p4l8-we1','21–23 MIN',body,'Click 1: base and the two walls beside it. Click 2: "The end square is the lid. The square above the left wall: when that wall stands up, the square swings round to the back." Click 3: "Now the square above the end square. The lid has folded over the top, so this square swings to the back too." Ask: "How many squares are at the back? How many at the front?" (2 and 0.) Think-aloud: "A net needs one of each face. Here the back is covered twice and the front is empty. It fails." Say: Having 4 squares in a row does NOT guarantee a net: where the other two squares go matters. (They must be on different sides, or both on the inside of the row.)'))

# ---------- 8. your turn: nets ----------
def mini(cells,label,c=34):
    w=max(x for x,y in cells)+1; h=max(y for x,y in cells)+1
    return SV(w*c+8,h*c+8,cellsq(cells,c,4,4,SKY,None,20,NAVY,3),label)
NA=row4(1)+[(0,0),(3,2)]; NB=[(0,0),(1,0),(2,0),(0,1),(1,1),(2,1)]; NC=[(0,0),(0,1),(0,2),(0,3),(1,1),(2,1)]
body=h2('Your turn: does it fold into a cube?')+stitle('Fold it in your head. Write YES or NO and say why.')
rowsd=[(NA,'a','A row of 4 with one square above the first and one below the last.','YES','a net'),(NB,'b','A 2 by 3 rectangle of squares.','NO','2 by 2 block'),(NC,'c','A column of 4 with two squares sticking out in a row.','NO','2 in a row')]
for i,(cells,l,t,a,_) in enumerate(rowsd):
    body+=pin(128,290+i*180,230,mini(cells,t),None,WHITE,20,'12px 20px')
    body+=qrow(400,300+i*180,980,l,t,32)+answer(1420,300+i*180,372,a)
put('p4l8-try1',sec('p4l8-try1','23–25 MIN • OPTIONAL',body,'Whiteboards (YES or NO), then click. a) YES: base the second square of the row; the other squares fold as walls; the square above the first swings to the back and the square below the last swings to the front. b) NO: it has a 2 by 2 block; 4 squares around one corner would be needed, but only 3 faces meet at a corner of a cube, so two squares overlap. c) NO: the two squares in a row stick out and one lands on top of the other (both want the same face). Ask a child to show each with a finger fold.'))

# ---------- 9. opposite faces ----------
c=88; W_,H_=4*c+20,3*c+20
LAB={(0,0):'A',(0,1):'B',(1,1):'C',(2,1):'D',(3,1):'E',(0,2):'F'}
base=SV(W_,H_,cellsq(ENDC,c,10,10,WHITE,LAB,34),'A net lettered A to F')
o1=SV(W_,H_,cellsq([(0,1),(1,1),(2,1)],c,10,10,YEL,{(0,1):'B',(1,1):'C',(2,1):'D'},34),'a line of 3: B, C, D')
o2=SV(W_,H_,cellsq([(0,0),(0,1),(0,2)],c,10,10,MINTC,{(0,0):'A',(0,1):'B',(0,2):'F'},34),'a line of 3 going down: A, B, F')
o3=SV(W_,H_,cellsq([(1,1),(2,1),(3,1)],c,10,10,PINK,{(1,1):'C',(2,1):'D',(3,1):'E'},34),'a line of 3: C, D, E')
body=h2('Opposite faces: look for a line of 3')+stitle('In a line of 3 squares, the two ends are opposite. The middle one folds between them.')
body+=pin(128,300,W_,base)+pin(128,300,W_,o1,'fade')+pin(128,300,W_,o2,'fade')+pin(128,300,W_,o3,'fade')
for k,t in enumerate(['B, C, D is a line of 3: B and D are opposite.','A, B, F is a line of 3 going down: A and F are opposite.','C, D, E is a line of 3: C and E are opposite.']):
    body+=ostep(128,300,k+1,t,None,0,0,dx=500,dy=0,tw=1164,size=34).replace('top:300px',f'top:{300+k*120}px')
body+=answer(628,700,1164,'Opposite pairs: B and D,  A and F,  C and E.')
body+=soft(628,780,1164,'Check: each letter is used once, and a pair never touches along an edge once folded.',30)
put('p4l8-we2',sec('p4l8-we2','25–27 MIN',body,'Teach before the worksheet (Q2 has a different net). Use the paper model: lay it flat, fold it, and point to the faces. Click 1: "Look along the row: B, C, D. When I fold, C is the bottom and B and D stand up on opposite sides. So B and D face each other." Click 2: the same going down: A, B, F. Click 3: C, D, E. Do NOT say "squares next to each other are opposite": opposite faces have exactly ONE square between them in a line. Ask: "Which net squares are NOT in a line of 3? Can you still find their partner?" (The last pair is what is left over.)'))
# dice try
c=70; W_,H_=3*c+20+c,4*c+20-c
dl={(1,0):'6',(0,1):'2',(1,1):'3',(1,2):'?',(2,1):'?',(3,1):'?'}
dice=SV(4*c+20,3*c+20,cellsq(CROSSN,c,10,10,WHITE,dl,36),'A dice net: 6 on top, 2 on the left, 3 in the middle and three squares with question marks')
body=h2('Your turn: fill in the dice')+stitle('Opposite faces add up to 7. The net shows 6, 2 and 3.')
body+=pin(128,300,4*c+20,dice,None,WHITE,20,'12px 20px')
for i,(t,a) in enumerate([('Below the 3.  Which number is opposite the 6?','1'),('Right of the 3.  Which number is opposite the 2?','5'),('The last square.  Which number is opposite the 3?','4')]):
    body+=qrow(520,290+i*150,880,'abc'[i],t,32)+answer(1420,290+i*150,372,a)
put('p4l8-try2',sec('p4l8-try2','27–29 MIN • OPTIONAL',body,'Whiteboards, then click. The ends of the vertical line of 3 (6, 3, ?) are opposite, so the square below the 3 is 1 (6 + 1 = 7). The horizontal row is 2, 3, ?, ?: the 2 and the square two to its right are opposite, so that is 5 (2 + 5 = 7). The last square is the end of the row, opposite the 3: 4 (3 + 4 = 7). Check: 1, 2, 3, 4, 5, 6 all appear once.'))

# ---------- key + break ----------
body=h2('Key idea: fold it in your head')+card(p('A net needs one base, one lid and four walls, with nothing in the same place twice. In a line of 3 squares, the two ends are opposite.',42,700))+card(p('A line of symmetry is a fold line: the two halves match exactly.',38,600,MUTED))
put('p4l8-key',sec('p4l8-key','29–30 MIN',body,'Say the key ideas together. Common mistakes to watch for during the worksheet: (1) Thinking any 6 squares make a cube, and ticking shapes with a 2 by 2 block, 5 squares in a row, or two squares that close the same end. (2) Saying two squares next to each other are opposite, instead of the ends of a line of 3. (3) Saying a rectangle has 4 lines of symmetry (the diagonal does not work), or completing a symmetric figure by sliding the half across instead of flipping it.'))
put('p4l8-break',break_slide('p4l8-break','30–34 MIN','Mirror partner! One of you moves slowly. The other is the mirror: raise your right hand when your partner raises their left.','Four minutes. Online: the tutor is the leader and all the children are mirrors. Ask: "Which hand does the mirror use when I raise my left hand?" (the right.) Then swap. This is the idea behind a line of symmetry: the mirror image.'))

# ---------- worksheet page 1 ----------
put('p4l8-ws1',ws_preview('p4l8-ws1','34–50 MIN','Worksheet page 1: with your partner',[('Q1','Six shapes of 6 squares. Which fold into a cube? Say why the others do not.'),('Q2','A lettered net. Which letter is opposite which?'),('Q3','Dice nets. Opposite faces add up to 7.')],'Stuck? Cut the shape out and fold it, or colour the base first.','Minutes 34 to 50. Walk around. Ask "How do you know?" before giving any help. For Q1 ask pairs to fold each shape in their heads first, then check one with paper. For Q3(b) ask: "Which squares are the ends of a line of 3?"'))
put('p4l8-ws1ans',checks('p4l8-ws1ans','50–53 MIN','Page 1: check together',[('Q1','a) 3 shapes: A, C and E.   b) B: both extra squares on the same side. D: 5 in a row. F: a 2 by 2 block.'),('Q2','A is opposite E,   B is opposite D,   C is opposite F'),('Q3','a) 3, 5, 4, 2 along the row and 6 below.   b) 5, 4 / 1, 2 / 3, 6.')],
 'Click after a pair explains. Q1: A is the cross (4 in a row with one above and one below the second square); C is the 3-3 net; E is the staircase; B puts both squares on the same side at the ends so they cover the same face; D has 5 in a row, so the 5th lands on the 1st; F has a 2 by 2 block. Q2: the net is a staircase. B, C, D is a line of 3, so B and D are opposite. A is above B and E is below D: they are the two ends of the step, so A and E are opposite. The last pair is C and F. Q3a: 1 is opposite 6; the row reads 3, 5, 4, 2 and the last square is 6. Q3b: 5 is opposite 2, 1 is opposite 6, 3 is opposite 4.',gapy=170))

# ---------- teach before page 2: complete symmetric figure ----------
c=44; W_,H_=11*c,8*c
LINE=f'<line x1="{5*c}" y1="0" x2="{5*c}" y2="{8*c}" stroke="{RED}" stroke-width="5" stroke-dasharray="12 8"/>'
def poly(pts): return f'<polyline points="{" ".join(f"{a*c},{b*c}" for a,b in pts)}" fill="none" stroke="{NAVY}" stroke-width="6" stroke-linejoin="round" stroke-linecap="round"/>'
HALF=[(5,0),(1,3),(1,7),(5,7)]
base=SV(W_,H_,grid(0,0,11,8,c)+LINE+poly(HALF),'Half of a house on a grid, with a dashed up-down line on the right of the house')
dots=''.join(f'<circle cx="{x*c}" cy="{y*c}" r="11" fill="{RED}"/>' for x,y in [(9,3)])
o1=SV(W_,H_,f'<path d="M{1*c} {3*c} H{5*c}" stroke="{TEAL}" stroke-width="7"/>'+dots+f'<path d="M{5*c} {3*c} H{9*c}" stroke="{TEAL}" stroke-width="7" stroke-dasharray="10 8"/>','4 squares from the line to the corner, so a dot 4 squares on the other side')
o2=SV(W_,H_,f'<path d="M{1*c} {7*c} H{5*c}" stroke="{TEAL}" stroke-width="7"/><circle cx="{9*c}" cy="{7*c}" r="11" fill="{RED}"/><path d="M{5*c} {7*c} H{9*c}" stroke="{TEAL}" stroke-width="7" stroke-dasharray="10 8"/>','the bottom corner and its partner')
o3=SV(W_,H_,poly([(5,0),(9,3),(9,7),(5,7)]),'the other half joined up')
body=h2('Complete the figure: count from the line')+stitle('Make the dashed line a line of symmetry.')
body+=pin(128,290,W_,base)+pin(128,290,W_,o1,'fade')+pin(128,290,W_,o2,'fade')+pin(128,290,W_,o3,'fade')
for k,t in enumerate(['The roof corner is 4 squares LEFT of the line. Put a dot 4 squares RIGHT.','The bottom corner is also 4 squares left. Put a dot 4 squares right, same height.','Join the dots in the same order. The two halves now match.']):
    body+=ostep(128,290,k+1,t,None,0,0,dx=W_+30,dy=0,tw=1664-W_-30,size=30).replace('top:290px',f'top:{290+k*130}px')
body+=soft(128+W_+30,700,1664-W_-30,'Flip, do not slide: the far corners swap sides.',30)
put('p4l8-teachsym',sec('p4l8-teachsym','53–54 MIN',body,'Teach before worksheet page 2 (Q4 has a rocket and a fish; this is a house). Click 1: run a finger along the row of squares from the line to the roof corner: 4. "A partner is the same distance on the other side." Click 2: the bottom corner. Click 3: join. Think-aloud: "Every corner needs a partner at the same height and the same distance from the line. I count squares; I do not guess." Common mistake: copying the half by sliding it to the right (it would look the same but not flipped). Ask: "If the left roof slopes down to the left, which way does the right roof slope?"'))

# ---------- teach before page 2: lines of symmetry ----------
c=40
def rectfig(x,y,w,h,extra,label):
    return f'<rect x="{x}" y="{y}" width="{w*c}" height="{h*c}" fill="{SKY}" stroke="{NAVY}" stroke-width="5"/>'+extra
def vline(x,y,h): return f'<line x1="{x}" y1="{y-14}" x2="{x}" y2="{y+h*c+14}" stroke="{RED}" stroke-width="5" stroke-dasharray="10 7"/>'
def hline(x,y,w): return f'<line x1="{x-14}" y1="{y}" x2="{x+w*c+14}" y2="{y}" stroke="{RED}" stroke-width="5" stroke-dasharray="10 7"/>'
def dline(x,y,w,h): return f'<line x1="{x}" y1="{y}" x2="{x+w*c}" y2="{y+h*c}" stroke="{NAVY}" stroke-width="5" stroke-dasharray="10 7"/>'
Rx,Ry=20,40
rec=rectfig(Rx,Ry,6,4,vline(Rx+3*c,Ry,4)+hline(Rx,Ry+2*c,6),'')
dia=rectfig(Rx+7*c+30,Ry,6,4,dline(Rx+7*c+30,Ry,6,4),'')
sq=rectfig(Rx+14*c+60,Ry,4,4,vline(Rx+14*c+60+2*c,Ry,4)+hline(Rx+14*c+60,Ry+2*c,4)+dline(Rx+14*c+60,Ry,4,4)+f'<line x1="{Rx+14*c+60+4*c}" y1="{Ry}" x2="{Rx+14*c+60}" y2="{Ry+4*c}" stroke="{NAVY}" stroke-width="5" stroke-dasharray="10 7"/>','')
lab=T(Rx+3*c,Ry+4*c+62,'rectangle: 2',34)+T(Rx+7*c+30+3*c,Ry+4*c+62,'the diagonal does not fit',30,NAVY)+T(Rx+14*c+60+2*c,Ry+4*c+62,'square: 4',34)
f1=SV(19*c+80,4*c+110,rec+dia+sq+lab,'A rectangle with 2 lines of symmetry, the same rectangle with a diagonal fold that does not match, and a square with 4 lines of symmetry')
body=h2('Find ALL the lines of symmetry')+pin(128,250,19*c+80,f1,None,WHITE,20,'10px 10px')
body+=ostep(128,250,1,'A rectangle: up-down and across. That is 2 lines.',None,0,0,dx=0,dy=0,tw=1664).replace('top:250px','top:640px')
body+=ostep(128,250,2,'Is the corner-to-corner line a line of symmetry? Fold along it: the long side lands on the short side, so the halves do NOT match. Not this one.',None,0,0,dx=0,dy=0,tw=1664,size=32).replace('top:250px','top:725px')
body+=ostep(128,250,3,'A square has 4 lines: up-down, across and both corner-to-corner lines.',None,0,0,dx=0,dy=0,tw=1664).replace('top:250px','top:830px')
put('p4l8-teachlines',sec('p4l8-teachlines','54–56 MIN',body,'Teach before worksheet page 2 (Q5). Use a paper rectangle: fold it up-down and across (the halves match) and then fold it corner to corner (the corners do not meet: the long edge lies beside the short edge). Systematic method: try up-down, across, then the two corner-to-corner lines, and mark each that works. Mention: a shape can have 0 lines (like the letter Z); that is a perfectly good answer.'))

# ---------- teach before page 2: shade to make symmetric ----------
c=70
def shgrid(shaded,extra='',fill=TEAL):
    g=''
    for x in range(4):
        for y in range(4):
            on=(x,y) in shaded
            g+=f'<rect x="{10+x*c}" y="{10+y*c}" width="{c}" height="{c}" fill="{fill if on else WHITE}" stroke="{NAVY}" stroke-width="3"/>'
    return g+extra
VL=f'<line x1="{10+2*c}" y1="0" x2="{10+2*c}" y2="{20+4*c}" stroke="{RED}" stroke-width="5" stroke-dasharray="10 7"/>'
SH=[(0,0),(1,1),(3,0)]
base=SV(4*c+20,4*c+20,shgrid(SH,VL),'A 4 by 4 grid with three shaded squares and a dashed up-down line down the middle')
o1=SV(4*c+20,4*c+20,f'<rect x="{10+0*c}" y="{10}" width="{c}" height="{c}" fill="none" stroke="{YEL}" stroke-width="9"/><rect x="{10+3*c}" y="10" width="{c}" height="{c}" fill="none" stroke="{YEL}" stroke-width="9"/>','the two top corners match')
o2=SV(4*c+20,4*c+20,f'<rect x="{10+1*c}" y="{10+c}" width="{c}" height="{c}" fill="none" stroke="{YEL}" stroke-width="9"/><rect x="{10+2*c}" y="{10+c}" width="{c}" height="{c}" fill="{TEAL}" fill-opacity="0.45" stroke="{RED}" stroke-width="7" stroke-dasharray="9 6"/>','the second row needs a partner')
body=h2('Shade one more square')+stitle('Make the dashed line a line of symmetry. Check every shaded square has a partner.')
body+=pin(128,300,4*c+20,base)+pin(128,300,4*c+20,o1,'fade')+pin(128,300,4*c+20,o2,'fade')
for k,t in enumerate(['Top row: the left corner and the right corner are the same distance from the line. They are partners already.','Second row: the shaded square is 1 square left of the line. Its partner, 1 square right of the line, is not shaded.','Shade it. Now every shaded square has a partner. Only 1 way works.']):
    body+=ostep(128,300,k+1,t,None,0,0,dx=420,dy=0,tw=1244,size=32).replace('top:300px',f'top:{300+k*135}px')
put('p4l8-teachshade',sec('p4l8-teachshade','56–57 MIN',body,'Teach before worksheet page 2 (Q6 has a different pattern and two lines). Method: take each shaded square in turn, flip it over the line, and check the partner is shaded. A square with an unshaded partner is the clue: that partner is the one to shade. Ask: "Could I shade a different square instead?" (No: any other square would have no partner.) Q6 on the worksheet has two dashed lines, so there are two ways: one for each line.'))
put('p4l8-try3',try_slide('p4l8-try3','57–58 MIN • OPTIONAL','Your turn: lines of symmetry','Use the fold test. Show a number with your fingers.',[('a','How many lines of symmetry does a square have?','4'),('b','A 5 cm by 3 cm rectangle?','2'),('c','A triangle with all three sides different lengths?','0')],'Whiteboards, then click. a) 4 (up-down, across and two corner-to-corner). b) 2 (the diagonals do not fit). c) 0: no fold makes the halves match. Extra: "A triangle with two equal sides?" (1.)',size=34))
put('p4l8-ws2',ws_preview('p4l8-ws2','58–76 MIN','Worksheet page 2: on your own',[('Q4','Complete the rocket and the fish. Count the squares from the line.'),('Q5','All the lines of symmetry of four shapes.'),('Q6','Shade ONE more square. Find all the ways.')],'Finished early? Stretch and Challenge come next.','Children work alone. Note who needs a short catch-up next lesson, especially children who count the diagonal of a rectangle as a line of symmetry.'))
put('p4l8-ws2ans',checks('p4l8-ws2ans','76–80 MIN','Page 2: check together',[('Q4','Each corner has a partner the same number of squares from the line, flipped to the other side.'),('Q5','a) T shape 1   b) H shape 2   c) plus 4   d) zigzag 0'),('Q6','2 ways: shade A2 (up-down line) or shade D3 (across line).')],
 'Click after a child explains. Q4: ask a child to say "this corner is 2 squares from the line, so its partner is 2 squares on the other side". Q5: the H has up-down and across; the plus has up-down, across and two corner-to-corner lines; the zigzag of 4 (an S shape) has none: it can be turned half a turn onto itself but never folded. Q6: shade A2: B2 has partner C2 across the up-down line; D2 needs A2. Shade D3: the across line needs B2 with B3, C2 with C3, and D2 with D3 (B3 and C3 are already shaded).',gapy=190,size=32))

# ---------- stretch / challenge ----------
from p4bank import th_items, th_notes, gf_numbers  # slide Think harder = the printed page (docs/audit/reaudit_fixes_p4.md)
st=th_items(8)
def numgrid(items,size=30): return '<div style="display:grid;grid-template-columns:1fr 1fr;gap:24px;align-items:stretch">'+''.join(card(p(f'<span style="color:{TEAL}">{a}</span>  {E(b)}',size,600,raw=True),extra='padding:24px 32px') for a,b in items)+'</div>'
put('p4l8-stretch',sec('p4l8-stretch','Early finishers / take-home',h2('Think harder')+numgrid(st,34),th_notes(8)))
ch=[('1.','Two dice are glued together face to face, and the two glued faces show the same number. The numbers on all the faces you can still see add up to 36. What number is on the glued faces?'),('2.','Shade exactly 5 squares of a 3 by 3 grid so that the pattern has 4 lines of symmetry. There are 2 ways. Find both.')]
put('p4l8-challenge',sec('p4l8-challenge','Early finishers / take-home',h2('Go further')+numcards(ch,36),'Pairs try first, then use the "see it" slide if stuck, then the walk-through. Answers: 1) 3 (two dice have 42 altogether; the 2 hidden faces are equal and 42 − 36 = 6, so each is 3). 2) The centre and the 4 corners (an X), or the centre and the 4 edge-middle squares (a plus).'))
c=60
dd=f'<rect x="20" y="40" width="150" height="150" fill="{WHITE}" stroke="{NAVY}" stroke-width="5"/><rect x="170" y="40" width="150" height="150" fill="{WHITE}" stroke="{NAVY}" stroke-width="5"/><rect x="150" y="30" width="40" height="170" rx="8" fill="{YEL}" stroke="{RED}" stroke-width="5" stroke-dasharray="9 6"/>'+T(170,235,'glued: same number',28,TEAL)+T(95,120,'dice',34)+T(245,120,'dice',34)+T(170,275,'visible faces add to 36',28,NAVY)
g3=''.join(f'<rect x="{20+x*c}" y="{20+y*c}" width="{c}" height="{c}" fill="{WHITE}" stroke="{NAVY}" stroke-width="3"/>' for x in range(3) for y in range(3))
g3+=f'<line x1="{20+1.5*c}" y1="6" x2="{20+1.5*c}" y2="{34+3*c}" stroke="{RED}" stroke-width="4" stroke-dasharray="9 6"/><line x1="6" y1="{20+1.5*c}" x2="{34+3*c}" y2="{20+1.5*c}" stroke="{RED}" stroke-width="4" stroke-dasharray="9 6"/><line x1="20" y1="20" x2="{20+3*c}" y2="{20+3*c}" stroke="{RED}" stroke-width="4" stroke-dasharray="9 6"/><line x1="{20+3*c}" y1="20" x2="20" y2="{20+3*c}" stroke="{RED}" stroke-width="4" stroke-dasharray="9 6"/>'
body=h2('Go further: see it',60)+'<div style="display:flex;gap:32px;align-items:flex-start">'
body+=card(f'<p style="font-size:30px;font-weight:700;color:{TEAL}">Q1: Two dice glued together</p>'+SV(340,300,dd,'Two dice side by side with the glued faces marked').replace('style="width:340px;height:300px;flex:none"','style="width:62%;margin:0 auto;height:auto;display:block"'),extra='flex:1;min-width:0;padding:20px 24px')
body+=card(f'<p style="font-size:30px;font-weight:700;color:{TEAL}">Q2: A 3 by 3 grid with 4 lines of symmetry</p>'+SV(3*c+40,3*c+40,g3,'A 3 by 3 grid with its four lines of symmetry drawn').replace(f'style="width:{3*c+40}px;height:{3*c+40}px;flex:none"','style="width:50%;height:auto;display:block;margin:0 auto"'),extra='flex:1;min-width:0;padding:20px 24px')+'</div>'
put('p4l8-chdiag',sec('p4l8-chdiag','Early finishers / take-home',body,'Show after pairs have tried the Challenge, or if they are stuck. The pictures show the problem, not the answer. Ask: Q1 "How many faces does one dice have? How many faces are hidden in all?" Q2 "Which square lies on ALL four lines? Which squares are partners under every line?" Answers are in the Challenge slide notes.'))
body=h2('Go further: walk-through')+pin(128,250,800,p('Q1: count the hidden faces',38,800,TEAL))
for i,t in enumerate(['Two dice: 21 + 21 = 42 (1 + 2 + … + 6 = 21 each)','Hidden: the 2 glued faces, both the same number','42 − 36 = 6 for the 2 hidden faces','6 ÷ 2 = 3 on each glued face ✓']): body+=pin(128,330+i*120,800,p(t,32),'rise',WHITE)
body+=pin(992,250,800,p('Q2: the middle, then a team of 4',38,800,TEAL))
for i,t in enumerate(['The middle square is on all 4 lines: it must be shaded.','Every other square has 3 partners: the 4 corners go together, the 4 edge squares go together.','5 = 1 + 4: shade the middle and one team.','Two teams, so 2 ways: an X or a plus.']): body+=pin(992,330+i*120,800,p(t,32),'rise',WHITE)
put('p4l8-chwalk',sec('p4l8-chwalk','Early finishers / take-home',body,'Use after pairs have tried. Q1: the trick is to count the hidden faces, not the visible ones. Check: if the glued number were 2, the hidden total would be 4 and the visible total 38. Q2: a square on a line of symmetry stays put when we fold along that line; the middle square lies on all four, so it must be shaded for any pattern to be symmetric under every line (or be empty). A corner square flips to another corner, so if one corner is shaded all four must be: that is a team of 4. The edge-middle squares are another team of 4.'))

# ---------- talk / exit ----------
body=h2('Talk time')+card(chip('TALK TIME',YEL,NAVY)+p('Mei says: "Every shape made of 6 squares folds into a cube." Ben says: "If a shape has 4 squares in a row, it always folds into a cube." Who is right?',40,600))+card(p('Sentence starters:',34,400,MUTED)+p('“I noticed that …”   “I tested it by …”   “I know because …”',38,600))
put('p4l8-talk',sec('p4l8-talk','80–85 MIN',body,'Minutes 80 to 85. Pairs talk for 2 minutes, then share. Answer: neither is right. A 2 by 3 rectangle has 6 squares and does not fold (it has a 2 by 2 block), so Mei is wrong. A row of 4 with one square above each end does not fold either, because both extra squares cover the back, so Ben is wrong. One counter-example is enough to show a rule is not always true. Second question if time: "How can you tell two faces are opposite without folding?" (They are the ends of a line of 3 squares.) Praise the reasons, not only the answers.'))
c=80
dl2={(0,0):'3',(1,1):'1',(1,0):'2',(2,1):'?'}
NETX=[(0,0),(1,0),(1,1),(2,1),(3,1),(3,2)]
exfig=SV(4*c+20,3*c+20,cellsq(NETX,c,10,10,WHITE,dl2,40),'A dice net with 3, 2, 1 and a question mark in the squares, and two more empty squares')
body=h2('Exit ticket')+card(chip('EXIT TICKET')+f'<div style="display:flex;gap:40px;align-items:center">{exfig}'+p('This dice net shows 3, 2 and 1. Opposite faces add up to 7. Which number goes in the square marked "?"',42,600)+'</div>')+card(p('Write your answer on a slip of paper. Show it to your tutor. Then collect your stamp in your inquiry journal.',34,400))
put('p4l8-exit',sec('p4l8-exit','85–88 MIN',body,'Minutes 85 to 88. Answer: 4. The 3, 2, 1 and ? squares make a staircase: the 3 and the ? are the two ends of the step, so they are opposite, and 3 + 4 = 7. Children who write 6 or 5 chose a square next to it. Extension: fill in the other two squares. The square right of the ? is opposite the 1, so 6; the bottom-right square is opposite the 2, so 5.'))

# ---------- write ----------
# ---------- fix pass (rebuild/p4_fix.py): sneak-peek puzzles, looking back, neutral names, go further, minute labels ----------
import subprocess as _sp, p4_fix
_G=json.loads(_sp.check_output(['node','-e',"process.stdout.write(JSON.stringify(require('"+os.path.join(H,'..','p4','content','l8.js')+"').gaps))"]))
_ID='p4l8'
_PIC=globals().get('PIC')

order=['p4l8-title','p4l8-warm1','p4l8-warm2','p4l8-explore1','p4l8-explore2','p4l8-teach1','p4l8-we1','p4l8-try1','p4l8-we2','p4l8-try2','p4l8-key','p4l8-break','p4l8-ws1','p4l8-ws1ans','p4l8-teachsym','p4l8-teachlines','p4l8-teachshade','p4l8-try3','p4l8-ws2','p4l8-ws2ans','p4l8-stretch','p4l8-challenge','p4l8-chdiag','p4l8-chwalk','p4l8-talk','p4l8-exit']
p4_fix.finish(S,8,_G,pic=_PIC)
order=p4_fix.order(order,8)
assert set(order)==set(S), set(order)^set(S)
sd=os.path.join(D,'slides')
for f in os.listdir(sd):
    if f.endswith('.html') and f[:-5] not in S: os.remove(os.path.join(sd,f))
for i,h in S.items(): open(os.path.join(sd,i+'.html'),'w').write(h)
deck={'v':4,'createdOnFiles':{'v':1,'at':datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')},'lists':'css',
 'title':'Math Inquirers P4: Lesson 8 – Symmetry and Nets','order':order,'cover':'p4l8-title',
 'sections':{'s1':{'description':'Warm-up and explore','start':'p4l8-title'},'s2':{'description':'Teach: fold nets in your head, opposite faces','start':'p4l8-teach1'},'s3':{'description':'Worksheet with teaching before each page','start':'p4l8-break'},'s4':{'description':'Stretch, challenge, talk and exit','start':'p4l8-stretch'}},
 'faces':{'fredoka':{'family':'Fredoka','href':'https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&display=swap'},'nunito-sans':{'family':'Nunito Sans','href':'https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@400;600;700&display=swap'}},
 'designSystems':[]}
json.dump(deck,open(os.path.join(D,'deck.json'),'w'),indent=1,ensure_ascii=False)
print(len(order),'slides')
