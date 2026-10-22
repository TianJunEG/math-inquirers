"""Math Inquirers P4, Lesson 9: Data Detectives (tables and line graphs). Writes split/p4l9/project (deck.json + slides/*.html).
Every graph is drawn to scale from the numbers stated on the slide; every answer was checked with a script."""
import json,os,sys,datetime
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,H)
import slidekit
from slidekit import *
slidekit.FOOT='Math Inquirers P4 Holiday Program  •  Notice it. Test it. Explain why.'
D=os.path.join(H,'..','split','p4l9','project'); os.makedirs(os.path.join(D,'slides'),exist_ok=True)
S={}
def put(i,h): S[i]=h
RED='#D64545'; FOOTX=slidekit.FOOT

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
            f'<p style="font-size:48px;font-weight:600">{E(text)}</p>\n<p style="font-size:36px;color:#D7EFEA">Then: a drink of water and back to our seats.</p>\n'
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
def txt(x,y,s,size=30,fill=NAVY,anchor='middle',weight=700,font='Nunito Sans, Arial',rot=False):
    r=f' transform="rotate(-90 {x} {y})"' if rot else ''
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" fill="{fill}" font-family="{font}"{r}>{E(str(s))}</text>'

# ---------- accurate line graph ----------
class G:
    """Line graph drawn to scale. Points sit on the vertical grid lines. None = no point."""
    def __init__(s,w,h,xl,y0,y1,step,lab,yt,title=None,legend=None,fs=26):
        s.w,s.h,s.xl,s.y0,s.y1=w,h,xl,y0,y1
        s.T=14+(46 if title else 0)+(48 if legend else 0); s.L=104; s.R=w-24; s.B=h-58
        n=len(xl); s.xs=lambda i:s.L+44+i*(s.R-s.L-88)/(n-1); s.ys=lambda v:s.B-(v-y0)*(s.B-s.T)/(y1-y0)
        b=f'<rect x="{s.L}" y="{s.T}" width="{s.R-s.L}" height="{s.B-s.T}" fill="{WHITE}"/>'
        if title: b+=txt((s.L+s.R)/2,36,title,fs,NAVY)
        v=y0
        while v<=y1+1e-9:
            major=abs((v-y0)%lab)<1e-9 or abs((v-y0)%lab-lab)<1e-9
            b+=f'<line x1="{s.L}" y1="{s.ys(v):.1f}" x2="{s.R}" y2="{s.ys(v):.1f}" stroke="{NAVY}" stroke-opacity="{0.3 if major else 0.12}" stroke-width="2"/>'
            if major: b+=txt(s.L-12,s.ys(v)+9,f'{v:g}',fs,NAVY,'end')
            v+=step
        for i,l in enumerate(xl):
            b+=f'<line x1="{s.xs(i):.1f}" y1="{s.T}" x2="{s.xs(i):.1f}" y2="{s.B}" stroke="{NAVY}" stroke-opacity="0.12" stroke-width="2"/>'+txt(s.xs(i),s.B+38,l,fs,NAVY)
        b+=f'<line x1="{s.L}" y1="{s.T-6}" x2="{s.L}" y2="{s.B}" stroke="{NAVY}" stroke-width="5"/><line x1="{s.L}" y1="{s.B}" x2="{s.R}" y2="{s.B}" stroke="{NAVY}" stroke-width="5"/>'
        b+=txt(30,(s.T+s.B)/2,yt,fs,TEAL,rot=True)
        if legend:
            for k,(name,col,mk,dash) in enumerate(legend):
                lx=s.L+20+k*260; ly=(60 if title else 14)+20
                b+=f'<line x1="{lx}" y1="{ly}" x2="{lx+64}" y2="{ly}" stroke="{col}" stroke-width="5"{" stroke-dasharray=\"14 9\"" if dash else ""}/>'+s.mark(lx+32,ly,col,mk)+txt(lx+80,ly+10,name,fs,NAVY,'start')
        s.base=b
    def mark(s,x,y,col,mk):
        return (f'<rect x="{x-10:.1f}" y="{y-10:.1f}" width="20" height="20" fill="{WHITE}" stroke="{col}" stroke-width="5"/>' if mk=='sq'
                else f'<circle cx="{x:.1f}" cy="{y:.1f}" r="10" fill="{YEL}" stroke="{col}" stroke-width="5"/>')
    def line(s,vals,col=NAVY,mk='o',dash=False,width=5):
        d=''; prev=None
        for i,v in enumerate(vals):
            if v is None: prev=None; continue
            d+=('M' if prev is None else 'L')+f'{s.xs(i):.1f} {s.ys(v):.1f} '; prev=v
        out=f'<path d="{d}" fill="none" stroke="{col}" stroke-width="{width}"{" stroke-dasharray=\"14 9\"" if dash else ""}/>' if d.count('L') else ''
        return out+''.join(s.mark(s.xs(i),s.ys(v),col,mk) for i,v in enumerate(vals) if v is not None)
    def svg(s,inner,label,base=True): return svgwrap(s.w,s.h,label,(s.base if base else '')+inner)

