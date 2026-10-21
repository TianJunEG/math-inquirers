"""Math Inquirers P5, Lesson 2: Fraction Feats. Writes split/p5l2/project (deck.json + slides/*.html)."""
import json,os,sys,datetime
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,H)
import slidekit
from slidekit import *
slidekit.FOOT='Math Inquirers P5 Holiday Program  •  Notice it. Test it. Explain why.'
D=os.path.join(H,'..','split','p5l2','project'); os.makedirs(os.path.join(D,'slides'),exist_ok=True)
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

# ---- fraction helpers ----
def F(n,d):
    return (f'<span style="display:inline-flex;flex-direction:column;align-items:center;vertical-align:middle;line-height:1;margin:0 6px;font-size:0.9em">'
            f'<span style="padding:0 6px 3px">{n}</span><span style="border-top:4px solid currentColor;padding:3px 6px 0">{d}</span></span>')
def rp(html,size=38,weight=600,color=None): return p(html,size,weight,color,raw=True)
def aw(left,top,width,html,build='pop',size=40):
    return pin(left,top,width,f'<p style="font-size:{size}px;font-weight:800;line-height:1.2">{html}</p>',build,YEL,20,'14px 26px')
def qr(left,top,width,label,html,size=38):
    return pin(left,top,width,f'<p style="font-size:{size}px;font-weight:600;line-height:1.3"><span style="color:{TEAL};font-weight:800">{E(label)}</span>  {html}</p>',None,WHITE,20,'14px 28px')
def try_raw(sid,time,title,sub,rows,notes,size=38,gap=150):
    body=h2(title)+p(sub,34,600,MUTED)
    for i,(a,b,c) in enumerate(rows): body+=qr(128,340+i*gap,1150,a,b,size)+aw(1320,340+i*gap,472,c)
    return sec(sid,time,body,notes)
def check_raw(sid,time,title,rows,notes,gap=150,size=34):
    body=h2(title)
    for i,(a,b) in enumerate(rows):
        top=250+i*gap
        body+=pin(128,top,150,f'<p style="font-size:34px;font-weight:800;color:{TEAL}">{E(a)}</p>',None,WHITE,20,'18px 24px')
        body+=aw(328,top,1464,b,'pop',size)
    return sec(sid,time,body,notes)
def items(lst,size=38):
    return ''.join(card(rp(f'<span style="color:{TEAL}">{a}</span>  {b}',size)) for a,b in lst)
def sstep(n,html,top,left=128,width=1664,size=36,build='rise'):
    return pin(left,top,width,f'<p style="font-size:{size}px;font-weight:600;line-height:1.3"><span style="color:{TEAL};font-weight:800">Step {n}.</span>  {html}</p>',build,WHITE,20,'18px 28px')
def svgwrap(w,h,label,inner):
    return f'<svg aria-label="{E(label)}" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="width:{w}px;height:{h}px;flex:none">{inner}</svg>'
def T(x,y,t,size=32,col=NAVY,anchor='middle',weight=700):
    return f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" fill="{col}" font-family="Fredoka, Arial">{E(str(t))}</text>'
def sfr(x,y,n,d,size=28,col=NAVY):
    return (T(x,y-5,n,size,col)+f'<line x1="{x-size*0.5:.1f}" y1="{y+1:.1f}" x2="{x+size*0.5:.1f}" y2="{y+1:.1f}" stroke="{col}" stroke-width="3"/>'+T(x,y+size+2,d,size,col))
def bar(x,y,w,h,n,shade=None,label=True,lsize=26,stroke=4):
    s=''; pw=w/n
    for i in range(n):
        f=(shade[i] if shade and i<len(shade) and shade[i] else WHITE)
        s+=f'<rect x="{x+i*pw:.2f}" y="{y}" width="{pw:.2f}" height="{h}" fill="{f}" stroke="{NAVY}" stroke-width="{stroke}"/>'
        if label and n>1: s+=sfr(x+i*pw+pw/2,y+h/2-2,1,n,lsize)
    return s
def pizza(cx,cy,r,n,shade=0,col=YEL):
    """a circle cut into n equal slices; first `shade` slices coloured"""
    import math
    g=f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{WHITE}" stroke="{NAVY}" stroke-width="5"/>'
    if n==1:
        if shade: g=f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{col}" stroke="{NAVY}" stroke-width="5"/>'
        return g
    for i in range(n):
        a0=-math.pi/2+2*math.pi*i/n; a1=-math.pi/2+2*math.pi*(i+1)/n
        x0,y0=cx+r*math.cos(a0),cy+r*math.sin(a0); x1,y1=cx+r*math.cos(a1),cy+r*math.sin(a1)
        fill=col if i<shade else WHITE
        g+=f'<path d="M{cx} {cy} L{x0:.1f} {y0:.1f} A{r} {r} 0 {1 if 2*math.pi/n>math.pi else 0} 1 {x1:.1f} {y1:.1f} Z" fill="{fill}" stroke="{NAVY}" stroke-width="4" stroke-linejoin="round"/>'
    return g
