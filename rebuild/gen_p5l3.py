"""Math Inquirers P5, Lesson 3: Before and After. Writes split/p5l3/project (deck.json + slides/*.html)."""
from p5l34_common import *
L='p5l3'; S={}
def put(i,h): S[f'{L}-{i}']=h
C=load(3); LS=C['lesson']; DK=C['deck']
GRN='#BFE3DC'; ORG='#F6D58A'

# ---- 1. title ----
put('title',title_slide(f'{L}-title','LESSON 3  •  WEEK 2','Before and After','Fraction word problems',DK['today'],
 'Objective: '+LS['objective']+' Thinking strategies today: DRAW A MODEL and ASK "WHAT STAYS THE SAME?" Materials: '+LS['materials']+' Online: '+LS['online']+
 ' Time plan: sneak-peek puzzles 0 to 3 (private answers, nobody is marked), warm-up 3 to 9, explore 9 to 21 (a Go further what-if is on the explore slide for anyone who wants more), teaching 21 to 33 (click to reveal each step and answer), brain break 33 to 37, workbook page 1 37 to 49 (after question 2 you may choose: carry on, or try Think harder), check together 49 to 53, short teaching before page 2 53 to 58, workbook page 2 58 to 72 (alone: start with the questions named at the top, then choose; nobody has to finish), check together 72 to 76, talk time 76 to 82 (you may say pass; volunteers first; then everyone tries the first step of the Investigation), exit ticket 82 to 86, reflection 86 to 88 (pass is always OK), stamp and goodbye 88 to 90. Think harder, Go further and the Investigation are open to every child. The tutor never announces who is on which page, and never splits a pair unless both children agree. Invite the WHOLE group, never one child: "when you have finished Start here you can choose Think harder, Go further or the Investigation."'))

# ---- 2. warm-up game: what's left ----
bar=bars([('',[(3,YEL,'given away'),(9,SKY,'left')])],135,x0=10,y0=8,bh=70,label='A jar of 120 marbles cut into 12 equal units; 3 units given away, 9 left',seg_size=32)
body=h2("Warm-up: What's left?")+card(p('A jar has 120 marbles. I turn over two cards, one at a time. After each card, draw what is LEFT as a new bar and write how many marbles are left. Each card says what to take the fraction of: "of the jar" or "of what is left".',36,700))
body+=pin(128,420,1664,bar+p('Each unit is 10 marbles. Card 1 gives away 3 units.',30,600,MUTED),None,WHITE,24,'16px 30px')
cards=[('Card 1','Give away 1/4 of the jar.','90 left'),('Card 2','Give away 1/3 of what is left.','60 left')]
for i,(a,b,c) in enumerate(cards):
    body+=qrow(128,660+i*110,1250,a,b,36)+answer(1420,660+i*110,372,c)
put('warm1',sec(f'{L}-warm1','0–4 MIN',body,
 'Minutes 0 to 4. What is left? Children have mini whiteboards. Say "Card 1" and read it; give thinking time; children write the number left and say the answer together on three; click to show the answer. Then Card 2. '
 'Talk: Card 2 says "of what is left", so we take 1/3 of 90, not 1/3 of 120 (90 − 30 = 60). Tutor extension if the group is ready: a third card, give away 5/6 of what is left (5/6 of 60 is 50, so 10 are left). Ask: "Did anyone take 1/3 of 120? What would that give? (40; the story would be different.)" '
 'The bar shows the first card: 120 is cut into 12 units of 10, and 1/4 is 3 units. Listen for children who draw the remainder as a new bar. Answers: 90, 60. This is the idea of the whole lesson: after each step the amount we start from changes.'))

