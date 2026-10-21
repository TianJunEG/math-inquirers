"""Math Inquirers P2, Lesson 9: Measure Masters. Writes split/p2l9/project (deck.json + slides/*.html)."""
import json,os,sys,math,shutil,datetime
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,H)
from slidekit import *
D=os.path.join(H,'..','split','p2l9','project'); S={}
def put(i,h): S[i]=h
RED='#D64545'; ORANGE='#F28C38'; GREEN='#BFE3DC'; PINK='#F4A6A6'; BLUE='#9CC9EE'

# ---------- generic helpers (P2 decks) ----------
def svg(w,h,body,aria,style=''): return f'<svg aria-label="{E(aria)}" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="width:{w}px;height:{h}px;{style}">{body}</svg>'
def T(x,y,s,size=30,fill=NAVY,anchor='middle',weight=800,font='Nunito Sans, Arial'): return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" fill="{fill}" font-family="{font}">{E(str(s))}</text>'
def title_slide(sid,n,title,sub,today,notes):
    return (f'<section id="{sid}" data-transition="fade" style="background:{NAVY};color:{CREAM};font-family:{BF};padding:128px 128px 160px;display:flex;flex-direction:column;justify-content:center;gap:36px">\n'
            f'<p style="font-size:32px;font-weight:700;letter-spacing:4px;color:{YEL}">PRIMARY 2  •  LESSON {n}  •  WEEK 5</p>\n'
            f'<h1 style="font-family:{HF};font-size:128px;font-weight:600;line-height:1.05">{E(title)}</h1>\n<p style="font-size:44px;color:#C9D4EC">{E(sub)}</p>\n'
            f'<div style="background:#26385F;border-radius:24px;padding:40px;display:flex;flex-direction:column;gap:12px"><p style="font-size:28px;font-weight:700;letter-spacing:3px;color:{YEL}">TODAY WE WILL</p><p style="font-size:44px;font-weight:600">{E(today)}</p></div>\n'
            f'<p style="position:absolute;left:128px;bottom:64px;width:1400px;font-size:24px;color:#B7C3DD">{E(FOOT)}</p>\n<aside>{E(notes)}</aside>\n</section>\n')
def break_slide(sid,text,sub,notes):
    return (f'<section id="{sid}" data-transition="fade" style="background:{TEAL};color:{CREAM};font-family:{BF};padding:128px 128px 160px;display:flex;flex-direction:column;justify-content:center;gap:36px">\n'
            f'<p style="font-size:32px;font-weight:700;letter-spacing:4px;color:{YEL}">32–36 MIN</p>\n<h2 style="font-family:{HF};font-size:110px;font-weight:600;line-height:1.05">Brain break</h2>\n'
            f'<p style="font-size:48px;font-weight:600">{E(text)}</p>\n<p style="font-size:36px;color:#D7EFEA">{E(sub)}</p>\n'
            f'<p style="position:absolute;left:128px;bottom:64px;width:1400px;font-size:24px;color:#D7EFEA">{E(FOOT)}</p>\n<aside>{E(notes)}</aside>\n</section>\n')
def numcards(items,size=36):
    return ''.join(card(p(f'<span style="color:{TEAL}">{a}</span>  {E(b)}',size,600,raw=True)) for a,b in items)
def quick(sid,time,qs,notes,step=125,size=36):
    body=h2('Quick questions')+''.join(qrow(128,250+i*step,1250,a,b,size) for i,(a,b,c) in enumerate(qs))+''.join(answer(1420,250+i*step,372,c) for i,(a,b,c) in enumerate(qs))
    return sec(sid,time,body,notes)
def talk_slide(sid,q,notes):
    body=h2('Talk time')+card(chip('TALK TIME',YEL,NAVY)+p(q,42,600))+card(p('Sentence starters:',34,400,MUTED)+p('“I started by …”   “I noticed that …”   “I know because …”',38,600))
    return sec(sid,'72–80 MIN',body,notes)
def exit_slide(sid,q,a,notes,time='80–90 MIN'):
    body=h2('Exit ticket')+card(chip('EXIT TICKET')+p(q,46,600))+card(p('Write your answer and how you know on a slip of paper. Show it to your tutor, then collect your stamp.',34,400))
    body+=answer(128,760,1664,'Answer: '+a)
    return sec(sid,time,body,notes)
