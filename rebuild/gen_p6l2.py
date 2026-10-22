"""Math Inquirers Level 6, Lesson 2: Prime Hunters. Writes split/p6l1/project (deck.json + slides/*.html)."""
import json,os,sys,re,datetime
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,H)
import slidekit
from slidekit import *
slidekit.FOOT='Math Inquirers Level 6  •  Notice it. Test it. Explain why.'
L='p6l2'
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


# ---------- helpers for this lesson ----------
def isp(n): return n>1 and all(n%d for d in range(2,int(n**.5)+1))
def grid_svg(w=1450,h=330,rows=3,circle=(2,3),grey=(2,)):
    """1..10*rows grid: multiples (other than itself) of numbers in grey are greyed; 1 greyed; circle marks chosen primes."""
    cwid=w/10; rh=h/rows; g=''
    for n in range(1,10*rows+1):
        r,c=(n-1)//10,(n-1)%10; x=c*cwid; y=r*rh
        out=n==1 or any(n%k==0 and n!=k for k in grey)
        g+=f'<rect x="{x:.0f}" y="{y:.0f}" width="{cwid:.0f}" height="{rh:.0f}" fill="{"#D5DAE6" if out else WHITE}" stroke="{NAVY}" stroke-width="2"/>'
        if n in circle: g+=f'<circle cx="{x+cwid/2:.0f}" cy="{y+rh/2:.0f}" r="{rh*0.4:.0f}" fill="{YEL}" stroke="{NAVY}" stroke-width="4"/>'
        g+=f'<text x="{x+cwid/2:.0f}" y="{y+rh/2+12:.0f}" font-size="34" font-weight="700" text-anchor="middle" fill="{NAVY if not out else "#7A869F"}" font-family="Fredoka, Arial">{n}</text>'
    return f'<svg aria-label="A 1 to {10*rows} number grid with 2 and 3 circled and multiples of 2 shaded grey" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="width:{w}px;height:{h}px;flex:none">{g}</svg>'
def tree_svg(top,l,r,w=520,h=240,fill_l=True,fill_r=True,label='Factor tree'):
    g=f'<line x1="260" y1="50" x2="130" y2="130" stroke="{NAVY}" stroke-width="5"/><line x1="260" y1="50" x2="390" y2="130" stroke="{NAVY}" stroke-width="5"/>'
    g+=f'<circle cx="260" cy="40" r="38" fill="{YEL}" stroke="{NAVY}" stroke-width="4"/><text x="260" y="54" font-size="38" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="Fredoka, Arial">{top}</text>'
    for cx,v,f in ((130,l,fill_l),(390,r,fill_r)):
        g+=f'<circle cx="{cx}" cy="150" r="36" fill="{SKY if f else WHITE}" stroke="{NAVY}" stroke-width="4"/>'
        if f: g+=f'<text x="{cx}" y="163" font-size="36" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="Fredoka, Arial">{v}</text>'
    return f'<svg aria-label="{E(label)}" viewBox="0 0 520 200" xmlns="http://www.w3.org/2000/svg" style="width:{w}px;height:{h}px;flex:none">{g}</svg>'
def tree2_svg(w=760,h=300,show=1):
    """60 -> 6 x 10 -> 2 x 3 and 2 x 5 ; show = how many levels (1 or 2)"""
    def node(cx,cy,v,col,r=36):
        return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{col}" stroke="{NAVY}" stroke-width="4"/><text x="{cx}" y="{cy+13}" font-size="36" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="Fredoka, Arial">{v}</text>'
    def ln(x1,y1,x2,y2): return f'<line x1="{x1}" y1="{y1+30}" x2="{x2}" y2="{y2-30}" stroke="{NAVY}" stroke-width="5"/>'
    g=ln(380,40,200,140)+ln(380,40,560,140)+node(380,40,60,YEL)+node(200,140,6,WHITE)+node(560,140,10,WHITE)
    if show>=2:
        g+=ln(200,140,110,240)+ln(200,140,290,240)+ln(560,140,470,240)+ln(560,140,650,240)
        for cx,v in ((110,2),(290,3),(470,2),(650,5)): g+=node(cx,240,v,SKY)
    return f'<svg aria-label="Factor tree for 60: 6 times 10, then 2 times 3 and 2 times 5" viewBox="0 0 760 300" xmlns="http://www.w3.org/2000/svg" style="width:{w}px;height:{h}px;flex:none">{g}</svg>'

