import { afterEach, expect, it } from "bun:test";
import { chmod, mkdir, mkdtemp, readFile, rm, writeFile } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { openStore, type Store } from "./store.ts";

const directories: string[] = [];
const stores: Store[] = [];
const originalPath = process.env.PATH;
const realGit = Bun.which("git")!;

function git(repo: string, ...args: string[]): string {
  const run = Bun.spawnSync([realGit, "-C", repo, ...args]);
  if (run.exitCode !== 0) throw new Error(run.stderr.toString());
  return run.stdout.toString().trim();
}

async function fixture() {
  const root = await mkdtemp(join(tmpdir(), "orch-frontier-"));
  directories.push(root);
  const repo = join(root, "repo");
  const remote = join(root, "origin.git");
  await mkdir(repo);
  git(repo, "init", "--initial-branch=main");
  git(repo, "config", "user.name", "Frontier Test");
  git(repo, "config", "user.email", "frontier@example.invalid");
  await writeFile(join(repo, "base.txt"), "base\n");
  git(repo, "add", ".");
  git(repo, "commit", "-m", "base");
  const base = git(repo, "rev-parse", "HEAD");
  const shas: string[] = [];
  for (const branch of ["stack/api", "stack/ui"]) {
    git(repo, "switch", "-c", branch);
    await writeFile(join(repo, branch.split("/")[1] + ".txt"), branch + "\n");
    git(repo, "add", ".");
    git(repo, "commit", "-m", branch);
    shas.push(git(repo, "rev-parse", "HEAD"));
  }
  git(repo, "init", "--bare", "--initial-branch=main", remote);
  git(repo, "remote", "add", "origin", remote);
  git(repo, "push", "origin", "main", "stack/api", "stack/ui");
  const identity = { full_name: "acme/app" };
  const prs = [
    { number: 10, state: "open", merged: false,
      head: { ref: "stack/api", sha: shas[0], repo: identity },
      base: { ref: "main", sha: base, repo: identity } },
    { number: 11, state: "open", merged: false,
      head: { ref: "stack/ui", sha: shas[1], repo: identity },
      base: { ref: "stack/api", sha: shas[0], repo: identity } },
  ];
  const packet = {
    repository: { full_name: "acme/app", default_branch: "main" },
    origin: "https://github.com/acme/app.git",
    prs,
    invalidJson: false,
    failApi: false,
    changePrOnSecondRead: false,
    changeRemoteOnSecondRead: false,
    badComparison: false,
  };
  const packetPath = join(root, "packet.json");
  const save = () => writeFile(packetPath, JSON.stringify(packet));
  await save();
  const bin = join(root, "bin");
  await mkdir(bin);
  const prelude = `#!${process.execPath}
import { readFileSync, writeFileSync, appendFileSync } from "node:fs";
import { execFileSync } from "node:child_process";
const root = ${JSON.stringify(root)};
const packet = JSON.parse(readFileSync(root + "/packet.json", "utf8"));
const counterPath = root + "/counts.json";
let counts = {};
try { counts = JSON.parse(readFileSync(counterPath, "utf8")); } catch {}
const args = process.argv.slice(2);
const tool = process.argv[1].endsWith("/gh") ? "gh" : "git";
appendFileSync(root + "/calls.jsonl", JSON.stringify({tool,args}) + "\\n");
const count = key => { counts[key] = (counts[key] || 0) + 1; writeFileSync(counterPath, JSON.stringify(counts)); return counts[key]; };
const git = (...args) => execFileSync(${JSON.stringify(realGit)}, ["-C", ${JSON.stringify(repo)}, ...args], {encoding:"utf8"}).trim();
`;
  await writeFile(join(bin, "git"), prelude + `
if (args.join(" ") === "remote get-url origin") console.log(packet.origin);
else {
  if (args[0] === "ls-remote" && count("refs") === 2 && packet.changeRemoteOnSecondRead)
    git("--git-dir=" + ${JSON.stringify(remote)}, "update-ref", "refs/heads/stack/ui", ${JSON.stringify(base)});
  process.stdout.write(execFileSync(${JSON.stringify(realGit)}, args, {cwd:${JSON.stringify(repo)}}));
}
`);
  await writeFile(join(bin, "gh"), prelude + `
if (args.slice(0,5).join(" ") !== "api --hostname github.com --method GET" || args.length !== 6) throw new Error("unexpected API arguments");
if (packet.failApi) { console.error("fixture API unavailable"); process.exit(1); }
if (packet.invalidJson) { console.log("not JSON"); process.exit(0); }
const endpoint = args[5];
if (endpoint === "repos/acme/app") console.log(JSON.stringify(packet.repository));
else if (/^repos\\/acme\\/app\\/pulls\\/\\d+$/.test(endpoint)) {
  const pr = Number(endpoint.split("/").pop());
  const row = packet.prs.find(p => p.number === pr);
  if (!row) throw new Error("unknown fixture PR");
  if (count("pr-" + pr) === 2 && packet.changePrOnSecondRead) row.head.sha = "b".repeat(40);
  console.log(JSON.stringify(row));
} else if (endpoint.startsWith("repos/acme/app/compare/")) {
  const [base, head] = endpoint.split("/").pop().split("...");
  const ancestor = git("merge-base", base, head);
  console.log(JSON.stringify({base_commit:{sha:base},merge_base_commit:{sha:packet.badComparison ? "c".repeat(40) : ancestor},status:ancestor === base ? (base === head ? "identical" : "ahead") : "diverged"}));
} else throw new Error("unexpected endpoint " + endpoint);
`);
  await chmod(join(bin, "git"), 0o755);
  await chmod(join(bin, "gh"), 0o755);
  process.env.PATH = `${bin}:${originalPath}`;
  const storePath = join(root, "store");
  const store = openStore(storePath);
  stores.push(store);
  await store.init();
  return { root, repo, remote, base, shas, packet, save, store, storePath };
}

