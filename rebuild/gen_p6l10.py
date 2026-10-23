"""Math Inquirers P6 (post-PSLE maths + coding bridge) - Lesson 10: Showcase Challenge. Writes split/p6l10/project."""
import json,os,sys,datetime
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,H)
import slidekit
from slidekit import *
slidekit.FOOT = FOOT = 'Math Inquirers P6  •  Notice it. Test it. Explain why.'
D=os.path.join(H,'..','split','p6l10','project'); SL=os.path.join(D,'slides'); os.makedirs(SL,exist_ok=True)
S={}; ORDER=[]
def put(i,h): S[i]=h; ORDER.append(i)
RED='#D64545'

def check_slide(sid,time,title,rows,notes,lw=200):
    """all answers visible at once (no click builds): check-together takes about 35 s a question"""
    body=h2(title)
    for i,(a,b) in enumerate(rows):
        top=250+i*130
        body+=pin(128,top,lw-20,f'<p style="font-size:36px;font-weight:800;color:{TEAL}">{E(a)}</p>',None,WHITE,20,'18px 24px')
        body+=answer(128+lw,top,1664-lw,b,None)
    return sec(sid,time,body,notes)

# ---------------- shared drawing helpers ----------------
def svg(w,h,body,aria,dw=None,dh=None): return f'<svg aria-label="{E(aria)}" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="width:{dw or w}px;height:{dh or h}px;flex:none">{body}</svg>'
def T(x,y,s,size=30,fill=NAVY,anchor='middle',weight=800,fam='Nunito Sans, Arial'): return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" fill="{fill}" font-family="{fam}">{E(str(s))}</text>'
BK={'event':(YEL,NAVY),'ctrl':(TEAL,WHITE),'var':(SKY,NAVY),'list':(WHITE,NAVY),'look':(RED,WHITE)}
def kind(s):
    w=s.split()[0]
    return 'event' if w=='when' else 'ctrl' if w in('repeat','if','else') else 'var' if w in('set','change') else 'list' if w in('add','delete') else 'look'
