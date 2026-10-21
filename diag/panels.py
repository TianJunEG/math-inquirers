from lib import *
W,H=800,520
def P(body): return SVG(W,H,body)
# ---------- L1
def l1a():
    b='';vals=['1','2','4','7','11','16','?','?']
    for i,v in enumerate(vals):
        x=40+i*92;col=YEL if v!='?' else WHITE
        b+=R(x,300,76,76,col,NAVY,3,10,v=='?')+T(x+38,350,v,36)+T(x+38,410,['1st','2nd','3rd','4th','5th','6th','7th','8th'][i],22,'#5B6785',weight=600)
    for i,lab in enumerate(['+1','+2','+3','+4','+5','+?','+?']):
        b+=ARC(78+i*92,78+(i+1)*92,290,70,lab,TEAL if '?' not in lab else RED)
    b+=T(400,90,'How do the jumps grow?',34)+T(400,150,'Fill in the jumps, then find the 8th number.',26,'#5B6785',weight=600)
    return P(b)
def l1b():
    b=L(40,260,760,260,NAVY,4);k=720/50
    for n in range(0,51,5): b+=L(40+n*k,248,40+n*k,272)+T(40+n*k,305,str(n),22)
    for n in range(2,51,3): b+=C(40+n*k,225,8,TEAL,TEAL,1)
    for n in range(1,51,4): b+=C(40+n*k,295-0,0.1,NAVY)  # placeholder none
    for n in range(1,51,4): b+=C(40+n*k,340,8,YEL,NAVY,2)
    b+=C(70,70,10,TEAL,TEAL,1)+T(95,78,'Ali: start at 2, count in 3s',26,anchor='start')
    b+=C(70,120,10,YEL,NAVY,2)+T(95,128,'Mei: start at 1, count in 4s',26,anchor='start')
    b+=T(400,430,'Where do the dots line up?',32)
    return P(b)
# ---------- L2
def l2a():
    A=(400,70);Bp=(130,400);Cp=(670,400)
    b=PG([A,Bp,Cp],'#FFFFFF',NAVY,4)
    pos=[A,Bp,Cp,((A[0]+Bp[0])/2,(A[1]+Bp[1])/2),((A[0]+Cp[0])/2,(A[1]+Cp[1])/2),((Bp[0]+Cp[0])/2,400)]
    for i,(x,y) in enumerate(pos): b+=C(x,y,40,YEL if i<3 else WHITE,NAVY,4)+T(x,y+12,'?',34)
    b+=T(400,330,'each side = 11',30,TEAL)
    for i in range(6): b+=C(110+i*116,485,26,'#E5E9F2')+T(110+i*116,495,str(i+1),28)
    return P(b)
def l2b():
    u=36;x0=40
    b=BRACE(x0,x0+20*u,90,'20 stickers')
    b+=R(x0,110,9*u,60,TEAL,NAVY)+T(x0+4.5*u,150,'keeps 9',28,WHITE)
    b+=R(x0+9*u,110,11*u,60,YEL,NAVY)+T(x0+14.5*u,150,'shared: 11',28)
    sx=x0+9*u
    b+=T(sx-10,262,'Mei',28,anchor='end')+R(sx,225,160,55,'#BFE3DC',NAVY)+T(sx+80,262,'?',30)
    b+=T(sx-10,352,'Ben',28,anchor='end')+R(sx,315,160,55,'#BFE3DC',NAVY)+T(sx+80,352,'?',30)+R(sx+160,315,3*u,55,WHITE,RED,3,8,True)+T(sx+160+54,352,'3 more',26,RED)
    b+=T(400,450,'Share the 11 so Ben has 3 more than Mei.',28,'#5B6785',weight=600)
    return P(b)
# ---------- L3
def l3a():
    u=30;x0=170;b=BRACE(x0,x0+24*u*0.78,70,'24 votes altogether')
    rows=[('Apple',[('6',6*u*0.78*1.0,YEL)]),('Banana',[('?',150,'#BFE3DC')]),('Orange',[('?',150,'#BFE3DC'),('?',150,'#BFE3DC')])]
    y=120
    for name,segs in rows:
        b+=T(x0-14,y+45,name,28,anchor='end');x=x0
        for lab,w,col in segs:
            b+=R(x,y,w,70,col,NAVY,3,6)+T(x+w/2,y+46,lab,32);x+=w
        y+=110
    b+=T(400,470,'Orange has twice as many as banana.',28,TEAL)
    return P(b)
