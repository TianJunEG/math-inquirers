from level_pages import LEVEL_CSS, level_index_cards, register_by, register_by_line
import interest_ui
WA_NUM,WA_SHOW='6598805962','+65 9880 5962'   # business WhatsApp (CONFIG in the page script and the no-JS note are filled from these)
css=open('lp_parts.txt').read()+LEVEL_CSS
hero=open('lp_hero.js').read()
interest_js=open('interest.js').read()
extra='''
.draft{border:2px dashed var(--coral);background:var(--peach);border-radius:14px;padding:10px 14px;font-size:14px;margin-top:6px}
.draft b{font-weight:800}
.eb{flex-wrap:wrap;display:inline-flex;align-items:center;gap:10px;background:var(--yellow);color:#1B2A49;border:2.5px solid #1B2A49;border-radius:16px;padding:8px 14px;font-weight:800;box-shadow:4px 4px 0 #1B2A49;justify-self:start}
.eb s{opacity:.6;font-weight:600}
.eb .big{font:600 26px var(--head);white-space:nowrap}
.pricebox{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.pcard{border:2.5px solid var(--ink);border-radius:22px;padding:20px;display:grid;gap:6px;background:var(--card)}
.pcard.hot{background:var(--soft);box-shadow:6px 6px 0 var(--ink)}
.pcard .amt{font:600 44px var(--head);line-height:1}
.cls{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:16px}
.cls label{cursor:pointer;display:grid;gap:6px;border:2.5px solid var(--ink);border-radius:20px;padding:16px;background:var(--card);box-shadow:4px 4px 0 var(--ink)}
.cls label:has(input:checked){background:var(--mint)}
.cls input{width:auto;accent-color:var(--teal)}
.waout{display:grid;gap:10px}
.waout pre{white-space:pre-wrap;background:var(--bg);border:2px dashed var(--line);border-radius:12px;padding:12px;font:14px/1.5 var(--body);margin:0}
@media (max-width:820px){.pricebox{grid-template-columns:1fr}}
'''+interest_ui.CSS
html='''<title>Math Inquirers December Holiday Program</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600&family=Nunito+Sans:wght@400;600;800&display=swap">
<style>'''+css+extra+'''</style>
<div class="wrap">
<a class="skip" href="#top">Skip to main content</a>
<header class="bar"><a class="brand" href="#top" style="text-decoration:none"><i>?</i><span>Math Inquirers</span></a><nav class="nav" aria-label="Page"><a class="tab" href="#program" style="text-decoration:none">Program</a><a class="tab" href="#classes" style="text-decoration:none">Classes</a><a class="tab" href="#levels" style="text-decoration:none">Levels</a><a class="tab" href="#price" style="text-decoration:none">Price</a><a class="tab" href="#faq" style="text-decoration:none">FAQ</a><a class="tab" href="/shop/" style="text-decoration:none" data-shoplink>Shop<span class="cartn" data-cartn hidden></span></a><a class="btn yel sm" href="#register" style="margin-left:6px;padding:8px 16px">Register</a></nav></header>

<main id="top">
<section class="hero"><div class="sec"><span class="eyebrow">November beta · Live online maths for ages 6 to 13</span><h1>Math Inquirers <mark>Holiday</mark> Program</h1><p class="slogan">Notice it. Test it. Explain why.</p><p class="lead">Maths enrichment for curious children in Singapore. Ten hands-on lessons where children solve puzzles, test ideas with objects and explain their answers, live online in small groups of up to 8. Six levels by age: pick your child's level, then a class time.</p>
<div class="eb" id="ebBadge"><span>November beta</span><span class="big" id="ebPrice"></span><s id="ebFull"></s><span id="ebLeft" style="font-weight:700"></span></div>
<div class="row" style="margin-top:6px"><a class="btn yel" href="#levels">Choose your child's level</a><a class="btn ghost" href="#classes">See class times</a></div></div><div id="art"></div></section>

<section class="facts" id="program"><div class="fact"><div class="v">10 lessons</div><div class="l">90 minutes each, over 5 weeks</div></div><div class="fact"><div class="v">Up to 8</div><div class="l">children in each group</div></div><div class="fact"><div class="v">Live online</div><div class="l">from home, workbook posted to you</div></div><div class="fact"><div class="v">All included</div><div class="l">workbook, kit, certificate</div></div></section>

<section class="sec"><div class="shead"><span class="eyebrow">How children learn</span><h2>Four habits of a young mathematician</h2><p class="muted">Every lesson follows the same four steps, so children learn how to think, not just what to write.</p></div><div class="rules4">
<div class="rule"><b>1</b><h3>Notice the pattern</h3><p class="muted small">Look closely before rushing to an answer.</p></div>
<div class="rule"><b>2</b><h3>Test it with objects</h3><p class="muted small">Counters, coins and strips to check an idea.</p></div>
<div class="rule"><b>3</b><h3>Check your answer</h3><p class="muted small">Does it make sense? Try another way.</p></div>
<div class="rule"><b>4</b><h3>Explain why</h3><p class="muted small">Say or draw why it works. This is where learning sticks.</p></div></div></section>

<section class="sec" id="design"><div class="shead"><span class="eyebrow">How it is designed</span><h2>A maths enrichment program, inspired by research-based approaches used in gifted education</h2><p class="muted">For curious, capable children who enjoy thinking hard about maths, whatever their starting point.</p></div><div class="rules4">
<div class="rule"><b>&#8593;</b><h3>Low floor, high ceiling</h3><p class="muted small">Every task has an easy way in and room to go further, so no child waits and no child is stuck.</p></div>
<div class="rule"><b>?</b><h3>Open investigations</h3><p class="muted small">Find every way, spot the pattern, make up your own puzzle, and ask "what if?".</p></div>
<div class="rule"><b>&#9998;</b><h3>Explain and look back</h3><p class="muted small">Children say why it works, try a second method, and note what was hard.</p></div>
<div class="rule"><b>&#9733;</b><h3>Beyond the syllabus</h3><p class="muted small">We extend thinking beyond the school syllabus with depth and reasoning, not by racing ahead.</p></div></div>
<p class="muted small" style="margin-top:14px">Frameworks that inspire the design include low-floor, high-ceiling tasks, P&oacute;lya's problem-solving steps and mathematical habits of mind. We do not identify or test for giftedness, we are not a GEP preparation course, and we do not promise exam or competition results.</p></section>

<section class="sec"><div class="shead"><span class="eyebrow">The 10 lessons</span><h2>What Level 1 (ages 6-8) covers</h2><p class="muted">Every level has its own ten lessons. See them on each level page below.</p></div><div class="lessons" id="lessons"></div></section>

<section class="two"><div class="tile yel"><span class="tag">Your child takes home</span><ul style="padding-left:18px;display:grid;gap:6px"><li>A printed Math Inquirers workbook, posted to your home</li><li>The Inquirer Kit: cut-out pages at the back of the workbook (for Ages 6-8: play coins, ten-frames, counters, number strips and tiles)</li><li>An Inquiry Journal page in the workbook, stamped after every lesson</li><li>A certificate page, signed on Challenge Day</li></ul></div>
<div class="tile mint"><span class="tag">You get</span><ul style="padding-left:18px;display:grid;gap:6px"><li>A short note each week: what we did and one thing to try at home</li><li>Notes on where your child is ready to be stretched further</li><li>Free weekly puzzles by email</li></ul><p class="small muted">Nothing to buy. We post the printed workbook (with the Inquirer Kit cut-out pages) to your home before the first lesson. Singapore addresses only.</p></div></section>

<section class="sec" id="tryit"><div class="shead"><span class="eyebrow">Try one now</span><h2>A taste of Lesson 1</h2></div><div class="pzcard"><div class="pzl"><span class="tag">Ages 6-8 · Frog hops</span><div class="big">3, 6, 9, ?</div><p style="font-size:18px">A frog starts at 0 and hops 3 steps each time: 3, 6, 9 … Where does it land on its 7th hop?</p><div class="row"><input id="pzA" aria-label="Your answer" placeholder="Your answer" inputmode="numeric" style="max-width:170px"><button class="btn yel" id="pzCheck" type="button">Check</button></div><div id="pzMsg"></div></div><div class="pzr"><h3>In class, the answer is only half the job</h3><p class="muted">Children then explain how they know: counting on a number line, adding 3 seven times, or spotting that every landing spot is in the 3 times table. Hearing three different ways is how thinking grows.</p><a class="btn sm alt" href="#register" style="justify-self:start">Register for the program</a></div></div></section>

<section class="sec" id="classes"><div class="shead"><span class="eyebrow">November beta · Singapore time</span><h2>Choose a group</h2><p class="muted">Lessons start in the week of <b>Mon 23 Nov</b> (first lessons Tue 24 to Fri 27 Nov, see each group). Each group meets twice a week for 5 weeks, 90 minutes a lesson, live online, up to 8 children. If a group fills, we open another.</p><div class="draft">Beta fee: S$<span id="betaPer"></span> a lesson, S$<span id="betaTot"></span> for all 10 lessons. The fee includes the printed workbook posted to your home. We confirm payment details on WhatsApp after you register.</div></div><div class="sessions" id="sess"></div><p class="small muted" style="margin-top:12px">No lessons on Fri 25 Dec (Christmas Day). Otherwise each group keeps the same two weekly times for all 5 weeks; where the final week differs it is shown on the card.</p><p style="margin-top:8px"><b>None of these times suit you?</b> <a href="#request-time">Request another time</a>. Each card also lists other times we may open if enough families are interested.</p></section>

<section class="sec" id="price"><div class="shead"><span class="eyebrow">Price</span><h2>What it costs</h2></div><div class="pricebox"><div class="pcard hot"><span class="tag" style="justify-self:start;font:800 12px var(--body);text-transform:uppercase;letter-spacing:.08em;border:2px solid var(--ink);border-radius:999px;padding:3px 10px;background:var(--card)">November beta</span><div class="amt" id="pE"></div><p id="pEnote"></p></div><div class="pcard"><span class="tag" style="justify-self:start;font:800 12px var(--body);text-transform:uppercase;letter-spacing:.08em;border:2px solid var(--ink);border-radius:999px;padding:3px 10px">After the beta</span><p>We have not set a regular price yet. Families who join the beta and give feedback will be offered an introductory price on the regular program. We tell you the details after the beta, before any regular program starts.</p></div></div><p class="small muted">For 15 hours of teaching and the printed workbook posted to your home (with the cut-out kit pages, Inquiry Journal page and certificate). No payment now: we confirm your place first and then send payment details.</p></section>

<section class="sec" id="levels"><div class="shead"><span class="eyebrow">Six levels</span><h2>Choose a level by age</h2><p class="muted">Each level has its own page with the ten lessons, what is in the kit, a sample puzzle, placement guidance and class times.</p></div><div class="lvgrid">'''+level_index_cards()+'''</div></section>

<section class="sec" id="level"><div class="shead"><span class="eyebrow">Placement</span><h2>Which level is right for my child?</h2></div>
<p class="muted">Levels are named by age, and each spans three ages and overlaps the next, so children can join at the level that suits how they are learning now. Start with the level that matches your child's school year:</p>
<ul><li>Ages 6-8 (builds on Primary 1 maths)</li><li>Ages 7-9 (builds on Primary 2 maths)</li><li>Ages 8-10 (builds on Primary 3 maths)</li><li>Ages 9-11 (builds on Primary 4 maths)</li><li>Ages 10-12 (builds on Primary 5 maths)</li><li>Ages 11-13 (maths + coding bridge, after PSLE)</li></ul>
<p>Take the free 30-minute diagnostic for the level that matches your child's school year (the Math Inquirers Placement Check for that level). Then:</p>
<ul><li>The check is scored out of 10. 7 to 10: enrol at that level.</li><li>4 to 6: enrol at that level (the tutor will note that support may help), or choose one level down.</li><li>0 to 3: we recommend one level down.</li><li>If it was too easy (9 or 10 out of 10), your child may also try the diagnostic one level up.</li></ul>
<p>You have the final say. You can change the level before lesson 1 at no cost, and the price is the same at every level. Ages 6-8 is the lowest level: if your child finds it hard, they start with the free taster and a tutor chat.</p></section>

<section class="band yel" id="register"><div class="sec"><img src="/shop/mi.png" width="63" height="75" alt="Mi the dolphin waving hello" style="justify-self:start"><span class="eyebrow">Register</span><h2>Hold a seat</h2><p class="muted">Fill this in and send it to us on WhatsApp. We reply within 2 working days to confirm the group and send payment details. Groups are small, so seats go in order of registration.</p><p class="regby" id="regby">__REGBY__</p><p class="small">WhatsApp: <b id="waShow"></b><span id="emLine1"><br>Email: <b id="emShow"></b></span></p></div>
<form class="card" id="reg"><div class="grid2"><div class="field"><label for="r1">Parent's name</label><input id="r1" autocomplete="name"></div><div class="field"><label for="r2">Mobile</label><input id="r2" type="tel" autocomplete="tel"></div></div>
<div class="grid2"><div class="field"><label for="r3">Child's name</label><input id="r3"></div><div class="field"><label for="r4">Level</label><select id="r4"><option>Ages 6-8 (builds on Primary 1 maths)</option><option>Ages 7-9 (builds on Primary 2 maths)</option><option>Ages 8-10 (builds on Primary 3 maths)</option><option>Ages 9-11 (builds on Primary 4 maths)</option><option>Ages 10-12 (builds on Primary 5 maths)</option><option>Ages 11-13 (maths + coding bridge, after PSLE)</option></select></div></div>
<div class="field"><label for="r5">Group</label><select id="r5"></select></div>
<div class="field"><label for="d1">Delivery address in Singapore <span class="muted" style="font-weight:600">(we post the printed workbook here)</span></label><input id="d1" autocomplete="street-address" placeholder="Block or house no., street, unit no."></div>
<div class="grid2"><div class="field"><label for="d2">Postal code</label><input id="d2" inputmode="numeric" maxlength="6" autocomplete="postal-code" placeholder="6 digits"></div><div class="field"><label for="d3">Parcel name and phone <span class="muted" style="font-weight:600">(only if not the parent above)</span></label><input id="d3" placeholder="e.g. Grandma Tan, 9123 4567"></div></div>
<div class="field"><label for="r6">Anything we should know? <span class="muted" style="font-weight:600">(optional)</span></label><textarea id="r6" style="min-height:70px"></textarea></div>
<label class="check" for="r7"><input type="checkbox" id="r7"><span>I agree to Math Inquirers (Preciouslyours Pte Ltd) using my details to arrange the class and contact me about it.</span></label>
<label class="check" for="r8"><input type="checkbox" id="r8"><span>I have read and agree to the <a href="/terms/" target="_blank">terms and refund policy</a>.</span></label>
<label class="check" for="r9"><input type="checkbox" id="r9"><span>I understand lessons are recorded (the tutor and the shared screen) and shared only with enrolled families of my child's group. See the <a href="/privacy/" target="_blank">privacy and recording notice</a>.</span></label>
<label class="check" for="r10"><input type="checkbox" id="r10"><span>I am the parent or guardian, and I agree to my child's work and answers being kept for the program as described in the privacy notice.</span></label>
<label class="check" for="r12"><input type="checkbox" id="r12"><span>I agree to Math Inquirers giving my delivery name, address and phone number to our printer and courier, only to print and deliver my child's workbook, and to delete them 30 days after the parcel is confirmed delivered, or after any resend is finished, whichever is later. See the <a href="/privacy/" target="_blank">privacy notice</a>.</span></label>
<label class="check" for="r11"><input type="checkbox" id="r11"><span>Optional: you may quote my feedback without my child's name.</span></label>
<div id="regMsg" role="status" aria-live="polite"></div><button class="btn" type="submit">Send on WhatsApp</button></form></section>

__INTEREST_FORM__

<section class="sec faq" id="faq"><div class="shead"><span class="eyebrow">Questions</span><h2>Parents often ask</h2></div>
<details><summary>Who is it for?</summary><p>Children aged 6 to 13 who enjoy puzzles or finish school work easily. There are six levels, by age and school year (Level 1 builds on Primary 1 maths). K2 children starting Primary 1 in 2027 are welcome in Level 1 after a free 15-minute readiness check, which we arrange after you register. Every lesson has three kinds of questions, Start here, Think harder and Go further, so every child is stretched.</p></details>
<details><summary>Is it linked to MOE or the GEP?</summary><p>No. Math Inquirers is an independent maths enrichment program. It is inspired by research-based approaches used in gifted education, such as low-floor, high-ceiling tasks and explaining why, but we do not identify or test for giftedness, and it is not a GEP preparation course.</p></details>
<details><summary>Who teaches?</summary><p>Lessons are planned and led by an experienced Singapore primary school maths teacher, using the Math Inquirers lesson plans, slides and workbook.</p></details>
<details><summary>What if my child misses a lesson?</summary><p>Every lesson is recorded, so your child can watch it later and use the online practice. Your child can make up a missed lesson once by joining the same lesson in another class of the same level, if a seat is free. Beta fees are not refunded.</p></details>
<details><summary>How does online work?</summary><p>Live video lessons with the same group of up to 8. We post the printed workbook (with the kit cut-out pages) to you before the first lesson. All your child needs is a laptop or tablet with a camera, on a table with space for the kit.</p></details>
<details><summary>What will it cost after the beta?</summary><p>We have not set the regular price yet. We plan an introductory price for the first families after the beta, including those who join the beta and give feedback. We will tell you the amount and how long it lasts after the beta, before any regular program starts.</p></details>
<details><summary>Can we ask for a different time?</summary><p>Yes. Use <a href="#request-time">Request another time</a> to tell us the level and the days and times that suit you. The times shown as "not open yet" are placeholders we may open if enough families are interested. Nothing is booked or charged when you ask.</p></details>
<details><summary>How does the workbook reach us?</summary><p>We print your child's workbook (the Inquirer Kit cut-out pages are at the back) and post it to your home in Singapore before the first lesson, included in the beta fee. We need a delivery address and postal code when you register. __REGBYFAQ__ If a parcel is late or arrives damaged, tell us within 7 days and we resend it once at no cost. <span class="small muted">[parcel policy: draft default, to confirm]</span></p></details>
<details><summary>How do I pay?</summary><p>There is nothing to pay when you register. We confirm the group first, then send payment details.</p></details>
<details><summary>What if we need to cancel, or miss a lesson?</summary><p>The November beta fee is not refunded. If your child cannot come to a lesson, they can make it up once by joining the same lesson in another class of the same level, if a seat is free. Every lesson is also recorded, so your child can watch it and use the online practice. The printed workbook and kit are yours to keep. If we cancel a lesson or a group and cannot reschedule, we refund every lesson not held. Message us on WhatsApp or email to arrange a make-up.</p></details></section>
</main>
<footer><div><b>Math Inquirers</b><p style="margin-top:6px">A maths holiday program for ages 6 to 13 by Preciouslyours Pte Ltd, Singapore. Not affiliated with MOE or the Gifted Education Programme.</p></div><div><b>Contact</b><p style="margin-top:6px">WhatsApp: <span id="waFoot"></span><span id="emLine2"><br>Email: <span id="emFoot"></span></span></p><p style="margin-top:6px"><a href="/shop/">Shop: extension workbooks (coming soon)</a></p></div><div><b>Your details</b><p style="margin-top:6px">We use your details only to arrange the class, post the workbook and reply to you, in line with the PDPA. <a href="/terms/">Terms</a> · <a href="/privacy/">Privacy</a></p></div></footer>
</div>
<!--PORTAL_CONFIG-->
<script>
(function(){
"use strict";
/* ---- settings to confirm ---- */
var CONFIG={
  whatsapp:"__WA__",           /* number with 65, no spaces */
  whatsappShow:"__WASHOW__",
  email:"",                        /* no email yet: the Email lines are hidden while this is empty */
    beta:__BETA__,
  delivery:{registerBy:"__REGBYLABEL__"},   /* set once in data/beta_schedule.json (delivery.register_by); shown on every page and in the WhatsApp message */
  classes:__CLASSES__
};
var INTEREST=__INTEREST__;
var LESSONS=[["Count with the Frog","Number patterns and skip counting"],["Number Bond Inquiry","Parts and wholes to 20"],["Let's Plan the Fruit Party","Picture graphs and tallies"],["Pattern Inquiry","Shape and number patterns"],["Mystery Number","Working backwards"],["Coin Combos","Money and finding every way"],["Shape Safari","2D shapes, sides and corners"],["Logic Lab","Clues, sorting and Venn diagrams"],["Measure It!","Length with non-standard units"],["Challenge Day","Mixed puzzles and the certificate"]];
function $(id){return document.getElementById(id)}
function esc(s){return String(s).replace(/[&<>"']/g,function(c){return{"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]})}
'''+hero+'''
$("art").outerHTML=heroArt();
$("ebPrice").textContent="S$"+CONFIG.beta.per+" a lesson";
$("ebFull").textContent="";
$("ebLeft").textContent="S$"+CONFIG.beta.total+" for all 10 lessons";
$("pE").textContent="S$"+CONFIG.beta.per+" a lesson";
$("pEnote").textContent="November beta: S$"+CONFIG.beta.total+" for all 10 lessons. The beta fee is not refunded; a child can make up one lesson once by joining another class. See the terms.";
$("lessons").innerHTML=LESSONS.map(function(l,i){return '<div class="lesson"><div class="n">'+(i+1)+'</div><div class="t">'+l[0]+'</div><div class="s">'+l[1]+'</div></div>'}).join("");
$("betaPer").textContent=CONFIG.beta.per;$("betaTot").textContent=CONFIG.beta.total;
function t12(t){var p=t.split(":"),h=+p[0],m=p[1],a=h>=12?"pm":"am";h=h%12||12;return h+":"+m+a}
function slotText(c){return c.sessions.map(function(x){return x.day+" "+t12(x.start)+"–"+t12(x.end)}).join(" & ")}
$("sess").innerHTML=CONFIG.classes.map(function(c){return '<div class="session"><div class="row" style="justify-content:space-between"><span class="pill p-ok">Open</span><span class="small muted">Up to '+c.seats+' children</span></div><h3>Level '+c.level+' <span class="muted small">ages '+esc(c.ages)+'</span></h3><p>'+c.sessions.map(function(x){return '<b>'+esc(x.day)+'</b> '+esc(t12(x.start))+'–'+esc(t12(x.end))}).join('<br>')+'<br><span class="muted small">First lesson '+esc(c.first)+' · last '+esc(c.last)+(c.exc?'<br>'+esc(c.exc):'')+'<br>Live video class</span></p><a class="btn sm" href="#register" data-pick="'+c.id+'" data-level="'+c.level+'" style="justify-self:start">Choose Level '+c.level+'</a>'+(c.other||'')+'</div>'}).join("");
function fillGroups(){var lv=$("r4").selectedIndex+1;var g=CONFIG.classes.filter(function(c){return c.level===lv});$("r5").innerHTML=g.map(function(c){return '<option value="'+c.id+'">'+esc("Level "+c.level+" · "+slotText(c)+" · from "+c.first)+'</option>'}).join("")+'<option value="any">Any group for this level</option>'}
fillGroups();$("r4").addEventListener("change",fillGroups);
try{var qs=new URLSearchParams(location.search),lv=parseInt(qs.get("level"),10);if(lv>=1&&lv<=6){$("r4").selectedIndex=lv-1;fillGroups();var gp=qs.get("group");if(gp){var os=$("r5").options;for(var oi=0;oi<os.length;oi++){if(os[oi].value===gp){$("r5").selectedIndex=oi}}}}}catch(e){}
["waShow","waFoot"].forEach(function(i){$(i).textContent=CONFIG.whatsappShow});["emShow","emFoot"].forEach(function(i){$(i).textContent=CONFIG.email});if(!CONFIG.email){["emLine1","emLine2"].forEach(function(i){$(i).hidden=true})}
document.addEventListener("click",function(e){var p=e.target.closest("[data-pick]");if(p){$("r4").selectedIndex=+p.dataset.level-1;fillGroups();$("r5").value=p.dataset.pick}});
$("pzCheck").addEventListener("click",function(){var v=($("pzA").value||"").replace(/\\D/g,"");$("pzMsg").innerHTML=v==="21"?'<div class="msg ok">Correct! Now ask: how do you know? 7 hops of 3 is 21.</div>':'<div class="msg no">Not yet. Try counting along a number line in 3s.</div>'});
$("reg").addEventListener("submit",function(e){
  e.preventDefault();
  var f={p:$("r1").value.trim(),m:$("r2").value.trim(),c:$("r3").value.trim(),l:$("r4").value,g:$("r5").options[$("r5").selectedIndex].text,n:$("r6").value.trim()};
  function bad(m,el){$("regMsg").innerHTML='<div class="msg no">'+m+'</div>';if(el){el.setAttribute("aria-invalid","true");el.focus();el.addEventListener("input",function(){el.removeAttribute("aria-invalid")},{once:true})}}
  if(!f.p||!f.m||!f.c){bad('Fill in your name, mobile and your child\\'s name.',!f.p?$("r1"):!f.m?$("r2"):$("r3"));return}
  f.a=$("d1").value.trim();f.z=$("d2").value.replace(/\\s/g,"");f.d=$("d3").value.trim();
  if(!f.a||!/^\\d{6}$/.test(f.z)){bad('Add your delivery address in Singapore and its 6-digit postal code, so we can post the workbook.',!f.a?$("d1"):$("d2"));return}
  var need=["r7","r8","r9","r10","r12"].filter(function(i){return !$(i).checked});if(need.length){bad('Please tick the five required boxes (contact, terms, recording, your child\\'s work, delivery details).',$(need[0]));return}
  var price="beta S$"+CONFIG.beta.per+" a lesson, S$"+CONFIG.beta.total+" for all 10 lessons";
  var msg="Hi! I'd like to register for the Math Inquirers November Beta.\\n\\nParent: "+f.p+"\\nMobile: "+f.m+"\\nChild: "+f.c+" ("+f.l+")\\nGroup: "+f.g+"\\nPrice: "+price+(f.n?"\\nNote: "+f.n:"")+"\\nDeliver workbook to: "+(f.d||f.p+", "+f.m)+"\\nAddress: "+f.a+", Singapore "+f.z+"\\nWorkbook: printed copy posted to this address (Singapore only)"+"\\nConsents: contact, terms, recording, child's work, delivery details"+($("r11").checked?", feedback quotes":"");
  var url="https://wa.me/"+CONFIG.whatsapp+"?text="+encodeURIComponent(msg);
  $("regMsg").innerHTML='<div class="waout"><div class="msg ok">Almost done. Tap the button to send this on WhatsApp.</div><pre>'+esc(msg)+'</pre><div class="row"><a class="btn teal" href="'+url+'" target="_blank" rel="noopener">Open WhatsApp</a><button class="btn alt sm" type="button" id="cp">Copy message</button></div><p class="small muted">If WhatsApp does not open, copy the message and send it to '+esc(CONFIG.whatsappShow)+' or '+esc(CONFIG.email)+'.</p></div>';
  $("cp").addEventListener("click",function(){var b=this;if(navigator.clipboard&&navigator.clipboard.writeText)navigator.clipboard.writeText(msg).then(function(){b.textContent="Copied"},function(){b.textContent="Select the text above to copy"});else b.textContent="Select the text above to copy"});
});
'''+interest_js+'''
})();
</script>
<script src="/shop/cart.js" defer></script>'''
import json
sch=json.load(open('data/beta_schedule.json'))
import datetime as _dt
def _t12(t):
    h,m=map(int,t.split(':')); return '%d:%02d%s'%((h%12) or 12,m,'pm' if h>=12 else 'am')
