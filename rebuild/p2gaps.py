"""Fix-pass slides for Math Inquirers P2: 3-minute Sneak-peek puzzles (minutes 1 to 4), an Explore 'Go further' what-if slide, and a 2-minute 'Looking back' slide.
Content comes from p2/gaps.json (shared with the workbook and the tutor guide; built by docs/audit/mk_gaps_p2.py).  Usage in a gen_p2lK.py:
    import p2gaps; p2gaps.add(S, K)            # before the slides are written; adds slides, re-times warm-up / exit, applies neutral labels
    order = p2gaps.order(order, K)             # after the order list exists
"""
import json,os,re
import slidekit
from slidekit import *
G=json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','p2','gaps.json')))
ST=json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','p2','stories.json')))   # one mathematician per lesson (docs/stories/final_p2.json, shortened child page text)
BOX=f'<span style="display:inline-block;width:46px;height:46px;border:4px solid {NAVY};border-radius:8px;background:{YEL};vertical-align:middle;margin:0 4px -8px"></span>'
def _txt(s): return E(s).replace('{box}','[ ]')
def _raw(s): return E(s).replace('{box}',BOX)
def _row(left,top,width,label,text,size):
    return pin(left,top,width,f'<p style="font-size:{size}px;font-weight:600;line-height:1.3"><span style="color:{TEAL};font-weight:800">{E(label)}</span>  {_raw(text)}</p>',None,WHITE,20,'18px 28px')
def precheck(K,idx=0):
    """idx 0 = question 1 slide (minute 1-2), idx 1 = question 2 slide (minute 2-4). One question per slide keeps the text short for ages 7-9."""
    g=G[str(K)]['pre']; C=G['common']; x=g[idx]
    if idx==0: body=h2('Sneak-peek puzzles')+p('Ideas we have not learnt yet. Guess, draw, count or say "I do not know". Show your paper to your tutor only.',32,600,MUTED)
    else: body=h2('Sneak-peek puzzles: question 2')+p('Take your time. Guessing is welcome.',32,600,MUTED)
    size=40 if len(x['q'])<190 else 36
    lab='Q1 (start here)' if idx==0 else 'Q2 (think about it)'
    body+=_row(128,330,1190,lab,x['q'],size)+answer(1420,330,372,x['short'])
    notes=('Minutes 1 to 4 (this slide is question 1, minutes 1 to 2; click to the next slide for question 2). Sneak-peek puzzles: two puzzles on the key idea of today, which the children have NOT learnt yet. Say out loud: "These are ideas we have not learnt yet. Guessing is welcome and so is I do not know. Nobody is marked." '
      'Question 1 is an access question: any child can try it with objects, a drawing or counting, so everyone has a first win (about 1 minute). Question 2 is the thinking question (about 2 minutes). '
      'Answers are PRIVATE: each child holds their own paper to the camera for you only, or writes it on their own paper and shows only you on camera. Do not raise whiteboards together, do not read answers out, do not name children. '
      f'Q1 answer: {_txt(g[0]["a"])} Listen for: {_txt(g[0]["w"])} '
      f'Q2 answer: {_txt(g[1]["a"])} Listen for: {_txt(g[1]["w"])} '
      'At the end click to show the answers as "one way to think about it", without saying who had what. Ask only for volunteers: "Would anyone like to tell us how they started?" '
      'Invite the WHOLE group at once, never one child: "When you have finished Start here, you can choose Think harder, Go further or the Investigation." Never announce who is on which page. Pairs are not split unless both children agree. Children can move either way at any time. Everyone joins explore, the mini-lesson, the check-together slides and talk time.')
    if idx==1:
        notes=('Minutes 2 to 4. Question 2, the thinking question (about 2 minutes). Same rules as question 1: guessing and "I do not know" are welcome; answers are shown to you only on each child\'s own paper; nothing is read out; nobody is marked or named. '
          f'Q2 answer: {_txt(g[1]["a"])} Listen for: {_txt(g[1]["w"])} At the end click to show the answer as "one way to think about it", without saying who had what. Ask only for volunteers: "Would anyone like to tell us how they started?" Then move on to the warm-up game.')
        return sec(f'p2l{K}-precheck2','2–4 MIN',body,notes)
    return sec(f'p2l{K}-precheck','1–2 MIN',body,notes)
