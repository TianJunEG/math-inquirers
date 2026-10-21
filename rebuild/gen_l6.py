import json,os,sys
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,H)
from slidekit import *
D=os.path.join(H,'..','split','l6','project'); S={}
def put(i,h): S[i]=h
qs=[('1.','Pay 15¢ with two coins.','10¢ + 5¢'),('2.','Pay 30¢ with the fewest coins.','20¢ + 10¢'),('3.','Pay 25¢ with two coins.','20¢ + 5¢'),('4.','Pay 40¢ with two coins.','20¢ + 20¢')]
body=h2('Quick questions')+''.join(qrow(128,260+i*150,1250,a,b) for i,(a,b,c) in enumerate(qs))+''.join(answer(1420,260+i*150,372,c) for i,(a,b,c) in enumerate(qs))
put('l6-warm2',sec('l6-warm2','5–10 MIN',body,'Minutes 5 to 10. Children show the coins with play money, then click to reveal. Ask: "Could you pay 40¢ with two coins another way?" (no: only 20¢ + 20¢).'))
# teach 1: table for 15c then 25c
W=[240,240,260]
body=h2('Every way, in order: use a table')+card(p('Make 15¢ with 10¢ and 5¢ coins.',40,700))
body+=trow(128,380,['10¢','5¢','Total'],W,None,True)
body+=trow(128,470,['1','1','15¢'],W,'rise')+trow(128,560,['0','3','15¢'],W,'rise')
body+=pin(1060,380,732,p('Start with as many of the BIGGEST coin as you can. Then use one fewer, and one fewer, until there are none.',36,700),None,SOFT,20,'24px 28px')
body+=pin(1060,640,732,p('No more rows: the 10¢ count is down to 0. So there are 2 ways.',36,700),'fade',WHITE,20,'24px 28px')
put('l6-teach1',sec('l6-teach1','25–28 MIN',body,'Teach. Click to add each row while children say what goes in it. Think-aloud: "Ways to make 15¢ with 10¢ and 5¢ coins. I start with the biggest coin: one 10¢. Then 5¢ is left, so one 5¢. Now no 10¢: only 5¢ coins, three of them. The 10¢ column went 1, 0, so I know I am finished."'))
W4=[200,200,200,240]
body=h2('Worked example: 25¢')+card(p('Make 25¢ with 20¢, 10¢ and 5¢ coins. How many ways?',40,700))
body+=trow(128,380,['20¢','10¢','5¢','Total'],W4,None,True)
rows=[['1','0','1','25¢'],['0','2','1','25¢'],['0','1','3','25¢'],['0','0','5','25¢']]
for i,r in enumerate(rows): body+=trow(128,470+i*90,r,W4,'rise')
body+=pin(1180,380,612,p('20¢ first: one 20¢ (20 + 5).',34,700),'fade',WHITE,20,'20px 24px')+pin(1180,520,612,p('Then no 20¢: two 10¢, one 10¢, no 10¢.',34,700),'fade',WHITE,20,'20px 24px')+pin(1180,680,612,p('4 ways. 10¢ + 5¢ + 10¢ is the same way as row 2.',34,700),'fade',SOFT,20,'20px 24px')
put('l6-we1',sec('l6-we1','28–31 MIN',body,'Click to build each row and the side notes. Ask before each row: "What comes next if I go one fewer?" Think-aloud: "With a 20¢: 20 + 5. With 10¢ but no 20¢: 10 + 10 + 5 and 10 + 5 + 5 + 5. With only 5¢: five of them. That is 4 ways. I used a table so I did not repeat any."'))
put('l6-try1',try_slide('l6-try1','31–33 MIN','Your turn: how many ways?','Use a table. Biggest coin first.',[('a','Make 10¢ with 10¢ and 5¢ coins.','2 ways'),('b','Make 20¢ with only 10¢ and 5¢ coins.','3 ways'),('c','Make 35¢ with 20¢ and 5¢ coins only.','2 ways')],'Whiteboards. a) 10, or 5 + 5. b) 10 + 10, 10 + 5 + 5, four 5¢. c) 20 + 5 + 5 + 5, or seven 5¢. Ask: "Why can\'t we use two 20¢ for c?" (40¢ is too much).'))
body=h2('Key idea: work in order')+card(p('Biggest coin first, then one fewer each time. Use a table so you do not repeat or miss a way.',44,700))+card(p('Same coins in a different order count as one way.',38,600,MUTED))
put('l6-key',sec('l6-key','33–35 MIN',body,'Say the key idea together. Common mistakes to watch for during the worksheet: (1) Listing the same way twice in a different order (10+5+5 and 5+10+5). (2) Choosing many small coins instead of looking for the fewest. (3) Stopping at the first set in Q4 instead of checking for all of them.'))
put('l6-ws1',ws_preview('l6-ws1','40–52 MIN','Worksheet page 1: with your partner',[('Q1','Ways to make 20¢. Fill in the table, biggest coin first.'),('Q2','All the ways to make 30¢. Write each way like this: 1 × 20¢ + 2 × 5¢')],'Use play coins on the table, then write the way down.','Minutes 40 to 52. Walk around. Ask "How do you know you have them all?" Check that pairs work in order.'))
put('l6-ws1ans',check_slide('l6-ws1ans','52–54 MIN','Page 1: check together',[('Q1','4 ways: 20 / 10+10 / 10+5+5 / 5+5+5+5.  Fewest: one 20¢.  Most: four 5¢.'),('Q2','6 ways: 20+10, 20+5+5, 10+10+10, 10+10+5+5, 10+5+5+5+5, six 5¢')],'Click after pairs explain. Q1c: "We started with the biggest coin and went one fewer each time until there were none."'))
# fewest coins
body=h2('Fewest coins: biggest coin you can, again and again')+card(p('Pay 65¢ with the fewest coins (5¢, 10¢, 20¢, 50¢).',40,700))+step(1,'Biggest coin that fits: 50¢. 15¢ is left.',top=420,size=36)+step(2,'Biggest coin that fits 15¢: 10¢. 5¢ is left.',top=530,size=36)+step(3,'Then 5¢. Nothing left. 50 + 10 + 5 = 65: 3 coins.',top=640,size=36)
put('l6-teachfew',sec('l6-teachfew','54–56 MIN',body,'Teach before worksheet page 2 (Q3). Ask after step 3: "Could 2 coins make 65¢?" (No: the two biggest, 50 + 20, make 70, and no pair makes exactly 65.)'))
# exact number of coins
body=h2('Exactly 3 coins')+card(p('Make 25¢ with exactly 3 coins (5¢, 10¢, 20¢).',40,700))+step(1,'Try a 20¢: 20 + 5 = 25, but that is only 2 coins ✗',top=420,size=36)+step(2,'Try two 10¢: 10 + 10 + 5 = 25, and it is 3 coins ✓',top=530,size=36)+step(3,'Try one 10¢: 10 + 5 + 5 = 20, too little ✗.  Only one way: 10 + 10 + 5.',top=640,size=36)+pin(128,770,1664,p('Check TWO things every time: the total, and the number of coins.',34,700),'fade',SOFT,20,'18px 28px')
put('l6-teachexact',sec('l6-teachexact','56–57 MIN',body,'Teach before worksheet page 2 (Q4 asks for ALL the sets of 4 coins worth 70¢). Model trying every biggest-coin start, not stopping at the first answer.'))
# swap coins
body=h2('Swap coins to reach the total')+card(p('5 coins, only 5¢ and 10¢, worth 35¢. How many of each?',40,700))+step(1,'Start with all 5¢: five 5¢ = 25¢. We need 10¢ more.',top=420,size=36)+step(2,'Each swap of a 5¢ for a 10¢ adds 5¢. 25 → 30 → 35: 2 swaps.',top=530,size=36)+step(3,'So two 10¢ and three 5¢. Check: 20 + 15 = 35, 5 coins ✓',top=640,size=36)
put('l6-teachswap',sec('l6-teachswap','57–58 MIN',body,'Teach before worksheet page 2 (Q6, Sam\'s 90¢). Act it out with play coins: lay out five 5¢, then swap one at a time and count the total aloud.'))
put('l6-ws2',ws_preview('l6-ws2','58–66 MIN','Worksheet page 2: on your own',[('Q3','85¢ with the fewest coins, then a way with exactly 6 coins.'),('Q4','Every set of 4 coins worth 70¢. Check the total AND the count.'),('Q5','Can 35¢ be made with 2 coins? Explain.'),('Q6','Sam\'s 90¢. Start with all 10¢ coins and swap.')],'Finished early? Stretch and Challenge come next.','Children work alone. Note who needs a short catch-up next lesson.'))
put('l6-ws2ans',check_slide('l6-ws2ans','66–68 MIN','Page 2: check together',[('Q3','4 coins: 50 + 20 + 10 + 5.  6 coins: e.g. 50 + 10 + 10 + 5 + 5 + 5'),('Q4','50 + 10 + 5 + 5,  and  20 + 20 + 20 + 10'),('Q5','No: two coins make 10, 15, 20, 25, 30, 40, 55, 60, 70 or 100'),('Q6','3 × 10¢ and 3 × 20¢.  4 coins: no, the most is 80¢')],'Click after a child explains. Q6: six 10¢ = 60¢; each swap to a 20¢ adds 10¢; 30¢ more means 3 swaps.'))
st=[('1.','How many ways can you make 40¢ with 20¢, 10¢ and 5¢ coins?'),('2.','Mei has 6 coins, all 5¢ and 10¢, worth 45¢. How many of each?'),('3.','What is the fewest number of coins for 95¢ (5¢, 10¢, 20¢, 50¢)?')]
put('l6-stretch',sec('l6-stretch','For early finishers',h2('Stretch')+''.join(card(p(f'<span style="color:#1F7A6F">{a}</span>  {E(b)}',38,600,raw=True)) for a,b in st),'Answers: 1) 9 ways (two 20¢: 1 way; one 20¢: 3 ways; no 20¢: 5 ways). 2) Three 10¢ and three 5¢. 3) 4 coins: 50 + 20 + 20 + 5 (3 coins cannot work: you need a 5¢, and no two coins make 90¢).'))
body=h2('Challenge: walk-through')+pin(128,250,800,p('Q1: count by number of coins',38,800,TEAL))
for i,t in enumerate(['1 coin: 5, 10, 20, 50 → 4 amounts','2 coins: 15, 25, 55, 30, 60, 70 → 6','3 coins: 35, 65, 75, 80 → 4','4 coins: 85 → 1.   Total: 15 ✓']): body+=pin(128,330+i*105,800,p(t,32),'rise',WHITE)
body+=pin(992,250,800,p('Q2: try biscuits 1, 2, 3 …',38,800,TEAL))
for i,t in enumerate(['1 biscuit: 70¢ left. Not a 15¢ amount ✗','2 biscuits: 50¢ left ✗','3 biscuits: 30¢ left = 2 sweets ✓','4 biscuits: 10¢ left ✗.  Answer: 2 sweets, 3 biscuits']): body+=pin(992,330+i*105,800,p(t,32),'rise',WHITE)
put('l6-chwalk',sec('l6-chwalk','Challenge',body,'Use after pairs have tried. Q1: the trick is to work in order by number of coins so nothing is missed or repeated. Q2: 15¢ amounts are 15, 30, 45, 60, 75; only 30¢ is left over when Ben buys 3 biscuits.'))
# exit ticket update
ex=os.path.join(D,'slides','l6-exit.html'); s=open(ex).read()
s=s.replace('Make 25¢ using exactly three coins from 5¢, 10¢, 20¢, 50¢.','Make 40¢ using exactly three coins from 5¢, 10¢, 20¢, 50¢.').replace('Answer: 10¢ + 10¢ + 5¢.','Answer: 20¢ + 10¢ + 10¢.')
open(ex,'w').write(s)
for i,h in S.items(): open(os.path.join(D,'slides',i+'.html'),'w').write(h)
for old in ['l6-mini1','l6-mini2']:
    f=os.path.join(D,'slides',old+'.html')
    if os.path.exists(f): os.remove(f)
