"""Math Inquirers P3, Lesson 2: Cryptarithm Crackers. Writes split/p3l2/project (deck.json + slides/*.html)."""
import json,os,sys,datetime
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,H)
import slidekit
from slidekit import *
slidekit.FOOT='Math Inquirers P3 Holiday Program  •  Notice it. Test it. Explain why.'
D=os.path.join(H,'..','split','p3l2','project'); S={}
def put(i,h): S[i]=h
LN=2; TITLE='Cryptarithm Crackers'; TOPIC='Addition and Subtraction'; PRE='p3l2-'
def ol(items,size=34): return f'<ol style="font-size:{size}px;font-weight:600;padding-left:48px;display:flex;flex-direction:column;gap:8px">'+''.join(f'<li>{E(x)}</li>' for x in items)+'</ol>'
def numcard(n,text,size=38): return card(p(f'<span style="color:{TEAL}">{n}</span>  {E(text)}',size,600,raw=True))
def check2(sid,time,title,rows,notes,gap=150,size=34,lw=170):
    body=h2(title)
    for i,(a,b) in enumerate(rows):
        top=250+i*gap
        body+=pin(128,top,lw-20,f'<p style="font-size:36px;font-weight:800;color:{TEAL}">{E(a)}</p>',None,WHITE,20,'18px 24px')
        body+=pin(128+lw,top,1664-lw,f'<p style="font-size:{size}px;font-weight:800;line-height:1.25">{E(b)}</p>','pop',YEL,20,'16px 26px')
    return sec(sid,time,body,notes)
def title_slide(sid,today,notes):
    return (f'<section id="{sid}" data-transition="fade" style="background:{NAVY};color:{CREAM};font-family:{BF};padding:128px 128px 160px;display:flex;flex-direction:column;justify-content:center;gap:36px">\n'
            f'<p style="font-size:32px;font-weight:700;letter-spacing:4px;color:{YEL}">PRIMARY 3  •  LESSON {LN}  •  WEEK 1</p>\n'
            f'<h1 style="font-family:{HF};font-size:128px;font-weight:600;line-height:1.05">{E(TITLE)}</h1>\n'
            f'<p style="font-size:44px;color:#C9D4EC">{E(TOPIC)}</p>\n'
            f'<div style="background:#26385F;border-radius:24px;padding:40px;display:flex;flex-direction:column;gap:12px"><p style="font-size:28px;font-weight:700;letter-spacing:3px;color:{YEL}">TODAY WE WILL</p><p style="font-size:44px;font-weight:600">{E(today)}</p></div>\n'
            f'<p style="position:absolute;left:128px;bottom:64px;width:1400px;font-size:24px;color:#B7C3DD">{E(slidekit.FOOT)}</p>\n<aside>{E(notes)}</aside>\n</section>\n')
def break_slide(sid,text,notes):
    return (f'<section id="{sid}" data-transition="fade" style="background:{TEAL};color:{CREAM};font-family:{BF};padding:128px 128px 160px;display:flex;flex-direction:column;justify-content:center;gap:36px">\n'
            f'<p style="font-size:32px;font-weight:700;letter-spacing:4px;color:{YEL}">35–40 MIN</p>\n<h2 style="font-family:{HF};font-size:110px;font-weight:600;line-height:1.05">Brain break</h2>\n'
            f'<p style="font-size:48px;font-weight:600">{E(text)}</p>\n<p style="font-size:36px;color:#D7EFEA">Then: a drink of water and back to our seats.</p>\n'
            f'<p style="position:absolute;left:128px;bottom:64px;width:1400px;font-size:24px;color:#D7EFEA">{E(slidekit.FOOT)}</p>\n<aside>{E(notes)}</aside>\n</section>\n')
# ---------- SVG pieces ----------
def cards_svg(ds,cw=110,ch=140,gap=24,label=None,hi=()):
    w=len(ds)*cw+(len(ds)-1)*gap+8; h=ch+8
    s=f'<svg aria-label="{E(label or "Digit cards "+", ".join(ds))}" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="width:{w}px;height:{h}px;flex:none">'
    for i,d in enumerate(ds):
        x=4+i*(cw+gap)
        s+=f'<rect x="{x}" y="4" width="{cw}" height="{ch}" rx="16" fill="{SKY if i in hi else YEL}" stroke="{NAVY}" stroke-width="5"/><text x="{x+cw/2}" y="{4+ch*0.7:.0f}" font-size="{int(ch*0.55)}" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="Fredoka, Arial">{E(d)}</text>'
    return s+'</svg>'

RED='#D64545'
import base64,tempfile
sys.path.insert(0,os.path.join(H,'..'))
from levels.diagrams import column_png
LC={'A':'#FFC93C','B':'#7DC4F0','C':'#96D28C','D':'#F09678','E':'#BEA0E6','F':'#F0AAC8'}
def col_img(rows,op,result,height=330,cell=110,alt='Column sum with letters for digits'):
    fp=tempfile.mktemp(suffix='.png'); column_png(fp,rows,op,result,cell=cell)
    b=base64.b64encode(open(fp,'rb').read()).decode(); os.remove(fp)
    return f'<img alt="{E(alt)}" src="data:image/png;base64,{b}" style="height:{height}px;width:auto;flex:none;align-self:center">'
