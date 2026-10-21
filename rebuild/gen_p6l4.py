"""Math Inquirers P6, Lesson 4: Algebra Machines (expressions and simple equations; input, rule, output). Writes split/p6l4/project."""
import json,os,re,sys,datetime
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,H)
import slidekit
from slidekit import *
slidekit.FOOT='Math Inquirers P6  •  Notice it. Test it. Explain why.'
RED='#D64545'
L='p6l4'
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

PY_MAIN='n = int(input("IN? "))\nout = n * 3 + 2\nprint("OUT:", out)'
PY_NOTE='Optional Python version (same machine, for children who know Python): '+' | '.join(PY_MAIN.split('\n'))+'   Typing 4 prints OUT: 14; typing 10 prints OUT: 32.'
MACH=[(0,'event','when flag clicked'),(0,'looks','ask [IN?] and wait'),(0,'var','set out to [(answer * 3) + 2]'),(0,'looks','say [out]')]

# ---------- 1 title ----------
put(f'{L}-title',title_slide(f'{L}-title',4,2,'Algebra Machines','Expressions and equations  •  Code: input, rule, output',
 'Find a machine’s rule and write it with a letter, run machines backwards to solve equations, and build a machine in code.',
 'Objective: Find the rule of a function machine from a table and write it with a letter (OUT = 3n + 2); see that the order of steps matters and use brackets; solve simple equations by running the machine backwards (undo the last step first) and check forwards; build an input-rule-output program and use a search loop to test an answer. '
 'Materials: laptop or desktop with Scratch 3 (scratch.mit.edu), mini whiteboard and marker, workbook, pencil. Tutor: this deck, Scratch open for screen share. '
 'Online set-up: for the explore, children work in pairs in breakout rooms; one partner shares their screen with the machine running and types in the numbers the other partner calls out. Page 1 of the worksheet is paper only. '
 'Time plan: warm-up 0 to 10, explore at the computer 10 to 25, teaching 25 to 35 (click to reveal each step and answer), brain break 35 to 40, worksheet 40 to 70 with short teaching before each page and a check-together slide after it, talk time 70 to 80, exit ticket 80 to 90.'))

