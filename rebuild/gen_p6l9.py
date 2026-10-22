"""Math Inquirers P6 (post-PSLE maths + coding bridge) - Lesson 9: Data Detectives. Writes split/p6l9/project."""
import json,os,sys,datetime
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,H)
import slidekit
from slidekit import *
slidekit.FOOT = FOOT = 'Math Inquirers P6  •  Notice it. Test it. Explain why.'
D=os.path.join(H,'..','split','p6l9','project'); SL=os.path.join(D,'slides'); os.makedirs(SL,exist_ok=True)
S={}; ORDER=[]
def put(i,h): S[i]=h; ORDER.append(i)
RED='#D64545'

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
C=json.loads(subprocess.run(['node','-e','process.stdout.write(JSON.stringify(require(process.argv[1])))',os.path.abspath(os.path.join(H,'..','p6','content','l9.js'))],capture_output=True,text=True,check=True).stdout)
L=C['lesson']; DK=C['deck']; QB=C['qbank']; SC=C['script']

# ---------------- 1. title ----------------
put('p6l9-title',title_slide('p6l9-title',9,5,'Data Detectives','Averages and data  •  lists, adding up, the average (mean)',DK['today'],
 f"Objective: {L['objective']} Materials: {L['materials']} Online: {L['online']} Time plan: warm-up 0 to 10 (quick-eye mean, then quick questions), explore at the computer 10 to 25 (class data in a Scratch list), teaching 25 to 35 (click to reveal each step and answer; the mean program with a trace table), brain break 35 to 40, worksheet 40 to 75 with short teaching before each page and a check-together slide after it, talk time 75 to 82, exit ticket 82 to 90. Before the lesson: make the starter project (one sprite, an empty list called data) and share its link, or let children build it from the code slide."))

# ---------------- 2. warm-up game ----------------
rounds=[('Round 1','8   12   10   9   11','Mean 10'),('Round 2','20   25   30   35   40','Mean 30'),('Round 3','3   4   5   6   37','Mean 11')]
body=h2('Warm-up: quick-eye mean')+p('Five numbers, five seconds. No working: write your best guess of the mean.',34,600,MUTED)
for i,(r,nums,a) in enumerate(rounds):
    top=330+i*170
    body+=pin(128,top,1250,f'<div style="display:flex;align-items:center;gap:36px"><p style="font-size:32px;font-weight:800;color:{TEAL}">{E(r)}</p><p style="font-family:{HF};font-size:60px;font-weight:600;letter-spacing:2px">{E(nums)}</p></div>',None,WHITE,20,'18px 30px')
    body+=answer(1420,top+12,372,a)
put('p6l9-warm1',sec('p6l9-warm1','0–5 MIN',body,
 'Minutes 0 to 5. Quick-eye mean. Hide the slide (or cover the numbers), show one round for 5 seconds, then hide it again. Children write a guess on paper (no points, no ranking). Click to show the mean and ask how they guessed. '
 'Round 1: 8 + 12 + 10 + 9 + 11 = 50, 50 ÷ 5 = 10. Round 2: 150 ÷ 5 = 30 (the middle number, because the numbers are evenly spaced). Round 3: 3 + 4 + 5 + 6 + 37 = 55, 55 ÷ 5 = 11. '
 'Ask after round 3: "Most of you guessed about 5. Why is the mean 11?" (The 37 pulls the mean up: we come back to this today.) Ask: "How did you guess so fast?" Listen for: pick a middle number, then check the big ones and small ones balance.'))

# ---------------- 3. quick questions ----------------
qs=[(f'{i+1}.',q,a) for i,(q,a) in enumerate(DK['warmQs'])]
body=h2('Quick questions')+''.join(qrow(128,250+i*125,1250,a,b,36) for i,(a,b,c) in enumerate(qs))+''.join(answer(1420,250+i*125,372,c) for i,(a,b,c) in enumerate(qs))
put('p6l9-warm2',sec('p6l9-warm2','5–10 MIN',body,
 'Minutes 5 to 10. Read each aloud, give thinking time, take answers, then click to show. Answers: 1) 6 (18 ÷ 3). 2) 25 (100 ÷ 4; not one of the values!). 3) 60 (5 × 12: we can turn the mean back into a total). 4) 22.4 (112 ÷ 5): four of the five values are 3, yet the mean is over 20. 5) 3 (6 ÷ 2): means can be decimals, and decimals can have a whole-number mean. '
 'Ask on 3: "How did you get a total from a mean?" This is the key move for today’s missing-value puzzles.'))

