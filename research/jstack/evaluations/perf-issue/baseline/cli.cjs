'use strict';
const fs = require('node:fs');
const { summarize } = require('./summary.cjs');
try {
  const events = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
  const rules = fs.readFileSync(process.argv[3], 'utf8');
  process.stdout.write(JSON.stringify(summarize(events, rules)) + '\n');
} catch (error) {
  process.stderr.write(error.message + '\n');
  process.exitCode = 1;
}
