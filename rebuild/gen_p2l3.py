"""Math Inquirers P2, Lesson 3: Legs, Wheels and Arrays. Writes split/p2l3/project (deck.json + slides/*.html)."""
import json,os,sys,shutil,datetime
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,H)
import slidekit
slidekit.FOOT='Math Inquirers P2 Holiday Program  •  Notice it. Test it. Explain why.'
from slidekit import *
RED='#D64545'
D=os.path.join(H,'..','split','p2l3','project'); S={}; ORDER=[]
def put(i,h): S[i]=h; ORDER.append(i)

# ---------- generic slides ----------
def title_slide(sid,label,title,topic,today,notes):
    return (f'<section id="{sid}" data-transition="fade" style="background:{NAVY};color:{CREAM};font-family:{BF};padding:128px 128px 160px;display:flex;flex-direction:column;justify-content:center;gap:36px">\n'
            f'<p style="font-size:32px;font-weight:700;letter-spacing:4px;color:{YEL}">{E(label)}</p>\n'
            f'<h1 style="font-family:{HF};font-size:120px;font-weight:600;line-height:1.05">{E(title)}</h1>\n'
            f'<p style="font-size:44px;color:#C9D4EC">{E(topic)}</p>\n'
            f'<div style="background:#26385F;border-radius:24px;padding:40px;display:flex;flex-direction:column;gap:12px"><p style="font-size:28px;font-weight:700;letter-spacing:3px;color:{YEL}">TODAY WE WILL</p><p style="font-size:44px;font-weight:600">{E(today)}</p></div>\n'
            f'<p style="position:absolute;left:128px;bottom:64px;width:1400px;font-size:24px;color:#B7C3DD">{E(slidekit.FOOT)}</p>\n<aside>{E(notes)}</aside>\n</section>\n')
def break_slide(sid,time,head,text,sub,notes):
    return (f'<section id="{sid}" data-transition="fade" style="background:{TEAL};color:{CREAM};font-family:{BF};padding:128px 128px 160px;display:flex;flex-direction:column;justify-content:center;gap:36px">\n'
            f'<p style="font-size:32px;font-weight:700;letter-spacing:4px;color:{YEL}">{E(time)}</p>\n'
            f'<h2 style="font-family:{HF};font-size:110px;font-weight:600;line-height:1.05">{E(head)}</h2>\n'
            f'<p style="font-size:48px;font-weight:600;line-height:1.3">{E(text)}</p>\n<p style="font-size:36px;color:#D7EFEA">{E(sub)}</p>\n'
            f'<p style="position:absolute;left:128px;bottom:64px;width:1400px;font-size:24px;color:#D7EFEA">{E(slidekit.FOOT)}</p>\n<aside>{E(notes)}</aside>\n</section>\n')
def explore1(sid,time,steps,pic,notes,picw=760):
    lst=''.join(f'<li>{E(s)}</li>' for s in steps)
    left=card(chip('EXPLORE')+f'<ol style="margin:0;font-size:36px;font-weight:600;padding-left:48px;display:flex;flex-direction:column;gap:16px;line-height:1.3">{lst}</ol>',extra='flex:1;min-width:0')
    right=card(pic,extra=f'width:{picw}px;flex:none;align-items:center;justify-content:center;padding:20px')
    return sec(sid,time,h2('Explore: what to do')+f'<div style="display:flex;gap:32px;align-items:stretch">{left}{right}</div>',notes)
def numbered_cards(items,size=40):
    return ''.join(card(p(f'<span style="color:{TEAL}">{a}</span>  {E(b)}',size,600,raw=True)) for a,b in items)
def talk_slide(sid,time,q,notes):
    body=h2('Talk time')+card(chip('TALK TIME',YEL,NAVY)+p(q,42))+card(p('Sentence starters:',34,400,MUTED)+p('“I noticed that …”   “I tested it by …”   “I know because …”',38))
    return sec(sid,time,body,notes)
def exit_slide(sid,time,q,notes):
    body=h2('Exit ticket')+card(chip('EXIT TICKET')+p(q,46))+card(p('Write your answer on a slip of paper. Show it to your tutor. Then collect your stamp in your inquiry journal.',34,400))
    return sec(sid,time,body,notes)
def svgwrap(label,vw,vh,inner,w=None,h=None,extra=''):
    w=w or vw; h=h or vh
    return f'<svg aria-label="{E(label)}" viewBox="0 0 {vw} {vh}" xmlns="http://www.w3.org/2000/svg" style="width:{w}px;height:{h}px;flex:none;{extra}">{inner}</svg>'
def T(x,y,s,size=30,fill=NAVY,w=700,anchor='middle',font='Fredoka, Arial'):
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{w}" text-anchor="{anchor}" fill="{fill}" font-family="{font}">{E(s)}</text>'

# ---------- icons (drawn in a 160 x 160 box) ----------
def g_car():
    return (f'<path d="M14 104 L14 84 Q16 74 28 72 L50 70 L66 46 Q70 42 78 42 L112 42 Q120 42 124 48 L138 70 L146 72 Q154 74 154 86 L154 104 Z" fill="{RED}" stroke="{NAVY}" stroke-width="4" stroke-linejoin="round"/>'
            f'<path d="M72 50 L84 50 L84 70 L60 70 Z M92 50 L110 50 L124 70 L92 70 Z" fill="{SKY}" stroke="{NAVY}" stroke-width="3"/>'
            f'<circle cx="44" cy="108" r="17" fill="{NAVY}"/><circle cx="44" cy="108" r="7" fill="{GREY}"/><circle cx="124" cy="108" r="17" fill="{NAVY}"/><circle cx="124" cy="108" r="7" fill="{GREY}"/>')
