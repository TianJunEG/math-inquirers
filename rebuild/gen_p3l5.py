"""Math Inquirers P3, Lesson 5: Remainder Riddles. Writes split/p3l5/project (deck.json + slides/*.html)."""
import json,os,sys
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,H)
from slidekit import *
D=os.path.join(H,'..','split','p3l5','project'); os.makedirs(os.path.join(D,'slides'),exist_ok=True)
S={}; ORDER=[]
def put(i,h): S[i]=h; ORDER.append(i)
RED='#D64545'

# ---------- small helpers (local, slidekit stays untouched) ----------
def title_slide(sid,label,title,topic,today,notes):
    return (f'<section id="{sid}" data-transition="fade" style="background:{NAVY};color:{CREAM};font-family:{BF};padding:128px 128px 160px;display:flex;flex-direction:column;justify-content:center;gap:36px">\n'
            f'<p style="font-size:32px;font-weight:700;letter-spacing:4px;color:{YEL}">{E(label)}</p>\n'
            f'<h1 style="font-family:{HF};font-size:128px;font-weight:600;line-height:1.05">{E(title)}</h1>\n'
            f'<p style="font-size:44px;color:#C9D4EC">{E(topic)}</p>\n'
            f'<div style="background:#26385F;border-radius:24px;padding:40px;display:flex;flex-direction:column;gap:12px"><p style="font-size:28px;font-weight:700;letter-spacing:3px;color:{YEL}">TODAY WE WILL</p><p style="font-size:44px;font-weight:600">{E(today)}</p></div>\n'
            f'<p style="position:absolute;left:128px;bottom:64px;width:1400px;font-size:24px;color:#B7C3DD">{E(FOOT)}</p>\n<aside>{E(notes)}</aside>\n</section>\n')
def break_slide(sid,time,big,small,notes):
    return (f'<section id="{sid}" data-transition="fade" style="background:{TEAL};color:{CREAM};font-family:{BF};padding:128px 128px 160px;display:flex;flex-direction:column;justify-content:center;gap:36px">\n'
            f'<p style="font-size:32px;font-weight:700;letter-spacing:4px;color:{YEL}">{E(time)}</p>\n'
            f'<h2 style="font-family:{HF};font-size:110px;font-weight:600;line-height:1.05">Brain break</h2>\n'
            f'<p style="font-size:48px;font-weight:600">{E(big)}</p>\n<p style="font-size:36px;color:#D7EFEA">{E(small)}</p>\n'
            f'<p style="position:absolute;left:128px;bottom:64px;width:1400px;font-size:24px;color:#D7EFEA">{E(FOOT)}</p>\n<aside>{E(notes)}</aside>\n</section>\n')
def items(lst,size=38):
    return ''.join(card(p(f'<span style="color:{TEAL}">{a}</span>  {E(b)}',size,600,raw=True)) for a,b in lst)
def svgwrap(label,w,h,body,style=None):
    st=style or f'width:{w}px;height:{h}px'
    return f'<svg aria-label="{E(label)}" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="{st};display:block">{body}</svg>'
def T(x,y,t,size=32,col=NAVY,anchor='middle',weight=700,fam='Fredoka, Arial'):
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" fill="{col}" font-family="{fam}">{E(t)}</text>'
def dot(x,y,r=17,fill=YEL): return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="{NAVY}" stroke-width="3"/>'
def group4(x,y,fill=YEL,cup=True):
    """4 counters in a 2 x 2 cluster inside a cup outline, top-left at (x,y), size 100 x 100"""
    s=f'<rect x="{x}" y="{y}" width="100" height="100" rx="20" fill="{WHITE}" stroke="{TEAL}" stroke-width="4" stroke-dasharray="10 6"/>' if cup else ''
    for dx in (30,70):
        for dy in (30,70): s+=dot(x+dx,y+dy,16,fill)
    return s

# ---------- 1. title ----------
put('p3l5-title',title_slide('p3l5-title','LESSON 5  •  WEEK 3','Remainder Riddles','Division',
 'Divide with leftovers, decide what the leftover means in a story, work backwards, and crack “what number am I?” riddles with a list.',
 'Objective: Divide with remainders, check that the remainder is smaller than the number we divide by, decide what the leftover means in a story (one more group, or leave it out), work backwards from groups and leftovers, and solve "what number am I?" riddles by making a list. '
 'Heuristics taught today: WORK BACKWARDS (start number = groups × size + leftover) and MAKE A LIST (list the numbers that fit one clue, then test each with the other clue). '
 'Materials: 25 counters per child (or beans or buttons), 6 small cups for groups, mini whiteboards and markers. '
 'Online: children use 25 small things at home (dried beans, buttons, LEGO bricks) and a few cups or bowls; whiteboards are held up to the camera. '
 'Time plan: warm-up 0 to 10, explore 10 to 25, teaching 25 to 35 (click to reveal each step and answer), brain break 35 to 40, worksheet 40 to 70 with short teaching before each page and a check-together slide after it, talk time 70 to 80, exit ticket 80 to 90. Stretch and Challenge slides are for early finishers. If the class is behind, children finish the last question of each page at home; the check slides cover it.'))