# ---- 3. quick questions ----
qs=[('1.','What is 2/5 of 45?','18'),('2.','3/4 of a number is 27. What is the number?','36'),('3.','What is 1/3 of 3/4?','1/4'),('4.','Ali has 12 more stickers than Ben. They each get 5 more. How many more does Ali have now?','Still 12')]
body=h2('Quick questions')
for i,(a,b,c) in enumerate(qs):
    body+=qrow(128,240+i*130,1370,a,b,34)+answer(1530,240+i*130,262,c)
put('warm2',sec(f'{L}-warm2','4–9 MIN',body,'Minutes 4 to 9. Whiteboards: read each question aloud, give thinking time, write on boards, say the answer together on three, click to show. Answers: 1) 18 (45 ÷ 5 = 9, 9 × 2).  2) 36 (3 units = 27, 1 unit = 9, 4 units = 36).  3) 1/4 (1/3 of 3 quarters is 1 quarter).  4) Still 12: both get the same, so the gap does not change.  Question 4 is one of the two big ideas of today (the other is that the total stays the same when cards move between two children); do not explain yet, just ask "why?" and collect ideas. If you are short of time, skip question 4.',
 ))

# ---- 4. explore: what to do ----
def counters(n,x,y,r=19,fill=YEL,gap=47):
    return ''.join(f'<circle cx="{x+i*gap}" cy="{y}" r="{r}" fill="{fill}" stroke="{NAVY}" stroke-width="3"/>' for i in range(n))
g=txt(70,50,'Ali',34,NAVY,'end',700,'Nunito Sans, Arial')+counters(18,100,40)+txt(70,110,'Mei',34,NAVY,'end',700,'Nunito Sans, Arial')+counters(6,100,100,fill=SKY)
g+=f'<path d="M1000 50 H1050 M1030 36 L1052 50 L1030 64" fill="none" stroke="{TEAL}" stroke-width="5"/>'+txt(1075,60,'Ali gives Mei',32,TEAL,'start',800,'Nunito Sans, Arial')+txt(1075,100,'1 counter at a time',32,TEAL,'start',800,'Nunito Sans, Arial')
steps=''.join(f'<li>{E(s)}</li>' for s in DK['expSetup'])
body=h2('Explore: what to do')+card(chip('EXPLORE')+f'<ol style="font-size:34px;font-weight:600;padding-left:52px;display:flex;flex-direction:column;gap:6px">{steps}</ol>')
body+=card(svgwrap(1500,140,'Ali has a row of 18 counters and Mei a row of 6 counters; Ali gives Mei counters one at a time',g),extra='padding:14px 32px')
put('explore1',sec(f'{L}-explore1','9–14 MIN',body,'Minutes 9 to 14. Pairs use 24 counters or paper squares (online: paper squares on the desk, camera up as usual; check the table against the slide). Predict first: when Ali gives counters away, does the total change? Does the difference change? Let pairs record in two tables: Ali, Mei, total, difference. Second table: start again at 18 and 6 and give BOTH children 2 more each time. Anyone who wants more (open to every pair): find when Mei has 1/3 as many as Ali (right at the start: 18 and 6), and 3/5 as many (after Ali gives 3: 15 and 9).'))
body=h2('Explore: talk about it')+numcards([('1.',DK['expAsk'][0][0]),('2.',DK['expAsk'][1][0])],40)
put('explore2',sec(f'{L}-explore2','14–21 MIN',body,'Minutes 14 to 21. Pencils down: gather the pairs. Build one table on the board and ask for each row. Answers: 1) The total: 24 every time Ali gives Mei counters (16 and 8, 15 and 9 …). 2) The difference: 12 every time both get 2 more (20 and 8, 22 and 10 …). (Not asked together: when did Mei have 1/2 as many as Ali? After Ali gives 2 (16 and 8), and after both get 6 more (24 and 12).) Ask: "Why does the total stay the same when Ali gives and the difference stay the same when both get?" Do NOT tell: the next slides name these two ideas.'))

