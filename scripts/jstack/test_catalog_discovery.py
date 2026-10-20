"""Opt-in Skills CLI discovery against a fresh clone of the committed repository."""

import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[2]


def snapshot(root):
    return {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in root.rglob('*') if p.is_file()}


@unittest.skipUnless(os.environ.get('JSTACK_SKILLS_CLI'),
                     'Set JSTACK_SKILLS_CLI to an existing Skills CLI file')
class CatalogDiscoveryTests(unittest.TestCase):
    def test_complete_committed_catalog_and_renamed_entrypoint_control(self):
        cli = Path(os.environ['JSTACK_SKILLS_CLI']).resolve(strict=True)
        # The clone tests HEAD. Refuse to silently miss edits to its inputs.
        pending = subprocess.check_output(
            ['git', '-C', str(ROOT), 'status', '--porcelain', '--untracked-files=all',
             '--', 'skills', 'automations', 'research/jstack/upstream.json'], text=True)
        self.assertFalse(pending, 'Commit package/manifest edits before testing discovery: ' + pending)
        env = dict(os.environ, DISABLE_TELEMETRY='1', DO_NOT_TRACK='1', NO_COLOR='1')
        env.pop('INSTALL_INTERNAL_SKILLS', None)
        with tempfile.TemporaryDirectory() as directory:
            clone = Path(directory) / 'checkout'
            subprocess.run(['git', 'clone', '--no-local', str(ROOT), str(clone)],
                           check=True, capture_output=True, text=True, timeout=60)
            self.assertFalse((clone / '.git/objects/info/alternates').exists())
            manifest = json.loads((clone / 'research/jstack/upstream.json').read_text())
            jstack = {s['name'] for s in manifest['skills']}
            expected = []
            for entry in (clone / 'skills').rglob('SKILL.md'):
                match = re.search(r'^name: ([a-z0-9-]+)$', entry.read_text(), re.M)
                self.assertIsNotNone(match, str(entry))
                expected.append(match[1])
            self.assertEqual(len(expected), len(set(expected)), 'Duplicate skill identity')
            self.assertEqual({n for n in expected if n.startswith('jstack-')}, jstack)

            def listing(*flags):
                run = subprocess.run(['node', str(cli), 'add', str(clone), '--list', *flags],
                                     cwd=clone, env=env, capture_output=True,
                                     text=True, timeout=30)
                self.assertEqual(run.returncode, 0, run.stderr + run.stdout)
                plain = re.sub(r'\x1b\[[0-?]*[ -/]*[@-~]', '', run.stdout)
                # Match catalog rows, not names mentioned inside descriptions.
                names = re.findall(r'^│    ([a-z0-9-]+)\s*$', plain, re.M)
                self.assertTrue(names, 'Skills CLI catalog format changed: ' + plain)
                return names

            before = snapshot(clone)
            for flags in [(), ('--full-depth',), ('--full-depth', '--skill', '*')]:
                with self.subTest(flags=flags):
                    self.assertCountEqual(listing(*flags), expected)
            self.assertEqual(snapshot(clone), before, 'Listing changed the checkout')

            # A deliberate packaging error must change the observed catalog.
            entry = clone / 'skills/jstack/jstack-bro/SKILL.md'
            entry.write_text(entry.read_text().replace(
                'name: jstack-bro\n', 'name: jstack-discovery-negative-control\n', 1))
            observed = listing()
            self.assertEqual(set(expected) - set(observed), {'jstack-bro'})
            self.assertEqual(set(observed) - set(expected), {'jstack-discovery-negative-control'})
            self.assertEqual(len(observed), len(expected))


if __name__ == '__main__':
    unittest.main()
