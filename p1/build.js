const fs=require('fs');
const {Document,Packer,Paragraph,TextRun,Table,TableRow,TableCell,WidthType,AlignmentType,BorderStyle,ShadingType,ImageRun,Footer,PageNumber,VerticalAlign,Tab,TabStopType}=require('docx');
const FONT='Arial', CW=9900;
const t=(s,o={})=>new TextRun({text:s,font:FONT,size:o.size||26,bold:o.bold,italics:o.italics,color:o.color});
const p=(c,o={})=>new Paragraph({children:Array.isArray(c)?c:(c instanceof TextRun?[c]:[t(c,o)]),spacing:{before:o.before||0,after:o.after===undefined?140:o.after,line:o.line||320,lineRule:'auto'},alignment:o.align,indent:o.indent,keepNext:o.keepNext,keepLines:true,pageBreakBefore:o.pb});
const B1={style:BorderStyle.SINGLE,size:8,color:'000000'};
const borders={top:B1,bottom:B1,left:B1,right:B1};
const cell=(c,w,o={})=>new TableCell({width:{size:w,type:WidthType.DXA},borders,verticalAlign:VerticalAlign.CENTER,margins:{top:o.h||100,bottom:o.h||100,left:100,right:100},shading:o.fill?{type:ShadingType.CLEAR,fill:o.fill,color:'auto'}:undefined,columnSpan:o.span,
  children:(Array.isArray(c)?c:[c]).map(x=>typeof x==='string'?p(x,{align:o.align||AlignmentType.CENTER,after:0,size:o.size||24,bold:o.bold,color:o.color}):(x instanceof TextRun?p([x],{align:o.align||AlignmentType.CENTER,after:0}):x))});
const tbl=(widths,rows)=>new Table({width:{size:widths.reduce((a,b)=>a+b,0),type:WidthType.DXA},columnWidths:widths,rows});
const row=(cells,o={})=>new TableRow({children:cells,cantSplit:true,height:o.h?{value:o.h,rule:'atLeast'}:undefined});
const q=(n,text,o={})=>p([t(n+'.',{bold:true}),new TextRun({children:[new Tab()],font:FONT,size:26}),...(Array.isArray(text)?text:[t(text)])],{indent:{left:560,hanging:560},tabStops:[{type:TabStopType.LEFT,position:560}],before:o.before===undefined?160:o.before,after:o.after===undefined?120:o.after,keepNext:o.keepNext,pb:o.pb});
const sub=(l,text,o={})=>p([t('('+l+')  ',{bold:true}),...(Array.isArray(text)?text:[t(text)])],{indent:{left:1000,hanging:440},after:o.after===undefined?120:o.after});
const ans=(label='Answer:',ind=1000)=>p([t(label+' ',{bold:true}),t('______________________________')],{indent:{left:ind},after:140});
const lines=(n)=>Array.from({length:n},()=>new Paragraph({children:[],spacing:{before:280,after:80},border:{bottom:{style:BorderStyle.SINGLE,size:6,color:'777777',space:1}},indent:{left:560}}));
const img=(file,w,h)=>p([new ImageRun({type:'png',data:fs.readFileSync(file),transformation:{width:w,height:h},altText:{title:file,description:file,name:file}})],{align:AlignmentType.CENTER,after:120});
function header(code,topic,title,first){
  return [
    p([t('WS  ',{bold:true,size:24}),t(code,{bold:true,size:24})],{align:AlignmentType.RIGHT,after:60,pb:!first}),
    tbl([CW],[row([cell(t('PRIMARY 1 MATHEMATICS  •  ENRICHMENT',{bold:true,size:26}),CW,{fill:'D9D9D9',h:110})]),row([cell(t(topic.toUpperCase(),{bold:true,size:26}),CW,{h:110})])]),
    p([t('Name: ',{bold:true,size:24}),t('______________________   ',{size:24}),t('Class: P1-',{bold:true,size:24}),t('_______   ',{size:24}),t('Date: ',{bold:true,size:24}),t('____________',{size:24})],{before:160,after:120}),
    p(t(title,{bold:true,size:44}),{align:AlignmentType.CENTER,after:120,before:20}),
  ];
}
const banner=(s)=>tbl([CW],[row([cell(t(s,{bold:true,size:26}),CW,{fill:'EDEDED',align:AlignmentType.LEFT,h:70})])]);
const gap=(n=120)=>p('',{after:n});