# ---------- 1. title ----------
put('p4l9-title',title_slide('p4l9-title','LESSON 9  •  WEEK 5','Data Detectives','Tables and line graphs',
 'Read line graphs and tables, find missing values, compare two lines and catch a graph that misleads.',
 'Objective: Read values and trends from line graphs (using the scale), find the biggest increase or decrease, find missing values in tables and graphs from totals and patterns, compare two lines on one graph, and explain why a graph with a different scale can mislead. '
 'Thinking strategies today: READ THE SCALE FIRST, LIST THE CHANGES, and WORK FROM THE TOTAL. '
 'Materials: Mini whiteboards, a ruler and two coloured pencils per child, printed blank graph grids (or squared paper), the queue table for the explore task. '
 'Online: children use a printed blank grid or squared paper and hold it up to the camera; the tutor plots on the slide graphs while children call out where each point goes. '
 'Time plan: Warm-up check 1 to 4 (two questions on the key idea; children who get both right and can say why start on the Think Harder pages at minute 34), warm-up game 4 to 6 (one short round), quick questions 6 to 8, explore 8 to 18, teaching 18 to 30 (click to reveal each step and answer; the "your turn" slides are optional, skip them if short of time), brain break 30 to 34, worksheet page 1 from 34 to 50 and check together 50 to 53, short teaching before page 2 from 53 to 58, worksheet page 2 from 58 to 76 and check together 76 to 80, talk time 80 to 85, exit ticket 85 to 88, What was hard? reflection 88 to 90. The Challenge slides and the Think Harder pages are for early finishers and for take-home: they have no fixed time slot. Online: page 1 is pair work, so allow about 2 minutes to move into and out of breakout rooms (or run page 1 as a whole-group screen-share if there are only 8 children).'))

# ---------- 2. warm-up: which graph tells the story ----------
def mini(kind):
    pts={'A':'24,150 172,32 320,150','B':'24,92 320,92','C':'24,150 320,32','D':'24,32 320,150'}[kind]
    g=f'<line x1="14" y1="10" x2="14" y2="166" stroke="{NAVY}" stroke-width="5"/><line x1="14" y1="166" x2="336" y2="166" stroke="{NAVY}" stroke-width="5"/>'
    g+=f'<polyline points="{pts}" fill="none" stroke="{TEAL}" stroke-width="8" stroke-linejoin="round" stroke-linecap="round"/>'
    names={'A':'goes up, then down','B':'stays flat','C':'goes up steadily','D':'goes down steadily'}
    return svgwrap(340,176,f'Graph {kind}: a line that {names[kind]}',g)
body=h2('Warm-up: which graph tells the story?')
for i,k in enumerate('ABCD'):
    body+=pin(128+i*424,240,392,f'<p style="font-family:{HF};font-size:40px;font-weight:600;color:{TEAL}">Graph {k}</p>'+mini(k),None,WHITE,24,'14px 24px',f'box-sizing:border-box;border:4px solid {NAVY}')
stories=[('1.','A bath filling with water from the tap','C'),('2.','People at a hawker centre from 10 am to 3 pm','A'),('3.','The height of a candle as it burns','D'),('4.','Money in a piggy bank that nobody touches','B')]
for i,(a,b,c) in enumerate(stories):
    body+=qrow(128,540+i*92,1250,a,b,32)+answer(1420,540+i*92,372,'Graph '+c)
put('p4l9-warm1',sec('p4l9-warm1','4–6 MIN',body,
 'Minutes 4 to 6 (one short round, about 2 minutes: the Warm-up check came first). Which graph tells the story? The graphs have no numbers on purpose: we read the SHAPE. Read story 1 aloud. Children point at (or write the letter of) the matching graph, then say why before you click. Clicks reveal the answers in order. '
 'Answers: 1) Graph C: the water goes up steadily. 2) Graph A: people arrive for lunch, then leave. 3) Graph D: the candle gets shorter steadily. 4) Graph B: nothing changes, so the line is flat. '
 'Ask: "Could the hawker centre graph be another shape on a rainy day?" "Make up a story for a line that goes DOWN, then UP." (e.g. water in a bathtub as it drains and is filled again). Listen for "steep" and "flat": we use those words all lesson.'))

# ---------- 3. quick questions ----------
qs=[('1.','75 − 48 = ?','27'),('2.','Scale in 10s: halfway between 40 and 50?','45'),('3.','38 + 47 + 15 = ?','100'),('4.','Four numbers total 200. Three are 45, 60 and 50. The fourth?','45'),('5.','Bigger change: 120 to 95, or 60 to 90?','60 to 90 (30)')]
body=h2('Quick questions')+''.join(qrow(128,250+i*125,1250,a,b,36) for i,(a,b,c) in enumerate(qs))+''.join(answer(1420,250+i*125,372,c) for i,(a,b,c) in enumerate(qs))
put('p4l9-warm2',sec('p4l9-warm2','6–8 MIN',body,'Minutes 6 to 8. Whiteboards up together, then click. Each one is a skill for today: 1) 27, the size of a change. 2) 45, reading halfway between two grid lines. 3) 100: add 85 + 15. 4) 45: 45 + 60 + 50 = 155, 200 − 155 = 45. 5) 60 to 90 is a change of 30; 120 to 95 is a change of 25. A change can go up or down: we compare the SIZE of the change.'))

