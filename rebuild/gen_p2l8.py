"""Math Inquirers P2, Lesson 8: Shape Builders (2D and 3D shapes). Writes split/p2l8/project (deck.json + slides/*.html)."""
import json,os,sys,math,re
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,H)
from slidekit import *
D=os.path.join(H,'..','split','p2l8','project'); os.makedirs(os.path.join(D,'slides'),exist_ok=True); S={}
def put(i,h): S[i]=h
RED='#D64545'; MINT='#D3F1E4'

# ---------- text with stacked fractions: write {3/8} in a string ----------
def fr(a,b,size):
    fs=max(24,round(size*0.8))
    return (f'<span style="display:inline-flex;flex-direction:column;align-items:center;vertical-align:middle;line-height:1;margin:0 5px;font-size:{fs}px">'
            f'<span style="padding:0 5px 3px;border-bottom:3px solid currentColor">{a}</span><span style="padding:3px 5px 0">{b}</span></span>')
def fx(s,size):
    out=''; last=0
    for m in re.finditer(r'\{(\d+)/(\d+)\}',s):
        out+=E(s[last:m.start()])+fr(m.group(1),m.group(2),size); last=m.end()
    return out+E(s[last:])
def P(s,size=40,weight=600,color=None): return p(fx(s,size),size,weight,color,raw=True)
def ansx(left,top,width,text,build='pop',size=40):
    return pin(left,top,width,f'<p style="font-size:{size}px;font-weight:800;line-height:1.2">{fx(text,size)}</p>',build,YEL,20,'18px 26px')
def qrowx(left,top,width,label,text,size=38):
    return pin(left,top,width,f'<p style="font-size:{size}px;font-weight:600;line-height:1.3"><span style="color:{TEAL};font-weight:800">{E(label)}</span>  {fx(text,size)}</p>',None,WHITE,20,'18px 28px')
def stepx(n,text,left=128,top=420,width=1664,build='rise',size=36,bg=WHITE):
    lab=f'<span style="color:{TEAL};font-weight:800">Step {n}.</span>  ' if n else ''
    return pin(left,top,width,f'<p style="font-size:{size}px;font-weight:600;line-height:1.3">{lab}{fx(text,size)}</p>',build,bg,20,'18px 28px')
def soft(left,top,width,text,size=34,build='fade'): return pin(left,top,width,P(text,size,700),build,SOFT,20,'18px 28px')
def stitle(t,size=34): return P(t,size,600,MUTED)
def try_x(sid,time,title,sub,rows,notes,size=38,top=330,gap=150):
    body=h2(title)+stitle(sub)
    for i,(a,b,c) in enumerate(rows): body+=qrowx(128,top+i*gap,1250,a,b,size)+ansx(1420,top+i*gap,372,c)
    return sec(sid,time,body,notes)
def check_x(sid,time,title,rows,notes,lw=200,gap=150,size=36):
    body=h2(title)
    for i,(a,b) in enumerate(rows):
        top=250+i*gap
        body+=pin(128,top,lw-20,f'<p style="font-size:36px;font-weight:800;color:{TEAL}">{E(a)}</p>',None,WHITE,20,'18px 24px')
        body+=ansx(128+lw,top,1664-lw,b,size=size)
    return sec(sid,time,body,notes)
def preview_x(sid,time,title,items,tip,notes):
    inner=''.join(p(f'<span style="color:{TEAL};font-weight:800">{E(a)}</span>  {fx(b,38)}',38,600,raw=True) for a,b in items)
    return sec(sid,time,h2(title)+card(inner)+card(P(tip,34,600,MUTED)),notes)

# ---------- SVG helpers ----------
def SV(w,h,body,label,dw=None,dh=None): return f'<svg aria-label="{E(label)}" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="width:{dw or w}px;height:{dh or h}px;flex:none">{body}</svg>'
def R(x,y,w,h,fill=WHITE,stroke=NAVY,sw=4,rx=0): return f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'
def T(x,y,s,size=40,fill=NAVY,weight=700,anchor='middle'): return f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" fill="{fill}" font-family="Fredoka, Arial">{E(str(s))}</text>'
def L(x1,y1,x2,y2,sw=4,col=NAVY,dash=''): return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{col}" stroke-width="{sw}"{f" stroke-dasharray=\"{dash}\"" if dash else ""} stroke-linecap="round"/>'
def PG(pts,fill=WHITE,stroke=NAVY,sw=4): return f'<polygon points="{" ".join(f"{a:.1f},{b:.1f}" for a,b in pts)}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round"/>'
def CI(x,y,r,fill=WHITE,stroke=NAVY,sw=4): return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'
def TICK(x,y,s=20,col=TEAL,sw=8): return f'<path d="M{x-s} {y} L{x-s/3:.1f} {y+s*0.7:.1f} L{x+s} {y-s*0.8:.1f}" fill="none" stroke="{col}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"/>'
def CROSS(x,y,s=30,col=RED,sw=9): return f'<path d="M{x-s} {y-s} L{x+s} {y+s} M{x+s} {y-s} L{x-s} {y+s}" fill="none" stroke="{col}" stroke-width="{sw}" stroke-linecap="round"/>'
def sfrac(x,yc,a,b,size=36,fill=NAVY):
    w=size*0.62*max(len(str(a)),len(str(b)))+10
    return T(x,yc-size*0.18,a,size,fill)+L(x-w/2,yc,x+w/2,yc,3,fill)+T(x,yc+size*0.86,b,size,fill)
def bar(x,y,w,h,n,shade=(),fill=YEL,fills=None,sw=4):
    """n EQUAL parts; shade = indices to fill; fills = {index: colour} overrides"""
    s=''; pw=w/n
    for i in range(n):
        f=(fills or {}).get(i, fill if i in shade else WHITE)
        s+=R(x+i*pw,y,pw,h,f,NAVY,sw)
    return s
def pol(cx,cy,r,a):  # angle in degrees, 0 = up, clockwise
    t=math.radians(a-90); return cx+r*math.cos(t),cy+r*math.sin(t)
def sector(cx,cy,r,a0,a1,fill,sw=4):
    x0,y0=pol(cx,cy,r,a0); x1,y1=pol(cx,cy,r,a1)
    return f'<path d="M{cx:.1f} {cy:.1f} L{x0:.1f} {y0:.1f} A{r} {r} 0 {1 if a1-a0>180 else 0} 1 {x1:.1f} {y1:.1f} Z" fill="{fill}" stroke="{NAVY}" stroke-width="{sw}" stroke-linejoin="round"/>'
def pie(cx,cy,r,n,shade=(),fill=YEL,sw=4):
    """circle cut into n EQUAL sectors (each 360/n degrees)"""
    return ''.join(sector(cx,cy,r,360*i/n,360*(i+1)/n,fill if i in shade else WHITE,sw) for i in range(n))
