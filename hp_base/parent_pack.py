# Weekly Dose of Thinking Math: the parent practice pack, parent edition style (B, "Magazine"; see parent_style.css). Built from qbank.json and lessons.js.
# Run in hp/:  python3 parent_pack.py   ->  Math_Inquirers_Weekly_Dose_of_Thinking_Math.pdf
import json, html, os, subprocess
from playwright.sync_api import sync_playwright
E = html.escape
Q = json.load(open('qbank.json'))
info = json.loads(subprocess.run(['node', '-e', "const L=require('./lessons.js');console.log(JSON.stringify(L.lessons.map(l=>({n:l.n,title:l.title,topic:l.topic}))))"],
                                 capture_output=True, text=True, check=True).stdout)
PICK = {'core': 4, 'stretch': 3, 'challenge': 2}
LEVEL = {'core': 'Core', 'stretch': 'Think Harder', 'challenge': 'Challenge'}
# per lesson: what your child learns, a tip for the parent, a question to ask
SIDE = {
 1: ('Counting in 2s, 3s and 5s, and finding the rule of a pattern that goes up or down.',
     'Hop a coin along a paper number line. Ask your child to say the rule out loud before writing the next number.',
     '"What is the rule? Does it work for every pair?"'),
 2: ('Number bonds of 10 and 20, and reading = as "is the same as" on both sides.',
     'Split 10 buttons into two groups in every possible way. List them in order so none is missed.',
     '"How do you know both sides are the same?"'),
 3: ('Reading picture graphs where one picture can stand for 1, 2 or 3 children, comparing rows and finding totals.',
     'Hold a family vote (favourite fruit or snack) and draw it together, one picture per vote.',
     '"What does one picture stand for?"'),
 4: ('Finding the part of a pattern that repeats, predicting far-away places, and growing patterns with a table.',
     'Make a pattern with spoons and forks. Ask what the 10th one will be before you build it.',
     '"Which part repeats? How many things are in it?"'),
 5: ('Working backwards: undoing each step, from the last step to the first.',
     'Hide some counters under a cup, add a few more on top, and let your child work out how many were hidden.',
     '"How can you check by going forwards?"'),
 6: ('Finding every way to make an amount, and paying with the fewest coins and notes, in cents and in dollars.',
     'Lay real coins and notes on the table. Ask "Can you do it with fewer?" before checking the answer.',
     '"How do you know you found them all?"'),
 7: ('Describing shapes by sides and corners, counting every shape in a picture, and making new shapes.',
     'Fold and cut a paper square. What shapes can your child make by putting the pieces together again?',
     '"Did you count the bigger shapes too?"'),
 8: ('Using clues to put things in order, sorting with two rules, and solving small logic grids.',
     'Play "Guess my number" from 1 to 20 with yes or no questions. Which questions help most?',
     '"Which clue tells you something for sure?"'),
 9: ('Measuring with equal units and a centimetre ruler, comparing lengths, and changing from one unit to another.',
     'Measure a spoon with paper clips, then with erasers. Talk about why the two numbers are different.',
     '"Why does a bigger unit give a smaller number?"'),
 10: ('Choosing how to start a puzzle: draw it, list it in order, or make a table.',
      'When your child is stuck, ask "Can you draw it?" before giving any other hint.',
      '"How did you start? What would you try next time?"'),
}

def q(n, text, lines):
    return f'<div class="q"><span class="n">{n}</span><div>{E(text)}' + '<div class="ln"></div>' * lines + '</div></div>'

shapes = ('<svg viewBox="0 0 680 210" width="100%" aria-label="Shapes">'
          '<g transform="translate(70,80) rotate(-10)"><rect x="-44" y="-44" width="88" height="88" fill="#FFC93C" stroke="#1B2A49" stroke-width="4"/></g>'
          '<polygon points="230,30 290,140 170,140" fill="#1F7A6F" stroke="#1B2A49" stroke-width="4"/>'
          '<g transform="translate(420,90) rotate(8)"><rect x="-70" y="-34" width="140" height="68" fill="#DDEBF7" stroke="#1B2A49" stroke-width="4"/></g>'
          '<polygon points="600,30 655,90 600,150 545,90" fill="#D64545" stroke="#1B2A49" stroke-width="4"/></svg>')
