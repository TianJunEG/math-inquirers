"""Math Inquirers P2, Lesson 6: Market Day. Writes split/p2l5/project (deck.json + slides/*.html)."""
import json,os,sys
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,H)
from slidekit import *
N=6; P=f'p2l{N}'
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

# ---------- shop item drawings (same drawings as the P1 Money Shop) ----------
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
def _tag(price,w=260):
    return (f'<svg aria-label="price tag {price}" viewBox="0 0 260 100" xmlns="http://www.w3.org/2000/svg" style="width:{w}px;height:{w*100/260:.0f}px;flex:none">'
            f'<polygon points="4,50 40,6 254,6 254,94 40,94" fill="{YEL}" stroke="{NAVY}" stroke-width="4" stroke-linejoin="round"/>'
            f'<circle cx="38" cy="50" r="9" fill="#FFF9EC" stroke="{NAVY}" stroke-width="4"/>'
            f'<text x="150" y="68" font-size="50" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="Fredoka, Arial">{price}</text></svg>')
def tags_svg(items,w=1664,h=150,aria='price tags'):
    """items: list of (name, price) drawn as a row of tags"""
    n=len(items); step_=w/n; s=f'<svg aria-label="{E(aria)}" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="width:{w}px;height:{h}px">'
    for i,(name,price) in enumerate(items):
        x=i*step_+10; tw=step_-30
        s+=(f'<polygon points="{x},{h/2} {x+40},8 {x+tw},8 {x+tw},{h-8} {x+40},{h-8}" fill="{YEL}" stroke="{NAVY}" stroke-width="4" stroke-linejoin="round"/><circle cx="{x+36}" cy="{h/2}" r="9" fill="{CREAM}" stroke="{NAVY}" stroke-width="4"/>'
            f'<text x="{x+20+tw/2}" y="{h/2-8}" font-size="34" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="Nunito Sans, Arial">{E(name)}</text>'
            f'<text x="{x+20+tw/2}" y="{h/2+42}" font-size="46" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="Fredoka, Arial">{E(price)}</text>')
    return s+'</svg>'

# 1 title
put(f'{P}-title',title_slide(f'{P}-title',3,'Market Day','Money',
 'Pay exactly with the fewest notes and coins, list every way in order, give change and work backwards with money.',
 'Objective: Read and write money in dollars and cents, pay exactly with the fewest notes and coins, make a list in order to find every way to pay, give change by counting on, decide whether there is enough money, and work backwards to find how much someone had at first. '
 'Materials: play money (coins 5¢, 10¢, 20¢, 50¢, $1; notes $2, $5, $10, $50), about 6 of each per pair, price tags, mini whiteboards. '
 'Online: print the cut-out coins and notes, or use real money at home; the shop and toy stall are on the slides and children show their money to the camera. '
 'Time plan: warm-up 0 to 8, explore 8 to 20 (explore2 talk is 6 minutes), teaching 20 to 32 (click to reveal each step and answer), brain break 32 to 36, short teaching 36 to 38, worksheet page 1 38 to 50 then check together 50 to 52, short teaching 52 to 57, worksheet page 2 57 to 69 then check together 69 to 72, talk time 72 to 80, exit ticket 80 to 90. '
 'Level: P2 adds and subtracts money in dollars only or in cents only; mixed amounts like $3.45 are only counted out with notes and coins, never added in columns. Singapore money has no $20 note.'))

# 2 warm1: Market Day shop
shop=[('eraser','Eraser','85¢','50¢ + 20¢ + 10¢ + 5¢  (4)'),('pencil','Pencil','$1.35','$1 + 20¢ + 10¢ + 5¢  (4)'),('sticker','Sticker book','$3.45','$2 + $1 + 20¢ + 20¢ + 5¢  (5)'),
      ('bottle','Water bottle','$6.50','$5 + $1 + 50¢  (3)'),('car','Toy car','$12.70','$10 + $2 + 50¢ + 20¢  (4)'),('scooter','Scooter','$57.20','$50 + $5 + $2 + 20¢  (4)')]
