"""Shared helpers for rebuilt lesson decks (Claude Slides format, 1920x1080, inline styles only)."""
import html
NAVY='#1B2A49'; CREAM='#FFF9EC'; TEAL='#1F7A6F'; YEL='#FFC93C'; WHITE='#FFFFFF'; MUTED='#3B4A6B'; SOFT='#FFF0C2'; SKY='#DDEBF7'; GREY='#EDEDED'
HF="'Fredoka', Arial, sans-serif"; BF="'Nunito Sans', Arial, sans-serif"
FOOT='Math Inquirers Holiday Program  •  Notice it. Test it. Explain why.'
E=html.escape
def sec(sid,time,body,notes,dark=False):
    bg=NAVY if dark else CREAM; fg=CREAM if dark else NAVY
    t=f'<p style="position:absolute;right:128px;top:64px;font-size:28px;font-weight:700;letter-spacing:2px;color:{YEL if dark else TEAL}">{E(time)}</p>' if time else ''
    return (f'<section id="{sid}" data-transition="fade" style="background:{bg};color:{fg};font-family:{BF};padding:128px 128px 160px;display:flex;flex-direction:column;gap:28px">\n'
            f'{t}\n{body}\n<p style="position:absolute;left:128px;bottom:64px;width:1400px;font-size:24px;color:{"#B7C3DD" if dark else "#5B6785"}">{E(FOOT)}</p>\n<aside>{E(notes)}</aside>\n</section>\n')
def h2(t,size=68): return f'<h2 style="font-family:{HF};font-size:{size}px;font-weight:600;line-height:1.1">{E(t)}</h2>'
def chip(t,bg=TEAL,fg=CREAM,size=28): return f'<p style="align-self:flex-start;background:{bg};color:{fg};border-radius:999px;padding:8px 24px;font-size:{size}px;font-weight:700">{E(t)}</p>'
def card(inner,bg=WHITE,extra=''): return f'<div style="background:{bg};border-radius:24px;padding:32px 40px;display:flex;flex-direction:column;gap:14px;{extra}">{inner}</div>'
def p(t,size=40,weight=600,color=None,raw=False):
    c=f'color:{color};' if color else ''
    return f'<p style="font-size:{size}px;font-weight:{weight};{c}line-height:1.3">{t if raw else E(t)}</p>'
def pin(left,top,width,inner,build=None,bg=None,radius=20,pad='18px 28px',extra=''):
    b=f' data-build-in="{build}"' if build else ''
    bgs=f'background:{bg};border-radius:{radius}px;padding:{pad};' if bg else ''
    return f'<div{b} style="position:absolute;left:{left}px;top:{top}px;width:{width}px;{bgs}display:flex;flex-direction:column;gap:8px;{extra}">{inner}</div>'
def step(n,text,left=128,top=420,width=1664,build='rise',size=38):
    inner=f'<p style="font-size:{size}px;font-weight:600;line-height:1.3"><span style="color:{TEAL};font-weight:800">Step {n}.</span>  {text}</p>'
    return pin(left,top,width,inner,build,WHITE,20,'20px 30px')
def machine(cells,back=None,w=1664,h=None):
    """cells: list of (text, kind) kind in q|op|res ; back: label for a backward arrow under the boxes"""
    n=len(cells); bw=min(230,(w-40)/n*0.72); gap=(w-40-n*bw)/(n-1) if n>1 else 0
    h=h or (240 if back else 130)
    fills={'q':YEL,'op':GREY,'res':SKY}
    s=f'<svg aria-label="Number machine" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="width:{w}px;height:{h}px">'
    xs=[]
    for i,(t,k) in enumerate(cells):
        x=20+i*(bw+gap); xs.append(x)
        s+=f'<rect x="{x}" y="10" width="{bw}" height="100" rx="18" fill="{fills[k]}" stroke="{NAVY}" stroke-width="4"/><text x="{x+bw/2}" y="76" font-size="{min(52,bw*0.3):.0f}" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="Fredoka, Arial">{E(t)}</text>'
        if i<n-1:
            a=x+bw+12; b=x+bw+gap-12
            s+=f'<line x1="{a}" y1="60" x2="{b-16}" y2="60" stroke="{NAVY}" stroke-width="5"/><polygon points="{b},60 {b-22},48 {b-22},72" fill="{NAVY}"/>'
    if back:
        a=xs[-1]+bw/2; b=xs[0]+bw/2
        s+=f'<path d="M{a} 116 Q{(a+b)/2} 196 {b} 116" fill="none" stroke="{TEAL}" stroke-width="5" stroke-dasharray="12 9"/><polygon points="{b},112 {b+10},136 {b+24},120" fill="{TEAL}"/><text x="{(a+b)/2}" y="228" font-size="34" font-weight="800" text-anchor="middle" fill="{TEAL}" font-family="Nunito Sans, Arial">{E(back)}</text>'
    return s+'</svg>'
