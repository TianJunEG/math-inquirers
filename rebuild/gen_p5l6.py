"""Math Inquirers P5, Lesson 6: Rate Racers. Writes split/p5l6/project (deck.json + slides/*.html)."""
import os,sys
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,H)
from p5l56_common import *
P='p5l6'
D=os.path.join(H,'..','split',P,'project'); S={}
def put(i,h): S[f'{P}-{i}']=h
def sid(i): return f'{P}-{i}'

# ---------- 1. title ----------
put('title',title_slide(sid('title'),'LESSON 6  •  WEEK 3','Rate Racers','Rate',
 'Find the rate for 1, compare better buys, add rates when taps and printers work together, and work out charges and price plans.',
 'Objective: Find a rate for 1 unit and use it to scale up or work backwards in a rate table; compare buys by the price of one item (including a free-gift deal); add rates when taps or printers work together and take away a leak; work out charges "for every half hour or part of it"; and compare two price plans with a table. '
 'Thinking strategies taught today: FIND THE VALUE OF 1, MAKE A TABLE and PRETEND A NUMBER (taps that fill a tank in a stated time). '
 'Materials: mini whiteboards, a calculator for checking only, a stopwatch or phone, a few real price tags or supermarket flyers if you have them. '
 'Online: children hold whiteboards up to the camera; the tutor fills the rate tables on the slides. Pairs work in breakout rooms for the Explore. The brain break uses a phone stopwatch. '
 'Time plan: warm-up 0 to 10, explore 10 to 25, teaching 25 to 35 (click to reveal each step and answer), brain break 35 to 40, worksheet 40 to 70 with short teaching before each page and a check-together slide after it, stretch and challenge for early finishers from 65, talk time 70 to 80, exit ticket 80 to 90.'))

# ---------- 2. warm-up: Better Buy Showdown ----------
rows=[('Pens','3 for $2.40','5 for $3.80','80¢ each  vs  76¢ each:  the 5-pack'),('Juice','1.5 ℓ for $3.00','2 ℓ for $3.80','$2.00 a litre  vs  $1.90 a litre:  the 2 ℓ'),('Eggs','10 for $3.20','12 for $3.96','32¢ each  vs  33¢ each:  the 10-pack')]
body=h2('Warm-up: Better Buy Showdown')+p('Two packs of the same thing. Point to the better buy, then prove it with the price of 1.',34,600,MUTED)
for i,(n,a,b,pr) in enumerate(rows):
    T=290+i*210
    body+=pin(128,T,300,p(n,44,800,TEAL),None,WHITE,20,'30px 28px','box-sizing:border-box;height:120px;justify-content:center')
    body+=pin(450,T,450,p(a,40,700),None,WHITE,20,'30px 28px','box-sizing:border-box;height:120px;justify-content:center;border:4px solid '+NAVY)
    body+=pin(920,T,450,p(b,40,700),None,WHITE,20,'30px 28px','box-sizing:border-box;height:120px;justify-content:center;border:4px solid '+NAVY)
    body+=pin(450,T+130,1342,p(pr,34,800),'pop',YEL,16,'8px 24px')
put('warm1',sec(sid('warm1'),'0–5 MIN',body,'Minutes 0 to 5. Better Buy Showdown. Show one row at a time. Children point left or right (online: hold up a left or right hand), then you click to show the proof. Pens: 3 for $2.40 is 80 cents each; 5 for $3.80 is 76 cents each, so the 5-pack. Juice: $3.00 / 1.5 = $2.00 a litre; $3.80 / 2 = $1.90 a litre, so the 2 litre bottle. Eggs: $3.20 / 10 = 32 cents each; $3.96 / 12 = 33 cents each, so the 10-pack (the bigger pack is NOT cheaper per egg). Ask: "Why is it fair to compare the price of ONE?" Watch for children who compare the pack prices ($2.40 and $3.80). Do not say "the bigger pack is always better": the eggs show it is not.'))

