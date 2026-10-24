#!/usr/bin/env bash
# Like run_sql_test.sh but for preview_class.sql (DRAFT): schema + policies + preview_class.sql (twice, to prove it is idempotent) + test/preview_test.sql.
# Local throwaway PostgreSQL only. Never touches a real Supabase project.
set -euo pipefail
HERE="$(cd "$(dirname "$0")/.." && pwd)"
PGBIN="${PGBIN:-$(ls -d /usr/lib/postgresql/*/bin | tail -1)}"
D="$(mktemp -d)"; chmod 755 "$D"; PORT=54333
chown postgres "$D" 2>/dev/null || true
run() { if [ "$(id -u)" = 0 ]; then su postgres -s /bin/bash -c "$*"; else bash -c "$*"; fi; }
run "$PGBIN/initdb -D $D/data -A trust >/dev/null"
run "$PGBIN/pg_ctl -D $D/data -o '-p $PORT -k $D' -l $D/log -w start >/dev/null"
trap 'run "$PGBIN/pg_ctl -D $D/data -m immediate stop >/dev/null" || true; rm -rf "$D"' EXIT
P="$PGBIN/psql -h $D -p $PORT -U postgres -d postgres -v ON_ERROR_STOP=1 -v HERE=$HERE/test -q"
for f in test/stub_supabase.sql schema.sql policies.sql preview_class.sql preview_class.sql test/preview_test.sql; do
  chmod -R a+rX "$HERE"; run "$P -f $HERE/$f" || { echo "FAILED in $f"; exit 1; }
done
echo "preview_class test: ALL OK"
