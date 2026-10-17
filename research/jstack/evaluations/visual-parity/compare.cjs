// Decode existing screenshots; never write to the supplied images.
const fs = require('node:fs');
const path = require('node:path');
const sharp = require(path.resolve(process.argv[2]));

async function compare(left, right) {
  const [a, b] = await Promise.all([left, right].map(file =>
    sharp(file).ensureAlpha().raw().toBuffer({ resolveWithObject: true })));
  if (a.info.width !== b.info.width || a.info.height !== b.info.height) {
    return { pass: false, reason: 'dimensions differ', left: a.info, right: b.info };
  }
  let changedPixels = 0;
  for (let i = 0; i < a.data.length; i += 4) {
    if (a.data[i] !== b.data[i] || a.data[i + 1] !== b.data[i + 1] ||
        a.data[i + 2] !== b.data[i + 2] || a.data[i + 3] !== b.data[i + 3]) changedPixels++;
  }
  return { pass: changedPixels === 0, changedPixels, width: a.info.width, height: a.info.height };
}

(async () => {
  // Batch manifests bind each pair to an explicit component/state.
  const { expected, pairs } = JSON.parse(fs.readFileSync(process.argv[3], 'utf8'));
  const keys = pairs.map(pair => pair.component + ':' + pair.state).sort();
  if (!expected.length || new Set(expected).size !== expected.length ||
      JSON.stringify(keys) !== JSON.stringify([...expected].sort())) {
    throw new Error('Incomplete or duplicate component/state coverage');
  }
  const results = [];
  for (const pair of pairs) results.push({ component: pair.component, state: pair.state,
    ...(await compare(pair.baseline, pair.actual)) });
  console.log(JSON.stringify(results, null, 2));
  if (results.some(row => !row.pass)) process.exitCode = 1;
})().catch(error => { console.error(error.message); process.exitCode = 2; });
