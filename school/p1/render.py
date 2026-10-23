"""HTML/CSS for pupil pages, front matter and teacher key. Pure black and white only."""
import html, datetime

FONT = "../../../fonts/node_modules/@fontsource"
CSS = """
@font-face{font-family:'Fredoka';font-weight:500;src:url('FONT/fredoka/files/fredoka-latin-500-normal.woff2') format('woff2')}
@font-face{font-family:'Fredoka';font-weight:600;src:url('FONT/fredoka/files/fredoka-latin-600-normal.woff2') format('woff2')}
@font-face{font-family:'Fredoka';font-weight:700;src:url('FONT/fredoka/files/fredoka-latin-700-normal.woff2') format('woff2')}
@font-face{font-family:'Nunito Sans';font-weight:400;src:url('FONT/nunito-sans/files/nunito-sans-latin-400-normal.woff2') format('woff2')}
@font-face{font-family:'Nunito Sans';font-weight:700;src:url('FONT/nunito-sans/files/nunito-sans-latin-700-normal.woff2') format('woff2')}
@font-face{font-family:'Nunito Sans';font-weight:800;src:url('FONT/nunito-sans/files/nunito-sans-latin-800-normal.woff2') format('woff2')}
@page{size:A4;margin:0}
*{box-sizing:border-box}
html,body{margin:0;padding:0;background:#fff;color:#000;font-family:'Nunito Sans',Arial,sans-serif;font-size:14pt}
.page{width:210mm;height:297mm;padding:15mm;display:flex;flex-direction:column;overflow:hidden;position:relative;break-after:page;background:#fff}
.page:last-child{break-after:auto}
header.ph{display:flex;align-items:center;gap:4mm;border-bottom:0.8mm solid #000;padding-bottom:2.5mm;height:19mm}
.code{font-family:'Fredoka';font-weight:600;font-size:12pt;border:0.5mm solid #000;border-radius:2mm;padding:1mm 2.5mm}
h1{font-family:'Fredoka';font-weight:600;font-size:25pt;margin:0;line-height:1.05;flex:1}
.stars svg{vertical-align:middle;margin-left:0.5mm}
.nameline{font-size:11pt;line-height:1.9;text-align:right;white-space:nowrap}
.nameline span{display:inline-block;border-bottom:0.4mm solid #000;width:36mm}
.topic{font-size:11.5pt;font-weight:700;padding:2mm 0 1mm}
.instr{font-size:15pt;line-height:1.3;padding:1mm 0 2mm}
.instr p{margin:0.4mm 0}
.area{flex:1;min-height:0;display:flex;flex-direction:column;justify-content:space-evenly;padding:2mm 0}
.check{border:0.8mm solid #000;border-radius:3mm;padding:2.5mm 4mm;display:flex;align-items:center;gap:4mm;min-height:24mm;margin-top:2mm}
.check .ct2{flex:1;font-size:14pt;line-height:1.25}
.check .ct2 b{font-family:'Fredoka';font-weight:600;font-size:15pt}
.check .lb{display:flex;gap:1.5mm;align-items:center;flex-wrap:nowrap}
.check .ab{width:11mm;height:12mm}
footer.pf{display:flex;justify-content:space-between;font-size:8pt;padding-top:2mm;line-height:1.2}
footer.pf b{font-weight:800}
p.lead{margin:0 0 2mm;font-size:13pt;font-weight:700}
.blk{display:block}
svg{max-width:100%;height:auto}
.item svg{width:100%}
/* answer bits */
.ab{display:inline-block;width:16mm;height:12.5mm;border:0.6mm solid #000;border-radius:1.5mm;vertical-align:middle;background:#fff}
.ab.sm{width:12mm;height:9mm}
.ab.wide{width:34mm}
.no{display:inline-flex;align-items:center;justify-content:center;width:7.5mm;height:7.5mm;border:0.5mm solid #000;border-radius:50%;font-family:'Fredoka';font-weight:600;font-size:12pt;flex:none}
.op{font-family:'Fredoka';font-weight:600;font-size:18pt}
.codetable{display:flex;flex-wrap:wrap;gap:2.5mm}
.ct{border:0.5mm solid #000;border-radius:1.5mm;padding:0.6mm 2.5mm;font-size:15pt;display:flex;gap:2mm;align-items:center;min-width:25mm;justify-content:center}
.ct .n{font-weight:800}.ct b{font-family:'Fredoka';font-weight:700;font-size:18pt;border-left:0.4mm solid #000;padding-left:2mm}
.items{display:grid;gap:5mm 4mm}.items.g3{grid-template-columns:repeat(3,1fr)}
.item,.citem{display:flex;flex-direction:column;align-items:flex-start;gap:2mm;border:0.4mm solid #000;border-radius:2mm;padding:2.5mm}
.item svg{align-self:center}
.item .ans{align-self:flex-end}
.riddle{display:flex;gap:4mm;align-items:center;margin:2mm 0}
.rtext{flex:1;font-size:15pt;line-height:1.25}
.cards{display:flex;gap:3mm;justify-content:space-between}
.card{width:27mm;height:42mm;border:0.7mm solid #000;border-radius:2.5mm;position:relative;display:flex;align-items:center;justify-content:center}
.card .cn{font-family:'Fredoka';font-weight:600;font-size:30pt}
.card .cl{position:absolute;right:1.5mm;bottom:1mm;font-weight:800;font-size:13pt;border:0.4mm solid #000;border-radius:50%;width:7mm;height:7mm;display:flex;align-items:center;justify-content:center}
.orderrow{display:flex;align-items:center;gap:3mm;font-weight:700;font-size:13pt}
.arrowline{flex:1;border-top:0.8mm solid #000;position:relative;height:0}
.arrowline:after{content:'';position:absolute;right:0;top:-2mm;border-left:4mm solid #000;border-top:2mm solid transparent;border-bottom:2mm solid transparent}
.slots{display:grid;grid-template-columns:repeat(6,1fr);gap:3mm;justify-items:center}
.slot{display:flex;flex-direction:column;align-items:center;gap:2mm}
.slot .ab{width:25mm;height:22mm}.slot .ab.letter{height:20mm}
.slotlabels{display:flex;justify-content:space-between;font-size:11pt;font-weight:700;padding:0 2mm}
.chips{display:flex;gap:4mm;flex-wrap:wrap}.chip{border:0.6mm solid #000;border-radius:6mm;padding:1mm 5mm;font-family:'Fredoka';font-weight:600;font-size:20pt}
ul.clues{margin:0;padding-left:7mm;font-size:15pt;line-height:1.5}
ul.clues li{margin:1mm 0}
table.lgrid{border-collapse:collapse}table.lgrid th,table.lgrid td{border:0.5mm solid #000;font-size:12.5pt;padding:0 2mm}
table.lgrid td{width:15mm;height:13mm}table.lgrid th{font-weight:800}table.lgrid th.rh{text-align:left;width:22mm}
.twocol{display:flex;gap:8mm;align-items:flex-start}.twocol>div:last-child{flex:1}
.ansline{font-size:15pt;margin:3mm 0;line-height:2.1;white-space:nowrap}
.seqs{display:flex;flex-direction:column;gap:5mm}
.seq{display:flex;gap:2.5mm;align-items:center}
.sq{width:21mm;height:13mm;border:0.5mm solid #000;display:inline-flex;align-items:center;justify-content:center;font-family:'Fredoka';font-weight:600;font-size:19pt}
.seq .ab{width:21mm;height:13mm}
.maze{display:grid;width:170mm;margin:0 auto;border:0.8mm solid #000}
.mcell{border:0.5mm solid #000;height:31mm;display:flex;align-items:center;justify-content:center;position:relative;font-family:'Fredoka';font-weight:600;font-size:22pt}
.flag{position:absolute;left:0;top:0;background:#000;color:#fff;font-style:normal;font-family:'Nunito Sans';font-weight:800;font-size:8.5pt;padding:0.6mm 2mm;letter-spacing:.3mm}
.magic{display:grid;grid-template-columns:repeat(3,29mm) 20mm;grid-auto-rows:29mm;gap:0;margin:0 auto;width:max-content}
.mc{border:0.9mm solid #000;display:flex;align-items:center;justify-content:center;font-family:'Fredoka';font-weight:700;font-size:32pt}
.msum{display:flex;align-items:center;justify-content:center}
.diag{text-align:center;font-size:14pt}
.ovals{display:flex;gap:3mm;justify-content:center}.oval{width:13mm;height:13mm;border:0.5mm solid #000;border-radius:50%;display:flex;align-items:center;justify-content:center;font-family:'Fredoka';font-weight:600;font-size:17pt}
.cgrid{display:grid;width:170mm;margin:0 auto;border:0.8mm solid #000}
.ccell{border:0.5mm solid #000;height:var(--ch,28mm);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:1.5mm;font-size:17pt}
.ccell .ex{font-family:'Fredoka';font-weight:600;font-size:18pt}
.ccell .eqsign{display:none}
.ccell .ln{display:inline-block;width:17mm;border-bottom:0.5mm solid #000;height:7mm}
.sumrows{display:grid;gap:5mm 6mm}.sumrows.two{grid-template-columns:1fr 1fr}
.sumrow{display:flex;align-items:center;gap:3mm;font-family:'Fredoka';font-weight:500;font-size:24pt;height:27mm;border-bottom:0.3mm solid #000}
.shblock{display:flex;gap:8mm;align-items:center;border:0.4mm solid #000;border-radius:2mm;padding:3mm 5mm}
.eqs{flex:1;display:flex;flex-direction:column;gap:3mm}
.eq{display:flex;align-items:center;gap:2mm;font-family:'Fredoka';font-weight:600;font-size:20pt;height:12mm}
.shansw{display:flex;flex-direction:column;gap:2mm;border-left:0.5mm solid #000;padding-left:6mm}
.shans{display:flex;align-items:center;gap:2mm}
.shans .ab{width:15mm;height:11mm}
.grows,.crows,.lrows{display:flex;flex-direction:column;gap:3mm}
.grow,.crow,.lrow{display:flex;align-items:center;gap:3mm;border-bottom:0.3mm solid #000;padding-bottom:2mm}
.gsvg{width:100mm;flex:none}.geq{margin-left:auto;display:flex;align-items:center;gap:2mm}.geq .ab{width:14mm}
.csvg{flex:1}.cans{display:flex;align-items:center;gap:2mm;font-size:16pt}
.lsvg{flex:none}.lsvg svg{max-width:none}.unit{font-size:14pt;font-weight:700}
.citem{flex-direction:row;align-items:center;gap:3mm;border:none;padding:0}.citem svg{width:36mm;flex:none}.cmid{display:flex;flex-direction:column;gap:2mm}
.cq{font-size:12.5pt;line-height:1.2}.items.g2{grid-template-columns:1fr 1fr;gap:4mm 6mm}
.ctime{font-size:18pt;font-weight:800}.ctime .ab{width:13mm;height:11mm}
.figwrap{text-align:center}
.srows{display:flex;gap:2mm;justify-content:space-between}
.srow{display:flex;align-items:center;gap:1mm}.srow svg{width:11mm}.srow .ab{width:12mm;height:11mm}
.pgraph{display:flex;flex-direction:column;gap:4mm}
.grow2{display:flex;align-items:center}
.gl{width:28mm;font-size:15pt}
.gc{width:16mm;height:16mm;border:0.5mm solid #000;display:inline-flex;align-items:center;justify-content:center;margin-right:-0.5mm}
.dotc{display:inline-block;width:10.5mm;height:10.5mm;border-radius:50%;background:#000}
.dotc.inl{width:4.5mm;height:4.5mm;vertical-align:middle}
.kids{display:flex;justify-content:space-between}.kid{display:flex;flex-direction:column;align-items:center;font-size:14pt}
.qslots{display:flex;flex-direction:column;gap:2.5mm}.qslot{display:flex;align-items:center;gap:4mm;font-size:16pt;font-weight:800}.qslot .qn{width:14mm}.qslot .ab.wide{width:60mm}
/* front matter and key */
.fm{font-size:13pt;line-height:1.4}
.fm h2{font-family:'Fredoka';font-weight:600;font-size:22pt;margin:0 0 4mm;border-bottom:0.8mm solid #000;padding-bottom:2mm}
.fm h3{font-family:'Fredoka';font-weight:600;font-size:14pt;margin:5mm 0 1.5mm}
.fm p{margin:1.5mm 0}.fm ul{margin:1mm 0 1mm 6mm;padding:0}
.cover{justify-content:space-between;text-align:center}
.cover .big{font-family:'Fredoka';font-weight:700;font-size:44pt;line-height:1.05}
.cover .sub{font-size:18pt}
.cover .box{border:1mm solid #000;border-radius:5mm;padding:6mm;font-size:15pt}
.cover .school{border-bottom:0.6mm solid #000;font-size:20pt;font-weight:800;padding:2mm 6mm;display:inline-block;min-width:110mm}
table.tbl{border-collapse:collapse;width:100%;font-size:10.5pt}
table.tbl th,table.tbl td{border:0.4mm solid #000;padding:1.2mm 2mm;text-align:left;vertical-align:top}
table.tbl th{font-weight:800;border-bottom:0.8mm solid #000}
.kentry{border:0.5mm solid #000;border-radius:2mm;padding:3mm 4mm;margin-bottom:4mm;font-size:10.5pt;line-height:1.3;break-inside:avoid}
.kentry h4{font-family:'Fredoka';font-weight:600;font-size:13pt;margin:0 0 1.5mm}
.kentry .tags{font-weight:700;margin-bottom:1mm}
.kentry .row{display:flex;gap:4mm}.kentry .row>div:first-child{flex:1}
.kmini{display:grid;gap:0;border:0.5mm solid #000}.kmini i{width:4mm;height:4mm;border:0.25mm solid #000;display:block}.kmini i.on{background:#000}
"""