# ---------- title ----------
OBJ='Find all the factors of a number using factor pairs, decide whether a number is prime by testing small divisors, write a number as a product of primes with a factor tree, use mod (the remainder), if and a counter in code to count factors, and explore Goldbach pairs and numbers with exactly 3 factors.'
MAT='Laptop or desktop with Scratch 3 open, a printed 1 to 100 grid (or squared paper), two coloured pencils, mini whiteboard, workbook. Optional: a Python editor for children who already know Python.'
ONL='Share the 1 to 100 grid on screen and annotate it while children work on their own printed or hand-drawn grid. Build the prime checker together in your shared Scratch window; the blocks are also on the slide. Block colours on our slides are simplified; in Scratch, find blocks by the category name on the left, not by colour. Children hold their grid up to the camera at minute 22.'
put(f'{L}-title',f'''<section id="{L}-title" data-transition="fade" style="background:{NAVY};color:{CREAM};font-family:{BF};padding:128px 128px 160px;display:flex;flex-direction:column;justify-content:center;gap:36px">
<p style="font-size:32px;font-weight:700;letter-spacing:4px;color:{YEL}">LESSON 2  •  WEEK 1  •  MATHS + CODE</p>
<h1 style="font-family:{HF};font-size:128px;font-weight:600;line-height:1.05">Prime Hunters</h1>
<p style="font-size:44px;color:#C9D4EC">Primes, factors and prime factorisation  •  if, mod and a counter</p>
<div style="background:#26385F;border-radius:24px;padding:40px;display:flex;flex-direction:column;gap:12px"><p style="font-size:28px;font-weight:700;letter-spacing:3px;color:{YEL}">TODAY WE WILL</p><p style="font-size:44px;font-weight:600">Find factors in pairs, test whether a number is prime, split numbers into primes, and teach a computer to count factors with mod.</p></div>
<p style="position:absolute;left:128px;bottom:64px;width:1400px;font-size:24px;color:#B7C3DD">{E(slidekit.FOOT)}</p>
<aside>{E(f"Objective: {OBJ} Materials: {MAT} Online: {ONL} Time plan: warm-up 0 to 10, explore 10 to 25 (the sieve by hand), teaching 25 to 35 (click to reveal each step and answer), brain break 35 to 40, worksheet 40 to 75 with short teaching before each page and a check-together slide after it (page 1 is the maths, page 2 is the code and the puzzles), talk time 75 to 82, exit ticket 82 to 90. Python: the optional Python version of each program is in the notes of the code slides and in the workbook Python corner.")}</aside>
</section>
''')

