"""Math Inquirers Level 4, Lesson 5: Decimal Detectives. Writes split/p4l5/project (deck.json + slides/*.html)."""
import json,os,sys,datetime
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,H)
import slidekit
from slidekit import *
slidekit.FOOT='Math Inquirers Level 4 Holiday Program  •  Notice it. Test it. Explain why.'
P='p4l5'
D=os.path.join(H,'..','split',P,'project'); os.makedirs(os.path.join(D,'slides'),exist_ok=True)
S={}
def put(i,h): S[f'{P}-{i}']=h
RED='#D64545'; FOOTX=slidekit.FOOT

# ---------- shared slide shapes (same look as the P1 and P2 decks) ----------
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
def svgwrap(w,h,label,inner,css=None):
    st=css or f'width:{w}px;height:{h}px;flex:none'
    return f'<svg aria-label="{E(label)}" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="{st}">{inner}</svg>'
def txt(x,y,s,size=40,fill=NAVY,anchor='middle',weight=700,font='Fredoka, Arial'):
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" fill="{fill}" font-family="{font}">{E(str(s))}</text>'
def dcards(digits,x0=0,y=6,w=96,h=124,gap=26,fill=YEL):
    g=''
    for i,d in enumerate(digits):
        x=x0+i*(w+gap)
        f=WHITE if d=='.' else fill
        g+=f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="16" fill="{f}" stroke="{NAVY}" stroke-width="5"/>'
        g+=(f'<circle cx="{x+w/2}" cy="{y+h*0.72}" r="11" fill="{NAVY}"/>' if d=='.' else txt(x+w/2,y+h/2+24,d,70))
    return g
def nline(x0,x1,y,n,labels,arrows=(),ticksize=18,lab=34,big=(),band=None,col=RED):
    """number line from x0 to x1 with n steps; labels {i:text}; arrows [(pos,label)]; band (a,b) shaded steps"""
    k=(x1-x0)/n; g=''
    if band: g+=f'<rect x="{x0+band[0]*k}" y="{y-34}" width="{(band[1]-band[0])*k}" height="68" fill="{YEL}" opacity="0.45"/>'
    g+=f'<line x1="{x0-20}" y1="{y}" x2="{x1+20}" y2="{y}" stroke="{NAVY}" stroke-width="5"/>'
    for i in range(n+1):
        t=ticksize*(1.6 if (i in labels or i in big) else 1)
        g+=f'<line x1="{x0+i*k}" y1="{y-t}" x2="{x0+i*k}" y2="{y+t}" stroke="{NAVY}" stroke-width="{5 if i in labels else 3}"/>'
    for i,s in labels.items(): g+=txt(x0+i*k,y+ticksize*1.6+lab+8,s,lab)
    for pos,s in arrows:
        x=x0+pos*k
        g+=f'<line x1="{x}" y1="{y-96}" x2="{x}" y2="{y-36}" stroke="{col}" stroke-width="6"/><polygon points="{x},{y-26} {x-13},{y-46} {x+13},{y-46}" fill="{col}"/>'+txt(x,y-108,s,36,col)
    return g
def bar(x,y,w,h,fill,label='',size=34):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="{NAVY}" stroke-width="4"/>'+(txt(x+w/2,y+h/2+size*0.36,label,size) if label else '')
def brace(x0,x1,y,label,size=32,up=True):
    d=-1 if up else 1
    return f'<path d="M{x0} {y} v{d*14} H{x1} v{-d*14}" fill="none" stroke="{NAVY}" stroke-width="4"/>'+txt((x0+x1)/2,y+d*26 if up else y+44,label,size,TEAL)

# ---------- 1. title ----------
put('title',title_slide(f'{P}-title','LESSON 5  •  WEEK 3','Decimal Detectives','Decimals',
 'Zoom in on number lines, order decimals to 3 places, round and work backwards from a rounded number, and solve money and mass puzzles.',
 'Objective: Read decimals to 3 places on number lines, compare and order them by place value, round to the nearest whole number, 1 or 2 decimal places and work backwards from a rounded number (smallest and largest), and solve money and mass puzzles with bar models. '
 'Thinking strategies today: ZOOM IN (what is one step worth?), LINE UP THE POINTS, MAKE A LIST IN ORDER, DRAW A BAR MODEL. '
 'Materials: Digit cards 0 to 9 and a decimal point card for each child, a place-value chart (ones, tenths, hundredths, thousandths), mini whiteboards, a metre ruler, play money. '
 'Online: children cut out paper digit cards and a paper decimal point before the lesson and move them on camera; the tutor marks the zoom-in number lines on the slides. '
 'Time plan: Warm-up check 1 to 4 (two questions on the key idea; children who get both right and can say why start on the Think Harder pages at minute 34), warm-up game 4 to 6 (one short round), quick questions 6 to 8, explore 8 to 18, teaching 18 to 30 (click to reveal each step and answer; the "your turn" slides are optional, skip them if short of time), brain break 30 to 34, worksheet page 1 from 34 to 50 and check together 50 to 53, short teaching before page 2 from 53 to 58, worksheet page 2 from 58 to 76 and check together 76 to 80, talk time 80 to 85, exit ticket 85 to 88, What was hard? reflection 88 to 90. The Challenge slides and the Think Harder pages are for early finishers and for take-home: they have no fixed time slot. Online: page 1 is pair work, so allow about 2 minutes to move into and out of breakout rooms (or run page 1 as a whole-group screen-share if there are only 8 children).'))

