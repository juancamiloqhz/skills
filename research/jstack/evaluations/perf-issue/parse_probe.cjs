'use strict';
const fs = require('node:fs');
const { performance } = require('node:perf_hooks');
const events = JSON.parse(fs.readFileSync(process.argv[3], 'utf8'));
const rules = fs.readFileSync(process.argv[4], 'utf8');
const { summarize } = require(process.argv[2]);
const original = JSON.parse;
let count = 0;
let parseMs = 0;
JSON.parse = function (...args) {
  const start = performance.now();
  try { return original(...args); }
  finally { count++; parseMs += performance.now() - start; }
};
const start = performance.now();
const result = summarize(events, rules);
const summaryMs = performance.now() - start;
JSON.parse = original;
console.log(JSON.stringify({ count, parseMs, summaryMs, processed: result.processed, accepted: result.accepted, rejected: result.rejected }));
