"""P6 close-gaps slides: Warm-up check (after the title) and What was hard? (after the exit ticket).
Called at the end of each gen_p6lK.py: p6_gaps.apply(K). Reads p6/content/gaps.json."""
import json,os,re,math
import slidekit
from slidekit import *
H=os.path.dirname(os.path.abspath(__file__))
G=json.load(open(os.path.join(H,'..','p6','content','gaps.json'),encoding='utf8'))

def short(a,limit=215):
    parts=re.split(r'(?<=[.?!])\s+',a); out=parts[0]
    for x in parts[1:]:
        if len(out)+1+len(x)>limit: break
        out+=' '+x
    return out

def check_slide(L,g):
    body=h2('Warm-up check')+f'<p style="font-size:30px;font-weight:700;color:{MUTED}">Two new puzzles. Whiteboard: your answer AND one reason. Hold up together.</p>'
    top=300
    for i,(q,a) in enumerate(g['check']):
        qs=f'Q{i+1}.  {q}'
        a=short(a)
        ql=math.ceil(len(qs)/80); qh=ql*50+40
        al=math.ceil(len(a)/92); ah=al*42+34
        body+=pin(128,top,1664,f'<p style="font-size:38px;font-weight:700;line-height:1.3"><span style="color:{TEAL};font-weight:800">Q{i+1}.</span>  {E(q)}</p>',None,WHITE,20,'18px 28px','box-sizing:border-box')
        body+=pin(128,top+qh+8,1664,f'<p style="font-size:32px;font-weight:800;line-height:1.25">{E(a)}</p>','pop',YEL,20,'16px 26px','box-sizing:border-box')
        top+=qh+8+ah+22
    assert top-22<=915,(L,top)
    notes=("Minutes 2 to 5 (3 minutes, taken out of the 10-minute warm-up: play the game for about 3 minutes and ask only the first three quick questions afterwards). "
      "Read the two puzzles aloud. Everyone writes the answer AND one reason on a whiteboard (online: in the chat or on a board held to the camera). Hold up together, then read every board before you say who is right. Click to reveal each answer. "
      "Answers: "+' '.join(f'Q{i+1}: {a}' for i,(q,a) in enumerate(g['check']))+" "
      "Fast track (nobody is labelled): a child with BOTH answers right and a reason that makes sense gets a private chat message, \"Today start on the Think Harder page at minute 40.\" They still join Explore, the mini-lesson and Talk time; only the worksheet time changes. Say to everyone: some of you will start on a different page today, it changes every lesson, and you can move any time. Never say advanced or top group. Do not record this as a mark.")
    return sec(f'{L}-check','3 MIN CHECK',body,notes)

def reflect_slide(L,g):
    body=h2('What was hard?')+f'<p style="font-size:32px;font-weight:700;color:{MUTED}">One minute, just for you. Nobody marks this.</p>'
    for i,a in enumerate(['The hardest part was ...','I got unstuck by ...','Next time I will try ...']):
        body+=pin(128,310+i*145,1664,f'<p style="font-size:52px;font-weight:800;line-height:1.2;color:{TEAL}">{E(a)}</p>',None,WHITE,20,'22px 34px','box-sizing:border-box')
    body+=pin(128,770,1664,f'<p style="font-size:32px;font-weight:600;line-height:1.3;color:{MUTED}">Write it in the box on the last page of today’s lesson. Then share ONE sentence if you like.</p>',None)
    notes=("About 1 minute, at minute 88, while you collect the exit tickets. Everyone finishes the three sentences in the \"What was hard?\" box on the last page of today's lesson. "
      "Share one: ask two or three children for one sentence each; \"pass\" is fine. Never grade or correct it. Praise the strategy, not the speed: say \"you "+g['reflectEx']+", and that is what got you unstuck\", never \"you were quick\". "
      "If a child writes that nothing was hard, ask what would make it harder.")
    return sec(f'{L}-reflect','1 MIN',body,notes)

def apply(n):
    L=f'p6l{n}'; D=os.path.join(H,'..','split',L,'project'); g=G[str(n)]
    open(os.path.join(D,'slides',f'{L}-check.html'),'w').write(check_slide(L,g))
    open(os.path.join(D,'slides',f'{L}-reflect.html'),'w').write(reflect_slide(L,g))
    dj=os.path.join(D,'deck.json'); d=json.load(open(dj,encoding='utf8')); o=[x for x in d['order'] if x not in (f'{L}-check',f'{L}-reflect')]
    o.insert(o.index(f'{L}-title')+1,f'{L}-check'); o.insert(o.index(f'{L}-exit')+1,f'{L}-reflect'); d['order']=o
    json.dump(d,open(dj,'w'),indent=1,ensure_ascii=False)
    print(len(o),'slides (with gaps slides)')
