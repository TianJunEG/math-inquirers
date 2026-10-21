N='#1B2A49'
def cell(svg,name,line,tag):
    return f'''<div class="c"><div class="tag">{tag}</div><svg viewBox="0 0 240 220">{svg}</svg><h3>{name}</h3><p>{line}</p></div>'''
frog=f'''<ellipse cx="120" cy="150" rx="72" ry="50" fill="#3DBE7A" stroke="{N}" stroke-width="5"/>
<circle cx="88" cy="96" r="26" fill="#3DBE7A" stroke="{N}" stroke-width="5"/><circle cx="152" cy="96" r="26" fill="#3DBE7A" stroke="{N}" stroke-width="5"/>
<circle cx="88" cy="96" r="15" fill="#fff" stroke="{N}" stroke-width="4"/><circle cx="152" cy="96" r="15" fill="#fff" stroke="{N}" stroke-width="4"/><circle cx="92" cy="98" r="6" fill="{N}"/><circle cx="156" cy="98" r="6" fill="{N}"/>
<path d="M95 150 Q120 170 145 150" fill="none" stroke="{N}" stroke-width="5" stroke-linecap="round"/><circle cx="78" cy="140" r="7" fill="#FF9C8A"/><circle cx="162" cy="140" r="7" fill="#FF9C8A"/>'''
otter=f'''<ellipse cx="120" cy="168" rx="60" ry="40" fill="#A86B3C" stroke="{N}" stroke-width="5"/>
<circle cx="76" cy="74" r="9" fill="#A86B3C" stroke="{N}" stroke-width="5"/><circle cx="164" cy="74" r="9" fill="#A86B3C" stroke="{N}" stroke-width="5"/>
<ellipse cx="120" cy="108" rx="58" ry="52" fill="#A86B3C" stroke="{N}" stroke-width="5"/><ellipse cx="120" cy="126" rx="36" ry="26" fill="#F3D9B8"/>
<circle cx="98" cy="94" r="7" fill="{N}"/><circle cx="142" cy="94" r="7" fill="{N}"/><ellipse cx="120" cy="114" rx="10" ry="7" fill="{N}"/>
<path d="M110 128 Q120 136 130 128" fill="none" stroke="{N}" stroke-width="4" stroke-linecap="round"/>
<path d="M84 120 L56 114 M84 128 L56 130 M156 120 L184 114 M156 128 L184 130" stroke="{N}" stroke-width="3" stroke-linecap="round"/>
<ellipse cx="120" cy="176" rx="22" ry="14" fill="#FFC93C" stroke="{N}" stroke-width="4"/><ellipse cx="94" cy="172" rx="13" ry="11" fill="#A86B3C" stroke="{N}" stroke-width="4"/><ellipse cx="146" cy="172" rx="13" ry="11" fill="#A86B3C" stroke="{N}" stroke-width="4"/>'''
import math
def arm(i):
    x0=74+i*13; spread=(i-3.5)*22; ex=120+spread*1.3; ey=196-abs(i-3.5)*9
    cx=x0+spread*0.6; cy=180
    curl=-1 if i<4 else 1
    return f'<path d="M{x0} 132 Q{cx} {cy} {ex} {ey} q{curl*12} -2 {curl*10} -14" fill="none" stroke="{N}" stroke-width="16" stroke-linecap="round"/><path d="M{x0} 132 Q{cx} {cy} {ex} {ey} q{curl*12} -2 {curl*10} -14" fill="none" stroke="#FF7A59" stroke-width="10" stroke-linecap="round"/>'
