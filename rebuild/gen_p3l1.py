"""Math Inquirers P3, Lesson 1: Number Sleuths. Writes split/p3l1/project (deck.json + slides/*.html)."""
import json,os,sys,datetime
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,H)
import slidekit
from slidekit import *
slidekit.FOOT='Math Inquirers P3 Holiday Program  •  Notice it. Test it. Explain why.'
D=os.path.join(H,'..','split','p3l1','project'); S={}
def put(i,h): S[i]=h
LN=1; TITLE='Number Sleuths'; TOPIC='Numbers to 10 000'; PRE='p3l1-'
def ol(items,size=34): return f'<ol style="font-size:{size}px;font-weight:600;padding-left:48px;display:flex;flex-direction:column;gap:8px">'+''.join(f'<li>{E(x)}</li>' for x in items)+'</ol>'
def numcard(n,text,size=38): return card(p(f'<span style="color:{TEAL}">{n}</span>  {E(text)}',size,600,raw=True))
def check2(sid,time,title,rows,notes,gap=150,size=34,lw=170):
    body=h2(title)
    for i,(a,b) in enumerate(rows):
        top=250+i*gap
        body+=pin(128,top,lw-20,f'<p style="font-size:36px;font-weight:800;color:{TEAL}">{E(a)}</p>',None,WHITE,20,'18px 24px')
        body+=pin(128+lw,top,1664-lw,f'<p style="font-size:{size}px;font-weight:800;line-height:1.25">{E(b)}</p>','pop',YEL,20,'16px 26px')
    return sec(sid,time,body,notes)
def title_slide(sid,today,notes):
    return (f'<section id="{sid}" data-transition="fade" style="background:{NAVY};color:{CREAM};font-family:{BF};padding:128px 128px 160px;display:flex;flex-direction:column;justify-content:center;gap:36px">\n'
            f'<p style="font-size:32px;font-weight:700;letter-spacing:4px;color:{YEL}">PRIMARY 3  •  LESSON {LN}  •  WEEK 1</p>\n'
            f'<h1 style="font-family:{HF};font-size:128px;font-weight:600;line-height:1.05">{E(TITLE)}</h1>\n'
            f'<p style="font-size:44px;color:#C9D4EC">{E(TOPIC)}</p>\n'
            f'<div style="background:#26385F;border-radius:24px;padding:40px;display:flex;flex-direction:column;gap:12px"><p style="font-size:28px;font-weight:700;letter-spacing:3px;color:{YEL}">TODAY WE WILL</p><p style="font-size:44px;font-weight:600">{E(today)}</p></div>\n'
            f'<p style="position:absolute;left:128px;bottom:64px;width:1400px;font-size:24px;color:#B7C3DD">{E(slidekit.FOOT)}</p>\n<aside>{E(notes)}</aside>\n</section>\n')
def break_slide(sid,text,notes):
    return (f'<section id="{sid}" data-transition="fade" style="background:{TEAL};color:{CREAM};font-family:{BF};padding:128px 128px 160px;display:flex;flex-direction:column;justify-content:center;gap:36px">\n'
            f'<p style="font-size:32px;font-weight:700;letter-spacing:4px;color:{YEL}">35–40 MIN</p>\n<h2 style="font-family:{HF};font-size:110px;font-weight:600;line-height:1.05">Brain break</h2>\n'
            f'<p style="font-size:48px;font-weight:600">{E(text)}</p>\n<p style="font-size:36px;color:#D7EFEA">Then: a drink of water and back to our seats.</p>\n'
            f'<p style="position:absolute;left:128px;bottom:64px;width:1400px;font-size:24px;color:#D7EFEA">{E(slidekit.FOOT)}</p>\n<aside>{E(notes)}</aside>\n</section>\n')
# ---------- SVG pieces ----------
def cards_svg(ds,cw=110,ch=140,gap=24,label=None,hi=()):
    w=len(ds)*cw+(len(ds)-1)*gap+8; h=ch+8
    s=f'<svg aria-label="{E(label or "Digit cards "+", ".join(ds))}" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="width:{w}px;height:{h}px;flex:none">'
    for i,d in enumerate(ds):
        x=4+i*(cw+gap)
        s+=f'<rect x="{x}" y="4" width="{cw}" height="{ch}" rx="16" fill="{SKY if i in hi else YEL}" stroke="{NAVY}" stroke-width="5"/><text x="{x+cw/2}" y="{4+ch*0.7:.0f}" font-size="{int(ch*0.55)}" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="Fredoka, Arial">{E(d)}</text>'
    return s+'</svg>'