# ---------------- 4. explore 1 ----------------
steps=''.join(f'<li>{E(s)}</li>' for s in DK['expSetup'])
lm,lw,lh=listmon('data',['12','9','15','11'],0,0,26,190)
mini_prog=[{'c':'repeat (length of data)','body':['change total by (item i of data)','change i by 1']},'say (total / (length of data))']
bs,bw,bh=blocks(mini_prog,24)
pic=svg(1300,232,lm+f'<g transform="translate(300,10)">{bs}</g>'+f'<path d="M210 116 L282 116" stroke="{NAVY}" stroke-width="5"/><polygon points="296,116 276,104 276,128" fill="{NAVY}"/>'
        +f'<path d="M{310+bw} 116 L{380+bw} 116" stroke="{NAVY}" stroke-width="5"/><polygon points="{394+bw},116 {374+bw},104 {374+bw},128" fill="{NAVY}"/>'
        +f'<rect x="{410+bw}" y="66" width="300" height="100" rx="18" fill="{YEL}" stroke="{NAVY}" stroke-width="4"/>'+T(560+bw,132,'mean = ?',44),
        'A list called data holding 12, 9, 15, 11, an arrow to code blocks that add up the list and divide by its length, and a yellow box: mean = ?',1300,232)
body=(h2('Explore: our class data')+card(chip('EXPLORE')+f'<ol style="font-size:30px;font-weight:600;padding-left:48px;margin:0;display:flex;flex-direction:column;gap:4px;line-height:1.25">{steps}</ol>')
      +card(pic,WHITE,'padding:16px 32px'))
put('p6l9-explore1',sec('p6l9-explore1','10–15 MIN',body,
 'Minutes 10 to 15. Everyone types the number of letters in their full name (no spaces) in the chat; copy the list onto the slide or a shared board. Each child estimates the mean, then works it out by hand (total ÷ how many), then opens the starter project (or builds the 5 blocks shown; full program on the code slide later) and types each value into the list called data with the + button under the list. Run it. '
 'Then the prediction: "Our tutor joins with a 30-letter name. Will the mean go up a little or a lot?" Add 30 to the list and run again. The picture uses example data (12, 9, 15, 11: mean 47 ÷ 4 = 11.75); your class data will differ. '
 'Online: children share their screen when their program runs. If Scratch is slow, pairs can share one screen. Watch for children who divide by the wrong count or who type a value twice.'))

# ---------------- 5. explore 2 ----------------
body=h2('Explore: talk about it')+numcards([(f'{i+1}.',q) for i,(q,a) in enumerate(DK['expAsk'])],40)
put('p6l9-explore2',sec('p6l9-explore2','15–25 MIN',body,
 'Minutes 15 to 25. Let pairs keep testing (add other values: which new value keeps the mean exactly the same?), then gather to answer. Answers: 1) '+DK['expAsk'][0][1]+' 2) '+DK['expAsk'][1][1]+' 3) '+DK['expAsk'][2][1]+' Finisher answer: adding a value equal to the mean keeps the mean the same (it is already "level").'))

