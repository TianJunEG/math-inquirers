"""Math Inquirers P3, Lesson 6: Fraction Walls. Writes split/p3l6/project (deck.json + slides/*.html).
Every fraction drawing cuts a whole into exactly equal parts (widths, angles or grid squares computed from the whole)."""
import json,os,sys,math
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,H)
from slidekit import *
D=os.path.join(H,'..','split','p3l6','project'); os.makedirs(os.path.join(D,'slides'),exist_ok=True)
S={}; ORDER=[]
def put(i,h): S[i]=h; ORDER.append(i)
RED='#D64545'

# ---------- local helpers ----------
def title_slide(sid,label,title,topic,today,notes):
    return (f'<section id="{sid}" data-transition="fade" style="background:{NAVY};color:{CREAM};font-family:{BF};padding:128px 128px 160px;display:flex;flex-direction:column;justify-content:center;gap:36px">\n'
            f'<p style="font-size:32px;font-weight:700;letter-spacing:4px;color:{YEL}">{E(label)}</p>\n'
            f'<h1 style="font-family:{HF};font-size:128px;font-weight:600;line-height:1.05">{E(title)}</h1>\n'
            f'<p style="font-size:44px;color:#C9D4EC">{E(topic)}</p>\n'
            f'<div style="background:#26385F;border-radius:24px;padding:40px;display:flex;flex-direction:column;gap:12px"><p style="font-size:28px;font-weight:700;letter-spacing:3px;color:{YEL}">TODAY WE WILL</p><p style="font-size:44px;font-weight:600">{E(today)}</p></div>\n'
            f'<p style="position:absolute;left:128px;bottom:64px;width:1400px;font-size:24px;color:#B7C3DD">{E(FOOT)}</p>\n<aside>{E(notes)}</aside>\n</section>\n')
def break_slide(sid,time,big,small,notes):
    return (f'<section id="{sid}" data-transition="fade" style="background:{TEAL};color:{CREAM};font-family:{BF};padding:128px 128px 160px;display:flex;flex-direction:column;justify-content:center;gap:36px">\n'
            f'<p style="font-size:32px;font-weight:700;letter-spacing:4px;color:{YEL}">{E(time)}</p>\n'
            f'<h2 style="font-family:{HF};font-size:110px;font-weight:600;line-height:1.05">Brain break</h2>\n'
            f'<p style="font-size:48px;font-weight:600">{E(big)}</p>\n<p style="font-size:36px;color:#D7EFEA">{E(small)}</p>\n'
            f'<p style="position:absolute;left:128px;bottom:64px;width:1400px;font-size:24px;color:#D7EFEA">{E(FOOT)}</p>\n<aside>{E(notes)}</aside>\n</section>\n')
def F(n,d):
    """stacked fraction in slide text (inherits the font size)"""
    return (f'<span style="display:inline-flex;flex-direction:column;align-items:center;vertical-align:middle;line-height:1;margin:0 6px;font-size:0.9em">'
            f'<span style="padding:0 6px 3px">{n}</span><span style="border-top:4px solid currentColor;padding:3px 6px 0">{d}</span></span>')
BOX='<span style="display:inline-block;width:0.9em;height:0.9em;border:4px solid currentColor;border-radius:8px;background:#FFFFFF"></span>'
def rp(html,size=38,weight=600,color=None): return p(html,size,weight,color,raw=True)
def aw(left,top,width,html,build='pop',size=40):
    return pin(left,top,width,f'<p style="font-size:{size}px;font-weight:800;line-height:1.2">{html}</p>',build,YEL,20,'14px 26px')
def qr(left,top,width,label,html,size=38):
    return pin(left,top,width,f'<p style="font-size:{size}px;font-weight:600;line-height:1.3"><span style="color:{TEAL};font-weight:800">{E(label)}</span>  {html}</p>',None,WHITE,20,'14px 28px')
def try_raw(sid,time,title,sub,rows,notes,size=40,gap=150):
    body=h2(title)+p(sub,34,600,MUTED)
    for i,(a,b,c) in enumerate(rows): body+=qr(128,340+i*gap,1250,a,b,size)+aw(1420,340+i*gap,372,c)
    return sec(sid,time,body,notes)
def check_raw(sid,time,title,rows,notes,gap=140,size=34):
    body=h2(title)
    for i,(a,b) in enumerate(rows):
        top=250+i*gap
        body+=pin(128,top,150,f'<p style="font-size:34px;font-weight:800;color:{TEAL}">{E(a)}</p>',None,WHITE,20,'18px 24px')
        body+=aw(328,top,1464,b,'pop',size)
    return sec(sid,time,body,notes)
def items(lst,size=38):
    return ''.join(card(rp(f'<span style="color:{TEAL}">{a}</span>  {b}',size)) for a,b in lst)
def svgwrap(label,w,h,body,style=None):
    st=style or f'width:{w}px;height:{h}px'
    return f'<svg aria-label="{E(label)}" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="{st};display:block">{body}</svg>'
