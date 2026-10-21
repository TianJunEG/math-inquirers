"""Math Inquirers P5, Lesson 7: Percentage Puzzles. Writes split/p5l7/project (deck.json + slides/*.html)."""
import json,os,sys,datetime
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,H)
import slidekit
from slidekit import *
slidekit.FOOT='Math Inquirers P5 Holiday Program  •  Notice it. Test it. Explain why.'
D=os.path.join(H,'..','split','p5l7','project'); os.makedirs(os.path.join(D,'slides'),exist_ok=True)
S={}
def put(i,h): S[i]=h
RED='#D64545'; FOOTX=slidekit.FOOT

# ---------- shared shapes ----------
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
def rect(x,y,w,h,fill=WHITE,stroke=NAVY,sw=4,rx=0): return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'
def soft(left,top,width,text,size=34,build='fade'): return pin(left,top,width,p(text,size,700),build,SOFT,20,'18px 28px')

def hundred(n,size=400):
    c=size/10; rows,rem=divmod(n,10)
    g=''
    if rows: g+=f'<rect x="0" y="0" width="{size}" height="{rows*c}" fill="{YEL}"/>'
    if rem: g+=f'<rect x="0" y="{rows*c}" width="{rem*c}" height="{c}" fill="{YEL}"/>'
    d=''.join(f'M{i*c:g} 0 V{size} M0 {i*c:g} H{size} ' for i in range(1,10))
    g+=f'<path d="{d}" stroke="{NAVY}" stroke-width="1.5" opacity=".5" fill="none"/><rect x="0" y="0" width="{size}" height="{size}" fill="none" stroke="{NAVY}" stroke-width="5"/>'
    return svgwrap(size+10,size+10,f'A 10 by 10 square with {n} small squares shaded',f'<g transform="translate(5 5)">{g}</g>')
def bar(x,y,w,h,parts,fills=None,labels=None,sw=4,size=34,lab_y=None):
    """a bar cut into equal parts; fills: dict index->colour; labels: dict index->text"""
    pw=w/parts; g=''
    for i in range(parts):
        g+=rect(x+i*pw,y,pw,h,(fills or {}).get(i,WHITE),NAVY,sw)
        if labels and i in labels: g+=txt(x+i*pw+pw/2,y+h/2+size*0.35,labels[i],size)
    return g

# ---------- 1. title ----------
put('p5l7-title',title_slide('p5l7-title','LESSON 7  •  WEEK 4A','Percentage Puzzles','Percentage: discounts, GST, increase and decrease',
 'Build any percentage from 10%, 5% and 1%, work out discounts and GST, and catch the percentage traps.',
 'Objective: Find any percentage of an amount by building it from 10%, 5% and 1%; work out a discount and then 9% GST on the sale price; find a percentage of a remainder; spot the classic percentage traps. Preview of P6 (Think Harder page only): find a percentage increase or decrease by comparing the change with the ORIGINAL amount. '
 'Thinking strategies taught today: ASK "PERCENTAGE OF WHAT?", BUILD FROM 10%, 5% AND 1%, and DRAW A BAR MODEL. GST in Singapore is 9%. '
 'Materials: mini whiteboard and marker, workbook, pencil, a hundred-square page or squared paper. A calculator only for checking at the end of each page. '
 'Online: children keep the workbook and a whiteboard in front of the camera. The tutor screen-shares the slides and draws bar models with the annotation tool. '
 'Time plan: warm-up 0 to 9, explore 9 to 21, teaching 21 to 33 (click to reveal each step and answer), brain break 33 to 37, worksheet page 1 37 to 49, check together 49 to 51, short teaching before page 2 51 to 57, worksheet page 2 57 to 72 (alone), check together 72 to 76, talk time 76 to 82, exit ticket 82 to 90. Stretch and challenge are for children who finish early, or for home.'))

# ---------- 2. warm-up game ----------
cols=[(30,'30% shaded'),(45,'45% shaded'),(64,'64% shaded')]
body=h2('Warm-up: Hundred-Square Snap')+card(p('Each big square has 100 small squares. Write the percentage SHADED and the percentage NOT shaded. Whiteboards up together!',36,700),extra='padding:24px 40px')
for i,(n,lab) in enumerate(cols):
    L=128+i*580
    body+=pin(L,380,420,hundred(n,400),None,WHITE,20,'4px 4px')
    body+=pin(L,820,500,p(f'{n}% shaded,  {100-n}% not shaded',32,800),'pop',YEL,20,'14px 18px')
