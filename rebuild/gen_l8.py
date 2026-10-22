import json,os,sys
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,H)
from slidekit import *
D=os.path.join(H,'..','split','l8','project'); S={}
def put(i,h): S[i]=h
RED='#D64545'; GOLD='#8A6A10'

# ---------- small SVG helpers (slidekit style) ----------
def SV(w,h,body,label): return f'<svg aria-label="{E(label)}" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="width:{w}px;height:{h}px">{body}</svg>'
def R(x,y,w,h,fill=WHITE,stroke=NAVY,sw=4,rx=0,dash=''): return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{dash}/>'
def T(x,y,s,size=40,fill=NAVY,weight=700,anchor='middle',extra=''): return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" fill="{fill}" font-family="Fredoka, Arial"{extra}>{E(str(s))}</text>'
def CI(x,y,r,fill=WHITE,stroke=NAVY,sw=4,op=''): return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}"{op} stroke="{stroke}" stroke-width="{sw}"/>'
def TICK(x,y,s=24,col=TEAL,sw=9): return f'<path d="M{x-s} {y} L{x-s/3:.1f} {y+s*0.7:.1f} L{x+s} {y-s*0.8:.1f}" fill="none" stroke="{col}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"/>'
def CROSS(x,y,s=20,col=RED,sw=8): return f'<path d="M{x-s} {y-s} L{x+s} {y+s} M{x+s} {y-s} L{x-s} {y+s}" fill="none" stroke="{col}" stroke-width="{sw}" stroke-linecap="round"/>'
def ostep(left,top,n,text,ov=None,ovw=0,ovh=0,dx=0,dy=0,tw=1000,size=34,build='fade'):
    """One click = overlay marks (same left/top as the base picture) + the step text box beside it."""
    lab=f'<span style="color:{TEAL};font-weight:800">Step {n}.</span>  ' if n else ''
    box=f'<div style="margin-top:{dy}px;width:{tw}px;box-sizing:border-box;background:{WHITE};border-radius:20px;padding:16px 28px;flex:none"><p style="font-size:{size}px;font-weight:600;line-height:1.3">{lab}{E(text)}</p></div>'
    o=f'<div style="width:{ovw}px;height:{ovh}px;flex:none">{ov or ""}</div>'
    return pin(left,top,dx+tw,f'<div style="display:flex;align-items:flex-start;gap:{dx-ovw}px">{o}{box}</div>',build)
def soft(left,top,width,text,size=34,build='fade'): return pin(left,top,width-56,p(text,size,700),build,SOFT,20,'18px 28px')
def stitle(t,size=34): return p(t,size,600,MUTED)

# logic grid drawn as a table: label column + header row; marks drawn as separate overlay layers
LW,CW,HH,RH=200,160,80,90
def grid_base(rows,cols,label):
    w=LW+CW*len(cols); h=HH+RH*len(rows); b=R(2,2,w-4,h-4,WHITE,NAVY,4,12)+R(LW,2,w-LW-2,HH-2,YEL,'none',0)
    d=''.join(f'M{LW+CW*i} 2 V{h-2} ' for i in range(len(cols)))+''.join(f'M2 {HH+RH*j} H{w-2} ' for j in range(len(rows)))
    b+=f'<path d="{d}" stroke="{NAVY}" stroke-width="3" fill="none"/>'
    b+=''.join(T(LW+CW*i+CW/2,HH/2+12,c,34,NAVY,800) for i,c in enumerate(cols))+''.join(T(LW/2,HH+RH*j+RH/2+12,r,36,NAVY,800) for j,r in enumerate(rows))
    return SV(w,h,b,label),w,h
def grid_marks(rows,cols,marks,label):
    w=LW+CW*len(cols); h=HH+RH*len(rows); b=''
    for (r,c),m in marks.items():
        x=LW+CW*cols.index(c)+CW/2; y=HH+RH*rows.index(r)+RH/2
        b+=TICK(x,y+4) if m=='y' else CROSS(x,y)
    return SV(w,h,b,label)

