CSS_NEW = """
/* ---- new pages (P1-21 to P1-40) ---- */
.stories{display:grid;grid-template-columns:1fr 1fr;gap:3.5mm 5mm}
.story{border:0.4mm solid #000;border-radius:2mm;padding:2mm 3mm;display:flex;flex-direction:column;gap:1mm}
.story .sh{display:flex;align-items:flex-start;gap:2.5mm}
.story .stx{flex:1}.story p.st{margin:0;font-size:12.5pt;line-height:1.22}
.story .sp{display:flex;flex-direction:column;gap:0.6mm}.story .sp svg{display:block}
.story .sa{display:flex;align-items:center;gap:2mm}.story .sa.below{gap:5mm;justify-content:flex-end}.story .sa.below .lbx small{font-size:8.5pt}
"""
CSS_NEW += """
/* N10 stack it up */
.vsums{display:grid;grid-template-columns:repeat(3,1fr);gap:4mm 5mm}
.vcard{border:0.4mm solid #000;border-radius:2mm;padding:2mm 3mm 3mm;display:flex;flex-direction:column;align-items:center;gap:1mm}
.vcard .no{align-self:flex-start}
.vs{display:grid;grid-template-columns:9mm 13mm 13mm;gap:1mm 1mm;align-items:center;justify-items:center;font-family:'Fredoka';font-weight:600;font-size:26pt;line-height:1}
.vs i{font-style:normal;display:flex;align-items:center;justify-content:center;width:13mm;height:13mm}
.vs i.ab{width:13mm;height:13mm;border:0.6mm solid #000;border-radius:1.5mm}
.vs b{font-weight:600;font-size:24pt}
.vs .rule{grid-column:1 / 4;width:100%;border-top:0.8mm solid #000;height:0}
.vlab{font-size:9pt;font-weight:700;display:grid;grid-template-columns:9mm 13mm 13mm;gap:1mm;justify-items:center}
/* N04 domino maze */
.dm{display:flex;flex-direction:column;align-items:center;gap:1.2mm;width:100%}
.dm .dw{font-family:'Nunito Sans';font-weight:800;font-size:12.5pt;padding:0 1mm;text-align:center}
.dm .dl{width:80%;border-top:0.4mm solid #000;height:0}
.dm .dn{font-family:'Fredoka';font-weight:600;font-size:22pt}
/* N05 count the crowd */
.cc3{display:grid;grid-template-columns:repeat(3,1fr);gap:4mm}.cc2{display:grid;grid-template-columns:1fr 1fr;gap:4mm 6mm}
.cc{border:0.4mm solid #000;border-radius:2mm;padding:2mm 3mm;display:flex;flex-direction:column;gap:1.5mm;align-items:center}
.cc .ch{display:flex;align-items:center;gap:2mm;align-self:stretch}.cc .ch .cq{flex:1;font-size:12.5pt;line-height:1.2}.cc .ch .ab{flex:none}
/* N06 hundred chart */
.hchart{display:grid;grid-template-columns:repeat(10,13.4mm);margin:0 auto;border:0.8mm solid #000;width:max-content}
.hc{border:0.4mm solid #000;height:12mm;display:flex;align-items:center;justify-content:center;font-family:'Fredoka';font-weight:600;font-size:13pt}
.hc.ab{border-radius:0;width:auto;height:12mm;background:#fff}
.dtable{border-collapse:collapse;margin:0 auto}.dtable th,.dtable td{border:0.5mm solid #000;width:22mm;height:12.5mm;text-align:center;font-family:'Fredoka';font-weight:600;font-size:15pt}.dtable th{font-family:'Nunito Sans';font-weight:800;font-size:11pt;height:8mm}
.dtable td .ab{width:16mm;height:12mm;border-width:0.5mm}
.mq{display:flex;gap:6mm;justify-content:center;font-size:14.5pt;flex-wrap:wrap}.mq .mqi{display:flex;align-items:center;gap:2mm}
"""
CSS_NEW += """
/* money and time pages */
.qrow{display:flex;align-items:center;gap:3mm;font-size:14.5pt;padding:1.5mm 0;border-bottom:0.3mm solid #000;line-height:1.2}
.qrow .qt{flex:1}.qrow .ab{flex:none}
.legend2{display:flex;align-items:center;gap:4mm;font-size:13pt;font-weight:700;justify-content:center}
.purses{display:grid;grid-template-columns:repeat(3,1fr);gap:3mm 4mm}
.purse{border:0.4mm solid #000;border-radius:2mm;padding:1.5mm 2mm;display:flex;align-items:center;gap:1mm}
.purse .ab{width:12mm;height:12mm}
.board{display:grid;grid-template-columns:repeat(3,1fr);gap:3mm 4mm}
.bitem{border:0.4mm solid #000;border-radius:2mm;padding:1.5mm 2mm;display:flex;align-items:center;gap:2.5mm}
.bitem svg{flex:none}.bitem .bn{flex:1;font-size:12.5pt;font-weight:700;line-height:1.15}.bitem .bp{font-family:'Fredoka';font-weight:700;font-size:17pt}
.bitem i.cl{font-style:normal;display:inline-flex;align-items:center;justify-content:center;width:8.5mm;height:8.5mm;border:0.5mm solid #000;border-radius:50%;font-size:14pt;font-weight:700;flex:none}
.buyer{display:flex;align-items:center;gap:3mm;font-size:14.5pt;padding:2mm 0;border-bottom:0.3mm solid #000}.buyer .bt{flex:1}.buyer .ab{width:14mm}
.tcards{display:grid;grid-template-columns:1fr 1fr;gap:3mm 5mm}
.tcard{border:0.4mm solid #000;border-radius:2mm;padding:2mm 3mm;display:flex;flex-direction:column;gap:1mm}
.tcard .th{display:flex;align-items:center;gap:2mm;font-size:12.5pt;font-weight:700}
.tcard .tclk{display:flex;align-items:center;gap:2mm;justify-content:center}.tcard .tclk small{font-size:10pt;font-weight:700;text-align:center;display:block}
.tcard .ta{display:flex;align-items:center;gap:2mm;justify-content:flex-end;font-size:12.5pt}
.tt{border-collapse:collapse;margin:0 auto}.tt th,.tt td{border:0.5mm solid #000;height:13mm;font-size:14pt;text-align:center;padding:0 3mm}.tt th{font-size:11pt;font-weight:800;height:9mm}.tt td .ab{width:20mm;height:12mm}
.tm{font-family:'Fredoka';font-weight:600;font-size:19pt}.ev{font-size:11.5pt;font-weight:700}
"""
CSS_NEW += """
.purse{flex-direction:row;justify-content:space-between}.purse .ab{width:11mm;height:12mm}.qrow{padding:1mm 0}
.bitem{padding:3mm 3mm}.bitem .bn{font-size:14pt}.bitem .bp{font-size:20pt}
.buyer{padding:5mm 0;font-size:15pt}.buyer .wk{display:flex;align-items:center;gap:1.5mm;font-size:14pt}.buyer .wk .ab{width:13mm}.buyer .lt{font-size:10pt;font-weight:700}
"""
CSS_NEW += """.qgrid{display:grid;grid-template-columns:1fr 1fr;gap:0 6mm}.qgrid .qrow{font-size:13.5pt}"""
CSS_NEW += """.tcard svg{width:36mm;height:36mm}.tt td .no{margin:0 auto}.tt th,.tt td{padding:0 2.5mm}"""
CSS_NEW += """
.lrow .lcl{display:inline-flex;align-items:center;justify-content:center;width:9mm;height:9mm;border:0.5mm solid #000;border-radius:50%;font-weight:800;font-size:14pt;flex:none}
.rr{display:flex;align-items:center;gap:3mm;border-bottom:0.3mm solid #000;padding-bottom:1.5mm}.rr .rs{flex:none}.rr .rs svg{max-width:none;display:block}.rr .rt{flex:1;font-size:12pt;line-height:1.2}.rr .rb{display:flex;align-items:center;gap:2mm;font-size:12pt;font-weight:700}
.rrows{display:flex;flex-direction:column;gap:2.2mm}
"""
CSS_NEW += """.srows.s5{gap:3mm}.srow .sn{font-size:9.5pt;line-height:1.15;width:22mm}.srow .sn b{font-size:10.5pt}.srows.s5 .srow svg{width:13mm}"""
CSS_NEW += """.rt2{display:flex;flex-wrap:wrap;align-items:center;gap:1mm 1.5mm;width:36mm;font-size:11pt}.rt2 small{font-size:9pt;font-weight:700}.rt2 b{width:100%;font-size:11.5pt}
.ctrow{display:grid;grid-template-columns:repeat(12,1fr);border:0.5mm solid #000}.ctrow div{border-left:0.3mm solid #000;text-align:center;line-height:1.1}.ctrow div:first-child{border-left:none}.ctrow span{display:block;font-weight:800;font-size:11pt;border-bottom:0.3mm solid #000}.ctrow b{font-family:'Fredoka';font-size:17pt;font-weight:700}
.rr{gap:2mm}"""
CSS_NEW += """.rt2{flex-wrap:nowrap;width:40mm;justify-content:flex-end}.rr{padding-bottom:0.5mm}.rrows{gap:1.2mm}.rt2 .lbx b{font-size:11.5pt}"""
CSS_NEW += """
.frows{display:flex;flex-direction:column;gap:4mm}
.frow{display:flex;align-items:center;gap:3mm;border-bottom:0.3mm solid #000;padding-bottom:2mm}
.fg{display:flex;flex-direction:column;gap:0.8mm;flex:none}.fg small,.fo small{font-size:9pt;font-weight:700}.fg svg,.fo svg{display:block;max-width:none}
.fo{display:flex;flex-direction:column;gap:0.8mm}.opts{display:flex;gap:4mm}.opt{display:flex;flex-direction:column;align-items:center;gap:1mm}
.opt i.cl{font-style:normal;display:inline-flex;align-items:center;justify-content:center;width:8mm;height:8mm;border:0.5mm solid #000;border-radius:50%;font-size:13pt;font-weight:700}
"""
CSS_NEW += """.pgraph.sm{gap:1.5mm}.pgraph.sm .gc{width:11.5mm;height:11.5mm}.pgraph.sm .gl{width:30mm;font-size:14pt}.pgraph.sm .gl svg{width:8mm;height:8mm}"""
CSS_NEW += """.srows.s5 .srow{flex-direction:column;width:33mm;text-align:center;gap:1mm}.srows.s5 .srow .sn{width:auto}.srows.s5 .srow .ab{width:14mm}"""
CSS_NEW += """
.tfrows{display:flex;flex-direction:column;gap:2mm}.tfrow{padding:6.5mm 0}.tfrow .qt{font-size:16pt}
.tfo{display:flex;align-items:center;gap:2mm;font-size:15pt;font-weight:800;margin-left:4mm}.tfo i.cl{font-style:normal;display:inline-flex;align-items:center;justify-content:center;width:8.5mm;height:8.5mm;border:0.5mm solid #000;border-radius:50%;font-size:14pt;font-weight:700}
"""
CSS_NEW += """.ansgrid2{display:flex;gap:6mm;justify-content:center;margin-top:1mm}"""
CSS_NEW += """.sumrows.arrs{gap:3mm 6mm}.sumcell{display:flex;flex-direction:column;gap:1mm;border-bottom:0.3mm solid #000;padding-bottom:2mm}.sumcell .arr{display:flex;justify-content:center}.sumcell .arr svg{max-width:none}"""
CSS_NEW += """.ctc .codetable{gap:2mm;flex-wrap:nowrap}.ctc .ct{min-width:0;flex:1;padding:0.6mm 1.5mm;font-size:14pt}.ctc .ct b{font-size:16pt}.sumrows.arrs .sumrow{font-size:21pt}"""
CSS_NEW += """.shrows{gap:0.3mm}.shrow{padding:0.2mm 0 0.8mm}.shtxt{margin:0 0 0.6mm}.shrow .ab{height:13mm}"""
