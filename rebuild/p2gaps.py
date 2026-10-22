"""Fix-pass slides for Math Inquirers P2: 3-minute Sneak-peek puzzles (minutes 1 to 4), an Explore 'Go further' what-if slide, and a 2-minute 'Looking back' slide.
Content comes from p2/gaps.json (shared with the workbook and the tutor guide; built by docs/audit/mk_gaps_p2.py).  Usage in a gen_p2lK.py:
    import p2gaps; p2gaps.add(S, K)            # before the slides are written; adds slides, re-times warm-up / exit, applies neutral labels
    order = p2gaps.order(order, K)             # after the order list exists
"""
import json,os,re,subprocess
import slidekit
from slidekit import *
G=json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','p2','gaps.json')))
BOX=f'<span style="display:inline-block;width:46px;height:46px;border:4px solid {NAVY};border-radius:8px;background:{YEL};vertical-align:middle;margin:0 4px -8px"></span>'
def _txt(s): return E(s).replace('{box}','[ ]')
def _raw(s): return E(s).replace('{box}',BOX)
def _row(left,top,width,label,text,size):
    return pin(left,top,width,f'<p style="font-size:{size}px;font-weight:600;line-height:1.3"><span style="color:{TEAL};font-weight:800">{E(label)}</span>  {_raw(text)}</p>',None,WHITE,20,'18px 28px')

