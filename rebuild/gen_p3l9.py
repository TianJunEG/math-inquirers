"""Math Inquirers P3, Lesson 9: Measure and Money Masters. Writes split/p3l9/project (deck.json + slides/*.html)."""
import json,os,sys,datetime
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,H)
from slidekit import *
D=os.path.join(H,'..','split','p3l9','project'); os.makedirs(os.path.join(D,'slides'),exist_ok=True)
S={}
def put(i,h): S[i]=h
RED='#D64545'; GREEN='#BFE3DC'; PINK='#F4A6A6'; BLUE='#9CC9EE'

def svg(w,h,body,aria,style=''): return f'<svg aria-label="{E(aria)}" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="width:{w}px;height:{h}px;{style}">{body}</svg>'
def T(x,y,s,size=30,fill=NAVY,anchor='middle',weight=800): return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" fill="{fill}" font-family="Nunito Sans, Arial">{E(s)}</text>'
def num_card(a,b): return card(p(f'<span style="color:{TEAL}">{E(a)}</span>  {E(b)}',36,600,raw=True))

# ---------- fixed-layout slides shared by every lesson ----------
def title_slide(sid,n,week,title,sub,today,notes):
    return (f'<section id="{sid}" data-transition="fade" style="background:{NAVY};color:{CREAM};font-family:{BF};padding:128px 128px 160px;display:flex;flex-direction:column;justify-content:center;gap:36px">\n'
            f'<p style="font-size:32px;font-weight:700;letter-spacing:4px;color:{YEL}">LESSON {n}  •  WEEK {week}</p>\n'
            f'<h1 style="font-family:{HF};font-size:110px;font-weight:600;line-height:1.05">{E(title)}</h1>\n'
            f'<p style="font-size:44px;color:#C9D4EC">{E(sub)}</p>\n'
            f'<div style="background:#26385F;border-radius:24px;padding:40px;display:flex;flex-direction:column;gap:12px"><p style="font-size:28px;font-weight:700;letter-spacing:3px;color:{YEL}">TODAY WE WILL</p><p style="font-size:44px;font-weight:600">{E(today)}</p></div>\n'
            f'<p style="position:absolute;left:128px;bottom:64px;width:1400px;font-size:24px;color:#B7C3DD">{E(FOOT)}</p>\n<aside>{E(notes)}</aside>\n</section>\n')
def break_slide(sid,time,head,text,small,notes):
    return (f'<section id="{sid}" data-transition="fade" style="background:{TEAL};color:{CREAM};font-family:{BF};padding:128px 128px 160px;display:flex;flex-direction:column;justify-content:center;gap:36px">\n'
            f'<p style="font-size:32px;font-weight:700;letter-spacing:4px;color:{YEL}">{E(time)}</p>\n'
            f'<h2 style="font-family:{HF};font-size:110px;font-weight:600;line-height:1.05">{E(head)}</h2>\n'
            f'<p style="font-size:48px;font-weight:600">{E(text)}</p>\n<p style="font-size:36px;color:#D7EFEA">{E(small)}</p>\n'
            f'<p style="position:absolute;left:128px;bottom:64px;width:1400px;font-size:24px;color:#D7EFEA">{E(FOOT)}</p>\n<aside>{E(notes)}</aside>\n</section>\n')
def explore1(sid,time,steps,pic,notes):
    ol='<ol style="font-size:32px;font-weight:600;padding-left:48px;margin:0;display:flex;flex-direction:column;gap:6px">'+''.join(f'<li>{E(s)}</li>' for s in steps)+'</ol>'
    body=h2('Explore: what to do')+card(chip('EXPLORE')+ol,extra='padding:24px 40px')+card(pic,extra='padding:16px 24px;align-items:center')
    return sec(sid,time,body,notes)
def talk_qs(sid,time,head,qs,notes):
    return sec(sid,time,h2(head)+''.join(card(p(f'<span style="color:{TEAL}">{i+1}.</span>  {E(q)}',40,600,raw=True)) for i,q in enumerate(qs)),notes)
def talk_slide(sid,time,prompt,notes):
    body=h2('Talk time')+card(chip('TALK TIME',YEL,NAVY)+p(prompt,42,600))+card(p('Sentence starters:',34,400,MUTED)+p('“I noticed that …”   “I tested it by …”   “I know because …”',38,600))
    return sec(sid,time,body,notes)
def exit_slide(sid,time,q,notes,extra=''):
    body=h2('Exit ticket')+card(chip('EXIT TICKET')+p(q,46,600))+card(p(extra or 'Write your answer on a slip of paper. Show it to your tutor. Then collect your stamp in your inquiry journal.',34,400))
    return sec(sid,time,body,notes)

# ---------- 1. title ----------
put('p3l9-title',title_slide('p3l9-title',9,5,'Measure and Money Masters','Length, mass, volume, money and time',
 'Change to one unit, plan a budget, and draw a time line for durations and the 24-hour clock.',
 'Objective: Change compound units (m and cm, kg and g, ℓ and ml, $ and ¢) to one unit to compare, add and subtract; plan a budget; find durations, start and end times by drawing a time line, in 12-hour and 24-hour time. Heuristics taught: (1) change to one unit; (2) draw a time line and jump to the next o’clock. '
 'Materials: Party menu cards (one per pair), play money, a metre ruler or measuring tape, a kitchen scale and a measuring jug if available, a clock with movable hands, mini whiteboards. '
 'Online: Show the menu card on screen; children use paper and pencil. Pairs work in breakout rooms and type their best party plan in the chat. '
 'Time plan: warm-up 0 to 10, explore 10 to 25, teaching 25 to 35 (change to one unit, then the time line; click to reveal each step and answer), brain break 35 to 40, worksheet 40 to 70 with short teaching before each page and a check-together slide after it, talk time 70 to 80, exit ticket 80 to 90. If the class is behind, children finish the last question of each page at home; the check slides cover it.'))

