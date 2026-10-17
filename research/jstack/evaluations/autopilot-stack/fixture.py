"""Generate three local PR branches and a simulated forge for stack exercises."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys


def git(repo, *args, data=None):
    return subprocess.check_output(["git", "-C", str(repo), *args], input=data, text=True).strip()


FORGE = '''import json
from pathlib import Path
import subprocess
import sys

root = Path(__file__).resolve().parent
packet = json.loads((root / "packet.json").read_text())
state_path = root / "state.json"
state = json.loads(state_path.read_text())

def git(repo, *args):
    return subprocess.check_output(["git", "-C", str(repo), *args], text=True).strip()

def tip(branch):
    return git(root / "origin.git", "rev-parse", "refs/heads/" + branch)

def record(event):
    with (root / "actions.jsonl").open("a") as f:
        f.write(json.dumps(event) + "\\n")

cmd = sys.argv[1]
if cmd == "view":
    print(json.dumps({n: dict(p, head=tip(p["branch"]), baseHead=tip(p["base"])) for n, p in state["prs"].items()}, indent=2))
elif cmd == "retarget":
    number, parent = sys.argv[2:4]
    tip(parent)
    state["prs"][number]["base"] = parent
    state_path.write_text(json.dumps(state, indent=2) + "\\n")
    record(dict(action="retarget", pr=number, base=parent))
elif cmd == "proof":
    number = sys.argv[2]
    item = state["prs"][number]
    head = tip(item["branch"])
    code = git(root / "origin.git", "show", head + ":" + packet["prs"][number]["file"])
    run = subprocess.run([sys.executable, "-c", code, "3"], capture_output=True, text=True, timeout=5)
    print(json.dumps(dict(head=head, observed=run.stdout.strip(), expected="9", complete=run.returncode == 0 and run.stdout.strip() == "9", artifactExit=run.returncode, ciKind="simulated current-head gate using a real local CLI")))
elif cmd == "drift":
    assert not state["driftInjected"]
    actor = root / "actor"
    subprocess.check_call(["git", "clone", str(root / "origin.git"), str(actor)], stdout=subprocess.DEVNULL)
    git(actor, "config", "user.name", "Stack Fixture")
    git(actor, "config", "user.email", "fixture@example.invalid")
    (actor / "README.md").write_text("Trunk documentation drift.\\n")
    git(actor, "commit", "-am", "fixture: trunk documentation drift")
    git(actor, "push", "origin", "main")
    git(actor, "switch", "--track", "origin/pr-202")
    path = actor / packet["prs"]["202"]["file"]
    path.write_text(path.read_text().replace("* 3", "* 4"))
    git(actor, "commit", "-am", "fixture: later owner patch")
    git(actor, "push", "origin", "pr-202")
    state["driftInjected"] = True
    state_path.write_text(json.dumps(state, indent=2) + "\\n")
    event = dict(action="drift", trunk=tip("main"), changedHead=tip("pr-202"))
    record(event)
    print(json.dumps(event))
else:
    raise SystemExit("Use view, retarget NUMBER PARENT, proof NUMBER, or drift")
'''


def create(root):
    root.mkdir(parents=True, exist_ok=False)
    repo = root / "repo"
    repo.mkdir()
    git(repo, "init", "-b", "main")
    git(repo, "config", "user.name", "Stack Fixture")
    git(repo, "config", "user.email", "fixture@example.invalid")
    app = 'import sys\nprint(int(sys.argv[1]) * 2)\n'
    files = {"201": "search.py", "202": "invoice.py", "203": "export.py"}
    for name in files.values():
        (repo / name).write_text(app)
    (repo / "README.md").write_text("Initial fixture documentation.\n")
    git(repo, "add", ".")
    git(repo, "commit", "-m", "fixture: baseline")
    base = git(repo, "rev-parse", "HEAD")
    git(repo, "init", "--bare", "--initial-branch=main", str(root / "origin.git"))
    git(repo, "remote", "add", "origin", str(root / "origin.git"))
    git(repo, "push", "-u", "origin", "main")
    prs = {}
    for n, name in files.items():
        branch = "pr-" + n
        git(repo, "switch", "-c", branch, base)
        (repo / name).write_text(app.replace("* 2", "* 3"))
        git(repo, "commit", "-am", "fixture: triple " + name)
        head = git(repo, "rev-parse", "HEAD")
        patch = git(repo, "patch-id", "--stable", data=git(repo, "diff", base, head)).split()[0]
        git(repo, "push", "-u", "origin", branch)
        prs[n] = dict(branch=branch, file=name, verdict=dict(base=base, head=head, patchId=patch, lanes=[dict(lane=l, status="PASS", head=head) for l in ["gates", "live", "audit-consumers", "audit-data", "regression"]]))
    git(repo, "switch", "main")
    packet = dict(kind="Simulated forge/lane receipts; Git, local remote pushes and CLI checks are real.", order=["201", "202", "203"], initialTrunk=base, prs=prs, ownersQuiescent=True, recurringRequest=False)
    (root / "packet.json").write_text(json.dumps(packet, indent=2) + "\n")
    (root / "state.json").write_text(json.dumps(dict(driftInjected=False, prs={n: dict(branch=i["branch"], base="main", state="OPEN", autoMerge=False) for n, i in prs.items()}), indent=2) + "\n")
    (root / "forge.py").write_text(FORGE)
    (root / "before.json").write_text(json.dumps(dict(protected={n: hashlib.sha256((root / n).read_bytes()).hexdigest() for n in ["forge.py", "packet.json"]}), indent=2) + "\n")
    print(root)


if __name__ == "__main__":
    create(Path(sys.argv[1]).resolve())
