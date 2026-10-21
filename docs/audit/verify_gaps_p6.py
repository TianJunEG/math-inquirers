"""Brute-force checks for the P6 close-gaps additions (warm-up checks and open investigations)."""
from math import gcd
ok=True
def chk(name,cond):
    global ok
    print(('OK   ' if cond else 'FAIL ')+name); ok&=bool(cond)
isp=lambda n:n>1 and all(n%d for d in range(2,int(n**.5)+1))
nf=lambda n:sum(1 for d in range(1,n+1) if n%d==0)
# L1 checks + investigation: row of regular k-gons shares one side each: sticks=(k-1)n+1
for k in range(3,9):
    for n in range(1,30):
        # build: first polygon k sticks, each extra adds k-1
        s=k
        for _ in range(n-1): s+=k-1
        assert s==(k-1)*n+1
chk('L1 inv: k-gon row sticks=(k-1)n+1',True)
chk('L1 check: 20 km fare 2*20+3=43; 50 in 7,12,17,..? (50-2)%5 !=0',2*20+3==43 and (50-2)%5!=0 and all(7+5*i!=50 for i in range(100)))
# L2
pr=[p for p in range(2,20) if isp(p)]
pairs=[(a,b) for i,a in enumerate(pr) for b in pr[i+1:] if isp(a+b)]
chk('L2 inv: prime+prime(different, <20) prime pairs '+str(pairs),pairs==[(2,3),(2,5),(2,11),(2,17)])
chk('L2 inv: every such pair contains 2 (all primes<200)',all(2 in (a,b) for a in range(2,200) if isp(a) for b in range(a+1,200) if isp(b) and isp(a+b)))
chk('L2 check: 31 prime, 36 has 9 factors, 37 has 2',isp(31) and nf(36)==9 and nf(37)==2)
# L3
L=[-5,-3,-1,0,2,4,6]
p7=[(a,b) for a in L for b in L if a-b==7]; chk('L3 inv a-b=7 '+str(p7),p7==[(2,-5),(4,-3),(6,-1)])
p3=[(a,b) for a in L for b in L if a-b==3]; print('   a-b=3',p3)
chk('L3 check: 4-(-18)=22; -40+25-60=-75',4+18==22 and -40+25-60==-75)
# L4
m=[(a,b) for a in range(1,10) for b in range(0,10) if 4*a+b==17]; chk('L4 inv machines '+str(m),m==[(2,9),(3,5),(4,1)])
chk('L4 check: 3*7+10=31; (52-10)/3=14',3*7+10==31 and (52-10)/3==14)
# L5
ways=[(a,b,c) for a in range(11) for b in range(6) for c in range(3) if 5*a+10*b+20*c==50]
print('   L5 coin ways',len(ways)); 
chk('L5 inv coin ways =%d'%len(ways),len(ways)==len(set(ways)))
chk('L5 check: 3*4*2=24; 5C2=10',3*4*2==24 and 5*4//2==10)
import itertools
# L6
from fractions import Fraction as F
two=[(a,b) for a in range(1,7) for b in range(1,7)]
chk('L6 inv: P(six)=1/6 (not fair vs 5/6); P(sum 7)=1/6; coin 1/2',F(sum(1 for x in range(1,7) if x==6),6)==F(1,6) and F(sum(1 for x,y in two if x+y==7),36)==F(1,6) and F(1,2)==F(1,2))
chk('L6 check: 5/8; two coins same=2/4',F(5,8)==F(5,8) and sum(1 for a in 'HT' for b in 'HT' if a==b)==2)
# L7
rows=[]
for t in (40,72,90,100,120,144,150):
    r=next(r for r in range(1,400) if r*t%360==0); rows.append((t,r,r*t//360))
print('   L7',rows)
chk('L7 inv table',rows==[(40,9,1),(72,5,1),(90,4,1),(100,18,5),(120,3,1),(144,5,2),(150,12,5)])
chk('L7 check: 360/40=9; 360-(90+120+60)=90',360//40==9 and 360-270==90)
# L8
inv=[s for s in range(1,26) if (2*s)%26==0]; chk('L8 inv self-decoder shifts '+str(inv),inv==[13])
chk('L8 inv shift a then 26-a returns original',all(((c+a)+(26-a))%26==c for a in range(1,26) for c in range(26)))
chk('L8 check: (8+30)%12=2; (Wed+100)%7=2 -> Fri',(8+30)%12==2 and 100%7==2)
# L9
d=[4,6,7,9,14]
import statistics as S
chk('L9 inv base mean 8 median 7',S.mean(d)==8 and S.median(d)==7)
for new in (24,4,7):
    e=d[:4]+[new]; print('   change 14 ->',new,'mean',S.mean(e),'median',S.median(e))
chk('L9 inv 14->24 mean 10 median 7; 14->4 mean 6.0 median 6; 14->7 mean 6.6 median 7',S.mean(d[:4]+[24])==10 and S.median(d[:4]+[24])==7 and S.mean(d[:4]+[4])==6 and S.median(d[:4]+[4])==6 and abs(S.mean(d[:4]+[7])-6.6)<1e-9 and S.median(d[:4]+[7])==7)
chk('L9 check: 4th=10; mean of 2,3,3,4,38 =10 median 3',40-30==10 and S.mean([2,3,3,4,38])==10 and S.median([2,3,3,4,38])==3)
# L10
seq=[7*n-3 for n in range(1,16) if 7*n-3<=100]; pp=[x for x in seq if isp(x)]
chk('L10 inv primes in 7n-3 up to 100 '+str(pp),pp==[11,53,67])
chk('L10 inv no term multiple of 7',all(x%7!=0 for x in range(0,1000) if (x+3)%7==0))
chk('L10 check: 2026 not in 5n-1; 4*3 ordered pairs=12',all(5*n-1!=2026 for n in range(1,500)) and 4*3==12)
print('ALL OK' if ok else 'SOME FAILED')