# ---------- 4. explore ----------
times=['11:00','11:30','12:00','12:30','1:00','1:30','2:00']; ppl=[4,9,18,22,15,7,3]
g=txt(20,52,'Time',28,TEAL,'start',800)+txt(20,122,'People',28,TEAL,'start',800)
for i,(t,n) in enumerate(zip(times,ppl)):
    x=150+i*118
    g+=f'<rect x="{x}" y="10" width="118" height="64" fill="{SOFT}" stroke="{NAVY}" stroke-width="3"/><rect x="{x}" y="74" width="118" height="70" fill="{WHITE}" stroke="{NAVY}" stroke-width="3"/>'+txt(x+59,52,t,28)+txt(x+59,122,n,34)
gx,gy,gw,gh=1150,10,430,166
for k in range(1,6): g+=f'<line x1="{gx}" y1="{gy+k*gh/6:.0f}" x2="{gx+gw}" y2="{gy+k*gh/6:.0f}" stroke="{NAVY}" stroke-opacity=".18" stroke-width="2"/>'
for k in range(1,7): g+=f'<line x1="{gx+k*gw/7:.0f}" y1="{gy}" x2="{gx+k*gw/7:.0f}" y2="{gy+gh}" stroke="{NAVY}" stroke-opacity=".18" stroke-width="2"/>'
g+=f'<line x1="{gx}" y1="{gy}" x2="{gx}" y2="{gy+gh}" stroke="{NAVY}" stroke-width="5"/><line x1="{gx}" y1="{gy+gh}" x2="{gx+gw}" y2="{gy+gh}" stroke="{NAVY}" stroke-width="5"/>'+txt(gx+gw/2,gy+gh+32,'your graph',26,MUTED,weight=600)
steps=''.join(f'<li>{E(s)}</li>' for s in ['Look at the table: people in the queue at a chicken rice stall.','Choose a scale for the side: how much is each line worth? Not sure? Try 2 per line.','Plot each point and join the points with straight lines.','Write three things your graph tells you.'])
body=h2('Explore: what to do')+card(chip('EXPLORE')+f'<ol style="font-size:32px;font-weight:600;padding-left:52px;display:flex;flex-direction:column;gap:6px">{steps}</ol>')
body+=card(svgwrap(1600,214,'Table of people in a queue every half hour from 11:00 to 2:00: 4, 9, 18, 22, 15, 7, 3, and an empty graph grid',g),extra='padding:20px 32px')
put('p4l9-explore1',sec('p4l9-explore1','8–13 MIN',body,'Minutes 8 to 13. Pairs plot the queue on a blank grid (online: printed grid or squared paper on camera). Ask them to predict first: when is the queue longest? Let pairs choose their own scale: lines worth 1, 2 or 5 all work if the lines are equal steps; a scale of 1 needs 22 lines. Hint for anyone unsure: try 2 per line (the biggest number is 22, so 12 lines are enough). Early finishers: between which two times did the queue grow the most? Can you see it without working out every change?'))
body=h2('Explore: talk about it')+numcards([('1.','When was the queue longest?'),('2.','Between which two times did the queue grow the most?'),('3.','When is the best time to buy chicken rice? Why?')],40)
put('p4l9-explore2',sec('p4l9-explore2','13–18 MIN',body,'Minutes 13 to 18. Gather pairs and compare graphs: are the shapes the same even if the scales are different? (Yes, if the steps are equal.) Answers: 1) 12:30, with 22 people. 2) 11:30 to 12:00: up 9 (the steepest line going up; the changes are up 5, up 9, up 4, down 7, down 8, down 4). 3) 2:00 (3 people) or 11:00 (4 people): the shortest queues. Do NOT teach the steepest-line idea yet if nobody notices it: the next slides teach it.'))

