#!/usr/bin/env python3
"""Write the owner's preview page: outputs/owner_review/teasers_preview/index.html

A single self-contained HTML file (no server, no network). Pick a level and a date (or step day by day), or jump to the
minute either side of midnight Singapore time, and see exactly what a visitor would see on the real pages. It uses the
same teasers.js and the same released batches as the site build, plus the same fallback rules.

    python3 website/teasers/build_preview.py
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
import teaser_html as TH   # noqa: E402

OUT = os.path.join(ROOT, 'outputs', 'owner_review', 'teasers_preview')


def main():
    os.makedirs(OUT, exist_ok=True)
    css = open(os.path.join(ROOT, 'website', 'lp_parts.txt'), encoding='utf-8').read()
    months = {}
    full = {}
    for mm in TH.released():
        for lv in range(1, 7):
            months['L%d-%s' % (lv, mm)] = TH.month_json(lv, mm)
    for lv in range(1, 7):
        full[str(lv)] = []
        for mm in sorted(TH.released()):
            for e in TH.load_month(mm)['levels'][str(lv)]:
                full[str(lv)].append(dict(date=e['date'], topic=e['topic'], q=e['q'], shown=e['shown'], kind=e['kind'], id=e['id']))
    pools = {str(lv): TH.fallback_pool(lv) for lv in range(1, 7)}
    js = open(os.path.join(HERE, 'teasers.js'), encoding='utf-8').read()
    data = json.dumps({'months': months, 'pools': pools, 'full': full, 'ages': TH.LEVEL_AGES, 'released': TH.released()}, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
    page = '''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Daily teaser preview</title>
<style>''' + css + TH.CSS + '''
body{margin:0}
.pv{max-width:980px;margin:0 auto;padding:16px;display:grid;gap:14px}
.pv h1{font-size:28px}
.ctl{display:flex;flex-wrap:wrap;gap:10px;align-items:end;border:2px dashed var(--line);border-radius:14px;padding:12px;background:var(--card)}
.ctl label{display:grid;gap:4px;font:800 13px var(--body)}
.ctl input,.ctl select{font:600 16px var(--body);padding:8px;border:2px solid var(--ink);border-radius:10px;background:var(--bg);color:var(--fg)}
.status{font:700 14px var(--body);background:var(--soft);border-radius:12px;padding:10px 14px}
table.keys{border-collapse:collapse;width:100%;font-size:14px}
table.keys td,table.keys th{border:1px solid var(--line);padding:5px 8px;text-align:left;vertical-align:top}
details.keys{background:var(--card);border:2px solid var(--ink);border-radius:14px;padding:10px 14px}
</style></head><body><div class="pv">
<h1>Daily teaser preview</h1>
<p class="muted">This page shows what a visitor sees on the home page (Ages 6-8) and on each level page. Nothing here is live: the real site is unchanged. Step through days, or press the midnight buttons to see the puzzle change at 00:00 Singapore time.</p>
<div class="ctl">
<label>Level<select id="lv"><option value="1">Ages 6-8 (home page)</option><option value="2">Ages 7-9</option><option value="3">Ages 8-10</option><option value="4">Ages 9-11</option><option value="5">Ages 10-12</option><option value="6">Ages 11-13</option></select></label>
<label>Singapore date<input type="date" id="dt" value="2026-11-01" min="2026-10-24" max="2028-03-31"></label>
<label>Singapore time<input type="time" id="tm" value="12:00" step="1"></label>
<button class="btn sm alt" id="prev" type="button">Previous day</button><button class="btn sm alt" id="next" type="button">Next day</button>
<button class="btn sm" id="before" type="button">23:59:30 on this date</button><button class="btn sm" id="after" type="button">00:00:30 on the next date</button>
</div>
<div class="status" id="status"></div>
<section class="sec" style="padding:0"><div class="pzcard"><div class="pzl" id="pzBox"></div><div class="pzr"><h3>In class, the answer is only half the job</h3><p class="muted">Children then explain how they know. This panel stays as it is on the real page.</p></div></div></section>
<details class="keys"><summary><b>All puzzles for this level</b> (answer key for you, not shown to children)</summary><div id="keys"></div></details>
<p class="small muted">Fallback rule: months that are not released yet use the first released month, chosen by day number modulo its length. Released months: <span id="rel"></span>.</p>
</div>
<script>''' + js + '''</script>
<script>
var DATA=''' + data + ''';
var SGT=8*3600000;
function $(i){return document.getElementById(i)}
var ctl=null, nowMs=Date.now();
function parse(){var d=$("dt").value.split("-"),t=($("tm").value||"12:00:00").split(":");return Date.UTC(+d[0],+d[1]-1,+d[2],+t[0],+t[1],+(t[2]||0))-SGT}
function fmtSGT(ms){var d=new Date(ms+SGT);return d.toISOString().replace("T"," ").slice(0,19)+" SGT"}
function mount(){
  var lv=+$("lv").value;
  nowMs=parse();
  var box=$("pzBox");box.innerHTML="";
  ctl=MiTeaser.init({box:box,level:lv,ages:DATA.ages[lv],pool:DATA.pools[lv],listen:false,now:function(){return nowMs},
    data:function(l,mm){return DATA.months["L"+l+"-"+mm]||null}});
  var s=box.getAttribute("data-teaser-source");
  $("status").textContent="Simulated time: "+fmtSGT(nowMs)+"  |  date key "+box.getAttribute("data-teaser-date")+"  |  puzzle "+box.getAttribute("data-teaser")+"  |  "+(s==="month"?"from the released batch":"fallback (this month has no released batch)");
  var rows=DATA.full[lv].map(function(e){return "<tr><td>"+e.date+"</td><td>"+e.topic+"</td><td>"+e.q.replace(/</g,"&lt;")+"</td><td><b>"+e.shown+"</b></td></tr>"}).join("");
  $("keys").innerHTML='<table class="keys"><tr><th>Date</th><th>Topic</th><th>Question</th><th>Answer</th></tr>'+rows+"</table>";
}
function shift(n){var d=$("dt").value.split("-");var x=new Date(Date.UTC(+d[0],+d[1]-1,+d[2]+n));$("dt").value=x.toISOString().slice(0,10);mount()}
$("lv").onchange=mount;$("dt").onchange=mount;$("tm").onchange=mount;
$("prev").onclick=function(){shift(-1)};$("next").onclick=function(){shift(1)};
$("before").onclick=function(){$("tm").value="23:59:30";mount()};
$("after").onclick=function(){$("tm").value="00:00:30";shift(1)};
$("rel").textContent=DATA.released.join(", ");
mount();
</script></body></html>
'''
    open(os.path.join(OUT, 'index.html'), 'w', encoding='utf-8').write(page)
    print('wrote', os.path.join(OUT, 'index.html'), len(page), 'bytes')


if __name__ == '__main__':
    main()
