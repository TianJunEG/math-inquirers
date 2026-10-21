import os
css=open('../fonts/fonts.css').read()+open('../hp/doc_style.css').read()+'''
.tb td{font-size:12.6px}
.sc{white-space:nowrap;text-align:center}
.sc span{display:inline-block;width:22px;height:22px;border:1.5px solid #1B2A49;border-radius:5px;margin:0 2px;font:700 11px 'Nunito Sans';line-height:20px;background:#fff}
.box{background:#fff;border:1.5px solid #1B2A49;border-radius:12px;padding:12px 16px;margin:8px 0 12px}
.band{display:grid;grid-template-columns:110px 1fr;gap:0;border:1.5px solid #1B2A49;border-radius:12px;overflow:hidden;margin:8px 0}
.band div{padding:10px 14px;border-top:1px solid #C9D7E6}.band div:nth-child(-n+2){border-top:0}
.band .k{font:600 18px Fredoka;display:flex;align-items:center}
.g{background:#D3F1E4}.y{background:#FFF0C4}.r{background:#FFE2D6}
.child{font-family:Fredoka;font-size:26px}
.child .bx{display:inline-block;width:64px;height:64px;border:3px solid #1B2A49;border-radius:10px;margin:6px 10px 6px 0;background:#fff;vertical-align:middle}
.child h3{font-size:22px;margin-top:22px}
'''
def sc(): return '<td class="sc"><span>0</span><span>1</span><span>2</span></td>'
items=[
('Counting','1','Put about 25 counters in a pile. "Count out 17 for me."','Touches each one once, stops at 17.'),
('Counting','2','Show number cards 9, 14, 17, 20. "Read these numbers."','Reads all four without counting up.'),
('Counting','3','"Write 6, 12 and 19 in the boxes." (child sheet, part A)','Numerals formed correctly, not reversed (12 not 21).'),
('Counting','4','"Count on from 8 to 15." Then: "Count back from 10 to 1."','Starts at 8 without going back to 1; counts back smoothly.'),
('Number sense','5','"Which is more, 13 or 18? How do you know?"','Says 18, and gives a reason ("18 comes after 13", "it has more ones").'),
('Number sense','6','"What is one more than 14? One less than 10?"','15 and 9 without counting from 1.'),
('Number sense','7','Give 7 counters. "Put them into two groups. Can you do it another way?"','Makes 7 in at least two different ways (e.g. 5 and 2, 4 and 3).'),
('Number sense','8','"I have 5 sweets and get 3 more. How many?" Then: "I have 9 and eat 4. How many left?"','8 and 5, with or without counters.'),
('Thinking','9','"Ali has 3 apples. Mei gives him 2 more. How many now? How did you work it out?"','Correct (5) and can say or show how.'),
('Thinking','10','Lay out red, red, blue, red, red, blue. "What comes next? And next?"','Red, red. Can say the rule ("two reds then a blue").'),
('Thinking','11','"2, 4, 6 … what comes next? And next?" (child sheet, part B)','8 and 10. Score 1 if counting by ones to get there.'),
('Thinking','12','Child sheet, part C: "Name these shapes. How many sides does the triangle have?"','Circle, triangle, square, rectangle; 3 sides.'),
]
rows=''.join(f'<tr><td><b>{n}</b></td><td>{s}</td><td>{l}</td>{sc()}</tr>' for a,n,s,l in items)
cover='<div class="cover"><div class="tag">Math Inquirers Holiday Program</div><h1>K2 Readiness Check</h1><div class="sub">A 15-minute check for K2 children who want to join before starting Primary 1</div><div class="slog">Notice it. Test it. Explain why.</div></div>'
p1=cover+'''<h2>Why we check</h2><p>Math Inquirers is built on the Primary 1 syllabus and goes beyond it. K2 children have not met P1 maths yet, so some will fly and some will feel lost. The check tells us who will enjoy the group, who needs a little support first, and who will get more from a later intake. It is short and friendly: children should feel they played some number games.</p>
<h2>How to run it</h2><ul><li><b>Time:</b> about 15 minutes, one child at a time. On video, with the parent setting out the counters beside the child.</li>
<li><b>You need:</b> about 25 counters (buttons or coins are fine), number cards 9, 14, 17 and 20, the child sheet (last page) and a pencil.</li>
<li><b>Parent:</b> may sit in, but asks them not to help or prompt. Online, the parent only moves objects when asked.</li>
<li><b>Tone:</b> say "Let's play some number games." Praise effort, not right answers. Never say "wrong"; say "Let's try another one."</li>
<li><b>Stop early</b> if the child is upset or has scored 0 on four items in a row. Note it and move to the decision.</li></ul>
<h2>Scoring</h2><div class="box"><b>2</b> = correct, without help. &emsp;<b>1</b> = correct with a hint, or slow (counting from 1, using fingers for everything). &emsp;<b>0</b> = not yet, or no answer. Total out of 24.</div>
<h2>Watch for these too</h2><table class="tb"><tr><td class="hd">Behaviour</td><td class="hd">Yes / not yet</td></tr><tr><td>Stays with the task for 15 minutes with only small reminders</td><td></td></tr><tr><td>Follows a two-step instruction ("Count out 7, then put them in two groups")</td><td></td></tr><tr><td>Tries again when stuck instead of giving up</td><td></td></tr><tr><td>Can hold a pencil and write numbers to 20</td><td></td></tr></table>
<div class="brk"></div>
<h2>Script and score sheet</h2><p>Child's name: ______________________ &emsp; Date: ____________ &emsp; Tutor: ______________</p>
<table class="tb"><colgroup><col style="width:5%"><col style="width:46%"><col style="width:33%"><col style="width:16%"></colgroup><tr><td class="hd">#</td><td class="hd">Say or do</td><td class="hd">Look for (2 marks)</td><td class="hd">Score</td></tr>'''+rows+'''<tr><td></td><td colspan="2" style="text-align:right"><b>Total (out of 24)</b></td><td></td></tr></table>
<div class="brk"></div>
<h2>Decision</h2><div class="band"><div class="k g">18–24</div><div class="g"><b>Ready.</b> Joins any group like a Primary 1 child. Tell the tutor in the class list that the child is in K2 and keep an eye on Lessons 5 and 6 (working backwards and money), which are the biggest jump.</div>
<div class="k y">12–17</div><div class="y"><b>Ready with support.</b> Joins, with three conditions: we send the K2 Starter Pack two weeks before the program (numbers to 20, writing numbers, number bonds to 10, coins); the child sits with a buddy; and the tutor sets Core questions first, with Think Harder only when Core is done.</div>
<div class="k r">0–11</div><div class="r"><b>Not yet.</b> Recommend a later intake (the March or June holidays) and give the free home activity sheet. Say it positively: "Your child will get much more out of it after a term of Primary 1."</div></div>
<h3>Override rules</h3><ul><li>Score 0 on item 3 (writing numbers) → <b>Ready with support</b> at best, because the workbook needs writing.</li><li>"Stays with the task" ticked "not yet" → recommend the online group with a parent nearby, or a later intake.</li><li>Child scores 22+ and explains reasons well → note "strong", so the tutor offers Challenge questions early.</li></ul>
<h2>Telling the parent</h2><p>Within a day, send a short message with the result band, one thing the child did well, and the next step. Sample for "Ready with support":</p>
<div class="box"><i>"Thank you for bringing Ethan for the number games today. He counted and compared numbers confidently and loved the pattern game. Primary 1 maths will be new to him, so we will send a short Starter Pack to try at home over the next two weeks, and he will start with the core questions in class. We think he will enjoy the program. His place in Group A is confirmed."</i></div>
<h2>If several K2 children sign up</h2><p>If four or more K2 children register for the same period, consider a separate K2 group. Teach the same ten lessons with smaller numbers (to 20 instead of 100), more objects and fewer written questions. This can grow into a "Little Inquirers" K2 program later.</p>
<div class="brk"></div>
<div class="child"><h2 style="font-size:26px">Number games</h2><p style="font-size:20px">Name: _______________________</p>
<h3>A. Write these numbers</h3><span class="bx"></span><span class="bx"></span><span class="bx"></span>
<h3>B. What comes next?</h3><p>2, &nbsp;4, &nbsp;6, &nbsp;<span class="bx"></span> <span class="bx"></span></p>
<h3>C. Name the shapes</h3><svg viewBox="0 0 640 170" width="100%"><circle cx="80" cy="85" r="62" fill="#D6E9FB" stroke="#1B2A49" stroke-width="5"/><polygon points="240,25 310,150 170,150" fill="#FFF0C4" stroke="#1B2A49" stroke-width="5" stroke-linejoin="round"/><rect x="360" y="35" width="110" height="110" fill="#D3F1E4" stroke="#1B2A49" stroke-width="5"/><rect x="500" y="55" width="130" height="80" fill="#FFE2D6" stroke="#1B2A49" stroke-width="5"/></svg>
<h3>D. Draw what comes next</h3><svg viewBox="0 0 640 90" width="100%">'''+''.join(f'<circle cx="{45+i*70}" cy="45" r="26" fill="{c}" stroke="#1B2A49" stroke-width="4"/>' for i,c in enumerate(['#D64545','#D64545','#3B6FC9','#D64545','#D64545','#3B6FC9']))+''.join(f'<rect x="{462+i*70}" y="19" width="52" height="52" rx="8" fill="#fff" stroke="#1B2A49" stroke-width="3" stroke-dasharray="7 5"/>' for i in range(2))+'''</svg></div>'''
html=f'<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body>{p1}</body></html>'
open('k2.html','w').write(html)
from playwright.sync_api import sync_playwright
ft='<div style="width:100%;font-size:8.5px;color:#5B6785;padding:0 13mm;display:flex;justify-content:space-between;font-family:Arial"><span>Math Inquirers  •  K2 Readiness Check</span><span>Page <span class="pageNumber"></span> of <span class="totalPages"></span></span></div>'
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page();pg.goto('file://'+os.path.abspath('k2.html'));pg.wait_for_timeout(400)
    pg.pdf(path='Math_Inquirers_K2_Readiness_Check.pdf',format='A4',print_background=True,display_header_footer=True,header_template='<div></div>',footer_template=ft,margin={'top':'13mm','bottom':'15mm','left':'13mm','right':'13mm'});b.close()
