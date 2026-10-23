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