/* ============ WORKSHEETS ============ */
const W=[];
// ---- WS1 ----
W.push(...header('P1-1','Whole Numbers: Number Patterns','COUNT WITH THE FROG!',true));
W.push(p('Look for the pattern. Fill in the missing numbers.',{italics:true,after:80}));
W.push(q(1,'Skip counting. Fill in the blanks.'));
W.push(sub('a','Counting in 2s:   2,  4,  6,  ____,  ____,  12,  ____,  16'));
W.push(sub('b','Counting in 5s:   5,  10,  ____,  20,  ____,  30,  ____'));
W.push(sub('c','Counting in 3s:   3,  6,  ____,  12,  ____,  18'));
W.push(q(2,'What is the rule? Fill in the rule and the next two numbers.'));
W.push(sub('a','4,  7,  10,  13,  ____,  ____        Rule: ______________'));
W.push(sub('b','30,  27,  24,  21,  ____,  ____       Rule: ______________'));
W.push(sub('c','2,  6,  10,  14,  ____,  ____        Rule: ______________'));
W.push(q(3,'A frog starts at 0 and hops 4 steps each time. Colour the numbers where the frog lands.',{keepNext:true}));
const strip=(fillFn)=>{const w=Math.floor(CW/21);const ws=Array(21).fill(w);ws[20]=CW-w*20;return tbl(ws,[row(ws.map((x,i)=>cell(String(i),x,{size:20,h:150,fill:fillFn&&fillFn(i)})))]);};
W.push(strip());
W.push(gap(80));
W.push(sub('a','A second frog also starts at 0 but hops 5 steps each time. Mark its landing numbers with a cross (X) above the number line.'));
W.push(sub('b','Besides 0, which number do BOTH frogs land on?'));
W.push(ans());
W.push(q(4,'Ali counts in 2s from 2 up to 50. Mei counts in 5s from 5 up to 50.',{pb:true,before:0}));
W.push(sub('a','Which numbers will BOTH of them say?'));
W.push(ans());
W.push(sub('b','What do you notice about these numbers?'));
W.push(...lines(2));
W.push(q(5,'Mei puts stickers in boxes. Box 1 has 2 stickers. Each box after it has 3 more stickers than the box before.',{keepNext:true}));
{const ws=[1900,...Array(10).fill(800)];ws[0]=CW-8000;
 const vals=['2','5'];
 W.push(tbl(ws,[row([cell('Box',ws[0],{bold:true,fill:'EDEDED'}),...Array.from({length:10},(_,i)=>cell(String(i+1),800,{bold:true,fill:'EDEDED'}))]),
   row([cell('Stickers',ws[0],{bold:true}),...Array.from({length:10},(_,i)=>cell(vals[i]||'',800,{h:160}))])]));}
W.push(gap(100));
W.push(sub('a','Fill in the table. How many stickers are in Box 10?'));
W.push(ans('Answer:',1000));
W.push(sub('b','Look at the numbers of stickers. Are they odd or even? What pattern do you see?'));
W.push(...lines(2));

// ---- WS2 ----
W.push(...header('P1-2','Picture Graphs','LET’S PLAN THE FRUIT PARTY!'));
W.push(p('Our teacher wants to buy fruit for a class party. Every child voted for ONE fruit. The picture graph shows the votes.',{after:120}));
W.push(p([t('Key:  ',{bold:true}),t('●',{color:'333333'}),t(' = 1 child',{})],{after:100}));
{const rows=[['Apple',6,'C0392B'],['Banana',5,'B8860B'],['Orange',8,'E67E22'],['Grape',3,'7D3C98'],['Watermelon',5,'1E8449']];
 const dots=(n,c)=>{let s='';for(let i=0;i<n;i++){s+='● ';if((i+1)%5===0&&i<n-1)s+='  ';}return p(t(s.trim(),{size:40,color:c}),{after:0,align:AlignmentType.LEFT});};
 W.push(tbl([2400,7500],[row([cell('Fruit',2400,{bold:true,fill:'D9D9D9'}),cell('Votes',7500,{bold:true,fill:'D9D9D9'})]),...rows.map(r=>row([cell(r[0],2400,{bold:true,h:40}),cell(dots(r[1],r[2]),7500,{align:AlignmentType.LEFT,h:40})]))]));}
