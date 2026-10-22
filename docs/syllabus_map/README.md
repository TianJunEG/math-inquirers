# Syllabus map (parent-facing)

Data and builders for the parent syllabus map and the tier map.

- `intl_rows_12places.json`: 12 places x 60 lessons (from docs/audit/intl_mapping_*.md).
- `add_singapore.py`: adds 60 Singapore (MOE) rows from docs/audit/moe_alignment_*.md, writes `intl_rows.json` (13 places).
- `build_tier_rows.py`: writes `tier_rows.json` (Start here / Think harder / Go further vs the syllabus, per level).
- `build_static.py`: writes `website/syllabus/index.html` (both maps, self-contained, site style; link as `/syllabus/`, tier map at `/syllabus/#tiers`).
- `src/*_page_live.html`: page code of the three claude.ai dashboards (the data is uploaded from the two JSON files above). `src/legacy_*`: earlier scratch builders.

Dashboards: parent map https://claude.ai/artifact/3CjaWn3L94tmTn8tEfaCTc, detailed map https://claude.ai/artifact/EVpMPxfpEEkMDoXSiJP8u8, tier map https://claude.ai/artifact/BGC9aLaVMX4sod2JEMaiiY
