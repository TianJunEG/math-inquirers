#!/usr/bin/env bash
# Like run_sql_test.sh but for delivery.sql: schema + policies + delivery.sql (twice, to prove it is idempotent) + test/delivery_test.sql.
set -euo pipefail
HERE="$(cd "$(dirname "$0")/.." && pwd)"
PGBIN="${PGBIN:-$(ls -d /usr/lib/postgresql/*/bin | tail -1)}"
D="$(mktemp -d)"; chmod 755 "$D"; PORT=54331
chown postgres "$D" 2>/dev/null || true
run() { if [ "$(id -u)" = 0 ]; then su postgres -s /bin/bash -c "$*"; else bash -c "$*"; fi; }
run "$PGBIN/initdb -D $D/data -A trust >/dev/null"
run "$PGBIN/pg_ctl -D $D/data -o '-p $PORT -k $D' -l $D/log -w start >/dev/null"
trap 'run "$PGBIN/pg_ctl -D $D/data -m immediate stop >/dev/null" || true; rm -rf "$D"' EXIT
P="$PGBIN/psql -h $D -p $PORT -U postgres -d postgres -v ON_ERROR_STOP=1 -v HERE=$HERE/test -q"
for f in test/stub_supabase.sql schema.sql policies.sql delivery.sql delivery.sql test/delivery_test.sql; do
  chmod -R a+rX "$HERE"; run "$P -f $HERE/$f" || { echo "FAILED in $f"; exit 1; }
done
