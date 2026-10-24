#!/usr/bin/env python3
"""Build website/syllabus/index.html: the parent syllabus map (13 places, chips + level cards) and the tier map,
as one self-contained static page in the site style (uses /fonts.css like the other site pages).

    python3 docs/syllabus_map/build_static.py
Inputs: intl_rows.json (python3 add_singapore.py), tier_rows.json (python3 build_tier_rows.py).
Live dashboards (same data): see README.md in this folder.
"""
import json, os, html
H = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(os.path.dirname(os.path.dirname(H)), 'website', 'syllabus', 'index.html')
rows = json.load(open(os.path.join(H, 'intl_rows.json')))
tiers = json.load(open(os.path.join(H, 'tier_rows.json')))
places = []
for r in rows:
    if r['jurisdiction'] not in places: places.append(r['jurisdiction'])
places.remove('Singapore (MOE)'); places.insert(0, 'Singapore (MOE)')
data = [[r['jurisdiction'], r['lesson'], r['lesson_title'], r['status'], int(r['unverified'])] for r in rows]
RN = {'AT': 'At school level', 'NEW': 'School ideas, new settings', 'AHEAD': 'Reaches further', 'MIX': 'Mixed or unclear'}
IC = {'AT': '\u2713', 'NEW': '\u25d0', 'AHEAD': '\u25b2', 'MIX': '?'}
CN = {'good': 'Lesson-by-lesson evidence', 'some': 'Item-level evidence, years checked', 'thin': 'Thin evidence'}
TT = [('Start here', 'The core idea, at the school year'), ('Think harder', 'The same idea in an unfamiliar setting'), ('Go further', 'Challenge: mastery, then extension')]
e = html.escape
grid = '<div class="tgrid"><div class="hd colh"></div>' + ''.join(f'<div class="hd colh">{e(a)}<small>{e(b)}</small></div>' for a, b in TT)
for L in range(1, 7):
    rs = {r['tier']: r for r in tiers if r['level'] == L}
    f = rs['Start here']
    grid += f'<div class="lv">Level {L}<small>{e(f["ages"])} · vs {e(f["year"])}</small></div>'
    for a, _ in TT:
        r = rs[a]
        grid += (f'<div class="cell" data-r="{r["rating"]}"><div class="tl">{e(a)}</div><div class="chip"><span aria-hidden="true">{IC[r["rating"]]}</span>{RN[r["rating"]]}</div>'
                 f'<h3>{e(r["headline"])}</h3><p>{e(r["detail"])}</p><p class="ev">{e(r["evidence"])}</p>'
                 f'<span class="tag" data-c="{r["confidence"]}">{CN[r["confidence"]]} · {r["items"]} items</span></div>')
