"""Math Inquirers P6, Lesson 3: Below Zero (negative numbers; a sprite on a number line). Writes split/p6l3/project."""
import json,os,re,sys,datetime
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,H)
import slidekit
from slidekit import *
slidekit.FOOT='Math Inquirers P6  •  Notice it. Test it. Explain why.'
RED='#D64545'
L='p6l3'
D=os.path.join(H,'..','split',L,'project'); os.makedirs(os.path.join(D,'slides'),exist_ok=True)
S={}
def put(i,h): S[i]=h

# ---------- drawing helpers (our own block style: rounded shapes, never Scratch artwork) ----------
BK={'event':(YEL,NAVY),'control':(TEAL,WHITE),'var':(RED,WHITE),'motion':(SKY,NAVY),'looks':(WHITE,NAVY)}
def tw(s,fs):
    w=0
    for ch in s:
        if ch in "il.,:;|!'()[] ": w+=0.32
        elif ch in 'mwMW': w+=0.86
        elif ch.isupper() or ch in '−+×=<>*?': w+=0.66
        else: w+=0.57
    return w*fs
def _row(x,y,text,kind,fs,rh):
    fill,fg=BK[kind]; segs=[s for s in re.split(r'(\[[^\]]*\])',text) if s]; pad=fs*0.6
    parts=[]; cx=x+pad
    for sg in segs:
        if sg.startswith('['):
            v=sg[1:-1]; pw=max(tw(v,fs)+fs*1.1,fs*1.6); ph=fs*1.3
            parts.append(f'<rect x="{cx:.0f}" y="{y+(rh-ph)/2:.0f}" width="{pw:.0f}" height="{ph:.0f}" rx="{ph/2:.0f}" fill="{SKY if fill==WHITE else WHITE}" stroke="{NAVY}" stroke-width="2"/><text x="{cx+pw/2:.0f}" y="{y+rh/2+fs*0.36:.0f}" font-size="{fs}" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="Arial">{E(v)}</text>')
            cx+=pw+fs*0.35
        else:
            t=sg.strip()
            if t:
                parts.append(f'<text x="{cx:.0f}" y="{y+rh/2+fs*0.36:.0f}" font-size="{fs}" font-weight="700" fill="{fg}" font-family="Arial">{E(t)}</text>')
                cx+=tw(t,fs)+fs*0.25
    return parts,cx-fs*0.25+pad-x
def blocks_svg(prog,fs=30,label='Code blocks',scale=1.0):
    """prog: list of (indent, kind, text); text may hold [value] inputs drawn as white pills."""
    rh=fs*1.9; arm=fs*1.0; foot=fs*0.8; ind=arm
    shapes=[]; texts=[]; y=fs*0.6 if prog and prog[0][1]=='event' else 4; maxx=0; stack=[]
    def close(level):
        nonlocal y,maxx
        while stack and stack[-1][0]>=level:
            lv,x,yt,w=stack.pop(); fill=BK['control'][0]
            shapes.append(f'<path d="M{x} {yt} H{x+w} V{yt+rh} H{x+arm} V{y} H{x+w} V{y+foot} H{x} Z" fill="{fill}" stroke="{NAVY}" stroke-width="3" stroke-linejoin="round"/>')
            y+=foot
    for lv,kind,text in prog:
        close(lv)
        x=4+lv*ind
        parts,w=_row(x,y,text,kind,fs,rh); w=max(w,fs*4)
        if kind=='control':
            stack.append((lv,x,y,w)); texts+=parts
        elif kind=='event':
            shapes.append(f'<path d="M{x} {y+rh} V{y+fs*0.15} Q{x+fs*2} {y-fs*0.75} {x+fs*4} {y+fs*0.15} H{x+w-10} Q{x+w} {y+fs*0.15} {x+w} {y+fs*0.15+10} V{y+rh} Z" fill="{BK[kind][0]}" stroke="{NAVY}" stroke-width="3" stroke-linejoin="round"/>'); texts+=parts
        else:
            shapes.append(f'<rect x="{x}" y="{y:.0f}" width="{w:.0f}" height="{rh:.0f}" rx="10" fill="{BK[kind][0]}" stroke="{NAVY}" stroke-width="3"/>'); texts+=parts
        maxx=max(maxx,x+w); y+=rh
    close(0)
    W=maxx+6; Hh=y+6
    return f'<svg aria-label="{E(label)}" viewBox="0 0 {W:.0f} {Hh:.0f}" xmlns="http://www.w3.org/2000/svg" style="width:{W*scale:.0f}px;height:{Hh*scale:.0f}px;flex:none">'+''.join(shapes)+''.join(texts)+'</svg>'
