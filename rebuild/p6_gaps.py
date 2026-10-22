"""P6 slides added to every lesson: Sneak-peek puzzles (after the title), Go further (explore stage) and Looking back (after the exit slip).
Also a neutral-wording clean-up over every slide of the lesson. Called at the end of each gen_p6lK.py: p6_gaps.apply(K). Reads p6/content/gaps.json."""
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

def sneak_slide(L,g):
    body=h2('Sneak-peek puzzles')+f'<p style="font-size:28px;font-weight:700;color:{MUTED};line-height:1.3">Two ideas we have not learnt yet. Guessing is welcome. “I do not know” is welcome. Nobody is marked. Show your answer only to your tutor: own paper held up to them, or a private chat message.</p>'
    top=300
    for i,(q,a) in enumerate(g['sneak']):
        lab='Puzzle 1: try it with objects, a drawing or counting' if i==0 else 'Puzzle 2: have a think'
        qh=math.ceil(len(q)/78)*48+36+34
        a=short(a,190)
        ah=math.ceil(len(a)/90)*40+30
        body+=pin(128,top,1664,f'<p style="font-size:26px;font-weight:800;color:{TEAL}">{E(lab)}</p><p style="font-size:34px;font-weight:700;line-height:1.3">{E(q)}</p>',None,WHITE,20,'14px 28px','box-sizing:border-box')
        body+=pin(128,top+qh+6,1664,f'<p style="font-size:30px;font-weight:800;line-height:1.25">{E(a)}</p>','pop',YEL,20,'12px 26px','box-sizing:border-box')
        top+=qh+6+ah+20
    assert top-20<=925,(L,top)
    notes=("Minutes 2 to 5 (3 minutes). These are ideas we have not learnt yet: say so, and say that guessing and \"I do not know\" are welcome and nobody is marked. Read the two puzzles aloud. Puzzle 1 is an access puzzle: any child can try it with objects, a drawing or counting, so everyone can get a first win. Puzzle 2 is a thinking puzzle on today's idea. "
      "Answers are shown PRIVATELY: own paper held up to you only, or a private chat message. Never boards held up for the group, never read wrong answers aloud. Click to reveal each answer at minute 5, then say: \"Both of these are what we learn today.\" "
      "Answers: "+' '.join(f'Puzzle {i+1}: {a}' for i,(q,a) in enumerate(g['sneak']))+" "
      "Quietly, and only by private chat message (never by name in front of the group), you may invite a child to try Think harder after the point printed on page 1. Any child can choose it and any child can go back. Never announce who is on which page and never say advanced or top group. Do not record this as a mark. Do not split a pair unless both children agree.")
    return sec(f'{L}-check','2–5 MIN',body,notes)

def go_slide(L,g):
    q,a=g['go']
    body=h2('Go further: a what-if')+f'<p style="font-size:30px;font-weight:700;color:{MUTED}">For any pair that has finished the explore task. Pick it up whenever you are ready. It is not extra homework.</p>'
    body+=pin(128,360,1664,f'<p style="font-size:26px;font-weight:800;color:{TEAL}">What if ...?</p><p style="font-size:42px;font-weight:700;line-height:1.3">{E(q)}</p>',None,WHITE,24,'24px 34px','box-sizing:border-box')
    body+=pin(128,740,1664,f'<p style="font-size:34px;font-weight:800;line-height:1.25">{E(short(a,230))}</p>','pop',YEL,20,'16px 26px','box-sizing:border-box')
    notes=("Minutes 12 to 25. Show this slide beside the explore instructions (or put it in the chat) from minute 12. Any pair that finishes the explore task can try this second what-if question, so nobody waits. Do not say who is ready for it. Take it up in the Explore discussion only if a pair wants to share. Answer: "+a)
    return sec(f'{L}-go','12–25 MIN',body,notes)

