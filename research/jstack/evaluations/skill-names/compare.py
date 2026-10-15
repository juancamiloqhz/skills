#!/usr/bin/env python3
"""Compare the migration with its baseline and every exact pinned upstream file."""

import argparse
import difflib
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess

BASE = "3c2e32c17ea6a08900af822fe205703e47be0072"
ROOT = Path(__file__).resolve().parents[4]
OUT = Path(__file__).resolve().parent


def git(*args, upstream=None):
    command = ["git"] + ([f"--git-dir={upstream}"] if upstream else ["-C", str(ROOT)])
    return subprocess.check_output(command + list(args))


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def diff(before, after, left, right):
    return "".join(difflib.unified_diff(before.decode().splitlines(True),
                                      after.decode().splitlines(True),
                                      fromfile=left, tofile=right))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--upstream", type=Path,
                        default=Path.home() / ".cache/jstack/upstream/upstream.git")
    parser.add_argument("--diff-dir", type=Path, help="Optional directory for full review diffs")
    args = parser.parse_args()
    manifest_path = ROOT / "research/jstack/upstream.json"
    spec = importlib.util.spec_from_file_location("checker", ROOT / "scripts/jstack/check_upstream.py")
    checker = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(checker)
    current, _ = checker.load_manifest(manifest_path, ROOT)
    before = json.loads(git("show", f"{BASE}:research/jstack/upstream.json"))
    assert {k: v for k, v in current.items() if k != "skills"} == {
        k: v for k, v in before.items() if k != "skills"}
    old_by_source = {s["upstreamPath"]: s for s in before["skills"]}
    names = {}
    for skill in current["skills"]:
        old = old_by_source[skill["upstreamPath"]]
        assert {k: v for k, v in skill.items() if k not in ("name", "localPath")} == {
            k: v for k, v in old.items() if k not in ("name", "localPath")}
        expected = "jstack-setup" if old["name"] == "setup-jstack" else "jstack-" + old["name"]
        assert skill["name"] == expected
        names[old["name"]] = expected
    assert len(names) == len(before["skills"]) == 38
    source_diff, migration_diff, residual_diff, packages = [], [], [], []
    for skill in current["skills"]:
        old = old_by_source[skill["upstreamPath"]]
        local = ROOT / skill["localPath"]
        previous = git("ls-tree", "-r", "--name-only", BASE, old["localPath"]).decode().splitlines()
        old_files = {str(Path(p).relative_to(old["localPath"])) for p in previous}
        new_files = {str(p.relative_to(local)) for p in local.rglob("*")
                     if p.is_file() and "__pycache__" not in p.parts}
        assert old_files == new_files, (skill["name"], old_files ^ new_files)
        upstream_paths = git("ls-tree", "-r", "--name-only", skill["adaptedFrom"],
                             skill["upstreamPath"], upstream=args.upstream).decode().splitlines()
        upstream_files = {str(Path(p).relative_to(skill["upstreamPath"])) for p in upstream_paths}
        rows = []
        for rel in sorted(new_files):
            target = local / rel
            raw = target.read_bytes()
            old_path = old["localPath"] + "/" + rel
            previous_raw = git("show", BASE + ":" + old_path)
            migration_diff.append(diff(previous_raw, raw, old_path, str(target.relative_to(ROOT))))
            normalized = raw.decode()
            for old_name, new_name in names.items():
                normalized = normalized.replace(new_name, old_name)
            for token in ("*", "<title>", "NAME"):
                normalized = normalized.replace("jstack-principle-" + token, "principle-" + token)
            residual_diff.append(diff(previous_raw, normalized.encode(), old_path,
                                      str(target.relative_to(ROOT)) + " (names normalized)"))
            row = {"file": rel, "sha256": digest(raw), "previousSha256": digest(previous_raw),
                   "unchangedAfterNameNormalization": normalized.encode() == previous_raw}
            if rel in upstream_files or rel == "LICENSE":
                source_path = "pstack/LICENSE" if rel == "LICENSE" else skill["upstreamPath"] + "/" + rel
                source = git("show", skill["adaptedFrom"] + ":" + source_path, upstream=args.upstream)
                row.update(upstreamPath=source_path, upstreamSha256=digest(source),
                           identicalToUpstream=source == raw)
                source_diff.append(diff(source, raw, skill["adaptedFrom"] + ":" + source_path,
                                        str(target.relative_to(ROOT))))
                if rel == "LICENSE":
                    assert raw == source == previous_raw
            rows.append(row)
        packages.append({"name": skill["name"], "previousName": old["name"],
                         "localPath": skill["localPath"], "upstreamPath": skill["upstreamPath"],
                         "pin": skill["adaptedFrom"], "differences": skill["differences"],
                         "upstreamOnlyFiles": sorted(upstream_files - new_files), "files": rows})
    (OUT / "normalized-residual.json").write_text(
        json.dumps({"diff": "".join(residual_diff)}, indent=2) + "\n")
    if args.diff_dir:
        args.diff_dir.mkdir(parents=True, exist_ok=True)
        (args.diff_dir / "pinned-source.diff").write_text("".join(source_diff))
        (args.diff_dir / "migration.diff").write_text("".join(migration_diff))
    result = {"baseline": BASE, "reviewedThrough": current["reviewedThrough"],
              "upstreamManifestFieldsPreserved": True, "packageFileSetsPreserved": True,
              "allLicensesPreserved": True, "packages": packages}
    (OUT / "comparison.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"packages": len(packages), "files": sum(len(p['files']) for p in packages),
                      "filesWithNonNameDifferences": sum(not f['unchangedAfterNameNormalization']
                                                        for p in packages for f in p['files'])}))


if __name__ == "__main__":
    main()
