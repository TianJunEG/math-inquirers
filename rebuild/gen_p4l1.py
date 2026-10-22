"""Math Inquirers P4, Lesson 1: Factor Hunters. Writes split/p4l1/project (deck.json + slides/*.html)."""
import json,os,sys,datetime
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,H)
import slidekit
from slidekit import *
slidekit.FOOT='Math Inquirers P4 Holiday Program  •  Notice it. Test it. Explain why.'
D=os.path.join(H,'..','split','p4l1','project'); os.makedirs(os.path.join(D,'slides'),exist_ok=True)
S={}
def put(i,h): S[i]=h
RED='#D64545'; FOOTX=slidekit.FOOT

# ---------- shared slide shapes (same look as the P1 and P2 decks) ----------
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
def tryq(sid,time,title,sub,rows,notes,qw=1250,size=38,top=340,gapy=150):
    body=h2(title)+p(sub,34,600,MUTED)
    for i,(a,b,c) in enumerate(rows):
        body+=qrow(128,top+i*gapy,qw,a,b,size)+answer(128+qw+40,top+i*gapy,1664-qw-40,c)
    return sec(sid,time,body,notes)
def svgwrap(w,h,label,inner):
    return f'<svg aria-label="{E(label)}" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="width:{w}px;height:{h}px;flex:none">{inner}</svg>'
def txt(x,y,s,size=40,fill=NAVY,anchor='middle',weight=700,font='Fredoka, Arial'):
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" fill="{fill}" font-family="{font}">{E(str(s))}</text>'
def line(left,top,width,text,build='rise',size=32,bg=WHITE):
    return pin(left,top,width,p(text,size,700),build,bg,16,'10px 24px')

# ---------- 1. title ----------
put('p4l1-title',title_slide('p4l1-title','LESSON 1  •  WEEK 1','Factor Hunters','Factors and multiples',
 'Hunt down every factor of a number, use common factors and common multiples to solve puzzles, and crack multiple riddles.',
 'Objective: Find all the factor pairs of a number by working in order, find common factors (sharing into identical packs) and common multiples (when do buses meet again), discover which numbers have an odd number of factors, and solve multiple-based logic riddles. '
 'Thinking strategies taught today: MAKE A LIST IN ORDER, LOOK FOR A PATTERN and USE THE CLUES ONE AT A TIME. '
 'Materials: 36 square tiles or squared paper per pair, mini whiteboards, coloured pencils, a 1 to 50 number strip. '
 'Online: children cut 24 paper squares (or use squared paper) before the lesson and build rectangles on camera; the tutor marks the bus time line and the factor rainbow on the slides. '
 'Time plan: Warm-up check 1 to 4 (two questions on the key idea; children who get both right and can say why start on the Think Harder pages at minute 34), warm-up game 4 to 6 (one short round), quick questions 6 to 8, explore 8 to 18, teaching 18 to 30 (click to reveal each step and answer; the "your turn" slides are optional, skip them if short of time), brain break 30 to 34, worksheet page 1 from 34 to 50 and check together 50 to 53, short teaching before page 2 from 53 to 58, worksheet page 2 from 58 to 76 and check together 76 to 80, talk time 80 to 85, exit ticket 85 to 88, What was hard? reflection 88 to 90. The Challenge slides and the Think Harder pages are for early finishers and for take-home: they have no fixed time slot. Online: page 1 is pair work, so allow about 2 minutes to move into and out of breakout rooms (or run page 1 as a whole-group screen-share if there are only 8 children).'))

