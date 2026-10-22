"""Math Inquirers P6, Lesson 1: Code the Pattern. Writes split/p6l1/project (deck.json + slides/*.html)."""
import json,os,sys,re,datetime
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,H)
import slidekit
from slidekit import *
slidekit.FOOT='Math Inquirers P6  •  Notice it. Test it. Explain why.'
L='p6l1'
D=os.path.join(H,'..','split',L,'project'); os.makedirs(os.path.join(D,'slides'),exist_ok=True)
S={}
def put(i,h): S[i]=h
RED='#D64545'

# ---------- our own code-block drawing (simple coloured shapes, not Scratch artwork) ----------
BK={'hat':(YEL,NAVY),'var':(RED,WHITE),'look':(SKY,NAVY),'ctl':(TEAL,WHITE)}
def blocks(prog,fs=30,label='Code blocks',width=None):
    """prog items: (kind,text) or (kind,text,[children]) or (kind,text,[children],[else children]). '(x)' in text = white value slot."""
    Hh=round(fs*1.9); arm=round(fs*1.1); bot=round(fs*0.8); cw=fs*0.57; pp=fs*0.42; pad=fs*0.55; bh=round(fs*0.55)
    out=[]; mx=[0]
    parts=lambda t:[s for s in re.split(r'(\([^)]*\))',t) if s]
    def tw(t): return sum(((len(s)-2)*cw+2*pp) if s.startswith('(') else len(s)*cw for s in parts(t))
    def text(t,x,y,fg):
        cx=x+pad; s=''
        for seg in parts(t):
            if seg.startswith('('):
                inner=seg[1:-1]; w=max(len(inner)*cw+2*pp,fs*1.4)
                s+=f'<rect x="{cx:.0f}" y="{y+Hh*0.17:.0f}" width="{w:.0f}" height="{Hh*0.66:.0f}" rx="{Hh*0.33:.0f}" fill="{WHITE}" stroke="{NAVY}" stroke-width="2"/><text x="{cx+w/2:.0f}" y="{y+Hh/2+fs*0.35:.0f}" font-size="{fs}" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="Arial, sans-serif">{E(inner)}</text>'
                cx+=w
            else:
                s+=f'<text x="{cx:.0f}" y="{y+Hh/2+fs*0.35:.0f}" font-size="{fs}" font-weight="700" fill="{fg}" font-family="Arial, sans-serif" xml:space="preserve">{E(seg)}</text>'
                cx+=len(seg)*cw
        return s
    def measure(items,y):
        for it in items:
            if it[0]=='hat': y+=bh*1.5+Hh
            elif len(it)>2:
                for ch in [it[2]]+([it[3]] if len(it)>3 else []):
                    y+=Hh; c0=y; y=measure(ch,y)
                    if y==c0: y+=Hh*0.6
                y+=bot
            else: y+=Hh
        return y
    def walk(items,x,y):
        for it in items:
            k,t=it[0],it[1]; bg,fg=BK[k]; w=max(tw(t)+2*pad,fs*4)
            if k=='hat':
                y+=bh*1.5
                out.append(f'<path d="M{x} {y} C{x+fs*0.8} {y-bh*1.9} {x+fs*3.2} {y-bh*1.9} {x+fs*4} {y} L{x+w} {y} Q{x+w+8} {y} {x+w+8} {y+8} L{x+w+8} {y+Hh-8} Q{x+w+8} {y+Hh} {x+w} {y+Hh} L{x+8} {y+Hh} Q{x} {y+Hh} {x} {y+Hh-8} Z" fill="{bg}" stroke="{NAVY}" stroke-width="3" stroke-linejoin="round"/>')
                out.append(text(t,x,y,fg)); mx[0]=max(mx[0],x+w+8); y+=Hh; continue
            if len(it)>2:
                arms=[it[2]]+([it[3]] if len(it)>3 else []); labels=[t,'else']; segs=[]; yy=y
                for ch in arms:
                    top=yy; yy+=Hh; c0=yy; yy=measure(ch,yy)
                    if yy==c0: yy+=Hh*0.6
                    segs.append((top,c0,yy))
                endy=yy+bot; bw=fs*3.4
                d=f'M{x+8} {y} L{x+w-8} {y} Q{x+w} {y} {x+w} {y+8} L{x+w} {y+Hh-8} Q{x+w} {y+Hh} {x+w-8} {y+Hh} L{x+arm} {y+Hh} '
                for i,(top,c0,c1) in enumerate(segs):
                    if i>0:
                        wl=max(tw(labels[i])+2*pad,fs*4); d+=f'L{x+arm} {top} L{x+wl} {top} L{x+wl} {top+Hh} L{x+arm} {top+Hh} '
                    d+=f'L{x+arm} {c1} '
                d+=f'L{x+bw} {segs[-1][2]} L{x+bw} {endy-6} Q{x+bw} {endy} {x+bw-6} {endy} L{x+8} {endy} Q{x} {endy} {x} {endy-8} L{x} {y+8} Q{x} {y} {x+8} {y} Z'
                out.append(f'<path d="{d}" fill="{bg}" stroke="{NAVY}" stroke-width="3" stroke-linejoin="round"/>')
                out.append(text(t,x,y,fg)); mx[0]=max(mx[0],x+w)
                for i,(top,c0,c1) in enumerate(segs):
                    if i>0: out.append(text(labels[i],x,top,fg))
                    walk(arms[i],x+arm,c0)
                y=endy
            else:
                out.append(f'<rect x="{x}" y="{y}" width="{w:.0f}" height="{Hh}" rx="10" fill="{bg}" stroke="{NAVY}" stroke-width="3"/>')
                out.append(text(t,x,y,fg)); mx[0]=max(mx[0],x+w); y+=Hh
        return y
    yend=walk(prog,3,3); W=mx[0]+6; Ht=yend+6
    sc=(width/W) if width else 1
    return f'<svg aria-label="{E(label)}" viewBox="0 0 {W:.0f} {Ht:.0f}" xmlns="http://www.w3.org/2000/svg" style="width:{W*sc:.0f}px;height:{Ht*sc:.0f}px;flex:none">'+''.join(out)+'</svg>'
