import json,os,sys
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,H)
from slidekit import *
D=os.path.join(H,'..','split','l1','project'); S={}
def put(i,h): S[i]=h

# ---- local helpers ----
def track(nums,labels=None,only=None,w=1664,h=230,bw=170):
    """Number boxes with jump arcs. labels: text over each arc. only: draw just label k (for build-in overlays)."""
    n=len(nums); gap=(w-40-n*bw)/(n-1); xs=[20+i*(bw+gap) for i in range(n)]
    s=f'<svg aria-label="Number pattern {E(", ".join(str(x) for x in nums))}" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="width:{w}px;height:{h}px">'
    if only is None:
        for i,v in enumerate(nums):
            blank=v in ('?','__'); dash=' stroke-dasharray="12 8"' if blank else ''
            s+=f'<rect x="{xs[i]}" y="110" width="{bw}" height="110" rx="18" fill="{WHITE if blank else YEL}" stroke="{NAVY}" stroke-width="4"{dash}/><text x="{xs[i]+bw/2}" y="185" font-size="56" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="Fredoka, Arial">{E(str(v))}</text>'
            if i<n-1:
                a=xs[i]+bw/2; b=xs[i+1]+bw/2
                s+=f'<path d="M{a} 104 Q{(a+b)/2} 10 {b} 104" fill="none" stroke="{TEAL}" stroke-width="5"/><polygon points="{b},106 {b-20},92 {b-6},84" fill="{TEAL}"/>'
    if labels:
        for i,t in enumerate(labels):
            if only is not None and i!=only: continue
            a=xs[i]+bw/2; b=xs[i+1]+bw/2; m=(a+b)/2
            s+=f'<rect x="{m-55}" y="22" width="110" height="52" rx="14" fill="{CREAM}" stroke="{TEAL}" stroke-width="3"/><text x="{m}" y="60" font-size="36" font-weight="800" text-anchor="middle" fill="{TEAL}" font-family="Nunito Sans, Arial">{E(t)}</text>'
    return s+'</svg>'
def fill_box(nums,k,val,w=1664,h=230,bw=170):
    n=len(nums); gap=(w-40-n*bw)/(n-1); x=20+k*(bw+gap)
    return f'<svg aria-label="{E(val)}" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="width:{w}px;height:{h}px"><rect x="{x}" y="110" width="{bw}" height="110" rx="18" fill="{SKY}" stroke="{NAVY}" stroke-width="4"/><text x="{x+bw/2}" y="185" font-size="56" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="Fredoka, Arial">{E(val)}</text></svg>'
def rows_slide(sid,time,title,sub,rows,notes,top=340,gap=150,size=40,aw=372):
    body=h2(title)+(p(sub,34,600,MUTED) if sub else '')
    for i,(a,b,c) in enumerate(rows):
        body+=qrow(128,top+i*gap,1664-aw-48,a,b,size)+answer(1792-aw,top+i*gap,aw,c)
    return sec(sid,time,body,notes)

# ---- warm2: click answers ----
qs=[('1.','Count in 2s: 2, 4, 6, __','8'),('2.','Count in 5s: 5, 10, __, 20','15'),('3.','Count in 3s: 3, 6, 9, __','12'),('4.','Count back in 2s: 20, 18, __','16'),('5.','4 jumps of 5 or 4 jumps of 3: which goes further?','Jumps of 5')]
body=h2('Quick questions')+''.join(qrow(128,250+i*125,1250,a,b) for i,(a,b,c) in enumerate(qs))+''.join(answer(1420,250+i*125,372,c) for i,(a,b,c) in enumerate(qs))
put('l1-warm2',sec('l1-warm2','5–10 MIN',body,'Minutes 5 to 10. Read each question aloud, give thinking time, take answers, then click to show the answer. For 4 ask: "Are we going up or down? So do we add or take away?" For 5, children can hop it on the number strip: 4 jumps of 5 land on 20, 4 jumps of 3 land on 12. Answers: 1) 8  2) 15  3) 12  4) 16  5) jumps of 5 (20 is further than 12).'))

