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
    notes=("Looking back is 2 full minutes, after the exit slip, and is never shortened. Everyone has the box: it is on the Finish page, a page every child reaches. Say: \"Two minutes, just for you. Finish: something I did well, the hardest part was, and tick what helped. You can write pass. If you are still stuck, tick that box and I will check in with you in the open session, in the shared room, with your parent nearby.\" "
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
 (r'Write your answers on paper\. Show your tutor, then collect your stamp\.','Write on your exit slip (Finish page). When your tutor says show, hold it to the camera at the same moment.'),
]
def clean(L,D):
    sl=os.path.join(D,'slides')
    for f in os.listdir(sl):
        if not f.endswith('.html'): continue
        pth=os.path.join(sl,f); s=open(pth).read(); o=s
        for a,b in SUBS:
            s=re.sub(a,b,s) if a.startswith(('>','Finished','Early','early','Stretch','Think','Write')) else s.replace(a,b)
        if s!=o: open(pth,'w').write(s)

# ---- clock times: every pill, 'Minutes a to b' note and the title-slide time plan come from rebuild/p6_budget.py ----
OPTLABEL='Optional, if you finish early'
OPTNOTE=OPTLABEL+' (no clock time): show it only while some children are working, never as a group slide at a fixed minute. '
PILLRE=re.compile(r'(<p style="position:absolute;right:128px;top:64px;[^"]*">)([^<]*)(</p>)')
BREAKRE=re.compile(r'(letter-spacing:4px;[^>]*>)[^<]*MIN(</p>)')
LEAD=re.compile(r'^Minutes [\d.]+ to [\d.]+(?: \([^)]*\))?\.?\s*')
def _part(n,title):
    for t,s,e in BUDG.BUD[n]['parts']:
        if t.startswith(title): return s,e
def _plan(n):
    f=BUDG.fmt; P=lambda t:_part(n,t)
    w,e,m,b,ws,fl,tk,ex=P('Warm-up'),P('Explore'),P('Mini-lesson'),P('Brain break'),P('Worksheet'),P('Flex'),P('Talk time'),P('Exit slip')
    return dict(
     warm=f"opening 0 to 2, sneak-peek puzzles 2 to {f(w[0])}, warm-up {f(w[0])} to {f(w[1])}",
     exp=(f(e[0]),f(e[1])),mini=f"mini-lesson {f(m[0])} to {f(m[1])}",brk=f"brain break {f(b[0])} to {f(b[1])}",
     ws=f"worksheet {f(ws[0])} to {f(ws[1])}",
     talk=f"flex {f(fl[0])} to {f(fl[1])} (unscripted: use it for Think harder or catch-up; it is lost first), talk time {f(tk[0])} to {f(tk[1])}",
     exit=f"exit slip {f(ex[0])} to 86, looking back 86 to 88, close and stamp 88 to 90")
def retime(n):
    """Rewrite the time pill and the leading 'Minutes a to b' of every slide of lesson n from p6_budget (idempotent)."""
    L=f'p6l{n}'; D=os.path.join(H,'..','split',L,'project'); B=BUDG.BUD[n]
    for sid in json.load(open(os.path.join(D,'deck.json'),encoding='utf8'))['order']:
        k=sid.split('-',1)[1]; pth=os.path.join(D,'slides',sid+'.html'); s=open(pth,encoding='utf8').read(); o=s
        m=re.search(r'<aside>(.*?)</aside>',s,re.S)
        if k=='title' and m and n!=10:
            t=m.group(1); pl=_plan(n)
            t=t.replace('Time plan:','Time plan (the exact minutes of this lesson, with a standing flex buffer):',1)
            t=re.sub(r'warm-up 0 to 10',pl['warm'],t,1)
            t=re.sub(r'(explore[^,(]*?) 10 to 25',lambda x:x.group(1)+' '+pl['exp'][0]+' to '+pl['exp'][1],t,1)
            t=re.sub(r'teaching 25 to 35',pl['mini'],t,1)
            t=re.sub(r'brain break 35 to 40',pl['brk'],t,1)
            t=re.sub(r'worksheet 40 to 75',pl['ws'],t,1)
            t=re.sub(r'talk time 75 to 82',pl['talk'],t,1)
            t=re.sub(r'exit ticket 82 to 90',pl['exit'],t,1)
            s=s.replace(m.group(1),t,1)
        elif k in B['slides'] or k in B['optional']:
            if k in B['optional']:
                s=PILLRE.sub(lambda x:x.group(1)+OPTLABEL+x.group(3),s,1)
                pre=OPTNOTE
            else:
                a,b=B['slides'][k]; pill=BUDG.pill(n,k)
                if k=='break': s=BREAKRE.sub(lambda x:x.group(1)+pill+x.group(2),s,1)
                else: s=PILLRE.sub(lambda x:x.group(1)+pill+x.group(3),s,1)
                pre=f'Minutes {BUDG.fmt(a)} to {BUDG.fmt(b)}'
                if k=='explore1':
                    ps,pe=_part(n,'Explore') or _part(n,'Challenge'); pre=f'Minutes {BUDG.fmt(ps)} to {BUDG.fmt(pe)} (this slide {BUDG.fmt(a)} to {BUDG.fmt(b)})'
                pre+='. '
            m=re.search(r'<aside>(.*?)</aside>',s,re.S)
            if m:
                body=LEAD.sub('',m.group(1))
                if k=='break': body=re.sub(r'^(Five|Two|Three) minutes',BUDG.fmt(b-a)+' minutes',body)
                s=s.replace(m.group(0),'<aside>'+pre+body+'</aside>',1)
        if s!=o: open(pth,'w',encoding='utf8').write(s)

def apply(n):
    L=f'p6l{n}'; D=os.path.join(H,'..','split',L,'project'); g=G[str(n)]
    open(os.path.join(D,'slides',f'{L}-check.html'),'w').write(sneak_slide(L,g))
    open(os.path.join(D,'slides',f'{L}-reflect.html'),'w').write(reflect_slide(L,g))
    gp=os.path.join(D,'slides',f'{L}-go.html')
    if os.path.exists(gp): os.remove(gp)
    # the Go further what-if leaves the group flow: it goes into the notes of the explore slide
    e1=os.path.join(D,'slides',f'{L}-explore1.html'); s=open(e1,encoding='utf8').read()
    s=s.replace('</aside>',E(go_note(g))+'</aside>',1); open(e1,'w',encoding='utf8').write(s)
    clean(L,D)
    dj=os.path.join(D,'deck.json'); d=json.load(open(dj,encoding='utf8')); o=[x for x in d['order'] if x not in (f'{L}-check',f'{L}-reflect',f'{L}-go')]
    o.insert(o.index(f'{L}-title')+1,f'{L}-check'); o.insert(o.index(f'{L}-exit')+1,f'{L}-reflect'); d['order']=o
    json.dump(d,open(dj,'w'),indent=1,ensure_ascii=False)
    retime(n)
    print(len(o),'slides (with gaps slides, no Go further slide)')
