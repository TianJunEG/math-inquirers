"""Math Inquirers P2, Lesson 10: Puzzle Day. Writes split/p2l10/project (deck.json + slides/*.html)."""
import json,os,sys,math,shutil,datetime
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,H)
from slidekit import *
import p2gaps
D=os.path.join(H,'..','split','p2l10','project'); S={}
def put(i,h): S[i]=h
RED='#D64545'; GREEN='#BFE3DC'; PINK='#F4A6A6'; BLUE='#9CC9EE'

# ---------- generic helpers (P2 decks) ----------
def svg(w,h,body,aria,style=''): return f'<svg aria-label="{E(aria)}" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="width:{w}px;height:{h}px;{style}">{body}</svg>'
def T(x,y,s,size=30,fill=NAVY,anchor='middle',weight=800,font='Nunito Sans, Arial'): return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" fill="{fill}" font-family="{font}">{E(str(s))}</text>'
def title_slide(sid,n,title,sub,today,notes):
    return (f'<section id="{sid}" data-transition="fade" style="background:{NAVY};color:{CREAM};font-family:{BF};padding:128px 128px 160px;display:flex;flex-direction:column;justify-content:center;gap:36px">\n'
            f'<p style="font-size:32px;font-weight:700;letter-spacing:4px;color:{YEL}">PRIMARY 2  •  LESSON {n}  •  WEEK 5</p>\n'
            f'<h1 style="font-family:{HF};font-size:128px;font-weight:600;line-height:1.05">{E(title)}</h1>\n<p style="font-size:44px;color:#C9D4EC">{E(sub)}</p>\n'
            f'<div style="background:#26385F;border-radius:24px;padding:40px;display:flex;flex-direction:column;gap:12px"><p style="font-size:28px;font-weight:700;letter-spacing:3px;color:{YEL}">TODAY WE WILL</p><p style="font-size:44px;font-weight:600">{E(today)}</p></div>\n'
            f'<p style="position:absolute;left:128px;bottom:64px;width:1400px;font-size:24px;color:#B7C3DD">{E(FOOT)}</p>\n<aside>{E(notes)}</aside>\n</section>\n')
def break_slide(sid,text,sub,notes):
    return (f'<section id="{sid}" data-transition="fade" style="background:{TEAL};color:{CREAM};font-family:{BF};padding:128px 128px 160px;display:flex;flex-direction:column;justify-content:center;gap:36px">\n'
            f'<p style="font-size:32px;font-weight:700;letter-spacing:4px;color:{YEL}">32–36 MIN</p>\n<h2 style="font-family:{HF};font-size:110px;font-weight:600;line-height:1.05">Brain break</h2>\n'
            f'<p style="font-size:48px;font-weight:600">{E(text)}</p>\n<p style="font-size:36px;color:#D7EFEA">{E(sub)}</p>\n'
            f'<p style="position:absolute;left:128px;bottom:64px;width:1400px;font-size:24px;color:#D7EFEA">{E(FOOT)}</p>\n<aside>{E(notes)}</aside>\n</section>\n')
def numcards(items,size=36):
    return ''.join(card(p(f'<span style="color:{TEAL}">{a}</span>  {E(b)}',size,600,raw=True)) for a,b in items)
def quick(sid,time,qs,notes,step=125,size=36):
    body=h2('Quick questions')+''.join(qrow(128,250+i*step,1250,a,b,size) for i,(a,b,c) in enumerate(qs))+''.join(answer(1420,250+i*step,372,c) for i,(a,b,c) in enumerate(qs))
    return sec(sid,time,body,notes)
def talk_slide(sid,q,notes):
    body=h2('Talk time')+card(chip('TALK TIME',YEL,NAVY)+p(q,42,600))+card(p('Sentence starters:',34,400,MUTED)+p('“I started by …”   “I noticed that …”   “I know because …”',38,600))
    return sec(sid,'72–80 MIN',body,notes)
def exit_slide(sid,q,a,notes,time='80–90 MIN'):
    body=h2('Exit ticket')+card(chip('EXIT TICKET')+p(q,46,600))+card(p('Write your answer and how you know on a slip of paper. Show it to your tutor, then collect your stamp.',34,400))
    body+=answer(128,760,1664,'Answer: '+a)
    return sec(sid,time,body,notes)
