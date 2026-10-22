import json,os,sys
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,H)
from slidekit import *
D=os.path.join(H,'..','split','l9','project'); S={}
def put(i,h): S[i]=h
RED='#D64545'; ROPE_R='#F4A6A6'; ROPE_B='#9CC9EE'; GREEN='#BFE3DC'; CLIP='#C9D4EC'; ERASER='#F7B7C8'; WOOD='#D9B38C'

# ---------- local drawing helpers ----------
def row_svg(label,items,u=60,lab_w=170,h=76,after='',aria='',width=None,lab_size=34):
    """items: list of (count, size_in_units, fill, style); style: solid|dashT|dashR|clip|blank|hl"""
    x=lab_w; b=''
    if label: b+=f'<text x="0" y="{h/2+12}" font-size="{lab_size}" font-weight="800" fill="{NAVY}" font-family="Nunito Sans, Arial">{E(label)}</text>'
    for cnt,size,fill,style in items:
        for i in range(cnt):
            w=size*u
            if style=='blank': pass
            elif style=='dashT': b+=f'<rect x="{x+2}" y="8" width="{w-4}" height="{h-16}" rx="6" fill="{WHITE}" stroke="{TEAL}" stroke-width="4" stroke-dasharray="10 7"/>'
            elif style=='dashR': b+=f'<rect x="{x+2}" y="8" width="{w-4}" height="{h-16}" rx="6" fill="{WHITE}" stroke="{RED}" stroke-width="4" stroke-dasharray="10 7"/>'
            elif style=='hl': b+=f'<rect x="{x+2}" y="4" width="{w-4}" height="{h-8}" rx="6" fill="{YEL}" fill-opacity=".55" stroke="{TEAL}" stroke-width="6"/>'
            elif style=='clip':
                b+=f'<rect x="{x+3}" y="10" width="{w-6}" height="{h-20}" rx="{(h-20)/2}" fill="{fill}" stroke="{NAVY}" stroke-width="4"/><rect x="{x+16}" y="22" width="{w-40}" height="{h-44}" rx="{(h-44)/2}" fill="none" stroke="{NAVY}" stroke-width="3"/>'
            else: b+=f'<rect x="{x+2}" y="8" width="{w-4}" height="{h-16}" rx="6" fill="{fill}" stroke="{NAVY}" stroke-width="4"/>'
            x+=w
    if after: b+=f'<text x="{x+18}" y="{h/2+12}" font-size="34" font-weight="800" fill="{TEAL}" font-family="Nunito Sans, Arial">{E(after)}</text>'
    W=width or int(x+(len(after)*19+40 if after else 10))
    return f'<svg aria-label="{E(aria or label or "bar")}" viewBox="0 0 {W} {h}" xmlns="http://www.w3.org/2000/svg" style="width:{W}px;height:{h}px">{b}</svg>'

def ruler_svg(n=12,cm=120,obj=None,arcs=None,only_arcs=False,aria='Ruler in centimetres'):
    """obj=(start,end,label,fill); arcs=(start,end) draws numbered jumps over each cm space"""
    ml=44; W=ml*2+n*cm; Hh=232
    X=lambda k: ml+k*cm
    b=''
    if not only_arcs:
        b+=f'<rect x="{ml-34}" y="126" width="{n*cm+68}" height="100" rx="10" fill="#FFE9A8" stroke="{NAVY}" stroke-width="4"/>'
        for k in range(n+1):
            b+=f'<line x1="{X(k)}" y1="126" x2="{X(k)}" y2="170" stroke="{NAVY}" stroke-width="4"/>'
            b+=f'<text x="{X(k)}" y="212" font-size="34" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="Nunito Sans, Arial">{k}</text>'
        b+=f'<text x="{X(n)-cm/2}" y="160" font-size="26" font-weight="800" text-anchor="middle" fill="{MUTED}" font-family="Nunito Sans, Arial">cm</text>'
        if obj:
            a,e,lab,fill=obj
            b+=f'<rect x="{X(a)}" y="70" width="{X(e)-X(a)}" height="46" rx="12" fill="{fill}" stroke="{NAVY}" stroke-width="4"/>'
            b+=f'<text x="{(X(a)+X(e))/2}" y="104" font-size="30" font-weight="800" text-anchor="middle" fill="{NAVY}" font-family="Nunito Sans, Arial">{E(lab)}</text>'
            for k in (a,e): b+=f'<line x1="{X(k)}" y1="116" x2="{X(k)}" y2="170" stroke="{RED}" stroke-width="4" stroke-dasharray="7 5"/>'
    if arcs:
        a,e=arcs
        for i,k in enumerate(range(a,e)):
            x1,x2=X(k)+4,X(k+1)-4
            b+=f'<path d="M{x1} 68 Q{(x1+x2)/2} -16 {x2} 68" fill="none" stroke="{TEAL}" stroke-width="4"/>'
            b+=f'<text x="{(x1+x2)/2}" y="62" font-size="28" font-weight="800" text-anchor="middle" fill="{TEAL}" font-family="Nunito Sans, Arial">{i+1}</text>'
    return f'<svg aria-label="{E(aria)}" viewBox="0 0 {W} {Hh}" xmlns="http://www.w3.org/2000/svg" style="width:{W}px;height:{Hh}px">{b}</svg>'

