/* "Request another time" form. Embedded by lp_build.py inside the home page script; expects $, esc, CONFIG and INTEREST ({consent, bands, levels}) in scope.
   Two modes, chosen at load:
   - portal: window.MI_CONFIG (from /portal/config.js, only present in a --with-portal build with real Supabase values) holds a Supabase URL + anon key
     (both public by design). The request goes to the SECURITY DEFINER function submit_interest_request via PostgREST; no key is ever hard-coded here.
   - WhatsApp: otherwise (or if the call fails) the form builds a prefilled WhatsApp message to the business number. */
(function(){
var form=$("itForm");if(!form)return;
var MC=window.MI_CONFIG||{},SB=/^https:\/\/[a-z0-9-]+\.supabase\.co$/.test(MC.SUPABASE_URL||"")&&MC.ANON_KEY&&MC.ANON_KEY!=="ANON_KEY"?{url:MC.SUPABASE_URL,key:MC.ANON_KEY}:null;
var LEVELS=INTEREST.levels,BANDS=INTEREST.bands;
$("itModeNote").textContent=SB?"Your request is stored securely and used only to plan new class times.":"Sending opens WhatsApp with your request written out, so you can check it before you send it to "+CONFIG.whatsappShow+".";
function checked(name){return Array.prototype.slice.call(form.querySelectorAll('input[name="'+name+'"]:checked'))}
function setSlot(id){
  Array.prototype.forEach.call(form.querySelectorAll('input[name="itslot"]'),function(c){if(c.value===id){c.checked=true}});
}
function applyParams(q){
  var lv=parseInt(q.level,10);if(lv>=1&&lv<=6)$("itLevel").value=String(lv);
  if(q.interest)setSlot(q.interest);
}
(function(){try{var p=new URLSearchParams(location.search),o={};p.forEach(function(v,k){o[k]=v});applyParams(o);
  if(o.interest){var s=$("request-time");if(s&&s.scrollIntoView)setTimeout(function(){s.scrollIntoView()},0)}}catch(e){}})();
/* the "I'm interested" buttons on this page preselect the slot without reloading */
document.addEventListener("click",function(e){
  var a=e.target.closest&&e.target.closest("a[data-level][data-interest]");if(!a||e.defaultPrevented||e.metaKey||e.ctrlKey||e.shiftKey)return;
  e.preventDefault();
  Array.prototype.forEach.call(form.querySelectorAll('input[name="itslot"]'),function(c){c.checked=false});
  applyParams({level:a.dataset.level,interest:a.dataset.interest});
  var s=$("request-time");if(s&&s.scrollIntoView)s.scrollIntoView({behavior:"smooth"});
  try{history.replaceState(null,"","?level="+a.dataset.level+(a.dataset.interest?"&interest="+encodeURIComponent(a.dataset.interest):"")+"#request-time")}catch(x){}
});
function fieldErr(id,text){var el=$(id);el.setAttribute("aria-invalid","true");var p=el.parentNode,m=p.querySelector(".err");if(!m){m=document.createElement("span");m.className="err";m.setAttribute("role","alert");p.appendChild(m)}m.textContent=text}
function clearErrs(){Array.prototype.forEach.call(form.querySelectorAll(".err"),function(n){n.parentNode.removeChild(n)});Array.prototype.forEach.call(form.querySelectorAll("[aria-invalid]"),function(n){n.removeAttribute("aria-invalid")})}
function digits(s){return String(s).replace(/\D/g,"")}
function normWa(s){var d=digits(s);if(d.length===10&&d.slice(0,2)==="65")d=d.slice(2);return d}
function valid(){
  clearErrs();var bad=[];
  var v={level:parseInt($("itLevel").value,10),age:$("itAge").value,name:$("itName").value.trim().replace(/\s+/g," "),other:$("itOther").value.trim(),note:$("itNote").value.trim(),
    wa:$("itWa").value.trim(),email:$("itEmail").value.trim(),slots:checked("itslot"),wins:checked("itwin")};
  if(!v.age)bad.push(["itAge","Choose your child's age range."]);
  if(!v.slots.length&&!v.wins.length&&!v.other)bad.push(["itOther","Tick at least one time, or write another day or time."]);
  if(!v.name)bad.push(["itName","Please add your first name."]);
  var wd=normWa(v.wa);
  if(v.wa&&!/^\d{8,15}$/.test(wd))bad.push(["itWa","Enter a WhatsApp number with 8 or more digits."]);
  if(v.email&&!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(v.email))bad.push(["itEmail","That email does not look right."]);
  if(!v.wa&&!v.email)bad.push(["itWa","Give a WhatsApp number or an email."]);
  if(!$("itConsent").checked)bad.push(["itConsent","Please tick the box so we may use your details to plan new times."]);
  bad.forEach(function(b){fieldErr(b[0],b[1])});
  if(bad.length){$("itMsg").innerHTML='<div class="msg no">Please fix the '+bad.length+' item'+(bad.length>1?'s':'')+' marked in red.</div>';try{$(bad[0][0]).focus()}catch(x){}return null}
  v.wd=v.wa?wd:"";return v;
}
function message(v){
  var times=v.slots.map(function(c){return c.dataset.label+" ("+c.value+")"}).concat(v.wins.map(function(c){return c.dataset.label}));
  if(v.other)times.push("Other: "+v.other);
  var lv=LEVELS[v.level];
  return "Hi! I'd like to request another class time for Math Inquirers.\n\nLevel: "+lv+"\nChild's age: "+BANDS[v.age]+"\nTimes: "+times.join("; ")+"\nParent: "+v.name+"\nContact: "+[v.wa?"WhatsApp "+v.wa:"",v.email?"email "+v.email:""].filter(Boolean).join(", ")+(v.note?"\nNote: "+v.note:"")+"\nI agree you may use these details only to plan new class times and contact me about them.";
}
function waOut(v,intro){
  var msg=message(v),url="https://wa.me/"+CONFIG.whatsapp+"?text="+encodeURIComponent(msg);
  $("itMsg").innerHTML='<div class="waout"><div class="msg ok">'+esc(intro)+'</div><pre id="itPre">'+esc(msg)+'</pre><div class="row"><a class="btn teal" id="itWaLink" href="'+url+'" target="_blank" rel="noopener">Open WhatsApp</a><button class="btn alt sm" type="button" id="itCopy">Copy message</button></div><p class="small muted">If WhatsApp does not open, copy the message and send it to '+esc(CONFIG.whatsappShow)+(CONFIG.email?' or '+esc(CONFIG.email):'')+'. Nothing is reserved by sending it.</p></div>';
  $("itCopy").addEventListener("click",function(){var b=this;if(navigator.clipboard&&navigator.clipboard.writeText)navigator.clipboard.writeText(msg).then(function(){b.textContent="Copied"},function(){b.textContent="Select the text above to copy"});else b.textContent="Select the text above to copy"});
}
var KEY="mi_interest_last";
function recentlySent(){try{var t=parseInt(localStorage.getItem(KEY),10);return t&&Date.now()-t<60000}catch(e){return false}}
function markSent(){try{localStorage.setItem(KEY,String(Date.now()))}catch(e){}}
function done(status){
  $("itMsg").innerHTML='<div class="msg ok" role="status">'+(status==="already_received"?"Thank you. We already have a request from this contact today, so we have kept that one.":"Thank you. We have your request.")+' This is not a booking: if we open a group at a matching time, we will message you first.</div>';
  form.reset();
}
form.addEventListener("submit",function(e){
  e.preventDefault();
  if($("itHp").value){return}                                  /* honeypot: a person never sees this field */
  var v=valid();if(!v)return;
  if(recentlySent()){$("itMsg").innerHTML='<div class="msg info">You just sent a request. Please wait a minute before sending another.</div>';return}
  if(!SB){markSent();waOut(v,"Almost done. Tap the button to send this request on WhatsApp.");return}
  var btn=$("itSubmit");btn.disabled=true;btn.textContent="Sending…";
  var body={p_level:v.level,p_age_band:v.age,p_slots:v.slots.map(function(c){return c.value}),p_windows:v.wins.map(function(c){return c.value}),p_other_time:v.other||null,
    p_first_name:v.name,p_whatsapp:v.wd||null,p_email:v.email||null,p_note:v.note||null,p_consent:true,p_consent_version:INTEREST.consent,p_hp:$("itHp").value||null};
  fetch(SB.url+"/rest/v1/rpc/submit_interest_request",{method:"POST",headers:{"Content-Type":"application/json",apikey:SB.key,Authorization:"Bearer "+SB.key},body:JSON.stringify(body)})
    .then(function(r){return r.json().catch(function(){return null}).then(function(j){return{ok:r.ok,j:j}})})
    .then(function(x){
      btn.disabled=false;btn.textContent="Send my request";
      if(x.ok&&x.j&&x.j.ok){markSent();done(x.j.status);return}
      var m=x.j&&x.j.message;
      if(m==="invalid_input"||m==="consent_required"){$("itMsg").innerHTML='<div class="msg no">Some details were not accepted. Please check the form and try again.</div>';return}
      waOut(v,"We could not save your request here. You can send it to us on WhatsApp instead.");
    },function(){btn.disabled=false;btn.textContent="Send my request";waOut(v,"We could not reach our server. You can send your request on WhatsApp instead.")});
});
})();
