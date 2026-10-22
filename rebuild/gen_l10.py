import json,os,sys
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,H)
from slidekit import *
D=os.path.join(H,'..','split','l10','project'); S={}
def put(i,h): S[i]=h
RED='#D64545'; GREEN='#BFE3DC'; PINK='#F4A6A6'; BLUE='#9CC9EE'

def svg(w,h,body,aria): return f'<svg aria-label="{E(aria)}" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="width:{w}px;height:{h}px">{body}</svg>'
def T(x,y,s,size=30,fill=NAVY,anchor='middle',weight=800): return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" fill="{fill}" font-family="Nunito Sans, Arial">{E(s)}</text>'
def row_svg(label,items,u=56,lab_w=170,h=76,after='',aria=''):
    """items: (count, fill, style) style solid|dashT"""
    x=lab_w; b=T(0,h/2+12,label,32,anchor='start') if label else ''
    for cnt,fill,style in items:
        for i in range(cnt):
            if style=='dashT': b+=f'<rect x="{x+2}" y="8" width="{u-4}" height="{h-16}" rx="6" fill="{WHITE}" stroke="{TEAL}" stroke-width="4" stroke-dasharray="10 7"/>'
            else: b+=f'<rect x="{x+2}" y="8" width="{u-4}" height="{h-16}" rx="6" fill="{fill}" stroke="{NAVY}" stroke-width="4"/>'
            x+=u
    if after: b+=T(x+18,h/2+12,after,34,TEAL,'start')
    W=int(x+(len(after)*19+40 if after else 10))
    return svg(W,h,b,aria or label)

# ---------- 3. quick questions (click answers) ----------
qs=[('1.','Count in 3s: 3, 6, 9, __','12'),('2.','10 = 4 + __','6'),('3.','Red 4, blue 6. How many more are blue?','2 more'),('4.','I think of a number, add 4, get 9. What is it?','5'),('5.','Which two coins make 15¢?','10¢ + 5¢')]
body=h2('Quick questions')+''.join(qrow(128,250+i*125,1250,a,b) for i,(a,b,c) in enumerate(qs))+''.join(answer(1420,250+i*125,372,c) for i,(a,b,c) in enumerate(qs))
put('l10-warm2',sec('l10-warm2','5–10 MIN',body,'Minutes 5 to 10. One question from each of our earlier lessons. Read each aloud, give thinking time, take answers, then click to show. Ask "Which lesson does this remind you of?" Answers: 1) 12 (patterns). 2) 6 (bonds of 10). 3) 2 more (picture graphs: 6 − 4). 4) 5 (working backwards: 9 − 4). 5) 10¢ + 5¢ (coins).'))

# ---------- 6. teach: how to start a puzzle ----------
ic_draw=svg(440,140,''.join(f'<rect x="20" y="{12+i*44}" width="{w}" height="34" rx="6" fill="{c}" stroke="{NAVY}" stroke-width="4"/>' for i,(w,c) in enumerate([(220,PINK),(320,BLUE),(160,GREEN)])),'Icon: bars drawn for a puzzle')
ic_list=svg(440,140,''.join(T(30,40+i*44,f'{i+1}.',30,TEAL,'start')+f'<line x1="80" y1="{30+i*44}" x2="{380-i*60}" y2="{30+i*44}" stroke="{NAVY}" stroke-width="6" stroke-linecap="round"/>' for i in range(3)),'Icon: a list in order')
tb=''.join(f'<rect x="{20+c*100}" y="{10+r*40}" width="100" height="40" fill="{YEL if r==0 else WHITE}" stroke="{NAVY}" stroke-width="3"/>' for r in range(3) for c in range(4))
ic_table=svg(440,140,tb,'Icon: a table')
cards=[('Draw it',ic_draw,'People in order, more than and fewer than, number machines.'),('List it',ic_list,'Find every way: coins, pairs of numbers, shapes to count.'),('Make a table',ic_table,'Something that grows or changes step by step.')]
body=h2('How to start a puzzle')+p('Stuck? Do not just stare. Put the puzzle on paper.',34,600,MUTED)
for i,(t,ic,use) in enumerate(cards):
    body+=pin(128+i*572,320,480,p(t,44,800,TEAL)+ic+p('Use it for: '+use,30,600),'rise',WHITE,24,'26px 30px')
