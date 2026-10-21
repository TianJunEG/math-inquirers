import json,os,sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','diag'))
from slidekit import *
D=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','split','l5','project')
S={}
def put(sid,html): S[sid]=html

# 3. quick questions with click answers
qs=[('1.','I think of a number, add 3, get 8. What is it?','5'),('2.','I think of a number, take away 2, get 6. What is it?','8'),('3.','I think of a number, add 4, then add 1, get 10. What is it?','5'),('4.','I think of a number, add 2, then take away 1, get 9. What is it?','8')]
body=h2('Quick questions')+''.join(qrow(128,260+i*150,1250,a,b) for i,(a,b,c) in enumerate(qs))+''.join(answer(1420,260+i*150,372,'= '+c) for i,(a,b,c) in enumerate(qs))
put('l5-warm2',sec('l5-warm2','5–10 MIN',body,'Minutes 5 to 10. Read each question aloud, give thinking time, take answers, then click to show the answer. For each one ask: "How did you work it out?" Listen for children who add instead of undoing; we fix this in the teaching part. Answers: 1) 5  2) 8  3) 5  4) 8.'))

# 6. teach: undo it
body=h2('Undo it: do the opposite')+card(p('Adding and taking away undo each other. If a number had 6 added, take 6 away to get back to it.',42,700))+pin(128,560,1664,machine([('?','q'),('+ 6','op'),('14','res')],back='go back:  − 6'),None)
put('l5-teach1',sec('l5-teach1','25–28 MIN',body,'Teach. Show 8 counters, add 6 more in front of the children: 14. Ask: "How do I get back to 8?" Take the 6 away. Say: "Adding 6 and taking away 6 undo each other. They are opposites." Then point to the machine: going forwards we add 6; going backwards we do the opposite, take away 6. Think-aloud: "Mystery number plus 6 is 14. To find it I go backwards. The opposite of add 6 is take away 6."'))

# 7. worked example 1
body=h2('Worked example: one step')+card(p('I think of a number. I add 6. I get 14. What is my number?',44,700))+step(1,'Draw the machine:  ? → + 6 → 14',top=440)+step(2,'Go backwards and do the opposite:  14 − 6 = 8',top=560)+step(3,'Check by going forwards:  8 + 6 = 14  ✓  My number is 8.',top=680)
put('l5-we1',sec('l5-we1','28–30 MIN',body,'Click to reveal each step. Say each step aloud before revealing it and ask the group to predict it. Stress step 3: we always check by going forwards. Model the words: "I go backwards. I do the opposite. I check."'))

# 8. try 1
tq=[('a','? → + 7 → 15','8'),('b','? → − 4 → 9','13'),('c','? → + 9 → 20','11')]
body=h2('Your turn: whiteboards')+p('Write the mystery number. Then check it by going forwards.',34,600,MUTED)+''.join(qrow(128,340+i*150,1250,a,b,42) for i,(a,b,c) in enumerate(tq))+''.join(answer(1420,340+i*150,372,c) for i,(a,b,c) in enumerate(tq))
put('l5-try1',sec('l5-try1','30–31 MIN',body,'Children write on whiteboards and hold them up together. Click for each answer. For b, ask: "The machine took 4 away, so what is the opposite?" (add 4: 9 + 4 = 13). Anyone who writes 5 for b has taken away again: show it with counters.'))

# 9. worked example 2
body=h2('Worked example: two steps')+card(p('I think of a number. I add 5, then I take away 3. I get 9.',44,700))+step(1,'Draw it:  ? → + 5 → □ → − 3 → 9',top=430,size=36)+step(2,'Undo the LAST step first: the opposite of − 3 is + 3.  9 + 3 = 12',top=540,size=36)+step(3,'Then undo + 5:  12 − 5 = 7',top=650,size=36)+step(4,'Check forwards:  7 + 5 = 12,  12 − 3 = 9  ✓  My number is 7.',top=760,size=36)
put('l5-we2',sec('l5-we2','31–33 MIN',body,'Click through the steps. Analogy that works well: "In the morning you put on socks, then shoes. At night you take off shoes first, then socks. Undoing goes in the opposite order." Think-aloud: "The last thing I did was take away 3, so I undo it first: 9 + 3 = 12. Then undo add 5: 12 − 5 = 7. Check: 7 + 5 = 12, 12 − 3 = 9."'))

