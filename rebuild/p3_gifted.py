"""P3 fix pass: called by rebuild/gen_p3lK.py just before the slides are written. Data: p3/gifted.json.
 - sneak-peek puzzles slide (minutes 2 to 5; one access puzzle and one thinking puzzle; private answers; nobody marked)
 - look-back slide (minutes 86 to 88; short, safe, pass always allowed)
 - Go further what-if on the explore slide (so nobody waits)
 - one lesson timeline (tags and notes minutes taken from gifted.json "plan")
 - neutral names: Think harder / Go further / Investigation (no labels such as 'for early finishers')
 - talk-time rules (volunteers first, pass allowed, no cold-calling, no public tallies)"""
import json,os,re,sys
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,H)
import slidekit
from slidekit import *
G=json.load(open(os.path.join(H,'..','p3','gifted.json'),encoding='utf8'))
def fr(n,d): return f'<span style="display:inline-flex;flex-direction:column;align-items:center;vertical-align:middle;line-height:1.1;margin:0 6px"><span style="padding:0 6px">{n}</span><span style="border-top:4px solid currentColor;padding:4px 6px 0">{d}</span></span>'
def rich(s): return re.sub(r'\[\[(\d+)/(\d+)\]\]',lambda m:fr(m.group(1),m.group(2)),E(s))
def plain(s): return re.sub(r'\[\[(\d+)/(\d+)\]\]',r'\1/\2',s)
TAG=re.compile(r'(position:absolute;right:128px;top:64px;[^>]*>)([^<]*)(</p>)')
GLOBAL=[('Stretch and Challenge slides are for early finishers.','Think harder and Go further are open to every child (they choose, when the whole group is invited).'),
 ('Stretch and Challenge are for early finishers.','Think harder and Go further are open to every child (they choose, when the whole group is invited).'),
 ('For children who finish early.','For children who choose Think harder.'),
 ('Finished early? Stretch and Challenge come next.','Want more? Think harder and Go further come next.'),
 ('Early finishers:','Ready for more:'),('Finished early','Ready for more'),('Quick finisher','Ready for more'),('quick finisher','child who wants more'),
 ('For early finishers','Think harder')]
def retime(s,a,b):
    s=TAG.sub(lambda m:m.group(1)+f'{a}–{b} MIN'+m.group(3),s,count=1)
    s=re.sub(r'(<aside>)Minutes? \d+(?: to \d+)?',lambda m:m.group(1)+f'Minutes {a} to {b}',s,count=1)
    return s
def aside_add(s,txt):
    assert '</aside>' in s
    return s.replace('</aside>',' '+E(txt)+'</aside>',1)