# ---------------- 6. teach 1: level it out ----------------
body=h2('The mean: level it out')+p('Four towers: 3, 7, 5 and 9 cubes. Move cubes until every tower is the same height.',34,600,MUTED)
body+=pin(128,320,760,p('Before',32,800,TEAL)+towers([3,7,5,9],32,60,SKY,aria='Towers of 3, 7, 5 and 9 cubes'),None,WHITE,24,'20px 30px',f'box-sizing:border-box;height:440px')
body+=pin(1032,320,760,p('Levelled',32,800,TEAL)+towers([6,6,6,6],32,60,YEL,aria='Four towers of 6 cubes',mx=9),'fade',WHITE,24,'20px 30px',f'box-sizing:border-box;height:440px')
body+=step(1,'Total: 3 + 7 + 5 + 9 = 24. Moving cubes keeps the total.',top=790,width=800,size=34)
put('p6l9-teach1',sec('p6l9-teach1','25–27 MIN',body+pin(1032,790,760,p('Mean = 24 ÷ 4 = 6',40,800),'pop',YEL,20,'20px 30px'),
 'Teach. Build the towers with real cubes on camera if you can. Think-aloud: "The 9-tower gives 3 cubes to the 3-tower; the 7-tower gives 1 cube to the 5-tower. Now they are all 6. That level is the mean." Click: the levelled towers, the total, then the mean. '
 'Say: "Levelling out and total ÷ how many give the same answer, because moving cubes keeps the total and sharing it equally is exactly dividing by how many towers." Ask: "Could the level ever be above the tallest tower?" (No: we only move cubes downhill.)'))

# ---------------- 7. worked example 1 ----------------
m1=DK['mini1']
body=h2('Worked example: find it, then check it')+card(p('Goals in 5 matches:  3,  0,  4,  1,  2.   Find the mean.',42,700))
body+=step(1,'Total: 3 + 0 + 4 + 1 + 2 = 10. There are 5 values: the 0 is a match too.',top=400,size=34)
body+=step(2,'Mean = total ÷ how many = 10 ÷ 5 = 2.',top=510,size=34)
body+=step(3,'Balance check: above 2 → 3 is +1, 4 is +2 (+3).  Below 2 → 0 is −2, 1 is −1 (−3).  +3 and −3 balance ✓',top=620,size=34)
body+=answer(128,770,1664,'Mean 2 goals. Above and below the mean always balance.')
put('p6l9-we1',sec('p6l9-we1','27–29 MIN',body,
 'Click to reveal each step. Think-aloud: '+SC['think'][0]+' Why the check works: levelling moves the extra cubes above the mean into the gaps below it, so "how much above" must equal "how much below". Common mistake: dividing by 4 because 0 "is nothing" (10 ÷ 4 = 2.5 is wrong).'))

# ---------------- 8. code it ----------------
prog=['when green flag clicked','set total to 0','set i to 1',{'c':'repeat (length of data)','body':['change total by (item i of data)','change i by 1']},'say (total / (length of data))']
body=h2('Code it: the mean machine')+pin(128,250,700,code_svg(prog,'Code blocks: when green flag clicked, set total to 0, set i to 1, repeat length of data (change total by item i of data, change i by 1), say total divided by length of data',28))
W=[150,150,190,190]; L0=1000
body+=pin(L0,240,792,p('data:  3,  0,  4,  1,  2',34,800,TEAL))
body+=trow(L0,310,['loop','i','item i','total'],W,None,True,32)
for k,(it,tot) in enumerate([(3,3),(0,3),(4,7),(1,8),(2,10)]): body+=trow(L0,385+k*72,[str(k+1),str(k+1),str(it),str(tot)],W,'rise',32)
body+=answer(L0,770,792,'It says 10 ÷ 5 = 2 ✓')
put('p6l9-code1',sec('p6l9-code1','29–31 MIN',body,
 'Build it live in Scratch while children copy (Variables: make total and i; make a list called data). Then trace it on the slide: click to add each row. Think-aloud: "i starts at 1, so item 1 of data is 3: total becomes 3. Change i by 1. Item 2 is 0: total stays 3. Item 3 is 4: total 7. Item 4 is 1: total 8. Item 5 is 2: total 10. The loop ran length of data = 5 times. 10 ÷ 5 = 2." '
 'Why "length of data" and not 5? Then the program still works when the list grows (teaching slide before page 2). '
 'Python version (optional, for children who know Python):\n'
 'data = [3, 0, 4, 1, 2]        # goals in 5 matches\ntotal = 0\nfor value in data:\n    total = total + value\nmean = total / len(data)\nprint("Total:", total)\nprint("Mean:", mean)\nabove = 0\nfor value in data:\n    if value > mean:\n        above = above + 1\nprint("Above the mean:", above)\n'
 'It prints: Total: 10, Mean: 2.0 (Python writes 2 as 2.0 after a division), Above the mean: 2.'))

