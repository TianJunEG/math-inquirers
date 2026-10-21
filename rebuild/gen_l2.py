import json,os,sys
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,H)
from slidekit import *
D=os.path.join(H,'..','split','l2','project'); S={}
def put(i,h): S[i]=h
# warm2
qs=[('1.','10 = 7 + __','3'),('2.','10 = 2 + __','8'),('3.','10 = __ + 5','5'),('4.','10 = 10 + __','0'),('5.','10 = __ + 1','9')]
body=h2('Quick questions')+''.join(qrow(128,250+i*125,1250,a,b) for i,(a,b,c) in enumerate(qs))+''.join(answer(1420,250+i*125,372,c) for i,(a,b,c) in enumerate(qs))
put('l2-warm2',sec('l2-warm2','5–10 MIN',body,'Minutes 5 to 10. Read each aloud, give thinking time, take answers, then click to show. For 4 ask: "Can a number bond have 0 in it?" (yes: 10 + 0). Answers: 3, 8, 5, 0, 9.'))
# teach1 list in order
rows=[('0 + 10'),('1 + 9'),('2 + 8'),('3 + 7'),('4 + 6'),('5 + 5')]
body=h2('Bonds of 10: list them in order')+p('Start with 0. Each time, the first number goes up by 1.',36,600,MUTED)
for i,r in enumerate(rows): body+=pin(128+(i%3)*560,300+(i//3)*130,520,p(r,48,700),'rise',WHITE,20,'18px 30px')
body+=pin(128,580,1664,p('The first number goes up by 1, the second goes down by 1. When we reach 5 + 5, the next ones are the same pairs turned round (6 + 4, 7 + 3 …). That is how we know we have them all.',36,700),'fade',SOFT,20,'22px 30px')
put('l2-teach1',sec('l2-teach1','25–27 MIN',body,'Teach. Click to add each bond while children say it with you; show each on a ten-frame (red and yellow counters). Think-aloud: "Let me list them in order: 0 + 10, 1 + 9, 2 + 8. What do you notice? The first number goes up by 1 and the second goes down by 1. That is how I know I have them all." Then the summary: 11 bonds from 0 + 10 to 10 + 0, or 6 different pairs if 3 + 7 and 7 + 3 count as the same.'))
put('l2-try1',try_slide('l2-try1','27–28 MIN','Your turn: whiteboards','Write the missing number.',[('a','10 = 3 + __','7'),('b','10 = __ + 6','4'),('c','Which pair is missing? 0+10, 1+9, 2+8, 4+6, 5+5','3 + 7')],'Whiteboards up together, then click. For c, ask how they found it: "the list goes 2 + 8 then 4 + 6, so 3 + 7 is missing".'))
# teach2 bonds of 20
tb=[('Bond of 10','Bond of 20'),('7 + 3 = 10','17 + 3 = 20'),('8 + 2 = 10','18 + 2 = 20'),('4 + 6 = 10','14 + 6 = 20')]
body=h2('Bonds of 10 help us make 20')
for i,(a,b) in enumerate(tb): body+=trow(128,250+i*95,[a,b],[520,520],None if i==0 else 'rise',header=(i==0),size=38)
body+=pin(1250,250,542,p('What stays the same? What changes?',36,700),None,SOFT,20,'22px 26px')+pin(1250,420,542,p('The ones are the same. One more ten makes 20.',36,700),'fade',WHITE,20,'22px 26px')
body+=step(1,'20 = 13 + ?   Think: 3 + 7 = 10, so 13 + 7 = 20.',top=660,size=36)
put('l2-teach2',sec('l2-teach2','28–30 MIN',body,'Click to build each row. Ask "What stays the same? What changes?" before revealing. Think-aloud: "I know 6 + 4 = 10. So 16 + 4 = 20. The ones stay the same. Only the tens change." Then the worked example at the bottom.'))
put('l2-try2',try_slide('l2-try2','30–31 MIN','Your turn: bonds of 20','Use a bond of 10 to help you.',[('a','20 = 16 + __','4'),('b','20 = __ + 11','9'),('c','15 + __ = 20','5')],'Whiteboards. For b: "1 + 9 = 10, so 11 + 9 = 20."'))
# teach3 equals
body=h2('"=" means "is the same as"')+card(p('6 + 2 = 5 + __',48,700))+pin(128,420,1100,seesaw_svg('6 + 2','5 + ?'),None)+step(1,'Work out the side you know:  6 + 2 = 8',left=1260,top=420,width=532,size=34)+step(2,'The other side must also be 8.',left=1260,top=560,width=532,size=34)+step(3,'5 + 3 = 8, so the missing number is 3. Check: 8 and 8 ✓',left=1260,top=700,width=532,size=34)
put('l2-teach3',sec('l2-teach3','31–33 MIN',body,'Teach. Imagine a see-saw: both sides must balance. Ask first: "What do you think goes in the blank?" Many children say 8 because "the answer comes next". Click through the steps. Think-aloud: "6 + 2 is 8, so the other side must be 8. What goes with 5 to make 8? 3."'))
put('l2-try3',try_slide('l2-try3','33–34 MIN','Your turn: balance it','Both sides must be the same.',[('a','7 + 4 = 9 + __','2'),('b','3 + 8 = __ + 6','5'),('c','True or false: 4 + 4 = 8 + 1','False: 8 and 9')],'Whiteboards. For c, children write T or F and show the two totals.'))
body=h2('Key idea: bonds and equals')+card(p('List bonds in order so none are missed. Bonds of 10 help with bonds of 20.',44,700))+card(p('"=" means both sides have the same value.',38,600,MUTED))
put('l2-key',sec('l2-key','34–35 MIN',body,'Say the key ideas together. Common mistakes to watch for during the worksheet: (1) Reading "=" as "the answer comes next" (5 + 3 = 4 + __ answered 8). (2) Counting 3 + 7 and 7 + 3 as different pairs when asked for different pairs. (3) Magic triangle: trying numbers at random instead of thinking about the corners.'))
put('l2-ws1',ws_preview('l2-ws1','40–55 MIN','Worksheet page 1: with your partner',[('Q1','Bonds of 10. Use a ten-frame if you need it.'),('Q2','List the pairs in order, then explain the pattern.'),('Q3','Use bonds of 10 to make bonds of 20.')],'Stuck? Fill a ten-frame with two colours and count each colour.','Minutes 40 to 55. Walk around. Ask "How do you know?" before giving any help.'))
put('l2-ws1ans',check_slide('l2-ws1ans','55–57 MIN','Page 1: check together',[('Q1','a) 7,   b) 4,   c) 2,   d) 5,   e) 10'),('Q2','2+8, 3+7, 4+6, 5+5.  The second number goes down by 1.  6 different pairs.'),('Q3','a) 20 and 20,   b) 20 and 20,   c) 8, 11, 5')],'Click each answer after a pair explains theirs. Q2c: 0+10, 1+9, 2+8, 3+7, 4+6 and 5+5 are 6 different pairs if turned-round pairs count as the same.'))
# teach magic triangle (sides of 12)
body=h2('Magic triangles: think about the corners')+card(p('Put 1, 2, 3, 4, 5 and 6 in the circles so each side adds up to 12.',40,700))
body+=pin(128,400,520,triangle_svg([None]*6,520,450),None)
body+=step(1,'Each corner is on TWO sides. Big sides need big corners: try 4, 5 and 6.',left=700,top=400,width=1092,size=34)
body+=pin(128,400,520,triangle_svg([4,5,6,None,None,None],520,450),'fade')
body+=step(2,'Side 4 + ? + 5 = 12, so ? = 3.  Side 5 + ? + 6 = 12, so ? = 1.',left=700,top=530,width=1092,size=34)
body+=step(3,'Side 6 + ? + 4 = 12, so ? = 2. Every number used once ✓',left=700,top=660,width=1092,size=34)
body+=pin(128,400,520,triangle_svg([4,5,6,3,1,2],520,450),'fade')
put('l2-teachtri',sec('l2-teachtri','57–59 MIN',body,'Teach before worksheet page 2 (Q5). Here the target is 12, so the BIG numbers go in the corners. On the worksheet the target is 9: ask "Small sides... so which numbers should go in the corners?" but do not tell them. Click order: step 1, corners appear, step 2, step 3, the finished triangle. Check each side aloud: 4 + 3 + 5, 5 + 1 + 6, 6 + 2 + 4.'))
# teach two numbers
body=h2('Two numbers: total and difference')+card(p('Two numbers add up to 8. One is 2 more than the other. What are they?',40,700))
body+=pin(128,400,1664,cubes_svg([(6,SKY,'6 cubes'),(2,YEL,'the extra 2')]),'rise')
body+=step(1,'Take away the extra 2. 6 cubes are left.',top=540,size=34)
body+=step(2,'Share the 6 equally: 3 and 3.',top=650,size=34)
body+=step(3,'Give the extra 2 back to one side: 3 and 5. Check: 3 + 5 = 8, and 5 is 2 more than 3 ✓',top=760,size=34)
put('l2-teachtwo',sec('l2-teachtwo','59–60 MIN',body,'Teach before worksheet page 2 (Q6). Use real cubes. Take 2 cubes away and put them aside, share the rest into two equal towers, then add the 2 to one tower. Children who guess-and-check are fine too: ask them to check both clues.'))
put('l2-ws2',ws_preview('l2-ws2','60–66 MIN','Worksheet page 2: on your own',[('Q4','The equals sign. Work out the side you know first.'),('Q5','Magic triangle. Think about which numbers go in the corners.'),('Q6','Two numbers. Use cubes: take away the extra, share, give it back.')],'Finished early? Stretch and Challenge come next.','Children work alone. Note who needs a short catch-up next lesson.'))
put('l2-ws2ans',check_slide('l2-ws2ans','66–68 MIN','Page 2: check together',[('Q4','a) 4,  b) 4,  c) 6,  d) 2,  e) No: 4 + 4 is 8 but 8 + 1 is 9'),('Q5','Sides of 9: corners 1, 2, 3 with 6, 4, 5 between.  Sides of 10: corners 1, 3, 5'),('Q6','4 and 6.   Challenge: 4 and 8')],'Click each answer after a child explains. Q5: small sides need small corners, so 1, 2, 3 go in the corners for 9. Between 1 and 2: 6; between 2 and 3: 4; between 3 and 1: 5. For 10 the corners are 1, 3, 5 with 6, 2, 4 between.'))
# stretch new
st=[('1.','13 + 7 = 10 + __ = 4 + __'),('2.','□ + □ + 4 = 20, and both boxes are the same number. What is in the box?'),('3.','How many pairs make 20 if both numbers are from 5 to 15? (7 + 13 and 13 + 7 count once.)')]
put('l2-stretch',sec('l2-stretch','For early finishers',h2('Stretch')+''.join(card(p(f'<span style="color:#1F7A6F">{a}</span>  {E(b)}',38,600,raw=True)) for a,b in st),'Answers: 1) 10 and 16 (all three are 20). 2) 8 (20 − 4 = 16, and 8 + 8 = 16). 3) 6 pairs: 5+15, 6+14, 7+13, 8+12, 9+11, 10+10.'))
# challenge walk-through
body=h2('Challenge: walk-through')+pin(128,250,760,p('Q1: sides of 11',40,800,TEAL))+pin(128,330,760,p('Try the even numbers 2, 4, 6 in the corners.',34),'rise',WHITE)+pin(128,450,760,p('2 + 5 + 4 = 11,  4 + 1 + 6 = 11,  6 + 3 + 2 = 11 ✓',34),'rise',WHITE)
body+=pin(960,250,832,p('Q2: stickers',40,800,TEAL))+pin(960,330,832,p('Ali keeps 9, so 20 − 9 = 11 are shared.',34),'rise',WHITE)+pin(960,450,832,p('Take away Ben\'s extra 3: 8 left. Share: 4 and 4.',34),'rise',WHITE)+pin(960,570,832,p('Mei 4, Ben 4 + 3 = 7. Check: 4 + 7 = 11 ✓',34),'rise',WHITE)
put('l2-chwalk',sec('l2-chwalk','Challenge',body,'Use after pairs have tried. Q1: if children ask why even numbers, say "we tried big corners for 12 and small corners for 9; 11 is in between, so try a mix". Q2 uses the same take-away-the-extra idea as Q6.'))
for i,h in S.items(): open(os.path.join(D,'slides',i+'.html'),'w').write(h)
for old in ['l2-mini1','l2-mini2']:
    f=os.path.join(D,'slides',old+'.html')
    if os.path.exists(f): os.remove(f)
t=os.path.join(D,'slides','l2-title.html'); s=open(t).read(); s=s.replace('mini-lesson 25 to 35, brain break 35 to 40, worksheet 40 to 70','teaching 25 to 35 (click to reveal each step and answer), brain break 35 to 40, worksheet 40 to 70 with short teaching before each page and a check-together slide after it'); open(t,'w').write(s)
deck=json.load(open(os.path.join(D,'deck.json')))
deck['order']=['l2-title','l2-warm1','l2-warm2','l2-explore1','l2-explore2','l2-teach1','l2-try1','l2-teach2','l2-try2','l2-teach3','l2-try3','l2-key','l2-break','l2-ws1','l2-ws1ans','l2-teachtri','l2-teachtwo','l2-ws2','l2-ws2ans','l2-stretch','l2-challenge','l2-chdiag','l2-chwalk','l2-talk','l2-exit']
deck['sections']={'s1':{'description':'Warm-up and explore','start':'l2-title'},'s2':{'description':'Teach: bonds of 10 and 20, and the equals sign','start':'l2-teach1'},'s3':{'description':'Worksheet with teaching before each page','start':'l2-break'},'s4':{'description':'Stretch, challenge, talk and exit','start':'l2-stretch'}}
json.dump(deck,open(os.path.join(D,'deck.json'),'w'),indent=1,ensure_ascii=False)
print(len(deck['order']),'slides')
