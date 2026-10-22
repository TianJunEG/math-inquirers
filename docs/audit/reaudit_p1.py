"""Re-audit helper for Math Inquirers Level 1 (P1). Run: python3 docs/audit/reaudit_p1.py
Part 1 (BLIND scores, written before any earlier audit file was opened) and diagnostic simulations.
Part 2 (comparison with baselines) is appended further down."""
import itertools, math
from fractions import Fraction

# ---------------- INSTRUMENT A: 12 criteria x 10 lessons (BLIND, current material) -------------
CRIT = ['LTHC','Depth','Generalise','Justify','Multi-path','Ladder','Inquiry/talk','Complexity','Posing','Metacog','Pacing','Extension']
A_NOW = {
 1:[2,2,2,2,1,2,2,1,2,2,1,2],
 2:[2,1,2,2,1,2,2,1,2,2,1,2],
 3:[2,1,1,2,1,2,2,2,2,2,1,1],
 4:[2,2,2,2,1,2,2,1,2,2,1,2],
 5:[2,1,2,2,1,2,1,1,2,2,1,1],
 6:[2,2,2,2,2,2,2,2,2,2,1,2],
 7:[2,1,1,1,1,2,1,1,2,2,1,2],
 8:[2,1,1,2,1,2,2,2,2,2,1,2],
 9:[2,1,2,2,1,2,1,2,2,2,1,1],
 10:[2,1,2,1,1,2,2,2,2,2,1,2],
}
# ---------------- INSTRUMENT B: [participate, fit, fun, confidence, motivation, social] -------------
DIM = ['Participate','Difficulty fit','Fun','Confidence','Motivation','Social/online']
B_NOW = {
 'LOW':   {1:[5,3,4,4,3,3],2:[5,2,4,3,3,3],3:[5,4,4,4,4,3],4:[5,3,4,3,3,3],5:[4,2,4,2,3,3],
           6:[4,3,4,3,4,3],7:[4,3,4,3,3,3],8:[5,2,3,3,3,3],9:[4,2,3,3,3,3],10:[4,2,3,3,3,3]},
 'MIDDLE':{1:[5,4,4,4,4,4],2:[5,4,4,4,4,4],3:[5,4,4,4,4,4],4:[5,4,5,4,4,4],5:[5,3,4,3,4,4],
           6:[5,4,5,4,4,4],7:[5,3,4,4,4,4],8:[5,3,4,4,4,4],9:[5,3,4,4,4,4],10:[5,3,4,4,4,4]},
 'HIGH':  {1:[5,3,4,4,4,4],2:[5,3,4,4,4,4],3:[5,3,3,4,3,4],4:[5,4,5,4,4,4],5:[5,4,4,4,4,4],
           6:[5,4,5,4,5,4],7:[5,4,5,4,4,4],8:[5,4,5,4,5,4],9:[5,4,4,4,4,4],10:[5,4,5,4,5,4]},
}

# ---------------- TIER COMPLIANCE (BLIND) -------------
WB_N = {'core':[5,6,9,4,5,4,6,6,6,9],'th':[4,4,4,4,4,5,4,5,4,4],'ch':[3]*10}
WB_PARTIAL = {  # (lesson, item): reason
 'core':{(2,'Q5'):'magic triangle needs the corner insight; 720 arrangements by trial',
         (5,'Q1c'):'two-step undo in Core; guess-and-check only',(5,'Q2b'):'rule + inverse for OUT 30 needs the taught method',
         (6,'Q3a'):'fewest coins for 85c needs the greedy strategy',(9,'Q3'):'unit-size/count inverse is the lesson idea itself',
         (9,'Q4'):'unit conversion both ways, text only, no picture',(10,'Q7'):'two-step backwards in Core'},
 'th':{(1,'T1'):'same as Core Q2 with gaps',(2,'T1'):'repeat of Core Q4a',(2,'T3'):'repeat of Core Q3',
       (9,'T1'):'same as Core Q6b',(6,'T5'):'dollars only taught on an optional slide'},
 'ch':{(2,'C1'):'same task as Core Q5, new total',(9,'C2'):'one idea (take away the extra, share), as in L2'}}
QB_N = {'core':74,'th':102,'ch':57}
QB_PARTIAL = {'core':['L6 #7','L6 #8'],
  'th':['L1 #8','L1 #9','L2 #1','L2 #2','L2 #3','L2 #8','L2 #9','L2 #10','L2 #11','L2 #12','L3 #8','L5 #8','L5 #9','L5 #10','L6 #8','L9 #10','L10 #9'],
  'ch':['L3 #1','L9 #2','L2 #5']}
def mean(x): return sum(x)/len(x)
if __name__=='__main__':
    print('A now totals',{n:sum(v) for n,v in A_NOW.items()}, 'mean',mean([sum(v) for v in A_NOW.values()]))
    for p,d in B_NOW.items():
        print(p,{n:round(mean(v),2) for n,v in d.items()},'mean',round(mean([mean(v) for v in d.values()]),2))
