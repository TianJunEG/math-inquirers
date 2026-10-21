N='#1B2A49'
dol=f'''<path d="M42 150 Q30 96 70 70 Q118 38 168 58 Q206 74 214 112 Q216 128 198 132 L168 134 Q150 160 112 166 Q72 170 42 150 Z" fill="#5AA9E6" stroke="{N}" stroke-width="5" stroke-linejoin="round"/>
<path d="M60 152 Q100 172 150 140 Q130 168 96 170 Q72 170 60 152 Z" fill="#D6E9FB"/>
<path d="M112 62 Q118 30 146 24 Q138 44 142 60" fill="#5AA9E6" stroke="{N}" stroke-width="5" stroke-linejoin="round"/>
<path d="M50 148 Q24 150 14 132 Q34 132 44 140 Q30 122 34 104 Q48 124 54 140" fill="#5AA9E6" stroke="{N}" stroke-width="5" stroke-linejoin="round"/>
<path d="M118 138 Q112 160 92 168 Q110 150 104 136" fill="#5AA9E6" stroke="{N}" stroke-width="4" stroke-linejoin="round"/>
<circle cx="168" cy="96" r="13" fill="#fff" stroke="{N}" stroke-width="4"/><circle cx="171" cy="97" r="6" fill="{N}"/>
<path d="M178 122 Q196 126 208 116" fill="none" stroke="{N}" stroke-width="4" stroke-linecap="round"/><circle cx="160" cy="118" r="6" fill="#FF9C8A"/>
<g transform="translate(176,26)"><circle cx="0" cy="0" r="14" fill="#FFC93C" stroke="{N}" stroke-width="4"/><text x="0" y="6" font-family="Fredoka" font-size="18" text-anchor="middle" fill="{N}">?</text></g>
<circle cx="200" cy="56" r="5" fill="#fff" stroke="{N}" stroke-width="3"/><circle cx="210" cy="44" r="3.5" fill="#fff" stroke="{N}" stroke-width="2.5"/>'''
html=f'''<html><head><style>{open('../fonts/fonts.css').read()}body{{margin:0;background:#EEF5FB;font-family:'Nunito Sans';color:{N};padding:24px}}
.c{{width:380px;background:#fff;border:3px solid {N};border-radius:22px;box-shadow:5px 5px 0 {N};padding:16px 20px 20px}}
.tag{{display:inline-block;font:800 11px 'Nunito Sans';letter-spacing:.08em;text-transform:uppercase;border:2px solid {N};border-radius:999px;padding:2px 10px}}
h3{{font:600 24px Fredoka;margin:4px 0}} p{{margin:0;font-size:14.5px;line-height:1.45}}</style></head><body><div class="c"><span class="tag">Option</span>
<svg viewBox="0 0 240 200" width="100%">{dol}</svg><h3>Dolphin</h3><p>Smart, friendly and learns in a group (a pod), like our small classes. Light blue matches the new brand colour.</p></div></body></html>'''
open('d.html','w').write(html)
from playwright.sync_api import sync_playwright
import os
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':440,'height':500},device_scale_factor=2)
    pg.goto('file://'+os.path.abspath('d.html'));pg.wait_for_timeout(300);pg.locator('.c').screenshot(path='Mascot_Dolphin.png');b.close()