# ---------- 3. quick questions ----------
qs=[('1.','4 kg of rice cost $10. Price of 1 kg?','$2.50'),('2.','A printer prints 30 pages a minute. Pages in 6 minutes?','180 pages'),('3.','A tap lets out 450 ml in 3 minutes. ml a minute?','150 ml'),('4.','Cheese costs $1.20 for 100 g. Price of 1 kg?','$12'),('5.','Ali types 40 words a minute. Time for 200 words?','5 minutes')]
body=h2('Quick questions')+''.join(qrow(128,250+i*125,1250,a,b) for i,(a,b,c) in enumerate(qs))+''.join(answer(1420,250+i*125,372,c) for i,(a,b,c) in enumerate(qs))
put('warm2',sec(sid('warm2'),'5–10 MIN',body,'Minutes 5 to 10. Read each aloud, whiteboards up together, then click to show. Answers: $2.50, 180 pages, 150 ml, $12, 5 minutes. After 2 ask: "Which operation scales up?" (multiply). After 5 ask: "Which operation finds how long?" (divide: how many 40s are in 200). After 4 ask: "How many 100 g are in 1 kg?" (10, so multiply the price by 10).'))

# ---------- 4. explore ----------
def printer(x,lab,sub):
    return (f'<rect x="{x}" y="60" width="200" height="90" rx="14" fill="{SKY}" stroke="{NAVY}" stroke-width="4"/><rect x="{x+30}" y="20" width="140" height="46" fill="{WHITE}" stroke="{NAVY}" stroke-width="3"/>'
            f'<line x1="{x+45}" y1="34" x2="{x+155}" y2="34" stroke="{NAVY}" stroke-width="2"/><line x1="{x+45}" y1="48" x2="{x+130}" y2="48" stroke="{NAVY}" stroke-width="2"/>'
            f'<rect x="{x+40}" y="130" width="120" height="50" fill="{WHITE}" stroke="{NAVY}" stroke-width="3"/>'+txt(x+100,112,lab,36)+tb(x+100,214,sub,28,TEAL))
g=printer(60,'A','72 pages in 4 min')+printer(420,'B','50 pages in 2 min')+f'<rect x="760" y="30" width="520" height="170" rx="18" fill="{SOFT}" stroke="{NAVY}" stroke-width="4"/>'+txt(1020,100,'Which is faster?',40)+txt(1020,160,'Both together: 430 pages?',34,TEAL)
steps=''.join(f'<li>{E(s)}</li>' for s in ['Printer A prints 72 pages in 4 minutes. Printer B prints 50 pages in 2 minutes.','Make a rate table for each printer: 1, 2, 4 and 10 minutes.','Which printer is faster? Show how you know.','Predict, then work out: how long do both together take for 430 pages?'])
body=h2('Explore: printer race')+card(chip('EXPLORE')+f'<ol style="font-size:36px;font-weight:600;padding-left:52px;display:flex;flex-direction:column;gap:8px">{steps}</ol>')
body+=card(svgwrap(1340,230,'Printer A, 72 pages in 4 minutes, and printer B, 50 pages in 2 minutes',g),extra='padding:12px 32px')
put('explore1',sec(sid('explore1'),'10–15 MIN',body,'Minutes 10 to 15. Pairs build a rate table for each printer. Ask them to predict first: which is faster, and how long for the 430-page job together? Many say A, because 72 is more than 50. Let them test it: in 4 minutes A prints 72 pages but B prints 100. Hint: how many pages in 1 minute? Early finishers: how many pages should go to each printer so both finish at the same time? (A 180, B 250: 10 minutes each.)'))
body=h2('Explore: talk about it')+numcards([('1.','Which printer is faster? How do you know?'),('2.','How long do both together take for 430 pages? How did you work it out?'),('3.','Why is the rate for 1 minute so useful?')],40)
put('explore2',sec(sid('explore2'),'15–25 MIN',body,'Minutes 15 to 25. Let pairs keep working, then gather them. Answers: 1) B is faster: 25 pages a minute against 18 pages a minute for A (or compare 4 minutes: A 72, B 100). 2) Together 18 + 25 = 43 pages a minute, and 430 / 43 = 10 minutes. Children who guessed "add the times" (4 + 2 = 6) or "half of the average" will need the teaching slides. 3) With the rate for 1 minute we can compare fairly, multiply to scale up and divide to find a time. Do not give the method if nobody finds it: the later slides teach it.'))

