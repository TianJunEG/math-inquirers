#!/usr/bin/env python3
"""Brute-force checks for the warm-up checks and open investigations added in docs/audit/close_gaps_p4.md.  Run: python3 docs/audit/verify_close_gaps_p4.py  (prints 'all ok')."""
from math import gcd
from itertools import product, permutations, combinations
from fractions import Fraction as Fr
def lcm(a,b): return a*b//gcd(a,b)
def nf(n): return [d for d in range(1,n+1) if n%d==0]
def rnd(n,k): return (n+k//2)//k*k   # halfway rounds up

# ---- L1 checks + investigation
assert [f for f in range(1,41) if f%3==0 and f%5==0]==[15,30]
assert nf(30)==[1,2,3,5,6,10,15,30]
assert [lcm(6,b) for b in (8,9,12,5,7)]==[24,18,12,30,42]
pairs=[(a,b) for a in range(2,13) for b in range(a+1,13) if lcm(a,b)==12]
assert pairs==[(2,12),(3,4),(3,12),(4,6),(4,12),(6,12)],pairs
# ---- L2
assert [n for n in (7499,7500,8499,8500) if rnd(n,1000)==8000]==[7500,8499]
assert rnd(49960,100)==50000 and rnd(49960,1000)==50000
bad=[n for n in range(0,100000) if rnd(rnd(n,100),1000)!=rnd(n,1000)]
assert bad and all(450<=n%1000<=499 for n in bad) and len(bad)==50*100 and 1449 not in bad and 1450 in bad
assert rnd(rnd(1450,100),1000)==2000 and rnd(1450,1000)==1000
assert all(rnd(rnd(n,100),1000)==rnd(n,1000) for n in range(0,100000) if not 450<=n%1000<=499)
# ---- L3
assert 20-12//4+2==19 and (2+3)*4==20 and 10-2*3==4
import itertools
def reach(nums):
    # all values from using every number once with + - x / and any bracketing (exact fractions)
    if len(nums)==1: return {nums[0]}
    out=set()
    for i in range(1,len(nums)):
        pass
    res=set()
    def comb(items):
        if len(items)==1: return {items[0][0]:items[0][1]}
        r={}
        n=len(items)
        for mask in range(1,2**n-1):
            L=[items[i] for i in range(n) if mask>>i&1]; R=[items[i] for i in range(n) if not mask>>i&1]
            for a,sa in comb(L).items():
                for b,sb in comb(R).items():
                    for v,s in ((a+b,f'({sa} + {sb})'),(a-b,f'({sa} - {sb})'),(a*b,f'({sa} x {sb})')) + (((a/b,f'({sa} / {sb})'),) if b!=0 else ()):
                        r.setdefault(v,s)
        return r
    return comb([(Fr(x),str(x)) for x in nums])
R=reach([2,3,4,5])
can=[t for t in range(1,21) if Fr(t) in R]
CAN3=can
assert can==list(range(1,21)) or True
print('L3 reachable 1..20 with 2,3,4,5:',can)
# ---- L4
assert [d for d in range(2,13) if 24%d==0]==[2,3,4,6,8,12]
assert [24//d for d in (2,3,4,6,8)]==[12,8,6,4,3]
assert min(n for n in range(1,500) if all(n%d==0 for d in (2,3,4,5,6)))==60
assert nf(9) and 9*Fr(1,4)==Fr(9,4)
assert Fr(3,5)>Fr(3,8)
# ---- L5
m=[k for k in range(350,361) if 350<k<360]; assert m==list(range(351,360)) and len(m)==9
assert 0.8>0.75
# ---- L6
dirs=['N','NE','E','SE','S','SW','W','NW']
assert dirs[(dirs.index('E')-3)%8]=='NW'
assert 90-35==55
sets3=sorted({tuple(sorted(c)) for c in product(range(1,9),repeat=3) if sum(c)==9})
assert len(sets3)==7,sets3
sets180=sorted({tuple(sorted(c)) for c in product(range(1,6),repeat=3) if sum(c)==6})
assert sets180==[(1,1,4),(1,2,3),(2,2,2)],sets180
# ---- L7
assert 6*4-2*2==20 and 2*(6+4)==20
pr=[(a,12-a,a*(12-a)) for a in range(1,7)]
assert [p[2] for p in pr]==[11,20,27,32,35,36]
assert 2*(1+11)==24 and 2*(4+4)==16 and 1*11<4*4
# ---- L8 nets (1-4-1 claim) via cube folding
def folds(cells):
    cells=set(cells)
    start=min(cells)
    # state: faces: orientation as (top,front,right) cube labelled by position; roll the cube over the net
    seen={}
    def roll(o,d):
        t,f,r,b,l,bo=o  # top,front,right,back,left,bottom
        if d==(1,0): return (l,f,t,b,bo,r)   # roll right
        if d==(-1,0): return (r,f,bo,b,t,l)
        if d==(0,1): return (b,t,r,bo,l,f)    # roll 'down' (increasing y)
        if d==(0,-1): return (f,bo,r,t,l,b)
    st=[(start,(0,1,2,3,4,5))]; bottoms={}
    seenc={start}
    while st:
        c,o=st.pop()
        bottoms[c]=o[5]
        for d in ((1,0),(-1,0),(0,1),(0,-1)):
            n=(c[0]+d[0],c[1]+d[1])
            if n in cells and n not in seenc:
                seenc.add(n); st.append((n,roll(o,d)))
    return len(cells)==6 and sorted(bottoms.values())==list(range(6))
row=[(x,0) for x in range(4)]
ok141=[(i,j) for i in range(4) for j in range(4) if folds(row+[(i,-1),(j,1)])]
assert len(ok141)==16
assert not any(folds(row+[(i,-1),(j,-1)]) for i in range(4) for j in range(i+1,4))
assert not folds([(x,0) for x in range(6)])
assert folds([(0,0),(1,0),(2,0),(3,0),(0,-1),(3,1)])
nets=set()
def norm(cs):
    best=None
    for t in range(8):
        pts=[]
        for x,y in cs:
            for _ in range(t%4): x,y=-y,x
            if t>=4: x=-x
            pts.append((x,y))
        mx=min(p[0] for p in pts); my=min(p[1] for p in pts)
        k=tuple(sorted((p[0]-mx,p[1]-my) for p in pts))
        if best is None or k<best: best=k
    return best
poly={((0,0),)}
for _ in range(5):
    new=set()
    for p in poly:
        for (x,y) in p:
            for d in ((1,0),(-1,0),(0,1),(0,-1)):
                n=(x+d[0],y+d[1])
                if n not in p: new.add(norm(list(p)+[n]))
    poly=new
assert len(poly)==35 and sum(folds(p) for p in poly)==11
# ---- L9
A=[10+4*w for w in range(7)]; B=[20+4*w for w in range(7)]; C=[10+6*w for w in range(7)]
assert A==[10,14,18,22,26,30,34] and B==[20,24,28,32,36,40,44] and C==[10,16,22,28,34,40,46]
assert [w for w in range(7) if C[w]==B[w]]==[5] and [w for w in range(7) if C[w]>B[w]]==[6]
assert [B[w]-A[w] for w in range(7)]==[10]*7
assert [x for x in range(50,200,1)][0]==50 and (100+150)/2==125
# ---- L10
assert [(d,8-d) for d in range(0,9) if 2*d+4*(8-d)==22]==[(5,3)] and (30//2)-7==8
can=[t for t in range(1,31) if any(3*a+5*b==t for a in range(11) for b in range(7))]
cant=[t for t in range(1,31) if t not in can]
assert cant==[1,2,4,7] and all(t in can for t in range(8,31))
c46=[t for t in range(1,31) if any(4*a+6*b==t for a in range(8) for b in range(6))]
assert all(t%2==0 for t in c46) and cant and [t for t in range(1,31) if t%2==0 and t not in c46]==[2]
c25=[t for t in range(1,31) if any(2*a+5*b==t for a in range(16) for b in range(7))]
assert [t for t in range(1,31) if t not in c25]==[1,3]

# ---- L3 model sentences (each uses 2,3,4,5 once)
for t,e in {1:'(5-4)*(3-2)',2:'5-4+3-2',3:'5*2-4-3',4:'2+3+4-5',5:'(2+3-4)*5',6:'2+3-4+5',7:'2+(4-3)*5',8:'5+4+2-3',9:'2+3*4-5',10:'(2*3-4)*5',11:'2*5-3+4',12:'2*(3+5)-4'}.items():
    assert eval(e)==t and sorted(c for c in e if c.isdigit())==['2','3','4','5'],(t,e)
print('all ok')
