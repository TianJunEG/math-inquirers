"""Math Inquirers P5, Lesson 4: Triangle Areas. Writes split/p5l4/project (deck.json + slides/*.html). All figures are to scale."""
from p5l34_common import *
L='p5l4'; S={}
def put(i,h): S[f'{L}-{i}']=h
C=load(4); LS=C['lesson']; DK=C['deck']
GRN='#BFE3DC'
def Mp(ox,oy,s): return lambda x,y:(ox+x*s,oy-y*s)
def lab(x,y,t,size=30,fill=NAVY,anchor='middle',weight=700): return txt(x,y,t,size,fill,anchor,weight,'Nunito Sans, Arial')
def ra(f,dx,dy,k=16): return f'<path d="M{f[0]+dx*k:.1f} {f[1]:.1f} V{f[1]+dy*k:.1f} H{f[0]:.1f}" fill="none" stroke="{NAVY}" stroke-width="3"/>'
def card_svg(sid_w,h,label,inner): return svgwrap(sid_w,h,label,inner)

# ---- title ----
put('title',title_slide(f'{L}-title','LESSON 4  •  WEEK 2','Triangle Areas','Area of a triangle',DK['today'],
 'Objective: '+LS['objective']+' Thinking strategies today: FIND THE BASE AND ITS HEIGHT, SAME BASE AND SAME HEIGHT, and SPLIT OR TAKE AWAY. Materials: '+LS['materials']+' Online: '+LS['online']+
 ' Time plan: warm-up 0 to 10, explore 10 to 25, teaching 25 to 35 (click to reveal each step and answer), brain break 35 to 40, worksheet 40 to 70 with short teaching before each page and a check-together slide after it, challenge for early finishers from 65, talk time 70 to 80, exit ticket 80 to 90.'))

# ---- warm-up: half or not ----
s=36; g=''
for k,(tip,fill) in enumerate([((12,8),YEL),((4,8),YEL),((12,4),YEL)]):
    ox=30+k*(12*s+110); P=Mp(ox,300,s)
    g+=poly([P(0,0),P(12,0),P(12,8),P(0,8)],WHITE)
    if k==0: tri=[P(0,0),P(12,0),P(12,8)]
    elif k==1: tri=[P(0,0),P(12,0),P(4,8)]
    else: tri=[P(0,0),P(12,0),P(12,4)]
    g+=poly(tri,fill)+lab(ox+6*s,345,['Rectangle 1','Rectangle 2','Rectangle 3'][k],30,TEAL)
body=h2('Warm-up: Half or not?')+card(p('Each rectangle has one shaded triangle. Is the shaded triangle exactly HALF of the rectangle? Vote: thumbs up or thumbs down.',36,700))
body+=pin(128,350,1664,svgwrap(1580,360,'Three 12 by 8 rectangles. Rectangle 1: the triangle is cut off by a diagonal. Rectangle 2: the top corner of the triangle is on the top side. Rectangle 3: the triangle has its corner in the middle of the right side.',g),None,WHITE,24,'14px 30px')
for k,t in enumerate(['Half: it is cut by a diagonal','Half: same base, same height','Not half: only 1/4']):
    body+=pin(128+k*572,770,520,p(t,32,800),'pop',YEL,20,'16px 22px')
put('warm1',sec(f'{L}-warm1','0–5 MIN',body,'Minutes 0 to 5. Half or not? Children vote with thumbs for each rectangle before you click. Answers: Rectangle 1 is half (a diagonal cuts a rectangle into two equal triangles). Rectangle 2 is half too: the top corner is on the top side, so the triangle has the whole bottom side as its base and the whole height of the rectangle as its height. Many children say no because the picture looks "pointy"; do not explain yet, collect reasons. Rectangle 3 is NOT half: the corner of the triangle is in the middle of the right side, so the triangle is 1/4 of the rectangle (base 12 cm, height 4 cm; 1/2 × 12 × 4 = 24 cm² out of 96 cm²). Say: "Hold on to your reasons. We will explain why."'))
qs=DK['warmQs']
body=h2('Quick questions')+''.join(qrow(128,240+i*125,1250,f'{i+1}.',a,36) for i,(a,b) in enumerate(qs))+''.join(answer(1420,240+i*125,372,b) for i,(a,b) in enumerate(qs))
put('warm2',sec(f'{L}-warm2','5–10 MIN',body,'Minutes 5 to 10. Whiteboards: read each question aloud, give thinking time, hold up boards together, then click. Answers: 1) 42 cm² (7 × 6).  2) 21 cm² (half of 42).  3) 18 (9 × 4 = 36, half is 18).  4) 7 cm (7 × 7 = 49).  5) 60 (15 × 8 = 120, half is 60). Ask after 3: "What are we really doing when we halve? A triangle is half of a rectangle: which rectangle?" Listen for "the base times the height".'))

