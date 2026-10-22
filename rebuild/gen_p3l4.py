"""Math Inquirers P3, Lesson 4: Model Makers. Writes split/p3l4/project (deck.json + slides/*.html)."""
import json,os,sys,math
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,H)
from slidekit import *
D=os.path.join(H,'..','split','p3l4','project'); os.makedirs(os.path.join(D,'slides'),exist_ok=True)
S={}
def put(i,h): S[i]=h
RED='#D64545'

# ---------- common slide shapes ----------
def title_slide(sid,n,week,title,topic,today,notes):
    return (f'<section id="{sid}" data-transition="fade" style="background:{NAVY};color:{CREAM};font-family:{BF};padding:128px 128px 160px;display:flex;flex-direction:column;justify-content:center;gap:36px">\n'
            f'<p style="font-size:32px;font-weight:700;letter-spacing:4px;color:{YEL}">PRIMARY 3  •  LESSON {n}  •  WEEK {week}</p>\n'
            f'<h1 style="font-family:{HF};font-size:128px;font-weight:600;line-height:1.05">{E(title)}</h1>\n'
            f'<p style="font-size:44px;color:#C9D4EC">{E(topic)}</p>\n'
            f'<div style="background:#26385F;border-radius:24px;padding:40px;display:flex;flex-direction:column;gap:12px"><p style="font-size:28px;font-weight:700;letter-spacing:3px;color:{YEL}">TODAY WE WILL</p><p style="font-size:44px;font-weight:600">{E(today)}</p></div>\n'
            f'<p style="position:absolute;left:128px;bottom:64px;width:1400px;font-size:24px;color:#B7C3DD">{E(FOOT)}</p>\n<aside>{E(notes)}</aside>\n</section>\n')
def break_slide(sid,text,sub,notes):
    return (f'<section id="{sid}" data-transition="fade" style="background:{TEAL};color:{CREAM};font-family:{BF};padding:128px 128px 160px;display:flex;flex-direction:column;justify-content:center;gap:36px">\n'
            f'<p style="font-size:32px;font-weight:700;letter-spacing:4px;color:{YEL}">35–40 MIN</p>\n'
            f'<h2 style="font-family:{HF};font-size:110px;font-weight:600;line-height:1.05">Brain break</h2>\n'
            f'<p style="font-size:48px;font-weight:600">{E(text)}</p>\n<p style="font-size:36px;color:#D7EFEA">{E(sub)}</p>\n'
            f'<p style="position:absolute;left:128px;bottom:64px;width:1400px;font-size:24px;color:#D7EFEA">{E(FOOT)}</p>\n<aside>{E(notes)}</aside>\n</section>\n')
def numbered(items,size=36):
    return ''.join(card(p(f'<span style="color:{TEAL}">{a}</span>  {E(b)}',size,600,raw=True)) for a,b in items)
def explore1(sid,steps,pic,notes):
    lis=''.join(f'<li>{E(s)}</li>' for s in steps)
    inner=chip('EXPLORE')+f'<ol style="font-size:34px;font-weight:600;padding-left:48px;margin:0;display:flex;flex-direction:column;gap:6px">{lis}</ol>'
    return sec(sid,'10–15 MIN',h2('Explore: what to do')+card(inner,extra='padding:24px 40px')+card(pic,extra='padding:12px 24px;align-items:center'),notes)
def talk_slide(sid,q,notes):
    body=h2('Talk time')+card(chip('TALK TIME',YEL,NAVY)+p(q,42,600))+card(p('Sentence starters:',34,400,MUTED)+p('“I noticed that …”   “I tested it by …”   “I know because …”',38,600))
    return sec(sid,'70–80 MIN',body,notes)
def exit_slide(sid,q,notes):
    body=h2('Exit ticket')+card(chip('EXIT TICKET')+p(q,46,600))+card(p('Write your answer on a slip of paper. Show it to your tutor. Then collect your stamp in your inquiry journal.',34,400))
    return sec(sid,'80–90 MIN',body,notes)
def check_rows(sid,time,title,rows,notes,lw=210,gap=128,size=38):
    body=h2(title)
    for i,(a,b) in enumerate(rows):
        top=250+i*gap
        body+=pin(128,top,lw-20,f'<p style="font-size:36px;font-weight:800;color:{TEAL}">{E(a)}</p>',None,WHITE,20,'18px 24px')
        body+=pin(128+lw,top,1664-lw,f'<p style="font-size:{size}px;font-weight:800;line-height:1.2">{E(b)}</p>','pop',YEL,20,'18px 26px')
    return sec(sid,time,body,notes)
def svgwrap(label,w,h,inner,style=''):
    return f'<svg aria-label="{E(label)}" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="width:{w}px;height:{h}px;{style}">{inner}</svg>'
def T(x,y,s,size=34,fill=NAVY,anchor='middle',w=700,font='Nunito Sans, Arial'):
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{w}" text-anchor="{anchor}" fill="{fill}" font-family="{font}">{E(str(s))}</text>'

