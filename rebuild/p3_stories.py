"""P3 mathematician stories: called by rebuild/gen_p3lK.py right after p3_gifted.add. Data: p3/stories.json.
Adds one optional 'Story break: <name>' slide straight after the brain-break slide (before the worksheet)."""
import json,os,sys
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,H)
import slidekit
from slidekit import *
ST=json.load(open(os.path.join(H,'..','p3','stories.json'),encoding='utf8'))
def add(S,order,ln):
    s=ST[str(ln)]; pre=order[0][:-len('title')]; sid=pre+'story'
    body=h2('Story break: '+s['name'])
    body+=p(f"{E(s['country'])}  •  {E(s['years'])}",34,700,MUTED,raw=True)
    body+=card(p(s["story"],34,500)+'',WHITE,'padding:28px 40px;')
    body+=card(f'<p style="align-self:flex-start;background:{YEL};color:{NAVY};border-radius:999px;padding:6px 22px;font-size:28px;font-weight:700">TRY IT (OPTIONAL)</p>'+p(s["try_it"],32,600),SOFT,'padding:22px 40px;')
    notes=('STORY BREAK (optional, 2 minutes). Skip this slide if you are short of time: click on to the worksheet, nothing else depends on it. '
           'Read the story aloud (about 1 minute), then give the optional question about 1 minute; anyone may pass, nobody is asked to answer by name and nothing is marked. '
           f"Who: {s['who']} Link to today: {s['link']} "
           f"ANSWER to the try-it (tutor only, do not show): {s['answer']}")
    if s['note']: notes+=f" TUTOR NOTE (accuracy): {s['note']}"
    S[sid]=sec(sid,'STORY BREAK  •  2 MIN',body,notes)
    b=pre+'break'; assert b in S and b in order,ln
    S[b]=S[b].replace('</aside>',' After the movement, the optional Story break slide follows (2 minutes, skip it if you are short of time).</aside>',1)
    order=list(order); order.insert(order.index(b)+1,sid); return order
