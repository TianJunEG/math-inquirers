from lib import *
def E(body): return SVG(1000,270,body,'height:190px;width:100%')
def e1():
    k=940/50;x0=30;b=L(x0,150,x0+50*k,150,NAVY,4)
    for n in range(0,51,5): b+=L(x0+n*k,140,x0+n*k,160,NAVY,2)+T(x0+n*k,185,str(n),22)
    for n in range(4,21,4): b+=L(x0+n*k-9,100,x0+n*k+9,120,RED,5)+L(x0+n*k-9,120,x0+n*k+9,100,RED,5)
    for n in range(5,21,5): b+=C(x0+n*k,215,12,WHITE,BLUE,4)
    b+=T(x0+20*k,250,'20 has both marks',24,TEAL)
    b+=T(30,45,'Frog A: 4s (red crosses)',28,RED,'start')+T(380,45,'Frog B: 5s (blue circles)',28,BLUE,'start')
    return E(b)
def e2():
    b=''
    for r in range(2):
        for c in range(5):
            x=60+c*96;y=40+r*100;b+=R(x,y,96,100,WHITE,NAVY,3,0)
            i=r*5+c;b+=C(x+48,y+50,34,RED if i<6 else YEL,NAVY,3)
    b+=R(620,70,340,120,'#FFF4D1',NAVY,3,16)+T(790,145,'6 + 4 = 10',48)+T(790,235,'record each pair',24,'#5B6785',weight=600)
    b+=T(270,255,'a ten-frame',24,'#5B6785',weight=600)
    return E(b)
def e3():
    rows=[('Apple',6),('Banana',4),('Orange',7),('Grape',3),('Pear',5)];b=''
    for i,(n,c) in enumerate(rows):
        y=30+i*48;b+=T(130,y+10,n,24,anchor='end')
        for k in range(c): b+=face(160+k*42,y+3,17)
    b+=R(640,60,320,120,'#FFF4D1',NAVY,3,16)+face(690,120,22)+T(830,130,'1 face = 1 child',26)
    return E(b)
def e4():
    b=''
    def strip(x0,n):
        s='';base=190;h=90;st=50
        pts=[(x0+j*st,base if j%2==0 else base-h) for j in range(n+2)]
        for a,c in zip(pts,pts[1:]): s+=L(a[0],a[1],c[0],c[1],TEAL,6)
        for j in range(n): s+=L(pts[j][0],pts[j][1],pts[j+2][0],pts[j+2][1],TEAL,6)
        return s,(x0+(n+1)*st/2)
    for n,x0 in [(1,40),(2,270),(3,560)]:
        s,cx=strip(x0,n);b+=s+T(cx,235,f'{n} triangle{"s" if n>1 else ""}: {2*n+1} sticks',26)
    b+=T(500,40,'Straws in a row',28)
    return E(b)
def e5():
    b=PG([(110,80),(290,80),(262,230),(138,230)],'#E5E9F2',NAVY,4)+T(200,170,'?',60,RED)+T(200,255,'hidden counters',22,'#5B6785',weight=600)
    for i in range(5): b+=C(430+i*64,150,26,YEL,NAVY,3)
    b+=T(590,215,'5 loose counters',24,'#5B6785',weight=600)
    b+=R(730,70,230,130,'#FFF4D1',NAVY,3,14)+T(845,128,'12',46)+T(845,170,'altogether',26)
    return E(b)
def e6():
    b=''
    for i,(l,r) in enumerate([('20¢',44),('10¢',38),('5¢',32)]): b+=coin(180+i*160,60,l,r)
    b+=T(80,140,'Ways to make 20¢',26,anchor='start')
    rows=[(1,0,0),(0,2,0),(0,1,2)]
    for j,(a,c,d) in enumerate(rows):
        y=165+j*34;b+=R(100,y-6,480,34,WHITE,NAVY,2,0)
        for i,v in enumerate((a,c,d)): b+=T(180+i*160,y+19,str(v),24)
    b+=R(650,100,310,110,'#FFF4D1',NAVY,3,14)+T(805,150,'Find every way.',30)+T(805,190,'How do you know?',26,TEAL)
    return E(b)