def pencil_svg(blocks,u=100,aria='Pencil measured with blocks'):
    """pencil 6u long; blocks: list of (x_in_u, w_in_u, fill)"""
    W=6*u+20; Hh=140
    b=f'<rect x="0" y="10" width="{6*u-50}" height="46" rx="6" fill="{YEL}" stroke="{NAVY}" stroke-width="4"/><polygon points="{6*u-50},10 {6*u},33 {6*u-50},56" fill="#F2C9A0" stroke="{NAVY}" stroke-width="4" stroke-linejoin="round"/>'
    b+=f'<line x1="2" y1="0" x2="2" y2="140" stroke="{RED}" stroke-width="4" stroke-dasharray="8 6"/>'
    for x,w,f in blocks: b+=f'<rect x="{x*u+2}" y="70" width="{w*u-4}" height="{min(w,1)*u*0.6}" rx="6" fill="{f}" stroke="{NAVY}" stroke-width="4"/>'
    return f'<svg aria-label="{E(aria)}" viewBox="0 0 {W} {Hh}" xmlns="http://www.w3.org/2000/svg" style="width:{W}px;height:{Hh}px;flex-shrink:0">{b}</svg>'

def side(inner,extra=''): return 'flex-direction:row;align-items:center;gap:40px;'+extra

# ---------- 3. quick questions ----------
qs=[('1.','A ribbon is 7 cubes. A string is 4 cubes. Which is longer?','Ribbon'),('2.','How many cubes longer is it?','3 cubes'),('3.','Crayon 5 cubes, pen 9 cubes, pencil 7 cubes. Shortest first?','Crayon, pencil, pen'),('4.','How do we compare two lengths fairly?','Line up the ends')]
body=h2('Quick questions')+''.join(qrow(128,250+i*150,1250,a,b,36) for i,(a,b,c) in enumerate(qs))+''.join(answer(1420,250+i*150,372,c) for i,(a,b,c) in enumerate(qs))
put('l9-warm2',sec('l9-warm2','5–10 MIN',body,'Minutes 5 to 10. Read each question aloud, give thinking time, take answers, then click to show the answer. Ask "How do you know?" each time. Answers: 1) The ribbon (7 cubes is more than 4 cubes). 2) 3 cubes (7 − 4 = 3; or count on from 4 to 7). 3) Crayon (5), pencil (7), pen (9). 4) Line up one end of each object at the same starting line, then look at the other end. Watch for children who say "the pen is longest because it has the biggest number" without saying the units are the same: praise it, then add "because they were all measured in the same cubes".'))

