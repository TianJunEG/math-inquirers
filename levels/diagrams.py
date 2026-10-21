"""Shared diagram helper: draws vertical-column arithmetic with blank boxes as PNG.
Usage: from levels.diagrams import column_png
 column_png('out.png', rows=['3_82','14_9'], op='+', result='5141')   # '_' = empty answer box
 column_png('out.png', rows=['A B C'...]) letters allowed: any char that is a letter is drawn inside a coloured rounded box
Characters: digits as text, '_' = blank white box with navy outline, letters A-Z = coloured box with the letter,
the same letter always gets the same colour. Never use unicode box/shape glyphs in content."""
from PIL import Image, ImageDraw, ImageFont
import os
NAVY=(27,42,73); CREAM=(255,249,236)
COLS={'A':(255,201,60),'B':(125,196,240),'C':(150,210,140),'D':(240,150,120),'E':(190,160,230),'F':(240,170,200)}
def _font(sz):
    for p in ['/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf','/usr/share/fonts/dejavu/DejaVuSans-Bold.ttf']:
        if os.path.exists(p): return ImageFont.truetype(p,sz)
    return ImageFont.load_default()
def column_png(path,rows,op='+',result=None,cell=70,bg=None):
    n=max(len(r.replace(' ','')) for r in rows+([result] if result else []))
    W=(n+2)*cell; H=(len(rows)+(2 if result else 1))*cell
    im=Image.new('RGB',(W,H),bg or (255,255,255)); d=ImageDraw.Draw(im); f=_font(int(cell*.6))
    def draw_row(y,s,lead=''):
        s=s.replace(' ','').rjust(n)
        if lead: d.text((cell*0.35,y+cell*0.1),lead,fill=NAVY,font=f)
        for i,ch in enumerate(s):
            x=(i+1.5)*cell; box=(x+4,y+4,x+cell-4,y+cell-4)
            if ch=='_': d.rounded_rectangle(box,10,outline=NAVY,width=4,fill=(255,255,255))
            elif ch.isalpha():
                d.rounded_rectangle(box,10,outline=NAVY,width=4,fill=COLS.get(ch.upper(),(200,200,200)))
                w=d.textlength(ch,font=f); d.text((x+(cell-w)/2,y+cell*0.1),ch,fill=NAVY,font=f)
            elif ch!=' ':
                w=d.textlength(ch,font=f); d.text((x+(cell-w)/2,y+cell*0.1),ch,fill=NAVY,font=f)
    for k,r in enumerate(rows): draw_row(k*cell,r,op if k==len(rows)-1 else '')
    y=len(rows)*cell; d.line((cell*0.3,y+4,W-cell*0.3,y+4),fill=NAVY,width=5)
    if result: draw_row(y+8,result)
    im.save(path); return path
if __name__=='__main__':
    column_png('/tmp/claude-0/-home-claude/2972495b-87c0-5185-98d8-712902f3b1b5/scratchpad/col.png',['3_82','14_9'],'+','5141')
