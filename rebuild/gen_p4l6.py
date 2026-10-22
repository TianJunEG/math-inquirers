"""Math Inquirers P4, Lesson 6: Angle Turns. Writes split/p4l6/project (deck.json + slides/*.html).
Every angle in the drawings is drawn to size (coordinates computed with cos and sin)."""
import json,os,sys,datetime,math
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,H)
import slidekit
from slidekit import *
slidekit.FOOT='Math Inquirers P4 Holiday Program  •  Notice it. Test it. Explain why.'
P='p4l6'
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
    notes=notes.replace('Four minutes.',__import__('p4_budget').break_lead(6),1)
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
def svgwrap(w,h,label,inner,css=None):
    st=css or f'width:{w}px;height:{h}px;flex:none'
    return f'<svg aria-label="{E(label)}" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="{st}">{inner}</svg>'
def txt(x,y,s,size=40,fill=NAVY,anchor='middle',weight=700,font='Fredoka, Arial'):
    return f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" fill="{fill}" font-family="{font}">{E(str(s))}</text>'

# ---------- geometry (maths angles: 0° points right, anticlockwise is positive; SVG y goes down) ----------
def pt(cx,cy,r,d): return (cx+r*math.cos(math.radians(d)), cy-r*math.sin(math.radians(d)))
def ln(a,b,w=6,c=NAVY): return f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" stroke="{c}" stroke-width="{w}" stroke-linecap="round"/>'
def arc(cx,cy,r,d0,d1,c=TEAL,w=5):
    a=pt(cx,cy,r,d0); b=pt(cx,cy,r,d1)
    return f'<path d="M{a[0]:.1f} {a[1]:.1f} A{r} {r} 0 {1 if d1-d0>180 else 0} 0 {b[0]:.1f} {b[1]:.1f}" fill="none" stroke="{c}" stroke-width="{w}"/>'
def dot(c,r=8,f=NAVY): return f'<circle cx="{c[0]:.1f}" cy="{c[1]:.1f}" r="{r}" fill="{f}"/>'
def angle_in(px,py,pw,ph,d0,d1,r,label='',ar=50):
    ps=[(0,0),pt(0,0,r,d0),pt(0,0,r,d1)]; xs=[q[0] for q in ps]; ys=[q[1] for q in ps]
    cx=px+pw/2-(min(xs)+max(xs))/2; cy=py+ph/2-(min(ys)+max(ys))/2
    g=ln((cx,cy),pt(cx,cy,r,d0))+ln((cx,cy),pt(cx,cy,r,d1))+arc(cx,cy,ar,d0,d1)+dot((cx,cy))
    if label: q=pt(cx,cy,ar+40,(d0+d1)/2); g+=txt(q[0],q[1]+12,label,36,TEAL)
    return g
COMP={'E':0,'NE':45,'N':90,'NW':135,'W':180,'SW':225,'S':270,'SE':315}
def compass(cx,cy,R=200,hi=(),size=44):
    g=f'<circle cx="{cx}" cy="{cy}" r="{R+10}" fill="{WHITE}" stroke="#C9D4EC" stroke-width="3"/>'
    for n,d in COMP.items():
        main=len(n)==1
        g+=ln((cx,cy),pt(cx,cy,R*(0.78 if main else 0.6),d),7 if main else 5,NAVY)
        q=pt(cx,cy,R*(0.78 if main else 0.6)+(44 if main else 46),d)
        g+=(f'<circle cx="{q[0]:.1f}" cy="{q[1]:.1f}" r="38" fill="{YEL}"/>' if n in hi else '')+txt(q[0],q[1]+size*0.36,n,size if main else size-8,NAVY if main else TEAL)
    return g+f'<circle cx="{cx}" cy="{cy}" r="14" fill="{YEL}" stroke="{NAVY}" stroke-width="4"/>'
def turn_arrow(cx,cy,r,d0,d1,c=RED,w=7):
    """arc arrow from maths angle d0 to d1 (d1<d0 means clockwise)"""
    a=pt(cx,cy,r,d0); b=pt(cx,cy,r,d1); sweep=1 if d1<d0 else 0; big=1 if abs(d1-d0)>180 else 0
    g=f'<path d="M{a[0]:.1f} {a[1]:.1f} A{r} {r} 0 {big} {sweep} {b[0]:.1f} {b[1]:.1f}" fill="none" stroke="{c}" stroke-width="{w}"/>'
    # arrow head along the tangent at the end
    t=-1 if d1<d0 else 1; hd=d1+t*0; tx=-math.sin(math.radians(hd))*t; ty=-math.cos(math.radians(hd))*t
    nx,ny=-ty,tx
    p1=(b[0]-tx*26+nx*14,b[1]-ty*26+ny*14); p2=(b[0]-tx*26-nx*14,b[1]-ty*26-ny*14)
    return g+f'<polygon points="{b[0]+tx*6:.1f},{b[1]+ty*6:.1f} {p1[0]:.1f},{p1[1]:.1f} {p2[0]:.1f},{p2[1]:.1f}" fill="{c}"/>'
