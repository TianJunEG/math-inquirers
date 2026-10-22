# Scheme of Work PDF for a level:  python3 levels/scheme.py p2   ->  outputs/schemes/Math_Inquirers_Level2_Scheme_of_Work.pdf
import sys, json, subprocess, os, html
from playwright.sync_api import sync_playwright
E = html.escape
LV = sys.argv[1]; N = LV[1:]; R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src = os.path.join(R, 'hp/lessons.js') if LV == 'p1' else os.path.join(R, LV, 'data.js')
js = "const L=require(process.argv[1]);const a=L.lessons;console.log(JSON.stringify(a))"
ls = json.loads(subprocess.run(['node', '-e', js, src], capture_output=True, text=True, check=True).stdout)
NAME = {'1': 'Level 1', '2': 'Level 2', '3': 'Level 3', '4': 'Level 4', '5': 'Level 5', '6': 'Level 6 (after the PSLE): Maths and Coding Bridge'}[N]
FOR = {'1': 'children whose school year covers Primary 1 topics', '2': 'children whose school year covers Primary 2 topics', '3': 'children whose school year covers Primary 3 topics', '4': 'children whose school year covers Primary 4 topics', '5': 'children whose school year covers Primary 5 topics', '6': 'children who have finished the PSLE'}[N]
def sk(x): return E(x if isinstance(x, str) else '; '.join(x))
rows = ''
for l in ls:
    rows += (f'<tr><td class="n">{l["n"]}<small>Week {(l["n"]+1)//2}{"AB"[(l["n"]+1)%2]}</small></td><td><b>{E(l["title"])}</b><br><span class="tp">{E(l["topic"])}</span></td>'
             f'<td>{E(l["objective"])}</td><td>{sk(l["skills"])}</td><td>{E(l["exit"]["q"] if isinstance(l.get("exit"), dict) else l.get("exit",""))}</td></tr>')
css = open(os.path.join(R, 'fonts/fonts.css')).read() + '''
@page{size:A4 landscape;margin:12mm}
body{font-family:'Nunito Sans',Arial;color:#1B2A49;font-size:10.5px;line-height:1.35}
h1{font-family:Fredoka,Arial;font-size:26px;margin:0 0 2px}.sub{color:#1F7A6F;font-weight:800;margin-bottom:8px}
.box{border-left:4px solid #FFC93C;background:#FFF9EC;padding:6px 10px;margin:6px 0 10px}
table{border-collapse:collapse;width:100%}th{background:#1B2A49;color:#fff;text-align:left;padding:5px 6px;font-size:10px}
td{border-bottom:1px solid #D9DEE9;padding:5px 6px;vertical-align:top}td.n{font-family:Fredoka;font-size:20px;color:#D64545;width:44px}td.n small{display:block;font-family:'Nunito Sans';font-size:8px;color:#5B6785}
.tp{color:#5B6785;font-size:9.5px}h2{font-family:Fredoka;font-size:15px;margin:12px 0 4px}tr{break-inside:avoid}
'''
rout = {'1': 'Numbers to 100, number bonds, picture graphs, patterns, money, shapes, logic, length.'}.get(N, '')
# P1 audit (P-1, P-6): the worksheet block includes the check-together slides, so talk time starts at minute 72; say what the program does not cover
ROUT = 'worksheet in pairs, then alone, then checked together (32), talk time (8)' if LV == 'p1' else 'worksheet in pairs then alone (30), talk time (10)'
COVER = '<br><b>Coverage.</b> This is enrichment. It does not teach time, multiplication and division, or 2-digit addition and subtraction within 100, so parents should not expect it to cover the whole Primary 1 syllabus.' if LV == 'p1' else ''
body = f'''<h1>Math Inquirers {NAME}: Scheme of Work</h1><div class="sub">Holiday program for {FOR}  •  10 lessons of 90 minutes  •  2 lessons a week for 5 weeks  •  live online, up to 8 children</div>
<div class="box"><b>Approach.</b> Enrichment, not extra drill: non-routine puzzles tagged to the school syllabus. Every lesson follows the same routine: warm-up (10 min), explore with objects or drawings (15), mini-lesson (10), brain break (5), {ROUT}, exit ticket and journal stamp (10).<br><b>Habits.</b> Notice it. Test it. Explain why.{COVER}</div>
<table><thead><tr><th>Lesson</th><th>Title and syllabus topic</th><th>Objective</th><th>Skills and heuristics practised</th><th>Exit ticket</th></tr></thead><tbody>{rows}</tbody></table>
<h2>Assessment and progress</h2><p>Each lesson has a 2-page worksheet (Start here), Think harder and Go further pages, an exit ticket and an Inquiry Journal stamp. Tutors record S (secure), D (developing) or H (needs help) for each child on the progress tracker in the tutor guide. Parents receive a short note each week and the Weekly Dose of Thinking Math practice pack.</p>
<h2>Materials</h2><p>Printed student workbook with cut-outs, pencil, scissors and paper; a laptop or tablet with a camera. Tutors use the slides for each lesson and the tutor guide scripts.</p>'''
out = os.path.join(R, 'outputs/schemes'); os.makedirs(out, exist_ok=True)
hp = os.path.join(out, f'{LV}_scheme.html'); open(hp, 'w').write(f'<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body>{body}</body></html>')
foot = '<div style="width:100%;font-size:8px;color:#5B6785;padding:0 12mm;display:flex;justify-content:space-between;font-family:Arial"><span>Math Inquirers ' + NAME.split(' (')[0] + ' Scheme of Work  •  Preciouslyours Pte Ltd</span><span>Page <span class="pageNumber"></span></span></div>'
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(); pg.goto('file://' + hp, wait_until='networkidle'); pg.wait_for_timeout(500)
    pg.pdf(path=os.path.join(out, f'Math_Inquirers_Level{N}_Scheme_of_Work.pdf'), format='A4', landscape=True, print_background=True, display_header_footer=True, header_template='<div></div>', footer_template=foot, margin={'top': '12mm', 'bottom': '14mm', 'left': '12mm', 'right': '12mm'})
    b.close()
os.remove(hp); print('scheme built', LV)