def T(x,y,t,size=32,col=NAVY,anchor='middle',weight=700):
    return f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" fill="{col}" font-family="Fredoka, Arial">{E(t)}</text>'
def sfr(x,y,n,d,size=28,col=NAVY):
    """stacked fraction in SVG, the bar sits at y"""
    return (T(x,y-5,str(n),size,col)+f'<line x1="{x-size*0.5:.1f}" y1="{y+1:.1f}" x2="{x+size*0.5:.1f}" y2="{y+1:.1f}" stroke="{col}" stroke-width="3"/>'+T(x,y+size+2,str(d),size,col))
def bar(x,y,w,h,n,shade=None,stroke=3,label=True,lsize=24):
    """a bar cut into n EQUAL parts; shade = list of fills per part (None = white)"""
    s=''; pw=w/n
    for i in range(n):
        f=(shade[i] if shade and i<len(shade) and shade[i] else WHITE)
        s+=f'<rect x="{x+i*pw:.2f}" y="{y}" width="{pw:.2f}" height="{h}" fill="{f}" stroke="{NAVY}" stroke-width="{stroke}"/>'
        if label and n>1: s+=sfr(x+i*pw+pw/2,y+h/2-2,1,n,lsize)
    return s
def wall_svg(dens,w,rowh,shade=None,lsize=26,dash=None,label='Fraction wall'):
    """rows of the fraction wall; shade = {den: (count, colour)}; dash = x fraction for a dashed line"""
    b=''
    for r,dn in enumerate(dens):
        y=4+r*rowh
        if dn==1:
            b+=f'<rect x="4" y="{y}" width="{w-8}" height="{rowh}" fill="{YEL}" stroke="{NAVY}" stroke-width="3"/>'+T(w/2,y+rowh/2+11,'1 whole',30)
            continue
        cnt,col=(shade or {}).get(dn,(0,None))
        b+=bar(4,y,w-8,rowh,dn,[col]*cnt+[SKY if r%2 else WHITE]*dn,3,True,lsize)
    if dash is not None:
        X=4+(w-8)*dash; b+=f'<line x1="{X:.1f}" y1="0" x2="{X:.1f}" y2="{8+len(dens)*rowh}" stroke="{RED}" stroke-width="5" stroke-dasharray="14 9"/>'
    return svgwrap(label,w,len(dens)*rowh+8,b)

# ---------- 1. title ----------
put('p3l6-title',title_slide('p3l6-title','LESSON 6  •  WEEK 3','Fraction Walls','Fractions',
 'Build a fraction wall, find equal fractions, compare fractions by making the parts the same size, and add related fractions.',
 'Objective: Use a fraction wall to find equivalent fractions, compare and order fractions by making the parts the same size, and add and subtract like and related fractions within one whole. '
 'Heuristics taught today: DRAW A MODEL (fraction wall or bar) and MAKE THE PARTS THE SAME SIZE (change one fraction to an equal fraction before comparing or adding). '
 'Materials: 7 paper strips per child, all the same length (24 cm works well), ruler, coloured pencils, scissors, mini whiteboards. '
 'Online: send the printed fraction strip page instead of asking children to measure and cut strips; marks every 12, 8, 6, 4, 3 and 2 cm give halves, thirds, quarters, sixths, eighths and twelfths. '
 'Time plan: warm-up 0 to 10, explore 10 to 25, teaching 25 to 35 (click to reveal each step and answer), brain break 35 to 40, worksheet 40 to 70 with short teaching before each page and a check-together slide after it, talk time 70 to 80, exit ticket 80 to 90. Stretch and Challenge slides are for early finishers. If the class is behind, children finish the last question of each page at home; the check slides cover it.'))

# ---------- 2. warm-up: Fraction Flash ----------
def circle8(sh):
    b=''; cx,cy,R=120,120,100
    for i in range(8):
        a0=math.radians(i*45-90); a1=math.radians((i+1)*45-90)
        b+=f'<path d="M{cx},{cy} L{cx+R*math.cos(a0):.2f},{cy+R*math.sin(a0):.2f} A{R},{R} 0 0 1 {cx+R*math.cos(a1):.2f},{cy+R*math.sin(a1):.2f} Z" fill="{YEL if i<sh else WHITE}" stroke="{NAVY}" stroke-width="4"/>'
    return svgwrap('Circle cut into 8 equal parts, 3 shaded',240,240,b)
def grid23():
    b=''; on={(0,0),(0,1),(1,0),(1,1)}
    for r in range(2):
        for c in range(3): b+=f'<rect x="{10+c*73.33:.2f}" y="{30+r*90}" width="73.33" height="90" fill="{TEAL if (c,r) in on else WHITE}" stroke="{NAVY}" stroke-width="4"/>'
    return svgwrap('Rectangle cut into 6 equal parts, 4 shaded',240,240,b)