def clock(cx,cy,R,h=None,m=None,nums=True,mark=None):
    g=f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="{WHITE}" stroke="{NAVY}" stroke-width="7"/>'
    for i in range(60):
        d=90-i*6; big=i%5==0
        g+=ln(pt(cx,cy,R-(26 if big else 12),d),pt(cx,cy,R-6,d),5 if big else 2)
    if nums:
        for k in ((3,6,9,12) if nums=='main' else range(1,13)):
            q=pt(cx,cy,R*0.72,90-k*30); g+=txt(q[0],q[1]+R*0.07,k,max(26,int(R*0.19)))
    if h is not None:
        hd=90-((h%12)*30+m*0.5); md=90-m*6
        g+=ln((cx,cy),pt(cx,cy,R*0.5,hd),12,NAVY)+ln((cx,cy),pt(cx,cy,R*0.8,md),8,TEAL)
    return g+dot((cx,cy),10)
def rsq(c,s,d0,col=TEAL):
    a=pt(c[0],c[1],s,d0); b=pt(c[0],c[1],s*1.414,d0+45); e=pt(c[0],c[1],s,d0+90)
    return f'<path d="M{a[0]:.1f} {a[1]:.1f} L{b[0]:.1f} {b[1]:.1f} L{e[0]:.1f} {e[1]:.1f}" fill="none" stroke="{col}" stroke-width="4"/>'

