#!/usr/bin/env python3
"""Compile and run the shipped non-empty guard and selection examples in isolation."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[4]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--tsc', default='/home/ubuntu/Dev/hirejohn/node_modules/typescript/lib/tsc.js')
    args = parser.parse_args()
    source = (ROOT/'skills/jstack/jstack-typescript-best-practices/references/patterns.md').read_text()
    blocks = re.findall(r'```ts\n(.*?)```', source, re.S)
    pick = next(b for b in blocks if 'function pickWinner' in b).split('// Do:', 1)[1]
    pick = '// Do:' + pick
    guard = next(b for b in blocks if 'const isNonEmpty' in b)
    code = 'type NonEmpty<T> = [T, ...T[]];\n'+pick+'\n'+guard+'''
function check(ok: boolean, message: string): void { if (!ok) throw new Error(message); }
check(!isNonEmpty<string>([]), "empty rejected");
check(!isNonEmpty(Array<string>(1)), "head hole rejected");
const dense = ["a", "b"];
check(isNonEmpty(dense), "dense accepted");
const random = Math.random;
try {
  if (isNonEmpty(dense)) {
    Math.random = () => 0;
    check(pickWinner(dense) === "a", "first selection");
    Math.random = () => 0.999;
    check(pickWinner(dense) === "b", "last selection");
  }
  check(pickWinner(["only"]) === "only", "singleton selection");
  const laterHole = ["head"];
  laterHole.length = 2;
  if (isNonEmpty(laterHole)) {
    check(pickWinner(laterHole) === "head", "unchecked later index uses valid head");
  }
} finally { Math.random = random; }
console.log("7 guard and selection assertions passed");
'''
    with tempfile.TemporaryDirectory(prefix='jstack-ts-replay-') as tmp:
        p = Path(tmp); (p/'examples.ts').write_text(code)
        records = []
        for command in [['node', args.tsc, '--strict', '--noUncheckedIndexedAccess', '--target', 'ES2022',
                         '--module', 'commonjs', '--outDir', str(p/'out'), str(p/'examples.ts')],
                        ['node', str(p/'out/examples.js')]]:
            result = subprocess.run(command, cwd=p, text=True, capture_output=True)
            records.append({'command': command, 'exitCode': result.returncode, 'stdout': result.stdout, 'stderr': result.stderr})
            assert result.returncode == 0, records
    print(json.dumps({'patternsSha256': hashlib.sha256(source.encode()).hexdigest(), 'extractedSourceAndAssertions': code,
                      'results': records}, indent=2))


if __name__ == '__main__':
    main()
