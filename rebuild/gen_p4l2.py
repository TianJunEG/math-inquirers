"""Math Inquirers P4, Lesson 2: Big Number Puzzles. Writes split/p4l2/project (deck.json + slides/*.html)."""
import json,os,sys,datetime
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,H)
import slidekit
from slidekit import *
slidekit.FOOT='Math Inquirers P4 Holiday Program  •  Notice it. Test it. Explain why.'
D=os.path.join(H,'..','split','p4l2','project'); os.makedirs(os.path.join(D,'slides'),exist_ok=True)
S={}
def put(i,h): S[i]=h
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
def tryq(sid,time,title,sub,rows,notes,qw=1250,size=38,top=340,gapy=150):
    body=h2(title)+p(sub,34,600,MUTED)
    for i,(a,b,c) in enumerate(rows):
        body+=qrow(128,top+i*gapy,qw,a,b,size)+answer(128+qw+40,top+i*gapy,1664-qw-40,c)
    return sec(sid,time,body,notes)
def svgwrap(w,h,label,inner):
    return f'<svg aria-label="{E(label)}" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="width:{w}px;height:{h}px;flex:none">{inner}</svg>'
def txt(x,y,s,size=40,fill=NAVY,anchor='middle',weight=700,font='Fredoka, Arial'):
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" fill="{fill}" font-family="{font}">{E(str(s))}</text>'
def line(left,top,width,text,build='rise',size=32,bg=WHITE):
    return pin(left,top,width,p(text,size,700),build,bg,16,'10px 24px')

def fmt(n): return f'{n:,}'.replace(',',' ') if n>=10000 else str(n)
class NL:
    """number line: values vmin..vmax drawn from x0 to x1 at height y"""
    def __init__(s,vmin,vmax,x0=60,x1=1540,y=110): s.vmin,s.vmax,s.x0,s.x1,s.y=vmin,vmax,x0,x1,y
    def X(s,v): return s.x0+(v-s.vmin)*(s.x1-s.x0)/(s.vmax-s.vmin)
    def base(s,minor,labels,hl=()):
        g=f'<line x1="{s.x0-30}" y1="{s.y}" x2="{s.x1+30}" y2="{s.y}" stroke="{NAVY}" stroke-width="5"/>'
        v=s.vmin
        while v<=s.vmax:
            big=v in labels; x=s.X(v)
            g+=f'<line x1="{x}" y1="{s.y-(18 if big else 10)}" x2="{x}" y2="{s.y+(18 if big else 10)}" stroke="{NAVY}" stroke-width="{4 if big else 2}"/>'
            if big: g+=txt(x,s.y+62,fmt(v),30,TEAL if v in hl else NAVY)
            v+=minor
        return g
    def band(s,a,b,col,y0=None,h=36,label=None):
        y0=s.y-h/2 if y0 is None else y0
        g=f'<rect x="{s.X(a)}" y="{y0}" width="{s.X(b)-s.X(a)}" height="{h}" rx="8" fill="{col}" opacity=".55" stroke="{NAVY}" stroke-width="2"/>'
        if label: g+=txt((s.X(a)+s.X(b))/2,y0-12,label,28)
        return g
    def mark(s,v,label,col=RED,anchor='end'):
        x=s.X(v); y=s.y-24
        return f'<polygon points="{x},{y} {x-14},{y-26} {x+14},{y-26}" fill="{col}" stroke="{NAVY}" stroke-width="2"/>'+txt(x-10 if anchor=='end' else x,y-38,label,32,col,anchor)

# ---------- 1. title ----------
put('p4l2-title',title_slide('p4l2-title','LESSON 2  •  WEEK 1','Big Number Puzzles','Numbers to 100 000',
 'Round big numbers on a number line, work backwards from a rounded number, and solve 5-digit riddles and patterns.',
 'Objective: Round numbers to the nearest 10, 100 and 1000 using a number line, work backwards from a rounded number to find the smallest and largest possible numbers, use rounding to estimate and check, and solve 5-digit number riddles, digit-card puzzles and number patterns. '
 'Thinking strategies taught today: DRAW A NUMBER LINE, WORK BACKWARDS, MAKE A LIST IN ORDER and USE THE CLUES ONE AT A TIME. '
 'Materials: Digit cards 0 to 9 (one set per child), mini whiteboards, a place-value chart (ten thousands to ones), a blank number line strip. '
 'Online: children cut out paper digit cards before the lesson and move them on camera; the tutor marks the number lines on the slides. '
 'Time plan: Warm-up check 1 to 4 (two questions on the key idea; children who get both right and can say why start on the Think Harder pages at minute 34), warm-up game 4 to 6 (one short round), quick questions 6 to 8, explore 8 to 18, teaching 18 to 30 (click to reveal each step and answer; the "your turn" slides are optional, skip them if short of time), brain break 30 to 34, worksheet page 1 from 34 to 50 and check together 50 to 53, short teaching before page 2 from 53 to 58, worksheet page 2 from 58 to 76 and check together 76 to 80, talk time 80 to 85, exit ticket 85 to 88, What was hard? reflection 88 to 90. The Challenge slides and the Think Harder pages are for early finishers and for take-home: they have no fixed time slot. Online: page 1 is pair work, so allow about 2 minutes to move into and out of breakout rooms (or run page 1 as a whole-group screen-share if there are only 8 children).'))

