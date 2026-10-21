"""Math Inquirers P2, Lesson 1: Digit Detectives. Writes split/p2l1/project (deck.json + slides/*.html)."""
import json,os,sys,datetime
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,H)
import slidekit, p2gaps
from slidekit import *
slidekit.FOOT='Math Inquirers P2 Holiday Program  •  Notice it. Test it. Explain why.'
D=os.path.join(H,'..','split','p2l1','project'); os.makedirs(os.path.join(D,'slides'),exist_ok=True)
S={}
def put(i,h): S[i]=h
RED='#D64545'; FOOTX=slidekit.FOOT

# ---------- shared slide shapes (same look as the P1 decks) ----------
def title_slide(sid,label,title,topic,today,notes):
    return (f'<section id="{sid}" data-transition="fade" style="background:{NAVY};color:{CREAM};font-family:{BF};padding:128px 128px 160px;display:flex;flex-direction:column;justify-content:center;gap:36px">\n'
            f'<p style="font-size:32px;font-weight:700;letter-spacing:4px;color:{YEL}">{E(label)}</p>\n'
            f'<h1 style="font-family:{HF};font-size:128px;font-weight:600;line-height:1.05">{E(title)}</h1>\n'
            f'<p style="font-size:44px;color:#C9D4EC">{E(topic)}</p>\n'
            f'<div style="background:#26385F;border-radius:24px;padding:40px;display:flex;flex-direction:column;gap:12px"><p style="font-size:28px;font-weight:700;letter-spacing:3px;color:{YEL}">TODAY WE WILL</p><p style="font-size:44px;font-weight:600">{E(today)}</p></div>\n'
            f'<p style="position:absolute;left:128px;bottom:64px;width:1400px;font-size:24px;color:#B7C3DD">{E(FOOTX)}</p>\n<aside>{E(notes)}</aside>\n</section>\n')
def break_slide(sid,time,text,notes):
    return (f'<section id="{sid}" data-transition="fade" style="background:{TEAL};color:{CREAM};font-family:{BF};padding:128px 128px 160px;display:flex;flex-direction:column;justify-content:center;gap:36px">\n'
            f'<p style="font-size:32px;font-weight:700;letter-spacing:4px;color:{YEL}">{E(time)}</p>\n'
            f'<h2 style="font-family:{HF};font-size:110px;font-weight:600;line-height:1.05">Brain break</h2>\n'
            f'<p style="font-size:48px;font-weight:600">{E(text)}</p>\n<p style="font-size:36px;color:#D7EFEA">Then: a drink of water and back to our seats.</p>\n'
            f'<p style="position:absolute;left:128px;bottom:64px;width:1400px;font-size:24px;color:#D7EFEA">{E(FOOTX)}</p>\n<aside>{E(notes)}</aside>\n</section>\n')
def numcards(items,size=38):
    return ''.join(card(p(f'<span style="color:{TEAL}">{a}</span>  {E(b)}',size,600,raw=True)) for a,b in items)
def chipcard(label,text,bg=TEAL,fg=CREAM,size=44):
    return card(chip(label,bg,fg)+p(text,size,600))
def checks(sid,time,title,rows,notes,top=250,gapy=150,size=34,lw=170):
    body=h2(title)
    for i,(a,b) in enumerate(rows):
        t=top+i*gapy
        body+=pin(128,t,lw-20,f'<p style="font-size:36px;font-weight:800;color:{TEAL}">{E(a)}</p>',None,WHITE,20,'18px 24px')
        body+=pin(128+lw,t,1664-lw,f'<p style="font-size:{size}px;font-weight:800;line-height:1.25">{E(b)}</p>','pop',YEL,20,'16px 26px')
    return sec(sid,time,body,notes)
def svgwrap(w,h,label,inner):
    return f'<svg aria-label="{E(label)}" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="width:{w}px;height:{h}px;flex:none">{inner}</svg>'
def txt(x,y,s,size=40,fill=NAVY,anchor='middle',weight=700,font='Fredoka, Arial'):
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" fill="{fill}" font-family="{font}">{E(str(s))}</text>'
def dcards(digits,x0=0,y=6,w=96,h=124,gap=26,fill=YEL):
    g=''
    for i,d in enumerate(digits):
        x=x0+i*(w+gap)
        g+=f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="16" fill="{fill}" stroke="{NAVY}" stroke-width="5"/>'+txt(x+w/2,y+h/2+24,d,70)
    return g