def _wheel(x,y,r): return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{WHITE}" stroke="{NAVY}" stroke-width="5"/><circle cx="{x}" cy="{y}" r="5" fill="{NAVY}"/>'
def g_bike():
    return (_wheel(38,108,30)+_wheel(122,108,30)+f'<path d="M38 108 L66 64 L110 64 L122 108 M66 64 L80 108 L38 108 M110 64 L104 44 M94 44 L116 44" fill="none" stroke="{TEAL}" stroke-width="7" stroke-linejoin="round" stroke-linecap="round"/><rect x="56" y="52" width="24" height="9" rx="4" fill="{NAVY}"/>')
def g_trike():
    return (_wheel(118,104,34)+_wheel(30,122,18)+_wheel(58,122,18)+f'<path d="M44 122 L94 76 L118 104 M94 76 L88 48 M76 48 L100 48 M44 122 L118 122" fill="none" stroke="{RED}" stroke-width="7" stroke-linejoin="round" stroke-linecap="round"/><rect x="56" y="80" width="26" height="9" rx="4" fill="{NAVY}"/>')
def g_hen():
    return (f'<path d="M30 70 L14 46 L40 62 Z" fill="{YEL}" stroke="{NAVY}" stroke-width="3" stroke-linejoin="round"/>'
            f'<ellipse cx="74" cy="86" rx="46" ry="34" fill="{WHITE}" stroke="{NAVY}" stroke-width="4"/>'
            f'<circle cx="112" cy="54" r="20" fill="{WHITE}" stroke="{NAVY}" stroke-width="4"/>'
            f'<path d="M100 36 Q104 22 110 34 Q114 20 120 34" fill="{RED}" stroke="{NAVY}" stroke-width="3"/>'
            f'<polygon points="130,52 146,58 130,64" fill="{YEL}" stroke="{NAVY}" stroke-width="3" stroke-linejoin="round"/><circle cx="116" cy="50" r="3.5" fill="{NAVY}"/>'
            f'<path d="M64 116 L60 146 M84 116 L88 146 M50 146 L70 146 M78 146 L98 146" stroke="#E08A00" stroke-width="5" stroke-linecap="round" fill="none"/>')
def g_goat():
    return (f'<rect x="22" y="58" width="96" height="48" rx="22" fill="{GREY}" stroke="{NAVY}" stroke-width="4"/>'
            f'<path d="M34 104 L34 146 M54 104 L54 146 M88 104 L88 146 M106 104 L106 146" stroke="{NAVY}" stroke-width="6" stroke-linecap="round"/>'
            f'<path d="M110 66 L124 30 Q132 22 142 30 L150 54 Q146 62 136 62 Z" fill="{GREY}" stroke="{NAVY}" stroke-width="4" stroke-linejoin="round"/>'
            f'<path d="M126 30 Q118 8 104 14 M136 26 Q132 6 120 8" stroke="{NAVY}" stroke-width="4" fill="none" stroke-linecap="round"/>'
            f'<path d="M142 60 L146 76 L138 66" fill="{NAVY}"/><circle cx="136" cy="40" r="3.5" fill="{NAVY}"/><path d="M22 70 L10 56" stroke="{NAVY}" stroke-width="5" stroke-linecap="round"/>')
def g_dog():
    return (f'<ellipse cx="72" cy="84" rx="48" ry="26" fill="{YEL}" stroke="{NAVY}" stroke-width="4"/>'
            f'<path d="M36 104 L34 142 M56 106 L56 142 M92 106 L92 142 M110 100 L112 142" stroke="{NAVY}" stroke-width="7" stroke-linecap="round"/>'
            f'<circle cx="124" cy="58" r="24" fill="{YEL}" stroke="{NAVY}" stroke-width="4"/><path d="M112 40 Q100 52 108 70" fill="#C98A1A" stroke="{NAVY}" stroke-width="3"/>'
            f'<circle cx="130" cy="54" r="3.5" fill="{NAVY}"/><circle cx="146" cy="62" r="5" fill="{NAVY}"/><path d="M26 76 Q8 60 16 44" stroke="{NAVY}" stroke-width="6" fill="none" stroke-linecap="round"/>')
def icon(g,size=170,label='picture'): return f'<svg aria-label="{E(label)}" viewBox="0 0 160 160" xmlns="http://www.w3.org/2000/svg" style="width:{size}px;height:{size}px;flex:none">{g}</svg>'
def place(g,x,y,s=1): return f'<g transform="translate({x},{y}) scale({s})">{g}</g>'

# ---------- 1. title ----------
put('p2l3-title',title_slide('p2l3-title','P2  •  LESSON 3  •  WEEK 2','Legs, Wheels and Arrays','Multiplication and Division','Use arrays for × and ÷, find how many of each with a table, and share with leftovers.',
 'Objective: Read an array as rows of equal groups and write two multiplication and two division sentences for it; solve "how many of each" legs and wheels puzzles with a table; share with leftovers and decide what the leftover means; find all the arrays for a number. Tables used: 2, 3, 4, 5 and 10 only. '
 'Thinking strategies taught today: DRAW IT (arrays, plates, boats) and MAKE A TABLE (start with all of one kind, swap one at a time; guess and check). '
 'Materials: About 30 counters per pair, mini whiteboards, squared paper. Optional picture cards of hens and goats, bicycles and tricycles. '
 'Online: Each child has 30 small objects (buttons, beans or Lego bricks) and a whiteboard or paper; children hold arrays and tables up to the camera. '
 'Time plan: warm-up 0 to 10, explore 10 to 25, teaching 25 to 35 (click to reveal each step and answer), brain break 35 to 40, worksheet 40 to 70 with short teaching before each page and a check-together slide after it, talk time 70 to 80, exit ticket 80 to 90. Stretch and Challenge slides are for early finishers.'))

