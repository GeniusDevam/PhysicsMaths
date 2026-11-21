#!/usr/bin/env bash
# Checks that the repo is self-consistent. Needs Python 3 and Node.js. Run from anywhere:
#   ./scripts/verify.sh
set -euo pipefail
cd "$(dirname "$0")/.."
TRK=skills/syllabus-deadline-tracker
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT
fail=0

echo "== 1. Build the small example config"
python3 "$TRK/scripts/build_app.py" "$TRK/examples/example-config.json" -o "$TMP/example.html"

echo; echo "== 2. Smoke-test FrontierPath and the example app (renders each screen against a stub DOM)"
for f in apps/frontierpath/index.html "$TMP/example.html"; do
  echo "-- $f"
  node "$TRK/scripts/smoke_test.js" "$f" || fail=1
done

echo; echo "== 3. The FrontierPath copy inside the coach skill matches the app"
cmp -s apps/frontierpath/index.html skills/physics-maths-mastery/assets/frontierpath.html \
  && echo "OK: identical" || { echo "MISMATCH"; fail=1; }

echo; echo "== 4. The packaged .skill files in dist/ match the skill folders"
python3 -I - <<'PY' || fail=1
import zipfile, pathlib, sys
bad = 0
for z in sorted(pathlib.Path('dist').glob('*.skill')):
    name = z.stem
    zf = zipfile.ZipFile(z)
    root = pathlib.Path('skills') / name
    for member in zf.namelist():
        if member.endswith('/'):
            continue
        rel = member.split('/', 1)[1]
        src = root / rel
        if not src.is_file() or src.read_bytes() != zf.read(member):
            print('MISMATCH:', z.name, member); bad = 1
    files = {str(p.relative_to(root)) for p in root.rglob('*') if p.is_file() and '__pycache__' not in p.parts}
    packed = {m.split('/', 1)[1] for m in zf.namelist() if not m.endswith('/')}
    if files != packed:
        print('FILE LIST DIFFERS:', z.name, sorted(files ^ packed)); bad = 1
    if not bad:
        print('OK:', z.name)
sys.exit(bad)
PY

echo
if [ "$fail" -eq 0 ]; then echo "All checks passed."; else echo "Some checks failed."; exit 1; fi
