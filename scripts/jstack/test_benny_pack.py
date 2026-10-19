"""Offline setup checks; optional actual Skills CLI discovery from a fresh checkout."""

import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import unittest

from copy_benny_pack import PACK, DESTINATION, copy_pack

ROOT = Path(__file__).resolve().parents[2]
NAMES = ['setup-benny', 'triage-issue-reports', 'reproduce-and-fix-issues']
DEPENDENCIES = ['jstack-how', 'jstack-why', 'jstack-tdd',
                *['jstack-principle-' + n for n in (
                    'separate-before-serializing-shared-state', 'minimize-reader-load',
                    'guard-the-context-window', 'sequence-verifiable-units',
                    'fix-root-causes', 'prove-it-works')]]


def git(root, *args):
    return subprocess.run(['git', '-c', 'user.name=Fixture', '-c',
                           'user.email=fixture@example.invalid', '-C', str(root), *args],
                          check=True, capture_output=True, text=True)


class CopyTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.target = self.root / 'target'
        self.target.mkdir()

    def test_preview_fresh_copy_and_repeat_preserve_user_files(self):
        user = self.target / '.agents/benny/configuration.yaml'
        user.parent.mkdir(parents=True)
        user.write_text('user-owned\n')
        destination = self.target / DESTINATION
        extra = destination / 'local-note.md'
        extra.parent.mkdir(parents=True)
        extra.write_text('keep\n')
        report = copy_pack(PACK, self.target)
        self.assertEqual(report['outcome'], 'preview')
        self.assertEqual(len(report['missing']), 13)
        self.assertFalse((destination / 'FOR_AGENTS.md').exists())
        copied = copy_pack(PACK, self.target, apply=True)
        self.assertEqual(len(copied['added']), 13)
        for path in PACK.rglob('*'):
            if path.is_file():
                self.assertEqual(path.read_bytes(), (destination / path.relative_to(PACK)).read_bytes())
        again = copy_pack(PACK, self.target, apply=True)
        self.assertEqual(again['added'], [])
        self.assertEqual(len(again['matching']), 13)
        self.assertEqual(user.read_text(), 'user-owned\n')
        self.assertEqual(extra.read_text(), 'keep\n')

    def test_changed_file_prevents_every_copy_until_reviewed(self):
        conflict = self.target / DESTINATION / 'README.md'
        conflict.parent.mkdir(parents=True)
        conflict.write_text('local customization\n')
        result = copy_pack(PACK, self.target, apply=True)
        self.assertEqual(result['conflicts'], ['README.md'])
        self.assertEqual(list(conflict.parent.iterdir()), [conflict])
        self.assertEqual(conflict.read_text(), 'local customization\n')

    def test_symlink_in_source_or_destination_is_never_followed(self):
        outside = self.root / 'outside'
        outside.mkdir()
        (self.target / '.agents').symlink_to(outside, target_is_directory=True)
        with self.assertRaisesRegex(ValueError, 'Symlink'):
            copy_pack(PACK, self.target, apply=True)
        self.assertEqual(list(outside.iterdir()), [])
        (self.target / '.agents').unlink()
        source = self.root / 'source'
        shutil.copytree(PACK, source)
        (source / 'unexpected').symlink_to(outside, target_is_directory=True)
        with self.assertRaisesRegex(ValueError, 'Symlink'):
            copy_pack(source, self.target, apply=True)
        self.assertEqual(list(self.target.iterdir()), [])

    def test_non_directory_parent_fails_before_writing(self):
        (self.target / '.agents').write_text('user data')
        with self.assertRaisesRegex(ValueError, 'not a directory'):
            copy_pack(PACK, self.target, apply=True)
        self.assertEqual((self.target / '.agents').read_text(), 'user data')

    def test_conflicting_directory_is_preserved(self):
        path = self.target / DESTINATION / 'README.md'
        path.mkdir(parents=True)
        self.assertEqual(copy_pack(PACK, self.target, apply=True)['conflicts'], ['README.md'])
        self.assertTrue(path.is_dir())

    def test_incomplete_source_does_not_copy(self):
        source = self.root / 'source'
        shutil.copytree(PACK, source)
        (source / 'skills/reproduce-and-fix-issues/references/verify-existing-fix.md').unlink()
        with self.assertRaisesRegex(ValueError, 'complete Benny pack'):
            copy_pack(source, self.target, apply=True)
        self.assertEqual(list(self.target.iterdir()), [])

    def test_cannot_copy_into_source(self):
        with self.assertRaisesRegex(ValueError, 'separate trees'):
            copy_pack(PACK, PACK, apply=True)

    def test_pack_links_and_normalized_trigger_examples(self):
        for path in PACK.rglob('*.md'):
            for target in re.findall(r'\]\(([^)]+)\)', path.read_text()):
                if not target.startswith(('https:', 'http:', '#')):
                    self.assertTrue((path.parent / target).exists(), (path, target))
        for name in ('triage', 'reproduce'):
            text = (PACK / f'templates/{name}-automation-prompt.md').read_text()
            trigger = json.loads(re.search(r'```json\n(.*?)\n```', text, re.S)[1])
            self.assertEqual(set(trigger), {'source_channel_id', 'ts', 'thread_ts'})
            self.assertTrue(all(isinstance(v, str) for v in trigger.values()))