body+=pin(128,790,1664,p('Why? A puzzle is hard to hold in your head. On paper you can see it, check it and explain it.',32,700),'fade',SOFT,20,'18px 28px')
put('l10-teach1',sec('l10-teach1','25–26 MIN',body,'Teach: the idea and why. "Today\'s puzzles mix everything we have learned. Clever inquirers do not know every answer straight away. They know how to START." Click each card and give one example from our lessons: Draw it (the queue in Lesson 5, the bars in Lesson 9). List it (the coin tables in Lesson 6). Make a table (the snail in Lesson 5, patterns in Lesson 1). Click the last box and read it together. The next three slides show each start in action.'))

# ---------- 7. worked example: draw it (order) ----------
lad=svg(160,460,f'<line x1="80" y1="60" x2="80" y2="400" stroke="{NAVY}" stroke-width="6"/><polygon points="80,30 62,64 98,64" fill="{NAVY}"/><polygon points="80,430 62,396 98,396" fill="{NAVY}"/>'+T(80,22,'taller',26,TEAL)+T(80,456,'shorter',26,TEAL),'A line from taller at the top to shorter at the bottom')
nm=lambda n,top: pin(330,top,260,p(n,40,800),'pop',YEL,16,'12px 24px')
body=h2('Draw it: put people in order')+card(p('Jo is taller than Ravi. Lin is shorter than Ravi. Kai is shorter than Jo but taller than Ravi. Who is the shortest?',36,700))
body+=pin(128,410,160,lad)
body+=step(1,'Draw a line: tallest at the top. Jo goes above Ravi. Leave a space.',left=680,top=420,width=1112,size=32)
body+=nm('Jo',420)+nm('Ravi',640)
body+=step(2,'Lin is shorter than Ravi, so Lin goes below Ravi.',left=680,top=560,width=1112,size=32)
body+=nm('Lin',750)
body+=step(3,'Kai is between Jo and Ravi: he goes in the space.',left=680,top=660,width=1112,size=32)
body+=nm('Kai',530)
body+=answer(680,770,1112,'Lin is the shortest. Check every clue ✓')
put('l10-we1',sec('l10-we1','26–28 MIN',body,'Worked example: draw it. Ask first: "Can you hold all of this in your head?" Click step 1, then Jo and Ravi appear. Think-aloud: "I draw a line with tall at the top. Jo is taller than Ravi, so Jo is higher. I leave a space in case someone goes between." Step 2, then Lin. Step 3, then Kai: "Shorter than Jo but taller than Ravi: that is the space I left." Answer: read the line from the bottom: Lin. Check each clue against the drawing aloud. The worksheet Q6 uses older and younger: same drawing, oldest at the top.'))

put('l10-try1',try_slide('l10-try1','28–29 MIN','Your turn: draw it','Draw a line, bars or a machine before you answer.',[('a','Ann is older than Bo. Cy is older than Ann. Who is the oldest?','Cy'),('b','Two numbers add up to 10. One is 4 more than the other.','3 and 7'),('c','I think of a number, add 6, take away 2 and get 11.','7')],'Whiteboards. a) Line, oldest at the top: Cy, Ann, Bo. b) Draw cubes: take away the extra 4, 6 left; share: 3 and 3; give the 4 back: 3 and 7. Check 3 + 7 = 10 and 7 is 4 more than 3. c) Draw the machine and go backwards, last step first: 11 + 2 = 13, 13 − 6 = 7. Check 7 + 6 = 13, 13 − 2 = 11.',36))