W.push(gap(20));
W.push(banner('Part A: Read the graph'));
W.push(q(1,'Which fruit got the most votes?',{before:140}));W.push(ans());
W.push(q(2,'Which fruit got the fewest votes?'));W.push(ans());
W.push(q(3,'How many more children chose orange than grape?'));W.push(ans());
W.push(q(4,'Two fruits got the same number of votes. Which two fruits are they?'));W.push(ans());
W.push(q(5,'How many children voted altogether? (Hint: each child had only 1 vote.)'));W.push(ans());
W.push(q(6,[t('Mei says, “Orange is the best fruit for the whole school!”')],{pb:true,before:0}));
W.push(sub('a',[t('Is Mei right?    '),t('Yes  /  No',{bold:true})]));
W.push(sub('b','Why do you think so?'));
W.push(...lines(2));
W.push(q(7,'What else should the teacher think about before buying fruit for the party?'));
W.push(...lines(3));
W.push(gap(140));
W.push(banner('Part B: Now it’s your turn!'));
W.push(p('Ask your own class to vote. Each child votes for ONE fruit. Make a tally mark for each vote.',{before:140,after:100}));
W.push(tbl([2400,5700,1800],[row([cell('Fruit',2400,{bold:true,fill:'D9D9D9'}),cell('Tally',5700,{bold:true,fill:'D9D9D9'}),cell('Total',1800,{bold:true,fill:'D9D9D9'})]),...['Apple','Banana','Orange','Grape','Watermelon'].map(f=>row([cell(f,2400,{bold:true}),cell('',5700,{h:90}),cell('',1800,{h:90})]))]));
W.push(q(8,'Which fruit did YOUR class like best?  ____________________    Is it the same as the graph above?  Yes / No',{before:200}));
W.push(q(9,'Why might two classes choose different fruits?'));
W.push(...lines(2));

// ---- WS3 ----
W.push(...header('P1-3','Patterns','PATTERN INQUIRERS'));
W.push(q(1,'Look at the shape pattern. Draw the missing shapes in places 8 and 9.',{before:60}));
W.push(img('shapes.png',640,92));
W.push(q(2,'The pattern keeps going in the same way.'));
W.push(sub('a','What shape will be in place 10?   ____________________'));
W.push(sub('b','What shape will be in place 12?   ____________________'));
W.push(sub('c','Without drawing, what shape will be in place 30?   ____________________'));
W.push(sub('d','How do you know?'));
W.push(...lines(2));
W.push(q(3,'Ben makes a row of triangles with matchsticks.',{keepNext:true,pb:true,before:0}));
W.push(img('sticks.png',620,127));
W.push(sub('a','Count the sticks. Fill in the table. Keep going until you reach 10 triangles.'));
{const ws=[2300,...Array(10).fill(760)];ws[0]=CW-7600;
 const vals={1:'3',2:'5',3:'7'};
 W.push(tbl(ws,[row([cell('Triangles',ws[0],{bold:true,fill:'EDEDED',size:22}),...Array.from({length:10},(_,i)=>cell(String(i+1),760,{bold:true,fill:'EDEDED'}))]),
   row([cell('Sticks',ws[0],{bold:true,size:22}),...Array.from({length:10},(_,i)=>cell(vals[i+1]||'',760,{h:170}))])]));}