# ---- explore ----
s=34; P=Mp(60,170,s); g=''
for i in range(9): g+=line(P(i,0),P(i,6),2,False,'#9FB3D1')
for j in range(7): g+=line(P(0,j),P(8,j),2,False,'#9FB3D1')
g+=poly([P(0,0),P(2,6),P(0,6)],SKY)+poly([P(2,6),P(8,0),P(8,6)],SKY)+poly([P(0,0),P(8,0),P(2,6)],YEL)+poly([P(0,0),P(8,0),P(8,6),P(0,6)],'none',5)
g+=lab(P(2,6)[0],P(2,6)[1]-12,'any point',28,TEAL)+lab(P(4,0)[0],P(0,0)[1]+36,'8 cm',28)+lab(P(0,3)[0]-14,P(0,3)[1]+10,'6 cm',28,NAVY,'end')
g+=lab(520,60,'Join the point to the two',28,TEAL,'start')+lab(520,96,'bottom corners. Cut out the',28,TEAL,'start')+lab(520,132,'3 pieces and compare.',28,TEAL,'start')
steps=''.join(f'<li>{E(x)}</li>' for x in DK['expSetup'])
body=h2('Explore: what to do')+card(chip('EXPLORE')+f'<ol style="font-size:34px;font-weight:600;padding-left:52px;display:flex;flex-direction:column;gap:6px">{steps}</ol>')
body+=card(svgwrap(980,210,'A rectangle 8 cm by 6 cm on a grid with a point on the top side joined to the two bottom corners; the middle triangle is yellow and the two corner pieces are blue',g),extra='padding:12px 32px')
put('explore1',sec(f'{L}-explore1','10–15 MIN',body,'Minutes 10 to 15. Pairs draw the rectangle on grid paper (cut-out page at the back of the workbook) and cut out the three pieces (online: camera pointing down at the desk). Predict first: what fraction of the rectangle is the triangle? Does it matter where the point is? Early finishers: put the point at the end of the top side. What kind of triangle is it now? Is it still half? (Yes: a right-angled triangle, half of the rectangle.)'))
body=h2('Explore: talk about it')+numcards([('1.',DK['expAsk'][0][0]),('2.',DK['expAsk'][1][0]),('3.',DK['expAsk'][2][0])],40)
put('explore2',sec(f'{L}-explore2','15–25 MIN',body,'Minutes 15 to 25. Gather the pairs. Hold up the pieces on camera: the two blue pieces fit exactly on the yellow triangle. Answers: 1) Yes. Each blue piece is half of a smaller rectangle (cut it along the dashed line from the point down), so together the blue pieces equal the triangle. 2) 24 cm²: the rectangle is 8 × 6 = 48 cm² and the triangle is half. 3) No: the base is always 8 cm and the height is always 6 cm, wherever the point is. Do NOT name the formula yet if nobody finds it; the next slide does.'))

# ---- teach 1: right-angled triangle ----
s=24; P=Mp(50,250,s)
def fig_right(extra=''):
    g=poly([P(0,0),P(12,0),P(0,5)],YEL)+ra(P(0,0),1,-1)+lab(P(6,0)[0],P(0,0)[1]+40,'base 12 cm',30)+lab(P(0,2.5)[0]-12,P(0,2.5)[1]+10,'height 5 cm',30,TEAL,'end')+lab(P(6,2.5)[0]+36,P(6,2.5)[1]-22,'13 cm',30,NAVY,'start')
    return g+extra