# ---- teach 1: the rule is the jump ----
N=[2,8,14,20,'?']
body=h2('The rule is the jump')+card(p('A number pattern follows a rule. The rule tells us how much we jump from one number to the next.',40,700))
body+=pin(128,420,1664,track(N),None)
for k in range(3): body+=pin(128,420,1664,track(N,['+6','+6','+6','+6'],only=k),'fade')
body+=pin(128,420,1664,track(N,['+6','+6','+6','+6'],only=3),'fade')+pin(128,420,1664,fill_box(N,4,'26'),'pop')
body+=pin(128,700,1664,p('Check EVERY pair of neighbours. The rule is add 6, so the next number is 20 + 6 = 26.',36,700),'fade',SOFT,20,'22px 30px')
put('l1-teach1',sec('l1-teach1','25–27 MIN',body,'Teach. Point at 2 and 8 and ask: "How far is it from 2 to 8?" Count the hops on the strip with the children: 3, 4, 5, 6, 7, 8. Six hops. Click to show +6. Then ask the same for 8 to 14 and 14 to 20, clicking after each. Click 4 shows the next jump and 26. Think-aloud: "The numbers are 2, 8, 14, 20. They go up. How much from 2 to 8? Six. From 8 to 14? Six. From 14 to 20? Six. I check every pair of neighbours and it is always six. So my rule is add 6. The next number is 20 + 6 = 26." Watch for children who count the numbers in between (3, 4, 5, 6, 7 is five numbers) instead of counting the hops (six). Show them: put a finger on 2, then say a number for every hop.'))

# ---- worked example 1: is 30 in the pattern? ----
body=h2('Worked example: is 30 in the pattern?')+card(p('2, 8, 14, 20, 26 …  Is 30 in this pattern?',44,700))
body+=step(1,'The rule is add 6. Keep jumping:  26 + 6 = 32.',top=430)
body+=step(2,'The pattern goes 26, then 32. It jumps right over 30. So 30 is NOT in the pattern.',top=540)
body+=step(3,'Is 38 in it?  32 + 6 = 38.  Yes!',top=650)
body+=pin(128,770,1664,p('A rule lets us test any number. We do not guess: we keep jumping.',34,700,MUTED),'fade')
put('l1-we1',sec('l1-we1','27–29 MIN',body,'Click to reveal each step. Before each click, ask the group to predict it. Many children say "yes" to 30 because it "feels close". Ask: "How can we test it?" Think-aloud: "My rule is add 6. 26 + 6 = 32. The pattern lands on 26 and then on 32. It never lands on 30, so 30 is not in the pattern. Is 38 in it? 32 + 6 = 38, yes." Count on from 26 on the strip if children are unsure: 27, 28, 29, 30, 31, 32.'))

# ---- try 1 ----
put('l1-try1',rows_slide('l1-try1','29–30 MIN','Your turn: whiteboards','Find the rule first. Then answer.',[('a','5, 9, 13, __, __','17, 21'),('b','31, 28, 25, __','22'),('c','4, 9, 14, 19 … Is 30 in it?','No')],'Children write on whiteboards and hold them up together. Click for each answer. a) Add 4: 13 + 4 = 17, 17 + 4 = 21. b) The numbers go down, so take away 3: 25 − 3 = 22. Anyone who writes 28 has added: ask "Are the numbers getting bigger or smaller?" c) Add 5: 19, 24, 29, 34. It jumps from 29 to 34, so 30 is not in the pattern.'))

