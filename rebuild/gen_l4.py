import json,os,sys
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,H)
from slidekit import *
D=os.path.join(H,'..','split','l4','project'); S={}
def put(i,h): S[i]=h

# ---- local helpers ----
RED='#D64545'; BLUE='#3A6EA5'; GOLD='#E0A100'
def beads(cols,layer='base',ring=(),core=3,w=1664,h=250,gap=150,x0=80):
    """layer: base (beads + place numbers), brackets (core brackets only), ring (rings on the given places only)."""
    n=len(cols)
    s=f'<svg aria-label="Bead pattern" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="width:{w}px;height:{h}px">'
    for i,c in enumerate(cols):
        x=x0+i*gap
        if layer=='base':
            s+=f'<circle cx="{x}" cy="115" r="44" fill="{RED if c=="R" else BLUE}" stroke="{NAVY}" stroke-width="4"/><text x="{x}" y="127" font-size="34" font-weight="800" text-anchor="middle" fill="{WHITE}" font-family="Nunito Sans, Arial">{c}</text>'
            s+=f'<text x="{x}" y="225" font-size="38" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="Fredoka, Arial">{i+1}</text>'
        if layer=='ring' and i+1 in ring:
            s+=f'<circle cx="{x}" cy="115" r="56" fill="none" stroke="{YEL}" stroke-width="10"/><circle cx="{x}" cy="212" r="30" fill="{YEL}" stroke="{NAVY}" stroke-width="3"/><text x="{x}" y="225" font-size="38" font-weight="800" text-anchor="middle" fill="{NAVY}" font-family="Fredoka, Arial">{i+1}</text>'
    if layer=='brackets':
        for k in range(0,n,core):
            a=x0+k*gap-55; b=x0+min(k+core-1,n-1)*gap+55
            s+=f'<path d="M{a} 62 L{a} 30 L{b} 30 L{b} 62" fill="none" stroke="{TEAL}" stroke-width="6" stroke-linejoin="round"/>'
    return s+'</svg>'
def squares(n,size=90):
    w=40+n*size; h=size+40
    s=f'<svg aria-label="{n} squares made of sticks" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="width:{w}px;height:{h}px">'
    for i in range(n):
        x=20+i*size; y=20; new=(i==n-1 and n>1); c=GOLD if new else NAVY
        segs=[(x,y,x+size,y),(x,y+size,x+size,y+size),(x+size,y,x+size,y+size)]
        if i==0: segs.append((x,y,x,y+size))
        for (a,b,c2,d) in segs: s+=f'<line x1="{a+(6 if a!=c2 else 0)}" y1="{b+(6 if b!=d else 0)}" x2="{c2-(6 if a!=c2 else 0)}" y2="{d-(6 if b!=d else 0)}" stroke="{c}" stroke-width="12" stroke-linecap="round"/>'
    return s+'</svg>'
def rows_slide(sid,time,title,sub,rows,notes,top=340,gap=150,size=40,aw=372):
    body=h2(title)+(p(sub,34,600,MUTED) if sub else '')
    for i,(a,b,c) in enumerate(rows):
        body+=qrow(128,top+i*gap,1664-aw-48,a,b,size)+answer(1792-aw,top+i*gap,aw,c)
    return sec(sid,time,body,notes)

# ---- warm2: click answers ----
qs=[('1.','clap, snap, stomp, clap, snap, stomp … 7th action?','clap'),('2.','What is the 8th action?','snap'),('3.','What is the 9th action?','stomp'),('4.','What is the 10th action?','clap')]
body=h2('Quick questions')+''.join(qrow(128,260+i*150,1250,a,b) for i,(a,b,c) in enumerate(qs))+''.join(answer(1420,260+i*150,372,c) for i,(a,b,c) in enumerate(qs))
put('l4-warm2',sec('l4-warm2','5–10 MIN',body,'Minutes 5 to 10. Do the actions together up to the 6th, then ask each question. Give thinking time, take answers, then click to show. Ask: "How did you know the 9th is stomp?" Listen for "stomp is always 3rd, 6th, 9th". Answers: 1) clap  2) snap  3) stomp  4) clap.'))

# ---- teach 1: find the core ----
B=list('RBBRBBRBB')
body=h2('Find the core')+card(p('A repeating pattern has a core: the part that repeats.',40,700))
body+=pin(128,380,1664,beads(B),None)
body+=pin(128,380,1664,beads(B,'brackets'),'fade')
body+=pin(128,380,1664,beads(B,'ring',(3,6,9)),'fade')
body+=pin(128,680,1664,p('Every core ends on 3, 6, 9 … : the numbers we say when we count in 3s. The bead there is always blue, the last bead of the core.',36,700),'fade',SOFT,20,'22px 30px')
put('l4-teach1',sec('l4-teach1','25–27 MIN',body,'Teach. Lay out real beads or cubes if you have them. Ask: "Which part keeps repeating?" Click 1: brackets around each core. "The core is red, blue, blue. It has 3 beads." Click 2: ring places 3, 6 and 9. Ask: "What do you notice about these numbers?" (we say them when we count in 3s). Click 3: the rule. Think-aloud: "I look for the part that repeats. That part is the core: red, blue, blue. It has 3 beads, so every core ends on a number I say when I count in 3s: 3, 6, 9, 12 … The bead there is always the last bead of the core, blue." Do not use groups or sharing language; children just count in 3s.'))

