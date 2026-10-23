"""Mi the dolphin on the HOLIDAY lesson decks (owner: yes, 23 Oct 2026; see docs/terms/owner_decisions.md).
Idempotent post-pass, called from levels/restyle.py (so it survives a gen_* rebuild + restyle), or run directly:
    python3 levels/mi_deco.py split/p2l3 [...]
Slides that get Mi (one small pose pinned in the bottom-right corner, never on a question slide):
  title      hello_wave (lesson 10 = Challenge/Puzzle Day opening: map)
  break      stretch (brain break)
  end        trophy (lesson 10 certificates slide, if it is not the last slide)
  last slide goodbye_wave (look-back / end)
No speech bubbles, no numbers, no calculator. Image src is /_blob/<id> (Claude Slides asset store); the ids differ per
deck and live in mascot/blob_ids.json {deckkey: {pose: "/_blob/<id>"}} (written by the republish step)."""
import sys,os,re,json
HERE=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.join(HERE,'..')
MAP=os.path.join(ROOT,'mascot','blob_ids.json')
LEVELS_ON={'1','2','3','4','5','6'}                       # all six levels (Levels 4-6 added 23 Oct, smaller and more subtle)
H={'1':230,'2':230,'3':230,'4':170,'5':160,'6':150}   # image height px; older levels smaller and more subtle
OP={'1':1,'2':1,'3':1,'4':0.92,'5':0.88,'6':0.85}
ASPECT={'hello_wave':699/834,'stretch':389/834,'goodbye_wave':644/834,'map':806/834,'trophy':842/834,'cheer':571/834}
ALT={'hello_wave':'Mi the dolphin waving hello','stretch':'Mi the dolphin stretching','goodbye_wave':'Mi the dolphin waving goodbye',
     'map':'Mi the dolphin holding a map','trophy':'Mi the dolphin holding trophies','cheer':'Mi the dolphin cheering'}
def key_level(d):
    k=os.path.basename(d.rstrip('/')); m=re.match(r'p(\d)l(\d+)$',k)
    if m: return k,m.group(1),int(m.group(2))
    m=re.match(r'l(\d+)$',k); return (k,'1',int(m.group(1))) if m else (k,None,0)
def plan(order,ln):
    """slide id -> pose"""
    P={}
    t=[i for i in order if i.endswith('-title')]
    if t: P[t[0]]='map' if ln==10 else 'hello_wave'
    b=[i for i in order if i.endswith('-break')]
    if b: P[b[0]]='stretch'
    last=order[-1]
    if ln==10 and 'end' in [i.split('-')[-1] for i in order]:
        e=[i for i in order if i.split('-')[-1]=='end'][0]
        if e!=last: P[e]='trophy'
    P[last]='goodbye_wave'
    return P
IMG=re.compile(r'<img data-mi="[^>]*>\n?')
def put(html,pose,lv,url,sid=''):
    html=IMG.sub('',html)
    h=H[lv]
    if sid.endswith('reflect'): h=120   # look-back cards/rows run to the bottom-right corner: small Mi keeps clear of the text (all levels)
    if sid.endswith('reflect') and lv in '456':   # L5 yellow 'tutor may read this' notice reached x=1844: narrow it so Mi (x>=1783) never touches it
        html=html.replace('top:860px;width:1664px;background:#FFF0C2','top:860px;width:1520px;background:#FFF0C2')
    if sid.endswith('-title'):   # keep the 'Today we will' card clear of Mi (L1-3 Mi is wider than L4-6)
        mr=150 if lv in '456' else 250
        html=re.sub(r'background:#26385F;(?:margin-right:\d+px;)?border-radius:24px;',f'background:#26385F;margin-right:{mr}px;border-radius:24px;',html,count=1)
    w=round(h*ASPECT[pose])
    op='' if OP[lv]==1 else f';opacity:{OP[lv]}'
    tag=(f'<img data-mi="{pose}" src="{url}" alt="{ALT[pose]}" style="position:absolute;right:44px;bottom:{18 if h<150 else 30}px;'
         f'width:{w}px;height:{h}px;object-fit:contain{op}">\n')
    i=html.rfind('<aside')
    if i<0: i=html.rfind('</section>')
    return html[:i]+tag+html[i:]
def apply(d):
    k,lv,ln=key_level(d)
    if lv not in LEVELS_ON: return 0
    deck=json.load(open(os.path.join(d,'project','deck.json'))); order=deck['order']
    try: bm=json.load(open(MAP)).get(k,{})
    except Exception: bm={}
    n=0
    for sid,pose in plan(order,ln).items():
        f=os.path.join(d,'project','slides',sid+'.html')
        if not os.path.exists(f): continue
        url=bm.get(pose) or (f'/_blob/PENDING-{pose}' if os.environ.get('MI_PREVIEW') else None)
        a=open(f).read(); b=put(a,pose,lv,url,sid) if url else IMG.sub('',a)   # no uploaded asset for this deck yet: no Mi (never a broken image)
        if a!=b: open(f,'w').write(b); n+=1
    return n
if __name__=='__main__':
    for d in sys.argv[1:]: print(d,apply(d))
