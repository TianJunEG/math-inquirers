#!/usr/bin/env bash
# Upload the PDFs listed in portal/data/delivery_manifest.json to the PRIVATE R2 bucket with wrangler.
#   bash portal/tools/upload_files.sh --dry-run          # show what would be uploaded, upload nothing
#   bash portal/tools/upload_files.sh                    # check the manifest, then upload every entry whose source file exists
#   bash portal/tools/upload_files.sh --only beta-workbook-l1:pdf
# Needs: node/npx (wrangler), python3, and a one-time "npx wrangler login" on the machine you run it from. No secret is read or written here.
# The bucket is never made public. Keys are versioned (files/<product>/v1/<name>); do not overwrite a published key, bump the version instead.
set -euo pipefail
HERE="$(cd "$(dirname "$0")/../.." && pwd)"
DRY=0; ONLY=""
while [ $# -gt 0 ]; do case "$1" in --dry-run) DRY=1;; --only) ONLY="${2:?--only needs product:format}"; shift;; *) echo "unknown option $1"; exit 2;; esac; shift; done
python3 "$HERE/portal/tools/delivery_manifest.py" check || { echo "Manifest does not match the files. Fix it first (see the messages above)."; exit 1; }
BUCKET="$(python3 -c "import json,sys;print(json.load(open('$HERE/portal/data/delivery_manifest.json'))['bucket'])")"
python3 "$HERE/portal/tools/delivery_manifest.py" list-upload | while IFS=$'\t' read -r KEY SRC SHA; do
  if [ -n "$ONLY" ]; then
    ID="$(python3 -c "import json;m=json.load(open('$HERE/portal/data/delivery_manifest.json'))['files'];print(next((k for k,v in m.items() if v['r2_key']=='$KEY'),''))")"
    [ "$ID" = "$ONLY" ] || continue
  fi
  if [ "$DRY" = 1 ]; then echo "would upload $SRC -> r2://$BUCKET/$KEY (sha256 $SHA)"; continue; fi
  echo "uploading $SRC -> r2://$BUCKET/$KEY"
  npx --yes wrangler r2 object put "$BUCKET/$KEY" --file "$HERE/$SRC" --content-type application/pdf --remote
done
echo "done. Verify with the test download in docs/shop/delivery_setup.md (step: test)."