# ---------- 6. teach: measure fairly ----------
r1=pencil_svg([(i,1,GREEN) for i in range(6)],aria='Pencil measured with 6 equal cubes and no gaps')
r2=pencil_svg([(i*1.5,1,GREEN) for i in range(4)],aria='Pencil measured with 4 cubes with gaps')
r3=pencil_svg([(0,2,'#9CC9EE'),(2,1,GREEN),(3,2,'#9CC9EE'),(5,1,GREEN)],aria='Pencil measured with big and small blocks')
cap=lambda t,col: p(t,36,800,col)
body=h2('Measure fairly: equal units')+p('The same pencil is measured three ways. Which way is fair?',34,600,MUTED)
body+=pin(128,300,1664,r1+cap('✓  Fair: equal cubes, touching, starting at the end: 6 cubes',TEAL),'rise',extra=side(''))
body+=pin(128,460,1664,r2+cap('Not fair: gaps. Only 4 cubes, but the pencil did not get shorter.',RED),'rise',extra=side(''))
body+=pin(128,620,1664,r3+cap('Not fair: big and small blocks. "4" does not tell us the length.',RED),'rise',extra=side(''))
body+=pin(128,790,1664,p('Same-size units, no gaps, no overlaps, start at the end. Then everyone gets the same number.',34,700),'fade',SOFT,20,'20px 30px')
put('l9-teach1',sec('l9-teach1','25–27 MIN',body,'Teach: the idea and why. Hold up a real pencil and some cubes. Click 1: six equal cubes from the very end of the pencil, touching. Click 2: the same pencil with gaps. Ask: "Is the pencil really 4 cubes long? Did it shrink?" (No: the gaps are length we did not count.) Click 3: big and small blocks. Ask: "If Ali says 4 blocks and Mei says 6 cubes, who has the longer pencil?" (We cannot tell: the units are not the same.) Click 4: read the rule together. Think-aloud: "Rules for measuring: equal units, no gaps, no overlaps, start at the end. If I break a rule, my number is not fair." Link back to the explore: "This is why you and your partner got different numbers of hand spans."'))

# ---------- 7. worked example: compare two lengths ----------
U=52
red=row_svg('Red',[(8,1,ROPE_R,'solid')],U,150,after='8',aria='Red rope, 8 cubes')
blue=row_svg('Blue',[(5,1,ROPE_B,'solid')],U,150,after='5',aria='Blue rope, 5 cubes')
hl=row_svg('',[(5,1,None,'blank'),(3,1,None,'hl')],U,150,width=8*U+150+10,aria='The extra 3 cubes of the red rope')
tog=row_svg('Together',[(8,1,ROPE_R,'solid'),(5,1,ROPE_B,'solid')],U,150,after='13',aria='Red and blue end to end, 13 cubes',lab_size=30)
cut=row_svg('Red, cut',[(5,1,ROPE_R,'solid'),(3,1,None,'dashR')],U,150,after='5',aria='Red rope cut 3 cubes shorter',lab_size=30)
body=h2('Worked example: compare two lengths')+card(p('A red rope is 8 cubes long. A blue rope is 5 cubes long.',40,700))
body+=pin(128,370,940,red)+pin(128,460,940,blue)
body+=step(1,'Line up the left ends. Red sticks out by 3 cubes: 8 − 5 = 3. Red is 3 cubes longer.',left=1100,top=370,width=692,size=32)
body+=pin(128,370,940,hl,'fade')
body+=step(2,'End to end: 8 + 5 = 13 cubes.',left=1100,top=560,width=692,size=32)
body+=pin(128,600,940,tog,'rise')
body+=step(3,'Cut 3 cubes off red: 8 − 3 = 5. Now red is the same as blue.',left=1100,top=690,width=692,size=32)
body+=pin(128,720,940,cut,'rise')
put('l9-we1',sec('l9-we1','27–29 MIN',body,'Worked example. Before each click ask the group to predict. Step 1 then the yellow highlight: "I line up the left ends, like a race start. Red goes further. The part that sticks out is the difference: 3 cubes. 8 take away 5 is 3." Step 2 then the long bar: "End to end means one after the other, so I add: 8 + 5 = 13." Step 3 then the cut bar: "If I cut 3 cubes off red, 8 − 3 = 5, the same as blue." Common mistake: answering "8" to "how much longer" (the length, not the difference). Point at the highlighted part.'))

put('l9-try1',try_slide('l9-try1','29–30 MIN','Your turn: whiteboards','Draw two bars. Line up the left ends.',[('a','A ribbon is 9 cubes. A string is 6 cubes. How much longer is the ribbon?','3 cubes'),('b','Put the ribbon and the string end to end. How long?','15 cubes'),('c','A 10-cube rope is cut 4 cubes shorter. How long is it now?','6 cubes')],'Whiteboards up together, then click. a) 9 − 6 = 3. b) 9 + 6 = 15. c) 10 − 4 = 6. Ask a child to show the part that sticks out on their bars for a. A child who writes 9 for a has given the length, not the difference.',36))