# ---------------- 9. your turn ----------------
put('p6l9-try1',try_slide('p6l9-try1','31–32 MIN','Your turn: find the mean','Whiteboards. Then do a balance check.',[('a','7, 8, 9, 10, 11','9'),('b','2, 4, 4, 10','5'),('c','0, 0, 6, 6, 3','3')],
 'Whiteboards. a) 45 ÷ 5 = 9 (evenly spaced: the middle value). b) 20 ÷ 4 = 5: not one of the values; check −3, −1, −1, +5 balances. c) 15 ÷ 5 = 3: both zeros count. Anyone who wrote 5 for c divided by 3 values; anyone who wrote 4 for b found the middle, not the mean.',44))

# ---------------- 10. worked example 2 ----------------
m2=DK['mini2']
body=h2('Missing value: use the total')+card(p(m2['body'][0]+' What is the 4th score?',40,700))
body+=step(1,'Mean × how many = total.  4 × 15 = 60.',top=420,size=36)
body+=step(2,'The three we know: 12 + 18 + 14 = 44.',top=530,size=36)
body+=step(3,'The missing score: 60 − 44 = 16.  Check: 60 ÷ 4 = 15 ✓',top=640,size=36)
body+=pin(128,770,1664,p('What 5th score would keep the mean at 15?   15 itself: it is already level.',34,700),'fade',SOFT,20,'18px 28px')
put('p6l9-we2',sec('p6l9-we2','32–33 MIN',body,
 'Click each step. Think-aloud: '+SC['think'][1]+' The last box: a new value equal to the mean changes nothing (5 × 15 = 75 = 60 + 15). Common mistake: 15 − 12 − 18 … (subtracting from the mean). Ask: "What number do we take the known values away FROM?" (the total).'))

# ---------------- 11. what changes the mean ----------------
put('p6l9-change',try_slide('p6l9-change','33–34 MIN','What changes the mean?','Data: 2, 4, 6. Mean 4. Predict first: up, down or the same? Then the new mean.',
 [('a','Add a new value: 4','same: 4'),('b','Add 1 to every value','up: 5'),('c','Remove the 6','down: 3'),('d','Change the 6 to 18','up: 8')],
 'Predict with thumbs (up, down, sideways) before each click. a) 16 ÷ 4 = 4: a value equal to the mean keeps it the same. b) 3, 5, 7: 15 ÷ 3 = 5; every value up by 1, so the mean goes up by 1. c) 2, 4: 6 ÷ 2 = 3; removing a value above the mean pulls it down. d) 2 + 4 + 18 = 24, 24 ÷ 3 = 8: the total went up by 12, shared by 3 values, so the mean went up by 4. Worksheet Q3 is like this with different data.',38))

# ---------------- 12. key idea ----------------
body=h2(DK['keyHead'])+card(p(DK['keyBig'],44,700))+card(p(DK['keySmall'],36,600,MUTED))
put('p6l9-key',sec('p6l9-key','34–35 MIN',body,'Say the key idea together: "Mean = total ÷ how many. Total = mean × how many." Common mistakes to watch for during the worksheet: (1) '+L['mistakes'][0]+' (2) '+L['mistakes'][1]+' (3) '+L['mistakes'][2]))

# ---------------- 13. break ----------------
put('p6l9-break',color_slide('p6l9-break',TEAL,'35–40 MIN','Brain break','Dice jumps! Roll two dice on screen. Everyone does that many star jumps. Three rounds.','Then: what was the mean number of jumps per round? A drink of water and back to the screen.',
 'Five minutes. Use any online dice roller. After 3 rounds, add the three totals and divide by 3 together (the answer may be a decimal: that is fine). Online: children stay in view of the camera and move in place.'))