def pv_svg(digs=(None,None,None,None),w=640,label='Place value chart'):
    heads=['Th','H','T','O']; bw=140; g=18; tot=4*bw+3*g; x0=(w-tot)/2
    s=f'<svg aria-label="{E(label)}" viewBox="0 0 {w} 250" xmlns="http://www.w3.org/2000/svg" style="width:{w}px;height:250px;flex:none">'
    for i,hd in enumerate(heads):
        x=x0+i*(bw+g)
        s+=f'<rect x="{x}" y="6" width="{bw}" height="64" rx="12" fill="{TEAL}" stroke="{NAVY}" stroke-width="4"/><text x="{x+bw/2}" y="52" font-size="36" font-weight="800" text-anchor="middle" fill="{CREAM}" font-family="Nunito Sans, Arial">{hd}</text>'
        s+=f'<rect x="{x}" y="84" width="{bw}" height="150" rx="14" fill="{WHITE}" stroke="{NAVY}" stroke-width="4"/>'
        if digs[i] is not None: s+=f'<text x="{x+bw/2}" y="190" font-size="96" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="Fredoka, Arial">{E(str(digs[i]))}</text>'
    return s+'</svg>'

# ---------- title ----------
put(PRE+'title',title_slide(PRE+'title','Build 4-digit numbers, make the greatest and smallest, list every number in order and crack clue puzzles.',
 'Objective: Read and build 4-digit numbers by place value; make the greatest, smallest, odd, even and closest numbers from digit cards; list every number in order (heuristic: make a list in order); solve clue puzzles and continue number patterns (heuristic: look for a pattern). '
 'Materials: Digit cards 0–9 (two sets per child), a place value mat (Th H T O), mini whiteboards, a 10-sided die or a bag of digit cards 0–9 for the warm-up game. '
 'Online: Children cut out the digit cards at the back of the workbook (or write 0–9 on small paper squares) and draw a Th H T O mat on paper. The tutor draws the digits on camera. '
 'Time plan: warm-up 0 to 10, explore 10 to 25, teaching 25 to 35 (click to reveal each step and answer), brain break 35 to 40, worksheet 40 to 70 with short teaching before each page and a check-together slide after it, talk time 70 to 80, exit ticket 80 to 90. If the class is behind, children finish the last question of each page at home; the check slides cover it.'))
# ---------- warm-up 1: game ----------
body=h2('Warm-up: Biggest number wins')
body+=pin(128,250,880,chip('HOW TO PLAY')+ol(['I draw a digit card and read it out.','Write it in Th, H, T or O straight away.','No moving it later!','After four digits, the biggest number scores a point.']),None,WHITE,24,'28px 36px')
body+=pin(1060,250,732,pv_svg(w=700,label='Empty Th H T O board'),None)
body+=pin(128,620,880,p('Round 2: the SMALLEST number wins. Careful: a 4-digit number cannot start with 0.',34,700),None,SOFT,24,'24px 32px')
body+=pin(1060,530,732,p('Sample round: the digits come out  6, 2, 9, 4',34,700),None,WHITE,20,'18px 28px')
body+=answer(1060,640,732,'Best for biggest: 9642')+answer(1060,760,732,'Best for smallest: 2469')
put(PRE+'warm1',sec(PRE+'warm1','0–5 MIN',body,
 'Minutes 0 to 5. Biggest number wins. Children draw a Th H T O board on their whiteboard. Draw a digit card (or roll a 10-sided die) four times; after each digit children must write it in one box straight away and cannot move it. Biggest number scores a point. Play 2 or 3 rounds, then a round where the SMALLEST number wins (0 cannot go in the thousands box). '
 'The sample round shows the idea: click to show the best possible numbers for 6, 2, 9, 4 (9642 biggest, 2469 smallest). '
 'Ask after each round: "Where did you put the 9? Why?" (the thousands place is worth the most). "You got a 1 first. Where should it go when we want the biggest number?" (the ones place: it is small). Listen for the words thousands, hundreds, tens, ones.'))
