"""P5 gap closers for the decks: adds a 'Warm-up check' slide (after the title) and a 'What was hard?' slide (last).
Run after a gen_p5lK.py has written split/p5lK/project:  p5_gaps.apply(K)   (idempotent). Content comes from p5/content/gaps.js via p5/data.js."""
import json,os,re,subprocess,sys
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,H)
import slidekit
from slidekit import *
slidekit.FOOT='Math Inquirers P5 Holiday Program  •  Notice it. Test it. Explain why.'
ROOT=os.path.join(H,'..')
def _data(n):
    out=subprocess.check_output(['node','-e',f"const L=require('./p5/data.js');const c=L.content[{n}-1];console.log(JSON.stringify({{check:c.deck.check,sc:c.script.check,sr:c.script.reflect}}))"],cwd=ROOT)
    return json.loads(out)
def short(a):
    parts=re.split(r'(?<=[.!?])\s+',a)
    s=parts[0]
    if len(s)<30 and len(parts)>1: s+=' '+parts[1]
    return s if len(s)<=120 else s[:117].rsplit(' ',1)[0]+' ...'
def box(): return '<span style="display:inline-block;width:30px;height:30px;border:4px solid #1B2A49;border-radius:7px;vertical-align:-5px;margin:0 10px 0 22px;background:#FFFFFF"></span>'
def check_slide_html(n,rows,notes):
    body=h2('Warm-up check: 3 minutes')+p('Whiteboards. Answer both, then be ready to say WHY.',34,600,MUTED)
    tops=[330,590]
    for i,(q,a) in enumerate(rows):
        t=tops[i]
        body+=pin(128,t,1100,f'<p style="font-size:32px;font-weight:600;line-height:1.25"><span style="color:{TEAL};font-weight:800">{i+1}.</span>  {E(q)}</p>',None,WHITE,20,'16px 26px')
        body+=pin(1290,t,502,f'<p style="font-size:30px;font-weight:800;line-height:1.2">{E(short(a))}</p>','pop',YEL,20,'16px 22px')
    body+=pin(128,830,1664,p('Everyone does the check. Then some of us start on page 1 and some start on the Think Harder pages. Both are good choices, and you can swap.',30,700,MUTED),None,SOFT,20,'14px 26px')
    return sec(f'p5l{n}-check','0–3 MIN',body,notes)
def reflect_slide_html(n,notes):
    items=[('1.','The hardest part was ...',''),
           ('2.','I got unstuck by ...','<span style="font-size:30px;font-weight:600;line-height:1.5">'+box()+'a picture or model'+box()+'a list or table'+box()+'a simpler number<br>'+box()+'asking my partner'+box()+'checking my estimate'+box()+'something else</span>'),
           ('3.','Next time I will try ...','')]
    body=h2('What was hard?')+p('One minute. Fill in your workbook. Nobody marks this.',34,600,MUTED)
    tops=[330,490,720]
    for (a,b,extra),t in zip(items,tops):
        body+=pin(128,t,1664,f'<p style="font-size:40px;font-weight:700"><span style="color:{TEAL};font-weight:800">{a}</span>  {E(b)}</p>'+extra,None,WHITE,20,'18px 28px')
    return sec(f'p5l{n}-reflect','LAST MINUTE',body,notes)
def apply(n):
    D=os.path.join(ROOT,'split',f'p5l{n}','project'); dj=os.path.join(D,'deck.json')
    d=json.load(open(dj)); sd=os.path.join(D,'slides'); g=_data(n)
    P=f'p5l{n}-'
    ans='; '.join(f'Q{i+1}: {a}' for i,(q,a) in enumerate(g['check']))
    cn=('Minutes 0 to 3. WARM-UP CHECK (pre-check). Show the two questions; children answer on whiteboards and hold them up; ask one child per question "How do you know?" and then click to show the short answer. '
        f'Answers and what to listen for: {ans} '
        'Fast track: a child who gets BOTH right and can explain why is invited to start on the Think Harder pages and the Open Investigation while the group works page 1 (online: send the page numbers in the chat or use a breakout room; they come back for talk time). Say it to the whole group as a choice of starting place; nobody is labelled and any child can swap. Never record scores. '
        +' '.join(g['sc']))
    rn=('Last minute, after the exit ticket. WHAT WAS HARD? Children complete the three prompts on the last workbook page: the hardest part, how they got unstuck (tick a strategy) and what they will try next time. One minute only; invite one or two children to read theirs aloud. Never grade it. Praise strategy, not speed. '
        +' '.join(g['sr']))
    open(os.path.join(sd,P+'check.html'),'w').write(check_slide_html(n,g['check'],cn))
    open(os.path.join(sd,P+'reflect.html'),'w').write(reflect_slide_html(n,rn))
    o=[x for x in d['order'] if x not in (P+'check',P+'reflect')]
    o.insert(1,P+'check'); o.append(P+'reflect'); d['order']=o
    # re-time the warm-up slides to make room for the check
    def edit(sid,f):
        fp=os.path.join(sd,sid+'.html'); s=open(fp).read(); s2=f(s)
        if s2!=s: open(fp,'w').write(s2)
    edit(P+'warm1',lambda s:s.replace('>0–4 MIN<','>3–6 MIN<').replace('Minutes 0 to 4.','Minutes 3 to 6 (play only 1 or 2 rounds to make room for the warm-up check).'))
    edit(P+'warm2',lambda s:s.replace('>4–9 MIN<','>6–9 MIN<').replace('Minutes 4 to 9.','Minutes 6 to 9.'))
    edit(P+'title',lambda s:s.replace('warm-up 0 to 9','warm-up check 0 to 3, warm-up game and quick questions 3 to 9') if 'warm-up check 0 to 3' not in s else s)
    json.dump(d,open(dj,'w'),indent=1,ensure_ascii=False)
    print('p5_gaps: lesson',n,len(o),'slides')
if __name__=='__main__':
    for k in sys.argv[1:]: apply(int(k))