# ---------- 1. title ----------
put('title',title_slide(f'{P}-title','LESSON 6  •  WEEK 3','Angle Turns','Angles',
 'Estimate and measure angles, find every angle in a fan, work out clock angles, turn on the 8-point compass and find missing angles in squares and rectangles.',
 'Objective: Estimate and measure angles with a protractor, find every angle in a fan of rays, work out angles between clock hands (30° for each space) and turns of the minute hand (6° a minute), turn on the 8-point compass (45° steps) and work backwards from a turn, and find unknown angles in squares and rectangles. '
 'Thinking strategies today: ESTIMATE FIRST (compare with 90° and 180°), COUNT THE TURN (12 clock spaces, 8 compass steps), WORK IN ORDER (every angle in a fan), WORK BACKWARDS (undo a turn). '
 'Materials: A clear 180° protractor and a 30 cm ruler for each child (not printed in the kit: families bring one from home; keep two or three spares), a paper clock with a split pin (or a real clock), a square of paper for checking right angles, mini whiteboards, a compass card on the floor or wall. '
 'Online: children use their own protractor and a paper clock at home; the screen is North for the turning games, and children stand and turn on camera. '
 'Time plan: (written by rebuild/p4_fix.py from rebuild/p4_budget.py).')

# ---------- 2. warm-up game ----------
g=compass(260,260,190,hi=('N',))
body=h2('Warm-up: Robot turns')+pin(128,230,540,svgwrap(520,520,'An 8-point compass with N at the top',g),None)
calls=[('Face N. Quarter turn clockwise.','E'),('Face N. Half turn.','S'),('Face N. Three-quarter turn clockwise.','W'),('Face N. Turn 45° clockwise.','NE')]
for i,(a,b) in enumerate(calls):
    body+=qrow(720,250+i*150,800,f'{i+1}.',a,36)+answer(1580,250+i*150,212,b)
put('warm1',sec(f'{P}-warm1','6.5–8.5 MIN',body,
 'Minutes 6.5 to 8.5 (one short round, about 90 seconds: the Sneak-peek puzzles came first). Robot turns. Everyone stands and faces the front of the room: that is North (online: the screen is North). Read each call; children turn, then point and say the direction they face. Click to show it. Start every call from North. '
 'If time allows play a faster round without the slide: "From where you are now: quarter turn anticlockwise! Half turn! 45° clockwise!" Children who end up facing the wrong way watch a partner and try again. '
 'Listen for children who say "clockwise is the way the clock hands go". Online: on a mirrored self-view a turn looks reversed, so say "turn to your right" for clockwise, and tell children to ignore their own picture.'))

# ---------- 3. quick questions ----------
qs=[('1.','How many degrees in a right angle?','90°'),('2.','How many degrees in a half turn?','180°'),('3.','How many right angles make a full turn?','4')]
body=h2('Quick questions')+''.join(qrow(128,250+i*125,1250,a,b) for i,(a,b,c) in enumerate(qs))+''.join(answer(1420,250+i*125,372,c) for i,(a,b,c) in enumerate(qs))
put('warm2',sec(f'{P}-warm2','8.5–11.5 MIN',body,'Minutes 8.5 to 11.5. Three questions, about 30 seconds each: whiteboards up together, then click. No follow-up questions. 1) 90°. 2) 180°: two right angles. 3) 4, so a full turn is 4 × 90° = 360°. The other two warm-up questions (face N, quarter turn anticlockwise; a 3/4 turn or 250°) are in the Weekly Dose of Thinking Math.'))

# ---------- 4. explore: what to do ----------
g=clock(100,100,92,3,0,nums='main')+rsq((100,100),26,0,RED)
g+=f'<rect x="260" y="20" width="800" height="160" rx="20" fill="{SOFT}" stroke="{NAVY}" stroke-width="4"/>'+txt(660,82,'3 o’clock is a right angle.',38)+txt(660,140,'Which other o’clock times make a right angle?',32,TEAL)
steps=''.join(f'<li>{E(s)}</li>' for s in ['Take a paper clock with two hands.','Set it to each o’clock time: 1 o’clock, 2 o’clock … 12 o’clock.','Which times make a right angle between the hands? Check with a paper corner.','Which time makes a straight line? What is the angle at 1 o’clock?'])
body=h2('Explore: what to do')+card(chip('EXPLORE')+f'<ol style="font-size:34px;font-weight:600;padding-left:52px;display:flex;flex-direction:column;gap:6px">{steps}</ol>')
body+=card(svgwrap(1060,200,'A clock showing 3 o’clock with a right angle marked between the hands, and the question which other o’clock times make a right angle',g),extra='padding:16px 32px;align-items:center')
put('explore1',sec(f'{P}-explore1','11.5–20.5 MIN',body,'Minutes 11.5 to 20.5. Pairs use a paper clock (online: a paper clock at home or a real clock held to the camera). Ask them to predict first: which times make a right angle? Most children say 3 o’clock; fewer think of 9 o’clock. They check each time with the corner of a square of paper. Early finishers: what is the angle at 1 o’clock? At 2 o’clock? Can you work it out without a protractor?'))

# ---------- 5. explore: talk ----------
body=h2('Explore: talk about it')+numcards([('1.','Which o’clock times make a right angle?'),('2.','Which time makes a straight line? What turn is that?')],40)
put('explore2',sec(f'{P}-explore2','20.5–23 MIN',body,'Minutes 20.5 to 23. Pencils down (or when the 60-second timer closes the rooms), then gather the pairs. Two debrief questions only. Answers: 1) 3 o’clock and 9 o’clock (3 spaces apart either way). 2) 6 o’clock: a straight line, a half turn, 180°. The third question (the angle at 1 o’clock, 30°: a full turn is 360° and the clock face has 12 equal spaces, so 360 ÷ 12 = 30; check: 3 o’clock is 3 spaces, 3 × 30 = 90) is not asked; the first teaching slide after the break uses it. Many children say 12 o’clock is a straight line too: the hands are on top of each other, so the angle is 0°. Keep the 30° idea: we use it after the break.'))

# ---------- 6. teach: measure with a protractor ----------
cx,cy,R=500,440,420
g=f'<path d="M{cx-R} {cy} A{R} {R} 0 0 1 {cx+R} {cy} Z" fill="{SKY}" fill-opacity="0.75" stroke="{NAVY}" stroke-width="4"/>'
for d in range(0,181,5):
    big=d%10==0
    g+=ln(pt(cx,cy,R,d),pt(cx,cy,R-(26 if big else 14),d),3 if big else 2)
for d in range(0,181,10):
    dl=min(max(d,3.5),176.5)
    q=pt(cx,cy,R-50,dl); g+=txt(q[0],q[1]+9,180-d,25,NAVY,weight=700,font='Nunito Sans, Arial')
    q=pt(cx,cy,R-104,dl); g+=txt(q[0],q[1]+9,d,25,TEAL,weight=700,font='Nunito Sans, Arial')
g+=f'<line x1="{cx-R}" y1="{cy}" x2="{cx+R}" y2="{cy}" stroke="{NAVY}" stroke-width="3"/>'
g+=ln((cx,cy),(cx+470,cy),7)+ln((cx,cy),pt(cx,cy,440,65),7)+arc(cx,cy,70,0,65,RED,6)+dot((cx,cy),9,RED)
q=pt(cx,cy,R-104,65); g+=f'<circle cx="{q[0]:.1f}" cy="{q[1]-1:.1f}" r="26" fill="none" stroke="{RED}" stroke-width="4"/>'
body=h2('Measure with a protractor')
body+=pin(128,215,1000,svgwrap(1000,460,'A protractor on an angle of 65 degrees. One arm lies along the baseline at 0 on the inside scale; the other arm passes 65 on the inside scale and 115 on the outside scale.',g),None)
body+=pin(1170,240,622,p('Estimate first: smaller than a right angle, so less than 90°.',34,700),None,SOFT,20,'18px 26px')
body+=step(1,'Centre on the vertex.',left=1170,top=390,width=562,size=32)
body+=step(2,'Baseline along one arm.',left=1170,top=480,width=562,size=32)
body+=step(3,'Count up from the 0 on that arm.',left=1170,top=570,width=562,size=32)
body+=answer(128,700,1664,'65°.  Not 115°: our estimate says less than 90°.')
body+=pin(128,800,1664,p('Arms too short? Draw them longer with a ruler. The angle does not change.',32,700),'fade',WHITE,20,'14px 28px')
put('teach1',sec(f'{P}-teach1','23–25.5 MIN',body,'Teach. Hold up a real protractor. Ask first: "Is this angle bigger or smaller than a right angle?" (smaller: estimate about 60°). Click through the steps. Think-aloud: "The bottom arm points to 0 on the INSIDE scale, so I count up the inside scale: 10, 20 … 60, 65. The outside scale says 115 at the same place, but 115 is more than a right angle and my estimate says less. So the angle is 65°." Online: children measure the angle on their screen with a real protractor if the screen is large enough, or on the worksheet later. Point out: the length of the arms does not change the angle.'))

# ---------- 7. try: estimate ----------
g=angle_in(0,0,540,330,0,30,230,'')+angle_in(560,0,540,330,30,130,210,'')+angle_in(1120,0,544,330,10,155,200,'')
g+=txt(270,322,'A',40,TEAL)+txt(830,322,'B',40,TEAL)+txt(1392,322,'C',40,TEAL)
body=h2('Your turn: estimate first')+p('Smaller or bigger than a right angle? Estimate to the nearest 10°.',34,600,MUTED)
body+=pin(128,320,1664,svgwrap(1664,340,'Three angles drawn to size: A is 30 degrees, B is 100 degrees, C is 145 degrees',g),None,WHITE,24,'0px')
for i,a in enumerate(['A: about 30°','B: about 100°','C: about 145°']): body+=answer(128+i*568,700,500,a)

# ---------- 8. teach: compass turns ----------
g=compass(270,270,200,hi=('NW','E'))+turn_arrow(270,270,120,135,4)
body=h2('Compass turns: count 45° steps')+pin(128,215,560,svgwrap(540,540,'An 8-point compass with a red arrow turning clockwise from NW to E',g),None)
body+=pin(740,240,1052,p('Face NW. Turn 135° clockwise. Which way do you face?',38,700),None,WHITE,20,'22px 28px')
body+=step(1,'From one point to the next is 45°: 8 steps make 360°.',left=740,top=370,width=992,size=32)
body+=step(2,'135° = 45° + 45° + 45°: that is 3 steps.',left=740,top=470,width=992,size=32)
body+=step(3,'Count 3 steps clockwise from NW: N, NE, E.',left=740,top=570,width=992,size=32)
body+=answer(740,670,1052,'Face E.')
body+=pin(740,770,1052,p('Another: face E, turn 225° anticlockwise. 5 steps: NE, N, NW, W, SW.',32,700),'fade',SOFT,20,'16px 26px')
put('teach2',sec(f'{P}-teach2','25.5–28 MIN',body,'Teach. Children stand facing the front (North) and act it out. Think-aloud: "I face North-West. Each step on the compass is 45 degrees, so 135 degrees is 3 steps. Clockwise is the way clock hands go: North, North-East, East. I face East." Common mistake: counting NW itself as the first step. Point with a finger: move first, then count. Then the second example: 225° is 5 steps; anticlockwise from E: NE, N, NW, W, SW. Getting back from SW to E is 225° clockwise, or 135° anticlockwise, the shorter way.'))
put('try2',try_slide(f'{P}-try2','28–29.5 MIN • OPTIONAL','Your turn: compass turns','Count the 45° steps. Stand up and turn if it helps.',[('a','Face N. Turn 45° clockwise.','NE'),('b','Face S. Turn 3/4 turn clockwise.','E'),('c','Smallest turn from E to NW?','135° anticl.')],'Whiteboards. a) 1 step: NE. b) A 3/4 turn is 270° = 6 steps clockwise from S: SW, W, NW, N, NE, E. Or think: 3/4 clockwise is the same as 1/4 anticlockwise, and 1/4 anticlockwise from S is E. c) Clockwise from E to NW is 5 steps (225°); anticlockwise is 3 steps (135°), so the smallest turn is 135° anticlockwise.',size=36))

# ---------- 10. key ----------
body=h2('Key idea: count the turn')+card(p('A full turn is 360°: 4 right angles, 8 compass steps of 45°, 12 clock spaces of 30°. Estimate first, then measure.',44,700))+card(p('Angles side by side add up. The corner of a square or rectangle is 90°.',38,600,MUTED))
put('key',sec(f'{P}-key','29.5–30.5 MIN',body,'Say the key idea together. Common mistakes to watch for during the worksheet: (1) Reading the wrong protractor scale (40° written as 140°) instead of starting from the 0 on the arm and checking with an estimate. (2) Counting the numbers on the clock instead of the spaces between them, or measuring the bigger way round (210° instead of 150° at 7 o’clock). (3) Compass turns: mixing up clockwise and anticlockwise, or counting the starting direction as the first 45° step.'))
put('break',break_slide(f'{P}-break','30.5–34 MIN','Compass dance. Face North. On each clap, jump a quarter turn clockwise: N, E, S, W, N! Then half turns. Then 45° steps, saying each direction.','Four minutes. Online: children stand in view of the camera; the screen is North. Finish with "Turn to face the screen" from different directions: who turned the smallest way?'))

# ---------- teach: every angle in a fan (Q2) ----------
O=(300,330); g=''
for d,n in [(0,'P'),(20,'Q'),(70,'R')]:
    g+=ln(O,pt(O[0],O[1],270,d)); q=pt(O[0],O[1],300,d); g+=txt(q[0],q[1]+14,n,40)
g+=arc(O[0],O[1],150,0,20)+arc(O[0],O[1],95,20,70)+dot(O,10)+txt(O[0]-10,O[1]+50,'O',40)
q=pt(O[0],O[1],190,10); g+=txt(q[0],q[1]+12,'20°',32,TEAL)
q=pt(O[0],O[1],130,45); g+=txt(q[0],q[1]+12,'50°',32,TEAL)
body=h2('Find every angle: work in order')+pin(128,215,700,svgwrap(700,420,'Three rays OP, OQ and OR from point O. Angle POQ is 20 degrees and angle QOR is 50 degrees.',g),None)
body+=pin(880,240,912,p('∠POQ means the angle at O between OP and OQ. How many angles can you find?',36,700),None,WHITE,20,'22px 28px')
body+=step(1,'Side by side:  ∠POQ = 20°,  ∠QOR = 50°',left=880,top=400,width=852,size=32)
body+=step(2,'Two together:  ∠POR = 20° + 50° = 70°',left=880,top=500,width=852,size=32)
body+=answer(880,600,912,'3 angles. Angles side by side add up.')
body+=pin(128,700,1664,p('More rays? Count the small ones, then pairs side by side, then three together … until you reach the biggest.',34,700),'fade',SOFT,20,'18px 28px')
put('teachfan',sec(f'{P}-teachfan','34–36 MIN',body,'Teach before worksheet page 1 (Q2 has 4 rays). Online: many cameras show a mirrored self-view, so left and right can look swapped when a child shows a paper protractor or points an arm; check against the shared slide, not the video tile. Name angles with three letters: the middle letter is always the vertex O. Think-aloud: "First the small angles that sit next to each other: 20° and 50°. Then two together: 20 + 50 = 70°. With 3 rays there are 3 angles." Do NOT give the number of angles for 4 rays: let pairs find it on the worksheet. Hint for strugglers: "Start from OA. List every angle that starts at OA, then every angle that starts at OB …"'))

# ---------- worksheet page 1 ----------
put('ws1',ws_preview(f'{P}-ws1','36–51.5 MIN','Worksheet page 1: with your partner',[('Q1','Estimate each angle first. Then measure it with your protractor.'),('Q2','Every angle in the fan. Work in order; angles side by side add up.')],'Stuck? Compare with the corner of a page. Draw longer arms with a ruler.','Minutes 36 to 51.5. Pair task for Q1: each child estimates and measures two of the four angles, then checks the partner\'s two (about 4.5 minutes, not 8). Walk around and watch protractors: centre on the vertex, baseline on an arm, count from 0. Ask "Does your answer match your estimate?" Q1c and d are turned, so children must turn the protractor (or the page). Accept answers within 2°.'))
put('ws1ans',checks(f'{P}-ws1ans','51.5–53 MIN','Page 1: check together',[('Q1','a 40°,   b 115°,   c 75°,   d 150°   (b and d are bigger than 90°)'),('Q2a','6 angles'),('Q2b','30°, 60°, 45°;   ∠AOC 90°,  ∠BOD 105°;   ∠AOD 135°'),('Q2c','∠AOC is the right angle (30° + 60°)')],
 'Click after a pair explains. Q1: accept 2° either way. If a child wrote 140° for a, ask "Is a bigger than a right angle?" Q2: work in order. Small angles: ∠AOB 30°, ∠BOC 60°, ∠COD 45°. Two together: ∠AOC = 30 + 60 = 90°, ∠BOD = 60 + 45 = 105°. All three: ∠AOD = 30 + 60 + 45 = 135°. 3 + 2 + 1 = 6 angles.',gapy=140))

# ---------- teach: clock angles (Q3) ----------
g=clock(200,200,185,2,0)+arc(200,200,74,30,90,RED,6)
g2=clock(200,200,185,10,0)+arc(200,200,74,90,150,RED,6)
body=h2('Clock angles: 12 spaces of 30°')
body+=pin(128,225,410,svgwrap(400,400,'A clock at 2 o’clock with the angle between the hands marked',g),None)
body+=pin(560,225,410,svgwrap(400,400,'A clock at 10 o’clock with the angle between the hands marked',g2),'fade')
body+=step(1,'360° ÷ 12 = 30° for each space.',left=1000,top=240,width=732,size=32)
body+=step(2,'2 o’clock: 2 spaces. 2 × 30° = 60°.',left=1000,top=340,width=732,size=32)
body+=step(3,'10 o’clock: the SHORTER way is 2 spaces: 60°.',left=1000,top=440,width=732,size=32)
body+=step(4,'Think Harder: minute hand, 6° a minute.',left=1000,top=590,width=732,size=30)
body+=answer(128,730,1664,'Think Harder: 6:05 to 6:20 is 15 minutes:  15 × 6° = 90°')
put('teachclock',sec(f'{P}-teachclock','53–54 MIN',body,'Teach before worksheet page 2 (Q3). Link back to explore: 3 o’clock was 90° = 3 spaces, so one space is 30°. Click 1: 2 o’clock. Click 2 shows 10 o’clock: "Is it 10 spaces? No: go the shorter way, from 10 to 12, 2 spaces." Then the minute hand: it goes all the way round (360°) in 60 minutes, so 360 ÷ 60 = 6° a minute, or 30° every 5 minutes. Count on with a paper clock: 6:05 to 6:20 is 3 jumps of 5 minutes, 3 × 30° = 90°.'))

# ---------- teach: corners of squares and rectangles (Q5) ----------
g=''
A=(40,70); g+=f'<rect x="40" y="70" width="400" height="250" fill="{SKY}" stroke="{NAVY}" stroke-width="5"/>'
e=(40+250/math.tan(math.radians(37)),320); g+=ln(A,e,5)+arc(A[0],A[1],70,-37,0,TEAL)+arc(A[0],A[1],48,-90,-37,RED)
q=pt(A[0],A[1],108,-18.5); g+=txt(q[0],q[1]+12,'37°',32,TEAL); q=pt(A[0],A[1],82,-66); g+=txt(q[0],q[1]+12,'?',38,RED)
B=(560,320); g+=f'<rect x="560" y="40" width="280" height="280" fill="{SKY}" stroke="{NAVY}" stroke-width="5"/>'
g+=ln(B,(840,320-280*math.tan(math.radians(20))),5)+ln(B,(840,320-280*math.tan(math.radians(45))),5)
g+=arc(B[0],B[1],150,0,20)+arc(B[0],B[1],100,20,45,RED)+arc(B[0],B[1],60,45,90)
q=pt(B[0],B[1],190,10); g+=txt(q[0],q[1]+12,'20°',30,TEAL); q=pt(B[0],B[1],130,32); g+=txt(q[0],q[1]+12,'?',38,RED); q=pt(B[0],B[1],95,67.5); g+=txt(q[0],q[1]+12,'45°',30,TEAL)
O=(1300,320); s=210
def sqpoly(d0,fill,op):
    pts=[O,pt(O[0],O[1],s,d0),pt(O[0],O[1],s*math.sqrt(2),d0+45),pt(O[0],O[1],s,d0+90)]
    return f'<polygon points="{" ".join(f"{a:.1f},{b:.1f}" for a,b in pts)}" fill="{fill}" fill-opacity="{op}" stroke="{NAVY}" stroke-width="5"/>'
g+=sqpoly(0,SKY,0.9)+sqpoly(50,YEL,0.45)+arc(O[0],O[1],90,50,90,TEAL)+arc(O[0],O[1],50,0,140,RED)
q=pt(O[0],O[1],125,70); g+=txt(q[0],q[1]+12,'40°',30,TEAL); q=pt(O[0],O[1],85,118); g+=txt(q[0]-6,q[1]+12,'?',38,RED)
body=h2('Corners of squares and rectangles: 90°')
body+=pin(128,215,1664,svgwrap(1664,360,'Three drawings. A rectangle corner cut into 37 degrees and an unknown angle. A square corner cut into 20 degrees, an unknown angle and 45 degrees. Two squares sharing a corner and overlapping by 40 degrees, with the big angle between their outside sides unknown.',g),None)
for i,(x,t) in enumerate([(128,'90° − 37° = 53°'),(640,'90° − 20° − 45° = 25°'),(1150,'90° + 90° − 40° = 140°')]):
    body+=answer(x,600,560 if i<2 else 642,t)
body+=pin(128,720,1664,p('Two squares: add both corners, then take away the overlap, which was counted twice.',34,700),'fade',SOFT,20,'18px 28px')
put('teachrect',sec(f'{P}-teachrect','54–54.5 MIN',body,'Teach before worksheet page 2 (Q5 has two parts; the third drawing, two squares, is an optional extension and is the idea behind Challenge 9). Fold a square of paper to show the corner is a right angle. Click each answer after children try on whiteboards. Rectangle: the whole corner is 90°, so the missing part is 90 − 37 = 53°. Square cut in three: 90 − 20 − 45 = 25° (check 20 + 25 + 45 = 90). Two squares: the two right angles together make 180°, but the overlap of 40° is counted twice, so 180 − 40 = 140°. Act it out with two paper squares on top of each other.'))

# ---------- teach: robot turns and working backwards (Q4d, Q6) ----------
g=compass(250,250,190,hi=('E','SE'))
body=h2('Robot turns: one card at a time')+pin(128,215,520,svgwrap(500,500,'An 8-point compass',g),None)
body+=pin(700,230,1092,p('A robot faces E. Cards: 45° anticlockwise, then 90° anticlockwise, then 180°.',34,700),None,WHITE,20,'20px 28px')
body+=step(1,'E → 45° anticlockwise → NE',left=700,top=380,width=1032,size=32)
body+=step(2,'NE → 90° anticlockwise (2 steps) → NW',left=700,top=470,width=1032,size=32)
body+=step(3,'NW → 180° (4 steps) → SE.   The robot faces SE.',left=700,top=560,width=1032,size=32)
body+=pin(700,660,1092,p('Work backwards: Mei turned 90° clockwise and now faces S. Undo it: turn 90° anticlockwise from S → E. She started facing E.',32,700),'fade',SOFT,20,'18px 26px')
body+=pin(128,800,1664,p('Find ALL pairs: list every pair of cards, then test each one. Do not stop at the first that works.',32,700),'fade',WHITE,20,'16px 28px')
put('teachrobot',sec(f'{P}-teachrobot','54.5–55.5 MIN',body,'Teach before worksheet page 2 (Q4d works backwards; Q6a is the robot). Act it out: one child is the robot, the group reads the cards. To undo a turn, turn the same amount the other way, like taking off shoes after socks. Check Mei: start E, 90° clockwise is S ✓. For "find all pairs" (a Think Harder question now): with three cards A, B, C the pairs are A and B, A and C, B and C. Example (not on the worksheet): cards 45° clockwise, 90° anticlockwise, 180°, from N to E. 45 + 180: SW, not this one. 45 cw and 90 acw: NW, not this one. 90 acw and 180: E ✓. Only one pair works.'))

# ---------- worksheet page 2 ----------
put('ws2',ws_preview(f'{P}-ws2','55.5–77.5 MIN','Worksheet page 2: on your own',[('Q3','Clock angles. Count the spaces of 30° the shorter way.'),('Q4','Compass turns. Count 45° steps; undo a turn to work backwards.'),('Q5','Corners of squares and rectangles are 90°.'),('Q6','The robot. One card at a time.')],'Finished early? Stretch and Challenge come next.','Children work alone. Note who needs a short catch-up next lesson, especially anyone who still counts the starting direction as a step or counts the numbers on the clock instead of the spaces.'))
put('ws2ans',checks(f'{P}-ws2ans','77.5–80 MIN','Page 2: check together',[('Q3','a) 120°   b) 150°   c) 1 o’clock and 11 o’clock'),('Q4','a) N   b) E   c) 135° clockwise   d) NE'),('Q5','∠a = 32°   ∠b = 27°'),('Q6','a) SW')],
 'Click after a child explains. Q3b: 7 o’clock is 5 spaces the shorter way (7 to 12), 150°, not 210°. The minute-hand question (3:10 to 3:35 is 25 minutes × 6° = 150°) is now a Think Harder item, so the page has fewer parts. Q4b: 135° is 3 steps anticlockwise from SW: S, SE, E. Q4c: clockwise NE, E, SE, S is 3 steps (135°); anticlockwise would be 5 steps (225°). Q4d: undo 90° anticlockwise by turning 90° clockwise from NW: N, NE. Q5: 90 − 58 = 32; 90 − 15 − 48 = 27. (The overlapping-squares idea is now a Challenge question.) Q6a: N → E → NE → SW. The "find ALL the pairs" question is now Think Harder stretch 4: list all 6 pairs: 45+90 (SE), 45 cw + 135 acw (W ✓), 45+180 (SW), 90 cw + 135 acw (NW), 90+180 (W ✓), 135 acw + 180 (NE).',gapy=150))

# ---------- stretch / challenge ----------
from p4bank import th_items, th_notes, gf_numbers  # slide Think harder = the printed page (docs/audit/reaudit_fixes_p4.md)
st=th_items(6)
def numgrid(items,size=30): return '<div style="display:grid;grid-template-columns:1fr 1fr;gap:24px;align-items:stretch">'+''.join(card(p(f'<span style="color:{TEAL}">{a}</span>  {E(b)}',size,600,raw=True),extra='padding:24px 32px') for a,b in items)+'</div>'
put('stretch',sec(f'{P}-stretch','Optional, if you finish early',h2('Think harder')+numgrid(st,34),th_notes(6)))
ch=[('1.','What is the angle between the hands of a clock at 3:30?'),('2.','Five rays come out of one point and make 4 equal angles side by side. The angle between the two outside rays is 120°. How many angles can you find altogether? How many are right angles?')]
put('challenge',sec(f'{P}-challenge','Optional, if you finish early',h2('Go further')+numcards(ch,36),'Pairs try first, then use the "see it" slide if stuck, then the walk-through. Answers: 1) 75°. At 3:30 the minute hand points to 6, but the hour hand is HALFWAY between 3 and 4 (half an hour has passed). From the hour hand to 4 is half a space (15°), from 4 to 6 is 2 spaces (60°): 75°. 2) 10 angles (4 small, 3 of two parts, 2 of three parts, 1 of four parts). Each small angle is 120 ÷ 4 = 30°, so the three-part angles are 90°: 2 right angles. More are in the question bank and on the Think Harder pages.'))
g1=clock(230,225,200,3,30)
O=(220,410); g2=''
for d in [0,30,60,90,120]: g2+=ln(O,pt(O[0],O[1],320,d),6)
g2+=arc(O[0],O[1],70,0,120,RED,6)+dot(O,9)
q=pt(O[0],O[1],200,105); g2+=txt(q[0],q[1]+12,'120°',34,RED)+txt(560,110,'4 equal',36,TEAL,'start')+txt(560,160,'angles',36,TEAL,'start')+txt(560,235,'How many',32,NAVY,'start')+txt(560,280,'angles?',32,NAVY,'start')
body=h2('Go further: see it',60)+'<div style="display:flex;gap:32px;align-items:flex-start">'
body+=card(f'<p style="font-size:30px;font-weight:700;color:{TEAL}">Q1: Where is the hour hand at 3:30?</p>'+svgwrap(460,450,'A clock showing 3:30: the minute hand points to 6 and the hour hand is halfway between 3 and 4',g1,'width:100%;max-height:450px;height:auto;display:block'),extra='flex:1;min-width:0;padding:20px 24px;align-items:center')
body+=card(f'<p style="font-size:30px;font-weight:700;color:{TEAL}">Q2: Five rays, 4 equal angles</p>'+svgwrap(760,450,'Five rays from one point make 4 equal angles; the whole angle is 120 degrees',g2,'width:100%;height:auto;display:block'),extra='flex:1;min-width:0;padding:20px 24px')+'</div>'
put('chdiag',sec(f'{P}-chdiag','Optional, if you finish early',body,'Show after pairs have tried the Challenge, or if they are stuck. The pictures show the problem, not the answer. Ask: Q1, is the hour hand pointing exactly at 3? Why not? How far has it moved since 3 o’clock? Q2, how big is each small angle? How can you count the angles without missing one? Answers are in the Challenge slide notes.'))
body=h2('Go further: walk-through')+pin(128,250,800,p('Q1: the hour hand moves too',38,800,TEAL))
for i,t in enumerate(['Minute hand: pointing at 6.','Half an hour has passed, so the hour hand is halfway from 3 to 4.','Hour hand to 4: half a space = 15°.   4 to 6: 2 spaces = 60°.','15° + 60° = 75°']): body+=pin(128,330+i*125,800,p(t,31),'rise',WHITE)
body+=pin(992,250,800,p('Q2: count in order',38,800,TEAL))
for i,t in enumerate(['Each small angle: 120° ÷ 4 = 30°.','1 part: 4 angles.  2 parts: 3.  3 parts: 2.  4 parts: 1.','4 + 3 + 2 + 1 = 10 angles.','3 parts = 90°: 2 right angles ✓']): body+=pin(992,330+i*125,800,p(t,31),'rise',WHITE)
put('chwalk',sec(f'{P}-chwalk','Optional, if you finish early',body,'Use after pairs have tried. Q1: many children say 90°, as if the hour hand still pointed at 3. Use a real clock: move the minute hand from 12 to 6 and watch the hour hand creep half way to 4. Q2: the list in order (by number of parts) is the same idea as the fan on page 1; 4 + 3 + 2 + 1 is a pattern worth noticing: with 6 rays it would be 5 + 4 + 3 + 2 + 1 = 15.'))

# ---------- talk / exit ----------
body=h2('Talk time')+card(chip('TALK TIME',YEL,NAVY)+p('Is turning 270° clockwise the same as turning 90° anticlockwise? How do you know?',42,600))+card(p('Sentence starters:',34,400,MUTED)+p('“I noticed that …”   “I tested it by …”   “I know because …”',38,600))
put('talk',sec(f'{P}-talk','80–83.5 MIN',body,'Minutes 80 to 83.5. Pair talk is 1 minute (no breakout rooms: children tell the grown-up beside them, or write one sentence), then test it standing up: everyone faces North and does both turns. Answer: yes, you end up facing the same way (both from N end at W), because 270° + 90° = 360°, a full turn. The turns are different sizes, but the direction you end up facing is the same. Not asked in class (moved to the Weekly Dose of Thinking Math): "Ben says the angle at 3 o’clock is smaller than at 9 o’clock because 3 is smaller than 9. Who agrees?" (both are 90°: 3 spaces the shorter way). Praise the reasons, not only the answers.'))
body=h2('Exit ticket')+card(chip('EXIT TICKET')+p('Face N. Turn 135° clockwise. Which way do you face? What is the angle between the clock hands at 5 o’clock?',46,600))+card(p('Write your answer on a slip of paper. Show it to your tutor. Then collect your stamp in your inquiry journal.',34,400))
put('exit',sec(f'{P}-exit','83.5–86.5 MIN',body,'Minutes 83.5 to 86.5. Answers: SE (3 steps of 45°: NE, E, SE). 150° (5 spaces of 30°). Extension: find all the o’clock times when the smaller angle between the hands is more than 90° (4, 5, 6, 7 and 8 o’clock).'))

# ---------- write ----------
# ---------- fix pass (rebuild/p4_fix.py): sneak-peek puzzles, looking back, neutral names, go further, minute labels ----------
import subprocess as _sp, p4_fix
_G=json.loads(_sp.check_output(['node','-e',"process.stdout.write(JSON.stringify(require('"+os.path.join(H,'..','p4','content','l6.js')+"').gaps))"]))
_ID='p4l6'
_PIC=globals().get('PIC')

order=[f'{P}-{x}' for x in ['title','warm1','warm2','explore1','explore2','teach1','teach2','try2','key','break','teachfan','ws1','ws1ans','teachclock','teachrect','teachrobot','ws2','ws2ans','stretch','challenge','chdiag','chwalk','talk','exit']]
p4_fix.finish(S,6,_G,pic=_PIC)
order=p4_fix.order(order,6)
assert set(order)==set(S), set(order)^set(S)
p4_fix.check_times(S,6)  # every time pill must match rebuild/p4_budget.py
sd=os.path.join(D,'slides')
for f in os.listdir(sd):
    if f.endswith('.html') and f[:-5] not in S: os.remove(os.path.join(sd,f))
for i,h in S.items(): open(os.path.join(sd,i+'.html'),'w').write(h)
deck={'v':4,'createdOnFiles':{'v':1,'at':datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')},'lists':'css',
 'title':'Math Inquirers P4: Lesson 6 – Angle Turns','order':order,'cover':f'{P}-title',
 'sections':{'s1':{'description':'Warm-up and explore','start':f'{P}-title'},'s2':{'description':'Teach: measure, estimate and compass turns','start':f'{P}-teach1'},'s3':{'description':'Worksheet with teaching before each page','start':f'{P}-break'},'s4':{'description':'Stretch, challenge, talk and exit','start':f'{P}-stretch'}},
 'faces':{'fredoka':{'family':'Fredoka','href':'https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&display=swap'},'nunito-sans':{'family':'Nunito Sans','href':'https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@400;600;700&display=swap'}},
 'designSystems':[]}
json.dump(deck,open(os.path.join(D,'deck.json'),'w'),indent=1,ensure_ascii=False)
print(len(order),'slides')
