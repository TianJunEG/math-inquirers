"""Math Inquirers P2, Lesson 4: Pattern Machines. Writes split/p2l4/project (deck.json + slides/*.html)."""
import json,os,sys,shutil,datetime
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,H)
import slidekit
slidekit.FOOT='Math Inquirers P2 Holiday Program  •  Notice it. Test it. Explain why.'
from slidekit import *
import p2gaps
RED='#D64545'; BLUE='#4A7FD6'; GREEN='#3DBE7A'; BROWN='#C98A1A'
D=os.path.join(H,'..','split','p2l4','project'); S={}; ORDER=[]
def put(i,h): S[i]=h; ORDER.append(i)

# ---------- generic slides ----------
def title_slide(sid,label,title,topic,today,notes):
    return (f'<section id="{sid}" data-transition="fade" style="background:{NAVY};color:{CREAM};font-family:{BF};padding:128px 128px 160px;display:flex;flex-direction:column;justify-content:center;gap:36px">\n'
            f'<p style="font-size:32px;font-weight:700;letter-spacing:4px;color:{YEL}">{E(label)}</p>\n'
            f'<h1 style="font-family:{HF};font-size:120px;font-weight:600;line-height:1.05">{E(title)}</h1>\n'
            f'<p style="font-size:44px;color:#C9D4EC">{E(topic)}</p>\n'
            f'<div style="background:#26385F;border-radius:24px;padding:40px;display:flex;flex-direction:column;gap:12px"><p style="font-size:28px;font-weight:700;letter-spacing:3px;color:{YEL}">TODAY WE WILL</p><p style="font-size:44px;font-weight:600">{E(today)}</p></div>\n'
            f'<p style="position:absolute;left:128px;bottom:64px;width:1400px;font-size:24px;color:#B7C3DD">{E(slidekit.FOOT)}</p>\n<aside>{E(notes)}</aside>\n</section>\n')
def break_slide(sid,time,head,text,sub,notes):
    return (f'<section id="{sid}" data-transition="fade" style="background:{TEAL};color:{CREAM};font-family:{BF};padding:128px 128px 160px;display:flex;flex-direction:column;justify-content:center;gap:36px">\n'
            f'<p style="font-size:32px;font-weight:700;letter-spacing:4px;color:{YEL}">{E(time)}</p>\n'
            f'<h2 style="font-family:{HF};font-size:110px;font-weight:600;line-height:1.05">{E(head)}</h2>\n'
            f'<p style="font-size:48px;font-weight:600;line-height:1.3">{E(text)}</p>\n<p style="font-size:36px;color:#D7EFEA">{E(sub)}</p>\n'
            f'<p style="position:absolute;left:128px;bottom:64px;width:1400px;font-size:24px;color:#D7EFEA">{E(slidekit.FOOT)}</p>\n<aside>{E(notes)}</aside>\n</section>\n')
def explore1(sid,time,steps,pic,notes,picw=760):
    lst=''.join(f'<li>{E(s)}</li>' for s in steps)
    left=card(chip('EXPLORE')+f'<ol style="margin:0;font-size:36px;font-weight:600;padding-left:48px;display:flex;flex-direction:column;gap:16px;line-height:1.3">{lst}</ol>',extra='flex:1;min-width:0')
    right=card(pic,extra=f'width:{picw}px;flex:none;align-items:center;justify-content:center;padding:20px')
    return sec(sid,time,h2('Explore: what to do')+f'<div style="display:flex;gap:32px;align-items:stretch">{left}{right}</div>',notes)
def numbered_cards(items,size=40):
    return ''.join(card(p(f'<span style="color:{TEAL}">{a}</span>  {E(b)}',size,600,raw=True)) for a,b in items)
def talk_slide(sid,time,q,notes):
    body=h2('Talk time')+card(chip('TALK TIME',YEL,NAVY)+p(q,42))+card(p('Sentence starters:',34,400,MUTED)+p('“I noticed that …”   “I tested it by …”   “I know because …”',38))
    return sec(sid,time,body,notes)
def exit_slide(sid,time,q,notes):
    body=h2('Exit ticket')+card(chip('EXIT TICKET')+p(q,46))+card(p('Write your answer on a slip of paper. Show it to your tutor. Then collect your stamp in your inquiry journal.',34,400))
    return sec(sid,time,body,notes)
def svgwrap(label,vw,vh,inner,w=None,h=None,extra=''):
    w=w or vw; h=h or vh
    return f'<svg aria-label="{E(label)}" viewBox="0 0 {vw} {vh}" xmlns="http://www.w3.org/2000/svg" style="width:{w}px;height:{h}px;flex:none;{extra}">{inner}</svg>'
