'use strict';
const test = require('node:test');
const assert = require('node:assert/strict');
const { summarize } = require('./summary.cjs');

test('reports all work and weighted category totals', () => {
  assert.deepEqual(summarize([
    { type: 'sale', amount: 12 }, { type: 'sale', amount: 3 },
    { type: 'sale', amount: 5 }, { type: 'refund', amount: 8 },
    { type: 'unknown', amount: 100 }
  ], JSON.stringify({ sale: { minimum: 5, multiplier: 2 }, refund: { minimum: 0, multiplier: -1 } })),
  { processed: 5, accepted: 3, rejected: 2, totals: { sale: 34, refund: -8 } });
});

test('empty batches do not consume rules', () => {
  assert.deepEqual(summarize([], 'invalid'), { processed: 0, accepted: 0, rejected: 0, totals: {} });
});

test('nonempty batches reject invalid rules', () => {
  assert.throws(() => summarize([{ type: 'sale', amount: 12 }], 'invalid'), SyntaxError);
});
