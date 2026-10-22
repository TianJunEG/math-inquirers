"""P5 feature slides for the decks (fix pass): adds the 'Sneak-peek puzzles' slide (after the title) and the 'Exit slip and reflection'
slide (last), adds the Go further what-if to the explore slide, the neutral choice line to the page 1 slide, the pass / volunteers
rules to the talk slide, and re-times every slide (time pill, leading 'Minutes a to b' of the notes, title-slide 'Time plan') from the
re-budget in rebuild/p5_budget.py (docs/audit/rebudget_p5.md). Slides with no clock time are labelled 'Optional, if you finish early'.

Run after a gen_p5lK.py has written split/p5lK/project:  p5_gaps.apply(K)   (idempotent). Content comes from p5/content/gaps.js via p5/data.js."""
import json,os,re,subprocess,sys
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,H)
import slidekit
from slidekit import *
import p5_budget as BUDG
slidekit.FOOT='Math Inquirers P5 Holiday Program  •  Notice it. Test it. Explain why.'
ROOT=os.path.join(H,'..')
RED='#D64545'

def _data(n):
    js=(f"const L=require('./p5/data.js');const c=L.content[{n}-1];console.log(JSON.stringify({{check:c.deck.check,whatIf:c.deck.whatIf,pic:c.deck.checkPic,sc:c.script.check,sr:c.script.reflect,tr:c.script.talkRules,solo:c.lesson.solo,p1:c.lesson.p1,take:c.lesson.take,cq:L.choiceQ({n})}}))")
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
def _svg(label,w,h,inner):
    return f'<svg aria-label="{label}" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="width:{w}px;height:{h}px;flex:none">{inner}</svg>'
def pic_cards():
    s=''
    for i,d in enumerate('3679'):
        x=10+i*84
        s+=f'<rect x="{x}" y="6" width="70" height="88" rx="10" fill="#FFFFFF" stroke="{NAVY}" stroke-width="4"/><text x="{x+35}" y="68" font-size="52" font-weight="800" text-anchor="middle" fill="{NAVY}" font-family="Nunito Sans, Arial">{d}</text>'
    return _svg('Four digit cards: 3, 6, 7 and 9',360,100,s)
def pic_bars2():
    s=''
    for r,(nm,n) in enumerate((('Ali',4),('Mei',2))):
        y=6+r*46
        s+=f'<text x="70" y="{y+30}" font-size="28" font-weight="700" text-anchor="end" fill="{NAVY}" font-family="Nunito Sans, Arial">{nm}</text>'
        for i in range(n): s+=f'<rect x="{84+i*90}" y="{y}" width="90" height="38" fill="{"#FFC93C" if r==0 else "#DDEBF7"}" stroke="{NAVY}" stroke-width="3"/><text x="{84+i*90+45}" y="{y+28}" font-size="24" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="Nunito Sans, Arial">10</text>'
    return _svg('Two bars: Ali has 40 cards (4 units of 10) and Mei has 20 cards (2 units of 10)',460,100,s)
def pic_grid64():
    s=''
    for r in range(4):
        for c in range(6): s+=f'<rect x="{10+c*24}" y="{4+r*24}" width="24" height="24" fill="#FFFFFF" stroke="{NAVY}" stroke-width="2"/>'
    s+=f'<rect x="10" y="4" width="144" height="96" fill="none" stroke="{NAVY}" stroke-width="4"/><line x1="10" y1="100" x2="154" y2="4" stroke="{TEAL}" stroke-width="4" stroke-dasharray="10 6"/>'
    return _svg('A rectangle 6 squares wide and 4 squares tall on squared paper with a diagonal from one corner to the opposite corner',170,104,s)
