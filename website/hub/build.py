import json,re,html as H
exec(open('qa.py').read())
css=open('../lp_parts.txt').read()
def strip(s): return re.sub('<[^>]+>','',s)
schema={"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":strip(a+' '+' '.join(body))}} for c,i,q,a,body,*src in QA]}
cname=dict(CATS)
cards=''
for c,i,q,a,body,*src in QA:
    s=src[0] if src else None
    cards+=f'''<article class="th" id="{i}" data-cat="{c}"><button class="thhead" aria-expanded="false" aria-controls="b-{i}"><span class="ctag c-{c}">{cname[c]}</span><h3>{H.escape(q)}</h3><p class="prev">{H.escape(a)}</p><span class="meta"><span class="who">Answered by a Math Inquirers teacher</span><span class="more">Read answer</span></span></button>
<div class="thbody" id="b-{i}" hidden><p class="short"><b>Short answer:</b> {H.escape(a)}</p>{''.join(x if x.startswith('<') else '<p>'+H.escape(x)+'</p>' for x in body)}{f'<p class="src">Source: <a href="{s[1]}" target="_blank" rel="noopener">{H.escape(s[0])}</a></p>' if s else ''}<div class="acts"><button class="btn sm alt" data-help="{i}">This helped</button><button class="btn sm alt" data-link="{i}">Copy link</button></div></div></article>'''
cats=''.join(f'<button class="cat" data-c="{k}"><span class="dot c-{k}"></span>{v}<span class="n">{sum(1 for x in QA if x[0]==k)}</span></button>' for k,v in CATS)
extra='''
[hidden]{display:none!important}
.hubhead{display:grid;gap:12px}
.search{display:flex;gap:10px;flex-wrap:wrap}.search input{flex:1;min-width:220px;font-size:17px;padding:13px 16px;border:2.5px solid var(--ink);border-radius:14px;background:var(--card)}
.layout{display:grid;grid-template-columns:260px 1fr;gap:24px;align-items:start}
.side{display:grid;gap:8px;position:sticky;top:12px}
.cat{display:flex;align-items:center;gap:10px;text-align:left;font:800 14.5px var(--body);color:var(--fg);background:var(--card);border:2px solid var(--line);border-radius:12px;padding:10px 12px;cursor:pointer}
.cat.on{border-color:var(--ink);box-shadow:3px 3px 0 var(--ink)}
.cat .n{margin-left:auto;font-weight:700;color:var(--muted)}
.dot{width:12px;height:12px;border-radius:3px;border:1.5px solid var(--ink);flex:none}
.c-p1{background:#FFF0C4}.c-topics{background:#D6E9FB}.c-home{background:#D3F1E4}.c-strong{background:#FFE2D6}.c-mi{background:#E6DFFB}
.list{display:grid;gap:14px;min-width:0}
.th{background:var(--card);border:2.5px solid var(--ink);border-radius:18px;box-shadow:4px 4px 0 var(--ink);overflow:hidden}
.thhead{display:grid;gap:6px;width:100%;text-align:left;background:none;border:0;color:var(--fg);padding:16px 18px;cursor:pointer;font:inherit}
.thhead h3{font-size:20px}
.ctag{justify-self:start;font:800 11.5px var(--body);letter-spacing:.06em;text-transform:uppercase;color:#1B2A49;border:1.5px solid #1B2A49;border-radius:6px;padding:2px 8px}
.prev{color:var(--muted)}
.th[open-state] .prev{display:none}
.meta{display:flex;justify-content:space-between;gap:10px;font-size:13px;font-weight:700;color:var(--teal);flex-wrap:wrap}
.more{color:var(--fg);text-decoration:underline}
.thbody{padding:0 18px 18px;display:grid;gap:10px;border-top:2px dashed var(--line);padding-top:14px}
.thbody ul,.thbody ol{padding-left:20px;display:grid;gap:4px}
.short{background:var(--soft);border-radius:10px;padding:10px 12px}
.src{font-size:13px;color:var(--muted)}
.acts{display:flex;gap:8px;flex-wrap:wrap}
.ask{display:grid;gap:10px}
.note{font-size:13.5px;color:var(--muted)}
.empty{padding:24px;text-align:center;color:var(--muted)}
@media (max-width:820px){.layout{grid-template-columns:1fr}.side{position:static;grid-template-columns:1fr 1fr}}
'''
page=f'''<title>Math Inquirers Parent Questions</title>
<meta name="claude:viewport-fit-sides" content="cover">
<meta name="description" content="Answers to common questions from Singapore parents about Primary 1 maths, getting ready for P1, helping at home and stretching strong learners.">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600&family=Nunito+Sans:wght@400;600;800&display=swap">
<script type="application/ld+json">{json.dumps(schema,ensure_ascii=False)}</script>
<style>{css}{extra}</style>
<div class="wrap">
<header class="bar"><span class="brand"><i>?</i><span>Math Inquirers</span></span><nav class="nav" aria-label="Site"><span class="tab" aria-current="true">Parent questions</span><span class="tab">Puzzles</span><span class="tab">Program</span><span class="btn yel sm" style="margin-left:6px;padding:8px 16px">Register</span></nav></header>
<main>
<section class="hero" style="grid-template-columns:1fr"><div class="hubhead"><span class="eyebrow">Parent questions</span><h1>Questions parents ask us about <mark>Primary 1</mark> maths</h1><p class="lead">Straight answers from our teachers on getting ready for P1, the topics your child will meet, helping at home and stretching strong learners.</p><div class="search"><input id="q" type="search" placeholder="Search, e.g. number bonds, GEP, holidays" aria-label="Search questions"></div></div></section>
<section class="layout"><aside class="side" aria-label="Topics"><button class="cat on" data-c="all"><span class="dot" style="background:#fff"></span>All questions<span class="n">{len(QA)}</span></button>{cats}
<div class="card ask" style="margin-top:10px"><h3 style="font-size:18px">Ask a question</h3><textarea id="askq" placeholder="Type your question" style="min-height:80px"></textarea><button class="btn sm" id="askb">Send question</button><div id="askmsg"></div><p class="note">We answer the most common questions here. Your name is never shown.</p></div></aside>
<div class="list" id="list">{cards}<div class="empty" id="none" hidden>No questions match. Try another word, or ask us.</div></div></section>
</main>
<footer><div><b>Math Inquirers</b><p style="margin-top:6px">Primary 1 maths enrichment by Preciouslyours Pte Ltd, Singapore. Not affiliated with MOE.</p></div><div><b>About these answers</b><p style="margin-top:6px">Questions are ones parents commonly ask us. Answers are written by our teachers and checked against MOE sources where facts are involved.</p></div><div><b>Contact</b><p style="margin-top:6px">hello@mathinquirers.example (to confirm)</p></div></footer>
</div>
<script>
(function(){{"use strict";
var arts=[].slice.call(document.querySelectorAll(".th")),cat="all";
function open(a,on){{var b=a.querySelector(".thbody"),h=a.querySelector(".thhead");b.hidden=!on;h.setAttribute("aria-expanded",on);a.querySelector(".more").textContent=on?"Hide answer":"Read answer";a.querySelector(".prev").hidden=on}}
function filter(){{var t=(document.getElementById("q").value||"").toLowerCase().trim(),n=0;arts.forEach(function(a){{var ok=(cat==="all"||a.dataset.cat===cat)&&(!t||a.textContent.toLowerCase().indexOf(t)>=0);a.hidden=!ok;if(ok)n++}});document.getElementById("none").hidden=n>0}}
document.addEventListener("click",function(e){{var h=e.target.closest(".thhead");if(h){{var a=h.parentNode;open(a,a.querySelector(".thbody").hidden);return}}
var c=e.target.closest(".cat");if(c){{cat=c.dataset.c;document.querySelectorAll(".cat").forEach(function(x){{x.classList.toggle("on",x===c)}});filter();return}}
var hp=e.target.closest("[data-help]");if(hp){{hp.textContent="Thanks for telling us";hp.disabled=true;return}}
var lk=e.target.closest("[data-link]");if(lk){{var u=location.href.split("#")[0]+"#"+lk.dataset.link;if(navigator.clipboard&&navigator.clipboard.writeText)navigator.clipboard.writeText(u).then(function(){{lk.textContent="Link copied"}},function(){{lk.textContent=u}});else lk.textContent=u;return}}
if(e.target.id==="askb"){{var v=document.getElementById("askq").value.trim();document.getElementById("askmsg").innerHTML=v?'<div class="msg ok">Thank you. We will add an answer if other parents ask this too.</div>':'<div class="msg no">Type your question first.</div>';if(v)document.getElementById("askq").value="";}}
}});
document.getElementById("q").addEventListener("input",filter);
var h=(location.hash||"").slice(1),t=h&&document.getElementById(h);if(t&&t.classList.contains("th")){{open(t,true);t.scrollIntoView()}}
}})();
</script>'''
open('parent_questions.html','w').write(page)
print(len(page))