# ---------- warm-up 2 ----------
qs=[('1.','What is the value of the 7 in 4719?','700'),('2.','3000 + 40 + 5 = ?','3045'),('3.','What is 1 more than 4999?','5000'),('4.','What is 100 less than 6050?','5950'),('5.','Which is greater: 7089 or 7098?','7098')]
body=h2('Quick questions')+''.join(qrow(128,250+i*125,1250,a,b) for i,(a,b,c) in enumerate(qs))+''.join(answer(1420,250+i*125,372,c) for i,(a,b,c) in enumerate(qs))
put(PRE+'warm2',sec(PRE+'warm2','5–10 MIN',body,'Minutes 5 to 10. Read each aloud, give thinking time, whiteboards up together, then click to show. Answers: 700; 3045 (watch for 345: there are no hundreds, so we write 0 in the hundreds place); 5000; 5950 (100 less: the hundreds digit goes down, and 0 hundreds becomes 9 hundreds); 7098 (same thousands and hundreds, compare the tens: 9 tens is more than 8 tens).'))
# ---------- explore ----------
def explore_pic():
    s='<svg aria-label="Digit cards 2, 4, 6, 8 above a number line from 4000 to 6000" viewBox="0 0 1600 250" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:230px;display:block">'
    for i,d in enumerate('2468'):
        x=560+i*130
        s+=f'<rect x="{x}" y="6" width="100" height="120" rx="14" fill="{YEL}" stroke="{NAVY}" stroke-width="4"/><text x="{x+50}" y="90" font-size="70" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="Fredoka, Arial">{d}</text>'
    s+=f'<line x1="200" y1="190" x2="1400" y2="190" stroke="{NAVY}" stroke-width="5"/>'
    for x,t in [(200,'4000'),(800,'5000'),(1400,'6000')]:
        s+=f'<line x1="{x}" y1="172" x2="{x}" y2="208" stroke="{NAVY}" stroke-width="5"/><text x="{x}" y="245" font-size="32" font-weight="800" text-anchor="middle" fill="{TEAL if t=="5000" else NAVY}" font-family="Nunito Sans, Arial">{t}</text>'
    s+=f'<text x="1480" y="200" font-size="32" font-weight="800" text-anchor="middle" fill="{TEAL}" font-family="Nunito Sans, Arial">?</text><text x="120" y="200" font-size="32" font-weight="800" text-anchor="middle" fill="{TEAL}" font-family="Nunito Sans, Arial">?</text>'
    return s+'</svg>'
