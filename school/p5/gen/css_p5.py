"""CSS of the Primary 5 pages (added to render.CSS after css_p2). Pure black and white; rules at least 0.4 mm; answer boxes at least 12 mm high."""
CSS_P5 = """
/* ---- Primary 5 pages ---- */
.fr{font-size:15pt}
.qt .fr,.ot .fr,.oc .fr,.mc2 .fr,.tv .fr,.rc .fr,.dn .fr{font-size:15pt}
.fr i{padding:0 1.3mm}
.mx{display:inline-flex;align-items:center;gap:0.8mm;vertical-align:middle}
.mx b{font-family:'Fredoka';font-weight:600;font-size:17pt}
.ab.w2{width:15mm;height:12mm}.ab.w5{width:44mm}.ab.w6{width:52mm}
.fans .ab.w2{width:15mm;height:12mm}
.qa .fans{margin-left:1mm}
.qg.c2 .qc,.qg.c3 .qc{min-height:30mm}
.qc .qt{font-size:13pt;line-height:1.25}
.qc .qt.big{font-size:17pt;font-family:'Fredoka';font-weight:500}
.qc .qt .num{font-family:'Fredoka';font-weight:600}
/* lettered choices */
.mcrow{align-items:center;gap:3mm;padding:1.2mm 0;flex-wrap:nowrap}
.mcrow .mq{flex:0 0 58mm;font-size:13pt;line-height:1.22}
.mcrow .mq svg{max-width:none;display:block;margin-top:1mm}
.mopts{display:flex;gap:2.5mm;flex:1;justify-content:flex-end;flex-wrap:nowrap}
.mopts.col{flex-direction:column;align-items:flex-start;gap:1.2mm}
.mo{display:inline-flex;align-items:center;gap:1.5mm;border:0.4mm solid #000;border-radius:2mm;padding:1mm 2mm}
.mo .ot{font-family:'Fredoka';font-weight:500;font-size:14pt;white-space:nowrap}
.mopts.col .mo .ot{white-space:normal;font-family:'Nunito Sans';font-weight:700;font-size:12pt;line-height:1.2}
.mcrow.wide{flex-wrap:wrap;row-gap:1.6mm}.mcrow.wide .mq{flex:1 1 calc(100% - 12mm)}.mcrow.wide .mopts{flex:1 1 100%;justify-content:flex-start}
.tfrows{gap:1.4mm}
.tfrows .mcrow{padding:3.4mm 0}
.tfrows.tight .mcrow{padding:1.3mm 0}
.tfrow2{display:flex;align-items:center;gap:3mm;border-bottom:0.3mm solid #000;padding:3.4mm 0}
.tfrow2 .qt{flex:1;font-size:15pt;font-family:'Fredoka';font-weight:500}
/* ordering cards */
.ocards{display:grid;gap:5mm 4mm}.ocards.c3{grid-template-columns:repeat(3,minmax(0,1fr))}.ocards.c2{grid-template-columns:repeat(2,minmax(0,1fr))}
.ocard{position:relative;border:0.6mm solid #000;border-radius:2.5mm;min-height:50mm;display:flex;align-items:center;justify-content:center;padding:4mm 3mm 3mm 3mm}
.ocard i.cl{position:absolute;left:2mm;top:2mm}
.ocard{flex-direction:column;gap:3mm}
.ocard .wk{font-family:'Fredoka';font-weight:600;font-size:17pt;display:flex;align-items:center;gap:2mm}
.ocard .oc{font-family:'Fredoka';font-weight:500;font-size:17pt;text-align:center;line-height:1.3}
/* matching */
.mcards2{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:4mm}
.mcard2{position:relative;border:0.5mm solid #000;border-radius:2mm;min-height:23mm;display:flex;align-items:center;justify-content:center;padding:2mm 2mm 2mm 10mm}
.mcard2 i.cl{position:absolute;left:1.5mm;top:1.5mm}
.mcard2 .mc2{font-family:'Fredoka';font-weight:500;font-size:15pt;text-align:center;line-height:1.25}
.tiles{display:grid;grid-template-columns:repeat(6,minmax(0,1fr));gap:3mm}
.tile{border:0.5mm solid #000;border-radius:2mm;display:flex;flex-direction:column;align-items:center;gap:2mm;padding:2mm 1mm 2mm}
.tile .tv{font-family:'Fredoka';font-weight:600;font-size:15pt;text-align:center;min-height:15mm;display:flex;align-items:center;justify-content:center;line-height:1.2}
.tile .ab.letter{width:14mm;height:13mm}
/* routes */
.maze.tall .mcell{height:40mm}
.rc{font-family:'Fredoka';font-weight:600;font-size:15pt;text-align:center;line-height:1.2;padding:0 1mm}
.rc.sm{font-size:12.5pt}
.maze .mcell .flag{font-size:8pt}
/* digit cards */
.dtiles{display:flex;gap:1.3mm;justify-content:center;margin:1mm 0 1.5mm}
.dtile{width:8.6mm;height:13mm;border:0.6mm solid #000;border-radius:1.5mm;display:flex;align-items:center;justify-content:center;font-family:'Fredoka';font-weight:600;font-size:18pt}
/* equations */
.eqlist{display:flex;flex-direction:column;gap:3.5mm}
.eqrow{display:flex;align-items:center;gap:3mm;border-bottom:0.3mm solid #000;padding-bottom:2mm}
.eqrow .eqt{font-family:'Fredoka';font-weight:600;font-size:21pt;display:flex;align-items:center;gap:2mm;flex:1;white-space:nowrap}
.eqrow .ab{width:17mm;height:13mm}
/* magic square */
.msq{display:grid;grid-template-columns:repeat(3,40mm);grid-auto-rows:40mm;margin:0 auto;width:max-content}
.msq .mq3{border:0.9mm solid #000;margin:-0.45mm;display:flex;align-items:center;justify-content:center;font-family:'Fredoka';font-weight:600;font-size:20pt}
.msq .mq3 .mx b{font-size:22pt}
.msq .mq3 .ab.w2{width:12mm}
.msq .mq3 .mxa{display:flex;align-items:center;gap:1mm}
.msq .mq3 .fans .ab.w2{width:13mm}
/* number chain loop */
.cloop{display:grid;grid-template-columns:repeat(5,auto);align-items:center;justify-content:center;gap:1mm 0;margin:0 auto}
.cn{width:30mm;height:28mm;border:0.7mm solid #000;border-radius:50%;display:flex;align-items:center;justify-content:center;font-family:'Fredoka';font-weight:600;font-size:24pt}
.cn.blank{border-style:solid}
.cn .ab{width:18mm;height:13mm;border-width:0.5mm}
.car{display:flex;flex-direction:column;align-items:center;gap:0.3mm;font-family:'Fredoka';font-weight:600;font-size:15pt;min-width:40mm}
.car .arrow{width:100%;border-top:0.7mm solid #000;position:relative;height:0}
.car .arrow:after{content:'';position:absolute;right:-0.5mm;top:-2mm;border-left:4mm solid #000;border-top:2mm solid transparent;border-bottom:2mm solid transparent}
.car.back .arrow:after{right:auto;left:-0.5mm;border-left:none;border-right:4mm solid #000}
.vcon{display:flex;flex-direction:column;align-items:center;justify-content:center;font-family:'Fredoka';font-weight:600;font-size:15pt;gap:0.5mm}
.vcon .vline{height:30mm;border-left:0.7mm solid #000;position:relative}
.vcon.up .vline:before,.vcon.dn .vline:after{content:'';position:absolute;left:-2mm;border-left:2mm solid transparent;border-right:2mm solid transparent}
.vcon.dn .vline:after{bottom:-0.5mm;border-top:4mm solid #000}
.vcon.up .vline:before{top:-0.5mm;border-bottom:4mm solid #000}
/* figures */
.figs{display:grid;gap:3mm 4mm}.figs.c3{grid-template-columns:repeat(3,minmax(0,1fr))}.figs.c2{grid-template-columns:repeat(2,minmax(0,1fr))}
.fig{border:0.4mm solid #000;border-radius:2mm;padding:1.5mm 2mm;display:flex;flex-direction:column;align-items:center;gap:1mm;position:relative}
.fig .no{position:absolute;left:1.5mm;top:1.5mm}
.fig svg{max-width:none;display:block}
.fig .qa{display:flex;align-items:center;gap:2mm;font-size:14pt;font-weight:700}
.fig .qa .ab{width:20mm;height:12.5mm}
.fsvg{display:block}
.ptxt{font-size:13pt;line-height:1.25}
.note5{font-size:11.5pt}
.gridnote{font-size:12pt;font-weight:700}
.kcard{font-size:11pt}
.stackq{display:flex;flex-direction:column;gap:1mm}
.mq.big{font-size:17pt;font-family:'Fredoka';font-weight:500}
.mq.big .fr{font-size:17pt}
.mcgrid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:3mm 4mm}
.mcgrid .mcrow{flex-direction:column;align-items:flex-start;border:0.4mm solid #000;border-radius:2mm;padding:1.4mm 3mm;position:relative;gap:1.5mm}
.mcgrid .mcrow .no{position:absolute;left:2mm;top:2mm}
.mcgrid .mq{flex:none;padding-left:8mm;font-size:12pt;line-height:1.15}.mcgrid .mq svg{margin:1mm auto 0}
.mcgrid .mopts{justify-content:center;width:100%}
.mcard2:has(svg){padding:5mm 1mm 1mm}
.mcard2:has(svg) .mc2 svg{max-width:none}
.qg.c3 .qc svg.fsvg,.qg.c2 .qc svg.fsvg{max-width:100%;height:auto}
em.msum{font-style:normal;font-weight:800;font-family:'Fredoka';font-size:16pt}
.unit{font-size:14pt;font-weight:700;margin-left:1mm}
.qg.s16 .qc{padding:1.2mm 3mm;gap:0.5mm}.qg.s16 .qc .qt{font-size:12pt;line-height:1.1}.qg.s16 .qt .fr{font-size:12.5pt}
.qg.s27 .unit{display:inline-block;width:16mm;margin-left:1.5mm}
.maze.tri .mcell{align-items:flex-end}
.qg .qc.figc svg.fsvg{max-width:none;margin-left:-10mm;margin-top:2mm}
"""