def hexa(sh):
    b=''; cx,cy,R=120,120,105
    pts=[(cx+R*math.cos(math.radians(60*i)),cy+R*math.sin(math.radians(60*i))) for i in range(6)]
    for i in range(6):
        a,c=pts[i],pts[(i+1)%6]
        b+=f'<polygon points="{cx},{cy} {a[0]:.2f},{a[1]:.2f} {c[0]:.2f},{c[1]:.2f}" fill="{YEL if i<sh else WHITE}" stroke="{NAVY}" stroke-width="4"/>'
    return svgwrap('Regular hexagon cut into 6 equal triangles, 5 shaded',240,240,b)
def bar10():
    return svgwrap('Bar cut into 10 equal parts, 7 shaded',240,240,bar(5,90,230,70,10,[RED]*7,3,False))
shapes=[(circle8(3),F(3,8)),(grid23(),F(4,6)+' = '+F(2,3)),(hexa(5),F(5,6)),(bar10(),F(7,10))]
body=h2('Warm-up: Fraction Flash')+p('Each shape is cut into equal parts. What fraction is shaded? Write it on your whiteboard.',34,600,MUTED)
CW=392
for i,(sv,a) in enumerate(shapes):
    L=128+i*(CW+32)
    body+=pin(L,320,CW,f'<div style="display:flex;justify-content:center">{sv}</div>',None,WHITE,24,'20px 20px',f'box-sizing:border-box;border:4px solid {NAVY};box-shadow:8px 8px 0 {NAVY}')
    body+=pin(L,640,CW,f'<p style="font-size:44px;font-weight:800;text-align:center">{a}</p>','pop',YEL,20,'12px 18px','box-sizing:border-box')
put('p3l6-warm1',sec('p3l6-warm1','0–5 MIN',body,
 'Minutes 0 to 5. Fraction Flash. Point to one shape at a time. Children count the equal parts (bottom number) and the shaded parts (top number), write the fraction, hold it up, then click to reveal (clicks go left to right). '
 'Answers: circle 3/8; rectangle 4/6, which is the same as 2/3 (the 4 shaded parts fill two of the three columns); hexagon 5/6; bar 7/10. '
 'Ask every time: "How do you know the parts are equal?" (same size triangles, same size squares). Ask: "What fraction is NOT shaded?" (5/8, 2/6, 1/6, 3/10).'))

# ---------- 3. quick questions ----------
qs=[('1.','How many quarters make one whole?','4'),('2.','Which is bigger: '+F(1,3)+' or '+F(1,5)+'?',F(1,3)),('3.',F(1,2)+' = '+F(BOX,10),'5')]
body=h2('Quick questions')+''.join(qr(128,230+i*130,1250,a,b,34) for i,(a,b,c) in enumerate(qs))+''.join(aw(1420,230+i*130,372,c,'pop',34) for i,(a,b,c) in enumerate(qs))
put('p3l6-warm2',sec('p3l6-warm2','5–10 MIN',body,
 'Minutes 5 to 10. Whiteboards, then click. Ask for a reason each time. Answers: 1) 4.  2) 1/3: the whole is cut into fewer pieces, so each piece is bigger.  3) 5.  4) 6/9: we add the ninths; the bottom number stays 9.  Questions 4 and 5 are take-home (2/9 + 4/9 = 6/9; 1 − 2/5 = 3/5): ask only 1 to 3. '
 'Watch for children who write 6/18 for question 4: we come back to this mistake later.'))

# ---------- 4. explore: what to do ----------
mini=wall_svg([1,2,4,8],1400,52,None,24,0.5,'A fraction wall with one whole, halves, quarters and eighths and a dashed line at one half').replace('style="width:1400px;height:216px;display:block"','style="width:100%;height:auto;display:block"')
steps_html='<ol style="font-size:32px;font-weight:600;padding-left:48px;display:flex;flex-direction:column;gap:6px">'+''.join(f'<li>{E(s)}</li>' for s in ['Take the 7 strips you cut out BEFORE the lesson (the printed strip page).','Keep one whole. Mark halves, quarters and eighths on three strips. The thirds, sixths and twelfths are already printed.','Label every part and stack the strips into a wall.','Ask: which pieces line up exactly?'])+'</ol>'
body=h2('Explore: what to do')+card(chip('EXPLORE')+steps_html,extra='padding:22px 40px;gap:8px')+card(mini,extra='padding:16px 24px')
put('p3l6-explore1',sec('p3l6-explore1','10–15 MIN',body,
 'Minutes 10 to 15. Predict first: "Which is bigger, one sixth or one eighth of the same strip?" Parents cut the printed strips out BEFORE the lesson (the one-week-before message says so), so nobody spends time finding or cutting strips. Pairs only MARK halves, quarters and eighths (fold in half again and again), then compare them with the printed thirds, sixths and twelfths (about 6.5 minutes of pair work). '
 'Children label every part (1/2, 1/4 …) and stack the strips. Stress: the parts in a row must be equal, or they are not halves, thirds … '
 'Hints: "Which pieces line up with the dashed line at one half?" Ready for more: "Find three different pieces that together cover exactly one half." (with three DIFFERENT pieces the only way is 1/4 + 1/6 + 1/12; 1/4 + 1/8 + 1/8 repeats a piece). '
 'Online: children hold their wall up to the camera.'))

