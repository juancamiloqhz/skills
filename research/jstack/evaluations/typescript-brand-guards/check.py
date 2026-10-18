#!/usr/bin/env python3
"""Compile the shipped brand example and exercise validation and nominal separation."""
import argparse
from pathlib import Path
import re
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[4]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--tsc', required=True, type=Path, help='Path to an existing TypeScript lib/tsc.js')
    args = parser.parse_args()
    patterns = (ROOT / 'skills/jstack/jstack-typescript-best-practices/references/patterns.md').read_text()
    brand = next(b for b in re.findall(r'```ts\n(.*?)```', patterns, re.S) if 'type AgentId' in b)
    # The documentation leaves isUUID to the consuming project. This fixture validates UUID-shaped strings.
    support = r'''
function isUUID(input: string): boolean {
  return /^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/i.test(input);
}
function check(value: boolean, message: string): void { if (!value) throw new Error(message); }
'''
    runtime = '''
for (const valid of ["550e8400-e29b-41d4-a716-446655440000", "550E8400-E29B-41D4-A716-446655440000"]) {
  check(isAgentId(valid), "valid guard rejected");
  const parsed: AgentId = parseAgentId(valid);
  check(parsed === valid, "parser changed ID");
  focusAgent(parsed);
  if (isAgentId(valid)) focusAgent(valid);
}
for (const invalid of ["", "agent-1", "550e8400-e29b-41d4-a716-44665544000", "550e8400-e29b-41d4-a716-44665544000z"]) {
  check(!isAgentId(invalid), "invalid guard accepted");
  let rejected = false;
  try { parseAgentId(invalid); } catch (error) { rejected = error instanceof Error; }
  check(rejected, "invalid parser input accepted");
}
console.log("valid and invalid branded-ID runtime cases passed");
'''
    # This is a fixture implementation of the retained numeric-boundary guidance, not shipped runtime code.
    duration = '''
function range(start: Date, durationMs: number): { start: Date; durationMs: number } {
  if (!Number.isFinite(start.getTime()) || !Number.isFinite(durationMs) || durationMs < 0 ||
      !Number.isFinite(new Date(start.getTime() + durationMs).getTime())) throw new Error("invalid range");
  return { start, durationMs };
}
check(range(new Date(0), 0).durationMs === 0, "zero duration lost");
check(range(new Date(0), 250).durationMs === 250, "positive duration lost");
for (const [start, durationMs] of [[new Date(0), -1], [new Date(0), NaN], [new Date(0), Infinity],
  [new Date(NaN), 1], [new Date(8640000000000000), 1]] satisfies [Date, number][]) {
  let rejected = false;
  try { range(start, durationMs); } catch { rejected = true; }
  check(rejected, "invalid numeric/date range accepted");
}
console.log("retained duration-boundary cases passed");
'''
    with tempfile.TemporaryDirectory(prefix='jstack-brands-') as tmp:
        root = Path(tmp)

        def compile_case(name, body, diagnostic=None):
            path = root / (name + '.ts')
            path.write_text(support + body)
            result = subprocess.run(['node', str(args.tsc.resolve()), '--strict', '--noUncheckedIndexedAccess',
                                     '--target', 'ES2022', '--module', 'commonjs', '--noEmitOnError',
                                     '--outDir', str(root / 'out'), str(path)], cwd=root, capture_output=True, text=True)
            output = result.stdout + result.stderr
            if diagnostic is None:
                assert result.returncode == 0, output
            else:
                assert result.returncode != 0 and diagnostic in output, output
            return root / 'out' / (name + '.js')

        positive = compile_case('valid', brand + runtime + duration)
        result = subprocess.run(['node', str(positive)], capture_output=True, text=True)
        assert result.returncode == 0, result.stdout + result.stderr
        print(result.stdout.strip())
        negatives = {
            'raw_string': '\nfocusAgent("550e8400-e29b-41d4-a716-446655440000");',
            'other_brand': '\ntype UserId = string & { readonly __brand: "UserId" };\ndeclare const userId: UserId;\nfocusAgent(userId);',
        }
        for name, caller in negatives.items():
            compile_case(name, brand + caller, 'TS2345')
            print(name + ': rejected with TS2345')
        compile_case('lost_predicate', brand.replace('input is AgentId', 'boolean'), 'TS2322')
        print('lost type predicate: rejected with TS2322')
        lying = compile_case('lying_guard', brand.replace('return isUUID(input);', 'return true;') + runtime)
        result = subprocess.run(['node', str(lying)], capture_output=True, text=True)
        assert result.returncode != 0 and 'invalid guard accepted' in result.stderr, result.stdout + result.stderr
        print('lying guard: compiles but runtime checks reject it')


if __name__ == '__main__':
    main()