A=svgwrap(560,290,'A right-angled triangle with a base of 12 cm, a height of 5 cm and a slanting side of 13 cm',fig_right())
ext=poly([P(0,5),P(12,5),P(12,0)],'#FFFFFF',3,True)
B=svgwrap(560,290,'The same triangle with a second copy turned over to make a rectangle 12 cm by 5 cm',fig_right(ext).replace(poly([P(0,0),P(12,0),P(0,5)],YEL),poly([P(0,0),P(12,0),P(0,5)],YEL)))
body=h2('Area of a triangle: 1/2 × base × height',62)+card(p('A right-angled triangle has sides of 5 cm, 12 cm and 13 cm. What is its area?',38,700))
body+=pin(128,370,700,A,None,WHITE,24,'12px 20px')+pin(128,370,700,B,'fade',WHITE,24,'12px 20px')
body+=step(1,'Find the square corner. The two sides that make it are the base (12 cm) and the height (5 cm).',left=900,top=370,width=892,size=32)
body+=step(2,'The 13 cm side is slanting. It is not a height, so we do not use it.',left=900,top=530,width=892,size=32)
body+=step(3,'Area = 1/2 × 12 × 5 = 30 cm². Two of these triangles make a 12 by 5 rectangle: 60 cm².',left=900,top=670,width=892,size=32)
put('teach1',sec(f'{L}-teach1','25–28 MIN',body,'Teach. Ask first: "Which length is the height?" Let children argue; then show the square corner. Click order: step 1, step 2, step 3 (the dashed copy makes the rectangle). Think-aloud: "The height must meet the base at a right angle. Here the square corner tells me: 12 is the base and 5 is the height. 13 leans over, so it is not a height. Half of base times height: half of 60 is 30." Link back to the explore: the triangle is half of the rectangle 12 by 5. Common error: using 13 as the height (1/2 × 12 × 13 = 78: wrong).'))
put('try1',try_slide(f'{L}-try1','28–29 MIN','Your turn: whiteboards','Write the area. Remember the 1/2.',[
 ('a','A triangle has a base of 10 cm and a height of 7 cm.','35 cm²'),
 ('b','A triangle has a base of 9 cm and a height of 12 cm. Its slanting sides are 15 cm and 20 cm.','54 cm²'),
 ('c','A triangle has an area of 40 cm² and a base of 8 cm. What is its height?','10 cm')],
 'Whiteboards. a) 1/2 × 10 × 7 = 35. b) 1/2 × 9 × 12 = 54; 15 and 20 are the slanting sides. c) 1/2 × 8 × height = 40, so 4 × height = 40, height = 10 (work backwards: double 40 is 80, and 80 ÷ 8 = 10).',size=34))

# ---- teach 2: height outside ----
s=20; P=Mp(40,230,s)
def fig_out(ext):
    g=poly([P(0,0),P(11,0),P(16,12)],YEL)+lab(P(5.5,0)[0],P(0,0)[1]+40,'base 11 cm',30)+lab(P(7.5,7)[0]-4,P(7.5,7)[1]-8,'20 cm',30,NAVY,'end')+lab(P(13.8,6)[0]+4,P(13.8,6)[1]+14,'13 cm',30,NAVY,'start')
    if ext: g=line(P(11,0),P(16,0),3,True)+line(P(16,12),P(16,0),3,True,TEAL)+ra(P(16,0),-1,-1)+g+lab(P(16,6)[0]+10,P(16,6)[1]+10,'12 cm',30,TEAL,'start')
    return g
A=svgwrap(540,290,'A triangle with base 11 cm whose top corner is past the end of the base; its slanting sides are 20 cm and 13 cm',fig_out(False))
B=svgwrap(540,290,'The same triangle with the base extended by a dashed line and the height of 12 cm drawn from the top corner down to it',fig_out(True))
body=h2('The height can be OUTSIDE the triangle',62)+card(p('The base is 11 cm. The top corner is past the end of the base. The height is 12 cm. What is the area?',38,700))
body+=pin(128,370,700,A,None,WHITE,24,'12px 20px')
body+=step(1,'The top corner is past the end of the base. Extend the base with a dashed line.',left=900,top=370,width=892,size=32)
body+=pin(128,370,700,B,'fade',WHITE,24,'12px 20px')
body+=step(2,'Drop the height from the top corner to the dashed line at a right angle: 12 cm.',left=900,top=500,width=892,size=32)
body+=step(3,'The base is still 11 cm. The dashed part is NOT part of the triangle.',left=900,top=630,width=892,size=32)
body+=answer(900,760,892,'1/2 × 11 × 12 = 66 cm²')
put('teach2',sec(f'{L}-teach2','28–31 MIN',body,'Teach. Ask: "Where is the height now? There is no square corner inside the triangle." Click order: step 1, the dashed extension and the height appear, steps 2 and 3, the answer. Think-aloud: "A height does not have to be inside. I extend the base with a dashed line, then draw a line from the top corner straight down to it, at a right angle. That is the height: 12 cm. But the base is only the 11 cm side. The area is half of 11 times 12: 66 cm². The 13 cm and 20 cm sides are not needed." Show it with a paper triangle leaning over. Common mistake: using the base plus the dashed part (16 cm).'))
# same base, same height
s=26; g=''
for k,(tx,fill) in enumerate([(2,YEL),(7,SKY),(12,GRN)]):
    ox=40+k*(14*s+60); P=Mp(ox,260,s)
    g+=poly([P(0,0),P(14,0),P(14,9),P(0,9)],WHITE,3)+poly([P(0,0),P(14,0),P(tx,9)],fill)+line(P(tx,9),P(tx,0),3,True,TEAL)
