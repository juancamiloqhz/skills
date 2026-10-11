"""Exercise the consumer CLI with separately located setup and config files."""

import copy
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


SCRIPT = Path(__file__).with_name("preflight.py")
SOURCE_SETUP = Path(__file__).resolve().parents[2] / "setup-jstack"
CATALOG = {
    "inheritedProviderInstanceId": "parent",
    "inheritedModel": "parent-model",
    "providers": [
        {"providerInstanceId": "parent", "canRunChildTask": True,
         "canRunCrossProviderChildTask": True,
         "models": [{"id": "parent-model", "options": []}]},
        {"providerInstanceId": "other", "canRunChildTask": True,
         "canRunCrossProviderChildTask": True,
         "models": [{"id": "other-model", "options": [
             {"id": "effort", "type": "select", "options": [{"id": "high"}]},
             {"id": "fast", "type": "boolean"}]}]},
    ],
}
SEAT = {"providerInstanceId": "other", "model": "other-model",
        "options": {"effort": "high", "fast": False}}


class PreflightTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.setup = self.root / "separate installation" / "setup-jstack"
        shutil.copytree(SOURCE_SETUP, self.setup, ignore=shutil.ignore_patterns("__pycache__"))
        self.config = self.root / "saved.json"
        self.catalog = self.root / "live.json"
        self.mapping = json.loads(subprocess.check_output([
            sys.executable, str(self.setup / "scripts/models.py"), "template",
        ], text=True))
        self.live = copy.deepcopy(CATALOG)
        self.save()

    def save(self):
        self.config.write_text(json.dumps(self.mapping))
        self.catalog.write_text(json.dumps(self.live))

    def run_cli(self, role="how explorer", explicit=True, env=None, setup=None):
        command = [sys.executable, str(SCRIPT), "--setup-skill", str(setup or self.setup),
                   "--catalog", str(self.catalog), "--role", role]
        if explicit:
            command.extend(["--config", str(self.config)])
        original = self.config.read_bytes()
        result = subprocess.run(command, cwd=self.root, text=True, capture_output=True,
                                env=dict(os.environ, **(env or {})))
        self.assertEqual(self.config.read_bytes(), original)
        return result

    def resolved(self, **kwargs):
        result = self.run_cli(**kwargs)
        self.assertEqual(result.returncode, 0, result.stderr)
        return json.loads(result.stdout)

    def rejected(self, expected, **kwargs):
        result = self.run_cli(**kwargs)
        self.assertEqual(result.returncode, 1)
        self.assertEqual(result.stdout, "")
        self.assertIn(expected, result.stderr)

    def test_discovered_dependency_inheritance_and_no_install_writes(self):
        before = sorted(str(p.relative_to(self.setup)) for p in self.setup.rglob("*"))
        result = self.resolved()
        self.assertEqual(result["targets"], [None])
        self.assertEqual(result["effectiveIdentities"], [{
            "providerInstanceId": "parent", "model": "parent-model", "inherited": True}])
        self.assertEqual(result["resolver"], str(self.setup / "scripts/models.py"))
        self.assertEqual(before, sorted(str(p.relative_to(self.setup)) for p in self.setup.rglob("*")))

    def test_order_duplicates_options_and_pool_semantics(self):
        seats = [copy.deepcopy(SEAT), {"alias": "inherit-parent"}, copy.deepcopy(SEAT)]
        self.mapping["roles"]["arena runners"] = seats
        self.mapping["roles"]["arena cross-judge pool"] = seats
        self.save()
        panel = self.resolved(role="arena runners")
        pool = self.resolved(role="arena cross-judge pool")
        self.assertEqual(panel["targets"], [SEAT, None, SEAT])
        self.assertEqual(pool["targets"], panel["targets"])
        self.assertEqual(panel["selectionKind"], "panel")
        self.assertEqual(pool["selectionKind"], "pool")

    def test_unrelated_stale_role_blocks_dispatch(self):
        self.mapping["roles"]["bug-fix"] = dict(SEAT, model="retired")
        self.save()
        self.rejected("bug-fix: unavailable model")

    def test_catalog_drift_and_inherited_provider_capability(self):
        self.live["providers"][0]["canRunChildTask"] = False
        self.save()
        self.rejected("effective child selection unavailable")
        self.live["providers"][0]["canRunChildTask"] = True
        self.live["inheritedModel"] = "missing"
        self.save()
        self.rejected("effective child selection unavailable")

    def test_cross_provider_capability_is_separate(self):
        self.mapping["roles"]["how explorer"] = copy.deepcopy(SEAT)
        self.live["providers"][1]["canRunCrossProviderChildTask"] = False
        self.save()
        self.rejected("cross-provider child execution unavailable")

    def test_config_reloaded_between_calls(self):
        self.assertEqual(self.resolved()["targets"], [None])
        self.mapping["roles"]["how explorer"] = copy.deepcopy(SEAT)
        self.save()
        self.assertEqual(self.resolved()["targets"], [SEAT])

    def test_config_path_precedence(self):
        missing = str(self.root / "absent.json")
        self.resolved(env={"JSTACK_CONFIG": missing})
        self.resolved(explicit=False, env={"JSTACK_CONFIG": str(self.config)})
        xdg_config = self.root / "xdg" / "jstack" / "models.json"
        xdg_config.parent.mkdir(parents=True)
        shutil.copyfile(self.config, xdg_config)
        result = self.resolved(explicit=False, env={"JSTACK_CONFIG": "", "XDG_CONFIG_HOME": str(self.root / "xdg")})
        self.assertEqual(result["config"], str(xdg_config))
        self.rejected("No such file", explicit=False, env={"JSTACK_CONFIG": missing})

    def test_missing_or_wrong_dependency(self):
        self.rejected("No such file", setup=self.root / "not-installed")
        (self.setup / "SKILL.md").write_text("---\nname: unrelated\n---\n")
        self.rejected("catalog-discovered setup-jstack")

    def test_invalid_and_duplicate_configuration(self):
        self.config.write_text('{"schemaVersion":1,"schemaVersion":2}')
        self.rejected("duplicate JSON key")
        self.mapping["roles"]["how explorer"] = dict(SEAT, options={"effort": "unsupported"})
        self.save()
        self.rejected("unsupported effort value")

    def test_one_inherited_judge_remains_one_alternative(self):
        result = self.resolved(role="arena cross-judge pool")
        self.assertEqual(result["targets"], [None])
        self.assertEqual(result["selectionKind"], "pool")

    def test_unavailable_pool_alternative_does_not_block_eligible_judge(self):
        seats = [{"alias": "inherit-parent"}, copy.deepcopy(SEAT)]
        self.mapping["roles"]["arena cross-judge pool"] = seats
        self.mapping["roles"]["arena runners"] = seats
        self.live["providers"][1]["canRunCrossProviderChildTask"] = False
        self.save()
        result = self.resolved(role="arena cross-judge pool")
        self.assertEqual(result["targets"], [None, SEAT])
        self.assertEqual([s["canDispatch"] for s in result["availability"]], [True, False])
        self.assertIn("cross-provider", result["availability"][1]["reason"])
        self.rejected("cross-provider child execution unavailable", role="arena runners")

    def test_pool_with_no_executable_alternative_fails(self):
        self.mapping["roles"]["arena cross-judge pool"] = [copy.deepcopy(SEAT)]
        self.live["providers"][1]["canRunCrossProviderChildTask"] = False
        self.save()
        self.rejected("no executable judge alternative", role="arena cross-judge pool")


if __name__ == "__main__":
    unittest.main()