def face(cx,cy,r=34):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{SOFT}" stroke="{NAVY}" stroke-width="4"/><circle cx="{cx-12}" cy="{cy-6}" r="4" fill="{NAVY}"/><circle cx="{cx+12}" cy="{cy-6}" r="4" fill="{NAVY}"/><path d="M{cx-14} {cy+8} Q{cx} {cy+24} {cx+14} {cy+8}" fill="none" stroke="{NAVY}" stroke-width="4"/>'

# ---------- 1. title ----------
put('p5l2-title',title_slide('p5l2-title','LESSON 2  •  WEEK 1','Fraction Feats','Four operations of fractions, fraction and division',
 'Share pizzas fairly, write fractions as unit fractions, take a fraction of a remainder with a model and find patterns in fraction sums.',
 'Objective: Link fractions and division (3 ÷ 4 = 3/4) and divide a proper fraction by a whole number; write fractions as the sum of two different unit fractions by testing in order; solve fraction-of-a-remainder problems forwards and backwards with a bar model; and spot and explain patterns in fraction sums. '
 'Thinking strategies taught today: DRAW A MODEL (bar or pizza), TEST IN ORDER and know when to stop, find the REMAINDER first, LOOK FOR A PATTERN, and test both ways. '
 'Materials: paper circles (about 6 per child) and scissors, a paper strip for bar models, digit cards 1 to 5, mini whiteboards, workbook. '
 'Online: children cut out their paper circles before the lesson and fold or cut them on camera; the tutor shares the slides and draws the bar models live; pairs use breakout rooms for the explore and page 1. '
 'Time plan: warm-up 0 to 9, explore 9 to 21, teaching 21 to 33 (click to reveal each step and answer), brain break 33 to 37, worksheet page 1 37 to 49, check together 49 to 51, short teaching before page 2 51 to 57, worksheet page 2 57 to 72 (alone), check together 72 to 76, talk time 76 to 82, exit ticket 82 to 90. Stretch and challenge are for children who finish early, or for home.'))

# ---------- 2. warm-up game ----------
pairs=[(3,5,3,7),(5,6,6,7),(4,9,1,2),(7,8,8,7)]
g=''
for i,(a,b,c,d) in enumerate(pairs):
    x=30+i*400
    g+=f'<rect x="{x}" y="20" width="360" height="200" rx="20" fill="{WHITE}" stroke="{NAVY}" stroke-width="4"/>'+sfr(x+90,100,a,b,56)+T(x+180,128,'or',36,TEAL)+sfr(x+270,100,c,d,56)
body=h2('Warm-up: Fraction Face-off')+card(p('Which fraction is bigger? One finger for the first, two fingers for the second. Give a reason: no common denominators allowed!',36,700))
body+=pin(128,400,1664,svgwrap(1640,240,'Four pairs of fractions: 3/5 or 3/7, 5/6 or 6/7, 4/9 or 1/2, 7/8 or 8/7',g),None,WHITE,24,'16px 12px')
body+=pin(128,700,1664,p('Clues to use: same top number? Close to 1? More than a half? More than a whole?',36,700),'fade',SOFT,20,'20px 30px')
put('p5l2-warm1',sec('p5l2-warm1','0–4 MIN',body,
 'Minutes 0 to 4. Fraction Face-off. Point to one pair at a time; children show 1 or 2 fingers, then explain. Answers and reasons: 3/5 is bigger than 3/7 (same top number: fewer, bigger pieces, fifths are bigger than sevenths). 6/7 is bigger than 5/6 (5/6 is 1/6 short of 1, 6/7 is only 1/7 short, and 1/7 is smaller than 1/6). 1/2 is bigger than 4/9 (4/9 is less than 4.5/9). 8/7 is bigger than 7/8 (8/7 is more than 1 and 7/8 is less than 1). '
 'Listen for the reasons. Praise "compare to a half" and "how far from 1" as strategies; these come back in the lesson.'))

# ---------- 3. quick questions ----------
qs=[('1.','Write 3 ÷ 4 as a fraction','3/4'),('2.','2/3 + 1/6 = ?','5/6'),('3.','3/4 of 20 = ?','15'),('4.','2/5 × 3/4 = ?','3/10'),('5.','4/5 ÷ 2 = ?','2/5')]
body=h2('Quick questions')+''.join(qrow(128,250+i*128,1250,a,b,36) for i,(a,b,c) in enumerate(qs))+''.join(answer(1420,250+i*128,372,c) for i,(a,b,c) in enumerate(qs))
put('p5l2-warm2',sec('p5l2-warm2','4–9 MIN',body,'Minutes 4 to 9. Read each aloud, whiteboards up together, then click to show. 1) The top is what is shared, the bottom is how many share. 2) 4/6 + 1/6 = 5/6. 3) 20 ÷ 4 = 5, × 3 = 15. 4) 6/20 = 3/10. 5) Cut each of the 4 parts in half: 4/10 = 2/5, or 4 ÷ 2 = 2 on top. Ask: "Who added the bottoms in question 2?" Answers: 3/4, 5/6, 15, 3/10, 2/5.'))

