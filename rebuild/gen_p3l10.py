"""Math Inquirers P3, Lesson 10: Challenge Day. Writes split/p3l10/project (deck.json + slides/*.html)."""
import json,os,sys,datetime
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,H)
from slidekit import *
D=os.path.join(H,'..','split','p3l10','project'); os.makedirs(os.path.join(D,'slides'),exist_ok=True)
S={}
def put(i,h): S[i]=h
RED='#D64545'; GREEN='#BFE3DC'; PINK='#F4A6A6'; BLUE='#9CC9EE'

def svg(w,h,body,aria,style=''): return f'<svg aria-label="{E(aria)}" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="width:{w}px;height:{h}px;{style}">{body}</svg>'
def T(x,y,s,size=30,fill=NAVY,anchor='middle',weight=800): return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" fill="{fill}" font-family="Nunito Sans, Arial">{E(s)}</text>'
def num_card(a,b,size=36): return card(p(f'<span style="color:{TEAL}">{E(a)}</span>  {E(b)}',size,600,raw=True))

# ---------- fixed-layout slides ----------
def title_slide(sid,n,week,title,sub,today,notes):
    return (f'<section id="{sid}" data-transition="fade" style="background:{NAVY};color:{CREAM};font-family:{BF};padding:128px 128px 160px;display:flex;flex-direction:column;justify-content:center;gap:36px">\n'
            f'<p style="font-size:32px;font-weight:700;letter-spacing:4px;color:{YEL}">LESSON {n}  •  WEEK {week}</p>\n'
            f'<h1 style="font-family:{HF};font-size:128px;font-weight:600;line-height:1.05">{E(title)}</h1>\n'
            f'<p style="font-size:44px;color:#C9D4EC">{E(sub)}</p>\n'
            f'<div style="background:#26385F;border-radius:24px;padding:40px;display:flex;flex-direction:column;gap:12px"><p style="font-size:28px;font-weight:700;letter-spacing:3px;color:{YEL}">TODAY WE WILL</p><p style="font-size:44px;font-weight:600">{E(today)}</p></div>\n'
            f'<p style="position:absolute;left:128px;bottom:64px;width:1400px;font-size:24px;color:#B7C3DD">{E(FOOT)}</p>\n<aside>{E(notes)}</aside>\n</section>\n')
def dark_slide(sid,kicker,head,big,small,notes,bg=NAVY,tag='h1',size=128):
    sub_c='#D7EFEA' if bg==TEAL else '#C9D4EC'
    return (f'<section id="{sid}" data-transition="fade" style="background:{bg};color:{CREAM};font-family:{BF};padding:128px 128px 160px;display:flex;flex-direction:column;justify-content:center;gap:36px">\n'
            f'<p style="font-size:32px;font-weight:700;letter-spacing:4px;color:{YEL}">{E(kicker)}</p>\n'
            f'<{tag} style="font-family:{HF};font-size:{size}px;font-weight:600;line-height:1.05">{E(head)}</{tag}>\n'
            f'{big}\n<p style="font-size:36px;color:{sub_c}">{E(small)}</p>\n'
            f'<p style="position:absolute;left:128px;bottom:64px;width:1400px;font-size:24px;color:{"#D7EFEA" if bg==TEAL else "#B7C3DD"}">{E(FOOT)}</p>\n<aside>{E(notes)}</aside>\n</section>\n')
def explore1(sid,time,steps,pic,notes):
    ol='<ol style="font-size:32px;font-weight:600;padding-left:48px;margin:0;display:flex;flex-direction:column;gap:6px">'+''.join(f'<li>{E(s)}</li>' for s in steps)+'</ol>'
    return sec(sid,time,h2('Explore: what to do')+card(chip('EXPLORE')+ol,extra='padding:24px 40px')+card(pic,extra='padding:16px 24px;align-items:center'),notes)
def talk_qs(sid,time,head,qs,notes):
    return sec(sid,time,h2(head)+''.join(card(p(f'<span style="color:{TEAL}">{i+1}.</span>  {E(q)}',40,600,raw=True)) for i,q in enumerate(qs)),notes)

# ---------- drawing helpers ----------
def person(x,y,fill,label='',lab_fill=NAVY):
    return (f'<circle cx="{x}" cy="{y}" r="22" fill="{fill}" stroke="{NAVY}" stroke-width="4"/><rect x="{x-28}" y="{y+26}" width="56" height="62" rx="20" fill="{fill}" stroke="{NAVY}" stroke-width="4"/>'
            +(T(x,y+122,label,26,lab_fill) if label else ''))
def queue(n,special,w=1664,h=230,gap=None,show=None,aria='A queue of people',ends=True):
    """special: {index: (fill,label)}; show: indexes to draw (default all)"""
    gap=gap or min(150,(w-280)/max(n-1,1)); x0=180; b=''
    if ends: b+=T(40,90,'FRONT',26,TEAL,'start')+f'<polygon points="40,104 20,116 40,128" fill="{TEAL}"/><line x1="40" y1="116" x2="110" y2="116" stroke="{TEAL}" stroke-width="5"/>'
    for i in range(n):
        if show is not None and i not in show: continue
        f,l=special.get(i,(WHITE,''))
        b+=person(x0+i*gap,60,f,l)
    return svg(w,h,b,aria)
