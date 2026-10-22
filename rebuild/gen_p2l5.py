"""Math Inquirers P2, Lesson 5: Mystery Number Machines. Writes split/p2l5/project (deck.json + slides/*.html)."""
import json,os,sys
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,H)
from slidekit import *
import p2gaps
N=5; P=f'p2l{N}'
D=os.path.join(H,'..','split',P,'project'); os.makedirs(os.path.join(D,'slides'),exist_ok=True)
S={}
def put(i,h): S[i]=h

# ---------- local helpers (title, game, explore, break, talk, exit, challenge) ----------
def title_slide(sid,week,title,topic,today,notes):
    return (f'<section id="{sid}" data-transition="fade" style="background:{NAVY};color:{CREAM};font-family:{BF};padding:128px 128px 160px;display:flex;flex-direction:column;justify-content:center;gap:36px">\n'
            f'<p style="font-size:32px;font-weight:700;letter-spacing:4px;color:{YEL}">P2  •  LESSON {N}  •  WEEK {week}</p>\n'
            f'<h1 style="font-family:{HF};font-size:120px;font-weight:600;line-height:1.05">{E(title)}</h1>\n'
            f'<p style="font-size:44px;color:#C9D4EC">{E(topic)}</p>\n'
            f'<div style="background:#26385F;border-radius:24px;padding:40px;display:flex;flex-direction:column;gap:12px"><p style="font-size:28px;font-weight:700;letter-spacing:3px;color:{YEL}">TODAY WE WILL</p><p style="font-size:44px;font-weight:600">{E(today)}</p></div>\n'
            f'<p style="position:absolute;left:128px;bottom:64px;width:1400px;font-size:24px;color:#B7C3DD">{E(FOOT)}</p>\n<aside>{E(notes)}</aside>\n</section>\n')
def break_slide(sid,text,notes):
    return (f'<section id="{sid}" data-transition="fade" style="background:{TEAL};color:{CREAM};font-family:{BF};padding:128px 128px 160px;display:flex;flex-direction:column;justify-content:center;gap:36px">\n'
            f'<p style="font-size:32px;font-weight:700;letter-spacing:4px;color:{YEL}">32–36 MIN</p>\n<h2 style="font-family:{HF};font-size:110px;font-weight:600;line-height:1.05">Brain break</h2>\n'
            f'<p style="font-size:48px;font-weight:600">{E(text)}</p>\n<p style="font-size:36px;color:#D7EFEA">Then: a drink of water and back to our seats.</p>\n'
            f'<p style="position:absolute;left:128px;bottom:64px;width:1400px;font-size:24px;color:#D7EFEA">{E(FOOT)}</p>\n<aside>{E(notes)}</aside>\n</section>\n')
def qcards(items,size=38):
    return ''.join(card(p(f'<span style="color:{TEAL}">{a}</span>  {E(b)}',size,600,raw=True)) for a,b in items)
STARTERS=card(p('Sentence starters:',34,400,MUTED)+p('“I noticed that …”   “I tested it by …”   “I know because …”',38))
def talk_slide(sid,q,notes):
    return sec(sid,'72–80 MIN',h2('Talk time')+card(chip('TALK TIME',YEL,NAVY)+p(q,42))+STARTERS,notes)
def exit_slide(sid,q,notes):
    return sec(sid,'80–90 MIN',h2('Exit ticket')+card(chip('EXIT TICKET')+p(q,46))+card(p('Write your answer on a slip of paper. Show it to your tutor. Then collect your stamp in your inquiry journal.',34,400)),notes)
def explore1(sid,steps,pic,notes):
    lis=''.join(f'<li>{E(s)}</li>' for s in steps)
    body=h2('Explore: what to do')+card(chip('EXPLORE')+f'<ol style="font-size:34px;font-weight:600;padding-left:48px;margin:0;display:flex;flex-direction:column;gap:8px;line-height:1.3">{lis}</ol>',extra='padding:24px 40px')+card(pic,extra='padding:16px 24px;align-items:center')
    return sec(sid,'8–14 MIN',body,notes)