# ---------- 2. warm-up game ----------
g=''
for i,x in enumerate([40,250,400]):
    g+=f'<rect x="{x}" y="50" width="130" height="160" rx="14" fill="{WHITE}" stroke="{NAVY}" stroke-width="5" stroke-dasharray="14 8"/>'
g+=f'<circle cx="210" cy="190" r="13" fill="{NAVY}"/>'
g+=txt(105,250,'ones',30,TEAL)+txt(315,250,'tenths',30,TEAL)+txt(465,250,'hundredths',30,TEAL)
g+=dcards(['6'],680,60,110,140)+txt(880,160,'?',90,TEAL)
for i in range(3): g+=f'<rect x="{960+i*130}" y="70" width="96" height="120" rx="14" fill="{SKY}" stroke="{NAVY}" stroke-width="4"/>'
g+=txt(1110,250,'cards still to come …',30,MUTED,weight=600,font='Nunito Sans, Arial')
g+=f'<rect x="1340" y="60" width="250" height="150" rx="20" fill="{SOFT}" stroke="{NAVY}" stroke-width="4"/>'+txt(1465,125,'Target',34,TEAL)+txt(1465,185,'5',64)
body=h2('Warm-up: Target 5')+card(p('I turn over one digit card at a time. Write it in a box straight away. No moving it later! The number closest to 5 wins.',38,700))
body+=pin(128,420,1664,svgwrap(1600,280,'Three empty boxes for ones, tenths and hundredths with a decimal point, a digit card 6 waiting, and the target 5',g),None,WHITE,24,'16px 32px')
body+=pin(128,770,1664,p('Where would you put a 4? A 5? A 9? Is a 6 in the ones box a good idea?',36,700),'fade',SOFT,20,'20px 30px')
put('warm1',sec(f'{P}-warm1','4–6 MIN',body,
 'Minutes 4 to 6 (one short round, about 2 minutes: the Warm-up check came first). Target 5. Children draw three empty boxes with a point after the first on a whiteboard. Shuffle digit cards 0 to 9 and turn over one at a time (online: hold it up to the camera). After EACH card, children write it in one empty box at once and cannot move it. After three cards, everyone reads their number aloud; the number closest to 5 wins (work out how far each is from 5). '
 'Play ONE round only (target 5), about 2 minutes. Keep target 2.5 and the smallest-number round for another day or for take-home. Click to show the thinking question. Talk: "A 4 or a 5 belongs in the ones box: 4.9 something or 5.0 something is close to 5. A 9 in the ones box is a disaster. A 9 in the hundredths box hardly matters: it is only 9 hundredths." '
 'Listen for children who say "the ones digit matters most, then the tenths". That is the key idea of today.'))

# ---------- 3. quick questions ----------
qs=[('1.','What is the 7 worth in 3.475?','0.07'),('2.','6 tenths and 4 thousandths = ?','0.604'),('3.','Which is bigger: 0.8 or 0.75?','0.8'),('4.','Round 4.68 to 1 decimal place.','4.7'),('5.','How much more than $3.05 is $5?','$1.95')]
body=h2('Quick questions')+''.join(qrow(128,250+i*125,1250,a,b) for i,(a,b,c) in enumerate(qs))+''.join(answer(1420,250+i*125,372,c) for i,(a,b,c) in enumerate(qs))
put('warm2',sec(f'{P}-warm2','6–8 MIN',body,'Minutes 6 to 8. Read each aloud, whiteboards up together, then click to show. 1) 7 hundredths. 2) Watch for 0.64: the 4 must be in the thousandths place, so the hundredths place needs a 0. 3) Many children say 0.75 because 75 > 8. Write 0.80 under 0.75: 8 tenths beats 7 tenths. Finish with the line: "0.8 is the same as 0.80. 0.80 is bigger than 0.75." It comes back in the teaching. 4) 4.68 is between 4.6 and 4.7, nearer 4.7. 5) Count on: $3.05 → $4 is 95¢, $4 → $5 is $1, so $1.95.'))

# ---------- 4. explore: what to do ----------
g=dcards(['2','5','8','.'],40,30,110,140)+f'<rect x="620" y="40" width="380" height="120" rx="18" fill="{WHITE}" stroke="{NAVY}" stroke-width="4"/>'+txt(810,90,'for example',28,MUTED,weight=600,font='Nunito Sans, Arial')+txt(810,142,'25.8',52)
g+=f'<rect x="1080" y="30" width="500" height="140" rx="18" fill="{SOFT}" stroke="{NAVY}" stroke-width="4"/>'+txt(1330,90,'Find every number.',34)+txt(1330,145,'Which is closest to 5?',32,TEAL)
steps=''.join(f'<li>{E(s)}</li>' for s in ['Take the digit cards 2, 5, 8 and the decimal point card.','Make a decimal with all four cards. The point goes between two digits.','Make as many different numbers as you can. Write each one down.','Put them in order. Which one is closest to 5?'])
body=h2('Explore: what to do')+card(chip('EXPLORE')+f'<ol style="font-size:36px;font-weight:600;padding-left:52px;display:flex;flex-direction:column;gap:8px">{steps}</ol>')
body+=card(svgwrap(1600,200,'Digit cards 2, 5 and 8 and a decimal point card, an example 25.8, and the question which is closest to 5',g),extra='padding:20px 32px')
put('explore1',sec(f'{P}-explore1','8–13 MIN',body,'Minutes 8 to 13. Pairs work with digit cards 2, 5, 8 and a decimal point card (online: paper cards on camera). Ask them to predict first: how many numbers? Let them record numbers in any order at first. Ask "Where can the point go?" (after the first digit or after the second digit; not at the start or the end, because then it is not between two digits). Early finishers: which number is closest to 50? (52.8, only 2.8 away; 58.2 is 8.2 away).'))