def stars_svg(n):
    one = ('<svg xmlns="http://www.w3.org/2000/svg" width="8mm" height="8mm" viewBox="-10 -10 20 20"><polygon fill="#000" stroke="#000" stroke-width="0.6" points="'
           + " ".join(f"{(10 if i%2==0 else 4.2)*__import__('math').cos(-__import__('math').pi/2+i*__import__('math').pi/5):.2f},{(10 if i%2==0 else 4.2)*__import__('math').sin(-__import__('math').pi/2+i*__import__('math').pi/5):.2f}" for i in range(10))
           + '"/></svg>')
    return f'<span class="stars" title="{n} star">{one*n}</span>'

def tick_svg():
    return ('<svg xmlns="http://www.w3.org/2000/svg" width="11mm" height="11mm" viewBox="0 0 20 20"><circle cx="10" cy="10" r="9" fill="#fff" stroke="#000" stroke-width="1.3"/>'
            '<polyline points="5,10.5 8.8,14.2 15,6" fill="none" stroke="#000" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>')

def footer(code, school):
    lic = (f"Photocopy licence: <b>{html.escape(school)}</b> only." if school.strip()
           else "Photocopy licence: <b>________________________</b> (school name) only.")
    return (f'<footer class="pf"><span>&copy; 2026 Preciouslyours Pte Ltd. {lic} Not for resale.</span><span><b>{code}</b></span></footer>')