# 10. try 2
tq=[('a','Add 4, then take away 2. I get 10.','8'),('b','Take away 3, then add 6. I get 11.','8'),('c','Add 2, then add 3. I get 15.','10')]
body=h2('Your turn: two steps')+p('Draw the machine first. Undo the last step first.',34,600,MUTED)+''.join(qrow(128,340+i*150,1250,a,b,40) for i,(a,b,c) in enumerate(tq))+''.join(answer(1420,340+i*150,372,c) for i,(a,b,c) in enumerate(tq))
put('l5-try2',sec('l5-try2','33–34 MIN',body,'Whiteboards again. a) 10 + 2 = 12, 12 − 4 = 8. b) 11 − 6 = 5, 5 + 3 = 8. c) 15 − 3 = 12, 12 − 2 = 10. Ask a child who got b right to explain the order out loud.'))

# 11. key
body=h2('Key idea: work backwards')+card(p('To find a mystery number, undo each step. Start with the last step. Then check by going forwards.',46,700))+card(p('Opposites:  + and −  undo each other.',38,600,MUTED))
put('l5-key',sec('l5-key','34–35 MIN',body,'Say the key idea together. Common mistakes to watch for during the worksheet: (1) Adding again instead of undoing (12 + 5). (2) Two steps: undoing in the wrong order. (3) Queue questions: counting a child twice, or adding numbers without drawing the queue.'))

# 13. teach machine rule
body=h2('Number machines: find the rule')+pin(128,250,1664,'<table style="font-size:44px"><tr><th style="text-align:left">IN</th><th style="text-align:left">1</th><th style="text-align:left">4</th><th style="text-align:left">7</th><th style="text-align:left">?</th></tr><tr style="background:#FFFFFF"><td>OUT</td><td>5</td><td>8</td><td>?</td><td>20</td></tr></table>')+step(1,'Compare each IN with its OUT: 1 → 5 is 4 more. Check 4 → 8: 4 more ✓',top=480,size=36)+step(2,'Rule: add 4.  So IN 7 gives OUT 7 + 4 = 11',top=590,size=36)+step(3,'OUT 20? Go backwards: 20 − 4 = 16. IN is 16.',top=700,size=36)
put('l5-teachm',sec('l5-teachm','40–42 MIN',body,'Teach before worksheet page 1 (Q2 uses number machines). Stress: check the rule on EVERY pair, not just the first. Ask: "If OUT is 20, which way do we go?" (backwards, take away 4).'))

# 14. worksheet page 1 preview
body=h2('Worksheet page 1: with your partner')+card(p('<span style="color:#1F7A6F;font-weight:800">Q1</span>  Mystery numbers. Draw the machine, go backwards, check forwards.',40,600,raw=True)+p('<span style="color:#1F7A6F;font-weight:800">Q2</span>  Number machines. Find the rule from every pair, then fill the gaps.',40,600,raw=True))+card(p('Stuck? Use counters and a cup to act it out.',36,600,MUTED))
put('l5-ws1',sec('l5-ws1','42–55 MIN',body,'Minutes 42 to 55. Walk around. Ask "How do you know?" before giving any help. For Q1c (two steps) check that pairs undo the last step first.'))

# 15. page 1 go-through
rows=[('Q1','a) 7,   b) 12,   c) 8'),('Q2a','IN 9 gives OUT 15.  OUT 14 comes from IN 8.'),('Q2b','Rule: add 4.  IN 15 → OUT 19.  OUT 30 ← IN 26.')]
body=h2('Page 1: check together')+''.join(qrow(128,260+i*150,1664,a,'',38).replace('</span>  </p>','</span></p>') for i,(a,b) in enumerate(rows))+''.join(answer(330,260+i*150,1462,b) for i,(a,b) in enumerate(rows))
put('l5-ws1ans',sec('l5-ws1ans','55–57 MIN',body,'Click each answer after a pair explains theirs. For Q1b: the machine takes away 3, so we add 3: 9 + 3 = 12. For Q1c: 10 + 2 = 12, then 12 − 4 = 8.'))