def write_deck(lesson_title,order,sections):
    sd=os.path.join(D,'slides')
    if os.path.isdir(sd): shutil.rmtree(sd)
    os.makedirs(sd)
    for i in order: open(os.path.join(sd,i+'.html'),'w').write(S[i])
    deck={'v':4,'createdOnFiles':{'v':1,'at':datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')},'lists':'css','title':lesson_title,'order':order,'cover':order[0],'sections':sections,
          'faces':{'fredoka':{'family':'Fredoka','href':'https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&display=swap'},'nunito-sans':{'family':'Nunito Sans','href':'https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@400;600;700&display=swap'}},'designSystems':[]}
    json.dump(deck,open(os.path.join(D,'deck.json'),'w'),indent=1,ensure_ascii=False)
    missing=[i for i in S if i not in order]
    print(len(order),'slides', 'UNUSED:'+','.join(missing) if missing else '')

# ---------- drawings for this lesson ----------
def item(k,x,base,u=1.0):
    """draw one thing sitting on a pan; returns (svg, width)"""
    if k=='pine':
        w=56*u; cx=x+w/2
        g=f'<path d="M{cx} {base-74*u} l-12 {-22*u} l10 {8*u} l2 {-18*u} l6 {16*u} l8 {-14*u} l0 {22*u} Z" fill="{TEAL}" stroke="{NAVY}" stroke-width="3"/><ellipse cx="{cx}" cy="{base-36*u}" rx="{26*u}" ry="{36*u}" fill="{YEL}" stroke="{NAVY}" stroke-width="3"/><path d="M{cx-18*u} {base-58*u} L{cx+18*u} {base-14*u} M{cx+18*u} {base-58*u} L{cx-18*u} {base-14*u} M{cx-24*u} {base-36*u} L{cx} {base-6*u} M{cx+24*u} {base-36*u} L{cx} {base-66*u}" stroke="#B9770E" stroke-width="2.5" fill="none"/>'
        return g,w
    if k=='orange':
        w=40*u; return f'<circle cx="{x+w/2}" cy="{base-w/2}" r="{w/2}" fill="{ORANGE}" stroke="{NAVY}" stroke-width="3"/><circle cx="{x+w/2+6*u}" cy="{base-w/2-7*u}" r="{3*u}" fill="#FFF0C2"/>',w
    if k=='water':
        w=120*u; cx=x+w/2; cy=base-40*u
        return f'<ellipse cx="{cx}" cy="{cy}" rx="{60*u}" ry="{40*u}" fill="{TEAL}" stroke="{NAVY}" stroke-width="3"/>'+''.join(f'<path d="M{cx+d*u} {cy-38*u} Q{cx+d*u*1.35} {cy} {cx+d*u} {cy+38*u}" stroke="#7FD1C3" stroke-width="5" fill="none"/>' for d in (-30,0,30)),w
    if k=='bag':
        w=44*u; return f'<path d="M{x+4*u} {base} L{x+2*u} {base-44*u} L{x+10*u} {base-54*u} L{x+w-10*u} {base-54*u} L{x+w-2*u} {base-44*u} L{x+w-4*u} {base} Z" fill="{WHITE}" stroke="{NAVY}" stroke-width="3"/><rect x="{x+8*u}" y="{base-36*u}" width="{w-16*u}" height="{14*u}" fill="{BLUE}"/>',w
    if k.startswith('w:'):
        lab=k[2:]; w=max(78,len(lab)*19+30)*u
        return f'<path d="M{x} {base} L{x+8*u} {base-48*u} L{x+w-8*u} {base-48*u} L{x+w} {base} Z" fill="{GREY}" stroke="{NAVY}" stroke-width="3"/>'+T(x+w/2,base-14*u,lab,max(26,int(28*u))),w
    if k=='cube':
        w=46*u; return f'<rect x="{x}" y="{base-w}" width="{w}" height="{w}" rx="5" fill="{YEL}" stroke="{NAVY}" stroke-width="3"/>',w
    if k=='ball':
        w=58*u; return f'<circle cx="{x+w/2}" cy="{base-w/2}" r="{w/2}" fill="{BLUE}" stroke="{NAVY}" stroke-width="3"/><path d="M{x+4*u} {base-w/2} Q{x+w/2} {base-w/2+16*u} {x+w-4*u} {base-w/2}" stroke="{NAVY}" stroke-width="2.5" fill="none"/>',w
    return '',0
def balance(left,right,arm=230,u=1.0,aria='',W=None,Hh=230):
    """pan balance, level. left/right: lists of item kinds"""
    W=W or int(2*arm+260*u); cx=W/2; by=Hh-80
    def pan(px,items):
        ws=[item(k,0,0,u)[1] for k in items]; tot=sum(ws)+6*(len(ws)-1); x=px-tot/2; out=''
        for k in items: g,w=item(k,x,by-10,u); out+=g; x+=w+6
        pw=max(150*u,tot+30)
        return out+f'<path d="M{px-pw/2} {by-10} L{px+pw/2} {by-10} L{px+pw/2-16} {by+6} L{px-pw/2+16} {by+6} Z" fill="{SKY}" stroke="{NAVY}" stroke-width="3"/>'
    b=pan(cx-arm,left)+pan(cx+arm,right)
    b+=f'<rect x="{cx-arm}" y="{by+6}" width="{2*arm}" height="12" rx="6" fill="{NAVY}"/><polygon points="{cx},{by-6} {cx-14},{by+14} {cx+14},{by+14}" fill="{YEL}" stroke="{NAVY}" stroke-width="3"/><rect x="{cx-8}" y="{by+18}" width="16" height="44" fill="{NAVY}"/><rect x="{cx-70}" y="{by+60}" width="140" height="16" rx="6" fill="{NAVY}"/>'
    return svg(W,Hh,b,aria or 'A level balance')
def jug_svg(caps,fills=None,W=560,Hh=230,aria='Jugs'):
    """caps: list of (litres,label); fills: litres of water in each jug (drawn as a level, no marks)"""
    b=''; x=40; maxc=max(c for c,_ in caps)
    for i,(c,lab) in enumerate(caps):
        h=50+100*c/maxc; w=70+40*c/maxc; base=Hh-46
        if fills and fills[i]: fh=h*fills[i]/c; b+=f'<rect x="{x}" y="{base-fh}" width="{w}" height="{fh}" fill="{BLUE}"/>'
        b+=f'<path d="M{x} {base-h} L{x} {base} L{x+w} {base} L{x+w} {base-h}" fill="none" stroke="{NAVY}" stroke-width="5"/><path d="M{x+w} {base-h+16} q30 6 30 {h/3} q0 {h/4} -30 {h/3}" fill="none" stroke="{NAVY}" stroke-width="5"/><path d="M{x} {base-h} l-16 -12" stroke="{NAVY}" stroke-width="5"/>'
        b+=T(x+w/2,base+38,lab,32)
        x+=w+110
    return svg(W,Hh,b,aria)
def clock_svg(h,m,R=150,aria=None):
    W=2*R+20; c=W/2; b=f'<circle cx="{c}" cy="{c}" r="{R}" fill="{WHITE}" stroke="{NAVY}" stroke-width="8"/>'
    for i in range(12):
        a=i*math.pi/6; b+=f'<line x1="{c+(R-26)*math.sin(a):.1f}" y1="{c-(R-26)*math.cos(a):.1f}" x2="{c+(R-6)*math.sin(a):.1f}" y2="{c-(R-6)*math.cos(a):.1f}" stroke="{NAVY}" stroke-width="5"/>'
        n=i if i else 12; b+=T(f'{c+(R-50)*math.sin(a):.1f}',f'{c-(R-50)*math.cos(a)+12:.1f}',n,34,font='Fredoka, Arial')
    ha=((h%12)*30+m*0.5)*math.pi/180; ma=m*6*math.pi/180
    b+=f'<line x1="{c}" y1="{c}" x2="{c+R*0.48*math.sin(ha):.1f}" y2="{c-R*0.48*math.cos(ha):.1f}" stroke="{NAVY}" stroke-width="16" stroke-linecap="round"/>'
    b+=f'<line x1="{c}" y1="{c}" x2="{c+R*0.8*math.sin(ma):.1f}" y2="{c-R*0.8*math.cos(ma):.1f}" stroke="{RED}" stroke-width="9" stroke-linecap="round"/><circle cx="{c}" cy="{c}" r="12" fill="{NAVY}"/>'
    return svg(W,W,b,aria or f'Clock showing {h}:{m:02d}')
def timeline(points,jumps=None,W=1100,Hh=170,aria='Time line',show=True):
    """points: list of (x_fraction,label); jumps: list of (i,j,text) arcs between point i and j"""
    X=lambda f: 40+f*(W-80); b=''
    if show:
        b+=f'<line x1="30" y1="110" x2="{W-30}" y2="110" stroke="{NAVY}" stroke-width="5"/>'
        for f,lab in points: b+=f'<line x1="{X(f)}" y1="94" x2="{X(f)}" y2="126" stroke="{NAVY}" stroke-width="5"/>'+T(X(f),162,lab,30)
    for i,j,t in (jumps or []):
        a,c=X(points[i][0])+6,X(points[j][0])-6
        b+=f'<path d="M{a} 100 Q{(a+c)/2} 30 {c} 100" fill="none" stroke="{TEAL}" stroke-width="5"/>'+T((a+c)/2,48,t,28,TEAL)
    return svg(W,Hh,b,aria)

# ---------- 1. title ----------
put('p2l9-title',title_slide('p2l9-title',9,'Measure Masters','Length, mass, volume and time','Solve balance, jug and ribbon puzzles, and work out times and how long things take.',
 'Objective: Solve balance-scale puzzles in g and kg by swapping things that balance; solve pouring puzzles with litre jugs by keeping a table of every pour; join and cut lengths in m and cm (overlaps, pieces and cuts); tell the time to 5 minutes with a.m. and p.m. and find start times, end times and how long, also across the hour. '
 'Materials: A coat hanger, two paper cups, string, a glue stick, a spoon and about 20 20¢ coins (a home-made balance; backup: a ruler balanced on a pencil); for the jug puzzles two cups or bottles of different size (about 3 and 5 units), a jug of dry rice or sand (or water), and tape marking 3 and 5 units; a cardboard clock with hands; mini whiteboards. '
 'Online: Children build the coat-hanger balance before the lesson and hold it up to the camera. Share the slide balances, jugs and clocks and annotate on screen. Each child needs a cardboard or paper-plate clock. For the pouring puzzles use dry rice or sand rather than water when online, and let children act out each pour with the two containers. '
 'Time plan: warm-up 0 to 8, explore 8 to 20 (explore2 talk is 6 minutes), teaching 20 to 32 (balance puzzles and jug puzzles; click to reveal each step and answer), brain break 32 to 36, worksheet page 1 36 to 50 then check together 50 to 52, short teaching 52 to 57, worksheet page 2 57 to 69 then check together 69 to 72, talk time 72 to 80, exit ticket 80 to 90.'))

# ---------- 2. warm-up game: which unit? ----------
def icon(k):
    N=NAVY
    g={'door':f'<rect x="40" y="10" width="80" height="140" rx="4" fill="{WOODC}" stroke="{N}" stroke-width="4"/><circle cx="105" cy="84" r="6" fill="{N}"/>',
       'pencil':f'<g transform="rotate(-30 80 80)"><rect x="10" y="64" width="110" height="32" fill="{YEL}" stroke="{N}" stroke-width="4"/><polygon points="120,64 152,80 120,96" fill="#F3D9B1" stroke="{N}" stroke-width="4"/><rect x="0" y="64" width="16" height="32" fill="{PINK}" stroke="{N}" stroke-width="4"/></g>',
       'rice':f'<path d="M36 150 L30 50 L50 26 L110 26 L130 50 L124 150 Z" fill="{WHITE}" stroke="{N}" stroke-width="4"/><rect x="44" y="76" width="72" height="40" fill="{SKY}" stroke="{N}" stroke-width="3"/>'+T(80,106,'RICE',27),
       'straw':f'<path d="M80 150 Q30 110 40 64 Q80 44 120 64 Q130 110 80 150 Z" fill="{RED}" stroke="{N}" stroke-width="4"/><path d="M50 60 L80 36 L110 60 L80 54 Z" fill="{TEAL}" stroke="{N}" stroke-width="3"/>'+''.join(f'<circle cx="{x}" cy="{y}" r="3" fill="#FFF0C2"/>' for x,y in [(66,80),(92,82),(78,104),(62,112),(98,110),(80,128)]),
       'bucket':f'<path d="M30 50 L130 50 L116 150 L44 150 Z" fill="{BLUE}" stroke="{N}" stroke-width="4"/><path d="M30 50 Q80 0 130 50" fill="none" stroke="{N}" stroke-width="4"/><path d="M40 72 L120 72" stroke="{WHITE}" stroke-width="5"/>',
       'brush':f'<g transform="rotate(-25 80 80)"><rect x="6" y="74" width="120" height="16" rx="8" fill="{TEAL}" stroke="{N}" stroke-width="4"/><rect x="104" y="52" width="44" height="24" rx="4" fill="{WHITE}" stroke="{N}" stroke-width="4"/></g>'}[k]
    return f'<svg aria-label="{k}" viewBox="0 0 160 160" xmlns="http://www.w3.org/2000/svg" style="width:150px;height:150px;flex:none">{g}</svg>'
WOODC='#D9B38C'
things=[('door','A classroom door: how tall?','m'),('pencil','A pencil: how long?','cm'),('rice','A big bag of rice: how heavy?','kg'),('straw','A strawberry: how heavy?','g'),('bucket','A bucket of water: how much water?','ℓ'),('brush','Brushing your teeth: how long?','minutes')]
body=h2('Warm-up: which unit?')+p('Write m, cm, kg, g, ℓ or minutes on your whiteboard. Then say why.',34,600,MUTED)
CW=533
for i,(k,t,a) in enumerate(things):
    L=128+(i%3)*(CW+32); Tp=280+(i//3)*310
    body+=pin(L,Tp,CW,f'<div style="display:flex;align-items:center;gap:18px">{icon(k)}<p style="font-size:34px;font-weight:700;line-height:1.2">{E(t)}</p></div>',None,WHITE,24,'14px 20px',f'box-sizing:border-box;height:280px;border:4px solid {NAVY};box-shadow:8px 8px 0 {NAVY}')
    body+=pin(L+300,Tp+196,CW-330,f'<p style="font-size:40px;font-weight:800;text-align:center">{E(a)}</p>','pop',YEL,16,'8px 14px',f'box-sizing:border-box;border:3px solid {NAVY}')
put('p2l9-warm1',sec('p2l9-warm1','0–5 MIN',body,'Minutes 0 to 5. Which unit? Point to one card at a time. Children write the unit on whiteboards and hold them up on three. Then click to show the unit (clicks reveal door, pencil, rice, strawberry, bucket, brushing teeth in order). '
 'Answers: door m (about 2 m), pencil cm, bag of rice kg, strawberry g, bucket of water ℓ, brushing teeth minutes (about 2 minutes). Ask "Why not grams for the rice?" (the number would be very big; kilograms are the bigger unit) and "Why not metres for the pencil?" (a pencil is much shorter than 1 m). '
 'Quick finisher: "Name something you would measure in litres at home." (a bottle of water, a pot of soup, a fish tank). Watch for children who mix up length and mass: "Is a heavy thing always long?"'))

# ---------- 3. quick questions ----------
qs=[('1.','35 cm + 40 cm = ?','75 cm'),('2.','The minute hand points to 6. How many minutes past the hour?','30 min'),('3.','A 5 ℓ bucket has 2 ℓ of water. How much more fills it?','3 ℓ'),('4.','Lunch at 12:30. Is it a.m. or p.m.?','p.m.'),('5.','One bag of rice is 5 kg. How heavy are 2 bags?','10 kg')]
put('p2l9-warm2',quick('p2l9-warm2','5–8 MIN',qs,'Minutes 5 to 8. Read each question aloud, give thinking time, take answers, then click to show. Ask "How do you know?" each time. Answers: 1) 75 cm (30 + 40 = 70, 5 more). 2) 30 minutes (count in 5s from 12 to 6: 5, 10, 15, 20, 25, 30; or half past). 3) 3 ℓ (count on from 2 to 5). 4) p.m.: 12 noon to 12 midnight is p.m., so half past twelve at lunchtime is p.m. Many children say a.m.; draw a day line from midnight to midnight and mark noon. 5) 10 kg (5 + 5).',size=34))

# ---------- 4. explore ----------
hanger=(f'<path d="M80 150 L300 70 L520 150 Z" fill="none" stroke="{NAVY}" stroke-width="6" stroke-linejoin="round"/><path d="M300 70 L300 46 Q300 20 324 20 Q346 22 344 42" fill="none" stroke="{NAVY}" stroke-width="6"/>'
        f'<line x1="90" y1="150" x2="90" y2="230" stroke="{NAVY}" stroke-width="3"/><line x1="510" y1="150" x2="510" y2="230" stroke="{NAVY}" stroke-width="3"/>'
        f'<path d="M40 230 L140 230 L126 330 L54 330 Z" fill="{WHITE}" stroke="{NAVY}" stroke-width="4"/><path d="M460 230 L560 230 L546 330 L474 330 Z" fill="{WHITE}" stroke="{NAVY}" stroke-width="4"/>'
        f'<rect x="76" y="168" width="28" height="90" rx="6" fill="{YEL}" stroke="{NAVY}" stroke-width="3" transform="rotate(12 90 213)"/>'
        +''.join(f'<ellipse cx="{510+dx}" cy="{318-j*9}" rx="22" ry="7" fill="#E5E9F2" stroke="{NAVY}" stroke-width="2.5"/>' for j,dx in enumerate([0,-4,4,-2,2,0,-3,3]))
        +T(90,370,'glue stick',28)+T(510,370,'20¢ coins',28))
exp=svg(600,390,hanger,'A coat hanger balance: a glue stick in one cup and a pile of 20 cent coins in the other, and the hanger is level')
steps=['Hang two paper cups from a coat hanger. Check it is level when the cups are empty.','Put a glue stick in one cup. Guess: how many 20¢ coins will balance it?','Add coins one at a time until the hanger is level. Then try a spoon.','Which is heavier, the glue stick or the spoon? How do you know?']
body=h2('Explore: balance lab')+pin(128,250,1000,chip('EXPLORE')+'<ol style="font-size:34px;font-weight:600;padding-left:48px;display:flex;flex-direction:column;gap:14px;line-height:1.3">'+''.join(f'<li>{E(s)}</li>' for s in steps)+'</ol>',None,WHITE,24,'28px 36px')
body+=pin(1180,250,612,exp,None,WHITE,24,'6px 6px')
put('p2l9-explore1',sec('p2l9-explore1','8–14 MIN',body,'Minutes 8 to 14. Pairs build or use their coat-hanger balance. Online: children hold their balance up to the camera; if a child has none, they balance two objects in their hands and guess which is heavier, then check on a kitchen scale with an adult. '
 'Say: "Before you add any coins, write your guess." Walk round and ask: "How do you know it is level?" "What happens if you add one more coin?" Do not teach the swapping idea yet: let children notice that the number of coins tells us how heavy the object is.'))
qs=[('1.','How many coins balanced your glue stick? Your spoon?'),('2.','A glue stick balances 8 coins. A spoon balances 5 coins. Which is heavier?'),('3.','Your partner used erasers and got a different number. Why?')]
put('p2l9-explore2',sec('p2l9-explore2','14–20 MIN',h2('Explore: talk about it')+numcards(qs,40),'Minutes 14 to 20. Let pairs keep testing, then gather to answer these one at a time. What we want them to notice: when the balance is level, the two sides are equally heavy, so the coins tell us how heavy the object is in "coins". '
 'Answers: 1) Open: compare with other pairs. 2) The glue stick: it needs more of the same coin to balance. 3) Erasers and coins are different units (an eraser is not as heavy as a coin), so the numbers are different. To compare, use the same unit. Follow-up: "If the glue stick balances 8 coins and 2 glue sticks are on one side, how many coins balance them?" (16).'))

# ---------- 6. teach: level balance, swap ----------
b1=balance(['pine'],['orange']*3,arm=200,W=820,aria='A pineapple balances 3 oranges')
b2=balance(['pine'],['w:200 g']*3,arm=200,u=0.9,W=820,aria='The pineapple balances three 200 g weights')
body=h2('A level balance: swap it')+card(p('A level balance means both sides are equally heavy.',40,700))
body+=pin(128,350,820,b1)+pin(128,620,820,b2,'fade')
body+=step(1,'1 pineapple balances 3 oranges. Each orange is 200 g.',left=1000,top=350,width=792,size=32)
body+=step(2,'Swap each orange for a 200 g weight. The balance stays level.',left=1000,top=500,width=792,size=32)
body+=step(3,'200, 400, 600. The pineapple is 600 g.',left=1000,top=650,width=792,size=32)
body+=pin(1000,790,792,p('Why? Things that balance are equally heavy, so we can swap them.',30,700),'fade',SOFT,20,'14px 26px')
put('p2l9-teach1',sec('p2l9-teach1','20–22 MIN',body,'Teach: the idea and why. Hold up the coat-hanger balance: "Level means both sides are equally heavy." Click 1: "1 pineapple balances 3 oranges. Each orange is 200 g. How heavy is the pineapple?" Let children guess first. Click 2: "If one orange is just as heavy as a 200 g weight, I can take the orange off and put the weight on instead. Is it still level?" (Yes.) Click 3 shows the weights. Click 4: count on in 200s: 200, 400, 600. Click 5: the why. '
 'Think-aloud: "The scale is level, so both sides are the same. I swap each orange for what it balances. The scale stays level, so the pineapple is 600 g." Common mistake: adding the two sides together (pineapple + oranges). Ask: "Does a level balance tell us the two sides are the same or that we add them?"'))

# ---------- 7. worked example: three scales ----------
bw=530
sa=balance(['water'],['pine']*3,arm=150,u=0.7,W=bw,Hh=190,aria='Scale A: a watermelon balances 3 pineapples')
sb=balance(['pine'],['w:2 kg'],arm=130,u=0.8,W=bw,Hh=190,aria='Scale B: a pineapple balances a 2 kg weight')
sc=balance(['water'],['pine','bag','bag','bag','bag'],arm=150,u=0.7,W=bw,Hh=190,aria='Scale C: a watermelon balances 1 pineapple and 4 bags of sugar')
body=h2('Worked example: three scales',62)
for i,(lab,s) in enumerate([('A',sa),('B',sb),('C',sc)]): body+=pin(128+i*567,220,530,p('Scale '+lab,30,800,TEAL)+s,None,WHITE,20,'8px 0px',extra='align-items:center')
body+=step(1,'Start with the scale that has a number. Scale B: 1 pineapple = 2 kg.',top=500,size=32)
body+=step(2,'Scale A: swap each pineapple for 2 kg.  2 + 2 + 2 = 6.  The watermelon is 6 kg.',top=600,size=32)
body+=step(3,'Scale C: 6 kg = 2 kg + 4 bags.  So the 4 bags are 6 − 2 = 4 kg.',top=700,size=32)
body+=step(4,'4 bags make 4 kg, so 1 bag is 1 kg.  Check: 2 + 1 + 1 + 1 + 1 = 6 ✓',top=800,size=32)
put('p2l9-we1',sec('p2l9-we1','22–26 MIN',body,'Worked example. Ask first: "Which scale should we start with? Why?" (the one with a number). Before each click, ask the group to predict. '
 'Think-aloud: "A watermelon balances 3 pineapples. One pineapple balances a 2 kg weight. The scale is level, so both sides are equally heavy. I can swap each pineapple for 2 kg: 2, 4, 6. The watermelon is 6 kg. Now the watermelon balances one pineapple and 4 bags of sugar. The watermelon is 6 kg and the pineapple is 2 kg, so the bags must be the rest: 6 − 2 = 4 kg. 4 bags make 4 kg, so each bag is 1 kg. I check scale C: 2 + 1 + 1 + 1 + 1 = 6 ✓." '
 'Common mistake in step 3: adding 6 + 2. Point to scale C: "The watermelon is on one side, the pineapple and the bags are on the other. The bags are what is left after the pineapple."'))

put('p2l9-try1',try_slide('p2l9-try1','26–27 MIN','Your turn: whiteboards','Find the scale with a number first. Then swap.',[('a','1 bag of flour balances 4 apples. Each apple is 100 g. How heavy is the flour?','400 g'),('b','2 cups balance 1 jug. The jug is 300 g. How heavy is 1 cup?','150 g'),('c','1 box balances 2 balls. 1 box and 1 ball balance 600 g. How heavy is 1 ball?','200 g')],
 'Whiteboards up together, then click. a) 100, 200, 300, 400: 400 g. b) Two cups share 300 g equally: 150 + 150 = 300, so 150 g. c) Swap the box for 2 balls: 3 balls balance 600 g, so 1 ball is 200 g (200 + 200 + 200 = 600) and the box is 400 g. Check: 400 + 200 = 600 ✓. For c, a child who writes 300 has shared 600 between the box and the ball as if they were the same: ask "Is the box as heavy as one ball?"',34))

# ---------- 9. worked example: jugs ----------
W4=[110,420,160,160]
rows=[['Start','',  '0 ℓ','0 ℓ'],['1','Fill the 9 ℓ jug','0 ℓ','9 ℓ'],['2','Pour 9 ℓ jug into 4 ℓ jug','4 ℓ','5 ℓ'],['3','Empty the 4 ℓ jug','0 ℓ','5 ℓ'],['4','Pour 9 ℓ jug into 4 ℓ jug','4 ℓ','1 ℓ']]
body=h2('Jug puzzle: keep a table')+p('A 4 ℓ jug and a 9 ℓ jug have no marks. Get exactly 1 ℓ.',36,700)
body+=trow(128,300,['Step','What I do','4 ℓ jug','9 ℓ jug'],W4,None,True,32)
for i,r in enumerate(rows): body+=trow(128,370+i*70,r,W4,None if i==0 else 'rise',False,32)
body+=pin(1240,300,552,p('You can:',32,800,TEAL)+p('fill a jug from the tap,',30,600)+p('empty a jug into the sink,',30,600)+p('pour from one jug into the other until one is full or the other is empty.',30,600),None,WHITE,20,'18px 26px')
body+=pin(1240,620,552,jug_svg([(4,'4 ℓ'),(9,'9 ℓ')],[0,1],W=552,Hh=210,aria='The 4 litre jug is empty and the 9 litre jug has 1 litre left'),'fade')
body+=answer(128,750,1000,'1 ℓ is left in the 9 ℓ jug.  9 − 4 − 4 = 1 ✓')
put('p2l9-we2',sec('p2l9-we2','27–30 MIN',body,'Worked example (a jug puzzle). Use two real cups if you have them. Read the rules on the right first. Click to reveal each row; before each click ask "What could we do next?" '
 'Think-aloud: "I want exactly 1 ℓ. I fill the 9 ℓ jug. I pour into the 4 ℓ jug until it is full: 9 − 4 = 5 left. I empty the 4 ℓ jug and pour again: 5 − 4 = 1. I write every pour in a table so I can check it, and so I can find my way back if I get lost." '
 'Stress: after each step write how much is in EACH jug. Common mistake: "pour half". We cannot pour half: there are no marks, so a pour only stops when one jug is full or the other is empty.'))

put('p2l9-try2',try_slide('p2l9-try2','30–31 MIN','Your turn: a 2 ℓ jug and a 5 ℓ jug','Draw a table. Write how much is in each jug after every step.',[('a','Get exactly 3 ℓ.','5 − 2 = 3'),('b','Get exactly 1 ℓ.','5 − 2 − 2 = 1'),('c','Get exactly 4 ℓ in the 5 ℓ jug.','2 + 2 = 4')],
 'Whiteboards, then click. Write the jugs as (2 ℓ jug, 5 ℓ jug). a) Fill 5 (0, 5); pour into 2 (2, 3): 3 ℓ in the 5 ℓ jug. b) Carry on: empty 2 (0, 3); pour into 2 (2, 1): 1 ℓ. c) Fill 2 (2, 0); pour into 5 (0, 2); fill 2 (2, 2); pour into 5 (0, 4): 4 ℓ. Point out that c ADDS jugs (2 + 2) while a and b TAKE AWAY (5 − 2). Ask: "Which way would get 6 ℓ?" (none: no jug holds 6 ℓ).',36))

# ---------- 11. key ----------
body=h2('Key idea: same on both sides')+card(p('A level balance means both sides are equally heavy, so you can swap.',46,700))+card(p('For jugs, write every pour in a table: how much is in each jug.',38,600,MUTED))
put('p2l9-key',sec('p2l9-key','31–32 MIN',body,'Say the key idea together. Common mistakes to watch for during the worksheet: (1) Balance puzzles: adding the masses on the two sides instead of using "both sides are the same". (2) Q1c: forgetting to take the apple away before sharing among the lemons. (3) Jug puzzles: writing "pour" without how much is in each jug, so the steps cannot be checked; or "pouring half". (4) Time: counting on past the hour as if there were 100 minutes in an hour (4:50 + 35 minutes written as 4:85 or 5:85).'))

put('p2l9-break',break_slide('p2l9-break','Be a balance! Stand on one leg with your arms out.','The tutor calls “heavy left!” or “heavy right!”: tip that way, then come back level.','Four minutes. Online: children stay in view of the camera. Finish with a drink of water.'))

put('p2l9-ws1',ws_preview('p2l9-ws1','36–50 MIN','Worksheet page 1: with your partner',[('Q1','Three balance scales. Start with the scale that has a number. Swap.'),('Q2','A 3 ℓ jug and a 5 ℓ jug. Get 2 ℓ, then 1 ℓ. Write each step.')],'Stuck? Act it out with two cups, or draw the jugs after every pour.','Minutes 36 to 50. Walk around. Ask "Which scale has a number?" and "How much is in each jug now?" before giving any help. Q1c: the melon is 400 g and the apple is 200 g, so the 4 lemons share the other 200 g. Q2b: children who are stuck can act it out with cups marked "3" and "5" and water or rice.'))
put('p2l9-ws1ans',check_slide('p2l9-ws1ans','50–52 MIN','Page 1: check together',[('Q1','a) 200 g   b) 400 g   c) 50 g   d) 8 lemons'),('Q2a','Fill 5 ℓ, pour into 3 ℓ: 2 ℓ left in the 5 ℓ jug'),('Q2b','Fill 3 ℓ, pour into 5 ℓ. Again: 1 ℓ left in the 3 ℓ jug')],
 'Click each answer after a pair explains theirs. Q1: scale 2: apple = 100 + 100 = 200 g. Scale 1: melon = 2 apples = 400 g. Scale 3: melon 400 g = apple 200 g + 4 lemons, so the lemons are 200 g and each lemon is 50 g (50 + 50 + 50 + 50 = 200). d) 400 g is 8 lots of 50 g; or: the apple is 4 lemons (scale 3 with scale 1), so the melon is 4 + 4 = 8 lemons. '
 'Q2a: (3 ℓ jug, 5 ℓ jug) fill 5: (0, 5); pour: (3, 2). Q2b: fill 3: (3, 0); pour: (0, 3); fill 3: (3, 3); pour until the 5 ℓ jug is full, only 2 ℓ fit: (1, 5). Say: "Keep this! Q3 on the next page starts from here."'))

# ---------- teach before page 2: ribbons ----------
U=8
red=f'<rect x="20" y="40" width="{52*U}" height="44" rx="8" fill="{RED}" stroke="{NAVY}" stroke-width="4"/>'+T(20+52*U/2,72,'52 cm',30,WHITE)
yel=f'<rect x="{20+48*U}" y="70" width="{37*U}" height="44" rx="8" fill="{YEL}" stroke="{NAVY}" stroke-width="4"/>'+T(20+48*U+37*U/2+12,102,'37 cm',30)
ov=f'<rect x="{20+48*U}" y="62" width="{4*U}" height="30" fill="{TEAL}" opacity=".85"/>'+T(20+50*U,24,'overlap 4 cm',28,TEAL)+f'<line x1="{20+50*U}" y1="30" x2="{20+50*U}" y2="58" stroke="{TEAL}" stroke-width="4"/>'
rib=svg(760,120,red+yel,'A 52 cm ribbon and a 37 cm ribbon glued with an overlap')
ribo=svg(760,120,ov,'The 4 cm overlap')
rope=svg(760,120,f'<rect x="20" y="40" width="720" height="34" rx="16" fill="{WOODC}" stroke="{NAVY}" stroke-width="4"/>'+''.join(f'<line x1="{20+240*k}" y1="20" x2="{20+240*k}" y2="94" stroke="{RED}" stroke-width="6" stroke-dasharray="10 6"/>' for k in (1,2))+''.join(T(140+240*k,114,'4 m',28,TEAL) for k in range(3)),'A 12 m rope cut into 3 equal pieces with 2 cuts')
body=h2('Ribbons: overlaps and cuts')
body+=pin(128,230,800,p('Glue 52 cm and 37 cm, with a 4 cm overlap.',32,800,TEAL))
body+=pin(128,300,800,rib)+pin(128,300,800,ribo,'fade')
body+=step(1,'End to end: 52 + 37 = 89 cm.',left=128,top=450,width=800,size=32)
body+=step(2,'The overlap is counted twice: 89 − 4 = 85 cm.',left=128,top=560,width=800,size=32)
body+=pin(992,230,800,p('Cut a 12 m rope into 3 equal pieces.',32,800,TEAL)+rope,'fade')
body+=step(3,'4 + 4 + 4 = 12, so each piece is 4 m.',left=992,top=450,width=800,size=32)
body+=step(4,'3 pieces need only 2 cuts.',left=992,top=560,width=800,size=32)
body+=qrow(128,710,1250,'Your turn:','Glue 30 cm and 25 cm with a 5 cm overlap. How long?',34)+answer(1420,710,372,'50 cm')
put('p2l9-teachlen',sec('p2l9-teachlen','52–54 MIN',body,'Teach before worksheet page 2 (Q4 ribbons). Use two paper strips and a real overlap if you can. Click 1 shows the overlap. Step 1: "End to end means add." Step 2: "Look at the yellow part: those 4 cm are under the red ribbon AND inside the yellow ribbon. We counted them twice, so we take them away once: 89 − 4 = 85." '
 'Then the rope (click): "3 equal pieces that make 12: try 3 + 3 + 3 = 9, too small; 4 + 4 + 4 = 12 ✓. How many cuts? Count the red lines: 2. The last piece does not need a cut." Your turn: 30 + 25 = 55, 55 − 5 = 50 cm. Common mistakes: adding the overlap (89 + 4) and saying 3 cuts for 3 pieces.'))

# ---------- teach: clock to 5 minutes, a.m. and p.m. ----------
body=h2('Read the clock: count in 5s')
body+=pin(110,230,400,clock_svg(7,35,180,'Clock showing 7:35'))
body+=step(1,'The short hand has gone past 7, so it is after 7 o’clock.',left=600,top=240,width=1192,size=32)
body+=step(2,'The long hand is on 7. Count in 5s from 12: 5, 10, 15, 20, 25, 30, 35.',left=600,top=350,width=1192,size=32)
body+=answer(600,460,600,'It is 7:35.')
dayline=svg(1232,150,f'<rect x="20" y="40" width="596" height="50" fill="{SKY}" stroke="{NAVY}" stroke-width="4"/><rect x="616" y="40" width="596" height="50" fill="{SOFT}" stroke="{NAVY}" stroke-width="4"/>'+T(318,75,'a.m.',32)+T(914,75,'p.m.',32)+T(20,128,'12 midnight',26,anchor='start')+T(616,128,'12 noon',26)+T(1212,128,'12 midnight',26,anchor='end'),'A day line: a.m. from midnight to noon, p.m. from noon to midnight')
body+=pin(600,580,1192,dayline.replace('width:1232px','width:1192px'),'fade')
body+=qrow(128,780,1250,'Your turn:','Mei eats breakfast at 7:35. Is it a.m. or p.m.?',34)+answer(1420,780,372,'a.m.')
put('p2l9-teachclock',sec('p2l9-teachclock','54–55 MIN',body,'Teach before worksheet page 2 (Q5 clocks). Use the cardboard clocks. Step 1: "The short hand tells the hour. It has gone past 7 but not reached 8." Step 2: count round in 5s together, pointing at each number. Click the answer. Click the day line: "From midnight until noon is a.m. (the morning). From noon until midnight is p.m. (afternoon and night)." '
 'Your turn: breakfast is in the morning, so 7:35 a.m. Ask: "What would you be doing at 7:35 p.m.?" Common mistake: reading the hour from the number the short hand is nearest (8) instead of the one it has passed (7).'))

# ---------- teach: how long, across the hour ----------
t1=timeline([(0,'2:45'),(0.43,'3:00'),(1,'3:20')],None,W=1100,Hh=170,aria='Time line from 2:45 to 3:20')
t1j=timeline([(0,'2:45'),(0.43,'3:00'),(1,'3:20')],[(0,1,'+15 min'),(1,2,'+20 min')],W=1100,Hh=170,aria='Jumps of 15 minutes and 20 minutes',show=False)
body=h2('How long? Count on to the o’clock first',62)+card(p('A show starts at 2:45 p.m. and lasts 35 minutes. When does it end?',36,700))
body+=pin(128,370,1100,t1)+pin(128,370,1100,t1j,'fade')
body+=step(1,'2:45 to 3:00 is 15 minutes.',left=1280,top=370,width=512,size=30)
body+=step(2,'35 − 15 = 20 more minutes: 3:20 p.m.',left=1280,top=480,width=512,size=30)
body+=pin(128,600,1664,p('9:50 a.m. to 11:05 a.m.: how long?',34,800,TEAL),'fade')
body+=step(3,'9:50 → 10:00 is 10 min.   10:00 → 11:00 is 1 hour.   11:00 → 11:05 is 5 min.',top=670,size=32)
body+=answer(128,790,1664,'1 hour and 10 + 5 = 15 minutes: 1 hour 15 minutes')
put('p2l9-teachdur',sec('p2l9-teachdur','55–56 MIN',body,'Teach before worksheet page 2 (Q5b and Q5c). Draw the time line on the board. Click the jumps, then step 1 and step 2. Think-aloud: "An hour has 60 minutes, not 100, so I cannot just add 45 + 35. I jump to the o’clock first: 2:45 to 3:00 is 15 minutes. I still need 35 − 15 = 20 minutes: 3:20 p.m." '
 'Second example: "How long from 9:50 a.m. to 11:05 a.m.? I jump to the next o’clock: 10 minutes. Then whole hours: 10:00 to 11:00 is 1 hour. Then the minutes left: 5. Altogether 1 hour 15 minutes." Common mistakes: writing 2:80; counting 9:50 to 11:05 as 2 hours because the hour changes twice.'))

put('p2l9-trytime',try_slide('p2l9-trytime','56–57 MIN','Your turn: time','Count on to the o’clock first.',[('a','The long hand is on 9. The short hand is between 3 and 4. What time is it?','3:45'),('b','A show starts at 6:35 p.m. and lasts 40 minutes. When does it end?','7:15 p.m.'),('c','Buses leave at 8:10, 8:30, 8:50 a.m. … Ali reaches the stop at 8:45 a.m. How long does he wait?','5 minutes')],
 'Whiteboards, then click. a) The short hand has passed 3; the long hand on 9 is 45 minutes (count in 5s): 3:45. b) 6:35 to 7:00 is 25 minutes; 40 − 25 = 15 more: 7:15 p.m. c) The buses are 20 minutes apart; the next bus after 8:45 is 8:50, so he waits 5 minutes. A child who says 15 minutes has counted from 8:30.',34))

put('p2l9-ws2',ws_preview('p2l9-ws2','57–69 MIN','Worksheet page 2: on your own',[('Q3','Start where Q2b ended. Get 4 ℓ. Fill the table.'),('Q4','Ribbons: shorter than, overlap, and cutting a rope.'),('Q5','Clocks, a.m. and p.m., and how long. Count on to the o’clock first.')],'Finished early? Stretch and Challenge come next.','Children work alone. Note who needs a short catch-up. Q3: children who did not finish Q2b can start from (1 ℓ, 5 ℓ) as written. Q5c: watch for children who stop at 12:00 and forget the last 10 minutes.'))
put('p2l9-ws2ans',check_slide('p2l9-ws2ans','69–72 MIN','Page 2: check together',[('Q3','Empty 5, pour the 1 ℓ in, fill 3, pour: 4 ℓ'),('Q4','a) 46 cm   b) 105 cm   c) 5 m each, 3 cuts'),('Q5','a) 7:25 a.m., 4:50 p.m.   b) 5:25 p.m.   c) 1 h 25 min')],
 'Click each answer after a child explains. Q3 (3 ℓ jug, 5 ℓ jug): start (1, 5); empty the 5 ℓ jug (1, 0); pour the 1 ℓ into it (0, 1); fill the 3 ℓ jug (3, 1); pour it in (0, 4) ✓. Some children find a longer way (empty 3, pour, empty 3, pour, fill 5, pour until the 3 ℓ jug is full: (3, 4)); it is also right. '
 'Q4: a) 64 − 18 = 46. b) 64 + 46 = 110, minus the 5 cm overlap: 105 cm. c) 5 + 5 + 5 + 5 = 20, so 5 m; 4 pieces need 3 cuts. Q5: a) breakfast: 7:25 a.m.; after school: 4:50 p.m. b) 4:50 to 5:00 is 10 minutes, 25 more: 5:25 p.m. c) 10:45 to 11:00 is 15 minutes, 11:00 to 12:00 is 1 hour, 12:00 to 12:10 is 10 minutes: 1 hour 25 minutes.'))

# ---------- stretch (new) ----------
st=[('1.','A box with 5 same pencils is 150 g. The empty box is 50 g. How heavy is one pencil?'),('2.','You have a 4 ℓ jug and a 5 ℓ jug. How can you get exactly 3 ℓ? List each pour.'),('3.','A train leaves at 9:35 a.m. The trip takes 50 minutes. When does it arrive? Ali gets to the station 15 minutes before it leaves. When is that?')]
put('p2l9-stretch',sec('p2l9-stretch','For early finishers',h2('Stretch')+numcards(st,36),'For children who finish early. Answers: 1) 20 g (the pencils are 150 − 50 = 100 g; 5 pencils share 100 g: 20 + 20 + 20 + 20 + 20 = 100). 2) (4 ℓ jug, 5 ℓ jug): fill 4 (4, 0); pour into 5 (0, 4); fill 4 (4, 4); pour into 5 until full, only 1 ℓ fits (3, 5): 3 ℓ in the 4 ℓ jug. 3) Arrives 10:25 a.m. (9:35 to 10:00 is 25 minutes, 25 more). Ali arrives at 9:20 a.m. (15 minutes before 9:35).'))

# ---------- challenge ----------
ch=[('1.','Scale 1: 2 cubes and 1 ball balance 2 balls. Scale 2: 1 ball and 1 cube balance a 300 g weight. How heavy is one cube? One ball?'),('2.','Mei has 3 lessons in a row. Each lesson is 35 minutes, with a 10-minute break between lessons. The first lesson starts at 8:15 a.m. When does the last lesson end?')]
put('p2l9-challenge',sec('p2l9-challenge','Challenge',h2('Challenge')+numcards(ch,36),'Pairs try first, then use the "see it" slide if stuck, then the walk-through. Answers: 1) Cube 100 g, ball 200 g. 2) 10:20 a.m. Both are on the workbook Think Harder page (Challenge 6 and 7).'))
c1=balance(['cube','cube','ball'],['ball','ball'],arm=190,u=1,W=760,Hh=200,aria='Scale 1: 2 cubes and 1 ball balance 2 balls')
c2=balance(['ball','cube'],['w:300 g'],arm=190,u=1,W=760,Hh=200,aria='Scale 2: 1 ball and 1 cube balance a 300 g weight')
segs=[('lesson',35),('break',10),('lesson',35),('break',10),('lesson',35)]
x=20; tl=''
for k,mn in segs:
    w=180 if k=='lesson' else 90; tl+=f'<rect x="{x}" y="50" width="{w}" height="70" rx="8" fill="{SKY if k=="lesson" else SOFT}" stroke="{NAVY}" stroke-width="4"/>'+T(x+w/2,95,f'{mn} min',26); x+=w
tl+=T(20,160,'8:15',28,anchor='start')+T(x,160,'?',34,RED,'end')+T(20,34,'a.m.',26,MUTED,'start',700)
tlsvg=svg(760,180,tl,'Time line: lesson 35 minutes, break 10, lesson 35, break 10, lesson 35, starting at 8:15 a.m.')
body=h2('Challenge: see it',60)+'<div style="display:flex;gap:32px;align-items:flex-start">'+card(p('Q1: two scales',30,800,TEAL)+c1+c2,extra='flex:1;min-width:0;padding:16px 24px')+card(p('Q2: draw a time line',30,800,TEAL)+tlsvg+p('What time is it at the end of each block?',30,600,MUTED),extra='flex:1;min-width:0;padding:16px 24px')+'</div>'
put('p2l9-chdiag',sec('p2l9-chdiag','Challenge',body,'Show after pairs have tried, or if they are stuck. The pictures show the problem, not the answer. Ask: What do you notice on scale 1? Is there something on BOTH sides? What happens if you take it off both sides? For Q2: How many blocks are there? Which time do we know?'))
body=h2('Challenge: walk-through')+pin(128,230,800,p('Q1: take the same off both sides',34,800,TEAL))
for i,t in enumerate(['Scale 1: take 1 ball off both sides. 2 cubes balance 1 ball.','Scale 2: swap the ball for 2 cubes. 3 cubes balance 300 g.','100 + 100 + 100 = 300: a cube is 100 g, a ball is 200 g.','Check scale 1: 100 + 100 + 200 = 400 = 200 + 200 ✓']): body+=pin(128,300+i*140,800,p(t,30),'rise',WHITE)
body+=pin(992,230,800,p('Q2: count on, block by block',34,800,TEAL))
for i,t in enumerate(['Lesson 1: 8:15 → 8:50.  Break → 9:00.','Lesson 2: 9:00 → 9:35.  Break → 9:45.','Lesson 3: 9:45 → 10:00 is 15 min, 20 more → 10:20.','The last lesson ends at 10:20 a.m. ✓']): body+=pin(992,300+i*140,800,p(t,30),'rise',WHITE)
put('p2l9-chwalk',sec('p2l9-chwalk','Challenge',body,'Use after pairs have tried. Q1: the new idea is "take the same thing off both sides and it stays level". Act it out on the coat-hanger balance with two identical objects. Q2: 8:15 + 35 minutes: 8:15 to 8:45 is 30 minutes, 5 more is 8:50. Then a 10-minute break: 9:00. 9:00 + 35: 9:35. Break: 9:45. 9:45 to 10:00 is 15 minutes, 20 more: 10:20 a.m. Check: 3 lessons of 35 minutes and 2 breaks of 10 minutes make 125 minutes, which is 2 hours 5 minutes, and 8:15 + 2 hours 5 minutes = 10:20.'))

put('p2l9-talk',talk_slide('p2l9-talk','How did swapping help you with the balance puzzles? Why is a table useful for jug puzzles?','Minutes 72 to 80. Pairs talk for 2 minutes, then share. Also ask: "How do you count on past the hour?" Listen for: a level balance means the two sides weigh the same, so the melon can be swapped for 2 apples (or 400 g) and the scale stays level. A table shows how much is in each jug after every pour, so we can check every step. Past the hour: count on to the o’clock first (4:50 to 5:00 is 10 minutes), then count the rest. Praise the reasons, not only the answers.'))
put('p2l9-exit',exit_slide('p2l9-exit','A lesson starts at 4:50 p.m. and lasts 25 minutes. What time does it end?','5:15 p.m.','Minutes 80 to 90. No talking, no helping. Click to show the answer after the slips are in. Answer: 5:15 p.m. (4:50 to 5:00 is 10 minutes; 15 more minutes is 5:15). A child who writes 4:75 or 5:75 is adding minutes as if an hour had 100 minutes: plan two minutes of catch-up with the time line. Close: "You were real Measure Masters today. Next lesson is Challenge Day!" Stamp the inquiry journal.'))

order=['p2l9-title','p2l9-warm1','p2l9-warm2','p2l9-explore1','p2l9-explore2','p2l9-teach1','p2l9-we1','p2l9-try1','p2l9-we2','p2l9-try2','p2l9-key','p2l9-break','p2l9-ws1','p2l9-ws1ans','p2l9-teachlen','p2l9-teachclock','p2l9-teachdur','p2l9-trytime','p2l9-ws2','p2l9-ws2ans','p2l9-stretch','p2l9-challenge','p2l9-chdiag','p2l9-chwalk','p2l9-talk','p2l9-exit']
write_deck('Math Inquirers P2: Lesson 9 – Measure Masters',order,{'s1':{'description':'Warm-up and explore','start':'p2l9-title'},'s2':{'description':'Teach: balance puzzles and jug puzzles','start':'p2l9-teach1'},'s3':{'description':'Worksheet with teaching before page 2 (ribbons, clocks, how long)','start':'p2l9-break'},'s4':{'description':'Stretch, challenge, talk and exit','start':'p2l9-stretch'}})
