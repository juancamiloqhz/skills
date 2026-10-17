'use strict';
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const { spawnSync } = require('node:child_process');
const root = __dirname;
const baseline = require('./baseline/summary.cjs');
const fixed = require('./app/summary.cjs');
const directory = path.join(root, process.argv[2]);
fs.mkdirSync(directory, { recursive: false });
assert.deepEqual(Object.keys(fixed), Object.keys(baseline));
assert.equal(fixed.summarize.length, baseline.summarize.length);
let comparisons = 0;
for (let batch = 0; batch < 150; batch++) {
  const events = Array.from({ length: batch % 31 }, (_, index) => ({ type: ['a', 'b', 'c', 'unknown'][index % 4], amount: (index * 19 + batch) % 43 - 10 }));
  const rules = JSON.stringify({ a: { minimum: batch % 7, multiplier: -2 }, b: { minimum: -9, multiplier: 0.5 }, c: { minimum: 20, multiplier: 3 } });
  assert.deepEqual(fixed.summarize(events, rules), baseline.summarize(events, rules));
  comparisons++;
}
for (const serializedRules of ['invalid', 'null', '{}', 'false', '[]', '"text"', '0']) {
  for (const events of [[], [{ type: 'sale', amount: 12 }]]) {
    let expected;
    let actual;
    try { expected = { value: baseline.summarize(events, serializedRules) }; }
    catch (error) { expected = { error: error.constructor.name, message: error.message }; }
    try { actual = { value: fixed.summarize(events, serializedRules) }; }
    catch (error) { actual = { error: error.constructor.name, message: error.message }; }
    assert.deepEqual(actual, expected);
    comparisons++;
  }
}
const cases = [
  { name: 'full', events: '../events.json', rules: '../rules.json' },
  { name: 'empty-invalid', eventValue: '[]', ruleValue: 'invalid' },
  { name: 'invalid-rules', eventValue: '[{"type":"sale","amount":1}]', ruleValue: 'invalid' },
  { name: 'invalid-events', eventValue: 'invalid', ruleValue: '{}' },
  { name: 'null-rules', eventValue: '[{"type":"sale","amount":1}]', ruleValue: 'null' },
  { name: 'missing-events', events: '/tmp/jstack-perf-issue-20261016/absent-input', ruleValue: '{}' },
  { name: 'empty-missing-rules', eventValue: '[]', rules: '/tmp/jstack-perf-issue-20261016/absent-rules' },
  { name: 'missing-arguments', args: [] }
];
for (const fixture of cases) {
  if (fixture.eventValue !== undefined) fs.writeFileSync(path.join(directory, fixture.name + '-events.json'), fixture.eventValue);
  if (fixture.ruleValue !== undefined) fs.writeFileSync(path.join(directory, fixture.name + '-rules.json'), fixture.ruleValue);
  const args = fixture.args || [fixture.events || path.join(directory, fixture.name + '-events.json'), fixture.rules || path.join(directory, fixture.name + '-rules.json')];
  const outputs = [];
  for (const side of ['baseline', 'app']) {
    const command = ['cli.cjs', ...args];
    const result = spawnSync(process.execPath, command, { cwd: path.join(root, side), encoding: 'utf8', timeout: 120000 });
    const record = { side, command: [process.execPath, ...command], cwd: path.join(root, side), exit_code: result.status, signal: result.signal, stdout: result.stdout, stderr: result.stderr, error: result.error && result.error.message };
    fs.writeFileSync(path.join(directory, fixture.name + '-' + side + '.json'), JSON.stringify(record, null, 2));
    assert.equal(result.signal, null);
    assert.equal(result.error, undefined);
    outputs.push({ code: result.status, stdout: result.stdout, stderr: result.stderr });
  }
  assert.deepEqual(outputs[1], outputs[0], fixture.name);
  if (fixture.name === 'full') assert.deepEqual(JSON.parse(outputs[1].stdout), JSON.parse(fs.readFileSync(path.join(root, 'expected.json'), 'utf8')));
}
const result = { commonjsComparisons: comparisons, cliScenarios: cases.length, status: 'pass' };
fs.writeFileSync(path.join(directory, 'summary.json'), JSON.stringify(result, null, 2));
console.log(JSON.stringify(result));
