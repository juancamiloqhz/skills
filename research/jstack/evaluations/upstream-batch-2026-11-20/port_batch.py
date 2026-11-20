#!/usr/bin/env python3
"""Port the 2026-11-20 batch from pstack at H into jstack, applying only recorded adaptations.

Usage: python3 -B port_batch.py <jstack-checkout> [--check]
With --check, exit 1 if any ported file differs from the expected result. Reads source objects from the
checker cache (JSTACK_UPSTREAM_GIT_DIR, default ~/.cache/jstack/upstream/upstream.git); never fetches.
Each substitution must match exactly once, so a moved or changed source sentence fails loudly.
"""
import os, re, subprocess, sys
from pathlib import Path

GIT = ["git", "--git-dir=" + os.environ.get("JSTACK_UPSTREAM_GIT_DIR",
       os.path.expanduser("~/.cache/jstack/upstream/upstream.git"))]
H = "aaeb0ea3a0584995aa8f55ce44c6c5259414b896"
root = Path(sys.argv[1])
check = "--check" in sys.argv

AUTH = ("Apply within the requested scope and existing authorization, preserving unrelated work and "
        "repository constraints. Direct invocation does not activate jstack-juan-mode or change model configuration.")
DISCOVER = ("Discover referenced skills through the current catalog and read their advertised paths; independently "
            "installed packages need not be siblings. Verify jstack identity when available and report ambiguity. "
            "If a required helper is unavailable, report the missing dependency and incomplete procedure, continue "
            "independent authorized work, and leave installation to the user.")

def src(path):
    return subprocess.run(GIT + ["show", f"{H}:{path}"], check=True, capture_output=True, text=True).stdout

def sub(text, old, new, count=1):
    n = text.count(old)
    if n != count:
        raise SystemExit(f"expected {count} match(es), found {n}: {old[:80]!r}")
    return text.replace(old, new)

def packaging(text, name):
    text = sub(text, f"name: {name}\n", f"name: jstack-{name}\n")
    text = sub(text, "disable-model-invocation: true\n", "")
    return text

def append(text, *paras):
    return text.rstrip("\n") + "\n\n" + "\n\n".join(paras) + "\n"

out = {}

PRINCIPLES = ["attack-the-premise", "boundary-discipline", "build-the-lever", "explain-the-number",
              "fix-root-causes", "foundational-thinking", "make-operations-idempotent", "minimize-reader-load",
              "model-the-domain", "prove-it-works", "separate-before-serializing-shared-state",
              "sequence-verifiable-units", "test-behavior-not-implementation", "type-system-discipline"]
for p in PRINCIPLES:
    name = f"principle-{p}"
    t = packaging(src(f"pstack/skills/{name}/SKILL.md"), name)
    refs = False
    if p == "boundary-discipline":
        t = sub(t, "Inside, trust the types: no re-validation",
                "Inside, trust the types where boundary validation and maintained invariants establish their "
                "guarantees: no re-validation")
        t = sub(t, "Is this data crossing a boundary right now? If not, the validation is redundant.",
                "Is this data crossing a boundary right now? If not, avoid repeating an already established check. "
                "A new authorization decision, concurrent mutation, or stale external state can require a fresh "
                "check even inside the process.")
    if p == "make-operations-idempotent":
        t = sub(t, "Write to a temporary path and rename it into place.\n",
                "Write to a temporary path and rename it into place. For a process-owned lock, check process "
                "identity and liveness before treating it as stale; a PID alone can be reused.\n")
    if p == "sequence-verifiable-units":
        t = sub(t, "Each commit lands on its own.",
                "Each delivery unit must pass its required checks before landing. Preserve failing-test evidence "
                "without presenting a red commit as independently merge-ready. Merging remains separately authorized.")
    if p == "explain-the-number":
        t = sub(t, "run the [benchmark-checklist](../benchmark-checklist/SKILL.md) skill",
                "run the **jstack-benchmark-checklist** (`jstack-benchmark-checklist`) skill")
        refs = True
    if p == "type-system-discipline":
        t = sub(t, "**typescript-best-practices** skill", "**jstack-typescript-best-practices** skill")
        refs = True
    if re.search(r"\]\(\.\./|\*\*[a-z-]+\*\* skill", t.replace("jstack-", "")) and not refs:
        raise SystemExit(f"unhandled skill reference in {p}")
    out[f"skills/jstack/jstack-{name}/SKILL.md"] = append(t, AUTH, DISCOVER) if refs else append(t, AUTH)