def answer(left,top,width,text,build='pop'):
    return pin(left,top,width,f'<p style="font-size:40px;font-weight:800;line-height:1.2">{E(text)}</p>',build,YEL,20,'18px 26px')
def qrow(left,top,width,label,text,size=38):
    return pin(left,top,width,f'<p style="font-size:{size}px;font-weight:600;line-height:1.3"><span style="color:{TEAL};font-weight:800">{E(label)}</span>  {E(text)}</p>',None,WHITE,20,'18px 28px')

def trow(left,top,cells,widths,build=None,header=False,size=36):
    bg=YEL if header else WHITE
    inner=''.join(f'<div style="width:{w}px;padding:14px 18px;font-size:{size}px;font-weight:{800 if header else 600};text-align:center">{E(c)}</div>' for c,w in zip(cells,widths))
    b=f' data-build-in="{build}"' if build else ''
    return f'<div{b} style="position:absolute;left:{left}px;top:{top}px;display:flex;background:{bg};border:3px solid {NAVY};border-radius:12px">{inner}</div>'
def triangle_svg(nums=None,w=600,h=520,label=''):
    pos=[(300,60),(70,450),(530,450),(185,255),(300,450),(415,255)]  # A,B,C, AB, BC, CA
    s=f'<svg aria-label="Magic triangle {E(label)}" viewBox="0 0 600 520" xmlns="http://www.w3.org/2000/svg" style="width:{w}px;height:{h}px"><polygon points="300,60 70,450 530,450" fill="none" stroke="{NAVY}" stroke-width="5" stroke-linejoin="round"/>'
    for i,(x,y) in enumerate(pos):
        corner=i<3
        s+=f'<circle cx="{x}" cy="{y}" r="44" fill="{YEL if corner else WHITE}" stroke="{NAVY}" stroke-width="5"/>'
        if nums and nums[i] is not None: s+=f'<text x="{x}" y="{y+17}" font-size="48" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="Fredoka, Arial">{nums[i]}</text>'
    return s+'</svg>'
def cubes_svg(groups,w=1100,h=110,size=70):
    """groups: list of (count, colour, label)"""
    s=f'<svg aria-label="cubes" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="width:{w}px;height:{h}px">'; x=4
    for n,col,lab in groups:
        x0=x
        for i in range(n):
            s+=f'<rect x="{x}" y="6" width="{size}" height="{size}" rx="8" fill="{col}" stroke="{NAVY}" stroke-width="4"/>'; x+=size+8
        if lab: s+=f'<text x="{(x0+x-8)/2}" y="{size+34}" font-size="28" font-weight="800" text-anchor="middle" fill="{TEAL}" font-family="Nunito Sans, Arial">{E(lab)}</text>'
        x+=30
    return s+'</svg>'
def seesaw_svg(left,right,w=1100,h=260,tilt=0):
    return (f'<svg aria-label="Balance: {E(left)} and {E(right)}" viewBox="0 0 1100 260" xmlns="http://www.w3.org/2000/svg" style="width:{w}px;height:{h}px">'
            f'<g transform="rotate({tilt} 550 150)"><rect x="80" y="140" width="940" height="22" rx="10" fill="{NAVY}"/>'
            f'<rect x="110" y="40" width="340" height="96" rx="18" fill="{SKY}" stroke="{NAVY}" stroke-width="4"/><text x="280" y="106" font-size="54" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="Fredoka, Arial">{E(left)}</text>'
            f'<rect x="650" y="40" width="340" height="96" rx="18" fill="{SOFT}" stroke="{NAVY}" stroke-width="4"/><text x="820" y="106" font-size="54" font-weight="700" text-anchor="middle" fill="{NAVY}" font-family="Fredoka, Arial">{E(right)}</text></g>'
            f'<polygon points="550,162 490,250 610,250" fill="{TEAL}" stroke="{NAVY}" stroke-width="4"/></svg>')
def ws_preview(sid,time,title,items,tip,notes):
    inner=''.join(p(f'<span style="color:#1F7A6F;font-weight:800">{E(a)}</span>  {E(b)}',38,600,raw=True) for a,b in items)
    return sec(sid,time,h2(title)+card(inner)+card(p(tip,34,600,MUTED)),notes)
def check_slide(sid,time,title,rows,notes,lw=200):
    body=h2(title)
    for i,(a,b) in enumerate(rows):
        top=250+i*130
        body+=pin(128,top,lw-20,f'<p style="font-size:36px;font-weight:800;color:{TEAL}">{E(a)}</p>',None,WHITE,20,'18px 24px')
        body+=answer(128+lw,top,1664-lw,b)
    return sec(sid,time,body,notes)
def try_slide(sid,time,title,sub,rows,notes,size=40):
    body=h2(title)+p(sub,34,600,MUTED)
    for i,(a,b,c) in enumerate(rows):
        body+=qrow(128,340+i*150,1250,a,b,size)+answer(1420,340+i*150,372,c)
    return sec(sid,time,body,notes)