# ---------- 5. teach: rate for 1 ----------
W5=[200,170,170,170,200]
body=h2('A rate tells us how much for 1')+card(p('5 kg of rice cost $9.50. How much do 3 kg cost? How many kg can you buy for $13.30?',38,700))
body+=trow(128,430,['kg','5','1','3','?'],W5,None,True,36)+trow(128,520,['price','$9.50','?','?','$13.30'],W5,None,False,36)
body+=step(1,'Find the price of 1 kg first:  $9.50 ÷ 5 = $1.90',left=128,top=650,width=1000,size=34)
body+=step(2,'3 kg:  3 × $1.90 = $5.70',left=128,top=770,width=1000,size=34)
body+=pin(1230,430,562,p('Divide to get 1.  Multiply to scale up.  Divide again to find how many.',34,700),'fade',SOFT,20,'22px 26px')
body+=step(3,'Backwards:  $13.30 ÷ $1.90 = 7 kg',left=1230,top=650,width=562,size=34)
put('teach1',sec(sid('teach1'),'25–27 MIN',body,'Teach. Fill the table with the children. Ask first: "What do we need to know to get 3 kg?" (the price of 1 kg). Click step 1: 9.50 / 5 = 1.90. Click step 2: 3 x 1.90 = 5.70. Check another way: 3 kg is 3/5 of 5 kg, 3/5 of 9.50 is 5.70. Click step 3: 13.30 / 1.90 = 7 (think: 1.90 x 7 = 13.30). Think-aloud: "A rate is how much for ONE. Once I know the rate for one, everything else is multiply or divide." Use a real price tag if you have one. The rate for 1 minute, 1 kg, 1 can are all the same idea.'))

# ---------- 6. worked example: better buy ----------
W3=[220,230,230]
body=h2('Worked example: the better buy')+card(p('Shop A sells 3 pens for $1.95. Shop B sells 5 pens for $3.10. Which is the better buy?',38,700))
body+=trow(128,430,['Pack','3 pens','5 pens'],W3,None,True,36)+trow(128,520,['Price','$1.95','$3.10'],W3,None,False,36)+trow(128,610,['1 pen','65¢','62¢'],W3,'rise',False,36)
body+=step(1,'Find the price of 1 pen:  $1.95 ÷ 3 = 65¢     $3.10 ÷ 5 = 62¢',left=128,top=730,width=1664,size=34)
body+=step(2,'62¢ is less than 65¢, so the 5-pack is the better buy.  Check: 15 pens cost $9.75 or $9.30 ✓',left=128,top=850,width=1664,size=34)
body+=pin(1000,430,792,p('But if Mei needs only 3 pens, the 3-pack costs less ($1.95 against $3.10). The better buy depends on how many you need.',34,700),'fade',SOFT,20,'22px 28px')
put('we1',sec(sid('we1'),'27–29 MIN',body,'Click to reveal the price of 1 pen, then the steps. Think-aloud: "To compare fairly I need the same unit: the price of ONE pen. 195 cents divided by 3 is 65. 310 cents divided by 5 is 62. 62 is smaller, so the 5-pack is cheaper per pen." Check another way: buy 15 pens each way (the common multiple of 3 and 5): 5 packs of 3 cost 5 x 1.95 = 9.75; 3 packs of 5 cost 3 x 3.10 = 9.30. Same answer. Last box: the better buy per pen is not always the one you should buy; you may not need that many.'))
put('try1',try_slide(sid('try1'),'29–30 MIN','Your turn: whiteboards','Find the value of 1 first.',[('a','4 pens cost $3.20. Price of 7 pens?','$5.60'),('b','A machine makes 15 toys a minute. Minutes for 135 toys?','9 minutes'),('c','Better buy: 4 for $2.80 or 6 for $4.50?','4 for $2.80')],'Whiteboards up together, then click. a) $3.20 / 4 = 80 cents each; 7 x 80 = $5.60. b) 135 / 15 = 9. c) 4 for $2.80 is 70 cents each; 6 for $4.50 is 75 cents each, so the smaller pack is cheaper. Ask for c: "Why might a bigger pack still cost more per item?" (not all shops give a discount for a bigger pack).',size=36))