def T(x,y,s,size=30,fill=NAVY,w=700,anchor='middle',font='Fredoka, Arial'):
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{w}" text-anchor="{anchor}" fill="{fill}" font-family="{font}">{E(s)}</text>'

# ---------- pictures ----------
def sun(x,y,r=34):
    rays=''.join(f'<line x1="{x}" y1="{y-r-6}" x2="{x}" y2="{y-r-20}" stroke="{NAVY}" stroke-width="5" stroke-linecap="round" transform="rotate({k*45} {x} {y})"/>' for k in range(8))
    return rays+f'<circle cx="{x}" cy="{y}" r="{r}" fill="{YEL}" stroke="{NAVY}" stroke-width="5"/>'
def moon(x,y,r=40):
    return f'<path d="M{x+8} {y-r} A{r} {r} 0 1 0 {x+8} {y+r} A{r*0.78:.1f} {r*0.78:.1f} 0 1 1 {x+8} {y-r} Z" fill="{SKY}" stroke="{NAVY}" stroke-width="5" stroke-linejoin="round"/>'
def star(x,y,r=44):
    import math
    pts=' '.join(f'{x+(r if k%2==0 else r*0.45)*math.sin(math.pi*k/5):.1f},{y-(r if k%2==0 else r*0.45)*math.cos(math.pi*k/5):.1f}' for k in range(10))
    return f'<polygon points="{pts}" fill="{TEAL}" stroke="{NAVY}" stroke-width="5" stroke-linejoin="round"/>'
def sky_strip(n=9,cell=180,h=200,label=True):
    g=''
    for i in range(n):
        x=cell/2+i*cell+10; k=i%3
        g+=(sun,moon,star)[k](x,78)
        if label: g+=T(x,178,str(i+1),34,TEAL)
        if k==2 and i<n-1: g+=f'<line x1="{x+cell/2}" y1="10" x2="{x+cell/2}" y2="190" stroke="{MUTED}" stroke-width="3" stroke-dasharray="10 8"/>'
    return svgwrap('Pattern: sun, moon, star, repeated 3 times, with places 1 to 9',n*cell+20,h,g,1664,h*1664/(n*cell+20))
def beads(seq,cols,lab='beads',w=1664,h=110,r=44,gap=112,dots=True):
    g=f'<line x1="10" y1="55" x2="{w-10}" y2="55" stroke="{NAVY}" stroke-width="4"/>'
    for i,c in enumerate(seq):
        x=60+i*gap; g+=f'<circle cx="{x}" cy="55" r="{r}" fill="{cols[c][0]}" stroke="{NAVY}" stroke-width="4"/>'+T(x,66,cols[c][1],30,cols[c][2])
    if dots: g+=T(60+len(seq)*gap,66,'…',44)
    return svgwrap(lab,w,h,g,w,h)
def cube(x,y,s,col): return f'<rect x="{x}" y="{y}" width="{s}" height="{s}" rx="6" fill="{col}" stroke="{NAVY}" stroke-width="4"/>'

# ---------- 1. title ----------
put('p2l4-title',title_slide('p2l4-title','P2  •  LESSON 4  •  WEEK 2','Pattern Machines','Patterns with Multiplication','Find far places in a pattern by counting in groups, and find the rule of a growing pattern with a table.',
 'Objective: Find far places in a repeating pattern by counting in groups (the ends of the groups are in a times table); count how many of one shape there are; describe a growing pattern with a table and a rule and use it forwards and backwards; find the numbers that two counting patterns share. Tables used: 2, 3, 4, 5 and 10 only. '
 'Thinking strategies taught today: LOOK FOR A PATTERN (group size, where groups end) and MAKE A TABLE / MAKE A LIST (growing patterns, two counting lists). '
 'Materials: Linking cubes in 3 colours (about 20 per pair), mini whiteboards, matchsticks or lolly sticks (about 25 per pair), counters. '
 'Online: Coloured pencils and squared paper (or Lego bricks) for the cube train; children draw sticks for the growing pattern and show their tutor their tables on camera or keep them to share if they want. '
 'Time plan: warm-up 0 to 8, explore 8 to 20 (explore2 talk is 6 minutes), teaching 20 to 32 (click to reveal each step and answer), brain break 32 to 36, worksheet page 1 36 to 50 then check together 50 to 52, short teaching 52 to 57, worksheet page 2 57 to 69 then check together 69 to 72, talk time 72 to 80, exit ticket 80 to 90. Stretch and Challenge slides are for early finishers.'))

