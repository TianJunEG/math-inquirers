import json,os,sys,math
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,H)
from slidekit import *
D=os.path.join(H,'..','split','l7','project'); S={}
def put(i,h): S[i]=h
RED='#D64545'; BLUE='#3A6EA5'; MINT='#D3F1E4'

# ---------- small SVG helpers (same style as slidekit: navy strokes, yellow/sky fills, Fredoka text) ----------
def SV(w,h,body,label): return f'<svg aria-label="{E(label)}" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="width:{w}px;height:{h}px">{body}</svg>'
def R(x,y,w,h,fill=WHITE,stroke=NAVY,sw=4,rx=0): return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'
def T(x,y,s,size=40,fill=NAVY,weight=700): return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" text-anchor="middle" fill="{fill}" font-family="Fredoka, Arial">{E(str(s))}</text>'
def PG(pts,fill=WHITE,stroke=NAVY,sw=4): return f'<polygon points="{" ".join(f"{a:.1f},{b:.1f}" for a,b in pts)}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round"/>'
def CI(x,y,r,fill=WHITE,stroke=NAVY,sw=4): return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'
def TICK(x,y,s=20,col=TEAL,sw=8): return f'<path d="M{x-s} {y} L{x-s/3:.1f} {y+s*0.7:.1f} L{x+s} {y-s*0.8:.1f}" fill="none" stroke="{col}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"/>'
def CROSS(x,y,s=50,col=RED,sw=10): return f'<path d="M{x-s} {y-s} L{x+s} {y+s} M{x+s} {y-s} L{x-s} {y+s}" fill="none" stroke="{col}" stroke-width="{sw}" stroke-linecap="round"/>'
def gridb(x,y,cols,rows,c,sw=4,fill=WHITE):
    """grid as 2 elements: outer rect + one path for inner lines"""
    d=''.join(f'M{x+i*c} {y} V{y+rows*c} ' for i in range(1,cols))+''.join(f'M{x} {y+j*c} H{x+cols*c} ' for j in range(1,rows))
    return R(x,y,cols*c,rows*c,fill,NAVY,sw)+(f'<path d="{d}" stroke="{NAVY}" stroke-width="{sw}" fill="none"/>' if d else '')
def hi(x,y,w,h): return R(x,y,w,h,YEL,TEAL,6)
def thumbs(n,w,h,draw,gap=24,label='thumbnails'):
    body=''.join(draw(i*(w+gap),i) for i in range(n))
    return SV(n*w+(n-1)*gap,h,body,label)
def cells_svg(cells,c,pad=6,fill=SKY,label='shape of squares'):
    W=max(a for a,b in cells)+1; Hh=max(b for a,b in cells)+1
    return SV(W*c+2*pad,Hh*c+2*pad,''.join(R(pad+a*c,pad+b*c,c,c,fill,NAVY,4) for a,b in cells),label)
def ostep(left,top,n,text,ov=None,ovw=0,ovh=0,dx=0,dy=0,tw=1000,size=34,extra='',row=False,twt=None,build='fade'):
    """One click = overlay marks (same left/top as the base picture) + the step text box beside it."""
    lab=f'<span style="color:{TEAL};font-weight:800">Step {n}.</span>  ' if n else ''
    ws=f'width:{twt}px;flex:none;' if row and twt else ''
    tx=f'<p style="{ws}font-size:{size}px;font-weight:600;line-height:1.3">{lab}{E(text)}</p>'
    inner=f'<div style="display:flex;align-items:center;gap:24px">{tx}{extra}</div>' if row else tx+extra
    box=f'<div style="margin-top:{dy}px;width:{tw}px;box-sizing:border-box;background:{WHITE};border-radius:20px;padding:16px 28px;display:flex;flex-direction:column;gap:10px;flex:none">{inner}</div>'
    if ov is None and ovw==0: return pin(left+dx,top,tw,box,build)
    o=f'<div style="width:{ovw}px;height:{ovh}px;flex:none">{ov or ""}</div>'
    return pin(left,top,dx+tw,f'<div style="display:flex;align-items:flex-start;gap:{dx-ovw}px">{o}{box}</div>',build)
def soft(left,top,width,text,size=34,build='fade'): return pin(left,top,width-56,p(text,size,700),build,SOFT,20,'18px 28px')
def stitle(t,size=34): return p(t,size,600,MUTED)

