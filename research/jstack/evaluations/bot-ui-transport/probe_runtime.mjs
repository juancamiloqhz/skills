// Runs only the pinned pure verifier extracted from a user-specified T3 executable.
// Does not launch T3, read app state, request credentials, or contact a webhook.
import { readFileSync } from "node:fs";
import crypto from "node:crypto";
import vm from "node:vm";
import assert from "node:assert/strict";

const binary = readFileSync(process.argv[2]);
const marker = Buffer.from("//#region src/scheduledTasks/webhookVerification.ts");
const start = binary.indexOf(marker);
const end = binary.indexOf(Buffer.from("var init_webhookVerification"), start);
assert(start >= 0 && end > start, "Runtime verifier section not found; inspect this runtime before updating the probe.");
const source = binary.subarray(start, end).toString("utf8");
const hash = crypto.createHash("sha256").update(source).digest("hex");
assert.equal(hash, "f8f78ec57c6ead5396df95fa4af3eb8d6a9988da1136fbf0478e3f3dacd0be67",
  "Verifier changed; inspect it before running code or updating the recorded contract.");
const verify = vm.runInNewContext(`${source}\nverifyWebhookSignature;`, { NodeCrypto: crypto }, { timeout: 1000 });
const fixture = JSON.parse(readFileSync(0, "utf8"));
const body = Buffer.from(fixture.bodyBase64, "base64");
const signature = { header: "x-jstack-signature", encoding: "hex", prefix: "sha256=" };
const input = { signature, secret: fixture.secret, body, headers: { "x-jstack-signature": fixture.signature } };
assert.equal(verify(input), true, "Sender's actual wire bytes must pass T3's verifier.");
assert.equal(verify({ ...input, headers: {} }), false);
assert.equal(verify({ ...input, secret: "different-public-fixture-key" }), false);
assert.equal(verify({ ...input, body: Buffer.concat([body, Buffer.from("\n")]) }), false);
const parsed = JSON.parse(body.toString("utf8"));
parsed.pr += 1;
assert.equal(verify({ ...input, body: Buffer.from(JSON.stringify(parsed)) }), false);
assert.equal(verify({ ...input, headers: { "x-jstack-signature": "wrong=" + fixture.signature.slice(7) } }), false);
console.log(JSON.stringify({ verifierHash: hash, checks: 6, result: "pass" }));
