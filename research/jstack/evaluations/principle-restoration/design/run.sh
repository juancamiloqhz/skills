#!/usr/bin/env bash
set -euo pipefail
fixture_dir=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)
run_dir=$(mktemp -d /tmp/jstack-principle-design.XXXXXX)
trap 'rm -rf -- "$run_dir"' EXIT
cp "$fixture_dir"/*.rs "$run_dir/"
cd "$run_dir"
rustc --edition 2021 --crate-type lib tracker.rs
rustc --edition 2021 --test checks.rs --extern tracker=libtracker.rlib -o checks
./checks --test-threads=1
for fixture in invalid_ids invalid_done invalid_head invalid_match; do
  if rustc --edition 2021 "$fixture.rs" --extern tracker=libtracker.rlib -o "$fixture" >"$fixture.log" 2>&1; then
    echo "FAIL: $fixture unexpectedly compiled"
    exit 1
  fi
  case "$fixture" in
    invalid_ids|invalid_head) diagnostic=E0308 ;;
    invalid_done) diagnostic=E0063 ;;
    invalid_match) diagnostic=E0004 ;;
  esac
  rg "$diagnostic" "$fixture.log"
  echo "PASS: $fixture rejected with $diagnostic"
done
