"""Math Inquirers P5, Lesson 1: Million Puzzles. Writes split/p5l1/project (deck.json + slides/*.html)."""
import json,os,sys,datetime
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,H)
import slidekit
from slidekit import *
slidekit.FOOT='Math Inquirers P5 Holiday Program  •  Notice it. Test it. Explain why.'
D=os.path.join(H,'..','split','p5l1','project'); os.makedirs(os.path.join(D,'slides'),exist_ok=True)
S={}
def put(i,h): S[i]=h
RED='#D64545'; FOOTX=slidekit.FOOT

# ---------- shared slide shapes (same look as the approved decks) ----------
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
def dcards(digits,x0=0,y=6,w=96,h=124,gap=26,fill=YEL,size=70):
    g=''
    for i,d in enumerate(digits):
        x=x0+i*(w+gap)
        g+=f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="16" fill="{fill}" stroke="{NAVY}" stroke-width="5"/>'+txt(x+w/2,y+h/2+size*0.35,d,size)
    return g
PV=['M','HTh','TTh','Th','H','T','O']
def pvchart(x0,y,digits=None,cw=150,ch=110,fills=None):
    """7-column place-value chart; digits: list of 7 strings ('' for empty)"""
    g=''
    for i,lab in enumerate(PV):
        x=x0+i*cw
        g+=f'<rect x="{x}" y="{y}" width="{cw}" height="56" fill="{YEL}" stroke="{NAVY}" stroke-width="4"/>'+txt(x+cw/2,y+40,lab,30)
        f=(fills[i] if fills and fills[i] else WHITE)
        g+=f'<rect x="{x}" y="{y+56}" width="{cw}" height="{ch}" fill="{f}" stroke="{NAVY}" stroke-width="4"/>'
        if digits and digits[i]!='': g+=txt(x+cw/2,y+56+ch/2+24,digits[i],68)
    return g
def sstep(n,html,top,left=128,width=1664,size=36,build='rise'):
    inner=f'<p style="font-size:{size}px;font-weight:600;line-height:1.3"><span style="color:{TEAL};font-weight:800">Step {n}.</span>  {html}</p>'
    return pin(left,top,width,inner,build,WHITE,20,'18px 28px')

# ---------- 1. title ----------
put('p5l1-title',title_slide('p5l1-title','LESSON 1  •  WEEK 1','Million Puzzles','Numbers to 10 million and the four operations',
 'Read and build numbers up to 10 million, solve digit puzzles, estimate to catch mistakes and use brackets to hit a target.',
 'Objective: Read, write and compare numbers up to 10 million; solve digit-card and digit-riddle puzzles with place value (testing the best number just below AND just above a target); estimate to check large calculations; and use the order of operations and brackets to hit target numbers. '
 'Thinking strategies taught today: TEST BOTH SIDES of a target, USE THE CLUES IN ORDER and check every clue, ESTIMATE by rounding, and WRITE THE RANGE FIRST before a "find all". '
 'Materials: Digit cards 0 to 9 (one set per child), a 7-column place-value mat (M, HTh, TTh, Th, H, T, O), mini whiteboards, a calculator for the explore only, workbook. '
 'Online: children cut out paper digit cards and draw a 7-box mat before the lesson and hold them up to the camera; the tutor writes on the slides; pairs use breakout rooms for the explore and page 1. '
 'Time plan: warm-up 0 to 9, explore 9 to 21, teaching 21 to 33 (click to reveal each step and answer), brain break 33 to 37, worksheet page 1 37 to 49, check together 49 to 51, short teaching before page 2 51 to 57, worksheet page 2 57 to 72 (alone), check together 72 to 76, talk time 76 to 82, exit ticket 82 to 90. Stretch and challenge are for children who finish early, or for home.'))

# ---------- 2. warm-up game ----------
g=pvchart(20,40,['','','','','','',''],cw=150,ch=120)
g+=dcards([4],1150,70,110,140)+txt(1205,262,'first card',28,MUTED,weight=600,font='Nunito Sans, Arial')
g+=txt(1400,150,'Target:',32,TEAL)+txt(1400,200,'5 000 000',40,TEAL)
body=h2('Warm-up: Million Maker')+card(p('I turn over one digit card at a time. Write it in a box straight away. No moving it later! Closest to 5 000 000 wins.',38,700))
body+=pin(128,430,1664,svgwrap(1560,280,'Seven empty place-value boxes from millions to ones, a digit card 4 and the target 5 000 000',g),None,WHITE,24,'16px 40px')
body+=pin(128,770,1664,p('Where would you put a 4? A 5? A 0? A 9?',38,700),'fade',SOFT,20,'20px 30px')
put('p5l1-warm1',sec('p5l1-warm1','0–4 MIN',body,
 'Minutes 0 to 4. Million Maker. Children draw seven boxes (M, HTh, TTh, Th, H, T, O) on a whiteboard. Shuffle digit cards 0 to 9 and turn over one at a time (online: hold it up to the camera). After EACH card, children write it in one empty box at once and cannot move it. After seven cards, each child reads their number aloud; the one closest to 5 000 000 wins. Play 2 or 3 rounds. '
 'Click to show the thinking question. Talk: "A 4 or a 5 belongs in the millions box: they are next to the target. After a 4, you want BIG digits next (4 9 8 …). After a 5, you want SMALL digits next (5 0 1 …)." '
 'Listen for children who say "it depends whether I start with 4 or 5". That is today\'s big idea: test both sides of a target.'))