# ---------- 5. explore: talk ----------
body=h2('Explore: talk about it')+items([('1.','How many '+F(1,8)+' pieces fit exactly on '+F(1,2)+'?'),('2.','Which is bigger, '+F(1,6)+' or '+F(1,8)+'? Why?'),('3.','Can eighths cover '+F(1,3)+' exactly?')],40)
put('p3l6-explore2',sec('p3l6-explore2','15–25 MIN',body,
 'Minutes 15 to 25. Gather the pairs. Answers: 1) 4, so 1/2 = 4/8. 2) 1/6: the same whole is cut into fewer parts, so each part is bigger. 3) No. 2 eighths are too small and 3 eighths are too big. Sixths and twelfths can (2/6 and 4/12). '
 'Ask: "What other pieces line up exactly?" Collect a list: 1/2 = 2/4 = 3/6 = 4/8 = 6/12, 1/3 = 2/6 = 4/12, 1/4 = 2/8 = 3/12, 2/3 = 4/6 = 8/12, 3/4 = 6/8 = 9/12.'))

# ---------- 6. teach: the fraction wall ----------
wall=wall_svg([1,2,3,4,6,8,12],1664,66,None,24,None,'Fraction wall with one whole, halves, thirds, quarters, sixths, eighths and twelfths, every row cut into equal parts')
body=h2('The fraction wall')+pin(128,240,1664,wall)+pin(128,790,1664,p('Every row is ONE WHOLE cut into EQUAL parts. More parts means smaller parts.',36,800),'fade',SOFT,20,'18px 30px')
put('p3l6-teach1',sec('p3l6-teach1','25–26 MIN',body,
 'Teach. This is the wall the children built. Run a finger along each row: "Every row is the same whole. Halves: 2 equal parts. Twelfths: 12 equal parts." Ask: "Which row has the biggest pieces? The smallest?" '
 'Click: the rule. Say: "The bottom number tells how many equal parts the whole is cut into. More parts, smaller parts. So 1/12 is the smallest piece on the wall, even though 12 is the biggest number."'))

# ---------- 7. worked example: equal fractions ----------
w3=wall_svg([3,6,12],1664,64,{3:(1,YEL),6:(2,YEL),12:(4,YEL)},24,1/3,'One third, two sixths and four twelfths shaded; they line up at the same dashed line')
body=h2('Equal fractions: same amount, different pieces')+chip('HEURISTIC: DRAW A MODEL',YEL,NAVY)+pin(128,320,1664,w3)
body+=step(1,'On the wall '+F(1,3)+' lines up with 2 sixths and with 4 twelfths:  '+F(1,3)+' = '+F(2,6)+' = '+F(4,12),top=540,size=34)
body+=step(2,'Pattern: top and bottom are multiplied by the SAME number:  × 2 gives '+F(2,6)+',  × 4 gives '+F(4,12),top=670,size=34)
body+=step(3,'So '+F(2,5)+' = '+F(4,10)+' too. No wall needed!',top=800,size=30)
put('p3l6-we1',sec('p3l6-we1','26–28 MIN',body,
 'Heuristic: DRAW A MODEL. Click through the steps. Think-aloud: "1/3 on the wall lines up with 2 sixths and with 4 twelfths. Same amount, different pieces. From 1/3 to 2/6 the top and the bottom were both doubled: each third is cut into 2, so there are twice as many parts and twice as many shaded. From 1/3 to 4/12, both times 4. So 2/5 = 4/10 without a wall." '
 'Ask: "Why must we multiply the top AND the bottom?" (cutting every piece into 2 doubles the shaded pieces and all the pieces).'))

# ---------- 8. try: equal fractions ----------
put('p3l6-try1',try_raw('p3l6-try1','28–29 MIN','Your turn: equal fractions','What goes in the box? Use the wall or multiply.',
 [('a',F(1,3)+' = '+F(BOX,9),'3'),('b',F(3,5)+' = '+F(6,BOX),'10'),('c',F(5,6)+' = '+F(BOX,12),'10')],
 'Whiteboards up together, then click. a) 3 × 3 = 9, so 1 × 3 = 3: 3/9 (ninths are not on our wall: multiplying works anyway). b) 3 × 2 = 6, so 5 × 2 = 10. c) 6 × 2 = 12, so 5 × 2 = 10. Ask a child to explain c with the wall.',38,165))