# ---------- 7. teach: free gift ----------
body=h2('Careful: “get 2 free!”')+card(p('Shop A: 8 pencils for $4, and you get 2 more FREE. Shop B: 5 pencils for $2.25. Which is the better buy?',38,700))
body+=step(1,'Shop A gives 8 + 2 = 10 pencils for $4. Count ALL the pencils you receive.',top=430,size=34)
body+=step(2,'Shop A:  $4.00 ÷ 10 = 40¢ each.     Shop B:  $2.25 ÷ 5 = 45¢ each.',top=550,size=34)
body+=answer(128,670,1664,'Shop A is the better buy: 40¢ is less than 45¢.')
body+=pin(128,790,1664,p('Not this one: $4 ÷ 8 = 50¢ each. That forgets the 2 free pencils.',34,700),'fade',SOFT,20,'18px 28px')
put('teachfree',sec(sid('teachfree'),'30–31 MIN',body,'Teach before worksheet page 1 (Q2, shop C has a free-gift deal). Ask first: "Do you pay for the free pencils?" (No, but you get them, so they share the price.) Click through. Think-aloud: "I pay $4 and I walk away with 10 pencils. $4 divided by 10 is 40 cents." The trap: dividing by 8 gives 50 cents and the wrong shop. Check: 20 pencils from shop A cost 2 x $4 = $8; 20 pencils from shop B cost 4 x $2.25 = $9.'))

# ---------- 8. worked example: taps together ----------
W2=[300,420]
body=h2('Worked example: taps working together')+card(p('A tank holds 180 ℓ. Tap A fills 9 ℓ a minute and tap B fills 6 ℓ a minute. How long do both take? Then a crack lets out 3 ℓ a minute: how long now?',34,700))
body+=trow(128,460,['Tap A','+ 9 ℓ a minute'],W2,None,False,34)+trow(128,545,['Tap B','+ 6 ℓ a minute'],W2,'rise',False,34)+trow(128,630,['Together','15 ℓ a minute'],W2,'rise',True,34)+trow(128,715,['Crack','− 3 ℓ a minute'],W2,'rise',False,34)+trow(128,800,['Stays in','12 ℓ a minute'],W2,'rise',True,34)
body+=step(1,'Together the rates ADD:  9 + 6 = 15 ℓ every minute.  180 ÷ 15 = 12 minutes.',left=930,top=460,width=862,size=32)
body+=step(2,'The crack takes its rate AWAY:  15 − 3 = 12 ℓ stay in each minute.',left=930,top=610,width=862,size=32)
body+=step(3,'180 ÷ 12 = 15 minutes.  Check: 15 × 12 = 180 ✓',left=930,top=740,width=862,size=32)
put('we2',sec(sid('we2'),'31–33 MIN',body,'Click to build the table row by row. Think-aloud: "Every minute tap A puts in 9 and tap B puts in 6, so 15 go in every minute. How many 15s make 180? 12 minutes. The crack lets out 3 every minute, so only 12 stay. How many 12s make 180? 15 minutes." Stress: we add RATES (litres a minute), never times. A common mistake is to say "A takes 20 minutes and B takes 30, so together 50". Together must be faster than either tap alone. Ask: "Is 12 minutes sensible? Tap A alone would need 180 / 9 = 20 minutes, so 12 is faster, good."'))
put('try2',try_slide(sid('try2'),'33–34 MIN','Your turn: working together','Add the rates. Take away a leak.',[('a','Taps of 8 ℓ and 12 ℓ a minute fill a 200 ℓ tank. How long?','10 minutes'),('b','Printers of 25 and 15 pages a minute. Time for 480 pages?','12 minutes'),('c','A tap puts in 10 ℓ a minute but a drain lets out 4 ℓ a minute. How long to fill 90 ℓ?','15 minutes')],'Whiteboards. a) 8 + 12 = 20 ℓ a minute; 200 / 20 = 10. b) 25 + 15 = 40 pages a minute; 480 / 40 = 12. c) 10 - 4 = 6 ℓ stay in each minute; 90 / 6 = 15. Ask for c: "What if the drain was 10 ℓ a minute?" (the tank never fills).',size=34))

body=h2('Key idea: find the rate for 1')+card(p('Find how much for 1 unit (1 minute, 1 kg, 1 can). Multiply to scale up. Divide to find how many or how long.',42,700))+card(p('Working together, the rates add. A leak or drain takes its rate away. Compare buys by the price of 1, counting every item you get.',36,600,MUTED))
put('key',sec(sid('key'),'34–35 MIN',body,'Say the key idea together. Common mistakes to watch for during the worksheet: (1) Adding or averaging the times when taps or printers work together (20 minutes and 30 minutes gives 50 or 25) instead of adding the rates. (2) Choosing the better buy by the pack price, or dividing a free-gift deal by the cans paid for instead of all the cans received. (3) Charges "for every half hour or part of it": dividing exactly instead of rounding up to the next half hour, or charging the first hour twice.'))
put('break',break_slide(sid('break'),'35–40 MIN','Rate race! Do star jumps for 10 seconds. How many did you do? Predict your 1-minute total (× 6). Then test it for 30 seconds: does your rate stay the same?','Five minutes. Use a phone stopwatch. Round 1: 10 seconds of star jumps; children count and call the number. Predict 1 minute: multiply by 6. Round 2: 30 seconds; compare with the prediction (x 2 from 30 seconds to a minute). Ask: "Why is the rate usually lower for longer?" (we get tired: a rate stays the same only if the speed stays the same, which machines do and people do not).'))