body=h2('Explore: what to do')+card(chip('EXPLORE')+ol(['Take the cards 2, 4, 6 and 8.','Make 4-digit numbers between 4000 and 6000.','Write each one on your whiteboard.','Which one is closest to 5000?'],36))+card(explore_pic(),extra='padding:16px 32px')
put(PRE+'explore1',sec(PRE+'explore1','10–15 MIN',body,'Minutes 10 to 15. Pairs work with their digit cards (online: their paper cards). Ask them to predict first: "How many numbers do you think there are?" Pairs make every 4-digit number between 4000 and 6000 from 2, 4, 6, 8 (each card once), record each one, then decide which is closest to 5000. Hints: "Which card must go first?" "Keep the 4 in front and change the hundreds digit in order." Ready for more: "How many numbers can you make altogether?" (24).'))
body=h2('Explore: talk about it')+numcard('1.','How many numbers did you make?',40)+numcard('2.','How do you know you have them all?',40)+numcard('3.','Which one is closest to 5000? How do you know?',40)
put(PRE+'explore2',sec(PRE+'explore2','15–25 MIN',body,'Minutes 15 to 25. Let pairs keep working, then gather them. Answers: 1) 6 numbers: 4268, 4286, 4628, 4682, 4826, 4862. 2) Every number must start with 4 (2 is too small, 6 and 8 are too big). Then list in order: hundreds digit 2 (4268, 4286), 6 (4628, 4682), 8 (4826, 4862). Two each, so 6. 3) 4862, only 138 below 5000. Above 5000 the smallest we can make is 6248, which is 1248 away. Praise pairs who listed in order: that is today\'s first heuristic, make a list in order.'))
# ---------- teach ----------
body=h2('Greatest and smallest: start at the left')+pin(128,240,700,cards_svg(list('4081')),None)
body+=pin(760,250,1032,p('The thousands place is worth the most, so decide it first.',36,700),None,SOFT,20,'22px 28px')
body+=step(1,'Greatest: biggest digit first, then the next biggest:  8 4 1 0',top=430,size=36)
body+=step(2,'Smallest: 0 cannot go first. Put the smallest digit that is not 0 first: 1',top=540,size=36)
body+=step(3,'Then the rest from smallest:  1 0 4 8',top=650,size=36)
body+=answer(128,770,1664,'Greatest 8410     Smallest 1048   (not 0148: that is only 148)')
put(PRE+'teach1',sec(PRE+'teach1','25–27 MIN',body,'Teach. Children lay out 4, 0, 8, 1 on their mats. Think-aloud: "Greatest number from 4, 0, 8, 1. The thousands place is worth the most, so the biggest digit goes there: 8. Then 4, then 1, then 0: 8410. Smallest: I want the smallest digit first, but 0 cannot go first or it is not a 4-digit number. So 1 goes first, then 0, then 4, then 8: 1048." Ask: "Is 0148 a 4-digit number?" (No, it is 148.)'))
body=h2('Odd or even? Choose the ones digit FIRST')+card(p('Cards 2, 9, 6, 0. Make the greatest ODD number and the smallest EVEN number.',38,700))
body+=step(1,'Odd numbers end in 1, 3, 5, 7 or 9. The only odd card is 9, so 9 goes in the ones place.',top=400,size=34)
body+=step(2,'Greatest odd: the other cards from biggest, then 9:  6 2 0 9',top=520,size=34)
body+=step(3,'Smallest even: start 2, then 0. The ones digit must be even, so 6 goes last: 2 0 9 6',top=640,size=34)
body+=answer(128,770,1664,'Greatest odd 6209     Smallest even 2096   (2069 is odd)')
put(PRE+'we1',sec(PRE+'we1','27–29 MIN',body,'Click through the steps. Think-aloud: "Odd numbers end in an odd digit. The only odd card is 9, so I put 9 in the ones place FIRST. Then I make the rest as big as I can: 6, 2, 0. So 6209." Ask before step 3: "Smallest number is 2069. Why is that not the answer?" (it ends in 9, so it is odd). Common error: making 9620 first and then trying to fix it.'))
body=h2('Closest to 4000: check both sides')+card(p('Cards 1, 4, 7, 3. Which number is closest to 4000?',38,700))
body+=step(1,'Just ABOVE 4000: start with 4, then the rest as small as possible: 4137. That is 137 more.',top=400,size=34)
body+=step(2,'Just BELOW 4000: start with 3, then the rest as big as possible: 3741. That is 259 less.',top=520,size=34)
body+=step(3,'Compare: 137 is less than 259.',top=640,size=34)
body+=answer(128,750,1664,'4137 is the closest to 4000.')
put(PRE+'we2',sec(PRE+'we2','29–30 MIN',body,'Click through. Draw a quick number line from 3000 to 5000 with 4000 in the middle and mark 3741 and 4137 on it. Think-aloud: "The closest number is either just above or just below 4000, so I make both and compare." To find how far 3741 is from 4000, count on: 3741 → 3800 is 59, 3800 → 4000 is 200, so 259.'))
put(PRE+'try1',try_slide(PRE+'try1','30–31 MIN','Your turn: cards 5, 1, 0, 6','Use your cards. Whiteboards up, then click.',[('a','The greatest number','6510'),('b','The smallest number','1056'),('c','The greatest odd number','6501')],'Whiteboards. a) 6510. b) 1056 (1 first, then 0). c) The odd cards are 1 and 5. Ending in 1: 6501. Ending in 5: 6105. 6501 is greater. Ask: "How did you decide which odd card goes last?" (try both and compare).'))
W2=[300,600]
body=h2('Make a list in order')+card(p('How many 3-digit numbers can you make with the cards 0, 3, 6?',38,700))
body+=trow(128,360,['First digit','Numbers'],W2,None,True)
body+=trow(128,450,['3','306, 360'],W2,'rise')+trow(128,540,['6','603, 630'],W2,'rise')+trow(128,630,['0','not allowed'],W2,'rise')
body+=pin(1180,360,612,p('Fix the first digit. Then list the rest from smallest. 4 numbers, and none missed.',34,700),'fade',SOFT,20,'22px 28px')
body+=qrow(128,750,1250,'Your turn:','How many from 5, 5, 2?',36)+answer(1420,750,372,'3')
put(PRE+'teach2',sec(PRE+'teach2','31–34 MIN',body,'Teach the heuristic MAKE A LIST IN ORDER. Click to add each row. Think-aloud: "I fix the first digit: 3. The other cards are 0 and 6, smallest first: 306, then 360. Next first digit: 6: 603, 630. 0 cannot go first. 4 numbers, and the list shows I have them all." Your turn (whiteboards): 5, 5, 2 gives 255, 525, 552, only 3, because the two 5s are the same. If time: 1, 2, 3 gives 6 numbers (123, 132, 213, 231, 312, 321).'))
body=h2('Key idea: start at the biggest place')+card(p('Decide the thousands digit first. To find every number, fix the first digit and list the rest in order.',44,700))+card(p('Odd or even? Choose the ones digit first.',38,600,MUTED))
put(PRE+'key',sec(PRE+'key','34–35 MIN',body,'Say the key idea together. Common mistakes to watch for during the worksheet: (1) Putting 0 first for the smallest number (0357 is really 357, a 3-digit number). (2) For the greatest odd number, making the greatest number first and then trying to fix it, instead of choosing the ones digit first. (3) Listing numbers in a random order, so some are missed or written twice (especially with the two 5s in Q2).'))
put(PRE+'break',break_slide(PRE+'break','Place value moves. I say a 4-digit number: jump for each thousand, clap for each hundred, tap your knees for each ten, touch your toes for each one.','Five minutes. Try 3021 (3 jumps, 0 claps, 2 knee taps, 1 toe touch), then 1203 and 2110. Online: children stay in view of the camera and move in place.'))
# ---------- before page 1: patterns ----------
body=h2('Look for a pattern: find the jumps')+card(p('5000,   4990,   4970,   4940,   ____,   ____',48,700))
body+=step(1,'Find each jump:  5000 → 4990 is − 10,   4990 → 4970 is − 20,   4970 → 4940 is − 30',top=420,size=34)
body+=step(2,'The jump grows by 10 each time. So the next jumps are − 40, then − 50.',top=530,size=34)
body+=step(3,'4940 − 40 = 4900,   4900 − 50 = 4850',top=640,size=34)
body+=answer(128,750,1664,'Always check the rule on EVERY jump, not just the first one.')
put(PRE+'teachpat',sec(PRE+'teachpat','40–42 MIN',body,'Teach the heuristic LOOK FOR A PATTERN before worksheet page 1 (Q3). Ask first: "What comes next?" Some children say 4930 (take away 10 each time) because they only checked the first jump. Click to show each jump. Then: "Some patterns add the same amount every time, some grow. Write the jumps between the numbers to find out."'))
put(PRE+'ws1',ws_preview(PRE+'ws1','42–52 MIN','Worksheet page 1: with your partner',[('Q1','Cards 3, 0, 7, 5: greatest, smallest, greatest odd, closest to 5000.'),('Q2','Make a list in order: every number from 2, 0, 5, 5.'),('Q3','Look for a pattern. Write the jumps first.')],'Use your digit cards on the mat, then write the number.','Minutes 42 to 52. Walk around. Ask "How do you know?" before giving any help. For Q1d check that pairs try a number above AND below 5000. For Q2 check that they fix the first digit and go in order, and that they do not write 2505 twice.'))
put(PRE+'ws1ans',check2(PRE+'ws1ans','52–54 MIN','Page 1: check together',[
 ('Q1','a) 7530   b) 3057   c) 7503   d) 5037: only 37 away; below 5000 the best is 3750, 1250 away'),
 ('Q2','2055, 2505, 2550, 5025, 5052, 5205, 5250, 5502, 5520.   a) 9   b) 4'),
 ('Q3','a) 9550, 9450   b) 4567, 5678   c) 1015, 1021   d) yes, 5000 is in it; right after it comes 5250')],
 'Click each answer after a pair explains theirs. Q1c: the odd cards are 3, 5 and 7; ending in 3 gives 7503, ending in 5 gives 7305, ending in 7 gives 5307. Q2: 3 numbers start with 2 and 6 start with 5 (the two 5s are the same, so 5 numbers are not doubled). Q3a take away 100; b add 1111; c the jumps are 1, 2, 3, 4, so next 5 and 6; d keep adding 250: 4000, 4250, 4500, 4750, 5000 (yes, it is in the pattern), then 5250 right after it.',gap=190))