# ---------- 3. quick questions (real questions, linked to Guess my number) ----------
qs=[('1.','My number is from 1 to 20. It is more than 10 and it is even. What could it be?','12, 14, 16, 18 or 20'),('2.','It is also less than 15. What could it be now?','12 or 14'),('3.','A new number: less than 20, odd, and you say it when counting in 5s.','5 or 15'),('4.','Which is a better first question: "Is it 7?" or "Is it more than 10?"','"More than 10?"')]
body=h2('Quick questions')+''.join(qrow(128,250+i*160,1250,a,b) for i,(a,b,c) in enumerate(qs))+''.join(answer(1420,250+i*160,372,c) for i,(a,b,c) in enumerate(qs))
put('l8-warm2',sec('l8-warm2','5–10 MIN',body,'Minutes 5 to 10. These follow on from Guess my number. Read each question aloud, give thinking time, take answers on whiteboards, then click. 1) More than 10 means 11 to 20; even ones are 12, 14, 16, 18, 20. 2) Of those, less than 15: 12 and 14. Point out that each clue crosses out more numbers. 3) Counting in 5s: 5, 10, 15 (20 is not less than 20); odd: 5 and 15. 4) "Is it 7?" usually crosses out only one number. "Is it more than 10?" crosses out about half the numbers, whatever the answer. Good questions cross out lots of numbers.'))

# ---------- 6. teach: one tick in every row and column ----------
rows=['Zoe','Kai','Lin']; cols=['apple','banana','pear']
base,gw,gh=grid_base(rows,cols,'Logic grid: Zoe, Kai and Lin against apple, banana and pear')
ov1=grid_marks(rows,cols,{('Kai','banana'):'y'},'tick: Kai has the banana')
ov2=grid_marks(rows,cols,{('Kai','apple'):'n',('Kai','pear'):'n'},'crosses in the rest of Kai\'s row')
ov3=grid_marks(rows,cols,{('Zoe','banana'):'n',('Lin','banana'):'n'},'crosses in the rest of the banana column')
body=h2('Logic grids: one tick in each row and column')+stitle('Zoe, Kai and Lin each have a different fruit: an apple, a banana or a pear.')
body+=pin(128,310,gw,base)
body+=ostep(128,310,1,'Clue: Kai has the banana. Put a ✓.',ov1,gw,gh,dx=gw+50,dy=0,tw=1664-gw-50)
body+=ostep(128,310,2,'Kai has only one fruit, so cross out the rest of his row.',ov2,gw,gh,dx=gw+50,dy=110,tw=1664-gw-50)
body+=ostep(128,310,3,'Nobody else has the banana, so cross out the rest of its column.',ov3,gw,gh,dx=gw+50,dy=240,tw=1664-gw-50)
body+=soft(128,710,1664,'Each child has a DIFFERENT fruit. So every row and every column ends with exactly one ✓.',36)
put('l8-teach1',sec('l8-teach1','25–27 MIN',body,'Teach. Read the sentence and stress "different": no two children have the same fruit. Click 1: tick Kai and banana. Ask: "Can Kai also have the apple?" No, he has only one fruit. Click 2: cross out the rest of his row. Ask: "Can Zoe have the banana?" No, Kai has it. Click 3: cross out the rest of the column. Click 4: the why. Think-aloud: "Every time I put a tick, I get crosses for free: the rest of that row and the rest of that column. Every time I put a cross, I check whether a row or column now has only one empty box left."'))