def hto(x0,y,w=150,h=130,vals=('','',''),gap=20):
    g=''
    for i,(lab,v) in enumerate(zip(['H','T','O'],vals)):
        x=x0+i*(w+gap)
        g+=f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="{WHITE}" stroke="{NAVY}" stroke-width="5" stroke-dasharray="14 8"/>'+txt(x+w/2,y-14,lab,32,TEAL)
        if v: g+=txt(x+w/2,y+h/2+26,v,72)
    return g

# ---------- 1. title ----------
put('p2l1-title',title_slide('p2l1-title','LESSON 1  •  WEEK 1','Digit Detectives','Numbers to 1000',
 'Build 3-digit numbers, find every number from digit cards by listing in order, and spot patterns on a 1000 chart.',
 'Objective: Read and build 3-digit numbers by place value (also with more than 9 tens), make every number from a set of digit cards by listing in order, find the biggest and smallest, and use patterns on a 1000 chart to count on and back in 1s, 10s and 100s. '
 'Thinking strategies taught today: MAKE A LIST IN ORDER and LOOK FOR A PATTERN. '
 'Materials: Digit cards 0 to 9 (one set per child), place-value mat (hundreds, tens, ones), base-ten blocks or paper strips and squares, mini whiteboards, a 1000 chart page (rows of 10). '
 'Online: children cut out paper digit cards before the lesson and move them on camera; the tutor writes on the 1000-chart pieces on the slides. '
 'Time plan: warm-up 0 to 8, explore 8 to 20 (explore2 talk is 6 minutes), teaching 20 to 32 (click to reveal each step and answer), brain break 32 to 36, worksheet page 1 36 to 50 then check together 50 to 52, short teaching 52 to 57, worksheet page 2 57 to 69 then check together 69 to 72, talk time 72 to 80, exit ticket 80 to 90. Stretch and Challenge slides are for early finishers.'))

# ---------- 2. warm-up game ----------
g=hto(40,60,200,170)+dcards([7],760,82,110,140)+txt(980,170,'?',90,TEAL)
for i,d in enumerate([3,9,1]): g+=f'<rect x="{1120+i*130}" y="92" width="96" height="120" rx="14" fill="{SKY}" stroke="{NAVY}" stroke-width="4"/>'
g+=txt(1310,262,'cards still to come …',30,MUTED,weight=600,font='Nunito Sans, Arial')
body=h2('Warm-up: Place It Right')+card(p('I turn over one digit card at a time. Write it in the H, T or O box straight away. No moving it later! Biggest number wins.',38,700))
body+=pin(128,420,1664,svgwrap(1600,290,'Three empty place-value boxes H, T, O and a digit card 7 waiting to be placed',g),None,WHITE,24,'16px 32px')
body+=pin(128,770,1664,p('Where would you put a 9? A 0? What about a 5: keep it, or wait for a bigger card?',36,700),'fade',SOFT,20,'20px 30px')
put('p2l1-warm1',sec('p2l1-warm1','0–5 MIN',body,
 'Minutes 0 to 5. Place It Right. Children draw three boxes on a whiteboard: H, T, O. Shuffle digit cards 0 to 9 and turn over one at a time (online: hold it up to the camera). After EACH card, children write it in one empty box at once and cannot move it. After three cards, read the numbers aloud: biggest wins. '
 'Play 3 rounds: two for the biggest, one for the smallest. Click to show the thinking question. Talk: "A 9 goes in the hundreds: it is worth 900 there. A 0 goes in the ones. A 5 is tricky: are there more big cards or small cards left?" '
 'Listen for children who say "the hundreds digit matters most". That idea comes back in talk time (401 or 399).'))

# ---------- 3. quick questions ----------
qs=[('1.','4 hundreds, 6 tens, 2 ones = ?','462'),('2.','What is the 8 worth in 384?','80'),('3.','10 more than 296?','306'),('4.','100 less than 405?','305'),('5.','The biggest 3-digit number?','999')]
body=h2('Quick questions')+''.join(qrow(128,250+i*125,1250,a,b) for i,(a,b,c) in enumerate(qs))+''.join(answer(1420,250+i*125,372,c) for i,(a,b,c) in enumerate(qs))
put('p2l1-warm2',sec('p2l1-warm2','5–8 MIN',body,'Minutes 5 to 8. Read each aloud, whiteboards up together, then click to show. Ask after 3: "Why did the hundreds digit change?" (9 tens and 1 more ten make 10 tens, which is another hundred). After 4: "Which digit changed? Why not the ones?" Answers: 462, 80, 306, 305, 999.'))

