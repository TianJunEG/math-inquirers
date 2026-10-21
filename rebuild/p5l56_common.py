"""Shared helpers for the P5 Lesson 5 and 6 generators (same look as the P1/P2 decks). Footer is set at run time."""
import json,os,sys,datetime
H=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,H)
import slidekit
from slidekit import *
slidekit.FOOT='Math Inquirers P5 Holiday Program  •  Notice it. Test it. Explain why.'
FOOTX=slidekit.FOOT
RED='#D64545'; WSIDE='#BCD6EE'; WTOP='#EEF5FC'
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
    return ''.join(card(p(f'<span style="color:{TEAL}">{a}</span>  {E(b)}',size,600,raw=True)) for a,b in items)
def checks(sid,time,title,rows,notes,top=250,gapy=150,size=34,lw=170):
    body=h2(title)
    for i,(a,b) in enumerate(rows):
        t=top+i*gapy
        body+=pin(128,t,lw-20,f'<p style="font-size:36px;font-weight:800;color:{TEAL}">{E(a)}</p>',None,WHITE,20,'18px 24px')
        body+=pin(128+lw,t,1664-lw,f'<p style="font-size:{size}px;font-weight:800;line-height:1.25">{E(b)}</p>','pop',YEL,20,'16px 26px')
    return sec(sid,time,body,notes)
def svgwrap(w,h,label,inner,style=''):
    return f'<svg aria-label="{E(label)}" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="width:{w}px;height:{h}px;flex:none;{style}">{inner}</svg>'
def txt(x,y,s,size=40,fill=NAVY,anchor='middle',weight=700,font='Fredoka, Arial'):
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" fill="{fill}" font-family="{font}">{E(str(s))}</text>'
def tb(x,y,s,size=28,fill=NAVY,anchor='middle'): return txt(x,y,s,size,fill,anchor,700,'Nunito Sans, Arial')
# ---- oblique box (x right = length, y up = height, z back = breadth) ----
def OB(x0,y0,s):
    return lambda x,y,z:(x0+x*s+z*s*0.433,y0-y*s-z*s*0.25)
def _pts(P,l): return ' '.join('%.1f,%.1f'%P(*q) for q in l)
def _ln(P,a,b,o=''):
    x1,y1=P(*a);x2,y2=P(*b); return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{NAVY}" {o}/>'
def box(P,L,B,Hh,water=None,grid=False,fill=None,labels=None,size=28,wlabel=None,sw=4,dash=True):
    s=''
    if water is not None:
        d=f'stroke-width="2.5" stroke-dasharray="8 6"'
        s+=_ln(P,(0,0,B),(L,0,B),d)+_ln(P,(0,0,B),(0,Hh,B),d)+_ln(P,(0,0,0),(0,0,B),d)
        if water>0:
            w=water
            s+=f'<polygon points="{_pts(P,[(0,w,0),(L,w,0),(L,w,B),(0,w,B)])}" fill="{WTOP}" stroke="{NAVY}" stroke-width="1.5"/>'
            s+=f'<polygon points="{_pts(P,[(0,0,0),(L,0,0),(L,w,0),(0,w,0)])}" fill="{SKY}"/>'
            s+=f'<polygon points="{_pts(P,[(L,0,0),(L,0,B),(L,w,B),(L,w,0)])}" fill="{WSIDE}"/>'
    elif fill:
        s+=f'<polygon points="{_pts(P,[(0,0,0),(L,0,0),(L,Hh,0),(0,Hh,0)])}" fill="{fill[0]}"/>'
        s+=f'<polygon points="{_pts(P,[(0,Hh,0),(L,Hh,0),(L,Hh,B),(0,Hh,B)])}" fill="{fill[1]}"/>'
        s+=f'<polygon points="{_pts(P,[(L,0,0),(L,0,B),(L,Hh,B),(L,Hh,0)])}" fill="{fill[2]}"/>'
    if grid:
        g='stroke-width="2"'
        for i in range(1,L): s+=_ln(P,(i,0,0),(i,Hh,0),g)+_ln(P,(i,Hh,0),(i,Hh,B),g)
        for j in range(1,Hh): s+=_ln(P,(0,j,0),(L,j,0),g)+_ln(P,(L,j,0),(L,j,B),g)
        for k in range(1,B): s+=_ln(P,(0,Hh,k),(L,Hh,k),g)+_ln(P,(L,0,k),(L,Hh,k),g)
    e=f'stroke-width="{sw}" stroke-linejoin="round"'
    s+=f'<polygon points="{_pts(P,[(0,0,0),(L,0,0),(L,Hh,0),(0,Hh,0)])}" fill="none" stroke="{NAVY}" {e}/>'
    s+=f'<polygon points="{_pts(P,[(0,Hh,0),(L,Hh,0),(L,Hh,B),(0,Hh,B)])}" fill="none" stroke="{NAVY}" {e}/>'
    s+=f'<polygon points="{_pts(P,[(L,0,0),(L,0,B),(L,Hh,B),(L,Hh,0)])}" fill="none" stroke="{NAVY}" {e}/>'
    if labels:
        a,b,c=labels
        if a: x,y=P(L/2,0,0); s+=tb(x,y+size+8,a,size)
        if b: x,y=P(0,Hh/2,0); s+=tb(x-12,y+size/3,b,size,NAVY,'end')
        if c: x,y=P(L,0,B/2); s+=tb(x+14,y+size+4,c,size,NAVY,'start')
    if wlabel and water:
        x1,y1=P(L*0.1,0,0);_,y2=P(L*0.1,water,0)
        s+=f'<line x1="{x1:.1f}" y1="{y1-3:.1f}" x2="{x1:.1f}" y2="{y2+3:.1f}" stroke="{TEAL}" stroke-width="4"/>'
        s+=tb(x1+12,(y1+y2)/2+size/3,wlabel,size,TEAL,'start')
    return s
CUBEF=('#C9CED8','#E3E6EC','#AEB4C2'); YELF=(YEL,'#FFE08A','#F2B92E')
def ws_prev(sid,time,title,items,tip,notes): return ws_preview(sid,time,title,items,tip,notes)
def finish(P,S,order,title,sections,D):
    assert set(order)==set(S),set(order)^set(S)
    sd=os.path.join(D,'slides'); os.makedirs(sd,exist_ok=True)
    for f in os.listdir(sd):
        if f.endswith('.html') and f[:-5] not in S: os.remove(os.path.join(sd,f))
    for i,h in S.items():
        assert len(h.split('<aside>')[1])<4100,(i,'notes too long')
        open(os.path.join(sd,i+'.html'),'w').write(h)
    deck={'v':4,'createdOnFiles':{'v':1,'at':datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')},'lists':'css','title':title,'order':order,'cover':order[0],
     'sections':sections,
     'faces':{'fredoka':{'family':'Fredoka','href':'https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&display=swap'},'nunito-sans':{'family':'Nunito Sans','href':'https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@400;600;700&display=swap'}},
     'designSystems':[]}
    json.dump(deck,open(os.path.join(D,'deck.json'),'w'),indent=1,ensure_ascii=False)
    print(len(order),'slides')
