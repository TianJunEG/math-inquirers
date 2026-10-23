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
footer.pf{display:flex;justify-content:space-between;gap:6mm;font-size:8pt;padding-top:2mm;line-height:1.2}
footer.pf b{font-weight:800}
footer.pf .fl{display:flex;gap:1.2mm;flex:1;min-width:0}footer.pf .fx{white-space:nowrap;flex:none}footer.pf .sn{min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;font-weight:800}footer.pf .pc{flex:none}
p.lead{margin:0 0 2mm;font-size:13pt;font-weight:700}
.blk{display:block}
svg{max-width:100%;height:auto}
.item svg{width:100%}
.items.g3 .item svg{width:86%}
/* answer bits */
.ab{display:inline-block;width:16mm;height:12.5mm;border:0.6mm solid #000;border-radius:1.5mm;vertical-align:middle;background:#fff}
.ab.sm{width:14mm;height:12mm}
.ab.wide{width:34mm}
.no{display:inline-flex;align-items:center;justify-content:center;width:7.5mm;height:7.5mm;border:0.5mm solid #000;border-radius:50%;font-family:'Fredoka';font-weight:600;font-size:12pt;flex:none}
.op{font-family:'Fredoka';font-weight:600;font-size:18pt}
.codetable{display:flex;flex-wrap:wrap;gap:2.5mm}
.ct{border:0.5mm solid #000;border-radius:1.5mm;padding:0.6mm 2.5mm;font-size:15pt;display:flex;gap:2mm;align-items:center;min-width:25mm;justify-content:center}
.ctl{font-size:12pt;align-self:center;margin-right:1mm}
.ct .n{font-weight:800}.ct b{font-family:'Fredoka';font-weight:700;font-size:18pt;border-left:0.4mm solid #000;padding-left:2mm}
.items{display:grid;gap:5mm 4mm}.items.g3{grid-template-columns:repeat(3,1fr)}
.item,.citem{display:flex;flex-direction:column;align-items:flex-start;gap:1.5mm;border:0.4mm solid #000;border-radius:2mm;padding:2mm 2.5mm}
.item svg{align-self:center}
.item .ans{align-self:flex-end}
.riddle{display:flex;gap:4mm;align-items:center;margin:2mm 0}
.rtext{flex:1;font-size:15pt;line-height:1.25}
.cards{display:flex;gap:3mm;justify-content:space-between}
.card{width:27mm;height:46mm;border:0.7mm solid #000;border-radius:2.5mm;position:relative;display:flex;align-items:center;justify-content:center}
.card .shp{display:block}
.card .cn{font-family:'Fredoka';font-weight:600;font-size:30pt}
.card .cl{position:absolute;right:1.5mm;bottom:1mm;font-weight:800;font-size:13pt;border:0.4mm solid #000;border-radius:50%;width:7mm;height:7mm;display:flex;align-items:center;justify-content:center}
.orderrow{display:flex;align-items:center;gap:3mm;font-weight:700;font-size:13pt}
.arrowline{flex:1;border-top:0.8mm solid #000;position:relative;height:0}
.arrowline:after{content:'';position:absolute;right:0;top:-2mm;border-left:4mm solid #000;border-top:2mm solid transparent;border-bottom:2mm solid transparent}
.slots{display:grid;grid-template-columns:20mm repeat(6,1fr);gap:3mm;justify-items:center;align-items:center}
.slots .rl{justify-self:start;font-size:12pt;font-weight:700}
.slots .ab{width:22mm;height:24mm}.slots .ab.letter{height:22mm}
.chips{display:flex;gap:4mm;flex-wrap:wrap}.chip{border:0.6mm solid #000;border-radius:6mm;padding:1mm 4mm 1mm 5mm;font-family:'Fredoka';font-weight:600;font-size:20pt;display:inline-flex;align-items:center}
.chip i.cl{font-style:normal;display:inline-flex;align-items:center;justify-content:center;width:8.5mm;height:8.5mm;border:0.5mm solid #000;border-radius:50%;font-size:14pt;margin-left:2.5mm;font-weight:700}
ul.clues{margin:0;padding-left:7mm;font-size:15pt;line-height:1.5}
ul.clues li{margin:1mm 0}
table.lgrid{border-collapse:collapse}table.lgrid th,table.lgrid td{border:0.5mm solid #000;font-size:12.5pt;padding:0 2mm}
table.lgrid td{width:15mm;height:13mm}table.lgrid th{font-weight:800}table.lgrid th.rh{text-align:left;width:22mm}
.twocol{display:flex;gap:8mm;align-items:flex-start}.twocol>div:last-child{flex:1}
.ansgrid{display:grid;grid-template-columns:auto 20mm 20mm;gap:1.5mm 3mm;align-items:center;justify-content:start}
.ansgrid b{font-size:11pt;text-align:center}.ansgrid .nm{font-size:15pt;font-weight:700}.ansgrid .ab{width:20mm}
.howto{border:0.5mm solid #000;border-radius:2mm;padding:2mm 3mm;font-size:11pt;line-height:1.25}.howto b{font-size:11.5pt}
.howto .hw{display:flex;gap:3mm;align-items:center;margin-top:1.5mm}.howto p{margin:0.6mm 0}
table.lgrid.mini td{width:9mm;height:9mm;text-align:center;padding:0}table.lgrid.mini th{font-size:10pt;padding:0 1.5mm}table.lgrid.mini th.rh{width:auto}
.twocol>ul.clues{flex:1;min-width:0}
.ansline{font-size:15pt;margin:1.5mm 0;line-height:2.1;white-space:nowrap}
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
.ccell .ex.sh{font-size:12.5pt;line-height:1.1;text-align:center;font-weight:600}
.ccell .ln{display:inline-block;width:17mm;border-bottom:0.5mm solid #000;height:7mm}
.sumrows{display:grid;gap:5mm 6mm}.sumrows.two{grid-template-columns:1fr 1fr}
.sumrow{display:flex;align-items:center;gap:3mm;font-family:'Fredoka';font-weight:500;font-size:24pt;height:27mm;border-bottom:0.3mm solid #000}
.sumrows.tall .sumrow{height:31mm}
.shrows{display:flex;flex-direction:column;gap:1.2mm}
.shrow{display:flex;align-items:center;gap:4mm;border-bottom:0.3mm solid #000;padding:0.8mm 0 2mm}
.shmid{flex:1}.shtxt{font-size:12pt;line-height:1.25;margin:0 0 1.5mm}.shsvg svg{display:block}
.shrow .ab{width:19mm;height:14mm;margin-left:2mm;flex:none}
.maze.tall .mcell{height:38mm}
.dicon{vertical-align:middle}
.shblock{display:flex;gap:8mm;align-items:center;border:0.4mm solid #000;border-radius:2mm;padding:3mm 5mm}
.eqs{flex:1;display:flex;flex-direction:column;gap:3mm}
.eq{display:flex;align-items:center;gap:2mm;font-family:'Fredoka';font-weight:600;font-size:20pt;height:12mm}
.shansw{display:flex;flex-direction:column;gap:2mm;border-left:0.5mm solid #000;padding-left:6mm}
.shans{display:flex;align-items:center;gap:2mm}
.shans .ab{width:15mm;height:12mm}
.grows,.crows,.lrows{display:flex;flex-direction:column;gap:1.2mm}
.grow,.crow,.lrow{display:flex;align-items:center;gap:3mm;border-bottom:0.3mm solid #000;padding-bottom:2mm}
.gsvg{width:100mm;flex:none}.geq{margin-left:auto;display:flex;align-items:center;gap:2mm}.geq .ab{width:14mm}
.lbx{display:inline-flex;flex-direction:column;align-items:center;gap:0.3mm}.lbx small{font-size:8.5pt;font-weight:700;line-height:1}
.csvg{flex:1}.cans{display:flex;align-items:center;gap:2mm;font-size:16pt}
.lsvg{flex:none}.lsvg svg{max-width:none}.unit{font-size:14pt;font-weight:700}
.citem{flex-direction:row;align-items:center;gap:3mm;border:none;padding:0}.citem svg{width:36mm;flex:none}.cmid{display:flex;flex-direction:column;gap:2mm}
.cq{font-size:12.5pt;line-height:1.2}.items.g2{grid-template-columns:1fr 1fr;gap:4mm 6mm}
.ctime{font-size:18pt;font-weight:800}.ctime .ab{width:13mm;height:12mm}
.figwrap{text-align:center}
.srows{display:flex;gap:2mm;justify-content:space-between}
.srow{display:flex;align-items:center;gap:1mm}.srow svg{width:11mm}.srow .ab{width:12mm;height:12mm}
.pgraph{display:flex;flex-direction:column;gap:4mm}
.grow2{display:flex;align-items:center}
.gl{width:34mm;font-size:15pt;display:flex;align-items:center;gap:1.5mm}.gl svg{flex:none}
.gc{width:15.5mm;height:15.5mm;border:0.5mm solid #000;display:inline-flex;align-items:center;justify-content:center;margin-right:-0.5mm}
svg.face{display:block}.lead svg.face{display:inline-block;vertical-align:middle}
.kids{display:flex;justify-content:space-between}.kid{display:flex;flex-direction:column;align-items:center;font-size:14pt}
.qslots{display:flex;flex-direction:column;gap:2.5mm}.qslot{display:flex;align-items:center;gap:4mm;font-size:16pt;font-weight:800}.qslot .qn{width:14mm}.qslot .ab.wide{width:68mm;height:12.5mm}
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
.kentry{border:0.5mm solid #000;border-radius:2mm;padding:2.2mm 3.5mm;margin-bottom:3mm;font-size:10pt;line-height:1.25;break-inside:avoid}
.kentry h4{font-family:'Fredoka';font-weight:600;font-size:13pt;margin:0 0 1.5mm}
.kentry .tags{font-weight:700;margin-bottom:1mm}
.kentry .row{display:flex;gap:4mm}.kentry .row>div:first-child{flex:1}
.kmini{display:grid;gap:0;border:0.5mm solid #000;width:max-content}.kmini i{width:4.5mm;height:4.5mm;border:0.25mm solid #000;display:flex;align-items:center;justify-content:center;font-style:normal;font-size:8pt}.kmini i.on{background:#000;color:#fff}
.kmini i.dt:after{content:'';width:1.8mm;height:1.8mm;border-radius:50%;background:#000;display:block}
.kroute i,.kgrid i{width:5mm;height:5mm}.kgrid i.tk{background:#000}.kmagic i.num{font-size:10pt;font-weight:800}.kmagic i{width:6mm;height:6mm}
.kgraph{font-size:8pt;border:0.4mm solid #000;padding:1mm 2mm;width:max-content}.kg{display:flex;align-items:center;gap:1mm;height:3.6mm}.kg span{width:12mm}.kg b{width:2.6mm;height:2.6mm;border-radius:50%;background:#000;display:inline-block}
.legend{display:flex;gap:10mm;justify-content:center;align-items:center;font-size:13pt;font-weight:700}.legend .lg{display:inline-flex;align-items:center;gap:2mm}
.cbcans svg.pic{width:var(--tw,162mm)}.cbcans h2{font-size:17pt;margin-bottom:2mm}
.cbckey{display:flex;gap:2mm;margin:0 auto 1.5mm;width:var(--cw,168mm)}
.cbckey .k{flex:1;border:0.6mm solid #000;border-radius:2mm;padding:0.6mm 1.5mm;text-align:center;line-height:1.15}
.cbckey .k b{display:block;font-family:'Fredoka';font-weight:700;font-size:14pt}
.cbckey .k i{display:block;font-style:normal;font-size:11pt;border-top:0.3mm solid #000;margin-top:0.4mm;padding-top:0.3mm}
svg.pic{display:block;margin:0 auto;width:var(--cw,168mm);height:auto;max-width:none}
svg.pic .r{fill:#fff;stroke:#000;stroke-width:0.9;stroke-linejoin:round;fill-rule:evenodd}
svg.pic text{font-family:'Fredoka';font-weight:600;dominant-baseline:central;fill:#000;text-anchor:start}
svg.pic text.a{font-weight:700}
svg.pic .bx{fill:#fff;stroke:#000;stroke-width:0.45}
svg.pic .ul{stroke:#000;stroke-width:0.4}
.fr{display:inline-flex;flex-direction:column;align-items:center;vertical-align:middle;line-height:1.05;font-size:11.5pt}.fr i{font-style:normal;display:block;padding:0 1mm}.fr i:first-child{border-bottom:0.35mm solid #000}
svg.mk{vertical-align:-0.9mm;margin:0 0.6mm}
svg.pic .fb{stroke:#000;stroke-width:0.45}
.draft{border:0.8mm solid #000;border-radius:2mm;padding:2mm 4mm;font-weight:800;font-size:12pt;text-align:center;margin:0 0 4mm}
.page.cbc header.ph{height:15mm}.page.cbc h1{font-size:22pt}
.page.cbc .topic{padding:1.2mm 0 0;font-size:11pt}.page.cbc .instr{font-size:13pt;line-height:1.25;padding:0.5mm 0 1.5mm}
.page.cbc .area{justify-content:flex-start;padding:0}
.page.cbc .check{min-height:0;padding:1.6mm 4mm;margin-top:1.5mm}
.page.cbc .check .ct2{font-size:10.5pt;line-height:1.25}.page.cbc .check .ct2 b{font-size:11.5pt}.page.cbc .check .ct2 div{margin-top:0.3mm}
.page.cbc .check svg{width:9mm;height:9mm}
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
    name = html.escape(school) if school.strip() else "________________________"
    tail = "only. Not for resale." if school.strip() else "(school name) only. Not for resale."
    return (f'<footer class="pf"><span class="fl"><span class="fx">&copy; 2026 Preciouslyours Pte Ltd. Photocopy licence:</span> <span class="sn">{name}</span> <span class="fx">{tail}</span></span>'
            f'<span class="pc"><b>{code}</b></span></footer>')

def pupil_page(p, school):
    code = f"P1-{p['no']:02d}"
    instr = "".join(f"<p>{html.escape(s)}</p>" for s in p["instr"])
    lb = ""
    if p.get("check_boxes"):
        lb = '<div class="lb">' + '<span class="ab"></span>' * p["check_boxes"] + "</div>"
    cls = "page cbc" if p.get("cbc") else "page"
    chk_html = html.escape(p["check"])
    if p.get("check_html_lines"):
        chk_html = "<b>Check it.</b>" + "".join(f"<div>{c}</div>" for c in p["check_html_lines"])
    elif p.get("check_lines"):
        chk_html = "<b>Check it.</b>" + "".join(f"<div>{html.escape(c.replace('..', '.'))}</div>" for c in p["check_lines"])
    else:
        chk_html = "<b>Check it.</b> " + chk_html
    return (f'<section class="{cls}"><header class="ph"><span class="code">{code}</span><h1>{html.escape(p["title"])}</h1>'
            f'{stars_svg(p["tier"])}<div class="nameline">Name <span></span></div></header>'
            f'<div class="topic">Topic: {html.escape(p["topic"])}</div><div class="instr">{instr}</div>'
            f'<div class="area">{p["body"]}</div>'
            f'<div class="check">{tick_svg()}<div class="ct2">{chk_html}</div>{lb}</div>'
            f'{footer(code, school)}</section>')

def doc(pages_html, title):
    return (f'<!doctype html><html lang="en-GB"><head><meta charset="utf-8"><title>{html.escape(title)}</title>'
            f'<style>{CSS.replace("FONT", FONT)}</style></head><body>{pages_html}</body></html>')

# ------------------------------------------------------------------ front matter
DRAFT = True                      # front matter carries DRAFT stamps until the owner (and a lawyer) approve the wording: build.py --final turns them off
CONTACT = "pypteltd@gmail.com (business contact email for now; to be changed later)"
REG_OFFICE = "[registered office address: to be added by the owner]"

def draft_banner(what):
    if not DRAFT: return ""
    return f'<div class="draft">DRAFT: {html.escape(what)} Contact: {html.escape(CONTACT)}</div>'

def cover(school):
    s = html.escape(school) if school.strip() else "&nbsp;"
    pub = ('<p style="margin-top:14mm;font-size:12pt">[Publisher line: wording to be confirmed by the owner]</p>' if DRAFT
           else '<p style="margin-top:14mm;font-size:12pt">Preciouslyours Pte Ltd</p>')
    return ('<section class="page cover fm"><div>' + (draft_banner("cover wording, title and publisher line are not final.") if DRAFT else "") +
            '<p class="sub" style="margin-top:12mm">Maths puzzles for early finishers</p>'
            '<div class="big" style="margin-top:6mm">Early Finisher Puzzles</div><div class="big" style="font-size:36pt;margin-top:3mm">Primary 1</div></div>'
            '<div class="box">20 single-page puzzles<br>Every puzzle checks itself<br>One star and two star pages<br>Teacher answer key included</div>'
            f'<div><p style="font-size:13pt;margin:0 0 2mm">This pack belongs to</p><span class="school">{s}</span>'
            + pub + '</div></section>')

def licence(school):
    s = html.escape(school) if school.strip() else "____________________________"
    return ('<section class="page fm"><h2>Photocopy licence' + (" (DRAFT)" if DRAFT else "") + '</h2>'
            + draft_banner("this licence wording is a placeholder. The owner and a lawyer must approve it, and the entity, year, term of the licence and the registered office address below must be filled in (the contact email is the business email for now and will change), before any school receives this pack.")
            + f'<p><b>Licensed to:</b> {s} (one school, one campus)</p>'
            '<h3>You may</h3><ul><li>Print this PDF and photocopy any page for the pupils and staff of the school named above.</li>'
            '<li>Keep the file on the school network and share it with the school\'s teachers.</li>'
            '<li>Hand a single page to a pupil, or keep a tray of pages in the classroom.</li></ul>'
            '<h3>You may not</h3><ul><li>Sell, lend or give the pages or the file to another school, tuition centre or person.</li>'
            '<li>Post the file or pages on a public website or a shared platform outside the school.</li>'
            '<li>Edit the pages, or remove the licence line at the foot of each page.</li></ul>'
            '<h3>Printed copies</h3><p>Printed sets: details to follow. ' + (html.escape("Contact: " + CONTACT + ". Registered office: " + REG_OFFICE) if DRAFT else "") + '</p>'
            '<h3>Notes</h3><p>The licence is for the edition bought. The school name shown on each page is set when the pack is made.</p>'
            '<p style="margin-top:12mm">&copy; 2026 Preciouslyours Pte Ltd.' + (" [entity name and year: owner to confirm]" if DRAFT else " All rights reserved.") + '</p></section>')

def _plist(pages, pred):
    return ", ".join("P1-%02d" % p["no"] for p in pages if pred(p))

def teacher_notes(pages):
    n1 = sum(1 for p in pages if p["tier"] == 1); n2 = len(pages) - n1
    cbc = _plist(pages, lambda p: p.get("cbc"))
    later = _plist(pages, lambda p: p.get("later"))
    return ('<section class="page fm"><h2>Teacher notes' + (" (DRAFT)" if DRAFT else "") + '</h2>'
            + draft_banner("teacher notes are for owner review.")
            + '<h3>What this is</h3><p>Twenty single-page maths puzzles for Primary 1 pupils who finish their work early. Each page stands alone, so you can hand out one page or keep a tray of pages. The pupil needs no help to start.</p>'
            f'<h3>Stars</h3><p>One star pages practise a topic as it is usually taught ({n1} pages). Two star pages use the same topics with two steps or two clues to combine ({n2} pages). Pages can be used in any order.</p>'
            '<h3>Every page checks itself</h3><p>The boxed strip at the foot of each page tells the pupil how to check. The check shows that something is wrong. It does not give the answer.</p>'
            '<ul><li><b>Code word.</b> The answers give letters that spell a word. The strip does not say what the word is; there is no clue to guess it from. The letters of every code word can be arranged into a word in one way only, so answers written in the wrong boxes never spell another word.</li><li><b>Colour by code.</b> Each answer is found in a key of five numbers and the part is coloured with that crayon. The pupil counts the parts of each colour and compares with the box on the page; matching parts must share a colour.</li>'
            '<li><b>Route.</b> The line must reach FINISH through the stated number of boxes.</li><li><b>Logic grid and queue.</b> Each number, price or child has a letter; the letters, read down the list, must spell a word. On P1-04 and P1-07 one more number or child is listed than there are places: a clue says which one is left out, and its letter is a decoy that is not in the word.</li><li><b>Total.</b> The whole count must make the stated total (P1-20 adds a second sum for the two questions).</li></ul>'
            '<p>Marking is not needed. To spot-check, look only at the check strip.</p>'
            '<h3>How the checks were tested</h3><p>For every page, a script tried each single wrong answer (one answer changed by 1, 2, 3, 4, 5 or 10, or any other value in the page\'s range) and every wrong arrangement of the logic pages. The check rejected at least 95% of them on every page. A wrong answer that happens to spell any English word from a list of about 129 000 words counts as not rejected.</p>'
            '</section>'
            '<section class="page fm"><h2>Teacher notes: using the pages' + (" (DRAFT)" if DRAFT else "") + '</h2>'
            '<h3>Using the pages</h3><ul><li><b>Time.</b> Most pages take 5 to 15 minutes; the colour-by-code pages (' + cbc + ') take longer because pupils colour a picture. Pupils need their own crayons (five colours: yellow, red, blue, green, orange). The outline is printed black and white; the colour words in the key are what the pupil follows.</li>'
            '<li><b>If the check fails.</b> The pupil goes back, looks for the slip, and asks a friend or you if still stuck.</li>'
            '<li><b>When to use.</b> Some topics are usually taught later in the year: ' + later + '. P1-06 uses o\'clock and half past; P1-18 reads times to 5 minutes and is usually used late in the year. Check your scheme of work before giving out these pages.</li>'
            '<li><b>Stars.</b> One star: one skill, as usually taught. Two stars: the same topics with two steps or two clues to combine.</li></ul>'
            '<h3>Photocopying</h3><p>All pages are black and white with solid lines, so they copy cleanly. Each page is one side only; the back of a copy stays blank. Pupils write on the page: the boxes are large for young hands. Use A4 and print at 100% (actual size); on P1-17 a real ruler matches the drawn ruler only at 100%.</p>'
            '<h3>What is in this pack</h3><table class="tbl"><tr><th>Part</th><th>Pages</th><th>Photocopy for pupils?</th></tr>'
            '<tr><td>Cover</td><td>1</td><td>No</td></tr><tr><td>Photocopy licence</td><td>1</td><td>No</td></tr>'
            '<tr><td>Teacher notes</td><td>2</td><td>No</td></tr><tr><td>Contents</td><td>1</td><td>No</td></tr>'
            '<tr><td>Puzzle pages P1-01 to P1-20</td><td>20</td><td>Yes</td></tr>'
            '<tr><td><b>Complete pack to print</b></td><td><b>25</b></td><td>The teacher answer key is a separate file.</td></tr></table>'
            '</section>')

def contents(pages):
    rows = "".join(f'<tr><td>P1-{p["no"]:02d}</td><td>{html.escape(p["title"])}</td><td>{html.escape(p["topic"])}</td><td>{"1 star" if p["tier"]==1 else "2 stars"}</td></tr>' for p in pages)
    return ('<section class="page fm"><h2>Contents</h2><table class="tbl"><tr><th>Page</th><th>Puzzle</th><th>Topic</th><th>Tier</th></tr>'
            + rows + '</table><p style="margin-top:4mm;font-size:11pt">Pages are independent. Pick any page.</p></section>')

# ------------------------------------------------------------------ teacher key
def key_entry(p):
    extra = p.get("mini", "")
    return (f'<div class="kentry"><h4>P1-{p["no"]:02d} {html.escape(p["title"])} &nbsp; {"1 star" if p["tier"]==1 else "2 stars"}</h4>'
            f'<div class="tags">Topic: {html.escape(p["topic"])}</div>'
            f'<div>Syllabus topic: {html.escape(p["strand"])}; reference {html.escape(p["syll"])}</div>'
            f'<div>Puzzle type: {html.escape(p["ptype"])}. How the pupil checks: {html.escape(p.get("mech_plain", p["mech"]))}.</div>'
            f'<div class="row"><div><b>Answers:</b> {html.escape(p["key"]["answers"])}<br><b>Check result:</b> {html.escape(p["key"]["check_result"])}</div>{extra}</div>'
            f'<div><b>Teacher note:</b> {html.escape(p["note"])}</div></div>')

def key_pages(pages, school, packing=None):
    out = ['<section class="page fm"><h2>Teacher answer key: Primary 1</h2>'
           '<p>This key lists the answers and the result of the check on every page. You do not need it for routine marking: a pupil who has a working check has the right answers. To spot-check, compare the check strip with the line "Check result" below.</p>'
           '<h3>How the topic tags work</h3><p>Each entry names the Primary 1 topic the puzzle practises, with a reference to the Primary 1 topics in the Mathematics Syllabus, Primary (2021 edition, pages 31 and 32). Where the syllabus lists several outcomes under one topic, the range of outcome numbers is given. The references are for your planning only and are not printed on the pupil pages.</p>'
           '<h3>Topic coverage</h3><table class="tbl"><tr><th>Strand</th><th>Pages</th></tr>'
           + "".join(f'<tr><td>{html.escape(k)}</td><td>{", ".join("P1-%02d" % x for x in v)}</td></tr>' for k, v in strand_map(pages).items())
           + '</table><p style="font-size:10pt;margin-top:4mm">Syllabus items not covered by a puzzle: reading and writing numbers in words, number-sentence signs in isolation, measuring and drawing a line to the nearest cm, am and pm, copying figures on a grid, forming figures from shapes, ordinals beyond 5th, naming a shape from a description.</p></section>']
    groups = packing or [pages[i:i + 3] for i in range(0, len(pages), 3)]
    for g in groups:
        out.append('<section class="page fm" >' + "".join(key_entry(p) for p in g) + footer("KEY", school).replace("Photocopy licence", "Teacher key. Photocopy licence") + "</section>")
    for p in pages:
        if p.get("cbc"):
            out.append(f'<section class="page fm cbcans" ><h2>Answers: P1-{p["no"]:02d} {html.escape(p["title"])}</h2>'
                       f'<p style="margin:0 0 2mm;font-size:10.5pt">Every part shows the question, the answer underlined and the colour in brackets. Pupils colour their own copy. '
                       f'Colour key: {html.escape(p["key"]["answers"].replace("Colour key: ", ""))}.</p>{p["teacher_svg"]}'
                       + footer("KEY", school).replace("Photocopy licence", "Teacher key. Photocopy licence") + "</section>")
    return "".join(out)

def strand_map(pages):
    m = {}
    for p in pages:
        m.setdefault(p["strand"], []).append(p["no"])
    return m