def pupil_page(p, school):
    code = f"P1-{p['no']:02d}"
    instr = "".join(f"<p>{html.escape(s)}</p>" for s in p["instr"])
    lb = ""
    if p.get("check_boxes"):
        lb = '<div class="lb">' + '<span class="ab"></span>' * p["check_boxes"] + "</div>"
    style = ' style="--ch:%smm"' % ("31" if p["no"] in (12,) else "26") if p["no"] in (12, 14) else ""
    return (f'<section class="page"{style}><header class="ph"><span class="code">{code}</span><h1>{html.escape(p["title"])}</h1>'
            f'{stars_svg(p["tier"])}<div class="nameline">Name <span></span></div></header>'
            f'<div class="topic">Topic: {html.escape(p["topic"])}</div><div class="instr">{instr}</div>'
            f'<div class="area">{p["body"]}</div>'
            f'<div class="check">{tick_svg()}<div class="ct2"><b>Check it.</b> {html.escape(p["check"])}</div>{lb}</div>'
            f'{footer(code, school)}</section>')

def doc(pages_html, title):
    return (f'<!doctype html><html lang="en-GB"><head><meta charset="utf-8"><title>{html.escape(title)}</title>'
            f'<style>{CSS.replace("FONT", FONT)}</style></head><body>{pages_html}</body></html>')

