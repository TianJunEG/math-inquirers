"""CSS of the Primary 4 pages (added after css_p4.py)."""
CSS_P4B = """
/* ---- Primary 4 pages ---- */
.g{display:inline;margin-left:0.22em}
.sym{vertical-align:-0.5mm;margin:0 0.2mm}
.an{font-family:'Fredoka';font-weight:600;margin-left:0.3mm}
.mx{display:inline-flex;align-items:center;gap:0.8mm;vertical-align:middle}.mx b{font-family:'Fredoka';font-weight:600;font-size:1.25em}
.qc.span2{grid-column:1 / -1}
.pvt4{border-collapse:collapse;margin:1mm auto 0;width:100%}.pvt4 th{border:0.4mm solid #000;font-size:10pt;font-weight:800;padding:0.6mm 1mm;text-align:center}.pvt4 td{border:0.4mm solid #000;font-family:'Fredoka';font-weight:600;font-size:18pt;text-align:center;height:11mm}
.ncards{display:grid;grid-template-columns:repeat(5,1fr);gap:2.5mm}
.ncard{position:relative;border:0.5mm solid #000;border-radius:2mm;height:16mm;display:flex;align-items:center;justify-content:center;font-family:'Fredoka';font-weight:600;font-size:17pt;padding:2mm 0 0 5.5mm}
.ncard i.cl{position:absolute;left:1.2mm;top:1.2mm;width:6.5mm;height:6.5mm;font-size:11pt}
.wrows{display:flex;flex-direction:column;gap:1.6mm}
.wrow{display:flex;align-items:center;gap:3mm;border-bottom:0.3mm solid #000;padding-bottom:1mm}
.wrow .wtxt{flex:1;font-size:13pt;line-height:1.2}
.seq4{display:flex;gap:1.6mm;align-items:center;flex-wrap:nowrap;padding:1mm 0}
.sq4{flex:1;min-width:0;height:12.5mm;border:0.5mm solid #000;display:inline-flex;align-items:center;justify-content:center;font-family:'Fredoka';font-weight:600;font-size:16pt}
.sq4.bl{border:none}.sq4.bl .ab{width:100%;height:12.5mm}
.qc.sqc .qt p{margin-bottom:1.2mm}
.yq{font-size:15pt;line-height:1.25}
.sq3{flex:1;min-width:0}
.mcell>span{display:flex;flex-direction:column;align-items:center;gap:0.6mm;text-align:center}.mcell small{font-family:'Nunito Sans';font-weight:700;font-size:8.5pt;line-height:1}
.vmul{grid-template-columns:7mm repeat(var(--n),9mm)}.vmul .vr{grid-template-columns:7mm repeat(var(--n),9mm);grid-column:1 / -1}.vmul .vrule{grid-column:1 / -1}
.vmul .vans{grid-template-columns:7mm 1fr}
.vc3{grid-template-columns:repeat(3,minmax(0,1fr));gap:4mm 3mm}
.vcard .vsum{align-self:center}
.mn{font-weight:inherit}
.srow3.tall{min-height:22mm;padding-bottom:3mm}.srows3.tallrows{gap:5mm}
.srow3 .tfo b{font-size:15pt}.srow3 i.cl{width:10mm;height:10mm;font-size:16pt}
.ptxt2{font-size:14pt;line-height:1.3}
.qc.pic .qt svg{margin:1.5mm auto 0}.qc.pic.span2 .qt{display:flex;flex-direction:column;align-items:center}.qc.pic.span2 .qt p{align-self:flex-start}
.qc.prot2{position:relative;padding:1.5mm 2mm;align-items:center}.qc.prot2 .no{position:absolute;left:2mm;top:2mm}.qc.prot2 svg{display:block;margin:0 auto}.qc.prot2 .pans{position:absolute;right:3mm;bottom:2mm;display:flex;align-items:center;gap:0.5mm;font-size:18pt;font-weight:700}
.srows3.grid2{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:3.5mm 5mm}
.srows3.grid2 .srow3{border:0.4mm solid #000;border-radius:2mm;padding:2mm 3mm;position:relative;min-height:0;align-items:center}
.srows3.grid2 .srow3 .no{position:absolute;left:2mm;top:2mm}
.srows3.grid2 .sopts{flex-direction:column;align-items:flex-start;gap:2.2mm;margin-left:0}
.afig{display:flex;flex-direction:column;align-items:center}.afig>svg{width:52mm;height:35mm;max-width:none}.aq{margin:0;font-size:11pt;font-weight:700;text-align:center;line-height:1.1}
.srows3.grid2 .tfo{display:flex;align-items:center;gap:2mm}.srows3.grid2 .tfo b{font-size:13pt;min-width:15mm}.afig>svg{display:block}
.figwrap svg{max-width:none;width:170mm;height:auto}
.srow3 .sq3 svg{max-width:none}
.dect td.pt{font-size:22pt;width:8mm;border-left:none;border-right:none}.dect th:nth-child(2){border:none;width:8mm}
.dcs{display:flex;gap:4mm;flex-wrap:wrap}.dcs.five{gap:3mm}
.dc{position:relative;border:0.5mm solid #000;border-radius:2mm;min-width:36mm;height:16mm;display:flex;align-items:center;justify-content:center;font-family:'Fredoka';font-weight:600;font-size:19pt;padding:1.5mm 2mm 0 6mm}
.dcs.five .dc{min-width:30mm;flex:1}
.dc i.cl{position:absolute;left:1.2mm;top:1.2mm;width:6.5mm;height:6.5mm;font-size:11pt}
.dc .fr{font-size:15pt}
.mrows{display:flex;flex-direction:column;gap:1.5mm}
.mrow{display:flex;align-items:center;gap:4mm;border-bottom:0.3mm solid #000;padding-bottom:1.2mm}
.mrow .mq{font-family:'Fredoka';font-weight:600;font-size:19pt;min-width:42mm;display:inline-flex;align-items:center;gap:2mm}.mrow .mq .fr{font-size:15pt}
.mrow .mto{flex:1;font-size:12pt;font-weight:700}
.dcs.big{gap:6mm}.dcs.big .dc{height:24mm;font-size:28pt;min-width:50mm;padding-left:8mm}.dcs.big .dc i.cl{width:8mm;height:8mm;font-size:13pt}
.msqwrap{display:flex;justify-content:center;padding:6mm 0}
.msq{display:grid;grid-template-columns:repeat(3,50mm);grid-auto-rows:34mm;border:0.9mm solid #000}
.mq3{border:0.9mm solid #000;display:flex;align-items:center;justify-content:center;font-family:'Fredoka';font-weight:700;font-size:30pt}
.mq3 .ab.mb{width:38mm;height:17mm}
.fgc svg{display:block;max-width:none}.fgc{display:flex;justify-content:center}
.qc.fgq .qt{display:flex;flex-direction:column;align-items:center}.qc.fgq .fq{margin:0.5mm 0 0;font-size:12pt;font-weight:700}
.qc.fgq{position:relative}.qc.fgq .no{position:absolute;left:2mm;top:2mm}
.qc.fgq .qa{font-size:13pt;font-weight:700}
.qc.fgq2 .qt{flex:none}.qc.fgq2 .qa{flex-direction:column;align-items:flex-start;gap:1mm;font-size:12pt;font-weight:700}.fq2{font-size:12pt;font-weight:700}
.qc.fgq2 .no{position:absolute;left:2mm;top:2mm}.qc.fgq2{position:relative}
.qc.fgq .qt{margin-left:6mm}
.mfigs{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:3mm 5mm}
.mfig{position:relative;border:0.4mm solid #000;border-radius:2mm;padding:1.5mm 2mm;display:flex;justify-content:center;align-items:center;min-height:36mm}
.mfig i.cl{position:absolute;left:2mm;top:2mm;width:8.5mm;height:8.5mm;font-size:13pt}
.mrows2{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:1.5mm 6mm}
.mrows2 .mrow{border-bottom:0.3mm solid #000}
.mq2{flex:1;font-family:'Fredoka';font-weight:600;font-size:14pt}
.srows3.grid2.corner .srow3{flex-direction:column;align-items:center;padding:2mm}.srows3.grid2.corner .sq3{flex:none}
.sblock{display:flex;gap:6mm;align-items:center;margin-bottom:3mm}.sfig svg{display:block;max-width:none}
.sqs{display:flex;flex-direction:column;gap:3mm;flex:1}.qrow2{display:flex;align-items:center;gap:2.5mm;font-size:12.5pt;line-height:1.2}.qrow2 .qt{flex:1}
.tt37{border-collapse:collapse;margin:3mm auto 0;font-size:17pt}.tt37 th,.tt37 td{border:0.5mm solid #000;text-align:center;height:19mm;min-width:30mm;font-family:'Fredoka';font-weight:600}
.tt37 th{background:#fff;font-weight:700;font-size:14pt}.tt37 .ab.tb{width:22mm;height:13mm}
.lgraph{display:flex;justify-content:center;margin-bottom:2mm}.lgraph svg{max-width:none;width:160mm;height:auto}
.lqs{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:3mm 6mm}
.sblock.pieb .sfig svg{width:90mm;height:90mm}
.srows3.grid2.solids .sopts{gap:1.5mm}.srows3.grid2.solids .tfo b{font-size:11.5pt;min-width:32mm}
.netfig svg{max-width:none}.srows3.grid2.solids .afig>svg{width:33mm;height:28mm}.srows3.grid2.solids .srow3{min-height:42mm}.srows3.grid2 .afig.netfig>svg{width:34mm;height:29mm}.srows3.grid2 .afig.netfig{margin:4mm 0 0 4mm}.lqs{margin-bottom:2mm}
"""
CSS_P4B = CSS_P4B + """.codetable[style*="repeat(8"] .ct,.codetable[style*="repeat(9"] .ct{min-width:0;padding:0.6mm 1.2mm;gap:1mm;font-size:13.5pt}.codetable[style*="repeat(8"] .ct b,.codetable[style*="repeat(9"] .ct b{padding-left:1.2mm;font-size:16pt}
.maze:not(.tall) .mcell small{font-size:9.5pt}
"""
CSS_P4B = CSS_P4B + """.dcs.big .dc{height:36mm;font-size:32pt}.qc.fgq .qt{margin-left:9mm}
"""
CSS_P4B = CSS_P4B + """.srows3.grid2.solids .afig{flex:none;width:33mm;margin-left:2mm}
"""
CSS_P4B = CSS_P4B + """.afig.mir>svg{width:44mm;height:32.5mm;margin-left:5mm}.afig.mir .aq{margin-top:2mm}
"""
CSS_P4B = CSS_P4B + """.qg.work .qc{min-height:23mm}.vcards.vc3 .vcard .vans{margin-top:9mm}
"""
CSS_P4B = CSS_P4B + """.qc.fgq2 .fgc{padding:5mm 0 0 0}\n"""
CSS_P4B = CSS_P4B + """.codetable[style*="repeat(8"] .ct{padding:0.6mm 0.8mm;gap:0.8mm;font-size:12.5pt}.codetable[style*="repeat(8"] .ct b{padding-left:0.8mm;font-size:15pt}\n"""
CSS_P4B = CSS_P4B + """.vcards.vc3 .vcard .vans{position:relative}.vcards.vc3 .vcard .vans:before{content:"Working";position:absolute;left:0;right:0;top:-7.5mm;border-top:0.3mm solid #000;font-size:8pt;font-weight:600;text-align:left;padding-top:0.3mm}.qg.work .qc:after{content:"Working";position:absolute;left:3mm;bottom:1.5mm;width:55%;border-top:0.3mm solid #000;font-size:8pt;font-weight:600;padding-top:0.3mm}.qg.work .qc{padding-bottom:6mm}"""