# ---------------- 14. teach before page 1: misleading mean ----------------
vals=[1,2,2,3,4,5,25]
g=''.join(f'<rect x="{10+i*170}" y="10" width="150" height="110" rx="16" fill="{YEL if i==3 else (SKY if v==2 else WHITE)}" stroke="{NAVY}" stroke-width="4"/>'+T(85+i*170,86,v,54) for i,v in enumerate(vals))
body=h2('When the mean misleads')+p('Goals scored by 7 players in a season, in order:',34,600,MUTED)+pin(128,320,1200,svg(1200,130,g,'Seven boxes in order: 1, 2, 2, 3, 4, 5, 25. The middle box, 3, is yellow. The two 2s are blue.'))
body+=step(1,'Mean: 42 ÷ 7 = 6. But 6 of the 7 players scored fewer than 6!',top=480,size=34)
body+=step(2,'Median: the middle value in order. 7 values, so the 4th: 3.',top=590,size=34)
body+=step(3,'Mode: the value that appears most often: 2.',top=700,size=34)
body+=pin(1380,320,412,p('One big value (25) pulls the mean up. The median does not move.',30,700),'fade',SOFT,20,'18px 24px')
put('p6l9-teachmed',sec('p6l9-teachmed','40–42 MIN',body,
 'Teach before worksheet page 1 (Q4). Think-aloud: '+SC['think'][2]+' Ask: "If the 25 became 250, what happens to the mean? To the median?" (Mean (17 + 250) ÷ 7 is about 38; the median is still 3.) Point out: for an even number of values the median is halfway between the middle two (we will not need that today). The mode is useful for things like shoe sizes: the shop wants the most common size.'))

# ---------------- 15/16. worksheet page 1 ----------------
put('p6l9-ws1',ws_preview('p6l9-ws1','42–53 MIN','Worksheet page 1: with your partner',[('Q1','Books read. Total, mean, then the balance check.'),('Q2','Siti’s game scores. Turn the mean into a total first.'),('Q3','Predict, then work out: what does each change do to the mean?'),('Q4','Pocket money. Mean, median, mode: which is fair?')],'Total = mean × how many. Then subtract what you know.',
 'Minutes 42 to 53. Walk around (or visit breakout rooms). Ask "What is the total? How many values?" and "Predict before you calculate." In Q3 insist on a prediction in words before the number.'))
put('p6l9-ws1ans',check_slide('p6l9-ws1ans','53–55 MIN','Page 1: check together',[('Q1','30;  mean 6;  −2, +1, −4, +2, +3 add up to 0'),('Q2','a) 68   b) 19   c) 22'),('Q3','a) same, 10   b) up, 13   c) down, 9   d) up, 16'),('Q4','$22;  $15;  $12;  6 pupils.  Not fair: the median $15 is more typical')],
 'Click after pairs explain. Q2: 17 × 4 = 68; 68 − 15 − 20 − 14 = 19; for a mean of 18 over 5 games the total must be 90, so 90 − 68 = 22. Q3: a) 60 ÷ 6 = 10; b) every value up 3; c) 36 ÷ 4 = 9; d) the total goes up by 30, shared by 5: up 6, so 16. Q4: 154 ÷ 7 = 22; in order the 4th value is $15; $12 appears twice; only the $69 pupil gets more than $22.'))

# ---------------- 17. teach before page 2: any length ----------------
fixed=['set total to 0','set i to 1',{'c':'repeat 5','body':['change total by (item i of data)','change i by 1']},'say (total / 5)']
body=h2('Make it work for ANY list')+p('We add an 8 to the goals list: 3, 0, 4, 1, 2, 8. True mean: 18 ÷ 6 = 3.',34,600,MUTED)
body+=pin(128,330,820,p('This program says 2. Why?',34,800,TEAL)+code_svg(fixed,'Code blocks: set total to 0, set i to 1, repeat 5 (change total by item i of data, change i by 1), say total divided by 5',28),None,WHITE,24,'20px 28px')
body+=step(1,'repeat 5 stops after item 5, so the 8 is never added. Total is still 10.',left=1010,top=330,width=782,size=32)
body+=step(2,'And it divides by 5, not 6.',left=1010,top=500,width=782,size=32)
body+=step(3,'Fix: use (length of data) in BOTH places. Now it says 18 ÷ 6 = 3 ✓',left=1010,top=610,width=782,size=32)
put('p6l9-teachany',sec('p6l9-teachany','55–57 MIN',body,
 'Teach before worksheet page 2 (Q5 asks which blocks must change). Think-aloud: "A number typed into the code is fixed. When the list grows, the program does not know. length of data is always the right count, so the loop visits every item and we divide by the right number." Try it live: add 8 to the list and run both versions.'))

