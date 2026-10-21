#!/usr/bin/env python3
"""Exact checks for every new or changed numeric answer and every 'find all / unique' claim in the P4 gifted-style rework
(docs/audit/gifted_fixes_p4.md).  Run:  python3 docs/audit/verify_gifted_p4.py   (prints 'all ok')."""
from fractions import Fraction as F
from decimal import Decimal as D
from math import gcd
from itertools import permutations, combinations
def lcm(a,b): return a*b//gcd(a,b)
def nf(n): return [d for d in range(1,n+1) if n%d==0]
def rnd(n,k): return (n+k//2)//k*k            # halfway rounds up

# ---- Lesson 1
assert nf(12)==[1,2,3,4,6,12]
assert [7*k for k in range(1,6)]==[7,14,21,28,35] and 52%4==0 and 52//4==13
assert [n for n in range(1,20) if n%3==0 and n%5==0]==[15]                      # C4 unique under 20
assert [(a,20//a) for a in range(1,21) if 20%a==0 and a<=20//a]==[(1,20),(2,10),(4,5)]
assert [n for n in range(1,13) if n%3==0 and n%4==0]==[12]
assert [n for n in range(1,61) if len(nf(n))==3]==[4,9,25,49]                   # stretch 4 and Q5c (49)
assert nf(49)==[1,7,49]
assert [x for x in range(1,500) if lcm(lcm(6,9),x)==36]==[4,12,36]              # challenge 7: Bus C gap, find ALL
assert all(lcm(6,9)==lcm(lcm(6,9),x)==18 for x in (1,2,3,6,9,18))
assert all(m%12==0 for m in range(1,5000) if m%4==0 and m%6==0) and 12%24!=0   # challenge 5: Ben is wrong
# ---- Lesson 2
assert 27649-27000>500 and 6352-6300>50                                         # core 3, 6 (28 000, 6400)
assert [n for n in range(5000,6000) if rnd(n,10)==5350]==list(range(5345,5355)) # new Q2b: 10 numbers
assert [n for n in range(5000,6000) if rnd(n,10)==5350 and rnd(n,100)==5400]==list(range(5350,5355))  # stretch 5: 5 numbers
lo=min(b-a for a in range(37500,38500) for b in range(40500,41500)); hi=max(b-a for a in range(37500,38500) for b in range(40500,41500))
assert (lo,hi)==(2001,3999)                                                      # stretch 7
sols=[n for n in range(10000,100000) if rnd(n,1000)==30000 and len(set(str(n)))==5 and sum(map(int,str(n)))==12 and n%2==1]
assert sols==[30261]                                                             # challenge 8 model riddle is unique
# ---- Lesson 3
assert 18+6*3==36 and (18+6)*3==72 and 56//7*2==16 and 90-30//5==84 and 2345*3==7035 and 4236//6==706
assert max(a+b*c-d for a,b,c,d in permutations([2,3,4,5]))==21 and 3+4*5-2==21 # stretch 7
assert (4+8)*(5-3)==24 and sum(1 for p in [(1,)] )==1                           # stretch 10 (old Q3d)
fours={1:F(8,8),2:F(4,4)+F(4,4),3:F(12,4),4:4+(4-4)*4,5:F(4*4+4,4)}
assert all(fours[k]==k for k in fours)                                           # challenge 1
assert [(s,3*s) for s in range(1,200) if 3*s-20==s+20]==[(20,60)]                # challenge 6 (Siti 20, Ravi 60)
assert all(F(x*5+50,5)-x==10 and F(x*4+12,4)-x==3 for x in range(0,60))          # challenge 9 number tricks
assert 8*55-15==425
# ---- Lesson 4
assert divmod(11,3)==(3,2) and 2*4+3==11 and 32//4==8 and 18//3*2==12
assert F(5,6)>F(2,3) and F(2,3)==F(4,6)
assert 10-3-4==3
assert [n for n in range(1,500) if n%12==0 and n//3-n//4==2]==[24]               # challenge 6 marbles: 24
assert all(F(t)*(1-F(1,2)-F(1,3))==l for l,t in ((5,30),(7,42)))                 # challenge 7 sweets
# ---- Lesson 5
assert 3+F(4,10)+F(7,100)==F('3.47') and F('0.90')>F('0.89')
assert abs(D('7.46')-D('7.5'))<abs(D('7.46')-D('7.4')) and 125*3==375
assert F(4,10)+F(7,100)==F('0.47') and F('3.6')+F(5,100)==F('3.65')
mys=[f'4.{t}{h}{th}' for t in range(10) for h in range(10) for th in range(10)
     if round(D(f'4.{t}{h}{th}'),1)==D('4.7') and h==t+2 and 4+t+h+th==25]
assert mys==['4.687']                                                            # stretch 4: unique
def best(cards,target):
    out=[]
    for p in permutations(cards):
        for pos in range(1,len(cards)):
            if len(cards)-pos==2: s=''.join(p[:pos])+'.'+''.join(p[pos:]); out.append((abs(D(s)-target),s))
    return sorted(set(out))
assert best('3569',40)[0][1]=='39.65' and best('3569',50)[0][1]=='53.69'        # challenge 7 model
# ---- Lesson 6
def clock(h,m):
    a=abs((h%12)*30+m*0.5-m*6)%360; return min(a,360-a)
assert clock(4,0)==120 and clock(4,10)==65 and clock(9,30)==105 and clock(2,30)==105 and clock(3,30)==75
assert all(clock(n,0)==clock(12-n,0)==30*n for n in range(1,6))                  # challenge 5 pairs
assert 150/6==25                                                                 # stretch 8: 2:10 + 25 min = 2:35
assert 360//12==30 and 3*45==135 and 90-64==26
# ---- Lesson 7
assert 9*7==63 and 2*(15+4)==38 and 56//8==7 and 2*(8+7)==30 and 6*4+3*2==30
assert (6*6-2*2, 4*6)==(32,24)                                                   # core 6
assert [(a,12//a) for a in range(1,13) if 12%a==0 and a<=12//a]==[(1,12),(2,6),(3,4)]
assert [(7+k)**2-49 for k in (1,2,3)]==[15,32,51]                                # challenge 5
assert max(a*(12-a) for a in range(1,12))==36 and max(w*(24-2*w) for w in range(1,12))==72   # challenge 3
assert max(a*(15-a) for a in range(1,15))==56 and max(w*(30-2*w) for w in range(1,15))==112 # challenge 7 model
assert sorted(w*(30-2*w) for w in range(1,15))[-2:]==[112,112]
# ---- Lesson 8
import itertools
def sym_lines(cells,n=3):
    cells=set(cells); maps={'v':lambda r,c:(r,n-1-c),'h':lambda r,c:(n-1-r,c),'d1':lambda r,c:(c,r),'d2':lambda r,c:(n-1-c,n-1-r)}
    return [k for k,f in maps.items() if {f(r,c) for r,c in cells}==cells]
g=[(r,c) for r in range(3) for c in range(3)]
assert len([s for s in combinations(g,3) if len(sym_lines(s))==1])>0
assert sorted(s for s in combinations(g,2) if len(sym_lines(s))==2)==[((0,0),(2,2)),((0,1),(2,1)),((0,2),(2,0)),((1,0),(1,2))]   # slide stretch 3 / stretch 8
assert len([s for s in combinations(g,2) if 'v' in sym_lines(s)])==6             # challenge 8
assert len([s for s in combinations(g,5) if len(sym_lines(s))==4])==2            # challenge 9
assert [L for L in 'ABFHLT' if L in 'ABHT']==list('ABHT')
# model dice net: row 2,1,5,6 with 3 above and 4 below the 1
assert 2+5==7 and 1+6==7 and 3+4==7
# ---- Lesson 10
assert [(c,m) for c in range(11) for m in [10-c] if 4*c+2*m==32]==[(6,4)]       # challenge 9 model unique
assert all((2*a+4*(12-a))%2==0 for a in range(13)) and 35%2==1                   # 35 legs impossible
print('all ok')