arms=''.join(arm(i) for i in range(8))
octo=f'''{arms}<path d="M62 136 Q56 40 120 40 Q184 40 178 136 Q120 152 62 136 Z" fill="#FF7A59" stroke="{N}" stroke-width="5"/>
<circle cx="98" cy="100" r="15" fill="#fff" stroke="{N}" stroke-width="4"/><circle cx="142" cy="100" r="15" fill="#fff" stroke="{N}" stroke-width="4"/><circle cx="101" cy="102" r="6" fill="{N}"/><circle cx="145" cy="102" r="6" fill="{N}"/>
<path d="M106 124 Q120 134 134 124" fill="none" stroke="{N}" stroke-width="4" stroke-linecap="round"/>
<text x="120" y="78" font-size="16" text-anchor="middle" fill="{N}" font-family="Fredoka">8</text>'''
fox=f'''<path d="M64 48 L92 92 L60 104 Z" fill="#F28C38" stroke="{N}" stroke-width="5" stroke-linejoin="round"/><path d="M176 48 L148 92 L180 104 Z" fill="#F28C38" stroke="{N}" stroke-width="5" stroke-linejoin="round"/>
<path d="M56 100 Q120 60 184 100 Q176 170 120 186 Q64 170 56 100 Z" fill="#F28C38" stroke="{N}" stroke-width="5" stroke-linejoin="round"/>
<path d="M70 128 Q100 132 120 186 Q140 132 170 128 Q150 172 120 186 Q90 172 70 128 Z" fill="#fff"/>
<circle cx="98" cy="118" r="7" fill="{N}"/><circle cx="142" cy="118" r="7" fill="{N}"/><ellipse cx="120" cy="160" rx="9" ry="7" fill="{N}"/>
<circle cx="186" cy="168" r="22" fill="#D6E9FB" stroke="{N}" stroke-width="5"/><path d="M170 184 L148 206" stroke="{N}" stroke-width="8" stroke-linecap="round"/>'''
owl=f'''<path d="M58 70 L76 92 M182 70 L164 92" stroke="{N}" stroke-width="5"/><ellipse cx="120" cy="128" rx="66" ry="76" fill="#1F7A6F" stroke="{N}" stroke-width="5"/>
<ellipse cx="120" cy="150" rx="40" ry="46" fill="#DCEFEA"/>
<circle cx="94" cy="104" r="22" fill="#fff" stroke="{N}" stroke-width="4"/><circle cx="146" cy="104" r="22" fill="#fff" stroke="{N}" stroke-width="4"/><circle cx="96" cy="106" r="9" fill="{N}"/><circle cx="148" cy="106" r="9" fill="{N}"/>
<path d="M112 128 L120 142 L128 128 Z" fill="#FFC93C" stroke="{N}" stroke-width="3" stroke-linejoin="round"/>'''
cells=[cell(otter,'Otter','Singapore\'s favourite wild animal. Otters use stones as tools, like children testing ideas with objects.','My pick'),
 cell(octo,'Octopus','Eight arms, like our groups of up to 8. Clever, curious, and good at counting and juggling ideas.','Strong option'),
 cell(fox,'Fox','Curious and clever, carrying a magnifying glass. Ties to "Notice it", but foxes are less local.','Option'),
 cell(frog,'Frog (current)','From Lesson 1: hopping along a number line. Fun, but says "jumping" more than "thinking".','Current'),
 cell(owl,'Owl','The classic "wise" animal. Clear meaning, but many tuition and school brands already use an owl.','Common')]
html=f'''<html><head><style>{open('../fonts/fonts.css').read()}
body{{margin:0;background:#EEF5FB;font-family:'Nunito Sans';color:{N};padding:28px}}
h1{{font:600 34px Fredoka;margin:0 0 4px}} .s{{font-size:16px;margin:0 0 20px;color:#56637A}}
.g{{display:grid;grid-template-columns:repeat(5,1fr);gap:16px;width:1260px}}
.c{{background:#fff;border:3px solid {N};border-radius:22px;box-shadow:5px 5px 0 {N};padding:14px 16px 18px;position:relative}}
.c:first-child{{background:#FFF0C4}}
.tag{{display:inline-block;font:800 11px 'Nunito Sans';letter-spacing:.08em;text-transform:uppercase;border:2px solid {N};border-radius:999px;padding:2px 10px;background:#fff}}
svg{{width:100%;height:auto}} h3{{font:600 22px Fredoka;margin:2px 0 4px}} p{{margin:0;font-size:14px;line-height:1.45}}
</style></head><body><h1>Mascot options</h1><p class="s">Rough sketches in the brand colours, to compare the ideas. A designer would refine the one you choose.</p><div class="g">{''.join(cells)}</div></body></html>'''
open('m.html','w').write(html)
from playwright.sync_api import sync_playwright
import os
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':1320,'height':600},device_scale_factor=2)
    pg.goto('file://'+os.path.abspath('m.html'));pg.wait_for_timeout(300)
    pg.screenshot(path='Mascot_Options.png',full_page=True);b.close()