def ostep(left,top,n,text,ov=None,ovw=0,ovh=0,dx=0,dy=0,tw=1000,size=34,build='fade'):
    """one click = overlay drawn over the base picture + a step box to its right"""
    lab=f'<span style="color:{TEAL};font-weight:800">Step {n}.</span>  ' if n else ''
    box=f'<div style="margin-top:{dy}px;width:{tw}px;box-sizing:border-box;background:{WHITE};border-radius:20px;padding:16px 28px;flex:none"><p style="font-size:{size}px;font-weight:600;line-height:1.3">{lab}{fx(text,size)}</p></div>'
    o=f'<div style="width:{ovw}px;height:{ovh}px;flex:none">{ov or ""}</div>'
    return pin(left,top,dx+tw,f'<div style="display:flex;align-items:flex-start;gap:{dx-ovw}px">{o}{box}</div>',build)
def colstep(left,top,width,n,text,ov,ovh,dy,size=34,build='fade'):
    """one click = overlay over a full-width picture + a step box under it"""
    lab=f'<span style="color:{TEAL};font-weight:800">Step {n}.</span>  ' if n else ''
    box=f'<div style="margin-top:{dy}px;width:{width}px;box-sizing:border-box;background:{WHITE};border-radius:20px;padding:14px 28px"><p style="font-size:{size}px;font-weight:600;line-height:1.3">{lab}{fx(text,size)}</p></div>'
    return pin(left,top,width,f'<div style="width:{width}px;height:{ovh}px">{ov or ""}</div>'+box,build,extra='gap:0px;')

# ---------- standard slides ----------
def title_slide(sid,label,title,topic,today,notes):
    return (f'<section id="{sid}" data-transition="fade" style="background:{NAVY};color:{CREAM};font-family:{BF};padding:128px 128px 160px;display:flex;flex-direction:column;justify-content:center;gap:36px">\n'
            f'<p style="font-size:32px;font-weight:700;letter-spacing:4px;color:{YEL}">{E(label)}</p>\n'
            f'<h1 style="font-family:{HF};font-size:128px;font-weight:600;line-height:1.05">{E(title)}</h1>\n'
            f'<p style="font-size:44px;color:#C9D4EC">{E(topic)}</p>\n'
            f'<div style="background:#26385F;border-radius:24px;padding:40px;display:flex;flex-direction:column;gap:12px"><p style="font-size:28px;font-weight:700;letter-spacing:3px;color:{YEL}">TODAY WE WILL</p><p style="font-size:44px;font-weight:600">{E(today)}</p></div>\n'
            f'<p style="position:absolute;left:128px;bottom:64px;width:1400px;font-size:24px;color:#B7C3DD">{E(FOOT)}</p>\n<aside>{E(notes)}</aside>\n</section>\n')
def break_slide(sid,time,text,sub,notes):
    return (f'<section id="{sid}" data-transition="fade" style="background:{TEAL};color:{CREAM};font-family:{BF};padding:128px 128px 160px;display:flex;flex-direction:column;justify-content:center;gap:36px">\n'
            f'<p style="font-size:32px;font-weight:700;letter-spacing:4px;color:{YEL}">{E(time)}</p>\n'
            f'<h2 style="font-family:{HF};font-size:110px;font-weight:600;line-height:1.05">Brain break</h2>\n'
            f'<p style="font-size:48px;font-weight:600">{E(text)}</p>\n<p style="font-size:36px;color:#D7EFEA">{E(sub)}</p>\n'
            f'<p style="position:absolute;left:128px;bottom:64px;width:1400px;font-size:24px;color:#D7EFEA">{E(FOOT)}</p>\n<aside>{E(notes)}</aside>\n</section>\n')
def qcards(items,size=38):
    return ''.join(card(p(f'<span style="color:{TEAL}">{a}</span>  {fx(b,size)}',size,600,raw=True)) for a,b in items)
def talk_slide(sid,time,q,notes):
    body=h2('Talk time')+card(chip('TALK TIME',YEL,NAVY)+P(q,42,600))+card(p('Sentence starters:',34,400,MUTED)+p('“I noticed that …”   “I tested it by …”   “I know because …”',38,600))
    return sec(sid,time,body,notes)
def exit_slide(sid,time,inner,notes):
    body=h2('Exit ticket')+card(chip('EXIT TICKET')+inner)+card(p('Write your answer on a slip of paper. Show it to your tutor. Then collect your stamp in your inquiry journal.',34,400))
    return sec(sid,time,body,notes)

# =====================================================================
ORANGE='#F28C38'; SIDE='#E6A817'
def gridb(x,y,cols,rows,c,sw=4,fill=WHITE):
    d=''.join(f'M{x+i*c} {y} V{y+rows*c} ' for i in range(1,cols))+''.join(f'M{x} {y+j*c} H{x+cols*c} ' for j in range(1,rows))
    return R(x,y,cols*c,rows*c,fill,NAVY,sw)+(f'<path d="{d}" stroke="{NAVY}" stroke-width="{sw}" fill="none"/>' if d else '')
def hi(x,y,w,h): return R(x,y,w,h,YEL,TEAL,6)
def thumbs(n,w,h,draw,gap=24,label='thumbnails'):
    return SV(n*w+(n-1)*gap,h,''.join(draw(i*(w+gap),i) for i in range(n)),label)
# ---- cube stacks: cells (x right, y back, z up), oblique view from the front, right and above ----
def stack_body(cells,s,ox,oy,fills=(YEL,SOFT,SIDE),sw=3,k=0.4):
    d=s*k; out=''
    for x,y,z in sorted(cells,key=lambda c:(-c[1],c[2],c[0])):
        X=ox+x*s+y*d; Y=oy-z*s-y*d
        out+=R(X,Y-s,s,s,fills[0],NAVY,sw)
        out+=PG([(X,Y-s),(X+s,Y-s),(X+s+d,Y-s-d),(X+d,Y-s-d)],fills[1],NAVY,sw)
        out+=PG([(X+s,Y),(X+s,Y-s),(X+s+d,Y-s-d),(X+s+d,Y-d)],fills[2],NAVY,sw)
    return out
def stack_size(cells,s,k=0.4):
    mx=max(c[0] for c in cells)+1; my=max(c[1] for c in cells)+1; mz=max(c[2] for c in cells)+1
    return mx*s+my*s*k, mz*s+my*s*k
def stack_svg(cells,s,label,pad=8,fills=(YEL,SOFT,SIDE)):
    w,h=stack_size(cells,s)
    return SV(round(w+2*pad),round(h+2*pad),stack_body(cells,s,pad,h+pad,fills),label)
def hmap(rows):
    """rows of heights, first row = FRONT row"""
    return [(x,y,z) for y,r in enumerate(rows) for x,hgt in enumerate(r) for z in range(hgt)]
# ---- nets ----
def net_cells(rows): return [(x,y) for y,r in enumerate(rows) for x,ch in enumerate(r) if ch=='#']
def net_svg(rows,c,label,fill=SKY,shade=(),letters=None,pad=6):
    cells=net_cells(rows); W=max(x for x,y in cells)+1; Hh=max(y for x,y in cells)+1
    g=''
    for i,(x,y) in enumerate(cells):
        g+=R(pad+x*c,pad+y*c,c,c,YEL if (x,y) in shade else fill,NAVY,4)
        if letters and (x,y) in letters: g+=T(pad+x*c+c/2,pad+y*c+c/2+c*0.17,letters[(x,y)],round(c*0.48))
    return SV(W*c+2*pad,Hh*c+2*pad,g,label)