g+=lab(40+7*s,298,'14 cm',28)+lab(40+14*s+60+14*s+60+14*s+8,142,'9 cm',28,TEAL,'start')
body=h2('Same base, same height: same area',62)+card(p('Three triangles stand on the bottom side of a 14 cm by 9 cm rectangle. Their top corners are at different points on the top side. What is the area of each?',36,700))
body+=pin(128,380,1664,svgwrap(1300,310,'Three 14 by 9 rectangles. In each, a triangle has the bottom side as its base and its top corner at a different point on the top side, with the height of 9 cm drawn as a dashed line.',g),None,WHITE,24,'12px 30px')
body+=step(1,'Each has base 14 cm and height 9 cm: 1/2 × 14 × 9 = 63 cm² for ALL three.',top=740,size=34)
body+=pin(128,840,1664,p('Same base and same height means the same area, however far the triangle leans.',34,800),'fade',SOFT,20,'16px 30px')
put('teach3',sec(f'{L}-teach3','31–33 MIN',body,'Teach. Ask first: "Do the three triangles have the same area? They look different." Collect opinions, then click. Think-aloud: "Look at the dashed height in each: it is 9 cm every time, because the top corner is on the top side, which is 9 cm above the bottom side. The base is the same 14 cm. So 63 cm² each, half of the rectangle." Connect to the warm-up: Rectangle 2 was half because it was this exact situation. Ask: "What if the top corner is at the very end of the top side?" (a right-angled triangle, still 63.) And: "What if it moves beyond the rectangle, along the same top line?" (the height is still 9 cm: still 63).'))
put('try2',try_slide(f'{L}-try2','33–34 MIN','Your turn: same area?','Work out base × height first.',[
 ('a','Triangle P: base 6 cm, height 10 cm. Triangle Q: base 12 cm, height 5 cm. Same area?','Yes: 30 and 30'),
 ('b','A rectangle is 8 cm by 5 cm. A triangle uses the 8 cm side as its base and its top corner on the opposite side. Area?','20 cm²'),
 ('c','Triangle R has base 10 cm and area 40 cm². What is its height?','8 cm')],
 'Whiteboards. a) 1/2 × 6 × 10 = 30 and 1/2 × 12 × 5 = 30: the same area, although the shapes are very different. b) Half of 8 × 5 = 40, so 20 cm². c) 1/2 × 10 × height = 40, so 5 × height = 40 and the height is 8 cm.',size=34))
body=h2('Key idea: 1/2 × base × height')+card(p('Area of a triangle = 1/2 × base × height. The height meets the base at a right angle, even when it is outside the triangle.',42,700))+card(p('Same base and same height: same area, whatever the shape. Slanting sides are not needed.',38,600,MUTED))
put('key',sec(f'{L}-key','34–35 MIN',body,'Say the key idea together. Common mistakes to watch for during the worksheet: (1) '+LS['mistakes'][0]+' (2) '+LS['mistakes'][1]+' (3) '+LS['mistakes'][2]))
put('break',break_slide(f'{L}-break','35–40 MIN',DK['brk'],'Five minutes. Online: children stand in view of the camera. Make a triangle with both arms above the head. Make a right angle with one arm. Then lean the triangle left and right: the height does not change. Then a drink of water.'))

