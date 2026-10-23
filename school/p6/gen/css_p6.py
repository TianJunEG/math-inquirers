"""CSS of the Primary 6 page types (added to render.CSS after the shared P2 CSS it was copied from). Pure black and white."""
CSS_P6 = """
/* ---- Primary 6 pages ---- */
.sy{font-family:'DejaVu Sans','Liberation Sans',Arial,sans-serif;font-weight:400}
.mx{font-family:'Fredoka';font-weight:600;font-size:1.25em;margin-right:0.6mm;vertical-align:middle}
.unit{font-size:13pt;font-weight:700;margin-left:1mm;white-space:nowrap}
.qc .qt{font-size:13pt}
.fr{font-size:13pt}
.fans .ab.w2{width:17mm;height:12.5mm}
.rt{font-family:'Fredoka';font-weight:600;font-size:15pt;white-space:nowrap}
.eqn{font-family:'Fredoka';font-weight:600;font-size:17pt;display:block;line-height:1.5}
.eqn .ab,.eqn .fans,.eqn .fr{vertical-align:middle}
.fans{display:inline-flex !important;vertical-align:middle;margin-left:1mm}
.eqn .ab{width:20mm}
.maze.sm .mcell{font-size:15pt;height:31mm;padding:0 1mm;text-align:center;line-height:1.15}
.maze.sm.tall .mcell{height:36mm}
.maze.sm .mcell .fr{font-size:15pt}
.maze.xs .mcell{font-size:12.5pt;height:36mm;padding:0 1.5mm;text-align:center;line-height:1.2}
.maze.xs .mcell .fr{font-size:13pt}
/* lettered choices */
.chrows{display:flex;flex-direction:column;gap:1mm}
.chrow{display:flex;align-items:flex-start;gap:2.5mm;border-bottom:0.3mm solid #000;padding:0.5mm 0 1.4mm}
.chrow .no{margin-top:0.5mm}
.chb{flex:1;min-width:0}
.chs{font-size:12.5pt;line-height:1.2;margin-bottom:1.2mm}
.cho{display:flex;gap:4mm;flex-wrap:wrap}
.chop{display:inline-flex;align-items:center;gap:1.8mm;border:0.4mm solid #000;border-radius:2mm;padding:0.5mm 2.5mm 0.5mm 1.4mm;font-size:13.5pt;font-family:'Fredoka';font-weight:500}
.chop .cht{white-space:nowrap}
.cho.wide .chop .cht{white-space:normal}
/* matching */
.mgrid{display:grid;gap:4mm 6mm;margin-bottom:5mm}
.mit{display:flex;align-items:center;gap:2.5mm;border:0.4mm solid #000;border-radius:2mm;padding:2.6mm 3mm}
.mit .mtt{flex:1;font-family:'Fredoka';font-weight:500;font-size:16pt;line-height:1.25}
.mit .ab{width:14mm;height:12.5mm;flex:none}
.mcards2{display:grid;gap:4mm 3mm}
.mcd{position:relative;border:0.55mm solid #000;border-radius:2mm;padding:3mm 2mm 3mm 11mm;display:flex;align-items:center;min-height:21mm}
.mcd .cl{position:absolute;left:1.6mm;top:50%;margin-top:-4.25mm}
.mcd .mct{font-family:'Fredoka';font-weight:500;font-size:15pt;line-height:1.2}
/* ordering cards */
.ogrid{display:grid;gap:3mm 4mm}
.ocd{position:relative;border:0.55mm solid #000;border-radius:2mm;padding:2mm 2mm 2mm 11mm;display:flex;align-items:center;justify-content:center;min-height:20mm}
.ocd .cl{position:absolute;left:1.6mm;top:1.6mm}
.ocd .oct{font-family:'Fredoka';font-weight:500;font-size:15pt;text-align:center;line-height:1.2}
.ocd svg{max-width:none;display:block}
/* domino loop */
.doms{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:4mm 6mm}
.dom{position:relative;display:grid;grid-template-columns:1fr 1fr;border:0.6mm solid #000;border-radius:2.5mm;min-height:27mm}
.dom .cl{position:absolute;left:-0.3mm;top:-3.4mm;background:#fff;z-index:2}
.dom .dstart{position:absolute;right:2mm;top:-2.8mm;background:#000;color:#fff;font-style:normal;font-weight:800;font-size:8.5pt;letter-spacing:.3mm;padding:0.4mm 2mm;border-radius:1mm;z-index:2}
.dom .dh{display:flex;flex-direction:column;gap:1mm;align-items:center;justify-content:center;text-align:center;padding:2mm 1.5mm;font-family:'Fredoka';font-weight:500;font-size:14pt;line-height:1.2}
.dom .dh.r{border-left:0.6mm solid #000}
/* figures in cards */
.fig{display:flex;justify-content:center;align-items:center}
.fig svg{max-width:none;display:block}
.qc .fig{padding:0.5mm 0}
.qa .ab.w4{width:30mm}
.note1{font-size:11.5pt;line-height:1.25;padding:0.5mm 0}
.legend2{display:flex;gap:6mm;justify-content:center;align-items:center;font-size:12.5pt;font-weight:700;margin:1mm 0}
.tbl2{border-collapse:collapse;margin:0 auto}.tbl2 th,.tbl2 td{border:0.5mm solid #000;font-size:13pt;text-align:center;padding:1.2mm 3.5mm}.tbl2 th{font-weight:800;background:#fff}
.tbl2 td.q{font-weight:800}
.twobox{display:grid;grid-template-columns:1fr 1fr;gap:5mm}
.sumline{font-size:13.5pt;font-weight:700;border:0.55mm solid #000;border-radius:2mm;padding:1.2mm 3mm;text-align:center}
.qc{padding:1.5mm 3mm}
.qg{gap:3mm 5mm}
.v{font-style:italic;font-family:'Fredoka';font-weight:600;padding:0 0.3mm}
.eqn .v{font-size:1.05em}
.sq{font-size:inherit}
.fr .v{font-size:0.95em}
html,body{font-family:'Nunito Sans','DejaVu Sans','Liberation Sans',Arial,sans-serif}
.figrow{display:flex;align-items:center;gap:2.5mm}
.figrow p{margin:0;font-size:12.5pt;line-height:1.2}
.cap{font-weight:700;font-size:12.5pt;line-height:1.2;max-width:26mm}
.qc.inl .qt{min-width:0}
.figrow svg{flex:none}
.chgrid{display:grid !important;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:3mm 5mm}
.chgrid .chrow{border:0.4mm solid #000;border-radius:2mm;padding:2mm 2.5mm}
.chgrid .chb{display:block}
.chgrid .chs{margin:0 0 1.5mm}
.chgrid .cho{flex-direction:row;gap:1.6mm;flex-wrap:nowrap;justify-content:space-between}
.chgrid .chop{padding:0.5mm 1.4mm 0.5mm 0.8mm;font-size:11.5pt;gap:1mm}
.chgrid .chop .cl{width:7.2mm;height:7.2mm;font-size:12pt}
.chgrid .cho .chop .rt{font-size:11.5pt}
.mgrid.cmp .mit{padding:1.2mm 2.5mm}
.mgrid.cmp .mit .mtt{font-size:12.5pt}
.mcards2.cmp .mcd{min-height:13mm;padding:1.5mm 2mm 1.5mm 11mm}
.mgrid.cmp{margin-bottom:2mm;gap:2.2mm 6mm}
.mcards2.cmp{gap:2.5mm 3mm}
.fcd{}
.fcd .fig svg{max-width:46mm}
.mgrid.vert .mit{flex-direction:column;align-items:center;gap:1.5mm;position:relative;padding:1.5mm 2mm 2mm}
.mgrid.vert .mit .no{position:absolute;left:2mm;top:2mm}
.mgrid.vert .mit .mtt{width:100%}
.mgrid.vert .mit .ab{align-self:center}
.mgrid.vert .mit .mrow{display:flex;align-items:center;gap:2mm;width:100%}
.mgrid.vert .mit .mcap{flex:1;font-family:'Nunito Sans';font-weight:400;font-size:11pt;line-height:1.2}
.mgrid.vert .mit .mcap p{margin:0}
.mgrid.vert .mit .mtt{display:flex;justify-content:center}
.mgrid.vert .mit .ab{align-self:auto;margin:0;width:13mm;flex:none}
.ctc.dense .ct{font-size:11pt;gap:0.8mm;padding:0.6mm 0.4mm}
.ctc.dense .ct b{font-size:13.5pt;padding-left:1mm;min-width:3.5mm}
.ctc.dense .ct .n{font-size:11pt}
.dom .dt{display:block;text-align:center}
.dom .dt .ex,.dom .dt .wh{display:block}
.qc.posb .no{position:absolute;left:2mm;bottom:2mm}.qc.posb .qh{justify-content:center}
.mgrid.vert .mit .mrow .no{position:static}
.mgrid.vert .mit{padding:1.2mm 2mm 1.6mm;gap:0.8mm}
.mgrid.vert .mit .mtop{display:flex;justify-content:space-between;align-items:center;width:100%;margin-bottom:-6mm;position:relative;z-index:2}
.mgrid.vert .mit .mtop .no{position:static}
.mgrid.vert .mit .mcap{font-size:10.5pt;line-height:1.18;width:100%}
.mgrid.vert .mit .mcap p{margin:0}
.maze .sy{font-size:1.18em}
.mnc{font-family:'Fredoka';font-weight:600;font-size:16pt;text-align:center;line-height:1.5}
.mnc p{margin:0;font-size:13pt;font-weight:500;line-height:1.3}
"""