# ---------- 9. teach: cm ruler ----------
body=h2('Centimetres: measure with a ruler')+p('A ruler is a row of equal units called centimetres (cm). Each space between two marks is 1 cm.',34,600,MUTED)
body+=pin(128,330,1664,ruler_svg(12,120,(0,7,'crayon',SKY),aria='Ruler 0 to 12 cm with a crayon from 0 to 7'))
body+=step(1,'Put one end of the crayon at 0.',top=620,size=34)
body+=step(2,'Read the number at the other end: 7. The crayon is 7 cm long.',top=720,size=34)
body+=pin(128,330,1664,ruler_svg(12,120,None,(0,7),True,aria='Counting the 7 cm spaces'),'fade')
body+=pin(128,820,1664,p('Check: count the spaces, not the marks: 7 spaces, 7 cm.',32,700),'fade',SOFT,20,'14px 28px')
put('l9-teachcm',sec('l9-teachcm','30–31 MIN',body,'Teach. Give out rulers. "Cubes are our own unit. Everyone in the world uses the same unit: the centimetre. A ruler is a row of centimetres stuck together." Show that each space from one mark to the next is 1 cm (a fingertip wide). Click 1 and 2. Click 3 shows the jumps: "The number 7 tells us 7 spaces from 0." Click 4: "We count spaces, not marks. If I counted the marks from 0 to 7 I would get 8, which is wrong." Some rulers have a blank bit before 0: show where 0 is on yours.'))

# ---------- 10. worked example: not starting at 0 ----------
body=h2('Worked example: not starting at 0')+card(p('A key lies from the 2 cm mark to the 9 cm mark. How long is the key?',40,700))
body+=pin(128,360,1664,ruler_svg(12,120,(2,9,'key',GREEN),aria='Ruler with a key from 2 cm to 9 cm'))
body+=step(1,'The key does not start at 0, so 9 is NOT the answer.',top=620,size=34)
body+=step(2,'Count the spaces from 2 to 9: 1, 2, 3, 4, 5, 6, 7.',top=720,size=34)
body+=pin(128,360,1664,ruler_svg(12,120,None,(2,9),True,aria='Counting the 7 spaces from 2 to 9'),'fade')
body+=step(3,'The key is 7 cm long. Check: 9 − 2 = 7 ✓',top=820,size=34)
put('l9-we2',sec('l9-we2','31–33 MIN',body,'Worked example (a ruler that does not start at 0, as if the end of the ruler were broken). Ask first: "How long is the key?" Many children say 9. Click 1: "9 is where the key ends, not how long it is. It started at 2, not 0." Click 2 and the jumps: count the spaces aloud together. Click 3: "Another way: from 0 to 9 is 9 spaces, but the first 2 spaces are not under the key. 9 − 2 = 7." Check by sliding a real key or pencil so it starts at 0. Think-aloud: "Where does it start? Where does it end? I count the spaces in between."'))

# ---------- 11. try 2 ----------
body=h2('Your turn: how long?')+p('Count the cm spaces between the two ends.',34,600,MUTED)
body+=qrow(128,290,1250,'a','How long is the eraser?',36)+answer(1420,290,372,'4 cm')
body+=pin(128,380,1250,ruler_svg(12,95,(2,6,'eraser',ERASER),aria='Ruler with an eraser from 2 cm to 6 cm'))
body+=qrow(128,640,1250,'b','A pencil lies from the 6 cm mark to the 11 cm mark.',36)+answer(1420,640,372,'5 cm')
body+=qrow(128,780,1250,'c','A clip lies from the 1 cm mark to the 4 cm mark.',36)+answer(1420,780,372,'3 cm')
put('l9-try2',sec('l9-try2','33–34 MIN',body,'Whiteboards. a) The eraser goes from 2 to 6: 4 spaces, 4 cm (6 − 2 = 4). b) 11 − 6 = 5 cm. c) 4 − 1 = 3 cm. A child who writes 6, 11 or 4 is reading the end mark only: ask "Where does it start?" Let them check b and c on a real ruler.'))