# Technical writing
t = packaging(src("pstack/skills/technical-writing/SKILL.md"), "technical-writing")
t = sub(t, "Use for /technical-writing", "Use for /jstack-technical-writing")
t = sub(t, "Write so a tired engineer understands on the first read.\n",
        "Write so a tired engineer understands on the first read.\n\n"
        "Run directly or through a calling workflow within the requested writing or review scope. A review request "
        "returns findings unless edits are authorized. Preserve factual uncertainty, literal code, and required "
        "repository or host templates. This skill does not activate jstack-juan-mode or authorize publication, "
        "installation, or configuration changes.\n")
t = sub(t, "formatting tells.\n",
        "formatting tells. Discover the intended pstack Unslop through the current catalog or an explicit authoring "
        "path and read it in full. Check content equivalence before using another same-name package. Respect host "
        "invocation restrictions; if the dependency is missing, ambiguous, or blocked, report the writing check "
        "incomplete rather than installing, substituting, or bypassing the restriction.\n")
t = sub(t, "Indent code snippets with tabs.",
        "Indent code snippets with tabs unless the language syntax or repository conventions require different "
        "indentation.")
out["skills/jstack/jstack-technical-writing/SKILL.md"] = t

# Sharpen: source-exact body with jstack naming
t = src("pstack/skills/sharpen/SKILL.md")
t = sub(t, "name: sharpen\n", "name: jstack-sharpen\n")
t = sub(t, "Use for /sharpen.", "Use for /jstack-sharpen.")
out["skills/jstack/jstack-sharpen/SKILL.md"] = t

# Local-only edits applied to current jstack text
def local(path, *pairs):
    t = (root / path).read_text()
    for old, new in pairs:
        if new in t and old not in t:
            continue  # already applied
        t = sub(t, old, new)
    out[path] = t

local("skills/jstack/jstack-sharpen/agents/openai.yaml",
      ("with expert methods and an outside check, leaving my choices open.",
       "with expert methods and an outside check, prototyping choices an experiment can settle and leaving my "
       "preference choices open."))
local("skills/jstack/jstack-benchmark-checklist/SKILL.md",
      ("- Keep a PR body to one primary number, per the **Opening a PR** playbook. Put",
       "- Keep a PR body to one primary number. Put"),
      ("The named playbooks are separate Juan-mode procedures. Perf issue and Hillclimb are available; Opening a PR "
       "remains unavailable in jstack. Apply",
       "The named playbooks are separate Juan-mode procedures; Perf issue and Hillclimb are available. Apply"))
local("skills/jstack/jstack-juan-mode/playbooks/autonomous-run.md",
      ("4. Mid-run discoveries are yours.", "4. Mid-run discoveries that support the goal are yours."))
local("skills/jstack/jstack-juan-mode/SKILL.md",
      ("- **Explain the Number.** Before you trust, report, or act on a number you measured",
       "- **Explain the Number.** Apply before you measure, and before you trust, report, or act on a number you "
       "measured"))

changed = 0
for rel, text in out.items():
    p = root / rel
    if p.read_text() != text:
        changed += 1
        if not check:
            p.write_text(text)
print(f"{len(out)} files ported, {changed} {'would change' if check else 'changed'}")
sys.exit(1 if check and changed else 0)