# ---------------- 18. teach before page 2: count with if ----------------
cnt=['set zeros to 0','set i to 1',{'c':'repeat (length of data)','body':[{'c':'if (item i of data) = 0 then','body':['change zeros by 1']},'change i by 1']},'say zeros']
body=h2('Count with an if')+p('How many matches had 0 goals? data: 3, 0, 4, 1, 2',34,600,MUTED)
body+=pin(128,320,800,code_svg(cnt,'Code blocks: set zeros to 0, set i to 1, repeat length of data (if item i of data equals 0 then change zeros by 1; change i by 1), say zeros',28))
body+=step(1,'Start the counter at 0, outside the loop.',left=1010,top=330,width=782,size=32)
body+=step(2,'Inside the loop: IF the item fits the rule, change the counter by 1.',left=1010,top=440,width=782,size=32)
body+=step(3,'Only item 2 is 0, so it says 1.',left=1010,top=600,width=782,size=32)
put('p6l9-teachif',sec('p6l9-teachif','57–58 MIN',body,
 'Teach before worksheet page 2 (Q6 plans a counting program with a different rule). Ask: "What would go wrong if set zeros to 0 were inside the loop?" (It would be reset every time, so the answer could only be 0 or 1.) "How would you count the matches with MORE than 2 goals?" (change the rule to item i of data > 2: it says 2, for the 3 and the 4.)'))

# ---------------- 19/20. worksheet page 2 ----------------
put('p6l9-ws2',ws_preview('p6l9-ws2','58–72 MIN','Worksheet page 2: on your own',[('Q5','Trace the mean program, one row per loop. Then make it work for any length.'),('Q6','Singapore temperatures: the mean, then plan the code that counts the hot days.')],'Finished early? Build Q6 in Scratch and test it. Then Stretch and Challenge.',
 'Children work alone. Early finishers build Q6 in Scratch with the temperatures in a list called temps and check that it says what they predicted; Python fans use the box on the page. Note who needs a short catch-up.'))
put('p6l9-ws2ans',check_slide('p6l9-ws2ans','72–75 MIN','Page 2: check together',[('Q5','total: 5, 14, 20, 32.  Says 8.  Use (length of scores) in repeat and in say: now 9'),('Q6','31 °C;  3 days;  blanks: mean and count;  it says 3')],
 'Click after a child explains. Q5: i goes 1, 2, 3, 4 and item i is 5, 9, 6, 12; 32 ÷ 4 = 8; with 13 added the total is 45 and the length is 5, so 9. Q6: 29 + 31 + 33 + 30 + 32 + 34 + 28 = 217, 217 ÷ 7 = 31; hotter than 31: 33, 32 and 34. The if compares item i of temps with mean, and change count by 1 counts it.'))

# ---------------- 21. stretch (new items) ----------------
st=[('1.','The mean of 6 numbers is 7. Five of them are 3, 5, 8, 9 and 10. What is the sixth?'),('2.','Find ALL the sets of 3 different counting numbers with a mean of 5 and a median of 3.'),('3.','A class of 30 has a mean score of 70. The 10 boys have a mean of 64. What is the mean of the 20 girls?')]
put('p6l9-stretch',sec('p6l9-stretch','For early finishers',h2('Stretch')+numcards(st,36),
 'Answers: 1) 7 (6 × 7 = 42; 3 + 5 + 8 + 9 + 10 = 35; 42 − 35 = 7). 2) Two sets: 1, 3, 11 and 2, 3, 10 (total 15; the middle is 3; the smallest is 1 or 2, so the largest is 15 − 3 − 1 = 11 or 15 − 3 − 2 = 10). 3) 73 (30 × 70 = 2100; 10 × 64 = 640; 2100 − 640 = 1460; 1460 ÷ 20 = 73). Test any of them in code: put the numbers in a list and run the mean program.'))

