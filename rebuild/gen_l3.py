import json,os,sys
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,H)
from slidekit import *
D=os.path.join(H,'..','split','l3','project'); S={}
def put(i,h): S[i]=h

# ---- local helpers ----
RED='#D64545'; BLUE='#3A6EA5'; GRN='#2E9E6B'; GOLD='#E0A100'; PURP='#7D3C98'
def graph(rows,w=1000,lw=220,cell=62,rh=64,marks=None,overlay=False,extra=None):
    """Picture graph. rows: (label,count,colour). marks: {(row,col):(fill,text,textcol)} drawn on top.
    overlay=True draws only the marks (for build-in reveals). extra: {row: text} written after the pictures."""
    h=rh*len(rows)+6
    s=f'<svg aria-label="Picture graph: {E(", ".join(f"{a} {n}" for a,n,c in rows))}" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="width:{w}px;height:{h}px">'
    if not overlay:
        for i,(lab,n,col) in enumerate(rows):
            y=3+i*rh
            s+=f'<rect x="3" y="{y}" width="{w-6}" height="{rh}" fill="{WHITE}" stroke="{NAVY}" stroke-width="3"/><line x1="{lw-10}" y1="{y}" x2="{lw-10}" y2="{y+rh}" stroke="{NAVY}" stroke-width="3"/>'
            s+=f'<text x="18" y="{y+rh/2+12}" font-size="34" font-weight="700" fill="{NAVY}" font-family="Nunito Sans, Arial">{E(lab)}</text>'
            for j in range(n):
                s+=f'<circle cx="{lw+j*cell+cell/2}" cy="{y+rh/2}" r="24" fill="{col}" stroke="{NAVY}" stroke-width="3"/>'
            if extra and i in extra:
                s+=f'<text x="{lw+n*cell+20}" y="{y+rh/2+14}" font-size="40" font-weight="800" fill="{TEAL}" font-family="Fredoka, Arial">{E(extra[i])}</text>'
    for (i,j),(fill,t,tc) in (marks or {}).items():
        cx=lw+j*cell+cell/2; cy=3+i*rh+rh/2
        s+=f'<circle cx="{cx}" cy="{cy}" r="27" fill="{fill}" stroke="{NAVY}" stroke-width="4"/>'
        if t: s+=f'<text x="{cx}" y="{cy+9}" font-size="26" font-weight="800" text-anchor="middle" fill="{tc}" font-family="Nunito Sans, Arial">{E(t)}</text>'
    return s+'</svg>'
def tally(n,h=120):
    groups=n//5; rest=n%5; w=groups*130+rest*26+30
    s=f'<svg aria-label="Tally of {n}" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="width:{w}px;height:{h}px">'
    x=20
    for g in range(groups):
        for k in range(4): s+=f'<line x1="{x+k*24}" y1="15" x2="{x+k*24}" y2="105" stroke="{NAVY}" stroke-width="7" stroke-linecap="round"/>'
        s+=f'<line x1="{x-12}" y1="88" x2="{x+84}" y2="32" stroke="{RED}" stroke-width="7" stroke-linecap="round"/>'; x+=130
    for k in range(rest): s+=f'<line x1="{x+k*26}" y1="15" x2="{x+k*26}" y2="105" stroke="{NAVY}" stroke-width="7" stroke-linecap="round"/>'
    return s+'</svg>'
def keybox(left,top,width,text): return pin(left,top,width,p(text,36,800),None,SOFT,20,'20px 28px')
def rows_slide(sid,time,title,sub,rows,notes,top=340,gap=150,size=40,aw=372):
    body=h2(title)+(p(sub,34,600,MUTED) if sub else '')
    for i,(a,b,c) in enumerate(rows):
        body+=qrow(128,top+i*gap,1664-aw-48,a,b,size)+answer(1792-aw,top+i*gap,aw,c)
    return sec(sid,time,body,notes)