# ---------- bar model drawing ----------
def bars(rows,w=1664,rowh=70,gap=22,unit=14,x0=230,aria='bar model'):
    """rows: list of (label, [(text, units, fill)], right_text)"""
    h=len(rows)*(rowh+gap)
    s=f'<svg aria-label="{E(aria)}" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="width:{w}px;height:{h}px">'
    for r,(lab,segs,right) in enumerate(rows):
        y=r*(rowh+gap)+4; x=x0
        s+=f'<text x="0" y="{y+rowh/2+12}" font-size="34" font-weight="800" fill="{NAVY}" font-family="Nunito Sans, Arial">{E(lab)}</text>'
        for t,u,f in segs:
            ww=u*unit
            dash=' stroke-dasharray="12 8"' if f=='none' else ''
            s+=f'<rect x="{x}" y="{y}" width="{ww}" height="{rowh}" rx="6" fill="{WHITE if f=="none" else f}" stroke="{NAVY}" stroke-width="4"{dash}/>'
            if t: s+=f'<text x="{x+ww/2}" y="{y+rowh/2+11}" font-size="30" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="Fredoka, Arial">{E(t)}</text>'
            x+=ww
        if right: s+=f'<text x="{x+24}" y="{y+rowh/2+12}" font-size="34" font-weight="800" fill="{TEAL}" font-family="Nunito Sans, Arial">{E(right)}</text>'
    return s+'</svg>'
GREEN='#D3F1E4'

# 1 title
put(f'{P}-title',title_slide(f'{P}-title',3,'Mystery Number Machines','Working Backwards',
 'Find mystery numbers in two-step machines with + − × ÷ by working backwards, and draw before-and-after bars for stories.',
 'Objective: Find a mystery number in two-step puzzles with +, −, × and ÷ by working backwards (undo the LAST step first with the opposite operation), check by going forwards, and use before-and-after bar models for stories where an amount changes. '
 'Materials: mini whiteboards, counters, paper cups, number machine cards (× 2, × 3, × 4, × 5, × 10, and + or − cards from 1 to 20), paper strips for bars. '
 'Online: machine cards are shown on the slides; children write on whiteboards and hold them up; for bars they draw on paper or fold a paper strip into equal parts. '
 'Time plan: warm-up 0 to 8, explore 8 to 20 (explore2 talk is 6 minutes), teaching 20 to 32 (click to reveal each step and answer), brain break 32 to 36, short teaching 36 to 38, worksheet page 1 38 to 50 then check together 50 to 52, short teaching 52 to 57, worksheet page 2 57 to 69 then check together 69 to 72, talk time 72 to 80, exit ticket 80 to 90. '
 'Level: × and ÷ only with the 2, 3, 4, 5 and 10 tables; all numbers within 1000.'))

# 2 warm1 game
body=h2('Warm-up: Guess my machine')+card(chip('WARM-UP GAME',YEL,NAVY)+p('I am a secret machine. Call out a number to put IN. I tell you what comes OUT. Can you guess what I do?',42))+card(machine([('4','q'),('?','op'),('12','res')],w=1100)+p('IN 4, OUT 12. Is it + 8? Or × 3? Test another number!',34,600,MUTED),extra='align-items:flex-start')
put(f'{P}-warm1',sec(f'{P}-warm1','0–5 MIN',body,'Minutes 0 to 5. You are the machine. Three rounds only (about 2.5 minutes): two rounds of IN to OUT guesses, then one OUT to IN round. Pick a secret one-step rule (start with × 3). Children call IN numbers; you say the OUT. After two or three, ask for a guess. Point at the picture: IN 4, OUT 12 could be + 8 OR × 3, so test another IN (5 gives 15 for × 3 but 13 for + 8). '
 'Good rules to use: × 3, + 15, × 10, ÷ 2 (only give even IN numbers), − 20, × 5. Round three is the flip: give only an OUT ("My machine is × 5. OUT is 35. What went IN?" 7). Listen for children who already "do the opposite".'))

# 3 warm2
qs=[('1.','I think of a number. I multiply it by 2. I get 18.','9'),('2.','I think of a number. I take away 25. I get 40.','65')]   # questions 1 and 3 of the guide table; 2, 4 and 5 are spare
body=h2('Quick questions')+''.join(qrow(128,250+i*125,1250,a,b,36) for i,(a,b,c) in enumerate(qs))+''.join(answer(1420,250+i*125,372,c) for i,(a,b,c) in enumerate(qs))
put(f'{P}-warm2',sec(f'{P}-warm2','5–8 MIN',body,'Minutes 5 to 8. Read each one aloud, give thinking time, whiteboards up, then click for the answer. Ask "How did you find it?" each time. 1) 18 ÷ 2 = 9. 2) 40 + 25 = 65. Spare questions in the guide table: I divide by 5 and get 4 (20); the opposite of × 4 is ÷ 4; I multiply by 3, then add 4, and get 19 (5: 19 − 4 = 15, 15 ÷ 3 = 5; do not teach it yet, see who tries 19 ÷ 3 first, that is today’s big idea).'))