# ---------- SVG pieces ----------
def shape(k,cx,cy,r):
    if k=='C': return f'<circle cx="{cx}" cy="{cy}" r="{r*0.8:.1f}" fill="{TEAL}" stroke="{NAVY}" stroke-width="4"/>'
    if k=='T': return f'<polygon points="{cx},{cy-r} {cx+r*0.95:.1f},{cy+r*0.75:.1f} {cx-r*0.95:.1f},{cy+r*0.75:.1f}" fill="{RED}" stroke="{NAVY}" stroke-width="4" stroke-linejoin="round"/>'
    if k=='D': return f'<polygon points="{cx},{cy-r} {cx+r*0.8:.1f},{cy} {cx},{cy+r} {cx-r*0.8:.1f},{cy}" fill="{SKY}" stroke="{NAVY}" stroke-width="4" stroke-linejoin="round"/>'
    if k=='Q': return f'<rect x="{cx-r*0.75:.1f}" y="{cy-r*0.75:.1f}" width="{r*1.5:.1f}" height="{r*1.5:.1f}" rx="4" fill="#B9A6F2" stroke="{NAVY}" stroke-width="4"/>'
    import math
    pts=' '.join(f'{cx+(r if i%2==0 else r*0.42)*math.cos(math.pi/5*i-math.pi/2):.1f},{cy+(r if i%2==0 else r*0.42)*math.sin(math.pi/5*i-math.pi/2):.1f}' for i in range(10))
    return f'<polygon points="{pts}" fill="{YEL}" stroke="{NAVY}" stroke-width="4" stroke-linejoin="round"/>'
def colsum_svg(rows,op,cw=88,rh=100,label='Column sum',fill=None,scale=1.0):
    """rows: strings right-aligned; '?' empty box; S C T D Q shapes; fill: list of strings (same shape) giving digits to write in the boxes"""
    cols=max(len(r) for r in rows); W=70+cols*cw+10; Hh=len(rows)*rh+30
    s=f'<svg aria-label="{E(label)}" viewBox="0 0 {W} {Hh}" xmlns="http://www.w3.org/2000/svg" style="width:{W*scale:.0f}px;height:{Hh*scale:.0f}px;flex:none">'
    for i,r in enumerate(rows):
        last=i==len(rows)-1; y=6+i*rh+(24 if last else 0)
        rr=r.rjust(cols); ff=(fill[i].rjust(cols) if isinstance(fill,list) else ' '*cols)
        for j,ch in enumerate(rr):
            x=70+j*cw
            if ch=='?':
                s+=f'<rect x="{x+6}" y="{y}" width="{cw-12}" height="{rh-16}" rx="10" fill="{SOFT if isinstance(fill,list) else WHITE}" stroke="{NAVY}" stroke-width="4"/>'
                if isinstance(fill,list) and ff[j]!=' ': s+=f'<text x="{x+cw/2}" y="{y+rh-38}" font-size="{int(rh*0.58)}" font-weight="700" text-anchor="middle" fill="{TEAL}" font-family="Fredoka, Arial">{ff[j]}</text>'
            elif ch in 'ABCDEF':
                dig=fill.get(ch) if isinstance(fill,dict) else None
                s+=f'<rect x="{x+6}" y="{y}" width="{cw-12}" height="{rh-16}" rx="10" fill="{SOFT if dig else LC[ch]}" stroke="{NAVY}" stroke-width="4"/><text x="{x+cw/2}" y="{y+rh-38}" font-size="{int(rh*0.58)}" font-weight="700" text-anchor="middle" fill="{TEAL if dig else NAVY}" font-family="Fredoka, Arial">{dig or ch}</text>'
            elif ch!=' ': s+=f'<text x="{x+cw/2}" y="{y+rh-38}" font-size="{int(rh*0.58)}" font-weight="600" text-anchor="middle" fill="{NAVY}" font-family="Fredoka, Arial">{E(ch)}</text>'
        if i==len(rows)-2:
            s+=f'<text x="36" y="{y+rh-38}" font-size="{int(rh*0.6)}" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="Fredoka, Arial">{E(op)}</text><line x1="10" y1="{y+rh+2}" x2="{W-6}" y2="{y+rh+2}" stroke="{NAVY}" stroke-width="5"/>'
    return s+'</svg>'