# ---------- 4. explore: what to do ----------
g=dcards([3,5,8],40,40,110,140)+hto(560,50,150,130)+f'<rect x="1150" y="40" width="430" height="150" rx="18" fill="{SOFT}" stroke="{NAVY}" stroke-width="4"/>'+txt(1365,105,'Find every number.',34)+txt(1365,155,'How do you know?',32,TEAL)
steps=''.join(f'<li>{E(s)}</li>' for s in ['Take the digit cards 3, 5 and 8.','Make a 3-digit number using each card once. Write it down.','Make as many different numbers as you can.','Circle the biggest and the smallest. Have you got them all?'])
body=h2('Explore: what to do')+card(chip('EXPLORE')+f'<ol style="font-size:36px;font-weight:600;padding-left:52px;display:flex;flex-direction:column;gap:8px">{steps}</ol>')
body+=card(svgwrap(1600,220,'Digit cards 3, 5 and 8 next to three empty boxes H, T, O',g),extra='padding:20px 32px')
put('p2l1-explore1',sec('p2l1-explore1','8–14 MIN',body,'Minutes 8 to 14. Pairs work with digit cards 3, 5 and 8 (online: paper cards on camera). Ask them to predict first: how many numbers? Most children guess 3 or 9. Let them record numbers in any order at first; the teaching part shows how to list them in order. Early finishers: add a 0 card and use 0, 3, 5. Why are there fewer numbers?'))

# ---------- 5. explore: talk ----------
body=h2('Explore: talk about it')+numcards([('1.','How many numbers did you make? Did your partner make the same?'),('2.','How do you know you have found them all?'),('3.','Which number is the biggest? The smallest? Why?')],40)
put('p2l1-explore2',sec('p2l1-explore2','14–20 MIN',body,'Minutes 14 to 20. Let pairs keep working, then gather them. Collect the numbers on the board in the order children say them, messy on purpose, then ask "Is anything missing? Is anything there twice?" Answers: 1) 6 numbers: 358, 385, 538, 583, 835, 853. 2) List them in order: 2 numbers start with 3, 2 start with 5, 2 start with 8. 3) 853 is biggest (biggest digit in the hundreds place), 358 is smallest. Do NOT tell the method yet if nobody finds it: the next slides teach it.'))

# ---------- 6. teach: place value ----------
def blocks(h,t,o):
    g=''; x=10
    for i in range(h):
        d=' '.join(f'M{x+k*11} 10 V120 M{x} {10+k*11} H{x+110}' for k in range(1,10))
        g+=f'<rect x="{x}" y="10" width="110" height="110" fill="{SKY}" stroke="{NAVY}" stroke-width="3"/><path d="{d}" stroke="{NAVY}" stroke-width="1" opacity=".45"/>'; x+=122
    x+=24
    for i in range(t):
        d=' '.join(f'M{x} {10+k*11} H{x+14}' for k in range(1,10))
        g+=f'<rect x="{x}" y="10" width="14" height="110" fill="{YEL}" stroke="{NAVY}" stroke-width="3"/><path d="{d}" stroke="{NAVY}" stroke-width="1" opacity=".5"/>'; x+=22
    x+=24
    for i in range(o):
        g+=f'<rect x="{x}" y="96" width="24" height="24" fill="#BFE3DC" stroke="{NAVY}" stroke-width="3"/>'; x+=32
    return g