# ---- worksheet 1 ----
put('ws1',ws_preview(f'{L}-ws1','40–52 MIN','Worksheet page 1: with your partner',[('Q1','Three triangles. Find the base and the height, then the area.'),('Q2','Triangles in a rectangle: P and Q are points on AB.')],'Stuck? Find the square corner or the dashed height first.','Minutes 40 to 52. Walk around. Ask "Which line is the height? How do you know?" before giving any help. Q1b: children often use 13 or 15 as the height; point to the dashed line. Q1c: the height is OUTSIDE the triangle and the base is only 9 cm (the dashed part is not in the triangle).'))
put('ws1ans',checks(f'{L}-ws1ans','52–54 MIN','Page 1: check together',[('Q1','a) 24 cm²   b) 84 cm²   c) 36 cm²   d) 13 cm and 15 cm: slanting sides'),('Q2','a) 30 cm²   b) 30 cm²   c) Same base DC = 10 cm and same height 6 cm')],
 'Click each answer after a pair explains theirs. Q1a: 1/2 × 8 × 6 = 24 (the 10 cm side is slanting). Q1b: 1/2 × 14 × 12 = 84. Q1c: 1/2 × 9 × 8 = 36 (the 17 cm side is not needed). Q2: P and Q are on AB, which is 6 cm above DC, so both triangles have base 10 cm and height 6 cm. Each is half of the 60 cm² rectangle.',gapy=170))

# ---- teach: split ----
s=28; P=Mp(60,160,s)
def fig_split(extra=''):
    g=poly([P(0,0),P(3,4),P(10,0),P(7,-6)],SKY)+line(P(0,0),P(10,0),4)+line(P(3,4),P(3,0),3,True,TEAL)+ra(P(3,0),1,-1,14)+line(P(7,-6),P(7,0),3,True,TEAL)+ra(P(7,0),1,1,14)
    g+=lab(P(0,0)[0]-16,P(0,0)[1]+10,'A',30,NAVY,'end')+lab(P(3,4)[0],P(3,4)[1]-14,'B',30)+lab(P(10,0)[0]+16,P(10,0)[1]+10,'C',30,NAVY,'start')+lab(P(7,-6)[0],P(7,-6)[1]+36,'D',30)
    g+=lab(P(3,2)[0]+10,P(3,2)[1]+10,'4 cm',28,TEAL,'start')+lab(P(7,-3)[0]+10,P(7,-3)[1]+10,'6 cm',28,TEAL,'start')+lab(P(5,0)[0],P(5,0)[1]-12,'AC = 10 cm',28,NAVY)
    return g