def numline_svg(lo,hi,w=1664,h=190,marks=(),jumps=(),every=1,lab_every=1,label='Number line',only=False,fs=30,ly=None):
    x0,x1=50,w-50; ly=ly or h-70
    X=lambda v: x0+(v-lo)*(x1-x0)/(hi-lo)
    s=[]
    if not only:
        s.append(f'<line x1="{x0-34}" y1="{ly}" x2="{x1+34}" y2="{ly}" stroke="{NAVY}" stroke-width="4"/><polygon points="{x0-44},{ly} {x0-26},{ly-10} {x0-26},{ly+10}" fill="{NAVY}"/><polygon points="{x1+44},{ly} {x1+26},{ly-10} {x1+26},{ly+10}" fill="{NAVY}"/>')
        v=lo
        while v<=hi:
            big=(v%lab_every==0)
            s.append(f'<line x1="{X(v):.1f}" y1="{ly-(14 if big else 9)}" x2="{X(v):.1f}" y2="{ly+(14 if big else 9)}" stroke="{NAVY}" stroke-width="{4 if v==0 else 3}"/>')
            if big: s.append(f'<text x="{X(v):.1f}" y="{ly+14+fs+2}" font-size="{fs}" font-weight="{800 if v==0 else 600}" text-anchor="middle" fill="{TEAL if v==0 else NAVY}" font-family="Arial">{v if v>=0 else "−"+str(-v)}</text>')
            v+=every
    for m in marks:
        v,t,col=m[:3]; dy=m[3] if len(m)>3 else 26
        s.append(f'<circle cx="{X(v):.1f}" cy="{ly}" r="13" fill="{col}" stroke="{NAVY}" stroke-width="3"/>')
        if t: s.append(f'<text x="{X(v):.1f}" y="{ly-dy}" font-size="{fs}" font-weight="800" text-anchor="middle" fill="{NAVY}" font-family="Arial">{E(t)}</text>')
    for j in jumps:
        a,b,t,col=j[:4]
        xa,xb=X(a),X(b); xm=(xa+xb)/2; hh=j[4] if len(j)>4 else min(ly-fs-20,40+abs(xb-xa)*0.18); cy=ly-8-2*hh
        s.append(f'<path d="M{xa:.1f} {ly-8} Q{xm:.1f} {cy:.1f} {xb:.1f} {ly-8}" fill="none" stroke="{col}" stroke-width="5"/>')
        dx,dy=xb-xm,(ly-8)-cy; n=(dx*dx+dy*dy)**0.5; ux,uy=dx/n,dy/n
        bx,by=xb-22*ux,ly-8-22*uy
        s.append(f'<polygon points="{xb:.1f},{ly-8} {bx-11*uy:.1f},{by+11*ux:.1f} {bx+11*uy:.1f},{by-11*ux:.1f}" fill="{col}"/>')
        s.append(f'<text x="{xm:.1f}" y="{ly-8-hh-14:.1f}" font-size="{fs}" font-weight="800" text-anchor="middle" fill="{col}" font-family="Arial">{E(t)}</text>')
    return f'<svg aria-label="{E(label)}" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="width:{w}px;height:{h}px;flex:none">'+''.join(s)+'</svg>'
def N(v): return str(v) if v>=0 else '−'+str(-v)
def card_q(a,b,size=38): return card(p(f'<span style="color:{TEAL}">{E(a)}</span>  {E(b)}',size,600,raw=True))
def title_slide(sid,lesson,week,title,topic,today,notes):
    return (f'<section id="{sid}" data-transition="fade" style="background:{NAVY};color:{CREAM};font-family:{BF};padding:128px 128px 160px;display:flex;flex-direction:column;justify-content:center;gap:36px">\n'
            f'<p style="font-size:32px;font-weight:700;letter-spacing:4px;color:{YEL}">LESSON {lesson}  •  WEEK {week}</p>\n'
            f'<h1 style="font-family:{HF};font-size:128px;font-weight:600;line-height:1.05">{E(title)}</h1>\n<p style="font-size:44px;color:#C9D4EC">{E(topic)}</p>\n'
            f'<div style="background:#26385F;border-radius:24px;padding:40px;display:flex;flex-direction:column;gap:12px"><p style="font-size:28px;font-weight:700;letter-spacing:3px;color:{YEL}">TODAY WE WILL</p><p style="font-size:44px;font-weight:600">{E(today)}</p></div>\n'
            f'<p style="position:absolute;left:128px;bottom:64px;width:1400px;font-size:24px;color:#B7C3DD">{E(slidekit.FOOT)}</p>\n<aside>{E(notes)}</aside>\n</section>\n')
def break_slide(sid,head,text,sub,notes):
    return (f'<section id="{sid}" data-transition="fade" style="background:{TEAL};color:{CREAM};font-family:{BF};padding:128px 128px 160px;display:flex;flex-direction:column;justify-content:center;gap:36px">\n'
            f'<p style="font-size:32px;font-weight:700;letter-spacing:4px;color:{YEL}">35–40 MIN</p>\n<h2 style="font-family:{HF};font-size:110px;font-weight:600;line-height:1.05">{E(head)}</h2>\n'
            f'<p style="font-size:48px;font-weight:600">{E(text)}</p>\n<p style="font-size:36px;color:#D7EFEA">{E(sub)}</p>\n'
            f'<p style="position:absolute;left:128px;bottom:64px;width:1400px;font-size:24px;color:#D7EFEA">{E(slidekit.FOOT)}</p>\n<aside>{E(notes)}</aside>\n</section>\n')
def ans_rows(rows,top=250,gapy=130,lw=200,size=36):
    b=''
    for i,(a,c) in enumerate(rows):
        t=top+i*gapy
        b+=pin(128,t,lw-20,f'<p style="font-size:36px;font-weight:800;color:{TEAL}">{E(a)}</p>',None,WHITE,20,'18px 24px')
        b+=pin(128+lw,t,1664-lw,f'<p style="font-size:{size}px;font-weight:800;line-height:1.2">{E(c)}</p>','pop',YEL,20,'18px 26px')
    return b

PY_MAIN='temp = 5\nfor hour in range(6):\n    temp = temp + (-3)\n    print(temp)'
PY_NOTE='Optional Python version (same program, for children who know Python): '+' | '.join(PY_MAIN.split('\n'))+'   Output: 2, -1, -4, -7, -10, -13 (one per line).'
THERMO=[(0,'event','when flag clicked'),(0,'var','set temp to [5]'),(0,'control','repeat [6]'),(1,'var','change temp by [−3]'),(1,'looks','say [temp] for [1] seconds')]

