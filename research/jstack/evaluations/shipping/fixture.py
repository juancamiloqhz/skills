import json
from pathlib import Path
import subprocess
import sys


def git(root, *args):
    return subprocess.check_output(["git", "-C", str(root), *args], text=True).strip()


def patch_id(root, base, head):
    patch = subprocess.check_output(["git", "-C", str(root), "diff", base, head])
    result = subprocess.check_output(["git", "patch-id", "--stable"], input=patch).decode().split()
    if not result:
        raise ValueError("empty patch")
    return result[0]


def create(root):
    root.mkdir(parents=True, exist_ok=False)
    git(root, "init", "-b", "main")
    git(root, "config", "user.name", "Shipping Fixture")
    git(root, "config", "user.email", "fixture@example.invalid")
    source = 'import argparse\np = argparse.ArgumentParser()\np.add_argument("mode", choices=["double"])\np.add_argument("value", type=int)\na = p.parse_args()\nprint(a.value * 2)\n'
    app = root / "math_cli.py"
    app.write_text(source)
    git(root, "add", "math_cli.py")
    git(root, "commit", "-m", "test: seed CLI")
    trunk = git(root, "rev-parse", "HEAD")
    layers = []
    for number, mode, expression in [(101, "triple", "a.value * 3"), (102, "square", "a.value * 2"), (103, "negate", "-a.value")]:
        base = git(root, "rev-parse", "HEAD")
        git(root, "switch", "-c", f"layer-{number}")
        source = source.replace('choices=[', f'choices=["{mode}", ')
        source = source.replace("\nprint(a.value * 2)\n", f'\nif a.mode == "{mode}":\n    print({expression})\n    raise SystemExit(0)\nprint(a.value * 2)\n')
        app.write_text(source)
        git(root, "add", "math_cli.py")
        git(root, "commit", "-m", f"feat: add {mode}")
        head = git(root, "rev-parse", "HEAD")
        layers.append(dict(number=number, mode=mode, base=base, head=head, patchId=patch_id(root, base, head)))
    git(root, "switch", "main")
    return dict(repository=str(root), trunk=trunk, layers=layers)


def identity_checks(root, manifest):
    first = manifest["layers"][0]
    (root / "README.md").write_text("Fixture trunk documentation.\n")
    git(root, "add", "README.md")
    git(root, "commit", "-m", "docs: advance trunk")
    trunk = git(root, "rev-parse", "HEAD")
    git(root, "switch", "-c", "rebased-first", first["head"])
    git(root, "rebase", "--onto", trunk, first["base"])
    head = git(root, "rev-parse", "HEAD")
    assert head != first["head"]
    assert patch_id(root, trunk, head) == first["patchId"]
    (root / "math_cli.py").write_text((root / "math_cli.py").read_text().replace("a.value * 3", "a.value * 4"))
    git(root, "add", "math_cli.py")
    git(root, "commit", "-m", "feat: add triple")
    changed = git(root, "rev-parse", "HEAD")
    assert patch_id(root, trunk, changed) != first["patchId"]
    assert patch_id(root, manifest["trunk"], head) != first["patchId"]
    try:
        patch_id(root, trunk, trunk)
    except ValueError:
        pass
    else:
        raise AssertionError("empty diff unexpectedly produced a patch ID")
    git(root, "switch", "main")
    git(root, "merge", "--squash", first["head"])
    git(root, "commit", "-m", "feat: land first layer")
    merged = git(root, "rev-parse", "HEAD")
    git(root, "merge-base", "--is-ancestor", merged, "main")
    assert "square" not in (root / "math_cli.py").read_text()
    assert "negate" not in (root / "math_cli.py").read_text()
    print("PASS: same patch after rebase; changed code and base invalidate; empty diff rejected; only first layer squash-landed locally")


if __name__ == "__main__":
    root = Path(sys.argv[1]).resolve()
    manifest = create(root)
    (root.parent / (root.name + ".json")).write_text(json.dumps(manifest, indent=2) + "\n")
    if "--check-identities" in sys.argv[2:]:
        identity_checks(root, manifest)
    print(json.dumps(manifest))
