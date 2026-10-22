"""The Think harder (A1 to A4) and Go further (B1 to B3) items exactly as printed in the Level 5 workbook, for the deck generators.
Content lives in p5/content/lK.js (qbank.stretch[0:4] and qbank.challenge[-3:]); an item may carry a figure (SVG string) in .fig."""
import json,os,subprocess
H=os.path.dirname(os.path.abspath(__file__))
_cache={}
def items(n):
    if n not in _cache:
        js=("const c=require('"+os.path.join(H,'..','p5','content','l'+str(n)+'.js')+"');"
            "const f=x=>({q:x.q,a:x.a,fig:x.fig||null});"
            "console.log(JSON.stringify({th:c.qbank.stretch.slice(0,4).map(f),gf:c.qbank.challenge.slice(-3).map(f),pose:require('"+os.path.join(H,'..','p5','content','gaps.js')+"')["+str(n)+"].pose}))")
        _cache[n]=json.loads(subprocess.check_output(['node','-e',js]))
    return _cache[n]
def th_cards(n):   return [(f'A{i+1}.',x['q']) for i,x in enumerate(items(n)['th'])]
def gf_cards(n):   return [(f'B{i+1}.',x['q']) for i,x in enumerate(items(n)['gf'])]
def th_notes(n):   return 'These are the printed Think harder questions A1 to A4 (the same as the workbook). Answers: '+' '.join(f'A{i+1}) {x["a"]}' for i,x in enumerate(items(n)['th']))
def gf_notes(n):   return 'These are the printed Go further questions B1 to B3 (the same as the workbook). Answers: '+' '.join(f'B{i+1}) {x["a"]}' for i,x in enumerate(items(n)['gf']))+' Make up your own (printed under Go further): '+items(n)['pose']+' Think for 30 seconds before anyone speaks. Open-ended: check that a partner can solve it and that exactly one answer fits.'
def same_as_printed(n,texts):
    g=[x['q'] for x in items(n)['gf']]
    return all(t in g for t in texts)

# ---------------- slide builders (used by rebuild/gen_p5lK.py) ----------------
import re,sys
sys.path.insert(0,H)
from slidekit import *
def _fig(svg,w=560):
    m=re.search(r'viewBox="0 0 ([\d.]+) ([\d.]+)"',svg)
    vw,vh=(float(m.group(1)),float(m.group(2))) if m else (600,200)
    h=min(190,w*vh/vw); w2=h*vw/vh if h<w*vh/vw else w
    s=re.sub(r'style="width:[\d.]+px;max-width:100%"',f'style="width:{w2:.0f}px;max-width:100%"',svg,count=1)
    return f'<div style="text-align:center">{s}</div>',h
def _est(it,lab):
    if it.get('fig'):
        lines=-(-len(it['q'])//58); return 64+max(46*lines,_fig(it['fig'],440)[1])+28
    lines=-(-len(it['q'])//88); return 64+46*lines+28
def _groups(its,limit=690):
    gs=[];cur=[];h=0
    for k,it in enumerate(its):
        e=_est(it,k)
        if cur and h+e>limit: gs.append(cur);cur=[];h=0
        cur.append((k,it));h+=e
    gs.append(cur);return gs
def slides(n,kind):
    """kind 'A' = printed Think harder A1-A4, 'B' = printed Go further B1-B3. Returns {suffix: html}."""
    key='th' if kind=='A' else 'gf'; its=items(n)[key]
    head='Think harder' if kind=='A' else 'Go further'; base='stretch' if kind=='A' else 'gofurther'
    notes=th_notes(n) if kind=='A' else gf_notes(n)
    out={}
    gs=_groups(its,690 if kind=='A' else 560)
    for gi,g in enumerate(gs):
        suf=base if gi==0 else f'{base}{gi+1}'
        body=h2(head+(' (continued)' if gi else ''))
        for k,it in g:
            inner=p(f'<span style="color:{TEAL}">{kind}{k+1}.</span>  {E(it["q"])}',34,600,raw=True)
            if it.get('fig'):
                body+=card('<div style="display:flex;gap:36px;align-items:center"><div style="flex:1;min-width:0">'+inner+'</div><div style="flex:none;width:440px">'+_fig(it['fig'],440)[0]+'</div></div>')
            else: body+=card(inner)
        if kind=='B' and gi==len(gs)-1 and items(n)['pose']:
            body+=f'<div style="background:{SOFT};border-radius:24px;padding:20px 40px"><p style="font-size:30px;font-weight:700;line-height:1.3"><span style="color:{TEAL};font-weight:800">Make up your own.</span> {E(items(n)["pose"])} <i>Think for 30 seconds before anyone speaks.</i></p></div>'
        out[suf]=sec(f'p5l{n}-{suf}','37–72 MIN  •  OPTION',body,notes)
    return out
def fix_order(order,n,S):
    """Insert the extra printed-item slides after their parent slide, and drop the old extras slide if it was emptied."""
    pre=f'p5l{n}-'; o=[]
    for x in order:
        if x==pre+'challenge' and x not in S: continue
        if x==pre+'stretch':
            o.append(x); o+= [pre+k for k in ('stretch2','stretch3') if pre+k in S]; continue
        if x==pre+'challenge' or (x==pre+'chdiag' and pre+'challenge' not in S and pre+'gofurther' not in o):
            pass
        o.append(x)
    # printed Go further goes immediately before the extras (or before the see-it slide when there are no extras)
    res=[]
    for x in o:
        if x in (pre+'challenge',) or (x==pre+'chdiag' and pre+'challenge' not in S):
            res+=[pre+k for k in ('gofurther','gofurther2','gofurther3') if pre+k in S and pre+k not in res]
        res.append(x)
    return res
