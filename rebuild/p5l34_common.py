"""Shared helpers for the P5 Lesson 3 and 4 deck generators (new file; slidekit.py is not edited)."""
import json,os,sys,subprocess,datetime
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,H)
import slidekit
from slidekit import *
slidekit.FOOT='Math Inquirers P5 Holiday Program  •  Notice it. Test it. Explain why.'
FOOTX=slidekit.FOOT
RED='#D64545'
def load(n):
    js=("const c=require('"+os.path.join(H,'..','p5','content','l'+str(n)+'.js')+"');console.log(JSON.stringify({lesson:c.lesson,deck:c.deck}))")
    return json.loads(subprocess.check_output(['node','-e',js]))
def title_slide(sid,label,title,topic,today,notes):
    return (f'<section id="{sid}" data-transition="fade" style="background:{NAVY};color:{CREAM};font-family:{BF};padding:128px 128px 160px;display:flex;flex-direction:column;justify-content:center;gap:36px">\n'
            f'<p style="font-size:32px;font-weight:700;letter-spacing:4px;color:{YEL}">{E(label)}</p>\n'
            f'<h1 style="font-family:{HF};font-size:128px;font-weight:600;line-height:1.05">{E(title)}</h1>\n'
            f'<p style="font-size:44px;color:#C9D4EC">{E(topic)}</p>\n'
            f'<div style="background:#26385F;border-radius:24px;padding:40px;display:flex;flex-direction:column;gap:12px"><p style="font-size:28px;font-weight:700;letter-spacing:3px;color:{YEL}">TODAY WE WILL</p><p style="font-size:44px;font-weight:600">{E(today)}</p></div>\n'
            f'<p style="position:absolute;left:128px;bottom:64px;width:1400px;font-size:24px;color:#B7C3DD">{E(FOOTX)}</p>\n<aside>{E(notes)}</aside>\n</section>\n')
def break_slide(sid,time,text,notes):
    return (f'<section id="{sid}" data-transition="fade" style="background:{TEAL};color:{CREAM};font-family:{BF};padding:128px 128px 160px;display:flex;flex-direction:column;justify-content:center;gap:36px">\n'
            f'<p style="font-size:32px;font-weight:700;letter-spacing:4px;color:{YEL}">{E(time)}</p>\n'
            f'<h2 style="font-family:{HF};font-size:110px;font-weight:600;line-height:1.05">Brain break</h2>\n'
            f'<p style="font-size:48px;font-weight:600">{E(text)}</p>\n<p style="font-size:36px;color:#D7EFEA">Then: a drink of water and back to our seats.</p>\n'
            f'<p style="position:absolute;left:128px;bottom:64px;width:1400px;font-size:24px;color:#D7EFEA">{E(FOOTX)}</p>\n<aside>{E(notes)}</aside>\n</section>\n')
def numcards(items,size=38):
    return ''.join(card(p(f'<span style="color:{TEAL}">{E(a)}</span>  {E(b)}',size,600,raw=True)) for a,b in items)
def checks(sid,time,title,rows,notes,top=250,gapy=150,size=34,lw=170):
    body=h2(title)
    for i,(a,b) in enumerate(rows):
        t=top+i*gapy
        body+=pin(128,t,lw-20,f'<p style="font-size:36px;font-weight:800;color:{TEAL}">{E(a)}</p>',None,WHITE,20,'18px 24px')
        body+=pin(128+lw,t,1664-lw,f'<p style="font-size:{size}px;font-weight:800;line-height:1.25">{E(b)}</p>','pop',YEL,20,'16px 26px')
    return sec(sid,time,body,notes)
def svgwrap(w,h,label,inner,fit=False):
    st=f'width:100%;height:auto;display:block' if fit else f'width:{w}px;height:{h}px;flex:none'
    return f'<svg aria-label="{E(label)}" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="{st}">{inner}</svg>'
def txt(x,y,s,size=40,fill=NAVY,anchor='middle',weight=700,font='Fredoka, Arial'):
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" fill="{fill}" font-family="{font}">{E(str(s))}</text>'
def poly(pts,fill=WHITE,sw=4,dash=False):
    d=' stroke-dasharray="12 8"' if dash else ''
    return f'<polygon points="{" ".join(f"{x:.1f},{y:.1f}" for x,y in pts)}" fill="{fill}" stroke="{NAVY}" stroke-width="{sw}" stroke-linejoin="round"{d}/>'
def line(a,b,sw=3,dash=False,col=NAVY):
    d=' stroke-dasharray="10 7"' if dash else ''
    return f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" stroke="{col}" stroke-width="{sw}"{d}/>'