# ---------- 4. explore ----------
g=''.join(pizza(110+i*210,90,70,1,1) for i in range(3))
for i in range(4): g+=face(1020+i*130,90)
g+=T(1280,185,'4 friends',30,TEAL)+T(300,185,'3 pizzas',30,TEAL)
steps=''.join(f'<li>{E(s)}</li>' for s in ['Take 3 paper pizzas. Share them equally among 4 friends.','How much does each friend get? Write it as a fraction.','Can you cut so that each friend gets only 2 pieces?','Now try 5 pizzas among 6 friends, with only 2 pieces each.'])
body=h2('Explore: fair shares')+card(chip('EXPLORE')+f'<ol style="font-size:34px;font-weight:600;padding-left:52px;display:flex;flex-direction:column;gap:6px">{steps}</ol>')
body+=card(svgwrap(1580,200,'Three whole pizzas and four smiling friends waiting for a fair share',g),extra='padding:16px 32px')
put('p5l2-explore1',sec('p5l2-explore1','9–14 MIN',body,'Minutes 9 to 14. Pairs with paper circles (online: each child cuts their own). Ask them to predict first: will each friend get more or less than half a pizza? Let them find any fair way, then push for "only 2 pieces each". Early finishers: 5 pizzas among 6 friends with only 2 pieces each.'))
body=h2('Explore: talk about it')+numcards([('1.','How much pizza does each of the 4 friends get? Write it as a division and as a fraction.'),('2.','How did you cut so that each friend got only 2 pieces?'),('3.','Could you do 5 pizzas among 6 friends with 2 pieces each?')],38)
put('p5l2-explore2',sec('p5l2-explore2','14–21 MIN',body,'Minutes 14 to 21. Gather the pairs. Answers: 1) 3 ÷ 4 = 3/4 of a pizza each (cut every pizza into 4: 12 quarters, 3 each). 2) Cut 2 pizzas into halves and 1 pizza into quarters: each friend gets 1/2 + 1/4 = 3/4, which is 2 pieces. 3) Yes: cut 3 pizzas into halves (6 halves) and 2 pizzas into thirds (6 thirds): each friend gets 1/2 + 1/3 = 5/6. '
 'Say: "This is the same as writing 5/6 as a sum of two different unit fractions: 1/2 + 1/3." That is the puzzle type on the worksheet, but with different numbers. Do not give away the worksheet fractions.'))

# ---------- 6. teach: fraction and division ----------
g=''.join(bar(30,40+i*70,300,50,5,[SKY if j<2 else None for j in range(5)] if False else None,False) for i in range(2))
g=''
for i in range(2): g+=bar(20,30+i*86,360,66,5,[YEL]*5,True,26)
g=''
for i in range(5): pass
# 2 pizzas among 5: each pizza cut in fifths, each friend gets one slice from each
g=pizza(110,130,90,5,0)+pizza(330,130,90,5,0)+T(220,260,'2 pizzas, each cut into 5',28,TEAL)
g+=f'<path d="M410 130 H500" stroke="{TEAL}" stroke-width="7"/><polygon points="520,130 494,114 494,146" fill="{TEAL}"/>'
g+=pizza(640,130,90,5,1,TEAL)+pizza(860,130,90,5,1,TEAL)+T(750,260,'one friend: 1 slice from each',28,TEAL)
body=h2('Fraction and division')+card(rp(f'2 pizzas shared among 5 friends:  2 ÷ 5 = {F(2,5)}.   And {F(3,5)} ÷ 2 = ?',40,700))
body+=pin(128,370,1000,svgwrap(980,290,'Two pizzas cut into fifths; one friend gets one fifth from each pizza',g),None)
body+=pin(1160,380,632,rp(f'Each friend gets {F(1,5)} + {F(1,5)} = {F(2,5)}.',38,700),'rise',SOFT,20,'20px 26px')
body+=sstep(1,f'The top number is what is <b>shared</b>. The bottom number is <b>how many share</b>.',690,size=32)
body+=sstep(2,f'{F(3,5)} ÷ 2: cut each fifth in half. 3 fifths become 6 tenths, shared in 2 groups: 3 tenths. So {F(3,5)} ÷ 2 = {F(3,10)}.',790,size=32)
put('p5l2-teach1',sec('p5l2-teach1','21–24 MIN',body,'Teach. Draw the two pizzas cut in fifths. "Each friend takes one slice from each pizza: 1/5 + 1/5 = 2/5. So 2 ÷ 5 = 2/5." Then the second idea: a fraction divided by a whole number. Draw a bar of 5 parts with 3 shaded; cut every part in half so there are 10 small parts and 6 shaded; two friends share the 6 shaded parts: 3 each, 3/10. Say: "Dividing by 2 makes each piece twice as small, so the bottom number doubles: 3/5 ÷ 2 = 3/10." '
 'Check: 3/10 × 2 = 6/10 = 3/5. Ask: "What is 3/4 ÷ 3?" (1/4: shortcut, the top 3 can be shared in 3 groups of 1.) This is a P6 skill: children who have not met it may need the picture twice.'))
put('p5l2-try1',try_raw('p5l2-try1','24–25 MIN','Your turn: whiteboards','Draw a quick picture if you need one.',[('a',f'4 ÷ 7 as a fraction',F(4,7)),('b',f'{F(4,5)} ÷ 3',F(4,15)),('c',f'{F(6,7)} ÷ 3',F(2,7))],'Whiteboards up together, then click. a) 4 pizzas among 7: 4/7. b) 4/5 ÷ 3: cut each fifth into 3 pieces, so 4 fifths = 12 fifteenths; shared by 3 gives 4 fifteenths: 4/15. c) 6 sevenths shared by 3 is 2 sevenths: 2/7 (the top divides exactly).'))