# ---------- 9. worked example: compare ----------
bars2=(T(150,46,'5/6',34,TEAL)+bar(300,10,1340,56,12,[TEAL]*10,3,False)+T(150,126,'3/4',34,TEAL)+bar(300,90,1340,56,12,[YEL]*9,3,False))
bars2=svgwrap('Two equal bars in twelfths: 10 twelfths shaded and 9 twelfths shaded',1664,156,bars2)
body=h2('Compare: make the parts the same size')+chip('HEURISTIC: MAKE THE PARTS THE SAME SIZE',YEL,NAVY)
body+=step(1,'Same bottom number: count the parts.  '+F(3,7)+' &lt; '+F(5,7),top=320,size=34)
body+=step(2,'Same top number: bigger parts win.  '+F(2,5)+' &gt; '+F(2,9)+'  (fifths are bigger than ninths)',top=450,size=34)
body+=step(3,'Different parts: change them.  '+F(5,6)+' = '+F(10,12)+',  '+F(3,4)+' = '+F(9,12)+',  so  '+F(5,6)+' &gt; '+F(3,4),top=580,size=34)
body+=pin(128,730,1664,bars2,'rise')
put('p3l6-we2',sec('p3l6-we2','29–31 MIN',body,
 'Heuristic: MAKE THE PARTS THE SAME SIZE. Click through. Think-aloud: "3/7 and 5/7: the parts are the same size, sevenths, so I just count: 5 is more than 3. 2/5 and 2/9: the same number of parts, but fifths are bigger pieces, so 2/5 wins. 5/6 or 3/4? The parts are different sizes, so I change both to twelfths: 10/12 and 9/12. Now the parts match: 5/6 is bigger." '
 'The last click shows both as twelfths on equal bars. Ask: "How did I know to use twelfths?" (12 is in both the 6 and the 4 times tables; the wall has twelfths).'))

# ---------- 10. try: compare ----------
OV='<span style="display:inline-block;width:0.9em;height:0.9em;border:4px solid currentColor;border-radius:50%;margin:0 10px;vertical-align:middle"></span>'
put('p3l6-try2',try_raw('p3l6-try2','31–33 MIN','Your turn: &gt;, &lt; or =','Make the parts the same size if you need to.',
 [('a',F(1,6)+OV+F(1,9),'&gt;'),('b',F(2,5)+OV+F(4,10),'='),('c',F(7,10)+OV+F(3,5),'&gt;')],
 'Whiteboards. a) Same top number: sixths are bigger than ninths, so 1/6 > 1/9. b) 2/5 = 4/10, so they are equal. c) 3/5 = 6/10, and 7/10 > 6/10. Ask: "Which rule did you use for each one?"',40,165).replace('Your turn: &amp;gt;, &amp;lt; or =','Your turn: &gt;, &lt; or ='))

# ---------- 11. key idea ----------
body=h2('Key idea: make the parts the same size')+card(p('To compare or add fractions, the parts must be the same size. Use the wall, or change one fraction to an equal fraction with the same bottom number.',42,700))+card(p('When we add, we add the top numbers. The bottom number (the size of the parts) stays the same.',38,600,MUTED))
put('p3l6-key',sec('p3l6-key','33–35 MIN',body,
 'Say the key idea together. Common mistakes to watch for during the worksheet: (1) Adding the bottom numbers as well as the top numbers (1/3 + 1/3 = 2/6, or 1/4 + 1/8 = 2/12). '
 '(2) Thinking 1/8 is bigger than 1/6 because 8 is bigger than 6. (3) Comparing or adding fractions with different-sized parts without changing one first (1/4 + 3/8 = 4/8).'))

# ---------- 12. break ----------
put('p3l6-break',break_slide('p3l6-break','35–40 MIN','Fraction turns. “A quarter turn!” “A half turn!” “Three quarters of a turn!” Turn on the spot and freeze.','Which calls make the same turn? Try “two quarters”. Then a drink of water and back to our seats.','Five minutes. Two quarters of a turn is the same as a half turn; four quarters is a whole turn. Online: children stay in view of the camera and turn in place.'))

# ---------- 13-14. worksheet page 1 ----------
put('p3l6-ws1',ws_preview('p3l6-ws1','40–52 MIN','Worksheet page 1: with your partner',
 [('Q1','The fraction wall: fill in the equal fractions (a), (b) and (d). (c) is a ★ take-home question.'),('Q2','Compare with >, < or =, then put four fractions in order.')],
 'Stuck? Find both fractions on the wall. Which one reaches further?',
 'Minutes 40 to 52. Walk around. Ask "Are the parts the same size? Which fraction did you change?" before giving any help. In Q1 do (a), (b) and (d) in class: Q1(c) is a take-home question (starred in the workbook). For Q2(g) suggest changing every fraction to twelfths.'))
put('p3l6-ws1ans',check_raw('p3l6-ws1ans','52–54 MIN','Page 1: check together',
 [('Q1','(a) 2, 3, 4, 6   (b) 4, 8   (c) 6, 9   (d) the bottom is double the top'),('Q2','(a) &gt;   (b) &lt;   (c) =   (d) &gt;   (e) &lt;   (f) &lt;'),('Q2g',F(1,3)+',  '+F(5,12)+',  '+F(1,2)+',  '+F(3,4))],
 'Click after a pair explains. Q1(d): 1/2 = 2/4 = 3/6 = 4/8 = 6/12; the bottom number is always double the top (top and bottom multiplied by the same number). Q2: (d) 3/4 = 6/8; (e) same top number, sevenths are bigger than ninths; (f) 2/3 = 8/12 and 3/4 = 9/12. (g) In twelfths: 4/12, 5/12, 6/12, 9/12.',165,34))

