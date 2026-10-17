import { afterEach, expect, it } from "bun:test";
import { chmod, mkdtemp, readFile, rm, writeFile } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { openStore, type Store } from "./store.ts";

const roots: string[] = [];
const stores: Store[] = [];
function handle(root: string): Store {
  const store = openStore(root);
  stores.push(store);
  return store;
}
async function fixture() {
  const root = await mkdtemp(join(tmpdir(), "orch-inbox-"));
  roots.push(root);
  const store = handle(root);
  await store.init();
  await store.units.add({ id: "api", track: "pagination" });
  const pushed = await store.inbox.push({ agent: "task-1", unit: "api", status: "completed", report: "worker.md" });
  const receipt = join(root, "classification.md");
  await writeFile(receipt, "task-1 / api: needs verification; unit state saved.\n");
  return { root, store, pushed, receipt };
}
async function snapshot(root: string) {
  return readFile(join(root, "inbox-batch.json"), "utf8");
}
afterEach(async () => {
  for (const store of stores.splice(0)) await store.close();
  for (const root of roots.splice(0)) {
    await chmod(join(root, "inbox"), 0o700).catch(() => {});
    await rm(root, { recursive: true, force: true });
  }
});

it("recovers the same batch after reopening and init without consuming pointers", async () => {
  const f = await fixture();
  const batch = await f.store.inbox.claim();
  expect(batch?.entries.map((entry) => entry.pointer)).toEqual([f.pushed.pointer]);
  expect(await f.store.inbox.peek()).toEqual([f.pushed.pointer]);
  const before = await snapshot(f.root);
  await f.store.close();
  const resumed = handle(f.root);
  await resumed.init();
  expect(await resumed.inbox.claim()).toEqual(batch);
  expect(await snapshot(f.root)).toBe(before);
  expect((await resumed.units.get("api")).state).toBe("pending");
});

it("keeps later arrivals for the next batch and bounds acknowledgement retries", async () => {
  const f = await fixture();
  const batch = (await f.store.inbox.claim())!;
  const later = await f.store.inbox.push({ agent: "task-2", unit: "ui", status: "completed" });
  expect(await f.store.inbox.claim()).toEqual(batch);
  await f.store.units.set({ id: "api", state: "needs-verify" });
  const ack = await f.store.inbox.ack(batch.id, f.receipt);
  expect(ack.state).toBe("acknowledged");
  expect(ack.receipt?.sha256).toMatch(/^[0-9a-f]{64}$/);
  expect(await f.store.inbox.ack(batch.id, f.receipt)).toEqual(ack);
  expect(await f.store.inbox.peek()).toEqual([later.pointer]);
  const next = (await f.store.inbox.claim())!;
  expect(next.id).not.toBe(batch.id);
  expect(next.entries.map((entry) => entry.pointer)).toEqual([later.pointer]);
  const before = await snapshot(f.root);
  await expect(f.store.inbox.ack(batch.id, f.receipt)).rejects.toThrow("does not match");
  expect(await snapshot(f.root)).toBe(before);
  expect((await f.store.units.get("api")).state).toBe("needs-verify");
});

it("blocks destructive drain while pending and preserves peek/count semantics", async () => {
  const f = await fixture();
  const batch = (await f.store.inbox.claim())!;
  await expect(f.store.inbox.drain()).rejects.toThrow("pending batch");
  expect(await f.store.inbox.count()).toBe(1);
  expect(await f.store.inbox.peek()).toEqual([f.pushed.pointer]);
  await f.store.inbox.ack(batch.id, f.receipt);
  expect(await f.store.inbox.drain()).toEqual([]);
  expect(await f.store.inbox.claim()).toBeNull();
});

it("keeps duplicate notifications distinct instead of pretending to deduplicate task results", async () => {
  const f = await fixture();
  await f.store.inbox.push({ agent: "task-1", unit: "api", status: "completed", report: "worker.md" });
  const batch = (await f.store.inbox.claim())!;
  expect(batch.entries).toHaveLength(2);
  expect(new Set(batch.entries.map((entry) => entry.filename)).size).toBe(2);
});

it("rejects missing, empty and inbox-local receipts without removing pending work", async () => {
  const f = await fixture();
  const batch = (await f.store.inbox.claim())!;
  const before = await snapshot(f.root);
  await expect(f.store.inbox.ack(batch.id, join(f.root, "missing.md"))).rejects.toThrow("cannot read classification receipt");
  await writeFile(f.receipt, " \n");
  await expect(f.store.inbox.ack(batch.id, f.receipt)).rejects.toThrow("must not be empty");
  await expect(f.store.inbox.ack(batch.id, join(f.root, "inbox", f.pushed.filename))).rejects.toThrow("outside the inbox");
  await expect(f.store.inbox.ack(batch.id, join(f.root, "inbox-batch.json"))).rejects.toThrow("outside the inbox");
  expect(await snapshot(f.root)).toBe(before);
  expect(await f.store.inbox.count()).toBe(1);
});

for (const missing of [false, true]) {
  it(`refuses ${missing ? "missing" : "modified"} claimed pointers before acknowledgement`, async () => {
    const f = await fixture();
    const batch = (await f.store.inbox.claim())!;
    const path = join(f.root, "inbox", f.pushed.filename);
    if (missing) await rm(path);
    else await writeFile(path, "changed\n");
    const before = await snapshot(f.root);
    await expect(f.store.inbox.claim()).rejects.toThrow(missing ? "cannot read claimed pointer" : "changed");
    await expect(f.store.inbox.ack(batch.id, f.receipt)).rejects.toThrow(missing ? "cannot read claimed pointer" : "changed");
    expect(await snapshot(f.root)).toBe(before);
  });
}

