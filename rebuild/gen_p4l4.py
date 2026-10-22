"""Math Inquirers P4, Lesson 4: Fraction Frontier. Writes split/p4l4/project (deck.json + slides/*.html)."""
import json,os,sys,datetime
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,H)
import slidekit
from slidekit import *
slidekit.FOOT='Math Inquirers P4 Holiday Program  •  Notice it. Test it. Explain why.'
FOOTX=slidekit.FOOT
D=os.path.join(H,'..','split','p4l4','project'); os.makedirs(os.path.join(D,'slides'),exist_ok=True)
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
    return (f'<section id="{sid}" data-transition="fade" style="background:{TEAL};color:{CREAM};font-family:{BF};padding:128px 128px 160px;display:flex;flex-direction:column;justify-content:center;gap:36px">\n'
            f'<p style="font-size:32px;font-weight:700;letter-spacing:4px;color:{YEL}">{E(time)}</p>\n'
            f'<h2 style="font-family:{HF};font-size:110px;font-weight:600;line-height:1.05">Brain break</h2>\n'
            f'<p style="font-size:44px;font-weight:600">{E(text)}</p>\n<p style="font-size:36px;color:#D7EFEA">Then: a drink of water and back to our seats.</p>\n'
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

# ---------- fraction helpers ----------
def fr(n,d,size=40,col=None):
    c=f'color:{col};' if col else ''
    return (f'<span style="display:inline-flex;flex-direction:column;align-items:center;vertical-align:middle;line-height:1;margin:0 6px;font-size:{size}px;{c}">'
            f'<span style="padding:0 6px 3px">{n}</span><span style="border-top:4px solid currentColor;padding:3px 6px 0">{d}</span></span>')
def mx(w,n,d,size=40): return f'{w}{fr(n,d,size)}'
def sfr(x,y,n,d,size=34,fill=NAVY):
    """stacked fraction in SVG; y is the numerator baseline"""
    return txt(x,y,n,size,fill)+f'<line x1="{x-size*0.5}" y1="{y+8}" x2="{x+size*0.5}" y2="{y+8}" stroke="{fill}" stroke-width="4"/>'+txt(x,y+size+10,d,size,fill)
def bars(nb,parts,shaded,x0=4,y0=4,bw=340,bh=100,gap=36,col=YEL):
    g=''; k=0; pw=bw/parts
    for b in range(nb):
        x=x0+b*(bw+gap)
        for i in range(parts):
            g+=f'<rect x="{x+i*pw:.1f}" y="{y0}" width="{pw:.1f}" height="{bh}" fill="{col if k<shaded else WHITE}" stroke="{NAVY}" stroke-width="3"/>'; k+=1
        g+=f'<rect x="{x}" y="{y0}" width="{bw}" height="{bh}" fill="none" stroke="{NAVY}" stroke-width="6"/>'
    return g
def brace(x1,x2,y,up=True,h=24):
    m=(x1+x2)/2; s=-1 if up else 1
    return f'<path d="M{x1} {y} Q{x1} {y+s*h*0.6} {x1+14} {y+s*h*0.6} L{m-12} {y+s*h*0.6} Q{m} {y+s*h*0.6} {m} {y+s*h} Q{m} {y+s*h*0.6} {m+12} {y+s*h*0.6} L{x2-14} {y+s*h*0.6} Q{x2} {y+s*h*0.6} {x2} {y}" fill="none" stroke="{NAVY}" stroke-width="4"/>'
def unitbar(n,shaded,x0,y0,uw,uh=90,col=YEL):
    return ''.join(f'<rect x="{x0+i*uw}" y="{y0}" width="{uw}" height="{uh}" fill="{col if i<shaded else WHITE}" stroke="{NAVY}" stroke-width="4"/>' for i in range(n))

# ---------- 1. title ----------
put('p4l4-title',title_slide('p4l4-title','LESSON 4  •  WEEK 2','Fraction Frontier','Fractions',
 'Change between improper fractions and mixed numbers, find a fraction of a set with a bar model, and compare fractions with different denominators.',
 'Objective: Change between improper fractions and mixed numbers using fraction bars and number lines, find a fraction of a set (and the whole set from a part) with a bar model, and compare fractions with different denominators by making the denominators the same, comparing with one half, or comparing pieces when the numerators are the same. '
 'Thinking strategies taught today: DRAW A MODEL (fraction bars, number lines, bar models), MAKE A LIST IN ORDER and COMPARE WITH A BENCHMARK (one half). '
 'Materials: paper strips (one per child, to fold into halves, quarters and eighths), paper circles to cut into quarters, 30 counters, mini whiteboards and markers. '
 'Online: before the lesson children cut out 3 paper circles and cut each into 4 equal slices; they fold paper strips on camera and hold up mini whiteboards. '
 'Time plan: Warm-up check 1 to 4 (two questions on the key idea; children who get both right and can say why start on the Think Harder pages at minute 34), warm-up game 4 to 6 (one short round), quick questions 6 to 8, explore 8 to 18, teaching 18 to 30 (click to reveal each step and answer; the "your turn" slides are optional, skip them if short of time), brain break 30 to 34, worksheet page 1 from 34 to 50 and check together 50 to 53, short teaching before page 2 from 53 to 58, worksheet page 2 from 58 to 76 and check together 76 to 80, talk time 80 to 85, exit ticket 85 to 88, What was hard? reflection 88 to 90. The Challenge slides and the Think Harder pages are for early finishers and for take-home: they have no fixed time slot. Online: page 1 is pair work, so allow about 2 minutes to move into and out of breakout rooms (or run page 1 as a whole-group screen-share if there are only 8 children).'))

# ---------- 2. warm-up: more or less than a half ----------
cards=[(3,8,'Less: half of 8 is 4'),(5,9,'More: half of 9 is 4½'),(6,12,'Exactly a half'),(7,10,'More: half of 10 is 5'),(2,5,'Less: half of 5 is 2½'),(4,7,'More: half of 7 is 3½')]
body=h2('Warm-up: more or less than a half?')+p('Thumbs up: more than a half.   Thumbs down: less.   Flat hand: exactly a half.',34,600,MUTED)
CW=533
for i,(n,d,a) in enumerate(cards):
    L=128+(i%3)*(CW+32); T=300+(i//3)*300
    body+=pin(L,T,CW,f'<p style="font-family:{HF};font-weight:600;text-align:center">{fr(n,d,66)}</p>',None,WHITE,24,'14px 22px',f'box-sizing:border-box;height:270px;align-items:center;border:4px solid {NAVY};box-shadow:8px 8px 0 {NAVY}')
    body+=pin(L+20,T+196,CW-40,p(a,32,800),'pop',SOFT,16,'10px 18px',f'box-sizing:border-box;align-items:center;border:3px solid {NAVY}')
put('p4l4-warm1',sec('p4l4-warm1','4–6 MIN',body,
 'Minutes 4 to 6 (one short round, about 2 minutes: the Warm-up check came first). More or less than a half? Point to one card at a time. Children show thumbs up (more than a half), thumbs down (less) or a flat hand (exactly a half), then you click to reveal (clicks go 3/8, 5/9, 6/12, 7/10, 2/5, 4/7). '
 'Ask each time: "How do you know?" The quick test: find half of the denominator and compare it with the numerator. 3/8: half of 8 is 4, and 3 is less than 4. 5/9: half of 9 is 4 and a half, and 5 is more. 6/12: half of 12 is 6, exactly a half. '
 'Listen for children who say "5/9 is less because 9 is big". That idea comes back when we compare fractions later.'))

# ---------- 3. quick questions ----------
S30=34
qs=[('1.',f'{fr(1,2,S30)} of 18 = ?','9'),('2.',f'{fr(1,4,S30)} of 20 = ?','5'),('3.',f'{fr(2,3,S30)} = {fr("?",12,S30)}','8'),('4.',f'{fr(3,4,S30)} + {fr(1,8,S30)} = ?',fr(7,8,S30)),('5.',f'1 − {fr(3,10,S30)} = ?',fr(7,10,S30))]
body=h2('Quick questions')
for i,(a,b,c) in enumerate(qs):
    t=240+i*132; body+=rq(128,t,1250,a,b,40)+ra(1420,t,372,c,'pop',40)
put('p4l4-warm2',sec('p4l4-warm2','6–8 MIN',body,'Minutes 6 to 8. Read each aloud, whiteboards up together, then click. Ask for the method: 2) 20 ÷ 4 = 5. 3) Thirds to twelfths: multiply top and bottom by 4, so 8/12. 4) 3/4 = 6/8, and 6/8 + 1/8 = 7/8. 5) 1 whole = 10/10, take away 3/10: 7/10. Answers: 9, 5, 8, 7/8, 7/10.'))

# ---------- 4. explore: pizza party ----------
def pizza(cx,cy,r,filled):
    g=''
    pts=[(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy)]
    for q in range(4):
        a=pts[q]; b=pts[(q+1)%4]
        if q<filled: g+=f'<path d="M{cx} {cy} L{a[0]} {a[1]} A{r} {r} 0 0 1 {b[0]} {b[1]} Z" fill="{YEL}" stroke="{NAVY}" stroke-width="4"/>'
        else: g+=f'<path d="M{cx} {cy} L{a[0]} {a[1]} A{r} {r} 0 0 1 {b[0]} {b[1]} Z" fill="{WHITE}" stroke="{NAVY}" stroke-width="3" stroke-dasharray="10 7"/>'
    return g
g=pizza(110,105,92,4)+pizza(330,105,92,4)+pizza(550,105,92,3)
g+=f'<rect x="760" y="40" width="520" height="130" rx="18" fill="{SOFT}" stroke="{NAVY}" stroke-width="4"/>'+txt(1020,98,'11 slices = ? pizzas',40)+txt(1020,148,'Write it two ways.',32,TEAL)
steps=''.join(f'<li>{E(s)}</li>' for s in ['Cut paper circles into 4 equal slices (quarters).','Ravi\'s group eats 11 slices. Take 11 quarter-slices.','Put the slices together to build whole pizzas.','Write how many pizzas they ate in two different ways.'])
body=h2('Explore: pizza party')+card(chip('EXPLORE')+f'<ol style="font-size:36px;font-weight:600;padding-left:52px;display:flex;flex-direction:column;gap:8px">{steps}</ol>')
body+=card(svgwrap(1600,215,'Three pizzas cut into quarters: two whole pizzas and 3 slices of a third pizza',g),extra='padding:16px 32px')
put('p4l4-explore1',sec('p4l4-explore1','8–13 MIN',body,'Minutes 8 to 13. Pairs use paper quarter-slices (online: cut paper circles on camera). Ask them to predict first: more than 2 pizzas or less? More than 3? Let them write the amount any way they like; listen for "eleven quarters" and "two and three quarters". Early finishers: what if every pizza had 6 slices and they ate 11 slices?'))
body=h2('Explore: talk about it')+numcards([('1.','How many pizzas did they eat? Write it in two ways.'),('2.','How many slices make exactly 3 pizzas?'),('3.','What if each pizza had 6 slices and they ate 11?')],40)
put('p4l4-explore2',sec('p4l4-explore2','13–18 MIN',body,'Minutes 13 to 18. Gather the ideas. Write 11/4 and 2 3/4 side by side and tell children the names: 11/4 is an IMPROPER fraction (the top is bigger than the bottom, so it is more than 1); 2 3/4 is a MIXED number (a whole number and a fraction). They are the same amount. Answers: 1) 11/4 = 2 3/4. 2) 12 slices (12/4 = 3). 3) 11/6 = 1 5/6: one whole pizza and 5 sixths.'))

# ---------- 6. teach: improper -> mixed ----------
B=lambda sh: svgwrap(1100,120,f'Three bars cut into thirds with {sh} thirds shaded',bars(3,3,sh,4,8,340,100,36))
body=h2('Improper fraction to mixed number')+card(p(f'Write {fr(7,3,40)} as a mixed number.',42,700,raw=True))
body+=pin(128,400,1100,B(0),None)
body+=step(1,'3 thirds make 1 whole. Fill the first bar: 3 thirds used.',top=560,size=34)
body+=pin(128,400,1100,B(3),'fade')
body+=step(2,'Fill the second bar: 6 thirds used. 1 third is left.',top=670,size=34)
body+=pin(128,400,1100,B(6),'fade')
body+=step(3,'Put the last third in the third bar: 2 wholes and 1 third.',top=780,size=34)
body+=pin(128,400,1100,B(7),'fade')
body+=pin(1290,390,502,p(f'{fr(7,3,40)} = {mx(2,1,3,40)}',52,800,raw=True)+p('7 ÷ 3 = 2 remainder 1',30,700),'pop',YEL,20,'18px 26px')
put('p4l4-teach1',sec('p4l4-teach1','18–20 MIN',body,'Teach. Strategy: DRAW A MODEL. Ask first: "Is 7/3 more or less than 1? How do you know?" (the top is bigger than the bottom). Click order: step 1, first bar fills, step 2, second bar fills, step 3, the last third, the answer. Think-aloud: "The denominator says 3 pieces make a whole. I have 7 pieces. 3 fill one bar, 3 more fill another, and 1 is left over. That is 2 and 1 third." Show the shortcut at the end: 7 ÷ 3 = 2 remainder 1; the remainder is the number of thirds left over.'))

# ---------- 7. worked example: mixed -> improper ----------
g=bars(5,3,14,4,8,250,90,28)
body=h2('Mixed number to improper fraction')+card(p(f'Write {mx(4,2,3,40)} as an improper fraction.',42,700,raw=True))
body+=pin(128,400,1400,svgwrap(1370,110,'Four whole bars of thirds and 2 thirds of a fifth bar shaded',g),None)
body+=step(1,'Each whole is 3 thirds. 4 wholes = 4 × 3 = 12 thirds.',top=550,size=34)
body+=step(2,'Add the 2 thirds: 12 + 2 = 14 thirds.',top=660,size=34)
body+=pin(128,770,1664,p(f'{mx(4,2,3,40)} = {fr(14,3,40)}      Check: 14 ÷ 3 = 4 remainder 2 ✓',40,800,raw=True),'pop',YEL,20,'14px 26px')
put('p4l4-we1',sec('p4l4-we1','20–22 MIN',body,'Worked example. Ask: "How many thirds are in ONE whole? In 4 wholes?" Children count the shaded thirds on the bars: 3, 6, 9, 12, then 13, 14. Think-aloud: "4 wholes, each cut into 3, is 12 thirds. 2 more thirds make 14 thirds." Watch for the common mistake 4 × 2 = 8 (multiplying the whole number by the numerator): ask them to point to 8 thirds on the bars.'))
put('p4l4-try1',rtry('p4l4-try1','22–23 MIN • OPTIONAL','Your turn: whiteboards','Draw bars if it helps.',[('a',f'Write {fr(9,2,32)} as a mixed number.',mx(4,1,2,32)),('b',f'Write {mx(2,7,8,32)} as an improper fraction.',fr(23,8,32)),('c','How many thirds are there in 4 wholes?','12')],
 'Whiteboards up together, then click. a) 9 halves: 4 wholes use 8 halves, 1 half left: 4 1/2. b) 2 wholes = 16 eighths, plus 7: 23/8. c) 3 thirds in each whole: 4 × 3 = 12 thirds (12/3 = 4).',top=320,gapy=165,qw=1250))

# ---------- 9. teach: number line ----------
x0=60; u=470; y=150
g=f'<line x1="{x0-20}" y1="{y}" x2="{x0+3*u+30}" y2="{y}" stroke="{NAVY}" stroke-width="5"/>'
for k in range(10):
    x=x0+k*u/3; big=k%3==0
    g+=f'<line x1="{x}" y1="{y-(26 if big else 15)}" x2="{x}" y2="{y+(26 if big else 15)}" stroke="{NAVY}" stroke-width="{6 if big else 4}"/>'
    if big: g+=txt(x,y+72,k//3,40)
for lab,k in [('P',2),('Q',4),('R',8)]:
    x=x0+k*u/3
    g+=f'<circle cx="{x}" cy="40" r="26" fill="{YEL}" stroke="{NAVY}" stroke-width="4"/>'+txt(x,52,lab,34)+f'<line x1="{x}" y1="66" x2="{x}" y2="{y-30}" stroke="{TEAL}" stroke-width="5"/><polygon points="{x},{y-20} {x-10},{y-38} {x+10},{y-38}" fill="{TEAL}"/>'
body=h2('Fractions on a number line')+p('This number line is marked in thirds. Which number is at P, Q and R?',34,600,MUTED)
body+=pin(128,310,1664,svgwrap(1500,240,'Number line from 0 to 3 marked in thirds, with arrows P, Q and R',g),None)
for i,h in enumerate([f'P = {fr(2,3,32)}',f'Q = {fr(4,3,32)} = {mx(1,1,3,32)}',f'R = {fr(8,3,32)} = {mx(2,2,3,32)}']):
    body+=pin(128+i*568,600,500,p(h,40,800,raw=True),'pop',YEL,20,'12px 26px')
body+=pin(128,770,1664,p('Count the small jumps from 0. Each jump is one third. 3 jumps make 1 whole.',34,700),None,SOFT,20,'18px 28px')
put('p4l4-teachline',sec('p4l4-teachline','23–26 MIN',body,'Teach (before Q2 of page 1, which uses quarters). Count the small jumps aloud from 0: one third, two thirds, three thirds (= 1), four thirds, five thirds, six thirds (= 2) … Click to reveal P, Q and R. Ask: "R is 8 thirds. How else can we write it?" (2 wholes and 2 thirds). "Where would 7/3 go?" (one small jump after 2).'))

# ---------- 10. worked example: fraction of a set ----------
uw=220; g=brace(40,40+5*uw,92,True,34)+txt(40+2.5*uw,34,'30 stickers',34,TEAL)+unitbar(5,3,40,100,uw)
g+=brace(40,40+3*uw,200,False,34)+txt(40+1.5*uw,272,'? star stickers',34,NAVY)
body=h2('Fraction of a set: use a bar model')+card(p(f'Mei has 30 stickers. {fr(3,5,36)} of them are stars. How many star stickers does she have?',38,700,raw=True))
body+=pin(128,380,1250,svgwrap(1200,290,'A bar of 5 equal units for 30 stickers, with 3 units shaded for the star stickers',g),None)
body+=step(1,'The denominator is 5: cut the bar into 5 equal units.',top=690,size=34)
body+=step(2,'5 units = 30, so 1 unit = 30 ÷ 5 = 6.',top=790,size=34,width=1080)
body+=step(3,'3 units = 3 × 6 = 18.',left=1310,top=790,width=482,size=34)
body+=answer(1420,500,372,'18 stars')
put('p4l4-we2',sec('p4l4-we2','26–28 MIN',body,'Strategy: DRAW A BAR MODEL. The whole bar is ALL the stickers. The denominator tells how many equal units to cut it into; the numerator tells how many units we want. Think-aloud: "30 stickers in 5 equal units: each unit is 6. Stars are 3 units: 18." Ask: "How many stickers are NOT stars?" (2 units = 12). Watch for children who divide by 3 (the numerator).'))
put('p4l4-try2',rtry('p4l4-try2','28–29 MIN • OPTIONAL','Your turn: fraction of a set','Draw the bar. Find 1 unit first.',[('a',f'{fr(3,4,32)} of 28 = ?','21'),('b',f'{fr(5,6,32)} of 42 = ?','35'),('c',f'Siti has 36 stamps. She gives away {fr(1,4,32)} of them. How many are left?','27')],
 'Whiteboards. a) 28 ÷ 4 = 7, 3 × 7 = 21. b) 42 ÷ 6 = 7, 5 × 7 = 35. c) 1 unit = 36 ÷ 4 = 9; she gives away 9 and keeps 3 units = 27. Ask: "Could you do c in one step?" (she keeps 3/4 of 36 = 27).',top=320,gapy=165,qw=1250,size=36))

# ---------- key / break ----------
body=h2('Key idea: fractions can be more than 1')+card(p(f'The denominator tells how many pieces make 1 whole:  {fr(7,3,40)} = {mx(2,1,3,40)}',44,700,raw=True))+card(p('Fraction of a set: the denominator gives the number of units. Find 1 unit, then take the units you need.',38,600,MUTED))
put('p4l4-key',sec('p4l4-key','29–30 MIN',body,'Say the key idea together. Common mistakes to watch for during the worksheet: (1) Changing a mixed number to an improper fraction by multiplying the whole number by the numerator, or forgetting to add the numerator (3 2/5 written as 6/5 or 15/5). (2) Thinking the bigger denominator means the bigger fraction (3/7 > 3/5 "because 7 is bigger than 5"). (3) Finding a fraction of a set by dividing by the numerator, or stopping at one unit (3/8 of 24 answered 8 or 3).'))
put('p4l4-break',break_slide('p4l4-break','30–34 MIN','Fraction stand-up. Stand up if the fraction is more than 1, sit down if it is less than 1, hands on your head if it is exactly 1.','Four minutes. Call out: 5/4 (stand), 3/8 (sit), 6/6 (hands on head), 9/5 (stand), 7/12 (sit), 12/12 (hands on head). Then let a child call the fractions. Online: children stand and sit on camera.'))

# ---------- worksheet page 1 ----------
put('p4l4-ws1',ws_preview('p4l4-ws1','34–50 MIN','Worksheet page 1: with your partner',[('Q1','Fraction bars. Count the pieces, then fill whole bars.'),('Q2','Number line in quarters. Count the small jumps.'),('Q3','Fraction of a set. Use the bar model.')],'Stuck? Fold a paper strip, or draw the bars.','Minutes 34 to 50. Walk around. Ask "How many pieces make one whole?" before giving any help. Q2 C is 10 quarters: children may write 2 2/4 or 2 1/2; both are right.'))
put('p4l4-ws1ans',checks('p4l4-ws1ans','50–53 MIN','Page 1: check together',[('Q1','a) 13 fifths: 13/5 = 2 3/5    b) 4 3/4    c) 17/5    d) 40'),('Q2','A = 3/4,  B = 1 3/4,  C = 2 2/4 = 2 1/2.   9/4 = 2 1/4: one small mark after 2'),('Q3','8 units = 24, 1 unit = 3.   a) 9 children   b) 15 children')],
 'Click each answer after a pair explains theirs. Q1c: 3 wholes = 15 fifths, plus 2 = 17 fifths. Q1d: 8 eighths in each whole, 5 × 8 = 40. Q3: glasses 3 units = 9; no glasses 5 units = 15 (or 24 − 9).',gapy=170))

# ---------- teach before page 2: compare ----------
cols=[('Same denominator',f'{fr(2,3,38)} or {fr(5,9,38)} ?',f'{fr(2,3,34)} = {fr(6,9,34)}, and {fr(6,9,34)} is more than {fr(5,9,34)}',f'{fr(2,3,38)} is bigger'),
      ('Compare with a half',f'{fr(3,8,38)} or {fr(4,7,38)} ?',f'Half of 8 is 4: {fr(3,8,34)} is less than a half. Half of 7 is 3½: {fr(4,7,34)} is more.',f'{fr(4,7,38)} is bigger')]
body=h2('Comparing fractions: tools 1 and 2')
for i,(head,qq,why,ans) in enumerate(cols):
    L=128+i*864
    body+=pin(L,240,800,p(head,36,800,TEAL)+p(qq,40,700,raw=True),None,WHITE,20,'18px 24px','box-sizing:border-box;height:190px')
    body+=pin(L,450,800,p(why,32,700,raw=True),'fade',SOFT,20,'18px 24px','box-sizing:border-box;height:240px')
    body+=pin(L,715,800,p(ans,40,800,raw=True),'pop',YEL,20,'14px 24px','box-sizing:border-box')
put('p4l4-teachcompare',sec('p4l4-teachcompare','53–54 MIN',body,'Minutes 53 to 54. Teach before worksheet page 2 (Q4). The tools are split over two slides so that each has room. Click each column: the reason, then the answer. Tool 1: change one fraction so the denominators match (2/3 = 6/9: multiply top and bottom by 3). Show it with paper strips: a strip in thirds and a strip in ninths, same length. Tool 2: compare each with a half, the "half of the denominator" test from the warm-up. Next slide: tool 3 and how to choose.'))
body=h2('Comparing fractions: tool 3, and which tool?')
body+=pin(128,240,800,p('Same numerator',36,800,TEAL)+p(f'{fr(2,5,40)} or {fr(2,9,40)} ?',40,700,raw=True),None,WHITE,20,'18px 24px','box-sizing:border-box;height:190px')
body+=pin(128,450,800,p('Both have 2 pieces. Fifths are bigger pieces than ninths.',32,700),'fade',SOFT,20,'18px 24px','box-sizing:border-box;height:240px')
body+=pin(128,715,800,p(f'{fr(2,5,40)} is bigger',40,800,raw=True),'pop',YEL,20,'14px 24px','box-sizing:border-box')
body+=pin(992,240,800,p('Which tool is quickest?',36,800,TEAL))
for i,t in enumerate(['Denominators that go into each other (3 and 9): make the denominators the same.','One fraction near a half: compare each with a half.','Same numerator: the bigger pieces win.']): body+=pin(992,330+i*150,800,p(t,32,700),'rise',WHITE,20,'18px 24px')
put('p4l4-teachcompare2',sec('p4l4-teachcompare2','54–55 MIN',body,'Minutes 54 to 55. Tool 3: same numerator, so look at the size of the pieces: sharing among 5 gives bigger pieces than sharing among 9. Then the choosing card on the right: click each line and ask the group for an example. Ask: "Which tool is quickest for 5/6 and 3/4?" (same denominator: twelfths).'))
put('p4l4-trycompare',rtry('p4l4-trycompare','55–56 MIN • OPTIONAL','Your turn: which is bigger?','Choose a tool. Then explain.',[('a',f'{fr(5,6,32)}  or  {fr(3,4,32)} ?',f'{fr(5,6,32)} (10/12 &gt; 9/12)'),('b',f'{fr(4,10,32)}  or  {fr(5,8,32)} ?',f'{fr(5,8,32)} (more than a half)'),('c',f'{fr(3,4,32)}  or  {fr(3,10,32)} ?',f'{fr(3,4,32)} (bigger pieces)')],
 'Whiteboards. a) Twelfths: 5/6 = 10/12 and 3/4 = 9/12, so 5/6. b) 4/10 is less than a half (half of 10 is 5); 5/8 is more than a half (half of 8 is 4). c) Same numerator: quarters are bigger pieces than tenths, so 3/4.',top=320,gapy=165,qw=1000,size=36,asize=32))

# ---------- teach: find the whole ----------
uw=240; g=brace(40,40+3*uw,92,True,34)+txt(40+1.5*uw,34,'? marbles in the bag',34,TEAL)+unitbar(3,2,40,100,uw,90,SKY)
g+=brace(40,40+2*uw,200,False,34)+txt(40+uw,272,'24 blue marbles',34,NAVY)
body=h2('Find the whole from a part')+card(p(f'{fr(2,3,36)} of the marbles in a bag are blue. There are 24 blue marbles. How many marbles are in the bag?',36,700,raw=True))
body+=pin(128,455,820,svgwrap(800,290,'A bar of 3 equal units for the whole bag, with 2 units shaded for the 24 blue marbles',g),None)
body+=step(1,'The whole bag is 3 units. 2 units are blue.',left=990,top=470,width=802,size=32)
body+=step(2,'2 units = 24, so 1 unit = 24 ÷ 2 = 12.',left=990,top=585,width=802,size=32)
body+=step(3,'3 units = 3 × 12 = 36.',left=990,top=700,width=802,size=32)
body+=answer(128,810,1664,f'36 marbles.  Check: 36 ÷ 3 = 12, 2 × 12 = 24 ✓')
put('p4l4-teachwhole',sec('p4l4-teachwhole','56–57 MIN',body,'Teach before worksheet page 2 (Q5). This time we know a PART, not the whole. Draw the whole bar in 3 units and shade 2 units; the 24 goes under the shaded part, the question mark over the whole. Think-aloud: "2 units are 24, so 1 unit is 12. The bag is 3 units: 36." Watch for children who find 2/3 of 24 (= 16): ask "Is the bag bigger or smaller than the blue marbles?"'))

# ---------- teach: find all ----------
body=h2('Find ALL: make the denominators the same')
body+=pin(128,240,1664,p(f'Fractions with denominator 8 between {fr(1,4,34)} and {fr(3,4,34)}',38,800,TEAL,raw=True))
for i,t in enumerate([f'{fr(1,4,34)} = {fr(2,8,34)}  and  {fr(3,4,34)} = {fr(6,8,34)}',f'In between: {fr(3,8,34)}, {fr(4,8,34)}, {fr(5,8,34)}',f'{fr(2,8,34)} and {fr(6,8,34)} are EQUAL to the ends: they do not count.']): body+=pin(128,340+i*130,1664,p(t,34,raw=True),'rise',WHITE)
body+=pin(128,750,1664,p('3 fractions.  Make a list in order, so none is missed.',40,800),'pop',YEL,20,'14px 28px')
put('p4l4-teachfind',sec('p4l4-teachfind','57–58 MIN',body,'Minutes 57 to 58. Teach before worksheet page 2 (Q6). Strategy: MAKE A LIST IN ORDER. Change the end fractions to eighths, then list every eighth in between. The ends themselves do not count, because "between" means bigger than one and smaller than the other. The "Who am I?" riddle is now on the Think Harder page (stretch 4): it uses the same idea, list everything that fits the first clues and then cross out with each new clue (example: improper fraction, denominator 4, between 1 and 2, odd numerator, closer to 2 than to 1: 5/4, 6/4, 7/4; odd: 5/4, 7/4; closer to 2: 7/4).'))

# ---------- worksheet page 2 ----------
put('p4l4-ws2',ws_preview('p4l4-ws2','58–76 MIN','Worksheet page 2: on your own',[('Q4','Compare. Choose a tool and explain.'),('Q5','The red sweets. Draw the bar: you know a part, not the whole.'),('Q6','Find ALL the twelfths in between.')],'Finished early? Stretch and Challenge come next.','Children work alone. Note who needs a short catch-up next lesson, especially children who still think a bigger denominator means a bigger fraction.'))
put('p4l4-ws2ans',checks('p4l4-ws2ans','76–80 MIN','Page 2: check together',[('Q4','a) >   b) >   c) <   d) >   e) 7/12, 2/3, 5/6   (a reason is needed in part c only)'),('Q5','3 units = 27, 1 unit = 9.   a) 45 sweets   b) 18 not red'),('Q6','5/12, 6/12, 7/12, 8/12: 4 fractions')],
 'Click after a child explains. Q4a: 3/4 = 6/8. b) 2/3 = 8/12. c) 4/9 is less than a half, 5/8 is more. d) Fifths are bigger pieces than sevenths. e) In twelfths: 7/12, 8/12, 10/12. Q6: 1/3 = 4/12 and 3/4 = 9/12; the ends do not count. (Who am I? is now Think Harder stretch 4: 17/6, because 13/6, 15/6, 17/6 are odd, and only 17/6 is closer to 3.)',gapy=150))

# ---------- stretch / challenge ----------
st=[('1.','How many halves are there in 6 1/2?'),('2.','Which is closer to 1: 7/8 or 9/10? Explain.'),('3.','Ben has 48 marbles. 5/8 of them are green. How many marbles are NOT green?')]
put('p4l4-stretch',sec('p4l4-stretch','Early finishers / take-home',h2('Stretch')+numcards(st),'Answers: 1) 13 (6 wholes = 12 halves, plus 1). 2) 9/10: it is only 1/10 short of 1, and 7/8 is 1/8 short; a tenth is a smaller piece than an eighth. 3) 18 (1 unit = 48 ÷ 8 = 6; green 5 units = 30; not green 3 units = 18).'))
ch=[('1.','Half of a number is 3 more than a third of the number. What is the number?'),('2.','Siti read 2/5 of her book on Monday. On Tuesday she read half of the pages that were left. She still has 45 pages to read. How many pages are in the book?')]
put('p4l4-challenge',sec('p4l4-challenge','Early finishers / take-home',h2('Challenge')+numcards(ch,36),'Pairs try first, then use the "see it" slide if stuck, then the walk-through. These are Think Harder Q6 and Q7. Answers: 1) 18 (half = 3 sixths, a third = 2 sixths, so 1 sixth = 3). 2) 150 pages (Monday 4 tenths, Tuesday 3 tenths, 3 tenths left = 45).'))
g1=f'<rect x="40" y="70" width="680" height="80" fill="{WHITE}" stroke="{NAVY}" stroke-width="4"/><rect x="40" y="70" width="340" height="80" fill="{YEL}" stroke="{NAVY}" stroke-width="4"/>'+txt(210,122,'a half',34)
g1+=f'<rect x="40" y="200" width="680" height="80" fill="{WHITE}" stroke="{NAVY}" stroke-width="4"/>'+''.join(f'<line x1="{40+680*k/3:.1f}" y1="200" x2="{40+680*k/3:.1f}" y2="280" stroke="{NAVY}" stroke-width="4"/>' for k in (1,2))+f'<rect x="40" y="200" width="226.7" height="80" fill="{SKY}" stroke="{NAVY}" stroke-width="4"/>'+txt(153,252,'a third',34)
g1+=brace(40,720,66,True,28)+txt(380,28,'the number = ?',30,TEAL)
g1+=f'<line x1="266.7" y1="160" x2="266.7" y2="300" stroke="{RED}" stroke-width="3" stroke-dasharray="8 6"/><line x1="380" y1="160" x2="380" y2="300" stroke="{RED}" stroke-width="3" stroke-dasharray="8 6"/>'
g1+=brace(266.7,380,300,False,30)+txt(323,370,'3 more',32,RED)
g1+=txt(380,440,'Can you cut both bars into the same pieces?',28,MUTED,weight=600,font='Nunito Sans, Arial')
g2=brace(40,720,66,True,28)+txt(380,28,'the whole book = ?',30,TEAL)
g2+=''.join(f'<rect x="{40+136*k}" y="70" width="136" height="90" fill="{SKY if k<2 else WHITE}" stroke="{NAVY}" stroke-width="4"/>' for k in range(5))
g2+=txt(176,200,'Monday',30,TEAL)+f'<line x1="516" y1="70" x2="516" y2="160" stroke="{RED}" stroke-width="4" stroke-dasharray="10 7"/>'
g2+=brace(312,720,170,False,34)+txt(516,240,'the rest',30,NAVY)
g2+=brace(312,516,280,False,30)+txt(414,345,'Tuesday: half',28,TEAL)+brace(516,720,280,False,30)+txt(618,345,'45 pages left',28,RED)
g2+=txt(380,440,'Cut every fifth in half. What do you get?',28,MUTED,weight=600,font='Nunito Sans, Arial')
body=h2('Challenge: see it',60)+'<div style="display:flex;gap:32px;align-items:flex-start">'
body+=card(f'<p style="font-size:30px;font-weight:700;color:{TEAL}">Q1: a half and a third</p>'+svgwrap(760,470,'Two bars of the same length: one with a half shaded, one with a third shaded; the gap between them is 3',g1).replace('width:760px;height:470px;flex:none','width:100%;height:auto;display:block'),extra='flex:1;min-width:0;padding:20px 24px')
body+=card(f'<p style="font-size:30px;font-weight:700;color:{TEAL}">Q2: Siti\'s book</p>'+svgwrap(760,470,'A bar in fifths: 2 fifths read on Monday; the rest is split in half: Tuesday and 45 pages left',g2).replace('width:760px;height:470px;flex:none','width:100%;height:auto;display:block'),extra='flex:1;min-width:0;padding:20px 24px')+'</div>'
put('p4l4-chdiag',sec('p4l4-chdiag','Early finishers / take-home',body,'Show after pairs have tried the Challenge, or if they are stuck. The pictures show the problem, not the answer. Ask: In Q1, how could you cut both bars into the same size pieces? (sixths). In Q2, the rest is 3 fifths; how can we cut 3 fifths in half? (make tenths). Answers are in the Challenge slide notes.'))
body=h2('Challenge: walk-through')+pin(128,250,800,p('Q1: cut both bars into sixths',38,800,TEAL))
for i,t in enumerate([f'A half = {fr(3,6,26)}.  A third = {fr(2,6,26)}.',f'The difference is {fr(1,6,26)}, and that is 3.',f'The number is {fr(6,6,26)}: 6 × 3 = 18.','Check: half of 18 is 9, a third is 6. 9 is 3 more ✓']): body+=pin(128,330+i*130,800,p(t,30,raw=True),'rise',WHITE)
body+=pin(992,250,800,p('Q2: cut each fifth in half',38,800,TEAL))
for i,t in enumerate([f'Monday {fr(2,5,26)} = {fr(4,10,26)}. The rest is {fr(6,10,26)}.',f'Tuesday: half of the rest = {fr(3,10,26)}.',f'Left: {fr(3,10,26)} = 45 pages, so {fr(1,10,26)} = 15.','The book is 10 × 15 = 150 pages ✓']): body+=pin(992,330+i*130,800,p(t,30,raw=True),'rise',WHITE)
put('p4l4-chwalk',sec('p4l4-chwalk','Early finishers / take-home',body,'Use after pairs have tried. Q1: guess and check also works (try 12: 6 and 4, only 2 more; try 18: 9 and 6, 3 more). The sixths idea shows WHY: the gap between a half and a third is always one sixth. Q2: check forwards: Monday 2/5 of 150 = 60, rest 90, Tuesday 45, left 45 ✓. A common mistake is to say Tuesday is half of the whole book.'))

# ---------- talk / exit ----------
body=h2('Talk time')+card(chip('TALK TIME',YEL,NAVY)+p(f'Which is more: {mx(2,1,3,40)} pizzas or {fr(9,4,40)} pizzas? A character in our story, Mei, says {fr(9,4,40)} because 9 is a big number. Is her idea right?',42,600,raw=True))+card(p('Sentence starters:',34,400,MUTED)+p('“I noticed that …”   “I tested it by …”   “I know because …”',38,600))
put('p4l4-talk',sec('p4l4-talk','80–85 MIN',body,'Minutes 80 to 85. Pairs talk for 2 minutes, then share. Answer: 2 1/3 is more. 9/4 = 2 1/4, so both have 2 wholes; a third is bigger than a quarter (sharing a pizza among 3 gives bigger slices than among 4). Mei is a made-up character, not a child in the group: say "her idea", never name a real child. Mei looked only at the 9, but quarters are small pieces. Second question if time: "Ravi says 3/7 is bigger than 3/5 because 7 is bigger than 5. What would you tell him?" (fifths are bigger pieces, so 3/5 is bigger). Praise the reasons, not only the answers.'))
body=h2('Exit ticket')+card(chip('EXIT TICKET')+p(f'Write {fr(23,5,44)} as a mixed number. Then find {fr(3,5,44)} of 25.',46,600,raw=True))+card(p('Write your answer on a slip of paper. Show it to your tutor. Then collect your stamp in your inquiry journal.',34,400))
put('p4l4-exit',sec('p4l4-exit','85–88 MIN',body,'Minutes 85 to 88. Answers: 23/5 = 4 3/5 (23 ÷ 5 = 4 remainder 3). 3/5 of 25 = 15 (1 unit = 5, 3 units = 15). Extension: find a fraction between 2/3 and 3/4 (for example 17/24, because 2/3 = 16/24 and 3/4 = 18/24).'))

# ---------- write ----------
# ---------- fix pass (rebuild/p4_fix.py): sneak-peek puzzles, looking back, neutral names, go further, minute labels ----------
import subprocess as _sp, p4_fix
_G=json.loads(_sp.check_output(['node','-e',"process.stdout.write(JSON.stringify(require('"+os.path.join(H,'..','p4','content','l4.js')+"').gaps))"]))
_ID='p4l4'
_PIC=globals().get('PIC')

order=['p4l4-title','p4l4-warm1','p4l4-warm2','p4l4-explore1','p4l4-explore2','p4l4-teach1','p4l4-we1','p4l4-try1','p4l4-teachline','p4l4-we2','p4l4-try2','p4l4-key','p4l4-break','p4l4-ws1','p4l4-ws1ans','p4l4-teachcompare','p4l4-teachcompare2','p4l4-trycompare','p4l4-teachwhole','p4l4-teachfind','p4l4-ws2','p4l4-ws2ans','p4l4-stretch','p4l4-challenge','p4l4-chdiag','p4l4-chwalk','p4l4-talk','p4l4-exit']
p4_fix.finish(S,4,_G,pic=_PIC)
order=p4_fix.order(order,4)
assert set(order)==set(S), set(order)^set(S)
sd=os.path.join(D,'slides')
for f in os.listdir(sd):
    if f.endswith('.html') and f[:-5] not in S: os.remove(os.path.join(sd,f))
for i,h in S.items(): open(os.path.join(sd,i+'.html'),'w').write(h)
deck={'v':4,'createdOnFiles':{'v':1,'at':datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')},'lists':'css',
 'title':'Math Inquirers P4: Lesson 4 – Fraction Frontier','order':order,'cover':'p4l4-title',
 'sections':{'s1':{'description':'Warm-up and explore','start':'p4l4-title'},'s2':{'description':'Teach: improper fractions, mixed numbers and fraction of a set','start':'p4l4-teach1'},'s3':{'description':'Worksheet with teaching before each page','start':'p4l4-break'},'s4':{'description':'Stretch, challenge, talk and exit','start':'p4l4-stretch'}},
 'faces':{'fredoka':{'family':'Fredoka','href':'https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&display=swap'},'nunito-sans':{'family':'Nunito Sans','href':'https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@400;600;700&display=swap'}},
 'designSystems':[]}
json.dump(deck,open(os.path.join(D,'deck.json'),'w'),indent=1,ensure_ascii=False)
print(len(order),'slides')