# ---------- 2. warm-up game ----------
cards=[([('car',g_car())],'4 cars','How many wheels?','16 wheels: 4, 8, 12, 16'),
       ([('bicycle',g_bike())],'5 bicycles','How many wheels?','10 wheels: 2, 4, 6, 8, 10'),
       ([('tricycle',g_trike())],'3 tricycles','How many wheels?','9 wheels: 3, 6, 9'),
       ([('dog',g_dog())],'5 dogs','How many legs?','20 legs: 4, 8, 12, 16, 20'),
       ([('hen',g_hen())],'6 hens','How many legs?','12 legs: 2, 4, 6, 8, 10, 12'),
       ([('car',g_car()),('bicycle',g_bike())],'2 cars and 1 bicycle','How many wheels?','10 wheels: 8 + 2')]
body=h2('Warm-up: count the legs and wheels')+p('Count in 2s, 3s, 4s or 5s. Not in 1s!',36,600,MUTED)
CW=533; cs=''; ans=''
for i,(ics,name,q,a) in enumerate(cards):
    L=128+(i%3)*(CW+32); Tp=290+(i//3)*300
    pics=''.join(icon(g,170 if len(ics)==1 else 96,lab) for lab,g in ics)
    picc=f'<div style="display:flex;flex-direction:column;gap:4px;width:170px;align-items:center">{pics}</div>'
    inner=(f'<div style="display:flex;align-items:flex-start;gap:16px">{picc}<div style="display:flex;flex-direction:column;gap:10px;padding-top:10px">'
           f'<p style="font-family:{HF};font-size:40px;font-weight:600;line-height:1.1">{E(name)}</p><p style="font-size:30px;font-weight:700;color:{TEAL}">{E(q)}</p></div></div>')
    cs+=pin(L,Tp,CW,inner,None,WHITE,24,'16px 22px',f'box-sizing:border-box;height:276px;border:4px solid {NAVY};box-shadow:8px 8px 0 {NAVY}')
    ans+=pin(L+20,Tp+196,CW-40,f'<p style="font-size:30px;font-weight:800;line-height:1.2">{E(a)}</p>','pop',SOFT,16,'12px 18px',f'box-sizing:border-box;border:3px solid {NAVY}')
put('p2l3-warm1',sec('p2l3-warm1','0–5 MIN',body+cs+ans,
 'Minutes 0 to 5. Legs and wheels count. Point to one card at a time. Children count in 2s, 3s, 4s or 5s (not in 1s) and show the number on fingers or a whiteboard, then you click to show the answer (clicks reveal the cards in order: cars, bicycles, tricycles, dogs, hens, mixed). '
 'Answers: 4 cars 16 wheels; 5 bicycles 10 wheels; 3 tricycles 9 wheels; 5 dogs 20 legs; 6 hens 12 legs; 2 cars and 1 bicycle 10 wheels (8 + 2). '
 'Ask: "Which times table did you use for the cars?" (4s). "For the tricycles?" (3s). For the last card: "Why can we not count all of them in 4s?" (the bicycle has only 2 wheels). '
 'Watch for children counting every wheel in 1s; ask them to point to each car and count "4, 8, 12, 16".'))

# ---------- 3. quick questions ----------
qs=[('1.','3 × 5 = ?','15'),('2.','4 groups of 4. How many altogether?','16'),('3.','20 ÷ 2 = ?','10'),('4.','30 shared equally by 10 children. How many each?','3'),('5.','How many 5s make 35?','7')]
body=h2('Quick questions')+''.join(qrow(128,250+i*125,1250,a,b) for i,(a,b,c) in enumerate(qs))+''.join(answer(1420,250+i*125,372,c) for i,(a,b,c) in enumerate(qs))
put('p2l3-warm2',sec('p2l3-warm2','5–10 MIN',body,'Minutes 5 to 10. Read each one aloud, give thinking time, take answers, then click to show. Answers: 15, 16, 10, 3, 7. For 5 ask: "How did you know?" (count in 5s: 5, 10, 15, 20, 25, 30, 35, that is 7 fives). For 4 ask: "Is that a multiplication or a division?" (division: sharing).'))

# ---------- 4. explore ----------
pen=(f'<rect x="20" y="96" width="680" height="300" rx="20" fill="#E8F3E0" stroke="{NAVY}" stroke-width="4"/>'
     +''.join(f'<rect x="{30+i*84}" y="80" width="16" height="56" rx="4" fill="#C98A1A" stroke="{NAVY}" stroke-width="3"/>' for i in range(9))
     +f'<line x1="30" y1="96" x2="700" y2="96" stroke="#C98A1A" stroke-width="8"/>'
     +place(g_hen(),70,150,1.1)+place(g_goat(),390,150,1.1)
     +T(160,384,'hen: 2 legs',30)+T(480,384,'goat: 4 legs',30)
     +f'<rect x="210" y="6" width="300" height="64" rx="12" fill="{YEL}" stroke="{NAVY}" stroke-width="4"/>'+T(360,50,'16 legs',38))
put('p2l3-explore1',explore1('p2l3-explore1','10–15 MIN',['A pen has only hens (2 legs) and goats (4 legs).','The farmer counts 16 legs altogether.','Use counters or drawings to find a mix of hens and goats.','Find EVERY mix. Record each one.'],
 svgwrap('A farm pen with a hen (2 legs) and a goat (4 legs) and a sign that says 16 legs',720,410,pen,700,400),
 'Minutes 10 to 15. Pairs use counters: 2 counters stand for a hen\'s legs, 4 for a goat\'s, or they draw circles for heads and sticks for legs. Ask for a prediction first: "Is there only one answer?" '
 'Do not show a method yet; let them try. Push early finishers: "How do you know you have them all?" Online: children draw on paper and hold it up. The 5 mixes are in the next slide\'s notes.'))
put('p2l3-explore2',sec('p2l3-explore2','15–25 MIN',h2('Explore: talk about it')+numbered_cards([('1.','How many different mixes did you find?'),('2.','How do you know you have them all?'),('3.','What happens when you swap 2 hens for 1 goat?')]),
 'Minutes 15 to 25. Gather the pairs and take answers. Write the mixes on the board IN ORDER of goats: 0 goats and 8 hens; 1 goat and 6 hens; 2 goats and 4 hens; 3 goats and 2 hens; 4 goats and 0 hens. That is 5 mixes (4 if the pen must have both kinds; accept either if the child says which). '
 'Answers: 1) 5 mixes. 2) The goats go 0, 1, 2, 3, 4; 5 goats would need 20 legs, too many. 3) The legs stay at 16: 2 hens have 4 legs, the same as 1 goat. Say: "Going in order made sure we did not miss one. Today we use tables to go in order."'))

# ---------- 5. teach arrays ----------
arr=''.join(f'<circle cx="{250+c*120}" cy="{190+r*120}" r="42" fill="{YEL}" stroke="{NAVY}" stroke-width="5"/>' for r in range(3) for c in range(4))
arr+=(f'<path d="M210 96 L210 80 L650 80 L650 96" fill="none" stroke="{TEAL}" stroke-width="5"/>'+T(430,56,'4 in each row',38,TEAL)
      +f'<path d="M168 150 L150 150 L150 470 L168 470" fill="none" stroke="{TEAL}" stroke-width="5"/>'+f'<text x="96" y="310" font-size="38" font-weight="700" text-anchor="middle" fill="{TEAL}" font-family="Fredoka, Arial" transform="rotate(-90 96 310)">3 rows</text>')
body=h2('Arrays: rows of equal groups')+pin(128,250,720,svgwrap('An array of 3 rows with 4 dots in each row',720,500,arr,720,500))
for i,t in enumerate(['Count the rows: 3. Count how many in each row: 4.','3 rows of 4:  4, 8, 12.   So 3 × 4 = 12.','Turn it round: 4 rows of 3.   4 × 3 = 12.','Share 12 into 3 rows: 12 ÷ 3 = 4.   Groups of 4: 12 ÷ 4 = 3.']):
    body+=step(i+1,t,left=900,top=250+i*150,width=892,size=34)
put('p2l3-teach1',sec('p2l3-teach1','25–27 MIN',body,'Teach. Build 3 rows of 4 counters while the children copy. Click to reveal each step. Think-aloud: "3 rows of 4 dots. I count the rows: 3. I count how many in each row: 4. 4, 8, 12. So 3 × 4 = 12. If I turn my head, it is 4 rows of 3, so 4 × 3 = 12 too. Sharing 12 into 3 rows gives 4 in each row: 12 ÷ 3 = 4. Putting 12 in groups of 4 gives 3 groups: 12 ÷ 4 = 3." '
 'Ask: "One array, how many number sentences?" (four: two × and two ÷). Say: "An array is a DRAW IT tool: it shows the groups so we can see the times table."'))
put('p2l3-try1',try_slide('p2l3-try1','27–28 MIN','Your turn: arrays','Draw dots if it helps. Then click to check.',[('a','2 rows of 10 chairs. How many chairs?','20'),('b','15 cakes in 3 equal rows. How many in each row?','5'),('c','40 dots in 4 equal rows. How many in each row?','10')],
 'Whiteboards up together, then click. a) 2 × 10 = 20. b) 15 ÷ 3 = 5 (count in 3s: 3, 6, 9, 12, 15, that is 5 threes, or 3 rows of 5). c) 40 ÷ 4 = 10. For c ask: "Which fact helped?" (4 × 10 = 40).',size=38))

# ---------- 6. worked example: hidden array ----------
tray=f'<rect x="10" y="10" width="700" height="460" rx="26" fill="{SKY}" stroke="{NAVY}" stroke-width="5"/>'
tray+=''.join(f'<circle cx="{130+c*115}" cy="{80+r*105}" r="38" fill="#E8B26A" stroke="{NAVY}" stroke-width="4"/><circle cx="{120+c*115}" cy="{72+r*105}" r="5" fill="{NAVY}"/><circle cx="{142+c*115}" cy="{90+r*105}" r="5" fill="{NAVY}"/>' for r in range(4) for c in range(5))
tray+=f'<rect x="188" y="130" width="500" height="320" rx="16" fill="{RED}" stroke="{NAVY}" stroke-width="5"/>'+''.join(f'<line x1="{188+i*62.5}" y1="130" x2="{188+i*62.5}" y2="450" stroke="#F2A7A7" stroke-width="5"/>' for i in range(1,8))+T(438,305,'cloth',44,WHITE)
body=h2('Worked example: under the cloth')+pin(128,240,1664,p('A tray of cookies has the same number in every row. How many are under the cloth?',36,700),None,WHITE,20,'18px 28px')
body+=pin(128,370,720,svgwrap('A tray of cookies, 4 rows of 5, with a cloth over all but the top row and the first cookie in each row',720,480,tray,600,400))
for i,t in enumerate(['The top row shows 5 in each row. The side shows 4 rows.','4 rows of 5:  5, 10, 15, 20.  20 cookies in all.','I can see 5 + 3 = 8 cookies.']):
    body+=step(i+1,t,left=780,top=370+i*130,width=1012,size=34)
body+=answer(780,770,1012,'Under the cloth: 20 − 8 = 12 cookies')
put('p2l3-we1',sec('p2l3-we1','28–30 MIN',body,'Click to reveal each step. Think-aloud: "Part of this tray is under a cloth. I do not need to see every cookie. The top row shows 5 in each row. The side shows 4 rows. 4 rows of 5 is 20. I can see 5 on top and 3 more down the side, that is 8. So 20 − 8 = 12 are hidden." '
 'Ask before step 3: "Did I count the corner cookie twice?" (No: 5 on top, then only the 3 BELOW it.) Common mistake: 5 + 4 = 9 seen, which counts the corner twice.'))

# ---------- 7. teach: how many of each (table) ----------
body=h2('How many of each? Make a table')+pin(128,240,1664,p('Bicycles (2 wheels) and cars (4 wheels). 6 vehicles and 16 wheels altogether. How many of each?',36,700),None,WHITE,20,'18px 28px')
W3=[220,170,360]
body+=trow(128,410,['Bicycles','Cars','Wheels'],W3,None,True)
for i,r in enumerate([['6','0','12  too few'],['5','1','14  too few'],['4','2','16  ✓']]): body+=trow(128,500+i*90,r,W3,'rise')
body+=pin(1100,410,692,p('Start with ALL bicycles:  6 × 2 = 12 wheels.',34,700),'fade',WHITE,20,'20px 26px')
body+=pin(1100,550,692,p('Swap 1 bicycle for a car: 2 more wheels each time.',34,700),'fade',WHITE,20,'20px 26px')
body+=pin(1100,690,692,p('4 bicycles and 2 cars.',38,800)+p('Check: 8 + 8 = 16 wheels, 4 + 2 = 6 ✓',30,600),'fade',SOFT,20,'20px 26px')
put('p2l3-teach2',sec('p2l3-teach2','30–32 MIN',body,'Teach. Click: the first note, then each table row, then the swap note and the answer (or reveal the rows as the children call them out). Think-aloud: "6 vehicles, bicycles and cars, 16 wheels. I start with all bicycles: 6 bicycles is 12 wheels. Too few. I swap one bicycle for a car: a car has 2 more wheels than a bicycle, so that adds 2 wheels, 14. Swap again: 16. So 4 bicycles and 2 cars. Check BOTH clues: 8 + 8 = 16 wheels, 4 + 2 = 6 vehicles." '
 'Say: "This is MAKE A TABLE. It is also guess and check, but tidy: every row is a guess, and the table shows us the pattern so we know which way to go."'))
put('p2l3-try2',try_slide('p2l3-try2','32–34 MIN','Your turn: how many of each?','Make a table. Start with all of one kind, then swap.',[('a','Hens and goats: 4 animals, 10 legs.','3 hens, 1 goat'),('b','Bicycles and tricycles: 5 of them, 12 wheels.','3 bikes, 2 trikes'),('c','Stools (3 legs) and chairs (4 legs): 3 seats, 10 legs.','2 stools, 1 chair')],
 'Whiteboards, then click. a) 4 hens = 8 legs; swap 1: 10 legs, so 3 hens and 1 goat. b) 5 bicycles = 10 wheels; each swap to a tricycle adds 1 wheel; 2 swaps make 12, so 3 bicycles and 2 tricycles. c) 3 stools = 9 legs; 1 swap adds 1 leg: 2 stools and 1 chair. Ask about b: "Why does each swap add only 1 this time?" (3 − 2 = 1).',size=36))
put('p2l3-key',sec('p2l3-key','34–35 MIN',h2('Key idea: draw it, then make a table')+card(p('An array is rows of equal groups: rows × number in each row. For "how many of each", start with all of one kind and swap one at a time in a table.',44,700))+card(p('Every swap changes the total by the same amount. Check both clues at the end.',38,600,MUTED)),
 'Say the key idea together. Common mistakes to watch for during the worksheet: (1) Counting the hidden part of an array one by one, or counting the corner twice, instead of rows × number in each row minus the ones you can see. (2) Giving the number of whole groups when the leftover still needs a place (28 children, vans of 5: writing 5 vans instead of 6). (3) In "how many of each" puzzles, matching the legs but forgetting to check the number of animals.'))
put('p2l3-break',break_slide('p2l3-break','35–40 MIN','Brain break','Array moves! "3 rows of 4": do 3 rows of 4 claps, counting 4, 8, 12. Then 5 rows of 2 jumps and 2 rows of 10 stomps.','Then: a drink of water and back to our seats.','Five minutes. Online: children stay in view of the camera and move in place. Count the totals aloud together: 12 claps, 10 jumps, 20 stomps.'))

# ---------- 8. worksheet page 1 ----------
put('p2l3-ws1',ws_preview('p2l3-ws1','40–52 MIN','Worksheet page 1: with your partner',[('Q1','An array of counters. Write two × and two ÷ sentences.'),('Q2','Cups under a cloth. Rows × number in each row, then take away.'),('Q3','Hens and goats. Fill in the table, then check both clues.')],'Build it with counters first, then write it down.','Minutes 40 to 52. Walk around. Ask "How do you know?" before giving any help. In Q3 check that pairs start with 7 hens and swap one at a time.'))
put('p2l3-ws1ans',check_slide('p2l3-ws1ans','52–54 MIN','Page 1: check together',[('Q1','4 × 5 = 20,  5 × 4 = 20.   20 ÷ 4 = 5,  20 ÷ 5 = 4'),('Q2','30 cups.  Under the cloth: 30 − 12 = 18'),('Q3','4 hens and 3 goats  (8 + 12 = 20 legs)')],
 'Click each answer after a pair explains. Q2: 3 rows of 10 is 30; we can see 10 on top and 2 more down the side, 12; 30 − 12 = 18. Q3 table: 7, 0, 14; 6, 1, 16; 5, 2, 18; 4, 3, 20. Each swap adds 2 legs. Check: 4 + 3 = 7 animals.'))

# ---------- 9. teaching before page 2 ----------
plates=''
for k in range(3):
    cx=130+k*230
    plates+=f'<ellipse cx="{cx}" cy="200" rx="100" ry="70" fill="{WHITE}" stroke="{NAVY}" stroke-width="5"/>'+''.join(f'<circle cx="{cx-56+j*28}" cy="{200+(12 if j%2 else -12)}" r="16" fill="{RED}" stroke="{NAVY}" stroke-width="3"/>' for j in range(5))+T(cx,310,f'child {k+1}: 5',30)
plates+=f'<circle cx="720" cy="188" r="16" fill="{RED}" stroke="{NAVY}" stroke-width="3"/><circle cx="756" cy="212" r="16" fill="{RED}" stroke="{NAVY}" stroke-width="3"/>'+T(738,310,'left: 2',30,TEAL)
body=h2('Sharing with leftovers')+pin(128,240,1664,p('Share 17 sweets equally among 3 children.',40,700),None,WHITE,20,'18px 28px')
body+=pin(128,370,820,svgwrap('Three plates with 5 sweets each and 2 sweets left over',820,340,plates,820,340),'fade')
for i,t in enumerate(['Give one each, round by round: 3, 6, 9, 12, 15.','5 rounds: each child gets 5. That uses 15.','17 − 15 = 2 left over.']):
    body+=step(i+1,t,left=1000,top=370+i*135,width=792,size=32)
body+=pin(128,780,1664,p('2 is less than 3, so there is not enough for another fair round.',34,700),'fade',SOFT,20,'18px 28px')
put('p2l3-teachshare',sec('p2l3-teachshare','54–56 MIN',body,'Teach before worksheet page 2 (Q4). Act it out with 17 counters and 3 paper plates: deal one to each plate per round, counting 3, 6, 9, 12, 15. Click: the plates, then each step, then the note. Think-aloud: "After 5 rounds each child has 5 and I have used 15. 2 are left. Can I do another round? No: I need 3 for a round." '
 'Ask: "Could the leftover ever be 3 or more when we share among 3?" (No: then we could do another round.)'))
boats=''
for k in range(4):
    x=20+k*410
    boats+=f'<path d="M{x} 70 L{x+360} 70 L{x+320} 140 L{x+40} 140 Z" fill="{SKY}" stroke="{NAVY}" stroke-width="5" stroke-linejoin="round"/>'
    n=4 if k<3 else 1
    boats+=''.join(f'<circle cx="{x+75+j*70}" cy="46" r="24" fill="{YEL}" stroke="{NAVY}" stroke-width="4"/>' for j in range(n))
body=h2('Leftovers still need a seat')+pin(128,240,1664,p('13 children go boating. Each boat holds 4 children. How many boats are needed?',38,700),None,WHITE,20,'18px 28px')
body+=pin(128,400,1664,svgwrap('Three boats with 4 children each and a fourth boat with 1 child',1664,160,boats,1664,160),'fade')
body+=step(1,'Count in 4s: 4, 8, 12. 3 boats carry 12 children.',top=600,size=36)
body+=step(2,'13 − 12 = 1 child is left. That child needs a boat too!',top=705,size=36)
body+=answer(128,810,1664,'4 boats are needed (not 3).')
put('p2l3-teachround',sec('p2l3-teachround','56–57 MIN',body,'Teach before worksheet page 2 (Q5). Click: the boats picture, the steps, the answer. Say: "In sharing, the leftover is left over. But here every child must ride, so the leftover child needs one more boat." Ask: "How many empty seats are in the 4th boat?" (3). '
 'Compare: "17 sweets among 3 children: how many EACH?" (5, 2 left over) and "13 children, boats of 4: how many BOATS?" (4). Read the question to know what to do with the leftover.'))
W3=[200,300,300]
body=h2('Find all the arrays: go in order')+pin(128,240,1664,p('12 chairs in equal rows. At least 2 rows, and at least 2 chairs in each row.',38,700),None,WHITE,20,'18px 28px')
body+=trow(128,380,['Rows','In each row','Works?'],W3,None,True,34)
for i,r in enumerate([['2','6','yes'],['3','4','yes'],['4','3','yes'],['5','—','no'],['6','2','yes']]): body+=trow(128,465+i*86,r,W3,'rise',False,34)
body+=pin(1100,380,692,p('Start at 2 rows. Add 1 row each time.',32,700),'fade',WHITE,20,'18px 24px')
body+=pin(1100,500,692,p('5 rows: 5, 10, 15. There is no 12, so 5 rows does not work.',32,700),'fade',WHITE,20,'18px 24px')
body+=pin(1100,640,692,p('7 rows of 2 needs 14 chairs: too many. Stop.',32,700),'fade',WHITE,20,'18px 24px')
body+=answer(1100,780,692,'4 ways')
put('p2l3-teachall',sec('p2l3-teachall','57–59 MIN',body,'Teach before worksheet page 2 (Q6). Use 12 counters to build each array as you click each row. Think-aloud: "2 rows: 12 shared into 2 rows is 6 in each row. 3 rows: 3, 6, 9, 12, that is 4 in each row. 4 rows of 3. 5 rows: 5, 10, 15, I jump over 12, so no. 6 rows of 2. 7 rows would need 14 chairs for 2 in each row, so I stop." '
 'Answer: 4 ways (2 rows of 6, 3 rows of 4, 4 rows of 3, 6 rows of 2). Ask: "Are 3 rows of 4 and 4 rows of 3 different?" (Yes for chairs in a hall: the rows look different. On the worksheet we count them as different ways.)'))
put('p2l3-try3',try_slide('p2l3-try3','59–60 MIN','Your turn: share, seat, list','Draw it or use counters. Then click to check.',[('a','22 marbles in 5 bags, the same in each. How many in each bag? How many left?','4 each, 2 left'),('b','14 children. Each car holds 4. How many cars?','4 cars'),('c','15 chairs. All the arrays (2 or more rows, 2 or more in each row)?','3 of 5, 5 of 3')],
 'Minutes 59 to 60. Whiteboards. a) 5, 10, 15, 20: 4 rounds use 20, 2 left over. b) 3 cars carry 12, 2 children are left, so 4 cars. c) 3 rows of 5 and 5 rows of 3 (2 and 4 rows do not work: 15 is odd, and 4 rows of 3 is 12, 4 rows of 4 is 16).',size=34))

# ---------- 10. worksheet page 2 ----------
put('p2l3-ws2',ws_preview('p2l3-ws2','60–67 MIN','Worksheet page 2: on your own',[('Q4','Ravi’s 23 stickers. Share them, then think about the leftover.'),('Q5','Vans for 28 children. Leftovers need a seat too!'),('Q6','All the arrays for 20 chairs. Start with 2 rows.'),('Q7','Bicycles and tricycles with 17 wheels. Find ALL the ways.')],'Finished early? Stretch and Challenge come next.','Children work alone. Note who needs a short catch-up next lesson. For Q7 point to the table: "Start with 1 tricycle. How many wheels are left for the bicycles?"'))
put('p2l3-ws2ans',check_slide('p2l3-ws2ans','67–70 MIN','Page 2: check together',[('Q4','5 each, 3 left over.  1 more sticker makes 24: 6 each'),('Q5','6 vans (5 vans hold 25, 3 more children).  2 empty seats'),('Q6','2 rows of 10,  4 rows of 5,  5 rows of 4,  10 rows of 2'),('Q7','7 bikes + 1 trike,   4 bikes + 3 trikes,   1 bike + 5 trikes')],
 'Click each answer after a child explains. Q6: 3 rows does not work (3 rows of 6 is 18, 3 rows of 7 is 21). Q7: with 1 tricycle, 14 wheels are left: 7 bicycles. 2 tricycles leave 11, an odd number, which bicycles cannot make. 3 tricycles leave 8: 4 bicycles. 4 leave 5: no. 5 leave 2: 1 bicycle. 6 tricycles need 18 wheels: too many. So exactly 3 ways.'))

# ---------- 11. stretch and challenge ----------
st=[('1.','Cars (4 wheels) and motorcycles (2 wheels): 8 vehicles and 22 wheels. How many cars?'),('2.','24 cupcakes go in boxes of 2, 3, 4, 5 or 10, the same in every box. Which box sizes leave none over?'),('3.','Tables have 4 legs and stools have 3 legs. Ravi counts 17 legs. How many tables and how many stools?')]
put('p2l3-stretch',sec('p2l3-stretch','For early finishers',h2('Stretch')+numbered_cards(st,36),
 'Answers: 1) 3 cars and 5 motorcycles (8 motorcycles = 16 wheels; each swap to a car adds 2; 3 swaps make 22; check 12 + 10 = 22). 2) Boxes of 2 (12 boxes), 3 (8 boxes) and 4 (6 boxes); boxes of 5 and 10 leave 4 over. 3) 2 tables and 3 stools (8 + 9 = 17); 0, 1, 3 or 4 tables leave 17, 13, 5 or 1 legs, which are not in the 3 times table.'))
ch=[('1.','Mr Lim has between 20 and 30 sweets. In groups of 4, 3 are left over. In groups of 5, 2 are left over. How many sweets does he have?'),('2.','A pen has hens and goats. There are 2 more hens than goats. There are 22 legs altogether. How many hens and how many goats?')]
put('p2l3-challenge',sec('p2l3-challenge','Challenge',h2('Challenge')+numbered_cards(ch,38),'Pairs try first, then use the "see it" slide if stuck, then the walk-through. These are Q6 and Q7 on the Think Harder page. Answers: 1) 27 sweets. 2) 5 hens and 3 goats.'))
# chdiag
def dots_box(x,y,n,col=YEL):
    w=n*30+14
    return f'<rect x="{x}" y="{y}" width="{w}" height="50" rx="10" fill="{WHITE}" stroke="{NAVY}" stroke-width="3"/>'+''.join(f'<circle cx="{x+22+j*30}" cy="{y+25}" r="11" fill="{col}" stroke="{NAVY}" stroke-width="2"/>' for j in range(n))
g1=T(20,40,'Groups of 4',28,TEAL,anchor='start')+dots_box(20,56,4)+dots_box(160,56,4)+T(318,92,'…',36)+f'<rect x="360" y="50" width="380" height="62" rx="14" fill="{SOFT}" stroke="{NAVY}" stroke-width="3"/>'+T(550,92,'3 left over',30)
g1+=T(20,170,'Groups of 5',28,TEAL,anchor='start')+dots_box(20,186,5)+dots_box(190,186,5)+T(378,222,'…',36)+f'<rect x="420" y="180" width="320" height="62" rx="14" fill="{SOFT}" stroke="{NAVY}" stroke-width="3"/>'+T(580,222,'2 left over',30)
g1+=T(380,310,'How many sweets? Try 21 to 29.',28)
g1+=''.join(f'<rect x="{30+i*80}" y="335" width="70" height="60" rx="10" fill="{WHITE}" stroke="{NAVY}" stroke-width="3"/>'+T(65+i*80,376,str(21+i),28) for i in range(9))
g2=place(g_goat(),40,20,1.0)+place(g_hen(),400,20,1.0)+T(120,206,'? goats',32)+T(480,206,'? hens',32)
g2+=f'<rect x="150" y="240" width="460" height="64" rx="14" fill="{SOFT}" stroke="{NAVY}" stroke-width="3"/>'+T(380,284,'2 more hens than goats',30)
g2+=f'<rect x="230" y="324" width="300" height="64" rx="14" fill="{YEL}" stroke="{NAVY}" stroke-width="3"/>'+T(380,368,'22 legs',32)
body=h2('Challenge: see it',60)+'<div style="display:flex;gap:32px;align-items:flex-start">'+card(f'<p style="font-size:28px;font-weight:700;color:{TEAL}">Q1: Mr Lim’s sweets</p>'+svgwrap('Groups of 4 with 3 left over, groups of 5 with 2 left over, and the numbers 21 to 29',760,410,g1,760,410),extra='flex:1;min-width:0;padding:20px 24px')+card(f'<p style="font-size:28px;font-weight:700;color:{TEAL}">Q2: Hens and goats</p>'+svgwrap('A goat and a hen, 2 more hens than goats, 22 legs',760,410,g2,760,410),extra='flex:1;min-width:0;padding:20px 24px')+'</div>'
put('p2l3-chdiag',sec('p2l3-chdiag','Challenge',body,'Show after pairs have tried the Challenge, or if they are stuck. The pictures show the problem, not the answer. Ask: What do you notice? What do we know? What do we not know yet? For Q1: "Which numbers from 21 to 29 leave 3 when we make groups of 4?" For Q2: "Try 1 goat. How many hens then?"'))
body=h2('Challenge: walk-through')+pin(128,250,800,p('Q1: make two lists',38,800,TEAL))
for i,t in enumerate(['Groups of 4, 3 left: 23, 27','Groups of 5, 2 left: 22, 27','In both lists: 27 sweets ✓']): body+=pin(128,330+i*110,800,p(t,34),'rise',WHITE)
body+=pin(992,250,800,p('Q2: guess and check',38,800,TEAL))
for i,t in enumerate(['1 goat, 3 hens: 4 + 6 = 10 legs','2 goats, 4 hens: 8 + 8 = 16 legs','3 goats, 5 hens: 12 + 10 = 22 ✓']): body+=pin(992,330+i*110,800,p(t,34),'rise',WHITE)
body+=pin(992,670,800,p('Each try adds 6 legs: one more goat (4) and one more hen (2).',30,600,MUTED),'fade')
put('p2l3-chwalk',sec('p2l3-chwalk','Challenge',body,'Use after pairs have tried. Q1: the 4 times table numbers from 20 to 28 are 20, 24, 28; add 3 to get 23, 27 (31 is too big). The 5 times table numbers are 20, 25; add 2 to get 22, 27. Only 27 is in both. Check: 27 = 6 fours + 3 = 5 fives + 2. '
 'Q2: keep the "2 more hens" rule in every guess, and change the number of goats by 1 each time. 5 hens and 3 goats: 10 + 12 = 22 legs.'))
put('p2l3-talk',talk_slide('p2l3-talk','70–80 MIN','Ravi shares stickers equally among 4 friends. Can the number left over ever be 4 or more? Why?','Minutes 70 to 80. Pairs talk for 2 minutes, then share. Answer: No. If 4 or more were left, Ravi could give each friend one more, so the leftover is always 0, 1, 2 or 3. Follow-up: "And when he shares among 5 friends?" (0 to 4). Praise the reasons, not only the answers.'))
put('p2l3-exit',exit_slide('p2l3-exit','80–90 MIN','A pen has hens and goats. There are 5 animals and 14 legs. How many hens and how many goats?','Minutes 80 to 90. Answer: 3 hens and 2 goats (6 + 8 = 14 legs, 3 + 2 = 5 animals). Look for a table starting with 5 hens (10 legs). Extension: find all the arrays (at least 2 rows, at least 2 in each row) for 16 counters (3 ways: 2 rows of 8, 4 rows of 4, 8 rows of 2).'))

# ---------- write ----------
if os.path.isdir(os.path.join(D,'slides')): shutil.rmtree(os.path.join(D,'slides'))
os.makedirs(os.path.join(D,'slides'))
for i,h in S.items(): open(os.path.join(D,'slides',i+'.html'),'w').write(h)
deck={'v':4,'createdOnFiles':{'v':1,'at':datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')},'lists':'css',
      'title':'Math Inquirers P2: Lesson 3 – Legs, Wheels and Arrays','order':ORDER,'cover':'p2l3-title',
      'sections':{'s1':{'description':'Warm-up and explore','start':'p2l3-title'},'s2':{'description':'Teach: arrays, and how many of each with a table','start':'p2l3-teach1'},'s3':{'description':'Worksheet with teaching before each page','start':'p2l3-break'},'s4':{'description':'Stretch, challenge, talk and exit','start':'p2l3-stretch'}},
      'faces':{'fredoka':{'family':'Fredoka','href':'https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&display=swap'},'nunito-sans':{'family':'Nunito Sans','href':'https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@400;600;700&display=swap'}},
      'designSystems':[]}
json.dump(deck,open(os.path.join(D,'deck.json'),'w'),indent=1,ensure_ascii=False)
print(len(ORDER),'slides')