# ---- 5. teach 1: fraction of a remainder ----
A=svgwrap(1130,100,'A bar for Mei\'s money cut into 5 equal parts; 2 parts are the bag',pbar(170,12,190,[(2,YEL,'bag',2),(3,WHITE,'3 parts left',3)],lab='Money',seg=30)+'')
B=svgwrap(1130,100,'The same bar with every part cut in 2: 10 equal units; bag 4 units, shoes 3 units, left 3 units',pbar(170,12,95,[(4,YEL,'bag',4),(3,SKY,'shoes',3),(3,GRN,'left',3)],lab='Money')+'')
body=h2('Worked example: fraction of the remainder',64)+card(p('Mei spent 2/5 of her money on a bag and 1/2 of the remainder on shoes. She had $27 left. How much money did she have at first?',36,700))
body+=pin(128,400,1664,A,None,WHITE,24,'18px 30px')
body+=step(1,'Money = 5 parts. The bag is 2 parts. The remainder is 3 parts.',top=560,size=34)
body+=pin(128,400,1664,B,'fade',WHITE,24,'18px 30px')
body+=pin(1330,420,440,p('Half of 3 parts is awkward: cut every part in 2.',30,700,TEAL),'fade')
body+=step(2,'Cut every part in 2: 10 equal units. Bag 4, shoes 3 (half of the remainder), left 3.',top=665,size=34)
body+=step(3,'3 units = $27, so 1 unit = $9 and 10 units = $90.   Check: 36 + 27 + 27 = 90 ✓',top=770,size=34)
put('teach1',sec(f'{L}-teach1','21–24 MIN',body,'Teach. Read the problem twice. Ask: "Is the 1/2 half of her money or half of what is left?" Click order: step 1, the cut bar, steps 2 and 3. Think-aloud: "2/5 on the bag means I draw 5 parts and shade 2. That leaves 3 parts. Half of the REMAINDER is half of 3 parts, and I cannot halve 3 parts neatly, so I cut every part into 2 pieces. Now every unit is the same size. The bag is 4 units, the remainder is 6 units, shoes are 3 units, and 3 units are left." Then: "3 units are $27 so one unit is $9; the whole bar is 10 units, $90." Check by going forwards: bag 2/5 of 90 = 36; remainder 54; shoes 27; left 27. Common error: taking 1/2 of the WHOLE for the shoes.'))
put('try1',try_slide(f'{L}-try1','24–26 MIN','Your turn: fraction of the remainder','Draw a bar. Cut the parts into equal units.',[
 ('a','Ben spent 1/2 of his money on a game and 1/4 of the remainder on lunch. He had $18 left. How much at first?','$48'),
 ('b','Mei read 3/10 of a book on Saturday and 2/7 of the remaining pages on Sunday. 25 pages were left. How many pages in the book?','50 pages'),
 ],
 'Whiteboards. a) Game 1/2 (4 of 8 units); remainder 4 units; lunch 1/4 of 4 units = 1 unit; left 3 units = $18, 1 unit = $6, 8 units = $48. Check: game $24, remainder $24, lunch $6, left $18. b) 10 units: Saturday 3; remainder 7; Sunday 2/7 of 7 = 2; left 5 units = 25 pages; 1 unit = 5; book 50 pages. Check: 15 read, 35 left, 10 read Sunday, 25 left. (Two items only.)',size=33))

# ---- 6. teach 2: the total stays the same ----
sc=11
A=svgwrap(1250,180,'Before: Ali and Ben share 96 cards in an unknown split. After: Ali has 1 unit and Ben has 3 units.',
  txt(120,56,'Before',32,NAVY,'end',700,'Nunito Sans, Arial')+pbar(140,14,sc,[(96,WHITE,'Ali ? + Ben ? = 96',1)])+
  txt(120,140,'After',32,NAVY,'end',700,'Nunito Sans, Arial')+pbar(140,98,sc,[(24,YEL,'Ali',1),(72,SKY,'Ben',3)]))