put('p5l7-warm1',sec('p5l7-warm1','0–4 MIN',body,
 'Minutes 0 to 4. Hundred-Square Snap. Show the three squares one at a time (cover the other two with your hand or paper online). Children write on whiteboards: the percentage shaded and the percentage NOT shaded, then hold them up together. Click to show the answers. '
 'Square 1: 30 shaded (3 full rows) so 30% shaded, 70% not shaded. Square 2: 45 shaded (4 rows and 5 more) so 45% and 55%. Square 3: 64 shaded (6 rows and 4 more) so 64% and 36%. '
 'Ask: "Who found the not-shaded part without counting? How?" (100 take away the shaded part.) "Why is the whole 100?" (percent means out of 100). '
 'Listen for: children counting every small square. Praise rows of 10: each row is 10%.'))

# ---------- 3. quick questions ----------
qs=[('1.','50% of $90','$45'),('2.','10% of 350','35'),('3.','25% of 48','12'),('4.','1% of $700','$7'),('5.','3 out of 20 as a percentage','15%')]
body=h2('Quick questions')+''.join(qrow(128,250+i*125,1250,a,b) for i,(a,b,c) in enumerate(qs))+''.join(answer(1420,250+i*125,372,c) for i,(a,b,c) in enumerate(qs))
put('p5l7-warm2',sec('p5l7-warm2','4–9 MIN',body,'Minutes 4 to 9. Read each aloud, whiteboards up together, then click to show. Ask "How did you do it?" each time. 1) 50% is half: $45. 2) 10% is one tenth: 350 ÷ 10 = 35. 3) 25% is a quarter: 48 ÷ 4 = 12. 4) 1% is one hundredth: $700 ÷ 100 = $7. 5) 3 out of 20: multiply top and bottom by 5 to get 15 out of 100, so 15%. Answers: $45, 35, 12, $7, 15%.'))

# ---------- 4. explore: what to do ----------
def tag(x,y,txt_,fill=YEL):
    return (f'<polygon points="{x},{y+60} {x+36},{y} {x+230},{y} {x+230},{y+120} {x+36},{y+120}" fill="{fill}" stroke="{NAVY}" stroke-width="4" stroke-linejoin="round"/>'
            f'<circle cx="{x+36}" cy="{y+60}" r="9" fill="{WHITE}" stroke="{NAVY}" stroke-width="3"/>'+txt(x+138,y+78,txt_,54))
def arrow(x1,x2,y,label):
    return (f'<line x1="{x1}" y1="{y}" x2="{x2-22}" y2="{y}" stroke="{NAVY}" stroke-width="6"/><polygon points="{x2},{y} {x2-26},{y-14} {x2-26},{y+14}" fill="{NAVY}"/>'+txt((x1+x2)/2,y-22,label,44,TEAL))
g=tag(20,20,'$200')+arrow(280,600,80,'up 10%')+tag(640,20,'?',SKY)+arrow(900,1220,80,'down 10%')+tag(1260,20,'?',SKY)
steps=''.join(f'<li>{E(s)}</li>' for s in ['A bicycle costs $200. Predict: if the price goes UP 10% and then DOWN 10%, is it back to $200?','Work it out. Up 10% first. Then take 10% of the NEW price off.','Try the other way round: down 10% first, then up 10%.','Compare both answers with your prediction. What do you notice?'])
body=h2('Explore: up 10%, down 10%')+card(chip('EXPLORE')+f'<ol style="font-size:36px;font-weight:600;padding-left:52px;display:flex;flex-direction:column;gap:8px">{steps}</ol>')
body+=card(svgwrap(1540,160,'A 200 dollar price tag, an arrow up 10 percent to a tag with a question mark, then an arrow down 10 percent to another tag with a question mark',g),extra='padding:20px 32px')
put('p5l7-explore1',sec('p5l7-explore1','9–14 MIN',body,'Minutes 9 to 14. Pairs predict first (thumbs: back to $200, less, or more?) and write the prediction. Then they work it out on whiteboards. Most children predict $200. Let them find out for themselves. Early finishers: try up 50% then down 50% on $80. Is the gap bigger or smaller than with 10%?'))

# ---------- 5. explore: talk ----------
body=h2('Explore: talk about it')+numcards([('1.','Is the price back to $200? What is it?'),('2.','Does it matter which change comes first?'),('3.','Why is the answer not $200? Which amount did you take 10% of, each time?')],40)
put('p5l7-explore2',sec('p5l7-explore2','14–21 MIN',body,'Minutes 14 to 21. Let pairs share, then draw both routes on the board. Answers: 1) No. $200, up 10% is $220 (10% of $200 = $20). Down 10% of $220 is $22 off, so $198. 2) No: down first gives $200 − $20 = $180, then up 10% is $18 more = $198. Same answer. 3) The two 10%s are of different amounts: $20 added, but $22 taken off, because the second 10% is of the NEW price. That is why it is $2 less. '
 'Write on the board: "Percentage of WHAT?" This question is the heart of the lesson. After a change, the new price is the new whole. Do NOT teach the method for the worksheet yet: the next slides do that.'))