# ---------- 2 warm1: guess my rule ----------
rounds=[('Round A','3 → 8|7 → 12|20 → 25','add 5:   n + 5'),('Round B','2 → 10|5 → 25|9 → 45','times 5:   5n'),('Round C','2 → 3|6 → 11|10 → 19','× 2, then − 1:   2n − 1'),('Round D','1 → 5|4 → 14|10 → 32','× 3, then + 2:   3n + 2')]
body=h2('Warm-up: guess my rule')+p('I am a machine. Here is what came out. What is my rule?',34,600,MUTED)
for i,(r,pairs,a) in enumerate(rounds):
    Lf=128+(i%2)*848; T=300+(i//2)*290
    body+=pin(Lf,T,816,f'<p style="font-family:{HF};font-size:36px;font-weight:600;color:{TEAL}">{E(r)}</p><p style="font-size:42px;font-weight:800">{"&nbsp;&nbsp;&nbsp;&nbsp;".join(E(x) for x in pairs.split("|"))}</p>',None,WHITE,24,'18px 28px',f'box-sizing:border-box;height:250px;border:4px solid {NAVY};box-shadow:8px 8px 0 {NAVY}')
    body+=pin(Lf+24,T+150,768,f'<p style="font-size:36px;font-weight:800">{E(a)}</p>','pop',SOFT,16,'12px 20px',f'box-sizing:border-box;border:3px solid {NAVY}')
put(f'{L}-warm1',sec(f'{L}-warm1','0–5 MIN',body,
 'Minutes 0 to 5. Guess my rule. Play each round live first: children call out an IN number, you say the OUT (use the rule on the card), and they guess. Then click to show the rule. Ask: "Which IN numbers helped most?" '
 'Round C and D need two steps. Check the rule on EVERY pair: Round D, 1 × 3 + 2 = 5, 4 × 3 + 2 = 14, 10 × 3 + 2 = 32. Some children say "add 4" for 1 → 5: it fails at 4 → 14. '
 'Write each rule with the letter n: n + 5, 5n (5 × n, we leave out the × sign), 2n − 1, 3n + 2. Round D is the machine they will build in the explore.'))

# ---------- 3 warm2 ----------
qs=[('1.','n = 6. What is 4n?','24'),('2.','n = 6. What is n + 9?','15'),('3.','n = 6. What is 3n − 5?','13'),('4.','2n = 18. What is n?','9'),('5.','n = 6. What is (n + 4) × 2?','20')]
body=h2('Quick questions')+''.join(qrow(128,250+i*125,1250,a,b,36) for i,(a,b,c) in enumerate(qs))+''.join(answer(1420,250+i*125,372,c) for i,(a,b,c) in enumerate(qs))
put(f'{L}-warm2',sec(f'{L}-warm2','5–10 MIN',body,'Minutes 5 to 10. Whiteboards, then click. Answers: 1) 24 (4n means 4 × n).  2) 15.  3) 13 (multiply first: 18 − 5).  4) 9.  5) 20 (brackets first: 10 × 2). Watch for 4n read as "46" in question 1, and 3n − 5 worked as 3 × 1 = 3 or as 3 × (6 − 5) = 3 in question 3.'))

# ---------- 4 explore1 ----------
steps=['Build the machine on the right. (* means ×. Find "ask" in Sensing and the green blocks in Operators.)','Change the rule to your OWN secret two-step rule.','Share your screen. Your partner calls IN numbers; you type them in.','Your partner writes your rule with n. Fewest IN numbers wins. Then swap.']
left=card(chip('EXPLORE AT THE COMPUTER')+'<ol style="font-size:31px;font-weight:600;padding-left:44px;display:flex;flex-direction:column;gap:10px;line-height:1.3">'+''.join(f'<li>{E(s)}</li>' for s in steps)+'</ol>',extra='flex:1;min-width:0')
mpic=machine([('IN','q'),('× 3','op'),('+ 2','op'),('OUT','res')],w=700).replace('width:700px;height:130px','width:700px;height:130px;flex:none')
right=card(mpic+blocks_svg(MACH,28,'Machine program: when flag clicked, ask IN? and wait, set out to answer times 3 plus 2, say out'),extra='flex:none;width:780px;padding:24px 28px;gap:24px')
body=h2('Explore: build a secret machine')+f'<div style="display:flex;gap:32px;align-items:flex-start">{left}{right}</div>'
put(f'{L}-explore1',sec(f'{L}-explore1','10–15 MIN',body,
 'Minutes 10 to 15. Screen-share Scratch for 2 minutes and build the machine together: "ask" is in Sensing (light blue), "answer" is the round block under it, the * and + blocks are in Operators (green); put the * block INSIDE the + block. Make a variable called out. Type 4: it says 14. '
 'Then pairs go to breakout rooms. Each child changes the rule to a secret two-step rule (one × and one + or −), shares their screen, and types in the IN numbers the partner calls out. The partner tries to write the rule with n using as few IN numbers as possible. '
 'Early finishers: put the ask and say inside a "forever" loop so the machine keeps going; or make a three-step machine. '
 +PY_NOTE))

# ---------- 5 explore2 ----------
ex=[('1.','Which IN numbers were the most useful for cracking a rule? Why?'),('2.','How did you write your partner’s rule with n?'),('3.','My machine is × 3, then + 2. It says 20. How can you find the IN without trying lots of numbers?')]
body=h2('Explore: talk about it')+''.join(card_q(a,b,40) for a,b in ex)
put(f'{L}-explore2',sec(f'{L}-explore2','15–25 MIN',body,'Minutes 15 to 25. Let pairs keep working, then gather them. Answers: 1) Numbers in a row (1, 2, 3) show the × part: OUT goes up by the × number each time. IN 0 shows the + part straight away (0 × 3 + 2 = 2). 2) Times part first, then the add part: 3n + 2 means n × 3, then + 2. 3) Run it backwards: undo + 2 first (20 − 2 = 18), then undo × 3 (18 ÷ 3 = 6). Check: 6 × 3 + 2 = 20.'))

# ---------- 6 teach1: from a table to a rule ----------
W=[200,150,150,150,150]
body=h2('From a table to a rule')
body+=trow(128,240,['IN  n','1','2','3','4'],W,None,True)+trow(128,330,['OUT','7','11','15','19'],W,None)
body+=pin(1180,240,560,p('+4 each time',40,800,TEAL)+p('When IN goes up by 1, OUT goes up by 4.',32,600),'fade',SOFT,20,'20px 28px')
body+=step(1,'OUT goes up by 4 each time, so the rule has × 4 in it: 4n.',top=470,size=36)
body+=step(2,'Test: IN 1 gives 4 × 1 = 4. But OUT is 7, so add 3.',top=580,size=36)
body+=step(3,'Rule: OUT = 4n + 3.   Check IN 4: 4 × 4 + 3 = 19 ✓',top=690,size=36)
put(f'{L}-teach1',sec(f'{L}-teach1','25–27 MIN',body,'Teach. Click: the "+4 each time" note, then the steps. Think-aloud: "Every time n goes up by 1, OUT goes up by 4. That is what times 4 does: 4, 8, 12, 16. The 4-times table is 3 less than my OUT every time, so I add 3." Link to Lesson 1: this is the nth term idea. Always check the rule on a pair you did not use.'))

# ---------- 7 we1 ----------
W=[200,150,150,150]
body=h2('Worked example: gaps in the table')
body+=trow(128,240,['IN  n','2','5','10'],W,None,True)+trow(128,330,['OUT','3','12','27'],W,None)
body+=step(1,'IN goes up by 3 (2 to 5). OUT goes up by 9 (3 to 12). 9 ÷ 3 = 3, so × 3.',top=460,size=36)
body+=step(2,'Test: 3 × 2 = 6. OUT is 3, so take away 3.',top=570,size=36)
body+=step(3,'Rule: OUT = 3n − 3.   Check IN 10: 3 × 10 − 3 = 27 ✓',top=680,size=36)
put(f'{L}-we1',sec(f'{L}-we1','27–29 MIN',body,'Click through the steps. Ask before step 1: "The IN numbers jump. How can we still find the times part?" (share the OUT jump by the IN jump). Think-aloud: "IN went up 3, OUT went up 9, so each 1 in IN is worth 3 in OUT: times 3. 2 times 3 is 6, but OUT is 3, so take away 3." Check on the pair we did not use (10 → 27).'))

# ---------- 8 try1 ----------
put(f'{L}-try1',try_slide(f'{L}-try1','29–30 MIN','Your turn: find the rule','Write OUT = … with n. Check it on every pair.',[('a','IN 1, 2, 3  →  OUT 5, 7, 9','2n + 3'),('b','IN 1, 2, 3  →  OUT 2, 8, 14','6n − 4'),('c','IN 0, 1, 2  →  OUT 4, 11, 18','7n + 4')],'Whiteboards. a) up 2 each time, 2 × 1 = 2, need 5: + 3.  b) up 6, 6 × 1 = 6, need 2: − 4.  c) up 7; IN 0 gives the add part straight away: 4. Ask: "Why is IN 0 a helpful number?"',size=40))

# ---------- 9 teach2: order matters ----------
body=h2('Order matters: use brackets')
body+=pin(128,240,1100,machine([('n','q'),('+ 2','op'),('× 5','op'),('A','res')],w=1100),None)
body+=pin(128,400,1100,machine([('n','q'),('× 5','op'),('+ 2','op'),('B','res')],w=1100),None)
body+=pin(1280,240,512,p('IN 4:  (4 + 2) × 5 = 30',36,800),'fade',SOFT,20,'22px 26px')+pin(1280,400,512,p('IN 4:  4 × 5 + 2 = 22',36,800),'fade',SOFT,20,'22px 26px')
body+=step(1,'Same steps, different order, different OUT.',top=580,size=36)
body+=step(2,'A: OUT = (n + 2) × 5.  The brackets say “do this first”.',top=690,size=36)
body+=step(3,'B: OUT = 5n + 2.  Times comes before add, so no brackets are needed.',top=800,size=36)
put(f'{L}-teach2',sec(f'{L}-teach2','30–31 MIN',body,'Teach. Ask first: "Will both machines give the same OUT for IN 4?" Thumbs up or down, then click. Remind them of the order rule from primary school: brackets first, then × and ÷, then + and −. (n + 2) × 5 can also be written 5(n + 2). Do NOT say whether A and B can ever match: that is worksheet Q2(c).'))

# ---------- 10 we2: run it backwards ----------
body=h2('Run the machine backwards')+card(p('A machine does × 5, then − 4. OUT is 31. What was IN?    That is the equation 5n − 4 = 31.',38,700))
body+=pin(128,380,1664,machine([('n','q'),('× 5','op'),('− 4','op'),('31','res')],back='go back: + 4, then ÷ 5',w=1664),None)
body+=step(1,'Undo the LAST step first: the opposite of − 4 is + 4.   31 + 4 = 35',top=640,size=34)
body+=step(2,'Then undo × 5 with ÷ 5.   35 ÷ 5 = 7.   So n = 7.',top=740,size=34)
body+=answer(1180,830,612,'Check: 7 × 5 − 4 = 31 ✓')
put(f'{L}-we2',sec(f'{L}-we2','31–33 MIN',body,'Click through. Analogy: "You put on socks, then shoes. To undo, shoes come off first." Think-aloud: "The machine did times 5 and then took away 4. The last thing it did was take away 4, so I undo that first: 31 + 4 = 35. Then undo times 5: 35 ÷ 5 = 7. Check forwards: 7 × 5 = 35, 35 − 4 = 31." A second one if time: (n + 2) × 5 = 45: undo × 5 first (9), then − 2: n = 7.'))

# ---------- 11 try2 ----------
put(f'{L}-try2',try_slide(f'{L}-try2','33–34 MIN','Your turn: solve by going backwards','Draw the machine. Undo the last step first. Check forwards.',[('a','4n + 7 = 43','n = 9'),('b','(n − 2) × 6 = 54','n = 11'),('c','n ÷ 3 + 5 = 12','n = 21')],'Whiteboards. a) 43 − 7 = 36, 36 ÷ 4 = 9; check 4 × 9 + 7 = 43.  b) The brackets happen first, so × 6 is the LAST step: 54 ÷ 6 = 9, 9 + 2 = 11; check (11 − 2) × 6 = 54.  c) 12 − 5 = 7, 7 × 3 = 21; check 21 ÷ 3 + 5 = 12.',size=40))

# ---------- 12 key ----------
body=h2('Key idea: a rule is a machine')+card(p('A rule with a letter is a machine: OUT = 3n + 2 means × 3, then + 2. To find IN from OUT, run it backwards: undo the last step first.',42,700))+card(p('Check every answer by running the machine forwards.',38,600,MUTED))
put(f'{L}-key',sec(f'{L}-key','34–35 MIN',body,'Say the key idea together. Common mistakes to watch for during the worksheet: (1) Finding a rule from the first pair only (1 → 6 "add 5") without checking the others. (2) Undoing the steps in the wrong order, or doing the same step again instead of the opposite. (3) Reading 4n + 1 as "add 1 then times 4", or forgetting that brackets are done first.'))

# ---------- 13 break ----------
put(f'{L}-break',break_slide(f'{L}-break','Brain break','Jumping machine. Rule: double it, then take away 1. I call an IN number; you do that many OUT star jumps, counting aloud. IN 2, 3, 4, 5.','Then: a drink of water and back to the computer.','Five minutes. OUT jumps: 3, 5, 7, 9. Last round: "I did 11 jumps. What was my IN?" (6). Online: children stay in view of the camera and jump in place.'))

# ---------- 14 ws1 ----------
put(f'{L}-ws1',ws_preview(f'{L}-ws1','40–52 MIN','Worksheet page 1: with your partner',[('Q1','Guess my rule: three tables. Write each rule with n.'),('Q2','Two machines, same steps, different order.'),('Q3','Run machines backwards to find n. Check forwards.')],'Stuck? Look at how much OUT goes up each time IN goes up by 1.','Minutes 40 to 52. Paper only (laptops turned away). Walk around (online: visit breakout rooms). Ask "Did you check your rule on every pair?" and "Which step did you undo first?" before giving help.'))

# ---------- 15 ws1ans ----------
rows=[('Q1','a) 3n + 3, OUT 33    b) 5n − 2, IN 10    c) 4n − 3, OUT 77'),('Q2','a) P 32, Q 23   b) P = (n + 3) × 4,  Q = 4n + 3   c) No'),('Q3','a) 8    b) 10    c) 12    d) 24')]
put(f'{L}-ws1ans',sec(f'{L}-ws1ans','52–54 MIN',h2('Page 1: check together')+ans_rows(rows,size=34),'Click each answer after a pair explains. Q1c: IN goes up 1, OUT goes up 4, so × 4; 4 × 1 = 4, OUT 1, so − 3; IN 20: 80 − 3 = 77. Q2c: (n + 3) × 4 is 4n + 12, so P is always 9 more than Q (32 − 23 = 9 for IN 5): they can never match. Q3: a) 43 + 5 = 48, ÷ 6 = 8; b) 74 − 4 = 70, ÷ 7 = 10; c) 45 ÷ 5 = 9, + 3 = 12; d) 15 − 9 = 6, × 4 = 24.'))

# ---------- 16 teach code ----------
body=h2('Predict what the code says')
body+=pin(128,240,860,blocks_svg([(0,'event','when flag clicked'),(0,'looks','ask [IN?] and wait'),(0,'var','set out to [(answer * 4) − 1]'),(0,'looks','say [out]')],32,'when flag clicked, ask IN? and wait, set out to answer times 4 minus 1, say out'),None)
for i,(q,a) in enumerate([('You type 5. It says …','19'),('You type 0. It says …','−1'),('What do you type to get 35?','9  (35 + 1 = 36, 36 ÷ 4 = 9)')]):
    body+=qrow(128,520+i*120,980,'',q,34)+answer(1140,520+i*120,652,a)
put(f'{L}-teachcode',sec(f'{L}-teachcode','54–55 MIN',body,'Teach before worksheet page 2 (Q4). "answer" holds whatever was typed in. * means ×. The rule is OUT = 4n − 1. Ask: "Typing 0 gives a negative number. Where have we seen that before?" (Lesson 3). The last one is the machine run backwards. Python version: n = int(input("IN? ")) | out = n * 4 - 1 | print(out)  (typing 5 prints 19).'))

# ---------- 17 teach search ----------
body=h2('Let the computer search')+card(p('Solve 6n + 5 = 71 by trying n = 0, 1, 2, 3 … until it works.',38,700))
body+=pin(128,400,900,blocks_svg([(0,'event','when flag clicked'),(0,'var','set n to [0]'),(0,'control','repeat until [(n * 6) + 5 = 71]'),(1,'var','change n by [1]'),(0,'looks','say [n]')],32,'set n to 0, repeat until n times 6 plus 5 equals 71: change n by 1, then say n'),None)
body+=step(1,'n = 0 gives 5, n = 1 gives 11, n = 2 gives 17 … not 71 yet, keep going.',left=1020,top=400,width=712,size=32)
body+=step(2,'It stops when n = 11 (66 + 5 = 71) and says 11.',left=1020,top=560,width=712,size=32)
body+=step(3,'By hand, backwards: 71 − 5 = 66, 66 ÷ 6 = 11 ✓',left=1020,top=700,width=712,size=32)
put(f'{L}-teachsearch',sec(f'{L}-teachsearch','55–56 MIN',body,'Teach before worksheet page 2 (Q6 plans a search). "repeat until" is in Control; the = block is in Operators. The computer is not clever, it is fast: it tries every n. Our backwards method is clever: it goes straight there. Both give 11. Ask: "What happens if the equation has no whole-number answer, like 6n + 5 = 70?" (it never stops: press the red stop sign). Python version: n = 0 | while n * 6 + 5 != 71: n = n + 1 | print(n)  (prints 11).'))

# ---------- 18 teach trick ----------
body=h2('Why does the trick always work?')+card(p('Think of a number. Add 3. Double it. Take away 6. Halve it. You get your number back!',38,700))
for i,(a,b) in enumerate([('Think of a number','n'),('Add 3','n + 3'),('Double it','2n + 6'),('Take away 6','2n'),('Halve it','n')]):
    body+=pin(128,400+i*95,700,p(a,34,700),None,WHITE,16,'14px 24px',f'box-sizing:border-box;height:80px')+pin(860,400+i*95,520,p(b,38,800),'rise',SKY,16,'12px 24px',f'box-sizing:border-box;height:80px')
body+=pin(1420,400,372,p('Try 7: 10, 20, 14, 7 ✓',32,700),None,SOFT,16,'18px 22px')
put(f'{L}-teachtrick',sec(f'{L}-teachtrick','56–57 MIN',body,'Teach before worksheet page 2 (Q7). First try it with a number (7: 10, 20, 14, 7). Then click to build the n column. "Testing one number shows it works once; the letter shows it works for EVERY number." Doubling n + 3 doubles both parts: 2n + 6. This is the Secondary 1 idea of simplifying an expression.'))

# ---------- 19 ws2 ----------
put(f'{L}-ws2',ws_preview(f'{L}-ws2','57–67 MIN','Worksheet page 2: on your own',[('Q4','Predict what the machine code says.'),('Q5','Trace the loop in the table. Write its rule with n.'),('Q6','Plan a search for 8n − 5 = 91, then check backwards.'),('Q7','The number trick: try it, then use n to explain it.')],'Finished early? Build Q4 to Q6 in Scratch to test, or try the Python box.','Children work alone, paper first, then they may build Q4 to Q6 in Scratch to test. Note who needs a short catch-up next lesson.'))

# ---------- 20 ws2ans ----------
rows=[('Q4','a) 13    b) −1    c) 16'),('Q5','says 5, 9, 13, 17.   b) 4n + 1   c) 41'),('Q6','set n to 0, until (n * 8) − 5 = 91, change n by 1.  Says 12.'),('Q7','Always 3:  n + 5,  2n + 10,  2n + 6,  n + 3,  3')]
put(f'{L}-ws2ans',sec(f'{L}-ws2ans','67–70 MIN',h2('Page 2: check together')+ans_rows(rows,size=34),'Click after a child explains. Q4: OUT = 2n − 7; 2 × 3 − 7 = −1; backwards: 25 + 7 = 32, ÷ 2 = 16. Q5: n goes 1, 2, 3, 4 and then becomes 5 after the last repeat; with repeat 10 the last n is 10: 4 × 10 + 1 = 41. Q6: backwards 91 + 5 = 96, 96 ÷ 8 = 12. Q7: with 7: 12, 24, 20, 10, 3; with 10: 15, 30, 26, 13, 3. Halving 2n + 6 gives n + 3; taking away n leaves 3.'))

# ---------- 21 stretch (new) ----------
st=[('1.','IN 3 gives OUT 11. IN 7 gives OUT 23. The rule is "× a number, then + a number". Find it.'),('2.','set n to 2, then repeat 3 times: set n to (n × 2) + 1. Then say n. What does it say?'),('3.','Solve (n + 6) × 4 = 60.')]
put(f'{L}-stretch',sec(f'{L}-stretch','For early finishers',h2('Stretch')+''.join(card_q(a,b,38) for a,b in st),'Answers: 1) OUT = 3n + 2 (IN up 4, OUT up 12, so × 3; 3 × 3 = 9, + 2 = 11; check 3 × 7 + 2 = 23).  2) 23 (2 → 5 → 11 → 23).  3) n = 9 (60 ÷ 4 = 15, 15 − 6 = 9; check 15 × 4 = 60).'))

# ---------- 22 challenge ----------
ch=[('1.','A machine does × 3, then − 4. Which IN number comes out as the SAME number?'),('2.','Two machines are joined: the OUT of the first goes into the second. Each one does × 2, then + 1. IN 5 gives OUT 23. Which IN gives OUT 63?')]
put(f'{L}-challenge',sec(f'{L}-challenge','Challenge',h2('Challenge')+''.join(card_q(a,b,38) for a,b in ch),'Pairs try first, then the "see it" slide if stuck, then the walk-through. Answers: 1) 2 (2 × 3 − 4 = 2; the equation is 3n − 4 = n).  2) 15 (backwards through the second machine: 63 − 1 = 62, ÷ 2 = 31; then through the first: 31 − 1 = 30, ÷ 2 = 15. Check: 15 → 31 → 63).'))

# ---------- 23 chdiag ----------
def mini_machine(cells,label,w=760,h=130):
    return machine(cells,w=w).replace(f'width:{w}px;height:130px','width:100%;height:auto').replace('aria-label="Number machine"',f'aria-label="{E(label)}"')
q1=(mini_machine([('n','q'),('× 3','op'),('− 4','op'),('n','res')],'Machine: n, times 3, minus 4, gives the same n')+
    '<svg aria-label="A table to try IN numbers: IN 1, 2, 3, 4 with OUT left empty" viewBox="0 0 760 250" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto">'+
    ''.join(f'<rect x="{30+i*140}" y="20" width="140" height="70" fill="{YEL if i==0 else WHITE}" stroke="{NAVY}" stroke-width="3"/><text x="{100+i*140}" y="68" font-size="34" font-weight="800" text-anchor="middle" fill="{NAVY}" font-family="Arial">{t}</text>' for i,t in enumerate(['IN','1','2','3','4']))+
    ''.join(f'<rect x="{30+i*140}" y="90" width="140" height="70" fill="{YEL if i==0 else WHITE}" stroke="{NAVY}" stroke-width="3"/><text x="{100+i*140}" y="138" font-size="34" font-weight="800" text-anchor="middle" fill="{NAVY}" font-family="Arial">{t}</text>' for i,t in enumerate(['OUT','?','?','?','?']))+
    f'<text x="380" y="220" font-size="30" font-weight="700" text-anchor="middle" fill="{TEAL}" font-family="Arial">When is OUT the same as IN?</text></svg>')
q2=(f'<p style="font-size:26px;font-weight:700;color:{MUTED}">Machine 1</p>'+mini_machine([('?','q'),('× 2','op'),('+ 1','op'),('□','res')],'First machine: unknown IN, times 2, plus 1, gives the middle box')+f'<p style="font-size:26px;font-weight:700;color:{MUTED}">Machine 2</p>'+mini_machine([('□','q'),('× 2','op'),('+ 1','op'),('63','res')],'Second machine: the middle box, times 2, plus 1, gives 63')+
    f'<svg aria-label="IN 5 gives 11 in the middle and 23 at the end" viewBox="0 0 760 130" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto"><text x="380" y="40" font-size="32" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="Arial">Test: 5 → 11 → 23</text><rect x="160" y="60" width="440" height="66" rx="16" fill="{SKY}" stroke="{NAVY}" stroke-width="3"/><text x="380" y="104" font-size="32" font-weight="800" text-anchor="middle" fill="{NAVY}" font-family="Arial">Which way do we go?</text></svg>')
body=h2('Challenge: see it',60)+'<div style="display:flex;gap:32px;align-items:flex-start">'+card(f'<p style="font-size:28px;font-weight:700;color:{TEAL}">Q1: Same in, same out</p>'+q1,extra='flex:1;min-width:0;padding:20px 24px')+card(f'<p style="font-size:28px;font-weight:700;color:{TEAL}">Q2: Two machines joined</p>'+q2,extra='flex:1;min-width:0;padding:20px 24px')+'</div>'
put(f'{L}-chdiag',sec(f'{L}-chdiag','Challenge',body,'Show after pairs have tried, or if they are stuck. The pictures show the problem, not the answer. Ask: For Q1, fill in the table: is OUT catching up with IN? For Q2, what is in the middle box when OUT is 63?'))

# ---------- 24 chwalk ----------
body=h2('Challenge: walk-through')+pin(128,250,800,p('Q1: make a table',38,800,TEAL))
for i,t in enumerate(['IN 1 → OUT −1.   IN 2 → OUT 2 ✓   IN 3 → OUT 5.','OUT grows by 3 each time, IN by 1, so they meet only once.','With n: 3n − 4 = n. Take n from both sides: 2n − 4 = 0, so n = 2.']): body+=pin(128,330+i*165,800,p(t,32),'rise',WHITE)
body+=pin(992,250,800,p('Q2: go backwards twice',38,800,TEAL))
for i,t in enumerate(['Second machine backwards: 63 − 1 = 62, 62 ÷ 2 = 31.','First machine backwards: 31 − 1 = 30, 30 ÷ 2 = 15.','Check forwards: 15 → 31 → 63 ✓']): body+=pin(992,330+i*165,800,p(t,32),'rise',WHITE)
put(f'{L}-chwalk',sec(f'{L}-chwalk','Challenge',body,'Use after pairs have tried. Q1: the table is the computer-style search done by hand; the algebra line is for strong pupils only. Q2: the middle box is 31. Extra for fast pairs: the two joined machines are the same as one machine "× 4, then + 3" (5 → 23: 4 × 5 + 3 = 23; 15 → 63: 4 × 15 + 3 = 63). Why? (2n + 1) × 2 + 1 = 4n + 3.'))

# ---------- 25 talk ----------
body=h2('Talk time')+card(chip('TALK TIME',YEL,NAVY)+p('To solve 4n + 7 = 43, Ravi tries n = 1, 2, 3 … like the computer. Mei runs the machine backwards. Which way is better, and when?',40,600))+card(p('Sentence starters:',34,400,MUTED)+p('“I noticed that …”   “I tested it by …”   “I know because …”',38,600))
put(f'{L}-talk',sec(f'{L}-talk','70–80 MIN',body,'Minutes 70 to 80. Pairs talk for 2 minutes, then share. Both get n = 9. Backwards is quicker by hand and works for big numbers (4n + 7 = 4007 would take Ravi 1000 tries). Trying every n is easy to code and also works when there is no easy backwards step, like n × n + n = 90 (n = 9). But a search must stop: if there is no whole-number answer, it would run forever. Praise answers that say WHEN each is better.'))

# ---------- 26 exit ----------
body=h2('Exit ticket')+card(chip('EXIT TICKET')+p('A machine does × 4, then + 5.   (a) IN 6: what is OUT?   (b) OUT 45: what was IN?',46,600))+card(p('Write your answer on a slip of paper. Show it to your tutor. Then collect your stamp in your inquiry journal.',34,400))
put(f'{L}-exit',sec(f'{L}-exit','80–90 MIN',body,'Minutes 80 to 90. Answers: (a) 29 (6 × 4 + 5).  (b) 10 (45 − 5 = 40, 40 ÷ 4 = 10; check 10 × 4 + 5 = 45). Extension: write the rule with n (4n + 5) and build it in Scratch.'))

order=['title','warm1','warm2','explore1','explore2','teach1','we1','try1','teach2','we2','try2','key','break','ws1','ws1ans','teachcode','teachsearch','teachtrick','ws2','ws2ans','stretch','challenge','chdiag','chwalk','talk','exit']
order=[f'{L}-{x}' for x in order]
assert set(order)==set(S), set(order)^set(S)
for f in os.listdir(os.path.join(D,'slides')):
    if f.endswith('.html') and f[:-5] not in S: os.remove(os.path.join(D,'slides',f))
for i,h in S.items(): open(os.path.join(D,'slides',i+'.html'),'w').write(h)
deck={'v':4,'createdOnFiles':{'v':1,'at':datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')},'lists':'css',
 'title':'Math Inquirers P6: Lesson 4 – Algebra Machines','order':order,'cover':order[0],
 'sections':{'s1':{'description':'Warm-up and explore','start':f'{L}-title'},'s2':{'description':'Teach: rules with a letter, and running machines backwards','start':f'{L}-teach1'},'s3':{'description':'Worksheet with teaching before each page','start':f'{L}-break'},'s4':{'description':'Stretch, challenge, talk and exit','start':f'{L}-stretch'}},
 'faces':{'fredoka':{'family':'Fredoka','href':'https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&display=swap'},'nunito-sans':{'family':'Nunito Sans','href':'https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@400;600;700&display=swap'}},
 'designSystems':[]}
json.dump(deck,open(os.path.join(D,'deck.json'),'w'),indent=1,ensure_ascii=False)
print(len(order),'slides')