def pic_box432():
    sx=30; ox,oy=14,90
    def P(x,y,z): return (ox+x*sx+z*sx*0.433, oy-y*sx*0.62-z*sx*0.25)
    def poly(pts,fill): return '<polygon points="'+' '.join(f'{a:.1f},{b:.1f}' for a,b in (P(*q) for q in pts))+f'" fill="{fill}" stroke="{NAVY}" stroke-width="3" stroke-linejoin="round"/>'
    s=poly([(0,0,0),(4,0,0),(4,2,0),(0,2,0)],'#FFC93C')+poly([(0,2,0),(4,2,0),(4,2,3),(0,2,3)],'#FFE08A')+poly([(4,0,0),(4,0,3),(4,2,3),(4,2,0)],'#F2B92E')
    for i in range(1,4):
        a=P(i,0,0);b=P(i,2,0);s+=f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" stroke="{NAVY}" stroke-width="1.5"/>'
    a=P(0,1,0);b=P(4,1,0);s+=f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" stroke="{NAVY}" stroke-width="1.5"/>'
    s+=f'<text x="{P(2,0,0)[0]:.0f}" y="{P(2,0,0)[1]+22:.0f}" font-size="22" font-weight="700" text-anchor="middle" fill="{TEAL}" font-family="Nunito Sans, Arial">4 long</text><text x="{P(4,1,3)[0]+14:.0f}" y="{P(4,1,1.5)[1]+8:.0f}" font-size="22" font-weight="700" fill="{TEAL}" font-family="Nunito Sans, Arial">3 wide, 2 tall</text>'
    return _svg('A box 4 cubes long, 3 cubes wide and 2 cubes tall',350,124,s)
def pic_bar12():
    s=f'<text x="0" y="30" font-size="26" font-weight="700" fill="{NAVY}" font-family="Nunito Sans, Arial">12 litres in 4 minutes</text>'
    for i in range(4): s+=f'<rect x="{10+i*160}" y="44" width="160" height="46" fill="#FFFFFF" stroke="{NAVY}" stroke-width="4"/><text x="{10+i*160+80}" y="76" font-size="24" font-weight="700" text-anchor="middle" fill="{MUTED}" font-family="Nunito Sans, Arial">minute {i+1}</text>'
    return _svg('A bar for 12 litres cut into 4 empty equal parts, one for each minute',660,100,s)
def pic_rt30():
    s=f'<path d="M20 90 L20 10 M20 90 L110 90" stroke="{NAVY}" stroke-width="5" fill="none" stroke-linecap="round"/><path d="M20 90 L98 45" stroke="{TEAL}" stroke-width="5" stroke-linecap="round"/>'
    s+=f'<path d="M20 78 H32 V90" fill="none" stroke="{NAVY}" stroke-width="3"/><path d="M60 90 A40 40 0 0 0 55 70" fill="none" stroke="#D64545" stroke-width="4"/><text x="70" y="78" font-size="22" font-weight="800" fill="#D64545" font-family="Nunito Sans, Arial">30&#176;</text><text x="30" y="40" font-size="26" font-weight="800" fill="#D64545" font-family="Nunito Sans, Arial">?</text>'
    return _svg('A right angle with a line drawn from the corner that makes a 30 degree angle with one arm and leaves a question mark angle with the other',130,100,s)
def pic_logic3():
    s=''
    cols=('red','blue','green'); rows=('Ali','Mei','Ravi')
    for j,c in enumerate(cols): s+=f'<text x="{150+j*110+55}" y="22" font-size="24" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="Nunito Sans, Arial">{c}</text>'
    for i,r in enumerate(rows):
        s+=f'<text x="120" y="{54+i*28}" font-size="24" font-weight="700" text-anchor="end" fill="{NAVY}" font-family="Nunito Sans, Arial">{r}</text>'
        for j in range(3): s+=f'<rect x="{150+j*110}" y="{30+i*28}" width="110" height="28" fill="#FFFFFF" stroke="{NAVY}" stroke-width="3"/>'
    return _svg('An empty table with Ali, Mei and Ravi down the side and red, blue and green across the top',490,116,s)
PICS={'bar3':pic_bar3,'hund':pic_hund,'tri':pic_tri,'cards':pic_cards,'bars2':pic_bars2,'grid64':pic_grid64,'box432':pic_box432,'bar12':pic_bar12,'rt30':pic_rt30,'logic3':pic_logic3}
PICPOS={'bar3':1,'bars2':1}   # every other picture sits under puzzle 1 of the sneak-peek slide (index 0)