def l3b():
    b=T(400,45,'1 picture = 4 children',32,TEAL)
    rows=[('A',3),('B',5),('C',0)]
    y=100
    for n,c in rows:
        b+=T(70,y+14,n,34)
        for i in range(c): b+=face(140+i*66,y+8,26)
        if n=='C':
            for i in range(3): b+=C(140+i*66,y+8,26,WHITE,NAVY,3,True)
            b+=T(140+3*66+10,y+20,'?',40,RED,'start')
        y+=105
    b+=R(90,420,620,70,'#FFF4D1',NAVY,3,12)+T(400,465,'40 children voted. A has 3. B has 2 more than A.',26)
    return P(b)
# ---------- L4
def l4a():
    cols=[RED,RED,BLUE,BLUE,TEAL];b=''
    def bead(x,y,c,dash=False): return C(x,y,24,c,NAVY,3)
    for i in range(12): b+=bead(60+i*56,170,cols[i%5])
    b+=T(740,185,'…',50)
    for g,(a,z) in enumerate([(0,4),(5,9)]):
        b+=BRACE(60+a*56-24,60+z*56+24,215,'group %d'%(g+1),False)
    b+=BRACE(60+10*56-24,60+11*56+24,215,'2 left',False)
    b+=R(60,330,680,150,WHITE,NAVY,3,14)+T(400,380,'47 beads in a row.',30)+T(400,430,'How many full groups of 5 fit in 47?',30)+T(400,470,'What is left over?',30,TEAL)
    return P(b)
def l4b():
    b='';x=15
    for n in range(1,8):
        sp=17;w=(n-1)*sp
        cx=x+55
        for r in range(n):
            for k in range(r+1):
                px=cx-(r*sp)/2+k*sp;py=300-(n-1-r)*sp
                py=330-(n-1)*sp+r*sp
                b+=C(px,py,6.5,TEAL if n<=5 else WHITE,NAVY,2.2,dash=n>5)
        lab=str([1,3,6,10,15,'?','?'][n-1])
        b+=T(cx,400,lab,32,NAVY if n<=5 else RED)
        x+=108
    b+=T(400,80,'Dot triangles grow row by row',32)+T(400,130,'What numbers come next? What is the 10th?',26,'#5B6785',weight=600)
    return P(b)
# ---------- L5
def l5a():
    u=34;x0=190
    def row(y,lab,segs):
        s=T(x0-12,y+32,lab,26,anchor='end');x=x0
        for t,w,col,dash in segs: s+=R(x,y,w,48,col,RED if dash else NAVY,3,6,dash)+T(x+w/2,y+33,t,26);x+=w
        return s
    b=T(400,40,'Now',28,TEAL)+row(60,'Ben',[('?',150,'#BFE3DC',0)])+row(120,'Ali',[('?',150,'#BFE3DC',0),('5',5*u,YEL,0)])
    b+=T(400,230,'In 3 years',28,TEAL)+row(250,'Ben',[('?',150,'#BFE3DC',0),('3',3*u,WHITE,1)])+row(310,'Ali',[('?',150,'#BFE3DC',0),('5',5*u,YEL,0),('3',3*u,WHITE,1)])
    b+=R(60,400,680,90,'#FFF4D1',NAVY,3,12)+T(400,440,'In 3 years: Ben + Ali = 25',32)+T(400,475,'Find how old each is now.',26,'#5B6785',weight=600)
    return P(b)
def l5b():
    k=38;y0=470;b=R(60,y0-9*k,90,9*k,'#E5E9F2',NAVY,4,4)
    for n in range(0,10): b+=L(60,y0-n*k,150,y0-n*k,NAVY,1.5)+T(40,y0-n*k+8,str(n),22,anchor='end')
    b+=T(105,y0-9*k-14,'top',24,TEAL)
    b+=f'<path d="M175,{y0} V{y0-3*k}" stroke="{TEAL}" stroke-width="6" marker-end="url(#a)" fill="none"/>'
    b+=f'<defs><marker id="a" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="{TEAL}"/></marker></defs>'
    b+=f'<path d="M205,{y0-3*k} V{y0-2*k}" stroke="{RED}" stroke-width="6" marker-end="url(#b)" fill="none"/><defs><marker id="b" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="{RED}"/></marker></defs>'
    rows=[('Day 1','up to 3','down to 2'),('Day 2','?','?'),('Day 3','?','?'),('Day 4','?','?')]
    b+=T(540,70,'Keep a snail table',30)
    b+=R(330,100,420,52,YEL,NAVY,3,6)+T(380,135,'Day',24)+T(520,135,'climbs to',22)+T(670,135,'slides to',22)
    for i,(a,c,d) in enumerate(rows):
        y=152+i*70;b+=R(330,y,420,70,WHITE,NAVY,3,0)+T(380,y+44,a,26)+T(520,y+44,c.replace('up to ',''),28,RED if c=='?' else NAVY)+T(670,y+44,d.replace('down to ',''),28,RED if d=='?' else NAVY)
    return P(b)
