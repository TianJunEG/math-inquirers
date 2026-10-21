"""Math Inquirers P3, Lesson 3: Times Table Treasure. Writes split/p3l3/project (deck.json + slides/*.html)."""
import json,os,sys,math
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,H)
from slidekit import *
D=os.path.join(H,'..','split','p3l3','project'); os.makedirs(os.path.join(D,'slides'),exist_ok=True)
S={}
def put(i,h): S[i]=h
RED='#D64545'

# ---------- common slide shapes ----------
def title_slide(sid,n,week,title,topic,today,notes):
    return (f'<section id="{sid}" data-transition="fade" style="background:{NAVY};color:{CREAM};font-family:{BF};padding:128px 128px 160px;display:flex;flex-direction:column;justify-content:center;gap:36px">\n'
            f'<p style="font-size:32px;font-weight:700;letter-spacing:4px;color:{YEL}">PRIMARY 3  •  LESSON {n}  •  WEEK {week}</p>\n'
            f'<h1 style="font-family:{HF};font-size:128px;font-weight:600;line-height:1.05">{E(title)}</h1>\n'
            f'<p style="font-size:44px;color:#C9D4EC">{E(topic)}</p>\n'
            f'<div style="background:#26385F;border-radius:24px;padding:40px;display:flex;flex-direction:column;gap:12px"><p style="font-size:28px;font-weight:700;letter-spacing:3px;color:{YEL}">TODAY WE WILL</p><p style="font-size:44px;font-weight:600">{E(today)}</p></div>\n'
            f'<p style="position:absolute;left:128px;bottom:64px;width:1400px;font-size:24px;color:#B7C3DD">{E(FOOT)}</p>\n<aside>{E(notes)}</aside>\n</section>\n')
def break_slide(sid,text,sub,notes):
    return (f'<section id="{sid}" data-transition="fade" style="background:{TEAL};color:{CREAM};font-family:{BF};padding:128px 128px 160px;display:flex;flex-direction:column;justify-content:center;gap:36px">\n'
            f'<p style="font-size:32px;font-weight:700;letter-spacing:4px;color:{YEL}">35–40 MIN</p>\n'
            f'<h2 style="font-family:{HF};font-size:110px;font-weight:600;line-height:1.05">Brain break</h2>\n'
            f'<p style="font-size:48px;font-weight:600">{E(text)}</p>\n<p style="font-size:36px;color:#D7EFEA">{E(sub)}</p>\n'
            f'<p style="position:absolute;left:128px;bottom:64px;width:1400px;font-size:24px;color:#D7EFEA">{E(FOOT)}</p>\n<aside>{E(notes)}</aside>\n</section>\n')
def numbered(items,size=36):
    return ''.join(card(p(f'<span style="color:{TEAL}">{a}</span>  {E(b)}',size,600,raw=True)) for a,b in items)
def explore1(sid,steps,pic,notes):
    lis=''.join(f'<li>{E(s)}</li>' for s in steps)
    inner=chip('EXPLORE')+f'<ol style="font-size:34px;font-weight:600;padding-left:48px;margin:0;display:flex;flex-direction:column;gap:6px">{lis}</ol>'
    return sec(sid,'10–15 MIN',h2('Explore: what to do')+card(inner,extra='padding:24px 40px')+card(pic,extra='padding:12px 24px;align-items:center'),notes)
def talk_slide(sid,q,notes):
    body=h2('Talk time')+card(chip('TALK TIME',YEL,NAVY)+p(q,42,600))+card(p('Sentence starters:',34,400,MUTED)+p('“I noticed that …”   “I tested it by …”   “I know because …”',38,600))
    return sec(sid,'70–80 MIN',body,notes)
def exit_slide(sid,q,notes):
    body=h2('Exit ticket')+card(chip('EXIT TICKET')+p(q,46,600))+card(p('Write your answer on a slip of paper. Show it to your tutor. Then collect your stamp in your inquiry journal.',34,400))
    return sec(sid,'80–90 MIN',body,notes)
def check_rows(sid,time,title,rows,notes,lw=210,gap=128,size=38):
    body=h2(title)
    for i,(a,b) in enumerate(rows):
        top=250+i*gap
        body+=pin(128,top,lw-20,f'<p style="font-size:36px;font-weight:800;color:{TEAL}">{E(a)}</p>',None,WHITE,20,'18px 24px')
        body+=pin(128+lw,top,1664-lw,f'<p style="font-size:{size}px;font-weight:800;line-height:1.2">{E(b)}</p>','pop',YEL,20,'18px 26px')
    return sec(sid,time,body,notes)
def svgwrap(label,w,h,inner,style=''):
    return f'<svg aria-label="{E(label)}" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="width:{w}px;height:{h}px;{style}">{inner}</svg>'