# ---------- 5. teach: reading a line graph ----------
DAYS=['Mon','Tue','Wed','Thu','Fri']; lib=[25,40,35,60,50]
g=G(940,640,DAYS,0,70,5,10,'Books borrowed',title='Library books borrowed each day')
ov=f'<line x1="{g.xs(1):.1f}" y1="{g.ys(40):.1f}" x2="{g.L}" y2="{g.ys(40):.1f}" stroke="{RED}" stroke-width="5" stroke-dasharray="12 8"/><line x1="{g.xs(1):.1f}" y1="{g.B}" x2="{g.xs(1):.1f}" y2="{g.ys(40):.1f}" stroke="{RED}" stroke-width="5" stroke-dasharray="12 8"/>'
ov+=f'<line x1="{g.xs(0):.1f}" y1="{g.ys(25):.1f}" x2="{g.L}" y2="{g.ys(25):.1f}" stroke="{TEAL}" stroke-width="5" stroke-dasharray="12 8"/>'
body=h2('Reading a line graph')+pin(128,230,940,g.svg(g.line(lib),'Line graph of library books borrowed: Monday 25, Tuesday 40, Wednesday 35, Thursday 60, Friday 50'))
body+=step(1,'Read the title and the axes: books borrowed, Monday to Friday.',left=1110,top=240,width=682,size=32)
body+=step(2,'Find the scale. Each numbered line is worth 10. The faint lines are 5.',left=1110,top=400,width=682,size=32)
body+=step(3,'Tuesday: up to the point, across to the side: 40. Monday is halfway between 20 and 30: 25.',left=1110,top=560,width=682,size=32)
body+=pin(128,230,940,svgwrap(940,640,'Dashed lines reading Tuesday at 40 and Monday at 25',ov),'fade')
body+=pin(1110,760,682,p('Always find what one line is worth first.',32,800),'fade',SOFT,20,'18px 26px')
put('p4l9-teach1',sec('p4l9-teach1','18–21 MIN',body,'Teach. Click through the steps, then the red and teal reading lines. Think-aloud: "First the title and the axes, so I know what is counted and when. Then the scale: 0, 10, 20 on the numbered lines, so each numbered line is worth 10, and the faint line between is 5. Tuesday\'s point sits on the 40 line. Monday\'s point is halfway between 20 and 30: 25." Ask children to read Wednesday (35), Thursday (60) and Friday (50) on whiteboards. Common mistake: reading each line as 1.'))

# ---------- 6. worked example: biggest change ----------
g=G(860,600,DAYS,0,70,5,10,'Books borrowed')
hi=f'<line x1="{g.xs(2):.1f}" y1="{g.ys(35):.1f}" x2="{g.xs(3):.1f}" y2="{g.ys(60):.1f}" stroke="{YEL}" stroke-width="22" stroke-linecap="round" stroke-opacity=".85"/>'+g.line(lib)
body=h2('Worked example: the biggest change')+pin(128,230,860,g.svg(g.line(lib),'The same library graph: 25, 40, 35, 60, 50'))
for i,t in enumerate(['Mon → Tue: up 15  (40 − 25)','Tue → Wed: down 5  (40 − 35)','Wed → Thu: up 25  (60 − 35)','Thu → Fri: down 10  (60 − 50)']):
    body+=pin(1030,240+i*92,762,p(t,32,700),'rise',WHITE,20,'14px 24px')
body+=pin(128,230,860,svgwrap(860,600,'The line from Wednesday to Thursday highlighted',''.join([hi])),'fade')
body+=answer(1030,620,762,'Biggest increase: Wed → Thu, up 25')
body+=pin(1030,750,762,p('The steeper the line, the bigger the change. Up or down, say which!',30,800),'fade',SOFT,20,'16px 24px')
put('p4l9-we1',sec('p4l9-we1','21–23 MIN',body,'Click to list each change, then the highlight, the answer and the rule. Think-aloud: "I list the change between each pair of neighbours and write up or down. The biggest increase is 25, Wednesday to Thursday. Look: on the graph it is the steepest line going up. So I can spot the biggest change by looking, then check it by working out." Ask: "Which is the biggest DEcrease?" (Thursday to Friday, 10). Worksheet Q1 asks for both.'))

# ---------- 7. your turn ----------
g=G(780,560,DAYS,0,70,5,10,'Books borrowed')
body=h2('Your turn: the library graph')+pin(128,240,780,g.svg(g.line(lib),'The library graph again: 25, 40, 35, 60, 50'))
for i,(q,a) in enumerate([('a) How many books in the 5 days?','210'),('b) Biggest decrease? By how many?','Thu → Fri: 10'),('c) How many more on Thursday than on Monday?','35')]):
    body+=pin(950,250+i*190,500,p(q,32,700),None,WHITE,20,'18px 24px')+answer(1510,250+i*190,282,a)
put('p4l9-try1',sec('p4l9-try1','23–25 MIN • OPTIONAL',body,'Whiteboards, then click. a) 25 + 40 + 35 + 60 + 50 = 210 (make 100s: 40 + 60 and 25 + 35 + 50 = 110). b) Thursday to Friday, down 10 (Tuesday to Wednesday is only down 5). c) 60 − 25 = 35. Watch for children who answer b) with "Friday" only: a change is BETWEEN two days.'))

# ---------- 8. worked example: missing values in a table ----------
W4=[150,150,150,150]
rows0=[['Ali','26','?','61'],['Mei','?','18','50'],['Ravi','40','27','?'],['Total','?','?','?']]
rows1=[['Ali','26','35','61'],['Mei','32','18','50'],['Ravi','40','27','67'],['Total','98','80','178']]
body=h2('Worked example: missing values in a table')+p('Stickers collected in June and July.',32,600,MUTED)
body+=trow(128,300,['','June','July','Total'],W4,None,True,34)
for i,r in enumerate(rows0): body+=trow(128,390+i*90,r,W4,None,False,34)
sl=['Ali’s row: 61 − 26 = 35','Mei’s row: 50 − 18 = 32','Ravi’s row: 40 + 27 = 67','Add down each column: June 98, July 80']
for i in range(4):
    body+=step(i+1,sl[i],left=1000,top=300+i*110,width=792,size=32)
    body+=trow(128,390+i*90,rows1[i],W4,'rise',False,34)
