"""P6 mathematician stories: one optional 'Story break' slide per lesson, placed straight after the brain-break slide.
Called at the end of each gen_p6lK.py (after p6_gaps.apply): p6_stories.apply(K). Reads p6/content/stories.json."""
import json,os
import slidekit
from slidekit import *
H=os.path.dirname(os.path.abspath(__file__))
ST=json.load(open(os.path.join(H,'..','p6','content','stories.json'),encoding='utf8'))

def story_slide(L,s):
    sub=f"{s['name']}  •  {s['years']}  •  {s['country']}"
    body=h2('Story break: '+s['name'],64)
    inner=p(sub,28,700,TEAL)
    inner+=f'<div style="background:{WHITE};border-radius:24px;padding:24px 36px">'+p(s['story'],32,600)+'</div>'
    foot=f'<div style="background:{SOFT};border-radius:24px;padding:16px 32px;display:flex;flex-direction:column;gap:6px;flex:3;box-sizing:border-box"><p style="font-size:24px;font-weight:800;color:{TEAL}">Try it (optional, no pressure)</p>'+p(s['tryit'],30,700)+'</div>'
    if s['legend']:
        k,v=s['legend'].split(': ',1); v=v[0].upper()+v[1:]
        foot+=f'<div style="background:{SKY};border-radius:24px;padding:16px 26px;display:flex;flex-direction:column;gap:4px;flex:2;box-sizing:border-box"><p style="font-size:22px;font-weight:800">{E(k)}</p><p style="font-size:21px;font-weight:600;line-height:1.3">{E(v)}</p></div>'
    inner+=f'<div style="display:flex;gap:24px;align-items:stretch">{foot}</div>'
    body+=pin(128,208,1664,inner,None,None,0,'0','gap:16px;box-sizing:border-box')
    notes=(f"Story break (optional, about 2 minutes, during the brain break). Skippable: if the lesson is running late or the group is tired, click straight on to the next slide; nothing later depends on it. "
      f"Read the story aloud, or ask a volunteer to read it (never pick a child). Who: {s['who']}. Link to today: {s['link']} "
      f"The Try it is optional and nobody is marked: children can think quietly, tell a partner, or pass. Never ask a child to answer in front of the group. "
      f"Answer for the tutor: {s['answer']} "
      +(f"{s['legend']} " if s['legend'] else '')
      +"Keep the tone as a story, not a quiz. Do not describe anyone as clever or gifted compared with other children.")
    return sec(f'{L}-story','OPTIONAL  •  2 MIN',body,notes)

def apply(n):
    L=f'p6l{n}'; D=os.path.join(H,'..','split',L,'project'); s=ST[str(n)]
    open(os.path.join(D,'slides',f'{L}-story.html'),'w').write(story_slide(L,s))
    dj=os.path.join(D,'deck.json'); d=json.load(open(dj,encoding='utf8'))
    o=[x for x in d['order'] if x!=f'{L}-story']; o.insert(o.index(f'{L}-break')+1,f'{L}-story'); d['order']=o
    json.dump(d,open(dj,'w'),indent=1,ensure_ascii=False)
    print(len(o),'slides (with story slide)')
