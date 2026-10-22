"""Fix-pass slides for Math Inquirers P2: 4.5-minute Sneak-peek puzzles (minutes 1.5 to 6), an Explore 'Go further' what-if box (a corner box on the explore1 slide since the re-budget), and a 2-minute 'Looking back' slide.
All clock times (pills, 'Minutes a to b' in the notes, the title slide's time plan) come from rebuild/p2budget.py: edit minutes there, not in the generators.
Content comes from p2/gaps.json (shared with the workbook and the tutor guide; built by docs/audit/mk_gaps_p2.py).  Usage in a gen_p2lK.py:
    import p2gaps; p2gaps.add(S, K)            # before the slides are written; adds slides, re-times warm-up / exit, applies neutral labels
    order = p2gaps.order(order, K)             # after the order list exists
"""
import json,os,re,subprocess
import slidekit
from slidekit import *
import p2budget
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
    notes=('Minutes 1.5 to 6. Sneak-peek puzzles: two puzzles on the key idea of today, which the children have NOT learnt yet. Say out loud (about 28 words): "Two sneak-peek puzzles on ideas we have not learnt yet. Guessing is welcome, so is I do not know. Nobody is marked. Show your paper to me only." '
      'Question 1 is an access question: any child can try it with objects, a drawing or counting, so everyone has a first win (about 45 seconds). Question 2 is the thinking question (about 90 seconds). Then about 2 minutes for the answers slide and the move on. '
      'Answers are PRIVATE: each child holds their own paper to the camera for you only, or writes it on their own paper and shows only you on camera. Do not raise whiteboards together, do not read answers out, do not name children. '
      f'Q1 answer: {_txt(g[0]["a"])} Listen for: {_txt(g[0]["w"])} '
      f'Q2 answer: {_txt(g[1]["a"])} Listen for: {_txt(g[1]["w"])} '
      'At the end click to show the answers as "one way to think about it", without saying who had what. Ask only for volunteers: "Would anyone like to tell us how they started?" '
      'Invite the WHOLE group at once, never one child: "When you have finished Start here, you can choose Think harder, Go further or the Investigation." Never announce who is on which page. Pairs are not split unless both children agree. Children can move either way at any time. Everyone joins explore, the mini-lesson, the check-together slides and talk time.')
    return sec(f'p2l{K}-precheck','1.5–6 MIN',body,notes)
def goexp_box(K,top=872):
    """Since the re-budget the Go further what-if is a corner box on the explore1 slide (no slide of its own)."""
    w=G[str(K)]['whatif']; q=w["q"].replace("Go further: ","")[:1].upper()+w["q"].replace("Go further: ","")[1:]
    return pin(128,top,1610,f'<p style="font-size:27px;font-weight:700;line-height:1.28"><span style="color:{TEAL};font-weight:800;letter-spacing:1px">GO FURTHER (optional, any time you finish early):</span>  {E(q)}</p>',None,SOFT,20,'12px 26px')
def goexp_note(K):
    w=G[str(K)]['whatif']
    return (' Go further (a second what-if, so nobody waits) is the box at the foot of this slide; the question is also posted in the chat when the pairs go to their breakout rooms. It is for ANY child who finishes the explore task or wants more: say it to the whole group as a choice, never as a prize, and never name who tries it. Pairs stay together unless both children agree to split. '
      f'Answer: {_txt(w["a"])} Take it at the debrief only if a pair offers it.')
def reflect(K):
    g=G[str(K)]; C=G['common']; ticks=g['unstuck']+['I asked for help','I am still stuck (my tutor will check in during the session)']
    body=h2('Looking back')+p('Two minutes. Finish one line, two lines or all three. You may pass on any line.',32,600,MUTED)
    body+=qrow(128,290,1664,'1.','Something I did well …',40)+qrow(128,410,1664,'2.','The hardest part was …',40)
    body+=pin(128,530,1664,f'<p style="font-size:36px;font-weight:800;color:{TEAL}">3. What helped me (tick any):</p>'+''.join(f'<p style="font-size:34px;font-weight:600;line-height:1.3"><span style="display:inline-block;width:30px;height:30px;border:4px solid {NAVY};border-radius:6px;background:#fff;vertical-align:middle;margin:0 14px -4px 0"></span>{E(t)}</p>' for t in ticks),None,WHITE,20,'18px 28px')
    _lb=[x for x in p2budget.parts(K) if x['title']=='Looking back'][0]
    notes=(f'Minutes {p2budget.fmt(_lb["start"])} to {p2budget.fmt(_lb["end"])}. Looking back: about 2 minutes, in the box on the page called "Before you go: Investigation and Looking back" (the page after worksheet page 2; every child reaches it). Children finish one line, two lines or all three, and tick what helped. A pass is always allowed. No marks and no wrong answers. '
      'Tutor script: SAY: '+C['refSay']+' DO: '+C['refDo']+' '+(C['close'] if K!=10 else 'Certificates and closing take the last 3 minutes (87 to 90).'))
    return sec(f'p2l{K}-reflect','87–89 MIN',body,notes)