# ---------- 2. warm-up: Place It Right (5 digits) ----------
def dcards(digits,x0=0,y=6,w=96,h=124,gap=26,fill=YEL):
    g=''
    for i,d in enumerate(digits):
        x=x0+i*(w+gap)
        g+=f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="16" fill="{fill}" stroke="{NAVY}" stroke-width="5"/>'+txt(x+w/2,y+h/2+24,d,70)
    return g
g=''
for i,lab in enumerate(['TTh','Th','H','T','O']):
    x=30+i*170
    g+=f'<rect x="{x}" y="60" width="150" height="150" rx="14" fill="{WHITE}" stroke="{NAVY}" stroke-width="5" stroke-dasharray="14 8"/>'+txt(x+75,44,lab,32,TEAL)
g+=dcards([4],930,70,110,140)+txt(1110,160,'?',90,TEAL)
for i in range(3): g+=f'<rect x="{1190+i*120}" y="80" width="96" height="120" rx="14" fill="{SKY}" stroke="{NAVY}" stroke-width="4"/>'
g+=txt(1370,250,'cards still to come …',30,MUTED,weight=600,font='Nunito Sans, Arial')
body=h2('Warm-up: Place It Right')+card(p('I turn over one digit card at a time. Write it in a box straight away. No moving it later! Round 1: biggest wins. Round 2: closest to 50 000 wins.',36,700))
body+=pin(128,400,1664,svgwrap(1600,270,'Five empty place-value boxes TTh, Th, H, T, O and a digit card 4 waiting to be placed',g),None,WHITE,24,'12px 32px')
body+=pin(128,740,1664,p('Round 2: where does a 4 go? A 5? Is 49 999 or 50 100 closer to 50 000?',36,700),'fade',SOFT,20,'20px 30px')
put('p4l2-warm1',sec('p4l2-warm1','4–6 MIN',body,
 'Minutes 4 to 6 (one short round, about 2 minutes: the Warm-up check came first). Place It Right with 5 digits. Children draw five boxes: TTh, Th, H, T, O. Shuffle digit cards 0 to 9 and turn over one at a time (online: hold it up to the camera). After EACH card, children write it in one empty box at once and cannot move it. After five cards, read the numbers aloud: biggest wins. '
 'Round 2: closest to 50 000 wins. Click to show the thinking question. Talk: "A 4 or a 5 in the ten thousands place. If you have a 4, you want the other digits BIG (49 9..). If you have a 5, you want them small (50 1..)." 49 999 is 1 away and 50 100 is 100 away. '
 'Listen for children who compare the distances; that is rounding thinking, and it comes straight back in the explore.'))

# ---------- 3. quick questions ----------
qs=[('1.','What is the 7 worth in 47 352?','7000'),('2.','Sixty thousand and forty-five in numerals?','60 045'),('3.','1000 more than 59 600?','60 600'),('4.','40 000 + 3000 + 50 + 8 = ?','43 058'),('5.','36 815 to the nearest 1000?','37 000')]
body=h2('Quick questions')+''.join(qrow(128,250+i*125,1250,a,b) for i,(a,b,c) in enumerate(qs))+''.join(answer(1420,250+i*125,372,c) for i,(a,b,c) in enumerate(qs))
put('p4l2-warm2',sec('p4l2-warm2','6–8 MIN',body,'Minutes 6 to 8. Read each aloud, whiteboards up together, then click. After 2: watch for 6045 or 600 045; say it as "60 thousand, 0 hundreds, 4 tens, 5 ones". After 3: the thousands digit was 9, so the ten thousands digit changes too. After 4: the 0 holds the hundreds place. After 5: 36 815 is between 36 000 and 37 000; ask "Is it nearer 36 000 or 37 000?" Do not teach the halfway rule yet. Answers: 7000, 60 045, 60 600, 43 058, 37 000.'))