body=h2('Split a figure into triangles',62)+card(p('ABCD has a diagonal AC of 10 cm. The height from B to AC is 4 cm and the height from D to AC is 6 cm. What is its area?',34,700))
body+=pin(128,370,700,svgwrap(660,350,'Four-sided figure ABCD with diagonal AC of 10 cm; the height from B is 4 cm and the height from D is 6 cm',fig_split()),None,WHITE,24,'12px 20px')
body+=step(1,'The diagonal AC is the base of BOTH triangles: ABC and ACD.',left=900,top=370,width=892,size=32)
body+=step(2,'ABC = 1/2 × 10 × 4 = 20 cm².   ACD = 1/2 × 10 × 6 = 30 cm².',left=900,top=500,width=892,size=32)
body+=step(3,'Add the two parts: 20 + 30 = 50 cm².',left=900,top=630,width=892,size=32)
put('teachsplit',sec(f'{L}-teachsplit','54–56 MIN',body,'Teach before worksheet page 2 (Q3). Ask: "How can we cut this figure into triangles we know?" Click: the diagonal is already there. Think-aloud: "AC is shared. Above it, triangle ABC has height 4 cm; below it, triangle ACD has height 6 cm. I find each area and add. I could also say: the two heights together make 10 cm, so the area is 1/2 × 10 × (4 + 6) = 50." Mention the second way only if children find it; check that it gives the same answer.'))
# ---- teach: take away ----
s=40; P=Mp(70,260,s)
g=poly([P(0,0),P(10,0),P(10,6),P(0,6)],WHITE,3)+poly([P(0,0),P(6,6),P(10,4)],YEL)
g+=lab(P(0,6)[0]-14,P(0,6)[1]-8,'A',30,NAVY,'end')+lab(P(10,6)[0]+14,P(10,6)[1]-8,'B',30,NAVY,'start')+lab(P(10,0)[0]+14,P(10,0)[1]+30,'C',30,NAVY,'start')+lab(P(0,0)[0]-14,P(0,0)[1]+30,'D',30,NAVY,'end')+lab(P(6,6)[0],P(6,6)[1]-14,'E',30)+lab(P(10,4)[0]+14,P(10,4)[1]+10,'F',30,NAVY,'start')
g+=lab(P(3,6)[0],P(3,6)[1]-48,'AE = 6 cm',26,TEAL)+lab(P(8,6)[0],P(8,6)[1]-48,'EB = 4 cm',26,TEAL)+lab(P(10,5)[0]+60,P(10,5)[1]+8,'BF = 2 cm',26,TEAL,'start')
body=h2('Take away the white triangles',62)+card(p('ABCD is a rectangle 10 cm by 6 cm. E is on AB with AE = 6 cm. F is on BC with BF = 2 cm. What is the area of the shaded triangle DEF?',34,700))
body+=pin(128,370,700,svgwrap(660,330,'Rectangle ABCD, 10 cm by 6 cm. E is on AB with AE 6 cm and EB 4 cm. F is on BC with BF 2 cm and FC 4 cm. Triangle DEF is shaded.',g.replace('V','V')),None,WHITE,24,'12px 20px')
body+=step(1,'Rectangle: 10 × 6 = 60 cm².',left=900,top=370,width=892,size=32)
body+=step(2,'White: ADE = 1/2 × 6 × 6 = 18,  EBF = 1/2 × 4 × 2 = 4,  FCD = 1/2 × 4 × 10 = 20.',left=900,top=470,width=892,size=32)
body+=step(3,'Shaded = 60 − 18 − 4 − 20 = 18 cm².',left=900,top=620,width=892,size=32)
put('teachtake',sec(f'{L}-teachtake','56–58 MIN',body,'Teach before worksheet page 2 (Q4). Ask: "The shaded triangle has no square corner and no side along the rectangle. Can we find its base and height directly?" (Hard.) "What do we know? The three white triangles each have a square corner." Click through. Think-aloud: "I find the whole rectangle, then take away the three white triangles, each with a right angle at a corner of the rectangle." Check: 18 + 18 + 4 + 20 = 60. Common error: forgetting one of the three white triangles.'))
# ---- teach: same area different triangles ----
s=17; g=''
for k,(b,h) in enumerate([(10,6),(12,5),(15,4)]):
    ox=40+[0,230,480][k]; P=Mp(ox,150,s)
    g+=poly([P(0,0),P(b,0),P(b*0.25,h)],[YEL,SKY,GRN][k],3)+lab(P(b/2,0)[0],P(0,0)[1]+30,f'{b} × {h}',26,NAVY)
body=h2('Same area, different triangles',62)+card(p('A triangle has an area of 30 cm². What could its base and height be?',38,700))
body+=step(1,'Area 30 cm², so base × height = 60 (double 30).',top=330,width=1664,size=34)
body+=step(2,'List pairs that multiply to 60: base 10, height 6;  base 12, height 5;  base 15, height 4;  and more.',top=430,width=1664,size=34)
body+=pin(128,560,1664,svgwrap(740,190,'Three triangles with base and height 10 by 6, 12 by 5 and 15 by 4. Each has an area of 30 square centimetres.',g),'fade',WHITE,24,'12px 30px')
body+=pin(128,790,1664,p('Check: 1/2 × 10 × 6 = 30,  1/2 × 12 × 5 = 30,  1/2 × 15 × 4 = 30 ✓',34,800),'fade',SOFT,20,'16px 30px')
put('teachsame',sec(f'{L}-teachsame','58–60 MIN',body,'Teach before worksheet page 2 (Q5, a triangle of 24 cm² with a base of 12 cm). Think-aloud: "The area is half of base times height, so base times height is DOUBLE the area: 60. Now I need two numbers that multiply to 60, and I can list them in order: 1 and 60, 2 and 30, 3 and 20, 4 and 15, 5 and 12, 6 and 10." On the worksheet they use the same idea with a different area. All the triangles lean in different ways but share the same area: link to same base and same height.'))
put('ws2',ws_preview(f'{L}-ws2','60–67 MIN','Worksheet page 2: on your own',[('Q3','Split the figure along the diagonal AC.'),('Q4','Rectangle with a shaded triangle: take away three white triangles.'),('Q5','Same area, different triangles.')],'Finished early? Stretch and Challenge come next.','Children work alone. Note who needs a short catch-up next lesson, especially children who give the area of a rectangle by forgetting the 1/2.'))
put('ws2ans',checks(f'{L}-ws2ans','67–69 MIN','Page 2: check together',[('Q3','56 cm²   (35 + 21)'),('Q4','a) 96   b) 16, 16, 24   c) 40 cm²'),('Q5','a) 24 cm²   b) 4 cm   c) base × height = 48, e.g. 16 and 3')],
 'Click after a child explains. Q3: ABC = 1/2 × 14 × 5 = 35 and ACD = 1/2 × 14 × 3 = 21; 35 + 21 = 56. Q4: rectangle 12 × 8 = 96; ADE = 1/2 × 4 × 8 = 16; EBF = 1/2 × 8 × 4 = 16; FCD = 1/2 × 4 × 12 = 24; 96 − 16 − 16 − 24 = 40. Q5: 1/2 × 8 × 6 = 24; 1/2 × 12 × height = 24 gives height 4 (check: 1/2 × 12 × 4 = 24); any pair with base × height = 48, such as 6 and 8, 16 and 3, 24 and 2.',gapy=170))