def story(K):
    """Optional 2-minute 'Story break: <name>' slide, right after the brain-break slide (minutes 34 to 36 of the 32-36 break). The try-it answer is in the notes only."""
    s=ST[str(K)]
    meta=f'<div style="display:flex;align-items:center;gap:24px">{chip("Optional  •  about 2 minutes  •  skip any time",YEL,NAVY,26)}<p style="font-size:30px;font-weight:700;color:{MUTED}">{E(s["country"])}  •  {E(s["years"])}</p></div>'
    inner=p(s['story'],38,600)
    if s['legend']: inner+=p(s['legend'],30,800,TEAL)
    body=h2('Story break: '+s['name'],64)+meta+card(inner,extra='padding:26px 40px;gap:10px')
    body+=f'<div data-build-in="rise" style="background:{SOFT};border-radius:24px;padding:20px 40px;display:flex;flex-direction:column;gap:8px">{chip("Try it (optional)",TEAL,CREAM,26)}<p style="font-size:34px;font-weight:700;line-height:1.3">{E(s["try_it"])}</p></div>'
    notes=('Story break, about 2 minutes, OPTIONAL (minutes 34 to 36: do a 2-minute movement game first, then this). SKIP IT, without comment, if you are behind time, the group is tired or the break needs all four minutes; nothing later in the lesson depends on it. '
      f'Say: "Time for a short story about a mathematician. Just listen." Read the story aloud (about 30 seconds). '
      + (f'Say clearly that this is a story or a memory told long after the event: {s["legend_note"]} ' if s['legend_note'] else '')
      + f'Why it is here: {s["link"]} Then click for the Try it question. It is a choice, never a test: ask "Would anyone like to try this one?", take volunteers only, never name a child, nobody is marked, passing is always fine. Children can show the answer on their own paper to the tutor only, or say it to a partner. '
      f'TRY-IT ANSWER (tutor only): {s["try_it_answer"]} '
      'Keep it to 2 minutes, then say "Thank you. Water, then back to our seats." Source and checking notes: docs/stories/final_p2.json.')
    return sec(f'p2l{K}-story','34–36 MIN (OPTIONAL)',body,notes)
def goexp(K):
    w=G[str(K)]['whatif']
    body=h2('Explore: go further')+p('Finished early or curious? Try this. It is your choice.',32,600,MUTED)
    body+=pin(128,330,1664,f'<p style="font-size:44px;font-weight:700;line-height:1.3;color:{TEAL}">{E(w["q"].replace("Go further: ","")[:1].upper()+w["q"].replace("Go further: ","")[1:])}</p>',None,WHITE,24,'36px 44px')
    body+=pin(128,640,1664,'<p style="font-size:34px;font-weight:600;line-height:1.3">Write or draw your answer on paper.</p>',None,SOFT,24,'28px 44px')
    notes=('Minutes 8 to 14. Go further (a second what-if question, so nobody waits). Show this slide with the explore slide or post the question in the chat when the pairs go to their breakout rooms. It is for ANY child who finishes the explore task or wants more: say it to the whole group as a choice, never as a prize, and never name who tries it. Pairs stay together unless both children agree to split. '
      f'Answer: {_txt(w["a"])} Take it at the debrief (minute 14) only if a pair offers it.')
    return sec(f'p2l{K}-goexp','8–14 MIN',body,notes)
