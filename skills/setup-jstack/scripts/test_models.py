"""Behavioral checks for catalog drift, inheritance and saved selections."""

import copy
import json
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


if __name__ == "__main__":
    unittest.main()
