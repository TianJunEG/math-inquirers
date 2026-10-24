const {load}=require('./vm_load.js');
const R=require('path').join(__dirname,'..')+'/';
const sleep=ms=>new Promise(r=>setTimeout(r,ms));
async function run(file,trigger,answers=[]){
  const {vm,said}=await load(R+file);
  const rt=vm.runtime; let qs=[]; const ans=[...answers];
  rt.on('QUESTION',q=>{ if(q!==null){qs.push(q); setTimeout(()=>rt.emit('ANSWER',String(ans.shift())),20);} });
  vm.start();
  if(trigger==='flag') vm.greenFlag(); else vm.postIOData('keyboard',{key:trigger,isDown:true});
  await sleep(300);
  const t0=Date.now();
  while(rt.threads.length && Date.now()-t0<60000) await sleep(100);
  vm.postIOData('keyboard',{key:trigger,isDown:false});
  vm.stopAll();
  const sp=rt.targets.find(t=>!t.isStage);
  return {said,qs,x:sp.x,y:sp.y,dir:sp.direction,vars:Object.fromEntries(Object.values(rt.getTargetForStage().variables).map(v=>[v.name,v.value]))};
}
let fails=0;
function chk(name,cond,info){ if(!cond){fails++;console.log('FAIL',name,JSON.stringify(info));}else console.log('ok  ',name); }
const last=r=>r.said[r.said.length-1];
(async()=>{
 const T=[
 ['starters/L1_Sequence_Tester.sb3','flag',[],r=>last(r)==='5'],
 ['answers/L1_Sequence_Tester_ANSWER.sb3','flag',[],r=>last(r)==='302'],
 ['answers/L1_Sequence_Tester_ANSWER.sb3','e',[],r=>last(r)==='term 333 is 1001'],
 ['starters/L2_Prime_Checker.sb3','flag',[],r=>last(r)==='0'],
 ['answers/L2_Prime_Checker_ANSWER.sb3','flag',[],r=>last(r)==='15 is not prime'&&r.vars.count==4],
 ['answers/L3_Below_Zero_ANSWER.sb3',' ',[],r=>last(r)==='-150'],
 ['starters/L3_Below_Zero.sb3',' ',[],r=>last(r)==='0'],
 ['answers/L3_Below_Zero_ANSWER.sb3','flag',[],r=>r.said.join(',')==='2,-1,-4,-7,-10,-13'],
 ['starters/L4_Function_Machine.sb3','flag',[7],r=>last(r)==='7'],
 ['answers/L4_Function_Machine_ANSWER.sb3','flag',[7],r=>last(r)==='23'],
 ['answers/L4_Function_Machine_ANSWER.sb3','s',[],r=>last(r)==='12'],
 ['answers/L4_Function_Machine_ANSWER.sb3','n',[],r=>last(r)==='9'],
 ['starters/L5_Every_Order.sb3','flag',[],r=>r.said.join()==='1,2,3'],
 ['answers/L5_Every_Order_ANSWER.sb3','flag',[],r=>r.said.join()==='11,12,21,22,31,32'],
 ['starters/L6_Chance_Lab.sb3','flag',[],r=>+last(r)>400&&+last(r)<600],
 ['starters/L6_Chance_Lab.sb3','d',[],r=>+last(r)>=2&&+last(r)<=12],
 ['answers/L6_Chance_Lab_ANSWER.sb3','p',[],r=>+last(r)>100&&+last(r)<240],
 ['answers/L7_Turtle_Start_ANSWER.sb3','flag',[],r=>Math.abs(r.x+50)<1e-6&&Math.abs(r.y-100)<1e-6&&r.dir===90],
 ['answers/L7_Turtle_Start_ANSWER.sb3','t',[],r=>Math.abs(r.x+50)<1e-6&&Math.abs(r.y-100)<1e-6],
 ['answers/L7_Turtle_Start_ANSWER.sb3','h',[],r=>Math.abs(r.x+50)<1e-6&&Math.abs(r.y-100)<1e-6],
 ['answers/L7_Turtle_Start_ANSWER.sb3','s',[],r=>Math.abs(r.x+50)<1e-6&&Math.abs(r.y-100)<1e-6],
 ['starters/L7_Turtle_Start.sb3','flag',[],r=>r.x===-50&&r.y===100],
 ['answers/L8_Code_Machine_ANSWER.sb3','flag',['MATH IS FUN'],r=>last(r)==='PDWK LV IXQ'],
 ['answers/L8_Code_Machine_ANSWER.sb3','flag',['XYZ'],r=>last(r)==='ABC'],
 ['starters/L8_Code_Machine.sb3','flag',['A B'],r=>last(r)===' '],
 ['answers/L8_Code_Machine_ANSWER.sb3','k',['PDWK LV IXQ'],r=>r.said.includes('shift 3: MATH IS FUN')&&r.said.filter(x=>x.startsWith('shift')).length===25],
 ['starters/L9_Mean_Machine.sb3','flag',[],r=>r.said.length===1],
 ['answers/L9_Mean_Machine_ANSWER.sb3','flag',[],r=>last(r)==='8'],
 ['answers/L9_Mean_Machine_ANSWER.sb3','m',[],r=>last(r)==='12'],
 ['starters/L10A_Mystery_Machine.sb3','flag',[0],r=>{const n=r.vars.n;return r.said[0]==='OUT is '+(3*n+4)&&last(r).startsWith('No, n was')}],
 ['answers/L10A_Mystery_Machine_ANSWER.sb3','flag',[0],r=>{const n=r.vars.n;return r.said[0]==='OUT is '+(4*n-1)&&n>=1&&n<=50}],
 ['starters/L10B_Prime_or_Not.sb3','flag',[91],r=>last(r)==='91 is not prime'],
 ['starters/L10B_Prime_or_Not.sb3','flag',[97],r=>last(r)==='97 is prime'],
 ['answers/L10B_Prime_or_Not_ANSWER.sb3','flag',[],r=>last(r)==='Primes up to 30: 10'],
 ['starters/L10C_Lucky_Seven.sb3','flag',[],r=>+last(r)>100&&+last(r)<240],
 ['answers/L10C_Lucky_Seven_ANSWER.sb3','flag',[],r=>+last(r)>80&&+last(r)<200],
 ['starters/L10D_Clock_Jumper.sb3','flag',[9,5],r=>last(r)==='The clock shows 2'],
 ['starters/L10D_Clock_Jumper.sb3','flag',[7,5],r=>last(r)==='The clock shows 12'],
 ['answers/L10D_Clock_Jumper_ANSWER.sb3','flag',[4,45],r=>last(r)==='That day is Sunday'],
 ];
 await Promise.all(T.map(async ([f,t,a,fn])=>{ try{const r=await run(f,t,a); chk(f.split('/').pop()+' ['+t+']',fn(r),{said:r.said.slice(-4),vars:r.vars,x:r.x,y:r.y})}catch(e){fails++;console.log('ERR',f,t,e.message)}}));
 console.log(fails?fails+' FAILED':'ALL PASSED'); process.exit(fails?1:0);
})();