# ---------- 9. worked example: list it (coins) ----------
coins=svg(560,110,''.join(f'<circle cx="{60+i*140}" cy="55" r="{r}" fill="#E5E9F2" stroke="{NAVY}" stroke-width="4"/><circle cx="{60+i*140}" cy="55" r="{r-8}" fill="none" stroke="#8A94AD" stroke-width="2"/>'+T(60+i*140,66,l,30) for i,(l,r) in enumerate([('50¢',52),('20¢',46),('10¢',42),('10¢',42)])),'Coins: one 50 cent, one 20 cent, two 10 cent')
body=h2('List it: every way, in order')+card('<div style="display:flex;align-items:center;gap:40px">'+p('Which of these coins make exactly 40¢?',38,700)+coins+'</div>')
body+=step(1,'Start with the biggest coin. 50¢ is more than 40¢: too much.',top=440,size=34)
body+=step(2,'Next, 20¢:  20 + 10 = 30, too little.  20 + 10 + 10 = 40 ✓',top=550,size=34)
body+=step(3,'Without 20¢:  10 + 10 = 20, too little.  So the only way is 20¢ + 10¢ + 10¢.',top=660,size=34)
body+=pin(128,790,1664,p('Going in order means you do not miss a way, and you know when to stop.',32,700),'fade',SOFT,20,'18px 28px')
put('l10-we2',sec('l10-we2','29–31 MIN',body,'Worked example: list it. Think-aloud: "I could grab coins at random, but then I might miss a way. So I go in order, biggest coin first. 50¢ is already too much. With the 20¢: 20 and 10 is 30, not enough; 20 and both 10s is 40, yes. Now without the 20¢: only the two 10s, that is 20, too little. I have tried everything, so there is only one way." This is the method for worksheet Q4b (a different set of coins), and for counting triangles later.'))

put('l10-try2',try_slide('l10-try2','31–32 MIN','Your turn: list it','Go in order. Biggest first.',[('a','You have 20¢, 10¢, 5¢, 5¢. Which coins make exactly 25¢?','20¢ + 5¢'),('b','How many ways can you make 20¢ with 20¢, 10¢ and 5¢ coins?','4 ways'),('c','2, 6, 10, 14, … Is 24 in the pattern?','No: 22, 26')],'Whiteboards. a) With 20¢: 20 + 5 = 25 ✓. Without 20¢: 10 + 5 + 5 = 20, too little. Only 20¢ + 5¢. b) 20; 10 + 10; 10 + 5 + 5; 5 + 5 + 5 + 5: 4 ways. c) List the pattern (add 4): 2, 6, 10, 14, 18, 22, 26. It jumps over 24, so no.',36))

# ---------- 11. worked example: make a table ----------
W=[150]+[96]*10
body=h2('Make a table: the 10th number')+card(p('4, 7, 10, 13, …   What is the 10th number?',40,700))
body+=step(1,'Find the rule. Check every pair: 4 → 7 → 10 → 13. Add 3 each time.',top=360,size=34)
body+=trow(128,470,['Place']+[str(i) for i in range(1,11)],W,header=True,size=34)
body+=trow(128,550,['Number','4','7','10','13']+['']*6,W,size=34)
body+=step(2,'Keep adding 3 until the 10th place.',top=660,width=1100,size=34)
body+=trow(128,550,['Number']+[str(4+3*i) for i in range(10)],W,'rise',size=34)
body+=answer(1260,660,532,'10th number: 31')
body+=qrow(128,780,1250,'Your turn:','2, 5, 8, … What is the 7th number?',34)+answer(1420,780,372,'20')
put('l10-we3',sec('l10-we3','32–34 MIN',body,'Worked example: make a table. Think-aloud: "I want the 10th number, so I need to know which place each number is in. A table keeps the places tidy. The rule is add 3: I checked every pair, not just the first. 13 is in place 4. Then 16, 19, 22, 25, 28, 31. Place 10 is 31." Count the places aloud with the children so no one skips one. Common mistake: counting the jumps instead of the places (10 numbers have only 9 jumps). Your turn: 2, 5, 8, 11, 14, 17, 20. The 7th number is 20.'))

