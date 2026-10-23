"""Math Inquirers P4, Lesson 10: Puzzle Day (mixed heuristics). Writes split/p4l10/project (deck.json + slides/*.html).
Every answer was checked with a script; each logic puzzle was checked against every arrangement (exactly one answer)."""
import json,os,sys,datetime
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,H)
import slidekit
from slidekit import *
slidekit.FOOT='Math Inquirers P4 Holiday Program  •  Notice it. Test it. Explain why.'
D=os.path.join(H,'..','split','p4l10','project'); os.makedirs(os.path.join(D,'slides'),exist_ok=True)
S={}
def put(i,h): S[i]=h
RED='#D64545'; FOOTX=slidekit.FOOT

# ---------- shared slide shapes (same look as the P1/P2 decks) ----------
def title_slide(sid,label,title,topic,today,notes,kicker='TODAY WE WILL'):
    return (f'<section id="{sid}" data-transition="fade" style="background:{NAVY};color:{CREAM};font-family:{BF};padding:128px 128px 160px;display:flex;flex-direction:column;justify-content:center;gap:36px">\n'
            f'<p style="font-size:32px;font-weight:700;letter-spacing:4px;color:{YEL}">{E(label)}</p>\n'
            f'<h1 style="font-family:{HF};font-size:128px;font-weight:600;line-height:1.05">{E(title)}</h1>\n'
            f'<p style="font-size:44px;color:#C9D4EC">{E(topic)}</p>\n'
            f'<div style="background:#26385F;border-radius:24px;padding:40px;display:flex;flex-direction:column;gap:12px"><p style="font-size:28px;font-weight:700;letter-spacing:3px;color:{YEL}">{E(kicker)}</p><p style="font-size:44px;font-weight:600">{E(today)}</p></div>\n'
            f'<p style="position:absolute;left:128px;bottom:64px;width:1400px;font-size:24px;color:#B7C3DD">{E(FOOTX)}</p>\n<aside>{E(notes)}</aside>\n</section>\n')