HAT=('hat','when green flag clicked')
def talkcard(n,t,size=40): return card(p(f'<span style="color:{TEAL}">{n}</span>  {E(t)}',size,600,raw=True))
def check(sid,time,title,rows,notes,top=250,gap=135,size=36,lw=150):
    body=h2(title)
    for i,(a,b) in enumerate(rows):
        tp=top+i*gap
        body+=pin(128,tp,lw-20,f'<p style="font-size:36px;font-weight:800;color:{TEAL}">{E(a)}</p>',None,WHITE,20,'18px 24px')
        body+=pin(128+lw,tp,1664-lw,f'<p style="font-size:{size}px;font-weight:800;line-height:1.25">{E(b)}</p>','pop',YEL,20,'18px 26px')
    return sec(sid,time,body,notes)

# ---------- title ----------
OBJ='Continue a sequence, find the rule for the nth term of a sequence with a constant difference, use it to find far terms such as the 100th, work backwards to decide whether a number is in a sequence, and test predictions with a loop and a variable in Scratch.'
MAT='Laptop or desktop with Scratch 3 open (scratch.mit.edu, no account needed), about 25 matchsticks or toothpicks per child (or squared paper), mini whiteboard, workbook. Optional: a Python editor for children who already know Python.'
ONL='The tutor shares the slides and a Scratch window. Share your Scratch window and build the four blocks together on screen; the blocks are also on the slide. Block colours on our slides are simplified; in Scratch, find blocks by the category name on the left, not by colour. Scratch is free at scratch.mit.edu and needs no account in class. Children hold paper up to the camera or share their screen when asked. Matchsticks can be drawn as lines.'
put(f'{L}-title',f'''<section id="{L}-title" data-transition="fade" style="background:{NAVY};color:{CREAM};font-family:{BF};padding:128px 128px 160px;display:flex;flex-direction:column;justify-content:center;gap:36px">
<p style="font-size:32px;font-weight:700;letter-spacing:4px;color:{YEL}">LESSON 1  •  WEEK 1  •  MATHS + CODE</p>
<h1 style="font-family:{HF};font-size:128px;font-weight:600;line-height:1.05">Code the Pattern</h1>
<p style="font-size:44px;color:#C9D4EC">Sequences and the nth term  •  loops and a variable</p>
<div style="background:#26385F;border-radius:24px;padding:40px;display:flex;flex-direction:column;gap:12px"><p style="font-size:28px;font-weight:700;letter-spacing:3px;color:{YEL}">TODAY WE WILL</p><p style="font-size:44px;font-weight:600">Find the rule for the nth term of a pattern, predict the 100th term, and test it with a loop in code.</p></div>
<p style="position:absolute;left:128px;bottom:64px;width:1400px;font-size:24px;color:#B7C3DD">{E(slidekit.FOOT)}</p>
<aside>{E(f"Objective: {OBJ} Materials: {MAT} Online: {ONL} Time plan: warm-up 0 to 10, explore 10 to 25 (matchsticks first, then Scratch), teaching 25 to 35 (click to reveal each step and answer), brain break 35 to 40, worksheet 40 to 75 with short teaching before each page and a check-together slide after it (page 1 is the maths, page 2 is the code), talk time 75 to 82, exit ticket 82 to 90. Python: the optional Python version of each program is in the notes of the code slides and in the workbook Python corner.")}</aside>
</section>
''')

# ---------- warm-up 1: pattern quick-fire ----------
cards=[('3, 7, 11, 15, …','19, 23  (add 4)'),('50, 44, 38, 32, …','26, 20  (take away 6)'),('1, 4, 9, 16, …','25, 36  (square numbers)'),
       ('2, 4, 8, 16, …','32, 64  (double)'),('1, 1, 2, 3, 5, …','8, 13  (add the last two)'),('0.5, 1.25, 2, 2.75, …','3.5, 4.25  (add 0.75)')]
