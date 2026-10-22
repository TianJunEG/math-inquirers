const fs=require('fs');const VM=require('scratch-vm');let Storage=require('scratch-storage');Storage=Storage.ScratchStorage;
async function load(f){
  const vm=new VM(); const st=new Storage(); vm.attachStorage(st); 
  const said=[]; vm.runtime.on('SAY',(t,type,text)=>said.push(String(text)));
  await vm.loadProject(fs.readFileSync(f));
  return {vm,said};
}
module.exports={load};
if(require.main===module){(async()=>{
 for(const f of process.argv.slice(2)){try{const {vm}=await load(f);console.log('OK',f.split('/').pop(),vm.runtime.targets.length,'targets');}catch(e){console.log('FAIL',f,e.message)}}
 process.exit(0)})()}