t=os.path.join(D,'slides','l6-title.html'); s=open(t).read(); s=s.replace('mini-lesson 25 to 35, brain break 35 to 40, worksheet 40 to 70','teaching 25 to 35 (click to reveal each step and answer), brain break 35 to 40, worksheet 40 to 70 with short teaching before each page and a check-together slide after it'); open(t,'w').write(s)
deck=json.load(open(os.path.join(D,'deck.json')))
deck['order']=['l6-title','l6-warm1','l6-warm2','l6-explore1','l6-explore2','l6-teach1','l6-we1','l6-try1','l6-key','l6-break','l6-ws1','l6-ws1ans','l6-teachfew','l6-teachexact','l6-teachswap','l6-ws2','l6-ws2ans','l6-stretch','l6-challenge','l6-chdiag','l6-chwalk','l6-talk','l6-exit']
deck['sections']={'s1':{'description':'Warm-up and explore','start':'l6-title'},'s2':{'description':'Teach: every way, in order','start':'l6-teach1'},'s3':{'description':'Worksheet with teaching before each page','start':'l6-break'},'s4':{'description':'Stretch, challenge, talk and exit','start':'l6-stretch'}}
json.dump(deck,open(os.path.join(D,'deck.json'),'w'),indent=1,ensure_ascii=False)
print(len(deck['order']),'slides')