# ---- circle pieces ----
def semi(cx,cy,r,rot=0,fill=SKY):  # flat side down, curve up, then rotated
    return f'<path transform="rotate({rot} {cx} {cy})" d="M{cx-r} {cy} A{r} {r} 0 0 1 {cx+r} {cy} Z" fill="{fill}" stroke="{NAVY}" stroke-width="4" stroke-linejoin="round"/>'
def quarter(cx,cy,r,rot=0,fill=SKY):  # square corner at (cx,cy), curve to the upper right, then rotated
    return f'<path transform="rotate({rot} {cx} {cy})" d="M{cx} {cy} L{cx} {cy-r} A{r} {r} 0 0 1 {cx+r} {cy} Z" fill="{fill}" stroke="{NAVY}" stroke-width="4" stroke-linejoin="round"/>'

# 1. title
put('p2l8-title',title_slide('p2l8-title','P2  •  LESSON 8  •  WEEK 4','Shape Builders','2D and 3D Shapes',
 'Build shapes from semicircles and quarter circles, count every hidden square, triangle and cube, and find which nets fold into a cube.',
 'Objective: Name and describe semicircles and quarter circles and use them to make and break up shapes; count every square and triangle in a figure by working in order; count the cubes in a stack, including hidden ones, layer by layer; decide which nets fold into a cube and find opposite faces. '
 'Materials: paper circles (2 per child), scissors, about 12 linking cubes per child (or sugar cubes), the cube-net cut-out page (nets A to F, near the back of the workbook, cut out before the lesson), mini whiteboards. '
 'Online: children cut paper circles and build stacks on camera; the tutor shows the stacks and nets on the slides; a cereal box cut open shows a net. '
 'Time plan: warm-up 0 to 8, explore 8 to 20 (explore2 talk is 6 minutes), teaching 20 to 32 (click to reveal each step and answer), brain break 32 to 36, worksheet page 1 36 to 50 then check together 50 to 52, short teaching 52 to 57, worksheet page 2 57 to 69 then check together 69 to 72, talk time 72 to 80, exit ticket 80 to 90.'))

# 2. warm1: name the solid
def solid(i):
    if i==0:  # dice
        g=R(20,60,100,100,WHITE)+PG([(20,60),(120,60),(160,20),(60,20)],WHITE)+PG([(120,160),(120,60),(160,20),(160,120)],SKY)
        g+=''.join(CI(x,y,8,NAVY,NAVY,1) for x,y in [(45,85),(95,85),(70,110),(45,135),(95,135)])+CI(90,40,7,NAVY,NAVY,1)
    elif i==1:  # tissue box
        g=R(10,80,120,70,SKY)+PG([(10,80),(130,80),(170,40),(50,40)],WHITE)+PG([(130,150),(130,80),(170,40),(170,110)],'#B9D3EE')+f'<ellipse cx="90" cy="60" rx="34" ry="9" fill="{WHITE}" stroke="{NAVY}" stroke-width="3"/>'+f'<path d="M78 58 Q88 36 100 56" fill="{WHITE}" stroke="{NAVY}" stroke-width="3"/>'
    elif i==2:  # tin can
        g=f'<path d="M45 40 L45 150 A45 14 0 0 0 135 150 L135 40 Z" fill="#C9CFDA" stroke="{NAVY}" stroke-width="4"/>'+R(45,75,90,45,RED,NAVY,3)+f'<ellipse cx="90" cy="40" rx="45" ry="14" fill="#E5E9F2" stroke="{NAVY}" stroke-width="4"/>'
    elif i==3:  # party hat
        g=f'<path d="M35 150 L90 22 L145 150 A55 16 0 0 1 35 150 Z" fill="{YEL}" stroke="{NAVY}" stroke-width="4" stroke-linejoin="round"/>'+f'<path d="M62 86 L118 86 M48 118 L132 118" stroke="{RED}" stroke-width="7"/>'+CI(90,20,11,RED,NAVY,3)
    elif i==4:  # drum
        g=f'<path d="M20 60 L20 130 A70 18 0 0 0 160 130 L160 60 Z" fill="{RED}" stroke="{NAVY}" stroke-width="4"/>'+f'<path d="M20 75 L48 120 L76 80 L104 122 L132 80 L160 118" fill="none" stroke="{CREAM}" stroke-width="5"/>'+f'<ellipse cx="90" cy="60" rx="70" ry="18" fill="{CREAM}" stroke="{NAVY}" stroke-width="4"/>'
    else:  # traffic cone
        g=PG([(25,160),(155,160),(165,172),(15,172)],NAVY)+f'<path d="M45 158 L90 18 L135 158 A45 12 0 0 1 45 158 Z" fill="{ORANGE}" stroke="{NAVY}" stroke-width="4" stroke-linejoin="round"/>'+f'<path d="M73 70 L107 70 M60 112 L120 112" stroke="{WHITE}" stroke-width="12"/>'
    return SV(180,180,g,['a dice','a tissue box','a tin can','a party hat','a drum','a traffic cone'][i],170,170)