# ---------- before page 2 ----------
body=h2('Renaming: 12 hundreds is 1 thousand 2 hundreds')+card(p('What number is 3 thousands, 12 hundreds, 5 tens and 14 ones?',40,700))
body+=step(1,'3 thousands = 3000.   12 hundreds = 1200.',top=420,size=36)
body+=step(2,'5 tens = 50.   14 ones = 14.',top=530,size=36)
body+=step(3,'Add them:  3000 + 1200 + 50 + 14 = 4264',top=640,size=36)
body+=answer(128,760,1664,'Check: 4264 has 4 thousands, 2 hundreds, 6 tens and 4 ones.')
put(PRE+'teachrename',sec(PRE+'teachrename','54–55 MIN',body,'Teach before worksheet page 2 (Q4). Show it with place value blocks or a drawing if possible: 10 hundreds make 1 thousand. Common error: writing the parts side by side, 3 | 12 | 5 | 14, to get 312514. Ask: "Can a place hold more than 9?" (Not when we write the number: we must rename.)'))
CL=['Clue 1: I am between 2000 and 3000.','Clue 2: My ones digit is 3 times my thousands digit.','Clue 3: My tens digit is 1 less than my ones digit.','Clue 4: My hundreds digit is my tens digit take away my thousands digit.']
body=h2('What number am I? One clue at a time')+pin(128,230,1664,''.join(p(c,32,600) for c in CL),None,WHITE,20,'20px 30px')
SL=['Th = 2','O = 3 × 2 = 6','T = 6 − 1 = 5','H = 5 − 2 = 3.  I am 2356.']
body+=pin(128,500,700,pv_svg((None,None,None,None),640,'Empty Th H T O chart'),None,CREAM,0,'0px')
for i,dg in enumerate([(2,None,None,None),(2,None,None,6),(2,None,5,6),(2,3,5,6)]):
    body+=pin(880,500+i*95,912,p(SL[i],36,700),'rise',WHITE,20,'14px 26px')
    body+=pin(128,500,700,pv_svg(dg,640,'Th H T O chart, step '+str(i+1)),'fade',CREAM,0,'0px')
