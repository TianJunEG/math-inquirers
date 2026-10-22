"""Math Inquirers P4, Lesson 3: Operation Detectives. Writes split/p4l3/project (deck.json + slides/*.html)."""
import json,os,sys,datetime
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,H)
import slidekit
from slidekit import *
slidekit.FOOT='Math Inquirers P4 Holiday Program  •  Notice it. Test it. Explain why.'
FOOTX=slidekit.FOOT
D=os.path.join(H,'..','split','p4l3','project'); os.makedirs(os.path.join(D,'slides'),exist_ok=True)
S={}
def put(i,h): S[i]=h
RED='#D64545'

# ---------- shared slide shapes (same look as the P1/P2 decks) ----------
def title_slide(sid,label,title,topic,today,notes):
    return (f'<section id="{sid}" data-transition="fade" style="background:{NAVY};color:{CREAM};font-family:{BF};padding:128px 128px 160px;display:flex;flex-direction:column;justify-content:center;gap:36px">\n'
            f'<p style="font-size:32px;font-weight:700;letter-spacing:4px;color:{YEL}">{E(label)}</p>\n'
            f'<h1 style="font-family:{HF};font-size:128px;font-weight:600;line-height:1.05">{E(title)}</h1>\n'
            f'<p style="font-size:44px;color:#C9D4EC">{E(topic)}</p>\n'
            f'<div style="background:#26385F;border-radius:24px;padding:40px;display:flex;flex-direction:column;gap:12px"><p style="font-size:28px;font-weight:700;letter-spacing:3px;color:{YEL}">TODAY WE WILL</p><p style="font-size:44px;font-weight:600">{E(today)}</p></div>\n'
            f'<p style="position:absolute;left:128px;bottom:64px;width:1400px;font-size:24px;color:#B7C3DD">{E(FOOTX)}</p>\n<aside>{E(notes)}</aside>\n</section>\n')
