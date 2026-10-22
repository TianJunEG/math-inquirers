"""P5 feature slides for the decks (fix pass): adds the 'Sneak-peek puzzles' slide (after the title) and the 'Exit slip and reflection'
slide (last), adds the Go further what-if to the explore slide, the neutral choice line to the page 1 slide, the pass / volunteers
rules to the talk slide, and re-times every slide to the ONE timeline used by the deck, script, guide and workbook:

  0-3 sneak-peek puzzles | 3-9 warm-up | 9-21 explore | 21-33 teaching | 33-37 break | 37-49 page 1 | 49-53 check page 1 |
  53-58 short teaching before page 2 | 58-72 page 2 | 72-76 check page 2 | 76-82 talk time | 82-86 exit ticket | 86-88 reflection | 88-90 stamp

Run after a gen_p5lK.py has written split/p5lK/project:  p5_gaps.apply(K)   (idempotent). Content comes from p5/content/gaps.js via p5/data.js."""
import json,os,re,subprocess,sys
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,H)
import slidekit
from slidekit import *
slidekit.FOOT='Math Inquirers P5 Holiday Program  •  Notice it. Test it. Explain why.'
ROOT=os.path.join(H,'..')
RED='#D64545'

def _story(n):
    js=f"const L=require('./p5/data.js');console.log(JSON.stringify(L.content[{n}-1].story))"
    return json.loads(subprocess.check_output(['node','-e',js],cwd=ROOT))

def story_slide_html(n,st):
    """Story break slide (optional, 2 minutes, skippable) placed right after the brain break slide, before the worksheet."""
    sub=f"{st['yshort']}   •   {st['cshort']}"+(f"   •   also spelled {st['also'].replace('also spelled ','')}" if st['also'] else '')
    body=h2('Story break: '+st['short'])+p(sub+'   •   '+st['who'],30,600,MUTED)
    left=(f'<div style="box-sizing:border-box;width:1110px;flex:none;background:{WHITE};border-radius:24px;padding:30px 40px;display:flex;flex-direction:column;gap:14px">'
          f'<p style="font-size:33px;font-weight:600;line-height:1.36">{E(st["story"])}</p>'
          +(f'<p style="font-size:26px;font-weight:700;line-height:1.3;color:{TEAL}">Good to know: {E(st["legend"])}</p>' if st['legend'] else '')+'</div>')
    right=(f'<div style="box-sizing:border-box;width:522px;flex:none;background:{SOFT};border-radius:24px;padding:28px 34px;display:flex;flex-direction:column;gap:12px">'
           f'<p style="font-size:26px;font-weight:800;letter-spacing:2px;color:{TEAL}">TRY IT  (OPTIONAL)</p>'
           f'<p style="font-size:30px;font-weight:600;line-height:1.3">{E(st["q"])}</p>'
           f'<p style="font-size:26px;font-weight:700;color:{MUTED}">Have a go, or just listen. Pass is always fine.</p></div>')
    body+=f'<div style="display:flex;gap:32px;align-items:flex-start">{left}{right}</div>'
    notes=('STORY BREAK, optional and skippable, about 2 minutes, inside the brain break (minutes 33 to 37). Do the stretch and drink first. '
      'SKIP IT if you are short of time or the group needs the full break: say "we will skip the story today" and click on to the worksheet at minute 37; nothing else depends on it. '
      f'1) Say: "Meet a mathematician: {st["short"]}." Read the story aloud slowly (about one minute), or let a volunteer read it. Do not add dialogue, feelings or scenes that are not in the story. '
      +(f'LABEL (keep it in your voice): {st["legend"]} ' if st['legend'] else '')
      +f'2) Link to today: {st["link"]} '
      '3) The Try it is an OPTIONAL question: "Have a go in your head or on paper, or just listen. Pass is always fine." Give about 30 seconds. Volunteers only; no cold-calling, nobody is marked, no tally. '
      f'ANSWER (for you; show it only after children have had a go): {st["a"]} '
      f'Confidence in the facts: {st["confidence"]}. Researched sources are listed in docs/stories/final_p5.json. Then: "Back to our seats, workbook out." (The same story is a small box on the Investigation page of the workbook, with no answer.)')
    return sec(f'p5l{n}-story','33–37 MIN  •  OPTION',body,notes)