# ---- worked example 2: going down, with gaps ----
body=h2('Worked example: going down, with gaps')+card(p('40, 36, __, 28, __, 20     Find the rule. Fill the gaps.',44,700))
body+=step(1,'The numbers get smaller, so the rule is take away.',top=420,size=36)
body+=step(2,'Use two neighbours we know: 40 to 36. Count back: 39, 38, 37, 36. Take away 4.',top=530,size=36)
body+=step(3,'Fill the gaps:  36 − 4 = 32,  then  28 − 4 = 24.',top=640,size=36)
body+=step(4,'Check it lands on the numbers we were given:  32 − 4 = 28 ✓   24 − 4 = 20 ✓',top=750,size=36)
put('l1-we2',sec('l1-we2','30–32 MIN',body,'Click through the steps. Stress step 2: only use two numbers that sit next to each other. 36 and 28 are not neighbours, there is a gap between them. Think-aloud: "The numbers are getting smaller, so my rule is take away. From 40 to 36 I count back 4. Take away 4. 36 − 4 = 32. Then 32 − 4 = 28, and 28 is already there, so my rule works. 28 − 4 = 24 and 24 − 4 = 20, which is there too. My rule is take away 4." Common slip: writing "add 4" because the jump is 4. Ask: "Up or down?"'))

# ---- try 2 ----
put('l1-try2',rows_slide('l1-try2','32–33 MIN','Your turn: fill the gaps','Use two neighbours to find the rule. Then check it.',[('a','50, 45, __, 35, __','40, 30'),('b','3, __, 11, 15, __','7, 19'),('c','27, 25, 23, __, __','21, 19')],'Whiteboards. a) Take away 5 (50 to 45): 45 − 5 = 40, 35 − 5 = 30. b) The neighbours we know are 11 and 15: add 4. 3 + 4 = 7, check 7 + 4 = 11, then 15 + 4 = 19. c) Take away 2: 21, 19. Ask a child who got b right to explain which two numbers they used.'))

# ---- key ----
body=h2('Key idea: find the rule')+card(p('Find the jump between two neighbours. Check it on every pair. Going up: add. Going down: take away.',44,700))+card(p('A rule lets us test any number: keep jumping and see if we land on it.',38,600,MUTED))
put('l1-key',sec('l1-key','33–35 MIN',body,'Say the key idea together. Common mistakes to watch for during the worksheet: (1) Counting the numbers in between instead of the hops: from 4 to 7 they count "5, 6" and say the jump is 2. Put a finger on 4 and say a number for every hop: 5, 6, 7 is 3 hops. (2) Writing "add 3" when the numbers go down (it is take away 3). (3) Restarting the count from 0 instead of adding to the last number. (4) Q4: missing 50, or listing numbers only one child says.'))

# ---- worksheet page 1 ----
put('l1-ws1',ws_preview('l1-ws1','40–53 MIN','Worksheet page 1: with your partner',[('Q1','Skip counting in 2s, 5s and 3s. Fill the gaps.'),('Q2','Find the rule, then write the next two numbers.'),('Q3','Two frogs on a number line to 20. Which number do both land on?')],'Stuck? Hop a counter along your number strip and say each landing out loud.','Minutes 40 to 53. Pairs work together. Walk around and ask "How do you know?" before giving any help. Q2b goes down: check that pairs write take away. Q3 is like the frog explore, but on a shorter line.'))
put('l1-ws1ans',check_slide('l1-ws1ans','53–55 MIN','Page 1: check together',[('Q1','a) 8, 10, 14     b) 15, 25, 35     c) 9, 15'),('Q2a','16, 19.   Rule: add 3'),('Q2b','18, 15.   Rule: take away 3'),('Q2c','18, 22.   Rule: add 4'),('Q3','Frog 1: 4, 8, 12, 16, 20.   Frog 2: 5, 10, 15, 20.   Both: 20')],'Click each answer after a pair explains theirs. Q2b: ask "How did you know it was take away?" (the numbers get smaller). Q3: ask a child to hop both frogs on the class number line.'))

# ---- teach before page 2: numbers in both patterns ----
body=h2('Numbers in both patterns')+card(p('Which numbers up to 20 do we say when we count in 2s AND when we count in 3s?',40,700))
body+=step(1,'Count in 2s and write it:  2, 4, 6, 8, 10, 12, 14, 16, 18, 20',top=420,size=36)
body+=step(2,'Count in 3s under it:  3, 6, 9, 12, 15, 18',top=530,size=36)
body+=step(3,'Ring the numbers in BOTH lists:  6, 12, 18',top=640,size=36)
body+=pin(128,760,1664,p('What do you notice? Each one is 6 more than the one before.',36,700),'fade',SOFT,20,'20px 30px')
put('l1-teachboth',sec('l1-teachboth','55–57 MIN',body,'Teach before worksheet page 2 (Q4 uses counting in 2s and in 5s, so we practise with 2s and 3s here; do not do 2s and 5s for them). Write the two lists on the board one under the other and ring the matches. Think-aloud: "I write the 2s in a row. Then I write the 3s under them. Now I look for numbers that are in both rows: 6, 12, 18." Ask: "Is 9 in both? No, we do not say 9 when we count in 2s."'))