# ---------- 7. worked example: drinks ----------
rows=['Tia','Sam','Raj']; cols=['milk','juice','water']
base,gw,gh=grid_base(rows,cols,'Logic grid: Tia, Sam and Raj against milk, juice and water')
m1=grid_marks(rows,cols,{('Tia','milk'):'n',('Sam','milk'):'n',('Sam','juice'):'n'},'crosses from the clues')
m2=grid_marks(rows,cols,{('Sam','water'):'y',('Tia','water'):'n',('Raj','water'):'n'},'Sam water ticked, rest of water column crossed')
m3=grid_marks(rows,cols,{('Tia','juice'):'y',('Raj','juice'):'n'},'Tia juice ticked, Raj juice crossed')
m4=grid_marks(rows,cols,{('Raj','milk'):'y'},'Raj milk ticked')
body=h2('Worked example: who drinks what?')+stitle('Tia, Sam and Raj each drink a different drink: milk, juice or water.')
body+=pin(128,300,1664,p('Clue 1: Tia does not drink milk.      Clue 2: Sam does not drink milk or juice.',36,700),None,WHITE,20,'18px 28px').replace('width:1664px','width:1608px')
G=410; tw=1664-gw-50
body+=pin(128,G,gw,base)
for k,(t,m) in enumerate([('Use the clues: cross out Tia–milk, Sam–milk and Sam–juice.',m1),('Sam has only water left: ✓. Cross out the rest of the water column.',m2),('Now Tia has only juice left: ✓. Cross out Raj–juice.',m3),('Raj has milk ✓. Check both clues again.',m4)]):
    body+=ostep(128,G,k+1,t,m,gw,gh,dx=gw+50,dy=k*122,tw=tw,size=32)
put('l8-we1',sec('l8-we1','27–29 MIN',body,'Click to reveal each step; ask the group what to write before each click. Think-aloud (from the tutor script): "Tia does not drink milk. Sam does not drink milk or juice. I put a cross where it cannot be. Sam cannot have milk or juice, so Sam has water. Now Tia cannot have milk and water is taken, so Tia has juice. Raj has milk." Stress that the puzzle only works because each child drinks a DIFFERENT drink. Ask: "Which row or column has only one empty box left?" That is always the next place to look.'))

# ---------- 8. your turn: hats ----------
body=h2('Your turn: hats')+stitle('Kim, Lee and Max each wear a different hat: red, blue or green. Draw a grid on your whiteboard.')
body+=qrow(128,310,1608,'Clue 1:','Lee’s hat is not red and not blue.',40)+qrow(128,420,1608,'Clue 2:','Kim’s hat is not red.',40)
body+=answer(128,560,1610,'Lee: green  (clue 1 leaves only green)')+answer(128,670,1610,'Kim: blue  (not red, and green is taken)')+answer(128,780,1610,'Max: red  (the only hat left)')
put('l8-try1',sec('l8-try1','29–30 MIN',body,'Children draw a 3 by 3 grid (names down the side, hats across the top) and fill it in. Click for each answer after a child explains. Lee: clue 1 crosses out red and blue, so green. Then cross out green for Kim and Max. Kim: not red (clue 2) and not green, so blue. Max: red. Check each clue again. Watch for children who stop after Lee: ask "Which row has only one empty box now?"'))

# ---------- 9. worked example: Venn diagram (numbers 10 to 20) ----------
VW,VH=1000,560
vb=(R(4,4,VW-8,VH-8,WHITE,NAVY,3,12)+CI(380,300,200,TEAL,TEAL,4,' fill-opacity="0.15"')+CI(620,300,200,YEL,'#C9971F',4,' fill-opacity="0.3"')
    +T(300,70,'less than 15',34,TEAL,800)+T(700,70,'even',34,GOLD,800))
base=SV(VW,VH,vb,'Venn diagram: loop for numbers less than 15, loop for even numbers')
def nums(pos,label): return SV(VW,VH,''.join(T(x,y,n,42,NAVY,800) for n,x,y in pos),label)
v1=nums([(10,500,250),(12,500,315),(14,500,380)],'10, 12, 14 in the middle')
v2=nums([(11,290,280),(13,290,350)],'11 and 13 in the less-than-15 part only')
v3=nums([(16,720,245),(18,720,315),(20,720,385)],'16, 18, 20 in the even part only')
v4=nums([(15,80,525),(17,150,525),(19,220,525)],'15, 17, 19 outside both loops')
body=h2('Worked example: sort into a two-loop picture')+stitle('Numbers 10 to 20. Test every number with BOTH rules.')
tw=1664-VW-50
for k,(t,v) in enumerate([('Both rules: 10, 12, 14 go in the middle.',v1),('Less than 15 only: 11, 13.',v2),('Even only: 16, 18, 20.',v3),('Neither rule: 15, 17, 19 go outside both loops.',v4)]):
    body+=ostep(128,300,k+1,t,v,VW,VH,dx=VW+50,dy=k*140,tw=tw,size=32) if k else pin(128,300,VW,base)+ostep(128,300,k+1,t,v,VW,VH,dx=VW+50,dy=0,tw=tw,size=32)