# ------------------------------------------------------------------ front matter
def cover(school):
    s = html.escape(school) if school.strip() else "&nbsp;"
    return ('<section class="page cover fm"><div><p class="sub" style="margin-top:14mm">Maths puzzles for early finishers</p>'
            '<div class="big" style="margin-top:6mm">Early Finisher Puzzles</div><div class="big" style="font-size:36pt;margin-top:3mm">Primary 1</div></div>'
            '<div class="box">20 single-page puzzles<br>Every puzzle checks itself<br>One star and two star pages<br>Teacher answer key included</div>'
            f'<div><p style="font-size:13pt;margin:0 0 2mm">This pack belongs to</p><span class="school">{s}</span>'
            '<p style="margin-top:14mm;font-size:12pt">Preciouslyours Pte Ltd</p></div></section>')

def licence(school):
    s = html.escape(school) if school.strip() else "____________________________"
    return ('<section class="page fm"><h2>Photocopy licence</h2>'
            f'<p><b>Licensed to:</b> {s} (one school, one campus)</p>'
            '<h3>You may</h3><ul><li>Print this PDF and photocopy any page for the pupils and staff of the school named above.</li>'
            '<li>Keep the file on the school network and share it with the school\'s teachers.</li>'
            '<li>Hand a single page to a pupil, or keep a tray of pages in the classroom.</li></ul>'
            '<h3>You may not</h3><ul><li>Sell, lend or give the pages or the file to another school, tuition centre or person.</li>'
            '<li>Post the file or pages on a public website or a shared platform outside the school.</li>'
            '<li>Edit the pages, or remove the licence line at the foot of each page.</li></ul>'
            '<h3>Printed copies</h3><p>Bound or loose-leaf printed sets can be ordered in bulk. Ask the publisher for a quote.</p>'
            '<h3>Notes</h3><p>The licence is for the edition bought. The school name shown on each page is set when the pack is made.</p>'
            '<p style="margin-top:12mm">&copy; 2026 Preciouslyours Pte Ltd. All rights reserved.</p></section>')