# ---------- 4. explore: what to do ----------
nl=NL(49000,51000,700,1500,150)
g=dcards([2,4,5,7,9],20,10,90,116,20)+nl.base(250,(49000,49500,50000,50500,51000),(50000,))+txt(1130,40,'Which numbers round to 50 000?',30,TEAL,font='Nunito Sans, Arial')
steps=''.join(f'<li>{E(s)}</li>' for s in ['Take the digit cards 2, 4, 5, 7 and 9.','Make a 5-digit number using each card once. Write it down.','Round it to the nearest thousand. Does it round to 50 000?','Find ALL the numbers that round to 50 000. Which is closest to 50 000?'])
body=h2('Explore: what to do')+card(chip('EXPLORE')+f'<ol style="font-size:34px;font-weight:600;padding-left:52px;display:flex;flex-direction:column;gap:6px">{steps}</ol>')
body+=card(svgwrap(1600,240,'Digit cards 2, 4, 5, 7 and 9 next to a number line from 49 000 to 51 000',g),extra='padding:16px 32px')
put('p4l2-explore1',sec('p4l2-explore1','8–13 MIN',body,'Minutes 8 to 13. Pairs work with digit cards 2, 4, 5, 7 and 9 (online: paper cards on camera). Ask for a prediction first: how many numbers will round to 50 000? Let them try numbers freely at first. Common first try: 52 479 (rounds to 52 000) or 54 279 (54 000). Push them towards numbers starting with 4 9. Early finishers: which number you can make is closest to 70 000? (72 459, which is 2459 away: there is no 6 card, so nothing can start 69.)'))

# ---------- 5. explore: talk ----------
body=h2('Explore: talk about it')+numcards([('1.','Which of your numbers round to 50 000 to the nearest thousand?'),('2.','How do you know you have found them all?'),('3.','Which one is closest to 50 000? How far away is it?')],40)
put('p4l2-explore2',sec('p4l2-explore2','13–18 MIN',body,'Minutes 13 to 18. Let pairs keep working, then gather. Collect numbers on the board and test each one together. Answers: 1) 49 527, 49 572, 49 725, 49 752. 2) A number that rounds to 50 000 must be from 49 500 to 50 499. With no 0 card, nothing starts 50, so it must start 49, and the hundreds digit must be 5 or 7 (2 and 4 are too small). Each of those gives 2 numbers. 3) 49 752, only 248 away. The next slides teach the halfway mark properly.'))

# ---------- 6. worked example: rounding on a number line ----------
nl=NL(36000,37000,80,1540,120)
base=nl.base(100,(36000,36500,37000))
half=f'<line x1="{nl.X(36500)}" y1="40" x2="{nl.X(36500)}" y2="170" stroke="{TEAL}" stroke-width="5" stroke-dasharray="12 8"/>'+txt(nl.X(36500)+120,58,'halfway',30,TEAL)
mk=nl.mark(36482,'36 482')
WN,HN=1620,210
body=h2('Worked example: round 36 482 to the nearest 1000')
body+=pin(128,240,WN,svgwrap(WN,HN,'Number line from 36 000 to 37 000',base),None,WHITE,24,'10px 20px')
body+=pin(128,240,WN,svgwrap(WN,HN,'Halfway mark at 36 500',half),'fade',None,0,'10px 20px')
body+=pin(128,240,WN,svgwrap(WN,HN,'36 482 marked just before halfway',mk),'pop',None,0,'10px 20px')
body+=step(1,'It is between 36 000 and 37 000.',top=510,size=34)
body+=step(2,'Halfway is 36 500. 36 482 is just BEFORE halfway.',top=610,size=34)
body+=step(3,'So it is nearer 36 000.   To the nearest 100: between 36 400 and 36 500; 82 is past 50, so 36 500.',top=710,size=32)
body+=answer(128,830,1664,'36 482 ≈ 36 000 (nearest 1000)     36 482 ≈ 36 500 (nearest 100)')
put('p4l2-we1',sec('p4l2-we1','18–20 MIN',body,'Teach. Clicks: halfway line, the number, then the steps. Think-aloud: "Which two thousands is 36 482 between? 36 000 and 37 000. The halfway mark is 36 500. My number is 18 short of halfway, so it is nearer 36 000." Then the shortcut: "Look only at the digit just to the right of the place I round to: for thousands, the hundreds digit. 4 is less than 5, so round down." Ask: "What about exactly 36 500?" (halfway rounds UP: 37 000). The sign ≈ on the last line means "is about"; say so if children have not met it.'))
put('p4l2-try1',tryq('p4l2-try1','20–21 MIN • OPTIONAL','Your turn: round it','Find the two round numbers and the halfway mark first.',[('a','58 361 to the nearest hundred','58 400'),('b','58 361 to the nearest thousand','58 000'),('c','29 960 to the nearest hundred','30 000')],
 'Whiteboards. a) Between 58 300 and 58 400; halfway 58 350; 58 361 is past it. b) Between 58 000 and 59 000; halfway 58 500; 58 361 is before it. c) Between 29 900 and 30 000; halfway 29 950; 29 960 is past it, so 30 000. Watch for 29 000 or 291 00: the 9 hundreds becomes 10 hundreds, which is another thousand.'))

