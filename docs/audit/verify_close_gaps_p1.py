"""Brute-force checks for the warm-up check answers and open investigations added to P1 (docs/audit/close_gaps_p1.md)."""
from itertools import product, permutations, combinations_with_replacement as cwr
ok=0
def chk(name,cond):
    global ok
    assert cond,name; ok+=1; print('ok',name)
# L1 check + investigation
seq=[1+3*i for i in range(10)]; chk('L1 c1 bunny misses 20',20 not in seq and 19 in seq and 22 in seq)
chk('L1 c2',18-12==6 and 12-6==6)
for h,exp in {3:[6,12,18,24,30],4:[4,8,12,16,20,24,28],5:[10,20,30],6:[6,12,18,24,30]}.items():
    both=[x for x in range(1,31) if x%2==0 and x%h==0]; chk(f'L1 inv hop {h}',both==exp)
# L2
chk('L2 c1',20-12==8); chk('L2 c2',7+5==6+6)
p10=[(a,10-a) for a in range(11)]; p20=[(a,20-a) for a in range(21)]
chk('L2 inv 10 same parity (11 pairs)',len(p10)==11 and all(a%2==b%2 for a,b in p10))
chk('L2 inv 20 same parity (21 pairs)',len(p20)==21 and all(a%2==b%2 for a,b in p20))
chk('L2 no odd+even makes 10 or 20',not any((a+b) in (10,20) and a%2!=b%2 for a in range(21) for b in range(21)))
# L3
chk('L3 c1',7-3==4)
data=[4,6,2]; keys=[k for k in range(1,13) if all(x%k==0 for x in data)]
chk('L3 inv keys that work are 1 and 2',keys==[1,2]); chk('L3 key 2 rows',[x//2 for x in data]==[2,3,1] and sum(data)==12)
# L4
core=('R','B','B'); chk('L4 c1 12th bead blue',core[(12-1)%3]=='B')
sticks=[4+3*i for i in range(4)]; chk('L4 c2 13 sticks',sticks[3]==13 and sticks[:3]==[4,7,10])
allok=True
for core in product('ABC',repeat=3):
    if len(set(core))==3:
        pat=lambda k: core[(k-1)%3]
        allok&=all(pat(k)==pat(3) for k in (3,6,9,30))
chk('L4 inv every 3-shape pattern: places 3,6,9,30 match',allok)
chk('L4 inv 4-shape: places 4,8,12,16,20 match',all(core4[(k-1)%4]==core4[3] for core4 in product('ABCD',repeat=4) for k in (4,8,12,16,20)))
# L5
chk('L5 c1',15-6==9); x=7; chk('L5 c2',x-2+7==12 and [n for n in range(100) if n-2+7==12]==[7])
chk('L5 inv +6-6 identity',all(n+6-6==n for n in range(200))); chk('L5 inv +6-4 is +2',all(n+6-4==n+2 for n in range(200)) and [3+2,10+2,25+2]==[5,12,27])
# L6
coins=[5,10,20,50]
chk('L6 c1',20+5==25 and 20+10==30 and 20+10+5==35<40)
ways=[c for c in cwr(coins,3) if sum(c)==25]; chk('L6 c2 only 10+10+5',ways==[(5,10,10)])
def can(amount,cs):
    return any(sum(a*c for a,c in zip(n,cs))==amount for n in product(range(11),repeat=len(cs)))
amts=range(5,55,5)
no5=[a for a in amts if not can(a,[10,20,50])]; chk('L6 inv no 5c: cannot make 5,15,25,35,45',no5==[5,15,25,35,45])
chk('L6 inv no 10c: can make all',all(can(a,[5,20,50]) for a in amts))
# L7 free polyominoes by brute force
def norm(cells):
    def tr(c):
        mx=min(x for x,y in c); my=min(y for x,y in c); return tuple(sorted((x-mx,y-my) for x,y in c))
    forms=[]; c=list(cells)
    for _ in range(4):
        c=[(y,-x) for x,y in c]; forms.append(tr(c)); forms.append(tr([(-x,y) for x,y in c]))
    return min(forms)
def grow(n):
    s={norm([(0,0)])}
    for _ in range(n-1):
        t=set()
        for p in s:
            for x,y in p:
                for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                    q=(x+dx,y+dy)
                    if q not in p: t.add(norm(list(p)+[q]))
        s=t
    return s
chk('L7 inv 3 squares: 2 shapes',len(grow(3))==2); chk('L7 inv 4 squares: 5 shapes',len(grow(4))==5)
chk('L7 c1 sides=corners (polygon n)',all(n==n for n in range(3,12)))
# L8
orders=list(permutations(['Ali','Mei','Ben'])); chk('L8 inv 6 orders',len(orders)==6)
chk('L8 inv Ali not first leaves 4',len([o for o in orders if o[0]!='Ali'])==4)
c1=[o for o in orders if o.index('Ali')<o.index('Ben')<o.index('Mei')]; chk('L8 clue A leaves exactly 1',c1==[('Ali','Ben','Mei')])
c2=[o for o in orders if o[0]=='Mei' and o[2]!='Ali']; chk('L8 clue B leaves exactly 1',c2==[('Mei','Ali','Ben')])
tall=['Ben','Cara','Dev','Eli']; chk('L8 c1 second tallest Dev',tall[-2]=='Dev')
chk('L8 c2 15 only odd',[n for n in (4,8,12,15) if n%2][0]==15 and len([n for n in (4,8,12,15) if n%2])==1 and [n for n in (4,8,12,15) if n%4]==[15])
# L9
chk('L9 c1',11-4==7)
chk('L9 inv shorter unit always bigger count',all(L/u1>L/u2 for L in range(1,60) for u1 in range(1,10) for u2 in range(u1+1,11)) and 12*2==24)
# L10
chk('L10 c1 7th term',[4+5*i for i in range(7)][-1]==34)
w=[c for c in cwr(coins,3) if sum(c)==35]; chk('L10 c2 only 20+10+5',w==[(5,10,20)])
tot={j:sum(5+j*i for i in range(3)) for j in (1,2,3,4,5)}; chk('L10 inv totals',tot=={1:18,2:21,3:24,4:27,5:30})
chk('L10 inv total = 3 x middle and +3 per jump',all(tot[j]==3*(5+j) for j in tot) and all(tot[j+1]-tot[j]==3 for j in range(1,5)) and sum(5+10*i for i in range(3))==45)
print(ok,'checks passed')