def T(x,y,s,size=34,fill=NAVY,anchor='middle',w=700,font='Nunito Sans, Arial'):
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{w}" text-anchor="{anchor}" fill="{fill}" font-family="{font}">{E(str(s))}</text>'

# ---------- lesson pictures ----------
def digit_circle(cx,cy,R,table=None,label=None,steps=10):
    s=f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="#C9D4EC" stroke-width="3"/>'
    pt=lambda d:(cx+R*math.sin(math.radians(36*d)),cy-R*math.cos(math.radians(36*d)))
    if table:
        seq=[table*i%10 for i in range(1,steps+1)]
        pts=[pt(d) for d in seq]; pts.append(pts[0])
        s+=f'<polyline points="{" ".join(f"{x:.1f},{y:.1f}" for x,y in pts)}" fill="none" stroke="{RED}" stroke-width="5" stroke-linejoin="round"/>'
    for d in range(10):
        x,y=pt(d); lx,ly=cx+(R+34)*math.sin(math.radians(36*d)),cy-(R+34)*math.cos(math.radians(36*d))
        s+=f'<circle cx="{x:.1f}" cy="{y:.1f}" r="13" fill="{YEL}" stroke="{NAVY}" stroke-width="3"/>'+T(f'{lx:.1f}',f'{ly+11:.1f}',d,30)
    if label: s+=T(cx,cy+R+86,label,30,TEAL,w=800)
    return s
def dot_array(rows,cols,split,x0=40,y0=30,g=58,r=19,lab_top='',lab_bot=''):
    s=''
    for i in range(rows):
        y=y0+i*g+(24 if i>=split else 0)
        for j in range(cols):
            s+=f'<circle cx="{x0+j*g}" cy="{y}" r="{r}" fill="{YEL if i<split else SKY}" stroke="{NAVY}" stroke-width="3"/>'
    yl=y0+(split-1)*g+g/2+12
    s+=f'<line x1="{x0-30}" y1="{yl}" x2="{x0+(cols-1)*g+30}" y2="{yl}" stroke="{RED}" stroke-width="5" stroke-dasharray="14 10"/>'
    bx=x0+(cols-1)*g+48
    def br(ya,yb,t): return f'<path d="M{bx} {ya} h18 V{yb} h-18" fill="none" stroke="{NAVY}" stroke-width="4"/>'+T(bx+34,(ya+yb)/2+12,t,34,TEAL,'start',800)
    s+=br(y0-r-4,y0+(split-1)*g+r+4,lab_top)+br(y0+split*g+24-r-4,y0+(rows-1)*g+24+r+4,lab_bot)
    return s

# ---------- 1 title ----------
put('p3l3-title',title_slide('p3l3-title',3,2,'Times Table Treasure','Tables of 6, 7, 8 and 9',
 'Find hidden patterns in the 6, 7, 8 and 9 times tables, use them to check answers, and solve times-table puzzles in order.',
 'Objective: Find and explain patterns in the 6, 7, 8 and 9 times tables, use last-digit patterns, split an array into facts we know, and solve grid and list puzzles in a careful order. Heuristics taught: look for a pattern; make a systematic list. '
 'Materials: Multiplication square (1 to 10), dot paper, coloured pencils, a ruler, mini whiteboards. '
 'Online: Tutor draws on the digit-circle slide. Each child draws 10 dots round a circle (like a clock) labelled 0 to 9, and has dot paper and coloured pencils. '
 'Time plan: warm-up 0 to 10, explore 10 to 25, teaching 25 to 35 (click to reveal each step and answer), brain break 35 to 40, worksheet 40 to 70 with short teaching before each page and a check-together slide after it, talk time 70 to 80, exit ticket 80 to 90. If the class is behind, children finish the last question of each page at home; the check slides cover it.'))

# ---------- 2 warm1: Buzz ----------
strip=''
for i in range(1,29):
    r_,c_=(i-1)//14,(i-1)%14; x=58+c_*112; y=60+r_*120; buzz=i%7==0
    strip+=f'<circle cx="{x}" cy="{y}" r="50" fill="{YEL if buzz else WHITE}" stroke="{NAVY}" stroke-width="4"/>'
    strip+=T(x,y+12,'BUZZ' if buzz else i,26 if buzz else 36,NAVY,w=800,font='Fredoka, Arial')