# ---------- 6. teach: 10, 5, 1 ----------
g=bar(10,10,1640,76,10,{},{i:'10%' for i in range(10)},4,34)
g+=f'<path d="M10 100 V112 H1650 V100" fill="none" stroke="{NAVY}" stroke-width="3"/>'+txt(830,150,'the whole = 100%  (10 equal parts, 10% each)',32,TEAL,'middle',700,'Nunito Sans, Arial')
body=h2('Build any percentage from 10%, 5% and 1%')+pin(128,250,1664,svgwrap(1660,168,'A bar cut into 10 equal parts, each part 10 percent, making the whole 100 percent',g),None,WHITE,20,'8px 0px')
for i,(a,b) in enumerate([('10%','divide by 10'),('5%','half of 10%'),('1%','divide by 100')]):
    L=128+i*568
    body+=pin(L,460,480,p(a,60,800,TEAL)+p(b,38,700),None,WHITE,20,'18px 28px')
ex=[('10% of $80 = $8','80 ÷ 10'),('5% of $80 = $4','half of $8'),('1% of $80 = $0.80','80 ÷ 100')]
for i,(a,b) in enumerate(ex):
    L=128+i*568
    body+=pin(L,670,480,p(a,36,800),'rise',YEL,20,'16px 24px')
body+=soft(128,790,1664,'Percent means "out of 100", so 1% is one of the 100 equal parts.',34,'fade')
put('p5l7-teach1',sec('p5l7-teach1','21–23 MIN',body,'Teach. Point to the bar: "100% is the whole thing. Cut it into 10 equal parts: each part is 10%." Then the three tools. Click to show each example with $80 (a different amount from the worksheet): 10% of $80 = $8; 5% is half of that, $4; 1% is $80 ÷ 100 = $0.80. '
 'Ask: "How can we make 15% from these?" (10% + 5% = $8 + $4 = $12.) "35%?" (3 × 10% + 5%.) Think-aloud: "I never learn a new rule for each percentage. I build it from 10%, 5% and 1%." '
 'Money check: 1% of $80 is 80 cents, so write $0.80, not $0.08.'))

# ---------- 7. worked example ----------
body=h2('Worked example: 45% and 98% of $60')+card(p('Find 45% of $60 and 98% of $60. Build them from 10%, 5% and 1%.',38,700),extra='padding:24px 40px')
body+=step(1,'10% of $60 = $6  (÷ 10).      5% = half of $6 = $3.',top=370,size=34)
body+=step(2,'45% = 4 × 10% + 5% = $24 + $3 = $27.',top=480,size=34)
body+=step(3,'98% is almost all of it. Find what is missing: 100% − 98% = 2%.  1% = $0.60, so 2% = $1.20.',top=590,size=34)
body+=step(4,'98% = $60 − $1.20 = $58.80.',top=700,size=34)
body+=answer(128,810,1664,'45% of $60 = $27.     98% of $60 = $58.80.')
put('p5l7-we1',sec('p5l7-we1','23–26 MIN',body,'Click to reveal each step and let children say the step first. Think-aloud: "10% is one tenth: $6. 5% is half of 10%: $3. 45% is four 10%s and one 5%: four sixes are 24, add 3: $27." Then: "For 98% I could add lots of pieces, but 98% is only 2% away from the whole. I take the 2% off: 1% is 60 cents, so 2% is $1.20. $60 take away $1.20 is $58.80." '
 'Check: 45% + 55% should make $60: 55% of $60 is $33, and $27 + $33 = $60. Ask: "When is take-away the clever way?" (when the percentage is close to 100%).'))
put('p5l7-try1',try_slide('p5l7-try1','26–27 MIN','Your turn: build it','Use 10%, 5% and 1%. Whiteboards up, then click.',[('a','20% of $70','$14'),('b','35% of $200','$70'),('c','99% of $300','$297')],
 'Whiteboards. a) 10% = $7, so 20% = $14. b) 10% = $20, 5% = $10: 30% + 5% = $60 + $10 = $70. c) 99% = 100% − 1% = $300 − $3 = $297. Ask: "Which one used take-away? Why was it a good idea?"'))