# ---------- 3. quick questions ----------
qs=[('1.','Write in numerals: 3 million, 40 thousand and 6','3 040 006'),('2.','The value of the 7 in 2 716 450?','700 000'),('3.','4 560 000 ÷ 1000 = ?','4560'),('4.','Round 6 849 500 to the nearest thousand','6 850 000'),('5.','8 + 4 × 5 − 6 ÷ 2 = ?','25')]
body=h2('Quick questions')+''.join(qrow(128,250+i*128,1250,a,b,36) for i,(a,b,c) in enumerate(qs))+''.join(answer(1420,250+i*128,372,c) for i,(a,b,c) in enumerate(qs))
put('p5l1-warm2',sec('p5l1-warm2','4–9 MIN',body,'Minutes 4 to 9. Read each aloud, whiteboards up together, then click to show. 1) Watch for 340 006: the zeros hold the hundred thousands, thousands, hundreds and tens places. 2) The 7 is in the hundred thousands place. 3) Dividing by 1000 moves every digit three places to the right. 4) The hundreds digit is 5, so round up: 849 thousands becomes 850 thousands. 5) × and ÷ first: 8 + 20 − 3 = 25. Ask: "Who got 27 or 57? What did you do first?"'))

# ---------- 4. explore: what to do ----------
sw=(f'<circle cx="150" cy="140" r="100" fill="{WHITE}" stroke="{NAVY}" stroke-width="7"/><rect x="132" y="18" width="36" height="26" rx="6" fill="{NAVY}"/>'
    f'<line x1="150" y1="140" x2="150" y2="68" stroke="{RED}" stroke-width="7" stroke-linecap="round"/><line x1="150" y1="140" x2="205" y2="160" stroke="{NAVY}" stroke-width="7" stroke-linecap="round"/><circle cx="150" cy="140" r="10" fill="{NAVY}"/>')
cnt=f'<rect x="330" y="70" width="560" height="140" rx="20" fill="{NAVY}"/>'+txt(610,165,'1 000 000 s',68,YEL)
arr=f'<line x1="920" y1="140" x2="1060" y2="140" stroke="{TEAL}" stroke-width="8"/><polygon points="1090,140 1056,120 1056,160" fill="{TEAL}"/>'
cal=(f'<rect x="1120" y="40" width="220" height="200" rx="16" fill="{WHITE}" stroke="{NAVY}" stroke-width="6"/><rect x="1120" y="40" width="220" height="56" rx="16" fill="{RED}"/>'
     +txt(1230,200,'?',100,TEAL)+txt(1450,130,'days?',48,TEAL))
steps=''.join(f'<li>{E(s)}</li>' for s in ['Guess first: is a million seconds about an hour, a day, a week, a month or a year?','Work out how many seconds there are in 1 hour.','Work out how many seconds there are in 1 day.','How many days is 1 000 000 seconds? Compare with your guess.'])
body=h2('Explore: how long is a million seconds?')+card(chip('EXPLORE')+f'<ol style="font-size:34px;font-weight:600;padding-left:52px;display:flex;flex-direction:column;gap:6px">{steps}</ol>')
body+=card(svgwrap(1580,260,'A stopwatch, a counter showing 1 000 000 seconds, an arrow and a calendar page with a question mark',sw+cnt+arr+cal),extra='padding:16px 32px')
put('p5l1-explore1',sec('p5l1-explore1','9–14 MIN',body,'Minutes 9 to 14. Pairs. Everybody writes a guess first and does not change it (most children guess a week, a month or a year). Let them work with pencil first; allow a calculator only for checking. Early finishers: how long is 10 million seconds? More or less than a school term?'))