def _data(n):
    js=(f"const L=require('./p5/data.js');const c=L.content[{n}-1];console.log(JSON.stringify({{check:c.deck.check,whatIf:c.deck.whatIf,pic:c.deck.checkPic,sc:c.script.check,sr:c.script.reflect,tr:c.script.talkRules,solo:c.lesson.solo,stuck:L.stuckTick({n}),ca:L.choiceAfter({n})}}))")
    return json.loads(subprocess.check_output(['node','-e',js],cwd=ROOT))

# ---------- small drawn pictures for the sneak-peek slide (drawn shapes, no unicode glyphs) ----------
def pic_bar3():
    s='<svg aria-label="An empty bar cut into 3 equal parts, for Mei\'s money" viewBox="0 0 960 80" xmlns="http://www.w3.org/2000/svg" style="width:960px;height:80px;flex:none">'
    s+=f'<text x="0" y="52" font-size="28" font-weight="700" fill="{NAVY}" font-family="Nunito Sans, Arial">Mei&#8217;s money</text>'
    for i in range(3):
        s+=f'<rect x="{220+i*240}" y="14" width="240" height="52" fill="#FFFFFF" stroke="{NAVY}" stroke-width="4"/>'
    return s+'</svg>'
def pic_hund():
    s='<svg aria-label="A square of 100 small squares, 10 rows of 10" viewBox="0 0 130 130" xmlns="http://www.w3.org/2000/svg" style="width:130px;height:130px;flex:none">'
    for r in range(10):
        for c in range(10):
            s+=f'<rect x="{5+c*12}" y="{5+r*12}" width="12" height="12" fill="#FFFFFF" stroke="{NAVY}" stroke-width="1.5"/>'
    return s+f'<rect x="5" y="5" width="120" height="120" fill="none" stroke="{NAVY}" stroke-width="3"/></svg>'
def pic_tri():
    s='<svg aria-label="Rows of sticks making 1 triangle, 2 triangles and 3 triangles" viewBox="0 0 1000 100" xmlns="http://www.w3.org/2000/svg" style="width:1000px;height:100px;flex:none">'
    x0=10
    for k in (1,2,3):
        w=70; h=70; pts=[]
        for i in range(k+2): pts.append((x0+i*w/2, 85 if i%2==0 else 15))
        for i in range(len(pts)-1): s+=f'<line x1="{pts[i][0]}" y1="{pts[i][1]}" x2="{pts[i+1][0]}" y2="{pts[i+1][1]}" stroke="{NAVY}" stroke-width="6" stroke-linecap="round"/>'
        for i in range(len(pts)-2): s+=f'<line x1="{pts[i][0]}" y1="{pts[i][1]}" x2="{pts[i+2][0]}" y2="{pts[i+2][1]}" stroke="{NAVY}" stroke-width="6" stroke-linecap="round"/>'
        s+=f'<text x="{x0+(k+1)*w/4-10}" y="100" font-size="24" font-weight="700" fill="{TEAL}" font-family="Nunito Sans, Arial">{k}</text>'
        x0+=(k+1)*w/2+110
    return s+'</svg>'
PICS={'bar3':pic_bar3,'hund':pic_hund,'tri':pic_tri}