body+=answer(128,780,1664,'Check: 98 + 80 = 178  and  61 + 50 + 67 = 178 ✓')
put('p4l9-we2',sec('p4l9-we2','25–27 MIN',body,'Click: each step, then its row fills in. Think-aloud: "A row must add up to its total. Ali has 26 and a missing number, total 61: 61 − 26 = 35. Then Mei. Ravi\'s total is the two numbers added. Last, I add down the columns. Then the best part: the check. The column totals and the row totals must both make the same grand total, 178. If they do not, I have made a mistake somewhere." Worksheet Q2 is the same kind of table.'))
put('p4l9-try2',try_slide('p4l9-try2','27–29 MIN • OPTIONAL','Your turn: missing values','Use the total. Then check.',[('a','Mon 30, Tue 45, Wed 35, Thu ?  Total 150.','40'),('b','4A has 28. 4A and 4B have 60 together. 4B?','32'),('c','A row total is 90. Both numbers are the same.','45 and 45')],'Whiteboards. a) 30 + 45 + 35 = 110, 150 − 110 = 40. b) 60 − 28 = 32. c) 90 shared equally: 45 and 45. Check each by adding back up to the total.',36))

body=h2('Key idea: scale first, then the changes')+card(p('Read the scale before you read a point. The steeper the line, the bigger the change.',44,700))+card(p('Totals help you find missing values. Check where the scale starts before you compare two graphs.',38,600,MUTED))
put('p4l9-key',sec('p4l9-key','29–30 MIN',body,'Say the key idea together. Common mistakes to watch for during the worksheet: (1) Reading the scale as 1 for each line when each line is worth 10 (or 5), so 75 is read as 7 and a half. (2) Looking only for the biggest increase and missing a bigger decrease, or comparing the heights of points instead of the change between them. (3) Comparing two graphs by how steep the lines look without checking where each scale starts and what each line is worth.'))
put('p4l9-break',break_slide('p4l9-break','30–34 MIN','Human line graph. The tutor tells a story: "the temperature rises slowly, then drops fast". Move your arm like the line: slow climb, fast drop, flat.','Four minutes. Stories to call: a slow climb then flat; a fast drop; up, up, up then a crash; flat, then a sudden jump. Online: children stay in view of the camera and move in place.'))

# ---------- worksheet page 1 ----------
put('p4l9-ws1',ws_preview('p4l9-ws1','34–50 MIN','Worksheet page 1: with your partner',[('Q1','The sugarcane juice graph. Read the scale first, then list the changes.'),('Q2','The library table. Use the totals, then check both ways.')],'Stuck? Write the change between each pair of days, with up or down.','Minutes 34 to 50. Walk around. Ask "What is one line worth?" and "How can you check?" before giving any help. Q1d asks for a reason from the story: the stall is next to an office.'))
put('p4l9-ws1ans',checks('p4l9-ws1ans','50–53 MIN','Page 1: check together',[('Q1','a) 75; 55   b) Wed → Thu, up 25   c) Fri → Sat, down 40   d) the steepest line down; e.g. offices are closed at the weekend'),('Q2','4A 47,  4B 41,  4C 97.  Week 1 124, Week 2 128, total 252.   a) 4B   b) 146')],
 'Click each answer after a pair explains. Q1: the changes are up 15, down 5, up 25, down 10, down 40, up 5. Saturday and Sunday: 25 + 30 = 55. Q2: 85 − 38 = 47, 70 − 29 = 41, 45 + 52 = 97; check 124 + 128 = 252 = 85 + 70 + 97. b) Week 3 is 6 more for each of the 3 classes: 128 + 18 = 146.',gapy=200))

# ---------- teach before page 2: two lines ----------
WK=['Wk 1','Wk 2','Wk 3','Wk 4','Wk 5']; P=[4,8,12,16,20]; Q=[10,12,14,16,18]
g=G(900,640,WK,0,22,2,4,'Height (cm)',title='Heights of two plants',legend=[('Plant P',TEAL,'o',False),('Plant Q',RED,'sq',True)])
body=h2('Two lines on one graph')+pin(128,230,900,g.svg(g.line(P,TEAL)+g.line(Q,RED,'sq',True),'Two lines: plant P grows 4, 8, 12, 16, 20 cm and plant Q grows 10, 12, 14, 16, 18 cm in weeks 1 to 5'))
body+=step(1,'Where the lines cross, the values are the same: Week 4, 16 cm each.',left=1070,top=240,width=722,size=32)
body+=step(2,'The gap between the lines is the difference. Week 1: 10 − 4 = 6 cm.',left=1070,top=400,width=722,size=32)
body+=step(3,'The steeper line grows faster: P grows 4 cm a week, Q grows 2 cm.',left=1070,top=560,width=722,size=32)
body+=pin(1070,730,440,p('Week 5: how much taller is P?',30,700),None,WHITE,20,'16px 22px')+answer(1550,730,242,'2 cm')
put('p4l9-teachtwo',sec('p4l9-teachtwo','53–55 MIN',body,'Teach before worksheet page 2 (Q3 has two lines). Use the key (legend) first: "Which line is which?" Click the steps. Think-aloud: "Q starts taller, but P grows faster: its line is steeper. Every week P catches up by 2 cm. The gap was 6, then 4, then 2, then 0: they cross at week 4. After that P is taller." Your turn: 20 − 18 = 2 cm. Do not do Q3 for them: Ali and Mei have different numbers.'))