put(PRE+'teachclues',sec(PRE+'teachclues','55–57 MIN',body,'Teach before worksheet page 2 (Q5). Use ONE clue at a time and fill one box at a time. Each clue takes two clicks: first the step appears, then its digit appears in the chart. Finish by checking every clue against 2356 aloud. Ask: "Which clue did you use first? Why that one?" (Clue 1 gives a digit straight away.)'))
put(PRE+'tryclues',try_slide(PRE+'tryclues','57–58 MIN','Your turn: clue puzzles','3-digit numbers, all digits different, digits add up to 4.',[('a','The smallest such number?','103'),('b','The greatest such number?','310'),('c','Between 7000 and 8000, my other three digits are all 2.','7222')],'Whiteboards. a) and b): the only three different digits that add to 4 are 0, 1 and 3 (0 + 1 + 2 is only 3, and 0 + 1 + 3 = 4). Smallest: 103. Greatest: 310. Ask: "How do you know there are no other digits?" c) 7222. This prepares Q5b on the worksheet, where FOUR different digits add up to 6.',size=36))
W3=[250,480,220]
body=h2('Digits that add up to 3: make a list in order')+card(p('How many 3-digit numbers have digits that add up to 3?',38,700))
body+=trow(128,370,['First digit','Numbers','How many'],W3,None,True)
for i,r in enumerate([['3','300','1'],['2','210, 201','2'],['1','120, 111, 102','3']]): body+=trow(128,460+i*90,r,W3,'rise')
body+=pin(1260,370,532,p('Start with the biggest first digit. Then the next digit goes down by 1 each time.',34,700),None,SOFT,20,'22px 26px')
body+=answer(128,760,1664,'6 numbers altogether.   Can the first digit be 0? No!')
put(PRE+'teachsum',sec(PRE+'teachsum','58–60 MIN',body,'Teach before worksheet page 2 (Q6, which asks the same question for 4-digit numbers). Click to add each row. Think-aloud for the last row: "First digit 1, so the other two digits add up to 2: 2 and 0 (120), 1 and 1 (111), 0 and 2 (102)." Ask: "What do you notice about the How many column?" (1, 2, 3). Do not tell them the 4-digit answer.'))
put(PRE+'ws2',ws_preview(PRE+'ws2','60–67 MIN','Worksheet page 2: on your own',[('Q4','Place value puzzles. Rename when a place has more than 9.'),('Q5','What number am I? One clue at a time. Q5b is for if you have time.'),('Q6','If time: digits that add up to 3. Make a list in order.')],'Ready for more? Q5b and Q6, then Stretch and Challenge.','Page 2, on your own: Q4 place value puzzles; Q5(a) what number am I?; then Q5(b) and Q6 (digits that add up to 3) if you have time. Children work alone. Note who needs a short catch-up next lesson. For Q5b ask: "Which four different digits can add up to only 6?"'))
put(PRE+'ws2ans',check2(PRE+'ws2ans','67–69 MIN','Page 2: check together',[
 ('Q4','a) 5527   b) 13 hundreds   c) No: 23 tens is 230, so it is 6230'),
 ('Q5','a) 6903   b) greatest 3201, smallest 1023 (digits 0, 1, 2, 3)'),
 ('Q6','10: 3000; 2100, 2010, 2001; 1200, 1110, 1101, 1020, 1011, 1002.   1, 3, 6')],
 'Click each answer after a child explains. Q4b: 7305 = 6000 + 1300 + 5. Q5a: thousands 6, ones half of 6 = 3, hundreds = 6 + tens + 3; a digit is at most 9, so tens is 0 and hundreds is 9. Q5b: the smallest four different digits, 0 + 1 + 2 + 3, already add up to 6, so the digits must be 0, 1, 2, 3. Odd means it ends in 1 or 3. Q6b: the counts 1, 3, 6 go up by 2, then 3.',gap=190))