# ---- teach before page 2: growing table ----
W=[200]+[110]*6
body=h2('Fill a table: add to the last box')+card(p('Box 1 has 1 sticker. Each box has 4 more stickers than the box before.',40,700))
body+=trow(128,400,['Box','1','2','3','4','5','6'],W,None,True)
body+=trow(128,490,['Stickers','1','5','9','13','17','21'],W,'rise')
body+=pin(1300,400,492,p('Add 4 to the stickers in the LAST box, not to the box number.',34,700),None,WHITE,20,'22px 26px')
body+=pin(128,620,1664,p('Odd or even? Even numbers end in 0, 2, 4, 6 or 8. Odd numbers end in 1, 3, 5, 7 or 9.',36,700),'fade',WHITE,20,'20px 30px')
body+=pin(128,750,1664,p('1, 5, 9, 13, 17, 21: these are all odd.',36,700),'fade',SOFT,20,'20px 30px')
put('l1-teachtable',sec('l1-teachtable','57–58 MIN',body,'Teach before worksheet page 2 (Q5, the sticker boxes). Click to fill the stickers row; say each step aloud: "1, add 4 is 5. 5, add 4 is 9 …" Common mistake: adding 4 to the box number (box 2 has 2 + 4 = 6). Then the odd and even reminder. Here every number is odd. Do not say what happens on the worksheet: Q5 adds 3, and children should look at their own row and say what they see.'))

# ---- worksheet page 2 ----
put('l1-ws2',ws_preview('l1-ws2','58–66 MIN','Worksheet page 2: on your own',[('Q4','Ali counts in 2s, Mei counts in 5s, up to 50. Which numbers do both say?'),('Q5','Sticker boxes: fill the table to Box 10. Odd or even?')],'Finished early? Stretch and Challenge come next.','Children work alone. Check that each child writes both lists for Q4 and adds 3 to the LAST box for Q5. Note who needs a short catch-up next lesson.'))
put('l1-ws2ans',check_slide('l1-ws2ans','66–68 MIN','Page 2: check together',[('Q4a','10, 20, 30, 40, 50'),('Q4b','They all end in 0. We say them when we count in 10s.'),('Q5a','2, 5, 8, 11, 14, 17, 20, 23, 26, 29.   Box 10 has 29.'),('Q5b','Even, odd, even, odd … they take turns.')],'Click each answer after a child explains. Q4b: numbers we say in 5s end in 5 or 0; numbers we say in 2s are even; so the shared ones end in 0. Q5: the rule is add 3. Box 10: 26 + 3 = 29. Q5b: adding 3 turns an even number into an odd one and an odd number into an even one, so they take turns.'))

# ---- stretch (new) ----
st=[('1.','Ali counts from 3 in 4s: 3, 7, 11, … Will he say 39? Will he say 40?'),('2.','50, 46, 42, … What is the first number less than 10?'),('3.','An add pattern has 11 as its 3rd number and 19 as its 5th number. What is the rule? What is the 1st number?')]
put('l1-stretch',sec('l1-stretch','For early finishers',h2('Stretch')+''.join(card(p(f'<span style="color:#1F7A6F">{a}</span>  {E(b)}',38,600,raw=True)) for a,b in st),'For children who finish early. Answers: 1) Yes to 39, no to 40 (3, 7, 11, 15, 19, 23, 27, 31, 35, 39, 43: it lands on 39 and jumps over 40). 2) 6 (… 18, 14, 10, 6; 10 is not less than 10). 3) Add 4: from the 3rd to the 5th number is two equal jumps that make 8, and 4 + 4 = 8. The 2nd number is 11 − 4 = 7 and the 1st is 7 − 4 = 3. Check: 3, 7, 11, 15, 19.'))