# ---------- 8. worked example: work backwards ----------
nl=NL(24000,26000,80,1540,130)
base=nl.base(250,(24000,24500,25000,25500,26000),(25000,))
bd=nl.band(24500,25499,YEL,h=40,label='all round to 25 000')
WN,HN=1620,220
body=h2('Work backwards: what rounds to 25 000?')+card(p('Rounded to the nearest thousand, a number is 25 000. What are the smallest and largest whole numbers it can be?',36,700))
body+=pin(128,400,WN,svgwrap(WN,HN,'Number line from 24 000 to 26 000',base),None,WHITE,24,'10px 20px')
body+=pin(128,400,WN,svgwrap(WN,HN,'Band from 24 500 to 25 499 shaded',bd),'fade',None,0,'10px 20px')
body+=step(1,'Halfway marks: 24 500 and 25 500. Halfway rounds UP.',top=670,size=34)
body+=step(2,'Smallest: 24 500.   Largest: 25 499 (25 500 would round to 26 000).',top=770,size=34)
put('p4l2-we2',sec('p4l2-we2','21–23 MIN',body,'Work backwards from the rounded number. Ask first: "Could the number be 25 600? 24 400? 25 500?" Let children argue, then click the band. Think-aloud: "Everything from the halfway mark below, 24 500, up to just before the halfway mark above rounds to 25 000. 25 500 itself is halfway, and halfway rounds up, to 26 000. So the largest whole number is 25 499." Common mistake: saying 25 500 is the largest.'))
put('p4l2-try2',tryq('p4l2-try2','23–25 MIN • OPTIONAL','Your turn: work backwards','Draw a number line. Mark the two halfway marks.',[('a','Smallest whole number that rounds to 7000 (nearest 1000)?','6500'),('b','Largest whole number that rounds to 40 000 (nearest 1000)?','40 499'),('c','How many whole numbers round to 800 (nearest 10)?','10')],
 'Whiteboards. a) Halfway below 7000 is 6500. b) Halfway above 40 000 is 40 500, so 40 499. c) 795, 796, … 804: count them, 10 numbers. Many children say 9 or 11: list them to check.',qw=1300,size=34))

# ---------- 10. two clues together ----------
nl=NL(4140,4260,80,1540,120)
base=nl.base(10,(4150,4200,4250),())
b1=nl.band(4245,4254.9,SKY,y0=200,h=34)+txt(nl.X(4250),268,'nearest 10 → 4250',28,NAVY)
b2=nl.band(4150,4249.9,YEL,y0=36,h=34)+txt(nl.X(4200),26,'nearest 100 → 4200',28,NAVY)
WN,HN=1620,280
body=h2('Two clues: where do they overlap?')+card(p('A whole number rounds to 4250 to the nearest 10, AND to 4200 to the nearest 100. Find all the numbers.',36,700))
body+=pin(128,390,WN,svgwrap(WN,HN,'Number line from 4140 to 4260',base),None,WHITE,24,'10px 20px')
body+=pin(128,390,WN,svgwrap(WN,HN,'Yellow band 4150 to 4249 for the nearest 100',b2),'fade',None,0,'10px 20px')
body+=pin(128,390,WN,svgwrap(WN,HN,'Blue band 4245 to 4254 for the nearest 10',b1),'fade',None,0,'10px 20px')
body+=step(1,'Nearest 100 is 4200: from 4150 to 4249.   Nearest 10 is 4250: from 4245 to 4254.',top=710,size=32)
body+=answer(128,815,1664,'In both: 4245, 4246, 4247, 4248, 4249  (5 numbers)')
put('p4l2-we4',sec('p4l2-we4','25–27 MIN',body,'Teach before worksheet page 1 (two rounding clues together: an optional stretch example, not on the worksheet any more). Click the yellow band (clue 2), then the blue band (clue 1). Ask: "Which numbers are in BOTH bands?" Check one at the edge: 4250 rounds to 4250 to the nearest 10, but to 4300 to the nearest 100, so it is out. 4244 rounds to 4240, so it is out too.'))

# ---------- 11. estimate with a bar model ----------
g=''
for i in range(7):
    x=10+i*220
    g+=f'<rect x="{x}" y="40" width="220" height="90" fill="{SKY}" stroke="{NAVY}" stroke-width="4"/>'+txt(x+110,98,'3089',34)