# ---------- 2. warm-up game ----------
g=''
for i in range(6):
    x=20+i*274; st=(i%3==2)
    g+=f'<rect x="{x}" y="10" width="250" height="120" rx="20" fill="{TEAL if st else YEL}" stroke="{NAVY}" stroke-width="5"/>'+T(x+125,86,'STOMP' if st else 'CLAP',48,CREAM if st else NAVY)+T(x+125,180,f'beat {i+1}',32,TEAL)
body=h2('Warm-up: pattern rhythm')+pin(128,250,1664,svgwrap('Beats 1 to 6: clap, clap, stomp, clap, clap, stomp',1664,200,g,1664,200))
for i,(q,a) in enumerate([('Beat 9?','STOMP: 9 is in the 3 times table'),('Beat 10?','CLAP: 9 ends a group, 10 starts again'),('Beat 20?','CLAP: 18 ends a group, then 19, 20')]):
    L=128+i*565
    body+=pin(L,500,533,p(q,48,700),None,WHITE,24,'24px 28px',f'box-sizing:border-box;height:330px;border:4px solid {NAVY};box-shadow:8px 8px 0 {NAVY}')
    body+=pin(L+20,640,493,f'<p style="font-size:32px;font-weight:800;line-height:1.25">{E(a)}</p>','pop',SOFT,16,'14px 20px',f'box-sizing:border-box;border:3px solid {NAVY}')
put('p2l4-warm1',sec('p2l4-warm1','0–5 MIN',body,
 'Minutes 0 to 5. Pattern rhythm. Everyone stands. Do clap, clap, stomp together for a few rounds while counting the beats aloud. Freeze, then ask each question; take predictions before clicking. '
 'Answers: beat 9 is a stomp (stomps are on 3, 6, 9: the 3 times table); beat 10 is a clap (9 ends a group, so 10 is the first beat of the next group); beat 20 is a clap (18 ends a group, 19 is clap 1, 20 is clap 2). '
 'Ask: "Which beats are stomps?" (3, 6, 9, 12 …). "How did you find beat 20 without clapping 20 times?" Online: children clap and stomp in view of the camera.'))
qs=[('1.','4, 8, 12, __','16'),('2.','50, 45, 40, __','35'),('3.','3, 6, 9, 12, __','15'),('4.','Count in 4s from 4. What is the 10th number?','40'),('5.','2, 5, 8, 11, __','14')]
body=h2('Quick questions')+''.join(qrow(128,250+i*125,1250,a,b) for i,(a,b,c) in enumerate(qs))+''.join(answer(1420,250+i*125,372,c) for i,(a,b,c) in enumerate(qs))
put('p2l4-warm2',sec('p2l4-warm2','5–8 MIN',body,'Minutes 5 to 8. Read each one aloud, take answers, then click to show. Answers: 16, 35, 15, 40, 14. Ask for the rule each time: add 4; take away 5; add 3; the 10th number in the 4 times table is 4 × 10; add 3. For 5 ask: "Is this the 3 times table?" (No: it starts at 2. Each number is 1 less than a 3 times table number.)'))

# ---------- 3. explore ----------
CC={'R':RED,'B':BLUE}
g=''.join(cube(20+i*78,30,70,CC['RRB'[i%3]])+T(55+i*78,140,str(i+1),30,TEAL) for i in range(9))
g+=T(380,220,'Keep going …',32,MUTED)+cube(560,170,70,WHITE)+T(595,218,'?',44)+T(595,280,'cube 20',30,TEAL)
put('p2l4-explore1',explore1('p2l4-explore1','8–14 MIN',['Build a cube train: red, red, blue, red, red, blue …','Stop after 9 cubes.','Predict: what colour is cube 20? Write it down.','Build to check. Which cubes are blue?'],
 svgwrap('A cube train of 9 cubes: red, red, blue three times, and a question mark for cube 20',720,300,g,700,292),
 'Minutes 8 to 14. Pairs build 9 cubes, then STOP and write a prediction for cube 20 before building on. Ask: "How could you know without building?" Online: children colour squares on squared paper or use Lego. The answers are in the next slide\'s notes.'))
put('p2l4-explore2',sec('p2l4-explore2','14–20 MIN',h2('Explore: talk about it')+numbered_cards([('1.','What colour is cube 20?'),('2.','How did you know without building?'),('3.','Which cubes are blue? What do you notice?')]),
 'Minutes 14 to 20. Gather the pairs and take answers. Answers: 1) Red. 2) The blue cubes are at 3, 6, 9, 12, 15, 18; then 19 and 20 are red. 3) The blue cubes are the 3 times table, because each group of 3 ends with a blue. '
 'Push: "What colour is cube 30? Cube 31?" (blue; red). Say: "The group is 3 cubes long, so the 3 times table tells us where each group ends. Today we use that idea to jump far along a pattern."'))