put('l8-we2',sec('l8-we2','30–32 MIN',body,'Click to fill each part. For every number ask two questions out loud: "Is it less than 15? Is it even?" Two yeses: the middle. One yes: that loop only. Two noes: outside. Think-aloud: "12. Is it less than 15? Yes. Is it even? Yes. Both, so it goes where the loops overlap. 16. Less than 15? No. Even? Yes. So it goes in the even loop, but not the middle. 15. Less than 15? No, it is equal to 15. Even? No. So it goes outside." Ask: "Why does 12 go in the middle?" (it follows both rules). Check: 3 + 2 + 3 + 3 = 11 numbers, the same as 10 to 20.'))

# ---------- 10. your turn: where does it go? ----------
put('l8-try2',try_slide('l8-try2','32–34 MIN','Your turn: where does it go?','Loop A: bigger than 10.     Loop B: numbers you say when counting in 5s.',[('a','Where does 15 go?','middle'),('b','Where does 5 go?','loop B only'),('c','Where does 12 go?','loop A only'),('d','Where does 7 go?','outside')],'Draw the two loops on the board. Children write the answer on whiteboards, then click. a) 15 is bigger than 10 AND we say it counting in 5s: middle. b) 5: we say it counting in 5s, but it is not bigger than 10: loop B only. c) 12 is bigger than 10, but we do not say it counting in 5s: loop A only. d) 7: neither, so outside both loops. Ask for a number that goes in the middle other than 15 (20, 25, 30 …).'))

# ---------- 11. key ----------
body=h2('Key idea: use what you know')+card(p('Every ✓ gives you crosses: the rest of its row and the rest of its column.',44,700))+card(p('The middle of a two-loop picture follows BOTH rules.',38,600,MUTED))
put('l8-key',sec('l8-key','34–35 MIN',body,'Say the key ideas together. Common mistakes to watch for during the worksheet: (1) Putting numbers in the middle of the Venn diagram that only fit one rule (for example 2 in the middle of "less than 6" and "odd"). (2) Giving up on the pets grid instead of using a cross to rule out. Before page 2 tell children: "Each child has a different pet." (3) Guessing a line-up without checking all the clues, or reading "behind" as "just behind". (4) In riddles, counting 20 or 40 as "between 20 and 40".'))

# ---------- teach before page 1: order from clues (ladder) ----------
LWd,LHd=520,540
slots=[20,150,280,410]
lb=(f'<path d="M50 {LHd-20} V24" stroke="{TEAL}" stroke-width="6"/><polygon points="50,6 34,36 66,36" fill="{TEAL}"/>'
    +T(28,150,'longer',28,TEAL,800,'middle',' transform="rotate(-90 28 150)"')+T(28,420,'shorter',28,TEAL,800,'middle',' transform="rotate(-90 28 420)"')
    +''.join(R(110,y,380,100,'none','#9AA6C0',3,16,' stroke-dasharray="10 8"') for y in slots))