def reflect(K):
    g=G[str(K)]; C=G['common']; ticks=g['unstuck']+['I asked for help','I am still stuck (my tutor will read this at the next lesson)']
    body=h2('Looking back')+p('Two minutes. Finish one line, two lines or all three. You may pass on any line.',32,600,MUTED)
    body+=qrow(128,290,1664,'1.','Something I did well …',40)+qrow(128,410,1664,'2.','The hardest part was …',40)
    body+=pin(128,530,1664,f'<p style="font-size:36px;font-weight:800;color:{TEAL}">3. What helped me (tick any):</p>'+''.join(f'<p style="font-size:34px;font-weight:600;line-height:1.3"><span style="display:inline-block;width:30px;height:30px;border:4px solid {NAVY};border-radius:6px;background:#fff;vertical-align:middle;margin:0 14px -4px 0"></span>{E(t)}</p>' for t in ticks),None,WHITE,20,'18px 28px')
    notes=('Minutes 87 to 89 (Lesson 10: 85 to 87). Looking back: about 2 minutes, on the small box on the last core page of the workbook (every child reaches it). Children finish one line, two lines or all three, and tick what helped. A pass is always allowed. No marks and no wrong answers. '
      'Tutor script: SAY: '+C['refSay']+' DO: '+C['refDo']+' '+C['close'])
    return sec(f'p2l{K}-reflect','87–89 MIN',body,notes)
LABELS=[('Stretch and Challenge slides are for early finishers.','The Think harder and Go further slides are open to every child who would like them.'),('Early finishers','Any child who would like more'),('early finishers','any child who would like more'),('Finished early? Stretch and Challenge come next.','Want more? Think harder and Go further come next.'),('For early finishers','Think harder'),('>Stretch<','>Think harder<'),('Stretch and Challenge slides are for early finishers.','The Think harder and Go further slides are open to every child who would like them.'),
        ('For children who finish early. ','Open to any child who chooses it. '),('For children who finish early','Open to any child who chooses it'),('children who finish early','any child who chooses to'),
        ('for strong thinkers','for any thinker'),('for early finishers','for any child who chooses it')]
def investigation(K):
    v=G[str(K)]['invest']
    txt=v['text']+((' '+v['need']) if v.get('need') else '')
    # the setting shows at once; each lettered part is revealed on a click (one idea at a time)
    chunks=[c for c in re.split(r'\s(?=\([a-d]\)\s)',txt) if c]
    size=36 if len(txt)<300 else 34
    body=h2('Investigation: '+v['title'])+p('A puzzle with more than one good answer. Share one way you tried it, or pass.',32,600,MUTED)
    inner=''
    for n,c in enumerate(chunks):
        bi='' if n==0 else ' data-build-in="rise"'
        inner+=f'<div{bi} style="background:#FFFFFF;border-radius:20px;padding:14px 28px"><p style="font-size:{size}px;font-weight:600;line-height:1.3">{E(c)}</p></div>'
    inner+=f'<div data-build-in="fade" style="background:{SOFT};border-radius:20px;padding:14px 28px"><p style="font-size:{size}px;font-weight:700;line-height:1.3;color:{TEAL}">{E(v["first"])}</p></div>'
    body+=f'<div style="display:flex;flex-direction:column;gap:12px">{inner}</div>'
    notes=('Minutes 77 to 80 (3 minutes, after talk time). Investigation debrief. The Investigation is printed on the last core page of the workbook; children may have started it any time after question 3 (it is open to everyone), or it is take-home. '
      'Say to the whole group: "Who would like to share one way they tried the Investigation? Passing is fine." Ask for volunteers only; never name a child; no public tallies, scores or rankings. Several answers are right: praise the method (a list in order, a table, a drawing), not the speed. '
      'If nobody has started it, show the first step on the slide and let pairs try for one minute, then set it as take-home. '
      'Model answer and what to look for: '+_txt(v['model']))
    return sec(f'p2l{K}-invest','77–80 MIN',body,notes)