# ---------- 4. teach: far places ----------
body=h2('Far places: count in groups')+pin(128,240,1664,sky_strip())
body+=pin(128,470,1664,p('What is in place 14?',40,700),None,WHITE,20,'18px 28px')
body+=step(1,'One group is sun, moon, star: 3 shapes. Each group ends with a star.',top=570,size=36)
body+=step(2,'Groups end at 3, 6, 9, 12 (count in 3s). Place 12 is a star.',top=680,size=36)
body+=answer(128,790,1664,'13 starts again with a sun, so place 14 is a MOON.')
put('p2l4-teach1',sec('p2l4-teach1','20–22 MIN',body,'Teach. Point to the dashed lines: "Each line marks the end of a group." Click to reveal each step. Think-aloud: "Sun, moon, star, sun, moon, star. The group is 3 shapes long. Every group ends with a star, at 3, 6, 9, 12: the 3 times table. Place 14? 12 is the end of a group, so 13 starts again with a sun, and 14 is a moon." '
 'Ask: "Is 12 the first shape of a group or the last?" (the last). Children often say "12 is in the 3 times table so it is a sun"; point at place 3, 6 and 9 to show they are stars.'))
body=h2('Worked example: which place? how many?')+pin(128,230,1664,sky_strip(h=200),None)
body+=pin(128,460,800,p('Where is the 5th star?',38,800,TEAL))+pin(992,460,800,p('How many moons in the first 21 shapes?',38,800,TEAL))
for i,t in enumerate(['One star at the end of each group.','Stars: 3, 6, 9, 12, 15.']): body+=pin(128,540+i*110,800,p(t,34),'rise',WHITE)
for i,t in enumerate(['21 shapes: 3, 6, 9 … 21 is 7 groups.','One moon in each group.']): body+=pin(992,540+i*110,800,p(t,34),'rise',WHITE)
body+=answer(128,770,800,'Place 15  (5 groups of 3)')+answer(992,770,800,'7 moons')
put('p2l4-we1',sec('p2l4-we1','22–25 MIN',body,'Click to reveal the left steps and answer, then the right. Think-aloud: "Where is the 5th star? There is one star at the end of each group, so the 5th star ends the 5th group: 5 × 3 = 15." "How many moons in the first 21 shapes? 21 is in the 3 times table: 7 groups. One moon in each group, so 7 moons." '
 'Ask: "How many suns in the first 22 shapes?" (8: 7 groups, and place 22 starts the 8th group with a sun).'))
BC={'B':(BLUE,'B',WHITE),'G':(GREEN,'G',NAVY)}
body=h2('Count the groups')+pin(128,240,1664,p('Beads: 1 blue, 3 green, 1 blue, 3 green … Ben uses 5 blue beads. The string ends with green beads. How many green beads? How many beads altogether?',34,700),None,WHITE,20,'18px 28px')
body+=pin(128,400,1664,beads('BGGGBGGG',BC,'Beads: blue, green, green, green, repeated'))
body+=step(1,'1 blue and 3 green make one group of 4 beads.',top=540,size=36)
body+=step(2,'5 blue beads, so there are 5 groups.',top=650,size=36)
body+=answer(128,760,1664,'Green: 5 × 3 = 15.   Altogether: 5 × 4 = 20 beads.')
put('p2l4-teachcount',sec('p2l4-teachcount','25–27 MIN',body,'Teach before worksheet page 1 (Q3 counts beads in groups). Click through. Think-aloud: "Every group has exactly 1 blue bead, so counting blue beads counts the groups. 5 groups. Each group has 3 green: 3, 6, 9, 12, 15. Each group has 4 beads: 4, 8, 12, 16, 20." '
 'Ask: "Why did it matter that the string ends with green beads?" (So the last group is complete; if it stopped right after a blue bead, the last group would have no green.)'))
RB={'R':(RED,'R',WHITE),'B':(BLUE,'B',WHITE),'Y':(YEL,'Y',NAVY)}
body=h2('Your turn: red, red, blue, yellow')+pin(128,230,1664,beads('RRBYRRBY',RB,'Beads: red, red, blue, yellow, repeated'))
for i,(a,b,c) in enumerate([('a','What colour is bead 12?','yellow'),('b','What colour is bead 15?','blue'),('c','Where is the 3rd blue bead?','bead 11')]):
    body+=qrow(128,390+i*150,1250,a,b,40)+answer(1420,390+i*150,372,c)