B=svgwrap(1250,180,'Before: Ali 38 and Ben 58. After: Ali 24 and Ben 72. Both bars are 96 long.',
  txt(120,56,'Before',32,NAVY,'end',700,'Nunito Sans, Arial')+pbar(140,14,sc,[(38,YEL,'Ali 38',1),(58,SKY,'Ben 58',1)])+
  txt(120,140,'After',32,NAVY,'end',700,'Nunito Sans, Arial')+pbar(140,98,sc,[(24,YEL,'Ali 24',1),(72,SKY,'Ben 72',3)]))
body=h2('Worked example: the total stays the same',64)+card(p('Ali and Ben had 96 cards altogether. Ali gave Ben 14 cards. Then Ali had 1/3 as many cards as Ben. How many cards did Ali have at first?',36,700))
body+=pin(128,400,1664,A,None,WHITE,24,'16px 30px')
body+=step(1,'Giving cards does not change the total: 96 before and 96 after.',top=640,size=34)
body+=step(2,'After: Ali 1 unit, Ben 3 units. 4 units = 96, so 1 unit = 24.',top=730,size=34)
body+=pin(128,400,1664,B,'fade',WHITE,24,'16px 30px')
body+=step(3,'Ali has 24 after. He gave away 14, so he had 24 + 14 = 38 at first.   Check: Ben 58 + 14 = 72 = 3 × 24 ✓',top=820,size=34)
put('teach2',sec(f'{L}-teach2','26–30 MIN',body,'Teach. Ask first: "Did the total change when Ali gave Ben some cards?" Draw the AFTER model first: it is the part with the fraction. Click order: step 1, step 2, then the bars fill in with the numbers, then step 3. Think-aloud: "Ali has 1/3 as many as Ben, so Ali is 1 unit and Ben is 3 units. The total is 4 units and that is 96, so a unit is 24. Ali has 24 AFTER giving away 14. To go back to BEFORE I add the 14 back: 38." Stress going backwards from after to before. Check: before 38 + 58 = 96.'))
put('try2',try_slide(f'{L}-try2','30–32 MIN','Your turn: the total stays the same','Draw the After model first.',[
 ('a','Ali has 45 stickers and Mei has 15. How many must Ali give Mei so that they have the same number?','15'),
 ('b','Ben and Ali have 72 marbles. Ben gives Ali 6, and then Ben has 1/2 as many as Ali. How many did Ben have at first?','30'),
 ],
 'Whiteboards. a) The total is 60, so 30 each; Ali gives 45 − 30 = 15 (check: 30 and 30). b) After: Ben 1 unit, Ali 2 units, 3 units = 72, 1 unit = 24, so Ben has 24 after and had 24 + 6 = 30 at first. (Two items only.)',size=33))

# ---- key idea ----
body=h2('Key idea: find what stays the same')+card(p('Ask: what stays the same? The total (one gives to the other), the difference (both get or spend the same), or one amount (only the other changes).',40,700))+card(p('Draw that part the same in the Before and After models. Fraction of a remainder: cut the parts that are left into equal units.',36,600,MUTED))
put('key',sec(f'{L}-key','32–33 MIN',body,'Say the key idea together. Common mistakes to watch for during the worksheet: (1) '+LS['mistakes'][0]+' (2) '+LS['mistakes'][1]+' (3) '+LS['mistakes'][2]))
put('break',break_slide(f'{L}-break','33–37 MIN',DK['brk'],'Five minutes. Online: children stand in view of the camera. Ask for 1/2 of the whole with arms (one arm up), 1/4, then 3/4. Ask: "What is 1/2 of 1/2?" and have them show it with their arms (1/4). Then a drink of water.'))