# 4 explore1
pic=machine([('?','q'),('× 2','op'),('+ 6','op'),('20','res')],back='go back to find the start',w=1300)
put(f'{P}-explore1',explore1(f'{P}-explore1',['Pick one × card and one + or − card. Put them in a row: that is your machine.','Secretly choose a start number. Run it through both cards. Say only the OUT.','Your partner works backwards to find your start number. Check it together.'],pic,
 'Minutes 8 to 14. Pairs build a two-step machine from the cards (one × card from × 2, × 3, × 4, × 5, × 10, and one + or − card). Partner A chooses a start number (keep it from 1 to 10) and says only the OUT. Partner B works backwards, then they check by going forwards. Partners swap roles every round, so each child both chooses the secret number and works backwards (never one child always being the solver). (Swapping the order of the two cards is dropped from the explore: the teachorder slide and worksheet Q5 ask exactly that.) '
 'Online: the tutor runs the machine on the slide and children work back on whiteboards; then pairs in breakout rooms make their own.'))

# 5 explore2
put(f'{P}-explore2',sec(f'{P}-explore2','14–20 MIN',h2('Explore: talk about it')+qcards([('1.','How did you find your partner’s start number?'),('2.','What is the opposite of × 3? Of − 8?')],40),
 'Minutes 14 to 20. Let pairs keep working, then gather them. Answers: 1) Undo the LAST card first with its opposite, then undo the first card. 2) ÷ 3 undoes × 3; + 8 undoes − 8. (Does the order of the cards matter? That is the teachorder slide and worksheet Q5, not asked here.) Ask a pair whose machine could not be undone with a whole number (for example ÷ 3 first, then OUT 7 with + 2: 5 is not in the 3 table) to share: what went wrong?'))

# 6 teach1
body=h2('Opposites undo each other')+'<div style="display:flex;gap:32px">'+card(p('+ 6  and  − 6',48,700)+p('Add 6, then take away 6: back where you started.',32,600,MUTED),extra='flex:1')+card(p('× 4  and  ÷ 4',48,700)+p('4 groups of 5 is 20. 20 shared into 4 groups is 5.',32,600,MUTED),extra='flex:1')+'</div>'
body+=pin(128,520,1000,machine([('?','q'),('× 4','op'),('20','res')],back='go back:  ÷ 4',w=1000))+answer(1180,560,612,'20 ÷ 4 = 5.  Check: 5 × 4 = 20 ✓')
put(f'{P}-teach1',sec(f'{P}-teach1','20–22 MIN',body,'Teach. Show 4 groups of 5 counters: "× 4 made 20." Now share the 20 back into 4 groups: 5 in each. "÷ 4 undid × 4." Do the same with + 6 and − 6. Think-aloud for the machine: "Something times 4 is 20. To go backwards I do the opposite of × 4, which is ÷ 4. 20 ÷ 4 = 5. Check: 5 × 4 = 20." Click for the answer.'))

# 7 we1 two steps
body=h2('Worked example: two steps')+card(p('I think of a number. I multiply it by 3, then add 4. I get 25.',42,700))
body+=pin(128,370,1664,machine([('?','q'),('× 3','op'),('+ 4','op'),('25','res')],w=1664))
body+=step(1,'Start at the end. The LAST step was + 4. Undo it:  25 − 4 = 21',top=530,size=36)
body+=step(2,'Then undo × 3:  21 ÷ 3 = 7',top=640,size=36)
body+=step(3,'Check forwards:  7 × 3 = 21,  21 + 4 = 25 ✓   My number is 7.',top=750,size=36)
put(f'{P}-we1',sec(f'{P}-we1','22–26 MIN',body,'Click to reveal each step; ask the group to predict it first. Analogy: "In the morning you put on socks, then shoes. At night you take off the shoes first." The last step done is the first step undone. Watch for children who do 25 ÷ 3 first: it does not even give a whole number, which is a clue they went the wrong way.'))

# 8 try1
put(f'{P}-try1',try_slide(f'{P}-try1','26–28 MIN','Your turn: whiteboards','Find what went IN. Undo the last step first, then check forwards.',[('a','? → × 2 → − 5 → 15','10')],
 'Whiteboards up together, then click. One item: 15 + 5 = 20, 20 ÷ 2 = 10. Ask for the rule in words: "undo the last step first". (Items b and c are dropped: worksheet Q1 has the same types.)',size=40))

