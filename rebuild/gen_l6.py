import json,os,sys
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,H)
from slidekit import *
D=os.path.join(H,'..','split','l6','project'); S={}
def put(i,h): S[i]=h
# --- warm-up 1: coin shop with priced items ---
def _item(kind):
    N=NAVY
    if kind=='sweet':
        g=f'<polygon points="30,80 6,58 6,102" fill="{YEL}" stroke="{N}" stroke-width="4"/><polygon points="130,80 154,58 154,102" fill="{YEL}" stroke="{N}" stroke-width="4"/><ellipse cx="80" cy="80" rx="52" ry="38" fill="#D64545" stroke="{N}" stroke-width="4"/><path d="M58 62 Q80 80 58 98 M80 50 Q102 80 80 110" stroke="#FFF9EC" stroke-width="6" fill="none"/>'
    elif kind=='pencil':
        g=f'<g transform="rotate(-35 80 80)"><rect x="10" y="64" width="110" height="32" fill="{YEL}" stroke="{N}" stroke-width="4"/><rect x="0" y="64" width="18" height="32" fill="#F2A7A7" stroke="{N}" stroke-width="4"/><polygon points="120,64 152,80 120,96" fill="#F3D9B1" stroke="{N}" stroke-width="4"/><polygon points="142,75 152,80 142,85" fill="{N}"/></g>'
    elif kind=='eraser':
        g=f'<g transform="rotate(-12 80 80)"><rect x="18" y="50" width="124" height="60" rx="10" fill="#FFFFFF" stroke="{N}" stroke-width="4"/><rect x="18" y="50" width="62" height="60" rx="10" fill="{TEAL}" stroke="{N}" stroke-width="4"/></g>'
    elif kind=='sticker':
        st=lambda cx,cy,c: f'<polygon points="{cx},{cy-18} {cx+6},{cy-6} {cx+19},{cy-5} {cx+9},{cy+5} {cx+12},{cy+18} {cx},{cy+11} {cx-12},{cy+18} {cx-9},{cy+5} {cx-19},{cy-5} {cx-6},{cy-6}" fill="{c}" stroke="{N}" stroke-width="2"/>'
        g=f'<rect x="28" y="14" width="104" height="132" rx="10" fill="{SKY}" stroke="{N}" stroke-width="4"/>'+st(58,46,YEL)+st(102,46,'#D64545')+st(58,90,TEAL)+st(102,90,YEL)+st(80,124,'#D64545')
    elif kind=='ruler':
        g=f'<g transform="rotate(-30 80 80)"><rect x="-4" y="58" width="168" height="44" rx="6" fill="{YEL}" stroke="{N}" stroke-width="4"/>'+''.join(f'<line x1="{8+i*12}" y1="58" x2="{8+i*12}" y2="{78 if i%2==0 else 70}" stroke="{N}" stroke-width="3"/>' for i in range(13))+'</g>'
    elif kind=='bottle':
        g=f'<rect x="58" y="10" width="44" height="22" rx="5" fill="{TEAL}" stroke="{N}" stroke-width="4"/><path d="M62 32 L98 32 L112 56 L112 146 Q112 154 104 154 L56 154 Q48 154 48 146 L48 56 Z" fill="{SKY}" stroke="{N}" stroke-width="4"/><rect x="48" y="86" width="64" height="34" fill="{YEL}" stroke="{N}" stroke-width="3"/>'
    elif kind=='car':
        g=f'<path d="M14 104 L14 84 Q16 74 28 72 L50 70 L66 46 Q70 42 78 42 L112 42 Q120 42 124 48 L138 70 L146 72 Q154 74 154 86 L154 104 Z" fill="#D64545" stroke="{N}" stroke-width="4" stroke-linejoin="round"/><path d="M72 50 L84 50 L84 70 L60 70 Z M92 50 L110 50 L124 70 L92 70 Z" fill="{SKY}" stroke="{N}" stroke-width="3"/><circle cx="44" cy="108" r="17" fill="{N}"/><circle cx="44" cy="108" r="7" fill="#EDEDED"/><circle cx="124" cy="108" r="17" fill="{N}"/><circle cx="124" cy="108" r="7" fill="#EDEDED"/>'
    elif kind=='scooter':
        g=f'<line x1="112" y1="24" x2="128" y2="122" stroke="{N}" stroke-width="7" stroke-linecap="round"/><line x1="96" y1="24" x2="128" y2="24" stroke="{N}" stroke-width="8" stroke-linecap="round"/><rect x="30" y="112" width="96" height="14" rx="7" fill="{TEAL}" stroke="{N}" stroke-width="4"/><circle cx="36" cy="132" r="15" fill="{YEL}" stroke="{N}" stroke-width="4"/><circle cx="128" cy="132" r="15" fill="{YEL}" stroke="{N}" stroke-width="4"/>'
    else:  # juice
        g=f'<rect x="44" y="40" width="72" height="108" rx="6" fill="#F28C38" stroke="{N}" stroke-width="4"/><polygon points="44,40 80,22 116,40" fill="#F7B26B" stroke="{N}" stroke-width="4"/><circle cx="80" cy="98" r="20" fill="#FFF9EC" stroke="{N}" stroke-width="3"/><line x1="98" y1="30" x2="112" y2="2" stroke="#D64545" stroke-width="7" stroke-linecap="round"/>'
    return f'<svg aria-label="{kind}" viewBox="0 0 160 160" xmlns="http://www.w3.org/2000/svg" style="width:170px;height:170px;flex:none">{g}</svg>'