put('p2l4-try1',sec('p2l4-try1','27–30 MIN',body,'Whiteboards, then click. The group is 4 beads: groups end with yellow at 4, 8, 12, 16. a) 12 ends a group: yellow. b) 12 ends a group; 13 red, 14 red, 15 blue. c) Blue is 3rd in each group: 3, 7, 11, so bead 11. Ask: "Which table helped?" (the 4 times table).'))
put('p2l4-key',sec('p2l4-key','30–32 MIN',h2('Key idea: count in groups')+card(p('Find the group size. The groups end at the times-table numbers. Jump to the end of a group, then count on.',44,700))+card(p('Growing pattern? Make a table, find the rule, then keep going.',38,600,MUTED)),
 'Say the key idea together. Common mistakes to watch for during the worksheet: (1) Saying a times-table place (like 20 for a group of 5) is the FIRST shape of a group, when it is the LAST. (2) Counting the whole pattern one by one instead of jumping to the end of a group. (3) Growing patterns: multiplying by the step and forgetting the start (10 squares: 10 × 3 = 30, forgetting the extra stick).'))
put('p2l4-break',break_slide('p2l4-break','32–36 MIN','Brain break','Pattern moves! Jump, jump, squat, jump, jump, squat … Keep going to 15 moves. Before you start: what will move 15 be?','Then: a drink of water and back to our seats.','Four minutes. Take predictions first. Move 15 is a squat (15 is in the 3 times table, so it ends a group). Online: children move in view of the camera.'))

# ---------- 5. worksheet page 1 ----------
put('p2l4-ws1',ws_preview('p2l4-ws1','36–50 MIN','Worksheet page 1: with your partner',[('Q1','The shape pattern. Draw a line after each group of 5.'),('Q2','M, A, T, H. Where do the groups end?'),('Q3','The bead string. Count the groups first.')],'Mark the end of each group. Use the times table to jump ahead.','Minutes 36 to 50. Walk around. Ask "How long is one group? Where does each group end?" before giving any help.'))
put('p2l4-ws1ans',check_slide('p2l4-ws1ans','50–52 MIN','Page 1: check together',[('Q1','a) square   b) circle   c) triangle'),('Q2','a) A   b) place 40   c) 7 Ts'),('Q3','18 yellow beads,  30 beads altogether')],
 'Click each answer after a pair explains. Q1: 20 ends a group (square); 23 is the 3rd shape (circle); 40 ends a group, so 41 is the 1st shape (triangle); (the circles in the first 30 shapes is Think harder 1: 6 groups with 2 circles each). Q2: 16 ends a group, so 18 is the 2nd letter, A; every H ends a group, the 10th at 4 × 10 = 40; Ts are at 3, 7, 11, 15, 19, 23, 27, and 29, 30 are M, A. Q3: 12 red is 6 groups; 6 × 3 = 18 yellow; 6 × 5 = 30 beads.'))

# ---------- 6. teaching before page 2 ----------
W7=[190,110,110,110,110,110]
body=h2('Pattern machine: a times table')+pin(128,240,1664,p('Each stool has 3 legs.',40,700),None,WHITE,20,'18px 28px')
body+=trow(128,360,['Stools','1','2','3','4','5'],W7,None,True)+trow(128,450,['Legs','3','6','9','12','15'],W7,'rise')
body+=step(1,'The rule: 3 legs for every stool. Legs = stools × 3.',top=570,size=36)
body+=step(2,'10 stools: 10 × 3 = 30 legs.',top=680,size=36)
body+=answer(128,790,1664,'24 legs? Count in 3s to 24: 8 stools.')
put('p2l4-teachtimes',sec('p2l4-teachtimes','52–54 MIN',body,'Teach before worksheet page 2 (Q4, flower petals). Click: the legs row, the rule, going forwards, going backwards. Think-aloud: "Each stool adds 3 legs, so the table is the 3 times table. To go forwards I multiply: 10 × 3 = 30. To go backwards from 24 legs I count in 3s until I reach 24: 3, 6, 9 … 24 is 8 threes, so 8 stools." '
 'Ask: "What about 20 legs?" (6 stools use 18, and 2 legs are left over: not enough for another stool.)'))