g=blocks(5,12,4)+txt(310,175,'5 hundreds',34,TEAL)+txt(776,175,'12 tens',34,TEAL)+txt(1000,175,'4 ones',34,TEAL)
body=h2('Place value: more than 9 tens')+card(p('What number is 5 hundreds, 12 tens and 4 ones?',42,700))
body+=pin(128,372,1664,svgwrap(1300,190,'5 hundred squares, 12 ten sticks and 4 ones',g),None)
body+=step(1,'5 hundreds = 500',top=590,size=34)
body+=step(2,'12 tens = 10 tens + 2 tens.  10 tens make 1 hundred, so 12 tens = 120.',top=690,size=34)
body+=step(3,'500 + 120 + 4 = 624.   Check: 6 hundreds, 2 tens, 4 ones ✓',top=790,size=34)
put('p2l1-teach1',sec('p2l1-teach1','20–22 MIN',body,'Teach. Build it with base-ten blocks (online: paper strips and squares). Ask first: "Can we write 5, 12, 4 as 5124?" (No: that is a 4-digit number. A box can only hold one digit.) Click through the steps. Think-aloud: "12 tens is too many for the tens box. Ten of them swap for one hundred. Now I have 6 hundreds, 2 tens and 4 ones: 624." Go the other way too: "624 is 6 hundreds and 2 tens. It is ALSO 5 hundreds and 12 tens."'))
put('p2l1-try1',try_slide('p2l1-try1','22–24 MIN','Your turn: whiteboards','Write the number. Swap 10 tens for 1 hundred when you need to.',[('a','3 hundreds, 0 tens, 9 ones','309'),('b','2 hundreds, 11 tens, 5 ones','315'),('c','What is the 6 worth in 461?','60')],'Whiteboards up together, then click. a) Watch for 39: the 0 tens still needs a 0 to hold the place. b) 11 tens = 1 hundred and 1 ten, so 3 hundreds, 1 ten, 5 ones. c) 6 tens = 60, not 6.'))

# ---------- 8. worked example: list in order ----------
body=h2('Worked example: every number from 1, 6, 9')+card(p('Use each card once. Make every 3-digit number. How many are there?',40,700))
cols=[('1 first',['169','196']),('6 first',['619','691']),('9 first',['916','961'])]
for i,(head,ns) in enumerate(cols):
    L=128+i*568
    body+=pin(L,380,500,p(head,38,800),None,YEL,20,'14px 28px')
    for j,n in enumerate(ns): body+=pin(L,470+j*95,500,p(n,46,700),'rise',WHITE,20,'12px 28px')
body+=pin(128,680,1664,p('Fix the hundreds digit. Swap the other two. Each card starts 2 numbers: 2 + 2 + 2 = 6 numbers.',36,700),'fade',SOFT,20,'20px 30px')
body+=pin(128,800,1664,p('Biggest: biggest digit first, 961.   Smallest: smallest digit first, 169.',36,700),'fade',WHITE,20,'18px 30px')
put('p2l1-we1',sec('p2l1-we1','24–27 MIN',body,'Make a list in order: this is today\'s main strategy. Click to reveal each number while children say it first. Think-aloud: "I keep 1 in the hundreds place. The 6 and 9 can go 6, 9 or 9, 6: 169, 196. Nothing else starts with 1. Now 6 first …" Ask: "How do we KNOW there are no more?" (every card has had its turn at the front, and each one only starts 2 numbers). Then the biggest and smallest, read straight from the list.'))
put('p2l1-try2',try_slide('p2l1-try2','27–28 MIN','Your turn: cards 3, 4, 8','List in order on your whiteboard first.',[('a','How many numbers can you make?','6'),('b','What is the biggest?','843'),('c','What is the smallest?','348')],'Whiteboards. The list: 348, 384, 438, 483, 834, 843. Ask a child to explain how they know there are exactly 6. Ask: "Which of the 6 is closest to 400?" (384 is only 16 away; 438 is 38 away).'))

# ---------- 10. teach zero ----------
g=dcards([0,3,6],40,30,100,130)
body=h2('Careful: the zero card')+pin(128,250,600,svgwrap(560,200,'Digit cards 0, 3 and 6',g),None)
body+=pin(760,250,1032,p('Make every 3-digit number with 0, 3 and 6.',40,700),None,WHITE,20,'26px 32px')
body+=step(1,'3 first: 306, 360.     6 first: 603, 630.',top=480,size=38)
body+=step(2,'0 first: 036 is just 36. It has only 2 digits: not this one!',top=590,size=38)
body+=pin(128,710,1664,p('So only 4 numbers. Zero can never be the hundreds digit. Smallest: 306.',38,800),'fade',SOFT,20,'20px 30px')
put('p2l1-teachzero',sec('p2l1-teachzero','28–31 MIN',body,'Teach before the worksheet (Q3 has a zero card). Ask first: "Will 0, 3, 6 make 6 numbers like before?" Let children argue. Show 036 on a calculator or say it aloud: "thirty-six". Click through. Smallest is 306, not 036. Biggest is 630.'))