# ---------- 5. explore: talk ----------
body=h2('Explore: talk about it')+numcards([('1.','How many seconds are there in 1 day? How did you work it out?'),('2.','About how many days is a million seconds? Was your guess close?'),('3.','About how long is 10 million seconds?')],40)
put('p5l1-explore2',sec('p5l1-explore2','14–21 MIN',body,'Minutes 14 to 21. Let pairs keep working, then gather them. Collect the guesses first: a show of hands for hour, day, week, month, year. Answers: 1) 60 × 60 = 3600 seconds in an hour, 3600 × 24 = 86 400 seconds in a day. 2) 10 days = 864 000 s (not enough), 11 days = 950 400 s, 12 days = 1 036 800 s (too many), so a million seconds is between 11 and 12 days: about 11 and a half days. 3) About 116 days, nearly 4 months (10 times as long). '
 'Ask: "Did you multiply or add? Why is multiplying faster?" and "How did you get close without dividing exactly?" (try 10 days, then add a day at a time). Point out the strategy: estimate, then test numbers either side. That links to the digit puzzles next.'))

# ---------- 6. teach: place value ----------
g=pvchart(20,20,['4','0','5','3','0','0','0'],cw=170,ch=120,fills=[SKY,None,None,None,None,None,None])
for x1,x2,lab in [(20,190,'millions'),(190,700,'thousands'),(700,1210,'ones')]:
    g+=f'<path d="M{x1+10} 212 V232 H{x2-10} V212" fill="none" stroke="{TEAL}" stroke-width="5"/>'+txt((x1+x2)/2,272,lab,30,TEAL)
body=h2('Big numbers: groups of three')+pin(128,240,1664,svgwrap(1240,290,'Place-value chart showing 4 053 000 with the groups millions, thousands and ones',g),None)
body+=pin(1400,250,392,p('4 053 000',56,700),None,SOFT,20,'20px 26px')
body+=sstep(1,'Read in groups of three from the right: <b>four million, fifty-three thousand</b>.',560,size=34)
body+=sstep(2,'The digit 3 is in the thousands place. Its <b>value</b> is 3000.',660,size=34)
body+=sstep(3,'But how many thousands make 4 053 000? 4 053 000 ÷ 1000 = <b>4053 thousands</b>.',760,size=34)
put('p5l1-teach1',sec('p5l1-teach1','21–24 MIN',body,'Teach. Build 4 053 000 on the place-value mat. Click through the steps. Think-aloud: "The space after every three digits from the right is a comma in words: four million, fifty-three thousand. The 0 in the hundred thousands place still has to be written: it holds the place." '
 'Step 3 is the trap: the DIGIT in the thousands place is 3, but the number has 4053 thousands altogether (4 million is 4000 thousands, plus 53 thousands). Ask: "How many hundreds make 4 053 000?" (40 530).'))
put('p5l1-try1',try_slide('p5l1-try1','24–25 MIN','Your turn: whiteboards','Group in threes. Watch the zeros.',[('a','Write: six million, two hundred and five thousand and thirty','6 205 030'),('b','The value of the 9 in 1 290 400?','90 000'),('c','How many hundreds make 2 400 000?','24 000')],'Whiteboards up together, then click. a) Watch for 6 205 30 or 6 250 030: thirty is 0 hundreds, 3 tens, 0 ones. b) The 9 is in the ten thousands place. c) 2 400 000 ÷ 100 = 24 000.',size=34))

# ---------- 8. worked example: closest to a target ----------
g=dcards([0,1,2,4,5,7,8],10,6,100,120,24,YEL,64)
body=h2('Worked example: closest to 5 000 000')+card(p('Use all seven cards once each. Make the number closest to 5 000 000.',38,700))
body+=pin(128,370,1664,svgwrap(860,140,'Digit cards 0, 1, 2, 4, 5, 7 and 8',g),None)
body+=pin(1040,380,752,p('A 4 or a 5 must go first. Test BOTH.',36,800),None,SOFT,20,'22px 28px')
body+=sstep(1,'Just above: 5, then the smallest digits: <b>5 012 478</b>.  5 012 478 − 5 000 000 = 12 478',540,size=34)
body+=sstep(2,'Just below: 4, then the biggest digits: <b>4 875 210</b>.  5 000 000 − 4 875 210 = 124 790',650,size=34)
body+=pin(128,770,1664,p('12 478 is the smaller gap, so 5 012 478 is closest.',40,800),'pop',YEL,20,'18px 28px')
put('p5l1-we1',sec('p5l1-we1','25–28 MIN',body,'Test both sides: today\'s main strategy. Ask first: "Which card goes first?" Some children say only 5. Click step 1, then ask "Are we sure? What about just below?" Click step 2. Think-aloud: "After a 5 I want the number as SMALL as possible, so the next digits go up: 0, 1, 2, 4, 7, 8. After a 4 I want it as BIG as possible, so the digits go down: 8, 7, 5, 2, 1, 0. Then I compare the gaps by subtracting." '
 'Point out that this time the number just above wins, but on the worksheet it may be the other way: always test both.'))