# ---------- 1 title ----------
put(f'{L}-title',title_slide(f'{L}-title',3,2,'Below Zero','Negative numbers  •  Code: a sprite on a number line',
 'Use a number line to compare, add and subtract negative numbers, and make a variable in code go below zero.',
 'Objective: Order and compare negative numbers on a number line; add and subtract with negative numbers by moving along the line (temperature, lifts, sea level); use "change by" a negative number in code and trace a variable that goes below 0. '
 'Materials: laptop or desktop with Scratch 3 open (scratch.mit.edu, no log-in needed), mini whiteboard and marker, workbook, pencil. Tutor: this deck, Scratch open for screen share. '
 'Online set-up: children keep Scratch in one browser tab and the video call in another; ask them to rename the sprite "Dot" so nobody is distracted by costumes. Children share their screen only when asked. '
 'Time plan: warm-up 0 to 10, explore at the computer 10 to 25, teaching 25 to 35 (click to reveal each step and answer), brain break 35 to 40, worksheet 40 to 70 with short teaching before each page and a check-together slide after it, talk time 70 to 80, exit ticket 80 to 90.'))

# ---------- 2 warm1: cold city line-up ----------
cities=[('Singapore',25),('Tokyo',3),('Seoul',-7),('Beijing',-9),('Harbin',-22)]
body=h2('Warm-up: cold city line-up')+p('7 a.m. on a December morning. Line the cities up from coldest to warmest.',34,600,MUTED)
for i,(c,t) in enumerate(cities):
    body+=pin(128+i*338,330,306,f'<p style="font-family:{HF};font-size:36px;font-weight:600">{E(c)}</p><p style="font-size:48px;font-weight:800;color:{TEAL if t>=0 else RED}">{N(t)} °C</p>',None,WHITE,20,'16px 22px',f'box-sizing:border-box;border:3px solid {NAVY}')
body+=pin(128,500,1664,numline_svg(-25,30,1664,150,every=5,lab_every=5,label='Number line from minus 25 to 30',ly=80),None)
body+=pin(128,500,1664,numline_svg(-25,30,1664,150,marks=[(t,c[:3],YEL if t>=0 else SKY,60 if c=='Seoul' else 26) for c,t in cities],every=5,lab_every=5,label='Cities placed on the number line',only=True,ly=80),'fade')
body+=answer(128,670,1664,'Coldest to warmest:  Harbin −22,  Beijing −9,  Seoul −7,  Tokyo 3,  Singapore 25')
body+=qrow(128,790,1100,'Then:','How many degrees warmer is Tokyo than Seoul?',34)+answer(1260,790,532,'10 degrees')
put(f'{L}-warm1',sec(f'{L}-warm1','0–5 MIN',body,
 'Minutes 0 to 5. Cold city line-up. Give each child a city (online: type the city names in the chat in order, coldest first, then reveal). Ask: "Which is colder, Beijing at −9 or Seoul at −7? Nine is bigger than seven, so why is −9 colder?" Let them argue before any click. '
 'Click 1 puts the cities on the number line (Har = Harbin, Bei = Beijing, Seo = Seoul, Tok = Tokyo, Sin = Singapore). Click 2 shows the order. Click 3 shows the gap Tokyo to Seoul: from −7 up to 0 is 7, then up to 3 is 3 more, 10 degrees. '
 'Extra: "How much warmer is Singapore than Harbin?" (22 up to 0, then 25 more: 47 degrees). Watch for children who say −9 is warmer than −7 because 9 > 7: we fix this with the number line in a moment.'))

# ---------- 3 warm2 ----------
qs=[('1.','It is 3 °C. It falls 5 degrees. What is it now?','−2 °C'),('2.','Which is colder: −7 °C or −2 °C?','−7 °C'),('3.','Count back in 3s: 6, 3, 0, __, __','−3, −6'),('4.','What number is 4 less than 1?','−3'),('5.','A lift is at B1. It goes down 2 floors. Where is it?','B3')]
body=h2('Quick questions')+''.join(qrow(128,250+i*125,1250,a,b,36) for i,(a,b,c) in enumerate(qs))+''.join(answer(1420,250+i*125,372,c) for i,(a,b,c) in enumerate(qs))
put(f'{L}-warm2',sec(f'{L}-warm2','5–10 MIN',body,'Minutes 5 to 10. Whiteboards: write, hold up together, then click. Answers: 1) −2 °C (3 down to 0, then 2 more).  2) −7 °C (further below 0).  3) −3, −6 (the pattern keeps going past 0).  4) −3.  5) B3. Ask: "Where have you seen numbers below zero?" (freezer, weather apps for Japan or Korea, basement lifts, golf scores, a bank balance that is overdrawn, sea level.)'))

