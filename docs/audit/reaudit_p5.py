"""Re-audit P5 helper: brute-force checks of a sample of answer keys + diagnostic placement simulation. Read-only."""
from itertools import permutations, product, combinations_with_replacement
from fractions import Fraction as F
import re, math

def ok(name, cond, info=''): print(('PASS ' if cond else 'FAIL ')+name, info)

# L1 Q3 digit riddle
sols=[]
for p in permutations(range(10),7):
    if p[0]==0: continue
    n=int(''.join(map(str,p)))
    if round(n/100000+1e-9)!=n//100000 + (1 if n%100000>=50000 else 0): pass
    r=(n+50000)//100000*100000
    if r!=7300000: continue
    M,H,T,Th,Hu,Te,O=p
    if T==H+3 and Th==T-H and Hu==2*Th and Te==0 and sum(p)==32: sols.append(n)
ok('L1 Q3 unique 7253609',sols==[7253609],sols)
# L1 Q6 (nearest thousand = 2 500 000, digit sum 9)
c=[n for n in range(2499500,2500500) if sum(map(int,str(n)))==9]
ok('L1 Q6 six numbers',len(c)==6 and min(c)==2500002,c)
# L1 Go further Q6
c=[int(''.join(map(str,p))) for p in permutations(range(10),7) if p[0] and p[-1]%2 and sum(p)==42 and 6950000<=int(''.join(map(str,p)))<7050000]
print('L1 GF Q6 smallest',min(c) if c else None,len(c))
# L1 Q2 closest to 6M with 0,2,3,5,6,8,9
d=[0,2,3,5,6,8,9]; nums=[int(''.join(map(str,p))) for p in permutations(d) if p[0]]
print('L1 Q2 greatest',max(nums),'smallest even',min(n for n in nums if n%2==0),'closest',min(nums,key=lambda n:abs(n-6000000)))
# L1 check puzzle 1: 3,6,7,9 closest to 7000
n4=[int(''.join(map(str,p))) for p in permutations([3,6,7,9])]; print('check1',min(n4,key=lambda n:abs(n-7000)))
# L1 check puzzle 2 single bracket placements for 4 + 6 x 5 - 3 = 47
toks=[4,'+',6,'*',5,'-',3]; res=set()
for i in range(0,7,2):
    for j in range(i+2,7,2):
        t=toks[:]; t.insert(j+1,')'); t.insert(i,'('); e=''.join(map(str,t)); 
        if (i,j)!=(0,6): res.add((e,eval(e)))
print('check2',sorted(res), 'nobracket',eval('4+6*5-3'))
# L1 Think harder Q4
print('TH Q4',7654321-1234567)
# L2
for f,a in [(F(7,10),'7/10'),(F(9,20),'9/20'),(F(3,8),'3/8'),(F(2,3),'2/3'),(F(7,12),'7/12')]:
    w=[(x,y) for x in range(2,200) for y in range(x+1,2000) if F(1,x)+F(1,y)==f]
    print('L2 unit pairs',a,w)
ok('L2 5/12 = 1/4+1/6',F(5,12)==F(1,4)+F(1,6))
print('L2 1/6+..+1/42',sum(F(1,k*(k+1)) for k in range(2,7)))
# L3 qbank challenge C2 (18,6): ways one child exactly k times other
ways=[(a,24-a) for a in range(0,25) if (a-24+a)!=0 and ((24-a)>0 and a%(24-a)==0 or a>0 and (24-a)%a==0) and a!=24-a]
print('L3 C2 pairs after (Ali,Mei)',ways)
# L3 inv total 48+12: twice => total divisible by 3, Ali>Mei start
print('L3 inv totals divisible by 3:',[t for t in (45,50,30,60) if t%3==0])
# L4 inv
print('L4 inv area6',[(a,b) for a in range(1,13) for b in range(a,13) if a*b==12],'area10',[(a,b) for a in range(1,21) for b in range(a,21) if a*b==20],'area12',[(a,b) for a in range(1,25) for b in range(a,25) if a*b==24])
# L5
print('L5 48 cuboids',len([1 for a in range(1,49) for b in range(a,49) for c in range(b,49) if a*b*c==48]),'64',len([1 for a in range(1,65) for b in range(a,65) for c in range(b,65) if a*b*c==64]),'60',len([1 for a in range(1,61) for b in range(a,61) for c in range(b,61) if a*b*c==60]))
print('L5 GF5',math.sqrt(12*15*20))
# L8 inv
print('L8 tens',[(180-2*b,b,b) for b in range(10,90,10)],'15s',[(180-2*b,b,b) for b in range(15,90,15) if (180-2*b)%15==0 and 180-2*b>0])
# L9
print('L9 Q3',[a for a in range(16) if 12*a+7*(15-a)==145],'Q4',[x for x in range(31) if 20*(30-x)+50*x==1020],'Q5 wrong',[(w,100-7*w) for w in range(5)])
d=[1];
for k in range(2,7): d.append(d[-1]+2*(2*k-3)+0) if False else None
print('L9 diamond',[ (k)**2+(k-1)**2 for k in range(1,7)])
s=''.join(map(str,range(1,200)));print('L9 100th digit',s[99])
print('L9 TH1 yellow in 100',sum(1 for i in range(100) if ['r','r','b','y','y','y'][i%6]=='y'),'50th',['r','r','b','y','y','y'][49%6])
print('L9 Q6 GF',[c for c in range(26) if 4*c-(22-c)==68])
# L10
print('L10 GF6',[(a,b,c) for a in range(0,12) for c in range(0,26) for b in [2*a] if a+b+c==25 and 50*a+10*b+20*c==530])
print('L10 GF7',[p for p in permutations('ABMS') if p[1]!='M' and False])
seats=[p for p in permutations(['Ali','Ben','Mei','Siti']) if p[0]!='Mei' and p[3]!='Mei' and abs(p.index('Ben')-p.index('Mei'))!=1 and p.index('Siti')<p.index('Ali') and p[0]!='Ben']; print('L10 GF7 seats',seats)
print('L10 TH5 coins 14 coins 4.90',[x for x in range(15) if 50*x+20*(14-x)==490])
print('L10 TH2 3-digit sum 5',len([n for n in range(100,1000) if sum(map(int,str(n)))==5]))
print('L10 C4 fours 1..50',''.join(map(str,range(1,51))).count('4'))
# L6 
print('L6 Q2 costs', 4.2/6, 2.92/4, 7.8/12)
# L7
print('L7 C4', 48/ (1.2*0.8))
# L7 GF5 lamp: P 60; Q 80*.9*.85
print('L7 lamp',80*.75,80*.9*.85)
# L2 qbank C1 sum of three unit fractions =1 (distinct)
w=[(a,b,c) for a in range(2,10) for b in range(a+1,50) for c in range(b+1,500) if F(1,a)+F(1,b)+F(1,c)==1]; print('L2 C1 three unit =1',w)
w=[(a,b,c) for a in range(2,20) for b in range(a+1,200) for c in range(b+1,2000) if F(1,a)+F(1,b)+F(1,c)==F(3,4)]; print('L2 C6 3/4 three unit',w)
# L2 Go further Q7 tank
print('L2 tank',16/(F(2,3)**3))