# ---------- 9. worked example: discount then GST ----------
body=h2('Discount first, then GST')+card(p('A fan costs $120 before GST. It is sold at 15% off. Then 9% GST is added to the SALE price. What do you pay?',36,700),extra='padding:24px 40px')
body+=pin(128,350,1664,machine([('$120','q'),('15% off','op'),('$102','res'),('9% GST','op'),('$111.18','res')],None,1664,130),None)
body+=step(1,'15% of $120 = $12 + $6 = $18.   Sale price = $120 − $18 = $102.',top=520,size=32)
body+=step(2,'GST is 9% of the SALE price $102.   10% = $10.20,  1% = $1.02.   9% = $10.20 − $1.02 = $9.18.',top=620,size=32)
body+=step(3,'Pay = $102 + $9.18 = $111.18.',top=720,size=32)
body+=answer(128,810,1664,'GST = $9.18.     You pay $111.18.')
put('p5l7-we2',sec('p5l7-we2','27–30 MIN',body,'Click to reveal each step. Ask first: "What do we take the 9% of: $120 or $102?" (the price after the discount: that is what the shop charges for the fan). Step 1: 10% of $120 is $12, 5% is $6, so 15% is $18; $102 is the sale price. Step 2: 10% of $102 is $10.20; 1% is $1.02; 9% is 10% take away 1%: $9.18. Step 3: add. '
 'Think-aloud: "GST in Singapore is 9%. It is added to what you actually pay for the thing, so I work it out on the sale price." Check by estimating: 9% is a bit less than 10% of $102 = $10.20. $9.18 is a bit less. Sensible. '
 'The machine picture shows the chain: price, discount, sale price, GST, final price.'))
put('p5l7-try2',try_slide('p5l7-try2','30–32 MIN','Your turn: discounts and GST','Use 10%, 5% and 1%. Click to check.',[('a','An $80 shirt is 25% off. Sale price?','$60'),('b','How much is the 9% GST on a $200 bill?','$18'),('c','$50 shoes: 10% off, then 9% GST. You pay?','$49.05')],
 'Whiteboards. a) 25% is a quarter: $20 off, $60. b) 10% of $200 = $20, 1% = $2, so 9% = $18. c) 10% of $50 = $5 off, sale price $45. GST: 10% of $45 = $4.50, 1% = $0.45, so 9% = $4.05. Pay $45 + $4.05 = $49.05. Watch for children who work out GST on $50 instead of $45.',size=36))

# ---------- 11. key ----------
body=h2('Key idea: percentage of WHAT?')+card(p('Build any percentage from 10%, 5% and 1%. Before every step, ask: percentage of what?',44,700))+card(p('Take the discount off first, then work out GST on the sale price. After a change, the new amount is the new whole.',38,600,MUTED))
put('p5l7-key',sec('p5l7-key','32–33 MIN',body,'Say the key idea together. Common mistakes to watch for during the worksheet: (1) Adding percentages of different wholes: 20% of the money and then 25% of the REMAINDER is not 45% of the money. (2) Thinking that up 25% and then down 25% brings the price back to the start. (3) Working out a percentage increase or decrease using the new amount instead of the ORIGINAL amount, or working out GST on the price before the discount.'))
put('p5l7-break',break_slide('p5l7-break','33–37 MIN','Percent stretch. The tutor calls a percentage: 100% is standing tall with arms up, 50% is hands on your head, 25% is hands on your knees, 0% is sitting down. What does 75% look like?','Five minutes. Online: children show the position on camera. Let children call the next percentage. Ask: "What percentage is half way between 50% and 100%?" (75%: hands on shoulders). Then a drink of water.'))

# ---------- worksheet page 1 ----------
put('p5l7-ws1',ws_preview('p5l7-ws1','37–49 MIN','Worksheet page 1: with your partner',[('Q1','Build percentages of $240 from 10%, 5% and 1%. Fill in the table.'),('Q2','Two shops, one rice cooker: 20% off and 9% GST, or a plain price. Which is cheaper?'),('Q3','Up 25%, then down 20%. Is it the same as up 5%?')],'Stuck? Write the whole at the start of each step, and ask: percentage of what?','Minutes 37 to 49. Walk around. Ask "Percentage of what?" before giving any help. Q1: check the boxes you already have before working out 35%. Q2 is the longest: shop A needs discount, then GST on the SALE price. Q3c: do not accept "yes" without working out the final price.'))
put('p5l7-ws1ans',checks('p5l7-ws1ans','49–51 MIN','Page 1: check together',[('Q1','10% $24,  5% $12,  1% $2.40,  15% $36,  35% $84,  99% $237.60'),('Q2','a) $128   b) $11.52   c) $139.52   d) Shop A, by 48¢'),('Q3','a) $100   b) $80   c) No: it is $80, not $84. The 20% is of $100, not of $80.')],
 'Click after a pair explains theirs. Q1: 35% = 3 × $24 + $12 = $84. 99% = $240 − $2.40 = $237.60. Q2a: 20% of $160 = $32, sale $128. Q2b: 10% of $128 = $12.80, 1% = $1.28, 9% = $11.52. Q2c: $128 + $11.52 = $139.52. Shop B is $140, so Shop A is 48¢ cheaper. Q3: $80 + $20 = $100 after the 25% rise; 20% of $100 is $20, so back to $80. The second percentage is of the new whole.',gapy=170))

