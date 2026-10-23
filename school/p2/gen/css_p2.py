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
"""