# ---- teach 1: read the key, then compare ----
G1=[('Red',4,RED),('Blue',7,BLUE),('Green',3,GRN),('Yellow',4,GOLD)]
body=h2('Read the key, then compare')+pin(128,240,1000,graph(G1),None)+keybox(1180,240,612,'Key:  ● = 1 child')
body+=pin(1180,370,612,p('Our favourite colours',34,700,MUTED),None)
body+=step(1,'Read the key: ● = 1 child.  Most: blue (7).  Fewest: green (3).  Same: red and yellow (4).',top=540,size=32)
body+=step(2,'How many more blue than green? Match each green with a blue. 4 blues are left:  7 − 3 = 4.',top=645,size=32)
body+=pin(128,240,1000,graph(G1,marks={(1,j):(YEL,'',NAVY) for j in range(3,7)},overlay=True),'fade')
body+=step(3,'How many altogether? Add every row:  7 + 3 = 10,  4 + 4 = 8,  10 + 8 = 18 children.',top=750,size=32)
put('l3-teach1',sec('l3-teach1','25–27 MIN',body,'Teach. Point to the key first: "Before I count anything, I read the key. One dot stands for one child." Click 1: most, fewest, same. Click 2 and 3: how many more. Put a finger on each green dot and the blue dot above it: "This green has a partner … this one … this one. These 4 blues have no partner, so blue has 4 more." Think-aloud from the lesson script: "How many more chose blue than green? I do not add. I compare. Blue has 7 and green has 3. The difference is 7 − 3 = 4." Click 4: altogether. "I look for a 10: 7 + 3 = 10. Then 4 + 4 = 8. 10 + 8 = 18." Watch for children who add (7 + 3 = 10) when asked "how many more".'))

# ---- try 1 ----
G2=[('Swim',6,BLUE),('Run',2,RED),('Cycle',6,GRN),('Skip',5,GOLD)]
body=h2('Your turn: whiteboards')+pin(128,240,1000,graph(G2,rh=60),None)+keybox(1180,240,612,'Key:  ● = 1 child')+pin(1180,370,612,p('Our favourite sports',34,700,MUTED),None)
for i,(a,b,c) in enumerate([('a','Which two sports are tied?','Swim, cycle'),('b','How many more chose swim than run?','4'),('c','How many children voted altogether?','19')]):
    body+=qrow(128,530+i*120,1250,a,b,36)+answer(1420,530+i*120,372,c)
put('l3-try1',sec('l3-try1','27–28 MIN',body,'Write it, say the answer together on three, then click. a) Swim and cycle both have 6. b) Match up: 4 swim dots have no partner, 6 − 2 = 4. c) 6 + 6 = 12, 12 + 2 = 14, 14 + 5 = 19. For c, ask: "Did anyone find a quick way?" Anyone who answers 8 for b has added: line up the two rows again.'))

# ---- teach 2: key of 2 ----
G3=[('Pizza',4,RED),('Noodles',6,GOLD),('Rice',2,GRN)]
body=h2('A key of 2: count in 2s')+pin(128,240,1000,graph(G3),None)+keybox(1180,240,612,'Key:  ● = 2 children')+pin(1180,370,612,p('Our class lunch vote',34,700,MUTED),None)
body+=step(1,'Read the key first: each ● stands for 2 children.',top=470,size=34)
body+=step(2,'Noodles: count in 2s.  2, 4, 6, 8, 10, 12.  12 children chose noodles.',top=575,size=34)
body+=pin(128,240,1000,graph(G3,marks={(1,j):(YEL,str(2*(j+1)),NAVY) for j in range(6)},overlay=True),'fade')
body+=step(3,'How many more noodles than rice? 4 more pictures: 2, 4, 6, 8.  8 more children.',top=680,size=34)
body+=pin(128,240,1000,graph(G3,marks={(1,j):(TEAL,str(2*(j-1)),WHITE) for j in range(2,6)},overlay=True),'fade')
body+=pin(128,810,1664,p('Why a key of 2? When many children vote, the rows stay short. But we must count in 2s.',32,700,MUTED),'fade')
put('l3-teach2',sec('l3-teach2','28–30 MIN',body,'Teach. Ask first: "How many children chose noodles?" Many children count the dots and say 6. Point to the key: "Each dot is 2 children." Click to step 2, then click to put the counting numbers on the dots and count in 2s together. Step 3: rice has 2 dots, so noodles has 4 extra dots; click to show them and count them in 2s: 8. Check: noodles 12 children, rice 4 children, 12 − 4 = 8. Think-aloud: "I always read the key first. One dot is 2 children, so I count in 2s, not 1s." Pizza: 2, 4, 6, 8. Total: 12 dots, count in 2s to 24.'))

