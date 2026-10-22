"""Math Inquirers P5, Lesson 10: Challenge Day (mixed heuristics). Writes split/p5l10/project (deck.json + slides/*.html).
Every answer was checked with a script (exhaustive search for every logic puzzle and every "find all")."""
import json,os,sys,datetime
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,H)
import slidekit
from slidekit import *
slidekit.FOOT='Math Inquirers P5 Holiday Program  •  Notice it. Test it. Explain why.'
FOOTX=slidekit.FOOT
S={}
def put(i,h): S[i]=h
RED='#D64545'; GREYT='#9AA5BD'

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
def svgwrap(w,h,label,inner):
    return f'<svg aria-label="{E(label)}" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="width:{w}px;height:{h}px;flex:none">{inner}</svg>'
def txt(x,y,s,size=40,fill=NAVY,anchor='middle',weight=700,font='Fredoka, Arial'):
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" fill="{fill}" font-family="{font}">{E(str(s))}</text>'
def stick(x1,y1,x2,y2,col=NAVY,w=9):
    return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{col}" stroke-width="{w}" stroke-linecap="round"/>'
def sq_fig(n,ox,oy,u=70):
    """n squares in a row; first square navy, the 3 NEW sticks of each later square teal"""
    g=''
    for i in range(n):
        x=ox+i*u; c=NAVY if i==0 else TEAL
        g+=stick(x,oy,x+u,oy,c)+stick(x,oy+u,x+u,oy+u,c)+stick(x+u,oy,x+u,oy+u,c)
        if i==0: g+=stick(x,oy,x,oy+u,c)
    return g
def tiles_fig(n,ox,oy,s=44):
    """n yellow tiles in a row with a grey border: (n+2) wide, 3 tall"""
    g=''
    for r in range(3):
        for c in range(n+2):
            edge=r in (0,2) or c in (0,n+1)
            g+=f'<rect x="{ox+c*s}" y="{oy+r*s}" width="{s}" height="{s}" fill="{GREYT if edge else YEL}" stroke="{NAVY}" stroke-width="3"/>'
    return g
def tag_box(x,y,w,h,label,fill=WHITE,size=34,col=NAVY):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="{fill}" stroke="{NAVY}" stroke-width="4"/>'+txt(x+w/2,y+h/2+size*0.35,label,size,col)