# ---- worksheet 1 ----
put('ws1',ws_preview(f'{L}-ws1','37–49 MIN','Worksheet page 1: with your partner',[('Q1','Fraction of a remainder. Cut the parts into equal units.'),('Q2','Siti and Mei: giving stickers. What stays the same? Tip: try 3 and 4, 6 and 8, 9 and 12 …'),],'Stuck? Draw the bar first and label every part before you use a number.','Minutes 37 to 49. Walk around. Ask "What stays the same in this story?" before giving any help. Q1 uses the remainder idea from the worked example, Q2 the "total stays the same" idea. Page 1 has only Q1 and Q2 (Q3, the marbles, is on page 2 and is take-home).'))
put('ws1ans',checks(f'{L}-ws1ans','49–51 MIN','Page 1: check together',[('Q1','a) 1/6   b) $72   c) $12 more (book $24, pen $12)'),('Q2','a) 84   b) Siti 48, Mei 36')],
 'Click each answer after a pair explains theirs. Q1: pen = 1/4 of 2/3 = 1/6; 6 units, 3 units left = $36, 1 unit = $12; total $72; book 2 units = $24, pen 1 unit = $12. Q2b: after, Siti 3 units and Mei 4 units = 84, 1 unit = 12; Siti 36 after, so 36 + 12 = 48 at first; Mei 84 − 48 = 36. Q3a: Ali has 20 more; if he gives 10, Ali 40 and Ben 40; if he gave 20, Ali 30 and Ben 50, the gap flips. Q3b: total 80, 8 units, 1 unit = 10, Ali 30 and Ben 50 after giving 20.',gapy=170))