body=h2('Warm-up: Buzz!')+p('Count round the group. Say “Buzz” instead of any number in the 7 times table.',38,600,MUTED)
body+=pin(128,370,1664,svgwrap('Numbers 1 to 28 with Buzz on 7, 14, 21 and 28',1600,240,strip))
body+=pin(128,650,1664,p('Round 2: Buzz on the 6s, up to 60.   Round 3: Buzz on the 8s, up to 80.',36,700),None,WHITE,20,'20px 28px')
body+=answer(128,770,1664,'7s Buzz numbers: 7, 14, 21, 28, 35, 42, 49, 56, 63, 70')
put('p3l3-warm1',sec('p3l3-warm1','0–5 MIN',body,
 'Minutes 0 to 5. Buzz! Count round the group (online: in the order of the names on screen) from 1 to 70. Any number in the 7 times table is replaced by "Buzz". If someone says the number instead of Buzz, or Buzzes on the wrong number, the count starts again from 1 (keep it light). '
 'Click to show all the 7s Buzz numbers at the end and read them together. Then play again with 6s (to 60) and 8s (to 80). '
 'Ask: "Which numbers were Buzz in BOTH the 6s round and the 8s round?" (24 and 48). "Was any 7s Buzz number also a 6s Buzz number?" (42). Watch for children who count on their fingers from 0 each time: encourage them to add 7 to the last Buzz.'))

# ---------- 3 warm2 ----------
qs=[('1.','6 × 7 = ?','42'),('2.','9 × 9 = ?','81'),('3.','8 × ? = 64','8'),('4.','Which is bigger: 6 × 8 or 7 × 7?','7 × 7, by 1')]
body=h2('Quick questions')+''.join(qrow(128,260+i*150,1250,a,b,40) for i,(a,b,c) in enumerate(qs))+''.join(answer(1420,260+i*150,372,c) for i,(a,b,c) in enumerate(qs))
put('p3l3-warm2',sec('p3l3-warm2','5–10 MIN',body,'Minutes 5 to 10. Children write on whiteboards and show together, then click to reveal. For each one ask: "How did you work it out? Which fact did you use?" Answers: 1) 42  2) 81  3) 8  4) 7 × 7 = 49 is 1 more than 6 × 8 = 48. For 4, ask: "Can you see why they are so close?" (Strong children may notice 6 × 8 is one less than 7 × 7; do not explain it yet.)'))

# ---------- 4 explore1 ----------
pic=svgwrap('Three digit circles: the 6 times table joined as a star, and empty circles for the 4s and 8s',1500,330,
    digit_circle(250,140,96,6,'6s: 6, 2, 8, 4, 0')+digit_circle(750,140,96,None,'4s: your turn')+digit_circle(1250,140,96,None,'8s: your turn'))
put('p3l3-explore1',explore1('p3l3-explore1',['Draw 10 dots round a circle. Label them 0 to 9, like a clock.','Write the 6 times table. Circle the last digit of each answer.','Join the last digits in order: 6 → 2 → 8 → 4 → 0 → back to 6.','Now do the same for the 4s and the 8s. Compare the shapes.'],pic,
 'Minutes 10 to 15. Pairs work with: dot paper or plain paper, coloured pencils, a ruler. Each pair draws three digit circles. Model the first two lines of the 6s on the slide: 6 × 1 = 6, so start at 6; 6 × 2 = 12, last digit 2, so draw a line from 6 to 2. Then pairs finish the 6s and do the 4s and the 8s with a different colour each. '
 'Online: children draw on paper and hold the circles up to the camera. Early finishers: try the 7s and the 3s (they make the same 10-pointed star, which uses every digit).'))

# ---------- 5 explore2 ----------
eq=[('1.','Which tables made the same shape?'),('2.','Why does the 6s shape never touch an odd digit?'),('3.','Predict: which table makes the same shape as the 3s? Test it.')]
put('p3l3-explore2',sec('p3l3-explore2','15–25 MIN',h2('Explore: talk about it')+numbered(eq,40),
 'Minutes 15 to 25. Let pairs keep working, then gather them for these three questions. Take ideas before giving any answer and ask "How could we test that?" '
 'Answers: 1) The 4s and the 6s make the same 5-pointed star, going round opposite ways (4, 8, 2, 6, 0 and 6, 2, 8, 4, 0). The 2s and the 8s make the same 5-sided shape. '
 '2) Every answer in the 6 times table is even: 6 groups can always be put into 3 pairs of groups, so nothing is left over. '
 '3) The 7s, because 3 + 7 = 10, just like 4 + 6 and 2 + 8. Let a pair test it on a new circle. Keep the circles: we use last digits again in the teaching.'))