def e7():
    b=R(70,50,170,170,'#BFE3DC',NAVY,4,0)+L(70,50,240,220,RED,4,True)+T(155,250,'fold corner to corner',22,'#5B6785',weight=600)
    b+=T(350,150,'✂',60)
    b+=PG([(450,220),(450,60),(610,220)],YEL)+PG([(660,60),(820,60),(820,220)],YEL)
    b+=T(630,250,'two triangles, same size',22,'#5B6785',weight=600)
    return E(b)
def e8():
    b=f'<ellipse cx="380" cy="135" rx="190" ry="105" fill="{RED}" fill-opacity="0.12" stroke="{RED}" stroke-width="4"/><ellipse cx="560" cy="135" rx="190" ry="105" fill="{BLUE}" fill-opacity="0.12" stroke="{BLUE}" stroke-width="4"/>'
    b+=T(300,22,'red buttons',24,RED)+T(640,22,'2-hole buttons',24,BLUE)
    def btn(x,y,col,holes):
        s=C(x,y,20,col,NAVY,3)
        if holes: s+=C(x-6,y,3,NAVY,NAVY,1)+C(x+6,y,3,NAVY,NAVY,1)
        return s
    for x,y in [(280,100),(330,170),(250,160)]: b+=btn(x,y,RED,False)
    for x,y in [(680,110),(640,180),(720,160)]: b+=btn(x,y,'#E5E9F2',True)
    for x,y in [(470,100),(470,170)]: b+=btn(x,y,RED,True)
    b+=T(470,250,'in the middle: red AND 2 holes',22,'#5B6785',weight=600)
    return E(b)
def e9():
    b=PG([(60,60),(120,90),(60,120)],'#F2C9A0')+PG([(60,60),(60,120),(120,90)],'#F2C9A0')+R(120,60,640,60,YEL,NAVY,3,0)+PG([(60,75),(100,90),(60,105)],NAVY)
    b+=R(780,60,40,60,'#F4A6A6',NAVY,3,0)
    b=''
    b+=PG([(60,90),(120,60),(120,120)],'#F2C9A0')+R(120,60,640,60,YEL,NAVY,3,0)+R(760,60,40,60,'#F4A6A6',NAVY,3,0)
    for i in range(16): b+=R(60+i*45,150,45,45,'#BFE3DC' if i%2==0 else '#FFFFFF',NAVY,3,0)
    b+=L(60,125,60,215,RED,3,True)+T(60,240,'start exactly at the tip',22,RED,'start')
    b+=T(790,190,'No gaps, no overlaps',26,'#5B6785',anchor='start')
    return E(b)
def e10():
    b='';names=['Play coins','Pattern strip','Clue card','Linking cubes']
    for i,n in enumerate(names):
        x=30+i*240;b+=R(x,40,210,150,'#FFF4D1',NAVY,3,16)+T(x+105,235,n,26)
    b+=C(95,115,28,'#E5E9F2')+C(150,115,28,'#E5E9F2')+T(95,125,'5¢',22)+T(150,125,'10¢',22)
    for j,c in enumerate([RED,BLUE,RED,BLUE,RED]): b+=R(285+j*32,95,30,40,c,NAVY,2,0)
    b+=R(540,70,150,90,WHITE,NAVY,3,8)+T(615,130,'Who am I?',24)
    for j in range(3): b+=R(770+j*34,110-j*0,32,32,[YEL,TEAL,RED][j],NAVY,3,0)
    return E(b)
EX={1:e1,2:e2,3:e3,4:e4,5:e5,6:e6,7:e7,8:e8,9:e9,10:e10}
