#!/usr/bin/env python3
"""Replay retained fixture behavior and check reviewer/parent edit boundaries."""
import ast
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import tokenize

ROOT = Path(__file__).resolve().parent


def tokens(text):
    return [(t.type, t.string) for t in tokenize.generate_tokens(io.StringIO(text).readline)
            if t.type not in (tokenize.COMMENT, tokenize.NL)]


def comments(text):
    return [t.string for t in tokenize.generate_tokens(io.StringIO(text).readline)
            if t.type == tokenize.COMMENT]


def main():
    cleanup = json.loads((ROOT/'cleanup-evidence.json').read_text())['files']
    boundary = json.loads((ROOT/'boundary-evidence.json').read_text())['files']
    before = cleanup['before/invoice.py']
    reviewer = cleanup['review-round-1/invoice.py']
    after = cleanup['invoice.py']
    assert tokens(before) == tokens(reviewer)
    assert ast.dump(ast.parse(before)) == ast.dump(ast.parse(reviewer))
    assert len(comments(before))-len(comments(reviewer)) == 4
    assert comments(after) == comments(reviewer)
    for marker in ['# Copyright 2026 Example Authors. MIT License.',
                   '# AGENT-CONTRACT: keep this marker for the repository scanner.',
                   '# The vendor protocol requires a trailing ASCII unit separator.',
                   '"""Return the public wire field for an invoice label."""']:
        assert marker in before and marker in reviewer and marker in after
    records = []
    for stage, text in [('before', before), ('reviewer', reviewer), ('after', after)]:
        with tempfile.TemporaryDirectory(prefix='jstack-comments-replay-') as directory:
            p = Path(directory)
            (p/'invoice.py').write_text(text)
            (p/'check.py').write_text(cleanup['check.py'])
            result = subprocess.run([sys.executable, '-B', 'check.py'], cwd=p, text=True, capture_output=True)
            if stage == 'after':
                assert result.returncode == 0 and '4 behavior assertions passed' in result.stdout
            else:
                assert result.returncode != 0 and 'TypeError' in result.stderr
            records.append({'stage': stage, 'exitCode': result.returncode,
                            'stdout': result.stdout, 'stderr': result.stderr})
    for case, file in [('A', 'f.py'), ('C', 'bridge.py')]:
        assert boundary[f'{case}/input/{file}'] == boundary[f'{case}/working/{file}']
    old, new = boundary['B/input/label.py'], boundary['B/working/label.py']
    assert tokens(old) == tokens(new)
    assert len(comments(old))-len(comments(new)) == 1
    assert ast.dump(ast.parse(old)) == ast.dump(ast.parse(new))
    for case in ['A', 'B', 'C']:
        result = json.loads(boundary[f'{case}/result.json'])
        assert result['encodings'] == []
    print(json.dumps({'reviewerNonCommentTokensAndAstUnchanged': True, 'protectedCommentsRetained': True,
                      'acceptedCommentDeletions': 4, 'fixtureBehavior': records,
                      'boundaryAandCUnchanged': True, 'boundaryBCommentOnlyDeletion': True,
                      'boundaryEncodingsApplied': 0}, indent=2))


if __name__ == '__main__':
    main()