# ---------- worksheet page 1 ----------
put('ws1',ws_preview(sid('ws1'),'40–52 MIN','Worksheet page 1: with your partner',[('Q1','The bottling machine. Fill the rate table.'),('Q2','Three shops, one can. Price of 1 and the best buy.'),('Q3','Two taps and a crack in the tank.')],'Stuck? Find the amount for 1 minute or for 1 can first.','Minutes 40 to 52. Walk around. Ask "What is the rate for 1?" and "How many cans do you really get in that deal?" before giving any help. Q2c: Ben may buy from more than one shop. Suggest: "Which total number of cans can you make exactly? Try 20 cans using whole packs." Q3d is a trick: with the taps off, the crack only takes water out.'))
put('ws1ans',checks(sid('ws1ans'),'52–54 MIN','Page 1: check together',[('Q1','a) 16, 48, 80, 10 min, 192   b) 9.25 a.m.'),('Q2','a) 70¢, 73¢, 65¢   b) Shop C   c) $13.64'),('Q3','a) 20 min   b) 8 min   c) 10 min   d) 20 min')],
 'Click each answer after a pair explains theirs. Q1: 48 / 3 = 16 bottles a minute; 5 minutes 80; 160 bottles take 10 minutes; 12 minutes 192. Q1b: 400 / 16 = 25 minutes, so 9.25 a.m. Q2a: $4.20 / 6 = 70 cents; $2.92 / 4 = 73 cents; shop C gives 12 cans for $7.80: 65 cents. Q2c: 20 cans exactly: one deal from C (12 cans, $7.80) and two packs from B (8 cans, $5.84) = $13.64. Q3: a) 240 / 12 = 20; b) 240 / 30 = 8; c) 30 - 6 = 24 a minute, 240 / 24 = 10; d) half is 120 litres, 120 / 6 = 20 minutes.',gapy=170))

# ---------- teach before page 2: car park ----------
g=''
x0=70; sc=8.5
def blk(a,b,fill,lab,dash=False):
    d=' stroke-dasharray="10 6"' if dash else ''
    return f'<rect x="{x0+a*sc}" y="60" width="{(b-a)*sc}" height="70" fill="{fill}" stroke="{NAVY}" stroke-width="4"{d}/>'+tb(x0+(a+b)/2*sc,106,lab,32)
g+=blk(0,60,YEL,'first hour: $3')+blk(60,90,SKY,'$1')+blk(90,120,SKY,'$1')+blk(120,150,SKY,'$1')+blk(150,160,'#FFF0C2','',False)+f'<rect x="{x0+150*sc}" y="60" width="{30*sc}" height="70" fill="none" stroke="{NAVY}" stroke-width="4" stroke-dasharray="10 6"/>'+tb(x0+165*sc,106,'$1',32)
g+=tb(x0,50,'1.30 p.m.',26)+tb(x0+160*sc,50,'4.10 p.m.',26)+tb(x0+90*sc,170,'every half hour or PART of one costs $1',28,TEAL)
body=h2('Car park charges: “or part of”')+card(p('First hour $3. After that $1 for every half hour or part of a half hour. How much for 1.30 p.m. to 4.10 p.m.?',36,700))
body+=pin(128,410,1664,svgwrap(1640,190,'A timeline from 1.30 p.m. to 4.10 p.m.: the first hour costs $3, then three full half hours and part of a fourth half hour cost $1 each',g),None,WHITE,20,'8px 8px')
body+=step(1,'Time:  1.30 to 4.10 is 2 h 40 min = 160 minutes.  After the first hour: 100 minutes.',top=640,size=32)
body+=step(2,'100 min = 3 half hours + 10 min.  The 10 min is part of a half hour: it counts as a whole $1.',top=740,size=32)
body+=answer(128,840,1664,'3 + 4 × 1 = $7')
put('teachpark',sec(sid('teachpark'),'54–57 MIN',body,'Teach before worksheet page 2 (Q5). Ask first: "If you stay 10 minutes into a new half hour, do you pay for it?" (Yes: "part of" means we round UP.) Click through. Think-aloud: "The first hour has its own price, so I take it away first. Then I count half hours: 100 minutes is 3 full half hours and 10 minutes left over. The 10 minutes still starts a fourth half hour, so I pay 4 lots of $1." Two traps: charging the first hour twice, and dividing 100 by 30 and writing 3.33 lots. Check with a different time: 1.30 p.m. to 3.45 p.m. is 2 h 15 min; after the first hour 75 min = 2 half hours + 15 min, so 3 lots and $3 + $3 = $6.'))