@unittest.skipUnless(os.environ.get('JSTACK_SKILLS_CLI'), 'Set JSTACK_SKILLS_CLI to an existing Skills CLI file')
class DiscoveryTests(unittest.TestCase):
    def test_real_cli_hides_procedures_and_fresh_clone_contains_dependencies(self):
        cli = Path(os.environ['JSTACK_SKILLS_CLI']).resolve(strict=True)
        env = dict(os.environ, DISABLE_TELEMETRY='1', DO_NOT_TRACK='1', NO_COLOR='1')
        env.pop('INSTALL_INTERNAL_SKILLS', None)
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source, clone = root / 'source', root / 'clone'
            source.mkdir()
            # Exercise source distribution's depth-five layout with real package contents.
            shutil.copytree(PACK, source / 'automations/jstack/benny')
            for name in DEPENDENCIES + ['jstack-setup']:
                shutil.copytree(ROOT / 'skills/jstack' / name, source / 'skills/jstack' / name)
            # External Unslop is a declared dependency; no counterfeit substitute in this test.
            unslop = os.environ.get('JSTACK_UNSLOP_SOURCE')
            self.assertTrue(unslop, 'Set JSTACK_UNSLOP_SOURCE to the reviewed external Unslop package')
            shutil.copytree(Path(unslop), source / 'skills/unslop')
            git(source, 'init', '-b', 'main')
            git(source, 'add', '.')
            git(source, 'commit', '-qm', 'Fixture project dependencies')
            git(root, 'clone', '--no-local', str(source), str(clone))
            shutil.rmtree(source)
            expected = DEPENDENCIES + ['unslop', 'jstack-setup']

            def listing(*flags, extra_env=None):
                run = subprocess.run(['node', str(cli), 'add', str(clone), '--list', *flags],
                                     cwd=clone, env={**env, **(extra_env or {})},
                                     capture_output=True, text=True, timeout=30)
                self.assertEqual(run.returncode, 0, run.stderr + run.stdout)
                return run.stdout

            for flags in [(), ('--full-depth',), ('--full-depth', '--skill', '*')]:
                output = listing(*flags)
                for name in expected:
                    self.assertIn(name, output)
                for name in NAMES:
                    self.assertNotIn(name, output)
            explicit = listing('--full-depth', '--skill', 'setup-benny')
            self.assertIn('setup-benny', explicit)
            override = listing('--full-depth', extra_env={'INSTALL_INTERNAL_SKILLS': '1'})
            for name in NAMES:
                self.assertIn(name, override)
            # Installed-style target copy remains directly readable but hidden from recursive listing.
            copy_pack(clone / 'automations/jstack/benny', clone, apply=True)
            output = listing('--full-depth')
            for name in NAMES:
                self.assertNotIn(name, output)
                self.assertTrue((clone / DESTINATION / 'skills' / name / 'SKILL.md').is_file())
            self.assertFalse((clone / 'skills-lock.json').exists())
            self.assertFalse((clone / '.agents/skills').exists())
            # Read actual dependency entrypoints solely from the fresh checkout.
            for name in expected:
                base = clone / ('skills/unslop' if name == 'unslop' else f'skills/jstack/{name}')
                self.assertIn(f'name: {name}', (base / 'SKILL.md').read_text())


if __name__ == '__main__':
    unittest.main()