def add(S,order,ln):
    g=G[str(ln)]; pl=g['plan']; pre=order[0][:-len('title')]
    # ---- global neutral wording ----
    for sid in list(S):
        for a,b in GLOBAL: S[sid]=S[sid].replace(E(a) if E(a)!=a else a,E(b) if E(b)!=b else b)
        S[sid]=S[sid].replace('Stretch and Challenge','Think harder and Go further')
    # ---- one timeline ----
    for suf,(a,b) in pl.items():
        sid=pre+suf
        if sid in S and suf not in ('warmcheck','reflect'): S[sid]=retime(S[sid],a,b)
    # ---- neutral names on the pages that follow the worksheet ----
    for suf in ('stretch',):
        S[pre+suf]=S[pre+suf].replace('>Stretch<','>Think harder<',1)
    S[pre+'challenge']=re.sub(r'(<h2[^>]*>)Challenge(</h2>)',r'\1Go further\2',S[pre+'challenge'],count=1)
    for suf in ('chdiag','chwalk'):
        S[pre+suf]=re.sub(r'(<h2[^>]*>)Challenge: ',r'\1Go further: ',S[pre+suf],count=1)
    for suf in ('stretch','challenge','chdiag','chwalk','ws1','ws2','ws1ans','ws2ans','talk'):
        s=S[pre+suf]
        s=re.sub(r'\b(the )?Challenge\b(?! Day)',lambda m:('the ' if m.group(1) else '')+'Go further',s)
        s=s.replace('Go further: see it','Go further: see it')
        S[pre+suf]=s
    # ---- title notes: one time plan ----
    S[pre+'title']=re.sub(r'(PRIMARY 3 +• +LESSON \d+ +• +WEEK \d+)(</p>)',r'\1  •  0–2 MIN\2',S[pre+'title'],count=1)
    t=S[pre+'title']
    m=re.search(r'Time plan:.*?(?=If the class is behind)',t,re.S); assert m,ln
    par=re.search(r'teaching 25 to 35( \([^)]*\))?',m.group(0)); par=par.group(1) if par and par.group(1) else ''
    new=('Time plan: opening 0 to 2, sneak-peek puzzles 2 to 5 (own paper, nobody marked), warm-up game 5 to 8 and quick questions 8 to 10, explore 10 to 25 (a Go further what-if is on the explore slide from minute 10), '
         f'teaching 25 to 35{par if par else " (click to reveal each step and answer)"}, brain break 35 to 40, worksheet 40 to 70 (page 1 in pairs, short teaching, page 2 on their own, a check-together slide after each page; after question 3 of page 1 any child may choose Think harder or the Investigation; from minute 67 everyone chooses), '
         'talk time 70 to 80 (volunteers first, pass is fine), exit ticket 80 to 86, look back 86 to 88, stamp and close 88 to 90. Think harder, Go further and the Investigation are open to every child; the tutor never announces who is on which page and invites the whole group, never one child. ')
    t=t[:m.start()]+new+t[m.end():]
    assert len(t)<3950,(ln,len(t))
    S[pre+'title']=t
    # ---- sneak-peek slide ----
    body=h2('Sneak-peek puzzles')+p('Ideas we have not learnt yet. Have a go: guessing and “I do not know” are welcome. Nobody is marked.',32,600,MUTED)
    body+=p('Write your answer on your own paper. Show it to your tutor on camera when asked.',30,600,MUTED)
    for i,c in enumerate(g['check']):
        pic=c.get('pic'); top=395+(i*(330 if (g['check'][0].get('pic')) else 250))
        hint='Try it with objects, a drawing or counting.' if i==0 else 'Think about it. Show how you thought.'
        picx=p(pic,84,800,NAVY) .replace('<p style="','<p style="letter-spacing:40px;font-family:Fredoka, Arial, sans-serif;margin:4px 0;',1) if pic else ''
        body+=pin(128,top,1664,p(f'<span style="color:{TEAL};font-weight:800">Puzzle {i+1}.</span>  {rich(c["q"])}',36,600,raw=True)+picx+p(hint,26,700,TEAL),None,WHITE,20,'20px 30px','box-sizing:border-box;min-height:215px')
    notes=('Minutes 2 to 5. Sneak-peek puzzles: two small puzzles on ideas we have not learnt yet. SAY: "These are ideas we have not learnt yet. Guessing is welcome and so is I do not know. Nobody is marked." '
      'Puzzle 1 is an ACCESS puzzle: any child can try it with objects, a drawing or counting, so everyone has a first win. Puzzle 2 is a thinking puzzle. '
      'Children write answers on their own paper and show them only to the tutor on camera (or everybody holds paper to the camera at the same moment). No private messages. Never answers read out, never "who got it?". Do not show the answers on the slide now. '
      + ' '.join(f'Puzzle {i+1} answer (tutor only): {plain(c["a"])}. Listen for: {plain(c["why"])}' for i,c in enumerate(g['check']))
      + ' Come back to puzzle 2 at talk time: "Now we know the idea, how could it help?" (volunteers only). '
      'Invite the WHOLE group once, never one child; this is an invitation, not a ranking, and any child may choose Think harder or the Investigation after question 3 of page 1. Never announce who is on which page, and never split pairs unless both children agree.')
    S[pre+'warmcheck']=sec(pre+'warmcheck',f'{pl["warmcheck"][0]}–{pl["warmcheck"][1]} MIN',body,notes)
    # ---- Go further what-if on the explore slide ----
    e=S[pre+'explore1']
    box=pin(868,106,924,p(f'<span style="color:{TEAL};font-weight:800">Go further, any time:</span>  {rich(g["go"])}',26,600,raw=True),None,SOFT,20,'12px 22px','box-sizing:border-box')
    k='<p style="position:absolute;left:128px;bottom:64px'; assert k in e,ln
    e=e.replace(k,box+'\n'+k,1)
    e=aside_add(e,'GO FURTHER (on the slide from minute 10, so nobody waits): '+plain(g['go'])+' Answer: '+plain(g['goans'])+' Any pair may choose it as soon as their first task is done; do not say who is ready for it.')
    S[pre+'explore1']=e
    # ---- talk time rules ----
    tk=S[pre+'talk']
    tk=tk.replace('Ask each child','Ask volunteers').replace('each child','volunteers')
    tk=aside_add(tk,'TALK TIME RULES: ask for volunteers first; a pass is always fine and so is sharing with a partner. No cold-calling by name, no public tallies or rankings, and nobody is told they were wrong in front of the group. Nobody is called on by name.')
    k='<p style="position:absolute;left:128px;bottom:64px'; assert k in tk,ln
    tk=tk.replace(k,'<p style="font-size:28px;font-weight:700;color:#1F7A6F">You can share, share with a partner, or pass.</p>\n'+k,1)
    S[pre+'talk']=tk
    # ---- exit ticket: private ----
    ex=S[pre+'exit']
    ex=aside_add(ex,'Answers are shown only to the tutor on camera (own paper). Never mark or read out answers in front of the group. Reflection (look back) follows on the next slide, 2 minutes.')
    S[pre+'exit']=ex
    # ---- look-back slide ----
    ex2=', '.join(g['reflect'])
    dw=', '.join(g['didwell'])
    c1=card(p('Something I did well:',40,800)+p('Tick one: '+dw+', or something else.',28,500,MUTED))
    c2=card(p('The hardest part was ...',40,800)+p('For example: '+ex2+', or something else.',28,500,MUTED))
    c3=card(p('What helped me:',40,800)+p('Tick one: drawing a picture, making a list, trying a number and checking, I asked for help, or I am still stuck (my tutor will check in with me).',28,500,MUTED))
    body=h2('Look back')+p('Two minutes. Open the last page of today’s lesson. Tick or write. You may pass on any line.',32,600,MUTED)+c1+c2+c3
    notes=('Minutes 86 to 88. Look back: short and safe. SAY: "Turn to the last page of today and find Look back. Tick or write one thing for each line. There are no right answers, and you may pass on any line." Give a full 2 minutes. '
      'The page is never collected, marked or read out in front of the group. Children keep their page. A child who ticked "I am still stuck" gets a check-in in the open session: a quick visit to the shared breakout room or a hand signal, with a parent nearby. Never a private message. '
      'Invite volunteers only (one or two) to share something they did well, or what helped. Praise the strategy ("you drew it and that got you unstuck"), not the speed or the answer. Then stamp the journal and close (minutes 88 to 90).')
    S[pre+'reflect']=sec(pre+'reflect',f'{pl["reflect"][0]}–{pl["reflect"][1]} MIN',body,notes)
    new=list(order)
    if pre+'warmcheck' not in new: new.insert(new.index(pre+'title')+1,pre+'warmcheck')
    if pre+'reflect' not in new:
        new.insert(new.index(pre+'exit')+1,pre+'reflect')
    return new
