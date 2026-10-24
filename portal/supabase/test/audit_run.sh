#!/usr/bin/env bash
# Independent audit harness (round 1). Builds a throwaway local Postgres with the repo's Supabase stand-in, loads the draft SQL in the documented order
# (schema, policies, seed, practice_submissions, portal_ui, recordings, preview_class) and runs every audit_*.sql file (adversarial checks).
# Each check prints "AUDIT|PASS|sev|name" or "AUDIT|FAIL|sev|name" as a NOTICE; this script prints a summary. A FAIL means the attack worked (a finding).
# Local only. Never touches a real Supabase project.
set -uo pipefail
HERE="$(cd "$(dirname "$0")/.." && pwd)"
PGBIN="${PGBIN:-$(ls -d /usr/lib/postgresql/*/bin | tail -1)}"
D="$(mktemp -d)"; chmod 755 "$D"; PORT=54347
chown postgres "$D" 2>/dev/null || true
run() { if [ "$(id -u)" = 0 ]; then su postgres -s /bin/bash -c "$*"; else bash -c "$*"; fi; }
run "$PGBIN/initdb -D $D/data -A trust >/dev/null"
run "$PGBIN/pg_ctl -D $D/data -o '-p $PORT -k $D' -l $D/log -w start >/dev/null"
trap 'run "$PGBIN/pg_ctl -D $D/data -m immediate stop >/dev/null" || true; rm -rf "$D"' EXIT
P="$PGBIN/psql -h $D -p $PORT -U postgres -d postgres -v ON_ERROR_STOP=1 -v HERE=$HERE/test -q"
chmod -R a+rX "$HERE"
for f in test/stub_supabase.sql schema.sql policies.sql seed_groups.sql practice_submissions.sql portal_ui.sql recordings.sql preview_class.sql; do
  run "$P -f $HERE/$f >/dev/null 2>&1" || { echo "SETUP FAILED in $f"; exit 1; }
done
OUT="$(mktemp)"
if [ -n "${AUDIT_ADHOC:-}" ]; then for f in $(ls $HERE/test/audit_0[0-9]*.sql | sort | head -${AUDIT_UPTO:-1}); do run "$P -f $f" >/dev/null 2>&1; done; run "$P -f $AUDIT_ADHOC" 2>&1; exit 0; fi   # debugging: load first N audit files, then run one ad-hoc file
for f in $(ls $HERE/test/audit_[0-9]*.sql | sort); do
  echo "== $(basename $f)"
  run "$P -f $f" >> "$OUT" 2>&1 || { echo "SCRIPT ERROR in $f"; tail -5 "$OUT"; }
done
grep -h "AUDIT|" "$OUT" | sed 's/^.*AUDIT|/AUDIT|/' | sort -t'|' -k2,2 -k3,3 > "$OUT.sum"
echo; echo "---- FAIL (attack worked or rule missing) ----"; grep "AUDIT|FAIL" "$OUT.sum" || echo none
echo; echo "PASS: $(grep -c 'AUDIT|PASS' "$OUT.sum")   FAIL: $(grep -c 'AUDIT|FAIL' "$OUT.sum")"
grep -h "ERROR\|SCRIPT" "$OUT" | head -5
[ -n "${AUDIT_FULL:-}" ] && cat "$OUT.sum"
rm -f "$OUT" "$OUT.sum"