# ---- worked example 1 ----
body=h2('Worked example: the 20th bead')+card(p('red, blue, blue, red, blue, blue …  What colour is the 20th bead?',44,700))
body+=step(1,'The core has 3 beads, so count in 3s:  3, 6, 9, 12, 15, 18.',top=420,size=36)
body+=step(2,'18 is a 3s number, so the 18th bead ends a core: blue.',top=530,size=36)
body+=step(3,'Start the core again:  19th red,  20th blue.',top=640,size=36)
body+=step(4,'Check: the 21st ends the next core (21 is a 3s number). 19 red, 20 blue, 21 blue ✓',top=750,size=36)
put('l4-we1',sec('l4-we1','27–29 MIN',body,'Click through the steps; ask the group to predict each one first. Count in 3s on fingers together and stop before passing 20. Think-aloud: "The core has 3 beads, so I count in 3s: 3, 6, 9, 12, 15, 18. The next one, 21, is too far. So the 18th bead is the end of a core, a blue bead. Then I start the core again: 19 is red, 20 is blue." Common mistake: starting the core again at 20 and saying red. Point to 18, 19, 20 on a number strip.'))

# ---- try 1 ----
put('l4-try1',rows_slide('l4-try1','29–30 MIN','Your turn: whiteboards','Find the core. Count in its size. Then count on.',[('a','red, blue, blue … What colour is the 14th bead?','blue'),('b','red, blue, blue … What colour is the 22nd bead?','red'),('c','cat, dog, dog, fish, cat, dog, dog, fish … 10th?','dog')],'Whiteboards. a) 3, 6, 9, 12: the 12th is blue and ends a core; 13th red, 14th blue. b) 21 is a 3s number, so the 21st ends a core; the 22nd starts again: red. c) The core has 4 (cat, dog, dog, fish), so count in 4s: 4, 8. The 8th is fish; 9th cat, 10th dog. Ask a child to explain c: "Why did you count in 4s this time?"',size=36))

# ---- teach 2: growing pattern ----
body=h2('Growing patterns: what is added?')+card(p('Make squares in a row with sticks. How many sticks does each new square need?',40,700))
for i,(x,n,cap) in enumerate([(128,1,'1 square: 4 sticks'),(480,2,'2 squares: 7 sticks'),(880,3,'3 squares: 10 sticks')]):
    body+=pin(x,380,[300,350,380][i],squares(n)+p(cap,30,800),'rise',WHITE,20,'16px 22px')
body+=pin(1340,380,452,p('Each new square shares a side with the one before. It needs only 3 new sticks.',32,700),'fade',SOFT,20,'20px 24px')
W=[220]+[120]*5
body+=trow(128,640,['Squares','1','2','3','4','5'],W,None,True)
body+=trow(128,730,['Sticks','4','7','10','13','16'],W,'rise')
body+=pin(1180,660,612,p('Rule: add 3 each time.',38,800),'pop',YEL,20,'20px 26px')
put('l4-teach2',sec('l4-teach2','30–32 MIN',body,'Teach. Build it with real sticks if you can. Click to show 1, 2 and 3 squares; the gold sticks are the new ones. Ask before click 4: "Why only 3 new sticks, not 4?" Let a child point to the shared side. Then fill the table and say the rule. Think-aloud: "One square needs 4 sticks. When I add a square, it shares a side with the last one, so I only need 3 new sticks. 4, 7, 10, 13, 16. The rule is add 3." The worksheet uses triangles, so do not do triangles here.'))

# ---- worked example 2: work backwards by extending the table ----
W7=[220]+[110]*7
body=h2('Work backwards: keep the table going')+card(p('How many squares in a row can you make with 22 sticks?',44,700))
body+=trow(128,370,['Squares','1','2','3','4','5','6','7'],W7,None,True)
body+=step(1,'Keep the table going. Add 3 each time until we reach 22.',top=560,size=36)
body+=trow(128,460,['Sticks','4','7','10','13','16','19','22'],W7,'rise')
body+=step(2,'22 sticks is under 7 squares.  So 7 squares.',top=670,size=36)
body+=step(3,'Check: 4 + 3 + 3 + 3 + 3 + 3 + 3 = 22 ✓',top=780,size=36)
put('l4-we2',sec('l4-we2','32–33 MIN',body,'Click through. Think-aloud: "I do not know how many squares, but I know the rule: add 3. I keep the table going: 4, 7, 10, 13, 16, 19, 22. I stop when I reach 22. It is under 7 squares." Check: the first square takes 4 sticks, and each of the other 6 squares takes 3 more: 4 + 18 = 22. Ask: "What if I had 23 sticks?" (still 7 squares, and 1 stick left over).'))

