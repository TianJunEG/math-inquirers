# Scheme of Work PDF for a level:  python3 levels/scheme.py p2   ->  outputs/schemes/Math_Inquirers_P2_Scheme_of_Work.pdf
import sys, json, subprocess, os, html
from playwright.sync_api import sync_playwright
E = html.escape
LV = sys.argv[1]; N = LV[1:]; R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src = os.path.join(R, 'hp/lessons.js') if LV == 'p1' else os.path.join(R, LV, 'data.js')
js = "const L=require(process.argv[1]);const a=L.lessons;console.log(JSON.stringify(a))"
ls = json.loads(subprocess.run(['node', '-e', js, src], capture_output=True, text=True, check=True).stdout)
NAME = {'1': 'Primary 1', '2': 'Primary 2', '3': 'Primary 3', '4': 'Primary 4', '5': 'Primary 5', '6': 'Primary 6 (after the PSLE): Maths and Coding Bridge'}[N]
FOR = {'1': 'ages 6 to 8 (builds on Primary 1 maths)', '2': 'ages 7 to 9 (builds on Primary 2 maths)', '3': 'ages 8 to 10 (builds on Primary 3 maths)', '4': 'ages 9 to 11 (builds on Primary 4 maths)', '5': 'ages 10 to 12 (builds on Primary 5 maths)', '6': 'ages 11 to 13, after the PSLE'}[N]
BUD = json.load(open(os.path.join(R, 'hp' if LV == 'p1' else LV, 'budget.json')))['lessons']
def fm(x): return ('%g' % round(x, 2))
def clean(t): return t.split(' (')[0] if '; ' in t else t
def plan(n):
    return ' &middot; '.join(f'{E(clean(p["title"]))} <b>{fm(p["end"] - p["start"])}</b>' for p in BUD[str(n)]['parts'])
def routine():
    # typical minutes for each part of lessons 1 to 9 (lesson 10 has its own plan), from the same budget.json the tutor guide reads
    out = []
    for p in BUD['1']['parts']:
        d = [q['end'] - q['start'] for k in range(1, 10) for q in BUD[str(k)]['parts'] if q['title'] == p['title']]
        lo, hi = min(d), max(d)
        out.append(f'{E(clean(p["title"]).lower() if out else clean(p["title"]))} ({fm(lo) if lo == hi else fm(lo) + " to " + fm(hi)})')
    return ', '.join(out[:-1]) + ', and ' + out[-1]
def sk(x): return E(x if isinstance(x, str) else '; '.join(x))
rows = ''
for l in ls:
    rows += (f'<tr><td class="n">{l["n"]}<small>Week {(l["n"]+1)//2}{"AB"[(l["n"]+1)%2]}</small></td><td><b>{E(l["title"])}</b><br><span class="tp">{E(l["topic"])}</span></td>'
             f'<td>{E(l["objective"])}</td><td>{sk(l["skills"])}</td><td>{E(l["exit"]["q"] if isinstance(l.get("exit"), dict) else l.get("exit",""))}</td></tr>'
             f'<tr class="pl"><td></td><td colspan="4"><b>Time plan (minutes):</b> {plan(l["n"])}</td></tr>')
css = open(os.path.join(R, 'fonts/fonts.css')).read() + '''
@page{size:A4 landscape;margin:12mm}
body{font-family:'Nunito Sans',Arial;color:#1B2A49;font-size:10.5px;line-height:1.35}
h1{font-family:Fredoka,Arial;font-size:26px;margin:0 0 2px}.sub{color:#1F7A6F;font-weight:800;margin-bottom:8px}
.box{border-left:4px solid #FFC93C;background:#FFF9EC;padding:6px 10px;margin:6px 0 10px}
table{border-collapse:collapse;width:100%}th{background:#1B2A49;color:#fff;text-align:left;padding:5px 6px;font-size:10px}
td{border-bottom:1px solid #D9DEE9;padding:5px 6px;vertical-align:top}td.n{font-family:Fredoka;font-size:20px;color:#D64545;width:44px}td.n small{display:block;font-family:'Nunito Sans';font-size:8px;color:#5B6785}
.tp{color:#5B6785;font-size:9.5px}h2{font-family:Fredoka;font-size:15px;margin:12px 0 4px}tr{break-inside:avoid}tr.pl td{font-size:9px;color:#33415f;background:#F6F8FC;border-bottom:1px solid #B8C0D4}
'''
# P1 audit (P-1, P-6): say what the program does not cover
COVER = '<br><b>Coverage.</b> This is enrichment. It does not teach time, multiplication and division, or 2-digit addition and subtraction within 100, so parents should not expect it to cover the whole Primary 1 syllabus.' if LV == 'p1' else ''
body = f'''<h1>Math Inquirers {NAME}: Scheme of Work</h1><div class="sub">Holiday program for {FOR}  •  10 lessons of 90 minutes  •  2 lessons a week for 5 weeks  •  live online, up to 8 children</div>
<div class="box"><b>Approach.</b> Enrichment, not extra drill: non-routine puzzles on topics chosen to complement the school syllabus. Lessons 1 to 9 follow the same routine, in minutes of the 90: {routine()}. Lesson 10 has its own plan. The time plan under each lesson is the one in the tutor guide.<br><b>Habits.</b> Notice it. Test it. Explain why.{COVER}</div>
<table><thead><tr><th>Lesson</th><th>Title and school topic</th><th>Objective</th><th>Skills and heuristics practised</th><th>Exit ticket</th></tr></thead><tbody>{rows}</tbody></table>
<h2>Assessment and progress</h2><p>Each lesson has a 2-page Start here worksheet, then Think harder, Go further and an Investigation with a Look-back (printed for every child, who may choose any of them at any time; nobody is placed in a group), an exit ticket and an Inquiry Journal stamp. Tutors record S (secure), D (developing) or H (needs help) for each child on the progress tracker in the tutor guide. Parents receive a short note each week and the Weekly Dose of Thinking Math practice pack.</p>
<h2>Materials</h2><p>Printed student workbook with cut-outs, pencil, scissors and paper; a laptop or tablet with a camera. Tutors use the slides for each lesson and the tutor guide scripts.</p>'''
out = os.path.join(R, 'outputs/schemes'); os.makedirs(out, exist_ok=True)
hp = os.path.join(out, f'{LV}_scheme.html'); open(hp, 'w').write(f'<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body>{body}</body></html>')
foot = '<div style="width:100%;font-size:8px;color:#5B6785;padding:0 12mm;display:flex;justify-content:space-between;font-family:Arial"><span>Math Inquirers ' + NAME.split(' (')[0] + ' Scheme of Work  •  Preciouslyours Pte Ltd</span><span>Page <span class="pageNumber"></span></span></div>'
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(); pg.goto('file://' + hp, wait_until='networkidle'); pg.wait_for_timeout(500)
    pg.pdf(path=os.path.join(out, f'Math_Inquirers_P{N}_Scheme_of_Work.pdf'), format='A4', landscape=True, print_background=True, display_header_footer=True, header_template='<div></div>', footer_template=foot, margin={'top': '12mm', 'bottom': '14mm', 'left': '12mm', 'right': '12mm'})
    b.close()
os.remove(hp); print('scheme built', LV)