# ---------- 8. worked example: unit fractions ----------
body=h2('Worked example: two different unit fractions')+card(rp(f'Write {F(7,12)} as the sum of two <b>different</b> unit fractions (1 on top).',38,700))
rows=[(f'Try {F(1,2)}:',f'{F(7,12)} − {F(6,12)} = {F(1,12)}',f'a unit fraction!  {F(1,2)} + {F(1,12)}'),(f'Try {F(1,3)}:',f'{F(7,12)} − {F(4,12)} = {F(3,12)} = {F(1,4)}',f'a unit fraction!  {F(1,3)} + {F(1,4)}'),(f'Try {F(1,4)}:',f'{F(7,12)} − {F(3,12)} = {F(4,12)} = {F(1,3)}',f'the same pair again. Stop!')]
for i,(a,b,c) in enumerate(rows):
    body+=pin(128,380+i*130,1664,rp(f'<span style="color:{TEAL};font-weight:800">{a}</span>  {b}  →  <b>{c}</b>',34,600,),'rise',WHITE,20,'18px 28px')
body+=pin(128,790,1664,p('Why stop? A first part smaller than half of 7/12 would leave a bigger part, and we already tried those.',34,700),'fade',SOFT,20,'18px 28px')
put('p5l2-we1',sec('p5l2-we1','25–28 MIN',body,'Test in order, and know when to stop: today\'s first strategy. Click each row while children work out the subtraction first. Think-aloud: "I list the unit fractions in order, biggest first. 1/2: is it less than 7/12? Yes. 7/12 − 6/12 = 1/12, a unit fraction, so that is one way. 1/3 leaves 3/12 = 1/4, another way. 1/4 leaves 4/12 = 1/3: that is the same pair as before, so I have found them all. A unit fraction must be less than 7/12 and at least half of it (so the two parts can be different and add up): that is 1/2 and 1/3 only." '
 'Why 1/2 can be the first: 1/2 < 7/12. What about 1/1? Too big. Answer: 1/2 + 1/12 and 1/3 + 1/4. Check: 6/12 + 1/12 = 7/12 and 4/12 + 3/12 = 7/12.'))
put('p5l2-try2',try_raw('p5l2-try2','28–29 MIN','Your turn: unit fractions','Test 1/2, 1/3, 1/4 … in order. Subtract and simplify.',[('a',f'{F(5,6)} = unit + unit',f'{F(1,2)} + {F(1,3)}'),('b',f'{F(3,4)} = unit + unit',f'{F(1,2)} + {F(1,4)}'),('c',f'{F(2,5)} = unit + unit',f'{F(1,3)} + {F(1,15)}')],'Whiteboards. a) 5/6 − 1/2 = 1/3 yes; 5/6 − 1/3 = 1/2 (the same pair). b) 3/4 − 1/2 = 1/4 is a unit fraction, so 1/2 + 1/4; 1/3 leaves 5/12, not a unit fraction. c) 1/2 is too big (more than 2/5); 2/5 − 1/3 = 1/15 yes; 1/4 leaves 3/20 no; 1/5 would leave the same 1/5, not different. So one way only. Ask: "How do you know when to stop?"',size=36))

# ---------- 10. worked example: remainder ----------
g=f'<path d="M80 40 V24 H1560 V40" fill="none" stroke="{NAVY}" stroke-width="3"/>'+T(820,12,'180 beads',28,NAVY)
cols=[SKY,YEL,YEL,YEL,YEL,YEL] ; labs=['bracelet','necklace','necklace','necklace','left','']
w=1480/6
for i in range(6):
    c=SKY if i<2 else (YEL if i<5 else WHITE)
    g+=f'<rect x="{80+i*w:.1f}" y="60" width="{w:.1f}" height="80" fill="{c}" stroke="{NAVY}" stroke-width="4"/>'
g+=f'<line x1="{80+2*w:.1f}" y1="40" x2="{80+2*w:.1f}" y2="160" stroke="{RED}" stroke-width="5" stroke-dasharray="12 8"/>'
g+=T(80+w,190,'bracelet: 1/3',28,TEAL)+T(80+w*3.5,190,'necklace: 3/4 of the remainder',28,TEAL)+T(80+5.5*w,190,'left',28,TEAL)
body=h2('Worked example: fraction of a remainder')+card(rp(f'Mei had 180 beads. She used {F(1,3)} of them for a bracelet and {F(3,4)} of the <b>remainder</b> for a necklace. How many beads were left?',34,700))
body+=pin(128,400,1664,svgwrap(1640,230,'A bar for 180 beads in six equal units: two for the bracelet, three for the necklace, one left',f'<g transform="translate(0,16)">{g}</g>'),'fade',WHITE,24,'12px 12px')
body+=sstep(1,f'Bar in 3 parts: bracelet 1 part, remainder 2 parts. Cut the remainder into 4 small units: the whole bar is 6 units.',640,size=32)
body+=sstep(2,f'Bracelet 2 units. Necklace {F(3,4)} of 4 units = 3 units. Left: 1 unit.',770,size=32)
body+=pin(128,860,1664,p('6 units = 180, so 1 unit = 30. 30 beads were left.',38,800),'pop',YEL,20,'14px 28px')
put('p5l2-we2',sec('p5l2-we2','29–32 MIN',body,'The fraction of WHAT? Draw the bar as you go (online: use the slide, then children draw their own). Think-aloud: "A third of the beads is 1 part out of 3. The remainder is the other 2 parts. The necklace uses 3/4 of THAT, so I cut the remainder into 4 equal small units, which means I must cut the bracelet part into 2 so that every unit is the same size. Now the whole bar is 6 units." '
 'Common wrong answer: 3/4 of 180 = 135. Ask: "Is 3/4 of the whole the same as 3/4 of the remainder? Who has more, the bracelet or the necklace?" Check: bracelet 60, remainder 120, necklace 90, left 30. Total 60 + 90 + 30 = 180.'))