# ---------- 12. key ----------
body=h2('Key idea: measure fairly')+card(p('Use equal units with no gaps and no overlaps. Line up the ends.',46,700))+card(p('On a ruler, count the cm spaces from one end to the other.',38,600,MUTED))
put('l9-key',sec('l9-key','34–35 MIN',body,'Say the key idea together. Common mistakes to watch for during the worksheet: (1) Counting a ribbon\'s squares carelessly or counting a square twice: touch each one. (2) Answering "how much longer" with the length instead of the difference. (3) "End to end" means add the two lengths. (4) Leaving gaps between cubes in Q2. (5) On a ruler, reading the end mark when the object does not start at 0.'))

# ---------- worksheet page 1 ----------
put('l9-ws1',ws_preview('l9-ws1','40–51 MIN','Worksheet page 1: with your partner',[('Q1','Three ribbons made of squares. Count each one, then compare.'),('Q2','Use what you measured in Explore. Write your guess, your measure and how far off you were. Only "My choice" is a new measure.')],'Stuck? Line up the ends and touch each square as you count.','Minutes 40 to 51. Walk around. Ask "How do you know?" before giving any help. Q1: check children count the squares (A 7, B 5, C 9) before answering. Q2: children copy the pencil, book and shoe numbers they found in Explore (no second measuring); only the "My choice" row is a new measure, so watch for gaps and for cubes not starting at the end of the object. The "How far off my guess was" column is the gap between guess and measure (for a guess of 8 and a measure of 6, it is 2).'))
put('l9-ws1ans',check_slide('l9-ws1ans','51–53 MIN','Page 1: check together',[('Q1','a) C   b) B   c) 2 squares   d) 12 squares   e) A'),('Q2','Answers will be different. Same-size cubes make the counts fair to compare.')],'Click each answer after a pair explains theirs. Q1: A has 7 squares, B has 5, C has 9. c) 7 − 5 = 2. d) 7 + 5 = 12. e) C cut 2 shorter: 9 − 2 = 7, the same as A. Q2a: "If the cubes were different sizes, the numbers would not mean the same thing, so we could not compare."'))

# ---------- teach before page 2: bigger unit ----------
U=60
stick=row_svg('Stick',[(1,8,WOOD,'solid')],U,200,aria='A stick 8 erasers long')
clips=row_svg('Clips',[(4,2,CLIP,'clip')],U,200,after='4 clips',aria='4 clips cover the stick')
ers=row_svg('Erasers',[(8,1,ERASER,'solid')],U,200,after='8 erasers',aria='8 erasers cover the stick')
body=h2('Bigger unit, smaller number')+card(p('1 clip is as long as 2 erasers. We measure one stick with both.',38,700))
body+=pin(128,350,1000,stick)+pin(128,440,1000,clips,'rise')+pin(128,530,1000,ers,'rise')
body+=pin(1180,350,612,p('Same stick! Each clip covers 2 erasers, so we need fewer clips.',34,700),'fade',SOFT,20,'22px 26px')
body+=qrow(128,680,1250,'Your turn:','A path is 5 of Tom\'s steps or 7 of Sue\'s steps. Who takes bigger steps?',34)+answer(1420,680,372,'Tom')
put('l9-teachunit',sec('l9-teachunit','53–55 MIN',body,'Teach before worksheet page 2 (Q3 and Q4). 1 clip = 2 erasers here and on the worksheet. Use real clips and erasers if you have them (or draw). Click 1: the clips. Click 2: the erasers. Ask: "Is the stick longer when we use erasers?" (No, it is the same stick.) Click 3. Think-aloud: "A bigger unit covers more of the stick each time, so I need fewer of them. A smaller unit gives a bigger number." Your turn: write it on your own paper, then click. "Tom needs fewer steps for the same path, so each of his steps is bigger." Do not tell them the Q3 answer: it is the same idea with hand spans.'))