W.push(gap(100));
W.push(sub('b','Each time Ben adds 1 more triangle, how many more sticks does he need?'));
W.push(ans());
W.push(sub('c','Why does he need only that many more sticks? (Look at the picture.)'));
W.push(...lines(2));
W.push(sub('d','How many sticks are needed for 10 triangles?'));
W.push(ans());
W.push(q(4,'Challenge! Ben has 15 sticks. How many triangles in a row can he make?'));
W.push(ans('Answer:',560));
W.push(p([t('Show how you worked it out:',{italics:true})],{indent:{left:560}}));
W.push(...lines(2));

// ---- WS4 ----
W.push(...header('P1-4','Money','COIN COMBOS'));
W.push(p('We have 5¢, 10¢, 20¢ and 50¢ coins. You can use the same kind of coin more than once.',{after:100}));
W.push(q(1,'Show different ways to make exactly 20¢ using only 20¢, 10¢ and 5¢ coins. Write how many of each coin in the table.',{before:100,keepNext:true}));
{const ws=[2500,2470,2470,2460];
 W.push(tbl(ws,[row(['Way','Number of 20¢','Number of 10¢','Number of 5¢'].map((s,i)=>cell(s,ws[i],{bold:true,fill:'D9D9D9',size:22}))),...['A','B','C','D','E'].map(l=>row([cell(l,ws[0],{bold:true,h:140}),cell('',ws[1]),cell('',ws[2]),cell('',ws[3])]))]));}
W.push(gap(60));
W.push(sub('a','Which way uses the FEWEST coins?'));W.push(ans());
W.push(sub('b','Which way uses the MOST coins?'));W.push(ans());
W.push(sub('c','How do you know you have found ALL the ways?'));
W.push(...lines(2));
W.push(q(2,'Challenge! Find ALL the ways to make 30¢ using 20¢, 10¢ and 5¢ coins. Write each way like this:  1 × 20¢ + 2 × 5¢',{pb:true,before:0}));
W.push(...lines(6));
W.push(q(3,'Mei wants to pay exactly 45¢. She can use 5¢, 10¢, 20¢ and 50¢ coins. What is the smallest number of coins she can use? Which coins are they?',{before:240}));
W.push(ans());
W.push(q(4,'Ben has 3 coins. They are worth 35¢ altogether. Which coins does he have?'));
W.push(ans());
W.push(q(5,'Can Ben make 35¢ using only 2 coins? Explain your answer.'));
W.push(...lines(2));

/* ============ TEACHER GUIDE ============ */
const G=[];
const h1=(s,pb)=>p(t(s,{bold:true,size:32}),{before:pb?0:300,after:120,pb});
const h2=(s)=>p(t(s,{bold:true,size:26,color:'1F3864'}),{before:200,after:60,keepNext:true});
const bl=(label,text)=>p([t(label+'  ',{bold:true,size:22}),t(text,{size:22})],{after:80,indent:{left:280}});
const tx=(s)=>p(t(s,{size:22}),{after:80});
G.push(p(t('PRIMARY 1 MATHEMATICS ENRICHMENT',{bold:true,size:22,color:'666666'}),{after:40}));
G.push(p(t('Teacher Guide and Answer Key',{bold:true,size:44}),{after:120}));
G.push(tx('Four worksheets for Primary 1 pupils who are ready for more than the standard practice. Each follows the same arc: start concrete, record in a table, spot the pattern, state the rule, apply it (often backwards), then explain or evaluate. Worksheets are original and sized for A4 printing.'));
G.push(h2('How to use the set'));
G.push(bl('Pacing:','One worksheet per 30 to 40 minute session. Do the warm-up first, then let pupils work in pairs on the table sections before writing alone.'));
G.push(bl('Reading support:','Read each question aloud. Let pupils answer orally or with manipulatives where writing is the barrier; the thinking is what is being stretched.'));
G.push(bl('Talk first:','The “How do you know?” and “Why?” questions are the heart of each sheet. Ask pupils to tell a partner before writing.'));