# ---------- 2. warm-up game ----------
calls=[('23 in 4s','5 groups, 3 left'),('17 in 3s','5 groups, 2 left'),('26 in 8s','3 groups, 2 left'),('41 in 6s','6 groups, 5 left')]
body=h2('Warm-up: Leftover Lucky Dip')+card(chip('WARM-UP GAME',YEL,NAVY)+p('I call some sweets and a group size. Show the number of groups on one hand and the leftover on the other.',36,600))
CW=392
for i,(c,a) in enumerate(calls):
    L=128+i*(CW+32)
    body+=pin(L,500,CW,f'<p style="font-family:{HF};font-size:60px;font-weight:600;text-align:center">{E(c)}</p>',None,WHITE,24,'34px 20px',f'box-sizing:border-box;border:4px solid {NAVY};box-shadow:8px 8px 0 {NAVY}')
    body+=pin(L,680,CW,f'<p style="font-size:34px;font-weight:800;text-align:center">{E(a)}</p>','pop',YEL,20,'16px 18px','box-sizing:border-box')
put('p3l5-warm1',sec('p3l5-warm1','0–5 MIN',body,
 'Minutes 0 to 5. Leftover Lucky Dip. Call each card in turn: "23 sweets, groups of 4." Children show the number of groups on one hand and the leftover on the other (fists for zero). Then click to reveal. '
 'Always ask for the times-table fact: "4 × 5 = 20, and 3 more makes 23." Answers: 23 in 4s = 5 groups, 3 left; 17 in 3s = 5 groups, 2 left; 26 in 8s = 3 groups, 2 left; 41 in 6s = 6 groups, 5 left. '
 'Extra calls if time: 30 in 7s (4 groups, 2 left), 50 in 9s (5 groups, 5 left). Watch for children who say "41 in 6s is 5 groups and 11 left": ask "Can 11 make another group of 6?"'))

# ---------- 3. quick questions ----------
qs=[('1.','17 ÷ 5','3 r 2'),('2.','30 ÷ 7','4 r 2'),('3.','45 ÷ 6','7 r 3'),('4.','50 ÷ 8','6 r 2'),('5.','63 ÷ 9','7 r 0')]
body=h2('Quick questions')+''.join(qrow(128,250+i*125,1250,a,b,40) for i,(a,b,c) in enumerate(qs))+''.join(answer(1420,250+i*125,372,c) for i,(a,b,c) in enumerate(qs))
put('p3l5-warm2',sec('p3l5-warm2','5–10 MIN',body,
 'Minutes 5 to 10. Write "r" for remainder. Whiteboards up together, then click. After each one ask: "How can we check?" (answer × divisor + remainder: 7 × 6 + 3 = 45). '
 'Answers: 1) 3 r 2  2) 4 r 2  3) 7 r 3  4) 6 r 2  5) 7 r 0, nothing left over because 63 is in the 9 table.'))

# ---------- 4. explore: what to do ----------
pic=''
for g in range(6): pic+=group4(20+g*120,30)
pic+=dot(770,80,16,RED)+T(770,160,'1 left',26,RED)+T(380,170,'25 in groups of 4: 6 groups',28)
tx=900; heads=['Group size','Groups','Left over']; ws=[230,180,190]; rows=[['2','',''],['3','',''],['4','6','1'],['5','',''],['6','','']]
x=tx
for h_,w_ in zip(heads,ws): pic+=f'<rect x="{x}" y="6" width="{w_}" height="40" fill="{YEL}" stroke="{NAVY}" stroke-width="2"/>'+T(x+w_/2,36,h_,24); x+=w_
for r,row in enumerate(rows):
    x=tx
    for c_,w_ in zip(row,ws): pic+=f'<rect x="{x}" y="{46+r*36}" width="{w_}" height="36" fill="{WHITE}" stroke="{NAVY}" stroke-width="2"/>'+T(x+w_/2,46+r*36+27,c_,24); x+=w_
