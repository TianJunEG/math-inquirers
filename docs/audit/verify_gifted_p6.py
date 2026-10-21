# Verifies every numeric answer touched by the P6 gifted-style tier rework (exact Fractions, brute force for "find all" claims).
# Run: python3 docs/audit/verify_gifted_p6.py   (prints OK / FAIL per check)
from fractions import Fraction as F
from itertools import product, permutations, combinations, combinations_with_replacement
from math import gcd
def ok(name, cond): 
    print(('OK   ' if cond else 'FAIL ')+name)
def divisors(n): return [d for d in range(1,n+1) if n%d==0]
isp=lambda n: n>1 and len(divisors(n))==2
# ---- L1
t=lambda a,d,n:a+d*(n-1)
ok('L1 C2 triangles pattern4=9', 2*4+1==9)
ok('L1 C3 10th of 7,10..=34', t(7,3,10)==34)
ok('L1 C6 fence 4 posts for 12m, 16 for 60m', 12//4+1==4 and 60//4+1==16)
ok('L1 S1 705', t(12,7,100)==705)
ok('L1 S2 200 not in 2,9,16..; 29th=198, 30th=205', 200 not in [t(2,7,n) for n in range(1,100)] and t(2,7,29)==198 and t(2,7,30)==205)
ok('L1 S3 19 houses', max(n for n in range(1,50) if 5*n+1<=100)==19 and 5*19+1==96 and 5*20+1==101)
ok('L1 S4 301 is 50th term of 7,13,..', 7+49*6==301 and t(7,6,50)==301 and 6*50+1==301)
ok('L1 S5 first term 7 rule 4n+3', 23-4*4==7 and 4*5+3==23)
ok('L1 S6 d=4', (40-4)/9==4)
ok('L1 S8 125 terms<500 of 3,7,..', len([n for n in range(1,1000) if t(3,4,n)<500])==125 and t(3,4,125)==499)
sq=[n*n for n in range(1,12)]
ok('L1 X1 squares 100, 121, 21 more', sq[9]==100 and sq[10]==121 and 121-100==21)
ok('L1 X3 6n-4 even', all((6*n-4)%2==0 for n in range(1,200)))
f=[n for n in range(1,1000) if t(5,3,n)>1000][0]
ok('L1 X4 first >1000 1001, 333rd', t(5,3,f)==1001 and f==333)
g=[n for n in range(1,1000) if t(5,3,n)>1000 and t(5,3,n)%10==0][0]
ok('L1 X4b first >1000 ending in 0 =1010, 336th', t(5,3,g)==1010 and g==336)
ok('L1 X5 2,6,18,54 7th=1458', 2*3**6==1458)
a=b=1
for _ in range(5): a+=b; b+=a
ok('L1 X6 fib code 144', b==144)
ben=[t(6,5,n) for n in range(1,100)]; mei=[t(83,-2,n) for n in range(1,100)]
common=[(n,ben[n-1]) for n in range(1,100) if ben[n-1]==mei[n-1]]
ok('L1 X7 same term 12th=61 (same position)', common==[(12,61)])
A={t(2,3,n) for n in range(1,100)}; B={t(4,5,n) for n in range(1,100)}
ok('L1 X8 14,29,44,59', sorted(x for x in A&B if x<60)==[14,29,44,59])
tt=kk=0
for _ in range(5): kk+=1; tt+=kk
ok('L1 X9 15 and 5050', tt==15 and sum(range(1,101))==5050)
# ---- L2
ok('L2 C1 factors 18', divisors(18)==[1,2,3,6,9,18])
ok('L2 C2 21 not prime, 23 prime', not isp(21) and isp(23) and divisors(21)==[1,3,7,21])
ok('L2 C3 29 mod 4 = 1', 29%4==1)
ok('L2 C4 30 max factors>1 is 3: 2*3*5', True)
def maxfactors(n):
    if n==1: return 0
    best=0
    for d in range(2,n+1):
        if n%d==0: best=max(best,1+maxfactors(n//d)) if d<n else max(best,1)
    return best
ok('L2 C4 30 split into max 3 numbers', maxfactors(30)==3)
ok('L2 C5 primes among 21..29', [x for x in (21,23,25,27,29) if isp(x)]==[23,29])
ok('L2 C6 20=3+17=7+13', sorted((p,20-p) for p in range(2,11) if isp(p) and isp(20-p))==[(3,17),(7,13)])
ok('L2 S1 64 has 7', len(divisors(64))==7)
ok('L2 S2 smallest with 6 factors=12', min(n for n in range(1,100) if len(divisors(n))==6)==12)
ok('L2 S3 100 six ways', [(p,100-p) for p in range(2,51) if isp(p) and isp(100-p)]==[(3,97),(11,89),(17,83),(29,71),(41,59),(47,53)])
ok('L2 S4 45 has 6 factors', len(divisors(45))==6)
ok('L2 S5 twin primes <50', [(p,p+2) for p in range(2,50) if isp(p) and isp(p+2)]==[(3,5),(5,7),(11,13),(17,19),(29,31),(41,43)])
ok('L2 S6 140 12 factors', 2*2*5*7==140 and len(divisors(140))==12)
m=max(range(1,30),key=lambda n:len(divisors(n)))
ok('L2 S7 24 has 8, unique max under 30', m==24 and len(divisors(24))==8 and sum(1 for n in range(1,30) if len(divisors(n))==8)==1)
ok('L2 S8 25 and 37', [n for n in range(20,41) if n%2==n%3==n%4==1]==[25,37])
ok('L2 X1 199', max(p for p in range(2,200) if isp(p))==199)
ok('L2 X2 91, 105', 7*13==91 and 3*5*7==105 and [(p,q) for p in range(2,92) for q in range(p+1,92) if isp(p) and isp(q) and p*q==91]==[(7,13)] and [(p,q,r) for p in range(2,106) for q in range(p+1,106) for r in range(q+1,106) if p*q*r==105 and isp(p) and isp(q) and isp(r)]==[(3,5,7)])
ok('L2 X3 60', min(n for n in range(1,1000) if all(n%k==0 for k in range(2,7)))==60)
ok('L2 X4 3003, 5005', 3*7*11*13==3003 and 5*7*11*13==5005 and 7*11*13==1001)
ok('L2 X5 49 only: 3 factors, 30..60', [n for n in range(31,60) if len(divisors(n))==3]==[49])
cnt=lambda n:sum(1 for p in range(2,n//2+1) if isp(p) and isp(n-p))
best=max(range(4,50,2),key=cnt)
ok('L2 X6 48 has 5 ways unique max', best==48 and cnt(48)==5 and sum(1 for n in range(4,50,2) if cnt(n)==5)==1)
ok('L2 X7 121 169', [n for n in range(100,201) if len(divisors(n))==3]==[121,169])
ok('L2 X8 301', min(n for n in range(1,1000) if all(n%k==1 for k in (2,3,4,5,6)) and n%7==0)==301)
op=[n for n in range(1,21) if sum(1 for s in range(1,21) if n%s==0)%2==1]
ok('L2 X9 lockers 1,4,9,16', op==[1,4,9,16])
# ---- L3
ok('L3 C1-C6', sorted([-4,2,-10,0,-1])==[-10,-4,-1,0,2] and -3+8==5 and 2-7==-5 and abs(-11-(-6))==5 and -2+6==4 and 30-50==-20)
ok('L3 S1..S8', -7+12==5 and 5-13==-8 and 9-(-14)==23 and 4-(-6)==10 and -10-(-3)==-7 and 7-(-4)==11 and 7-9==-2 and 10-5*4==-10 and (-9+3)/2==-3 and -120+45-70==-145)
# magic squares
sols=[]
for p in permutations(range(-4,5)):
    g=[p[0:3],p[3:6],p[6:9]]
    if all(sum(r)==0 for r in g) and all(sum(g[r][c] for r in range(3))==0 for c in range(3)) and sum(g[i][i] for i in range(3))==0 and sum(g[i][2-i] for i in range(3))==0: sols.append(g)
ok('L3 X1 magic: 8 solutions, example valid', len(sols)==8 and [(-3,2,1),(4,0,-4),(-1,-2,3)] in sols)
ok('L3 X2 17', -6+7*2==8 and 8+3*3==17)
ok('L3 X3 -180', 6*(50-80)==-180)
ok('L3 X4', (-3-(-4))-(-3-4)==8)
x=-10; first=None
for k in range(1,50):
    x+= 5 if k%2 else -3
    if x>0: first=(k,x); break
ok('L3 X7 7 moves at 1', first==(7,1))
ok('L3 X8 unique 4,-6', [(a,b) for a in range(-50,51) for b in range(-50,51) if a+b==-2 and a-b==10]==[(4,-6)])
# lifts X6: A -35t, B -300+25t
ok('L3 X6 t=5 at -175', [t for t in range(0,20) if -35*t==-300+25*t]==[5] and -35*5==-175)
ok('L3 X9 levels 4 to B3 =6 floors', 6==len([4,3,2,1,'B1','B2','B3'])-1)
# ---- L4
ok('L4 C', 6*4+1==25 and 2*10+1==21 and 54//3==18 and (38+4)//6==7 and 7*3+4==25)
ok('L4 C5 table', (3+8,7+12,10+15)==(11,19,25))
ok('L4 S1', 6*20-5==115 and [6*n-5 for n in (1,2,3,4)]==[1,7,13,19])
ok('L4 S2', (65+7)/9==8)
ok('L4 S3', all((n+5)*2==2*n+10 for n in range(100)))
ok('L4 S4', (15-6)*4==36)
ok('L4 S5', [(a,b) for a in range(1,10) for b in range(-10,11) if 3*a+b==11 and 7*a+b==23]==[(3,2)])
n=2
for _ in range(3): n=n*2+1
ok('L4 S6 23', n==23)
ok('L4 S7 9', (9+6)*4==60)
ok('L4 S8', (30-4)/2==13)
ok('L4 X1 ', [n for n in range(-50,50) if 3*n-4==n]==[2])
ok('L4 X2', ((15*2+1)*2+1)==63 and ((5*2+1)*2+1)==23)
ok('L4 X3 pairs 5a+b=18, 2a+b=6', [(a,b) for a in range(-20,21) for b in range(-50,51) if 5*a+b==18 and 2*a+b==6]==[(4,-2)] and (3*5+3,2*5+8)==(18,18))
n=0
while not (n*7+3>100): n+=1
ok('L4 X4 14', n==14)
ok('L4 X5', [n for n in range(-50,50) if 5*n-3==2*n+15]==[6] and 5*6-3==27)
ok('L4 X6', all(3*(n+2)-(3*n+5)==1 for n in range(100)))
ok('L4 X7', 28+29+30==87)
ok('L4 X8', [n for n in range(1,100) if 3*n+12==2*(n+12)]==[12])
ok('L4 X9', 3*20-3==57 and (99+3)//3==34 and 3*4-3==9 and 3*9-3==24)
# ---- L5
ok('L5 C', 3*5==15 and len(list(permutations([4,6,9],2)))==6 and len(list(combinations(range(4),2)))==6 and 4*6==24 and 10*10==100)
def routes(w,h):
    from math import comb
    return comb(w+h,w)
ok('L5 C5 3x1 routes=4', routes(3,1)==4)
ok('L5 S1', 60//(4*3)==5)
nums=[int(''.join(map(str,p))) for p in permutations([1,2,3,4],3)]
ok('L5 S2 24, 12 even', len(nums)==24 and sum(1 for n in nums if n%2==0)==12)
ok('L5 S3..S8', 6*5==30 and 3**4==81 and len(list(combinations(range(6),2)))-6==9 and 4+3+2+1==10 and 120==5*4*3*2 and 24==4*3*2 and routes(4,2)==15)
ok('L5 X1 pentagon 10, hexagon 20', len(list(combinations(range(5),3)))==10 and len(list(combinations(range(6),3)))==20)
ok('L5 X2 3-digit different digits 648', sum(1 for n in range(100,1000) if len(set(str(n)))==3)==648 and 9*9*8==648)
ok('L5 X3 digits 252', sum(len(str(n)) for n in range(1,121))==252)
ok('L5 X4 24 examples', 4*3*2*1==24 and 2*3*4==24)
ok('L5 X5 n(n-1)=90 -> 10 unique', [n for n in range(2,100) if n*(n-1)==90]==[10])
sqn=lambda k:sum((k-i+1)**2 for i in range(1,k+1))
ok('L5 X6 14 and 4x4=30', sqn(3)==14 and sqn(4)==30)
ok('L5 X7 70', routes(4,4)==70)
ok('L5 X8 28', len([(a,b) for a in range(7) for b in range(a,7)])==28)
ok('L5 X9 15', sum(1 for n in range(100,1000) if sum(map(int,str(n)))==5)==15)
# ---- L6
ok('L6 basics', F(3,6)==F(1,2) and F(7,10)==F(7,10) and F(2,4)==F(1,2))
d2=[(a,b) for a in range(1,7) for b in range(1,7)]
ok('L6 S1 prime 10 spinner', F(len([x for x in range(1,11) if isp(x)]),10)==F(2,5))
ok('L6 S2 total 9', F(sum(1 for a,b in d2 if a+b==9),36)==F(1,9))
ok('L6 S3', 5*4==20 and 20-5==15)
ok('L6 S5', 'MATHEMATICS'.count('M')==2 and len('MATHEMATICS')==11)
ok('L6 S6 >4 of 1200 =400', F(2,6)*1200==400)
ok('L6 S7 at least one 6 = 11/36', F(sum(1 for a,b in d2 if 6 in (a,b)),36)==F(11,36))
ok('L6 S8 points 2', F(1,3)*2==F(2,3)*1)
ok('L6 X2 14/30', F(len([n for n in range(1,31) if n%3==0 or n%5==0]),30)==F(7,15))
ok('L6 X3 9/36', F(sum(1 for a,b in d2 if (a*b)%2==1),36)==F(1,4))
ok('L6 X5 1/3', F(3,9)==F(1,3))
ok('L6 X7 3/8', F(sum(1 for c in product('HT',repeat=3) if c.count('H')==2),8)==F(3,8))
mei=sum(1 for a,b in d2 if a>b); ali=sum(1 for a,b in d2 if a<=b)
ok('L6 X8 15/36 21/36', (mei,ali)==(15,21))
ok('L6 X9 odd 4/12', F(sum(1 for a in (1,2,3) for b in (1,2,3,4) if (a*b)%2==1),12)==F(1,3))
ok('L6 X1 example fair game 3/6 each, unfair 4/6', F(3,6)==F(3,6) and F(4,6)==F(2,3))
# ---- L7
ok('L7 C', 4*90==360 and 6*60==360 and 360//3==120 and 72*5==360 and min(k for k in range(1,20) if 72*k%360==0)==5 and 180-50==130 and 180-60==120)
ok('L7 S1 10', [n for n in range(3,100) if (180-360/n)==4*(360/n)]==[10])
ok('L7 S2 1260', [n for n in range(3,100) if 180-360/n==140]==[9] and 9*140==1260 and 7*180==1260)
ok('L7 S6', [n for n in range(10,21) if 360%n==0]==[10,12,15,18,20])
ok('L7 S8 1080', 3*360==1080)
ok('L7 X1', 5*108==540 and min(k for k in range(1,100) if 108*k%360==0)==10 and 108*10==1080)
stars9=[k for k in range(1,5) if gcd(9,k)==1 and k>1]
ok('L7 X2 9-point stars: k=2,4', stars9==[2,4] and 360*2/9==80 and 360*4/9==160)
ok('L7 X4 12-point star only k=5', [k for k in range(2,6) if gcd(12,k)==1]==[5] and 360*5/12==150)
ok('L7 X5 13', 12*(360+30)==4680 and 4680/360==13)
ok('L7 X6 old 9; new: inside=180-360/n<180 increasing', [n for n in range(3,100) if 180-360/n==140]==[9] and 180-360/60==174 and 180-360/12==150 and 180-360/5==108)
ok('L7 X7 new 12 -> 24, 3960', [n for n in range(3,100) if (n-2)*180==1800]==[12] and 360/12/2==15 and 360/15==24 and 22*180==3960 and 24*165==3960)
ok('L7 X8', 90+135+135==360 and 60+150+150==360)
ok('L7 X3 8 points k=3: turn 135, point 45, 8*135=1080', 360*3/8==135 and 180-135==45 and 8*135==1080 and gcd(8,3)==1 and 360*3/9==120)
ok('L7 X9', 6*60==360 and 6*120==720)
# ---- L8
ok('L8 C', (10+5)%12==3 and 20%12==8 and 45%7==3 and (1+10)%7==4)  # Monday=0 -> +10 -> 3 = Thursday
al='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def sh(s,k): return ''.join(al[(al.index(c)+k)%26] if c in al else c for c in s)
ok('L8 C5 DOG+1=EPH, KBN-1=JAM', sh('DOG',1)=='EPH' and sh('KBN',-1)=='JAM')
ok('L8 S1 100th of CODE =E', 'CODE'[(100-1)%4]=='E')
ok('L8 S2 1000h from 10 -> 2', (10+1000)%12==2)
ok('L8 S3 smallest >10 rem 3 by 4 and 5: 23', min(n for n in range(11,200) if n%4==3 and n%5==3)==23)
ok('L8 S4 BYFFI shift20 -> HELLO', sh('BYFFI',-20)=='HELLO')
ok('L8 S5 365 -> Tue, 366 -> Wed', 365%7==1 and 366%7==2)
ok('L8 S6', 29%26==3)
ok('L8 S7', (47%12,35%12,(47+35)%12)==(11,11,10))
ok('L8 S8', (21+50)%24==23)
ok('L8 X1 ×2 collides A,N', (0*2)%26==(13*2)%26)
ok('L8 X2 ×3 CAB->GAD, injective', ''.join(al[(al.index(c)*3)%26] for c in 'CAB')=='GAD' and len({(i*3)%26 for i in range(26)})==26)
ok('L8 X3 example', sh('MEET AT SIX',3)=='PHHW DW VLA')
ok('L8 X4 new 182', min(n for n in range(3,2000) if n%3==2 and n%4==2 and n%5==2 and n%7==0)==182)
# X5 library
d=[n for n in range(1,200) if n%4==0 and n%6==0]
ok('L8 X5 next meet day 12 Sat; 5th meeting day 60 Fri', d[0]==12 and 12%7==5 and d[4]==60 and 60%7==4)  # Monday=0 -> 5=Saturday(Mon,Tue,Wed,Thu,Fri,Sat) index5=Sat
ok('L8 X6', [k for k in range(26) if (2*k)%26==6]==[3,16])
ok('L8 X7 crack', sh('X ADKT BPIWH',-15)=='I LOVE MATHS')
ok('L8 X8 21', (7+21)%26==2)
ok('L8 X9', len({(5*i)%12 for i in range(1,13)})==12 and {(4*i)%12 for i in range(1,13)}=={0,4,8})
ok('L8 X old3 1000 days after Mon -> Sunday', 1000%7==6)
ok('L8 X old5 2026th -> 3', 2026%7==3 and (2026-1)%7+1==3)
# ---- L9
mean=lambda xs:F(sum(xs),len(xs))
ok('L9 C', mean([3,5,7,9])==6 and mean([10,0,8,6])==6 and 55==5*11)
ok('L9 S1', 5*152-4*150==160)
ok('L9 S2', 4*86-3*84==92)
ok('L9 S4', F(8*12+21,9)==13)
ok('L9 S5', 40-7-11-14==8)
ok('L9 S6', 20*2-3==37)
ok('L9 S7', F(5*16-3*15,2)==F(35,2))
import statistics as st
from collections import Counter
def modes(xs):
    c=Counter(xs); m=max(c.values()); return [k for k,v in c.items() if v==m] if m>1 else []
sols=[]
for c in combinations_with_replacement(range(5,15),5):
    if c[0]==5 and c[-1]==14 and sum(c)==45 and st.median(c)==8 and modes(c)==[8]: sols.append(c)
ok('L9 S8 unique 5,8,8,10,14', sols==[(5,8,8,10,14)])
ok('L9 X1 12', 5*8-4*7==12)
ok('L9 X1b 4,6,8,10,12 mean 8; remove 4 -> 9', mean([4,6,8,10,12])==8 and mean([6,8,10,12])==9)
ok('L9 X2 50, max mean 33', 10*32-9*30==50 and F(270+60,10)==33)
sols=[c for c in combinations_with_replacement(range(0,30),5) if sum(c)==25 and c[0]==2 and c[-1]==9 and st.median(c)==4 and modes(c)==[4]]
ok('L9 X3 example clues unique', sols==[(2,4,4,6,9)])
ok('L9 X4 boss', mean([2000]*9+[11000])==2900 and st.median([2000]*9+[11000])==2000 and modes([2000]*9+[11000])==[2000])
ok('L9 X5 1,5: +3 mean 6, x3 mean 9, squares mean 13 != 9', mean([1,5])==3 and mean([4,8])==6 and mean([3,15])==9 and mean([1,25])==13)
sols=[c for c in combinations_with_replacement(range(0,40),5) if sum(c)==30 and st.median(c)==5 and modes(c)==[2]]
ok('L9 X6 max biggest 15', max(c[-1] for c in sols)==15)
ok('L9 X7 3 sets', sorted(c for c in combinations(range(1,20),3) if sum(c)==12 and c[1]==4)==[(1,4,7),(2,4,6),(3,4,5)])
ok('L9 X8 99', sum(range(1,100))==4950 and 4950/99==50)
ok('L9 X9 68 and 34', 9*44-8*41==68 and 10*43-9*44==34)
# ---- L10
ok('L10 C', t(5,3,20)==62 and 2*2*3*5==60 and -3-5==-8 and 5*4-6==14 and len(list(permutations([3,5,7],2)))==6 and mean([12,15,9,20,14])==14)
ok('L10 S1 33', 3*33+1==100)
ok('L10 S2', [p for p in range(80,101) if isp(p)]==[83,89,97])
ok('L10 S3 12', 360/(180-150)==12)
ok('L10 S4 1/6', F(sum(1 for a,b in d2 if a+b>=10),36)==F(1,6))
ok('L10 S5 MATHS+5=RFYMX', sh('MATHS',5)=='RFYMX')
ok('L10 S6 12', (10+50)%12==0)
ok('L10 S7 16', 7*10-6*9==16)
ok('L10 X1 33', sum(1 for n in range(1,101) if n%2 and n%3)==33)
ok('L10 X2 4 and -4', [n for n in range(-50,50) if 3*n-8==n]==[4] and [n for n in range(-50,50) if 3*n+8==n]==[-4])
ok('L10 X3 30', sqn(4)==30)
ok('L10 X4 example 7n-3 first multiple of 5 = 25 at n=4', [7*n-3 for n in range(1,10) if (7*n-3)%5==0][0]==25)
ok('L10 X5 150 turn: 12 repeats, 5 rounds', min(k for k in range(1,100) if 150*k%360==0)==12 and 150*12==1800 and 1800//360==5)
sols=[(a,b,c) for a in range(0,30) for b in range(a,30) for c in range(b,30) if a+b+c==24 and b==7 and c-a==9]
ok('L10 X6 4,7,13', sols==[(4,7,13)])
ok('L10 X7 50 four ways', [(p,50-p) for p in range(2,26) if isp(p) and isp(50-p)]==[(3,47),(7,43),(13,37),(19,31)])
ok('L10 X8 1/8', F(sum(1 for a in range(1,9) for b in range(1,9) if a+b==9),64)==F(1,8))
ok('L10 X9 2027', 6*338-1==2027 and 6*339-1==2033)
ok('L10 slides: 50th of 7,11,.. ; exactly 3 factors <=50; prime total', t(7,4,50)==203 and len([n for n in range(1,51) if len(divisors(n))==3])==4 and F(sum(1 for a,b in d2 if isp(a+b)),36)==F(5,12))
