#!/bin/sh
# Full gate for one level (default 1): answers, duplicates, wording, build, black-and-white, page fill.  Stops at the first failure.
L=${1:-1}
cd "$(dirname "$0")/.." || exit 1
set -e
python3 extension/verify/run_checks.py --level "$L"
python3 extension/verify/dup_check.py --level "$L"
python3 extension/verify/wording_lint.py --level "$L"
python3 extension/tools/build.py --level "$L"
python3 extension/verify/bw_check.py
python3 print/check_bw.py outputs/extension/L$L/Math_Inquirers_L${L}_Extension_Workbook_Print_BW.pdf
python3 extension/verify/fill_check.py --level "$L"
echo "ALL GATES PASSED for level $L"