# ---- teach: difference stays the same ----
sc=25
A=svgwrap(1250,190,'Now: Mei is 8 and her mother is 36. The difference is 28.',txt(120,56,'Mei',34,NAVY,'end',700,'Nunito Sans, Arial')+pbar(140,14,sc,[(8,YEL,'8',1)])+txt(120,150,'Mum',34,NAVY,'end',700,'Nunito Sans, Arial')+pbar(140,108,sc,[(8,SKY,'8',1),(28,GRN,'28 more',1)])+'')
B=svgwrap(1250,190,'Later: Mei is 1 unit and her mother is 3 units. The difference is 2 units.',txt(120,56,'Mei',34,NAVY,'end',700,'Nunito Sans, Arial')+pbar(140,14,sc*14,[(1,YEL,'1 unit',1)])+txt(120,150,'Mum',34,NAVY,'end',700,'Nunito Sans, Arial')+pbar(140,108,sc*14,[(1,SKY,'1 unit',1),(2,GRN,'2 units = 28',2)]).replace(f'width="{sc*14*3}"','')+'')
body=h2('Worked example: the difference stays the same',60)+card(p('Mei is 8 and her mother is 36. In how many years will Mei be 1/3 as old as her mother?',36,700))
body+=pin(128,380,1664,A,None,WHITE,24,'16px 30px')
body+=step(1,'Both get older by the same number of years, so the difference stays the same: 36 − 8 = 28.',top=620,size=33)
body+=pin(128,380,1664,B,'fade',WHITE,24,'16px 30px')
body+=step(2,'Later: Mei 1 unit, Mum 3 units. The difference is 2 units = 28, so 1 unit = 14.',top=715,size=33)
body+=step(3,'Mei will be 14, so 14 − 8 = 6 years later.   Check: 14 and 42, and 14 is 1/3 of 42 ✓',top=810,size=33)
put('teachdiff',sec(f'{L}-teachdiff','51–54 MIN',body,'Teach before worksheet page 2 (Q4: both get the same amount of money). Ask first: "Everyone gets one year older every year. Does the gap between Mei and her mother change?" No. Click: step 1, then the later model, then steps 2 and 3. Think-aloud: "The gap is 28 now and it will be 28 later. Later, Mei is 1 unit and Mum is 3 units, so the gap is 2 units. 2 units are 28, so 1 unit is 14. Mei is 14 later; she is 8 now; 6 years." Link to the worksheet: "Giving each person the same money is just like each person getting one year older: the difference stays the same." Do the same story with money: both get $5 more, the gap is unchanged.'))
# ---- teach: one amount stays the same ----
A=svgwrap(1250,190,'Before: girls are 2 units and boys are 3 units.',txt(120,56,'Girls',34,NAVY,'end',700,'Nunito Sans, Arial')+pbar(140,14,150,[(2,YEL,'girls',2)])+txt(120,150,'Boys',34,NAVY,'end',700,'Nunito Sans, Arial')+pbar(140,108,150,[(3,SKY,'boys',3)]))
B=svgwrap(1250,190,'After: 4 more girls join and the girls bar is as long as the boys bar. The 4 new girls are 1 unit.',txt(120,56,'Girls',34,NAVY,'end',700,'Nunito Sans, Arial')+pbar(140,14,150,[(2,YEL,'girls',2),(1,ORG,'+4',1)])+txt(120,150,'Boys',34,NAVY,'end',700,'Nunito Sans, Arial')+pbar(140,108,150,[(3,SKY,'boys: no change',3)]))
body=h2('Worked example: one amount stays the same',60)+card(p('2/5 of the pupils in a class are girls. After 4 more girls join, half of the class are girls. How many pupils were in the class at first?',36,700))
body+=pin(128,400,1664,A,None,WHITE,24,'16px 30px')
body+=step(1,'The boys did not change: 3 units before and 3 units after.',top=640,size=33)
body+=pin(128,400,1664,B,'fade',WHITE,24,'16px 30px')
body+=step(2,'After, half are girls, so girls = boys = 3 units. The girls grew by 1 unit: that is the 4 new girls.',top=730,size=33)
body+=step(3,'1 unit = 4, so at first 5 units = 20 pupils.   Check: 8 girls, 12 boys; 12 and 12 later ✓',top=820,size=33)
# ---- worksheet 2 ----
put('ws2',ws_preview(f'{L}-ws2','57–72 MIN','Worksheet page 2: on your own',[('Q4','Ravi and Ali. Both are given the same amount. The difference stays the same.'),('Q3','★ Take-home: Ali and Ben\'s marbles. Is Ben right?'),('Q5','★ Take-home: a jar of 12 red and 8 blue beads, then 10 more red.')],'Want more? Think harder and Go further are at the back of your workbook.','Children work alone on Q4 only; Q3 and Q5 are take-home (starred). Note who needs a short catch-up next lesson, especially children who keep the total the same when the stay-the-same amount is the difference.'))
put('ws2ans',checks(f'{L}-ws2ans','72–76 MIN','Page 2: check together',[('Q4','a) The difference: $24   b) $22 each'),('Q3','a) No: 10 each way, 40 and 40.'),('Q5','a) Blue   b) 2/5 blue at first (8 of 20); now 30 beads and 4/15 are blue   c) the blue beads are still 8, but the jar has more beads')],
 'One child explains Q4; click through the rest (Q3 and Q5 are take-home, their answers are here for you). Click each answer after a child explains. Q4: the difference $50 − $26 = $24 stays $24; after, Ali 2 units and Ravi 3 units, so 1 unit = $24, Ali has $48 after, so the mother gave $48 − $26 = $22 (check: $72 and $48; 48 is 2/3 of 72). Q5: 12 red and 8 blue, 20 beads. 10 red are added, so the jar has 30 beads. Blue is 8 of 20 = 2/5 at first and 8 of 30 = 4/15 now. Only red was added, so blue is the part that does not change; the blue fraction gets smaller because the whole gets bigger. The full problem (3/7 red, then 30 red added, 3/5 red) is Think harder A2: blue 4 units at first and 2 parts of 5 after, so the whole box is 10 units; red 3 units then 6 units, so 30 = 3 units, 1 unit = 10, 70 beads at first and 100 now.',gapy=170))