# ---------- teach: same step each time ----------
DY=['Day 1','Day 2','Day 3','Day 4','Day 5']; full=[8,12,16,20,24]
g=G(860,540,DY,0,28,2,4,'Laps swum',title='Laps Ben swims each day')
body=h2('Same jump each time: fill the gaps')+card(p('Ben swims the same number of laps more each day. Day 1: 8 laps. Day 4: 20 laps.',36,700))
body+=pin(128,370,860,g.svg(g.line([8,None,None,20,None],NAVY),'Two points: day 1 at 8 laps and day 4 at 20 laps, with days 2, 3 and 5 empty'))
body+=step(1,'Day 1 to Day 4 is 3 jumps, not 4.',left=1030,top=380,width=762,size=32)
body+=step(2,'20 − 8 = 12.  12 ÷ 3 = 4 laps each jump.',left=1030,top=500,width=762,size=32)
body+=step(3,'Day 2: 12,  Day 3: 16,  Day 5: 24.',left=1030,top=620,width=762,size=32)
body+=pin(128,370,860,svgwrap(860,540,'The full line: 8, 12, 16, 20, 24',g.line(full,TEAL)),'fade')
body+=pin(1030,750,420,p('Laps in the 5 days?',30,700),None,WHITE,20,'16px 22px')+answer(1510,750,282,'80')
put('p4l9-teachsteps',sec('p4l9-teachsteps','55–56 MIN',body,'Teach before worksheet page 2 (Q4, Siti\'s pages). Ask first: "How many jumps from Day 1 to Day 4?" Many children say 4. Count the gaps on the graph: 1 to 2, 2 to 3, 3 to 4: 3 jumps. Click the steps, then the full line appears. Check: 8, 12, 16, 20, 24 all go up by 4. Total: 8 + 12 + 16 + 20 + 24 = 80 (or 5 days × the middle day, 16).'))

# ---------- teach: check the scale ----------
cars=[52,54,56,58]; D4=['Mon','Tue','Wed','Thu']
g1=G(800,440,D4,0,60,10,10,'Cars',title='Graph 1'); g2=G(800,440,D4,50,60,2,2,'Cars',title='Graph 2')
body=h2('Check the scale!')+pin(128,230,800,g1.svg(g1.line(cars),'Graph 1: cars 52, 54, 56, 58 on a scale from 0 to 60. The line looks almost flat.'))
body+=pin(992,230,800,g2.svg(g2.line(cars),'Graph 2: the same numbers on a scale from 50 to 60. The line looks very steep.'))
body+=pin(128,690,1664,p('Same numbers: 52, 54, 56, 58. Both went up by only 6 cars! Graph 2 starts at 50 and each line is 2.',34,700),'fade',WHITE,20,'18px 28px')
body+=pin(128,800,1664,p('Before you compare graphs: where does the scale start? What is each line worth?',34,800),'fade',SOFT,20,'18px 28px')
put('p4l9-teachscale',sec('p4l9-teachscale','56–58 MIN',body,'Teach before worksheet page 2 (Q5, the two shops). Ask first: "Which car park got much busier?" Most children say Graph 2. Then let them read the numbers from both graphs: they are the same! Click. Think-aloud: "Graph 2 does not start at 0. It starts at 50, and each line is only 2, so a small change looks huge. Graph 1 starts at 0, so the same change looks tiny. Neither graph is wrong, but Graph 2 can trick you." Ask: "Who might want to draw Graph 2? Why?" (someone who wants the change to look big, like an advert).'))

# ---------- worksheet page 2 ----------
put('p4l9-ws2',ws_preview('p4l9-ws2','58–76 MIN','Worksheet page 2: on your own',[('Q3','Two money boxes. Use the key. Where do the lines cross?'),('Q4','Siti’s pages. Count the jumps, not the days.'),('Q5','Two shops. Read both scales before you agree with Ravi.')],'Finished early? Stretch and Challenge come next.','Children work alone. Note who still reads every line as 1, and who compares the graphs by their look only.'))
put('p4l9-ws2ans',checks('p4l9-ws2ans','76–80 MIN','Page 2: check together',[('Q3','a) $40; $10   b) Week 5; Week 6   c) $15 (Ali $80, Mei $65)'),('Q4','10, 14, 18, 22, 26.   a) 4 more each day; 90 pages'),('Q5','a) Shop A 60, Shop B 12.  b) No: the scales are different (A starts at 0, lines of 20; B starts at 40, lines of 4).')],
 'Click after a child explains. Q3: Ali goes up $10 a week, Mei $5; the gap of $20 in week 1 closes by $5 each week, so they meet in week 5 ($50) and Ali is ahead from week 6. Week 8: Ali 80, Mei 65. Q4: Day 2 to Day 5 is 3 jumps, 26 − 14 = 12, 12 ÷ 3 = 4; total 10 + 14 + 18 + 22 + 26 = 90. Q5: A goes 20 to 80, B goes 44 to 56. The lines look the same because each graph was stretched to fit its own scale.',gapy=190))