# ---------- 4 explore1 ----------
stage=(f'<svg aria-label="The Scratch stage is a number line: x goes from minus 240 to 240" viewBox="0 0 760 330" xmlns="http://www.w3.org/2000/svg" style="width:700px;height:304px;flex:none">'
 f'<rect x="20" y="10" width="720" height="250" rx="14" fill="{SKY}" stroke="{NAVY}" stroke-width="4"/>'
 f'<line x1="20" y1="135" x2="740" y2="135" stroke="{NAVY}" stroke-width="3" stroke-dasharray="10 8"/>'
 +''.join(f'<line x1="{380+v*1.5:.0f}" y1="125" x2="{380+v*1.5:.0f}" y2="145" stroke="{NAVY}" stroke-width="3"/>' for v in (-100,0,100))
 +f'<circle cx="{380-150*1.5:.0f}" cy="105" r="26" fill="{YEL}" stroke="{NAVY}" stroke-width="4"/><text x="{380-150*1.5:.0f}" y="66" font-size="26" font-weight="800" text-anchor="middle" fill="{NAVY}" font-family="Arial">Dot</text>'
 +''.join(f'<text x="{x}" y="300" font-size="28" font-weight="{800 if v=="0" else 600}" text-anchor="middle" fill="{TEAL if v=="0" else NAVY}" font-family="Arial">{v}</text>' for x,v in [(52,'−240'),(230,'−100'),(380,'0'),(530,'100'),(712,'240')])
 +'</svg>')
steps=['Set x to 0. Your sprite (call it Dot) is in the middle.','Predict, then test: change x by 100, then change x by −250. Where is Dot?','Build the thermometer program on the right.','Predict the LAST number it says. Then click the flag.']
left=card(chip('EXPLORE AT THE COMPUTER')+'<ol style="font-size:32px;font-weight:600;padding-left:44px;display:flex;flex-direction:column;gap:10px;line-height:1.3">'+''.join(f'<li>{E(s)}</li>' for s in steps)+'</ol>',extra='flex:1;min-width:0')
right=card(stage+blocks_svg(THERMO,26,'Thermometer program: when flag clicked, set temp to 5, repeat 6: change temp by minus 3, say temp for 1 seconds'),extra='flex:none;width:760px;padding:20px 24px;gap:10px')
body=h2('Explore: the stage is a number line')+f'<div style="display:flex;gap:32px;align-items:flex-start">{left}{right}</div>'
put(f'{L}-explore1',sec(f'{L}-explore1','10–15 MIN',body,
 'Minutes 10 to 15. Screen-share Scratch for 1 minute: show the x number under the stage as you drag the sprite left and right. "The stage is a number line. The middle is 0. Left of the middle is negative." Then children work in pairs (breakout rooms online), each on their own computer. '
 'Step 2: Dot starts at 0, change x by 100 takes it to 100, change x by −250 takes it to −150. Step 3: the variable is made with "Make a Variable" (call it temp). There is no "decrease" block: to go down you change by a negative number. Step 4: they must write the prediction on the whiteboard BEFORE clicking. '
 'The program says 2, −1, −4, −7, −10, −13. Early finishers: add "if temp < 0 then say Below zero!" inside the loop, or make Dot glide to x = temp × 10 each time so it walks along the stage. '
 +PY_NOTE))

# ---------- 5 explore2 ----------
ex=[('1.','Where did Dot end up after +100 and then −250?'),('2.','What was the last number the thermometer said? Did your prediction match?'),('3.','Scratch has no "take away" block for variables. How do we make a variable go down?')]
body=h2('Explore: talk about it')+''.join(card_q(a,b,40) for a,b in ex)
put(f'{L}-explore2',sec(f'{L}-explore2','15–25 MIN',body,'Minutes 15 to 25. Let pairs keep working, then gather them to answer. Answers: 1) x = −150 (100 − 250: from 100 back to 0 is 100, then 150 more). 2) −13 (5, then 2, −1, −4, −7, −10, −13: six jumps of 3 down). Many predict −12 or −18: ask them to count the jumps on a number line. 3) Change it by a negative number: "change temp by −3" moves it 3 to the left. Adding a negative is the same as taking away.'))

# ---------- 6 teach1: order ----------
body=h2('The number line: right is bigger')+card(p('Numbers get bigger as you go right and smaller as you go left. Below zero, the further left, the colder.',38,700))
body+=pin(128,440,1664,numline_svg(-10,10,1664,170,label='Number line from minus 10 to 10'),None)
body+=pin(128,440,1664,numline_svg(-10,10,1664,170,marks=[(-6,'−6',SKY),(-1,'−1',SKY),(3,'3',YEL)],only=True,label='Points at minus 6, minus 1 and 3'),'fade')
body+=step(1,'−6 is further left than −1, so −6 &lt; −1. (Think: −6 °C is colder.)',top=640,size=36)
body+=step(2,'Which is colder, −2 °C or −8 °C? −8 is further left, so −8 °C is colder.',top=750,size=36)
put(f'{L}-teach1',sec(f'{L}-teach1','25–27 MIN',body,'Teach. Click 1: the three points. Ask: "Which is biggest? Which is smallest?" Then the steps. Think-aloud: "Six is bigger than one, but MINUS 6 is further below zero than minus 1. If I owe you $6, I am poorer than if I owe you $1." Use the signs: < means "is less than", pointing at the smaller number. Common slip: ordering by the digits only.'))

# ---------- 7 we1: up and down ----------
body=h2('Worked example: up and down the line')+card(p('It is −4 °C at 6 a.m. It rises 9 degrees by noon. Then it falls 7 degrees by night.',38,700))
body+=pin(128,410,1664,numline_svg(-8,8,1664,230,label='Number line from minus 8 to 8',ly=160),None)
body+=pin(128,410,1664,numline_svg(-8,8,1664,230,jumps=[(-4,5,'+9',TEAL)],only=True,label='Jump of plus 9 from minus 4 to 5',ly=160),'fade')
body+=pin(128,410,1664,numline_svg(-8,8,1664,230,jumps=[(5,-2,'−7',RED,55)],only=True,label='Jump of minus 7 from 5 to minus 2',ly=160),'fade')
body+=step(1,'Rise 9: from −4, 4 up to 0, then 5 more. Noon: 5 °C.   (−4 + 9 = 5)',top=670,size=34)
body+=step(2,'Fall 7: from 5, 5 down to 0, then 2 more. Night: −2 °C.   (5 − 7 = −2)',top=780,size=34)
put(f'{L}-we1',sec(f'{L}-we1','27–29 MIN',body,'Click order: the +9 jump, the −7 jump, step 1, step 2. Ask before each jump: "Which way do we move? Where do we cross zero?" Think-aloud: "Rising means moving right. From −4 it takes 4 to reach 0. I still have 5 of my 9 left, so I land on 5. Falling means moving left: 5 to get down to 0, 2 more to −2." Splitting the jump at 0 is the key move.'))