put('p5l1-try2',try_slide('p5l1-try2','28–29 MIN','Your turn: cards 1, 3, 4, 6, 7, 8, 9','Use all seven cards once each.',[('a','The greatest ODD number','9 876 431'),('b','The smallest EVEN number','1 346 798'),('c','The number closest to 2 000 000','1 987 643')],'Whiteboards. a) The ones digit must be odd: keep the 1 for the end, then the rest as big as possible. b) The ones digit must be even: use the smallest even digit that leaves the front small, 8 at the end gives 1 346 798 (ending in 4 gives 1 367 894, ending in 6 gives 1 347 896, both bigger). c) There is no 2 card, so test 1 (just below: 1 987 643, 12 357 away) and 3 (just above: 3 146 789, more than a million away).',size=34))

# ---------- 10. worked example: digit riddle ----------
clues=['Rounded to the nearest hundred thousand, I am 3 600 000.','My ten thousands digit is 4 more than my hundred thousands digit.','My thousands digit is the difference of those two digits.','My hundreds digit is half my thousands digit. My tens digit is 0.','My digits are all different and add up to 31.']
ctext=''.join(f'<p style="font-size:28px;font-weight:600;line-height:1.25"><span style="color:{TEAL};font-weight:800">{i+1}.</span> {E(c)}</p>' for i,c in enumerate(clues))
body=h2('Worked example: a digit riddle')+pin(128,230,1664,ctext,None,WHITE,20,'18px 28px',f'gap:6px')
g=pvchart(10,6,['','','','','','',''],cw=150,ch=96)
body+=pin(128,520,1080,svgwrap(1070,170,'Empty place-value chart from millions to ones',g),None)
for i,(d,build) in enumerate([('3','fade'),('5','fade'),('9','fade'),('4','fade'),('2','fade'),('0','fade'),('8','fade')]):
    body+=pin(128+10+i*150,520+62,150,f'<p style="font-family:{HF};font-size:64px;font-weight:600;text-align:center">{d}</p>',build)
body+=pin(1240,520,552,p('Clue 1: 3 5 with a big digit next, or 3 6 with a small digit next.',30,700),'rise',SOFT,20,'16px 22px')
body+=pin(1240,690,552,p('Clue 2: 5 + 4 = 9 fits. 6 + 4 = 10 is not a digit.',30,700),'rise',SOFT,20,'16px 22px')
body+=pin(128,730,1080,p('9 − 5 = 4,  half of 4 is 2,  0,  31 − 23 = 8.   I am 3 594 208.',32,800),'pop',YEL,20,'16px 24px')
put('p5l1-we2',sec('p5l1-we2','29–32 MIN',body,'Use the clues in order: start with the clue that fixes the most digits. Click order: the digits appear one by one (3, 5, 9, 4, 2, 0, 8), then the two clue notes, then the answer. Talk through the digits as they appear. '
 'Think-aloud: "Rounded to the nearest hundred thousand it is 3 600 000, so it is between 3 550 000 and 3 649 999. Either it starts 3 5 and the next digit is 5 or more, or it starts 3 6 and the next digit is 4 or less. Clue 2: 5 + 4 = 9, and 9 is 5 or more, good. 6 + 4 = 10 is not a digit. So 3 5 9. Thousands: 9 − 5 = 4. Hundreds: half of 4 is 2. Tens: 0. So far 3 + 5 + 9 + 4 + 2 + 0 = 23, and 31 − 23 = 8." '
 'Then CHECK every clue: 3 594 208 rounds to 3 600 000; all digits different; total 31. The workbook riddle uses the same idea with different clues: do not give it away.'))

# ---------- 11. key ----------
body=h2('Key idea: test both sides, check every clue')+card(p('Place value tells you what each digit is worth. To get closest to a target, test the best number just below AND just above.',44,700))+card(p('Riddles: start with the clue that fixes the most digits. Check every clue at the end.',38,600,MUTED))
put('p5l1-key',sec('p5l1-key','32–33 MIN',body,'Say the key idea together. Common mistakes to watch for during the worksheet: (1) Leaving out zeros that hold a place (340 006 for 3 040 006), or mixing up the value of a digit (3000) with how many thousands a number has (4053). (2) Looking only on one side of the target, for example trying only numbers that start with 6 for "closest to 6 000 000". (3) Working from left to right and ignoring the order of operations (6 + 4 × 5 read as 50 instead of 26).'))
put('p5l1-break',break_slide('p5l1-break','33–37 MIN','Human number line: stretch tall for 10 million, crouch small for 1. Now show 5 million, 2 500 000 and 9 900 000 with your arms!','Five minutes. Online: children stand back from the camera. Ask: "Where is 1 million? Why is it so close to the floor?" (it is only one tenth of the way up).'))