body=h2('Warm-up: Market Day shop')+p('Pay exactly with notes and coins. Who can pay with the fewest pieces?',36,600,MUTED)
CW=533; cards=''; ans=''
for i,(k,name,price,a) in enumerate(shop):
    L=128+(i%3)*(CW+32); T=290+(i//3)*300
    inner=(f'<div style="display:flex;align-items:center;gap:16px">{_item(k).replace("width:170px;height:170px","width:160px;height:160px")}<div style="display:flex;flex-direction:column;gap:10px">'
           f'<p style="font-family:{HF};font-size:38px;font-weight:600">{E(name)}</p>{_tag(price,250)}</div></div>')
    cards+=pin(L,T,CW,inner,None,WHITE,24,'16px 20px',f'box-sizing:border-box;height:276px;border:4px solid {NAVY};box-shadow:8px 8px 0 {NAVY}')
    ans+=pin(L+16,T+186,CW-32,f'<p style="font-size:28px;font-weight:800;line-height:1.2">{E(a)}</p>','pop',SOFT,16,'12px 16px',f'box-sizing:border-box;border:3px solid {NAVY}')
put(f'{P}-warm1',sec(f'{P}-warm1','0–5 MIN',body+cards+ans,
 'Minutes 0 to 5. The Market Day shop. Hand out play money. Point to one item at a time: "The sticker book costs $3.45: 3 dollars and 45 cents. Pay exactly. Can you use fewer pieces than your partner?" Children lay out their money; click to show the fewest way (clicks go Eraser, Pencil, Sticker book, Water bottle, Toy car, Scooter). '
 'Fewest: 85¢ = 50¢ + 20¢ + 10¢ + 5¢ (4). $1.35 = $1 + 20¢ + 10¢ + 5¢ (4). $3.45 = $2 + $1 + 20¢ + 20¢ + 5¢ (5). $6.50 = $5 + $1 + 50¢ (3). $12.70 = $10 + $2 + 50¢ + 20¢ (4). $57.20 = $50 + $5 + $2 + 20¢ (4). '
 'Strategy to draw out: pay the dollars first with the biggest note that is not too much, then the cents with the biggest coin that fits. Ask: "Someone paid $6.50 with three $2 notes and five 10¢ coins. Is it exact? Is it the fewest?" (Exact, yes. Fewest, no: 8 pieces instead of 3.) Watch for 50¢ and $50 mixed up.'))

# 3 warm2
qs=[('1.','Write 345¢ in dollars and cents.','$3.45'),('2.','How many cents is $2.05?','205¢'),('3.','Which is more: $1.50 or 105¢?','$1.50'),('4.','Pay 75¢ with the fewest coins.','50¢+20¢+5¢'),('5.','You have 60¢. A sticker costs 85¢. How much more do you need?','25¢')]
body=h2('Quick questions')+''.join(qrow(128,250+i*125,1250,a,b,36) for i,(a,b,c) in enumerate(qs))+''.join(answer(1420,250+i*125,372,c) for i,(a,b,c) in enumerate(qs))
put(f'{P}-warm2',sec(f'{P}-warm2','5–8 MIN',body,'Minutes 5 to 8. Whiteboards, then click. 1) 345¢ is 300¢ and 45¢: $3 and 45¢. 2) $2 is 200¢, so $2.05 is 205¢ (watch for 25¢ or 250¢). 3) $1.50 is 150¢, which is more than 105¢. 4) 50¢ + 20¢ + 5¢, 3 coins. 5) Count on: 60¢ → 80¢ is 20¢, then 5¢ more to 85¢: 25¢ (cents only, no mixed dollars and cents). Ask: "Why does $2.05 need a 0?"'))

# 4 explore1: toy stall
toys=[('kite','Kite','$6'),('ball','Ball','$4'),('yoyo','Yo-yo','$3'),('bubbles','Bubbles','$2'),('sticker','Sticker','$1')]
def toy(k):
    N=NAVY
    if k=='kite': g=f'<polygon points="60,6 106,52 60,110 14,52" fill="#D64545" stroke="{N}" stroke-width="4"/><line x1="60" y1="6" x2="60" y2="110" stroke="{N}" stroke-width="3"/><line x1="14" y1="52" x2="106" y2="52" stroke="{N}" stroke-width="3"/><path d="M60 110 q-10 10 0 18 q10 8 0 14" fill="none" stroke="{N}" stroke-width="3"/>'
    elif k=='ball': g=f'<circle cx="60" cy="66" r="50" fill="{YEL}" stroke="{N}" stroke-width="4"/><path d="M14 52 Q60 82 106 52 M22 96 Q60 62 98 96" fill="none" stroke="{N}" stroke-width="4"/>'
    elif k=='yoyo': g=f'<line x1="60" y1="2" x2="60" y2="34" stroke="{N}" stroke-width="3"/><circle cx="60" cy="74" r="42" fill="{TEAL}" stroke="{N}" stroke-width="4"/><circle cx="60" cy="74" r="14" fill="{CREAM}" stroke="{N}" stroke-width="4"/>'
    elif k=='bubbles': g=f'<rect x="34" y="40" width="52" height="80" rx="10" fill="{SKY}" stroke="{N}" stroke-width="4"/><rect x="44" y="26" width="32" height="16" rx="4" fill="#D64545" stroke="{N}" stroke-width="3"/><circle cx="96" cy="22" r="14" fill="none" stroke="{TEAL}" stroke-width="3"/><circle cx="24" cy="30" r="10" fill="none" stroke="{TEAL}" stroke-width="3"/>'
    else: g=f'<polygon points="60,14 74,46 108,48 82,70 90,104 60,86 30,104 38,70 12,48 46,46" fill="{YEL}" stroke="{N}" stroke-width="4"/>'
    return g
g=''
for i,(k,name,price) in enumerate(toys):
    x=i*300
    g+=f'<g transform="translate({x+60},0)">{toy(k)}</g>'
    g+=f'<polygon points="{x+20},180 {x+44},144 {x+220},144 {x+220},216 {x+44},216" fill="{YEL}" stroke="{NAVY}" stroke-width="4" stroke-linejoin="round"/><text x="{x+132}" y="194" font-size="44" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="Fredoka, Arial">{price}</text>'
pic=f'<svg aria-label="Toy stall: kite $6, ball $4, yo-yo $3, bubbles $2, sticker $1" viewBox="0 0 1480 222" xmlns="http://www.w3.org/2000/svg" style="width:1480px;height:222px">{g}</svg>'
put(f'{P}-explore1',explore1(f'{P}-explore1',['You have $10. Look at the toy stall.','Choose some toys (at most one of each). What do they cost? What change do you get?','Find every basket that costs EXACTLY $10.','Make a list in order so you do not miss one or count one twice.'],pic,
 'Minutes 8 to 14. Each pair gets a $10 note and the price list: kite $6, ball $4, yo-yo $3, bubbles $2, sticker $1 (whole dollars, so children add in dollars only). First they choose any basket and find the change, then they hunt for every basket that costs exactly $10. Prediction first: "How many $10 baskets do you think there are?" '
 'Online: the stall is on the slide; children record baskets on whiteboards. Hint for stuck pairs: "Put the kite in first. How much is left to spend?"'))

# 5 explore2
put(f'{P}-explore2',sec(f'{P}-explore2','14–20 MIN',h2('Explore: talk about it')+qcards([('1.','How many baskets cost exactly $10?'),('2.','How do you know you have found them all?'),('3.','You buy the kite and the bubbles. How much change do you get?')],40),
 'Minutes 14 to 20. Gather the pairs. Answers: 1) 3 baskets: kite + ball ($6 + $4); kite + yo-yo + sticker ($6 + $3 + $1); ball + yo-yo + bubbles + sticker ($4 + $3 + $2 + $1). 2) Work in order: first all baskets WITH the kite ($4 more to spend: ball, or yo-yo + sticker, since bubbles + sticker is only $3 and yo-yo + bubbles is $5), then baskets WITHOUT the kite (the other four toys cost $10 altogether, so all four is the only one). 3) $6 + $2 = $8, so $2 change.'))

# 6 teach1 dollars and cents
body=h2('Dollars and cents')
boxes=[('$3.45','the price tag'),('3 dollars 45 cents','what we say'),('345¢','all in cents')]
for i,(a,b) in enumerate(boxes):
    body+=pin(128+i*560,260,520,p(a,52,800)+p(b,30,600,MUTED),'rise' if i else None,WHITE,24,'24px 30px','align-items:center')
body+=pin(128,470,1664,p('100¢ = $1.   So $3 = 300¢, and $3.45 = 300¢ + 45¢ = 345¢.',40,700),'fade',SOFT,20,'22px 30px')
body+=pin(128,600,810,p('$3.05 = 305¢',44,800)+p('3 dollars and 5 cents',32,600,MUTED),'rise',WHITE,20,'22px 30px')
body+=pin(982,600,810,p('$3.50 = 350¢',44,800)+p('3 dollars and 50 cents',32,600,MUTED),'rise',WHITE,20,'22px 30px')
body+=pin(128,790,1664,p('The two digits after the dot are the cents. 5 cents is written .05',36,700,TEAL),'fade')
put(f'{P}-teach1',sec(f'{P}-teach1','20–22 MIN',body,'Teach. Hold up $3 in notes and coins and 45¢ in coins: "This is 3 dollars and 45 cents. We write $3.45." Count it all in cents with the children: 100, 200, 300, then 320, 340, 345. Then the trap: $3.05 and $3.50 look alike but 5¢ and 50¢ are very different. Ask: "How do you write 2 dollars and 8 cents?" ($2.08).'))

# 7 we1 make a list in order
W4=[200,200,200,260]
body=h2('Make a list in order')+card(p('Pay exactly $6 using $5 notes, $2 notes and $1 coins. How many ways?',40,700))
body+=trow(128,380,['$5','$2','$1','Pieces'],W4,None,True)
for i,r in enumerate([['1','0','1','2'],['0','3','0','3'],['0','2','2','4'],['0','1','4','5'],['0','0','6','6']]): body+=trow(128,462+i*82,r,W4,'rise')
body+=pin(1180,380,612,p('Start with the MOST of the biggest note: one $5. $1 is left.',34,700),'fade',WHITE,20,'20px 24px')
body+=pin(1180,540,612,p('No $5: as many $2 as fit (three), then one fewer each time. Fill up with $1.',34,700),'fade',WHITE,20,'20px 24px')
body+=pin(1180,740,612,p('The $2 column went 3, 2, 1, 0: finished. 5 ways.',34,700),'fade',SOFT,20,'20px 24px')
put(f'{P}-we1',sec(f'{P}-we1','22–25 MIN',body,'Click to build each row and the side notes. Ask before each row: "What comes next if I use one fewer $2?" Think-aloud: "One $5 and one $1. Now no $5: three $2 makes $6. Two $2 makes $4, so two $1. One $2 and four $1. Six $1 coins. The $2 column counts down to 0, so I know I have them all: 5 ways." Point out $5 + $1 and $1 + $5 are the same way.'))

# 8 try1
put(f'{P}-try1',try_slide(f'{P}-try1','25–27 MIN','Your turn: in order','Make a table. Most of the biggest first.',[('a','How many ways to pay 40¢ with 20¢ and 10¢ coins?','3 ways'),('b','How many ways to pay $10 with only $5 and $2 notes?','2 ways'),('c','Pay 95¢ with the fewest coins.','50+20+20+5')],
 'Whiteboards. a) 20 + 20; 20 + 10 + 10; four 10¢. b) Two $5; or five $2. One $5 leaves $5, which $2 notes cannot make (2, 4, 6 …), so that row is "not this one". c) 50¢ + 20¢ + 20¢ + 5¢, 4 coins.',size=36))

# 9 we2 work backwards with money
bsvg=bars([('Mei',[('drink 80¢',80,GREEN),('bun 65¢',65,YEL),('left 55¢',55,SKY)],'')],unit=6,x0=140,aria='A bar for all of Mei’s money: drink 80¢, bun 65¢, left 55¢')
body=h2('Work backwards with money')+card(p('Mei bought a drink for 80¢. Then she bought a bun for 65¢. She has 55¢ left. How much money did she have at first?',38,700))
body+=pin(128,420,1664,bsvg)
body+=step(1,'Start at the end: 55¢ is left.',top=530,size=34)
body+=step(2,'Put back the bun:  55¢ + 65¢ = 120¢',top=625,size=34)
body+=step(3,'Put back the drink:  120¢ + 80¢ = 200¢',top=720,size=34)
body+=answer(128,820,1664,'200¢ = $2.  Check: 200 − 80 = 120,  120 − 65 = 55 ✓')
put(f'{P}-we2',sec(f'{P}-we2','27–30 MIN',body,'Click through. The bar shows all her money cut into what she spent and what is left, so "at first" is the whole bar. Think-aloud: "The last thing she did was buy the bun, so I put the bun money back first." Ask: "How do we write 200¢ in dollars?" ($2, or $2.00).'))

# 10 try2
put(f'{P}-try2',try_slide(f'{P}-try2','30–31 MIN','Your turn: work backwards','Start from the end. Put back what was spent.',[('a','Ali paid with a $10 note and got $4 change. What did the toy cost?','$6'),('b','Mei spent 35¢. Now she has 40¢. How much did she have at first?','75¢'),('c','Ravi spent half his money on a book, then $5 on a game. He has $3 left. How much at first?','$16')],
 'Whiteboards. a) $10 − $4 = $6 (check: $6 + $4 = $10). b) 40¢ + 35¢ = 75¢. c) $3 + $5 = $8 is the half he kept after the book; the other half is also $8, so $16 (check: half of $16 is $8, $8 − $5 = $3).',size=34))

# 11 key
body=h2('Key idea: in order, and backwards')+card(p('Find every way: make a list in order, the most of the biggest note first, then one fewer each time.',42,700))+card(p('Find what someone had at first: start at the end and put back what was spent.',42,700))+card(p('100¢ = $1.  There is no $20 note.',36,600,MUTED))
put(f'{P}-key',sec(f'{P}-key','31–32 MIN',body,'Say the key ideas together. Common mistakes to watch for during the worksheet: (1) Mixing up dollars and cents: 345¢ written as $34.5, or $3.05 read as $3.50. (2) Using a $20 note, or not starting with the biggest note that fits when finding the fewest. (3) Listing ways with no order, so some are missed or written twice.'))

# 12 break
put(f'{P}-break',break_slide(f'{P}-break','Shopkeeper stretch. The tutor calls an amount: reach up high for dollars, touch your toes for cents. “$3.50!”  “75¢!”  “205¢!” (that is $2.05, so reach up!)','Four minutes. Online: children stay in view of the camera and move in place.'))

# 13 teachfew
body=h2('Fewest notes and coins: dollars first')+card(p('Pay exactly $27.85 with the fewest notes and coins.',40,700))
body+=step(1,'Dollars: $50 is too much. There is no $20 note. $10, $10, then $5, then $2:  $27.',top=380,size=34)
body+=step(2,'Cents: biggest coin that fits each time: 50¢, 20¢, 10¢, 5¢:  85¢.',top=490,size=34)
body+=step(3,'$10 + $10 + $5 + $2 + 50¢ + 20¢ + 10¢ + 5¢:  8 pieces.',top=600,size=34)
body+=pin(128,720,1664,p('Count on to check: $10, $20, $25, $27, then $27.50, $27.70, $27.80, $27.85 ✓',34,700),'fade',SOFT,20,'18px 28px')
put(f'{P}-teachfew',sec(f'{P}-teachfew','36–38 MIN',body,'Teach before worksheet page 1 (Q1 has four prices to pay with the fewest pieces). Model with play money. Stress: $20 is two $10 notes. Ask: "Could $27 use fewer than 4 notes?" (No: no single note or pair of notes makes $27 without a $20 note.) Do not do the worksheet prices.'))

# 14 ws1, 15 ws1ans
put(f'{P}-ws1',ws_preview(f'{P}-ws1','38–50 MIN','Worksheet page 1: with your partner',[('Q1','Pay exactly with the FEWEST notes and coins. Dollars first, then cents.'),('Q2','Every way to pay $8 with $5, $2 and $1. Fill the table in order.')],'Use play money first, then write it down.','Minutes 38 to 50. Walk around. Ask "How do you know you have them all?" Check that pairs start Q2 with one $5 note and then count the $2 notes down.'))
put(f'{P}-ws1ans',check_slide(f'{P}-ws1ans','50–52 MIN','Page 1: check together',[('$1.65','$1 + 50¢ + 10¢ + 5¢   (4)'),('$4.30','$2 + $2 + 20¢ + 10¢   (4)'),('$18.75','$10 + $5 + $2 + $1 + 50¢ + 20¢ + 5¢   (7)'),('$76','$50 + $10 + $10 + $5 + $1   (5)'),('Q2','7 ways.   4 pieces: $5 + $1 + $1 + $1,  and  $2 + $2 + $2 + $2')],
 'Click after pairs explain. Q2 table ($5, $2, $1): 1,1,1 / 1,0,3 / 0,4,0 / 0,3,2 / 0,2,4 / 0,1,6 / 0,0,8. Row H stays empty. With one $5 there is $3 left: one $2 + one $1, or three $1. With no $5 the $2 column goes 4, 3, 2, 1, 0. Pieces: 3, 4, 4, 5, 6, 7, 8.',lw=230))

# 16 teachchange
body=h2('Change: count on like a shopkeeper')+card(p('A book costs $33. Ali pays with a $50 note. How much change?',40,700))
body+=step(1,'Count on from $33:  $33 → $35 is $2.',top=380,size=34)
body+=step(2,'$35 → $40 is $5.   $40 → $50 is $10.',top=480,size=34)
body+=step(3,'Change: $2 + $5 + $10 = $17. Fewest notes: $10 + $5 + $2.',top=580,size=34)
body+=pin(128,700,1664,p('Cents too: 45¢ from a $1 coin.  45¢ → 50¢ is 5¢,  50¢ → $1 is 50¢.  Change 55¢.',34,700),'fade',SOFT,20,'18px 28px')
put(f'{P}-teachchange',sec(f'{P}-teachchange','52–54 MIN',body,'Teach before worksheet page 2 (Q3). Act it out: one child is the shopkeeper and counts the change into Ali’s hand: "33 … 35, 40, 50." The notes given ARE the fewest notes. Check with take-away: $50 − $33 = $17. Watch for children who give $27 (counting the wrong way).'))

# 17 teachenough
items=[('Kite','$7'),('Ball','$5'),('Puzzle','$12'),('Book','$6')]
body=h2('Is there enough? List the pairs')+pin(128,230,1664,tags_svg(items,1100,130,'Price tags: kite $7, ball $5, puzzle $12, book $6'))+pin(1260,240,532,p('Ravi has $15.',44,800),None,SOFT,20,'22px 28px')
body+=step(1,'Kite and puzzle? $7 + $12 = $19. More than $15: $4 short.',left=128,top=400,width=760,size=32)
body+=step(2,'Which pair gives exactly $2 change? $15 − $2 = $13. Find pairs that cost $13.',left=128,top=540,width=760,size=32)
body+=step(3,'List every pair in order. Only kite and book cost $13.',left=128,top=720,width=760,size=32)
WP=[340,200,140]
body+=trow(940,400,['Pair','Cost','$13?'],WP,None,True,30)
for i,r in enumerate([['kite + ball','$12',''],['kite + puzzle','$19',''],['kite + book','$13','yes'],['ball + puzzle','$17',''],['ball + book','$11',''],['puzzle + book','$18','']]): body+=trow(940,474+i*68,r,WP,'rise',size=30)
put(f'{P}-teachenough',sec(f'{P}-teachenough','54–56 MIN',body,'Teach before worksheet page 2 (Q4). "Is there enough?" means: add the prices, then compare with the money. To find ALL the pairs, list them in order: kite with each of the others, then ball with the ones after it, then puzzle with book. 4 things make 6 pairs. Do not do the worksheet prices.'))

# 18 teachlist2
W5=[330,260,400,380]
body=h2('Two kinds of things: make a list')+card(p('Pencils cost 20¢. Erasers cost 30¢. Spend exactly $1. Find all the ways.',40,700))
body+=trow(128,380,['Erasers','Cost','Left for pencils','Pencils'],W5,None,True,34)
for i,r in enumerate([['3','90¢','10¢','not this one'],['2','60¢','40¢','2'],['1','30¢','70¢','not this one'],['0','0¢','100¢','5']]): body+=trow(128,462+i*82,r,W5,'rise',size=34)
body+=pin(128,800,1664,p('Most erasers first, then one fewer each time. 2 ways: 2 erasers + 2 pencils, or 5 pencils.',34,700),'fade',SOFT,20,'18px 28px')
put(f'{P}-teachlist2',sec(f'{P}-teachlist2','56–57 MIN',body,'Teach before worksheet page 2 (Q6 uses stickers and erasers at different prices). Ask for each row: "Can 20¢ pencils make exactly the amount left?" Count in 20s: 20, 40, 60, 80, 100. 10¢ and 70¢ are not in the count, so those rows do not work. Four erasers would cost $1.20, too much, so we start at 3.'))

# 19 ws2, 20 ws2ans
put(f'{P}-ws2',ws_preview(f'{P}-ws2','57–69 MIN','Worksheet page 2: on your own',[('Q3','Change. Count on like a shopkeeper.'),('Q4','Is there enough? Then find ALL the pairs.'),('Q5','Work backwards: put back what was spent.'),('Q6','Stickers and erasers for exactly $2. Make a list in order.')],'Finished early? Stretch and Challenge come next.','Children work alone. Note who needs a short catch-up next lesson. Check that Q6 is a list in order, not guesses.'))
put(f'{P}-ws2ans',check_slide(f'{P}-ws2ans','69–72 MIN','Page 2: check together',[('Q3','a) 35¢     b) $24:  $10 + $10 + $2 + $2'),('Q4','a) No: $14 + $8 = $22, $2 short    b) book + cap,  bag + pen'),('Q5','a) 100¢ = $1.00     b) $20'),('Q6','4 erasers;   2 erasers + 5 stickers;   10 stickers')],
 'Click after a child explains. Q3b: count on $26 → $30 → $40 → $50, or $50 − $26 = $24; no $20 note, so two $10 and two $2. Q4b: she spends $20 − $3 = $17: book + cap = $17, bag + pen = $17; the other four pairs cost $12, $23, $11 and $22. Q5a: 25 + 30 + 45 = 100¢. Q5b: $6 + $4 = $10 is half, so $20. Q6: 1 or 3 erasers leave 150¢ or 50¢, not in the 20¢ count.'))

# 21 stretch (new, not on the worksheet)
st=[('1.','Find all the ways to pay exactly $9 using only $5 and $2 notes.'),('2.','Ali has 3 coins worth 75¢ altogether. Which coins are they? Is there another way?'),('3.','Ben’s mum gave him $5. Then he spent $12 on a game. Now he has $3. How much did he have at first?')]
put(f'{P}-stretch',sec(f'{P}-stretch','For early finishers',h2('Stretch')+qcards(st,38),'For children who finish early. Answers: 1) Only 1 way: $5 + $2 + $2 (without a $5 note, $2 notes make only even amounts, and two $5 notes is $10, too much). 2) 50¢ + 20¢ + 5¢, and there is no other way (we need a 5¢ coin to end in 5, then 70¢ from two coins is only 50¢ + 20¢). 3) $10 ($3 + $12 = $15 before the game; $15 − $5 = $10 before mum gave him money).'))

# 22 challenge
ch=[('1.','Ali has 10 coins. Every coin is a 10¢ or a 20¢ coin. They could be worth $1.50: how many of each is that? Write ALL the totals his 10 coins could be worth. Could they be worth $1.55?'),('2.','Mei has $1. At the snack stall: chips 45¢, sweet 15¢, jelly 25¢, biscuit 30¢, lollipop 20¢. She wants as many DIFFERENT snacks as she can. Which should she buy?')]
put(f'{P}-challenge',sec(f'{P}-challenge','Challenge',h2('Challenge')+qcards(ch,38),'Pairs try first, then the "see it" slide, then the walk-through. Answers: 1) Five 10¢ and five 20¢ (50¢ + 100¢ = 150¢). The totals are $1.00, $1.10, … $2.00 (11 totals, going up 10¢ at a time); $1.55 is not possible because every total is a multiple of 10¢. 2) Sweet, lollipop, jelly and biscuit: 15 + 20 + 25 + 30 = 90¢, with 10¢ change. All five cost $1.35, too much, and any 4 snacks with the chips cost at least $1.05.'))

# 23 chdiag
WT=[230,230,230]
rows=''.join(f'<tr style="background:{YEL if i==0 else WHITE}">'+''.join(f'<td style="border:3px solid {NAVY};padding:10px 16px;text-align:center;font-weight:{800 if i==0 else 600}">{E(c)}</td>' for c in r)+'</tr>' for i,r in enumerate([['10¢ coins','20¢ coins','Total'],['10','0','$1.00'],['9','1','?'],['8','2','?'],['…','…','$1.50 ?']]))
q1='<p style="font-size:28px;font-weight:700;color:#1F7A6F">Q1: Swap one coin at a time</p>'+f'<table style="font-size:34px;border-collapse:collapse;align-self:center">{rows}</table>'+p('Always 10 coins.',30,700,MUTED)
snacks=[('Chips','45¢'),('Sweet','15¢'),('Jelly','25¢'),('Biscuit','30¢'),('Lollipop','20¢')]
sv=f'<svg aria-label="Snack price tags and a $1 coin" viewBox="0 0 760 470" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto">'
for i,(nm,pr) in enumerate(snacks):
    x=(i%2)*380+10; y=(i//2)*120+10
    sv+=f'<polygon points="{x},{y+50} {x+34},{y+6} {x+340},{y+6} {x+340},{y+96} {x+34},{y+96}" fill="{YEL}" stroke="{NAVY}" stroke-width="4" stroke-linejoin="round"/><circle cx="{x+32}" cy="{y+50}" r="8" fill="{CREAM}" stroke="{NAVY}" stroke-width="3"/><text x="{x+60}" y="{y+64}" font-size="34" font-weight="700" fill="{NAVY}" font-family="Nunito Sans, Arial">{nm}</text><text x="{x+320}" y="{y+66}" font-size="40" font-weight="700" text-anchor="end" fill="{NAVY}" font-family="Fredoka, Arial">{pr}</text>'
sv+=f'<circle cx="570" cy="300" r="62" fill="#E8D27A" stroke="{NAVY}" stroke-width="4"/><circle cx="570" cy="300" r="50" fill="none" stroke="{NAVY}" stroke-width="2"/><text x="570" y="316" font-size="44" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="Fredoka, Arial">$1</text>'
sv+=f'<text x="380" y="420" font-size="32" font-weight="700" text-anchor="middle" fill="{TEAL}" font-family="Nunito Sans, Arial">How many different snacks for $1?</text></svg>'
q2='<p style="font-size:28px;font-weight:700;color:#1F7A6F">Q2: The snack stall</p>'+sv
body=h2('Challenge: see it',60)+'<div style="display:flex;gap:32px;align-items:flex-start">'+card(q1,extra='flex:1;min-width:0;padding:20px 24px')+card(q2,extra='flex:1;min-width:0;padding:20px 24px')+'</div>'
put(f'{P}-chdiag',sec(f'{P}-chdiag','Challenge',body,'Show after pairs have tried, or if they are stuck. The pictures show the problem, not the answer. Ask: What changes each time we swap one 10¢ for a 20¢? (The total goes up by 10¢; there are still 10 coins.) For Q2: If you want MANY snacks, which ones should you choose first?'))

# 24 chwalk
body=h2('Challenge: walk-through')+pin(128,250,800,p('Q1: start with all 10¢',38,800,TEAL))
for i,t in enumerate(['Ten 10¢ coins = $1.00','Each swap to a 20¢ adds 10¢','$1.50 is 50¢ more: 5 swaps (5 and 5)','Totals: $1.00, $1.10 … $2.00 (11). $1.55? No ✓']): body+=pin(128,330+i*110,800,p(t,32),'rise',WHITE)
body+=pin(992,250,800,p('Q2: cheapest first',38,800,TEAL))
for i,t in enumerate(['15¢ + 20¢ = 35¢','+ 25¢ = 60¢,  + 30¢ = 90¢','Chips next: 90¢ + 45¢ is too much','4 snacks, 10¢ change ✓']): body+=pin(992,330+i*110,800,p(t,32),'rise',WHITE)
put(f'{P}-chwalk',sec(f'{P}-chwalk','Challenge',body,'Use after pairs have tried. Q1: the swap idea is a list in order (10 and 0, 9 and 1, 8 and 2 …) with the total going up by 10¢ each row. Q2: to get the MOST things, buy the cheapest things first. Ask: "Could she swap the biscuit for the chips?" (15 + 20 + 25 + 45 = 105¢, too much.)'))

# 25 talk, 26 exit
put(f'{P}-talk',talk_slide(f'{P}-talk','Mei says: “To pay $40 with the fewest notes, I use two $20 notes.” What would you tell her?','Minutes 72 to 80. Pairs talk for 2 minutes, then share. Answer: there is no $20 note in Singapore. $50 is too much, so we use four $10 notes. Follow-up: "What about $45?" ($10 + $10 + $10 + $10 + $5, 5 notes.) Praise the reasons, not only the answers.'))
put(f'{P}-exit',exit_slide(f'{P}-exit','A pen costs $3.65. Pay exactly with the fewest notes and coins.','Minutes 80 to 90. Answer: $2 + $1 + 50¢ + 10¢ + 5¢ (5 pieces). Extension: find every way to pay exactly $10 using $5 notes, $2 notes and $1 coins (there are 10).'))

order=['title','warm1','warm2','explore1','explore2','teach1','we1','try1','we2','try2','key','break','teachfew','ws1','ws1ans','teachchange','teachenough','teachlist2','ws2','ws2ans','stretch','challenge','chdiag','chwalk','talk','exit']
order=[f'{P}-{x}' for x in order]
assert set(order)==set(S), set(order)^set(S)
for f in os.listdir(os.path.join(D,'slides')):
    if f.endswith('.html') and f[:-5] not in S: os.remove(os.path.join(D,'slides',f))
for i,h in S.items(): open(os.path.join(D,'slides',i+'.html'),'w').write(h)
deck={'v':4,'createdOnFiles':{'v':1,'at':'2026-10-21T08:00:00Z'},'lists':'css','title':f'Math Inquirers P2: Lesson {N} – Market Day','order':order,'cover':order[0],
 'sections':{'s1':{'description':'Warm-up and explore','start':f'{P}-title'},'s2':{'description':'Teach: dollars and cents, lists in order, working backwards','start':f'{P}-teach1'},'s3':{'description':'Worksheet with teaching before each page','start':f'{P}-break'},'s4':{'description':'Stretch, challenge, talk and exit','start':f'{P}-stretch'}},
 'faces':{'fredoka':{'family':'Fredoka','href':'https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&display=swap'},'nunito-sans':{'family':'Nunito Sans','href':'https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@400;600;700&display=swap'}},'designSystems':[]}
json.dump(deck,open(os.path.join(D,'deck.json'),'w'),indent=1,ensure_ascii=False)
print(len(order),'slides')