def break_slide(sid,time,text,notes):
    notes=notes.replace('Four minutes.',__import__('p4_budget').break_lead(3),1)
    return (f'<section id="{sid}" data-transition="fade" style="background:{TEAL};color:{CREAM};font-family:{BF};padding:128px 128px 160px;display:flex;flex-direction:column;justify-content:center;gap:36px">\n'
            f'<p style="font-size:32px;font-weight:700;letter-spacing:4px;color:{YEL}">{E(time)}</p>\n'
            f'<h2 style="font-family:{HF};font-size:110px;font-weight:600;line-height:1.05">Brain break</h2>\n'
            f'<p style="font-size:36px;color:#D7EFEA">First, one minute: a drink of water and a toilet stop if you need one.</p>\n<p style="font-size:44px;font-weight:600">{E(text)}</p>\n<p style="font-size:36px;color:#D7EFEA">Then back to our seats on time.</p>\n'
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
def rq(left,top,width,label,html,size=38):
    return pin(left,top,width,f'<p style="font-size:{size}px;font-weight:600;line-height:1.3"><span style="color:{TEAL};font-weight:800">{E(label)}</span>  {html}</p>',None,WHITE,20,'18px 28px')
def ra(left,top,width,html,build='pop',size=38):
    return pin(left,top,width,f'<p style="font-size:{size}px;font-weight:800;line-height:1.2">{html}</p>',build,YEL,20,'18px 26px')
def rtry(sid,time,title,sub,rows,notes,size=38,asize=38,top=330,gapy=150,qw=1250):
    body=h2(title)+p(sub,34,600,MUTED)
    for i,(a,b,c) in enumerate(rows):
        t=top+i*gapy
        body+=rq(128,t,qw,a,b,size)+ra(128+qw+40,t,1664-qw-40,c,'pop',asize)
    return sec(sid,time,body,notes)
CIR=f'<span style="display:inline-block;width:46px;height:46px;border:4px solid {NAVY};border-radius:50%;background:{WHITE};vertical-align:middle;margin:0 12px;box-sizing:border-box"></span>'
def tiles(items,x0=0,y=20,w=110,h=120,gap=22,size=64):
    """items: list of (text, kind) kind n=number card, s=sign card, b=bracket card, c=empty circle, t=plain text"""
    g=''; x=x0
    for t,k in items:
        if k=='c':
            g+=f'<circle cx="{x+w/2}" cy="{y+h/2}" r="{h*0.32}" fill="{WHITE}" stroke="{NAVY}" stroke-width="5"/>'
        elif k=='t':
            g+=txt(x+w/2,y+h/2+size*0.36,t,size)
        else:
            fill={'n':YEL,'s':GREY,'b':SKY}[k]
            g+=f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="16" fill="{fill}" stroke="{NAVY}" stroke-width="5"/>'+txt(x+w/2,y+h/2+size*0.36,t,size)
        x+=w+gap
    return g

# ---------- 1. title ----------
put('p4l3-title',title_slide('p4l3-title','LESSON 3  •  WEEK 2','Operation Detectives','Four operations',
 'Use the order of operations, find missing signs and brackets to hit a target, and work backwards through number chains.',
 'Objective: Use the order of operations (brackets first, then × and ÷ from left to right, then + and − from left to right), find missing signs and brackets to hit a target, work backwards through a chain of operations, and solve "times as many" problems with a bar model. '
 'Thinking strategies taught today: ESTIMATE, TEST AND ADJUST (guess and check), WORK BACKWARDS and DRAW A BAR MODEL. '
 'Materials: mini whiteboards and markers; paper number cards 0 to 9; sign cards +, −, ×, ÷ and two pairs of bracket cards per child; scrap paper for bar models. '
 'Online: children write on whiteboards and hold them up to the camera; before the lesson they cut out the sign and bracket cards so they can move them on camera in the explore task. '
 'Time plan: (written by rebuild/p4_fix.py from rebuild/p4_budget.py).'))

# ---------- 2. warm-up game: target numbers ----------
g=tiles([('2','n'),('4','n'),('5','n'),('9','n')],0,10,110,130,30,70)+tiles([('+','s'),('−','s'),('×','s'),('÷','s')],620,30,90,90,24,56)
body=h2('Warm-up: Target Numbers')+p('Use the cards 2, 4, 5 and 9, each card once at most, with + − × ÷. Hit the target!',34,600,MUTED)
body+=pin(128,310,1664,svgwrap(1100,150,'Number cards 2, 4, 5 and 9 and sign cards plus, minus, times and divide',g),None)
targets=[('13','4 + 9'),('22','2 + 4 × 5'),('36','4 × 9'),('81','(4 + 5) × 9')]
for i,(t,a) in enumerate(targets):
    L=128+i*424
    body+=pin(L,490,392,p('TARGET',28,800,TEAL)+f'<p style="font-family:{HF};font-size:110px;font-weight:600;line-height:1">{t}</p>',None,WHITE,24,'20px 28px',f'box-sizing:border-box;height:330px;align-items:center;border:4px solid {NAVY};box-shadow:8px 8px 0 {NAVY}')
    body+=pin(L+24,700,344,p(a,40,800),'pop',SOFT,16,'12px 18px',f'box-sizing:border-box;align-items:center;border:3px solid {NAVY}')
put('p4l3-warm1',sec('p4l3-warm1','6.5–8.5 MIN',body,
 'Minutes 6.5 to 8.5 (one short round, about 90 seconds: the Sneak-peek puzzles came first). Target Numbers. Children copy the four cards 2, 4, 5 and 9 onto their whiteboards. Point to one target at a time: "Make 13. Go!" Everyone writes a sentence and holds it up at the same moment: there is no race and no points. Click to show one way for each target (clicks reveal 13, 22, 36, 81 in order). '
 'Other ways: 13 = 2 × 9 − 5; 22 = 2 × 9 + 4; 81 needs brackets: (4 + 5) × 9. '
 'Listen for children who write 2 + 4 × 5 and say 30: they added first. That leads straight into today\'s lesson. Finisher: "Can you make 100?" (Let them try; it cannot be done with these cards and signs, which is a good thing to notice.)'))

# ---------- 3. quick questions ----------
qs=[('1.','25 × 4 = ?','100'),('2.','48 ÷ 6 = ?','8'),('3.','9 × 6 = ?','54')]
body=h2('Quick questions')+''.join(qrow(128,250+i*125,1250,a,b) for i,(a,b,c) in enumerate(qs))+''.join(answer(1420,250+i*125,372,c) for i,(a,b,c) in enumerate(qs))
put('p4l3-warm2',sec('p4l3-warm2','8.5–11.5 MIN',body,'Minutes 8.5 to 11.5. Mental maths, three questions, about 30 seconds each. Read each aloud, whiteboards up together, then click. No follow-up questions. Answers: 100, 8, 54. The other two warm-up questions (1 000 − 368; 4 × 20) are in the Weekly Dose of Thinking Math.'))

# ---------- 4. explore ----------
g=tiles([('6','n'),('+','s'),('4','n'),('×','s'),('3','n'),('−','s'),('2','n')],330,80,100,110,18,60)
g+=tiles([('(','b'),(')','b')],40,20,80,90,30,60)
g+=f'<path d="M240 70 Q300 40 360 76" fill="none" stroke="{TEAL}" stroke-width="5" stroke-dasharray="12 8"/><polygon points="366,82 344,78 358,62" fill="{TEAL}"/>'
g+=f'<rect x="1270" y="40" width="320" height="150" rx="18" fill="{SOFT}" stroke="{NAVY}" stroke-width="4"/>'+txt(1430,105,'One pair of',32)+txt(1430,150,'brackets!',32,TEAL)
steps=''.join(f'<li>{E(s)}</li>' for s in ['Write 6 + 4 × 3 − 2 on your whiteboard and work it out.','Put ONE pair of brackets somewhere. Work it out again.','Move the brackets to other places. Write every answer.','How many different answers? Which is the biggest? The smallest?'])
body=h2('Explore: where do the brackets go?')+card(chip('EXPLORE')+f'<ol style="font-size:36px;font-weight:600;padding-left:52px;display:flex;flex-direction:column;gap:8px">{steps}</ol>')
body+=card(svgwrap(1600,220,'Cards 6 + 4 × 3 − 2 in a row, with a pair of bracket cards waiting to be placed',g),extra='padding:20px 32px')
put('p4l3-explore1',sec('p4l3-explore1','11.5–20.5 MIN',body,'Minutes 11.5 to 20.5. Pairs work with number, sign and bracket cards (online: paper cards on camera, or write on whiteboards). Ask them to predict first: how many different answers? Many children guess 5 or 6, one for each place. Let them try any placement; the brackets must go round at least two numbers. Early finishers: can TWO pairs of brackets make a new answer? ((6 + 4) × (3 − 2) = 10, the same as one of the others.)'))
body=h2('Explore: talk about it')+numcards([('1.','How many different answers did you find?'),('2.','Where do the brackets go to make the biggest answer? The smallest?')],40)
put('p4l3-explore2',sec('p4l3-explore2','20.5–23.5 MIN',body,'Minutes 20.5 to 23.5. Pencils down (or when the 60-second timer closes the rooms), then gather the answers on the board. Two debrief questions only. Answers: 1) Only 3 different answers: 16 (no brackets), 28 and 10. 2) Biggest: (6 + 4) × 3 − 2 = 10 × 3 − 2 = 28. Smallest: 6 + 4 × (3 − 2) = 6 + 4 × 1 = 10. The third question (which brackets do not change the answer? Brackets round 4 × 3, round 6 + 4 × 3, or round 4 × 3 − 2 all give 16, because the × is done first anyway) is answered by the first teaching slide, so it is not asked here. Do NOT teach the rule yet if nobody says it: the next slides teach it.'))

# ---------- 6. teach: order of operations ----------
rules=p('The order',34,800,TEAL)+p('1.  Brackets first',38,700)+p('2.  × and ÷, from left to right',38,700)+p('3.  + and −, from left to right',38,700)
body=h2('Order of operations')+pin(128,250,620,rules,None,SOFT,24,'26px 32px','box-sizing:border-box')
body+=pin(840,250,952,p('40 − 8 × 3 + 6 ÷ 2',60,700),None,WHITE,24,'22px 32px')
body+=step(1,'No brackets. × and ÷ first: 8 × 3 = 24, 6 ÷ 2 = 3.',left=840,top=400,width=952,size=34)
body+=step(2,'Now 40 − 24 + 3. Go from left to right: 40 − 24 = 16.',left=840,top=530,width=952,size=34)
body+=step(3,'16 + 3 = 19.',left=840,top=660,width=952,size=34)
body+=answer(840,770,952,'40 − 8 × 3 + 6 ÷ 2 = 19')
body+=pin(128,560,620,p('Not this one: 40 − 8 = 32, then 32 × 3 = 96 … Going only from left to right gives the wrong answer.',32,700),'fade',WHITE,20,'22px 28px',f'box-sizing:border-box;border:3px dashed {RED}')
put('p4l3-teach1',sec('p4l3-teach1','23.5–25 MIN',body,'Teach. Read the order together. Children work out the example on whiteboards first, then click through the steps. Think-aloud: "No brackets, so I look for × and ÷ first: 8 × 3 is 24 and 6 ÷ 2 is 3. Now I only have + and −, so I go from left to right: 40 − 24 is 16, and 16 + 3 is 19." The last click shows the common mistake: doing everything from left to right. Ask: "Which part did this child do first? Why is that wrong?"'))

# ---------- 8. worked example: missing signs ----------
pz=[('8','n'),('','c'),('5','n'),('','c'),('3','n'),('=','t'),('37','n')]
g0=tiles(pz,0,10,120,120,26,64)
g1=tiles(pz,0,10,120,120,26,64)+txt(206,94,'×',64,TEAL)+txt(498,94,'−',64,TEAL)
body=h2('Worked example: missing signs')+p('Write +, −, × or ÷ in each circle to make the number sentence true.',34,600,MUTED)
body+=pin(128,300,1100,svgwrap(1050,140,'8, circle, 5, circle, 3 equals 37',g0),None)
body+=step(1,'37 is big. Adding all three makes only 16, so we need a ×.',top=470,size=34)
body+=step(2,'Try 8 × 5 = 40. Then 40 and 3 make 37: 40 − 3 = 37 ✓',top=580,size=34)
body+=pin(128,300,1100,svgwrap(1050,140,'8 times 5 minus 3 equals 37',g1),'fade')
body+=step(3,'Check another way: 8 + 5 × 3 = 8 + 15 = 23. Not this one.',top=690,size=34)
body+=answer(1260,320,532,'8 × 5 − 3 = 37')
put('p4l3-we1',sec('p4l3-we1','25–26 MIN',body,'Strategy: ESTIMATE, TEST, ADJUST. Ask first: "Is 37 big or small compared with 8, 5 and 3? What does that tell us?" Click through: step 1, step 2, the signs appear in the circles, step 3, the answer. Think-aloud: "If I add everything I only get 16, so I need a times. 8 × 5 is 40, that is just 3 too many, so take away 3." Remind them to CHECK in the right order: 8 × 5 − 3 means 40 − 3, not 8 × 2.'))

# ---------- 10. worked example: brackets ----------
body=h2('Worked example: brackets to hit a target')+pin(128,250,1664,p('Put in ONE pair of brackets to make 29:     2 + 3 × 4 + 5',40,700),None,WHITE,24,'22px 32px')
body+=step(1,'No brackets: 2 + 12 + 5 = 19. Too small: we need to multiply a bigger number.',top=380,size=34)
body+=step(2,'Try (2 + 3) × 4 + 5 = 5 × 4 + 5 = 25. Closer, but not 29.',top=490,size=34)
body+=step(3,'Try 2 + 3 × (4 + 5) = 2 + 3 × 9 = 2 + 27 = 29 ✓',top=600,size=34)
body+=answer(128,715,1664,'2 + 3 × (4 + 5) = 29')
body+=pin(128,820,1664,p('Brackets round 3 × 4 change nothing: × is done first anyway.',32,700),'fade',SOFT,20,'16px 28px')
put('p4l3-we2',sec('p4l3-we2','26–27.5 MIN',body,'Strategy: test and adjust. Think-aloud: "19 is too small. Brackets let me add BEFORE I multiply, which makes the multiplication bigger. Round 2 + 3 gives 25. Round 4 + 5 gives 29. Found it." (Two pairs of brackets would give (2 + 3) × (4 + 5) = 45; with one pair, 29.)'))

# ---------- 11. key ----------
body=h2('Key idea: order matters')+card(p('Brackets first. Then × and ÷, then + and −, each from left to right.',44,700))+card(p('To hit a target: estimate first, test, then adjust. A big target usually needs a ×.',38,600,MUTED))
put('p4l3-key',sec('p4l3-key','27.5–28.5 MIN',body,'Say the key idea together. Common mistakes to watch for during the worksheet: (1) Working strictly from left to right and ignoring the order: 40 − 8 × 3 done as 32 × 3. (2) Thinking addition always comes before subtraction (or × before ÷) instead of working left to right: 20 − 8 + 2 answered 10, 72 ÷ 8 × 3 answered 3. (3) Working backwards but using the same operation instead of the opposite one (for − 18, taking away 18 again instead of adding 18).'))
put('p4l3-break',break_slide('p4l3-break','28.5–32.5 MIN','Odd or even? Stand up if the answer is even, crouch down if it is odd: 3 + 4 × 2,  (3 + 4) × 2,  20 ÷ 4 + 1,  20 ÷ (4 + 1).','Four minutes. Read each sentence, count down from 3, everyone moves. Answers: 3 + 4 × 2 = 11 (odd, crouch); (3 + 4) × 2 = 14 (even, stand); 20 ÷ 4 + 1 = 6 (even, stand); 20 ÷ (4 + 1) = 4 (even, stand). Online: children stand up and crouch on camera.'))

# ---------- worksheet page 1 ----------
put('p4l3-ws1',ws_preview('p4l3-ws1','32.5–49 MIN','Worksheet page 1: with your partner',[('Q1','Order of operations. Underline the part you do first.'),('Q2','Missing signs. Estimate, test, adjust.'),('Q3','On your own, first: brackets change the answer. Put one pair in to hit a target.')],'Stuck? Say the order out loud: brackets, then × and ÷, then + and −.','Minutes 32.5 to 49. Pairs do Q1 and Q2 (about 9 minutes of work). Q3 is the first question each child does on their own, at the start of page 2 time; its answer is checked together with page 2. Walk around. Ask "Which part do you work out first?" before giving any help. Q2d has four numbers: encourage children to test a sign in the first circle and see how big the answer is so far.'))
put('p4l3-ws1ans',checks('p4l3-ws1ans','49–51 MIN','Page 1: check together',[('Q1','a) 106   b) 250   c) 27   d) 98   e) 12'),('Q2','a) 7 × 6 − 4   b) 48 ÷ 6 × 2   c) 9 ÷ 3 + 5   d) 12 ÷ 3 + 2 × 5')],
 'Click each answer after a pair explains theirs. Q1d: 45 ÷ 5 = 9 first, then 100 − 9 + 7 = 98 (not 55 ÷ 5 + 7). Q1e: 6 × 8 ÷ 4 = 48 ÷ 4 = 12. Q2d: 12 ÷ 3 = 4 and 2 × 5 = 10, 4 + 10 = 14; each puzzle on this page has only one answer.',gapy=170))

# ---------- teach before page 2: work backwards ----------
body=h2('Work backwards through a machine')+pin(128,240,1664,machine([('?','q'),('× 4','op'),('− 6','op'),('÷ 2','op'),('21','res')],back='Work backwards: undo each step'),None)
body+=step(1,'Undo ÷ 2: multiply.  21 × 2 = 42',top=530,size=36)
body+=step(2,'Undo − 6: add.  42 + 6 = 48',top=640,size=36)
body+=step(3,'Undo × 4: divide.  48 ÷ 4 = 12.   Check: 12 × 4 = 48, 48 − 6 = 42, 42 ÷ 2 = 21 ✓',top=750,size=36)
put('p4l3-teachback',sec('p4l3-teachback','51–52 MIN',body,'Teach before worksheet page 2 (Q4). Only two methods are taught before page 2 (this one and the bar model). The chain slide for Q7, a choice question, is in the take-home pack. Strategy: WORK BACKWARDS. Start at the END. Each step is undone with the opposite operation: × and ÷ undo each other, + and − undo each other. Ask before each click: "What was the last thing the machine did? How do we undo it?" Watch for children who take away 6 again instead of adding 6. Always check by going forwards.'))

# ---------- teach: bar model ----------
u=190; g=''
for r,(lab,n,col) in enumerate([('Ali',4,YEL),('Ben',1,SKY)]):
    y=30+r*120
    g+=txt(80,y+62,lab,40,NAVY,'end')
    for i in range(n): g+=f'<rect x="{110+i*u}" y="{y}" width="{u}" height="90" fill="{col}" stroke="{NAVY}" stroke-width="4"/>'
    g+=txt(110+n*u+24,y+60,f'{n} unit{"s" if n>1 else ""}',30,TEAL,'start',700,'Nunito Sans, Arial') if r==0 else ''
bx=110+4*u+200
g+=f'<path d="M{bx} 30 Q{bx+24} 30 {bx+24} 60 L{bx+24} 110 Q{bx+24} 135 {bx+44} 135 Q{bx+24} 135 {bx+24} 160 L{bx+24} 210 Q{bx+24} 240 {bx} 240" fill="none" stroke="{NAVY}" stroke-width="4"/>'+txt(bx+60,148,'1 345',44,NAVY,'start')
body=h2('Bar model: 4 times as many')+p('Ali has 4 times as many stickers as Ben. They have 1 345 stickers altogether. How many stickers does Ali have?',34,600)
body+=pin(128,330,1400,svgwrap(1300,260,'Bar model: Ali has 4 units, Ben has 1 unit, 1 345 altogether',g),None)
body+=step(1,'Ali has 4 units and Ben has 1 unit: 5 units altogether.',top=600,size=34)
body+=step(2,'5 units = 1 345, so 1 unit = 1 345 ÷ 5 = 269.',top=700,size=34)
body+=step(3,'Ali: 4 units = 269 × 4 = 1 076.   Check: 1 076 + 269 = 1 345 ✓',top=800,size=34)
put('p4l3-teachbar',sec('p4l3-teachbar','52–53.5 MIN',body,'Teach before worksheet page 2 (Q6). Strategy: DRAW A BAR MODEL. Draw Ben\'s bar first (1 unit), then Ali\'s bar with 4 units the same size. The brace shows the total. Ask: "How many units altogether? What is one unit worth?" Show the division on the board: 1 345 ÷ 5 = 269 (13 hundreds ÷ 5 = 2 hundreds r 3 hundreds; 34 tens ÷ 5 = 6 tens r 4 tens; 45 ÷ 5 = 9). Extra question: "How many MORE stickers does Ali have?" (3 units = 807).'))

# ---------- teach: number chains ----------
body=h2('Number chains: add the two before')+p('Example:  1, 3, 4, 7, 11   (1 + 3 = 4,  3 + 4 = 7,  4 + 7 = 11)',36,600,MUTED)
body+=pin(128,320,800,p('Work backwards:  __, __, 9, 15, __',36,800,TEAL))
for i,t in enumerate(['15 − 9 = 6: the 2nd number','9 − 6 = 3: the 1st number','9 + 15 = 24: the 5th number']): body+=pin(128,400+i*105,800,p(t,32),'rise',WHITE)
body+=pin(128,715,800,p('3, 6, 9, 15, 24',40,800),'pop',YEL,20,'16px 28px')
body+=pin(992,320,800,p('Guess and check:  2, __, __, 16, __',36,800,TEAL))
for i,t in enumerate(['Try 5:  2, 5, 7, 12.  Too small.','Try 8:  2, 8, 10, 18.  Too big.','Try 7:  2, 7, 9, 16 ✓']): body+=pin(992,400+i*105,800,p(t,32),'rise',WHITE)
body+=pin(992,715,800,p('2, 7, 9, 16, 25',40,800),'pop',YEL,20,'16px 28px')
put('p4l3-teachchain',sec('p4l3-teachchain','Optional, if you finish early',body,'Take-home pack (Q7 is a choice question that is not taught in the lesson; any child who picks it can use this slide). Read the example aloud. Left: when two numbers next to each other are known, work backwards by taking away. Right: when the gaps are in the middle, guess the 2nd number and test it, then adjust: 12 was too small and 18 too big, so the answer is in between. Ask: "When I add 1 to my guess, how much does the 4th number go up?" (by 2, because the guess is used twice). That helps strong children find it in one step.'))

# ---------- worksheet page 2 ----------
put('p4l3-ws2',ws_preview('p4l3-ws2','53.5–76.5 MIN','Worksheet page 2: on your own',[('Q4','Machine chain. Work backwards, then check forwards.'),('Q5','Number trick. Try it, notice, then explain why.'),('Q6','Hawker stall. Draw a bar model first.'),('Q7','Number chains. Work backwards, or guess and check.')],'Finished early? Stretch and Challenge come next.','Children work alone. Note who needs a short catch-up next lesson, especially children who undo − with − when working backwards.'))
put('p4l3-ws2ans',checks('p4l3-ws2ans','76.5–80.5 MIN','Page 2: check together',[('Q3','a) 41   b) (4 + 8) × 5 − 3   c) 4 + 8 × (5 − 3)'),('Q4','23:  30 × 4 = 120,  120 + 18 = 138,  138 ÷ 6 = 23'),('Q5','Always 7. Blanks: my number, 7, 7. (× 5 then ÷ 5 gives it back; 35 ÷ 5 = 7)'),('Q6','4 units = 124, 1 unit = 31.  b) 93 plates   c) 62 more'),('Q7','a) 5, 8, 13, 21, 34    b) 4, 7, 11, 18, 29')],
 'Click after a child explains. Q3 (brackets, done first on their own): a) 4 + 8 × 5 − 3 = 41; b) (4 + 8) × 5 − 3 = 57; c) 4 + 8 × (5 − 3) = 20. Q4 check: 23 × 6 = 138, − 18 = 120, ÷ 4 = 30. Q5: with 3: 15, 50, 10, 7. Part b is now a fill-in: number, 7, 7 (the open "explain why" is the Think Harder stretch). Bar model: five bars of your number plus 35; shared into 5 groups, each group is one bar and 7; take away the bar and 7 is left. Q6: chicken rice 3 units, laksa 1 unit; 124 ÷ 4 = 31; 3 × 31 = 93; the difference is 2 units = 62. (The old 1 236 version, 309 / 927 / 618, is in the question bank.) Q7b: try 7 for the 2nd number: 4, 7, 11, 18.',gapy=150,size=32))

# ---------- stretch / challenge ----------
from p4bank import th_items, th_notes, gf_numbers  # slide Think harder = the printed page (docs/audit/reaudit_fixes_p4.md)
st=th_items(3)
def numgrid(items,size=30): return '<div style="display:grid;grid-template-columns:1fr 1fr;gap:24px;align-items:stretch">'+''.join(card(p(f'<span style="color:{TEAL}">{a}</span>  {E(b)}',size,600,raw=True),extra='padding:24px 32px') for a,b in items)+'</div>'
put('p4l3-stretch',sec('p4l3-stretch','Optional, if you finish early',h2('Think harder')+numgrid(st,34),th_notes(3)))
ch=[('1.','Put + or − in each gap so that the answer is 7:  1 __ 2 __ 3 __ 4 __ 5 __ 6 = 7. Find ALL the ways.'),('2.','Mei spent half of her money on a book. Then she spent $6 on lunch. Then she spent half of what was left on a gift. She had $9 left. How much money did she have at first?')]
put('p4l3-challenge',sec('p4l3-challenge','Optional, if you finish early',h2('Go further')+numcards(ch,36),'Pairs try first, then use the "see it" slide if stuck, then the walk-through. These are Go further Q5 and Q6. Answers: 1) 2 ways: 1 − 2 + 3 + 4 − 5 + 6 = 7 and 1 + 2 − 3 − 4 + 5 + 6 = 7. 2) $48 (work backwards: 9 × 2 = 18, 18 + 6 = 24, 24 × 2 = 48).'))
g1=''
for i in range(6):
    x=10+i*104
    g1+=f'<rect x="{x}" y="60" width="66" height="90" rx="12" fill="{YEL}" stroke="{NAVY}" stroke-width="4"/>'+txt(x+33,122,i+1,48)
    if i<5: g1+=f'<circle cx="{x+85}" cy="105" r="15" fill="{WHITE}" stroke="{NAVY}" stroke-width="4"/>'
g1+=txt(690,122,'= 7',48)
g1+=f'<rect x="20" y="260" width="720" height="80" rx="14" fill="{SOFT}" stroke="{NAVY}" stroke-width="3"/>'+txt(380,312,'All + :  1 + 2 + 3 + 4 + 5 + 6 = ?',34)
g1+=f'<rect x="20" y="370" width="720" height="80" rx="14" fill="{WHITE}" stroke="{NAVY}" stroke-width="3"/>'+txt(380,422,'What does one − do to the total?',34,TEAL)
g2=f'<path d="M30 76 Q30 60 50 60 L360 60 Q380 60 380 46 Q380 60 400 60 L710 60 Q730 60 730 76" fill="none" stroke="{NAVY}" stroke-width="4"/>'+txt(380,34,'money at first = ?',30,TEAL)
g2+=f'<rect x="30" y="80" width="350" height="90" fill="{SKY}" stroke="{NAVY}" stroke-width="4"/>'+txt(205,136,'book: half',32)
g2+=f'<rect x="380" y="80" width="90" height="90" fill="{GREY}" stroke="{NAVY}" stroke-width="4"/>'+txt(425,136,'$6',32)
g2+=f'<rect x="470" y="80" width="130" height="90" fill="{SOFT}" stroke="{NAVY}" stroke-width="4"/>'+txt(535,136,'gift',32)
g2+=f'<rect x="600" y="80" width="130" height="90" fill="{YEL}" stroke="{NAVY}" stroke-width="4"/>'+txt(665,136,'$9',32)
g2+=txt(425,210,'lunch',28,MUTED,weight=600,font='Nunito Sans, Arial')+txt(600,210,'half and half',28,MUTED,weight=600,font='Nunito Sans, Arial')
g2+=f'<rect x="30" y="270" width="700" height="80" rx="14" fill="{WHITE}" stroke="{NAVY}" stroke-width="3"/>'+txt(380,322,'Start at the END: $9 is half of …?',34,TEAL)
g2+=f'<rect x="30" y="370" width="700" height="80" rx="14" fill="{WHITE}" stroke="{NAVY}" stroke-width="3"/>'+txt(380,422,'Then undo the $6. Then undo the half.',32)
body=h2('Go further: see it',60)+'<div style="display:flex;gap:32px;align-items:flex-start">'
body+=card(f'<p style="font-size:30px;font-weight:700;color:{TEAL}">Q1: plus or minus?</p>'+svgwrap(760,470,'Cards 1 to 6 with empty circles between them, equals 7',g1).replace('width:760px;height:470px;flex:none','width:100%;height:auto;display:block'),extra='flex:1;min-width:0;padding:20px 24px')
body+=card(f'<p style="font-size:30px;font-weight:700;color:{TEAL}">Q2: Mei\'s money as a bar</p>'+svgwrap(760,470,'A bar for Mei\'s money: half for a book, $6 for lunch, then the rest split into a gift and $9 left',g2).replace('width:760px;height:470px;flex:none','width:100%;height:auto;display:block'),extra='flex:1;min-width:0;padding:20px 24px')+'</div>'
put('p4l3-chdiag',sec('p4l3-chdiag','Optional, if you finish early',body,'Show after pairs have tried the Challenge, or if they are stuck. The pictures show the problem, not the answer. Ask: In Q1, what is the total if every sign is +? If you change one + to a −, how much smaller does the total get? In Q2, where does the bar END? Which part do you know? Answers are in the Challenge slide notes.'))
body=h2('Go further: walk-through')+pin(128,250,800,p('Q1: start with all +',38,800,TEAL))
for i,t in enumerate(['All +: 1 + 2 + 3 + 4 + 5 + 6 = 21. That is 14 too many.','A − instead of + takes the number away TWICE: from +2 to −2 is 4 less.','So the numbers we flip must add up to 7: 2 + 5 or 3 + 4.','1 − 2 + 3 + 4 − 5 + 6 = 7 and 1 + 2 − 3 − 4 + 5 + 6 = 7 ✓']): body+=pin(128,330+i*130,800,p(t,30),'rise',WHITE)
body+=pin(992,250,800,p('Q2: work backwards',38,800,TEAL))
for i,t in enumerate(['$9 is the half she kept, so before the gift: $9 × 2 = $18','Undo lunch: $18 + $6 = $24','$24 is the half left after the book: $24 × 2 = $48','Check: 48 → 24 → 18 → 9 ✓   She had $48.']): body+=pin(992,330+i*130,800,p(t,30),'rise',WHITE)
put('p4l3-chwalk',sec('p4l3-chwalk','Optional, if you finish early',body,'Use after pairs have tried. Q1: children usually find one way by guess and check. The "take it away twice" idea proves there are exactly 2 ways: the 1 cannot be changed (there is no sign in front of it) and 7 cannot be made from 2 to 6 in any other way (6 + 1 needs the 1; 7 alone is not a card). Q2: the same working backwards as the machine on page 2: undo each step in reverse order.'))

# ---------- talk / exit ----------
body=h2('Talk time')+card(chip('TALK TIME',YEL,NAVY)+p('Ben says 20 − 8 + 2 = 10 because you add first. Mei says the answer is 14. Who is right? Why?',42,600))+card(p('Sentence starters:',34,400,MUTED)+p('“I noticed that …”   “I tested it by …”   “I know because …”',38,600))
put('p4l3-talk',sec('p4l3-talk','80.5–84 MIN',body,'Minutes 80.5 to 84. Pair talk is 1 minute (no breakout rooms: children tell the grown-up beside them, or write one sentence), then share. Answer: Mei is right. With only + and − we work from left to right: 20 − 8 = 12, then 12 + 2 = 14. Ben worked out 8 + 2 first; to do that we would need brackets: 20 − (8 + 2) = 10. Not asked in class (moved to the Weekly Dose of Thinking Math): "How did you know which sign to try first in the missing-sign puzzles?" (estimate: a big target needs ×, a small one may need ÷ or −). Praise the reasons, not only the answers.'))
body=h2('Exit ticket')+card(chip('EXIT TICKET')+p('Work out  50 − 6 × (3 + 4).  Show the step you did first.',46,600))+card(p('Write your answer on a slip of paper. Show it to your tutor. Then collect your stamp in your inquiry journal.',34,400))
put('p4l3-exit',sec('p4l3-exit','84–86.5 MIN',body,'Minutes 84 to 86.5. Answer: 8. Brackets first: 3 + 4 = 7; then 6 × 7 = 42; then 50 − 42 = 8. Common wrong answers: 308 (50 − 6 = 44, 44 × 7) and 47 (working left to right inside out). Extension: use four 4s and any signs and brackets to make every number from 0 to 9.'))

# ---------- write ----------
# ---------- fix pass (rebuild/p4_fix.py): sneak-peek puzzles, looking back, neutral names, go further, minute labels ----------
import subprocess as _sp, p4_fix
_G=json.loads(_sp.check_output(['node','-e',"process.stdout.write(JSON.stringify(require('"+os.path.join(H,'..','p4','content','l3.js')+"').gaps))"]))
_ID='p4l3'
_PIC=globals().get('PIC')

order=['p4l3-title','p4l3-warm1','p4l3-warm2','p4l3-explore1','p4l3-explore2','p4l3-teach1','p4l3-we1','p4l3-we2','p4l3-key','p4l3-break','p4l3-ws1','p4l3-ws1ans','p4l3-teachback','p4l3-teachbar','p4l3-teachchain','p4l3-ws2','p4l3-ws2ans','p4l3-stretch','p4l3-challenge','p4l3-chdiag','p4l3-chwalk','p4l3-talk','p4l3-exit']
p4_fix.finish(S,3,_G,pic=_PIC)
order=p4_fix.order(order,3)
assert set(order)==set(S), set(order)^set(S)
p4_fix.check_times(S,3)  # every time pill must match rebuild/p4_budget.py
sd=os.path.join(D,'slides')
for f in os.listdir(sd):
    if f.endswith('.html') and f[:-5] not in S: os.remove(os.path.join(sd,f))
for i,h in S.items(): open(os.path.join(sd,i+'.html'),'w').write(h)
deck={'v':4,'createdOnFiles':{'v':1,'at':datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')},'lists':'css',
 'title':'Math Inquirers P4: Lesson 3 – Operation Detectives','order':order,'cover':'p4l3-title',
 'sections':{'s1':{'description':'Warm-up and explore','start':'p4l3-title'},'s2':{'description':'Teach: order of operations, missing signs and brackets','start':'p4l3-teach1'},'s3':{'description':'Worksheet with teaching before each page','start':'p4l3-break'},'s4':{'description':'Stretch, challenge, talk and exit','start':'p4l3-stretch'}},
 'faces':{'fredoka':{'family':'Fredoka','href':'https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&display=swap'},'nunito-sans':{'family':'Nunito Sans','href':'https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@400;600;700&display=swap'}},
 'designSystems':[]}
json.dump(deck,open(os.path.join(D,'deck.json'),'w'),indent=1,ensure_ascii=False)
print(len(order),'slides')
