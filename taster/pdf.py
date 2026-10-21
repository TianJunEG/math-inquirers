from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':794,'height':1123})
    pg.goto('file:///tmp/claude-0/-home-claude/2972495b-87c0-5185-98d8-712902f3b1b5/scratchpad/taster/taster.html',wait_until='networkidle')
    pg.wait_for_timeout(800)
    print(pg.evaluate("document.fonts.check('16px Fredoka')"))
    pg.pdf(path='Math_Inquirers_Free_Taster_for_Parents.pdf',width='794px',height='1123px',print_background=True)
    b.close()