# ---------- stretch / challenge ----------
st=[('1.','What is the smallest 4-digit number with all different digits that add up to 10?'),('2.','How many times do you write the digit 5 when you write all the numbers from 1 to 100?'),('3.','Continue the pattern: 1, 3, 7, 15, 31, ___, ___')]
put(PRE+'stretch',sec(PRE+'stretch','For early finishers',h2('Stretch')+''.join(numcard(a,b) for a,b in st),'Answers: 1) 1027 (start 1, then 0; the last two digits must add to 9 and cannot be 0 or 1, so 2 then 7). 2) 20 (ten times in the ones place: 5, 15, …, 95; ten times in the tens place: 50 to 59; 55 has two 5s). 3) 63, 127 (double and add 1; or the jumps double: 2, 4, 8, 16, then 32 and 64).'))
ch=[('1.','A 4-digit number has all different digits. Its thousands digit is the sum of its other three digits. What is the greatest such number? What is the smallest?'),('2.','Mei uses the cards 1, 2, 3, 4 once each to make 4-digit numbers. She lists them all from smallest to greatest. What is the 10th number in her list?')]
put(PRE+'challenge',sec(PRE+'challenge','Challenge',h2('Challenge')+''.join(numcard(a,b,36) for a,b in ch),'Pairs try first, then use the "see it" slide if stuck, then the walk-through. Answers: 1) Greatest 9810 (9 = 8 + 1 + 0). Smallest 3012 (the smallest sum of three different digits is 0 + 1 + 2 = 3). 2) 2341 (6 numbers start with 1; then 2134, 2143, 2314, 2341).'))
def diag1():
    s=f'<svg aria-label="Four boxes Th H T O: the thousands digit equals the sum of the other three" viewBox="0 0 800 440" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;display:block">'
    for i,hd in enumerate(['Th','H','T','O']):
        x=70+i*175
        s+=f'<text x="{x+70}" y="50" font-size="34" font-weight="800" text-anchor="middle" fill="{TEAL}" font-family="Nunito Sans, Arial">{hd}</text><rect x="{x}" y="70" width="140" height="140" rx="16" fill="{YEL if i==0 else WHITE}" stroke="{NAVY}" stroke-width="5"/><text x="{x+70}" y="170" font-size="80" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="Fredoka, Arial">?</text>'
    s+=f'<path d="M420 230 L420 260 L770 260 L770 230 M245 230 L245 260 L420 260" fill="none" stroke="{NAVY}" stroke-width="4"/><path d="M595 260 L595 300 L140 300 L140 230" fill="none" stroke="{TEAL}" stroke-width="5"/><polygon points="140,222 128,244 152,244" fill="{TEAL}"/>'
    s+=f'<text x="400" y="355" font-size="34" font-weight="800" text-anchor="middle" fill="{NAVY}" font-family="Nunito Sans, Arial">Th = H + T + O</text><text x="400" y="410" font-size="30" font-weight="700" text-anchor="middle" fill="{MUTED}" font-family="Nunito Sans, Arial">All four digits different. Greatest? Smallest?</text>'
    return s+'</svg>'
def diag2():
    s=f'<svg aria-label="Cards 1, 2, 3, 4 and an ordered list with gaps" viewBox="0 0 800 440" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;display:block">'
    for i,d in enumerate('1234'):
        x=230+i*90; s+=f'<rect x="{x}" y="10" width="70" height="86" rx="12" fill="{YEL}" stroke="{NAVY}" stroke-width="4"/><text x="{x+35}" y="72" font-size="50" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="Fredoka, Arial">{d}</text>'
    rows=[('1st','1 2 3 4'),('2nd','1 2 4 3'),('…','starts with 1'),('7th','2 _ _ _'),('…',''),('10th','?')]
    for i,(a,b) in enumerate(rows):
        y=112+i*48
        s+=f'<rect x="150" y="{y}" width="500" height="42" rx="8" fill="{WHITE if i%2 else SKY}" stroke="{NAVY}" stroke-width="2"/><text x="215" y="{y+32}" font-size="30" font-weight="800" text-anchor="middle" fill="{TEAL}" font-family="Nunito Sans, Arial">{a}</text><text x="440" y="{y+32}" font-size="30" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="Fredoka, Arial">{E(b)}</text>'
    s+=f'<text x="400" y="435" font-size="28" font-weight="700" text-anchor="middle" fill="{MUTED}" font-family="Nunito Sans, Arial">How many start with 1?</text>'
    return s+'</svg>'