# ---- try 2 ----
put('l4-try2',rows_slide('l4-try2','33–34 MIN','Your turn: a block tower','1 floor uses 3 blocks, 2 floors use 7, 3 floors use 11 …',[('a','What is added each time?','4 blocks'),('b','How many blocks for 5 floors?','19'),('c','How many floors use 23 blocks?','6 floors')],'Whiteboards. a) 3 to 7 is 4, 7 to 11 is 4: add 4. b) 11, 15, 19: 5 floors use 19 blocks. c) Keep going: 3, 7, 11, 15, 19, 23. 23 is under 6 floors. Ask: "How did you know when to stop?"',size=38))

# ---- key ----
body=h2('Key idea: core and growth')+card(p('Repeating: find the core. Count in its size to see where each core ends. Then count on.',44,700))+card(p('Growing: find what is added each time. Keep the table going, to find a far number or to work backwards.',38,600,MUTED))
put('l4-key',sec('l4-key','34–35 MIN',body,'Say the key idea together. Common mistakes to watch for during the worksheet: (1) Saying 3 more sticks each time because one triangle needs 3; ask them to point to the shared side. (2) Thinking the 30th shape is a circle because 30 starts with 3. (3) Q4: sharing 15 sticks into 3s to get 5 triangles; ask them to keep the table going instead. (4) Q2: drawing all 30 shapes; praise it, then ask for a quicker way.'))

# ---- worksheet page 1 ----
put('l4-ws1',ws_preview('l4-ws1','40–52 MIN','Worksheet page 1: with your partner',[('Q1','Shape pattern: draw the shapes in places 8 and 9.'),('Q2','Places 10, 12 and 30. Then explain how you know.')],'Ring the core first. How many shapes are in it? Count in that size.','Minutes 40 to 52. Pairs work together. Walk around and ask "Where does each core end?" For Q2c, ask pairs to explain without drawing all 30 shapes. Children who draw them all can check their reasoning with the drawing.'))
put('l4-ws1ans',check_slide('l4-ws1ans','52–54 MIN','Page 1: check together',[('Q1','Place 8: triangle.   Place 9: square.'),('Q2a','Place 10: circle'),('Q2b','Place 12: square'),('Q2c','Place 30: square'),('Q2d','We say 30 when we count in 3s, so the 30th shape ends a core: a square.')],'Click each answer after a pair explains theirs. The core is circle, triangle, square (3 shapes). 9 is a 3s number, so the 9th is a square and the 10th starts again: circle. 12 is a 3s number: square. 30 is a 3s number: square.'))

# ---- worksheet page 2 ----
put('l4-ws2',ws_preview('l4-ws2','54–66 MIN','Worksheet page 2: on your own',[('Q3','Ben\'s triangles: fill the table up to 10 triangles. Why only that many more sticks?'),('Q4','Ben has 15 sticks. How many triangles can he make?')],'Keep the table going until you reach the number of sticks. Finished early? Stretch and Challenge come next.','Children work alone. Q3 builds on the triangle explore. For Q4, check that children use their table (as with the squares) instead of sharing 15 into 3s. Note who needs a short catch-up next lesson.'))
put('l4-ws2ans',check_slide('l4-ws2ans','66–68 MIN','Page 2: check together',[('Q3a','3, 5, 7, 9, 11, 13, 15, 17, 19, 21'),('Q3b','2 more sticks each time'),('Q3c','The new triangle shares a side with the one before.'),('Q3d','21 sticks'),('Q4','7 triangles:  3, 5, 7, 9, 11, 13, 15')],'Click each answer after a child explains. Q3: start at 3 and add 2 for each new triangle. Q4: the table reaches 15 sticks at 7 triangles. Children who say 5 triangles have shared 15 into 3s: build 5 triangles in a row with them and count the sticks (11), then keep going.'))