# ---------- teach before page 2: compare plans ----------
W4=[220,220,220]
body=h2('Comparing two plans: make a table')+card(p('Plan A: $24 to join + $3 a visit. Plan B: $5 a visit, no joining fee. When do they cost the same?',36,700))
body+=trow(128,420,['Visits','Plan A','Plan B'],W4,None,True,36)
for i,(v,a,b) in enumerate([(4,36,20),(8,48,40),(12,60,60),(16,72,80)]): body+=trow(128,510+i*90,[str(v),f'${a}',f'${b}'],W4,'rise',False,36)
body+=pin(900,420,892,p('Plan A: $24 + 4 × $3 = $36.  Plan B: 4 × $5 = $20.',32,700),None,WHITE,20,'18px 26px')
body+=pin(900,560,892,p('Same cost at 12 visits: $60 each.',34,800),'fade',YEL,20,'18px 26px')
body+=pin(900,670,892,p('After that Plan A is cheaper. Why? Plan B costs $2 more for every visit, and that catches up the $24 joining fee: 24 ÷ 2 = 12.',32,700),'fade',SOFT,20,'18px 26px')
put('teachplans',sec(sid('teachplans'),'57–60 MIN',body,'Teach before worksheet page 2 (Q6). Ask first: "Which plan do you think is cheaper?" Take a show of hands, then test with a table. Click the rows. Think-aloud: "For each number of visits I work out both costs. At 4 visits Plan A costs 24 + 12 = 36 and B costs 20. At 12 visits they are both 60. After 12 visits B is dearer." Why 12? Each visit costs Plan B $2 more than Plan A, and Plan A starts $24 higher, so they meet after 24 / 2 = 12 visits. The table tells us WHEN the answer changes: it depends on how many visits you will make. Use a table, not algebra.'))
put('ws2',ws_preview(sid('ws2'),'60–67 MIN','Worksheet page 2: on your own',[('Q4','Two printers: working together, and joining in late.'),('Q5','The car park sign. Count every half hour or part.'),('Q6','Two gyms. Find when they cost the same.')],'Finished early? Stretch and Challenge come next.','Children work alone. Note who needs a short catch-up next lesson, especially children who still add the times for taps or printers.'))
put('ws2ans',checks(sid('ws2ans'),'67–69 MIN','Page 2: check together',[('Q4','a) 18 min   b) 20 min   c) 540 pages to P'),('Q5','a) $4.80   b) 3 hours'),('Q6','a) A $50, $70, $90;  B $35, $70, $105   b) 10 visits   c) A, by $12')],
 'Click each answer after a child explains. Q4a: 30 + 20 = 50 pages a minute; 900 / 50 = 18. Q4b: P alone prints 150 pages in 5 minutes; 750 left; 750 / 50 = 15; 5 + 15 = 20 minutes. Q4c: both finish in 18 minutes; P prints 30 x 18 = 540 and Q prints 20 x 18 = 360. Q5a: 9.40 a.m. to 1.15 p.m. is 3 h 35 min; after the first hour 155 min = 5 half hours + 5 min, so 6 lots: $1.20 + 6 x 60 cents = $4.80. Q5b: $3.60 - $1.20 = $2.40 = 4 half hours after the first hour, so up to 1 h + 2 h = 3 hours. Q6c: 14 visits: A $30 + $56 = $86; B $98.',gapy=170))

