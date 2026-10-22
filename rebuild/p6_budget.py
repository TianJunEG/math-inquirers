"""Level 6 re-budget: the ONE place where the minute plan of the ten P6 lessons lives (docs/audit/rebudget_p6.md explains it).

  BUD[n]['parts']   part budgets (title, start, end) in minutes on the lesson clock; each lesson sums to 90.
  BUD[n]['slides']  clock time of every slide in the group flow: {slide id without the 'p6lN-' prefix: (start, end)}
  BUD[n]['optional'] slides that carry no clock time ("Optional, if you finish early")
  Used by rebuild/p6_gaps.py (time pills and 'Minutes a to b' notes of every slide, run at the end of each gen_p6lK.py)
  and by p6/guide.js (reads p6/budget.json, written by `python3 rebuild/p6_budget.py`).
"""
import json,os
H=os.path.dirname(os.path.abspath(__file__))
OPT=['stretch','challenge','chdiag','chwalk']
FLEX='Flex (catch-up or Think harder; lose first)'

def fmt(x):
    return ('%g'%x)

def build(n,cuts,flex,slides,exit_slip=None):
    """cuts: list of (title,minutes) for Opening..Worksheet.. in order incl. 'Worksheet'; flex minutes; slides: list of (part_title,[(id,minutes)...])"""
    parts=[];t=0.0;sl={}
    for title,dur,*rest in cuts:
        parts.append((title,t,t+dur))
        if title in slides:
            s=t
            for sid,d in slides[title]:
                sl[sid]=(s,s+d);s+=d
            assert abs(s-(t+dur))<1e-9,(n,title,s,t+dur)
        t+=dur
    return parts,sl,t

def lesson(n,bud,flex,talk,exit_slip,slides):
    """bud: dict of Opening..Worksheet minutes (ordered list of (title,minutes)); returns the record"""
    parts=[];t=0.0;sl={}
    for title,dur in bud:
        parts.append((title,t,t+dur))
        if title in slides:
            s=t
            for sid,d in slides[title]:
                sl[sid]=(s,s+d);s+=d
            assert abs(s-(t+dur))<1e-9,(n,title,s,t+dur)
        t+=dur
    parts.append((FLEX,t,t+flex));t+=flex
    parts.append(('Talk time',t,t+talk));sl['talk']=(t,t+talk);t+=talk
    es=90-4-t   # exit slip runs to minute 86; looking back 86-88; close and stamp 88-90
    assert abs(es-exit_slip)<1e-9,(n,es,exit_slip)
    parts.append(('Exit slip',t,86.0));sl['exit']=(t,86.0)
    parts.append(('Looking back',86.0,88.0));sl['reflect']=(86.0,88.0)
    parts.append(('Close and stamp',88.0,90.0))
    return dict(parts=parts,slides=sl,optional=OPT)

BUD={}
std=lambda o,sn,w,e,m,b,ws:[('Opening',o),('Sneak-peek puzzles',sn),('Warm-up',w),('Explore',e),('Mini-lesson',m),('Brain break',b),('Worksheet',ws)]

BUD[1]=lesson(1,std(2,4,6.5,12.5,11,4.5,33.5),2.5,5,4.5,{
 'Sneak-peek puzzles':[('check',4)],'Warm-up':[('warm1',4),('warm2',2.5)],'Explore':[('explore1',4),('explore2',8.5)],
 'Mini-lesson':[('teach1',2),('we1',2),('try1',1),('we2',4),('key',2)],'Brain break':[('break',4.5)],
 'Worksheet':[('teachwhich',2.5),('trywhich',3),('ws1',12),('ws1ans',2.5),('teachtrace',2.5),('ws2',8),('ws2ans',3)]})
BUD[2]=lesson(2,std(2,4.5,6,14,8.5,5,35.5),1.5,5,4,{
 'Sneak-peek puzzles':[('check',4.5)],'Warm-up':[('warm1',3.5),('warm2',2.5)],'Explore':[('explore1',4.5),('explore2',9.5)],
 'Mini-lesson':[('teach1',1.5),('we1',2),('we2',1.5),('we3',2.5),('key',1)],'Brain break':[('break',5)],
 'Worksheet':[('ws1',11),('ws1ans',3),('teachtrace',3),('teachgold',2),('ws2',13.5),('ws2ans',3)]})
BUD[3]=lesson(3,std(2,3.5,6,15,10,5,33),3,6,2.5,{
 'Sneak-peek puzzles':[('check',3.5)],'Warm-up':[('warm1',3.5),('warm2',2.5)],'Explore':[('explore1',4.5),('explore2',10.5)],
 'Mini-lesson':[('teach1',2),('we1',2),('try1',1),('teach2',1),('we2',2),('try2',1),('key',1)],'Brain break':[('break',5)],
 'Worksheet':[('ws1',13),('ws1ans',3),('teachtrace',3),('ws2',10),('ws2ans',4)]})
BUD[4]=lesson(4,std(2,4,6.5,14,8,5.5,34.5),3.5,5,3,{
 'Sneak-peek puzzles':[('check',4)],'Warm-up':[('warm1',4),('warm2',2.5)],'Explore':[('explore1',5.5),('explore2',8.5)],
 'Mini-lesson':[('teach1',1.5),('we1',1.5),('teach2',1),('we2',1.5),('try2',1.5),('key',1)],'Brain break':[('break',5.5)],
 'Worksheet':[('ws1',14),('ws1ans',3),('teachcode',3.5),('ws2',10),('ws2ans',4)]})