def teacher_notes(pages):
    n1 = sum(1 for p in pages if p["tier"] == 1); n2 = len(pages) - n1
    return ('<section class="page fm"><h2>Teacher notes</h2>'
            '<h3>What this is</h3><p>Twenty single-page maths puzzles for Primary 1 pupils who finish their work early. Each page stands alone, so you can hand out one page or keep a tray of pages. The pupil needs no help to start.</p>'
            f'<h3>Stars</h3><p>One star pages practise a topic as it is usually taught ({n1} pages). Two star pages use the same topics with more steps or more clues ({n2} pages). Pages can be used in any order.</p>'
            '<h3>Every page checks itself</h3><p>The boxed strip at the foot of each page tells the pupil how to check. The check shows that something is wrong. It does not give the answer.</p>'
            '<ul><li><b>Code word.</b> The answers give letters that spell a word.</li><li><b>Hidden picture.</b> Shading the right boxes makes a picture.</li>'
            '<li><b>Route.</b> The path must reach FINISH.</li><li><b>Grid.</b> One tick in each row and column.</li><li><b>Total.</b> Every line or the whole count must make the stated total.</li></ul>'
            '<p>Marking is not needed. To spot-check, look only at the check strip.</p>'
            '<h3>Photocopying</h3><p>All pages are black and white with solid lines, so they copy cleanly. Each page is one side only; the back of a copy stays blank. Pupils write on the page: the boxes are large for young hands. Use A4.</p>'
            '<h3>What is in this pack</h3><table class="tbl"><tr><th>Part</th><th>Pages</th><th>Photocopy for pupils?</th></tr>'
            '<tr><td>Cover</td><td>1</td><td>No</td></tr><tr><td>Photocopy licence</td><td>1</td><td>No</td></tr>'
            '<tr><td>Teacher notes</td><td>1</td><td>No</td></tr><tr><td>Contents</td><td>1</td><td>No</td></tr>'
            '<tr><td>Puzzle pages P1-01 to P1-20</td><td>20</td><td>Yes</td></tr>'
            '<tr><td><b>Complete pack to print</b></td><td><b>24</b></td><td>The teacher answer key is a separate file (8 pages).</td></tr></table>'
            '</section>')