# ---------- 8 try1 ----------
put(f'{L}-try1',try_slide(f'{L}-try1','29–30 MIN','Your turn: draw the jumps','Sketch a number line on your whiteboard. Split each jump at 0.',[('a','−6 + 10','4'),('b','3 − 8','−5'),('c','−2 − 6','−8')],'Whiteboards. a) 6 up to 0, then 4 more: 4.  b) 3 down to 0, then 5 more: −5.  c) Already below zero, keep going left 6: −8. Children who write 8 or −4 for c have moved the wrong way: "Take away means move left."',size=40))

# ---------- 9 teach2: adding a negative ----------
body=h2('Adding a negative moves left')+card(p('In code we write "change temp by −4". That ADDS −4. It moves the number 4 to the LEFT.',38,700))
body+=pin(128,420,820,blocks_svg([(0,'var','set temp to [1]'),(0,'var','change temp by [−4]'),(0,'looks','say [temp]')],34,'set temp to 1, change temp by minus 4, say temp'),None)
body+=pin(1000,420,792,numline_svg(-5,3,792,200,jumps=[(1,-3,'+ (−4)',RED)],label='Jump from 1 to minus 3',ly=140,fs=28),'fade')
body+=step(1,'1 + (−4) is the same as 1 − 4.  Both land on −3.',top=690,size=36)
body+=pin(128,800,1664,p('Adding a negative = taking away.   7 + (−2) = 7 − 2 = 5',36,700),'fade',SOFT,20,'18px 28px')
put(f'{L}-teach2',sec(f'{L}-teach2','30–31 MIN',body,'Teach. Point at the red "change temp by −4" block from explore. "We are adding, but we are adding a negative, so we move left." Click: the jump, step 1, the summary. Ask: "What will the sprite say?" (−3). Brackets: we write 1 + (−4) so the two signs do not crash into each other.'))

# ---------- 10 we2: subtracting = the jump ----------
body=h2('Subtracting: the jump from b to a')+card(p('How much warmer is 7 °C than −3 °C?   That is 7 − (−3).',38,700))
body+=pin(128,400,1664,numline_svg(-5,9,1664,220,label='Number line from minus 5 to 9',ly=150),None)
body+=pin(128,400,1664,numline_svg(-5,9,1664,220,marks=[(-3,'',SKY),(7,'',YEL)],jumps=[(-3,0,'3',TEAL),(0,7,'7',TEAL)],only=True,label='Jumps from minus 3 to 0 and 0 to 7',ly=150),'fade')
body+=step(1,'a − b asks: how far is it from b to a? Start at −3, finish at 7.',top=640,size=34)
body+=step(2,'−3 up to 0 is 3. 0 up to 7 is 7. That is 10 steps to the RIGHT, so the answer is +10.',top=750,size=34)
body+=answer(128,860,1664,'7 − (−3) = 10.   Check: −3 + 10 = 7 ✓')
put(f'{L}-we2',sec(f'{L}-we2','31–33 MIN',body,'Click order: the jumps, step 1, step 2, the answer. Think-aloud: "Subtraction finds the difference. 10 − 4 = 6 because from 4 to 10 is 6. The same works below zero: from −3 to 7 is 10." Right means a positive answer, left means a negative answer: 2 − 5 is the jump from 5 to 2, 3 steps LEFT, so −3. Second example if time: −2 − (−8) is the jump from −8 to −2: 6 right, so 6. Do NOT teach "two minuses make a plus" as a rule today; let them see it.'))

# ---------- 11 try2 ----------
put(f'{L}-try2',try_slide(f'{L}-try2','33–34 MIN','Your turn: add and take away negatives','Adding a negative: move left. a − b: the jump from b to a.',[('a','3 + (−7)','−4'),('b','6 − (−2)','8'),('c','−5 − (−9)','4')],'Whiteboards. a) Move 7 left from 3: −4.  b) From −2 to 6: 2 + 6 = 8 steps right, so 8.  c) From −9 to −5: 4 steps right, so 4. Check each by adding back: −2 + 8 = 6, −9 + 4 = −5.',size=40))

# ---------- 12 key ----------
body=h2('Key idea: move along the number line')+card(p('Right is bigger. Adding a positive moves right. Adding a negative moves left. a − b is the jump from b to a.',44,700))+card(p('In code, "change by −3" makes a variable go down by 3.',38,600,MUTED))
put(f'{L}-key',sec(f'{L}-key','34–35 MIN',body,'Say the key idea together. Common mistakes to watch for during the worksheet: (1) Ordering negatives by their digits (saying −9 > −4). (2) Crossing zero wrongly: 3 − 8 answered as 5 or −11 (split the jump at 0). (3) In code, using "change by 1" when the variable should go down, or counting the start value as one of the repeats when tracing.'))