it("persists acknowledgement before deletion and resumes after a real filesystem refusal", async () => {
  const f = await fixture();
  const batch = (await f.store.inbox.claim())!;
  const inbox = join(f.root, "inbox");
  await chmod(inbox, 0o500);
  try {
    await expect(f.store.inbox.ack(batch.id, f.receipt)).rejects.toThrow();
    expect(JSON.parse(await snapshot(f.root)).state).toBe("acknowledged");
    expect(await f.store.inbox.count()).toBe(1);
  } finally {
    await chmod(inbox, 0o700);
  }
  await f.store.close();
  const resumed = handle(f.root);
  expect(await resumed.inbox.claim()).toBeNull();
  expect(await resumed.inbox.count()).toBe(0);
  expect((await resumed.inbox.ack(batch.id, f.receipt)).state).toBe("acknowledged");
});

it("resumes a partially cleaned acknowledged batch without deleting a later arrival", async () => {
  const f = await fixture();
  const second = await f.store.inbox.push({ agent: "task-2", unit: "tests", status: "completed" });
  const batch = (await f.store.inbox.claim())!;
  await chmod(join(f.root, "inbox"), 0o500);
  try { await expect(f.store.inbox.ack(batch.id, f.receipt)).rejects.toThrow(); }
  finally { await chmod(join(f.root, "inbox"), 0o700); }
  await rm(join(f.root, "inbox", second.filename));
  const later = await f.store.inbox.push({ agent: "task-3", unit: "ui", status: "completed" });
  await f.store.close();
  const resumed = handle(f.root);
  const next = (await resumed.inbox.claim())!;
  expect(next.entries.map((entry) => entry.pointer)).toEqual([later.pointer]);
  expect(await resumed.inbox.count()).toBe(1);
  expect(batch.entries).toHaveLength(2);
});

for (const corruption of ["invalid JSON", "path traversal", "duplicate entry"]) {
  it(`rejects ${corruption} in the batch manifest without deleting pointers`, async () => {
    const f = await fixture();
    const batch = (await f.store.inbox.claim())!;
    const raw = JSON.parse(JSON.stringify(batch));
    if (corruption === "path traversal") raw.entries[0].filename = "../units.tsv";
    if (corruption === "duplicate entry") raw.entries.push(raw.entries[0]);
    await writeFile(join(f.root, "inbox-batch.json"), corruption === "invalid JSON" ? "{" : JSON.stringify(raw));
    await expect(f.store.inbox.claim()).rejects.toThrow("inbox-batch.json");
    await expect(f.store.inbox.ack(batch.id, f.receipt)).rejects.toThrow("inbox-batch.json");
    await expect(f.store.inbox.drain()).rejects.toThrow("inbox-batch.json");
    expect(await f.store.inbox.count()).toBe(1);
    expect((await f.store.units.get("api")).state).toBe("pending");
  });
}

it("uses actual CLI processes to claim, resume, acknowledge and reject a wrong batch", async () => {
  const f = await fixture();
  await f.store.close();
  const run = (...args: string[]) => Bun.spawnSync([
    process.execPath, join(import.meta.dir, "orch.ts"), "--store", f.root, "--json", "inbox", ...args,
  ], { env: process.env });
  const first = run("claim");
  expect({ code: first.exitCode, stderr: first.stderr.toString() }).toEqual({ code: 0, stderr: "" });
  const batch = JSON.parse(first.stdout.toString());
  expect(JSON.parse(run("claim").stdout.toString())).toEqual(batch);
  expect(run("ack", "wrong", "--receipt", f.receipt).exitCode).toBe(1);
  expect(run("ack", batch.id).exitCode).toBe(1);
  expect(JSON.parse(run("ack", batch.id, "--receipt", f.receipt).stdout.toString()).state).toBe("acknowledged");
  expect(JSON.parse(run("claim").stdout.toString())).toBeNull();
});

it("recovers a claimed batch after the actual holder process is killed", async () => {
  const f = await fixture();
  await f.store.close();
  const source = `import { openStore } from ${JSON.stringify(join(import.meta.dir, "store.ts"))};
const store = openStore(${JSON.stringify(f.root)});
const batch = await store.inbox.claim();
console.log(JSON.stringify(batch));
setInterval(() => {}, 1000);`;
  const child = Bun.spawn([process.execPath, "--eval", source], { stdout: "pipe", stderr: "pipe", env: process.env });
  let timer: ReturnType<typeof setTimeout> | undefined;
  try {
    const reader = child.stdout.getReader();
    const first = await Promise.race([
      reader.read(),
      new Promise<never>((_, reject) => { timer = setTimeout(() => reject(new Error("holder did not claim")), 3000); }),
    ]);
    clearTimeout(timer);
    const batch = JSON.parse(new TextDecoder().decode(first.value));
    const contender = handle(f.root);
    await expect(contender.inbox.claim()).rejects.toThrow("store lock held");
    child.kill("SIGKILL");
    await child.exited;
    const resumed = handle(f.root);
    expect(await resumed.inbox.claim()).toEqual(batch);
    expect(await resumed.inbox.count()).toBe(1);
    expect((await resumed.units.get("api")).state).toBe("pending");
    expect((await resumed.inbox.ack(batch.id, f.receipt)).state).toBe("acknowledged");
    expect(await resumed.inbox.count()).toBe(0);
  } finally {
    clearTimeout(timer);
    if (child.exitCode === null) child.kill("SIGKILL");
    await child.exited;
  }
});