base=SV(LWd,LHd,lb,'Ladder with 4 empty places, longest at the top')
def lad(items,label): return SV(LWd,LHd,''.join(R(110,slots[s],380,100,SKY,NAVY,4,16)+T(300,slots[s]+64,n,44,NAVY,700) for n,s in items),label)
body=h2('Put things in order: draw a ladder')+stitle('Write them from longest to shortest.')
tw=1664-LWd-60
body+=pin(128,290,LWd,base)
body+=ostep(128,290,1,'Clue 1: the pencil is longer than the crayon. Pencil goes ABOVE crayon.',lad([('pencil',1),('crayon',2)],'pencil above crayon'),LWd,LHd,dx=LWd+60,dy=0,tw=tw,size=32)
body+=ostep(128,290,2,'Clue 2: the ruler is longer than the pencil. Ruler goes above pencil.',lad([('ruler',0)],'ruler at the top'),LWd,LHd,dx=LWd+60,dy=130,tw=tw,size=32)
body+=ostep(128,290,3,'Clue 3: the eraser is shorter than the crayon. Eraser goes below crayon.',lad([('eraser',3)],'eraser at the bottom'),LWd,LHd,dx=LWd+60,dy=260,tw=tw,size=32)
body+=answer(128+LWd+60,700,tw-52,'Longest to shortest: ruler, pencil, crayon, eraser')
put('l8-teachorder',sec('l8-teachorder','40–42 MIN',body,'Teach before worksheet page 1 (Q1 puts children, animals and ribbons in order). Draw the ladder on the board: longer at the top, shorter at the bottom. Click 1: "Longer than" means higher up. Leave a gap above and below, because more clues may come. Click 2 and 3: place each new thing next to the one it is compared with. Think-aloud: "The ruler is longer than the pencil, so the ruler goes above the pencil. The eraser is SHORTER than the crayon, so it goes below the crayon." Common mistake: writing the names in the order they appear in the clues. For heavier and lighter, or taller and shorter, use the same ladder.'))

put('l8-ws1',ws_preview('l8-ws1','42–52 MIN','Worksheet page 1: with your partner',[('Q1','Order from clues. Draw a ladder: tallest, heaviest or longest at the top.'),('Q2','Two-loop picture, numbers 1 to 10. Test every number with BOTH rules.')],'Stuck? Say each clue aloud and move the names up or down your ladder. Odd numbers end in 1, 3, 5, 7 or 9. Even numbers end in 0, 2, 4, 6 or 8.','Minutes 42 to 52. Walk around. Ask "How do you know?" before giving any help. For Q2, ask pairs to say the two questions for each number: "Is it less than 6? Is it odd?"'))
put('l8-ws1ans',check_slide('l8-ws1ans','52–54 MIN','Page 1: check together',[('Q1a, b','a) Tallest Ali, shortest Mei.   b) Heaviest cat, lightest hen.'),('Q1c','Yellow, red, blue, green'),('Q2','Middle: 1, 3, 5.     Less than 6 only: 2, 4.'),('Q2','Odd only: 7, 9.     Outside both: 6, 8, 10.'),('Q2b','1, 3 and 5 are less than 6 AND odd.')],'Click each answer after a pair explains. Q1c: yellow is longer than red, red is longer than blue, blue is longer than green. Q2: check that 6 is outside (it is not less than 6, and it is even). Q2b: they follow both rules, so they go where the loops overlap.',lw=240))

# ---------- teach before page 2: line-ups ----------
cx=[110,330,550,770]
lb=''.join(CI(x,110,70,WHITE,NAVY,4)+T(x,232,o,30,MUTED,800) for x,o in zip(cx,['1st','2nd','3rd','4th']))+T(110,28,'front',28,TEAL,800)+T(770,28,'back',28,TEAL,800)
LW2,LH2=900,245
base=SV(LW2,LH2,lb,'Four empty circles in a row from front to back')
def names(items,label): return SV(LW2,LH2,''.join(CI(cx[i],110,70,SKY,NAVY,4)+T(cx[i],124,n,40,NAVY,700) for n,i in items),label)
tw=1664-LW2-50
body=h2('Line-ups: draw the row')+card(p('Tom, Kim, Sue and Raj stand in a line. Sue is last. Tom is just in front of Sue. Kim is not first.',38,700),extra='padding:22px 36px')
body+=pin(128,390,LW2,base)
for k,(t,it) in enumerate([('Sue is last: she goes in the 4th circle.',[('Sue',3)]),('“Just in front of Sue” means right next to her: Tom is 3rd.',[('Tom',2)]),('Kim is not first, so Kim is 2nd. Raj is 1st.',[('Kim',1),('Raj',0)]),('Check every clue ✓  Raj, Kim, Tom, Sue.',[])]):
    body+=ostep(128,390,k+1,t,names(it,'names placed') if it else None,LW2,LH2,dx=LW2+50,dy=k*125,tw=tw,size=32)