# ---------- worksheet page 1 ----------
put('p5l1-ws1',ws_preview('p5l1-ws1','37–49 MIN','Worksheet page 1: with your partner',[('Q1','Place value. Group in threes, watch the zeros.'),('Q2','Seven digit cards: greatest, smallest even, closest to 6 000 000.'),('Q3','A digit riddle. Fill in the chart, then check every clue.')],'Stuck? Lay out the real cards on your place-value mat.','Minutes 37 to 49. Walk around. Ask "Did you test just below AND just above?" before giving any help on Q2c. Q3: ask "Which clue fixes the most digits?" (clue 2, the rounding clue).'))
put('p5l1-ws1ans',checks('p5l1-ws1ans','49–51 MIN','Page 1: check together',[('Q1','a) 5 308 040   b) 400 000; 8   c) 3250'),('Q2','a) 9 865 320   b) 2 035 698   c) 5 986 320 (13 680 away). Just above, 6 023 589, is 23 589 away.'),('Q3','7 253 609')],
 'Click each answer after a pair explains theirs. Q2b: the ones digit must be even; try each even ending with the rest as small as possible: ending 0 gives 2 356 890, ending 2 gives 3 056 892, ending 6 gives 2 035 896, ending 8 gives 2 035 698. The smallest is 2 035 698 Q2c: this time just BELOW wins. Q3: rounding gives 7 2 (then 5 or more) or 7 3 (then 4 or less); 2 + 3 = 5 works, 3 + 3 = 6 does not. Then 5 − 2 = 3, 6, 0, and 32 − 23 = 9.',gapy=180))

# ---------- teach before page 2: estimate ----------
body=h2('Estimate to catch mistakes')+card(p('Mei\'s calculator says  5896 × 41 = 2 417 336.  Could that be right?',40,700))
body+=sstep(1,'Round each number: 5896 is about 6000, and 41 is about 40.',400,size=36)
body+=sstep(2,'6000 × 40 = 240 000. So the answer should be about 240 000.',510,size=36)
body+=pin(128,620,1664,p('2 417 336 is about 10 times too big. It must be wrong! (Mei pressed an extra digit: the real answer is 241 736.)',36,800),'pop',YEL,20,'18px 28px')
body+=pin(128,780,1664,p('Round to an easy number with one non-zero digit, work it out in your head, then compare.',34,700),'fade',SOFT,20,'18px 28px')
put('p5l1-teachest',sec('p5l1-teachest','51–53 MIN',body,'Teach before worksheet page 2 (Q4). Ask first: "Without working it out, is 2 417 336 too big, too small or about right?" Think-aloud: "6 thousand times 4 tens is 24 ten-thousands, 240 000. Mei\'s answer is over 2 million: way too big." Stress that an estimate cannot prove an answer is RIGHT, only that it COULD be right; it can prove an answer is wrong.'))

# ---------- brackets ----------
rows=[('No brackets:','7 + 5 × 4 − 3  =  7 + 20 − 3','24'),('(7 + 5) × 4 − 3','=  12 × 4 − 3','45'),('7 + 5 × (4 − 3)','=  7 + 5 × 1','12')]
body=h2('Brackets change the answer')+p('Brackets first. Then × and ÷ from left to right. Then + and − from left to right.',34,600,MUTED)
for i,(a,b,c) in enumerate(rows):
    body+=pin(128,340+i*140,1250,p(f'<span style="color:{TEAL};font-weight:800">{E(a)}</span>  {E(b)}',38,600,raw=True),None,WHITE,20,'18px 28px')+answer(1420,340+i*140,372,c)
body+=pin(128,780,1664,p('Same numbers, same signs, three different answers!',36,700),'fade',SOFT,20,'18px 30px')
put('p5l1-teachbrackets',sec('p5l1-teachbrackets','53–54 MIN',body,'Teach before worksheet page 2 (Q5). Children work out each line on whiteboards before you click. Think-aloud for row 2: "The brackets say add first: 12. Then 12 × 4 = 48, then 48 − 3 = 45." Ask: "Which answer is biggest? Why does (7 + 5) × 4 grow so much?" (the 7 + 5 is multiplied by 4 instead of only the 5).'))
put('p5l1-trybrackets',try_slide('p5l1-trybrackets','54–55 MIN','Your turn: one pair of brackets','Where do the brackets go? Then a target!',[('a','20 − 8 ÷ 4 + 2 = 5','(20 − 8) ÷ 4 + 2'),('b','20 − 8 ÷ 4 + 2 = 16','20 − (8 ÷ 4 + 2)'),('c','Make 24 with 3, 4, 6, 8 once each','(8 − 6) × 3 × 4')],'Whiteboards. a) 12 ÷ 4 + 2 = 5. b) 8 ÷ 4 + 2 = 4, and 20 − 4 = 16. c) Many ways: (8 − 6) × 3 × 4, 6 × (3 × 4 − 8), (6 ÷ 3) × (4 + 8), 3 × (6 + 8 ÷ 4). Collect several and check each one aloud. Strategy for targets: think of a multiplication that makes the target (24 = 2 × 12 = 3 × 8), then try to build the parts.',size=34))