# ---------- teach: percentage of a remainder ----------
g=bar(10,10,1640,90,4,{0:YEL},{0:'spent',1:'$20',2:'$20',3:'$20'},4,36)
g+=f'<path d="M10 120 V132 H1650 V120" fill="none" stroke="{NAVY}" stroke-width="3"/>'+txt(830,170,'Ali had $80: 4 equal parts of $20 (25% each)',32,TEAL,'middle',700,'Nunito Sans, Arial')
body=h2('Percentage of the REMAINDER')+card(p('Ali had $80. He spent 25% of it. Then he spent 40% of the money LEFT. How much is left at the end? What percentage of $80 is that?',34,700),extra='padding:22px 40px')
body+=pin(128,370,1664,svgwrap(1660,190,'A bar of 80 dollars cut into 4 equal parts of 20 dollars, the first part spent',g),None,WHITE,20,'8px 0px')
body+=step(1,'25% of $80 = $20 spent.  Left: $60.   The NEW whole is $60.',top=590,size=32)
body+=step(2,'40% of $60: 10% = $6, so 40% = $24.   Left: $60 − $24 = $36.',top=690,size=32)
body+=step(3,'$36 out of $80 = 45 out of 100.   Do NOT add 25% and 40%!',top=790,size=32)
put('p5l7-teachrem',sec('p5l7-teachrem','51–54 MIN',body,'Teach before worksheet page 2 (Q4 has a remainder). Draw the bar of $80 in 4 equal parts: each part is $20, which is 25%. Click 1: one part spent, $60 left, and that $60 is the NEW whole. Click 2: the 40% is of $60, not of $80. 10% of $60 is $6, so 40% is $24. $36 is left. '
 'Click 3: the trap. 25% + 40% = 65% suggests 35% is left, which would be $28. Wrong. The real fraction left is $36 out of $80: 36 ÷ 80 = 0.45, so 45%. Ask: "Why can we not add 25% and 40%?" (they are percentages of different wholes: $80 and $60). Check: spent $20 + $24 = $44, which is 55% of $80, and 55% + 45% = 100%.'))

# ---------- teach: percentage change ----------
g=rect(10,10,500,70,YEL,NAVY,4)+txt(260,58,'$15',40)+rect(10,110,1000,70,SKY,NAVY,4)+txt(510,158,'$30',40)
g+=f'<path d="M520 112 V150" stroke="{TEAL}" stroke-width="0"/>'+rect(510,10,500,70,WHITE,TEAL,4).replace('fill="#FFFFFF"','fill="none"').replace(f'stroke="{TEAL}"',f'stroke="{TEAL}" stroke-dasharray="12 8"')+txt(760,58,'+ $15',38,TEAL)
body=h2('Percentage change: compare with the ORIGINAL')+card(p('A ticket costs $15. The price DOUBLES to $30. Then it goes back from $30 to $15. Find each percentage change.',34,700),extra='padding:22px 40px')
body+=pin(128,370,1664,svgwrap(1030,190,'Two bars: a 15 dollar bar, and a 30 dollar bar that is the first bar plus another 15 dollars',g),None,WHITE,20,'8px 20px')
body+=step(1,'Up: the change is $15. The ORIGINAL price is $15.  $15 out of $15 = 100% increase.',top=590,size=32)
body+=step(2,'Down: the change is $15. The ORIGINAL price is now $30.  $15 out of $30 = 50% decrease.',top=690,size=32)
body+=soft(128,795,1664,'Same $15 change, different percentages: each is compared with the amount you START from.',32,'fade')
put('p5l7-teachchange',sec('p5l7-teachchange','Think Harder: P6 preview',body,'Use this after worksheet page 2, for children who go on to the Think Harder page (Q1), or at home. Percentage change is a P6 skill, so say so: it is a preview, and the Percentage change = change out of the amount you START with line is all a child needs. Draw the two bars: $15 and $30. Click 1: the rise is $15, the starting price is $15, so $15 out of $15 is the whole thing again: 100% increase (doubling is a 100% increase, not 200%). Click 2: the fall is $15, but now the starting price is $30. $15 out of $30 is half: 50%. '
 'Say in words: "The percentage change is the change out of the STARTING amount." Ask: "Why are the two percentages not the same, when both changes are $15?" (the starting amount is different each time).'))

