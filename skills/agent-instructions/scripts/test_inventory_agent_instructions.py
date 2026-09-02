#!/usr/bin/env python3

from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).with_name("inventory_agent_instructions.py")
SPEC = importlib.util.spec_from_file_location("inventory_agent_instructions", MODULE_PATH)
assert SPEC and SPEC.loader
inventory = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(inventory)


class InventoryTests(unittest.TestCase):
    def test_discovers_instruction_files_but_skips_dependency_trees(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "AGENTS.md").write_text("Root policy\n", encoding="utf-8")
            (root / ".claude" / "rules").mkdir(parents=True)
            (root / ".claude" / "rules" / "tests.md").write_text("Tests\n", encoding="utf-8")
            (root / "node_modules").mkdir()
            (root / "node_modules" / "AGENTS.md").write_text("Ignore\n", encoding="utf-8")

            data = inventory.build_inventory(root.resolve(), root.resolve(), [])
            self.assertEqual(
                [item["path"] for item in data["files"]],
                ["AGENTS.md", ".claude/rules/tests.md"],
            )
            rendered = inventory.render_markdown(data)
            self.assertIn("| AGENTS.md | codex | 1 | 12 | False |", rendered)

    def test_ignores_example_imports_and_finds_real_broken_references(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "AGENTS.md").write_text("Shared\n", encoding="utf-8")
            (root / "CLAUDE.md").write_text(
                "@AGENTS.md\n"
                "[Missing](docs/missing.md)\n"
                "`@inline.md`\n"
                "``@double.md``\n"
                "```md\n@sample.md\n```\n",
                encoding="utf-8",
            )

            data = inventory.build_inventory(root.resolve(), root.resolve(), [])
            claude = next(item for item in data["files"] if item["path"] == "CLAUDE.md")
            targets = {(ref["target"], ref["status"]) for ref in claude["references"]}
            self.assertIn(("AGENTS.md", "exists"), targets)
            self.assertIn(("docs/missing.md", "missing"), targets)
            self.assertNotIn(("inline.md", "missing"), targets)
            self.assertNotIn(("double.md", "missing"), targets)
            self.assertNotIn(("sample.md", "missing"), targets)

    def test_checks_backticked_repository_paths_without_treating_commands_as_paths(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "docs").mkdir()
            (root / "docs" / "existing.md").write_text("Current\n", encoding="utf-8")
            route = root / "src" / "app" / "blog" / "[slug]"
            route.mkdir(parents=True)
            (route / "page.tsx").write_text("export default function Page() {}\n", encoding="utf-8")
            (root / "AGENTS.md").write_text(
                "Read `docs/existing.md` and `docs/missing.md`.\n"
                "The route is `src/app/blog/[slug]/page.tsx`.\n"
                "Run `bun run check`; open `/admin`; import `@/lib/utils`.\n",
                encoding="utf-8",
            )

            data = inventory.build_inventory(root.resolve(), root.resolve(), [])
            agents = next(item for item in data["files"] if item["path"] == "AGENTS.md")
            references = {
                (ref["target"], ref["status"], ref["syntax"])
                for ref in agents["references"]
            }
            self.assertIn(("docs/existing.md", "exists", "inline-code-path"), references)
            self.assertIn(("docs/missing.md", "missing", "inline-code-path"), references)
            self.assertIn(
                ("src/app/blog/[slug]/page.tsx", "exists", "inline-code-path"),
                references,
            )
            self.assertNotIn(("bun run check", "missing", "inline-code-path"), references)
            self.assertNotIn(("/admin", "missing", "inline-code-path"), references)
            self.assertNotIn(("@/lib/utils", "missing", "inline-code-path"), references)

    def test_codex_chain_prefers_override_at_each_directory(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            nested = root / "packages" / "api"
            nested.mkdir(parents=True)
            (root / "AGENTS.md").write_text("Root\n", encoding="utf-8")
            (nested / "AGENTS.md").write_text("Nested\n", encoding="utf-8")
            (nested / "AGENTS.override.md").write_text("Override\n", encoding="utf-8")

            data = inventory.build_inventory(root.resolve(), nested.resolve(), [])
            self.assertEqual(
                [item["path"] for item in data["codex_project_chain"]],
                ["AGENTS.md", "packages/api/AGENTS.override.md"],
            )

    def test_claude_project_dot_directory_is_only_a_root_candidate(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            nested = root / "packages" / "api"
            (root / ".claude").mkdir()
            (nested / ".claude").mkdir(parents=True)
            (root / ".claude" / "CLAUDE.md").write_text("Root project\n", encoding="utf-8")
            (nested / ".claude" / "CLAUDE.md").write_text("Not an ancestor candidate\n", encoding="utf-8")
            (nested / "CLAUDE.local.md").write_text("Nested local\n", encoding="utf-8")

            data = inventory.build_inventory(root.resolve(), nested.resolve(), [])
            self.assertEqual(
                data["claude_ancestor_candidates"],
                [".claude/CLAUDE.md", "packages/api/CLAUDE.local.md"],
            )

    def test_codex_fallback_is_used_only_when_primary_files_are_empty(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "AGENTS.md").write_text("\n", encoding="utf-8")
            (root / "TEAM.md").write_text("Fallback\n", encoding="utf-8")

            data = inventory.build_inventory(root.resolve(), root.resolve(), ["TEAM.md"])
            self.assertEqual(
                [item["path"] for item in data["codex_project_chain"]],
                ["TEAM.md"],
            )
            fallback = next(item for item in data["files"] if item["path"] == "TEAM.md")
            self.assertEqual(fallback["kind"], "codex-fallback")

    def test_codex_default_byte_limit_risk_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "AGENTS.md").write_text("x" * (32 * 1024 + 1), encoding="utf-8")

            data = inventory.build_inventory(root.resolve(), root.resolve(), [])
            self.assertEqual(data["codex_project_bytes"], 32 * 1024 + 1)
            self.assertTrue(data["codex_default_limit_risk"])

    def test_cli_emits_machine_readable_inventory(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            nested = root / "app"
            nested.mkdir()
            (root / "AGENTS.md").write_text("Root\n", encoding="utf-8")
            (root / "CLAUDE.md").write_text("@AGENTS.md\n", encoding="utf-8")

            completed = subprocess.run(
                [
                    sys.executable,
                    str(MODULE_PATH),
                    "--root",
                    str(root),
                    "--cwd",
                    str(nested),
                    "--format",
                    "json",
                ],
                check=True,
                capture_output=True,
                text=True,
            )
            data = json.loads(completed.stdout)
            self.assertEqual(data["codex_project_chain"][0]["path"], "AGENTS.md")
            self.assertEqual(data["claude_ancestor_candidates"], ["CLAUDE.md"])
            self.assertEqual(data["broken_references"], [])

    def test_external_instruction_symlink_is_reported_without_reading(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            root = base / "repo"
            root.mkdir()
            outside = base / "outside.md"
            outside.write_text("Private instructions\n", encoding="utf-8")
            (root / "AGENTS.md").symlink_to(outside)

            data = inventory.build_inventory(root.resolve(), root.resolve(), [])
            agents = next(item for item in data["files"] if item["path"] == "AGENTS.md")
            self.assertEqual(agents["bytes"], 0)
            self.assertEqual(agents["references"], [])
            self.assertIn("outside the repository", agents["error"])
            self.assertEqual(data["codex_project_chain"], [])
            self.assertEqual(data["loading_warnings"][0]["source"], "AGENTS.md")


if __name__ == "__main__":
    unittest.main()