# ---------- 3. quick questions ----------
qs=[('1.','How many sides has a triangle?','3'),('2.','How many corners has a square?','4'),('3.','Which shape has no corners?','circle'),('4.','Fold a square in half, edge to edge. What shapes do you get?','2 rectangles')]
body=h2('Quick questions')+''.join(qrow(128,260+i*150,1250,a,b) for i,(a,b,c) in enumerate(qs))+''.join(answer(1420,260+i*150,372,c) for i,(a,b,c) in enumerate(qs))
put('l7-warm2',sec('l7-warm2','5–10 MIN',body,'Minutes 5 to 10. Read each question aloud, give thinking time, take answers, then click to show the answer. Ask "How do you know?" each time. For 4, fold a paper square in front of them after they answer: two rectangles of the same size. Answers: 1) 3  2) 4  3) circle  4) 2 rectangles (if a child says 2 triangles, they folded corner to corner: that is what we do in Explore next).'))

# ---------- 6. teach: squares hide inside squares (2 by 2) ----------
c=170; base=SV(360,360,gridb(10,10,2,2,c),'A 2 by 2 grid of squares')
ov1=SV(360,360,''.join(T(10+c*(i%2)+c/2,10+c*(i//2)+c/2+22,i+1,64,TEAL) for i in range(4)),'small squares numbered 1 to 4')
ov2=SV(360,360,R(10,10,340,340,'none',TEAL,14,6),'the whole grid outlined')
body=h2('Squares hide inside bigger squares')+stitle('How many squares can you see? Count the small ones first, then the bigger ones.')
body+=pin(128,320,360,base)
body+=ostep(128,320,1,'Small squares: 1, 2, 3, 4.',ov1,360,360,dx=440,dy=0,tw=1224)
body+=ostep(128,320,2,'The whole grid is a square too. It is made of 4 small ones: 1 more.',ov2,360,360,dx=440,dy=120,tw=1224)
body+=ostep(128,320,3,'Add them: 4 + 1 = 5 squares.',dx=440,dy=0,tw=1224).replace('top:320px','top:580px')
body+=soft(568,700,1224,'Why count by size? Then we never miss a square, and we never count one twice.')
put('l7-teach1',sec('l7-teach1','25–27 MIN',body,'Teach. Ask first: "How many squares can you see?" Most children say 4. Do not correct them yet. Click 1: number the small squares. Click 2: run your finger round the outside: "Is this a square? 4 straight sides, all the same length, 4 square corners. Yes! It is made of 4 small squares." Click 3: 4 + 1 = 5. Click 4: the why. Think-aloud: "Squares can hide inside bigger squares. So I count by size: all the small ones first, then the next size up, then the next. That way I do not miss any and I do not count any twice."'))

# ---------- 7. worked example: 3 by 3 grid ----------
c=100; base=SV(320,320,gridb(10,10,3,3,c),'A 3 by 3 grid of squares')
ov1=SV(320,320,''.join(T(10+c*(i%3)+c/2,10+c*(i//3)+c/2+17,i+1,48,TEAL) for i in range(9)),'small squares numbered 1 to 9')
ov3=SV(320,320,R(10,10,300,300,'none',TEAL,14,6),'the whole grid outlined')
tc=34
def th2(x,i):
    a,b=i%2,i//2
    return gridb(x+4,4,3,3,tc,3)+hi(x+4+a*tc,4+b*tc,2*tc,2*tc)
t2=thumbs(4,110,110,th2,26,'the four 2 by 2 squares')
body=h2('Worked example: how many squares?')+stitle('This grid is 3 squares long and 3 squares high. Count by size.')
body+=pin(128,310,320,base)
body+=ostep(128,310,1,'Small squares: 3 in each row, 3 rows. 3 + 3 + 3 = 9',ov1,320,320,dx=380,dy=0,tw=1284)
body+=ostep(128,310,2,'Squares made of 4 small ones: slide a 2 by 2 window along. 4 of them.',dx=380,tw=1284,extra=t2).replace('top:310px','top:420px')
body+=ostep(128,310,3,'The whole grid is 1 big square.',ov3,320,320,dx=380,dy=360,tw=1284)
body+=answer(508,785,1228,'9 + 4 + 1 = 14 squares')
put('l7-we1',sec('l7-we1','27–29 MIN',body,'Click to reveal each step. Before each click, ask the group to predict. Step 1: count the small squares row by row. Step 2: hold up a paper 2 by 2 window (or cut one from card) and slide it: top left, top right, bottom left, bottom right. "Can it go anywhere else?" No: 4 places. Step 3: the whole grid. Think-aloud: "I count by size. Small squares: 9. Squares 2 across and 2 down: I slide my window, 4 places. Squares 3 across and 3 down: just the whole grid, 1. 9 + 4 + 1 = 14." Watch for children who count squares made of 2 small squares side by side: that shape is a rectangle, not a square.'))

# ---------- 8. your turn: squares ----------
row3=SV(222,82,gridb(6,6,3,1,70),'A row of 3 squares')
lsh=cells_svg([(0,0),(1,0),(0,1),(1,1),(2,1)],56,6,WHITE,'A 2 by 2 square with one more square on the right')
body=h2('Your turn: count the squares')+stitle('Draw it on your whiteboard. Small ones first, then bigger ones.')
body+=pin(128,330,300,row3,None,WHITE,20,'24px 30px')+qrow(500,330,880,'a','How many squares are in a row of 3 squares?',38)+answer(1420,330,372,'3')
body+=pin(128,480,300,lsh,None,WHITE,20,'18px 30px')+qrow(500,480,880,'b','A 2 by 2 square with one more square stuck on. How many squares?',38)+answer(1420,480,372,'6')
body+=qrow(128,700,1252,'c','Draw a shape made of small squares that has exactly 5 squares in it.',38)+answer(1420,700,372,'2 by 2 grid, or a row of 5')
put('l7-try1',sec('l7-try1','29–30 MIN',body,'Whiteboards up together, then click. a) 3: there is no bigger square, because a bigger square needs 2 rows. b) 6: 5 small squares and 1 square made of 4 small ones (the 2 by 2 part). The extra square cannot make a second big square because the square above it is missing: show this with your 2 by 2 window. c) Open: a 2 by 2 grid (4 + 1) or a row of 5 small squares (5 + 0) both work. Ask a child with each answer to explain.'))

# ---------- 9. worked example: rectangles in a strip of 4 ----------
c=95; base=SV(400,115,gridb(10,10,4,1,c),'A strip of 4 squares')
sc=36
def strip_th(L):
    def f(x,i): return gridb(x+3,3,4,1,sc,3)+hi(x+3+i*sc,3,L*sc,sc)
    return f
body=h2('Worked example: rectangles in a strip')+stitle('A strip of 4 squares. How many rectangles? In this puzzle only, count squares as rectangles too.')
body+=pin(128,320,400,base)+pin(128,480,364,p('Count by length: shortest first.',34,700),None,SOFT,20,'18px 28px')
for k,(L,n) in enumerate([(1,4),(2,3),(3,2),(4,1)]):
    t=thumbs(n,150,42,strip_th(L),16,f'rectangles {L} squares long')
    body+=pin(608,310+k*120,1184,f'<div style="display:flex;align-items:center;gap:24px"><p style="width:440px;flex:none;font-size:34px;font-weight:600;line-height:1.3"><span style="color:{TEAL};font-weight:800">Step {k+1}.</span>  {L} square{"s" if L>1 else ""} long: {n}</p>{t}</div>','fade',WHITE,20,'16px 28px')
body+=answer(608,800,1128,'4 + 3 + 2 + 1 = 10 rectangles')
put('l7-we2',sec('l7-we2','30–32 MIN',body,'Click to build each length. Say first: "In this puzzle a square counts as a rectangle. Why? A rectangle has 4 square corners and its opposite sides are the same length. A square has all of that too." (On the worksheet\'s house picture, squares still go only in the Square column.) Think-aloud: "I count by length, shortest first. 1 square long: there are 4. 2 squares long: I slide it along: 3 places. 3 squares long: 2 places. The whole strip: 1. Each time the length goes up by 1, there is one fewer place. 4 + 3 + 2 + 1 = 10." Use a paper strip and a card window to slide along it.'))

# ---------- 10. your turn: strips ----------
put('l7-try2',try_slide('l7-try2','32–33 MIN','Your turn: rectangles in strips','Draw the strip. Count by length, shortest first.',[('a','A strip of 2 squares. How many rectangles?','3'),('b','A strip of 5 squares. How many rectangles are 2 squares long?','4'),('c','A strip of 4 squares. How many rectangles are NOT squares?','6')],'Whiteboards, then click. a) 2 + 1 = 3. b) Slide a 2-long window along 5 squares: it fits in 4 places. c) From the worked example there are 10 rectangles; the 4 single squares are squares, so 10 − 4 = 6 (3 that are 2 long, 2 that are 3 long, 1 that is 4 long). Ask a child to show b by sliding a finger along the strip.'))

# ---------- 11. composing with 3 squares ----------
sh_line=cells_svg([(0,0),(1,0),(2,0)],50,6,SKY,'three squares in a line')
sh_L=cells_svg([(0,0),(0,1),(1,1)],50,6,SKY,'an L of three squares')
sh_L2=SV(250,112,''.join(R(6+a*50,6+b*50,50,50,SKY,NAVY,4) for a,b in [(0,0),(1,0),(1,1)])+''.join(R(144+a*50,6+b*50,50,50,SKY,NAVY,4) for a,b in [(1,0),(0,1),(1,1)]),'the L turned two ways')
corner=SV(250,112,R(30,6,50,50,SKY,NAVY,4)+R(80,56,50,50,SKY,NAVY,4)+CROSS(190,56,34,RED,9),'two squares touching only at a corner: not allowed')
body=h2('Make shapes from 3 squares')+stitle('Join 3 same-size squares. Whole sides must touch. How many different shapes?')
body+=pin(1310,310,426,p('Not allowed: squares that touch only at a corner.',32,700)+corner,None,SOFT,20,'20px 28px')
for k,(t,pic) in enumerate([('Put them all in a row: a line.',sh_line),('Move one end square up: an L.',sh_L),('Turn or flip the L. It is the same shape, so it is not new.',sh_L2)]):
    body+=pin(128,310+k*150,1100,f'<div style="display:flex;align-items:center;gap:24px"><p style="width:700px;flex:none;font-size:34px;font-weight:600;line-height:1.3"><span style="color:{TEAL};font-weight:800">Step {k+1}.</span>  {E(t)}</p>{pic}</div>','fade',WHITE,20,'14px 28px')
body+=answer(128,770,1104,'Only 2 different shapes: the line and the L.')
put('l7-we3',sec('l7-we3','33–34 MIN',body,'Use 3 real squares (paper or pattern blocks) under the visualiser. Click through the steps. Think-aloud: "I start with all three in a row. Now I move one end square up, so it sits on top of its neighbour: an L. What if I move the middle square up? Then it only touches at corners: not allowed. If I turn the L or flip it over, it is the same L, just turned. So with 3 squares there are only 2 shapes." Let children try to find a third one with their own squares: every try is a line or an L. The stretch asks the same question with 4 squares.'))

# ---------- 12. key idea ----------
body=h2('Key idea: count in order')+card(p('Count the smallest shapes first. Then count the bigger shapes made of smaller ones. Add them up.',44,700))+card(p('Turning or flipping a shape does not make a new shape.',38,600,MUTED))+card(p('On the house picture, a square goes in the Square column only.',38,600,MUTED))
put('l7-key',sec('l7-key','34–35 MIN',body,'Say the key ideas together. Common mistakes to watch for during the worksheet: (1) Counting only the small shapes: in the square with both lines from corner to corner (Q4 picture C) children write 4 instead of 8. Ask "Are there bigger triangles made of 2 small ones?" (2) In the house picture (Q1), counting a square window in both the Square and the Rectangle columns. Each shape goes in one column only. (3) Saying a circle has 1 side, or counting the same side twice when going round a shape: put a dot where you start. (4) Thinking a turned or flipped shape is a new one.'))

# ---------- 14. teach before page 1: counting shapes in a picture ----------
rob=(R(0,0,440,500,WHITE,'none',0,24)+PG([(220,22),(170,92),(270,92)],YEL)+R(145,92,150,150,SKY)+CI(185,145,20)+CI(255,145,20)+R(175,195,90,22,GREY)
     +R(110,255,220,160,MINT)+CI(220,335,26,YEL)+R(130,425,70,45,GREY)+R(240,425,70,45,GREY))
base=SV(440,500,rob,'Robot made of shapes: a triangle hat, a square head, two round eyes, a rectangle mouth, a rectangle body, a round button and two rectangle feet')
ov1=SV(440,500,TICK(185,145,16)+TICK(255,145,16)+TICK(220,335,18),'ticks on the 3 circles')
ov2=SV(440,500,TICK(220,68,16,BLUE)+TICK(220,180,16,BLUE)+TICK(220,206,12,BLUE,6)+TICK(160,300,18,BLUE)+TICK(165,447,14,BLUE,6)+TICK(275,447,14,BLUE,6),'ticks on the other shapes')
body=h2('Count shapes in a picture: one kind at a time')
body+=pin(128,250,440,base)
body+=ostep(128,250,1,'Pick one kind. Find every circle and tick it as you count: 3 circles.',ov1,440,500,dx=500,dy=0,tw=1164)
body+=ostep(128,250,2,'Then the next kind: triangles 1, squares 1, rectangles 4. A square goes only in the Square column.',ov2,440,500,dx=500,dy=130,tw=1164)
body+=ostep(128,250,3,'Add: 3 + 1 + 1 + 4 = 9 shapes. Every shape has one tick: none missed, none counted twice.',dx=500,tw=1164).replace('top:250px','top:520px')
body+=trow(628,680,['Circle','Triangle','Square','Rectangle'],[260,260,260,260],None,True)+trow(628,766,['3','1','1','4'],[260,260,260,260],'rise')
put('l7-teachpic',sec('l7-teachpic','40–41 MIN',body,'Teach before worksheet page 1 (Q1 counts the shapes in a house picture; this robot is a different picture). Click 1: tick the circles one by one: the two eyes and the button. Click 2: tick the others in a new colour: the hat is a triangle, the head is a square, the mouth, the body and the two feet are rectangles. Click 3: add. Click 4: fill the table. Think-aloud: "If I jump around the picture I will miss one or count one twice. So I pick one kind of shape, find every one and tick it. Then the next kind." Say clearly: a square goes in the Square column only, even though a square is a special rectangle.'))

# ---------- 15. teach before page 1: sides and corners ----------
pts=[(o+x*1.1,o+y*1.1) for x,y in [(100,0),(200,0),(200,100),(300,100),(300,200),(200,200),(200,300),(100,300),(100,200),(0,200),(0,100),(100,100)] for o in [45]]
base=SV(420,420,PG(pts,SKY),'A plus-shaped figure')
ov1=SV(420,420,CI(pts[0][0],pts[0][1],13,RED,NAVY,3),'start dot')
lab=''
for i in range(12):
    (x1,y1),(x2,y2)=pts[i],pts[(i+1)%12]; dx_,dy_=x2-x1,y2-y1; L=math.hypot(dx_,dy_); nx,ny=dy_/L,-dx_/L
    mx,my=(x1+x2)/2+nx*26,(y1+y2)/2+ny*26
    lab+=T(round(mx),round(my+10),i+1,28,TEAL,800)
ov2=SV(420,420,lab,'sides numbered 1 to 12')
ov3=SV(420,420,''.join(CI(x,y,9,YEL,NAVY,3) for x,y in pts),'dots on all 12 corners')
def reg(cx,cy,r,n): return [(cx+r*math.cos(-math.pi/2+2*math.pi*k/n),cy+r*math.sin(-math.pi/2+2*math.pi*k/n)) for k in range(n)]
names=SV(1664,200,''.join(PG(reg(x,76,68,n),SKY)+T(x,180,nm,32) for x,n,nm in [(330,5,'pentagon'),(830,6,'hexagon'),(1330,8,'octagon')]),'Shape names: pentagon, hexagon, octagon')
body=h2('Sides and corners: mark where you start')
body+=pin(128,240,420,base)
body+=ostep(128,240,1,'Put a dot on one corner. That is where you start.',ov1,420,420,dx=470,dy=10,tw=1194,size=32)
body+=ostep(128,240,2,'Go round. Count each side until you are back at the dot: 12 sides.',ov2,420,420,dx=470,dy=115,tw=1194,size=32)
body+=ostep(128,240,3,'Go round again. Count the corners: 12 corners.',ov3,420,420,dx=470,dy=240,tw=1194,size=32)
body+=soft(598,575,1194,'What do you notice? Is it true for every shape? Test it on page 1.')
body+=pin(128,680,1664,names,None,WHITE,20,'8px 0px')
put('l7-teachsides',sec('l7-teachsides','41–42 MIN',body,'Teach before worksheet page 1 (Q2 is a sides and corners table). Click 1: the start dot. Click 2: trace the outline with your finger and count the sides aloud with the children. Click 3: go round again for the corners (dots). Think-aloud: "This shape has lots of sides, so I could easily lose my place. I put a dot where I start, count each side, and stop when I am back at the dot." Then ask "What do you notice?" but let them test the idea on the worksheet table; do not tell them the rule. The names at the bottom are for Q2: children count the sides of each shape themselves on the worksheet. Memory help: an octopus has 8 arms (octagon).'))

put('l7-ws1',ws_preview('l7-ws1','42–52 MIN','Worksheet page 1: with your partner',[('Q1','Count the shapes in the house. One kind at a time, tick as you count.'),('Q2','Sides and corners table. Put a dot where you start, then go round.')],'Stuck? Hold a pattern block and count its sides with your finger.','Minutes 42 to 52. Walk around. Ask "How do you know?" before giving any help. For Q1 check that pairs tick each shape. For Q2 ask "What do you notice about the two numbers?" and "Does it work for every shape?"'))
put('l7-ws1ans',check_slide('l7-ws1ans','52–54 MIN','Page 1: check together',[('Q1','Circle 1,  triangle 2,  square 3,  rectangle 2.   Most: squares.   8 shapes.'),('Q2','Square 4 and 4,  pentagon 5 and 5,  hexagon 6 and 6,  octagon 8 and 8'),('Q2a, b','Sides and corners are always the same number.   7 sides: 7 corners.')],'Click each answer after a pair explains theirs. Q1: the sun is the circle; the roof and the flag are triangles; the 3 windows are squares; the wall and the door are rectangles. 1 + 2 + 3 + 2 = 8. Q2b: "Each side ends at a corner, and going round, each corner starts the next side, so there are as many corners as sides."',lw=240))

# ---------- page 2 teach: who am I ----------
xs=[140,417,694,971,1248,1525]
shp=(PG([(xs[0],22),(xs[0]-80,150),(xs[0]+80,150)],SKY)+R(xs[1]-64,22,128,128,SKY)+R(xs[2]-100,42,200,96,SKY)+CI(xs[3],86,64,SKY)
     +PG(reg(xs[4],92,70,5),SKY)+PG(reg(xs[5],88,70,6),SKY))
shp+=''.join(T(x,212,nm,32) for x,nm in zip(xs,['triangle','square','rectangle','circle','pentagon','hexagon']))
base=SV(1664,230,shp,'Six shapes: triangle, square, rectangle, circle, pentagon, hexagon')
ov1=SV(1664,230,''.join(CROSS(xs[i],86,56) for i in [0,3,4,5]),'triangle, circle, pentagon and hexagon crossed out')
ov2=SV(1664,230,CROSS(xs[1],86,56)+R(xs[2]-122,10,244,216,'none',TEAL,8,24),'square crossed out, rectangle circled')
def colstep(top,n,text,ov,dy,size=32):
    box=f'<div style="margin-top:{dy}px;width:1664px;box-sizing:border-box;background:{WHITE};border-radius:20px;padding:14px 28px"><p style="font-size:{size}px;font-weight:600;line-height:1.3"><span style="color:{TEAL};font-weight:800">Step {n}.</span>  {E(text)}</p></div>'
    o=f'<div style="width:1664px;height:230px">{ov or ""}</div>'
    return pin(128,top,1664,o+box,'fade',extra='gap:0px;')
body=h2('Who am I? Cross out shapes that do not fit')+card(p('I have 4 corners. My sides are not all the same length. Who am I?',40,700),extra='padding:24px 40px')
body+=pin(128,370,1664,base)
body+=colstep(370,1,'Clue 1: 4 corners. Cross out every shape that does not have 4 corners.',ov1,16)
body+=colstep(370,2,'Clue 2: sides not all the same length. Cross out the square.',ov2,111)
body+=colstep(370,3,'One shape is left. I am a rectangle. Check it with every clue ✓',None,206)
put('l7-teachwho',sec('l7-teachwho','54–55 MIN',body,'Teach before worksheet page 2 (Q3 is three "Who am I?" riddles). Read the riddle aloud. Click 1: "Which shapes have 4 corners? Count with me." Cross out the triangle (3), the circle (0), the pentagon (5) and the hexagon (6). Click 2: "Square or rectangle? A square has all sides the same length. My sides are not all the same, so cross out the square." Click 3: check: a rectangle has 4 corners, and its long sides and short sides are different lengths ✓. Think-aloud: "I read one clue at a time and cross out every shape that does not fit. When one shape is left, I check it against every clue."'))

# ---------- page 2 teach: triangles ----------
A=(210,20); B=(20,330); Cc=(400,330); m1=(146.7,330); m2=(273.3,330)
base=SV(420,350,PG([A,B,Cc],WHITE)+f'<path d="M{A[0]} {A[1]} L{m1[0]} {m1[1]} M{A[0]} {A[1]} L{m2[0]} {m2[1]}" stroke="{NAVY}" stroke-width="4"/>','A triangle with 2 lines from the top corner to the bottom')
tw_,th_=140,110
def tri_th(parts):
    xs3=[6,6+128/3,6+256/3,134]
    def f(x,i):
        a,b=parts[i]
        return (PG([(x+70,6),(x+xs3[a],104),(x+xs3[b],104)],YEL,TEAL,5)+PG([(x+70,6),(x+6,104),(x+134,104)],'none',NAVY,3)
                +f'<path d="M{x+70} 6 L{x+xs3[1]:.1f} 104 M{x+70} 6 L{x+xs3[2]:.1f} 104" stroke="{NAVY}" stroke-width="3"/>')
    return f
body=h2('Count triangles: small ones first')+stitle('How many triangles are in this picture?')
body+=pin(128,310,420,base)
for k,(t,parts) in enumerate([('Made of 1 small part: 3',[(0,1),(1,2),(2,3)]),('Made of 2 small parts: 2',[(0,2),(1,3)]),('Made of all 3 parts: 1',[(0,3)])]):
    tt=thumbs(len(parts),tw_,th_,tri_th(parts),20,t)
    body+=pin(608,300+k*150,1184,f'<div style="display:flex;align-items:center;gap:24px"><p style="width:540px;flex:none;font-size:34px;font-weight:600;line-height:1.3"><span style="color:{TEAL};font-weight:800">Step {k+1}.</span>  {E(t)}</p>{tt}</div>','fade',WHITE,20,'14px 28px')
body+=answer(608,770,1128,'3 + 2 + 1 = 6 triangles')
put('l7-teachtri',sec('l7-teachtri','55–57 MIN',body,'Teach before worksheet page 2 (Q4 asks for the triangles in 3 pictures; this picture is not one of them). Ask first: "How many triangles?" Take guesses. Click through the sizes. Think-aloud: "I count the small triangles first: 1, 2, 3. Now triangles made of 2 small parts: the left two together, the right two together: 2. Then all 3 parts: the whole big triangle: 1. 3 + 2 + 1 = 6." Ask "Is the middle part with the right part a triangle?" Yes. Watch for children who stop after the small ones.'))

put('l7-ws2',ws_preview('l7-ws2','57–68 MIN','Worksheet page 2: on your own',[('Q3','Who am I? Cross out the shapes that do not fit each clue.'),('Q4','Count the triangles. Small ones first, then bigger ones.'),('Q5','Two same-size triangles, joined along one side. Draw one and name it.'),('Q6','How many squares can you find in the 2 by 2 grid? Small ones first, then the bigger one.')],'Finished early? Stretch and Challenge come next.','Children work alone. Note who needs a short catch-up next lesson. For Q5, children can use the two triangles they cut in Explore.'))
put('l7-ws2ans',check_slide('l7-ws2ans','68–70 MIN','Page 2: check together',[('Q3','a) square,   b) circle,   c) hexagon'),('Q4','A: 3,    B: 2,    C: 8  (4 small + 4 made of 2 small ones)'),('Q5','Any correct shape and its name: a square, a bigger triangle, a parallelogram or a rectangle'),('Q6','5 squares:  4 small + 1 big')],'Click each answer after a child explains. Q4A: 2 small + the whole triangle = 3. Q4B: the line from corner to corner makes 2 triangles; the square is not a triangle. Q4C: 4 small triangles meet in the middle; each line from corner to corner also cuts the square into 2 big triangles, and there are 2 such lines, so 4 big ones: 4 + 4 = 8. Q5: hold up the Explore shapes to check each drawing.'))

# ---------- stretch (new items) ----------
st=[('1.','How many squares are in a grid 3 squares long and 2 squares high?'),('2.','How many rectangles are in a grid 2 squares long and 2 squares high? (Squares count too.)'),('3.','Join 4 same-size squares, whole sides touching. How many different shapes can you make? (Turns and flips are the same shape.)')]
put('l7-stretch',sec('l7-stretch','For early finishers',h2('Stretch')+''.join(card(p(f'<span style="color:#1F7A6F">{a}</span>  {E(b)}',38,600,raw=True)) for a,b in st),'For children who finish early. Answers: 1) 8: 6 small squares + 2 squares made of 4 small ones (a 2 by 2 window fits in 2 places). 2) 9: 4 small squares, 2 rectangles 2 long lying down, 2 rectangles 2 long standing up, and the whole grid. 3) 5 shapes: a line of 4, a 2 by 2 square, an L, a T and a zigzag (S). Let children build them with paper squares and check each new one is not a turned or flipped copy.'))

# ---------- challenge walk-through ----------
body=h2('Challenge: walk-through')+pin(128,250,780,p('Q1: 4 lines make 5 small parts',38,800,TEAL))
for i,t in enumerate(['Made of 1 part: 5.   Made of 2 parts: 4','Made of 3 parts: 3.   Made of 4 parts: 2','Made of all 5 parts: 1','5 + 4 + 3 + 2 + 1 = 15 triangles ✓']): body+=pin(128,330+i*110,780,p(t,34),'rise',WHITE)
body+=pin(992,250,800,p('Q2: count each size',38,800,TEAL))
for i,t in enumerate(['The big square: 1','Medium squares (the 4 quarters): 4','Tiny squares in one quarter: 4','1 + 4 + 4 = 9 squares ✓']): body+=pin(992,330+i*110,800,p(t,34),'rise',WHITE)
put('l7-chwalk',sec('l7-chwalk','Challenge',body,'Use after pairs have tried. Q1: the same idea as the 2-line triangle we counted (3 + 2 + 1 = 6), now with 5 small parts. Children who know the pattern 3, 6, 10 can add the next jumps: 10 + 5 = 15. Ask: "Which triangles are made of 4 parts?" (the left 4 and the right 4). Q2: the quarter that is cut up still counts as a medium square. Watch for 8 (forgetting the big square) or 5 (forgetting the tiny ones).'))

# ---------- exit ticket (new: the old one repeated worksheet Q4B) ----------
eg=SV(372,372,gridb(6,6,3,3,120),'A grid 3 squares long and 3 squares high')
body=h2('Exit ticket')+card(chip('EXIT TICKET')+p('How many squares are in this grid? Count every size.',46,600)+eg)+card(p('Write your answer on a slip of paper. Show it to your tutor. Then collect your stamp in your inquiry journal.',34,400))
put('l7-exit',sec('l7-exit','80–90 MIN',body,'Minutes 80 to 90. Answer: 14 (9 small squares + 4 squares made of 4 small squares + 1 whole grid). This is the grid we counted in the worked example, so it checks the core idea. Children who write 9 counted only the small squares: ask "Are there any bigger squares hiding?" Extension: how many squares are in a grid 4 squares long and 2 squares high? (11: 8 + 3). Then 4 long and 3 high? (20: 12 + 6 + 2).'))


# ---------- aria-labels on the kept diagrams (pictures unchanged) ----------
def label_svgs(sid,labels):
    f=os.path.join(D,'slides',sid+'.html'); s=open(f).read(); parts=s.split('<svg ')
    for i,l in enumerate(labels):
        if i+1<len(parts) and not parts[i+1].startswith('aria-label'): parts[i+1]=f'aria-label="{l}" '+parts[i+1]
    open(f,'w').write('<svg '.join(parts))
label_svgs('l7-explore1',['Fold a square corner to corner and cut it into two same-size triangles'])
label_svgs('l7-chdiag',['A triangle with 4 lines from the top corner to the bottom','A square cut into 4 squares, with one of them cut into 4 smaller squares'])
# ---------- write ----------
for i,h in S.items(): open(os.path.join(D,'slides',i+'.html'),'w').write(h)
for old in ['l7-mini1','l7-mini2']:
    f=os.path.join(D,'slides',old+'.html')
    if os.path.exists(f): os.remove(f)
t=os.path.join(D,'slides','l7-title.html'); s=open(t).read(); s=s.replace('mini-lesson 25 to 35, brain break 35 to 40, worksheet 40 to 70','teaching 25 to 35 (click to reveal each step and answer), brain break 35 to 40, worksheet 40 to 70 with short teaching before each page and a check-together slide after it').replace('Describe shapes by their sides and corners, then count the triangles hiding in a picture.','Find every shape hiding in a picture by counting in order, describe shapes by sides and corners, and make new shapes from squares.'); open(t,'w').write(s)
deck=json.load(open(os.path.join(D,'deck.json')))
deck['order']=['l7-title','l7-warm1','l7-warm2','l7-explore1','l7-explore2','l7-teach1','l7-we1','l7-try1','l7-key','l7-break','l7-teachpic','l7-teachsides','l7-ws1','l7-ws1ans','l7-teachwho','l7-teachtri','l7-ws2','l7-ws2ans','l7-stretch','l7-we2','l7-try2','l7-we3','l7-challenge','l7-chdiag','l7-chwalk','l7-talk','l7-exit']
deck['sections']={'s1':{'description':'Warm-up and explore','start':'l7-title'},'s2':{'description':'Teach: count shapes in order, and make shapes from squares','start':'l7-teach1'},'s3':{'description':'Worksheet with teaching before each page','start':'l7-break'},'s4':{'description':'Stretch, challenge, talk and exit','start':'l7-stretch'}}
json.dump(deck,open(os.path.join(D,'deck.json'),'w'),indent=1,ensure_ascii=False)
missing=[i for i in deck['order'] if not os.path.exists(os.path.join(D,'slides',i+'.html'))]
print(len(deck['order']),'slides; wrote',len(S),'missing',missing)

import p1fix
p1fix.finish(D,7,{'l7-teach1':'25–28 MIN','l7-we1':'28–31 MIN','l7-try1':'31–34 MIN','l7-teachtri':'55–58 MIN','l7-ws2':'58–68 MIN'},optional=('stretch','challenge','chdiag','chwalk','we2','try2','we3'))