body+=qrow(128,670,840,'Your turn:','Ali, Ben and Cara are in a line. Cara is in the middle. Ali is not first. Who is first?',32)+answer(128,830,300,'Ben')
put('l8-teachline',sec('l8-teachline','54–56 MIN',body,'Teach before worksheet page 2 (Q4 is a line-up of 4 children). Draw 4 circles on the board and label the front. Think-aloud: "I start with the clue that tells me something for sure: Sue is last. Then the clue that uses Sue: just in front of Sue means right next to her, so Tom is 3rd. Kim is not first, and the only places left are 1st and 2nd, so Kim is 2nd and Raj is 1st. Now I check every clue." Teach the words: "just in front of" or "just behind" means right next to; "in front of" or "behind" means somewhere before or after, not always next to. Your turn: Cara 2nd, Ali not 1st so Ali 3rd, Ben 1st.'))

# ---------- teach before page 2: number riddles ----------
body=h2('Number riddles: list, then cross out')+card(p('I have 2 digits. My digits add up to 4. I am bigger than 20. I am odd. Who am I?',40,700),extra='padding:22px 36px')
for k,t in enumerate(['Clue 1: list every 2-digit number whose digits add up to 4:  13, 22, 31, 40','Clue 2: bigger than 20. Cross out 13.  22, 31, 40 are left.','Clue 3: odd. Cross out 22 and 40.  I am 31.','Check 31 with every clue:  3 + 1 = 4,  bigger than 20,  odd ✓']):
    body+=step(k+1,E(t),top=370+k*105,size=32,build=None)
body+=qrow(128,800,1250,'Your turn:','Between 20 and 30, odd, and you say it counting in 5s.',32)+answer(1420,800,372,'25')
put('l8-teachriddle',sec('l8-teachriddle','56–57 MIN',body,'Teach before worksheet page 2 (Q5 has one number riddle, marked "if you have time"; two more are Think harder T5). All the steps are already showing: give this slide 30 seconds. Say: "Clue 1 gives a short list. Each later clue crosses one out." Your turn: only 25 is between 20 and 30, odd and said when counting in 5s ("between" leaves out 20 and 30).'))

# ---------- teach before page 2: odd one out ----------
body=h2('Odd one out: what do the others share?')+card(p('Which one does NOT belong?      5,     10,     12,     15',44,700),extra='padding:22px 36px')
for k,t in enumerate(['5, 10 and 15 are numbers we say when counting in 5s. 12 is not, so 12 does not belong.','A second reason: 5 is the only number with 1 digit. So 5 can be the odd one out too!','Say it like this:  “___ does not belong because ___.”']):
    body+=step(k+1,E(t),top=360+k*120,size=32,build=None)
body+=qrow(128,730,1250,'Your turn:','4,    8,    10,    13',36)+answer(1420,730,372,'13: the only odd number')
put('l8-teachodd',sec('l8-teachodd','57–58 MIN',body,'Teach before worksheet page 2 (Q6 asks for an odd one out and a second reason, marked "if you have time"). All the steps are already showing: give this slide 30 seconds. Say: "Three share something and one does not. 12 does not belong. A second reason: 5 has only one digit." Your turn: 13, the only odd number (also accept 10, the only one we say counting in 5s).'))

put('l8-ws2',ws_preview('l8-ws2','58–68 MIN','Worksheet page 2: on your own',[('Q3','Pets grid. Each child has a different pet. Tick where it fits, cross where it cannot.'),('Q4','Line-up. Draw 4 circles. Put in the sure ones first.'),('Q5','Number riddles. List what fits one clue, then cross out.'),('Q6','Odd one out. Find a reason, then a second reason.')],'Finished early? Stretch and Challenge come next.','Children work alone. Q3 says each child has a DIFFERENT pet: read that sentence aloud before they start. In Q4, "in front of" means somewhere in front, not always right in front. Note who needs a short catch-up next lesson.'))
put('l8-ws2ans',check_slide('l8-ws2ans','68–70 MIN','Page 2: check together',[('Q3','Ali: fish.    Mei: cat.    Ben: dog.'),('Q4','1st Mei,   2nd Ali,   3rd Ben,   4th Sam'),('Q5','a) 15,    b) 30,    c) 14'),('Q6','11: we do not say it counting in 3s.  Or 6: the only even number.')],'Click each answer after a child explains. Q3: Ali has no cat and no dog, so fish. Mei has no dog, and the fish is taken, so cat. Ben has the dog. Q4: Mei is 1st; Ali is in front of Ben and Ben is in front of Sam, so the order of the last three is Ali, Ben, Sam. Q5b: 20 and 40 are not between 20 and 40, so 30. Q5c: 14 (1 + 4 = 5, less than 20). Q6: also accept "11 is the only number with 2 digits".'))