# ---------- 6 teach1: patterns in the 8s ----------
W=[190]+[104]*10
body=h2('Look for a pattern: the 8 times table')
body+=trow(128,250,['8 ×']+[str(i) for i in range(1,11)],W,None,True,34)
body+=trow(128,345,['Answer']+[str(8*i) for i in range(1,11)],W,None,False,34)
body+=trow(128,440,['Last digit']+[str(8*i%10) for i in range(1,11)],W,'rise',False,34)
body+=pin(128,560,1664,p('Notice it: the last digits go 8, 6, 4, 2, 0 and then repeat.',38,700),'fade',SOFT,20,'20px 30px')
body+=pin(128,670,1664,p('Test it: 8 × 11 = 88 and 8 × 12 = 96. Do they carry on the pattern? (8, 6: yes!)',38,700),'fade',WHITE,20,'20px 30px')
body+=pin(128,780,1664,p('Explain why: adding 8 is the same as adding 10 and taking away 2, so the ones digit goes down by 2.',36,700),'fade',WHITE,20,'20px 30px')
put('p3l3-teach1',sec('p3l3-teach1','25–27 MIN',body,
 'Teach the first heuristic: LOOK FOR A PATTERN. Say: "Mathematicians notice a pattern, test it, then explain why it works. That is our slogan!" Click 1 shows the last digits. Ask: "What do you notice?" before click 2. Click 3: test the pattern on numbers beyond the table. Click 4: explain why: 8 = 10 − 2, so every time we add 8 the ones digit goes down by 2 (and the tens digit goes up). '
 'Think-aloud: "Look at the 8 times table: 8, 16, 24, 32, 40, 48 … The last digits go 8, 6, 4, 2, 0, then again. So the pattern repeats every 5." Do not teach the 9s patterns here: children discover them in worksheet Q1.'))

# ---------- 7 we1 ----------
body=h2('Worked example: the last digit')+card(p('What is the last digit of 8 × 23? Do not work out the whole answer.',44,700))
body+=step(1,'Split 23 into 20 and 3.  8 × 20 = 160 ends in 0.',top=420,size=38)
body+=step(2,'So only 8 × 3 decides the last digit.  8 × 3 = 24 ends in 4.',top=530,size=38)
body+=step(3,'The last digit of 8 × 23 is 4.',top=640,size=38)
body+=step(4,'Check: 8 × 23 = 160 + 24 = 184.  It ends in 4 ✓',top=750,size=38)
put('p3l3-we1',sec('p3l3-we1','27–28 MIN',body,'Click to reveal each step. Before each click ask the group to predict it. Stress step 2: "Only the ones digit of 23 matters for the last digit." Think-aloud: "8 × 20 ends in 0, so only 8 × 3 matters. 8 × 3 = 24, so 8 × 23 ends in 4. Check: 8 × 23 = 184. Yes." Then ask: "What is the last digit of 8 × 33? 8 × 43?" (still 4).'))

# ---------- 8 try1 ----------
put('p3l3-try1',try_slide('p3l3-try1','28–29 MIN','Your turn: last digits','Only the ones digit matters. Then check by working it out.',
 [('a','Last digit of 6 × 14?','4'),('b','Last digit of 8 × 17?','6'),('c','Last digit of 9 × 12?','8')],
 'Whiteboards, hold up together, then click. a) 6 × 4 = 24, so 4 (6 × 14 = 84). b) 8 × 7 = 56, so 6 (8 × 17 = 136). c) 9 × 2 = 18, so 8 (9 × 12 = 108). Ask a child to explain c out loud using the words "only the ones digit".'))

# ---------- 9 teach2: split an array ----------
arr=svgwrap('An array of 6 rows of 8 dots split into 5 rows and 1 row',760,400,dot_array(6,8,5,40,34,56,18,'5 × 8','1 × 8'))
body=h2('Use facts you know: split the array')+pin(128,250,760,arr)
body+=step(1,'6 × 8 is 6 rows of 8.  Cut off 5 rows.',left=940,top=260,width=852,size=36)
body+=step(2,'5 rows of 8:  5 × 8 = 40',left=940,top=380,width=852,size=36)
body+=step(3,'1 more row of 8:  1 × 8 = 8',left=940,top=500,width=852,size=36)
body+=step(4,'Add the parts:  40 + 8 = 48.  So 6 × 8 = 48.',left=940,top=620,width=852,size=36)
body+=pin(128,770,1664,p('Fives are easy facts. Split a hard fact into a five fact and a small fact, then ADD.',36,700),'fade',SOFT,20,'20px 30px')
put('p3l3-teach2',sec('p3l3-teach2','29–31 MIN',body,'Teach: use facts you know. Show the array on dot paper (or draw it). Cover the bottom row with a ruler: "How many dots above the ruler? 5 rows of 8 is 40. How many below? One row of 8. Altogether 40 + 8 = 48." Click through the steps. Common slip: giving 40 as the answer and forgetting to add the second part. Ask: "Where else could I cut it?" (3 rows and 3 rows: 24 + 24 = 48).'))