# ---------- 13 break ----------
put(f'{L}-break',break_slide(f'{L}-break','Brain break','Human lift. Standing tall is floor 0. Up 1: reach higher. Down 1: bend lower. Moves: up 3, down 5, down 2, up 6. Call out your floor after each move.','Then: a drink of water and back to the computer.','Five minutes. Floors after each move: 3, −2, −4, 2. Online: children stay in view of the camera and move in place.'))

# ---------- 14 ws1 ----------
put(f'{L}-ws1',ws_preview(f'{L}-ws1','40–52 MIN','Worksheet page 1: with your partner',[('Q1','Read the number line, put numbers in order, and use < or >.'),('Q2','Harbin temperatures: rises, falls and the gap to Singapore.'),('Q3','Sea level: heights above and below 0 m.')],'Stuck? Draw a number line and split every jump at 0.','Minutes 40 to 52. Paper only for page 1 (laptops closed or turned away). Walk around (online: visit breakout rooms). Ask "Which way did you move? Where did you cross zero?" before giving help.'))

# ---------- 15 ws1ans ----------
rows=[('Q1','a) A −8, B −3, C 4    b) −12, −5, −1, 0, 3, 7    c) >,  <,  <'),('Q2','a) 3 p.m. (−11 °C)  b) 11 degrees  c) 9 degrees  d) −25 °C  e) 44 degrees'),('Q3','a) 15 m    b) 9 m    c) −13 m')]
put(f'{L}-ws1ans',sec(f'{L}-ws1ans','52–54 MIN',h2('Page 1: check together')+ans_rows(rows,size=34),'Click each answer after a pair explains theirs. Q1c: −4 > −9 because −4 is further right (warmer). Q2b: −24 up to −13 is 11. Q2e: 13 up to 0, then 31 more: 44. Q3a: from −6 up to 9 is 6 + 9 = 15 m. Q3c: −6 + 4 = −2, then −2 − 11 = −13 m.'))

# ---------- 16 teach trace ----------
body=h2('Trace the code in a table')
body+=pin(128,240,700,blocks_svg([(0,'event','when flag clicked'),(0,'motion','set x to [20]'),(0,'control','repeat [3]'),(1,'motion','change x by [−15]'),(0,'looks','say [x position]')],32,'set x to 20, repeat 3: change x by minus 15, then say x position'),None)
W=[300,300]
body+=trow(1000,240,['After repeat','x'],W,None,True)
body+=trow(1000,320,['start','20'],W,None)
for i,(r,v) in enumerate([('1','5'),('2','−10'),('3','−25')]): body+=trow(1000,400+i*80,[r,v],W,'rise')
body+=pin(128,690,1664,p('Write one row each time the loop runs. Then read the last row: the sprite says −25.',36,700),'fade',SOFT,20,'20px 28px')
put(f'{L}-teachtrace',sec(f'{L}-teachtrace','54–56 MIN',body,'Teach before worksheet page 2 (Q5 traces a program). Click to fill each row while the children call out the value: 20 − 15 = 5, 5 − 15 = −10, −10 − 15 = −25. Point out: the "start" row is not one of the repeats. The "say" block is outside the loop, so it only speaks once, at the end. Optional Python version of this trace: x = 20 | for i in range(3): x = x - 15 | print(x)  (prints -25).'))

# ---------- 17 teach bug ----------
body=h2('Find the bug')+card(p('Ravi wants a countdown that says 3, 2, 1, 0, −1. His code says 3, 4, 5, 6, 7.',38,700))
body+=pin(128,400,760,blocks_svg([(0,'event','when flag clicked'),(0,'var','set n to [3]'),(0,'control','repeat [5]'),(1,'looks','say [n] for [1] seconds'),(1,'var','change n by [1]')],32,'Ravi\'s code: set n to 3, repeat 5: say n, change n by 1'),None)
body+=step(1,'Read each block. Which one makes n go UP?',left=960,top=400,width=772,size=34)
body+=step(2,'Fix it: change n by −1. Now n goes 3, 2, 1, 0, −1 ✓',left=960,top=530,width=772,size=34)
body+=step(3,'Test it: run the code and check the last number.',left=960,top=680,width=772,size=34)
put(f'{L}-teachbug',sec(f'{L}-teachbug','56–57 MIN',body,'Teach before worksheet page 2 (Q6 has a lift bug and Q7 asks them to plan code). Ask first: "Which block is wrong? How do you know?" Only one block needs to change. Show that 5 repeats are still right: 3, 2, 1, 0, −1 is five numbers. Planning tip for Q7: write the start value, how many repeats, and the change each time.'))

# ---------- 18 ws2 ----------
put(f'{L}-ws2',ws_preview(f'{L}-ws2','57–67 MIN','Worksheet page 2: on your own',[('Q4','Six calculations. Draw the jumps.'),('Q5','Trace the sprite code in the table.'),('Q6','The lift bug: predict, fix, predict again.'),('Q7','Plan the diver\'s code. Then build it in Scratch to test.')],'Finished early? Build Q5 to Q7 in Scratch, or try the Python box.','Children work alone. Paper first, then they may build Q5 to Q7 in Scratch to test their answers. Note who needs a short catch-up next lesson.'))

