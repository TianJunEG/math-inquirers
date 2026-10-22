from playwright.sync_api import sync_playwright
import os
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':794,'height':1123})
    pg.goto('file://'+os.path.abspath('taster.html'),wait_until='networkidle')
    pg.wait_for_timeout(800)
    pg.pdf(path='Math_Inquirers_Level1_Free_Taster.pdf',width='794px',height='1123px',print_background=True)
    b.close()
os.remove('taster.html')