# ---------- 10 we2 ----------
body=h2('Worked example: 9 × 7 two ways')+card(p('Find 9 × 7 using facts you know.',44,700))
body+=step(1,'Way 1: split 9 rows of 7 into 5 rows and 4 rows.  5 × 7 = 35,  4 × 7 = 28',top=400,size=36)
body+=step(2,'Add the parts:  35 + 28 = 63',top=510,size=36)
body+=step(3,'Way 2: 10 rows of 7 is 70. Take away one row of 7:  70 − 7 = 63',top=620,size=36)
body+=step(4,'Both ways give 63 ✓  So 9 × 7 = 63.',top=730,size=36)
put('p3l3-we2',sec('p3l3-we2','31–32 MIN',body,'Click through. Way 2 is the "one too many" trick: 9 of something is 10 of it, take one away. Think-aloud: "For 9 × 7 I can do 10 sevens, which is 70, and take one 7 away: 63. I check it the other way: 35 + 28 is also 63." Two ways that agree is a strong check.'))

# ---------- 11 try2 ----------
put('p3l3-try2',try_slide('p3l3-try2','32–33 MIN','Your turn: split it','Write the two facts you used, then the answer.',
 [('a','6 × 7','35 + 7 = 42'),('b','8 × 6','30 + 18 = 48'),('c','9 × 8','80 − 8 = 72')],
 'Whiteboards. Accept any correct split. a) 5 × 7 + 1 × 7 = 35 + 7 = 42. b) 5 × 6 + 3 × 6 = 30 + 18 = 48. c) 10 × 8 − 8 = 72, or 5 × 8 + 4 × 8 = 40 + 32 = 72. Ask two children with different splits to show theirs.'))

# ---------- 12 key ----------
body=h2('Key idea: look for a pattern')+card(p('Look for a pattern and test it. Use facts you know to find facts you do not know.',46,700))+card(p('When there are many answers, make a list in order so none are missed.',38,600,MUTED))
put('p3l3-key',sec('p3l3-key','33–35 MIN',body,'Say the key idea together. Common mistakes to watch for during the worksheet: (1) Checking the 9s table only by "the digits add up to 9" (81 passes, but 9 × 8 is 72). (2) Splitting an array and then giving one part as the answer (40 instead of 40 + 16). (3) Missing or repeating ways in a list because the rows are not tried in order 2, 3, 4, 5 …'))

# ---------- 13 break ----------
put('p3l3-break',break_slide('p3l3-break','Times-table jumps. I call a fact like 6 × 3: do 3 jumps and count 6, 12, 18 out loud.','Then: a drink of water and back to our seats.','Five minutes. Call 6 × 3, 7 × 2, 8 × 3, 9 × 2. Online: children stay in view of the camera and jump on the spot.'))

# ---------- 14-15 worksheet page 1 ----------
put('p3l3-ws1',ws_preview('p3l3-ws1','40–52 MIN','Worksheet page 1: with your partner',[('Q1','Patterns in the 9 times table. Notice, test, explain.'),('Q2','Last digits of the 7 times table. Test the 3, 6 and 9 tables: which use every digit?'),('Q3','Split 7 rows of 8 dots. Then split 9 × 6 your own way.')],'Stuck? Write the table in order and look at the ones digits.',
 'Minutes 40 to 52. Pairs work together. Walk around and ask "What pattern do you notice? Does it work every time?" For Q1b push for the pattern that catches Ali: the tens digit is one less than the number of nines. For Q2a pairs test only the 3, 6 and 9 tables (6 gives only even digits) and may need the digit circles from the explore.'))
put('p3l3-ws1ans',check_rows('p3l3-ws1ans','52–54 MIN','Page 1: check together',[
 ('Q1','9, 18, 27, 36, 45, 54, 63, 72, 81, 90'),
 ('Q1a','Tens digit up 1, ones digit down 1. Digits add to 9.'),
 ('Q1b','9 × 8: tens digit is 8 − 1 = 7, so 72. 81 is 9 × 9.'),
 ('Q2','7, 4, 1, 8, 5, 2, 9, 6, 3, 0.   a) 3 and 9   b) 2'),
 ('Q3','a) 40, 16, 56    b) e.g. 30 + 24 = 54')],
 'Click each answer after a pair explains theirs. Q1a also accept: the tens digit is 1 less than the number of nines. Q1b: the digit-sum test alone is not enough, because 81 also has digits adding to 9; the tens-digit pattern shows 9 × 8 must be in the 70s. '
 'Q2a: the 3s go 3, 6, 9, 2, 5, 8, 1, 4, 7, 0 and the 9s go 9, 8, 7 … 0. The 6s give only even digits (6, 2, 8, 4, 0). Ask why the even tables cannot work (all their answers are even) and why the 5s cannot (only 5 and 0). Q2b: 7 × 6 = 42 ends in 2; 7 × 46 = 322. Q3b: any correct split, e.g. 5 × 6 + 4 × 6 or 10 × 6 − 6.'))