# ---------- 15. teach before page 2: adding ----------
pw6=1656/6
bsv=svgwrap('A bottle shown as a bar cut into 6 equal parts: 2 parts teal, 1 part yellow',1664,170,bar(4,86,1656,80,6,[TEAL,TEAL,YEL],4,False)+f'<path d="M8 80 L8 70 L{4+2*pw6-4:.1f} 70 L{4+2*pw6-4:.1f} 80" fill="none" stroke="{TEAL}" stroke-width="4"/>'+sfr(4+pw6,30,1,3,26,TEAL)+sfr(4+pw6*2.5,30,1,6,26,NAVY))
body=h2('Add fractions: draw a bar')+card(rp('Ali drinks '+F(1,3)+' of a bottle of water, then '+F(1,6)+' of the bottle more. How much has he drunk?',36,700))
body+=pin(128,390,1664,bsv,'rise')
body+=step(1,'Make the parts the same size:  '+F(1,3)+' = '+F(2,6),top=575,size=32)
body+=step(2,F(2,6)+' + '+F(1,6)+' = '+F(3,6)+' = '+F(1,2)+'.  Add the top numbers only: the parts are still sixths.',top=685,size=32)
body+=step(3,'Left in the bottle:  '+F(6,6)+' − '+F(3,6)+' = '+F(3,6)+' = '+F(1,2),top=795,size=32)
put('p3l6-teachadd',sec('p3l6-teachadd','54–56 MIN',body,
 'Teach before worksheet page 2 (Q4 and Q5). Heuristic: DRAW A BAR. Click 1: the bar cut into sixths; the two teal parts are the third (the 1/3 label sits across both), the yellow part is the extra sixth. '
 'Think-aloud: "1/3 and 1/6 are different-sized parts, so I change 1/3 into sixths: 2/6. Now 2 sixths and 1 sixth make 3 sixths. The parts are still sixths, so the bottom number stays 6." '
 'Show the mistake: "Ben says 1/3 + 1/6 = 2/9. Is a ninth bigger or smaller than a sixth? He drank MORE than 1/3, but 2/9 is less than 1/3. So 2/9 cannot be right."'))

# ---------- 17. teach: partners that make one whole ----------

# ---------- 18. teach: all the fractions between ----------

SP='&nbsp;&nbsp;&nbsp;'
# ---------- 19-20. worksheet page 2 ----------
put('p3l6-ws2',ws_preview('p3l6-ws2','59–66 MIN','Worksheet page 2: on your own',
 [('Q3','Which shapes show one quarter? Count the equal parts.'),('Q4','Add and subtract: make the parts the same size first.'),('Q5','Ravi paints a fence: draw a bar.'),('Q6','★ Take-home: partner cards that make one whole.'),('TH','Think harder: ALL the twelfths between one half and three quarters.')],
 'Ready for more? Stretch and Challenge come next.',
 'Children work alone. Note who needs a short catch-up next lesson. Watch for adding the bottom numbers in Q4 and Q5. Page 2 is Q4 and Q5 only (Q6 is take-home).'))
put('p3l6-ws2ans',check_raw('p3l6-ws2ans','66–70 MIN','Page 2: check together',
 [('Q3','(a) A, B, D   (b) C: '+F(2,6)+' = '+F(1,3)+',  E: '+F(3,8)),
  ('Q4',(SP).join(['(a) '+F(5,7),'(b) '+F(5,8),'(c) '+F(9,12)+' = '+F(3,4),'(d) '+F(3,6)+' = '+F(1,2),'(e) '+F(7,10),'(f) '+F(8,10)+' = '+F(4,5)])),
  ('Q5','(a) '+F(5,6)+'   (b) '+F(1,6)+'   (c) '+F(3,6)+' = '+F(1,2)+' more'),
  ('Q6',(SP).join([F(a,b)+' + '+F(c,d) for a,b,c,d in [(1,4,6,8),(2,3,4,12),(3,8,5,8),(5,12,7,12),(1,6,5,6)]])),
  ('TH 1',F(7,12)+' and '+F(8,12)+'.   '+F(8,12)+' = '+F(2,3))],
 'Click after a child explains. Q3: B is 2/8 and D is 3/12, both equal to 1/4. Q4: (b) 2/8 + 3/8; (c) 4/12 + 5/12; (d) 5/6 − 2/6; (e) 10/10 − 3/10; (f) 5/10 + 3/10. Q5: 2/3 = 4/6; 1/6 + 4/6 = 5/6; 6/6 − 5/6 = 1/6; 4/6 − 1/6 = 3/6. '
 'Q6: 1/4 needs 3/4 = 6/8; 2/3 needs 1/3 = 4/12; 5/12 needs 7/12; 3/8 needs 5/8; 1/6 needs 5/6. Think harder 1: 1/2 = 6/12 and 3/4 = 9/12, so 7/12 and 8/12.',128,30))

