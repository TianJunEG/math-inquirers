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
QB_N = {'core':74,'th':102,'ch':58}
QB_PARTIAL = {'core':['L6 #7','L6 #8'],
  'th':['L1 #8','L1 #9','L2 #1','L2 #2','L2 #3','L2 #8','L2 #9','L2 #10','L2 #11','L2 #12','L3 #8','L5 #8','L5 #9','L5 #10','L6 #8','L9 #10','L10 #9'],
  'ch':['L3 #1','L9 #2','L2 #5']}
def mean(x): return sum(x)/len(x)
if __name__=='__main__':
    print('A now totals',{n:sum(v) for n,v in A_NOW.items()}, 'mean',mean([sum(v) for v in A_NOW.values()]))
    for p,d in B_NOW.items():
        print(p,{n:round(mean(v),2) for n,v in d.items()},'mean',round(mean([mean(v) for v in d.values()]),2))

# =====================  DIAGNOSTIC SIMULATION  =====================
def pb(ps):
    """Poisson-binomial distribution of the number correct."""
    d=[1.0]
    for p in ps:
        nd=[0.0]*(len(d)+1)
        for k,v in enumerate(d):
            nd[k]+=v*(1-p); nd[k+1]+=v*p
        d=nd
    return d
def conv(a,b):
    r=[0.0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): r[i+j]+=x*y
    return r
# per-question success probabilities. 'BASE' = the assumptions printed in journey_p1.md (kept so results are like-for-like)
PROF_BASE = {
 'Strong-for-age':  ([.95,.97,.90,.80,.90,.90],[.50,.35]),
 'Typical-for-age': ([.85,.85,.65,.50,.60,.70],[.12,.06]),
 'Weak-for-age':    ([.45,.50,.15,.10,.20,.40],[.02,.01]),
 'Younger, strong': ([.90,.90,.35,.55,.65,.80],[.20,.08]),
 'Older, weak':     ([.70,.70,.50,.35,.45,.55],[.06,.03]),
 'Guesser/rusher':  ([.65,.65,.40,.25,.30,.50],[.05,.03]),
}
# 'MINE' = my own blind assumptions, written before opening the old audit; Q8 is now a 3-row dot graph (easier than the old 17-word sentence)
PROF_MINE = {
 'Strong-for-age':  ([.97,.95,.90,.92,.90,.95],[.70,.50]),
 'Typical-for-age': ([.90,.85,.75,.80,.80,.85],[.30,.15]),
 'Weak-for-age':    ([.60,.40,.25,.40,.35,.55],[.05,.02]),
 'Younger, strong': ([.85,.80,.40,.60,.50,.80],[.20,.10]),
 'Older, weak':     ([.90,.90,.70,.85,.80,.90],[.20,.10]),
 'Guesser/rusher':  ([.60,.55,.45,.50,.45,.60],[.10,.05]),
}
def current_rule(main,stretch):
    """build_diag.py as printed: main 4-6 join (+ 'try Level 2 check' if >=1 stretch), 2-3 chat+taster 'with a little support', 0-1 chat+taster. Warm-up is not used (Level 1 has no level below)."""
    return 'join' if main>=4 else ('support' if main>=2 else 'taster')
def old_rule_8(total):   # the pre-fix 8-mark rule in the old audit: 6-8 join, 4-5 join+expect support, 0-3 taster+chat
    return 'join' if total>=6 else ('support' if total>=4 else 'taster')
def run(profs):
    out={}
    for name,(m,s) in profs.items():
        dm=pb(m); ds=pb(s)
        res={'join':0,'join+tryL2':0,'support':0,'taster':0}
        for k,pk in enumerate(dm):
            r=current_rule(k,0)
            if r=='join':
                p_s1=1-ds[0]; res['join+tryL2']+=pk*p_s1; res['join']+=pk*ds[0]
            else: res[r]+=pk
        tot=conv(dm,ds); old={'join':0,'support':0,'taster':0}
        for k,pk in enumerate(tot): old[old_rule_8(k)]+=pk
        out[name]=(sum(i*p for i,p in enumerate(dm)),res,old)
    return out
def band_probs(p, n=6):
    d=pb([p]*n); return sum(d[4:]), d[2]+d[3], d[0]+d[1]