# ---------- find all with rounding ----------
g=f'<line x1="20" y1="80" x2="1180" y2="80" stroke="{NAVY}" stroke-width="5"/><rect x="250" y="56" width="700" height="48" fill="{SKY}" stroke="{NAVY}" stroke-width="3" stroke-dasharray="10 6"/>'
for x,lab in [(60,'4900'),(250,'4950'),(600,'5000'),(950,'5050'),(1140,'5100')]:
    g+=f'<line x1="{x}" y1="50" x2="{x}" y2="110" stroke="{NAVY}" stroke-width="5"/>'+txt(x,155,lab,32,TEAL if lab=='5000' else NAVY)
body=h2('Find ALL: write the range first')+card(p('A number rounded to the nearest hundred is 5000. Its digits add up to 6. Find all the numbers.',38,700))
body+=pin(128,380,1664,svgwrap(1200,170,'Number line from 4900 to 5100 with the numbers from 4950 to 5049 shaded',g),None)
body+=sstep(1,'Range: from 4950 up to 5049.',570,size=34)
body+=sstep(2,'4950 to 4999: 4 + 9 + 5 = 18 already. Too big: none!',670,size=34)
body+=sstep(3,'5000 to 5049: 5 + 0, so the last two digits add to 1:  5001 and 5010.',770,size=34)
put('p5l1-teachfind',sec('p5l1-teachfind','55–57 MIN',body,'Teach before worksheet page 2 (Q6, the same idea with a 7-digit number: do not give it away). Ask: "What is the smallest number that rounds to 5000 (nearest hundred)? The biggest?" (4950 and 5049; 5050 rounds up to 5100). Think-aloud for step 2: "Numbers just below 5000 have lots of 9s, so their digits add up to a lot." Step 3: make a list in order so nothing is missed: 5001, 5010. Check: is 5100 allowed? No, it is out of the range.'))

# ---------- worksheet page 2 ----------
put('p5l1-ws2',ws_preview('p5l1-ws2','57–72 MIN','Worksheet page 2: on your own',[('Q4','Estimate Ravi\'s calculator answers. Which must be wrong?'),('Q5','One pair of brackets, then a target of 100.'),('Q6','Write the range first, then find ALL the numbers.')],'Finished early? Stretch and Challenge come next.','Children work alone. Note who needs a short catch-up next lesson, especially children who still work from left to right in Q5.'))
put('p5l1-ws2ans',checks('p5l1-ws2ans','72–76 MIN','Page 2: check together',[('Q4','a) about 100 000: could be right   b) about 60 000: must be wrong   c) about 6 300 000: must be wrong   d) about 320 000: could be right'),('Q5','a) (6 + 4) × 5 − 2   b) 6 + 4 × (5 − 2)   c) 1 000 000 ÷ (200 + 300) × 2   d) 5 × (3 × 9 − 7) = 100'),('Q6','a) 2 499 500 and 2 500 499   b) 2 500 002, 2 500 011, 2 500 020, 2 500 101, 2 500 110, 2 500 200')],
 'Click after a child explains. Q4b: 3 000 000 ÷ 50 = 60 000, so 6259 is 10 times too small (real answer 62 594). Q4c: 2 300 000 + 4 000 000 = 6 300 000 (real answer 6 333 332). Q5c: 1 000 000 ÷ 500 = 2000, × 2 = 4000. Q5d: 3 × 9 = 27, 27 − 7 = 20, 5 × 20 = 100; it is the only way. Q6: 2 499 5__ starts 2 + 4 + 9 + 9 + 5 = 29, far too big. From 2 500 000, the last three digits add to 2 (hundreds digit at most 4): list in order, 6 numbers.',gapy=190,size=32))