# ---------- key + break ----------
body=h2('Key idea: the fraction of WHAT?')+card(p('Find the remainder first, then take the fraction of the remainder. Draw a model with equal small units.',44,700))+card(rp(f'a ÷ b = {F("a","b")}. Unit fractions: test {F(1,2)}, {F(1,3)}, {F(1,4)} … in order and stop when the first part is too small.',36,600,MUTED))
put('p5l2-key',sec('p5l2-key','32–33 MIN',body,'Say the key idea together. Common mistakes to watch for during the worksheet: (1) Taking the second fraction of the whole amount instead of the remainder. (2) Adding tops and bottoms, 1/2 + 1/3 = 2/5, or using the same unit fraction twice when the question says different. (3) Writing 3 ÷ 4 as 4/3, or multiplying instead of dividing when a fraction is shared.'))
put('p5l2-break',break_slide('p5l2-break','33–37 MIN','Fraction freeze: walk on the spot. When the tutor calls a fraction, freeze: arms up for more than a half, arms out for exactly a half, crouch for less than a half.','Five minutes. Call: 3/5 (up), 4/8 (out), 2/9 (crouch), 7/12 (up), 5/10 (out), 11/25 (crouch), 6/11 (up). Ask: "How did you decide without drawing? Compare the top number with half the bottom number."'))

# ---------- worksheet page 1 ----------
put('p5l2-ws1',ws_preview('p5l2-ws1','37–49 MIN','Worksheet page 1: with your partner',[('Q1','Sharing, and fraction and division.'),('Q2','Unit fraction puzzles: test in order, then say when to stop.'),('Q3','Fraction of a remainder: finish the model.')],'Stuck? Draw a bar and cut it into equal units.','Minutes 37 to 49. Walk around. Ask "Is that a fraction of the whole or of the remainder?" before giving any help on Q3. Q2c: ask "How do you know you have found both ways?"'))
put('p5l2-ws1ans',check_raw('p5l2-ws1ans','49–51 MIN','Page 1: check together',[('Q1','a) 5/8   b) 9/4 = 2 1/4 m   c) Group A: 2/3 is more than 3/5   d) (stretch) 1/8'),('Q2','a) 1/2 + 1/5   b) 1/4 + 1/5   c) 1/3 + 1/24 and 1/4 + 1/8'),('Q3','a) 120   b) 60   c) 1/4')],
 'Click each answer after a pair explains. Q1c: 2/3 = 10/15, 3/5 = 9/15; or each child in A is 1/3 short of a pizza, in B 2/5 short. Q1d (stretch, a P6 preview): 3/4 ÷ 6 = 1/8 (3 quarters shared by 6 children is half a quarter each, and half of 1/4 is 1/8). Q2: 7/10 − 1/2 = 2/10 = 1/5, so 1/2 + 1/5. 9/20 − 1/4 = 9/20 − 5/20 = 4/20 = 1/5, so 1/4 + 1/5. 3/8: 1/3 leaves 1/24; 1/4 leaves 1/8; 1/5 leaves 7/40 (not a unit fraction); after that the first part is less than half of 3/8, so stop. Q3: Ben 60, remainder 180, Ali 2/3 of 180 = 120, left 60 = 1/4 of 240.',gap=170))

# ---------- teach: pattern ----------
body=h2('Look for a pattern')+card(rp(f'{F(1,7)} − {F(1,8)} = {F(1,56)} and {F(1,8)} − {F(1,9)} = {F(1,72)}.   What is {F(1,10)} − {F(1,11)}?',34,700))
body+=sstep(1,f'Bottom numbers: 56 = 7 × 8 and 72 = 8 × 9. So {F(1,10)} − {F(1,11)} = {F(1,110)} (10 × 11).',380,size=32)
body+=sstep(2,f'Now add:  {F(1,56)} + {F(1,72)} = ({F(1,7)} − {F(1,8)}) + ({F(1,8)} − {F(1,9)}).',490,size=32)
body+=sstep(3,f'The {F(1,8)} cancels: {F(1,7)} − {F(1,9)} = {F(9,63)} − {F(7,63)} = {F(2,63)}.',600,size=32)
body+=pin(128,730,1664,p('Each fraction is a difference of two unit fractions, so the middle parts cancel.',36,800),'pop',YEL,20,'18px 28px')
put('p5l2-teachpattern',sec('p5l2-teachpattern','51–53 MIN',body,'Teach before worksheet page 2 (Q4). Ask first: "How do you think the bottom numbers are made?" (two neighbouring numbers multiplied: 7 × 8, 8 × 9). Think-aloud: "1/56 + 1/72 looks hard, but each one is a difference. The 1/8 is added in one and taken away in the other, so it disappears." Check: 1/56 + 1/72 = 9/504 + 7/504 = 16/504 = 2/63. Do not show the worksheet fractions: tell the children they will meet a set of fractions with the same trick on page 2.'))