# ---------- 16 teach grid ----------
GW=[130,180,180]
body=h2('Grid puzzles: start with a one-way number')
body+=trow(128,260,['×','?','?'],GW,None,True,40)+trow(128,365,['?','72',''],GW,None,False,40)+trow(128,470,['?','63','42'],GW,None,False,40)
body+=trow(128,260,['×','9','6'],GW,'fade',True,40)+trow(128,365,['8','72','48'],GW,'fade',False,40)+trow(128,470,['7','63','42'],GW,'fade',False,40)
body+=pin(128,600,560,p('Rows and columns use numbers from 1 to 10.',32,600,MUTED),None)
body+=step(1,'63 can only be 7 × 9. 72 can only be 8 × 9. They share the first column, so it is 9.',left=800,top=260,width=932,size=34)
body+=step(2,'Then the rows are 8 (8 × 9 = 72) and 7 (7 × 9 = 63).',left=800,top=420,width=932,size=34)
body+=step(3,'42 = 7 × 6, so the second column is 6.',left=800,top=530,width=932,size=34)
body+=step(4,'Fill the gap: 8 × 6 = 48. Check every number ✓',left=800,top=640,width=932,size=34)
put('p3l3-teachgrid',sec('p3l3-teachgrid','54–56 MIN',body,'Teach before worksheet page 2 (Q4 is a 3 by 3 grid puzzle). Ask first: "Which number can be made in only ONE way with numbers from 1 to 10?" Children list factor pairs: 72 = 8 × 9 only; 63 = 7 × 9 only; 42 = 6 × 7 only. Click order: steps 1 to 3, then the finished grid fades in, then step 4. On the worksheet, do NOT tell them where to start; the hint says to look for a number made in only one way.'))

# ---------- 17 teach list ----------
LW=[170,280,190]
body=h2('Every way, in order: arrays of 18')+card(p('Put 18 chairs in equal rows. At least 2 rows and at least 2 chairs in each row.',38,700),extra='padding:22px 34px')
rows=[('2','9','yes'),('3','6','yes'),('4','—','no'),('5','—','no'),('6','3','yes'),('7','—','no'),('8','—','no'),('9','2','yes')]
for k,(a,b,c) in enumerate(rows):
    L=128 if k<4 else 900; top=470+(k%4)*82
    body+=trow(L,top,[a,b,c],LW,'rise',False,32)
body+=trow(128,388,['Rows','In each row','Works?'],LW,None,True,30)+trow(900,388,['Rows','In each row','Works?'],LW,None,True,30)
body+=pin(128,820,1664,p('4 ways. Stop at 9 rows: 10 or more rows would leave fewer than 2 in a row.',34,700),'fade',SOFT,20,'16px 28px')
put('p3l3-teachlist',sec('p3l3-teachlist','56–57 MIN',body,'Teach the second heuristic: MAKE A SYSTEMATIC LIST. Before worksheet Q5 (36 chairs). Click to add each row while children say whether it works: "Can 18 be shared into 4 equal rows?" (No: 4 rows of 4 is 16, 2 are left over.) Point out the pairs: 2 rows of 9 and 9 rows of 2, 3 rows of 6 and 6 rows of 3. Ask: "How do we know we have them all?" (We tried every number of rows in order.) Do not do 36: that is Q5.'))

# ---------- 18 teach two clues ----------
body=h2('Two clues: list one, test the other')+card(p('I am a 2-digit number. I can be divided exactly by 7 and by 3. My digits add up to 3.',40,700))
body+=step(1,'List the 2-digit numbers you can divide by 7:  14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98',top=420,size=34)
body+=step(2,'Test each one: which can be divided by 3?  21, 42, 63, 84',top=580,size=34)
body+=step(3,'Add the digits: 2 + 1 = 3 ✓   (42 → 6,  63 → 9,  84 → 12)   I am 21.',top=690,size=34)
put('p3l3-teachboth',sec('p3l3-teachboth','57–58 MIN',body,'Teach before worksheet Q6. Strategy: list the numbers for ONE clue in order, then test the other clues one at a time. Ask: "Why list the 7s, not the 3s?" (There are fewer of them, so the list is shorter.) Children may notice 21, 42, 63, 84 go up in 21s. Do not do Q6 (6 and 8) here.'))