# ---------- teach: table for groups ----------
W=[430,260,260,340]
body=h2('Groups in a class: make a table')+card(p('50 pupils. 40% are boys. 30% of the boys and 10% of the girls have a bicycle. What percentage of the class have a bicycle?',34,700),extra='padding:22px 40px')
body+=trow(128,372,['','Boys','Girls','Whole class'],W,None,True,34)
body+=trow(128,462,['Number of pupils','20','30','50'],W,'rise',False,34)
body+=trow(128,552,['Have a bicycle','6','3','9'],W,'rise',False,34)
body+=step(1,'Boys: 40% of 50 = 20.   Girls: 50 − 20 = 30.',top=640,size=32)
body+=step(2,'Bicycles: 30% of 20 = 6,   10% of 30 = 3,   6 + 3 = 9.',top=730,size=32)
body+=answer(128,820,1664,'9 out of 50 = 18 out of 100 = 18%')
put('p5l7-teachtable',sec('p5l7-teachtable','54–57 MIN',body,'Teach before worksheet page 2 (Q5 has a table for a class). Fill the table row by row, click by click. Boys: 40% of 50: 10% is 5, so 40% is 20. Girls: the rest, 30. Bicycles: boys 30% of 20 = 6 (10% is 2, so 30% is 6); girls 10% of 30 = 3. Whole class: 6 + 3 = 9. Tip for the table: fill in the easy parts first. Last step: 9 out of 50. To turn it into a percentage: multiply top and bottom by 2 to get 18 out of 100. Ask: "Why can we not just add 30% and 10%?" (they are percentages of different groups: 20 boys and 30 girls).'))

# ---------- teach: compare deals ----------
body=h2('Which deal is better? Work out the real price')+card(p('Pens cost $10 each. Deal A: buy 2, get 1 free. Deal B: 30% off every pen. You want 3 pens.',34,700),extra='padding:22px 40px')
body+=pin(128,350,810,p('Deal A: buy 2, get 1 free',40,800,TEAL)+p('Pay for 2 pens:  2 × $10 = $20',36,600),None,WHITE,20,'20px 28px')
body+=pin(982,350,810,p('Deal B: 30% off',40,800,TEAL)+p('3 pens = $30.  30% of $30 = $9 off.  Pay $21',36,600),'rise',WHITE,20,'20px 28px')
body+=step(1,'Compare the two prices: $20 and $21. Deal A is cheaper, by $1.',top=560,size=34)
body+=step(2,'Deal A is really how many percent off?  $10 free out of $30 = about 33% off.',top=670,size=34)
body+=soft(128,790,1664,'Work out the real price for each deal, then compare. Do not just compare the numbers on the signs!',32,'fade')
put('p5l7-teachdeal',sec('p5l7-teachdeal','Think Harder',body,'Use this after worksheet page 2, for children who go on to the Think Harder page (Q2 compares two deals for 4 boxes). Ask first: "Which sounds better, a free pen or 30% off?" Let children vote, then work out both. Deal A: pay for 2 pens, $20. Deal B: $30 less 30% ($9) is $21. So the free pen wins here, by $1. Step 2: a free pen is $10 off $30, which is one third: about 33% off. '
 'On the worksheet the numbers are different and the answer is different: do not assume "buy and get free" always wins.'))

# ---------- worksheet page 2 ----------
put('p5l7-ws2',ws_preview('p5l7-ws2','57–72 MIN','Worksheet page 2: on your own',[('Q4','Siti spends 20%, then 25% of the money left. Is 55% left?'),('Q5','A class, a table, and glasses: boys, girls and the whole class.')],'Finished early? Try the Think Harder page. Q1 and Q2 have a teaching slide first.','Children work alone. Note who needs a short catch-up next lesson, especially children who add 20% and 25% in Q4. Page 2 has only two questions so that there is time to think. The percentage-change and deal questions are on the Think Harder page (Q1 and Q2).'))
put('p5l7-ws2ans',checks('p5l7-ws2ans','72–76 MIN','Page 2: check together',[('Q4','a) $24   b) $24   c) $72   d) 60% left: she spent $48 of $120 = 40%'),('Q5','Girls 24, boys 16.  Glasses: girls 6, boys 8, class 14.  a) 35%')],
 'Click after a child explains. Q4: 20% of $120 = $24; $96 left; 25% of $96 = $24; $72 left; $72 out of $120 = 60 out of 100. Ben forgot that 25% was of the remainder, not of $120. Q5: girls 60% of 40 = 24, boys 16; glasses 25% of 24 = 6, 50% of 16 = 8; 14 out of 40 = 35 out of 100. Think Harder Q1 (P6 preview): $1 out of the starting $4 is 25%; $1 out of the starting $5 is 20%. Think Harder Q2: X: pay for 3 boxes = $45. Y: 4 boxes = $60, 30% off = $18 off, $42. (b) one free box out of 4 = 25% off.',gapy=135,size=32))