const ws=(code,name,obj,skills,materials,warm,ask,mistakes,ext,key)=>{
  G.push(h1(code+'  '+name,true));
  G.push(bl('Objective:',obj));G.push(bl('Thinking skills:',skills));G.push(bl('Materials:',materials));
  G.push(h2('Warm-up (5 to 10 minutes)'));G.push(tx(warm));
  G.push(h2('Questions to ask'));ask.forEach(a=>G.push(bl('•',a)));
  G.push(h2('Common mistakes'));mistakes.forEach(a=>G.push(bl('•',a)));
  G.push(h2('Extension'));G.push(tx(ext));
  G.push(h2('Answer key'));key.forEach(k=>G.push(p([t(k[0]+'  ',{bold:true,size:22}),t(k[1],{size:22})],{after:70,indent:{left:280}})));
};
ws('WS P1-1','Count with the Frog (Number Patterns)',
 'Skip count in 2s, 3s, 5s; find and state an add or take-away rule; notice common multiples of 2 and 5.',
 'Pattern spotting, rule finding, generalising, spotting odd/even structure.',
 'Number line 0 to 50 (floor or wall), counters, two colours of crayon.',
 'Walk the number line as a class in 2s, then 5s. Pupils stamp on each number. Ask: who stamped on 10? Why did two groups stamp there?',
 ['What is staying the same each time? What is changing?','Frog 1 and frog 2 both landed on 20. Will they land together again? Where?','Why do the box numbers go even, odd, even, odd?'],
 ['Counting the gap squares instead of the jump size (e.g. 4, 7, 10 read as “add 2”).','Q2(b): writing “add 3” instead of “take away 3”.','Q5: restarting at 3 instead of adding 3 to 2 for Box 2.'],
 'Pupils make their own rule (start at 1, add 6) and swap with a partner to find the rule.',
 [['Q1','(a) 8, 10, 14   (b) 15, 25, 35   (c) 9, 15'],['Q2','(a) 16, 19; add 3   (b) 18, 15; take away 3   (c) 18, 22; add 4'],['Q3','Frog 1 lands on 4, 8, 12, 16, 20. Frog 2 lands on 5, 10, 15, 20. Both: 20.'],['Q4','(a) 10, 20, 30, 40, 50   (b) They all end in 0 / they are in the 10 times table.'],['Q5','Stickers: 2, 5, 8, 11, 14, 17, 20, 23, 26, 29. (a) Box 10 has 29.  (b) They go even, odd, even, odd (they alternate).']]);
ws('WS P1-2','Let’s Plan the Fruit Party (Picture Graphs)',
 'Read a picture graph, compare and total data, then judge what a class vote can and cannot tell us.',
 'Data reading, comparing, sampling awareness, considering other factors.',
 'Sticky dots or counters for the live class vote in Part B.',
 'Run a quick class vote on a favourite fruit with sticky dots before pupils see the graph, so Part B feels familiar.',
 ['If every child voted once, how can we find out how many children there are?','Would the Primary 6 pupils choose the same fruit? Why or why not?','What if one child is allergic or the fruit is too expensive?'],
 ['Q3: counting orange as 8 and grape as 3, then writing 8 + 3 instead of finding the difference.','Q4: naming only one of the two tied fruits.','Q6: answering “Yes” because orange won in the class, ignoring that other classes did not vote.'],
 'Pupils draw their own picture graph from the Part B tally using ● for each child.',
 [['Q1','Orange'],['Q2','Grape'],['Q3','5 more (8 − 3)'],['Q4','Banana and watermelon (5 each)'],['Q5','27 children (6 + 5 + 8 + 3 + 5)'],['Q6','(a) No.  (b) Only our class voted. Other classes may like different fruits.'],['Q7','Accept sensible ideas: cost, how many are needed, easy to share, how long it keeps, messy to eat, any child who cannot eat it.'],['Part B','Answers depend on the class vote. Q9: different children like different things; small groups may not match the whole school.']]);