# ---------- 19-20 worksheet page 2 ----------
put('p3l3-ws2',ws_preview('p3l3-ws2','58–66 MIN','Worksheet page 2: on your own',[('Q4','Grid puzzle. Find a number that can be made in only one way.'),('Q5','Every way to put 36 chairs in equal rows. Go in order. Only write the ways that work.'),('Q6','If time: number riddle. List one clue, then test the others.')],'Finished early? Stretch and Challenge come next.','Children work alone. Note who needs a short catch-up next lesson. For Q4, if a child is stuck after a few minutes, ask "Which number is in only one times table up to 10 × 10?" (81).'))
put('p3l3-ws2ans',check_rows('p3l3-ws2ans','66–68 MIN','Page 2: check together',[
 ('Q4','Rows 7, 9, 6.   Columns 8, 6, 9.'),
 ('Q4','56, 42, 63  /  72, 54, 81  /  48, 36, 54'),
 ('Q5','2×18, 3×12, 4×9, 6×6, 9×4, 12×3, 18×2'),
 ('Q5','b) 7 ways   c) 6 rows of 6 has no partner'),
 ('Q6','a) 24, 48, 72, 96    b) 48')],
 'Click after a child explains. Q4: start with 81 = 9 × 9, so the middle row and the last column are 9. Then 56 = 7 × 8 and 48 = 6 × 8 share the first column, so it is 8 (7 × 7 = 49 rules out 7), giving rows 7 and 6; 36 = 6 × 6 gives the middle column 6. '
 'Q5: 5, 7, 8, 10 and 11 rows do not work. The number of ways is odd because 6 × 6 pairs with itself. Q6: list 16, 24, 32 … 96 and test each for ÷ 6: 24, 48, 72, 96. Digit sums 6, 12, 9, 15, so 48.'))

# ---------- 21 stretch ----------
st=[('1.','Which is more, 7 × 8 or 6 × 9? By how much?'),('2.','The last digit of 9 × 9 is 1. What is the last digit of 9 × 9 × 9 × 9?'),('3.','Ben multiplies a number by 6. The answer ends in 4. What could the last digit of his number be? Find all.')]
put('p3l3-stretch',sec('p3l3-stretch','For early finishers',h2('Stretch')+numbered(st,38),'For children who finish early. Answers: 1) 7 × 8 = 56 is 2 more than 6 × 9 = 54. 2) 1: the last digits go 9, 1, 9, 1 (9 × 9 × 9 × 9 = 6561). 3) 4 or 9: 6 × 4 = 24 and 6 × 9 = 54; check every digit 0 to 9, no other one gives a last digit of 4.'))

# ---------- 22 challenge ----------
ch=[('1.','In a multiplication square, the top row of a 2 by 2 block shows 42 and 48. The row below shows 49 and 56. What are the two row numbers and the two column numbers?'),('2.','Ben writes the answers of the 6 times table from 6 × 1 to 6 × 20. How many of the answers end in 8?')]
put('p3l3-challenge',sec('p3l3-challenge','Challenge',h2('Challenge')+numbered(ch,38),'Pairs try first, then use the "see it" slide if stuck, then the walk-through. Answers: 1) Rows 6 and 7, columns 7 and 8. Start with 49: it can only be 7 × 7. 2) 4 answers: 18, 48, 78, 108. The last digits 6, 2, 8, 4, 0 repeat every 5, so 8 comes once in every 5 answers.'))

# ---------- 23 chdiag ----------
g=''
cells=[['×','?','?'],['?','42','48'],['?','49','56']]
for i,rw in enumerate(cells):
    for j,c in enumerate(rw):
        x=60+j*190; y=40+i*120; hd=(i==0 or j==0)
        g+=f'<rect x="{x}" y="{y}" width="190" height="120" fill="{YEL if hd else WHITE}" stroke="{NAVY}" stroke-width="4"/>'+T(x+95,y+78,c,52,NAVY,w=700,font='Fredoka, Arial')