g+=f'<path d="M10 150 Q10 175 40 175 L760 175 Q785 175 785 200 Q785 175 810 175 L1520 175 Q1550 175 1550 150" fill="none" stroke="{NAVY}" stroke-width="4"/>'+txt(785,240,'7 × 3089 = ?',34,TEAL)
body=h2('Estimate first, then check')+card(p('7 boxes each hold 3089 beads. About how many beads is that?',36,700))
body+=pin(128,340,1600,svgwrap(1560,250,'Bar model: 7 equal parts of 3089',g),None)
body+=step(1,'Round 3089 to the nearest thousand: 3000.',top=610,size=34)
body+=step(2,'Estimate: 7 × 3000 = 21 000.',top=705,size=34)
body+=step(3,'We rounded DOWN, so the exact answer is a bit MORE.  7 × 3089 = 21 623 ✓',top=800,size=34)
put('p4l2-we3',sec('p4l2-we3','27–29 MIN',body,'Teach before worksheet page 1 (Q3 estimates and checks). Draw the bar: 7 equal parts. Think-aloud: "3089 is close to 3000. 7 × 3 thousands = 21 thousands. I rounded each part down by 89, so my estimate is too small, and the real answer is more." Work out 7 × 3089 together in columns if time (21 623). Ask: "If the number were 2950, would the exact answer be more or less than 21 000?" (less: 2950 was rounded up).'))

# ---------- 12. key ----------
body=h2('Key idea: find the halfway mark')+card(p('To round, find the two round numbers and the halfway mark. Halfway or more rounds up.',44,700))+card(p('Working backwards: the smallest number IS the halfway mark below. The largest is 1 less than the halfway mark above.',38,600,MUTED))
put('p4l2-key',sec('p4l2-key','29–30 MIN',body,'Say the key idea together. Common mistakes to watch for during the worksheet: (1) Forgetting to carry when the digit to change is a 9 (63 950 to the nearest hundred written as 63 900 instead of 64 000). (2) Working backwards with the wrong limits: saying the largest number that rounds to 63 000 is 63 500 instead of 63 499. (3) Digit-card puzzles: putting 0 in the ten thousands place, or making the biggest number first and hoping it is even, instead of choosing the ones digit first.'))
put('p4l2-break',break_slide('p4l2-break','30–34 MIN','Human number line. Five children are 10 000, 20 000, 30 000, 40 000 and 50 000. I call a number: everyone points to the nearest ten thousand.','Four minutes. Call numbers such as 34 999, 25 000, 47 210, 15 500, 44 999. Online: children hold up 1 to 5 fingers for the ten thousand they point to. Ask after 25 000: "It is exactly halfway. Which way?" (up, to 30 000).'))

# ---------- worksheet page 1 ----------
put('p4l2-ws1',ws_preview('p4l2-ws1','34–50 MIN','Worksheet page 1: with your partner',[('Q1','Round to the nearest 10, 100 and 1000. Watch out for 9s!'),('Q2','Work backwards: smallest and largest, then every number that rounds to 5350.'),('Q3','Estimate the buns, decide more or less, then check.')],'Stuck? Draw a number line and mark the halfway point.','Minutes 34 to 50. Walk around. Ask "Which two round numbers is it between? Where is halfway?" before giving any help. Q1: 63 950 to the nearest 100 and 9049 to the nearest 10 are the traps. Q2b: write 5340, 5341, 5342 … and check each one on the number line.'))
put('p4l2-ws1ans',checks('p4l2-ws1ans','50–53 MIN','Page 1: check together',[('Q1','47 290, 47 300, 47 000 / 63 950, 64 000, 64 000. Try next: 9049 gives 9050, 9000, 9000; 80 503 gives 80 500, 80 500, 81 000'),('Q2','a) Smallest 62 500, largest 63 499   b) 5345 to 5354 (10 numbers)'),('Q3','a) 6 × 5000 = 30 000   b) Less: 4982 was rounded up   c) 29 892')],
 'Click each answer after a pair explains theirs. Q1: 63 950 is halfway between 63 900 and 64 000, and halfway rounds up. 80 503 to the nearest 1000: 503 is past 500, so 81 000. Q2b: halfway is 5345, so 5345 rounds up to 5350; 5354 rounds to 5350 but 5355 rounds up to 5360. That is 10 numbers. (Two clues together, 5350 to 5354, is a Think harder question in the question bank.) Q3c: 6 × 4982 = 29 892, only 108 less than the estimate.',gapy=180,size=32))