# ---------- stretch / challenge ----------
st=[('1.','Which is the best estimate of 4108 × 29: 12 000, 120 000 or 1 200 000? Explain.'),('2.','Use 2, 3, 5 and 7 once each, with +, −, ×, ÷ and brackets, to make 29, then 31, then 100.'),('3.','Use four 4s with +, −, ×, ÷ and brackets to make 3, then 5, then 7.')]
put('p5l1-stretch',sec('p5l1-stretch','For early finishers',h2('Stretch')+numcards(st,36),'Answers: 1) 120 000, because 4000 × 30 = 120 000 (exactly 119 132). 2) 29 = 5 × 7 − 2 × 3;  31 = 2 × 5 + 3 × 7;  100 = 2 × 5 × (3 + 7); other ways are possible. 3) (4 + 4 + 4) ÷ 4 = 3;  (4 × 4 + 4) ÷ 4 = 5;  4 + 4 − 4 ÷ 4 = 7. Other ways are possible: check each with the order of operations.'))
ch=[('1.','Put brackets into  1 + 2 × 3 + 4 × 5 + 6  to make the answer as big as possible. You may use more than one pair. What is the biggest answer?'),('2.','I am a 7-digit odd number. My digits are all different and add up to 42. Rounded to the nearest hundred thousand, I am 7 000 000. I am the smallest number that fits. Who am I?')]
put('p5l1-challenge',sec('p5l1-challenge','For early finishers',h2('Challenge')+numcards(ch,36),'Pairs try first, then use the "see it" slide if stuck, then the walk-through. These are Think Harder Q5 and Q6. Answers: 1) 231: (1 + 2) × (3 + 4) × (5 + 6) = 3 × 7 × 11. With no brackets it is only 33. 2) 6 953 487. The seven digits must be 3, 4, 5, 6, 7, 8 and 9, because the biggest seven different digits add to exactly 42. The number is between 6 950 000 and 7 049 999; 7 0… needs a 0, so it starts 6 9 then 5, 7 or 8. The smallest: 6 95, then 3, 4, 8, 7 so that it ends in an odd digit.'))
g1=''
toks=['1','+','2','×','3','+','4','×','5','+','6']
for i,t in enumerate(toks):
    x=20+i*66
    if t.isdigit(): g1+=f'<rect x="{x}" y="70" width="60" height="80" rx="12" fill="{YEL}" stroke="{NAVY}" stroke-width="4"/>'+txt(x+30,128,t,44)
    else: g1+=txt(x+30,128,t,44,TEAL)
g1+=txt(380,40,'( ? )   ( ? )   ( ? )',34,MUTED,weight=600,font='Nunito Sans, Arial')
g1+=f'<rect x="20" y="200" width="720" height="90" rx="14" fill="{WHITE}" stroke="{NAVY}" stroke-width="3"/>'+txt(380,258,'No brackets: 1 + 6 + 20 + 6 = 33',32)
g1+=f'<rect x="20" y="320" width="720" height="90" rx="14" fill="{SOFT}" stroke="{NAVY}" stroke-width="3"/>'+txt(380,378,'Does × or + make numbers grow faster?',30)
g2=f'<line x1="30" y1="80" x2="730" y2="80" stroke="{NAVY}" stroke-width="5"/><rect x="130" y="58" width="500" height="44" fill="{SKY}" stroke="{NAVY}" stroke-width="3" stroke-dasharray="10 6"/>'
for x,lab in [(130,'6 950 000'),(380,'7 000 000'),(630,'7 049 999')]:
    g2+=f'<line x1="{x}" y1="50" x2="{x}" y2="110" stroke="{NAVY}" stroke-width="5"/>'+txt(x,148,lab,28,TEAL if x==380 else NAVY)
for i in range(7):
    g2+=f'<rect x="{40+i*100}" y="190" width="84" height="90" rx="12" fill="{WHITE}" stroke="{NAVY}" stroke-width="4" stroke-dasharray="10 6"/>'
g2+=txt(380,340,'7 different digits that add up to 42?',30)+txt(380,390,'Biggest seven: 9 + 8 + 7 + 6 + 5 + 4 + 3 = ?',28,MUTED,weight=600)
body=h2('Challenge: see it',60)+'<div style="display:flex;gap:32px;align-items:flex-start">'
body+=card(f'<p style="font-size:30px;font-weight:700;color:{TEAL}">Q1: Where do the brackets go?</p>'+svgwrap(760,420,'The expression 1 + 2 × 3 + 4 × 5 + 6 with empty bracket slots; without brackets it is 33',g1).replace('width:760px;height:420px;flex:none','width:100%;height:auto;display:block'),extra='flex:1;min-width:0;padding:20px 24px')
body+=card(f'<p style="font-size:30px;font-weight:700;color:{TEAL}">Q2: The range and the digits</p>'+svgwrap(760,420,'A number line from 6 950 000 to 7 049 999, seven empty digit boxes and a question about digits that add to 42',g2).replace('width:760px;height:420px;flex:none','width:100%;height:auto;display:block'),extra='flex:1;min-width:0;padding:20px 24px')+'</div>'
put('p5l1-chdiag',sec('p5l1-chdiag','For early finishers',body,'Show after pairs have tried the Challenge, or if they are stuck. The pictures show the problem, not the answer. Ask: Q1: "Which makes a number grow faster, adding or multiplying? So which signs should go inside the brackets?" Q2: "Which numbers round to 7 000 000? Can the number start 7 0 if it has no 0? What do the biggest seven digits add up to?" Answers are in the Challenge slide notes.'))
body=h2('Challenge: walk-through')+pin(128,250,800,p('Q1: add inside, multiply outside',38,800,TEAL))
for i,t in enumerate(['Multiplying grows faster than adding.','So put each + inside brackets:','(1 + 2) × (3 + 4) × (5 + 6)','= 3 × 7 × 11 = 231 (not 33!)']): body+=pin(128,330+i*110,800,p(t,32),'rise',WHITE)
body+=pin(992,250,800,p('Q2: the digits, then the range',38,800,TEAL))
for i,t in enumerate(['Sum 42: the digits are 3 to 9, no 0.','Range 6 950 000 to 7 049 999.','No 0, so it starts 6 9, then 5, 7 or 8.','Smallest, ending odd: 6 953 487']): body+=pin(992,330+i*110,800,p(t,32),'rise',WHITE)
put('p5l1-chwalk',sec('p5l1-chwalk','Challenge',body,'Use after pairs have tried. Q1: test a few placements first: 1 + 2 × (3 + 4) × 5 + 6 = 77; (1 + 2) × 3 + 4 × (5 + 6) = 53; then all three additions in brackets give 231, the biggest. Q2: 9 + 8 + 7 + 6 + 5 + 4 + 3 = 42 exactly, so there is no room for 0, 1 or 2. After 6 95, the digits 3, 4, 7, 8 are left; 6 953 478 is even, so the smallest odd one is 6 953 487. Check every clue.'))