# ---- try 2 ----
put('l3-try2',rows_slide('l3-try2','30–31 MIN','Your turn: keys of 2 and 3','Read the key first.',[('a','● = 2 children. Milk has 5 pictures. How many children?','10'),('b','▲ = 3 children. Juice has 4 pictures. How many children?','12'),('c','● = 2 children. 8 children chose water. How many pictures?','4')],'Whiteboards. a) Count in 2s five times: 2, 4, 6, 8, 10. b) Count in 3s four times: 3, 6, 9, 12. c) Count in 2s until you say 8: 2, 4, 6, 8 is 4 counts, so 4 pictures. Children can tap a finger for each count. For c, ask: "Why not 8 pictures?"',gap=150,size=34))

# ---- teach 3: missing row from the total ----
G4=[('Pizza',8,RED),('Noodles',5,GOLD),('Rice',0,GRN)]
body=h2('Find the missing row')+card(p('20 children voted. Pizza 8, noodles 5. The rest chose rice. How many chose rice?',40,700))
body+=pin(128,430,820,graph(G4,w=820,lw=200,cell=62,extra={2:'?'}),None)
body+=pin(128,430,820,graph(G4,w=820,lw=200,cell=62,marks={(2,j):(GRN,'','') for j in range(7)},overlay=True),'fade')
body+=step(1,'Add the rows we know:  8 + 5 = 13.',left=990,top=430,width=742,size=32)
body+=step(2,'Count on from 13 to 20:  14, 15, 16, 17, 18, 19, 20.  That is 7.',left=990,top=545,width=742,size=32)
body+=step(3,'Draw 7 for rice. Check:  8 + 5 + 7 = 20 ✓',left=990,top=700,width=742,size=32)
body+=qrow(128,835,1200,'Your turn:','15 children voted. Red 6, blue 4, the rest chose green. How many chose green?',30)+answer(1420,845,372,'5')
put('l3-teach3',sec('l3-teach3','31–32 MIN',body,'Teach. This graph has a row missing, but we know how many children voted. Click 1: add the rows we know. Click 2: count on from 13 to 20 on fingers (7 fingers). Click 3: the rice row appears. Click 4: check. Think-aloud: "Everybody voted once, so all the rows together must make 20. Pizza and noodles make 13. How many more to make 20? I count on: 14, 15, 16, 17, 18, 19, 20. Seven." Ask: "Which food won now?" (pizza, 8). Your turn (the only one in this mini-lesson after the keys of 2 and 3): children write on their own paper, then click for 5 (6 + 4 = 10, count on from 10 to 15). Take-home for children who want more (also on the Think harder slide, not for class time): the key is lost, cats have 3 pictures and 6 children chose cats (1 picture = 2 children); then dogs have 5 pictures (10 children).'))

# ---- try 3 ----
put('l3-try3',rows_slide('l3-try3','32–33 MIN','Your turn: think it through','Use what you know to find what is missing.',[('a','15 children voted. Red 6, blue 4, the rest chose green. How many chose green?','5'),('b','The key is lost! Cats have 3 pictures. 6 children chose cats. What is 1 picture worth?','2 children'),('c','Same graph: dogs have 5 pictures. How many chose dogs?','10')],'Whiteboards. a) 6 + 4 = 10, count on from 10 to 15: 5. b) Try a key of 1: 3 pictures would be 3 children, too few. Try 2: count in 2s, 2, 4, 6. Yes, 1 picture = 2 children. c) 5 pictures, count in 2s: 2, 4, 6, 8, 10.',top=330,gap=180,size=34))