# ---- challenge walk-through ----
body=h2('Challenge: walk-through')+pin(128,250,760,p('Q1: look at the jumps',38,800,TEAL))
for i,t in enumerate(['Jumps: +1, +2, +3, +4, +5. They grow by 1.','7th: 16 + 6 = 22','8th: 22 + 7 = 29 ✓']): body+=pin(128,330+i*120,760,p(t,34),'rise',WHITE)
body+=pin(960,250,832,p('Q2: two lists, ring the matches',38,800,TEAL))
for i,t in enumerate(['Ali: 2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41, 44, 47, 50','Mei: 1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49','In both: 5, 17, 29, 41']): body+=pin(960,330+[0,170,340][i],832,p(t,32),'rise',WHITE if i<2 else YEL)
put('l1-chwalk',sec('l1-chwalk','Challenge',body,'Use after pairs have tried. Q1: many children add 5 again and say 21 for the 7th. Ask: "Does the jump stay the same, or does it change?" Q2: write both lists in rows on the board and ring the matches. Ask: "What do you notice about 5, 17, 29, 41?" (each is 12 more than the one before).'))

# ---- small fixes to kept slides ----
ex=os.path.join(D,'slides','l1-explore2.html'); s=open(ex).read()
s=s.replace('They are in the 20 times table: 5 jumps of 4 or 4 jumps of 5.','We say them when we count in 20s: 20 is 5 jumps of 4 and also 4 jumps of 5.'); open(ex,'w').write(s)

for i,h in S.items(): open(os.path.join(D,'slides',i+'.html'),'w').write(h)
for old in ['l1-mini1','l1-mini2']:
    f=os.path.join(D,'slides',old+'.html')
    if os.path.exists(f): os.remove(f)
t=os.path.join(D,'slides','l1-title.html'); s=open(t).read(); s=s.replace('mini-lesson 25 to 35, brain break 35 to 40, worksheet 40 to 70','teaching 25 to 35 (click to reveal each step and answer), brain break 35 to 40, worksheet 40 to 70 with short teaching before each page and a check-together slide after it'); open(t,'w').write(s)
deck=json.load(open(os.path.join(D,'deck.json')))
deck['order']=['cover','routine','rules','l1-title','l1-warm1','l1-warm2','l1-explore1','l1-explore2','l1-teach1','l1-we1','l1-try1','l1-we2','l1-try2','l1-key','l1-break','l1-ws1','l1-ws1ans','l1-teachboth','l1-teachtable','l1-ws2','l1-ws2ans','l1-stretch','l1-challenge','l1-chdiag','l1-chwalk','l1-talk','l1-exit']
deck['sections']={'s1':{'description':'Warm-up and explore','start':'cover'},'s2':{'description':'Teach: find the rule, test a number, fill the gaps','start':'l1-teach1'},'s3':{'description':'Worksheet with teaching before each page','start':'l1-break'},'s4':{'description':'Stretch, challenge, talk and exit','start':'l1-stretch'}}
json.dump(deck,open(os.path.join(D,'deck.json'),'w'),indent=1,ensure_ascii=False)
print(len(deck['order']),'slides')

# ---- P1 audit fixes (issues 8, 9, 27, 28): timing and routine slide ----
import p1gifted; p1gifted.apply(D,1)
import p1gaps; p1gaps.apply(D,1)
import p1fix
p1fix.finish(D,1,{'l1-ws2':'58–68 MIN'})
p1fix.patch(D,'routine',[('<td>40–70</td><td><b>Worksheet</b></td><td>Pairs, then on your own, then stretch</td>','<td>40–72</td><td><b>Worksheet</b></td><td>Pairs, then on your own, then check together. Think Harder and Challenge are for early finishers or home.</td>'),('<td>70–80</td>','<td>72–80</td>')])
import p1neutral; p1neutral.apply(D,1)

import p1round2; p1round2.apply(D,1)