# ---------- teach: riddle with a rounding clue ----------
body=h2('Number riddles: strongest clue first')+card(p('I am a 5-digit number. Rounded to the nearest thousand, I am 20 000. My digits add up to 5. My ones digit is 3.',38,700))
body+=step(1,'Rounding clue: I am from 19 500 to 20 499.',top=420,size=34)
body+=step(2,'Starting 19: 1 + 9 = 10, already more than 5. So I start 20 …',top=520,size=34)
body+=step(3,'2 + 0 + ? + ? + 3 = 5, so the hundreds and tens are 0.',top=620,size=34)
body+=answer(128,730,1664,'I am 20 003.   Check every clue ✓')
put('p4l2-teachriddle',sec('p4l2-teachriddle','53–55 MIN',body,'Teach before worksheet page 2 (Q4a starts with a rounding clue). Use the clues one at a time: the rounding clue turns a huge list into a short range. Ask after step 1: "Which numbers between 19 500 and 20 499 could have digits that add to only 5?" Check at the end: 20 003 rounds to 20 000; 2 + 0 + 0 + 0 + 3 = 5; ones digit 3. For Q4b ("find ALL"), remind them: list in order, starting with the smallest ten thousands digit.'))

# ---------- teach: patterns ----------
rows=[('Up by the same amount:','34 800, 36 000, 37 200, ___, ___','38 400, 39 600'),('Down by the same amount:','62 000, 60 750, 59 500, ___','58 250'),('First number above 50 000?','41 000, 43 500, 46 000 …','51 000')]
body=h2('Big number patterns')+p('Find the rule from TWO gaps. Then use it.',34,600,MUTED)
for i,(a,b,c) in enumerate(rows):
    body+=qrow(128,330+i*150,1250,a,b,34)+answer(1420,330+i*150,372,c)
body+=pin(128,790,1664,p('Check the rule on every gap. Going down? Take away.',34,700),'fade',SOFT,20,'18px 30px')
put('p4l2-teachpattern',sec('p4l2-teachpattern','55–56 MIN',body,'Teach before worksheet page 2 (Q5). Row 1: 36 000 − 34 800 = 1200, 37 200 − 36 000 = 1200: add 1200. Row 2: take away 1250. Row 3: add 2500: 48 500 is not above 50 000 yet, the next one, 51 000, is. Ask: "Is 50 000 in this pattern?" (no). Watch for children who cross a ten thousand wrongly: 37 200 + 1200 = 38 400.'))

# ---------- teach: digit cards ----------
g=dcards([0,2,4,7,9],10,10,96,124,26)
body=h2('Digit cards: choose the ones digit first')+pin(128,240,640,svgwrap(620,150,'Digit cards 0, 2, 4, 7 and 9',g),None)
body+=pin(820,250,972,p('Use 0, 2, 4, 7 and 9 once each.',38,700),None,WHITE,20,'26px 32px')
body+=step(1,'Largest ODD: the ones digit must be 7 or 9. Keep 9 in front, 7 last: 94 207.',top=430,size=32)
body+=step(2,'Smallest EVEN: 0 cannot go first, so 2 then 0. The only even card left is 4: 20 794.',top=550,size=32)
body+=step(3,'Closest to 50 000: 49 720 (280 away) beats 70 249 (20 249 away).',top=670,size=32)
put('p4l2-teachcards',sec('p4l2-teachcards','56–58 MIN',body,'Teach before worksheet page 2 (Q6). Think-aloud for step 1: "Odd means the ones digit is odd. I decide that FIRST, then put the biggest of the rest in front." Step 2: "Smallest: the smallest digit that is not 0 goes first, then 0. The ones digit must be even, and the only even card left is 4." Step 3: compare the best number on each side of 50 000. Ask: "Why not 4 … something?" (we need a 9 in the thousands to get close: 49 720).'))

# ---------- worksheet page 2 ----------
put('p4l2-ws2',ws_preview('p4l2-ws2','58–76 MIN','Worksheet page 2: on your own',[('Q4','Number riddles. Strongest clue first. Then find ALL the numbers.'),('Q5','Patterns. Find the rule from two gaps.'),('Q6','Digit cards 0, 3, 5, 6, 8. Choose the ones digit first.')],'Finished early? Stretch and Challenge come next.','Children work alone. Note who needs a short catch-up next lesson, especially anyone who still rounds 63 950 to 63 900.'))
put('p4l2-ws2ans',checks('p4l2-ws2ans','76–80 MIN','Page 2: check together',[('Q4','a) 47 621   b) 10 001, 10 010, 10 100, 11 000, 20 000: 5 numbers'),('Q5','a) 26 450, 27 450   b) 76 800, 75 300   c) 99 990, 100 000   d) 32 500'),('Q6','a) 86 530   b) 30 685   c) 60 358')],
 'Click after a child explains. Q4a: 47 500 to 48 499 with hundreds digit 6 means 47 6..; ones digit 1 and tens digit double that (2) gives 47 621. Q4b: ten thousands digit 1 leaves 1 more in 4 places (4 numbers), ten thousands digit 2 leaves 0 (20 000). Q5c: 99 990 + 10 = 100 000. Q6b: odd means 3 or 5 last; smallest is 3 first and 5 last: 30 685. Q6c: 58 630 is 1370 away; 60 358 is 358 away.',gapy=180,size=32))