# ---- key ----
body=h2('Key idea: read the key first')+card(p('The key tells us what one picture means. Count in 1s, 2s or 3s to match the key.',44,700))+card(p('How many more? Match up and count the extra. Altogether? Add every row.',38,600,MUTED))+card(p('A vote tells us about the people who voted.',38,600,MUTED))
put('l3-key',sec('l3-key','33–35 MIN',body,'Say the key idea together. Common mistakes to watch for during the worksheet: (1) Adding when asked "how many more" (8 + 3 instead of 8 − 3). (2) Naming only one of two tied fruits. (3) Q5: missing a row when adding; tick each row as you add it. (4) Saying "Yes" in Q6 because our class chose orange. (5) Counting pictures in 1s when the key is 2 (Stretch and Challenge).'))

# ---- worksheet page 1 ----
put('l3-ws1',ws_preview('l3-ws1','40–52 MIN','Worksheet page 1: with your partner',[('Q1–Q2','Most and fewest: find the longest and the shortest row.'),('Q3','How many more? Match up the two rows and count the extra.'),('Q4','Two the same: find two rows that end in the same place.')],'Read the key first. Point to each dot as you count it.','Minutes 40 to 52. Pairs work together on Part A. Walk around and ask "What does one dot stand for?" and "Is the question asking how many more or how many altogether?"'))
put('l3-ws1ans',check_slide('l3-ws1ans','52–54 MIN','Page 1: check together',[('Q1','Orange'),('Q2','Grape'),('Q3','5 more:  8 − 3 = 5'),('Q4','Banana and watermelon (5 each)')],'Click each answer after a pair explains theirs. Q3: match the 3 grape dots with 3 orange dots; 5 orange dots are left.'))

# ---- teach before page 2: who voted? ----
body=h2('Who voted? What else matters?')+card(p('P1B voted for ice cream for their class party. Can we say the whole school likes ice cream best?',40,700))
body+=step(1,'Who voted? Only the children in P1B.',top=430,size=36)
body+=step(2,'Other classes did not vote. They might choose something else. We can only say: "P1B likes ice cream best."',top=540,size=36)
body+=step(3,'Think about more than votes. Will the ice cream melt before the party? Is there a freezer?',top=700,size=36)
put('l3-teachwho',sec('l3-teachwho','54–56 MIN',body,'Teach before worksheet page 2 (Q6 asks if one class vote tells us about the whole school; Q7 asks what else the teacher should think about). Ask the question first and take a thumbs vote. Then click through. Ask: "How could we find out what the whole school likes?" (ask more children, every class). Step 3 ideas are only about ice cream; let children find their own ideas for fruit on the worksheet.'))

# ---- teach before page 2: tally marks ----
body=h2('Tally marks: bundles of 5')+card(p('Make one mark for each vote. The 5th mark goes across the first 4.',40,700))
body+=pin(128,370,640,tally(12),None,WHITE,20,'20px 28px')
body+=step(1,'Count the bundles in 5s:  5, 10.',left=860,top=370,width=872,size=34)
body+=step(2,'Count on the single marks:  11, 12.  12 votes.',left=860,top=480,width=872,size=34)
body+=pin(128,620,1210,f'<p style="font-size:36px;font-weight:600;line-height:1.3"><span style="color:{TEAL};font-weight:800">Your turn:</span>  how many votes?</p>'+tally(8,110),None,WHITE,20,'18px 28px')
body+=answer(1420,620,372,'8 votes')
put('l3-teachtally',sec('l3-teachtally','56–58 MIN',body,'Teach before worksheet page 2 (Part B, where children take their own vote with tally marks). Draw a tally on the board as you say "one, two, three, four, and the fifth goes across: a bundle of 5." Click through the counting. Your turn: children count on whiteboards, then click: 5, then 6, 7, 8. Remind them: the totals of all the rows must add up to the number of children who voted.'))

