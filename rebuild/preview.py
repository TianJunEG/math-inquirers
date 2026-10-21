import sys,os,json
from playwright.sync_api import sync_playwright
d=sys.argv[1]; out=sys.argv[2]; ids=sys.argv[3].split(',') if len(sys.argv)>3 else json.load(open(d+'/deck.json'))['order']
fonts=open(os.path.join(os.path.dirname(__file__),'..','fonts','fonts.css')).read()
os.makedirs(out,exist_ok=True)
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':1920,'height':1080})
    for i in ids:
        sec=open(f'{d}/slides/{i}.html').read()
        html=f'<html><head><style>{fonts} body{{margin:0}} section{{width:1920px;height:1080px;box-sizing:border-box;position:relative;overflow:hidden}} aside{{display:none}} p,h1,h2,h3{{margin:0}} table{{border-collapse:collapse}} td,th{{padding:12px 24px}}</style></head><body>{sec}</body></html>'
        pg.set_content(html);pg.wait_for_timeout(120)
        o=pg.evaluate("(()=>{const s=document.querySelector('section');return [s.scrollHeight,s.scrollWidth]})()")
        pg.screenshot(path=f'{out}/{i}.png')
        if o[0]>1080 or o[1]>1920: print('OVERFLOW',i,o)
    b.close()
