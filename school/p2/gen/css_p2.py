"""CSS of the Primary 2 pages (added to render.CSS)."""
CSS_P2 = """
/* ---- Primary 2 pages ---- */
.ab.w3{width:23mm}.ab.w4{width:30mm}.ab.w5{width:38mm}
.qg{display:grid;gap:3.5mm 5mm}.qg.c1{grid-template-columns:1fr}.qg.c2{grid-template-columns:repeat(2,minmax(0,1fr))}.qg.c3{grid-template-columns:repeat(3,minmax(0,1fr))}
.qc{border:0.4mm solid #000;border-radius:2mm;padding:2mm 3mm;display:flex;flex-direction:column;gap:1.5mm;justify-content:space-between}
.qc .qh{display:flex;align-items:flex-start;gap:2.5mm}.qc .qt{flex:1;font-size:13.5pt;line-height:1.22}.qc .qt p{margin:0}
.qc .qa{display:flex;align-items:center;justify-content:flex-end;gap:2mm;font-size:14pt}
.qc svg{max-width:none;display:block}
.ctc .codetable{display:grid;gap:1.6mm 2mm}.ctc .ct{min-width:0;padding:0.6mm 1mm;font-size:13pt;gap:1.5mm;justify-content:center}.ctc .ct b{font-size:16pt;padding-left:1.6mm;min-width:5mm;text-align:center}
.qc.inl{flex-direction:row;align-items:center;justify-content:space-between;gap:3mm}.qc.inl .qh{flex:1}.qc.inl .qa{flex:none}
.vsum{display:grid;grid-template-columns:7mm repeat(3,9mm);gap:0;align-items:center;font-family:'Fredoka';font-weight:600;font-size:25pt;line-height:1.05}
.vsum .vr{grid-column:1 / 5;display:grid;grid-template-columns:7mm repeat(3,9mm);align-items:center;justify-items:center;height:12.5mm}
.vsum .vr em{font-style:normal;font-size:22pt}.vsum .vr i{font-style:normal}
.vsum .vr i.ab{width:8.5mm;height:12mm;border-width:0.5mm;border-radius:1mm}
.vsum .vrule{grid-column:1 / 5;border-top:0.8mm solid #000;height:0;margin:0.8mm 0}
.vsum .vans{height:14mm;grid-template-columns:7mm 1fr}.vsum .vans .ab{width:27mm;height:13mm;justify-self:start}
.vcards{display:grid;grid-template-columns:repeat(3,1fr);gap:4mm 5mm}
.vcard{border:0.4mm solid #000;border-radius:2mm;padding:2mm 3mm 3mm;display:flex;flex-direction:column;align-items:center;gap:1mm}.vcard .no{align-self:flex-start}
.pvc{display:flex;flex-direction:column;gap:2mm}
.pvt{display:grid;grid-template-columns:repeat(3,1fr);border:0.4mm solid #000;border-radius:1.5mm}
.pvt>div{padding:0.8mm 1.5mm 1mm;border-left:0.3mm solid #000;display:flex;flex-direction:column;align-items:center}.pvt>div:first-child{border-left:none}
.pvt small{font-size:9.5pt;font-weight:800;display:block;border-bottom:0.3mm solid #000;width:100%;text-align:center;margin-bottom:1mm}
.pvt svg{display:block;max-width:none}
.qc .dl{font-family:'Fredoka';font-weight:600;font-size:20pt}
.qg.c1{gap:2.4mm}
.clk{display:flex;justify-content:center}.qg.clocks .qc{align-items:center}.qg.clocks .qa{justify-content:center}
.trows{display:flex;flex-direction:column;gap:3mm}
.trow{display:flex;align-items:center;gap:2.5mm;border-bottom:0.3mm solid #000;padding-bottom:1.5mm}.trow .tl{width:17mm;font-size:12pt;font-weight:700}
.trow .ts{flex:1}.trow .ts svg{max-width:none;display:block}.trow .ta{display:flex;align-items:center;gap:1.5mm;font-size:14pt;font-weight:700;flex:none}
.qc{position:relative}.qc.pos .no{position:absolute;left:2mm;top:2mm}.qc.pos .qh{justify-content:center}
.clk svg{width:47mm;height:47mm}
.qc.inl{padding:1mm 3mm}
/* domino maze (words over numerals) */
.dm{display:flex;flex-direction:column;align-items:center;gap:1.2mm;width:100%}
.dm .dw{font-family:'Nunito Sans';font-weight:800;font-size:11pt;line-height:1.1;text-align:center;padding:0 1mm}
.dm .dl{width:80%;border-top:0.4mm solid #000;height:0}
.dm .dn{font-family:'Fredoka';font-weight:600;font-size:22pt}
/* digit cards */
.dcards{display:flex;gap:2mm;justify-content:center;margin-bottom:1.5mm}
.dcard{width:11.5mm;height:17mm;border:0.6mm solid #000;border-radius:1.5mm;display:flex;align-items:center;justify-content:center;font-family:'Fredoka';font-weight:600;font-size:24pt}
/* number sequences */
.sqrows{display:flex;flex-direction:column;gap:3.2mm}
.sqrows .srow{display:flex;align-items:center;gap:3mm;border-bottom:0.3mm solid #000;padding-bottom:2mm}
.seq{display:flex;gap:2mm;align-items:center}.seq .sq{width:20mm;height:13mm;border:0.5mm solid #000;display:inline-flex;align-items:center;justify-content:center;font-family:'Fredoka';font-weight:600;font-size:18pt}
.seq .ab.w3{width:20mm;height:13mm}
/* fractions */
.fans{display:flex;flex-direction:column;align-items:center;gap:0}.fans .ab.w2{width:15mm;height:12mm}.fans .fline{width:17mm;border-top:0.7mm solid #000;height:0;margin:0.6mm 0}
.ffig{display:flex;justify-content:center;align-items:center;min-height:30mm}.ffig svg{max-width:none}
.ct .fr{font-size:11pt;margin-right:0.5mm}
.qg .span2{grid-column:1 / -1}
/* wave 3 */
.ansgrid2{display:flex;gap:6mm;justify-content:center;margin-top:1mm}
.tfrows{display:flex;flex-direction:column;gap:2mm}
.qrow{display:flex;align-items:center;gap:3mm;font-size:14.5pt;padding:1.5mm 0;border-bottom:0.3mm solid #000;line-height:1.2}.qrow .qt{flex:1}
.tfrow{padding:6.5mm 0}.tfrow .qt{font-size:16pt}
.tfo{display:flex;align-items:center;gap:2mm;font-size:15pt;font-weight:800;margin-left:4mm}
i.cl{font-style:normal;display:inline-flex;align-items:center;justify-content:center;width:8.5mm;height:8.5mm;border:0.5mm solid #000;border-radius:50%;font-size:14pt;font-weight:700;flex:none}
.fcards,.pcards{display:flex;gap:6mm;justify-content:center;padding:1mm 0}
.fcard,.pcard{border:0.5mm solid #000;border-radius:2mm;padding:2.5mm 3mm;display:flex;flex-direction:column;align-items:center;gap:2mm;min-width:34mm;position:relative}
.fcard .fnum .fr{font-size:20pt}.fcard .fnum .fr i{padding:0 2mm}
.pcard{min-width:44mm}.pname{font-size:14pt;font-weight:700}.pprice{font-family:'Fredoka';font-weight:600;font-size:22pt}
.pur{border:0.4mm solid #000;border-radius:2mm;padding:2mm 2.5mm;display:flex;align-items:center;gap:3mm}.pur svg{max-width:none}
.purses2{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:2.5mm 4mm}
.amts{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:2.5mm 4mm}
.amt{display:flex;align-items:center;gap:2.5mm;border:0.4mm solid #000;border-radius:2mm;padding:1.5mm 2.5mm}.amt b{font-family:'Fredoka';font-weight:600;font-size:17pt;flex:1}
.fsum{font-size:15pt;display:flex;align-items:center;gap:2mm;flex-wrap:wrap}.fsum .fr{font-size:16pt}.fsum .fr i{padding:0 1.2mm}.fsum .ptxt{font-size:12.5pt;line-height:1.2;display:block;flex-basis:100%}
.fb{display:inline-block;width:13mm !important;height:12mm !important;vertical-align:middle}
.fr i .ab.w2{width:13mm;height:12mm}
.ab.w2{width:15mm}
.riddles{display:flex;flex-direction:column;gap:1mm}
.howto{margin-bottom:2mm}
/* wave 4 */
.dial svg,.tank svg{width:44mm;height:44mm;display:block}.tank svg{width:30mm;height:44mm}
.dial,.tank{display:flex;justify-content:center}
.qg.dials .qa,.qg.tanks .qa{justify-content:center;font-size:14pt}
.mcards{display:flex;gap:6mm;justify-content:center}.mcard{position:relative;border:0.5mm solid #000;border-radius:2mm;padding:2mm 3mm;display:flex;align-items:center;gap:2mm}
.mcard svg{max-width:none;width:34mm;height:34mm}.mcard i.cl{position:absolute;left:1.5mm;top:1.5mm}
.hrows{display:flex;flex-direction:column;gap:2.5mm}
.hrow{display:flex;align-items:center;gap:3mm;border-bottom:0.3mm solid #000;padding-bottom:2mm}
.ckp{display:flex;align-items:center;gap:3mm;flex:1}.clk30 svg{width:30mm;height:30mm;max-width:none}.arr{font-size:20pt;font-weight:800}
.dgt{flex:1;font-size:15pt;font-weight:700;line-height:1.3}
.hans{display:flex;align-items:center;gap:1.5mm;font-size:13pt;font-weight:700;flex:none}
table.tt{border-collapse:collapse;margin:0 auto}.tt th,.tt td{border:0.5mm solid #000;height:9mm;font-size:13pt;text-align:center;padding:0 5mm}.tt th{font-weight:800;font-size:11pt}.tt td:first-child{text-align:left;font-weight:700}
.prows{display:flex;flex-direction:column;gap:3.5mm}
.prow{display:flex;align-items:center;gap:2.5mm;border-bottom:0.3mm solid #000;padding-bottom:2.5mm}
.pcells{display:flex;gap:0.5mm;align-items:center}.pcell{width:13mm;height:13mm;display:flex;align-items:center;justify-content:center}.pcell svg{width:13mm;height:13mm;max-width:none}
.pcell.q{border:0.5mm dashed #000;border-radius:1.5mm;font-family:'Fredoka';font-weight:700;font-size:16pt}
.popts{display:flex;gap:3mm;margin-left:auto}.popt{display:flex;flex-direction:column;align-items:center;gap:0.5mm}.popt svg{width:13mm;height:13mm;max-width:none}
.mcard{padding:2mm 3mm 2mm 11mm}.clk30 svg{width:26mm;height:26mm}
.tt th,.tt td{height:7.4mm;font-size:12pt}.qc.tq .qt{font-size:12pt}.qc.tq{padding:1.2mm 2.5mm}.qc.tq .ab{height:12.5mm;width:20mm}
/* wave 5 */
.srows3{display:flex;flex-direction:column;gap:2.5mm}
.srow3{display:flex;align-items:center;gap:3mm;border-bottom:0.3mm solid #000;padding-bottom:2mm}
.sol{width:34mm;display:flex;justify-content:center}.sol svg{max-width:none;height:24mm;width:auto}
.sopts{display:flex;gap:2mm;margin-left:auto}
.sgrid{display:grid;grid-template-columns:repeat(5,1fr);gap:1.5mm;border:0.4mm solid #000;border-radius:2mm;padding:2mm}
.sc{display:flex;align-items:center;justify-content:center;height:20mm}.sc svg{max-width:none;height:17mm;width:auto}
.trows2{display:grid;grid-template-columns:repeat(5,1fr);gap:2mm}
.trow2{display:flex;flex-direction:column;align-items:center;gap:1mm;border:0.4mm solid #000;border-radius:2mm;padding:1.5mm}.trow2 b{font-size:12pt}.ticon svg{max-width:none;height:13mm;width:auto}
.pgraph3{display:flex;flex-direction:column;gap:1.2mm;border:0.4mm solid #000;border-radius:2mm;padding:2mm 3mm}
.grow3{display:flex;align-items:center;gap:3mm;height:11.5mm;border-bottom:0.25mm solid #000}.gname{width:26mm;font-size:13pt;font-weight:700}
.gcells{display:flex;gap:0.8mm}.gcell svg{display:block;max-width:none;width:10.5mm;height:10.5mm}.hid{font-size:11pt;font-weight:700;border:0.4mm dashed #000;padding:1mm 6mm;border-radius:1mm}
.gkey{font-size:13pt;font-weight:800;display:flex;align-items:center;gap:2mm;padding-top:1mm}.gkey svg{max-width:none;width:10.5mm;height:10.5mm}
ul.clues{font-size:13.5pt;margin:1mm 0;padding-left:6mm}
.grow3{height:10.2mm}
ul.clues{margin:0.5mm 0;font-size:12.5pt}.grow3{height:9.6mm}.gkey{font-size:12pt}.qc.tq{padding:1mm 2.5mm}
.qg.c1{gap:1.3mm}.qc.inl{padding:0.6mm 3mm}
"""
