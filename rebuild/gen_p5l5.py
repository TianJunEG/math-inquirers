"""Math Inquirers P5, Lesson 5: Volume Vault. Writes split/p5l5/project (deck.json + slides/*.html)."""
import os,sys
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,H)
from p5l56_common import *
P='p5l5'
D=os.path.join(H,'..','split',P,'project'); S={}
def put(i,h): S[f'{P}-{i}']=h
def sid(i): return f'{P}-{i}'

# ---------- 1. title ----------
put('title',title_slide(sid('title'),'LESSON 5  •  WEEK 3','Volume Vault','Volume',
 'Count cubes in layers, list every cuboid from a number of cubes, and solve tank puzzles: litres, water levels and stones that make the water rise.',
 'Objective: Find the volume of a cuboid by counting layers of 1-cm cubes and by length x breadth x height; list every cuboid that can be built from a number of cubes; solve water-tank problems (cm3 and litres, new water levels, the rise when an object sinks, pouring from one tank into another); and count the painted faces of a cube cut into small cubes. '
 'Thinking strategies taught today: MAKE A LIST IN ORDER, DRAW IT TO SCALE and WORK BACKWARDS from a water level. '
 'Materials: about 30 one-centimetre cubes (or dice, Lego bricks, sugar cubes) per pair, a ruler, squared paper, mini whiteboards. Tutor: a clear plastic box with a ruler taped to its side, water and a stone for the demonstration. '
 'Online: show the water rise live on camera (clear box, ruler on the side, drop in a stone). Children use dice or Lego for the Explore; with no cubes they draw layers on squared paper. '
 'Time plan: sneak-peek puzzles 0 to 3 (private answers, nobody is marked), warm-up 3 to 9, explore 9 to 21 (a Go further what-if is on the explore slide for anyone who wants more), teaching 21 to 33 (click to reveal each step and answer), brain break 33 to 37, workbook page 1 37 to 49 (after question 3 you may choose: carry on, or try Think harder), check together 49 to 53, short teaching before page 2 53 to 58, workbook page 2 58 to 72 (alone: start with the questions named at the top, then choose; nobody has to finish), check together 72 to 76, talk time 76 to 82 (you may say pass; volunteers first; then everyone tries the first step of the Investigation), exit ticket 82 to 86, reflection 86 to 88 (pass is always OK), stamp and goodbye 88 to 90. Think harder, Go further and the Investigation are open to every child. The tutor never announces who is on which page, and never splits a pair unless both children agree. Invite the WHOLE group, never one child: "when you have finished Start here you can choose Think harder, Go further or the Investigation."'))