# 9 we2 before-and-after bars
U=14
body=h2('Before and after: draw the bars')+card(p('Ben had some stamps. He gave 18 to Mei. Then he bought 25 more. Now he has 60. How many stamps did he have at first?',38,700))
body+=pin(128,640,1664,bars([('Now',[('35',35,SKY),('25 bought',25,YEL)],'60')],unit=U,x0=260,aria='Now: 60 stamps, made of 35 and the 25 he bought'),'rise')
body+=pin(128,530,1664,bars([('After giving',[('35',35,SKY)],'60 − 25 = 35')],unit=U,x0=260,aria='Before buying: 35 stamps'),'rise')
body+=pin(128,420,1664,bars([('At first',[('35',35,SKY),('18 given',18,GREEN)],'35 + 18 = 53')],unit=U,x0=260,aria='At first: 35 and the 18 he gave away'),'rise')
body+=answer(128,760,1664,'He had 53 stamps. Check: 53 − 18 = 35,  35 + 25 = 60 ✓')
put(f'{P}-we2',sec(f'{P}-we2','28–30 MIN',body,'Click 1: the "Now" bar (bottom): 60 is the stamps he had before buying, plus the 25 he bought. Click 2: before buying he had 60 − 25 = 35. Click 3: before giving 18 away he had 35 + 18 = 53. Click 4: check forwards. '
 'Say: "We read the story forwards but we solve it backwards, from the bottom bar up." The bars stop children from adding 18 and 25 to 60 without thinking.'))

# 10 try2
put(f'{P}-try2',try_slide(f'{P}-try2','30–31 MIN','Your turn: before and after','Start from what is there now. Undo each change.',[('a','Ali lost 12 cards. Now he has 30. How many at first?','42'),('b','Siti had $40. She spent some, then got $15. Now she has $35. How much did she spend?','$20')],
 'Whiteboards. a) 30 + 12 = 42. b) Before the $15: 35 − 15 = $20. She went from $40 to $20, so she spent $20. Two items only: the bus item is dropped.',size=34))

# 11 key
body=h2('Key idea: undo it backwards')+card(p('Start at the end. Undo the LAST step first with its opposite, then the step before. Check by going forwards.',44,700))+card(p('Opposites:  + and −  undo each other.  × and ÷  undo each other.',38,600,MUTED))
put(f'{P}-key',sec(f'{P}-key','31–32 MIN',body,'Say the key idea together. Common mistakes to watch for during the worksheet: (1) Doing the same step again instead of the opposite (27 × 2 instead of 27 ÷ 2). (2) Undoing in the wrong order: the first step first. (3) Bar stories: stopping at one part (one bag, one half) instead of the whole, or forgetting to undo one of the changes.'))

# 12 break
put(f'{P}-break',break_slide(f'{P}-break','Machine moves. The tutor writes a number and calls a machine: “3, times 2, jumps!” Everyone does the OUT number of jumps (6). Then “+ 4 claps!”','Four minutes. Online: children stay in view of the camera and move in place. Keep the OUT numbers small (under 15).'))

# 13 teachrule
W3=[400,520,580]
body=h2('Find a two-step rule: guess and test')+card(p('A machine does  × a number,  then  + a number.   IN 1 gives OUT 7.   IN 4 gives OUT 13.',38,700))
body+=trow(128,390,['Guess','Make IN 1 give 7','Test IN 4: is it 13?'],W3,None,True,32)
gs=[['× 2, then + 5','1 × 2 + 5 = 7','4 × 2 + 5 = 13  yes'],['× 3, then + 4','1 × 3 + 4 = 7','4 × 3 + 4 = 16  not this one'],['× 4, then + 3','1 × 4 + 3 = 7','4 × 4 + 3 = 19  not this one']]
for i,r in enumerate(gs): body+=trow(128,475+i*85,r,W3,'rise',size=32)
body+=pin(128,750,1664,p('Only  × 2, then + 5  works for BOTH pairs. Always test a second pair!',36,700),'fade',SOFT,20,'18px 28px')
put(f'{P}-teachrule',sec(f'{P}-teachrule','36–38 MIN',body,'Teach before worksheet page 1 (Think harder 1 asks for a rule like this). Think-aloud: "I guess the × part first. If it is × 2, then IN 1 makes 2, and I need + 5 to reach 7. Now I test it on the other pair: 4 × 2 = 8, 8 + 5 = 13. Yes!" Then show that × 3 and × 4 also give 7 for IN 1 but fail the test. '
 'Point out: with IN 1 every guess works, so the second pair is what tells them apart. Do not tell them the worksheet rule.'))

# 14 ws1
put(f'{P}-ws1',ws_preview(f'{P}-ws1','38–50 MIN','Worksheet page 1: with your partner',[('Q1','Mystery machines (part d is a ★ take-home star). Undo the last step first. Write the IN in the yellow box.'),('Q2','Two-step machine tables: fill in the OUT or the IN.')],'Check every answer by going forwards through the machine.','Minutes 38 to 50. Walk around. Ask "What was the last step? What is its opposite?" before giving any help. Q1(d) (× 4, then − 15) is marked ★ take-home on the page: children do it at home. For Q2a the last two columns need going backwards. For Q2b suggest a table of guesses like the one on the last slide.'))