CARD=re.compile(r'<div style="background:#FFFFFF;border-radius:24px;padding:32px 40px[^>]*>(?:(?!<div).)*?</div>',re.S)
def splitcards(S,P):
    """Go further slide: one item per slide (less text at once for ages 7-9). Slide 2 is 'challenge2'."""
    k=f'{P}-challenge'
    if k not in S: return
    h=S[k]; cards=CARD.findall(h)
    if len(cards)!=2: return
    a=h.replace(cards[1],'',1)
    b=h.replace(cards[0],'',1)
    b=re.sub(r'<section id="([^"]*)"',lambda m:'<section id="'+m.group(1)+'-2"',b,count=1)
    S[k]=a; S[k+'2']=b
def add(S,K):
    P=f'p2l{K}'; ex=K==10
    S[f'{P}-story']=story(K); S[f'{P}-invest']=investigation(K); S[f'{P}-precheck']=precheck(K); S[f'{P}-precheck2']=precheck(K,1); S[f'{P}-reflect']=reflect(K); S[f'{P}-goexp']=goexp(K)
    r=lambda k,a,b: S.__setitem__(k,S[k].replace(a,b))
    r(f'{P}-warm1','0–5 MIN','4–6 MIN'); r(f'{P}-warm1','Minutes 0 to 5.','Minutes 4 to 6 (a 2-minute game: one or two rounds).')
    r(f'{P}-warm2','5–8 MIN','6–8 MIN'); r(f'{P}-warm2','Minutes 5 to 8.','Minutes 6 to 8 (2 minutes: ask questions 1, 3 and 5; 2 and 4 are spare). Children answer by thumbs, hands, not by naming a child.')
    s=S[f'{P}-title']
    s=s.replace('talk time 72 to 80','talk time 72 to 77, Investigation share 77 to 80')
    s=re.sub(r'warm-up 0 to 8','Sneak-peek puzzles 1 to 4, warm-up game 4 to 6, quick questions 6 to 8',s)
    s=s.replace('exit ticket 80 to 90.','exit ticket 80 to 87, Looking back 87 to 89, closing and stamps 89 to 90.')
    s=s.replace('exit ticket 80 to 88, certificates 88 to 90','exit ticket 80 to 85, Looking back 85 to 87, certificates 87 to 90')
    s=s.replace('brain break 32 to 36','brain break 32 to 36 (with an optional 2-minute Story break at 34 to 36)')
    S[f'{P}-title']=s
    S[f'{P}-break']=S[f'{P}-break'].replace('</aside>',' Story break (optional, 2 minutes): if you run it, keep the movement game to 2 minutes (32 to 34), then click on to the Story break slide (34 to 36). If you are short of time, skip it and use all four minutes for the break.</aside>')
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
    splitcards(S,P)
    t=f'{P}-talk'
    S[t]=S[t].replace('72–80 MIN','72–77 MIN').replace('Minutes 72 to 80.','Minutes 72 to 77 (5 minutes: pairs talk 2, then share).')
    S[t]=S[t].replace('“I know because …”','“I know because …”   “Pass.”')
    S[t]=S[t].replace('</aside>',' Talk time rules: you choose volunteers first ("Who would like to share?"); never cold-call a child by name; any child may say pass; no public tallies, scores or rankings.</aside>')
    w=f'{P}-ws1'
    if w in S: S[w]=S[w].replace('</aside>',' Say once, to everyone: "After question 3 you may choose: carry on, or try Think harder." Never say who is on which page. Invite the WHOLE group at once, never one child: "When you have finished Start here, you can choose Think harder, Go further or the Investigation." Pairs are not split unless both children agree.</aside>')
def order(o,K):
    P=f'p2l{K}'; out=[]
    for i in o:
        out.append(i)
        if i==f'{P}-break': out.append(f'{P}-story')
        if i==f'{P}-title': out.append(f'{P}-precheck'); out.append(f'{P}-precheck2')
        if i==f'{P}-explore1': out.append(f'{P}-goexp')
        if i==f'{P}-talk': out.append(f'{P}-invest')
        if i==f'{P}-challenge': out.append(f'{P}-challenge2')
        if i==f'{P}-exit': out.append(f'{P}-reflect')
    return out
