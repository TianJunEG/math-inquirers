"""Math Inquirers P2, Lesson 2: Missing Digit Mysteries. Writes split/p2l2/project (deck.json + slides/*.html)."""
import json,os,sys,datetime
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,H)
import slidekit
from slidekit import *
slidekit.FOOT='Math Inquirers P2 Holiday Program  •  Notice it. Test it. Explain why.'
D=os.path.join(H,'..','split','p2l2','project'); os.makedirs(os.path.join(D,'slides'),exist_ok=True)
S={}
def put(i,h): S[i]=h
FOOTX=slidekit.FOOT

# ---------- shared slide shapes (same look as the P1 decks) ----------
def title_slide(sid,label,title,topic,today,notes):
    return (f'<section id="{sid}" data-transition="fade" style="background:{NAVY};color:{CREAM};font-family:{BF};padding:128px 128px 160px;display:flex;flex-direction:column;justify-content:center;gap:36px">\n'
            f'<p style="font-size:32px;font-weight:700;letter-spacing:4px;color:{YEL}">{E(label)}</p>\n'
            f'<h1 style="font-family:{HF};font-size:112px;font-weight:600;line-height:1.05">{E(title)}</h1>\n'
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
def svgwrap(w,h,label,inner,fluid=False):
    st='width:100%;height:auto;display:block' if fluid else f'width:{w}px;height:{h}px;flex:none'
    return f'<svg aria-label="{E(label)}" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="{st}">{inner}</svg>'
def txt(x,y,s,size=40,fill=NAVY,anchor='middle',weight=700,font='Fredoka, Arial'):
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" fill="{fill}" font-family="{font}">{E(str(s))}</text>'

# column sum: '?' = box. returns svg inner, width = 60 + 4*c
def colsum(top,bot,res,op,x0=0,y0=0,c=86,size=60,shade=False):
    g=''; ys=[y0+80,y0+180,y0+310]
    if shade:
        for k in range(1,4): g+=f'<rect x="{x0+50+k*c-c/2+6}" y="{y0+10}" width="{c-12}" height="{330}" rx="14" fill="{SKY}"/>'
    for r,y in zip([top,bot,res],ys):
        for i,d in enumerate(r):
            cx=x0+50+(4-len(r)+i)*c
            if d=='?': g+=f'<rect x="{cx-32}" y="{y-62}" width="64" height="76" rx="10" fill="{SOFT}" stroke="{NAVY}" stroke-width="4"/>'
            else: g+=txt(cx,y,d,size)
    g+=txt(x0+50,ys[1],op,size)+f'<line x1="{x0+20}" y1="{y0+215}" x2="{x0+50+3*c+c/2}" y2="{y0+215}" stroke="{NAVY}" stroke-width="5"/>'
    return g

# ---------- 1. title ----------
put('p2l2-title',title_slide('p2l2-title','LESSON 2  •  WEEK 1','Missing Digit Mysteries','Addition and subtraction within 1000',
 'Find missing digits in 3-digit sums, make both sides of "=" balance, and solve magic squares and triangles with bigger numbers.',
 'Objective: Find missing digits in 3-digit addition and subtraction by starting at the ones and checking for a carry, use "=" as "is the same as" to balance number sentences, and complete magic squares and triangles with bigger numbers. '
 'Thinking strategies taught today: WORK BACKWARDS (turn a subtraction into an addition) and GUESS AND CHECK (try a digit, test it, improve). Also: draw a model for two numbers with a known total and difference. '
 'Materials: Digit cards 0 to 9, base-ten blocks or place-value counters, mini whiteboards, a paper magic triangle with 6 circles and number tiles 110 to 160. '
 'Online: children write column sums on whiteboards and hold them up; number tiles are cut from paper before the lesson; the tutor writes on the slide sums. '
 'Time plan: warm-up 0 to 10, explore 10 to 25, teaching 25 to 35 (click to reveal each step and answer), brain break 35 to 40, worksheet 40 to 70 with short teaching before each page and a check-together slide after it, challenge for early finishers from 65, talk time 70 to 80, exit ticket 80 to 90.'))

# ---------- 2. warm-up game ----------
items=[('Partner to 100:','65','35'),('Partner to 100:','20','80'),('Partner to 100:','45','55'),('Partner to 1000:','370','630'),('Partner to 1000:','850','150'),('Partner to 1000:','125','875')]
body=h2('Warm-up: Partners')+p('I say a number. You say its partner. Shout it out together!',36,600,MUTED)
for i,(a,b,c) in enumerate(items):
    col=i//3; row=i%3; L=128 if col==0 else 990; T=330+row*150
    body+=qrow(L,T,500,a,b,40)+answer(L+572,T,178 if col else 200,c)
put('p2l2-warm1',sec('p2l2-warm1','0–5 MIN',body,
 'Minutes 0 to 5. Partners. Say a number; children call out the partner (online: unmute together or type in the chat). Click to reveal each answer, left column first. Then make up more: 30, 85, 99 for 100; 600, 240, 505 for 1000. '
 'Ask after 125: "How did you find 875 so fast?" Listen for: "1 and 8 make 9 hundreds, 2 and 7 make 9 tens, 5 and 5 make 10 ones." That is the key to today\'s explore. '
 'Watch for: children who say 985 for 125 (making every column 10). The columns are 9, 9 and 10 because of the carries.'))

# ---------- 3. quick questions ----------
qs=[('1.','65 + __ = 100','35'),('2.','300 + 450 = ?','750'),('3.','700 − 250 = ?','450'),('4.','238 + 10 = ?','248'),('5.','500 − __ = 120','380')]
body=h2('Quick questions')+''.join(qrow(128,250+i*125,1250,a,b) for i,(a,b,c) in enumerate(qs))+''.join(answer(1420,250+i*125,372,c) for i,(a,b,c) in enumerate(qs))
put('p2l2-warm2',sec('p2l2-warm2','5–10 MIN',body,'Minutes 5 to 10. Whiteboards up together, then click. For 3 ask: "How did you take 250 from 700?" (700 − 200 = 500, then − 50 = 450). For 5: "Which is easier: count on from 120 to 500, or take away?" (count on: 120 → 200 is 80, 200 → 500 is 300, so 380). Answers: 35, 750, 450, 248, 380.'))

# ---------- 4. explore ----------
g=colsum('358','641','999','+',x0=10,y0=50,c=96,size=60,shade=True)
for k in range(1,4): g+=txt(10+50+k*96,44,'9?',34,TEAL)
steps=''.join(f'<li>{E(s)}</li>' for s in ['Pick any 3-digit number, like 358.','Find its partner that makes 999. Check by adding.','Do it for three more numbers.','Look at each column. What do you notice?'])
body=h2('Explore: what to do')+'<div style="display:flex;gap:32px;align-items:flex-start">'+card(chip('EXPLORE')+f'<ol style="font-size:38px;font-weight:600;padding-left:56px;display:flex;flex-direction:column;gap:14px">{steps}</ol>',extra='flex:1;min-width:0')
body+=card(svgwrap(440,410,'Column sum 358 + 641 = 999 with each column shaded',g),extra='flex:none;padding:20px 32px')+'</div>'
put('p2l2-explore1',sec('p2l2-explore1','10–15 MIN',body,'Minutes 10 to 15. Pairs choose their own 3-digit numbers and find partners to 999, checking with a column sum. Do not explain the pattern; let them find it. Early finishers: "Now find partners to 1000. What changes?" (the ones add up to 10 and the tens and hundreds to 9, because of the carry).'))
body=h2('Explore: talk about it')+numcards([('1.','What did you notice about each column?'),('2.','Why is there never a carry when you make 999?'),('3.','Find the partner of 274 without adding.')],40)
put('p2l2-explore2',sec('p2l2-explore2','15–25 MIN',body,'Minutes 15 to 25. Gather the group. Answers: 1) The two digits in each column add up to 9. 2) No column adds up to more than 9, so nothing is carried. 3) 725 (2 + 7, 7 + 2 and 4 + 5 all make 9). Push: "So if I know the answer and one number, can I find a missing digit?" That is today\'s mystery.'))

# ---------- 6. teach: missing digits, addition ----------
g=colsum('4?7','28?','723','+',x0=10,y0=0)
body=h2('Missing digits: start at the ones')+pin(128,240,520,svgwrap(420,340,'Column sum 4 box 7 plus 28 box equals 723',g),None,WHITE,24,'20px 40px')
body+=step(1,'Ones: 7 + □ ends in 3. 7 + 6 = 13, so □ = 6. Carry 1 ten.',left=740,top=240,width=1052,size=34)
body+=step(2,'Tens: □ + 8 + 1 ends in 2. 3 + 8 + 1 = 12, so □ = 3. Carry 1 hundred.',left=740,top=370,width=1052,size=34)
body+=step(3,'Hundreds: 4 + 2 + 1 = 7. It matches ✓',left=740,top=500,width=1052,size=34)
body+=answer(128,660,1664,'437 + 286 = 723.   Check by adding the whole numbers.')
body+=pin(128,780,1664,p('Ask every time: was there a carry into this column?',36,700),'fade',SOFT,20,'18px 30px')
put('p2l2-teach1',sec('p2l2-teach1','25–28 MIN',body,'Teach. Ask first: "Which column should we start with?" Some children start at the hundreds: 4 + 2 = 6, not 7, and they get stuck. Show why the ones go first: a carry from the ones changes the tens, and a carry from the tens changes the hundreds. Think-aloud: "7 plus something ends in 3. 7 + 6 = 13. The box is 6, and I carry 1 ten. Tens: something + 8 + 1 ends in 2 …" Guess and check works too: "Try 2 in the tens box: 2 + 8 + 1 = 11. Ends in 1, not 2. Try 3."'))
put('p2l2-try1',try_slide('p2l2-try1','28–30 MIN','Your turn: whiteboards','Find the missing digits. Start at the ones.',[('a','3□2 + 145 = 487','4'),('b','15□ + 2□7 = 412','5 and 5'),('c','□64 + 17□ = 542','3 and 8')],'Write each as a column sum on the whiteboard first. a) No carries: 4 + 4 = 8. b) Ones: □ + 7 ends in 2, so 5 (12, carry 1). Tens: 5 + □ + 1 ends in 1, so 5 (11, carry 1). Hundreds 1 + 2 + 1 = 4 ✓: 155 + 257. c) Ones: 4 + 8 = 12. Tens: 6 + 7 + 1 = 14. Hundreds: □ + 1 + 1 = 5, so 3: 364 + 178.'))

# ---------- 8. worked example: subtraction ----------
g=colsum('6?2','24?','385','−',x0=10,y0=0)
g2=colsum('385','24?','6?2','+',x0=10,y0=0)
body=h2('Subtraction: work backwards')+pin(128,240,440,svgwrap(420,340,'Column subtraction 6 box 2 minus 24 box equals 385',g).replace('width:420px;height:340px','width:360px;height:291px'),None,WHITE,24,'16px 30px')
body+=pin(650,240,440,svgwrap(420,340,'The same sum turned into an addition',g2).replace('width:420px;height:340px','width:360px;height:291px'),'fade',SOFT,24,'16px 30px')
body+=step(1,'Turn it round: 385 + 24□ = 6□2',left=1180,top=240,width=612,size=34)
body+=step(2,'Ones: 5 + □ ends in 2. 5 + 7 = 12, so □ = 7.',left=1180,top=370,width=612,size=34)
body+=step(3,'Tens: 8 + 4 + 1 = 13, so □ = 3. Hundreds: 3 + 2 + 1 = 6 ✓',left=1180,top=520,width=612,size=34)
body+=answer(128,700,1664,'632 − 247 = 385')
put('p2l2-we2',sec('p2l2-we2','30–32 MIN',body,'Work backwards: the answer plus the number we took away gives back the number we started with. Click 1 shows the turned-round sum, then each step. Think-aloud: "Subtraction with gaps is hard, so I undo it. 385 + 247 must make 632." Check the other way at the end: 632 − 247. Ones: 2 − 7 cannot be done, so take a ten: 12 − 7 = 5 ✓.'))
put('p2l2-try2',try_slide('p2l2-try2','32–33 MIN','Your turn: subtraction','Turn it into an addition first.',[('a','8□5 − 321 = 514','3'),('b','74□ − 2□8 = 465','3 and 7'),('c','9□4 − □37 = 517','5 and 4')],'Whiteboards. a) 514 + 321 = 835. b) 465 + 2□8: ones 5 + 8 = 13, so 3; tens 6 + □ + 1 ends in 4, so 7; hundreds 4 + 2 + 1 = 7 ✓: 743 − 278. c) 517 + □37: ones 7 + 7 = 14; tens 1 + 3 + 1 = 5; hundreds 5 + □ = 9, so 4: 954 − 437.'))

# ---------- 10. balance ----------
body=h2('"=" means "is the same as"')+card(p('245 + 130 = 200 + □',48,700))
body+=pin(128,400,1100,seesaw_svg('245 + 130','200 + ?'),None)
body+=step(1,'245 is 45 MORE than 200.',left=1260,top=400,width=532,size=34)
body+=step(2,'So □ must be 45 more than 130.',left=1260,top=530,width=532,size=34)
body+=step(3,'□ = 175. Check: both sides are 375 ✓',left=1260,top=690,width=532,size=34)
body+=pin(128,700,1060,p('You can also work out one side: 245 + 130 = 375, then 375 − 200 = 175.',32,700),'fade',SOFT,20,'18px 28px')
put('p2l2-teach3',sec('p2l2-teach3','33–34 MIN',body,'Teach. Ask first: "What goes in the box?" Some children say 375 because "the answer comes next". The see-saw must balance: both sides the same. Click through. Two ways: compare (look for the difference between 245 and 200), or work out the full side and subtract. Comparing is faster with big numbers, and it is how Ravi\'s question on the worksheet works.'))
put('p2l2-try3',try_slide('p2l2-try3','34–35 MIN','Your turn: balance it','Both sides must be the same.',[('a','320 + 150 = 400 + □','70'),('b','560 − 100 = □ − 200','660'),('c','True or false: 199 + 302 = 200 + 301','True: 501')],'Whiteboards. a) 320 is 80 less than 400, so □ is 80 less than 150: 70. b) Left side is 460, so □ − 200 = 460: □ = 660. c) 199 is 1 less than 200 and 302 is 1 more than 301. Both sides are 501.'))
body=h2('Key idea: start at the ones')+card(p('Start at the ones column and ask: was there a carry? Check by adding the whole numbers.',44,700))+card(p('Turn a subtraction into an addition to work backwards. "=" means both sides are the same.',38,600,MUTED))
put('p2l2-key',sec('p2l2-key','35 MIN',body,'Say the key ideas together. Common mistakes to watch for during the worksheet: (1) Forgetting the carried 1: in Q1c writing 6 in the tens box (8 + 6 = 14) instead of 5 (8 + 5 + 1 = 14). (2) Reading "=" as "the answer comes next": 350 + 140 = 300 + □ answered 490. (3) Magic triangle: putting the biggest numbers in the corners when the side total is small.'))
put('p2l2-break',break_slide('p2l2-break','35–40 MIN','Balance bodies. Stand like a see-saw with arms out. The tutor says a number sentence: stay level if it is true, tip to one side if it is false.','Five minutes. Sentences to call: 300 + 200 = 400 + 100 (true); 250 + 250 = 600 (false); 999 = 1000 − 1 (true); 450 + 50 = 400 + 150 (false). Online: children lean in front of the camera.'))

# ---------- worksheet page 1 ----------
put('p2l2-ws1',ws_preview('p2l2-ws1','40–52 MIN','Worksheet page 1: with your partner',[('Q1','Missing digits in additions. Start at the ones, check the carry.'),('Q2','Missing digits in subtractions. Turn them into additions.'),('Q3','Balance it. Compare the numbers before you work anything out.')],'Stuck? Try a digit in the box, add, and see if it fits.','Minutes 40 to 52. Walk around. Ask "Was there a carry into this column?" before giving any help. Q3d: push for an explanation without working out both sides.'))
put('p2l2-ws1ans',checks('p2l2-ws1ans','52–54 MIN','Page 1: check together',[('Q1','a) 224 + 355 = 579   b) 462 + 375 = 837   c) 386 + 259 = 645'),('Q2','a) 778 − 325 = 453   b) 543 − 267 = 276'),('Q3','a) 190   b) 525   c) 280   d) Yes: 398 is 2 less than 400, 205 is 2 more than 203')],
 'Click each answer after a pair explains theirs. Q1b: ones 2 + 5 = 7 (no carry), tens 6 + 7 = 13, hundreds 4 + 3 + 1 = 8. Q1c: ones 6 + 9 = 15, tens 8 + 5 + 1 = 14, hundreds 3 + 2 + 1 = 6. Q2b: 276 + 267 = 543. Q3d: both sides are 603; moving 2 from one number to the other does not change the total.',gapy=170))

# ---------- teach: magic square ----------
sq=[[220,270,260],[290,250,210],[240,230,280]]; given={(0,0),(0,1),(0,2),(1,1),(2,0)}
def square(show_all):
    g=''
    for r in range(3):
        for c in range(3):
            x=10+c*150; y=10+r*150; gv=(r,c) in given
            g+=f'<rect x="{x}" y="{y}" width="150" height="150" fill="{SKY if gv else WHITE}" stroke="{NAVY}" stroke-width="5"/>'
            if gv or show_all: g+=txt(x+75,y+95,sq[r][c],52,NAVY if gv else TEAL)
    return svgwrap(470,470,'Magic square' if show_all else 'Magic square with five numbers given',g)
body=h2('Magic squares: find the total first')+pin(128,240,470,square(False),None)+pin(128,240,470,square(True),'fade')
body+=step(1,'Find a line with all three numbers: 220 + 270 + 260 = 750. That is the magic total.',left=700,top=240,width=1092,size=34)
body+=step(2,'Left column: 220 + □ + 240 = 750. 220 + 240 = 460, so □ = 750 − 460 = 290.',left=700,top=370,width=1092,size=34)
body+=step(3,'Diagonal: 220 + 250 + □ = 750, so □ = 280. Keep going: total minus the two you know.',left=700,top=500,width=1092,size=34)
body+=pin(700,640,1092,p('Check every row, column and diagonal at the end.',34,700),'fade',SOFT,20,'18px 28px')
put('p2l2-teachsq',sec('p2l2-teachsq','54–56 MIN',body,'Teach before worksheet page 2 (Q4). Click order: step 1, step 2, step 3, the check line, then the full square appears. Ask the group for the last two (210 and 230) before the square is shown. The worksheet square uses different numbers and asks what happens if we add 100 to every number: do not tell them.'))

# ---------- teach: magic triangle ----------
body=h2('Magic triangles: think about the corners')+card(p('Put 11, 12, 13, 14, 15 and 16 in the circles so each side adds up to 42.',38,700))
body+=pin(128,380,480,triangle_svg([None]*6,480,416),None)
body+=step(1,'Each corner is on TWO sides. A big total needs big corners: try 14, 15, 16.',left=680,top=380,width=1112,size=34)
body+=pin(128,380,480,triangle_svg([14,15,16,None,None,None],480,416),'fade')
body+=step(2,'14 + □ + 15 = 42, so □ = 13.   15 + □ + 16 = 42, so □ = 11.',left=680,top=510,width=1112,size=34)
body+=step(3,'16 + □ + 14 = 42, so □ = 12. Every number used once ✓',left=680,top=640,width=1112,size=34)
body+=pin(128,380,480,triangle_svg([14,15,16,13,11,12],480,416),'fade')
put('p2l2-teachtri',sec('p2l2-teachtri','56–58 MIN',body,'Teach before worksheet page 2 (Q5). Here the total is BIG, so the big numbers go in the corners. On the worksheet the first total (390) is the SMALLEST possible: ask "Small total… so which numbers go in the corners?" but do not tell them. Click order: step 1, corners appear, step 2, step 3, the finished triangle. Check each side aloud: 14 + 13 + 15, 15 + 11 + 16, 16 + 12 + 14.'))

# ---------- teach: two numbers (model) ----------
g=(f'<rect x="200" y="20" width="400" height="80" rx="10" fill="{SKY}" stroke="{NAVY}" stroke-width="4"/>'+txt(80,74,'small',34,NAVY,'start',800,'Nunito Sans, Arial')+txt(400,74,'?',44)
   +f'<rect x="200" y="130" width="400" height="80" rx="10" fill="{SKY}" stroke="{NAVY}" stroke-width="4"/><rect x="600" y="130" width="200" height="80" rx="10" fill="{YEL}" stroke="{NAVY}" stroke-width="4"/>'
   +txt(80,184,'big',34,NAVY,'start',800,'Nunito Sans, Arial')+txt(400,184,'?',44)+txt(700,184,'100',40)
   +f'<path d="M830 20 Q860 20 860 60 L860 100 Q860 115 880 115 Q860 115 860 130 L860 170 Q860 210 830 210" fill="none" stroke="{TEAL}" stroke-width="5"/>'+txt(900,128,'500 altogether',38,TEAL,'start'))
body=h2('Two numbers: total and difference')+card(p('Two numbers add up to 500. One is 100 more than the other. What are they?',38,700))
body+=pin(128,380,1664,svgwrap(1240,230,'Bar model: a small bar, and a big bar that is the same plus 100, making 500 altogether',g),None)
body+=step(1,'Take away the extra 100: 500 − 100 = 400.',top=630,size=34)
body+=step(2,'Two equal bars make 400, so each is 200.',top=730,size=34)
body+=step(3,'Give back the 100: 200 and 300. Check: 200 + 300 = 500 ✓',top=830,size=34)
put('p2l2-teachtwo',sec('p2l2-teachtwo','58–60 MIN',body,'Teach before worksheet page 2 (Q6). Draw a model: the big bar is the small bar plus the extra. Take the extra away, share what is left into two equal bars, then give the extra back. Children who guess and check (250 and 250? 150 and 350?) are welcome: ask them to check BOTH clues. Halving 400: half of 4 hundreds is 2 hundreds.'))

# ---------- worksheet page 2 ----------
put('p2l2-ws2',ws_preview('p2l2-ws2','60–67 MIN','Worksheet page 2: on your own',[('Q4','Magic square. Find the total from a full line first.'),('Q5','Magic triangles. Which numbers should go in the corners?'),('Q6','Two mystery numbers. Draw a model: take away the extra, halve, give it back.')],'Finished early? Stretch and Challenge come next.','Children work alone. Note who needs a short catch-up next lesson, especially anyone still starting column sums at the hundreds.'))
put('p2l2-ws2ans',checks('p2l2-ws2ans','67–69 MIN','Page 2: check together',[('Q4','a) 150   b) top 10; middle 30, 70; bottom 90   c) Yes, still magic: total 450 (150 + 3 hundreds)'),('Q5','a) corners 110, 120, 130; between them 160, 140, 150   b) corners 140, 150, 160; between them 130, 110, 120'),('Q6','250 and 450:  700 − 200 = 500,  half is 250,  250 + 200 = 450')],
 'Click after a child explains. Q4c: every line has three numbers and each went up by 100, so every line total went up by 300. Q5a: 390 is the smallest total possible, so the smallest numbers are corners: 110 + 160 + 120, 120 + 140 + 130, 130 + 150 + 110. Q5b: 420 is the biggest: 140 + 130 + 150, 150 + 110 + 160, 160 + 120 + 140. Q6 check: 250 + 450 = 700 and 450 − 250 = 200.',gapy=170))

# ---------- stretch / challenge ----------
st=[('1.','Find the missing digits:  6□5 + □7□ = 900'),('2.','The same number goes in both boxes:  □ + □ + 250 = 750. What is it?'),('3.','Adding 99 is the same as adding 100, then taking away 1. Use it:  456 + 99 = ?')]
put('p2l2-stretch',sec('p2l2-stretch','For early finishers',h2('Stretch')+numcards(st),'Answers: 1) 625 + 275 = 900 (ones 5 + 5 = 10; tens 2 + 7 + 1 = 10; hundreds 6 + 2 + 1 = 9). 2) 250 (750 − 250 = 500, and 250 + 250 = 500). 3) 555 (456 + 100 = 556, then 556 − 1 = 555).'))
ch=[('1.','Find ALL the ways to fill the boxes:  □□7 + 4□□ = 1000'),('2.','Box A and Box B hold 250 marbles together. Box B and Box C hold 350. Box A and Box C hold 400. How many marbles are in each box?')]
put('p2l2-challenge',sec('p2l2-challenge','65–80 MIN',h2('Challenge')+numcards(ch,36),'Pairs try first, then use the "see it" slide if stuck, then the walk-through. These are Think Harder Q5 and Q6. Answers: 1) 10 ways: 507 + 493, 517 + 483, 527 + 473, 537 + 463, 547 + 453, 557 + 443, 567 + 433, 577 + 423, 587 + 413, 597 + 403. 2) A 150, B 100, C 250.'))
g1=colsum('??7','4??','1000','+',x0=40,y0=40,c=100,size=56)
for k in range(0,3): g1+=f'<circle cx="{40+50+k*100}" cy="30" r="20" fill="{WHITE}" stroke="{TEAL}" stroke-width="3" stroke-dasharray="6 4"/>'
g1+=txt(450,470,'Which digits can go in each box?',30,TEAL)
g2=''
for i,(lab,col) in enumerate([('A',SKY),('B',YEL),('C','#BFE3DC')]):
    x=70+i*240; g2+=f'<rect x="{x}" y="40" width="180" height="150" rx="16" fill="{col}" stroke="{NAVY}" stroke-width="4"/>'+txt(x+90,138,lab,70)
for i,(t,y) in enumerate([('A + B = 250',260),('B + C = 350',330),('A + C = 400',400)]):
    g2+=f'<rect x="200" y="{y-44}" width="420" height="60" rx="10" fill="{WHITE}" stroke="{NAVY}" stroke-width="3"/>'+txt(410,y-2,t,36)
g2+=txt(410,470,'How many in each box?',30,TEAL)
body=h2('Challenge: see it',60)+'<div style="display:flex;gap:32px;align-items:flex-start">'
body+=card(f'<p style="font-size:30px;font-weight:700;color:{TEAL}">Q1: Make 1000</p>'+svgwrap(820,500,'Column sum box box 7 plus 4 box box equals 1000, with circles for carries',g1,True),extra='flex:1;min-width:0;padding:20px 24px')
body+=card(f'<p style="font-size:30px;font-weight:700;color:{TEAL}">Q2: Three boxes</p>'+svgwrap(820,500,'Boxes A, B and C with the three pair totals',g2,True),extra='flex:1;min-width:0;padding:20px 24px')+'</div>'
put('p2l2-chdiag',sec('p2l2-chdiag','65–80 MIN',body,'Show after pairs have tried the Challenge, or if they are stuck. The pictures show the problem, not the answer. Ask: Which column can you be sure about first? Will there be a carry? In Q2, compare two of the clues: what is the same, what is different? Answers are in the Challenge slide notes.'))
body=h2('Challenge: walk-through')+pin(128,250,800,p('Q1: one column at a time',38,800,TEAL))
for i,t in enumerate(['Ones: 7 + □ = 10, so □ = 3. Carry 1.','Hundreds: □ + 4 + 1 = 10, so □ = 5.','Tens: □ + □ + 1 = 10, so the two add to 9.','0 + 9, 1 + 8 … 9 + 0: 10 ways (507 + 493 … 597 + 403)']): body+=pin(128,330+i*120,800,p(t,32),'rise',WHITE)
body+=pin(992,250,800,p('Q2: compare the clues',38,800,TEAL))
for i,t in enumerate(['A + B = 250 and B + C = 350: C is 100 more than A.','A + C = 400. Take away the extra 100: 300.','Half of 300 is 150: A = 150, C = 250.','B = 250 − 150 = 100. Check: 100 + 250 = 350 ✓']): body+=pin(992,330+i*120,800,p(t,32),'rise',WHITE)
put('p2l2-chwalk',sec('p2l2-chwalk','Challenge',body,'Use after pairs have tried. Q1: list the tens pairs in order so none is missed: (0, 9), (1, 8) … (9, 0). Many children find a few and stop; ask "How do you know there are no more?" Q2: the same "take away the extra, halve" model as worksheet Q6. Guess and check also works: try A = 100, then B = 150, C = 200, but A + C = 300, too small, so A must be bigger.'))

# ---------- talk / exit ----------
body=h2('Talk time')+card(chip('TALK TIME',YEL,NAVY)+p('Why do we start at the ones column when we look for missing digits?',42,600))+card(p('Sentence starters:',34,400,MUTED)+p('“I noticed that …”   “I tested it by …”   “I know because …”',38,600))
put('p2l2-talk',sec('p2l2-talk','70–80 MIN',body,'Minutes 70 to 80. Pairs talk for 2 minutes, then share. Answer: the ones can make a carry that changes the tens, and the tens can make a carry that changes the hundreds. So we must know the ones first. Second question if time: "Ravi says 398 + 205 = 400 + 203 without adding. How can he know?" (He moved 2 from one number to the other; the total stays the same, 603.) Praise the reasons, not only the answers.'))
body=h2('Exit ticket')+card(chip('EXIT TICKET')+p('4□6 + 37□ = 801.  Find the missing digits.',52,600))+card(p('Write your answer on a slip of paper. Show it to your tutor. Then collect your stamp in your inquiry journal.',34,400))
put('p2l2-exit',sec('p2l2-exit','80–90 MIN',body,'Minutes 80 to 90. Answer: 426 + 375 = 801 (ones 6 + 5 = 11, carry 1; tens 2 + 7 + 1 = 10, carry 1; hundreds 4 + 3 + 1 = 8). Extension: make your own missing-digit sum with two boxes and exactly one answer; swap with a partner.'))

# ---------- write ----------
order=['p2l2-title','p2l2-warm1','p2l2-warm2','p2l2-explore1','p2l2-explore2','p2l2-teach1','p2l2-try1','p2l2-we2','p2l2-try2','p2l2-teach3','p2l2-try3','p2l2-key','p2l2-break','p2l2-ws1','p2l2-ws1ans','p2l2-teachsq','p2l2-teachtri','p2l2-teachtwo','p2l2-ws2','p2l2-ws2ans','p2l2-stretch','p2l2-challenge','p2l2-chdiag','p2l2-chwalk','p2l2-talk','p2l2-exit']
assert set(order)==set(S), set(order)^set(S)
sd=os.path.join(D,'slides')
for f in os.listdir(sd):
    if f.endswith('.html') and f[:-5] not in S: os.remove(os.path.join(sd,f))
for i,h in S.items(): open(os.path.join(sd,i+'.html'),'w').write(h)
deck={'v':4,'createdOnFiles':{'v':1,'at':datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')},'lists':'css',
 'title':'Math Inquirers P2: Lesson 2 – Missing Digit Mysteries','order':order,'cover':'p2l2-title',
 'sections':{'s1':{'description':'Warm-up and explore','start':'p2l2-title'},'s2':{'description':'Teach: missing digits, working backwards and balance','start':'p2l2-teach1'},'s3':{'description':'Worksheet with teaching before each page','start':'p2l2-break'},'s4':{'description':'Stretch, challenge, talk and exit','start':'p2l2-stretch'}},
 'faces':{'fredoka':{'family':'Fredoka','href':'https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&display=swap'},'nunito-sans':{'family':'Nunito Sans','href':'https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@400;600;700&display=swap'}},
 'designSystems':[]}
json.dump(deck,open(os.path.join(D,'deck.json'),'w'),indent=1,ensure_ascii=False)
print(len(order),'slides')
