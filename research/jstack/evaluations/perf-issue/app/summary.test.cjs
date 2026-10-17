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

test('empty iterables do not parse rules regardless of length', () => {
  const events = { length: 3, *[Symbol.iterator]() {} };
  assert.deepEqual(summarize(events, 'invalid'),
    { processed: 3, accepted: 0, rejected: 0, totals: {} });
  const yieldedEvents = {
    length: 0,
    *[Symbol.iterator]() { yield { type: 'sale', amount: 4 }; }
  };
  assert.deepEqual(summarize(yieldedEvents, '{"sale":{"minimum":0,"multiplier":2}}'),
    { processed: 0, accepted: 1, rejected: 0, totals: { sale: 8 } });
});

test('iteration errors precede invalid rules', () => {
  const failure = new Error('iteration failed');
  const events = { *[Symbol.iterator]() { throw failure; } };
  assert.throws(() => summarize(events, 'invalid'), error => error === failure);
});

test('each call uses its own rules and totals', () => {
  const events = [{ type: 'sale', amount: 4 }, { type: 'sale', amount: 7 }];
  assert.deepEqual(summarize(events, '{"sale":{"minimum":0,"multiplier":2}}'),
    { processed: 2, accepted: 2, rejected: 0, totals: { sale: 22 } });
  assert.deepEqual(summarize(events, '{"sale":{"minimum":5,"multiplier":3}}'),
    { processed: 2, accepted: 1, rejected: 1, totals: { sale: 21 } });
});

test('non-string rules can change through coercion between events', () => {
  const documents = [
    '{"sale":{"minimum":0,"multiplier":2}}',
    '{"sale":{"minimum":5,"multiplier":3}}',
    '{"sale":{"minimum":0,"multiplier":-1}}'
  ];
  const rules = { toString() { return documents.shift(); } };
  assert.deepEqual(summarize([
    { type: 'sale', amount: 4 },
    { type: 'sale', amount: 4 },
    { type: 'sale', amount: 7 }
  ], rules), { processed: 3, accepted: 2, rejected: 1, totals: { sale: 1 } });
});

test('non-string rules retain later coercion failures', () => {
  const documents = ['{"sale":{"minimum":0,"multiplier":2}}', 'invalid'];
  const rules = { toString() { return documents.shift(); } };
  assert.throws(() => summarize([
    { type: 'sale', amount: 4 },
    { type: 'sale', amount: 7 }
  ], rules), SyntaxError);
});