# ---- worksheet page 2 ----
put('l3-ws2',ws_preview('l3-ws2','58–66 MIN','Worksheet page 2: on your own',[('Q5','Altogether: add every row. Look for a 10.'),('Q6','Mei says orange is best for the whole school. Is she right? Why?'),('Q7','What else should the teacher think about before buying?'),('Part B','Take your own group vote with tally marks. Then Q8 and Q9.')],'Finished early? Stretch and Challenge come next.','Children work alone on Q6 and Q7, then the group votes together for Part B. Check that totals add up to the number of children who voted. Note who needs a short catch-up next lesson.'))
put('l3-ws2ans',check_slide('l3-ws2ans','66–68 MIN','Page 2: check together',[('Q5','27 children:  6 + 5 + 8 + 3 + 5'),('Q6','No. Only our class voted. Other classes may like other fruits.'),('Q7','Cost, enough for everyone, easy to share, keeps fresh, allergies'),('Part B','The totals add up to the number of children who voted.'),('Q9','Different children like different things. A small group may not match.')],'Click each answer after a child explains. Q5: one quick way is 5 + 5 = 10, 6 + 8 = 14, 10 + 14 = 24, 24 + 3 = 27. Q7: accept any sensible idea, such as cost, how many are needed, easy to share, keeps fresh, messy to eat, or a child who cannot eat it. Q8 depends on the group vote.',lw=220))

# ---- stretch (new) ----
st=[('1.','Key: ● = 2 children.  Apple ●●●,  Banana ●●●●●,  Orange ●●.  How many more chose banana than orange?'),('2.','25 children voted: apple 8, banana 6, grape 4, and the rest chose orange. Draw the orange row. Which fruit won?'),('3.','The key is missing. Apple has 4 pictures and 12 children chose apple. Banana has 3 pictures. How many chose banana?')]
put('l3-stretch',sec('l3-stretch','For early finishers',h2('Stretch')+''.join(card(p(f'<span style="color:#1F7A6F">{a}</span>  {E(b)}',38,600,raw=True)) for a,b in st),'For children who finish early. Answers: 1) 6 more. Banana 2, 4, 6, 8, 10 children; orange 2, 4 children; 10 − 4 = 6 (or: 3 extra pictures, count in 2s: 2, 4, 6). 2) Orange 7 (8 + 6 + 4 = 18, count on from 18 to 25: 7). Apple wins with 8. 3) 9. Count in 3s: 3, 6, 9, 12 is 4 pictures, so 1 picture = 3 children. Banana: 3, 6, 9.'))

# ---- challenge (rewritten for the audit: Q1 "6 more", Q2 key of 2) ----
ch=[('1.','24 children voted. Apple got 6 votes. Orange got 6 more votes than banana. How many votes did banana and orange get?'),('2.','1 picture = 2 children. 20 children voted for three fruits. A has 3 pictures. B has 2 more pictures than A. How many children chose C?')]
put('l3-challenge',sec('l3-challenge','Optional: if you finish early',h2('Challenge')+''.join(card(p(f'<span style="color:#1F7A6F">{a}</span>  {E(b)}',34,600,raw=True)) for a,b in ch),'Use as a pair challenge or in talk time. Ask for the reason every time. More are in the question bank. Answers: 1) Banana 6 and orange 12.  2) 4 children (20 children is 10 pictures in all; A 3 + B 5 = 8, so C has 2 pictures = 4 children).'))
def bar(x,y,w,col,lab,h=70,q=False):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{col}" stroke="{NAVY}" stroke-width="4"/>'
            f'<text x="{x+w/2}" y="{y+h/2+11}" font-size="32" font-weight="800" text-anchor="middle" fill="{NAVY}" font-family="Nunito Sans, Arial">{E(lab)}</text>')
u=50
q1=f'<svg aria-label="Bars: apple 6, banana a mystery, orange the banana bar plus 6" viewBox="0 0 800 330" xmlns="http://www.w3.org/2000/svg" style="width:700px;height:289px">'
q1+=f'<text x="0" y="52" font-size="30" font-weight="700" fill="{NAVY}" font-family="Nunito Sans, Arial">Apple</text>'+bar(150,10,6*u,RED,'6')
q1+=f'<text x="0" y="152" font-size="30" font-weight="700" fill="{NAVY}" font-family="Nunito Sans, Arial">Banana</text>'+bar(150,110,6*u,BLUE,'?')
q1+=f'<text x="0" y="252" font-size="30" font-weight="700" fill="{NAVY}" font-family="Nunito Sans, Arial">Orange</text>'+bar(150,210,6*u,GOLD,'?')+bar(150+6*u,210,6*u,'#FFFFFF','6 more')
q1+='</svg>'
G5=[('A',3,RED),('B',5,BLUE),('C',0,GRN)]
q2=graph(G5,w=700,lw=110,cell=52,rh=70,extra={2:'?'})
body=h2('Challenge: see it')+'<div style="display:flex;gap:32px;align-items:flex-start">'+card(p('Q1: Votes as bars',28,700,TEAL)+q1)+card(p('Q2: A picture graph, key: ● = 2 children',28,700,TEAL)+q2)+'</div>'
put('l3-chdiag',sec('l3-chdiag','Optional: if you finish early',body,'Show after pairs have tried the Challenge, or if they are stuck. The diagrams show the problem, not the answer. Q1: orange is the banana bar plus 6 more. Q2: A has 3 dots, B has 2 more than A, and C is the part we do not know. Ask: What do you notice? What do we know? What do we not know yet? Can you draw it? Answers are in the Challenge slide notes.'))