# ---------- 5. explore: talk ----------
body=h2('Explore: talk about it')+numcards([('1.','How many numbers did you make? How do you know you have them all?'),('2.','Which number is the smallest? The largest?'),('3.','Which number is closest to 5? How do you know?')],40)
put('explore2',sec(f'{P}-explore2','13–18 MIN',body,'Minutes 13 to 18. Let pairs keep working, then gather them. Write their numbers on the board in the order they say them, messy on purpose, then ask "Is anything missing? Is anything there twice?" Answers: 1) 12 numbers. The three digits can be arranged 6 ways (258, 285, 528, 582, 825, 852) and the point can go in 2 places: 2.58, 2.85, 5.28, 5.82, 8.25, 8.52, 25.8, 28.5, 52.8, 58.2, 82.5, 85.2. 2) Smallest 2.58, largest 85.2. 3) 5.28: it is only 0.28 away from 5. 5.82 is 0.82 away and 2.85 is 2.15 away. Ask: "Why is a number with 2 decimal places always smaller than one with 1 decimal place here?" (it has only one digit in front of the point).'))

# ---------- 6. teach: zoom in on a number line ----------
k=(1500-100)/10
g=nline(100,1500,110,10,{0:'2',10:'3'},big=(5,),band=(3,4))
g+=f'<path d="M{100+3*k} 200 L100 300 M{100+4*k} 200 L1500 300" stroke="{TEAL}" stroke-width="4" stroke-dasharray="12 8" fill="none"/>'
g+=txt(100+3*k,184,'2.3',30,TEAL)+txt(100+4*k,184,'2.4',30,TEAL)
g2=nline(100,1500,380,10,{0:'2.3',10:'2.4'},arrows=[(6,'?')],big=(5,))
body=h2('Zoom in: what is one step worth?')
body+=pin(128,230,1664,svgwrap(1600,480,'A number line from 2 to 3 in tenths. The part from 2.3 to 2.4 is zoomed in and cut into 10 smaller steps. An arrow points to the 6th small step.',g+g2),None)
body+=step(1,'Top line: 2 to 3 in 10 steps, so one step is 0.1.',top=700,width=1240,size=34)
body+=step(2,'Zoom in: 2.3 to 2.4 in 10 steps, so one step is 0.01.',top=790,width=1240,size=34)
body+=pin(1420,700,372,p('6 steps past 2.3:  2.36',40,800),'pop',YEL,20,'18px 26px')
put('teach1',sec(f'{P}-teach1','18–20 MIN',body,'Teach. Start with the top line: "How many steps from 2 to 3? Ten. So each step is one tenth, 0.1." Point along: 2.1, 2.2, 2.3. Then the zoom: "The gap from 2.3 to 2.4 is cut into ten tiny steps. Each one is a tenth of a tenth: one hundredth, 0.01." Click step 1, step 2, then the answer. Think-aloud: "The arrow is 6 tiny steps past 2.3. So it is 2.3 and 6 hundredths: 2.36." Ask: "Can we zoom in again, between 2.36 and 2.37?" (yes: 10 steps of 0.001; halfway is 2.365). Use a metre ruler too: 1 m = 100 cm, so 2.36 m is 2 m 36 cm.'))

# ---------- 7. worked example 1: order ----------
W=[190,120,140,200,220]
body=h2('Worked example: line up the points')+card(p('Order from smallest:  4.307,  4.37,  4.073,  4.3',40,700))
body+=trow(128,370,['Number','Ones','Tenths','Hundredths','Thousandths'],W,None,True,30)
rows=[['4.307','4','3','0','7'],['4.37','4','3','7','0'],['4.073','4','0','7','3'],['4.3','4','3','0','0']]
for i,r in enumerate(rows): body+=trow(128,450+i*84,r,W,'rise',size=34)
body+=pin(1230,370,518,p('1. Same ones: 4.',32,700),'fade',WHITE,20,'16px 22px')
body+=pin(1230,460,518,p('2. Tenths: 4.073 has 0 tenths, so it is the smallest.',32,700),'fade',WHITE,20,'16px 22px')
body+=pin(1230,610,518,p('3. 4.3 = 4.300. Then compare hundredths and thousandths.',32,700),'fade',WHITE,20,'16px 22px')
body+=answer(128,800,1664,'4.073,  4.3,  4.307,  4.37')
put('we1',sec(f'{P}-we1','20–22 MIN',body,'Line up the points: today\'s main idea. Click to fill each row of the place-value chart; children say the digits first. Point out the 0s in grey places: "4.37 has no thousandths. I can write a 0 there: 4.370. It is the same number." Then the side notes. Think-aloud: "All have 4 ones. Tenths: 3, 3, 0, 3. The 0 tenths is smallest: 4.073. Now 4.300, 4.307, 4.370. Hundredths: 0, 0, 7. So 4.37 is the biggest. 4.300 and 4.307: thousandths 0 and 7, so 4.3 comes first." Common mistake: "4.307 has more digits so it is bigger." Show 4.307 and 4.37 on a zoom number line if needed.'))
put('try1',try_slide(f'{P}-try1','22–23 MIN • OPTIONAL','Your turn: whiteboards','Line up the points. Fill empty places with 0.',[('a','Which is bigger: 0.6 or 0.58?','0.6'),('b','Smallest first: 2.15, 2.5, 2.105','2.105, 2.15, 2.5'),('c','Halfway between 3.4 and 3.5?','3.45')],'Whiteboards up together, then click. a) 0.60 and 0.58: 6 tenths beats 5 tenths. b) 2.150, 2.500, 2.105: tenths 1, 5, 1, so 2.5 is biggest; then hundredths 5 and 0, so 2.105 is smallest. c) Zoom in: 3.4 to 3.5 in hundredths is 3.40 to 3.50; halfway is 3.45. Ask: "Halfway between 3.45 and 3.46?" (3.455).',size=36))

