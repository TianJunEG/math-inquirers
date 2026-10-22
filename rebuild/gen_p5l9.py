"""Math Inquirers P5, Lesson 9: Pattern Generalisers (patterns and number sense). Writes split/p5l9/project (deck.json + slides/*.html).
Growing patterns are drawn from the rule stated on the slide; every answer was checked with a script."""
import json,os,sys,datetime
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,H)
import slidekit
from slidekit import *
slidekit.FOOT='Math Inquirers P5 Holiday Program  •  Notice it. Test it. Explain why.'
FOOTX=slidekit.FOOT
S={}
def put(i,h): S[i]=h
RED='#D64545'; GREYT='#9AA5BD'

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
def txt(x,y,s,size=40,fill=NAVY,anchor='middle',weight=700,font='Fredoka, Arial'):
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" fill="{fill}" font-family="{font}">{E(str(s))}</text>'
def stick(x1,y1,x2,y2,col=NAVY,w=9):
    return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{col}" stroke-width="{w}" stroke-linecap="round"/>'
def sq_fig(n,ox,oy,u=70):
    """n squares in a row; first square navy, the 3 NEW sticks of each later square teal"""
    g=''
    for i in range(n):
        x=ox+i*u; c=NAVY if i==0 else TEAL
        g+=stick(x,oy,x+u,oy,c)+stick(x,oy+u,x+u,oy+u,c)+stick(x+u,oy,x+u,oy+u,c)
        if i==0: g+=stick(x,oy,x,oy+u,c)
    return g
def tiles_fig(n,ox,oy,s=44):
    """n yellow tiles in a row with a grey border: (n+2) wide, 3 tall"""
    g=''
    for r in range(3):
        for c in range(n+2):
            edge=r in (0,2) or c in (0,n+1)
            g+=f'<rect x="{ox+c*s}" y="{oy+r*s}" width="{s}" height="{s}" fill="{GREYT if edge else YEL}" stroke="{NAVY}" stroke-width="3"/>'
    return g
def tag_box(x,y,w,h,label,fill=WHITE,size=34,col=NAVY):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="{fill}" stroke="{NAVY}" stroke-width="4"/>'+txt(x+w/2,y+h/2+size*0.35,label,size,col)