LABELS=[('Stretch and Challenge slides are for early finishers.','The Think harder and Go further slides are open to every child who would like them.'),('Early finishers','Any child who would like more'),('early finishers','any child who would like more'),('Finished early? Stretch and Challenge come next.','Want more? Think harder and Go further come next.'),('For early finishers','Think harder'),('>Stretch<','>Think harder<'),('Stretch and Challenge slides are for early finishers.','The Think harder and Go further slides are open to every child who would like them.'),
        ('For children who finish early. ','Open to any child who chooses it. '),('For children who finish early','Open to any child who chooses it'),('children who finish early','any child who chooses to'),
        ('for strong thinkers','for any thinker'),('for early finishers','for any child who chooses it')]
def add(S,K,explore_box_top=872):
    P=f'p2l{K}'
    S[f'{P}-precheck']=precheck(K); S[f'{P}-reflect']=reflect(K)
    S[f'{P}-stretch']=think(K)
    # Go further what-if: a corner box on explore1 (no slide of its own)
    e=S[f'{P}-explore1']
    foot='<p style="position:absolute;left:128px;bottom:64px;'
    assert foot in e, 'explore1 footer not found'
    e=e.replace(foot,goexp_box(K,explore_box_top)+foot,1)
    e=e.replace('</aside>',goexp_note(K)+'</aside>')
    S[f'{P}-explore1']=e
    s=S[f'{P}-title']
    assert 'Time plan:' in s
    s=s[:s.index('Time plan:')]+p2budget.plan_sentence(K)+' Kit ready at minute 0: ask families to put every item on the desk before the lesson starts (a 30-second check at the start).</aside>\n</section>\n'
    S[f'{P}-title']=s
    r=lambda k,a,b: S.__setitem__(k,S[k].replace(a,b))
    S[f'{P}-warm1']=S[f'{P}-warm1'].replace('</aside>',' A game of about 2.5 minutes: stop it on the clock even if the game is not finished.</aside>')
    S[f'{P}-warm2']=S[f'{P}-warm2'].replace('</aside>',' Ask quick questions 1 and 3 only (about 2 minutes): children answer by thumbs, hands, not by naming a child. The other questions are spare.</aside>')
    S[f'{P}-break']=S[f'{P}-break'].replace('Four minutes.','Three minutes: two of movement, one for a drink of water.')
    S[f'{P}-explore2']=S[f'{P}-explore2'].replace('</aside>',' Keep it moving (about 4 minutes in all): ask "how do you know?" on question 2 only; about 15 seconds of talk on the other questions.</aside>')
    e=S[f'{P}-exit']
    S[f'{P}-exit']=e.replace('</aside>',' Hold-up: children hold their slips up one at a time (never all together); the answer is on the next click. About 2 minutes of child work.</aside>')
    for k in list(S):
        for a,b in LABELS: S[k]=S[k].replace(a,b)
        S[k]=re.sub(r'([Ww])hiteboards up( together)?',lambda m:m.group(1)+'hiteboards face down until 3, 2, 1 (or show only the tutor; never read a board out)',S[k])
    for suf,lab in (('stretch','THINK HARDER'),('challenge','GO FURTHER'),('chdiag','GO FURTHER'),('chwalk','GO FURTHER')):
        k=f'{P}-{suf}'
        if k in S and suf!='stretch': S[k]=S[k].replace('Challenge','Go further').replace('challenge','go-further')
    t=f'{P}-talk'
    S[t]=S[t].replace('“I know because …”','“I know because …”   “Pass.”')
    S[t]=S[t].replace('</aside>',' Talk time rules: you choose volunteers first ("Who would like to share?"); never cold-call a child by name; any child may say pass; no public tallies, scores or rankings.</aside>')
    w=f'{P}-ws1'
    if w in S: S[w]=S[w].replace('</aside>',' Say once, to everyone: "After question 3 you may choose: carry on, or try Think harder." Never say who is on which page. Invite the WHOLE group at once, never one child: "When you have finished Start here, you can choose Think harder, Go further or the Investigation." Pairs are not split unless both children agree.</aside>')
    w=f'{P}-ws2'
    if w in S: S[w]=S[w].replace('</aside>',' Tutor rule at minute '+p2budget.fmt([x for x in p2budget.parts(K) if x['title']=='Worksheet page 2 (alone)'][0]['start'])+': if the clock is more than 2 minutes late, drop the last Core question of page 2 to take-home (children draw a star beside it). Never shorten talk time, the exit ticket, looking back or the closing. Questions marked with a star and the words take-home on the page are done at home; their answers are still on the check-together slide.</aside>')
    p2budget.apply(S,K)
    return S
def order(o,K):
    P=f'p2l{K}'; out=[]
    for i in o:
        out.append(i)
        if i==f'{P}-title': out.append(f'{P}-precheck')
        if i==f'{P}-exit': out.append(f'{P}-reflect')
    return out