# ---------- stretch / challenge ----------
st=[('1.','Week 1: 48, Week 2: 56, Week 3: 51, Week 4: 66. Between which two weeks was the biggest change?'),('2.','Each line on a scale is worth 5. A point is 7 lines above 0. Another point is 4 lines higher. What do they show?'),('3.','Sales for 4 days add up to 200. Each day is 6 more than the day before. What were the sales on Day 1?')]
put('p4l9-stretch',sec('p4l9-stretch','Early finishers / take-home',h2('Stretch')+numcards(st,36),'Answers: 1) Week 3 to Week 4: up 15 (the other changes are up 8 and down 5). 2) 35 and 55. 3) 41 (41, 47, 53, 59: take away the extras 6 + 12 + 18 = 36, then 164 ÷ 4 = 41).'))
ch=[('1.','Four teams scored 100 points. Team A scored twice as many as Team B. Team C scored 10 more than Team B. Team D scored 22. Find each team’s points.'),('2.','Tank A has 80 litres and loses 6 litres each hour. Tank B has 20 litres and gains 9 litres each hour. After how many hours do they hold the same amount?')]
put('p4l9-challenge',sec('p4l9-challenge','Early finishers / take-home',h2('Challenge')+numcards(ch,36),'Pairs try first, then use the "see it" slide if stuck, then the walk-through. These are Go further Q5 and Q6. Answers: 1) A 34, B 17, C 27, D 22. 2) After 4 hours: 56 litres each.'))
gq=''
for i,(lab,units,extra) in enumerate([('A',2,None),('B',1,None),('C',1,'10'),('D',0,'22')]):
    y=30+i*84; gq+=txt(60,y+46,lab,32,NAVY)
    x=110
    for u in range(units): gq+=f'<rect x="{x}" y="{y}" width="150" height="64" rx="6" fill="{SKY}" stroke="{NAVY}" stroke-width="4"/>'+txt(x+75,y+44,'?',32,RED); x+=150
    if extra: gq+=f'<rect x="{x}" y="{y}" width="{90 if lab=="C" else 130}" height="64" rx="6" fill="{YEL}" stroke="{NAVY}" stroke-width="4"/>'+txt(x+(45 if lab=='C' else 65),y+44,extra,30)
gq+=f'<rect x="60" y="380" width="640" height="70" rx="12" fill="{SOFT}" stroke="{NAVY}" stroke-width="3"/>'+txt(380,426,'All four together: 100 points',30)
gt=''
cols=['Hour','0','1','2','3','4','5']
for r,(lab,first) in enumerate([('Hour',None),('Tank A','80'),('Tank B','20')]):
    for c in range(7):
        x=20+c*104 if c else 20; w=140 if c==0 else 90; x=20 if c==0 else 170+(c-1)*92
        val=(cols[c] if r==0 else (lab if c==0 else (first if c==1 else '')))
        gt+=f'<rect x="{x}" y="{30+r*80}" width="{w}" height="70" fill="{YEL if r==0 else WHITE}" stroke="{NAVY}" stroke-width="3"/>'+(txt(x+w/2,30+r*80+46,val,28) if val else '')
gt+=txt(390,320,'Tank A: 6 litres less each hour',28,RED)+txt(390,370,'Tank B: 9 litres more each hour',28,TEAL)+txt(390,440,'When are they the same?',32,NAVY)
body=h2('Challenge: see it',60)+'<div style="display:flex;gap:32px;align-items:flex-start">'
body+=card(f'<p style="font-size:30px;font-weight:700;color:{TEAL}">Q1: Draw the teams as bars</p>'+svgwrap(760,470,'Bars: team A two units, team B one unit, team C one unit and 10, team D 22; all four make 100',gq).replace('width:760px;height:470px;flex:none','width:100%;height:auto;display:block'),extra='flex:1;min-width:0;padding:20px 24px')
body+=card(f'<p style="font-size:30px;font-weight:700;color:{TEAL}">Q2: Make a table, hour by hour</p>'+svgwrap(760,470,'A table of hours 0 to 5 with tank A starting at 80 litres and tank B at 20 litres, the rest empty',gt).replace('width:760px;height:470px;flex:none','width:100%;height:auto;display:block'),extra='flex:1;min-width:0;padding:20px 24px')+'</div>'
put('p4l9-chdiag',sec('p4l9-chdiag','Early finishers / take-home',body,'Show after pairs have tried the Challenge, or if they are stuck. The pictures show the problem, not the answer. Ask: In Q1, how many equal bars can you see if you take away the 10 and the 22? In Q2, what happens to the GAP between the tanks every hour? Answers are in the Challenge slide notes.'))
body=h2('Challenge: walk-through')+pin(128,250,800,p('Q1: bars, take away the extras',38,800,TEAL))
for i,t in enumerate(['A + B + C = 100 − 22 = 78','Take away C’s extra 10: 68 = 4 equal bars','One bar: 68 ÷ 4 = 17','B 17, A 34, C 27, D 22.  Check: 100 ✓']): body+=pin(128,330+i*110,800,p(t,32),'rise',WHITE)
body+=pin(992,250,800,p('Q2: watch the gap',38,800,TEAL))
for i,t in enumerate(['Hour 0: gap 80 − 20 = 60 litres','Each hour the gap closes by 6 + 9 = 15','60 ÷ 15 = 4 hours','A: 80, 74, 68, 62, 56.  B: 20, 29, 38, 47, 56 ✓']): body+=pin(992,330+i*110,800,p(t,32),'rise',WHITE)
put('p4l9-chwalk',sec('p4l9-chwalk','Early finishers / take-home',body,'Use after pairs have tried. Q1: the bar model turns "twice as many" and "10 more" into equal bars; check 34 + 17 + 27 + 22 = 100. Q2: a table works (keep going hour by hour), but the gap idea is quicker: Tank A goes down and Tank B goes up, so the gap shrinks by both amounts each hour. On a line graph the two lines cross at hour 4, at 56 litres. After that, Tank B has more.'))