async function unchangedOnFailure(f: Awaited<ReturnType<typeof fixture>>, message: string, prs = [10, 11]) {
  const before = await readFile(join(f.storePath, "frontier.json"));
  await expect(f.store.frontier.set({ repo: f.repo, prs })).rejects.toThrow(message);
  expect(await readFile(join(f.storePath, "frontier.json"))).toEqual(before);
}

afterEach(async () => {
  process.env.PATH = originalPath;
  for (const store of stores.splice(0)) await store.close();
  for (const directory of directories.splice(0)) await rm(directory, { recursive: true, force: true });
});

it("records published heads despite stale local branches and preserves the store schema", async () => {
  const f = await fixture();
  git(f.repo, "update-ref", "refs/heads/stack/api", f.base);
  const value = await f.store.frontier.set({ repo: f.repo, prs: [10, 11] });
  expect(value).toEqual({ generation: 1, lowestUnmerged: 10, prs: [
    { pr: 10, branches: "stack/api", sha: f.shas[0], state: "OPEN" },
    { pr: 11, branches: "stack/ui", sha: f.shas[1], state: "OPEN" },
  ] });
  expect((await f.store.frontier.set({ repo: f.repo, prs: [10, 11] })).generation).toBe(2);
  const calls = (await readFile(join(f.root, "calls.jsonl"), "utf8")).trim().split("\n").map((line) => JSON.parse(line));
  expect(calls.every((c) => c.tool === "gh" || ["remote", "check-ref-format", "ls-remote"].includes(c.args[0]))).toBe(true);
});

it("accepts a merged prefix and retargeted open root even after the merged branch is deleted", async () => {
  const f = await fixture();
  git(f.repo, "--git-dir=" + f.remote, "update-ref", "refs/heads/main", f.shas[0]!);
  git(f.repo, "--git-dir=" + f.remote, "update-ref", "-d", "refs/heads/stack/api");
  Object.assign(f.packet.prs[0]!, { state: "closed", merged: true });
  f.packet.prs[1]!.base.ref = "main";
  await f.save();
  expect((await f.store.frontier.set({ repo: f.repo, prs: [10, 11] })).lowestUnmerged).toBe(11);
});

it("records an all-merged supplied scope without requiring deleted head refs", async () => {
  const f = await fixture();
  for (const row of f.packet.prs) {
    row.state = "closed"; row.merged = true;
    git(f.repo, "--git-dir=" + f.remote, "update-ref", "-d", "refs/heads/" + row.head.ref);
  }
  git(f.repo, "--git-dir=" + f.remote, "update-ref", "refs/heads/main", f.shas[1]!);
  await f.save();
  expect((await f.store.frontier.set({ repo: f.repo, prs: [10, 11] })).lowestUnmerged).toBeNull();
});

