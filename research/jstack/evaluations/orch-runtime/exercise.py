"""Exercise the real orch CLI across process boundaries in disposable stores."""
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import time


DEFAULT = Path(__file__).resolve().parents[4] / "skills/jstack/jstack-juan-mode/scripts/orch/orch.ts"
CLI = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else DEFAULT
BUN = shutil.which("bun")
assert BUN, "Bun must already be available"


def run(store, *args, code=0, cli=CLI):
    result = subprocess.run(
        [BUN, str(cli), "--store", str(store), "--json", *args],
        capture_output=True, text=True, timeout=10,
    )
    assert result.returncode == code, (args, result.returncode, result.stderr)
    return json.loads(result.stdout) if result.stdout else result.stderr


with tempfile.TemporaryDirectory(prefix="jstack-orch-exercise-") as directory:
    root = Path(directory)
    store = root / "store"
    run(store, "init")
    run(store, "standing", "add", "Leave PRs open for operator review.")
    for unit in ["api", "ui", "tests"]:
        run(store, "unit", "add", unit, "--track", "pagination")
    run(store, "unit", "set", "api", "--state", "needs-verify", "--pr", "201", "--sha", "a" * 40)
    before = (store / "units.tsv").read_bytes()
    run(store, "init")
    assert (store / "units.tsv").read_bytes() == before
    assert len(run(store, "unit", "list")) == 3
    assert run(store, "standing", "show")[0]["line"] == "Leave PRs open for operator review."
    print("PASS: independent CLI processes preserve units and standing orders across init")

    run(store, "ledger", "record", "201", "a" * 40, "unit-test-verified", "--evidence", "reports/api.md", "--verifier", "reviewer")
    assert run(store, "ledger", "check", "201", "a" * 40)["verdict"] == "unit-test-verified"
    assert run(store, "ledger", "check", "201", "b" * 40, code=2)["verdict"] == "NOT-VERIFIED"
    run(store, "ledger", "record", "201", "b" * 40, "verifier-blocked", "--evidence", "reports/blocked.md")
    assert run(store, "ledger", "check", "201", "b" * 40)["verdict"] == "verifier-blocked"
    print("PASS: a new SHA lacks a verdict; exit-zero lookup can still return blocked")

    for _ in range(2):
        run(store, "inbox", "push", "task-1", "api", "completed", "--report", "reports/api.md")
    assert run(store, "inbox", "count")["count"] == 2
    assert len(run(store, "inbox", "drain", "--peek")) == 2
    assert run(store, "inbox", "count")["count"] == 2
    assert len(run(store, "inbox", "drain")) == 2
    assert run(store, "inbox", "drain") == []
    assert run(store, "unit", "get", "api")["state"] == "needs-verify"
    print("PASS: duplicate completion pointers remain distinct; draining does not finish a unit")

    run(store, "gate", "park", "landing", "--question", "Land the stack?", "--options", "land,hold", "--default", "hold")
    report = run(store, "status")
    assert report["summary"]["openGateIds"] == ["landing"]
    assert report["summary"]["unitStates"] == {"needs-verify": 1, "pending": 2}
    assert len(run(store, "gate", "list")) == 1
    assert "landing" in (store / "status.md").read_text()
    print("PASS: status derives counts and leaves the decision gate open")

    holder_script = root / "holder.ts"
    holder_script.write_text(
        f'import {{ openStore }} from {json.dumps(str(CLI.with_name("store.ts")))};\n'
        'const store = openStore(process.argv[2]);\n'
        'await store.standing.add({line: "Holder started"});\n'
        'console.log("LOCKED");\n'
        'setInterval(() => {}, 1000);\n'
    )
    ready = root / "holder.out"
    with ready.open("w") as output:
        holder = subprocess.Popen([BUN, str(holder_script), str(store)], stdout=output, stderr=subprocess.PIPE)
        try:
            for _ in range(100):
                if "LOCKED" in ready.read_text():
                    break
                assert holder.poll() is None, "holder failed before acquiring its lock"
                time.sleep(0.02)
            else:
                raise AssertionError("holder did not acquire its lock")
            before = (store / "units.tsv").read_bytes()
            error = run(store, "unit", "add", "blocked", "--track", "pagination", code=1)
            assert "store lock held by pid" in error
            assert (store / "units.tsv").read_bytes() == before
        finally:
            holder.kill()
            holder.wait(timeout=5)
            holder.stderr.close()
    run(store, "unit", "add", "recovered", "--track", "pagination")
    assert len(run(store, "unit", "list")) == 4
    assert not (store / ".orch.lock").exists()
    print("PASS: a live writer blocks mutation; a killed owned process leaves a recoverable lock")

    isolated = root / "missing-dependency"
    (isolated / "orch").mkdir(parents=True)
    for filename in ["orch.ts", "store.ts"]:
        shutil.copyfile(CLI.with_name(filename), isolated / "orch" / filename)
    for filename in ["bootstrap.ts", "package.json"]:
        shutil.copyfile(CLI.parent.parent / filename, isolated / filename)
    absent_store = root / "must-not-exist"
    for version in [None, "0.0.0"]:
        if version is not None:
            dependency = isolated / "node_modules/commander"
            dependency.mkdir(parents=True)
            (dependency / "package.json").write_text(json.dumps({"version": version}))
        before = {str(p.relative_to(isolated)): p.read_bytes() for p in isolated.rglob("*") if p.is_file()}
        error = run(absent_store, "init", code=1, cli=isolated / "orch/orch.ts")
        after = {str(p.relative_to(isolated)): p.read_bytes() for p in isolated.rglob("*") if p.is_file()}
        assert after == before
        assert "nothing was installed" in error
        assert not absent_store.exists()
        if version is None:
            assert not (isolated / "node_modules").exists()
    print("PASS: absent and mismatched dependencies fail before store writes or installation")