# ---------- stretch (new items) ----------
st=[('1.','Ali, Ben, Cara and Dan each have a different pet: a cat, a dog, a fish or a rabbit. Cara has the dog or the fish. Cara does not have the dog. Dan does not have the cat or the rabbit. Ali does not have the cat. Who has which pet?'),('2.','Five children stand in a line. Ali is in the middle. Ben is just in front of Ali. Cara is last. Dan is not first. Where is Eve?'),('3.','Numbers 1 to 30: which do you say when counting in 2s AND when counting in 5s?')]
put('l8-stretch',sec('l8-stretch','For early finishers',h2('Stretch')+''.join(card(p(f'<span style="color:#1F7A6F">{a}</span>  {E(b)}',36,600,raw=True)) for a,b in st),'For children who finish early. Answers: 1) Cara fish (dog or fish, not dog). Dan: not cat, not rabbit, fish taken, so dog. Ali: not cat, so rabbit. Ben: cat. 2) Eve is first. Ali is 3rd (the middle of 5), Ben 2nd, Cara 5th; 1st and 4th are left for Dan and Eve, and Dan is not first, so Dan 4th and Eve 1st: Eve, Ben, Ali, Dan, Cara. 3) 10, 20 and 30.'))

# ---------- challenge (wording: "numbers you say when counting in 3s", not "times table") ----------
ch=[('1.','A secret number is between 10 and 30. It is even, and you say it when counting in 3s. It is 2 more than a number you say when counting in 5s. What is it?'),('2.','Numbers 1 to 20. Sort them into a two-loop picture with the loops "I say it counting in 2s" and "I say it counting in 3s". How many go in each part?')]
put('l8-challenge',sec('l8-challenge','65–80 MIN',h2('Challenge')+''.join(card(p(f'<span style="color:#1F7A6F">{a}</span>  {E(b)}',36,600,raw=True)) for a,b in ch),'Use as a pair challenge or in talk time. Ask for the reason every time. Pairs try first, then the "see it" slide, then the walk-through. Answers: 1) 12.  2) Counting in 2s only: 7. Counting in 3s only: 3. Both: 3 (6, 12, 18). Neither: 7.'))

# ---------- chdiag: same pictures, new wording ----------
cd=os.path.join(D,'slides','l8-chdiag.html'); s=open(cd).read()
for a,b in [('even AND in the 3 times table','even AND said counting in 3s'),('2 more than a number in the 5 times table','2 more than a number said counting in 5s'),('>multiples of 2<','>counting in 2s<'),('>multiples of 3<','>counting in 3s<'),('>2 only<','>2s only<'),('>3 only<','>3s only<')]:
    s=s.replace(a,b)
assert 'times table' not in s and 'multiples' not in s
open(cd,'w').write(s)