def write_deck(num,title,order,sections,D):
    os.makedirs(os.path.join(D,'slides'),exist_ok=True)
    assert set(order)-{'end'}==set(S), set(order)^set(S)
    sd=os.path.join(D,'slides')
    for f in os.listdir(sd):
        if f.endswith('.html') and f[:-5] not in S: os.remove(os.path.join(sd,f))
    for i,h in S.items(): open(os.path.join(sd,i+'.html'),'w').write(h)
    deck={'v':4,'createdOnFiles':{'v':1,'at':datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')},'lists':'css',
     'title':title,'order':order,'cover':order[0],'sections':sections,
     'faces':{'fredoka':{'family':'Fredoka','href':'https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&display=swap'},'nunito-sans':{'family':'Nunito Sans','href':'https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@400;600;700&display=swap'}},
     'designSystems':[]}
    json.dump(deck,open(os.path.join(D,'deck.json'),'w'),indent=1,ensure_ascii=False)
    print(len(order),'slides')
D=os.path.join(H,'..','split','p5l9','project')
P='p5l9-'

# 1 title
put(P+'title',title_slide(P+'title','LESSON 9  •  WEEK 5A','Pattern Generalisers','Patterns and number sense',
 'See how a pattern grows, say the rule for any figure in words, work backwards from a total, and solve problems by supposing.',
 'Objective: Continue growing patterns drawn as figures, say the rule for any figure in words (for example, sticks = 3 × figure number + 1) and explain it from the picture, work backwards from a total to find the figure, and solve "two kinds of things" problems with a guess-and-check table and with supposition. '
 'Thinking strategies today: LOOK FOR A PATTERN, MAKE A TABLE, WORK BACKWARDS, GUESS AND CHECK, SUPPOSITION. '
 'Materials: matchsticks or toothpicks (about 40), square paper tiles or the square grid from the cut-out pages, mini whiteboards, workbook. '
 'Online: children have toothpicks and paper squares ready on the desk and build each figure on camera; pairs go to breakout rooms for the explore and page 1 and hold their tables up to the camera. '
 'Time plan: sneak-peek puzzles 0 to 3 (private answers, nobody is marked), warm-up 3 to 9, explore 9 to 21 (a Go further what-if is on the explore slide for anyone who wants more), teaching 21 to 33 (click to reveal each step and answer), brain break 33 to 37, workbook page 1 37 to 49 (after question 3 you may choose: carry on, or try Think harder), check together 49 to 53, short teaching before page 2 53 to 58, workbook page 2 58 to 72 (alone: start with the questions named at the top, then choose; nobody has to finish), check together 72 to 76, talk time 76 to 82 (you may say pass; volunteers first; then everyone tries the first step of the Investigation), exit ticket 82 to 86, reflection 86 to 88 (pass is always OK), stamp and goodbye 88 to 90. Think harder, Go further and the Investigation are open to every child. The tutor never announces who is on which page, and never splits a pair unless both children agree. Private invitations only by private chat message.'))

# 2 warm1: guess my rule
body=h2('Warm-up: Guess My Rule')+card(p('Call out a number. I put it through a secret machine and tell you what comes out. Test your idea on the next number before you say the rule in words.',38,700))
body+=pin(128,400,1664,machine([('number','q'),('?','op'),('?','op'),('answer','res')],w=1664,h=130),None,WHITE,24,'16px 20px')
W3=[360,360,360]
body+=trow(128,590,['In','Out'],[300,300],None,True,36)
for i,(a,b) in enumerate([(2,7),(5,16),(10,31)]):
    body+=trow(128+(i+1)*0,590+80*(i+1),[str(a),str(b)],[300,300],'rise',False,36)
body+=pin(820,590,972,p('What do you notice? Is the rule "add 5"? Test it on the next number!',36,700),None,SOFT,20,'22px 28px')
body+=answer(820,740,972,'Rule: times 3, then add 1')
put(P+'warm1',sec(P+'warm1','0–4 MIN',body,
 'Minutes 0 to 4. Guess My Rule. Play without the slide first if you like: children call a number, you answer from your secret rule (times 3, then add 1), and write the pairs on the board. Round 1 uses the slide: click to show 2 to 7, 5 to 16, 10 to 31. '
 'Ask: "Is it add 5? 2 + 5 = 7 works! Now test 5." (5 + 5 = 10, not 16). This is the habit for today: TEST your rule on every case, not just the first. Then: "Say it in words: multiply by 3, then add 1." Click to reveal. '
 'Rounds 2 and 3: make up your own secret rule (one or two steps) and let the group guess; use 1 to 10 as inputs and add 0 to see what the machine does to 0. Listen for children who say "it goes up by 3" (true for the steps) but cannot say what happens to 100. That gap is today\'s lesson.'))

# 3 warm2
qs=[('1.','7, 11, 15, 19, __, __','23, 27'),('2.','1, 4, 9, 16, 25, __','36'),('3.','2, 6, 18, 54, __','162'),('4.','The 20th even number','40'),('5.','4 × 25 + 3','103')]
body=h2('Quick questions')+''.join(qrow(128,250+i*125,1250,a,b) for i,(a,b,c) in enumerate(qs))+''.join(answer(1420,250+i*125,372,c) for i,(a,b,c) in enumerate(qs))
put(P+'warm2',sec(P+'warm2','4–9 MIN',body,'Minutes 4 to 9. Whiteboards up together, then click. Ask after 1: "What is the rule? add 4." After 2: "What do you notice about 1, 4, 9, 16, 25?" (square numbers: 1 × 1, 2 × 2 ...). After 3: "multiply by 3 each time", so it is not the same kind of pattern as 1. After 4: the 20th even number is 2 × 20 = 40, a rule in words: 2 × the place. Answers: 23 and 27; 36; 162; 40; 103.'))

# 4 explore1
g=''
import math
def poly(n,cx,cy,r):
    return [(cx+r*math.sin(2*math.pi*k/n),cy-r*math.cos(2*math.pi*k/n)) for k in range(n)]
for n,cx in [(2,200),(3,620),(4,1060)]:
    pts=[(cx-70,105),(cx+70,105)] if n==2 else poly(n,cx,105,80)
    for i in range(len(pts)):
        for j in range(i+1,len(pts)):
            g+=stick(pts[i][0],pts[i][1],pts[j][0],pts[j][1],TEAL,6)
    for (x,y) in pts: g+=f'<circle cx="{x:.1f}" cy="{y:.1f}" r="20" fill="{YEL}" stroke="{NAVY}" stroke-width="4"/>'
    g+=txt(cx,238,f'{n} children: {[1,3,6][n-2]} high five{"s" if n>2 else ""}',32,NAVY,font='Nunito Sans, Arial')
g+=txt(1500,90,'5 children?',44,TEAL)+txt(1500,150,'8 children?',44,TEAL)
steps=''.join(f'<li>{E(s)}</li>' for s in ['Guess first: if all 8 of us high-five everyone else once, how many high fives is that?','Start small: 2 children, then 3, then 4. Draw each child as a dot and each high five as a line.','Make a table: number of children, number of high fives.','Look for a pattern and use it to find the answer for 8.'])
body=h2('Explore: High Fives')+card(chip('EXPLORE')+f'<ol style="font-size:32px;font-weight:600;padding-left:52px;display:flex;flex-direction:column;gap:6px">{steps}</ol>')
body+=card(svgwrap(1640,252,'Dots joined by lines: 2 children and 1 line, 3 children and 3 lines, 4 children and 6 lines',g),extra='padding:16px 24px')
put(P+'explore1',sec(P+'explore1','9–14 MIN',body,'Minutes 9 to 14. Pairs. Online: breakout rooms, each pair draws dots on a whiteboard and joins them. Predict first: most children guess 8 × 8 = 64 or 8 + 7; write guesses down. Let them draw 2, 3, 4 and 5 dots before they look for the pattern. Anyone who wants more (open to every pair): a class of 30. The picture shows 1, 3 and 6 lines for 2, 3 and 4 children.'))

# 5 explore2
body=h2('Explore: talk about it')+numcards([('1.','How many high fives for 5 children? For 8? How did you get it?'),('2.','What does the table do? What does each new child add?'),('3.','Class of 30: is there a quick way?')],40)
put(P+'explore2',sec(P+'explore2','14–21 MIN',body,'Minutes 14 to 21. Gather pairs. Answers: 1) 5 children: 10. 8 children: 28. 2) Table 2, 3, 4, 5, 6, 7, 8 children: 1, 3, 6, 10, 15, 21, 28. The jumps are 2, 3, 4, 5, 6, 7: a new child high-fives everyone already there, so the 4th child adds 3, the 5th adds 4 and so on (the 8th child adds 7). 3) 30 children: each high-fives 29 others, 30 × 29 = 870, but every high five is counted twice (once by each child), so 870 ÷ 2 = 435. Do not push for this if nobody finds it; it returns on the Go further page. Note the jumps 2, 3, 4, 5 … grow each time; today we mostly study patterns that grow by the SAME amount each time.'))

# 6 teach1: matchstick squares
g=sq_fig(1,40,30)+sq_fig(2,270,30)+sq_fig(3,590,30)
g+=txt(75,150,'Figure 1',32,NAVY,font='Nunito Sans, Arial')+txt(340,150,'Figure 2',32,NAVY,font='Nunito Sans, Arial')+txt(700,150,'Figure 3',32,NAVY,font='Nunito Sans, Arial')
body=h2('Growing pattern: matchstick squares')+pin(128,230,1000,svgwrap(900,170,'Matchstick squares in a row: figure 1 has 4 sticks, figure 2 has 7 sticks, figure 3 has 10 sticks; the 3 new sticks of each new square are teal',g))
body+=trow(1000,240,['Figure','1','2','3','4'],[170,100,100,100,100],None,True,32)+trow(1000,320,['Sticks','4','7','10','13'],[170,100,100,100,100],'rise',False,32)
body+=step(1,'Each new square shares a side with the one before, so it adds only 3 sticks (the teal ones), not 4.',top=430,size=34)
body+=step(2,'Start with the first square\'s 4 sticks, or: 1 stick, then 3 for every square.  Rule in words: sticks = 3 × figure number + 1',top=540,size=34)
body+=step(3,'Check the rule on figures 1, 2 AND 3:  3 × 1 + 1 = 4,  3 × 2 + 1 = 7,  3 × 3 + 1 = 10 ✓',top=650,size=34)
body+=answer(128,770,1664,'Figure 25: 3 × 25 + 1 = 76 sticks. No drawing needed!')
put(P+'teach1',sec(P+'teach1','21–24 MIN',body,'Teach. Children build the three figures with toothpicks. Ask first: "How many sticks in figure 4? Figure 25?" Click the table row. Look at the picture: the teal sticks are the 3 new ones each time. Think-aloud: "Figure 2 is not 2 times figure 1 (8): the middle side is shared, so we save a stick. Each new square adds 3. I start with 1 stick and add 3 for each square: 3 times the figure number, plus the 1 extra." Then check the rule on three figures, not one. Trap to name: 25 lots of 3 plus 4 would be 79 (wrong), because the first square already counts its 4 sticks. The rule 3 × 25 + 1 = 76 is safe.'))
put(P+'try1',try_slide(P+'try1','24–25 MIN','Your turn: say the rule','A dot pattern has 7, 12, 17, 22, … dots in figures 1, 2, 3, 4.',[('a','What does each figure add?','5 more dots'),('b','Rule in words, then figure 12?','5 × 12 + 2 = 62'),('c','Is there a figure with 100 dots?','No: 98 ÷ 5 is not whole')],'Whiteboards, then click. a) 12 − 7 = 5. b) Figure 1 has 7 = 5 × 1 + 2, figure 2 has 12 = 5 × 2 + 2: dots = 5 × figure number + 2. Figure 12: 60 + 2 = 62. c) 100 − 2 = 98 and 98 ÷ 5 = 19.6, not a whole number, so 100 is not in the pattern. The numbers end in 2 or 7; 100 ends in 0.',38))

# 8 we1: backwards
body=h2('Working backwards: which figure?')+card(p('Matchstick squares: sticks = 3 × figure number + 1. Which figure uses 61 sticks?',38,700))
body+=machine([('figure','q'),('× 3','op'),('+ 1','op'),('61','res')],back='undo the last step first',w=1664,h=240)
body=body.replace('<svg aria-label="Number machine"','<svg aria-label="Number machine from figure number, times 3, plus 1, to 61 sticks with a backward arrow"')
body+=step(1,'Undo the last step first:  61 − 1 = 60',top=660,size=36)
body+=step(2,'Undo the times 3:  60 ÷ 3 = 20.   Check forwards: 3 × 20 + 1 = 61 ✓',top=760,size=36)
put(P+'we1',sec(P+'we1','25–27 MIN',body,'Worked example: backwards. Children first say what the machine does going forwards: times 3, then plus 1. Going backwards we undo in reverse order: the last step first. Click step 1, then step 2. Always check by going forward again. Ask: "What if the answer was 62 sticks?" (62 − 1 = 61, 61 ÷ 3 is not whole, so no figure uses exactly 62 sticks.) This is Q1c and Q3c on the worksheet.'))
put(P+'try2',try_slide(P+'try2','27–28 MIN','Your turn: backwards','Use sticks = 3 × figure number + 1 from the last slide.',[('a','Which figure has 100 sticks?','Figure 33'),('b','Is there a figure with exactly 50 sticks?','No: 49 ÷ 3'),('c','You have 80 sticks. Biggest figure you can make?','Figure 26')],'Whiteboards. a) 100 − 1 = 99, 99 ÷ 3 = 33. b) 50 − 1 = 49, 49 ÷ 3 is not a whole number. c) 80 − 1 = 79, 79 ÷ 3 = 26 remainder 1, so figure 26 uses 79 sticks with 1 left over (figure 27 needs 82).',38))

# 10 we2: two ways
g=tiles_fig(1,30,20)+tiles_fig(2,330,20)+tiles_fig(3,700,20)
g+=txt(97,190,'Figure 1',30,NAVY,font='Nunito Sans, Arial')+txt(440,190,'Figure 2',30,NAVY,font='Nunito Sans, Arial')+txt(830,190,'Figure 3',30,NAVY,font='Nunito Sans, Arial')
body=h2('Seeing it two ways: tiles with a border')+pin(128,230,1100,svgwrap(1000,205,'Figure 1 has 1 yellow tile and 8 grey border tiles, figure 2 has 2 yellow and 10 grey, figure 3 has 3 yellow and 12 grey',g))
body+=pin(1180,240,612,p('Grey tiles: 8, 10, 12. How many in figure 12?',36,700),None,SOFT,20,'22px 26px')
body+=step(1,'Way 1: a top row and a bottom row of (figure + 2) tiles, and 1 tile at each end:  2 × figure number + 6',top=470,size=34)
body+=step(2,'Way 2: the whole rectangle has 3 rows of (figure + 2) tiles. Take away the yellow ones:  3 × (figure + 2) − figure.  Figure 12: 3 × 14 − 12',top=590,size=34)
body+=answer(128,740,1664,'Both ways give 30 grey tiles in figure 12.')
body+=pin(128,830,1664,p('Different pictures, different-looking rules, the same answer. Check each rule on figures 1, 2, 3.',34,700),'fade',WHITE,20,'16px 28px')
put(P+'we2',sec(P+'we2','28–31 MIN',body,'Worked example: two ways to see one pattern. First let children count the grey tiles in figures 1, 2 and 3 on their own. Then show Way 1 (top and bottom rows plus the two end tiles): figure 12 has 14 + 14 + 2 = 30 grey tiles. Way 2: the whole 3 by 14 rectangle has 42 tiles; 12 are yellow, so 42 − 12 = 30. Both rules are the same: 3 × (figure + 2) − figure = 2 × figure + 6. Do not need to simplify with letters; just check that both give 8, 10, 12 for the first three figures. The grey count grows by 2 each time, which is why the rule has 2 × figure number in it, like the chairs in Q1.'))
put(P+'try3',try_slide(P+'try3','31–32 MIN','Your turn: border tiles','Grey tiles = 2 × figure number + 6.',[('a','Grey tiles in figure 10?','26'),('b','Which figure has 40 grey tiles?','Figure 17'),('c','Can a figure have 45 grey tiles?','No: 39 ÷ 2')],'Whiteboards. a) 2 × 10 + 6 = 26. b) 40 − 6 = 34, 34 ÷ 2 = 17. c) 45 − 6 = 39 and 39 ÷ 2 is not a whole number. Also: the grey count is always even.',38))

# key
body=h2('Key idea: find the rule, say it in words')+card(p('Ask: what stays the same and what grows? Look at the picture to see WHY. Say the rule in words: sticks = 3 × figure number + 1.',42,700))+card(p('Check the rule on every figure you know. To go backwards, undo the steps in reverse order.',38,600,MUTED))
put(P+'key',sec(P+'key','32–33 MIN',body,'Say the key idea together. Common mistakes to watch for during the worksheet: (1) Doubling: figure 20 is NOT twice figure 10, because the starting stick or the end chairs get counted twice. (2) Counting the jumps wrongly, 25 lots of 3 instead of 24 for figure 25 when starting from figure 1, or writing the rule as "add 3" without saying what to do with the figure number. (3) Supposition: dividing the gap by the value of one thing (22 ÷ 4) instead of the change for each swap (22 ÷ 2), and not checking BOTH facts (how many things and the total).'))
put(P+'break',break_slide(P+'break','33–37 MIN','Pattern moves: clap, clap, stamp, clap, clap, stamp … Do 12 moves together.','Five minutes. Online: everyone stands on camera. Do the pattern for 12 moves (children say the number of each move). Then ask: what is the 20th move? The 30th? (every 3rd move is a stamp, so multiples of 3: 30th is a stamp, 20th is a clap since 20 = 18 + 2.) Do not let children count up to 30; ask for a rule.'))

# ws1
put(P+'ws1',ws_preview(P+'ws1','37–49 MIN','Worksheet page 1: with your partner',[('Q1','Tables and chairs. Rule in words, and a trap about doubling.'),('Q2','Matchstick houses. Why does each house add only 5?')],'Stuck? Build figures 1, 2, 3 with toothpicks or paper squares.','Minutes 37 to 49. Walk around. Ask "Show me where in the picture the rule comes from" before any help. Q1d and Q2c are the tricky ones (doubling does not work; leftover sticks). Anyone who wants more (open to every pair): draw figure 4 of the border-tiles pattern from the slides and count the grey tiles (12 grey).'))
put(P+'ws1ans',checks(P+'ws1ans','49–51 MIN','Page 1: check together',[('Q1','a) 10, 12, 22   b) 2 × tables + 2   c) 24 tables   d) No: 20 tables seat 42'),('Q2','a) 5 sticks (shares a wall)   b) 5 × houses + 1; 101 sticks   c) 39 houses, 4 sticks left')],
 'Click each answer after a pair explains. Q1c: 50 − 2 = 48, 48 ÷ 2 = 24. Q1d: 2 × 20 + 2 = 42; doubling counts the two end chairs twice. Q2a: the first house needs 6 sticks; each new house shares its left wall, so it needs a roof (2), a floor (1), a top (1) and a right wall (1) = 5. Q2c: 200 − 1 = 199, 199 ÷ 5 = 39 remainder 4. Compare with the border-tiles example on the slides: the grey tiles grow by 2 each figure, so the rule has 2 × figure number in it.',gapy=190))

# teach guess and check: drinks
W5=[220,220,330,300]
body=h2('Guess and check with a table')+card(p('Ravi buys 12 drinks for $29. Teh costs $2 and kopi costs $3. How many of each?',38,700))
body+=trow(128,370,['Teh','Kopi','Total','Check'],W5,None,True,34)
rows=[['6','6','$12 + $18 = $30','too much'],['8','4','$16 + $12 = $28','too little']]
body+=trow(128,450,rows[0],W5,'rise',False,34)+trow(128,530,rows[1],W5,'rise',False,34)
body+=trow(128,610,['7','5','$14 + $15 = $29','just right'],W5,'rise',False,34)
body+=pin(1420,370,372,p('Each swap of a teh for a kopi changes the total by $1. Use that to jump close!',32,700),None,SOFT,20,'18px 24px')
body+=answer(128,720,1664,'7 teh and 5 kopi.  Check both facts: 7 + 5 = 12 drinks ✓')
body+=pin(128,820,1664,p('A good guess uses the first answer: $30 is $1 too much, so swap one kopi for a teh.',34,700),'fade',WHITE,20,'16px 28px')
put(P+'teachgs',sec(P+'teachgs','51–53 MIN',body,'Teach before worksheet page 2 (Q3). Start with a guess that is easy to check: half and half, 6 and 6 = $30. Too much by $1. Ask: "Which way do we change it?" A teh costs less, so we need more teh and fewer kopi. Each swap (one kopi becomes one teh) takes $1 off. One swap: 7 teh, 5 kopi = $29. Compare a random guess of 2 and 10 (way too much): a table that you CHANGE using what the last row told you finds the answer in 3 or 4 rows. Always check both facts: number of drinks AND the total.'))

# supposition
body=h2('Supposition: suppose they are all the same')+card(p('A car park has 24 cars and motorcycles with 70 wheels altogether. A car has 4 wheels and a motorcycle has 2 wheels. How many cars?',36,700))
body+=step(1,'Suppose all 24 are motorcycles:  24 × 2 = 48 wheels.',top=430,size=34)
body+=step(2,'We are short:  70 − 48 = 22 wheels.',top=530,size=34)
body+=step(3,'Each motorcycle changed to a car adds 4 − 2 = 2 wheels.  22 ÷ 2 = 11 cars.',top=630,size=34)
body+=answer(128,740,1664,'11 cars and 13 motorcycles.  Check: 44 + 26 = 70 wheels ✓,  11 + 13 = 24 ✓')
body+=pin(128,830,1664,p('Divide the gap by the change for ONE swap, not by the value of one thing.',34,700),'fade',WHITE,20,'16px 28px')
put(P+'teachsup',sec(P+'teachsup','53–55 MIN',body,'Teach before worksheet page 2 (Q4). The same problem as the table, but faster. Click through. The key question after step 2 is "what happens to the total when I change ONE motorcycle into ONE car?" The answer is 2, not 4 (the motorcycle\'s 2 wheels are replaced). Show the other way too: suppose all cars: 96 wheels, 26 too many, each swap removes 2, 13 motorcycles. Same answer. Compare with the table: when numbers are big, supposition is quicker.'))

# marks taken away
body=h2('Marks taken away')+card(p('A quiz has 12 questions. Each correct answer scores 5 marks and each wrong answer loses 1 mark. Siti answers every question and scores 42. How many are correct?',34,700))
body+=step(1,'Suppose all 12 are correct:  12 × 5 = 60 marks.',top=450,size=34)
body+=step(2,'We scored less:  60 − 42 = 18 marks fewer.',top=550,size=34)
body+=step(3,'Each wrong answer loses the 5 marks AND 1 more mark taken away: 5 + 1 = 6 marks.  18 ÷ 6 = 3 wrong.',top=650,size=32)
body+=answer(128,800,1664,'9 correct, 3 wrong.  Check: 45 − 3 = 42 ✓')
put(P+'teachmarks',sec(P+'teachmarks','55–57 MIN',body,'Teach before worksheet page 2 (Q5). This is supposition with a twist: a wrong answer costs more than missing out on the 5 marks, because 1 mark is also taken off. Ask after step 2: "What is the difference between a correct answer and a wrong answer?" (6 marks: from +5 to −1.) Check with the other fact: 9 × 5 = 45, minus 3 × 1 = 3, gives 42. Q5b of the worksheet asks why one score is impossible: every score is 100 minus a multiple of 7 in that quiz.'))

# ws2
put(P+'ws2',ws_preview(P+'ws2','57–72 MIN','Worksheet page 2: on your own',[('Q3','Tickets. Guess and check with a table. Change your guess using the last row.'),('Q4','Coins. Suppose they are all 20¢, then swap.'),('Q5','The quiz with marks taken away, and why one score is impossible.')],'Want more? Think harder and Go further are at the back of your workbook.','Children work alone. Q3: check that each row changes from the one before. Q5b: a good explanation says that each wrong answer costs 7 marks, so scores go down in 7s from 100.'))
put(P+'ws2ans',checks(P+'ws2ans','72–76 MIN','Page 2: check together',[('Q3','8 adult tickets and 7 child tickets: $96 + $49 = $145'),('Q4','a) $6.00; up by 30¢   b) 14 fifty-cent coins (and 16 twenty-cent coins)'),('Q5','a) 15 correct, 5 wrong   b) Scores go 100, 93, 86, 79 … 80 is not one of them')],
 'Click after a child explains. Q3: 15 × $7 = $105 if all child; $145 − $105 = $40; each adult in place of a child adds $5; 40 ÷ 5 = 8 adults. Q4: 30 × 20¢ = $6.00; $10.20 − $6.00 = $4.20; each swap adds 30¢; $4.20 ÷ 30¢ = 14. Check 14 × 50¢ = $7.00 and 16 × 20¢ = $3.20, total $10.20. Q5a: all correct is 100; each wrong costs 5 + 2 = 7; 100 − 65 = 35; 35 ÷ 7 = 5 wrong; 15 correct; check 75 − 10 = 65. Q5b: 100 − 80 = 20, which is not a multiple of 7, so no whole number of wrong answers fits.',gapy=190))

# stretch
st=[('1.','Ali saves $3 in week 1. Each week he saves $2 more than the week before. How much does he save in week 15?'),('2.','3, 8, 13, 18, …  What is the first number in this pattern that is greater than 200?'),('3.','A test has 10 questions. A correct answer scores 3 marks and 1 mark is taken away for each wrong answer. Siti answered every question and scored 18. How many did she get correct?')]
put(P+'stretch',sec(P+'stretch','37–72 MIN  •  OPTION',h2('Think harder')+numcards(st,36),'Answers: 1) $31 (week 15 is 14 jumps of $2 after week 1: $3 + $28). 2) 203 (add 5 each time; the 40th number is 3 + 39 × 5 = 198, which is not above 200, so the 41st, 203, is the first). 3) 7 correct and 3 wrong (all correct would be 30; each wrong answer costs 3 + 1 = 4; 12 ÷ 4 = 3 wrong; check 21 − 3 = 18).'))
ch=[('1.','A dot pattern makes diamonds. Figure 1 has 1 dot. Figure 2 has rows of 1, 3 and 1 dots. Figure 3 has rows of 1, 3, 5, 3 and 1 dots. How many dots are in figure 6?'),('2.','A quiz has 25 questions. A correct answer scores 4 marks, 1 mark is taken away for each wrong answer, and a blank scores 0. Mei left 3 questions blank and scored 68. How many did she get correct?')]
put(P+'challenge',sec(P+'challenge','37–72 MIN  •  OPTION',h2('Go further')+numcards(ch,34),'Pairs try first, then the "see it" slide, then the walk-through. These are Go further Q5 and Q6 (the first two of the three Go further items). Answers: 1) 61 dots. 2) 18 correct.'))
# chdiag
g1=''
rows_=[[1],[1,3,1],[1,3,5,3,1]]
for k,rw in enumerate(rows_):
    n=len(rw); cx=[90,330,610][k]; cy0=40
    for r,c in enumerate(rw):
        for d in range(c):
            x=cx+(d-(c-1)/2)*34; y=cy0+r*34
            g1+=f'<circle cx="{x:.1f}" cy="{y}" r="12" fill="{YEL}" stroke="{NAVY}" stroke-width="3"/>'
    g1+=txt(cx,40+5*34+10,f'Figure {k+1}: {[1,5,13][k]}',28,NAVY,font='Nunito Sans, Arial')
g1+=txt(380,300,'Figure 6 = ?',34,TEAL)
g2=''
for i,(lab) in enumerate(['Answered','Blank','Correct','Wrong']):
    pass
g2+=tag_box(20,20,230,80,'25 questions',SKY,28)+tag_box(290,20,200,80,'3 blank',WHITE,28)+tag_box(530,20,190,80,'? answered',YEL,28)
g2+=tag_box(20,150,330,80,'Correct: +4 each',WHITE,28)+tag_box(390,150,330,80,'Wrong: −1 each',WHITE,28)+tag_box(20,280,700,80,'Total score 68. Correct = ?',YEL,30)
body=h2('Go further: see it',60)+'<div style="display:flex;gap:32px;align-items:flex-start">'
body+=card(f'<p style="font-size:30px;font-weight:700;color:{TEAL}">Q1: Count the dots in each row</p>'+svgwrap(760,330,'Diamond dot patterns for figures 1, 2 and 3 with 1, 5 and 13 dots, and a question mark for figure 6',g1).replace('width:760px;height:330px;flex:none','width:100%;height:auto;display:block'),extra='flex:1;min-width:0;padding:20px 24px')
body+=card(f'<p style="font-size:30px;font-weight:700;color:{TEAL}">Q2: Sort the 25 questions</p>'+svgwrap(760,380,'Boxes: 25 questions, 3 blank, correct scores 4, wrong loses 1, total 68',g2).replace('width:760px;height:380px;flex:none','width:100%;height:auto;display:block'),extra='flex:1;min-width:0;padding:20px 24px')+'</div>'
put(P+'chdiag',sec(P+'chdiag','37–72 MIN  •  OPTION',body,'Show after pairs have tried Go further, or if they are stuck. The pictures show the problem, not the answers. Ask: What do you notice about the rows of the diamond? Do the blanks count as answered? Answers are in the Go further slide notes.'))
body=h2('Go further: walk-through')+pin(128,250,800,p('Q1: two squares of dots',38,800,TEAL))
for i,t in enumerate(['Figures: 1, 5, 13 … rows 1 | 1, 3, 1 | 1, 3, 5, 3, 1','The widest row of figure 6 has 2 × 6 − 1 = 11 dots','Figure 6 = 6 × 6 + 5 × 5 = 36 + 25','= 61 dots.  Check: 1, 5, 13, 25, 41, 61 ✓']): body+=pin(128,330+i*125,800,p(t,30),'rise',WHITE)
body+=pin(992,250,800,p('Q2: suppose all answers are correct',38,800,TEAL))
for i,t in enumerate(['Answered: 25 − 3 = 22 questions','All 22 correct: 22 × 4 = 88 marks','88 − 68 = 20 marks lost; each wrong loses 4 + 1 = 5','20 ÷ 5 = 4 wrong, so 18 correct. Check: 72 − 4 = 68 ✓']): body+=pin(992,330+i*125,800,p(t,30),'rise',WHITE)
put(P+'chwalk',sec(P+'chwalk','37–72 MIN  •  OPTION',body,'Use after pairs have tried. Q1: in a diamond the rows go up 1, 3, 5 … to the widest row and back down. The widest row of figure 6 has 2 × 6 − 1 = 11 dots. The top half, including the widest row, is a square number of dots (6 × 6 = 36 for figure 6) and the bottom half is the square number before it (5 × 5 = 25). Figure 6: 36 + 25 = 61. Q2: blank questions score nothing and lose nothing, so only the 22 answered ones matter: suppose all 22 correct (88 marks), the gap is 20, each wrong answer costs 5 (the 4 you do not get and the 1 taken away), so 4 wrong and 18 correct.'))

# talk / exit
body=h2('Talk time')+card(chip('TALK TIME',YEL,NAVY)+p('Mei says: “10 squares in a row need 31 sticks, so 20 squares need 62 sticks.” Is she right? Show with a picture.',42,600))+card(p('Sentence starters:',34,400,MUTED)+p('“I noticed that …”   “I tested it by …”   “I know because …”',38,600))
put(P+'talk',sec(P+'talk','76–82 MIN',body,'Minutes 76 to 82. Pairs talk for 2 minutes, then share. Answer: no, 20 squares need 3 × 20 + 1 = 61 sticks. Doubling doubles the 1 extra starting stick too, so it is one stick too many. Draw 10 squares, then another 10 squares joined on: the 11th square joins the 10th by sharing a side, so the sticks add up to 31 + 30 = 61. The same trap appears with chairs in Q1d. Second question if time: "In Q4 and Q5, which method did you like better, a table or supposing? Why?"'))
body=h2('Exit ticket')+card(chip('EXIT TICKET')+p('Figure 1 of a pattern has 6 dots. Each figure has 4 more dots than the figure before.  (a) How many dots are in figure 20?  (b) Which figure has 102 dots?',44,600))+card(p('Write your answers on a slip of paper. Show it to your tutor. Then collect your stamp in your inquiry journal.',34,400))
put(P+'exit',sec(P+'exit','82–90 MIN',body,'Minutes 82 to 90. Answers: (a) 82 (dots = 4 × figure number + 2; 4 × 20 + 2 = 82, or 6 + 19 × 4). (b) Figure 25 (102 − 2 = 100, 100 ÷ 4 = 25). Extension: a square grid of matchsticks: 1 by 1 uses 4 sticks, 2 by 2 uses 12. How many for 3 by 3 and 10 by 10? (24 and 220.)'))

order=[P+x for x in ['title','warm1','warm2','explore1','explore2','teach1','try1','we1','try2','we2','try3','key','break','ws1','ws1ans','teachgs','teachsup','teachmarks','ws2','ws2ans','stretch','challenge','chdiag','chwalk','talk','exit']]
write_deck(9,'Math Inquirers P5: Lesson 9 – Pattern Generalisers',order,{'s1':{'description':'Warm-up and explore','start':P+'title'},'s2':{'description':'Teach: growing patterns and the rule in words','start':P+'teach1'},'s3':{'description':'Worksheet with teaching before each page','start':P+'break'},'s4':{'description':'Think harder, Go further, talk and exit','start':P+'stretch'}},D)

import p5_gaps; p5_gaps.apply(9)