def check_slide_html(n,rows,pic,notes):
    body=h2('Sneak-peek puzzles')+p('Guessing is welcome. Nobody is marked.',32,600,MUTED)
    top=300; pics={}
    if pic:
        pics[PICPOS.get(pic,0)]=PICS[pic]()
    for i,r in enumerate(rows):
        q,a,short=r[0],r[1],(r[2] if len(r)>2 else r[1])
        lines=-(-len(q)//62); hq=lines*40+56+(120 if i in pics else 0)
        inner=f'<p style="font-size:30px;font-weight:600;line-height:1.3"><span style="color:{TEAL};font-weight:800">{i+1}.</span>  {E(q)}</p>'
        if i in pics: inner+=pics[i]
        body+=pin(128,top,1150,inner,None,WHITE,20,'16px 28px')
        body+=pin(1310,top,482,f'<p style="font-size:30px;font-weight:800;line-height:1.2">{E(short)}</p>','pop',YEL,20,'16px 22px')
        top+=hq+30
    body+=pin(128,max(top,780),1664,p('Show your paper ONCE, after both puzzles: only to your tutor, or all hold paper to the camera together.',28,700,MUTED),None,SOFT,20,'14px 26px')
    return sec(f'p5l{n}-check',BUDG.pill(n,'check'),body,notes)

def bx(): return '<span style="display:inline-block;width:28px;height:28px;border:4px solid #1B2A49;border-radius:7px;vertical-align:-5px;margin:0 10px 0 20px;background:#FFFFFF"></span>'
def reflect_slide_html(n,notes):
    t3=('<span style="font-size:28px;font-weight:600;line-height:1.6">'+bx()+'a picture or model'+bx()+'a list or table'+bx()+'a simpler number'+bx()+'my partner'
        +'<br>'+bx()+'I asked for help'+bx()+'checking my estimate'+bx()+'I am still stuck (my tutor will check in with me)</span>')
    items=[('1.','Something I did well ...',''),('2.','The hardest part was ...',''),('3.','What helped me ...',t3)]
    body=h2('Exit slip and reflection')+p('About a minute and a half. Use the box at the bottom of the Investigation page. Pass is always OK: write pass or tick a box.',30,600,MUTED)
    tops=[330,460,590]
    for (a,b,extra),t in zip(items,tops):
        body+=pin(128,t,1664,f'<p style="font-size:38px;font-weight:700"><span style="color:{TEAL};font-weight:800">{a}</span>  {E(b)}</p>'+extra,None,WHITE,20,'16px 28px')
    body+=pin(128,860,1664,p('Your tutor may read this privately to plan the next lesson. It is never marked or shown to the group.',28,700,MUTED),None,SOFT,20,'12px 26px')
    return sec(f'p5l{n}-reflect',BUDG.pill(n,'reflect'),body,notes)

# ---------- helpers on existing slide files ----------
def rd(fp): return open(fp,encoding='utf8').read()
def wr(fp,s): open(fp,'w',encoding='utf8').write(s)
def add_notes(s,txt):
    i=s.rindex('</aside>'); return s[:i]+' '+E(txt)+s[i:]
def append_card(s,html):
    # slides are flex columns; the footer <p> is the last child before <aside>
    k=s.index('<p style="position:absolute;left:128px;bottom:64px')
    return s[:k]+html+'\n'+s[k:]
def fm(x): return BUDG.fmt(x)

PILLRE=re.compile(r'(<p style="position:absolute;right:128px;top:64px;[^"]*">)([^<]*)(</p>)')
BREAKRE=re.compile(r'(letter-spacing:4px;[^>]*>)[^<]*MIN(</p>)')
LEAD=re.compile(r'^(?:Minutes? [\d.]+ (?:to|–) [\d.]+|Minute [\d.]+)(?: \([^)]*\))?[.:]?\s*')
OPTNOTE=BUDG.OPT_PILL+' (no clock time): show it only while some pairs are working or have finished, never as a group slide at a fixed minute. '
PAIRWORK={1:6,2:6,3:6,4:6.5,5:6,6:6,7:6,8:6.5,9:5.5,10:6}   # minutes of pair work in the explore (audit section 6: 6, 6.5 where pairs stay in the main room, 5.5 in lesson 9)

def plan_text(n,cq):
    P=lambda t:BUDG.part(n,t); f=fm
    g=lambda t:f"{f(P(t)[0])} to {f(P(t)[1])}"
    bu=P('Buffer'); ex=BUDG.BUD[n]['slides']
    last=('certificates and goodbye ' if n==10 else 'stamp typed in the chat and goodbye ')+f"{f(ex['end'][0] if n==10 else ex['reflect'][1])} to {f(ex['end'][1] if n==10 else ex['reflect'][1]+BUDG.CLOSE[n])}"
    t=(f"Time plan (the exact minutes of this lesson; every lesson adds up to 90): opening {g('Opening')}, sneak-peek puzzles {g('Sneak')} (one hold-up for both puzzles, no volunteer round, nobody is marked), "
       f"warm-up {g('Warm-up')} (one game round, four quick questions), explore {g('Explore')} (pair work {f(PAIRWORK[n])} minutes at most, then two questions together; a Go further what-if is on the explore slide for any pair that finishes), "
       f"teaching {g('Mini')} (click to reveal each step and answer), brain break {g('Brain')}, workbook page 1 {g('Worksheet page 1')} (the questions without a star; after question {cq} you may choose: carry on, or try Think harder), "
       f"check together {g('Check page 1')}, ")
    if P('Short teaching'): t+=f"short teaching before page 2 {g('Short teaching')}, "
    t+=(f"workbook page 2 {g('Worksheet page 2')} (alone: start with the questions named at the top, then choose; starred parts are take-home; nobody has to finish), check together {g('Check page 2')}, "
        f"talk time {g('Talk')} (you may say pass; volunteers first; the first step of the Investigation is take-home), exit ticket {f(ex['exit'][0])} to {f(ex['exit'][1])}, reflection {f(ex['reflect'][0])} to {f(ex['reflect'][1])} (pass is always OK), {last}, "
        f"and the buffer {f(bu[0])} to {f(bu[1])} (floating time: spend it first if you run late, never fill it on purpose). "
        "Think harder, Go further and the Investigation are open to every child and have no clock time. The tutor never announces who is on which page, "
        'and never splits a pair unless both children agree. Invite the WHOLE group, never one child: "when you have finished Start here you can choose Think harder, Go further or the Investigation."')
    return t

def retime(n):
    """Rewrite the time pill and the leading 'Minutes a to b' of every slide of lesson n from rebuild/p5_budget.py (idempotent)."""
    L=f'p5l{n}'; D=os.path.join(ROOT,'split',L,'project'); B=BUDG.BUD[n]; sd=os.path.join(D,'slides')
    for sid in json.load(open(os.path.join(D,'deck.json'),encoding='utf8'))['order']:
        k=sid.split('-',1)[1] if sid.startswith(L+'-') else sid
        pth=os.path.join(sd,sid+'.html'); s=rd(pth); o=s
        if k in B['slides']:
            a,b=B['slides'][k]
            if k=='break': s=BREAKRE.sub(lambda x:x.group(1)+BUDG.pill(n,k)+x.group(2),s,1)
            elif k not in ('title','end'): s=PILLRE.sub(lambda x:x.group(1)+BUDG.pill(n,k)+x.group(3),s,1)
            pre=f'Minutes {fm(a)} to {fm(b)}'
            if k=='title': pre+=' (opening, inside the 90-minute clock)'
            if k=='explore1':
                es,ee=BUDG.part(n,'Explore'); pre=f'Minutes {fm(es)} to {fm(ee)} (the whole explore; this slide {fm(a)} to {fm(b)})'
            pre+='. '
        elif k in B['optional']:
            s=PILLRE.sub(lambda x:x.group(1)+BUDG.OPT_PILL+x.group(3),s,1); pre=OPTNOTE
        else:
            raise SystemExit(f'p5_gaps.retime: slide {sid} is neither in the clock plan nor optional (add it to rebuild/p5_budget.py)')
        m=re.search(r'<aside>(.*?)</aside>',s,re.S)
        if m:
            body=LEAD.sub('',m.group(1)); s=s.replace(m.group(0),'<aside>'+pre+body+'</aside>',1)
        if s!=o: wr(pth,s)

def apply(n):
    D=os.path.join(ROOT,'split',f'p5l{n}','project'); dj=os.path.join(D,'deck.json')
    d=json.load(open(dj,encoding='utf8')); sd=os.path.join(D,'slides'); g=_data(n); B=BUDG.BUD[n]
    P=f'p5l{n}-'
    for k in B['cut']:      # slides cut by the re-budget: never in the deck
        fp=os.path.join(sd,P+k+'.html')
        if os.path.exists(fp): os.remove(fp)
    ans='; '.join(f'Q{i+1}: {a[1]}' for i,a in enumerate(g['check']))
    cn=('SNEAK-PEEK PUZZLES. Show puzzle 1 and give about a minute; click to show the short answer later. Then show puzzle 2 and give about a minute. '
        'Open with one line only: "Guessing is welcome. Nobody is marked." Puzzle 1 is an access puzzle: any child can try it with objects, drawing or counting, so everyone can start well. Puzzle 2 is a thinking puzzle. '
        'ONE hold-up for both puzzles: after puzzle 2, everyone shows their paper at the same moment (own paper shown only to you as you walk round; online, all hold paper to the camera together, or show it to you only, on camera). '
        'Then click through the two short answers and say each with one short reason. NO volunteer round here (volunteers come in the talk time). Never boards in front of the group, never read out answers with names, no tally, no ranking. Never record scores. '
        f'Answers and what to listen for. {ans} '
        +' '.join(g['sc']))
    rn=('REFLECTION, about a minute and a half. Children use the small box at the bottom of the Investigation and reflection page: Something I did well; The hardest part was; What helped me (tick boxes include "I asked for help" and "I am still stuck (my tutor will check in with me)"). '
        'Pass is always OK. Never collected in public; you may read it privately later to plan the next lesson and check in with any child who ticked still stuck in the open session (a quick visit to the shared breakout room or a hand signal, parent nearby, never a private message). Never read a child\'s reflection aloud. '
        +' '.join(g['sr'][1:])+(' Then the certificates (see the next slide).' if n==10 else ' Then type the stamp in the chat for every child (one message) and say goodbye. If the clock is behind, the reflection becomes a one-tick version: pass or one box.'))
    wr(os.path.join(sd,P+'check.html'),check_slide_html(n,g['check'],g['pic'],cn))
    wr(os.path.join(sd,P+'reflect.html'),reflect_slide_html(n,rn))
    o=[x for x in d['order'] if x not in (P+'check',P+'reflect') and x[len(P):] not in B['cut']]
    o.insert(1,P+'check')
    if 'end' in o: o.insert(o.index('end'),P+'reflect')      # lesson 10: the certificates slide comes after the reflection
    else: o.append(P+'reflect')
    d['order']=o
    json.dump(d,open(dj,'w'),indent=1,ensure_ascii=False)

    def edit(sid,f):
        fp=os.path.join(sd,sid+'.html')
        if not os.path.exists(fp): return
        s=rd(fp); s2=f(s)
        if s2!=s: wr(fp,s2)
    cq=g['cq']
    edit(P+'title',lambda s:re.sub(r'Time plan:.*?(?:or for home\.|Investigation\.(?:"|&quot;|&#34;|&#x22;)?)',lambda m:E(plan_text(n,cq)+(' In this last lesson the closing slot is certificates (12 seconds each).' if n==10 else '')),s,count=1,flags=re.S))

    # ---- page 1: the neutral choice line + private-invitation guidance + what is in class today ----
    def ws1(s):
        if 'you may choose: carry on' in s: return s
        s=append_card(s,card(p(f'After question {cq} you may choose: carry on, or try Think harder. You can swap at any time.',34,700,TEAL)))
        return add_notes(s,f'Everyone sees the same neutral line: "After question {cq} you may choose: carry on, or try Think harder." (Question {cq} is the last question to do in class on page 1 of this lesson.) Never announce who is on which page and never name a child in front of the group. Invite the WHOLE group, never one child: "when you have finished Start here you can choose Think harder, Go further or the Investigation." Do not split a pair unless BOTH children agree. Think harder is the next pages after the Investigation page in the workbook. '
                         f'IN CLASS NOW: {g["p1"]}. Parts marked with a star in the workbook are take-home: say so once ("the starred parts are for home") and do not wait for them.')
    edit(P+'ws1',ws1)
    e2=B['slides']['ws2']
    def ws2(s):
        s=s.replace('Finished early? Stretch and Challenge come next.','Want more? Think harder and Go further are at the back of your workbook.')
        if 'Page 2 plan' in s: return s
        s=append_card(s,card(p('Page 2 plan: start with '+g['solo']+'. Then choose what to try next. You do not have to finish the page.',32,700,TEAL)))
        return add_notes(s,'Page 2 is a menu, not a wall. Everyone sees the same line: start with '+g['solo']+', then choose. Nobody has to finish; stop at minute '+fm(e2[1])+' whatever has been done, because the check-together slide gives every answer with its explanation. '
                         'Starred parts are take-home (their answers are on the check slide for you; do not spend class time on them). Walk round, ask "what could you try first?", and give the first hint before any answer.')
    edit(P+'ws2',ws2)

    # ---- explore: the Go further what-if; pair work is capped; two questions together ----
    wi_q,wi_a=g['whatIf']
    es,ee=B['slides']['explore1'][0],B['slides']['explore2'][0]
    def ex1(s):
        return add_notes(s,f'PROTECTED THINK TIME: before the pairs touch anything, say "Think for 30 seconds before anyone speaks" and show the clock; then pairs talk and start. PAIR WORK IS CAPPED AT {fm(PAIRWORK[n])} MINUTES: say "Pencils down" at minute {fm(ee)} and bring the group back (the minutes before that include the 30 seconds of thinking, finding materials and, in lessons that use them, the move to and from breakout rooms). '
                         'GO FURTHER (say it as soon as a pair has finished the task): any pair that finishes early may try the what-if question on the next slide. It is open to every pair, not a reward. Answer: '+wi_a)
    edit(P+'explore1',ex1)
    def ex2(s):
        if 'A SECOND WHAT-IF' in s: return s
        s=append_card(s,f'<div style="background:{SOFT};border-radius:24px;padding:26px 40px;display:flex;flex-direction:column;gap:10px"><p style="font-size:28px;font-weight:800;letter-spacing:2px;color:{TEAL}">GO FURTHER: A SECOND WHAT-IF (OPTIONAL, IF YOU FINISH EARLY)</p><p style="font-size:34px;font-weight:700;line-height:1.3">{E(wi_q)}</p></div>')
        return add_notes(s,'TWO questions together only (about a minute each), then move on. GO FURTHER what-if (open to every pair as soon as it has finished; nobody waits): '+wi_a)
    edit(P+'explore2',ex2)

    # ---- talk time: pass, volunteers first; the Investigation first step is take-home ----
    def talk(s):
        if 'You may say pass' in s: return s
        s=append_card(s,card(p('You may say "pass". Volunteers first. Take-home: try the first step of the Investigation (the page after workbook page 2).',32,700,TEAL)))
        return add_notes(s,' '.join(g['tr'])+' Talk time: 30 seconds of silent thinking, 2 minutes pairs talk, 1 and a half minutes volunteers share, then tell everyone that the first step of the Investigation (the page after workbook page 2) is take-home, or the opener of the next lesson. Pass is always allowed.')
    edit(P+'talk',talk)
    retime(n)
    BUDG.write_json()
    print('p5_gaps: lesson',n,len(o),'slides')

if __name__=='__main__':
    for k in sys.argv[1:]: apply(int(k))