# ---------- 11. key ----------
body=h2('Key idea: list in order')+card(p('Fix the hundreds digit, then swap the others. Each card starts the same number of numbers, so you know when you have them all.',44,700))+card(p('Zero can never be the hundreds digit. Biggest digit first makes the biggest number.',38,600,MUTED))
put('p2l1-key',sec('p2l1-key','31–32 MIN',body,'Say the key idea together. Common mistakes to watch for during the worksheet: (1) Writing 6 hundreds, 15 tens and 2 ones as 6152 instead of regrouping 15 tens as 1 hundred and 5 tens (752). (2) Listing digit-card numbers at random, so one is missed or written twice, or counting 059 as a 3-digit number. (3) Counting back in 10s across a hundred: 512, 502, 592 instead of 492.'))
put('p2l1-break',break_slide('p2l1-break','32–36 MIN','Swap the digits. Each child puts three digit cards in a row (hundreds, tens, ones). The tutor calls “swap the hundreds and the tens” or “swap the tens and the ones”. Show your new number on camera. Is it bigger or smaller?','Four minutes. Online: each child lays out 3 digit cards in a row on camera and reads the number; call a swap and everyone shows the new number. Ask each time: bigger or smaller? Ask: "Which swap makes the biggest jump?" (swapping the hundreds digit).'))

# ---------- worksheet page 1 ----------
put('p2l1-ws1',ws_preview('p2l1-ws1','36–50 MIN','Worksheet page 1: with your partner',[('Q1','Place value. Swap 10 tens for 1 hundred when you need to.'),('Q2','The cards 2, 7, 4. Make a list in order, then answer the questions.'),('Q3','The cards 0, 5, 9. Watch out for the zero!')],'Stuck? Build the number with blocks, or lay out the real cards.','Minutes 36 to 50. Walk around. Ask "How do you know you have them all?" before giving any help. Q1c is the hardest on this page: 830 is 8 hundreds and 3 tens, and ALSO 7 hundreds and 13 tens (break one hundred into 10 tens).'))
put('p2l1-ws1ans',checks('p2l1-ws1ans','50–52 MIN','Page 1: check together',[('Q1','a) 407   b) 752   c) 3 tens; 13 tens   d) 70'),('Q2','a) 247, 274, 427, 472, 724, 742   b) 742 and 247   c) 472   d) 2 (247, 427)'),('Q3','a) 509, 590, 905, 950   b) 0 cannot go first, so only 5 or 9 start: 2 + 2 = 4')],
 'Click each answer after a pair explains theirs. Q1b: 15 tens = 1 hundred and 5 tens, so 7 hundreds, 5 tens, 2 ones. Q2c: 472 is 28 away from 500, 427 is 73 away, 724 is 224 away. Q2d: a number is odd when its ones digit is odd; only 7 is odd, so the numbers ending in 7.',gapy=170))

# ---------- teach: 1000 chart ----------
g=''
for r in range(3):
    for c in range(10):
        n=271+r*10+c; x=10+c*118; y=10+r*74
        hi=n in (283,)
        g+=f'<rect x="{x}" y="{y}" width="118" height="74" fill="{YEL if hi else WHITE}" stroke="{NAVY}" stroke-width="3"/>'+txt(x+59,y+50,n,34)
body=h2('Patterns on a 1000 chart')+pin(128,240,1664,svgwrap(1200,250,'Part of a 1000 chart: rows 271 to 300',g),None)
body+=pin(1360,240,432,p('Each row has 10 numbers.',34,700),None,SOFT,20,'18px 24px')
body+=step(1,'One square RIGHT: 1 more.   283 → 284',top=520,size=36)
body+=step(2,'One square DOWN: 10 more.   283 → 293',top=620,size=36)
body+=qrow(128,730,1250,'Your turn:','Which number is directly below 296? Directly above 281?',36)+answer(1420,730,372,'306 and 271')
put('p2l1-teachchart',sec('p2l1-teachchart','52–54 MIN',body,'Teach before worksheet page 2 (Q4 has chart pieces). Look for a pattern: point along a row (+1 each time) and down a column (+10 each time; the ones digit stays the same). Ask: "What is directly below 296 (one square down)? It is not on our piece!" Go down a column: 296, 306, because 10 more than 296 crosses the hundred. Directly above 281 (one square up) is 10 less: 271.'))