if __name__=='__main__':
    for lab,pr in (('BASE (old audit assumptions)',PROF_BASE),('MINE (blind assumptions)',PROF_MINE)):
        print('\n',lab)
        for n,(em,res,old) in run(pr).items():
            print(f'{n:16s} E[main]={em:.2f} NOW join {res["join"]*100:4.0f}% +tryL2 {res["join+tryL2"]*100:3.0f}% support {res["support"]*100:3.0f}% taster {res["taster"]*100:3.0f}% | OLD 8-mark rule join {old["join"]*100:3.0f}% support {old["support"]*100:3.0f}% taster {old["taster"]*100:3.0f}%')
    print('\nuniform p per main question (6 items): P(4-6) / P(2-3) / P(0-1)')
    for p in (.95,.9,.8,.7,.6,.5):
        a,b,c=band_probs(p); print(p, round(a*100),round(b*100),round(c*100))
    guess=[.1,.1,.05,.1,.1,1/3]
    print('pure guessing, P(main>=4)=',round(sum(pb(guess)[4:])*100,3),'%  (guessing 4+ of 6)')
    # Q12 uniqueness and Q11
    sols=[(a,5-a) for a in range(6) if 10*a+5*(5-a)==40]; print('Q12 solutions',sols)
    print('Q7 40+30=',40+30,' Q9 12-8=',12-8,' Q8 5-2=',5-2)

# =====================  PART 2: BASELINES (copied from the earlier audits AFTER the blind scores above were fixed) =====================
A_BEFORE = {1: [2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2], 2: [2, 1, 2, 2, 1, 1, 1, 1, 0, 1, 1, 2], 3: [1, 1, 1, 2, 1, 1, 1, 2, 1, 0, 1, 1], 4: [1, 1, 2, 1, 1, 1, 1, 1, 0, 0, 1, 2], 5: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 6: [2, 1, 1, 2, 1, 1, 1, 1, 0, 0, 1, 2], 7: [2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2], 8: [1, 1, 1, 2, 1, 1, 1, 1, 1, 0, 1, 2], 9: [1, 1, 1, 2, 1, 1, 1, 1, 0, 0, 1, 1], 10: [1, 1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1]}   # docs/audit/gifted_p1.md, per-criterion scores before the tier rework
A_CLAIMED_AFTER = {1:17,2:17,3:16,4:15,5:15,6:15,7:17,8:16,9:14,10:16}   # same file, 'Rubric (after rework)' column (totals only)
TIER_BEFORE = (227,309)   # gifted_p1.md: 227/309 compliant = 73%; after rework claimed 100% 'by construction' (gifted_fixes_p1.md)
B_BEFORE = {'LOW': {1: [4, 2, 3, 2, 3, 3], 2: [4, 2, 3, 3, 3, 3], 3: [5, 3, 5, 4, 4, 4], 4: [5, 3, 4, 3, 3, 3], 5: [4, 2, 3, 2, 3, 3], 6: [3, 1, 2, 1, 2, 2], 7: [4, 3, 4, 3, 3, 3], 8: [3, 2, 3, 2, 3, 3], 9: [4, 2, 4, 3, 3, 3], 10: [3, 2, 3, 3, 4, 2]}, 'MIDDLE': {1: [5, 3, 4, 3, 4, 4], 2: [5, 3, 4, 3, 3, 4], 3: [5, 4, 5, 4, 4, 4], 4: [5, 4, 4, 4, 4, 4], 5: [5, 3, 4, 3, 4, 4], 6: [4, 2, 3, 2, 3, 3], 7: [5, 3, 5, 4, 4, 4], 8: [4, 3, 4, 3, 4, 4], 9: [5, 3, 4, 3, 4, 4], 10: [4, 3, 4, 4, 4, 3]}, 'HIGH': {1: [5, 2, 4, 3, 3, 3], 2: [5, 2, 3, 4, 3, 3], 3: [5, 2, 4, 4, 3, 4], 4: [5, 2, 3, 3, 3, 3], 5: [5, 3, 4, 4, 4, 3], 6: [5, 3, 5, 4, 4, 4], 7: [5, 3, 5, 4, 4, 3], 8: [5, 3, 5, 4, 4, 4], 9: [5, 3, 4, 4, 4, 3], 10: [5, 3, 5, 4, 5, 4]}}   # docs/audit/journey_p1.md per-lesson [P,D,F,C,M,S]
B_BEFORE_DIM = {'LOW':[3.9,2.2,3.4,2.6,3.1,2.9],'MIDDLE':[4.7,3.1,4.1,3.3,3.8,3.8],'HIGH':[5.0,2.6,4.2,3.8,3.7,3.4]}  # as printed in journey_p1.md

