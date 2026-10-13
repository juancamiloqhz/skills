"""Exercise only the invocation guard extracted from the installed Claude binary."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--binary', type=Path, required=True)
args = parser.parse_args()
binary = args.binary.resolve()
version = subprocess.check_output([str(binary), '--version'], text=True).strip()
if version != '2.1.296 (Claude Code)':
    raise SystemExit('This extraction probe is specific to Claude Code 2.1.296; inspect a new version separately.')
data = binary.read_bytes()
start = data.index(b'function Gtt(e,n){')
end = data.index(b'if(h){', start)
prefix = data[start:end].decode()
assert 'userTypedThisTurn:s' in prefix
assert 'if(e.disableModelInvocation&&!s)' in prefix
assert 'reason:"disable_model_invocation"' in prefix
# The remainder implements unrelated permissions. Return a sentinel instead of
# treating a successful passage through this one guard as full invocation.
script = 'const Ro="Skill"; const wXe=()=>"";\n' + prefix + 'return {reason:"passed_this_guard"};}\n'
script += '''
const cases = [];
for (const disabled of [false, true]) {
  for (const typed of [false, true]) {
    const result = Gtt({type:"prompt", disableModelInvocation:disabled},
      {commandName:"fixture", userTypedThisTurn:typed, isMainSession:false});
    cases.push({disableModelInvocation:disabled, userTypedThisTurn:typed, result:result.reason});
  }
}
process.stdout.write(JSON.stringify(cases));
'''
cases = json.loads(subprocess.check_output(['node', '-e', script]))
assert [c['result'] for c in cases] == ['passed_this_guard', 'passed_this_guard', 'disable_model_invocation', 'passed_this_guard']
result = {
    'provider': 'Claude Code', 'version': '2.1.296',
    'binarySha256': hashlib.sha256(data).hexdigest(),
    'extractedGuardSha256': hashlib.sha256(prefix.encode()).hexdigest(),
    'cases': cases,
    'scope': 'Executed the installed invocation guard only, with stubs for error wording and an early success sentinel before other permission checks. No provider session, model call, skill installation or complete invocation.',
}
print(json.dumps(result, indent=2))