body=h2('Key idea: how to start a puzzle')+card(p('Stuck? Draw it, list it in order, or make a table.',46,700))+card(p('Then check your answer and explain why.',38,600,MUTED))
put('l10-key',sec('l10-key','34–35 MIN',body,'Say the key idea together. Common mistakes to watch for during the worksheet: (1) Rushing: not checking the answer against every clue. (2) Q1: finding the rule from the first pair only. (3) Q3c and Q4b: stopping at the first pair or set that works without listing them all. (4) Q5b: counting only the 3 small triangles. (5) Q7: undoing in the wrong order. (6) Q8b: adding 6 + 4 instead of 6 + 10.'))

# ---------- teach before page 1: picture graphs ----------
fr=[('Apples',6,'#C0392B'),('Pears',3,'#7DA453'),('Plums',5,'#7D3C98'),('Figs',4,'#B9770E')]
g=''.join(T(0,48+i*80,n,32,anchor='start')+''.join(f'<circle cx="{200+j*70}" cy="{38+i*80}" r="26" fill="{c}"/>' for j in range(k)) for i,(n,k,c) in enumerate(fr))+f'<circle cx="14" cy="361" r="11" fill="{NAVY}"/>'+T(34,370,'= 1 fruit',28,MUTED,'start',700)
body=h2('Picture graphs: count, compare, combine')+pin(128,260,640,svg(640,390,g,'Picture graph: apples 6, pears 3, plums 5, figs 4'))
body+=step(1,'How many more apples than pears? Line up the rows: 3 stick out. 6 − 3 = 3.',left=840,top=260,width=952,size=32)
body+=step(2,'How many fruits altogether? 6 + 3 + 5 + 4 = 18.',left=840,top=420,width=952,size=32)
body+=step(3,'Which two make exactly 11? List the pairs with apples first: 6 + 3 = 9, no. 6 + 5 = 11 ✓ Apples and plums.',left=840,top=540,width=952,size=32)
body+=pin(128,720,1664,p('Count each row carefully. To compare, find the difference. To combine, add.',32,700),'fade',SOFT,20,'18px 28px')
put('l10-teachgraph',sec('l10-teachgraph','40–42 MIN',body,'Teach before worksheet page 1 (Q3 is a picture graph). Click each step after children try it on whiteboards. Step 1: "How many more" means the difference: the 3 apples that stick out past the pears. Step 3: list the pairs in order so none are missed: apples with pears (9), plums (11 ✓), figs (10); then pears with plums (8), figs (7); plums with figs (9). Only apples and plums make 11. Total check: 6 + 3 = 9, 9 + 5 = 14, 14 + 4 = 18.'))

put('l10-ws1',ws_preview('l10-ws1','42–53 MIN','Worksheet page 1: with your partner',[('Q1','Pattern. Find the rule from every pair, then continue.'),('Q2','Two numbers. Draw cubes: take away the extra, share, give it back.'),('Q3','Picture graph. Count, compare, combine.'),('Q4','Coins. List in order, biggest coin first.')],'Stuck? Draw it, list it, or make a table.','Minutes 42 to 53. Walk around. Ask "How did you start?" and "How do you know?" before giving any help. Q2 is like the cube method from Lesson 2. Q4b: check pairs list in order.'))
put('l10-ws1ans',check_slide('l10-ws1ans','53–55 MIN','Page 1: check together',[('Q1','23, 28.   Rule: add 5.'),('Q2','5 and 7'),('Q3','a) 2 more   b) 19 pets   c) Cat and fish'),('Q4','a) 50¢   b) 20¢ + 10¢ + 5¢')],'Click each answer after a pair explains how they started. Q1: 3 → 8 → 13 → 18, add 5 each time: 23, 28. Q2: take away the extra 2: 10 left, share: 5 and 5, give back 2: 5 and 7. Check 5 + 7 = 12. Q3: a) cats 7 − birds 5 = 2. b) 4 + 7 + 3 + 5 = 19. c) list the pairs: only cat and fish make 7 + 3 = 10. Q4: a) 20 + 10 + 10 + 5 + 5 = 50. b) with 20¢: 20 + 10 = 30, 20 + 10 + 5 = 35 ✓.'))