def break_slide(sid,time,text,notes):
    notes=notes.replace('Four minutes.',__import__('p4_budget').break_lead(10),1)
    return (f'<section id="{sid}" data-transition="fade" style="background:{TEAL};color:{CREAM};font-family:{BF};padding:128px 128px 160px;display:flex;flex-direction:column;justify-content:center;gap:36px">\n'
            f'<p style="font-size:32px;font-weight:700;letter-spacing:4px;color:{YEL}">{E(time)}</p>\n'
            f'<h2 style="font-family:{HF};font-size:110px;font-weight:600;line-height:1.05">Brain break</h2>\n'
            f'<p style="font-size:36px;color:#D7EFEA">First, one minute: a drink of water and a toilet stop if you need one.</p>\n<p style="font-size:48px;font-weight:600">{E(text)}</p>\n<p style="font-size:36px;color:#D7EFEA">Then back to our seats on time.</p>\n'
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
def txt(x,y,s,size=30,fill=NAVY,anchor='middle',weight=700,font='Nunito Sans, Arial'):
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" fill="{fill}" font-family="{font}">{E(str(s))}</text>'
def tick(cx,cy,col=TEAL): return f'<path d="M{cx-18} {cy} L{cx-5} {cy+14} L{cx+20} {cy-16}" fill="none" stroke="{col}" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>'
def cross(cx,cy,col=RED): return f'<path d="M{cx-15} {cy-15} L{cx+15} {cy+15} M{cx+15} {cy-15} L{cx-15} {cy+15}" stroke="{col}" stroke-width="7" stroke-linecap="round"/>'

# ---------- 1. title ----------
put('p4l10-title',title_slide('p4l10-title','LESSON 10  •  WEEK 5','Puzzle Day','Mixed heuristics',
 'Choose a way into tricky puzzles: guess and check, suppose, work backwards, and logic. Then check every fact.',
 'Objective: Choose a way into a non-routine problem (guess and check with a table, suppose they are all the same, work backwards, a logic grid, draw it) and use it on competition-style puzzles, checking every answer against every fact. '
 'Thinking strategies today: GUESS AND CHECK WITH A TABLE, SUPPOSE (heads and legs), WORK BACKWARDS, LOGIC GRID, DRAW IT. '
 'Materials: Four puzzle cards (A to D) for the explore stations, mini whiteboards, counters or cubes, certificates, stamps. '
 'Online: pairs go to breakout rooms with one puzzle card each and report back; the tutor ticks and crosses the logic grid on the slide as children call out. '
 'Time plan: (written by rebuild/p4_fix.py from rebuild/p4_budget.py).'))

# ---------- 2. warm-up: who am I? ----------
CW,CH=56,46
def gridsvg(label='A 1 to 100 grid'):
    d=' '.join([f'M2 {2+r*CH} H{2+10*CW}' for r in range(11)]+[f'M{2+c*CW} 2 V{2+10*CH}' for c in range(11)])
    g=f'<rect x="2" y="2" width="{10*CW}" height="{10*CH}" fill="{WHITE}"/><path d="{d}" stroke="{NAVY}" stroke-width="2"/>'
    g+=''.join(txt((n-1)%10*CW+2+CW/2,(n-1)//10*CH+2+32,n,24,NAVY,weight=700) for n in range(1,101))
    return svgwrap(564,464,label,g)
def overlay(nums,col,label,ring=False):
    g=''
    for n in nums:
        r,c=(n-1)//10,(n-1)%10; x,y=c*CW+2,r*CH+2
        g+=(f'<circle cx="{x+CW/2}" cy="{y+CH/2}" r="25" fill="none" stroke="{col}" stroke-width="6"/>' if ring else f'<rect x="{x}" y="{y}" width="{CW}" height="{CH}" fill="{col}" fill-opacity=".55" stroke="{NAVY}" stroke-width="2"/>'+txt(x+CW/2,y+32,n,24,NAVY))
    return svgwrap(564,464,label,g)
m7=[n for n in range(10,100) if n%7==0]
body=h2('Warm-up: who am I?')+pin(128,240,564,gridsvg(label='A 1 to 100 grid'))
clues=['Clue 1: I am a 2-digit number.','Clue 2: I am in the 7 times table.','Clue 3: My digits add up to 10.','Clue 4: I am odd.']
body+=pin(760,240,1032,p(clues[0],34,700),'rise',WHITE,20,'16px 26px')
body+=pin(760,340,1032,p(clues[1],34,700),'rise',WHITE,20,'16px 26px')
body+=pin(128,240,564,overlay(m7,YEL,'2-digit numbers in the 7 times table shaded'),'fade')
body+=pin(760,440,1032,p(clues[2],34,700),'rise',WHITE,20,'16px 26px')
body+=pin(128,240,564,overlay([28,91],RED,'28 and 91 circled',True),'fade')
body+=pin(760,540,1032,p(clues[3],34,700),'rise',WHITE,20,'16px 26px')
body+=answer(760,660,1032,'I am 91.  (28 is even.)')
body+=pin(760,780,1032,p('Every clue crosses numbers out. Clue 2 did the most work.',30,700),'fade',SOFT,20,'16px 26px')
put('p4l10-warm1',sec('p4l10-warm1','6.5–8.5 MIN',body,
 'Minutes 6.5 to 8.5 (one short round, about 90 seconds: the Sneak-peek puzzles came first). Who am I? Children have a 1 to 100 grid (or a whiteboard list). Click one clue at a time; after each, children cross out every number that no longer fits. Clicks: clue 1, clue 2, the 7 times table shades (14, 21, 28 … 98), clue 3, 28 and 91 are circled, clue 4, the answer, the question. '
 'Clue 3 check: 1 + 4, 2 + 1, 2 + 8 = 10 ✓, 3 + 5, 4 + 2, 4 + 9, 5 + 6, 6 + 3, 7 + 0, 7 + 7, 8 + 4, 9 + 1 = 10 ✓, 9 + 8. So 28 and 91; clue 4 leaves 91. '
 'Clue 2 did the most work: it left only 13 numbers. Say it as a statement; no follow-up question.'))

# ---------- 3. quick questions ----------
qs=[('1.','Buses every 6 min and every 8 min leave together at 9:00. Next together?','9:24'),('2.','Round 45 678 to the nearest thousand.','46 000'),('3.','3/4 of 24 = ?','18')]
body=h2('Quick questions')+''.join(qrow(128,250+i*125,1250,a,b,34) for i,(a,b,c) in enumerate(qs))+''.join(answer(1420,250+i*125,372,c) for i,(a,b,c) in enumerate(qs))
put('p4l10-warm2',sec('p4l10-warm2','8.5–11.5 MIN',body,'Minutes 8.5 to 11.5. Three questions from earlier lessons, about 30 seconds each. Whiteboards up together, then click. No follow-up questions. 1) 9:24: the first common multiple of 6 and 8 is 24 (Factor Hunters). 2) 46 000: the hundreds digit is 6, so round up (Big Number Puzzles). 3) 24 ÷ 4 = 6, 6 × 3 = 18 (Fraction Frontier). The other two (0.6 × 4 = 2.4; turn clockwise from N to SW, 225°) are in the Weekly Dose of Thinking Math.'))

# ---------- 4. explore ----------
cards=[('A','Guess and check','Two next-door numbers','multiply to 210.'),('B','Heads and legs','Spiders and beetles:','10 bugs, 68 legs.'),('C','Work backwards','Double it, add 7.','I get 43.'),('D','Logic','Ali, Mei, Ravi: cat,','dog, fish. Who has what?')]
g=''
for i,(l,t,a,b) in enumerate(cards):
    x=10+i*398
    g+=f'<rect x="{x}" y="10" width="378" height="196" rx="18" fill="{(SOFT if i%2==0 else SKY) if i<2 else "#E4E7EE"}" stroke="{NAVY}" stroke-width="4"'+('' if i<2 else ' stroke-dasharray="12 8"')+'/>'+f'<circle cx="{x+44}" cy="54" r="30" fill="{YEL}" stroke="{NAVY}" stroke-width="4"/>'+txt(x+44,66,l,34,NAVY,font='Fredoka, Arial')
    g+=txt(x+86,64,t,28,TEAL,'start',800)+txt(x+189,134,a,26,NAVY,weight=600)+txt(x+189,174,b,26,NAVY,weight=600)
steps=''.join(f'<li>{E(s)}</li>' for s in ['Two live puzzle cards, A and B. Pairs do both. Cards C and D (grey) are ★ take-home.','Read the card aloud with your partner.','Try something: a guess, a drawing or a table.','Write the answer AND how you got it.'])
body=h2('Explore: puzzle cards A and B')+card(chip('EXPLORE')+f'<ol style="font-size:32px;font-weight:600;padding-left:52px;display:flex;flex-direction:column;gap:6px">{steps}</ol>')
body+=card(svgwrap(1600,216,'Four puzzle cards: A guess and check and B heads and legs are live; C work backwards and D logic are take-home',g),extra='padding:20px 32px')
put('p4l10-explore1',sec('p4l10-explore1','11.5–21.5 MIN',body,'Minutes 11.5 to 21.5. Pairs do two live cards, A then B (online: one breakout room for the whole explore, about 60 seconds each way, closed by a 60-second timer). Cards C and D are take-home (★): they are the first Think harder tasks to try at home. Full cards: A) Two next-door numbers multiply to make 210. What are they? B) Spiders have 8 legs and beetles have 6 legs. 10 bugs have 68 legs altogether. How many spiders? C) I double a number and add 7. I get 43. What is my number? D) Ali, Mei and Ravi each have a different pet: a cat, a dog and a fish. Ali\'s pet has no fur. Mei\'s pet does not bark. Who has which pet? Answers: A) 14 and 15. B) 4 spiders and 6 beetles. C) 18. D) Ali fish, Mei cat, Ravi dog. Hands-on is about 6 minutes for the two live cards. Do not teach the methods yet: let pairs try their own way.'))
body=h2('Explore: talk about it')+numcards([('1.','How did you start card B?'),('2.','Which card was hardest? What helped?')],40)
put('p4l10-explore2',sec('p4l10-explore2','21.5–24.5 MIN',body,'Minutes 21.5 to 24.5. Pencils down (or when the 60-second timer closes the rooms), then gather pairs and collect ways of starting. Two debrief questions only: write them on the board in children\'s words ("I guessed and changed it", "I pretended they were all beetles", "I started at 43"). Answers: 1) Suppose all 10 are beetles: 60 legs, 8 short; each spider instead of a beetle adds 2 legs, so 4 spiders. Or guess and check with a table. 2) Open. The third question (could any card have two answers?) is not asked: A has only 14 × 15 = 210 and C undoing gives one number. The next slides name the four ways in.'))

# ---------- 5. teach: four ways in ----------
def icon(kind):
    if kind=='table':
        b=''.join(f'<rect x="{20+c*110}" y="{10+r*36}" width="110" height="36" fill="{YEL if r==0 else WHITE}" stroke="{NAVY}" stroke-width="3"/>' for r in range(3) for c in range(3))
    elif kind=='same':
        b=''.join(f'<circle cx="{40+i*56}" cy="60" r="22" fill="{SKY}" stroke="{NAVY}" stroke-width="4"/>' for i in range(6))+f'<circle cx="{40+5*56}" cy="60" r="22" fill="{YEL}" stroke="{NAVY}" stroke-width="4"/>'
    elif kind=='back':
        b=f'<rect x="20" y="30" width="90" height="60" rx="12" fill="{SKY}" stroke="{NAVY}" stroke-width="4"/><rect x="250" y="30" width="90" height="60" rx="12" fill="{YEL}" stroke="{NAVY}" stroke-width="4"/><path d="M240 60 L130 60" stroke="{TEAL}" stroke-width="7" stroke-dasharray="14 8"/><polygon points="118,60 140,46 140,74" fill="{TEAL}"/>'
    else:
        b=''.join(f'<rect x="{30+c*70}" y="{8+r*36}" width="70" height="36" fill="{WHITE}" stroke="{NAVY}" stroke-width="3"/>' for r in range(3) for c in range(3))+tick(65,26)+cross(135,26)+cross(205,26)
    return svgwrap(360,118,{'table':'Icon: a table of tries','same':'Icon: a row of the same things, one swapped','back':'Icon: an arrow going backwards','grid':'Icon: a logic grid with a tick and crosses'}[kind],b)
ways=[('Guess and check','table','Try, then use a table: too big or too small?'),('Suppose','same','Pretend they are all the same, then swap.'),('Work backwards','back','You know the END. Undo each step.'),('Logic grid','grid','Who has what? Tick and cross.')]
body=h2('Four ways in')+p('Stuck? Do not stare at it. Pick a way in and start.',34,600,MUTED)
for i,(t,k,u) in enumerate(ways):
    body+=pin(128+i*424,320,392,p(t,38,800,TEAL)+icon(k)+p(u,30,600),'rise',WHITE,24,'22px 22px','box-sizing:border-box;height:400px')
body+=pin(128,760,1664,p('Whatever way you choose: check your answer against EVERY fact in the question.',34,700),'fade',SOFT,20,'18px 28px')
put('p4l10-teach1',sec('p4l10-teach1','24.5–25.5 MIN',body,'Teach: the idea and why. "Mathematicians do not know the answer straight away. They know ways to START." Click each card and link it to the explore stations: A was guess and check, B was suppose, C was work backwards, D was a logic puzzle. A puzzle can often be started more than one way: B can also be done by guess and check. The next slides show each way in action, with new numbers.'))

# ---------- 6. worked example: guess and check ----------
W3=[230,230,360]
body=h2('Guess and check with a table')+card(p('Two next-door numbers (like 7 and 8) multiply to make 342. What are they?',38,700))
body+=trow(128,390,['Try','Product','Result'],W3,None,True,34)
rows=[('20 × 21','420','too big: go down'),('17 × 18','306','too small: go up'),('18 × 19','342','just right ✓')]
expl=['Estimate: 20 × 20 = 400, near 342. Try 20 × 21.','420 is too big. Jump down: 17 × 18.','306 is too small. The answer is between: 18 × 19.']
for i,((a,b,c),e) in enumerate(zip(rows,expl)):
    body+=pin(1100,390+i*110,692,p(e,30,700),'rise',WHITE,20,'16px 24px')+trow(128,480+i*90,[a,b,c],W3,'rise',False,34)
body+=answer(128,770,1664,'18 and 19.  Each try tells you which way to go next.')
put('p4l10-we1',sec('p4l10-we1','25.5–27 MIN',body,'Click: each reason on the right, then its row in the table. Think-aloud: "I could guess at random, but a table is smarter: every try tells me whether to go up or down. 20 × 20 is 400, so the numbers are a bit less than 20. 20 × 21 = 420, too big. 17 × 18 = 306, too small. So 18 × 19: 18 × 19 = 342." Worked check: 18 × 19 = 18 × 20 − 18 = 360 − 18 = 342. Worksheet Q1 uses a different number.'))

# ---------- 8. worked example: suppose ----------
def cycles(n,tri=0):
    g=''
    for i in range(n):
        x=20+i*104
        g+=f'<circle cx="{x+18}" cy="70" r="16" fill="{WHITE}" stroke="{NAVY}" stroke-width="5"/><circle cx="{x+66}" cy="70" r="16" fill="{WHITE}" stroke="{NAVY}" stroke-width="5"/><path d="M{x+18} 70 L{x+42} 34 L{x+66} 70" fill="none" stroke="{TEAL}" stroke-width="5"/>'
        if i>=n-tri: g+=f'<circle cx="{x+42}" cy="22" r="16" fill="{YEL}" stroke="{NAVY}" stroke-width="5"/>'
    return g
body=h2('Suppose they are all the same')+card(p('15 bicycles and tricycles have 38 wheels altogether. How many tricycles?',38,700))
body+=pin(128,380,1600,svgwrap(1600,100,'15 cycles drawn as bicycles with 2 wheels each',cycles(15)),None)
body+=step(1,'Suppose ALL 15 are bicycles: 15 × 2 = 30 wheels.',top=510,size=32)
body+=step(2,'We need 38. 38 − 30 = 8 wheels short.',top=610,size=32)
body+=step(3,'Swap a bicycle for a tricycle: 1 more wheel. 8 swaps.',top=710,size=32)
body+=pin(128,380,1600,svgwrap(1600,100,'8 of the cycles get a third wheel',cycles(15,8)),'fade')
body+=answer(128,810,1664,'8 tricycles, 7 bicycles.  Check: 14 + 24 = 38 wheels, 15 cycles ✓')
put('p4l10-we2',sec('p4l10-we2','27–28.5 MIN',body,'Click the steps, then 8 cycles get a third wheel, then the answer. Think-aloud: "Two facts: 15 cycles and 38 wheels. I keep the 15 and pretend they are all bicycles. That gives 30 wheels: 8 too few. Every time I change a bicycle into a tricycle I add exactly 1 wheel, so I change 8 of them." Check BOTH facts: 7 + 8 = 15 cycles, 7 × 2 + 8 × 3 = 38 wheels. Point out: for chickens and goats, each swap adds 2 legs, so you divide the shortfall by 2. Worksheet Q2 is a heads-and-legs puzzle.'))
put('p4l10-try2',try_slide('p4l10-try2','28.5–29.5 MIN • OPTIONAL','Your turn: suppose','All the same first. How far off? What does one swap add?',[('a','Ducks and cows: 10 heads, 28 legs. How many cows?','4 cows'),('b','12 coins, all 10¢ or 20¢, make $1.80. How many 20¢?','6'),('c','Cars and bicycles: 9 of them, 26 wheels. Cars?','4 cars')],'Whiteboards. a) All ducks: 20 legs, 8 short, each cow adds 2: 4 cows (and 6 ducks; 12 + 16 = 28). b) All 10¢: 120¢, 60¢ short, each 20¢ adds 10¢: six 20¢ and six 10¢ (120 + 60 = 180). c) All bicycles: 18 wheels, 8 short, each car adds 2: 4 cars and 5 bicycles (16 + 10 = 26).',34))

# ---------- 10. worked example: work backwards ----------
body=h2('Work backwards: start at the end')+card(p('Siti spent half her money on a book. Then she spent $4 on lunch. She had $11 left. How much did she have at first?',36,700))
body+=pin(128,400,1664,machine([('?','q'),('half','op'),('− $4','op'),('$11','res')],back='go backwards: undo each step'),None)
body+=step(1,'Start at the end and undo the last step: − $4 becomes + $4.  $11 + $4 = $15.',top=660,size=32)
body+=step(2,'Undo "half" by doubling: $15 × 2 = $30.',top=760,width=1100,size=32)
body+=answer(1290,760,502,'At first: $30')
put('p4l10-we3',sec('p4l10-we3','29.5–30.5 MIN',body,'Think-aloud: "I know the END, $11, not the start. So I walk backwards through the machine, undoing each step, LAST step first. She took away $4, so I add it back: $15. She halved her money, so I double: $30." Check forwards: half of $30 is $15, $15 − $4 = $11 ✓. Common mistakes: undoing in the wrong order (11 × 2 = 22, 22 + 4 = 26: check forwards and it fails), or taking away 4 again. Worksheet Q3 has three steps to undo.'))

body=h2('Key idea: pick a way in')+card(p('Guess and check with a table, suppose they are all the same, or work backwards from the end.',44,700))+card(p('Then check your answer against every fact in the question.',38,600,MUTED))
put('p4l10-key',sec('p4l10-key','30.5–31 MIN',body,'Say the key idea together. Common mistakes to watch for during the worksheet: (1) Guessing at random instead of using a table, so each try does not tell them whether to go up or down. (2) Working backwards but doing the same operation again (taking away 4 instead of adding 4), or undoing the steps in the wrong order. (3) Queues: adding the two positions (7th and 12th makes 19) and counting the person twice; logic puzzles: stopping before every clue has been used.'))
put('p4l10-break',break_slide('p4l10-break','31–34.5 MIN','Heads and legs! The tutor calls "3 chickens and 2 goats": stamp that many legs. Then "5 animals, 16 legs": who can say the animals?','Four minutes. 3 chickens and 2 goats: 6 + 8 = 14 stamps. 5 animals with 16 legs: all chickens is 10 legs, 6 short, each goat adds 2, so 3 goats and 2 chickens (12 + 4 = 16 ✓). Online: children stamp or clap in place on camera.'))

# ---------- worksheet page 1 ----------
put('p4l10-ws1',ws_preview('p4l10-ws1','34.5–51 MIN','Worksheet page 1: with your partner',[('Q1','Pairs: part (a), guess and check. Part (b) is ★ take-home.'),('Q2','Heads and legs. Suppose they are all chickens first.'),('Q3','On your own, first: work backwards. Undo the last step first.')],'Stuck? Name your way in to your partner before you start.','Minutes 34.5 to 51. Pairs do Q1a and Q2 (about 9 minutes of work). Q1b (all the ways to buy pens and notebooks) is a ★ take-home question. Q3 (working backwards) is the first question each child does on their own, at the start of page 2 time; its answer is checked with page 2. Walk around. Ask "What is your way in?" and "Does it fit every fact?" before giving any help.'))
put('p4l10-ws1ans',checks('p4l10-ws1ans','51–52.5 MIN','Page 1: check together',[('Q1','a) 23 and 24   b) ★ take-home: 9 pens + 2 notebooks, or 2 pens + 6 notebooks'),('Q2','a) 36; 14 short   b) 2; 7 goats, 11 chickens   c) 11 cars')],
 'Click each answer after a pair explains their way in. Q1a: 20 × 20 = 400 and 25 × 25 = 625, so try 23 × 24 = 552 ✓. Q1b: money left for pens with 1 to 7 notebooks is $43, $36, $29, $22, $15, $8, $1; only $36 (9 pens) and $8 (2 pens) can be paid with $4 pens. Q2: 50 − 36 = 14, 14 ÷ 2 = 7 goats; check 11 × 2 + 7 × 4 = 50. Q2c: all motorcycles 48 wheels, 22 short, 11 cars.',gapy=170))

# ---------- teach: logic grid ----------
SP=['Swim','Badminton','Football']; KN=['Ben','Siti','Ravi']
GX,GY,CWd,CHd=170,60,180,90
def lg(marks=(),label='Logic grid'):
    g=''
    if not marks:
        for c,s in enumerate(SP): g+=f'<rect x="{GX+c*CWd}" y="0" width="{CWd}" height="{GY}" fill="{YEL}" stroke="{NAVY}" stroke-width="3"/>'+txt(GX+c*CWd+CWd/2,42,s,28)
        for r,k in enumerate(KN):
            g+=f'<rect x="0" y="{GY+r*CHd}" width="{GX}" height="{CHd}" fill="{SOFT}" stroke="{NAVY}" stroke-width="3"/>'+txt(GX/2,GY+r*CHd+56,k,32)
            for c in range(3): g+=f'<rect x="{GX+c*CWd}" y="{GY+r*CHd}" width="{CWd}" height="{CHd}" fill="{WHITE}" stroke="{NAVY}" stroke-width="3"/>'
    for (r,c,m) in marks:
        cx,cy=GX+c*CWd+CWd/2,GY+r*CHd+CHd/2
        g+=tick(cx,cy) if m else cross(cx,cy)
    return svgwrap(GX+3*CWd+4,GY+3*CHd+4,label,g)
body=h2('Logic grid: tick and cross')+card(p('Ben, Siti and Ravi each play a different sport. Clue 1: Siti does not play football or badminton. Clue 2: Ben does not play football.',34,700))
body+=pin(128,420,714,lg(label='Empty logic grid: Ben, Siti, Ravi against swimming, badminton, football'),None)
body+=step(1,'Clue 1: cross Siti’s football and badminton. Only swimming is left: tick it. Nobody else swims: cross.',left=900,top=420,width=892,size=30)
body+=pin(128,420,714,lg([(1,2,0),(1,1,0),(1,0,1),(0,0,0),(2,0,0)],'Siti ticked for swimming; crosses for her other sports and for the others swimming'),'fade')
body+=step(2,'Clue 2: cross Ben’s football. Ben’s only box left is badminton.',left=900,top=580,width=892,size=30)
body+=pin(128,420,714,lg([(0,2,0),(0,1,1),(2,1,0)],'Ben ticked for badminton'),'fade')
body+=step(3,'Ravi: football is the only box left. Every row and column has one tick ✓',left=900,top=730,width=892,size=30)
body+=pin(128,420,714,lg([(2,2,1)],'Ravi ticked for football'),'fade')
put('p4l10-teachlogic',sec('p4l10-teachlogic','52.5–54 MIN',body,'Teach before worksheet page 2 (Q4 is a 4 by 4 grid). Click: step 1, then its ticks and crosses; step 2, then its marks; step 3, then the last tick. Think-aloud: "Each person has exactly one sport, and each sport has exactly one person. So when I tick a box, I can cross out the rest of that row AND that column." Answer: Ben badminton, Siti swimming, Ravi football. On the worksheet, children write ✓ for yes and X for no.'))

# ---------- teach: draw the queue ----------
def queue(n=12,me=5,lab=True):
    g=txt(40,40,'front',28,TEAL,'start',800)+txt(20+n*130-40,40,'back',28,TEAL,'end',800)
    for i in range(n):
        x=20+i*130+50
        g+=f'<circle cx="{x}" cy="100" r="34" fill="{YEL if i==me-1 else SKY}" stroke="{NAVY}" stroke-width="4"/>'
        if i==me-1: g+=txt(x,111,'Ali',28)
    return g
qg=svgwrap(1580,150,'A queue of 12 people with Ali 5th from the front',queue())
br=f'<path d="M50 20 L50 40 L{20+3*130+90} 40 L{20+3*130+90} 20" fill="none" stroke="{RED}" stroke-width="5"/>'+txt((50+20+3*130+90)/2,80,'4 in front',30,RED)
br+=f'<path d="M{20+5*130+10} 20 L{20+5*130+10} 40 L{20+11*130+90} 40 L{20+11*130+90} 20" fill="none" stroke="{RED}" stroke-width="5"/>'+txt((20+5*130+10+20+11*130+90)/2,80,'7 behind',30,RED)
body=h2('Draw it: queues')+card(p('Ali is 5th from the front and 8th from the back of a queue. How many people are in the queue?',36,700))
body+=pin(128,380,1580,qg,None)+pin(128,540,1580,svgwrap(1580,100,'Brackets: 4 people in front of Ali and 7 behind him',br),'fade')
body+=step(1,'5th from the front: 4 people in front of Ali. 8th from the back: 7 behind him.',top=660,size=32)
body+=step(2,'4 + 1 + 7 = 12 people. Not 5 + 8 = 13: that counts Ali twice!',top=760,width=1100,size=32)
body+=answer(1290,760,502,'12 people')
put('p4l10-teachqueue',sec('p4l10-teachqueue','54–55 MIN',body,'Teach before worksheet page 2 (Q5). Ask first: "Is it 13?" Many children add 5 + 8. Draw it: click the brackets, then the steps. Think-aloud: "If Ali is 5th, there are 4 people in front of him. If he is 8th from the back, there are 7 behind him. Ali himself is 1. 4 + 1 + 7 = 12." Quick check on the picture: count the circles: 12. Going the other way: 30 people, Mei 11th from the front: 19 behind her, so she is 20th from the back (30 − 11 + 1).'))

# ---------- teach: ages ----------
def bars():
    g=txt(10,60,'Mei',32,NAVY,'start')+f'<rect x="130" y="20" width="240" height="64" rx="6" fill="{SKY}" stroke="{NAVY}" stroke-width="4"/>'
    g+=txt(10,160,'Aunt',32,NAVY,'start')+f'<rect x="130" y="120" width="240" height="64" rx="6" fill="{SKY}" stroke="{NAVY}" stroke-width="4"/><rect x="370" y="120" width="240" height="64" rx="6" fill="{SKY}" stroke="{NAVY}" stroke-width="4"/>'
    g+=f'<path d="M640 20 L660 20 L660 184 L640 184" fill="none" stroke="{RED}" stroke-width="5"/>'+txt(680,112,'48 in 4 years',30,RED,'start')
    return svgwrap(900,200,'Bars in 4 years: Mei one bar, her aunt two bars, 48 altogether',g)
body=h2('Ages: everyone gets older together')+card(p('Mei and her aunt are 40 years old altogether. In 4 years, her aunt will be twice as old as Mei. How old is Mei now?',34,700))
body+=step(1,'In 4 years, BOTH are 4 years older: 40 + 4 + 4 = 48.',top=410,size=32)
body+=pin(128,520,900,bars(),'fade')
body+=step(2,'Then: 3 equal bars = 48. 1 bar = 16.',left=1080,top=520,width=712,size=32)
body+=step(3,'Mei will be 16, so now she is 16 − 4 = 12.',left=1080,top=630,width=712,size=32)
body+=answer(128,800,1664,'Mei is 12, her aunt is 28.  Check: 12 + 28 = 40;  16 and 32 ✓')
put('p4l10-teachages',sec('p4l10-teachages','55–56 MIN',body,'Teach before worksheet page 2 (Q6). Ask first: "In 4 years, how much older is the TOTAL?" Many say 4: but two people each get 4 years older, so the total grows by 8. Click step 1, the bars, steps 2 and 3, the answer. Think-aloud: "The twice-as-old fact is about the future, so I draw the bars in 4 years: Mei one bar, her aunt two bars, 48 altogether. 48 ÷ 3 = 16. That is Mei in 4 years, so now she is 12." Common mistake: forgetting to go back to NOW at the end.'))

# ---------- worksheet page 2 ----------
put('p4l10-ws2',ws_preview('p4l10-ws2','56–73 MIN','Worksheet page 2: on your own',[('Q4','The hawker centre logic grid. Tick one, cross the rest of its row and column.'),('Q5','Queues. Draw it. Do not count the person twice.'),('Q6','Ages. Everyone gets older together. Draw bars.')],'Finished early? Stretch and Challenge come next.','Children work alone. Note who still adds the two queue positions, and who forgets to go back to NOW in Q6.'))
put('p4l10-ws2ans',checks('p4l10-ws2ans','73–76 MIN','Page 2: check together',[('Q3','a) 52 marbles   b) 20'),('Q4','Ali nasi lemak,  Ben laksa,  Mei prata,  Siti chicken rice'),('Q5','a) 18 people   b) 15th from the back'),('Q6','Ben is 10, his father is 40')],
 'Click after a child explains. Q3a (done first on their own): 30 + 5 = 35, 35 − 9 = 26, 26 × 2 = 52; check forwards 26, 35, 30 ✓. Q3b: 21 × 2 = 42, 42 + 18 = 60, 60 ÷ 3 = 20. Q4: clue 1 gives Ali and Siti the two rice dishes; clue 2 means Ali has nasi lemak, so Siti has chicken rice; Ben and Mei have laksa and prata, and clue 3 gives Ben laksa, Mei prata. Q5a: 6 in front + Mei + 11 behind = 18. Q5b: 14 people behind Ben, so he is 15th from the back (20 − 6 + 1). Q6: in 5 years the total is 50 + 10 = 60; father 3 bars, Ben 1 bar: 4 bars = 60, 1 bar = 15; Ben will be 15, so he is 10 now. Check: 10 + 40 = 50; 15 and 45, and 45 = 3 × 15 ✓.',gapy=170))

# ---------- stretch / challenge ----------
from p4bank import th_items, th_notes, gf_numbers  # slide Think harder = the printed page (docs/audit/reaudit_fixes_p4.md)
st=th_items(10)
def numgrid(items,size=30): return '<div style="display:grid;grid-template-columns:1fr 1fr;gap:24px;align-items:stretch">'+''.join(card(p(f'<span style="color:{TEAL}">{a}</span>  {E(b)}',size,600,raw=True),extra='padding:24px 32px') for a,b in items)+'</div>'
put('p4l10-stretch',sec('p4l10-stretch','Optional, if you finish early',h2('Think harder')+numgrid(st,34),th_notes(10)))
ch=[('1.','A hawker centre has 15 tables. Some seat 4 people and some seat 6. There are 76 seats altogether. (a) How many tables seat 6? (b) What is the fewest and the most seats 15 tables could have? (c) Could the centre have 77 seats? Explain.'),('2.','Mei gave Ali half of her stickers and 2 more. Then she gave Ben half of the stickers left and 2 more. She had 5 left. How many did she have at first?')]
put('p4l10-challenge',sec('p4l10-challenge','Optional, if you finish early',h2('Go further')+numcards(ch,36),'Pairs try first, then use the "see it" slide if stuck, then the walk-through. These are Go further Q5 and Q6. Answers: 1) (a) 8 tables seat 6 (and 7 seat 4). (b) Fewest 60 (all seat 4), most 90 (all seat 6). (c) No: every table seats an even number of people, so the total is even and 77 is odd. The diagrams that follow show part (a). 2) 32 stickers.'))
g1=''
for i in range(15):
    r,c=i//5,i%5; x,y=40+c*140,20+r*110
    g1+=f'<rect x="{x}" y="{y}" width="120" height="80" rx="12" fill="{SKY}" stroke="{NAVY}" stroke-width="4"/>'+txt(x+60,y+52,'4 or 6?',26)
g1+=f'<rect x="60" y="370" width="640" height="80" rx="12" fill="{SOFT}" stroke="{NAVY}" stroke-width="3"/>'+txt(380,423,'15 tables, 76 seats',32)
g2=''
for i,(lab,fill) in enumerate([('?',WHITE),('?',WHITE),('5',YEL)]):
    y=20+i*170
    g2+=f'<rect x="260" y="{y}" width="240" height="90" rx="14" fill="{fill}" stroke="{NAVY}" stroke-width="4"/>'+txt(380,y+60,lab,46,RED if lab=='?' else NAVY,font='Fredoka, Arial')
    if i<2:
        g2+=f'<line x1="380" y1="{y+96}" x2="380" y2="{y+150}" stroke="{TEAL}" stroke-width="6"/><polygon points="380,{y+164} 366,{y+142} 394,{y+142}" fill="{TEAL}"/>'
        g2+=txt(410,y+134,['gives Ali half and 2 more','gives Ben half and 2 more'][i],26,TEAL,'start')
g2+=txt(140,65,'at first',28,MUTED,weight=600)+txt(140,405,'left',28,MUTED,weight=600)
body=h2('Go further: see it',60)+'<div style="display:flex;gap:32px;align-items:flex-start">'
body+=card(f'<p style="font-size:30px;font-weight:700;color:{TEAL}">Q1: 15 tables</p>'+svgwrap(760,470,'15 tables each marked 4 or 6 seats, 76 seats altogether',g1).replace('width:760px;height:470px;flex:none','width:100%;height:auto;display:block'),extra='flex:1;min-width:0;padding:20px 24px')
body+=card(f'<p style="font-size:30px;font-weight:700;color:{TEAL}">Q2: Mei’s stickers</p>'+svgwrap(760,470,'Mei starts with an unknown number, gives Ali half and 2 more, then gives Ben half and 2 more, and has 5 left',g2).replace('width:760px;height:470px;flex:none','width:100%;height:auto;display:block'),extra='flex:1;min-width:0;padding:20px 24px')+'</div>'
put('p4l10-chdiag',sec('p4l10-chdiag','Optional, if you finish early',body,'Show after pairs have tried the Challenge, or if they are stuck. The pictures show the problem, not the answer. Ask: In Q1, what if every table seated 4? In Q2, where do we know the number for sure? Which way in fits each puzzle? Answers are in the Challenge slide notes.'))
body=h2('Go further: walk-through')+pin(128,250,800,p('Q1: suppose all seat 4',38,800,TEAL))
for i,t in enumerate(['All 15 seat 4: 15 × 4 = 60 seats','76 − 60 = 16 seats short','A 6-seat table adds 2: 16 ÷ 2 = 8','8 seat 6, 7 seat 4.  Check: 48 + 28 = 76 ✓']): body+=pin(128,330+i*110,800,p(t,32),'rise',WHITE)
body+=pin(992,250,800,p('Q2: work backwards',38,800,TEAL))
for i,t in enumerate(['Left after Ben: 5. Add the 2 back: 7 = half','Before Ben: 7 × 2 = 14','Before Ali: (14 + 2) × 2 = 32','Check: 32 → gives 18 → 14 → gives 9 → 5 ✓']): body+=pin(992,330+i*110,800,p(t,32),'rise',WHITE)
put('p4l10-chwalk',sec('p4l10-chwalk','Optional, if you finish early',body,'Use after pairs have tried. Q1 is a heads-and-legs puzzle in disguise: tables are the heads, seats are the legs. Q2: "half and 2 more" is undone in two steps, last first: add the 2 back (that is the half she kept), then double. Many children add 2 and then halve, or take 2 away: check forwards to catch it. 32: Ali gets 16 + 2 = 18, 14 left. Ben gets 7 + 2 = 9, 5 left ✓.'))

# ---------- talk / exit / end ----------
body=h2('Talk time')+card(chip('TALK TIME',YEL,NAVY)+p('Which way in did you use most today? Pick one puzzle and teach it to the group in two sentences.',42,600))+card(p('Sentence starters:',34,400,MUTED)+p('“My way in was …”   “I tested it by …”   “I know because …”',38,600))
put('p4l10-talk',sec('p4l10-talk','76–79.5 MIN',body,'Minutes 76 to 79.5. Pair talk is 1 minute (no breakout rooms: children tell the grown-up beside them, or write one sentence), then share. Listen for the name of the strategy (guess and check, suppose, work backwards, logic grid, draw it) and a check against every fact. Only if volunteers dry up: "Which puzzle could be started in two different ways?" (heads and legs: suppose, or guess and check with a table). Praise the reasons, not only the answers.'))
body=h2('Exit ticket')+card(chip('EXIT TICKET')+p('A farm has ducks and goats: 12 heads and 34 legs. How many goats? Show your way in.',46,600))+card(p('Write your answer on a slip of paper. Show it to your tutor. Then collect your last stamp in your inquiry journal.',34,400))
put('p4l10-exit',sec('p4l10-exit','79.5–84 MIN',body,'Minutes 79.5 to 84. Answer: 5 goats (and 7 ducks). Suppose all ducks: 24 legs, 10 short, each goat adds 2 legs: 5 goats. Check: 14 + 20 = 34. Accept a guess-and-check table too. Extension: write your own heads-and-legs puzzle with exactly one answer and swap with a partner.'))
put('p4l10-end',f'<section id="p4l10-end" data-transition="fade" style="background:{NAVY};color:{CREAM};font-family:{BF};padding:128px 128px 160px;display:flex;flex-direction:column;justify-content:center;gap:36px">\n'
 f'<p style="position:absolute;right:128px;top:52px;font-size:26px;font-weight:800;letter-spacing:2px;color:{YEL};border:2px solid {YEL};border-radius:999px;padding:6px 22px">87.5–90 MIN</p>\n'
 f'<p style="font-size:32px;font-weight:700;letter-spacing:4px;color:{YEL}">WELL DONE, INQUIRERS</p>\n'
 f'<h1 style="font-family:{HF};font-size:128px;font-weight:600;line-height:1.05">Keep asking why</h1>\n'
 f'<p style="font-family:{HF};font-size:64px;font-weight:500;color:{YEL}">Notice it. Test it. Explain why.</p>\n'
 f'<p style="font-size:36px;color:#C9D4EC">Certificates and a last stamp for every inquirer. See you in Primary 5!</p>\n'
 f'<p style="position:absolute;left:128px;bottom:64px;width:1400px;font-size:24px;color:#B7C3DD">{E(FOOTX)}</p>\n<aside>{E("Minutes 87.5 to 90 (2.5 minutes, whole group, no per-child comments). Certificates and stamped journals are posted or sent after the lesson, each with a personal sentence the tutor wrote before the lesson. Live: three volunteers each name one puzzle and one way in (about 20 seconds each), then say one sentence about the group, then goodbye. Give parents the one-page summary from the tutor guide.")}</aside>\n</section>\n')

# ---------- write ----------
# ---------- fix pass (rebuild/p4_fix.py): sneak-peek puzzles, looking back, neutral names, go further, minute labels ----------
import subprocess as _sp, p4_fix
_G=json.loads(_sp.check_output(['node','-e',"process.stdout.write(JSON.stringify(require('"+os.path.join(H,'..','p4','content','l10.js')+"').gaps))"]))
_ID='p4l10'
_PIC=globals().get('PIC')

order=['p4l10-title','p4l10-warm1','p4l10-warm2','p4l10-explore1','p4l10-explore2','p4l10-teach1','p4l10-we1','p4l10-we2','p4l10-try2','p4l10-we3','p4l10-key','p4l10-break','p4l10-ws1','p4l10-ws1ans','p4l10-teachlogic','p4l10-teachqueue','p4l10-teachages','p4l10-ws2','p4l10-ws2ans','p4l10-stretch','p4l10-challenge','p4l10-chdiag','p4l10-chwalk','p4l10-talk','p4l10-exit','p4l10-end']
p4_fix.finish(S,10,_G,pic=_PIC)
order=p4_fix.order(order,10)
assert set(order)==set(S), set(order)^set(S)
p4_fix.check_times(S,10)  # every time pill must match rebuild/p4_budget.py
sd=os.path.join(D,'slides')
for f in os.listdir(sd):
    if f.endswith('.html') and f[:-5] not in S: os.remove(os.path.join(sd,f))
for i,h in S.items(): open(os.path.join(sd,i+'.html'),'w').write(h)
deck={'v':4,'createdOnFiles':{'v':1,'at':datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')},'lists':'css',
 'title':'Math Inquirers P4: Lesson 10 – Puzzle Day','order':order,'cover':'p4l10-title',
 'sections':{'s1':{'description':'Warm-up and explore','start':'p4l10-title'},'s2':{'description':'Teach: four ways in (guess and check, suppose, work backwards)','start':'p4l10-teach1'},'s3':{'description':'Worksheet with teaching before each page','start':'p4l10-break'},'s4':{'description':'Stretch, challenge, talk, exit and close','start':'p4l10-stretch'}},
 'faces':{'fredoka':{'family':'Fredoka','href':'https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&display=swap'},'nunito-sans':{'family':'Nunito Sans','href':'https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@400;600;700&display=swap'}},
 'designSystems':[]}
json.dump(deck,open(os.path.join(D,'deck.json'),'w'),indent=1,ensure_ascii=False)
print(len(order),'slides')