def report():
    print('\n=== A per lesson: before / claimed after / now (blind) ===')
    for n in range(1,11):
        b=A_BEFORE[n]; w=A_NOW[n]
        d=[w[i]-b[i] for i in range(12)]
        print(n,sum(b),A_CLAIMED_AFTER[n],sum(w),'delta',sum(w)-sum(b),' per-criterion delta',d)
    mb=mean([sum(v) for v in A_BEFORE.values()]); mc=mean(A_CLAIMED_AFTER.values()); mn=mean([sum(v) for v in A_NOW.values()])
    print('level mean before %.1f claimed %.1f now %.1f'%(mb,mc,mn))
    print('criterion means before / now:')
    for i,c in enumerate(CRIT):
        print('  %-13s %.1f -> %.1f'%(c, mean([A_BEFORE[n][i] for n in A_BEFORE]), mean([A_NOW[n][i] for n in A_NOW])))
    # calibration: points I judge to be stricter/laxer scoring on evidence that did not change
    calib={'C7 inquiry (teacher-led 25-35 and 55-58 unchanged)':6,'C8 complexity (contexts unchanged)':4,'C2 depth (item counts unchanged)':3}
    print('calibration points',calib,'sum',sum(calib.values()),' -> adjusted mean %.1f'%(mn-sum(calib.values())/10))
    print('strict C10 (needs what-I-would-try-next): mean %.1f ; strict C10 + calibration %.1f'%(mn-1.0, mn-1.0-sum(calib.values())/10))
    print('\n=== B heatmap before -> now ===')
    for n in range(1,11):
        print(n,' '.join('%s %.2f -> %.2f (%+.2f)'%(p[0],mean(B_BEFORE[p][n]),mean(B_NOW[p][n]),mean(B_NOW[p][n])-mean(B_BEFORE[p][n])) for p in ('LOW','MIDDLE','HIGH')))
    for p in ('LOW','MIDDLE','HIGH'):
        bm=mean([mean(v) for v in B_BEFORE[p].values()]); nm=mean([mean(v) for v in B_NOW[p].values()])
        dn=[mean([B_NOW[p][n][i] for n in range(1,11)]) for i in range(6)]
        db=[mean([B_BEFORE[p][n][i] for n in range(1,11)]) for i in range(6)]
        print(p,'mean %.2f -> %.2f'%(bm,nm),'dims before',[round(x,1) for x in db],'now',[round(x,1) for x in dn])
    cnt_b=sum(1 for p in B_BEFORE for n in B_BEFORE[p] if mean(B_BEFORE[p][n])<3); cnt_n=sum(1 for p in B_NOW for n in B_NOW[p] if mean(B_NOW[p][n])<3)
    print('cells below 3.0: before',cnt_b,'now',cnt_n, ' cells <3.5 now', sum(1 for p in B_NOW for n in B_NOW[p] if mean(B_NOW[p][n])<3.5))
    wb=sum(sum(v) for v in WB_N.values()); wp=sum(len(v) for v in WB_PARTIAL.values()); qb=sum(QB_N.values()); qp=sum(len(v) for v in QB_PARTIAL.values())
    # unique-item count: workbook Think harder/Go further items ARE bank items (stretch[0:4], challenge[-3:]), so count workbook CORE (60) + bank (233) + 1 workbook-only item (L6 T5 dollars)
    uniq=WB_N['core'][:]; ucore=sum(uniq)
    n_items=ucore+sum(QB_N.values())+1
    n_part=len(WB_PARTIAL['core'])+sum(len(v) for v in QB_PARTIAL.values())+3+1   # +3 workbook TH/C partials that map to bank items not already listed (L1 T1, L9 T1, L9 C2), +1 L6 T5
    print('UNIQUE-ITEM tier compliance now: %d/%d = %.0f%% strict, %.0f%% if partial counts half'%(n_items-n_part,n_items,100*(1-n_part/n_items),100*(1-n_part/2/n_items)))
    print('\ntier: before %d/%d = %.0f%% ; claimed 100%% ; now workbook %d/%d = %.0f%%, bank %d/%d = %.0f%%, combined %d/%d = %.0f%% strict, %.0f%% if partial counts half'%(TIER_BEFORE[0],TIER_BEFORE[1],100*TIER_BEFORE[0]/TIER_BEFORE[1],wb-wp,wb,100*(1-wp/wb),qb-qp,qb,100*(1-qp/qb),wb+qb-wp-qp,wb+qb,100*(1-(wp+qp)/(wb+qb)),100*(1-(wp+qp)/2/(wb+qb))))
if __name__=='__main__':
    report()