def check_slide_html(n,rows,pic,notes):
    body=h2('Sneak-peek puzzles')+p('Ideas we have not learnt yet. Guessing is welcome. "I do not know" is welcome. Nobody is marked.',32,600,MUTED)
    top=300; pics={}
    if pic:
        pics[1 if pic in ('bar3',) else 0]=PICS[pic]()
    for i,r in enumerate(rows):
        q,a,short=r[0],r[1],(r[2] if len(r)>2 else r[1])
        lines=-(-len(q)//62); hq=lines*40+56+(100 if i in pics else 0)
        inner=f'<p style="font-size:30px;font-weight:600;line-height:1.3"><span style="color:{TEAL};font-weight:800">{i+1}.</span>  {E(q)}</p>'
        if i in pics: inner+=pics[i]
        body+=pin(128,top,1150,inner,None,WHITE,20,'16px 28px')
        body+=pin(1310,top,482,f'<p style="font-size:30px;font-weight:800;line-height:1.2">{E(short)}</p>','pop',YEL,20,'16px 22px')
        top+=hq+30
    body+=pin(128,max(top,780),1664,p('Show your answer only to your tutor: on your own paper, or all hold paper to the camera together. Then a volunteer can tell us how they thought.',28,700,MUTED),None,SOFT,20,'14px 26px')
    return sec(f'p5l{n}-check','0–3 MIN',body,notes)

def bx(): return '<span style="display:inline-block;width:28px;height:28px;border:4px solid #1B2A49;border-radius:7px;vertical-align:-5px;margin:0 10px 0 20px;background:#FFFFFF"></span>'
def reflect_slide_html(n,notes,stuck):
    t3=('<span style="font-size:28px;font-weight:600;line-height:1.6">'+bx()+'a picture or model'+bx()+'a list or table'+bx()+'a simpler number'+bx()+'my partner'
        +'<br>'+bx()+'I asked for help'+bx()+'checking my estimate'+bx()+E(stuck)+'</span>')
    items=[('1.','Something I did well ...',''),('2.','The hardest part was ...',''),('3.','What helped me ...',t3),('4.','Next time I will try ...','')]
    body=h2('Exit slip and reflection')+p('2 minutes. Use the box at the bottom of the Investigation page. Pass is always OK: write pass or tick a box.',30,600,MUTED)
    tops=[290,395,500,690]
    for (a,b,extra),t in zip(items,tops):
        body+=pin(128,t,1664,f'<p style="font-size:38px;font-weight:700"><span style="color:{TEAL};font-weight:800">{a}</span>  {E(b)}</p>'+extra,None,WHITE,20,'16px 28px')
    body+=pin(128,830,1664,p('Your tutor may read this to plan the next lesson. It is never marked or shown to the group.',28,700,MUTED),None,SOFT,20,'12px 26px')
    return sec(f'p5l{n}-reflect','86–88 MIN',body,notes)

# ---------- helpers on existing slide files ----------
LABEL=re.compile(r'(letter-spacing:2px;color:[^"]*">)([^<]*)(<)')
def rd(fp): return open(fp).read()
def wr(fp,s): open(fp,'w').write(s)
def get_label(s):
    m=LABEL.search(s); return m.group(2) if m else None
def set_label(s,new):
    return LABEL.sub(lambda m:m.group(1)+new+m.group(3),s,count=1)
def add_notes(s,txt):
    i=s.rindex('</aside>'); return s[:i]+' '+E(txt)+s[i:]
def append_card(s,html):
    # slides are flex columns; the footer <p> is the last child before <aside>
    k=s.index('<p style="position:absolute;left:128px;bottom:64px')
    return s[:k]+html+'\n'+s[k:]
def rng(label):
    m=re.match(r'(\d+)–(\d+) MIN',label or '')
    return (int(m.group(1)),int(m.group(2))) if m else None

def plan(n,ca):
    return ('Time plan: sneak-peek puzzles 0 to 3 (private answers, nobody is marked), warm-up 3 to 9, explore 9 to 21 (a Go further what-if is on the explore slide for anyone who wants more), '
      'teaching 21 to 33 (click to reveal each step and answer), brain break 33 to 37 (with an optional 2-minute Story break about a mathematician; skip it if you are short of time), workbook page 1 37 to 49 (after question %d you may choose: carry on, or try Think harder), '
      'check together 49 to 53, short teaching before page 2 53 to 58, workbook page 2 58 to 72 (alone: start with the questions named at the top, then choose; nobody has to finish; minutes 62 to 72 are protected open think time, 10 quiet minutes for Think harder, Go further or the Investigation, with no hints unless a child asks), '
      'check together 72 to 76, talk time 76 to 82 (you may say pass; volunteers first; then everyone tries the first step of the Investigation), exit ticket 82 to 86, '
      'reflection 86 to 88 (pass is always OK; includes "Next time I will try"), stamp and goodbye 88 to 90. Think harder, Go further and the Investigation are open to every child. The tutor never announces who is on which page, '
      'and never splits a pair unless both children agree. Invite the WHOLE group, never one child: "when you have finished Start here you can choose Think harder, Go further or the Investigation."') % ca

def apply(n):
    D=os.path.join(ROOT,'split',f'p5l{n}','project'); dj=os.path.join(D,'deck.json')
    d=json.load(open(dj)); sd=os.path.join(D,'slides'); g=_data(n)
    P=f'p5l{n}-'
    ans='; '.join(f'Q{i+1}: {a[1]}' for i,a in enumerate(g['check']))
    cn=('Minutes 0 to 3. SNEAK-PEEK PUZZLES. Show puzzle 1, give about a minute, click to show the short answer, then puzzle 2. '
        'Say it out loud: these are ideas we have not learnt yet; guessing is welcome; "I do not know" is welcome; nobody is marked. '
        'Puzzle 1 is an access puzzle: any child can try it with objects, drawing or counting, so everyone can start well. Puzzle 2 is a thinking puzzle. '
        'Answers are shown PRIVATELY (own paper shown only to you as you walk round; online, everyone holds paper to the camera at the same moment, or shows it to you only, on camera). Never boards in front of the group, never read out answers with names, no tally, no ranking. Never record scores. '
        f'Answers and what to listen for. {ans} '
        +' '.join(g['sc']))
    rn=('Minutes 86 to 88. EXIT SLIP AND REFLECTION, 2 minutes. Children use the small box at the bottom of the Investigation and reflection page: Something I did well; The hardest part was; What helped me (tick boxes include "I asked for help" and "'+g['stuck']+'"); Next time I will try. '
        'Pass is always OK. Never collected in public. '
        +' '.join(g['sr'][1:])+' At 88 stamp the inquiry journals and say goodbye.')
    wr(os.path.join(sd,P+'check.html'),check_slide_html(n,g['check'],g['pic'],cn))
    wr(os.path.join(sd,P+'reflect.html'),reflect_slide_html(n,rn,g['stuck']))
    o=[x for x in d['order'] if x not in (P+'check',P+'reflect')]
    o.insert(1,P+'check')
    if 'end' in o: o.insert(o.index('end'),P+'reflect')   # reflection (86-88) comes BEFORE the goodbye / certificates slide (88-90)
    else: o.append(P+'reflect')
    d['order']=o
    json.dump(d,open(dj,'w'),indent=1,ensure_ascii=False)

    # ---- warm-up slides sit at 3-6 and 6-9 (the sneak-peek puzzles take 0-3) ----
    def edit(sid,f):
        fp=os.path.join(sd,sid+'.html')
        if not os.path.exists(fp): return
        s=rd(fp); s2=f(s)
        if s2!=s: wr(fp,s2)
    edit(P+'warm1',lambda s:s.replace('>0–4 MIN<','>3–6 MIN<').replace('Minutes 0 to 4.','Minutes 3 to 6 (play only 1 or 2 rounds).').replace(' (play only 1 or 2 rounds to make room for the warm-up check)',' (play only 1 or 2 rounds)'))
    edit(P+'warm2',lambda s:s.replace('>4–9 MIN<','>6–9 MIN<').replace('Minutes 4 to 9.','Minutes 6 to 9.'))
    edit(P+'title',lambda s:re.sub(r'Time plan:.*?(?:or for home\.|Investigation\.(?:"|&quot;|&#34;|&#x22;)?)',lambda m:E(plan(n,g['ca'])+(' In this last lesson the 88 to 90 slot is certificates.' if n==10 else '')),s,count=1,flags=re.S))

    # ---- re-time every slide after the break ----
    order=d['order']
    def i_of(suffix):
        return order.index(P+suffix) if P+suffix in order else None
    iw1a=i_of('ws1ans'); iw2=i_of('ws2')
    newlab={}
    def lab(sid):
        return get_label(rd(os.path.join(sd,sid+'.html')))
    if iw1a is not None and iw2 is not None:
        newlab[order[iw1a]]=(49,53)
        mids=order[iw1a+1:iw2]
        durs=[]
        for sid in mids:
            r=rng(lab(sid))
            durs.append((r[1]-r[0]) if r else 2)
        tot=sum(durs)
        while tot>5:
            k=durs.index(max(durs)); durs[k]-=1; tot-=1
        t=53
        for sid,dd in zip(mids,durs):
            newlab[sid]=(t,t+dd); t+=dd
        while t<58 and mids:   # pad the last slide if the block was shorter than 5 minutes
            last=mids[-1]; newlab[last]=(newlab[last][0],newlab[last][1]+1); t+=1
        newlab[order[iw2]]=(58,72)
    for sfx,r in (('exit',(82,86)),):
        if P+sfx in order: newlab[P+sfx]=r
    for sid,(a,b) in newlab.items():
        fp=os.path.join(sd,sid+'.html'); s=rd(fp); old=get_label(s)
        s=set_label(s,f'{a}–{b} MIN')
        r0=rng(old)
        if r0:
            s=s.replace(f'Minutes {r0[0]} to {r0[1]}',f'Minutes {a} to {b}')
            s=s.replace(f'minutes {r0[0]} to {r0[1]}',f'minutes {a} to {b}')
        wr(fp,s)
    # optional slides (think harder / go further / investigation extras) get a label too
    for sfx in ('stretch','challenge','chdiag','chwalk'):
        edit(P+sfx,lambda s:set_label(s,'37–72 MIN  •  OPTION'))
    for sfx in ('teachchange','teachdeal'):
        edit(P+sfx,lambda s:set_label(s,'72–76 MIN  •  OPTION'))
    edit(P+'exit',lambda s:s.replace('Minutes 82 to 90.','Minutes 82 to 86.').replace('82 to 90','82 to 86'))

    # ---- page 1: the neutral choice line + whole-group invitation guidance ----
    def ws1(s):
        if 'you may choose: carry on' in s: return s
        s=append_card(s,card(p('After question %d you may choose: carry on, or try Think harder. You can swap at any time.'%g['ca'],34,700,TEAL)))
        return add_notes(s,'Everyone sees the same neutral line: "After question %d you may choose: carry on, or try Think harder." Never announce who is on which page and never name a child in front of the group. Invite the WHOLE group, never one child: "when you have finished Start here you can choose Think harder, Go further or the Investigation." Do not split a pair unless BOTH children agree. Think harder is the next pages after the Investigation page in the workbook.'%g['ca'])
    edit(P+'ws1',ws1)
    def ws2(s):
        s=s.replace('Finished early? Stretch and Challenge come next.','Want more? Think harder and Go further are at the back of your workbook.')
        if 'quiet think time' in s: return s
        s=append_card(s,card(p('Page 2: start with '+g['solo']+', then choose. You do not have to finish. Minutes 62 to 72 are quiet think time for Think harder, Go further or the Investigation.',32,700,TEAL)))
        return add_notes(s,'Page 2 is a menu, not a wall. Everyone sees the same line: start with '+g['solo']+', then choose. Nobody has to finish. OPEN THINK TIME, minutes 62 to 72 (10 minutes, protected): from minute 62 the room is quiet and any child who wants a longer problem works on Think harder, Go further or the Investigation without interruption. Give no hints unless a child asks, and do not call on anyone. Children who are still on Start here simply carry on. It is open to every child. Stop at minute 72 whatever has been done, because the check-together slide gives every answer with its explanation. Before minute 62, walk round, ask "what could you try first?", and give the first hint before any answer.')
    edit(P+'ws2',ws2)

    # ---- explore: the Go further what-if ----
    wi_q,wi_a=g['whatIf']
    def ex1(s):
        return add_notes(s,'GO FURTHER (say it at minute 9): any pair that finishes step 4 early may try the what-if question on the next slide. It is open to every pair, not a reward. Answer: '+wi_a)
    edit(P+'explore1',ex1)
    def ex2(s):
        if 'A SECOND WHAT-IF' in s: return s
        s=append_card(s,f'<div style="background:{SOFT};border-radius:24px;padding:26px 40px;display:flex;flex-direction:column;gap:10px"><p style="font-size:28px;font-weight:800;letter-spacing:2px;color:{TEAL}">GO FURTHER: A SECOND WHAT-IF (OPTIONAL, FOR ANY PAIR)</p><p style="font-size:34px;font-weight:700;line-height:1.3">{E(wi_q)}</p></div>')
        return add_notes(s,'GO FURTHER what-if (open to every pair from minute 9; nobody waits): '+wi_a)
    edit(P+'explore2',ex2)

    # ---- talk time: pass, volunteers first ----
    def talk(s):
        if 'You may say pass' in s: return s
        s=append_card(s,card(p('You may say "pass". Volunteers first. Then everyone tries the first step of the Investigation with a partner.',32,700,TEAL)))
        return add_notes(s,' '.join(g['tr'])+' Minutes 76 to 82: 2 minutes pairs talk, 2 minutes volunteers share, 2 minutes everyone tries the Easy first step of the Investigation (the page after workbook page 2). Pass is always allowed.')
    edit(P+'talk',talk)
    # ---- Story break (optional, skippable) right after the brain break, before the worksheet ----
    st=_story(n)
    wr(os.path.join(sd,P+'story.html'),story_slide_html(n,st))
    d=json.load(open(dj)); o=[x for x in d['order'] if x!=P+'story']
    o.insert(o.index(P+'break')+1,P+'story'); d['order']=o
    json.dump(d,open(dj,'w'),indent=1,ensure_ascii=False)
    def brk(s):
        if 'STORY BREAK FOLLOWS' in s: return s
        return add_notes(s,'STORY BREAK FOLLOWS (optional, 2 minutes, skippable): after the stretch and a drink, the next slide is a short true story about a mathematician with one optional question. Skip it if you are short of time.')
    edit(P+'break',brk)
    print('p5_gaps: lesson',n,len(o),'slides')

if __name__=='__main__':
    for k in sys.argv[1:]: apply(int(k))
