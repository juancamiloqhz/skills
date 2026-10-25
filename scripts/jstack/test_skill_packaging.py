"""Check the shipped catalog and cross-package references without installing skills."""

import json
from pathlib import Path
import re
import subprocess
import unittest

ROOT = Path(__file__).resolve().parents[2]
SKILLS = ROOT / "skills/jstack"
MANIFEST = json.loads((ROOT / "research/jstack/upstream.json").read_text())
TRACKED = [ROOT / name.decode() for name in subprocess.check_output(
    ["git", "-C", str(ROOT), "ls-files", "-z", "--", "skills/jstack"]
).split(b"\0") if name]


class SkillPackagingTest(unittest.TestCase):
    def test_catalog_matches_manifest_and_portable_directory_names(self):
        actual = {}
        for entry in SKILLS.glob("*/SKILL.md"):
            name = re.search(r"^name: ([a-z0-9-]+)$", entry.read_text(), re.M).group(1)
            self.assertRegex(name, r"^jstack-[a-z0-9]+(?:-[a-z0-9]+)*$")
            self.assertLessEqual(len(name), 64)
            self.assertEqual(entry.parent.name, name)
            self.assertNotIn(name, actual)
            actual[name] = str(entry.parent.relative_to(ROOT))
        self.assertEqual(actual, {s["name"]: s["localPath"] for s in MANIFEST["skills"]})

    def test_explicit_callers_and_install_commands_use_current_names(self):
        names = {s["name"] for s in MANIFEST["skills"]}
        former = {n.removeprefix("jstack-") for n in names} - {"setup"}
        former.add("setup-jstack")
        for entry in TRACKED:
            if entry.suffix not in (".md", ".yaml"):
                continue
            text = entry.read_text()
            for name in re.findall(r"--skill ([a-z][a-z0-9-]*)(?=[ `\n]|$)", text):
                self.assertIn(name, names, str(entry))
            for name in former:
                for marker in (f"**{name}**", f"${name}", f"`{name}` skill"):
                    self.assertNotIn(marker, text, str(entry))
            self.assertNotRegex(text, r"(?<![a-z-])principle-\*", str(entry))

    def test_package_markdown_links_resolve_within_the_package(self):
        for entry in TRACKED:
            if entry.suffix != ".md":
                continue
            package = SKILLS / entry.relative_to(SKILLS).parts[0]
            for target in re.findall(r"\]\(([^)]+)\)", entry.read_text()):
                if "://" in target or target.startswith("#") or target == "url":
                    continue
                target = target.split("#", 1)[0]
                resolved = (entry.parent / target).resolve()
                self.assertTrue(resolved.is_relative_to(package), (entry, target))
                self.assertTrue(resolved.exists(), (entry, target))

    def test_ui_prompts_invoke_their_own_package(self):
        for entry in SKILLS.glob("*/agents/openai.yaml"):
            name = entry.parent.parent.name
            self.assertIn(f"${name} ", entry.read_text())


if __name__ == "__main__":
    unittest.main()