# ---------- teach before page 2: count triangles ----------
A,B,C,M=(300,40),(40,400),(560,400),(300,400)
pts=lambda *q: ' '.join(f'{x},{y}' for x,y in q)
base=svg(600,460,f'<polygon points="{pts(A,B,C)}" fill="{WHITE}" stroke="{NAVY}" stroke-width="6" stroke-linejoin="round"/><line x1="300" y1="40" x2="300" y2="400" stroke="{NAVY}" stroke-width="6"/>','A triangle with one line from the top to the bottom')
o1=svg(600,460,f'<polygon points="{pts(A,B,M)}" fill="{YEL}" fill-opacity=".6" stroke="{NAVY}" stroke-width="6"/>'+T(215,320,'1',48),'First small triangle')
o2=svg(600,460,f'<polygon points="{pts(A,M,C)}" fill="{GREEN}" fill-opacity=".8" stroke="{NAVY}" stroke-width="6"/>'+T(385,320,'2',48),'Second small triangle')
o3=svg(600,460,f'<polygon points="{pts(A,B,C)}" fill="none" stroke="{TEAL}" stroke-width="14" stroke-linejoin="round" stroke-dasharray="22 12"/>'+T(300,450,'3: the big one',34,TEAL),'The whole big triangle')
body=h2('Count triangles: small ones first')+pin(128,250,600,base)
body+=step(1,'Count the small triangles: 1, 2.',left=800,top=270,width=992,size=34)
body+=pin(128,250,600,o1,'fade')+pin(128,250,600,o2,'fade')
body+=step(2,'Now triangles made of two small ones: the big one, 3.',left=800,top=380,width=992,size=34)
body+=pin(128,250,600,o3,'fade')
body+=step(3,'3 triangles. Small first, then bigger, so none are missed.',left=800,top=520,width=992,size=34)
body+=qrow(128,740,1250,'Your turn:','I have 4 sides and 4 corners. Only the opposite sides are the same length. What am I?',32)+answer(1420,740,372,'A rectangle')
put('l10-teachtri',sec('l10-teachtri','55–57 MIN',body,'Teach before worksheet page 2 (Q5). Click: step 1, then each small triangle lights up as you count. Step 2, then the whole outline. Step 3. Think-aloud: "I count in order: the smallest first, then ones made of two pieces, then three pieces. That way I do not miss the big one or count one twice." The teaching picture has TWO lines from the top (the worksheet picture has one, so it is easier): ask "What are the smallest ones? Which ones are made of two?" Your turn (a shape riddle like Q5a): a rectangle. A square has all 4 sides the same, so it does not fit "only the opposite sides".'))

# ---------- teach: longer than, then end to end ----------
cr=row_svg('Crayon',[(5,PINK,'solid')],56,190,after='5',aria='Crayon 5 cubes')
ru=row_svg('Ruler',[(5,PINK,'solid'),(7,None,'dashT')],56,190,after='5 + 7 = 12',aria='Ruler 7 cubes longer than the crayon')
to=row_svg('Together',[(5,PINK,'solid'),(12,BLUE,'solid')],56,190,after='17',aria='Crayon and ruler end to end, 17 cubes')
body=h2('Longer than, then end to end')+card(p('A crayon is 5 cubes long. A ruler is 7 cubes longer than the crayon.',38,700))
body+=pin(128,370,1664,cr)+pin(128,460,1664,ru,'rise')
body+=step(1,'Ruler: start from the crayon\'s bar and add 7.  5 + 7 = 12 cubes.',top=560,size=34)
body+=pin(128,670,1664,to,'rise')
body+=step(2,'End to end: 5 + 12 = 17 cubes. Not 5 + 7!',top=780,size=34)
put('l10-teachlen',sec('l10-teachlen','57–58 MIN',body,'Teach before worksheet page 2 (Q8). Click the ruler bar, step 1, the end-to-end bar, step 2. Think-aloud: "7 longer is not the ruler\'s length: it is the extra bit. The ruler is the crayon\'s 5 and 7 more: 12. End to end means both whole lengths: 5 + 12 = 17." Common mistake: 5 + 7 = 12 given as the end-to-end answer.'))

