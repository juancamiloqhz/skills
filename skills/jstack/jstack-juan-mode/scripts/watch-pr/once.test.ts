import { expect, it } from "bun:test";
import { main, type CliRuntime } from "./cli.ts";
import { fakeReader, failedCheck, pendingCheck } from "./fakes.test-helper.ts";
import { WatcherQueryError } from "./github.ts";
import type { GitHubReader, PrContext, WatcherVerdict } from "./types.ts";

async function assess(reader: GitHubReader, args: string[] = []) {
  const events: WatcherVerdict[] = [];
  const runtime: CliRuntime = {
    reader,
    clock: {
      now: () => 0,
      observedAt: () => "2026-10-17T00:00:00Z",
      async sleep() { throw new Error("single-pass assessment slept"); },
    },
    stdout: value => events.push(JSON.parse(value)),
    stderr: value => { throw new Error(value); },
  };
  const exitCode = await main(
    ["--owner", "owner", "--repo", "repo", "--pr", "1", "--once", ...args],
    runtime
  );
  return { exitCode, events };
}

it("returns one nonterminal WAITING without sleeping on pending CI", async () => {
  const result = await assess(fakeReader({ fastPath: { kind: "checks", checks: [pendingCheck()] } }));
  expect(result.exitCode).toBe(0);
  expect(result.events).toHaveLength(1);
  expect(result.events[0]).toMatchObject({ kind: "WAITING", terminal: false, reason: { kind: "pending-checks" } });
});

it("returns READY for a settled single PR", async () => {
  const result = await assess(fakeReader());
  expect(result.exitCode).toBe(0);
  expect(result.events.at(-1)).toMatchObject({ kind: "READY", terminal: true });
});

it("does not retry a failed query even with a larger requested error budget", async () => {
  let reads = 0;
  const reader = {
    ...fakeReader(),
    async pullRequest() {
      reads++;
      throw new WatcherQueryError({ kind: "command-exit", retryable: true, code: 1, detail: "rate limited" });
    },
  };
  const result = await assess(reader, ["--max-query-errors", "99"]);
  expect(reads).toBe(1);
  expect(result.exitCode).toBe(7);
  expect(result.events).toHaveLength(1);
  expect(result.events[0]).toMatchObject({ kind: "BLOCKER", blocker: { kind: "status-query", failures: 1 } });
});

it("keeps empty check evidence unavailable instead of ready", async () => {
  const result = await assess(fakeReader({ fastPath: { kind: "checks", checks: [] } }));
  expect(result.exitCode).toBe(7);
  expect(result.events.at(-1)).toMatchObject({ kind: "BLOCKER", blocker: { failure: { kind: "checks-unavailable" } } });
});

it("keeps conflict priority over a thread and failing CI", async () => {
  const result = await assess(fakeReader({
    facts: { mergeable: "CONFLICTING" },
    threads: [{ id: "thread", firstComment: null, isBugbot: false, bugbotReviewPasses: 0 }],
    fastPath: { kind: "checks", checks: [failedCheck()] },
  }));
  expect(result.exitCode).toBe(2);
  expect(result.events.at(-1)).toMatchObject({ kind: "BLOCKER", blocker: { kind: "merge-conflicts" } });
});

it("returns zero for status-only while retaining a conflict in the rows", async () => {
  const result = await assess(fakeReader({ facts: { mergeable: "CONFLICTING" } }), ["--status-only"]);
  expect(result.exitCode).toBe(0);
  expect(result.events[0]).toMatchObject({ kind: "STATUS", rows: [{ facts: { mergeable: "CONFLICTING" } }] });
});

it("does not wait for an upper pending check after the queue frontier clears", async () => {
  const base = fakeReader();
  const result = await assess({
    ...base,
    async checksFastPath(pr: PrContext) {
      return pr.number === 2 ? { kind: "checks", checks: [pendingCheck("upper")] } : base.checksFastPath(pr);
    },
  }, ["--queued-stack", "--stack-prs", "1,2"]);
  expect(result.events.map(event => event.kind)).toEqual(["QUEUE", "STATUS", "WAITING"]);
  expect(result.events.at(-1)).toMatchObject({ kind: "WAITING", frontier: { number: 1 }, reason: { kind: "merge-queue", unmergedCount: 2 } });
});

it("reads the same frozen queue afresh after a frontier merge", async () => {
  const base = fakeReader();
  const read: number[] = [];
  const reader = {
    ...base,
    async pullRequest(pr: PrContext) {
      read.push(pr.number);
      const facts = await base.pullRequest(pr);
      return pr.number === 1 ? { ...facts, state: "MERGED" as const, mergedAt: "now" } : facts;
    },
  };
  const result = await assess(reader, ["--queued-stack", "--stack-prs", "1,2"]);
  expect(read).toEqual([1, 2]);
  expect(result.events.at(-1)).toMatchObject({ kind: "WAITING", frontier: { number: 2 }, reason: { kind: "merge-queue", unmergedCount: 1 } });
});

it("returns COMPLETE when another actor has merged the entire queue", async () => {
  const result = await assess(fakeReader({ facts: { state: "MERGED", mergedAt: "now" } }), ["--queued-stack", "--stack-prs", "1,2"]);
  expect(result.events.at(-1)).toMatchObject({ kind: "COMPLETE", terminal: true, exitCode: 0 });
});

it("reads a changed head on rearm and replaces the previous ready verdict", async () => {
  expect((await assess(fakeReader())).events.at(-1)?.kind).toBe("READY");
  const result = await assess(fakeReader({
    facts: { headRefOid: "new-head", mergeStateStatus: "BLOCKED" },
    commitRollups: [{ oid: "head", state: "SUCCESS" }, { oid: "new-head", state: "FAILURE" }],
  }));
  expect(result.exitCode).toBe(4);
  expect(result.events.at(-1)).toMatchObject({ kind: "BLOCKER", blocker: { ci: { kind: "ci-github-rejected" } } });
});
