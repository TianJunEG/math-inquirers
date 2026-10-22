"""Verifies every Level 3 mathematician-story try-it answer (docs/stories/final_p3.json, p3/stories.json)."""
from fractions import Fraction as F
import itertools
ok=[]
def chk(n,c,msg): ok.append((n,c)); print(n,'OK' if c else 'FAIL',msg)
# 1 Rozsa Peter: x -> 2x+1 from 5
x=5; seq=[]
for _ in range(5): x=2*x+1; seq.append(x)
chk(1,seq==[11,23,47,95,191],seq)
# 2 Joan Clarke: A+A+A = BA, distinct digits, B != 0
s=[(a,b) for a in range(10) for b in range(1,10) if a!=b and 3*a==10*b+a]
chk(2,s==[(5,1)],s)
# 3 Napier rod for 9
r=[9*k for k in range(1,10)]; t=[v//10 for v in r]; o=[v%10 for v in r]
chk(3,r==[9,18,27,36,45,54,63,72,81] and t==list(range(0,9)) and o==list(range(9,0,-1)) and all(a+b==9 for a,b in zip(t,o)),r)
# 4 Bhaskara pearls: x/2 + x/4 + 5 = x
s=[x for x in range(1,200) if F(x,2)+F(x,4)+5==x]
chk(4,s==[20] and 10+5+5==20,s)
# 5 Sun Zi
chk(5,23%3==2 and 23%5==3 and 23%7==2,'23')
s=[n for n in range(10,21) if n%4==1 and n%3==2]
chk(5,s==[17],s)
# 6 al-Hassar
chk(6,F(2,3)==F(8,12) and F(3,4)==F(9,12) and F(3,4)>F(2,3),'3/4>2/3')
# 7 Uhlenbeck
chk(7,2*(6+4)==20 and 2*(5+5)==20 and 6*4==24 and 5*5==25 and 25-24==1,'25>24')
# 8 Ibn al-Haytham
chk(8,90-30==60 and 60+60==120,'120')
# 9 Zu Chongzhi
chk(9,24//4==6 and 4*365+4*F(1,4)==1461,'1461')
# 10 Smullyan: Ana says Ben knave; Ben says both knights. True = knight
sol=[]
for a,b in itertools.product([True,False],repeat=2):
    sa=(not b); sb=(a and b)
    if (a==sa) and (b==sb): sol.append((a,b))
chk(10,sol==[(True,False)],sol)
assert all(c for _,c in ok); print('ALL OK')
