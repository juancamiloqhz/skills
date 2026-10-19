"""Exercise detection against disposable Git repositories, with no network."""

import fcntl
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


CHECKER = Path(__file__).with_name("check_upstream.py")


def git(root, *args):
    return subprocess.check_output(
        ["git", "-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid",
         "-C", str(root), *args], stderr=subprocess.DEVNULL,
    ).decode().strip()


def write(root, name, text):
    path = root / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)


def commit(root):
    git(root, "add", ".")
    git(root, "commit", "-qm", "Fixture change")
    return git(root, "rev-parse", "HEAD")


class UpstreamCheckTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.directory = Path(self.temp.name)
        self.upstream = self.directory / "upstream"
        self.root = self.directory / "jstack"
        self.cache = self.directory / "cache"
        for root in (self.upstream, self.root):
            root.mkdir()
            git(root, "init", "-b", "main")
        write(self.upstream, "pstack/skills/example/SKILL.md", "# Original\n")
        write(self.upstream, "pstack/skills/example/references/helper.md", "Original helper\n")
        write(self.upstream, "pstack/skills/context/SKILL.md", "Original context\n")
        write(self.upstream, "pstack/LICENSE", "License\n")
        self.base = commit(self.upstream)
        write(self.root, "skills/jstack/example/SKILL.md", "# Adaptation\n")
        write(self.root, "skills/jstack/example/references/upstream.md", "Intentional differences\n")
        self.local_commit = commit(self.root)
        git(self.root, "update-ref", "refs/remotes/origin/main", self.local_commit)
        self.manifest = self.root / "research/jstack/upstream.json"
        self.data = {
            "schemaVersion": 1, "repository": str(self.upstream), "branch": "main",
            "initialRevision": self.base, "reviewedThrough": None,
            "watchPaths": ["pstack", ".cursor-plugin/marketplace.json"],
            "skills": [{"name": "example", "localPath": "skills/jstack/example",
                        "upstreamPath": "pstack/skills/example", "adaptedFrom": self.base,
                        "contextPaths": ["pstack/skills/context"],
                        "differences": "skills/jstack/example/references/upstream.md"}],
            "decisions": [],
        }
        self.save_manifest()

    def save_manifest(self):
        write(self.root, "research/jstack/upstream.json", json.dumps(self.data))

    def run_check(self, *args, code=0):
        result = subprocess.run(
            [sys.executable, str(CHECKER), "--repo-root", str(self.root),
             "--cache-dir", str(self.cache), *args], capture_output=True, text=True,
        )
        self.assertEqual(result.returncode, code, result.stdout + result.stderr)
        return json.loads(result.stdout)

    def add_pack(self):
        write(self.upstream, "pstack/automations/benny/FOR_AGENTS.md", "Original pack\n")
        write(self.root, "automations/jstack/benny/FOR_AGENTS.md", "Adapted pack\n")
        write(self.root, "research/jstack/adaptations/benny.md", "Differences\n")
        self.data["automationPacks"] = [{
            "name": "benny", "localPath": "automations/jstack/benny",
            "upstreamPath": "pstack/automations/benny", "adaptedFrom": self.base,
            "contextPaths": ["pstack/LICENSE"], "differences": "research/jstack/adaptations/benny.md"}]
        self.save_manifest()
        commit(self.root)

    def test_automation_pack_maps_changes_and_license_without_catalog_skill(self):
        self.add_pack()
        write(self.upstream, "pstack/LICENSE", "Changed license\n")
        commit(self.upstream)
        receipt = self.run_check()
        self.assertEqual(receipt["directAutomationPacks"], ["benny"])
        report = json.loads(Path(receipt["report"]).read_text())
        changes = {c["path"]: c for c in report["changes"]}
        pack = changes["pstack/automations/benny/FOR_AGENTS.md"]
        self.assertEqual(pack["directAutomationPacks"], ["benny"])
        self.assertEqual(pack["directSkills"], [])
        self.assertEqual(changes["pstack/LICENSE"]["contextAutomationPacks"], ["benny"])

    def test_removed_automation_source_is_reported(self):
        self.add_pack()
        baseline = commit(self.upstream)
        self.data["reviewedThrough"] = baseline
        self.save_manifest()
        git(self.upstream, "rm", "pstack/automations/benny/FOR_AGENTS.md")
        commit(self.upstream)
        receipt = self.run_check()
        self.assertEqual(receipt["missingSources"], ["pstack/automations/benny"])
        self.assertEqual(receipt["directAutomationPacks"], ["benny"])

    def test_dirty_automation_pack_rejects_detection(self):
        self.add_pack()
        commit(self.upstream)
        write(self.root, "automations/jstack/benny/FOR_AGENTS.md", "Pending work\n")
        receipt = self.run_check(code=2)
        self.assertIn("commit or isolate", receipt["error"])

    def test_automation_mapping_requires_local_attribution(self):
        self.add_pack()
        (self.root / "research/jstack/adaptations/benny.md").unlink()
        receipt = self.run_check(code=2)
        self.assertIn("attribution", receipt["error"])

    def test_maps_supporting_context_new_and_shared_files(self):
        write(self.upstream, "pstack/skills/example/references/helper.md", "Fixed helper\n")
        write(self.upstream, "pstack/skills/context/SKILL.md", "Changed context\n")
        write(self.upstream, "pstack/skills/new/SKILL.md", "New skill\n")
        write(self.upstream, ".cursor-plugin/marketplace.json", "{}\n")
        write(self.upstream, "other-plugin/SKILL.md", "Unrelated\n")
        head = commit(self.upstream)
        original = self.manifest.read_bytes()
        receipt = self.run_check()
        report = json.loads(Path(receipt["report"]).read_text())
        self.assertEqual(receipt["head"], head)
        self.assertEqual(receipt["changedFiles"], 4)
        changes = {c["path"]: c for c in report["changes"]}
        self.assertEqual(changes["pstack/skills/example/references/helper.md"]["directSkills"], ["example"])
        self.assertEqual(changes["pstack/skills/context/SKILL.md"]["contextSkills"], ["example"])
        self.assertEqual(changes["pstack/skills/new/SKILL.md"]["directSkills"], [])
        self.assertIn("Fixed helper", Path(receipt["patch"]).read_text())
        self.assertEqual(report["reviewStatus"], "not_reviewed")
        self.assertEqual(self.manifest.read_bytes(), original)

    def test_no_change_reuses_report_and_keeps_deferred_decisions(self):
        write(self.root, "research/jstack/review.md", "Deferred until requested\n")
        self.data["reviewedThrough"] = self.base
        self.data["decisions"] = [{"id": "future", "disposition": "defer", "from": self.base,
                                   "to": self.base, "paths": ["pstack/skills/context"],
                                   "reason": "Future workflow", "report": "research/jstack/review.md"}]
        self.save_manifest()
        first = self.run_check()
        content = Path(first["report"]).read_bytes()
        second = self.run_check()
        self.assertEqual(first["status"], "no_changes")
        self.assertEqual(second["pendingDecisions"], 1)
        self.assertEqual(first["reportId"], second["reportId"])
        self.assertTrue(second["reused"])
        self.assertEqual(Path(second["report"]).read_bytes(), content)
        self.assertEqual(len(list((self.cache / "reports").glob("*.json"))), 1)

    def test_detects_rename_outside_scope_and_missing_source(self):
        git(self.upstream, "mv", "pstack/skills/example", "moved-example")
        commit(self.upstream)
        receipt = self.run_check()
        report = json.loads(Path(receipt["report"]).read_text())
        self.assertEqual(receipt["status"], "changes")
        self.assertEqual(receipt["missingSources"], ["pstack/skills/example"])
        self.assertTrue(all(c["status"].startswith("R") for c in report["changes"]))
        self.assertTrue(all(c["directSkills"] == ["example"] for c in report["changes"]))
        self.assertIn("rename to moved-example", Path(receipt["patch"]).read_text())

    def test_unrelated_changes_do_not_create_drift(self):
        write(self.upstream, "unrelated/SKILL.md", "Other plugin\n")
        commit(self.upstream)
        self.assertEqual(self.run_check()["status"], "no_changes")

    def test_repository_watch_list_detects_each_external_pstack_path(self):
        manifest = CHECKER.parents[2] / "research/jstack/upstream.json"
        self.data["watchPaths"] = json.loads(manifest.read_text())["watchPaths"]
        self.save_manifest()
        original = self.manifest.read_bytes()
        paths = [
            "harness/pstack/claude-code/skills/poteto-mode/SKILL.md",
            ".claude-plugin/marketplace.json",
            "scripts/generate-pstack-harness-trees.mjs",
            "scripts/check-pstack-docs.mjs",
        ]
        for path in paths:
            with self.subTest(path=path):
                base = git(self.upstream, "rev-parse", "HEAD")
                write(self.upstream, path, "External pstack change\n")
                head = commit(self.upstream)
                receipt = self.run_check("--base", base, "--head", head)
                self.assertEqual(receipt["status"], "changes")
                self.assertEqual(receipt["changedFiles"], 1)
                report = json.loads(Path(receipt["report"]).read_text())
                self.assertEqual(report["changes"], [{
                    "status": "A", "path": path, "directSkills": [], "contextSkills": [],
                }])
                self.assertEqual(report["reviewStatus"], "not_reviewed")
                self.assertIn("External pstack change", Path(receipt["patch"]).read_text())
                self.assertEqual(self.manifest.read_bytes(), original)

        base = git(self.upstream, "rev-parse", "HEAD")
        write(self.upstream, "harness/other-plugin/README.md", "Unrelated adapter\n")
        write(self.upstream, "scripts/check-other-docs.mjs", "Unrelated checker\n")
        head = commit(self.upstream)
        self.assertEqual(self.run_check("--base", base, "--head", head)["status"], "no_changes")

    def test_expanded_watch_list_reassesses_cached_no_change_result(self):
        manifest = CHECKER.parents[2] / "research/jstack/upstream.json"
        watched = json.loads(manifest.read_text())["watchPaths"]
        self.data["watchPaths"] = [p for p in watched if p != "harness/pstack"]
        self.save_manifest()
        write(self.upstream, "harness/pstack/README.md", "Changed adapter\n")
        commit(self.upstream)
        before = self.run_check()
        self.assertEqual(before["status"], "no_changes")
        old_report = Path(before["report"]).read_bytes()
        self.data["watchPaths"] = watched
        self.save_manifest()
        after = self.run_check()
        self.assertEqual(after["status"], "changes")
        self.assertFalse(after["reused"])
        self.assertNotEqual(before["reportId"], after["reportId"])
        self.assertEqual(Path(before["report"]).read_bytes(), old_report)
        self.assertEqual(json.loads(self.manifest.read_text())["reviewedThrough"], None)

    def test_fetch_failure_preserves_previous_report_and_manifest(self):
        receipt = self.run_check()
        original_report = Path(receipt["report"]).read_bytes()
        self.data["repository"] = str(self.directory / "missing")
        self.save_manifest()
        original_manifest = self.manifest.read_bytes()
        failed = self.run_check(code=2)
        self.assertEqual(failed["status"], "error")
        self.assertEqual(json.loads((self.cache / "last-run.json").read_text())["status"], "error")
        self.assertEqual(Path(receipt["report"]).read_bytes(), original_report)
        self.assertEqual(self.manifest.read_bytes(), original_manifest)

    def test_rewritten_history_cannot_advance_checkpoint(self):
        write(self.upstream, "pstack/LICENSE", "Changed license\n")
        old = commit(self.upstream)
        self.data["reviewedThrough"] = old
        self.save_manifest()
        self.run_check()
        git(self.upstream, "checkout", "-B", "main", self.base)
        write(self.upstream, "pstack/LICENSE", "Different history\n")
        commit(self.upstream)
        failed = self.run_check(code=2)
        self.assertIn("history diverged", failed["error"])
        self.assertEqual(json.loads(self.manifest.read_text())["reviewedThrough"], old)

    def test_dirty_local_skill_is_rejected(self):
        write(self.root, "skills/jstack/example/SKILL.md", "Uncommitted behavior\n")
        self.assertIn("local skill changes", self.run_check(code=2)["error"])

    def test_invalid_paths_missing_history_and_overlap_fail_explicitly(self):
        self.data["watchPaths"] = [":(exclude)pstack"]
        self.save_manifest()
        self.assertIn("literal", self.run_check(code=2)["error"])
        self.data["watchPaths"] = ["pstack"]
        self.save_manifest()
        self.assertEqual(self.run_check("--base", "a" * 40, code=2)["status"], "error")
        with (self.cache / "check.lock").open("a") as lock:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
            self.assertIn("another upstream check", self.run_check(code=2)["error"])

    def test_historical_trial_does_not_move_review_checkpoint(self):
        write(self.upstream, "pstack/LICENSE", "Changed license\n")
        head = commit(self.upstream)
        self.data["reviewedThrough"] = head
        self.save_manifest()
        trial = self.run_check("--base", self.base, "--head", head)
        self.assertEqual(trial["changedFiles"], 1)
        self.assertEqual(self.run_check()["status"], "no_changes")
        self.assertEqual(json.loads(self.manifest.read_text())["reviewedThrough"], head)

    def test_large_diff_and_deleted_supporting_file_are_complete(self):
        for i in range(305):
            write(self.upstream, f"pstack/skills/new/references/{i}.md", f"Reference {i}\n")
        git(self.upstream, "rm", "pstack/skills/example/references/helper.md")
        commit(self.upstream)
        receipt = self.run_check()
        self.assertEqual(receipt["changedFiles"], 306)
        report = json.loads(Path(receipt["report"]).read_text())
        deleted = [c for c in report["changes"] if c["status"] == "D"]
        self.assertEqual(deleted[0]["directSkills"], ["example"])

    def test_applied_decisions_require_canonical_history(self):
        write(self.root, "research/jstack/review.md", "Implementation approved\n")
        local = commit(self.root)
        self.data["decisions"] = [{"id": "fix", "disposition": "adapt", "from": self.base,
                                   "to": self.base, "paths": ["pstack/skills/example"],
                                   "reason": "Fix", "report": "research/jstack/review.md",
                                   "appliedCommit": local}]
        self.save_manifest()
        self.assertEqual(self.run_check(code=2)["status"], "error")
        git(self.root, "update-ref", "refs/remotes/origin/main", local)
        self.assertEqual(self.run_check()["pendingDecisions"], 0)


if __name__ == "__main__":
    unittest.main()
