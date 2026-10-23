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
"""
