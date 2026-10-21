"""Brute-force checks for every 'find all' / 'always true' / answer claim in the P3 close-the-gaps additions. Run: python3 docs/audit/verify_gifted_p3.py"""
from itertools import permutations, product
ok=True
def chk(name,cond,detail=''):
    global ok; ok&=bool(cond); print(('PASS ' if cond else 'FAIL ')+name+(' '+str(detail) if detail else ''))
ds=lambda n:sum(map(int,str(n)))
# L1
chk('L1 check1',2*1000+13*100+4*10==3340)
odd=sorted(int(''.join(p)) for p in permutations('4093') if p[0]!='0' and int(p[-1])%2==1); chk('L1 check2 smallest odd 3049',odd[0]==3049,odd[:3])
def nums(cards): return sorted(set(int(''.join(p)) for p in permutations(cards) if p[0]!='0'))
a=nums('0123'); b=nums('1234')
chk('L1 inv 18 and 24',(len(a),len(b))==(18,24))
chk('L1 inv start-1 list',[x for x in a if x//1000==1]==[1023,1032,1203,1230,1302,1320])
chk('L1 inv counts 6/6/6/0',[len([x for x in a if x//1000==d]) for d in (1,2,3,0)]==[6,6,6,0])
chk('L1 inv evens 10 vs 12',(len([x for x in a if x%2==0]),len([x for x in b if x%2==0]))==(10,12))
# L2
chk('L2 check1',4000-1250==2750)
sol=[d for d in range(10) if int(f'3{d}47')+2865==6212]; chk('L2 check2 A=3 only',sol==[3])
allok=True; vals=set(); n95=[]
for n in range(100,1000):
    a_,c_=n//100,n%10
    if a_>c_:
        r=int(str(n)[::-1]); d=n-r
        if d!=99*(a_-c_): allok=False
        vals.add(d)
        if d==495: n95.append(n)
chk('L2 inv reverse-subtract = 99 x (first - last) for ALL 3-digit numbers with first>last',allok)
chk('L2 inv answers are the 99 table up to 891',sorted(vals)==[99*k for k in range(1,10)])
chk('L2 inv 842-248=594, 720-27=693',842-248==594 and 720-27==693)
chk('L2 inv 495 only when digits differ by 5',all((n//100-n%10)==5 for n in n95))
# L3
chk('L3 check1',[x for x in (49,54,63,74,84) if x%7==0]==[49,63,84])
chk('L3 check2',(42*2,42-6)==(84,36))
dsum=lambda t:[ds(t*k) for k in range(1,13)]
chk('L3 inv 9s digit sums',dsum(9)==[9]*10+[18,9],dsum(9))
chk('L3 inv 3s all multiples of 3',all(x%3==0 for x in dsum(3)))
chk('L3 inv 6s all multiples of 3',all(x%3==0 for x in dsum(6)),dsum(6))
chk('L3 inv 4s NOT',not all(x%3==0 for x in dsum(4)),dsum(4))
# L4
chk('L4 check1',(70+30)//2==50 and 70-50==20)
chk('L4 check2',(9-5)//2==2)
rows=[(n,13+n,5+n,13+n-5-n,18+2*n) for n in range(0,6)]; print(rows)
chk('L4 inv diff constant 8, total +2',all(r[3]==8 for r in rows) and all(rows[i+1][4]-rows[i][4]==2 for i in range(5)))
dbl=[n for n in range(0,100) if 13+n==2*(5+n)]; tr=[n for n in range(-5,100) if 13+n==3*(5+n)]
chk('L4 inv double only at n=3 (16 and 8)',dbl==[3]); chk('L4 inv triple only at n=-1 (past)',tr==[-1],tr)
# L5
chk('L5 check1',7*5+4==39)
chk('L5 inv 3 in a row has exactly one multiple of 3',all(sum(1 for k in range(n,n+3) if k%3==0)==1 for n in range(1,3000)))
chk('L5 inv 4 in a row, 4 table',all(sum(1 for k in range(n,n+4) if k%4==0)==1 for n in range(1,3000)))
chk('L5 inv 2 in a row, 3 table not always',any(sum(1 for k in range(n,n+2) if k%3==0)==0 for n in range(1,50)))
# L6
from fractions import Fraction as F
w=[(a,b,c) for a in range(0,3) for b in range(0,4) for c in range(0,7) if F(1,2)*a+F(1,4)*b+F(1,8)*c==F(3,4)]
chk('L6 inv 3/4: 6 ways',len(w)==6,w)
w1=[(a,b,c) for a in range(0,3) for b in range(0,5) for c in range(0,9) if F(1,2)*a+F(1,4)*b+F(1,8)*c==1]
chk('L6 inv whole: 9 ways',len(w1)==9,w1)
chk('L6 check 3/4=6/8',F(3,4)==F(6,8)); chk('L6 1/3>1/4',F(1,3)>F(1,4))
# L7
chk('L7 check1',[(3*b) for b in range(1,8) if 2*(3+b)==14]==[12])
chk('L7 check2',[(2*(1+12),2*(2+6),2*(3+4))]==[(26,16,14)])
chk('L7 inv square->(n+1)(n-1): same perimeter, area -1 for all n 2..500',all(2*((n+1)+(n-1))==4*n and n*n-(n+1)*(n-1)==1 for n in range(2,500)))
# L8 staircase
def stair(k):
    # columns heights 1..k, unit squares; outline vertices
    pts=[(0,0),(k,0)]
    for i in range(k,0,-1):
        pts.append((i,i)); pts.append((i-1,i))
    pts=pts[:2]+[]  # rebuilt below
    pts=[(0,0),(k,0),(k,1)]
    x=k; y=1
    out=[(0,0),(k,0)]
    for i in range(k,0,-1):  # column i (x from i-1 to i) has height i
        out.append((i,i)); out.append((i-1,i))
    return out
def corners(poly):
    n=len(poly); area2=sum(poly[i][0]*poly[(i+1)%n][1]-poly[(i+1)%n][0]*poly[i][1] for i in range(n))
    sgn=1 if area2>0 else -1; conv=refl=0
    for i in range(n):
        a,b,c=poly[i-1],poly[i],poly[(i+1)%n]
        cr=(b[0]-a[0])*(c[1]-b[1])-(b[1]-a[1])*(c[0]-b[0])
        if cr==0: continue
        if cr*sgn>0: conv+=1
        else: refl+=1
    return conv,refl
res={k:corners(stair(k)) for k in (1,2,3,4,10)}; print(res)
chk('L8 inv staircase: right=k+3, bigger=k-1, total=2k+2',all(res[k]==(k+3,k-1) for k in res))
chk('L8 inv 2-step has 3 squares, 3-step 6',(1+2,1+2+3)==(3,6))
chk('L8 check: 10-step totals 13,9,22',res[10]==(13,9) and sum(res[10])==22)
# L9
ways=[(a,b,c) for a in range(0,3) for b in range(0,6) for c in range(0,11) if 20*a+10*b+5*c==50]
chk('L9 inv 12 ways',len(ways)==12,ways)
chk('L9 inv fewest 3 coins (2,1,0), most 10 coins (0,0,10)',min(sum(w) for w in ways)==3 and max(sum(w) for w in ways)==10 and [w for w in ways if sum(w)==3]==[(2,1,0)])
chk('L9 check1',2040<2400)
h,m=15,50+85; h+=m//60; m%=60; chk('L9 check2 17:15',(h,m)==(17,15))
# L10
chk('L10 check1 orders with Ben before Mei',len([p for p in permutations(['Ali','Ben','Mei']) if p.index('Ben')<p.index('Mei')])==3)
hs=lambda n:n*(n-1)//2
chk('L10 inv 1,3,6,10,15 and 10 friends 45',[hs(n) for n in range(2,7)]==[1,3,6,10,15] and hs(10)==45)
chk('L10 inv 20 handshakes impossible',all(hs(n)!=20 for n in range(2,100)) and hs(6)==15 and hs(7)==21)
chk('L10 check2 bar 50',(40+60)//2==50)
print('ALL PASS' if ok else 'SOME FAILED')
raise SystemExit(0 if ok else 1)