# ---------- bar-model pictures ----------
GREEN='#D3F1E4'
def R(x,y,w,h,fill,label='',dash=False,size=36):
    d=' stroke-dasharray="12 8"' if dash else ''
    return f'<rect x="{x:.0f}" y="{y}" width="{w:.0f}" height="{h}" fill="{fill}" stroke="{NAVY}" stroke-width="4"{d}/>'+(T(f'{x+w/2:.0f}',y+h/2+size*0.36,label,size,NAVY,w=800) if label else '')
def BH(x0,x1,y,up,label,size=32,hh=22):
    q=min(14,(x1-x0)/4); m=(x0+x1)/2; s=-1 if up else 1; ym=y+s*hh/2; yt=y+s*hh
    path=f'<path d="M{x0:.0f} {y} Q{x0:.0f} {ym} {x0+q:.0f} {ym} L{m-q:.0f} {ym} Q{m:.0f} {ym} {m:.0f} {yt} Q{m:.0f} {ym} {m+q:.0f} {ym} L{x1-q:.0f} {ym} Q{x1:.0f} {ym} {x1:.0f} {y}" fill="none" stroke="{NAVY}" stroke-width="4"/>'
    return path+(T(f'{m:.0f}',yt-10 if up else yt+size+2,label,size,TEAL,w=800) if label else '')
def BV(y0,y1,x,label,size=32,hh=22):
    q=min(14,(y1-y0)/4); m=(y0+y1)/2; xm=x+hh/2; xt=x+hh
    return (f'<path d="M{x} {y0} Q{xm} {y0} {xm} {y0+q} L{xm} {m-q} Q{xm} {m} {xt} {m} Q{xm} {m} {xm} {m+q} L{xm} {y1-q} Q{xm} {y1} {x} {y1}" fill="none" stroke="{NAVY}" stroke-width="4"/>'
            +(T(xt+14,m+size*0.36,label,size,TEAL,'start',800) if label else ''))
def NM(y,s,size=36): return T(0,y,s,size,NAVY,'start',800)
def VL(x,y0,y1): return f'<line x1="{x:.0f}" y1="{y0}" x2="{x:.0f}" y2="{y1}" stroke="{NAVY}" stroke-width="2" stroke-dasharray="6 6"/>'

# ---------- 1 title ----------
put('p3l4-title',title_slide('p3l4-title',4,2,'Model Makers','Word Problems: Bar Models',
 'Draw bar models for word problems: parts of a whole, comparing, times as many, and before and after.',
 'Objective: Draw bar models for part-whole, comparison, times-as-many and before-and-after word problems, and use them to solve two-step problems and check the answers. Heuristics taught: draw a model; before and after (look for what stays the same). '
 'Materials: Multilink cubes (about 30 per pair), strips of squared paper, scissors, mini whiteboards and markers. '
 'Online: Tutor builds the bars on the slides. Each child uses Lego bricks, coins or paper strips at home, and a whiteboard or paper to draw bars. Print the workbook before the lesson. Pairs work in one breakout room for 10 minutes, then return for the check slide. '
 'Time plan: warm-up 0 to 10, explore 10 to 25, teaching 25 to 35 (click to reveal each step and answer), brain break 35 to 40, worksheet 40 to 70 with short teaching before each page and a check-together slide after it, talk time 70 to 80, exit ticket 80 to 90. If the class is behind, children finish the last question of each page at home; the check slides cover it.'))

# ---------- 2 warm1: arm bars ----------
def mini(kind):
    if kind==1: g=NM(52,'Ben',30)+R(110,15,300,55,SKY)+NM(132,'Ali',30)+R(110,95,300,55,SKY)+R(410,95,120,55,YEL,'5',size=32)
    elif kind==2: g=NM(52,'Siti',30)+R(110,15,140,55,YEL)+NM(132,'Mei',30)+''.join(R(110+140*i,95,140,55,YEL) for i in range(3))
    elif kind==3: g=NM(52,'Ravi',30)+R(110,15,260,55,SKY)+NM(132,'Ben',30)+R(110,95,190,55,GREEN)+BV(15,150,390,'20',32)
    else: g=NM(52,'Mei',30)+R(110,15,420,55,SKY)+NM(132,'Siti',30)+R(110,95,300,55,GREEN)+R(410,95,120,55,WHITE,'4',True,32)
    return svgwrap('bar picture',744,160,g)