# ---------- talk / exit ----------
body=h2('Talk time')+card(chip('TALK TIME',YEL,NAVY)+p('Two graphs show the same numbers, but one line looks much steeper. How can that be? How would you draw a fair graph?',42,600))+card(p('Sentence starters:',34,400,MUTED)+p('“I noticed that …”   “I tested it by …”   “I know because …”',38,600))
put('p4l9-talk',sec('p4l9-talk','80–85 MIN',body,'Minutes 80 to 85. Pairs talk for 2 minutes, then share. Answer: the scales are different. If a scale starts at a big number, or each line is worth very little, a small change looks huge. To compare fairly, use the same scale for both graphs, starting at 0. Second question if time: "Why did we list the changes instead of just looking at the highest point?" (the highest point shows the biggest number, not the biggest change). Praise the reasons, not only the answers.'))
body=h2('Exit ticket')+card(chip('EXIT TICKET')+p('Visitors: Mon 35, Tue 50, Wed 20, Thu 45. Between which two days was the biggest change? Was it an increase or a decrease?',44,600))+card(p('Write your answer on a slip of paper. Show it to your tutor. Then collect your stamp in your inquiry journal.',34,400))
put('p4l9-exit',sec('p4l9-exit','85–88 MIN',body,'Minutes 85 to 88. Answer: Tuesday to Wednesday, a decrease of 30 (the other changes are up 15 and up 25). Watch for children who choose Wednesday to Thursday (the biggest INCREASE, 25). Extension: draw two line graphs of 52, 54, 56, 58, one that makes the change look huge and one that makes it look tiny.'))

# ---------- write ----------
# ---------- fix pass (rebuild/p4_fix.py): sneak-peek puzzles, looking back, neutral names, go further, minute labels ----------
import subprocess as _sp, p4_fix
_G=json.loads(_sp.check_output(['node','-e',"process.stdout.write(JSON.stringify(require('"+os.path.join(H,'..','p4','content','l9.js')+"').gaps))"]))
_ID='p4l9'
_PIC=globals().get('PIC')

order=['p4l9-title','p4l9-warm1','p4l9-warm2','p4l9-explore1','p4l9-explore2','p4l9-teach1','p4l9-we1','p4l9-try1','p4l9-we2','p4l9-try2','p4l9-key','p4l9-break','p4l9-ws1','p4l9-ws1ans','p4l9-teachtwo','p4l9-teachsteps','p4l9-teachscale','p4l9-ws2','p4l9-ws2ans','p4l9-stretch','p4l9-challenge','p4l9-chdiag','p4l9-chwalk','p4l9-talk','p4l9-exit']
p4_fix.finish(S,9,_G,pic=_PIC)
order=p4_fix.order(order,9)
assert set(order)==set(S), set(order)^set(S)
sd=os.path.join(D,'slides')
for f in os.listdir(sd):
    if f.endswith('.html') and f[:-5] not in S: os.remove(os.path.join(sd,f))
for i,h in S.items(): open(os.path.join(sd,i+'.html'),'w').write(h)
deck={'v':4,'createdOnFiles':{'v':1,'at':datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')},'lists':'css',
 'title':'Math Inquirers P4: Lesson 9 – Data Detectives','order':order,'cover':'p4l9-title',
 'sections':{'s1':{'description':'Warm-up and explore','start':'p4l9-title'},'s2':{'description':'Teach: reading line graphs, the biggest change, missing values in tables','start':'p4l9-teach1'},'s3':{'description':'Worksheet with teaching before each page','start':'p4l9-break'},'s4':{'description':'Stretch, challenge, talk and exit','start':'p4l9-stretch'}},
 'faces':{'fredoka':{'family':'Fredoka','href':'https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&display=swap'},'nunito-sans':{'family':'Nunito Sans','href':'https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@400;600;700&display=swap'}},
 'designSystems':[]}
json.dump(deck,open(os.path.join(D,'deck.json'),'w'),indent=1,ensure_ascii=False)
print(len(order),'slides')