def write_deck(lesson_title,order,sections):
    sd=os.path.join(D,'slides')
    if os.path.isdir(sd): shutil.rmtree(sd)
    os.makedirs(sd)
    for i in order: open(os.path.join(sd,i+'.html'),'w').write(S[i])
    deck={'v':4,'createdOnFiles':{'v':1,'at':datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')},'lists':'css','title':lesson_title,'order':order,'cover':order[0],'sections':sections,
          'faces':{'fredoka':{'family':'Fredoka','href':'https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&display=swap'},'nunito-sans':{'family':'Nunito Sans','href':'https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@400;600;700&display=swap'}},'designSystems':[]}
    json.dump(deck,open(os.path.join(D,'deck.json'),'w'),indent=1,ensure_ascii=False)
    missing=[i for i in S if i not in order]
    print(len(order),'slides', 'UNUSED:'+','.join(missing) if missing else '')

# ---------- drawings for this lesson ----------
def tick(x,y,s=1): return f'<path d="M{x-20*s} {y} L{x-6*s} {y+16*s} L{x+22*s} {y-18*s}" fill="none" stroke="{TEAL}" stroke-width="{9*s}" stroke-linecap="round" stroke-linejoin="round"/>'
def cross(x,y,s=1): return f'<path d="M{x-15*s} {y-15*s} L{x+15*s} {y+15*s} M{x+15*s} {y-15*s} L{x-15*s} {y+15*s}" stroke="{RED}" stroke-width="{7*s}" stroke-linecap="round"/>'
def star(cx,cy,r=22,fill=YEL):
    pts=' '.join(f'{cx+(r if k%2==0 else r*0.45)*math.sin(k*math.pi/5):.1f},{cy-(r if k%2==0 else r*0.45)*math.cos(k*math.pi/5):.1f}' for k in range(10))
    return f'<polygon points="{pts}" fill="{fill}" stroke="{NAVY}" stroke-width="3"/>'
def digit_cards(ds,w=100,gap=24,aria='Digit cards'):
    b=''.join(f'<rect x="{6+i*(w+gap)}" y="6" width="{w}" height="{int(w*1.2)}" rx="12" fill="{WHITE}" stroke="{NAVY}" stroke-width="5"/>'+T(6+i*(w+gap)+w/2,6+w*0.82,d,int(w*0.62),font='Fredoka, Arial') for i,d in enumerate(ds))
    return svg(len(ds)*(w+gap)+12-gap,int(w*1.2)+12,b,aria)

# ---------- 1. title ----------
put('p2l10-title',title_slide('p2l10-title',10,'Puzzle Day','Mixed puzzles: how to start a puzzle','Learn three ways to start a puzzle, then use them on mixed challenges.',
 'Objective: Choose a way to start a puzzle (draw it, list it in order, make a table) and use it on mixed puzzles: picture graphs with a key of 5 or 10, a logic grid with exactly one answer, numbers to 1000, money, fractions, and × and ÷ with the 2, 3, 4, 5 and 10 tables. Check the answer and explain it. '
 'Materials: Four station cards (all on ONE slide in the deck, printed in the tutor guide), play coins, digit cards 0 to 9, paper strips for fractions, mini whiteboards, certificates, stamps. '
 'Online: Each breakout pair takes two station cards (the tutor pastes their text into the breakout room chat), about 2 minutes a card, then everyone reports back to the group. Each child needs digit cards (cut from paper), a pencil and a mini whiteboard. '
 'Time plan: warm-up 0 to 8, explore 8 to 20 (explore2 talk is 6 minutes), teaching 20 to 32 (how to start a puzzle: draw it, list it, make a table; click to reveal each step and answer), brain break 32 to 36, short teaching 36 to 38, worksheet page 1 38 to 50 then check together 50 to 52, short teaching 52 to 57, worksheet page 2 57 to 69 then check together 69 to 72, talk time 72 to 80, exit ticket 80 to 88, certificates 88 to 90.'))

# ---------- 2. warm-up: relay cards ----------
relay_all=[('Digit cards','Make the biggest 3-digit number with 4, 0, 7.','740'),('Missing digit','3[ ]5 + 214 = 579. Which digit goes in the box?','6'),('Legs','How many legs do 5 chairs have?','20'),('Patterns','3, 8, 13, 18, __','23'),('Money','A pen costs 65¢. You pay $1. What is your change?','35¢'),('Fractions','1/4 of a pizza is eaten. What fraction is left?','3/4')]
relay=[relay_all[0],relay_all[4],relay_all[5]]   # three relay cards only: digits, change, fractions (about 2.5 minutes)
body=h2('Warm-up: relay review')+p('Answer the card, then pass it on: choose a friend who has not had a turn. You may say “pass”.',34,600,MUTED)
CW=533
for i,(tag,q,a) in enumerate(relay):
    L=128+(i%3)*(CW+32); Tp=280+(i//3)*310
    body+=pin(L,Tp,CW,chip(tag,TEAL,CREAM,26)+p(q,34,700),None,WHITE,24,'18px 24px',f'box-sizing:border-box;height:280px;border:4px solid {NAVY};box-shadow:8px 8px 0 {NAVY}')
    body+=pin(L+CW-200,Tp+196,170,f'<p style="font-size:40px;font-weight:800;text-align:center">{E(a)}</p>','pop',YEL,16,'8px 14px',f'box-sizing:border-box;border:3px solid {NAVY}')
put('p2l10-warm1',sec('p2l10-warm1','0–5 MIN',body,'Minutes 0 to 5. Relay review, three cards only (digits, change, fractions; the other three are spare). Read a card and ask for a volunteer; that child answers, then chooses a friend who has not had a turn yet. Any child may say “pass”. Never name a child to put them on the spot. Click to reveal each answer in order. A different answer gets “let us test that”, never a groan. '
 'Answers: 740 (biggest digit first; 0 last). 35¢ ($1 = 100¢; 65 + 35 = 100). 3/4 (4 quarters make the whole; 1 eaten, 3 left). Spare cards: missing digit 3[ ]5 + 214 = 579 is 6; 5 chairs have 20 legs; 3, 8, 13, 18, __ is 23. Ask after each: "Which lesson does this remind you of?"'))

qs=[('1.','Share 40 stickers equally among 5 children. How many each?','8'),('2.','Which is bigger: 1/3 or 1/5 of the same cake?','1/3')]   # questions 1 and 3 of the guide table; 2, 4 and 5 are spare
put('p2l10-warm2',quick('p2l10-warm2','5–8 MIN',qs,'Minutes 5 to 8. Read each aloud, give thinking time, take answers, then click to show. Answers: 1) 8 (5 × 8 = 40, count in 5s to 40: 8 jumps). 2) 1/3: the cake is cut into fewer pieces, so each piece is bigger (draw two same bars, one cut in 3 and one cut in 5). Spare questions in the guide table: 10:55 am plus 10 minutes is 11:05 am; half of a circle is a half circle; a number plus 30 makes 100: 70.',size=34))

# ---------- 4. explore ----------
st=''
st+=f'<rect x="20" y="20" width="270" height="200" rx="16" fill="{WHITE}" stroke="{NAVY}" stroke-width="4"/>'+''.join(star(60+k*44,70+r*56,17) for r,n in enumerate([4,2,3]) for k in range(n))+T(155,256,'Graph',28)
gx,gy=330,20
st+=f'<rect x="{gx}" y="{gy}" width="270" height="200" rx="16" fill="{WHITE}" stroke="{NAVY}" stroke-width="4"/>'+''.join(f'<rect x="{gx+30+c*70}" y="{gy+30+r*50}" width="70" height="50" fill="{GREY if (r+c)%2 else WHITE}" stroke="{NAVY}" stroke-width="2.5"/>' for r in range(3) for c in range(3))+tick(gx+65,gy+55,0.8)+cross(gx+135,gy+105,0.8)+T(gx+135,256,'Logic grid',28)
cx_=640
st+=f'<rect x="{cx_}" y="20" width="270" height="200" rx="16" fill="{WHITE}" stroke="{NAVY}" stroke-width="4"/>'+''.join(f'<circle cx="{cx_+60+k*75}" cy="{120}" r="{r}" fill="#E5E9F2" stroke="{NAVY}" stroke-width="3"/>'+T(cx_+60+k*75,130,l,26) for k,(l,r) in enumerate([('20¢',34),('50¢',38),('10¢',30)]))+T(cx_+135,256,'Coins',28)
fx=950
st+=f'<rect x="{fx}" y="20" width="270" height="200" rx="16" fill="{WHITE}" stroke="{NAVY}" stroke-width="4"/><rect x="{fx+25}" y="95" width="220" height="50" fill="{YEL}" stroke="{NAVY}" stroke-width="3"/>'+''.join(f'<line x1="{fx+25+k*44}" y1="95" x2="{fx+25+k*44}" y2="145" stroke="{NAVY}" stroke-width="3"/>' for k in range(1,5))+f'<rect x="{fx+25}" y="95" width="88" height="50" fill="{TEAL}" opacity=".55"/>'+T(fx+135,256,'Fraction strip',28)
exp=svg(1240,270,st,'Four station cards: a picture graph, a logic grid, coins and a fraction strip','width:960px;height:209px')
steps=['Your pair takes two station cards from the next slide (for example 1 and 3, or 2 and 4).','Read the card aloud. Before you solve it, write how you will start: draw, list or table.','Solve it and check it (about 2 minutes a card). Then take the other card.','Be ready to explain how you started and how you know.']
body=h2('Explore: four puzzle stations')+pin(128,240,1664,chip('EXPLORE')+'<ol style="font-size:32px;font-weight:600;padding-left:48px;display:flex;flex-direction:column;gap:8px;line-height:1.3">'+''.join(f'<li>{E(s)}</li>' for s in steps)+'</ol>',None,WHITE,24,'22px 36px')
body+=pin(128,625,1664,exp,None,WHITE,24,'8px 20px','align-items:center')
put('p2l10-explore1',sec('p2l10-explore1','8–9 MIN',body,'Minutes 8 to 9. Explain the plan: four station cards, all on the NEXT slide. Online, a tutor cannot visit four physical stations, so each breakout pair takes TWO cards (paste their text into the breakout room chat) and works about 2 minutes on each: 4.5 minutes of pair work in all, one round of breakout rooms. Answers are in the notes of the next slide. '
 'Walk round and ask "How did you start?" before anything else.'))

# ---------- 3b. the four station cards: ONE slide (re-budget: -4 slide changes) ----------
CARDS=[(1,'picture graph','Each picture stands for 5 books. Monday has 3 pictures, Tuesday 5, Wednesday 2. How many books were read on these 3 days?','50 books'),
       (2,'logic grid','Ali, Ben and Cai each have one pet: a cat, a dog or a fish. Ben has the fish. Ali does not have the dog. Who has the cat?','Ali has the cat (Cai has the dog)'),
       (3,'coin puzzle','Make 70¢ with exactly 4 coins. You can use 5¢, 10¢, 20¢ and 50¢ coins. Find all the ways.','2 ways: 50¢ + 10¢ + 5¢ + 5¢, and 20¢ + 20¢ + 20¢ + 10¢'),
       (4,'fraction strip','A strip is cut into 8 equal parts. 3 parts are red and 2 parts are blue. What fraction is NOT coloured?','3/8')]
body=h2('Four station cards',60)
for k,(n,topic,text,ans) in enumerate(CARDS):
    L=128+(k%2)*852; TT=215+(k//2)*345
    body+=pin(L,TT,800,chip(f'CARD {n}: {topic}')+p(text,30,700),None,WHITE,24,'16px 24px',f'box-sizing:border-box;height:330px')
    body+=pin(L+20,TT+232,760,f'<p style="font-size:28px;font-weight:800;line-height:1.2">{E(ans)}</p>','pop',YEL,16,'10px 16px',f'box-sizing:border-box;border:3px solid {NAVY}')
put('p2l10-cards',sec('p2l10-cards','12–18.5 MIN',body,
 'Minutes 12 to 18.5. All four station cards are on this ONE slide (one slide change instead of four). Online, each breakout pair takes TWO cards (for example 1 and 3, or 2 and 4); paste the text of their two cards into the breakout room chat. About 2 minutes a card. Answers appear on the click. '
 'Card 1 (picture graph): read the key first: one picture is worth 5 books. 3 + 5 + 2 = 10 pictures, 10 × 5 = 50 books. Common mistake: 10 (counting the pictures). '
 'Card 2 (logic grid): tick Ben and fish, cross the rest of Ben\u2019s row and the fish column. Ali is not dog and fish is taken, so Ali has the cat. Cai has the dog. '
 'Card 3 (coins): list in order, biggest coin first. With 50¢: 20¢ left for 3 coins: 10 + 5 + 5. Without 50¢: 20 + 20 + 20 + 10. Exactly 2 ways. '
 'Card 4 (fraction strip): 3 + 2 = 5 coloured, 8 − 5 = 3 not coloured: 3/8. Common mistake: 5/8.'))

qs=[('1.','How did you start each card? Draw, list or table?'),('2.','Which card was hardest? Why?'),('3.','What helped when you were stuck?')]
put('p2l10-explore2',sec('p2l10-explore2','14–20 MIN',h2('Explore: talk about it')+numcards(qs,40),'Minutes 14 to 20. Let pairs finish, then gather (all three questions stay; about 4 to 5 minutes). What we want them to notice: every card got easier once it was on paper (a drawing, a list in order, or a table). Answers: 1) Open answers; collect one example of each start on the board. 2) Open answers. 3) Listen for: drawing it, going in order, trying small numbers first, checking with every clue. Follow-up: "How do you know there is only one answer to the coin card?" (we listed every 3-coin set in order).'))

# ---------- 6. teach: how to start ----------
ic_draw=svg(440,140,''.join(f'<rect x="20" y="{12+i*44}" width="{w}" height="34" rx="6" fill="{c}" stroke="{NAVY}" stroke-width="4"/>' for i,(w,c) in enumerate([(220,PINK),(320,BLUE),(160,GREEN)])),'Icon: bars drawn for a puzzle')
ic_list=svg(440,140,''.join(T(30,40+i*44,f'{i+1}.',30,TEAL,'start')+f'<line x1="80" y1="{30+i*44}" x2="{380-i*60}" y2="{30+i*44}" stroke="{NAVY}" stroke-width="6" stroke-linecap="round"/>' for i in range(3)),'Icon: a list in order')
ic_table=svg(440,140,''.join(f'<rect x="{20+c*100}" y="{10+r*40}" width="100" height="40" fill="{YEL if r==0 else WHITE}" stroke="{NAVY}" stroke-width="3"/>' for r in range(3) for c in range(4)),'Icon: a table')
cards=[('Draw it',ic_draw,'Before-and-after stories, more than and fewer than, halves.'),('List it',ic_list,'Find every number, every coin set, every way.'),('Make a table',ic_table,'Try 0, 1, 2, 3 … when something changes step by step.')]
body=h2('How to start a puzzle')+p('Stuck? Do not just stare. Put the puzzle on paper.',34,600,MUTED)
for i,(t,ic,use) in enumerate(cards): body+=pin(128+i*572,320,480,p(t,44,800,TEAL)+ic+p('Use it for: '+use,30,600),'rise',WHITE,24,'26px 30px')
body+=pin(128,790,1664,p('Why? A puzzle is hard to hold in your head. On paper you can see it, check it and explain it.',32,700),'fade',SOFT,20,'18px 28px')

# ---------- 7. worked example: draw it ----------
def sticker_bar(stage):
    b=f'<rect x="20" y="40" width="1100" height="80" rx="8" fill="{WHITE}" stroke="{NAVY}" stroke-width="5"/><line x1="570" y1="30" x2="570" y2="130" stroke="{NAVY}" stroke-width="5"/>'
    b+=T(295,92,'half to Ben',32,MUTED)
    if stage>=1: b+=f'<rect x="572" y="42" width="324" height="76" fill="{PINK}"/><rect x="896" y="42" width="222" height="76" fill="{GREEN}"/><line x1="896" y1="40" x2="896" y2="120" stroke="{NAVY}" stroke-width="4"/>'+T(734,92,'6 to Siti',32)+T(1007,92,'4 left',32)
    if stage>=2: b+=f'<path d="M575 140 Q845 190 1115 140" fill="none" stroke="{TEAL}" stroke-width="5"/>'+T(845,196,'6 + 4 = 10',32,TEAL)+f'<path d="M25 140 Q295 190 565 140" fill="none" stroke="{TEAL}" stroke-width="5"/>'+T(295,196,'also 10',32,TEAL)
    b+=T(20,26,'All of Mei’s stickers',28,NAVY,'start')
    return svg(1140,210,b,['Mei’s stickers drawn as a bar cut into two halves','The second half: 6 to Siti and 4 left','Both halves are 10'][stage])
body=h2('Draw it: a before-and-after story')+card(p('Mei had some stickers. She gave half of them to Ben. Then she gave 6 to Siti. She has 4 left. How many did she have at first?',34,700))
body+=pin(128,400,1140,sticker_bar(0))+pin(128,400,1140,sticker_bar(1),'fade')+pin(128,400,1140,sticker_bar(2),'fade')
body+=step(1,'Draw a bar for all the stickers. Cut it into two equal halves.',top=640,size=32)
body+=step(2,'The half Mei kept is the 6 for Siti and the 4 left: 6 + 4 = 10.',top=740,size=32)
body+=pin(1300,400,492,p('Both halves are the same: 10 + 10 = 20.',34,800),'pop',YEL,20,'18px 26px')
body+=pin(1300,540,492,p('Check: half of 20 is 10. 10 − 6 = 4 ✓',30,700),'fade',SOFT,20,'14px 22px')
put('p2l10-we1',sec('p2l10-we1','21–24 MIN',body,'Worked example: draw it. Ask first: "Can you hold all of this in your head?" Click order: the second half fills in (6 and 4), then the 10s, then step 1, step 2, the answer, the check. (If you prefer, say step 1 before the first click.) '
 'Think-aloud: "Mei had some stickers. She gave half to Ben. Then she gave 6 to Siti and had 4 left. I cannot hold that in my head, so I draw a bar cut into two halves. One half went to Ben. The other half is the 6 for Siti and the 4 left: 6 + 4 = 10. Both halves are the same, so Mei had 10 + 10 = 20 stickers. Check: half of 20 is 10, 10 − 6 = 4 ✓." '
 'Common mistake: 6 + 4 = 10 given as the answer (that is only half).'))


# ---------- 9. worked example: list it ----------
body=h2('List it: every number, in order')+pin(128,230,560,p('Use the cards 2, 0 and 5 once each. How many 3-digit numbers can you make?',34,700)+digit_cards([2,0,5],110,30,'Digit cards 2, 0 and 5'),None,WHITE,24,'22px 28px')
body+=step(1,'Go in order of the hundreds digit. 0 cannot go first: 025 is not a 3-digit number.',left=760,top=230,width=1032,size=32)
body+=step(2,'Hundreds digit 2:   205,   250',left=760,top=380,width=1032,size=34)
body+=step(3,'Hundreds digit 5:   502,   520',left=760,top=480,width=1032,size=34)
body+=answer(760,590,1032,'4 numbers.  Greatest 520, smallest 205.')
body+=pin(128,740,1664,p('Going in order means you do not miss a number, and you know when to stop.',32,700),'fade',SOFT,20,'18px 28px')
put('p2l10-we2',sec('p2l10-we2','25–27 MIN',body,'Worked example: list it. Give out digit cards if you have them. Think-aloud: "Digit cards 2, 0 and 5. How many 3-digit numbers? I list them in order, smallest hundreds digit first. 0 cannot go first, because 025 is just 25. With 2 first, the other two cards can go 0 5 or 5 0: 205, 250. With 5 first: 502, 520. Four numbers, and I know I have them all because I went in order." '
 'Ask: "Why are there two numbers for each first card?" (the last two cards can swap). This is the method for worksheet Q2 (different cards).'))
put('p2l10-try2',try_slide('p2l10-try2','27–28 MIN','Your turn: list it','Go in order. Biggest or smallest first.',[('a','Cards 1, 3 and 6. How many 3-digit numbers can you make?','6 numbers'),('b','Which of those numbers is the biggest even number?','316')],
 'Whiteboards. a) 136, 163, 316, 361, 613, 631: 6 numbers (no 0 this time, so every card can go first). b) Even numbers end in 0, 2, 4, 6 or 8: only 136 and 316 end in 6; the bigger is 316. c) List with the biggest coin first: a 50¢ coin is already 50¢ with 1 coin, no. With 20¢: 20 + 20 + 5 + 5 ✓, 20 + 10 + 10 + 10 ✓. With no 20¢: four 10¢ is only 40¢. So 2 ways.',34))

# ---------- 11. worked example: make a table ----------
W3=[260,260,260]
body=h2('Make a table: heads and legs')+card(p('A farm has chickens and goats. There are 7 heads and 20 legs. How many goats?',36,700))
body+=trow(128,370,['Goats','Chickens','Legs'],W3,None,True,32)
for i,(g,c) in enumerate([(0,7),(1,6),(2,5),(3,4)]): body+=trow(128,440+i*70,[str(g),str(c),f'{4*g} + {2*c} = {4*g+2*c}'+(' ✓' if g==3 else '')],W3,'rise',False,32)
body+=pin(1100,370,692,p('Start with 0 goats. Each time, swap one chicken for a goat: 2 more legs.',32,700),'fade',WHITE,20,'20px 26px')
body+=answer(1100,560,692,'3 goats and 4 chickens')
body+=qrow(128,780,1250,'Your turn:','6 bicycles and tricycles have 15 wheels. How many tricycles?',32)+answer(1420,780,372,'3')
put('p2l10-we3',sec('p2l10-we3','28–31 MIN',body,'Worked example: make a table. Think-aloud: "Chickens and goats: 7 heads and 20 legs. I make a table. 0 goats: 7 chickens, 14 legs. 1 goat: 4 + 12 = 16. 2 goats: 8 + 10 = 18. 3 goats: 12 + 8 = 20 ✓. So 3 goats and 4 chickens. Each goat I swap in adds 2 legs, so I could even have jumped straight there: 20 − 14 = 6 more legs, 3 swaps." '
 'Your turn: tricycles 0 → 12 wheels, 1 → 13, 2 → 14, 3 → 15 ✓: 3 tricycles and 3 bicycles (9 + 6 = 15). This is the method for worksheet Q3 (coins).'))

body=h2('Key idea: how to start a puzzle')+card(p('Stuck? Draw it, list it in order, or make a table.',46,700))+card(p('Then check your answer against every clue and explain why.',38,600,MUTED))
put('p2l10-key',sec('p2l10-key','31–32 MIN',body,'Say the key idea together. Common mistakes to watch for during the worksheet: (1) Q1: counting the pictures instead of using the key (writing 6 instead of 30). (2) Q2: putting 0 first, or missing a number because the list is not in order. (3) Q3: guessing without a table, or not checking that there are exactly 6 coins. (4) Q4: putting a tick without crossing out the rest of that row and column. (5) Q5: forgetting that Mei eats 2 MORE pieces than Ali (not 2 pieces).'))
put('p2l10-break',break_slide('p2l10-break','Freeze with maths! Dance until the music stops.','Then make the shape the tutor calls with your arms: a half circle, a quarter circle, a cone, a cuboid.','Four minutes. Online: children stay in view of the camera and move in place. Finish with a drink of water.'))

# ---------- teach before page 1: picture graph ----------
rows=[('Ali',4),('Mei',2),('Ravi',None)]
g=''
for i,(n,k) in enumerate(rows):
    y=10+i*86; g+=f'<rect x="0" y="{y}" width="760" height="80" fill="{SKY if i%2==0 else WHITE}"/>'+T(20,y+52,n,34,anchor='start')
    if k: g+=''.join(star(200+j*70,y+40,28) for j in range(k))
    else: g+=T(200,y+52,'?',40,RED,'start')
g+=f'<rect x="0" y="10" width="760" height="258" fill="none" stroke="{NAVY}" stroke-width="4"/><line x1="160" y1="10" x2="160" y2="268" stroke="{NAVY}" stroke-width="4"/>'+star(220,316,26)+T(260,328,'= 10 books',34,anchor='start')
graph=svg(760,350,g,'Picture graph of books read: Ali 4 stars, Mei 2 stars, Ravi unknown; each star stands for 10 books')
ravi=svg(760,350,''.join(star(200+j*70,10+2*86+40,28,'#FFE9A8') for j in range(3)),'Ravi’s row: 3 stars')
body=h2('Picture graphs: read the key first')+card(p('The children read 90 books altogether. How many did Ravi read?',34,700))
body+=pin(128,340,760,graph)+pin(128,340,760,ravi,'fade')
body+=step(1,'Key: one star is 10 books. Ali: 10, 20, 30, 40. Mei: 20.',left=950,top=340,width=842,size=32)
body+=step(2,'Ravi: 90 − 40 − 20 = 30 books.',left=950,top=470,width=842,size=32)
body+=step(3,'30 books is 3 stars. Draw them!',left=950,top=570,width=842,size=32)
body+=qrow(128,750,1250,'Your turn:','Key: one picture = 5 children. A row has 4 pictures. How many children?',32)+answer(1420,750,372,'20')
put('p2l10-teachgraph',sec('p2l10-teachgraph','36–38 MIN',body,'Teach before worksheet page 1 (Q1 is a picture graph with a key of 5). Ask first: "Ali has 4 stars. Did he read 4 books?" (No: read the key first.) Click step 1: count in 10s along each row. Step 2: "The total is 90. Ali and Mei read 40 + 20 = 60, so Ravi read the rest: 90 − 60 = 30." Step 3, then the stars appear: "30 books is 10, 20, 30: 3 stars." '
 'Your turn: count in 5s: 5, 10, 15, 20. Common mistake: writing the number of pictures (4) instead of using the key.'))

put('p2l10-ws1',ws_preview('p2l10-ws1','38–50 MIN','Worksheet page 1: with your partner',[('Q1','Picture graph, key of 5. Read the key first. Find Thursday from the total.'),('Q2','Digit cards 3, 0, 8. List the numbers in order.'),('Q3','★ Take-home star: 6 coins worth $1.80. Make a table: 0, 1, 2 … 50¢ coins.')],'Stuck? Draw it, list it, or make a table.','Minutes 38 to 50. Walk around. Ask "How did you start?" and "How do you know?" before giving any help. Q3 (the coins table) is marked ★ take-home on the page: children do it at home, so there is no Q3 in class; the table method was shown in the mini-lesson (chickens and goats).'))
put('p2l10-ws1ans',check_slide('p2l10-ws1ans','50–52 MIN','Page 1: check together',[('Q1','a) 30   b) 5 pictures (25 ice-creams)   c) $30'),('Q2','a) 308, 380, 803, 830   b) 830, 308   c) 308, 380, 803'),('Q3','★ take-home:  Two 50¢ coins and four 20¢ coins')],
 'Click each answer after a pair explains how they started (answer lines only). Q3 is a take-home star: the answer stays here so children can mark it at home. Q1: a) 6 pictures × 5: 5, 10, … 30. b) Monday 20, Tuesday 30, Wednesday 15: 65; 90 − 65 = 25, which is 5 pictures. c) 15 ice-creams at $2: count in 2s fifteen times, or 15 + 15 = 30: $30. '
 'Q2: 0 cannot go first. 3 first: 308, 380. 8 first: 803, 830. Between 300 and 810: 308, 380, 803 (830 is more than 810). Q3: table: 0 fifties: 120¢; 1: 150¢; 2: 180¢ = $1.80 ✓. Check: 50 + 50 + 20 + 20 + 20 + 20 = 180 and that is 6 coins.'))

# ---------- teach before page 2: logic grid ----------
names=['Ravi','Lin','Kai']; foods=['kaya toast','roti prata','chicken rice']
CWg,RH,LW=250,90,170
def gx(c): return LW+c*CWg+CWg/2
def gy(r): return 80+r*RH+RH/2
base=''.join(f'<rect x="{LW+c*CWg}" y="80" width="{CWg}" height="{RH*3}" fill="none" stroke="{NAVY}" stroke-width="3"/>' for c in range(3))
base+=''.join(f'<rect x="0" y="{80+r*RH}" width="{LW+3*CWg}" height="{RH}" fill="none" stroke="{NAVY}" stroke-width="3"/>'+T(20,gy(r)+12,n,34,anchor='start') for r,n in enumerate(names))
base+=''.join(f'<rect x="{LW+c*CWg}" y="0" width="{CWg}" height="80" fill="{YEL}" stroke="{NAVY}" stroke-width="3"/>'+T(gx(c),52,f,30) for c,f in enumerate(foods))
GW=LW+3*CWg+4; GH=80+3*RH+4
g0=svg(GW,GH,base,'A logic grid: Ravi, Lin and Kai, and kaya toast, roti prata and chicken rice')
g1=svg(GW,GH,tick(gx(1),gy(2))+cross(gx(0),gy(2))+cross(gx(2),gy(2))+cross(gx(1),gy(0))+cross(gx(1),gy(1)),'Clue 1 marks: Kai has roti prata, so the rest of his row and the roti prata column are crossed')
g2=svg(GW,GH,cross(gx(2),gy(1))+tick(gx(0),gy(1))+cross(gx(0),gy(0)),'Clue 2 marks: Lin is not chicken rice, so Lin has kaya toast')
g3=svg(GW,GH,tick(gx(2),gy(0)),'Ravi has chicken rice')
body=h2('Logic grid: tick one, cross the rest')+p('Each child buys a different snack. Clue 1: Kai buys roti prata. Clue 2: Lin does not buy chicken rice.',32,700)
for i,gg in enumerate([g0,g1,g2,g3]): body+=pin(128,330,GW,gg,None if i==0 else 'fade')
body+=step(1,'Clue 1: tick Kai and roti prata. Cross the rest of his row and the rest of that column.',left=1100,top=330,width=692,size=30)
body+=step(2,'Clue 2: cross Lin and chicken rice. Only kaya toast is left for Lin.',left=1100,top=490,width=692,size=30)
body+=step(3,'Ravi gets the last one: chicken rice. Check both clues ✓',left=1100,top=640,width=692,size=30)
put('p2l10-teachlogic',sec('p2l10-teachlogic','52–55 MIN',body,'Teach before worksheet page 2 (Q4 is a logic grid with 4 children). Draw the grid. Click order: the clue 1 marks, step 1, the clue 2 marks, step 2, the last tick, step 3. (Or reveal each step first if you prefer.) '
 'Think-aloud: "Each child buys a DIFFERENT snack, so each row has exactly one tick and each column has exactly one tick. Clue 1 tells me Kai buys roti prata: tick. So Kai cannot buy anything else, and nobody else can buy roti prata: I cross them. Clue 2: Lin does not buy chicken rice: cross. Look at Lin’s row: only kaya toast is left, tick it, and cross kaya toast for Ravi. Ravi’s row has one empty box left: chicken rice." '
 'Check exactly one answer: every row and every column has one tick. Common mistake: ticking without crossing the rest, so the next step is hidden.'))

# ---------- teach before page 2: growing tables + fractions ----------
def hexes(n,x0,y0,r):
    b=''; w=r*math.sqrt(3); d=r*math.sqrt(3)/2+13
    for k in range(n):
        cx=x0+w/2+k*w; pts=' '.join(f'{cx+r*math.cos(math.radians(30+60*j)):.1f},{y0+r*math.sin(math.radians(30+60*j)):.1f}' for j in range(6))
        b+=f'<polygon points="{pts}" fill="{SKY}" stroke="{NAVY}" stroke-width="3"/>'
        for ang in (0,60,120,180,240,300):
            if (ang==0 and k<n-1) or (ang==180 and k>0): continue
            b+=f'<circle cx="{cx+d*math.cos(math.radians(ang)):.1f}" cy="{y0+d*math.sin(math.radians(ang)):.1f}" r="7" fill="{RED}" stroke="{NAVY}" stroke-width="2"/>'
    return b,x0+n*w
hb=''; x=110
for n in (1,2,3):
    b,x2=hexes(n,x,78,44); hb+=b+T((x+x2)/2,176,f'{n} table{"s" if n>1 else ""}: {2+4*n} people',28); x=x2+150
hexsvg=svg(int(x-40),190,hb,'Hexagon tables in a row with a seat on each free side: 1 table seats 6, 2 tables seat 10, 3 tables seat 14')
W7=[150]+[80]*6
body=h2('Tables in a row: make a table')+pin(128,215,1664,hexsvg)
body+=trow(128,420,['Tables','1','2','3','4','5','6'],W7,None,True,32)+trow(128,490,['People','6','10','14','','',''],W7,None,False,32)
body+=step(1,'Each new table adds 4 people: 6, 10, 14 …',left=1080,top=420,width=712,size=30)
body+=trow(128,490,['People','6','10','14','18','22','26'],W7,'rise',False,32)
body+=step(2,'30 people? Keep going: 26, 30. That is 7 tables.',left=1080,top=540,width=712,size=30)
body+=qrow(128,700,1250,'Your turn:','A pizza has 8 equal slices. Ali eats 3/8. Ben eats 1 slice more than Ali. What fraction is left?',30)+answer(1420,700,372,'1/8')
put('p2l10-teachgrow',sec('p2l10-teachgrow','55–57 MIN',body,'Teach before worksheet page 2 (Q6 towers of cubes, a growing pattern; Q5 fractions). Ask first: "How many people at 1 table? 2 tables? Why not 12 for 2 tables?" (the sides that touch lose their seats). Click step 1: the rule is add 4. Then the table fills in: 18, 22, 26. Step 2: "How many tables for 30 people? I keep the table going: 26, then 30 at 7 tables." '
 'Your turn (fractions, like Q5): Ali eats 3 slices, Ben eats 4 slices, 3 + 4 = 7 slices, so 1 slice of 8 is left: 1/8. Common mistake: Ben eats 1/8 (reading "1 slice more" as "1 slice"). The worksheet uses towers of cubes (4, 8, 12 …): do not give the rule away.'))

put('p2l10-ws2',ws_preview('p2l10-ws2','57–69 MIN','Worksheet page 2: on your own',[('Q4','Logic grid. Tick one, cross the rest of the row and column.'),('Q5','Cake in 10 pieces. Draw it and shade each child’s pieces.'),('Q6','Towers of cubes. Fill the table and find the rule.')],'Finished early? Stretch and Challenge come next.','Children work alone. Note who needs a short catch-up. Q4: check children start with clue 1 and cross out the rest of Siti’s row and the walk column.'))
put('p2l10-ws2ans',check_slide('p2l10-ws2ans','69–72 MIN','Page 2: check together',[('Q4','Ali car,  Ben MRT,  Mei bus,  Siti walks'),('Q5','a) 5/10   b) 2/10   c) Mei, Ali, Ben'),('Q6','a) 32 cubes (Tower 8)   b) Tower 9')],
 'Click each answer after a child explains how they started. Q4: Clue 1: Siti walks (cross the rest). Clue 2: Ben is not bus or car, and walk is taken, so Ben goes by MRT. Clue 3: Mei is not car; walk and MRT are taken, so Mei goes by bus. Ali gets the car. Exactly one answer: each clue was needed. '
 'Q5: Ali 3 pieces, Mei 3 + 2 = 5 pieces, Ben 10 − 8 = 2 pieces. Q6: add 4 each tower: 4, 8, 12, 16, 20, 24, 28, 32, so Tower 8 has 32 cubes; 36 cubes is Tower 9 (4 × 9, or keep adding 4: 32, 36).'))

# ---------- stretch (new) ----------
st=[('1.','Use three of the cards 4, 0, 6, 2. What is the greatest 3-digit number you can make that is less than 500?'),('2.','A farm has ducks and rabbits. There are 10 heads and 26 legs. How many rabbits?'),('3.','Siti, Ravi and Lin sit in a row of 3 chairs. Lin is not at either end. Siti is on the left of Ravi. Who sits on the right end?')]
put('p2l10-stretch',sec('p2l10-stretch','For early finishers',h2('Stretch')+numcards(st,36),'For children who finish early. Answers: 1) 462 (the hundreds digit must be 4 or 2 to be less than 500; take 4, then the biggest tens and ones left: 6 and 2). 2) 3 rabbits and 7 ducks (table: 0 rabbits 20 legs, 1: 22, 2: 24, 3: 26 ✓). 3) Ravi (Lin is in the middle, so Siti and Ravi are at the ends; Siti is on the left, so Ravi is on the right end).'))

# ---------- challenge ----------
ch=[('1.','Ali, Ben, Mei and Siti each have one coin: 10¢, 20¢, 50¢ or $1. Mei has more money than Ali but less than Ben. Ben does not have the $1 coin. Who has which coin?'),('2.','At a hawker centre, chicken rice costs $4 a plate and noodles cost $3 a bowl. Ravi’s family buys 7 dishes for $25. How many plates of chicken rice do they buy? What is the smallest total 7 dishes can cost? The biggest? Can 7 dishes cost $30? Can they cost EVERY whole-dollar amount in between?')]
put('p2l10-challenge',sec('p2l10-challenge','Challenge',h2('Challenge')+numcards(ch,36),'Pairs try first, then use the "see it" slide if stuck, then the walk-through. Answers: 1) Ali 10¢, Mei 20¢, Ben 50¢, Siti $1. 2) 4 plates of chicken rice (and 3 bowls of noodles). Extension: the smallest total is $21 (all noodles) and the biggest is $28 (all chicken rice), so $30 is impossible; each swap of a bowl for a plate adds exactly $1, so every whole dollar from $21 to $28 is possible. Both are on the workbook Think Harder page (Challenge 6 and 7). A program check confirms each has exactly one answer.'))
coins=[('10¢',40),('20¢',46),('50¢',54),('$1',60)]
cl=f'<line x1="40" y1="120" x2="720" y2="120" stroke="{NAVY}" stroke-width="5"/><polygon points="740,120 716,106 716,134" fill="{NAVY}"/>'+T(40,212,'less',28,MUTED,'start')+T(740,212,'more',28,MUTED,'end')
cl+=''.join(f'<circle cx="{100+k*170}" cy="120" r="{r}" fill="#E5E9F2" stroke="{NAVY}" stroke-width="4"/>'+T(100+k*170,131,l,30) for k,(l,r) in enumerate(coins))
cl+=''.join(f'<rect x="{30+k*190}" y="236" width="150" height="56" rx="12" fill="{WHITE}" stroke="{NAVY}" stroke-width="3" stroke-dasharray="8 6"/>'+T(105+k*190,274,n,30) for k,n in enumerate(['Ali','Ben','Mei','Siti']))
q1=svg(780,300,cl,'Four coins in order from less to more money, and four name cards to place: Ali, Ben, Mei, Siti')
pl=''.join(f'<circle cx="{60+k*104}" cy="70" r="44" fill="{WHITE}" stroke="{NAVY}" stroke-width="4"/>'+T(60+k*104,82,'?',36,RED) for k in range(7))
pl+=f'<rect x="40" y="150" width="300" height="70" rx="12" fill="{SOFT}" stroke="{NAVY}" stroke-width="3"/>'+T(190,196,'chicken rice $4',30)+f'<rect x="400" y="150" width="300" height="70" rx="12" fill="{SKY}" stroke="{NAVY}" stroke-width="3"/>'+T(550,196,'noodles $3',30)+T(380,280,'7 dishes, $25 altogether',32,TEAL)
q2=svg(780,300,pl,'Seven empty plates, chicken rice costs 4 dollars and noodles cost 3 dollars, 25 dollars altogether')
body=h2('Challenge: see it',60)+'<div style="display:flex;gap:32px;align-items:flex-start">'+card(p('Q1: put the names in order',30,800,TEAL)+q1,extra='flex:1;min-width:0;padding:16px 24px')+card(p('Q2: what is on each plate?',30,800,TEAL)+q2,extra='flex:1;min-width:0;padding:16px 24px')+'</div>'
put('p2l10-chdiag',sec('p2l10-chdiag','Challenge',body,'Show after pairs have tried, or if they are stuck. The pictures show the problem, not the answer. Ask: Q1: Who has less than Mei? Who has more? Can Ben be the one with the least? Q2: If every plate were noodles, how much would it cost? What changes when one plate is chicken rice?'))
body=h2('Challenge: walk-through')+pin(128,230,800,p('Q1: draw it in order',34,800,TEAL))
for i,t in enumerate(['Ali < Mei < Ben: two people have less than Ben.','So Ben is not 10¢ or 20¢, and not $1: Ben has 50¢.','Ali and Mei share 10¢ and 20¢: Ali 10¢, Mei 20¢.','Siti has the $1 coin. Check both clues ✓']): body+=pin(128,300+i*140,800,p(t,30),'rise',WHITE)
body+=pin(992,230,800,p('Q2: make a table',34,800,TEAL))
for i,t in enumerate(['0 chicken rice, 7 noodles: $21.','Each swap to chicken rice adds $1: $22, $23, $24, $25.','4 swaps: 4 chicken rice and 3 noodles.','Check: $16 + $9 = $25, and 4 + 3 = 7 dishes ✓']): body+=pin(992,300+i*140,800,p(t,30),'rise',WHITE)
put('p2l10-chwalk',sec('p2l10-chwalk','Challenge',body,'Use after pairs have tried. Q1: draw a line from less to more and put Ali, Mei, Ben on it in that order (with gaps). Ben needs two coins smaller than his, so he has 50¢ or $1, and the clue says not $1. Q2: the same swap idea as chickens and goats: start with all noodles (7 × $3 = $21: count in 3s), each chicken rice instead of noodles adds $1, and we need $4 more.'))

put('p2l10-talk',talk_slide('p2l10-talk','Pick one puzzle and teach it to the group in two sentences: how you started it, and how you know your answer is right.','Minutes 72 to 80. Pairs talk for 90 seconds, then two volunteers share. One question. Listen for a clear start (I drew bars, I listed in order, I made a table) and a check (I put my answer back into the puzzle). Praise the reasons, not only the answers.'))
put('p2l10-exit',exit_slide('p2l10-exit','5 bicycles and tricycles have 13 wheels. How many tricycles? How did you start?','3 tricycles (9 + 4 = 13)','Minutes 80 to 88. No talking, no helping. Click to show the answer after the slips are in. Answer: 3 tricycles and 2 bicycles: 3 + 3 + 3 + 2 + 2 = 13. A table of 0, 1, 2, 3 tricycles works well (10, 11, 12, 13 wheels). Anyone who would like to may finish: "My favourite puzzle in the program was ____ because ____." Stamp the inquiry journal.','80–88 MIN'))
put('p2l10-end',(f'<section id="p2l10-end" data-transition="fade" style="background:{NAVY};color:{CREAM};font-family:{BF};padding:128px 128px 160px;display:flex;flex-direction:column;justify-content:center;gap:36px">\n'
 f'<p style="font-size:32px;font-weight:700;letter-spacing:4px;color:{YEL}">WELL DONE, INQUIRERS</p>\n<h1 style="font-family:{HF};font-size:128px;font-weight:600;line-height:1.05">Keep asking why</h1>\n'
 f'<p style="font-family:{HF};font-size:64px;font-weight:500;color:{YEL}">Notice it. Test it. Explain why.</p>\n<p style="font-size:36px;color:#C9D4EC">Certificates and a last stamp for every inquirer. See you in Primary 3!</p>\n'
 f'<p style="position:absolute;left:128px;bottom:64px;width:1400px;font-size:24px;color:#B7C3DD">{E(FOOT)}</p>\n<aside>{E("Minutes 87 to 90. Hand out certificates (about 20 seconds each). Say one specific thing each child did well, or say it in the open session; nothing is sent by private message. Volunteers may name a puzzle they enjoyed; nobody has to. Give parents the one-page summary from the tutor guide.")}</aside>\n</section>\n'))

p2gaps.add(S,10)
order=['p2l10-title','p2l10-warm1','p2l10-warm2','p2l10-explore1','p2l10-cards','p2l10-explore2','p2l10-we1','p2l10-we2','p2l10-try2','p2l10-we3','p2l10-key','p2l10-break','p2l10-teachgraph','p2l10-ws1','p2l10-ws1ans','p2l10-teachlogic','p2l10-teachgrow','p2l10-ws2','p2l10-ws2ans','p2l10-stretch','p2l10-challenge','p2l10-chdiag','p2l10-chwalk','p2l10-talk','p2l10-exit','p2l10-end']
order=p2gaps.order(order,10)
write_deck('Math Inquirers P2: Lesson 10 – Puzzle Day',order,{'s1':{'description':'Warm-up and explore','start':'p2l10-title'},'s2':{'description':'Teach: how to start a puzzle (draw it, list it, make a table)','start':'p2l10-we1'},'s3':{'description':'Worksheet with teaching before each page','start':'p2l10-break'},'s4':{'description':'Think harder, go further, talk, exit and certificates','start':'p2l10-stretch'}})