# ---------- stretch / challenge ----------
st=[('1.','A $90 jacket is 10% off. Then the sale price is a further 10% off. What do you pay? Is it the same as 20% off?'),('2.','A jar has 60 sweets. 25% are red. 40% of the REST are green. How many are green?'),('3.','A $80 bag goes up by 50%, then down by 50%. What is the final price?')]
put('p5l7-stretch',sec('p5l7-stretch','For early finishers',h2('Stretch')+numcards(st),'Answers: 1) $72.90. 10% of $90 = $9 off, so $81; then 10% of $81 = $8.10 off, so $72.90. It is NOT the same as 20% off ($72), because the second 10% is of $81, not of $90. '
 '2) 18 green. Red: 25% of 60 = 15. Rest: 45. 40% of 45 = 18. 3) $60. Up 50%: $80 + $40 = $120. Down 50% of $120 = $60 off, so $60.'))
ch=[('1.','A price tag says $109, GST included. Ali says the GST is 9% of $109, which is $9.81. Is he right? How much GST is in the price?'),('2.','Mrs Tan spent 40% of her money on groceries and 25% of the remaining money on a gift. She had $54 left. How much money did she have at first?')]
put('p5l7-challenge',sec('p5l7-challenge','For early finishers',h2('Challenge')+numcards(ch,36),'Pairs try first, then use the "see it" slide if stuck, then the walk-through. These are Think Harder Q5 and Q7 (Q6, the two lamp shops, is only in the workbook). Answers: 1) No. $109 is 109% of the price before GST, so 1% = $1 and the price before GST was $100. The GST is $9, not $9.81. 2) $120. Work backwards: $54 is 75% of the money left after groceries, so that was $72; $72 is 60% of her money, so 10% is $12 and 100% is $120.'))
# chdiag
g1=rect(20,70,640,80,SKY,NAVY,4)+txt(340,122,'price before GST = 100%',30)+rect(660,70,58,80,YEL,NAVY,4)+txt(630,185,'GST = 9%',28,TEAL)
g1+=f'<path d="M20 58 V46 H718 V58" fill="none" stroke="{NAVY}" stroke-width="3"+/>'.replace('+/>','/>')+txt(369,34,'$109 = 109%',34,NAVY)
g1+=txt(369,232,'1% of the price before GST = ?',30,TEAL,'middle',700,'Nunito Sans, Arial')
g2=''
for i in range(10): g2+=rect(20+i*72,64,72,70,YEL if i<4 else WHITE,NAVY,4)
g2+=txt(20+2*72,54,'groceries',26)+txt(20+7*72,54,'money left',26)
x0=20+4*72; wrem=6*72
g2+=f'<path d="M{x0} 146 V156 H{x0+wrem} V146" fill="none" stroke="{TEAL}" stroke-width="3"/>'
for j in range(4): g2+=rect(x0+j*wrem/4,196,wrem/4,70,YEL if j==0 else SKY,NAVY,4)
g2+=txt(x0+wrem/8,241,'gift',26)+txt(x0+wrem*5/8,241,'$54 left',26)
g2+=txt(x0+wrem/2,184,'cut the money left into 4 equal parts',24,TEAL,'middle',700,'Nunito Sans, Arial')
g2+=txt(20+360,310,'whole = ?   Work backwards.',30,TEAL,'middle',700,'Nunito Sans, Arial')
body=h2('Challenge: see it',60)+'<div style="display:flex;gap:32px;align-items:flex-start">'
body+=card(f'<p style="font-size:30px;font-weight:700;color:{TEAL}">Q1: What is the whole?</p>'+svgwrap(740,250,'A bar showing 109 percent made of 100 percent price before GST and 9 percent GST',g1).replace('width:740px;height:250px;flex:none','width:100%;height:auto;display:block'),extra='flex:1;min-width:0;padding:20px 24px')
body+=card(f'<p style="font-size:30px;font-weight:700;color:{TEAL}">Q2: Money left, then a gift</p>'+svgwrap(740,330,'A bar of 10 equal parts, 4 for groceries, and the remaining 6 parts cut into 4 equal parts: one for a gift and three that are 54 dollars',g2).replace('width:740px;height:330px;flex:none','width:100%;height:auto;display:block'),extra='flex:1;min-width:0;padding:20px 24px')+'</div>'
put('p5l7-chdiag',sec('p5l7-chdiag','For early finishers',body,'Show after pairs have tried the Challenge, or if they are stuck. The pictures show the problem, not the answer. Ask: What is the whole in Q1, and what is it 100% of? In Q2, which amount is the new whole after the groceries? How many equal parts is $54? Answers are in the Challenge slide notes.'))
body=h2('Challenge: walk-through')+pin(128,250,800,p('Q1: the whole is the price BEFORE GST',34,800,TEAL))
for i,t in enumerate(['$109 = 100% + 9% = 109%','1% = $109 ÷ 109 = $1','GST = 9% of $100 = $9','Ali used 9% of $109: wrong whole!']): body+=pin(128,330+i*110,800,p(t,32),'rise',WHITE)
body+=pin(992,250,800,p('Q2: work backwards from $54',34,800,TEAL))
for i,t in enumerate(['$54 = 75% of the money left (3 of 4 parts)','1 part = $18, so money left = $72','$72 = 60% of all → 10% = $12','100% = $120.   Check: $48, then $18 ✓']): body+=pin(992,330+i*110,800,p(t,32),'rise',WHITE)
put('p5l7-chwalk',sec('p5l7-chwalk','Challenge',body,'Use after pairs have tried. Q1: the price tag already includes the GST, so $109 is 109% of the unknown price before GST. 109 ÷ 109 = 1: each 1% is $1, and the price before GST is $100, so the GST is $9. Ali took 9% of the wrong whole. Q2: work backwards, undoing each step. After the gift, $54 is 75% of the money left, so a quarter of it is $18 and the money left was $72. After the groceries, 60% of her money is $72, so 10% is $12 and all of it is $120. Check forwards: 40% of $120 = $48 on groceries; $72 left; 25% of $72 = $18 gift; $54 left.'))