body=h2('Challenge: see it',60)+'<div style="display:flex;gap:32px;align-items:flex-start">'+card(f'<p style="font-size:28px;font-weight:700;color:{TEAL}">Q1: The thousands digit is the sum</p>'+diag1(),extra='flex:1;min-width:0;padding:20px 24px')+card(f'<p style="font-size:28px;font-weight:700;color:{TEAL}">Q2: The 10th number</p>'+diag2(),extra='flex:1;min-width:0;padding:20px 24px')+'</div>'
put(PRE+'chdiag',sec(PRE+'chdiag','Challenge',body,'Show after pairs have tried, or if they are stuck. The pictures show the problem, not the answer. Ask: What do you notice? What do we know? Where should we start? For Q1: "To make the number greatest, what should the thousands digit be?" For Q2: "Can you list the numbers that start with 1 in order?"'))
body=h2('Challenge: walk-through')+pin(128,250,800,p('Q1: greatest, then smallest',36,800,TEAL))
for i,t in enumerate(['Greatest: Th = 9. Three different digits, not 9, that add to 9.','Biggest hundreds digit: 8. Then 1 + 0. So 9810.','Smallest: the smallest sum of 3 different digits is 0 + 1 + 2 = 3.','So Th = 3, then 0, 1, 2 in order: 3012.']): body+=pin(128,330+i*120,800,p(t,30),'rise',WHITE)
body+=pin(992,250,800,p('Q2: make a list in order',36,800,TEAL))
for i,t in enumerate(['Start with 1: 1234, 1243, 1324, 1342, 1423, 1432. That is 6.','7th 2134,  8th 2143','9th 2314,  10th 2341','Answer: 2341. A list in order lets us count without missing any.']): body+=pin(992,330+i*120,800,p(t,30),'rise',WHITE)
put(PRE+'chwalk',sec(PRE+'chwalk','Challenge',body,'Use after pairs have tried. Q1: the big idea is to decide the most important place first. For the smallest, ask: "Could the thousands digit be 1 or 2?" (No: three DIFFERENT digits add up to at least 0 + 1 + 2 = 3.) Q2: some children notice that 6 numbers start with each card, so the 7th to 12th numbers start with 2; then they only need to list those in order.'))
body=h2('Talk time')+card(chip('TALK TIME',YEL,NAVY)+p('Mei says the smallest 4-digit number she can make with 3, 0, 7, 5 is 0357. Do you agree?',42))+card(p('Sentence starters:',34,400,MUTED)+p('“I noticed that …”   “I tested it by …”   “I know because …”',38))
put(PRE+'talk',sec(PRE+'talk','70–80 MIN',body,'Minutes 70 to 80. Pairs talk for 2 minutes, then share. Answer: No. 0357 is really 357, a 3-digit number. The smallest 4-digit number is 3057: the smallest digit that is not 0 goes first, then 0. Follow-up: "How do you know you found ALL the numbers in a list?" (We fixed the first digit and listed the rest in order, so nothing is missed or repeated.) Praise the reasons, not only the answers.'))
body=h2('Exit ticket')+card(chip('EXIT TICKET')+p('Use the cards 6, 0, 3, 8 once each. Write the smallest 4-digit number and the greatest odd 4-digit number.',44))+card(p('Write your answer on a slip of paper. Show it to your tutor. Then collect your stamp in your inquiry journal.',34,400))
put(PRE+'exit',sec(PRE+'exit','80–90 MIN',body,'Minutes 80 to 90. Answer: smallest 3068; greatest odd 8603 (3 is the only odd card, so it goes in the ones place). Extension: with the cards 1, 2, 3, 4, how many 4-digit numbers can you make? How many are odd? (24 numbers; 12 are odd.)'))

ORDER=['title','warm1','warm2','explore1','explore2','teach1','we1','we2','try1','teach2','key','break','teachpat','ws1','ws1ans','teachrename','teachclues','tryclues','teachsum','ws2','ws2ans','stretch','challenge','chdiag','chwalk','talk','exit']
ORDER=[PRE+x for x in ORDER]
import p3_gifted; ORDER[:]=p3_gifted.add(S,ORDER,1)  # close-the-gaps: warm-up check + look-back slides
assert set(ORDER)==set(S), set(ORDER)^set(S)
os.makedirs(os.path.join(D,'slides'),exist_ok=True)
for f in os.listdir(os.path.join(D,'slides')):
    if f.endswith('.html') and f[:-5] not in S: os.remove(os.path.join(D,'slides',f))
for i,h in S.items(): open(os.path.join(D,'slides',i+'.html'),'w').write(h)
deck={'v':4,'createdOnFiles':{'v':1,'at':datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')},'lists':'css',
 'title':f'Math Inquirers P3: Lesson {LN} – {TITLE}','order':ORDER,'cover':ORDER[0],
 'sections':{'s1':{'description':'Warm-up and explore','start':PRE+'title'},'s2':{'description':'Teach: greatest, smallest and make a list in order','start':PRE+'teach1'},'s3':{'description':'Worksheet with teaching before each page','start':PRE+'break'},'s4':{'description':'Think harder, go further, talk and exit','start':PRE+'stretch'}},
 'faces':{'fredoka':{'family':'Fredoka','href':'https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&display=swap'},'nunito-sans':{'family':'Nunito Sans','href':'https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@400;600;700&display=swap'}},
 'designSystems':[]}
json.dump(deck,open(os.path.join(D,'deck.json'),'w'),indent=1,ensure_ascii=False)
print(len(ORDER),'slides')