# ---- stretch (new) ----
st=[('1.','star, circle, circle, triangle, star, circle, circle, triangle … What is the 23rd shape?'),('2.','Squares in a row need 4, 7, 10, … sticks. With 20 sticks, how many squares can you make? How many sticks are left over?'),('3.','A, B, B, C, A, B, B, C, … How many Bs are in the first 18 letters?')]
put('l4-stretch',sec('l4-stretch','For early finishers',h2('Stretch')+''.join(card(p(f'<span style="color:#1F7A6F">{a}</span>  {E(b)}',38,600,raw=True)) for a,b in st),'For children who finish early. Answers: 1) circle. The core has 4 shapes, so count in 4s: 4, 8, 12, 16, 20. The 20th is a triangle, the end of a core; 21st star, 22nd circle, 23rd circle. 2) 6 squares, 1 stick left over. The table goes 4, 7, 10, 13, 16, 19; 7 squares would need 22, which is too many; 20 − 19 = 1. 3) 9 Bs. Each core A, B, B, C has 2 Bs. 16 letters are 4 cores: 2, 4, 6, 8 Bs. The 17th is A and the 18th is B: 9.'))

# ---- challenge walk-through ----
body=h2('Challenge: walk-through')+pin(128,250,800,p('Q1: where do the greens sit?',38,800,TEAL))
for i,(t,bg) in enumerate([('The core has 5 beads. Green is the last one.',WHITE),('Greens are at 5, 10, 15 … 45: count in 5s.',WHITE),('That is 9 numbers. The 46th and 47th are red.',WHITE),('9 green beads',YEL)]): body+=pin(128,330+i*120,800,p(t,32),'rise',bg)
body+=pin(992,250,800,p('Q2: look at the jumps',38,800,TEAL))
for i,(t,bg) in enumerate([('Jumps: +2, +3, +4, +5. They grow by 1.',WHITE),('15 + 6 = 21,   21 + 7 = 28',WHITE),('28 + 8 = 36,   36 + 9 = 45',WHITE),('10th: 45 + 10 = 55',YEL)]): body+=pin(992,330+i*120,800,p(t,32),'rise',bg)
put('l4-chwalk',sec('l4-chwalk','Challenge',body,'Use after pairs have tried. Q1: count in 5s on fingers: 5, 10, 15, 20, 25, 30, 35, 40, 45 is 9 counts, so 9 green beads; 50 is past 47. Q2: the next two numbers are 21 and 28. Keep a list of places: 6th 21, 7th 28, 8th 36, 9th 45, 10th 55.'))

# ---- fix challenge notes (no groups/division language) ----
ch=os.path.join(D,'slides','l4-challenge.html'); s=open(ch).read()
s=s.replace('1) 9 green beads (9 full groups of 5 and 2 red beads left over).','1) 9 green beads. Green ends each core of 5, so the greens are at the numbers we say when counting in 5s: 5, 10, 15 … 45. That is 9; the 46th and 47th are red.'); open(ch,'w').write(s)

for i,h in S.items(): open(os.path.join(D,'slides',i+'.html'),'w').write(h)
for old in ['l4-mini1','l4-mini2']:
    f=os.path.join(D,'slides',old+'.html')
    if os.path.exists(f): os.remove(f)
t=os.path.join(D,'slides','l4-title.html'); s=open(t).read(); s=s.replace('mini-lesson 25 to 35, brain break 35 to 40, worksheet 40 to 70','teaching 25 to 35 (click to reveal each step and answer), brain break 35 to 40, worksheet 40 to 70 with a check-together slide after each page'); open(t,'w').write(s)
deck=json.load(open(os.path.join(D,'deck.json')))
deck['order']=['l4-title','l4-warm1','l4-warm2','l4-explore1','l4-explore2','l4-teach1','l4-we1','l4-try1','l4-teach2','l4-we2','l4-try2','l4-key','l4-break','l4-ws1','l4-ws1ans','l4-ws2','l4-ws2ans','l4-stretch','l4-challenge','l4-chdiag','l4-chwalk','l4-talk','l4-exit']
deck['sections']={'s1':{'description':'Warm-up and explore','start':'l4-title'},'s2':{'description':'Teach: find the core, grow a pattern, work backwards','start':'l4-teach1'},'s3':{'description':'Worksheet with a check after each page','start':'l4-break'},'s4':{'description':'Stretch, challenge, talk and exit','start':'l4-stretch'}}
json.dump(deck,open(os.path.join(D,'deck.json'),'w'),indent=1,ensure_ascii=False)
print(len(deck['order']),'slides')

import p1gifted; p1gifted.apply(D,4)
import p1gaps; p1gaps.apply(D,4)
import p1fix
p1fix.sub_all(D,[('21 matchsticks or straws per pair','21 straws, lolly sticks or paper strips per pair (never real matches)'),('growing matchstick pattern','growing stick pattern'),('matchstick','stick'),('straws, toothpicks or pencils','straws, lolly sticks or paper strips')])
p1fix.finish(D,4,{'l4-ws1':'40–54 MIN','l4-ws1ans':'54–56 MIN','l4-ws2':'56–68 MIN'})
import p1neutral; p1neutral.apply(D,4)

import p1round2; p1round2.apply(D,4)
import p1stories; p1stories.apply(D,4)