# 15 ws1ans
put(f'{P}-ws1ans',check_slide(f'{P}-ws1ans','50–52 MIN','Page 1: check together',[('Q1','a) 10    b) 16    c) 24    ★ take-home: d) 9'),('Q2a','IN 4 → OUT 14.  IN 10 → OUT 32.  OUT 17 ← IN 5.  OUT 29 ← IN 9.'),('Q2b','× 2, then + 1:  IN 3, 5, 10, 20 → OUT 7, 11, 21, 41')],
 'Click after a pair explains (answer lines only). Q1(d) is a take-home star: the answer stays here for children to mark at home. Q1: a) 27 − 7 = 20, 20 ÷ 2 = 10. b) 40 ÷ 5 = 8, 8 + 8 = 16. c) 20 − 12 = 8, 8 × 3 = 24. d) 21 + 15 = 36, 36 ÷ 4 = 9. Q2a: 4 × 3 + 2 = 14, 10 × 3 + 2 = 32; 17 − 2 = 15, 15 ÷ 3 = 5; 29 − 2 = 27, 27 ÷ 3 = 9. '
 'Q2b: 3 × 2 + 1 = 7, 5 × 2 + 1 = 11, 10 × 2 + 1 = 21, 20 × 2 + 1 = 41. (Finding a hidden rule from a table is Think harder 1.)',lw=220))

# 16 teachparts (halves)
half=500; u5=round(half*5/14)
svg=(f'<svg aria-label="A bar for all of Mei’s beads cut into two halves; the second half is cut into 5 used and 9 left" viewBox="0 0 1664 190" xmlns="http://www.w3.org/2000/svg" style="width:1664px;height:190px">'
     f'<path d="M200 54 v-14 H{200+2*half} v14" fill="none" stroke="{NAVY}" stroke-width="4"/><text x="{200+half}" y="28" font-size="32" font-weight="800" text-anchor="middle" fill="{NAVY}" font-family="Nunito Sans, Arial">all her beads: ?</text>'
     f'<rect x="200" y="64" width="{half}" height="80" rx="6" fill="{GREEN}" stroke="{NAVY}" stroke-width="4"/><text x="{200+half/2}" y="116" font-size="32" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="Fredoka, Arial">half to her friend</text>'
     f'<rect x="{200+half}" y="64" width="{u5}" height="80" rx="6" fill="{YEL}" stroke="{NAVY}" stroke-width="4"/><text x="{200+half+u5/2}" y="116" font-size="32" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="Fredoka, Arial">used 5</text>'
     f'<rect x="{200+half+u5}" y="64" width="{half-u5}" height="80" rx="6" fill="{SKY}" stroke="{NAVY}" stroke-width="4"/><text x="{200+half+u5+(half-u5)/2}" y="116" font-size="32" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="Fredoka, Arial">left 9</text>'
     f'<text x="{200+half}" y="182" font-size="28" font-weight="700" text-anchor="middle" fill="{TEAL}" font-family="Nunito Sans, Arial">the two halves are the same length</text></svg>')
body=h2('Equal parts: one part tells you the rest')+card(p('Mei had some beads. She gave half of them to her friend. Then she used 5 beads to make a ring. She has 9 beads left. How many beads did she have at first?',36,700))
body+=pin(128,410,1664,svg)
body+=step(1,'The half Mei kept is the part she used and the part left:  5 + 9 = 14',top=620,size=34)
body+=step(2,'The two halves are equal, so the other half is also 14.',top=715,size=34)
body+=step(3,'All her beads:  14 + 14 = 28.  Check: half of 28 is 14,  14 − 5 = 9 ✓',top=810,size=34)
put(f'{P}-teachparts',sec(f'{P}-teachparts','52–55 MIN',body,'Teach before worksheet page 2 (Q4 uses 3 equal bags instead of 2 halves; do not do Q4 for them). Fold a paper strip in half to show the two equal parts, then fold one half again unevenly for "used" and "left". Common mistake: answering 14 (one half) instead of 28. Ask: "Is 14 ALL her beads, or one part?"'))