def reflect_slide(L,g):
    body=h2('Looking back')+f'<p style="font-size:32px;font-weight:700;color:{MUTED}">About 2 minutes, just for you. Nobody marks this. You can write “pass”.</p>'
    for i,a in enumerate(['Something I did well ...','The hardest part was ...']):
        body+=pin(128,280+i*120,1664,f'<p style="font-size:48px;font-weight:800;line-height:1.2;color:{TEAL}">{E(a)}</p>',None,WHITE,20,'20px 34px','box-sizing:border-box')
    body+=pin(128,530,1664,f'<p style="font-size:36px;font-weight:800;color:{TEAL}">What helped me (tick):</p><p style="font-size:34px;font-weight:600;line-height:1.35">I drew or built it   •   I tried a smaller example   •   I checked my answer   •   I asked for help</p><p style="font-size:34px;font-weight:600;line-height:1.35">I am still stuck (my tutor will check in privately)   •   pass</p>',None,WHITE,20,'20px 34px','box-sizing:border-box')
    body+=pin(128,820,1664,f'<p style="font-size:28px;font-weight:600;line-height:1.3;color:{MUTED}">Write it in the “Looking back” box on your Finish page. Nobody has to share it.</p>',None)
    notes=("Minutes 86 to 88 (2 minutes), after the exit slip. Everyone has the box: it is on the Finish page, a page every child reaches. Say: \"Two minutes, just for you. Finish: something I did well, the hardest part was, and tick what helped. You can write pass. If you are still stuck, tick that box and I will check in with you privately.\" "
      "Never collect it in front of the group and never read an answer out. You may read a child's box privately afterwards and reply by private chat message. Praise the strategy, not the speed: say \"you "+g['reflectEx']+", and that is what got you unstuck\", never \"you were quick\". "
      "If a child ticks I am still stuck, check in privately that day. If a child writes \"everything\" or \"I am bad at maths\", say privately: \"Thank you for telling me. Let's find one small thing that worked today,\" and point to a specific item they got right. If a child writes that nothing was hard, ask what would make it harder.")
    return sec(f'{L}-reflect','86–88 MIN',body,notes)

# ---- neutral wording over every slide of the lesson ----
SUBS=[
 ('For early finishers','40–72 MIN'),
 (r'>Stretch</h2>','>Think harder</h2>'),
 (r'>Challenge: see it</h2>','>Go further: see it</h2>'),
 (r'>Challenge: walk-through</h2>','>Go further: walk-through</h2>'),
 (r'>Challenge</h2>','>Go further</h2>'),
 (r'Finished early\? Stretch and Challenge come next\.','Finished? Your choice: Think harder, Go further or the Investigation on your Finish page.'),
 (r'Finished early\? ','Finished? Your choice: '),
 (r'Stretch and Challenge','Think harder or Go further'),
 (r'Finished early:','If a pair wants more:'),
 (r'Early finishers:','Anyone who wants more:'),
 (r'early finishers','anyone who wants more'),
 (r'Early finishers','Anyone who wants more'),
 (r'Think Harder','Think harder'),
 (r'Whiteboards up together, then click to reveal\.','Thumbs or a whisper to a partner, then click to reveal.'),
 (r'Write your answers on paper\. Show your tutor, then collect your stamp\.','Write on your exit slip (Finish page). Show only your tutor.'),
]
def clean(L,D):
    sl=os.path.join(D,'slides')
    for f in os.listdir(sl):
        if not f.endswith('.html'): continue
        pth=os.path.join(sl,f); s=open(pth).read(); o=s
        sid=f[:-5]
        if sid.endswith(('-challenge','-chdiag','-chwalk')):
            s=re.sub(r'(letter-spacing:2px;[^>]*>)\s*Challenge\s*(</p>)',r'\g<1>40–72 MIN\2',s) if '40–72' not in s else s
        for a,b in SUBS:
            s=re.sub(a,b,s) if a.startswith(('>','Finished','Early','early','Stretch','Think','Write')) else s.replace(a,b)
        if sid.endswith('-warm1') and not L.endswith('l10'):
            s=s.replace('0–5 MIN','5–8 MIN').replace('Minutes 0 to 5','Minutes 5 to 8')
        if sid.endswith('-warm2') and not L.endswith('l10'):
            s=s.replace('5–10 MIN','8–10 MIN').replace('Minutes 5 to 10','Minutes 8 to 10')
        if sid.endswith('-exit'):
            s=s.replace('82–90 MIN','82–86 MIN').replace('Minutes 82 to 90.','Minutes 82 to 86.')
        if s!=o: open(pth,'w').write(s)

def apply(n):
    L=f'p6l{n}'; D=os.path.join(H,'..','split',L,'project'); g=G[str(n)]
    open(os.path.join(D,'slides',f'{L}-check.html'),'w').write(sneak_slide(L,g))
    open(os.path.join(D,'slides',f'{L}-go.html'),'w').write(go_slide(L,g))
    open(os.path.join(D,'slides',f'{L}-reflect.html'),'w').write(reflect_slide(L,g))
    clean(L,D)
    dj=os.path.join(D,'deck.json'); d=json.load(open(dj,encoding='utf8')); o=[x for x in d['order'] if x not in (f'{L}-check',f'{L}-reflect',f'{L}-go')]
    o.insert(o.index(f'{L}-title')+1,f'{L}-check'); o.insert(o.index(f'{L}-explore1')+1,f'{L}-go'); o.insert(o.index(f'{L}-exit')+1,f'{L}-reflect'); d['order']=o
    json.dump(d,open(dj,'w'),indent=1,ensure_ascii=False)
    print(len(o),'slides (with gaps slides)')