# ---------- challenge walk-through ----------
body=h2('Challenge: walk-through')+pin(128,250,780,p('Q1: cross out, clue by clue',38,800,TEAL))
for i,t in enumerate(['Even, said counting in 3s, between 10 and 30: 12, 18, 24','12 = 10 + 2. We say 10 counting in 5s ✓','18 = 16 + 2. We do not say 16 counting in 5s.','24 = 22 + 2. We do not say 22 counting in 5s.','The secret number is 12 ✓']): body+=pin(128,[330,455,570,685,800][i],780,p(t,32),'rise',WHITE)
body+=pin(992,250,800,p('Q2: test each number with both rules',38,800,TEAL))
for i,t in enumerate(['Both: 6, 12, 18  →  3','2s only: 2, 4, 8, 10, 14, 16, 20  →  7','3s only: 3, 9, 15  →  3','Neither: 1, 5, 7, 11, 13, 17, 19  →  7.  Check: 3 + 7 + 3 + 7 = 20 ✓']): body+=pin(992,330+i*115,800,p(t,32),'rise',WHITE)
put('l8-chwalk',sec('l8-chwalk','Challenge',body,'Use after pairs have tried. Q1: start with the clue that gives the shortest list (even numbers we say counting in 3s: 6, 12, 18, 24, 30; between 10 and 30 leaves 12, 18, 24). Then test each with the last clue: take away 2 and ask "Do we say it counting in 5s?" Q2: test every number from 1 to 20 with two questions, exactly like the Venn diagram in the lesson. The check (the four parts add up to 20) shows no number was missed.'))


# ---------- aria-labels on the kept diagrams (pictures unchanged) ----------
def label_svgs(sid,labels):
    f=os.path.join(D,'slides',sid+'.html'); s=open(f).read(); parts=s.split('<svg ')
    for i,l in enumerate(labels):
        if i+1<len(parts) and not parts[i+1].startswith('aria-label'): parts[i+1]=f'aria-label="{l}" '+parts[i+1]
    open(f,'w').write('<svg '.join(parts))
label_svgs('l8-explore1',['Two overlapping loops: red buttons and buttons with 2 holes'])
label_svgs('l8-chdiag',['Three clues for the secret number and the numbers 10 to 30','Venn diagram for numbers 1 to 20: counting in 2s and counting in 3s'])
# ---------- write ----------
for i,h in S.items(): open(os.path.join(D,'slides',i+'.html'),'w').write(h)
for old in ['l8-mini1','l8-mini2']:
    f=os.path.join(D,'slides',old+'.html')
    if os.path.exists(f): os.remove(f)
t=os.path.join(D,'slides','l8-title.html'); s=open(t).read(); s=s.replace('mini-lesson 25 to 35, brain break 35 to 40, worksheet 40 to 70','teaching 25 to 35 (click to reveal each step and answer), brain break 35 to 40, worksheet 40 to 70 with short teaching before each page and a check-together slide after it'); open(t,'w').write(s)
deck=json.load(open(os.path.join(D,'deck.json')))
deck['order']=['l8-title','l8-warm1','l8-warm2','l8-explore1','l8-explore2','l8-teach1','l8-we1','l8-try1','l8-we2','l8-try2','l8-key','l8-break','l8-teachorder','l8-ws1','l8-ws1ans','l8-teachline','l8-teachriddle','l8-teachodd','l8-ws2','l8-ws2ans','l8-stretch','l8-challenge','l8-chdiag','l8-chwalk','l8-talk','l8-exit']
deck['sections']={'s1':{'description':'Warm-up and explore','start':'l8-title'},'s2':{'description':'Teach: logic grids and Venn diagrams','start':'l8-teach1'},'s3':{'description':'Worksheet with teaching before each page','start':'l8-break'},'s4':{'description':'Stretch, challenge, talk and exit','start':'l8-stretch'}}
json.dump(deck,open(os.path.join(D,'deck.json'),'w'),indent=1,ensure_ascii=False)
missing=[i for i in deck['order'] if not os.path.exists(os.path.join(D,'slides',i+'.html'))]
print(len(deck['order']),'slides; wrote',len(S),'missing',missing)

import p1gifted; p1gifted.apply(D,8)
import p1gaps; p1gaps.apply(D,8)
import p1fix
p1fix.sub_all(D,[('the Venn diagram in the lesson','the two-loop picture in the lesson'),('Putting numbers in the middle of the Venn diagram','Putting numbers in the middle of the two-loop picture'),('(Venn diagram)',''),('in a Venn diagram','in a two-loop picture'),('with a Venn diagram','with a two-loop picture')])
p1fix.finish(D,8,{})
import p1neutral; p1neutral.apply(D,8)
import p1budget; p1budget.apply(D,8)
