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
    if case in ("owner-gate", "other-action", "failed-gate"):
        result.append(dict(name="ci-action" if case == "other-action" else "Code Review Gate",
                           state="FAILURE" if case == "failed-gate" else "ACTION_REQUIRED", bucket="fail"))
    if case == "owner-gate-rollup":
        result = []
elif args[:2] == ["api", "graphql"]:
    query = next(arg for arg in args if arg.startswith("query="))
    if "query ReviewThreads" in query:
        after = next((arg.removeprefix("after=") for arg in args if arg.startswith("after=")), None)
        nodes = []
        page_info = dict(hasNextPage=False, endCursor=None)
        if case in ("late-thread", "resolved-later", "page-error", "missing-cursor", "repeated-cursor"):
            paginated_query = "after: $after" in query and "pageInfo" in query
            assert after is None or paginated_query, "cursor sent without paginated query"
            start, end = (1, 101) if after is None else (101, 121)
            for i in range(start, end):
                run_id = "run-1" if i <= 100 else "run-3" if i == 120 else "run-2"
                nodes.append(dict(id=f"thread-{i}", isResolved=case == "resolved-later" or i != 110,
                    comments=dict(nodes=[dict(body=f"RUN_ID: {run_id}", createdAt="now", path="a.ts",
                                             line=i, author=dict(login="bugbot"))])))
            if after is None or case == "repeated-cursor":
                page_info = dict(hasNextPage=True, endCursor=None if case == "missing-cursor" else "page-2")
            if after is not None and case == "page-error":
                print("fixture: later page unavailable", file=sys.stderr)
                raise SystemExit(1)
        pr = dict(reviewThreads=dict(nodes=nodes, pageInfo=page_info))
    elif "query PrCommitStatuses" in query:
        pr = dict(commits=dict(nodes=[dict(commit=dict(oid="head", statusCheckRollup=dict(state="FAILURE" if case == "hidden" else "SUCCESS")))]))
    elif "query PrCheckRollup" in query:
        pr = dict(commits=dict(nodes=[dict(commit=dict(statusCheckRollup=None))]))
        if case == "owner-gate-rollup":
            contexts = dict(pageInfo=dict(hasNextPage=False, endCursor=None), nodes=[
                dict(__typename="CheckRun", name="ci", status="COMPLETED", conclusion="SUCCESS"),
                dict(__typename="CheckRun", name="Code Review Gate", status="COMPLETED", conclusion="ACTION_REQUIRED")])
            pr = dict(commits=dict(nodes=[dict(commit=dict(statusCheckRollup=dict(contexts=contexts)))]))
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
        ("late-thread", [], 3, "BLOCKER"),
        ("resolved-later", [], 0, "READY"),
        ("page-error", [], 7, "BLOCKER"),
        ("missing-cursor", [], 7, "BLOCKER"),
        ("repeated-cursor", [], 7, "BLOCKER"),
        ("owner-gate", [], 0, "READY"),
        ("owner-gate-rollup", [], 0, "READY"),
        ("other-action", [], 4, "BLOCKER"),
        ("failed-gate", [], 4, "BLOCKER"),
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
            assert result.returncode == exit_code, (case, result.returncode, result.stderr, result.stdout)
            events = [json.loads(line) for line in result.stdout.splitlines()]
            assert len(events) == 1, (case, events)
            assert events[0]["kind"] == kind, (case, events)
            if case == "pending":
                assert events[0]["terminal"] is False
                assert events[0]["reason"]["kind"] == "pending-checks"
            if case == "late-thread":
                blocker = events[0]["blocker"]
                assert blocker["kind"] == "review-threads", blocker
                assert [(t["id"], t["bugbotReviewPasses"]) for t in blocker["threads"]] == [("thread-110", 3)], blocker
            if case in ("page-error", "missing-cursor", "repeated-cursor"):
                blocker = events[0]["blocker"]
                assert blocker["kind"] == "status-query" and blocker["failures"] == 1, blocker
            if case in ("other-action", "failed-gate"):
                assert events[0]["blocker"]["kind"] == "failing-checks", events
            print(f"PASS {case} {' '.join(extra)}: exit {exit_code}, {kind}")


if __name__ == "__main__":
    main()