# ---------- L6
def l6a():
    b=''
    for i,(l,r) in enumerate([('5¢',34),('10¢',40),('20¢',46),('50¢',54)]): b+=coin(110+i*190,95,l,r)
    b+=T(400,200,'Use any of the coins. Count each different total once.',24,'#5B6785',weight=600)
    rows=['Use 1 coin','Use 2 coins','Use 3 coins','Use all 4 coins']
    for i,r in enumerate(rows):
        y=235+i*58;b+=R(120,y,560,50,WHITE,NAVY,3,6)+T(150,y+34,r,26,anchor='start')+R(540,y+6,110,38,'#FFF4D1',NAVY,2,6)+T(595,y+34,'?',26)
    b+=T(400,505,'How many different totals in all?',30,TEAL)
    return P(b)
def l6b():
    k=8;x0=40;b=BRACE(x0,x0+90*k,80,'90¢ altogether')
    b+=R(x0,100,90*k,70,WHITE,NAVY,3,6)
    b+=R(x0,100,15*k,70,'#BFE3DC',NAVY,3,6)+T(x0+7.5*k,145,'15¢',26)+R(x0+15*k,100,20*k,70,YEL,NAVY,3,6)+T(x0+25*k,145,'20¢',26)
    b+=T(400,215,'Start: 1 sweet + 1 biscuit = 35¢',26,TEAL)
    b+=R(120,270,200,90,'#BFE3DC',NAVY,3,10)+T(220,325,'sweet 15¢',30)+R(430,270,260,90,YEL,NAVY,3,10)+T(560,325,'biscuit 20¢',30)
    b+=T(400,440,'Fill the rest of the 90¢ bar.',30)+T(400,485,'He buys some of each.',26,'#5B6785',weight=600)
    return P(b)
# ---------- L7
def l7a():
    A=(400,50);pts=[(70+130*k,430) for k in range(6)]
    b=PG([A,pts[0],pts[-1]],'#FFFFFF')
    for p in pts[1:-1]: b+=L(A[0],A[1],p[0],p[1],NAVY,3)
    b+=PG([A,pts[0],pts[1]],'#BFE3DC')
    b+=T(400,490,'4 lines from the top. How many triangles?',28)
    return P(b)
def l7b():
    x0,y0,s=200,40,400;b=R(x0,y0,s,s,'#FFFFFF',NAVY,4,0)
    b+=L(x0+s/2,y0,x0+s/2,y0+s)+L(x0,y0+s/2,x0+s,y0+s/2)
    h=s/4;b+=L(x0+h,y0,x0+h,y0+s/2,NAVY,2.5)+L(x0,y0+h,x0+s/2,y0+h,NAVY,2.5)
    b+=R(x0,y0,h,h,'#BFE3DC',NAVY,2.5,0)
    b+=T(400,490,'Count squares of every size.',28)
    return P(b)
# ---------- L8
def l8a():
    b=''
    for i,c in enumerate(['between 10 and 30','even AND in the 3 times table','2 more than a number in the 5 times table']):
        y=30+i*62;b+=C(60,y+24,22,YEL,NAVY,3)+T(60,y+34,str(i+1),26)+R(100,y,640,50,WHITE,NAVY,3,25)+T(130,y+35,c,26,anchor='start')
    for i,n in enumerate(range(10,31)):
        r,c=divmod(i,7);b+=R(50+c*100,245+r*85,88,72,'#FFF4D1',NAVY,3,10)+T(94+c*100,293+r*85,str(n),32)
    b+=T(400,510,'Cross out numbers that break a clue.',24,'#5B6785',weight=600)
    return P(b)
def l8b():
    b=R(30,30,740,470,'#FFFFFF',NAVY,3,10)+T(50,62,'Numbers 1 to 20',24,anchor='start',fill=NAVY)
    b+=f'<circle cx="300" cy="280" r="170" fill="{TEAL}" fill-opacity="0.15" stroke="{TEAL}" stroke-width="4"/><circle cx="500" cy="280" r="170" fill="{YEL}" fill-opacity="0.3" stroke="#C9971F" stroke-width="4"/>'
    b+=T(230,100,'multiples of 2',26,TEAL)+T(570,100,'multiples of 3',26,'#8A6A10')
    for x,y,t in [(200,280,'2 only'),(400,280,'both'),(600,280,'3 only'),(100,450,'neither')]:
        b+=T(x,y,t,28)+R(x-40,y+14,80,52,WHITE,NAVY,3,8)+T(x,y+50,'?',30,RED)
    return P(b)