pic=svgwrap('25 counters in six groups of 4 with 1 left over, and a table of group sizes, groups and leftovers',1520,236,pic,'width:100%;height:auto')
steps_html='<ol style="font-size:32px;font-weight:600;padding-left:48px;display:flex;flex-direction:column;gap:6px">'+''.join(f'<li>{E(s)}</li>' for s in ['Take 25 counters.','Put them in groups of 2, then 3, 4, 5 and 6.','Record the groups and the leftover in a table.','Ask: what do you notice about the leftovers?'])+'</ol>'
body=h2('Explore: what to do')+card(chip('EXPLORE')+steps_html,extra='padding:22px 40px;gap:8px')+card(pic,extra='padding:12px 24px')
put('p3l5-explore1',sec('p3l5-explore1','10–15 MIN',body,
 'Minutes 10 to 15. Predict first: "Which group size will leave nothing over?" Pairs make the groups with real counters (cups help) and fill in the table on a whiteboard. '
 'Results: 2s: 12 groups, 1 left. 3s: 8 groups, 1 left. 4s: 6 groups, 1 left. 5s: 5 groups, 0 left. 6s: 4 groups, 1 left. '
 'Hints: "Use a times-table fact: 6 × 4 = 24." Finished early: "Try 49 counters. Which group sizes leave 1 over? Why?" (2, 3, 4, 6 and 8 all leave 1, because 48 is in all those tables; 7s leave 0.) '
 'Online: children use beans or buttons and hold the whiteboard to the camera.'))

# ---------- 5. explore: talk ----------
body=h2('Explore: talk about it')+items([('1.','Which group size left nothing over?'),('2.','Why did 2s, 3s, 4s and 6s all leave 1 over?'),('3.','In groups of 4, can 4 or more be left over?')],40)
put('p3l5-explore2',sec('p3l5-explore2','15–25 MIN',body,
 'Minutes 15 to 25. Let pairs keep working, then gather. Answers: 1) Groups of 5: 25 is in the 5 table. 2) 24 is in the 2, 3, 4 and 6 tables, and 25 is one more than 24. '
 '3) No. If 4 were left over they would make another group. The leftover (remainder) is always smaller than the group size. This is the rule we use all lesson.'))