# ---- stretch, challenge ----
import p5_printed as _PP
for _k,_v in _PP.slides(3,'A').items(): S[f'p5l3-{_k}']=_v
ch=[('E1.', 'Ali and Ben had $90 altogether. Ali spent 1/3 of his money and Ben spent $10. Then they had the same amount of money. How much did Ali have at first?'), ('E2.', 'Mei is 1/4 as old as her father. In 12 years she will be 1/2 as old as her father. How old is Mei now?')]
for _k,_v in _PP.slides(3,'B').items(): S[f'p5l3-{_k}']=_v
put('challenge',sec(f'{L}-challenge','Optional, if you finish early',h2('More Go further puzzles (extra, not in your workbook)')+numcards(ch,36),'Pairs try first, then use the "see it" slide if stuck, then the walk-through. These are NOT on the workbook. Answers: 1) $48 (Ali has 3 units and keeps 2 after spending 1 unit; Ben has $90 − 3 units, and after spending $10 he has $80 − 3 units, which equals the 2 units Ali keeps; so 5 units = $80, 1 unit = $16; Ali $48, Ben $42; both have $32 left). 2) 6 years old (the difference is 3 units now and 1 unit in 12 years, so 3 old units = 1 new unit; Mei now 1 unit = 6, father 24; in 12 years 18 and 36).'))
# chdiag
g1=txt(110,70,'Ali',32,NAVY,'end',700,'Nunito Sans, Arial')+pbar(130,36,150,[(2,YEL,'',2),(1,RED,'spent',1)])+txt(110,190,'Ben',32,NAVY,'end',700,'Nunito Sans, Arial')+pbar(130,156,150,[(2.3,SKY,'',1),(0.7,RED,'$10',1)])
g1+=txt(130,270,'Ali + Ben = $90.',30,TEAL,'start',800,'Nunito Sans, Arial')+txt(130,310,'After spending, they have the same.',30,TEAL,'start',800,'Nunito Sans, Arial')
g2=txt(210,64,'Now',30,TEAL,'end',800,'Nunito Sans, Arial')+txt(210,110,'Mei',30,NAVY,'end',700,'Nunito Sans, Arial')+pbar(230,76,120,[(1,YEL,'',1)],h=50)+txt(210,176,'Dad',30,NAVY,'end',700,'Nunito Sans, Arial')+pbar(230,142,120,[(4,SKY,'',4)],h=50)
g2+=txt(210,246,'In 12 years',30,TEAL,'end',800,'Nunito Sans, Arial')+txt(210,290,'Mei',30,NAVY,'end',700,'Nunito Sans, Arial')+pbar(230,256,120,[(1,YEL,'',1),(0.5,RED,'+12',1)],h=50)+txt(210,356,'Dad',30,NAVY,'end',700,'Nunito Sans, Arial')+pbar(230,322,120,[(4,SKY,'',4),(0.5,RED,'+12',1)],h=50)
g2+=txt(230,420,'Mei is half of Dad in 12 years.',28,TEAL,'start',800,'Nunito Sans, Arial')
body=h2('Go further: see it',60)+'<div style="display:flex;gap:32px;align-items:flex-start">'
body+=card(f'<p style="font-size:30px;font-weight:700;color:{TEAL}">E1: Spending, then equal</p>'+svgwrap(780,330,'Ali has 3 equal units and spends 1; Ben spends 10 dollars; the two have 90 dollars altogether',g1,True),extra='flex:1;min-width:0;padding:20px 24px')
body+=card(f'<p style="font-size:30px;font-weight:700;color:{TEAL}">E2: Ages now and later</p>'+svgwrap(800,440,'Mei is 1 unit and Dad is 4 units now; in 12 years Mei is half of Dad',g2,True),extra='flex:1;min-width:0;padding:20px 24px')+'</div>'
put('chdiag',sec(f'{L}-chdiag','Optional, if you finish early',body,'Show after pairs have tried Go further, or if they are stuck. The pictures show the situation, not the answer. Ask: What stays the same in E1 after Ali and Ben spend? (They end up equal.) In E2, what stays the same? (The difference between the ages.) Which unit is "1 unit" in the later picture? Answers are in the Go further slide notes.'))
body=h2('Go further: walk-through')+pin(128,250,800,p('E1: Ali and Ben, equal after',38,800,TEAL))
rows1=['Ali spends 1/3: he keeps 2 units, spends 1 unit.','Ben also has 2 units left, and spent $10.','Total: 3 units + 2 units + $10 = $90, so 5 units = $80.','1 unit = $16. Ali had 3 units = $48 ✓']
rows2=['The difference is 3 units now.','In 12 years Mei is half of Dad, so Mei = the difference.','So 3 units now = Mei later = 1 unit + 12.','2 units = 12, 1 unit = 6. Mei is 6 ✓ (Dad 24)']
for i,t in enumerate(rows1): body+=pin(128,330+i*120,800,p(t,32),'rise',WHITE)
body+=pin(992,250,800,p('E2: ages and the difference',38,800,TEAL))
for i,t in enumerate(rows2): body+=pin(992,330+i*120,800,p(t,32),'rise',WHITE)
put('chwalk',sec(f'{L}-chwalk','Optional, if you finish early',body,'Use after pairs have tried. E1: both start from different places but end equal, so the SPENT amounts matter: Ali spends 1 unit, Ben spends $10; Ali keeps 2 units and Ben keeps 2 units, so after spending the two have 4 units; the total after is 90 − 1 unit − 10. Check: Ali 48 spends 16 and keeps 32; Ben 42 spends 10 and keeps 32; 48 + 42 = 90 ✓. E2: the difference stays 3 units; in 12 years Mei is half, so the difference equals Mei\'s age then. Check: now 6 and 24 (6 is 1/4 of 24); later 18 and 36 (18 is half of 36) ✓.'))