# ---------------- 22. challenge ----------------
ch=QB['challenge'][:2]
put('p6l9-challenge',sec('p6l9-challenge','62–75 MIN',h2('Challenge')+numcards([(f'{i+1}.',c['q']) for i,c in enumerate(ch)],36),
 'Use as a pair challenge or in talk time. Ask for the reason every time. More are in the question bank. Answers: 1) '+ch[0]['a']+'  2) '+ch[1]['a']))

# ---------------- 23. challenge: see it ----------------
base=330
q1=''.join(f'<rect x="{20+i*60}" y="{base-88}" width="46" height="88" rx="6" fill="{SKY}" stroke="{NAVY}" stroke-width="3"/>' for i in range(5))
q1+=f'<line x1="10" y1="{base-88}" x2="320" y2="{base-88}" stroke="{TEAL}" stroke-width="4" stroke-dasharray="10 7"/>'+T(160,base+40,'5 numbers, mean 8',28)
q1+=''.join(f'<rect x="{440+i*60}" y="{base-77}" width="46" height="77" rx="6" fill="{YEL}" stroke="{NAVY}" stroke-width="3"/>' for i in range(4))
q1+=f'<line x1="430" y1="{base-77}" x2="680" y2="{base-77}" stroke="{TEAL}" stroke-width="4" stroke-dasharray="10 7"/>'+T(560,base+40,'4 numbers, mean 7',28)
q1+=f'<rect x="270" y="{base+70}" width="240" height="90" rx="14" fill="{WHITE}" stroke="{RED}" stroke-width="4" stroke-dasharray="12 8"/>'+T(390,base+128,'removed: ?',30,RED)
q1+=T(380,60,'Find the totals first.',30,TEAL)
q2=''.join(f'<rect x="{20+i*62}" y="{base-99}" width="48" height="99" rx="6" fill="{SKY}" stroke="{NAVY}" stroke-width="3"/>' for i in range(9))
q2+=f'<rect x="{20+9*62}" y="{base-200}" width="48" height="200" rx="6" fill="{WHITE}" stroke="{RED}" stroke-width="4" stroke-dasharray="10 7"/>'+T(20+9*62+24,base-150,'?',40,RED)
q2+=f'<line x1="10" y1="{base-99}" x2="640" y2="{base-99}" stroke="{TEAL}" stroke-width="4" stroke-dasharray="10 7"/>'+T(660,base-90,'30',28,TEAL,'start')
q2+=f'<line x1="10" y1="{base-106}" x2="640" y2="{base-106}" stroke="{RED}" stroke-width="3"/>'+T(660,base-118,'32',28,RED,'start')
q2+=T(370,base+40,'9 games: mean 30',28)+T(370,base+85,'After game 10: mean 32',28,RED)+T(370,60,'How many points in game 10?',30,TEAL)
cardsvg=lambda t,s,a: f'<div style="background:{WHITE};border-radius:24px;padding:20px 24px;display:flex;flex-direction:column;gap:10px;flex:1;min-width:0"><p style="font-size:30px;font-weight:700;color:{TEAL}">{E(t)}</p>'+svg(760,base+180,s,a,'100%','auto').replace('height:auto;flex:none','height:auto;display:block')+'</div>'
body=h2('Challenge: see it')+f'<div style="display:flex;gap:32px;align-items:flex-start">'+cardsvg('Q1: one number removed',q1,'Five bars levelled at 8, then four bars levelled at 7, and a dashed box for the removed number')+cardsvg('Q2: the 10th game',q2,'Nine bars at a mean of 30, a dashed tenth bar with a question mark, and a higher line for the new mean 32')+'</div>'
put('p6l9-chdiag',sec('p6l9-chdiag','62–75 MIN',body,'Show after pairs have tried the Challenge, or if they are stuck. The diagrams show the problem, not the answer. Ask: What do you notice? What do we know? What do we not know yet? Which totals can you find? Answers are in the Go further slide notes.'))