# ---------- teach: backwards ----------
g=''
w=1300/3
for i in range(3):
    c=SKY if i==0 else (YEL if i==1 else WHITE)
    g+=f'<rect x="{80+i*w:.1f}" y="20" width="{w:.1f}" height="80" fill="{c}" stroke="{NAVY}" stroke-width="4"/>'
g+=f'<line x1="{80+2*w:.1f}" y1="20" x2="{80+2*w:.1f}" y2="100" stroke="{NAVY}" stroke-width="4"/>'
g+=T(80+w/2,66,'book',30)+T(80+1.5*w,66,'lunch',30)+T(80+2.5*w,66,'$15 left',30)+T(740,150,'?  (whole bar)',28,TEAL)
body=h2('Working backwards with a model')+card(rp(f'Ali spent {F(1,3)} of his money on a book and {F(1,2)} of the remainder on lunch. He had $15 left. How much did he have at first?',34,700))
body+=pin(128,430,1664,svgwrap(1480,170,'A bar in three equal units: book, lunch and the $15 left',g),'fade',WHITE,24,'12px 12px')
body+=sstep(1,f'Book: 1 of 3 parts. Remainder: 2 parts. Lunch: half of the remainder = 1 part. Left: 1 part.',640,size=32)
body+=sstep(2,'The part left is $15, so 1 part = $15.  3 parts = $45.',740,size=32)
body+=pin(128,830,1664,p('Check: book $15, lunch $15, left $15. Total $45 ✓',38,800),'pop',YEL,20,'18px 28px')
put('p5l2-teachback',sec('p5l2-teachback','53–55 MIN',body,'Teach before worksheet page 2 (Q5). Start from the END of the story: what do we know? The $15 is what is left, so we know the size of one unit. Ask: "Why is the lunch exactly the same size as what is left?" (half of the remainder is spent, so half is left). Common error: working with 1/3 + 1/2 = 5/6 as if both were fractions of the whole. Draw the model first, then work out one unit.'))

# ---------- teach: both ways ----------
body=h2('Test both ways')+card(rp(f'Cards {"1 2 3 5"}: make the SMALLEST sum of two fractions {F("▢","▢")} + {F("▢","▢")}.',36,700))
body+=sstep(1,f'Big digits on the bottom make small pieces. Try 1 and 2 on top:  {F(1,3)} + {F(2,5)} = {F(5,15)} + {F(6,15)} = <b>{F(11,15)}</b>',380,size=32)
body+=sstep(2,f'But test the other way too:  {F(1,5)} + {F(2,3)} = {F(3,15)} + {F(10,15)} = {F(13,15)}  (bigger)',490,size=32)
body+=pin(128,620,1664,rp(f'Smallest sum: {F(1,3)} + {F(2,5)} = {F(11,15)}.   Largest sum: {F(5,1)} + {F(3,2)} = 6 {F(1,2)}.',36,800),'pop',YEL,20,'18px 28px')
body+=pin(128,780,1664,p('Put the big digits on the bottom for the smallest sum, and on the top for the largest.',34,700),'fade',SOFT,20,'18px 28px')
put('p5l2-teachboth',sec('p5l2-teachboth','55–57 MIN',body,'Teach before worksheet page 2 (Q6 uses the cards 1, 2, 3, 4: do not give those away). Ask: "Where should the big digits go for the smallest sum?" Test BOTH ways: 1/3 + 2/5 = 11/15 and 1/5 + 2/3 = 13/15. Largest: 5/1 + 3/2 = 5 + 1 1/2 = 6 1/2. Do the fractions have to be proper? No: 5/1 is a fraction too.'))

# ---------- worksheet page 2 ----------
put('p5l2-ws2',ws_preview('p5l2-ws2','57–72 MIN','Worksheet page 2: on your own',[('Q4','A fraction pattern: find the sums.'),('Q5','Work backwards from the money left. Draw a model.'),('Q6','Digit cards 1 2 3 4: the largest, smallest and closest to 1.')],'Finished early? Stretch and Challenge come next.','Children work alone. Note who needs a short catch-up next lesson, especially children who take the second fraction of the whole instead of the remainder.'))
put('p5l2-ws2ans',check_raw('p5l2-ws2ans','72–76 MIN','Page 2: check together',[('Q4','a) 1/30, 1/42: bottoms are 1 × 2, 2 × 3, 3 × 4 …   b) 2/3, 3/4, 4/5   c) 9/10'),('Q5','a) $120   b) $36'),('Q6','a) 4/1 + 3/2 = 5 1/2   b) 1/3 + 2/4 = 5/6   c) 1/4 + 2/3 = 11/12')],
 'Click after a child explains. Q4: 1/2 + 1/6 = 2/3, + 1/12 = 3/4, + 1/20 = 4/5; each sum is 1 take away the next unit fraction (1 − 1/3, 1 − 1/4, 1 − 1/5), because a unit fraction minus the next unit fraction is 1 over (the number times the next number), for example 1/9 − 1/10 = 1/90. So the sum up to 1/90 (9 × 10) is 1 − 1/10 = 9/10. Q5: 10 equal units; game 4, remainder 6, book 3, left 3 units = $36, so 1 unit is $12, total $120, book $36. Q6: smallest sum: 1/3 + 2/4 = 5/6, test the other way 1/4 + 2/3 = 11/12 (bigger). Largest: 4/1 + 3/2 = 5 1/2. Closest to 1: 11/12 is 1/12 away; 5/6 is 1/6 away.',gap=170))

