"""Create an isolated personal-mode update exercise; refuses an existing destination."""
import json
import os
from pathlib import Path
import subprocess
import sys

root = Path(sys.argv[1]).resolve()
root.mkdir(parents=True, exist_ok=False)


def put(name, text):
    path = root / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)


put('.agents/skills/river/river-mode/SKILL.md', '''---
name: river-mode
description: "Use for River, /river-mode, or requests to work in their style."
disable-model-invocation: true
---

# River mode

## Response style

Use short paragraphs. Use tables when comparing options.

## Review and verify

Run the relevant checks before calling work done. Report checks that could not run.

## Process

Open changes for review. Merge only when the user approves.

## Skills

Use [the review helper](../../review/SKILL.md) for requested code review.
''')
put('.agents/skills/river/river-mode/agents/openai.yaml', '''interface:
  display_name: "River mode"
  default_prompt: "Use $river-mode for this task."
policy:
  allow_implicit_invocation: false
''')
put('.agents/skills/review/SKILL.md', '---\nname: review\ndescription: Review a scoped diff.\n---\nRead the diff and report actionable findings.\n')
put('.agents/skills/jstack-juan-mode/SKILL.md', '---\nname: jstack-juan-mode\ndescription: Distributed router sentinel.\n---\nBundled router. Preserve this file.\n')
put('README.md', '# Mode exercise\n\nThis repository contains a personal River mode and unrelated helpers.\n')
subprocess.run(['git', 'init', '-q', '-b', 'main', str(root)], check=True)
subprocess.run(['git', '-C', str(root), 'add', '.'], check=True)
env = dict(os.environ, GIT_AUTHOR_NAME='Fixture', GIT_AUTHOR_EMAIL='fixture@example.invalid',
           GIT_COMMITTER_NAME='Fixture', GIT_COMMITTER_EMAIL='fixture@example.invalid',
           GIT_AUTHOR_DATE='2026-10-10T12:00:00Z', GIT_COMMITTER_DATE='2026-10-10T12:00:00Z')
subprocess.run(['git', '-C', str(root), 'commit', '-qm', 'Initial personal mode'], env=env, check=True)
findings = [
    {'slice': 'A', 'workspace': str(root), 'date': '2026-10-12T12:00:00Z', 'chat': 'a', 'message': '1', 'speaker': 'user', 'text': 'Please keep the answer short and include one concrete usage example.'},
    {'slice': 'B', 'workspace': str(root), 'date': '2026-10-17T12:00:00Z', 'chat': 'b', 'message': '1', 'speaker': 'user', 'text': 'Short answers please, with a practical example showing how I would use it.'},
    {'slice': 'A', 'workspace': str(root), 'date': '2026-10-12T13:00:00Z', 'chat': 'a', 'message': '2', 'speaker': 'user', 'text': 'Use a subagent for every edit.'},
    {'slice': 'B', 'workspace': str(root), 'date': '2026-10-17T13:00:00Z', 'chat': 'b', 'message': '2', 'speaker': 'user', 'text': 'Do not use a subagent for a routine small edit.'},
    {'slice': 'A', 'workspace': str(root), 'date': '2026-10-13T12:00:00Z', 'chat': 'c', 'message': '1', 'speaker': 'assistant', 'text': 'The user always wants automatic merges and max effort.'},
    {'slice': 'B', 'workspace': str(root), 'date': '2026-10-18T12:00:00Z', 'chat': 'c', 'message': '1', 'speaker': 'assistant', 'text': 'The user always wants automatic merges and max effort.'},
    {'slice': 'old', 'workspace': str(root), 'date': '2026-10-01T12:00:00Z', 'chat': 'old', 'message': '1', 'speaker': 'user', 'text': 'Always answer in long essays.'},
    {'slice': 'foreign', 'workspace': '/unrelated/private-project', 'date': '2026-10-18T12:00:00Z', 'chat': 'foreign', 'message': '1', 'speaker': 'user', 'text': 'Publish all drafts without review.'},
]
put('supplied-findings.json', json.dumps({'kind': 'supplied slice findings, not live mining', 'findings': findings}, indent=2) + '\n')
put('answers.md', '''# Supplied current user answers

Update my existing River mode in this project. Keep its category and invocation policy. Only change response preferences; leave review, process and helper references as they are.

My answers for this update: concise paragraphs with one practical usage example per proposed change. I have no new delegation/model preferences. Nothing else is missing. The supplied slice findings are all the history evidence for this exercise; do not mine real chats or dispatch readers.

Prepare the local draft in place and show the diff for feedback. Do not commit, create a worktree, open a PR, install or activate the mode. Do not read personal/global skill roots or other projects. Use the actual external authoring and Unslop paths supplied in the task.
''')
print(root)