# ---------- stretch / challenge ----------
st=[('1.','A bath holds 168 ℓ. The tap fills 12 ℓ a minute. The plug is out and 4 ℓ drain away each minute. How long does the bath take to fill?'),('2.','Cheese costs $2.40 for 200 g at shop X and $5.40 for 500 g at shop Y. Which shop is cheaper per 100 g, and by how much?'),('3.','A taxi costs $4 for the first km and 60¢ for every 500 m or part of 500 m after that. How much does a 3.2 km trip cost?')]
put('stretch',sec(sid('stretch'),'For early finishers',h2('Stretch')+numcards(st,36),'Answers: 1) 21 minutes (12 - 4 = 8 ℓ stay in each minute; 168 / 8 = 21). 2) Shop Y by 12 cents: X costs $1.20 per 100 g and Y costs $5.40 / 5 = $1.08 per 100 g. 3) $7.00 (after the first km: 2.2 km = 2200 m; 2200 / 500 = 4.4, so 5 lots of 60 cents = $3.00; $4 + $3 = $7).'))
ch=[('1.','A machine starts at 9.52 a.m. and makes 50 cups a minute. At 10.00 a.m. a second machine starts, making 30 cups a minute. At what time have they made 1600 cups altogether?'),('2.','A tap fills an empty bath in 12 minutes. With the plug out, a full bath empties in 20 minutes. Ben turns on the tap but forgets the plug. How long does the bath take to fill?')]
put('challenge',sec(sid('challenge'),'65–80 MIN',h2('Challenge')+numcards(ch,36),'Pairs try first, then use the "see it" slide if stuck, then the walk-through. These are in the question bank. Answers: 1) 10.15 a.m. (400 cups by 10.00; then 80 cups a minute; 1200 / 80 = 15 minutes more). 2) 30 minutes (pretend the bath holds 60 litres: 5 litres a minute in, 3 a minute out, 2 a minute stay in: 60 / 2 = 30). Many children say 8 minutes (20 - 12) or 32: pretending a number shows why they are wrong.'))
g1=f'<line x1="40" y1="190" x2="720" y2="190" stroke="{NAVY}" stroke-width="4"/>'
for x,lab in [(40,'9.52'),(200,'10.00')]: g1+=f'<line x1="{x}" y1="180" x2="{x}" y2="200" stroke="{NAVY}" stroke-width="4"/>'+tb(x,230,lab,26)
g1+=tb(720,230,'?',30,TEAL)
g1+=f'<rect x="40" y="60" width="680" height="44" rx="8" fill="{YEL}" stroke="{NAVY}" stroke-width="3"/>'+tb(380,92,'Machine 1: 50 cups a minute',24)
g1+=f'<rect x="200" y="120" width="520" height="44" rx="8" fill="{SKY}" stroke="{NAVY}" stroke-width="3"/>'+tb(460,152,'Machine 2: 30 cups a minute',24)
g1+=tb(380,40,'1600 cups altogether',26,TEAL)
g2=(f'<rect x="150" y="150" width="300" height="130" rx="12" fill="{WHITE}" stroke="{NAVY}" stroke-width="4"/><rect x="154" y="200" width="292" height="76" fill="{SKY}"/>'
    f'<path d="M110 60 H300 V120" fill="none" stroke="{NAVY}" stroke-width="10" stroke-linecap="round"/><line x1="300" y1="126" x2="300" y2="190" stroke="#7FB2DE" stroke-width="6" stroke-dasharray="8 6"/>'
    +tb(120,48,'Tap: fills it in 12 min',24,NAVY,'start')+f'<line x1="300" y1="280" x2="300" y2="330" stroke="{RED}" stroke-width="6" stroke-dasharray="8 6"/>'+tb(300,372,'Plug out: empties it in 20 min',24,RED)+tb(300,250,'bath',28,TEAL))