# ---------- stretch / challenge ----------
st=[('1.','Which is bigger, 5/6 or 6/7? Explain without finding common denominators.'),('2.','Find a fraction between 2/5 and 1/2 with 20 as the bottom number.'),('3.','Which is bigger, 7/8 of 24 or 5/6 of 30?')]
put('p5l2-stretch',sec('p5l2-stretch','For early finishers',h2('Stretch')+items(st,36),'Answers: 1) 6/7: 5/6 is 1/6 short of 1 and 6/7 is only 1/7 short, and 1/7 is smaller than 1/6. 2) 9/20: 2/5 = 8/20 and 1/2 = 10/20. 3) 5/6 of 30 is bigger: 7/8 of 24 = 21 and 5/6 of 30 = 25.'))
ch=[('1.','Work out 1/6 + 1/12 + 1/20 + 1/30 + 1/42. Hint: 1/6 = 1/2 − 1/3.'),('2.','5 pizzas are shared equally among 12 children. Each child must get exactly 2 pieces, and each piece must be a unit fraction of a pizza. How can the pizzas be cut? (Find two ways.)')]
put('p5l2-challenge',sec('p5l2-challenge','For early finishers',h2('Challenge')+items(ch,36),'Pairs try first, then use the "see it" slide if stuck, then the walk-through. These are Think Harder Q5 and Q6. Answers: 1) 5/14: each fraction is a difference ((1/2 − 1/3) + (1/3 − 1/4) + (1/4 − 1/5) + (1/5 − 1/6) + (1/6 − 1/7)), the middle parts cancel, leaving 1/2 − 1/7 = 5/14. 2) Each child gets 5/12. Two ways: 1/3 + 1/12 (cut 4 pizzas into thirds and 1 pizza into twelfths: 12 thirds and 12 twelfths) or 1/4 + 1/6 (cut 3 pizzas into quarters and 2 pizzas into sixths: 12 of each).'))
g1=''
for i,(a,b) in enumerate([(1,6),(1,12),(1,20),(1,30),(1,42)]):
    x=60+i*140; g1+=f'<rect x="{x-50}" y="20" width="100" height="100" rx="14" fill="{WHITE}" stroke="{NAVY}" stroke-width="4"/>'+sfr(x,64,a,b,32)
g1+=T(380,185,'1/6 = 1/2 − 1/3  …  what about 1/12?',30,TEAL)
g1+=f'<rect x="20" y="220" width="720" height="110" rx="14" fill="{SOFT}" stroke="{NAVY}" stroke-width="3"/>'+T(380,288,'Which parts cancel?',34)
g2=''
for i in range(5): g2+=pizza(80+i*140,90,56,1,0)
g2+=T(380,200,'5 pizzas',30,TEAL)
for i in range(12): g2+=face(40+i*58,290,22)
g2+=T(380,360,'12 children, 2 pieces each',30,TEAL)+T(380,410,'5/12 = 1/3 + ?   and   5/12 = 1/4 + ?',32)
body=h2('Challenge: see it',60)+'<div style="display:flex;gap:32px;align-items:flex-start">'
body+=card(f'<p style="font-size:30px;font-weight:700;color:{TEAL}">Q1: A sum of five fractions</p>'+svgwrap(760,350,'Five fractions 1/6, 1/12, 1/20, 1/30 and 1/42 in boxes and a hint about differences',g1).replace('width:760px;height:350px;flex:none','width:100%;height:auto;display:block'),extra='flex:1;min-width:0;padding:20px 24px')
body+=card(f'<p style="font-size:30px;font-weight:700;color:{TEAL}">Q2: 5 pizzas, 12 children</p>'+svgwrap(760,430,'Five whole pizzas and twelve children, each to get two unit-fraction pieces',g2).replace('width:760px;height:430px;flex:none','width:100%;height:auto;display:block'),extra='flex:1;min-width:0;padding:20px 24px')+'</div>'
put('p5l2-chdiag',sec('p5l2-chdiag','For early finishers',body,'Show after pairs have tried the Challenge, or if they are stuck. The pictures show the problem, not the answer. Ask: Q1: "Write 1/12 as a difference of two unit fractions. What happens when you add the differences one after another?" Q2: "How much does each child get? Which two unit fractions add to 5/12? Try the unit fractions in order." Answers are in the Challenge slide notes.'))
body=h2('Challenge: walk-through')+pin(128,250,800,p('Q1: a trail of differences',38,800,TEAL))
for i,t in enumerate(['1/6 = 1/2 − 1/3,  1/12 = 1/3 − 1/4,  …','1/42 = 1/6 − 1/7','The middle parts cancel one by one.','1/2 − 1/7 = 7/14 − 2/14 = 5/14']): body+=pin(128,330+i*110,800,p(t,32),'rise',WHITE)
body+=pin(992,250,800,p('Q2: each child gets 5/12',38,800,TEAL))
for i,t in enumerate(['Test 1/2: too big (6/12 is more than 5/12).','1/3: 5/12 − 4/12 = 1/12 ✓','1/4: 5/12 − 3/12 = 2/12 = 1/6 ✓','1/5: 5/12 − 1/5 = 13/60 is not a unit fraction. Stop.']): body+=pin(992,330+i*110,800,p(t,32),'rise',WHITE)
put('p5l2-chwalk',sec('p5l2-chwalk','Challenge',body,'Use after pairs have tried. Q1: show 1/6 = 1/2 − 1/3 (3/6 − 2/6 = 1/6), then ask the pattern for 1/12 (1/3 − 1/4 = 4/12 − 3/12). Q2: the two ways are 1/3 + 1/12 and 1/4 + 1/6. For 1/3 + 1/12 you need 12 thirds (4 pizzas) and 12 twelfths (1 pizza); for 1/4 + 1/6 you need 12 quarters (3 pizzas) and 12 sixths (2 pizzas). Check: 4 + 1 = 5 and 3 + 2 = 5 pizzas. In the walk-through slide, 5/12 − 1/5 is not a unit fraction, and 1/5 is already less than half of 5/12, so stop (5/12 is 25/60, 1/5 is 12/60, the leftover 13/60).'))