B = []
B.append(f'''<div class="cover"><div class="kick">For parents  •  Primary 1</div>
<div class="ctitle">Weekly Dose of<br><span>Thinking Math</span></div>
<div class="lede">One dose a week for five weeks: short sets of questions for every Math Inquirers lesson, a tip for you, and the answers at the back.</div>
<div class="rule"></div>{shapes}
<div class="bottom"><div class="slogan">Notice it. Test it. Explain why.</div><div class="by">Math Inquirers Holiday Program<br>Preciouslyours Pte Ltd</div></div></div>''')
B.append('''<div class="pb"><div class="kick">Before you start</div><div class="hd"><div class="big">00</div><div><div class="tp">For grown-ups</div><h1>How to help</h1></div></div>
<ol class="tips">
<li><div><b>Ask before you tell.</b> Start with "What do you notice?" and let your child answer first.</div></li>
<li><div><b>Use real things.</b> Coins, notes, buttons, spoons, pasta or blocks. Try it with objects before writing.</div></li>
<li><div><b>Give hints in three steps.</b> Look again. Try it with objects. Try a smaller example. Say the answer last.</div></li>
<li><div><b>Ask "How do you know?"</b> even when the answer is right. The reason matters as much as the answer.</div></li>
<li><div><b>Praise the thinking.</b> "I like how you checked that" works better than "You are clever".</div></li>
<li><div><b>Keep it short.</b> Ten minutes and two or three questions is enough. Stop while it is still fun.</div></li>
<li><div><b>Answers are at the back.</b> Look only after your child has tried.</div></li>
</ol>
<div class="quote">Hard question? Great. Getting stuck is where the thinking happens.</div>
<div class="panel"><h3>One dose a week</h3><p style="margin:0">Each week has two lessons and about 18 questions. Do two or three a day, Monday to Friday, and keep the weekend for the Challenge questions if your child enjoys them.</p></div>
<div class="panel"><h3>The three levels</h3><p style="margin:0"><b>Core</b> is for everyone. <b>Think Harder</b> stretches the idea. <b>Challenge</b> is for strong thinkers, and it is fine to leave it for another day.</p></div>
<div class="panel"><h3>What your child is doing in class</h3><p style="margin:0">Ten 90-minute lessons over five weeks. Each lesson starts with a hands-on puzzle, then a short teaching part, then the workbook. These pages practise the same ideas at home.</p></div></div>''')
for L in info:
    n = L['n']; b = Q[str(n)]; learn, tip, ask = SIDE[n]
    h = f'<div class="pb"><div class="kick">Weekly Dose of Thinking Math  •  Week {(n+1)//2}</div><div class="hd"><div class="big">W{(n+1)//2}</div><div><div class="tp">Lesson {n}  •  {E(L["topic"])}</div><h1>{E(L["title"])}</h1></div></div><div class="cols"><div>'
    k = 1
    for lev, cnt in PICK.items():
        h += f'<div class="lv">{LEVEL[lev]}</div>'
        for item in b[lev][:cnt]:
            h += q(k, item['q'], 2 if lev == 'core' else 3); k += 1
    h += f'</div><div class="side"><h3>What your child learns</h3><p>{E(learn)}</p><h3>Tip for you</h3><p>{E(tip)}</p><h3>Ask</h3><p>{E(ask)}</p></div></div></div>'
    B.append(h)
h = '<div class="pb"><div class="kick">Look after your child has tried</div><div class="hd"><div class="big">✓</div><div><div class="tp">All lessons</div><h1>Answers</h1></div></div><div class="acols">'
for L in info:
    b = Q[str(L['n'])]; k = 1; rows = ''
    for lev, cnt in PICK.items():
        for item in b[lev][:cnt]:
            rows += f'<div class="ar"><b>{k}</b><span>{E(item["a"])}</span></div>'; k += 1
    h += f'<div class="ablk"><h3>Week {(L["n"]+1)//2}  •  Lesson {L["n"]}: {E(L["title"])}</h3>{rows}</div>'
B.append(h + '</div></div>')

css = open('../fonts/fonts.css').read() + open('parent_style.css').read()
open('parent_pack.html', 'w').write(f'<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body>{chr(10).join(B)}</body></html>')
foot = '<div style="width:100%;font-size:9px;color:#5B6785;padding:0 16mm;display:flex;justify-content:space-between;font-family:Arial"><span>Weekly Dose of Thinking Math  •  Math Inquirers</span><span>Page <span class="pageNumber"></span></span></div>'
with sync_playwright() as p:
    br = p.chromium.launch(); pg = br.new_page()
    pg.goto('file://' + os.path.abspath('parent_pack.html'), wait_until='networkidle'); pg.wait_for_timeout(800)
    pg.pdf(path='Math_Inquirers_Weekly_Dose_of_Thinking_Math.pdf', format='A4', print_background=True, display_header_footer=True,
           header_template='<div></div>', footer_template=foot, margin={'top': '16mm', 'bottom': '18mm', 'left': '16mm', 'right': '16mm'})
    br.close()
os.remove('parent_pack.html')
print('weekly dose built')