BUD[5]=lesson(5,std(2,4.5,6.5,13,9.5,5,34.5),3,5,3,{
 'Sneak-peek puzzles':[('check',4.5)],'Warm-up':[('warm1',4),('warm2',2.5)],'Explore':[('explore1',4.5),('explore2',8.5)],
 'Mini-lesson':[('teach1',2),('we1',2),('try1',1.5),('teachcode',3),('key',1)],'Brain break':[('break',5)],
 'Worksheet':[('teachcards',2),('ws1',13),('ws1ans',3),('teachhand',3),('ws2',10),('ws2ans',3.5)]})
BUD[6]=lesson(6,std(2,4.5,6,14.5,10.5,5,31.5),2.5,6,3.5,{
 'Sneak-peek puzzles':[('check',4.5)],'Warm-up':[('warm1',3.5),('warm2',2.5)],'Explore':[('explore1',4.5),('explore2',10)],
 'Mini-lesson':[('teach1',1.5),('we1',1.5),('try1',1),('teachtwo',2),('try2',1),('teachcode',2.5),('key',1)],'Brain break':[('break',5)],
 'Worksheet':[('teachbag',2),('ws1',10),('ws1ans',3),('teachfair',3),('ws2',11),('ws2ans',2.5)]})
BUD[7]=lesson(7,std(2,4.5,6.5,14.5,12.5,5.5,30),2.5,5,3,{
 'Sneak-peek puzzles':[('check',4.5)],'Warm-up':[('warm1',4),('warm2',2.5)],'Explore':[('explore1',5),('explore2',9.5)],
 'Mini-lesson':[('teach1',1.5),('we1',2),('try1',1.5),('we2',2),('try2',1.5),('we3',2.5),('key',1.5)],'Brain break':[('break',5.5)],
 'Worksheet':[('ws1',10),('ws1ans',3),('teachtrace',2.5),('teachstar',2.5),('ws2',9),('ws2ans',3)]})
BUD[8]=lesson(8,std(2,4,5.5,14.5,11,5,31),4,6,3,{
 'Sneak-peek puzzles':[('check',4)],'Warm-up':[('warm1',3),('warm2',2.5)],'Explore':[('explore1',5),('explore2',9.5)],
 'Mini-lesson':[('teach1',1.5),('we1',2),('we2',2),('try2',1.5),('we3',3),('key',1)],'Brain break':[('break',5)],
 'Worksheet':[('ws1',11),('ws1ans',3),('teachtrace',2.5),('teachcrack',2.5),('ws2',9),('ws2ans',3)]})
BUD[9]=lesson(9,std(2,4.5,5.5,14,11.5,5.5,32.5),1.5,5,4,{
 'Sneak-peek puzzles':[('check',4.5)],'Warm-up':[('warm1',3),('warm2',2.5)],'Explore':[('explore1',4.5),('explore2',9.5)],
 'Mini-lesson':[('teach1',1.5),('we1',2),('code1',3),('try1',1.5),('we2',2),('key',1.5)],'Brain break':[('break',5.5)],
 'Worksheet':[('teachmed',2),('ws1',15),('ws1ans',3),('teachany',2.5),('ws2',7),('ws2ans',3)]})

# ---- Lesson 10 has its own plan: no relay, no talk time, showcase 2:15 per child ----
def l10():
    parts=[('Opening',0,2),('Sneak-peek puzzles',2,6),('Challenge round (teams of 2) and check',6,19.5),('Starter projects (A-D)',19.5,26.5),
           ('Brain break',26.5,30),('Plan and build',30,58),(FLEX,58,60.5),('Showcase (8 children)',60.5,82.5),('Exit slip and talk question',82.5,86),
           ('Looking back',86,88),('Certificates and close',88,90)]
    sl={'check':(2,6),'warm1':(6,8),'explore1':(8,10),'ws1':(10,16.5),'ws1ans':(16.5,19.5),
        'teach1':(19.5,21),'we1':(21,23),'we2':(23,24.5),'we3':(24.5,26),'key':(26,26.5),
        'break':(26.5,30),'teachplan':(30,32),'teachtest':(32,33),'ws2':(33,58),'ws2ans':(58,58),   # placeholders replaced below
        'showcase':(60.5,82.5),'exit':(82.5,86),'reflect':(86,88),'end':(88,90)}
    return dict(parts=parts,slides=sl,optional=OPT)
BUD[10]=l10()

def check():
    for n,b in BUD.items():
        t=0
        for title,s,e in b['parts']:
            assert abs(s-t)<1e-9,(n,title,s,t); t=e
        assert abs(t-90)<1e-9,(n,t)

def pill(n,sid):
    a,b=BUD[n]['slides'][sid]
    return fmt(a)+'–'+fmt(b)+' MIN'

def part_of(n,sid):
    a,b=BUD[n]['slides'][sid]
    for title,s,e in BUD[n]['parts']:
        if s-1e-9<=a and b<=e+1e-9: return title,s,e

def write_json(path=None):
    check()
    out={'lessons':{str(n):{'parts':[{'title':t,'start':s,'end':e} for t,s,e in b['parts']],
                            'optional_slides':[f'p6l{n}-{x}' for x in b['optional']]} for n,b in BUD.items()}}
    path=path or os.path.join(H,'..','p6','budget.json')
    json.dump(out,open(path,'w'),indent=1,ensure_ascii=False)
    return out

if __name__=='__main__':
    write_json(); print('p6/budget.json written')