def write_deck(num,title,order,sections,D):
    os.makedirs(os.path.join(D,'slides'),exist_ok=True)
    assert set(order)==set(S), set(order)^set(S)
    sd=os.path.join(D,'slides')
    for f in os.listdir(sd):
        if f.endswith('.html') and f[:-5] not in S: os.remove(os.path.join(sd,f))
    for i,h in S.items(): open(os.path.join(sd,i+'.html'),'w').write(h)
    deck={'v':4,'createdOnFiles':{'v':1,'at':datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')},'lists':'css',
     'title':title,'order':order,'cover':order[0],'sections':sections,
     'faces':{'fredoka':{'family':'Fredoka','href':'https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&display=swap'},'nunito-sans':{'family':'Nunito Sans','href':'https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@400;600;700&display=swap'}},
     'designSystems':[]}
    json.dump(deck,open(os.path.join(D,'deck.json'),'w'),indent=1,ensure_ascii=False)
    print(len(order),'slides')
D=os.path.join(H,'..','split','p5l10','project')
P='p5l10-'

# 1 title
put(P+'title',title_slide(P+'title','LESSON 10  •  WEEK 5B','Challenge Day','Mixed heuristics',
 'Choose a start for a puzzle: draw a model, work backwards, use a logic grid, list in order or guess and check. Then check every clue.',
 'Objective: Choose a way to start a puzzle (draw a model, list in order, make a table, work backwards, guess and check or suppose, use a logic grid), solve competition-style problems, check every answer against every clue, and explain why the chosen start works. '
 'Materials: puzzle cards for 4 stations (backwards, logic, counting, guess and check), mini whiteboards, scrap paper, a 3 by 4 grid drawn on paper, certificates, stamps. '
 'Online: each breakout pair gets one puzzle card on screen and reports back how they started; logic grids and models are shared on screen and annotated together; children hold their working up to the camera. '
 'Time plan: sneak-peek puzzles 0 to 3 (private answers, nobody is marked), warm-up 3 to 9, explore 9 to 21 (a Go further what-if is on the explore slide for anyone who wants more), teaching 21 to 33 (click to reveal each step and answer), brain break 33 to 37, workbook page 1 37 to 49 (after question 3 you may choose: carry on, or try Think harder), check together 49 to 53, short teaching before page 2 53 to 58, workbook page 2 58 to 72 (alone: start with the questions named at the top, then choose; nobody has to finish), check together 72 to 76, talk time 76 to 82 (you may say pass; volunteers first; then everyone tries the first step of the Investigation), exit ticket 82 to 86, reflection 86 to 88 (pass is always OK), stamp and goodbye 88 to 90. Think harder, Go further and the Investigation are open to every child. The tutor never announces who is on which page, and never splits a pair unless both children agree. Private invitations only by private chat message. In this last lesson the 88 to 90 slot is certificates.'))

# 2 warm1 relay cards
cards=[('Place value','Value of the 5 in 2 507 314','500 000'),('Fractions','2/3 + 1/6','5/6'),('Triangle','Base 8 cm, height 5 cm. Area?','20 cm²'),('Volume','Cuboid 5 cm × 4 cm × 3 cm. Volume?','60 cm³'),
       ('Rate','4 pens cost $6. Cost of 10 pens?','$15'),('Percentage','20% of $80','$16'),('Angles','Isosceles, top angle 40°. A base angle?','70°'),('Patterns','Sticks = 3 × figure + 1. Figure 10?','31')]
body=h2('Warm-up: Mix-up Relay')+p('Read a card. Say a name. That child answers, then names the next child.',34,600,MUTED)
CW=397
for i,(t,q,a) in enumerate(cards):
    L=128+(i%4)*(CW+24); T=290+(i//4)*290
    body+=pin(L,T,CW,f'<p style="font-size:28px;font-weight:800;color:{TEAL}">{E(t)}</p><p style="font-size:32px;font-weight:700;line-height:1.25">{E(q)}</p>',None,WHITE,22,'16px 22px',f'box-sizing:border-box;height:250px;border:4px solid {NAVY}')
    body+=pin(L+20,T+172,CW-40,f'<p style="font-size:34px;font-weight:800">{E(a)}</p>','pop',YEL,16,'8px 18px',f'box-sizing:border-box;border:3px solid {NAVY}')
put(P+'warm1',sec(P+'warm1','0–4 MIN',body,'Minutes 0 to 4. Relay review: one card from each of our earlier topics. Read a card, say a child\'s name; that child answers and names the next child. Click to reveal each answer in order. A wrong answer gets a friendly "try again", never a groan. '
 'Answers: 1) the 5 is in the hundred thousands place: 500 000. 2) 4/6 + 1/6 = 5/6. 3) 8 × 5 ÷ 2 = 20 cm². 4) 5 × 4 × 3 = 60 cm³. 5) $6 ÷ 4 = $1.50 each, × 10 = $15. 6) 10% is $8, so 20% is $16. 7) base angles are equal: (180° − 40°) ÷ 2 = 70°. 8) 3 × 10 + 1 = 31. '
 'Ask "Which lesson does this remind you of?" for each card.'))

# 3 warm2
qs=[('1.','What is 3/4 of 48?','36'),('2.','Area of a triangle with base 10 cm and height 6 cm','30 cm²'),('3.','A tap fills 6 ℓ in 2 minutes. How long for 45 ℓ?','15 minutes'),('4.','Two angles on a straight line: 65° and ___','115°'),('5.','5, 8, 11, 14, __','17')]
body=h2('Quick questions')+''.join(qrow(128,250+i*125,1250,a,b) for i,(a,b,c) in enumerate(qs))+''.join(answer(1420,250+i*125,372,c) for i,(a,b,c) in enumerate(qs))
put(P+'warm2',sec(P+'warm2','4–9 MIN',body,'Minutes 4 to 9. Whiteboards up together, then click. Answers: 1) 48 ÷ 4 = 12, × 3 = 36. 2) 10 × 6 ÷ 2 = 30 cm². 3) 6 ℓ in 2 min is 3 ℓ per minute; 45 ÷ 3 = 15 minutes. 4) 180° − 65° = 115°. 5) add 3: 17. Ask after 3: "Which start did you use: a table, a rate per minute, or something else?"'))

# 4 explore1
g=''
for i,(lab,col) in enumerate([('A',SKY),('B',YEL),('C','#BFE3DC'),('D','#F4A6A6')]):
    x=40+i*390
    g+=f'<rect x="{x}" y="10" width="340" height="120" rx="20" fill="{col}" stroke="{NAVY}" stroke-width="5"/>'+txt(x+170,90,lab,64)
g+=txt(210,175,'number machine',30,NAVY,font='Nunito Sans, Arial')+txt(600,175,'pets logic',30,NAVY,font='Nunito Sans, Arial')+txt(990,175,'squares',30,NAVY,font='Nunito Sans, Arial')+txt(1380,175,'two numbers',30,NAVY,font='Nunito Sans, Arial')
steps=''.join(f'<li>{E(s)}</li>' for s in ['Pick 2 of the 4 puzzle cards. Work in pairs.','Write your answer AND how you started: draw, list, table, work backwards, guess and check.','Check your answer against every clue.','Be ready to teach one card to the group in two sentences.'])
body=h2('Explore: puzzle menu')+card(chip('EXPLORE')+f'<ol style="font-size:34px;font-weight:600;padding-left:52px;display:flex;flex-direction:column;gap:8px">{steps}</ol>')
body+=card(svgwrap(1580,200,'Four puzzle cards labelled A, B, C and D: a number machine, pets logic, squares and two numbers',g),extra='padding:20px 32px')
put(P+'explore1',sec(P+'explore1','9–14 MIN',body,'Minutes 9 to 14. Pairs choose 2 of 4 puzzle cards (online: the tutor puts each card on the shared screen). Card A: a number is doubled, 7 is added, the answer is divided by 3, giving 5; find the number. Card B: Ali, Ben and Mei have a cat, a dog and a fish; Ali has no dog; Ben has no cat and no dog. Card C: how many squares of all sizes are in a 2 by 2 grid? Card D: two numbers add to 20 and differ by 6. '
 'Predict first: which card is the hardest? Children write the answer and how they started. Anyone who wants more (open to every pair): make a puzzle card for the next pair.'))

# 5 explore2
body=h2('Explore: talk about it')+numcards([('1.','Which cards did you solve? How did you START each one?'),('2.','Did anyone start a different way? Did you both get the same answer?'),('3.','How did you check your answer?')],40)
put(P+'explore2',sec(P+'explore2','14–21 MIN',body,'Minutes 14 to 21. Gather pairs, then take one card at a time. Answers: A) 4: work backwards, 5 × 3 = 15, 15 − 7 = 8, 8 ÷ 2 = 4; check forwards. B) Ben has the fish, Ali the cat, Mei the dog (Ben has no cat and no dog, so fish; Ali has no dog, so cat; Mei has the dog). C) 5 squares: 4 small and 1 big; most children first say 4. D) 13 and 7 (guess and check, or: take away the 6, share 14 into 7 and 7, give the 6 back to one). '
 'Write the starts on the board as children say them: "work backwards", "tick and cross grid", "count by size", "guess and check". Do NOT give a method before they have tried; the next slides name them.'))

# 6 teach1 toolbox
tools=[('Draw a model','Parts and units, amounts that are shared or compared.'),('Work backwards','A number is changed in steps and you know the end. Undo the LAST step first.'),('Logic grid','Who has what? Ticks and crosses; a tick means crosses in the rest of its row and column.'),
       ('List in order','"Find all", counting shapes of every size. Go in order so nothing is missed.'),('Make a table','Something grows or changes step by step.'),('Guess and check / suppose','Two kinds of things with a total.')]
body=h2('Your toolbox: how to START')+p('Stuck? Do not stare. Pick a start and put the puzzle on paper.',34,600,MUTED)
for i,(t,u) in enumerate(tools):
    L=128+(i%3)*(533+32); T=300+(i//3)*270
    body+=pin(L,T,533,p(t,38,800,TEAL)+p(u,30,600),'rise',WHITE,24,'22px 28px',f'box-sizing:border-box;height:240px')
body+=pin(128,850,1664,p('Then check against EVERY clue and explain why your start works.',32,700),'fade',SOFT,20,'12px 28px')
put(P+'teach1',sec(P+'teach1','21–22 MIN',body,'Teach: the toolbox. "Today\'s puzzles mix everything. Clever inquirers do not know every answer straight away. They know how to START." Click each card and give one example from our lessons: model (fraction word problems, Lesson 3), working backwards (percentage and fractions of a remainder), logic grid (today), list in order (digit puzzles, Lesson 1), table (patterns, Lesson 9), guess and check or supposition (Lesson 9). Click the last box and read it together. The next slides show three starts in action.'))

# 7 we1 backwards
body=h2('Work backwards: undo the last step first')+card(p('Siti spent 1/4 of her money, then $10, then half of what was left. She has $13 left. How much did she start with?',34,700))
body+=machine([('money','q'),('− 1/4','op'),('− $10','op'),('÷ 2','op'),('$13','res')],w=1664,h=130)
body=body.replace('<svg aria-label="Number machine"','<svg aria-label="Steps from her money, take away a quarter, take away 10 dollars, divide by 2, to 13 dollars left"')
body+=step(1,'Undo the half:  $13 is half of what was left, so before that she had 13 × 2 = $26.',top=560,size=32)
body+=step(2,'Undo the $10:  26 + 10 = $36.',top=650,size=32)
body+=step(3,'$36 is 3/4 of her money (1/4 was spent). 1/4 = 36 ÷ 3 = $12, so all of it is 4 × 12 = $48.',top=740,size=32)
body+=answer(128,830,1664,'$48.  Check forwards: 48 − 12 = 36, 36 − 10 = 26, 26 ÷ 2 = 13 ✓')
put(P+'we1',sec(P+'we1','22–25 MIN',body,'Worked example: working backwards with fractions. Ask first: "What do we know? Only the END." Draw the steps as a machine going forwards, then go back along the machine with the OPPOSITE of each step, starting at the end. Think-aloud: "Half of what was left is $13, so what was left is $26. Before the $10 lunch she had $36. Now the tricky bit: she spent a quarter, so $36 is three quarters. If 3 quarters is $36, 1 quarter is $12, and four quarters is $48." Always check by running forwards. Common mistake: taking 3/4 of $36 or adding 1/4 of 36. Worksheet Q1 uses the same idea with different numbers.'))
put(P+'try1',try_slide(P+'try1','25–26 MIN','Your turn: work backwards','Write the steps first. Undo the last step first.',[('a','A number is multiplied by 3, then 4 is added. The answer is 19. What is the number?','5'),('b','Ravi spends 1/2 of his money, then $5. He has $9 left. How much at first?','$28'),('c','Ali spends 1/3 of his money, then $6. He has $14 left. How much at first?','$30')],'Whiteboards, then click. a) 19 − 4 = 15, 15 ÷ 3 = 5. Check 5 × 3 + 4 = 19. b) 9 + 5 = 14, 14 is half, so 28. Check 28 ÷ 2 = 14, 14 − 5 = 9. c) 14 + 6 = 20; 20 is 2/3 of the money (1/3 was spent); 1/3 = 10, so 30. Check 30 − 10 = 20, 20 − 6 = 14.',34))

# 9 we2 logic grid
def lgrid(w=800):
    cw=200; rh=90; hh=70; ox=0; g=''
    cols=['Badminton','Swimming','Football']; rows=['Ravi','Siti','Ben']
    g+=f'<rect x="0" y="0" width="{cw*4}" height="{hh}" fill="{YEL}" stroke="{NAVY}" stroke-width="4"/>'
    for c,n in enumerate(cols): g+=txt(cw*(c+1)+cw/2,hh/2+10,n,28,NAVY,font='Nunito Sans, Arial',weight=800)
    for r,n in enumerate(rows):
        y=hh+r*rh
        g+=f'<rect x="0" y="{y}" width="{cw}" height="{rh}" fill="{SKY}" stroke="{NAVY}" stroke-width="4"/>'+txt(cw/2,y+rh/2+11,n,34)
        for c in range(3): g+=f'<rect x="{cw*(c+1)}" y="{y}" width="{cw}" height="{rh}" fill="{WHITE}" stroke="{NAVY}" stroke-width="4"/>'
    return g
def mark(r,c,kind):
    cx=200*(c+1)+100; cy=70+r*90+45
    if kind=='x': return stick(cx-18,cy-18,cx+18,cy+18,RED,8)+stick(cx-18,cy+18,cx+18,cy-18,RED,8)
    return f'<polyline points="{cx-22},{cy} {cx-6},{cy+18} {cx+24},{cy-20}" fill="none" stroke="{TEAL}" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/>'
def ov(marks,label):
    return pin(128,360,800,svgwrap(800,340,label,''.join(mark(*m) for m in marks)),'fade')
body=h2('Logic grid: ticks and crosses')+card(p('Ravi, Siti and Ben play badminton, swimming and football (one each). Ravi does not swim. Siti plays neither football nor badminton. Ben does not play football.',30,700))
body+=pin(128,360,800,svgwrap(800,340,'Empty logic grid: Ravi, Siti and Ben against badminton, swimming and football',lgrid()))
body+=ov([(0,1,'x'),(1,0,'x'),(1,2,'x'),(2,2,'x'),(1,1,'t')],'Crosses from the clues and a tick for Siti swimming')
body+=ov([(2,1,'x')],'A cross for Ben swimming')
body+=ov([(0,0,'x'),(2,0,'t'),(0,2,'t')],'Ben badminton and Ravi football')
body+=step(1,'Cross out what the clues say no to. Siti has two crosses, so Siti swims: tick.',left=980,top=400,width=812,size=30)
body+=step(2,'A tick means crosses in the rest of its row and column: nobody else swims.',left=980,top=540,width=812,size=30)
body+=step(3,'Ben has two crosses, so Ben plays badminton. Ravi gets football.',left=980,top=680,width=812,size=30)
body+=answer(128,740,1664,'Ravi football, Siti swimming, Ben badminton.  Check all three clues ✓') if False else ''
body+=pin(980,815,812,p('Ravi football, Siti swimming, Ben badminton. Check all 3 clues ✓',32,800),'pop',YEL,20,'16px 26px')
put(P+'we2',sec(P+'we2','26–29 MIN',body,'Worked example: a logic grid. Read the clues aloud and let children say where a cross goes before you click. Click 1 shows the crosses from the three clues and the first tick: Siti\'s row has two crosses, so only swimming is left. Click 2 (step 2): a tick means crosses in the rest of its column, so nobody else swims. Click 3 (step 3): Ben has crosses for swimming and football, so badminton; Ravi has the one left, football. Ask: "Could we have started with a different clue?" (Ben also gets a cross in football, but Siti is the one with two crosses at the start.) Finish with: check every clue against the answer. This is the method for worksheet Q2, which has four people.'))
put(P+'try2',try_slide(P+'try2','29–30 MIN','Your turn: pick your start','Say which start you use before you answer.',[('a','Ali does not have red, Bo does not have blue, Cy has neither red nor blue. Red, blue or green: who has green?','Cy'),('b','Two numbers add to 30 and differ by 8. What are they?','19 and 11'),('c','How many squares of all sizes in a 2 by 2 grid?','5')],'Whiteboards. a) Logic grid: Cy has neither red nor blue, so green. Then Ali is not red, so blue, and Bo has red. b) Take away the 8: 22, share 11 and 11, add 8 to one: 19 and 11. Check 19 + 11 = 30 and 19 − 11 = 8. c) 4 small and 1 big: 5.',32))

# 11 we3 model
u=150
g=f'<text x="0" y="62" font-size="34" font-weight="800" fill="{NAVY}" font-family="Nunito Sans, Arial">Ali</text><text x="0" y="162" font-size="34" font-weight="800" fill="{NAVY}" font-family="Nunito Sans, Arial">Ben</text>'
for i in range(3): g+=f'<rect x="{110+i*u}" y="20" width="{u-4}" height="60" rx="6" fill="{YEL}" stroke="{NAVY}" stroke-width="4"/>'
for i in range(2): g+=f'<rect x="{110+i*u}" y="120" width="{u-4}" height="60" rx="6" fill="{SKY}" stroke="{NAVY}" stroke-width="4"/>'
g+=f'<rect x="{110+2*u}" y="120" width="{70}" height="60" rx="6" fill="{WHITE}" stroke="{TEAL}" stroke-width="4" stroke-dasharray="10 6"/>'+txt(110+2*u+35,162,'$6',34,TEAL)
g+=txt(110+3*u+120,100,'$86 together',34,TEAL,'start',800,'Nunito Sans, Arial')
body=h2('Draw a model: units and an extra')+card(p('Ali and Ben have $86 altogether. Ben has $6 more than 2/3 of Ali’s money. How much does each have?',34,700))
body+=pin(128,360,1100,svgwrap(1050,200,'Bars: Ali is 3 equal units, Ben is 2 equal units and 6 dollars; together 86 dollars',g))
body+=step(1,'Take away the extra $6:  86 − 6 = 80. Now there are 3 + 2 = 5 equal units.',top=590,size=32)
body+=step(2,'5 units = 80, so 1 unit = 80 ÷ 5 = $16.',top=680,size=32)
body+=step(3,'Ali: 3 × 16 = $48.   Ben: 2 × 16 + 6 = $38.',top=770,size=32)
body+=pin(128,860,1664,p('Check BOTH clues: 48 + 38 = 86 ✓   2/3 of 48 = 32, and 32 + 6 = 38 ✓',32,800),'pop',YEL,20,'12px 28px')
put(P+'we3',sec(P+'we3','30–32 MIN',body,'Worked example: a model. "Ali is 3 units because Ben has 2/3 of Ali (2 units), so Ali is split into 3 equal units. Ben has 2 of those units and an extra $6." Draw the bars on the board while children say what to draw. Click step 1: remove the extra before sharing equally. Step 2: 80 ÷ 5 = 16. Step 3: Ali 48 and Ben 38. Check both clues, not just the total. Common mistake: 86 ÷ 5 without taking away the $6 first (17.2, not a whole number: a sign something went wrong). Worksheet Q3 is the same kind with Mei and Ravi.'))

# key
body=h2('Key idea: choose a start, check every clue')+card(p('Draw a model, work backwards, use a logic grid, list in order, make a table, or guess and check. Say WHY your start works.',42,700))+card(p('Check your answer against EVERY clue, not just one.',38,600,MUTED))
put(P+'key',sec(P+'key','32–33 MIN',body,'Say the key idea together. Common mistakes to watch for during the worksheet: (1) Working backwards in the wrong order or taking away instead of adding back. (2) Q2: guessing instead of using a clue that tells you something for sure; not crossing out the rest of the row and column after a tick. (3) Q3: dividing 115 by 7 without removing the extra $10 first. (4) Q4: counting only the 12 small squares. (5) Q5: stopping at the first suspect that fits one statement instead of counting the liars for each suspect. (6) Q6: adding the same number of years to only one person.'))
put(P+'break',break_slide(P+'break','33–37 MIN','Puzzle stretch: stand up and show a 3 by 3 grid with your fingers. How many squares can you find on it?','Five minutes. Online: everyone stands on camera. Children draw a 3 by 3 grid in the air, then count squares by size and whisper the answer to a partner or type it in the chat on the way back (14: 9 small, 4 of size 2 by 2 and 1 of size 3 by 3). Drink of water.'))

# ws1
put(P+'ws1',ws_preview(P+'ws1','37–49 MIN','Worksheet page 1: with your partner',[('Q1','Money puzzle with fractions. Work backwards.'),('Q2','Four people, four dishes. Logic grid.'),('Q3','Two amounts. Draw a model.')],'Stuck? Draw it, work backwards, or put the clues in a grid.','Minutes 37 to 49. Walk around. Ask "How did you start?" and "How do you know?" before giving any help. Q1: the fraction step is last in the story, so it is FIRST to undo? No: the story goes book (1/3), lunch, gift (half). Undo the gift first, then lunch, then the 1/3. Q2: Clue 2 and clue 4 together fix the roti prata.'))
put(P+'ws1ans',checks(P+'ws1ans','49–51 MIN','Page 1: check together',[('Q1','$63'),('Q2','Ali chicken rice, Ben laksa, Mei satay, Siti roti prata'),('Q3','Mei $60, Ravi $55')],
 'Click each answer after a pair explains how they started. Q1: 15 × 2 = 30 before the gift; 30 + 12 = 42 before lunch; 42 is 2/3 of the money so 1/3 = 21 and all of it is 63. Check 63 − 21 = 42, 42 − 12 = 30, 30 ÷ 2 = 15. Q2: roti prata is a girl (clue 2) and not Mei (clue 4), so Siti. Ali is not laksa or satay, so chicken rice. Ben is not satay, so laksa; Mei satay. Q3: Mei is 4 units; Ravi is 3 units and $10. 7 units + $10 = $115; 7 units = $105; 1 unit = $15. Mei 60, Ravi 55. Check 3/4 of 60 = 45, 45 + 10 = 55.',gapy=190))

# teach before page 2: counting squares
s=90; g=''
for r in range(2):
    for c in range(3): g+=f'<rect x="{10+c*s}" y="{10+r*s}" width="{s}" height="{s}" fill="{SKY}" stroke="{NAVY}" stroke-width="4"/>'
gr=svgwrap(290,200,'A 2 by 3 grid of 6 small squares',g)
o=f'<rect x="10" y="10" width="{2*s}" height="{2*s}" fill="none" stroke="{RED}" stroke-width="8" stroke-dasharray="14 8"/>'
o2=f'<rect x="{10+s}" y="10" width="{2*s}" height="{2*s}" fill="none" stroke="{TEAL}" stroke-width="8" stroke-dasharray="14 8"/>'
body=h2('Count by size: squares in a grid')+pin(128,250,320,gr)
body+=pin(128,250,320,svgwrap(290,200,'The 2 by 2 square on the left',o),'fade')+pin(128,250,320,svgwrap(290,200,'The 2 by 2 square on the right',o2),'fade')
body+=pin(500,250,1292,p('How many squares of all sizes are in this 2 by 3 grid?',38,700),None,WHITE,20,'22px 28px')
body+=step(1,'Size 1 by 1: 3 in each of 2 rows = 6.',left=500,top=380,width=1292,size=34)
body+=step(2,'Size 2 by 2: it can start in the left column or the next one = 2.',left=500,top=480,width=1292,size=34)
body+=step(3,'Size 3 by 3: the grid is only 2 rows tall, so none.',left=500,top=580,width=1292,size=34)
body+=answer(128,730,1664,'6 + 2 = 8 squares.  Counting by size means nothing is missed.')
body+=pin(128,830,1664,p('Try the next one on your whiteboard: how many squares in a 2 by 4 grid?  (answer: 8 + 3 = 11)',32,700),'fade',SOFT,20,'14px 28px')
put(P+'teachsq',sec(P+'teachsq','51–53 MIN',body,'Teach before worksheet page 2 (Q4). Ask first: "How many squares?" Most children say 6. Click: the red square, then the teal square appear with step 2. Think-aloud: "I count by size, smallest first. 1 by 1: 6. Then 2 by 2: I slide the big square along: left or right, 2. 3 by 3 will not fit, so I stop." 6 + 2 = 8. The check slide for the next grid (2 by 4): size 1: 8; size 2: 3 positions; size 3: none; total 11.'))

# teach liar
Wl=[330,230,230,230,230]
body=h2('Who is lying? Try each suspect')+card(p('Someone broke a window. Ali: “Ben did it.”  Ben: “I did not do it.”  Mei: “Ali did it.”  Exactly ONE child is lying. Who broke it?',34,700))
body+=trow(128,420,['If it was …','Ali says','Ben says','Mei says','Liars'],Wl,None,True,34)
rows=[['Ali','lies','true','true','1'],['Ben','true','lies','lies','2'],['Mei','lies','true','lies','2']]
for i,r in enumerate(rows): body+=trow(128,510+i*90,r,Wl,'rise',False,34)
body+=answer(128,810,1664,'Only Ali gives exactly 1 liar. Ali broke the window.')
put(P+'teachliar',sec(P+'teachliar','53–55 MIN',body,'Teach before worksheet page 2 (Q5). Try each suspect and count the liars: this is a table of cases. If Ali did it: Ali says Ben did it, which is a lie; Ben says "I did not", which is true; Mei says Ali did it, which is true. One liar: fits. If Ben did it: Ali is true, Ben is lying, Mei is lying: two liars, does not fit. If Mei did it: Ali is lying, Ben is true, Mei is lying: two liars, does not fit. Only Ali. Ask: "Why can we be sure there is only one answer?" (We tried every suspect.)'))

# teach ages
W5=[240,200,200,260]
body=h2('Keep the age gap the same')+card(p('Dad is 38 and Sam is 10. In how many years will Dad be exactly 3 times as old as Sam?',34,700))
body+=trow(128,400,['Years later','Dad','Sam','3 × Sam'],W5,None,True,34)
for i,(y,d,sm) in enumerate([(1,39,11),(2,40,12),(3,41,13),(4,42,14)]):
    body+=trow(128,490+i*80,[str(y),str(d),str(sm),str(3*sm)],W5,'rise',False,34)
body+=pin(1330,400,462,p('The gap never changes: 38 − 10 = 28. When Dad is 3 times as old, 28 is 2 times Sam’s age, so Sam is 14. That is 4 years later.',30,700),'fade',SOFT,20,'20px 26px')
body+=answer(128,830,1664,'In 4 years: Dad 42, Sam 14, and 3 × 14 = 42 ✓')
put(P+'teachage',sec(P+'teachage','55–57 MIN',body,'Teach before worksheet page 2 (Q6). Two starts: a table (both ages go up by 1 each year, so the 3 × Sam column grows faster) and the age gap (the difference between two people\'s ages stays the same). With the gap: if Dad is 3 times as old as Sam, then Dad is Sam\'s age three times, so the gap of 28 is two Sam-ages: Sam is 14. 14 − 10 = 4 years. Ask: "Which start would be quicker for Dad 41 and Sam 3?" Common mistake: 38 ÷ 10 or adding years to only one person.'))

# ws2
put(P+'ws2',ws_preview(P+'ws2','57–72 MIN','Worksheet page 2: on your own',[('Q4','Squares of all sizes in a 3 by 4 grid. Count by size.'),('Q5','Who broke the vase? Try each child and count the liars.'),('Q6','Ages: in how many years? And which start did you use?')],'Want more? Think harder and Go further are at the back of your workbook.','Children work alone. Q6b: look for children who can say WHY they chose a table or the age gap, not only which one.'))
put(P+'ws2ans',checks(P+'ws2ans','72–76 MIN','Page 2: check together',[('Q4','a) 12   b) 6 of size 2 by 2 and 2 of size 3 by 3   c) 20 squares'),('Q5','Ben broke the vase'),('Q6','a) 7 years: Mum 48, Mei 16   b) open, say why')],
 'Click after a child explains. Q4: size 1: 3 rows × 4 = 12; size 2: 2 rows × 3 positions = 6; size 3: 1 row × 2 positions = 2; total 20; no size 4 because the grid is only 3 rows tall. Q5: Ali did it: Ali lies (Ben did not), Ben lies (it was not Mei), Mei is true: 2 liars. Mei did it: Ali lies, Ben is true, Mei lies: 2 liars. Ben did it: Ali true, Ben lies, Mei true: 1 liar. So Ben. Q6: table: after 7 years Mum 48 and Mei 16. Or gap 32: Mei would be 16 (2 × 16 = 32), that is 7 years from now.',gapy=190))

# stretch
st=[('1.','Ben has 14 coins, all 50¢ and 20¢ coins, worth $4.90. How many of each?'),('2.','What is the smallest whole number bigger than 1 that leaves a remainder of 1 when divided by 2, by 3, by 4, by 5 and by 6?'),('3.','1/2 of a number is 5 more than 1/3 of the same number. What is the number?')]
put(P+'stretch',sec(P+'stretch','37–72 MIN  •  OPTION',h2('Think harder')+numcards(st,36),'Answers: 1) 7 fifty-cent coins and 7 twenty-cent coins (suppose all 14 are 20¢: $2.80; $2.10 short; each swap adds 30¢; 210 ÷ 30 = 7; check 350 + 140 = 490). 2) 61 (1 more than the smallest number that 2, 3, 4, 5 and 6 all divide into: 60). 3) 30 (a half minus a third is 1/6 of the number, and that is 5; check 15 and 10).'))
ch=[('1.','A monkey eats half of the rambutans in a pile and 1 more, every day for 3 days. After the third day there are none left. How many were in the pile at the start?'),('2.','Ali, Ben, Mei and Siti sit in a row of 4 chairs. Mei is not on either end. Ben does not sit next to Mei. Siti sits somewhere to the left of Ali. Ben is not on the left end. In what order do they sit, from left to right?')]
put(P+'challenge',sec(P+'challenge','37–72 MIN  •  OPTION',h2('Go further')+numcards(ch,32),'Pairs try first, then the "see it" slide, then the walk-through. The chairs puzzle (2) is Go further Q7; the rambutan puzzle (1) is in the question bank only. Answers: 1) 14 rambutans. 2) Siti, Mei, Ali, Ben.'))
# chdiag
g1=''
for i,lab in enumerate(['Start','After day 1','After day 2','After day 3']):
    x=10+i*190; g1+=tag_box(x,60,160,90,'?' if i<3 else '0',YEL if i<3 else SKY,44)+txt(x+80,200,lab,24,NAVY,font='Nunito Sans, Arial')
    if i<3: g1+=f'<line x1="{x+165}" y1="105" x2="{x+185}" y2="105" stroke="{NAVY}" stroke-width="4"/>'
g1+=txt(380,40,'each day: eat half and 1 more',26,TEAL,font='Nunito Sans, Arial')
g2=''
for i in range(4):
    x=20+i*150; g2+=tag_box(x,60,130,90,str(i+1),WHITE,40)
g2+=txt(310,40,'4 chairs, left to right',26,TEAL,font='Nunito Sans, Arial')
for i,t in enumerate(['Mei: not on either end','Ben: not next to Mei','Siti: somewhere left of Ali','Ben: not on the left end']):
    g2+=txt(20,215+i*34,t,26,NAVY,'start',700,'Nunito Sans, Arial')
body=h2('Go further: see it',60)+'<div style="display:flex;gap:32px;align-items:flex-start">'
body+=card(f'<p style="font-size:30px;font-weight:700;color:{TEAL}">Q1: Three days of eating</p>'+svgwrap(760,260,'Four boxes: the pile at the start, after day 1, after day 2 and after day 3, which is zero',g1).replace('width:760px;height:260px;flex:none','width:100%;height:auto;display:block'),extra='flex:1;min-width:0;padding:20px 24px')
body+=card(f'<p style="font-size:30px;font-weight:700;color:{TEAL}">Q2: Four chairs and four clues</p>'+svgwrap(760,370,'Four numbered chairs and the four clues about where Ali, Ben, Mei and Siti sit',g2).replace('width:760px;height:370px;flex:none','width:100%;height:auto;display:block'),extra='flex:1;min-width:0;padding:20px 24px')+'</div>'
put(P+'chdiag',sec(P+'chdiag','37–72 MIN  •  OPTION',body,'Show after pairs have tried Go further, or if they are stuck. The pictures show the problem, not the answers. Ask: What do you know for sure about the pile at the end? Which chair can Mei be in? Answers are in the Go further slide notes.'))
body=h2('Go further: walk-through')+pin(128,250,800,p('Q1: work backwards from 0',38,800,TEAL))
for i,t in enumerate(['After day 3: 0. Eating half and 1 more leaves half minus 1: so half of the pile was 1, the pile was 2.','Before day 2: half minus 1 = 2, so half = 3 and the pile was 6.','Before day 1: half minus 1 = 6, so half = 7 and the pile was 14.','Check forwards: 14 → 6 → 2 → 0 ✓']): body+=pin(128,330+i*135,800,p(t,28),'rise',WHITE)
body+=pin(992,250,800,p('Q2: where can Mei sit?',38,800,TEAL))
for i,t in enumerate(['Mei is in chair 2 or chair 3.','If Mei is in chair 3, only chair 1 is not next to her: Ben, but he is not on the left end. So not this one.','So Mei is in chair 2, and Ben must be in chair 4.','Siti is left of Ali: Siti 1, Ali 3. Order: Siti, Mei, Ali, Ben ✓']): body+=pin(992,330+i*135,800,p(t,28),'rise',WHITE)
put(P+'chwalk',sec(P+'chwalk','37–72 MIN  •  OPTION',body,'Use after pairs have tried. Q1: eating half and 1 more means the pile after the day is half the pile minus 1. After day 3 it is 0, so the pile before was 2 (half is 1, 1 more is 2 eaten). Then 6, then 14. Check: 14: eats 7 + 1 = 8, 6 left; eats 3 + 1 = 4, 2 left; eats 1 + 1 = 2, 0 left. Q2: Mei is in chair 2 or 3 (not an end). Chair 3 leaves only chair 1 free from her side, so Ben would be at the left end, which the last clue forbids. So Mei is in chair 2 and Ben in chair 4. Siti and Ali take chairs 1 and 3, with Siti on the left.'))

# talk / exit / end
body=h2('Talk time')+card(chip('TALK TIME',YEL,NAVY)+p('Pick one puzzle and teach it to the group in two sentences: how did you start, and how do you know you are right?',42,600))+card(p('Sentence starters:',34,400,MUTED)+p('“I noticed that …”   “I tested it by …”   “I know because …”',38,600))
put(P+'talk',sec(P+'talk','76–82 MIN',body,'Minutes 76 to 82. Pairs talk for 2 minutes, then share. Praise the reasons, not only the answers. Good answers say what the start does: a model shows how the parts relate; working backwards undoes the steps in reverse order; a logic grid keeps the clues tidy; counting by size stops us missing any. Second question: "Which start do you think was the most useful today? When would you NOT use it?"'))
body=h2('Exit ticket')+card(chip('EXIT TICKET')+p('Ravi spends 1/2 of his money on a ticket, then $5 on a snack, and has $7 left. How much money did he start with? Say which start you used.',44,600))+card(p('Write your answer on a slip of paper. Show it to your tutor. Then collect your last stamp in your inquiry journal.',34,400))
put(P+'exit',sec(P+'exit','82–88 MIN',body,'Minutes 82 to 88. Answer: $24. Work backwards: 7 + 5 = 12; 12 is half of his money, so 12 × 2 = 24. Check: 24 ÷ 2 = 12, 12 − 5 = 7. Extension: write your own logic puzzle with four people and four things. Does it have exactly ONE answer?'))
put('end',(f'<section id="end" data-transition="fade" style="background:{NAVY};color:{CREAM};font-family:{BF};padding:128px 128px 160px;display:flex;flex-direction:column;justify-content:center;gap:36px">\n'
 f'<p style="font-size:32px;font-weight:700;letter-spacing:4px;color:{YEL}">WELL DONE, INQUIRERS</p>\n<h1 style="font-family:{HF};font-size:128px;font-weight:600;line-height:1.05">Keep asking why</h1>\n'
 f'<p style="font-family:{HF};font-size:64px;font-weight:500;color:{YEL}">Notice it. Test it. Explain why.</p>\n<p style="font-size:36px;color:#C9D4EC">Certificates and a last stamp for every inquirer. See you in Primary 6!</p>\n'
 f'<p style="position:absolute;left:128px;bottom:64px;width:1400px;font-size:24px;color:#B7C3DD">{E(FOOTX)}</p>\n<aside>{E("Minutes 88 to 90. Hand out certificates. Ask each child to name one puzzle they enjoyed and one start they will use again. Give parents the one-page summary from the tutor guide.")}</aside>\n</section>\n'))

order=[P+x for x in ['title','warm1','warm2','explore1','explore2','teach1','we1','try1','we2','try2','we3','key','break','ws1','ws1ans','teachsq','teachliar','teachage','ws2','ws2ans','stretch','challenge','chdiag','chwalk','talk','exit']]+['end']
write_deck(10,'Math Inquirers P5: Lesson 10 – Challenge Day',order,{'s1':{'description':'Warm-up and explore','start':P+'title'},'s2':{'description':'Teach: how to choose a start','start':P+'teach1'},'s3':{'description':'Worksheet with teaching before each page','start':P+'break'},'s4':{'description':'Stretch, challenge, talk, exit and certificates','start':P+'stretch'}},D)

import p5_gaps; p5_gaps.apply(10)
