"""P6 slides added to every lesson: Sneak-peek puzzles (after the title), Go further (explore stage) and Looking back (after the exit slip).
Also a neutral-wording clean-up over every slide of the lesson. Called at the end of each gen_p6lK.py: p6_gaps.apply(K). Reads p6/content/gaps.json."""
import json,os,re,math
import p6_budget as BUDG
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
    body=h2('Sneak-peek puzzles')+f'<p style="font-size:26px;font-weight:700;color:{MUTED};line-height:1.3">Two ideas we have not learnt yet. Guessing is welcome. “I do not know” is welcome. Nobody is marked. When your tutor says show, everyone holds their paper to the camera at the same moment.</p>'
    top=330
    for i,(q,a) in enumerate(g['sneak']):
        lab='Puzzle 1: try it with objects, a drawing or counting' if i==0 else 'Puzzle 2: have a think'
        qh=math.ceil(len(q)/84)*44+30+30
        a=short(a,150)
        ah=math.ceil(len(a)/96)*38+28
        body+=pin(128,top,1664,f'<p style="font-size:26px;font-weight:800;color:{TEAL}">{E(lab)}</p><p style="font-size:32px;font-weight:700;line-height:1.3">{E(q)}</p>',None,WHITE,20,'12px 28px','box-sizing:border-box')
        body+=pin(128,top+qh+6,1664,f'<p style="font-size:28px;font-weight:800;line-height:1.25">{E(a)}</p>','pop',YEL,20,'10px 26px','box-sizing:border-box')
        top+=qh+6+ah+14
    assert top-14<=925,(L,top)
    a,b=BUDG.BUD[int(L[3:])]['slides']['check']
    notes=(f"Minutes {BUDG.fmt(a)} to {BUDG.fmt(b)} ({BUDG.fmt(b-a)} minutes). These are ideas we have not learnt yet: say so, and say that guessing and \"I do not know\" are welcome and nobody is marked. Read the two puzzles aloud. Puzzle 1 is an access puzzle: any child can try it with objects, a drawing or counting, so everyone can get a first win. Puzzle 2 is a thinking puzzle on today's idea. "
      "ONE show moment only: after both puzzles, everyone holds their paper to the camera at the same moment (or shows it to you only on camera). Never private chat. Never compare answers across children, never read wrong answers aloud. Then click to reveal the answers one after the other and move on with no reaction round: say each answer in 15 words or fewer, then say: \"Both of these are what we learn today.\" "
      "Answers: "+' '.join(f'Puzzle {i+1}: {a}' for i,(q,a) in enumerate(g['sneak']))+" "
      "Invite the WHOLE group, never one child: say \"When you have finished Start here, you can choose Think harder, Go further or the Investigation.\" Nobody is singled out. Any child can choose it and any child can go back. Never announce who is on which page and never say advanced or top group. Do not record this as a mark. Do not split a pair unless both children agree.")
    return sec(f'{L}-check',BUDG.pill(int(L[3:]),'check'),body,notes)

def go_note(g):
    """The Go further what-if is no longer a slide in the group flow (re-budget): the tutor pastes it in the chat for a pair that finishes the explore task."""
    q,a=g['go']
    return ' Go further what-if (not a slide: paste it in the chat for any pair that finishes early, and take it up only if a pair wants to share): '+q+' Answer: '+a

def reflect_slide(L,g):
    body=h2('Looking back')+f'<p style="font-size:32px;font-weight:700;color:{MUTED}">About 2 minutes, just for you. Nobody marks this. You can write “pass”.</p>'
    for i,a in enumerate(['Something I did well ...','The hardest part was ...']):
        body+=pin(128,280+i*120,1664,f'<p style="font-size:48px;font-weight:800;line-height:1.2;color:{TEAL}">{E(a)}</p>',None,WHITE,20,'20px 34px','box-sizing:border-box')
    body+=pin(128,530,1664,f'<p style="font-size:36px;font-weight:800;color:{TEAL}">What helped me (tick):</p><p style="font-size:34px;font-weight:600;line-height:1.35">I drew or built it   •   I tried a smaller example   •   I checked my answer   •   I asked for help</p><p style="font-size:34px;font-weight:600;line-height:1.35">I am still stuck (my tutor will check in during the lesson)   •   pass</p>',None,WHITE,20,'20px 34px','box-sizing:border-box')
    body+=pin(128,820,1664,f'<p style="font-size:28px;font-weight:600;line-height:1.3;color:{MUTED}">Write it in the “Looking back” box on your Finish page. Nobody has to share it.</p>',None)
    notes=("Minutes 86 to 88 (2 minutes), after the exit slip, and never shortened. Everyone has the box: it is on the Finish page, a page every child reaches. Say: \"Two minutes, just for you. Finish: something I did well, the hardest part was, and tick what helped. You can write pass. If you are still stuck, tick that box and I will check in with you in the open session, in the shared room, with your parent nearby.\" "
      "Never collect it in front of the group and never read an answer out. You may look at a child's box on camera in the open session if the child offers it. Praise the strategy, not the speed: say \"you "+g['reflectEx']+", and that is what got you unstuck\", never \"you were quick\". "
      "If a child ticks I am still stuck, check in during the open session the same day: visit the shared breakout room or use a hand signal, with a parent nearby. Never by private message. If a child writes \"everything\" or \"I am bad at maths\", say quietly in the open session: \"Thank you for telling me. Let's find one small thing that worked today,\" and point to a specific item they got right. If a child writes that nothing was hard, ask what would make it harder.")
    return sec(f'{L}-reflect',BUDG.pill(int(L[3:]),'reflect'),body,notes)

# ---- neutral wording over every slide of the lesson ----
SUBS=[
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
        if sid.endswith(('-challenge','-chdiag','-chwalk')): s=s.replace('62–75 MIN','40–72 MIN')
        if sid.endswith('-warm1') and not L.endswith('l10'):
            s=s.replace('0–5 MIN','5–8 MIN').replace('Minutes 0 to 5','Minutes 5 to 8')
        if sid.endswith('-warm2') and not L.endswith('l10'):
            s=s.replace('5–10 MIN','8–10 MIN').replace('Minutes 5 to 10','Minutes 8 to 10')
        if L=='p6l10': s=s.replace('40–72 MIN','35–60 MIN')
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