def squares(n,x0,s=80):
    g=''
    for i in range(n+1): g+=f'<line x1="{x0+i*s}" y1="30" x2="{x0+i*s}" y2="{30+s}" stroke="{BROWN}" stroke-width="12" stroke-linecap="round"/>'
    for i in range(n): g+=f'<line x1="{x0+i*s}" y1="30" x2="{x0+(i+1)*s}" y2="30" stroke="{BROWN}" stroke-width="12" stroke-linecap="round"/><line x1="{x0+i*s}" y1="{30+s}" x2="{x0+(i+1)*s}" y2="{30+s}" stroke="{BROWN}" stroke-width="12" stroke-linecap="round"/>'
    return g+T(x0+n*s/2,160,f'{n} square{"s" if n>1 else ""}: {3*n+1} sticks',30,TEAL)
g=squares(1,130)+squares(2,470)+squares(3,880)
W8=[190,90,90,90,90,90,90]
body=h2('Growing pattern: find the rule')+pin(128,230,1664,svgwrap('Squares made of sticks in a row: 1 square uses 4 sticks, 2 squares use 7, 3 squares use 10',1200,180,g,1200,180))
body+=trow(128,440,['Squares','1','2','3','4','5','6'],W8,None,True)+trow(128,530,['Sticks','4','7','10','13','16','19'],W8,'rise')
body+=pin(1330,440,462,p('+3 each time: a new square shares one side.',32,700),'fade',SOFT,20,'18px 24px')
body+=step(1,'Keep adding 3: 22, 25, 28, 31. 10 squares need 31 sticks.',top=650,size=36)
body+=answer(128,770,1664,'22 sticks? 4, 7, 10, 13, 16, 19, 22: 7 squares.')
put('p2l4-teachgrow',sec('p2l4-teachgrow','54–55 MIN',body,'Teach before worksheet page 2 (Q5, tables and chairs). Build the squares with lolly sticks. Ask: "How many more sticks for the next square? Why not 4?" (it shares a side with the square before). Click: the sticks row, the note, the step, the answer. '
 'Think-aloud: "I make a table. 4, 7, 10: it goes up by 3 each time. I keep adding 3 to reach 10 squares: 31. To go backwards from 22 sticks, I keep adding 3 until I reach 22 and read the squares: 7." Watch for: 10 × 3 = 30 or 10 × 4 = 40. Point at the first square: it needs 4, not 3.'))
body=h2('In both patterns: make two lists')+pin(128,240,1664,p('Ali counts in 2s. Mei counts in 5s. Which numbers up to 30 do they BOTH say?',38,700),None,WHITE,20,'18px 28px')
body+=pin(128,380,1664,p('Ali:  2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30',38,600),'rise',WHITE,20,'18px 28px')
body+=pin(128,490,1664,p('Mei:  5, 10, 15, 20, 25, 30',38,600),'rise',WHITE,20,'18px 28px')
body+=answer(128,610,1664,'Both say: 10, 20, 30')
body+=pin(128,730,1664,p('They go up by 10 each time: they are in the 2 AND the 5 times tables.',34,700),'fade',SOFT,20,'18px 28px')
put('p2l4-teachboth',sec('p2l4-teachboth','55–56 MIN',body,'Teach before worksheet page 2 (Q6 uses 3s and 4s). Click: Ali\'s list, Mei\'s list, the answer, the note. Children circle the numbers that appear in both lists. Say: "MAKE A LIST: write both counts in order, then look for the numbers in both." Ask: "What would the next one after 30 be?" (40).'))
put('p2l4-try2',try_slide('p2l4-try2','56–57 MIN','Your turn: pattern machines','Make a table or a list. Then click to check.',[('a','Each car has 4 wheels. How many wheels on 7 cars?','28'),('b','Squares of sticks: 4, 7, 10 … How many sticks for 8 squares?','25'),('c','Counting in 2s and in 3s: which numbers up to 20 are in both?','6, 12, 18')],
 'Minutes 56 to 57. Whiteboards. a) 4, 8, 12, 16, 20, 24, 28. b) 4, 7, 10, 13, 16, 19, 22, 25. c) 2s: 2, 4, 6 … 20; 3s: 3, 6, 9, 12, 15, 18; both: 6, 12, 18.',size=36))

