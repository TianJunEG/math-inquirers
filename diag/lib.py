NAVY='#1B2A49';TEAL='#1F7A6F';YEL='#FFC93C';CREAM='#FFF9EC';RED='#D64545';BLUE='#3A6EA5';GREY='#C9D4EC';WHITE='#FFFFFF'
def T(x,y,s,size=28,fill=NAVY,anchor='middle',weight=700):
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}" font-family="Nunito Sans, Arial, sans-serif">{s}</text>'
def R(x,y,w,h,fill=WHITE,stroke=NAVY,sw=3,rx=8,dash=False):
    d=' stroke-dasharray="10 7"' if dash else ''
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>'
def C(x,y,r,fill=WHITE,stroke=NAVY,sw=3,dash=False):
    d=' stroke-dasharray="6 5"' if dash else ''
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>'
def L(x1,y1,x2,y2,stroke=NAVY,sw=3,dash=False):
    d=' stroke-dasharray="8 6"' if dash else ''
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{sw}"{d}/>'
def PG(pts,fill='none',stroke=NAVY,sw=3):
    return f'<polygon points="{" ".join(f"{a},{b}" for a,b in pts)}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round"/>'
def PL(pts,stroke=NAVY,sw=3,dash=False):
    d=' stroke-dasharray="8 6"' if dash else ''
    return f'<polyline points="{" ".join(f"{a},{b}" for a,b in pts)}" fill="none" stroke="{stroke}" stroke-width="{sw}"{d}/>'
def ARC(x1,x2,y,h,label,col=TEAL):
    mx=(x1+x2)/2
    return f'<path d="M{x1},{y} Q{mx},{y-h} {x2},{y}" fill="none" stroke="{col}" stroke-width="4"/>'+T(mx,y-h/2-8,label,26,col)
def BRACE(x1,x2,y,label,up=True):
    d=-1 if up else 1
    return f'<path d="M{x1},{y} v{d*10} H{x2} v{-d*10}" fill="none" stroke="{NAVY}" stroke-width="3"/>'+T((x1+x2)/2,y+d*40 if up else y+d*38,label,26)
def SVG(w,h,body,style=''):
    return f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;display:block;{style}">{body}</svg>'
def face(x,y,r=22,fill=YEL):
    return C(x,y,r,fill)+C(x-r*0.35,y-r*0.2,r*0.1,NAVY,NAVY,1)+C(x+r*0.35,y-r*0.2,r*0.1,NAVY,NAVY,1)+f'<path d="M{x-r*0.4},{y+r*0.3} Q{x},{y+r*0.7} {x+r*0.4},{y+r*0.3}" fill="none" stroke="{NAVY}" stroke-width="2.5"/>'
def coin(x,y,lab,r=46,fill='#E5E9F2'):
    return C(x,y,r,fill)+C(x,y,r-7,fill,'#8A94AD',2)+T(x,y+9,lab,26)