def _tag(price):
    return (f'<svg aria-label="price tag {price}" viewBox="0 0 220 100" xmlns="http://www.w3.org/2000/svg" style="width:220px;height:100px">'
            f'<polygon points="4,50 40,6 214,6 214,94 40,94" fill="{YEL}" stroke="{NAVY}" stroke-width="4" stroke-linejoin="round"/>'
            f'<circle cx="38" cy="50" r="9" fill="#FFF9EC" stroke="{NAVY}" stroke-width="4"/>'
            f'<text x="132" y="68" font-size="54" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="Fredoka, Arial">{price}</text></svg>')
shop=[('eraser','Eraser','65¢','50¢ + 10¢ + 5¢  (3 coins)'),('pencil','Pencil','80¢','50¢ + 20¢ + 10¢  (3 coins)'),('sticker','Sticker book','$3','$2 note + $1 coin'),
      ('bottle','Water bottle','$12','$10 + $2  (2 notes)'),('car','Toy car','$25','$10 + $10 + $5  (3 notes)'),('scooter','Scooter','$65','$50 + $10 + $5  (3 notes)')]
body=h2('Warm-up: the Money Shop')+p('Pay exactly with coins and notes. Who can pay with the fewest?',36,600,MUTED)
CW=533; cards=''; ans=''
for i,(k,name,price,a) in enumerate(shop):
    L=128+(i%3)*(CW+32); T=290+(i//3)*300
    inner=(f'<div style="display:flex;align-items:center;gap:20px">{_item(k)}<div style="display:flex;flex-direction:column;gap:10px">'
           f'<p style="font-family:{HF};font-size:40px;font-weight:600">{E(name)}</p>{_tag(price)}</div></div>')
    cards+=pin(L,T,CW,inner,None,WHITE,24,'16px 22px',f'box-sizing:border-box;height:276px;border:4px solid {NAVY};box-shadow:8px 8px 0 {NAVY}')
    ans+=pin(L+20,T+190,CW-40,f'<p style="font-size:30px;font-weight:800;line-height:1.2">{E(a)}</p>','pop',SOFT,16,'12px 18px',f'box-sizing:border-box;border:3px solid {NAVY}')
put('l6-warm1',sec('l6-warm1','0–5 MIN',body+cards+ans,
 'Minutes 0 to 5. The Money Shop. Hand out play money: coins (5¢, 10¢, 20¢, 50¢, $1) and notes ($2, $5, $10, $50). Point to one item at a time: "The pencil costs 80¢. Pay exactly. Can you pay with fewer pieces of money than your partner?" '
 'Children lay out their money, then you click to show the fewest way for that item (clicks reveal Eraser, Pencil, Sticker book, Water bottle, Toy car, Scooter in order). '
 'Fewest: Eraser 65¢ = 50¢ + 10¢ + 5¢ (3). Pencil 80¢ = 50¢ + 20¢ + 10¢ (3). Sticker book $3 = $2 + $1 (2). Water bottle $12 = $10 + $2 (2). Toy car $25 = $10 + $10 + $5 (3). Scooter $65 = $50 + $10 + $5 (3). '
 'Ask: "Cents or dollars? How do you know?" (the ¢ sign or the $ sign). "Someone paid $12 with six $2 notes. Is that right?" (Yes, exactly $12, just not the fewest.) "Why do we start with the biggest note that is not too big?" '
 'Quick finisher: "Buy the water bottle AND the toy car. How much? Fewest notes?" ($37: $10 + $10 + $10 + $5 + $2, 5 notes). Watch for: children who count how many pieces instead of the value, and children who mix up 50¢ and $50.'))
qs=[('1.','Pay 15¢ with two coins.','10¢ + 5¢'),('2.','Pay 30¢ with the fewest coins.','20¢ + 10¢'),('3.','Pay 25¢ with two coins.','20¢ + 5¢'),('4.','Pay 40¢ with two coins.','20¢ + 20¢')]
body=h2('Quick questions')+''.join(qrow(128,260+i*150,1250,a,b) for i,(a,b,c) in enumerate(qs))+''.join(answer(1420,260+i*150,372,c) for i,(a,b,c) in enumerate(qs))
put('l6-warm2',sec('l6-warm2','5–10 MIN',body,'Minutes 5 to 10. Children show the coins with play money, then click to reveal. Ask: "Could you pay 40¢ with two coins another way?" (no: only 20¢ + 20¢).'))
# teach 1: table for 15c then 25c
W=[240,240,260]
body=h2('Every way, in order: use a table')+card(p('Make 15¢ with 10¢ and 5¢ coins.',40,700))
body+=trow(128,380,['10¢','5¢','Total'],W,None,True)
body+=trow(128,470,['1','1','15¢'],W,'rise')+trow(128,560,['0','3','15¢'],W,'rise')
body+=pin(1060,380,732,p('Start with as many of the BIGGEST coin as you can. Then use one fewer, and one fewer, until there are none.',36,700),None,SOFT,20,'24px 28px')
body+=pin(1060,640,732,p('No more rows: the 10¢ count is down to 0. So there are 2 ways.',36,700),'fade',WHITE,20,'24px 28px')
put('l6-teach1',sec('l6-teach1','25–28 MIN',body,'Teach. Click to add each row while children say what goes in it. Think-aloud: "Ways to make 15¢ with 10¢ and 5¢ coins. I start with the biggest coin: one 10¢. Then 5¢ is left, so one 5¢. Now no 10¢: only 5¢ coins, three of them. The 10¢ column went 1, 0, so I know I am finished."'))
W4=[200,200,200,240]
body=h2('Worked example: 25¢')+card(p('Make 25¢ with 20¢, 10¢ and 5¢ coins. How many ways?',40,700))
body+=trow(128,380,['20¢','10¢','5¢','Total'],W4,None,True)
rows=[['1','0','1','25¢'],['0','2','1','25¢'],['0','1','3','25¢'],['0','0','5','25¢']]
for i,r in enumerate(rows): body+=trow(128,470+i*90,r,W4,'rise')
body+=pin(1180,380,612,p('20¢ first: one 20¢ (20 + 5).',34,700),'fade',WHITE,20,'20px 24px')+pin(1180,520,612,p('Then no 20¢: two 10¢, one 10¢, no 10¢.',34,700),'fade',WHITE,20,'20px 24px')+pin(1180,680,612,p('4 ways. 10¢ + 5¢ + 10¢ is the same way as row 2.',34,700),'fade',SOFT,20,'20px 24px')
put('l6-we1',sec('l6-we1','28–31 MIN',body,'Click to build each row and the side notes. Ask before each row: "What comes next if I go one fewer?" Think-aloud: "With a 20¢: 20 + 5. With 10¢ but no 20¢: 10 + 10 + 5 and 10 + 5 + 5 + 5. With only 5¢: five of them. That is 4 ways. I used a table so I did not repeat any."'))
put('l6-try1',try_slide('l6-try1','31–33 MIN','Your turn: how many ways?','Use a table. Biggest coin first.',[('a','Make 10¢ with 10¢ and 5¢ coins.','2 ways'),('b','Make 20¢ with only 10¢ and 5¢ coins.','3 ways'),('c','Make 35¢ with 20¢ and 5¢ coins only.','2 ways')],'Whiteboards. a) 10, or 5 + 5. b) 10 + 10, 10 + 5 + 5, four 5¢. c) 20 + 5 + 5 + 5, or seven 5¢. Ask: "Why can\'t we use two 20¢ for c?" (40¢ is too much).'))
body=h2('Key idea: work in order')+card(p('Biggest coin first, then one fewer each time. Use a table so you do not repeat or miss a way.',44,700))+card(p('Same coins in a different order count as one way.',38,600,MUTED))
put('l6-key',sec('l6-key','33–35 MIN',body,'Say the key idea together. Common mistakes to watch for during the worksheet: (1) Listing the same way twice in a different order (10+5+5 and 5+10+5). (2) Choosing many small coins instead of looking for the fewest. (3) Stopping at the first set in Think Harder T2 instead of checking for all of them.'))
put('l6-ws1',ws_preview('l6-ws1','40–52 MIN','Worksheet page 1: with your partner',[('Q1','Ways to make 20¢. Fill in the table, biggest coin first.'),('Q2','All the ways to make 30¢. Write each way like this: 20¢ + 5¢ + 5¢')],'Use play coins on the table, then write the way down.','Minutes 40 to 52. Walk around. Ask "How do you know you have them all?" Check that pairs work in order.'))
put('l6-ws1ans',check_slide('l6-ws1ans','52–54 MIN','Page 1: check together',[('Q1','4 ways: 20 / 10+10 / 10+5+5 / 5+5+5+5.  Fewest: one 20¢.  Most: four 5¢.'),('Q2','6 ways: 20+10, 20+5+5, 10+10+10, 10+10+5+5, 10+5+5+5+5, six 5¢')],'Click after pairs explain. Q1c: "We started with the biggest coin and went one fewer each time until there were none."'))
# fewest coins
body=h2('Fewest coins: biggest coin you can, again and again')+card(p('Pay 65¢ with the fewest coins (5¢, 10¢, 20¢, 50¢).',40,700))+step(1,'Biggest coin that fits: 50¢. 15¢ is left.',top=420,size=36)+step(2,'Biggest coin that fits 15¢: 10¢. 5¢ is left.',top=530,size=36)+step(3,'Then 5¢. Nothing left. 50 + 10 + 5 = 65: 3 coins.',top=640,size=36)
put('l6-teachfew',sec('l6-teachfew','54–56 MIN',body,'Teach before worksheet page 2 (Q3). Ask after step 3: "Could 2 coins make 65¢?" (No: the two biggest, 50 + 20, make 70, and no pair makes exactly 65.)'))
# exact number of coins
body=h2('Exactly 3 coins')+card(p('Make 25¢ with exactly 3 coins (5¢, 10¢, 20¢).',40,700))+step(1,'Try a 20¢: 20 + 5 = 25, but that is only 2 coins. Not 3.',top=420,size=36)+step(2,'Try two 10¢: 10 + 10 + 5 = 25, and it is 3 coins ✓',top=530,size=36)+step(3,'Try one 10¢: 10 + 5 + 5 = 20, too little.  Only one way: 10 + 10 + 5.',top=640,size=36)+pin(128,770,1664,p('Check TWO things every time: the total, and the number of coins.',34,700),'fade',SOFT,20,'18px 28px')
put('l6-teachexact',sec('l6-teachexact','56–57 MIN',body,'Optional teaching for early finishers, before Think Harder T2 (ALL the sets of 4 coins worth 70¢). Model trying every biggest-coin start, not stopping at the first answer.'))
# swap coins
body=h2('Swap coins to reach the total')+card(p('5 coins, only 5¢ and 10¢, worth 35¢. How many of each?',40,700))+step(1,'Start with all 5¢: five 5¢ = 25¢. We need 10¢ more.',top=420,size=36)+step(2,'Each swap of a 5¢ for a 10¢ adds 5¢. 25 → 30 → 35: 2 swaps.',top=530,size=36)+step(3,'So two 10¢ and three 5¢. Check: 20 + 15 = 35, 5 coins ✓',top=640,size=36)
put('l6-teachswap',sec('l6-teachswap','57–58 MIN',body,'Optional teaching for early finishers, before Think Harder T3 (Sam\'s 90¢). Act it out with play coins: lay out five 5¢, then swap one at a time and count the total aloud.'))

# dollars: notes and $1 coins
def money_strip(w=1664,h=130):
    items=[('$1','coin','#E8D27A'),('$2','note','#C9B6E4'),('$5','note','#A8D5A2'),('$10','note','#F2A7A7'),('$50','note','#A7C4F2')]
    g=''; x=10
    for lab,kind,col in items:
        if kind=='coin':
            g+=f'<circle cx="{x+55}" cy="65" r="52" fill="{col}" stroke="{NAVY}" stroke-width="4"/><circle cx="{x+55}" cy="65" r="42" fill="none" stroke="{NAVY}" stroke-width="2"/><text x="{x+55}" y="80" font-size="40" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="Fredoka, Arial">{lab}</text>'; x+=150
        else:
            g+=f'<rect x="{x}" y="10" width="250" height="110" rx="10" fill="{col}" stroke="{NAVY}" stroke-width="4"/><rect x="{x+12}" y="22" width="226" height="86" rx="6" fill="none" stroke="{NAVY}" stroke-width="2" stroke-dasharray="6 5"/><text x="{x+125}" y="84" font-size="52" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="Fredoka, Arial">{lab}</text>'; x+=290
    return f'<svg aria-label="A $1 coin and $2, $5, $10 and $50 notes" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="width:{w}px;height:{h}px;flex:none">{g}</svg>'
body=h2('Dollars: notes and $1 coins')+money_strip()+card(p('A game costs $38. Pay exactly with the fewest notes and coins.',40,700))
body+=step(1,'Biggest first. $50 is too much. Use $10 notes: $10, $20, $30.',top=560,size=36)
body+=step(2,'$8 is left. $5 → $35. $2 → $37. $1 → $38.',top=660,size=36)
body+=answer(128,770,1664,'$10 + $10 + $10 + $5 + $2 + $1 = $38   (6 pieces of money)')
put('l6-teachnotes',sec('l6-teachnotes','58–59 MIN',body,'Teach before worksheet page 2 (Q5 uses dollars). Hold up play notes: "These are dollars, not cents. Look for the $ sign." Same idea as coins: biggest note that is not too much, then work down, then count on to check: 10, 20, 30, 35, 37, 38. Point out there is no $20 note, so $20 is two $10 notes. Watch for: children who mix up $50 and 50¢, and children who write 38¢ instead of $38.'))
put('l6-trynotes',try_slide('l6-trynotes','59–60 MIN','Your turn: dollars','Use play notes. Then click to check.',[
 ('a','A book costs $14. Fewest notes and coins?','$10 + $2 + $2'),
 ('b','Ali pays for a $20 toy with a $50 note. How much change?','$30'),
 ('c','You have two $10 notes and one $5 note. Can you buy a $27 kite?','No, $2 short')],
 'Minutes 59 to 60. Whiteboards. a) $10 + $2 + $2 (3 notes); $10 + $4 is not a note, so two $2 notes. b) Count on from $20 to $50: $30. c) $10 + $10 + $5 = $25, which is less than $27, so no: $2 short.',size=36))
put('l6-ws2',ws_preview('l6-ws2','60–67 MIN','Worksheet page 2: on your own',[('Q3','85¢ with the fewest coins, then a way with exactly 6 coins.'),('Q4','Can 35¢ be made with 2 coins? Explain.'),('Q5','Dollars: notes and $1 coins. Fewest notes, 3 ways to pay $20, and is there enough money?')],'Finished early? Stretch and Challenge come next.','Children work alone. Note who needs a short catch-up next lesson.'))
put('l6-ws2ans',check_slide('l6-ws2ans','67–69 MIN','Page 2: check together',[('Q3','4 coins: 50 + 20 + 10 + 5.  6 coins: e.g. 50 + 10 + 10 + 5 + 5 + 5'),('Q4','No: two coins make 10, 15, 20, 25, 30, 40, 55, 60, 70 or 100'),('Q5','a) $10 + $5 + $2.   b) e.g. $10 + $10;  $10 + $5 + $5;  $5 + $5 + $5 + $5.   c) No: $73 is more than $70.')],'Click after a child explains. Think Harder T3 (Sam): six 10¢ = 60¢; each swap to a 20¢ adds 10¢; 30¢ more means 3 swaps.'))
st=[('1.','How many ways can you make 40¢ with 20¢, 10¢ and 5¢ coins?'),('2.','Mei has 6 coins, all 5¢ and 10¢, worth 45¢. How many of each?'),('3.','What is the fewest number of coins for 95¢ (5¢, 10¢, 20¢, 50¢)?')]
put('l6-stretch',sec('l6-stretch','For early finishers',h2('Stretch')+''.join(card(p(f'<span style="color:#1F7A6F">{a}</span>  {E(b)}',38,600,raw=True)) for a,b in st),'Answers: 1) 9 ways (two 20¢: 1 way; one 20¢: 3 ways; no 20¢: 5 ways). 2) Three 10¢ and three 5¢. 3) 4 coins: 50 + 20 + 20 + 5 (3 coins cannot work: you need a 5¢, and no two coins make 90¢).'))
body=h2('Challenge: walk-through')+pin(128,250,800,p('Q1: count by number of coins',38,800,TEAL))
for i,t in enumerate(['1 coin: 5, 10, 20, 50 → 4 amounts','2 coins: 15, 25, 55, 30, 60, 70 → 6','3 coins: 35, 65, 75, 80 → 4','4 coins: 85 → 1.   Total: 15 ✓']): body+=pin(128,330+i*105,800,p(t,32),'rise',WHITE)
body+=pin(992,250,800,p('Q2: try biscuits 1, 2, 3 …',38,800,TEAL))
for i,t in enumerate(['1 biscuit: 70¢ left. Not a 15¢ amount ✗','2 biscuits: 50¢ left ✗','3 biscuits: 30¢ left = 2 sweets ✓','4 biscuits: 10¢ left ✗.  Answer: 2 sweets, 3 biscuits']): body+=pin(992,330+i*105,800,p(t,32),'rise',WHITE)
put('l6-chwalk',sec('l6-chwalk','Challenge',body,'Use after pairs have tried. Q1: the trick is to work in order by number of coins so nothing is missed or repeated. Q2: 15¢ amounts are 15, 30, 45, 60, 75; only 30¢ is left over when Ben buys 3 biscuits.'))
# exit ticket update
ex=os.path.join(D,'slides','l6-exit.html'); s=open(ex).read()
s=s.replace('Make 25¢ using exactly three coins from 5¢, 10¢, 20¢, 50¢.','Make 40¢ using exactly three coins from 5¢, 10¢, 20¢, 50¢.').replace('Answer: 10¢ + 10¢ + 5¢.','Answer: 20¢ + 10¢ + 10¢.')
open(ex,'w').write(s)
for i,h in S.items(): open(os.path.join(D,'slides',i+'.html'),'w').write(h)
for old in ['l6-mini1','l6-mini2']:
    f=os.path.join(D,'slides',old+'.html')
    if os.path.exists(f): os.remove(f)
t=os.path.join(D,'slides','l6-title.html'); s=open(t).read(); s=s.replace('mini-lesson 25 to 35, brain break 35 to 40, worksheet 40 to 70','teaching 25 to 35 (click to reveal each step and answer), brain break 35 to 40, worksheet 40 to 70 with short teaching before each page and a check-together slide after it'); open(t,'w').write(s)
deck=json.load(open(os.path.join(D,'deck.json')))
deck['order']=['l6-title','l6-warm1','l6-warm2','l6-explore1','l6-explore2','l6-teach1','l6-we1','l6-try1','l6-key','l6-break','l6-ws1','l6-ws1ans','l6-teachfew','l6-teachnotes','l6-trynotes','l6-ws2','l6-ws2ans','l6-stretch','l6-teachexact','l6-teachswap','l6-challenge','l6-chdiag','l6-chwalk','l6-talk','l6-exit']
deck['sections']={'s1':{'description':'Warm-up and explore','start':'l6-title'},'s2':{'description':'Teach: every way, in order','start':'l6-teach1'},'s3':{'description':'Worksheet with teaching before each page','start':'l6-break'},'s4':{'description':'Stretch, challenge, talk and exit','start':'l6-stretch'}}
json.dump(deck,open(os.path.join(D,'deck.json'),'w'),indent=1,ensure_ascii=False)
print(len(deck['order']),'slides')

import p1fix
p1fix.finish(D,6,{'l6-ws1':'40–52 MIN','l6-ws1ans':'52–54 MIN','l6-teachfew':'54–56 MIN','l6-teachnotes':'56–57 MIN','l6-trynotes':'57–58 MIN','l6-ws2':'58–68 MIN'},optional=('stretch','challenge','chdiag','chwalk','teachexact','teachswap'))