put('l10-ws2',ws_preview('l10-ws2','58–66 MIN','Worksheet page 2: on your own',[('Q5','Shapes. Count the small triangles first, then bigger ones.'),('Q6','Older and younger. Draw a line, oldest at the top.'),('Q7','Mystery number. Draw the machine and go backwards.'),('Q8','Pencil and pen. Draw the bars.')],'Finished early? Stretch and Challenge come next.','Children work alone. Note who needs a short catch-up. Q9: check that the puzzle has exactly one answer and that the child can say how to start it.'))
put('l10-ws2ans',check_slide('l10-ws2ans','66–68 MIN','Page 2: check together',[('Q5','a) A square   b) 3 triangles'),('Q6','Mei is the youngest.'),('Q7','5'),('Q8','a) 10 cubes   b) 16 cubes')],'Click each answer after a child explains how they started. Q5b (one line from the top corner, picture on the page): 2 small triangles and 1 big one made of both = 3. The 3 + 2 + 1 = 6 count is the teaching picture with two lines. Q6: line, oldest at the top: Ali, Ben, Mei. Q7: undo the last step first: 10 + 4 = 14, 14 − 9 = 5. Check 5 + 9 = 14, 14 − 4 = 10. Q8: pen 6 + 4 = 10; end to end 6 + 10 = 16.'))

# ---------- stretch (new) ----------
st=[('1.','Mei thinks of a number, adds 7, takes away 2 and gets 19. Ben does the same and gets 25. How much bigger is Ben\'s number?'),('2.','4, 9, 14, 19, …  Which number in this pattern is closest to 50?'),('3.','Ali has 5 coins worth 60¢. He has only 5¢, 10¢ and 20¢ coins. Find every possible set.')]
put('l10-stretch',sec('l10-stretch','For early finishers',h2('Stretch')+''.join(card(p(f'<span style="color:#1F7A6F">{a}</span>  {E(b)}',36,600,raw=True)) for a,b in st),'For children who finish early. Answers: 1) 6 bigger. Work backwards: Mei 19 + 2 = 21, 21 − 7 = 14; Ben 25 + 2 = 27, 27 − 7 = 20; 20 − 14 = 6. (Clever shortcut: both did the same steps, so the answers differ by the same amount: 25 − 19 = 6.) 2) 49 (list it: 24, 29, 34, 39, 44, 49, 54; 49 is 1 away, 54 is 4 away). 3) Two sets: 20 + 10 + 10 + 10 + 10, and 20 + 20 + 10 + 5 + 5. Make a table by number of 20¢ coins: one 20¢ needs 40¢ from 4 coins (four 10¢); two 20¢ need 20¢ from 3 coins (10 + 5 + 5); three 20¢ need 0¢ from 2 coins (impossible); no 20¢: 5 coins make at most 50¢.'))

# ---------- challenge walk-through ----------
body=h2('Challenge: walk-through')+pin(128,250,800,p('Q1: draw bars',38,800,TEAL))
for i,t in enumerate(['Ben is Ali and 4 more. Mei is 3 fewer than Ben, so Mei is Ali and 1 more.','Take away the extras: 29 − 4 − 1 = 24','Three equal bars make 24: 8 + 8 + 8 = 24','Ali 8, Ben 12, Mei 9. Check: 8 + 12 + 9 = 29 ✓']): body+=pin(128,330+i*135,800,p(t,32),'rise',WHITE)
body+=pin(992,250,800,p('Q2: list it, biggest coin first',38,800,TEAL))
for i,t in enumerate(['With 50¢: 20¢ more from 3 coins: 10 + 5 + 5 ✓','No 50¢: 20 + 20 + 20 + 10 = 70 ✓','20 + 20 + 20 + 5 = 65, and 20 + 20 + 10 + 10 = 60: too little.','So there are 2 ways.']): body+=pin(992,330+i*135,800,p(t,32),'rise',WHITE)
put('l10-chwalk',sec('l10-chwalk','Challenge',body,'Use after pairs have tried, with the "see it" slide. Q1: Mei is 3 fewer than Ben, and Ben is Ali plus 4, so Mei is Ali plus 1. Remove the extra 4 and the extra 1 and three equal bars are left: 24. Try equal bars: 7 + 7 + 7 = 21 is too small, 8 + 8 + 8 = 24 ✓. Q2: with 50¢ the other 3 coins must make 20¢: only 10 + 5 + 5. Without 50¢, four coins of 20¢ or less make at most 80¢: only 20 + 20 + 20 + 10 reaches 70¢.'))