# 17 teachorder
body=h2('Does the order matter?')+card(p('Put 2 into each machine. Do they give the same OUT?',40,700))
body+=pin(128,360,1000,machine([('2','q'),('+ 6','op'),('× 3','op'),('?','res')],w=1000))+pin(128,510,1000,machine([('2','q'),('× 3','op'),('+ 6','op'),('?','res')],w=1000))
body+=answer(1180,370,612,'A:  2 + 6 = 8,  8 × 3 = 24')+answer(1180,520,612,'B:  2 × 3 = 6,  6 + 6 = 12')
body+=step(1,'Not the same! The order matters.',top=670,size=34)
body+=step(2,'What must go into B to give 24?  Go backwards:  24 − 6 = 18,  18 ÷ 3 = 6',top=770,size=34)
put(f'{P}-teachorder',sec(f'{P}-teachorder','55–57 MIN',body,'Teach before worksheet page 2 (Q5). The top machine is A, the bottom one is B. Children predict first, then click for each OUT. Then step 1 and step 2. Check step 2 forwards: 6 × 3 = 18, 18 + 6 = 24. Link to the explore: "Remember swapping your two cards?"'))

# 18 teachthree
bsvg=bars([('Tom',[('?',20,SKY)],''),('Mei',[('?',20,SKY),('3',10,YEL)],''),('Ravi',[('?',20,SKY),('4',13,YEL)],'25 altogether')],unit=15,rowh=58,gap=14,aria='Three bars: Tom, Mei is Tom and 3 more, Ravi is Tom and 4 more, 25 altogether')
body=h2('Three children: take away the extras')+card(p('Tom, Mei and Ravi have 25 stickers altogether. Mei has 3 more than Tom. Ravi has 4 more than Tom. How many does each child have?',36,700))
body+=pin(128,400,1664,bsvg)
body+=step(1,'Take away the extras:  25 − 3 − 4 = 18',top=630,size=32)
body+=step(2,'Now there are 3 equal bars:  18 ÷ 3 = 6.  Tom has 6.',top=722,size=32)
body+=step(3,'Mei  6 + 3 = 9,   Ravi  6 + 4 = 10.   Check:  6 + 9 + 10 = 25 ✓',top=814,size=32)
put(f'{P}-teachthree',sec(f'{P}-teachthree','For early finishers',body,'Teach for Think Harder 4 (three children and 40 marbles), after page 2 is checked. Draw Tom’s bar first: the other two are "Tom’s bar and a bit more". Cover the yellow extras with your hand: "If nobody had the extras, there would be 25 − 3 − 4 = 18, in three equal bars." Then give the extras back. Common mistake: 25 ÷ 3 straight away (it does not even work).'))

# 19 ws2
put(f'{P}-ws2',ws_preview(f'{P}-ws2','57–69 MIN','Worksheet page 2: on your own',[('Q3','Stickers: fill in the two ? bars. Start from what Siti has now.'),('Q4','Sweets in 3 equal bags. Use the bar: one bag first.'),('Q5','Mei’s and Ali’s machines. Does the order matter?'),('Think Harder','Finished early? Try Think Harder 4: three children and 40 marbles. Take away the extras first.')],'Finished early? Stretch and Challenge come next.','Children work alone. Note who needs a short catch-up next lesson. Check that every child draws bars for Q3 and Q4. Q6 (three children, 40 marbles) is now Think Harder 4 for early finishers; the slide before the Stretch slide teaches the method.'))

# 20 ws2ans
put(f'{P}-ws2ans',check_slide(f'{P}-ws2ans','69–72 MIN','Page 2: check together',[('Q3','59 stickers  (50 − 15 = 35,  35 + 24 = 59)'),('Q4','30 sweets  (one bag 6 + 4 = 10,  3 bags 30)'),('Q5','a) 18   b) 14   c) No, the order matters   d) 7')],
 'Click after a child explains. Q3 check: 59 − 24 = 35, 35 + 15 = 50. Q4: one bag had 10 before 4 were taken out; 10 + 10 + 10 = 30. Q5: Mei (5 + 4) × 2 = 18; Ali 5 × 2 + 4 = 14; for Ali to get 18: 18 − 4 = 14, 14 ÷ 2 = 7.'))

# 21 stretch (new items, not on the worksheet)
st=[('1.','? → + 7 → × 2 → 30.  What went IN?'),('2.','Mei had some stamps. She gave half to Ali, then 3 to Ben. She has 5 left. How many did she have at first?'),('3.','Ben, Ravi and Tom have 31 cards. Ravi has 2 more than Ben. Tom has 5 more than Ben. How many does each have?')]
put(f'{P}-stretch',sec(f'{P}-stretch','For early finishers',h2('Stretch')+qcards(st,36),'For children who finish early. Answers: 1) 8 (30 ÷ 2 = 15, 15 − 7 = 8; check 8 + 7 = 15, 15 × 2 = 30). 2) 16 (5 + 3 = 8 is the half she kept, 8 + 8 = 16; check: half of 16 is 8, 8 − 3 = 5). 3) Ben 8, Ravi 10, Tom 13 (31 − 2 − 5 = 24, 24 ÷ 3 = 8; check 8 + 10 + 13 = 31).'))

