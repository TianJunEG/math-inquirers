"""Brute-force verification for the P3 fix pass (sneak-peek puzzles, Go further answers, changed worksheet / exit answers, party menu, diagnostic). Run: python3 docs/audit/verify_fixpass_p3.py"""
import json, os, itertools
from itertools import permutations, product
from fractions import Fraction
R=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..')
ok=True
def chk(n,c,d=''):
    global ok; ok&=bool(c); print(('PASS ' if c else 'FAIL ')+n+(' '+str(d) if d else ''))
# ---- sneak-peek puzzles (L1-L10), as printed in p3/gifted.json ----
chk('L1 sp1 biggest from 4,0,9 = 940',max(int(''.join(p)) for p in permutations('409'))==940)
odd=sorted(int(''.join(p)) for p in permutations('4093') if p[0]!='0' and int(p[-1])%2); chk('L1 sp2 smallest odd 3049',odd[0]==3049)
nums=sorted(int(''.join(p)) for p in permutations('2458'))
inr=[n for n in nums if 4000<n<6000]; chk('L1 go 12 numbers, closest 4852',len(inr)==12 and min(inr,key=lambda n:abs(n-5000))==4852)
chk('L2 sp1 2A5+134=389 A=5',[a for a in range(10) if int(f'2{a}5')+134==389]==[5])
chk('L2 sp2 4000-1250',4000-1250==2750)
sums=[]
for p in permutations('123456789',6):
    a=int(''.join(p[:3]))+int(''.join(p[3:]))
    if a<1000 and sorted(str(a)+''.join(p))==list('123456789'): sums.append(a)