# ---------- talk / exit ----------
body=h2('Talk time')+card(chip('TALK TIME',YEL,NAVY)+rp(f'Ben says {F(1,2)} + {F(1,3)} = {F(2,5)}, because you add the tops and add the bottoms. Is he right? Draw a pizza to show why.',40,600))+card(p('Sentence starters:',34,400,MUTED)+p('“I noticed that …”   “I tested it by …”   “I know because …”',38,600))
put('p5l2-talk',sec('p5l2-talk','76–82 MIN',body,'Minutes 76 to 82. Pairs talk for 2 minutes, then share. Answer: Ben is wrong. 1/2 of a pizza is already more than 2/5, so adding 1/3 more cannot give 2/5. Cut into sixths: 1/2 = 3/6 and 1/3 = 2/6, so the total is 5/6. We can only add the tops when the pieces are the same size. Second question if time: "In Q4, why is each sum 1 take away a unit fraction?" Praise the reasons, not only the answers.'))
body=h2('Exit ticket')+card(chip('EXIT TICKET')+p('(a) 4 pizzas are shared equally among 5 children. How much does each child get?',42,600)+p('(b) Ali had 60 marbles. He gave 1/3 of them to Mei and 1/2 of the remainder to Ben. How many marbles did Ali have left?',42,600))+card(p('Write your answer on a slip of paper. Show it to your tutor. Then collect your stamp in your inquiry journal.',34,400))
put('p5l2-exit',sec('p5l2-exit','82–90 MIN',body,'Minutes 82 to 90. Answers: (a) 4/5 of a pizza. (b) 20 marbles: 1/3 of 60 = 20 to Mei, 40 left, half of 40 = 20 to Ben, 20 left. Extension: write 1 as the sum of three different unit fractions (1/2 + 1/3 + 1/6, the only way).'))

# ---------- write ----------
order=['p5l2-title','p5l2-warm1','p5l2-warm2','p5l2-explore1','p5l2-explore2','p5l2-teach1','p5l2-try1','p5l2-we1','p5l2-try2','p5l2-we2','p5l2-key','p5l2-break','p5l2-ws1','p5l2-ws1ans','p5l2-teachpattern','p5l2-teachback','p5l2-teachboth','p5l2-ws2','p5l2-ws2ans','p5l2-stretch','p5l2-challenge','p5l2-chdiag','p5l2-chwalk','p5l2-talk','p5l2-exit']
assert set(order)==set(S), set(order)^set(S)
sd=os.path.join(D,'slides')
for f in os.listdir(sd):
    if f.endswith('.html') and f[:-5] not in S: os.remove(os.path.join(sd,f))
for i,h in S.items(): open(os.path.join(sd,i+'.html'),'w').write(h)
deck={'v':4,'createdOnFiles':{'v':1,'at':datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')},'lists':'css',
 'title':'Math Inquirers P5: Lesson 2 – Fraction Feats','order':order,'cover':'p5l2-title',
 'sections':{'s1':{'description':'Warm-up and explore','start':'p5l2-title'},'s2':{'description':'Teach: fraction and division, unit fractions, fraction of a remainder','start':'p5l2-teach1'},'s3':{'description':'Worksheet with teaching before each page','start':'p5l2-break'},'s4':{'description':'Stretch, challenge, talk and exit','start':'p5l2-stretch'}},
 'faces':{'fredoka':{'family':'Fredoka','href':'https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&display=swap'},'nunito-sans':{'family':'Nunito Sans','href':'https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@400;600;700&display=swap'}},
 'designSystems':[]}
json.dump(deck,open(os.path.join(D,'deck.json'),'w'),indent=1,ensure_ascii=False)
print(len(order),'slides')

import p5_gaps; p5_gaps.apply(2)