# ---------- teach: count across a hundred ----------
rows=[('Count on in 10s:','475, 485, ___, ___','495, 505'),('Count back in 10s:','628, 618, 608, ___, ___','598, 588'),('Count on in 100s:','63, 163, 263, ___','363')]
body=h2('Counting past a hundred')+p('Say each number aloud. Watch what happens to the hundreds digit.',34,600,MUTED)
for i,(a,b,c) in enumerate(rows):
    body+=qrow(128,330+i*150,1250,a,b,38)+answer(1420,330+i*150,372,c)
body+=pin(128,790,1664,p('Past 9 tens, the hundreds digit goes up. Back past 0 tens, it goes down.',36,700),'fade',SOFT,20,'18px 30px')
put('p2l1-teachcount',sec('p2l1-teachcount','54–55 MIN',body,'Teach before worksheet page 2 (Q5). Children say the next numbers on whiteboards before each click. The trap is in the second row: many children say 608, 698. Show it on the chart: going up a row from 608 is 598. Think-aloud: "608 is 6 hundreds and 0 tens. To take 10, I break a hundred: 5 hundreds and 9 tens, 598."'))

# ---------- teach: digit riddle ----------
body=h2('Digit riddles: list, then check')+card(p('I am a 3-digit number. My hundreds digit is 2. My tens digit is 3 more than my ones digit. My digits add up to 11.',38,700))
body+=step(1,'List the tens and ones that fit:  ones 0, tens 3;  ones 1, tens 4;  ones 2, tens 5;  ones 3, tens 6 …',top=420,size=34)
body+=step(2,'Check the total:  2 + 3 + 0 = 5,  2 + 4 + 1 = 7,  2 + 5 + 2 = 9,  2 + 6 + 3 = 11 ✓',top=530,size=34)
body+=answer(128,640,1664,'I am 263.')
body+=pin(128,750,1664,p('"Find ALL" riddles: list in order. Digits add up to 2: 101, 110, 200. Start with the smallest hundreds digit.',34,700),'fade',SOFT,20,'18px 30px')
put('p2l1-teachriddle',sec('p2l1-teachriddle','55–57 MIN',body,'Teach before worksheet page 2 (Q6). Two strategies together: make a list in order, then check each one (guess and check, but tidy). Ask after step 2: "Why can we stop?" (the totals go up by 2 each time, so 11 only comes once). For the "find all" line: hundreds digit 1 leaves 1 for the tens and ones (101, 110); hundreds digit 2 leaves 0 (200). Zero cannot be the hundreds digit.'))

# ---------- worksheet page 2 ----------
put('p2l1-ws2',ws_preview('p2l1-ws2','57–69 MIN','Worksheet page 2: on your own',[('Q4','Chart pieces. Right is 1 more, down is 10 more.'),('Q5','Count on and back. Watch the hundreds digit.'),('Q6','Digit riddles. List in order, then check every clue.')],'Finished early? Stretch and Challenge come next.','Children work alone. Note who needs a short catch-up next lesson, especially children who still write 592 after 502.'))
put('p2l1-ws2ans',checks('p2l1-ws2ans','69–72 MIN','Page 2: check together',[('Q4','A: 348, 349 / 357, 359 / 367, 368.  B: 595, 596, 597 and 606.  Down 10, right 1.  b) 405'),('Q5','a) 347, 447   b) 502, 492   c) 1000   d) 700, 699'),('Q6','a) 435   b) 102, 111, 120, 201, 210, 300: 6 numbers')],
 'Click after a child explains. Q4 Piece B: the square under 586 is 596; left 595, right 597; under 596 is 606. Q4b: 385, 395, 405. Q6a: tens and ones pairs (0, 2), (1, 3), (2, 4), (3, 5): only 4 + 3 + 5 = 12. Q6b: hundreds 1 leaves 2 (102, 111, 120), hundreds 2 leaves 1 (201, 210), hundreds 3 leaves 0 (300).',gapy=170))

