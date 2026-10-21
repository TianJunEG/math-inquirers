"""P3 close-the-gaps: adds the Warm-up check slide (after the title) and the 'What was hard?' look-back slide (last) to a lesson deck,
and re-times the warm-up game slides. Data: p3/gifted.json. Used by rebuild/gen_p3lK.py just before the slides are written."""
import json,os,re,sys
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,H)
import slidekit
from slidekit import *
G=json.load(open(os.path.join(H,'..','p3','gifted.json'),encoding='utf8'))
def fr(n,d): return f'<span style="display:inline-flex;flex-direction:column;align-items:center;vertical-align:middle;line-height:1.1;margin:0 6px"><span style="padding:0 6px">{n}</span><span style="border-top:4px solid currentColor;padding:4px 6px 0">{d}</span></span>'
def rich(s): return re.sub(r'\[\[(\d+)/(\d+)\]\]',lambda m:fr(m.group(1),m.group(2)),E(s))
def plain(s): return re.sub(r'\[\[(\d+)/(\d+)\]\]',r'\1/\2',s)
def add(S,order,ln):
    g=G[str(ln)]; pre=order[0][:-len('title')]
    # re-time the warm-up game slides (the check takes minutes 2 to 5)
    for sid in list(S):
        if sid==pre+'warm1':
            S[sid]=S[sid].replace('0–5 MIN','5–8 MIN',1); assert '5–8 MIN' in S[sid]
            S[sid]=S[sid].replace('Minutes 0 to 5.','Minutes 5 to 8 (after the warm-up check).',1)
        if sid==pre+'warm2':
            S[sid]=S[sid].replace('5–10 MIN','8–10 MIN',1); assert '8–10 MIN' in S[sid]
            S[sid]=S[sid].replace('Minutes 5 to 10.','Minutes 8 to 10.',1)
    t=S[pre+'title']
    assert 'warm-up 0 to 10' in t and re.search(r'exit ticket[a-z ]{0,30}80 to 90',t), ln
    t=t.replace('warm-up 0 to 10','warm-up check 2 to 5, then the warm-up game and quick questions to minute 10',1)
    t=re.sub(r'(exit ticket[a-z ]{0,30}80 to 90)',r'\1, with the one-minute look-back "What was hard?" on the last slide',t,count=1)
    assert len(t)<3900, len(t)
    S[pre+'title']=t
    # warm-up check slide
    body=h2('Warm-up check')+p('Two questions. Answer on your own whiteboard. Hold it up on three. Be ready to say why.',32,600,MUTED)
    for i,c in enumerate(g['check']):
        top=330+i*270
        body+=pin(128,top,1130,p(f'<span style="color:{TEAL};font-weight:800">{i+1}.</span>  {rich(c["q"])}',36,600,raw=True),None,WHITE,20,'22px 30px','box-sizing:border-box;min-height:240px')
        body+=pin(1290,top,502,p(rich(c['a']),40,800,raw=True),'pop',YEL,20,'20px 26px','box-sizing:border-box;min-height:120px')
    notes=('Minutes 2 to 5. Warm-up check: two quick questions on today\'s key idea in a new setting. Whiteboards, on their own, boards up together, then click to show the answer and ask one child to say why. Never mark or label children in front of the group. '
      + ' '.join(f'Q{i+1}: {plain(c["a"])}. Listen for: {plain(c["why"])}' for i,c in enumerate(g['check']))
      + ' FAST TRACK: a child who gets both right AND can say why starts on the Think Harder pages and the Investigation (last workbook page of the lesson) at minute 40, while the group works the core pages. Tell them by name in the chat or a small breakout room. Different children can have different pages, nobody is labelled, and the check decides again next lesson.')
    S[pre+'warmcheck']=sec(pre+'warmcheck','2–5 MIN',body,notes)
    # look-back slide
    ex=', '.join(g['reflect'])
    c1=card(p('1.  The hardest part was ...',42,800)+p('For example: '+ex+', or something else.',28,500,MUTED))
    c2=card(p('2.  I got unstuck by ...',42,800)+p('For example: drawing a picture, making a list, trying a number and checking, asking or listening.',28,500,MUTED))
    c3=card(p('3.  Next time I will try ...',42,800))
    body=h2('What was hard?')+p('One minute. Open the last page of today\'s lesson. Tick or write. There are no right answers.',32,600,MUTED)+c1+c2+c3
    notes=('Minutes 88 to 90. Look-back. Say: "Turn to the last page of today\'s lesson and find What was hard? Tick or write one thing for each sentence. There are no right answers." Take one volunteer to share (the hardest part, or what got them unstuck). '
      'Never collect it, mark it or grade it. Praise the strategy ("you drew it and that got you unstuck"), not the speed or the answer. If a child ticked "I am still stuck", plan two minutes of catch-up at the start of the next lesson.')
    S[pre+'reflect']=sec(pre+'reflect','88–90 MIN',body,notes)
    new=list(order); new.insert(new.index(pre+'title')+1,pre+'warmcheck'); new.append(pre+'reflect')
    return new
