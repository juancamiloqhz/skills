import assert from "node:assert/strict";
import { spawnSync } from "node:child_process";
import { copyFileSync, mkdirSync, mkdtempSync, readFileSync, rmSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import test from "node:test";

const checker = fileURLToPath(new URL("check_docs.mjs", import.meta.url));
const mode = "skills/jstack/jstack-juan-mode/SKILL.md";

function fixture(t) {
  const root = mkdtempSync(join(tmpdir(), "jstack-docs-"));
  t.after(() => rmSync(root, { recursive: true, force: true }));
  const write = (path, text) => {
    mkdirSync(dirname(join(root, path)), { recursive: true });
    writeFileSync(join(root, path), text);
  };
  const append = (path, text) => write(path, readFileSync(join(root, path), "utf8") + "\n" + text);
  write("scripts/jstack/check_docs.mjs", "");
  copyFileSync(checker, join(root, "scripts/jstack/check_docs.mjs"));
  const names = ["jstack-juan-mode", "jstack-how", "jstack-principle-prove-it-works"];
  for (const name of names) write(`skills/jstack/${name}/SKILL.md`, `# ${name}\n`);
  write(mode, "[Feature](playbooks/feature.md)\n[Bug fix](playbooks/bug-fix.md)\n");
  for (const name of ["feature", "bug-fix"]) write(`skills/jstack/jstack-juan-mode/playbooks/${name}.md`, `# ${name}\n`);
  write("README.md", names.map((name) => `[${name}](./skills/jstack/${name})`).join("\n") + "\nAll two playbooks. The three skills. One short principles.\n");
  write("research/jstack/README.md", "# Current status\nJstack ships 3 packages and all 2 Juan-mode playbook procedures.\n");
  write("research/jstack/guide/start.md", "# Start\nUse /jstack-how or $jstack-how. Install with `--skill jstack-how`.\n[Status](../README.md#current-status)\n");
  const run = () => spawnSync(process.execPath, [join(root, "scripts/jstack/check_docs.mjs")], { encoding: "utf8", cwd: tmpdir() });
  const remove = (path) => rmSync(join(root, path), { recursive: true, force: true });
  return { write, append, run, remove };
}

function fails(result, pattern) {
  assert.equal(result.status, 1, result.stdout + result.stderr);
  assert.match(result.stdout, pattern);
}

test("valid catalog, whole counts, subset counts and current command forms pass", (t) => {
  const f = fixture(t);
  f.append("README.md", "One playbooks example. These 1 jstack skills are a subset. `jstack-principle-*` is a pattern.");
  const result = f.run();
  assert.equal(result.status, 0, result.stdout + result.stderr);
  assert.match(result.stdout, /3 skills \(2 commands, 1 principles\), 2 playbooks/);
  assert.match(result.stdout, /0 problems/);
});

for (const claim of ["All 23 playbooks", "The twenty-three playbooks", "All 23 procedures", "All 23 playbook procedures", "All 23 Juan-mode playbook procedures", "Jstack ships 45 packages", "The 24 principles"]) {
  test(`rejects stale count: ${claim}`, (t) => {
    const f = fixture(t);
    f.append("research/jstack/README.md", claim);
    fails(f.run(), /research\/jstack\/README.md:4 says .*but the tree has/);
  });
}

for (const mention of ["/jstack-missing", "$jstack-missing", "`jstack-missing`", "--skill jstack-missing"]) {
  test(`rejects nonexistent helper: ${mention}`, (t) => {
    const f = fixture(t);
    f.append("research/jstack/guide/start.md", mention);
    fails(f.run(), /names jstack-missing, which no shipped skill provides/);
  });
}

test("checks guide anchors, including repeated and formatted headings", (t) => {
  const f = fixture(t);
  f.append("research/jstack/README.md", "## **Déjà** vu\n## **Déjà** vu\n```md\n# Example only\n```\n");
  f.append("research/jstack/guide/start.md", "[Repeat](../README.md#déjà-vu-1)");
  assert.equal(f.run().status, 0);
  f.append("research/jstack/guide/start.md", "[Wrong](../README.md#example-only)");
  fails(f.run(), /has no heading with that anchor/);
});

test("rejects missing local documents but leaves remote URLs unchecked", (t) => {
  const f = fixture(t);
  f.append("README.md", "[Web](https://example.invalid/missing#heading)");
  assert.equal(f.run().status, 0);
  f.append("README.md", "[Missing](research/jstack/missing.md)");
  fails(f.run(), /links to research\/jstack\/missing.md, which does not exist/);
});

test("requires catalog links even when a skill is named elsewhere", (t) => {
  const f = fixture(t);
  f.write("README.md", "`jstack-juan-mode` `jstack-how` `jstack-principle-prove-it-works`");
  fails(f.run(), /README.md does not link skill jstack-how/);
});

test("requires all shipped playbooks in the mode index", (t) => {
  const f = fixture(t);
  f.write(mode, "[Feature](playbooks/feature.md)");
  fails(f.run(), /does not list playbook bug-fix/);
});

test("rejects nonexistent playbooks in the mode index", (t) => {
  const f = fixture(t);
  f.append(mode, "[Missing](playbooks/missing.md)");
  fails(f.run(), /links to playbooks\/missing.md, which does not exist/);
});

test("historical reports retain their original counts and names", (t) => {
  const f = fixture(t);
  f.write("research/jstack/evaluations/old/README.md", "All 99 playbooks. Use /jstack-missing. [Old](missing.md#gone)");
  assert.equal(f.run().status, 0);
});

test("a missing guide is disclosed without blocking the current-doc check", (t) => {
  const f = fixture(t);
  f.remove("research/jstack/guide");
  const result = f.run();
  assert.equal(result.status, 0, result.stdout + result.stderr);
  assert.match(result.stdout, /no guide pages present; guide coverage remains pending/);
});

test("allows other repository skills without treating them as jstack packages", (t) => {
  const f = fixture(t);
  f.write("skills/agent-instructions/SKILL.md", "# Agent instructions");
  f.append("README.md", "Install with `--skill agent-instructions`.");
  const result = f.run();
  assert.equal(result.status, 0, result.stdout + result.stderr);
  assert.match(result.stdout, /tree: 3 skills/);
});