# ---------- 9. worked example 2: rounding ----------
g=nline(100,1500,150,10,{0:'6.4',5:'6.45',10:'6.5'},arrows=[(7,'6.47')],big=(5,))
body=h2('Rounding: find the neighbours')+card(p('Round 6.47 to 1 decimal place. Then to the nearest whole number.',40,700))
body+=pin(128,360,1664,svgwrap(1600,250,'A number line from 6.4 to 6.5 in hundredths with the halfway mark 6.45 and an arrow at 6.47',g),None)
body+=step(1,'1 decimal place: the neighbours are 6.4 and 6.5. Halfway is 6.45.',top=620,size=34)
body+=step(2,'6.47 is past halfway, so it rounds UP to 6.5.',top=715,size=34)
body+=step(3,'Nearest whole number: neighbours 6 and 7, halfway 6.5. 6.47 is below it: 6.',top=810,size=34)
put('we2',sec(f'{P}-we2','23–26 MIN',body,'Click through the steps. Think-aloud: "Rounding to 1 decimal place means: which tenth is it nearest to? 6.47 is between 6.4 and 6.5. The halfway mark is 6.45. 6.47 is past it, so 6.5." Then the whole number: "Which whole numbers is it between? 6 and 7. Halfway is 6.5, and 6.47 has not reached it, so it rounds to 6." Rule we use: exactly halfway rounds UP (6.45 rounds to 6.5). Ask: "Why does 6.47 round up one time and down the other?" (we are looking for different neighbours).'))

# ---------- 10. worked example 3: rounding backwards ----------
g=nline(100,1500,150,20,{0:'3.7',10:'3.8',20:'3.9'},big=(5,15),band=(5,14.6))
g+=txt(100+5*70,236,'3.75',32,TEAL)+txt(100+15*70,236,'3.85',32,RED)
body=h2('Rounding backwards: the detective question')+card(p('A number has 2 decimal places. Rounded to 1 decimal place, it is 3.8. What is the smallest it can be? The largest?',38,700))
body+=pin(128,380,1664,svgwrap(1600,250,'A number line from 3.7 to 3.9 in hundredths. The part from 3.75 up to just before 3.85 is shaded.',g),'fade')
body+=step(1,'Halfway marks: 3.75 and 3.85. The shaded numbers all round to 3.8.',top=640,size=34)
body+=step(2,'3.75 rounds UP to 3.8: it is the smallest.  3.85 rounds up to 3.9: not this one!',top=735,size=34)
body+=answer(128,830,1664,'Smallest 3.75,  largest 3.84')
put('we3',sec(f'{P}-we3','26–28 MIN',body,'This is the detective question: work backwards from the rounded number. Click to shade the band, then the steps. Ask before step 2: "Is 3.85 in or out?" Many children say in. Test it: 3.85 is exactly halfway, so it rounds UP to 3.9. So the largest with 2 decimal places is 3.84. Ask: "How many numbers with 2 decimal places round to 3.8?" (3.75 to 3.84: 10 numbers).'))
put('try2',try_slide(f'{P}-try2','28–29 MIN • OPTIONAL','Your turn: round it','Find the neighbours and the halfway mark.',[('a','Round 5.38 to 1 decimal place.','5.4'),('b','Round 12.96 to 1 decimal place.','13.0'),('c','2 decimal places, rounds to 9 (whole number). Smallest? Largest?','8.50, 9.49')],'Whiteboards. a) Neighbours 5.3 and 5.4, halfway 5.35; 5.38 is past it, so 5.4. b) Neighbours 12.9 and 13.0: write 13.0, not 13, to show 1 decimal place. c) Halfway marks 8.5 and 9.5. 8.50 rounds up to 9, so it is the smallest; 9.50 would round to 10, so the largest is 9.49.',size=34))