g+=T(345,470,'Which number can be made in only one way?',28,TEAL,w=800)
q1=svgwrap('A 2 by 2 block of a multiplication square with hidden row and column numbers',690,500,g,'width:100%;height:auto')
h_=''
for k in range(20):
    x=24+(k%10)*64; y=70+(k//10)*170
    h_+=T(x+28,y-14,f'×{k+1}',24,MUTED,w=700)+f'<rect x="{x}" y="{y}" width="56" height="70" rx="8" fill="{SOFT if k<2 else WHITE}" stroke="{NAVY}" stroke-width="3"/>'
    if k<2: h_+=T(x+28,y+48,[6,2][k],38,NAVY,w=800,font='Fredoka, Arial')
h_+=T(345,440,'Last digits of 6 × 1 to 6 × 20.',28,NAVY,w=700)+T(345,480,'How many will be 8?',28,TEAL,w=800)
q2=svgwrap('Twenty boxes for the last digits of the 6 times table from 6 times 1 to 6 times 20',690,500,h_,'width:100%;height:auto')
body=h2('Challenge: see it',60)+'<div style="display:flex;gap:32px;align-items:flex-start">'+card('<p style="font-size:30px;font-weight:700;color:#1F7A6F">Q1: The hidden block</p>'+q1,extra='flex:1;min-width:0;padding:20px 24px')+card('<p style="font-size:30px;font-weight:700;color:#1F7A6F">Q2: Last digits to × 20</p>'+q2,extra='flex:1;min-width:0;padding:20px 24px')+'</div>'
put('p3l3-chdiag',sec('p3l3-chdiag','Challenge',body,'Show after pairs have tried the Challenge, or if they are stuck. The pictures show the problem, not the answer. Ask: What do you notice? What do we know? Which number should we start with? Could we use a pattern instead of writing all 20 answers? Answers are in the Challenge slide notes.'))

# ---------- 24 chwalk ----------
body=h2('Challenge: walk-through')+pin(128,250,800,p('Q1: start with 49',38,800,TEAL))
for i,t in enumerate(['49 can only be 7 × 7: row 2 is 7, column 1 is 7.','42 = 6 × 7, so row 1 is 6.','56 = 7 × 8, so column 2 is 8.','Check: 6 × 8 = 48 ✓  Rows 6, 7. Columns 7, 8.']): body+=pin(128,330+i*120,800,p(t,32),'rise',WHITE)
body+=pin(992,250,800,p('Q2: use the pattern',38,800,TEAL))
for i,t in enumerate(['Last digits repeat every 5: 6, 2, 8, 4, 0.','So 8 comes once in every 5 answers.','20 answers = 4 groups of 5, so 4 answers end in 8.','Check: 18, 48, 78, 108 ✓']): body+=pin(992,330+i*120,800,p(t,32),'rise',WHITE)
put('p3l3-chwalk',sec('p3l3-chwalk','Challenge',body,'Use after pairs have tried. Q1: the same idea as the worksheet grid: find the number with only one factor pair. Q2: children who wrote all 20 answers are right too; ask them to look for the shortcut. 6 × 13 = 78 and 6 × 18 = 108.'))

# ---------- 25-26 talk, exit ----------
put('p3l3-talk',talk_slide('p3l3-talk','Why is every answer in the 6 times table even, but the 7 times table has odd and even answers?','Minutes 70 to 80. Pairs talk for 2 minutes, then share. Praise the reasons, not only the answers. Expected: 6 groups can always be put into 3 pairs of groups, so nothing is left over and the answer is even. With 7 groups one group has no partner, so when each group is odd (7 × 3 = 21) the answer is odd. Use counters in 6 or 7 groups to show it.'))
put('p3l3-exit',exit_slide('p3l3-exit','What is the last digit of 6 × 47? Explain how you know without working out 6 × 47.','Minutes 80 to 90. Answer: 2. Only 6 × 7 = 42 decides the last digit, because 6 × 40 ends in 0. (6 × 47 = 282.) Extension: draw last-digit circles for all the tables from 1 to 9 and group the tables that make the same shape.'))

# ---------- write ----------
order=['p3l3-title','p3l3-warm1','p3l3-warm2','p3l3-explore1','p3l3-explore2','p3l3-teach1','p3l3-we1','p3l3-try1','p3l3-teach2','p3l3-we2','p3l3-try2','p3l3-key','p3l3-break','p3l3-ws1','p3l3-ws1ans','p3l3-teachgrid','p3l3-teachlist','p3l3-teachboth','p3l3-ws2','p3l3-ws2ans','p3l3-stretch','p3l3-challenge','p3l3-chdiag','p3l3-chwalk','p3l3-talk','p3l3-exit']
assert set(order)==set(S), set(order)^set(S)
for f in os.listdir(os.path.join(D,'slides')):
    if f.endswith('.html') and f[:-5] not in S: os.remove(os.path.join(D,'slides',f))
for i,h in S.items(): open(os.path.join(D,'slides',i+'.html'),'w').write(h)
deck={'v':4,'createdOnFiles':{'v':1,'at':'2026-10-21T12:00:00Z'},'lists':'css','title':'Math Inquirers P3: Lesson 3 – Times Table Treasure','order':order,'cover':'p3l3-title',
 'sections':{'s1':{'description':'Warm-up and explore','start':'p3l3-title'},'s2':{'description':'Teach: look for a pattern, use facts you know','start':'p3l3-teach1'},'s3':{'description':'Worksheet with teaching before each page','start':'p3l3-break'},'s4':{'description':'Stretch, challenge, talk and exit','start':'p3l3-stretch'}},
 'faces':{'fredoka':{'family':'Fredoka','href':'https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&display=swap'},'nunito-sans':{'family':'Nunito Sans','href':'https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@400;600;700&display=swap'}},
 'designSystems':[]}
json.dump(deck,open(os.path.join(D,'deck.json'),'w'),indent=1,ensure_ascii=False)
print(len(order),'slides')
