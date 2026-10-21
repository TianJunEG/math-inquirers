from playwright.sync_api import sync_playwright
import sys
body=open('workbook_body.html').read()
import re as _re
out=[];openb=False
INBOX=('class="p sub','class="p ans','class="ln"','<table class="tb"','class="p img','<div style="height:')
for line in body.split('\n'):
    core=line
    pre=''
    if core.startswith('<div class="brk"></div>'):
        pre='<div class="brk"></div>';core=core[len(pre):]
    if core.startswith('<div class="p q'):
        if openb: out.append('</div></div>')
        out.append(pre+'<div class="qwrap"><div class="qbox">'+core);openb=True;continue
    if openb and not pre and any(core.startswith(x) or x in core[:40] for x in INBOX):
        out.append(core);continue
    if openb: out.append('</div></div>');openb=False
    out.append(line)
if openb: out.append('</div></div>')
body='\n'.join(out);css=open('../fonts/fonts.css').read()+open('../hp/wb_style.css').read()
html=f'<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body>{body}</body></html>'
open('workbook_full.html','w').write(html)
foot='<div style="width:100%;font-size:9px;color:#5B6785;padding:0 14mm;display:flex;justify-content:space-between;font-family:Arial"><span>Math Inquirers P5 Holiday Program  •  Notice it. Test it. Explain why.</span><span>Page <span class="pageNumber"></span></span></div>'
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page()
    pg.goto('file://'+__import__('os').path.abspath('workbook_full.html'),wait_until='networkidle');pg.wait_for_timeout(1000)
    pg.pdf(path='Math_Inquirers_P5_Student_Workbook_Designed.pdf',format='A4',print_background=True,display_header_footer=True,header_template='<div></div>',footer_template=foot,margin={'top':'14mm','bottom':'16mm','left':'14mm','right':'14mm'})
    b.close()