# ---------- warm-up 1 ----------
cards=[('12','1×12, 2×6, 3×4'),('16','1×16, 2×8, 4×4'),('20','1×20, 2×10, 4×5'),('24','1×24, 2×12, 3×8, 4×6'),('29','only 1×29'),('30','1×30, 2×15, 3×10, 5×6')]
body=h2('Warm-up: Factor pair hunt')+p('Find every pair of whole numbers that multiply to make the number. One card has only ONE pair.',34,600,MUTED)
CW=533
for i,(a,b) in enumerate(cards):
    Lf=128+(i%3)*(CW+32); T=300+(i//3)*290
    body+=pin(Lf,T,CW,f'<p style="font-family:{HF};font-size:30px;font-weight:600;color:{TEAL}">Card {i+1}</p><p style="font-family:{HF};font-size:64px;font-weight:600">{a}</p>',None,WHITE,24,'20px 28px',f'box-sizing:border-box;height:260px;border:4px solid {NAVY};box-shadow:8px 8px 0 {NAVY}')
    body+=pin(Lf+160,T+130,CW-180,f'<p style="font-size:28px;font-weight:800">{E(b)}</p>','pop',SOFT,16,'12px 18px',f'box-sizing:border-box;border:3px solid {NAVY}')
put(f'{L}-warm1',sec(f'{L}-warm1','0–5 MIN',body,'Minutes 5 to 8. Pairs work together (no racing, no points); show one card at a time and click to reveal its pairs (clicks go card 1 to card 6). Ask: "How do you know you have them all?" Listen for working in order (1, 2, 3, 4 …) and stopping when the pairs meet. Card 2: 4 × 4 is one pair, so 16 has 5 factors (1, 2, 4, 8, 16). Card 5: 29 has only the pair 1 × 29, so it is PRIME: that is today\'s word. Try 2, 3, 4, 5 on 29 to prove it. Card 4: 8 factors; card 3: 6 factors; card 1: 6; card 6: 8.'))
qs=[('1.','17 ÷ 5 = 3 remainder __','2'),('2.','30 ÷ 6 = 5 remainder __','0'),('3.','23 ÷ 4 = 5 remainder __','3'),('4.','100 ÷ 7: what is the remainder?','2'),('5.','A remainder of 0 means the number is a ___ of the other.','factor')]
body=h2('Quick questions')+''.join(qrow(128,250+i*125,1250,a,b,36) for i,(a,b,c) in enumerate(qs))+''.join(answer(1420,250+i*125,372,c) for i,(a,b,c) in enumerate(qs))
put(f'{L}-warm2',sec(f'{L}-warm2','5–10 MIN',body,'Minutes 5 to 10. Whiteboards, then click. Introduce the word: "The remainder has a short name in computing: mod. 17 mod 5 = 2. We will use it in code today." Q4: 7 × 14 = 98, so 100 mod 7 = 2. Q5: if 30 mod 6 = 0, then 6 divides 30 exactly, so 6 is a factor of 30. This is the link between maths and code for the whole lesson.'))

# ---------- explore ----------
steps=['On your 1 to 100 grid, cross out 1. It is not prime.','Circle 2. Cross out every other multiple of 2 (4, 6, 8, …).','Circle the next number not crossed out (3). Cross out its other multiples. Do the same for 5 and 7.','Circle every number left. How many primes are there?']
inner=chip('EXPLORE')+'<ol style="font-size:32px;font-weight:600;padding-left:48px;margin:0;display:flex;flex-direction:column;gap:6px">'+''.join(f'<li>{E(s)}</li>' for s in steps)+'</ol>'
body=h2('Explore: the sieve')+card(inner)+card(grid_svg(1450,300),extra='align-items:center;padding:12px 40px')
put(f'{L}-explore1',sec(f'{L}-explore1','10–15 MIN',body,'Minutes 10 to 15. Pairs work on a printed 1 to 100 grid (online: drawn grid, or the tutor annotates a shared grid and children copy). The picture shows the start: 1 greyed, 2 and 3 circled, multiples of 2 greyed. First ask for a prediction: how many primes below 100? Insist on circling each prime as they go. This is the sieve of Eratosthenes, about 2200 years old. Do not reveal the count yet. Finished early: look at which numbers are left after crossing out multiples of 2, 3, 5 and 7 and whether any multiple of 11 is still uncrossed.'))
body=h2('Explore: talk about it')+talkcard('1.','How many primes are there from 1 to 100?')+talkcard('2.','Why could we stop after the multiples of 7?')+talkcard('3.','Is 1 prime? Is 2 prime? Is any other even number prime?')
put(f'{L}-explore2',sec(f'{L}-explore2','15–25 MIN',body,'Minutes 15 to 25. Answers: 1) 25: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97. 2) The next prime is 11 and 11 × 11 = 121 is bigger than 100. Any multiple of 11 below 100 (22, 33, … 99) is 11 times something smaller than 11, so it was crossed out earlier. 3) 1 is not prime: it has only one factor. 2 is prime (factors 1 and 2) and it is the only even prime: every other even number has 2 as a factor too.'))

# ---------- teach ----------
body=h2('Factors come in pairs')+card(p('Find all the factors of 18.',44,700))
rows=[('1 × 18','1 and 18'),('2 × 9','2 and 9'),('3 × 6','3 and 6'),('4 ×  ?','4 does not divide 18'),('Next pair would be 6 × 3: already have it. Stop.','')]
body+=trow(128,390,['pair','factors'],[330,400],None,True)
for i,(a,b) in enumerate(rows[:3]): body+=trow(128,480+i*90,[a,b],[330,400],'rise')
body+=pin(1050,390,742,p('Work in order: 1, 2, 3, 4 … Test each number. Write BOTH numbers of each pair.',34,700),None,WHITE,20,'22px 26px')
body+=pin(1050,560,742,p('4 and 5 do not divide 18. The next pair would be 6 × 3, which we already have, so we stop.',34,700),'fade',SOFT,20,'22px 26px')
body+=answer(128,780,1664,'18 has 6 factors: 1, 2, 3, 6, 9, 18')
put(f'{L}-teach1',sec(f'{L}-teach1','25–27 MIN',body,'Teach. Think-aloud: "Factors of 18. 1 × 18, so 1 and 18. 2 × 9, so 2 and 9. 3 × 6. Does 4 go into 18? No. 5? No. The next is 6, and I already have 6. The pairs have met, so I stop." A prime has exactly two factors: 1 and itself. 18 is not prime. 1 is not prime (one factor only). A square number such as 36 has the pair 6 × 6, and 6 is counted once, so 36 has 9 factors.'))
body=h2('Worked example: is 91 prime?')+card(p('A prime has exactly two factors. Test small numbers.',44,700))
body+=step(1,'Not even. 9 + 1 = 10, not a multiple of 3. Does not end in 0 or 5.',top=410,size=36)
body+=step(2,'Try 7: 7 × 13 = 91. So 7 is a factor.',top=520,size=36)
body+=step(3,'Stop testing once d × d is bigger than the number: 10 × 10 = 100 is bigger than 91.',top=630,size=36)
body+=answer(128,750,1664,'91 is NOT prime: 91 = 7 × 13')
put(f'{L}-we1',sec(f'{L}-we1','27–29 MIN',body,'Click to reveal each step; ask the group to predict it. 91 looks prime but is not: nice surprise. The quick tests: even (divides by 2); digits add to a multiple of 3 (divides by 3); ends in 0 or 5 (divides by 5). Then try 7. Why stop at 10? If 91 had a factor pair with both numbers 10 or more, the product would be at least 100. So one factor of any pair is less than 10. Check 91 ÷ 7 = 13 with 7 × 13.'))
put(f'{L}-try1',try_slide(f'{L}-try1','29–30 MIN','Your turn: prime or not?','Use the quick tests, then 7. Show your factor pair if it is not prime.',[('a','Is 57 prime?','No: 3 × 19'),('b','Is 71 prime?','Yes'),('c','Is 119 prime?','No: 7 × 17')],'Whiteboards. a) 5 + 7 = 12, so 3 divides it: 57 = 3 × 19. b) Not even, 7 + 1 = 8 so not 3, not 5, 7 × 10 = 70 so 71 is not 7 times anything; 8 × 8 = 64 and 9 × 9 = 81 > 71, so test up to 7 only: prime. c) 7 × 17 = 119. Many children say 119 is prime: it is the classic trap.',size=40))
body=h2('Factor trees: split into primes')+pin(128,240,760,tree2_svg(760,300,2),'fade')
body+=step(1,'60 = 6 × 10. Split any two factors you know.',left=900,top=250,width=892,size=34)
body+=step(2,'6 = 2 × 3 and 10 = 2 × 5. Keep splitting until every branch is a prime.',left=900,top=370,width=892,size=34)
body+=step(3,'Primes at the ends: 2, 3, 2, 5. Write them in order.',left=900,top=490,width=892,size=34)
body+=answer(128,640,1664,'60 = 2 × 2 × 3 × 5     (another start, 4 × 15, gives the same primes)')
body+=pin(128,780,1664,p('Every number above 1 has only ONE set of prime factors. A prime that is a factor is a "prime factor".',32,700,MUTED),'fade')
put(f'{L}-we2',sec(f'{L}-we2','30–32 MIN',body,'Build the tree on the whiteboard as you click. Stop each branch only at a prime: circle primes (2, 3, 5 ...). Start again with 60 = 4 × 15 = 2 × 2 × 3 × 5: the same primes, different tree. Check by multiplying: 2 × 2 × 3 × 5 = 60. Think-aloud: "Is 6 prime? No, it has factors 2 and 3. Split it."'))
prog=[HAT,('var','set count to (0)'),('var','set d to (1)'),('ctl','repeat (15)',[('ctl','if (15 mod d = 0) then',[('var','change count by (1)')]),('var','change d by (1)')]),('look','say (count)')]
body=h2('Test it in code: count the factors')+pin(128,240,860,blocks(prog,26,'Code: set count 0, d 1; repeat 15: if 15 mod d = 0 then change count by 1; change d by 1; then say count'),None)
body+=step(1,'d goes 1, 2, 3, … 15 (change d by 1 each loop).',left=1020,top=250,width=772,size=32)
body+=step(2,'15 mod d = 0 means d is a factor. Count it.',left=1020,top=370,width=772,size=32)
body+=step(3,'Factors 1, 3, 5, 15: count = 4. Not 2.',left=1020,top=490,width=772,size=32)
body+=answer(1020,610,772,'It says 4. Not 2, so 15 is not prime')
put(f'{L}-we3',sec(f'{L}-we3','32–35 MIN',body,'Build live in Scratch while children copy: make variables count and d. n mod d is in the operators section (the "mod" block). Ask before running: "Which loops add 1 to count?" (d = 1, 3, 5, 15). Then change both 15s to 13: it says 2, so 13 is prime (count = 2 means prime). Extension for any child who wants more: add if count = 2 then say prime, else say not prime after the loop. Python (optional):\nn = 15\ncount = 0\nfor d in range(1, n + 1):\n    if n % d == 0:\n        count = count + 1\nif count == 2:\n    print("prime")\nelse:\n    print("not prime")\nIt prints not prime.'))
body=h2('Key idea: exactly two factors')+card(p('A prime has exactly 2 factors: 1 and itself. Test 2, 3, 5, 7, … until d × d is bigger than the number.',44,700))+card(p('n mod d is the remainder. n mod d = 0 means d is a factor of n.',38,600,MUTED))
put(f'{L}-key',sec(f'{L}-key','35 MIN',body,'Say the key idea together. Common mistakes to watch for during the worksheet: (1) Saying 1 is prime, or that 2 is not prime because it is even. (2) Missing factors by not working in pairs, or counting the middle factor of a square number twice (6 in 36). (3) Stopping a factor tree at a number that is not prime (72 = 2 × 2 × 18), or reading mod as division (thinking 10 mod 4 is 2.5 instead of the remainder 2).'))
put(f'{L}-break',f'''<section id="{L}-break" data-transition="fade" style="background:{TEAL};color:{CREAM};font-family:{BF};padding:128px 128px 160px;display:flex;flex-direction:column;justify-content:center;gap:36px">
<p style="font-size:32px;font-weight:700;letter-spacing:4px;color:{YEL}">35–40 MIN</p>
<h2 style="font-family:{HF};font-size:110px;font-weight:600;line-height:1.05">Brain break</h2>
<p style="font-size:48px;font-weight:600">Prime or not? Jump if it is prime, squat if it is not: 7, 9, 13, 21, 2, 1, 31, 27, 51, 53.</p>
<p style="font-size:36px;color:#D7EFEA">Then: a drink of water, stretch your fingers, back to the screen.</p>
<p style="position:absolute;left:128px;bottom:64px;width:1400px;font-size:24px;color:#D7EFEA">{E(slidekit.FOOT)}</p>
<aside>Five minutes, away from the keyboard. Answers in order: prime, not (3 × 3), prime, not (3 × 7), prime (2: the only even prime), not (1 has one factor), prime, not (3 × 9), not (3 × 17), prime.</aside>
</section>
''')

# ---------- page 1 ----------
put(f'{L}-ws1',ws_preview(f'{L}-ws1','40–54 MIN','Worksheet page 1: the maths, with your partner',[('Q1','Factors table (28, 31, 49, 51, 1), prime tests, and Ali\'s claim about 87.'),('Q2','Factor trees for 72 and 150, then a number from its prime factors.')],'Stuck? Work in pairs from 1, and use the quick tests. Finished? Try the Python corner to test your table.','Minutes 40 to 54. Pairs talk before they write. Ask "How do you know you have every factor?" and "Why can you stop here?" Children who finish early run the Python corner for n = 28, 31, 49 and 51.'))
put(f'{L}-ws1ans',check(f'{L}-ws1ans','54–56 MIN','Page 1: check together',[('Q1','28: 6 factors. 31: 2, prime. 49: 1, 7, 49. 51: 1, 3, 17, 51. 1: just 1, not prime. Primes: 67, 83, 97. 87 = 3 × 29.'),('Q2','72 = 2 × 2 × 2 × 3 × 3.   150 = 2 × 3 × 5 × 5.   2 × 3 × 3 × 7 = 126.')],
 'Click after a pair explains. Q1: 28 = 1 × 28, 2 × 14, 4 × 7. 31 has only 1 × 31. 49 = 1 × 49, 7 × 7 (7 counts once): 3 factors, not prime. 51 = 3 × 17 (5 + 1 = 6, a multiple of 3). 57 = 3 × 19, 77 = 7 × 11, 99 = 9 × 11 are the traps. Ali is wrong about 87: 8 + 7 = 15, a multiple of 3, so 87 = 3 × 29. Q2: any tree works if it ends in primes.',size=34,gap=190))

# ---------- page 2 teaching ----------
prog=[HAT,('var','set count to (0)'),('var','set d to (1)'),('ctl','repeat (4)',[('ctl','if (8 mod d = 0) then',[('var','change count by (1)')]),('var','change d by (1)')]),('look','say (count)')]
body=h2('Trace the loop in a table')+pin(128,230,780,blocks(prog,26,'Code: set count 0, d 1; repeat 4: if 8 mod d = 0 then change count by 1; change d by 1; say count'),None)
Wt=[140,230,230]
body+=trow(960,240,['d','8 mod d','count'],Wt,None,True)
for i,r in enumerate([('1','0','1'),('2','0','2'),('3','2','2'),('4','0','3')]): body+=trow(960,330+i*90,list(r),Wt,'rise')
body+=pin(128,720,1664,p('If 8 mod d is 0, count goes up. After 4 loops count = 3 (1, 2 and 4 are factors of 8). It says 3.',34,800),'fade',YEL,20,'20px 30px')
put(f'{L}-teachtrace',sec(f'{L}-teachtrace','56–58 MIN',body,'Teach before worksheet page 2 (Q3). Walk through: d starts at 1; each time round the loop we test 8 mod d, maybe add 1 to count, then add 1 to d. Rows reveal on click. Row 3: 8 mod 3 = 2 (8 = 3 × 2 + 2), not 0, so count stays 2. Ask: "Why is the answer 3 and not 4?" (the loop only goes up to d = 4; 8 has more factors, 8 itself, but it is not tested.) Python (optional):\ncount = 0\nfor d in range(1, 5):\n    if 8 % d == 0:\n        count = count + 1\nprint(count)\nPrints 3.'))
body=h2('Goldbach pairs: sum of two primes')+card(p('Write 20 as a sum of two primes, in every way.',44,700))
body+=step(1,'List the primes below 20: 2, 3, 5, 7, 11, 13, 17, 19.',top=410,size=36)
body+=step(2,'For each prime p, is 20 − p prime?  3 + 17 yes.  7 + 13 yes.  Others: 20 − 5 = 15, 20 − 11 = 9 no.',top=520,size=34)
body+=answer(128,650,1664,'20 = 3 + 17 = 7 + 13   (2 ways)')
body+=pin(128,780,1664,p('Only go as far as half of 20: after 10, the pairs repeat in reverse (17 + 3).',32,700,MUTED),'fade')
put(f'{L}-teachgold',sec(f'{L}-teachgold','58–59 MIN',body,'Teach before worksheet page 2 (Q4). Goldbach wrote in 1742 that every even number above 2 is the sum of two primes. No one has found a counterexample, and no one has proved it. Check primes up to 10 only: 3, 7 (5 gives 15, 2 gives 18). For odd totals: one of the two numbers must be even, and the only even prime is 2.'))
body=h2('Count the factors of a square')+card(p('How many factors do 16 and 36 have? What do you notice?',44,700))
body+=step(1,'16: 1 × 16, 2 × 8, 4 × 4.  Factors 1, 2, 4, 8, 16: 5 factors.',top=410,size=36)
body+=step(2,'36: 1 × 36, 2 × 18, 3 × 12, 4 × 9, 6 × 6.  9 factors.',top=520,size=36)
body+=step(3,'Both counts are ODD: the middle pair is a number times itself.',top=630,size=36)
body+=pin(128,770,1664,p('Page 2, Q5 asks for numbers with exactly 3 factors. Which squares might work?',34,700),'fade',SOFT,20,'18px 28px')
put(f'{L}-teachsq',sec(f'{L}-teachsq','59–60 MIN',body,'Teach before worksheet page 2 (Q5). Do NOT give the Q5 answer. Say: "36 has 9 factors; 16 has 5. A number with exactly 3 factors must be a square, because the count is odd. Which squares have only 3? Try 4, 9, 16, 25, 36 yourself." Children find 4, 9, 25, 49 and notice they are squares of primes.'))
prog=[HAT,('var','set d to (1)'),('ctl','repeat (20)',[('ctl','if (20 mod d = 0) then',[('look','say (d) for (1) seconds')]),('var','change d by (1)')])]
body=h2('Plan your code: say every factor of 20')+pin(128,240,780,blocks(prog,30,'Code: set d to 1; repeat 20: if 20 mod d = 0 then say d for 1 seconds; change d by 1'),None)
body+=step(1,'d starts at 1 and tests every number up to 20.',left=960,top=250,width=832,size=32)
body+=step(2,'The if block goes INSIDE the repeat; change d is inside too, but outside the if.',left=960,top=370,width=832,size=32)
body+=answer(960,540,832,'It says 1, 2, 4, 5, 10, 20 (one per second)')
body+=pin(128,740,1664,p('If change d were inside the if, d would get stuck on 3: 20 mod 3 is not 0, so it would never move on.',32,700,MUTED),'fade')
put(f'{L}-teachplan',sec(f'{L}-teachplan','60–61 MIN',body,'Teach before worksheet page 2 (Q6). The workbook puts the blocks in a jumble for factors of 40. Point out the three things in order: set up (hat and set d), the loop, and what goes inside the loop (if, then say, then change d). With plain say (no seconds) the loop is so fast that only the last number stays on screen, so use say for 1 seconds. The classic bug: change d by 1 inside the if. Python (optional):\nfor d in range(1, 21):\n    if 20 % d == 0:\n        print(d)\nPrints 1, 2, 4, 5, 10, 20.'))
put(f'{L}-ws2',ws_preview(f'{L}-ws2','61–72 MIN','Worksheet page 2: on your own',[('Q3','Trace the factor counter for 6, then think about 13.'),('Q4','Goldbach pairs for 24, and why 27 cannot work.'),('Q5','Numbers up to 30 with exactly 3 factors.'),('Q6','Plan your code: factors of 40.')],'Write on paper first, then test in Scratch. Finished early? Stretch and Challenge come next.','Children work alone. Let them test Q3 and Q6 in Scratch AFTER writing their prediction. Note who needs a short catch-up next lesson.'))
put(f'{L}-ws2ans',check(f'{L}-ws2ans','72–75 MIN','Page 2: check together',[('Q3','count: 1, 2, 3, 3, 3, 4. Says 4. For 13 it says 2: 13 is prime.'),('Q4','24 = 5 + 19 = 7 + 17 = 11 + 13.  27: needs a 2, but 25 is not prime.'),('Q5','4, 9, 25: squares of primes (2², 3², 5²).'),('Q6','E, C, B [ F [ A ], D ].  It says 8 numbers, one per second: 1, 2, 4, 5, 8, 10, 20, 40.')],
 'Click after a child explains. Q3: 6 mod d: 0, 0, 0, 2, 1, 0 (d = 1 to 6). Q4: the only even prime is 2, so an odd total needs 2 + an odd prime; 27 − 2 = 25 = 5 × 5. Q5: 16 has five factors and 36 has nine, so not every square works: only a prime times itself (factors 1, p, p × p). Q6: set d to 1 comes before the loop; the if is inside the loop, say inside the if, and change d by 1 inside the loop but after the if.',size=32,gap=155,top=240))

# ---------- stretch, challenge ----------
import p6_th
st=p6_th.pairs(2)
put(f'{L}-stretch',sec(f'{L}-stretch','For early finishers',h2('Stretch')+''.join(talkcard(a,b,30) for a,b in st),p6_th.answers(2)))
ch=[('1.','Find the smallest number that can be divided exactly by 2, 3, 4, 5 and 6.'),('2.','1001 = 7 × 11 × 13. Use this to write 3003 and 5005 as products of primes.')]
put(f'{L}-challenge',sec(f'{L}-challenge','Challenge',h2('Challenge')+''.join(talkcard(a,b,38) for a,b in ch),'Pairs try first, then the "see it" slide, then the walk-through. Answers: 1) 60 (2 × 2 × 3 × 5). 2) 3003 = 3 × 7 × 11 × 13 and 5005 = 5 × 7 × 11 × 13.'))
def box(x,y,w,t,col=WHITE,fs=34):
    return f'<rect x="{x}" y="{y}" width="{w}" height="66" rx="12" fill="{col}" stroke="{NAVY}" stroke-width="3"/><text x="{x+w/2}" y="{y+45}" font-size="{fs}" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="Fredoka, Arial">{t}</text>'
g=''
for i,(n,s) in enumerate([(2,'2'),(3,'3'),(4,'2 × 2'),(5,'5'),(6,'2 × 3')]):
    g+=box(20,20+i*76,90,str(n),YEL)+f'<text x="130" y="{66+i*76}" font-size="34" font-weight="700" fill="{NAVY}" font-family="Fredoka, Arial">=</text>'+box(160,20+i*76,200,s,SKY)
g+=f'<text x="400" y="200" font-size="32" font-weight="800" fill="{TEAL}" font-family="Nunito Sans, Arial">Which primes does the</text><text x="400" y="240" font-size="32" font-weight="800" fill="{TEAL}" font-family="Nunito Sans, Arial">number need, and how</text><text x="400" y="280" font-size="32" font-weight="800" fill="{TEAL}" font-family="Nunito Sans, Arial">many of each?</text>'
q1=f'<svg aria-label="The numbers 2 to 6 each written as a product of primes" viewBox="0 0 760 420" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;display:block">{g}</svg>'
g=box(250,10,260,'1001 = 7 × 11 × 13',SKY,30)+box(40,130,200,'3003 = 3 × ?',WHITE,30)+box(520,130,200,'5005 = 5 × ?',WHITE,30)+f'<line x1="330" y1="76" x2="140" y2="130" stroke="{NAVY}" stroke-width="3"/><line x1="430" y1="76" x2="620" y2="130" stroke="{NAVY}" stroke-width="3"/>'
g+=f'<text x="380" y="280" font-size="32" font-weight="800" text-anchor="middle" fill="{TEAL}" font-family="Nunito Sans, Arial">3003 ÷ 1001 = ?   5005 ÷ 1001 = ?</text>'
q2=f'<svg aria-label="1001 written as 7 times 11 times 13 with 3003 and 5005 as multiples of 1001" viewBox="0 0 760 340" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;display:block">{g}</svg>'
body=h2('Challenge: see it',60)+'<div style="display:flex;gap:32px;align-items:flex-start">'+card(f'<p style="font-size:28px;font-weight:700;color:{TEAL}">Q1: Divisible by 2, 3, 4, 5 and 6</p>'+q1,extra='flex:1;min-width:0;padding:20px 24px')+card(f'<p style="font-size:28px;font-weight:700;color:{TEAL}">Q2: Using 1001</p>'+q2,extra='flex:1;min-width:0;padding:20px 24px')+'</div>'
put(f'{L}-chdiag',sec(f'{L}-chdiag','Challenge',body,'Show after pairs have tried, or if they are stuck. The pictures show the problem, not the answer. Ask: What do you notice? Q1: a number divisible by 4 must contain how many 2s? Q2: 3003 is how many 1001s?'))
body=h2('Challenge: walk-through')+pin(128,250,800,p('Q1: list the prime parts',36,800,TEAL))
for i,t in enumerate(['4 needs 2 × 2 (two 2s)','6 = 2 × 3, so 3 is needed; 2 is already there','5 needs a 5','2 × 2 × 3 × 5 = 60. Check: 60 ÷ 4 = 15, 60 ÷ 6 = 10']): body+=pin(128,330+i*120,800,p(t,30),'rise',WHITE)
body+=pin(992,250,800,p('Q2: 3003 = 3 × 1001',36,800,TEAL))
for i,t in enumerate(['3003 ÷ 1001 = 3','So 3003 = 3 × 7 × 11 × 13','5005 ÷ 1001 = 5','So 5005 = 5 × 7 × 11 × 13']): body+=pin(992,330+i*120,800,p(t,30),'rise',WHITE)
put(f'{L}-chwalk',sec(f'{L}-chwalk','Challenge',body,'Use after pairs have tried. Q1: this is the lowest common multiple, found with primes: take the most of each prime that any of the numbers needs. 60 is the smallest. Q2: 3 and 5 are prime, so no more splitting is needed. Python (optional) to check Q1:\nn = 1\nwhile not all(n % k == 0 for k in range(2, 7)):\n    n = n + 1\nprint(n)\nPrints 60.'))
body=h2('Talk time')+card(chip('TALK TIME',YEL,NAVY)+p('Why does a square number like 36 have an odd number of factors, when most numbers have an even number?',42,600))+card(p('Sentence starters:',34,400,MUTED)+p('“I noticed that …”   “I tested it by …”   “I know because …”',38,600))
put(f'{L}-talk',sec(f'{L}-talk','75–82 MIN',body,'Minutes 75 to 82. Pairs talk for 2 minutes, then share. Listen for: factors come in pairs that multiply to the number, so the count is usually even. For a square number one pair is a number times itself (6 × 6), counted once, so the total is odd. Extension: is there a biggest prime? (No. Euclid showed this about 2300 years ago: a secondary-school teaser.)'))
body=h2('Exit ticket')+card(chip('EXIT TICKET')+p('(a) Is 111 prime? Show your test.',46,600)+p('(b) Write 66 as a product of primes.',46,600)+p('(c) Optional: is 133 prime?',38,600,MUTED))+card(p('Write your answers on paper. Show your tutor, then collect your stamp.',34))
put(f'{L}-exit',sec(f'{L}-exit','82–90 MIN',body,'Minutes 82 to 90. Answers: (a) No. 1 + 1 + 1 = 3, so 3 divides it: 111 = 3 × 37. (b) 66 = 2 × 3 × 11. (c) Optional: 133 is not prime, 7 × 19 = 133. Extension: put the prime checker inside a second loop so n goes 1, 2, 3, … 100 and the sprite says only the primes. It should find 25 primes, like the sieve.'))

order=[f'{L}-{x}' for x in ['title','warm1','warm2','explore1','explore2','teach1','we1','try1','we2','we3','key','break','ws1','ws1ans','teachtrace','teachgold','teachsq','teachplan','ws2','ws2ans','stretch','challenge','chdiag','chwalk','talk','exit']]
assert set(order)==set(S), set(order)^set(S)
for f in os.listdir(os.path.join(D,'slides')):
    if f.endswith('.html') and f[:-5] not in S: os.remove(os.path.join(D,'slides',f))
for i,h in S.items(): open(os.path.join(D,'slides',i+'.html'),'w').write(h)
deck={'v':4,'createdOnFiles':{'v':1,'at':datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')},'lists':'css',
      'title':'Math Inquirers Level 6: Lesson 2 – Prime Hunters','order':order,'cover':f'{L}-title',
      'sections':{'s1':{'description':'Warm-up and explore','start':f'{L}-title'},'s2':{'description':'Teach: factors, primes and prime factors, tested in code','start':f'{L}-teach1'},'s3':{'description':'Worksheet with teaching before each page','start':f'{L}-break'},'s4':{'description':'Stretch, challenge, talk and exit','start':f'{L}-stretch'}},
      'faces':{'fredoka':{'family':'Fredoka','href':'https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&display=swap'},'nunito-sans':{'family':'Nunito Sans','href':'https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@400;600;700&display=swap'}},'designSystems':[]}
json.dump(deck,open(os.path.join(D,'deck.json'),'w'),indent=1,ensure_ascii=False)
print(len(order),'slides')

import p6_gaps; p6_gaps.apply(2)

import p6_stories; p6_stories.apply(2)