it("requires an explicit nonempty unique PR scope without changing the generation", async () => {
  const f = await fixture();
  await expect(f.store.frontier.set({ repo: f.repo })).rejects.toThrow("set --prs");
  await unchangedOnFailure(f, "set --prs", []);
  await unchangedOnFailure(f, "duplicates", [10, 10]);
  expect((await f.store.frontier.show()).generation).toBe(0);
});

const failures: [string, (f: Awaited<ReturnType<typeof fixture>>) => void, string][] = [
  ["reversed order", () => {}, "unexpected base/head"],
  ["wrong base branch", f => { f.packet.prs[1]!.base.ref = "main"; }, "unexpected base/head"],
  ["stale API head", f => { f.packet.prs[1]!.head.sha = "b".repeat(40); }, "unexpected base/head"],
  ["malformed SHA", f => { f.packet.prs[1]!.head.sha = "b".repeat(41); }, "invalid"],
  ["fork head", f => { f.packet.prs[1]!.head.repo = { full_name: "fork/app" }; }, "cross-repository"],
  ["unknown state", f => { f.packet.prs[0]!.state = "unknown"; }, "invalid"],
  ["closed unmerged link", f => { f.packet.prs[0]!.state = "closed"; }, "closed without merging"],
  ["merged above open link", f => { Object.assign(f.packet.prs[1]!, { state: "closed", merged: true }); }, "merged PRs must precede"],
  ["duplicate branch", f => { f.packet.prs[1]!.head.ref = "stack/api"; }, "must be distinct"],
  ["malformed JSON", f => { f.packet.invalidJson = true; }, "not valid JSON"],
  ["API failure", f => { f.packet.failApi = true; }, "frontier read failed"],
  ["comparison mismatch", f => { f.packet.badComparison = true; }, "does not contain"],
  ["PR changes during inspection", f => { f.packet.changePrOnSecondRead = true; }, "changed during inspection"],
  ["remote changes during inspection", f => { f.packet.changeRemoteOnSecondRead = true; }, "changed during inspection"],
  ["unsupported origin", f => { f.packet.origin = "https://other.example/acme/app.git"; }, "origin remote on github.com"],
  ["repository mismatch", f => { f.packet.repository.full_name = "other/app"; }, "identity does not match"],
];
for (const [name, mutate, error] of failures) {
  it(`retains an existing generation on ${name}`, async () => {
    const f = await fixture();
    await f.store.frontier.set({ repo: f.repo, prs: [10, 11] });
    await writeFile(join(f.root, "counts.json"), "{}");
    mutate(f); await f.save();
    await unchangedOnFailure(f, error, name === "reversed order" ? [11, 10] : [10, 11]);
  });
}

it("rejects a missing published branch without updating the saved frontier", async () => {
  const f = await fixture();
  await f.store.frontier.set({ repo: f.repo, prs: [10, 11] });
  git(f.repo, "--git-dir=" + f.remote, "update-ref", "-d", "refs/heads/stack/ui");
  await unchangedOnFailure(f, "missing published frontier ref");
});

it("rejects matching PR base names when trunk advanced beyond the child's ancestry", async () => {
  const f = await fixture();
  await f.store.frontier.set({ repo: f.repo, prs: [10, 11] });
  git(f.repo, "switch", "main");
  await writeFile(join(f.repo, "later.txt"), "new trunk\n");
  git(f.repo, "add", "."); git(f.repo, "commit", "-m", "trunk moved");
  git(f.repo, "push", "origin", "main");
  f.packet.prs[0]!.base.sha = git(f.repo, "rev-parse", "HEAD");
  await f.save();
  await unchangedOnFailure(f, "does not contain its current parent");
});

it("runs the actual frontier CLI and returns JSON while leaving Git work unchanged", async () => {
  const f = await fixture();
  await f.store.close();
  const before = git(f.repo, "status", "--porcelain=v1");
  const args = [process.execPath, join(import.meta.dir, "orch.ts"), "--store", f.storePath, "--json", "frontier", "set", "--repo", f.repo];
  const missing = Bun.spawnSync(args, { env: process.env });
  expect(missing.exitCode).toBe(1);
  expect(missing.stderr.toString()).toContain("set --prs");
  const good = Bun.spawnSync([...args, "--prs", "10,11"], { env: process.env });
  expect({ code: good.exitCode, stderr: good.stderr.toString() }).toEqual({ code: 0, stderr: "" });
  expect(JSON.parse(good.stdout.toString()).lowestUnmerged).toBe(10);
  expect(git(f.repo, "status", "--porcelain=v1")).toBe(before);
});
