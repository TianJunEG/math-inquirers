#!/usr/bin/env bash
# Runs schema.sql + policies.sql + seed + rls_test.sql in a throwaway local Postgres (needs postgresql-16 server binaries).
set -euo pipefail
HERE="$(cd "$(dirname "$0")/.." && pwd)"
PGBIN="${PGBIN:-$(ls -d /usr/lib/postgresql/*/bin | tail -1)}"
D="$(mktemp -d)"; chmod 755 "$D"; PORT=54329
chown postgres "$D" 2>/dev/null || true
run() { if [ "$(id -u)" = 0 ]; then su postgres -s /bin/bash -c "$*"; else bash -c "$*"; fi; }
run "$PGBIN/initdb -D $D/data -A trust >/dev/null"
run "$PGBIN/pg_ctl -D $D/data -o '-p $PORT -k $D' -l $D/log -w start >/dev/null"
trap 'run "$PGBIN/pg_ctl -D $D/data -m immediate stop >/dev/null" || true; rm -rf "$D"' EXIT
P="$PGBIN/psql -h $D -p $PORT -U postgres -d postgres -v ON_ERROR_STOP=1 -v HERE=$HERE/test -q"
for f in test/stub_supabase.sql schema.sql policies.sql seed_groups.sql test/rls_test.sql test/interest_test.sql; do
  chmod -R a+rX "$HERE"; run "$P -f $HERE/$f" || { echo "FAILED in $f"; exit 1; }
done