# ---------- 6. teach: remainder rule ----------
def fourteen(ok):
    b=''
    n=3 if ok else 2
    for g in range(n): b+=group4(10+g*120,20)
    left=2 if ok else 6
    for k in range(left):
        b+=dot(10+n*120+30+(k%3)*42,50+(k//3)*42,16,RED)
    return b
svA=svgwrap('14 counters: 3 groups of 4 and 2 left over',740,140,fourteen(True))
svB=svgwrap('14 counters: 2 groups of 4 and 6 left over',740,140,fourteen(False))
body=h2('The remainder rule')+card(p('14 counters in groups of 4. Which picture is right?',40,700))
body+=pin(128,420,816,svA+p('3 groups, 2 left over.  14 ÷ 4 = 3 r 2 ✓',34,700),None,WHITE,20,'20px 26px','box-sizing:border-box')
body+=pin(976,420,816,svB+p('2 groups, 6 left over: not this one. 4 of the 6 make another group!',34,700,RED),'rise',WHITE,20,'20px 26px','box-sizing:border-box')
body+=pin(128,760,1664,p('The leftover must be SMALLER than the group size. If it is not, make another group.',36,800),'fade',SOFT,20,'20px 30px')
put('p3l5-teach1',sec('p3l5-teach1','25–27 MIN',body,
 'Teach. Show 14 counters and make groups of 4 in front of the children. Click 1: the wrong picture (2 groups, 6 left). Ask: "What is wrong?" Click 2: the rule. '
 'Think-aloud: "When I divide, I keep making groups until I cannot make another one. So what is left must be smaller than the group size. Dividing by 4, the remainder can only be 0, 1, 2 or 3."'))

# ---------- 7. worked example 1 ----------
body=h2('Worked example: share with a leftover')+card(p('Ali shares 38 sweets equally among 5 children. How many does each child get? How many are left over?',40,700))
body+=step(1,'Count in 5s: 5 × 7 = 35. 5 × 8 = 40 is too many. Each child gets 7.',top=440,size=36)
body+=step(2,'38 − 35 = 3 left over. Is 3 smaller than 5? Yes.  38 ÷ 5 = 7 r 3',top=550,size=36)
body+=step(3,'Check: 7 × 5 + 3 = 35 + 3 = 38 ✓',top=660,size=36)
body+=step(4,'How many more sweets so that none are left over? 40 − 38 = 2 more.',top=770,size=36)
put('p3l5-we1',sec('p3l5-we1','27–29 MIN',body,
 'Click to reveal each step; ask the group to predict it first. Think-aloud: "38 sweets for 5 children. I count in 5s: 5 × 7 = 35, 5 × 8 = 40, too many. So each child gets 7. I used 35, so 3 are left. 3 is smaller than 5, good. I check: 7 × 5 + 3 = 38." '
 'Step 4 is new for most children: the next number in the 5 table is 40, so 2 more sweets would leave none over.'))

# ---------- 8. try 1 ----------
put('p3l5-try1',try_slide('p3l5-try1','29–30 MIN','Your turn: whiteboards','Write the answer and the remainder. Check that the remainder is small enough.',
 [('a','29 ÷ 4','7 r 1'),('b','52 ÷ 9','5 r 7'),('c','Tom says 40 ÷ 6 = 5 r 10. Fix it.','6 r 4')],
 'Whiteboards up together, then click. a) 4 × 7 = 28, 1 left. b) 9 × 5 = 45, 7 left (7 is smaller than 9, so it is fine). c) 10 is bigger than 6, so another group fits: 6 × 6 = 36, 4 left. Ask: "How could Tom have noticed his mistake?"'))

# ---------- 9. worked example 2: what does the leftover mean ----------
body=h2('Worked example: what does the leftover mean?')+card(p('A van holds 8 people. 50 people go on a trip. How many vans are needed?',40,700))
body+=step(1,'50 ÷ 8 = 6 r 2:  6 full vans, and 2 people are left over.',top=380,size=36)
body+=step(2,'The 2 people still need a ride, so we need one more van:  7 vans.',top=490,size=36)
body+=pin(128,620,1664,p('Now: 50 cakes are packed into boxes of 8. How many boxes are FULL?',38,700),'fade',SOFT,20,'20px 30px')
body+=step(3,'50 ÷ 8 = 6 r 2 again, but only full boxes count:  6 boxes. Read the question!',top=740,size=36)
put('p3l5-we2',sec('p3l5-we2','30–32 MIN',body,
 'Click through. Think-aloud: "50 people, vans of 8: 50 ÷ 8 = 6 r 2. Those 2 people cannot stay behind, so I need one more van: 7. But 50 cakes in boxes of 8 fill only 6 boxes; the 2 cakes do not make a full box. Same division, different answer. I read the question again." '
 'Ask: "Can you think of another story where we need one more group?" (tables, buses, boats, boxes to hold ALL the things).'))

# ---------- 10. try 2 ----------
put('p3l5-try2',try_slide('p3l5-try2','32–33 MIN','Your turn: one more, or leave it out?','Divide first. Then think about the leftover.',
 [('a','26 children. A car holds 4. How many cars?','7 cars'),('b','$40. A toy costs $6. How many toys?','6 toys'),('c','45 cm of ribbon. Cut 8 cm pieces. How many?','5 pieces')],
 'Whiteboards. a) 26 ÷ 4 = 6 r 2: the 2 children need a car, so 7. b) 40 ÷ 6 = 6 r 4: $4 is not enough for another toy, so 6. c) 45 ÷ 8 = 5 r 5: 5 whole pieces and 5 cm left over. Ask a child to explain a) and b) side by side.',size=36))

# ---------- 11. key idea ----------
body=h2('Key idea: read the leftover')+card(p('The remainder is always smaller than the number we divide by.  Start number = groups × size + leftover.',44,700))+card(p('Then ask: does the leftover need one more group, or is it left out?',38,600,MUTED))
put('p3l5-key',sec('p3l5-key','33–35 MIN',body,
 'Say the key idea together. Common mistakes to watch for during the worksheet: (1) Leaving a remainder that is as big as, or bigger than, the number we divide by (60 ÷ 7 = 7 r 11). '
 '(2) Giving the division answer when the story needs one more group (minibuses, boxes for ALL the eggs), or adding one when only full groups count (books she can buy). '
 '(3) Stopping at the first number that fits one clue in a riddle, without testing the other clue or finding ALL the numbers.'))

# ---------- 12. break ----------
put('p3l5-break',break_slide('p3l5-break','35–40 MIN','Clap-and-stomp groups. “Clap 17 in 5s!” Clap in groups of 5, then stomp once for each leftover clap.','Then try 23 in 4s and 20 in 6s. A drink of water and back to our seats.','Five minutes. 17 in 5s: 3 groups, 2 stomps. 23 in 4s: 5 groups, 3 stomps. 20 in 6s: 3 groups, 2 stomps. Online: children stay in view of the camera and move in place.'))

# ---------- 13. teach before page 1: work backwards ----------
bags=''
for i in range(9):
    x=10+(i%5)*112; y=10+(i//5)*130
    bags+=f'<path d="M{x+14} {y+30} L{x+86} {y+30} L{x+94} {y+112} L{x+6} {y+112} Z" fill="{SKY}" stroke="{NAVY}" stroke-width="3"/><rect x="{x+30}" y="{y+14}" width="40" height="18" rx="6" fill="{TEAL}" stroke="{NAVY}" stroke-width="3"/>'+T(x+50,y+88,'6',40)
for k in range(4): bags+=dot(470+(k%2)*46,170+(k//2)*46,17,'#C68B59')
bags+=T(493,262,'4 left',26,TEAL)
svb=svgwrap('9 bags with 6 cookies in each and 4 cookies left over',580,280,bags)
body=h2('Work backwards: groups × size + leftover')+chip('HEURISTIC: WORK BACKWARDS',YEL,NAVY)+card(p('Mei packs cookies into bags of 6. She fills 9 bags and has 4 cookies left. How many cookies does she have?',40,700))
body+=step(1,'9 bags of 6:  9 × 6 = 54',top=520,width=960,size=36)
body+=step(2,'Add the leftover:  54 + 4 = 58 cookies',top=630,width=960,size=36)
body+=step(3,'Check forwards:  58 ÷ 6 = 9 r 4 ✓',top=740,width=960,size=36)
body+=pin(1200,520,592,svb,None,WHITE,20,'12px 6px','box-sizing:border-box')
put('p3l5-teachback',sec('p3l5-teachback','40–42 MIN',body,
 'Teach before worksheet page 1 (Q3 works backwards from bags and a leftover, then repacks). Heuristic: WORK BACKWARDS. Say: "Division splits the cookies into bags and a leftover. To go back, we put the bags together, groups × size, and add the leftover." '
 'Think-aloud: "9 bags of 6 is 54. Plus the 4 loose ones: 58. I check by dividing again: 58 ÷ 6 = 9 r 4. That matches the story." Ask: "Why must the leftover be less than 6?" (otherwise she could fill another bag).'))

# ---------- 14-15. worksheet page 1 ----------
put('p3l5-ws1',ws_preview('p3l5-ws1','42–52 MIN','Worksheet page 1: with your partner',
 [('Q1','Siti’s stickers. Is the remainder smaller than 6? Then fix Ben’s mistake.'),('Q2','Minibuses, books and egg boxes: what does the leftover mean?'),('Q3','Ravi’s marbles: work backwards, then pack them again.')],
 'Stuck? Use counters, or count up in the times table.',
 'Minutes 42 to 52. Walk around. Ask "Is your remainder smaller than the number you divided by?" and "What happens to the leftover in this story?" before giving any help. For Q2c check that pairs give two different answers.'))
put('p3l5-ws1ans',check_slide('p3l5-ws1ans','52–54 MIN','Page 1: check together',
 [('Q1','(a) 7 each, 5 left over   (b) 1 more   (c) 11 is bigger than 7, so 8 r 4'),('Q2','(a) 9 minibuses   (b) 8 books   (c) 14 full boxes; 15 boxes for all'),('Q3','(a) 12 × 8 + 5 = 101   (b) 11 full bags, 2 left over')],
 'Click after a pair explains. Q1: 6 × 7 = 42, 47 − 42 = 5; 48 is in the 6 table, so 1 more sticker. Q1c: 7 × 8 = 56, 60 − 56 = 4. Q2: 75 ÷ 9 = 8 r 3 (the 3 pupils need a bus: 9); 60 ÷ 7 = 8 r 4 ($4 is not enough: 8); 87 ÷ 6 = 14 r 3. Q3: 9 × 11 = 99, so 101 ÷ 9 = 11 r 2.'))

# ---------- 16. teach before page 2: make a list ----------
body=h2('What number am I? Make a list')+chip('HEURISTIC: MAKE A LIST',YEL,NAVY)+card(p('I am between 20 and 40. Divided by 3, my remainder is 2. Divided by 5, my remainder is 4. Who am I?',40,700))
body+=step(1,'List the clue with the BIGGER divisor first (a shorter list). Remainder 4 when ÷ 5:  24, 29, 34, 39',top=520,size=34)
body+=step(2,'Test each one with ÷ 3:  24 r 0,  29 r 2 ✓,  34 r 1,  39 r 0',top=660,size=34)
body+=step(3,'Only 29 fits both clues. For “find ALL”, keep every number that fits.',top=770,size=34)
put('p3l5-teachlist',sec('p3l5-teachlist','54–56 MIN',body,
 'Teach before worksheet page 2 (Q4). Heuristic: MAKE A LIST. Think-aloud: "Two clues. I list the numbers for one clue, then test them with the other. The 5 clue gives a shorter list: 5 × 4 = 20, plus 4 is 24, then every 5 more: 29, 34, 39. Now test with 3." '
 'Stress: write the list in order so nothing is missed. If a question says "find ALL", do not stop at the first one. Check 29: 3 × 9 = 27, remainder 2 ✓; 5 × 5 = 25, remainder 4 ✓.'))

# ---------- 17. teach: biggest remainder ----------
body=h2('The biggest remainder')+p('Dividing by 6, the remainder can only be 0, 1, 2, 3, 4 or 5.',36,600,MUTED)+card(p('A number between 30 and 40 is divided by 6. The remainder is as big as it can be. What is the number?',40,700))
body+=step(1,'The biggest remainder when ÷ 6 is 5 (one less than 6).',top=500,size=36)
body+=step(2,'Numbers in the 6 table near 30 to 40: 30 and 36. Add 5: 35 and 41.',top=610,size=36)
body+=step(3,'41 is too big. The number is 35. Check: 35 ÷ 6 = 5 r 5 ✓',top=720,size=36)
put('p3l5-teachbig',sec('p3l5-teachbig','56–57 MIN',body,
 'Teach before worksheet page 2 (Q5). Ask first: "Dividing by 6, could the remainder be 6? Could it be 7?" (No: another group would fit.) The biggest remainder is always one less than the number we divide by. Then click through.'))

# ---------- 18. teach: make a table ----------
W4=[170,440,240,170]
body=h2('Make a table: the benches')+card(p('If 3 children sit on each bench, 4 children must stand. If 4 sit on each bench, every seat is filled. How many benches? How many children?',38,700))
body+=trow(128,440,['Benches','3 on each + 4 standing','4 on each','Same?'],W4,None,True,32)
for i,r in enumerate([['1','7','4','no'],['2','10','8','no'],['3','13','12','no'],['4','16','16','yes ✓']]): body+=trow(128,522+i*82,r,W4,'rise',False,32)
body+=pin(1400,440,392,p('The gap shrinks by 1 on each row. 4 standing, so 4 rows: 4 benches, 16 children.',30,700),'fade',SOFT,20,'20px 22px')
put('p3l5-teachtable',sec('p3l5-teachtable','57–58 MIN',body,
 'Teach before worksheet page 2 (Q6, the party tables). Click to build each row while children say the numbers. Think-aloud: "1 bench: 3 + 4 = 7 children, but 4 on a bench holds only 4. Not the same. 2 benches: 6 + 4 = 10 and 8. Closer." '
 'Point out the pattern: each extra bench takes one more of the standing children, so the gap shrinks by 1 each row. 4 standing children means 4 benches. Check: 4 × 3 + 4 = 16 and 4 × 4 = 16.'))

# ---------- 19-20. worksheet page 2 ----------
put('p3l5-ws2',ws_preview('p3l5-ws2','58–66 MIN','Worksheet page 2: on your own',
 [('Q4','What number am I? List, then test. Part b: find ALL the numbers.'),('Q5','Dividing by 8: every remainder, and the biggest one.'),('Q6','If time: the party tables. Fill in the table until the rows match.')],
 'Finished early? Stretch and Challenge come next.',
 'Children work alone. Note who needs a short catch-up next lesson. Check that every child writes a list for Q4 and fills the table for Q6.'))
put('p3l5-ws2ans',check_slide('p3l5-ws2ans','66–70 MIN','Page 2: check together',
 [('Q4','(a) 53   (b) 11, 23, 35, 47 (they go up in 12s)'),('Q5','(a) 0, 1, 2, 3, 4, 5, 6, 7   (b) 63'),('Q6','(a) 5 tables, 35 children   (b) 5 empty seats')],
 'Click after a child explains. Q4a: 43, 48, 53, 58; divided by 4 they leave 3, 0, 1, 2, so 53. Q4b: remainder 5 when ÷ 6: 11, 17, 23, 29, 35, 41, 47; test ÷ 4: 11, 23, 35, 47 leave 3. Ask: "Why do they go up in 12s?" (12 is in both the 4 and 6 tables). '
 'Q5b: biggest remainder 7; 56 + 7 = 63. Q6: rows 11/7, 17/14, 23/21, 29/28, 35/35. With 8 at each table: 40 seats − 35 children = 5 empty.'))

# ---------- 21. stretch (new items) ----------
body=h2('Stretch')+items([('1.','Siti has between 40 and 50 beads. In groups of 6, 1 is left over. In groups of 4, 3 are left over. How many beads?'),('2.','A number ÷ 9 = 8 r 7. What is the number ÷ 8?'),('3.','Ali packs 60 cupcakes into boxes of 8. How many more cupcakes does he need to fill one more box?')],36)
put('p3l5-stretch',sec('p3l5-stretch','For early finishers',body,
 'For children who finish early. Answers: 1) 43 (remainder 1 when ÷ 6: 43 and 49; 43 ÷ 4 = 10 r 3 ✓, 49 ÷ 4 = 12 r 1). 2) 9 r 7 (work backwards: 9 × 8 + 7 = 79; 79 ÷ 8 = 9 r 7). 3) 4 more (60 ÷ 8 = 7 r 4; the next box needs 64).'))

# ---------- 22. challenge ----------
body=h2('Challenge')+items([('1.','Today is Monday. What day of the week will it be 100 days from today? What day of the week was it 100 days ago?'),('2.','Mr Lim gives pens to his pupils. If each pupil gets 4 pens, 10 pens are left over. If each pupil gets 6 pens, he is 4 pens short. How many pupils are there? How many pens does he have?')],38)
put('p3l5-challenge',sec('p3l5-challenge','Challenge',body,
 'Pairs try first, then use the "see it" slide if stuck, then the walk-through. Answers: 1) Wednesday in 100 days (100 ÷ 7 = 14 r 2, so 2 days after Monday). Saturday 100 days ago (14 weeks back is Monday, then 2 more days back: Sunday, Saturday). 2) 7 pupils and 38 pens.'))

# ---------- 23. challenge: see it ----------
days=['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
cal=''
for w in range(2):
    for i,dn in enumerate(days):
        x=8+i*104; y=40+w*130
        f=YEL if i==0 else (SKY if i>=5 else WHITE)
        cal+=f'<rect x="{x}" y="{y}" width="96" height="80" rx="10" fill="{f}" stroke="{NAVY}" stroke-width="3"/>'+T(x+48,y+52,dn,28)
cal+=T(8,32,'Today',24,TEAL,'start')+T(8,282,'7 days later',24,TEAL,'start')
cal+=T(380,340,'Every 7 days it is Monday again.',28)+T(380,390,'How many weeks fit in 100 days?',28,TEAL)
sv1=svgwrap('Two weeks of day boxes, Monday to Sunday, starting today on Monday',740,410,cal,'width:100%;height:auto')
def pen(x,y,dash=False):
    extra=' stroke-dasharray="6 4"' if dash else ''
    fill='none' if dash else TEAL; st=RED if dash else NAVY
    return f'<rect x="{x}" y="{y}" width="12" height="54" rx="4" fill="{fill}" stroke="{st}" stroke-width="3"{extra}/>'
def kid(x,y,n):
    s=f'<circle cx="{x+48}" cy="{y+22}" r="20" fill="{YEL}" stroke="{NAVY}" stroke-width="3"/><path d="M{x+18} {y+78} Q{x+48} {y+36} {x+78} {y+78} Z" fill="{YEL}" stroke="{NAVY}" stroke-width="3"/>'
    for k in range(n): s+=pen(x+6+k*15,y+90)
    return s
pp=T(360,30,'4 pens each:',26,TEAL)
for i in range(3): pp+=kid(10+i*110,44,4)
pp+=T(352,124,'…',44)+T(560,100,'10 left over',26,TEAL)
for k in range(10): pp+=pen(420+k*17,124)
pp+=T(360,240,'6 pens each:',26,TEAL)
for i in range(3): pp+=kid(10+i*110,254,6)
pp+=T(352,334,'…',44)+T(560,310,'4 short',26,RED)
for k in range(4): pp+=pen(470+k*17,334,True)
sv2=svgwrap('Pupils with 4 pens each and 10 pens left over; pupils with 6 pens each and 4 pens missing',740,400,pp,'width:100%;height:auto')
body=h2('Challenge: see it',60)+'<div style="display:flex;gap:32px;align-items:flex-start">'+card('<p style="font-size:28px;font-weight:700;color:#1F7A6F">Q1: Days come in weeks of 7</p>'+sv1,extra='flex:1;min-width:0;padding:20px 24px')+card('<p style="font-size:28px;font-weight:700;color:#1F7A6F">Q2: Two ways to share the pens</p>'+sv2,extra='flex:1;min-width:0;padding:20px 24px')+'</div>'
put('p3l5-chdiag',sec('p3l5-chdiag','Challenge',body,
 'Show after pairs have tried, or if they are stuck. The pictures show the problem, not the answer. Q1: "Every 7 days we are back to Monday. So what matters is the leftover after the full weeks." Q2: "What changes between the two rows? How many more pens does each pupil get? Where do those extra pens come from?"'))

# ---------- 24. challenge walk-through ----------
body=h2('Challenge: walk-through')+pin(128,250,800,p('Q1: weeks are groups of 7',38,800,TEAL))
for i,t in enumerate(['100 ÷ 7 = 14 r 2. After 14 weeks (98 days) it is Monday again.','Forward 2 more days: Tuesday, then Wednesday.','Backward: 14 weeks ago was Monday; 2 more days back: Sunday, then Saturday.','100 days from Monday is Wednesday. 100 days ago was Saturday ✓']): body+=pin(128,330+i*110,800,p(t,32),'rise',WHITE)
body+=pin(992,250,800,p('Q2: compare the two shares',38,800,TEAL))
for i,t in enumerate(['From 4 to 6 pens, each pupil gets 2 more.','That needs the 10 spare pens + 4 more = 14 pens.','14 ÷ 2 = 7 pupils.','Pens: 7 × 4 + 10 = 38. Check: 7 × 6 = 42 = 38 + 4 ✓']): body+=pin(992,330+i*110,800,p(t,32),'rise',WHITE)
put('p3l5-chwalk',sec('p3l5-chwalk','Challenge',body,
 'Use after pairs have tried. Q1: the remainder is what matters: full weeks bring us back to the same day. Many children count on 100 from Monday or say Tuesday; the table of days shows why it is 2 days on. For 100 days AGO, children often say Wednesday again: ask them to go backwards, so 2 days BEFORE Monday is Saturday. '
 'Q2: if children are stuck, act it out with 3 or 4 "pupils" and pens; a table (pupils 1, 2, 3 … with pens needed both ways) also works: 7 pupils is where 4 × 7 + 10 = 38 and 6 × 7 − 4 = 38 match.'))

# ---------- 25. talk ----------
body=h2('Talk time')+card(chip('TALK TIME',YEL,NAVY)+p('Why can the remainder never be as big as the number we divide by?',42,600))+card(p('Sentence starters:',34,400,MUTED)+p('“I noticed that …”   “I tested it by …”   “I know because …”',38,600))
put('p3l5-talk',sec('p3l5-talk','70–80 MIN',body,
 'Minutes 70 to 80. Pairs talk for 2 minutes, then share. Second question if time: "75 ÷ 9 = 8 r 3. Why was the minibus answer 9, not 8?" '
 'Answer: If the leftover were as big as the group size, we could make one more group, so the remainder is always smaller. The 3 pupils left over still need a seat, so we need one more minibus. Praise the reasons, not only the answers.'))

# ---------- 26. exit ----------
body=h2('Exit ticket')+card(chip('EXIT TICKET')+p('52 children go on a ride. Each car holds 6 children. How many cars are needed? Write the division and explain the leftover.',44,600))+card(p('Write your answer on a slip of paper. Show it to your tutor. Then collect your stamp in your inquiry journal.',34,400))
put('p3l5-exit',sec('p3l5-exit','80–90 MIN',body,
 'Minutes 80 to 90. Answer: 52 ÷ 6 = 8 r 4. 9 cars are needed: the 4 children left over still need a car. Extension: Find the smallest number bigger than 1 that leaves a remainder of 1 when divided by 2, 3, 4, 5 and 6 (61).'))

# ---------- write ----------
import p3_gifted; ORDER[:]=p3_gifted.add(S,ORDER,5)  # close-the-gaps: warm-up check + look-back slides
for f in os.listdir(os.path.join(D,'slides')):
    if f.endswith('.html') and f[:-5] not in S: os.remove(os.path.join(D,'slides',f))
for i,h in S.items(): open(os.path.join(D,'slides',i+'.html'),'w').write(h)
deck={'v':4,'createdOnFiles':{'v':1,'at':'2026-10-21T12:00:00Z'},'lists':'css','title':'Math Inquirers P3: Lesson 5 – Remainder Riddles','order':ORDER,'cover':'p3l5-title',
 'sections':{'s1':{'description':'Warm-up and explore','start':'p3l5-title'},'s2':{'description':'Teach: remainders and what they mean','start':'p3l5-teach1'},'s3':{'description':'Worksheet with teaching before each page','start':'p3l5-break'},'s4':{'description':'Think harder, go further, talk and exit','start':'p3l5-stretch'}},
 'faces':{'fredoka':{'family':'Fredoka','href':'https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&display=swap'},'nunito-sans':{'family':'Nunito Sans','href':'https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@400;600;700&display=swap'}},
 'designSystems':[]}
json.dump(deck,open(os.path.join(D,'deck.json'),'w'),indent=1,ensure_ascii=False)
print(len(ORDER),'slides')