body=h2('Challenge: walk-through')+pin(128,250,800,p('Q1: take away the extra 6',38,800,TEAL))
for i,(t,bg) in enumerate([('Apple has 6, so 24 − 6 = 18 for banana and orange.',WHITE),('Orange has 6 more than banana. Take away the extra 6: 18 − 6 = 12.',WHITE),('Share 12 equally: banana 6. Give orange the 6 back: 12.',WHITE),('Banana 6, orange 12.  Check: 6 + 6 + 12 = 24 ✓',YEL)]): body+=pin(128,330+i*130,800,p(t,32),'rise',bg)
body+=pin(992,250,800,p('Q2: count in 2s',38,800,TEAL))
for i,(t,bg) in enumerate([('2, 4, 6 … 20 is 10 counts: 10 pictures in all.',WHITE),('A has 3. B has 3 + 2 = 5. Together: 8 pictures.',WHITE),('C has 10 − 8 = 2 pictures: 2, 4.',WHITE),('C: 4 children',YEL)]): body+=pin(992,330+i*130,800,p(t,32),'rise',bg)
put('l3-chwalk',sec('l3-chwalk','Optional: if you finish early',body,'Use after pairs have tried. Q1: guess and check is fine: banana 6 and orange 12 make 18, and 6 + 6 + 12 = 24. Or take the extra 6 away and share the rest. Q2: A 6 children, B 10 children, C 4 children, and 6 + 10 + 4 = 20.'))

for i,h in S.items(): open(os.path.join(D,'slides',i+'.html'),'w').write(h)
for old in ['l3-mini1','l3-mini2']:
    f=os.path.join(D,'slides',old+'.html')
    if os.path.exists(f): os.remove(f)
t=os.path.join(D,'slides','l3-title.html'); s=open(t).read(); s=s.replace('mini-lesson 25 to 35, brain break 35 to 40, worksheet 40 to 70','teaching 25 to 35 (click to reveal each step and answer), brain break 35 to 40, worksheet 40 to 70 with short teaching before each page and a check-together slide after it'); open(t,'w').write(s)
deck=json.load(open(os.path.join(D,'deck.json')))
deck['order']=['l3-title','l3-warm1','l3-warm2','l3-explore1','l3-explore2','l3-teach1','l3-try1','l3-teach2','l3-try2','l3-teach3','l3-try3','l3-key','l3-break','l3-ws1','l3-ws1ans','l3-teachwho','l3-teachtally','l3-ws2','l3-ws2ans','l3-stretch','l3-challenge','l3-chdiag','l3-chwalk','l3-talk','l3-exit']
deck['sections']={'s1':{'description':'Warm-up and explore','start':'l3-title'},'s2':{'description':'Teach: read the key, compare, keys of 2 and 3, missing rows','start':'l3-teach1'},'s3':{'description':'Worksheet with teaching before each page','start':'l3-break'},'s4':{'description':'Stretch, challenge, talk and exit','start':'l3-stretch'}}
json.dump(deck,open(os.path.join(D,'deck.json'),'w'),indent=1,ensure_ascii=False)
print(len(deck['order']),'slides')

import p1gifted; p1gifted.apply(D,3)
import p1gaps; p1gaps.apply(D,3)
import p1fix; p1fix.finish(D,3,{'l3-ws2':'58–68 MIN'})
import p1neutral; p1neutral.apply(D,3)
import p1budget; p1budget.apply(D,3)