def grid_svg(vals,c=150,label='Magic square',hi=()):
    W=3*c+8; s=f'<svg aria-label="{E(label)}" viewBox="0 0 {W} {W}" xmlns="http://www.w3.org/2000/svg" style="width:{W}px;height:{W}px;flex:none">'
    for i,v in enumerate(vals):
        x=4+(i%3)*c; y=4+(i//3)*c
        s+=f'<rect x="{x}" y="{y}" width="{c}" height="{c}" fill="{SOFT if i in hi else (SKY if v!="" else WHITE)}" stroke="{NAVY}" stroke-width="5"/>'
        if v!='': s+=f'<text x="{x+c/2}" y="{y+c/2+18}" font-size="52" font-weight="700" text-anchor="middle" fill="{TEAL if i in hi else NAVY}" font-family="Fredoka, Arial">{v}</text>'
    return s+'</svg>'
def pyr_svg(vals,bw=200,bh=84,label='Number pyramid',hi=()):
    pos=[(bw,0),(bw/2,bh),(1.5*bw,bh),(0,2*bh),(bw,2*bh),(2*bw,2*bh)]
    W=3*bw+8; Hh=3*bh+8
    s=f'<svg aria-label="{E(label)}" viewBox="0 0 {W} {Hh}" xmlns="http://www.w3.org/2000/svg" style="width:{W}px;height:{Hh}px;flex:none">'
    for i,(x,y) in enumerate(pos):
        v=vals[i]
        s+=f'<rect x="{x+4}" y="{y+4}" width="{bw}" height="{bh}" fill="{SOFT if i in hi else (SKY if v!="" else WHITE)}" stroke="{NAVY}" stroke-width="5"/>'
        if v!='': s+=f'<text x="{x+4+bw/2}" y="{y+4+bh/2+16}" font-size="46" font-weight="700" text-anchor="middle" fill="{TEAL if i in hi else NAVY}" font-family="Fredoka, Arial">{v}</text>'
    return s+'</svg>'
def digit_cards(ds,cw=80,ch=100,gap=16,label=None):
    w=len(ds)*cw+(len(ds)-1)*gap+8
    s=f'<svg aria-label="{E(label or "Digit cards "+", ".join(ds))}" viewBox="0 0 {w} {ch+8}" xmlns="http://www.w3.org/2000/svg" style="width:{w}px;height:{ch+8}px;flex:none">'
    for i,d in enumerate(ds):
        x=4+i*(cw+gap); s+=f'<rect x="{x}" y="4" width="{cw}" height="{ch}" rx="12" fill="{YEL}" stroke="{NAVY}" stroke-width="4"/><text x="{x+cw/2}" y="{4+ch*0.72:.0f}" font-size="{int(ch*0.58)}" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="Fredoka, Arial">{d}</text>'
    return s+'</svg>'

# ---------- title ----------
put(PRE+'title',title_slide(PRE+'title','Crack missing digits one column at a time, check subtraction by adding, and solve magic squares and shape puzzles.',
 'Objective: Find missing digits in 4-digit addition and subtraction by working column by column from the ones; check subtraction by adding and work backwards in magic squares and number pyramids (heuristic: work backwards); use guess, check and improve for digit-card and shape puzzles (heuristic: guess and check). '
 'Materials: Digit cards 0–9 (one set per child), mini whiteboards, a printed 3 × 3 grid, counters or small paper squares to move around. '
 'Online: Children use the cut-out digit cards at the back of the workbook (or paper squares numbered 0–9) and draw the grids on paper. Share the screen for the column sums and write on them. '
 'Time plan: warm-up 0 to 10, explore 10 to 25, teaching 25 to 35 (click to reveal each step and answer), brain break 35 to 40, worksheet 40 to 70 with short teaching before each page and a check-together slide after it, talk time 70 to 80, exit ticket 80 to 90. If the class is behind, children finish the last question of each page at home; the check slides cover it.'))
# ---------- warm-up 1: make 1000 ----------
pairs=[('350','650'),('720','280'),('105','895'),('999','1'),('460','540'),('75','925')]
body=h2('Warm-up: Make 1000')+p('What goes with each number to make 1000? Write it, then hold it up.',36,600,MUTED)
CW=533
for i,(a,b) in enumerate(pairs):
    L=128+(i%3)*(CW+32); T=290+(i//3)*300
    inner=f'<p style="font-family:{HF};font-size:96px;font-weight:600;line-height:1">{a} + ?</p>'
    body+=pin(L,T,CW,inner,None,WHITE,24,'28px 32px',f'box-sizing:border-box;height:270px;border:4px solid {NAVY};box-shadow:8px 8px 0 {NAVY}')
    body+=pin(L+24,T+160,CW-48,f'<p style="font-size:40px;font-weight:800;line-height:1.2">{E(b)}</p>','pop',SOFT,16,'12px 20px',f'box-sizing:border-box;border:3px solid {NAVY}')
put(PRE+'warm1',sec(PRE+'warm1','0–5 MIN',body,
 'Minutes 0 to 5. Make 1000. Point to one card at a time; children write the missing number on their whiteboards and hold them up together; click to reveal (order: 350, 720, 105, 999, 460, 75). Answers: 650, 280, 895, 1, 540, 925. '
 'Ask: "How did you work out 720?" Good ways: count on to the next hundred (720 → 800 is 80) then to 1000 (200 more), so 280; or use bonds of 10 for each place. For 105 watch for 995 (it is 895: 105 + 895 = 1000). '
 'Quick finisher: "Make 10 000 with 3500." (6500)'))
qs=[('1.','3456 + 1000 = ?','4456'),('2.','5000 − 1 = ?','4999'),('3.','2700 + 300 = ?','3000'),('4.','8000 − 2500 = ?','5500'),('5.','4999 + 2 = ?','5001')]
body=h2('Quick questions')+''.join(qrow(128,250+i*125,1250,a,b) for i,(a,b,c) in enumerate(qs))+''.join(answer(1420,250+i*125,372,c) for i,(a,b,c) in enumerate(qs))
put(PRE+'warm2',sec(PRE+'warm2','5–10 MIN',body,'Minutes 5 to 10. Mental maths, no written working. Whiteboards up together, then click. Ask for 2: "Which digits changed when we took away 1? Why did so many change?" (every 0 had to be exchanged). For 5: 4999 + 1 = 5000, then 1 more.'))
# ---------- explore ----------
def explore_pic():
    cards=digit_cards(list('123456789'),cw=70,ch=86,gap=14)
    return f'<div style="display:flex;align-items:center;justify-content:space-around;gap:40px">{cards}{colsum_svg(["???","???","???"],"+",cw=64,rh=72,label="Empty sum: three boxes plus three boxes equals three boxes")}</div>'
body=h2('Explore: what to do')+card(chip('EXPLORE')+ol(['Take the digit cards 1 to 9.','Make two 3-digit numbers that add up to a 3-digit number, using every card once.','Check the sum by adding.','Find more. What is always true?'],34))+card(explore_pic(),extra='padding:16px 32px')
put(PRE+'explore1',sec(PRE+'explore1','10–15 MIN',body,'Minutes 10 to 15. Pairs work with the digit cards 1 to 9 (online: paper squares). Ask them to predict first: "Many ways, a few, or none?" Each card is used once, so the nine boxes use all nine digits. Hints: "Put small digits in the hundreds of the two numbers you add, like 1 and 2." "A digit repeats? Swap two cards and add again." Two examples to keep in your pocket: 173 + 286 = 459 and 218 + 349 = 567. Finished early: "Add the digits of your answer. Compare with another pair."'))
body=h2('Explore: talk about it')+numcard('1.','How many sums did you find? Read one out.',40)+numcard('2.','How many times did you carry in your sum?',40)+numcard('3.','Add the digits of your answer. What do you notice?',40)
put(PRE+'explore2',sec(PRE+'explore2','15–25 MIN',body,'Minutes 15 to 25. Let pairs keep working, then gather them and collect sums on the board. Answers: 1) There are many: 168, if 173 + 286 and 286 + 173 count once. 2) Exactly once, every time. 3) The digits of the answer always add up to 18 (4 + 5 + 9 = 18, 5 + 6 + 7 = 18). Do not explain why in full; just say: "Mathematicians can prove this is ALWAYS true. Notice it, test it, explain why!" Strong children: "Can the answer be less than 400?" (No: the smallest answer is 459.)'))
# ---------- teach: missing digits ----------
r1=['4A68','17B5','C043']
body=h2('Missing digits: start at the ones')+pin(128,250,620,colsum_svg(r1,'+',cw=100,rh=110,label='4 box 6 8 plus 1 7 box 5 equals box 0 4 3'),None,WHITE,24,'16px 20px')
body+=pin(128,250,620,colsum_svg(r1,'+',cw=100,rh=110,label='Solved: 4268 plus 1775 equals 6043',fill={'A':'2','B':'7','C':'6'}),'fade',WHITE,24,'16px 20px')
for i,t in enumerate(['Ones: 8 + 5 = 13. Write 3, carry 1.','Tens: 6 + B + 1 must end in 4. 6 + 7 + 1 = 14, so B = 7. Carry 1.','Hundreds: A + 7 + 1 must end in 0. 2 + 7 + 1 = 10, so A = 2. Carry 1.','Thousands: 4 + 1 + 1 = 6, so C = 6.']):
    body+=step(i+1,t,left=820,top=250+i*130,width=972,size=32)
body+=answer(128,780,1664,'4268 + 1775 = 6043   Check: add again ✓')
put(PRE+'teach1',sec(PRE+'teach1','25–27 MIN',body,'Teach. Click once for each step; the solved sum fades in over the puzzle, then the answer. Think-aloud: "I start at the ones, because nothing is carried into the ones. 8 + 5 = 13. I write 3 and carry 1. Tens: 6 + B + the carried 1 must end in 4. 6 + 1 is 7, and 7 + 7 = 14, so B is 7 and I carry 1 again. Hundreds: A + 7 + 1 must end in 0, so it makes 10: A is 2. Thousands: 4 + 1 + 1 = 6." Ask: "Why not start at the thousands?" (we do not know yet if something is carried into it).'))
put(PRE+'try1',try_slide(PRE+'try1','27–28 MIN','Your turn: missing digits','Start at the ones. Write the carry.',[('a','3A5 + 24B = 621','375 + 246'),('b','C6 + 5D = 123','66 + 57'),('c','6A4 − B58 = 296','654 − 358')],'Whiteboards. a) Ones 5 + B ends in 1, so 5 + 6 = 11, B = 6, carry 1. Tens A + 4 + 1 ends in 2, so A = 7. Hundreds 3 + 2 + 1 = 6 ✓. b) 6 + D ends in 3: 6 + 7 = 13, D = 7. Tens C + 5 + 1 = 12, so C = 6. c) is a preview of the next slide: turn it round, 296 + B58 = 6A4. Ones 6 + 8 = 14, carry 1. Tens 9 + 5 + 1 = 15, so A = 5, carry 1. Hundreds 2 + B + 1 = 6, so B = 3.',size=38))
r2=['6A02','B35C','1947']; r2b=['1947','B35C','6A02']
body=h2('Work backwards: check subtraction by adding')+pin(128,250,560,colsum_svg(r2,'−',cw=90,rh=100,label='6 box 0 2 minus box 3 5 box equals 1947'),None,WHITE,24,'14px 18px')
body+=pin(128,250,560,colsum_svg(r2b,'+',cw=90,rh=100,label='Turned round: 1947 plus box 3 5 box equals 6 box 0 2'),'fade',SOFT,24,'14px 18px')
for i,t in enumerate(['Undo it: 6A02 − B35C = 1947 means 1947 + B35C = 6A02.','Ones: 7 + C ends in 2: 7 + 5 = 12, so C = 5. Carry 1.','Tens: 4 + 5 + 1 = 10. Hundreds: 9 + 3 + 1 = 13, so A = 3.','Thousands: 1 + B + 1 = 6, so B = 4.']):
    body+=step(i+1,t,left=760,top=250+i*130,width=1032,size=32)
body+=answer(128,780,1664,'6302 − 4355 = 1947   Check: 1947 + 4355 = 6302 ✓')
put(PRE+'teach2',sec(PRE+'teach2','28–30 MIN',body,'Teach the heuristic WORK BACKWARDS: subtraction and addition undo each other. Click 1 turns the subtraction into an addition (the picture changes). Think-aloud: "Subtracting with missing digits on top is hard, because I would have to exchange without knowing the digit. So I undo it: the answer plus the number taken away gives back the first number." Common error: looking for a digit that can be taken from 2 to leave 7. There is none; it must be 12 − 5 = 7.'))
# guess check improve
W3=[300,300,260]
body=h2('Guess, check, improve')+card(p('Use 1, 2, 3, 4 once each to make two 2-digit numbers with the SMALLEST difference.',38,700))
body+=trow(128,400,['Try','Numbers','Difference'],W3,None,True)
for i,r in enumerate([['1st guess','43 − 21','22'],['Improve','42 − 31','11'],['Improve again','31 − 24','7']]):
    body+=trow(128,490+i*90,r,W3,'rise')
body+=pin(1180,400,612,p('Make the tens digits next to each other: 3 and 2.',34,700),'fade',WHITE,20,'20px 24px')
body+=pin(1180,560,612,p('The bigger number gets the SMALL ones digit, the smaller number gets the BIG one.',34,700),'fade',SOFT,20,'20px 24px')
body+=answer(128,790,1664,'Smallest difference: 31 − 24 = 7')
put(PRE+'teach3',sec(PRE+'teach3','30–33 MIN',body,'Teach the heuristic GUESS AND CHECK, then IMPROVE. Click for each row and note. Think-aloud: "First guess 43 − 21 = 22. Can I do better? The tens make the biggest difference, so the tens digits should be next to each other, like 3 and 2." Row 2: 42 − 31 = 11, better. Row 3: try the tens 3 and 2 with the ones swapped round. "Now the bigger number, 3_, should have the smallest ones digit left, 1, and the smaller number, 2_, the biggest, 4: 31 − 24 = 7." Check other pairs quickly: 41 − 32 = 9, 21 − 14 is not allowed (1 twice). So 7 is the smallest.'))
put(PRE+'try2',try_slide(PRE+'try2','33–34 MIN','Your turn: guess, check, improve','Use each card once. Make two 2-digit numbers.',[('a','Cards 1, 2, 3, 4: the GREATEST sum','41 + 32 = 73'),('b','Cards 1, 2, 3, 4: the SMALLEST sum','13 + 24 = 37'),('c','Cards 2, 4, 5, 8: the smallest difference','52 − 48 = 4')],'Whiteboards. a) The big digits go in the tens: 4 and 3 tens, then 2 and 1 ones: 73 (42 + 31 is also 73). b) The small digits go in the tens: 37 (14 + 23 is also 37). c) Tens next to each other: 5 and 4; bigger number gets the smaller ones digit 2, smaller number gets 8: 52 − 48 = 4. Other tries: 82 − 54 = 28, 45 − 28 = 17.',size=36))
body=h2('Key idea: one column at a time')+card(p('Start at the ones and carry to the left. Check subtraction by adding. Stuck? Guess, check, then improve.',44,700))+card(p('A puzzle is cracked when you can say why it is the ONLY answer.',38,600,MUTED))
put(PRE+'key',sec(PRE+'key','34–35 MIN',body,'Say the key idea together. Common mistakes to watch for during the worksheet: (1) Forgetting the carried 1 when working out the missing digit in the next column. (2) In subtraction, looking for a digit that can be taken from 3 to leave 8 (there is none) instead of regrouping: 13 − 5 = 8. (3) Magic squares: guessing numbers instead of finding a full line first to get the total.'))
put(PRE+'break',break_slide(PRE+'break','Code-breaker moves. I say a digit: odd means hop on one foot that many times, even means clap that many times, 0 means freeze!','Five minutes. Try 3, 8, 0, 5, 2. Online: children stay in view of the camera and move in place.'))
put(PRE+'ws1',ws_preview(PRE+'ws1','40–52 MIN','Worksheet page 1: with your partner',[('Q1','Missing digits. Start at the ones. For (b), turn it round and add.'),('Q2','Digit cards 1 to 6: greatest sum, smallest sum, smallest difference.')],'Use digit cards for Q2: move them, then write your tries.','Minutes 40 to 52. Walk around. Ask "Which column did you start with?" and "Is there a carry coming in?" For Q2c ask: "Which hundreds digits should you try? Why?" Expect several tries; praise improving a guess.'))
put(PRE+'ws1ans',check2(PRE+'ws1ans','52–54 MIN','Page 1: check together',[
 ('Q1','a) 3447 + 2578 = 6025     b) 7003 − 4465 = 2538     c) 2538 + 4465 = 7003'),
 ('Q2','a) 1173, e.g. 642 + 531     b) 381, e.g. 135 + 246     c) 47:  412 − 365')],
 'Click each answer after a pair explains. Q1a: ones 7 + 8 = 15, carry 1; tens 4 + the missing digit + 1 ends in 2, so 7 (12), carry 1; hundreds the missing digit + 5 + 1 ends in 0, so 4, carry 1; thousands 3 + 2 + 1 = 6. Q1b: turn it round, 2538 + the second number = the first number; ones 8 + the missing ones digit ends in 3, so 5; tens 3 + 6 + 1 = 10; hundreds 5 + 4 + 1 = 10, so the missing hundreds digit on top is 0; thousands 2 + the missing digit + 1 = 7, so 4. Q2a: big digits in the hundreds (6, 5), then tens (4, 3), then ones (2, 1). Q2c: hundreds 4 and 3 (next to each other); 4 gets the smallest ones left (1, 2), 3 gets the biggest (6, 5): 412 − 365 = 47. It is the only way to get 47.',gap=170,size=36))
# ---------- before page 2 ----------
g0=['80','10','60','','50','','','','']; g1=['80','10','60','','50','','40','','20']; g2=['80','10','60','30','50','70','40','90','20']
body=h2('Magic squares: find a full line first')+pin(128,240,470,grid_svg(g0,label='Magic square: top row 80, 10, 60, centre 50'),None,CREAM,0,'0px')
body+=step(1,'Full line: 80 + 10 + 60 = 150. EVERY line must make 150.',left=660,top=250,width=1132,size=34)
body+=pin(128,240,470,grid_svg(g1,label='Diagonals filled: 40 and 20',hi=(6,8)),'fade',CREAM,0,'0px')
body+=step(2,'Diagonals: 80 + 50 + ? = 150, so 20.   60 + 50 + ? = 150, so 40.',left=660,top=380,width=1132,size=34)
body+=pin(128,240,470,grid_svg(g2,label='Full magic square',hi=(3,5,7)),'fade',CREAM,0,'0px')
body+=step(3,'Now every line has one gap: 150 − 80 − 40 = 30,  150 − 60 − 20 = 70,  150 − 40 − 20 = 90.',left=660,top=510,width=1132,size=34)
body+=pin(660,670,1132,p('Check every row, column and diagonal: 150 ✓',36,800),'pop',YEL,20,'18px 26px')
put(PRE+'teachmagic',sec(PRE+'teachmagic','54–56 MIN',body,'Teach before worksheet page 2 (Q3). This is WORK BACKWARDS again: we know the total, so we take away to find the missing number. Click order: step 1, diagonals appear, step 2, the rest appear, step 3, check. Ask: "Which line should we use next? One with only ONE gap." Do not show the worksheet square.'))
pv0=['2000','','1200','450','','']; pv1=['2000','800','1200','450','','']; pv2=['2000','800','1200','450','350','850']
body=h2('Work backwards: number pyramids')+p('Each brick is the sum of the two bricks under it.',34,600,MUTED)
body+=pin(128,320,620,pyr_svg(pv0,label='Pyramid: top 2000, middle right 1200, bottom left 450'),None,CREAM,0,'0px')
body+=step(1,'Top: 2000 = ? + 1200. Undo: 2000 − 1200 = 800.',left=820,top=320,width=972,size=34)
body+=pin(128,320,620,pyr_svg(pv1,label='Middle left 800 found',hi=(1,)),'fade',CREAM,0,'0px')
body+=step(2,'800 = 450 + ?. Undo: 800 − 450 = 350.',left=820,top=450,width=972,size=34)
body+=step(3,'1200 = 350 + ?. Undo: 1200 − 350 = 850.',left=820,top=580,width=972,size=34)
body+=pin(128,320,620,pyr_svg(pv2,label='Bottom row 450, 350, 850',hi=(4,5)),'fade',CREAM,0,'0px')
body+=answer(820,720,972,'Check by adding up: 450 + 350 = 800 ✓')
put(PRE+'teachpyr',sec(PRE+'teachpyr','56–57 MIN',body,'Teach before worksheet page 2 (Q4). Click through: step, picture, step, step, picture, check. Stress "undo the adding by taking away". For Q4b (equal corner bricks) say only: "If you are stuck, guess a number for the corners, check the top, then improve your guess."'))
body=h2('A pattern for taking from 1000')+card(p('1000 − 372 = ?',48,700))
body+=step(1,'999 − 372: each place is 9 take away a digit, so no exchanging!   9 − 3, 9 − 7, 9 − 2  →  627',top=430,size=34)
body+=step(2,'1000 is 1 more than 999, so the answer is 1 more:  628',top=560,size=34)
body+=pin(128,680,1250,p('Your turn:  1000 − 456 = ?',38,700),None,WHITE,20,'18px 28px')+answer(1420,680,372,'544')
put(PRE+'teach999',sec(PRE+'teach999','57–58 MIN',body,'Teach before worksheet page 2 (Q5). Ask: "Why is 999 − 372 so easy?" (9 is the biggest digit, so we never need to exchange). Check: 628 + 372 = 1000. Your turn: 999 − 456 = 543, plus 1 = 544. Q5 asks children to notice the same pattern with 9999, so do not show 4-digit examples.'))
body=h2('Letter puzzles: what must each letter be?')+pin(128,240,560,col_img(['AB','BA'],'+','CAC',height=330,alt='AB plus BA equals CAC, each letter a different digit'),None,WHITE,24,'14px 18px')
body+=pin(720,240,1072,p('Each letter is a digit. Different letters are different digits.',32,700),None,SOFT,20,'18px 26px')
for i,t in enumerate(['Two 2-digit numbers make less than 200, so C = 1.','Ones: B + A ends in 1, so B + A = 11. Carry 1.','Tens: A + B + 1 = 12. The middle digit of the answer is A, so A = 2. Then B = 9.']):
    body+=step(i+1,t,left=720,top=360+i*125,width=1072,size=32)
body+=answer(128,760,1664,'29 + 92 = 121 ✓   A = 2,  B = 9,  C = 1')
put(PRE+'teachshape',sec(PRE+'teachshape','58–60 MIN',body,'Teach before worksheet page 2 (Q6). Model: "What do I know for sure?" Start with the biggest place (the answer can only start with 1) and the ones column. If children prefer guess and check: "Try A = 1: 19 + 91 = 110, the middle is not 1. Try A = 2: 29 + 92 = 121 ✓." Ask: "Is there another answer?" (No: A + B must be 11 and A must be 2.)'))
put(PRE+'ws2',ws_preview(PRE+'ws2','60–67 MIN','Worksheet page 2: on your own',[('Q3','Magic square. Find a full line first.'),('Q4','Number pyramids. Work backwards. Stuck on (b)? Guess, check, improve.'),('Q5','The 9999 pattern.'),('Q6','If time: letter puzzle. Start at the ones: try 0 and 5.')],'Finished early? Stretch and Challenge come next.','Children work alone. Note who needs a short catch-up next lesson. Q6 hint if needed: "Three of the same digit add up to a number that ends in that same digit. Which digits can do that?"'))
put(PRE+'ws2ans',check2(PRE+'ws2ans','67–69 MIN','Page 2: check together',[
 ('Q3','Total 4500.  1900, 1500, 1100 / 1400, 1300, 1800.  Opposite pairs make 3000.'),
 ('Q4','a) 2375; bottom 1250, 1125, 2475     b) both corners 1500'),
 ('Q5','a) 5872, 7406    b) each place adds up to 9    c) 5873'),
 ('Q6','A = 5,  B = 0,  C = 1:   50 + 50 + 50 = 150')],
 'Click each answer after a child explains. Q3: total 1200 + 1700 + 1600 = 4500; diagonals give 1800 and 1400; then 1900, 1100, 1300. Q4a: 5975 − 3600 = 2375, 2375 − 1250 = 1125, 3600 − 1125 = 2475. Q4b: corners equal; middle bricks are corner + 2000 each; top 7000, so each middle brick is 3500 and each corner 1500. Q6: B + B + B ends in B, so B is 0 or 5. If B = 5, the tens get a carry of 1 and A + A + A + 1 cannot end in A (try them). So B = 0; then A + A + A ends in A, A is not 0, so A = 5 and 15 gives C = 1.',gap=150,size=34))
# ---------- stretch / challenge ----------
st=[('1.','AB + B = BA. Different letters are different digits. Find A and B.'),('2.','Siti worked out 9999 − 3746 = 6253 by taking each digit away from 9. Use her answer to work out 10 000 − 3746 and 10 003 − 3746. How do you know?'),('3.','AA + BB = CBC. Different letters are different digits. Find them.')]
put(PRE+'stretch',sec(PRE+'stretch','For early finishers',h2('Stretch')+''.join(numcard(a,b) for a,b in st),'Answers: 1) A = 8, B = 9: 89 + 9 = 98 (the answer is bigger than the first number by only B, so the tens go up by 1: B = A + 1; ones: B + B = 10 + A; try A = 8). 2) 6254 and 6257 (10 000 is 1 more than 9999, so 1 more than 6253; 10 003 is 4 more than 9999, so 4 more than 6253. Check: 6254 + 3746 = 10 000). 3) A = 9, B = 2, C = 1: 99 + 22 = 121 (C must be 1; ones A + B ends in 1, so they make 11; tens 11 + 1 = 12, so B = 2 and A = 9).'))
ch=[('1.','Use the digit cards 1 to 8 once each to make two 4-digit numbers. Make their difference as small as possible.'),('2.','ABC + ACB = CBA. Different letters are different digits. Find them.')]
put(PRE+'challenge',sec(PRE+'challenge','Challenge',h2('Challenge')+''.join(numcard(a,b,36) for a,b in ch),'Pairs try first, then use the "see it" slide if stuck, then the walk-through. Answers: 1) 247: 5123 − 4876 (the only way to get 247). 2) A = 4, B = 5, C = 9: 459 + 495 = 954 (the only answer).'))
def diag1():
    s='<svg aria-label="Two rows of four empty boxes, one taken from the other, and cards 1 to 8" viewBox="0 0 800 440" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;display:block">'
    for i in range(8):
        x=40+i*92; s+=f'<rect x="{x}" y="10" width="76" height="90" rx="12" fill="{YEL}" stroke="{NAVY}" stroke-width="4"/><text x="{x+38}" y="74" font-size="52" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="Fredoka, Arial">{i+1}</text>'
    for r in range(2):
        for j in range(4):
            x=280+j*100; y=140+r*110; s+=f'<rect x="{x}" y="{y}" width="84" height="94" rx="12" fill="{WHITE}" stroke="{NAVY}" stroke-width="4"/>'
    s+=f'<text x="230" y="320" font-size="64" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="Fredoka, Arial">−</text><line x1="200" y1="358" x2="690" y2="358" stroke="{NAVY}" stroke-width="5"/>'
    s+=f'<text x="485" y="418" font-size="40" font-weight="800" text-anchor="middle" fill="{TEAL}" font-family="Nunito Sans, Arial">as small as possible?</text>'
    return s+'</svg>'
body=h2('Challenge: see it',60)+'<div style="display:flex;gap:32px;align-items:flex-start">'+card(f'<p style="font-size:28px;font-weight:700;color:{TEAL}">Q1: The smallest difference</p>'+diag1(),extra='flex:1;min-width:0;padding:20px 24px')
body+=card(f'<p style="font-size:28px;font-weight:700;color:{TEAL}">Q2: The letter sum</p><div style="display:flex;justify-content:center">'+col_img(['ABC','ACB'],'+','CBA',height=330,alt='ABC plus ACB equals CBA, each letter a different digit')+'</div>',extra='flex:1;min-width:0;padding:20px 24px')+'</div>'
put(PRE+'chdiag',sec(PRE+'chdiag','Challenge',body,'Show after pairs have tried, or if they are stuck. The pictures show the problem, not the answer. Ask: What do you notice? What do we know? Where should we start? Q1: "Which place makes the biggest difference?" Q2: "Look at the tens column: B and C make B again. What must C be?"'))
body=h2('Challenge: walk-through')+pin(128,250,800,p('Q1: guess, check, improve',36,800,TEAL))
for i,t in enumerate(['Thousands digits next to each other, like 5 and 4.','Bigger number: the rest as SMALL as possible: 5123.','Smaller number: the rest as BIG as possible: 4876.','5123 − 4876 = 247. Try 4 and 3: 4125 − 3876 = 249. So 5 and 4 win.']): body+=pin(128,330+i*125,800,p(t,30),'rise',WHITE)
body+=pin(992,250,800,p('Q2: one column at a time',36,800,TEAL))
for i,t in enumerate(['Tens: B + C + carry ends in B, so C + carry = 10. C = 9, carry 1.','Hundreds: A + A + 1 = C = 9, so A = 4.','Ones: C + B = 9 + B ends in A = 4, so B = 5.','459 + 495 = 954 ✓']): body+=pin(992,330+i*125,800,p(t,30),'rise',WHITE)
put(PRE+'chwalk',sec(PRE+'chwalk','Challenge',body,'Use after pairs have tried. Q1: the thousands decide most of the difference, so make them next to each other; then make the bigger number as small as it can be and the smaller number as big as it can be. Trying every neighbouring pair: 2345 − 1876 = 469, 3145 − 2876 = 269, 4125 − 3876 = 249, 5123 − 4876 = 247, 6123 − 5874 = 249, 7123 − 6854 = 269, 8123 − 7654 = 469. Q2: C cannot be 0 (the answer would start with 0), so C + carry = 10 means C = 9. Then the hundreds give A = 4 (4 + 4 + 1 = 9) and the ones give 9 + 5 = 14.'))
body=h2('Talk time')+card(chip('TALK TIME',YEL,NAVY)+p('Why do we always start a missing-digit puzzle at the ones column?',42))+card(p('Sentence starters:',34,400,MUTED)+p('“I noticed that …”   “I tested it by …”   “I know because …”',38))
put(PRE+'talk',sec(PRE+'talk','70–80 MIN',body,'Minutes 70 to 80. Pairs talk for 2 minutes, then share. Answer: a carry moves from right to left, so the ones column is the only one with nothing coming into it. Once we know the ones, we know the carry, and the next column has only one possible digit, and so on. That is also why each puzzle has only one answer. Follow-up: "How did checking by adding help you?" Praise the reasons, not only the answers.'))
body=h2('Exit ticket')+card(chip('EXIT TICKET')+p('Find the missing digits A and B.',44)+'<div style="display:flex;justify-content:center">'+col_img(['3A82','14B9'],'+','5141',height=300,alt='3A82 plus 14B9 equals 5141, A and B are missing digits')+'</div>')+card(p('Write your answer on a slip of paper. Show it to your tutor. Then collect your stamp in your inquiry journal.',34,400))
put(PRE+'exit',sec(PRE+'exit','80–90 MIN',body,'Minutes 80 to 90. Answer: 3682 + 1459 = 5141 (the missing digits are 6 and 5). Ones 2 + 9 = 11, carry 1; tens 8 + B + 1 ends in 4, so B = 5; hundreds A + 4 + 1 ends in 1, so A = 6; thousands 3 + 1 + 1 = 5. Extension: find three sums of two 3-digit numbers with a 3-digit answer that use the digits 1 to 9 once each; add the digits of each answer (always 18).'))

ORDER=['title','warm1','warm2','explore1','explore2','teach1','try1','teach2','teach3','try2','key','break','ws1','ws1ans','teachmagic','teachpyr','teach999','teachshape','ws2','ws2ans','stretch','challenge','chdiag','chwalk','talk','exit']
ORDER=[PRE+x for x in ORDER]
import p3_gifted; ORDER[:]=p3_gifted.add(S,ORDER,2)  # close-the-gaps: warm-up check + look-back slides
assert set(ORDER)==set(S), set(ORDER)^set(S)
os.makedirs(os.path.join(D,'slides'),exist_ok=True)
for f in os.listdir(os.path.join(D,'slides')):
    if f.endswith('.html') and f[:-5] not in S: os.remove(os.path.join(D,'slides',f))
for i,h in S.items(): open(os.path.join(D,'slides',i+'.html'),'w').write(h)
deck={'v':4,'createdOnFiles':{'v':1,'at':datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')},'lists':'css',
 'title':f'Math Inquirers P3: Lesson {LN} – {TITLE}','order':ORDER,'cover':ORDER[0],
 'sections':{'s1':{'description':'Warm-up and explore','start':PRE+'title'},'s2':{'description':'Teach: missing digits, check by adding, guess and check','start':PRE+'teach1'},'s3':{'description':'Worksheet with teaching before each page','start':PRE+'break'},'s4':{'description':'Think harder, go further, talk and exit','start':PRE+'stretch'}},
 'faces':{'fredoka':{'family':'Fredoka','href':'https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&display=swap'},'nunito-sans':{'family':'Nunito Sans','href':'https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@400;600;700&display=swap'}},
 'designSystems':[]}
json.dump(deck,open(os.path.join(D,'deck.json'),'w'),indent=1,ensure_ascii=False)
print(len(ORDER),'slides')