# 16. teach bars
def bar(label,units,col,extra_label=''):
    w=60*units
    return f'<svg aria-label="{E(label)} bar" viewBox="0 0 1664 90" xmlns="http://www.w3.org/2000/svg" style="width:1664px;height:90px"><text x="0" y="58" font-size="40" font-weight="800" fill="{NAVY}" font-family="Nunito Sans, Arial">{E(label)}</text><rect x="200" y="12" width="{w}" height="66" rx="8" fill="{col}" stroke="{NAVY}" stroke-width="4"/>'+''.join(f'<line x1="{200+60*i}" y1="12" x2="{200+60*i}" y2="78" stroke="{NAVY}" stroke-width="1.5" opacity=".35"/>' for i in range(1,units))+f'<text x="{220+w}" y="58" font-size="40" font-weight="800" fill="{TEAL}" font-family="Nunito Sans, Arial">{E(extra_label)}</text></svg>'
body=h2('More than, fewer than: draw bars')+card(p('Tom has 6 stickers. Sue has 4 more than Tom. Kim has 3 fewer than Sue.',40,700))+pin(128,420,1664,bar('Tom',6,SKY,'6'),'rise')+pin(128,530,1664,bar('Sue',10,YEL,'6 + 4 = 10'),'rise')+pin(128,640,1664,bar('Kim',7,'#D3F1E4','10 − 3 = 7'),'rise')+pin(128,760,1664,p('"More than" means a longer bar. "Fewer than" means a shorter bar. Compare with the RIGHT person.',34,600,MUTED),'fade')
put('l5-teachbar',sec('l5-teachbar','57–59 MIN',body,'Teach before worksheet page 2 (Q3). Click to build each bar. Ask before each click: "Is Sue\'s bar longer or shorter than Tom\'s? By how much?" Common mistake: comparing Kim with Tom instead of Sue. Point at the words "than Sue".'))

# 17. teach queue
def queue(n,hi,labels=None,arc=None):
    s=f'<svg aria-label="Queue of {n} children" viewBox="0 0 1664 140" xmlns="http://www.w3.org/2000/svg" style="width:1664px;height:140px"><text x="0" y="78" font-size="30" font-weight="800" fill="{MUTED}" font-family="Nunito Sans, Arial">front</text>'
    for i in range(n):
        x=150+i*110
        s+=f'<circle cx="{x}" cy="70" r="40" fill="{YEL if i in hi else WHITE}" stroke="{NAVY}" stroke-width="4"/>'
        if labels and i in labels: s+=f'<text x="{x}" y="84" font-size="40" font-weight="800" text-anchor="middle" fill="{NAVY}" font-family="Fredoka, Arial">{E(labels[i])}</text>'
    s+=f'<text x="{150+n*110}" y="78" font-size="30" font-weight="800" fill="{MUTED}" font-family="Nunito Sans, Arial">back</text></svg>'
    return s
body=h2('Queue puzzles: draw the queue')+card(p('Mei is 3rd from the front. There are 2 children behind her. How many children are in the queue?',40,700))+pin(128,440,1664,queue(3,[2],{2:'M'}),'rise')+pin(128,580,1664,queue(5,[2],{2:'M'}),'rise')+pin(128,730,1664,p('Count the circles: 5 children. Always draw circles. Never add the numbers straight away.',36,700),'fade')
put('l5-teachq1',sec('l5-teachq1','59–60 MIN',body,'Teach before worksheet page 2 (Q4). Click 1: draw 2 circles and Mei as the 3rd. Click 2: add 2 children behind her. Click 3: count. Children who say "3 + 2 = 5" are right here, but the next slide shows why drawing matters.'))