# ---------- 2. warm-up game: Fizz-Buzz ----------
BW,BH,GX,GY=120,100,8,130
def box_xy(n): i=n-1; return 10+(i%12)*(BW+GX), 10+(i//12)*GY
base=''.join(f'<rect x="{box_xy(n)[0]}" y="{box_xy(n)[1]}" width="{BW}" height="{BH}" rx="14" fill="{WHITE}" stroke="{NAVY}" stroke-width="4"/>'+txt(box_xy(n)[0]+BW/2,box_xy(n)[1]+66,n,48) for n in range(1,25))
fizz=''.join(f'<rect x="{box_xy(n)[0]+8}" y="{box_xy(n)[1]+8}" width="{BW-16}" height="{BH-16}" rx="10" fill="none" stroke="{TEAL}" stroke-width="7"/>' for n in range(3,25,3))
buzz=''.join(f'<line x1="{box_xy(n)[0]+18}" y1="{box_xy(n)[1]+BH+12}" x2="{box_xy(n)[0]+BW-18}" y2="{box_xy(n)[1]+BH+12}" stroke="{RED}" stroke-width="9" stroke-linecap="round"/>' for n in range(4,25,4))
both=''.join(f'<rect x="{box_xy(n)[0]}" y="{box_xy(n)[1]}" width="{BW}" height="{BH}" rx="14" fill="{YEL}" stroke="{NAVY}" stroke-width="4"/>'+txt(box_xy(n)[0]+BW/2,box_xy(n)[1]+66,n,48) for n in (12,24))
W2,H2=1550,250
body=h2('Warm-up: Fizz-Buzz')+card(p('Count round the group. Multiple of 3: say <b style="color:#1F7A6F">Fizz</b>. Multiple of 4: say <b style="color:#D64545">Buzz</b>. Both: say <b>Fizz-Buzz</b>!',38,600,raw=True))
body+=pin(128,420,W2,svgwrap(W2,H2,'Number boxes 1 to 24 in two rows',base),None)
body+=pin(128,420,W2,svgwrap(W2,H2,'Multiples of 3 outlined in teal',fizz),'fade')
body+=pin(128,420,W2,svgwrap(W2,H2,'Multiples of 4 underlined in red',buzz),'fade')
body+=pin(128,420,W2,svgwrap(W2,H2,'12 and 24 filled yellow',both),'pop')
body+=pin(128,740,1664,p('Fizz-Buzz numbers: 12 and 24. They are common multiples of 3 and 4. What comes next? (36)',36,700),'fade',SOFT,20,'20px 30px')
put('p4l1-warm1',sec('p4l1-warm1','4–6 MIN',body,
 'Minutes 4 to 6 (one short round, about 2 minutes: the Warm-up check came first). Fizz-Buzz. Count round the group (online: in the order of the video tiles), one number each. A multiple of 3 is "Fizz", a multiple of 4 is "Buzz", a multiple of both is "Fizz-Buzz". A child who slips just says "my go again" and carries on: no one is out and nobody is counted. Go to 40 if it is going well. '
 'Before you start, ask for a prediction: "Which number will be the first Fizz-Buzz?" Then click: the teal boxes are the multiples of 3, the red lines the multiples of 4, and yellow shows the numbers in both: 12 and 24. Ask: "What is the next Fizz-Buzz? How do you know without counting?" (36: they go up in 12s). '
 'Introduce the words: 12 is a MULTIPLE of 3 and of 4, so it is a COMMON MULTIPLE. That idea comes back with the buses later.'))

# ---------- 3. quick questions ----------
qs=[('1.','Is 7 a factor of 56?','Yes: 7 × 8'),('2.','The first five multiples of 6?','6, 12, 18, 24, 30'),('3.','A common multiple of 4 and 6?','12, 24, 36 …'),('4.','Is 45 a multiple of 4?','No'),('5.','Write 18 as a product: 3 ways.','1×18, 2×9, 3×6')]
body=h2('Quick questions')+''.join(qrow(128,250+i*125,1100,a,b) for i,(a,b,c) in enumerate(qs))+''.join(answer(1268,250+i*125,524,c) for i,(a,b,c) in enumerate(qs))
put('p4l1-warm2',sec('p4l1-warm2','6–8 MIN',body,'Minutes 6 to 8. Read each aloud, whiteboards up together, then click to show. Ask after 1: "Is 56 a factor of 7 too?" (No: a factor goes INTO the number; 56 is a multiple of 7.) After 3: "Is there a smaller common multiple than 24?" (12). After 4: 44 and 48 are the multiples of 4 around 45, so 45 is not one. After 5: "Did anyone find a fourth way?" (no: after 3 × 6 the next would be 6 × 3, the same pair turned round). Answers: yes, 6 12 18 24 30, 12 (or 24, 36), no, 1 × 18 / 2 × 9 / 3 × 6.'))

# ---------- 4. explore: what to do ----------
DASH=' stroke-dasharray="6 5"'
def tiles(x0,y0,rows,cols,s=34,fill=YEL,dash=False):
    g=''
    for r in range(rows):
        for c in range(cols):
            g+=f'<rect x="{x0+c*s}" y="{y0+r*s}" width="{s}" height="{s}" fill="{fill}" stroke="{NAVY}" stroke-width="3"{DASH if dash else ""}/>'
    return g
g=tiles(40,40,3,8)+txt(176,180,'3 × 8 = 24',34,TEAL)+tiles(470,20,6,12,24,WHITE,True)+txt(770,190,'next rectangle?',30,MUTED,weight=600,font='Nunito Sans, Arial')
g+=f'<rect x="1000" y="30" width="560" height="150" rx="18" fill="{SOFT}" stroke="{NAVY}" stroke-width="4"/>'+txt(1280,95,'Use ALL 24 tiles.',34)+txt(1280,145,'How many rectangles?',32,TEAL)
steps=''.join(f'<li>{E(s)}</li>' for s in ['Take 24 square tiles.','Use ALL the tiles to make a rectangle. Write it as a multiplication, like 2 × 12.','Make as many different rectangles as you can. A 2 by 12 and a 12 by 2 count as the same.','How do you know you have found them all?'])
body=h2('Explore: what to do')+card(chip('EXPLORE')+f'<ol style="font-size:34px;font-weight:600;padding-left:52px;display:flex;flex-direction:column;gap:6px">{steps}</ol>')
body+=card(svgwrap(1600,210,'24 tiles in 3 rows of 8, and an empty grid for the next rectangle',g),extra='padding:20px 32px')
put('p4l1-explore1',sec('p4l1-explore1','8–13 MIN',body,'Minutes 8 to 13. Pairs build rectangles with 24 tiles (online: paper squares or squared paper on camera). Ask for a prediction first: how many rectangles? Most guess too many or too few. Let them build in any order at first; the teaching part shows how to work in order. Early finishers: do it again with 36 tiles. Something special happens (a 6 by 6 square). What is it?'))

# ---------- 5. explore: talk ----------
body=h2('Explore: talk about it')+numcards([('1.','How many different rectangles did you make with 24 tiles?'),('2.','How do you know you have found them all?'),('3.','What do the side lengths tell us about the number 24?')],40)
put('p4l1-explore2',sec('p4l1-explore2','13–18 MIN',body,'Minutes 13 to 18. Let pairs keep working, then gather. Collect the rectangles in the order children say them, then ask: "Is anything missing? Is anything there twice?" Answers: 1) 4 rectangles: 1 × 24, 2 × 12, 3 × 8, 4 × 6. 2) Try 1, 2, 3, 4, 5, 6 rows in order. 5 rows does not work (24 is not in the 5 times table). 6 rows is the 4 × 6 turned round, so we can stop. 3) The side lengths are the factors of 24: 1, 2, 3, 4, 6, 8, 12, 24. With 36 tiles there are 5 rectangles, and one is a square (6 × 6). Do NOT teach the rainbow yet: the next slides do.'))

# ---------- 6. teach: factors and multiples ----------
g=''
for r in range(3):
    for c in range(8): g+=f'<circle cx="{40+c*70}" cy="{40+r*70}" r="26" fill="{TEAL}" stroke="{NAVY}" stroke-width="3"/>'
g+=txt(280,250,'3 rows of 8 = 24',34,TEAL)
body=h2('Factors and multiples')+pin(128,250,600,svgwrap(570,270,'24 dots in 3 rows of 8',g),None,WHITE,24,'16px 16px')
body+=pin(800,250,992,p('3 × 8 = 24',64,800),None,SOFT,24,'26px 36px')
body+=step(1,'3 and 8 are <b>factors</b> of 24. They go into 24 exactly.',800,400,992,size=34)
body+=step(2,'24 is a <b>multiple</b> of 3 and of 8. It is in their times tables.',800,530,992,size=34)
body+=step(3,'Is 5 a factor of 24? 24 ÷ 5 = 4 remainder 4. Not this one.',128,680,1664,size=34)
body+=pin(128,790,1664,p('A factor is never bigger than the number. A multiple is never smaller.',34,700),'fade',SOFT,20,'18px 30px')
put('p4l1-teach1',sec('p4l1-teach1','18–20 MIN',body,'Teach. Point at the array: "3 rows of 8 make 24." Click through. Think-aloud: "A factor goes INTO a number with nothing left over. A multiple is what you get when you multiply, so it is in the times table." Ask before step 3: "Is 5 a factor of 24? How could you check?" (divide, or look at the 5 times table: 20, 25; 24 is not there). Last line: a quick way to catch a mix-up. 24 has factors up to 24, and multiples from 24 upwards.'))

# ---------- 7. worked example: factor pairs of 36 ----------
body=h2('Worked example: all the factor pairs of 36')+card(p('Find every factor of 36. How do you know you have them all?',38,700))
body+=trow(128,360,['Try','Factor pair'],[150,420],None,True,32)
rows=[('1','1 × 36'),('2','2 × 18'),('3','3 × 12'),('4','4 × 9'),('5','not this one'),('6','6 × 6  stop!')]
for i,(a,b) in enumerate(rows): body+=trow(128,436+i*76,[a,b],[150,420],'rise',False,32)
nums=[1,2,3,4,6,9,12,18,36]; xs=[60+i*112 for i in range(9)]
g=''
for i in range(4):
    a,b=xs[i],xs[8-i]; r=(b-a)/2
    g+=f'<path d="M{a} 220 A{r} {[200,160,120,80][i]} 0 0 1 {b} 220" fill="none" stroke="{[TEAL,RED,YEL,NAVY][i]}" stroke-width="7"/>'
g+=f'<path d="M{xs[4]-30} 220 Q{xs[4]} 140 {xs[4]+30} 220" fill="none" stroke="{TEAL}" stroke-width="7" stroke-dasharray="10 8"/>'
for x,n in zip(xs,nums): g+=f'<circle cx="{x}" cy="250" r="38" fill="{WHITE}" stroke="{NAVY}" stroke-width="4"/>'+txt(x,264,n,36)
body+=pin(780,350,1012,svgwrap(1000,300,'Factor rainbow for 36: 1 joins 36, 2 joins 18, 3 joins 12, 4 joins 9, and 6 sits alone in the middle',g),'fade',WHITE,24,'6px 6px')
body+=pin(780,690,1012,p('Try 1, 2, 3 … in order. Stop when the pairs meet. 36 has 9 factors.',34,700),'fade',SOFT,20,'20px 28px')
put('p4l1-we1',sec('p4l1-we1','20–22 MIN',body,'Make a list in order: today\'s main strategy. Click to add each row while children say it first on whiteboards. Think-aloud: "1 × 36. 2 goes into 36: 2 × 18. 3 × 12. 4 × 9. Does 5 go into 36? No, 36 is not in the 5 times table, so I skip it. 6 × 6. The next number to try is 7, then 8, then 9, but 9 is already in my list (4 × 9). The pairs have met, so I stop." Then click for the factor rainbow: each arch joins a factor pair. 6 has no partner because 6 × 6 uses it twice, so 36 has an odd number of factors (9). We come back to that before page 2.'))

# ---------- 8. your turn ----------
put('p4l1-try1',tryq('p4l1-try1','22–23 MIN • OPTIONAL','Your turn: whiteboards','Write the factor pairs in order first. Then list the factors.',[('a','All the factors of 20?','1, 2, 4, 5, 10, 20'),('b','How many factors does 30 have?','8'),('c','All the factors of 16?','1, 2, 4, 8, 16')],
 'Whiteboards up together, then click. a) 1 × 20, 2 × 10, 4 × 5 (3 does not go in). b) 1 × 30, 2 × 15, 3 × 10, 5 × 6: 8 factors. c) 1 × 16, 2 × 8, 4 × 4: only 5 factors, because 4 × 4 uses 4 twice. Ask: "Why does 16 have an odd number of factors?" Do not explain fully yet; just notice it.',qw=1000))

# ---------- 9. worked example: common factors ----------
body=h2('Worked example: identical bags')+card(p('12 apples and 18 oranges go into identical bags, with none left over. What is the greatest number of bags?',38,700))
body+=step(1,'Factors of 12:  1, 2, 3, 4, 6, 12.     Factors of 18:  1, 2, 3, 6, 9, 18.',top=420,size=34)
body+=step(2,'The number of bags must be a factor of BOTH. Common factors: 1, 2, 3, 6.',top=520,size=34)
body+=step(3,'Greatest: 6 bags. Each bag: 12 ÷ 6 = 2 apples, 18 ÷ 6 = 3 oranges.',top=620,size=34)
g=''
for b in range(6):
    x=10+b*265
    g+=f'<path d="M{x+20} 40 L{x+230} 40 L{x+215} 170 L{x+35} 170 Z" fill="{SKY}" stroke="{NAVY}" stroke-width="4" stroke-linejoin="round"/>'
    for k in range(2): g+=f'<circle cx="{x+75+k*50}" cy="80" r="20" fill="{RED}" stroke="{NAVY}" stroke-width="3"/>'
    for k in range(3): g+=f'<circle cx="{x+60+k*50}" cy="132" r="20" fill="#F28C38" stroke="{NAVY}" stroke-width="3"/>'
body+=pin(128,730,1664,svgwrap(1600,180,'6 identical bags, each with 2 apples and 3 oranges',g),'fade')
put('p4l1-we2',sec('p4l1-we2','23–26 MIN',body,'Teach before worksheet page 1 (Q3 is the same kind of puzzle). Ask first: "Could we use 4 bags?" (4 goes into 12 but not into 18: 2 oranges would be left over). Click through. Think-aloud: "Every bag is the same, and nothing is left over, so the number of bags must go into 12 exactly AND into 18 exactly. That is a common factor." Click the bags to check: 6 × 2 = 12 apples, 6 × 3 = 18 oranges.'))

# ---------- 10. worked example: buses (common multiples) ----------
L0,UX=40,32  # minute 0 at x=40, 33 px per minute
base=f'<line x1="{L0}" y1="120" x2="{L0+48*UX+20}" y2="120" stroke="{NAVY}" stroke-width="5"/>'
for m in range(49):
    big=m in (0,6,8,12,16,18,24,30,32,36,40,42,48)
    base+=f'<line x1="{L0+m*UX}" y1="{108 if big else 113}" x2="{L0+m*UX}" y2="{132 if big else 127}" stroke="{NAVY}" stroke-width="{4 if big else 2}"/>'
    if big: base+=txt(L0+m*UX,170,m,28)
base+=txt(L0+48*UX+64,130,'min',28,MUTED,weight=600,font='Nunito Sans, Arial')
six=''.join(f'<path d="M{L0+a*UX} 104 Q{L0+(a+3)*UX} 30 {L0+(a+6)*UX} 104" fill="none" stroke="{TEAL}" stroke-width="5"/>' for a in range(0,48,6))
eight=''.join(f'<path d="M{L0+a*UX} 186 Q{L0+(a+4)*UX} 270 {L0+(a+8)*UX} 186" fill="none" stroke="{RED}" stroke-width="5"/>' for a in range(0,48,8))
hi=''.join(f'<circle cx="{L0+m*UX}" cy="160" r="30" fill="none" stroke="{YEL}" stroke-width="8"/>' for m in (24,48))
WB,HB=1700,280
body=h2('Worked example: when do the buses meet?')+card(p('Bus A leaves every 6 minutes. Bus B leaves every 8 minutes. Both leave at 7:00 am. When do they next leave together?',36,700))
body+=pin(110,400,WB,svgwrap(WB,HB,'Time line from 0 to 48 minutes',base),None)
body+=pin(110,400,WB,svgwrap(WB,HB,'Jumps of 6 above the line: 6, 12, 18, 24, 30, 36, 42, 48',six),'fade')
body+=pin(110,400,WB,svgwrap(WB,HB,'Jumps of 8 below the line: 8, 16, 24, 32, 40, 48',eight),'fade')
body+=pin(110,400,WB,svgwrap(WB,HB,'24 and 48 circled: both buses',hi),'pop')
body+=pin(128,700,1664,p('Bus A: 6, 12, 18, <b>24</b>, 30 …     Bus B: 8, 16, <b>24</b>, 32 …',36,600,raw=True),'rise',WHITE,20,'16px 28px')
body+=answer(128,800,1664,'First number in both lists: 24. They meet again at 7:24 am.')
put('p4l1-we3',sec('p4l1-we3','26–28 MIN',body,'Click to draw the jumps of 6 (teal, above), then the jumps of 8 (red, below), then circle where both land. Think-aloud: "Bus A leaves at 6, 12, 18, 24 minutes past 7. Bus B at 8, 16, 24. The first number in both lists is 24, the smallest common multiple of 6 and 8." Ask: "Ravi says 6 × 8 = 48, so they meet at 7:48. Is he right?" (They DO meet at 48, but they meet first at 24. Multiplying gives a common multiple, not always the first one.)'))

# ---------- 11. your turn: common multiples ----------
put('p4l1-try2',tryq('p4l1-try2','28–29 MIN • OPTIONAL','Your turn: when do they meet?','List the multiples of each number. Find the first one in both lists.',[
 ('a','Two lights blink every 4 s and every 6 s. They blink together now. Next time together?','after 12 s'),
 ('b','Mei swims every 4 days and goes to the library every 10 days. Both today. Both again in?','20 days'),
 ('c','The smallest number that is a multiple of both 3 and 5?','15')],
 'Whiteboards. a) 4, 8, 12 and 6, 12: 12 seconds (not 24). b) 4, 8, 12, 16, 20 and 10, 20: 20 days (not 40). c) 3, 6, 9, 12, 15 and 5, 10, 15: 15. Ask a child to explain why b is not 40.',qw=1260,size=34,gapy=160))

# ---------- 12. key ----------
body=h2('Key idea: hunt in order')+card(p('Factors: try 1, 2, 3 … in order until the pairs meet. Multiples: list them and look for the first number in both lists.',44,700))+card(p('A factor goes into a number exactly. A multiple is in its times table.',38,600,MUTED))
put('p4l1-key',sec('p4l1-key','29–30 MIN',body,'Say the key idea together. Common mistakes to watch for during the worksheet: (1) Listing factors at random and missing one, or stopping too early (for 48, forgetting 6 × 8), instead of trying 1, 2, 3 … in order until the pairs meet. (2) Mixing up factors and multiples: saying 12 is a factor of 4. (3) For common multiples, multiplying the two numbers every time (10 × 15 = 150 minutes) instead of listing the multiples to find the first one they share (30).'))
put('p4l1-break',break_slide('p4l1-break','30–34 MIN','Factor freeze. I call a number. Stand up if 10 is a factor of it, sit down if not. Then we change 10 to 3, 4 and 5.','Four minutes. Call numbers such as 30, 45, 60, 100, 72, 15. Online: hands up for stand, hands down for sit. Ask: "Which numbers made everyone stand for 3, 4 AND 5?" (60: a common multiple of 3, 4 and 5).'))

# ---------- worksheet page 1 ----------
put('p4l1-ws1',ws_preview('p4l1-ws1','34–50 MIN','Worksheet page 1: with your partner',[('Q1','Every factor of 48. Try 1, 2, 3 … in order until the pairs meet.'),('Q2','40 trees in equal rows. Find every way.'),('Q3','18 red beads and 24 blue beads in identical packs. Use common factors.')],'Stuck? Draw the rectangles, or build them with tiles.','Minutes 34 to 50. Walk around. Ask "How do you know you have them all?" before giving any help. Q2 is the rectangles idea again, but the stem now says 2 rows of 20 and 20 rows of 2 are different ways to plant (unlike the explore, where a turned rectangle did not count), so both count. Point children to that sentence. Q3c: check that each pack has the same number of each colour.'))
put('p4l1-ws1ans',checks('p4l1-ws1ans','50–53 MIN','Page 1: check together',[('Q1','a) 1×48, 2×24, 3×16, 4×12, 6×8   b) 1, 2, 3, 4, 6, 8, 12, 16, 24, 48   c) 10 factors; after 6 × 8 the pairs meet'),('Q2','6 ways: 2 rows of 20, 4 of 10, 5 of 8, 8 of 5, 10 of 4, 20 of 2'),('Q3','a) 1, 2, 3, 6, 9, 18  and  1, 2, 3, 4, 6, 8, 12, 24   b) 1, 2, 3, 6   c) 6 packs: 3 red, 4 blue')],
 'Click each answer after a pair explains theirs. Q1c: 7 does not go into 48 and the next factor, 8, is already in the pair 6 × 8. Q2: the rows can be 2, 4, 5, 8, 10 or 20 (factors of 40 apart from 1 and 40). Q3: 18 ÷ 6 = 3 red and 24 ÷ 6 = 4 blue in each pack.',gapy=180,size=32))

# ---------- teach: odd number of factors ----------
body=h2('Count the factors: odd or even?')
body+=pin(128,240,800,p('Factor pairs of 100',36,800,TEAL))
for i,t in enumerate(['1 × 100','2 × 50','4 × 25','5 × 20','10 × 10']): body+=line(128,310+i*68,800,t)
body+=pin(992,240,800,p('Factor pairs of 18',36,800,TEAL))
for i,t in enumerate(['1 × 18','2 × 9','3 × 6']): body+=line(992,310+i*68,800,t)
body+=pin(992,530,800,p('18: 3 pairs, 6 factors (even). 100: 9 factors (odd)!',32,700),'fade',SOFT,16,'14px 24px')
body+=pin(128,680,1664,p('10 × 10 uses 10 twice, so 10 is counted once. A number times itself has an ODD number of factors.',34,700),'fade',SOFT,20,'16px 28px')
body+=qrow(128,800,1100,'Your turn:','How many factors does 81 have?',34)+answer(1268,800,524,'5: 1, 3, 9, 27, 81')
put('p4l1-teachodd',sec('p4l1-teachodd','53–55 MIN',body,'Teach before worksheet page 2 (Q5 counts factors). Click to list the pairs of 100 and of 18. Ask: "Count the factors of 100. Why is it odd when every factor has a partner?" (10 is its own partner). Numbers like 4, 9, 16, 25, 36, 100 are a number times itself, called square numbers: they make square arrays, like the 6 by 6 square from the explore. 81 = 9 × 9: pairs 1 × 81, 3 × 27, 9 × 9, so 5 factors. Do not list the numbers with exactly 3 factors: that is Q5c.'))

# ---------- teach: multiple riddles ----------
body=h2('Multiple riddles: one clue at a time')+card(p('I am a number between 40 and 80. I am a multiple of 3 and a multiple of 5. I am even. Who am I?',38,700))
body+=step(1,'Multiple of 3 AND 5: count in 15s.  15, 30, 45, 60, 75, 90',top=420,size=34)
body+=step(2,'Between 40 and 80:  45, 60, 75',top=520,size=34)
body+=step(3,'Even:  only 60.   Check every clue: 60 = 3 × 20 = 5 × 12 ✓',top=620,size=34)
body+=pin(128,740,1664,p('Tip: list the multiples of the bigger number, then cross out any that do not fit the next clue.',34,700),'fade',SOFT,20,'18px 30px')
put('p4l1-teachriddle',sec('p4l1-teachriddle','55–56 MIN',body,'Teach before worksheet page 2 (Q6a). Use the clues one at a time and make a list. Ask before step 1: "Which numbers are multiples of both 3 and 5?" Some children will list the 3s and the 5s and circle the numbers in both; that works too. Think-aloud: "After each clue my list gets shorter. When only one number is left, I check it against EVERY clue."'))

# ---------- teach: one example can show it is wrong ----------
body=h2('Always true? Test it!')+card(p('Ben says: "Every multiple of 4 is even." Siti says: "Every even number is a multiple of 4."',38,700))
body+=step(1,'Test Ben: 4, 8, 12, 16, 20 … all even. 4 = 2 × 2, so the 4s are all in the 2s. Ben is right.',top=420,size=34)
body+=step(2,'Test Siti: 2? 6? 6 is even, but 6 is not in the 4 times table.',top=540,size=34)
body+=answer(128,650,1664,'Siti is wrong. ONE example that does not work is enough to show it.')
put('p4l1-teachtest',sec('p4l1-teachtest','56–58 MIN',body,'Teach before worksheet page 2 (Q6b asks who is right). Ask the group to vote before clicking. Think-aloud: "To show something is ALWAYS true I need a reason, like 4 = 2 × 2. To show it is NOT always true I only need one example that breaks it." Ask: "Is every multiple of 10 a multiple of 5? Is every multiple of 5 a multiple of 10?" for children who are quick.'))

# ---------- worksheet page 2 ----------
put('p4l1-ws2',ws_preview('p4l1-ws2','58–76 MIN','Worksheet page 2: on your own',[('Q4','Buses every 10 and 15 minutes. List the times, find when they meet.'),('Q5','Count the factors. Which numbers have exactly 3?'),('Q6','Multiple riddles, then: who is right? Explain with an example.')],'Finished early? Stretch and Challenge come next.','Children work alone. Note who needs a short catch-up next lesson, especially children who still mix up factors and multiples.'))
put('p4l1-ws2ans',checks('p4l1-ws2ans','76–80 MIN','Page 2: check together',[('Q4','a) 6:30 am   b) 5 times: 6:00, 6:30, 7:00, 7:30, 8:00'),('Q5','a) 6: 4,  9: 3,  10: 4,  15: 4,  16: 5,  25: 3   b) 9 and 25: 3 × 3 and 5 × 5   c) Yes: 1, 7, 49 (7 × 7)'),('Q6','a) 36   b) Ravi. 6 = 2 × 3. But 9 is a multiple of 3 and not of 6, so Mei is wrong.')],
 'Click after a child explains. Q4: Bus 33 at :00, :10, :20, :30; Bus 51 at :00, :15, :30. They meet every 30 minutes. Q5c: 49 = 7 × 7, so its factors are 1, 7 and 49: exactly 3. A number with exactly 3 factors is a number times itself where that number has only 2 factors: 2 × 2, 3 × 3, 5 × 5, 7 × 7. 16 = 4 × 4 has 5 factors, and 36 has 9. Finding ALL such numbers from 1 to 60 (4, 9, 25, 49) is Think Harder Q4. Q6a: multiples of 12 between 30 and 70 are 36, 48, 60; 48 is a multiple of 8; in 60 the ones digit is smaller than the tens digit.',gapy=180,size=32))

# ---------- stretch / challenge ----------
from p4bank import th_items, th_notes, gf_numbers  # slide Think harder = the printed page (docs/audit/reaudit_fixes_p4.md)
st=th_items(1)
def numgrid(items,size=30): return '<div style="display:grid;grid-template-columns:1fr 1fr;gap:24px;align-items:stretch">'+''.join(card(p(f'<span style="color:{TEAL}">{a}</span>  {E(b)}',size,600,raw=True),extra='padding:24px 32px') for a,b in items)+'</div>'
put('p4l1-stretch',sec('p4l1-stretch','Early finishers / take-home',h2('Think harder')+numgrid(st,34),th_notes(1)))
ch=[('1.','There are 20 closed lockers, numbered 1 to 20. Child 1 opens every locker. Child 2 changes every 2nd locker (opens it if closed, closes it if open). Child 3 changes every 3rd locker, and so on, up to child 20. Which lockers are open at the end?'),('2.','I am a number less than 100. When I am divided by 2, 3, 4, 5 or 6, there is always 1 left over. I am bigger than 1. Who am I?')]
put('p4l1-challenge',sec('p4l1-challenge','Early finishers / take-home',h2('Go further')+numcards(ch,34),'Pairs try first, then use the "see it" slide if stuck, then the walk-through. These are Go further Q7 and Q6. Answers: 1) Lockers 1, 4, 9 and 16: each locker is changed once for every factor of its number, and only numbers with an odd number of factors end up open. 2) 61: one less than the number is a common multiple of 2, 3, 4, 5 and 6, which is 60.'))
g1=''
for i in range(10):
    x=20+i*74
    for r,base_n in enumerate((1,11)):
        y=20+r*150; n=base_n+i
        g1+=f'<rect x="{x}" y="{y}" width="62" height="120" rx="6" fill="{SKY}" stroke="{NAVY}" stroke-width="3"/><circle cx="{x+50}" cy="{y+66}" r="5" fill="{NAVY}"/>'+txt(x+31,y+40,n,26)
g1+=f'<rect x="20" y="330" width="740" height="120" rx="12" fill="{SOFT}" stroke="{NAVY}" stroke-width="3"/>'+txt(390,380,'Locker 6 is changed by children 1, 2, 3, 6.',26,NAVY,font='Nunito Sans, Arial')+txt(390,425,'Open, closed, open, closed …',26,TEAL,font='Nunito Sans, Arial')
g2=''
for i,(k) in enumerate([2,3,4,5,6]):
    x=30+i*146
    g2+=f'<rect x="{x}" y="30" width="126" height="90" rx="12" fill="{WHITE}" stroke="{NAVY}" stroke-width="3"/>'+txt(x+63,88,f'÷ {k}',34)+txt(x+63,160,'1 left',26,RED,font='Nunito Sans, Arial')
g2+=f'<rect x="120" y="220" width="520" height="100" rx="16" fill="{YEL}" stroke="{NAVY}" stroke-width="4"/>'+txt(380,284,'my number − 1  =  ?',36)
g2+=txt(380,380,'Take away the 1 left over …',28,MUTED,weight=600,font='Nunito Sans, Arial')+txt(380,425,'what is left fits 2s, 3s, 4s, 5s, 6s',28,TEAL,font='Nunito Sans, Arial')
body=h2('Go further: see it',60)+'<div style="display:flex;gap:32px;align-items:flex-start">'
body+=card(f'<p style="font-size:30px;font-weight:700;color:{TEAL}">Q1: Who touches each locker?</p>'+svgwrap(780,470,'20 lockers in two rows, and a note that locker 6 is changed by children 1, 2, 3 and 6',g1).replace('width:780px;height:470px;flex:none','width:100%;height:auto;display:block'),extra='flex:1;min-width:0;padding:20px 24px')
body+=card(f'<p style="font-size:30px;font-weight:700;color:{TEAL}">Q2: Always 1 left over</p>'+svgwrap(780,470,'Dividing by 2, 3, 4, 5 and 6 leaves 1 each time; take away the 1',g2).replace('width:780px;height:470px;flex:none','width:100%;height:auto;display:block'),extra='flex:1;min-width:0;padding:20px 24px')+'</div>'
put('p4l1-chdiag',sec('p4l1-chdiag','Early finishers / take-home',body,'Show after pairs have tried the Challenge, or if they are stuck. The pictures show the problem, not the answer. Ask: For Q1, which children touch locker 6? Locker 9? What do those numbers have to do with factors? For Q2, if you take away the 1 that is left over, what kind of number is left? Answers are in the Challenge slide notes.'))
body=h2('Go further: walk-through')+pin(128,250,800,p('Q1: count the changes',38,800,TEAL))
for i,t in enumerate(['Locker 6: children 1, 2, 3, 6 → 4 changes: closed','Locker 9: children 1, 3, 9 → 3 changes: open','Changes = number of factors. Odd → open','Open: 1, 4, 9, 16 (a number times itself)']): body+=pin(128,330+i*110,800,p(t,30),'rise',WHITE)
body+=pin(992,250,800,p('Q2: take away the 1',38,800,TEAL))
for i,t in enumerate(['Number − 1 is a multiple of 2, 3, 4, 5 and 6','Multiples of 4, 5, 6 in common: 60, 120 …','60 is in the 2s and 3s too ✓','60 + 1 = 61   (121 is too big)']): body+=pin(992,330+i*110,800,p(t,30),'rise',WHITE)
put('p4l1-chwalk',sec('p4l1-chwalk','Early finishers / take-home',body,'Use after pairs have tried. Q1: act out locker 6 and locker 9 with a door (a book cover) opening and closing. Every factor pair gives two changes, so a locker ends up closed, unless its number is something times itself: 1, 4, 9, 16. Q2: check 61: 61 = 2 × 30 + 1 = 3 × 20 + 1 = 4 × 15 + 1 = 5 × 12 + 1 = 6 × 10 + 1.'))

# ---------- talk / exit ----------
body=h2('Talk time')+card(chip('TALK TIME',YEL,NAVY)+p('Ali says: "Bigger numbers always have more factors." Is he right? Find an example to show it.',42,600))+card(p('Sentence starters:',34,400,MUTED)+p('“I noticed that …”   “I tested it by …”   “I know because …”',38,600))
put('p4l1-talk',sec('p4l1-talk','80–85 MIN',body,'Minutes 80 to 85. Pairs talk for 2 minutes, then share. Answer: Ali is wrong. 24 has 8 factors, but 29, which is bigger, has only 2 (1 and 29). One example is enough to show he is wrong (like Siti\'s claim earlier). Second question if time: "Why did the 36-tile rectangles give an odd number of factors?" (6 × 6: 6 is its own partner). Praise the reasons, not only the answers.'))
body=h2('Exit ticket')+card(chip('EXIT TICKET')+p('Write all the factors of 28. Then find the smallest number that is a multiple of both 6 and 9.',46,600))+card(p('Write your answer on a slip of paper. Show it to your tutor. Then collect your stamp in your inquiry journal.',34,400))
put('p4l1-exit',sec('p4l1-exit','85–88 MIN',body,'Minutes 85 to 88. Answer: 1, 2, 4, 7, 14, 28. The smallest common multiple of 6 and 9 is 18 (6, 12, 18 and 9, 18). Extension: which numbers from 1 to 50 have exactly 4 factors? (15 numbers: 6, 8, 10, 14, 15, 21, 22, 26, 27, 33, 34, 35, 38, 39, 46.)'))

# ---------- write ----------
# ---------- fix pass (rebuild/p4_fix.py): sneak-peek puzzles, looking back, neutral names, go further, minute labels ----------
import subprocess as _sp, p4_fix
_G=json.loads(_sp.check_output(['node','-e',"process.stdout.write(JSON.stringify(require('"+os.path.join(H,'..','p4','content','l1.js')+"').gaps))"]))
_ID='p4l1'
_PIC=globals().get('PIC')

order=['p4l1-title','p4l1-warm1','p4l1-warm2','p4l1-explore1','p4l1-explore2','p4l1-teach1','p4l1-we1','p4l1-try1','p4l1-we2','p4l1-we3','p4l1-try2','p4l1-key','p4l1-break','p4l1-ws1','p4l1-ws1ans','p4l1-teachodd','p4l1-teachriddle','p4l1-teachtest','p4l1-ws2','p4l1-ws2ans','p4l1-stretch','p4l1-challenge','p4l1-chdiag','p4l1-chwalk','p4l1-talk','p4l1-exit']
p4_fix.finish(S,1,_G,pic=_PIC)
order=p4_fix.order(order,1)
assert set(order)==set(S), set(order)^set(S)
sd=os.path.join(D,'slides')
for f in os.listdir(sd):
    if f.endswith('.html') and f[:-5] not in S: os.remove(os.path.join(sd,f))
for i,h in S.items(): open(os.path.join(sd,i+'.html'),'w').write(h)
deck={'v':4,'createdOnFiles':{'v':1,'at':datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')},'lists':'css',
 'title':'Math Inquirers P4: Lesson 1 – Factor Hunters','order':order,'cover':'p4l1-title',
 'sections':{'s1':{'description':'Warm-up and explore','start':'p4l1-title'},'s2':{'description':'Teach: factor pairs, common factors and common multiples','start':'p4l1-teach1'},'s3':{'description':'Worksheet with teaching before each page','start':'p4l1-break'},'s4':{'description':'Stretch, challenge, talk and exit','start':'p4l1-stretch'}},
 'faces':{'fredoka':{'family':'Fredoka','href':'https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&display=swap'},'nunito-sans':{'family':'Nunito Sans','href':'https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@400;600;700&display=swap'}},
 'designSystems':[]}
json.dump(deck,open(os.path.join(D,'deck.json'),'w'),indent=1,ensure_ascii=False)
print(len(order),'slides')