# ---------- stretch / challenge ----------
st=[('1.','How many 3-digit numbers have all three digits the same?'),('2.','Use the digit cards 3, 0 and 0. How many 3-digit numbers can you make?'),('3.','I am a 3-digit number. You say me when you count in 10s from 5. My hundreds digit is 7. My tens digit is 1 less than my hundreds digit. Who am I?')]
put('p2l1-stretch',sec('p2l1-stretch','For early finishers',h2('Stretch')+numcards(st),'Answers: 1) 9 (111, 222, … 999; 000 is not a 3-digit number). 2) Only 1: 300 (003 and 030 are not 3-digit numbers). 3) 765 (counting in 10s from 5 always ends in 5; tens digit 7 − 1 = 6).'))
ch=[('1.','Ben writes all the numbers from 300 to 399. How many times does he write the digit 3?'),('2.','Mei uses each of the digit cards 1, 2, 3, 4, 5 and 6 once to make two 3-digit numbers. She adds them. What is the smallest total she can make?')]
put('p2l1-challenge',sec('p2l1-challenge','69–80 MIN',h2('Challenge')+numcards(ch,36),'Pairs try first, then use the "see it" slide if stuck, then the walk-through. These are Think Harder Q7 and Q5. Answers: 1) 120 (100 in the hundreds place, 10 in the tens place from 330 to 339, 10 in the ones place 303, 313 … 393). 2) 381, for example 135 + 246 (1 and 2 in the hundreds, 3 and 4 in the tens, 5 and 6 in the ones).'))
g1=''
for i,(n) in enumerate(['303','317','333','345','393']):
    x=30+i*140; g1+=f'<rect x="{x}" y="20" width="120" height="70" rx="10" fill="{WHITE}" stroke="{NAVY}" stroke-width="3"/>'+txt(x+60,68,n,36)
g1+=txt(380,140,'… 300 to 399 …',30,MUTED,weight=600,font='Nunito Sans, Arial')
for i,lab in enumerate(['3s in the hundreds place','3s in the tens place','3s in the ones place']):
    y=180+i*82; g1+=f'<rect x="30" y="{y}" width="700" height="68" rx="10" fill="{WHITE}" stroke="{NAVY}" stroke-width="3"/>'+txt(60,y+46,lab,30,NAVY,'start',700,'Nunito Sans, Arial')+f'<rect x="600" y="{y+10}" width="110" height="48" rx="8" fill="{SOFT}" stroke="{NAVY}" stroke-width="2"/>'+txt(655,y+46,'?',32)
g2=dcards([1,2,3,4,5,6],60,20,90,110,20)
for r in range(2):
    for c in range(3):
        g2+=f'<rect x="{230+c*110}" y="{170+r*110}" width="96" height="96" rx="12" fill="{WHITE}" stroke="{NAVY}" stroke-width="4" stroke-dasharray="10 6"/>'
g2+=txt(180,340,'+',60)+f'<line x1="170" y1="390" x2="580" y2="390" stroke="{NAVY}" stroke-width="5"/>'+txt(400,445,'smallest total = ?',36,TEAL)
body=h2('Challenge: see it',60)+'<div style="display:flex;gap:32px;align-items:flex-start">'
body+=card(f'<p style="font-size:30px;font-weight:700;color:{TEAL}">Q1: Count the 3s, place by place</p>'+svgwrap(760,470,'Numbers from 300 to 399 and a table for the 3s in each place',g1).replace('width:760px;height:470px;flex:none','width:100%;height:auto;display:block'),extra='flex:1;min-width:0;padding:20px 24px')
body+=card(f'<p style="font-size:30px;font-weight:700;color:{TEAL}">Q2: Six cards, two numbers</p>'+svgwrap(760,470,'Digit cards 1 to 6 and two rows of three empty boxes added together',g2).replace('width:760px;height:470px;flex:none','width:100%;height:auto;display:block'),extra='flex:1;min-width:0;padding:20px 24px')+'</div>'
put('p2l1-chdiag',sec('p2l1-chdiag','69–80 MIN',body,'Show after pairs have tried the Challenge, or if they are stuck. The pictures show the problem, not the answer. Ask: What do you notice? Which place matters most in Q2? Can you count the 3s one place at a time in Q1? Answers are in the Challenge slide notes.'))
body=h2('Challenge: walk-through')+pin(128,250,800,p('Q1: one place at a time',38,800,TEAL))
for i,t in enumerate(['Hundreds: every number 300 to 399 → 100','Tens: 330, 331 … 339 → 10','Ones: 303, 313 … 393 → 10','100 + 10 + 10 = 120.  333 has three 3s!']): body+=pin(128,330+i*110,800,p(t,32),'rise',WHITE)
body+=pin(992,250,800,p('Q2: smallest digits in the biggest places',38,800,TEAL))
for i,t in enumerate(['Hundreds: 1 and 2 → 100 + 200 = 300','Tens: 3 and 4 → 30 + 40 = 70','Ones: 5 and 6 → 11','300 + 70 + 11 = 381,  e.g. 135 + 246 ✓']): body+=pin(992,330+i*110,800,p(t,32),'rise',WHITE)
put('p2l1-chwalk',sec('p2l1-chwalk','Challenge',body,'Use after pairs have tried. Q1: a list in order by PLACE stops us missing any 3s; many children say 111 or 102 because they count 333 once. Q2: the hundreds digits matter most, so they get the smallest cards; any way of placing 1, 2 / 3, 4 / 5, 6 gives 381 (136 + 245 also works). Check by adding: 135 + 246 = 381.'))

