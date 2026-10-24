#!/bin/bash
# Rebuild the skill-gap slides of one level (1, 2 or 3): items -> checks -> slides -> restyle (twice; second must be 0) -> tutor data.
#   bash rebuild/skill_pipeline.sh 1
set -e
N=$1; cd "$(dirname "$0")/.."
python3 rebuild/skill_items_check.py
python3 rebuild/skill_items_dupcheck.py | grep -v "^WARN\|^REVIEW"
python3 rebuild/gen_skill_slides.py $N
if [ "$N" = "1" ]; then D=$(for i in 1 2 3 4 5 6 7 8 9 10; do echo split/l$i; done); else D=$(for i in 1 2 3 4 5 6 7 8 9 10; do echo split/p${N}l$i; done); fi
python3 levels/restyle.py $D | tr '\n' ' '; echo
python3 levels/restyle.py $D | tr '\n' ' '; echo "(second run: all 0 expected)"
python3 tutor/build_data.py $N