# ---------------- 24. challenge walk-through ----------------
body=h2('Challenge: walk-through')+pin(128,250,800,p('Q1(a): compare the totals',38,800,TEAL))
for i,t in enumerate(['Total of 5: 5 × 8 = 40','Total of 4: 4 × 7 = 28','Removed: 40 − 28 = 12','(b) Above the mean: lowers it. Below: raises it.']): body+=pin(128,330+i*120,800,p(t,32),'rise',WHITE)
body+=pin(992,250,800,p('Q2(a): total needed, total so far',38,800,TEAL))
for i,t in enumerate(['Needed after 10 games: 10 × 32 = 320','So far after 9 games: 9 × 30 = 270','Game 10: 320 − 270 = 50 points','(b) Best case: 270 + 60 = 330, 330 ÷ 10 = 33']): body+=pin(992,330+i*120,800,p(t,30),'rise',WHITE)
put('p6l9-chwalk',sec('p6l9-chwalk','Challenge',body,'Use after pairs have tried, with the "see it" slide. The big idea in both: work with TOTALS, not means. Q2 also has a levelling explanation: the 10th score must bring itself up to 32 and also give 2 extra to each of the 9 earlier games. Q1(b): Ali is wrong. Removing a number ABOVE the mean (like 12) lowers the mean; removing one BELOW the mean raises it. Example: 4, 6, 8, 10, 12 has mean 8; remove 4 and the mean of 6, 8, 10, 12 is 9. Check for (a): 28 + 12 = 40 and 40 ÷ 5 = 8. Q2(b): the best she can do is 60 in game 10, so the total is 270 + 60 = 330 and the mean is 33. Test either in Scratch: put the numbers in a list and run the mean program.'))

# ---------------- 25. talk ----------------
body=h2('Talk time')+card(chip('TALK TIME',YEL,NAVY)+p(L['share'],42))+card(p('Sentence starters:',34,400,MUTED)+p('“I noticed that …”   “I tested it by …”   “I know because …”',38))
put('p6l9-talk',sec('p6l9-talk','75–82 MIN',body,'Minutes 75 to 82. Pairs talk for 2 minutes, then share. Ask them to test ideas in the mean program. Answer: '+SC['talkAns']+' Praise the reasons, not only the answers.'))

# ---------------- 26. exit ----------------
body=h2('Exit ticket')+card(chip('EXIT TICKET')+p(L['exit']['q'],44))+card(p('Write your answer on a slip of paper or in the chat. Show your working. Then collect your stamp.',34))
put('p6l9-exit',sec('p6l9-exit','82–90 MIN',body,'Minutes 82 to 90. Answer: '+L['exit']['a']+' '+SC['close'][0]+' '+SC['close'][1]+' Extension: '+L['extension']))

# ---------------- write ----------------
for f in os.listdir(SL):
    if f.endswith('.html') and f[:-5] not in S: os.remove(os.path.join(SL,f))
for i,h in S.items(): open(os.path.join(SL,i+'.html'),'w').write(h)
deck={'v':4,'createdOnFiles':{'v':1,'at':datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')},'lists':'css','title':'Math Inquirers P6: Lesson 9 – Data Detectives','order':ORDER,'cover':'p6l9-title',
      'sections':{'s1':{'description':'Warm-up and explore: class data in a list','start':'p6l9-title'},'s2':{'description':'Teach: the mean, the mean program, missing values','start':'p6l9-teach1'},'s3':{'description':'Worksheet with teaching before each page','start':'p6l9-break'},'s4':{'description':'Stretch, challenge, talk and exit','start':'p6l9-stretch'}},
      'faces':{'fredoka':{'family':'Fredoka','href':'https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&display=swap'},'nunito-sans':{'family':'Nunito Sans','href':'https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@400;600;700&display=swap'}},'designSystems':[]}
json.dump(deck,open(os.path.join(D,'deck.json'),'w'),indent=1,ensure_ascii=False)
print(len(ORDER),'slides')

import p6_gaps; p6_gaps.apply(9)
