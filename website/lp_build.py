css=open('lp_parts.txt').read()
hero=open('lp_hero.js').read()
extra='''
.draft{border:2px dashed var(--coral);background:var(--peach);border-radius:14px;padding:10px 14px;font-size:14px;margin-top:6px}
.draft b{font-weight:800}
.eb{display:inline-flex;align-items:center;gap:10px;background:var(--yellow);color:#1B2A49;border:2.5px solid #1B2A49;border-radius:16px;padding:8px 14px;font-weight:800;box-shadow:4px 4px 0 #1B2A49;justify-self:start}
.eb s{opacity:.6;font-weight:600}
.eb .big{font:600 26px var(--head)}
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
'''
html='''<title>Math Inquirers December Holiday Program</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600&family=Nunito+Sans:wght@400;600;800&display=swap">
<style>'''+css+extra+'''</style>
<div class="wrap">
<header class="bar"><a class="brand" href="#top" style="text-decoration:none"><i>?</i><span>Math Inquirers</span></a><nav class="nav" aria-label="Page"><a class="tab" href="#program" style="text-decoration:none">Program</a><a class="tab" href="#classes" style="text-decoration:none">Classes</a><a class="tab" href="#price" style="text-decoration:none">Price</a><a class="tab" href="#faq" style="text-decoration:none">FAQ</a><a class="btn yel sm" href="#register" style="margin-left:6px;padding:8px 16px">Register</a></nav></header>
<div class="draft" id="draft"><b>Draft for Jasmine:</b> class times, the WhatsApp number and contact email are placeholders marked "to confirm". Remove this note before sharing.</div>
<main id="top">
<section class="hero"><div class="sec"><span class="eyebrow">December holidays 2026 · Primary 1</span><h1>Math Inquirers <mark>Holiday</mark> Program</h1><p class="slogan">Notice it. Test it. Explain why.</p><p class="lead">Ten hands-on lessons where children solve puzzles, test ideas with objects and explain their answers. Small groups of up to 8, face to face or online.</p>
<div class="eb" id="ebBadge"><span>Price</span><span class="big" id="ebPrice"></span><span id="ebLeft" style="font-weight:700"></span></div>
<div class="row" style="margin-top:6px"><a class="btn yel" href="#register">Register now</a><a class="btn ghost" href="#classes">See class times</a></div></div><div id="art"></div></section>

<section class="facts" id="program"><div class="fact"><div class="v">10 lessons</div><div class="l">90 minutes each, over 5 weeks</div></div><div class="fact"><div class="v">Up to 8</div><div class="l">children in each group</div></div><div class="fact"><div class="v">2 ways</div><div class="l">face to face or online</div></div><div class="fact"><div class="v">All included</div><div class="l">workbook, kit, journal, certificate</div></div></section>

<section class="sec"><div class="shead"><span class="eyebrow">How children learn</span><h2>Four habits of a young mathematician</h2><p class="muted">Every lesson follows the same four steps, so children learn how to think, not just what to write.</p></div><div class="rules4">
<div class="rule"><b>1</b><h3>Notice the pattern</h3><p class="muted small">Look closely before rushing to an answer.</p></div>
<div class="rule"><b>2</b><h3>Test it with objects</h3><p class="muted small">Counters, coins and strips to check an idea.</p></div>
<div class="rule"><b>3</b><h3>Check your answer</h3><p class="muted small">Does it make sense? Try another way.</p></div>
<div class="rule"><b>4</b><h3>Explain why</h3><p class="muted small">Say or draw why it works. This is where learning sticks.</p></div></div></section>

<section class="sec"><div class="shead"><span class="eyebrow">The 10 lessons</span><h2>What we cover</h2></div><div class="lessons" id="lessons"></div></section>

<section class="two"><div class="tile yel"><span class="tag">Your child takes home</span><ul style="padding-left:18px;display:grid;gap:6px"><li>A 46-page Math Inquirers workbook</li><li>The Inquirer Kit: coins, ten-frames, counters, number strips</li><li>An Inquiry Journal, stamped after every lesson</li><li>A certificate on Challenge Day</li></ul></div>
<div class="tile mint"><span class="tag">You get</span><ul style="padding-left:18px;display:grid;gap:6px"><li>A short note each week: what we did and one thing to try at home</li><li>Notes on where your child is ready to be stretched further</li><li>Free weekly puzzles by email</li></ul><p class="small muted">Nothing to buy. Online families print the kit pages at home.</p></div></section>

<section class="sec" id="tryit"><div class="shead"><span class="eyebrow">Try one now</span><h2>A taste of Lesson 1</h2></div><div class="pzcard"><div class="pzl"><span class="tag">Primary 1 · Frog hops</span><div class="big">3, 6, 9, ?</div><p style="font-size:18px">A frog starts at 0 and hops 3 steps each time: 3, 6, 9 … Where does it land on its 7th hop?</p><div class="row"><input id="pzA" placeholder="Your answer" inputmode="numeric" style="max-width:170px"><button class="btn yel" id="pzCheck" type="button">Check</button></div><div id="pzMsg"></div></div><div class="pzr"><h3>In class, the answer is only half the job</h3><p class="muted">Children then explain how they know: counting on a number line, adding 3 seven times, or spotting that every landing spot is in the 3 times table. Hearing three different ways is how thinking grows.</p><a class="btn sm alt" href="#register" style="justify-self:start">Register for the program</a></div></div></section>

<section class="sec" id="classes"><div class="shead"><span class="eyebrow">Class times</span><h2>Choose a group</h2><p class="muted">Each group meets twice a week for 5 weeks. Times are to confirm.</p></div><div class="sessions" id="sess"></div></section>

<section class="sec" id="price"><div class="shead"><span class="eyebrow">Price</span><h2>One price, everything included</h2></div><div class="pricebox"><div class="pcard hot"><span class="tag" style="justify-self:start;font:800 12px var(--body);text-transform:uppercase;letter-spacing:.08em;border:2px solid var(--ink);border-radius:999px;padding:3px 10px;background:var(--card)">Program fee</span><div class="amt" id="pR"></div><p>10 lessons of 90 minutes: S$50 a lesson, workbook included.</p></div><div class="pcard"><span class="tag" style="justify-self:start;font:800 12px var(--body);text-transform:uppercase;letter-spacing:.08em;border:2px solid var(--ink);border-radius:999px;padding:3px 10px">Current students</span><div class="amt" id="pE"></div><p id="pEnote"></p></div></div><p class="small muted">For 15 hours of teaching, the printed workbook, cut-out kit, Inquiry Journal and certificate. No payment now: we confirm your place first and then send payment details.</p></section>

<section class="band yel" id="register"><div class="sec"><span class="eyebrow">Register</span><h2>Hold a seat</h2><p class="muted">Fill this in and send it to us on WhatsApp. We reply within 2 working days to confirm the group and send payment details. Groups are small, so seats go in order of registration.</p><p class="small">WhatsApp: <b id="waShow"></b><br>Email: <b id="emShow"></b></p></div>
<form class="card" id="reg"><div class="grid2"><div class="field"><label for="r1">Parent's name</label><input id="r1" autocomplete="name"></div><div class="field"><label for="r2">Mobile</label><input id="r2" type="tel" autocomplete="tel"></div></div>
<div class="grid2"><div class="field"><label for="r3">Child's name</label><input id="r3"></div><div class="field"><label for="r4">Level in 2026</label><select id="r4"><option>Primary 1</option><option>K2 (starting P1 in 2027, free readiness check)</option><option>Primary 2</option></select></div></div>
<div class="field"><label for="r5">Group</label><select id="r5"></select></div>
<div class="field"><label for="r6">Anything we should know? <span class="muted" style="font-weight:600">(optional)</span></label><textarea id="r6" style="min-height:70px"></textarea></div>
<label class="check" for="r8"><input type="checkbox" id="r8"><span>My child is a current Math Inquirers student (S$450)</span></label>
<label class="check" for="r7"><input type="checkbox" id="r7"><span>I agree to Math Inquirers (Preciouslyours Pte Ltd) using these details to arrange the class and contact me about it.</span></label>
<div id="regMsg"></div><button class="btn" type="submit">Send on WhatsApp</button></form></section>

<section class="sec faq" id="faq"><div class="shead"><span class="eyebrow">Questions</span><h2>Parents often ask</h2></div>
<details><summary>Who is it for?</summary><p>Children in Primary 1 this year who enjoy puzzles or finish school work easily. K2 children starting Primary 1 in 2027 are welcome after a free 15-minute readiness check, which we arrange after you register. Puzzles come in three levels, so every child is stretched.</p></details>
<details><summary>Is it linked to MOE or the GEP?</summary><p>No. Math Inquirers is an independent enrichment program. It builds the thinking habits used in school maths but it is not a GEP preparation course.</p></details>
<details><summary>Who teaches?</summary><p>Lessons are planned and led by an experienced Singapore primary school maths teacher, using the Math Inquirers lesson plans, slides and workbook.</p></details>
<details><summary>What if my child misses a lesson?</summary><p>We send that lesson's workbook pages and a short catch-up guide, so your child can do it at home.</p></details>
<details><summary>How does online work?</summary><p>Live video lessons with the same group of up to 8. Print the kit pages before the first lesson.</p></details>
<details><summary>How do I pay?</summary><p>There is nothing to pay when you register. We confirm the group first, then send payment details. The current-student price is for children already in a Math Inquirers class or a past program.</p></details></section>
</main>
<footer><div><b>Math Inquirers</b><p style="margin-top:6px">A Primary 1 holiday program by Preciouslyours Pte Ltd, Singapore. Not affiliated with MOE or the Gifted Education Programme.</p></div><div><b>Contact</b><p style="margin-top:6px">WhatsApp: <span id="waFoot"></span><br>Email: <span id="emFoot"></span></p></div><div><b>Your details</b><p style="margin-top:6px">We use your details only to arrange the class and reply to you, in line with the PDPA.</p></div></footer>
</div>
<script>
(function(){
"use strict";
/* ---- settings to confirm ---- */
var CONFIG={
  whatsapp:"6590000000",           /* to confirm: number with 65, no spaces */
  whatsappShow:"+65 9000 0000 (to confirm)",
  email:"hello@mathinquirers.example (to confirm)",
  price:500, current:450,
  classes:[
    {id:"A",name:"Group A",mode:"Face to face",days:"Mon & Thu",time:"9:30–11:00am",start:"Mon 23 Nov",venue:"Venue to confirm"},
    {id:"B",name:"Group B",mode:"Face to face",days:"Tue & Fri",time:"2:30–4:00pm",start:"Tue 24 Nov",venue:"Venue to confirm"},
    {id:"C",name:"Group C",mode:"Online",days:"Wed & Sat",time:"10:00–11:30am",start:"Wed 25 Nov",venue:"Live video class"}]
};
var LESSONS=[["Count with the Frog","Number patterns and skip counting"],["Number Bond Inquiry","Parts and wholes to 20"],["Let's Plan the Fruit Party","Picture graphs and tallies"],["Pattern Inquiry","Shape and number patterns"],["Mystery Number","Working backwards"],["Coin Combos","Money and finding every way"],["Shape Safari","2D shapes, sides and corners"],["Logic Lab","Clues, sorting and Venn diagrams"],["Measure It!","Length with non-standard units"],["Challenge Day","Mixed puzzles and the certificate"]];
function $(id){return document.getElementById(id)}
function esc(s){return String(s).replace(/[&<>"']/g,function(c){return{"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]})}
'''+hero+'''
$("art").outerHTML=heroArt();
$("ebPrice").textContent="S$"+CONFIG.price;
$("ebLeft").textContent="workbook included · S$"+CONFIG.current+" for current students";
$("pE").textContent="S$"+CONFIG.current;$("pR").textContent="S$"+CONFIG.price;
$("pEnote").textContent="For children already in a Math Inquirers class or a past program. Save S$"+(CONFIG.price-CONFIG.current)+".";
$("lessons").innerHTML=LESSONS.map(function(l,i){return '<div class="lesson"><div class="n">'+(i+1)+'</div><div class="t">'+l[0]+'</div><div class="s">'+l[1]+'</div></div>'}).join("");
$("sess").innerHTML=CONFIG.classes.map(function(c){return '<div class="session"><div class="row" style="justify-content:space-between"><span class="pill '+(c.mode==="Online"?"p-ok":"p-wait")+'">'+esc(c.mode)+'</span><span class="small muted">Up to 8 children</span></div><h3>'+esc(c.name)+'</h3><p><b>'+esc(c.days)+'</b>, '+esc(c.time)+'<br><span class="muted small">Starts '+esc(c.start)+' · '+esc(c.venue)+'</span></p><a class="btn sm" href="#register" data-pick="'+c.id+'" style="justify-self:start">Choose '+esc(c.name)+'</a></div>'}).join("");
$("r5").innerHTML=CONFIG.classes.map(function(c){return '<option value="'+c.id+'">'+esc(c.name+" · "+c.mode+" · "+c.days+", "+c.time+" · from "+c.start)+'</option>'}).join("")+'<option value="any">Any group is fine</option>';
["waShow","waFoot"].forEach(function(i){$(i).textContent=CONFIG.whatsappShow});["emShow","emFoot"].forEach(function(i){$(i).textContent=CONFIG.email});
document.addEventListener("click",function(e){var p=e.target.closest("[data-pick]");if(p)$("r5").value=p.dataset.pick});
$("pzCheck").addEventListener("click",function(){var v=($("pzA").value||"").replace(/\\D/g,"");$("pzMsg").innerHTML=v==="21"?'<div class="msg ok">Correct! Now ask: how do you know? 7 hops of 3 is 21.</div>':'<div class="msg no">Not yet. Try counting along a number line in 3s.</div>'});
$("reg").addEventListener("submit",function(e){
  e.preventDefault();
  var f={p:$("r1").value.trim(),m:$("r2").value.trim(),c:$("r3").value.trim(),l:$("r4").value,g:$("r5").options[$("r5").selectedIndex].text,n:$("r6").value.trim()};
  if(!f.p||!f.m||!f.c){$("regMsg").innerHTML='<div class="msg no">Fill in your name, mobile and your child\\'s name.</div>';return}
  if(!$("r7").checked){$("regMsg").innerHTML='<div class="msg no">Tick the consent box so we can contact you.</div>';return}
  var price=$("r8").checked?"current-student S$"+CONFIG.current:"S$"+CONFIG.price;
  var msg="Hi! I'd like to register for the Math Inquirers December Holiday Program.\\n\\nParent: "+f.p+"\\nMobile: "+f.m+"\\nChild: "+f.c+" ("+f.l+")\\nGroup: "+f.g+"\\nPrice: "+price+(f.n?"\\nNote: "+f.n:"");
  var url="https://wa.me/"+CONFIG.whatsapp+"?text="+encodeURIComponent(msg);
  $("regMsg").innerHTML='<div class="waout"><div class="msg ok">Almost done. Tap the button to send this on WhatsApp.</div><pre>'+esc(msg)+'</pre><div class="row"><a class="btn teal" href="'+url+'" target="_blank" rel="noopener">Open WhatsApp</a><button class="btn alt sm" type="button" id="cp">Copy message</button></div><p class="small muted">If WhatsApp does not open, copy the message and send it to '+esc(CONFIG.whatsappShow)+' or '+esc(CONFIG.email)+'.</p></div>';
  $("cp").addEventListener("click",function(){var b=this;if(navigator.clipboard&&navigator.clipboard.writeText)navigator.clipboard.writeText(msg).then(function(){b.textContent="Copied"},function(){b.textContent="Select the text above to copy"});else b.textContent="Select the text above to copy"});
});
})();
</script>'''
open('mi_signup.html','w').write(html)
print(len(html))