# ---------- 2. warm-up: Missing Edge Race ----------
cards=[(60,5,4,3),(72,6,3,4),(90,6,5,3),(84,7,3,4),(150,10,5,3),(96,8,2,6)]
body=h2('Warm-up: Missing Edge Match')+p('Each cuboid card shows the volume and two edges. Find the third edge. Write the division you used. We show answers together, nobody shouts.',34,600,MUTED)
CW=533
for i,(v,a,b,c) in enumerate(cards):
    L=128+(i%3)*(CW+32); T=300+(i//3)*290
    inner=(f'<p style="font-family:{HF};font-size:52px;font-weight:600;color:{TEAL}">{v} cm³</p><p style="font-size:36px;font-weight:700">edges: {a} cm and {b} cm</p><p style="font-size:36px;font-weight:700">third edge: ?</p>')
    body+=pin(L,T,CW,inner,None,WHITE,24,'18px 26px',f'box-sizing:border-box;height:270px;border:4px solid {NAVY};box-shadow:8px 8px 0 {NAVY}')
    body+=pin(L+20,T+196,CW-40,f'<p style="font-size:32px;font-weight:800">{v} ÷ ({a} × {b}) = {c} cm</p>','pop',YEL,16,'8px 16px',f'box-sizing:border-box;border:3px solid {NAVY}')
put('warm1',sec(sid('warm1'),'0–4 MIN',body,
 'Minutes 0 to 4. Missing Edge Match (not a race: nobody shouts, speed does not matter). Read one card at a time; teams write the third edge and the division on whiteboards, then show them together on three, two, one. Click to reveal the check (the card pops). Answers: 3, 4, 3, 4, 3, 6. Ask each time: "Which operation did you use?" (volume divided by the area of the base: one layer times the missing edge gives the volume). Watch for children who divide by only one edge. Extension: "A cuboid has volume 60 cm3. Its base is 5 cm by 4 cm. How many cm3 in one layer?" (20 cm3). If a child says 5 + 4 + 3, point out that a volume is multiplied, never added.'))

# ---------- 3. quick questions ----------
qs=[('1.','A cuboid is 7 cm by 5 cm by 2 cm. Volume?','70 cm³'),('2.','1 ℓ = ? cm³','1000 cm³'),('3.','3.2 ℓ = ? ml','3200 ml'),('4.','A cube has a volume of 125 cm³. Each edge?','5 cm'),('5.','4500 cm³ of water = ? ℓ','4.5 ℓ')]
body=h2('Quick questions')+''.join(qrow(128,250+i*125,1250,a,b) for i,(a,b,c) in enumerate(qs))+''.join(answer(1420,250+i*125,372,c) for i,(a,b,c) in enumerate(qs))
put('warm2',sec(sid('warm2'),'4–9 MIN',body,'Minutes 4 to 9. Read each aloud, whiteboards up together, then click to show. Answers: 70 cm3, 1000 cm3, 3200 ml, 5 cm, 4.5 litres. After 4 ask: "Which number multiplied by itself three times gives 125?" (5 x 5 x 5). After 2 ask: "How big is a 1000 cm3 box?" (10 cm by 10 cm by 10 cm, about the size of a small tissue box). 1 ml is the same as 1 cm3: a small sugar cube of water.'))

# ---------- 4. explore ----------
P1=OB(30,150,30); P2=OB(330,150,30)
g=box(P1,6,4,1,grid=True,fill=YELF,sw=3)+box(P2,2,3,4,grid=True,fill=YELF,sw=3)+tb(110,195,'6 × 4 × 1',28,TEAL)+tb(385,195,'2 × 3 × 4',28,TEAL)
g+=f'<rect x="640" y="12" width="640" height="170" rx="18" fill="{SOFT}" stroke="{NAVY}" stroke-width="4"/>'+txt(960,82,'24 cubes. Same volume.',40)+txt(960,140,'How many different cuboids?',36,TEAL)
steps=''.join(f'<li>{E(s)}</li>' for s in ['Take 24 one-centimetre cubes (or draw them on squared paper).','Build a cuboid that uses ALL 24 cubes. Write its length, breadth and height.','Build as many different cuboids as you can. Turning one round is not a new one.','How do you know you have found them all?'])
body=h2('Explore: the 24-cube challenge')+card(chip('EXPLORE')+f'<ol style="font-size:36px;font-weight:600;padding-left:52px;display:flex;flex-direction:column;gap:8px">{steps}</ol>')
body+=card(svgwrap(1300,210,'A flat 6 by 4 by 1 cuboid and a 2 by 3 by 4 cuboid, each made of 24 cubes',g),extra='padding:16px 32px')
put('explore1',sec(sid('explore1'),'9–14 MIN',body,'Minutes 9 to 14. Pairs build or draw cuboids with exactly 24 cubes (online: dice, Lego or squared-paper drawings). Ask them to predict first: how many cuboids? Most guess 3 or 4. Let them record in any order at first; the next slide asks how they know they have all. Hint: start with a flat cuboid 1 cube high, then 2 cubes high. Anyone who wants more (open to every pair): which one is most like a cube? Could any be a perfect cube? (No: 2 x 2 x 2 = 8 and 3 x 3 x 3 = 27, and 24 is between.)'))
body=h2('Explore: talk about it')+numcards([('1.','How many different cuboids did you find? Did your partner find the same ones?'),('2.','How do you know you have found them all?'),('3.','Do they all have the same volume? Do they look the same?')],40)
put('explore2',sec(sid('explore2'),'14–21 MIN',body,'Minutes 14 to 21. Let pairs keep working, then gather them. Write their cuboids on the board in the order they say them, messy on purpose, then ask "Is anything missing? Is anything there twice?" Answers: 1) 6 cuboids: 1 x 1 x 24, 1 x 2 x 12, 1 x 3 x 8, 1 x 4 x 6, 2 x 2 x 6, 2 x 3 x 4. 2) List in order by the shortest edge. Shortest edge 1: the other two multiply to 24 (1 x 24, 2 x 12, 3 x 8, 4 x 6). Shortest edge 2: the other two multiply to 12 and are at least 2 (2 x 6, 3 x 4). Shortest edge 3 would need two edges of at least 3 that multiply to 8: impossible. 3) All 24 cm3, but the shapes look very different. Do not name the method if nobody finds it: the later slides teach it.'))

# ---------- 5. teach: layers ----------
Pc=OB(110,330,50)
g=box(Pc,5,3,4,grid=True,fill=YELF,sw=4)+tb(235,372,'5 cm',28,NAVY)+tb(98,235,'4 cm',28,NAVY,'end')+tb(405,316,'3 cm',28,NAVY,'start')
body=h2('Volume: count a layer, then the layers')+pin(128,250,600,svgwrap(520,390,'A cuboid 5 cm long, 3 cm wide and 4 cm high built from 1-cm cubes',g),None,WHITE,24,'12px 12px')
body+=step(1,'One layer on the bottom: 5 rows of 3 cubes.  5 × 3 = 15 cubes.',left=800,top=250,width=992,size=36)
body+=step(2,'There are 4 layers on top of each other.  15 × 4 = 60 cubes.',left=800,top=390,width=992,size=36)
body+=step(3,'Volume = length × breadth × height = 5 × 3 × 4 = 60 cm³.  Each cube is 1 cm³.',left=800,top=530,width=992,size=36)
body+=pin(800,690,992,p('The base (length × breadth) is one layer. The height says how many layers.',36,700),'fade',SOFT,20,'22px 30px')
put('teach1',sec(sid('teach1'),'21–23 MIN',body,'Teach. Build the 5 by 3 by 4 cuboid with real cubes (or draw it on squared paper). Ask first: "How many cubes are in the bottom layer? How many layers?" Click through the steps. Think-aloud: "One layer is 5 rows of 3: 15. I have 4 layers, so 15 four times: 60. Length times breadth times height counts the same thing quickly." Ask: "If I use a 1-cm cube, one cube is 1 cm3." Go backwards: "A cuboid has volume 60 cm3 and a base of 15 cm2. How tall is it?" (60 / 15 = 4 layers).'))

# ---------- 6. worked example: water in a tank ----------
Pw=OB(110,340,9)
g=box(Pw,40,25,30,water=12,wlabel='12 cm',labels=['40 cm','30 cm','25 cm'],size=26,sw=3)
body=h2('Worked example: water in a tank')+card(p('A tank is 40 cm long, 25 cm wide and 30 cm high. The water is 12 cm deep. Then 8 ℓ more is poured in. How deep is the water now?',38,700))
body+=pin(128,450,680,svgwrap(680,400,'A tank 40 cm long, 25 cm wide and 30 cm high with water 12 cm deep, drawn to scale',g),None)
body+=step(1,'Water now:  40 × 25 × 12 = 12 000 cm³ = 12 ℓ',left=860,top=450,width=932,size=32)
body+=step(2,'8 ℓ = 8000 cm³.  One cm of height holds  40 × 25 = 1000 cm³.',left=860,top=570,width=932,size=32)
body+=step(3,'The water rises  8000 ÷ 1000 = 8 cm.   Now 12 + 8 = 20 cm deep.',left=860,top=690,width=932,size=32)
body+=pin(860,845,932,p('Check: 40 × 25 × 20 = 20 000 cm³ = 20 ℓ = 12 ℓ + 8 ℓ ✓',34,700),'fade',SOFT,20,'16px 28px')
put('we1',sec(sid('we1'),'23–26 MIN',body,'Click to reveal each step and let children say it first. Think-aloud: "The water is a cuboid too: 40 by 25 by 12. That is 12 000 cm3, and 1000 cm3 is 1 litre, so 12 litres. Adding 8 litres is 8000 cm3. The floor of the tank is 40 x 25 = 1000 cm2, so every centimetre of depth holds 1000 cm3. That means 8000 cm3 is 8 cm more." Stress: change litres to cm3 BEFORE dividing. The drawing is to scale: the tank is 30 cm tall and the water is 12 cm, so the water is a bit less than half way. Ask: "How many more litres fill the tank to the top?" (40 x 25 x 10 = 10 000 cm3 = 10 litres).'))
put('try1',try_slide(sid('try1'),'26–27 MIN','Your turn: whiteboards','Change litres to cm³ before you divide.',[('a','Base 20 cm by 10 cm, water 6 cm deep. How many ℓ?','1.2 ℓ'),('b','Base 30 cm by 20 cm. 3 ℓ of water. How deep?','5 cm'),('c','Base 25 cm by 20 cm, water 4 cm deep. Add 1.5 ℓ. New depth?','7 cm')],'Whiteboards up together, then click. a) 20 x 10 x 6 = 1200 cm3 = 1.2 litres. b) 3 litres = 3000 cm3; base 600 cm2; 3000 / 600 = 5 cm. c) 1.5 litres = 1500 cm3; base 500 cm2; 1500 / 500 = 3 cm more, so 4 + 3 = 7 cm. Watch for children who write 1.5 / 500 or who answer c with 3 cm (the rise, not the new depth).',size=36))

# ---------- 7. worked example: a stone sinks ----------
Pa=OB(30,300,7); Pb=OB(360,300,7)
g=box(Pa,30,20,24,water=10,wlabel='10 cm',labels=['30 cm',None,None],size=26,sw=3)
g+=box(Pb,30,20,24,water=13,wlabel='13 cm',labels=['30 cm',None,'20 cm'],size=26,sw=3)
Ps=lambda x,y,z: Pb(x+14,y,z+6)
g+=box(Ps,9,7,6,fill=CUBEF,sw=3)
g+=tb(140,372,'before',28,TEAL)+tb(480,372,'after: a stone sinks',28,TEAL)
body=h2('Worked example: a stone sinks')+card(p('The water in a tank (base 30 cm by 20 cm) is 10 cm deep. A stone sinks to the bottom. The water rises to 13 cm. What is the volume of the stone?',38,700))
body+=pin(128,450,740,svgwrap(740,390,'A tank with base 30 cm by 20 cm, water 10 cm deep before and 13 cm deep after a stone sinks, drawn to scale',g),None)
body+=step(1,'The water did not change. The stone pushes it up.',left=900,top=450,width=892,size=32)
body+=step(2,'Rise  = 13 − 10 = 3 cm.  The new slice of water: 30 × 20 × 3 = 1800 cm³.',left=900,top=570,width=892,size=32)
body+=step(3,'That slice is exactly the room the stone takes up.',left=900,top=700,width=892,size=32)
body+=answer(900,810,892,'The stone is 1800 cm³.')
put('we2',sec(sid('we2'),'27–29 MIN',body,'Do the live demonstration first if you can: clear box, ruler on the side, read the water level, drop in a stone, read it again. Then click through. Think-aloud: "The water went up 3 cm. The water itself is the same amount, so the stone must be taking up the space of a slice 30 by 20 by 3: 1800 cm3." Rule to write down: rise = volume of object / base area, so volume of object = base area x rise. Backwards: "A stone of 600 cm3 in this tank: 600 / 600 = 1 cm rise." Note the stone is completely under water here. If it sticks out, only the part under water counts: that comes back on the Go further page.'))
put('try2',try_slide(sid('try2'),'29–30 MIN','Your turn: sinking objects','The object is completely under water.',[('a','Base 30 cm by 10 cm. A stone makes the water rise 4 cm. Volume?','1200 cm³'),('b','Base 25 cm by 20 cm. A 1000 cm³ block sinks. How far does the water rise?','2 cm'),('c','Base 40 cm by 20 cm. Water goes from 9 cm to 12 cm. Volume?','2400 cm³')],'Whiteboards. a) 30 x 10 x 4 = 1200. b) base 500 cm2; 1000 / 500 = 2 cm. c) rise 3 cm; 40 x 20 x 3 = 2400. Ask for b: "Why is the rise small? (a wide base spreads the volume out)".',size=36))

# ---------- 8. teach: list in order ----------
body=h2('Every cuboid from 30 cubes: list in order')+card(p('Fix the SHORTEST edge. The other two edges must multiply to give the rest.',38,700))
rows=[('Shortest edge 1','other two make 30','1×1×30,  1×2×15,  1×3×10,  1×5×6'),('Shortest edge 2','other two make 15, each 2 or more','2×3×5'),('Shortest edge 3','other two make 10, each 3 or more','none: stop!')]
for i,(a,b,c) in enumerate(rows):
    T=450+i*130
    body+=pin(128,T,420,p(a,34,800,TEAL),None,WHITE,20,'16px 24px')+pin(580,T,620,p(b,30,600),'rise',WHITE,20,'16px 24px')+pin(1230,T,562,p(c,34,800),'rise',YEL,20,'16px 24px')
body+=pin(128,850,1664,p('5 cuboids. Your turn: how many cuboids from 20 cubes?',34,700),'fade',SOFT,20,'12px 28px')
body+=answer(1380,850,412,'4 cuboids')
put('teachlist',sec(sid('teachlist'),'30–32 MIN',body,'Teach: the listing method from the Explore, with a new number. Click to reveal row by row; children say the pairs first. Think-aloud: "If the shortest edge is 1, the other two multiply to 30: 1 x 30, 2 x 15, 3 x 10, 5 x 6. I stop at 5 x 6 because the next pair would just be turned round. Shortest edge 2: the other two multiply to 15 and cannot be 1: 3 x 5. Shortest edge 3 needs two edges of at least 3 that multiply to 10: impossible. So I am finished: 5 cuboids." Your turn (20 cubes): 1x1x20, 1x2x10, 1x4x5, 2x2x5. The 20-cube answer is 4. Ask: "Why can the shortest edge never be bigger than the cube root?" only if time (3 x 3 x 3 = 27 is already more than 20).'))
body=h2('Key idea: base area × height')+card(p('A cuboid, or the water in a tank, has volume = base area × height. Anything that sinks raises the water by its volume ÷ base area.',42,700))+card(p('1 ℓ = 1000 cm³ and 1 ml = 1 cm³. Change litres to cm³ before you divide by a base area.',36,600,MUTED))
put('key',sec(sid('key'),'32–33 MIN',body,'Say the key idea together. Common mistakes to watch for during the worksheet: (1) Mixing units: dividing 8 litres by a base area in cm2 without changing 8 litres to 8000 cm3. (2) Using the height of the tank instead of the depth of the water, or giving the new level when the question asks for the rise (or the other way round). (3) Painted cubes: counting a corner cube again as an edge cube, or using n instead of n - 2 for the cubes along each edge.'))
put('break',break_slide(sid('break'),'33–37 MIN','More or less than 1 litre? I name an object. Stand tall if it holds more than 1 ℓ. Crouch if it holds less.','Five minutes. Call: a teacup (less), a big bottle of water (1.5 litres: more), a bathtub (more), a can of drink (330 ml: less), a fish tank (more), a bowl of soup (less), a bucket (more). Ask about the can: "How many cm3 is that?" (330 cm3). Online: children stand and crouch in view of the camera.'))

# ---------- worksheet page 1 ----------
put('ws1',ws_preview(sid('ws1'),'37–49 MIN','Worksheet page 1: with your partner',[('Q1','Count the cubes. Turn the cuboid into a cube.'),('Q2','All the cuboids from 36 cubes. List in order.'),('Q3','The glass tank: litres, filling up, letting water out.')],'Stuck? Draw the tank and write every length on the picture. Is it litres or cm³?','Minutes 37 to 49. Walk around. Ask "How do you know you have them all?" and "Is that litres or cm3?" before giving any help. Q1b: the cube must be big enough to hold the cuboid, so its edge is at least 4 cm (the longest edge). Q2: remind them to keep the shortest edge fixed. Q3c: water LEAVES, so the level goes down.'))
put('ws1ans',checks(sid('ws1ans'),'49–51 MIN','Page 1: check together',[('Q1','a) 24 cm³   b) 40 cubes (4 × 4 × 4 = 64, and 64 − 24 = 40)'),('Q2','a) 8 cuboids   b) only 3 × 3 × 4 fits in 5 × 5 × 5'),('Q3','a) 27 ℓ   b) 33 ℓ   c) 12 cm')],
 'Click each answer after a pair explains theirs. Q2a: 1x1x36, 1x2x18, 1x3x12, 1x4x9, 1x6x6, 2x2x9, 2x3x6, 3x3x4. Q2b: every other cuboid has an edge longer than 5 cm; 3 x 3 x 4 has edges 3, 3 and 4. Q3a: 50 x 30 x 18 = 27 000 cm3 = 27 litres. Q3b: the tank holds 50 x 30 x 40 = 60 litres, so 60 - 27 = 33 (or 50 x 30 x 22 = 33 000 cm3). Q3c: 9 litres = 9000 cm3; base 1500 cm2; 9000 / 1500 = 6 cm lower; 18 - 6 = 12 cm.',gapy=170))

# ---------- teach before page 2: painted cubes ----------
Pp=OB(30,370,50)
g=box(Pp,5,5,5,grid=True,fill=YELF,sw=4)
W3=[340,420,200]
body=h2('Painted cubes: a 5 × 5 × 5 cube')+pin(128,250,600,svgwrap(520,430,'A 5 by 5 by 5 cube made of 125 small cubes, painted yellow on the outside',g),None,WHITE,24,'8px 8px')
body+=trow(760,250,['Painted faces','How we count','Cubes'],W3,None,True,30)
rws=[['3 faces','8 corners','8'],['2 faces','12 edges × 3','36'],['1 face','6 faces × 3 × 3','54'],['no paint','inside 3 × 3 × 3','27']]
for i,r in enumerate(rws): body+=trow(760,345+i*88,r,W3,'rise',False,30)
body+=pin(760,690,1032,p('Along each edge, the 2 end cubes are corners. The rest, 5 − 2 = 3, are edge cubes.',34,700),'fade',SOFT,20,'18px 28px')
body+=pin(760,830,1032,p('Check: 8 + 36 + 54 + 27 = 125 ✓',36,800),'fade',YEL,20,'12px 28px')
put('teachpaint',sec(sid('teachpaint'),'51–54 MIN',body,'Teach before worksheet page 2 (Q5, a 4 x 4 x 4 cube). Ask first: "How many of the 125 cubes touch the outside? Which cubes have 3 painted faces? 2? 1? none?" Click row by row. Think-aloud: "The 8 corner cubes show 3 faces. Along each edge there are 5 cubes: the 2 ends are corners, so 3 are in the middle, with 2 painted faces. A cube has 12 edges: 12 x 3 = 36. Each face is a 5 by 5 square: take off the border, and the middle is 3 x 3 = 9 cubes with only 1 painted face. 6 faces: 54. What is left is a 3 x 3 x 3 block inside with no paint: 27. Check that they add up to 125." Why do we write 5 - 2? Because each edge loses its 2 corner cubes. For the worksheet cube the middle size will be 4 - 2.'))

# ---------- teach before page 2: pouring ----------
Pa=OB(100,330,6); Pb=OB(450,330,6)
g=box(Pa,20,10,24,water=24,labels=['20 cm','24 cm','10 cm'],size=26,sw=3)+box(Pb,30,20,14,water=0,labels=['30 cm','14 cm','20 cm'],size=26,sw=3)
g+=tb(170,150,'A (full)',28,TEAL)+tb(600,190,'B (empty)',28,TEAL)
body=h2('Pouring from one tank into another')+card(p('Container A (20 × 10 × 24 cm) is full of water. It is poured into empty tank B (base 30 × 20 cm). How deep is the water in B?',36,700))
body+=pin(128,430,780,svgwrap(780,380,'Container A, 20 cm by 10 cm by 24 cm, full of water, and empty tank B with base 30 cm by 20 cm, drawn to the same scale',g),None)
body+=step(1,'Water in A:  20 × 10 × 24 = 4800 cm³.  The amount does not change when we pour.',left=930,top=430,width=862,size=32)
body+=step(2,'Base of B is 30 × 20 = 600 cm².   4800 ÷ 600 = 8 cm deep.',left=930,top=560,width=862,size=32)
body+=step(3,'Pour back until the depths are equal. Both bases share: 200 + 600 = 800 cm².',left=930,top=690,width=862,size=32)
body+=pin(930,840,862,p('4800 ÷ 800 = 6 cm in each.  Check: 200 × 6 + 600 × 6 = 4800 ✓',34,800),'fade',YEL,20,'14px 28px')
put('teachpour',sec(sid('teachpour'),'54–57 MIN',body,'Teach before worksheet page 2 (Q6). Ask first: "Does the amount of water change when we pour it?" (No: the volume is the same, only the shape changes.) Click through. Think-aloud: "Volume stays 4800. Base of B is 600, so depth 8. Now both containers: the water is shared over both floors. Equal depth d means 200 x d + 600 x d = 4800, so 800 x d = 4800 and d = 6 cm. I add the two base areas, then divide." Do not use letters with the children: say "the same depth" and divide 4800 by 800. Check: A holds 200 x 6 = 1200 cm3 and B holds 600 x 6 = 3600 cm3 and 1200 + 3600 = 4800.'))
put('ws2',ws_preview(sid('ws2'),'57–72 MIN','Worksheet page 2: on your own',[('Q4','The metal cubes sink. Start with the layer: one cm of water over the base. Then the rise.'),('Q5','The 4 × 4 × 4 painted cube. Check that you get 64.'),('Q6','Container A into tank B: litres, then the depth.')],'Want more? Think harder and Go further are at the back of your workbook.','Children work alone. Note who needs a short catch-up next lesson, especially children who still divide litres by cm2 without changing the unit.'))
put('ws2ans',checks(sid('ws2ans'),'72–76 MIN','Page 2: check together',[('Q4','a) 5000 cm³   b) 5 cm   c) 20 cm'),('Q5','3 faces 8,  2 faces 24,  1 face 24,  no paint 8  (total 64)'),('Q6','a) 14.4 ℓ   b) 12 cm')],
 'Click each answer after a child explains. Q4: 5 cubes of 1000 cm3 = 5000 cm3; base 40 x 25 = 1000 cm2; rise 5 cm; depth 15 + 5 = 20 cm. Q5: 8 corners; 12 edges x (4 - 2) = 24; 6 faces x 2 x 2 = 24; inside 2 x 2 x 2 = 8; 8 + 24 + 24 + 8 = 64. Q6a: 30 x 20 x 24 = 14 400 cm3 = 14.4 litres. Q6b: base of B 40 x 30 = 1200; 14 400 / 1200 = 12 cm. (Equal depth after pouring back, in the question bank: bases 600 + 1200 = 1800; 14 400 / 1800 = 8 cm. A stone that raises the water 3 cm: 1000 x 3 = 3000 cm3.)',gapy=170))

# ---------- stretch / challenge ----------
import p5_printed as _PP
for _k,_v in _PP.slides(5,'A').items(): S[f'p5l5-{_k}']=_v
ch=[('E1.', 'A tank has a base 40 cm by 30 cm. A cube with edges of 10 cm sits on the bottom, and the water is 6 cm deep around it. How much water is in the tank?')]
for _k,_v in _PP.slides(5,'B').items(): S[f'p5l5-{_k}']=_v
put('challenge',sec(sid('challenge'),'37–72 MIN  •  OPTION',h2('More Go further puzzles (extra, not in your workbook)')+numcards(ch,36),'Pairs try first, then use the "see it" slide if stuck, then the walk-through. These are in the question bank and Think harder. Answers: 1) 6600 cm3 = 6.6 litres (40 x 30 x 6 = 7200 cm3 if there were no cube, but the cube takes up 10 x 10 x 6 = 600 cm3 of that space: the cube is taller than the water, so only 6 cm of it is under water. 7200 - 600 = 6600). 2) 12 cm (the block takes 10 x 10 = 100 cm2 of the floor, so the water spreads over 500 cm2: 6000 / 500 = 12 cm; the block is 15 cm tall so it sticks out of the water). Not 12.5 cm: 12.5 would come from adding the block as if it were fully under water.'))
Pa=OB(100,300,5); Pc=lambda x,y,z: Pa(x+15,y,z+10)
g1=box(Pa,40,30,18,water=6,labels=['40 cm','18 cm','30 cm'],size=24,sw=3)+box(Pc,10,10,10,fill=CUBEF,sw=3)+tb(300,372,'cube 10 cm, water 6 cm deep',24,TEAL)
Pt=OB(110,340,6); Pk=lambda x,y,z: Pt(x+10,y,z+5)
g2=box(Pt,30,20,30,water=10,labels=['30 cm','30 cm','20 cm'],size=26,sw=3)+box(Pk,10,10,15,fill=CUBEF,sw=3)+tb(230,408,'block: 10 × 10 × 15 cm, upright',24,TEAL)
def dcard(title,svgs,w): return card(f'<p style="font-size:30px;font-weight:700;color:{TEAL}">{title}</p>'+svgs,extra='flex:1;min-width:0;padding:20px 24px')
body=h2('Go further: see it',60)+'<div style="display:flex;gap:32px;align-items:flex-start">'
body+=dcard('E1: A cube in the tank',svgwrap(780,390,'A tank with base 40 cm by 30 cm, a 10 cm cube on the bottom and water 6 cm deep around it',g1,'width:100%;height:auto'),0)
body+=dcard('B3: The upright block',svgwrap(520,420,'A tank with base 30 cm by 20 cm, water 10 cm deep, and a block 10 cm by 10 cm by 15 cm standing on the bottom',g2,'width:520px;height:auto;align-self:center'),0)+'</div>'
put('chdiag',sec(sid('chdiag'),'37–72 MIN  •  OPTION',body,'Show after pairs have tried Go further, or if they are stuck. The pictures show the problem, not the answer, and are drawn to scale. Ask: What do you notice? In E1, how tall is the cube compared with the water, and how much of the cube is under water? In B3, how tall is the block compared with the water? Is it completely under water? What floor area does the water have now? Answers are in the Go further slide notes.'))
body=h2('Go further: walk-through')+pin(128,250,800,p('E1: the cube takes up space',38,800,TEAL))
for i,t in enumerate(['No cube: 40 × 30 × 6 = 7200 cm³','Cube under water: 10 × 10 × 6 = 600 cm³','7200 − 600 = 6600 cm³','6600 cm³ = 6.6 ℓ ✓']): body+=pin(128,330+i*105,800,p(t,32),'rise',WHITE)
body+=pin(992,250,800,p('B3: the block takes up floor',38,800,TEAL))
for i,t in enumerate(['Water: 30 × 20 × 10 = 6000 cm³','Floor left: 600 − 100 = 500 cm²','6000 ÷ 500 = 12 cm','12 is less than 15: the block sticks out ✓']): body+=pin(992,330+i*105,800,p(t,32),'rise',WHITE)
put('chwalk',sec(sid('chwalk'),'37–72 MIN  •  OPTION',body,'Use after pairs have tried. E1: the cube is 10 cm tall but the water is only 6 cm deep, so only 6 cm of the cube is under water. Ask: what if the water were 12 cm deep? (Then the whole cube is under water: 40 x 30 x 12 - 1000 = 13 400 cm3.) B3: the water has the same volume as before, but the block takes away 10 x 10 = 100 cm2 of the floor, so the water is squeezed into 500 cm2 and rises higher. Always check that the block is taller than the water (15 > 12); if the water were deeper than the block, we would add the block as a solid instead.'))

# ---------- talk / exit ----------
body=h2('Talk time')+card(chip('TALK TIME',YEL,NAVY)+p('Ali says: “A 1000 cm³ stone always makes the water rise 1 cm.” Is he right? Explain.',42,600))+card(p('Sentence starters:',34,400,MUTED)+p('“I noticed that …”   “I tested it by …”   “I know because …”',38,600))
put('talk',sec(sid('talk'),'76–82 MIN',body,'Minutes 76 to 82. Pairs talk for 2 minutes, then share. Answer: Ali is right only when the base is 1000 cm2 (for example 40 cm by 25 cm). The rise is the stone\'s volume divided by the base area. In a tank with a 20 cm by 10 cm base (200 cm2) the same stone makes the water rise 1000 / 200 = 5 cm. A wide tank spreads the volume over a big base, so the water hardly rises. Second question if time: "If the stone sticks out of the water, is it the whole volume of the stone that counts?" (No, only the part under the water.) Praise the reasons, not only the answers.'))
body=h2('Exit ticket')+card(chip('EXIT TICKET')+p('A tank has a base 30 cm by 25 cm and water 8 cm deep. A rock sinks and the water rises to 10 cm. (a) What is the volume of the rock? (b) How many litres of water are in the tank?',40,600))+card(p('Write your answer on a slip of paper. Show it to your tutor. Then collect your stamp in your inquiry journal.',34,400))
put('exit',sec(sid('exit'),'82–90 MIN',body,'Minutes 82 to 90. Answers: (a) 1500 cm3 (30 x 25 x 2). (b) 6 litres (30 x 25 x 8 = 6000 cm3). Extension: find every cuboid with whole-number edges and a volume of 60 cm3 (there are 10, from 1 x 1 x 60 to 3 x 4 x 5). Which one is most like a cube? (3 x 4 x 5).'))

order=[sid(x) for x in ['title','warm1','warm2','explore1','explore2','teach1','we1','try1','we2','try2','teachlist','key','break','ws1','ws1ans','teachpaint','teachpour','ws2','ws2ans','stretch','challenge','chdiag','chwalk','talk','exit']]
order=_PP.fix_order(order,5,S)
finish(P,S,order,'Math Inquirers P5: Lesson 5 – Volume Vault',{'s1':{'description':'Warm-up and explore','start':sid('title')},'s2':{'description':'Teach: layers, water in tanks, sinking objects','start':sid('teach1')},'s3':{'description':'Worksheet with teaching before each page','start':sid('break')},'s4':{'description':'Think harder, Go further, talk and exit','start':sid('stretch')}},D)

import p5_gaps; p5_gaps.apply(5)