names=['Dice','Tissue box','Tin can','Party hat','Drum','Traffic cone']
labs=['Cube: 6 square faces','Cuboid: 6 rectangle faces','Cylinder: 2 flat circles','Cone: 1 flat circle and a tip','Cylinder: 2 flat circles','Cone: 1 flat circle and a tip']
body=h2('Warm-up: name the solid')+stitle('Cube, cuboid, cylinder or cone? Show me with your hands, then say it.')
CW=533
for i in range(6):
    Lf=128+(i%3)*(CW+32); Tp=290+(i//3)*300
    inner=f'<div style="display:flex;align-items:center;gap:20px">{solid(i)}<p style="font-family:{HF};font-size:40px;font-weight:600">{E(names[i])}</p></div>'
    body+=pin(Lf,Tp,CW,inner,None,WHITE,24,'16px 22px',f'box-sizing:border-box;height:276px;border:4px solid {NAVY};box-shadow:8px 8px 0 {NAVY}')
for i in range(6):
    Lf=128+(i%3)*(CW+32); Tp=290+(i//3)*300
    body+=pin(Lf+20,Tp+190,CW-40,f'<p style="font-size:30px;font-weight:800;line-height:1.2">{E(labs[i])}</p>','pop',SOFT,16,'12px 18px',f'box-sizing:border-box;border:3px solid {NAVY}')
put('p2l8-warm1',sec('p2l8-warm1','0–5 MIN',body,
 'Minutes 0 to 5. Point to one object at a time: "What solid is it the same shape as?" Children make the shape with their hands (fists together for a cube, a long box shape for a cuboid, a tube for a cylinder, hands meeting in a point for a cone), then say the name. Click to show (clicks go dice, tissue box, tin can, party hat, drum, traffic cone). '
 'Ask: "How do you know it is a cube and not a cuboid?" (all 6 faces are the same square). "Which ones can roll?" (cylinder and cone). "Which can you stack?" (cube, cuboid, cylinder standing up). '
 'Watch for children who call the cube a square: a square is flat, a cube is a solid with 6 square faces.'))

# 3. warm2
qs=[('1.','How many faces does a cube have?','6'),('2.','How many flat faces does a cylinder have?','2'),('3.','Cut a circle into 2 equal parts. What is each part called?','a semicircle'),('4.','How many quarter circles make 1 whole circle?','4'),('5.','Which solid has a tip and can roll?','a cone')]
body=h2('Quick questions')+''.join(qrowx(128,250+i*128,1250,a,b,36) for i,(a,b,c) in enumerate(qs))+''.join(ansx(1420,250+i*128,372,c,size=34) for i,(a,b,c) in enumerate(qs))
put('p2l8-warm2',sec('p2l8-warm2','5–8 MIN',body,
 'Minutes 5 to 8. Read each question aloud, give thinking time, take answers, then click. Answers: 1) 6  2) 2 (the top and the bottom; the side is curved)  3) a semicircle (half circle)  4) 4  5) a cone. '
 'For 1, hold up a cube and count the faces with the children, putting a finger on each: front, back, left, right, top, bottom. Ask: "How do you know you did not count a face twice?" (go in pairs: front and back, left and right, top and bottom).'))

# 4. explore1
g=CI(150,130,105,SKY)+T(150,252,'',28)
g+=f'<path d="M290 130 L380 130" stroke="{NAVY}" stroke-width="6"/><polygon points="398,130 376,118 376,142" fill="{NAVY}"/>'
g+=semi(520,145,105,0,YEL)+semi(520,165,105,180,YEL)
g+=CI(870,130,105,SKY)+f'<path d="M1010 130 L1100 130" stroke="{NAVY}" stroke-width="6"/><polygon points="1118,130 1096,118 1096,142" fill="{NAVY}"/>'
g+=quarter(1270,120,100,0,MINT)+quarter(1270,140,100,90,MINT)+quarter(1250,140,100,180,MINT)+quarter(1250,120,100,270,MINT)
g+=T(1480,110,'Then make',32,MUTED)+T(1480,150,'new shapes!',32,MUTED)
pic=SV(1620,270,g,'One paper circle cut into 2 semicircles, and one paper circle cut into 4 quarter circles')
body=h2('Explore: circle pieces')+card(chip('EXPLORE')+'<ol style="font-size:32px;font-weight:600;padding-left:48px;display:flex;flex-direction:column;gap:6px;margin:0"><li>Take 2 paper circles that are the same size.</li><li>Fold one in half and cut along the fold.</li><li>Fold the other in half, then in half again. Open it and cut along both folds.</li><li>Use your pieces to make new shapes. Name them!</li></ol>',extra='padding:24px 40px')
body+=pin(128,580,1664,pic,None,WHITE,24,'8px 22px')
put('p2l8-explore1',sec('p2l8-explore1','8–14 MIN',body,
 'Minutes 8 to 14. Each child cuts their own circles (draw round a cup if there are no ready-made circles). One circle gives 2 semicircles; the other gives 4 quarter circles. Children then put pieces together: whole straight sides must touch. '
 'Things to make: a whole circle in different ways, a semicircle from 2 quarter circles, a "fan", a "wave" (two semicircles side by side, one turned over). Online: the same on camera.'))

# 5. explore2
items=[('1.','How many quarter circles cover a semicircle exactly?'),('2.','Find 3 different ways to make a whole circle from your pieces.'),('3.','How many straight sides has a quarter circle? Are they the same length?')]
put('p2l8-explore2',sec('p2l8-explore2','14–20 MIN',h2('Explore: talk about it')+qcards(items,40),
 'Minutes 14 to 20. Let pairs keep building, then gather them. Answers: 1) 2.  2) 2 semicircles; 4 quarter circles; 1 semicircle and 2 quarter circles.  3) 2 straight sides, and yes, they are the same length (each goes from the middle of the circle to its edge). They meet at a square corner. '
 'Ask: "What fraction of the circle is a semicircle? A quarter circle?" (1/2 and 1/4: last lesson!).'))

# 6. teach1: semicircles and quarter circles
base=SV(1664,300,CI(190,150,120,SKY)+T(190,295,'',24),'A whole circle')
ov1=SV(1664,300,L(190,26,190,274,6,RED,'14 10')+f'<path d="M370 150 L450 150" stroke="{NAVY}" stroke-width="6"/><polygon points="468,150 446,138 446,162" fill="{NAVY}"/>'+semi(610,150,120,270,YEL)+semi(640,150,120,90,YEL),'cut through the middle: 2 semicircles')
ov2=SV(1664,300,f'<path d="M790 150 L870 150" stroke="{NAVY}" stroke-width="6"/><polygon points="888,150 866,138 866,162" fill="{NAVY}"/>'+quarter(1060,140,120,270,MINT)+quarter(1060,160,120,180,MINT)+T(1360,130,'2 quarter',34,TEAL)+T(1360,172,'circles',34,TEAL),'cut a semicircle in half again: 2 quarter circles')
body=h2('Semicircles and quarter circles')
body+=pin(128,240,1664,base)
body+=colstep(128,240,1664,1,'Cut a circle in half through its middle: 2 semicircles. A semicircle has 1 straight side and 1 curved side.',ov1,300,0,32)
body+=colstep(128,240,1664,2,'Cut a semicircle in half again: 2 quarter circles. A quarter circle has 2 straight sides and 1 curved side.',ov2,300,108,32)
body+=soft(128,780,1664,'The 2 straight sides of a quarter circle are the same length, and they meet at a square corner.',32)
put('p2l8-teach1',sec('p2l8-teach1','20–22 MIN',body,
 'Teach. Hold up a paper circle. Click 1: fold and cut through the middle. "Each half is a semicircle: semi means half. How many sides? One straight side, one curved side." Click 2: cut one semicircle again: "Each piece is a quarter of the circle: a quarter circle. Two straight sides and one curved side." Click 3: put the two straight sides of a quarter circle against a ruler: the same length, and they make a square corner like the corner of a page. '
 'Think-aloud: "To name a piece I count its straight sides and look for a curved side. One straight and one curved: semicircle. Two straight that meet at a square corner, and one curved: quarter circle."'))

# 7. we1: find the pieces
mush=semi(250,190,150,0,SKY)+R(190,190,120,120,SKY)+quarter(190,310,70,270,SKY)+quarter(310,310,70,0,SKY)
base=SV(520,330,mush,'A mushroom made of a semicircle cap, a square stem and 2 quarter circles of grass')
ov1=SV(520,330,TICK(250,135,22),'tick on the semicircle')
ov2=SV(520,330,TICK(150,290,16,RED)+TICK(350,290,16,RED),'ticks on the 2 quarter circles')
ov3=SV(520,330,TICK(250,255,20,'#3A6EA5'),'tick on the square')
body=h2('Worked example: find the pieces')+stitle('This mushroom is made of pieces. How many of each kind? Tick each piece as you count.')
body+=pin(128,320,520,base)
body+=ostep(128,320,1,'1 straight side and 1 curved side: semicircle. 1 of them.',ov1,520,330,dx=580,dy=0,tw=1084,size=32)
body+=ostep(128,320,2,'2 straight sides with a square corner and 1 curved side: quarter circles. 2 of them.',ov2,520,330,dx=580,dy=100,tw=1084,size=32)
body+=ostep(128,320,3,'4 straight sides, all the same length: square. 1 of them.',ov3,520,330,dx=580,dy=244,tw=1084,size=32)
body+=ansx(708,700,1084,'1 + 2 + 1 = 4 pieces',size=38)
body+=soft(128,800,1664,'Notice: the 2 quarter circles together would make 1 more semicircle.',30)
put('p2l8-we1',sec('p2l8-we1','22–25 MIN',body,
 'Click to reveal each step. Think-aloud: "I count one kind of piece at a time and tick it, so I never miss one or count one twice. The cap has one straight side along the bottom and a curved side: a semicircle. The grass pieces each have two straight sides meeting in a square corner and a curved side: quarter circles, even though they face different ways. The stem has 4 straight sides, all the same: a square." '
 'Ask: "Does turning a quarter circle make it a different shape?" No. This is the same thinking as the robot on the worksheet.'))

# 8. try1
put('p2l8-try1',try_x('p2l8-try1','25–26 MIN','Your turn: circle pieces','Use your paper pieces to check.',
 [('a','How many quarter circles make a semicircle?','2'),('b','Ben has 2 semicircles and 4 quarter circles. How many whole circles can he make?','2 circles'),('c','What fraction of a whole circle is 1 quarter circle?','{1/4}')],
 'Whiteboards, then click. a) 2. b) 2 semicircles make 1 circle and 4 quarter circles make another: 2 circles. Push: "What if he had 1 semicircle and 2 quarter circles?" (1 circle). c) 1/4: the circle is cut into 4 equal parts.',size=36,gap=160))

# 9. we2: squares in a 3 by 3 grid
c=100; base=SV(320,320,gridb(10,10,3,3,c),'A 3 by 3 grid of squares')
ov1=SV(320,320,''.join(T(10+c*(i%3)+c/2,10+c*(i//3)+c/2+17,i+1,48,TEAL) for i in range(9)),'small squares numbered 1 to 9')
ov3=SV(320,320,R(10,10,300,300,'none',TEAL,14,6),'the whole grid outlined')
tc=34
def th2(x,i):
    a,b=i%2,i//2
    return gridb(x+4,4,3,3,tc,3)+hi(x+4+a*tc,4+b*tc,2*tc,2*tc)
t2=thumbs(4,110,110,th2,26,'the four 2 by 2 squares')
body=h2('Worked example: count every square')+stitle('This grid is 3 squares long and 3 squares high. Count by size, smallest first.')
body+=pin(128,310,320,base)
body+=ostep(128,310,1,'1 by 1 squares: 3 in each row, 3 rows. 3 + 3 + 3 = 9',ov1,320,320,dx=380,dy=0,tw=1284)
body+=pin(508,420,1284,f'<div style="display:flex;align-items:center;gap:24px"><p style="width:640px;flex:none;font-size:34px;font-weight:600;line-height:1.3"><span style="color:{TEAL};font-weight:800">Step 2.</span>  2 by 2 squares: slide a 2 by 2 window. It fits in 4 places.</p>{t2}</div>','fade',WHITE,20,'16px 28px')
body+=ostep(128,310,3,'3 by 3 squares: the whole grid. 1 of them.',ov3,320,320,dx=380,dy=290,tw=1284)
body+=ansx(508,720,1100,'9 + 4 + 1 = 14 squares',size=40)
put('p2l8-we2',sec('p2l8-we2','26–28 MIN',body,
 'Click to reveal each step; ask the group to predict before each click. Step 2: hold up a paper 2 by 2 window and slide it: top left, top right, bottom left, bottom right. "Can it go anywhere else?" No: 4 places. '
 'Think-aloud: "Squares hide inside bigger squares, so I count by size. 1 by 1: 9. 2 by 2: I slide my window: 4. 3 by 3: just the whole grid: 1. 9 + 4 + 1 = 14." Watch for children who count 2 small squares side by side: that is a rectangle, not a square. '
 'Ask: "What do you notice about 9, 4 and 1?" (3 + 3 + 3, 2 + 2, 1: the window fits in fewer places as it grows).'))

# 10. try2
g22=SV(140,140,gridb(10,10,2,2,60),'a 2 by 2 grid'); g32=SV(200,140,gridb(10,10,3,2,60),'a grid 3 long and 2 high'); g42=SV(260,140,gridb(10,10,4,2,60),'a grid 4 long and 2 high')
body=h2('Your turn: count every square')+stitle('Whiteboards. Small squares first, then bigger ones.')
for k,(pic,q,a) in enumerate([(g22,'A 2 by 2 grid. How many squares?','5'),(g32,'3 long and 2 high. How many squares?','8'),(g42,'4 long and 2 high. How many squares?','11')]):
    top=300+k*190
    body+=pin(128,top,280,pic,None,WHITE,20,'10px 10px')+qrowx(470,top+30,900,'abc'[k],q,36)+ansx(1420,top+30,372,a,size=36)
put('p2l8-try2',sec('p2l8-try2','28–30 MIN',body,
 'Whiteboards up together, then click. a) 4 + 1 = 5. b) 6 small + 2 squares made of 4 (the 2 by 2 window fits in 2 places) = 8. There is no 3 by 3 square: the grid is only 2 high. c) 8 small + 3 of size 2 by 2 = 11. Ask a child to show the window sliding along c.'))

# 11. we3: triangles by the line they sit on
Ax,Ay=230,20; Bx,By=20,380; Cx,Cy=440,380
def trifig(x0,y0,sc,sw=4):
    A=(x0+Ax*sc,y0+Ay*sc); B=(x0+Bx*sc,y0+By*sc); C=(x0+Cx*sc,y0+Cy*sc); M=((B[0]+C[0])/2,B[1]); P=((A[0]+B[0])/2,(A[1]+B[1])/2); Q=((A[0]+C[0])/2,(A[1]+C[1])/2)
    return A,B,C,M,P,Q,PG([A,B,C],WHITE,NAVY,sw)+L(A[0],A[1],M[0],M[1],sw)+L(P[0],P[1],Q[0],Q[1],sw)
A,Bp,Cp,M,Pp,Qp,fig=trifig(0,0,1)
base=SV(460,400,fig,'A triangle with 1 line from the top corner to the middle of the bottom, and 1 line across the middle')
def tri_th(which):
    def f(x,i):
        sc=0.3; a,b,c_,m,pp,qq,fg=trifig(x+4,4,sc,3)
        k=((pp[0]+qq[0])/2,pp[1])
        shape=which[i]
        pts={'L':[a,b,m],'Rr':[a,m,c_],'W':[a,b,c_],'tl':[a,pp,k],'tr':[a,k,qq],'tw':[a,pp,qq]}[shape]
        return fg+PG(pts,YEL,TEAL,4)
    return f
body=h2('Count triangles: sort them by their bottom line')+stitle('How many triangles are in this picture?')
body+=pin(128,300,460,base)
for k,(t,sh) in enumerate([('Triangles that sit on the bottom line: 3',['L','Rr','W']),('Triangles that sit on the line across: 3',['tl','tr','tw'])]):
    tt=thumbs(3,146,128,tri_th(sh),18,t)
    body+=pin(660,300+k*200,1132,f'<div style="display:flex;align-items:center;gap:24px"><p style="width:500px;flex:none;font-size:34px;font-weight:600;line-height:1.3"><span style="color:{TEAL};font-weight:800">Step {k+1}.</span>  {E(t)}</p>{tt}</div>','fade',WHITE,20,'14px 28px')
body+=ansx(660,720,1132,'3 + 3 = 6 triangles',size=40)
body+=soft(128,820,1664,'No other line can be the bottom of a triangle here, so we have them all.',30)
put('p2l8-we3',sec('p2l8-we3','30–31 MIN',body,
 'Click through. Think-aloud: "Every triangle has a bottom side. In this picture a bottom side must lie on the bottom line or on the line across. On the bottom line: the left part, the right part, and the whole big triangle: 3. On the line across: the small left one, the small right one and the small triangle at the top made of both: 3. 3 + 3 = 6." '
 'Ask: "Is the shape under the line across a triangle?" No: it has 4 sides. The worksheet picture has 2 lines from the top: count the same way.'))

# 12. key
body=h2('Key idea: count in order')+card(p('Sort what you count: by size, by the line it sits on, or by layer. Then you never miss one or count one twice.',44,700))+card(p('Name a piece by its sides: a semicircle has 1 straight side, a quarter circle has 2.',38,600,MUTED))
put('p2l8-key',sec('p2l8-key','31–32 MIN',body,
 'Say the key idea together. Common mistakes to watch for during the worksheet: (1) Counting only the small squares in Q2a (16 instead of 30): ask "Are there bigger squares hiding?" '
 '(2) Calling a quarter circle a semicircle when it is turned (Q1): count its straight sides. '
 '(3) Counting only the cubes you can see in Q3: ask "What is holding up the top cube?" '
 '(4) Thinking any 6 joined squares fold into a cube (Q4).'))

# 13. break
put('p2l8-break',break_slide('p2l8-break','32–36 MIN','Be a shape! When the tutor calls a shape, make it with your body: a semicircle (arms in an arch over your head), a cone (hands to a point), a cube (curl up small), a cylinder (stand tall and straight).','Then: a drink of water and back to our seats.',
 'Four minutes. Call the shapes faster and faster. Add "quarter circle" (one arm up, one arm out to the side, then sweep the hand round). Online: children stay in view of the camera.'))

# 14-15. worksheet page 1
put('p2l8-ws1',preview_x('p2l8-ws1','36–50 MIN','Worksheet page 1: with your partner',[('Q1','The robot. Count one kind of piece at a time and tick it. Then make whole circles from pieces.'),('Q2','Count every square (by size) and every triangle (by the line it sits on).')],'Stuck? Use your paper pieces, or colour each shape you count.',
 'Minutes 36 to 50. Pairs work together. Ask "How do you know you have them all?" before giving any help. For Q2a, give pairs a paper window to slide (cut a 2 by 2 and a 3 by 3 hole in card).'))
put('p2l8-ws1ans',check_x('p2l8-ws1ans','50–52 MIN','Page 1: check together',[('Q1','Square 2, triangle 3, semicircle 4, quarter circle 2'),('Q1 a–c','a) semicircles    b) 11 pieces    c) 3 circles'),('Q2','a) 16 + 9 + 4 + 1 = 30 squares     b) 6 + 6 = 12 triangles')],
 'Click each answer after a pair explains theirs. Q1c: think in quarter circles: 3 semicircles are 6 quarter circles, plus 6 more is 12 quarter circles, and 4 make a circle: 3 circles. Or: 2 semicircles make 1 circle, 4 quarter circles make 1 circle, and the last semicircle with the last 2 quarter circles make 1 more. '
 'Q1: the ears and the feet are semicircles; the shoulders are quarter circles; the hat and the hands are triangles. Q2a: the 2 by 2 window fits 3 across and 3 down (9 places), the 3 by 3 window fits in 4 places. Q2b: on the bottom line: 3 single parts, 2 made of 2 parts, 1 whole = 6; on the line across: the same, 6.',lw=180,gap=170,size=34))

# 16. teach cubes
cells=hmap([[1,1,1],[2,2,2]])
s=90
w,hh=stack_size(cells,s)
base=stack_svg(cells,s,'A stack of cubes: a bottom layer 3 long and 2 deep, with a row of 3 cubes on top at the back')
top=[c for c in cells if c[2]==1]; bot=[c for c in cells if c[2]==0]
s2=62
lay=SV(600,330,stack_body([(x,y,0) for x,y,z in top],s2,10,120,(MINT,WHITE,'#9FD8C0'))+T(290,76,'top layer: 3',34,TEAL,700,'start')+stack_body(bot,s2,10,320,(YEL,SOFT,SIDE))+T(290,262,'bottom layer: 6',34,NAVY,700,'start'),'The stack taken apart: a top layer of 3 cubes and a bottom layer of 6 cubes')
body=h2('Count cubes layer by layer')+stitle('How many cubes are in this stack? Some are hidden!')
body+=pin(128,320,round(w+16),base)
body+=stepx(1,'Lift off the top layer in your head: 3 cubes.',left=540,top=320,width=540,size=32,build='fade')
body+=stepx(2,'Bottom layer: 3 long and 2 deep. 3 + 3 = 6. The back 3 hold up the top layer, so they must be there!',left=540,top=460,width=540,size=32,build='fade')
body+=pin(1160,320,600,lay,'fade',WHITE,20,'10px 20px')
body+=ansx(540,720,1262,'3 + 6 = 9 cubes',size=40)
put('p2l8-teachcube',sec('p2l8-teachcube','52–54 MIN',body,
 'Teach before worksheet page 2 (Q3 counts the cubes in three stacks). Build this stack with real cubes first, then show the picture. Ask: "How many cubes can you see? How many are there really?" Many children say 6 or 7. '
 'Click 1: the top layer. Click 2: the bottom layer: point to the right side, where you can see the end of the back row. Click 3: the stack taken apart. Think-aloud: "I count layer by layer. The top layer has 3. The bottom layer is a rectangle 3 long and 2 deep: 6. Cubes cannot float, so there must be cubes under the top ones. 3 + 6 = 9." '
 'On the worksheet the rule is the same: every cube sits on the table or on another cube, and the stack is only as deep as the picture shows (Stack A is only 1 cube deep).'))

# 17. try cubes
ta=hmap([[1,1,2]]); tb=hmap([[1,1],[2,2]]); tcx=hmap([[1,1,1],[2,2,1]])
body=h2('Your turn: count the cubes')+stitle('Count layer by layer. Remember the cubes you cannot see.')
for k,(cl,lab,a) in enumerate([(ta,'3 cubes in a row and 1 cube on top of the end','4'),(tb,'A bottom layer 2 long and 2 deep, and 2 cubes on top at the back','6'),(tcx,'A bottom layer 3 long and 2 deep, and 2 cubes on top at the back','8')]):
    sv=stack_svg(cl,76,lab)
    x=128+k*560
    body+=pin(x,300,520,f'<div style="height:270px;display:flex;align-items:flex-end;justify-content:center">{sv}</div><p style="font-size:36px;font-weight:800;color:{TEAL};text-align:center">{"abc"[k]}</p>',None,WHITE,20,'14px 20px',f'box-sizing:border-box')
    body+=ansx(x+80,700,300,a+' cubes',size=40)
put('p2l8-trycube',sec('p2l8-trycube','54–55 MIN',body,
 'Whiteboards, then click. a) 3 + 1 = 4. b) bottom 2 + 2 = 4, top 2: 6 (2 cubes are hidden under the top ones). c) bottom 3 + 3 = 6, top 2: 8. Ask: "In c, how many cubes can you not see at all?" (2: the back bottom cubes under the top ones; you can see a little of the third back cube on the right). Let children build c to check.'))

# 18. teach nets
ncells=['#...','####','..#.']
nb=net_svg(ncells,92,'A net of 6 squares: a row of 4, one square above the first and one below the third',shade=[(1,1)])
ub=net_svg(['####','#..#'],70,'Six squares: a row of 4 with one square under each end',fill='#F6D2D2')
body=h2('Nets: will it fold into a cube?')+stitle('A net is a flat shape that folds up into a solid. A cube net has 6 squares.')
body+=pin(128,300,400,nb,None,WHITE,20,'12px 16px')
body+=stepx(1,'Pick a square to be the bottom (yellow). Fold up the squares next to it: they are the walls.',left=600,top=300,width=1192,size=32,build='fade')
body+=stepx(2,'Keep folding. The square at the top end folds over to be the lid. Each square lands on a NEW face.',left=600,top=430,width=1192,size=32,build='fade')
body+=ansx(600,560,1192,'6 different faces, nothing left open: it folds into a cube ✓',size=34)
body+=pin(128,690,1664,f'<div style="display:flex;align-items:center;gap:36px">{ub}<p style="font-size:32px;font-weight:700;line-height:1.3">Not a cube net: the 2 bottom squares both fold onto the same face, and there is no lid.</p></div>','fade',SOFT,20,'14px 28px')
put('p2l8-teachnet',sec('p2l8-teachnet','55–56 MIN',body,
 'Teach before worksheet page 2 (Q4 asks which nets fold into a cube; the children cut out and fold nets A to F). Have a printed copy of this net cut out, or open up a small box. Click 1 and 2: fold it in front of the children. Think-aloud: "I choose a bottom. The squares touching it fold up as walls. The row of 4 wraps round: bottom, wall, top, wall. The two loose squares close the ends. Every square lands on a different face, so it is a cube." '
 'Click 4: the shape with two squares under the ends: "When I fold, both of these land on the same face. One face gets two squares, and one face gets none. Not a cube." '
 'Tip for the worksheet: squares that land on the same place, or a row of 5 or more squares, or a 2 by 2 block of squares mean it is not a cube net.'))

# 19. try nets
na=net_svg(['###..','..###'],62,'Two rows of 3 squares, joined like a step')
nbb=net_svg(['#.#.','####'],62,'A row of 4 squares with one square above the 1st and one above the 3rd')
letters={(0,0):'A',(1,0):'B',(1,1):'C',(2,1):'D',(3,1):'E',(3,2):'F'}
nc=net_svg(['##...','.###.','...#.'],62,'A cube net with squares lettered A to F',letters=letters,shade=[(1,1)])
body=h2('Your turn: fold it in your head')+stitle('Use a paper net if you need to.')
for k,(sv,q,a) in enumerate([(na,'Does it fold into a cube?','Yes'),(nbb,'Does it fold into a cube?','No: 2 squares land on the same face'),(nc,'Which square is opposite C?','E')]):
    x=128+k*560
    body+=pin(x,290,520,f'<div style="height:220px;display:flex;align-items:center;justify-content:center">{sv}</div><p style="font-size:34px;font-weight:700;text-align:center"><span style="color:{TEAL};font-weight:800">{"abc"[k]}</span>  {E(q)}</p>',None,WHITE,20,'14px 20px','box-sizing:border-box')
    body+=ansx(x,640,456,a,size=34)
body+=soft(128,800,1664,'Two squares in a straight line with one square between them end up opposite each other.',30)
put('p2l8-trynet',sec('p2l8-trynet','56–57 MIN',body,
 'Whiteboards (or thumbs up and down), then click. a) Yes: this is one of the 11 cube nets. b) No: the 1st and the 3rd square of the row are opposite each other, so the two squares on top of them both fold onto the same face (the lid), and the bottom is open. '
 'c) E: C, D and E are in a straight line, so when D is the bottom, C and E are the two walls facing each other. Also A is opposite D, and B is opposite F. This is the same idea that solves the dice challenge on the Think Harder page.'))

# 20-21. worksheet page 2
put('p2l8-ws2',preview_x('p2l8-ws2','57–69 MIN','Worksheet page 2: on your own',[('Q3','Count the cubes, layer by layer. Remember the hidden ones.'),('Q4','Cut out nets A to F and try folding them. Circle the ones that make a cube. Then add one square to make a net.')],'Finished early? Stretch and Challenge come next.',
 'Children work alone. Note who needs a short catch-up next lesson. Q4 uses the cut-out nets A to F from the kit page at the back of the workbook: children should have them cut out before the lesson (if not, give 2 minutes to cut). They decide first, then fold to check.'))
put('p2l8-ws2ans',check_x('p2l8-ws2ans','69–72 MIN','Page 2: check together',[('Q3','a) A 5   B 8   C 14 (9 + 4 + 1)    b) 13 more (27 − 14)'),('Q4','a) A, C and E    b) under any one of the 4 squares in the row')],
 'Click each answer after a child explains. Q3 B: one cube is completely hidden at the back, bottom, left. C: count layers: 9 + 4 + 1 = 14. b) a 3 by 3 by 3 cube has 3 layers of 9: 27; 27 − 14 = 13. '
 'Q4a: B (2 by 3) has a 2 by 2 block; D has two squares that land on the same face; F has a row of 5, which wraps round onto itself. Q4b: the extra square must go under the row (any of the 4 places), so the two loose squares become the top and the bottom. Above the row, or at the ends, it does not work. '
 'The dice net (opposite faces add up to 7) is on the Think Harder page for strong thinkers: in a straight row, the 1st and 3rd squares are opposite, and so are the 2nd and 4th.',lw=180,gap=170,size=34))

# 22. stretch
st=[('1.','How many rectangles can you find in a row of 4 squares joined side by side? (A square is a rectangle too. Count all sizes.)'),('2.','A stack is 3 cubes long, 3 cubes wide and 2 cubes high. How many cubes?'),('3.','How many triangles are in a triangle with 3 lines from the top corner to the bottom?')]
put('p2l8-stretch',sec('p2l8-stretch','For early finishers',h2('Stretch')+qcards(st,38),
 'For children who finish early. Answers: 1) 10 (4 of length 1, 3 of length 2, 2 of length 3, 1 of length 4).  2) 18 (each layer 3 + 3 + 3 = 9, two layers).  3) 10: made of 1 part 4, of 2 parts 3, of 3 parts 2, all 4 parts 1 (4 + 3 + 2 + 1).'))

# 23. challenge
ch=[('1.','Steps are made of cubes. They are 3 cubes high, then 2, then 1, and every step is 3 cubes wide (from front to back). How many cubes?'),('2.','How many squares can you find in a grid 4 squares long and 3 squares high? Another grid, longer than it is high and at least 2 squares high, also has exactly 20 squares. Find ALL such grids.')]
put('p2l8-challenge',sec('p2l8-challenge','Challenge',h2('Challenge')+qcards(ch,36),
 'Use as a pair challenge or in talk time. Ask for the reason every time. More are in the question bank. Answers: 1) 18 cubes.  2) 20 squares in the 4 by 3 grid; the other grid is 7 long and 2 high (14 + 6 = 20). So 4 by 3 and 7 by 2.'))

# 24. chdiag
steps=hmap([[3,2,1]]*3)
d1=stack_svg(steps,70,'Steps of cubes 3, 2 and 1 high, each 3 cubes deep')
d2=SV(420,320,gridb(10,10,4,3,100),'A grid 4 squares long and 3 squares high')
def chcol(t,svg_,sub): return f'<div style="background:{WHITE};border-radius:24px;padding:20px 24px;display:flex;flex-direction:column;gap:10px;flex:1;min-width:0;align-items:center"><p style="align-self:flex-start;font-size:28px;font-weight:700;color:{TEAL}">{E(t)}</p>{svg_}<p style="font-size:28px;font-weight:600;color:{MUTED}">{E(sub)}</p></div>'
body=h2('Challenge: see it',60)+f'<div style="display:flex;gap:32px;align-items:flex-start">{chcol("Q1: steps of cubes",d1,"Some cubes are hidden at the back.")}{chcol("Q2: squares in a 4 by 3 grid",d2,"Count squares of every size.")}</div>'
put('p2l8-chdiag',sec('p2l8-chdiag','Challenge',body,'Show after pairs have tried the Challenge, or if they are stuck. The diagrams show the problem, not the answer. Ask: What do you notice? What do we know? What do we not know yet? Can you build it? Answers are in the Challenge slide notes.'))

# 25. chwalk
body=h2('Challenge: walk-through')+pin(128,250,800,p('Q1: count one step at a time',38,800,TEAL))
for i,t in enumerate(['Tall step: 3 high and 3 deep: 3 + 3 + 3 = 9','Middle step: 2 high and 3 deep: 2 + 2 + 2 = 6','Short step: 1 high and 3 deep: 3','9 + 6 + 3 = 18 cubes ✓']): body+=pin(128,330+i*110,800,p(t,32),'rise',WHITE)
body+=pin(992,250,800,p('Q2: count by size',38,800,TEAL))
for i,t in enumerate(['1 by 1: 4 in a row, 3 rows: 12','2 by 2: the window fits 3 across, 2 down: 6','3 by 3: it fits 2 across, 1 down: 2','4 by 4: too big. 12 + 6 + 2 = 20 ✓ (7 by 2 also: 14 + 6 = 20)']): body+=pin(992,330+i*110,800,p(t,32),'rise',WHITE)
put('p2l8-chwalk',sec('p2l8-chwalk','Challenge',body,
 'Use after pairs have tried. Q1: you could also count front to back: each slice from the front is 3 + 2 + 1 = 6 cubes, and there are 3 slices: 6 + 6 + 6 = 18. Two ways, same answer: a great check. '
 'Q2: the grid is only 3 high, so there is no 4 by 4 square. Watch for 12 (only small squares) and for 21 or more (counting a 4 by 4 that is not there).'))

# 26. talk
put('p2l8-talk',talk_slide('p2l8-talk','72–80 MIN','How can you be sure you counted every cube in a stack, even the ones you cannot see?',
 'Minutes 72 to 80. Pairs talk for 2 minutes, then share. Listen for: count layer by layer; every cube on top must sit on a cube below (cubes do not float); a layer is a rectangle, so count its rows; build it to check. Praise the reasons, not only the answers.'))

# 27. exit
ex=stack_svg(hmap([[1,1,1],[1,1,2]]),70,'A stack: a bottom layer 3 cubes long and 2 cubes deep, with 1 cube on top at the back right')
put('p2l8-exit',exit_slide('p2l8-exit','80–90 MIN',f'<div style="display:flex;align-items:center;gap:48px">{ex}{P("How many cubes are in this stack? Every cube sits on the table or on another cube.",42,600)}</div>',
 'Minutes 80 to 90. Answer: 7 (bottom layer 3 + 3 = 6, top layer 1). Children who write 4 counted only the front faces and the top cube; ask "What is under the top cube? What is behind the front row?" Extension: How many more cubes would make the stack 2 layers of 6? (5 more).'))

# ---------- write ----------
for f in os.listdir(os.path.join(D,'slides')):
    if f.endswith('.html') and f[:-5] not in S: os.remove(os.path.join(D,'slides',f))
for i,h in S.items(): open(os.path.join(D,'slides',i+'.html'),'w').write(h)
order=['p2l8-title','p2l8-warm1','p2l8-warm2','p2l8-explore1','p2l8-explore2','p2l8-teach1','p2l8-we1','p2l8-try1','p2l8-we2','p2l8-try2','p2l8-we3','p2l8-key','p2l8-break','p2l8-ws1','p2l8-ws1ans','p2l8-teachcube','p2l8-trycube','p2l8-teachnet','p2l8-trynet','p2l8-ws2','p2l8-ws2ans','p2l8-stretch','p2l8-challenge','p2l8-chdiag','p2l8-chwalk','p2l8-talk','p2l8-exit']
deck={'v':4,'createdOnFiles':{'v':1,'at':'2026-10-21T12:00:00Z'},'lists':'css','title':'Math Inquirers P2: Lesson 8 – Shape Builders','order':order,'cover':'p2l8-title',
 'sections':{'s1':{'description':'Warm-up and explore','start':'p2l8-title'},'s2':{'description':'Teach: circle pieces, and counting squares and triangles in order','start':'p2l8-teach1'},'s3':{'description':'Worksheet with teaching before page 2','start':'p2l8-break'},'s4':{'description':'Stretch, challenge, talk and exit','start':'p2l8-stretch'}},
 'faces':{'fredoka':{'family':'Fredoka','href':'https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&display=swap'},'nunito-sans':{'family':'Nunito Sans','href':'https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@400;600;700&display=swap'}},'designSystems':[]}
json.dump(deck,open(os.path.join(D,'deck.json'),'w'),indent=1,ensure_ascii=False)
missing=[i for i in order if i not in S]
print(len(order),'slides; wrote',len(S),'missing',missing)