# ---------- kept slides: accessibility and minimum text size ----------
import re
def tidy(sid,labels,fix_fonts=False):
    f=os.path.join(D,'slides',sid+'.html'); s=open(f).read(); k=iter(labels)
    s=re.sub(r'<svg (?!aria-label)',lambda m:f'<svg aria-label="{next(k)}" ',s)
    if fix_fonts: s=s.replace('font-size="22"','font-size="26"').replace('font-size="24"','font-size="25"')
    open(f,'w').write(s)
tidy('l10-explore1',['Four puzzle stations: coins, patterns, logic and measuring'])
tidy('l10-chdiag',['Stickers drawn as bars for Ali, Ben and Mei','Four empty coin boxes for exactly 4 coins making 70 cents'],True)
# ---------- puzzle cards slide (audit 1: the four cards, pairs get ONE card for 10 minutes, swap for 4) ----------
import subprocess
CARDS=json.loads(subprocess.run(['node','-e',"console.log(JSON.stringify(require('./hp/lessons.js').lessons[9].cards))"],capture_output=True,text=True,cwd=os.path.join(H,'..')).stdout)
body=h2('Puzzle cards: pick one')+p('Your pair gets ONE card for 10 minutes. Then swap with another pair for 4 minutes.',34,600,MUTED)
for k,c in enumerate(CARDS):
    L=128+(k%2)*848; T=330+(k//2)*330
    body+=pin(L,T,816,p(E(c['title']),38,800,TEAL)+p(E(c['text']),34,600,raw=True),None,WHITE,24,'22px 30px',f'box-sizing:border-box;min-height:290px;border:4px dashed {NAVY}')
put('l10-cards',sec('l10-cards','11–21 MIN',body,'Minutes 11 to 21. Each pair works on ONE puzzle card for 10 minutes (the printed cards are on the Puzzle cards page of the workbook; online, one card per breakout room). Then pairs swap cards with another pair for a 4-minute second round (21 to 25, with Explore: talk about it). Each pair reports back in 30 seconds. Answers: Coins) 20¢ + 20¢ + 5¢ (the only way). Patterns) 32: add 3 each time, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32. Logic) Mei, Ben, Sam, Ali. Measuring) 16 cubes: the pen is 10 cubes, and 6 + 10 = 16.'))
for i,h in S.items(): open(os.path.join(D,'slides',i+'.html'),'w').write(h)
for old in ['l10-mini1','l10-mini2']:
    f=os.path.join(D,'slides',old+'.html')
    if os.path.exists(f): os.remove(f)
t=os.path.join(D,'slides','l10-title.html'); s=open(t).read()
for a,b in [('mini-lesson 25 to 35, brain break 35 to 40, worksheet 40 to 70','teaching 25 to 35 (how to start a puzzle: draw it, list it, make a table; click to reveal each step and answer), brain break 35 to 40, worksheet 40 to 70 with short teaching before each page and a check-together slide after it'),
            ('Materials: Puzzle cards for 4 stations, play coins, cubes, certificates, stamps.','Materials: Puzzle cards for 4 stations, play coins, cubes, mini whiteboards, certificates, stamps.')]:
    if a in s: s=s.replace(a,b)
open(t,'w').write(s)
deck=json.load(open(os.path.join(D,'deck.json')))
deck['order']=['l10-title','l10-warm1','l10-warm2','l10-explore1','l10-explore2','l10-teach1','l10-we1','l10-try1','l10-we2','l10-try2','l10-we3','l10-key','l10-break','l10-teachgraph','l10-ws1','l10-ws1ans','l10-teachtri','l10-teachlen','l10-ws2','l10-ws2ans','l10-stretch','l10-challenge','l10-chdiag','l10-chwalk','l10-talk','l10-exit','end']
deck['sections']={'s1':{'description':'Warm-up and explore','start':'l10-title'},'s2':{'description':'Teach: how to start a puzzle (draw it, list it, make a table)','start':'l10-teach1'},'s3':{'description':'Worksheet with teaching before each page','start':'l10-break'},'s4':{'description':'Stretch, challenge, talk, exit and close','start':'l10-stretch'}}
json.dump(deck,open(os.path.join(D,'deck.json'),'w'),indent=1,ensure_ascii=False)
print(len(deck['order']),'slides; wrote',len(S))

import re, p1fix
for sid,pairs in {'l10-explore1':[('Four stations, eight minutes at each: coins, patterns, logic, measuring.','Four puzzle cards: coins, patterns, logic, measuring. Your pair gets ONE card for 10 minutes. Then swap cards with another pair for 4 minutes.')],
                  'l10-explore2':[('What did you do first at each station?','What did you do first on your card?'),('Which station was hardest? Why?','Which card was hardest? Why?')]}.items():
    p1fix.patch(D,sid,pairs)
f=os.path.join(D,'slides','l10-explore1.html'); t=open(f).read()
t=re.sub(r'<aside>.*?</aside>','<aside>Minutes 10 to 11. Explain the plan, then move to the next slide with the four puzzle cards. Each pair works on ONE card for 10 minutes (11 to 21), then swaps with another pair for a 4-minute second round (21 to 25). Materials: the four puzzle cards (workbook Puzzle cards page), play coins, cubes, mini whiteboards. Online: one card per breakout room; each pair reports back in 30 seconds.</aside>',t,flags=re.S); open(f,'w').write(t)
f=os.path.join(D,'slides','l10-explore2.html'); t=open(f).read()
t=re.sub(r'<aside>.*?</aside>','<aside>Minutes 21 to 25. Pairs swap cards with another pair for the second 4-minute round, then gather to answer these. Keep report-backs to 30 seconds each; shorten them if time is tight. Answers: 1) Open answers.  2) Open answers.  3) An inquirer rule: notice, test, check, explain.</aside>',t,flags=re.S); open(f,'w').write(t)
f=os.path.join(D,'slides','l10-talk.html'); t=open(f).read()
if 'Q9' not in t:
    t=t.replace('Pick one puzzle and teach it to the group in two sentences.','Make a puzzle for a friend (workbook Q9) with its answer. Swap it with a partner and solve it. Then pick one puzzle and teach it to the group in two sentences.')
    t=re.sub(r'<aside>Minutes 70 to 80\.','<aside>Minutes 72 to 80. Q9 (make a puzzle for a friend) is done here, not on worksheet page 2: pairs write a puzzle with its answer, swap, and solve each other\'s.',t)
    open(f,'w').write(t)
p1fix.sub_all(D,[('Puzzle cards for 4 stations','the four puzzle cards (coins, patterns, logic, measuring)'),('Online: one puzzle per breakout pair.',''),('Online: Breakout pairs work on one puzzle card each, then report back to the group.','Online: one card per breakout room; each pair reports back in 30 seconds.')])
d=json.load(open(os.path.join(D,'deck.json'))); 
if 'l10-cards' not in d['order']: d['order'].insert(d['order'].index('l10-explore1')+1,'l10-cards')
json.dump(d,open(os.path.join(D,'deck.json'),'w'),indent=1,ensure_ascii=False)
import p1gifted; p1gifted.apply(D,10)
import p1gaps; p1gaps.apply(D,10)
p1fix.finish(D,10,{'l10-explore1':'10–11 MIN','l10-explore2':'21–25 MIN','l10-ws2':'58–68 MIN'})
import p1neutral; p1neutral.apply(D,10)