grid += '</div>'
PAGE = r'''<style>
:root{--bg:#FFF8E7;--ink:#1B2A49;--card:#fff;--line:#c9c1a8;--same:#E4F2EA;--later:#FBEBCB;--new:#E6EDF8;--mut:#4A5470;--non:#E9E4D2;--a-same:#1B6B49;--a-new:#2B4C94;--a-later:#8A4B00}
@media (prefers-color-scheme:dark){:root{--bg:#101a30;--ink:#f3efe2;--mut:#C3CBE0;--card:#1a2646;--line:#4a5b8a;--same:#1B3B30;--later:#46320F;--new:#1F2F58;--non:#2A365A;--a-same:#8FD9B3;--a-new:#A9C1FF;--a-later:#FFCF7A}}
*{box-sizing:border-box}html,body{margin:0}
body{background:var(--bg);color:var(--ink);font:17px/1.55 'Nunito Sans',Arial,sans-serif;padding-block:max(18px,env(safe-area-inset-top)) max(48px,env(safe-area-inset-bottom));padding-left:max(16px,env(safe-area-inset-left));padding-right:max(16px,env(safe-area-inset-right))}
main{max-width:70rem;margin:0 auto}
h1{font:600 clamp(28px,6vw,40px)/1.15 Fredoka,Arial,sans-serif;margin:.3rem 0 .4rem;text-wrap:balance}
h2{font:600 clamp(22px,4vw,28px)/1.2 Fredoka,Arial,sans-serif;margin:2.4rem 0 .4rem}
a{color:inherit;font-weight:700}
.back{display:inline-block;margin-bottom:1rem}
.lead{color:var(--mut);max-width:44rem;margin:.3rem 0 1rem}
.chips{display:flex;flex-wrap:wrap;gap:.4rem;margin:.4rem 0 1rem}
.chips button{font:inherit;font-size:15px;padding:.35rem .8rem;border-radius:999px;border:1.5px solid var(--ink);background:transparent;color:var(--ink);cursor:pointer}
.chips button[aria-pressed=true]{background:var(--ink);color:var(--bg)}
.legend{display:flex;flex-wrap:wrap;gap:.3rem 1.2rem;font-size:14px;color:var(--mut);margin:0 0 1rem}
.legend span{display:inline-flex;align-items:center;gap:.4rem}.legend{font-size:15px}
.sw{min-width:1.7rem;height:1.5rem;border-radius:5px;display:inline-flex;align-items:center;justify-content:center;font:800 13px/1 Arial,sans-serif;border:1px solid var(--line);border-bottom:4px solid var(--line);color:var(--ink)}
.sw[data-s=SAME],.sw[data-s=EARLIER]{background:var(--same);border-bottom-color:var(--a-same)}.sw[data-s=LATER]{background:var(--later);border-bottom-color:var(--a-later)}
.sw[data-s=NOT]{background:var(--non);border-bottom-color:var(--mut)}.sw[data-s=MIXED]{border:1px dashed var(--mut);border-bottom:1px dashed var(--mut)}
.sw[data-r]{font-size:15px}.sw[data-r=AT]{background:var(--same);border-bottom-color:var(--a-same);color:var(--a-same)}.sw[data-r=NEW]{background:var(--new);border-bottom-color:var(--a-new);color:var(--a-new)}.sw[data-r=AHEAD]{background:var(--later);border-bottom-color:var(--a-later);color:var(--a-later)}.sw[data-r=MIX]{border:1px dashed var(--mut);border-bottom:1px dashed var(--mut);color:var(--mut)}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,20rem),1fr));gap:14px}
.card{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:16px;display:flex;flex-direction:column;gap:.6rem;min-width:0}
.card h3{margin:0;font:600 20px/1.2 Fredoka,Arial,sans-serif}.card h3 small{font:400 14px 'Nunito Sans',Arial,sans-serif;color:var(--mut);margin-left:.4rem}
.strip{display:grid;grid-template-columns:repeat(10,1fr);gap:3px}
.seg{height:3rem;border-radius:5px;display:flex;flex-direction:column;align-items:center;justify-content:center;font-size:15px;line-height:1.1;font-weight:800;border-bottom:4px solid transparent;position:relative;cursor:default;padding:0;font-family:inherit;color:var(--ink)}.seg i{font-style:normal;font-size:12px;font-weight:800}
.seg[data-s=SAME],.seg[data-s=EARLIER]{background:var(--same);border-bottom-color:var(--a-same)}.seg[data-s=LATER]{background:var(--later);border-bottom-color:var(--a-later)}
.seg[data-s=NOT]{background:var(--non);border-bottom-color:var(--mut)}.seg[data-s=MIXED]{border:1px dashed var(--mut);color:var(--mut);background:transparent}
.seg:focus-visible{outline:2px solid var(--ink);outline-offset:1px}
.seg .tip{display:none;position:absolute;z-index:5;bottom:calc(100% + 6px);left:50%;transform:translateX(-50%);width:max-content;max-width:16rem;background:var(--ink);color:var(--bg);font-weight:600;font-size:13px;line-height:1.35;padding:.4rem .6rem;border-radius:8px;text-align:left;pointer-events:none}
.seg:hover .tip,.seg:focus .tip{display:block}
.strip .seg:nth-child(-n+2) .tip{left:0;transform:none}.strip .seg:nth-child(n+9) .tip{left:auto;right:0;transform:none}
.say{margin:0;font-size:17px}.further{margin:0;padding:0;list-style:none;font-size:15px;color:var(--mut)}.further li::before{content:"▲ ";color:var(--a-later);font-weight:700}
.notes{font-size:14px;color:var(--mut);max-width:50rem}.notes p{margin:.4rem 0}
.tgrid{display:grid;grid-template-columns:8.5rem repeat(3,minmax(0,1fr));gap:6px;margin-top:.8rem}
.hd{padding:.4rem .5rem;font-weight:800}.hd small{display:block;font-weight:400;color:var(--mut);font-size:15px;line-height:1.35}
.lv{padding:.5rem;font:600 20px/1.2 Fredoka,Arial,sans-serif}.lv small{display:block;font:400 14px 'Nunito Sans',Arial,sans-serif;color:var(--mut)}
.cell{border-radius:14px;padding:.8rem .9rem;border:1px solid var(--line);border-left:8px solid var(--line);display:flex;flex-direction:column;gap:.4rem;min-width:0;background:var(--card)}
.cell[data-r=AT]{background:var(--same);border-left-color:var(--a-same)}.cell[data-r=NEW]{background:var(--new);border-left-color:var(--a-new)}.cell[data-r=AHEAD]{background:var(--later);border-left-color:var(--a-later)}.cell[data-r=MIX]{background:transparent;border-style:dashed;border-left-style:dashed;border-left-color:var(--mut)}
.chip{font-size:14px;font-weight:800;text-transform:uppercase;letter-spacing:.03em;display:flex;align-items:center;gap:.4rem}
.cell[data-r=AT] .chip{color:var(--a-same)}.cell[data-r=NEW] .chip{color:var(--a-new)}.cell[data-r=AHEAD] .chip{color:var(--a-later)}.cell[data-r=MIX] .chip{color:var(--mut)}
.cell h3{margin:0;font-size:18px;line-height:1.3}.cell p{margin:0;font-size:16px;line-height:1.5}.cell .ev{color:var(--mut)}
.tag{display:inline-block;max-width:100%;font-size:14px;padding:.1rem .55rem;border-radius:999px;border:1px solid var(--mut);width:fit-content;margin-top:.2rem;color:var(--ink)}.tag[data-c=thin]{border-style:dashed;border-width:2px;font-weight:800}
.tl{display:none;font-weight:800;color:var(--ink);font-size:16px}
@media (max-width:760px){.tgrid{grid-template-columns:1fr}.colh{display:none}.lv{margin-top:.8rem;padding-inline:0}.tl{display:block}}
</style>
<main>
<a class="back" href="/">← Back to Math Inquirers</a>
<h1>How Math Inquirers fits school maths</h1>
<p class="lead">Math Inquirers is independent enrichment. It is not affiliated with or endorsed by MOE, the Gifted Education Programme or any other ministry. Choose where your child goes to school: each level card shows how its ten lessons compare with that system's maths at the same age.</p>
<div class="chips" id="chips" role="group" aria-label="School system"></div>
<div class="legend" id="legend"></div>
<div class="cards" id="cards"></div>
<div class="notes">
<p id="sgnote" hidden>Singapore: checked lesson by lesson against the MOE 2021 Primary Mathematics syllabus (updated October 2025); only three Secondary 1 placements could not be read from an MOE document. Where the syllabus names a topic in the same year, the lesson is marked as taught at school; harder questions inside a lesson can still go further (see the tier map below).</p>
<p>Lessons use puzzles and explaining, not school-style practice, so “goes a little further” means the topic is usually met at school a year or more later. Level 1 is for ages 6 to 8, Level 2 for 7 to 9, Level 3 for 8 to 10, Level 4 for 9 to 11, Level 5 for 10 to 12 and Level 6 for 11 to 13. Each lesson box shows its number and a mark: ✓ Same, ▲ Later, – Not listed, ~ Mixed. Hover or tab to a lesson for details. The tenth lesson of each level is a mixed review and is not compared.</p>
<p>This is our own comparison, made from public curriculum documents. Singapore was checked against the MOE syllabus text; for the other places some placements could not be confirmed.</p>
</div>

<h2 id="tiers">How the three tiers fit the syllabus</h2>
<p class="lead">Every lesson has three tiers of questions. <b>Start here</b> is the core idea. <b>Think harder</b> is the same idea in an unfamiliar setting. <b>Go further</b> is the challenge: mastery, then extension. Each level is compared with the school year it is named after (Level 1 with Primary 1, and so on).</p>
<div class="legend"><span><i class="sw" data-r="AT" aria-hidden="true">✓</i>At school level</span><span><i class="sw" data-r="NEW" aria-hidden="true">◐</i>School ideas, new settings</span><span><i class="sw" data-r="AHEAD" aria-hidden="true">▲</i>Reaches further</span><span><i class="sw" data-r="MIX" aria-hidden="true">?</i>Mixed or unclear (thin evidence)</span></div>
@@GRID@@
<div class="notes">
<p><b>How firm each row is.</b> Levels 1 to 3: a lesson-by-lesson audit lists which Think harder and Go further items go beyond the Singapore syllabus, so these rows are well supported. Levels 4 and 5: the audit lists the items that look ahead but gives no verdict for a whole tier; their year placements have now been checked against the syllabus text. Level 6: thin evidence. The audit compared whole lessons with Primary 6 and Secondary 1 and did not separate the tiers, so its cells are a best reading, not a finding.</p>
<p>A tier marked “at school level” can still hold the odd item that goes beyond, and a tier marked “reaches further” is mostly built from school-level ideas. These are desk comparisons, not a claim of alignment with any ministry.</p>
</div>
</main>
<script>
(function(){
var D=@@DATA@@, PLACES=@@PLACES@@;
var AGES={1:'ages 6 to 8',2:'ages 7 to 9',3:'ages 8 to 10',4:'ages 9 to 11',5:'ages 10 to 12',6:'ages 11 to 13'};
var W={SAME:'Taught at school around this age',EARLIER:'Already met at school before this age',LATER:'Goes a little further than school',NOT:'Not part of the school syllabus',MIXED:'Mixed review, not compared'};
var G={SAME:'\u2713',EARLIER:'\u2713',LATER:'\u25b2',NOT:'\u2013',MIXED:'~'};
var place=PLACES[0];
function el(t,c,x){var e=document.createElement(t);if(c)e.className=c;if(x!=null)e.textContent=x;return e}
document.getElementById('legend').innerHTML=[['SAME','Same','Taught at school around this age'],['LATER','Later','Goes a little further than school'],['NOT','Not listed','Not part of the school syllabus'],['MIXED','Mixed','Mixed review, not compared']].map(function(p){return '<span><i class="sw" data-s="'+p[0]+'" aria-hidden="true">'+G[p[0]]+'</i><b>'+p[1]+':</b> '+p[2]+'</span>'}).join('');
function render(){
  var c=document.getElementById('chips');c.textContent='';
  PLACES.forEach(function(p){var b=el('button','',p);b.type='button';b.setAttribute('aria-pressed',String(p===place));b.onclick=function(){place=p;render()};c.appendChild(b)});
  document.getElementById('sgnote').hidden=(place!==PLACES[0]);
  var box=document.getElementById('cards');box.textContent='';
  [1,2,3,4,5,6].forEach(function(L){
    var card=el('div','card'),h=el('h3','','Level '+L);h.appendChild(el('small','',AGES[L]));card.appendChild(h);
    var strip=el('div','strip'),match=0,cells=0,ahead=[],none=0;
    for(var n=1;n<=10;n++){
      var r=D.filter(function(x){return x[0]===place&&x[1]===L+'.'+n})[0];
      var s=el('button','seg');s.type='button';
      if(r){s.setAttribute('data-s',r[3]);s.appendChild(document.createTextNode(n));s.appendChild(el('i','',G[r[3]]));
        var t=el('span','tip','Lesson '+r[1]+': '+r[2]+'. '+W[r[3]]+(r[4]?' (not fully confirmed)':''));s.appendChild(t);
        s.setAttribute('aria-label','Lesson '+r[1]+', '+r[2]+': '+W[r[3]]);
        if(r[3]!=='MIXED'){cells++;if(r[3]==='LATER')ahead.push(r[2]);else if(r[3]==='NOT')none++;else match++}}
      strip.appendChild(s)}
    card.appendChild(strip);
    var p=el('p','say',match+' of '+cells+' topics are already part of school maths by this age; '+ahead.length+' go a little further than school'+(none?'; '+none+' have no school equivalent.':'.'));
    card.appendChild(p);
    if(ahead.length){var ul=el('ul','further');ahead.forEach(function(t){ul.appendChild(el('li','',t))});card.appendChild(ul)}
    box.appendChild(card)});
}
render();
})();
</script>'''
body = (PAGE.replace('@@GRID@@', grid).replace('@@DATA@@', json.dumps(data, ensure_ascii=False, separators=(',', ':')))
        .replace('@@PLACES@@', json.dumps(places)))
title = 'How Math Inquirers fits school maths'
desc = 'How each Math Inquirers level and tier compares with the Singapore MOE syllabus and 12 other places. Independent enrichment, not affiliated with MOE.'
doc = ('<!doctype html>\n<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
       f'<title>{e(title)}</title><meta name="description" content="{e(desc)}"><meta name="theme-color" content="#1B2A49">'
       '<link rel="stylesheet" href="/fonts.css"></head><body>\n' + body + '\n</body></html>\n')
os.makedirs(os.path.dirname(OUT), exist_ok=True)
open(OUT, 'w', encoding='utf-8').write(doc)
print(OUT, len(doc))