body=h2('Warm-up: Next! Pattern quick-fire')+p('Type the next two terms in the chat. Say the rule if you spot it. No race, no points.',36,600,MUTED)
CW=533
for i,(a,b) in enumerate(cards):
    Lf=128+(i%3)*(CW+32); T=300+(i//3)*290
    body+=pin(Lf,T,CW,f'<p style="font-family:{HF};font-size:30px;font-weight:600;color:{TEAL}">Card {i+1}</p><p style="font-family:{HF};font-size:48px;font-weight:600">{E(a)}</p>',None,WHITE,24,'20px 28px',f'box-sizing:border-box;height:260px;border:4px solid {NAVY};box-shadow:8px 8px 0 {NAVY}')
    body+=pin(Lf+20,T+160,CW-40,f'<p style="font-size:32px;font-weight:800">{E(b)}</p>','pop',SOFT,16,'12px 18px',f'box-sizing:border-box;border:3px solid {NAVY}')
put(f'{L}-warm1',sec(f'{L}-warm1','0–5 MIN',body,'Minutes 5 to 8. Pairs (online: type in the chat). No racing, no points. Show one card at a time by pointing; click to reveal its answer (clicks go card 1 to card 6). Ask for the rule every time. Card 3 and card 5 are traps: the difference is NOT the same each time (square numbers go up by 3, 5, 7, 9; in card 5 each term is the sum of the two before, the Fibonacci numbers). Say: "Today we focus on the friendly kind, where the difference stays the same, like cards 1, 2 and 6." Card 6: 2.75 + 0.75 = 3.5, then 4.25.'))

# ---------- warm-up 2 ----------
qs=[('1.','4, 9, 14, 19, __','24'),('2.','The 10th term of 2, 4, 6, 8, …','20'),('3.','The 10th term of 3, 5, 7, 9, …','21'),('4.','Ali has $12 and saves $5 a week. How much after 6 weeks?','$42'),('5.','100, 93, 86, __','79')]
body=h2('Quick questions')+''.join(qrow(128,250+i*125,1250,a,b,36) for i,(a,b,c) in enumerate(qs))+''.join(answer(1420,250+i*125,372,c) for i,(a,b,c) in enumerate(qs))
put(f'{L}-warm2',sec(f'{L}-warm2','5–10 MIN',body,'Minutes 5 to 10. Whiteboards up together, then click to reveal. Q2 and Q3 are the seed of today: 2, 4, 6, 8 is the 2 times table, so the 10th term is 2 × 10 = 20. 3, 5, 7, 9 is always 1 more than the 2 times table, so the 10th term is 21. Ask: "How did you get Q3 without counting on?" Q4: 12 + 6 × 5 = 42 (6 weeks, 6 jumps of $5, because Ali starts with $12 before any saving). Q5: take away 7.'))

# ---------- explore ----------
def tri_svg(w=1000,h=250):
    s=60; g=''; x0=40
    def stick(a,b):
        (x1,y1),(x2,y2)=a,b; dx,dy=x2-x1,y2-y1; Lh=(dx*dx+dy*dy)**.5; ux,uy=dx/Lh,dy/Lh
        A=(x1+ux*6,y1+uy*6); B=(x2-ux*6,y2-uy*6)
        return f'<line x1="{A[0]:.0f}" y1="{A[1]:.0f}" x2="{B[0]:.0f}" y2="{B[1]:.0f}" stroke="{NAVY}" stroke-width="6" stroke-linecap="round"/><circle cx="{B[0]:.0f}" cy="{B[1]:.0f}" r="6" fill="{RED}"/>'
    for k in (1,2,3):
        yb,yt=110,110-52; Bp=lambda j:(x0+j*s,yb); Tp=lambda j:(x0+s/2+j*s,yt); E2=set()
        for i in range(k):
            tri=[Bp(i//2),Bp(i//2+1),Tp(i//2)] if i%2==0 else [Tp((i-1)//2),Tp((i+1)//2),Bp((i+1)//2)]
            for a,b in ((0,1),(1,2),(0,2)): E2.add(tuple(sorted((tri[a],tri[b]))))
        assert len(E2)==2*k+1
        g+=''.join(stick(a,b) for a,b in sorted(E2))
        wk=s*((k+1)//2)+(s/2 if k%2==0 else 0)
        g+=f'<text x="{x0+wk/2:.0f}" y="150" font-size="26" font-weight="700" text-anchor="middle" fill="{TEAL}" font-family="Nunito Sans, Arial">Pattern {k}</text>'
        x0+=wk+70
    # table
    tx=560; cols=['Pattern','1','2','3','10','100']; vals=['Sticks','3','5','7','?','?']
    for i,(c,v) in enumerate(zip(cols,vals)):
        cwid=130 if i==0 else 58; xx=tx+(0 if i==0 else 130+(i-1)*58)
        g+=f'<rect x="{xx}" y="40" width="{cwid}" height="50" fill="{YEL}" stroke="{NAVY}" stroke-width="3"/><text x="{xx+cwid/2}" y="74" font-size="24" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="Nunito Sans, Arial">{c}</text>'
        g+=f'<rect x="{xx}" y="90" width="{cwid}" height="50" fill="{WHITE}" stroke="{NAVY}" stroke-width="3"/><text x="{xx+cwid/2}" y="124" font-size="24" font-weight="700" text-anchor="middle" fill="{RED if v=="?" else NAVY}" font-family="Nunito Sans, Arial">{v}</text>'
    g+=f'<text x="{tx+210}" y="200" font-size="28" font-weight="700" text-anchor="middle" fill="{TEAL}" font-family="Nunito Sans, Arial">Predict. Then test in code.</text>'
    return f'<svg aria-label="Matchstick triangles: patterns 1, 2 and 3 use 3, 5 and 7 sticks; table with question marks for patterns 10 and 100" viewBox="0 0 1000 220" xmlns="http://www.w3.org/2000/svg" style="width:{w}px;height:{h}px;flex:none">{g}</svg>'
steps=['Build matchstick triangles in a row: pattern 1 has 1 triangle, pattern 2 has 2, pattern 3 has 3.','Count the sticks in each pattern. Make a table.','Predict the sticks in pattern 10 and in pattern 100. Do not build them!','Check pattern 10 in Scratch with a loop and a variable.']
inner=chip('EXPLORE')+'<ol style="font-size:32px;font-weight:600;padding-left:48px;margin:0;display:flex;flex-direction:column;gap:6px">'+''.join(f'<li>{E(s)}</li>' for s in steps)+'</ol>'
body=h2('Explore: what to do')+card(inner)+card(tri_svg(1450,320),extra='align-items:center;padding:12px 40px')
put(f'{L}-explore1',sec(f'{L}-explore1','10–15 MIN',body,'Minutes 10 to 15. Pairs build with matchsticks (online: draw the sticks as lines). Insist on a written prediction for pattern 100 BEFORE anyone opens Scratch. Then Scratch: make a variable called sticks; blocks: when green flag clicked, set sticks to 3, repeat 9, change sticks by 2, say sticks. It says 21 (pattern 10). Ask: "Why repeat 9 and not 10?" Python (optional, for children who know it): sticks = 3, then for i in range(9): sticks = sticks + 2, then print(sticks). Prints 21.'))
body=h2('Explore: talk about it')+talkcard('1.','How many sticks are in pattern 10?')+talkcard('2.','How many in pattern 100? How did you get it without building it?')+talkcard('3.','Which pattern uses exactly 75 sticks?')
put(f'{L}-explore2',sec(f'{L}-explore2','15–25 MIN',body,'Minutes 15 to 25. Pairs keep working, then gather. Answers: 1) 21. 2) 201: each new triangle adds 2 sticks, so 3 + 2 × 99 = 201; or "2 sticks per triangle plus 1 extra", 2 × 100 + 1 = 201. Both are right: celebrate both methods. 3) Pattern 37: work backwards, 75 − 1 = 74, 74 ÷ 2 = 37. Ask who checked pattern 100 in Scratch with repeat 99.'))

# ---------- teach ----------
W6=[190,118,118,118,118,118]
body=h2('Two kinds of rule')+card(p('7, 9, 11, 13, 15, …',48,700))
body+=trow(128,400,['n','1','2','3','4','5'],W6,None,True)
body+=trow(128,490,['term','7','9','11','13','15'],W6,None)
body+=trow(128,580,['2 × n','2','4','6','8','10'],W6,'rise')
body+=pin(1180,400,612,p('Term-to-term rule: add 2. Good for the NEXT term.',34,700),None,WHITE,20,'22px 26px')
body+=pin(1180,540,612,p('The difference is 2, so compare with the 2 times table. Each term is 5 more.',34,700),'fade',SOFT,20,'22px 26px')
body+=pin(128,750,1664,p('Rule for the nth term:  2 × n + 5,  written  2n + 5.   Good for ANY term: the 50th is 2 × 50 + 5 = 105.',36,800),'fade',YEL,20,'20px 30px')
put(f'{L}-teach1',sec(f'{L}-teach1','25–27 MIN',body,'Teach. n means the position (1st, 2nd, 3rd …). Think-aloud: "Add 2 each time. That gets me the next term, but for the 50th I would add 2 forty-nine times. The difference is 2, so I write the 2 times table underneath (click). Every term is 5 more than the 2 times-table number (click). So the term in position n is 2 × n + 5. In algebra we write 2n + 5, the same letter idea you used for the PSLE." Check with n = 3: 2 × 3 + 5 = 11, which matches.'))
body=h2('Worked example: the 100th term')+card(p('Find the 100th term of  5, 8, 11, 14, …',44,700))
body+=step(1,'The difference is 3, so compare with the 3 times table: 3, 6, 9, 12.',top=410,size=36)
body+=step(2,'Each term is 2 more than 3 × n. So the nth term is 3n + 2.',top=520,size=36)
body+=step(3,'Check the 4th term: 3 × 4 + 2 = 14 ✓',top=630,size=36)
body+=answer(128,750,1664,'100th term = 3 × 100 + 2 = 302')
put(f'{L}-we1',sec(f'{L}-we1','27–29 MIN',body,'Click to reveal each step, asking the group to predict it first. Stress step 3: always check the rule on a term you can see, not only the 1st. Think-aloud: "3n on its own would give 3, 6, 9, 12. Ours are 5, 8, 11, 14, always 2 more. So 3n + 2."'))
put(f'{L}-try1',try_slide(f'{L}-try1','29–30 MIN','Your turn: rule and 100th term','Difference, times table, compare, check.',[('a','4, 9, 14, 19, …','5n − 1;  499'),('b','10, 12, 14, 16, …','2n + 8;  208'),('c','1, 8, 15, 22, …','7n − 6;  694')],'Whiteboards. a) Compare with 5, 10, 15, 20: 1 less, so 5n − 1; 500 − 1 = 499. b) 2, 4, 6, 8: 8 more, so 2n + 8; 208. c) 7, 14, 21, 28: 6 less, so 7n − 6; 694. Check c with the 4th term: 28 − 6 = 22. Watch for children writing 7n + 1 (they added the 1st term instead of comparing).',size=40))
prog=[HAT,('var','set term to (5)'),('ctl','repeat (99)',[('var','change term by (3)')]),('look','say (term)')]
body=h2('Test it in code')+pin(128,260,700,blocks(prog,34,'Code: set term to 5, repeat 99: change term by 3, then say term'),None)
body+=step(1,'Start at the 1st term: set term to 5.',left=880,top=260,width=912,size=34)
body+=step(2,'One loop = one jump: change term by 3.',left=880,top=380,width=912,size=34)
body+=step(3,'1st term to 100th term = 99 jumps: repeat 99.',left=880,top=500,width=912,size=34)
body+=answer(880,640,912,'It says 302. Same as 3 × 100 + 2 ✓')
body+=pin(128,780,1664,p('Maths first, then code to test it. If they disagree, one of them has a bug!',32,700,MUTED),'fade')
put(f'{L}-we2',sec(f'{L}-we2','30–33 MIN',body,'Build it live in Scratch while children copy (make a variable called term first: Variables, Make a Variable). Ask before step 3: "How many times should it repeat?" Many say 100. Draw 4 terms with 3 jumps between them on the whiteboard: 4 terms, 3 jumps. So 100 terms, 99 jumps. Run it: 302. Then try repeat 100: it says 305, the 101st term. Python version (optional):\nterm = 5\nfor i in range(99):\n    term = term + 3\nprint(term)\nIt prints 302.'))
body=h2('Key idea: the rule for the nth term')+card(p('The difference tells you the times table. Compare with it to find what to add or take away.',44,700))+card(p('From the 1st term to the nth term there are n − 1 jumps. Test your rule in code.',38,600,MUTED))
put(f'{L}-key',sec(f'{L}-key','33–35 MIN',body,'Say the key idea together. Common mistakes to watch for during the worksheet: (1) Using only the difference as the rule (writing 3n for 5, 8, 11, …) and not comparing with the 1st term. (2) Off by one: doing 100 jumps from the 1st term (5 + 3 × 100) instead of 99, in the maths and in the repeat block. (3) Putting "change" before "say" in a loop, so the sprite never says the 1st term.'))
put(f'{L}-break',f'''<section id="{L}-break" data-transition="fade" style="background:{TEAL};color:{CREAM};font-family:{BF};padding:128px 128px 160px;display:flex;flex-direction:column;justify-content:center;gap:36px">
<p style="font-size:32px;font-weight:700;letter-spacing:4px;color:{YEL}">35–40 MIN</p>
<h2 style="font-family:{HF};font-size:110px;font-weight:600;line-height:1.05">Brain break</h2>
<p style="font-size:48px;font-weight:600">Pattern moves: clap, clap, stomp, clap, clap, stomp … Do 12 moves together. Then predict: what is the 20th move? The 30th?</p>
<p style="font-size:36px;color:#D7EFEA">Then: a drink of water, stretch your fingers, back to the screen.</p>
<p style="position:absolute;left:128px;bottom:64px;width:1400px;font-size:24px;color:#D7EFEA">{E(slidekit.FOOT)}</p>
<aside>Five minutes, away from the keyboard. Answers: the pattern repeats every 3 moves. 20 = 6 × 3 + 2, so the 20th move is the 2nd in its group: clap. 30 = 10 × 3, so the 30th move ends a group: stomp.</aside>
</section>
''')

# ---------- before page 1: is it in the sequence? ----------
body=h2('Is it in the sequence? Work backwards')+card(p('2, 5, 8, 11, …   The rule is 3n − 1.',44,700))
body+=step(1,'Is 62 a term?  3n − 1 = 62, so 3n = 63 and n = 21.  Yes: the 21st term.',top=410,size=36)
body+=step(2,'Is 100 a term?  3n − 1 = 100, so 3n = 101. But 101 is not in the 3 times table.  No.',top=530,size=36)
body+=step(3,'Shortcut: every term is 1 less than a multiple of 3.',top=650,size=36)
put(f'{L}-teachwhich',sec(f'{L}-teachwhich','40–42 MIN',body,'Teach before worksheet page 1 (Q1d and Q3). This is the PSLE "think of a number" idea run backwards: undo the − 1, then undo the × 3. Check step 1 forwards: 3 × 21 − 1 = 62. For step 2, ask: "Which terms are near 100?" (98 is the 33rd, 101 would need n = 33⅔.)'))
put(f'{L}-trywhich',try_slide(f'{L}-trywhich','42–44 MIN','Your turn: work backwards','Find the rule first. Then undo it.',[('a','Is 50 a term of 2, 6, 10, 14, …?','Yes: 13th'),('b','Which term of 6, 11, 16, … is 96?','The 19th'),('c','Is 75 a term of 4, 8, 12, 16, …?','No: all even')],'Whiteboards. a) Rule 4n − 2: 4n = 52, n = 13. b) Rule 5n + 1: 5n = 95, n = 19. c) Rule 4n: every term is a multiple of 4, so every term is even; 75 is odd.',size=36))
put(f'{L}-ws1',ws_preview(f'{L}-ws1','44–54 MIN','Worksheet page 1: the maths, with your partner',[('Q1','Matchstick squares: table, rule, pattern 100, and which pattern has 61 sticks.'),('Q2','Two sequences: difference, rule for the nth term, 100th term.'),('Q3','Is it in the sequence? Work backwards.')],'Finished? Use the Python corner (or Scratch) to test your Q1 and Q2 answers.','Minutes 44 to 54. Pairs talk before they write. Ask "How did you check your rule?" Children who finish early test Q2 in Scratch: set term to the 1st term, repeat 99, change term by the difference, say term.'))
put(f'{L}-ws1ans',check(f'{L}-ws1ans','54–56 MIN','Page 1: check together',[('Q1','a) 7, 10, 13, 16, 19; adds 3 (shares a side)  b) 3n + 1  c) 301  d) pattern 20'),('Q2','a) 4n + 2 → 402   b) 5n − 4 → 496'),('Q3','a) 4n + 1   b) yes, the 25th term   c) no: every term is odd, 150 is even')],
 'Click after a pair explains. Q1a: 4 sticks for the first square, then only 3 for each new square because it shares a side. Q2: the other two sequences (2n + 7 and 0.5n) are now on the Think harder page. Q3b: 4n + 1 = 101, 4n = 100, n = 25.',size=36,gap=150))

# ---------- before page 2: trace, plan, bug ----------
prog=[HAT,('var','set x to (1)'),('ctl','repeat (3)',[('var','change x by (4)'),('look','say (x) for (1) seconds')])]
body=h2('Trace the code in a table')+pin(128,260,640,blocks(prog,34,'Code: set x to 1, repeat 3: change x by 4, say x for 1 seconds'),None)
Wt=[260,260]
body+=trow(900,260,['Loop','x'],Wt,None,True)
for i,(a,b) in enumerate([('1','5'),('2','9'),('3','13')]): body+=trow(900,350+i*90,[a,b],Wt,'rise')
body+=pin(128,660,1664,p('It says 5, 9, 13.  With repeat 50, the last number is 1 + 4 × 50 = 201.',36,800),'fade',YEL,20,'20px 30px')
put(f'{L}-teachtrace',sec(f'{L}-teachtrace','56–57 MIN',body,'Teach before worksheet page 2 (Q4). Point at each block in order and say what the computer does: "x is 1. Loop 1: change x by 4, x is 5, say 5." Click a row after children say it. Then ask for repeat 50 WITHOUT tracing 50 rows: x starts at 1 and gets 50 jumps of 4. Python (optional):\nx = 1\nfor i in range(3):\n    x = x + 4\n    print(x)\nPrints 5, 9, 13.'))
prog=[HAT,('var','set n to (7)'),('ctl','repeat (10)',[('look','say (n) for (1) seconds'),('var','change n by (5)')])]
body=h2('Plan your code: say 10 terms of 7, 12, 17, …')+pin(128,260,700,blocks(prog,32,'Code: set n to 7, repeat 10: say n, change n by 5'),None)
body+=step(1,'set n to the 1st term: 7.',left=880,top=260,width=912,size=34)
body+=step(2,'say BEFORE change, so the 1st term is said.',left=880,top=380,width=912,size=34)
body+=step(3,'10 terms said: repeat 10.',left=880,top=500,width=912,size=34)
body+=answer(880,620,912,'Last said: 7 + 5 × 9 = 52')
body+=pin(128,770,1664,p('n ends at 57, but 57 is never said. Ask: what would swapping say and change do?',32,700,MUTED),'fade')
put(f'{L}-teachplan',sec(f'{L}-teachplan','57–58 MIN',body,'Teach before worksheet page 2 (Q5). Plan on paper first: which variable, what start value, what goes inside the loop, in which order. If say and change are swapped, the sprite says 12, 17, …, 57: it misses the 1st term and says one extra. Python (optional):\nn = 7\nfor i in range(10):\n    print(n)\n    n = n + 5'))
def posts_svg(w=1664,h=150):
    g=''
    for i in range(5):
        x=140+i*330
        g+=f'<circle cx="{x}" cy="60" r="44" fill="{YEL}" stroke="{NAVY}" stroke-width="4"/><text x="{x}" y="76" font-size="40" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="Fredoka, Arial">{["1st","2nd","3rd","4th","5th"][i]}</text>'
        if i<4: g+=f'<path d="M{x+50} 40 Q{x+165} -10 {x+280} 40" fill="none" stroke="{TEAL}" stroke-width="5"/><polygon points="{x+284},44 {x+262},36 {x+276},20" fill="{TEAL}"/><text x="{x+165}" y="120" font-size="30" font-weight="800" text-anchor="middle" fill="{TEAL}" font-family="Nunito Sans, Arial">jump {i+1}</text>'
    return f'<svg aria-label="5 terms joined by 4 jumps" viewBox="0 0 1664 140" xmlns="http://www.w3.org/2000/svg" style="width:{w}px;height:{h}px;flex:none">{g}</svg>'
body=h2('Bug hunt: count the jumps')+pin(128,240,1664,posts_svg(),None)+pin(128,410,1664,p('5 terms, only 4 jumps. The 1st term is there before any jump.',36,700),None,SOFT,20,'18px 28px')
body+=step(1,'Ben wants the 20th term of 2, 6, 10, … His code: set n to 2, repeat 20, change n by 4.',top=530,size=34)
body+=step(2,'It says 2 + 20 × 4 = 82. But the rule 4n − 2 gives 78.',top=640,size=34)
body+=step(3,'Fix: 1st term to 20th term is 19 jumps, so repeat 19 (2 + 19 × 4 = 78 ✓).',top=750,size=34)
put(f'{L}-teachbug',sec(f'{L}-teachbug','58–59 MIN',body,'Teach before worksheet page 2 (Q6). This is the fence-post idea: 5 posts have 4 gaps. When the maths and the code disagree, find which one is wrong and why. Ask: "Is there another fix?" (yes: start n at −2, the 0th term, and keep repeat 20).'))
put(f'{L}-ws2',ws_preview(f'{L}-ws2','59–72 MIN','Worksheet page 2: the code, on your own',[('Q4','Predict, then trace the loop in a table.'),('Q5','Plan your code: say the first 20 terms of 4, 10, 16, 22, …'),('Q6','Spot the bug in Mei’s code, then fix it.')],'Write on paper first, then test in Scratch. Finished early? Stretch and Challenge come next.','Children work alone. Let them test Q4 to Q6 in Scratch AFTER writing their prediction. Note who needs a short catch-up next lesson.'))
put(f'{L}-ws2ans',check(f'{L}-ws2ans','72–75 MIN','Page 2: check together',[('Q4','x: 7, 12, 17, 22.  a) 22   b) 502 (2 + 100 × 5)'),('Q5','set n to 4, repeat 20 [say n for 1 seconds, change n by 6].  Last said: 118'),('Q6','a) 203   b) 199 (4n − 1)   c) repeat 49: the 1st term needs no jump')],
 'Click after a child explains. Q5: say must come before change. The last number said is the 20th term, 6 × 20 − 2 = 118 (n ends at 124 but it is never said). Q6: 3 + 50 × 4 = 203 is the 51st term.',size=36,gap=150))

# ---------- stretch, challenge ----------
st=[('1.','The 5th term is 23 and the 6th term is 27. The difference is always the same. What is the 1st term? What is the rule?'),('2.','The 1st term is 4 and the 10th term is 40. What is the difference?'),('3.','Write a sequence whose 1st term is 10 and whose 100th term is 1000.')]
put(f'{L}-stretch',sec(f'{L}-stretch','For early finishers',h2('Stretch')+''.join(talkcard(a,b,36) for a,b in st),'Answers: 1) 7: go back 4 jumps of 4 from 23 (23 − 16 = 7); rule 4n + 3. 2) 4: from the 1st to the 10th term is 9 jumps, and 36 ÷ 9 = 4 (rule 4n). 3) 10, 20, 30, 40, … (rule 10n): 99 jumps must add 990, so each jump is 10.'))
ch=[('1.','Which numbers below 60 are in BOTH sequences 2, 5, 8, 11, … and 4, 9, 14, 19, …? Find them all.'),('2.','What does this code say?  set t to 0, set k to 0, then repeat 5 [change k by 1, change t by k], then say t. What would it say with repeat 100?')]
put(f'{L}-challenge',sec(f'{L}-challenge','Challenge',h2('Challenge')+''.join(talkcard(a,b,36) for a,b in ch),'Pairs try first, then the "see it" slide, then the walk-through. Answers: 1) 14, 29, 44 and 59. 2) 15 (1 + 2 + 3 + 4 + 5); with repeat 100 it says 5050.'))
def lines2_svg():
    g=''
    for r,(lab,a,d,col) in enumerate([('A',2,3,YEL),('B',4,5,SKY)]):
        y=80+r*150
        g+=f'<text x="10" y="{y+10}" font-size="30" font-weight="800" fill="{TEAL}" font-family="Nunito Sans, Arial">{lab}</text><line x1="50" y1="{y}" x2="790" y2="{y}" stroke="{NAVY}" stroke-width="4"/>'
        for v in range(0,61,10):
            x=60+v*12; g+=f'<line x1="{x}" y1="{y-10}" x2="{x}" y2="{y+10}" stroke="{NAVY}" stroke-width="3"/><text x="{x}" y="{y+48}" font-size="27" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="Nunito Sans, Arial">{v}</text>'
        for k in range(3):
            v=a+k*d; x=60+v*12; g+=f'<circle cx="{x}" cy="{y}" r="11" fill="{col}" stroke="{NAVY}" stroke-width="3"/>'
        g+=f'<text x="{60+(a+3*d)*12+30}" y="{y-16}" font-size="30" font-weight="800" fill="{NAVY}" font-family="Nunito Sans, Arial">…?</text>'
    g+=f'<text x="400" y="380" font-size="28" font-weight="700" text-anchor="middle" fill="{TEAL}" font-family="Nunito Sans, Arial">Where do the two lists land on the same number?</text>'
    return f'<svg aria-label="Two number lines from 0 to 60 with the first three terms of each sequence marked" viewBox="0 0 800 400" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;display:block">{g}</svg>'
prog=[HAT,('var','set t to (0)'),('var','set k to (0)'),('ctl','repeat (5)',[('var','change k by (1)'),('var','change t by (k)')]),('look','say (t)')]
tt='<div style="display:flex;gap:24px;align-items:flex-start">'+blocks(prog,24,'Code: set t to 0, set k to 0, repeat 5: change k by 1, change t by k, then say t')
tt+='<div style="display:flex;flex-direction:column">'+''.join(f'<div style="display:flex;background:{YEL if i==0 else WHITE};border:3px solid {NAVY};margin-top:-3px"><p style="width:90px;padding:6px;font-size:26px;font-weight:800;text-align:center">{a}</p><p style="width:90px;padding:6px;font-size:26px;font-weight:800;text-align:center">{b}</p></div>' for i,(a,b) in enumerate([('k','t'),('0','0'),('?','?'),('?','?'),('?','?')]))+'</div></div>'
body=h2('Challenge: see it',60)+'<div style="display:flex;gap:32px;align-items:flex-start">'+card(f'<p style="font-size:28px;font-weight:700;color:{TEAL}">Q1: Two sequences</p>'+lines2_svg(),extra='flex:1;min-width:0;padding:20px 24px')+card(f'<p style="font-size:28px;font-weight:700;color:{TEAL}">Q2: Trace the loop</p>'+tt,extra='flex:1;min-width:0;padding:20px 24px')+'</div>'
put(f'{L}-chdiag',sec(f'{L}-chdiag','Challenge',body,'Show after pairs have tried, or if they are stuck. The pictures show the problem, not the answer. Ask: What do you notice? Q1: what are the next marks on each line? Q2: what happens to k and to t in the first loop?'))
body=h2('Challenge: walk-through')+pin(128,250,800,p('Q1: list, then look for a pattern',36,800,TEAL))
for i,t in enumerate(['A: 2, 5, 8, 11, 14, 17, 20, 23, 26, 29, …','B: 4, 9, 14, 19, 24, 29, …','Both: 14, 29, 44, 59 — every 15','One more is in the 3 AND 5 times tables']): body+=pin(128,330+i*120,800,p(t,30),'rise',WHITE)
body+=pin(992,250,800,p('Q2: trace the table',36,800,TEAL))
for i,t in enumerate(['k: 1, 2, 3, 4, 5','t: 1, 3, 6, 10, 15 → says 15','repeat 100: 1 + 2 + … + 100','Pairs 1 + 100, 2 + 99, …: 50 × 101 = 5050']): body+=pin(992,330+i*120,800,p(t,30),'rise',WHITE)
put(f'{L}-chwalk',sec(f'{L}-chwalk','Challenge',body,'Use after pairs have tried. Q1: the common terms go up by 15 because 15 is the smallest number in both the 3 and the 5 times tables; 14 + 15 = 29, then 44, then 59 (the next, 74, is too big). Q2: t adds up 1, 2, 3, … These are the triangle numbers. Python (optional):\nt = 0\nk = 0\nfor i in range(100):\n    k = k + 1\n    t = t + k\nprint(t)\nPrints 5050.'))
body=h2('Talk time')+card(chip('TALK TIME',YEL,NAVY)+p('Ali says the 100th term of 7, 10, 13, … is 7 + 3 × 100 = 307. Is he right? Explain with a rule, a picture or code.',42,600))+card(p('Sentence starters:',34,400,MUTED)+p('“I noticed that …”   “I tested it by …”   “I know because …”',38,600))
put(f'{L}-talk',sec(f'{L}-talk','75–82 MIN',body,'Minutes 75 to 82. Pairs talk for 2 minutes, then share. Listen for: No. The 1st term is already 7 before any jump, so the 100th term is only 99 jumps away: 7 + 3 × 99 = 304. The rule 3n + 4 gives 304 too. Then ask: "When is the rule better than adding on? When is code better than both?" (The rule is fastest for one far term; code is best for listing many terms or checking.)'))
body=h2('Exit ticket')+card(chip('EXIT TICKET')+p('The sequence 8, 11, 14, 17, …',46,600)+p('(a) Write the rule for the nth term.   (b) Find the 100th term.   (c) A loop starts at the 1st term. How many times must it repeat “change by 3” to reach the 100th term?',38,600))+card(p('Write your answers on paper. Show your tutor, then collect your stamp.',34))
put(f'{L}-exit',sec(f'{L}-exit','82–90 MIN',body,'Minutes 82 to 90. Answers: (a) 3n + 5  (b) 305  (c) 99 times. Extension: make the program say the position and the term together (for example "term 7 is 23") using a second variable pos and the join block, then make it stop at the first term bigger than 1000 (the 333rd term, 1001).'))

order=[f'{L}-{x}' for x in ['title','warm1','warm2','explore1','explore2','teach1','we1','try1','we2','key','break','teachwhich','trywhich','ws1','ws1ans','teachtrace','teachplan','teachbug','ws2','ws2ans','stretch','challenge','chdiag','chwalk','talk','exit']]
assert set(order)==set(S), set(order)^set(S)
for f in os.listdir(os.path.join(D,'slides')):
    if f.endswith('.html') and f[:-5] not in S: os.remove(os.path.join(D,'slides',f))
for i,h in S.items(): open(os.path.join(D,'slides',i+'.html'),'w').write(h)
deck={'v':4,'createdOnFiles':{'v':1,'at':datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')},'lists':'css',
      'title':'Math Inquirers P6: Lesson 1 – Code the Pattern','order':order,'cover':f'{L}-title',
      'sections':{'s1':{'description':'Warm-up and explore','start':f'{L}-title'},'s2':{'description':'Teach: the rule for the nth term, tested in code','start':f'{L}-teach1'},'s3':{'description':'Worksheet with teaching before each page','start':f'{L}-break'},'s4':{'description':'Stretch, challenge, talk and exit','start':f'{L}-stretch'}},
      'faces':{'fredoka':{'family':'Fredoka','href':'https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&display=swap'},'nunito-sans':{'family':'Nunito Sans','href':'https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@400;600;700&display=swap'}},'designSystems':[]}
json.dump(deck,open(os.path.join(D,'deck.json'),'w'),indent=1,ensure_ascii=False)
print(len(order),'slides')

import p6_gaps; p6_gaps.apply(1)