# 18. queue 2
body=h2('Count each child once')+card(p('Ali is 3rd from the front AND 3rd from the back. How many children are in the queue?',40,700))+pin(128,440,1664,queue(5,[2],{2:'A'}),'rise')+pin(128,590,1664,p('3 from the front and 3 from the back share Ali. 3 + 3 = 6 counts Ali twice, so 6 − 1 = 5.',36,700),'fade')+qrow(128,720,1250,'Your turn:','4th from the front and 4th from the back?',36)+answer(1420,720,372,'7 children')
put('l5-teachq2',sec('l5-teachq2','60–61 MIN',body,'Click 1: draw the queue so Ali is 3rd from both ends. Click 2: explain the double count. Then whiteboards for the "your turn" and click for 7. Extra if time: "10 children. Ben is 4th from the front. How many are behind him?" (6, because Ben is not behind himself).'))

# 19. worksheet page 2
body=h2('Worksheet page 2: on your own')+card(p('<span style="color:#1F7A6F;font-weight:800">Q3</span>  Marble puzzle. Draw a bar for each child.',40,600,raw=True)+p('<span style="color:#1F7A6F;font-weight:800">Q4</span>  Queue puzzles. Draw the circles.',40,600,raw=True)+p('<span style="color:#1F7A6F;font-weight:800">Q5</span>  Make your own mystery number story for a friend.',40,600,raw=True))+card(p('Finished early? Stretch and Challenge come next.',36,600,MUTED))
put('l5-ws2',sec('l5-ws2','61–68 MIN',body,'Children work alone. Note who needs a short catch-up next lesson. Check that every child draws bars for Q3 and circles for Q4.'))

# 20. page 2 go-through
rows=[('Q3','Mei 13,  Ben 7,  Mei has 6 more than Ben,  28 altogether'),('Q4a','13 children are behind Mei (20 − 7)'),('Q4b','15 children: 8 + 8 counts Ali twice, so 16 − 1')]
body=h2('Page 2: check together')+''.join(qrow(128,260+i*150,1664,a,'',38).replace('</span>  </p>','</span></p>') for i,(a,b) in enumerate(rows))+''.join(answer(330,260+i*150,1462,b) for i,(a,b) in enumerate(rows))
put('l5-ws2ans',sec('l5-ws2ans','68–70 MIN',body,'Click each answer after a child explains. Q3: Mei = 8 + 5 = 13, Ben = 13 − 6 = 7, difference 13 − 7 = 6, total 8 + 13 + 7 = 28. Q4a: Mei is not behind herself, so 20 − 7 = 13. Q5: check that each story has one clear answer.'))

# 21. stretch (new items)
st=[('1.','Ali and Ben have 20 marbles together. Ali has 4 more than Ben. How many does each have?'),('2.','Ben had some stickers. He gave away 6, got 4, then gave away 3. Now he has 10. How many did he have at first?'),('3.','Tom is 5th from the front. There are 4 children between Tom and Sue, who is last. How many are in the queue?')]
body=h2('Stretch')+''.join(card(p(f'<span style="color:#1F7A6F">{a}</span>  {E(b)}',36,600,raw=True)) for a,b in st)
put('l5-stretch',sec('l5-stretch','For early finishers',body,'For children who finish early. Answers: 1) Ben 8, Ali 12 (take away the extra 4: 16, share equally: 8 each, then give Ali the 4). 2) 15 (work backwards: 10 + 3 = 13, 13 − 4 = 9, 9 + 6 = 15; check 15 − 6 + 4 − 3 = 10). 3) 10 (Tom is 5th, then 4 children, then Sue: 5 + 4 + 1).'))

