const NAVY='#1B2A49',YEL='#FFC93C',RED='#D64545',BLUE='#3B6FC9',TEAL='#1F7A6F';
const svg=(h,body)=>`<div class="p" style="text-align:center;margin:0"><svg viewBox="0 0 700 ${h}" width="100%" xmlns="http://www.w3.org/2000/svg" font-family="Nunito Sans,Arial,sans-serif">${body}</svg></div>`;
const H=(t,s)=>`<div class="kh"><div class="kt">${t}</div>${s?`<div class="ks">${s}</div>`:''}</div>`;
const lab=(x,y,t)=>`<text x="${x}" y="${y}" font-size="17" font-weight="800" fill="${NAVY}">${t}</text>`;
const note=(x,y,t)=>`<text x="${x}" y="${y}" font-size="14" fill="#666">${t}</text>`;
function coins(){
  const kinds=[['5¢',28,7,'#E4E4E4'],['10¢',32,7,'#D4D4D4'],['20¢',36,6,'#C2C2C2'],['50¢',40,5,'#AEAEAE']];
  let b='',y=60;
  kinds.forEach(([n,r,c,f])=>{ for(let i=0;i<c;i++){const x=50+i*100;
    b+=`<circle cx="${x}" cy="${y}" r="${r}" fill="${f}" stroke="${NAVY}" stroke-width="2.5" stroke-dasharray="6 4"/><circle cx="${x}" cy="${y}" r="${r-6}" fill="none" stroke="#888" stroke-width="1"/><text x="${x}" y="${y+6}" font-size="${r>34?19:17}" font-weight="800" text-anchor="middle" fill="${NAVY}">${n}</text>`;}
    y+=100;});
  return svg(430,b);
}
function notes(){
  let b='';
  for(let i=0;i<6;i++){const x=55+i*105;
    b+=`<circle cx="${x}" cy="50" r="38" fill="#EBD98A" stroke="${NAVY}" stroke-width="2.5" stroke-dasharray="6 4"/><circle cx="${x}" cy="50" r="30" fill="none" stroke="#888" stroke-width="1"/><text x="${x}" y="57" font-size="20" font-weight="800" text-anchor="middle" fill="${NAVY}">$1</text>`;}
  const rows=[['$2','#D9CCEE',4],['$5','#C8E6C3',4],['$10','#F6C9C9',4],['$50','#C9DBF6',2]];
  let y=115;
  rows.forEach(([n,c,k])=>{for(let i=0;i<k;i++){const x=15+i*172;
    b+=`<rect x="${x}" y="${y}" width="160" height="78" rx="6" fill="${c}" stroke="${NAVY}" stroke-width="2.5" stroke-dasharray="6 4"/><rect x="${x+8}" y="${y+8}" width="144" height="62" rx="4" fill="none" stroke="#888" stroke-width="1"/><text x="${x+80}" y="${y+50}" font-size="30" font-weight="800" text-anchor="middle" fill="${NAVY}">${n}</text><text x="${x+148}" y="${y+66}" font-size="10" font-weight="700" text-anchor="end" fill="#555">PLAY MONEY</text>`;}
    y+=92;});
  return svg(490,b);
}
function cubes(){
  let b=lab(20,22,'Strip A')+lab(20,102,'Strip B');
  [30,110].forEach((y,k)=>{for(let i=0;i<20;i++){const x=20+i*33;
    b+=`<rect x="${x}" y="${y}" width="33" height="33" fill="${i%2?'#E3EEF7':'#FFF1C9'}" stroke="${NAVY}" stroke-width="1.6" stroke-dasharray="${0}"/><text x="${x+16.5}" y="${y+22}" font-size="13" font-weight="800" text-anchor="middle" fill="${NAVY}">${i+1}</text>`;}});
  return svg(160,b);
}
function frames(){
  let b='';const pos=[[40,40,'Ten-frame 1'],[380,40,'Ten-frame 2'],[40,220,'Ten-frame 3'],[380,220,'Ten-frame 4']];
  pos.forEach(([x,y,n])=>{b+=lab(x,y-12,n);
    for(let r=0;r<2;r++)for(let c=0;c<5;c++)b+=`<rect x="${x+c*56}" y="${y+r*56}" width="56" height="56" fill="#fff" stroke="${NAVY}" stroke-width="2.2"/>`;
    b+=`<rect x="${x-6}" y="${y-6}" width="292" height="124" fill="none" stroke="#999" stroke-width="1.2" stroke-dasharray="6 4"/>`;});
  b+=lab(40,400,'Counters: cut out all 20 (10 red, 10 yellow)');
  [[RED,440],[YEL,510]].forEach(([c,y])=>{for(let i=0;i<10;i++){const x=55+i*65;
    b+=`<circle cx="${x}" cy="${y}" r="24" fill="${c}" stroke="${NAVY}" stroke-width="1.5" stroke-dasharray="5 3"/>`;}});
  b+=note(40,570,'Cut along the dashed lines.');
  return svg(590,b);
}
function strips(){
  let b=lab(20,30,'Number strips 0 to 20 (cut out; use as a number line)');
  [50,125,200].forEach(y=>{for(let i=0;i<=20;i++){const x=20+i*32;
    b+=`<rect x="${x}" y="${y}" width="32" height="44" fill="#fff" stroke="${NAVY}" stroke-width="1.6"/><text x="${x+16}" y="${y+28}" font-size="14" font-weight="800" text-anchor="middle" fill="${i==0||i==10||i==20?RED:NAVY}">${i}</text>`;}});
  return svg(270,b);
}
function tiles(){
  let b=lab(20,30,'Shape and sorting tiles (cut out all 24: 4 shapes, 3 colours, 2 sizes)');
  const cols=[[RED,'red'],[YEL,'yellow'],[BLUE,'blue']];
  const shape=(k,x,y,s,c)=>{const big=s==1,a=big?34:20;
    if(k==0)return `<circle cx="${x}" cy="${y}" r="${a}" fill="${c}" stroke="#555" stroke-width="1.2" stroke-dasharray="5 3"/>`;
    if(k==1)return `<rect x="${x-a}" y="${y-a}" width="${2*a}" height="${2*a}" fill="${c}" stroke="#555" stroke-width="1.2" stroke-dasharray="5 3"/>`;
    if(k==2)return `<polygon points="${x},${y-a} ${x+a*1.1},${y+a*0.8} ${x-a*1.1},${y+a*0.8}" fill="${c}" stroke="#555" stroke-width="1.2" stroke-dasharray="5 3"/>`;
    return `<rect x="${x-a*1.25}" y="${y-a*0.7}" width="${a*2.5}" height="${a*1.4}" fill="${c}" stroke="#555" stroke-width="1.2" stroke-dasharray="5 3"/>`;};
  let i=0;
  for(let k=0;k<4;k++)cols.forEach(([c])=>[1,0].forEach(s=>{const col=i%6, row=Math.floor(i/6);
    b+=shape(k,70+col*110,95+row*105,s,c);i++;}));
  b+=note(20,490,'Shapes: circle, square, triangle, rectangle.   Colours: red, yellow, blue.   Sizes: big, small.');
  return svg(510,b);
}
module.exports=()=>[
 H('Cut-outs','For Lesson 6 (Coin Combos) and Lesson 9 (Measure It!). Cut along the dashed lines and keep the pieces in an envelope.'),
 lab2('Play coins (seven 5¢, seven 10¢, six 20¢, five 50¢)'),coins(),
 lab2('Paper cube strips (every square is the same size)'),cubes(),
 '<div class="brk"></div>',H('Play notes and $1 coins','For Lesson 6 (Coin Combos). Six $1 coins, four $2, four $5, four $10 and two $50 notes.'),notes(),
 '<div class="brk"></div>',H('Inquirer Kit','Nothing needs to be bought. Print, cut out and keep everything in one envelope.'),frames(),
 '<div class="brk"></div>',H('Number strips and sorting tiles',''),strips(),tiles()];
function lab2(t){return `<div class="kl">${t}</div>`}