# ---------- talk / exit ----------
body=h2('Talk time')+card(chip('TALK TIME',YEL,NAVY)+p('Siti says a 7-digit number is always bigger than a 6-digit number. Ravi says not if the 6-digit number has bigger digits, like 999 999. Who is right? Why?',40,600))+card(p('Sentence starters:',34,400,MUTED)+p('“I noticed that …”   “I tested it by …”   “I know because …”',38,600))
put('p5l1-talk',sec('p5l1-talk','76–82 MIN',body,'Minutes 76 to 82. Pairs talk for 2 minutes, then share. Answer: Siti is right. The smallest 7-digit number is 1 000 000 and the biggest 6-digit number is 999 999, which is 1 less. The millions digit of a 7-digit number is at least 1, and that alone beats every 6-digit number. Second question if time: "How did you check that you had found ALL the numbers in Q6?" (we wrote the range first, then listed in order). Praise the reasons, not only the answers.'))
body=h2('Exit ticket')+card(chip('EXIT TICKET')+p('(a) What is the value of the digit 4 in 8 406 125?',44,600)+p('(b) Add one pair of brackets to make it true:   5 + 3 × 8 − 2 = 62',44,600))+card(p('Write your answer on a slip of paper. Show it to your tutor. Then collect your stamp in your inquiry journal.',34,400))
put('p5l1-exit',sec('p5l1-exit','82–90 MIN',body,'Minutes 82 to 90. Answers: (a) 400 000. (b) (5 + 3) × 8 − 2 = 62. (Without brackets it is 27; 5 + 3 × (8 − 2) = 23.) Extension: use the digit cards 0 to 9, each at most once, to make the 7-digit number closest to 5 000 000 (5 012 346 is 12 346 away; 4 987 653 is 12 347 away, so 5 012 346 wins by 1).'))

# ---------- write ----------
order=['p5l1-title','p5l1-warm1','p5l1-warm2','p5l1-explore1','p5l1-explore2','p5l1-teach1','p5l1-try1','p5l1-we1','p5l1-try2','p5l1-we2','p5l1-key','p5l1-break','p5l1-ws1','p5l1-ws1ans','p5l1-teachest','p5l1-teachbrackets','p5l1-trybrackets','p5l1-teachfind','p5l1-ws2','p5l1-ws2ans','p5l1-stretch','p5l1-challenge','p5l1-chdiag','p5l1-chwalk','p5l1-talk','p5l1-exit']
assert set(order)==set(S), set(order)^set(S)
sd=os.path.join(D,'slides')
for f in os.listdir(sd):
    if f.endswith('.html') and f[:-5] not in S: os.remove(os.path.join(sd,f))
for i,h in S.items(): open(os.path.join(sd,i+'.html'),'w').write(h)
deck={'v':4,'createdOnFiles':{'v':1,'at':datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')},'lists':'css',
 'title':'Math Inquirers P5: Lesson 1 – Million Puzzles','order':order,'cover':'p5l1-title',
 'sections':{'s1':{'description':'Warm-up and explore','start':'p5l1-title'},'s2':{'description':'Teach: place value, closest to a target, digit riddles','start':'p5l1-teach1'},'s3':{'description':'Worksheet with teaching before each page','start':'p5l1-break'},'s4':{'description':'Stretch, challenge, talk and exit','start':'p5l1-stretch'}},
 'faces':{'fredoka':{'family':'Fredoka','href':'https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&display=swap'},'nunito-sans':{'family':'Nunito Sans','href':'https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@400;600;700&display=swap'}},
 'designSystems':[]}
json.dump(deck,open(os.path.join(D,'deck.json'),'w'),indent=1,ensure_ascii=False)
print(len(order),'slides')