# ---------- teach: change unit both ways ----------
U=50
L1=row_svg('clips',[(4,2,CLIP,'clip')],U,140,aria='Rope 4 clips long',lab_size=30)
L2=row_svg('erasers',[(8,1,ERASER,'solid')],U,140,aria='The same rope is 8 erasers long',lab_size=30)
R1=row_svg('erasers',[(6,1,ERASER,'solid')],U,140,aria='Book 6 erasers long',lab_size=30)
R2=row_svg('clips',[(3,2,CLIP,'clip')],U,140,aria='The same book is 3 clips long',lab_size=30)
body=h2('Change the unit: both ways')+card(p('1 clip is as long as 2 erasers.',40,700),SOFT)
body+=pin(128,365,800,p('Clips to erasers: a rope is 4 clips long.',34,800,TEAL))
body+=pin(128,430,800,L1)+pin(128,510,800,L2,'rise')
body+=step('A','Each clip is 2 erasers: 2, 4, 6, 8. The rope is 8 erasers long.',left=128,top=610,width=800,size=32)
body+=pin(992,365,800,p('Erasers to clips: a book is 6 erasers long.',34,800,TEAL))
body+=pin(992,430,800,R1)+pin(992,510,800,R2,'rise')
body+=step('B','Put the erasers in groups of 2: 2, 4, 6. That is 3 groups, so the book is 3 clips long.',left=992,top=610,width=800,size=32)
body+=pin(128,810,1664,p('To a smaller unit: the number gets bigger. To a bigger unit: the number gets smaller.',32,700),'fade',SOFT,20,'16px 28px')
put('l9-teachconv',sec('l9-teachconv','55–57 MIN',body,'Teach before worksheet page 2 (Q4 goes both ways). Left side, click 1: draw 2 erasers under each clip. Click 2: count in 2s along the erasers: 2, 4, 6, 8. Think-aloud: "4 clips, and every clip is 2 erasers, so 2 and 2 and 2 and 2: 8 erasers." Right side, click 3: ring the erasers in 2s. Click 4: "6 erasers make 3 groups of 2, so 3 clips. I check: 2 + 2 + 2 = 6." Click 5: the summary. Ask: "Changing to erasers, did the number get bigger or smaller? Why?" The teaching slides and the worksheet both use 1 clip = 2 erasers, so the worksheet Q4 is the same method (5 clips; 12 erasers).'))
put('l9-tryconv',try_slide('l9-tryconv','57–58 MIN','Your turn: change the unit','Draw the bars. Count in groups.',[('a','1 clip = 3 erasers. A ribbon is 5 clips long. How many erasers?','15 erasers'),('b','1 clip = 3 erasers. A pen is 9 erasers long. How many clips?','3 clips'),('c','1 straw = 2 cubes. A tray is 8 cubes long. How many straws?','4 straws')],'Whiteboards. a) 3, 6, 9, 12, 15: 15 erasers. b) Groups of 3: 3, 6, 9 is 3 groups, so 3 clips. Check 3 + 3 + 3 = 9. c) Groups of 2: 2, 4, 6, 8 is 4 groups, so 4 straws. Ask after b: "Erasers to clips: bigger unit, so is the number bigger or smaller?"',34))

# ---------- teach: longer than / shorter than ----------
U=60
rr=row_svg('Red',[(7,1,ROPE_R,'solid')],U,170,after='7',aria='Red ribbon 7 cubes')
bb=row_svg('Blue',[(7,1,ROPE_B,'solid'),(2,1,None,'dashT')],U,170,after='7 + 2 = 9',aria='Blue ribbon: 2 cubes longer than red')
gg=row_svg('Green',[(4,1,GREEN,'solid'),(3,1,None,'dashR')],U,170,after='7 − 3 = 4',aria='Green ribbon: 3 cubes shorter than red')
body=h2('Longer than, shorter than',64)+card(p('A red ribbon is 7 cubes. Blue is 2 cubes longer than red. Green is 3 cubes shorter than red.',38,700))
body+=pin(128,420,1664,rr)+pin(128,510,1664,bb,'rise')+pin(128,600,1664,gg,'rise')
body+=pin(128,710,1664,p('All three end to end: 7 + 9 + 4 = 20 cubes.',38,700),'fade',WHITE,20,'20px 30px')
body+=pin(128,815,1664,p('Read "than red": start from red\'s bar each time.',32,700),'fade',SOFT,20,'14px 28px')
put('l9-teachmore',sec('l9-teachmore','58–59 MIN',body,'Teach before worksheet page 2 (Q5). Click to build each bar; before each click ask "Longer or shorter than red? By how much?" Think-aloud: "Blue is 2 longer than red, so I draw red\'s 7 and 2 more: 9. Green is 3 shorter than red, so I draw red\'s 7 and cross off 3: 4. End to end: 7 + 9 = 16, and 4 more is 20." Common mistake: adding 7 + 2 + 3 for the total, using the differences instead of the lengths.'))

