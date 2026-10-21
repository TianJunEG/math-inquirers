"""Verification + diagnostic simulation for docs/audit/journey_p2.md. Run: python3 -I docs/audit/journey_p2.py"""
from itertools import product, permutations
from math import comb
from fractions import Fraction

print("== Lesson key spot checks ==")
# L1
n3 = sorted({int(''.join(p)) for p in permutations('047') if p[0]!='0'}); print('L1 PRE1 4,0,7:', n3)
print('L1 Q3 0,5,9:', sorted({int(''.join(p)) for p in permutations('059') if p[0]!='0'}))
print('L1 Q2 2,7,4 closest to 500:', min((abs(int(''.join(p))-500),int(''.join(p))) for p in permutations('274')))
print('L1 Q6a:', [n for n in range(100,1000) if n//100==4 and n%10==(n//10)%10+2 and sum(map(int,str(n)))==12])
print('L1 Q6b:', [n for n in range(100,1000) if sum(map(int,str(n)))==3])
print('L1 mirror 200-299:', len([n for n in range(200,300) if str(n)==str(n)[::-1]]))
print('L1 C: digits in pages 1-120:', sum(len(str(i)) for i in range(1,121)), ' threes 300-399:', sum(str(i).count('3') for i in range(300,400)))
# L2
print('L2 exit 4A6+37B=801:', [(a,b) for a in range(10) for b in range(10) if 406+a*10+370+b==801-0 or (400+a*10+6)+(370+b)==801])
print('L2 Q1a:', [(a,b) for a in range(10) for b in range(10)][0:0] or [(x,y) for x in range(10) for y in range(10) if 204+x*10+350+y==579])
print('L2 PRE1 4A6+237=683:', [a for a in range(10) if 406+a*10+237==683])
# L3
print('L3 Q7 2b+3t=17 b,t>=1:', [(b,t) for b in range(1,9) for t in range(1,6) if 2*b+3*t==17])
print('L3 Q3 7 animals 20 legs:', [(h,7-h) for h in range(8) if 2*h+4*(7-h)==20])
print('L3 C6 sweets 20-30 rem3 (4), rem2 (5):', [n for n in range(20,31) if n%4==3 and n%5==2])
print('L3 C5 tri 3 + car 4 =30:', [(t,c) for t in range(1,11) for c in range(1,8) if 3*t+4*c==30])
# L4
print('L4 Q6 both 3s and 4s to 36:', [n for n in range(1,37) if n%3==0 and n%4==0])
print('L4 MATH 30 letters, Ts:', sum(1 for i in range(1,31) if 'MATH'[(i-1)%4]=='T'))
# L5
print('L5 Q4 bags:', 3*(6+4))
# L6
toys={'kite':6,'ball':4,'yoyo':3,'bubbles':2,'sticker':1}
bk=[c for r in range(1,6) for c in __import__('itertools').combinations(toys,r) if sum(toys[x] for x in c)==10]; print('L6 baskets =$10:',len(bk),bk)
print('L6 Q2 pay $8 with 5,2,1:', [(a,b,8-5*a-2*b) for a in range(2) for b in range(5) if 8-5*a-2*b>=0])
print('L6 Q6 20c,50c =200:', [(s,e) for s in range(11) for e in range(5) if 20*s+50*e==200])
print('L6 explore S1 pay $10 with 5,2,1 ways:', len([(a,b) for a in range(3) for b in range(6) if 10-5*a-2*b>=0]))
# L7
print('L7 C5 Ben:', [b for b in range(0,9) if b+(b+2)==8])
# L8
print('L8 grid 4x4 squares:', sum((5-k)**2 for k in range(1,5)), ' 5x5:', sum((6-k)**2 for k in range(1,6)))
# L9
print('L9 clock B 4:50pm +35 -> 5:25pm; 10:45am to 12:10pm = ', (12*60+10-(10*60+45)),'min')
# L10
print('L10 PRE1:', [(s,9-s) for s in range(10) if 4*s+3*(9-s)==31])
print('L10 station 3 (70c, 4 coins):', sorted({tuple(sorted(c)) for c in product([5,10,20,50],repeat=4) if sum(c)==70}))
print('L10 C7 4a+3(7-a)=25:', [a for a in range(8) if 4*a+3*(7-a)==25])

print("\n== Diagnostic ==")
def dist(ps):
    d={0:1.0}
    for p in ps:
        nd={}
        for k,v in d.items():
            nd[k]=nd.get(k,0)+v*(1-p); nd[k+1]=nd.get(k+1,0)+v*p
        d=nd
    return d
def place(w,t):
    if t>=6: return 'up?' if (t==8 and w==4) else 'join'
    if t>=4: return 'support/down' if w<=2 else 'join+support'
    return 'down'
PROF={
 'strong-for-age (8y, top)':([.98,.98,.97,.97],[.97,.9,.95,.9,.85,.95],[.6,.55]),
 'typical-for-age (8y)':([.97,.95,.92,.92],[.92,.6,.85,.7,.6,.85],[.2,.15]),
 'weak-for-age (8y)':([.85,.8,.55,.55],[.55,.15,.4,.2,.15,.45],[.02,.02]),
 'younger strong (6y9m, P1 done)':([.98,.98,.95,.95],[.9,.55,.5,.75,.3,.6],[.5,.4]),
 'older weak (9y)':([.92,.9,.75,.75],[.75,.3,.65,.4,.35,.6],[.04,.04]),
 'guesser/rusher':([.9,.5,.5,.85],[.6,.1,.4,.3,.2,.35],[.03,.03]),
}
for name,(w,m,s) in PROF.items():
    dm=dist(m+s); dw=dist(w); out={}
    for tw,pw in dw.items():
        for tm,pm in dm.items():
            k=place(tw,tm); out[k]=out.get(k,0)+pw*pm
    print(f'{name:34s} E[W]={sum(w):.2f} E[T]={sum(m+s):.2f}  '+', '.join(f'{k} {v:.0%}' for k,v in sorted(out.items(),key=lambda x:-x[1])))
print('\nUniform-ability child, P(total of 8 = k) bands; p = per-question success')
for p in [.4,.5,.6,.7,.75,.8,.9]:
    d=dist([p]*8); print(f'p={p:.2f}: P(>=6)={sum(v for k,v in d.items() if k>=6):.0%}  P(4-5)={sum(d[k] for k in (4,5)):.0%}  P(<=3)={sum(d[k] for k in range(4)):.0%}  SD={ (8*p*(1-p))**.5:.2f}')
print('\nPure guess on the 8 scored questions: P(T>=4) with p=.03 =', f"{sum(v for k,v in dist([.03]*8).items() if k>=4):.4%}", ' with p=.1:', f"{sum(v for k,v in dist([.1]*8).items() if k>=4):.2%}")
print('Warm-up: P(W<=2) if all 4 at p=.95:', f"{sum(v for k,v in dist([.95]*4).items() if k<=2):.2%}", ' at p=.9:', f"{sum(v for k,v in dist([.9]*4).items() if k<=2):.2%}")
print('Share of a mid child (p=.7 mains): T>=6 requires ~', 'see table')
# alt cut: 7/8 etc
print('\nProposed change: weighted score (core 1, stretch 0.5 -> out of 7)')

print("\n== Alternative rule B (core 6 only decides; stretch is bonus) ==")
def placeB(w,c,s):
    if c>=5: return 'up?' if (c==6 and s==2 and w==4) else 'join'
    if c>=3: return 'down' if w<=2 else 'join+support'
    return 'down'
for name,(w,m,s) in PROF.items():
    dc=dist(m); ds=dist(s); dw=dist(w); out={}
    for tw,pw in dw.items():
        for tc,pc in dc.items():
            for ts,ps in ds.items():
                k=placeB(tw,tc,ts); out[k]=out.get(k,0)+pw*pc*ps
    print(f'{name:34s} '+', '.join(f'{k} {v:.0%}' for k,v in sorted(out.items(),key=lambda x:-x[1])))
print('\nCore-only (6 items) uniform ability: P(core>=5), P(3-4), P(<=2)')
for p in [.4,.5,.6,.7,.8,.9]:
    d=dist([p]*6); print(f'p={p:.1f}: >=5 {sum(d[k] for k in (5,6)):.0%}  3-4 {sum(d[k] for k in (3,4)):.0%}  <=2 {sum(d[k] for k in range(3)):.0%}')

print("\n== Fix checks ==")
print('L2 proposed exit 3[x]4 + 257 = 601:', [x for x in range(10) if 304+10*x+257==601])
print('L2 Q2a 7x8 - 32y = 453:', [(x,y) for x in range(10) for y in range(10) if 708+10*x-(320+y)==453], ' Q2b 5x3 - y67 = 276:', [(x,y) for x in range(10) for y in range(10) if 503+10*x-(y*100+67)==276])
print('L9 proposed Q5c 10:45 to 11:30 =', (11*60+30)-(10*60+45),'min;  proposed check 3l/5l: 5-3 =',5-3)
print('L5 proposed PRE: machine +7 then x2 OUT 20 -> IN', (20//2)-7)
print('L8 proposed PRE: 2 layers of 2x3 =', 2*3*2)

print("\n== Journey scores (P participate, D difficulty fit, F fun, C confidence, M motivation, S social/online) ==")
SC={ # lesson: {persona: [P,D,F,C,M,S]}
1:{'L':[4,3,4,3,3,3],'M':[5,4,4,4,4,4],'H':[4,2,3,3,3,3]},
2:{'L':[3,2,3,3,2.5,3],'M':[4,2.5,4,3,4,4],'H':[5,4,5,4,4,3]},
3:{'L':[4,2.5,4,3,3,3.5],'M':[5,3.5,4.5,4,4,4],'H':[5,3,4,4,4,3]},
4:{'L':[4,3,4,3,3,3.5],'M':[5,4,4,4,4,4],'H':[5,3,4,4,4,3]},
5:{'L':[3,2,3,3,3,3],'M':[4,3,4,3.5,4,4],'H':[5,3.5,4.5,4,4.5,3.5]},
6:{'L':[4,3,4.5,4,3.5,3.5],'M':[5,4,5,4,4.5,4],'H':[5,3,4.5,4,4,3.5]},
7:{'L':[4,3,4,3.5,3.5,3.5],'M':[5,4,4.5,4,4,4],'H':[5,3,3.5,3.5,3.5,3]},
8:{'L':[4,2,4,3,3,3],'M':[5,3,4.5,3.5,4,4],'H':[5,3.5,4.5,4,4,3.5]},
9:{'L':[3,1.5,3.5,2,2.5,3],'M':[4,2.5,4,3,3.5,4],'H':[5,3.5,4.5,4,4,3.5]},
10:{'L':[3.5,2.5,3.5,3.5,3.5,3],'M':[4,3.5,4.5,4,4.5,4],'H':[5,3,4.5,4,4.5,4]},
}
means={}
print('| Lesson | LOW | MIDDLE | HIGH | lesson mean |\n|---|---|---|---|---|')
for n,d in SC.items():
    m={k:sum(v)/6 for k,v in d.items()}; means.update({(n,k):x for k,x in m.items()})
    print(f"| L{n} | {m['L']:.2f} | {m['M']:.2f} | {m['H']:.2f} | {sum(m.values())/3:.2f} |")
for k in 'LMH':
    print(k,'mean across lessons',f"{sum(means[(n,k)] for n in SC)/10:.2f}")
rk=sorted(means.items(),key=lambda x:x[1]); print('weakest 6:',[(f'L{n}-{k}',round(v,2)) for (n,k),v in rk[:6]]); print('strongest 4:',[(f'L{n}-{k}',round(v,2)) for (n,k),v in rk[::-1][:4]])
dims='PDFCMS'
for k in 'LMH':
    print(k,'by dimension:',{d:round(sum(SC[n][k]['PDFCMS'.index(d)] for n in SC)/10,2) for d in dims})

print("\n== Rule C: >=5 join; 3-4 join+support (down if warm-up<=2); <=2 down; 8/8+4/4 may try up ==")
def placeC(w,t):
    if t>=5: return 'up?' if (t==8 and w==4) else 'join'
    if t>=3: return 'down' if w<=2 else 'join+support'
    return 'down'
for name,(w,m,s) in PROF.items():
    dm=dist(m+s); dw=dist(w); out={}
    for tw,pw in dw.items():
        for tm,pm in dm.items():
            k=placeC(tw,tm); out[k]=out.get(k,0)+pw*pm
    print(f'{name:34s} '+', '.join(f'{k} {v:.0%}' for k,v in sorted(out.items(),key=lambda x:-x[1])))
print('Uniform ability, total of 8: P(T>=5)')
for p in [.4,.5,.6,.7,.8]:
    d=dist([p]*8); print(f' p={p}: {sum(v for k,v in d.items() if k>=5):.0%}')
# how many main-6 correct does a P(stretch)=.2 typical child need; chance of 8/8 for a strong child
d=dist([.97,.9,.95,.9,.85,.95,.6,.55]); print('strong child P(8/8)=',f"{d[8]:.0%}",' P(7)=',f"{d[7]:.0%}", ' P(6)=',f"{d[6]:.0%}")