def dcard(title,svgs): return card(f'<p style="font-size:30px;font-weight:700;color:{TEAL}">{title}</p>'+svgs,extra='flex:1;min-width:0;padding:20px 24px')
body=h2('Challenge: see it',60)+'<div style="display:flex;gap:32px;align-items:flex-start">'
body+=dcard('Q1: Two machines',svgwrap(760,260,'A time line starting at 9.52: machine 1 makes 50 cups a minute from 9.52; machine 2 makes 30 cups a minute from 10.00; 1600 cups altogether',g1,'width:100%;height:auto'))
body+=dcard('Q2: The bath',svgwrap(640,390,'A bath with a tap that fills it in 12 minutes and a plug hole that empties it in 20 minutes',g2,'width:100%;height:auto'))+'</div>'
put('chdiag',sec(sid('chdiag'),'65–80 MIN',body,'Show after pairs have tried the Challenge, or if they are stuck. The pictures show the problem, not the answer. Ask: What do you notice? In Q1, how many cups does machine 1 make before machine 2 starts? Which rate applies after 10.00? In Q2, how much water goes in and how much goes out each minute? Which number could we pretend the bath holds? Answers are in the Challenge slide notes.'))
body=h2('Challenge: walk-through')+pin(128,250,800,p('Q1: two stages',38,800,TEAL))
for i,t in enumerate(['9.52 to 10.00 is 8 min: 8 × 50 = 400 cups','After that: 50 + 30 = 80 cups a minute','Still to make: 1600 − 400 = 1200 cups','1200 ÷ 80 = 15 min after 10.00: 10.15 a.m. ✓']): body+=pin(128,330+i*105,800,p(t,32),'rise',WHITE)
body+=pin(992,250,800,p('Q2: pretend the bath holds 60 ℓ',38,800,TEAL))
for i,t in enumerate(['Tap: 60 ÷ 12 = 5 ℓ in each minute','Plug out: 60 ÷ 20 = 3 ℓ out each minute','5 − 3 = 2 ℓ stay in each minute','60 ÷ 2 = 30 minutes ✓']): body+=pin(992,330+i*105,800,p(t,32),'rise',WHITE)
put('chwalk',sec(sid('chwalk'),'Challenge',body,'Use after pairs have tried. Q1: split into two stages: machine 1 alone for 8 minutes, then both machines. Q2: nobody told us how big the bath is, so we PRETEND: choose a number that both 12 and 20 divide into (60, the smallest, works). The answer does not depend on the pretend number: try 120 litres: 10 in, 6 out, 4 stay, 120 / 4 = 30 minutes again.'))

# ---------- talk / exit ----------
body=h2('Talk time')+card(chip('TALK TIME',YEL,NAVY)+p('Tap A fills a tank in 20 minutes. Tap B fills it in 30 minutes. Ben says together they take 50 minutes. Mei says 25 minutes. Who is right?',40,600))+card(p('Sentence starters:',34,400,MUTED)+p('“I noticed that …”   “I tested it by …”   “I know because …”',38,600))
put('talk',sec(sid('talk'),'70–80 MIN',body,'Minutes 70 to 80. Pairs talk for 2 minutes, then share. Answer: neither. Together the taps must be faster than the faster tap alone (30 minutes is slower than 20), so the answer must be less than 20 minutes. Pretend the tank holds 60 litres (both 20 and 30 go into 60): tap A fills 3 litres a minute and tap B fills 2 litres a minute, together 5 litres a minute, and 60 / 5 = 12 minutes. Second question if time: "Is the biggest pack always the best buy?" (No: the eggs in the warm-up.) Praise the reasons, not only the answers.'))
body=h2('Exit ticket')+card(chip('EXIT TICKET')+p('Tap A fills 15 ℓ a minute and tap B fills 10 ℓ a minute. How long do both taps take to fill a 200 ℓ tank? How long if a crack also lets out 5 ℓ a minute?',40,600))+card(p('Write your answer on a slip of paper. Show it to your tutor. Then collect your stamp in your inquiry journal.',34,400))
put('exit',sec(sid('exit'),'80–90 MIN',body,'Minutes 80 to 90. Answers: 8 minutes (15 + 10 = 25 ℓ a minute; 200 / 25 = 8). With the crack, 10 minutes (25 - 5 = 20 ℓ a minute; 200 / 20 = 10). Extension: make a better-buy poster of three pack sizes where the biggest pack is NOT the best buy. Swap with a partner.'))

order=[sid(x) for x in ['title','warm1','warm2','explore1','explore2','teach1','we1','try1','teachfree','we2','try2','key','break','ws1','ws1ans','teachpark','teachplans','ws2','ws2ans','stretch','challenge','chdiag','chwalk','talk','exit']]
finish(P,S,order,'Math Inquirers P5: Lesson 6 – Rate Racers',{'s1':{'description':'Warm-up and explore','start':sid('title')},'s2':{'description':'Teach: the rate for 1, better buys, taps together','start':sid('teach1')},'s3':{'description':'Worksheet with teaching before each page','start':sid('break')},'s4':{'description':'Stretch, challenge, talk and exit','start':sid('stretch')}},D)