chk('L2 go: two 3-digit numbers and their sum use cards 1-9 once each; smallest sum 459, biggest 981',(min(sums),max(sums))==(459,981) and all(sum(map(int,str(x)))==18 for x in sums),(min(sums),max(sums)))
chk('L3 sp1',[x for x in (49,54,63) if x%7==0]==[49,63]); chk('L3 sp2',(6*14,6*6)==(84,36))
chk('L3 go 5s touch 2 dots, 9s touch 10',(len({5*k%10 for k in range(1,11)}),len({9*k%10 for k in range(1,11)}))==(2,10))
chk('L4 sp1',(70-30)//2==20); chk('L4 sp2 pen $2',[p for p in range(0,10) if p+(p+5)==9]==[2])
chk('L4 go towers 8,10,12 and 7,10,13',8+10+12==30 and 7+10+13==30)
chk('L5 sp1',(13//4,13%4)==(3,1)); chk('L5 sp2',(6//6,6%6)==(1,0))
chk('L5 go sizes leaving 1',[k for k in range(2,9) if 49%k==1]==[2,3,4,6,8] and 49%5==4 and 49%7==0)
chk('L6 sp2 1/3>1/4',Fraction(1,3)>Fraction(1,4))
three=[(a,b,c) for a,b,c in itertools.combinations(range(2,25),3) if Fraction(1,a)+Fraction(1,b)+Fraction(1,c)==Fraction(1,2)]
chk('L6 go only 1/4+1/6+1/12 with 3 different unit pieces with denominators 2..24? (also 1/3+1/12+1/12 repeats)',(4,6,12) in three,three)
chk('L7 sp1',(3*2,2*(3+2))==(6,10)); chk('L7 sp2 12 cm2 perimeters',sorted({2*(a+12//a) for a in (1,2,3,4,6,12)})==[14,16,26])
chk('L7 go 16 squares',[2*(a+16//a) for a in (1,2,4)]==[34,20,16])
chk('L10 sp orders',len(list(permutations('ABM')))==6 and [''.join(p) for p in permutations('ABM') if p.index('B')<p.index('M')]==['ABM','BAM','BMA'])
chk('L10 go ribbon',[15,25,35,45]==[(120-60)//4+10*i for i in range(4)] and 15+25+35+45==120)
chk('L9 sp2 3:45+1h30',(3*60+45+90)==5*60+15)
# ---- changed worksheet / exit items ----
chk('L2 Q1b 5A2-216=316 A=3',[a for a in range(10) if int(f'5{a}2')-216==316]==[3])
chk('L2 exit 5A3+126=689 A=6',[a for a in range(10) if int(f'5{a}3')+126==689]==[6])
sol=[(a,b,c) for a in range(10) for b in range(10) for c in range(10) if 7000+a*100+3-(b*1000+400+60+c)==2538]
chk('L2 think harder 7A03-B46C=2538',(0,4,5) in sol,sol)
chk('L5 exit 29 in cars of 4',(29//4,29%4,-(-29//4))==(7,1,8))
chk('L7 exit perimeter 12 length 4',[(4*w) for w in range(1,10) if 2*(4+w)==12]==[8])
def right_corners(P):
    n=len(P); c=0
    for i in range(n):
        a,b,d=P[i-1],P[i],P[(i+1)%n]
        v1=(a[0]-b[0],a[1]-b[1]); v2=(d[0]-b[0],d[1]-b[1])
        dot=v1[0]*v2[0]+v1[1]*v2[1]; cr=v1[0]*v2[1]-v1[1]*v2[0]
        if dot==0: c+=1
    return c
def inside_right(P):  # interior right angles only (convex ones); orientation from signed area
    n=len(P); area=sum(P[i][0]*P[(i+1)%n][1]-P[(i+1)%n][0]*P[i][1] for i in range(n))
    s=1 if area>0 else -1; c=0
    for i in range(n):
        a,b,d=P[i-1],P[i],P[(i+1)%n]
        v1=(b[0]-a[0],b[1]-a[1]); v2=(d[0]-b[0],d[1]-b[1])
        dot=v1[0]*v2[0]+v1[1]*v2[1]; cr=v1[0]*v2[1]-v1[1]*v2[0]
        if dot==0 and cr*s>0: c+=1
    return c
plus=[(1,0),(2,0),(2,1),(3,1),(3,2),(2,2),(2,3),(1,3),(1,2),(0,2),(0,1),(1,1)]
stair=[(0,0),(3,0),(3,1),(2,1),(2,2),(1,2),(1,3),(0,3)]
house=[(0,0),(4,0),(4,3),(2,5),(0,3)]; trap=[(0,0),(5,0),(3,3),(0,3)]
chk('L8 Q2 right angles A 8, B 6, C 3, D 2',[inside_right(P) for P in (plus,stair,house,trap)]==[8,6,3,2],[inside_right(P) for P in (plus,stair,house,trap)])
# ---- L9: party menu (whole and half dollars) ----
pr=dict(pizza=850,wings=600,puffs=400,punch=300,cup=550,ball=250)
ways=[d for c in product(range(5),repeat=6) for d in [dict(zip(pr,c))] if d['punch']>=1 and d['pizza']+d['wings']+d['puffs']+d['cup']>=1 and sum(pr[k]*v for k,v in d.items())==2000]
chk('L9 exactly 15 ways to spend $20 (up to 4 each, 1+ punch, 1+ food)',len(ways)==15)
chk('L9 punch 8 x 250 ml = 2 l',8*250==2000)
chk('L9 Q1 conversions',(200,3000,306,2450,4080//1000,4080%1000,300-4*65)==(200,3000,306,2450,4,80,40))
chk('L9 exit 3:30 + 1h20 = 4:50',(3*60+30+80)==4*60+50)
chk('L9 Q5b 4:35+50 = 5:25; Q5c ends 9:15 pm lasted 1h50 started 7:25',(4*60+35+50)==5*60+25 and (9*60+15-110)==7*60+25)
chk('L9 Go $30 with 12 friends: 3000 ml = 3 l, 2 bottles; 2 punch + 3 cup + 3 ball = $30',12*250==3000 and 2*300+3*550+3*250==3000 and 2*400+2*300+2*550+2*250==3000)
n30=sum(1 for c in product(range(7),repeat=6) if c[3]>=2 and c[0]+c[1]+c[2]+c[4]>=1 and sum(p*v for p,v in zip(pr.values(),c))==3000); print('  (info) ways to spend $30, 2+ punch, up to 6 each:',n30)
# ---- diagnostic (diag/content/p3.json) ----
d=json.load(open(os.path.join(R,'diag','content','p3.json'),encoding='utf8'))
chk('DIAG warm-up 47+38, 305-128, 4x8, 24/3',(47+38,305-128,4*8,24//3)==(85,177,32,8)==tuple(int(x['a']) for x in d['foundation']))
chk('DIAG M1 2_7+358=645 -> 8',[a for a in range(10) if 200+10*a+7+358==645]==[8]==[int(d['core'][0]['a'])])
chk('DIAG M2 36',(48//4*3,)==(36,) and d['core'][1]['a']=='36')
chk('DIAG M3 52 in rows of 7: 3 left over (single answer)',(52//7,52%7)==(7,3) and d['core'][2]['a']=='3' and 'left over' in d['core'][2]['q'] and 'full rows' not in d['core'][2]['q'])
chk('DIAG M4 3/4=9/12',Fraction(3,4)==Fraction(9,12) and d['core'][3]['a']=='9')
chk('DIAG M5 area 9x4 = 36 (perimeter 26)',9*4==36 and 2*(9+4)==26 and d['core'][4]['a'].startswith('36') and 'units' not in d['core'][4]['q'])
chk('DIAG M6 2:45 pm + 1 h 50 = 4:35 pm',(14*60+45+110)==16*60+35)
chk('DIAG S1 6n-4=38 -> 7',[n for n in range(100) if 6*n-4==38]==[7])
dig=[10*a+b for a,b in permutations([2,5,8,0],2) if a]
chk('DIAG S2 digits 2,5,8,0 -> 9 numbers; wrong answers 12 and 16',len(dig)==9==int(d['stretch'][1]['a']) and len(list(permutations([2,5,8,0],2)))==12 and len(list(product([2,5,8,0],repeat=2)))==16,sorted(dig))
print('ALL PASS' if ok else 'SOME FAILED'); raise SystemExit(0 if ok else 1)