def grid_svg(rows,cols,marks=(),base=True,cw=260,rw=80,lw=200,aria='Logic grid'):
    W=lw+cw*len(cols)+10; Hh=rw*(len(rows)+1)+10; b=''
    if base:
        b+=f'<rect x="5" y="5" width="{W-10}" height="{Hh-10}" rx="12" fill="{WHITE}" stroke="{NAVY}" stroke-width="4"/>'
        b+=f'<rect x="5" y="5" width="{W-10}" height="{rw}" rx="12" fill="{YEL}" stroke="{NAVY}" stroke-width="4"/>'
        for j,c in enumerate(cols): b+=T(lw+cw*j+cw/2,5+rw/2+11,c,30)
        for i,r in enumerate(rows): b+=T(lw/2+5,5+rw*(i+1)+rw/2+11,r,32)
        for j in range(len(cols)+1): b+=f'<line x1="{lw+cw*j}" y1="5" x2="{lw+cw*j}" y2="{Hh-5}" stroke="{NAVY}" stroke-width="3"/>' if j else ''
        b+=f'<line x1="{lw}" y1="5" x2="{lw}" y2="{Hh-5}" stroke="{NAVY}" stroke-width="3"/>'
        for i in range(1,len(rows)+1): b+=f'<line x1="5" y1="{5+rw*i}" x2="{W-5}" y2="{5+rw*i}" stroke="{NAVY}" stroke-width="3"/>'
    for (i,j,m) in marks:
        cx=lw+cw*j+cw/2; cy=5+rw*(i+1)+rw/2
        if m=='x': b+=f'<path d="M{cx-18} {cy-18} L{cx+18} {cy+18} M{cx+18} {cy-18} L{cx-18} {cy+18}" stroke="{RED}" stroke-width="7" stroke-linecap="round"/>'
        else: b+=f'<path d="M{cx-22} {cy} L{cx-6} {cy+18} L{cx+24} {cy-20}" fill="none" stroke="{TEAL}" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/>'
    return svg(W,Hh,b,aria)
def bar_graph(data,top,stepv,k,bw=110,slot=170,aria='Bar graph',title='',ylab='',xlab='',fills=(YEL,SKY,TEAL,RED,GREEN),labsize=28):
    x0=110; y0=40+top*k; W=x0+slot*len(data)+30; Hh=y0+100; b=''
    for v in range(0,top+1,stepv):
        y=y0-v*k
        b+=f'<line x1="{x0}" y1="{y}" x2="{W-10}" y2="{y}" stroke="{"#C9D4EC" if v else NAVY}" stroke-width="{2 if v else 4}"/>'+T(x0-14,y+10,str(v),labsize,anchor='end',weight=700)
    b+=f'<line x1="{x0}" y1="{y0}" x2="{x0}" y2="{y0-top*k-10}" stroke="{NAVY}" stroke-width="4"/>'
    for i,(n,v) in enumerate(data):
        x=x0+(slot-bw)/2+i*slot
        if v is not None: b+=f'<rect x="{x}" y="{y0-v*k}" width="{bw}" height="{v*k}" fill="{fills[i%len(fills)]}" stroke="{NAVY}" stroke-width="4"/>'
        b+=T(x+bw/2,y0+40,n,labsize)
    if ylab: b+=f'<text x="30" y="{y0-top*k/2}" font-size="{labsize}" font-weight="800" text-anchor="middle" fill="{NAVY}" font-family="Nunito Sans, Arial" transform="rotate(-90 30 {y0-top*k/2})">{E(ylab)}</text>'
    if xlab: b+=T(x0+slot*len(data)/2,y0+84,xlab,labsize)
    return svg(W,Hh,b,aria)

# ---------- 1. title ----------
put('p3l10-title',title_slide('p3l10-title',10,5,'Challenge Day','Mixed puzzles: bar graphs and logic',
 'Choose how to start a puzzle, solve a logic grid, read a bar graph with a scale, and explain our thinking.',
 'Objective: Choose a way to start a puzzle (draw it, list it, make a table), solve a logic grid with ticks and crosses, read and complete a bar graph with a scale, and explain the thinking. Heuristics taught: (1) draw it, list it or make a table to start; (2) a logic grid: a tick means crosses in the rest of its row and column. '
 'Materials: Puzzle cards for 2 stations (list, measure), digit cards 0 to 9 (or paper cards), squared paper, mini whiteboards, certificates, stamps. '
 'Online: Two stations, 7 minutes each. Pairs stay in one breakout room, and the tutor shares the next station card when the timer ends. No physical materials beyond paper. Logic grids and graphs are shared on screen and annotated together. '
 'Time plan: warm-up 0 to 10, explore 10 to 25, teaching 25 to 35 (how to start a puzzle: draw it, make a table, read the scale; click to reveal each step and answer), brain break 35 to 40, worksheet 40 to 70 with short teaching before each page and a check-together slide after it, talk time 70 to 80, exit ticket and certificates 80 to 90. If the class is behind, children finish the last question of each page at home; the check slides cover it.'))

