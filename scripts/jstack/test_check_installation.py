"""Exercise the CLI against disposable Git repositories and installations."""

import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


CHECKER = Path(__file__).with_name("check_installation.py")


class InstallationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.repo = self.root / "repo"
        self.source = self.repo / "skills/jstack/jstack-demo"
        self.source.mkdir(parents=True)
        (self.source / "SKILL.md").write_text("demo\n")
        (self.source / "scripts").mkdir()
        (self.source / "scripts/run.py").write_text("print('demo')\n")
        self.manifest = self.repo / "research/jstack/upstream.json"
        self.manifest.parent.mkdir(parents=True)
        self.manifest.write_text(json.dumps({"skills": [
            {"name": "jstack-demo", "localPath": "skills/jstack/jstack-demo"}
        ]}))
        subprocess.run(["git", "init", "-q", str(self.repo)], check=True)
        subprocess.run(["git", "-C", str(self.repo), "add", "."], check=True)
        self.installed = self.root / "installed"
        self.target = self.installed / "jstack-demo"
        shutil.copytree(self.source, self.target)

    def run_check(self, code):
        result = subprocess.run([sys.executable, str(CHECKER), "--repo-root", str(self.repo),
                                 "--installed-root", str(self.installed), "--json"],
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, code, result.stdout + result.stderr)
        return json.loads(result.stdout)

    def test_matching_symlink_and_ignored_extras_are_read_only(self):
        shutil.rmtree(self.target)
        self.target.symlink_to(self.source, target_is_directory=True)
        (self.source / "untracked-cache").write_text("ignore")
        before = {p.relative_to(self.root): p.read_bytes() for p in self.root.rglob("*") if p.is_file()}
        self.assertEqual(self.run_check(0)["summary"]["matching"], 1)
        after = {p.relative_to(self.root): p.read_bytes() for p in self.root.rglob("*") if p.is_file()}
        self.assertEqual(before, after)

    def test_missing_package(self):
        shutil.rmtree(self.target)
        report = self.run_check(1)
        self.assertEqual(report["summary"]["missing"], 1)
        self.assertEqual(report["outcome"], "complete")

    def test_changed_and_missing_files_with_installed_extra(self):
        (self.target / "SKILL.md").write_text("customized")
        (self.target / "scripts/run.py").unlink()
        (self.target / "extra").write_text("ignored")
        package = self.run_check(1)["packages"][0]
        self.assertEqual(package["status"], "different")
        self.assertEqual(package["missingFiles"], ["scripts/run.py"])
        self.assertEqual(package["changedFiles"], ["SKILL.md"])

    def test_invalid_manifest_and_root_are_incomplete(self):
        for content in ("{", "[]", '{"skills": []}',
                        '{"skills":[{"name":"jstack-demo","localPath":"../escape"}]}'):
            with self.subTest(content=content):
                self.manifest.write_text(content)
                self.assertEqual(self.run_check(2)["outcome"], "incomplete")
        shutil.rmtree(self.installed)
        self.assertIn("not a directory", self.run_check(2)["error"])

    def test_source_loss_or_unreadable_target_is_incomplete(self):
        target = self.target / "SKILL.md"
        target.unlink()
        target.mkdir()
        self.assertEqual(self.run_check(2)["outcome"], "incomplete")
        target.rmdir()
        (self.source / "SKILL.md").unlink()
        self.assertEqual(self.run_check(2)["outcome"], "incomplete")


if __name__ == "__main__":
    unittest.main()