# 22 challenge
ch=[('1.','A machine does × 2, then − 4. Ravi puts a number in, then puts the OUT straight back in again. The final OUT is 12. What number did he put in first?'),('2.','Ben gives Ali 5 marbles. Now they both have 20 marbles. How many marbles did each boy have before? How many MORE did Ben have than Ali at first? Why is it not 5?')]
put(f'{P}-challenge',sec(f'{P}-challenge','Challenge',h2('Challenge')+qcards(ch,38),'Pairs try first, then use the "see it" slide if stuck, then the walk-through. Ask for the reason every time. Answers: 1) 6 (go back twice: 12 + 4 = 16, 16 ÷ 2 = 8; 8 + 4 = 12, 12 ÷ 2 = 6; check 6 → 8 → 12). 2) Ben 25, Ali 15 (give the 5 back: Ben 20 + 5, Ali 20 − 5). Ben had 10 more than Ali, not 5, because Ben lost 5 AND Ali gained 5. Extension: if Ben had given 8 and they ended equal, he had 16 more at first (the gap is double the number given). Common wrong answer for 2: "both had 20" or "Ben 25, Ali 20", or "5 more".'))

# 23 chdiag
m1=machine([('A','q'),('× 2','op'),('− 4','op'),('B','res')],w=760).replace('width:760px;height:130px','width:100%;height:auto')
m2=machine([('B','q'),('× 2','op'),('− 4','op'),('12','res')],w=760).replace('width:760px;height:130px','width:100%;height:auto')
q1='<p style="font-size:28px;font-weight:700;color:#1F7A6F">Q1: Twice through the machine</p>'+m1+p('The OUT goes back IN:',30,700,MUTED)+m2
bw=320
q2s=(f'<svg aria-label="Before: Ben and Ali have unknown numbers of marbles; Ben gives Ali 5. After: both bars are 20." viewBox="0 0 760 470" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto">'
     f'<text x="0" y="36" font-size="30" font-weight="800" fill="{TEAL}" font-family="Nunito Sans, Arial">Before</text>'
     f'<text x="0" y="98" font-size="30" font-weight="800" fill="{NAVY}" font-family="Nunito Sans, Arial">Ben</text><rect x="110" y="60" width="{bw+40}" height="60" rx="6" fill="{WHITE}" stroke="{NAVY}" stroke-width="4" stroke-dasharray="12 8"/><text x="{110+(bw+40)/2}" y="101" font-size="32" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="Fredoka, Arial">?</text>'
     f'<text x="0" y="178" font-size="30" font-weight="800" fill="{NAVY}" font-family="Nunito Sans, Arial">Ali</text><rect x="110" y="140" width="{bw-40}" height="60" rx="6" fill="{WHITE}" stroke="{NAVY}" stroke-width="4" stroke-dasharray="12 8"/><text x="{110+(bw-40)/2}" y="181" font-size="32" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="Fredoka, Arial">?</text>'
     f'<path d="M520 90 Q600 130 520 170" fill="none" stroke="{TEAL}" stroke-width="5"/><polygon points="520,170 540,152 544,176" fill="{TEAL}"/><text x="610" y="140" font-size="30" font-weight="800" fill="{TEAL}" font-family="Nunito Sans, Arial">gives 5</text>'
     f'<text x="0" y="276" font-size="30" font-weight="800" fill="{TEAL}" font-family="Nunito Sans, Arial">After</text>'
     f'<text x="0" y="338" font-size="30" font-weight="800" fill="{NAVY}" font-family="Nunito Sans, Arial">Ben</text><rect x="110" y="300" width="{bw}" height="60" rx="6" fill="{SKY}" stroke="{NAVY}" stroke-width="4"/><text x="{110+bw/2}" y="341" font-size="32" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="Fredoka, Arial">20</text>'
     f'<text x="0" y="418" font-size="30" font-weight="800" fill="{NAVY}" font-family="Nunito Sans, Arial">Ali</text><rect x="110" y="380" width="{bw}" height="60" rx="6" fill="{SKY}" stroke="{NAVY}" stroke-width="4"/><text x="{110+bw/2}" y="421" font-size="32" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="Fredoka, Arial">20</text></svg>')