# ---------- 12. key ----------
body=h2('Key idea: line up the points')+card(p('Line up the decimal points and compare place by place: ones, tenths, hundredths, thousandths. More digits does not mean bigger.',44,700))+card(p('To round, find the two neighbours and the halfway mark. To round backwards, find the smallest and largest numbers that round to it.',38,600,MUTED))
put('key',sec(f'{P}-key','29–30 MIN',body,'Say the key idea together. Common mistakes to watch for during the worksheet: (1) Comparing decimals by the number of digits (3.405 > 3.45 because 405 > 45) instead of lining up the points. (2) Reading a number line by counting marks without first working out what one step is worth (0.1, 0.01 or 0.001). (3) Rounding backwards: giving 7.45 as the largest number that rounds to 7.4 (it rounds to 7.5), or forgetting 7.35 to 7.39, which are below 7.4.'))
put('break',break_slide(f'{P}-break','30–34 MIN','Decimal stand-up. I call a decimal. More than 0.5: stand tall. Less than 0.5: crouch. Exactly 0.5: freeze like a statue!','Four minutes. Call: 0.7, 0.45, 0.50, 0.09, 0.6, 0.555, 0.499, 0.5. Watch 0.45 (crouch, many stand) and 0.50 (freeze). Online: children stand and crouch in view of the camera.'))

# ---------- worksheet page 1 ----------
put('ws1',ws_preview(f'{P}-ws1','34–50 MIN','Worksheet page 1: with your partner',[('Q1','Zoom-in number lines. What is one small step worth?'),('Q2','Order and compare. Line up the points.'),('Q3','The rounding detective. Use the number line: the smallest and the largest number that round to 7.4.')],'Stuck? Write the numbers in a place-value chart, or draw a zoom-in number line.','Minutes 34 to 50. Walk around. Ask "What is one step worth?" and "Which place do you compare first?" before giving any help. Q3 is part (a) only: the number line from 7.30 to 7.50 shows the halfway marks. How many numbers and the digit clue are in the question bank.'))
put('ws1ans',checks(f'{P}-ws1ans','50–53 MIN','Page 1: check together',[('Q1','A 6.3,  B 6.85,  C 4.53,  D 4.58,  E 0.247.   f) B'),('Q2','a) 3.045, 3.054, 3.405, 3.45, 3.5   b) No: 3.405 < 3.450'),('Q3','a) Smallest 7.35, largest 7.44')],
 'Click each answer after a pair explains theirs. Q1: line a steps are 0.1 (B is halfway between 6.8 and 6.9, so 6.85); line b steps are 0.01; line c steps are 0.001, so E is 0.247. f) only 6.85 rounds to 7. Q2b: line up the points: 3.405 and 3.450 have the same ones and tenths, but 0 hundredths is less than 5 hundredths. Q3: the halfway marks are 7.35 and 7.45; 7.45 rounds up to 7.5, so the largest is 7.44. (Question bank: 7.35 to 7.44 is 10 numbers, and the digits-adding-to-18 clue gives 7.38.)',gapy=170))

# ---------- teach: closest to a target (Q4) ----------
g=dcards(['1','4','8','.'],20,20,96,124,22)
body=h2('Closest to a target: check both sides')+pin(128,240,520,svgwrap(520,170,'Digit cards 1, 4, 8 and a decimal point',g),None)
body+=pin(700,250,1092,p('Use 1, 4, 8 and the point once each. Which number is closest to 3?',38,700),None,WHITE,20,'24px 30px')
body+=step(1,'There is no 3 card. Just below 3: start with 1, make the rest big: 1.84',top=460,size=34)
body+=step(2,'Just above 3: start with 4, make the rest small: 4.18',top=560,size=34)
body+=step(3,'How far?  3 − 1.84 = 1.16.   4.18 − 3 = 1.18.',top=660,size=34)
body+=answer(128,770,1664,'1.84 is closest (by just 0.02!)')
put('teachcards',sec(f'{P}-teachcards','53–55 MIN',body,'Teach before worksheet page 2 (Q4 uses digit cards 3, 6, 9). Ask first: "Which do you think is closer to 3?" Most children pick one side without checking. Click through. Think-aloud: "Below 3 I want the biggest number that starts with a smaller digit: 1, then the biggest digits: 1.84. Above 3 I want the smallest number starting with a bigger digit: 4.18. Now I measure both distances." The lesson: always check both sides of the target.'))

# ---------- teach: bar model (Q5) ----------
x0=150; bw=400; ew=190
g=txt(x0-24,108,'Ravi',38,NAVY,'end')+bar(x0,60,bw,84,SKY,'?',40)+bar(x0+bw,60,ew,84,YEL,'$0.60',36)
g+=txt(x0-24,218,'Ben',38,NAVY,'end')+bar(x0,170,bw,84,SKY,'?',40)
xb=x0+bw+ew+30
g+=f'<path d="M{xb} 60 h16 V254 h-16" fill="none" stroke="{NAVY}" stroke-width="4"/>'+txt(xb+30,168,'$6.80',38,TEAL,'start')
body=h2('Bar model: take away the extra, then share')+card(p('Ravi and Ben have $6.80 altogether. Ravi has $0.60 more than Ben. How much does each boy have?',38,700))
body+=pin(128,400,1664,svgwrap(940,300,'Bar model: Ravi\'s bar is Ben\'s bar plus an extra $0.60. Both bars together are $6.80.',g),None)
body+=step(1,'Take away the extra:  $6.80 − $0.60 = $6.20',left=1110,top=400,width=682,size=32)
body+=step(2,'Two equal bars:  $6.20 ÷ 2 = $3.10  (Ben)',left=1110,top=530,width=682,size=32)
body+=step(3,'Ravi:  $3.10 + $0.60 = $3.70',left=1110,top=660,width=682,size=32)
body+=pin(128,780,1664,p('Check: $3.10 + $3.70 = $6.80, and $3.70 is $0.60 more than $3.10 ✓',36,700),'fade',SOFT,20,'18px 30px')
put('teachbar',sec(f'{P}-teachbar','55–58 MIN',body,'Teach before worksheet page 2 (Q5). Draw the two bars first: "Who has more? Whose bar is longer? By how much?" Think-aloud: "If I cut off Ravi\'s extra 60 cents, the two bars are the same. Together they are $6.80 minus $0.60, which is $6.20. Shared equally: $6.20 divided by 2. 6 divided by 2 is 3, 20 cents divided by 2 is 10 cents: $3.10." Show the division as 6.20 ÷ 2 = 3.10 too. Always check BOTH clues at the end.'))