# ---------- L9
def l9a():
    u=40;x0=170;b=''
    def row(y,lab,solid,extra=0,cut=0):
        s=T(x0-14,y+32,lab,28,anchor='end')
        for i in range(solid): s+=R(x0+i*u,y,u,46,YEL,NAVY,3,2)
        for i in range(cut): s+=R(x0+(solid+i)*u,y,u,46,WHITE,RED,3,2,True)
        for i in range(extra): s+=R(x0+(solid+cut+i)*u,y,u,46,WHITE,TEAL,3,2,True)
        return s
    b+=row(60,'Ali',9)
    b+=row(160,'Mei',7,0,2)+T(x0+8*u+u,152,'2 shorter',22,RED)
    b+=row(260,'Ben',7,3,0)+T(x0+8.5*u+u,252,'3 longer than Mei',22,TEAL)
    b+=R(60,380,680,110,'#FFF4D1',NAVY,3,12)+T(400,435,'How long are the three pencils',30)+T(400,475,'together?',30)
    return P(b)
def l9b():
    u=20;x0=190;b=T(400,40,'30 cubes altogether',30,TEAL)
    def row(y,lab,segs):
        s=T(x0-14,y+34,lab,28,anchor='end');x=x0
        for t,w,col,dash,ec in segs: s+=R(x,y,w,52,col,ec,3,4,dash)+T(x+w/2,y+36,t,24);x+=w
        return s
    b+=row(80,'First',[('second',220,'#BFE3DC',0,NAVY),('+4',80,WHITE,1,TEAL)])
    b+=row(190,'Second',[('?',220,'#BFE3DC',0,NAVY)])
    b+=row(300,'Third',[('second − 4',140,'#BFE3DC',0,NAVY),('4 less',80,WHITE,1,RED)])
    b+=T(400,450,'First + second + third = 30',30)+T(400,490,'What is the second piece?',26,'#5B6785',weight=600)
    return P(b)
# ---------- L10
def l10a():
    u=30;x0=190
    def row(y,lab,segs):
        s=T(x0-14,y+34,lab,28,anchor='end');x=x0
        for t,w,col,dash,ec in segs: s+=R(x,y,w,52,col,ec,3,4,dash)+T(x+w/2,y+36,t,24);x+=w
        return s
    b=row(50,'Ali',[('?',180,'#BFE3DC',0,NAVY)])
    b+=row(140,'Ben',[('?',180,'#BFE3DC',0,NAVY),('4',4*u,YEL,0,NAVY)])
    b+=row(230,'Mei',[('?',180,'#BFE3DC',0,NAVY),('1',u,YEL,0,NAVY),('',3*u,WHITE,1,RED)])+T(x0+300,318,'3 fewer than Ben',24,RED,'end')
    b=b.replace('<rect x="370.0" y="230" width="60"','<rect x="370.0" y="230" width="60"')
    b+=R(60,360,680,120,'#FFF4D1',NAVY,3,12)+T(400,410,'Together they have 29.',32)+T(400,455,'Ben has 4 more than Ali. Mei has 3 fewer than Ben.',24,'#5B6785',weight=600)
    return P(b)
def l10b():
    b=T(400,50,'Exactly 4 coins. Total 70¢.',34)
    for i in range(4): b+=R(60+i*175,100,150,150,WHITE,NAVY,3,14,True)+T(135+i*175,190,'?',50,RED)
    for i,l in enumerate(['5¢','10¢','20¢','50¢']): b+=coin(130+i*180,380,l,[34,40,46,54][i])
    b+=T(400,490,'How many different ways?',30,TEAL)
    return P(b)
CH={1:(l1a,l1b,'Q1: Jumps that grow','Q2: Two counting patterns'),
2:(l2a,l2b,'Q1: Magic triangle','Q2: Share the stickers'),
3:(l3a,l3b,'Q1: Votes as bars','Q2: A picture graph'),
4:(l4a,l4b,'Q1: Bead groups','Q2: Dot triangles'),
5:(l5a,l5b,'Q1: Ages now and later','Q2: The snail and the wall'),
6:(l6a,l6b,'Q1: Coin totals','Q2: Sweets and biscuits'),
7:(l7a,l7b,'Q1: Triangles in a triangle','Q2: Squares in a square'),
8:(l8a,l8b,'Q1: Secret number','Q2: Sort into a Venn diagram'),
9:(l9a,l9b,'Q1: Three pencils','Q2: Cut the ribbon'),
10:(l10a,l10b,'Q1: Stickers as bars','Q2: Four coins')}