sent=['Ali has 5 more than Ben.','Mei has 3 times as many as Siti.','Ravi and Ben have 20 altogether.','Siti has 4 fewer than Mei.']
body=h2('Warm-up: arm bars')+p('Show the two bars with your hands. Then draw them in 10 seconds.',36,600,MUTED)
for i,s_ in enumerate(sent):
    L=128+(i%2)*864; T_=330+(i//2)*300
    body+=pin(L,T_,800,p(f'<span style="color:{TEAL};font-weight:800">{i+1}.</span>  {E(s_)}',36,700,raw=True),None,WHITE,24,'18px 28px',f'box-sizing:border-box;height:280px;border:4px solid {NAVY}')
    body+=pin(L+28,T_+96,744,mini(i+1),'pop')
put('p3l4-warm1',sec('p3l4-warm1','0–5 MIN',body,
 'Minutes 0 to 5. Arm bars. Read each sentence aloud. Children hold their two hands apart, one above the other, to show the two bars (online: in front of the camera), then draw the bars on whiteboards in 10 seconds. Click to show a model after each one (clicks reveal 1, 2, 3, 4 in order). '
 'Ask: "Whose bar is longer? How do you show the 5?" For 2: "How many equal parts does Mei have?" (3). For 3: "Altogether means we show the total with a bracket." For 4: "Fewer: Siti\'s bar is shorter. The dashed piece shows what she does not have." '
 'Watch for: children who draw "4 fewer" as a longer bar, and children who draw 3 times as many with 4 parts.'))

# ---------- 3 warm2 ----------
qs=[('1.','348 + 52','400'),('2.','1000 − 365','635'),('3.','3 units = 27. 1 unit = ?','9'),('4.','Ben has 40. Ali has 15 more. Ali?','55'),('5.','Mei has 60. Siti has 12 fewer. Siti?','48')]
body=h2('Quick questions')+''.join(qrow(128,250+i*125,1250,a,b,38) for i,(a,b,c) in enumerate(qs))+''.join(answer(1420,250+i*125,372,c) for i,(a,b,c) in enumerate(qs))
put('p3l4-warm2',sec('p3l4-warm2','5–10 MIN',body,'Minutes 5 to 10. Whiteboards, show together, click to reveal. Ask "How did you do it in your head?" For 2, praise counting on (365 → 400 → 1000 is 35 + 600). For 3: "If 3 equal units make 27, one unit is 27 ÷ 3." Answers: 400, 635, 9, 55, 48.'))

# ---------- 4 explore1 ----------
g=(R(200,130,100,150,SKY,'?')+''.join(R(340,30+25*k,100,25,YEL) for k in range(4))+R(340,130,100,150,SKY,'?')+T(470,90,'4 more',30,TEAL,'start',800)
   +T(320,325,'20 cubes altogether',30,NAVY,w=800)
   +R(900,220,100,60,SKY,'?')+''.join(R(1040,100+60*k,100,60,SKY) for k in range(3))+T(1170,200,'3 times as tall',30,TEAL,'start',800)+T(1020,325,'20 cubes altogether',30,NAVY,w=800)
   +f'<line x1="150" y1="282" x2="1450" y2="282" stroke="{NAVY}" stroke-width="5"/>')
pic=svgwrap('Two pairs of cube towers: one tower 4 cubes taller, and one tower 3 times as tall',1500,340,g,'height:300px;width:auto')
put('p3l4-explore1',explore1('p3l4-explore1',['Take 20 cubes. Build two towers. One tower must have 4 more cubes than the other.','Stand the towers side by side. How many cubes are in each?','Use 20 cubes again: now one tower must be 3 times as tall as the other.','Draw each pair of towers as two bars on your whiteboard.'],pic,
 'Minutes 10 to 15. Pairs work with Multilink cubes (about 30 per pair). Online: Lego bricks, coins in two piles, or paper strips. Let them try and adjust (move a cube from one tower to the other). Do not show the take-away-the-extra method yet: listen for pairs who find it. Early finishers: 30 cubes where one tower is 4 times as tall (6 and 24).'))

# ---------- 5 explore2 ----------
eq=[('1.','How did you find the two towers for "4 more"?'),('2.','How many cubes were in each tower for "3 times as tall"?'),('3.','Could you make "3 times as tall" with 22 cubes? Why or why not?')]
put('p3l4-explore2',sec('p3l4-explore2','15–25 MIN',h2('Explore: talk about it')+numbered(eq,40),
 'Minutes 15 to 25. Gather the pairs. Take ideas, then show with cubes. Answers: 1) Take away the extra 4 (16 left), share 16 into two equal towers of 8, then put the 4 back: 8 and 12. Check 8 + 12 = 20 and 12 − 8 = 4. '
 '2) 5 and 15: together the towers make 4 equal parts of 5 (1 part and 3 parts). 3) No: we need 4 equal parts, and 22 cannot be shared into 4 equal parts (5 each leaves 2 over). Then say: "Cubes are great, but big numbers need too many cubes. Today we draw the towers as bars: bar models."'))

# ---------- 6 we1 part-whole ----------
k=1300/1500; a_=645*k; b_=480*k
bar=NM(108,'Seats')+R(180,66,a_,70,SKY,'645')+R(180+a_,66,b_,70,YEL,'480')+R(180+a_+b_,66,1300-a_-b_,70,WHITE,'?')+BH(180,1480,60,True,'1500 seats',34)
body=h2('Part-whole model')+card(p('A hall has 1500 seats. 645 are red, 480 are blue and the rest are green. How many seats are green?',40,700))
body+=pin(128,430,1664,svgwrap('Part-whole bar: 1500 seats cut into 645, 480 and a missing part',1664,150,bar),'rise')
body+=step(1,'One whole cut into parts: draw ONE bar for 1500. Label the parts.',top=600,size=36)
body+=step(2,'Whole take away the parts:  1500 − 645 = 855,  855 − 480 = 375',top=705,size=36)
body+=step(3,'375 seats are green. Check: 645 + 480 + 375 = 1500 ✓',top=810,size=36)
put('p3l4-we1',sec('p3l4-we1','25–28 MIN',body,'Teach the first heuristic: DRAW A MODEL. Click 1 builds the bar, then the steps. Ask before the bar appears: "Is this one thing cut into parts, or two things being compared?" (one whole: the hall). Think-aloud: "It is one whole cut into parts, so I draw ONE bar for 1500 and cut it into 645, 480 and a question mark. Whole take away the parts: 1500 − 645 = 855, 855 − 480 = 375. Check: 645 + 480 + 375 = 1500." Point out that the ? part looks a bit smaller than 480 on the model: a quick sense check.'))

# ---------- 7 try1 ----------
put('p3l4-try1',try_slide('p3l4-try1','28–29 MIN','Your turn: part-whole','Draw one bar for the whole first.',
 [('a','A rope is 900 cm long. 275 cm is cut off. How long is the rest?','625 cm'),('b','Ali has 1200 stamps: 450 from Singapore, 380 from Malaysia, the rest from Japan. How many from Japan?','370'),('c','A shop sold 368 cups on Saturday and 245 cups on Sunday. How many cups in all?','613')],
 'Whiteboards: draw the bar, then the answer. a) 900 − 275 = 625 cm. b) 1200 − 450 − 380 = 370. c) Here the parts are known and the whole is the ?: 368 + 245 = 613. Ask: "Where does the ? go this time?"',size=34))

# ---------- 8 we2 comparison ----------
k=900/403; rv=236*k; sv=403*k; bv=308*k
def rowsvg(label,inner,lab): return svgwrap(label,1664,90,inner)
r1=NM(56,'Ravi',40)+R(200,10,rv,70,SKY,'236')
r2=NM(56,'Siti',40)+R(200,10,rv,70,SKY)+R(200+rv,10,sv-rv,70,YEL,'167')+T(1130,58,'236 + 167 = 403',40,TEAL,'start',800)
r3=NM(56,'Ben',40)+R(200,10,bv,70,GREEN,'?')+R(200+bv,10,sv-bv,70,WHITE,'95',True)+T(1130,58,'403 − 95 = 308',40,TEAL,'start',800)
body=h2('Comparison model')+card(p('Ravi has 236 cards. Siti has 167 more cards than Ravi. Ben has 95 fewer cards than Siti. How many cards does Ben have?',40,700))
body+=pin(128,420,1664,rowsvg('Ravi bar 236',r1,''),'rise')+pin(128,520,1664,rowsvg('Siti bar: Ravi and 167 more',r2,''),'rise')+pin(128,620,1664,rowsvg('Ben bar: 95 fewer than Siti',r3,''),'rise')
body+=answer(128,740,1664,'Ben has 308 cards. Check: 403 − 308 = 95 ✓')
put('p3l4-we2',sec('p3l4-we2','28–31 MIN',body,'Click to build each bar. Before each click ask: "Is this bar longer or shorter? Than whose bar? By how much?" Think-aloud: "Siti has 167 MORE than Ravi, so her bar is Ravi\'s bar and an extra piece of 167: 236 + 167 = 403. Ben has 95 FEWER than Siti, so I compare Ben with Siti, not with Ravi. His bar is Siti\'s bar with 95 missing: 403 − 95 = 308." Common mistake: 236 − 95 (comparing with the wrong person). Point at the words "than Siti".'))

# ---------- 9 try2 ----------
put('p3l4-try2',try_slide('p3l4-try2','31–33 MIN','Your turn: compare','A bar for each. Who has more? By how much?',
 [('a','Mei has 125 beads. Ali has 60 more. How many beads does Ali have?','185'),('b','Ben has 342 marbles. Ravi has 87 fewer. How many do they have altogether?','597'),('c','Box A has 500 g of rice. Box B has 135 g less. How much more rice is in Box A?','135 g')],
 'Whiteboards. a) 125 + 60 = 185. b) Ravi 342 − 87 = 255, altogether 342 + 255 = 597 (two steps). c) A trick question: the model shows the difference is already given, 135 g. Nobody needs to work out Box B. Praise children who spotted it from their model.',size=34))

# ---------- 10 key ----------
body=h2('Key idea: draw a model')+card(p('Draw a bar for each amount. Label what you know and put ? on what you want to find.',46,700))+card(p('Then ask: what stays the same? The total, or the difference?',38,600,MUTED))
put('p3l4-key',sec('p3l4-key','33–35 MIN',body,'Say the key idea together. Common mistakes to watch for during the worksheet: (1) Comparing with the wrong person (Ben has 79 fewer than ALI, not Mei), or drawing "more than" as a shorter bar. (2) Times as many: dividing the total by 3 instead of by 3 + 1 = 4 units. (3) Make them equal: giving the whole difference instead of half of it.'))

# ---------- 11 break ----------
put('p3l4-break',break_slide('p3l4-break','Stretch and shrink. "Longer bar": stretch your arms wide. "Shorter bar": bring them close. "3 times as long": take three big steps.','Then: a drink of water and back to our seats.','Five minutes. Mix the calls quickly. Online: children stay in view of the camera and move in place.'))

# ---------- 12 teach units ----------
u=200
g=NM(58,'Ali')+R(200,20,u,64,YEL)+NM(152,'Ben')+''.join(R(200+u*i,114,u,64,YEL) for i in range(4))+BV(20,178,1030,'175 altogether',34)
body=h2('Times as many: equal units')+card(p('Ben has 4 times as many stamps as Ali. They have 175 stamps altogether. How many stamps does Ben have?',40,700))
body+=pin(128,420,1664,svgwrap('Units model: Ali 1 unit, Ben 4 units, 175 altogether',1664,190,g),'rise')
body+=step(1,'Ali 1 unit, Ben 4 units: 1 + 4 = 5 units = 175',top=630,size=36)
body+=step(2,'1 unit = 175 ÷ 5 = 35',top=730,size=36)
body+=step(3,'Ben = 4 units = 4 × 35 = 140. Check: 35 + 140 = 175 ✓',top=830,size=34)
put('p3l4-teachunits',sec('p3l4-teachunits','40–42 MIN',body,'Teach before worksheet page 1 (Q3 is times as many). "4 times as many" means Ben\'s bar is 4 of Ali\'s bars. Ask before step 1: "How many units altogether?" Many children say 4. Point to the model and count: Ali\'s 1 and Ben\'s 4 make 5. Then share 175 into 5 equal units (175 ÷ 5 = 35).'))

# ---------- 13 try units ----------
put('p3l4-tryunits',try_slide('p3l4-tryunits','42–43 MIN','Your turn: units','Draw the units. Count ALL the units.',
 [('a','Mei has twice as many pens as Siti. They have 36 altogether. How many pens does Siti have?','12'),('b','A cake costs 3 times as much as a drink. Together they cost $20. How much is the cake?','$15'),('c','Ali has 5 times as many cards as Ben. Ali has 48 MORE than Ben. How many does Ben have?','12')],
 'Whiteboards. a) 3 units = 36, 1 unit = 12. b) 4 units = $20, 1 unit = $5, cake 3 units = $15. c) Different! The difference is 5 − 1 = 4 units = 48, so 1 unit = 12. Ask: "Why did we use 4 units in c, not 6?"',size=34))

# ---------- 14-15 worksheet page 1 ----------
put('p3l4-ws1',ws_preview('p3l4-ws1','43–53 MIN','Worksheet page 1: with your partner',[('Q1','Part-whole: the bakery. Use the bar.'),('Q2','Compare three children. Who do you compare Ben with?'),('Q3','Times as many: count all the units.')],'Label the bars. Put ? on what you want to find.','Minutes 43 to 53. Pairs work together. Walk around and ask "Is it a whole cut into parts, or a comparison?" For Q2, check pairs subtract 79 from ALI\'s number. For Q3, check they use 4 units.'))
put('p3l4-ws1ans',check_rows('p3l4-ws1ans','53–55 MIN','Page 1: check together',[
 ('Q1','a) 386 buns      b) 108 more'),
 ('Q2','a) Ali 473, Ben 394      b) 1212 stickers'),
 ('Q3','a) 4 units, 1 unit = 62      b) Siti 186, 124 more')],
 'Click each answer after a pair explains theirs. Q1: 1250 − 486 − 378 = 386; 486 − 378 = 108. Q2: Ali 345 + 128 = 473; Ben 473 − 79 = 394; total 345 + 473 + 394 = 1212. Q3: 248 ÷ 4 = 62; Siti 3 × 62 = 186; the difference is 2 units = 124.',lw=210,gap=150))

# ---------- 16 teach total and difference ----------
k=520/37
g=NM(58,'Siti')+R(200,20,520,64,SKY,'?')+NM(152,'Mei')+R(200,114,520,64,SKY)+R(720,114,16*k,64,YEL,'16')+BV(20,178,980,'90 altogether',34)
body=h2('Total and difference')+card(p('Mei and Siti have 90 beads altogether. Mei has 16 more beads than Siti. How many beads does each girl have?',40,700))
body+=pin(128,420,1664,svgwrap('Siti bar and a longer Mei bar with 16 extra; 90 altogether',1664,190,g),'rise')
body+=step(1,'Take away the extra 16:  90 − 16 = 74.  Now the two bars are equal.',top=630,size=36)
body+=step(2,'Share:  74 ÷ 2 = 37.  Siti has 37.',top=730,size=36)
body+=step(3,'Mei:  37 + 16 = 53.  Check: 37 + 53 = 90 ✓',top=830,size=36)
put('p3l4-teachtd',sec('p3l4-teachtd','55–57 MIN',body,'Teach before worksheet page 2 (Q4). This is the explore idea with bigger numbers: take away the extra, share equally, give the extra back. Cover Mei\'s yellow piece with your hand: "Now the bars are the same. What do they add up to?" (74). Ask: "Why not 90 ÷ 2 = 45 each?" (Then Mei would not have 16 more.)'))

# ---------- 17 teach give to make equal ----------
k=14
g=(NM(98,'Ali')+R(200,60,30*k,64,SKY)+R(200+30*k,60,17*k,64,WHITE,'17',True)+R(200+47*k,60,17*k,64,WHITE,'17',True)+BH(200+30*k,200+64*k,54,True,'difference 34',32)
   +NM(190,'Ben')+R(200,152,30*k,64,SKY,'30')+R(200+30*k,152,17*k,64,YEL,'+ 17'))
body=h2('Before and after: give to make equal')+card(p('Ali has 64 cards. Ben has 30 cards. How many cards must Ali give Ben so that they have the same number?',40,700))
body+=pin(128,420,1664,svgwrap('Ali bar 64 with the difference 34 cut into two halves of 17; Ben bar 30 plus 17',1664,225,g),'rise')
body+=step(1,'Difference: 64 − 30 = 34. Ali gives HALF of it:  34 ÷ 2 = 17',top=665,size=36)
body+=step(2,'Check: Ali 64 − 17 = 47,  Ben 30 + 17 = 47 ✓  The total, 94, stays the same.',top=775,size=34)
put('p3l4-teachgive',sec('p3l4-teachgive','57–58 MIN',body,'Teach before worksheet Q5. Act it out first with cubes: 6 and 2. "How many must I move to make them equal?" Many say 4 (the difference). Try it: 6 − 4 = 2 and 2 + 4 = 6, they just swapped! Move 2 instead: 4 and 4. So give HALF the difference. Then click to build the model. What stays the same: the total.'))

# ---------- 18 teach same amount given ----------
k=20
g=(NM(108,'Siti')+R(200,70,12*k,64,SKY,'$12')+R(200+12*k,70,5*k,64,YEL,'$5')+BH(200,200+17*k,64,True,'$17 after',30)
   +NM(202,'Mei')+R(200,164,30*k,64,SKY,'$30')+R(200+30*k,164,5*k,64,YEL,'$5')+VL(200+12*k,156,236)+VL(200+17*k,156,236)
   +BH(200+17*k,200+35*k,234,False,'difference $18 (same as before)',30))
body=h2('Before and after: what stays the same?')+card(p('Mei has $30 and Siti has $12. Their aunt gives each girl $5. How much more does Mei have than Siti before? How much more after?',36,700))
body+=pin(128,400,1664,svgwrap('Siti 12 plus 5 and Mei 30 plus 5: the gap between them is 18 both before and after',1664,296,g),'rise')
body+=step(1,'Before: $30 − $12 = $18.   After: Mei $35, Siti $17, and $35 − $17 = $18.',top=705,size=34)
body+=step(2,'Both get the same, so the difference stays the same: $18.',top=805,size=34)
put('p3l4-teachsame',sec('p3l4-teachsame','58–60 MIN',body,'Teach the second heuristic: BEFORE AND AFTER, look for what stays the same. Before worksheet Q6. Ask: "When both girls get $5, what happens to the gap between them?" Show with two cube towers, add 2 cubes to each: the gap does not change. Then click the model. Check aloud: Siti $12 + $5 = $17, Mei $30 + $5 = $35, and $35 − $17 = $18, the same gap as before. Compare with Q5: when one gives to the other, the TOTAL stays the same; when both get the same, the DIFFERENCE stays the same.'))

# ---------- 19-20 worksheet page 2 ----------
put('p3l4-ws2',ws_preview('p3l4-ws2','60–67 MIN','Worksheet page 2: on your own',[('Q4','Total and difference. Take away the extra first.'),('Q5','Give to make equal. Is Ravi right?'),('Q6','Grandma gives both boys $10. What stays the same?')],'Ready for more? Stretch and Challenge come next.','Children work alone and draw their own models in the dashed boxes. Note who needs a short catch-up next lesson.'))
put('p3l4-ws2ans',check_rows('p3l4-ws2ans','67–69 MIN','Page 2: check together',[
 ('Q4','Ben 63, Ali 87   (150 − 24 = 126, 126 ÷ 2 = 63)'),
 ('Q5a','19 stickers: both then have 66'),
 ('Q5b','38 is the whole difference: they would just swap'),
 ('Q6','a) $27      b) $27      c) the difference stays the same')],
 'Click after a child explains with their model. Q4 check: 63 + 87 = 150 and 87 − 63 = 24. Q5: difference 85 − 47 = 38, give half: 19. Ravi\'s 38 leaves Mei with 47 and Siti with 85. Q6: after Grandma, Ali has $55 and Ben $28, so $55 − $28 = $27; before, $45 − $18 = $27. Both boys got the same amount, so the difference stays the same.',lw=210,gap=150))

# ---------- 21 stretch ----------
st=[('1.','A bag of rice and a bag of flour weigh 9 kg altogether. The rice is 3 kg heavier. How heavy is each bag?'),('2.','Ben had 3 times as many marbles as Ravi. Ben gave Ravi 20 marbles, and then they had the same. How many did Ben have at first?'),('3.','A bag of sugar and 2 bags of flour weigh 1700 g. Each bag of flour is 400 g heavier than the sugar. How heavy is the sugar?')]
put('p3l4-stretch',sec('p3l4-stretch','For early finishers',h2('Stretch')+numbered(st,36),'For children who finish early. Answers: 1) Flour 3 kg, rice 6 kg (9 − 3 = 6, 6 ÷ 2 = 3). 2) 60: the difference is 2 units and Ben gave half of it, so 1 unit = 20; Ravi had 20, Ben 60 (then 40 and 40). 3) 300 g: take away the two extras, 1700 − 800 = 900 for 3 equal units, 900 ÷ 3 = 300 (flour 700 g each).'))

# ---------- 22 challenge ----------
ch=[('1.','Ali and Ben have 120 stickers altogether. Ali has 3 times as many as Ben. (a) How many stickers does each boy have? (b) Ali gives 20 stickers to Ben. How many does each boy have now?'),('2.','A pencil box and 3 pens cost $25 altogether. A pencil box and 5 pens cost $35 altogether. How much does one pen cost? How much does the pencil box cost?')]
put('p3l4-challenge',sec('p3l4-challenge','Challenge',h2('Challenge')+numbered(ch,36),'Pairs try first, then use the "see it" slide if stuck, then the walk-through. Answers: 1) (a) Ben 1 unit, Ali 3 units; 4 units = 120, so 1 unit = 30: Ben 30, Ali 90. (b) Ali 90 − 20 = 70, Ben 30 + 20 = 50. The total is still 120. 2) Pen $5, box $10. The second bill is $10 more because it has 2 more pens, so 2 pens cost $10 and 1 pen costs $5. Then 3 pens cost $15 and the box costs $10.'))

# ---------- 23 chdiag ----------
g=(T(345,34,'At first',28,TEAL,w=800)+NM(100,'Ben',28)+R(100,62,560/4,56,SKY,'?',size=28)
   +NM(176,'Ali',28)+''.join(R(100+140*m,138,140,56,SKY,'?' if m==0 else '',size=28) for m in range(3))+BV(62,194,540,'120',28)
   +T(345,250,'Ali gives 20 stickers to Ben',28,TEAL,w=800)
   +NM(306,'Ben',28)+R(100,268,140,56,SKY,'?',size=28)+R(240,268,70,56,YEL,'+20',size=24)
   +NM(382,'Ali',28)+R(100,344,350,56,SKY,'?',size=28)+R(450,344,70,56,GREY,'-20',size=24)+BV(268,400,540,'120',28))
q1=svgwrap('Before bars: Ben 1 unit, Ali 3 units, 120 altogether. After bars: Ali gives 20 stickers to Ben, so Ben gets 20 more and Ali has 20 fewer',690,470,g,'width:100%;height:auto')
pw=70
g=(T(345,34,'Bill 1: $25',28,TEAL,w=800)+R(90,50,110,60,YEL,'Box',size=26)+''.join(R(200+pw*i,50,pw,60,SKY,'Pen',size=22) for i in range(3))+BV(50,110,430,'$25',28)
   +T(345,190,'Bill 2: $35',28,TEAL,w=800)+R(90,206,110,60,YEL,'Box',size=26)+''.join(R(200+pw*i,206,pw,60,SKY,'Pen',size=22) for i in range(5))+BV(206,266,570,'$35',28)
   +T(345,340,'What is different about the two bills?',28,TEAL,w=800)+T(345,390,'One pen = ?',30,NAVY,w=800))
q2=svgwrap('Bill 1 is a box bar and three pen bars, 25 dollars. Bill 2 is a box bar and five pen bars, 35 dollars',690,470,g,'width:100%;height:auto')
body=h2('Challenge: see it',60)+'<div style="display:flex;gap:32px;align-items:flex-start">'+card('<p style="font-size:30px;font-weight:700;color:#1F7A6F">Q1: Before and after</p>'+q1,extra='flex:1;min-width:0;padding:20px 24px')+card('<p style="font-size:30px;font-weight:700;color:#1F7A6F">Q2: Two bills</p>'+q2,extra='flex:1;min-width:0;padding:20px 24px')+'</div>'
put('p3l4-chdiag',sec('p3l4-chdiag','Challenge',body,'Show after pairs have tried the Challenge, or if they are stuck. The pictures show the problem, not the answer. Ask: What stays the same? What do we know? For Q1: what happens to the total when Ali gives 20 to Ben? For Q2: what is different about the two bills? Answers are in the Challenge slide notes.'))

# ---------- 24 chwalk ----------
body=h2('Challenge: walk-through')+pin(128,250,800,p('Q1: draw the bars BEFORE and AFTER',38,800,TEAL))
for i,t in enumerate(['(a) Ben 1 unit, Ali 3 units, so 4 units = 120. 120 ÷ 4 = 30.','Ben has 30 and Ali has 90.','(b) Ali gives 20: Ali 90 − 20 = 70. Ben 30 + 20 = 50.','Check: 70 + 50 = 120 ✓ The total does not change.']): body+=pin(128,330+i*130,800,p(t,32),'rise',WHITE)
body+=pin(992,250,800,p('Q2: compare the two bills',38,800,TEAL))
for i,t in enumerate(['Bill 2 has 2 more pens than Bill 1.','It costs $35 − $25 = $10 more. So 2 pens cost $10.','1 pen = $10 ÷ 2 = $5.','3 pens cost $15, so the box is $25 − $15 = $10. Check: $10 + 5 × $5 = $35 ✓']): body+=pin(992,330+i*130,800,p(t,32),'rise',WHITE)
put('p3l4-chwalk',sec('p3l4-chwalk','Challenge',body,'Use after pairs have tried. Q1 is a before-and-after problem: find each boy’s share first (4 units = 120), then the giver goes down and the receiver goes up by the same amount, so the total stays 120. Q2: when two bills differ in only one thing, the difference in price tells you the price of that one thing.'))

# ---------- 25-26 talk, exit ----------
put('p3l4-talk',talk_slide('p3l4-talk','Mei and Siti are each given $5. Why does the difference between them stay the same?','Minutes 70 to 80. Pairs talk for 2 minutes, then share. Expected: both bars grow by the same piece, so the gap between their ends does not change. Follow-up: "When Mei GIVES Siti $5, what stays the same?" (the total). "How can a model help you check your answer?" (put the answers back: the parts must make the whole and the difference must match).'))
put('p3l4-exit',exit_slide('p3l4-exit','Ali has 3 times as many stickers as Ben. They have 80 stickers altogether. How many stickers does Ali have? Draw the model.','Minutes 80 to 90. Answer: 60. 4 units = 80, so 1 unit = 20, and Ali has 3 units. Watch for 80 ÷ 3. Extension: write your own before-and-after story, draw its model and check it, then swap with a partner.'))

# ---------- write ----------
order=['p3l4-title','p3l4-warm1','p3l4-warm2','p3l4-explore1','p3l4-explore2','p3l4-we1','p3l4-try1','p3l4-we2','p3l4-try2','p3l4-key','p3l4-break','p3l4-teachunits','p3l4-tryunits','p3l4-ws1','p3l4-ws1ans','p3l4-teachtd','p3l4-teachgive','p3l4-teachsame','p3l4-ws2','p3l4-ws2ans','p3l4-stretch','p3l4-challenge','p3l4-chdiag','p3l4-chwalk','p3l4-talk','p3l4-exit']
import p3_gifted; order[:]=p3_gifted.add(S,order,4)  # close-the-gaps: warm-up check + look-back slides
import p3_stories; order[:]=p3_stories.add(S,order,4)  # mathematician story break (optional)
assert set(order)==set(S), set(order)^set(S)
for f in os.listdir(os.path.join(D,'slides')):
    if f.endswith('.html') and f[:-5] not in S: os.remove(os.path.join(D,'slides',f))
for i,h in S.items(): open(os.path.join(D,'slides',i+'.html'),'w').write(h)
deck={'v':4,'createdOnFiles':{'v':1,'at':'2026-10-21T12:00:00Z'},'lists':'css','title':'Math Inquirers P3: Lesson 4 – Model Makers','order':order,'cover':'p3l4-title',
 'sections':{'s1':{'description':'Warm-up and explore','start':'p3l4-title'},'s2':{'description':'Teach: draw a model (part-whole and comparison)','start':'p3l4-we1'},'s3':{'description':'Worksheet with teaching before each page','start':'p3l4-break'},'s4':{'description':'Think harder, go further, talk and exit','start':'p3l4-stretch'}},
 'faces':{'fredoka':{'family':'Fredoka','href':'https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&display=swap'},'nunito-sans':{'family':'Nunito Sans','href':'https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@400;600;700&display=swap'}},
 'designSystems':[]}
json.dump(deck,open(os.path.join(D,'deck.json'),'w'),indent=1,ensure_ascii=False)
print(len(order),'slides')