put('l9-ws2',ws_preview('l9-ws2','59–67 MIN','Worksheet page 2: on your own',[('Q3','Hand spans. Measure the desk with big paper clips, then small cubes: which needs fewer?'),('Q4','Clips and erasers, both ways. Draw the bars and count in groups.'),('Q5','Three pencils. Start from Mei\'s pencil each time.'),('Q6','Use your ruler: a pencil from 0 to 12 cm, a crayon from 3 to 8 cm (put a finger on 3 and hop to 8, counting each space), and measure your own pencil.')],'Finished early? Stretch and Challenge come next.','Children work alone. Note who needs a short catch-up next lesson. Q4: the worksheet says 1 clip = 2 erasers (not 3 as in our teaching), so check children use groups of 2.'))
put('l9-ws2ans',check_slide('l9-ws2ans','67–70 MIN','Page 2: check together',[('Q3','Ali\'s span is longer: he needs fewer spans for the same desk.'),('Q4','a) 10 erasers   b) 6 clips'),('Q5','a) 11 cubes   b) 6 cubes   c) 25 cubes'),('Q6','a) 12 cm    b) 5 cm (8 − 3)    c) Open: check against their own ruler.')],'Click each answer after a child explains. Q3: 6 spans and 8 spans for the same desk; fewer spans means each one covers more, so Ali\'s hand span is longer. Q4a: 5 clips, each 2 erasers: 2, 4, 6, 8, 10. Q4b: 12 erasers in groups of 2: 2, 4, 6, 8, 10, 12 is 6 groups, so 6 clips. Q5: Ali 8 + 3 = 11, Ben 8 − 2 = 6, together 8 + 11 + 6 = 25. Q6: b) count the spaces from 3 to 8, or 8 − 3 = 5; a child who writes 8 has read the end mark only. Each child needs a cm ruler.'))

# ---------- stretch (new) ----------
st=[('1.','A crayon lies from the 3 cm mark to the 11 cm mark on a ruler. How long is it?'),('2.','A pencil is 3 erasers long. A ruler is 2 pencils long. A desk is 4 rulers long. How many erasers long is the desk?'),('3.','A ribbon 15 cubes long is cut into 3 equal pieces. How long is each piece? How many cuts?')]
put('l9-stretch',sec('l9-stretch','For early finishers',h2('Stretch')+''.join(card(p(f'<span style="color:#1F7A6F">{a}</span>  {E(b)}',36,600,raw=True)) for a,b in st),'For children who finish early. Answers: 1) 8 cm, not 11 (count the spaces from 3 to 11, or 11 − 3 = 8). 2) 24 erasers (a ruler is 3 + 3 = 6 erasers; a desk is 6 + 6 + 6 + 6 = 24). 3) 5 cubes each (5 + 5 + 5 = 15) and 2 cuts: 3 pieces need only 2 cuts. Let them check 3 with a cube strip and scissors or by drawing.'))

# ---------- challenge walk-through ----------
body=h2('Challenge: walk-through')+pin(128,250,800,p('Q1: one pencil at a time',38,800,TEAL))
for i,t in enumerate(['Mei: 2 shorter than Ali.  9 − 2 = 7 cubes','Ben: 3 longer than Mei.  7 + 3 = 10 cubes','Together: 9 + 7 + 10 = 26 cubes ✓']): body+=pin(128,330+i*120,800,p(t,32),'rise',WHITE)
body+=pin(992,250,800,p('Q2: make the pieces equal',38,800,TEAL))
for i,t in enumerate(['Move the extra 4 from the first piece to the third. Now all three are the same.','Three equal pieces make 30: 10 + 10 + 10 = 30.','First 10 + 4 = 14, second 10, third 10 − 4 = 6.','Check: 14 + 10 + 6 = 30 ✓']): body+=pin(992,330+i*135,800,p(t,32),'rise',WHITE)
put('l9-chwalk',sec('l9-chwalk','Challenge',body,'Use after pairs have tried. Q1: the trap is Ben, who is compared with Mei, not Ali: find Mei first. Q2: the first piece has 4 extra and the third is missing 4, so moving 4 from the first to the third makes them equal. Then try equal pieces: 9 + 9 + 9 = 27 is too small, 10 + 10 + 10 = 30 ✓. Use a strip of 30 cubes to act it out.'))