# ---------- teach: mass with a container (Q6) ----------
def scale(cx,label,cups,cap):
    s=f'<rect x="{cx-170}" y="200" width="340" height="90" rx="16" fill="{SKY}" stroke="{NAVY}" stroke-width="4"/><rect x="{cx-100}" y="218" width="200" height="54" rx="8" fill="{WHITE}" stroke="{NAVY}" stroke-width="3"/>'+txt(cx,258,label,34)
    s+=f'<rect x="{cx-190}" y="178" width="380" height="18" rx="6" fill="{NAVY}"/><rect x="{cx-160}" y="150" width="320" height="28" rx="6" fill="{YEL}" stroke="{NAVY}" stroke-width="4"/>'
    for i in range(cups): s+=f'<path d="M{cx-150+i*62} 90 h50 l-7 60 h-36 z" fill="{WHITE}" stroke="{NAVY}" stroke-width="4"/>'
    return s+txt(cx,40,cap,32,TEAL)
g=scale(260,'2.3 kg',5,'tray with 5 cups')+scale(760,'0.55 kg',0,'empty tray')
body=h2('Mass puzzles: take away the container')+pin(128,230,1000,svgwrap(1000,300,'A tray with 5 cups on a scale reads 2.3 kg. The empty tray reads 0.55 kg.',g),None)
body+=pin(1180,240,612,p('The 5 cups all have the same mass. What is the mass of one cup?',36,700),None,WHITE,20,'24px 28px')
body+=step(1,'The cups alone:  2.3 kg − 0.55 kg = 1.75 kg   (write 2.30 − 0.55)',top=560,size=34)
body+=step(2,'One cup:  1.75 kg ÷ 5 = 0.35 kg',top=660,size=34)
body+=pin(128,770,1664,p('Check: 5 × 0.35 = 1.75, and 1.75 + 0.55 = 2.3 ✓',36,700),'fade',SOFT,20,'18px 30px')
put('teachmass',sec(f'{P}-teachmass','ON DEMAND • Q6',body,'ON DEMAND: show this during page 2 (screen share or whiteboard) when a child chooses Q6, a choice question; the page already sets out Step 1 and Step 2. Only two ideas are taught before page 2 (closest to a target, and the bar model). Ask: "Why can\'t we just divide 2.3 by 5?" (the tray is on the scale too). Think-aloud: "First I take the tray away: 2.30 minus 0.55. I line up the points and write 2.3 as 2.30. That is 1.75 kg for 5 cups. Then 1.75 divided by 5: 175 hundredths divided by 5 is 35 hundredths, 0.35 kg." Q6b on the worksheet takes cans OUT: ask "How much mass leaves the scale?"'))

# ---------- teach: mystery decimal (Q7) ----------
body=h2('Mystery decimal: list the cases, check every clue')+card(p('I have 2 decimal places. Rounded to 1 decimal place, I am 3.2. My hundredths digit is 6 more than my tenths digit.',38,700))
body+=step(1,'Rounds to 3.2, so I am from 3.15 to 3.24. My tenths digit is 1 or 2.',top=420,size=34)
body+=step(2,'Tenths 1: hundredths 1 + 6 = 7.  3.17 is from 3.15 to 3.24 ✓',top=520,size=34)
body+=step(3,'Tenths 2: hundredths 2 + 6 = 8.  3.28 rounds to 3.3: not this one!',top=620,size=34)
body+=answer(128,730,1664,'I am 3.17. Only one number fits every clue.')
put('teachclue',sec(f'{P}-teachclue','ON DEMAND • Think harder Q4',body,'ON DEMAND (Think harder Q4, not part of the teaching before page 2): show it only if a child chooses that question (the mystery decimal with 3 places). Strategy: use the rounding clue to make a short list, then test every case against every clue. Ask after step 1: "Why only tenths 1 or 2?" (3.15 to 3.19 have tenths 1; 3.20 to 3.24 have tenths 2). Stress step 3: the case that breaks a clue must be crossed out out loud, so children see why the answer is the only one.'))