def _exc(g):
    for l in g['lessons']:
        if l.get('moved'):
            return 'Week 5: %s %s–%s (not Fri 25 Dec)'%(_dt.date.fromisoformat(l['date']).strftime('%a %-d %b'),_t12(l['start']),_t12(l['end']))
    return ''
def _faq_regby(sch):
    return 'Register by %s so it arrives in time; if you register later, we send the workbook as a PDF to print at home and post the printed copy if we can.' % register_by(sch)[0]
_slots=interest_ui.load_slots()
cls=[dict(id=g['id'],level=g['level'],ages=g['ages'],seats=g['seats'],sessions=g['sessions'],first=g['first'],last=g['last'],exc=_exc(g),other=interest_ui.other_times_block(g['level'],_slots)) for g in sch['groups']]
_int=dict(consent=interest_ui.CONSENT_VERSION,bands=dict(interest_ui.AGE_BANDS),levels={n:'Level %d (ages %s)'%(n,a) for n,a in interest_ui.LEVEL_AGES.items()})
html=html.replace('__REGBYFAQ__',_faq_regby(sch)).replace('__REGBYLABEL__',register_by(sch)[0]).replace('__REGBY__',register_by_line(sch)).replace('__INTEREST_FORM__',interest_ui.form_section(WA_NUM,WA_SHOW)).replace('__WASHOW__',WA_SHOW).replace('__WA__',WA_NUM).replace('__INTEREST__',json.dumps(_int)).replace('__CLASSES__',json.dumps(cls)).replace('__BETA__',json.dumps(dict(per=sch['price']['per_lesson'],total=sch['price']['total'])))
open('mi_signup.html','w').write(html)
print(len(html))