ws('WS P1-3','Pattern Inquirers (Repeating and Growing Patterns)',
 'Extend a repeating pattern and predict far positions using the pattern core; extend a growing matchstick pattern and work backwards from a total.',
 'Core identification, prediction by multiples, building a table, working backwards.',
 'Shape cut-outs, 21 matchsticks or straws per pair.',
 'Pairs build 1, 2, 3 triangles with matchsticks and count the sticks. Ask them to predict 4 before they build it.',
 ['Which shapes repeat? How many shapes are in the repeating part?','Which places are always squares? What do 3, 6, 9, 12 have in common?','When two triangles touch, how many sticks do they share?'],
 ['Saying 3 more sticks each time because one triangle needs 3.','Q2(c): thinking 30 is a circle because 30 starts with 3.','Q4: dividing 15 by 3 to get 5 triangles.'],
 'Change the shape to squares in a row (4, 7, 10, …) and ask for the rule.',
 [['Q1','Place 8: triangle. Place 9: square.'],['Q2','(a) circle  (b) square  (c) square  (d) The pattern repeats every 3 shapes and every 3rd shape is a square. 30 is in the 3 times table.'],['Q3','(a) 3, 5, 7, 9, 11, 13, 15, 17, 19, 21  (b) 2 more sticks  (c) The new triangle shares one side with the triangle before it, so only 2 new sticks are needed.  (d) 21 sticks'],['Q4','7 triangles. 15 − 1 = 14, then 14 ÷ 2 = 7. Or continue the table until 15.']]);
ws('WS P1-4','Coin Combos (Money)',
 'Find all combinations of coins for a total, work systematically, and use reasoning to rule out cases.',
 'Systematic listing, comparing, working backwards, justifying “there are no more”.',
 'Play coins (5¢, 10¢, 20¢, 50¢), about 6 of each per pair.',
 'Give pairs 20¢ in play coins and ask them to make it in as many ways as possible. Record each way on a mini whiteboard.',
 ['Start with the biggest coin. What is left? How can you make that?','How can you be sure you have not missed a way?','Why can’t you make 35¢ with two coins?'],
 ['Listing the same way twice in a different order (10+5+5 and 5+10+5).','Q3: choosing many small coins (e.g. 10+10+10+10+5) instead of looking for the fewest coins.','Q4: forgetting the three coins must be different.'],
 'Use 5¢, 10¢, 20¢, 50¢ to make 50¢ in as many ways as possible. Introduce the idea of a “fewest coins” rule.',
 [['Q1','A: 1 × 20¢.  B: 2 × 10¢.  C: 1 × 10¢ + 2 × 5¢.  D: 4 × 5¢.  Row E is spare (there are only 4 ways).  (a) one 20¢ coin  (b) four 5¢ coins  (c) Start with the biggest coin and work down, checking each case in turn.'],['Q2','6 ways: 20+10;  20+5+5;  10+10+10;  10+10+5+5;  10+5+5+5+5;  5×6.'],['Q3','3 coins: 20¢ + 20¢ + 5¢.'],['Q4','20¢, 10¢ and 5¢.'],['Q5','No. With two coins the possible totals are 10, 15, 20, 25, 30, 40, 55, 60, 70, 100 (using 5, 10, 20, 50); 35 is not one of them.']]);

const common={styles:{default:{document:{run:{font:FONT,size:26}}}},sections:[]};
const footer=(txt)=>new Footer({children:[new Paragraph({alignment:AlignmentType.CENTER,children:[new TextRun({text:txt+'  •  Page ',font:FONT,size:18,color:'777777'}),new TextRun({children:[PageNumber.CURRENT],font:FONT,size:18,color:'777777'})]})]});
const page={size:{width:11906,height:16838},margin:{top:800,right:1003,bottom:800,left:1003}};
const d1=new Document({styles:common.styles,sections:[{properties:{page},footers:{default:footer('P1 Maths Enrichment Worksheets')},children:W}]});
const d2=new Document({styles:common.styles,sections:[{properties:{page},footers:{default:footer('P1 Maths Enrichment: Teacher Guide and Answer Key')},children:G}]});
Promise.all([Packer.toBuffer(d1).then(b=>fs.writeFileSync('P1_Enrichment_Worksheets.docx',b)),Packer.toBuffer(d2).then(b=>fs.writeFileSync('P1_Teacher_Guide_and_Answer_Key.docx',b))]).then(()=>console.log('built'));