_QB=None
def qbank():
    """Question bank of the level, read from p2/data.js (the same source as the printed workbook and the Question Bank PDF)."""
    global _QB
    if _QB is None:
        r=subprocess.run(['node','-e',"console.log(JSON.stringify(require('./p2/data.js').qbank))"],capture_output=True,text=True,check=True,cwd=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..'))
        _QB=json.loads(r.stdout)
    return _QB
def _frac(a,b,size):
    fs=max(24,round(size*0.8))
    return (f'<span style="display:inline-flex;flex-direction:column;align-items:center;vertical-align:middle;line-height:1;margin:0 5px;font-size:{fs}px">'
            f'<span style="padding:0 5px 3px;border-bottom:3px solid currentColor">{a}</span><span style="padding:3px 5px 0">{b}</span></span>')
def _rich(K,s,size):
    """Escape text; in Lesson 7 show a/b as stacked fractions (same look as the rest of that deck); [ ] as a yellow box."""
    out=''; last=0
    pat=re.compile(r'(\d+)/(\d+)') if K==7 else re.compile(r'(?!)')
    for m in pat.finditer(s):
        out+=E(s[last:m.start()])+_frac(m.group(1),m.group(2),size); last=m.end()
    out+=E(s[last:])
    return out.replace('[ ]',BOX)
def think(K):
    """Think harder slide = the SAME questions as the printed Think harder page (questions 1 to 3 on the slide, question 4 on the page)."""
    items=qbank()[str(K)]['stretch'][:4]
    tot=sum(len(x['q']) for x in items[:3]); size=36 if tot<330 else 32 if tot<470 else 29
    body=h2('Think harder')
    for i,x in enumerate(items[:3]):
        body+=card(p(f'<span style="color:{TEAL}">{i+1}.</span>  {_rich(K,x["q"],size)}',size,600,raw=True))
    body+=p('Question 4 is on your Think harder page.',28,600,MUTED)
    ans='  '.join(f'{i+1}) '+(f'(Question: {x["q"]}) ' if i==3 else '')+x['a'] for i,x in enumerate(items))
    notes=('Open to any child who chooses it (the choice after question 3 on the worksheet). These are the SAME four questions as the printed Think harder page: the slide shows 1 to 3 and question 4 is on the page only. '
           'Never announce who is working on which page. Answers: '+ans)
    return sec(f'p2l{K}-stretch','Think harder',body,notes)
def precheck(K):
    g=G[str(K)]['pre']; C=G['common']
    body=h2('Sneak-peek puzzles')+p('Ideas we have not learnt yet. Guess, draw, count or say "I do not know". Show your paper to your tutor only.',32,600,MUTED)
    tops=[300,590]; hs=[260,300]
    for i,x in enumerate(g):
        size=34 if len(x['q'])<190 else 31
        lab='Q1 (start here)' if i==0 else 'Q2 (think about it)'
        body+=_row(128,tops[i],1250,lab,x['q'],size)+answer(1420,tops[i],372,x['short'])
    notes=('Minutes 1 to 4. Sneak-peek puzzles: two puzzles on the key idea of today, which the children have NOT learnt yet. Say out loud: "These are ideas we have not learnt yet. Guessing is welcome and so is I do not know. Nobody is marked." '
      'Question 1 is an access question: any child can try it with objects, a drawing or counting, so everyone has a first win (about 1 minute). Question 2 is the thinking question (about 2 minutes). '
      'Answers are PRIVATE: each child holds their own paper to the camera for you only, or writes it on their own paper and shows only you on camera. Do not raise whiteboards together, do not read answers out, do not name children. '
      f'Q1 answer: {_txt(g[0]["a"])} Listen for: {_txt(g[0]["w"])} '
      f'Q2 answer: {_txt(g[1]["a"])} Listen for: {_txt(g[1]["w"])} '
      'At the end click to show the answers as "one way to think about it", without saying who had what. Ask only for volunteers: "Would anyone like to tell us how they started?" '
      'Invite the WHOLE group at once, never one child: "When you have finished Start here, you can choose Think harder, Go further or the Investigation." Never announce who is on which page. Pairs are not split unless both children agree. Children can move either way at any time. Everyone joins explore, the mini-lesson, the check-together slides and talk time.')
    return sec(f'p2l{K}-precheck','1–4 MIN',body,notes)
def goexp(K):
    w=G[str(K)]['whatif']
    body=h2('Explore: go further')+p('Finished early, or curious? Try this any time during the explore. It is always your choice.',32,600,MUTED)
    body+=pin(128,330,1664,f'<p style="font-size:44px;font-weight:700;line-height:1.3;color:{TEAL}">{E(w["q"].replace("Go further: ","")[:1].upper()+w["q"].replace("Go further: ","")[1:])}</p>',None,WHITE,24,'36px 44px')
    body+=pin(128,640,1664,'<p style="font-size:34px;font-weight:600;line-height:1.3">Write or draw your answer on paper. Tell your partner or the group how you know when we come back together.</p>',None,SOFT,24,'28px 44px')
    notes=('Minutes 8 to 14. Go further (a second what-if question, so nobody waits). Show this slide with the explore slide or post the question in the chat when the pairs go to their breakout rooms. It is for ANY child who finishes the explore task or wants more: say it to the whole group as a choice, never as a prize, and never name who tries it. Pairs stay together unless both children agree to split. '
      f'Answer: {_txt(w["a"])} Take it at the debrief (minute 14) only if a pair offers it.')
    return sec(f'p2l{K}-goexp','8–14 MIN',body,notes)
def reflect(K):
    g=G[str(K)]; C=G['common']; ticks=g['unstuck']+['I asked for help','I am still stuck (my tutor will check in during the session)']
    body=h2('Looking back')+p('Two minutes. Finish one line, two lines or all three. You may pass on any line.',32,600,MUTED)
    body+=qrow(128,290,1664,'1.','Something I did well …',40)+qrow(128,410,1664,'2.','The hardest part was …',40)
    body+=pin(128,530,1664,f'<p style="font-size:36px;font-weight:800;color:{TEAL}">3. What helped me (tick any):</p>'+''.join(f'<p style="font-size:34px;font-weight:600;line-height:1.3"><span style="display:inline-block;width:30px;height:30px;border:4px solid {NAVY};border-radius:6px;background:#fff;vertical-align:middle;margin:0 14px -4px 0"></span>{E(t)}</p>' for t in ticks),None,WHITE,20,'18px 28px')
    notes=('Minutes 87 to 89 (Lesson 10: 85 to 87). Looking back: about 2 minutes, in the box on the page called "Before you go: Investigation and Looking back" (the page after worksheet page 2; every child reaches it). Children finish one line, two lines or all three, and tick what helped. A pass is always allowed. No marks and no wrong answers. '
      'Tutor script: SAY: '+C['refSay']+' DO: '+C['refDo']+' '+C['close'])
    return sec(f'p2l{K}-reflect','85–87 MIN' if K==10 else '87–89 MIN',body,notes)
LABELS=[('Stretch and Challenge slides are for early finishers.','The Think harder and Go further slides are open to every child who would like them.'),('Early finishers','Any child who would like more'),('early finishers','any child who would like more'),('Finished early? Stretch and Challenge come next.','Want more? Think harder and Go further come next.'),('For early finishers','Think harder'),('>Stretch<','>Think harder<'),('Stretch and Challenge slides are for early finishers.','The Think harder and Go further slides are open to every child who would like them.'),
        ('For children who finish early. ','Open to any child who chooses it. '),('For children who finish early','Open to any child who chooses it'),('children who finish early','any child who chooses to'),
        ('for strong thinkers','for any thinker'),('for early finishers','for any child who chooses it')]
def add(S,K):
    P=f'p2l{K}'; ex=K==10
    S[f'{P}-precheck']=precheck(K); S[f'{P}-reflect']=reflect(K); S[f'{P}-goexp']=goexp(K)
    S[f'{P}-stretch']=think(K)
    r=lambda k,a,b: S.__setitem__(k,S[k].replace(a,b))
    r(f'{P}-warm1','0–5 MIN','4–6 MIN'); r(f'{P}-warm1','Minutes 0 to 5.','Minutes 4 to 6 (a 2-minute game: one or two rounds).')
    r(f'{P}-warm2','5–8 MIN','6–8 MIN'); r(f'{P}-warm2','Minutes 5 to 8.','Minutes 6 to 8 (2 minutes: ask questions 1, 3 and 5; 2 and 4 are spare). Children answer by thumbs, hands, not by naming a child.')
    s=S[f'{P}-title']
    s=re.sub(r'warm-up 0 to 8','Sneak-peek puzzles 1 to 4, warm-up game 4 to 6, quick questions 6 to 8',s)
    s=s.replace('exit ticket 80 to 90.','exit ticket 80 to 87, Looking back 87 to 89, closing and stamps 89 to 90.')
    s=s.replace('exit ticket 80 to 88, certificates 88 to 90','exit ticket 80 to 85, Looking back 85 to 87, certificates 87 to 90')
    S[f'{P}-title']=s
    e=S[f'{P}-exit']
    if ex: e=e.replace('80–88 MIN','80–85 MIN').replace('Minutes 80 to 88.','Minutes 80 to 85.')
    else: e=e.replace('80–90 MIN','80–87 MIN').replace('Minutes 80 to 90.','Minutes 80 to 87.')
    S[f'{P}-exit']=e
    for k in list(S):
        for a,b in LABELS: S[k]=S[k].replace(a,b)
        S[k]=re.sub(r'([Ww])hiteboards up( together)?',lambda m:m.group(1)+'hiteboards face down until 3, 2, 1 (or show only the tutor; never read a board out)',S[k])
    for suf,lab in (('stretch','THINK HARDER'),('challenge','GO FURTHER'),('chdiag','GO FURTHER'),('chwalk','GO FURTHER')):
        k=f'{P}-{suf}'
        if k in S:
            if suf!='stretch': S[k]=S[k].replace('Challenge','Go further').replace('challenge','go-further')
            S[k]=re.sub(r'(<p style="position:absolute;right:128px;top:64px;[^>]*>)[^<]*(</p>)',lambda m:m.group(1)+lab+m.group(2),S[k],count=1)
    t=f'{P}-talk'
    S[t]=S[t].replace('“I know because …”','“I know because …”   “Pass.”')
    S[t]=S[t].replace('</aside>',' Talk time rules: you choose volunteers first ("Who would like to share?"); never cold-call a child by name; any child may say pass; no public tallies, scores or rankings.</aside>')
    w=f'{P}-ws1'
    if w in S: S[w]=S[w].replace('</aside>',' Say once, to everyone: "After question 3 you may choose: carry on, or try Think harder." Never say who is on which page. Invite the WHOLE group at once, never one child: "When you have finished Start here, you can choose Think harder, Go further or the Investigation." Pairs are not split unless both children agree.</aside>')
def order(o,K):
    P=f'p2l{K}'; out=[]
    for i in o:
        out.append(i)
        if i==f'{P}-title': out.append(f'{P}-precheck')
        if i==f'{P}-explore1': out.append(f'{P}-goexp')
        if i==f'{P}-exit': out.append(f'{P}-reflect')
    return out