# ---------- 19 ws2ans ----------
rows=[('Q4','a) 3   b) −7   c) −8   d) −8   e) 8   f) 6'),('Q5','10, −20, −50, −80. It says −80.   b) 4 more repeats'),('Q6','a) 13   b) change floor by −1   c) −3 (B3)'),('Q7','set depth to 0, repeat 7, change depth by −4.   b) 28')]
put(f'{L}-ws2ans',sec(f'{L}-ws2ans','67–70 MIN',h2('Page 2: check together')+ans_rows(rows,size=34),'Click each answer after a child explains. Q4e: from −3 to 5 is 8 steps right. Q4f: from −7 to −1 is 6 steps right. Q5b: −80 to −200 is 120 more, and 120 ÷ 30 = 4. Q6a: 5 + 8 = 13 (the lift goes UP to floor 13). Q6c: 5 − 8 = −3, the third basement. Q7: 7 × 4 = 28, so 7 repeats reach −28; to come back up in one block, change depth by 28.'))

# ---------- 20 stretch (new) ----------
st=[('1.','At 6 a.m. it was −4 °C. By 2 p.m. it was 7 °C. By 10 p.m. it had fallen 9 degrees. How much did it rise by 2 p.m.? What was it at 10 p.m.?'),('2.','set n to 10, then repeat 5 times: change n by −4. Then say n. What does it say?'),('3.','What number is exactly halfway between −9 and 3?')]
put(f'{L}-stretch',sec(f'{L}-stretch','For early finishers',h2('Stretch')+''.join(card_q(a,b,36) for a,b in st),'Answers: 1) It rose 11 degrees (4 up to 0, then 7). At 10 p.m.: 7 − 9 = −2 °C.  2) −10 (10 − 4 × 5 = 10 − 20 = −10).  3) −3: the gap is 12, half is 6, and −9 + 6 = −3 (check: 3 − 6 = −3).'))

# ---------- 21 challenge ----------
ch=[('1.','Put −4, −3, −2, −1, 0, 1, 2, 3, 4 in a 3 by 3 grid so that every row, every column and both diagonals add up to 0.'),('2.','At midnight it was −6 °C. It rose 2 degrees every hour until 7 a.m., then 3 degrees every hour. What was the temperature at 10 a.m.?')]
put(f'{L}-challenge',sec(f'{L}-challenge','Challenge',h2('Challenge')+''.join(card_q(a,b,38) for a,b in ch),'Pairs try first, then the "see it" slide if stuck, then the walk-through. Answers: 1) One answer: top row −3, 2, 1; middle row 4, 0, −4; bottom row −1, −2, 3 (0 must be in the middle; there are 8 answers, all turns and flips of this one).  2) 17 °C: midnight to 7 a.m. is 7 hours, −6 + 14 = 8 °C; 7 a.m. to 10 a.m. is 3 hours, 8 + 9 = 17 °C.'))

# ---------- 22 chdiag ----------
grid='<svg aria-label="An empty 3 by 3 grid with the nine number tiles minus 4 to 4" viewBox="0 0 760 470" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;display:block">'
for r in range(3):
    for c in range(3): grid+=f'<rect x="{40+c*110}" y="{30+r*110}" width="110" height="110" fill="{WHITE}" stroke="{NAVY}" stroke-width="4"/>'