def contents(pages):
    rows = "".join(f'<tr><td>P1-{p["no"]:02d}</td><td>{html.escape(p["title"])}</td><td>{html.escape(p["topic"])}</td><td>{"1 star" if p["tier"]==1 else "2 stars"}</td></tr>' for p in pages)
    return ('<section class="page fm"><h2>Contents</h2><table class="tbl"><tr><th>Page</th><th>Puzzle</th><th>Topic</th><th>Tier</th></tr>'
            + rows + '</table><p style="margin-top:4mm;font-size:11pt">Pages are independent. Pick any page.</p></section>')

# ------------------------------------------------------------------ teacher key
def mini_mask(mask):
    n = len(mask[0]); cells = "".join(f'<i class="{"on" if ch=="#" else ""}"></i>' for r in mask for ch in r)
    return f'<div class="kmini" style="grid-template-columns:repeat({n},4mm);width:max-content">{cells}</div>'

def key_entry(p):
    extra = ""
    if "mask" in p: extra = mini_mask(p["mask"])
    vs = p.get("verify", [])
    ok = sum(1 for _, o, _ in vs if o)
    return (f'<div class="kentry"><h4>P1-{p["no"]:02d} {html.escape(p["title"])} &nbsp; {"1 star" if p["tier"]==1 else "2 stars"}</h4>'
            f'<div class="tags">Topic: {html.escape(p["topic"])}</div>'
            f'<div>Syllabus: {html.escape(p["strand"])}; outcomes {html.escape(p["syll"])}</div>'
            f'<div>Puzzle type: {html.escape(p["ptype"])}. Self-check: {html.escape(p["mech"])}.</div>'
            f'<div class="row"><div><b>Answers:</b> {html.escape(p["key"]["answers"])}<br><b>Check result:</b> {html.escape(p["key"]["check_result"])}</div>{extra}</div>'
            f'<div><b>Teacher note:</b> {html.escape(p["note"])}</div>'
            f'<div style="font-size:9pt">Script checks passed: {ok} of {len(vs)}.</div></div>')

def key_pages(pages, school):
    out = ['<section class="page fm"><h2>Teacher answer key: Primary 1</h2>'
           '<p>This key lists the answers and the result of the check on every page. You do not need it for routine marking: a pupil who has a working check has the right answers. To spot-check, compare the check strip with the line "Check result" below.</p>'
           '<h3>How the topic tags work</h3><p>Each entry names the Primary 1 topic strand and the syllabus outcome numbers the puzzle practises (Mathematics Syllabus, Primary, 2021 edition; Primary 1, pages 31 and 32). Outcome numbers are in this key only and not on the pupil pages.</p>'
           '<h3>Topic coverage</h3><table class="tbl"><tr><th>Strand</th><th>Pages</th></tr>'
           + "".join(f'<tr><td>{html.escape(k)}</td><td>{", ".join("P1-%02d" % x for x in v)}</td></tr>' for k, v in strand_map(pages).items())
           + '</table><p style="font-size:10pt;margin-top:4mm">Syllabus items not covered by a puzzle: reading and writing numbers in words, number-sentence signs in isolation, measuring and drawing a line to the nearest cm, am and pm, copying figures on a grid, forming figures from shapes. Teachers may wish to tell the pupils these topics are covered in class work.</p></section>']
    per = 3
    for i in range(0, len(pages), per):
        out.append('<section class="page fm" >' + "".join(key_entry(p) for p in pages[i:i + per]) + footer("KEY", school).replace("Photocopy licence", "Teacher key. Photocopy licence") + "</section>")
    return "".join(out)

def strand_map(pages):
    m = {}
    for p in pages:
        m.setdefault(p["strand"], []).append(p["no"])
    return m