# ---------- stretch / challenge ----------
from p4bank import th_items, th_notes, gf_numbers  # slide Think harder = the printed page (docs/audit/reaudit_fixes_p4.md)
st=th_items(2)
def numgrid(items,size=30): return '<div style="display:grid;grid-template-columns:1fr 1fr;gap:24px;align-items:stretch">'+''.join(card(p(f'<span style="color:{TEAL}">{a}</span>  {E(b)}',size,600,raw=True),extra='padding:24px 32px') for a,b in items)+'</div>'
put('p4l2-stretch',sec('p4l2-stretch','Early finishers / take-home',h2('Think harder')+numgrid(st,34),th_notes(2)))
ch=[('1.','How many 5-digit numbers have digits that add up to 3?'),('2.','The distance counter on Mr Tan\'s car shows 39 993 km. It reads the same forwards and backwards. What is the next number like this the counter will show? How many more kilometres is that?')]
put('p4l2-challenge',sec('p4l2-challenge','Early finishers / take-home',h2('Go further')+numcards(ch,36),'Pairs try first, then use the "see it" slide if stuck, then the walk-through. These are Go further Q5 and Q7. Answers: 1) 15 (10 starting with 1, 4 starting with 2, and 30 000). 2) 40 004, which is 11 km more.'))
g1=''
for i,lab in enumerate(['TTh','Th','H','T','O']):
    x=40+i*145
    g1+=f'<rect x="{x}" y="70" width="125" height="125" rx="14" fill="{WHITE}" stroke="{NAVY}" stroke-width="4" stroke-dasharray="12 7"/>'+txt(x+62,52,lab,28,TEAL)
g1+=txt(390,250,'digits add up to 3',32,NAVY)+txt(390,300,'Example: 10 011',30,MUTED,weight=600,font='Nunito Sans, Arial')
g1+=f'<rect x="60" y="340" width="660" height="110" rx="14" fill="{SOFT}" stroke="{NAVY}" stroke-width="3"/>'+txt(390,385,'TTh digit 1?  2?  3?',30)+txt(390,428,'How many for each?',28,TEAL,font='Nunito Sans, Arial')
g2=f'<rect x="60" y="40" width="660" height="150" rx="20" fill="{NAVY}"/>'
for i,d in enumerate('39993'): g2+=f'<rect x="{90+i*124}" y="60" width="104" height="110" rx="10" fill="{WHITE}"/>'+txt(142+i*124,140,d,72)
g2+=txt(390,240,'km',30,MUTED,font='Nunito Sans, Arial')
g2+=f'<rect x="60" y="300" width="660" height="140" rx="16" fill="{SOFT}" stroke="{NAVY}" stroke-width="3"/>'+txt(390,355,'Next palindrome:  ? ? ? ? ?',34)+txt(390,410,'It must be bigger than 39 993.',28,TEAL,font='Nunito Sans, Arial')
body=h2('Go further: see it',60)+'<div style="display:flex;gap:32px;align-items:flex-start">'
body+=card(f'<p style="font-size:30px;font-weight:700;color:{TEAL}">Q1: Five places, digits add up to 3</p>'+svgwrap(780,470,'Five empty place-value boxes; the digits must add up to 3',g1).replace('width:780px;height:470px;flex:none','width:100%;height:auto;display:block'),extra='flex:1;min-width:0;padding:20px 24px')
body+=card(f'<p style="font-size:30px;font-weight:700;color:{TEAL}">Q2: The distance counter</p>'+svgwrap(780,470,'A distance counter showing 39 993 km',g2).replace('width:780px;height:470px;flex:none','width:100%;height:auto;display:block'),extra='flex:1;min-width:0;padding:20px 24px')+'</div>'
put('p4l2-chdiag',sec('p4l2-chdiag','Early finishers / take-home',body,'Show after pairs have tried the Challenge, or if they are stuck. The pictures show the problem, not the answer. Ask: For Q1, what can the ten thousands digit be? For each choice, how much is left to share among the other four places? For Q2, if the number starts with 39, how must it end? Is there a palindrome 39 _ 93 bigger than 39 993? Answers are in the Challenge slide notes.'))
body=h2('Go further: walk-through')+pin(128,250,800,p('Q1: list by the first digit',38,800,TEAL))
for i,t in enumerate(['Starts 1: share 2 in 4 places. A 2: 4 ways. Two 1s: 6 ways → 10','Starts 2: one 1 in 4 places → 4','Starts 3: 30 000 → 1','10 + 4 + 1 = 15']): body+=pin(128,330+i*120,800,p(t,30),'rise',WHITE)
body+=pin(992,250,800,p('Q2: change the first digit',38,800,TEAL))
for i,t in enumerate(['39 ? 93: the middle digit can only go up to 9. 39 993 is the last one.','So the next one starts and ends with 4: 4 _ _ _ 4','Smallest: 40 004','40 004 − 39 993 = 11 km']): body+=pin(992,330+i*120,800,p(t,30),'rise',WHITE)
put('p4l2-chwalk',sec('p4l2-chwalk','Early finishers / take-home',body,'Use after pairs have tried. Q1: list in order by the first digit so nothing is missed. The 6 ways for two 1s (in two of the four places Th, H, T, O): 11 100, 11 010, 11 001, 10 110, 10 101, 10 011. The 4 ways for a 2: 12 000, 10 200, 10 020, 10 002. Q2: count on from 39 993 to 40 000 (7) and on to 40 004 (4): 11 km.'))