# 22. challenge
ch=[('1.','A number machine adds 3, then adds 4. IN 5 gives OUT 12. What goes IN to give OUT 20?'),('2.','A snail climbs 3 cm each day and slides back 1 cm each night. It starts at the bottom of a 9 cm wall. On which day does it reach the top?')]
body=h2('Challenge')+''.join(card(p(f'<span style="color:#1F7A6F">{a}</span>  {E(b)}',38,600,raw=True)) for a,b in ch)
put('l5-challenge',sec('l5-challenge','Challenge',body,'Pairs try first, then use the "see it" slide if stuck, then the walk-through. Answers: 1) 13 (20 − 4 = 16, 16 − 3 = 13; check 13 + 3 + 4 = 20). 2) Day 4 (end of day 1: 3, night: 2; day 2: 5, night: 4; day 3: 7, night: 6; day 4: 9, it is at the top before it can slide back).'))

# 23. chdiag
import panels
snail=panels.l5b()
body=h2('Challenge: see it',60)+'<div style="display:flex;gap:32px;align-items:flex-start">'+card('<p style="font-size:28px;font-weight:700;color:#1F7A6F">Q1: The two-step machine</p>'+machine([('?','q'),('+ 3','op'),('+ 4','op'),('20','res')],w=760).replace('width:760px;height:130px','width:100%;height:auto'),extra='flex:1;min-width:0;padding:20px 24px')+card('<p style="font-size:28px;font-weight:700;color:#1F7A6F">Q2: The snail and the wall</p>'+snail.replace('<svg ','<svg aria-label="Snail climbing a 9 cm wall" ',1),extra='flex:1;min-width:0;padding:20px 24px')+'</div>'
put('l5-chdiag',sec('l5-chdiag','Challenge',body,'Show after pairs have tried, or if they are stuck. The pictures show the problem, not the answer. Ask: What do you notice? What do we know? Which way do we go?'))

# 24. walk-through
body=h2('Challenge: walk-through')+pin(128,250,800,p('Q1: go backwards',40,800,TEAL),None)+pin(128,330,800,p('20 − 4 = 16',40),'rise',WHITE)+pin(128,440,800,p('16 − 3 = 13',40),'rise',WHITE)+pin(128,550,800,p('Check: 13 + 3 + 4 = 20 ✓',40),'rise',WHITE)
tbl='<table style="font-size:34px"><tr><th style="text-align:left">Day</th><th style="text-align:left">After climbing</th><th style="text-align:left">After night</th></tr><tr style="background:#FFFFFF"><td>1</td><td>3 cm</td><td>2 cm</td></tr><tr><td>2</td><td>5 cm</td><td>4 cm</td></tr><tr style="background:#FFFFFF"><td>3</td><td>7 cm</td><td>6 cm</td></tr><tr><td>4</td><td>9 cm: top!</td><td>does not slide</td></tr></table>'
body+=pin(1000,250,792,p('Q2: make a table',40,800,TEAL),None)+pin(1000,330,792,tbl,'rise')
put('l5-chwalk',sec('l5-chwalk','Challenge',body,'Use after pairs have tried. Q1: undo the last step first. Q2: many children say day 5 or day 3. The table shows the snail reaches 9 cm during day 4, before night comes. Ask: "Why does the table stop at day 4?"'))

for sid,h in S.items(): open(os.path.join(D,'slides',sid+'.html'),'w').write(h)
deck=json.load(open(os.path.join(D,'deck.json')))
deck['order']=['l5-title','l5-warm1','l5-warm2','l5-explore1','l5-explore2','l5-teach1','l5-we1','l5-try1','l5-we2','l5-try2','l5-key','l5-break','l5-teachm','l5-ws1','l5-ws1ans','l5-teachbar','l5-teachq1','l5-teachq2','l5-ws2','l5-ws2ans','l5-stretch','l5-challenge','l5-chdiag','l5-chwalk','l5-talk','l5-exit']
deck['sections']={'s1':{'description':'Warm-up and explore','start':'l5-title'},'s2':{'description':'Teach: working backwards, step by step','start':'l5-teach1'},'s3':{'description':'Worksheet with teaching before each page','start':'l5-break'},'s4':{'description':'Stretch, challenge, talk and exit','start':'l5-stretch'}}
json.dump(deck,open(os.path.join(D,'deck.json'),'w'),indent=1,ensure_ascii=False)
print(len(deck['order']),'slides; wrote',len(S))