# ---------- 2. warm-up game: name that unit ----------
cards=[('A bus is 12 __ long.','m'),('A pencil is 15 __ long.','cm'),('An MRT ride of about 15 __','km'),('A bag of rice: 5 __','kg'),
       ('An eraser: 20 __','g'),('A spoon of medicine: 5 __','ml'),('A fish tank holds 40 __','ℓ'),('A watermelon: 3 __','kg')]
body=h2('Warm-up: Name that unit')+p('Write the best unit: m, cm, km, g, kg, ml or ℓ.',36,600,MUTED)
CWd=392
for i,(t,a) in enumerate(cards):
    L=128+(i%4)*(CWd+32); Tp=300+(i//4)*290
    body+=pin(L,Tp,CWd,p(t,34,700),None,WHITE,24,'22px 24px',f'box-sizing:border-box;height:250px;border:4px solid {NAVY};box-shadow:8px 8px 0 {NAVY}')
    body+=pin(L+24,Tp+150,120,f'<p style="font-family:{HF};font-size:48px;font-weight:600;text-align:center">{E(a)}</p>','pop',YEL,16,'4px 10px',f'box-sizing:border-box;border:3px solid {NAVY}')
put('p3l9-warm1',sec('p3l9-warm1','0–5 MIN',body,
 'Minutes 0 to 5. Name that unit. Read each card aloud; children write the unit on whiteboards and hold them up together, then click to show (the cards reveal in order). '
 'Ask each time: "Why not the other units?" A bus is 12 m (12 cm is a finger, 12 km is a long trip). A pencil is 15 cm. An MRT ride of about 15 km. Rice 5 kg. An eraser about 20 g. Medicine 5 ml. A fish tank about 40 ℓ. A watermelon about 3 kg. '
 'Quick finisher: "Put these in order: 1 m, 90 cm, 1 km." (90 cm, 1 m, 1 km). Watch for children who mix up mass and volume units (kg for a drink).'))

# ---------- 3. quick questions ----------
qs=[('1.','1 m 40 cm = __ cm','140 cm'),('2.','3 kg = __ g','3000 g'),('3.','2 ℓ 50 ml = __ ml','2050 ml'),('4.','1 hour 20 minutes = __ minutes','80 min'),('5.','2:00 p.m. in 24-hour time','14:00')]
body=h2('Quick questions')+''.join(qrow(128,250+i*125,1250,a,b) for i,(a,b,c) in enumerate(qs))+''.join(answer(1420,250+i*125,372,c) for i,(a,b,c) in enumerate(qs))
put('p3l9-warm2',sec('p3l9-warm2','5–10 MIN',body,'Minutes 5 to 10. Read each aloud, give thinking time, take answers, then click to show. Answers: 1) 140 cm (100 + 40). 2) 3000 g. 3) 2050 ml: watch for 250 ml, the most common mistake; 2 ℓ is 2000 ml and 50 more. 4) 80 minutes (60 + 20), not 120. 5) 14:00 (2 + 12). Ask after 3: "Why is it not 250?"'))

# ---------- 4-5. explore ----------
menu=[('Pizza','$8.90',YEL),('Chicken wings','$6.50','#F7B26B'),('Curry puffs','$4.20','#F3D9B1'),('Fruit punch 2 ℓ','$3.15',PINK),('Cupcakes','$5.75',SKY),('Balloons','$2.40',GREEN)]
g=''
for i,(n,pr,c) in enumerate(menu):
    x=10+i*270
    g+=f'<rect x="{x}" y="10" width="250" height="200" rx="18" fill="{c}" stroke="{NAVY}" stroke-width="4"/>'+T(x+125,70,n,28)+f'<rect x="{x+45}" y="110" width="160" height="70" rx="12" fill="{WHITE}" stroke="{NAVY}" stroke-width="3"/>'+T(x+125,158,pr,40)
pic=svg(1630,220,g,'Party menu: pizza $8.90, chicken wings $6.50, curry puffs $4.20, fruit punch 2 litres $3.15, cupcakes $5.75, balloons $2.40')
put('p3l9-explore1',explore1('p3l9-explore1','10–15 MIN',['You have $20 to plan a party for 8 friends.','Each friend drinks 250 ml of punch. Buy at least 2 ℓ of punch (any number of bottles).','Buy at least one food. You may buy more than one of an item. Spend as close to $20 as you can.','Challenge: can you spend exactly $20?'],pic,
 'Minutes 10 to 15. Party planner. Pairs use the menu card and play money (or paper). You may buy more than one of an item. Punch: 8 × 250 ml = 2000 ml = 2 ℓ, so 1 bottle is the least; the rule is "at least 2 ℓ of punch (any number of bottles) and at least one food". '
 'Let pairs try first; prompt with "How did you add the prices?" Ways that cost exactly $20 (there are exactly 3): pizza + 2 punch + 2 balloons ($8.90 + $6.30 + $4.80); wings + 2 punch + 3 balloons ($6.50 + $6.30 + $7.20); cupcakes + 3 punch + 2 balloons ($5.75 + $9.45 + $4.80). '
 'Hint for exact $20: look at the cents. Only the punch (15¢) and the cupcakes (75¢) end in 5, so you need an even number of those altogether. Online: share the menu on screen; pairs type their plan in the chat.'))
put('p3l9-explore2',talk_qs('p3l9-explore2','15–25 MIN','Explore: talk about it',['How much punch do 8 friends need? How many bottles?','Who got closest to $20? How did you add the prices?','Can you spend exactly $20? How many ways?'],
 'Minutes 15 to 25. Let pairs keep working, then gather to answer. Answers: 1) 8 × 250 ml = 2000 ml = 2 ℓ: at least 1 bottle, more is allowed. 2) Open: changing to cents (890 + 315 = 1205¢) or adding dollars then cents both work. 3) Yes, exactly 3 ways (see the notes on the previous slide). Ask: "How do you know there are no more?" A strong group can reason with the cents digits.'))

# ---------- 6. teach: change to one unit ----------
U=5.2
bar=(f'<rect x="10" y="10" width="{100*U}" height="80" rx="8" fill="{SKY}" stroke="{NAVY}" stroke-width="4"/>'+T(10+50*U,62,'1 m = 100 cm',30)+
     f'<rect x="{10+100*U}" y="10" width="{100*U}" height="80" rx="8" fill="{SKY}" stroke="{NAVY}" stroke-width="4"/>'+T(10+150*U,62,'1 m = 100 cm',30)+
     f'<rect x="{10+200*U}" y="10" width="{35*U}" height="80" rx="8" fill="{YEL}" stroke="{NAVY}" stroke-width="4"/>'+T(10+217.5*U,62,'35 cm',28)+
     T(10+235*U+30,62,'= 235 cm',40,TEAL,'start'))
body=h2('Change to ONE unit')+card(p('1 m = 100 cm  •  1 kg = 1000 g  •  1 ℓ = 1000 ml  •  $1 = 100¢',38,700),SOFT,'padding:18px 32px')
body+=pin(128,370,1664,p('2 m 35 cm',36,800,TEAL)+svg(1600,100,bar,'2 metres 35 centimetres drawn as 100 cm, 100 cm and 35 cm: 235 cm'))
for i,t in enumerate(['1 kg 250 g = 1000 g + 250 g = 1250 g','1 ℓ 300 ml = 1000 ml + 300 ml = 1300 ml','$3.45 = 300¢ + 45¢ = 345¢']):
    body+=pin(128,560+i*96,960,p(t,36,700),'rise',WHITE,18,'14px 26px')
body+=pin(1180,560,560,p('Careful! 2 m 5 cm = 205 cm, not 25 cm. 3 kg 40 g = 3040 g.',34,700),'fade',SOFT,20,'22px 26px')
body+=pin(1180,760,612,p('Why? In one unit we can compare, add and take away like normal numbers.',30,700,TEAL),'fade',None)
put('p3l9-teach1',sec('p3l9-teach1','25–27 MIN',body,
 'Teach heuristic 1: change to one unit. Hold up a metre ruler: "This is 1 m, 100 cm." Point to the bar: 2 m is 200 cm, and 35 cm more is 235 cm. Click the three rows: each time, the big unit becomes the small unit and we add the rest. '
 'Click "Careful!": "How do I write 2 m 5 cm in cm? Some people write 25. Is that right? 2 m alone is 200 cm, so it is 205." Same for 3 kg 40 g = 3040 g, not 340 g. '
 'Click "Why?": "Once everything is in the same unit, the numbers behave like the numbers we already know." Going back: 1650 g = 1000 g + 650 g = 1 kg 650 g.'))

# ---------- 7. worked example: flour ----------
k=0.62
fb=(f'<rect x="10" y="40" width="{2100*k}" height="80" rx="8" fill="{SKY}" stroke="{NAVY}" stroke-width="4"/>'+
    f'<rect x="{10+(2100-850)*k}" y="40" width="{850*k}" height="80" rx="8" fill="{WHITE}" stroke="{RED}" stroke-width="4" stroke-dasharray="12 8"/>'+
    T(10+(2100-850)*k/2,92,'left: ?',32)+T(10+(2100-425)*k,92,'used 850 g',32,RED)+
    f'<path d="M10 30 L10 14 L{10+2100*k} 14 L{10+2100*k} 30" fill="none" stroke="{TEAL}" stroke-width="4"/>')
fb=svg(1320,140,f'<g transform="translate(0,18)">{fb}</g>'+T(10+1050*k,24,'2 kg 100 g',28,TEAL),'Bar: 2 kg 100 g of flour, 850 g used, the rest left')
body=h2('Worked example: change, then work')+card(p('A bag has 2 kg 100 g of flour. Mum uses 850 g. How much flour is left?',40,700))
body+=pin(128,364,1664,fb)
body+=step(1,'Change to grams:  2 kg 100 g = 2000 g + 100 g = 2100 g',top=530,size=34)
body+=step(2,'Take away:  2100 g − 850 g = 1250 g',top=630,size=34)
body+=step(3,'Change back:  1250 g = 1000 g + 250 g = 1 kg 250 g',top=730,size=34)
body+=answer(1100,830,640,'Check: 1250 + 850 = 2100 ✓')
put('p3l9-we1',sec('p3l9-we1','27–29 MIN',body,
 'Worked example. Ask first: "Can we take 850 away from 100 g?" (Not without breaking the kilograms.) Click each step. Think-aloud: "I change the bag to grams: 2 kg is 2000 g, plus 100 is 2100 g. Now it is a normal take-away: 2100 − 850 = 1250 g. I change back: 1000 g of it is 1 kg, so 1 kg 250 g. I check by adding back: 1250 + 850 = 2100." '
 'Some children prefer to work in kg and g separately (renaming 1 kg as 1000 g): accept it, but show why one unit is less likely to go wrong.'))
put('p3l9-try1',try_slide('p3l9-try1','29–30 MIN','Your turn: one unit','Whiteboards. Change to the smaller unit first.',[('a','4 m 9 cm = __ cm','409 cm'),('b','2750 ml = __ ℓ __ ml','2 ℓ 750 ml'),('c','Which is longer: 3 m 5 cm or 350 cm?','350 cm')],
 'Whiteboards up together, then click. a) 400 + 9 = 409 (not 49). b) 2000 ml is 2 ℓ, 750 ml left. c) 3 m 5 cm = 305 cm, so 350 cm is longer by 45 cm. Ask a child to explain c: the "5" in 3 m 5 cm is only 5 cm.',38))

# ---------- 9. teach: time line ----------
def tline(ticks,arcs=(),w=1664,h=230,only_arcs=False,aria='Time line'):
    """ticks: list of (x, label); arcs: list of (x1, x2, label)"""
    b=''
    if not only_arcs:
        b+=f'<line x1="20" y1="150" x2="{w-20}" y2="150" stroke="{NAVY}" stroke-width="6" stroke-linecap="round"/>'
        for x,lab in ticks: b+=f'<line x1="{x}" y1="132" x2="{x}" y2="168" stroke="{NAVY}" stroke-width="6"/>'+T(x,208,lab,32)
    for x1,x2,lab in arcs:
        b+=f'<path d="M{x1+6} 138 Q{(x1+x2)/2} 40 {x2-6} 138" fill="none" stroke="{TEAL}" stroke-width="5"/><polygon points="{x2-6},140 {x2-24},126 {x2-6},118" fill="{TEAL}"/>'
        b+=f'<rect x="{(x1+x2)/2-80}" y="44" width="160" height="50" rx="12" fill="{YEL}" stroke="{NAVY}" stroke-width="3"/>'+T((x1+x2)/2,80,lab,30)
    return svg(w,h,b,aria)
X=[110,420,1250,1554]
ticks=list(zip(X,['9:45','10:00','11:00','11:20']))
body=h2('Draw a time line: jump to the next o’clock')+card(p('How long is it from 9:45 a.m. to 11:20 a.m.?',40,700))
body+=pin(128,360,1664,tline(ticks,aria='Time line from 9:45 to 11:20'))
for i,(a,b_,lab) in enumerate([(X[0],X[1],'15 min'),(X[1],X[2],'1 h'),(X[2],X[3],'20 min')]):
    body+=pin(128,360,1664,tline(ticks,[(a,b_,lab)],only_arcs=True,aria=f'Jump of {lab}'),'fade')
body+=answer(128,620,740,'15 min + 1 h + 20 min = 1 h 35 min')
body+=pin(960,620,780,p('Why not 11.20 − 9.45? An hour has 60 minutes, not 100. Time is not like normal numbers.',32,700),'fade',SOFT,20,'18px 26px')
body+=pin(128,790,1664,p('Jump to the next o’clock, then jump whole hours, then the minutes left.',34,700,TEAL),'fade')
put('p3l9-teach2',sec('p3l9-teach2','30–32 MIN',body,
 'Teach heuristic 2: draw a time line. Ask first: "How long is it from 9:45 to 11:20?" Collect guesses (someone may say 1 h 75 min or 2 h 25 min). Click the three jumps one at a time. Think-aloud: "From 9:45 I jump to the next o’clock: 15 minutes to 10:00. Then a whole hour to 11:00. Then 20 minutes to 11:20. Add the jumps: 15 + 20 = 35 minutes, and 1 hour." '
 'Click the "Why not" box: "If we subtract like normal numbers we treat an hour as 100 minutes. That is the trap." Show it on a real clock if you have one.'))

# ---------- 10. worked example: end time ----------
X=[110,560,1100,1554]
ticks=list(zip(X,['2:50','3:00','4:00','4:35']))
body=h2('Worked example: when does it end?')+card(p('A movie starts at 2:50 p.m. and lasts 1 h 45 min. When does it end?',40,700))
body+=step(1,'Split the 45 minutes: 10 minutes takes us to 3:00, and 35 minutes are left.',top=360,size=34)
body+=pin(128,470,1664,tline(ticks[:1]+[(X[1],'3:00')],aria='Time line starting at 2:50'),'fade')
for a,b_,lab in [(X[0],X[1],'10 min'),(X[1],X[2],'1 h'),(X[2],X[3],'35 min')]:
    body+=pin(128,470,1664,tline(ticks,[(a,b_,lab)],aria=f'Jump of {lab}') if lab=='35 min' else tline(ticks,[(a,b_,lab)],only_arcs=True,aria=f'Jump of {lab}'),'fade')
body+=answer(128,730,1664,'2:50 + 10 min = 3:00,  + 1 h = 4:00,  + 35 min = 4:35 p.m.')
put('p3l9-we2',sec('p3l9-we2','32–33 MIN',body,
 'Worked example. Click step 1: "45 minutes is too big a jump from 2:50, it goes past the o’clock. So I split it: 10 minutes to reach 3:00, and 45 − 10 = 35 minutes left." Then click the jumps: 10 min, 1 h, 35 min (the last click also shows all the times). Then the answer. '
 'Check: "From 2:50 to 4:35 is 10 + 60 + 35 = 105 minutes, and 1 h 45 min is 60 + 45 = 105 minutes." In 24-hour time this is 16:35 (we learn that after the break).'))
put('p3l9-try2',try_slide('p3l9-try2','33–34 MIN','Your turn: time lines','Draw a time line. Jump to the o’clock first.',[('a','How long from 10:40 a.m. to 1:15 p.m.?','2 h 35 min'),('b','Start 8:35 a.m. Lasts 1 h 40 min. Ends?','10:15 a.m.'),('c','Ends 6:10 p.m. Lasted 45 min. Started?','5:25 p.m.')],
 'Whiteboards. a) 20 min to 11:00, 2 h to 1:00, 15 min to 1:15: 2 h 35 min. b) 25 min to 9:00, 1 h to 10:00, 15 min left: 10:15 a.m. c) Go backwards: 10 min back to 6:00, 35 min back to 5:25 p.m. Check c forwards: 5:25 + 35 min = 6:00, + 10 min = 6:10.',36))

body=h2('Key idea: one unit, and a time line')+card(p('Change to one unit before you compare, add or take away. For time, draw a time line and jump to the next o’clock.',44,700))+card(p('1 m = 100 cm  •  1 kg = 1000 g  •  1 ℓ = 1000 ml  •  $1 = 100¢  •  1 h = 60 min',36,600,MUTED))
put('p3l9-key',sec('p3l9-key','34–35 MIN',body,'Say the key idea together. Common mistakes to watch for during the worksheet: (1) 2 m 5 cm written as 25 cm, or 3 kg 40 g as 340 g. (2) Subtracting times like normal numbers (11.20 − 9.45), or counting 100 minutes in an hour. (3) 24-hour clock: adding 12 to a.m. times or to 12:30 p.m.; reading 17:00 as 7 p.m. (4) Budgets: adding the dollars and forgetting to carry the cents (85¢ + 90¢ = $1.75).'))
put('p3l9-break',break_slide('p3l9-break','35–40 MIN','Brain break','Human clock! Use your arms as the clock hands. Show 3 o’clock, 6 o’clock, quarter past 9 … and 15:00!','Then: a drink of water and back to our seats.','Five minutes. Call out times; children make the hands with their arms. Mix in 24-hour times: 15:00 (3 o’clock), 18:00 (6 o’clock), 21:15 (quarter past 9). Online: children stay in view of the camera.'))

# ---------- teach before page 1: budgets ----------
body=h2('Budgets: is there enough money?')+card(p('Ben has $15. A kite costs $6.85, a ball $4.50 and a cap $3.95. Can he buy all three?',40,700))
body+=step(1,'Estimate:  about $7 + $4.50 + $4 = $15.50. Very close, so work it out exactly.',top=380,size=34)
body+=step(2,'Change to cents:  685¢ + 450¢ + 395¢ = 1530¢ = $15.30',top=490,size=34)
body+=step(3,'Compare:  $15.30 is more than $15. No: he is 30¢ short.',top=600,size=34)
body+=pin(128,730,1664,p('Spend the most with 2 things? Try the dearest first: kite + ball = $11.35 (change $3.65). Kite + cap = $10.80, ball + cap = $8.45.',32,700),'fade',SOFT,20,'18px 28px')
put('p3l9-teachbudget',sec('p3l9-teachbudget','40–42 MIN',body,
 'Teach before worksheet page 1 (Q3). Click each step. Think-aloud: "An estimate tells me if it is close. $15.50 is too close to be sure, so I work it out exactly in cents: 685 + 450 = 1135, and 395 more is 1530 cents, $15.30. That is more than $15: 30 cents short." '
 'Last click: "To spend as much as I can, I start with the dearest things and check every pair in order." Do not do the worksheet question for them: it uses 3 things from 5.'))
put('p3l9-ws1',ws_preview('p3l9-ws1','42–53 MIN','Worksheet page 1: with your partner',[('Q1','Change the units. Watch out for the zeros. Q1d is the ribbon.'),('Q2','Order four masses, then fix Ben’s mistake.'),('Q3','Siti’s $20 budget. Change to cents. Q3b only if time.')],'Stuck? Change everything to cm, g, ml or ¢.',
 'Minutes 42 to 53. Walk around. Ask "What unit did you change to?" and "How do you know?" before helping. Q3b (if time): check pairs are listing sets in an order, starting with the dearest items, not guessing.'))
put('p3l9-ws1ans',check_slide('p3l9-ws1ans','53–55 MIN','Page 1: check together',[('Q1','a) 306 cm   b) 2450 g   c) 4 ℓ 80 ml   d) 40 cm left'),('Q2','1 kg, 1 kg 3 g, 1030 g, 1 kg 300 g.   1 kg 30 g = 1030 g'),('Q3','a) No: $20.25, 25¢ short   b) Book, pen set, puzzle: $19.35, 65¢ change')],
 'Click each answer after a pair explains. Q1d: 4 × 65 = 260 cm; 300 − 260 = 40 cm. Q2: in grams 1000, 1003, 1030, 1300. Q3a: 785 + 690 + 550 = 2025¢. Q3b: book + puzzle = $14.75 leaves $5.25: the dearest thing that fits is the pen set ($4.60), total $19.35. Without that pair, the best is $17.95, so $19.35 is the most.'))

# ---------- teach before page 2: 24-hour clock ----------
w=1664; sx=lambda h: 40+h*(w-80)/24
g=f'<rect x="{sx(0)}" y="30" width="{sx(12)-sx(0)}" height="70" fill="{SKY}" stroke="{NAVY}" stroke-width="4"/><rect x="{sx(12)}" y="30" width="{sx(24)-sx(12)}" height="70" fill="{SOFT}" stroke="{NAVY}" stroke-width="4"/>'
g+=T(sx(6),76,'a.m. (midnight to noon)',30)+T(sx(18),76,'p.m. (noon to midnight)',30)
for h_ in range(0,25,3):
    g+=f'<line x1="{sx(h_)}" y1="100" x2="{sx(h_)}" y2="120" stroke="{NAVY}" stroke-width="4"/>'+T(sx(h_),152,f'{h_:02d}:00',26)
    lab={0:'12 a.m.',12:'12 noon',24:'12 a.m.'}.get(h_,f'{h_%12} {"a.m." if h_<12 else "p.m."}')
    g+=T(sx(h_),190,lab,26,TEAL,weight=700)
strip=svg(w,200,g,'24-hour strip from 00:00 to 24:00 with the matching 12-hour times')
body=h2('The 24-hour clock')+pin(128,250,1664,strip)
body+=step(1,'a.m.: same numbers, 2 digits for the hour.  6:05 a.m. → 06:05',top=480,size=34)
body+=step(2,'p.m.: add 12 to the hour.  4:20 p.m. → 16:20',top=580,size=34)
body+=step(3,'Back again: take away 12.  19:30 → 7:30 p.m.',top=680,size=34)
body+=pin(128,790,1664,p('Careful: 12:45 p.m. stays 12:45 (it is already after 12 noon). Midnight is 00:00.',32,700),'fade',SOFT,20,'16px 28px')
put('p3l9-teach24',sec('p3l9-teach24','55–57 MIN',body,
 'Teach before worksheet page 2 (Q4). "The 24-hour clock does not start again at 12 noon: it keeps counting, 13, 14, 15 … up to 23, then midnight is 00:00." Point along the strip. Click each step. '
 'Think-aloud: "4:20 p.m. is in the afternoon, so I add 12: 4 + 12 = 16, so 16:20. Going back: 19 − 12 = 7, so 7:30 p.m." Click the careful box: the hour from 12 noon to 1 p.m. is already 12, so we do not add 12. Quick check: "What is 15:00?" (3 p.m.) "What is 9:10 p.m.?" (21:10).'))

# ---------- teach: list the times / go backwards ----------
body=h2('Timetables and going backwards')
body+=pin(128,250,800,p('Trains leave every 15 minutes from 09:50. Mei reaches the platform at 10:27. How long does she wait?',32,700),None,WHITE,20,'20px 26px')
for i,t in enumerate(['09:50','10:05','10:20','10:35']):
    body+=pin(128+i*200,440,180,p(t,36,800),'rise',YEL if i==3 else WHITE,16,'12px 20px','text-align:center')
body+=pin(128,560,800,p('List the times. The first one after 10:27 is 10:35. Wait: 3 min to 10:30 + 5 min = 8 min.',32,700),'fade',SOFT,20,'18px 24px')
body+=pin(992,250,800,p('A film lasts 1 h 25 min and ends at 20:10. When did it start?',32,700),None,WHITE,20,'20px 26px')
for i,t in enumerate(['20:10 back 10 min → 20:00','20:00 back 1 h → 19:00','19:00 back 15 min → 18:45']):
    body+=pin(992,400+i*100,800,p(t,32,700),'rise',WHITE,16,'14px 24px')
body+=pin(992,710,800,p('Go backwards on the time line: back to the o’clock first.',30,700,TEAL),'fade')
put('p3l9-teachlist',sec('p3l9-teachlist','57–58 MIN',body,
 'Teach before worksheet page 2 (Q5c and Q6). Left: "Every 15 minutes means I keep adding 15. I list the times in order until I pass 10:27." Click the times. "The first train after 10:27 is 10:35. From 10:27: 3 minutes to 10:30, 5 more to 10:35: 8 minutes." '
 'Right: "To find a start time I go backwards. 25 minutes back from 20:10 passes the o’clock, so I split 25 into 10 and 15." Check forwards: 18:45 + 15 min = 19:00, + 1 h = 20:00, + 10 min = 20:10.'))
put('p3l9-ws2',ws_preview('p3l9-ws2','58–67 MIN','Worksheet page 2: on your own',[('Q4','The 24-hour clock. After 12 noon, add 12.'),('Q5','Time lines: how long, when it ends, when it started.'),('Q6','If time: the bus timetable. List the times, every 25 minutes.')],'Finished early? Stretch and Challenge come next.','Children work alone. Note who needs a short catch-up. Q6 (if time): check children list ALL the bus times (adding 25 each time across the hour: 07:05 + 25 min = 07:30).'))
put('p3l9-ws2ans',check_slide('p3l9-ws2ans','67–70 MIN','Page 2: check together',[('Q4','07:15,  15:40,  8:05 p.m.,  12:30.   17:00 is 5 p.m., not 7 p.m.'),('Q5','a) 1 h 25 min   b) 17:25   c) 19:25'),('Q6','(if time) a) 08:20, waits 5 min   b) 08:55')],
 'Click after a child explains. Q5a: 15 min to 4:00, 1 h to 5:00, 10 min to 5:10. Q5b: 25 min to 17:00, 25 min more: 17:25. Q5c: back 15 min to 21:00, back 1 h to 20:00, back 35 min to 19:25. Q6 (if time): 06:40, 07:05, 07:30, 07:55, 08:20. b) 08:20 + 35 min = 08:55. The "latest bus to arrive by 08:30" question is a Think Harder item: 07:55 + 35 min = 08:30 exactly; the 08:20 bus is too late.'))

# ---------- stretch, challenge ----------
st=[('1.','A night train leaves at 22:40 and arrives at 01:15 the next morning. How long is the trip?'),('2.','Siti’s home is 1 km 250 m from school. She walks there and back every day. How far does she walk in 2 days?'),('3.','Ali needs 2 ℓ of milk. A 250 ml carton costs $1.10 and a 1 ℓ carton costs $3.60. What is the cheapest way?')]
put('p3l9-stretch',sec('p3l9-stretch','For early finishers',h2('Stretch')+''.join(num_card(a,b) for a,b in st),
 'For children who finish early. Answers: 1) 2 h 35 min: 20 min to 23:00, 1 h to 00:00 (midnight), 1 h to 01:00, 15 min to 01:15. 2) 5 km: one day is 1250 + 1250 = 2500 m; two days 5000 m = 5 km. 3) Two 1 ℓ cartons: $7.20 (one 1 ℓ and four small cartons cost $3.60 + $4.40 = $8.00; eight small cartons cost $8.80).'))
ch=[('1.','A bottle full of water weighs 1 kg 200 g. After half of the water is poured out, it weighs 750 g. How heavy is the empty bottle?'),('2.','Mei buys 3 pens and 2 files for $9.20. Each file costs 60¢ more than each pen. How much does one pen cost?')]
put('p3l9-challenge',sec('p3l9-challenge','Challenge',h2('Challenge')+''.join(num_card(a,b) for a,b in ch),
 'Use as a pair challenge or in talk time. Ask for the reason every time. Answers: 1) 300 g (half the water weighs 1200 − 750 = 450 g, so all the water is 900 g; the bottle is 1200 − 900 = 300 g). 2) $1.60 (take away the extra 60¢ on each file: $9.20 − $1.20 = $8.00 for 5 pens; 800¢ ÷ 5 = 160¢. A file costs $2.20. Check: $4.80 + $4.40 = $9.20).'))
# see it
def bottle(x,level,lab,sub):
    b=f'<rect x="{x+40}" y="40" width="40" height="30" rx="6" fill="{TEAL}" stroke="{NAVY}" stroke-width="4"/><path d="M{x+30} 70 L{x+90} 70 L{x+110} 110 L{x+110} 380 Q{x+110} 400 {x+90} 400 L{x+30} 400 Q{x+10} 400 {x+10} 380 L{x+10} 110 Z" fill="{WHITE}" stroke="{NAVY}" stroke-width="5"/>'
    top=400-level*270
    b+=f'<rect x="{x+14}" y="{top}" width="92" height="{396-top}" fill="{BLUE}" opacity=".8"/>'
    return b+T(x+60,450,lab,32)+T(x+60,490,sub,26,MUTED,weight=700)
g1=bottle(60,1,'1 kg 200 g','full')+bottle(330,0.5,'750 g','half the water poured out')
g1+=f'<rect x="560" y="170" width="200" height="120" rx="14" fill="{SOFT}" stroke="{NAVY}" stroke-width="3"/>'+T(660,222,'What does',28)+T(660,262,'half weigh?',28)
d1=svg(800,510,g1,'Two bottles: full weighs 1 kg 200 g; with half the water poured out it weighs 750 g')
u=95
g2=T(10,70,'pens',30,anchor='start')+''.join(f'<rect x="{120+i*u}" y="30" width="{u}" height="64" fill="{SKY}" stroke="{NAVY}" stroke-width="4"/>' for i in range(3))
g2+=T(10,190,'files',30,anchor='start')
for i in range(2):
    x=120+i*(u+60)
    g2+=f'<rect x="{x}" y="150" width="{u}" height="64" fill="{SKY}" stroke="{NAVY}" stroke-width="4"/><rect x="{x+u}" y="150" width="60" height="64" fill="{YEL}" stroke="{NAVY}" stroke-width="4"/>'+T(x+u+30,192,'60¢',28)
g2+=f'<path d="M620 30 Q660 30 660 122 Q660 214 620 214" fill="none" stroke="{TEAL}" stroke-width="5"/>'+T(730,132,'$9.20',36,TEAL)
g2+=f'<rect x="60" y="300" width="680" height="120" rx="14" fill="{SOFT}" stroke="{NAVY}" stroke-width="3"/>'+T(400,350,'Each file is a pen and 60¢ more.',30)+T(400,395,'What if we took the yellow parts away?',28,MUTED,weight=700)
d2=svg(800,510,g2,'Bar model: 3 pen bars and 2 file bars, each file a pen bar plus 60 cents, all together $9.20')
cardsvg=lambda t,s: f'<div style="background:{WHITE};border-radius:24px;padding:20px 24px;display:flex;flex-direction:column;gap:10px;flex:1;min-width:0"><p style="font-size:30px;font-weight:700;color:{TEAL}">{E(t)}</p>{s.replace("style=\"width:800px;height:510px;","style=\"width:100%;height:auto;")}</div>'
body=h2('Challenge: see it')+f'<div style="display:flex;gap:32px;align-items:flex-start">{cardsvg("Q1: the bottle and the water",d1)}{cardsvg("Q2: pens and files as bars",d2)}</div>'
put('p3l9-chdiag',sec('p3l9-chdiag','Challenge',body,'Show after pairs have tried the Challenge, or if they are stuck. The diagrams show the problem, not the answer. Ask: What do you notice? What changed between the two bottles? (Only the water.) For Q2: what would the bars show without the yellow parts? Answers are in the Challenge slide notes.'))
body=h2('Challenge: walk-through')+pin(128,250,800,p('Q1: what changed?',38,800,TEAL))
for i,t in enumerate(['Only water was poured out: 1200 g − 750 g = 450 g.','That was half the water, so all the water is 450 + 450 = 900 g.','Bottle = 1200 g − 900 g = 300 g.','Check: 300 + 450 = 750 g ✓']): body+=pin(128,330+i*125,800,p(t,32),'rise',WHITE)
body+=pin(992,250,800,p('Q2: take away the extras',38,800,TEAL))
for i,t in enumerate(['Each file = a pen + 60¢. Two files have 2 × 60¢ = $1.20 extra.','$9.20 − $1.20 = $8.00 is 5 equal pen bars.','800¢ ÷ 5 = 160¢. One pen costs $1.60.','A file: $2.20. Check: $4.80 + $4.40 = $9.20 ✓']): body+=pin(992,330+i*125,800,p(t,32),'rise',WHITE)
put('p3l9-chwalk',sec('p3l9-chwalk','Challenge',body,'Use after pairs have tried, with the "see it" slide. Q1: compare the two bottles: the bottle is the same, only the water changed, so the difference is half the water. Q2: the same idea as Lesson 4 (Model Makers): remove the extra parts so all the bars are equal. Change $8.00 to 800¢ before dividing.'))
put('p3l9-talk',talk_slide('p3l9-talk','70–80 MIN','Which is longer: 3 m 5 cm or 350 cm? Why can we not just do 11.20 − 9.45 to find a time?',
 'Minutes 70 to 80. Pairs talk for 2 minutes, then share. Answers: 350 cm is longer, because 3 m 5 cm = 305 cm. An hour has 60 minutes, not 100, so we count on with a time line: 9:45 to 11:20 is 15 min + 1 h + 20 min = 1 h 35 min. Praise the reasons, not only the answers.'))
put('p3l9-exit',exit_slide('p3l9-exit','80–90 MIN','A swimming lesson starts at 16:50 and lasts 1 h 25 min. When does it end? Give the 24-hour time.',
 'Minutes 80 to 90. Answer: 18:15 (16:50 + 10 min = 17:00, + 1 h = 18:00, + 15 min = 18:15), which is 6:15 p.m. A child who writes 17:75 or 18:75 is adding like normal numbers: revisit the time line next lesson. Extension: plan a real outing with a timetable and a $50 budget.'))

# ---------- write ----------
order=['p3l9-title','p3l9-warm1','p3l9-warm2','p3l9-explore1','p3l9-explore2','p3l9-teach1','p3l9-we1','p3l9-try1','p3l9-teach2','p3l9-we2','p3l9-try2','p3l9-key','p3l9-break','p3l9-teachbudget','p3l9-ws1','p3l9-ws1ans','p3l9-teach24','p3l9-teachlist','p3l9-ws2','p3l9-ws2ans','p3l9-stretch','p3l9-challenge','p3l9-chdiag','p3l9-chwalk','p3l9-talk','p3l9-exit']
import p3_gifted; order[:]=p3_gifted.add(S,order,9)  # close-the-gaps: warm-up check + look-back slides
assert set(order)==set(S), set(order)^set(S)
for i,h in S.items(): open(os.path.join(D,'slides',i+'.html'),'w').write(h)
deck={'v':4,'createdOnFiles':{'v':1,'at':datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')},'lists':'css',
      'title':'Math Inquirers P3: Lesson 9 – Measure and Money Masters','order':order,'cover':'p3l9-title',
      'sections':{'s1':{'description':'Warm-up and explore','start':'p3l9-title'},'s2':{'description':'Teach: change to one unit, and draw a time line','start':'p3l9-teach1'},'s3':{'description':'Worksheet with teaching before each page','start':'p3l9-break'},'s4':{'description':'Think harder, go further, talk and exit','start':'p3l9-stretch'}},
      'faces':{'fredoka':{'family':'Fredoka','href':'https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&display=swap'},'nunito-sans':{'family':'Nunito Sans','href':'https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@400;600;700&display=swap'}},
      'designSystems':[]}
json.dump(deck,open(os.path.join(D,'deck.json'),'w'),indent=1,ensure_ascii=False)
print(len(order),'slides')