# ---------- talk / exit ----------
body=h2('Talk time')+card(chip('TALK TIME',YEL,NAVY)+p('Siti says 49 999 rounds to 50 000 to the nearest 10, 100 AND 1000. Ravi says 45 000 rounds to 40 000 to the nearest ten thousand. Who is right?',40,600))+card(p('Sentence starters:',34,400,MUTED)+p('“I noticed that …”   “I tested it by …”   “I know because …”',38,600))
put('p4l2-talk',sec('p4l2-talk','80–85 MIN',body,'Minutes 80 to 85. Pairs talk for 2 minutes, then share. Answer: Siti is right: 49 999 is only 1 away from 50 000, so it rounds to 50 000 each time (49 999 → 50 000 to the nearest 10 because 9 ones round up). Ravi is wrong: 45 000 is exactly halfway between 40 000 and 50 000, and halfway rounds up, to 50 000. Praise the reasons, not only the answers.'))
body=h2('Exit ticket')+card(chip('EXIT TICKET')+p('Round 74 652 to the nearest thousand. Then write the smallest whole number that rounds to 74 000 to the nearest thousand.',46,600))+card(p('Write your answer on a slip of paper. Show it to your tutor. Then collect your stamp in your inquiry journal.',34,400))
put('p4l2-exit',sec('p4l2-exit','85–88 MIN',body,'Minutes 85 to 88. Answer: 75 000 (652 is past halfway). The smallest whole number that rounds to 74 000 is 73 500. Extension: how many whole numbers round to 45 000 to the nearest thousand AND to 50 000 to the nearest ten thousand? (500: from 45 000 to 45 499.)'))

# ---------- write ----------
# ---------- fix pass (rebuild/p4_fix.py): sneak-peek puzzles, looking back, neutral names, go further, minute labels ----------
import subprocess as _sp, p4_fix
_G=json.loads(_sp.check_output(['node','-e',"process.stdout.write(JSON.stringify(require('"+os.path.join(H,'..','p4','content','l2.js')+"').gaps))"]))
_ID='p4l2'
_PIC=globals().get('PIC')

order=['p4l2-title','p4l2-warm1','p4l2-warm2','p4l2-explore1','p4l2-explore2','p4l2-we1','p4l2-try1','p4l2-we2','p4l2-try2','p4l2-we4','p4l2-we3','p4l2-key','p4l2-break','p4l2-ws1','p4l2-ws1ans','p4l2-teachriddle','p4l2-teachpattern','p4l2-teachcards','p4l2-ws2','p4l2-ws2ans','p4l2-stretch','p4l2-challenge','p4l2-chdiag','p4l2-chwalk','p4l2-talk','p4l2-exit']
p4_fix.finish(S,2,_G,pic=_PIC)
order=p4_fix.order(order,2)
assert set(order)==set(S), set(order)^set(S)
sd=os.path.join(D,'slides')
for f in os.listdir(sd):
    if f.endswith('.html') and f[:-5] not in S: os.remove(os.path.join(sd,f))
for i,h in S.items(): open(os.path.join(sd,i+'.html'),'w').write(h)
deck={'v':4,'createdOnFiles':{'v':1,'at':datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')},'lists':'css',
 'title':'Math Inquirers P4: Lesson 2 – Big Number Puzzles','order':order,'cover':'p4l2-title',
 'sections':{'s1':{'description':'Warm-up and explore','start':'p4l2-title'},'s2':{'description':'Teach: rounding, working backwards and estimating','start':'p4l2-we1'},'s3':{'description':'Worksheet with teaching before each page','start':'p4l2-break'},'s4':{'description':'Stretch, challenge, talk and exit','start':'p4l2-stretch'}},
 'faces':{'fredoka':{'family':'Fredoka','href':'https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&display=swap'},'nunito-sans':{'family':'Nunito Sans','href':'https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@400;600;700&display=swap'}},
 'designSystems':[]}
json.dump(deck,open(os.path.join(D,'deck.json'),'w'),indent=1,ensure_ascii=False)
print(len(order),'slides')