q2='<p style="font-size:28px;font-weight:700;color:#1F7A6F">Q2: Before and after</p>'+q2s
body=h2('Challenge: see it',60)+'<div style="display:flex;gap:32px;align-items:flex-start">'+card(q1,extra='flex:1;min-width:0;padding:20px 24px')+card(q2,extra='flex:1;min-width:0;padding:20px 24px')+'</div>'
put(f'{P}-chdiag',sec(f'{P}-chdiag','Challenge',body,'Show after pairs have tried, or if they are stuck. The pictures show the problem, not the answer. Ask: What do you notice? What do we know? Where do we start? (At the end: the 12, and the two bars of 20.) Which bar was longer before? How do you know?'))

# 24 chwalk
body=h2('Challenge: walk-through')+pin(128,250,800,p('Q1: go back through twice',38,800,TEAL))
for i,t in enumerate(['Second time: 12 + 4 = 16,  16 ÷ 2 = 8','First time: 8 + 4 = 12,  12 ÷ 2 = 6','Check: 6 × 2 − 4 = 8,  8 × 2 − 4 = 12 ✓']): body+=pin(128,330+i*110,800,p(t,32),'rise',WHITE)
body+=pin(992,250,800,p('Q2: undo the give',38,800,TEAL))
for i,t in enumerate(['After: Ben 20, Ali 20.','Undo it: Ben gets his 5 back: 20 + 5 = 25','Ali gives the 5 back: 20 − 5 = 15','Ben had 25 − 15 = 10 more, not 5 ✓']): body+=pin(992,330+i*110,800,p(t,32),'rise',WHITE)
put(f'{P}-chwalk',sec(f'{P}-chwalk','Challenge',body,'Use after pairs have tried. Q1: the machine runs twice, so we undo it twice, starting from the final OUT; the number in the middle is 8. Q2: the last thing that happened was "Ben gives 5", so we undo it: Ben takes 5 back and Ali gives 5 back. Ask: "Why is the difference 10 and not 5?" (Ben lost 5 AND Ali gained 5.)'))

# 25 talk, 26 exit
put(f'{P}-talk',talk_slide(f'{P}-talk','To undo “× 2, then + 6” with OUT 20, Mei takes away 6 first. Ali divides by 2 first. Who is right?','Minutes 72 to 80. Pairs talk for 90 seconds, then two volunteers share. Make them test both ways. Answer: Mei is right: 20 − 6 = 14, 14 ÷ 2 = 7, and 7 × 2 + 6 = 20. Ali gets 20 ÷ 2 = 10, 10 − 6 = 4, but 4 × 2 + 6 = 14, not 20. The last step happened last, so it is undone first. Praise the reasons, not only the answers.'))
put(f'{P}-exit',exit_slide(f'{P}-exit','I think of a number. I multiply it by 4, then take away 6. I get 14. What is my number?','Minutes 80 to 90. Answer: 5 (14 + 6 = 20, 20 ÷ 4 = 5; check 5 × 4 = 20, 20 − 6 = 14). Extension: make a three-step machine with a × card, a ÷ card and a + card for a partner.'))

order=['title','warm1','warm2','explore1','explore2','teach1','we1','try1','we2','try2','key','break','teachrule','ws1','ws1ans','teachparts','teachorder','ws2','ws2ans','teachthree','stretch','challenge','chdiag','chwalk','talk','exit']
order=[f'{P}-{x}' for x in order]
p2gaps.add(S,5); order=p2gaps.order(order,5)
assert set(order)==set(S), set(order)^set(S)
for f in os.listdir(os.path.join(D,'slides')):
    if f.endswith('.html') and f[:-5] not in S: os.remove(os.path.join(D,'slides',f))
for i,h in S.items(): open(os.path.join(D,'slides',i+'.html'),'w').write(h)
deck={'v':4,'createdOnFiles':{'v':1,'at':'2026-10-21T08:00:00Z'},'lists':'css','title':f'Math Inquirers P2: Lesson {N} – Mystery Number Machines','order':order,'cover':order[0],
 'sections':{'s1':{'description':'Warm-up and explore','start':f'{P}-title'},'s2':{'description':'Teach: undo it backwards, and before-and-after bars','start':f'{P}-teach1'},'s3':{'description':'Worksheet with teaching before each page','start':f'{P}-break'},'s4':{'description':'Think harder, go further, talk and exit','start':f'{P}-stretch'}},
 'faces':{'fredoka':{'family':'Fredoka','href':'https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&display=swap'},'nunito-sans':{'family':'Nunito Sans','href':'https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@400;600;700&display=swap'}},'designSystems':[]}
json.dump(deck,open(os.path.join(D,'deck.json'),'w'),indent=1,ensure_ascii=False)
print(len(order),'slides')
