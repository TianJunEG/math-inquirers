import sys,glob,os
from playwright.sync_api import sync_playwright
S='/tmp/claude-0/-home-claude/2972495b-87c0-5185-98d8-712902f3b1b5/scratchpad/split/'
os.makedirs('shots',exist_ok=True)
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/opt/pw-browsers/chromium') if os.path.exists('/opt/pw-browsers/chromium') else p.chromium.launch()
    pg=b.new_page(viewport={'width':1920,'height':1080})
    for k in range(1,11):
        for sid in (f'l{k}-explore1',f'l{k}-chdiag'):
            h=open(f'{S}l{k}/project/slides/{sid}.html').read()
            pg.set_content(f'<html><body style="margin:0"><div style="position:relative;width:1920px;height:1080px;overflow:hidden">{h.replace("<section ","<section data-x ",1).replace("style=\"background","style=\"position:absolute;inset:0;box-sizing:border-box;background",1)}</div></body></html>')
            pg.screenshot(path=f'shots/{sid}.png')
            # overflow check
            sh=pg.evaluate("(()=>{const s=document.querySelector('section');const kids=[...s.children].filter(c=>getComputedStyle(c).position!=='absolute');return [Math.round(kids[kids.length-1].getBoundingClientRect().bottom)]})()")
            print(sid,sh)
    b.close()