# ---------- talk / exit ----------
body=h2('Talk time')+card(chip('TALK TIME',YEL,NAVY)+p('Which is bigger, 401 or 399? Ali says 399, because it has two 9s. Who is right? Why?',42,600))+card(p('Sentence starters:',34,400,MUTED)+p('“I noticed that …”   “I tested it by …”   “I know because …”',38,600))
put('p2l1-talk',sec('p2l1-talk','72–80 MIN',body,'Minutes 72 to 80. Pairs talk for 2 minutes, then share. Answer: 401 is bigger. Compare the hundreds first: 4 hundreds is more than 3 hundreds, so the tens and ones do not matter. Count on from 399: 400, 401. Second question if time: "How do you know you found every number from your digit cards?" (we listed them in order; each card started the same number of numbers). Praise the reasons, not only the answers.'))
body=h2('Exit ticket')+card(chip('EXIT TICKET')+p('Use the digit cards 6, 0 and 2 once each. Write the biggest and the smallest 3-digit number.',46,600))+card(p('Write your answer on a slip of paper. Show it to your tutor. Then collect your stamp in your inquiry journal.',34,400))
put('p2l1-exit',sec('p2l1-exit','80–90 MIN',body,'Minutes 80 to 90. Answer: biggest 620, smallest 206 (not 026, which is not a 3-digit number). Extension: use any three of the cards 1, 3, 5 and 7. How many different 3-digit numbers can you make? (24)'))

# ---------- write ----------
order=['p2l1-title','p2l1-warm1','p2l1-warm2','p2l1-explore1','p2l1-explore2','p2l1-teach1','p2l1-try1','p2l1-we1','p2l1-try2','p2l1-teachzero','p2l1-key','p2l1-break','p2l1-ws1','p2l1-ws1ans','p2l1-teachchart','p2l1-teachcount','p2l1-teachriddle','p2l1-ws2','p2l1-ws2ans','p2l1-stretch','p2l1-challenge','p2l1-chdiag','p2l1-chwalk','p2l1-talk','p2l1-exit']
assert set(order)==set(S), set(order)^set(S)
sd=os.path.join(D,'slides')
for f in os.listdir(sd):
    if f.endswith('.html') and f[:-5] not in S: os.remove(os.path.join(sd,f))
for i,h in S.items(): open(os.path.join(sd,i+'.html'),'w').write(h)
deck={'v':4,'createdOnFiles':{'v':1,'at':datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')},'lists':'css',
 'title':'Math Inquirers P2: Lesson 1 – Digit Detectives','order':order,'cover':'p2l1-title',
 'sections':{'s1':{'description':'Warm-up and explore','start':'p2l1-title'},'s2':{'description':'Teach: place value and listing in order','start':'p2l1-teach1'},'s3':{'description':'Worksheet with teaching before each page','start':'p2l1-break'},'s4':{'description':'Stretch, challenge, talk and exit','start':'p2l1-stretch'}},
 'faces':{'fredoka':{'family':'Fredoka','href':'https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&display=swap'},'nunito-sans':{'family':'Nunito Sans','href':'https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@400;600;700&display=swap'}},
 'designSystems':[]}
json.dump(deck,open(os.path.join(D,'deck.json'),'w'),indent=1,ensure_ascii=False)
print(len(order),'slides')