# ---------- worksheet page 2 ----------
put('ws2',ws_preview(f'{P}-ws2','58–76 MIN','Worksheet page 2: on your own',[('Q4','Digit cards 3, 6, 9: put the point after the first digit. List the 6 numbers, then find the one nearest 7.'),('Q5','Mei and Siti. Draw the bars: take away the extra, then share.'),('Q6','The box of cans. Take away the box first.')],'Done? Think harder and Go further come next.','Children work alone. Note who needs a short catch-up next lesson, especially children who still compare decimals by their number of digits.'))
put('ws2ans',checks(f'{P}-ws2ans','76–80 MIN','Page 2: check together',[('Q4','a) 3.69, 3.96, 6.39, 6.93, 9.36, 9.63   b) 9.63   c) 6.93   d) 3.69 and 3.96'),('Q5','Siti $4.10,  Mei $5.30'),('Q6','a) 0.4 kg   b) 2.05 kg')],
 'Click after a child explains. Q4a: the decimal point goes after the first digit, so there are 6 numbers: 3.69, 3.96, 6.39, 6.93, 9.36, 9.63. Q4c: below 7 the best is 6.93 (0.07 away); above 7 it is 9.36 (2.36 away). Q4d: 3.69 and 3.96 both round to 4 (3.5 to 4.5). Q5: $9.40 − $1.20 = $8.20, $8.20 ÷ 2 = $4.10 for Siti, $4.10 + $1.20 = $5.30 for Mei. Q6: 2.85 − 0.45 = 2.40 kg for 6 cans, 2.40 ÷ 6 = 0.4 kg; 2 cans are 0.8 kg, 2.85 − 0.8 = 2.05 kg. (The mystery decimal 4.687 is Think Harder Q4: it rounds to 4.7, so 4.650 to 4.749; tenths 6 gives hundredths 8, tenths 7 gives hundredths 9, which is too big; 4 + 6 + 8 = 18, so the thousandths digit is 7.)',gapy=150))

# ---------- stretch / challenge ----------
st=[('1.','Siti buys 4 notebooks that cost the same. She pays with a $10 note and gets $2.60 change. How much is one notebook?'),('2.','Find ALL the digits that the letter A can be:  3.A5 < 3.42'),('3.','Mei is 1.38 m tall. Ben is 0.15 m taller than Mei. Ali is 0.09 m shorter than Ben. How tall is Ali?')]
put('stretch',sec(f'{P}-stretch','Early finishers / take-home',h2('Stretch')+numcards(st,36),'Answers: 1) $1.85 ($10 − $2.60 = $7.40, $7.40 ÷ 4 = $1.85). 2) 0, 1, 2 and 3 (3.35 < 3.42 but 3.45 > 3.42). 3) 1.44 m (Ben 1.38 + 0.15 = 1.53 m, Ali 1.53 − 0.09 = 1.44 m).'))
ch=[('1.','A number with 3 decimal places rounds to 2.46 (to 2 decimal places). Its digits add up to 20. What is the number?'),('2.','3 apples and 1 pear weigh 0.95 kg. 1 apple and 1 pear weigh 0.45 kg. All the apples weigh the same. What is the mass of the pear?')]
put('challenge',sec(f'{P}-challenge','Early finishers / take-home',h2('Challenge')+numcards(ch,36),'Pairs try first, then use the "see it" slide if stuck, then the walk-through. Answers: 1) 2.459 (it is from 2.455 to 2.464; 2 + 4 + 5 + 9 = 20; 2.46_ would need an 8, but 2.468 rounds to 2.47). 2) 0.2 kg (the extra 2 apples weigh 0.95 − 0.45 = 0.5 kg, so 1 apple is 0.25 kg and the pear is 0.45 − 0.25 = 0.2 kg). More are in the question bank and on the Think Harder pages.'))
g1=nline(60,700,190,20,{0:'2.45',10:'2.46',20:'2.47'},big=(5,15),band=(5,14.6),lab=28,ticksize=14)
g1+=f'<rect x="60" y="300" width="640" height="80" rx="14" fill="{SOFT}" stroke="{NAVY}" stroke-width="3"/>'+txt(380,352,'digits add up to 20',34)
g1+=txt(380,60,'2 . ? ? ?',52)
uw=150
g2=txt(30,50,'3 apples + 1 pear',32,NAVY,'start')
for i in range(3): g2+=bar(30+i*uw,125,uw,72,'#F2A7A7','apple',28)
g2+=bar(30+3*uw,125,110,72,'#BFE3DC','pear',28)+brace(30,30+3*uw+110,125,'0.95 kg',32)
g2+=txt(30,262,'1 apple + 1 pear',32,NAVY,'start')+bar(30,280,uw,72,'#F2A7A7','apple',28)+bar(30+uw,280,110,72,'#BFE3DC','pear',28)
g2+=brace(30,30+uw+110,352,'0.45 kg',32,up=False)
body=h2('Challenge: see it',60)+'<div style="display:flex;gap:32px;align-items:flex-start">'
body+=card(f'<p style="font-size:30px;font-weight:700;color:{TEAL}">Q1: Which numbers round to 2.46?</p>'+svgwrap(760,420,'A number line from 2.45 to 2.47 in thousandths with a shaded band around 2.46, and the clue digits add up to 20',g1,'width:100%;height:auto;display:block'),extra='flex:1;min-width:0;padding:20px 24px')
body+=card(f'<p style="font-size:30px;font-weight:700;color:{TEAL}">Q2: Compare the two bars</p>'+svgwrap(760,420,'Bar model: 3 apples and 1 pear make 0.95 kg; 1 apple and 1 pear make 0.45 kg',g2,'width:100%;height:auto;display:block'),extra='flex:1;min-width:0;padding:20px 24px')+'</div>'
put('chdiag',sec(f'{P}-chdiag','Early finishers / take-home',body,'Show after pairs have tried the Challenge, or if they are stuck. The pictures show the problem, not the answer. Ask: Q1, where do the numbers that round to 2.46 start and stop? Which tenths and hundredths digits can they have? Q2, what is the same in both bars? What is different? Answers are in the Challenge slide notes.'))
body=h2('Challenge: walk-through')+pin(128,250,800,p('Q1: list the cases',38,800,TEAL))
for i,t in enumerate(['Rounds to 2.46: from 2.455 to 2.464','2.45_:  2 + 4 + 5 + ? = 20, so ? = 9 → 2.459 ✓','2.46_:  2 + 4 + 6 + ? = 20, so ? = 8 → 2.468 rounds to 2.47: not this one','Answer: 2.459']): body+=pin(128,330+i*125,800,p(t,31),'rise',WHITE)
body+=pin(992,250,800,p('Q2: compare the bars',38,800,TEAL))
for i,t in enumerate(['The difference is 2 apples: 0.95 − 0.45 = 0.5 kg','1 apple: 0.5 ÷ 2 = 0.25 kg','Pear: 0.45 − 0.25 = 0.2 kg','Check: 0.25 × 3 + 0.2 = 0.95 ✓']): body+=pin(992,330+i*125,800,p(t,31),'rise',WHITE)
put('chwalk',sec(f'{P}-chwalk','Early finishers / take-home',body,'Use after pairs have tried. Q1: the rounding clue makes a short list (only 10 numbers), so we test cases instead of guessing. The second case is the trap: 2.468 has the right digit total but rounds to 2.47. Q2: lining up the two bars shows the extra 2 apples; this "compare and take away" idea is the same as the bar models on page 2.'))