grid+=f'<text x="205" y="400" font-size="30" font-weight="700" text-anchor="middle" fill="{TEAL}" font-family="Arial">each line: 0</text>'
for i,v in enumerate(range(-4,5)):
    x=430+(i%3)*105; y=40+(i//3)*105
    grid+=f'<rect x="{x}" y="{y}" width="88" height="88" rx="14" fill="{SKY if v<0 else (YEL if v>0 else WHITE)}" stroke="{NAVY}" stroke-width="3"/><text x="{x+44}" y="{y+58}" font-size="40" font-weight="800" text-anchor="middle" fill="{NAVY}" font-family="Arial">{N(v)}</text>'
grid+=f'<text x="590" y="400" font-size="28" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="Arial">Where does 0 go?</text></svg>'
tl='<svg aria-label="A time line from midnight to 10 a.m.: plus 2 each hour until 7 a.m., then plus 3 each hour" viewBox="0 0 760 470" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;display:block">'
for h in range(11):
    x=50+h*66; tl+=f'<line x1="{x}" y1="210" x2="{x}" y2="240" stroke="{NAVY}" stroke-width="3"/>'
    if h in (0,7,10): tl+=f'<text x="{x}" y="285" font-size="28" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="Arial">{["12 a.m.","","","","","","","7 a.m.","","","10 a.m."][h]}</text>'
tl+=f'<line x1="50" y1="225" x2="710" y2="225" stroke="{NAVY}" stroke-width="4"/>'
for h in range(10):
    x=50+h*66; col=TEAL if h<7 else RED
    tl+=f'<path d="M{x+4} 205 Q{x+33} 165 {x+62} 205" fill="none" stroke="{col}" stroke-width="4"/>'
tl+=f'<text x="260" y="140" font-size="30" font-weight="800" text-anchor="middle" fill="{TEAL}" font-family="Arial">+2 each hour</text><text x="610" y="140" font-size="30" font-weight="800" text-anchor="middle" fill="{RED}" font-family="Arial">+3 each hour</text>'
tl+=f'<rect x="20" y="20" width="200" height="70" rx="14" fill="{SKY}" stroke="{NAVY}" stroke-width="3"/><text x="120" y="66" font-size="32" font-weight="800" text-anchor="middle" fill="{NAVY}" font-family="Arial">−6 °C</text>'
tl+=f'<rect x="600" y="330" width="150" height="70" rx="14" fill="{YEL}" stroke="{NAVY}" stroke-width="3"/><text x="675" y="377" font-size="36" font-weight="800" text-anchor="middle" fill="{NAVY}" font-family="Arial">?</text>'
tl+=f'<text x="300" y="380" font-size="28" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="Arial">How many hours of each kind?</text></svg>'
body=h2('Challenge: see it',60)+'<div style="display:flex;gap:32px;align-items:flex-start">'+card(f'<p style="font-size:28px;font-weight:700;color:{TEAL}">Q1: Zero magic square</p>'+grid,extra='flex:1;min-width:0;padding:20px 24px')+card(f'<p style="font-size:28px;font-weight:700;color:{TEAL}">Q2: The warming morning</p>'+tl,extra='flex:1;min-width:0;padding:20px 24px')+'</div>'
put(f'{L}-chdiag',sec(f'{L}-chdiag','Challenge',body,'Show after pairs have tried, or if they are stuck. The pictures show the problem, not the answer. Ask: What do you notice? Which pairs of tiles add to 0? Where must 0 go? For Q2: count the hops of each colour before adding anything.'))

# ---------- 23 chwalk ----------
body=h2('Challenge: walk-through')+pin(128,250,800,p('Q1: zero magic square',38,800,TEAL))
for i,t in enumerate(['A line through the middle pairs opposites: 3 and −3, so 0 goes in the middle.','4 can not go in a corner (a corner needs 3 pairs that make −4; there are only 2).','Put 4 and −4 in the middle of the left and right sides. Fill the rest: −3 2 1 / 4 0 −4 / −1 −2 3']): body+=pin(128,330+i*175,800,p(t,30),'rise',WHITE)
body+=pin(992,250,800,p('Q2: two kinds of hop',38,800,TEAL))
for i,t in enumerate(['Midnight to 7 a.m.: 7 hops of +2 = +14.','−6 + 14 = 8 °C at 7 a.m. (6 up to 0, then 8 more).','7 a.m. to 10 a.m.: 3 hops of +3 = +9.  8 + 9 = 17 °C ✓']): body+=pin(992,330+i*150,800,p(t,32),'rise',WHITE)
put(f'{L}-chwalk',sec(f'{L}-chwalk','Challenge',body,'Use after pairs have tried. Q1: check every line of the finished square aloud: rows −3 + 2 + 1, 4 + 0 − 4, −1 − 2 + 3; columns −3 + 4 − 1, 2 + 0 − 2, 1 − 4 + 3; diagonals −3 + 0 + 3, 1 + 0 − 1. All 0. Why 4 is not in a corner: the two numbers with it must make −4, and only −4 with 0 or −3 with −1 do that, but a corner is in three lines. Q2: a common mistake is 10 hops of +2 (−6 + 20 = 14). Code idea: set t to −6, repeat 7 change t by 2, repeat 3 change t by 3, say t.'))

# ---------- 24 talk ----------
body=h2('Talk time')+card(chip('TALK TIME',YEL,NAVY)+p('Ben says −8 is bigger than −3 because 8 is bigger than 3. Is he right? Use a thermometer or a lift to explain.',42,600))+card(p('Sentence starters:',34,400,MUTED)+p('“I noticed that …”   “I tested it by …”   “I know because …”',38,600))
put(f'{L}-talk',sec(f'{L}-talk','70–80 MIN',body,'Minutes 70 to 80. Pairs talk for 2 minutes, then share. Answer: No. −8 is further left on the number line, so it is smaller: −8 °C is colder than −3 °C, and floor −8 is lower than floor −3. The digits 8 and 3 tell us how FAR from 0, not which side. Praise reasons that use a picture or a real example. Second question if time: "Why does change by −3 make a number go down?"'))

# ---------- 25 exit ----------
body=h2('Exit ticket')+card(chip('EXIT TICKET')+p('It is −3 °C. The temperature falls 6 degrees, then rises 4 degrees. What is the temperature now?',46,600))+card(p('Write your answer on a slip of paper. Show it to your tutor. Then collect your stamp in your inquiry journal.',34,400))
put(f'{L}-exit',sec(f'{L}-exit','80–90 MIN',body,'Minutes 80 to 90. Answer: −5 °C (−3 − 6 = −9, then −9 + 4 = −5). Extension: write a Scratch program that starts temp at −3 and shows each change, then try it.'))

order=['title','warm1','warm2','explore1','explore2','teach1','we1','try1','teach2','we2','try2','key','break','ws1','ws1ans','teachtrace','teachbug','ws2','ws2ans','stretch','challenge','chdiag','chwalk','talk','exit']
order=[f'{L}-{x}' for x in order]
assert set(order)==set(S), set(order)^set(S)
for f in os.listdir(os.path.join(D,'slides')):
    if f.endswith('.html') and f[:-5] not in S: os.remove(os.path.join(D,'slides',f))
for i,h in S.items(): open(os.path.join(D,'slides',i+'.html'),'w').write(h)
deck={'v':4,'createdOnFiles':{'v':1,'at':datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')},'lists':'css',
 'title':'Math Inquirers P6: Lesson 3 – Below Zero','order':order,'cover':order[0],
 'sections':{'s1':{'description':'Warm-up and explore','start':f'{L}-title'},'s2':{'description':'Teach: moving along the number line','start':f'{L}-teach1'},'s3':{'description':'Worksheet with teaching before each page','start':f'{L}-break'},'s4':{'description':'Stretch, challenge, talk and exit','start':f'{L}-stretch'}},
 'faces':{'fredoka':{'family':'Fredoka','href':'https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&display=swap'},'nunito-sans':{'family':'Nunito Sans','href':'https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@400;600;700&display=swap'}},
 'designSystems':[]}
json.dump(deck,open(os.path.join(D,'deck.json'),'w'),indent=1,ensure_ascii=False)
print(len(order),'slides')