# ---------- 21. stretch (new items) ----------
body=h2('Stretch')+items([('1.',F(1,3)+' + '+BOX+' = '+F(5,6)+'.  What goes in the box?'),('2.','Put in order, smallest first:  '+F(1,2)+',  '+F(2,5)+',  '+F(7,10)),('3.','Find all the fractions with bottom number 10 between '+F(1,5)+' and '+F(1,2)+'.')],36)
put('p3l6-stretch',sec('p3l6-stretch','For early finishers',body,
 'SUPPORT FOR THINK HARDER 1 (this replaces the old teach-between slide; show it only to a pair who chooses Think harder): the number line is cut into 8 equal steps from 0 to 1. Change the ends to eighths: 1/4 = 2/8 and 3/4 = 6/8. In between: 3/8, 4/8, 5/8, so 3 fractions; list them in order and do not count the end fractions. Which of the three is the same as 1/2? (4/8). Answers: 1) 1/2, or 3/6 (1/3 = 2/6, and 5/6 − 2/6 = 3/6). 2) 2/5, 1/2, 7/10 (4/10, 5/10, 7/10). 3) 3/10 and 4/10 (1/5 = 2/10 and 1/2 = 5/10; the ends do not count).'))

# ---------- 22. challenge ----------
body=h2('Challenge')+items([('1.','Fill one whole bar using exactly 5 pieces. You may use '+F(1,2)+', '+F(1,4)+' and '+F(1,8)+' pieces, as many of each as you like. Find all the ways.'),('2.','Find a fraction that is bigger than '+F(2,3)+' but smaller than '+F(3,4)+'. Hint: cut every part into smaller equal parts. Can you find another one?')],34)
put('p3l6-challenge',sec('p3l6-challenge','Challenge',body,
 'Pairs try first, then use the "see it" slide if stuck, then the walk-through. Answers: 1) 2 ways: 1/2 + 1/8 + 1/8 + 1/8 + 1/8, and 1/4 + 1/4 + 1/4 + 1/8 + 1/8. 2) 17/24 (2/3 = 16/24 and 3/4 = 18/24). Another: 25/36 (24/36 and 27/36). Many answers are possible.'))

# ---------- 23. challenge: see it ----------
c1=(f'<rect x="10" y="40" width="720" height="70" fill="{WHITE}" stroke="{NAVY}" stroke-width="4"/>'+T(370,86,'1 whole: fill it with exactly 5 pieces',26)
    +T(10,170,'Pieces you can use:',26,TEAL,'start')
    +bar(10,195,360,64,1,[YEL],3,False)+sfr(190,226,1,2,26)
    +bar(10,280,180,64,1,[SKY],3,False)+sfr(100,311,1,4,26)
    +bar(10,365,90,64,1,[TEAL],3,False)+sfr(55,396,1,8,24,WHITE)
    +T(400,300,'Same length as the whole:',24,MUTED,'start')+T(400,334,'2 halves, 4 quarters',24,MUTED,'start')+T(400,368,'or 8 eighths.',24,MUTED,'start'))
sv1=svgwrap('An empty whole bar and the half, quarter and eighth pieces drawn to the same scale',740,440,c1,'width:100%;height:auto')
c2=(T(10,40,'Two thirds',28,TEAL,'start')+bar(10,56,720,80,3,[YEL,YEL],4,True,26)
    +T(10,200,'Three quarters',28,TEAL,'start')+bar(10,216,720,80,4,[SKY]*3,3,False)
    +T(370,370,'Is there a fraction in between? Cut the parts smaller.',24,MUTED))
sv2=svgwrap('Two equal bars: one cut into thirds with 2 shaded, one cut into quarters with 3 shaded',740,400,c2,'width:100%;height:auto')
body=h2('Challenge: see it',60)+'<div style="display:flex;gap:32px;align-items:flex-start">'+card('<p style="font-size:28px;font-weight:700;color:#1F7A6F">Q1: Five pieces, one whole</p>'+sv1,extra='flex:1;min-width:0;padding:20px 24px')+card('<p style="font-size:28px;font-weight:700;color:#1F7A6F">Q2: Between two fractions</p>'+sv2,extra='flex:1;min-width:0;padding:20px 24px')+'</div>'
put('p3l6-chdiag',sec('p3l6-chdiag','Challenge',body,
 'Show after pairs have tried, or if they are stuck. The pictures show the problem, not the answer. Q1: "Start with the biggest piece. If you use a half, what must the other 4 pieces make?" Q2: "The parts are different sizes. How can you cut both bars so the parts match?"'))

