#!/bin/bash
# Build one lesson: bash term/l1/build.sh 01      (validates first; outputs in term/l1/out/l01/)
set -e
N=${1:-01}
cd "$(dirname "$0")/../.."
python3 term/l1/tools/validate.py "$N" --no-built | tail -25
python3 term/l1/tools/build.py "$N"