# ---- stretch / challenge ----
st=[('1.','A right-angled triangle has sides of 6 cm, 8 cm and 10 cm. What is the height when the 10 cm side is the base?'),('2.','ABCD is a rectangle 14 cm by 6 cm. P is any point on AB. What is the area of triangle PDC? What is the total area of the other two triangles?'),('3.','A triangle has a base of 8 cm and a height of 5 cm. What is its area? What is the area if the base is doubled? If both the base and the height are doubled?')]
put('stretch',sec(f'{L}-stretch','For early finishers',h2('Stretch')+numcards(st,34),'Answers: 1) 4.8 cm (area = 1/2 × 6 × 8 = 24 cm²; 1/2 × 10 × height = 24, so height = 24 × 2 ÷ 10 = 4.8). 2) Triangle PDC = 1/2 × 14 × 6 = 42 cm² (half of 84); the other two triangles together are 42 cm². 3) 20 cm²; 40 cm² (twice as big); 80 cm² (four times as big).'))
ch=[('1.','ABCD is a rectangle with AB = 12 cm and BC = 10 cm. M is the middle of BC. N is the middle of CD. What is the area of triangle AMN?'),('2.','PQRS joins the middle points of the sides of a square of side 10 cm. What is the area of PQRS?')]
put('challenge',sec(f'{L}-challenge','65–80 MIN',h2('Challenge')+numcards(ch,36),'Pairs try first, then use the "see it" slide if stuck, then the walk-through. These are NOT on the workbook. Answers: 1) 45 cm² (rectangle 120; white triangles ABM 30, MCN 15, NDA 30; 120 − 75 = 45). 2) 50 cm² (square 100; four white corner triangles of 12.5 each make 50; PQRS is half of the square).'))
s=26; P=Mp(30,300,s)
g1=poly([P(0,0),P(12,0),P(12,10),P(0,10)],WHITE,3)+poly([P(0,0),P(12,5),P(6,10)],YEL,3)
g1+=lab(P(0,0)[0]-12,P(0,0)[1]+28,'A',28,NAVY,'end')+lab(P(12,0)[0]+12,P(12,0)[1]+28,'B',28,NAVY,'start')+lab(P(12,10)[0]+12,P(12,10)[1]-6,'C',28,NAVY,'start')+lab(P(0,10)[0]-12,P(0,10)[1]-6,'D',28,NAVY,'end')+lab(P(12,5)[0]+14,P(12,5)[1]+10,'M',28,NAVY,'start')+lab(P(6,10)[0],P(6,10)[1]-14,'N',28)
g1+=lab(P(6,0)[0],P(0,0)[1]+30,'AB = 12 cm',26,TEAL)+lab(P(0,5)[0]-14,P(0,5)[1]+10,'BC = 10 cm',26,TEAL,'end')
P=Mp(40,250,22)
g2=poly([P(0,0),P(10,0),P(10,10),P(0,10)],WHITE,3)+poly([P(5,0),P(10,5),P(5,10),P(0,5)],YEL,3)
g2+=lab(P(5,0)[0],P(5,0)[1]+30,'P',28)+lab(P(10,5)[0]+14,P(10,5)[1]+10,'Q',28,NAVY,'start')+lab(P(5,10)[0],P(5,10)[1]-12,'R',28)+lab(P(0,5)[0]-14,P(0,5)[1]+10,'S',28,NAVY,'end')+lab(P(5,0)[0]+110,P(0,0)[1]+30,'side 10 cm',26,TEAL)
body=h2('Challenge: see it',60)+'<div style="display:flex;gap:32px;align-items:flex-start">'
body+=card(f'<p style="font-size:30px;font-weight:700;color:{TEAL}">Q1: Rectangle and triangle AMN</p>'+svgwrap(500,340,'Rectangle ABCD 12 cm by 10 cm with M the middle of BC and N the middle of CD; triangle AMN is shaded',g1,True),extra='flex:1;min-width:0;padding:20px 24px')
body+=card(f'<p style="font-size:30px;font-weight:700;color:{TEAL}">Q2: Joining the middle points</p>'+svgwrap(360,330,'A square of side 10 cm with the middle points of the four sides joined to make a tilted square PQRS',g2,True),extra='flex:1;min-width:0;padding:20px 24px')+'</div>'
put('chdiag',sec(f'{L}-chdiag','65–80 MIN',body,'Show after pairs have tried the Challenge, or if they are stuck. The pictures show the problem, not the answer. Ask: What do you notice? Which triangles have a square corner? Can you find the area of the shaded part by taking away? What do you know about the four corner triangles in Q2? Answers are in the Challenge slide notes.'))
body=h2('Challenge: walk-through')+pin(128,250,800,p('Q1: box it, take away',38,800,TEAL))
r1=['Rectangle: 12 × 10 = 120 cm².','ABM = 1/2 × 12 × 5 = 30.   MCN = 1/2 × 5 × 6 = 15.','NDA = 1/2 × 6 × 10 = 30.   White total: 75.','AMN = 120 − 75 = 45 cm² ✓']
r2=['Square: 10 × 10 = 100 cm².','Four corner triangles, each 1/2 × 5 × 5 = 12.5.','4 × 12.5 = 50 white.','PQRS = 100 − 50 = 50 cm²: half the square ✓']
for i,t in enumerate(r1): body+=pin(128,330+i*120,800,p(t,32),'rise',WHITE)
body+=pin(992,250,800,p('Q2: the same idea',38,800,TEAL))
for i,t in enumerate(r2): body+=pin(992,330+i*120,800,p(t,32),'rise',WHITE)
put('chwalk',sec(f'{L}-chwalk','Challenge',body,'Use after pairs have tried. Q1: M and N are middle points, so MC = 5, CN = 6, DN = 6. Each white triangle has a square corner at a corner of the rectangle. Check: 30 + 15 + 30 + 45 = 120 ✓. Q2: each corner triangle has two sides of 5 cm at a right angle; a second way to see Q2 is to cut the square along the diagonals of PQRS: PQRS is made of 4 triangles that are the same as the corner ones, so PQRS is exactly half.'))
body=h2('Talk time')+card(chip('TALK TIME',YEL,NAVY)+p(LS['share'],42,600))+card(p('Sentence starters:',34,400,MUTED)+p('“The base is … and the height is …”   “They have the same … so …”',38,600))
put('talk',sec(f'{L}-talk','70–80 MIN',body,'Minutes 70 to 80. Pairs talk for 2 minutes, then share. Answer: No. Two triangles with the same base and the same height have the same area, even if one leans over and has much longer sides. The area depends on the base and the height, not on the slanting sides. A long, thin triangle can have a smaller area than a short, wide one. Ask: "Can you draw a triangle with one very long side and a tiny area?" (Yes: a long base with a tiny height.) Praise reasons, not only answers.'))
body=h2('Exit ticket')+card(chip('EXIT TICKET')+p(LS['exit']['q'],46,600))+card(p('Write your answer on a slip of paper. Show it to your tutor. Then collect your stamp in your inquiry journal.',34,400))
put('exit',sec(f'{L}-exit','80–90 MIN',body,'Minutes 80 to 90. Answer: '+LS['exit']['a']+' Extension: '+LS['extension']))

order=[f'{L}-{x}' for x in ['title','warm1','warm2','explore1','explore2','teach1','try1','teach2','teach3','try2','key','break','ws1','ws1ans','teachsplit','teachtake','teachsame','ws2','ws2ans','stretch','challenge','chdiag','chwalk','talk','exit']]
sections={'s1':{'description':'Warm-up and explore','start':f'{L}-title'},'s2':{'description':'Teach: base and height, same base same height','start':f'{L}-teach1'},'s3':{'description':'Worksheet with teaching before each page','start':f'{L}-break'},'s4':{'description':'Stretch, challenge, talk and exit','start':f'{L}-stretch'}}
write_deck(L,order,sections,S,'Math Inquirers P5: Lesson 4 – Triangle Areas')