def blocks(prog,size=30):
    """prog: list of str or dict(c=header, body=[...], els=[...]). Our own simple block shapes."""
    Hh=round(size*1.9); ind=round(size*1.5); cw=size*0.58; pad=14
    tw=lambda s: round(len(s)*cw+2*pad)
    def txt(s,x,y,c): return f'<text x="{x+pad}" y="{y+round(Hh*0.66)}" font-size="{size}" font-weight="700" fill="{c}" font-family="Nunito Sans, Arial">{E(s)}</text>'
    def lay(items,x,y):
        out=''; w=0
        for it in items:
            if isinstance(it,str):
                k=kind(it); f,c=BK[k]; bw=tw(it)
                out+=f'<rect x="{x}" y="{y}" width="{bw}" height="{Hh}" rx="{18 if k=="event" else 10}" fill="{f}" stroke="{NAVY}" stroke-width="3"/>'+txt(it,x,y,c)
                y+=Hh; w=max(w,x+bw)
            else:
                segs=[(it['c'],it['body'])]+([('else',it['els'])] if it.get('els') else [])
                pts=[(x,y)]; inner=''; heads=''
                for lab,body in segs:
                    hw=max(tw(lab),ind+90)
                    pts+=[(x+hw,y),(x+hw,y+Hh),(x+ind,y+Hh)]; heads+=txt(lab,x,y,WHITE); w=max(w,x+hw)
                    s2,y2,w2=lay(body,x+ind,y+Hh); inner+=s2; w=max(w,w2)
                    y=max(y2,y+Hh+Hh//2); pts.append((x+ind,y))
                bh=round(Hh*0.45); pts+=[(x+ind+80,y),(x+ind+80,y+bh),(x,y+bh)]
                out+=f'<polygon points="{" ".join(f"{a},{b}" for a,b in pts)}" fill="{TEAL}" stroke="{NAVY}" stroke-width="3" stroke-linejoin="round"/>'+heads+inner
                y+=bh
        return out,y,w
    s,y,w=lay(prog,3,3)
    return s,int(w+6),int(y+6)
def code_svg(prog,aria,size=30):
    s,w,h=blocks(prog,size); return svg(w,h,s,aria)
def listmon(name,vals,x=0,y=0,size=28,w=200):
    rh=round(size*1.6); s=f'<rect x="{x+2}" y="{y+2}" width="{w}" height="{rh*(len(vals)+1)+12}" rx="14" fill="{WHITE}" stroke="{NAVY}" stroke-width="3"/>'+T(x+2+w/2,y+rh-4,name,size,TEAL)
    for i,v in enumerate(vals):
        yy=y+rh*(i+1)+6
        s+=T(x+22,yy+rh-12,i+1,size-2,NAVY,'middle',700)+f'<rect x="{x+48}" y="{yy+4}" width="{w-62}" height="{rh-8}" rx="8" fill="{YEL}" stroke="{NAVY}" stroke-width="2"/>'+T(x+48+(w-62)/2,yy+rh-12,v,size,NAVY)
    return s,w+4,rh*(len(vals)+1)+16
def towers(vals,unit=40,gap=36,col=SKY,hi=None,label=True,aria='towers',mx=None):
    mx=mx or max(vals); W=len(vals)*(unit+gap)+gap; Hh=mx*unit+60; b=''
    for i,v in enumerate(vals):
        x=gap+i*(unit+gap)
        for j in range(v): b+=f'<rect x="{x}" y="{Hh-50-(j+1)*unit}" width="{unit}" height="{unit}" rx="5" fill="{hi[i] if hi else col}" stroke="{NAVY}" stroke-width="3"/>'
        if label: b+=T(x+unit/2,Hh-14,v,30)
    return svg(W,Hh,b,aria)
def title_slide(sid,n,week,title,sub,today,notes):
    return (f'<section id="{sid}" data-transition="fade" style="background:{NAVY};color:{CREAM};font-family:{BF};padding:128px 128px 160px;display:flex;flex-direction:column;justify-content:center;gap:36px">\n'
            f'<p style="font-size:32px;font-weight:700;letter-spacing:4px;color:{YEL}">P6 LESSON {n}  •  WEEK {week}</p>\n<h1 style="font-family:{HF};font-size:128px;font-weight:600;line-height:1.05">{E(title)}</h1>\n<p style="font-size:44px;color:#C9D4EC">{E(sub)}</p>\n'
            f'<div style="background:#26385F;border-radius:24px;padding:40px;display:flex;flex-direction:column;gap:12px"><p style="font-size:28px;font-weight:700;letter-spacing:3px;color:{YEL}">TODAY WE WILL</p><p style="font-size:44px;font-weight:600">{E(today)}</p></div>\n'
            f'<p style="position:absolute;left:128px;bottom:64px;width:1400px;font-size:24px;color:#B7C3DD">{E(FOOT)}</p>\n<aside>{E(notes)}</aside>\n</section>\n')
def color_slide(sid,bg,kicker,title,big,small,notes,fg=CREAM,sc='#D7EFEA',kc=YEL,tsize=110):
    return (f'<section id="{sid}" data-transition="fade" style="background:{bg};color:{fg};font-family:{BF};padding:128px 128px 160px;display:flex;flex-direction:column;justify-content:center;gap:36px">\n'
            f'<p style="font-size:32px;font-weight:700;letter-spacing:4px;color:{kc}">{E(kicker)}</p>\n<h2 style="font-family:{HF};font-size:{tsize}px;font-weight:600;line-height:1.05">{E(title)}</h2>\n'
            f'<p style="font-size:48px;font-weight:600">{E(big)}</p>\n<p style="font-size:36px;color:{sc}">{E(small)}</p>\n'
            f'<p style="position:absolute;left:128px;bottom:64px;width:1400px;font-size:24px;color:{sc}">{E(FOOT)}</p>\n<aside>{E(notes)}</aside>\n</section>\n')
def numcards(items,size=38): return ''.join(card(p(f'<span style="color:{TEAL}">{E(a)}</span>  {E(b)}',size,600,raw=True)) for a,b in items)

import subprocess
C=json.loads(subprocess.run(['node','-e','process.stdout.write(JSON.stringify(require(process.argv[1])))',os.path.abspath(os.path.join(H,'..','p6','content','l10.js'))],capture_output=True,text=True,check=True).stdout)
L=C['lesson']; DK=C['deck']; QB=C['qbank']; SC=C['script']

PY_A='import random\nn = random.randint(1, 20)\nout = n * 3 + 4\nprint("My machine does x 3, then + 4.")\nprint("Out came", out)\nguess = int(input("What went in? "))\nif guess == n:\n    print("You cracked it!")\nelse:\n    print("No, it was", n)\n'
PY_B='n = int(input("Give me a whole number: "))\nfactors = 0\nfor d in range(1, n + 1):\n    if n % d == 0:\n        factors = factors + 1\nif factors == 2:\n    print(n, "is prime!")\nelse:\n    print(n, "is not prime. It has", factors, "factor(s).")\n'
PY_C='import random\nsevens = 0\nfor roll in range(1000):\n    if random.randint(1, 6) + random.randint(1, 6) == 7:\n        sevens = sevens + 1\nprint(sevens, "sevens in 1000 rolls")\nprint("We expect about", round(1000 / 6))\n'
PY_D='hours = int(input("How many hours from 9 o\'clock? "))\nt = (9 + hours) % 12\nif t == 0:\n    t = 12\nprint(t, "o\'clock")\n'

# ---------------- 1. title ----------------
put('p6l10-title',title_slide('p6l10-title',10,5,'Showcase Challenge','Mixed: maths and code  •  challenge round, then your own puzzle program',DK['today'],
 f"Objective: {L['objective']} Materials: {L['materials']} Online: {L['online']} Time plan (this lesson changes the usual routine; no relay and no separate talk time): opening 0 to 2, sneak-peek puzzles 2 to 6, challenge round 6 to 19.5 (workbook page 1 in teams of 2, Q1 and Q3; check together; ask how we started as the first line of the check), starter projects 19.5 to 26.5 (only Starter A is run live; click to reveal), brain break 26.5 to 30, plan and build 30 to 58 (teaching for the planning sheet, then workbook page 2 and Scratch; Think harder and Go further are open to everyone), flex 58 to 60.5 (unscripted, lost first), showcase 60.5 to 82.5 (two rounds of 4, 2 minutes 15 seconds each plus a 20-second switch, stars typed in the chat, rubric in the showcase notes), exit slip with the talk question 82.5 to 86, looking back 86 to 88, certificates (sent as PDFs) and the last stamp 88 to 90. Build target: a working copy of one starter with ONE change is full marks; an own idea is optional. Children chose their starter and their twist at the end of Lesson 9. Before the lesson: build the starter projects once (A Mystery Machine, B Prime or Not?, C Lucky Seven and D Clock Jumper) and share them as .sb3 files (children use File, Load from your computer; no account needed) with shared project links as a backup. Print or fill in certificates, and decide a random showcase order. Showcase switching: ask the next child to have their screen ready while the one before answers questions; a child may paste a screenshot of the program into the chat and the tutor runs their file, which removes the switching time."))

# ---------------- 4. explore 1: challenge round rules ----------------
steps=''.join(f'<li>{E(s)}</li>' for s in DK['expSetup'])
sb=''.join(f'<rect x="{10+c*230}" y="10" width="230" height="64" fill="{YEL}" stroke="{NAVY}" stroke-width="3"/>'+T(125+c*230,54,t,30) for c,t in enumerate(['Puzzle','Answer','Check','Reason']))
for r,lab in enumerate(['Q1','Q3']):
    sb+=''.join(f'<rect x="{10+c*230}" y="{74+r*58}" width="230" height="58" fill="{WHITE}" stroke="{NAVY}" stroke-width="3"/>' for c in range(4))+T(125,116+r*58,lab,30,TEAL)
    sb+=''.join(T(125+c*230,116+r*58,'+1',28,MUTED,weight=700) for c in (1,2,3))
board=svg(940,260,sb,'Scoreboard: for each puzzle Q1 and Q3, plus 1 point for the answer, plus 1 for a check, plus 1 for a reason')
body=h2('Challenge round: how it works')+'<div style="display:flex;gap:32px;align-items:flex-start">'+card(chip('TEAMS OF 2')+f'<ol style="font-size:30px;font-weight:600;padding-left:44px;margin:0;display:flex;flex-direction:column;gap:8px;line-height:1.3">{steps}</ol>',WHITE,'flex:1;min-width:0')+card(board,WHITE,'flex:none;padding:24px')+'</div>'
put('p6l10-explore1',sec('p6l10-explore1','5–7 MIN',body,
 'Teams do Q1 and Q3; Q2 (prime hunters) is the take-home question, marked with a star in the workbook. Explain the rules, then send teams of 2 to breakout rooms (or work side by side). Points: 1 for each correct answer, 1 for each check (worked a different way, or tested in code), 1 for each reason they can say aloud. Each team keeps its own score on page 1 and shows it only if the team wants to: no tally on the board or in the chat. The point of the check and reason columns: a lucky guess is worth only a third of the points. '
 'Predict first: '+SC['predict'][0]))

# ---------------- 5/6. worksheet page 1 (the round) ----------------
put('p6l10-ws1',ws_preview('p6l10-ws1','7–19 MIN','Challenge round: workbook page 1',[('Q1','Hexagon chains. Find the rule, then predict what the code says.'),('Q2','★ Take-home: prime hunters. Factors, prime factors and prime pairs.'),('Q3','Quick-fire: below zero, machines, turtle turns, clock.')],'Stuck? Which lesson does it remind you of? Make a table, list it in order, or draw it.',
 'Show this preview, do not read it aloud. Visit each team. Ask "How did you start?" and "What is your check?" before giving any help. Hints: '+' '.join(SC['exploreHints'])+' Teams who finish early can test Q1 in Scratch (the four blocks are on the page) or list the Q3e numbers with two nested loops.'))
put('p6l10-ws1ans',check_slide('p6l10-ws1ans','19–21 MIN','Challenge round: check together',[('Q1','a) 51   b) 5n + 1   c) 20   d) 76: a chain of 15 hexagons'),('Q2 ★','Take-home. a) 49   b) 2 × 2 × 3 × 7   c) 3 + 37,  11 + 29,  17 + 23'),('Q3','a) −7 °C  b) 5  c) 15  d) 1 o’clock')],
 'All the answers are shown at once. Children mark in a different colour (about 35 seconds a question). There is no separate how-we-started slide: ask it as the first line, "How did you start the hexagon puzzle?" (' + DK['expAsk'][0][1] + ') Then ask ONE volunteer to explain only Q1. Q2 is the take-home question: its answer is here so children can mark it at home. Q1: each new hexagon adds 5 sticks (it shares one side), so 5n + 1; 5 × 10 + 1 = 51; 5n + 1 = 101 gives n = 20; the code starts at 6 and adds 5 fourteen times: 6 + 70 = 76, which is 5 × 15 + 1, the chain of 15. '
 'Q2: a 2-digit number with exactly 3 factors is the square of a prime: 25 or 49; digits add to 13: 49. 84 = 2 × 42 = 2 × 2 × 21 = 2 × 2 × 3 × 7. For 40 test every prime up to 20: 3 + 37, 11 + 29, 17 + 23 work; 2, 5, 7, 13, 19 do not (38, 35, 33, 27, 21 are not prime). '
 'Q3: a) −4 + 9 = 5, 5 − 12 = −7. b) 3n − 10 = n, so 2n = 10, n = 5 (or trial: 5 × 3 − 10 = 5). c) 360 ÷ 24 = 15. d) 100 hours = 8 × 12 + 4, so 4 hours on from 9: 1 o’clock. (Digit cards and probability are now in Think harder 4.)',lw=200))

# ---------------- 8. teach: from puzzle to program ----------------
cards4=[('1','Maths first','Pick a puzzle. Work out its answer by hand.'),('2','Blocks','Input → rule → check → output. Under 15 blocks.'),('3','Test it','Use a value you already know the answer to.'),('4','Twist','Change the rule, add a score, or a level 2.')]
body=h2('From puzzle to program')+p('Every program you build today follows the same four steps.',34,600,MUTED)
for i,(n,t,d) in enumerate(cards4):
    body+=pin(128+i*424,330,392,p(n,64,800,TEAL)+p(t,40,800)+p(d,32,600),'rise',WHITE,24,'26px 28px','box-sizing:border-box;height:400px')
body+=pin(128,780,1664,p('The program is a test of your maths. If they agree, both are probably right.',34,700),'fade',SOFT,20,'18px 28px')
put('p6l10-teach1',sec('p6l10-teach1','22–23 MIN',body,
 'Teach. Click each card. Say: "A program that shows an answer you could not check is not a puzzle, it is a mystery box. So the maths always comes first." Then the three starters, each about one minute. Children do not copy them yet: they choose one at the planning stage after the break.'))

# ---------------- 9. starter A ----------------
progA=['when green flag clicked','set n to (pick random 1 to 20)','ask (join "OUT: " ((n * 3) + 4)) and wait',{'c':'if (answer = n) then','body':['say "You cracked it!"'],'els':['say (join "No, it was " n)']}]
body=h2('Starter A: Mystery Machine')+pin(128,250,820,code_svg(progA,'Code blocks: when green flag clicked, set n to pick random 1 to 20, ask join OUT: and n times 3 plus 4 and wait, if answer equals n then say You cracked it! else say join No, it was, n',28))
body+=pin(1010,250,782,p('The maths',30,800,TEAL)+p('OUT = 3n + 4.  Backwards: take away 4, then divide by 3.',34,700),'rise',WHITE,20,'20px 28px')
body+=pin(1010,470,782,p('Test it',30,800,TEAL)+p('If n is 5, it must show OUT: 19. Type 5: “You cracked it!”',34,700),'rise',WHITE,20,'20px 28px')
body+=pin(1010,690,782,p('Twist ideas',30,800,TEAL)+p('A different rule each time; keep a score; allow negative numbers.',32,700),'rise',SOFT,20,'20px 28px')
put('p6l10-we1',sec('p6l10-we1','23–24 MIN',body,
 'Starter A (Lesson 4 idea). Run it on screen. Think-aloud: '+SC['think'][1]+' Note: Scratch uses * for ×. "answer" is what the player typed. The worksheet (Q4a) asks for a different test, n = 9, so do not reveal it. 7 blocks. '
 'Python version (optional):\n'+PY_A+'With n = 5 it prints "Out came 19"; typing 5 gives "You cracked it!", typing 7 gives "No, it was 5".'))

# ---------------- 10. starter B ----------------
progB=['when green flag clicked','ask "Give me a whole number" and wait','set factors to 0','set d to 1',{'c':'repeat (answer)','body':[{'c':'if ((answer mod d) = 0) then','body':['change factors by 1']},'change d by 1']},{'c':'if (factors = 2) then','body':['say "Prime!"'],'els':['say "Not prime"']}]
body=h2('Starter B: Prime or Not?')+pin(128,232,800,code_svg(progB,'Code blocks: when green flag clicked, ask give me a whole number and wait, set factors to 0, set d to 1, repeat answer times (if answer mod d equals 0 then change factors by 1; change d by 1), if factors equals 2 then say Prime! else say Not prime',24))
W=[150,220,190]; L0=1060
body+=pin(L0,240,732,p('Test: type 6',32,800,TEAL))
body+=trow(L0,300,['d','6 mod d','factors'],W,None,True,30)
for k,(m,f) in enumerate([(0,1),(0,2),(0,3),(2,3),(1,3),(0,4)]): body+=trow(L0,368+k*64,[str(k+1),str(m),str(f)],W,'rise',30)
body+=answer(L0,770,732,'4 factors → “Not prime” ✓')
put('p6l10-we2',sec('p6l10-we2','25–26 MIN',body,
 'Starter B (Lesson 2 idea): one line only, NOT run live; children run it when they load the file. "n mod d = 0" means d divides n exactly, so d is a factor. A prime has exactly 2 factors: 1 and itself. Click through the trace for 6: factors 1, 2, 3 and 6 make 4, so not prime. Then run it with 7 (2 factors: prime) and 1 (1 factor: not prime, which is correct: 1 is not a prime). 11 blocks. Worksheet Q4b tests 91, so do not run 91 now. Twist ideas: say how many factors; only accept numbers up to 1000; find the numbers with exactly 3 factors. '
 'Python version (optional):\n'+PY_B+'Tested: 6 → "6 is not prime. It has 4 factor(s)."  7 → "7 is prime!"  97 → "97 is prime!"  1 → "1 is not prime. It has 1 factor(s)."'))

# ---------------- 11. starter C ----------------
progC=['when green flag clicked','set sevens to 0',{'c':'repeat 1000','body':[{'c':'if ((pick random 1 to 6) + (pick random 1 to 6) = 7) then','body':['change sevens by 1']}]},'say (join sevens " sevens")']
g=''
for a in range(7):
    for b in range(7):
        x=a*62; y=b*62
        if a==0 and b==0: continue
        if a==0 or b==0:
            g+=f'<rect x="{x}" y="{y}" width="58" height="58" rx="8" fill="{TEAL}"/>'+T(x+29,y+40,b if a==0 else a,28,WHITE)
        else:
            s7=(a+b==7)
            g+=f'<rect x="{x}" y="{y}" width="58" height="58" rx="8" fill="{YEL if s7 else WHITE}" stroke="{NAVY}" stroke-width="2"/>'+T(x+29,y+40,a+b,26,NAVY,weight=800 if s7 else 600)
grid=svg(436,436,g,'A 6 by 6 table of two-dice totals; the six cells with total 7 are yellow',400,400)
body=h2('Starter C: Lucky Seven')+pin(128,240,1000,code_svg(progC,'Code blocks: when green flag clicked, set sevens to 0, repeat 1000 (if pick random 1 to 6 plus pick random 1 to 6 equals 7 then change sevens by 1), say join sevens and the word sevens',24))
body+=pin(128,560,1000,p('6 of the 36 equally likely results make 7: that is 1/6.  1000 ÷ 6 ≈ 167.',34,700),'rise',WHITE,20,'20px 28px')
body+=pin(128,730,1000,p('Our runs: 152, 182, 162. Close to 167, never exactly the same: chance varies.',32,700),'rise',SOFT,20,'20px 28px')
body+=pin(1300,240,440,grid)
put('p6l10-we3',sec('p6l10-we3','26–28 MIN',body,
 'Starter C (Lesson 6 idea): one line only, NOT run live; children run it when they load the file. Think-aloud: '+SC['think'][2]+' The table: there are 6 × 6 = 36 ways two dice can land, all equally likely; the yellow cells (1 + 6, 2 + 5, … , 6 + 1) make 7. Run it 3 times on screen and write the results: they will differ. A run of 1000 usually lands between about 145 and 190. Worksheet Q4c asks about 8s, so do not count the 8s now. 5 blocks. Twist ideas: let the player pick the total; count every total in a list; compare 100 rolls with 10 000 rolls. '
 'Python version (optional):\n'+PY_C+'Three test runs printed 152, 182 and 162 sevens; the last line always prints "We expect about 167".'))

# ---------------- 12. key ----------------
body=h2(DK['keyHead'])+card(p(DK['keyBig'],42,700))+card(p(DK['keySmall'],36,600,MUTED))
put('p6l10-key',sec('p6l10-key','28–29 MIN',body,'Say the key idea together. Common mistakes to watch for while children build: (1) '+L['mistakes'][0]+' (2) '+L['mistakes'][1]+' (3) '+L['mistakes'][2]))

# ---------------- 13. break ----------------
put('p6l10-break',color_slide('p6l10-break',TEAL,'29–32 MIN','Brain break: turtle moves','I call a shape. Turn on the spot by its outside angle at every corner: triangle 120°, square 90°, hexagon 60°.','Count the corners until you face the front again. Then a drink of water and back to the screen.',
 'Three minutes. Call: square (4 turns of 90°), triangle (3 of 120°), hexagon (6 of 60°), then the surprise: a star (5 turns of 144°, which takes 2 full turns to face the front again). Online: children stay in view of the camera.'))

# ---------------- 14. teach before page 2: plan it ----------------
progD=['when green flag clicked',"ask \"How many hours from 9 o'clock?\" and wait",'set t to ((9 + answer) mod 12)',{'c':'if (t = 0) then','body':['set t to 12']},"say (join t \" o'clock\")"]
body=h2('Plan it: a worked example')+pin(128,240,860,p('Clock Jumper (Lesson 8)',32,800,TEAL)+p('Puzzle: it is 9 o’clock. What time is it h hours from now?',32,700)+p('By hand: add, then remove whole 12s. 0 left means 12 o’clock.',32,600),None,WHITE,20,'20px 28px')
body+=pin(128,520,860,code_svg(progD,"Code blocks: when green flag clicked, ask how many hours from 9 o'clock and wait, set t to 9 plus answer mod 12, if t equals 0 then set t to 12, say join t o'clock",26))
W=[180,260,200]; L0=1080
body+=pin(L0,240,712,p('Tests, worked out FIRST',30,800,TEAL))
body+=trow(L0,300,['h','by hand','it said'],W,None,True,30)
for k,(h_,bh,said) in enumerate([('5','2 o’clock','2 ✓'),('15','12 o’clock','12 ✓'),('30','3 o’clock','3 ✓')]): body+=trow(L0,368+k*70,[h_,bh,said],W,'rise',30)
body+=pin(L0,610,712,p('15 is the edge case: 9 + 15 = 24, and 24 mod 12 is 0. Without the if block it says “0 o’clock”.',30,700),'fade',SOFT,20,'18px 24px')
put('p6l10-teachplan',sec('p6l10-teachplan','32–34 MIN',body,
 'Teach before worksheet page 2 (Q5 is the planning table, Q6 the blocks and tests). Walk through a FOURTH idea so the starters stay fresh. Think-aloud: "My puzzle: 9 o’clock plus h hours. By hand: 9 + 5 = 14, take away 12: 2 o’clock. 9 + 15 = 24, take away two 12s: 0, which on a clock is 12. 9 + 30 = 39, take away three 12s: 3. I write these tests BEFORE I run anything." Click the rows. Then: "I found a bug with the edge case: without the if block it said 0 o’clock." '
 'Python version (optional):\n'+PY_D+'Tested: 5 → "2 o\'clock", 15 → "12 o\'clock", 30 → "3 o\'clock".'))

# ---------------- 15. teach: test like a detective ----------------
body=h2('Test it like a detective')
tt=[('Known answer','Pick an input you worked out by hand.','Prime or Not? with 7: it must say Prime!'),('Edge case','Try the smallest, 0, 1 or the biggest.','Prime or Not? with 1: 1 factor, so Not prime ✓'),('Random programs','Run it several times. Close, not exact.','Lucky Seven: near 167 each time')]
for i,(t,d,e) in enumerate(tt):
    body+=pin(128,250+i*215,1664,p(t,36,800,TEAL)+p(d,32,700)+p('e.g. '+e,30,600,MUTED),'rise',WHITE,20,'18px 28px')
put('p6l10-teachtest',sec('p6l10-teachtest','34–35 MIN',body,
 'Teach before worksheet page 2. Click each kind of test. Ask: "Why is 1 a good edge case for Prime or Not?" (it is the only whole number with exactly 1 factor; a program that counts badly might call it prime). "If Lucky Seven said 400, what would you think?" (a bug: 400 is far too many; maybe it counts 7 OR something, or never resets sevens to 0).'))

# ---------------- 16/17. worksheet page 2 ----------------
put('p6l10-ws2',ws_preview('p6l10-ws2','35–60 MIN','Page 2: plan, then build',[('Q4','Maths first: what should YOUR starter do? Work out only the part for the starter you picked.'),('Q5','Your plan: the idea, the answer, your twist.'),('Q6','Your blocks and three tests, written BEFORE you run them.'),('Then','Build it in Scratch (or Python). Under 15 blocks.')],'Finished early? Stretch and Challenge, or give your program a level 2.',
 'Show this preview, do not read it aloud. Q4: only the part for the starter you picked (about 2 minutes); Q5: three cells (idea, answer, twist); Q6: three test rows written BEFORE running. Then build for about 20 minutes (test as you go; a working copy of one starter with one change is full marks). Anyone who wants to start from their own idea may, but only after a starter works. Circulate: '+' '.join(SC['circulate'])+' Hints: '+' '.join(SC['hints'])+' Anyone stuck after 5 minutes: build a starter exactly, then change ONE thing (the rule, the range, the total).'))
put('p6l10-ws2ans',check_slide('p6l10-ws2ans','60–62 MIN','Page 2: check Q4, then get ready',[('Q4a','31;  OUT 58 came from 18'),('Q4b','4 factors (1, 7, 13, 91): not prime'),('Q4c','about 139: 5 of 36 results make 8'),('Q5–6','Open: tests worked out by hand first')],
 'All the answers are shown at once. a) 9 × 3 + 4 = 31; (58 − 4) ÷ 3 = 18. b) 91 = 7 × 13, so it has 4 factors. c) 2 + 6, 3 + 5, 4 + 4, 5 + 3, 6 + 2: 5 of the 36 results; 1000 × 5 ÷ 36 is about 139 (138.9), and a real run will be near this, not exactly. Finish and save. Everyone gets their project open and ready to share.',lw=220))

# ---------------- 18. stretch ----------------
st=[('1.','What is the 50th term of 7, 11, 15, 19, …?'),('2.','How many of the numbers 1 to 50 have exactly 3 factors?'),('3.','Two dice are rolled and added. What is the probability that the total is a prime number?')]
put('p6l10-stretch',sec('p6l10-stretch','For early finishers',h2('Stretch')+numcards(st,36),
 'For children who finish building early. Answers: 1) 203 (nth term 4n + 3: 4 × 50 + 3). 2) 4: 4, 9, 25 and 49 (the squares of the primes 2, 3, 5, 7; their only factors are 1, the prime and the square). 3) 15/36 = 5/12 (prime totals: 2 in 1 way, 3 in 2, 5 in 4, 7 in 6, 11 in 2; 1 + 2 + 4 + 6 + 2 = 15). Each one can be tested in code: a loop for 1, a factor counter for 2, a dice simulation for 3.'))

# ---------------- 19. challenge ----------------
ch=QB['challenge'][:2]
put('p6l10-challenge',sec('p6l10-challenge','For early finishers',h2('Challenge')+numcards([(f'{i+1}.',c['q']) for i,c in enumerate(ch)],36),
 'Pair challenge for early finishers, or take home. Ask for the reason every time. Answers: 1) '+ch[0]['a']+'  2) '+ch[1]['a']))

# ---------------- 20. challenge: see it ----------------
st1=''
for k in range(12):
    n=k+1; x=10+k*62
    fill=SKY if n%2==0 else WHITE
    st1+=f'<rect x="{x}" y="70" width="56" height="70" rx="8" fill="{fill}" stroke="{NAVY}" stroke-width="3"/>'+T(x+28,116,n,28)
    if n%3==0: st1+=f'<circle cx="{x+28}" cy="105" r="30" fill="none" stroke="{RED}" stroke-width="4"/>'
st1+=f'<rect x="10" y="190" width="40" height="40" rx="6" fill="{SKY}" stroke="{NAVY}" stroke-width="3"/>'+T(62,220,'multiple of 2',26,NAVY,'start',700)
st1+=f'<circle cx="420" cy="210" r="20" fill="none" stroke="{RED}" stroke-width="4"/>'+T(452,220,'multiple of 3',26,NAVY,'start',700)
st1+=T(380,300,'The pattern repeats every 6 numbers.',28,TEAL)+T(380,345,'How many are left in each block of 6?',28,TEAL)+T(380,40,'1 to 12 of the 100 numbers',28)
mach=f'<g transform="translate(0,40)">'
for i,(t,f) in enumerate([('IN: ?',YEL),('× 3',GREY),('− 8',GREY),('OUT: ?',SKY)]):
    x=10+i*190; mach+=f'<rect x="{x}" y="20" width="150" height="90" rx="16" fill="{f}" stroke="{NAVY}" stroke-width="4"/>'+T(x+75,78,t,32)
    if i<3: mach+=f'<line x1="{x+150}" y1="65" x2="{x+182}" y2="65" stroke="{NAVY}" stroke-width="4"/><polygon points="{x+190},65 {x+176},57 {x+176},73" fill="{NAVY}"/>'
mach+=f'<path d="M655 115 Q380 230 85 115" fill="none" stroke="{TEAL}" stroke-width="4" stroke-dasharray="12 8"/>'+T(380,215,'the SAME number',30,TEAL)+'</g>'
mach+=T(380,330,'Try 1, 2, 3, … in a table.',28,NAVY,weight=700)+T(380,375,'Then: × 3, then + 8. Can IN be negative?',28,RED,weight=700)
cardsvg=lambda t,s,a: f'<div style="background:{WHITE};border-radius:24px;padding:20px 24px;display:flex;flex-direction:column;gap:10px;flex:1;min-width:0"><p style="font-size:30px;font-weight:700;color:{TEAL}">{E(t)}</p>'+svg(770,400,s,a,'100%','auto').replace('height:auto;flex:none','height:auto;display:block')+'</div>'
body=h2('Challenge: see it')+'<div style="display:flex;gap:32px;align-items:flex-start">'+cardsvg('Q1: not 2, not 3',st1,'The numbers 1 to 12; even numbers are shaded blue and multiples of 3 are circled red')+cardsvg('Q2: same in, same out',mach,'A machine: IN, times 3, minus 8, OUT, with a dashed arrow saying OUT is the same number as IN')+'</div>'
put('p6l10-chdiag',sec('p6l10-chdiag','For early finishers',body,'Show after pairs have tried the Challenge, or if they are stuck. The diagrams show the problem, not the answer. Ask: What do you notice? What repeats? What do we know? Answers are in the Challenge slide notes.'))

# ---------------- 21. challenge walk-through ----------------
body=h2('Challenge: walk-through')+pin(128,250,800,p('Q1: count, then take away',38,800,TEAL))
for i,t in enumerate(['Multiples of 2: 50.  Multiples of 3: 33.','Multiples of 6 were counted twice: 16.','2 or 3: 50 + 33 − 16 = 67.  Not 2 or 3: 100 − 67 = 33','Check: 2 left in every 6 (1 and 5): 16 × 2 = 32, plus 97 → 33 ✓']): body+=pin(128,330+i*130,800,p(t,30),'rise',WHITE)
body+=pin(992,250,800,p('Q2: make it balance',38,800,TEAL))
for i,t in enumerate(['× 3 − 8 = same: 3 lots of n, minus 8, is 1 lot of n','So 2 lots of n = 8, and n = 4','Check: 4 × 3 − 8 = 4 ✓','× 3 + 8: 2 lots of n = −8, so n = −4.  Check: −12 + 8 = −4 ✓']): body+=pin(992,330+i*130,800,p(t,30),'rise',WHITE)
put('p6l10-chwalk',sec('p6l10-chwalk','For early finishers',body,'Use after pairs have tried, with the "see it" slide. Q1 can be checked in code: repeat 100 with if (n mod 2 > 0) and (n mod 3 > 0) then change count by 1: it says 33. Q2 is the equation 3n − 8 = n from Lesson 4; the second part needs Lesson 3’s negative numbers. Trial in a table also works: n = 1, 2, 3, 4 gives OUT −5, −2, 1, 4.'))

# ---------------- 22. showcase ----------------
parts=[('25 s','Show the puzzle','What maths question does it ask?'),('30 s','Run it','Let someone in the group play.'),('35 s','Prove it','One test you worked out by hand first.'),('45 s','Explain why','The maths that makes it work.')]
body=h2('Showcase: 2 minutes 15 each')
for i,(t,a,b) in enumerate(parts):
    body+=pin(128+i*424,260,392,chip(t,YEL,NAVY)+p(a,40,800)+p(b,30,600),None,WHITE,24,'24px 28px','box-sizing:border-box;height:330px')
body+=pin(128,640,1604,p('Audience: type two stars and a question in the chat for each presenter (stars are typed, not spoken).  “I liked … because …”   “I wonder …”',32,700),None,SOFT,20,'22px 30px')
put('p6l10-showcase',sec('p6l10-showcase','62–87 MIN',body,
 'TWO ROUNDS OF 4 so nobody waits more than about 11 minutes: round 1 is about minutes 60.5 to 71.5, round 2 about 71.5 to 82.5. Each child has 2 minutes 15 seconds (show the puzzle 25 s, run it 30 s, prove it with one hand-worked test 35 s, explain the maths 45 s) plus a 20-second switch: 8 x 2:35 = 20 minutes 40 seconds, plus set-up (the flex minutes before the showcase are for this). Stars (two stars and a question) are TYPED in the chat by the audience, not spoken, so a spoken reply never breaks the slot. A child who is not ready can show a screenshot and you run their file, or show their plan only. Use a timer, volunteers first (never name a child to go next); a child may pass to the second round. The next child has their screen ready while the one before answers questions; a child may paste a screenshot into the chat and the tutor runs their file instead of sharing a screen. A child who did not finish shows their plan and the tests they worked out by hand: that still earns full marks for maths and testing. '
 'SHOWCASE RUBRIC (1 to 3 points each; note it privately, share only the stars and the wish). '
 'Maths: 1 = gives an answer; 2 = correct answer with working; 3 = correct, and can say why the rule works. '
 'Testing: 1 = ran it once; 2 = a test with an answer known in advance; 3 = a known-answer test and an edge case, or a bug found and fixed. '
 'Code: 1 = it runs; 2 = under 15 blocks with sensible variable names; 3 = a twist that changes the puzzle (new rule, score, levels). '
 'Explaining: 1 = reads the blocks aloud; 2 = says what the program does; 3 = explains the maths and answers a question from the group. '
 'Questions to ask each presenter: "Which test did you do first?" "What would happen with 0 or 1?" "Where is the maths in your blocks?" Write one specific sentence of praise for each child for the certificate moment.'))

# ---------------- 24. exit ----------------
body=h2('Exit ticket')+card(chip('EXIT TICKET')+p(L['exit']['q'],42))+card(p('Write it on your exit slip (Finish page). The last line answers: what was the hardest bug you fixed today, and how did you find it? When your tutor says show, tick the slip against the answer slide. Then collect your last stamp.',34))
put('p6l10-exit',sec('p6l10-exit','88–90 MIN',body,'The talk question is folded into the exit slip as its last line (there is no separate talk time): "'+SC['talk'][0].strip('“”')+'" Everyone holds the slip up at the same moment. '+L['exit']['a']+' Extension to take home: '+L['extension']))

# ---------------- 25. end (certificates) ----------------
put('p6l10-end',color_slide('p6l10-end',NAVY,'WELL DONE, INQUIRERS','Ten lessons of maths and code','Notice it. Test it. Explain why.','Certificates (sent as PDFs) and a last stamp for every inquirer.',
 'Certificates are sent to parents as a PDF with one specific line of praise already written for each child (the showcase rubric asks for it): do not hand out paper certificates or write praise live. Say one sentence of praise to the whole group. '+SC['close'][0]+' Ask each child to name one puzzle or program they enjoyed. Give parents the one-page summary from the tutor guide, with links to Scratch and to the starter projects so children can keep building.',fg=CREAM,sc='#C9D4EC',kc=YEL,tsize=120))

# ---------------- write ----------------
for f in os.listdir(SL):
    if f.endswith('.html') and f[:-5] not in S: os.remove(os.path.join(SL,f))
for i,h in S.items(): open(os.path.join(SL,i+'.html'),'w').write(h)
deck={'v':4,'createdOnFiles':{'v':1,'at':datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')},'lists':'css','title':'Math Inquirers P6: Lesson 10 – Showcase Challenge','order':ORDER,'cover':'p6l10-title',
      'sections':{'s1':{'description':'Warm-up and the challenge round','start':'p6l10-title'},'s2':{'description':'From puzzle to program: three starter projects','start':'p6l10-teach1'},'s3':{'description':'Plan and build (Think harder and Go further are open to everyone)','start':'p6l10-break'},'s4':{'description':'Showcase, talk, exit and certificates','start':'p6l10-showcase'}},
      'faces':{'fredoka':{'family':'Fredoka','href':'https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&display=swap'},'nunito-sans':{'family':'Nunito Sans','href':'https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@400;600;700&display=swap'}},'designSystems':[]}
json.dump(deck,open(os.path.join(D,'deck.json'),'w'),indent=1,ensure_ascii=False)
print(len(ORDER),'slides')

import p6_gaps; p6_gaps.apply(10)