def rect(x,y,w,h,fill=WHITE,sw=4,rx=0,dash=False):
    d=' stroke-dasharray="10 7"' if dash else ''
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{NAVY}" stroke-width="{sw}"{d}/>'
def bars(rows,unit,x0=170,y0=10,bh=64,gap=26,lab_size=34,seg_size=30,label='Bar model',w=None,extra='',lab_x=None,h=None):
    """rows: list of (label, [(units, fill, text)]). Every unit is drawn as its own box so equal units are visible."""
    s=''; y=y0; maxx=0
    for lab,segs in rows:
        s+=txt((lab_x if lab_x is not None else x0-14),y+bh/2+12,lab,lab_size,NAVY,'end',700,'Nunito Sans, Arial')
        x=x0
        for n,fill,t in segs:
            for i in range(n): s+=rect(x+i*unit,y,unit,bh,fill,3)
            if t: s+=txt(x+n*unit/2,y+bh/2+10,t,seg_size,NAVY,'middle',800,'Nunito Sans, Arial')
            x+=n*unit
        maxx=max(maxx,x); y+=bh+gap
    W=w or int(maxx+30)
    return svgwrap(W,max(int(y-gap+y0+4),h or 0),label,s+extra)
def brace(x1,x2,y,text,size=30,up=False):
    d=-1 if up else 1
    mid=(x1+x2)/2
    return (f'<path d="M{x1} {y} v{8*d} q0 {10*d} 10 {10*d} H{mid-10} q10 0 10 {10*d} q0 -{10*d} 10 -{10*d} H{x2-10} q10 0 10 -{10*d} v-{8*d}" fill="none" stroke="{TEAL}" stroke-width="4" transform="translate(0,0)"/>'
            +txt(mid,y+(52 if not up else -22)*(1 if not up else 1),text,size,TEAL,'middle',800,'Nunito Sans, Arial'))
def write_deck(L,order,sections,S,title,D=None):
    D=D or os.path.join(H,'..','split',L,'project'); sd=os.path.join(D,'slides'); os.makedirs(sd,exist_ok=True)
    assert set(order)==set(S),set(order)^set(S)
    for f in os.listdir(sd):
        if f.endswith('.html') and f[:-5] not in S: os.remove(os.path.join(sd,f))
    for i,h in S.items(): open(os.path.join(sd,i+'.html'),'w').write(h)
    deck={'v':4,'createdOnFiles':{'v':1,'at':datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')},'lists':'css',
     'title':title,'order':order,'cover':order[0],'sections':sections,
     'faces':{'fredoka':{'family':'Fredoka','href':'https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&display=swap'},'nunito-sans':{'family':'Nunito Sans','href':'https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@400;600;700&display=swap'}},
     'designSystems':[]}
    json.dump(deck,open(os.path.join(D,'deck.json'),'w'),indent=1,ensure_ascii=False)
    # lint
    import re
    for i,h in S.items():
        assert '✗' not in h,i
        assert len(re.findall(r'<[a-z]',h))<=200,(i,len(re.findall(r'<[a-z]',h)))
        a=re.search(r'<aside>(.*?)</aside>',h,re.S).group(1); assert len(a)<=4000,(i,len(a))
    print(len(order),'slides')

def pbar(x,y,scale,parts,h=64,sw=3,lab=None,labsize=32,seg=30):
    """One bar split into parts: (value, fill, text, nunits). Width = value*scale. Returns svg fragments."""
    s=''
    if lab: s+=txt(x-14,y+h/2+11,lab,labsize,NAVY,'end',700,'Nunito Sans, Arial')
    cx=x
    for v,fill,t,*n in parts:
        n=n[0] if n else 1; w=v*scale
        s+=rect(cx,y,w,h,fill,sw)
        for i in range(1,n): s+=line((cx+i*w/n,y),(cx+i*w/n,y+h),2)
        if t: s+=txt(cx+w/2,y+h/2+10,t,seg,NAVY,'middle',800,'Nunito Sans, Arial')
        cx+=w
    return s
def vbrace(x,y1,y2,text,size=30,left=False):
    """Brace beside a bar: from y1 to y2 at x (opens to the bar)."""
    d=-1 if left else 1; m=(y1+y2)/2
    return (f'<path d="M{x} {y1} q{10*d} 0 {10*d} 12 V{m-10} q0 10 {10*d} 10 q{-10*d} 0 {-10*d} 10 V{y2-12} q0 12 {10*d} 12" fill="none" stroke="{TEAL}" stroke-width="4"/>'
            +txt(x+(26 if not left else -26)*1,m+10,text,size,TEAL,'start' if not left else 'end',800,'Nunito Sans, Arial'))
def hbrace(x1,x2,y,text,size=30):
    m=(x1+x2)/2
    return (f'<path d="M{x1} {y} v10 q0 10 10 10 H{m-10} q10 0 10 10 q0 -10 10 -10 H{x2-10} q10 0 10 -10 v-10" fill="none" stroke="{TEAL}" stroke-width="4"/>'
            +txt(m,y+60,text,size,TEAL,'middle',800,'Nunito Sans, Arial'))