# ---------- 24. challenge walk-through ----------
body=h2('Challenge: walk-through')+pin(128,250,800,p('Q1: biggest piece first',38,800,TEAL))
for i,t in enumerate(['With a '+F(1,2)+': four '+F(1,8)+' make the other '+F(1,2)+' ✓',
                      F(1,4)+' + three '+F(1,8)+' = '+F(5,8)+': too much. 1 way with a half.',
                      'No half: three '+F(1,4)+' + two '+F(1,8)+' = 1 whole ✓',
                      '2 ways altogether.']):
    body+=pin(128,330+i*140,800,rp(t,28),'rise',WHITE)
body+=pin(992,250,800,p('Q2: make the parts the same size',38,800,TEAL))
for i,t in enumerate([F(2,3)+' = '+F(8,12)+'  and  '+F(3,4)+' = '+F(9,12),'Nothing fits between '+F(8,12)+' and '+F(9,12)+'. Cut every part in 2:',F(16,24)+'  and  '+F(18,24)+'.  '+F(17,24)+' fits in between!']):
    body+=pin(992,330+i*140,800,rp(t,28),'rise',WHITE)
put('p3l6-chwalk',sec('p3l6-chwalk','Challenge',body,
 'Use after pairs have tried. Q1: work in order from the biggest piece, as in the list-in-order puzzles earlier in the program. With a half: the other half needs 4 pieces; 1/4 + 1/8 + 1/8 is only 3 pieces, and 1/4 + three eighths is too much, so only four eighths. Without a half: four quarters is only 4 pieces; three quarters + two eighths works; two quarters + eighths needs 4 eighths, which is 6 pieces. '
 'Q2: first make the parts the same size: 2/3 = 8/12 and 3/4 = 9/12. There is no twelfth between them, so cut every part in two: 16/24 and 18/24, and 17/24 is in between. Children may cut into 3 or 4 instead (24/36 and 27/36 leave 25/36 and 26/36). The answer is not unique: the ladder of cuts never ends.'))

# ---------- 25. talk ----------
body=h2('Talk time')+card(chip('TALK TIME',YEL,NAVY)+rp('Why is '+F(1,8)+' smaller than '+F(1,6)+', even though 8 is bigger than 6?',42))+card(p('Sentence starters:',34,400,MUTED)+p('“I noticed that …”   “I tested it by …”   “I know because …”',38,600))
put('p3l6-talk',sec('p3l6-talk','70–80 MIN',body,
 'Minutes 70 to 80. Pairs talk for 2 minutes, then share. Second question if time: "Why is 1/3 + 1/3 not 2/6?" '
 'Answer: The same whole is cut into more pieces, so each eighth is smaller than each sixth. 1/3 + 1/3 is two thirds; the pieces are still thirds, so we add only the top numbers (2/6 is just 1/3). Praise the reasons, not only the answers.'))

# ---------- 26. exit ----------
body=h2('Exit ticket')+card(chip('EXIT TICKET')+rp('Ali says  '+F(1,4)+' + '+F(1,8)+' = '+F(2,12)+'.  Is he right? Write the correct answer and show how you know.',44))+card(p('Write your answer on a slip of paper. Show it to your tutor. Then collect your stamp in your inquiry journal.',34,400))
put('p3l6-exit',sec('p3l6-exit','80–90 MIN',body,
 'Minutes 80 to 90. Answer: No. 1/4 = 2/8, so 1/4 + 1/8 = 2/8 + 1/8 = 3/8. We add the parts, not the bottom numbers. Extension: How many different ways can you fill one whole bar using 1/2, 1/4 and 1/8 pieces, as many of each as you like? (9 ways.)'))

# ---------- write ----------
import p3_gifted; ORDER[:]=p3_gifted.add(S,ORDER,6)  # close-the-gaps: warm-up check + look-back slides
for f in os.listdir(os.path.join(D,'slides')):
    if f.endswith('.html') and f[:-5] not in S: os.remove(os.path.join(D,'slides',f))
for i,h in S.items(): open(os.path.join(D,'slides',i+'.html'),'w').write(h)
deck={'v':4,'createdOnFiles':{'v':1,'at':'2026-10-21T12:00:00Z'},'lists':'css','title':'Math Inquirers P3: Lesson 6 – Fraction Walls','order':ORDER,'cover':'p3l6-title',
 'sections':{'s1':{'description':'Warm-up and explore','start':'p3l6-title'},'s2':{'description':'Teach: the fraction wall, equal fractions and comparing','start':'p3l6-teach1'},'s3':{'description':'Worksheet with teaching before each page','start':'p3l6-break'},'s4':{'description':'Think harder, go further, talk and exit','start':'p3l6-stretch'}},
 'faces':{'fredoka':{'family':'Fredoka','href':'https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&display=swap'},'nunito-sans':{'family':'Nunito Sans','href':'https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@400;600;700&display=swap'}},
 'designSystems':[]}
json.dump(deck,open(os.path.join(D,'deck.json'),'w'),indent=1,ensure_ascii=False)
print(len(ORDER),'slides')