# ---------- exit ticket: check the new ruler skill ----------
ex=os.path.join(D,'slides','l9-exit.html'); s=open(ex).read()
a1='A pencil is 8 cubes. A pen is 3 cubes longer. How long is the pen?'; a2='Answer: 11 cubes '
if a1 in s:
    s=s.replace(a1,'A ribbon lies from the 3 cm mark to the 9 cm mark on a ruler. How long is it?').replace(a2,'Answer: 6 cm (count the spaces from 3 to 9, or 9 − 3 = 6). A child who writes 9 has read the end mark only. ')
    open(ex,'w').write(s)


# ---------- kept slides: accessibility and minimum text size ----------
import re
def tidy(sid,labels,fix_fonts=False):
    f=os.path.join(D,'slides',sid+'.html'); s=open(f).read(); k=iter(labels)
    s=re.sub(r'<svg (?!aria-label)',lambda m:f'<svg aria-label="{next(k)}" ',s)
    if fix_fonts: s=s.replace('font-size="22"','font-size="26"').replace('font-size="24"','font-size="25"')
    open(f,'w').write(s)
tidy('l9-explore1',['A pencil measured with a row of cubes, starting exactly at the tip'])
tidy('l9-chdiag',['Three pencils drawn as cube bars: Ali 9, Mei 2 shorter, Ben 3 longer than Mei','A 30-cube ribbon cut into three pieces shown as bars'],True)
for i,h in S.items(): open(os.path.join(D,'slides',i+'.html'),'w').write(h)
for old in ['l9-mini1','l9-mini2']:
    f=os.path.join(D,'slides',old+'.html')
    if os.path.exists(f): os.remove(f)
t=os.path.join(D,'slides','l9-title.html'); s=open(t).read()
for a,b in [('mini-lesson 25 to 35, brain break 35 to 40, worksheet 40 to 70','teaching 25 to 35 (click to reveal each step and answer), brain break 35 to 40, worksheet 40 to 70 with short teaching before each page and a check-together slide after it'),
            ('Measure with equal units, compare lengths, and see why a bigger unit gives a smaller count.</p>','Measure with equal units and a cm ruler, compare lengths, and change from one unit to another.</p>'),
            ('Objective: Compare and order lengths, measure with equal units, and see why a bigger unit gives a smaller count.','Objective: Compare and order lengths, measure with equal units and with a centimetre ruler (also when the object does not start at 0), and change a length from one unit to another in both directions.'),
            ('Materials: Linking cubes or paper cube strips, paper clips, erasers, objects to measure.','Materials: Linking cubes or paper cube strips, paper clips, erasers, objects to measure, a cm ruler for each child, mini whiteboards.')]:
    if a in s: s=s.replace(a,b)
open(t,'w').write(s)
deck=json.load(open(os.path.join(D,'deck.json')))
deck['order']=['l9-title','l9-warm1','l9-warm2','l9-explore1','l9-explore2','l9-teach1','l9-we1','l9-try1','l9-teachcm','l9-we2','l9-try2','l9-key','l9-break','l9-ws1','l9-ws1ans','l9-teachunit','l9-teachconv','l9-tryconv','l9-teachmore','l9-ws2','l9-ws2ans','l9-stretch','l9-challenge','l9-chdiag','l9-chwalk','l9-talk','l9-exit']
deck['sections']={'s1':{'description':'Warm-up and explore','start':'l9-title'},'s2':{'description':'Teach: fair measuring, comparing, and the cm ruler','start':'l9-teach1'},'s3':{'description':'Worksheet with teaching before each page','start':'l9-break'},'s4':{'description':'Stretch, challenge, talk and exit','start':'l9-stretch'}}
json.dump(deck,open(os.path.join(D,'deck.json'),'w'),indent=1,ensure_ascii=False)
print(len(deck['order']),'slides; wrote',len(S))

import p1gifted; p1gifted.apply(D,9)
import p1gaps; p1gaps.apply(D,9)
import p1fix
p1fix.finish(D,9,{'l9-ws1':'40–50 MIN','l9-ws1ans':'50–52 MIN','l9-teachunit':'52–54 MIN','l9-teachconv':'54–56 MIN','l9-tryconv':'56–57 MIN','l9-teachmore':'57–58 MIN','l9-ws2':'58–68 MIN'})
import p1neutral; p1neutral.apply(D,9)
import p1budget; p1budget.apply(D,9)
