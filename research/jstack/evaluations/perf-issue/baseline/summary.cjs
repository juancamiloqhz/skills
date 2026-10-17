'use strict';

function summarize(events, serializedRules) {
  const totals = {};
  let accepted = 0;
  let rejected = 0;
  for (const event of events) {
    const rules = JSON.parse(serializedRules);
    const rule = rules[event.type];
    if (!rule || event.amount < rule.minimum) {
      rejected++;
      continue;
    }
    totals[event.type] = (totals[event.type] || 0) + event.amount * rule.multiplier;
    accepted++;
  }
  return { processed: events.length, accepted, rejected, totals };
}

module.exports = { summarize };