# ---------- 2. warm-up: relay chain ----------
chain=[('Start','6 × 9','54'),('Then','add 46','100'),('Then','multiply by 7','700'),('Then','take away 250','450'),('Then','divide by 5','90'),('Last','change to h and min','1 h 30 min')]
body=h2('Warm-up: Relay chain')+p('Each answer is passed on. It is the start of the next question. Join in, or say “pass”: the tutor will always help.',34,600,MUTED)
CWd=530
for i,(k_,t,a) in enumerate(chain):
    L=128+(i%3)*(CWd+37); Tp=300+(i//3)*290
    body+=pin(L,Tp,CWd,p(k_,28,800,TEAL)+p(t,38,700),None,WHITE,24,'20px 26px',f'box-sizing:border-box;height:250px;border:4px solid {NAVY};box-shadow:8px 8px 0 {NAVY}')
    body+=pin(L+26,Tp+160,280,f'<p style="font-family:{HF};font-size:44px;font-weight:600;text-align:center">{E(a)}</p>','pop',YEL,16,'4px 10px',f'box-sizing:border-box;border:3px solid {NAVY}')
put('p3l10-warm1',sec('p3l10-warm1','0–5 MIN',body,
 'Minutes 5 to 8. Relay chain, made safe: the TUTOR reads each card; volunteers say the answer (a pass is always fine, and the tutor or the group gives it). The chain never depends on one child: if an answer is wrong the tutor says "Let us check together" and writes the correct number on screen, and the chain carries on from the correct number. No child is named as the one who broke the chain. Click to show each answer after it is said. '
 'Chain: 6 × 9 = 54 (tables), 54 + 46 = 100 (adding to the next hundred), 100 × 7 = 700, 700 − 250 = 450, 450 ÷ 5 = 90 (think 45 tens ÷ 5 = 9 tens), 90 minutes = 1 h 30 min (time). Second round if time: start with 8 × 7 and change the steps.'))
qs=[('1.','Value of the digit 7 in 4732?','700'),('2.','3/8 + 2/8 = ?','5/8'),('3.','47 ÷ 5 = ?','9 r 2'),('4.','Perimeter of a 6 cm by 4 cm rectangle?','20 cm'),('5.','2 kg 50 g = __ g','2050 g')]
body=h2('Quick questions')+''.join(qrow(128,250+i*125,1250,a,b) for i,(a,b,c) in enumerate(qs))+''.join(answer(1420,250+i*125,372,c) for i,(a,b,c) in enumerate(qs))
put('p3l10-warm2',sec('p3l10-warm2','5–10 MIN',body,'Minutes 5 to 10. One question from each part of our program. Read each aloud, give thinking time, then click. Ask "Which lesson does this remind you of?" Answers: 1) 700 (hundreds place). 2) 5/8 (add the eighths; the bottom number stays). 3) 9 remainder 2 (9 × 5 = 45, 2 left). 4) 20 cm (6 + 4 + 6 + 4). 5) 2050 g (not 250 g).'))

# ---------- explore ----------
g=''
tiles=['List','Measure']
for i,t in enumerate(tiles):
    x=10+i*810
    g+=f'<rect x="{x}" y="10" width="790" height="230" rx="18" fill="#FFF4D1" stroke="{NAVY}" stroke-width="4"/>'+T(x+395,226,t,32)
g+=''.join(f'<rect x="{255+j*100}" y="50" width="76" height="110" rx="10" fill="{YEL}" stroke="{NAVY}" stroke-width="4"/>'+T(293+j*100,128,d,56) for j,d in enumerate('369'))
g+=f'<rect x="870" y="90" width="670" height="60" fill="#FFE9A8" stroke="{NAVY}" stroke-width="4"/>'+T(1205,128,'120 cm ribbon: 3 pieces, each 10 cm longer',30)+f'<path d="M870 80 Q870 66 884 66 L1190 66 Q1205 66 1205 50 Q1205 66 1220 66 L1526 66 Q1540 66 1540 80" fill="none" stroke="{NAVY}" stroke-width="4"/>'
pic=svg(1630,250,g,'Two puzzle stations: digit cards 3, 6 and 9, and a 120 cm ribbon to cut into 3 pieces')
put('p3l10-explore1',explore1('p3l10-explore1','10–15 MIN',['Two stations, 7 minutes each: List, then Measure.','Work in pairs. Read the puzzle card aloud.','Before you solve it, decide: draw it, list it or make a table?','Stuck on the ribbon? Draw 3 pieces: a short one, then 10 cm longer, then 10 cm longer again.'],pic,
 'Minutes 10 to 25. Two stations only, so that the rotation fits online. Share the List card first (7 minutes), then the Measure card (7 minutes, the timer is on the screen); the tutor shares each card when the timer ends, and the last minutes to 25 are for explore talk. If the class is slow on the first card, shorten each station to 6 minutes. Ribbon scaffold (say it if a pair is stuck, do not tell the answer): draw the ribbon as 3 boxes, the short piece, then a piece with a 10 cm extra, then a piece with a 20 cm extra; take the extras (10 + 20) away from 120 cm. Pairs stay in the same breakout room. List: make every 3-digit number from the cards 3, 6, 9 (there are 6). '
 'Measure: a 120 cm ribbon is cut into 3 pieces, each piece 10 cm longer than the one before. Draw it and find each piece (30 cm, 40 cm, 50 cm). The graph and logic puzzles come next on worksheet page 1. Online: one station card on screen at a time, then report back.'))
put('p3l10-explore2',talk_qs('p3l10-explore2','15–25 MIN','Explore: talk about it',['How did you start each puzzle?','List station: how many numbers? How do you know you have them all?','Measure station: how long is each piece of ribbon?'],
 'Minutes 15 to 25. Gather the pairs. Answers: 1) Open: listen for "I drew it", "I listed them in order", "I made a table". 2) 6 numbers: 369, 396, 639, 693, 936, 963. Each hundreds digit has 2 numbers, so 3 × 2 = 6. 3) 30 cm, 40 cm and 50 cm: take away the extras (10 cm and 20 cm) from 120 cm: 90 cm, so 30 cm each; then give the extras back. Check: 30 + 40 + 50 = 120.'))

# ---------- teach 1: how to start ----------
ic_draw=svg(440,140,''.join(person(60+i*80,20,[YEL,WHITE,SKY,WHITE,WHITE][i]) for i in range(5)),'Icon: people in a queue')
ic_list=svg(440,140,''.join(T(30,40+i*44,f'{i+1}.',30,TEAL,'start')+f'<line x1="80" y1="{30+i*44}" x2="{380-i*60}" y2="{30+i*44}" stroke="{NAVY}" stroke-width="6" stroke-linecap="round"/>' for i in range(3)),'Icon: a list in order')
ic_table=svg(440,140,''.join(f'<rect x="{20+c*100}" y="{10+r*40}" width="100" height="40" fill="{YEL if r==0 else WHITE}" stroke="{NAVY}" stroke-width="3"/>' for r in range(3) for c in range(4)),'Icon: a table')
cards=[('Draw it',ic_draw,'queues, bar models, people in order.'),('List it',ic_list,'find ALL the ways: numbers, coins, shapes.'),('Make a table',ic_table,'clues (a logic grid), patterns that grow.')]
body=h2('How to start a puzzle')+p('Stuck? Do not just stare. Put the puzzle on paper.',34,600,MUTED)
for i,(t,ic,use) in enumerate(cards):
    body+=pin(128+i*572,320,480,p(t,44,800,TEAL)+ic+p('Use it for: '+use,30,600),'rise',WHITE,24,'26px 30px')
body+=pin(128,790,1664,p('A puzzle is hard to hold in your head. On paper you can see it, check it and explain it.',32,700),'fade',SOFT,20,'18px 28px')
put('p3l10-teach1',sec('p3l10-teach1','25–26 MIN',body,'Teach: the idea and why. "Today mixes everything. Clever inquirers do not know every answer straight away; they know how to START." Click each card and give an example from our P3 lessons: Draw it (bar models in Lesson 4, time lines in Lesson 9). List it (digit puzzles in Lesson 1, budgets in Lesson 9). Make a table (times-table patterns in Lesson 3). Click the last box and read it together. The next slides show each start in action.'))

# ---------- we1: draw it (queue) ----------
sp={3:(YEL,'Siti')}
base=queue(9,sp,show={3},aria='A queue with Siti')
front=queue(9,{0:(SKY,'1'),1:(SKY,'2'),2:(SKY,'3')},show={0,1,2},ends=False,aria='3 people in front of Siti')
back=queue(9,{4:(GREEN,''),5:(GREEN,''),6:(GREEN,''),7:(GREEN,''),8:(GREEN,'')},show={4,5,6,7,8},ends=False,aria='5 people behind Siti')
gap=min(150,(1664-260)/8)
body=h2('Draw it: a queue')+card(p('Siti is 4th from the front and 6th from the back of a queue. How many people are in the queue?',38,700))
body+=pin(128,380,1664,base)+pin(128,380,1664,front,'fade')+pin(128,380,1664,back,'fade')
body+=step(1,'4th from the front: 3 people in front of Siti.',top=620,size=34)
body+=step(2,'6th from the back: 5 people behind Siti.',top=720,size=34)
body+=answer(128,820,1664,'3 + 1 + 5 = 9 people.   (4 + 6 = 10 counts Siti twice: 10 − 1 = 9)')
put('p3l10-we1',sec('p3l10-we1','26–28 MIN',body,
 'Worked example: draw it. Ask first: "Is it 10?" Many children add 4 + 6. Click: the 3 people in front appear, then the 5 behind, then the steps and answer. (Click order: front people, back people, step 1, step 2, answer.) '
 'Think-aloud: "I draw Siti. 4th from the front means 3 people are in front of her. 6th from the back means 5 people behind her. Count: 3 + 1 + 5 = 9. If I add 4 + 6, I count Siti twice, so I take 1 away." Check by counting the drawing from both ends.'))
put('p3l10-try1',try_slide('p3l10-try1','28–29 MIN','Your turn: draw it','Draw the people before you answer.',[('a','Ravi is 2nd from the front and 8th from the back. How many people?','9'),('b','10 people. Ben is 3rd from the front. Place from the back?','8th'),('c','Two numbers add up to 30. One is 6 more than the other.','12 and 18')],
 'Whiteboards. a) 1 in front, Ravi, 7 behind: 9 (or 2 + 8 − 1). b) 2 in front, Ben, so 10 − 3 = 7 behind: Ben is 8th from the back (10 − 3 + 1). c) Draw two bars: take away the extra 6: 24; share: 12 and 12; give the 6 back: 12 and 18. Check 12 + 18 = 30.',36))

# ---------- we2: logic grid ----------
R=['Ben','Siti','Ravi']; C=['curry puff','kaya toast','popiah']
body=h2('Make a table: a logic grid')+card(p('Ben, Siti and Ravi each like a different snack. Clue 1: Ben does not like curry puff or popiah. Clue 2: Ravi does not like curry puff.',34,700))
body+=pin(128,400,1000,grid_svg(R,C))
steps_m=[[(0,0,'x'),(0,2,'x')],[(0,1,'t')],[(1,1,'x'),(2,1,'x')],[(2,0,'x'),(2,2,'t'),(1,0,'t'),(1,2,'x')]]
for m in steps_m: body+=pin(128,400,1000,grid_svg(R,C,m,base=False,aria='Marks in the grid'),'fade')
body+=pin(1150,400,642,p('Clue 1: cross out 2 boxes for Ben. Only kaya toast is left: ✓.',30,700),'rise',WHITE,20,'16px 22px')
body+=pin(1150,530,642,p('A ✓ means crosses in the rest of its column: nobody else has kaya toast.',30,700),'rise',WHITE,20,'16px 22px')
body+=pin(1150,680,642,p('Clue 2: Ravi is not curry puff, so popiah ✓. Siti: curry puff ✓.',30,700),'rise',WHITE,20,'16px 22px')
put('p3l10-we2',sec('p3l10-we2','29–31 MIN',body,
 'Worked example: make a table. Click order: Ben’s two crosses, Ben’s tick, the crosses in the kaya toast column, the last marks; the three side notes rise in between as you talk. '
 'Think-aloud: "A table keeps every clue in one place. Clue 1 tells me 2 things Ben does NOT like: 2 crosses. Only one box is left in his row, so a tick. A tick means nobody else can have kaya toast, so I cross out the rest of that column. Clue 2: Ravi is not curry puff, and kaya toast is gone, so Ravi likes popiah. Siti gets the last one: curry puff." Check each clue against the answer.'))
put('p3l10-try2',try_slide('p3l10-try2','31–32 MIN','Your turn: a small logic grid','Ali, Mei and Ben each choose a different colour: red, blue, green.',[('a','Mei does not choose red or blue. Ali does not choose red.','Mei: green'),('b','So what does Ali choose?','Ali: blue'),('c','And Ben?','Ben: red')],
 'Whiteboards: draw a 3 by 3 grid. Mei has 2 crosses, so green is the only one left: tick, then cross green for Ali and Ben. Ali is not red, and green is gone, so blue. Ben gets red. Check: Mei green (not red or blue ✓), Ali blue (not red ✓).',36))

# ---------- we3: bar graph ----------
bg=bar_graph([('Mon',12),('Tue',7),('Wed',15),('Thu',10)],16,2,24,bw=100,slot=180,aria='Bar graph of books borrowed: Monday 12, Tuesday 7, Wednesday 15, Thursday 10',ylab='Books',xlab='Day')
body=h2('Reading a bar graph: the scale first')+pin(128,230,880,bg)
body+=step(1,'Read the scale: 0, 2, 4, 6 … Each space stands for 2 books.',left=1040,top=250,width=752,size=32)
body+=step(2,'Tuesday’s bar stops halfway between 6 and 8, so it shows 7.',left=1040,top=400,width=752,size=32)
body+=step(3,'How many more on Wednesday than Tuesday? 15 − 7 = 8.',left=1040,top=550,width=752,size=32)
body+=answer(1040,700,752,'Altogether: 12 + 7 + 15 + 10 = 44 books')
put('p3l10-we3',sec('p3l10-we3','32–34 MIN',body,
 'Worked example: a bar graph (books borrowed from the class library). Ask first: "How many books on Tuesday?" Children who count spaces say 3 or 4. Click step 1: "Before reading any bar, read the scale. The lines go up in 2s." Step 2: "Tuesday is halfway between 6 and 8: 7." Step 3: "How many more" means the difference. '
 'Answer: add all four. The worksheet graph goes up in 10s with halfway values (5s); do not read it for them.'))
body=h2('Key idea: how to start a puzzle')+card(p('Stuck? Draw it, list it in order, or make a table. Then check every clue.',46,700))+card(p('Logic grid: a ✓ means crosses in the rest of its row and column. Bar graph: read the scale first.',36,600,MUTED))
put('p3l10-key',sec('p3l10-key','34–35 MIN',body,'Say the key idea together. Common mistakes to watch for during the worksheet: (1) Queues: adding the two places and counting the person twice. (2) Bar graphs: counting spaces as 1 instead of reading the scale; missing the halfway values 45 and 55. (3) Logic grids: a tick without crossing out the rest of the row and column. (4) Digit cards: missing a number because the list is not in order. (5) Matchstick pattern: 4 sticks for every square (shared sticks are counted twice).'))
put('p3l10-break',dark_slide('p3l10-break','35–40 MIN','Brain break','<p style="font-size:48px;font-weight:600">Freeze dance with maths. When the music stops, the tutor shows a 24-hour time: make the clock hands with your arms!</p>','Then: a drink of water and back to our seats.','Five minutes. Show 15:00, 18:00, 21:15, 09:30. Online: children stay in view of the camera and move in place.',TEAL,'h2',110))

put('p3l10-ws1',ws_preview('p3l10-ws1','40–52 MIN','Worksheet page 1: with your partner',[('Q1','The drinks bar graph. Read the scale: the lines go up in 10s.'),('Q2','The CCA logic grid. Use a clue that tells you something for sure.')],'Stuck? Draw it, list it, or make a table.',
 'Minutes 40 to 52. Walk around. Ask "How did you start?" and "Which clue did you use first?" before helping. Q1c: they must find the missing number first (200 − 150), then draw the bar to the 50 line. Q2: if a pair is stuck, ask "Who can be in the choir?" (clue 2 and clue 1 rule out three people).'))
put('p3l10-ws1ans',check_slide('p3l10-ws1ans','52–54 MIN','Page 1: check together',[('Q1','a) Kopi   b) 25 cups   c) 50 cups (bar to the 50 line)   d) Milo and Kopi'),('Q2','Ali: football.  Mei: chess.  Ravi: swimming.  Siti: choir.')],
 'Click after a pair explains. Q1: Milo 45, Teh 30, Kopi 55, Bandung 20. b) 55 − 30 = 25. c) 45 + 30 + 55 + 20 = 150; 200 − 150 = 50. d) Check all pairs: only 45 + 55 = 100. '
 'Q2: Clue 2 says Mei and Ravi are not in the choir; clue 1 says Ali is not; so Siti is in the choir. Clue 3: the swimmer has 4 letters: Ravi or Siti; Siti is in the choir, so Ravi swims. Ali: not choir, not chess, not swimming, so football. Mei: chess. The puzzle has exactly one answer.'))

# ---------- teach before page 2 ----------
body=h2('List it: in order, so none are missed')
body+=pin(128,250,800,p('Make 3-digit numbers with 3, 6 and 9. How many are even?',32,700),None,WHITE,20,'18px 26px')
for i,(hd,ns) in enumerate([('3 first','369,  396'),('6 first','639,  693'),('9 first','936,  963')]):
    body+=pin(128,400+i*95,800,p(f'<span style="color:{TEAL};font-weight:800">{hd}:</span>  {ns}',34,700,raw=True),'rise',WHITE,16,'12px 24px')
body+=pin(128,700,800,p('6 numbers (2 for each first digit). Even: 396 and 936.',32,700),'fade',SOFT,20,'16px 24px')
body+=pin(992,250,800,p('Riddle: I am an even 2-digit number. My digits add up to 7. My tens digit is bigger than my ones digit. Find ALL.',32,700),None,WHITE,20,'18px 26px')
for i,t in enumerate(['Even: the ones digit is 0, 2, 4 or 6.','70 ✓   52 ✓   34: 3 is not bigger than 4   16: no','Answers: 70 and 52.']):
    body+=pin(992,470+i*110,800,p(t,32,700),'rise',SOFT if i==2 else WHITE,16,'14px 24px')
put('p3l10-teachlist',sec('p3l10-teachlist','54–56 MIN',body,
 'Teach before worksheet page 2 (Q4 and Q6). Left: "I list them in order. Start with 3 in the hundreds place: 369, 396. Then 6: 639, 693. Then 9: 936, 963. Two for each first digit, so 6. Even numbers end in an even digit: only 6 is even, so 396 and 936." '
 'Right: "For a find-ALL riddle, I list every case for one clue, then cross out the ones that break another clue." The worksheet uses different digits and an odd-number riddle: do not do them here.'))
def tbl_row(n,x0=20,y0=70,s=90):
    b=''
    for i in range(n): b+=f'<rect x="{x0+i*s}" y="{y0}" width="{s}" height="{s}" fill="#F3D9B1" stroke="{NAVY}" stroke-width="4"/>'
    for i in range(n): b+=f'<circle cx="{x0+i*s+s/2}" cy="{y0-26}" r="16" fill="{SKY}" stroke="{NAVY}" stroke-width="3"/><circle cx="{x0+i*s+s/2}" cy="{y0+s+26}" r="16" fill="{SKY}" stroke="{NAVY}" stroke-width="3"/>'
    b+=f'<circle cx="{x0-26}" cy="{y0+s/2}" r="16" fill="{SKY}" stroke="{NAVY}" stroke-width="3"/><circle cx="{x0+n*s+26}" cy="{y0+s/2}" r="16" fill="{SKY}" stroke="{NAVY}" stroke-width="3"/>'
    return b
pic=svg(1100,200,f'<g transform="translate(40,10)">{tbl_row(1)}</g><g transform="translate(260,10)">{tbl_row(2)}</g><g transform="translate(570,10)">{tbl_row(3)}</g>','Tables in a row: 1 table seats 4, 2 tables seat 6, 3 tables seat 8')
W7=[220]+[120]*7
body=h2('Make a table: a growing pattern')+pin(128,230,1100,pic)
body+=pin(1260,240,532,p('1 table seats 4. Each new table adds 2 seats.',32,700),None,SOFT,20,'18px 24px')
body+=trow(128,470,['Tables','1','2','3','4','5','6','7'],W7,header=True,size=34)
body+=trow(128,550,['People','4','6','8','','','',''],W7,size=34)
body+=trow(128,550,['People','4','6','8','10','12','14','16'],W7,'rise',size=34)
body+=step(1,'7 tables seat 16 people.',top=660,width=900,size=32)
body+=step(2,'20 people? Keep going: 8 tables 18, 9 tables 20. So 9 tables.',top=760,size=32)
put('p3l10-teachtable',sec('p3l10-teachtable','56–57 MIN',body,
 'Teach before worksheet page 2 (Q5). "Why only 2 more seats for each new table? Because where two tables join, those seats are lost." Click to fill the table, then the steps. Think-aloud: "The table goes 4, 6, 8 … add 2 each time. I keep the table going until I reach what I need." Going backwards (20 people) uses the same table. The worksheet pattern adds a different number: let them find it.'))
q2=queue(6,{1:(YEL,'Mei'),5:(GREEN,'Ben'),2:(WHITE,''),3:(WHITE,''),4:(WHITE,''),0:(WHITE,'')},show={1,5},aria='Queue: Mei near the front, Ben last')
q2b=queue(6,{0:(SKY,'1'),2:(PINK,''),3:(PINK,''),4:(PINK,'')},show={0,2,3,4},ends=False,aria='1 in front of Mei, 3 between Mei and Ben')
body=h2('Draw it: people in between')+card(p('Mei is 2nd from the front. Ben is last. There are 3 people between them. How many in the queue?',36,700))
body+=pin(128,370,1664,q2)+pin(128,370,1664,q2b,'fade')
body+=step(1,'In front of Mei: 1 person. Then Mei, then 3 people, then Ben.',top=620,size=34)
body+=answer(128,730,1664,'1 + 1 + 3 + 1 = 6 people.  Count your drawing to check.')
put('p3l10-teachbetween',sec('p3l10-teachbetween','57–58 MIN',body,
 'Teach before worksheet page 2 (Q3). Ask first: "Is it 2 + 3 = 5?" No: that forgets Ben. Click the drawing, the step and the answer. Think-aloud: "I draw Mei 2nd, so 1 person in front. Then the 3 between, then Ben. Count every person: 6." The worksheet Q3b has different names; let children draw it themselves.'))
put('p3l10-ws2',ws_preview('p3l10-ws2','58–67 MIN','Worksheet page 2: on your own',[('Q3','Queues. Draw the people.'),('Q4','Digit cards 2, 5, 8. List them in order.'),('Q5','Matchstick squares. Make a table.'),('Q6','If time: a number riddle. Find ALL the answers.')],'Ready for more? Stretch and Challenge come next.','Children work alone. Note who needs a short catch-up. Q6: check that children list every case (ones digit 1, 3 or 5) and cross out, not stop at the first answer.'))
put('p3l10-ws2ans',check_slide('p3l10-ws2ans','67–70 MIN','Page 2: check together',[('Q3','a) 7 people   b) 6 people'),('Q4','258, 285, 528, 582, 825, 852.   Odd: 2.   Closest to 600: 582'),('Q5','13, 16, 19.   8 squares: 25 sticks.   31 sticks: 10 squares'),('Q6','411, 321, 213')],
 'Click after a child explains. Q3a: 2 in front, Ben, 4 behind: 7 (3 + 5 − 1). Q3b: 1 in front of Ali, Ali, 3 between, Siti: 6. Q4: odd ones end in 5: 285 and 825. 582 is 18 from 600; 528 is 72 away. '
 'Q5: the first square needs 4 sticks, each new square adds 3 (it shares a side). 8 squares: 4 + 7 × 3 = 25. Keep the table going: 22, 25, 28, 31 at 10 squares. Q6: digits add to 6, none 0, odd: ones digit 1 (hundreds and tens add to 5: 41 or 32, hundreds bigger: 411, 321), ones 3 (add to 3: 21: 213), ones 5 (add to 1: impossible).'))

# ---------- stretch, challenge ----------
st=[('1.','A bar graph shows stamps: Ali 35 and Ben 20. Mei has 15 more than Ben. Siti has as many as Ali and Ben together. How many stamps altogether?'),('2.','Ali, Ben and Siti stand in a line. Ali is not first. Ben is just behind Siti. Who is first?'),('3.','A snail climbs a 12 m wall. Each day it climbs up 5 m; each night it slides down 2 m. On which day does it reach the top?')]
put('p3l10-stretch',sec('p3l10-stretch','For early finishers',h2('Stretch')+''.join(num_card(a,b,34) for a,b in st),
 'For children who finish early. Answers: 1) 145 (Mei 20 + 15 = 35; Siti 35 + 20 = 55; 35 + 20 + 35 + 55 = 145). 2) Siti: if Ben is just behind Siti, the line is Siti, Ben, Ali or Ali, Siti, Ben; Ali is not first, so Siti, Ben, Ali. 3) Day 4: make a table: end of day 1: highest point 5 m (night: slides back to 3 m), day 2: highest point 8 m (night: 6 m), day 3: highest point 11 m (night: 9 m), day 4: 9 + 5 = 14 m, past the top. Many children say day 4 because 12 ÷ 3 = 4, which is the right day but the wrong reason: check the table.'))
ch=[('1.','In a queue, Siti is 6th from the front and Ravi is 4th from the back. There are 3 children between them, and Siti is in front of Ravi. How many children are in the queue?'),('2.','A bar graph shows paper collected by 4 classes. 3P1 collected 10 kg more than 3P2. 3P3 collected the same as 3P1. 3P4 collected 5 kg less than 3P2. Altogether: 135 kg. How much did each class collect?')]
put('p3l10-challenge',sec('p3l10-challenge','Challenge',h2('Challenge')+''.join(num_card(a,b,34) for a,b in ch),
 'Use as a pair challenge or in talk time. Ask for the reason every time. Answers: 1) 13 children (5 in front of Siti, Siti, 3 between, Ravi, 3 behind Ravi: 5 + 1 + 3 + 1 + 3 = 13). 2) 3P1 40 kg, 3P2 30 kg, 3P3 40 kg, 3P4 25 kg (compare everything with 3P2: the extras are +10, +10 and −5, so 135 − 15 = 120 kg is 4 equal parts of 30 kg).'))
# see it
qg=(T(40,30,'FRONT',26,TEAL,'start')+person(110,70,YEL,'Siti')+person(560,70,GREEN,'Ravi')+
    T(20,250,'6th from front',26,TEAL,'start')+T(560,250,'4th from back',26,TEAL)+
    ''.join(f'<rect x="{230+j*80}" y="96" width="50" height="62" rx="14" fill="{PINK}" stroke="{NAVY}" stroke-width="3"/>' for j in range(3))+T(320,62,'3 between',26,RED)+
    f'<rect x="40" y="300" width="720" height="150" rx="14" fill="{SOFT}" stroke="{NAVY}" stroke-width="3"/>'+T(400,360,'How many are in front of Siti?',28)+T(400,410,'How many are behind Ravi?',28))
d1=svg(800,480,qg,'Queue: Siti 6th from the front, 3 children between, Ravi 4th from the back')
bb=''
for i,(n,lab,extra) in enumerate([('3P1','3P2 + 10',1),('3P2','?',0),('3P3','same as 3P1',1),('3P4','3P2 − 5',-1)]):
    y=30+i*95
    bb+=T(10,y+52,n,30,anchor='start')+f'<rect x="110" y="{y}" width="300" height="64" fill="{SKY}" stroke="{NAVY}" stroke-width="4"/>'
    if extra==1: bb+=f'<rect x="410" y="{y}" width="100" height="64" fill="{YEL}" stroke="{NAVY}" stroke-width="4"/>'+T(460,y+43,'10',28)
    if extra==-1: bb+=f'<rect x="360" y="{y}" width="50" height="64" fill="{WHITE}" stroke="{RED}" stroke-width="4" stroke-dasharray="8 6"/>'+T(385,y+43,'5',26,RED)
    bb+=T(640,y+43,lab,26,MUTED)
bb+=f'<rect x="40" y="420" width="720" height="70" rx="14" fill="{SOFT}" stroke="{NAVY}" stroke-width="3"/>'+T(400,466,'All four bars together: 135 kg',30)
d2=svg(800,500,bb,'Four bars: 3P1 is 3P2 plus 10, 3P2 unknown, 3P3 same as 3P1, 3P4 is 3P2 minus 5, total 135 kg')
def cardsvg(t,s,w,h): return f'<div style="background:{WHITE};border-radius:24px;padding:20px 24px;display:flex;flex-direction:column;gap:10px;flex:1;min-width:0"><p style="font-size:30px;font-weight:700;color:{TEAL}">{E(t)}</p>{s.replace(f"style=\"width:{w}px;height:{h}px;","style=\"width:100%;height:auto;")}</div>'
body=h2('Challenge: see it')+f'<div style="display:flex;gap:32px;align-items:flex-start">{cardsvg("Q1: draw the queue",d1,800,480)}{cardsvg("Q2: compare every class with 3P2",d2,800,500)}</div>'
put('p3l10-chdiag',sec('p3l10-chdiag','Challenge',body,'Show after pairs have tried the Challenge, or if they are stuck. The diagrams show the problem, not the answer. Ask: What do you know? What do you not know yet? For Q1: "Can you draw the children in front of Siti and behind Ravi?" For Q2: "Why compare with 3P2?" (every clue talks about 3P2 or 3P1). Answers are in the Challenge slide notes.'))
body=h2('Challenge: walk-through')+pin(128,250,800,p('Q1: draw it',38,800,TEAL))
for i,t in enumerate(['Siti is 6th from the front: 5 children in front of her.','Then Siti, 3 children, Ravi: Ravi is 6 + 3 + 1 = 10th from the front.','Ravi is 4th from the back: 3 children behind him.','10 + 3 = 13 children ✓']): body+=pin(128,330+i*125,800,p(t,32),'rise',WHITE)
body+=pin(992,250,800,p('Q2: take away the extras',38,800,TEAL))
for i,t in enumerate(['Extras compared with 3P2: +10, +10, and −5.','135 − 10 − 10 + 5 = 120 kg is 4 equal parts.','120 ÷ 4 = 30. 3P2 has 30 kg.','3P1 40, 3P3 40, 3P4 25. Check: 135 ✓']): body+=pin(992,330+i*125,800,p(t,32),'rise',WHITE)
put('p3l10-chwalk',sec('p3l10-chwalk','Challenge',body,'Use after pairs have tried, with the "see it" slide. Q1: the trap is to add 6 + 3 + 4 = 13 by luck or 6 + 4 + 3 + 2 by guessing; the drawing makes it sure: 5 + 1 + 3 + 1 + 3. Q2: 3P4 is 5 kg LESS than 3P2, so to make it equal we add 5 back (135 − 20 + 5 = 120). Check: 40 + 30 + 40 + 25 = 135.'))
body=h2('Talk time')+card(chip('TALK TIME',YEL,NAVY)+p('Choose one puzzle from today. How did you START it, and how do you know you are right? You can share, share with a partner, or pass.',40,600))+card(p('Sentence starters:',34,400,MUTED)+p('“I started by …”   “I noticed that …”   “I know because …”',38,600))
put('p3l10-talk',sec('p3l10-talk','70–80 MIN',body,'Minutes 70 to 80. Pairs talk for 2 minutes, then volunteers share (a pass is always fine, and nobody is called on by name). Ask: "Draw it, list it or make a table: which helped you most today? Why?" Teaching a puzzle to the group is only for volunteers. Also ask: "Why do we take away 1 in a queue puzzle?" (the person is counted from the front and from the back). Praise the reasons, not only the answers.'))
body=h2('Exit ticket')+card(chip('EXIT TICKET')+p('Ali is 4th from the front and 4th from the back of a queue. How many people are in the queue? How did you start?',44,600))+card(p('Write your answer on a slip of paper and show it to your tutor on camera. Then collect your last stamp.',34,400))
put('p3l10-exit',sec('p3l10-exit','80–85 MIN',body,'Minutes 80 to 85. Answer: 7 people (3 in front, Ali, 3 behind; 4 + 4 − 1 = 7), started by drawing it. A child who writes 8 has counted Ali twice. The favourite-lesson line is open: use it to plan next steps. Next slide: look back (2 minutes). Extension: write a logic grid puzzle with 3 people and 3 things for a friend, and check it has exactly one answer.'))
put('end',dark_slide('end','WELL DONE, INQUIRERS · 88–90 MIN','Keep asking why',f'<p style="font-family:{HF};font-size:64px;font-weight:500;color:{YEL}">Notice it. Test it. Explain why.</p>','Certificates and a last stamp for every inquirer.','Minutes 88 to 90. Hand out certificates and stamp the journal. Invite volunteers to name one puzzle they enjoyed in the program (pass is fine). Tell each child one specific thing they did well. Give parents the one-page summary from the tutor guide.'))

# ---------- write ----------
order=['p3l10-title','p3l10-warm1','p3l10-warm2','p3l10-explore1','p3l10-explore2','p3l10-teach1','p3l10-we1','p3l10-try1','p3l10-we2','p3l10-try2','p3l10-we3','p3l10-key','p3l10-break','p3l10-ws1','p3l10-ws1ans','p3l10-teachlist','p3l10-teachtable','p3l10-teachbetween','p3l10-ws2','p3l10-ws2ans','p3l10-stretch','p3l10-challenge','p3l10-chdiag','p3l10-chwalk','p3l10-talk','p3l10-exit','end']
import p3_gifted; order[:]=p3_gifted.add(S,order,10)  # close-the-gaps: warm-up check + look-back slides
assert set(order)==set(S), set(order)^set(S)
for i,h in S.items(): open(os.path.join(D,'slides',i+'.html'),'w').write(h)
deck={'v':4,'createdOnFiles':{'v':1,'at':datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')},'lists':'css',
      'title':'Math Inquirers P3: Lesson 10 – Challenge Day','order':order,'cover':'p3l10-title',
      'sections':{'s1':{'description':'Warm-up and explore','start':'p3l10-title'},'s2':{'description':'Teach: how to start a puzzle (draw it, make a table, read the scale)','start':'p3l10-teach1'},'s3':{'description':'Worksheet with teaching before each page','start':'p3l10-break'},'s4':{'description':'Stretch, challenge, talk, exit and close','start':'p3l10-stretch'}},
      'faces':{'fredoka':{'family':'Fredoka','href':'https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&display=swap'},'nunito-sans':{'family':'Nunito Sans','href':'https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@400;600;700&display=swap'}},
      'designSystems':[]}
json.dump(deck,open(os.path.join(D,'deck.json'),'w'),indent=1,ensure_ascii=False)
print(len(order),'slides')
