"""Behavioral checks for catalog drift, inheritance and saved selections."""

import copy
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from models import atomic_write, read_json, resolve, template, validate


CATALOG = {"providers": [
    {"providerInstanceId": "codex", "canRunChildTask": True, "models": [
        {"id": "code-model", "options": [
            {"id": "reasoningEffort", "type": "select", "options": [
                {"id": "medium"}, {"id": "high"}]},
            {"id": "fastMode", "type": "boolean"},
        ]},
    ]},
    {"providerInstanceId": "disabled", "canRunChildTask": False, "models": [
        {"id": "code-model", "options": []},
    ]},
]}
SEAT = {"providerInstanceId": "codex", "model": "code-model",
        "options": {"reasoningEffort": "high", "fastMode": True}}


class ModelsTest(unittest.TestCase):
    def test_inheritance_and_panel_count(self):
        config = template("medium")
        config["roles"]["arena runners"] *= 2
        validate(config, CATALOG)
        self.assertEqual(resolve(config, "arena runners"), [None, None])
        self.assertEqual(resolve(config, "how explorer"), [None])

    def test_concrete_target_and_atomic_roundtrip(self):
        config = template("large")
        config["roles"]["bug-fix"] = copy.deepcopy(SEAT)
        validate(config, CATALOG)
        self.assertEqual(resolve(config, "bug-fix"), [SEAT])
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "nested" / "models.json"
            atomic_write(path, config)
            self.assertEqual(read_json(path), config)
            atomic_write(path, template("small"))
            self.assertEqual(read_json(path), template("small"))
            self.assertEqual(list(path.parent.iterdir()), [path])

    def test_invalid_selection_and_catalog_drift(self):
        changes = [
            {"providerInstanceId": "disabled", "options": {}},
            {"providerInstanceId": "missing"},
            {"model": "code-model-high"},
            {"options": {"reasoningEffort": "max"}},
            {"options": {"fastMode": "true"}},
            {"options": {"invented": True}},
        ]
        for change in changes:
            with self.subTest(change=change):
                config = template("medium")
                config["roles"]["bug-fix"] = dict(SEAT, **change)
                with self.assertRaises(ValueError):
                    validate(config, CATALOG)
        config = template("medium")
        config["roles"]["bug-fix"] = copy.deepcopy(SEAT)
        with self.assertRaises(ValueError):
            validate(config, {"providers": []})

    def test_contract_errors_preserve_input(self):
        config = template("medium")
        config["roles"]["arena runners"] = []
        before = copy.deepcopy(config)
        with self.assertRaises(ValueError):
            validate(config, CATALOG)
        self.assertEqual(config, before)
        for mutate in (
            lambda c: c.update(schemaVersion=2),
            lambda c: c["roles"].update(retired={"alias": "inherit-parent"}),
            lambda c: c["roles"].update({"bug-fix": {"alias": "auto"}}),
        ):
            config = template("medium")
            mutate(config)
            with self.assertRaises(ValueError):
                validate(config, CATALOG)

    def test_duplicate_json_keys_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "bad.json"
            path.write_text('{"preset":"small","preset":"large"}')
            with self.assertRaises(ValueError):
                read_json(path)

    def test_invalid_cli_write_preserves_saved_configuration(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            catalog = root / "catalog.json"
            draft = root / "draft.json"
            output = root / "models.json"
            catalog.write_text(json.dumps(CATALOG))
            original = template("small")
            output.write_text(json.dumps(original))
            invalid = template("medium")
            invalid["roles"]["bug-fix"] = dict(SEAT, model="removed-model")
            draft.write_text(json.dumps(invalid))
            result = subprocess.run([
                sys.executable, str(Path(__file__).with_name("models.py")),
                "write", str(draft), "--catalog", str(catalog),
                "--output", str(output),
            ], capture_output=True, text=True)
            self.assertEqual(result.returncode, 1)
            self.assertIn("unavailable model", result.stderr)
            self.assertEqual(read_json(output), original)


class ConfigLookupTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.repo = self.root / "project with spaces"
        self.repo.mkdir()
        subprocess.run(["git", "init", "-q", "-b", "main", str(self.repo)], check=True)
        self.nested = self.repo / "src" / "nested"
        self.nested.mkdir(parents=True)
        self.global_config = self.root / "xdg" / "jstack" / "models.json"
        self.project_config = self.repo / ".jstack" / "models.json"
        self.env = dict(os.environ, JSTACK_CONFIG="", XDG_CONFIG_HOME=str(self.root / "xdg"))
        self.catalog = self.root / "catalog.json"
        self.catalog.write_text(json.dumps(CATALOG))
        self.script = Path(__file__).with_name("models.py").resolve()
        atomic_write(self.global_config, template("small"))

    def cli(self, *args, cwd=None, env=None):
        return subprocess.run([sys.executable, str(self.script), *map(str, args)],
                              cwd=cwd or self.nested, env=env or self.env,
                              capture_output=True, text=True)

    def output(self, *args, **kwargs):
        result = self.cli(*args, **kwargs)
        self.assertEqual(result.returncode, 0, result.stderr)
        return json.loads(result.stdout)

    def test_complete_precedence_and_absolute_paths(self):
        self.assertEqual(self.output("locate"), {
            "path": str(self.global_config), "source": "global", "exists": True})
        atomic_write(self.project_config, template("medium"))
        self.assertEqual(self.output("locate")["path"], str(self.project_config))
        custom = self.root / "environment.json"
        env = dict(self.env, JSTACK_CONFIG=str(custom))
        self.assertEqual(self.output("locate", env=env), {
            "path": str(custom), "source": "environment", "exists": False})
        self.assertEqual(self.output("locate", "--config", "chosen.json", env=env), {
            "path": str(self.nested / "chosen.json"), "source": "explicit", "exists": False})

    def test_symlink_parent_paths_preserve_filesystem_meaning(self):
        actual = self.root / "actual"
        (actual / "subdir").mkdir(parents=True)
        links = self.root / "links"
        links.mkdir()
        (links / "current").symlink_to(actual / "subdir", target_is_directory=True)
        intended = template("large")
        intended["roles"]["how explorer"] = copy.deepcopy(SEAT)
        atomic_write(actual / "models.json", intended)
        atomic_write(links / "models.json", template("small"))
        requested = links / "current" / ".." / "models.json"
        args = ("--catalog", self.catalog, "--role", "how explorer", "--with-source")
        self.assertEqual(self.output("resolve", requested, *args)["targets"], [SEAT])
        self.assertEqual(self.output("resolve", *args,
                                     env=dict(self.env, JSTACK_CONFIG=str(requested)))["targets"], [SEAT])
        atomic_write(actual / ".jstack/models.json", intended)
        atomic_write(links / ".jstack/models.json", template("small"))
        result = self.output("resolve", "--project-root", links / "current" / "..", *args)
        self.assertEqual(result["targets"], [SEAT])
        self.assertTrue(Path(result["config"]).is_absolute())

    def test_scope_is_read_only_and_ignores_other_scope_overrides(self):
        env = dict(self.env, JSTACK_CONFIG=str(self.root / "environment.json"))
        target = self.output("locate", "--scope", "project", env=env)
        self.assertEqual(target, {"path": str(self.project_config), "source": "project", "exists": False})
        self.assertFalse(self.project_config.parent.exists())
        atomic_write(self.project_config, template("medium"))
        self.assertEqual(self.output("locate", "--scope", "global", env=env)["path"], str(self.global_config))
        self.assertNotEqual(self.cli("locate", "--scope", "global", "--config", "x").returncode, 0)

    def test_explicit_project_and_no_git_fallback(self):
        plain = self.root / "plain-project"
        plain.mkdir()
        self.assertEqual(self.output("locate", cwd=plain)["path"], str(self.global_config))
        self.assertNotEqual(self.cli("locate", "--scope", "project", cwd=plain).returncode, 0)
        target = self.output("locate", "--scope", "project", "--project-root", plain)
        self.assertEqual(target["path"], str(plain / ".jstack/models.json"))
        self.assertNotEqual(self.cli("locate", "--project-root", plain / "missing").returncode, 0)

    def test_selected_file_is_complete_and_invalid_project_never_falls_back(self):
        project = template("large")
        project["roles"]["how explorer"] = copy.deepcopy(SEAT)
        atomic_write(self.project_config, project)
        args = ("resolve", "--catalog", self.catalog, "--role", "how explorer", "--with-source")
        self.assertEqual(self.output(*args), {
            "config": str(self.project_config), "configSource": "project", "targets": [SEAT]})
        self.assertEqual(self.output("resolve", self.global_config, "--catalog", self.catalog,
                                     "--role", "how explorer"), [None])
        for invalid in ('{"roles": {}}', '{"schemaVersion":1,"schemaVersion":2}', 'invalid JSON'):
            self.project_config.write_text(invalid)
            result = self.cli(*args)
            self.assertEqual(result.returncode, 1)
            self.assertEqual(result.stdout, "")
            self.assertIn(str(self.project_config), result.stderr)
            self.assertEqual(read_json(self.global_config), template("small"))

    def test_directory_and_dangling_symlink_are_selected_errors(self):
        self.project_config.mkdir(parents=True)
        self.assertEqual(self.output("locate")["source"], "project")
        args = ("resolve", "--catalog", self.catalog, "--role", "how explorer")
        self.assertEqual(self.cli(*args).returncode, 1)
        self.project_config.rmdir()
        self.project_config.symlink_to(self.root / "missing-target.json")
        self.assertEqual(self.output("locate")["source"], "project")
        self.assertEqual(self.cli(*args).returncode, 1)

    def test_project_seed_save_and_global_save_preserve_other_scope(self):
        target = self.output("locate", "--scope", "project")
        source = self.output("locate", "--scope", "global")
        draft = read_json(source["path"])
        draft["roles"]["bug-fix"] = copy.deepcopy(SEAT)
        draft_path = self.root / "draft.json"
        draft_path.write_text(json.dumps(draft))
        original_global = self.global_config.read_bytes()
        self.output("write", draft_path, "--catalog", self.catalog, "--output", target["path"])
        self.assertEqual(read_json(self.project_config), draft)
        self.assertEqual(self.global_config.read_bytes(), original_global)
        self.assertEqual(len(draft["roles"]), 17)
        original_project = self.project_config.read_bytes()
        draft_path.write_text(json.dumps(template("unlimited")))
        self.output("write", draft_path, "--catalog", self.catalog, "--output", source["path"])
        self.assertEqual(self.project_config.read_bytes(), original_project)

    def test_worktree_root_and_pinned_parent_selection(self):
        (self.repo / "file.txt").write_text("fixture\n")
        subprocess.run(["git", "-C", str(self.repo), "add", "file.txt"], check=True)
        subprocess.run(["git", "-C", str(self.repo), "-c", "user.name=Test",
                        "-c", "user.email=test@example.invalid", "commit", "-qm", "Fixture"], check=True)
        project = template("medium")
        project["roles"]["how explorer"] = copy.deepcopy(SEAT)
        atomic_write(self.project_config, project)
        selected = self.output("locate")["path"]
        worktree = self.root / "child-worktree"
        subprocess.run(["git", "-C", str(self.repo), "worktree", "add", "-q", "-b", "child", str(worktree)], check=True)
        self.assertEqual(self.output("locate", cwd=worktree)["path"], str(self.global_config))
        args = ("resolve", selected, "--catalog", self.catalog, "--role", "how explorer", "--with-source")
        pinned = self.output(*args, cwd=worktree)
        self.assertEqual(pinned["config"], selected)
        self.assertEqual(pinned["targets"], [SEAT])
        atomic_write(worktree / ".jstack/models.json", template("large"))
        self.assertEqual(self.output("locate", cwd=worktree)["path"], str(worktree / ".jstack/models.json"))
        self.assertEqual(self.output(*args, cwd=worktree)["targets"], [SEAT])


if __name__ == "__main__":
    unittest.main()