# ---------- talk / exit ----------
body=h2('Talk time')+card(chip('TALK TIME',YEL,NAVY)+p('Which is better for the shopper: add 9% GST first and then take 20% off, or take 20% off first and then add 9% GST?',40,600))+card(p('Sentence starters:',34,400,MUTED)+p('“I noticed that …”   “I tested it by …”   “I know because …”',38,600))
put('p5l7-talk',sec('p5l7-talk','76–82 MIN',body,'Minutes 76 to 82. Pairs try it with $100 for 2 minutes, then share. Answer: it is exactly the same. GST first: $109, then 20% off ($21.80) is $87.20. Discount first: $80, then 9% GST ($7.20) is $87.20. Each change is a multiplication, and the order of multiplying does not matter. '
 'Second question if time: Mei says "20% off and then 9% GST is the same as 11% off." Is she right? (No: 11% off $100 would be $89, but the real price is $87.20, because the GST is on the smaller sale price.) Praise the reasons, not only the answers.'))
body=h2('Exit ticket')+card(chip('EXIT TICKET')+p('A $30 toy is sold at 20% off. Then 9% GST is added to the sale price. How much do you pay?',46,600))+card(p('Write your answer on a slip of paper. Show it to your tutor. Then collect your stamp in your inquiry journal.',34,400))
put('p5l7-exit',sec('p5l7-exit','82–90 MIN',body,'Minutes 82 to 90. Answer: $26.16. 20% of $30 = $6, sale price $24. 9% of $24: 10% = $2.40, 1% = $0.24, so 9% = $2.16. $24 + $2.16 = $26.16. Extension: a shop raises every price by 25%, then has a "20% off everything" sale. Is the sale price more than, less than or the same as the old price? Try $40, $100 and $64. (The same: up 25% then down 20% always gives back the old price. $40 to $50 to $40; $100 to $125 to $100; $64 to $80 to $64. Siti on the worksheet fell for the opposite trap: it is NOT the same as up 5%.)'))

# ---------- write ----------
order=['p5l7-title','p5l7-warm1','p5l7-warm2','p5l7-explore1','p5l7-explore2','p5l7-teach1','p5l7-we1','p5l7-try1','p5l7-we2','p5l7-try2','p5l7-key','p5l7-break','p5l7-ws1','p5l7-ws1ans','p5l7-teachrem','p5l7-teachtable','p5l7-ws2','p5l7-ws2ans','p5l7-teachchange','p5l7-teachdeal','p5l7-stretch','p5l7-challenge','p5l7-chdiag','p5l7-chwalk','p5l7-talk','p5l7-exit']
assert set(order)==set(S), set(order)^set(S)
sd=os.path.join(D,'slides')
for f in os.listdir(sd):
    if f.endswith('.html') and f[:-5] not in S: os.remove(os.path.join(sd,f))
for i,h in S.items(): open(os.path.join(sd,i+'.html'),'w').write(h)
deck={'v':4,'createdOnFiles':{'v':1,'at':datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')},'lists':'css',
 'title':'Math Inquirers P5: Lesson 7 – Percentage Puzzles','order':order,'cover':'p5l7-title',
 'sections':{'s1':{'description':'Warm-up and explore','start':'p5l7-title'},'s2':{'description':'Teach: percentages, discounts and GST','start':'p5l7-teach1'},'s3':{'description':'Worksheet with teaching before page 2','start':'p5l7-break'},'s4':{'description':'Stretch, challenge, talk and exit','start':'p5l7-stretch'}},
 'faces':{'fredoka':{'family':'Fredoka','href':'https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&display=swap'},'nunito-sans':{'family':'Nunito Sans','href':'https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@400;600;700&display=swap'}},
 'designSystems':[]}
json.dump(deck,open(os.path.join(D,'deck.json'),'w'),indent=1,ensure_ascii=False)
print(len(order),'slides')

import p5_gaps; p5_gaps.apply(7)
