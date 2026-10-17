import json
import os
from pathlib import Path
import subprocess
import tempfile


REPO = Path(__file__).resolve().parents[4]
WATCHER = REPO / "skills/jstack/jstack-juan-mode/scripts/watch-pr/watch-pr"
GH = '''#!/usr/bin/env python3
import json, os, sys
case = os.environ["JSTACK_FIXTURE_CASE"]
args = sys.argv[1:]
if args[:2] == ["pr", "view"]:
    result = dict(mergeable="CONFLICTING" if case == "conflict" else "MERGEABLE",
                  mergeStateStatus="BLOCKED" if case == "hidden" else "CLEAN",
                  reviewDecision="", headRefOid="head", headRefName="feature",
                  baseRefName="main", state="OPEN", mergedAt=None, isDraft=False)
elif args[:2] == ["pr", "checks"]:
    result = [] if case == "empty" else [dict(name="ci", state="PENDING" if case == "pending" else "SUCCESS",
                  bucket="pending" if case == "pending" else "pass", description="", link="", workflow="")]
elif args[:2] == ["api", "graphql"]:
    query = next(arg for arg in args if arg.startswith("query="))
    if "query ReviewThreads" in query:
        pr = dict(reviewThreads=dict(nodes=[]))
    elif "query PrCommitStatuses" in query:
        pr = dict(commits=dict(nodes=[dict(commit=dict(oid="head", statusCheckRollup=dict(state="FAILURE" if case == "hidden" else "SUCCESS")))]))
    elif "query PrCheckRollup" in query:
        pr = dict(commits=dict(nodes=[dict(commit=dict(statusCheckRollup=None))]))
    else:
        raise SystemExit("unexpected GraphQL query")
    result = dict(data=dict(repository=dict(pullRequest=pr)))
else:
    raise SystemExit("unexpected gh operation: " + repr(args))
print(json.dumps(result))
'''


def main():
    cases = [
        ("pending", [], 0, "WAITING"),
        ("conflict", [], 2, "BLOCKER"),
        ("hidden", [], 4, "BLOCKER"),
        ("empty", [], 7, "BLOCKER"),
        ("conflict", ["--status-only"], 0, "STATUS"),
    ]
    with tempfile.TemporaryDirectory(prefix="jstack-babysit-cli-") as directory:
        gh = Path(directory) / "gh"
        gh.write_text(GH)
        gh.chmod(0o755)
        for case, extra, exit_code, kind in cases:
            env = dict(os.environ, PATH=directory + os.pathsep + os.environ["PATH"], JSTACK_FIXTURE_CASE=case)
            result = subprocess.run(
                [str(WATCHER), "--owner", "fixture", "--repo", "repo", "--pr", "1", *extra],
                env=env, capture_output=True, text=True, timeout=5, check=False,
            )
            assert result.returncode == exit_code, (case, result.returncode, result.stderr)
            events = [json.loads(line) for line in result.stdout.splitlines()]
            assert len(events) == 1, (case, events)
            assert events[0]["kind"] == kind, (case, events)
            if case == "pending":
                assert events[0]["terminal"] is False
                assert events[0]["reason"]["kind"] == "pending-checks"
            print(f"PASS {case} {' '.join(extra)}: exit {exit_code}, {kind}")


if __name__ == "__main__":
    main()