# ---------- talk / exit ----------
body=h2('Talk time')+card(chip('TALK TIME',YEL,NAVY)+p('Ben says 3.405 is bigger than 3.45 because 405 is bigger than 45. Who agrees? How can we check?',42,600))+card(p('Sentence starters:',34,400,MUTED)+p('“I noticed that …”   “I tested it by …”   “I know because …”',38,600))
put('talk',sec(f'{P}-talk','80–85 MIN',body,'Minutes 80 to 85. Pairs talk for 2 minutes, then share. Answer: Ben is wrong. Line up the points: 3.405 and 3.450. Same ones, same tenths; 0 hundredths is less than 5 hundredths, so 3.405 is smaller. A number line check: 3.405 is just past 3.40; 3.45 is halfway to 3.5. Second question if time: "Why does 3.45 = 3.450, but 3.45 is not the same as 3.045?" (a 0 at the end adds nothing; a 0 after the point moves the other digits to smaller places). Praise the reasons, not only the answers.'))
body=h2('Exit ticket')+card(chip('EXIT TICKET')+p('Write 2.8, 2.08 and 2.088 in order, smallest first. Then round 2.088 to 1 decimal place.',46,600))+card(p('Write your answer on a slip of paper. Show it to your tutor. Then collect your stamp in your inquiry journal.',34,400))
put('exit',sec(f'{P}-exit','85–88 MIN',body,'Minutes 85 to 88. Answer: 2.08, 2.088, 2.8 (as 2.080, 2.088, 2.800). 2.088 rounds to 2.1 (neighbours 2.0 and 2.1, halfway 2.05). Extension: use the digit cards 1, 3, 5, 7 and a decimal point to make the number with 2 decimal places that is closest to 40 (37.51).'))

# ---------- write ----------
# ---------- fix pass (rebuild/p4_fix.py): sneak-peek puzzles, looking back, neutral names, go further, minute labels ----------
import subprocess as _sp, p4_fix
_G=json.loads(_sp.check_output(['node','-e',"process.stdout.write(JSON.stringify(require('"+os.path.join(H,'..','p4','content','l5.js')+"').gaps))"]))
_ID='p4l5'
_PIC=globals().get('PIC')

order=[f'{P}-{x}' for x in ['title','warm1','warm2','explore1','explore2','teach1','we1','try1','we2','we3','try2','key','break','ws1','ws1ans','teachcards','teachbar','ws2','teachmass','teachclue','ws2ans','stretch','challenge','chdiag','chwalk','talk','exit']]
p4_fix.finish(S,5,_G,pic=_PIC)
order=p4_fix.order(order,5)
assert set(order)==set(S), set(order)^set(S)
sd=os.path.join(D,'slides')
for f in os.listdir(sd):
    if f.endswith('.html') and f[:-5] not in S: os.remove(os.path.join(sd,f))
for i,h in S.items(): open(os.path.join(sd,i+'.html'),'w').write(h)
deck={'v':4,'createdOnFiles':{'v':1,'at':datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')},'lists':'css',
 'title':'Math Inquirers Level 4: Lesson 5 – Decimal Detectives','order':order,'cover':f'{P}-title',
 'sections':{'s1':{'description':'Warm-up and explore','start':f'{P}-title'},'s2':{'description':'Teach: zoom in, line up the points, round and round backwards','start':f'{P}-teach1'},'s3':{'description':'Worksheet with teaching before page 2','start':f'{P}-break'},'s4':{'description':'Stretch, challenge, talk and exit','start':f'{P}-stretch'}},
 'faces':{'fredoka':{'family':'Fredoka','href':'https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&display=swap'},'nunito-sans':{'family':'Nunito Sans','href':'https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@400;600;700&display=swap'}},
 'designSystems':[]}
json.dump(deck,open(os.path.join(D,'deck.json'),'w'),indent=1,ensure_ascii=False)
print(len(order),'slides')