# ---- talk, exit ----
body=h2('Talk time')+card(chip('TALK TIME',YEL,NAVY)+p(LS['share'],42,600))+card(p('Sentence starters:',34,400,MUTED)+p('“What stays the same is …”   “I know because …”   “One unit is worth …”',38,600))
put('talk',sec(f'{L}-talk','76–82 MIN',body,'Minutes 76 to 82. Pairs talk for 2 minutes, then share. Answer: Yes. If Ali gives Mei 20 marbles, Ali has 30 and Mei has 50: the difference is 20 again, but now Mei has more. The total is 80 the whole time. Ask: "When does the total stay the same? When does the difference stay the same?" (Giving between two people keeps the total. Both getting or spending the same keeps the difference.) Praise the reasons, not only the answers.'))
body=h2('Exit ticket')+card(chip('EXIT TICKET')+p(LS['exit']['q'],44,600))+card(p('Draw a model on a slip of paper. Tick it when your tutor shows the answer. Then collect your stamp in your inquiry journal.',34,400))
put('exit',sec(f'{L}-exit','82–90 MIN',body,'Minutes 82 to 90. Answer: '+LS['exit']['a']+' Extension: '+LS['extension']))

order=[f'{L}-{x}' for x in ['title','warm1','warm2','explore1','explore2','teach1','try1','teach2','try2','key','break','ws1','ws1ans','teachdiff','ws2','ws2ans','stretch','challenge','chdiag','chwalk','talk','exit']]
order=_PP.fix_order(order,3,S)
sections={'s1':{'description':'Warm-up and explore','start':f'{L}-title'},'s2':{'description':'Teach: fraction of a remainder and the total that stays the same','start':f'{L}-teach1'},'s3':{'description':'Worksheet with teaching before each page','start':f'{L}-break'},'s4':{'description':'Think harder, Go further, talk and exit','start':f'{L}-stretch'}}
write_deck(L,order,sections,S,'Math Inquirers P5: Lesson 3 – Before and After')

import p5_gaps; p5_gaps.apply(3)
