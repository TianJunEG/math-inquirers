"""Close-the-gaps slides for Math Inquirers P2: a 3-minute Warm-up check and a 1-minute 'What was hard?' reflection.
Content comes from p2/gaps.json (shared with the workbook and the tutor guide).  Usage in a gen_p2lK.py:
    import p2gaps; p2gaps.add(S, K)            # before the slides are written; adds 2 slides and re-times the warm-up / exit
    order = p2gaps.order(order, K)             # after the order list exists
"""
import json,os,re
import slidekit
from slidekit import *
G=json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','p2','gaps.json')))
def _face(x,y,kind,r=62):
    mouth={'happy':f'M{x-30} {y+14} Q{x} {y+48} {x+30} {y+14}','ok':f'M{x-28} {y+26} H{x+28}','hard':f'M{x-30} {y+36} Q{x} {y+4} {x+30} {y+36}'}[kind]
    return (f'<circle cx="{x}" cy="{y}" r="{r}" fill="{YEL}" stroke="{NAVY}" stroke-width="5"/><circle cx="{x-22}" cy="{y-16}" r="7" fill="{NAVY}"/><circle cx="{x+22}" cy="{y-16}" r="7" fill="{NAVY}"/>'
            f'<path d="{mouth}" fill="none" stroke="{NAVY}" stroke-width="6" stroke-linecap="round"/>')
def precheck(K):
    g=G[str(K)]['pre']; C=G['common']
    body=h2('Warm-up check')+p('Two questions, 3 minutes. Whiteboards up together, then tell your partner HOW you know.',34,600,MUTED)
    for i,x in enumerate(g):
        t=320+i*230
        body+=qrow(128,t,1250,'Q%d'%(i+1),x['q'],34)+answer(1420,t,372,x['short'])
    notes=('Minutes 1 to 4. Warm-up check: two questions on the key idea of today, in a NEW setting (not recall). Give about 1 minute each. Whiteboards up together, ask one child "How do you know?", then click to show each answer. '
      f'Q1 answer: {g[0]["a"]} Listen for: {g[0]["w"]} '
      f'Q2 answer: {g[1]["a"]} Listen for: {g[1]["w"]} '
      'FAST TRACK: a child who gets BOTH right AND can say why starts on the THINK HARDER pages and the Open investigation (workbook Q8) when the worksheet begins at minute 36, in their own breakout room or with you checking in. A right answer without a reason stays with the group. If unsure, keep the child in the group. '
      'Nobody is labelled: say "Some of you will start on a different page today; everyone gets a turn at both." Children can move at any time. Everyone joins explore, the mini-lesson, the check-together slides and talk time.')
    return sec(f'p2l{K}-precheck','1–4 MIN',body,notes)
def reflect(K):
    g=G[str(K)]; C=G['common']
    f=''.join(_face(110+i*300,90,k)+f'<text x="{110+i*300}" y="205" font-size="34" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="Nunito Sans, Arial">{t}</text>' for i,(k,t) in enumerate([('happy','easy'),('ok','OK'),('hard','tricky')]))
    svg=f'<svg aria-label="Three faces: easy, OK, tricky" viewBox="0 0 900 220" xmlns="http://www.w3.org/2000/svg" style="width:900px;height:220px;flex:none">{f}</svg>'
    body=h2('What was hard?')+pin(128,250,1664,f'<div style="display:flex;align-items:center;gap:40px">{svg}<p style="font-size:36px;font-weight:700;line-height:1.3">Tick the face that shows how this lesson felt.</p></div>',None,WHITE,24,'16px 32px')
    body+=qrow(128,520,1664,'1.','The hardest part was …',40)
    body+=qrow(128,640,1664,'2.','I got unstuck by …   ('+',  '.join(g['unstuck'])+')',36)
    body+=qrow(128,760,1664,'3.','Next time I will try …',40)
    notes=('Minutes 88 to 90. What was hard? About 1 minute: children tick a face and finish the three sentences on the last workbook page. No marks and no wrong answers. '
      'Tutor script: SAY: '+C['refSay']+' DO: '+C['refDo'])
    return sec(f'p2l{K}-reflect','88–90 MIN',body,notes)
def add(S,K):
    P=f'p2l{K}'
    S[f'{P}-precheck']=precheck(K); S[f'{P}-reflect']=reflect(K)
    r=lambda k,a,b: S.__setitem__(k,S[k].replace(a,b))
    r(f'{P}-warm1','0–5 MIN','4–6 MIN'); r(f'{P}-warm1','Minutes 0 to 5.','Minutes 4 to 6 (shortened to two minutes because of the Warm-up check: one or two rounds).')
    r(f'{P}-warm2','5–8 MIN','6–8 MIN'); r(f'{P}-warm2','Minutes 5 to 8.','Minutes 6 to 8 (if short of time, ask only questions 1, 3 and 5).')
    s=S[f'{P}-title']
    s=re.sub(r'warm-up 0 to 8','Warm-up check 1 to 4 (fast-track decision), warm-up 4 to 8',s)
    s=s.replace('exit ticket 80 to 90','exit ticket 80 to 88, What was hard? 88 to 90')
    S[f'{P}-title']=s
    e=S[f'{P}-exit']; e=e.replace('80–90 MIN','80–88 MIN').replace('Minutes 80 to 90.','Minutes 80 to 88.'); S[f'{P}-exit']=e
def order(o,K):
    P=f'p2l{K}'; out=[]
    for i in o:
        out.append(i)
        if i==f'{P}-title': out.append(f'{P}-precheck')
        if i==f'{P}-exit': out.append(f'{P}-reflect')
    return out