# ---------- 7. worksheet page 2 ----------
put('p2l4-ws2',ws_preview('p2l4-ws2','57–69 MIN','Worksheet page 2: on your own',[('Q4','Flower petals: a times-table pattern. Forwards and backwards.'),('Q5','Tables and chairs: fill in the table, find the rule.'),('Q6','Counting in 3s and 4s: make two lists.')],'Finished early? Stretch and Challenge come next.','Children work alone. Note who needs a short catch-up next lesson. For Q5 ask: "How many more children when you add a table? Why?"'))
put('p2l4-ws2ans',check_slide('p2l4-ws2ans','69–72 MIN','Page 2: check together',[('Q4','5, 10, 15, 20, 25, 30.  50 petals.  7 flowers.  4 flowers, 3 left'),('Q5','4, 6, 8, 10, 12, 14.   22 children.   9 tables'),('Q6','Both say 12, 24, 36.  They go up by 12.')],
 'Click each answer after a child explains. Q4: 23 petals: 4 flowers use 20, 3 petals left over. Q5: the rule is add 2: each new table adds 1 child on top and 1 below, and the 2 end seats stay; 10 tables seat 22; 9 tables seat 20. Q6: Ali 3, 6, 9 … 36 (12 numbers); Mei 4, 8 … 36 (9 numbers); both 12, 24, 36.'))

# ---------- 8. stretch and challenge ----------
st=[('1.','A pattern goes 1, 2, 3, 1, 2, 3 … What is the total of the first 15 numbers?'),('2.','Ben’s pattern is 2, 5, 8, 11 … Will 30 be in his pattern? Explain.'),('3.','Square, circle, circle, square, circle, circle … Mei draws 20 shapes. How many squares?')]
put('p2l4-stretch',sec('p2l4-stretch','For early finishers',h2('Stretch')+numbered_cards(st,38),
 'Answers: 1) 30 (5 groups, each adds up to 6). 2) No: 2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, it jumps from 29 to 32 (every number is 1 less than a 3 times table number). 3) 7 squares, in places 1, 4, 7, 10, 13, 16, 19 (18 shapes is 6 groups, then place 19 starts a 7th group with a square).'))
ch=[('1.','Siti builds towers of cubes. Tower 1 has 2 cubes, tower 2 has 5 cubes, tower 3 has 8 cubes. They keep growing in the same way. Which tower has 29 cubes? Is there a tower with exactly 50 cubes? With exactly 100 cubes?'),('2.','Frog A starts at 0 and jumps 4 each time. Frog B starts at 2 and jumps 3 each time. Which numbers up to 30 do both frogs land on?')]
put('p2l4-challenge',sec('p2l4-challenge','Challenge',h2('Challenge')+numbered_cards(ch,38),'Pairs try first, then use the "see it" slide if stuck, then the walk-through. These are Q6 and Q7 on the Think Harder page. Answers: 1) Tower 10 has 29 cubes. Tower 17 has 50 cubes (3 × 17 − 1). No tower has 100, because every tower is 1 less than a 3 times table number and 101 is not in the 3 times table. 2) 8 and 20.'))
g1=''
for k,(n,col) in enumerate([(2,YEL),(5,SKY),(8,'#F2A7A7')]):
    x=40+k*170
    g1+=''.join(cube(x,330-(j+1)*36,36,col) for j in range(n))+T(x+18,366,f'tower {k+1}',26,TEAL)
g1+=T(560,190,'…',44)+f'<rect x="620" y="60" width="110" height="270" rx="10" fill="{WHITE}" stroke="{NAVY}" stroke-width="4" stroke-dasharray="12 8"/>'+T(675,180,'29',40)+T(675,220,'cubes',26)+T(675,366,'tower ?',26,TEAL)
g2=f'<line x1="30" y1="230" x2="730" y2="230" stroke="{NAVY}" stroke-width="4"/>'
for v in range(31):
    x=30+v*700/30; g2+=f'<line x1="{x:.1f}" y1="{220 if v%5 else 210}" x2="{x:.1f}" y2="240" stroke="{NAVY}" stroke-width="3"/>'
    if v%5==0: g2+=T(round(x),280,str(v),28)
