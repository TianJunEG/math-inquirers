"""Render every P5 slide at 1920x1080 and report content below y=925 (footer excluded) or outside the right edge.
Usage: python3 docs/audit/fixes_round2_p5_overflow.py [lesson numbers]   (default 1..10); optional SHOT=dir to save PNGs."""
import sys,os,json
from playwright.sync_api import sync_playwright
R=os.environ.get('ROOT') or os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..')
lv=[int(x) for x in sys.argv[1:]] or range(1,11)
JS="""()=>{const sec=document.querySelector('section');const out=[];const sr=sec.getBoundingClientRect();
for(const e of sec.querySelectorAll('*')){if(e.closest('aside')||e.closest('[data-deco]'))continue;
 if(e.children.length&&e.tagName!=='svg'&&!e.matches('p,li,h2,span'))continue;
 const r=e.getBoundingClientRect();if(!r.width||!r.height)continue;
 if(e.tagName.toLowerCase()==='p'&&e.getAttribute('style')&&e.getAttribute('style').includes('bottom:64px'))continue;
 if(r.bottom-sr.top>925||r.right-sr.left>1925)out.push([e.tagName,Math.round(r.bottom-sr.top),Math.round(r.right-sr.left),(e.textContent||'').slice(0,40)]);}
return out.slice(0,3)}"""
bad=0;tot=0
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':1920,'height':1080})
    for n in lv:
        D=os.path.join(R,'split',f'p5l{n}','project'); d=json.load(open(os.path.join(D,'deck.json')))
        for sid in d['order']:
            h=open(os.path.join(D,'slides',sid+'.html')).read()
            pg.set_content('<html><body style="margin:0"><div style="width:1920px;height:1080px;position:relative">'+h+'</div></body></html>')
            pg.add_style_tag(content='section{width:1920px;height:1080px;box-sizing:border-box;position:relative;overflow:hidden} aside{display:none} *{margin:0}')
            pg.wait_for_timeout(30)
            r=pg.evaluate(JS); tot+=1
            if r: bad+=1; print('OVERFLOW',sid,r)
            if os.environ.get('SHOT') and sid.split('-',1)[-1] in os.environ.get('ONLY','').split(','):
                pg.screenshot(path=os.path.join(os.environ['SHOT'],sid+'.png'))
    b.close()
print(tot,'slides checked,',bad,'with overflow')