xa=lambda v:30+v*700/30
g2+=f'<path d="M{xa(0):.0f} 210 Q{xa(2):.0f} 90 {xa(4):.0f} 210" fill="none" stroke="{TEAL}" stroke-width="5"/>'+T(round(xa(0)),130,'A: +4',28,TEAL,anchor='start')
g2+=f'<circle cx="{xa(2):.0f}" cy="230" r="10" fill="{RED}" stroke="{NAVY}" stroke-width="3"/><path d="M{xa(2):.0f} 220 Q{xa(3.5):.0f} 150 {xa(5):.0f} 216" fill="none" stroke="{RED}" stroke-width="5" stroke-dasharray="10 6"/>'+T(round(xa(5))+16,170,'B: +3',28,RED,anchor='start')
g2+=T(380,50,'A starts at 0, B starts at 2',28)
body=h2('Challenge: see it',60)+'<div style="display:flex;gap:32px;align-items:flex-start">'+card(f'<p style="font-size:28px;font-weight:700;color:{TEAL}">Q1: Growing towers</p>'+svgwrap('Towers of 2, 5 and 8 cubes, and a mystery tower with 29 cubes',760,390,g1,760,390),extra='flex:1;min-width:0;padding:20px 24px')+card(f'<p style="font-size:28px;font-weight:700;color:{TEAL}">Q2: Two frogs</p>'+svgwrap('Number line 0 to 30. Frog A jumps 4 from 0. Frog B starts at 2 and jumps 3',760,390,g2,760,390),extra='flex:1;min-width:0;padding:20px 24px')+'</div>'
put('p2l4-chdiag',sec('p2l4-chdiag','Challenge',body,'Show after pairs have tried the Challenge, or if they are stuck. The pictures show the problem, not the answer. Ask: What do you notice? How many more cubes in each new tower? Where does each frog land after its first jump? Could you make a table or two lists?'))
body=h2('Challenge: walk-through')+pin(128,250,800,p('Q1: make a table, add 3',38,800,TEAL))
for i,t in enumerate(['Towers 1 to 5:  2, 5, 8, 11, 14','Towers 6 to 10:  17, 20, 23, 26, 29','Tower 10 has 29 cubes ✓']): body+=pin(128,330+i*110,800,p(t,34),'rise',WHITE)
body+=pin(992,250,800,p('Q2: make two lists',38,800,TEAL))
for i,t in enumerate(['A:  4, 8, 12, 16, 20, 24, 28','B:  5, 8, 11, 14, 17, 20, 23, 26, 29','Both: 8 and 20 ✓']): body+=pin(992,330+i*110,800,p(t,34),'rise',WHITE)
put('p2l4-chwalk',sec('p2l4-chwalk','Challenge',body,'Use after pairs have tried. Q1: each tower has 3 more cubes than the one before; keep the table going until 29. A strong child may notice each tower is 1 less than the 3 times table (tower 10: 30 − 1 = 29), which answers the extra questions: 50 + 1 = 51 is in the 3 times table (17 × 3), so tower 17 has 50 cubes; 100 + 1 = 101 is not (99 and 102 are), so no tower has 100. '
 'Q2: list each frog\'s landings in order up to 30 and circle the numbers in both lists. The next shared number would be 32 (they meet every 12 steps: 8, 20, 32).'))
put('p2l4-talk',talk_slide('p2l4-talk','72–80 MIN','A pattern repeats every 5 shapes. Is the 10th shape always the same as the 20th? What if it repeats every 3 shapes?','Minutes 72 to 80. Pairs talk for 2 minutes, then share. Answer: Every 5: yes, 10 and 20 are both in the 5 times table, so both are the LAST shape of a group. Every 3: no. 9 ends a group, so 10 is the 1st shape; 18 ends a group, so 20 is the 2nd shape. Praise the reasons, not only the answers.'))
put('p2l4-exit',exit_slide('p2l4-exit','80–90 MIN','The pattern goes triangle, circle, square, triangle, circle, square … What is the 17th shape? How do you know?','Minutes 80 to 90. Answer: a circle. 15 ends a group (5 groups of 3), so 16 is a triangle and 17 is a circle. Extension: make your own repeating pattern of 4 shapes and write 3 far-place questions about it for a partner, with the answers.'))

p2gaps.add(S,4); ORDER[:]=p2gaps.order(ORDER,4)
# ---------- write ----------
if os.path.isdir(os.path.join(D,'slides')): shutil.rmtree(os.path.join(D,'slides'))
os.makedirs(os.path.join(D,'slides'))
for i,h in S.items(): open(os.path.join(D,'slides',i+'.html'),'w').write(h)
deck={'v':4,'createdOnFiles':{'v':1,'at':datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')},'lists':'css',
      'title':'Math Inquirers P2: Lesson 4 – Pattern Machines','order':ORDER,'cover':'p2l4-title',
      'sections':{'s1':{'description':'Warm-up and explore','start':'p2l4-title'},'s2':{'description':'Teach: far places by counting in groups','start':'p2l4-teach1'},'s3':{'description':'Worksheet with teaching before each page','start':'p2l4-break'},'s4':{'description':'Think harder, go further, talk and exit','start':'p2l4-stretch'}},
      'faces':{'fredoka':{'family':'Fredoka','href':'https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&display=swap'},'nunito-sans':{'family':'Nunito Sans','href':'https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@400;600;700&display=swap'}},
      'designSystems':[]}
json.dump(deck,open(os.path.join(D,'deck.json'),'w'),indent=1,ensure_ascii=False)
print(len(ORDER),'slides')
